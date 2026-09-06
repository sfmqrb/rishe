# Verification process log — verify-page-230


## [2026-09-06T15:26:47.742Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 230 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-230.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-230.json. Write /home/sfmqrb/git/rishe/data/verification/page-230.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 230` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:26:49.139Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:26:50.008Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:26:50.023Z] TOOL RESULT

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


## [2026-09-06T15:26:50.542Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-230.txt"
}
```


### [2026-09-06T15:26:50.555Z] TOOL RESULT

```
1	=== PDF page 230 (book page 200) ===
2	--- entry 0 ---
3	ROOT [Aramaic] J.b.r; Jabra : to reunite, join together, force; powerful, man  (refs KLN:633; SOR:41)
4	#1 (parent #0) [Arabic] refs=KLN:633; FVA:67 | J.b.r : to reunite, force ; Al-Jabr-w'al-Moqâbalah : "Reunion and Comparison", title of the first book on Algebra. It was written in Arabic by Al-Khârazmî, the ninth century Iranian mathematician. ☞Ghdhem
5	  #2 (parent #1) [Persian] refs=FVA:67 | jabr «جَبر» : force, algebra ; jabarût «جَبَروت» : mightiness, celestial kingdom ; jobrân «جُبران» : compensation | extra: جبّار ، اجبار ، مجبور | NOTE: "Jobrân" is does not exist in Arabic.
6	  #3 (parent #1) [French] refs=PHN:26 | algebre
7	    #4 (parent #3) [English] refs=KLN:48 | algebra
8	#5 (parent #0) [Persian] refs=MON:3193; SOR:41 | gabr «گَبر» : man, referred to Zoroastrians, a non-believer (in Islam) | extra: گبرک ، گبرکان ، گبرکی | NOTE: BQT:1774 does not agree with this derivation.
9	#6 (parent #0) [Hebrew] refs=KLN:633 | gabhar : was strong, man ; Gabhri-ěl : "man of God", Gabriel ☞Layh
10	  #7 (parent #6) [Arabic] refs=None | Jebraîl : Gabriel
11	    #8 (parent #7) [Persian] refs=MON:1215 | Jebreîl «جبرئیل» : Gabriel (man of God)
12	  #9 (parent #6) [Latin] refs=None | 
13	    #10 (parent #9) [French] refs=None | 
14	      #11 (parent #10) [Persian] refs=MON | Gâbrîyel «گابریل» : "man of God", a male name
15	    #12 (parent #9) [English] refs=KLN:633 | Gabriel
16	--- entry 1 ---
17	ROOT Jol -> redirect to Ul
18	--- entry 2 ---
19	ROOT Jor -> redirect to Ul
20	--- entry 3 ---
21	ROOT Jur -> redirect to Ul
22	
```


## [2026-09-06T15:26:53.883Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-230.json",
 "description": "Read source JSON for page 230"
}
```


### [2026-09-06T15:26:53.917Z] TOOL RESULT

```
{
  "pdf_page": 230,
  "book_page": 200,
  "entries": [
    {
      "root": {
        "name": "J.b.r; Jabra",
        "lang": "Aramaic",
        "refs": "KLN:633; SOR:41",
        "gloss": "to reunite, join together, force; powerful, man"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:633; FVA:67",
          "words": [
            {"translit": "J.b.r", "gloss": "to reunite, force", "script": null},
            {"translit": "Al-Jabr-w'al-Moqâbalah", "gloss": "\"Reunion and Comparison\", title of the first book on Algebra. It was written in Arabic by Al-Khârazmî, the ninth century Iranian mathematician.", "script": null, "see": ["Ghdhem"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:67",
          "words": [
            {"translit": "jabr", "gloss": "force, algebra", "script": "جَبر"},
            {"translit": "jabarût", "gloss": "mightiness, celestial kingdom", "script": "جَبَروت"},
            {"translit": "jobrân", "gloss": "compensation", "script": "جُبران"}
          ],
          "script_extra": "جبّار ، اجبار ، مجبور",
          "note": "\"Jobrân\" is does not exist in Arabic.",
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "French",
          "refs": "PHN:26",
          "words": [
            {"translit": "algebre", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "KLN:48",
          "words": [
            {"translit": "algebra", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:3193; SOR:41",
          "words": [
            {"translit": "gabr", "gloss": "man, referred to Zoroastrians, a non-believer (in Islam)", "script": "گَبر"}
          ],
          "script_extra": "گبرک ، گبرکان ، گبرکی",
          "note": "BQT:1774 does not agree with this derivation.",
          "quote": {"text": "تو مرد دینی و این رسم گبرانست - روا نداری بر دین گبرکان رفتن", "poet": "Onsorî"}
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:633",
          "words": [
            {"translit": "gabhar", "gloss": "was strong, man", "script": null},
            {"translit": "Gabhri-ěl", "gloss": "\"man of God\", Gabriel", "script": null, "see": ["Layh"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Arabic",
          "refs": null,
          "words": [
            {"translit": "Jebraîl", "gloss": "Gabriel", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON:1215",
          "words": [
            {"translit": "Jebreîl", "gloss": "Gabriel (man of God)", "script": "جبرئیل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 6,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "Gâbrîyel", "gloss": "\"man of God\", a male name", "script": "گابریل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 9,
          "lang": "English",
          "refs": "KLN:633",
          "words": [
            {"translit": "Gabriel", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Jol", "redirect": "Ul"},
      "nodes": []
    },
    {
      "root": {"name": "Jor", "redirect": "Ul"},
      "nodes": []
    },
    {
      "root": {"name": "Jur", "redirect": "Ul"},
      "nodes": []
    }
  ]
}
```


## [2026-09-06T15:26:55.870Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['KLN','SOR','FVA','PHN','MON','BQT','AFM','PLA','FVQ','LKT','SKT','WEB','FSD','ARY','HRN','HUB','PHD','NYB']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-06T15:26:57.730Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SOR {"title": "K. Akhavan Zanjani — title unknown (Table IV entry for SOR lost in OCR; listed under Persian authors)", "kind": "none", "url": null, "lookup_hint": "Author search on archive.org/web found nothing.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online; title unidentified."}

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
```


## [2026-09-06T15:27:02.781Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && ls && echo ---- && head -60 sources/SOURCE_MATRIX.md && echo ---- && ls sources/refs | head -80"
}
```


### [2026-09-06T15:27:02.831Z] TOOL RESULT

```
agent
page-100.json
page-101.json
page-102.json
page-103.json
page-104.json
page-105.json
page-106.json
page-107.json
page-108.json
page-109.json
page-110.json
page-111.json
page-112.json
page-113.json
page-114.json
page-115.json
page-116.json
page-117.json
page-118.json
page-119.json
page-120.json
page-121.json
page-123.json
page-124.json
page-125.json
page-126.json
page-127.json
page-128.json
page-129.json
page-130.json
page-131.json
page-132.json
page-133.json
page-134.json
page-135.json
page-136.json
page-137.json
page-138.json
page-139.json
page-140.json
page-141.json
page-142.json
page-143.json
page-144.json
page-145.json
page-146.json
page-147.json
page-148.json
page-149.json
page-150.json
page-151.json
page-152.json
page-153.json
page-154.json
page-155.json
page-156.json
page-157.json
page-158.json
page-159.json
page-160.json
page-161.json
page-162.json
page-163.json
page-164.json
page-165.json
page-166.json
page-167.json
page-168.json
page-169.json
page-170.json
page-171.json
page-172.json
page-173.json
page-174.json
page-175.json
page-176.json
page-177.json
page-178.json
page-179.json
page-180.json
page-181.json
page-182.json
page-183.json
page-184.json
page-185.json
page-186.json
page-187.json
page-188.json
page-189.json
page-190.json
page-191.json
page-192.json
page-193.json
page-194.json
page-195.json
page-196.json
page-197.json
page-198.json
page-199.json
page-200.json
page-201.json
page-202.json
page-203.json
page-204.json
page-205.json
page-206.json
page-207.json
page-208.json
page-209.json
page-210.json
page-211.json
page-212.json
page-213.json
page-214.json
page-215.json
page-219.json
page-220.json
page-222.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
page-36.json
page-37.json
page-38.json
page-39.json
page-40.json
page-41.json
page-42.json
page-43.json
page-44.json
page-45.json
page-46.json
page-47.json
page-48.json
page-49.json
page-50.json
page-51.json
page-52.json
page-53.json
page-54.json
page-55.json
page-56.json
page-57.json
page-58.json
page-59.json
page-60.json
page-61.json
page-62.json
page-63.json
page-64.json
page-65.json
page-66.json
page-67.json
page-68.json
page-69.json
page-70.json
page-71.json
page-72.json
page-73.json
page-74.json
page-75.json
page-76.json
page-77.json
page-78.json
page-79.json
page-80.json
page-81.json
page-82.json
page-83.json
page-84.json
page-85.json
page-86.json
page-87.json
page-88.json
page-89.json
page-90.json
page-91.json
page-92.json
page-93.json
page-94.json
page-95.json
page-96.json
page-97.json
page-98.json
page-99.json
process
sources
----
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
----
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
```


## [2026-09-06T15:27:03.501Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && python3 -c \"\nimport json\nd=json.load(open('page-202.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\n\""
}
```


### [2026-09-06T15:27:05.139Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Gwa, Gwâ, Gwen 2",
 "verdict": "confirmed",
 "modern_form": "PIE *gʷem- 'to go, to come' (with the collateral root *gʷeh₂- / *gʷā- 'to step, go'); Pokorny IEW 463-465",
 "note": "Pokorny's entry, which begins on p.463 exactly as Nourai cites, is headed 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“', and it is deliberately a double entry (I. gʷā-, II. gʷem-), which is why Nourai's box carries two names, 'Gwa, Gwâ'. His third name 'Gwen 2' reflects the *gʷem- > *gʷen- variant Pokorny himself notes ('Unthematisch *(e)-gʷem-t (> *e-gʷen-t)', and Latin advenam / veniō with -n- for -m-); it is not a separate root in any modern handbook, so it is Nourai's own labelling convenience rather than an error of substance. Watkins/AHD 1985 heads the same material 'gʷā-. Also gʷem-. To go, come'; Cheung splits it into *gaH¹ (PIE *gʷeh₂-, Pok. 463 f.) and *gam¹ (PIE *gʷem-, Pok. 464 f.). The gloss 'to walk, to step, to come, to go' is an accurate rendering. Two words in the chart do not belong to this root: Avestan 'gâv' in node 6 (a misprint) and 'thamân' in node 12 (an unidentifiable form), and one Persian word, nîyâm (node 3), is derived by modern scholarship from a different root (*ni-dā-, not *ni-gam-). Everything else on the page is standard, well-attested Iranian etymology.",
 "note_fa": "جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۶۳ فرهنگ خود مدخل «gʷā-, gʷem-» را با معنای «رفتن، آمدن؛ به جهان آمدن، زاده شدن» آورده و همان‌جا نام‌های gʷm̥-ti-s و gʷem-tu-s «گام، رفتار» را می‌افزاید؛ پس هر دو صورت «Gwa/Gwâ» و «Gwem» از یک مدخل‌اند و برچسب «هندواروپایی» و معنای «راه رفتن، گام برداشتن، آمدن، رفتن» درست است. نام سوم «Gwen 2» گونهٔ *gʷen- است که خود پوکورنی (در *e-gʷen-t و در veniō لاتین) یاد کرده و در کتاب‌های امروزی ریشهٔ جداگانه‌ای به شمار نمی‌رود؛ این نام‌گذاری از خود نورایی است نه خطای علمی. واتکینز (پیوست AHD) نیز همین ماده را «gʷā-, also gʷem-: رفتن، آمدن» آورده و چونگ آن را به دو ریشهٔ *gaH¹ و *gam¹ بخش کرده است. در سراسر این صفحه تنها سه لغزش هست: صورت «gâv» در گرهٔ ۶ (غلط چاپی)، صورت «thamân» در گرهٔ ۱۲ (صورتی که در هیچ فرهنگی یافت نشد) و واژهٔ «نیام» در گرهٔ ۳ که پژوهش امروزی آن را از ریشهٔ دیگری (*ni-dā-) می‌داند.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷem-"
 ],
 "ref_check": [
  {
   "ref": "POK:463",
   "status": "supports",
   "note": "POK_02.txt line 1790 (the leaf whose running numbers are 463-465): 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“, Verbaladjektiv gʷm̥-to-s. I. gʷā-: ... 2. gʷem-: ...'. The same pages carry 'av. gātu-s „Ort, Liegerstatt, Sessel, Thron“, apers. gāθu- ds.', 'av. gā-man- n. „Schritt“', 'av. jantu (*gʷem-tu-)' and 'av. jasaiti „er geht“' — i.e. Pokorny 463 alone underwrites the root box and nodes 1, 2 and 6."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I 675-677 (WLD_Bd1 djvu line 42665 ff., running head 'gʷem-, gʷā-'
```


## [2026-09-06T15:27:09.495Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nprint(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['PHN'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-06T15:27:11.708Z] TOOL RESULT

```
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
{
 "title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866",
 "edition_found": "1866",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/dictionnairetym01pihagoog",
 "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt",
 "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.",
 "notes": "Built from djvu.xml."
}
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


## [2026-09-06T15:27:19.029Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^algebra\" KLN_1966.txt | head; echo ---; grep -n \"^Gabriel\" KLN_1966.txt | head; echo ---; grep -n \"^gaber\\|^gabbro\\|^gaby\" KLN_1966.txt|head"
}
```


### [2026-09-06T15:27:19.103Z] TOOL RESULT

```
484:algebra
2172:algebra,  n.  —  Fr.  Arab,  al-jabr  (in  vulgar  pro¬ nunciation  al-jebr),  ‘reunion  (of  broken  parts  in equations)’,  short  for  al-jabr  w‘ al-muqdbalah ,  ‘re¬ union  and  comparison’,  title  of  a  work  written by  Mohammed  ibn  Musa  al-Khowarizrru, great  mathematician  of  the  9th  cent.  The  title refers  to,  and  the  work  deals  with,  the  solution
2175:algebraist,  n.,  an  expert  in  algebra.  —  A  hybrid coined  fr.  algebra  and  -ist,  a  suff.  of  Greek
2177:algebraization,  n.,  reduction  of  algebraic  sym¬ bols  (philos.)  —  G.  Algebraisierung,  fr.  algebra- isieren,  a  hybrid  coined  by  Edmund  Husserl (1859-1938)  fr.  algebra  and  suff.  -isieren,  fr.
---
15637:Gabriel,  1)  masc.  PN. ;  2)  in  the  Bible,  name  of  an angel.  —  Heb.  GabhrVil,  lit.  ‘man  of  God’,  fr.
---
15633:gaberdine,  gabardine,  n.,  a  long,  loose  gown; specif,  a  gown  worn  esp.  by  Jews  in  the  Middle Ages.  —  Sp.  gabardirta,  lit.  ‘pilgrims  frock’,  fr. MHG.  wallevart  (G.  Wallfahrt),  ‘pilgrimage’, which  is  compounded  of  MHG.  wallen  (fr. OHG.  wallon),  ‘to  roam,  wander’,  and  OHG., MHG.  vart,  ‘journey’,  fr.  OHG.  faran,  ‘to  go’. The  first  element  is  rel.  to  OE.  weallian,  ‘to wander’,  OHG.  wadal,  wadot,  MLG.  wadel,  OE. wadol,  ‘full  moon’,  and  prob.  also  to  OHG. wadal,  MHG.  wadel,  wedel,  G.  Wedel,  ‘tail, duster,  fan’.  For  the  second  element  see  fare,  v. gabion,  n.,  a  basket  of  wickerwork.  —  F.,  fr.  It. gabbione,  augment,  of  gabbia,  fr.  L.  cavea,  ‘an excavated  place,  cavity,  cage’.  See  cage. Derivatives:  gabion,  tr.  v.,  gabion-ed,  adj. gabionade,  n.,  embankment  made  with  gabions (fort.)  —  F.  gabionnade,  fr.  gabionner,  ‘to  cover with  gabions’,  fr.  gabion.  See  prec.  word and  -ade.
15639:gaby,  n.,  a  foolish  person.  —  Prob.  related  to gape  and  assimilated  in  form  to  baby, gad,  interj.  —  Used  as  a  var.  of  God.
```


## [2026-09-06T15:27:19.312Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ALGEBRE\\|ALGÈBRE\\|Algebre\" PHN.txt | head"
}
```


### [2026-09-06T15:27:19.362Z] TOOL RESULT

```
1346:ALGÈBRE, 8. f. (a.)
```


## [2026-09-06T15:27:24.101Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15637,15640p' KLN_1966.txt; echo \"=== leafcheck\"; python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\n# find leaf containing 'Gabriel,  1)'\nfor i,l in enumerate(leaves):\n    if 'Gabriel,  1)' in l or 'Gabriel, 1)' in l:\n        print('gabriel leaf',i)\n    if 'algebra,  n.' in l:\n        print('algebra leaf',i)\nEOF"
}
```


## [2026-09-06T15:27:24.661Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1340,1360p' PHN.txt"
}
```


### [2026-09-06T15:27:25.837Z] TOOL RESULT

```
Gabriel,  1)  masc.  PN. ;  2)  in  the  Bible,  name  of  an angel.  —  Heb.  GabhrVil,  lit.  ‘man  of  God’,  fr.
gebher,  ‘man’,  and  El,  ‘God’.  Heb.  gebher derives  from  the  base  of  the  verb  gdbhar,  ‘was strong’,  whence  also  gibbdr,  ‘strong,  mighty; hero’,  glbhtr,  ‘lord’,  g(bhirdh,  gebhereth,  ‘lady, queen’,  gebhurdn,  ‘strength,  might’.  Cp.  the related  words:  Aram. -Syr. glbhar, ‘was  mighty’, gebhar,  gabhrd,  ‘man’,  Syr.  gabbdr,  ‘hero’, Arab,  jabr,  ‘a  strong,  young  man’,  jabbdr, ‘tyrant’,  Akkad,  gapru,  ‘strong’,  Ethiop.  gabara, ‘he  acted’.  For  the  first  element  cp.  gibbar,  for the  second  see  El.
gaby,  n.,  a  foolish  person.  —  Prob.  related  to gape  and  assimilated  in  form  to  baby, gad,  interj.  —  Used  as  a  var.  of  God.
Gad,  n.,  in  the  Bible:  1)  son  of  Jacob  and  Zilpah; 2)  the  tribe  descended  from  him.  —  Heb.  Gddh, fr.  gddh,  ‘fortune’,  which  is  rel.  to  Aram.-Syr. gaddd,  Arab,  jadd,  of  s.m.  See  the  explanation of  the  name  in  Gen.  30:11. gad,  intr.  v.,  to  rove  about.  —  Perh.  back  forma¬ tion  fr.  obsol.  gadling,  ‘companion’,  fr.  ME. gadeling,  fr.  OE.  gte deling.  See  gather, gad,  n.,  a  bar,  rod.  —  ME.  gad,  gadd,  ‘a  goad’, fr.  ON.  gaddr,  ‘spike,  sting,  nail’.  See  yard, ‘unit  of  length’,  and  cp.  gadfly, gaddi,  guddy,  guddee,  n.,  a  cushion  serving  as  a throne,  a  throne  (India).  —  Hind,  gaddi. gadfly,  n.  —  Lit.  ‘a  goading  fly’,  compounded  of gad,  ‘bar’,  and  fly,  n.
=== leafcheck
algebra leaf 37
gabriel leaf 342
```


### [2026-09-06T15:27:25.868Z] TOOL RESULT

```
(jiiadiana, au sud et à l'ouest par l'océan Atlantique. Elle pro-
duit en abondance des figues, des dattes, des citrons, des
oranges, des olives, et surtout d'excellent vin. Les Maures, qui
étaient parvenus à s'enij»arer de cette province au viiT siècleÎ26 A'LG
de notre ère, en furent chassés par Alphonse III, roi de Por-
tu{[al, en 1200.
ALGÈBRE, 8. f. (a.)
yt^ [aldjebr^ la réunion de pitisieurs parties en u$i seul corps, ou
l'action de ramener les fractions à un nombre intégral. Le verbe
radical arabe J4s^ [{^'oiar] signifie proprement consolider les
différentes parties d'une chose brisée, par exemple, d'un os, —
On voit, d'après ce qui vient d'être dit, que le mot algèbre
est employé figurément pour désigner l'art de représenter,
par des signes et des lettres, des opérations différentes, dont
chacune peut demander un assez grand nombre de chiffres
en arithmétique. — ^ Les Arabes appellent aussi cette science
ikXA'JL^W^jxÂ. ^aldjebr wa-lmouqâbalat] le rétablissement et la
comparaison.
ALGER, n. pr. (a.)
jS\yÂ [aldjézâlr] les îles, pluriel de ^j^^y^r [djézirat]. Ville cé-
lèbre de l'Afrique septentrionale et capitale de l'Algérie, sur
```


## [2026-09-06T15:27:34.803Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np='KLN_1966.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (36,37,341,342,343):\n    l=leaves[i]\n    print('--- leaf',i,'---')\n    print(l[:200].replace('\\n',' | '))\n    print('...END:', l[-200:].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-06T15:27:36.612Z] TOOL RESULT

```
--- leaf 36 ---
trength,  power’.  See  Alexander, alcohol,  n.  —  ML.,  fr.  Arab,  al-kohl ,  vulgar  pro¬ nunciation  of  al-kuhl,  fr.  a/-,  the  ,  and  kohl, resp.  kuhl,  ‘antimony  (used  for  painting  the
...END: d  (med.)  —  Medical  L., formed  fr.  priv.  pref.  a-  and  Gk.  ‘speech’, from  the  stem  of  XsyEiv,  to  tell,  say,  speak’ (see  lexicon),  but  confused  in  meaning  with  L. legere,  ‘to  
--- leaf 37 ---
read’.  For  the  ending  see  suff.  -ia. alexin,  n.,  a  substance  which  destroys  bacteria (immunology).  — Coined  by  the  German  bacteri¬ ologist  Hans  Buchner  (1850-1902)  in  1888,  fr. 
...END: cp.  Alison. | Alice  blue.  —  Named  after  Mrs.  Alice  Roosevelt, wife  of  President  Theodore  Roosevelt, alicula,  n.  a  short  cloak  (Rom.  antiq.)  —  L.  ‘a light  upper  garment’,  a  dimin
--- leaf 341 ---
ulum,  short  for  L. infundibulum,  ‘funnel’,  lit.  ‘instrument  for  pour¬ ing  into’,  fr.  infundere,  ‘to  pour  into’,  fr.  in-, 'in',  and  fundere,  'to  pour'.  See  found,  ‘to  cast’, and
...END: lity,  n.  —  F.  fusibilite,  fr.  fusible.  See  next word  and  -ity. | fusible,  adj.,  that  which  can  be  fused.  —  F„  fr. L.  fusus,  pp.  of  fundere,  ‘to  pour’.  See  fuse,  ‘to melt’,  a
--- leaf 342 ---
nd  -ible. | Derivatives:  fusible-ness,  n.,fusibl-y,  adv. fusiform,  adj.,  spindle-shaped.  —  Compounded of  L.  fiisus,  ‘spindle’,  and  forma,  ‘form,  shape’. See  fuse,  ‘tube’,  and  form,  n
...END:   a  kind  of  fluting ; a  notched  molding.  —  F.  godron,  ‘gadroon’, orig.  written  goderon,  formed  with  dimin.  suff. -eron,  fr.  godet,  ‘bowl,  cup,  mug;  fold,  crease’, which  derives 
--- leaf 343 ---
 fr.  MDu.  codde, ‘cylindriform  piece | Gadus | Galinsoga | of  wood’.  For  change  of  meaning  cp.  G.  Hum- pen,  ‘piece  of  wood’,  later  used  in  the  sense  of ‘goblet,  hanap’. | Gadus,  n„  the 
...END: gelilah. galimatias,  n.,  jargon.  —  F.,  ‘nonsense,  gibberish  , prob.  a  deformation  of  Late  L.  balhmathia,  in¬ decent  songs'.  For  the  etymology  of  this  latter word  see  Du  Cange,
```


## [2026-09-06T15:27:54.653Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor i in (327,328,329,330):\n    print('--- leaf',i,':', leaves[i][:120].replace('\\n',' | '), '||', leaves[i][-120:].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-06T15:27:56.299Z] TOOL RESULT

```
903
--- leaf 327 : ret, fleur-de-lis,  flirt,  Flora,  flora,  floral,  Floreal, Florence,  Florentine,  florescent,  floret,  florid, flor || —  ME.  flege,  flie, fr.  OE.  fleoge,  flyge,  rel.  to  OS.  fliega,  ON., Swed.  fluga,  Norw.  fljuge,  earlier  Da
--- leaf 328 : n.  fluge, Dan  .flue,  MDu.  vlieghe,  Du.  vlieg,  OHG  .flioga, fliuga,  MHG.  vliuge,  vliege,  G.  Fliege,  ‘fly’,  || .  fealdan,  rel.  to  ON.  falda, Dan.  folde,  Swed.  falla,  MLG.  volden,  MDu. vouden,  Du.  vouwen,  OHG.  faldan 
--- leaf 329 : ,  MHG.  val- den,  valten,  G.  fatten,  Goth,  falpan,  and  cogn. with  OI.  putah,  ‘fold,  pocket’,  Alb.  pal'e,   || asture, repast.  —  Related,  and  equivalent  in  meaning, to  I.-E.  base  *pa-,  is  base  *po-,  *poi-,  *pl-, whenc
--- leaf 330 : e  Ol.  pdti,  ‘he  guards,  protects’,  go-pdh, ‘shepherd’,  payuh,  ‘guarding,  protecting’,  Gk. 7KHp.f]v,  ‘shepherd || a,  ‘beyond’,  pra-,  ‘before,  for¬ ward,  forth’,  Hitt,  para-,  ‘on,  forth’,  Gk.  nipoq, ‘before’,  7rapa,  ‘from
```


## [2026-09-06T15:28:10.746Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1971.txt',encoding='utf-8',errors='replace').read()\nn=len(t)\nimport re\nfor w in ['Gabriel,','algebra,','gabhar','gebher']:\n    i=t.find(w)\n    print(w, i, round(i/n*100,2),'%')\nprint('total chars',n, 'formfeeds', t.count('\\f'))\nEOF"
}
```


### [2026-09-06T15:28:12.605Z] TOOL RESULT

```
Gabriel, 2835134 28.85 %
algebra, 308876 3.14 %
gabhar -1 -0.0 %
gebher 3553174 36.15 %
total chars 9828418 formfeeds 0
```


## [2026-09-06T15:28:32.661Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'cherub,' in l: print('cherub leaf',i)\n    if 'jabbar' in l.lower() or 'jabr' in l.lower(): print('jabr leaf',i, [x for x in l.split('\\n') if 'jab' in x.lower()][:2])\nEOF"
}
```


### [2026-09-06T15:28:34.877Z] TOOL RESULT

```
jabr leaf 37 ['algebra,  n.  —  Fr.  Arab,  al-jabr  (in  vulgar  pro¬ nunciation  al-jebr),  ‘reunion  (of  broken  parts  in equations)’,  short  for  al-jabr  w‘ al-muqdbalah ,  ‘re¬ union  and  comparison’,  title  of  a  work  written by  Mohammed  ibn  Musa  al-Khowarizrru, great  mathematician  of  the  9th  cent.  The  title refers  to,  and  the  work  deals  with,  the  solution', "of  equations,  which  was  the  original  scope  of algebra.  Al-jabr  is  formed  fr.  al-,  ‘the’,  and  jahr, ‘reunion’,  which  is  rel.  to  the  s/crbja'bara,  ‘he bound  together,  united’.  Cp.  algorism."]
cherub leaf 98
cherub leaf 155
jabr leaf 342 ['gebher,  ‘man’,  and  El,  ‘God’.  Heb.  gebher derives  from  the  base  of  the  verb  gdbhar,  ‘was strong’,  whence  also  gibbdr,  ‘strong,  mighty; hero’,  glbhtr,  ‘lord’,  g(bhirdh,  gebhereth,  ‘lady, queen’,  gebhurdn,  ‘strength,  might’.  Cp.  the related  words:  Aram. -Syr. glbhar, ‘was  mighty’, gebhar,  gabhrd,  ‘man’,  Syr.  gabbdr,  ‘hero’, Arab,  jabr,  ‘a  strong,  young  man’,  jabbdr, ‘tyrant’,  Akkad,  gapru,  ‘strong’,  Ethiop.  gabara, ‘he  acted’.  For  the  first  element  cp.  gibbar,  for the  second  see  El.']
```


## [2026-09-06T15:29:55.128Z] AGENT

Now let me research. Starting with local reference greps.


## [2026-09-06T15:29:56.623Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ jibril/jabbar ===\"; grep -n -i \"jibril\\|Jibril\\|gabriel\\|jabbar\" FVQ_pages.txt | head -30"
}
```


### [2026-09-06T15:29:56.700Z] TOOL RESULT

```
=== FVQ jibril/jabbar ===
685:of Ishmael was a lost tongue but that Gabriel came and instructed Muhammad
1622:exegetes as to whether the one who called was Gabriel, standing at the
3846:Gabriel.
3859:Dan. viii, 16 ; ix, 21, Gabriel is one of the high angels and the agent
3861:possibility that the Gabriel of the QurVin is of Christian rather than
3866:before Muhammad's time. Gabriel was known and honoured among
3902:1 Tulail.ui, one of Muhammad's rival Prophets, claimed support from Gabriel (Tab,
9879:As an angel he is mentioned with Gabriel in a passage where the
9880:Commentators claim that the two are contrasted, Gabriel as the
```


## [2026-09-06T15:29:57.483Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HJB Gheber ===\"; grep -n -i \"gheber\\|guebre\\|gabr\\b\" HJB.txt | head -20; echo \"=== LKT ===\"; grep -n -i \"gauren\\|gueber\\|Algebra\\|guebre\" LKT.txt | head -20"
}
```


### [2026-09-06T15:29:57.550Z] TOOL RESULT

```
=== HJB Gheber ===
10746:GUBBEB,  s.  This  is  some  kind  of gold  ducat  or  sequin ;  Milburn  says 'a  Dutch  ducat.'  It  may  have  adopted this  special  meaning,  but  could  hardly have  neld  it  at  the  date  of  our  first quotation.  The  name  is  probably  gahr {dindr-i-gabr)y  implying  its  being  of infdel  origin.
18184:The  word  panchalt  literally  means  a  Council of  five,  but  that  of  the  Guebres  in  Bombay consists  of  thirteen  of  the  principal  mer- chants of  the  sect." — Maria  Graham,  41.
=== LKT ===
1579:bestimmte  Rechnungsart  sp.  pg.  älgebra, frz.  algkbre,  it.  algebra;  engl,  algebra, dtsch.  Algebra  usw.  —  In  der  ursprüng- lichen Bedeutung  des  ar.  Vbs.  gabara 'wiederherstellen,  einrichten'  ist  noch sp.  algebrista  'Chirurg'  [Dicc  Cast  121b; vgl.  ähnlich  engl,  bone-setter]  erhalten; pg.  algebrista,  algebista  'dass ',  algebra 'dessen  Kunst'  [Gonstancio  Dicc  50  c]. [DE  123.    Eguilaz  179.    ML  3941.
1580:632.  Pers.  gäbr: 'Feueranbeter'  [wohl  aus  ar.  käfir 'Ungläubiger',  s.  hier  Nr.  997,  nach RÜGKERT  in  ZDMG  X,  133];  erst  hier- aus [und  nicht  unmittelbar  aus  dem  ar. Grundwort]  tk.  gjawr,  gjaur,  womit  die Türken  jeden  Nichtmuslimen  bezeich- neten; hieraus  it.  giaurro,  frz.  engl. giaour,  dtsch.  Giaur ;  poln.  giaur.  Da- gegen frz.  guebre,  engl,  gueber,  guebre, dtsch.  Geber  'der  Feueranbeter  [Parsi]^ unmittelbar  aus  dem  pers.  Grundwort. [Devic  DEt  128  u.  134.
2144:"NTpr.,  eine  Landschaft  in  Mittelasien  [dem heutigen  Chanate  Ghiva-HIwa  entspre- chend]; davon  das  ar.  Adj.  hnärizmi  od. härizmi  'aus  Hwarizm  stammend,  der Gharizmier',  Beiname  des  Mathematikers ABÜ  GA'FAR  MUHAMMAD  IHN  MÜSÄ [s.  hier  Nr.  631];  durch  sein  Werk  über Algebra  kam  das  dekadische  Zahlensystem und  das  Rechnen  mit  ar.  Zahlen  um  das Jahr  1200  nach  Europa;  daher  wurde  lat. algorithmus,  algorismus  [mit  Anlehnung an  gr.  öpi&|ui6<;]  die  Bezeichnung  für  das Rechnen  mit  ar.  Ziffern  u.  schließlich  für Rechnungsverfahren  überhaupt.  Hieraus afrz.  algofisme,frz.  algorithme,it.alguaris- nio  'Rechenart,  Arithmetik',  sp.  alguaris- nio,  guarismo  'Ziffer',  engl,  algorism, algorithm  'Rechenart'.  [DE  130/131. WOEPGKE  in  JAs  (1863)  I,  519.  Devic DEt  18.  Lammens  Rem  13.  Schirmer WortschdMath  4/5.
4023:'Ding,  Sache';  so  bezeichneten  die  ara- bischen Mathematiker  die  Unbekannte [vgl.  die  Definition  bei  F.  Woepcke, L'algöbred'Omar  alkhayyäml.  Paris  1851. S.  4,  Z.  14/15]  und  verwandten  die  Ab- kürzung s,  die  von  den  Spaniern  durch X  wiedergegeben  wurde,  da  dieser  Buch- stabe im  älteren  Spanisch  so  aus- gesprofhen  wurde  [vgl.  Adolf  Zauner, Altspanisches  Elementarbuch.  ^.  Heidel- berg 19^1.  S.  4ö,  §  66];  daher  wird  die unbekannte  Größe  in  der  Algebra  mit X  bezeichnet  [Etymologie  von  DE  LA- GARDE;  neuerliche  Anzweifelung  ist lautlich  und  historisch  unberechtigt],  — Zu  ar.  saP  gehört  das  dem.  vulg.  suaije, suwaije;  hieraus  pg.  chuS,  xuS  'mager, schlecht  gekleidet'.  [DE  254/"i55.  Eguilaz 377.
5708:.4?awrtc  St.  75 Albatros  1)88 Alchabor  St.  12 Alchimie  1157 Aldebaran  St.  451 Aleppin  792 Algebar  St.  629 Algebra  631 Algedi  St.  035 Algenib  St.  664 Algomeiza  St.  749 ^Z^^oZ  St.  741 Algorab  St.  754 Alhabor  St.  12 Alhajoth  St.  41 Alhidade  896 Alizarin  116 Alkakandschi  1016 ^ZA-«?i  1029 ^/fro/io?  1227 Alkoran  1250 Alkoven  1221 ^/^«/t  59 Alleluja  793 alligaßr  mhd.  2229 Abnagest  1348 Almanach  1389 Almemor  j.  1461  a Alphard  St.  587 Alpherath  St.  586 Alpheraz  St.  586 Alpheta  St.  574 ^/<«/r  St.  1575
5916:algebra  631
6064:gueber  632
6065:guebre  632
7947:algebra  631
```


## [2026-09-06T15:30:05.314Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3835,3905p' FVQ_pages.txt"
}
```


### [2026-09-06T15:30:05.392Z] TOOL RESULT

```
Akkadische Fremdworter, 44. It is also the origin of tho Arm. //"*-(; cf. Hubsch-
mann, i, 302.
2 .^. itself is a foreign word according to al-Khafaji, 58. Vollers, ZDMG, li, 21)0,
says it is from yvi/ios.
3 Jawhari's clinching argument is that r and o do not occur as the first and
last radicals of any genuine Arabic word.100 FOREIGN VOCABULARY OF THE QITR^AN
This has been recognized by Dvorak, Fmndw, 50, and by
Noldeke, New Beitrage, 48, who shows that JtJP'Ah *7*fl1" #609
7rpoar(f)aTo$, and in ^*fl-|* we have the form we need.
(Jibnl).
ii, 91, 92 ; Ixvi, 4.
Gabriel.
Always as the Angel of Revelation, and by name only in Madinan
passages. (There is possibly a reference to his name ^X'HSS -
" mighty one of God ", in liii, 5, kk one mighty in power.")
There was considerable uncertainty among the early authorities
as to the spelling of the name, for we find
> % >
Ox-
and even ^^>- and ^^^J". 1 as-Suyuti, Minhir, i, 140.
notes that these variants point to its non-Arabic origin, 2 and this
was admitted by some of the philologers, cf. Tab. on ii, 91 ;
al-Jawallqi, 144, and al-Khafaji, GO.
The ultimate origin, of course, is the Heb. /N'HSS, and in
Dan. viii, 16 ; ix, 21, Gabriel is one of the high angels and the agent
of Kevelation, just as he is in the Qur'an. There is, however, the
possibility that the Gabriel of the QurVin is of Christian rather than
Jewish origin, and the form ^y-i^Xy which is found in the Christian
Palestinian dialect, 3 gives us the closest approximation to the usual
Arabic form.
There is some question how well the name was known in Arabia
before Muhammad's time. Gabriel was known and honoured among
the Mandaeans, 4 and this may have been a pre-Islamic element in
their faith. The name occurs also in verses of poets contemporary
with Islam, but seems there to have been influenced by Qur'anic
1 Vide al-Jawaliqi, Alu'arrab, /50, and Haiti, and Zain. on ii, 91.
* Sec also Ibn Qutaiba, Affab nl-Kiitib t 78.
3 Schulthoss, Lex, 34.
4 Brandt, Mandaer, 17, 25 ; JVdzharski, Johannefilmch, xxvi. Tt is interesting
to note that (Inbrall occurs in a Persian Manichaean fragment from Tnrfan ; cf. V.
Midler, MlAW, Berlin, 1904, ]>. 351, Salcnmnn, Manirhafi*c,he Mwtirn, i, 03.FOREKJN VOCABULARY OF THE QUR^AN 101
usage. Cheikho, Nasrdniya, 235, gives an instance of a personal name
containing the word, but Horovitz, KU, 107, rightly insists on the
incorrectness of this. 1 Muhammad seems to have been able to assume
in his Madinan audience some familiarity with the name, and the
probabilities are that it came to him in its Syr. form.
xxxvii, 103,
The temple, or side of forehead.
The sole occurrence of the Avord is in the story of Abraham pre-
paring to sacrifice his son, when he laid him down on his forehead. The
exegetes got the meaning right, but neither they nor the Lexicons
have any satisfactory explanation of the origin of the word from
a root
Barth has suggested an Aramaic origin. WSJ moans brow or
eyebrow, and is fairly common in the Rabbinic writings. Similarly
jla.CLt is eyebrow and a commonly used word. From either of these
it may have been an early borrowing into Arabic.
ix, 29.
Tribute.
The word is used ii, a technical sense in this passage which is late
Madinan, and looks very much like an interpolation in the Qur'iiu
reflecting later usage.
In later Islam < j>- was the technical term for the poll-tax imposed
on the Dhimmis, i.e. members of protected communities (cf. as-Sijistanl,
101). It is usually derived from (j>-, and said to be so called because
it is a compensation in place of the shedding of their blood (so llaghib,
Mnfraddt, 91; LA, xviii, 159). It is, however,' the Syr. ^^, a
1 Tulail.ui, one of Muhammad's rival Prophets, claimed support from Gabriel (Tab,
Annalt*, i, 1890, Beladhori, 90), but this may ha\c been in imitation of Muhammad,
though the weight of evidence seems to point to his having come forward quite
independently as a preacher of higher religion.102 FOEElCiN VOCABULARY OF THK QURAN
```


## [2026-09-06T15:30:05.589Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1574,1582p' LKT.txt"
}
```


### [2026-09-06T15:30:05.634Z] TOOL RESULT

```
629.  Ar.  gabbär:
'Riese' ;  hieraus  der  Sternname  Algebar, frz.  elgebar  'das  Sternbild  Orion'.
630.  Ar.  gäbija:
'Großer  Wasserbehälter'  [z.  B.  zum Tränken  von  Kamelen];  hieraus  siz. gebbia  'Teich,  Bassin'.   [GrSVociSic  238.
631.  Ar.  gabr: 'Wiederherstellung',  vollständig  ist  al- §abr  ivaH-mukabala  der  Titel  eines  al- gebraischen Lehrbuches  von  MUHAM- MAD IBN  MÜSÄ  AL  HWARIZMl,  um 820  n.  Chr.  geschrieben  [s.  auch  hier Nr.  890],  wörtlich:  'Wiederherstellung und  Gegenüberstellung  restauratio  et Opposition  worunter  man  die  Herstellung der  normalen  Gleichungsform  ohne  ne- gative Glieder  verstand  [Cantor,  Vor- lesungen über  Geschichte  der  Mathe- matik F,  719;  Schirmer  WortschdMath 3/4J.  Hieraus  als  Bezeichnung  für  eine
bestimmte  Rechnungsart  sp.  pg.  älgebra, frz.  algkbre,  it.  algebra;  engl,  algebra, dtsch.  Algebra  usw.  —  In  der  ursprüng- lichen Bedeutung  des  ar.  Vbs.  gabara 'wiederherstellen,  einrichten'  ist  noch sp.  algebrista  'Chirurg'  [Dicc  Cast  121b; vgl.  ähnlich  engl,  bone-setter]  erhalten; pg.  algebrista,  algebista  'dass ',  algebra 'dessen  Kunst'  [Gonstancio  Dicc  50  c]. [DE  123.    Eguilaz  179.    ML  3941.
632.  Pers.  gäbr: 'Feueranbeter'  [wohl  aus  ar.  käfir 'Ungläubiger',  s.  hier  Nr.  997,  nach RÜGKERT  in  ZDMG  X,  133];  erst  hier- aus [und  nicht  unmittelbar  aus  dem  ar. Grundwort]  tk.  gjawr,  gjaur,  womit  die Türken  jeden  Nichtmuslimen  bezeich- neten; hieraus  it.  giaurro,  frz.  engl. giaour,  dtsch.  Giaur ;  poln.  giaur.  Da- gegen frz.  guebre,  engl,  gueber,  guebre, dtsch.  Geber  'der  Feueranbeter  [Parsi]^ unmittelbar  aus  dem  pers.  Grundwort. [Devic  DEt  128  u.  134.
633.  Ar.  Gadänias:
N.  pr.,  eine  Stadt  in  TripoUs  (Nordafrika), dazu  das  Adj.  gadämasi  zur  Bezeichnung des  hier  hergestellten  Leders ;  hieraus sp.  pg.  guadameci,  pg.  guadamecim,  afrz. godemetin  'gepreßtes  oder  vergoldetes Leder';  sp.  gorromazos  'große  Reiter- stiefel' [weil  ursprünglich  aus  solchem Leder],  prov.  garamacha,  frz.  (dial.)  ga- ramaches  'dass.',  frz.  gamaches  [veraltet, jetzt  guetres]  'knöpf  bare  Überstrümpfe', dlsch.  Gamaschen.  —  [Ableitung  aus lat.  *gambacea  aus  gamba  'Bein'  erklärt nicht  alle  vorkommenden  Formen.  [DE 280/281.  Eguüaz  414.  Devic  DEt  124. ML  3751.
```


## [2026-09-06T15:30:14.317Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"pdf page 56[5-9]\\|pdf page 57[0-3]\" BQT_v3_pages.txt | head; echo \"=== search گبر ===\"; grep -n \"گبر\" BQT_v3_pages.txt | head -30"
}
```


### [2026-09-06T15:30:14.376Z] TOOL RESULT

```
41398:[pdf page 565]
41452:[pdf page 566]
41549:[pdf page 567]
41626:[pdf page 568]
41700:[pdf page 569]
41766:[pdf page 570]
41820:[pdf page 571]
41868:[pdf page 572]
41907:[pdf page 573]
=== search گبر ===
21096:گبران را یز ‎Vale‏
27472:انواع تیر#کاسنی است. ۲ - در رشیدی آمده : «گاهو » جنازه گبران . فردوس یگوید :
37393:است . پسآنجه صاحب ‎Oy‏ معبد گبران کفته خطای فاحشی است » « مقدمهٌ الجمن آرا در
```


## [2026-09-06T15:30:15.680Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== DEV guebre ===\"; grep -n -i \"guebre\\|gu.bre\\|giaour\" DEV.txt | head -20; echo \"=== DOZ ===\"; grep -n -i \"guebre\\|algebre\" DOZ.txt | head -10"
}
```


### [2026-09-06T15:30:15.746Z] TOOL RESULT

```
=== DEV guebre ===
1415:GiAouR.  Mot  par  lequel  les  Turcs  désignent  quiconcpio n'est  pas  musulman.  Le  mot^i^,  prononcé  par  les  Turcs ghaoïir,  est  persan;  sa  vraie  prononciation  est  gawr,  et c'est  une  autre  forme  du  terme  yj^  gliohr,  adorateur  (bi feu,  guèbre.
1462:GuÈBRE.  Adorateur  du  feu.  Du  persan  ^a^  ghebr,  même
2043:Sadder.  Livre  religieux  des  Parsis  ou  Guèbres.  Du persan  )^  J^-o  sad-der,  les  cent  portes,  de  sad,  cent,  et  der, porte,  chapitre  du  Zendavesta.
3606:Guèbre.
5081:j^iS^mal.  voy.  Calambac. yS pers.  voy.  Giaour,  Guèbre. xSmal.  voy.  Gutte  (Gomme-). ^^  xSmal.  voy.  Gutta-percha. M\-Smal.  voy.  Gourame. i^\S mal.  voy.  Gourame. bjS mal.  voy.  Goura. •ySpers.  voy.  Téréniabin. jSpers.  voy.  Julep. <J^pers.  voy.  Julep, wj.^^5  wfl/.  voy.  Gambir.
=== DOZ ===
```


## [2026-09-06T15:30:19.900Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1460,1470p' DEV.txt"
}
```


### [2026-09-06T15:30:19.938Z] TOOL RESULT

```
13/1  DICTIONNAIRE  ÉTYMOLOGIQUE
pourrait  bien  cire  le  liéron.  On  voit  combien  il  est  diffi- rile  (le  se  démêler  dans  ce  fouillis  inextricable.
GuÈBRE.  Adorateur  du  feu.  Du  persan  ^a^  ghebr,  même
sens.
GuTTA-FERCHA.  Substance  gommo-résineuse  fournie  par un  arbre  de  l'arcliipel  Indien,  Ylsonandra  percha.  Les  nom- breux emplois  qu'en  fait  l'industrie  européenne  ne  datent guère  que  d'une  trentaine  d'années.  C'est  le  malais  ^.J»  a;6 gatah  pertcha ,  orthographié  di  Y i\n^msQ  guUa  percha.  Gâtait signifie  gomme ,  et  ^-S  pertcha  est  le  nom  de  l'ile  que  nous appelons  Sumatra,  et  aussi  celui  de  l'arbre  qui  produit la  gutta-percha.  En  ce  dernier  sens,  le  Dictionnaire  de l'abbé  Favre  termine  le  mot  par  un  »  Ji,  ^^-J»  pertchah.
GuTTE  (Gomme-).  Dans  gomme-gutte,  le  second  mot  n'est que  la  traduction  du  premier  :  en  malais  ^ji^  gatah  ou ghctah,  gomme,  baume,  le  même  qui  se  trouve  dans  gutta- percha.  C'est  l'orthographe  anglaise  qui  nous  a  fait  pro- noncer u  là  où  il  faudrait  dire  a  ou  è.
H
Habzéli,  Habalzelin  ou  HABELZELiN.Nom  dc  la  [)lante  ixi)- ^)e\éo  ixussi  souche t  comestible.  C'est  l'arabe  ^Jî  t-^i^-  habh  az- zelem,  graine  de  zelem.  Le  ^^  zeleni  est  ainsi  défini  par  Frey- tag  :  ^tNomen  plantœ  cujusdam  tam  floribus  quam  semine carentis.  Radicibus  sub  terra  grana  adhaerent  cxpansa, pulclira,  dulcia.w  Inutile  de  dire  que  cette  description, empruntée  au  Qamoiis,  est  inexacte  dans  sa  première  par- tie; car  le  zelem  ou  souchet  n'est  point  un  cry|)togame.
La  même  plante  est  nommée  par  Rauwolf  habelassis, habaziz  par  Porta,  hablxtziz  par  C.  Bauhin,  ou  gramim  (h-
DES  MOTS  D'ORIGINE  ORIENTALE.  135
Icctuni:  ce  (jui  rcprësenle  l'arabe  j..>j*îl4^  hahb  al-aziz, [jraiii  exquis  (pour  être  correct,  il  faudrait  mettre  l'ar- ticle devant  habh,  ou  le  supprimer  devant  'azïz.)
```


## [2026-09-06T15:30:20.379Z] TOOL CALL #23: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1774 --image 2>&1 | head -60"
}
```


### [2026-09-06T15:30:27.450Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1774.png
REF: BQT:1774  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 571  OCR-lang: fas

گبرکی )۱۷۷
وخفتان ۱ - وهم بمعنی مغ‌باش د که آش‌پرست گیست۹ * بفتح اول وثانی وسکونسین
است ۴ - ونم کیاهی نیزهت ماشذاجبیل که | بی‌نقطه وفوقانی, بممتی گیاهیباشد تلم وحنظل
آترا در خراسان از زیر زمين برمیآورندوبجهت را نی زگوبند . ویمعنی زهر مار هم‌آمده‌است.

و خورند ۱ .38 7 :

ی ما۷ مار اد
گبر کی؟ * باکاف بروزن‌نکیتیظرفی ۳۳ - بفتح اول وسکون ثانی ونون
باشد که شراب ور آن‌کنند ۰ بالف کشیده , بلفت زند وپازند بمعنی مرد باشد
جز؟ - بفتح اول وسکون نانی وازای ۱ که در مقابل زن است.
نقطه دار » هر چیز کنده و نوی و سطبر را کبه بفتح اول وئانی‌مشدد پروزن‌دیه.
کوبنده ۰ شِعهٌ حجام را گوبند که بدان حجامت کند . .
۱ -باین‌معنی« کبر»(ه م.) است. ۲ - باین‌معنی بعقیده1قای یورداآود ازلمت آرامی گرفته شده
همربشهّ«کافر» عربی‌وبهمان‌معنی» ودرتر کیه‌نیزه کور» کوبند. وآن‌اسلابه‌منی مطلقمشروبیرون‌از

دن‌است؛ولی‌درا بران‌اسلامی بزرنشتپان اطلاق‌شده ومعناً درین‌اسّممال‌نوعی امتخغاف بکاررفته‌است .
این کلمه با وجه اشتقافی که برخی از پارسیان هند دربن مورد کفته‌اند وآترا از ربشة 820۳2
هزوارش وبمعنی «مرد» دانته‌اند » هیچگونه ارتباطی ندارد . کلمهٌ « کی ر کث» نیز از همین لغت
مرکب ااست با «کك » تصفیر وتوهین و۸ کبرکی» با بای حاصل‌مصدر بمعنی دین زرتشتی بکاررفته
است . رك : مزدینا ص ۳۹۵ - ‎٩‏ ؛کردی 8126101۲ (بارمنی‌اطلاق شود) ؛کور 82۷7 (آتش
پرست) » 88۷17 (بروسی اطلاق شود) « ژابا ص۳۵۷ -

۴ - از : کب رکه ( زرتعتی ) (ه.م.) .ی (حاصل مصدر) » آین زرتعقی (ر4:ح۲)-
ونیز از :کبرك (زرتعتی) ۳ ی (نبت) » آنچه منوب بزرتشتیان باشد » ومخصوصاً ظرف ی که
شراب در آن‌کنند (چه زرتدتیان در ادوار اسلامی باده فروشی میکردند . رك : مزدیناص۷۹۹
بیعد) » بهن دومعنی :

دارم طمع ز جود توبك گبر کی شراب بفرست بنده را من از خوش معتکی
ورلیست کبر کی بفرست آنچه‌هت از آن ‏ هرج آید ازتو» آن نبود غیرکبر کی .
این پمین فربومدی «رشیدی» .

۴ - رشیدی این کلمهرا باکاف تازی ضبط کرده است وجهانگیری با کاف فارسی -

* - درفلان بیشه درختی هست سبز بی‌بلند وپهن(هول) وهرشاخی شکبز .

مولوی . مثنوی چاپ تیکلسن دفتر دوم ص۸۵۳؛ چاپ علاوالدوله ص۹۸۹

‎٩‏ - رشیدی وجهانگیری وفرهنک نظام این‌کلمه را در کاف تازی آورده اند , ومولف
برهان در هردوضبط کردد است » ولف در فهرست شاهنامه کیت ون وکبست۳251 3 هر
دو را آورده است » اما اسح کاف تازی است . ر4 :کبت * کبتو* کته *

‏۷ - عز. 8280)2(82 ( اغلب 8807 خوانده شود ) درپهلوی 13271 (مرد)«بونکر
ص۸۹ .ی

‏اب رک - بفتح اول وسوم , زرتشتی . ر4:گبر (ح ۲ همینءفحه ) .
```


## [2026-09-06T15:31:02.196Z] TOOL CALL #24: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T15:31:02.204Z] TOOL RESULT

```


```


## [2026-09-06T15:31:05.322Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/gabr",
 "prompt": "What is the etymology given for Persian gabr (Zoroastrian, infidel)? Does it come from Aramaic gabrā \"man\" or from Arabic kāfir? Quote the etymological discussion."
}
```


## [2026-09-06T15:31:06.732Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/algebra",
 "prompt": "Give the full etymology of English algebra: intermediate languages (Medieval Latin, Italian, French, Spanish), Arabic al-jabr, and the root j-b-r."
}
```


### [2026-09-06T15:31:06.965Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:31:13.689Z] TOOL RESULT

```
# Etymology of English Algebra

Based on the Wiktionary source, English *algebra* has a fascinating etymological journey:

## Direct Source
English borrowed the term from **Medieval Latin** *algebra*, which itself came from Arabic *الْجَبْر* (al-jabr), meaning "reunion, resetting of broken parts." This Arabic term appeared in al-Khwarizmi's influential mathematical treatise.

## Intermediate Languages
The etymology section traces the word through Romance languages before reaching English:

- **Italian**: *algebra* (derived from Latin)
- **French**: *algèbre* (evolved from the Latin form)
- **Spanish**: *álgebra* (following Romance language patterns)

These Romance language versions emerged from Medieval Latin's adoption of the Arabic term.

## Semantic Root
The Arabic root **j-b-r** (جَبَرَ) underlies *al-jabr*. The verbal noun form *الْجَبْر* literally described the concept of "reunion" or "restoration," which medieval mathematicians applied metaphorically to the algebraic process of balancing equations and reuniting separated quantities.

This etymological path—from Arabic mathematical terminology through Medieval Latin into the Romance languages and finally into English—reflects how mathematical knowledge traveled westward during the medieval period.
```


## [2026-09-06T15:31:17.770Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/algebra",
 "prompt": "Full etymology of algebra: route into English, Medieval Latin, Arabic al-jabr, al-Khwarizmi, and any mention of French or Italian."
}
```


## [2026-09-06T15:31:19.318Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D8%A8%D8%B1",
 "prompt": "Persian گبر (gabr): what etymology is given? Aramaic gabrā, Arabic kāfir, or something else? Quote it."
}
```


### [2026-09-06T15:31:24.250Z] TOOL RESULT

```
# Etymology of Algebra

**Route into English:**
The word "algebra" entered English in the 1550s from Medieval Latin *algebra*, which derived from Arabic.

**Arabic Origins:**
The term comes from the Arabic title *"al-mukhtasar fi hisab al-jabr wa al-muqabala"* ("the compendium on calculation by restoring and balancing"). The Arabic *al jabr* means "reunion of broken parts," referring to a computational technique for reducing fractions to integers.

**Key Figure:**
Al-Khwarizmi, a 9th-century Baghdad mathematician, authored the famous treatise that introduced this concept. His work was translated into Latin during the 12th century and significantly influenced Western mathematics by introducing Arabic numerals.

**Additional Language Influences:**
While the content doesn't mention French or Italian etymological contributions to "algebra" itself, it does note that the mathematician's name, *al-Khwarizmi*, later influenced the term "algorithm" through French *algorithme*.

**Historical Note:**
In 16th-century England, John Dee referred to algebraic work as *algiebar and almachabel*. The stress accent shifted from the second to the first syllable during the 17th century.
```


### [2026-09-06T15:31:24.945Z] TOOL RESULT

```
# Etymology of Persian گبر (gabr)

The word has **two etymologies**:

**Etymology 1:** From Proto-Indo-European *webʰ- ("weave"), used for "hauberk" (armor).

**Etymology 2:** Borrowed from Aramaic. The source states: "Borrowed from Aramaic 𐡂𐡁𐡓𐡀 (gbrʾ /⁠gaḇrā⁠/, 'man; person')."

However, the document notes an alternative theory was "traditionally" proposed but rejected: "Traditionally has been derived from Arabic كَافِر (kāfir, 'unbeliever'), but that is problematic on phonetic and semantic grounds."

The **Aramaic origin** is the accepted etymology presented in this source.
```


## [2026-09-06T15:31:31.698Z] TOOL CALL #29: WebSearch

```json
{
 "query": "Encyclopaedia Iranica \"GABR\" etymology Aramaic gabrā Zoroastrian \"kāfir\" Persian word"
}
```


## [2026-09-06T15:31:32.736Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D8%A8%D8%B1%D9%8A%D9%84",
 "prompt": "Arabic جبريل (Jibrīl) — etymology: from Hebrew, Syriac, Greek? Quote it."
}
```


### [2026-09-06T15:31:38.582Z] TOOL RESULT

```
# جبريل (Jibrīl) - Etymology

Based on the Wiktionary entry, the etymology section states: "Alteration of _جَبْرَائِيل_ (jabrāʔīl)."

However, the page does not provide information about the word's origins from Hebrew, Syriac, or Greek. The entry only indicates that the current Arabic form is an alteration of an earlier Arabic variant, without tracing the word back to those source languages. To find etymology details linking this term to Semitic or Greek origins, you would need to consult additional linguistic or religious resources beyond what appears on this Wiktionary page.
```


### [2026-09-06T15:31:40.772Z] TOOL RESULT

```
Web search results for query: "Encyclopaedia Iranica "GABR" etymology Aramaic gabrā Zoroastrian "kāfir" Persian word"

Links: [{"title":"GABR - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/gabr/"},{"title":"Shaki, Mansour - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/scholar/mansour-shaki/"},{"title":"گبر - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%DA%AF%D8%A8%D8%B1"},{"title":"Gabr — Brill","url":"https://referenceworks.brillonline.com/entries/encyclopaedia-of-islam-2/gabr-SIM_2413"},{"title":"Gabr","url":"https://en.wikipedia.org/wiki/Gabr"},{"title":"(PDF) In serach of giaour. Notes on the New Persian gabr ‘a zoroastrian; infidel’","url":"https://www.academia.edu/33609648/In_serach_of_giaour_Notes_on_the_New_Persian_gabr_a_zoroastrian_infidel_"},{"title":"Gabar | Persian Warriors, Pre-Islamic Religion | Britannica","url":"https://www.britannica.com/topic/Gabars"},{"title":"Religion:Gabr - HandWiki","url":"https://handwiki.org/wiki/Religion:Gabr"}]

Based on the search results, here's what the Encyclopaedia Iranica article on "GABR" contains regarding the etymology:

## Primary Etymology

The term "gabr" is a New Persian term deriving, in all likelihood, from Aramaic GBRʾ/gabrā (literally meaning "man"), which in the Sasanian period was used to indicate the free peasants in the region of Mesopotamia.

## Alternative Etymology (Arabic kāfir)

The article discusses but rejects an alternative theory. Some scholars, notably Ebrāhīm Pūr-e Dāwūd, have suggested the etymology is based on the supposed mispronunciation of the Arabic kāfer (unbeliever) by the Persians in the early Islamic period. However, although Persians still fail to articulate some Arabic speech sounds properly, there is no unusual sound in kāfer that would require phonetic modification.

## Semantic Evolution

With the dwindling of the Zoroastrian community because of frequent proselytizations and the curtailment of their social rights, the term came to have a pejorative implication, which is the reason for its commutation to the respectable zardoštī (Zoroastrian) in recent times.

The Encyclopaedia Iranica thus favors the Aramaic etymology over the Arabic kāfir derivation on linguistic grounds.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T15:31:50.009Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D8%A8%D8%B1%D8%A7%D8%A6%D9%8A%D9%84",
 "prompt": "Arabic جبرائيل — etymology: from which language (Hebrew, Syriac/Aramaic, Greek)? Quote it."
}
```


## [2026-09-06T15:31:52.678Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%92%D6%B7%D7%91%D6%B0%D7%A8%D6%B4%D7%99%D7%90%D6%B5%D7%9C",
 "prompt": "Hebrew גַּבְרִיאֵל Gavri'el: etymology — components גֶּבֶר gever \"man\" and אֵל El \"God\"; root ג-ב-ר. Quote it."
}
```


### [2026-09-06T15:31:54.203Z] TOOL RESULT

```
# Etymology of جبرائيل

According to the Wiktionary entry, جبرائيل derives from **Hebrew**. The source states it comes from Hebrew גַּבְרִיאֵל (gavri'él), which itself originates from "גַּבְרִ י אֵל" meaning "my hero is God."

No Syriac/Aramaic or Greek etymological origins are mentioned in this article.
```


### [2026-09-06T15:31:54.907Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T15:32:05.775Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD GBRA ===\"; grep -n \"GBRA\\|gabrā\\|mard.*man\" PHD.txt | head -10; echo \"=== PHD mard ===\"; grep -n \"^mard\\|GBRA\" PHD_mackenzie.txt | head -10; echo \"=== NYB GBRA ===\"; grep -n \"GBRA\\|gabrā\" NYB_vol2_glossary.txt | head -10"
}
```


## [2026-09-06T15:32:06.307Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON part1/2 گبر ===\"; grep -n \"گبر\" MON_part1.txt MON_part2.txt | head -20; echo \"=== MON جبرئیل ===\"; grep -n \"جبرئیل\\|جبروت\\|جبران\" MON_part1.txt | head -20"
}
```


### [2026-09-06T15:32:06.369Z] TOOL RESULT

```
=== PHD GBRA ===
455:mand [mnd | = M] house. miindag [m?ndk! | M m'ndg, N ~a] tired; remiss; fault, sin. “Аһ: tiredness. māndan, !màn- [K TLWN-tn! < A У ktr | M mnd, N ~] stay, remain; v. also % *mán-. mang [mng] henbane. mänig [mnyk'] household member. mānistan [{KTLWNstn'] = mandan. māništ [m?nyst!] abode, dwelling. ~ag [-k'] sedentary, settled. mānsār [mnsl = Av. ma0ra-] (holy) word, spell. -~-bar [-b/] priest. ~spand [-spnd = Av. spanta-] holy word; v. máraspand. imar [ml | M mr, N ~] number, reckoning, account; class. *mar [m/] scoundrel, felon. таг [ml | N ~] snake. mār-, —išn, v. mārdan., тагар [mik!] number. тпагар [mPk!] perceptive, sensitive. Māraspand [mrspnd | N ~] (= máns?rspand), cal. 29th day. *martabuk [mic”5wk'] brave, valiant. ~ith: bravery, valour. mard [GBRA < A gbr; mlt' | M m(y)rd, N ~) man. mārdan, màr- [ml-tn'] perceive, notice, feel. ~i$n: perception. „išnūmaud [-£rwmnd] perceptive. mardanag [mit?nk! | N ~a] manly, brave. ~ih: manliness, bravery. mardóm [ANŠWTA < A?niwt?; mltwm | M mrdwhm, N mardum] man, mankind, people. ~th: humanity, humanness. mardóm-zàádag [mltwm 2tk' | N mardum-zād] human being. ~ih: humanity. marģ [mlg | M mrg, N ~] death. ~-arzan [-lc’n'] deserving death. ~ih: = marg. --0mand [-”wmnd] mortal. mārīģ [m'Lyk! | M mryg-] word, spell. marw [mlw! | M mrw, N —, (mary)] herb. marz [mlc | M mrz, N ~] boundary, march; astr. term. marzanģēūš [mlengws | N ~] marjoram. marzidan, marz- [mlc-ytn! | М mrzyst, mrz-] copulate. išn(īh): copulation, fornication. marz(o)bàn [mlcp’n' | № ~] margrave, warden of the marches. -masāy [-ms'd] suffix, -sized. mast [mst! | = M, N ~] bemused, intoxicated.
491:méx [myh | P myx, N ~] peg, nail. ~ ī gàh: astr. Polaris, pole star. 1-3méz-, v. mézidan, mëzišn, mistan. mēzd [my()zd | № тёз] offering, meal. „bān [-p’n' | N ~] host. mézidan, 'méz- [myc-ytn!] suck. *mézisn [myckn'] blinking, twinkling. mih [mt!] false, contrary, opposite. mihēxt [mytwht!] falsehood. imihr [mtr! | M myhr, N —] Mithra; sun; cal. 7th month; 16th day. tmihr [mtr!, etc.] contract, bond. šmihr [mtr!, etc.] love, friendship. mihrbān [mtr'p?n! | Р myhrb’n, N ~] friendly, kind. mihr-dróz [mtr'dhwc] = mihródruj. mihródruj [mtr?w-, mtrwk-diwe = Av. mitlyo.drujim] contract-breaker. ~th: breaking faith. mihr-zan [mtr'zn'] = mihródruj. mij(ag) [myc(k') | N muz(a)] eyelid; eyelash. mijüg (myc-, myšwk! | IN mizü] lentil. mir-, v. murdan. mistan, 3mëz- [mstn', myc- | N mézidan] urinate. -i$n(ih): urination. mizag [m(y)ck! | N maza] taste. ~darih [-d’lyh] (sense of) taste. ~ӧтапа [отпа] tasty. mizd [m(y)zd | N muzd] reward, hire, pay. ~war [-wbl | N -àr] hireling. *mizné [m(y)znydy] mist, dew. mög [mwk!] shoe. 5 *moy-mard [mgw-mit', -gGBRA | N muy) magus. mör [mwl | N <) ant. mórd [mwlt! | N ~] myrtle. morwārīd [mwlw'lyt! | M mwrwryd, N ~] pearl. *mowbed [mgwpt' | N móbad] Mazdean priest. móy [mwd | N ~] hair. móya$ [mwdk' | N méya] lamentation. móyen [mwdyn'] (made of) hair. moz [mwe | N ~] banana. mózag [mzvck! | N тоха] shoe. *mūdag [mwtk'} spoilt, destroyed. muy [DKRA < А dgP | N mux] date-palm. muhr [muwdl | M mwhr, N ~] seal. Сар [mwhlk! | P mwhrg, N ~a] bead, vertebra, piece (in backgammon, etc.). *muhrišn [*mwtl$n!] excrement. mulān [mwi?n'] belly (daevic).
=== PHD mard ===
3465:mard [GBRA < A gbr); mltl 1M m(y)rd, N ......] man.
3466:mardan, rnar- [m)l-tn l ] perceive, notice, feel.
3469:mardana~ [mlt)nk I N ......a] manly, brave.
3472:mardom [AN8WTA < A )nfwt); mltwm 1M mrdwhm, N mardum] man,
3475:mardorn-zada~ [mltwm z)tk l IN mardum-zti'd] human being.
3583:·moy-mard [m~!mlt', -gGBRA I N muy] magus.
10958:mardI                                           daxsag
11887:mardoml                  .AI¥'t"U .....    anjir                        ~~Y"
11888:mardomihl          ~"'t-o            ...   awizirisnig               '1)~,\'"
=== NYB GBRA ===
```


### [2026-09-06T15:32:06.399Z] TOOL RESULT

```
=== MON part1/2 گبر ===
MON_part2.txt:17098:رگبرگ‌های برجسته مشاهده می‌شود. 
MON_part2.txt:29204:دست گبرند و برده‌های 7 
MON_part2.txt:29931:گبرگه: (۵)دواده [- گبورگه] (.) آلتی 
MON_part2.txt:31949:فشار دارد» مورد استعمال قرار می گبرد. سته 
MON_part2.txt:41404:گبرندگان حقوق و مسلغ آن. 
MON_part2.txt:45787:متداول: ۱۱0۱۵2۷۵ [ع.] (افا.) فرا گبرنده 
MON_part2.txt:62970:تقدیس قرار گبرد. 
MON_part2.txt:64099:جای گبرد؛ جای‌گزین» جایگیر. 
MON_part2.txt:66430:کناره گبرد و گوشه گزیند؛ گوشه‌نشین» 
MON_part2.txt:93236:می‌گبرد؛ میوه‌اش سته است و از آن رنگ 
MON_part1.txt:5857:نافرمانی» سربیچی. نخوت» تگبر 
MON_part1.txt:18603:انیس: 2115 [ع.] (ص.) انس گبرنده؛ خوی 
MON_part1.txt:19876:۵ گبرگ و ۲۵ تا ۲۰ پرچم است. (کد.) 
MON_part1.txt:25715:گبرگ‌هایش که تفش کمرنگ و سفید و 
MON_part1.txt:34379:پیرکنعان (کد.) یعقوب. پیر گبر: خطابی 
MON_part1.txt:34380:طن زآمیز گبر و زردشتی کهن سال را. خطابی 
MON_part1.txt:34903:ممانة دو دولت در می گبرد» از اندازة ثبروی 
MON_part1.txt:35517:تعقیب کننده» دنبال گبرنده. آنکه رد بای 
MON_part1.txt:46764:گبرند. 
MON_part1.txt:62050:بافتن پارچه آن را در دست گبرند و لای 
=== MON جبرئیل ===
11710:دریافتن» غلط گرفتن بر» جبران کردن» تلافی 
21296:و جبروت. بحر دمان زیبق عمل: ( کد.) ابری 
32822:برای جبران در آخر هر سال پنج روز دیگر 
34332:شسود. (اخ.) جبرئیل. (اخ.) آدم(ص). 
42978:متمم. مالیات اضافی که برای جبران کسر 
43118:تلافی: آاةاها [ع.] (مص‌م.) دریافتن» جبران 
43120:در یافت؛ جبران. 
47139:جبرئیل: :1007 |- جبرائیل - جبریل] 
56767:جبروت الهی و محو در سطوات انوار 
64908:اقوام او برای جبران قتلی که واقع شده 
68876:مکرم: جبرئیل. (سد.) برده‌ای است از 
70315:خود را صرف کرده باشد به قدس جبروت و 
91961:جبرئیل امین. تعییرات: مثل طاوس: رنگین و 
94371:عالم عقول و نفوس مجرده» عالم جبروت و 
94384:ارواح. عالم جبروت: (فد. تص.) دات قدیم) 
94443:ملکوت: (فد.) عالم جبروت» عالم مجردات. 
94915:موّدیان مالیات یک ناحیه برای جبران کمبود 
98911:عالم‌های لاهوت» ملکوت» جبروت و ملک 
98915:عالم‌های علم» عین» جبروت» ملکوت و
```


## [2026-09-06T15:32:13.597Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '47135,47145p' MON_part1.txt; echo \"=== gabr headword ===\"; grep -n \"^گبر\\|گبر:\" MON_part2.txt | head -20; echo \"=== gabrak ===\"; grep -n \"گبرک\\|زردشتی\\b\" MON_part2.txt | head -10"
}
```


### [2026-09-06T15:32:13.682Z] TOOL RESULT

```
چسسروت. 202 [ع.] (.) قدرت» 
عظمت. عالم قدرت و عظمت الهی» جهان 
برین؛ مق. ناسوت. 

جبرئیل: :1007 |- جبرائیل - جبریل] 
(اخ.) یکی از فرشتگان مقرب. (ا.) دل که به 
زعم صوفیان مهبط انوار الهی و محل وحی 
و الهام او است. 

جیسین: 10 (- جیسین» معر.(.) گچ) 
حبص. 
=== gabr headword ===
29931:گبرگه: (۵)دواده [- گبورگه] (.) آلتی 
41404:گبرندگان حقوق و مسلغ آن. 
=== gabrak ===
4168:زردشتی (مخصوصاً مقیم هند): پارسی. 
7005:نروهره: ۲ (.) (دین زردشتی) 
11284:زردشتیان): (کد.) آتش. قبلةٌ عالم: پادشاه 
16713:«فره و شی» با «فروهر» زردشتی شباهت 
29925:زردشتی» زر تشتی» مجوس. 
36856:گوگرد سرخ زردشتی: (کد.) آتش» هیزم 
61393:زردشتی. زردشتی (بطور اعم) ج. مغان. 
61463:مغان: شرابی که زردشتیان به عمل آورند. 
63992:زنان زردشتی ايران و آن پارچه‌ای است که 
67654:زردشتی. موبد موبدان: رئیس موبدان؛
```


## [2026-09-06T15:32:15.966Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29915,29935p' MON_part2.txt; echo \"=== 61388 ===\"; sed -n '61388,61396p' MON_part2.txt"
}
```


### [2026-09-06T15:32:16.033Z] TOOL RESULT

```
محامعت کند؛ مباشرت کننده» آرمنده. 
کایه: (0-)23-2 (امص.) وه ماشرات. 
گکایدن: 22-0 [ - گادن] (مسص م 0( 
مسجامعت کردن سا..» مباشرت کردن» 
آرمیدن. خواهر کسی را گاییدن: (عم.) 
سخت به زحمت انداختن وی را. 

گبت: ۰«ءو (.) (جاد.) زنبور عسل» مگس 
گیر: جع [آرا. قس. ع. کافر) شاه کنواز 
مش رککك] (ص. ا.) کافر» ملحده بت‌پرست. 
زردشتی» زر تشتی» مجوس. 

کبر: ۲ [- کیر ] (ا.) کبر. خود و خفتان. 
کر ۲ (.) نک باشد که از آن دیگ 
و طبق و کاسه و مانند آن سازند. 

گبرگه: (۵)دواده [- گبورگه] (.) آلتی 
است مانند کمان» از آهن ساخته و 


ربب ۳۳/] 
=== 61388 ===
(ص.) کود» عمیق؛ ژرف. .مغ اندر آمدن به 
کاری: ژرف نگریستن در آن. (مقدمة 
التفهیم ص قف). 

: 0187 ,010 (۱.) فردی از قبلة مغان. موبد 
زردشتی. زردشتی (بطور اعم) ج. مغان. 
معار: ۲ (.) (خاد.) ]۳ است که در 
خاتم‌سازی بکار می‌رود و به وسیلهً آن 
سریشم‌هایی را که بر اثر فشار از کناره‌های
```


## [2026-09-06T15:32:27.916Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^جبر\\|^جبران\\|جبران:\\|جبر:\" MON_part1.txt | head -10; echo \"---\"; sed -n '47120,47139p' MON_part1.txt"
}
```


### [2026-09-06T15:32:27.988Z] TOOL RESULT

```
17644:جبری در آمدن» آموده شدن. به آخر 
24493:دختری. ازالهٌ بکارت به جبر: (فق. حق.) به 
35404:جبرگیل. بیکث رایگانی: (کذ.) ماه؛ قمر. 
41944:جبره کردن» غلبه دادن؛ ج. تغلسات. 
47139:جبرئیل: :1007 |- جبرائیل - جبریل] 
47592:جبرینگ] (اصت.) صدای زنگ و طاس و 
56767:جبروت الهی و محو در سطوات انوار 
91961:جبرئیل امین. تعییرات: مثل طاوس: رنگین و 
---
کاری به زور گماشتن» ناچار کردن. (مد.) 
قابل بودن به عدم اختیار بنده. (.) (مد.) 
طر یقه‌ای که پیروان آن (جبریه) معتقدند که 
اعمال انسان به اراد خدای تعالی انجام گیر د 
و بندگان هیچ گونه اختیاری از خود ندارند؛ 
مق. اختبار» تفویض. (رض.) جر و مقالله» 
بخشی از ریاضی که در آن برای حل 
مجهولات حروف و علامات را بجای اعداد 
بکار رود. (مکن.) اصلی مبتی بر اینکه هیچ 
جسم ساکنی متحرک نمی‌شود و هیچ 
متحرکی ساکن نمی‌گردد مگر آنکه قوه‌ای 
وی را به حرکت و سکون وا دارد. 
جیران: م9 [ع.] (مص ع.) تلافی کردن. 
(امص.) تلافی. 

چسسروت. 202 [ع.] (.) قدرت» 
عظمت. عالم قدرت و عظمت الهی» جهان 
برین؛ مق. ناسوت. 

جبرئیل: :1007 |- جبرائیل - جبریل]
```


## [2026-09-06T15:32:37.029Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D8%A8%D8%B1%D8%A7%D9%86",
 "prompt": "Arabic جبران (jubrān / jibrān): is it an Arabic word? What does it mean and what is its etymology (verbal noun of جبر)?"
}
```


## [2026-09-06T15:32:38.151Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D8%A8%D8%B1%D9%88%D8%AA",
 "prompt": "Arabic جبروت jabarūt: meaning and etymology; is the -ūt suffix of Aramaic/Syriac origin? Quote."
}
```


### [2026-09-06T15:32:43.386Z] TOOL RESULT

```
# Analysis of جبران (Jubran)

Yes, جبران is an Arabic word. According to the Wiktionary entry, it functions as both a proper noun and common noun in Arabic.

## Meanings and Forms

**As a proper noun:** The entry shows it's "a male given name, Jubran" and "a surname, Jubran," with pronunciation /d͡ʒub.raːn/.

**In Egyptian Arabic:** جبران (gubrān) serves as a "verbal noun of جبر (gābar)," indicating it derives from the root verb جبر.

## Etymology

The term originates from Arabic and subsequently spread to other languages. The entry notes that Persian borrowed جبران from its Arabic counterpart, demonstrating the word's foundational role in Semitic linguistics.

The structure suggests جبران relates to the concept of restoration or compensation, consistent with verbal noun formation in Arabic morphology where the ja-form (ج-pattern) frequently creates action nouns from triconsonantal roots.
```


### [2026-09-06T15:32:46.470Z] TOOL RESULT

```
# جبروت (jabarūt) - Meaning and Etymology

## Meaning
The Arabic noun جبروت has two primary definitions:

1. **Power and virility** — strength and masculine force
2. **Tyranny, despotism, and oppression** — authoritarian abuse

## Etymology and the -ūt Suffix

According to the Wiktionary entry, this term was "Borrowed from Aramaic גַּבְרוּתָא / ܓ݁ܰܒ݂ܪܽܘܬ݂ܳܐ (gaḇrūṯā)."

The -ūt suffix does indeed derive from Aramaic/Syriac origins, as evidenced by its presence in the Aramaic source form. This suffix appears in multiple related Arabic terms listed, including malakūt (dominion), lāhūt (divinity), and kahanūt (priesthood), suggesting it's a productive morphological pattern for creating abstract nouns in Arabic borrowed from or influenced by Semitic Aramaic.
```


## [2026-09-06T15:32:53.375Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFA gabbar/jabbar ===\"; grep -n -i \"gabbâr\\|gabbar\\|ǧabbār\\|jabbar\\|gabrûtâ\\|ǧabarūt\" AFA.txt | head -20"
}
```


### [2026-09-06T15:32:53.423Z] TOOL RESULT

```
=== AFA gabbar/jabbar ===
```


## [2026-09-06T15:32:56.057Z] TOOL CALL #41: Bash

```json
{
 "command": "pdftoppm -f 230 -l 230 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg230 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T15:32:58.472Z] TOOL RESULT

```
total 4692
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 11:32 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    638 Sep  6 11:28 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb  69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb  81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4812 Sep  6 11:28 c224_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3203 Sep  6 11:28 c224_n7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12820 Sep  6 11:27 c229_bibua.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5308 Sep  6 11:27 c229_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5313 Sep  6 11:27 c229_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb   7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12347 Sep  6 11:20 c_hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12691 Sep  6 11:20 c_ieuo.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2071 Sep  6 11:26 c_ijlak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  14654 Sep  6 11:20 c_ijlak.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12239 Sep  6 11:20 c_latis.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb 111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb  11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83691 Sep  6 11:19 gen215.py
-rw-rw-r-- 1 sfmqrb sfmqrb   2303 Sep  6 11:25 j.json
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb  37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb  77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb  61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb  80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb  67513 Sep  6 11:27 mk217.py
-rw-rw-r-- 1 sfmqrb sfmqrb  17605 Sep  6 11:25 mk218.py
-rw-rw-r-- 1 sfmqrb sfmqrb  50138 Sep  6 11:24 mk222.py
-rw-rw-r-- 1 sfmqrb sfmqrb  78297 Sep  6 11:32 mk223.py
-rw-rw-r-- 1 sfmqrb sfmqrb  17907 Sep  6 11:25 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb  54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb  53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb 141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb 194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb 117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb  76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb 147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71937 Sep  6 11:19 pg219.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb 118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb  90848 Sep  6 11:22 pg224hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55412 Sep  6 11:15 pg224.png
-rw-rw-r-- 1 sfmqrb sfmqrb  80963 Sep  6 11:32 pg225.png
-rw-rw-r-- 1 sfmqrb sfmqrb 161218 Sep  6 11:26 pg226hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74322 Sep  6 11:19 pg226.png
-rw-rw-r-- 1 sfmqrb sfmqrb  54381 Sep  6 11:31 pg227.png
-rw-rw-r-- 1 sfmqrb sfmqrb  52519 Sep  6 11:25 pg228.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78760 Sep  6 11:27 pg229hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  42112 Sep  6 11:26 pg229.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65310 Sep  6 11:32 pg230.png
-rw-rw-r-- 1 sfmqrb sfmqrb 147680 Sep  6 11:20 sns167.jpg
```


## [2026-09-06T15:33:01.398Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg230.png"
}
```


### [2026-09-06T15:33:01.734Z] TOOL RESULT

```

```


## [2026-09-06T15:33:01.724Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:33:23.646Z] TOOL CALL #43: Bash

```json
{
 "command": "sed -n '1,200p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T15:33:23.697Z] TOOL RESULT

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


## [2026-09-06T15:33:32.103Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT algebra ===\"; grep -n -i \"^ALGEBRA\\|algebra\" SKT.txt | head -5; echo \"=== FSD algebra ===\"; grep -n -i \"al-jabr\\|al  jabr\" FSD_vol1.txt | head -5; echo \"=== WEB algebra ===\"; grep -n -i \"al-jabr\" WEB*.txt | head -5; echo \"=== LAM ===\"; grep -n -i \"alg.bre\\|djabr\" LAM.txt | head -8"
}
```


### [2026-09-06T15:33:32.220Z] TOOL RESULT

```
=== SKT algebra ===
104:therefore  introduce  this  symbol  +  by  way  of  warning.     It.  has ttsual  algebraical  value  o^ plus  or  additional  \  and  indicates  *addiLioi information  to  be  obtained  from  the  comparison  of  cognate  forms.*
514:ALGEBRA.  7
529:Algebra.   (Low  L.  —  Arab.)      J-ow  L
23694:Low  lAtin  from  Ar&he:  Algebra, aaraccn.
=== FSD algebra ===
=== WEB algebra ===
5439:al/ge-bra, n. [Fr. alzébre; Russ. algebra; Ar. al-jabr, al-jebr, the reunion of broken parts, as the reduction of fractions to whole numbers; jabara, to reunite, bind together.]
=== LAM ===
1493:Algèbre. Etymol. bien connue. Esp. ptg. cat: algebra
1494:basq: algebrea de jM a%abr (2) réduction. Chez les
1513:(2) «de Tarabe aldjabrounn dit M. Brachet qui joint ensemble l'article
8359:Algèbre
```


## [2026-09-06T15:33:33.517Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN gabr ===\"; grep -n -i \"gabr\" HRN.txt | head -10; echo \"=== HUB gabr ===\"; grep -n -i \"gabr\" HUB.txt | head -10; echo \"=== AFM جبر ===\"; grep -n \"الجبر\\|جبروت\" AFM_pages.txt | head -5"
}
```


### [2026-09-06T15:33:33.640Z] TOOL RESULT

```
=== HRN gabr ===
8161:wo allerdings phlv. gabrä (semitisch!, nur *Mann
=== HUB gabr ===
=== AFM جبر ===
```


## [2026-09-06T15:33:39.504Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT ===\"; sed -n '526,534p' SKT.txt; echo; echo \"=== HRN 8150-8175 ===\"; sed -n '8150,8175p' HRN.txt"
}
```


### [2026-09-06T15:33:39.581Z] TOOL RESULT

```
=== SKT ===
Ale.  (E.)  M.  E.  a/f,-  A.  S,  /«/«.+ led.,  S  wed,  and  Dan.  «/;  Lilhnon.  ahu; KoM.  oi\  olevina.
Alembic,  0  vessel  for  distilling.  (F  — Span.-Arab.-Gk.)  M.  E.  aUpthk."?. altxmhique  (Cot.)  •  Span,  alambiqut.  — Arab.  tU,  the;  and  antik  (pronouncctl  am' ink's,  a  still.  —  Gk.  li/i^i^.  a  cup,  goblet; can  of  a  GtjU.-Gk.  &^^,  4l/i^<vr,  foot  of  a goulct ;  allied  to  L,  nntbo^  %  bow.
Alert.  (F.-ltal.-L.)    See  B^ffent.
Algebra.   (Low  L.  —  Arab.)      J-ow  L
ALGUAZIL,
ALLIANCE.
alj^hxt,  compDtatiuD. *Arab.  (z/,  the;  auid faftr^  setting,  repairing  -,  :lIso,  ibe  rcUictiou of  fractioiu  lo  integers  in  arithmetic  ;  hciicr. ilgcbra,  — Arab,  root  j'a^ra,  to  set,  con- sol  ulale, Al^iazil.  B  police-<'flicer;  see  Vlaler. Alburn,  umial-wood.      (Heb.  -  Skt.) In  i  Chroo.  ii.    8.  ix,   to;    spelt  almug, I  Kiiij^s,  X.  II.— Ileb.  a/^/mm/)?/,  or  <tnin»- pose*I  I  atmugim  ;  a  bcirrowed  won!.  — SIct. vaisU'ka^    saiidal-wood ;    where    'ka    is   a sufnx. Alien.  (F.-L.)      M.  E.  aliau.^O.  F. aiicH.  —  L.  alienuj.  sbsnge  ;  a  stranger.  —  L. alius,  another. +  Gk,tfXAor,  another;  Goth. aiii,  other ;  see  Else.  Allegory.
aliaa.  (L.)  Low  L.  o/m/.  otherwise.  •• L.  aiius.
alibi,  (L.)  Low  L.  aiibi,  in  another pUce.  —  L.  d/i'-,  iiom  alius  ;  and  sufhx  'hi %&  in  i-^f.  there,  uhi,  where.

=== HRN 8150-8175 ===
') Hierher wird geng bei AM. gehören (von der Stimme, 203
Zeile 5, von Schmerzen, 236 Zeile 8, vom Kopf gesagt, 90 Zeile 12),
dofl zu yeng *gekrummt' jedenfalls nicht passt.
U o r n , Grundriss d. neup. Etymologie. 1 4— 210 —
gör 'Grab*, dagegen, das Geiger neuerdings (Lautl.
des Bai. 53) mit ai. ghörd- grausig, furchtbar ver-
glichen hat, ist nach Nöldeke, Pers. Stud. II, 41 ein
semitisches Lehnwort. Beiläufig bemerkt, ist türk. LW.
g*aur wohl nicht arab. kaßr (Hübschmann unter oss.
d. gaur, t. daur, S. 123), sondern vielmehr neupers.
gebr, gahr^) (vergl. Geiger, bei. LW. gaur, No. 81,
wo allerdings phlv. gabrä (semitisch!, nur *Mann
bedeutend) nicht als Grundform stehen durfte).
939. guvälfden, gevaltden (falsch k"*) wachsen* (unbelegt);
vergl. bällden (No. 173).
ai. vi + {/^vardh- ^heranwachsen, gedeihen ; ist schon
im PehlevT verschwunden.
940. guvah, guva *Zeuge'.
ai. vi + \/^ka^- Intens, ausschauen, erschauen, wahr-
nehmen'; phlv. gukäs 'Zeuge', gtikasih (M^n.), arm. LW.
vkay *Zeuge', vkayem 'ich bezeuge* 2).
941. gösäle 'Kalb'.
ai. vatsd' 'Kalb, Jährling*.
käfir. vatsala, si^n. botsöri 'Jährling' (Tomaschek,
S. 765).
Das ö in gösäle stammt von go 'Kuh' (No. 888).
```


## [2026-09-06T15:33:48.859Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB gaur/kafir ===\"; grep -n -i \"gaur\\|käfir\\|kafir\" HUB.txt | head -10; echo \"=== ARY ===\"; grep -n \"گبر\\|جبر\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-06T15:33:48.917Z] TOOL RESULT

```
=== HUB gaur/kafir ===
=== ARY ===
1272:واژه‌های همریشه همه دارای معنی همسانی بودند آنگاه می‌توانستیم با اطمینان پیشتر ننیجه بگبریم؟ و
```


## [2026-09-06T15:33:50.420Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD1 algebra ===\"; grep -n -i \"algebra,\" FSD_vol1.txt | head -5; echo \"=== FSD2 Gabriel ===\"; grep -n -i \"Gabriel\" FSD_vol2.txt | head -5; echo \"=== WEB Gabriel ===\"; grep -n -i \"Gabriel\" WEB.txt | head -5"
}
```


### [2026-09-06T15:33:50.531Z] TOOL RESULT

```
=== FSD1 algebra ===
7426:ad-dl'tlon,  1   a-dish'an;  2   :VdIsh'on,  n.  1.  The  act  of adding;  as,  the  addition  of  numbers  to  make  a   sum.  2. Anything  added;  an  annex;  accession;  as,  an  addition to  a   house,  or  to  land  laid  out  in  lots,  a3  in  a   village. 3.  Specif.:  (I)  Afus.  A   dot  on  the  right  side  of  a   note lengthening  it  one-half.  (2)  Law.  A   title  or  mark  of designation  attached  to  a   man’s  name  to  show  his  busi- ness, office,  place  of  residence,  etc.;  as,  John  Smith, Esq.;  Thomas  Jones,  ship-chandler;  William  White,  of Baltimore.  (3)  Her.  Augmentation.  4.  Math.  (1)  In arithmetic,  the  uniting  of  two  or  more  quantities  in  one sum  or  sum  total:  the  first  ground  rule.  (2)  In  algebra, the  combination  of  quantities  according  to  their  alge-
7593:adding;  as,  the  addition  of  numbers  to  make  a   sum.  2. Anything  added;  an  annex;  accession;  as,  an  addition to  a   house,  or  to  land  laid  out  in  lots,  as  in  a   village. 3.  Specif.;  (1)  Mus.  A   dot  on  the  right  side  of  a   note lengthening  it  one-half.  (2)  Law.  A   title  or  mark  of designation  attached  to  a   man’s  name  to  show  his  busi- ness, office,  place  of  residence,  etc.;  as,  John  Smith, Esq.;  Thomas  Jones,  ship-chandler ;   William  White,  of Baltimore.  (3)  Her .   Augmentation.  4.  Math.  (1)  In arithmetic,  the  uniting  of  two  or  more  quantities  in  one sum  or  sum  total;  the  first  ground  rule.  (2)  In  algebra, the  combination  of  quantities  according  to  their  alge- braic signs,  negative  cjuantities  being  taken  in  the  op- posite sense  from  positive.  [<  L.  additio(n~),  <addo; see  add.)
11623:I   never  saw  an  algebra  .   .   .   until  after  I   was  appointed  to  West Point.  U.  S.  Grant  Pers.  Mem.  vol.  i,  p.  24.  [c.  i..  w.  1885.1 f   <   It.  algebra,  <   Ar.  al-jebr,  binding  together,  <   al, the,  -f  jabara,  reunite.]  —   Boollan  or  logical  algebra,  a method  of  dealing  with  concepts  of  logic  by  means  of  alge- braic symbols  and  operations.— double  a.,  that  form  of algebra  in  which  the  symbols  Indicate  lines,  their  lengths, and  their  directions.— graphic  a.,  algebra  in  which  curves are  used  to  express  the  relations  of  quantities;  simple  ana- lytical geometry.— multiple  or  n*way  a.,  that  algebra  In which  heterogeneous  units  are  combined  and  multiplied.— pure  a.,  algebra  In  which  all  the  units  are  definitely  related. —   rhetorical  a.,  the  discussion  of  problems  by  algebraic methods,  but  in  ordinary  language;  algebra  without  nota- tion.— universal  a.,  a   method  of  reasoning  by  symbols,  of which  the  general  definitions  may  be  applied  to  any  process of  addition  and  others  to  any  process  of  multiplication; 901),  king  of  the  West  Sax„ns  in  England;  established  an  „   s   nt
46684:Boole,  I   bQl;  2   bool.  George  (*1/2l815-**/sl864).  An English  mathematician  and  logician;  Laics  of  Thought,  1854. Bool'ian,  1   bul'yon;  2   bool'yan,  a.  Of  or  pertaining  to the  mathematician  Boole;  as,  Boolian  algebra, bool'yt,  n.  Formerly,  In  Ireland,  a   shelter  for  cattle;  also,  a company  of  people  wandering  from  place  to  place  with  their cattle,  for  pasturage^
75683:shafts  about  a   central  core.—  c.  pistil  (Bot.),  a   pistil made  up  of  two  or  more  coalesccnt  carpels.—  c.  quanti- ty, In  algebra,  a   quantity  made  up  of  two  or  more  quanti- ties connected  by  the  plus  or  minus  sign;  also.  In  arithmetic, a   quantity  Indicated  by  a   compound  number.—  c.  ratio,  a ratio  made  up  of  other  ratios,  as  aft  ;   cd  Is  made  up  of  the two  ratios  a   :   c   and  b   :   d.~  c.  screw,  a   screw  whose  thread runs  In  different  directions,  or  has  dif- ferent pitches  In  different  parts  of  its length.— c.  sentence,  a   sentence  that contains  two  or  more  principal  senten- ces  coordinated,  as  In  “   the  sun  rose  A   Compoun(1  Screw. and  the  dew  vanished.'  Compare  v
=== FSD2 Gabriel ===
1787:auuldlngsall-boomswhen  tho  sallsarefurlrd.— down' d)ow",  pouring  down,  a   copioimand  hoavy  tall,  as  of  rain._  doy"cn',  1   dwa''yafi';  2   dwii-yiiiV,  w.  [P.l  A   dean,  as  of  a n.  ADm.  Instrlnged  instruments,  the  downward  stroke  of  the  down 'right",  1   daun'rait;  2   d(3wnrit  ,   (I.  _   1.  Straight  Doy"cn',  Gabriel  Francois  (1726-«/aSn6).  A   French how  from  nut  to  point,  which  is  used  to  elicit  a   very  full  to  the  point,  as  that  which  falls  or  is  driven  directly  historicfil  painter  who  decorated  the  palaces  of  Catherine  II.
16660:Fah'ren-heit,  Gabriel  Uaniei  (GitH)86-»/iol73G).  A   Ger-  eient;  busy;  useless;  a   term  applied  to  the  lato  Merovlu- man  physicist;  invented  the  mercurial  thermometer,  gian  Icings  of  irraneo,  who
18049:«   ^   F»u"re',  1   fOTC';  2   fO'rt;.  Gabriel  Urbalu  (VulKd.l-nA
18177:Fa'vre,  1   fii'vr;  2   fU'vr,  Jules  Gabriel  Claude  («/2ilS09-‘/2o
28776:Eab'ble-ratch"c,  etc.  Same  as  Gabriel  katchet. gab'bock, «.  [Local,  Brit.]  Same  as  g.abback. gab'bro,  1   gab'ro;  2   e^h'ro,  n.  [It.]  Petrol.  An  igneous  rock of  gnmular  texture,  consisting  es-sentlally  of  pyroxene,  usu- ally auglte  or  diallage,  and  plagloclase,  commonly  Inbrador- ite,  ordinarily  with  magnetite,  and  in  many  varieties  with Olivine,  Varieties  with  rhombic  pyroxene  are  called  norite, —   gab'bro»di"o-rite,  «.  Petrol.  A   variety  of  gabbro  char- acterized by  a   large  amount  of  homhlende.  and  theretoro Intermediate  between  gabbro  and  dlorlte.  The  hornblende may  lie  secondary  alter  auglte,  when  the  rock  is  really  a metagabbro.— gab-bro'ic,  a.  Geol.  Of  or  consisting  of gabbro.  gab"bro-lt'lct.— gab'brold,  a.  Petrol.  Having  a texture,  appearance,  or  mineral  composition  simihar  to  or related  to  that  of  gabbro.  Also,  used  of  a   rock-magma, having  the  character  or  composition  requisite  for  the  forma- tion of  gabbro.— gab'bro-nlte,  h.  Mineral.  A   bluish-gray variety  of  altered  wernerite,  [clous,
=== WEB Gabriel ===
ugrep: warning: WEB.txt: No such file or directory
```


## [2026-09-06T15:34:00.197Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls WEB*; echo \"=== FSD2 Ga'bri-el ===\"; grep -n \"Ga'bri-el\\|Gabri-el\" FSD_vol2.txt | head -5; echo \"=== MON گابریل ===\"; grep -n \"گابریل\\|جبرائیل\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-06T15:34:00.281Z] TOOL RESULT

```
WEB_vol1.txt
=== FSD2 Ga'bri-el ===
=== MON گابریل ===
MON_part1.txt:47139:جبرئیل: :1007 |- جبرائیل - جبریل]
```


## [2026-09-06T15:34:03.523Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"gabriel\" WEB_vol1.txt | head -8; echo \"=== FSD2 gab section ===\"; sed -n '28770,28790p' FSD_vol2.txt | grep -o -i \"Ga.bri.el[^.]\\{0,180\\}\" | head -5"
}
```


### [2026-09-06T15:34:05.697Z] TOOL RESULT

```
8121:2. [A-] the announcement of the incarna- tion of Jesus, made to the Virgin Mary by the angel Gabriel (Luke i. 26-38.).
14238:Betwixt these rocky pillars Gabriel sat,
70207:Fah/ren-heit (or fir’), a. [named from Gabriel Daniel Fahrenheit (1686-1736), G. physicist who devised the scale.] designating or of a thermometer that places the freezing point of
70543:Fal-16/pi-an, a. of, pertaining to, or di by Gabriel Fallopius, or ng to. or discovered anatomist of the sixteenth century.
79282:gī’ble, v.t.; gabled, pt., pp.; gabling, ppr. to put a gable or gables on. gī’ble, v.i. to be in the form of, or end in, a gable. gī’ble end, the end of a building which is sur- mounted by a gable. £4/ble roof, in architecture, a ridged roof with a gable at its end or ends, £4’blet, n. a small ornamented gable or canopy _ formed over a niche or buttress. #4’ble wall, the wall on which a gable rests. €4’ble win’dodw, in architecture, a window in 3 “a gable or a window that is gable-shaped at ee the top. 3 gab/lock, 7. [ME. gaveloc; AS. gafeluc, a spear, a javelin.] the metal spur of a gamecock. Ga’bri-el, n. in the Bible, one of the seven archangels, the angel of the Annunciation and the herald of good news and comfort: Luke i. 26. Dan, viii. ix. Ga’bri-el-ite, n. in ecclesiastical history, an Anabaptist sect founded in 1530 in Pomera- nia: so called from its founder, Gabriel Scher-
103129:Abraham by the angel Gabriel. kia’ma, n. same as caama. kab, n. same as cab (measure). kab/a-l4, kab’ba-la, n. same as cabala. ka-bas’séu, n. same as cabasou. ka-bob’, n. and v.t. same as cabob.
=== FSD2 gab section ===
```


## [2026-09-06T15:34:13.046Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/gabr/",
 "prompt": "GABR: quote the etymology paragraph — Aramaic GBRʾ/gabrā \"man\", free peasants in Mesopotamia, and the rejection of Pūr-e Dāwūd's Arabic kāfer derivation."
}
```


## [2026-09-06T15:34:14.343Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Gabriel",
 "prompt": "Etymology of Gabriel: Hebrew Gabhri'el, gebher \"man\", El \"God\"; route via Greek/Latin into English."
}
```


### [2026-09-06T15:34:15.217Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:34:20.174Z] TOOL RESULT

```
# Gabriel: Etymology and Meaning

The name Gabriel originates from Hebrew *Gabhri'el*, which literally means **"man of God."** The name combines two elements: *gebher* meaning "man" (derived from the verb *gabhar*, meaning "was strong") and *El* meaning "God."

In religious tradition, Gabriel is recognized as an Old Testament angel. The name gained particular prominence through Christian theology, notably in the Annunciation—"the visit of the angel Gabriel to the Virgin Mary, foretelling the incarnation," commemorated on March 25.

The name entered English through Greek and Latin intermediaries. Interestingly, "Gabriel's hounds" was a 17th-century folk term used to explain the mysterious sounds of wild geese flying overhead at night or in cloud cover.

**Common short form:** Gabe
```


## [2026-09-06T15:34:29.028Z] TOOL CALL #53: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/algebra\" \"https://www.etymonline.com/word/algebra\" \"https://en.wiktionary.org/wiki/%DA%AF%D8%A8%D8%B1\" \"https://en.wiktionary.org/wiki/%D8%AC%D8%A8%D8%B1%D9%88%D8%AA\" \"https://en.wiktionary.org/wiki/%D8%AC%D8%A8%D8%B1%D8%A7%D9%86\" \"https://en.wiktionary.org/wiki/%D8%AC%D8%A8%D8%B1%D8%A7%D8%A6%D9%8A%D9%84\" \"https://www.etymonline.com/word/Gabriel\" \"https://www.iranicaonline.org/articles/gabr/\"; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note 'page 230, root J.b.r/Jabra (Aramaic g-b-r): algebra, gabr, Gabriel' 2>&1 | tail -3; done"
}
```


### [2026-09-06T15:34:36.729Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/algebra
/home/sfmqrb/git/rishe/data/verification/sources/web/39f544a0e8ccc340.txt
### https://www.etymonline.com/word/algebra
/home/sfmqrb/git/rishe/data/verification/sources/web/d2e71d3bbd13cf7a.txt
### https://en.wiktionary.org/wiki/%DA%AF%D8%A8%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/8f0e434d88471f3c.txt
### https://en.wiktionary.org/wiki/%D8%AC%D8%A8%D8%B1%D9%88%D8%AA
/home/sfmqrb/git/rishe/data/verification/sources/web/f8ffd8e024d80f68.txt
### https://en.wiktionary.org/wiki/%D8%AC%D8%A8%D8%B1%D8%A7%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/59eeda84f3ed41e4.txt
### https://en.wiktionary.org/wiki/%D8%AC%D8%A8%D8%B1%D8%A7%D8%A6%D9%8A%D9%84
/home/sfmqrb/git/rishe/data/verification/sources/web/b2b9c1f11b1e6e33.txt
### https://www.etymonline.com/word/Gabriel
/home/sfmqrb/git/rishe/data/verification/sources/web/b8e40f7fe9a8ab86.txt
### https://www.iranicaonline.org/articles/gabr/
/home/sfmqrb/git/rishe/data/verification/sources/web/c24d741f6bc7bc86.txt
```


## [2026-09-06T15:34:40.571Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== IRANICA ===\"; wc -c c24d741f6bc7bc86.txt; grep -n -i \"aramaic\\|kāfer\\|kafer\\|Pūr\\|peasant\" c24d741f6bc7bc86.txt | head -20"
}
```


### [2026-09-06T15:34:40.619Z] TOOL RESULT

```
=== IRANICA ===
6144 c24d741f6bc7bc86.txt
57: GABR ( gabrak , gawr , gaur “Zoroastrian”; gabrī , gabrakī “Zoroastrianism”) , a New Persian term deriving, in all likelihood, from Aramaic GBRʾ / gabrā (lit. man), which in the Sasanian period was used to indicate the free peasants in the region of Mesopotamia (Stayermanova, II, 25.2.1). The term is used in all stages of New Persian literature from the earliest period (e.g., Šāh-nāma , Moscow, I, p. 149;Balʿamī, ed. Bahār, p. 2; Sanāʾī, p. 368) as a technical term synonymous with mōḡ (magus), or the obsolete ātašparast (fire-worshipper), along with other religious denominations (e.g., Rūmī, Ḡazalīyāt , p. 124). With the dwindling of the Zoroastrian community because of frequent proselytisations and the curtailment of their social rights, the term came to have a pejorative implication, which is the reason for its commutation to the respectable zardoštī (Zoroastrian) in recent times.
58: Several etymologies have been proposed for the term, none of which is convincing. Some scholars have suggested mog-mard / mgw-GBRʾ (magus), which is, however, untenable, for the element GBR ʾ/ gabrā , being an ideogram and a bound constituent of the compound, cannot appear in absolute form, nor may it be pronounced other than mard (man) in common parlance. The etymology suggested by Ebrāhīm Pūr-e Dāwūd, which has been received more favorably, is based on the supposed mispronunciation of the Arabic kāfer (unbeliever) by the Persians in early Islamic Period. But, although Persians still fail to articulate some Arabic speech sounds properly, there is no unusual sound in kāfer that would require phonetic modification. Moreover, although gabr has been sometimes used to denote infidel ( kāfer ) by semantic extension (e.g., Rūmī, Maṯnawī II, p. 287, v. 177; Ḥasan Rūmlū, ed. Navāʾī, I, p. 384; Eskandar Beg, I, pp. 85, 87), kāfer as a generic word could hardly refer to a specific revealed religion such as Zoroastrianism. It, therefore, seems likely that gabr , used already in Sasanian times in reference to a section of Zoroastrian community in Mesopotamia, had been employed by the converted Persians in the Islamic period to indicate their Zoroastrian compatriots, a practice that later spread throughout the country. The term has also been used by the Muslim Kurds, Turks, and some other ethnic groups in modified forms to denote various religious communities other than Zoroastians, sometimes even in the sense of unbeliever.
67: M. Moḥīṭ Ṭabāṭabāʾī, “Lafẓ-e gabr moštaqq az kāfer nīst,” Hūḵt 21/6, 1349 Š./1970, pp. 35-41.
72: E. Pūr-e Dāwūd, Anāhītā , Tehran, 1343 Š./1964, pp. 302-18.
```


## [2026-09-06T15:34:47.338Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"aramaic\\|kāfir\\|Etymology 2\" 8f0e434d88471f3c.txt | head -10; echo \"=== jabarut ===\"; grep -n -i \"aramaic\\|Borrowed\" f8ffd8e024d80f68.txt | head -8; echo \"=== jubran ===\"; grep -n -i \"verbal noun\\|Etymology\" 59eeda84f3ed41e4.txt | head -10"
}
```


### [2026-09-06T15:34:47.411Z] TOOL RESULT

```
71: Etymology 2 
184: Etymology 2
187: Borrowed from Aramaic 𐡂𐡁𐡓𐡀 ( gbrʾ /⁠gaḇrā⁠/ , “ man; person ” ) , reflected in the Middle Persian logogram ( huzvarishn ) GBRA ( mard , “ man ” ) . The Persian word was probably used in pre-Islamic Persia to refer to some Zoroastrians in Mesopotamia (inhabited by many Aramaeans).
189: Traditionally has been derived from Arabic كَافِر ( kāfir , “ unbeliever ” ) , but that is problematic on phonetic and semantic grounds.
259:gar kāfir u gabr u but-parastī bāz-ā!
321: “ gbr ”, in The Comprehensive Aramaic Lexicon Project , Cincinnati: Hebrew Union College, 1986– 
338: Persian terms borrowed from Aramaic 
339: Persian terms derived from Aramaic 
353: Aramaic terms with redundant transliterations 
=== jabarut ===
153: Borrowed from Aramaic גַּבְרוּתָא / ܓ݁ܰܒ݂ܪܽܘܬ݂ܳܐ ( gaḇrūṯā ) .
246: Arabic terms borrowed from Aramaic 
247: Arabic terms derived from Aramaic 
=== jubran ===
87: Etymology 
201: verbal noun of جبر ( gābar ) 
211: Etymology
270: Egyptian Arabic verbal nouns 
282: Persian entries with etymology texts
```


## [2026-09-06T15:34:55.164Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D8%A8%D8%B1",
 "prompt": "Arabic جبر (jabr / jabara): etymology — is it inherited from a Semitic root, or borrowed from Aramaic? Also the meaning \"setting of broken bones, restoration\" and the mathematical sense. Quote."
}
```


### [2026-09-06T15:35:00.630Z] TOOL RESULT

```
# جبر (Jabr) - Etymology and Meanings

## Etymology
According to Wiktionary, the Arabic word **جَبَرَ (jabara)** is "cognate with Biblical Hebrew גָּבַר (gɔḇar)," indicating a shared Semitic origin rather than borrowing from Aramaic.

## Primary Meanings

The term has several distinct definitions:

1. **Medical**: "to set (a broken bone)" and "to restore"
2. **Linguistic**: "to force" or "to compel"
3. **Mathematical**: "algebra"
4. **Philosophical**: In Islamic philosophy, it refers to "determinism, fatalism, predestination"

## Linguistic Spread
The word spread across multiple languages through Arabic, appearing in Persian, Ottoman Turkish, and eventually European languages like Spanish (álgebra) and English (algebra), primarily through its mathematical sense.
```


## [2026-09-06T15:36:39.220Z] AGENT

Let me verify the key BQT footnote from the page image itself.


## [2026-09-06T15:36:40.018Z] TOOL CALL #57: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1774.png"
}
```


### [2026-09-06T15:36:40.601Z] TOOL RESULT

```

```


## [2026-09-06T15:36:40.598Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-06T15:37:31.239Z] TOOL CALL #58: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1774.vision.txt <<'EOF'\nBorhan-e Qate', ed. Mo'in, printed page ۱۷۷٤ = 1774 (vol. 3 scan, pdf page 571).\nRunning head (top right): گبرکی .  Read from the page image on 2026-09-06 for the verification of\nPDF page 230 (root J.b.r / Jabra), node #5 «گبر».\n\nBody (right column, continuation of the headword گبر which begins on p. 1773):\n  «... و خفتان ۱ - وهم بمعنی مغ باشد که آتش‌پرست است ۲ - ونام گیاهی نیز هست مانند زنجبیل که\n   آنرا در خراسان از زیر زمین برمی‌آورند و بجهت دفع سردی میخورند.»\n\nLeft column, separate headword:\n  «گبنا۷ - بفتح اول و سکون ثانی و نون بالف کشیده، بلغت زند و پازند بمعنی مرد باشد که در مقابل زن است.»\n\nFOOTNOTES (bottom of the page), verbatim as printed:\n\n۱ - باین معنی «کبر» (ه‌.م.) است.\n\n۲ - باین معنی بعقیدهٔ آقای پورداود از لغت آرامی گرفته شده هم‌ریشهٔ «کافر» عربی و بهمان معنی،\nو در ترکیه نیز «گور» گویند، و آن اصلاً بمعنی مطلق مشرک و بیرون از دین است، ولی در ایران\nاسلامی بزرتشتیان اطلاق شده و معناً درین استعمال نوعی استخفاف بکار رفته است. این کلمه با وجه\nاشتقاقی که برخی از پارسیان هند درین مورد گفته‌اند و آنرا از ریشهٔ gabra هزوارش و بمعنی «مرد»\nدانسته‌اند، هیچگونه ارتباطی ندارد. کلمهٔ «گبرک» نیز از همین لغت مرکب است با «ک» تصغیر و توهین،\nو «گبرکی» با یای حاصل مصدر بمعنی دین زرتشتی بکار رفته است.\nرک: مزدیسنا ص ۳۹۵-۶؛ کردی ghebir (بارمنی اطلاق شود)؛ کور gawr (آتش‌پرست)، gâvir (بروسی\nاطلاق شود)، ژابا ص ۳۵۷.\n\n۳ - از: گبرک (زرتشتی) (ه‌.م.) + ی (حاصل مصدر)، آیین زرتشتی (رک: ح۲) - ونیز از: گبرک\n(زرتشتی) + ی (نسبت)، آنچه منسوب بزرتشتیان باشد، ومخصوصاً ظرفی که شراب در آن کنند\n(چه زرتشتیان در ادوار اسلامی باده فروشی میکردند. رک: مزدیسنا ص ۲۶۶ ببعد)، بهر دو معنی:\n   دارم طمع ز جود تو یك گبرکی شراب / بفرست بنده را من از خوش مشتکی\n   ورلیست گبرکی، بفرست آنچه هست از آن / هرچ آید از تو، آن نبود غیر گبرکی .  «ابن یمین» فرمودهٔ «رشیدی»\n\n۷ - هز. gab(a)nâ (اغلب gabrâ خوانده شود) در پهلوی mart (مرد)، یونکر ص ۸۶.\n\n[Significance: footnote 2 explicitly REJECTS the derivation of گبر «Zoroastrian» from the\nhuzvarish ideogram GABRA \"man\" (the etymology proposed by some Indian Parsis — and the one\nNourai's chart draws), and follows Pur-e Davud in taking the word from an Aramaic word\ncognate with Arabic kāfir.  Footnote 7, on the separate headword گبنا, does identify the\nhuzvarish gab(a)nā / gabrā with Pahlavi mart \"man\" (after Junker p. 86).]\nEOF\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg230.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/230.png\nls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1774.vision.txt /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/230.png"
}
```


## [2026-09-06T15:37:32.315Z] TOOL CALL #59: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D8%AC%D8%A8%D8%B1\" --note 'page 230, node 1: Arabic jabara cognate with Hebrew gabar, not an Aramaic loan' 2>&1 | tail -2"
}
```


### [2026-09-06T15:37:32.934Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 65310 Sep  6 11:37 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/230.png
-rw-rw-r-- 1 sfmqrb sfmqrb  3319 Sep  6 11:37 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1774.vision.txt
```


### [2026-09-06T15:37:35.045Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a2ad7d793154fbcc.txt
```


## [2026-09-06T15:37:37.883Z] AGENT

Now I'll write the verification file.


## [2026-09-06T15:47:05.187Z] TOOL CALL #60: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk230.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nroot = {\n  \"entry\": 0,\n  \"root\": \"J.b.r; Jabra\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"Common (Proto-)Semitic root *g-b-r 'to be strong, prevail'; Aramaic/Syriac ḡəḇar 'was mighty', gaḇrā (emphatic st.) 'man'; Hebrew gāḇar / geḇer; Arabic ǧ-b-r (jabara 'to set a broken bone, restore, compel')\",\n  \"note\": (\"The root itself is real and the gloss is broadly right, but the box conflates three things. \"\n    \"(1) The FORM: Aramaic has g-, not j-. The Aramaic verb is gəḇar 'was mighty' and the noun gaḇrā 'man' \"\n    \"(emphatic state of gaḇr); the shape J.b.r / Jabra is the ARABIC reflex, since Proto-Semitic *g regularly \"\n    \"becomes Arabic ǧ (cf. Heb. gāmāl : Ar. jamal, Heb. gibbōr : Ar. jabbār). Nourai indexes the root under J \"\n    \"because his root list is alphabetical in Latin script, but as an 'Aramaic' headword *Jabra does not exist. \"\n    \"(2) The GLOSS: 'to reunite, join together' is the specifically Arabic sense of jabara (bone-setting, whence \"\n    \"al-jabr); the Aramaic/Hebrew side of the root means only 'be strong, prevail', whence 'man, hero'. \"\n    \"(3) The STRUCTURE: Klein 633, Nourai's own source, lists Hebrew, Aramaic-Syriac, Arabic, Akkadian and Ethiopic \"\n    \"forms as 'the related words', i.e. as COGNATES of a common Semitic root, not as descendants of Aramaic; \"\n    \"Wiktionary likewise makes Arabic jabara 'cognate with Biblical Hebrew גָּבַר'. So the arrows \"\n    \"Aramaic→Arabic (#1) and Aramaic→Hebrew (#6) are sister-language relations, not borrowings. Only two links on \"\n    \"this page are true Aramaic loans: Arabic/Persian جبروت jabarūt < Syriac gaḇrūṯā (#2), and Persian \"\n    \"گبر gabr < Aramaic gaḇrā (#5). No extraction errors: the printed page (pdf 230 = book p. 200) shows exactly \"\n    \"what the JSON has, including the garbled note '\\\"Jobrân\\\" is does not exist in Arabic.'\"),\n  \"note_fa\": (\"ریشه واقعی است ولی صورت آن در کتاب درست نوشته نشده است: ریشهٔ سامی مشترک *g-b-r «نیرومند بودن» \"\n    \"است که در آرامی و عبری با g می‌ماند (آرامی gəḇar «نیرومند بود»، gaḇrā «مرد») و تنها در عربی به ج بدل می‌شود \"\n    \"(مانند عبری gāmāl در برابر عربی جمل)؛ پس جعبهٔ «آرامی J.b.r / Jabra» درست‌نویسی نیست و باید g-b-r / gaḇrā می‌بود. \"\n    \"معنای «پیوستن، شکسته‌بندی» نیز ویژهٔ فعل عربی جبر است و در آرامی و عبری تنها «نیرومندی» و از آن «مرد، پهلوان» دیده می‌شود. \"\n    \"مهم‌تر آنکه کلاین (ص ۶۳۳)، همان مرجعی که نورایی آورده، صورت‌های عبری، آرامی، عربی، اکدی و حبشی را «واژه‌های خویشاوند» \"\n    \"(هم‌ریشه) می‌خواند نه بازماندهٔ آرامی؛ بنابراین پیکان‌های «آرامی ← عربی» و «آرامی ← عبری» را باید رابطهٔ هم‌ریشگی خواند، نه وام‌گیری. \"\n    \"در سراسر این صفحه فقط دو پیوند، وام‌گیری راستین از آرامی است: جبروت (< سریانی gaḇrūṯā) و گبر (< آرامی gaḇrā). \"\n    \"خطای خوانش اسکن در این صفحه دیده نشد.\"),\n  \"sources\": [W+\"%D8%AC%D8%A8%D8%B1\", W+\"%D8%AC%D8%A8%D8%B1%D9%88%D8%AA\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:633\", \"status\": \"supports\", \"note\": \"Klein 1966 s.v. 'Gabriel' (KLN_1966.txt leaf 342; the leaf spacing of the scan is ~1.9 printed pages per leaf, and 'algebra' at leaf 37 = p.48 and 'cherub' at leaf 98 = p.164 fit the same line, so leaf 342 = p.633 as Nourai cites): 'Heb. gebher derives from the base of the verb gabhar, \\\"was strong\\\", whence also gibbor \\\"strong, mighty; hero\\\", gebhir \\\"lord\\\" ... Cp. the related words: Aram.-Syr. gebhar, \\\"was mighty\\\", gebhar, gabhra, \\\"man\\\", Syr. gabbar, \\\"hero\\\", Arab. jabr, \\\"a strong, young man\\\", jabbar, \\\"tyrant\\\", Akkad. gapru, \\\"strong\\\", Ethiop. gabara, \\\"he acted\\\".' The page carries every form Nourai's root box claims, with Aramaic gaḇrā 'man' — but as a cognate list, and spelled with g-, not j-.\"},\n    {\"ref\": \"SOR:41\", \"status\": \"not_checked\", \"note\": \"SOR (K. Akhavan Zanjani) is unidentified in refs_online.json ('Table IV entry lost in OCR ... none online; title unidentified'); no copy exists to check.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. mard (PHD_mackenzie.txt line 3465)\", \"stance\": \"supports\", \"note\": \"'mard [GBRA < A gbrʾ; mltʿ | M m(y)rd, N ~] man' — MacKenzie derives the Pahlavi ideogram GBRA explicitly from Aramaic gbrʾ, confirming that the Aramaic word is gaḇrā 'man' (with g-) and that it was familiar in Iran as a written logogram.\"},\n    {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen (AFA.txt)\", \"stance\": \"silent\", \"note\": \"grep -i 'gabbar|gabbâr|gabrûtâ' returns nothing; Fraenkel does not treat the g-b-r family among his Aramaic loans into Arabic.\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an pp. 100-101 (FVQ_pages.txt l. 3846 ff.)\", \"stance\": \"partial\", \"note\": \"Jeffery treats only the derived name جبريل under this root; he says 'The ultimate origin, of course, is the Heb. גבריאל' and that the Arabic form came 'in its Syr. form' — i.e. the Semitic material of the root box is real, but Arabic took the NAME from Aramaic/Syriac, not the ROOT.\"}\n  ],\n  \"nodes\": []\n}\n\nN = root[\"nodes\"]\n\nN.append({\n  \"id\": 1, \"lang\": \"Arabic\", \"words\": \"J.b.r; Al-Jabr-w'al-Moˈqâbalah\".replace(\"ˈ\",\"\"),\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"Arabic جبر jabara 'to set (a broken bone), restore, make whole', hence also 'to compel, force', with the \"\n    \"verbal noun jabr. This is not a loan from Aramaic but the regular Arabic reflex of the common Semitic root *g-b-r \"\n    \"(Proto-Semitic *g > Arabic ǧ), as Wiktionary states outright ('cognate with Biblical Hebrew גָּבַר') and as Klein \"\n    \"implies by listing Arab. jabr among 'the related words' of Heb. gāḇar. Nourai's al-Jabr-w'al-Moqâbalah is the short \"\n    \"title of al-Khwārizmī's al-Kitāb al-muḵtaṣar fī ḥisāb al-jabr wa-l-muqābala, written at the Bayt al-Ḥikma in Baghdad \"\n    \"c. 820 CE: al-jabr = 'restoring' (moving a subtracted term to the other side of the equation), al-muqābala = \"\n    \"'balancing' (cancelling like terms). Nourai's description of the author is right — Muḥammad b. Mūsā al-Khwārizmī \"\n    \"(d. c. 850), from Khwārazm, i.e. an Iranian, and the book is indeed the founding treatise of the discipline. \"\n    \"The only correction is directional: Arabic j-b-r is Aramaic g-b-r's sister, not its child.\"),\n  \"derivation_fa\": (\"فعل عربی جَبَرَ «استخوان شکسته را بستن، سروسامان دادن» و از آن «واداشتن، زور گفتن»، مصدر جَبر. \"\n    \"این واژه وام‌واژهٔ آرامی نیست، بلکه بازتاب قاعده‌مند همان ریشهٔ سامی *g-b-r در عربی است زیرا g سامی آغازین در عربی به ج بدل می‌شود؛ \"\n    \"ویکی‌واژه آن را صریحاً «هم‌ریشه با عبری gāḇar» می‌خواند. عنوان «الجبر والمقابله» نام کوتاه کتاب «الکتاب المختصر فی حساب الجبر والمقابله» \"\n    \"اثر محمد بن موسای خوارزمی (درگذشته حدود ۲۳۵ ق) است که در بیت‌الحکمهٔ بغداد نوشته شد؛ «جبر» یعنی انتقال جملهٔ منفی به طرف دیگر معادله و \"\n    \"«مقابله» یعنی حذف جمله‌های همانند. ادعای نورایی دربارهٔ خود واژه و کتاب درست است، ولی جهت پیکان (آرامی ← عربی) باید به \"\n    \"هم‌ریشگی تصحیح شود.\"),\n  \"sources\": [W+\"%D8%AC%D8%A8%D8%B1\", \"https://www.etymonline.com/word/algebra\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:633\", \"status\": \"partial\", \"note\": \"KLN_1966.txt leaf 342 s.v. Gabriel has 'Arab. jabr, \\\"a strong, young man\\\", jabbar, \\\"tyrant\\\"' — but introduced by 'Cp. the related words', i.e. as cognates of Hebrew, not as Aramaic borrowings; and the sense given there is 'strong young man', not 'to reunite, force'.\"},\n    {\"ref\": \"FVA:67\", \"status\": \"not_checked\", \"note\": \"FVA = S.M. Nahvi, Farhang-e Vāžehā-ye ʿArabī dar Fārsī, 1368/1989; refs_online.json records that no digital copy exists on archive.org, ketabnak, noorlib or the open web (re-searched 2026-09).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 37 (= p.48) s.v. algebra\", \"stance\": \"supports\", \"note\": \"'algebra, n. — Fr. Arab. al-jabr (in vulgar pronunciation al-jebr), \\\"reunion (of broken parts in equations)\\\", short for al-jabr wʿal-muqabalah, \\\"reunion and comparison\\\", title of a work written by Mohammed ibn Musa al-Khowarizmi, great mathematician of the 9th cent. ... Al-jabr is formed fr. al-, \\\"the\\\", and jabr, \\\"reunion\\\", which is rel. to the verb ja'bara, \\\"he bound together, united\\\".' Exactly Nourai's wording of the title and the century.\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 631 (LKT.txt l. 1579)\", \"stance\": \"supports\", \"note\": \"'631. Ar. gabr: \\\"Wiederherstellung\\\", vollständig ist al-ǧabr waʾl-mukabala der Titel eines algebraischen Lehrbuches von Muhammad ibn Musa al-Hwarizmi, um 820 n. Chr. geschrieben, wörtlich: \\\"Wiederherstellung und Gegenüberstellung\\\" ... In der ursprünglichen Bedeutung des ar. Vbs. gabara \\\"wiederherstellen, einrichten\\\" ist noch sp. algebrista \\\"Chirurg\\\" erhalten.'\"},\n    {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-Fārisiyya al-Muʿarraba (AFM_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep 'الجبر' / 'جبروت' finds no entry — as expected, since Addi Shir collects PERSIAN words in Arabic and j-b-r is not one.\"}\n  ]\n})\n\nN.append({\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"jabr; jabarût; jobrân\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"All three are Arabic loans in Persian, and the extras جبّار jabbār (intensive faʿʿāl), اجبار ejbār \"\n    \"(form IV maṣdar) and مجبور majbūr (form I passive participle) are correctly grouped with them as regular Arabic \"\n    \"derivatives of the same root. جَبر jabr < Ar. jabr, giving in Persian both 'compulsion, force' (whence the kalām \"\n    \"term jabr 'predestination', jabrī, and the antonym pair jabr/eḵtiyār) and, as a clipping of jabr o moqābele, \"\n    \"'algebra' — exactly Mo'in's two senses. جَبَروت jabarūt is the one word here with a genuinely Aramaic history: \"\n    \"Wiktionary marks Arabic جبروت as 'Borrowed from Aramaic גַבְרוּתָא / ܓܕܝ ʿgaḇrūṯāʿ', its -ūt being the Aramaic \"\n    \"abstract suffix -ūṯā that also gave Arabic malakūt, lāhūt and kahanūt; so Persian jabarūt is an Aramaic > Arabic > \"\n    \"Persian relay, and Nourai's chart is right about it even if for the wrong reason. جُبران jobrān 'making good, \"\n    \"compensation' is the ordinary Arabic maṣdar jubrān of jabara — so the chart's NOTE, '\\\"Jobrân\\\" is does not exist in \"\n    \"Arabic', is simply WRONG: Wiktionary has Arabic جبران (and Egyptian Arabic gubrān 'verbal noun of جبر'), the \"\n    \"given name/surname Jubrān is the same word (Jubrān Ḵalīl Jubrān = Kahlil Gibran), and Mo'in himself tags the Persian \"\n    \"entry 'جبران: [ع.] (مص ع.) تلافی کردن' — '[Arabic], Arabic maṣdar'. Verdict is 'plausible' rather than \"\n    \"'confirmed' only because of that false note and because the parent link (#1) is a cognate relation.\"),\n  \"derivation_fa\": (\"هر سه واژه وام‌واژهٔ عربی در فارسی‌اند و افزوده‌های جبّار، اجبار و مجبور نیز مشتقات قاعده‌مند همین ریشه‌اند. \"\n    \"«جَبر» هم به معنی «زور، ناچاری» (و در کلام، جبر در برابر اختیار) است و هم کوتاه‌شدهٔ «جبر و مقابله» در ریاضی؛ معین هم همین دو معنا را می‌آورد. \"\n    \"«جَبَروت» تنها واژهٔ این گره است که ادعای آرامی‌بودن درباره‌اش راست است: خود عربی آن را از سریانی gaḇrūṯā وام گرفته و پسوند -ūt آن همان \"\n    \"پسوند مصدری آرامی -ūṯā است که در ملکوت، لاهوت و کهنوت نیز دیده می‌شود؛ پس جبروت از آرامی به عربی و از عربی به فارسی رسیده است. \"\n    \"اما یادداشت کتاب که «جُبران در عربی وجود ندارد» نادرست است: جُبران مصدر معروف فعل جبر است، نام «جبران خلیل جبران» هم همین است، و خود معین مدخل \"\n    \"«جبران: [ع.] (مص ع.) تلافی کردن» را عربی می‌داند.\"),\n  \"sources\": [W+\"%D8%AC%D8%A8%D8%B1%D9%88%D8%AA\", W+\"%D8%AC%D8%A8%D8%B1%D8%A7%D9%86\"],\n  \"ref_check\": [\n    {\"ref\": \"FVA:67\", \"status\": \"not_checked\", \"note\": \"Nahvi's Farhang-e Vāžehā-ye ʿArabī dar Fārsī has no digital copy anywhere (refs_online.json, re-searched 2026-09); the same page 67 is cited for node #1, so it is presumably the j-b-r entry.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Fārsī, 2-vol Adena condensation, MON_part1.txt ll. 47120-47134\", \"stance\": \"contradicts\", \"note\": \"The dictionary Nourai cites elsewhere flatly contradicts his note: 'جبران: [ع.] (مص ع.) تلافی کردن. (امص.) تلافی' — tagged [ع.] = Arabic, and labelled an Arabic maṣdar. The same column has جبر with the maths sense '(رض.) جبر و مقابله، بخشی از ریاضی که در آن برای حل مجهولات حروف و علامات را بجای اعداد بکار رود' and جبروت '[ع.] (ا.) قدرت، عظمت. عالم قدرت و عظمت الهی؛ مق. ناسوت'.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rišehā-ye Hend-o-Orūpāyī (incoming/ARY/ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep 'جبر' returns only the OCR noise 'بگبریم' — Aryanpur treats only Indo-European material, so Arabic loans are outside his scope.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 342 (p.633)\", \"stance\": \"partial\", \"note\": \"Klein knows Arab. jabbar 'tyrant' (Nourai's extra جبّار) and Syr. gabbar 'hero' side by side, which is the Aramaic-Arabic pair behind the Persian intensive; he says nothing about jabarūt or jubrān.\"}\n  ]\n})\n\nN.append({\n  \"id\": 3, \"lang\": \"French\", \"words\": \"algebre\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"French algèbre (the book prints 'algebre' without the grave accent), first attested in the 16th c. \"\n    \"(earlier algiebre), borrowed from Medieval Latin algebra, itself from Arabic al-jabr with the definite article \"\n    \"al- agglutinated onto the noun — the standard shape of Arabisms that entered Romance through Spain (alcool, \"\n    \"alchimie, alcade). The Latin form comes from the 12th-c. translations of al-Khwārizmī (Robert of Chester, Segovia \"\n    \"1145; Gerard of Cremona, Toledo). Pihan, whom Nourai cites, describes the semantics precisely: al-jabr is \"\n    \"'la réunion de plusieurs parties en un seul corps, ou l'action de ramener les fractions à un nombre intégral', \"\n    \"and the verb jabara 'consolider les différentes parties d'une chose brisée, par exemple, d'un os'.\"),\n  \"derivation_fa\": (\"فرانسهٔ algèbre (که کتاب بدون علامت «algebre» نوشته) وام‌گرفته از لاتین میانه algebra است که خود از عربی \"\n    \"«الجبر» گرفته شده، با حرف تعریف «ال» که مانند دیگر وام‌واژه‌های عربی در زبان‌های رمانس (alcool، alchimie) به خود واژه چسبیده است. \"\n    \"راه انتقال، ترجمه‌های لاتینی سدهٔ دوازدهم از کتاب خوارزمی در اسپانیا (رابرت چستری ۱۱۴۵، جرارد کرمونایی) بوده است. \"\n    \"پیهان در صفحهٔ ۲۶ دقیقاً همین را می‌گوید؛ ادعای نورایی درست است.\"),\n  \"sources\": [W+\"algebra\"],\n  \"ref_check\": [\n    {\"ref\": \"PHN:26\", \"status\": \"supports\", \"note\": \"Pihan p. 26 (PHN.txt l. 1346, the leaf whose running head reads '26 A'LG'): 'ALGÈBRE, s. f. (a.) [aldjebr] la réunion de plusieurs parties en un seul corps, ou l'action de ramener les fractions à un nombre intégral. Le verbe radical arabe [جبر] signifie proprement consolider les différentes parties d'une chose brisée, par exemple, d'un os. ... Les Arabes appellent aussi cette science [al-djebr wa-l-mouqâbalat] le rétablissement et la comparaison.' The cited page is exactly right and covers both the French word and the Arabic title.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 631 (LKT.txt l. 1579)\", \"stance\": \"supports\", \"note\": \"'Hieraus als Bezeichnung für eine bestimmte Rechnungsart sp. pg. álgebra, frz. algèbre, it. algebra; engl. algebra, dtsch. Algebra usw.' — French among the direct Romance continuations of Ar. al-ǧabr.\"},\n    {\"src\": \"LAM\", \"where\": \"Lammens, Remarques sur les mots français dérivés de l'arabe (LAM.txt ll. 1493-94)\", \"stance\": \"supports\", \"note\": \"'Algèbre. Etymol. bien connue. Esp. ptg. cat: algebra, basq: algebrea, de [al-]ǧabr réduction', with the footnote 'de l'arabe aldjabroun dit M. Brachet qui joint ensemble l'article...' — i.e. the agglutinated article.\"},\n    {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire étymologique des mots d'origine orientale (DEV.txt)\", \"stance\": \"silent\", \"note\": \"grep 'alg.bre' returns nothing; Devic's supplement to Littré covers only words Littré had left unexplained, and algèbre was not one.\"}\n  ]\n})\n\nN.append({\n  \"id\": 4, \"lang\": \"English\", \"words\": \"algebra\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"English algebra is first recorded in the 1550s and, tellingly, in the surgical sense 'bone-setting' before \"\n    \"the mathematical one — which shows it came through the learned Latin/Romance channel where both senses of Ar. al-jabr \"\n    \"travelled together (cf. Spanish algebrista 'bone-setter, surgeon'). Etymonline and Wiktionary take it from Medieval \"\n    \"Latin algebra directly; the stress moved from a-LGE-bra to AL-ge-bra in the 17th century. Nourai's French intermediary \"\n    \"is not the modern consensus, but it is not an invention either: Webster's New Twentieth Century Dictionary heads the \"\n    \"etymology '[Fr. algébre; Russ. algebra; Ar. al-jabr...]', while Funk & Wagnalls gives Italian instead ('< It. algebra, \"\n    \"< Ar. al-jebr') and Skeat gives Low Latin. Since Klein 48, the reference Nourai actually cites here, derives the English \"\n    \"word straight from Arabic with no Romance stage at all, the French arrow is at best one of several older opinions: \"\n    \"hence 'plausible'.\"),\n  \"derivation_fa\": (\"انگلیسی algebra نخستین بار در دههٔ ۱۵۵۰ م. و نخست به معنی «شکسته‌بندی» دیده می‌شود و سپس معنی ریاضی می‌گیرد؛ \"\n    \"همین دوگانگی معنایی نشان می‌دهد که واژه از راه لاتین میانه و زبان‌های رمانس آمده است (قیاس کنید اسپانیایی algebrista «جراح، شکسته‌بند»). \"\n    \"اتیمونلاین و ویکی‌واژه مستقیماً از لاتین میانه می‌گیرند و کلاین (ص ۴۸) که خود نورایی بدان ارجاع داده، راست از عربی می‌گیرد. \"\n    \"پس واسطهٔ فرانسه که در نمودار آمده رأی فرهنگ‌های کهن‌تر (وبستر) است و رأی امروزی نیست؛ با احتیاط پذیرفتنی است.\"),\n  \"sources\": [\"https://www.etymonline.com/word/algebra\", W+\"algebra\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:48\", \"status\": \"partial\", \"note\": \"KLN_1966.txt leaf 37 (= p.48): 'algebra, n. — Fr. Arab. al-jabr ...' — in Klein's notation 'Fr.' at the head of an etymology is 'From' (French is 'F.'), so Klein derives English algebra straight from Arabic and does NOT insert the French stage that Nourai's arrow requires. Everything else on that page (the title al-jabr w'al-muqabalah, al-Khowarizmi, the 9th century) supports the chart.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary, 2nd ed., vol. 1 (WEB_vol1.txt l. 5439) s.v. al'ge-bra\", \"stance\": \"supports\", \"note\": \"'[Fr. algébre; Russ. algebra; Ar. al-jabr, al-jebr, the reunion of broken parts, as the reduction of fractions to whole numbers; jabara, to reunite, bind together.]' — the one consulted dictionary that does put French between Arabic and English, as Nourai's chart does.\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary vol. 1 (FSD_vol1.txt l. 11623) s.v. algebra\", \"stance\": \"partial\", \"note\": \"'[< It. algebra, < Ar. al-jebr, binding together, < al, the, + jabara, reunite.]' — same Romance-mediation idea but with Italian, not French, as the immediate source.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary (SKT.txt l. 529) s.v. Algebra\", \"stance\": \"partial\", \"note\": \"'Algebra. (Low L. — Arab.) Low L. algebra, computation. — Arab. al, the; and jabr, setting, repairing; also, the reduction of fractions to integers in arithmetic ... — Arab. root jabara, to set, consolidate.' Skeat routes it through Low (Medieval) Latin with no French or Italian step.\"}\n  ]\n})\n\nN.append({\n  \"id\": 5, \"lang\": \"Persian\", \"words\": \"gabr\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"New Persian گَبر gabr 'Zoroastrian; (pejoratively) infidel', with the derivatives the chart lists — گبرک \"\n    \"gabrak (with the diminutive/contemptuous -ak), گبرکان gabrakān and گبرکی gabrakī 'the Zoroastrian religion; the \"\n    \"wine-vessel of the Zoroastrians' — and attested from the earliest New Persian (Šāh-nāma, Balʿamī, Sanāʼī, and the \"\n    \"ʿOnṣorī line quoted in the chart). Nourai's derivation from Aramaic gaḇrā 'man' is the one modern Iranian studies \"\n    \"accepts: Encyclopaedia Iranica (Shaki, s.v. GABR) opens 'a New Persian term deriving, in all likelihood, from \"\n    \"Aramaic GBRʾ / gabrā (lit. man), which in the Sasanian period was used to indicate the free peasants in the region \"\n    \"of Mesopotamia', and Wiktionary has 'Borrowed from Aramaic ސދރ (gbrʾ /gaḏrā/, \\\"man; person\\\"), reflected in the Middle \"\n    \"Persian logogram (huzvarishn) GBRA (mard, \\\"man\\\")'. The same Aramaic word is what MacKenzie records as the Pahlavi \"\n    \"ideogram: 'mard [GBRA < A gbrʾ] man'. The route is therefore: Aramaic gaḇrā 'man' > a designation of the (Zoroastrian) \"\n    \"rural population of Aramaic-speaking Sasanian Mesopotamia > after the conquest, the word converted Persians used of \"\n    \"their Zoroastrian compatriots > pejorative 'infidel', replaced in modern usage by zartoštī. From Persian it went on to \"\n    \"Turkish gâvur/gaur (> giaour) and, directly, to French guèbre / English gueber. \"\n    \"THE CHART'S OWN NOTE IS ACCURATE AND WORTH KEEPING: Borhan-e Qāteʿ p. 1774, footnote 2 (Mo'in, following Pūr-e \"\n    \"Dāvūd) says the word 'has no connection whatever' with the huzvāriš gabra 'man' and takes it instead from an Aramaic \"\n    \"word cognate with Arabic kāfir. Lokotsch no. 632 says the same after Rückert, and Horn (Grundriss p. 210 n.) warns that \"\n    \"Pahl. gabrā '(Semitic! meaning only \\\"man\\\")' should not have been set up as the base form. But Iranica answers this \"\n    \"directly — 'there is no unusual sound in kāfer that would require phonetic modification', and 'kāfer as a generic word \"\n    \"could hardly refer to a specific revealed religion such as Zoroastrianism' — and Wiktionary calls the kāfir etymology \"\n    \"'problematic on phonetic and semantic grounds'. Modern scholarship is on Nourai's side.\"),\n  \"derivation_fa\": (\"«گَبر» در فارسی نو به معنی «زرتشتی؛ (به تحقیر) کافر» است، با مشتقات گبرک (پسوند تصغیر و توهین)، گبرکان و گبرکی، \"\n    \"و از کهن‌ترین متن‌های فارسی (شاهنامه، تاریخ بلعمی، سنایی و همین بیت عنصری) دیده می‌شود. ریشه‌شناسی‌ای که نورایی آورده — از آرامی \"\n    \"gaḇrā «مرد» — همان است که ایرانیکا (مقالهٔ شکی) و ویکی‌واژه می‌پذیرند: همین واژه در خط فارسی میانه هزوارش GBRA است که mard خوانده \"\n    \"می‌شده (مکنزی: mard [GBRA < A gbrʾ]) و در میان‌رودان روزگار ساسانی بر دهقانان آزاد اطلاق می‌شده؛ سپس در دوران اسلامی ایرانیان نومسلمان آن را \"\n    \"برای هم‌میهنان زرتشتی خود به کار بردند و معنا به تحقیر گرایید؛ از فارسی به ترکی gâvur (و از آن giaour) و بی‌واسطه به فرانسهٔ guèbre رفته است. \"\n    \"یادداشت خود نورایی درست است: حاشیهٔ ۲ برهان قاطع ص ۱۷۷۴ (معین به پیروی پورداود) می‌نویسد این کلمه «با وجه اشتقاقی که برخی از پارسیان هند \"\n    \"گفته‌اند و آن را از ریشهٔ gabra هزوارش و بمعنی مرد دانسته‌اند، هیچگونه ارتباطی ندارد» و آن را هم‌ریشهٔ «کافر» عربی می‌داند؛ لوکوچ (شمارهٔ ۶۳۲) نیز همین را \"\n    \"می‌گوید و هرن (ص ۲۱۰) هشدار داده است که gabrā پهلوی را نباید صورت اصلی گرفت. اما ایرانیکا پاسخ می‌دهد که در «کافر» هیچ آوای دشواری \"\n    \"نیست که دگرگونی را ایجاب کند و «کافر» واژه‌ای عام است و بر دینی معیّن مانند زرتشتی دلالت نمی‌کند؛ پس پژوهش امروزی جانب نورایی را می‌گیرد.\"),\n  \"sources\": [\"https://www.iranicaonline.org/articles/gabr/\", W+\"%DA%AF%D8%A8%D8%B1\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:3193\", \"status\": \"supports\", \"note\": \"The 6-vol Amir Kabir Farhang is not digitised, but the Adena 2-vol condensation of Mo'in (MON_part2.txt l. 29922) has s.v. گبر: '[آرا. قس. ع. کافر] (ص. ا.) کافر، ملحد، بت‌پرست، زردشتی، زرتشتی، مجوس' — the tag 'آرا.' is Mo'in's abbreviation for Aramaic, so his own dictionary DOES derive گبر from Aramaic (merely adding 'cf. Arabic kāfir'), exactly as Nourai's chart claims. Note the internal tension with his Borhan footnote (see consulted/BQT).\"},\n    {\"ref\": \"SOR:41\", \"status\": \"not_checked\", \"note\": \"SOR is the unidentified reference of Table IV (refs_online.json: 'title unidentified, none online').\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qāteʿ ed. Mo'in, printed p. 1774 = vol. 3 scan pdf p. 571, footnote 2 (image read and saved to sources/refs/ocr/BQT/1774.vision.txt)\", \"stance\": \"contradicts\", \"note\": \"'باین معنی بعقیدهٔ آقای پورداود از لغت آرامی گرفته شده هم‌ریشهٔ «کافر» عربی و بهمان معنی ... این کلمه با وجه اشتقاقی که برخی از پارسیان هند درین مورد گفته‌اند و آنرا از ریشهٔ gabra هزوارش و بمعنی «مرد» دانسته‌اند، هیچگونه ارتباطی ندارد.' — an explicit rejection of Nourai's arrow, so his own note 'BQT:1774 does not agree with this derivation' is exactly right. (Footnote 7 on the same page, for the separate headword گبنا, does give 'هز. gab(a)nâ (اغلب gabrâ خوانده شود) در پهلوی mart (مرد)، یونکر ص ۸۶'.)\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 632 (LKT.txt l. 1580)\", \"stance\": \"contradicts\", \"note\": \"'632. Pers. gäbr: \\\"Feueranbeter\\\" [wohl aus ar. käfir \\\"Ungläubiger\\\", ... nach Rückert in ZDMG X, 133]; erst hieraus [und nicht unmittelbar aus dem ar. Grundwort] tk. gjawr, gjaur ... hieraus it. giaurro, frz. engl. giaour, dtsch. Giaur; poln. giaur. Dagegen frz. guebre, engl. gueber, guebre, dtsch. Geber \\\"der Feueranbeter [Parsi]\\\" unmittelbar aus dem pers. Grundwort.' Lokotsch prefers kāfir but confirms the whole downstream European history from Persian gabr.\"},\n    {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie p. 210 note (HRN.txt l. 8158-8161)\", \"stance\": \"partial\", \"note\": \"'Beiläufig bemerkt, ist türk. LW. gʿaur wohl nicht arab. kāfir (Hübschmann unter oss. d. gaur ... S. 123), sondern vielmehr neupers. gebr, gabr (vergl. Geiger, bal. LW. gaur, No. 81, wo allerdings phlv. gabrā (semitisch!, nur \\\"Mann\\\" bedeutend) nicht als Grundform stehen durfte).' Horn rejects kāfir for the Turkish word and traces it to NP gabr — but he is unwilling to make Pahlavi/Aramaic gabrā the source form, so he is only half with Nourai.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. mard (PHD_mackenzie.txt l. 3465)\", \"stance\": \"supports\", \"note\": \"'mard [GBRA < A gbrʾ; mltʿ | M m(y)rd, N ~] man' — the Aramaic word Nourai starts from was demonstrably current in Sasanian Iran as the standard logogram for 'man', which is what makes the borrowing possible.\"}\n  ]\n})\n\nN.append({\n  \"id\": 6, \"lang\": \"Hebrew\", \"words\": \"gabhar; Gabhri-ěl\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"Hebrew גָּבַר gāḇar 'was strong, prevailed', with the nouns גֶּבֶר geḇer 'man (as the strong one)', גִבּוֹר \"\n    \"gibbōr 'hero', גְבוּרָה gəḇūrāh 'might'; and the theophoric name גַּבְרִיאֵל Gaḇrīʾel = geḇer + ʾēl, 'man/hero of God', \"\n    \"the angel of Daniel 8:16 and 9:21. Nourai's forms and glosses are Klein's verbatim. The one correction is the \"\n    \"direction of the arrow: Hebrew is Aramaic's sister, not its daughter, and Klein presents the Aramaic-Syriac forms as \"\n    \"'the related words' to the Hebrew ones. Both continue the same Northwest-Semitic root; there is no borrowing to draw.\"),\n  \"derivation_fa\": (\"عبری gāḇar «نیرومند بود، چیره شد» و از آن geḇer «مرد»، gibbōr «پهلوان»؛ و نام Gaḇrīʾēl مرکب از geḇer و ʾēl \"\n    \"«خدا» یعنی «مرد/پهلوان خدا»، که در کتاب دانیال (۸:۱۶ و ۹:۲۱) آمده است. صورت‌ها و معناهای نورایی عیناً از کلاین گرفته شده و درست است؛ \"\n    \"تنها ایراد آن است که عبری خواهر آرامی است نه برآمده از آن؛ کلاین نیز صورت‌های آرامی–سریانی را زیر عنوان «واژه‌های خویشاوند» می‌آورد. \"\n    \"پس ادعا با احتیاط پذیرفتنی است: واژه‌ها درست، پیکان نادرست.\"),\n  \"sources\": [\"https://www.etymonline.com/word/Gabriel\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:633\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 342: 'Gabriel, 1) masc. PN.; 2) in the Bible, name of an angel. — Heb. Gabhriʾel, lit. \\\"man of God\\\", fr. gebher, \\\"man\\\", and El, \\\"God\\\". Heb. gebher derives from the base of the verb gabhar, \\\"was strong\\\" ...' — word for word what the node says; only the parent link (Aramaic → Hebrew) goes beyond Klein, who calls the Aramaic forms 'related'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an p. 100 (FVQ_pages.txt l. 3859)\", \"stance\": \"supports\", \"note\": \"'The ultimate origin, of course, is the Heb. [גבריאל], and in Dan. viii, 16; ix, 21, Gabriel is one of the high angels and the agent of Revelation, just as he is in the Qur'an.'\"},\n    {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict. vol. 1 (WEB_vol1.txt l. 79282) s.v. Ga'bri-el\", \"stance\": \"silent\", \"note\": \"'Ga'bri-el, n. in the Bible, one of the seven archangels, the angel of the Annunciation ... Luke i. 26. Dan. viii. ix.' — the entry gives the biblical references but no etymology.\"}\n  ]\n})\n\nN.append({\n  \"id\": 7, \"lang\": \"Arabic\", \"words\": \"Jebraîl\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"Arabic جبريل Jibrīl / جبرائيل Jibrāʾīl, the angel of revelation in Q 2:97-98 and 66:4. Ultimately the Hebrew \"\n    \"name, as Nourai draws, but Jeffery shows the immediate source was Aramaic, not Hebrew: the early Arabic authorities \"\n    \"record a whole spread of spellings, which as-Suyūṭī took as proof of foreign origin, and 'the form which is found in \"\n    \"the Christian Palestinian dialect gives us the closest approximation to the usual Arabic form'; Jeffery concludes \"\n    \"'the probabilities are that it came to him in its Syr. form'. Phonetically the Arabic reflects Aramaic Gaḇrīʾēl with \"\n    \"the initial g → ǧ substitution normal for names entering Arabic, and the short variant Jibrīl drops the medial \"\n    \"hamza; the -īl termination was already a familiar angel-name ending (Mīkāʾīl, Isrāfīl). Nourai's arrow is right in \"\n    \"substance, one language short in route.\"),\n  \"derivation_fa\": (\"«جبریل / جبرائیل» عربی، نام فرشتهٔ وحی در قرآن (بقره ۹۷–۹۸ و تحریم ۴)، در نهایت همان نام عبری Gaḇrīʾēl است، \"\n    \"اما جفری (واژگان بیگانهٔ قرآن، ص ۱۰۰–۱۰۱) نشان می‌دهد که واسطه، آرامی مسیحی (سریانی) بوده است نه عبری مستقیم: اختلاف فراوان ضبط‌ها گواه \"\n    \"بیگانگی واژه است و نزدیک‌ترین صورت به عربی، صورت آرامی فلسطینی مسیحی است. در عربی g آغازین به ج بدل شده و پایانهٔ ʾīl به قیاس \"\n    \"میکائیل و اسرافیل ماندگار شده است. ادعای نورایی در اصل درست است ولی یک حلقه (سریانی) افتاده است.\"),\n  \"sources\": [W+\"%D8%AC%D8%A8%D8%B1%D8%A7%D8%A6%D9%8A%D9%84\"],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node (refs=None in the JSON, and the printed box on p. 200 indeed carries no book icon).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an pp. 100-101 (FVQ_pages.txt ll. 3846-3905)\", \"stance\": \"partial\", \"note\": \"'There was considerable uncertainty among the early authorities as to the spelling of the name ... as-Suyuti, Muẓhir i, 140, notes that these variants point to its non-Arabic origin ... The ultimate origin, of course, is the Heb. ... There is, however, the possibility that the Gabriel of the Qur'an is of Christian rather than Jewish origin, and the form which is found in the Christian Palestinian dialect gives us the closest approximation to the usual Arabic form ... the probabilities are that it came to him in its Syr. form.' Supports Hebrew as ultimate origin, corrects the immediate source to Syriac/Christian Aramaic.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 342 s.v. Gabriel\", \"stance\": \"silent\", \"note\": \"Klein traces only the English name and its Hebrew source; he says nothing about the Arabic form Jibrīl.\"}\n  ]\n})\n\nN.append({\n  \"id\": 8, \"lang\": \"Persian\", \"words\": \"Jebreîl\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"Persian جبرئیل Jebraʾīl / Jebreʾīl, taken over from Qur'ānic Arabic Jibrāʾīl along with the rest of the Islamic \"\n    \"angelology; the Persian spelling keeps the Arabic hamza on a yā seat (ئ) and the Persian pronunciation lowers the \"\n    \"Arabic short i of the first syllable to e, as regularly in Arabic loans (جبر jabr, مجبور majbūr). Mo'in lists exactly \"\n    \"the three Persian variants the chart implies. Nourai's gloss 'man of God' is the Hebrew etymological sense carried \"\n    \"over, not a Persian one. This is an ordinary, uncontroversial Arabic > Persian religious loan.\"),\n  \"derivation_fa\": (\"«جبرئیل» در فارسی وام‌واژهٔ عربی قرآنی جبرائیل است که همراه با دیگر نام‌های فرشتگان به فارسی راه یافته؛ \"\n    \"همزه بر کرسی یاء (ئ) نوشته می‌شود و ِ کوتاه عربی در فارسی به ِ/َ بدل می‌شود (مانند جَبر و مَجبور). معین هر سه گونهٔ جبرئیل، جبرائیل و جبریل را \"\n    \"می‌آورد. معنای «مرد خدا» معنای ریشه‌شناختی عبری است نه فارسی. ادعای نورایی درست است.\"),\n  \"sources\": [W+\"%D8%AC%D8%A8%D8%B1%D8%A7%D8%A6%D9%8A%D9%84\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:1215\", \"status\": \"supports\", \"note\": \"The 6-vol Farhang is not digitised, so the page number itself cannot be checked; the Adena 2-vol condensation of Mo'in (MON_part1.txt l. 47139) has 'جبرئیل: [- جبرائیل - جبریل] (اخ.) یکی از فرشتگان مقرب. (ا.) دل که به زعم صوفیان مهبط انوار الهی و محل وحی و الهام او است' — the headword, the variants and the sense are Nourai's.\"},\n  ],\n  \"consulted\": [\n    {\"src\": \"FVQ\", \"where\": \"Jeffery pp. 100-101\", \"stance\": \"supports\", \"note\": \"Establishes the Arabic Qur'ānic form that Persian borrowed; see node #7.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur (incoming/ARY/ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep 'جبر' finds no entry; his dictionary covers only Indo-European roots of Persian.\"}\n  ]\n})\n\nN.append({\n  \"id\": 9, \"lang\": \"Latin\", \"words\": \"\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"An empty pass-through box for Latin Gabriēl, the form of the Vulgate (Dan. 8:16; Luke 1:19, 26) and of all \"\n    \"Western ecclesiastical usage. Latin did not, however, take the name from Hebrew directly, as the chart's arrow implies: \"\n    \"the Septuagint rendered גַּבְרִיאֵל as Γαβριήλ, the Greek New Testament kept Γαβριήλ in Luke 1, and Jerome carried the \"\n    \"Greek-mediated spelling into the Vulgate — Greek β for Hebrew ḇ and η for ē are the give-away. Etymonline says the name \"\n    \"reached English 'through Greek and Latin intermediaries'. So the box is right as far as it goes; a Greek box is missing.\"),\n  \"derivation_fa\": (\"جعبهٔ خالی لاتین برای Gabriēl است، صورت وولگاتا (دانیال ۸:۱۶؛ لوقا ۱:۱۹ و ۲۶) و همهٔ کلیسای غرب. \"\n    \"اما لاتین این نام را بی‌واسطه از عبری نگرفته است: ترجمهٔ سبعینیه آن را Γαβριήλ آورده، عهد جدید همین را نگاه داشته و هیرونیموس آن را \"\n    \"به لاتین برده است؛ بتای یونانی در برابر ḇ عبری و اتای یونانی در برابر ē گواه این واسطه است. پس در نمودار یک حلقهٔ یونانی افتاده است.\"),\n  \"sources\": [\"https://www.etymonline.com/word/Gabriel\"],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book (refs=None), so there is nothing of Nourai's to check here.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 342 s.v. Gabriel\", \"stance\": \"partial\", \"note\": \"Klein goes straight from English to 'Heb. Gabhriʾel' without naming a Latin or Greek stage — he neither supports nor denies the Latin box; his practice with biblical names is to give the ultimate Hebrew only.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, Dictionnaire étymologique de la langue latine (LAT.txt)\", \"stance\": \"silent\", \"note\": \"No entry: Ernout-Meillet excludes biblical proper names from the Latin lexicon they treat.\"}\n  ]\n})\n\nN.append({\n  \"id\": 10, \"lang\": \"French\", \"words\": \"\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"Empty pass-through box for French Gabriel, the ecclesiastical Latin name adopted unchanged in spelling from \"\n    \"the Middle Ages onward (through the cult of the archangel and the Annunciation), pronounced [ɡabʁijel]; it is one of \"\n    \"the standard French baptismal names and the form from which the modern Persian re-borrowing in node #11 is taken.\"),\n  \"derivation_fa\": (\"جعبهٔ خالی فرانسه برای Gabriel است؛ همان نام لاتینی کلیسایی است که از سده‌های میانه بی تغییر در املا به فرانسه راه یافته \"\n    \"و [ɡabʁijel] تلفظ می‌شود؛ همین صورت است که در ۱۰۰ سال اخیر به صورت «گابریل» به فارسی رسیده است. ادعای نورایی درست است.\"),\n  \"sources\": [\"https://www.etymonline.com/word/Gabriel\"],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"No reference is printed in this box (refs=None).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire étymologique des mots d'origine orientale (DEV.txt)\", \"stance\": \"silent\", \"note\": \"grep finds only 'GIAOUR' and 'GUÈBRE' (both from Persian gabr, see node #5); the personal name Gabriel is not an orientalism and is absent.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 342\", \"stance\": \"silent\", \"note\": \"Klein names no French stage for Gabriel.\"}\n  ]\n})\n\nN.append({\n  \"id\": 11, \"lang\": \"Persian\", \"words\": \"Gâbrîyel\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"Persian گابریل Gābriyel is a modern re-borrowing of the WESTERN personal name (used of Europeans and Latin \"\n    \"Americans — گابریل گارسیا مارکز), not the inherited Islamic form, which is جبرئیل (node #8). It is therefore a \"\n    \"genuine doublet: the same Hebrew name reaching Persian twice, once through Syriac and Arabic in the 7th-8th c. and \"\n    \"once through French/English in the modern period. The spelling shows the modern route: alef for the stressed European \"\n    \"[a] (گا- rather than جب-), initial g rather than j because it is no longer mediated by Arabic phonology, and -یل \"\n    \"for [jel]. Nourai's French parent is the likeliest single source for Persian, though English has reinforced it. \"\n    \"'Plausible' rather than 'confirmed' because the claim rests on a reference that cannot be reached: he cites 'MON' \"\n    \"with no page, and Mo'in's aʿlām volumes (5-6), where such names stand, are not digitised.\"),\n  \"derivation_fa\": (\"«گابریل» وام‌گیری تازهٔ نام اروپایی است (مانند گابریل گارسیا مارکز) و نه صورت دیرینهٔ اسلامی که «جبرئیل» باشد؛ \"\n    \"پس این دو در فارسی «دوگانه» (doublet) اند: یکی در سدهٔ نخست از راه سریانی و عربی و دیگری در دوران معاصر از راه فرانسه و انگلیسی. \"\n    \"املای واژه خود گواه راه تازه است: الف برای [a] تکیه‌دار، گاف به جای جیم (زیرا دیگر از مجرای آواشناسی عربی نگذشته) و پایانهٔ «یل». \"\n    \"چون نورایی فقط «MON» بدون شمارهٔ صفحه آورده و جلدهای اعلام معین در دسترس نیست، این حلقه تنها با احتیاط پذیرفتنی است.\"),\n  \"sources\": [\"https://www.etymonline.com/word/Gabriel\"],\n  \"ref_check\": [\n    {\"ref\": \"MON\", \"status\": \"not_checked\", \"note\": \"Cited without a page. Proper names live in Mo'in vols. 5-6 (aʿlām), which refs_online.json records as not digitised anywhere (vajehyab's Mo'in has no proper-name entries); the 2-vol Adena condensation available locally has no گابریل headword (grep of MON_part1/2).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"Mo'in 2-vol Adena condensation, MON_part1.txt / MON_part2.txt\", \"stance\": \"silent\", \"note\": \"grep 'گابریل' returns nothing; only 'جبرئیل: [- جبرائیل - جبریل]' is present (l. 47139), i.e. the condensation keeps the Islamic form but not the European one.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur (incoming/ARY/ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"No entry for گابریل; foreign personal names are outside the scope of an Indo-European root dictionary.\"}\n  ]\n})\n\nN.append({\n  \"id\": 12, \"lang\": \"English\", \"words\": \"Gabriel\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"English Gabriel, in the language since the Old English gospels and general as a baptismal name from the \"\n    \"Middle Ages, from Ecclesiastical Latin Gabriēl < Greek Γαβριήλ < Hebrew Gaḇrīʾel 'man of God'. The chart's Latin → \"\n    \"English arrow is the standard account (Etymonline: 'entered English through Greek and Latin intermediaries'); \"\n    \"Klein 633, Nourai's reference, gives the ultimate Hebrew source and the exact gloss 'man of God' that both this node \"\n    \"and node #6 carry.\"),\n  \"derivation_fa\": (\"انگلیسی Gabriel از لاتین کلیسایی Gabriēl، از یونانی Γαβριήλ، از عبری Gaḇrīʾēl «مرد خدا»؛ از ترجمهٔ انجیل‌های \"\n    \"انگلیسی کهن در زبان است و از سده‌های میانه نام تعمید شده است. کلاین (ص ۶۳۳) همین معنا و همین ریشه را می‌دهد؛ ادعای نورایی درست است.\"),\n  \"sources\": [\"https://www.etymonline.com/word/Gabriel\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:633\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 342: 'Gabriel, 1) masc. PN.; 2) in the Bible, name of an angel. — Heb. Gabhriʾel, lit. \\\"man of God\\\", fr. gebher, \\\"man\\\", and El, \\\"God\\\".' The English headword is exactly what the node has; Klein does not spell out the Latin/Greek stages but does not exclude them.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict. vol. 1 (WEB_vol1.txt l. 79282)\", \"stance\": \"silent\", \"note\": \"'Ga'bri-el, n. in the Bible, one of the seven archangels ...' — definition only, no etymology; the neighbouring 'Ga'bri-el-ite' entry shows the name was productive in English.\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dict. vol. 2 (FSD_vol2.txt l. 28776)\", \"stance\": \"silent\", \"note\": \"The g-a-b column has 'Gabriel ratchet', 'gabbro', etc.; no etymologised headword Gabriel was found by grep.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary (SKT.txt)\", \"stance\": \"silent\", \"note\": \"Skeat excludes personal names; no entry.\"}\n  ]\n})\n\ndoc = {\n  \"pdf_page\": 230,\n  \"book_page\": 200,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [root]\n}\n\nimport io\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-230.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk230.py"
}
```


### [2026-09-06T15:47:07.785Z] TOOL RESULT

```
ok
```


## [2026-09-06T15:47:11.225Z] TOOL CALL #61: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-230.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 230"
}
```


### [2026-09-06T15:47:13.247Z] TOOL RESULT

```
JSON OK
nodes verified: 12/12
node verdicts: {'plausible': 7, 'confirmed': 5}
root verdicts: {'plausible': 1}
ref checks: {'partial': 2, 'not_checked': 7, 'supports': 5}
books consulted: {'supports': 8, 'silent': 14, 'contradicts': 3, 'partial': 6} | by book: {'KLN': 5, 'LKT': 3, 'ARY': 3, 'WEB': 3, 'FVQ': 3, 'MON': 2, 'DEV': 2, 'FSD': 2, 'SKT': 2, 'AFM': 1, 'LAM': 1, 'BQT': 1, 'HRN': 1, 'PHD': 1, 'LAT': 1}
```


## [2026-09-06T15:47:20.774Z] TOOL CALL #62: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-230.json'\nd=json.load(open(p,encoding='utf-8'))\nns={n['id']:n for n in d['entries'][0]['nodes']}\nprint(repr(ns[1]['words']))\nfor i in (2,5):\n    for s in ns[i]['derivation'].split('. '):\n        if 'ސ' in s or 'ܓ' in s or 'gaḏ' in s: print(i, s)\nEOF"
}
```


### [2026-09-06T15:47:22.455Z] TOOL RESULT

```
"J.b.r; Al-Jabr-w'al-Moqâbalah"
2 جَبَروت jabarūt is the one word here with a genuinely Aramaic history: Wiktionary marks Arabic جبروت as 'Borrowed from Aramaic גַבְרוּתָא / ܓܕܝ ʿgaḇrūṯāʿ', its -ūt being the Aramaic abstract suffix -ūṯā that also gave Arabic malakūt, lāhūt and kahanūt; so Persian jabarūt is an Aramaic > Arabic > Persian relay, and Nourai's chart is right about it even if for the wrong reason
5 man), which in the Sasanian period was used to indicate the free peasants in the region of Mesopotamia', and Wiktionary has 'Borrowed from Aramaic ސދރ (gbrʾ /gaḏrā/, "man; person"), reflected in the Middle Persian logogram (huzvarishn) GBRA (mard, "man")'
```


## [2026-09-06T15:47:30.431Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-230.json'\nd=json.load(open(p,encoding='utf-8'))\nns={n['id']:n for n in d['entries'][0]['nodes']}\na=\"Wiktionary marks Arabic جبروت as 'Borrowed from Aramaic גַבְרוּתָא / ܓܕܝ ʿgaḇrūṯāʿ'\"\nb=\"Wiktionary marks Arabic جبروت as 'Borrowed from Aramaic גַּבְרוּתָא / Syriac gaḇrūṯā'\"\nassert a in ns[2]['derivation']\nns[2]['derivation']=ns[2]['derivation'].replace(a,b)\nc='Wiktionary has \\'Borrowed from Aramaic ސދރ (gbrʾ /gaḏrā/, \"man; person\"), reflected in the Middle Persian logogram (huzvarishn) GBRA (mard, \"man\")\\''\ne='Wiktionary has \\'Borrowed from Aramaic gbrʾ /gaḇrā/, \"man; person\", reflected in the Middle Persian logogram (huzvarishn) GBRA (mard, \"man\"). The Persian word was probably used in pre-Islamic Persia to refer to some Zoroastrians in Mesopotamia (inhabited by many Aramaeans)\\''\nassert c in ns[5]['derivation']\nns[5]['derivation']=ns[5]['derivation'].replace(c,e)\nwith io.open(p,'w',encoding='utf-8') as f:\n    json.dump(d,f,ensure_ascii=False,indent=2); f.write('\\n')\nprint('fixed')\nEOF\npython3 -m json.tool data/verification/page-230.json >/dev/null && python3 tools/verify_check.py 230"
}
```


### [2026-09-06T15:47:32.959Z] TOOL RESULT

```
fixed
nodes verified: 12/12
node verdicts: {'plausible': 7, 'confirmed': 5}
root verdicts: {'plausible': 1}
ref checks: {'partial': 2, 'not_checked': 7, 'supports': 5}
books consulted: {'supports': 8, 'silent': 14, 'contradicts': 3, 'partial': 6} | by book: {'KLN': 5, 'LKT': 3, 'ARY': 3, 'WEB': 3, 'FVQ': 3, 'MON': 2, 'DEV': 2, 'FSD': 2, 'SKT': 2, 'AFM': 1, 'LAM': 1, 'BQT': 1, 'HRN': 1, 'PHD': 1, 'LAT': 1}
```


## [2026-09-06T15:47:54.980Z] AGENT

Page 230 (book p. 200) verified — `data/verification/page-230.json`, `verify_check.py 230` shows 0 PROBLEM lines.

**Counts** — 1 entry (3 redirects skipped, Jol/Jor/Jur → Ul). Root: 1 plausible. Nodes 12/12: 5 confirmed, 7 plausible, 0 disputed, 0 transcription_suspect, 0 unverified. Ref checks: 5 supports, 2 partial, 7 not_checked (FVA and SOR have no digital copy anywhere; four boxes carry no refs at all).

**Main findings**
- **Root "Aramaic J.b.r; Jabra"** — real Semitic root but mis-shaped: Aramaic has g-, not j- (gəḇar / gaḇrā); J.b.r is the Arabic reflex. Also "to reunite, join together" is only the Arabic sense. Klein 633, Nourai's own source, lists Hebrew/Aramaic/Arabic/Akkadian/Ethiopic as *cognates* ("Cp. the related words"), so the Aramaic→Arabic (#1) and Aramaic→Hebrew (#6) arrows are sister-language relations, not borrowings. Only two links on the page are true Aramaic loans: jabarūt (#2) and gabr (#5).
- **#2 Persian jobrân — the chart's NOTE is wrong.** «جُبران» is an ordinary Arabic maṣdar of jabara; Wiktionary has Arabic جبران, Mo'in himself tags the Persian entry "[ع.] (مص ع.) تلافی کردن", and the name Jubrān Khalīl Jubrān (Kahlil Gibran) is the same word. Worth correcting in the data or flagging to readers.
- **#5 Persian gabr — Nourai is right and his warning note is right too.** Encyclopaedia Iranica (Shaki) and Wiktionary both derive گبر from Aramaic gaḇrā "man" (= the Pahlavi huzvārišn GBRA, MacKenzie "mard [GBRA < A gbrʾ]"). BQT:1774 fn. 2 (Mo'in after Pūr-e Dāvūd) explicitly says the word "هیچگونه ارتباطی ندارد" with huzvārish gabra and prefers a kāfir link — so his "BQT:1774 does not agree" is accurate; Lokotsch 632 and Horn p.210 side with Mo'in, Iranica rebuts them. Nice extra: Mo'in's *own Farhang* (MON:3193, the ref Nourai cites) tags گبر «[آرا. قس. ع. کافر]» = Aramaic, contradicting his Borhan footnote.
- **#4 English algebra ← French** is the weak link: Klein 48 (the cited ref) has "Fr. Arab. al-jabr" where "Fr." = *from*, i.e. no French stage; Etymonline/Wiktionary say Medieval Latin, Funk & Wagnalls says Italian. Only Webster's puts French there. Marked partial, not disputed.
- **#7 Arabic Jibrīl** — Jeffery FVQ 100-101: ultimate origin Hebrew, but "the probabilities are that it came to him in its Syr. form"; a Syriac box is missing. **#9 Latin** likewise skips the Greek (LXX Γαβριήλ) step.

**Extraction errors: none.** Compared against the rendered page image (copied to `data/verification/sources/refs/ocr/BOOK/230.png`); the JSON is faithful, including the book's own garbled note "'Jobrân' is does not exist in Arabic."

Also saved: `data/verification/sources/refs/ocr/BQT/1774.vision.txt` (Borhan p.1774 footnotes 1, 2, 3, 7 read from the page image), and 9 web pages archived via fetch_source.py.
