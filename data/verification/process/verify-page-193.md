# Verification process log — verify-page-193


## [2026-09-06T02:14:33.077Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 193 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-193.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-193.json. Write /home/sfmqrb/git/rishe/data/verification/page-193.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 193` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T02:14:34.686Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T02:14:35.397Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T02:14:35.408Z] TOOL RESULT

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
226	```json
227	{
228	  "pdf_page": 126,
229	  "book_page": 96,
230	  "verified_by": "claude-opus-5",
231	  "verified_on": "2026-09-05",
232	  "entries": [
233	    {
234	      "entry": 0,
235	      "root": "Dheigh, Dhigha",
236	      "verdict": "confirmed",
237	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
238	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
239	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
240	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
241	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
242	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
243	      "nodes": [
244	        {
245	          "id": 6,
246	          "lang": "Avestan",
247	          "words": "pairi-daeza",
248	          "verdict": "confirmed",
249	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
250	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
251	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
252	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
253	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
254	        }
255	      ]
256	    }
257	  ]
258	}
259	```
260	
261	Rules:
262	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
263	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
264	- `words` = the transliterations of the node joined by "; " (copy from the chart).
265	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
266	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
267	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
268	- If a node lists several words, cover each word; if they differ in verdict, use the worst
269	  verdict for the node and explain per word in `derivation`.
270	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
271	  scholarship takes.
272	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
273	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
274	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
275	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
276	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
277	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
278	  any extraction errors (JSON differs from the printed page) the owner must fix.
279	  Do not paste the JSON back into your reply.
280	
```


## [2026-09-06T02:14:35.825Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-193.txt"
}
```


### [2026-09-06T02:14:35.835Z] TOOL RESULT

```
1	=== PDF page 193 (book page 163) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gheugh, Ghŭgh : to hide, conceal  (refs POK:450)
4	#1 (parent #0) [Old Persian] refs=POK:450; KNT:182; SOD:50; SYN:852 | gaud : to hide ; â-gaud : cover ; apa-gaudaya : to uncover ☞Apo
5	  #2 (parent #1) [Sogdian] refs=SOD:3,5 | â-gaud, `g`wd : cover, barn, shelter ; `g`wnd : to cover
6	    #3 (parent #2) [Persian] refs=MON:68; SOD:3 | âğol «آغل» : barn | extra: آغیل ، آغال
7	#4 (parent #0) [Avestan] refs=POK:450; KNT:182; SYN:852 | guz, gaoz : to conceal ; fra-gauzayanta : to conceal
8	#5 (parent #0) [Sanskrit] refs=POK:450; KNT:182 | gŭhati : conceals
9	--- entry 1 ---
10	ROOT Ghi -> redirect to Ghei 1
11	--- entry 2 ---
12	ROOT Ğhî -> redirect to Ghĕi
13	--- entry 3 ---
14	ROOT Ğhiâ -> redirect to Ghĕi
15	--- entry 4 ---
16	ROOT Ghiem -> redirect to Ghei 1
17	--- entry 5 ---
18	ROOT Ghies -> redirect to Ghdies
19	--- entry 6 ---
20	ROOT Ghi-ghe-me -> redirect to Ghě 1
21	--- entry 7 ---
22	ROOT [Indo-European] Ghlâd : to sound, to ring  (refs POK:451)
23	#1 (parent #0) [Avestan] refs=POK:451 | zrâda : linked armor
24	  #2 (parent #1) [Pahlavi] refs=VDQ:257 | zrih
25	    #3 (parent #2) [Persian] refs=POK:451; HRN:146; BQT:1019 | zereh «زره» : armor
26	#4 (parent #0) [Arabic] refs=VDQ:257 | zard, sarad : armor ; zarrâd : armor maker
27	  #5 (parent #4) [Persian] refs=MON:1729 | zarrâd «زرّاد» : armor maker | extra: زرّادخانه ، زرّادگاه
28	#6 (parent #0) [Indo-European] refs=POK:439,451 | Gher 2 : to call out
29	  #7 (parent #6) [Germanic] refs=AHD | grĕtan : to moan ; grôtjan : to speak
30	    #8 (parent #7) [English] refs=None | regret ; greet
31	--- entry 8 ---
32	ROOT Ghordho -> redirect to Gher 1
33	--- entry 9 ---
34	ROOT Ghosh -> redirect to Ôus 1
35	--- entry 10 ---
36	ROOT Ghosto -> redirect to Ghesto
37	
```


## [2026-09-06T02:14:38.979Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-193.json",
 "description": "Read source JSON for page 193"
}
```


### [2026-09-06T02:14:39.045Z] TOOL RESULT

```
{
  "pdf_page": 193,
  "book_page": 163,
  "entries": [
    {
      "root": {
        "name": "Gheugh, Ghŭgh",
        "lang": "Indo-European",
        "refs": "POK:450",
        "gloss": "to hide, conceal"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:450; KNT:182; SOD:50; SYN:852",
          "words": [
            {"translit": "gaud", "gloss": "to hide", "script": null},
            {"translit": "â-gaud", "gloss": "cover", "script": null},
            {"translit": "apa-gaudaya", "gloss": "to uncover", "script": null, "see": ["Apo"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:3,5",
          "words": [
            {"translit": "â-gaud, `g`wd", "gloss": "cover, barn, shelter", "script": null},
            {"translit": "`g`wnd", "gloss": "to cover", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:68; SOD:3",
          "words": [
            {"translit": "âğol", "gloss": "barn", "script": "آغل"}
          ],
          "script_extra": "آغیل ، آغال",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:450; KNT:182; SYN:852",
          "words": [
            {"translit": "guz, gaoz", "gloss": "to conceal", "script": null},
            {"translit": "fra-gauzayanta", "gloss": "to conceal", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:450; KNT:182",
          "words": [
            {"translit": "gŭhati", "gloss": "conceals", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {"root": {"name": "Ghi", "redirect": "Ghei 1"}, "nodes": []},
    {"root": {"name": "Ğhî", "redirect": "Ghĕi"}, "nodes": []},
    {"root": {"name": "Ğhiâ", "redirect": "Ghĕi"}, "nodes": []},
    {"root": {"name": "Ghiem", "redirect": "Ghei 1"}, "nodes": []},
    {"root": {"name": "Ghies", "redirect": "Ghdies"}, "nodes": []},
    {"root": {"name": "Ghi-ghe-me", "redirect": "Ghě 1"}, "nodes": []},
    {
      "root": {
        "name": "Ghlâd",
        "lang": "Indo-European",
        "refs": "POK:451",
        "gloss": "to sound, to ring"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:451",
          "words": [
            {"translit": "zrâda", "gloss": "linked armor", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "VDQ:257",
          "words": [
            {"translit": "zrih", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "POK:451; HRN:146; BQT:1019",
          "words": [
            {"translit": "zereh", "gloss": "armor", "script": "زره"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Arabic",
          "refs": "VDQ:257",
          "words": [
            {"translit": "zard, sarad", "gloss": "armor", "script": null},
            {"translit": "zarrâd", "gloss": "armor maker", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:1729",
          "words": [
            {"translit": "zarrâd", "gloss": "armor maker", "script": "زرّاد"}
          ],
          "script_extra": "زرّادخانه ، زرّادگاه",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "POK:439,451",
          "words": [
            {"translit": "Gher 2", "gloss": "to call out", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "grĕtan", "gloss": "to moan", "script": null},
            {"translit": "grôtjan", "gloss": "to speak", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "regret", "gloss": null, "script": null},
            {"translit": "greet", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {"root": {"name": "Ghordho", "redirect": "Gher 1"}, "nodes": []},
    {"root": {"name": "Ghosh", "redirect": "Ôus 1"}, "nodes": []},
    {"root": {"name": "Ghosto", "redirect": "Ghesto"}, "nodes": []}
  ]
}
```


## [2026-09-06T02:14:39.324Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T02:14:39.368Z] TOOL RESULT

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


## [2026-09-06T02:14:45.138Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60; echo ---; grep -n \"geu\\|gheugh\\|ghū̆gh\\|guz-\\|gūh\" POK_full.txt | head -40",
 "description": "List refs and grep Pokorny"
}
```


### [2026-09-06T02:14:45.207Z] TOOL RESULT

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
---
14791:blagettan, bl^gettan^ccy', ndd. blageu. "kid, child'; Middle High German bleren, blerren 
16042:Material: Zigeun. buzn/'goat'; Avestan buzam. "he-goaf, npers. buz'goat, he-goat; billy 
30859:Slavic *ggz- {a\so *guz-\N'\t\r\ i/from Indo Germanic ^ei/-^-, see be\o\N geu-f) in serb. 
30873:for the Slavic mixture from *gong- and *geug-, gug- (extension from geu- "crook', see 
30875:Lithuanian guzas "knag' and for Baltic gunz-, guz- formation from such nasalized *gu-n-g- 
30878:parallel extension *geu-g-, compare under ^ei/-/.' Lithuanian guga^ bump in saddle, hump, 
31708:Irish guar coa\' (< *geulo- or * goulo); 
31753:Root / lemma: geu-, gau-, gu-{*sgeu-) 
31759:Root/ lemma: geu- gsu- gu-\ to bend, curl; a kind of vessel probably derived from Root/ 
31822:gu-t-, geu-t-\ about gu-et-see distinctive article; ^'^//'-/"throat'. 
31831:geut- in Old English ceod(a)m. "sack, bag, pouch ', Old High German kiotds.. Middle 
31917:with Baltic {gunz-) guz- as gunzys, guzys " crop by birds, head of the femur ' etc.; s. 
31925:about that from Slavic guz- not certainly to separative ggz- see below geng-. 
32008:d. With Asuffixes; geu-/o-s' round vessel'. 
32054:f. With /--suffixes; geu-ro-s, gou-ro-s, gu-ro-s, gur-no-s. 
32116:crooked, humped ', yet au is also difficult, because an ablaut *geu- : gdu-'\n spite of the 
32138:gevelm., acorn. geuel-hoern<^\. A pair of snuffers), (gall-)Latin gabalus^ cross, gallows '; 
32334:mcymr. geu, ncymr. gau' incorrect ', Subst. "lie, falsity', corn. gowm. ds., bret. gaou ds.; 
32335:derived mcymr. geuawc, ncymr. ei/o^ "culpable'. 
32338:back to Indo Germanic *gdu- (to geu- "bend', S. 393). compare to vocalism Pokorny 
33234:Root / lemma: gheugh-, ghugh- 
33244:Avestan guz- {guzaeta, fra-guzayanta) "conceal, hide', Old pers. yadiy apa-gaudayahr 
34386:See also: see also under geu-1. 
34415:'cottage' (above geu-S. 394); 
34709:Note: (extension from geu- 'bend'? see there) 
35683:Root / lemma: geus- 
35702:alb. deshal loved', present do, dua{*geus-n-, Jokl IF. 37, 101 f.); 
35710:doroigu^ elegit ' {*to-ro-gi-geus-t), Pokorny IF. 35, 177 ff., etc. (see Pedersen aaO.); 
35743:Root / lemma: geu- geua- (besides geus^ 
37483:', Modern High German vergeuden; Old High German inginnan^ open up, open, lacerate, 
41638:labialized laryngeal hreu- > Proto Greek yeu- > geu- > Greek zu- 
43551:abret. //7/cc»^ca/7/ "complete'; mcymr. yn geuganf6s. (actually "very skillful ' from *kouo- 
46753:Note: Numerous parallel formations from the root geu-see there, compare esp. the 
55838:Material: Old Irish lu(i)geu., cymr. Ilwm., bret. /e'oath, vow, pledge' {*lughiom)\ 
62190:dviypoq " Ka9apT0(; '; Latin noegeum ( *noig"-io-) " Schweif^tuch '; common Old Indie gh- > 
63697:auga. Old High German ouga. Old English eageu. 'eye'; stem *augja-\n Gothic and-augi 
77520:Old Church Slavic skgdb^arm, small'; russ. scedryj^ generous ' ('*vergeudend, sein Gut 
78915:Irish snigid^ it drips, is raining ', snigeu. "drip, flux ', snechtfaje ' snow' (to /-forms 
92836:'lowland, depression, meadow', corn, goen, goon, gon, bret. geun, ye^/7 'marshland'
```


## [2026-09-06T02:14:47.439Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','SOD','SYN','MON','VDQ','HRN','BQT','AHD','WLD','IEC','BRT','PHD','NYB','KLN','SKT']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600]); print()\n\"",
 "description": "Check refs_online entries"
}
```


### [2026-09-06T02:14:49.194Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
```


## [2026-09-06T02:14:56.749Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '33230,33270p' POK_full.txt",
 "description": "Read Pokorny gheugh- entry"
}
```


### [2026-09-06T02:14:56.799Z] TOOL RESULT

```
References: WP. I 567 f., Trautmann 100 f. 
Page(s): 450 

Root / lemma: gheugh-, ghugh- 

Meaning: to conceal 

Material: Old Indie guhati, guhati^ hidden' (Aor. aghuksat), guha^ hideout, cave', goha-h^ 

hideout, lair '; common Old Indie gh- > ks- 



Avestan guz- {guzaeta, fra-guzayanta) "conceal, hide', Old pers. yadiy apa-gaudayahr 
If you hide '; 

Note: 

Reduplicated laryngeal In -h2™ahre- > Avestan -ae- 

Old Icelandic gygri. " unnolain, giantess ' ( *gugT-z, compare formal Lithuanian guze), 
Old Danish gyg^ a subterranean, an underground ', ^/ige/"" murderer, robber '; 

Lithuanian guztr patronize, guard, cover ', also "brood, hatch, cover warmly ', guzyne^ 
blind man's buff, guzis, guzta^ Brutnest ', guze^ heldnlsche Relsegottin '; In addition 
guzas, guzutis " stork ' (as " the nest builder '). 

References: WP. I 566 f. 
Page(s): 450 

Root / lemma: gheueja {gheueji) 

Meaning: pit, hollow 

Note: Only gr. and Latin 

Material: Gr. x£ici, Hom. x£in "cave, hiding place, nook, bolt-hole' = 

Latin fovea^ pothole, cave a small pit, esp. for taking wild beasts, a pit fall; a snare, 
conspiracy
```


## [2026-09-06T02:14:58.107Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ghlad\\|ghlād\\|ghl.d-\\|zrada\\|zrāda\\|zrāδa\" POK_full.txt | head -30",
 "description": "Grep Pokorny for ghlad/zrada"
}
```


### [2026-09-06T02:14:58.168Z] TOOL RESULT

```
33360:Root / lemma: ghlad!^- 
36461:ghlad-\v\ Old English giseterian^ become bright, begin to shine, derive lustre ', participle 
36493:Here ghlad!^-, ^^/sd^- "gleaming, smooth '? 
36624:ghlud-: Middle English glouten, engl. to glouV stare, look grievingly or sullenly ', to 
38009:Root / lemma: ghlad- 
38013:Material: Old Indie hradate^ sounds', hrada-m. " Geton, noise', Avestan zrada-m. ' coat 
40276:overflow '; further formations in a-yzradaye/t/" a\\o\NS to surge ', vT-yzra5ayeiti^ leaves
```


## [2026-09-06T02:15:02.796Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '38000,38040p' POK_full.txt; echo \"=== ghlad2 ===\"; sed -n '33355,33375p' POK_full.txt",
 "description": "Read Pokorny ghlad- entries"
}
```


### [2026-09-06T02:15:02.867Z] TOOL RESULT

```
References: WP. I 664, Trautmann 373, Schwyzer Gr. Gr. I 325, 413; to Indo Germanic d 
compare lastly Lejeune Traite de Phonetique grecque S. 31 f. 



Page(s): 416-417 



Root / lemma: ghlad- 

Meaning: to sound, call 

Material: Old Indie hradate^ sounds', hrada-m. " Geton, noise', Avestan zrada-m. ' coat 

of mail, garment made of linked metal rings ' ('rattling, clashing, clinking, chinking '), npers. 

zirih "armor, coat of mail, garment made of linked metal rings '; 

gr. K£xAa5a (Pind.) 'swell, of sound, ring out, murmur, rustle, roar, blossom ', KaxAa^w " 
plash or bubble, of the sound of liquids, of the sea, of rain, of boiling water, frothing forth 
foam '; 

Old Irish ad-gladur^\ address, speak to; refer'. 

The Aryan words can but just as well with Indo Germanic rto Gothic gretan be\ov\Q\ see 
below gher-1. 

References: WP. I 659 f. 
Page(s): 451 

Root / lemma: gho 

Meaning: behind, towards 

Grammatical information: preposition and Partikel 

Material: Armenian z preposition and proverb " referring to, applying to, pertaining to ' etc. 

(Meillet Esquisse2 166); 

=== ghlad2 ===
uka) Alb. Arberesh uth, alb. une'V common alb. -k > -th. 

References: WP. I 541 f., WH. I 644, Schwyzer Gr. Gr. I 606, 624. 
Page(s):418 

Root / lemma: ghlad!^- 
Meaning: " brilliant, smooth, shining ' 
See also: see below ghel- 'gleam' 
Page(s): 451 

Root / lemma: ghleu- 

Meaning: to be joyful, to joke 

Note: extension from ghel- 'cry' or ghel- 'gleam'? 

Material: Gr. x^£un f- " joke, derision '; 

Old Icelandic glyr\. 'pleasure, joy'. Old English gleo, glleg, gITwu. 'game, pleasure, joy'. 

With dental extension:
```


## [2026-09-06T02:15:04.525Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gher-2\\|Root / lemma: gher-\" POK_full.txt | head; echo ---; grep -n \"grotjan\\|grôtjan\\|gretan\\|regret\" AHD_watkins1985.txt | head -20",
 "description": "Grep Pokorny gher-2 and AHD gher"
}
```


### [2026-09-06T02:15:04.592Z] TOOL RESULT

```
18272:Root / lemma: deii(- : to look derived from Root / lemma: gher-3 und ghere-, ghre- : to 
33008:Root / lemma: gher-1 
33052:Root / lemma: gher-2 
33078:Root / lemma: gher-3, ghre- : ghro- : ghra- 
33901:Note: extension from gher-26s., mostly with dental extension (originally present?) 
34637:basic form *ghrd6'^-, ghrd^"^- must be assumed, to gr. X£PMa<^ pebble ' (see gher-2), 
36766:Root / lemma: gher-1 
36823:Root / lemma: gher-2 
36838:Root / lemma: gher-Sand ghera-, ghre- 
36881:Root / lemma: gher-4 
---
522:gher-2. To call out. Extended root *ghréd-. Germanic *grotjan in Old English grétan, to speak to, greet: GREET. [Pok. 1. gher- 439.]
```


## [2026-09-06T02:15:11.673Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '33008,33060p' POK_full.txt",
 "description": "Read Pokorny gher-1"
}
```


### [2026-09-06T02:15:11.718Z] TOOL RESULT

```
Root / lemma: gher-1 

Meaning: expr. root 

Note: mostly only newer parallel Wortschopfungen, frequent, often with expressive vowel 

change and Gemination 

Material: Old \n6\c gharghara-h ' rattling, clashing, gargling, gurgling ', m. " rattling, 

laughter ', gharghar/fa-n. ' grunting ', ghurghura-h^ a gargling sound ', ghurghurV cricket 

', ghurghurayate^ whizzes, hums '; 

Maybe alb. gurgullon " water sounds ', ^i//re "water spring' 

Latin hirnre " whimper, growl ' ("rr' with /vocalized as reproduction of of high tone); 

Old English g/erran stem V. "sound, clink, creak, babble, chatter ', Modern High German 
g/'rren {M\66\e High German also garren, gurren), Swedish Norwegian garpa^raui, roister, 
brag, boast'. Old Icelandic ^a/x?/"" intrepid pugnacious person'; Norwegian dial. garta"\oke, 
chat, prate, grunt'; Old English gierman, Norwegian garma'roar, bellow'. Old Norse garmr 
'dog'; further Old English gryllan^ gnash, rage ', Middle High German gre//en stem V. " 
piercingly, before rage shouts ', gre/'roug\r\, grell, angry, irate', Dutch ^/"o/Ze/? "murmur, be 
angry, irate'. Middle High German grullen " scoff ', Modern High German grollen, 

russ. -Church Slavic g-trkati^ coo ', Czech /7/re//" rattle, clash, purr, murmur', hrkati 
"crack, creak, burr '; slov. grgati^ gargle, coo '; 

Maybe alb. gryke^ throat ' : russ.-Church Slavic g-trkati^ coo ' 



here perhaps ghre-d-\r\ Gothic gretan, Old Norse grata, asachs. gratan, Old English 
grsetan {greofan aiter reofan6s.), Modern High German Alemannian grats9'\i\/eep, cry, 
lament '; ablaut, causative Old Icelandic greta'reduce to tears, bring to tears'. Old English 
graetan^ assail, greet ', asachs. grotian^ call ', Old High German gruozen. Modern High 
German grulien; Old Norse gratrm. " weeping, cry ', Old High German graz^iury'; 

ghre-6!^- in Old English grsedan "call, shout, cry'. 

References: WP. I 605. 
Page(s): 439 

Root / lemma: gher-2 
Meaning: to stroke roughly, rub 



Note: compare also the extensions ghrei-, ghreu-, ghrem-, ghren-, as well as above grod- 
Material: Gr. k£yxpo<; "millet, sorghum, ordure', Kaxpu(; ' parched barley, winter-bud barley 
' (diss, from * gher-ghro- dx\^ *ghn-ghru-)\ xspaSoc; n. and x^PCK^. -aSoc; f. " detritus, gravel ' 
( *gherad- or *ghernd-l)\ x£PMC(<^. -a5o(; f. " large pebble or stone, esp. for throwing or
```


## [2026-09-06T02:15:12.708Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"regret\" KLN_1966.txt SKT.txt | head -10",
 "description": "Grep Klein and Skeat for regret"
}
```


### [2026-09-06T02:15:12.772Z] TOOL RESULT

```
SKT.txt:15858:Regret,   sorrow.   (F.  — L.  and  O.  Low
KLN_1966.txt:47:It  is  a  well-known  fact  that  in  the  course  of  the  last  sixty  years  philology  has  attained  a  high degree  of  development.  It  is  so  much  the  more  to  be  regretted  that  modern  lexicography  has remained  far  behind  the  achievements  of  philology.  As  a  rule,  even  the  most  authoritative English  etymological  dictionaries  give  such  etymologies  as  reflect  the  level  reached  by  philology about  half  a  century  ago.  In  most  cases  etymologies  given  up  by  serious  science  long  ago  are still  wandering  out  of  one  dictionary  into  another  and  continue  living  with  tenacity,  appa¬ rently  ignoring  the  truths  established  in  the  field  of  philology  in  the  course  of  the  latter  decades.
KLN_1966.txt:16660:greet,  intr.  v.,  to  weep;  tr.  v.,  to  bewail  (archaic or  dial.)  —  ME.  greten,  graten,  fr.  OE.  gretan, grxtan,  ‘to  weep,  bewail',  rel.  to  OS.  gratan, ON.  grata,  Dan.  grxde,  Goth,  gretan,  greitan, ‘to  weep’,  ON.  grata,  ‘to  cause  to  weep,  cry’. The  orig.  sense  of  all  these  verbs  was  ‘to  sound, speak,  shout’.  They  derive  from  I.-E.  base *ghred-,  ‘to  sound,  clash,  speak  loudly’,  whence also  OI.  hrddate,  ‘it  sounds,  rustles'.  See  greet, ‘to  salute’,  and  cp.  regret.
KLN_1966.txt:23432:Derivative:  memoriz-ation,  n. memory,  n.  —  ME.  memorie,  fr.  OF.  memorie  (F. memoire),  fr.  L.  memoria,  ‘memor}'’,  fr.  memor, ‘mindful’,  which  stands  for  *me-mor  and  de¬ rives  fr.  I.-E.  *mer-{s)mer-,  reduplication  of base  *(s)mer-,  ‘to  care  for,  be  anxious  about, think,  consider,  remember’.  From  the  redupli¬ cated  base  derive  also  Avestic  mimara-,  ‘mind¬ ful’,  OE.  gemimor,  ‘known’,  mamrian,  ‘to  plot, design’,  Du.  mijmeren,  ‘to  ponder’.  Cp. — with full  reduplication  of  base  *mer- — Gk.  pcppEpoc, ‘causing  anxiety,  mischievous,  baneful’,  pip- prjpa  (poet.),  ‘care,  trouble’,  peppatpEtv,  pep- pTjpi^eiv,  ‘to  be  anxious,  to  ponder’.  Arm.  mor- mok ‘  (for  *mermero-  or  * mormoro -),  ‘regret, grief’.  The  simple  base  *{s)mer-  appears  in  OI. smarati,  Avestic  maraiti,  ‘remembers’,  Gk.  pipi- llvx,  ‘care,  thought’,  pEpipviv,  ‘to  care  for,  be anxious’,  Serbo-Croat  mariti,  ‘to  care  for’, Goth,  maurnan,  OE.  murnan,  ‘to  be  anxious for',  W.  marth,  ‘sadness,  anxiety',  and  possibly also  in  L.  mora,  ‘hesitation,  delay’,  OIr.  maraim, ‘I  remain’.  Cp.  memoir,  commemorate,  remem¬ ber.  Cp.  also  martyr,  mourn,  smriti.  Cp.  also moratory.
KLN_1966.txt:32172:regret,  tr.  v.  —  ME.  regretten,  fr.  MF.  regrater, regreter  (F.  regretter),  fr.  OF.  The  orig.  meaning of  this  verb  was  ‘to  bewail  the  dead’ ;  it  is  prob. formed  fr.  re-  (see  re-)  and  ON.  grata,  ‘to  weep, lament’,  which  is  rel.  to  Goth,  gretan,  OE. grxtan,  of  s.m.  See  greet,  ‘to  lament’. Derivatives:  regret,  n.  (q.v.),  regrettable  (q.v.), r egret t-er,  n.
KLN_1966.txt:32173:regret,  n.  —  MF.  ( =  F.),  fr.  OF.,  ‘lamentation’, back  formation  fr.  regreter.  See  regret,  v. Derivatives:  regret-ful,  adj.,  regret-ful-ly,  adv., regret-ful-ness,  n.
KLN_1966.txt:32174:regrettable,  adj.  —  F.,  fr.  regretter.  See  regret,  v., and  -able.
KLN_1966.txt:32175:Derivatives :  regrettable-ness,n.,regrettabl-y,a<iv. regula,  n.,  a  band  or  filled  in  a  Doric  architrave (arch.)  —  L.  regula,  ‘ruler ;  rule’.  See  rule,  n.,  and cp.  regular.
KLN_1966.txt:33292:rue,  tr.  and  intr.  v.,  to  regret.  —  ME.  rewen,  ruen , fr.  OE.  hreowan,  ‘to  sadden,  cause  repentance’, rel.  to  OS.  hreuwan,  OHG.  hriuwan,  MHG. riuwen,  G.  reuen,  ‘to  sadden,  cause  repentance’, Du.  rouwen,  ‘to  mourn’.  These  words  are  pos¬ sibly  cogn.  with  OI.  karuna,  ‘compassion’, OSlav.  su-krusiti,  ‘to  smash,  shatter',  sti- krusenije,  ‘contrition’.  See  anacrusis  and  cp. ruth.
KLN_1966.txt:33293:rue,  n.,  regret,  compassion.  —  ME.  re  we,  fr.  OE. hreow,  ‘grief,  repentance’,  fr.  hreowan,  ‘to  sad¬ den.  cause  repentance’ ;  rel.  to  M  Du.  rouwe,  Du. rouw,  ‘mourning’,  OHG.  hriuwa,  hreuwa,  riuwa, ‘regret,  repentance',  MHG.  riuwe,  G.  Reue,  of s.m.  See  prec.  word.
```


## [2026-09-06T02:15:38.546Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT zrada ===\"; grep -n \"zrāda\\|zrada\\|zrāδa\\|Panzer\" BRT.txt | head -20; echo \"=== BRT guz ===\"; grep -n \"guz-\\|gaozaya\\|fraguz\\|fra-guz\" BRT.txt | head -20",
 "description": "Grep Bartholomae"
}
```


### [2026-09-06T02:15:38.619Z] TOOL RESULT

```
=== BRT zrada ===
14953:•  j,  paiti.däna-  m.  'Vortuch,  Schutztuch'; a)  auf  der  Brust  (unter  demPanzer)  getragen, 'Brusttuch':  yalsqm  zayanqm  ra^BtlH  . . naumö  'nS'V.j4.g;  —  taranafrum  °ram  .  . histaile  draiimns  (statt  fem,)  artdvX  Yt 5.133.  b)  insbes.  Name  des  von  den Priestern  über  Nase  und  Mund  getragenen Tuchs  *^  das  bestimmt  war,  das  Feuer  vor der  Berührung  durch  den  Atem  zu  be- wahren**': yagsqm  zayanqm  a%aurune astra  gaoihi  'nD  V.14.8;  —  'rum  *ainm iarai/i  anaiwyäs/ff  dalnqm  V.  lÜ.  i;  — wird  dem  Toten  mitgegeben  (s.  *'):  avi h?  iristanqm  tanüm  .  ./rada%eiiti  , ,  xa/fvl 'nahe  Vd.  12.
28344:•  j.  zräda-  m.  'Panzerkoller,  Panzer": yaisqm  xayanam  rahsi^ti . .  haptakiS  'is  V. i4-9l  —  *°aahe''>  ..paiti.dSnake  Vd./2.
=== BRT guz ===
6012:ni/antlni  Ytß.  54;  18,  22',  26,  30,  42,  50, 54,  lOS,  117,  130,  p.4,  9f.s,  18,  22,  26, 72.2,  74- 58',  75.3,  28,  32,  Vytao»,  21, 4ß;  —  da%äni  ti .  ,  kazannm  .  .  uta  Ig 'S3m  äfrinäni  ..  Y.22.4L;  YL5.63;  — j/ai  mam  iura  paedayanta  .  .  äai  'stm tanüm  aguze  .  .  äai  tnam  fraguzayania  . . Yti^-SS;  56;  —  kü^a  tl  'um  varsm i?rjnavane  V.  2.  $t ;  lff.12,  22.6',  Ytij. 57;  —  't?m  II  g<K%ä  frähoyeni  'z?m  .  . 'Z3m  V. 2.5;  27.6,  7,  Vr.j.7;  —  \valnä a''ur(^mazdäha''  'dam  xsäya%iya^  amiy . . 'damsäm  xs'äya^iyi^  aham  Bh.  7. 5!;  — iyam  gaumätJ'  ,  .  avahä  a%ak(r  'dam baräiy^  amiy  . ,  'dam  xl3ya%iye^  amiy Bh.b;  c-j",  7.11,  13,  i6',  2.3,  s,  14,  J-S. 13;  1^2^;  —  ima'  tya'  'dam  akunavatn vasnä  J'ur^mazdäha'  ah/^ ..pasavJ' ya%ä x^aydiiiyJ'  abavam  'dam  19  hamaranä akunavam  vasnä  t^un^mazdäht^  'dam- säm ajanatn  uta  9  xssyaHyä  agarbäyam Bh..^.  2;  — pasäv^  'dam  t^urt^tnazdäm patiyävahaiy  a^urJ'matdämaiy  upastsm abar(^  .  .  avähä  'dam  . .  gaumätam  .  . aväjanam  . .  avadasim  aväjanam  x/a- %''amHm  °dam  adrnam  vasnä  a^urc^maz- dähc^  'dam  xsilya'^iyaf'  abavam  J'ur^- mazdä  x/ä^^am  manS  Jrsbara^  Bh.  J.  13; 14';  —  'damsaiy  uta  ftaham  .  .  frajanam ,  .  pasävJ'  'dam  .  .  uzmayapaiiy  akuna- vam Bh.  2. 13;  — pasävtrsaiy  'dam  ulä näham  .  .  fräjanam  ,  .  pasäve^sim  ,  ,  ut- mayäpatiy  akunavam  fih.2. 14;  —  °dam (s.  I  b)  xläya%iy^  amiy  vasna  c^urt^- mazdäha/"  'damsim  *g'a^avä  niya/ädayam tya^/äm  'dam  a%akam  avc^  .  .  D.  ö.  4 ; 3'.  5>  4-1,  5-2.  ^7-3^  Bh.  j.is,  16,  17', 18I,  19',  2.1',  2,  4,  6',  7,  9,  10,  II,  12*, 13,  Bh.^.  I,  2,  6,  8,  13,  14,  4.4,  6,  8, 12,  IS,  18,  5.1%  X.7.3,  ^.311.  Die Übrigen  Siog.-Kasus  des  Fron.  i.  Fers. s.  unter  ^ma-.  [¥.4:^.14;  lies  a&;  — Yt.  7.29:  lies  zamarf.'j
7038:satz'so,  dann;  da.' -.yezi ('wenn') aAipaurva.- naem3l  3'  mqm  avi.rimilnaya  (sd.)  Yt.16. 2;  a.  3-3,  Y.2.43,  ^'.36,  103,  /ö'.ii,Nik. 3,  Vd.  13';  —  yat  ('wenn')  yave  dayat ä'  datva  y^ism  (sd.)  V.J. 32;  321,  H.  2". 13,  N.  IJ2;  —  3at  (s.  8)  yat  apö  uzbargnte .  .  a°  fraiasinti  . .  fravasayö  Yt.  13.65; V.  Ä40,  i7.4;  —  yat  ("als')  mqm  tura pazdayatita  .  .  3'  az3m  tanüm  aguze  .  . \3at  (s.  3)  mqm  fraguzayanta  ..Yt  i7.  55^'; — yas}  tat  nmäfum  äk^rstmn  .  .  «7°  mqm tnairyö  akasat  dai  (s.  2)  .  .  fräksrmaot V.  22.  i£;  —  3at  (s.  8)  yat  miirtm  .  . /radaöqm   .  .   a°  dim  danqm  ,  .  Yt.  10.  i ;
7265:13,  N.  Ö2;  —  äat  (s.  8)  yat  äpd  udiannte .  .  ä'  fralasinH  .  .  fravalayS  Yt  JJ.  65; V,  ^,40,  ^7.4;  —  yat  ('als')  mqm  Iura pazdayaiita  . .  ä°  azsm  tanüm  aguze  . . äat  (s.  3)  mamfraguzayanta  ..  Yt  i;.  553'; — yas)  Uli  mnärom  äktrirum  .  .  ü°  mam mairyd  äkasat  äat  (s.  2)  .  .  fräkirmaot V.  22.  if;    —    äat  (s.  8)  yat  mi>r)m   .  .
9875:mit^a  'aus  dem  Versteck  hervorholen': äai  mam  fraguzayanta  . .  "da  holten  mich aus  dem  Versteck  . ."  Yt. /".  55.
20912:Nominativ  oder  dem  ihm  gleichen  Akku-' 12; —  Hat  mqm  fraguzayanta  ysi  i
27713:•  j.  *zamara-guz-'>,  z«inar-güz-  Adj. 'in  der  Erde  sich  verbergend,  verkriechend' : tum  'gBtd  (AP.)  *ak>rmvS  vispe  daiva  Y. fj.  1 5 ;  —  alvB  ahunS  vairyS . .  'gusa  (AP.)  "
```


## [2026-09-06T02:15:40.085Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT gaud ===\"; grep -n \"gaud\\|apagaudaya\" KNT.txt | head -20; echo \"=== PHD zreh ===\"; grep -n \"zreh\\|zrēh\\|zlyh\" PHD.txt PHD_mackenzie.txt | head -20",
 "description": "Grep Kent and MacKenzie"
}
```


### [2026-09-06T02:15:40.167Z] TOOL RESULT

```
=== KNT gaud ===
1183:in adánd, vardana-; from plE gh in gaud-, Bar- diya; from pIE ĝ or gh in yaud-. For materials
2509:pAr. *gau£h-aja- ‘conceal’, OP 2d sg. inj. apa- gaudaya^; cf. Skt. gühdyati.
2539:II. Thematic stems have subjunctives with the long thematie vowel throughout, Ist sg. and 181 and 3d pl. o, other forms é; 2d and 3d sg. and mid. as in Skt. bhár-àsi -àt -àse -äte : OP zšnāsāhy, Gahy (for *6aháhy), apa-gaudayàhy, \drau\jiyahy, pati-parsühy, pari-barühy (and -Gh*-d13), vainahy; ni-rasütty, xsndsdtiy, pati~parsatiy, bavatiy, vaind- tty; maniyahaty (for variant spellings, see Lex. s.v. ‘man-); maniydtaiy, gaubdtaty, 6adayátaty, yadataiy, vainātaiy. 3d pl. act. as in Skt. -dnis: OP vi-naéaya*tty (restored form).
2549:$224. Тнк INiuNCTIVE FORMATIONS are merely secondary indicative forms lacking the augment; the following forms have been found in OP: Ist sg. tarsam; 2d sg. stabava* apa-gaudaya* ava-rada*; 3d sg. fadaya'. See also $237.
2566:І. The primary ending -si was attached directly to the present stem, whether thematic or non- thematie, but happens to oceur in OP only in sub- junetive forms: pali-parsühy (on -hy, $87), Skt. prechasi; pari-barühy and -barüh*-di& ($136), vi- kanühy and -kanáh-dif, kunavahy, xindsdhy, à- tínavühy, vainahy, apa-gaudayahy, Idrau|jtyahy; 6ühy for *даћаћу ($131); ahy for short-vowel sub- junctive (8222.1) *ahahy = Skt. dsast.
2567:II. The secondary ending -s is seen in Skt. ábharas, Gk. édepes; in OP it happens to occur only in injunctive ava-rada, apa-gaudaya, slabava, and in opt. [biylà, in which it is not written be- cause it is final after a (§36).
2603:§237. THE PERSONAL ENDINGS oF THE IMPER- ATIVE. Apart from mjunctive forms, there are im- peratives with special endings, here discussed. The injunctives are those used in prohibitions with mà: ist sg. tarsam (226.1), 2d sg. stabavat apa- gaudaya^ ava-rada? ($227.11), 3d sg. байауа! (8228.II); and those used as regular imperatives: 2d pl. paraità jalà ($231).
2924:mand or a prayer, once a future statement (DPe 22): apagaudayahy DB 4.55; 6ahy DB 4.55, 58; vaindhy DB 4.78, 77; vikanàhy DB 4.73; wikanàle-di$ DB 4.77; pattbarah*-dis DB 4.74; patibarühy DB 4.78; maniyáhaty DB 4.89, DPe 20, DNa 38, XPh 47; ahatty DPe 22.
2946:$281. Tug Insunctive Моор, which is a sec- ondary indicative form lacking the augment, has in OP only the use in a negative prohibition, with má: in the first person, iarsam DPe 21; in the second person, apagaudaya DB 4.54, avarada and stabava DNa 60; in the third person, &adaya DNa 58, DNb 58.
3848:54 A : kartam : avata : kárahyà : rádiy : ma : apágaudaya : yadiy : пой :
3849:55 hadugàm : naiy : apagaudaydhy : kürahy& :8àhy : Auramazdà : fuvām :
3851:57 :08ty : Darayavaus : zXiyatiya : yadiy : imam : hadugüm : apagaudaya
3896:WB, from Wb.'s reading of Rl.s squeezes, add the fol- lowing, also in roman, which were not visible to KT, nor to RI.: ! абаһа : adam; ** draujana ; 5 apagaudayihy; " miyapaiBam : imaivd; ^ ahatiy; 78 iaumá : ahatiy : naiydis; 9 алаа; ** Vàyaspàrahya; % puça : Pārsa : Gaubarusa; * puça : Рагва : Vidarna; 9 g&bignahy& : puça; 95 Bagabuzsa; * Ardumanis : nàma : Vahaukahyá : puça; 9? kå : z5agafiya.
4995:and, Lt. ab, Gt. af, Gm. ab, NEng. оў, off, pIE *apo. Used with vb. gaud- and in sbb. apaddna-, apa- niydka-; with suffix in apalara-, apara-.
5341:gaud- vb. ‘conceal’: Av. gaoz-, Skt. githati (§88). apa- + gaud- ‘conceal, hide away’: apagau- dayahy 2d sg. subj. (§227.1) DB 4.55, 51. apagaudaya 2d sg. inj. (5215, §224, §227.II, $237) DB 4.54. gaub- vb. ‘say’, mid. ‘call one’s self’ (§213): Sas. РЫ. gowét ‘he says’, NPers. goydd, inf. guftán: perhaps a -bh- extension of pIE root *gheu- seen with -s- extension in gauga- (q.v.; Ву. BSLP 31.2.70). gaubataiy mid. (42851) DB 2,21, 31, 51; 3.15, 59. agaubaté imt. mid. DB 1.84, 93; 2.66f; 3.35, 55 (written agauratà, 454.11), 89f; 4.82. agauba^ià 3d pl. imf. mid. ($28617) DB 293. gaubdtaty subj. mid. (5285.1) DB 2.84; 3.86.
5372:gud- vb., see gaud-.
=== PHD zreh ===
PHD_mackenzie.txt:5855:l zreh [zlyh I P zryh] sea, lake.
PHD_mackenzie.txt:5856:Zzreh [zlyh I N zirih] armour.
PHD_mackenzie.txt:5953:and ud, (u-).                             armour zen, zreh, gurdih.
PHD_mackenzie.txt:6948:lake war, zreh.                           leek gandaniig.
PHD_mackenzie.txt:7510:                                           sea draya(b), zreh.
PHD.txt:680:žzēn [zyn! | N zin] saddle. zēn-abzār [zyn'pe!l | N zinafzár] horse-armour. zēnāwand [zy>zond] alert, vigilant. zēndān [zynd?n! | = M, N zindān] prison. «bān [-p?*x! | N -ban] jailer. ~ig [-yk! | N -i] prisoner. zënënidan, zënën- [zynyn-ytn!] look after, preserve. zēnhār [zyn)?] | N zinhàr] protection. zénig [zynyk!] armed. *zibāl [zb | N zībāl] swift (horse, etc.). zih [zyh | N zih] bow-string. zindag [zy(w)ndk! | M zyndg, N zinda] alive, living. ~th: life. zindakkar [zywndkkl | M zyndkr] vivifier, reviver. zinénidan, zinén- [zynyn-ytn'] damage, harm. zirak [zylk' | M zyr, N ~] wise, clever. zistan, v. ziwistan. zišt [zyst! | = P, N ~] hateful, ugly. ziwénidan, ziwén- [zywyn-ytn! | M zywyn-] vivify, revive. zi(wi)stan, zi(w)- [zyz-stn! | M zywystn, zyw-, N zistan] live. zi(w)išn [zywšn! | M zyysn] life; livelihood. ~ih: life, living. --6mand [-”xmnd] living, alive. ziyānaģ [zyd?nk'] young woman. zīyišn, v. zī(w)išn. zofāy [zwp'd | M zwp’y] deep; depth. *~ih: depth. ` zofr [zwpl | M zwwpr, J zwrf, (N žarf)) deep. —šy [2d] depth. ~-payag [-p'dyk'] deep. zóhr [zwhl | M zwhr] libation, offering. zor [z())wl | M zwr, N ~] power, strength. Bay ge J ~ig, ~dmand [-yk!, -wmnd | M -mnd, N —mand] powerful, strong. d z^ 201 [zwt! = Av. zaotar-] first officiating priest. ~ih: office of 201. Zraw-, v. zruftan. !zréh [zlyh | P zryh] sea, lake. *zréh [ziyh | N zirih] armour. zruftan, zraw- [zlwp-tn'] = azruftan. zūd [zwt! | M zwd, N ~] quick(ly). ^h : speed. zür [zwl | M z*wr] false, deceitful.
PHD.txt:2549:lake war, zrēh.
PHD.txt:3540:sea drayā(b), zrēh.
```


## [2026-09-06T02:15:51.405Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef leafof(path, lineno):\n    txt=open(path,encoding='utf-8',errors='replace').read().split('\\n')\n    pre='\\n'.join(txt[:lineno])\n    return pre.count('\\f')\nprint('KNT gaud line5341 leaf', leafof('KNT.txt',5341))\nprint('KNT line1183 leaf', leafof('KNT.txt',1183))\nprint('BRT zrada 28344 leaf', leafof('BRT.txt',28344))\nprint('BRT 27713 leaf', leafof('BRT.txt',27713))\nprint('PHD_mackenzie 5855 leaf', leafof('PHD_mackenzie.txt',5855))\nEOF",
 "description": "Compute leaf numbers"
}
```


### [2026-09-06T02:15:53.014Z] TOOL RESULT

```
KNT gaud line5341 leaf 205
KNT line1183 leaf 48
BRT zrada 28344 leaf 927
BRT 27713 leaf 907
PHD_mackenzie 5855 leaf 120
```


## [2026-09-06T02:15:53.779Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT guz headword ===\"; grep -n \"guz-  \\|^guz\\|güz-\\|'guz\" BRT.txt | head -20; echo \"=== SOD agwd ===\"; grep -n \"ʾγʾwd\\|g'wd\\|āγol\\|aghol\\|sheepfold\\|byre\\|barn\" SOD.txt | head -30",
 "description": "Grep BRT guz and SOD"
}
```


### [2026-09-06T02:15:53.857Z] TOOL RESULT

```
=== BRT guz headword ===
27713:•  j.  *zamara-guz-'>,  z«inar-güz-  Adj. 'in  der  Erde  sich  verbergend,  verkriechend' : tum  'gBtd  (AP.)  *ak>rmvS  vispe  daiva  Y. fj.  1 5 ;  —  alvB  ahunS  vairyS . .  'gusa  (AP.)  "
28116:■  j.  Z9mar-güz-  Adj.:  s.  unter  zamar^gut-,
=== SOD agwd ===
```


## [2026-09-06T02:15:59.857Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==206' KNT.txt | head -30",
 "description": "Print KNT leaf 205"
}
```


## [2026-09-06T02:16:00.823Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 1500 SOD.txt; echo; echo \"=== size ===\"; wc -l SOD.txt SOD_pages.txt",
 "description": "Inspect SOD file"
}
```


### [2026-09-06T02:16:01.408Z] TOOL RESULT

```
 sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 5110, $122) DB 1.52.
azinav- vb. ‘hear, satisfy’ ($96): cf. Av. zšnav- ‘Genüge haben an’, adj. zínav- ‘Genüge leistend’, ріс. zšnůta-, sb. zínütay- ‘Zufriedenstellung’ (Bthl. AiW 557-60); apparently an extension of root zinà- ‘learn’ (cf. pIE *40- and *doy- ‘give’), with semantic development ‘learn, hear of, hear’, and ‘hear, hearken to, satisfy’ (Lg. 15.171; ef. also Bv. TPS 1945.47-50). Hz. ApI 238-40 gives an impossible equation with Skt. éru- ‘hear’ (pIE
OLD PERSIAN
*flu-); Sen 247, 251, has wrong meanings. Р}.
sani, Acme 1.319-20, gives another etymology, -
See also uzsnav-.
z5nula- past pte. pass. ($71, 3242.1), cf. uzšnav-: zSnuta nsm. ‘satisfied’ DNb 26. |xsnutam) nsn. ‘heard’ DNb 53.
à + zínav-: dxSnautiy (§71, $122, $208) ‘satisfy’ DNb 24. āzšnavāhy 2d sg. subj. (§227.1) ‘satisfy’ DNb 29f. äzšnudiy 2d sg. ішу. ($208, §237.1) ‘hear’ DNb 54.
gaifa- sb. ‘(living) personal property, cattle’: Av. gaébü- ‘individual living being, pl. world; household, property’, РЫ. géhdn ‘world’ (from gen, pl.), to root pIE *g*ei- seen in OP jiv- (869, $101, $151). For varying interpretations, see Tm. Lex, 85, with lit. — ga26àm-cà (S89) asf. DB 1.65.
gaud- vb. ‘conceal’: Av. gaoz-, Skt. githati (§88). apa- + gaud- ‘conceal, hide away’: apagau- dayahy 2d sg. subj. (§227.1) DB 4.55, 51. apagaudaya 2d sg. inj. (5215, §224, §227.II, $237) DB 4.54. gaub- vb. ‘say’, mid. ‘call one’s self’ (§213): Sas. РЫ. gowét ‘he says’, NPers. goydd, inf. guftán: perhaps a -bh- extension of pIE root *gheu- seen with -s- extension in gauga- (q.v.; Ву. BSLP 31.2.70). gaubataiy mid. (42851) DB 2,21, 31, 51; 3.15, 59. agaubaté imt. mid. DB 1.84, 93; 2.66f; 3.35, 55 (written agauratà, 454.11), 89f; 4.82. agauba^ià 3d pl. imf. mid. ($28617) DB 293. gaubdtaty subj. mid. (5285.1) DB 2.84; 3.86.
Gaubarwa- sb. ‘Gobryas’, ally of Darius against Gaumata: Flam. kam-bar-ma, Akk. gu-ba- ru-’, Gk. TwBpins; from gav- ‘cattle’ + *baruva-, cf. Skt. bharu- ‘lord’, to vb. bar- ($85.П, $101, $122, $142, $143.II, $150, $1581, $160.Ib): ‘Cattle- Possessor’ (Justi, IFA 17.111; otherwise Foy, ZDMG 54360). Gaubaruva nsm. DB 4.84; 5.7, 9, 11; DNe 1.
Gaumdta- sb. ‘Gaumata’, Median pretender who took the name Smerdis ($164.I): Elam. kam- ma-ad-da, АКК. gu-ma-a-lá; from gav- ‘cattle’ + pte. mdta- of unknown meaning ($242.II). Gau- mata nsm. DB 1.36, 44, 46, 64, 65, 70; 4.7; DBb 1f. Gaumdiam asm. DB 1.49f, 54, 57, 73; 4.81.
gausa- sb. ‘ear’: Av. gaosa-, NPers. gas, Skt. ghóga- ‘noise’; Iran. root *gaus- ‘hear’, pIE *gheus-
(670, 5101, $1431). диа adm. ($189) DB 274, — |
| КИ adven as n Le ЧЕР Г PERDE :
ок ALES
e
LESIN EI EOE PE EERE СООТУ
I aen i bag ih oea CAU Lin aE M iig Án
LEXICON
89. gaušāyā idm. (5189; with sg. ending, Lg. 19.225) DNb 53.
gafu- sb. ‘place, throne, place of battle’
(JNES 4.49-50): Av. gdtav- дабш-, NPers. gah, Skt. gütu-, to pAr. root gam-, pIE *g*em- ‘come’ ($68, $81, $158.11, §179.n2). давит asm. DNa 41f. дйбарй lsm. ($137, $182.IT) DB 1.62f, 66, 69; DNa 36; DNb 35 (INES 4.49-50); DSe 36f, 44, 44f; XPf 33 (as abl., $182.III, though without hacé: Lg. 941-6; Ву. BSLP 33.2.148-50; Wb. А 41.319-20; Sehaeder, SbPAW 1935.503; Hz. AMI 4.130-2, 8.45, ApI 177-80), 85; XPh 34.
gad- vb., see jad-.
Ga*dara- sb. ‘Gandara, Gandaritis’, a prov- ince of the Persian Empire: Elam. gan-da-ra, Akk. gan-da-ri. See also Gadáraya-. Сайдта nsm. DB 1.16; DPe 1.18; DNa 24f; DSe 24°; DSm 9°; XPh 25. Gadārā absm. DSf 34.
Ga"déraya- adj. ‘Gandarian’: adj. to preced- ing ($144.III, $167). Gadàraya пзш. APP 12.
Ga*dutava- sb. ‘Gandutava’, a district in Arachosia: Elam. gan-du-ma-+. Cf. Tm. Lex. 86. Gadutava пет. DB 3.66.
gan- vb., see jan-. gand- vb., see gasta-.
gam- vb. ‘come’: Av. gam-, Skt. gam-, Gk. Ваши, Lt. venió, Gt. qiman, pIE g*em- ($101, $244). See also gdéu-.
à + gam- ‘come’: бјата opt. (Skt. gamyat; §67.1, §101, $122, $132.2, $218.11, $293.I, §228.IT) DPd 19.
```


### [2026-09-06T02:16:01.459Z] TOOL RESULT

```
SOGDIAN 
DICTIONARY 

Sogdian  -  Persian  -  English 


B.Gharib 


FARHANGAN  PUBLICATIONS 


Sogdian  Dictionary  (Sogdian-Persian-English) 

by  B.  Gharib 

editorial  supervisor:  A.  Mansouri 

editor:  S.  Fotouhi 

©  1995,  Farhangan  Publications 

2/52.  Shahid-e  Said  Street,  Tehran  15916,  Iran. 

Tel:  6460069.    Fax:  670230 


ISBN:  964-5558-06-9 


4f*Jj*l{^  0"J-^8  'Jy^**-  ^J>*4^  tfW  :  j'  a>„J^  <f  jljX-U^  -LUi^-L  ^JjJ'j^  L»  e jlf  ijj- 
;l_^0  jL-u  jlS'  4$"  (.5*^-*^'  "^^  (H^-  fJ 


L?JJ  J' 


•  l^>  o-^  jl  ^^<o  (j  ^jb^b  j  uij^-  ^C*" 


O    i  j^tbj^>  j^Ui    ^O  ^  p-iU-  jl  ^ 


^  jS.  Ji  * 

JU-ib^y*  jl^  *^Up  ^j^>»  4^—*a  j  -U>_# 
~J*A*  u^T  J  ('.»-)  ^.^  MJ-^  ^  jl 

^S"  ^L^wJb  jf  .x>*j$  oo  I  3^^"  f  j^^*  ^^u^J^i  J  oU^U^I 


iJUj 


*_»(  *0  k_S-*J     4rf  (J^^l  -^j'-3  iT'W-'  "^J_^ 


&*>jS  jj!  jl  d*»Us*>l  fjdjbj^ 


»>jb  ^^rj 
.Jii 

B  :C— I  eJLi  <J^ji  j  I   I  ^-Hi-"  ^ej'j  JL>-U   -p*  <o    C—l  ^yioi-  ^X-l;Lj 


^J-A— 


Joj-<U  O    i 


,(-~"  is***-*?  s.->*  S  cj^-  ^  •( 


ut*->u 


Jai»-<;  ^jptj-w*    -J>  iS(M)  I  ^U."-'  1*}>-<j  <Sy^  J^  .Jj'oX*  I    ^J-^  U^* 

ft^b  OUjS(AL)  u  (<uoa*  .^T.j)  ^^-b  ^U^U))  j  iS(C)  t  ^jul^ 


I  Jta^-  4J^T 


<->  ^  jj  ojl j  0  (  o-^»^*p  ^j  Jb  oij 


4j  ^j^^h9  i^-j^j-*  ^^i^-w...^  ^u*^  (Ul^  y^***  <ftjij  *-^>  i^'^  i""^  j-;^>- 


^j-J^Ol  ^f-UJUw  JJUly^  iy\  lf>-j  I  .C-^^C  JLjUT  
=== size ===
 111423 SOD.txt
  45615 SOD_pages.txt
 157038 total
```


## [2026-09-06T02:16:19.043Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"cover\" SOD.txt | head -40",
 "description": "Grep SOD for cover"
}
```


### [2026-09-06T02:16:19.118Z] TOOL RESULT

```
3886:discovered  in  Central  Asia  around  the  beginning  of 
4148:13.  J.  A.  Dabbs,  History  of  the  Discovery  and  Exploration 
4363:dated  580  A.D.,  discovered  in  central  Mongolia  in 
4517:discovered  a  walled  up  library.  The  library  was 
4522:packed  bundles,  he  discovered  a  number  of  rolls  and 
4610:all  the  Paris  manuscripts  recovered  by  Pelliot's 
4674:Buddhist  texts  recovered  by  Sir  Aurel  Stein:  "Reste 
4739:survey  covers  the  Buddhist  Sogdian  materials 
4740:discovered  by  A.  Stein  (1907-1933),  P.  Pelliot  (1910) 
4771:55.  It  docs  not  cover  Buddhist  Fragments  of  Leningrad 
4786:Manichean  materials  were  discovered  in  the  oasis  of 
4793:Other  Sogdian  materials  were  discovered  in  Yar- 
4796:which  was  discovered  in  a  ruined  temple  at  the  head 
4940:Christian  materials  were  discovered  in  the  Turfan 
4983:History  of  the  Discovery  of  Central  Asia,  1963,  p.  14. 
5064:Sogdiana  have  been  discovered  and  deciphered  by 
5072:The  first  report  of  an  accidental  discovery  of  a 
5137:they  were  discovered,  the  Mug  Documents.  The 
5186:history.  Archaeological  discoveries  in  old 
5193:inscriptions.  The  longest,  of  16  lines,  was  uncovered 
5251:inscription  discovered  in  Karabalgasun,  North 
5290:German  expedition  in  North  Pakistan  discovered, 
5301:A£>.  A  preliminary  edition  covering  one  third  of  the 
5318:91.  The  inscription  was  discovered  by  the  first  Russian 
5480:discovered  at  Panjikant  in  1965  and  published  by 
5497:documents  discovered  in  Chinese  Turkestan,  as  in 
7558:*  The  abbreviation  denotes  H.  Oldenburg,  the  discovered  of  the  fragments. 
8092:cover,  covering 
8279:(to)cover,  (ro)dress 
8285:(to)cover,  (fo)dress 
8293:(to)cover,  (ro)dress 
8306:covering 
15954:(fo)uncovcr,  (^discover 
18303:horse  covering,  horse  armour 
19467:(fo)bury,  (rc)cover 
19472:buried,  covered 
24401:(ro)cover,  (fo)wrap 
24407:coating,  covering 
24843:(a  sort  <?/)covering 
36515:covering
```


## [2026-09-06T02:16:19.966Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1,80p' SOD.txt | cat -A | head -0; awk 'BEGIN{RS=\"\\f\"} NR>=70 && NR<=72' SOD.txt | head -60",
 "description": "Sample SOD pages"
}
```


### [2026-09-06T02:16:21.519Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T02:16:24.470Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8070,8320p' SOD.txt",
 "description": "Read SOD around cover entries"
}
```


### [2026-09-06T02:16:24.582Z] TOOL RESULT

```
74  "YlnS    B  .  J^K*. 

axans   =*»x>s,  'ny's 
fight,  dispute 
TSP  9.12,  13ii  7 

75  »YV    M  ->  »yrt>k 

76  nvV2     R 

axar  ' 

step,  pace 

SCE  197;  BSTBL,  Dhy.  93,  97,  EGSii  167 

77  »Y>st-   S  =»  »Yst-' 

78  YwS   B  *  «    ,^     ,. 
ayofc  ©<a-gaud-   =»»Ywnd- 

cover,  covering 

VJ  961;  BSTBL;  Gharib.  AI  4.249 


Y6- 


79  »Y>y8-    B  b^jj^y-icr^y*- 
aye5   ©<*a-gadaya-  =^*Yy5- 

(to)wish,  (fo)demand 
BSTBL,  Dhy.  15,  75;  GMS  653 

80  YyS'k  B  jJjT  <u^l>- 
aye5e  (•yyS'k)  ^yS'kCw) 

wish,  desire 

TSP  2,  382,  »rj<5>jbv;  Sogdica.  60.28,  61 

81  Vynt-   B  &£*J\io*fS\& 
ayind  ? 

(ro)defile 

Mack.  SCE  180(N);  Gersh.  IF  75,  304 

82  Yyr-    B  u*j^5 'j^j 
axer  ^Y1"2*  xrt~^  >xYr- 

(to)walk 

BSTBL,  Dhy.;  SCE  383 

83  Yyr   B  ^*«^> 
axer 

moving,  going,  ambulant 
VJ  882 

84  Yyrn'k   B  l^,  «-ujj  <<-0*> 
axerne   (*Y>yrn>y)  =»*xyrny 

moving,  walking,  going,  ambulator 
BSTBL,  Dhy.  100,  246;  ->y,  Dhy.  228,  297,  311; 
*Yyrn%  Dhy.  245 

85  Yyrn>y  =*  1Y>yrn>k 

86  "y^-  (J>>  j<*&  jj) j-bjUT  t&J'&ji 
ayaz  (*y*z)   ©<*a-gaz  ^•yst-1,  Yz- 
0<?)begin 

87  Yz  B.M.C  ^j>O^T 
ayaz  ©ob.  -(>)y 

beginning 

TSP;  BSTBL;  Frag.  Len;  STi  77.1;  Hen.  Giants. 
68.24;  nom.  TVy,  Dhu.  259 

88  "yS^w)   B,  S  lIw.^l^.jjjT 
ayaSe,  ayaSaku  ©<*a-gadaka-,  Sgad\  Parth. 

'g'dg;  Khwar.  yVSk   =»Yy§-,  'Y^y 

wish,  desire 

TSP;  VJ;  BSTBL;  MSP;  KG;  Frag.  Len.;  ace. 
>rd>kwy  VJ  99,  142,  376,  383,  BSTBL,  Padm.  23, 
25,  53;  Vim.  51;  nom.  VJ  101,  442,  446,  47c 

89  »yd>r-   C  j^T 
aya6ar  ©trans,  pret,  =>*yt-2 

(to)bring 

STii  4.32,  3pl.  -nt 

90  »y5>w  B  jAjh'sxJ 


aya5o  ©<aTa6aku  ? 
wish 

VJ;  EGSii  75;  GMS  960;  nom.  VJ  29d,  650,  1185; 
ace.  VJ  17,  59\  1223 

91  "yS'y  S,B  j*ljr<jjj 
ayaSe  (*ydy,  Y>yy)  -»iY8'k(w) 

wish 

SCE  555;  VJ  44e;  TSP;  BSTBL;  BBB;  GMS  962; 
KG;  STii  8.10,  4.12 

92  »ydy   C  **  »y5>y 

93  »y8yy   M  =*  »y5>y 

94  "ymp-   M  j&^tfrJ'cSj*- 
ayamp 

walking 

Sogdica.  64,  lln66 

95  "yrt'k  S  ouA^io^ 
ayar(te)  ?  (Y*1)  ^yrtqy*,  >y>xc 

radiant,  splendid 

S  W,  C2  pl49,  27;  *r>r,  Hen.  JRAS  1944,  144n3; 
Mack.  AI  1985  422,  424  n4 

96  »yrtystr  M  ji>\>*Kj^ 
ayartistar  ?  ©superl.  *Yyrt 

most  fertile,  richest 

GMS  656,  1289;  Sogdica.  29.6.30 

97  "y^r-  S,  C  uJb>T<u^^> 
ayasSar  ©<**Yst-d}r-  ©trans,  pret.  =»  Yz-> 

*yst-\  ^sd'r- 
(to)begin 
STii  p574;  Frag.  Len.  *Y(>)sS>r 

98  "yst-1  M,  S  0*>£j> 
avast  (Yst-)  ©pt.  st.  =>Yz-  }Yst-,  'ysS'r- 
(to)begin 

BBB;  W-Li,  ii;  GMS  865;  Frag.  Len.;  KG  pl77; 
MSP  b47;  »rj/-,  MSP  b5,  b47,  bl36 

99  »yst->  S  ^-^ 
axast  ©pt.  st.  =^*xst- 

(ro)rise 

STi  86.17,  >Y}st- 

100  "yt-1  (Oj*  j~t  j*)ojJ 
ayat  Cyt-)  ©<*a-gata   ©intrans.  v.;  pt.  st. 

=**ys- 
(to)come 
GMS  603;  AVS  139 

101  »Yt-'  o>jf\ 
ayat  ©<*a-gata  ©trans,  v^  pt.  st.  ^■pr-, 

'yd'r- 


?)k>ptc(h) 


(to)bring 

GMS  603;  AVS  139 

102  "y^k1  B  <^7 
ayate  (*yVy,  'ytk1)  ©intrans.  v.;  pp.  =^»yt-1 
came 

TSP;  SCE 

103  VkJ  B  (u^>^-j^jjT 
ayate  ('ytk2)  ©PP*;  trans,  v. 

brought 
TSP;  SCE 

104  "yt'y  B  =*  'yt*1 

105  "ytk1  =»  'yt'k1 

106  »ytk2  =»  *yVk7 

107  Mywnd-    M  lUU^j4  <UJsiji 

ayund  ©<*a-gunt;  Sgaud-  ©impf.  myYwnd 

=^ywnt-,  *Ywst->  *Y>W$ 
(to)cover,  (ro)dress 
GMS  601,  807;  Gharib.  AI  4.249 

108  »ywnt-   B,  C  Oxli^ioJ^ji 
ayund  ©impf.  nVywnt  =»»ywnd- 

(to)cover,  (fo)dress 

BSTBL,  Dhy.  16;  STi  16.8;  Gharib.  AI  4249 

109  »ywst   S  =>  »ywstk 

110  wywst-   M  d^x 
ayust   ©<*a-gusta  ©pt.  st.  =^ywnt-,  *ywstyh 
(to)cover,  (ro)dress 

Gharib.  AI  4.249 

111  "ywstk   B  o^ t^J\ 
ayuste  (*ywst)  ©Parth.  >gwd,  }gwst\  MP  }gwh- 
dirty,  defiled 

Hen.  AION  1965,  32.6;  BSTBL,  Dhy.  397;  >rwst, 
MSP,  p39,  b85 

112  "ywstyh    M 
ayuste   ©inf.  =4»ywst- 
covering 
GMS  931 

113  Mywyr   B 
axwer  =»*xwyr-,  >xwyr 
stable 
VJ  17b 

114  "ywyr-   B  (?  jx^ 
axwer  ? 
(to  /zave)indigestion  ? 
TSP  n  p216,  8.124 

115  »yWyr>kh   B  ?  <w>U^ 
axwerak  ?  axwere  ?
```


## [2026-09-06T02:16:40.478Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('SOD.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in (8092,8279,8285):\n    print(ln, '\\n'.join(txt[:ln]).count('\\f'))\nEOF\necho \"=== find page tags ===\"; grep -n \"pdf page\" SOD_pages.txt | sed -n '60,80p'",
 "description": "Find SOD leaf numbers"
}
```


## [2026-09-06T02:16:41.659Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sheepfold\\|fold\\b\\|stable\\|byre\\|cattle-pen\" SOD.txt | head -20; echo \"=== MON agol ===\"; grep -n \"آغل\\|آغيل\\|آغال\" MON_part1.txt MON_part2.txt | head -20",
 "description": "Grep SOD stable and MON āγol"
}
```


### [2026-09-06T02:16:42.227Z] TOOL RESULT

```
8092 0
8279 0
8285 0
=== find page tags ===
```


### [2026-09-06T02:16:42.314Z] TOOL RESULT

```
8311:stable 
8338:chief  of  stable 
21719:stable 
31601:ten-fold 
34927:stable,  strong 
48900:ninefold 
54096:five-fold 
61395:stable 
62120:instable 
73766:two-fold  ? 
78090:(to)unfold,  (to)bc  explained 
85157:"fold"  GMS  1034,  1328;  MSP 
85171:of  many  kinds,  manifold 
88173:chief  of  stable     116 
89623:five-fold     6896 
90815:instable    8067 
91565:manifold     11353 
92074:ninefold    6121 
93979:stable     113,2130,4139,7955 
94393:ten-fold     3634 
=== MON agol ===
MON_part2.txt:3443:آغل. مغا کی در دشت يا در کوه. 
MON_part2.txt:41406:لیسه: (0-):-۱15 (۱.) سنکی که در آغل سب 
MON_part2.txt:60957:معطن : ۵۸ ۱۱ ۳ )1( خوایگاه ستر . آغل 
MON_part2.txt:77300:سازند برای گوسفندان؛ آغل. 
MON_part2.txt:77402:صحرا برای گوسفندان سازند؛ آغل. 
MON_part2.txt:80358:آغل‌ها به چمن‌های سبز و خرم می‌کشانیدند 
MON_part2.txt:80361:که کله را به آغال کشانیده توشه و و 
MON_part1.txt:3635:آغار: : :38 ((.) اغرء آغال: بد آغار (شوم» 
MON_part1.txt:3662:آغال: اقبة (- آغار - اغر | اغره شگون بد 
MON_part1.txt:3663:آغال» شوم. 
MON_part1.txt:3671:اغ‌الش: کت-21ب2 (امص. آغالیدن) 
MON_part1.txt:3674:آغالشگر: 7-.2 (ص‌فا.) تحریکك کننده؛ 
MON_part1.txt:3678:آغالد» خواهد آغالید» بباغال» آغالنده؛ 
MON_part1.txt:3679:آغالیده) انگیختن» تسحریک کردن» 
MON_part1.txt:3704:اغل: (هبة باب [- آغال - آغیل] (.) جای 
MON_part1.txt:3746:اغول: اقبة [- آغل] (.) آغل زاغه. 
MON_part1.txt:14689:اغر: ۲ (- اغور» قس. آغار آغال] (ا.) 
MON_part1.txt:14698:برآغالیدن» تحریک کردن» برانگیختن. 
MON_part1.txt:14699:(امص.) آغالش» انگیزش. اغراء به جهل: به 
MON_part1.txt:14700:جهل کشانیدن» آغالش به نادانی
```


## [2026-09-06T02:16:47.229Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3695,3750p' MON_part1.txt",
 "description": "Read MON around āγol"
}
```


### [2026-09-06T02:16:47.286Z] TOOL RESULT

```
فرهنگ فارسی معین ۵0۱ 


آغشتن: 272)6(۹-0 | < آغزدن - آغاردن] 
(اعشتا آغده .هاش اعست).ساع 
آغرنده» آغشته) (مص ع.) خیس کردن» نم 
ون آلودن. (فز .) آلودن جسمی به مایع 
(فره.) (مص‌ل.) خیسیدن» نم کشیدن. 

اغل: (هبة باب [- آغال - آغیل] (.) جای 
گوسفندان و گاوان و دیگر چارپایان به 
شب در خانه با در کوه و با در کنده‌ای در 
زير زمین. 

اغنده: (6-)2721-012 (- غنده» غندشض) (.) 
پنبه پیچیده و گرد کرده برای ریسیدن. 
(جان.) نوعی از عنکبوت زهردار» رتیلاه 
رتیل» عند۵. 

اغوز: 2ج [- آغز] (.) شبر کاو و گو سفند 
ماده نو زاییده» اولین شبری که بکك ماده به 
نوزادش دهد ما کك» شیر ما ک» فله» بله» 
حرش؛ فرشه» گورماست» لباء زهک» آغ: 
آغوز: «5بة (- گوز] (.) (گیا.) درختی از 
تبرة بباله‌داران که از چوب ارم ورهتل: 
و مانند آن سازند و در جنگل‌های ابران 
سیار است؛ گوز» جوز» گردو» گردکان؛ 
چارمغز. 

اغوش: 2۷54 (- آگوش - کش - آغش] 
(.) مبان دو دست فراهم آورده» جون از آن 
دو دابره‌واری سازند؛ بغل. ان مقدار از 
گیاه چوب؛ کاغذ و مانند آن که به آغوش 
توان برداشت؛ بغل. به آغوش کشمدن: در 
میان دو دست فراهم آوردن» به خود 
چسبانیدن کسی يا چیزی را. به (در) آغوش 
کشیدن: به آغوش کشیدن. 

آغوش: 25 [ تر. آقوش: آق» سفید + 
قوش برنده: برنده سفید] (.) نامی است از 
نام‌های غلامان و بندگان ترک و آن 
بصورت نمونةٌ نام‌های ترکی بکار رفته. 
اغوشیدن: 2۷01-14۰ [- آگوشیدن] 
(مسصم.) (آغوشید» آغوشد» خواهد 


2۲ فرهنگ فارسی معیر آغول 


آغوشید» باغوش» آغوشنده» آغوشیده) در 
بغل گرفتن» در بر کشیدن. 
اغول: اقبة [- آغل] (.) آغل زاغه. 
اغول: ۱ آغیل ] (.) ی به 
ی چشم از روی غضب؛ چشم آغول» 
ِ 
اناق: ۷ [ع.] (۱.) ج. افسق. افق‌هاء
```


## [2026-09-06T02:16:49.064Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" SOD_pages.txt | head -5; echo ---; grep -n \"ywnd\\|ʾγwd\\|>Ywd\\|'Ywd\" SOD_pages.txt | head -10",
 "description": "SOD pages structure"
}
```


### [2026-09-06T02:16:49.166Z] TOOL RESULT

```
---
4134:107 Mywnd-     M                              lUU^j4 <UJsiji
4143:    ayund ©impf. nVywnt =»»ywnd-                                     GMS 27, 860; Hen. BSOAS 11, 68.17
12436:3052 bywnd'ry        C                               ^^
13345:                                                                           ciwand (cywnd, cywnt) ©<*haca-yavant ?
13366:                                                                     3376 cywnd       M =* cyw'nt
15857:4250 yr8mrywndy M            S             tjfjrfj                           yarmec
15859:     yarS-marywnde              jj=r <{* '                                   S W, BAI 1990, 286
15906:                                                              4280 yryw jywndg M           (^yU ^Ij^)^j ^"-uj^jj
16858:                                                                  living     (jywndyy, jwndty) ^jw'ndyCyX
16956:4620 jywndg M                                           *xj        paper
```


## [2026-09-06T02:17:02.959Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\n# find markers\nm=re.findall(r'\\[pdf page \\d+\\]',txt)[:5]\nprint(m[:5], len(m))\nlines=txt.split('\\n')\nfor i,l in enumerate(lines):\n    if l.strip().startswith('107 ') or l.strip().startswith('78 '):\n        print(i,l[:80])\nEOF",
 "description": "Inspect SOD_pages markers"
}
```


## [2026-09-06T02:17:04.169Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN zirih ===\"; grep -n \"zirih\\|zirih\\|zirh\\|Panzer\" HRN.txt | head -20; echo \"=== HUB ===\"; grep -n \"zirih\\|zrāda\\|Panzer\" HUB.txt | head -10",
 "description": "Grep Horn and Hübschmann for zirih"
}
```


### [2026-09-06T02:17:04.925Z] TOOL RESULT

```
[] 0
4133 107 Mywnd-     M                              lUU^j4 <UJsiji
```


### [2026-09-06T02:17:04.986Z] TOOL RESULT

```
=== HRN zirih ===
2179:205. bergustuwän 'Panzer, Pferdepanzer'.
5045:bei. zirih *Qnell\ zira *Meer (425).
5841:660. ^irih 'Panzer.
5842:aw. zraöa- 'Panzer'; phlv. zrai (päz. zareh) bezw.
5850:LW. kurd. zirt, zir/ * Panzer ; af;'. zira; bei. zirili
8408:Ar. mäSiy 'weisser Honig', moMyat 'glatter Panzer; "Wein* (dazu
=== HUB ===
4519:Ueber np. zirih 'Panzer' siehe § 12, fiber -tr- s.
4714:Ap. a = mp. a = e = np. i in zirih *Panzer , paz.
5609:varapanak-U *Waffenrock' 1 Kg. 17, 38, varapan *Panzer
7027:zd. spada-, ap. {Taxma-)spaia' ; zirih *Panzer', paz. zreh,
7884:zar van *Zeit' (g^) siehe oben p. 69; zirih *Panzer' -- zd.
7917:zrahK 'Panzer, bazuk 'Arm*, vzruk^ vzurk gross', part€z
9777:zirih ist hier girih *Knoten (vgl. p. 93) zu er-
```


## [2026-09-06T02:17:08.497Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5838,5860p' HRN.txt; echo \"=== leaf ===\"; python3 -c \"\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nprint('\\n'.join(t[:5841]).count('\\f'))\"",
 "description": "Read Horn zirih entry"
}
```


## [2026-09-06T02:17:08.982Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4515,4525p;7880,7890p;7910,7925p' HUB.txt",
 "description": "Read Hübschmann zirih passages"
}
```


### [2026-09-06T02:17:10.217Z] TOOL RESULT

```
Berosus — ; ai. jarimdn- 'Alter'.
Ist etwa auch zemän (aus *<^ermöw), zemäne^ persisch
und nicht arabisch, wie man gewöhnlich annimmt?
660. ^irih 'Panzer.
aw. zraöa- 'Panzer'; phlv. zrai (päz. zareh) bezw.
zrad (aram. LW. n^T, arab. zarad, zarad[xäne).
*) Nöldeke, Pers. Studien, I, 38 üimmt eine Form ohne ;*, also
*zarta-, als Grundform für np. zerd an.
2) FR führt dieselben beiden Verse wie HQ an (Wiener Jahr-
bücher, Band 40, 176).
*) Später ist der zoroaatrische Zevfän zu dem Patriarchen
Abraham ^owonlon.— 147 —
LW. kurd. zirt, zir/ * Panzer ; af;'. zira; bei. zirili
(306); arm. zrah.
Urverwandt mit afy. zyara * Kettenpanzer', oss. zyär
Tanzer (132) ?
%l, liieryiin gelbfarbig.
aw. zairi.gaona- gelbfarbig'; phlv. vergl. zarlnqün
(vd. 2 (67)).
Vergl. np. öün aus *cigün (No. 450) und aöenjiin,
G62. »ist 'schlecht, schimpflich*, zistür.
Kää. Z. jist (auch s. v. bed).
aw. jlstayamna- (y. 8, 3) Verachtend, vorspottend'
=== leaf ===
167
```


### [2026-09-06T02:17:10.275Z] TOOL RESULT

```
die alten Positive ap. *ma&'y ^kadu- und *va(h)u- im Mittel-
persischen bestehen blieben, so wurden sie zu *mah, *kah
und *vah und spater durch die Komparativform meh, keh,
veh verdrangt.
Ueber np. zirih 'Panzer' siehe § 12, fiber -tr- s.
§ 34, b.
*) Vgl. farrux = phi. farraxv § 4, a.
') Da im Neup. neben dih die Form ^i^, Alter also deh steht,
liegt es allerdings nfther, dih = dih aus *daih = *dahy^ also durch
Epenthese, hervorgehen zu lassen, wie Horn will. Ahnlioh wftre dann
hih = phi. v9h zu erklSren, nicht aber mih und kih (= phi. m-£ und k^s.)
gross = ap. va2rka-^)\ nur mp. und np. : zadan gebaren,
geboren werden' {g^) H. 645; zal *Greis*, zar 'Greis {g^) H.
648, 655; zanu *Knie {g^) H. 648; zar 'Gold' {g'h) H. 645;
zaryUn gelbfarbig' (g^h) H. 661; zard gelb* {g%) H. 656;
zar van *Zeit' (g^) siehe oben p. 69; zirih *Panzer' -- zd.
zrada-'^ zafar 'Rachen' (das aber nicht urspr. persisch ist,
vgl. dahan --= zd. zafan § 80, c und 110 sowie § 163, c)
mit g^, siehe oben p. 70; zam 'Kalte* (g^h) H. 666; zamt,
zamln *Erde (g^) H. 667; zanax 'Kinn {g^h) H. 669; zud
'schneir (g^) = skr. juta-y siehe oben p. 70; zor 'Kraft' =
zd. zavare; zDr *Weihwasser' {g^h) H. 675, Parsenwort;
Dagegen sind r und z erst im spateren Mp. zasammen-
gekommen in farzana *weise' [g'^) = phi. frazanak (zd. zan,
skr. /wS wissen, vgl. § 110, 2), farzand 'Spross [g^) = zd.
frazainti' (zd. zan^ skr. /aw). Durch Umstellung entstand
rz in jrwr^ *Keule* {<g^) = zd. vazra-.
Im Paz. und Phi. erscheint fiir ap. z immer z, ebenso
im Armenischen: zoh *Opfer, zur 'ungerecht', zaur 'Heer',
zrahK 'Panzer, bazuk 'Arm*, vzruk^ vzurk gross', part€z
'Garten', Varaz (in Namen) 'Eber' u. s. w. ; rz, das auch zu rj
(= rdz) wird, fiir iran. rz: apaharzan 'Scheidung von der
Frau' ^= zd. apa + harezana- (vgl. vis-harezana-), skr. apasar-
jana- (unbelegt) 'das Verlassen', apasrsta- 'sich zuriick-
gezogen habend von' — ; hamaharz 'Adjutant' (sicher per-
sisch); andarj Testament' = np. andarz 'Rath, Testament',
anderjapet oder handerjapet = phi. andarzpat BB. 4, 62;
derjak 'Schneider, Schuster', derjan Taden', handerj *Kleid',
```


## [2026-09-06T02:17:20.661Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v2 زره ===\"; grep -n \"زره\" BQT_v2_pages.txt | head -20",
 "description": "Grep BQT v2 for زره"
}
```


### [2026-09-06T02:17:20.721Z] TOOL RESULT

```
=== BQT v2 زره ===
797: ‫‪.‬‬       ‫ورس‬    ‫زره‬   ‫‪ 3‬زلف‬   ‫کمان کشیده‬          ‫چشم‬         ‫شاعي‌است چهرءات که دو جاندار خاص او‬
1429:              ‫وبمعنی جلد و چابك لبزرهست ‪.‬‬            ‫آواز زدن شمشیر وتبغ وزنجیررا ندز گوبند ؛‬
2123:‫باشد شبیه به‬             ‫پواو کشیده ‪ .‬ستبزرههو‌ای‬         ‫_‪١‬‏ و نام‬   ‫همآمده است‬
3241: ‫مردم بدخوی وثرش روی هم هت ‪ -‬و درعربی‬      ‫باشد ‪ -‬و حلقای را بیز گویند مالند حلفه زره‬
3243:‫زره را ‪ -‬و دلشب بعنی لصف شب ‪ -‬و سینه را‬ ‫|‬ ‫ء‬ ‫و جوشن ‪ -‬و نامروز چپاردهم است از هر ما‬
3270: ‫جو کات ه باکاف بر وزن کوچك ‪.‬‬                                  ‫باشد بر زره چه زره تمام ازحلقه است وجوشن‬
5955:        ‫اپوالفتح بستی «لفت‌فرس ‪ ۱۷۱‬رك ‪ :‬بچفازره‪.‬‬
7131:                              ‫و انگشتان مردم*‪- ۱‬‬                                    ‫آن ولات را زره ‪6‬‬
7150: ‫‪ - ۱‬از ‪ :‬چندل و‬         ‫زره سستان امت ‪ .‬رکه‪ :‬زره‪.‬‬ ‫‪۵‬‬             ‫اوستا ‪ ۹۳۱‬و‪۲6۱۰‬‬
14062:  ‫نزدیکی درباچة زره (هامون ) سیستانست ‪.‬انرا هم « کوه خدا» گویند وهم «کوء خواجه » (اين‬
15296:‫خیار زره سنك ‪ -‬رستنیی باشد مانند‬
17610: ‫مفتوح» بمعنی زره باشد که بعربی درع خوانتد‬        ‫است که تابن ومنورباشد ‪ -‬و بمعنی لرزیدن هم‬
20852:                                                             ‫حرع وزره باشد با تیر وئیزه مربدن دشمن ‪٩‬‏ =‬
23200:                                                             ‫رائیز گفته‌اند که ازز وة‬       ‫وزرهی‬      ‫گوشد‬
23293:                                                                       ‫‪۰‬‬   ‫زرهس‬   ‫رك‪:‬‬   ‫‪-‬‬   ‫راهیر‬    ‫*‬
23823:    ‫فردوسی طوسی‪-‬‬            ‫زره را گره ب رکمربند زد‪.‬‬                    ‫بپوشید درع سیاوش رد‬
23901:    ‫زره د بنتح اول وتخفیف ثالی » ن‬                       ‫وی »‬
28024:                                                  ‫زراتشت‪ .‬زارتشت» زره‌تشت؛ زاردهشت» زاردشت»‬
28151:   ‫® ‪ -‬یز قمت زره رنگه درون‬                   ‫‪.‬‬     ‫‪۲۲۱-‬‬
28437:‫زره = بکر اول و الی و ظهور های‬               ‫‪۱‬‬                ‫‪ 2‬آنبادی‬        ‫بمعی ا‬
```


## [2026-09-06T02:17:22.374Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM zarad ===\"; grep -n \"زرد\\|زراد\\|الزرد\" AFM.txt | head -20; echo \"=== PLA ===\"; grep -n -i \"zarad\\|zirih\\|zarrād\\|zard\" incoming/PLA/PLA_pages.txt | head -20",
 "description": "Grep AFM and PLA"
}
```


### [2026-09-06T02:17:22.471Z] TOOL RESULT

```
=== AFM zarad ===
1540:وفسّرت بضرب من 130 ن انواع الزرد.وهى في ± ܝܒܒ 
2033:( الجَوسّن ) الصدر والدرع ومن الليل وسطة ܐܨܠܐ جوشن وهو ܘܒܐ الزرد 
2035:ܠ على اللهر والفرق ܢܢ وبين اازرد 2 الزرد يكون من ملعريكة وإنندة ديفم 
3208:زدد وزدد به وزراد ودرع وأدرع وتدرع › ܙܕ زرخ بالتركيّة 
3222:+ (الرردى ) نوع ܝܨ !ܐ ܙܒ ;ܐ‫ 05 3:3 والعسل تعر يب زرده 
7433:زرده ^ 
=== PLA ===
1133:>51                - "azrad:          Pl.      v. „,; zarad             4-        V.
3171:ls          -    bißtäsb:                  "Schützer,               Schirmherr              v.    zardoßt     (Zarathustra,           grch.
5775:Prlr-                       $auzfandum:                   "Weizenblüte"                       pers.       s.      Zardandum        ı,
8042:„b>> -         zidwär:            "Kurkuma"            aus       dem    pers,     -\b>,)    zardwar        "gelblich"         aus    dem
8043:      pers.          >», zard             "gelb"             mp.       is zard     4      port.     zedoria,        it.    zeltovaria,
8079:zarbil                                                                          142                                                         zardgüb
8093:>2.,-       zarad:             "Ringpanzer,                     Kettenkleid"               aus    pers.      „,    zreh       <Imp.        _\   zreh
8094:            au.                zrai,           gen.        zarasvehe           5, ar.          Lw. „_) zarad,            syr.}’,,)         zarda         6,
8097:>», zarada:                "einen              Ringpanzer              machen,         aus       Ringen      eine       Kette    machen"         s.
8098:      zarad
8101:)),-            zardäb:              "Safflorsaft"                     aus     dem     pers.          12     zardan_ ’<T             mp.     >35 zarda.
8103:EJ1              -    zardälüß:                  "Aprikose"             aus     pers.          „|,         zardälu       8 mp.             ne eds
8104:        zardälüg 3,                            aram.        „pl         "9.
8106:2)      -       zardab:             "erwürgen,                  zusammenpressen"                  pers.      11,
8109:&r -            zardaß:             "flüssiger                  Safran"        aus     pers.       2),,, zardak          12 mp.             ges zardak
8112:2,”                  zardöüb:              "Kurkuma,              Gelbwurz"            aus       pers.      a, ,>»       Zzardöübe         18. mp.
8113:            EBN2SO zardöobag                              14,
8130:zard$üba                                                                       143                                                        zaraq
8133:Lo,                    - zard$üba              = zarddüb              ga. v.
8136:0                  - zardüs              = zardgub               gq. v.
```


## [2026-09-06T02:17:34.966Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"sard\\b\\|zarad\\|coats of mail\\|Ringpanzer\" FVQ.txt | head -20",
 "description": "Grep Jeffery FVQ for sard"
}
```


### [2026-09-06T02:17:35.015Z] TOOL RESULT

```
10653:*j~ (Sard).
```


## [2026-09-06T02:17:36.381Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"greet\" KLN_1966.txt | head -8; echo \"=== AHD gher ===\"; sed -n '515,530p' AHD_watkins1985.txt",
 "description": "Klein greet and AHD gher-"
}
```


### [2026-09-06T02:17:36.457Z] TOOL RESULT

```
4092:Semitic  bases  h-w-h  (h-w-')  and  h-y-h  is  illustrat¬ ed  in  Gen.  3 : 20,  ‘And  the  man  called  his  wife’s name  Eve  (Hawwdh),  because  she  was  the  mother of  all  living  (hay)'.  See  Eve.  For  sense  de¬ velopment  cp.  Heb.  yehi  ddhdnt  hammelekh Dciwidh  I'o/dm:  ‘Let  my  lord  king  David  live  for ever!’  (1  Kings  1:31;  cp.  Dan.  2:4  and  passim), E.  ‘Long  live  the  King!’,  F.  ‘Vive  le  roi’,  etc., all  used  as  formulas  of  greeting.
4093:(The  origin  of  L.  ave  being  thus  established,  we shall  be  able  to  find  the  exact  meaning  of  the words  with  which  the  gladiators  greeted  the emperor:  ‘Ave,  Imperator,  morituri  te  salutant��� (see  Suetonius,  Claudius  2 1).  The  usual  rendering is:  ‘Hail,  Emperor,  who  are  about  to  die  salute you’.  In  fact,  however,  the  Latin  words  express a  perfect  antithesis.  According  to  my  opinion, their  original  meaning  was:  ‘Live,  Emperor! They  who  are  about  to  die  salute  you.’) avellan,  avellane,  adj . ,  pertaining  to,  or  resembling, a  filbert  or  hazel.  —  Fr.  L.  avellana ,  ‘filbert’, shortened  from  nux  avellana,  lit.  ‘nut  of  Avella’, fr.  Avella,  Abella ,  name  of  a  town  in  Campania, abounding  in  nuts.  See  apple.
4410:banzai,  interj.,  form  of  greeting  addressed  to  the Emperor  of  Japan.  —  Jap.  ‘may  you  live  ten thousand  years’.  Cp.  Chin,  wan,  ‘myriad’,  sui, ‘year’.
16637:Derivatives:  grease ,  tr.  v.,  greas-er,  n.,  greas-y, adj.,  greas-i-ly,  adv.,  greas-i-ness,  n. great,  adj.  —  ME.  great,  gret,  greet,  grete,  fr.
16658:greet,  tr.  v.,  to  salute.  —  ME.  greten,  fr.  OE. gretan,  ‘to  address,  approach,  visit,  greet’,  rel. to  OS.  grotian,  OFris.  greta,  Du.  groeten,  OHG. gruoyen,  MHG.  griieyen,  G.  griifien,  ‘to  salute, greet’,  fr.  Teut.  base  *grdtjan,  orig.  ‘to  cause  to speak’,  whence  also  OE.  gretan,  grxtan,  ‘to weep,  bewail’.  See  next  word.
16659:Derivatives:  greet-er,  n.,  greet-ing,  n.,  greet-ing- ly,  adv.
16660:greet,  intr.  v.,  to  weep;  tr.  v.,  to  bewail  (archaic or  dial.)  —  ME.  greten,  graten,  fr.  OE.  gretan, grxtan,  ‘to  weep,  bewail',  rel.  to  OS.  gratan, ON.  grata,  Dan.  grxde,  Goth,  gretan,  greitan, ‘to  weep’,  ON.  grata,  ‘to  cause  to  weep,  cry’. The  orig.  sense  of  all  these  verbs  was  ‘to  sound, speak,  shout’.  They  derive  from  I.-E.  base *ghred-,  ‘to  sound,  clash,  speak  loudly’,  whence also  OI.  hrddate,  ‘it  sounds,  rustles'.  See  greet, ‘to  salute’,  and  cp.  regret.
16661:Derivatives:  greet-er,  n.,  greet-ing,  n. greffier,  n.,  registrar.  —  F.,  ‘clerk  of  the  court, registrar’,  fr.  ML.  graphiarius,  fr.  L.  graphium, ‘a  writing  style’.  See  graft  and  -ier. gregarious,  adj.,  pertaining  to  a  flock;  living  in flocks.  —  L.  gregarius,  ‘pertaining  to  a  flock’, fr.  grex,  gen .gregis,  ‘flock’,  fr.  I.-E.  base  *gre-g-, partial  reduplication  of  base  *gere-,  *ger-,  ‘to gather  together,  assemble’,  whence  Gk.  dyci- petv,  ‘to  assemble’,  ayopa,  ‘assembly;  place  of assembly’,  oiyupu;,  ‘assembly’,  dyupTY)<;,  ‘beg¬ gar’,  OSlav.  grusti  (for  *g[-s-ti-),  ‘handful’, Lith.  gurgulys,  ‘chaos,  confusion’,  gurguoli, ‘crowd,  mass’,  and  Gk.  xi  ydpyapa  (Hesychius), ‘crowd,  plenty’  and  possibly  also  OI.  ganah (for  *gf(ia-),  ‘herd,  troop,  company’.  Cp.  aggre¬ gate,  congregate,  egregious,  segregate.  Cp.  also agora,  allegory,  category,  panegyric,  paregoric. Cp.  also  cram.
=== AHD gher ===
gheled-. Hail. Zero-grade form *ghled- in Greek khalaza (< *khalad-ya), a hailstone, hard lump, also a small cyst: CHALAZA, CHALAZION. [Pok. ghelsd- 435.]
gheli-. Tortoise. Suffixed form “ghel-dnd in Greek khe- l6né, tortoise: CHELONIAN. [Pok. ghel-du- 435.] ghel-una. Jaw. 1. Germanic *geliz in Old Norse *gil, gill of a fish, akin to the Scandinavian source of Middle English gile, gill: GILL!. 2. Suffixed variant form *ghel-wo- in Greek kheilos, lip: CHEILOSIS, CHILOPOD. [Pok. ghelunda 436.]
ghen-. To gnaw. Hypothetical base of various Germanic forms. 1. Germanic *gnagan in: a. Old English gnagan, to gnaw: GNAW; b. Old Norse gnaga, to bite, akin to the probable Scandinavian source of NAG!. 2. Suffixed Ger- manic form “gnag-sk- in *(g)naskon in Old High German nascon, to nibble: NOSH. 3. Perhaps related is Germanic *gnatt-, “biting insect,” in Old English gnzt, gnat: GNAT. [Pok. ghen- 436.]
ghend-. Also ghed-. To seize, take. 1. Germanic *getan in: a. Old Norse getfa, to get: GET; b. compound *bigetan (*bi-, intensive prefix; see ambhi), to acquire, in Old English begietan, to get, beget: BEGET; C. compound *fer-getan (*fer-, prefix denoting rejection; see per’), “to lose one’s hold,” forget, in Old English forg(iJetan, to forget: FORGET. 2. Germanic “getison, “to try to get,” aim at, in Old Swedish gissa, to guess, akin to the Scandinavian source of Middle English gessen, to guess: GuEss. 3. Basic form *ghend- in Latin prendere, prehen- dere (pre-, prae-, before; see per'), to get hold of, seize, grasp: PREHENSILE, PREHENSION, PRISON, PRIZE?, (PRIZES), (PRY2); APPREHEND, (APPRENTICE), (APPRISE), COMPREHEND, COMPRISE, EMPRISE, ENTERPRISE, (EN- TREPRENEUR), MISPRISION, PREGNABLE, REPREHEND, (REPRISAL), (REPRISE), SURPRISE. 4. Form “ghed- in Latin praeda, booty (< *prai-heda, “something seized before”; prai-, prae-, before; see per'): PREDATORY, PREY, SPREE; DEPREDATE, OSPREY. [Pok. ghend- 437.]
ghendh-. Abscess, boil. Zero-grade form *ghndh- in Germanic *gund- in Old English gund, pus: GROUNDSEL!. [Pok. ghendh- 438.]
ghengh-. To go, walk. 1. Germanic “gang-, a going, in: a. Old English gang, a going: GANG}; b. Old High Ger- man gang, a going: GANGUE. 2. Germanic “gangan, to go, walk, in Old English gangan, to go: GANGLING. [Pok. ghengh- 438.]
gher-'. To grasp, enclose; with derivatives meaning “enclosure.” 1. Suffixed zero-grade form *ghr-dh- in: a. Germanic *gurdjan in Old English gyrdan, to gird: GIRD; b. Old English gyrdel, girdle: GIRDLE; c. Old Norse gjordh, girdle, girth: GirTH. 2. Suffixed o-grade form *ghor-dho- (in Germanic) or *ghor-to-, an enclosure, in: a. Germanic *gardaz in (i) Old English geard, enclosure, garden, yard: YARD?; ORCHARD (ii) Old Norse gardhr, garden, yard: GARTH (iii) Old High German garto, gar- den: KINDERGARTEN (iv) Old North French gardin, gar- den: GARDEN (v) compound *midja-gardaz, “middle zone,” earth (see medhyo-); b. Latin hortus, garden: HORTICULTURE, ORCHARD, ORTOLAN. 3. Prefixed and suffixed zero-grade form *ko(m)-ghr-ti- (*ko(m)-, collec- tive prefix, “together”; see kom) in Latin cohors (stem cohort-), enclosed yard, company of soldiers, multitude: COHORT, CORTEGE, COURT, COURTEOUS, COURTESAN, (COURTESY), COURTIER, (CURTILAGE), (CURTSY). 4. Per- haps suffixed o-grade form *ghor-o- in Greek khoros, dancing ground (? perhaps originally a special enclosure for dancing), dance, dramatic chorus: (CHOIR), (CHORAL), (CHORALE), CHORIC, (CHORISTER), CHORUS; CHORAGUS, TERPSICHORE. [Pok. 4. gher- 442, gherd- 444.]
gher-2. To call out. Extended root *ghréd-. Germanic *grotjan in Old English grétan, to speak to, greet: GREET. [Pok. 1. gher- 439.]
gheu-
gher-’. To shine, glow; gray. Hypothetical base of various Germanic forms. 1. Germanic *gréwaz, gray, in: a. Old English greg, gray: GRAY; b. probably Old English grighund, greyhound: GREYHOUND. 2. Germanic *gris- Jaz, gray, in: a. Old French gris (> French gris), gray: GRISAILLE, (GRISETTE), (GRISON), GRIZZLE; AMBERGRIS; b. Medieval Latin griseus, gray, grayish: GRISEOUS. [Pok. 3. gher- 441.] gher-4. To scrape, scratch. 1. Extended zero-grade form *ghr(e)-k- in: a. Greek kharax, a pointed stake, also a kind of sea bream: CHARACIN; b. Greek kharassein, to sharpen, notch, carve, cut: CHARACTER, GASH. 2. Ex- tended form *ghers-.in suffixed zero-grade form *ghrs-to- perhaps (but unlikely) in Sanskrit ghattah, ghat: GHAT. See also extensions ghréi- and ghréu-. [Pok. 2. gher- 439.] gher-5. To like, want. 1. Suffixed form *gher-n- in Ger- manic “*gernjan in Old English giernan, gyrnan, to strive, desire, yearn: YEARN. 2. Extended form *ghré- possibly in: a. Germanic *gréduz, hunger, forming *grédagaz, hungry, in Old English grédig, hungry, covetous, greedy: GREEDY; b. Greek khré, it is necessary, whence krésthai, to lack, want, use: CATACHRESIS, CHRESARD, CHRESTOM- ATHY. 3. Suffixed zero-grade form *ghr-td- in Latin hortari, to urge on, encourage (< “to cause to strive or desire”): HORTATIVE; EXHORT. 4. Suffixed zero-grade form “ghr-i- in Greek kharis, grace, favor: CHARISMA; Eucnarist. [Pok. 1. gher- 440.] ghere-. Gut, entrail. 1. Suffixed form *ghero-no- in Ger- manic *garn6, string, in Old English gearn, yarn: YARN. 2. Suffixed form *ghero-n- in Latin hernia, “protruded viscus,” rupture, hernia: HERNIA. 3. Suffixed o-grade form *ghoro-d- in Greek khordé, gut, string: (CHORD?), CORD, (CORDON); HARPSICHORD, TETRACHORD. 4. O-grade form *ghors- in Greek khorion, intestinal membrane, afterbirth: CHORION. 5. Possible suffixed zero-grade form *ghr-u- in Latin haruspex (-spex, “he who sees” < *spek-, “to see”; see spek-), “he who inspects entrails,” diviner (but perhaps borrowed from Etruscan): HARUSPEX. [Pok. 5. gher- 443.] ghers-. To bristle. 1. Extended zero-grade form *ghrzd-, prickly plant, in: a. Germanic *gorst- in Old English gorst, furze, gorse: GORSE; b. Latin hordeum, barley: ORGEAT. 2. Lengthened-grade form *ghér(s)- in Latin hér, ér, hedgehog: URCHIN. 3. Suffixed lengthened-grade form *ghér(s)-ika in Latin ériica, caterpillar: ROCKET?. 4. Suffixed full-grade form *gher-tu-, remade to *hirsu- in Latin hirsitus, bristly, shaggy, hairy: HIRSUTE. 5. Suf- fixed full-grade form *ghers-ko- in Latin hispidus (prob- ably a dialectal borrowing), bristly, shaggy, prickly: HISPID. 6. Suffixed o-grade form “ghors-eyo- in Latin horrére, to bristle, shudder, be terrified, look frightful: HORROR; ABHOR, ORDURE. 7. Suffixed full-grade form *ghers-o- in Greek khersos, dry land: CHERSONESE. [Pok. Bhers- 445.] gheslo-. Seen by some as a base for words meaning “thousand.” 1, Suffixed form *ghesl-yo- in Greek khilioi, thousand: CHILIAD, KILO-. 2. Latin mille, thousand, which has been analyzed as *smi-, “one” + a form *ghsli-, is of obscure origin: MIL!, MIL2, MILE, MILLE- NARY, MILLESIMAL, MILLI-, MILLIEME, MILLION; MIL- FOIL, MILLENNIUM, MILLEPORE, MILLIARY, MILLIPEDE. [Pok. ghéslo- 446.] ghesor-. Hand. Reduced form “ghesr- in Greek kheir, hand: CHIRO-; (CHIRURGEON), ENCHIRIDION, (SURGEON), SURGERY. [Pok. 1. 8hesor- 447.] gheu-. To pour, pour a libation. I. Extended form *gheud-. 1. Zero-grade form *ghud- in Germanic *gut- in Old English guttas, intestines: GuT. 2. Nasalized zero-grade form *ghu-n-d- in Latin fundere, to pour: FOISON, FONDANT, FONDUE, FONT, FOUND2, FUNNEL, FUSE?, FUSILE, FUSION; AFFUSION, CIRCUMFUSE, CON- FOUND, CONFUSE, DIFFUSE, EFFUSE, INFUSE, PERFUSE, PROFUSE, REFUND!, (REFUSE!), (REFUSE?), SUFFUSE,
ghéu-
TRANSFUSE. II. Extended form *gheus-. 1. Germanic zero-grade form *gus- in: a. suffixed form *gustiz in Old Norse gustr, a cold blast of wind: cusT!; b. Icelandic gusa, to gush, perhaps akin to Middle English gushen, to gush: GUSH. 2. Germanic suffixed o-grade form *gausjan in Old Norse geysa, to gush: GEYSER. III. Suffixed form *gheu-ti- in Latin fatilis, “(of a vessel) easily emptied, leaky,” hence untrustworthy, useless: FUTILE. IV. Basic form *gheu- in Greek khein, to pour: CHOANA, CHYLE, (CHYME); CHOANOCYTE, ECCHYMOSIS, PARENCHYMA. [Pok. gheu- 447.] ghéu-. To yawn, gape. Compare ghai-. 1. Germanic suffixed form g6-ma- in Old English goma, palate, jaw: GuM?, 2. Variant form *ghau- in Greek khaos, chasm, empty space, chaos: CHAOS, GAS. [Pok. ghéu- 449.] gheu(e)-. To call, invoke. Suffixed zero-grade form *ghu-to-, “the invoked,” god, in Germanic *gudam, god, in: a. Old English god, god: Gop; b. Germanic *gud-igaz, possessed by a god, in Old English gydig, gidig, possessed, insane: GIDDY. [Pok. ghau- 413.] gh6. Behind, after. Slavic *za in Russian za, by, to: SASTRUGA. [Pok. 26 451.] ghos-ti-. Stranger, guest, host; properly “someone with whom one has reciprocal duties of hospitality.” 1. Basic form *ghos-ti- in: a. Germanic *gastiz in Old Norse gestr, guest: GUEST; b. Latin hostis, enemy (< stranger): HOST?, (HOSTILE). 2. Compound “ghos-pot-, *ghos-po(d)-, “guest-master,” one who symbolizes the relationship of reciprocal obligation (*pot-, master; see poti-), in Latin hospes (stem hospit-), host, guest, stranger: (HOSPICE), (HOSPITAL), (HOSPITALITY), HOST!, (HOSTAGE), (HOSTEL), (HOSTLER). See also xenos. [Pok. ghosti-s 453.] ghow-é-. To honor, revere, worship. 1. Germanic *gaw6n in Old Norse gd, to heed: GAWK. 2. Basic form *ghow-é- in Latin favére, to favor, be favorable: FAVOR, (FAVOR- ITE). [Pok. ghou(é)- 453.] ghré-. To grow, become green. Contracted from “ghreo-. 1. O-grade form “ghré- in Germanic *grd(w)an in Old English gréwan, to grow: GROW. 2. Suffixed o-grade form *ghro-nyo- in Germanic *grénjaz, green, in Old English gréne, green: GREEN. 3. Suffixed zero-grade form *“ghro-so- in Germanic *grasam, grass, in Old English grees, grass: GRASS. [Pok. ghré- 454.] ghrebh-'. To seize, reach. 1. Zero-grade form *ghrbh- in Sanskrit grbhndati, grhndati, he seizes: SATYAGRAHA. 2. Parallel (imitative) Germanic creations with base *grab-, *grap- in: a. Middle English graspen, to grasp: GRASP; b. Middle Dutch and Middle Low German grab- ben, to seize: GRAB. [Pok. 1. ghrebh- 455.] ghrebh-?. To dig, bury, scratch. 1. O-grade form “ghrobh- in: a. Germanic *graban in (i) Old English grafan, to dig, engrave, scratch, carve: GRAVE3; (EN- GRAVE) (ii) Old High German graban, to dig: GRABEN (iii) Old French graver, to engrave: GRAVURE; b. Germanic *grabam in Old English grzf, trench, grave: GRAVE}. 2. Germanic *grub(byan (with secondary ablaut) in Old English *grybban (> Middle English grubben), to dig: GRUB. 3. Germanic *gr6b6 in Middle Dutch groeve, ditch: GROOVE. 4. Perhaps Germanic *greub- in Low German greven, fibrous refuse of tallow: GREAVES. [Pok. 2. ghrebh- 455.] ghredh-. To walk, go. Suffixed zero-grade form ghrdh-yo- in: a. Latin gradi (past participle gressus), to walk, go: GRESSORIAL; AGGRESS, CONGRESS, DEGRESSION, DI- GRESS, EGRESS, INGRESS, PLANTIGRADE, PROGRESS, RE- GRESS, RETROGRESS, TRANSGRESS; b. Latin gradus (< deverbative *grad-u-), step, stage, degree, rank: GRADE; CENTIGRADE, DEGRADE, DEGREE, RETROGRADE. [Pok. ghredh- 456.] ghréi-. To rub. A derivative of gher-4. 1. Germanic *gris-, to frighten (< “to grate on the mind”), in Old English grislic, terrifying: GRISLY. 2. Germanic *grim-, smear, in Middle Dutch grime, grime, akin to the source of Middle English grime, grime: GRIME. 3. Extended form *ghris-
gno-
in Greek khriein, to anoint: CHRISM, CHRIST, CHRISTEN, (CHRISTIAN); (CHRISTMAS). [Pok. ghréi- 457.] ghreib-. To grip. 1. Germanic *grip- in Old English gripe, grasp, and gripa, handful: crip!. 2. Germanic *gripan in: a. Old English gripan, to grasp: GRIPE; b. Old French gripper, to seize: GRIPPE. 3. Suffixed o-grade form *ghroib-eyo- in Germanic *graipjan in Old English grd- pian, to feel for, grope: GROPE. [Pok. ghreib- 457.] ghrem-. Angry. 1. Germanic *grimmaz in: a. Old English grim(m), fierce, severe: GRIM; b. Old French grimace, a grimace: GRIMACE. 2. Germanic *grum- in Middle Dutch grommen, to mutter angrily, probably akin to Middle English grummen, to grumble: GRUMBLE. 3. Suffixed o-grade form *ghrom-o- in Russian grom, thunder: Po- crom. [Pok. 2. ghrem- 458.] ghrendh-. To grind. 1. Germanic “grindan in Old Eng- lish grindan, to grind: GRIND. 2. Germanic *grinst-, a grinding, in Old English grist, the action of grinding: GRisT. 3. Latin frénum (< frendere, to grind), horse’s bit (on which its teeth grind), bridle: FRENULUM, FRENUM; REFRAIN). 4, Variant form *ghrend- is sometimes but improbably regarded as the root of Greek khondros, granule, groats, hence cartilage: CHONDRO-; HYPOCHON- DRIA, MITOCHONDRION. [Pok. ghren- 459.] ghréu-. To rub, grind. Extension of gher-4. 1. Germanic *greut- in Old English gréot, sand, gravel: GRIT. 2. Ger- manic *grut- in Old English grotan, pieces of hulled grain, groats: GROATS. 3. Germanic “grit- in: a. Old English griit, coarse meal: GRouT; b. Old French gruel, porridge: GRUEL. 4, Germanic *grautaz, coarse, thick (< “coarsely ground”), in: a. Old English gréat, coarse, thick, bulky, large: GREAT; b. Middle Dutch groot, thick: Groat. 5. Germanic *griiw-, to recoil from (< “to be offended, be grated on by”), in Middle Dutch griiwen, to abhor, akin to Middle English grue, horrible: GRUESOME. 6. Variant form *ghrow- in Greek khrés, skin (< “rough surface” ?), hence flesh, complexion, color: RHODOCHRO- SITE. 7. Suffixed variant form *ghré-mn in Greek khréma, skin, complexion, color (semantic development as in 6. above): CHROMA, CHROMATIC, CHROMATO-, CHROME, -CHROME, (CHROMIUM), CHROMO-; ACHRO- Matic. 8. Probably Celtic *graw- in Old French grave, greve, coarse sand, gravel: GRAVEL. 9. Probably Latin *grau-, to touch, graze, in con-gruere, to agree (com-, together; see kom): CONGRUENT. [Pok. 2. ghréu- 460.] ghwer-. Wild beast. 1. Suffixed form *ghwer-o- in Latin ferus, wild: FERAL, FIERCE. 2. Compound *ghwero-okv-, “of wild aspect” (*-ak-, “-looking”; see okw-), in Latin feréx (stem feréc-), fierce: FEROCIOUS. 3. Length- ened-grade form *ghwér- in Greek thér, wild beast: TREACLE; THEROPOD. [Pok. ghuér- 493.] gladh-. Smooth. Suffixed form “gladh-ro- in Latin gla- ber, smooth, bald: GABRO, (GLABELLA), GLABROUS. gleubh-. To cut, cleave. 1. Germanic *k/euban in Old English cléofan, to split, cleave: CLEAVE!. 2. Germanic *klub-, a splitting, in: a. Old English clufu, clove (of garlic): CLOVE*; b. Middle Dutch clove, a cleft: KLOOF. 3. Germanic *k/aubri- in: a. Old Norse kleyfr, easy to split, perhaps akin to Middle English cliver, “expert in seizing,” skillful: CLEVER; b. Old Norse lofi, a cleft, akin to English clevi, “cleft instrument,” clevis: CLEVIS. 4. Zero-grade form *glubh- in Greek gluphein, to carve: GLYPH, GLYPTIC; ANAGLYPH, HIEROGLYPHIC. 5. Suffixed zero-grade form *glubh-md- in Latin glima, husk of grain: GLUME. [Pok. gleubh- 401.] glégh-. Thorn, point. 1. Suffixed form *glégh-i- in Greek glokhis, barb of an arrow: GLOCHIDIUM. 2. Suffixed form *glégh-ya in Greek gléssa, glétta, tongue, hence also language: GLOSS2, (GLOSSARY), GLOTTIS; BUGLOSS, GLOS- SOLALIA, ISOGLOSS, POLYGLOT, PROGLOTTID. [Pok. glégh- 402.] gno-. To know. Contracted from *gnoo-. 1. Variant form *gné- in Germanic *kné(w)- in Old English cndwan, to know: KNOW. 2. Zero-grade form *gno- in: a. Germanic
gras-
*kunnan in Old English cunnan, to know, know how to, be able to (Old English first and third singular can from Germanic *kann from o-grade *gona-): CAN}, CON2, CUN- NING; b. Germanic causative verb *kannjan, to make known, in Old English cennan, to declare, and Old Norse kenna, to name (in a formal poetic metaphor): KEN, KENNING; c. Germanic *kunthaz in Old English cath, known, well-known, usual, excellent, familiar: (COUTH); UNCOUTH; d. Germanic *kunthithd in Old English cyth(the), cyththu, knowledge, acquaintance, friendship, kinfolk: KrTH. 3. Suffixed form *gné-sko- in Latin (g)n6- Scere, cognéscere, to get to know, get acquainted with: NOTICE, NOTIFY, NOTION, NOTORIOUS; (ACQUAINT), COG- NITION, (COGNIZANCE), (CONNOISSEUR), (QUAINT), REC- OGNIZE. 4. Suffixed form *gné-ro- in Latin igndrdre, not to know, to disregard (i- for in-, not; see ne): IGNORANT, IGNORE. 5. Suffixed form *gn6-dhli- in Latin nobilis, knowable, known, famous, noble: NOBLE. 6. Redupli- cated and suffixed form *gi-gn6é-sko- in Greek gignd- skein, to know, think, judge (and *gnd- in gndm6n, a judge, interpreter): GNOME2, GNOMON, GNOSIS; AGNOSIA, DIAGNOSIS, PATHOGNOMIC, PHYSIOGNOMY, PROGNOSIS. 7. Suffixed zero-grade form “gna-ro- in Latin gndrus, knowing, expert, whence narrdre (< *gnarrare), to tell, relate: NARRATE. (8. Traditionally but improbably re- ferred here are: a. Latin nota, a mark, note, sign, cipher, shorthand character: NOTE; ANNOTATE, CONNOTE, PRO- THONOTARY; b. Latin norma, carpenter’s square, rule, pattern, precept: NORM, NORMA, NORMAL; ABNORMAL, ENORMOUS.) [Pok. 2. gen- 376.]
```


## [2026-09-06T02:17:47.825Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10630,10690p' FVQ.txt",
 "description": "Read FVQ around Sard"
}
```


### [2026-09-06T02:17:47.873Z] TOOL RESULT

```
3 Hubschmann, Arm. Gramm, i, 241. 

4 Noldeke, Mand. Gramm, xxxi ; Lagarde, Ubersicht, 176 n. ; Fraenkel, Fremdw, 
29. It may be argued, however, that the Mand. form is from ^Arabic. 

6 So bi"1D in Dan. iii, 21, 27. Vide Andreas in the Glossary to Marti's Gram- 
matik d. bibl. aram. Sprache, 1896, and the other suggestions discussed by S. A. Cook 
in the Journal of Philology, xxvi, 306 ff., in an article " The Articles of Dress in Dan. 
in, 21 ". 



FOREIGN VOCABULARY OF THE QUR'AN 169 



form. Syr. U^r*> however, like Gk. crapd/3aX\a, seems to have been 
used particularly for breeches. 1 All these, of course, are borrowings 
from Iranian, but the probabilities seem to be that the word was an 
early loan-word in Arabic from Aramaic. 

^^ 

*j~ (Sard). 


xxxiv, 10. 

Chain armour, i.e. work of rings woven together. 

It occurs only in a passage relating to David's skill as an armourer. 

The Muslim authorities derive it from 5^*** to stitch or sew (cf. 

Raghib, Mufradat, 229), though it is curious that they know that 
armourer ought to be Zarrad rather than Sarrad (as-Sijistani, 177). 

As a matter of fact }~ seems to be but a form of ^jj, which, like 



j*-> was commonly used among the Arabs. 2 This ^j J is a borrowing 
from Iranian sources as Fraonkel, Vocab, 13, noted. 3 Av. jjgjujij 
zraSa (AIW, 1703) moans a coat of mail, and becomes in Phlv. both 

-)J( zrih, whence Mod. Pers. ajj and Arm. qjw^f and also 

was borrowed into Syr. as ]*j]. 6 The word was a pre-lslamic borrow- 
ing, possibly direct from Persia, or maybe through Syriac. 

* 

.* (Safara). 

, Ixviii, 1; jjia^~, xvii, 00; xxxiii, 6 ; lii, 2; 



liv, 53 [also the forms J^L^LA, Ixxxviii, 22 ; and j^kx^a^, lii, 37]. 

To write, to inscribe.
```


## [2026-09-06T02:18:02.189Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in (23901,23823,20852):\n    ctx='\\n'.join(t[max(0,ln-40):ln+5])\n    tags=re.findall(r'\\[pdf page (\\d+)\\]', '\\n'.join(t[:ln]))\n    print(ln, 'last tag', tags[-1] if tags else None)\nprint('---context 23890-23930---')\nprint('\\n'.join(t[23885:23935]))\nEOF",
 "description": "Locate BQT زره page"
}
```


### [2026-09-06T02:18:03.823Z] TOOL RESULT

```
23901 last tag None
23823 last tag None
20852 last tag None
---context 23890-23930---
                                                         ‫کبهرنج پوست دباارشد ‪ ۴‬چرهزاز براج کوب‬
                        ‫مگیر =‬            ‫رد‬
                   ‫بازدهم باشد از ماهپای ملکی ‪۱‬‬
                                                                                      ‫رکاویند ‪.‬‬
 ‫ررمه = بفتح‌اول والك وسکون ثالی»‬                       ‫ربران * د بباای ابجدبالف کشیده‬
  ‫ایند*‪ -۱‬وبك لنگه بار واسباب‬
                            ‫رو‬‫بوفچرخت ک‬                                  ‫بروزن بزدان ‪ .‬باغبانرا گویند ‪.‬‬
 ‫وقماش را نکیفزته‌اند » و بکضویبند ابن لفت‬               ‫ررد ‏‪ = ٩‬بقتح اول وسکون نالی ودال‬
                    ‫غرمی است‪ »:‬وبکسی اول ات‬                     ‫ابجد (‪ » )۱‬پرخور وشکم خوار کروایند ‪.‬‬

 ‫دزم یوز بوامبیامی حطی (»)‬                               ‫ررده ‪ = ۷‬بقتح اول بر وزن زرده »‬
                                                              ‫بمعنی «انده وکوفته شده وآزرد‪ :‬راه باشد ‪.‬‬
‫جوز بمعنی تفحص و تجسی و جستجو کردن حم‬                    ‫درم = بفتح اول وسکون الی و میم »‬
                                    ‫‪٣‬‏‬    ‫آ مده ات‬       ‫بمعتی جنک و جدال باشد ‪ - ۸‬و هیمه وهیزم‬

    ‫زره د بنتح اول وتخفیف ثالی » ن‬                       ‫وی »‬
                                                            ‫طعام پختن را نیزگوند ‪ -‬و بفتحاتولال‬
‫‪۱‬ت‪ .۴‬وآن ناي ا هردوسوآیرا‬                 ‫‪E‬‬             ‫رنگه هم‌آمده‬     ‫بعنیر نگه میکنم‪٩‬‏ چه ربزمعتی‬




                                         ‫(‪ )۲‬چك ‪ :‬بامیم ویا‪.‬‬               ‫امد‬       ‫‪:‬‏‬   ‫(‪ )۱‬چك‬


   ‫رکه ‪:‬‬     ‫‪۴‬‬           ‫‪ ۴‬در ‪ :‬رنگرز ( رنگگ رزنده ) ‪.‬‬                  ‫‪ :‬رزیدن ‪.‬‬         ‫رکه‬
                                                                                            ‫‏‪٩‬‬
   ‫*‏ از ‪ :‬رز‬            ‫وید دوم) برنج ( منتهی الارب ) ‪۰‬‬
                                                       ‫اتولشد‬               ‫م‬
                                                                            ‫(ضرز‬
                                                                               ‫‪۴‬‬                     ‫ربخن ‪.‬‬
                                                   ‫(باغ وباغ انگور) (ه‪.‬م‪ ).‬بت بان (یسوند حفاظت ) ‪:‬‬
         ‫مادر ایز‪ ,‬بچگکایرا ندهد شیر همی ‪...‬‬                  ‫رزبان گفت چه رابت وچه ندییرهمی‬
    ‫«منوچهری دامخانی ‪ ۸۲۱‬ورك ‪ :‬رز‬
             ‫‪ ۷‬ظ ؛ مصحثف « زردهم» مخذف ‪ 5‬آزرده * ‪.‬‬                       ‫ری ‪.‬‬   ‫»‬   ‫رژد‬   ‫رك‪:‬‬   ‫‪۹‬‬


    ‫(ده وصف جنك) از ‪= 74۲‬‬   ‫‪ - ۸‬از پارسی باستان ‪٥ 200123۲‬‏ = اومتا ‪ 30152۲‬ر‬
   ‫[رك‪ :‬رده ] رك‪ :‬هو شمان‬     ‫هندوزرمالی (هند و ارویادی) ‪EET‬‏ قس‪ :‬خاشکریت ‪ijar‬‏ (رده سف)‬

                                ‫ارمنی ع ‪( 0۳22۲6۱۵۳‬جنکه) و ‪« 0122۲‬اسشق ‪۲۱۱٩‬‏ ‪.‬‬                             ‫‪۲‬‬
   ‫است‬   ‫سته‌شده‬   ‫آجیزیتکه‬     ‫بکراول»‬        ‫) عر ( «رزمه‬    ‫‪۹‬‬          ‫‪‎‬ندیزر > ‪.‬‬
                                                                                 ‫‪ _ ٩‬زا «‬
   ‫دربك جامه و آنرا بفارسی پشت وارء میگویند و آن قدری از جام بکجا بسته است که‌بریشت‬
                                                                        ‫توان برداشت ‪« ».‬شرح قاموس »‬
   ‫انون مخرمن؛عودسوز اکنون‌بتنگه‪.‬‬
                                ‫مثك ریز ک‬                     ‫خزبده اکنون برزهه» می‌بده اکنون برطل‬
   ‫‪ ۵‬منوچهری دامخالی ‪. ۸4۲‬‬
   ‫‪١۹‬ے‏ در فهرست ولف هل از فرهنك شاهنامةٌ عبدا لقادر نمرة ‪ ۵۸۹۷۲‬همین معتی آهده‪.‬‬
    ‫دوکه‬
```


## [2026-09-06T02:18:14.013Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\\|^\\[\" BQT_v2_pages.txt | head -5; echo \"---formfeeds---\"; python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nprint('ff count',t.count('\\f'))\nlines=t.split('\\n')\nprint('leaf of 23901:', '\\n'.join(lines[:23901]).count('\\f'))\n\"",
 "description": "Check BQT page structure"
}
```


## [2026-09-06T02:18:14.844Z] TOOL CALL #37: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1019 2>&1 | head -60",
 "description": "Fetch BQT page 1019"
}
```


### [2026-09-06T02:18:15.762Z] TOOL RESULT

```
---formfeeds---
ff count 683
leaf of 23901: 405
```


### [2026-09-06T02:18:17.660Z] TOOL RESULT

```
no scan of BQT covers printed page 1019 (see 'scans' in refs_online.json)
```


## [2026-09-06T02:18:22.724Z] TOOL CALL #38: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\"",
 "description": "BQT ref details"
}
```


### [2026-09-06T02:18:24.329Z] TOOL RESULT

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


## [2026-09-06T02:18:31.086Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==480' BQT_v2_pages.txt",
 "description": "Print BQT v2 leaf 479 (p.1019)"
}
```


### [2026-09-06T02:18:33.330Z] TOOL RESULT

```
  ‫ژروان بز رگ‬                                                                       ‫لاه —‬

‫رر نله = بفتح ارل بر وزن غریله »‬                     ‫وشناهمرست که حاکم شین سیستان بومها ‪-‬‬
 ‫ربوای راکوبند‪ .‬و آن‌رستنیی باشد معروف که‬            ‫وزرشك رالیز کوبند که البربارس باشد؟ وسر‬
          ‫خورند ومعرب آن زریلج است © ‪.‬‬              ‫کوه و قله کوه را همگفته اند‪ -‬و بمعنی کله‬

‫زرو ‪« ۲‬بروزن و مسنی زلو باشد چه‬                     ‫ميعنتی بضم اول هم‬
                                                                    ‫وایلغی اسبان باشد ؛ و با‬
                                                    ‫و بمعتی لو هم هت که لقیش‬        ‫آمده است ‪-‬‬
‫در فارسی رای بی نفطه بلام تبدیل مبیاید »‬
 ‫وآن جالورست که چون براعنا بچصبانند خون‬              ‫را گیفزته‌اندسویمعنی‬     ‫ددچ‪-‬ویه‬
                                                                                    ‫راش‬
                                                                                      ‫ونزه ب‬
                                                                                           ‫که‬
 ‫اآزنجا بمکد ‪ -‬ونام داروبی هم هت که مالند‬           ‫خردل هم هت ‪ -‬و زرد آب کل کاوشه رالیز‬
 ‫سرمه وتونیا درچشم کشند روشنایی چشم رازیاده‬                                          ‫کوند ‪. ۳‬‬
                                          ‫کند ‪.‬‬     ‫‪ ۰‬مخفف زرنیخ‬     ‫تی‬
                                                                      ‫رزن‬
                                                                        ‫رد نی ‪ -‬ببر و‬
 ‫زوراس بر وزن کربای ‪ ۰‬بممنی‬                         ‫است؟ ‪ ۰‬وآن جوهری باشد کانی رآن بردو لوع‬
 ‫سخاوت باشد که بذل بی‌سوا'ل است یعنی چیزی‬            ‫صنعت كيا‬       ‫ل‬
                                                                    ‫ار را‬
                                                                        ‫احم‬     ‫فرر‪.‬‬
                                                                                   ‫صحم‬
                                                                                     ‫وتا‪ :‬ا‬
                                                                                          ‫اس‬
     ‫بکی دادن پیآنکه او بطلید وبخواهد ‪9.‬‬                   ‫کار براندصفوی را استادان نقاش‪* .‬‬
 ‫زروان بدزرگ ‪ ۲‬د یکی ورن‬                            ‫رر نق ‪ -‬بفتح اول سوکون آخ رکه‬
 ‫بزبان پهلوی ‪٠‬‏ دام حضرت ابراهیم عليه اللام‬          ‫قاف باشد بروزن ومعنی زرلیخ است؟ ؛ وبکر‬


   ‫( ‪ ) 67218031221‬سدها ‪ , 606052665‬جتان »‬                         ‫‪ - ۱‬در قدیم ‪8‬‬
   ‫سیستان شده و آن شامل حوضة سفلای رود هلمند» شابد تا زمین داور میشد ‪ « .‬دائرة المعارف‬
   ‫اسلام ‪ .‬فراه ج ‪ ۱‬ص ‪ » ۷۵۱‬معرب آن زرنج است وبجای آن زاهدان کنولی است » وخرایف‬
  ‫آجا دیده مشود ‪ .‬حاکم صره سرداری بنام عبدالرحمن‌ن سمرة زاماحور‬
                                                              ‫های زرنگه هدوز در ل‬
   ‫ة الممارف اسللام ‪ .‬اسا ج‪۱‬‬       ‫حمله بستان کرد و او زرنج را درحصا ر گرفت وتخ رکرد ‪.‬را‬
    ‫‪ = ۴‬زرتك = ‪ « 51۲60۲61‬ثابتی ‪.*4۸۱‬‬                      ‫ص‪ > 4۸‬ورك ‪ :‬همان کناب ‪ :‬زرنج ‪.‬‬
                                                                                        ‫‪۱‬‬
                      ‫رك‪ :‬زریخ ‪.‬‬      ‫‪۴‬‬       ‫‪.‬‬    ‫دك‬
                                                    ‫مصحف «زرتك» ( م‪ ).‬وزركر‪:‬‬         ‫‪۴‬‬
   ‫زلو (هم‪).‬‬    ‫‪= ۹‬‬            ‫‪( 5601۲‬فر) د لك‪ ۲‬ص ‪٩ ۸۰۲‬‏ ‪.‬‬        ‫معرب زریلم ‏‬       ‫®‬
                                                                    ‫‪ :‬رك زروان ‪.‬‬     ‫‪۲‬‬
   ‫ح اول و کر آن ‪ .‬هوبد‪.‬ان احتمال داده همريشةٌ ‪( 22‬طلا) باشد ‏‬
                                                             ‫ت‪-‬‬‫فیخ‬
                                                                 ‫بررل‬
                                                                    ‫‪#‬‬
    ‫ارمنی ‪ ( 61۳22‬زرلیخ ) = پهلوی ‪ 2 1۲732‬از ‪* 611۳722‬‏ اوستا ‪(0 276132‬بجای‬
   ‫‪ 8102722-‬طلابی » ذرین) ؟«هوبشمان ‪ . ۲ 40۰‬بعضی آلرا مأخون از ‪ 8061065۲۸‬ونای‬
    ‫دانته‌اند ‪ ۶‬تفس >‪ .‬در فارسی ‪ :‬زرلی » زرله » زرلیق هم آمده ؛ ماده‌است سخت‪ .‬دارای‌هرارت‬
                                                           ‫معمول » رنکش ابرش براق ‪.‬راه‪ :‬زرنی‪.‬‬
     ‫لهماة‬
         ‫کار‬
           ‫بتاوب‬
               ‫‪ 0۵۷۳2‬بمعنی مان اس‬                 ‫ترا‬
                                                    ‫س» د‬
                                                       ‫ون‪,‬‬
                                                         ‫مآ‬‫‪#‬روان ‪ -‬بفتح اول و ا‬
                                                                              ‫ژ‬
    ‫(بمروز) آمده برای تعبین‌هنگام ظهر ‪ ۰‬ومکرر با کلمات ‪( 01289۳0‬دیر =‬                    ‫‪8‬‬
   ‫ومان دراز و بلند‪ .‬چندین بار زروان دو‬‫درنگ ) و ‪« 0122۳1‬دراز» آمده بممنی دیر زمانی ز‬
   ‫ردیف دیگر ابزدان نام برده شده وازآن فرشته زمانهٌ ببکراله اراده شده ‪ .‬اغلب زروان باصقات‬
   ‫‪ 6889۳2‬آمده که در « مینوخرد » پازند « زروان‬              ‫یرانه ) ر ‪21802۷5‬‬
                                                                            ‫دک‬            ‫‪8‬‬
     ‫درنگه خدای» ودر رسالة پارسی « علمای الام » به « زمان درنگه خدای » تعبیر شده است ‪.‬‬
    ‫بقهدرسفحة ‪۱۰۱‬‬
```


## [2026-09-06T02:18:42.428Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==481' BQT_v2_pages.txt",
 "description": "Print BQT v2 leaf 480"
}
```


### [2026-09-06T02:18:44.208Z] TOOL RESULT

```
 ‫‪ 0‬ات‬
                                                                                     ‫زروع‬



                       ‫نم اول بر وزن دروغ > | کیاهی است دوایی ‪.‬‬            ‫رروع =‬
‫زره = بکر اول و الی و ظهور های‬               ‫‪۱‬‬                ‫‪ 2‬آنبادی‬        ‫بمعی ا‬

‫زروك = بفتح‌اول بروزن مکه‌ك للم | حلقهای آهنین ترتیب داده الد و در روز های‬

         ‫زو گرفتم جمله اسب واشترش‪. ‎‬‬             ‫‪ - ٩‬نیز و گندا چون زروغ اشترست‬
 ‫پور بهای حامی «جهانگیری»‪۰ ‎‬‬

                                                                        ‫مه از صفحهٌ ‪۷۱۶۱‬‬
 ‫آرا همشه پابدار وبا بعبارت‬
                          ‫ازین دوصقت بیدامت که برای‌زمانه آغاز و انجامی تصورشده ب‬
 ‫دیگر قدیم وجاودانی دادته‌اند ‪ .‬درزاد سپرم فصل ‪ ۱‬بند ‪ 8۲‬زروان صراحة آفربدة اهور مزدا‬
  ‫محوب شده" درجمله حابی از اوستاکه از زروان باد شده اورافقط درردیف ابزدان دبگرآورده‬
  ‫درخور تیاب خواسساند ‪ .‬از مندرجات اوستا چنین مستفاد میشودکه زروان ایزد زمانهٌ سکرانه‬
  ‫و جاودانی است‪ .‬در عبارتی کاازنها (بسنا ‪ ۰۳‬بند ‪ ) ۳‬روان یکو کارو روح شر بمنزلةٌ ‪ ۵‬دو‬
‫کوهر همزاد » معرفی شده‌اند ‪ .‬بنا براین بنظر میرسه کهزرتشت بوهماصنلشایی اقدمکهپدر‬
 ‫واامنده ‪.‬‬‫تهشت او رمابیچخه ن‬
                           ‫دوروان مزبور باشد » عقیده داشته است ولی مملوم لزیتر ک‬
 ‫شك یت که بمدها زروان بمنزلة برورد کاری شناخته شده ‪ .‬درزمان هخامنشیان عقاید مختلفی‬
  ‫در باب ماهیت این پرورد کار وجود داشته است بسنی او را بامکان و برخی دبگر با زمان مکی‬
  ‫میداستند ‪ .‬عفیدة اخیر فایق آمد ‪ .‬در آبین »هربرستی عقده مربوط بزروان رباذبرفتند ‪.‬‬
  ‫مالی با اقتبای افکار زرتشتی عصرخود‪ .‬نام زروان ‪ 02۷۳17‬را مضدای بز رکه اطلاق کرده است‪.‬‬
 ‫برخی از محققان مذهب معمول مزدینی عبد ساسالی را همان زروانت دادته‌الد ‪ .‬بیاری از‬
  ‫بوسند کان‌ومورخان قاری پنجپ_هشتم میلادی امطورة ذیل‌را راجم بآفربش از عقابد ابرانیان‬
  ‫ون متملق بباین زروانی است ‪ :‬زروان » خدای نشتن » در هدت‬
                                                       ‫عپد ‪-‬اسانی نکقرلهده‌اند " آ‬
  ‫زار سال قربالی‌هاکود تا پسری بیابد ولم او را هرمزد نهد ‪ .‬اما عاقبت وی دربارٌ تأثیر قربالی‬
  ‫های خود بثك افتاد‪ .‬یں دو بردر بطن اویدید آ مدند‪ :‬یکی‌اهرمزد» چون وی قربائی کرده‌بود؛‬
 ‫دیگری اهریمن » زبرا که وی شك کرده بود ‪ .‬زروان وعده داد که پادشاهی جهان را بیکی از‬
  ‫آن درکه ژودتر بحضور اوآبد ‪ ۰‬عطا کند ‪ .‬یس اهریمن سنه يدر بشکافت و خود را يدو نمود‪.‬‬

  ‫زروان پرسید‪ :‬کیستی ! پاسخ داد ‪ :‬پسرنوام‪ :‬زروان گفت ‪ :‬پسرم دارای وی خوش ونورانی امت‬
  ‫و توظلمالی و بد بوبی! درین‌هنگام اهرمزد با پیکری تورانی ومسطر خوبشتن بدو نمود ‪ .‬زروان‬
  ‫او را پفرزدی شناخت‪ .‬اهریمن وعد پدر را بخاطر اوآورد‪ .‬زروان پاسخ داد که سلطتت جهاترا‬
  ‫مدت له هزار سال باهریمن خواهد داد » اما پس ازانشنای مدت مزیور اهرمزد تتهاسلطان جهان‬
  ‫(ضممة مجلة‬    ‫‪.‬پران ‪۰۳۳۱‬‬
                         ‫خواهد بود ‪ .‬رك ‪ :‬اقبال وابران باستان بقلم نگارندے دراقبال‌نامه ت‬
  ‫داش ) ص ‪ ۷۵ - ۱۵‬؛ پور داود ‪ .‬خرده اوستا‪.‬ص‪CİnaVFUZ + ۱۹-۷۹‬‏ بقلم ‪۲600622‬‬
  ‫بیمد‪ .‬ص‪٥۷٤‬‏ پیعد » ص ‪٩۷۸‬‏ یمد ؛ ج ص ‪ ۷۷۳‬بیمد »‬               ‫‪۰۳‬س‪۳‬‬
                                                                  ‫در ‪ 84058‬ے ×‪1‬‬
  ‫ص ‪۱*٩‬‏ بیعد‪ .‬بايد دانت که بمدها زروان را با زردشت وهر دو را با ابراهیم خلیل خلط‬
                                                              ‫کردماند‪ .‬رك ‪ :‬زروان بزرکه ‪۰‬‬
```


## [2026-09-06T02:18:56.636Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==482' BQT_v2_pages.txt | tail -30",
 "description": "Print BQT v2 leaf 481 tail"
}
```


### [2026-09-06T02:18:58.228Z] TOOL RESULT

```
      ‫آل ه‬
         ‫علتی است معروف ؛ و بکسر او‬                           ‫زردشت رگاوبند کهپیشوایآتش برستان باشد‪.‬‬
                                             ‫استخ‬

 ‫رر یرا = بروزن سرا ‪ .‬بلقت صربالی‬                            ‫بروزن و هنی زره تشت است که زردشت باشد ‪.‬‬

 ‫خرفه راگوبند و بعربی بقلةالمبار که وبقلةالحمقا‬              ‫‪ - ۳‬بپروزن مرهون» ببزان‬             ‫رهشون‬
                                        ‫خوانند ‪۹‬‬


                                    ‫‪.‬‬    ‫رشت‬
                                           ‫ق‪-‬‬‫(‪)۲‬چك ‪:‬‬                     ‫(‪ )۱‬چك ‪ :‬ژد و پاژند ‪.‬‬
   ‫‪ - ٩‬یولپب ‪ » 26۵‬دىزاپ ‪ » 267610‬ربارب یباتسوا ‪‎ « 2۲8002 -‬هملوتراب ‪. › ۱۷۰۳‬‬
     ‫ارمثی ع ‪ . ۷-۵۳2‬آرامی ع ‪ ( 042۲62‬و زرد ( بفتح اول دووم ) عربی‌ازان ماخوة است‬
   ‫(ره ) ‪ ,‬افقالی‪ ,2712‬بلوچی ط‪, 1612‬‬
                                   ‫ریک ‪ ,).2 0۵72 : ۷۵۷‬کردی ‪ ۴712 ۰ 1۲12‬ز‬ ‫(رك ‪ :‬ی‬
                                          ‫استی ‪(۲882‬زره) ‪ .‬رك‪ :‬اسشق وهویشمان ‪. ۰71‬‬
   ‫‪ ۴‬ؤس ‪ :‬پهلوی تا‪aj _ ۴ .872‬‏ « ‪. 88)(1)۵6۳۴(2)2‬‬             ‫‪ ۴‬رك ‪ :‬زریت‪.‬‬
   ‫‏‪ . zarh ntn‬یولهپ ‪ , 22120‬نداز « رکتوب ‏‪۲۵۱ ٩۱۰۸‬هلراهد * نیربانبو »نتوهرز*لصا‬
   ‫‪ ۵‬هز ‪ 8۵0۲22 . 899۲22 ,‬پپلوی ‪ [24530‬زمتان «بوتکر ‪› ۸۰۱‬‬                   ‫است‪: .‬‬
                     ‫رك ‪ :‬زردشت » زارتشت ‪.‬‬          ‫‪۱‬‬             ‫بتابرین زره پیج مصحف « زرپین» است ‪.‬‬
                         ‫‪ - ۷‬قرائتی است ازکمةٌبهلوی زروان ‪ . 0۵۷۲22‬رك ‪ :‬رزوان ‪.‬‬
               ‫‪ , 82010۵1112,‬پپنوی ‪ . 012151‬کاشتن «یونکر ‪۸۰٩‬‏ * ‪-‬‬
                                                                ‫‪ - ۸‬هز ‪2‬‬
    ‫‪ 17122.‬جزو اول بمعنی زرین وزرد رنگ وجزو دوم از رمشة‬                     ‫‏‪ - ٩‬در اوستا ‪1۵۷‬‬
    ‫‪ 8‬پهلوی ‪ ۲8۷‬فارسی بر (مینه) است؛ جمعاً بمعنی زرین بر وزرین جوشن ‪.‬زریی پر کی‬
   ‫اسپ و سپهبد ابران بوده است ‪ .‬رك ‪ :‬بشتها اص ‪ ۷۸۲‬ح و مزد مستا‬     ‫کادشرتکی‬
                                                                          ‫لهراسب و بر‬
                                                        ‫‪.‬‬    ‫‪ -‬رك ‪ :‬لك ‪ ۲‬ص ‪۷۰۲‬‬               ‫‪۰‬‬          ‫ص‪. ۸۳۳‬‬
```


## [2026-09-06T02:19:10.822Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"زرّاد\\|زراد\\|زرادخانه\" MON_part1.txt MON_part2.txt | head -20; echo \"=== ARY ===\"; grep -n \"زره\\|آغل\" incoming/ARY/ARY_pages.txt | head -20",
 "description": "Grep Mo'in zarrād and Aryanpur"
}
```


### [2026-09-06T02:19:10.916Z] TOOL RESULT

```
MON_part2.txt:15586:اهشتر.) کسجن کنه در زرادخانه کار کند» 
MON_part2.txt:15591:اسلحه خانه» سلاح‌خانه» زرادخانه. 
MON_part1.txt:70804:زراد: 71770 [معر .] (ص.) آنکه زره سازد؛ 
MON_part1.txt:70809:زرادگاه 2.25 [معر. ف - زرادگه] (امر.) 
MON_part1.txt:78972:را کرد آورند؛ زرادخانه» اسلحه‌خانه. 
=== ARY ===
3414:انگلیسی (6۸/01/5[7): 3 دا ری ۱۱ 0 (8۸0777833) زره
6657:افغانی (پشتو) (۸۳017۸47): لد ان زره ۱
7053:لیتوانی ((7247/1۵/)): اد زره :5 لمع ص۸4
9530:۱ بازگشت به؛ زره
9892:ز(زره اسب)؛ 2581287/۸0 (هشیار بیدار). به پندار من واژه‌ی "زندان" (پهلوی:2:)(210۸7
10164:انگلیسی (4ا8اا8(/0): لد با را زره 1054 عا8
10969:پارسي باستان (۳28۵(۷ 012): 811۳۷2718 تورس کهن (۸08۶5 0ا0): زره ایا
12475:بلوچی (1تلنانا8۸). زره گرتیک (0077710): 1۸
12563:پهلری (1تماتزمه): 22 انگلیسی (8۸/0/57): لد زره
15368:5 ,۸5 1 (۷۸88) زره ۱
15896:بازگشت به‌زرهم.
```


## [2026-09-06T02:19:11.725Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"agyl\\|aghyl\\|agil\\|Hürde\\|Pferch\" incoming/TTS/TTS_pages.txt | head -20",
 "description": "Grep Vámbéry for ağıl"
}
```


### [2026-09-06T02:19:11.783Z] TOOL RESULT

```
11026:     richt suvagila
14885:agil 5.                                           a/tce 5.
```


## [2026-09-06T02:19:19.466Z] TOOL CALL #44: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T02:19:19.473Z] TOOL RESULT

```


```


## [2026-09-06T02:19:23.506Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%BA%D9%84",
 "prompt": "Give the full etymology given for Persian آغل (āɣol) 'sheepfold, barn' — what origin does Wiktionary give (Turkic? Sogdian? Iranian)? Quote it."
}
```


## [2026-09-06T02:19:24.787Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D9%87",
 "prompt": "Give the full etymology for Persian زره (zereh) 'armour, coat of mail' — Middle Persian, Avestan forms, and any mention of Arabic زرد."
}
```


### [2026-09-06T02:20:04.932Z] TOOL RESULT

```
# Etymology of Persian آغل

Wiktionary presents **two possible origins** for this word, without definitively choosing one:

**Primary theory - Iranian origin:**
"Ultimately a derivative of Proto-Iranian *gauz- ("to hide, conceal"), compare Sanskrit गूहति (gūhati). Possibly influenced by Northeastern Iranian, compare Sogdian...āγōδ /, 'cover, shelter, barn'."

**Alternative theory - Turkic borrowing:**
"Alternatively, borrowed from a Turkic source: cognate with Ottoman Turkish آغل above."

The Wiktionary entry deliberately leaves the etymology uncertain, offering both a Proto-Iranian derivation (potentially influenced by Sogdian) and a Turkic borrowing hypothesis as plausible explanations.
```


### [2026-09-06T02:21:16.025Z] TOOL RESULT

```
# Etymology of Persian زره (zereh)

**Persian زره** derives from **Middle Persian** [script needed] (zlyh /⁠zrēy, zrēh⁠/), ultimately tracing to **Proto-Indo-European** _*ǵʰreh₁d-_ meaning "to sound, to ring."

## Avestan Connection
The Avestan form **𐬰𐬭𐬁𐬜𐬀-** (zrāδa-) means "chainmail, linkings to armor," providing linguistic evidence for the ancient military context.

## Related Language Borrowings
The word spread across neighboring linguistic communities through Iranian borrowing patterns. **Arabic زَرَد** (zarad) represents one such transmission, alongside Old Armenian, Old Georgian, Classical Syriac, and Jewish Babylonian Aramaic variants that share cognate forms.

This etymological family demonstrates how a Proto-Indo-European root describing sound or resonance became specialized terminology for protective metalwork across multiple ancient Near Eastern languages.
```


## [2026-09-06T02:21:27.252Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/a%C4%9F%C4%B1l",
 "prompt": "What etymology does Nişanyan give for Turkish ağıl 'sheepfold'? Quote the Old Turkic form and date, and any comment on Persian."
}
```


## [2026-09-06T02:21:27.564Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/regret",
 "prompt": "Give the full etymology of 'regret' — Old French regreter, and the Germanic/Old Norse element."
}
```


### [2026-09-06T02:21:33.518Z] TOOL RESULT

```
I cannot provide the requested etymology information based on the content supplied. The web page excerpt shown contains only the header, navigation elements, and footer of the Nişanyan Sözlük website—it does not include the actual dictionary entry for "ağıl" or any etymological details about the Old Turkic form, dating, or Persian connections.

To find this information, you would need to access the full dictionary entry for "ağıl" on the Nişanyan Sözlük website directly.
```


### [2026-09-06T02:21:33.970Z] TOOL RESULT

```
# Etymology of "Regret"

**Old French Origin:**
The word comes from Old French *regreter*, meaning "long after, bewail, lament someone's death." This comprises *re-* (an intensive prefix) plus *-greter*.

**Germanic Element:**
The *-greter* component likely derives from Frankish or another Germanic source. The dictionary notes it "compare[s] Old English *grætan* 'to weep'" and "Old Norse *grata* 'to weep, groan,'" both tracing back to Proto-Germanic *\*gretan* meaning "weep."

**Key Point:**
The etymology is notably complex because the word "is not found in other Romance languages, and variously explained." The Germanic weeping-related roots merged with Old French prefix structures to create the modern English term for sorrowful remembrance.
```


## [2026-09-06T02:21:38.744Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/gauzah",
 "prompt": "Does this page exist? What does it say about Proto-Iranian *gauz- 'to hide' and its descendants (Avestan, Old Persian, Sogdian)?"
}
```


## [2026-09-06T02:21:40.284Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D8%AF#Arabic",
 "prompt": "What etymology does Wiktionary give for Arabic زرد (zarad) 'coat of mail' and for زرّاد (zarrād)? Quote the origin."
}
```


### [2026-09-06T02:21:40.425Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T02:21:47.117Z] TOOL RESULT

```
# Etymology of Arabic زرد (zarad)

According to Wiktionary, the etymology for Arabic زرد (zarad) meaning 'coat of mail' comes from an early Iranian source. The entry states:

"From an early West Iranian source, probably via Aramaic זַרְדָּא / ܙܰܪܕܳܐ (zarədā)."

The derived term زَرَّاد (zarrād) means "who makes coats of mail" and derives from the same root ز ر د (z r d), but Wiktionary does not provide a separate distinct etymology for this particular word form—it simply appears as a derived term within the established semantic field of chainmail-related vocabulary.
```


## [2026-09-06T02:22:08.643Z] TOOL CALL #51: Bash

```json
{
 "command": "ls site/pages/193.jpg 2>/dev/null || echo \"no jpg\"; ls data/verification/sources/refs/ocr/ 2>/dev/null | head",
 "description": "Check for page image"
}
```


### [2026-09-06T02:22:08.690Z] TOOL RESULT

```
site/pages/193.jpg
AFM
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
```


## [2026-09-06T02:22:10.955Z] TOOL CALL #52: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/193.jpg"
}
```


### [2026-09-06T02:22:10.995Z] TOOL RESULT

```

```


## [2026-09-06T02:22:29.230Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN hide conceal ===\"; grep -n \"HIDE, CONCEAL\\|Hide, Conceal\\|gaud\\|gūhati\\|guhati\" SYN.txt | head -20",
 "description": "Grep Buck SYN"
}
```


### [2026-09-06T02:22:29.291Z] TOOL RESULT

```
=== SYN hide conceal ===
11144:Sp. joya, through OFr. joi(e), fr. Lat. gaudium ‘joy’. REW 3705.
21723:12.27 HIDE, CONCEAL
21763:guz-, OPers. gud- (in ma apagaudaya ‘do
27871:16.22 JOY apt Goth. fahéps Lith. dziaugsmas, links- xapt ON gledi, fagnadr mybe gaudium, laelitia Dan. glade, fryd Lett. prieks, liksma gioia Sw. glidje, fréjd ChSl. radostt joie OE geféa, blips, glednes, SCr. __radost alegria, gozo wynn Boh.  radost . veselte, bucurie ME blisse, tote, gladnes, Pol. radosé faille, sube, Githes wunne Russ. _radost’ athas, liithghair NE joy Skt. dnanda-, harsa-, lawenydd, dywenydd Du. vreugde mayas- levenez, joa OHG  gifeho, frewi, frewida, Av. mayd-, $dili-, urvaza- mendi, wunna MHG vréude, mende NHG freude
27881:2. Lat. gaudium (> Sp. gozo, Fr. joie > It. gioia) : gaudére ‘rejoice’, Grk. ynbiw, Dor. yapéw ‘rejoice’, Hom. yalav ‘rejoicing’, etc., root *gdu-. Walde-P. 1.529. Ernout-M. 411f. Walde-H. 1.584. REW 3705.
27900:5. Lith. dziaugsmas, fr. dzaugti-s “be glad, rejoice’, prob. with cons. transposi- tion fr. gaudz- : Lat. gaudium (above, 2). Walde-P. 1.529. Walde-H. 1.584.
```


## [2026-09-06T02:22:30.913Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 gheugh ===\"; grep -n \"gheugh\\|ghū̆gh\\|guzaeta\\|gūhati\\|guhati\" incoming/WLD/WLD_Bd1_pages.txt | head -20; echo \"=== IEC ===\"; grep -n \"gheugh\\|ghūgh\\|ghlad\" IEC.txt | head -10",
 "description": "Grep Walde-Pokorny and Mann"
}
```


### [2026-09-06T02:22:30.998Z] TOOL RESULT

```
=== WLD Bd1 gheugh ===
52831:mit ai. guhati ,,verbirgt ). Miihlenbach-Endzelin Lett.-D. Wb. I 6S5. 6S7.
53748:566                                                gheugh-   — gheugh-, ghugh-
53802: gheugh- etwa „spielend oder ausgelassen sich umbertreiben, ulken, Possen
53825:  gheugh-, ghugh-                      ,
53832:                       guzaeta ,    fra-guzayanta) „verbergen, verstecken",                  apers. yadiy
53850:Persson Beitr. 59.                 Ygl. *gheugh- ds., wo iiber versuchte Wzzerlegungen.
=== IEC ===
3968:geugil- (2), see gheughil- (gheughl-, gheugho)
4660:gheughilos, gheughos "Tool" Cf. geugos Ir. cf. guag ‘folly; fool’; guagaire ‘vagrant’;
4696:ghladh- ‘smooth, bright, glad" See next and cf. WP I, 626 OHG glat; MHG cf. also glete ‘lead-sludge’; OE glæd ‘bright, glad, kind; joy’; OS glad- modi ‘glad’; ON glað, Sw. glad, as E.; R cf. glod ‘whitethorn’. See SUPT: ghlad-
4697:ghlådh- (ghlàdhro-) ‘smooth, bright; lustre; white-flowering tree’. Cf. ghladh-. WP I, 626 Gk. cf. kléthros ‘alder; W glawdd ‘lustre’; OCS gladükü (‘smooth, level, and com. SL R also glad" ‘smooth place’; Cz. hlad', hlád', i-st. id.; Li. glodùs ‘smooth’. Verbal types: OCS glazdo, gladiti: Li. glodZiu, glosti ‘smooth, polish’. Cf. also LLat. glastum, It. glastro, glasto, Rum. glast *woad' fr. a Celtic source, cf. W Ir. glas, adj. “blue, green”, and Latv. glāsts ‘caress’, beside W gloddest, m. ‘tevel’. See SUPT: ghlad-
4698:ghlagh- “bright, smooth; white-flowering tree’. See ghladh-, ghladh-
4708:OE glom ‘twilight, gloom’; Big. glamav “silly” ghlastos, om ‘brilliant; brilliance’. Cf. ghladh-, ghladh-. Cf. WP I, 626 Gallo-Lat. glastum *woad'; glastinus ‘azure’; Mir glass, Ir. OBr. glas, W Cor. Br. glas “blue, green’. Ir. also ‘bright’; MHG, LG glast, m. ‘brilliance’. Long-gde in Latv. glasts "fond. ing; variant in Cz. hat “smooth surface beside hlad', see ghladh-.
4733:ghlódhos, à, io, us 'smooth, bright; smooth- ness, brilliance’. Cf. ghladh- Alb. gledhé ‘fondling; flattery’; W glawdd (lustre, ambig. cf. ghladh-); MHG gluot, Du. gloed, OE glede, ON glóð “ember, am- big. see ghládh-); Li. gluodas, -ùs smooth’, beside glodüs, id., see ghladh-); Latv. cf., glodens ‘smooth’. For Sl. gladükü, etc. see ghladh-
```


## [2026-09-06T02:22:39.373Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21755,21775p' SYN.txt; echo \"=== leaf ===\"; python3 -c \"\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nprint('leaf',  '\\n'.join(t[:21763]).count('\\f'))\"",
 "description": "Read Buck 12.27"
}
```


### [2026-09-06T02:22:41.336Z] TOOL RESULT

```
Du. versteken, NHG verstecken (MHG verstecken only ‘cause to choke’), lit. ‘stick away’.
6. Lith. slépti, Lett. slépt : Grk. xdéq- tw, Goth. hlifan ‘steal’, etc. (11.56). Walde-P. 1.497. Miibl.-Endz. 3.930.
7. ChSl. stikryti, etc., general Slavic : Grk. xpimrw, etc. (above, 2).
Boh. schovati, Pol. schowaé ‘preserve’ and ‘hide’, epds. of Boh. chovati, Pol. chowaé ‘keep, preserve’ (11.24).
Russ. prjatat’ : ChSl. o-pretatt ‘adorn, cover’ (with clothing), vtiz-pretati ‘de- prive’ (Supr.), SCr. pretati ‘cover with ashes’, Pol. sprzataé ‘clear away’, etc.,
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
852 SELECTED INDO-EUROPEAN SYNONYMS
etym. and primary sense dub., but Russ. ‘hide’ obviously fr. ‘cover’. Miklosich 262f. Brickner 436 f.
guz-, OPers. gud- (in ma apagaudaya ‘do
something warm’ (cf. NSB 8.V.). Walde
not hide’) perh. : Lith. gaz ‘cover
8. Skt. guh- (8sg. pres. giuhati), Av. | P. 1.566 f. 12.31 HIGH
Grk. més Goth. hauhs Lith. auk3tas NG ymros ON har Lett. augsts Lat. altus, (ex)celsus Dan. hf ChSl.  vysokit It. alto Sw. hég SCr. _visok Fr. haut OE héah Boh. — vysoky Sp. alto ME heigh Pol. wysoki Rum, inalt NE high Russ. vysokij Ir. ard, uasal Du. hoog Skt. ucca-, unnata- Nir. Grd OHG hoh Av. baraz-, barazant- W. uchel MHG hich Br. uhel NHG hoch
Words for ‘high’ are partly from ad- verbs for ‘above, over, up’, partly from notions like ‘grown up’, ‘heaped up’, etc.
1. Grk. tyndos, NG pop. yds; Ir. uasal, W. uchel, Br. whel, Corn. huhel, Gall. Uxello-(diinum); ChSl. vysoki, etc., general Slavic group: Grk. iw adv. ‘high’, Ir. 6s, was, W. uch, Corn. ugh ‘above, over’, fr. IE *up(e)s-, etc., be- side *wpo- in Grk. jré ‘under’, Skt. wpa ‘unto’, Ir. fo, Goth. uf ‘under’, etc. (for the contrast between ‘over’ and ‘under’ in this group, cf. Brugmann, Grd. 2.2.912). Walde-P. 1.198. Boisacq 1009.
2. Lat. altus (> It., Sp. alto; Fr. haut with A- fr. Frank. hoh; Rum. tnalt fr. in alto), orig. pass. pple. of alere ‘nourish, rear’, but from earliest times used only as adj. in transferred sense ‘high’ (and ‘deep’). Ernout-M. 36. Walde-H. 1.32.
Lat. celsus, and more usually excelsus, pass. pple. of -cellere in antecellere ‘pro- ject, surpass’, excellere ‘surpass, excel’, etc. : Lat. collis ‘hill’, Lith. kelti ‘lift’, etc. Walde-P. 1.485. Ernout-M. 170f. Walde-H. 1.197.
3. Ir. ard, NIr. Grd: Lat. arduus ‘steep, elevated’, also (in part fr. parallel -dh- forms) Ay. aradwa- ‘lifted up, ele- vated’, ON ordugr ‘steep’, ChSI. rasii
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
‘grow’. Walde-P. 1.148 f. Ernout-M. 69f. Walde-H. 1.64. Pedersen 1.51.
Ir. uasal, W. uchel, etc., above, 1.
=== leaf ===
leaf 921
```


## [2026-09-06T02:22:49.935Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12555,12575p' incoming/ARY/ARY_pages.txt; echo \"=== pdf tag ===\"; python3 -c \"\nimport re\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\ntags=re.findall(r'\\[pdf page (\\d+)\\]','\\n'.join(t[:12563]))\nprint(tags[-1] if tags else None)\"",
 "description": "Read Aryanpur zereh entry"
}
```


### [2026-09-06T02:22:51.727Z] TOOL RESULT

```
0 (8ق۲۸) :0102/5 پرهان قاطع : ۱۷۶۳
بادداشت:
هیچکدام از پسگشت‌ها (مراجع) من به رابطه‌ی واژه‌های ایرانی و سانسکریت این فهرست با دیگر واژه‌های این
فهرست اشاره‌ای نمی‌کنند. بهمین دلیل در جلر واجریشه‌ی هند و اروپایی (شاید) آورده‌ام.
۱
ارستایی (4814): آلمانی (0870/424). دا ایکا
1 ج۸لام6 رفن02 انگلیسی کهن (87/0/57ظ 010):
پارسی پاستان (۷لفاق۳88 صا0): ۰ 021110 7 ماطفلانت :
پهلری (1تماتزمه): 22 انگلیسی (8۸/0/57): لد زره
کردی (01374/ن): 04 دانمارکی (0۸(/182): ناسا
افقانی (پشتو) (/4۳0۸27): 1 سوئدی (5(7801374): 0۸
تخاری ۸ (۸ (ل47تل707): ۱۹ نروژی (08۳50۵(۷/. ان انا
تخاری 8 (8 ۵(7ل37ل70) ق هلندی (007): 00
سانسکرپت (77ج82/50): لينواني ((۵لههنا 7 ): 77
8 الفاق۸- ,02۸ لنونی (لتی) (/7ل): تال2ج
ارمتی (/(فا8/): ۰ - ۱1 ایرلندی کهن (#لفل/ 2ز۵م: 0278۸31
بونانی (07885): 7 21585۸ آلبانی (9مامهتم: شا
تور لاتین (112ل): ۷۱۳ 1
گوتیکه ش یسنان با پبگشت‌ل ۸8۳8۴8۷۵۵۶
ایسلندی کهن (/۸01442ی5 صا0): 463464 میا
101۸ 2 (۱/8م۲) ی
=== pdf tag ===
422
```


## [2026-09-06T02:23:00.165Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/greet",
 "prompt": "Full etymology of 'greet' (to salute) — Old English gretan, Proto-Germanic *grotjan, and the sense 'to weep' variant."
}
```


## [2026-09-06T02:23:02.712Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0reh%E2%82%81d-",
 "prompt": "Does this reconstruction page exist for PIE *ǵʰreh₁d-? What is the meaning and which descendants are listed (Sanskrit hrādate, Avestan zrāδa-, Greek kakhlazō, Germanic *grētaną)?"
}
```


### [2026-09-06T02:23:06.441Z] TOOL RESULT

```
# Etymology of "Greet"

The word "greet" originates from Old English *gretan*, meaning "to come in contact with" in various senses including "attack, accost," "salute, welcome," and "touch, handle."

## Linguistic Origins

The term derives from West Germanic *grotjan*, which also appears in related forms across Germanic languages: Old Saxon *grotian*, Dutch *groeten*, and German *grüßen*.

## Semantic Evolution

While the primary modern sense in English, German, and Dutch is "to salute," the word historically carried much broader meaning. Scholars propose it may originally have meant "to resound," potentially stemming from Proto-Germanic *grætanan, the same root as Old English *grætan* meaning "weep, bewail."

## Related Words

The word connects to several English terms:
- **Greeting**: The noun form, first recorded as "greeting card" in 1876
- **Regret**: The second element shares etymological roots through the weeping sense
- **Greeter**: An agent noun appearing in late 14c. records

The word retains its archaic weeping sense in Scottish and northern English dialects, though this connection may stem from a different linguistic root.
```


### [2026-09-06T02:23:08.275Z] TOOL RESULT

```
# PIE *ǵʰreh₁d- Reconstruction

Yes, this reconstruction page exists on Wiktionary. The root means **"to sound."**

## Key Descendants Listed:

**Sanskrit:** ह्रादते (hrā́date) – "to sound, make noise"

**Avestan:** 𐬰𐬭𐬁𐬛𐬀 (zrāda) – "chainmail" (marked with uncertainty)

**Greek:** κέχλαδα (kékhlada) – "to sound, sing aloud"

**Germanic:** *grētaną – "to weep, cry"

## Notable Insight:

The page notes an alternative form *ǵʰleh₂d- appearing in the Old Irish, Sanskrit, and Greek cognates mentioned above, suggesting some variation in the reconstruction's vowel quality among descendant languages.
```


## [2026-09-06T02:23:15.838Z] TOOL CALL #59: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/آغل' --note 'page 193, root Gheugh, Persian آغل: Wiktionary gives both a Proto-Iranian *gauz- derivation (Sogdian āγōδ influence) and a Turkic alternative' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/زره' --note 'page 193, root Ghlad, Persian زره < MP zrēh < PIE *ǵʰreh₁d-; Arabic زرد a borrowing' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/زرد' --note 'page 193, Arabic زرد zarad from an early West Iranian source via Aramaic zardā; زرّاد derived' 2>&1 | tail -3",
 "description": "Archive Wiktionary sources"
}
```


### [2026-09-06T02:23:18.915Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6b658b80d03eee7d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/de9f31c680355818.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5ab80b54d3901e71.txt
```


## [2026-09-06T02:23:24.128Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ǵʰreh₁d-' --note 'page 193, root Ghlad: PIE *ǵʰreh₁d- \"to sound\", descendants Skt hrādate, Av zrāda, Gk kekhlada, Gmc *grētaną' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://www.etymonline.com/word/regret' --note 'page 193, node English regret < OFr regreter, Germanic *grētaną' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://www.etymonline.com/word/greet' --note 'page 193, node English greet < OE gretan < WGmc *grotjan' 2>&1 | tail -2",
 "description": "Archive remaining sources"
}
```


### [2026-09-06T02:23:26.929Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fae925eafdfd7d13.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/31f9589780d4f312.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/42fe1742f3a7edf4.txt
```


## [2026-09-06T02:23:33.609Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"GAUZ\\|gauz\\b\\|\\*gauz\" CHEUNG.txt | head -20",
 "description": "Grep Cheung for gauz"
}
```


### [2026-09-06T02:23:33.664Z] TOOL RESULT

```
8435:*gauz ‘to hide, conceal’ 
8479:forms also contain the root *gauz. On the other hand, the different formations 
17937:conceal’ (> Skt. goh, Ir. *gauz), cf. EWAia: Le 
31243:Gharib 1975: Badr ol-Zaman Gharib, Old Iranian roots gauz- and gaud- in Iranian, 
55517:*gar* (s.v.), *gauz (s.v.), 
56136:*gauz, *maus(H), *sar! 
56331:(s.v), *gauz (s.v.), *HuaH? 
56893:*gauz, *sar! 
58362:*gauz (s.v.)
```


## [2026-09-06T02:23:36.298Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8430,8495p' CHEUNG.txt; echo \"=== gharib1975 ref ===\"; sed -n '31240,31248p' CHEUNG.txt",
 "description": "Read Cheung *gauz entry"
}
```


### [2026-09-06T02:23:36.380Z] TOOL RESULT

```
*gaz ? 117 


*gauz ‘to hide, conceal’ 


*AVESTAN: Y Av. guz- ‘to hide, conceal’ = Liste: 20 

MED.; Pres. them.: IND. impf. 1sg. YAv. aguze (Yt 17.55 Ё), OPT. 35р. YAv. guzaéta (Yt 4.4), ? 3pl. 
Y Av. fraguzaiianta (Yt 17.55 f.). % Hoffmann — Forssman 1996: 186f. analyse YAv. fraguzaiianta 
differently: pres. aja- (with the zero grade root). 


*OLD PERSIAN: (+ *apa-) apagaud- ‘to conceal, hide away’ = Kent: 182b 

Caus.: INJ. 2sg. apagaudaya < a-p-g-u-d-y-> (DB 4.54), SUBJ. 2sg. apagaudayahy < a-p-g-[u]-d-[y]- 
[a]-h-y> (DB 4.55), < a-p-g-u-d-y-a-h-y> (4.57) 

*MIDDLE PERSIAN: BMP gwe /göz/ ‘walnut’ 

*PARTHIAN: (+ *ni-) ngwz- ‘to hide, disappear’ = Ghilain: 64 | DMMPP: 241b 

Pres.: IND. 3sg. ngwzyd, 3pl. ngwzynd, IMPV. 2sg. ngwz; Inf.: ngwz’dn 

*SOGDIAN: (+ *apa-) BSogd. ’pyw’yz, CSogd. pyws- (pret. stem) ‘to conceal 

Pres.: IND. 35р. BSogd. ‘pyw’yzt; Pret.: tr. 35р. f. CSogd. pywst’; Partic.: perf. pass. CSogd. pywsty (m.) 
‘concealed’ 

*NWIR: NP göz ‘(wal)nut; fart, Kurd. (Kurm.) goz, guz (Ё), (Sor.) gwéz ‘walnut’ 
(also aquza, anquza). 9 In modern Persian parlance, the "arabicized" form joz for 
‘(wal)nut’ has replaced gōz, which now exclusively means ‘fart’, but note Sh. jay ‘a 
dumb fart’ (EVS: 39a). 

*NEIR: Oss. I. qoyzyn/qoyzt (qoyzyd), D. guzun/guzt ‘to crouch’, Pash. пух (m.), Sh. 
yüz, (Baj.), Bart., Rosh. yuz (f.), Sariq. yewz, Yzgh. yaz ‘walnut’ || (+ *apa-) Yghn. 
büyünc-, büyünj-/büyüsta ‘to steal’ || (+ *à-) Yi. oyúzo ‘walnut’ || (+ *pari-) ? Wa. 
poergas-/pargast ‘fall (into a trap), be stuck (into), entangled; to attain’ || (+ *ham-) 
Oss. I. ænguz, D. engoz& ‘walnut’ 

*MISC: (+ *ni- ?) Georg. nigoz- ‘walnut’ (< Ir.) 

*SANSKRIT: goh ‘to hide’ (RV+) = EWAia I: 502 

The root appears to be of IIr. origin: IE connections are uncertain. The following 
forms are mentioned as possible cognates: Lith. güZti ‘to shelter, cover’, ON gygr 
(f.) ‘female monster, giant’. According to Gippert 1993: 155 ff., the Ir. "walnut 
forms also contain the root *gauz. On the other hand, the different formations 
attested for ‘walnut’ perhaps indicate the adoption of a non-native word. 


«PIE? > LIV: 199 | Pok.: 450 

*REFERENCES: EVP: 10; IFL П: 534b, 189b; Andreev — PeSéereva: 234a; Abaev, Slovar’ I: 160 Ё; EVS: 
38a; Abaev, Slovar’ II: 336 f.; Werba 1997: 178; Steblin-Kamenskij 1999: 276; Cabolov 2001: 409 f.; 
NEVP: 8 


*gaz ? ‘to bite, sting’ 

*MIDDLE PERSIAN: BMP gc- /gaz-/ ‘to sting’ (LW) 

Pres.: IND. 3sg. BMP асу! /gazéd/, SUBJ. 3sg. BMP gc't/gazad/; Partic.: perf. pass. BMP gcyt /gazid/ 
*PARTHIAN: “gst (pret. stem) ‘to bite” = Ghilain: 96 | DMMPP: 170b 
=== gharib1975 ref ===
Farhang-i Sugdi, Sugdi-Farsi-Anglisi. Tehran: Farhangan Publications / Inti- 
Sarat-i Farhangan 1995/1374. 

Gharib 1975: Badr ol-Zaman Gharib, Old Iranian roots gauz- and gaud- in Iranian, 
Gs Nyberg I: 247-256. 

Ghilain: Antoine Ghilain, Essai sur la langue parthe, son systéme verbal d’apres les 
textes manichéens du Turkestan oriental (Bibliotheque du Muséon, Volume 9). 
Louvain, 1939.
```


## [2026-09-06T02:24:00.084Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"gheugh[^ ]*\\|ghugh[^ ]*\" AHD_watkins1985.txt | head; echo \"--none above means silent--\"; grep -c \"ghlad\" AHD_watkins1985.txt; echo \"=== NYB ===\"; grep -n \"zrēh\\|zrh\\|zrah\" NYB_vol2_glossary.txt | head -5",
 "description": "Check AHD for gheugh/ghlad and Nyberg for zrēh"
}
```


### [2026-09-06T02:24:00.170Z] TOOL RESULT

```
--none above means silent--
0
=== NYB ===
1341:drayäp [dly’p'] the sea 621. 211, 1131, — SW form of Av. (1701 sq.) zrayah (v. zrah, zrài): OP drayah- -+ dp; the com- pound was guite clear to those who created the Aram. expression used later as ideogr. (FrP 3): YMYMY^, i. e. yammé mayyä ‘seas of water’, a purely mechan- ical transposition of dray(ah)-āp ‘sea- waters’. MPrs dry’b (A-H I); Paz. daryäv; Ps. has the bizarre spelling dlyw*w (cf s. v. niyandar); NP daryä.
4511:Zartuxšt[zltwhšt'], Zartušt [zltwšt'] the Prophet 312-47 and passim (-ušt 11319 and v. next w.). — Av. (1670 sgg.) Zara- 0uštra-; MPrth zrhwšt; MPrs zrdrwšt (A— H II), adj. zrdrwstg’n (S). As to -xšt, v. Benveniste, BSL 29, 1929, 107. Cf the discussion of the name by Bailey, TPhS 1958, 40-41.
4564:zrāh [zh], zrai [zl?y, zPd] sea 622. 3212-19, 4617, 869-10, 8919, 9316.21.27, _ Av. (1701 sq.) zrayah-; MPrth zryh, zryy, adj. zrhyg; MPrs zryh (S) borrowed from NW, the
4570:zréh [zlyh], zré [zlyd] armour, harness 69, 2013-14, 8515, 12027, — Arm. lw. zrah-k‘; Syr. lw. zardä ‘coat of mail’, Talm zrd’, Telegdi 243, Arab. lw. zarad-; Paz. z(a)reh ; NP zirih, zarah: all these forms presup- pose *zrdda- and do not tally with Av. (1703) zrača- (Vd. 14? without variant; Phl. Vd. has zrāt evidently through the influence of the Av. form). Some im- portance should perhaps be attached to the curious gen. zaradvehe (1703) quoted from a fragment preserved in the Phl Vd. — NP zirih, Paz. zreh perhaps < cas. obl. *zrdóe.
5493:zrayah-: drayàp, zrah zyā-: zin-
```


## [2026-09-06T02:24:08.535Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in (4570,4564):\n    print(ln, 'leaf', '\\n'.join(t[:ln]).count('\\f'))\"",
 "description": "Nyberg leaf"
}
```


### [2026-09-06T02:24:10.282Z] TOOL RESULT

```
4570 leaf 255
4564 leaf 255
```


## [2026-09-06T02:24:18.228Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9865,9880p' BRT.txt; python3 -c \"\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nprint('leaf', '\\n'.join(t[:9875]).count('\\f'))\"",
 "description": "Bartholomae guz- context"
}
```


### [2026-09-06T02:24:19.888Z] TOOL RESULT

```
•  j.  gao-s&ra-  Adj.  'über  Rinder  gebietend, reich  an  Rindern':  nmän»n  bir^züstütum 'sütvm  Vyt.  p;  —  ailam  nmänä  ki'taätä ^'surar?kö^^  histtnte  Ytiy.S.
VgL  gaosutä:  —  Vgl,  DsT.  ZA.  2. 572.  Ohne Wert  Gdn.  3  Yt  79.  —  ■)  Die  mask.  statt der  neutr.  Form.  Im  Ausgang-^  und  -a  fielen die  Nom.  Flur,  beider  Geschlechter  zusammen. NA.  'sür',  s.  aber  die  Hds.
•  j.  gao-8urä-  f.  'Reichtum  an  Rindern' (?) : TtrthrtrjnS  avi  imal  nmänpm  •räbyBijiV. als  IP.)  :^ar»nö  pairi.vsnnavaiti  (sd.)  Yt.
Seht  unsicher  i  vgl.  ^aataf  n-.  —  Npü. :  un- deutlich.
•  j-^gac'^-Stäna-m.,  -stanay-  m.,  'Rin- derstall': yaua  ai^a  galwa  -naisva /ra- jasiit  V.  ;5.  29; — yö  altim  -tarn  uzdasta yerihh  v3  alsS  °nis  anhai  V.  /j.  30  ".
BJ.  goflhana-  Adj.,  gasthäna-  n.;  mp.  (Pü.j ^slän.  —  I)  So  Jpi,  Mfa;  NA.  hat  ^avö.ü'. —  ä)  zSt.  s.  HHr5.slSna.  No.   l.
•  j.  gaoz-,    p.  gaud-    V.     'verberget Praes.  4   gusa-,    24   gutaya-,    30  (Iter.) gauiiayot,
'verbergen,  verstecken':  haom  tanSm guzaita  Yt  4~  4.
D  mit  apa  'verbergen,  verheimlichen' yadiy  imäm  htfdugam  afiagaudayäAy  Bh. i^iiiio; — avakyarädiy  mä  apagaudaya'' (aS.)  Bh.^io.
mit  a  'ins  Versteck  bringen':  yat  .  . äal  azftn  tanSm  aguse  atairi ..  "..dabe- gab  ich  mich  ins  Versteck  unter  .."   Yt.
mit^a  'aus  dem  Versteck  hervorholen': äai  mam  fraguzayanta  . .  "da  holten  mich aus  dem  Versteck  . ."  Yt. /".  55.
ai.  guhaH  'er  verbirgt'.    —    Npil.  (lu  Yt.  4);
dar  miyStt  guiäilan  (wegen  des  Anklaugs !).
•  j.  gao-zasta-  Adj.  'Milch  in  der  Hand habend,  mit  M.  in  der  Hand':  yasß  %wä .  .  fräyazSite  .  .  'td  Y.  62.  i ;  V.J.  1.
PQ.  (in  Y.)i  göit  dasl,  (lu  V.):  yäml^)  dast, mit  der  Bemerkung:  lui  ke  elön  gäuiet  fatkSß fTir-ofl;   s.  daiu  DST.  ZA.  2.  33.
•  j-,  g.  gaoS-  V.  'hören'.  Praes.  i  gus-, 3  gäid-,  30  (Kaus.)  güsaya-,  —  PPfP. 'guäa-.
leaf 292
```


## [2026-09-06T02:24:37.439Z] TOOL CALL #66: Bash

```json
{
 "command": "sed -n '1,200p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T02:24:37.487Z] TOOL RESULT

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


## [2026-09-06T02:31:22.862Z] TOOL CALL #67: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk193.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_AGOL = \"https://en.wiktionary.org/wiki/%D8%A2%D8%BA%D9%84\"\nW_ZEREH = \"https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D9%87\"\nW_ZARAD = \"https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D8%AF\"\nW_GHRED = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0reh%E2%82%81d-\"\nE_REGRET = \"https://www.etymonline.com/word/regret\"\nE_GREET = \"https://www.etymonline.com/word/greet\"\n\ndoc = {\n \"pdf_page\": 193,\n \"book_page\": 163,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Gheugh, Ghŭgh\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *gʰeugʰ- / *gʰugʰ- 'to conceal' (Pokorny 450; LIV 199) → Proto-Iranian *gauz- / *gaud- 'to hide, conceal'\",\n   \"note\": \"Pokorny IEW p.450 carries the lemma verbatim as 'gheugh-, ghugh-' with the meaning 'to conceal', and its material is exactly Nourai's: OInd. gūhati 'hidden', guhā 'hideout'; Av. guz- (guzaēta, fra-guzayanta); OPers. yadiy apa-gaudayāhy 'if you hide'; ON gýgr, Lith. gūžti. Language label ('Indo-European') and gloss are therefore right, and Nourai's two ablaut grades reproduce Pokorny's lemma exactly. One caveat that Nourai does not signal: Cheung (Etym. Dict. of the Iranian Verb, 2007, p.117 s.v. *gauz) writes 'The root appears to be of IIr. origin: IE connections are uncertain' — outside Indo-Iranian only Lith. gūžti 'to shelter, cover' and ON gýgr are offered, so the reconstruction is secure for Indo-Iranian but thin for PIE. Note also that Iranian shows two root-final variants, *gauz- (Avestan) and *gaud- (Old Persian, Sogdian); Gharib devoted a whole article to the pair ('Old Iranian roots gauz- and gaud- in Iranian', Gedenkschrift Nyberg I, 247-256), and Nourai's chart silently merges them.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *gʰeugʰ- / *gʰugʰ- «پنهان کردن، نهفتن» دقیقاً همان مدخلی است که پوکورنی در صفحهٔ ۴۵۰ فرهنگ خود آورده و شواهدش نیز همان است که نورایی می‌آورد: سنسکریت gūhati، اوستایی guz-، پارسی باستان apa-gaudaya-. پس برچسب زبانی و معنای ریشه در نمودار درست است. با این همه چونگ (۲۰۰۷، ص ۱۱۷) یادآور می‌شود که پیوند این ریشه با بیرون از هندوایرانی قطعی نیست و تنها لیتوانیایی gūžti و نورس باستان gýgr را می‌توان هم‌ریشه شمرد؛ افزون بر این در ایرانی دو گونهٔ *gauz- (اوستایی) و *gaud- (پارسی باستان و سغدی) در کنار هم‌اند که نورایی آن‌ها را یکی گرفته است. حکم: ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n   \"sources\": [],\n   \"ref_check\": [\n    {\"ref\": \"POK:450\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt (line ~33234): 'Root / lemma: gheugh-, ghugh- | Meaning: to conceal | Material: Old Indic guhati … Avestan guz- (guzaeta, fra-guzayanta) \\\"conceal, hide\\\", Old pers. yadiy apa-gaudayahy \\\"if you hide\\\" … References: WP. I 566 f. Page(s): 450'. Nourai's root box reproduces this entry, headword, gloss and page all correct.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 566 (incoming/WLD/WLD_Bd1_pages.txt line ~53825)\", \"stance\": \"supports\",\n     \"note\": \"Running head '566  gheugh- — gheugh-, ghugh-'; the entry has '(guzaeta, fra-guzayanta) „verbergen, verstecken\\\", apers. yadiy [apagaudayahy]'. This is Pokorny's own source (POK cites 'WP. I 566 f.').\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, gh- section\", \"stance\": \"silent\",\n     \"note\": \"grep for 'gheugh'/'ghugh' in AHD_watkins1985.txt returns nothing — Watkins omits the root (no English reflex), so the AHD appendix neither supports nor contradicts.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. gheughilos/gheughos\", \"stance\": \"silent\",\n     \"note\": \"IEC.txt has only 'gheughilos, gheughos \\\"fool\\\"' (Ir. guag 'folly'), a different root; Mann has no 'conceal' lemma of this shape.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"p.117 s.v. *gauz 'to hide, conceal'\", \"stance\": \"partial\",\n     \"note\": \"'The root appears to be of IIr. origin: IE connections are uncertain. The following forms are mentioned as possible cognates: Lith. gūžti \\\"to shelter, cover\\\", ON gygr … «PIE? > LIV: 199 | Pok.: 450'. Confirms the Indo-Iranian root and Pokorny's page, but downgrades its PIE status.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Old Persian\", \"words\": \"gaud; â-gaud; apa-gaudaya\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Old Persian gaud- 'to conceal' is genuine and is the regular Old Iranian *gaud- variant of the root; it is attested only in the compound apa-gaud-, in Darius' Bisotun inscription DB 4.54 'avahyarādiy mā apagaudaya' and DB 4.55, 57 'yadiy imām hadugām naiy apagaudayāhy'. The causative stem *gauda-ya- (Skt. gūhayati) gives OP apa-gaudaya-. THE GLOSS IS WRONG: apa-gaudaya- means 'conceal, hide away', not 'to uncover' — apa- here is the perfective/intensive 'away' of Nourai's own root Apo, so the phrase mā apagaudaya is 'do not conceal (it)'. Kent (whom Nourai cites) p.182b: 'gaud- vb. \\\"conceal\\\" … apa- + gaud- \\\"conceal, hide away\\\"'; Buck p.852 §12.27 renders mā apagaudaya as 'do not hide'; Bartholomae col. ~526 'mit apa \\\"verbergen, verheimlichen\\\"'. Cheung 2007:117 likewise lists OP apagaud- 'to conceal, hide away'. Second problem: 'â-gaud : cover' is not an attested Old Persian form. Bartholomae's ā-compound is Avestan (aguze, Yt 17.55, 'mit ā \\\"ins Versteck bringen\\\"'), and the *ā-gaud- that gives Sogdian ʾγwd is a Sogdian/Eastern Iranian formation, not Old Persian; Nourai has copied the Sogdian etymon back into the Old Persian box so that the arrow to Sogdian looks direct. The root form gaud- and the arrow from the root are correct; the two glosses/forms are not.\",\n     \"derivation_fa\": \"ستاک پارسی باستان gaud- «پنهان کردن» راست است و تنها در ترکیب apa-gaud- در سنگ‌نبشتهٔ بیستون (بند ۴٫۵۴: mā apagaudaya و ۴٫۵۵: naiy apagaudayāhy) به‌کار رفته است؛ ستاک سببی *gauda-ya- (قس. سنسکریت gūhayati) به apa-gaudaya- می‌انجامد. اما معنایی که نورایی داده نادرست است: apa-gaudaya- یعنی «پنهان کردن، نهان داشتن»، نه «آشکار کردن»؛ پیشوند apa- در اینجا معنای سلبی ندارد. کنت (ص ۱۸۲ب)، باک (ص ۸۵۲) و بارتولومه (ستون ۵۲۶) هر سه همین معنا را می‌دهند و هر سه از مراجع خودِ نورایی‌اند. نکتهٔ دوم آنکه صورت â-gaud در پارسی باستان گواهی نشده است؛ ā-guz- اوستایی است (aguze در یشت ۱۷٫۵۵) و *ā-gaud- ساختی سغدی/ایرانی شرقی است. حکم: پیوند ریشه‌شناختی درست، ولی خطای معنایی و صورتی در کتاب.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"POK:450\", \"status\": \"supports\", \"note\": \"POK_full.txt p.450: 'Old pers. yadiy apa-gaudayahy \\\"If you hide\\\"' — the OP form is Pokorny's, and Pokorny glosses it 'hide', not 'uncover'.\"},\n      {\"ref\": \"KNT:182\", \"status\": \"contradicts\", \"note\": \"KNT.txt leaf 205/206 (Lexicon, printed p.182b — the page Cheung 2007:117 also cites as 'Kent: 182b'): 'gaud- vb. \\\"conceal\\\": Av. gaoz-, Skt. gūhati (§88). apa- + gaud- \\\"conceal, hide away\\\": apagaudayahy 2d sg. subj. DB 4.55, 57. apagaudaya 2d sg. inj. DB 4.54.' Kent has no ā-gaud- and glosses apa-gaud- 'conceal', the opposite of Nourai's 'to uncover'.\"},\n      {\"ref\": \"SOD:50\", \"status\": \"not_found\", \"note\": \"SOD.txt has no numbered entry or page around 50 bearing on Old Persian; Gharib's dictionary is Sogdian-only. The relevant Gharib material is at entries 78 and 107 (≈ printed pp. 3 and 5), i.e. Nourai's other citation SOD:3,5; SOD:50 looks like a stray.\"},\n      {\"ref\": \"SYN:852\", \"status\": \"contradicts\", \"note\": \"SYN.txt leaf 921 = printed p.852, §12.27 HIDE, CONCEAL, sub-§8: 'Skt. guh- (3sg. pres. gūhati), Av. guz-, OPers. gud- (in mā apagaudaya \\\"do not hide\\\") perh. : Lith. gūžti \\\"cover something warm\\\". Walde-P. 1.566 f.' Buck's translation 'do not hide' contradicts Nourai's gloss 'to uncover'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"col. ~526 (local scan leaf 292) s.v. gaoz-, p. gaud-\", \"stance\": \"contradicts\",\n       \"note\": \"'j., g. gaoz-, p. gaud- V. \\\"verbergen\\\". Praes. gusa-, guzaya-, gauzayat … mit apa \\\"verbergen, verheimlichen\\\": yadiy imām hadugām apagaudayāhy Bh.; avahyarādiy mā apagaudaya Bh. 4.54; mit ā \\\"ins Versteck bringen\\\": āat azәm tanūm aguze … Yt.' Bartholomae explicitly assigns the ā-compound to Avestan, and glosses apa-gaud- 'conceal'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p.117 s.v. *gauz\", \"stance\": \"partial\",\n       \"note\": \"'*OLD PERSIAN: (+ *apa-) apagaud- \\\"to conceal, hide away\\\" = Kent: 182b. Caus.: INJ. 2sg. apagaudaya (DB 4.54), SUBJ. 2sg. apagaudayahy (DB 4.55), (4.57)'. Cheung lists only the apa- compound for OP and glosses it 'conceal'.\"},\n      {\"src\": \"KNT\", \"where\": \"p.182b (Lexicon)\", \"stance\": \"partial\",\n       \"note\": \"See ref_check; Kent has gaud- but not ā-gaud-, and his gloss is 'conceal'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Sogdian\", \"words\": \"â-gaud, `g`wd; `g`wnd\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Gharib, Sogdian Dictionary, entry 78: 'ʾγwd (B) — aγoδ ©<*ā-gaud- ⇒ ʾγwnd- : cover, covering (VJ 961; BSTBL; Gharib, AI 4.249)', and entry 107: 'ʾγwnd- (M) — aγund ©<*ā-gunt; √gaud- ⇒ ʾγwnt-, ʾγwst-: (to) cover, (to) dress (GMS 601, 807)'. The forms are therefore real Sogdian and Gharib herself derives them from Old Iranian *ā-gaud-: prefix *ā- 'on, over' + the -d- variant of the root, with a nasal-infix present *ā-gu-n-d- (ʾγwnd-/ʾγwnt-) beside the athematic ʾγwd, past stem ʾγwst- < *ā-gusta-. In the Manichaean and Buddhist Sogdian orthography ʾ- writes the prosthetic/initial ā-, and -γ- is the voiced spirant from Iranian *g. Nourai's transliteration ('`g`wd', '`g`wnd') is the standard Sogdian consonant skeleton with ʿ for aleph. One gloss overshoots: Gharib gives only 'cover, covering' — 'barn, shelter' is not in her entry (she has a separate word ʾγwyr 'stable', entry 113); the 'barn' sense is Nourai's bridge to āγol, and Wiktionary's 'cover, shelter, barn' for Sogdian āγōδ likewise looks derived from this same chain.\",\n     \"derivation_fa\": \"غریب در «فرهنگ سغدی» مدخل ۷۸ می‌آورد: «ʾγwd (بودایی) aγoδ ← *ā-gaud- : پوشش، پوشاندن» و مدخل ۱۰۷: «ʾγwnd- (مانوی) aγund ← *ā-gunt؛ ریشهٔ gaud- : پوشاندن، پوشانیدن». پس هر دو صورت سغدی راست‌اند و خودِ غریب آن‌ها را از ایرانی باستان *ā-gaud- (پیشوند ā- + گونهٔ دال‌دار ریشه) می‌گیرد؛ ʾγwnd- ستاک حال با میانوند خیشومی (*ā-gu-n-d-) و ʾγwst- ستاک گذشته از *ā-gusta- است. تنها نکته آنکه غریب فقط معنای «پوشش» را می‌دهد و «آغل، سرپناه» افزودهٔ نورایی است. حکم: ادعای نورایی دربارهٔ خودِ صورت‌های سغدی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"SOD:3\", \"status\": \"supports\", \"note\": \"SOD.txt entry 78 (≈ printed p.3): '78 ʾγwd  B | aγoδ ©<*ā-gaud- ⇒ʾγwnd- | cover, covering | VJ 961; BSTBL; Gharib. AI 4.249'. Exactly the form, the etymon and the 'cover' gloss Nourai draws; 'barn, shelter' is not in Gharib.\"},\n      {\"ref\": \"SOD:5\", \"status\": \"supports\", \"note\": \"SOD.txt entry 107 (≈ printed p.5): '107 ʾγwnd-  M | aγund ©<*ā-gunt; √gaud- ©impf. mʾγwnd ⇒ʾγwnt-, ʾγwst-, ʾγwš | (to)cover, (to)dress | GMS 601, 807; Gharib. AI 4.249'. Confirms the second Sogdian word and its derivation from √gaud-.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SOD\", \"where\": \"entries 78, 107, 108, 110, 112 (pp. 3-5)\", \"stance\": \"supports\",\n       \"note\": \"The whole ʾγwd / ʾγwnd- / ʾγwnt- / ʾγwst- / ʾγwstyh family is present with 'cover' senses; Gharib's own article 'Old Iranian roots gauz- and gaud- in Iranian' (Gs Nyberg I 247-256) is the study behind these etymologies.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p.117 s.v. *gauz, *SOGDIAN section\", \"stance\": \"partial\",\n       \"note\": \"Cheung lists for Sogdian only '(+ *apa-) BSogd. ʾpγwʾyz, CSogd. pyws- \\\"to conceal\\\"' under *gauz — i.e. he files the z-variant; the d-variant ʾγwd/ʾγwnd- belongs to Gharib's parallel root *gaud-, which Cheung does not treat separately. No contradiction, a different scope.\"},\n      {\"src\": \"BRT\", \"where\": \"col. ~526 s.v. gaoz-, 'mit ā \\\"ins Versteck bringen\\\"'\", \"stance\": \"supports\",\n       \"note\": \"Bartholomae attests the ā- preverb with this root in Avestan (aguze Yt 17.55), which is the Old Iranian pattern the Sogdian ʾγwd continues.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"âğol «آغل»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"NP آغل āγol (also آغیل āγil, آغال āγāl) 'sheepfold, cattle byre'. Nourai's route is: Sogdian ʾγwd/ʾγwnd- 'cover, shelter' → Persian āγol 'barn'. This is one of the two etymologies current in the literature. Wiktionary (s.v. آغل) gives it as the primary one — 'Ultimately a derivative of Proto-Iranian *gauz- (\\\"to hide, conceal\\\") … Possibly influenced by Northeastern Iranian, compare Sogdian āγōδ \\\"cover, shelter, barn\\\"' — but immediately offers the rival: 'Alternatively, borrowed from a Turkic source: cognate with Ottoman Turkish آغل', i.e. Turkish ağıl, Old Turkic aɣɨl 'sheepfold', a well-attested Turkic word with its own Turkic family. Two things weigh against a straight Sogdian loan: (a) the -l of āγol/āγil is unexplained from Sogdian ʾγwd (d-stem) — Turkic ağıl supplies it directly; (b) the word is not attested in Middle Persian and appears in New Persian in the period of heavy Turkic lexical influx. Mo'in's Farhang (the reference Nourai cites) prints the entry with the variants آغال and آغیل and a definition ('جای گوسفندان و گاوان و دیگر چارپایان … در کوه یا در کنده‌ای در زیر زمین') but no origin tag at all, so it does not in fact support the Sogdian arrow. Verdict: an accepted-by-some derivation, with a serious Turkic competitor that Nourai does not mention.\",\n     \"derivation_fa\": \"«آغل» (نیز آغیل و آغال) «جای نگاهداری گوسفند و گاو». نورایی آن را از سغدی ʾγwd «پوشش، سرپناه» می‌گیرد. ویکی‌واژه همین را نخست می‌آورد («در نهایت برگرفته از ایرانی آغازین *gauz- «پنهان کردن»، شاید به تأثیر ایرانی شمال‌شرقی، قس سغدی āγōδ») ولی بی‌درنگ گزینهٔ دوم را نیز یاد می‌کند: وام‌گیری از ترکی، هم‌ریشه با ترکی عثمانی آغل و ترکی باستان aɣɨl «آغل». دو نکته به سود گزینهٔ ترکی است: نخست آنکه لامِ پایانی آغل/آغیل از ʾγwd سغدی توضیح‌پذیر نیست ولی در ağıl ترکی خود‌به‌خود هست؛ دوم آنکه این واژه در فارسی میانه گواهی نشده و در دورهٔ نفوذ گستردهٔ واژگان ترکی در فارسی نو پدیدار می‌شود. افزون بر این، معین ــ که خودِ نورایی به او ارجاع می‌دهد ــ در ذیل «آغل» هیچ نشانِ ریشه‌شناختی نمی‌آورد. حکم: با احتیاط پذیرفتنی است؛ نورایی گزینهٔ ترکی را نادیده گرفته است.\",\n     \"sources\": [W_AGOL],\n     \"ref_check\": [\n      {\"ref\": \"MON:68\", \"status\": \"partial\", \"note\": \"MON_part1.txt line ~3704: 'آغل: [= آغال ‹ آغیل] (ا.) جای گوسفندان و گاوان و دیگر چارپایان به شب در خانه یا در کوه یا در کنده‌ای در زیر زمین.' Mo'in gives the headword and exactly the two variants Nourai prints as script_extra (آغیل، آغال), but carries NO origin tag (no [سغ.], no [تر.]) — so the page documents the word, not the Sogdian derivation.\"},\n      {\"ref\": \"SOD:3\", \"status\": \"partial\", \"note\": \"Gharib entry 78 ʾγwd 'cover, covering' is real (see node 2), but Gharib says nothing about New Persian آغل; the Sogdian→Persian step is Nourai's own inference.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"s.v. آغل (MON_part1.txt line 3704) and آغول (line 3746: 'آغول: [= آغل] (ا.) آغل، زاغه')\", \"stance\": \"silent\",\n       \"note\": \"Mo'in records آغل/آغول/آغال/آغیل without any etymological bracket, unlike his usual [په.] / [تر.] tags.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, grep 'آغل'\", \"stance\": \"silent\",\n       \"note\": \"Aryanpur's Indo-European roots dictionary has no entry for آغل — no Indo-European pedigree claimed there.\"},\n      {\"src\": \"TTS\", \"where\": \"Vámbéry, incoming/TTS/TTS_pages.txt, grep 'agil/agyl'\", \"stance\": \"silent\",\n       \"note\": \"only a stray 'agil s.' in an index line; Vámbéry's OCR does not yield a usable ağıl entry, so the Turkic side had to be taken from Wiktionary's Ottoman/Old Turkic material.\"},\n      {\"src\": \"HRN\", \"where\": \"grep 'agol/aghol' in HRN.txt\", \"stance\": \"silent\",\n       \"note\": \"Horn's Grundriss has no entry for آغل — it is not in his New Persian Iranian-inherited stock, which is itself an argument for the loanword view.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Avestan\", \"words\": \"guz, gaoz; fra-gauzayanta\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Avestan gaoz- / guz- 'to conceal, hide' is Bartholomae's headword (AiW col. ~526): 'j., g. gaoz-, p. gaud- V. \\\"verbergen\\\"', present stems guza-, guzaya-, gauzaya-. The full-grade gaoz- is the citation form, guz- the zero grade regular before the thematic vowel (PIE *gʰeugʰ- > Ir. *gauz- with the Iranian palatal *ǰʰ > z development of the second *gʰ, cf. Skt. gūhati with h). fra-gauzayanta (correctly fraguzaiianta, Yt 17.55 f., of Aši rescuing the persecuted) is the causative/iterative with preverb fra- 'forth', which Bartholomae glosses 'aus dem Versteck hervorholen' ('to fetch out of hiding') — so its meaning in context is nearly the opposite of Nourai's 'to conceal'; Hoffmann–Forssman 1996:186f. (per Cheung 2007:117) even analyse it as a zero-grade aya-present rather than a causative. The forms and the descent from the root are right; only the gloss of the fra- compound is loose.\",\n     \"derivation_fa\": \"اوستایی gaoz-/guz- «پنهان کردن» سرواژهٔ بارتولومه است (ستون ۵۲۶: «gaoz- اوستایی، gaud- پارسی باستان، فعل: verbergen») با ستاک‌های حال guza-، guzaya- و gauzaya-. صورت پایهٔ gaoz- درجهٔ کامل و guz- درجهٔ صفر ریشه است؛ *gʰ دوم هندواروپایی در ایرانی به z بدل شده (قس سنسکریت gūhati با h). ترکیب fra-gauzayanta (درست‌تر: fraguzaiianta، یشت ۱۷٫۵۵) را بارتولومه «از نهانگاه بیرون آوردن» معنا می‌کند، یعنی درست وارونهٔ معنایی که نورایی داده است. حکم: صورت‌ها و تبار ریشه درست است، تنها معنای ترکیب fra- سست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"POK:450\", \"status\": \"supports\", \"note\": \"POK_full.txt p.450: 'Avestan guz- (guzaeta, fra-guzayanta) \\\"conceal, hide\\\"' — both Avestan words of the node, in Pokorny's own spelling (which is where Nourai's 'fra-gauzayanta' comes from).\"},\n      {\"ref\": \"KNT:182\", \"status\": \"supports\", \"note\": \"KNT.txt p.182b s.v. gaud-: 'Av. gaoz-, Skt. gūhati' — Kent gives exactly the Avestan citation form gaoz- alongside the OP verb.\"},\n      {\"ref\": \"SYN:852\", \"status\": \"supports\", \"note\": \"SYN.txt p.852 §12.27.8: 'Skt. guh- (3sg. pres. gūhati), Av. guz-, OPers. gud- …' — Buck's list has the Avestan zero-grade guz-.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"col. ~526 (leaf 292) s.v. gaoz-\", \"stance\": \"supports\",\n       \"note\": \"'gaoz-, p. gaud- V. \\\"verbergen\\\". Praes. 4 guza-, 24 guzaya-, 30 (Iter.) gauzayat … \\\"verbergen, verstecken\\\": haom tanūm guzaita Yt 4.4 … mit fra \\\"aus dem Versteck hervorholen\\\": āat mam fraguzayanta … Yt 17.55. ai. gūhati \\\"er verbirgt\\\".'\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p.117 s.v. *gauz\", \"stance\": \"supports\",\n       \"note\": \"'*AVESTAN: Y Av. guz- \\\"to hide, conceal\\\" = Liste: 20. MED.; Pres. them.: IND. impf. 1sg. YAv. aguze (Yt 17.55), OPT. 3sg. YAv. guzaēta (Yt 4.4), ? 3pl. YAv. fraguzaiianta (Yt 17.55 f.)'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I p.566\", \"stance\": \"supports\",\n       \"note\": \"'(guzaeta, fra-guzayanta) „verbergen, verstecken\\\"' under gheugh-, ghugh-.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Sanskrit\", \"words\": \"gŭhati\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Sanskrit गूहति gūhati 'he hides, conceals' (RV onwards; root guh-, aorist aghukṣat, nouns guhā 'hiding place, cave', gūḍha- 'hidden'). It is the Indic member of the same root: PIE *gʰeugʰ- gives Indo-Iranian *gʰaugʰ-/*gʰugʰ-, and in Indic the second aspirate surfaces as h (the regular Sanskrit outcome of *gʰ before a following consonant/in this position, whence guh- beside Iranian guz-), with lengthening of the root vowel in the present gūhati. Nourai's macron-less 'gŭhati' with a breve is Pokorny's typographic convention for the short/zero grade of the root; Whitney and Monier-Williams print gūhati with a long ū. Verdict: word, language and descent all correct; the vowel notation is Pokorny's, not an error of substance.\",\n     \"derivation_fa\": \"سنسکریت gūhati «می‌پوشاند، پنهان می‌کند» (از ریشهٔ guh-، با اسم‌های guhā «نهانگاه، غار» و gūḍha- «پنهان») شاخهٔ هندی همین ریشه است: هندواروپایی *gʰeugʰ- در هندوایرانی *gʰaugʰ-/*gʰugʰ- و در هندی با تبدیل *gʰ به h به guh- می‌رسد، حال آنکه در ایرانی همان واج به z بدل شده (guz-). واکهٔ کشیدهٔ ū در ستاک حال gūhati کشش ثانوی است. علامت کوتاهِ «ŭ» در نمودار نورایی از شیوهٔ نگارش پوکورنی گرفته شده است، نه خطای صورت. حکم: ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"POK:450\", \"status\": \"supports\", \"note\": \"POK_full.txt p.450: 'Material: Old Indic guhati, gūhati \\\"hidden\\\" (Aor. aghukṣat), guhā \\\"hideout, cave\\\", goha-ḥ \\\"hideout, lair\\\"' — Pokorny's very first witness for the root.\"},\n      {\"ref\": \"KNT:182\", \"status\": \"supports\", \"note\": \"KNT.txt p.182b s.v. gaud-: 'Av. gaoz-, Skt. gūhati (§88)' — Kent cites the Sanskrit present exactly as the cognate of the Old Persian verb.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SYN\", \"where\": \"p.852 §12.27.8\", \"stance\": \"supports\",\n       \"note\": \"'Skt. guh- (3sg. pres. gūhati), Av. guz-, OPers. gud- … perh. : Lith. gūžti \\\"cover something warm\\\". Walde-P. 1.566 f.'\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p.117 s.v. *gauz, *SANSKRIT\", \"stance\": \"supports\",\n       \"note\": \"'*SANSKRIT: guh \\\"to hide\\\" (RV+) = EWAia I: 502' — Mayrhofer's EWAia is the modern standard reference and agrees.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I p.566\", \"stance\": \"supports\",\n       \"note\": \"the Indic forms head the entry; WLD I 566 is the source Pokorny cites.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 7,\n   \"root\": \"Ghlâd\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ǵʰreh₁d- 'to sound, resound' (Pokorny 451 'ghlad-'; also written *ǵʰleh₂d-)\",\n   \"note\": \"Pokorny IEW p.451 has 'Root / lemma: ghlad- | Meaning: to sound, call', with the material Nourai uses: 'Old Indic hradate \\\"sounds\\\", hrada- m. \\\"noise\\\", Avestan zrada- \\\"coat of mail, garment made of linked metal rings\\\" (\\\"rattling, clashing\\\"), npers. zirih \\\"armor\\\" …; Gk. κέχλαδα (Pind.), καχλάζω; Old Irish ad-gladur'. So the root label, the language tag and the gloss 'to sound, to ring' are Pokorny's own, page and all. Two updates the chart does not carry: (1) modern reconstruction writes the root with -r-, *ǵʰreh₁d- (Wiktionary; the -l- of Pokorny's lemma is a variant *ǵʰleh₂d- seen in the Greek and Old Irish forms) — this matters because the Iranian and Germanic branches both require -r-; (2) Pokorny himself ends the entry 'The Aryan words can but just as well with Indo-European r to Gothic gretan belong; see below gher-1', which is precisely the arrow Nourai draws in node 6, and modern Wiktionary simply files Germanic *grētaną under *ǵʰreh₁d- alongside Avestan zrāda — i.e. the two 'roots' of the chart are now one.\",\n   \"note_fa\": \"پوکورنی در صفحهٔ ۴۵۱ مدخل «ghlad- : آواز دادن، بانگ زدن» را دارد با همان شواهدی که نورایی می‌آورد: سنسکریت hrādate «آوا می‌دهد»، اوستایی zrāda- «زره» (یعنی «آنچه به‌هم می‌خورد و بانگ می‌دهد»)، فارسی zirih، یونانی κέχλαδα و ایرلندی کهن ad-gladur. پس برچسب ریشه و معنای آن درست است. دو نکتهٔ امروزی: نخست آنکه بازسازی کنونی این ریشه را با r می‌نویسد (*ǵʰreh₁d-) و صورت لام‌دار *ǵʰleh₂d- را گونه‌ای کناری می‌شمارد؛ دوم آنکه خود پوکورنی در پایان همین مدخل می‌نویسد واژه‌های آریایی را می‌توان با gretan گوتی زیر gher-1 نیز نهاد ــ که همان پیوندی است که نورایی در گرهٔ ۶ کشیده است. حکم: ادعای نورایی دربارهٔ ریشه درست است.\",\n   \"sources\": [W_GHRED],\n   \"ref_check\": [\n    {\"ref\": \"POK:451\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt (line ~38009): 'Root / lemma: ghlad- | Meaning: to sound, call | Material: Old Indic hradate \\\"sounds\\\", hrada- m. \\\"noise\\\", Avestan zrada- m. \\\"coat of mail, garment made of linked metal rings\\\" (\\\"rattling, clashing, clinking\\\"), npers. zirih \\\"armor, coat of mail\\\" … References: WP. I 659 f. Page(s): 451'. Root name, gloss and page all exactly as in the chart.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I pp. 659 f. (cited by Pokorny as his source)\", \"stance\": \"supports\",\n     \"note\": \"POK's 'References: WP. I 659 f.' for ghlad-; the Walde-Pokorny entry is the origin of Pokorny's lemma and of the Indo-Iranian material.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, gh- section\", \"stance\": \"silent\",\n     \"note\": \"grep 'ghlad' in AHD_watkins1985.txt = 0 hits. Watkins has gher-2 'to call out' (with GREET) but no separate ghlad-, which is consistent with modern practice of merging the two.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, ghladh- / ghlādh- 'smooth, bright'\", \"stance\": \"silent\",\n     \"note\": \"Mann's ghladh- lemma is 'smooth, bright, glad' (OHG glat, OCS gladŭkŭ) — a homophonous but unrelated root; he has no 'sound' lemma of this shape.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"zrâda\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Avestan zrāδa- m. 'coat of mail, ring armour', attested in Vīdēvdād 14.9 in the list of weapons ('yaēšąm zayanąm … haptaθa zrāδa') and 12.x beside paiti.dāna-. Bartholomae AiW col. 1703 heads it 'j. zrāδa- m. \\\"Panzerkoller, Panzer\\\"'. Its derivation from the 'sound' root is Pokorny's: *ǵʰreh₁d- 'to resound' → 'the rattling thing' → 'mail-shirt' (Skt. hrādate 'it rattles' is the same root with the regular Indic *ǵʰ > h; Iranian palatalises the initial to z, and the *d appears as the intervocalic spirant δ). The semantic step is the standard 'clashing/rattling' > 'ring-mail' one and is accepted by Wiktionary's *ǵʰreh₁d- page, which lists Avestan zrāda 'chainmail' among the descendants (marked with a question mark).\",\n     \"derivation_fa\": \"اوستایی zrāδa- «زره، جوشن حلقه‌دار» در وندیداد ۱۴٫۹ در فهرست جنگ‌افزارها آمده است؛ بارتولومه (ستون ۱۷۰۳) آن را «Panzerkoller, Panzer» معنا می‌کند. پیوند آن با ریشهٔ «آوا دادن» از آنِ پوکورنی است: *ǵʰreh₁d- «بانگ دادن» ← «آنچه به‌هم می‌خورد و می‌خرد» ← «جامهٔ حلقه‌های آهنین»؛ قس سنسکریت hrādate «صدا می‌دهد» با همان ریشه. در ایرانی *ǵʰ آغازین به z و *d میان‌واکه‌ای به δ بدل شده است. ویکی‌واژه نیز zrāda اوستایی را (با علامت تردید) در زیر همین ریشه می‌آورد. حکم: ادعای نورایی درست است.\",\n     \"sources\": [W_GHRED],\n     \"ref_check\": [\n      {\"ref\": \"POK:451\", \"status\": \"supports\", \"note\": \"POK_full.txt p.451 s.v. ghlad-: 'Avestan zrada- m. \\\"coat of mail, garment made of linked metal rings\\\" (\\\"rattling, clashing, clinking, chinking\\\")' — the arrow root→Avestan is Pokorny's own.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"col. 1703 (local scan leaf 927)\", \"stance\": \"supports\",\n       \"note\": \"'j. zrāδa- m. \\\"Panzerkoller, Panzer\\\": yaēšąm zayanąm … haptaθa \\\"…\\\" V.14.9; — …ahe … paiti.dānahe Vd.12.' Bartholomae's col. 1703 is also the reference Jeffery (FVQ 169) and Mo'in (BQT footnote) cite for this word.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, p.247 s.v. zrēh\", \"stance\": \"partial\",\n       \"note\": \"'all these forms presuppose *zradda- and do not tally with Av. (1703) zrāδa- (Vd. 14.9 without variant; Phl. Vd. has zrāt evidently through the influence of the Av. form). Some importance should perhaps be attached to the curious gen. zaraδvehe (1703).' Nyberg accepts the word but flags that the Avestan and Middle Persian forms do not match exactly.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 659 f.\", \"stance\": \"supports\",\n       \"note\": \"the source Pokorny cites for the ghlad- material including the Avestan noun.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"zrih\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian zrēh 'armour, mail', written <zlyh> in Book Pahlavi. MacKenzie's Concise Pahlavi Dictionary has it as a minimal pair with the homograph for 'sea': '¹zrēh [zlyh | P zryh] sea, lake' and '²zrēh [zlyh | N zirih] armour', the second explicitly glossed with New Persian zirih. Nyberg II 247 spells it 'zrēh [zlyh], zrē [zlyd] armour, harness'. The step Av. zrāδa- → MP zrēh involves loss of the final vowel, the Middle Persian shift of intervocalic δ to h (as in Av. -aδa- > MP -ēh) and the reduction of the unstressed first syllable; Pāzand writes it z(a)reh. Nourai's 'zrih' is the Pāzand/New Persian transliteration (Jeffery FVQ 169 also writes 'Phlv. zrih'), a spelling variant rather than an error. Nyberg's caveat (see node 1) is that the Armenian, Syriac, Arabic and NP reflexes all point to a base *zradda-, so the exact prehistory of the -ēh is not fully regular.\",\n     \"derivation_fa\": \"فارسی میانه zrēh «زره» با املای پهلوی <zlyh>. مکنزی آن را جفت کمینهٔ zrēh «دریا» می‌آورد: «²zrēh [zlyh | فارسی نو zirih] زره». نیبرگ (ج ۲، ص ۲۴۷) نیز «zrēh [zlyh]، zrē [zlyd] : زره، ساز جنگ» ثبت کرده است. گذار از zrāδa- اوستایی به zrēh پهلوی با افتادن واکهٔ پایانی، بدل شدن δ میان‌واکه‌ای به h و کوتاه شدن هجای نخست انجام گرفته؛ در پازند z(a)reh نوشته می‌شود. صورت «zrih» که نورایی آورده همان خوانش پازندی/فارسی نو است (جفری نیز «Phlv. zrih» می‌نویسد) و خطا نیست. حکم: ادعای نورایی درست است، با این احتیاط که نیبرگ صورت پایه را *zradda- می‌داند نه مستقیماً zrāδa-.\",\n     \"sources\": [W_ZEREH],\n     \"ref_check\": [\n      {\"ref\": \"VDQ:257\", \"status\": \"supports\",\n       \"note\": \"VDQ is Badre'i's Persian translation of Jeffery's Foreign Vocabulary of the Qur'an, same entry order; the substance is verifiable in FVQ.txt p.169 s.v. سرد (Sard): 'Av. zraδa (AIW, 1703) means a coat of mail, and becomes in Phlv. zrih, whence Mod. Pers. زره and Arm. զրահ, and also was borrowed into Syr. as ܙܪܕܐ.' Jeffery's 'Phlv. zrih' is exactly Nourai's Pahlavi box, spelling included.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.99 s.v. zrēh (PHD_mackenzie.txt line 5855-6)\", \"stance\": \"supports\",\n       \"note\": \"'¹zrēh [zlyh | P zryh] sea, lake. ²zrēh [zlyh | N zirih] armour.' MacKenzie links the Pahlavi word directly to NP zirih.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p.247 s.v. zrēh\", \"stance\": \"partial\",\n       \"note\": \"'zrēh [zlyh], zrē [zlyd] armour, harness 6.9, 20.13-14, 85.15, 120.27. — Arm. lw. zrah-kʻ; Syr. lw. zardā \\\"coat of mail\\\", Talm. zrdʾ, Telegdi 243, Arab. lw. zarad-; Paz. z(a)reh; NP zirih, zarah: all these forms presuppose *zradda- and do not tally with Av. (1703) zrāδa-.' Supports the Pahlavi word and its loans, but questions the exact Avestan filiation.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 660, p.146\", \"stance\": \"supports\",\n       \"note\": \"'zirih \\\"Panzer\\\". aw. zraδa- \\\"Panzer\\\"; phlv. zrat (pāz. zareh) bezw. zrad (aram. LW. זרד, arab. zarad, zarad[xāne]).' Horn gives the Pahlavi link and, in the same breath, the Aramaic/Arabic loans.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"zereh «زره»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP زره zereh (classically zirih) 'coat of mail'. It continues MP zrēh directly: Middle Persian ē regularly appears in early New Persian orthography as ی and is read i/e, and the Pahlavi consonant cluster zr- is broken by an anaptyctic vowel in the classical pronunciation zirih (Hübschmann Persische Studien §12 treats np. zirih under exactly this heading, and §34b under the -tr-/-dr- development). Horn no. 660 (p.146) and Hübschmann pp.70-71 both give the chain Av. zrāδa- → Phlv. → NP zirih, together with the collateral loans Kurd. zirih/zirt, Balochi zirih, Afghan zira, Arm. zrah. Mo'in's footnote in Borhan-e Qate' (vol. 2, printed p.1019/1020, note 1 on the headword زره) states it in Persian: 'پهلوی zrah، پازند zareh، اوستایی zrāδa- «بارتولومه ۱۷۰۳»؛ ارمنی zrah، آرامی zardā (و زردِ عربی از آن مأخوذ است) … رک: هوبشمان ۷۱'.\",\n     \"derivation_fa\": \"«زره» (تلفظ کلاسیک zirih) دنبالهٔ مستقیم zrēh فارسی میانه است: ē فارسی میانه در فارسی نو به ی/کسره بدل شده و خوشهٔ آغازین zr- با واکهٔ میانجی شکسته شده است (زِ‑رِه). هرن (شمارهٔ ۶۶۰، ص ۱۴۶) و هوبشمان (ص ۷۰-۷۱) هر دو زنجیرهٔ اوستایی zrāδa- ← پهلوی ← فارسی zirih را می‌دهند و وام‌های همسایه را نیز برمی‌شمارند: کردی zirih/zirt، بلوچی zirih، پشتو zira، ارمنی zrah. معین نیز در حاشیهٔ برهان قاطع (ج ۲، ص ۱۰۱۹/۱۰۲۰، حاشیهٔ ۱ ذیل «زره») همین را می‌نویسد و می‌افزاید که «زردِ عربی از آن مأخوذ است». حکم: ادعای نورایی درست است.\",\n     \"sources\": [W_ZEREH],\n     \"ref_check\": [\n      {\"ref\": \"POK:451\", \"status\": \"supports\", \"note\": \"POK_full.txt p.451 s.v. ghlad-: '… npers. zirih \\\"armor, coat of mail, garment made of linked metal rings\\\"' — Pokorny names the New Persian word himself.\"},\n      {\"ref\": \"HRN:146\", \"status\": \"supports\", \"note\": \"HRN.txt line 5841, page 146 (the running head '— 147 —' follows immediately): '660. zirih \\\"Panzer\\\". aw. zraδa- \\\"Panzer\\\"; phlv. zrat (pāz. zareh) bezw. zrad (aram. LW. זרד, arab. zarad, zarad[xāne]).' Horn entry number and page are exactly Nourai's citation.\"},\n      {\"ref\": \"BQT:1019\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 480 (= printed p.1020, the entry begins at the top of the column, its footnote 1 straddling pp.1019-1020): headword 'زره = بکسر اول و ثانی … حلقه‌های آهنین ترتیب داده‌اند …' with Mo'in's footnote 'پهلوی zrah، پازند zareh، اوستایی zrāδa- «بارتولومه ۱۷۰۳»، ارمنی zrah، آرامی zardā (و زردِ عربی از آن مأخوذ است) … کردی zirih, zirt، بلوچی zirih، پشتو zirah … رک: هوبشمان ۷۱.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HUB\", \"where\": \"Persische Studien pp. 70-71 and §12\", \"stance\": \"supports\",\n       \"note\": \"'zirih \\\"Panzer\\\" = zd. zrada-' (p.70, in the list of z < IE ǵʰ words) and 'Ueber np. zirih \\\"Panzer\\\" siehe §12' (p.~26); also 'zrahkʻ \\\"Panzer\\\"' among the Armenian loans.\"},\n      {\"src\": \"BQT\", \"where\": \"vol. 2, printed pp.1019-1020, headword زره + Mo'in's footnote 1\", \"stance\": \"supports\",\n       \"note\": \"see ref_check; Mo'in's note is the Persian-language statement of exactly Nourai's chain, plus the Arabic loan.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt pdf page ~422 (comparative table with زره)\", \"stance\": \"silent\",\n       \"note\": \"Aryanpur has a cognate table listing Avestan/Old Persian/Pahlavi/Armenian forms against زره, but the OCR of the Latin-script column is unusable, so nothing quotable.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Arabic\", \"words\": \"zard, sarad; zarrâd\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The Arabic words are real and their connection to the Iranian family is well established, but the arrow is drawn from the wrong place. Arabic زَرَد zarad 'ring-mail' is not an Indo-European inheritance: it is a pre-Islamic loan from Middle Persian zrēh (i.e. it should hang from node #2), 'possibly direct from Persia, or maybe through Syriac' (Jeffery). The Syriac intermediary ܙܰܪܕܳܐ zardā / Jewish-Babylonian-Aramaic זרדא is the usual assumption; Wiktionary s.v. زرد: 'From an early West Iranian source, probably via Aramaic זַרְדָּא / ܙܰܪܕܳܐ (zarədā)', and Nyberg II 247 lists 'Syr. lw. zardā \\\"coat of mail\\\", Talm. zrdʾ … Arab. lw. zarad-' as loans FROM Middle Persian. سَرْد sard, the Qur'anic word (Q 34:10-11, of David's mail-making), is according to Jeffery 'but a form of زرد' with s for z; the native Arab grammarians instead derived it from the root س-ر-د 'to stitch, plait' — Jeffery's argument against them is that they themselves knew the agent noun had to be zarrād, not sarrād (as-Sijistānī 177). زَرَّاد zarrād 'mail-maker' is then the regular Arabic faʿʿāl agent noun built on the borrowed root ز-ر-د. Verdict plausible: every word and every gloss in the box is right, but the direction Nourai's tree implies (IE root → Arabic, parallel to Avestan) inverts the actual route Iranian → Aramaic → Arabic.\",\n     \"derivation_fa\": \"واژه‌های عربی این جعبه راست‌اند و پیوندشان با خانوادهٔ ایرانی نیز پذیرفته است، اما جهت پیکان نادرست است. زَرَد عربی میراث هندواروپایی نیست بلکه وام‌واژه‌ای پیش از اسلام از فارسی میانهٔ zrēh است ــ یعنی می‌بایست از گرهٔ پهلوی (شمارهٔ ۲) آویخته شود، نه از خودِ ریشه. واسطه به احتمال زیاد سریانی zardā و آرامی بابلی זרדא بوده است؛ ویکی‌واژه می‌نویسد «از منبعی ایرانی غربی کهن، احتمالاً از راه آرامی zarədā»، و نیبرگ نیز zardā سریانی و zarad عربی را وام از فارسی میانه می‌شمارد. سَرْد قرآنی (سبأ ۱۰-۱۱) به گفتهٔ جفری تنها گونه‌ای از زَرَد با ابدال ز به س است؛ نحویان عرب آن را از ریشهٔ س-ر-د «به هم بافتن» می‌گرفتند، ولی جفری یادآور می‌شود که خودشان هم می‌دانستند نام فاعل باید زَرّاد باشد نه سَرّاد. زَرّاد نیز صیغهٔ فَعّال منظم بر همان ریشهٔ وام‌گرفتهٔ ز-ر-د است. حکم: با احتیاط پذیرفتنی است؛ مسیر درست ایرانی ← آرامی ← عربی است، نه هندواروپایی ← عربی.\",\n     \"sources\": [W_ZARAD],\n     \"ref_check\": [\n      {\"ref\": \"VDQ:257\", \"status\": \"partial\",\n       \"note\": \"VDQ = Badre'i's Persian translation of Jeffery; the corresponding passage is FVQ.txt p.169 s.v. سرد (Sard): 'Chain armour, i.e. work of rings woven together. It occurs only in a passage relating to David's skill as an armourer [Q xxxiv,10]. The Muslim authorities derive it from سرد to stitch or sew … though it is curious that they know that armourer ought to be Zarrād rather than Sarrād (as-Sijistānī, 177). As a matter of fact سرد seems to be but a form of زرد … This زرد is a borrowing from Iranian sources as Fraenkel, Vocab, 13, noted. Av. zraδa (AIW, 1703) means a coat of mail, and becomes in Phlv. zrih, whence Mod. Pers. زره … and also was borrowed into Syr. as ܙܪܕܐ. The word was a pre-Islamic borrowing, possibly direct from Persia, or maybe through Syriac.' Supports every word of the box but makes the Arabic a loan from Middle Persian, not a sister of Avestan.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FVQ\", \"where\": \"Jeffery p.169 s.v. سرد\", \"stance\": \"partial\", \"note\": \"quoted in full above; the source behind VDQ:257.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen, p.142 s.v. zarad / zarada\", \"stance\": \"contradicts\",\n       \"note\": \"'zarad: \\\"Ringpanzer, Kettenkleid\\\" aus pers. زره zreh < mp. zreh, av. zrāδa, gen. zaraδahe; ar. Lw. زرد zarad, syr. zardā' and 'zarada: \\\"einen Ringpanzer machen, aus Ringen eine Kette machen\\\"'. Asbaghi files zarad squarely as a Persian loanword in Arabic — contradicting a direct IE→Arabic arrow.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p.247 s.v. zrēh\", \"stance\": \"contradicts\",\n       \"note\": \"'Arm. lw. zrah-kʻ; Syr. lw. zardā \\\"coat of mail\\\", Talm. zrdʾ … Arab. lw. zarad-' — all marked 'lw.' (loanword) from the Middle Persian word.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, AFM.txt line ~3208\", \"stance\": \"supports\",\n       \"note\": \"'زرد وزرد به وزراد ودرع وأدرع وتدرع … زره بالتركية [read: بالفارسية]' — Addi Shir lists زرد/زراد among the Persianisms in Arabic, glossing with زره.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 660, p.146\", \"stance\": \"contradicts\",\n       \"note\": \"'phlv. zrat (pāz. zareh) bezw. zrad (aram. LW. זרד, arab. zarad, zarad[xāne])' — Horn derives the Arabic from the Pahlavi via Aramaic.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Persian\", \"words\": \"zarrâd «زرّاد»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP زرّاد zarrād 'armourer, mail-maker' with its compounds زرّادخانه zarrādxāne 'armoury, arsenal' and زرّادگاه zarrādgāh. This is a textbook Persian → Arabic → Persian round trip: MP zrēh gave Arabic زَرَد zarad; Arabic built the faʿʿāl agent noun زَرَّاد zarrād on it; and Persian then re-borrowed that Arabic agent noun, which is why the word carries a šadda and the Arabic morphological shape rather than a native Persian agent suffix (-gar, -bān). Mo'in tags it exactly so: 'زراد [معر.] (ص.) آنکه زره سازد' — [معر.] = معرَّب, 'Arabicised'. The compounds are then Persian formations on the re-borrowed noun (zarrād + Persian خانه / گاه); Horn already cites 'arab. zarad, zarad[xāne]' at no. 660.\",\n     \"derivation_fa\": \"«زرّاد» یعنی زره‌ساز، با ترکیب‌های «زرّادخانه» و «زرّادگاه». این نمونهٔ روشنی از رفت‌وبرگشت فارسی ← عربی ← فارسی است: zrēh فارسی میانه به عربی رفت و زَرَد شد؛ عرب بر آن صیغهٔ فَعّال ساخت و زَرّاد پدید آمد؛ سپس همین صورت معرَّب دوباره به فارسی بازگشت. نشانهٔ بازگشت، تشدید و ساخت عربی واژه است، چون اگر ساخت فارسی می‌بود «زره‌گر» یا «زره‌ساز» می‌شد. معین نیز آن را با نشان [معر.] یعنی معرَّب ثبت کرده است: «زراد [معر.] (ص.) آنکه زره سازد». ترکیب‌های زرّادخانه و زرّادگاه ساخته‌های فارسی روی همین واژهٔ بازگشته‌اند؛ هرن نیز در شمارهٔ ۶۶۰ «arab. zarad, zaradxāne» را می‌آورد. حکم: ادعای نورایی درست است.\",\n     \"sources\": [W_ZARAD],\n     \"ref_check\": [\n      {\"ref\": \"MON:1729\", \"status\": \"supports\",\n       \"note\": \"MON_part1.txt line 70804: 'زراد: [معر.] (ص.) آنکه زره سازد' and line 70809 'زرادگاه [معر. + ف. = زرادگه] (امر.)'; MON_part2.txt line 15591 'اسلحه‌خانه، سلاح‌خانه، زرادخانه'. Mo'in's [معر.] tag ('Arabicised') is precisely the Arabic→Persian arrow Nourai draws, and the two compounds of the script_extra field are in Mo'in too.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"s.v. زراد, زرادگاه, زرادخانه\", \"stance\": \"supports\", \"note\": \"see ref_check; the [معر.] bracket is Mo'in's own origin tag.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 660, p.146\", \"stance\": \"supports\",\n       \"note\": \"'arab. zarad, zarad[xāne]' — Horn already notes the Arabic derivative and the xāne compound alongside NP zirih.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, AFM.txt line ~3208\", \"stance\": \"supports\",\n       \"note\": \"'زرد وزرد به وزراد ودرع وأدرع وتدرع' — the Arabic agent noun زراد is in Addi Shir's list of Arabic words of Persian origin.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi p.142\", \"stance\": \"supports\",\n       \"note\": \"Asbaghi's entry 'zarada: \\\"einen Ringpanzer machen, aus Ringen eine Kette machen\\\"' shows the Arabic denominal verb built on the loan, the base of zarrād.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Indo-European\", \"words\": \"Gher 2\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"A cross-reference node: Nourai links his Ghlâd to his root Gher 2 'to call out'. This is not his own invention — it is Pokorny's own closing sentence at IEW 451: 'The Aryan words can but just as well with Indo-European r to Gothic gretan belong; see below gher-1', i.e. Skt. hrādate / Av. zrāda may belong not with the l-form but with the r-form of the root, which Pokorny files as gher-1 (expressive root) on p.439 — exactly the two page numbers Nourai cites, POK:439,451. Watkins prints the same root as 'gher-2. To call out. Extended root *ghréd-' with '[Pok. 1. gher- 439]'. Modern reconstruction has completed the merger: Wiktionary's *ǵʰreh₁d- 'to sound' lists Sanskrit hrādate, Avestan zrāda AND Germanic *grētaną under one root, so the two boxes of this chart are today a single etymon. The only quibble is the numbering: Nourai's 'Gher 2' answers to Watkins' gher-2 but to Pokorny's gher-1.\",\n     \"derivation_fa\": \"این گره ارجاعی است: نورایی ریشهٔ Ghlâd را به ریشهٔ Gher 2 «بانگ زدن» می‌پیوندد. این پیوند ساختهٔ خودِ او نیست؛ پوکورنی در پایان مدخل ghlad- (ص ۴۵۱) می‌نویسد که واژه‌های آریایی را می‌توان با r هندواروپایی به gretan گوتی نیز نسبت داد و به gher-1 (ص ۴۳۹) ارجاع می‌دهد ــ یعنی همان دو صفحه‌ای که نورایی یاد کرده است. واتکینز نیز در پیوست فرهنگ American Heritage همین ریشه را «gher-2: بانگ زدن، ریشهٔ گستردهٔ *ghréd-» می‌نامد و به پوکورنی ۴۳۹ ارجاع می‌دهد. ریشه‌شناسی امروزی این دو را یکی کرده است: ویکی‌واژه زیر *ǵʰreh₁d- هم hrādate سنسکریت و zrāda اوستایی و هم *grētaną ژرمنی را می‌آورد. تنها ایراد، شمارهٔ ریشه است: «Gher 2»ی نورایی با gher-2 واتکینز می‌خواند ولی با gher-1 پوکورنی. حکم: ادعای نورایی درست است.\",\n     \"sources\": [W_GHRED],\n     \"ref_check\": [\n      {\"ref\": \"POK:439\", \"status\": \"supports\",\n       \"note\": \"POK_full.txt (line ~33008): 'Root / lemma: gher-1 | Meaning: expr. root | Material: … here perhaps ghre-d- in Gothic gretan, Old Norse grata, OSax. gratan, Old English grǣtan …; ablaut. causative Old Icelandic grǣta \\\"reduce to tears\\\", Old English grētan \\\"assail, greet\\\", OSax. grōtian \\\"call\\\", Old High German gruozen, NHG grüßen … References: WP. I 605. Page(s): 439.' Both Germanic words of node #7 are on this page.\"},\n      {\"ref\": \"POK:451\", \"status\": \"supports\",\n       \"note\": \"POK_full.txt p.451 s.v. ghlad-, closing line: 'The Aryan words can but just as well with Indo-European r to Gothic gretan belong; see below gher-1.' This IS the arrow Ghlâd → Gher 2.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. gher-2\", \"stance\": \"supports\",\n       \"note\": \"'gher-2. To call out. Extended root *ghréd-. Germanic *grotjan in Old English grētan, to speak to, greet: GREET. [Pok. 1. gher- 439.]' — the root name, gloss and Pokorny page all match the node.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. greet 'to weep'\", \"stance\": \"supports\",\n       \"note\": \"'They derive from I.-E. base *ghred-, \\\"to sound, clash, speak loudly\\\", whence also OI. hrādate, \\\"it sounds, rustles\\\".' Klein unites the Germanic verbs and the Sanskrit 'sound' verb under one base, i.e. he too merges Ghlâd and Gher 2.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann, grep 'ghlad'/'gher'\", \"stance\": \"silent\",\n       \"note\": \"Mann's ghladh-/ghlādh- lemmas are the 'smooth, bright' root, not this one; no comparable 'call out' lemma was found.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Germanic\", \"words\": \"grĕtan; grôtjan\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Two Germanic reflexes of the extended root *ǵʰreh₁d- / *ghréd-. (a) *grētaną, in Gothic grētan, Old Norse gráta, Old Saxon grātan, Old English grētan/grǣtan 'to weep, bewail, lament'; Klein: 'The orig. sense of all these verbs was \\\"to sound, speak, shout\\\". They derive from I.-E. base *ghred-, \\\"to sound, clash, speak loudly\\\", whence also OI. hrādate.' Nourai's gloss 'to moan' is a fair rendering of the attested 'weep, bewail'. (b) the causative *grōtjan 'to make (someone) speak, address', in Old English grētan 'to address, approach, greet', OS grōtian 'to call', OHG gruozen, MHG grüezen, NHG grüßen, Du. groeten; Klein: 'fr. Teut. base *grōtjan, orig. \\\"to cause to speak\\\"'. The ē : ō alternation is the normal Germanic strong-verb / ō-causative pair (Verner-free, from PIE full grade vs o-grade *ghrōd-eye-). Nourai's spellings 'grĕtan' and 'grôtjan' are the ordinary handbook transcriptions; note that grōtjan is a reconstructed West-Germanic form, not an attested word, which the box does not signal.\",\n     \"derivation_fa\": \"دو بازتاب ژرمنی از ریشهٔ گسترده‌شدهٔ *ǵʰreh₁d-: نخست *grētaną که در گوتی grētan، نورس باستان gráta و انگلیسی کهن grētan/grǣtan «گریستن، مویه کردن» بازمانده است؛ کلاین می‌نویسد معنای اصلی همهٔ این فعل‌ها «آوا دادن، سخن گفتن، بانگ زدن» بوده و از پایهٔ هندواروپایی *ghred- آمده‌اند، همان پایه‌ای که hrādate سنسکریت نیز از آن است. دوم ستاک سببی *grōtjan «به سخن واداشتن، خطاب کردن» که به انگلیسی کهن grētan «خطاب کردن، درود گفتن»، ساکسون باستان grōtian «فراخواندن» و آلمانی grüßen رسیده است. جفتِ ē/ō همان تناوب معمول فعل قوی و فعل سببی ō‑دار در ژرمنی است (درجهٔ کامل در برابر درجهٔ o). یادآوری: grōtjan صورتی بازسازی‌شده است نه واژه‌ای گواهی‌شده، و نمودار این را نشان نمی‌دهد. حکم: ادعای نورایی درست است.\",\n     \"sources\": [E_GREET],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt line 522: 'gher-2. To call out. Extended root *ghréd-. Germanic *grotjan in Old English grétan, to speak to, greet: GREET. [Pok. 1. gher- 439.]' — Watkins gives the very form *grotjan and the very gloss ('to speak to') that Nourai's box carries. He does not print grētan, which comes from Pokorny 439 / Klein.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.vv. greet (to salute) and greet (to weep)\", \"stance\": \"supports\",\n       \"note\": \"'greet, tr. v., to salute. — ME. greten, fr. OE. gretan … rel. to OS. grotian, OFris. greta, Du. groeten, OHG. gruoyen, MHG. grüeyen, G. grüßen, \\\"to salute, greet\\\", fr. Teut. base *grōtjan, orig. \\\"to cause to speak\\\"' and 'greet, intr. v., to weep … rel. to OS. gratan, ON. grata, Dan. græde, Goth. gretan, greitan, \\\"to weep\\\" … They derive from I.-E. base *ghred-, \\\"to sound, clash, speak loudly\\\", whence also OI. hrādate.'\"},\n      {\"src\": \"POK\", \"where\": \"IEW p.439 s.v. gher-1\", \"stance\": \"supports\",\n       \"note\": \"'here perhaps ghre-d- in Gothic gretan, Old Norse grata, asachs. gratan, Old English grǣtan … Old English grētan \\\"assail, greet\\\", asachs. grotian \\\"call\\\", Old High German gruozen, NHG grüßen' — both stems, with the ē/ō pair.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, s.v. Regret / Greet\", \"stance\": \"supports\",\n       \"note\": \"SKT.txt line 15858: 'Regret, sorrow. (F. — L. and O. Low [G.])' — Skeat too takes the second element of regret from Low German/Norse grātan.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"English\", \"words\": \"regret; greet\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"GREET: OE grētan 'to come in contact with, address, accost, salute' < West Germanic *grōtjan (OS grōtian, Du. groeten, OHG gruozen, G. grüßen); ME greten > NE greet. Etymonline notes the probable original sense 'to resound', linking it to OE grǣtan 'weep, bewail' — the same pair as node #7. REGRET is a French detour rather than a direct Germanic inheritance: ME regretten < Middle French regreter, Old French regreter 'to long after, bewail, lament someone's death' = re- (intensive) + a Germanic element, 'probably from Frankish or another Germanic source, compare Old English grǣtan \\\"to weep\\\", Old Norse grāta \\\"to weep, groan\\\"' (Etymonline); Klein: 'prob. formed fr. re- and ON. grāta, \\\"to weep, lament\\\", which is rel. to Goth. gretan, OE. grǣtan.' Etymonline flags that the word 'is not found in other Romance languages, and [is] variously explained', so the Germanic etymon is probable rather than certain. Both English words therefore do descend from the node above, but by different routes — greet natively, regret through Old French — and the chart's single arrow hides that.\",\n     \"derivation_fa\": \"«greet» بازماندهٔ بومی است: انگلیسی کهن grētan «خطاب کردن، درود گفتن» از ژرمنی غربی *grōtjan (قس آلمانی grüßen، هلندی groeten)، و از آن انگلیسی میانه greten و انگلیسی نو greet. اتیمونلاین معنای آغازین آن را «طنین انداختن» می‌داند و آن را با grǣtan «گریستن» یک‌جا می‌آورد. اما «regret» وام‌واژه است نه میراث مستقیم: انگلیسی میانه regretten از فرانسهٔ میانه regreter و فرانسهٔ کهن regreter «در سوگ کسی نالیدن» که از پیشوند تأکیدی re- و عنصری ژرمنی (فرانکی یا نورس؛ قس نورس باستان grāta و انگلیسی کهن grǣtan «گریستن») ساخته شده است. کلاین نیز همین را می‌گوید. اتیمونلاین می‌افزاید که این واژه در دیگر زبان‌های رومی نیست و توضیح‌های گوناگون برای آن داده‌اند، پس ریشهٔ ژرمنی محتمل است نه قطعی. حکم: ادعای نورایی درست است، اما دو واژه از دو راه ــ یکی ارثی و دیگری از راه فرانسه ــ به انگلیسی رسیده‌اند و نمودار این تفاوت را نشان نمی‌دهد.\",\n     \"sources\": [E_GREET, E_REGRET],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"The node carries no refs in the book (refs=None); the parent Germanic box's AHD citation covers GREET ('Germanic *grotjan in Old English grétan, to speak to, greet: GREET').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.vv. regret, greet\", \"stance\": \"supports\",\n       \"note\": \"'regret, tr. v. — ME. regretten, fr. MF. regrater, regreter (F. regretter), fr. OF. The orig. meaning of this verb was \\\"to bewail the dead\\\"; it is prob. formed fr. re- and ON. grāta, \\\"to weep, lament\\\", which is rel. to Goth. gretan, OE. grǣtan, of s.m. See greet, \\\"to lament\\\".'\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, s.v. Regret (SKT.txt line 15858)\", \"stance\": \"supports\",\n       \"note\": \"'Regret, sorrow. (F. — L. and O. Low [German])' — Skeat's formula marks it as French from a Low German source, agreeing with Klein and Etymonline.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gher-2\", \"stance\": \"partial\",\n       \"note\": \"Watkins lists only GREET under gher-2; REGRET is absent from his root list (as a French borrowing it falls outside the appendix's Germanic-inheritance entries).\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-193.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk193.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-193.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 193",
 "description": "Write and check page-193.json"
}
```


### [2026-09-06T02:31:25.271Z] TOOL RESULT

```
written
JSON OK
nodes verified: 13/13
node verdicts: {'plausible': 3, 'confirmed': 10}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 17, 'contradicts': 2, 'not_found': 1, 'partial': 3, 'not_checked': 1}
books consulted: {'contradicts': 4, 'partial': 7, 'supports': 26, 'silent': 6} | by book: {'BRT': 4, 'CHEUNG': 4, 'HRN': 4, 'WLD': 3, 'NYB': 3, 'KLN': 3, 'MON': 2, 'ARY': 2, 'PLA': 2, 'AFM': 2, 'AHD': 2, 'SKT': 2, 'KNT': 1, 'SOD': 1, 'TTS': 1, 'SYN': 1, 'PHD': 1, 'HUB': 1, 'BQT': 1, 'FVQ': 1, 'IEC': 1, 'POK': 1}
```


## [2026-09-06T02:31:32.479Z] TOOL CALL #68: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /home/sfmqrb/git/rishe/site/pages/193.jpg /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/193.jpg && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Archive page image"
}
```


### [2026-09-06T02:31:32.577Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T02:31:50.525Z] AGENT

Page 193 verified. `verify_check.py 193` → **0 PROBLEM lines**, 13/13 nodes.

**Verdicts:** roots 2 confirmed (Gheugh/Ghŭgh, Ghlâd); nodes 10 confirmed, 3 plausible, 0 disputed, 0 transcription_suspect.
Ref checks: 17 supports, 3 partial, 2 contradicts, 1 not_found, 1 not_checked. 22 different books consulted (38 entries).

**The three `plausible` nodes:**
- **Gheugh #1 Old Persian `gaud / â-gaud / apa-gaudaya`** — root and arrow fine, but two errors in the box, both present on the printed page (extraction is faithful; image archived to `data/verification/sources/refs/ocr/BOOK/193.jpg`): (a) `apa-gaudaya` is glossed "to uncover", whereas Kent p.182b ("conceal, hide away"), Buck p.852 ("mā apagaudaya 'do not hide'") and Bartholomae col. 526 ("verbergen, verheimlichen") — all Nourai's own citations — say the opposite; (b) `â-gaud` is not an attested Old Persian form (Av. ā-guz-, and *ā-gaud- is the Sogdian etymon copied back into the OP box).
- **Gheugh #3 Persian آغل** — the Sogdian route is one of two live etymologies; Wiktionary gives it first but offers Turkic ağıl / Old Turkic aɣɨl as the alternative, which explains the -l that Sogdian ʾγwd cannot. Mo'in (MON:68), Nourai's own ref, prints the entry with **no** origin tag.
- **Ghlâd #4 Arabic zard/sarad/zarrâd** — words and glosses all right, but the arrow is drawn from the IE root as a sister of Avestan; Jeffery (FVQ 169 = VDQ:257), Asbaghi PLA 142, Nyberg II 247 and Horn 660 all make Arabic زرد a pre-Islamic loan from MP zrēh via Syriac/Aramaic zardā, i.e. it should hang from node #2.

**Reference notes:** `SOD:50` on the Old Persian node is a stray — Gharib is Sogdian-only, and the material Nourai uses is at entries 78 and 107 (≈ pp. 3 and 5), his other citation. `VDQ:257` was checked through Jeffery's English original (FVQ p.169), of which VDQ is the Persian translation. `HRN:146`, `BQT:1019` (vol. 2 leaf 480, Mo'in's footnote 1 on زره), `MON:1729`, `KNT:182`, `SYN:852`, `POK:450/451/439` all located and quoted.

**For the owner (extraction, minor):** the printed chart of entry 0 has an **empty box** hanging off the Avestan node (top right of the first tree, no language label, no words); `data/extracted/batch/page-193.json` drops it. Everything else on the page matches the print exactly, including the erroneous "to uncover" gloss.
