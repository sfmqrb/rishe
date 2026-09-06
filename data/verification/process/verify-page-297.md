# Verification process log — verify-page-297


## [2026-09-06T22:31:45.643Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 297 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-297.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-297.json. Write /home/sfmqrb/git/rishe/data/verification/page-297.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 297` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T22:31:47.141Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T22:31:47.847Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T22:31:47.865Z] TOOL RESULT

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


## [2026-09-06T22:31:48.580Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-297.txt"
}
```


## [2026-09-06T22:31:48.589Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-297.json"
}
```


### [2026-09-06T22:31:48.597Z] TOOL RESULT

```
1	=== PDF page 297 (book page 267) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kwo, Kwi 1 : stem of interrogative and relative pronouns  (refs POK:644,646; AHD)
4	#1 (parent #0) [Avestan] refs=POK:644,648; BQT:1748; HRN:196 | kô, ka 1, kŭ 1, kŭ-thra, ka-hya : who, which, where? ; kâ 3 : how? ; kam 1, kam-čit, katama : which? ; kat : whether ; ka-da, ka-tha : when? ☞De 2 ; katâra : which of the two? either
5	  #2 (parent #1) [Persian] refs=BQT:672 | kŭ «کو» : where? ; kojâ «کجا» : where? ; kodâm «کدام» : which? ; kay 1 «کی ۱» : when? ; kî «کی ۲» : who?
6	#3 (parent #0) [Avestan] refs=POK:644,648; BQT:1748; HRN:196 | č-, čŭ, čî 2 : how? ; čiš 2, čiš-ca 2 : who? ; čeč : whether ; cit : even, in any case ; čaiti, chvant : how many? ; ča-hyâ : who, which?
7	  #4 (parent #3) [Persian] refs=BQT:672 | čeh «چه» : what? ; čŭn «چون» : how? ; čîz «چیز» : thing ; čand «چند» : how many? | extra: چی
8	#5 (parent #0) [Old Persian] refs=POK:644; SNS:86 | ka 1, kam 1 : if ; kâi-gi : what, how? ; čiy 2 : even, in any case ; čiš-čiy, kaš-čiy : who? ; aiva-čiy : nothing, none ☞I 2
9	  #6 (parent #5) [Persian] refs=BQT:1641; SNS:86 | kas «کس ۱» : person ; hîč «هیچ» : nothing, none
10	#7 (parent #0) [Germanic] refs=POK:464; AHD | hwa, hwi : ? ; hwatharaz
11	  #8 (parent #7) [English] refs=None | who, what, why, which, how, where, when, either, neither
12	#9 (parent #0) [Latin] refs=AHD | qu-, quantis, qualis
13	  #10 (parent #9) [English] refs=None | quantity, quality
14	--- entry 1 ---
15	ROOT Kwoi -> redirect to Kwei 2
16	
```


### [2026-09-06T22:31:48.600Z] TOOL RESULT

```
1	{
2	  "pdf_page": 297,
3	  "book_page": 267,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Kwo, Kwi 1",
8	        "lang": "Indo-European",
9	        "refs": "POK:644,646; AHD",
10	        "gloss": "stem of interrogative and relative pronouns"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "POK:644,648; BQT:1748; HRN:196",
18	          "words": [
19	            {"translit": "kô, ka 1, kŭ 1, kŭ-thra, ka-hya", "gloss": "who, which, where?", "script": null},
20	            {"translit": "kâ 3", "gloss": "how?", "script": null},
21	            {"translit": "kam 1, kam-čit, katama", "gloss": "which?", "script": null},
22	            {"translit": "kat", "gloss": "whether", "script": null},
23	            {"translit": "ka-da, ka-tha", "gloss": "when?", "script": null, "see": ["De 2"]},
24	            {"translit": "katâra", "gloss": "which of the two? either", "script": null}
25	          ],
26	          "script_extra": null,
27	          "note": null,
28	          "quote": null
29	        },
30	        {
31	          "id": 2,
32	          "parent": 1,
33	          "lang": "Persian",
34	          "refs": "BQT:672",
35	          "words": [
36	            {"translit": "kŭ", "gloss": "where?", "script": "کو"},
37	            {"translit": "kojâ", "gloss": "where?", "script": "کجا"},
38	            {"translit": "kodâm", "gloss": "which?", "script": "کدام"},
39	            {"translit": "kay 1", "gloss": "when?", "script": "کی ۱"},
40	            {"translit": "kî", "gloss": "who?", "script": "کی ۲"}
41	          ],
42	          "script_extra": null,
43	          "note": null,
44	          "quote": null
45	        },
46	        {
47	          "id": 3,
48	          "parent": 0,
49	          "lang": "Avestan",
50	          "refs": "POK:644,648; BQT:1748; HRN:196",
51	          "words": [
52	            {"translit": "č-, čŭ, čî 2", "gloss": "how?", "script": null},
53	            {"translit": "čiš 2, čiš-ca 2", "gloss": "who?", "script": null},
54	            {"translit": "čeč", "gloss": "whether", "script": null},
55	            {"translit": "cit", "gloss": "even, in any case", "script": null},
56	            {"translit": "čaiti, chvant", "gloss": "how many?", "script": null},
57	            {"translit": "ča-hyâ", "gloss": "who, which?", "script": null}
58	          ],
59	          "script_extra": null,
60	          "note": null,
61	          "quote": null
62	        },
63	        {
64	          "id": 4,
65	          "parent": 3,
66	          "lang": "Persian",
67	          "refs": "BQT:672",
68	          "words": [
69	            {"translit": "čeh", "gloss": "what?", "script": "چه"},
70	            {"translit": "čŭn", "gloss": "how?", "script": "چون"},
71	            {"translit": "čîz", "gloss": "thing", "script": "چیز"},
72	            {"translit": "čand", "gloss": "how many?", "script": "چند"}
73	          ],
74	          "script_extra": "چی",
75	          "note": null,
76	          "quote": null
77	        },
78	        {
79	          "id": 5,
80	          "parent": 0,
81	          "lang": "Old Persian",
82	          "refs": "POK:644; SNS:86",
83	          "words": [
84	            {"translit": "ka 1, kam 1", "gloss": "if", "script": null},
85	            {"translit": "kâi-gi", "gloss": "what, how?", "script": null},
86	            {"translit": "čiy 2", "gloss": "even, in any case", "script": null},
87	            {"translit": "čiš-čiy, kaš-čiy", "gloss": "who?", "script": null},
88	            {"translit": "aiva-čiy", "gloss": "nothing, none", "script": null, "see": ["I 2"]}
89	          ],
90	          "script_extra": null,
91	          "note": null,
92	          "quote": null
93	        },
94	        {
95	          "id": 6,
96	          "parent": 5,
97	          "lang": "Persian",
98	          "refs": "BQT:1641; SNS:86",
99	          "words": [
100	            {"translit": "kas", "gloss": "person", "script": "کس ۱"},
101	            {"translit": "hîč", "gloss": "nothing, none", "script": "هیچ"}
102	          ],
103	          "script_extra": null,
104	          "note": null,
105	          "quote": null
106	        },
107	        {
108	          "id": 7,
109	          "parent": 0,
110	          "lang": "Germanic",
111	          "refs": "POK:464; AHD",
112	          "words": [
113	            {"translit": "hwa, hwi", "gloss": "?", "script": null},
114	            {"translit": "hwatharaz", "gloss": null, "script": null}
115	          ],
116	          "script_extra": null,
117	          "note": null,
118	          "quote": null
119	        },
120	        {
121	          "id": 8,
122	          "parent": 7,
123	          "lang": "English",
124	          "refs": null,
125	          "words": [
126	            {"translit": "who, what, why, which, how, where, when, either, neither", "gloss": null, "script": null}
127	          ],
128	          "script_extra": null,
129	          "note": null,
130	          "quote": null
131	        },
132	        {
133	          "id": 9,
134	          "parent": 0,
135	          "lang": "Latin",
136	          "refs": "AHD",
137	          "words": [
138	            {"translit": "qu-, quantis, qualis", "gloss": null, "script": null}
139	          ],
140	          "script_extra": null,
141	          "note": null,
142	          "quote": null
143	        },
144	        {
145	          "id": 10,
146	          "parent": 9,
147	          "lang": "English",
148	          "refs": null,
149	          "words": [
150	            {"translit": "quantity, quality", "gloss": null, "script": null}
151	          ],
152	          "script_extra": null,
153	          "note": null,
154	          "quote": null
155	        }
156	      ]
157	    },
158	    {
159	      "root": {
160	        "name": "Kwoi",
161	        "redirect": "Kwei 2"
162	      },
163	      "nodes": []
164	    }
165	  ]
166	}
167	
```


## [2026-09-06T22:31:52.432Z] TOOL CALL #4: Bash

```json
{
 "command": "ls tools/ && sed -n '1,60p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T22:31:52.482Z] TOOL RESULT

```
build_site.py
fetch_source.py
ganjoor.py
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
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
```


## [2026-09-06T22:31:54.205Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','BQT','HRN','SNS','KLN','BRT','KNT','PHD','NYB','WLD','MON','ARY','HUB','IEC','SYN','SKT','WEB','FSD']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-06T22:31:55.993Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
```


## [2026-09-06T22:32:09.569Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=1 && NR<=0' POK_full.txt >/dev/null; grep -n \"kʷo-\\|kᵘ̯o-\\|k^u̯o-\" POK_full.txt | head -30; echo ---; grep -n \"644\\]\\|\\[644\\]\\|page 644\" POK_full.txt | head"
}
```


## [2026-09-06T22:32:09.710Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60; echo ===; ls ocr 2>/dev/null | head"
}
```


### [2026-09-06T22:32:12.166Z] TOOL RESULT

```
---
```


### [2026-09-06T22:32:12.210Z] TOOL RESULT

```
Exit code 1
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
(eval):1: == not found
```


## [2026-09-06T22:32:14.733Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | sed -n '60,200p'"
}
```


### [2026-09-06T22:32:14.780Z] TOOL RESULT

```
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
```


## [2026-09-06T22:32:17.500Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 800 POK_full.txt; echo; echo ===; grep -n \"^Page\\|Seite 644\\|644\" POK_full.txt | head -5"
}
```


### [2026-09-06T22:32:17.546Z] TOOL RESULT

```
Exit code 1
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk. 




Akkadian 


Alan. 




Alanian (=Old Ossetic) 


Alb. 




Albanian 


Anat. 




Anatolian 


Ang. 




Anglian 


AngN 




Anglo-Norman 


Aram.- 


■Iran 


Aramaeo-lranian 


Ash. 




Ashkun 


Ass. 




Assyrian 


Auk. 




Aukshtaitian 


Bactr. 




Bactrian 


Bel. 




Belorussian 


Br. 




British 


Bret. 




Breton 


BVan. 




Bas-Vannetais 


CCI. 




Continental Celtic 


Chak. 




Chakavian 


Chor. 




Chorasmian 


Clb. 




Celtiberian 


Class. 


Skt. 


Classical Sanskrit 


Co. 




Cornish 


Corn. 




Cornouillais 


Dae. 




Dacian 


Dan. 




Danish 


Dard. 




Dardic 


Dzuk. 




Dzukian 


EBI. 




East Baltic 


EGm. 




East Germanic
(eval):1: == not found
```


## [2026-09-06T22:32:18.380Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json\nd=json.load(open('../refs_online.json'))\nfor k in ['POK','BQT','SNS','HRN','AHD']:\n    print('==',k); print(json.dumps(d[k],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-06T22:32:20.106Z] TOOL RESULT

```
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
== SNS
{
 "title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/VajnameShayest",
 "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"
 ],
 "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image",
 "covers_etymology": true,
 "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."
}
== HRN
{
 "title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893",
 "edition_found": "1893 (Google scan, Univ. Michigan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/grundrissderneu00horngoog",
 "identifier": "grundrissderneu00horngoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.",
 "notes": "OCR of German Fraktur-free text is decent; Persian script is not OCRed.",
 "cites": "page number of Horn, Grundriss der neupersischen Etymologie (1893); entries are also numbered"
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


## [2026-09-06T22:32:25.178Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: k\" POK_full.txt | grep -i \"u̯o\\|u̯i\\|^.*k.o-\" | head -40"
}
```


### [2026-09-06T22:32:25.231Z] TOOL RESULT

```
47920:Root / lemma: kola- : klo-
```


## [2026-09-06T22:32:26.105Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==301' POK_02.txt | head -80"
}
```


### [2026-09-06T22:32:27.679Z] TOOL RESULT

```
  I  514  f..  WH.  I  45.  245  ff..  250.  846,  Trautmann  125.
2.  k^el-  .fern  (örtlich  und  zeitlich)'  in:
ai.   caramd-   .der  letzte,  äußerste',   cirds   ,lang  (zeitlich)',   gr.  TfjXe,  äol. TtrjXvL  .ferU;  weit'  (rr^lö-d-ev,  -^t.  -crs).  ftdXccv  .längst'  (/raAcctog  .alt'.  TtaXai-  t- TBQoq,  -TaTOQ),  cymr.  corn.  bret.  pell  .fern'  (*Ä;oeZ-s-o-?).  cymr.  pellaf  .der  _ äußerste'.  ^,
WP.  I  517.  ^
j.  kHei-  .Schwärm.  Schar.  Sippe'?
Ai.  küla-m  n.  .Herde.  Menge;  Geschlecht';  kj-sti-  f.  .Leute.  Menschen'; gr.  rsXog  n.  .Schar';
aksl.  celjadh  f.  .Gesinde'.  Kollektiv  zu  dem  in  celovSkT,  .Mensch'  vor- liegenden celo-,
WP.  I  517.  Berneker  141  f..  Meillet  BSL.  22. 18  f.,  Kuiper  Proto-Munda  55.
k^em-  .schlürfen,  schlucken'.
Ai.  cämati  und  camati  .schlürft'.  Partiz.  äcänta-j  camasd-  m.  .Trink- schale. Becher',  camü-  m.  .Schüssel';  npers.  cam  .das  Essen',  camiöan .trinken',  osset.  cumun  , schlürfen' ;
arm.  kim-k  PL  .faux,  guttur'  (*Ä;%emä-);  mit  Ablautstufe  ö:  npers.  kam .Gaumen',  afghan.  kümai  ds. ;  zweifelhaft  ist  gr.  ezef-iev'  ^jfxsXysv  und ri^vowa  [wohl  rs^ovra]'  äfisXyovra  Hes..  wobei  äfxsXysiv  in  der  spätem Bed.  .Flüssiges  aussaugen,  auspressen'  zu  fassen  wäre;
641
nisl.  hvöma  (aus  ^hväma,  idg.  "^k^emö  =  ai.  cdmati)  .verschlucken,  ver- ■!:      schlingen';  hvöma  f.  .Speiseröhre.  Schlund^. WP.  I  Ö14.
^ugae,  Partikel  der  Verallgemeinerung  und  Unbestimmtheit.
Ai.  cana,  av.  <^inä  .irgend^;  oft  negativ,  z.  B.  ai.  nd  Bka§  cana  .keiner^;
germ.  -%in  in  aisl.  hver-gin  .keineswegs^,  ags.  asächs.  ahd.  hiver-gin .irgendwo^  (aus  htvar  .wo'  +  -gin)  aus  ahd.;  io-wergin,  mhd.  iergen,  nhd. irgend.
WP.  I  399  f..  Wackernagel-Debrunner  III  562.
y^üQnth-  .leiden,  duldend
Gr.  Tcevd-og  n.  .Leid.  Trauer.  Unglück';  nachhom.  nad^og  n.  .Leid.  Un- glück, Leidenschaft',  ndoxo)  (*k^nth-s7cö),  Fut.  itslaoiiai,  Aor.  errad-ov, perf.  TCSTtovd^a  ,leide.  erdulde'  (tts-  für  le-  nach  den  Formen  mit  na-,  Tto-) ;
lit.  kenciü,  kgsti  .aushalten,  leiden',  pakantä  f.  .Geduld',  kanciä  .heftiger körperlicher  Schmerz',  itiem-kintis  .den  Winter  über  aushaltend',  lett.  aiehi cust  .leiden,  dulden',  ziem-ciesis  {^kentsia-)  .Wintergrün';
air.  cess{a)im  .ich  leide'  (*k^enth-tö  oder  *k^Aenth-s-ö),  cessad  .passiö'.
Pedersen  KG.  II  486  vermutet  einen  nasallosen  VerAvandten  in  air. ar-cessi  (*k'!^et-si-)  .schont,  erbarmt  sich'  (Bed.  wäre  wie  in  lit.  pakenteti .mit  jemandem  Geduld  haben'),  cymr.  arhedu  (*Ä:^e^)  .schonen',  bret. erhedi  .empfehlen*  (älter  auch  .schonen'),  acorn.  henbidiat  ,parcus'.
WP.  I  513.  Trautmann  126 f..  Schwyzer  Gr.  Gr.  1.  708.
I.  k"er-  .machen,   gestalten'.  Adelleicht  ursprünglich   von  irgendeiner  nicht mehr  bestimmbaren  Handwerkstätigkeit.
Ai.  karöti  (Imper.  kuru),  krnöti  .macht,  vollbringt'.  Partiz.  kftd-]  kard- .tuend.  machend',  m.  .Hand.  Elefantenrüssel',  kära-  .machend',  m.  .Tat'. kdrman-  n.  .Handlung.  Werk',  karmära-h
```


## [2026-09-06T22:32:33.588Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Interrogativ\\|Fragepron\\|Relativpron\" POK_02.txt | head -20"
}
```


### [2026-09-06T22:32:33.629Z] TOOL RESULT

```
1071:ai.  gha  {*gho),  ha  {*ghe)  hinter  Negation  (nd  glia),  Personalpron.  (z.  B. vaydm  gha),  dem  5o/^o-Pron.  (sd  gha^  sd  ha)^  dem  Fragepron.  (z.  ß.  kdrii ha),  dem  Relativpron.  (yö  gha^  yö  ha),  auch  hinter  andern  Wortarten;  ai. hdnta  ^wohlan,  auf,  da  nimm,  sieh  da^;
1074:aksl.  -gOf  -ze  hinter  Negation  (ni-ze  ,neque^,  nejedim  ze  ,ne  unus  quidem, ovösig']  vgl.  auch  aksl.  7ieze,  serb.  nego  ,als'  beim  Komparativ  und  serb. nego  ^sondern,  aber^,  cech.  nez(e)  ,doch^,  wo  ne-  eher  der  Negation  als  der positiv  weisenden  Bed.  des  Pron.-St.  ne-  entsprungen  ist),  hinter  dem Relativpron.  (ize),  dehnstufig  {*gho)  osorb.  kdy-ha  ,wann  denn'  (u.  dgl.; Berneker  316);
1075:lit.  -gu  {*ghö),  -gi  (dies  mit  dem  Vokal  i  der  2.  Gruppe)  in  negl,  neigt, negü  , nicht',  hinter  Pers.-Pron.  (z.  B.  tu-gu,  tu-gi  ,ovye'),  alit.  auch  -ga,  -ge, dem  so/^o-Pron.  (z.  B.  tie-gi),  dem  Fragepron.  (kaip-gi  ,wie'),  -gu  auch Fragepartikel  (vgl.  auch  alit.  an-gu  ,ob',  apr.  an-ga  ,ob'),  apr.  beggi  ,denn', käigi  ,wie',  neggi  ,auch  nicht,  noch',  niqueigi  ,nimmermehr';  gr.  ovx^ s.  unten.
1083:in  o-r.  i^€-y6  =  got.  m^-^,  ahd.  mi-h  =  arm.  25  ,me'  (zunächst  aus  *in-^\ iyo)  ys,  eyw-ys,  av  ys,  got.  pu-k,  si-k,  ahd.  di-h,  si-h;  nach  dem  so//o-prQj. 6'  /£,  nach  dem  Relativpron.  oaaa  ys,  ovTiva  ys,  ferner  yh,  dor.  böot^^ yä  auch  hinter  andern  Wortarten.  Im  Balt.  sowie  auch  (außer  in  der  mit X  vokalisierten  Form)  im  Slav.  ist  der  Guttural  der  1.  Gruppe  herrschend geworden,  wie  auch  in  gr.  -^t;
4668:j.  ic"e  enklit.  ,und*  aus  ,*irgendwie*,  wie  auch  zum  Pron.-St.  klio-y  k^e-  des  Inter- rogativums  und  Indefinitums  im  selben  Verhältnis  stehend,  wie  *ke jhier*  zu  Zco-,  ke-  , dieser*.  Damit  identisch  kV^e  hinter  Formen  vom Interrogativ-Indefinit-Stamme  zur  Verstärkung  des  indefiniten  Sinnes.
4812:k^o-,  k^.e-,  fem.  k^ä]  k^ei-  (vermutlich  einst  nur  im  Nom.  Akk.  Sg.). kY,u-  (nur  im  Adv.) ;  die  betonten  Formen  sind  Interrogativa,  die  im! betonten  Indefinita;  einzel sprachlich  z.  T.  Relativum  geworden.
4818:gr.  Gen.  Sg.  hom.  reo,  att.  tov  ,wessen?^  (=  abg.  ceso^  ahd.  hwes]  idg. *k^es(j)o);  Dat.  Sg.  f.  dor.  fra,  att.  titj,  ion.  y.fj  (*Ä;?^ä-)  ,wohin?,  wozu?,  wie?^; Instr.  f.  ion.  att.  ftfj  ,wohin^ ;  Instr.  Sg.  m.  n.  kret.  6-7i^  ,wo,  wohin^,  dor. TtT^-TtoKa,  7t(h-7tOY.a,  att.  Ttcb-noTs  ,je  einmal,  noch  je^,  ttw,  ion.  xw  ,(*über einen  Zeitraum  hin,  irgendwann  =)  noch'  und  modal  ,irgendwie^  in  o^ niü  ,noch  nicht^  und  ,nicht  irgendwie,  keinesfalls*^  (vgl.  got.  he  sowie  lat. quo  ,wohin^,  wenn  nicht  Ablativ) ;  ftwg,  ion.  xwg  ,wie^ ;  Ttoöanog  ^von  woher stammend^  (neutr.  "^k^od  +  Formans  -i^k^o-y  vgl.  äXlod-anög  oben  S.  25 unter  "^alios  ,anderer^);  att.  usw.  tvol  ,wohin^,  dor.  tvsZ  ,wo^  (Lok.);  att. Ttov,  ion.  Y.OV  ,wo^  (Gen.);  n6&ev  ,von  wo?*^;  hom.  rcöd-v,  ion.  %6&i  ,wo^; TtöxB  ,wann?^  (dor.  ^roxa  ,wann^,  vgl.  Schwyzer  Gr.  Gr.  1,  629),  norij  lesb. Ttöta,  ion.  xoTf  ,irgendeinmal,  einst^,  wozu  auch  rtoxs  nach  Interrogativen, z.  B.  iL  TtoTB  ,was  dann^  und  —  mit  erst  gr.  Red.  —  -riW«  ds.  (s.  dazu  unter foti-s),  TTÖas  ,wohin^  (-ae  aus  -ts)  =  got.  kap,  had  ,wohin^;  kret.  zsTov noXov  Hes.,  att.  Ttotog  ,qualis^  aus  *Ho-  +  oiuo-  =  ai.  Eva-  ,Art  und  Weise^, ahd.  ewa,  vgl.  got.  laiwa  ,wie?^,  s.  unter  ei-  ,gehen'^;  zum  Wechsel  von 7t-  (:  ion.  X-):  t-  s.  Schwyzer  Gr.  Gr.  1,  293  f.
4856:hitt.  Frage-  und  Relativpron.  kuiä  ^wer^  welcher^,  verallgemeinernd kui§  kui§  usw.  (=  lat.  quisquis)  ^wer  immer'^  Indefinitum  kuis-ki  (=  lat. quisque)  ^irgend  jemand^,  n.  kuit-ki  (=  lat.  quidque);  lyk.  ti-ke  (=  hitt. kuis-ki)]  s.  P.  Tedesco  Lang.  21,  128 ff.,  A.  Hahn  Lang.  22,  68 ff.
```


## [2026-09-06T22:32:37.180Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4805,4875p' POK_02.txt"
}
```


### [2026-09-06T22:32:37.220Z] TOOL RESULT

```
lit.  keturi  (Akk.  keturis  =  ai.  caturah),  fem.  heturios-^  lett.  ^e^W;  aksl. ce^j^T^e  m.,  -i  f.  n.,
toch.  A  s<«;ar  (*/(;JJe^Wer-),  B  §(t)wäry  s(t)ioer  [*k^etuores)  ,4c' ^  A  stwaräk  ,4.0'. In  Kompositis  (und  Ableitungen)  k^etur-,  k^etur-,  k'^etru-  :  ai.  cdtur- [a7dga-h  ^viergliedrig^],  mit  Schwundst.  der  1.  Silbe  av.  ä-xtüirlm  ^viermal^, ai.  turiya-,  turya-h,  av.  tüirya-  ,vierter^;  av.  ^a^ioard-aspa-  av.  cad^ru- \igao§a-']]  aus  *TETJ^ga  (idg.  ^k'ifietur-) :  gr.  TSTga-lnöaioi],  -7iovg\  kontaminiert aus  rgv-  und  Tsxga-  :  gr.  xg&jtst,«]  rgv-(päXsLa  ,Helm^  ("^gl-  Tergcc-q)aXog ,mit  vier  Schirmen  versehen^)  wohl  schwundstufig  *[k}Ü]tru-,  wie  osk. trutom  (wenn  es  ,quartum^  bedeutet);  lat.  quadru-[jpes]]  umbr.  petur[-pursus ^quadrupedibus'] ;  gall.  Petru-corii  ,die  Vierstämmigen^^  petru-deca-metos ,vierzehnter',  cymr.  pedry-  _,vierfach'  (gall.  petor-ritum  ,vierräderiger Wagen'  wohl  mit  dem  Vokal  von  ^k'^etuores),  , viereckig;,  kräftigt;  got. fidur-dögs  (Westgermanisches  s.  oben);  lit.  ketur-[kdjis  ,vierfüßig'] ;  arm. Iciar-a-sun  ,40'  (aus  *tiür-,  vgl.  ai.  turlya-  , vierter'). Ordinale:
Ai.  caturthd-,  turiya-,  türya-,  av.  tüirya- ;  arm.  6orir,  corr-ord,  kar-ord ; gr.  att.  'vexagzog,  hom.  reTgarog  (für  ^rvgxog  ^vierter'  in  Tvgratog),  böot. Tthgazog;  lat.  quäi'tus,  prän.  Quorta,  osk.  vielleicht  truto-  (s.  oben);  air. cethramad  (*kV:etru-metos) -^  gall.  p etu arios  =  3iCjmi\  petuerid]  ahd.  ßordo, ags.  feorda,  aisl.  fiördi]  lit.  ketvirtas  (lett.  ceturtais  wie  ai.  caturthd-h), aksl.  cetvrbh]  toch.  A  Hart  i^kVietuftos),  B  itwerne.
Von  anderem  Zubehör  sei  herausgehoben  lat.  quattuor decira,  got.  fid- wörtaihun,  ahd.  viorzehan  ,14';  dor.  ion.  delph.  rsrgcoxovra  (*k^etUor9- komte)  =  lat.  quadrägintä  „40";  av.  iia&rus  ^viermal',  ai.  catüh  =  lat. quater  {*k^etrus)]  ai.  catvard-  m.  ^viereckiger  Platz',  lit.  ketverz  ,je  vier', aksl.  cetverb,  öetvor^  ds.,  air.  cethorcho  „40"  (^k'^etru-Jcomt-s).
41*
644  *
WP.  I  512,  Trautmann  131  f.,  Schwyzer  Gr.  Gr.  I  351  f.,  589  f.,  WH.  U 394,  400  f.,   F.  Sommer  Zum  Zahlwort,  27.
k^o-,  k^.e-,  fem.  k^ä]  k^ei-  (vermutlich  einst  nur  im  Nom.  Akk.  Sg.). kY,u-  (nur  im  Adv.) ;  die  betonten  Formen  sind  Interrogativa,  die  im! betonten  Indefinita;  einzel sprachlich  z.  T.  Relativum  geworden.
1.  Stamm  kiio-,  k^e-,  fem.  küä-;  Gen.  k'iesOy  Instr.  k^^i,  Zeitadverb  ic^ozö.
A.   Kasuelle  Formen  und  nur  einzelsprachlich   belegbare  Ableitungen:
Ai.  kd-h  (=  phryg.  xog  ,irgendeiner^;  got.  has  ,wer?'),  fem.  kä  ,wer?* und  indefinit;    idg.  k^os  wohl  der  alte  Nom.  Sg.  m.;
av.  kö  (Gen.  gthav.  ka-liyä,  (Sa-hya),  fem.  kä  ,wer?,  welcher?^,  apers. ka^[^6iy'\,  als  Indef.  mit  -cTt,  oder  in  Doppelsetzung,  oder  in  neg.  oder rel.  Sätzen;  av.  kä  ,wie?^;  apers.  ada-kaiy  ,damals^  ==  gr.  jtoi  bei  Pindar jTCov'  gesetzt;
arm.  o  ,wer?^  {*kl^o-,  Meillet  Esquisse^  189),  indef.  o-k  ,irgendwer'  {-k  ^ lat.  que),  o-mn  ,wer^  (relativ  o-r  ,welcher^);  kani  ,wievieF,  kan  ,als,  nach dem  Komparativ^  (=  lat.  quam)^  kanak  ,quantita'  u.  dgl. ;  lat.  quantus  ,wie groß^,  umbr.  panta  ^quanta'^  ist  von  quam  mit  Formans  -to-  abgeleitet;
gr.  Gen.  Sg.  hom.  reo,  att.  tov  ,wessen?^  (=  abg.  ceso^  ahd.  hwes]  idg. *k^es(j)o);  Dat.  Sg.  f.  dor.  fra,  att.  titj,  ion.  y.fj  (*Ä;?^ä-)  ,wohin?,  wozu?,  wie?^; Instr.  f.  ion.  att.  ftfj  ,wohin^ ;  Instr.  Sg.  m.  n.  kret.  6-7i^  ,wo,  wohin^,  dor. TtT^-TtoKa,  7t(h-7tOY.a,  att.  Ttcb-noTs  ,je  einmal,  noch  je^,  ttw,  ion.  xw  ,(*über einen  Zeitraum  hin,  irgendwann  =)  noch'  und  modal  ,irgendwie^  in  o^ niü  ,noch  nicht^  und  ,nicht  irgendwie,  keinesfalls*^  (vgl.  got.  he  sowie  lat. quo  ,wohin^,  wenn  nicht  Ablativ) ;  ftwg,  ion.  xwg  ,wie^ ;  Ttoöanog  ^von  woher stammend^  (neutr.  "^k^od  +  Formans  -i^k^o-y  vgl.  äXlod-anög  oben  S.  25 unter  "^alios  ,anderer^);  att.  usw.  tvol  ,wohin^,  dor.  tvsZ  ,wo^  (Lok.);  att. Ttov,  ion.  Y.OV  ,wo^  (Gen.);  n6&ev  ,von  wo?*^;  hom.  rcöd-v,  ion.  %6&i  ,wo^; TtöxB  ,wann?^  (dor.  ^roxa  ,wann^,  vgl.  Schwyzer  Gr.  Gr.  1,  629),  norij  lesb. Ttöta,  ion.  xoTf  ,irgendeinmal,  einst^,  wozu  auch  rtoxs  nach  Interrogativen, z.  B.  iL  TtoTB  ,was  dann^  und  —  mit  erst  gr.  Red.  —  -riW«  ds.  (s.  dazu  unter foti-s),  TTÖas  ,wohin^  (-ae  aus  -ts)  =  got.  kap,  had  ,wohin^;  kret.  zsTov noXov  Hes.,  att.  Ttotog  ,qualis^  aus  *Ho-  +  oiuo-  =  ai.  Eva-  ,Art  und  Weise^, ahd.  ewa,  vgl.  got.  laiwa  ,wie?^,  s.  unter  ei-  ,gehen'^;  zum  Wechsel  von 7t-  (:  ion.  X-):  t-  s.  Schwyzer  Gr.  Gr.  1,  293  f.
alb.  ke  ,wen?^  (*A;Jto-m),  se  ,was?'  (Abi.  *Ä;^öc?  mit  analogischer  Palatali- sierung?),  si  ,wie?'  (*Ä:?tei?);
lat.  qul  (alat.  quoi  aus  *Ä;!^o  +  Demonstr.  -i),  quae,  quod  Rel.  und  Inde- finit\im,  osk.  <pui,  pai,  püd  ,qui,  quae,  quod^,  umbr.  po-i,  -e,  -ei  ,qui^  pufe, porse  ,quod',  lat.  cuius,  cui,  quo,  qua  usw.,  umbr.  pusme  ,cui^;  Adv.  lat. quo  ,wohin'  (Abi.)  =  umbr.  pu-e   ,quö'  (u  =  ö,   das   vor  Enklitika  nicht
645
verkürzt  ist);  lat.  quam  ,wie,  als'  (Akk.  Sg.  f.)  =  umbr.  [pre-]pa  ,[prius-] qiiamS  osk.  pruter  pam  ds.  (av.  kam-cit  ^in  irgendeiner,  jeder  Weise^^ .ilat.  quam-de  =  umbr.  pane,  osk.  pan  ^quam';  lat.  quantus  s.  oben;
lat.  quom,  cum  ,wenn,  als;  so  oft  als'  (Akk.  Sg.  n.  wie  primum  usw.) ^  av.  k^'^  >^ieS  got.  kan  ,wann',  apr.  kan^  lit.  (dial.)  kq  ,wenn';  aksl. ko-gda  aus  *ko-g{o)da,  Meillet  Slave  commun^  470;
mit  -de  erweitert  umbr.  pon(n)e,  osk.  jpün  ,quom';  lat.  quandö  ,wann' i*quäm  Akk.  der  Zeiterstreckung  +  dö),  umbr.  panu-pei  ,quandöque', mnd.  icante  ,bis';  lat.  quantus,  umbr.  panta  ^quanta'  (S.  644);
air.  nech,  adj.  (proklit.)  nach  ,aliquis;  ulluS;  quisquam',  cymr.  com.  bret. nep  {^ne-k'^o-s,  mit  Verblassen  der  Negation  in  neg.  Sätzen  mit  wiederholter ^[egation,  ebenso  lit.  kaz-ne-käs  , etwas',  kadä-ne-kadä  ^zuweilen',  abg. n^k^to  Jemand');  air.  cach,  verbunden  cach,  mcymr.  paiop,  verbunden pop,  com.  pupj  pop,  pep,  bret.  pep  Jeder'  (*Ä^ä-  oder  Ä?iö-Ä;?to-s ;  zu  abg. kak^  ^welcher?'),  ir.  cech  Jeder'  (das  e  nach  necK)]  air.  can,  mcymr.  pan I  (*k^ana)y  mbret.  pe-han  ,woher?';  air.  cuin  ,wann?',  mcymr.  usw.  pan, pann  ,als,  wenn'  (*kV^ani?),  air.  ca-ni,  mcymr.  po-ny  ,nonne'  (*^"ä-);
got.  Ivas  (*k'!^o-s)  ;Wer?'  und  indefinit  (Gen.  Jvis,  ahd.  Jiwes  =  abg. ceso,  gr.  T€o)j  aschwed.  hvar,  har,  adän.  hvä,  ags.  hwä  ,wer',  mit  dem  e I  des  Gen.  as.  hwe,  ahd.  hwer  (*Ä:^e-s)  ,wer';  neutr.  got.  ha  {*k^o-d),  ahd. liwaz^  an.  hvat,  ags.  hwoßt,  as.  hicat  ,was';  fem.  got.  hö  ,wer?  welche?'; got.  Ivan  ,wann,  wie',  as.  hwan,  ahd.  liwanne  ,wann'  (näherer  Vergleich mit  air.  can  ,woher'  ist  wegen  der  Bed.  fraglich),  as.  hwanda  ,weil',  ahd. hwanta  ,warum';  got.  he  ,womit?'  (Instr.);  afries.  hö,  as.  hioö,  ahd.  hicuö ,wie'  zu  lat.  quo  , wohin'  (Ablat.),  gr.  Ttw,  xw  ,irgendwie';
lit.  käs  ,wer?,  was?'  auch  indefinit,  fem.  M,  apr.  kas  m.,  ka  n.  ,wer  ?', kas  f.  quai,  quoi,  n.  ka  (Akk.  auch  kan,  kai)  ,welcher,  -e,  -es';  lit.  kad ;Wenu,  daß,  damit'  (Konjunktion  wie  lat.  quod,  aus  dem  fragenden  Ge- brauch, vgl.  ai.  kad,  av.  kat  adv.  Fragewort  ,nun,  ob?');  lit.  ka%,  kat-p, apr.  kai-gi  ,wie?'  (=  abg.  c^;  aber  über  gr.  ytal  s.  unter  *kai  ,und');
abg.  k^-to  ,wer?'  (G-en.  ceso),  kyß,  f.  kaja,  n.  koje  ,qui,  7toLog?%  ce, ,y,aitOL,  Y.ai'rteq,  sltisq'  (s.  oben).
B.    Ableitungen,    die    sich   durch   mehrere   Sprachen   verfolgen   lassen:
k^o-tero-  ,wer  von  zweien?';    k^ä-li-  ,wie?';    k"o-ti-,  k"e--ti-  ,wie
viele  ?'.
Ai.  katard-,  av.  katära-  ,wer  von  zweien',    gr.  ftörsQog,  ion.  yiÖTSQog  ds.,
osk.  Lok.  puterei-pid  ,in  utroque',  umbr.  podruh-pei  adv.  ,utroque',  putres-pe
,utriusque',  got.  ha^ar,   aisl.  huärr,  ags.    hiuceper  ,wer  von  beiden'  (ahd.
hwedar,  nhd.  noch  in  iveder,  mit  e,  wie  hwer  ,wer' :  got.  kas),  lit.   katräs
jwelcher  von  beiden,  welcher  ?',  abg.  koteryjh,  kotoryjh  ,welcher'  Kompara-
646
tivbildung  (Beschränkung  auf  die  Wahl  zwischen  zwei  Gegensätzen), superlativisch  ai.  katamd-  .welcher  von  mehreren^ ;  vgl.  vom  Stamm  khi^ ! lat.  uter.
Ai.  kadä,  av.  kada  .wann?';  aber  lit.  kadä  .wann?'  aus  *kadhn]  zum Ausgang  siehe  oben  S.  181  ff.  (auch  für  abg.  kqdg,  kgde  .woher',  lat, q2ian-do).
Gr.  TtrjU-yiog  .wie  groß?  wie  alt?',  lat.  quälis  .wie  beschaffen',  lit.  kdUi köV  .wie  lange' ;  vom  St.  k^o-  aus  :  abg.  koUH  .wie  groß',  koh  ^quantum« (Trautmann  111).
Ai.  kdti  .wie  viele'  =  hitt.  kuwatta,  lat.  quot  ds.  (vom  apokopierteu quot  aus :  quotus  .der  wievielte'),  ai.  kati-thd-  .der  wievielte'  =  lat. *quotitei  (Lok.  m.)  die  >  cottl-die  .am  wievielten  Tage  auch  immer,  täglich'« gr.  lesb.  TCÖaaoQ  (hom.  7toaaf](.iaQ),  att.  TroVog.  ion.  ycöaog  .wie  groß'  (*k^oti'09^^ Ttöarog  ,der  wievielte'  aus  *7toGaoaT6g',  daneben  mit  idg.  e  av.  caiti  .wie viele',  bret.  pet  in  pet  dez  .wieviel  Tage',  petguez  .quotiens'.
Ai.  kdr-hi  .wann?'  ==   got.    Ivar^  aisl.   hvar  (*k'!ior)  .wo?'    und   relativ (davon  got.  harjis,  aisl.  hverr  .welcher',  eig.  .wo  er',  wie  aus  lit.  kur  [*Ä:!ittr] jWO^ -\- jis  .er'  das  lit.   Rel.  kurisj  kurs  .welcher'  erwuchs);    e-stufig  ags.i hwöRr,  ahd.  as.  hwär  .wo';  ö-stufig  lat.  cur  .warum,  weshalb',  alt  quör.    ^
Eine  Parallelbildung  zu  lat.  quis  in  alat.  quir-quir  .ubicunque'.  "J
2.  Stamm  k^ei-,  gleiche  Form  für  Maskul..  Neutr.  und  Femin.:
Ai.  kirn  .was?  was',  kih  .wer?',  nd-ki-h  .niemand'  (mit  k  statt  c;  letzteres lautgesetzlich  in:)  ai.  cit  (cid),  av.  cit,  apers.  ciy  .sogar,  jedenfalls'  (ur- sprüngl.  Nom.  Sg.  n.  *irHi-d;  s.  auch  unter  k^e  ,und');  av.  iii§  .wer'.  6i§ca ==  lat.  quisque,  gr.  rlg  is,  apers.  Öi§-öiy  ds. ;  av.  öl  .wie'  (Instr.);
arm.  -6  in  in-ö  .etwas'  (=  ai.  kirn — cid),  das  auch  im  ersten  Glied  hierher, mit  Abfall  des  ä:J?-  wie  i  (z-i)  .was?*  (*kl^id-),  Instr.  i-v  .wodurch,  womit', (s.  auch  oben  zu  arm.  o  ,wer') ;  zum  Alb.  s.  oben  unter  1 ;
gr.  rlg  {*k^is)  m.  f.  (thess.  mg,  ark.  kypr.  aig),  n.  rl  (*k^id)  .wer?  welcher,  -e, -es  ?'  und  rlg,  rt  .(irgend)  wer.  was'.  Akk.  m.  *tlv  {*knim)  erw.  zu  TtVa.  wonach rivog,  TLvi,  Fl.  n.  *k'!^id  in  megar.  ad  (.idv  .wieso?'  ti  (,irjv;  höot.  t«  .warum' =  lat.  quia]  auch  in  ion.  dcaaa,  att.  Icrra,  ,rLvä  Nom.  PI.'  (durch  falsche Trennung  aus  ÖTCoTd  aaa)  und  mit  dem  relativen  ä  verbunden  äoüa,  att. &TTa ;
lat.  quis,  quid  .wer.  was'  (fragend,  indefinit,  relativ),  qul  Adv.  .wodurch, wovon  (rel.);  wie  denn,  warum  (frag.);  irgendwie  (in  Wunschformeln)' (könnte  Abi.  *äjM  sein,  aber  doch  wohl  auf  Grund  eines  Instr.  *Ä?tz  =  av. öl,  sloven.  ci  .wenn',  cech.  H  ,oh'.  ags.  usw.  hwl  .wie.  wozu,  warum'); qul-n  (aus  -ne)  .wie  nicht ;  daß  nicht,  ohne',  quia-nam  .warum',  quia  .daß. weil'  (Akk.  PI.  *kV:i9)  s.  oben;
647
osk.  p'isj  Tpid  ,quis,  quid^  (fragend,  indefinit^  unbestimmt-relativ),  umbr. sve-pis  ,si  quis'^,  jpis-i  ^quis,  quisquis^;  gedoppelt  osk.  pispisj  lat.  quisquis, ar^iv.  TtCTtg  in  verallgemeinernd  indef.  Sinne  j
air.  cid  ^was?'  mit  dem  i  von  c-id  ^obwohl  es  sei^;  ursprüngl.  wie  das adj.  c^d  aus  *ce  ed]
air.  cia  ,wer^,  cjmY.pwy,  com.  pyw,  hvet.  piou  jWer^  (*k^ei)]  verbunden xymr.  py,  pa,  p-  usw.  (air.  cotej  cate  ,was  ist^,  ,wo  ist^  ist  unklar);
got.  Ivi-leiksj  ags.  hioilc  ,w\q  beschaffen^;  ags.  hwi,  as.  hwl,  hwiu,  aisl. hvl  ,wie,  wozu^  warum^  (Jc^l  Instr.);
abg.  ch-to  ,was^;  Instr.  te  (s.  oben)  in  sloven.  ci  ,wenn;  auch  Frage- partikel^;  öech.  H  joW,  poln.  czy  ,oV,  russ.  alt  ci  ^wenn*^,  abg.  H-mh  Instr. daraus  erweitert;
über  toch.  A  kus,  B  kuse  ^welcher^  s.  Pedersen  Toch.  121;
hitt.  Frage-  und  Relativpron.  kuiä  ^wer^  welcher^,  verallgemeinernd kui§  kui§  usw.  (=  lat.  quisquis)  ^wer  immer'^  Indefinitum  kuis-ki  (=  lat. quisque)  ^irgend  jemand^,  n.  kuit-ki  (=  lat.  quidque);  lyk.  ti-ke  (=  hitt. kuis-ki)]  s.  P.  Tedesco  Lang.  21,  128 ff.,  A.  Hahn  Lang.  22,  68 ff.
3.  Stamm  k"u~:
Ai.  kü,  av.  kü  ,wo?^,  ved.  kuv-id  ,o\),  etwa^,  av.  iSü  ,wie,  in  welchem Maße?^  (^-  nach  6l  ,wie?^);  ai.  kuva,  kvd  ,wo,  wohin*^;  ai.  kutra,  av.  kud-ra ,wo?  wohin  ?^;  ai.  kutah  ,woher';  ai.  küTia  =  gathav.  kudä  ,wo^  (=  abg. Zc-Bö^e;  idg.  *k^u-dhe]  s.  unten  lat.  uhi)]  av.  kud-a  ,wie^;  hierher  auch  ar. ku  als  1.  Zsglied  zum  Ausdruck  des  Schlechten,  Mangelhaften  (eig.  ,was für  ein  .  .  .  !^),  z.  B.  ai.  ku-putra-  , schlechter  Sohn^,  av.  ku-näiri,  ,Hure^, vgl.  böot.  TTovlLf-iOQ  , Heißhunger'  (*^^-);>  aböot.  Tlvliiiiädag,  auch  von  den Stämmen  k^o-  und  kV^i- :  ai.  ka-,  kä-,  kad-,  kim-^  z.  B.  kä-purusa-  ,Wicht', ka-püya-  ,übelriechend^,  kim-purusa-  , Kobold,  Zwerg'  (W.  Schulze  Kl. Sehr.  399 f.);
kret.  o-7tvL  , wohin',  syrak.  fivg  ("^TrvL-g),  rhod.  djtvg  , wohin'  (*^vl  neu gebildet  zu  ftoZ)]
alb.  kur  ,als,  wann'  (s.  unter  1.  B  bei  den  r-Bildungen)  =  lit.  kur, arm.  wr),  kurre  ,je'  (*kur-nei),  ku  ,wo',  ku-sh  ,wer',  kü-sh  ,wie'  (ü  aus idg.  w);
lat.  ub^  ,wo'  (dazu  unde  gebildet  nach  ihi :  inde),  woneben  inlaut.  -cuhi in  ne-cubi,  si-cuhi,  ali-cuhi,  nesciö-cuhi,  nun-cubi  (ne-cunde  usw.);  es  ist das  durch  die  Stämme  lat.  quo-,  qua,  qui  vor  der  Entlabialisierung  durch u  bewahrte  qu-  vor  u  zu  qw-  geworden  und  qicu-  hat  anl.  wu-,  u-  ergeben, während  in  *ne-qwuhi  usw.  infolge  der  Silbentrennung  neq-iouhl  der  Gutt. erhalten  blieb ;  ist  uht  nach  Lok.  auf  -l  (*ei,  *oi)  aus  *ub^  =  ai.  küha,  av. kudä,   abg.    kT>de  umgebildet  =  osk.  puf  ,ubi'   (umbr.    erweitert  zu  pufe
648
1
,ubiO?;  nach  Pedersen  Hitt.  50  f.  enthalten  uhi,  ihi  vielmehr  die  idg.  Ad- verbialenduDg-  -bhi  (gr.  -g)0;  ^g^-  ^^*^-  ^^-'^«-P^  {kwahi)  ,^o,  wann?'; entsprechend  lat.  ut  ,wie,  damit,  daß^  {uti-nam,  -que)  und  uti,  alat.  utei (Umbildung  wie  in  uhl)  aus  '^k'^u-ti  {us-^iam,  -quam  ^irgendwo'  aus  ut-}- adv.  s  =  osk.  'puz,  umbr.  jpw2-e  aus  *lc^ut-s-),  uter,  utra,  -um  ^welcher von  beiden'  aus  *k^u-teros  (parallel  mit  nötsQog  usw.),  unquam,  umquam ^irgendeinmal^  {k'^um-  temporaler  Akk.) ;  ob  umbr.  pu-e  (-o  Part.)  ,wo'  ä: ai.  kü  ist  oder  *k'^ö,  ist  fraglich;
mcymr.  cio,  ciod  (==  d),  ciot  (=  d)  ,^o,  wohin^  (*Ä;^*w-)  =  air.  co  ,wie?<|
got.  -hun  zur  Bildung  unbestimmter  Pronomina:  ni  ains-hun  ,nicht irgendeiner',  usw.;  ags.  hü  ,wie';  engl,  liow,  afries.  liü,  mnd.  loü]
lit.  kur  ,wo'  (s.  oben  1.  B);  auch  lit.  dial.  ku  ,was?'  aus  *kunl  apr.  gfitej ,wo'  aus  "^k^u-ei  und  wohl  der  Ausgangspunkt  des  qu-  statt  k-  im  fem. Nom.  gfttai,  quoi  usw. ;
WP.  I  514ff.,  WH.  I  313,  II  397 f.,  404 ff.,  408 f.,  410ff.,  Trautmann llOf.,  120f.,  133,  134,  Meillet  Slave  commun^  442ff.,  469,  Schwyzer  Gr. Gr.  1,  293  f.,  615  ff.,  Wackernagel-Debrunner  3,  558  ff.
kjirei-  ,kaufenV  Präs.  k"ri-nä-mi;  k}^roio-  ,Kauf preist
Ai.  krinäti  ,kauft'  (l  nach  krltd-  Partiz. ;  ved.  auch  krinäti  nach  Ausweis des  Metrums,  wie  auch  Päli  hinäti),  Infin.  kretum,  krayd-  ,Kauf,  Kauf- preis'; npers.  xarldan  ,kaufen';
gr.  TCQiaiiai  ,kaufe';
air.  cren{a)im  (*k^ri-nd-mi)  ,ich  kaufe',  Konj.  ni-cria  {*h^riiät),  crlth , Bezahlung,  Kauf,  crlthid  ,emax^;  cymr.  prynu  ,emere,  redimere'  (3.  Sg. acymr.  prinit),  corn.  prenne,  perna,  bret.  prena  ,kaufen',  cymr.  prid  (=  ir. crlth)  ,oppigneratio' ;  mir.  tochra  ,Umwerben'^  (,*Brautkauf'),  t-ind-s-cra n.  ,Kaufpreis  für  die  Braut'  (scheint  *kViroio-  =  ai.  krayd-) j  cymr.  g(w)o-hr ,Preis,  Belohnung^,  corn.  goher,  bret.  gohr  ds.,  cymr.  auch  go-hrwy  ds. (-i(;?/-Suffix) ;  Verbaln.  Akk.  mir.  ereicc  (formal  nach  reicc  ,verkaufen', worüber  s.  Thurneysen  Gr.  454),  air.  fochr(a)icc  f.  ,Belohnung';
alit.  (Gen.)  krieno  ,pretium  pro  sponsis',  lett.  kriens,  krienis  ,Geschenk an  die  Braut',  auch  lit.  kraitis  ,Brautschatz,  Mitgift  der  Braut^;
aruss.  krbnutij  krenuti  ,kaufen',  Infin.  hiti,  russ.-ksl.  einmal  auch  u-kri- jem  {*u-krhjem)  ,gekauft'  ohne  den  präsentischen  Nasal;
toch.  A  kuryar  ,Handel',  kuryart  ,Händler',  B  karyor  ,Kauf',  kdryorttau ,Kaufmann'.
```


## [2026-09-06T22:32:49.930Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK page 464 area ===\"; grep -n \"^464$\\|  464  \\| 464$\" POK_02.txt | head -5"
}
```


## [2026-09-06T22:32:50.805Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD kʷo ===\"; grep -n -i \"^kwo-\\|^kwi-\\|^kwo\\b\\|kwo-\\.\" AHD_watkins1985.txt | head -20; echo \"--- context\"; grep -n -A25 \"^kwo-\" AHD_watkins1985.txt | head -60"
}
```


### [2026-09-06T22:32:51.555Z] TOOL RESULT

```
=== POK page 464 area ===
1800:464
```


### [2026-09-06T22:32:51.606Z] TOOL RESULT

```
=== AHD kʷo ===
166:Stockbreeding and animal husbandry were an important part of Indo-European eco- nomic life. The names for all the familiar domesticated animals are present throughout the family: gvou-, “cow and bull,” owi-, “sheep,” ag“h-no-, ‘lamb,’ aig- and ghaido-, “goat,” sd-, “swine,” and porko-, “farrow.” The domestic dog was ancient (kwon-); its name may underlie the common Indo-European word for horse, ekwo-. The expansion and migration of the Indo- European-speaking peoples in the later third and early second millennia B.c. is intimately bound up with the diffusion of the horse. The verbal root deme-?, “to force,” acquired the special sense of “‘to tame horses,” whence English TAME. Stock was a source and meas- ure of wealth; the original sense of peku- was probably “wealth, riches,” as in Latin pecu- nia, whence “wealth in cattle” and finally “cattle” proper. The same evolution from the general to the particular may be observed in the root neud-, “to make use of,” whence English NEAT?.
433:ekwo-. Horse. Possibly originally derived from kwon-. 1. Latin equus, horse: EQUESTRIAN, EQUINE, EQUITANT, (EQUITATION); EQUISETUM. 2. Greek hippos, horse: EO- HIPPUS, HIPPOCAMPUS, HIPPOGRIFF, HIPPOPOTAMUS. [Pok. ekuo-s 301.]
655:kwo-. Also ki-. Stem of relative and interrogative pro- nouns. 1. Germanic *hwa-, hwi- in: a. personal pronouns *hwas, *hwasa, *hwam in Old English hwd, hwes, hwem, who, whose, whom: WHO, WHOSE, WHOM; b. pro- noun *hwat in Old English hwet, what: WHAT; c. adverb *hwi in Old English hwy, why: wHy; d. relative pronoun *hwa-lik- (*lik-, body, form; see lik-) in Old English hwilc, hwelc, which: WHICH; e. adverb *hwo6 in Old English hii, how: How!; f. adverb *hwan- in (i) Old English hwenne, hwanne, when: WHEN (ii) Old English hwanon, whence: WHENCE; g. adverb *hwithré in Old English hwider, whither: WHITHER; h. adverb *hwar- in Old English hwér, where: WHERE. 2. Germanic *hwatha- raz in: a. Old English hwether, hwether, which of two, whether: WHETHER; NEITHER; b. Germanic phrase *aiwo gihwatharaz, “ever each of two” (*aiwo, *aiwi, ever; see aiw-; *gi- from *ga-, collective prefix; see kom), in Old English €ghwether, &ther, either: EITHER. 3. Latin gui, who (genitive plural guérum): QUA, QUIB- BLE, QUORUM. 4. Latin quid, what, something: HIDALGO, QUIDDITY, QUIDNUNC, QuIP. 5. Latin quam, as, than, how, in quasi (quam + si, if; see swo-), as if: QUASI. 6. Latin quod, what: QUODLIBET. 7. Latin quot, how Many: QUOTE, QUOTIDIAN, QUOTIENT; ALIQUOT. 8. Latin quom, when: QUONDAM. 9. Latin quem, whom: CON- QUIAN. 10. Latin quantus, how great: QUANTITY. 11. Latin gudlis, of what kind: QuALITY. 12. Latin ut, that: (uT). 13. Latin uter, either of two: NEUTER. 14, Latin ubi, where, and ibi, there: ALIBI, UBIQUITY. 15. Persian chiz, thing: CHEESE, [Pok. k¥o- 644.] kwon-. Dog. 1. Greek kudn, dog: CYNIC; CYNOSURE, PROCYON, QUINSY. 2. Suffixed zero-grade form “kwn-to- in Germanic *hundaz in: a. Old English hund, dog: HOUND; b. Old High German Aunt (> German Hund), dog: DACHSHUND; c. Dutch hond, dog: KEESHOND. 3. Nominative form *kw6o in Welsh ci, dog: CORGI. 4. Variant *kan-i- in Latin canis, dog: CANAILLE, CA- NARY, CANICULA, CANINE, CHENILLE, KENNEL}, [Pok. Ruon- 632.]
1057:swo-. Pronominal stem; so. Derivative of s(w)e-. 1. Ger- manic *swa- in: a. Old English swd, so: sol; b. Germanic compound *swa-lik-, “so like,” of the same kind (*/ik-, same; see lik-), in Old English swylc, such: sucH. 2. Ad- verbial form *swai in Latin si, if, in quasi (quam, as; see kWo- + si, if): NISI, QUASI. [In Pok. 2. seu- 882.] s(w)okwo-. Resin, juice. Variant form *sokvo- in Greek opos (< *hopos), juice: opruM. [Pok. s(wekvo-s 1044.] swombho-. Spongy. Germanic *swamba- in: a. Middle Low German sump, swamp: SUMP; b. Low German zwamp, swamp, akin to the Low German source of swamp. [Pok. suomb(hjo-s 1052.]
1172:*wer-ald., “life or age of man” (*-ald-, age; see al-3), in Old English weorold, world: woRLD; c. Frankish *wer- wulf, “man-wolf” (*wulf, wolf; see wikvo-), in French garou, werewolf: LOUP-GAROU. 2. Latin vir, man: VI- RAGO, VIRILE, VIRTUE, (VIRTUOSA), (VIRTUOSO); DECEM- VIR, DUUMVIR, TRIUMVIR. 3. Possibly Latin ciria, curia, court, if regarded as from *co-vir, “men together” (co-, together; see kom): CURIA. [Pok. uiro-s 1177.] wleik-. To flow, run. Zero-grade form *wlik-. 1. Adjective *wlik-u-, wet, in: a. suffixed form *wlik-w-d- in Latin liquare, to dissolve: LIQUATE; b. suffixed form *wlik-w-é- in Latin liquére, to be liquid: LIQUESCENT, LIQUID, LIQUOR; DELIQUESCE, LIQUEFY. 2. Suffixed form *wlik-s- in: a. Latin lixa, lye: LIXIVIATE; b. Latin prélixus, poured forth, stretched out in front, extended (pro-, forth; see per’): PROLIX. [In Pok. leiku- 669.] wlkwo-. Wolf. 1. Germanic *wulfaz in: a. Old English wulf, wolf: WOLF; b. Middle Dutch wolf, wulf, wolf: AARDWOLF; Cc. Old High German wolf, wolf, in German Wolfram, tungsten: WOLFRAM; d. Frankish *wulf, wolf (see wi-ro-). 2. Taboo variant */upo- in Latin lupus, wolf: LOBO, LUPINE!, LUPINE?; LOUP-GAROU. 3. Taboo variant *luko- in: a. Greek lukos, wolf: LYCANTHROPE, LYCOPO- piuM; b. Suffixed form */uk’-ya in Greek lussa, martial rage, madness, rabies (“wolf-ness”): LYTTA; ALYSSUM. [Pok. ulkvos 1178.] wip-6-. Fox. 1. Latin vulpés, fox: VULPINE. 2. Taboo variant *slépek- in Greek alépéx, fox: ALOPECIA. [Pok. ulp-, lup- 1179.] wogYh-ni-. Plowshare, wedge. 1. Probably Germanic *wagjaz in Old English wecg, wedge: WEDGE. 2. Prob- ably Latin vdmer, plowshare: vOMER. [Pok. wog¢hni-s 1179.] wokso-. Wax. Related to weg-!. Germanic *wahsam in Old English wex, weax, wax: WAX!. [Pok. uokso- 1180.] wopsa. Wasp. Metathesized form *wospd. 1. Germanic *wosp- in Old English wesp, weps, wasp: wAsP. 2. Latin vespa, wasp: VESPIARY. [Pok. yobhsd 1179.] wos. You (plural). Latin vds (> Old French vous), you: RENDEZVOUS. [In Pok. 1. iu- 513.] wrad-. Branch, root. I. Basic form *wrdd- in Germanic *wrét- in Old Norse rét, root: ROOT!; RUTABAGA. II. Zero-grade form *wred-. 1. Germanic *wurtiz in: a. Old English wyrt, plant, herb: wort; b. German Wurzel (< *wurzwala, rootstock; *-wala, a roll, round stem; see wel-3), root: MANGELWURZEL. 2. Latin rddix, root: RACE3, RADICAL, RADICLE, RADISH, RADIX; DERACI- NATE, ERADICATE. 3. Suffixed form *wrod-mo- in Latin rdmus, branch: RAMOSE, RAMUS; RAMIFY. 4. Suffixed reduced form *wr(e)d-ya perhaps in Greek rhiza, root: RHIZO-, RHIZOME; COLEORHIZA, LICORICE, MYCORRHIZA. [Pok. ufe)rad- 1167.] wragh-. Thorn, tip. Greek rhakhis, ridge, spine: RACHIS. [Pok. 1. uragh- 1180.] wreg-. To push, shove, drive, track down. I. Basic form *wreg- in Germanic *wrekan in: a. Old English wrecan, to drive, expel: WREAK; b. Old Norse rek (older form urek), wreckage, akin to the Scandinavian source of Anglo-Norman wrec, wreck: WRECK. II. O-grade form *wrog-. 1. Germanic *wrakjén-, “pursuer, one pursued,” in: a. Old English wrecca, exile: WRETCH; b. Frankish *wrakjo, “one pursued, an exile,” perhaps in French garce, a girl: GASKET. 2.Germanic *wrakaz in: a. Old English wrzc, exile, punishment, and Middle Dutch wrak, wreckage: WRACK}; b. Swedish rak, wreckage, akin to the source of Middle English rak, mass of driven clouds: RackK®. III. Zero-grade form “wrg-eyo-, “urg-eyo- in Latin urgére, to urge, drive: URGE. [Pok. ureg- 1181.] wrég-. To break. Suffixed form *wrég-nu- in Greek rhégnunai, to burst forth: -RRHAGIA. [Pok. urég- 1181.] [wrod-. Rose. A word (not common Indo-European) of unknown origin. 1. Suffixed form *wrod-o- in Greek rhodon, rose: RHODO-; (RHODIUM). 2. Suffixed form *wrod-ya- (perhaps via Etruscan) in Latin rosa, rose:
--- context
655:kwo-. Also ki-. Stem of relative and interrogative pro- nouns. 1. Germanic *hwa-, hwi- in: a. personal pronouns *hwas, *hwasa, *hwam in Old English hwd, hwes, hwem, who, whose, whom: WHO, WHOSE, WHOM; b. pro- noun *hwat in Old English hwet, what: WHAT; c. adverb *hwi in Old English hwy, why: wHy; d. relative pronoun *hwa-lik- (*lik-, body, form; see lik-) in Old English hwilc, hwelc, which: WHICH; e. adverb *hwo6 in Old English hii, how: How!; f. adverb *hwan- in (i) Old English hwenne, hwanne, when: WHEN (ii) Old English hwanon, whence: WHENCE; g. adverb *hwithré in Old English hwider, whither: WHITHER; h. adverb *hwar- in Old English hwér, where: WHERE. 2. Germanic *hwatha- raz in: a. Old English hwether, hwether, which of two, whether: WHETHER; NEITHER; b. Germanic phrase *aiwo gihwatharaz, “ever each of two” (*aiwo, *aiwi, ever; see aiw-; *gi- from *ga-, collective prefix; see kom), in Old English €ghwether, &ther, either: EITHER. 3. Latin gui, who (genitive plural guérum): QUA, QUIB- BLE, QUORUM. 4. Latin quid, what, something: HIDALGO, QUIDDITY, QUIDNUNC, QuIP. 5. Latin quam, as, than, how, in quasi (quam + si, if; see swo-), as if: QUASI. 6. Latin quod, what: QUODLIBET. 7. Latin quot, how Many: QUOTE, QUOTIDIAN, QUOTIENT; ALIQUOT. 8. Latin quom, when: QUONDAM. 9. Latin quem, whom: CON- QUIAN. 10. Latin quantus, how great: QUANTITY. 11. Latin gudlis, of what kind: QuALITY. 12. Latin ut, that: (uT). 13. Latin uter, either of two: NEUTER. 14, Latin ubi, where, and ibi, there: ALIBI, UBIQUITY. 15. Persian chiz, thing: CHEESE, [Pok. k¥o- 644.] kwon-. Dog. 1. Greek kudn, dog: CYNIC; CYNOSURE, PROCYON, QUINSY. 2. Suffixed zero-grade form “kwn-to- in Germanic *hundaz in: a. Old English hund, dog: HOUND; b. Old High German Aunt (> German Hund), dog: DACHSHUND; c. Dutch hond, dog: KEESHOND. 3. Nominative form *kw6o in Welsh ci, dog: CORGI. 4. Variant *kan-i- in Latin canis, dog: CANAILLE, CA- NARY, CANICULA, CANINE, CHENILLE, KENNEL}, [Pok. Ruon- 632.]
656-kerep-. Body. 1. Suffixed form *krep-es- in Germanic *hrifiz in Old English Arif, belly: MipRIFF. 2. Suffixed zero-grade form *krp-es- in Latin corpus, body, sub- stance: CORPORAL, CORPORAL’, CORPORATE, CORPOREAL, CORPOSANT, CORPS, CORPSE, CORPULENCE, CORPUS, COR- PUSCLE, CORSAGE, CORSE, CORSET; LEPRECHAUN. [Pok. 1. krep- 620.]
657-kermi-. Mite, worm. Rhyme word to *wrmi-, worm (see wer-3). Sanskrit krmi-, worm, in compound krmi-ja-, “(red dye) produced by worms” (ja-, produced; see gene-), borrowed into Arabic as girmiz, kermes: (CRIM- SON), KERMES. [Pok. kermi- 649.]
658-la-. Echoic root. 1. Middle Dutch Jollen, to mutter, akin to the Low German source of Middle English Jlollen, to loll: LOLL. 2. Middle Low German lollen, to lull, akin to the Low German source of Middle English Jud/en, to lull: LULL. 3. Old Norse lémr, loon: LOON}. 4. Latin lamen- tum, expression of sorrow: LAMENT. 5. Greek /alos, talk- ative: ECHOLALIA. 6. Greek Jalein, to talk: GLOSSOLALIA. [Pok. 1. la- 650.]
659-lab-. Lapping, smacking the lips; to lick. Variant of leb-?. 1. Germanic */apjan in Old English lapian, to lap up: LAP’, 2. Nasalized form */a-m-b- in: a. Germanic */amp- in French damper, to gulp down: Lampoon; b. Latin lambere, to lick: LAMBENT. [Pok. /ab- 651.]
660-ladh-
661-ladh-. To be hidden. 1. Greek léthé, forgetfulness: LETH- ARGY, LETHE. 2. Zero-grade form *ladh- (< *bdh-), with nasalized form *landh-, in Greek lanthanein (aorist lathein), to escape the notice of, with middle anthanes- thai, to forget: LANTHANUM; ALASTOR. 3. Suffixed (sta- tive) variant form */at-é- in Latin latére, to lie hidden: LATENT. [In Pok. 2. /a- 651.] laiwo-. Left. Latin Jaevus, left: LEVO-; (LEVOROTATION), (LEVOROTATORY). [Pok. laiuo- 652.] laks-. Salmon. Suffixed form */aks-o- in Germanic */ahs- az in Old High German Jahs, salmon: Lox}. [Pok. lak- 653.] laku-. Body of water, lake, sea. 1. Latin /acus, lake, pond, basin: LAKE!. 2. Greek lakkos, cistern: LACCOLITH. 3. O-grade form *loku- in Old Irish and Scottish Gaelic loch, lake: LocH, LouGH. [Pok. laku- 653.] lap-. To light, burn. Nasalized shortened form */a-m-p- in Greek lampein, to shine: LAMP, LANTERN; ECLAMPSIA. [Pok. la(i)p- 652.] las-. To be eager, wanton, or unruly. 1. Suffixed Ger- manic zero-grade form *lustuz in: a. Old English Just, lust: Lust; b. Old High German Just (> German Lust), desire: WANDERLUST; Cc. Germanic denominative verb *lustjan in Old English lystan, to please, satisfy a desire: LisT’, 2. Suffixed form */as-ko- in Latin lJascivus, wan- ton, lustful: Lascivious. [Pok. las- 654.] lat-. Wet, moist. Latin latex, liquid: LaTEx. [Pok. Jat- 654.] lau-. Gain, profit. 1. Suffixed form */au-no- in Germanic *Jaunam in Old High German J6n, reward: GUERDON. 2. Suffixed zero-grade form */u-tlo- in Latin lucrum, gain, profit: LUCRATIVE, LUCRE. 3. Suffixed variant form *low-ero- in Irish Gaelic ledr, sufficiency, enough: GA- LORE. [Pok. ldu- 655.] lé-1. To get. Contracted from “lea-. Suffixed zero-grade form *b-tr- in: a. Greek Jatreia, service (for pay), duties, worship: -LATRY; b. Greek Jatron, pay, akin to the Greek source of Latin latré, robber: LARCENY; c. Greek -/latrés, worshiper: IDOLATER. [Pok. 2. /é(i)- 665.] lé-2, To let go, slacken. Contracted from *les-. 1. Ex- tended form */éd- in: a. Germanic */étan in Old English létan, to allow, leave undone: LET!; b. Germanic deriva- tive *léthigaz, freed, in Medieval Latin /étus, litus, serf (< “free man”): LIEGE. 2. Extended zero-grade form */d- in: a. Germanic */ataz in Old English Zt, late, with its comparative lztra, latter, and its superlative Jatost, last: LATE, LATTER, LAST!; b. Germanic */atjan in Old English lettan, to hinder, impede (< “to make late”): LET?; c. suffixed form */od-to- in Latin lassus, tired, weary: LASSITUDE; ALAS. 3. Suffixed reduced form */é-ni- in Latin lénis, soft, gentle: LENIENT, LENIS, LENITIVE, LENITY. [Pok. 3. lé(i)- 666.] leb-'. Base of loosely related derivatives meaning “hang- ing loosely.” I. Variant form *lep- in Germanic */ap- in Old English lzppa, lappa, flap of a garment: Lap’. II. Nasalized form *lemb(h)-, with variant form *slemb(h)-. 1. Germanic *lemp- probably in obsolete English limphalt, lame (halt, lame; see kel-'): LIMP. 2. Germanic */ump- in: a. Dutch lomp, rag, akin to the Low German source of Middle English Jump, lump: LUMP!; b. possibly obsolete English Jump, lumpfish: LUMPFISH; Cc. German Lumpen, rags: LUMPEN. 3. Ger- manic *slimp- in Middle Dutch slim(p), slanting, bad: SLIM. 4, Middle High German slam, mud: SLUMGULLION. 5. Old Norse slambra, to strike at, akin to the Scandina- vian source of SLAM!. 6. Norwegian slumpa, to slump, akin to the Scandinavian source of sLuMpP. III. Variant *(s)lab- in Germanic *s/ab-. 1. Danish slab, mud, akin to the Scandinavian source of SLAB2. 2. Swedish slabb, slime, mud, akin to the Scandinavian source of Irish slab, mud: sLos. IV. Variants *slap-, *slep-. Germanic *slap- in: a. Low German s/app, slap: SLAP; b. Old Norse slafra, to slaver: SLAVER}. V. Variant */ab-. 1. Germanic *lab- in Old French label, ribbon, strip: LABEL. 2. Latin
662-lei-
663-labi (past participle /apsus), to fall, slip: LABILE, LAPSE; COLLAPSE, ELAPSE, PRELAPSARIAN, PROLAPSE, RELAPSE, SUPRALAPSARIAN. 3. Suffixed form */ab-os- perhaps in Latin labor, labor, toil, exertion: LABOR; COLLABORATE, ELABORATE. (But both Latin /abi and Jabor may belong to a root *sléb.) VI. O-grade form *lob- in Greek lobos, lobe: LOBE. [Pok. /éb- 655.]
664-leb-2. Lip. 1. Germanic */ep- in Old English lippa, lip: Lip. 2. Variant form Jab- in: a. suffixed form */ab-yo- in Latin labium, lip: LABIAL, LABIUM; b. suffixed form */ab-ro- in Latin labrum, lip: LABELLUM, LABRET, LABRUM. Com- pare lab-. [Pok. léb- 655.]
665-leg-'. To collect; with derivatives meaning “to speak.” 1. Perhaps Germanic */ékjaz, enchanter, one who speaks magic words, in Old English /éce, physician: LEECH). 2. Latin legere, to gather, choose, pluck, read: LECTERN, LECTION, LECTURE, LEGEND, LEGIBLE, LEGION, (LES- SON); (COIL!), COLLECT!, DILIGENT, ELECT, INTELLIGENT, NEGLECT, PRELECT, SACRILEGE, SELECT, SORTILEGE. 3. Greek legein, to gather, speak: LEXICON; ALEXIA, ANALECTS, BRADYLEXIA, CATALOGUE, DIALECT, (DIA- LOGUE), DYSLEXIA, ECLECTIC, EPILOGUE, PROLEGOM- ENON. 4. Suffixed form */eg-no- in Latin lignum, wood, firewood (< “that which is gathered”): LIGNEOUS, LIGNI-. 5. Lengthened-grade form */ég- possibly in: a. Latin léx, law (? < “collection of rules”): LEGAL, LEGIST, LEGITI- MATE, LEX, LOYAL; LEGISLATOR, PRIVILEGE; b. Latin denominative légdre, to depute, commission, charge (< “to engage by contract”; but possibly from legh-): LEGACY, LEGATE; ALLEGE, COLLEAGUE, (COLLEGIALITY), DELEGATE, RELEGATE. 6. Suffixed o-grade form *log-o- in Greek logos, speech, word, reason: LOGIC, LOGISTIC, LOGO-, LOGOS, -LOGY; ANALOGOUS, APOLOGUE, APOLOGY, DECALOGUE, HOMOLOGOUS, LOGARITHM, PARALOGISM, PROLOGUE, SYLLOGISM. [Pok. leg- 658.]
666-leg-2. To dribble, trickle. Germanic “/ek- in: a. Middle English leke, a leak: LEAK; b. Middle English lack, deficiency: LACK. [Pok. 1. leg- 657.]
667-legh-. To lie, lay. 1. Suffixed form *leg-yo- in: a. Ger- manic */igjan in Old English licgan, to lie: LIE!; b. Ger- manic *lagjan in (i) Old English lecgan, to lay: Lay}, LEDGE, (LEDGER) (ii) Old English belecgan, to cover, surround (be-, over; see ambhi): BELAY. 2. Suffixed form *leg-ro- in Germanic *legraz in: a. Old English Jeger, lair: LAIR; b. Dutch /eger, lair, camp: LEAGUER!; BELEA- GUER; c. Old High German Jegar, bed, lair (> German Lager, store, and Afrikaans lager, laager): LAAGER, LAGER; (STALAG). 3. Celtic *leg-yd- in Medieval Latin lia, sediment: LEES. 4. Lengthened-grade form *légh- in Germanic */égaz, “lying flat,” low, in Old Norse Jagr, low: Low!. 5. Suffixed form */egh-to- in Latin lectus, bed: LITTER; WAGON-LIT. 6. Suffixed o-grade form *logh-o- in Germanic */agam in: a. Old Norse *lagu, lag-, law, “that which is set down” (> Old English Jagu, law): LAW; DANELAW; b. Old Norse Jag, a laying down: FELLOW; c. Old Norse lég, law: OUTLAW; d. Old High German laga (> Middle High German lage > German Lage), act of laying: ANLAGE, VORLAGE. 7. Suffixed o-grade form *logh-o- in Greek lokhos, childbirth, place for lying in wait: LOCHIA. [Pok. legh- 658, 2. légh- 660.]
668-legwh-. Light, having little weight. 1. Suffixed form *legeh-t- in Germanic */iht()az in: a. Old English Jiht, léoht, light: LicHT?; b. Old English /ihtan, to lighten: LIGHTER?. 2. Suffixed form *legvh-u-i- in Latin levis (> Old French Jeger), light, with its derivative levdre, to lighten, raise: LEAVEN, LEVER, LEVITY; ALLEVIATE, CARNIVAL, ELEVATE, LEGERDEMAIN, LEVIGATE, (MEZZO-RELIEVO), RELIEVE. 3. Variant form *lagvh- in Old Irish /i-, small: LEPRECHAUN. 4. Nasalized form *l(e)ngeh- in Germanic *lung- in Old English lungen, lungs (from their lightness): LUNG. 5. Attributed by some to this root is Latin oblivisci, to forget, which is more likely from lei-. [Pok. legzh- 660.]
669-lei-. Also slei-. Slimy. 1. Germanic *sli- with various
670-1éi-
671-extensions in: a. Old English slim, slime: sLIME; b. Old English slipor, slippery: SLIPPERY; Cc. Old English *slice, smooth (> Middle English slike, smooth): sLick; d. Old English lim, cement, birdlime: LIME; e. Old English lam, loam: LOAM; f. Old Norse s/éttr, smooth, sleek, akin to the probable Scandinavian source of Middle English slight, slender: SLIGHT; g. Middle Dutch and Middle Low German slippen, to slip, slip away, akin to the probable source of Middle English slippen, to slip: sL1P!; h. Middle Low German slépen, to drag: SCHLEP. 2. Suffixed form *lei-mo- in Latin limus, slime: LIMACINE, LIMICOLINE. 3. Suffixed form */ei-w- in Latin oblivisci (ob-, away; see epi), to forget (< “to wipe, let slip from the mind”): OBLIVION, OUBLIETTE. 4. Extended form *(sjleia- in: a. nasalized zero-grade form */i-n-a- in Latin linere, to anoint: LINIMENT; b. Suffixed zero-grade form *li- (< *lig-) in Greek litos, plain, simple: LiToTEs. [Pok. 3. lei- 662.] léi-. Also lei-. To flow. 1. Extended form “/eib- in Latin libdre, to pour out, taste: LIBATION; PRELIBATION. 2. Possibly suffixed extended form */eit-os- in Latin litus, shore: LITTORAL. [Pok. 4. lei- 664.] leid-. To play, jest. Suffixed o-grade form *loid-o- in Latin lidus, game, play, with its derivative lidere, to play (but both words may possibly be from Etruscan): LUDICROUS; ALLUDE, COLLUDE, DELUDE, ELUDE, ILLU- SION, INTERLUDE, PRELUDE, PROLUSION. [Pok. leid- 666.] leie-. To waste away. Zero-grade form “li- (< *lia-) in Greek limos, hunger, famine: BULIMIA. [In Pok. 2. lei- 661.] leig-'. To bind. 1. Germanic */ik- in Middle Low German lik, leech line: LEECH?. 2. Zero-grade form */ig-d- in Latin ligare, to bind: LEAGUE!, LEGATO, LIABLE, LIEN, LIGASE, LIGATE; ALLOY, (ALLY), COLLIGATE, COLLIGATIVE, FURL, OBLIGE, (RALLY), RELY. [Pok. 4. leig- 668.] leig-?. Poor. Perhaps Greek oligos, few, little: OLIGO-. [Pok. 1. leig- 667.] leig-5. To leap, tremble. O-grade form */oig- in Germanic *laik- in: a. Old English -lac, suffix denoting activity: WEDLOCK; b. Old Norse leika, to play: LARK?. [Pok. 3. leig- 667.] leigh-. To lick. 1. Greek leikhein, to lick: ELECTUARY. 2. Zero-grade form *lig- in Germanic *likk6n in: a. Old English liccian, to lick: Lick; b. Old French lechier, to live in debauchery: LECHER. 3. Nasalized zero-grade form *ling- in Latin lingere, to lick: ANILINGUS, CUNNI- LinGus. [Pok. leigh- 668.] leikw-, To leave. 1. Basic form *leikv- in Greek leipein, to leave: ECLIPSE, ELLIPSIS. 2. O-grade form *loikv- in: a. Germanic */aihwnjan in Old English lénan, to lend, give (< “to leave to”): LEND; b. suffixed form *loikv-nes- in Germanic */aihwniz in Old Norse Jan, loan: LOAN. 3. Zero-grade form *likv- in Germanic *-lif-, left, in: a. Germanic *ain-lif-, “one (beyond ten),” in Old English endleofan, eleven (see oi-no-); b. Germanic *twa-lif-, “two left (beyond ten),” in Old English twelf, twelve (see dwo-). 4. Nasalized zero-grade form *li-n-kv- in Latin linquere, to leave: DELINQUENT, DERELICT, RELINQUISH. [Pok. leike- 669.] leip-. To stick, adhere; fat. 1. Germanic *libam in Old English Jif, life (< “continuance”): LIFE, LIVELY. 2. Ger- manic “libén in Old English lifian, libban, to live: LIVE}. 3. Germanic */aibjan in Old English léfan, to leave, have remaining: LEAVE!. 4. Germanic “libro in Old English lifer, liver (formerly believed to be the blood-producing organ): LIVER}. 5. Zero-grade form *lip- in Greek lipos, fat: L1po-. 6. Variant form *aleibh- in Greek aleiphein, to anoint with oil (> aleiphar, unguent): ALIPHATIC; SYNA- LEPHA. [Pok. eip- 670.] leis-'. Track, furrow. 1. O-grade form *lois- in: a. Ger- manic */aist- in Old English Jast, lést, sole, footprint: Last’; b. Germanic */laistjan, “to follow a track,” in Old English /éstan, to continue: LAST?; c. suffixed form *lois-G in Germanic */aiz6 in Old English Jar, learning:
672-36
673-leu-'
674-LORE!. 2. Germanic zero-grade form *lizndn, “to follow a course (of study),” in Old English leornian, to learn: LEARN. 3. Suffixed full-grade form */eis-G in Latin lira, a furrow: DELIRIUM. [Pok. /eis- 671.]
675-leis-?. Small. Germanic comparative */ais-iz(a) and super- lative */ais-ista- in Old English comparative lés, léssa and superlative ést, rest: LEAST, LESS.
676-leit-'. To detest. 1. Germanic */aithaz in Old English lath, loathsome: LOATH. 2. Germanic */aithén in Old English lathian, to loathe: LOATHE. [Pok. 1. leit- 672.]
677-leit-2. To go forth, die. 1. Suffixed o-grade form *loit-eyo- in Germanic *laidjan in: a. Old English dan, to lead: LEAD!, b. Old High German /eiten, to lead: LEITMOTIF. 2. Suffixed variant o-grade form *loit-4 in Germanic *laid6é in Old English /éd, course, way: LOAD, LODE; LIVELIHOOD. [Pok. leit(h)- 672.]
678-leizd-. Border, band. Germanic */ist6n- in: a. Old English liste, border, edge, strip: LisT?; b. Old Italian lista, border, strip of paper, list: List. [Pok. leizd- 672.]
679-lek-. To leap, fly. Possibly suffixed o-grade form */ok-ost- in Latin locusta, locusta, a marine shellfish, lobster: LOBSTER, Locust. [Pok. 2. lek- 673.]
680-lék-. To tear. Zero-grade form *bk- becoming Jak-. 1. Latin dacinia, flap of a garment: LACINIATE. 2. Suf- fixed form *lak-ero- in Latin lacer, torn: LACERATE. [Pok. 2. lék- 674.]
```


## [2026-09-06T22:32:58.493Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1794,1806p' POK_02.txt | cut -c1-400"
}
```


### [2026-09-06T22:32:58.545Z] TOOL RESULT

```
arm.  kam  ,stehe^  ( :  gr.  eßrjv)  ;
gr.  *ßlßr]GLj  ßißdg,  kßrjv  s.  oben;  ßrjzaQfiög  ,Tanz'^,  ßr]raQ{.i(Dv  ,Tänzer*^ (aus  *ßäTog  oder  *ßacä  ,das  Fußaufsetzen^  -]-^'?.""  ,Gefüge^);  äi.LcpLGßrjiiw,  ion. a(.iq)L(TßäT€(jü  ,streite'  (,nach  zwei  Seiten  auseinandergehend^),  ßfj!,ia  n.  ,Schritt^ ablautend  ßioixög  m.  ,Tritt,  Stufe,  Gestell,  Altar^;  Infinitiv  ßrjf,ievaL]  ßrjXög m.  
alb.  ngä  ,ich  laufe'  (*ga-niö)]
lit.  dial.  göti  ,gehen';  lett.  gäj^i  (Prät.  zu  iet)  ,ich  ging'  (setzt  ein  Präs. ^gäiö  voraus,  dessen  j  präsensbildend  sein  wird),  davon  weiter  gäjums ,Gang,  Reihe';  gäita  ,Gang'  (mit  analogischem  ai,  Endzelin  Lett.  Gr. S.  678);  gätis  PL  ,Fluglöcher  der  Bienen';  lit.  pröga  ,Gelegenheit,  Frist' (Präfix  *prai  -\-  gä) ;  lit.  gätve  ,Straße,
gang' sind  germ.  Lw.
Vielleicht  hierher  auch  die  kelt.  Worte  für  ,sterben'  (als  , fortgehen', ix  ßqoTvbv  ßfjvat),  wie  air.  bald  ,stirbt'  (*bä-a-ti  aus  *g^ä-)j  at-bath  ,starb' {*-gud-t  .  .),  bath  ,Tod'  =  cymr.  bad  ,Pest',  bret.  bad  ,Betäubung',  corn. bad-us  ,wahnsinnig';  air.  bäs  ,Tod'  ist  nach  gnäs  ,Gewohnheit'  usw.  gebildet.
464
Trotz  Thurneysen  Gr.  §§  547,  728  ist  ein  Stamm  hus-  nicht  nachzuweisenj  |^ s.  richtiger  Pedersen  Litteris  2,  89  f.  -^^'
2.  g'iem-'.  ^:},'
Unthematisch  *{e)-gi}em-t  (>  *e-guen-t),  -gMm-te,  -gnm-ent  im  ai.  Aor.  dgan,  '-  ■ gan  (g  für  j  nach  Formen  mit  ursprünglichem  *g^7ri-,  *gum-'^  1.  Sg.  dgamam\ dgata   {*g'^m-),  dgman,   dgmata]    gthav.    3.  Sg.   Inj.   uz-J9n,   3.  PI.   ^»T/ian;
arm.  3.  Sg.  ekn  ,er  kam'  (=  ai.  dgan)-,  über  die  noch  unklare  1.  Sg.  eki, 3.  PI.  ekin  siehe  Meillet  Esquisse  134  f.;
gr.  ßdTTjv  3.  Du.,  vnsQßäaav  3.  PL  wohl  zur  Wurzelf.  *^?^ä-;
Konj.  *gi^emeti  in  ai.  gdm-at,  -anti,  gthav.  jamaHi,  jimaHi]  Opt.  gurji. jet  in  ai.  gamyät,  av.  jamyät,  ap.  jawjä''  {J  für  g  aus  Formen  mit  hoch- stufigem idg.  *guem-) ;  ags.  cyme  s.  unten ;
```


## [2026-09-06T22:33:10.235Z] TOOL CALL #18: Bash

```json
{
 "command": "pdftoppm -f 297 -l 297 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg297 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-06T22:33:12.457Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT kō ===\"; grep -n \"^kā-,\\|kǝ-, kā-\\|ka-, kā-\\|^kō\\b\" BRT.txt | head -20; echo \"=== BRT kuθra ===\"; grep -n \"kuθra\\|kuδra\\|kuθrā\" BRT.txt | head -10; echo \"=== BRT katāra ===\"; grep -n \"katāra\\|katama\\|kada\\b\\|kaθa\\b\" BRT.txt | head -20"
}
```


### [2026-09-06T22:33:12.901Z] TOOL RESULT

```
total 118932
drwx------ 5 sfmqrb sfmqrb    12288 Sep  6 18:33 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb   416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb      814 Sep  6 18:31 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  5157031 Sep  6 18:05 aiw.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    26688 Sep  6 18:20 ary377_bot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71464 Sep  6 18:20 ary377_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71267 Sep  6 18:19 ary378_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25966 Sep  6 18:19 ary378_top_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   127656 Sep  6 18:17 bqt1267_foot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb   362419 Sep  6 17:50 bqt1583_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105420 Sep  6 18:16 bqt27.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   703015 Sep  6 17:50 bqt_fn4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299015 Sep  6 17:50 bqt_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   325427 Sep  6 17:50 bqt_n552.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   315487 Sep  6 17:50 bqt_n553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   330101 Sep  6 17:50 bqt_n554.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   560485 Sep  6 17:53 bqtv2_650_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   541712 Sep  6 17:53 bqtv2_651_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9689 Sep  6 18:33 bqtv2_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   729454 Sep  6 17:53 bqtv2_n650.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   702551 Sep  6 17:53 bqtv2_n651.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   100817 Sep  6 17:36 bqt_v3_111.png
-rw-rw-r-- 1 sfmqrb sfmqrb   110820 Sep  6 17:36 bqt_v3_112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   137595 Sep  6 18:10 buck2.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      146 Sep  6 18:10 buck3.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52615 Sep  6 17:36 build275.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74145 Sep  6 17:43 build278.py
-rw-rw-r-- 1 sfmqrb sfmqrb    72342 Sep  6 17:58 build283.py
-rw-rw-r-- 1 sfmqrb sfmqrb    28249 Sep  6 18:25 build290a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63778 Sep  6 18:33 build290b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68833 Sep  6 18:30 build291.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb 60831599 Sep  6 18:01 cad_k.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  2530822 Sep  6 18:01 cad_k.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2612 Sep  6 18:28 c_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13418 Sep  6 18:28 c_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8430 Sep  6 18:28 c_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11245 Sep  6 18:28 c_katrang.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6717 Sep  6 18:28 c_katvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28872 Sep  6 18:28 c_katvar_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 18:09 cpd.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 18:09 cpd.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  2144625 Sep  6 17:55 dmmpp.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14732 Sep  6 18:27 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17126 Sep  6 17:54 e1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    18004 Sep  6 17:56 e2.json
-rw-rw-r-- 1 sfmqrb sfmqrb  5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1845041 Sep  6 18:04 gharib.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3698758 Sep  6 17:50 IEC_full_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb     4265 Sep  6 17:53 kapi_script.png
-rw-rw-r-- 1 sfmqrb sfmqrb   944060 Sep  6 18:06 kent_full.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   288525 Sep  6 18:07 kent_n222.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   285652 Sep  6 18:07 kent_n223.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282304 Sep  6 18:07 kent_n224.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   268920 Sep  6 18:07 kent_n225.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb    73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51778 Sep  6 17:32 mk276.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46494 Sep  6 17:52 mk279.py
-rw-rw-r-- 1 sfmqrb sfmqrb    16605 Sep  6 17:54 mk280b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17667 Sep  6 17:56 mk280c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    43177 Sep  6 17:50 mk280.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58322 Sep  6 17:51 mk282.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63940 Sep  6 18:05 mk285.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67974 Sep  6 18:09 mk286.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60646 Sep  6 18:11 mk287.py
-rw-rw-r-- 1 sfmqrb sfmqrb    14748 Sep  6 18:27 mk292.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41011 Sep  6 18:29 mk294.py
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb    10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb    14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb    25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb   105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53703 Sep  6 17:22 p275_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7106 Sep  6 17:34 p279_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    12970 Sep  6 17:34 p279_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3647 Sep  6 17:34 p279_xsaeta.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130651 Sep  6 17:48 p283_arrow.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:02 p284
-rw-rw-r-- 1 sfmqrb sfmqrb    43108 Sep  6 17:51 p284_e0_fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89734 Sep  6 17:51 p284_e0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59639 Sep  6 17:48 p284_e2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106502 Sep  6 17:48 p284_e2.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:25 p289
-rw-rw-r-- 1 sfmqrb sfmqrb    54419 Sep  6 18:05 p289_labibi.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:33 p290
-rw-rw-r-- 1 sfmqrb sfmqrb     1476 Sep  6 18:11 p291_esfand.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31043 Sep  6 18:11 p291_root.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66829 Sep  6 17:28 pg273_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70615 Sep  6 17:27 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44171 Sep  6 17:16 pg277.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89267 Sep  6 17:26 pg278.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168655 Sep  6 17:34 pg279hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75777 Sep  6 17:34 pg279.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82065 Sep  6 17:34 pg280.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61535 Sep  6 17:39 pg281.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70575 Sep  6 17:34 pg282.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74784 Sep  6 17:47 pg283.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:50 pg284hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:51 pg284.png
-rw-rw-r-- 1 sfmqrb sfmqrb   144566 Sep  6 17:49 pg284_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84487 Sep  6 17:53 pg285.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106264 Sep  6 17:53 pg286hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76099 Sep  6 18:10 pg286.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72442 Sep  6 17:59 pg287.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53847 Sep  6 17:58 pg288.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28862 Sep  6 18:27 pg289_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91779 Sep  6 18:26 pg289.png
-rw-rw-r-- 1 sfmqrb sfmqrb   187988 Sep  6 18:19 pg290hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98901 Sep  6 18:18 pg290.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105586 Sep  6 18:11 pg291hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70592 Sep  6 18:10 pg291.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103438 Sep  6 18:12 pg292.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36312 Sep  6 18:20 pg294_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb   125960 Sep  6 18:28 pg295hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77133 Sep  6 18:28 pg295.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66500 Sep  6 18:33 pg297.png
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1548.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1549.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1550.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     3698 Sep  6 18:19 zar_line.png
```


### [2026-09-06T22:33:12.969Z] TOOL RESULT

```
=== BRT kō ===
=== BRT kuθra ===
=== BRT katāra ===
4218:Sprechenden  nahe  liegt,  adjektivisch,  auch sva,  'dieser  mein,  unser':  °na  bansmana imqm  zao^ram  äyese  yaH'^.2.1;  —  vlspa tarsuca  xhiärata  *vanaiti(?)  °na  masanaca i'atihanaca  .  .  ".  .  "durch  diese  (meine) Grösse  und  .,"  P,42";  —  \iimä  dakyai«^ tyil  adam  adarsty  kada  (sd.)  °«J  pärsä iärJ  D.j.z.  n)  in  schwachdeikti- schem  Sinn  'dieser,  der,  er';  l)  auf  Vor- hergenanntes, -gesagtes  (Wort  oder  Satz) zurückweisend;  i)  auf  ein  Wort,  a)  ad- jektivisch: iwt  hafat  vir^rmt  .  .  aal  °na v>r3>!ra  hacimnS  . .  YL  ig.  54;  54;  — parttum  ayasalsa  .  .  °na  parma  tanüm aizuiji/gisYl.i4.^$;  35,  /7.61';  —  mana zaya  asti  vahistjm{%A.)  ,.*na'  vaca  vanSni ..  'na  saya'V.if).<).  b)  substantivisch: yat  .  .  aoxte  alsa  .  .  kacanuha  ml  *''na^^ apirmäyüka  .  .  a%a  *hä  *xsayäe  *°na*'' Aaxisit  (sd.)  ciiva/  *'na^'>  .  .  faraakacaiti (sd.)  ". .  'geh  mit  ihm,  mein  Kind!' . ." N.;?;  —  aitatca..  uxnanam  luchs-isnum.. astica  -na  avavat  uxoala  (sd.) . .  Y.  ig,  10;
5986:kada  mazda  yöi  uxsand  "snam  . .  /rärmtg
10730:ntanauhl  '%r3J  hcUü  paitt.mraot  asä  kuL- haxa  Y.32.  2;  —  mazdä  , .  vokü  uxfya (sd.)  manavAä  °hr3  aiälä  ustä  tanüm Y._jj.  10;  —  yahmi  spfntJ  %wä  mainyU urvafse  jass  mafsds  "ärä  ahmt{s,A.)  voha mananha  Y.43.6;  —  aAmäicä  «ärJ  (als Sah].)  ^^ /asaj  (sA.)  mananha  voha  asaüä Y.3Q.  7;  —  ahmsi  dqn  (sd.)  .  .  mazdä •^rJ  armaitf  ahurS  Y.  47.  i;  —  kj  binx- 'iqm  täil  ''hrJ  mal  ärmaitim  ^..44.1;  — kada  masda  ala  mal  ärmai/i/ /imaj  (sd.) •^ra  Y.48.11;  — yqm  Asi  °'^ra  voAuäi cdiit  (sA)  tnananhi  Y.^o.y,  —  mazdi dadät . .  haurvat3  aminlätasca  . .  asahyica ..  •UraAyä  sarS  (sd.)  Y.^jj.ai.  a)  im YHapt,  mit  va^hav-K^y.as>m..vahist>m ..vohuia  maiid ..  vokucä  '"hrsm  \.3~.i,i.\ —  asäatcä  hacä  varahsuseä  mananhs  vatf- ksusca  'hrai  Y. J5. 10.  a)  im  jAw.,  mit va i rya- Adj. :  '^rtm  vairTm  amihm  sptn- hm  yazamaide  S. 2.  4 ;  Vr.  20.  i;  —  ahurS mazdä  . .  vohu  manö . .  ahm  vahist»m  .  . ''i:r>m  VairTm  .  ,  spmta  ärmaitis  .  .  Y. 57.  24;  1.1  f.,  /tf.  3,  Yt/.  25,  4.  i;  —  ahu- rake  maxdä  .  .  vanh^us  mananhB aiahe ..'"hrahe  vairyeke..  Y.70.2;  —  aku- rai  masdäi  . .  aläi  . .  °^rai  vairyät  armatSe V,  iff.  iii  G.J.  s;  —  vaAu  manauha  haH- mnS  aläca  .  .  '^r3ca  ya  vairya  FrW.  /, I ;  —  viscihnm  dim  ayasata  Syapta  (sd.) ■ira  vairyaY.2Q-^(J\  k)  xlaiirahe  vair- yeht  a)  (nämlich  mS)  heisst  der  6.  Monat im  Jahr:  pancaca  haptaitttn  *pailisJiahyehe (sd.)  '"hrahe  vairyehe  anayranqm  A.  3. 9.  ß>    (nämlich    ayani)    heisst    der  4.
11261:'Ableit.  aus  '!aia-  m.  -Lehre",  ium  V.  kai-, vgl,  iBild.  mq%ran-.  —  Pü.:  eäiilärtum,  Sü.r prajhäpakatamah.  —  >)  Them.
18675:elliptisch  sva,  'ein  Mann  und  ein  Weib,  ein Menschenpaar"**:  dvaübya  haca  n)r>bya dva  nara  us^ayein/e (sd.)  t//i^wa/ia  s/ri^a nairyas^a  V.2.41.  2) '•  praegn. 'wehr- hafter Mann,  Kriegsmann;  kriegerischer Held':  narSi  ßrasaoifträi  Y.  28.  8;  — katna  (sd.)  syävarsänai  zurSjatahe  na- rahe''*  Yt*j.  18;  — pqsnus  narJ  (NS.)'^ HryS  taxmS  Aog.  84;  — y^i  narS  taxma ptntmU  Yt./J  27;  —  t! nard paiti.sanmti ySkva  v3r3%ra.l'aohl!  {sd.)  YtJ_j.  46;  — yat  mS  slärS  .  .  AacÜnte  (sd.)  n?r>byS ä^annff  *bax/3nia  Yt- 8.  1 ;  5.11,  77.6,7; das/a  narqm  *pouru.tät?m  stäkyanqm.. vanatqm  avammnanqm  Ny. J.  10;  —  hva- iai  naire  barumnäi  Y.  65.  4;  — yä  na- qm  vjg3r>pla{sd.yit . .  baoxtär^m  dahäi/i Vr.7,3;  Yt  10.12;  —  ya^a  hazannm Oim  narftn  adar.taySi^  Yt.  8.  $$; I.  19*;  —  a%ra  narqtn  mihrS.drujqtn apq/{sd.)  gavB  dar>tayeiti  Yt70. 48;  — narqm  asätanqm  frasS.car^'hrqm  saosyan- tqm  Y.  24.  5,  Yt.  13. 17.  a)  als  Bezeich- nung für  den  zweiten  Stand  (s.  'piflra-) 'Krieger,  Ritter***:  kada  .  .  mquarfi/ (sd.) rS  vis3nliY.48.  10;  — daidx atturai (AP.)  ,  .  asaunS  .  .  aidyüi  väsliyJng  ,  . ahmaibyä  ahma.rafonarahs  {^d^  Y.40.3; %wqm  ttarakl  ysi  taxma  Jathyintt äsu.aspim  .  .  %wqm  a^ravanS  .  .  mastim Yt5.  86.  3)''  ohne  Betonung  des  Ge- schlechts sva.  Mensch;  Person';  1)  im Gegensatz  zum  Tier;  uzw.  zu  a)  pasav-: ahe  nmanaßie pasvqmca  narqntla  Y.^-S; pasBm  .  .  nanm  ra?syät  V,  13.  32 b)  'span-.  . .  ahe  nmanake  spä  vä na  va  irihyat  V.5, 39;  8. 1,  4;  —  yat ahmi  spänasca  narasca  para.irüinti  V. 6.1; — y!i  pa^a  uebarmte  (^)  spänasca irista  iiarawca  (NF.)"  irisia  V.  Ä  14; 3.  32;  —  yat  ,  .  sairi  riiianie  spänasca irista  naraila  (AP.)'*  irista  V.  3.  8; 36.  c)   ^av-:  janyäi  *n>rSuI^'*  para
19586:Haomai  vTipe  zi  anyg  *°SawAj  aaftwa fiaSnte  .  .  äat  hs  ys  kaomahe  '%6  aiä AacaiU . .  rmjaiü  (sd.)  hasmake  °%3  "denn alle  andern  Rauschtrinke  sind  von  . .  A. begleitet,  aber  er,  der  Rauschtrank  des H.  . ."  Y.  10.  8;  Yt  17.5'.  b)  sonst: dahms  hurqm  (sd.)  ifaraiti  'S?  ^asfya.- paya/ahü  N.  jo;  —  kada  ajSn  mB%r>m ahya  *°äahyä''>  yä  . .  "wann  wirst  du  den Unflat  dieses  Rauschtranks  treffen,  mit dem.."  Y-^i".!©!).  [N.jo:  lies  mi^Ue statt  mähB  ^araiti;  s.  Pü.]
20478:•  g.  m^iaray- 1  'Verkündigung,  Botschaft" des  Propheten:  kada  tnazda  "röÜ  narS vjs^ntl  "wann,  o  M.,  werden  die  Ritter die  Botschaft  verstehen  lernen?"  M.48. 10.
20847:I  et  (eum)  qui  (est)  faciendi  et  dicendi" I  Y.  33. 14;  —  *grSkms . .  atikSus  maraxtärB I  (sd.)  ahya  \yai(a  ^'Grlhmas  . .  et  (ii)  qui (sunt) ..  destructores"  Y.J2. 13; —  ku%ra töi  andrS  (sd.)  .  .  yöi  .  ,  caxrays  "num tibi  (sunt)  fidi  (ü)  qui  . ,"  Y.^4.7;  — kada  .  .  yOi  uxiäiiS  ainqm  .  .  frärmtl "quando  . .  (ii)  qui  (sunt)  tauri  .  ."  Y.  4G. 3;  —  naldä  dahySus  \ydi  iastSrS  drjsvatas "neque  (ii)  qui  (sunt)  . .  imperatores"  Y. 4O.  I ;  —  tat  ..  uitanai  data  . .  ySi  sl gSus  v^nzinl  (sd.)  azyi  ".  .  vitae  (eorum) qui  .  ."  Y.  34.  14;  —  tim  at  yasna- nqm  paurvataia  yazamaidl  ySi  ..  iyeintJ ".  .  imprecationum  .  .  (eorum)  qui  .  ." ^•37-  2;  —  yi  varpsaiil  (sd.)  kyat vasnä  firasöJ^mim  "qui  . .  fecerit  . .  (id) quod  (est)  .  ."  "^.46.  19;  —  hyatcS dar>gSm  dr)gvll.d»byS  rasB  savai'a  alavabyö "et  (id)  quod  (est)  . .  damnum  et  lucra  . ." Y._jo.  11;  —  Aaihyavanitqm  {%A.)  hyat vasna  f?rasS.t}m}m  "verificationem  (eius) quod.."  Y. 50.11;  —  ai  zt  töi  vaxsya .. hyai  aksyä  (NSf.;  sd.)  dngvaiii  wörtlich ",.  von  dem,  was  die  Androhung  ist,,"  Y, 51.  8;  —  hyat  "qsasutä  (sd.)  yä  (NPn.) daiiiiana  (sd.)  fraoxta  "..  (ea)  quae  (sunt) . .  enuntiata"  Y.  48.  1 ;  —  das  Relativ  kon- gruirt  mit  dem  Praedikat:  vldvä  yalclt güzra  (sd.)  singhanhS  (wörtlich)  "kennend auch  (das),  was  die  geheimen  Lehren  (sind)" Y.4<V,3;  —  anais  a  vT.nSnasa  ya  (NSt) iarapsjis{ad.}cä  kjvltäscä  Y._J2.  15;  — *m>ndäiäyai  (sd.)  ya  (NSf)  toi  adisHi Y.44.8;  5,^.13;  —  nipatihw . .  tumas^a ya  armaitiH&d.)  Tiilcä  Y.4g.  10;  —  yS va  mSi  \yh  (NPf)  gasha  dasdi  (Sp. 7 1 S  u.)  *asnatihe  wörtlich  ". .  (das),  was meine  Besitztümer  (sind)  .  ."  Y,  46. 8;  — vtayUta  yä  (NPn.)  mrqi  sädra  drtgvats (wörtlich)  "immer  (wird  sein)  was  die Qualen  (sind)  .  ."   Y.45.  7;  43-5,  49-6;
22631:•  j.  vanar-  n.  —  ?  — :  'nar»  F.  8. Pu.:  nddakada.
22890:—  unsinnlich:  kada  .  .  frannil  V)rsz- ääis  s^nghlil  saosyantam  xratavB  (sd.) Y.4tf.3.
25851:684  m.)  patöis  sp)ntä  damä  urva'ho  .  .  Retter  um'  i^.,  d,  i.  Ästval.trita-  (sd.),  der Y.  45-11.  a)  Plur,,  von  denen,  die  auch 'der  sieghafte' (wr-p��r^f««-)  genannt bei  Zara%uitrai  Rettungswerk  zu  helfen  wird:  Aaia  gayäi  manknat  J  •yantai^'' bereit  sind:  kada..ySi  uxsanS{%A)  asnqtii  \vtr)%ra-jnai  "^.26. 10;    —    'yanhm
```


## [2026-09-06T22:33:21.677Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && head -3 aiw.txt; echo ===; grep -n \"kuθra\\|kudra\\|katāra\\|katama\" aiw.txt | head -20; echo \"=== kent ===\"; head -3 kent_full.txt; grep -n \"kašciy\\|ka\\Wciy\\|cišciy\\|aivačiy\\|ciy\" kent_full.txt | head -20"
}
```


### [2026-09-06T22:33:21.736Z] TOOL RESULT

```
Exit code 1
Google 


(eval):1: == not found
```


## [2026-09-06T22:33:24.263Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && echo \"--- aiw katara\"; grep -n \"katāra\\|katama\\|kuθra\" aiw.txt | head -10; echo \"--- kent head\"; head -3 kent_full.txt"
}
```


### [2026-09-06T22:33:24.321Z] TOOL RESULT

```
--- aiw katara
45912:prajhäpakatamah.  —  >)  Them. 
--- kent head
Google
```


## [2026-09-06T22:33:28.159Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && for w in \"aivaciy\" \"cis-ciy\" \"kas-ciy\" \"adakaiy\" \"kaiy\" \"ciy\" \"kam-\" ; do echo \"### $w\"; grep -n -- \"$w\" kent_full.txt | head -6; done"
}
```


### [2026-09-06T22:33:29.972Z] TOOL RESULT

```
### aivaciy
### cis-ciy
### kas-ciy
### adakaiy
17123:11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 
17136:24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 
18186:81 :adakaiy : avada: Ghat : yàtà : adam : Gaumãtam : tyam : magum : ayãjanam :. 
18187:82 hya : Bardiya : agaubatà;: adakaiy : imaiy : martiya : hamataxáatà : anudiyd : man 
23253:adakaiy adv. ‘then’: OP ada- + -kazy, Gk. 
### kaiy
7293:ada-kaiy; diirada-Sa. 
10361:-kaiy, сий, cina], ciytikara- in the Lexicon. 
17123:11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 
17136:24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 
18186:81 :adakaiy : avada: Ghat : yàtà : adam : Gaumãtam : tyam : magum : ayãjanam :. 
18187:82 hya : Bardiya : agaubatà;: adakaiy : imaiy : martiya : hamataxáatà : anudiyd : man 
### ciy
1882:masc. kašciy, nt. cifciy, avaSciy, aniyasciy, with 
3101:gaibām-cã; zXagam-Sim, paruvam-ciy, adam-&im. 
3151:ciydkaramcamary. 
3605:ciydkarammeciy® DNb 51, 511, for -cmeüp, = 
3606:ciyükaram-ca-mauy. 
3827:ciyakaram DNb 50, 51, 514, but ciyăkaram DNa 1 
### kam-
3013:kam-bar-ma, or -barw- on the added evidence 
3143:= niydkam-maiy (852.1). An error in cutting 
5898:the root kam- (if this etymology be correct) 
6144:kama = |kam-ma, see $130. On pIE m, see $67; ^ 
6184:kam-bu-2t~{a. 
7129:maniíaiy = taumanis-Saiy, I'yü)kama = -kam-
```


## [2026-09-06T22:33:35.140Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && sed -n '1875,1895p' kent_full.txt; echo \"=== lexicon ka ===\"; grep -n \"^ka-\\|^ka \\|ka rel\\|indef. pron\" kent_full.txt | sed -n '1,30p'"
}
```


### [2026-09-06T22:33:35.202Z] TOOL RESULT

```
V. Names of cultural materials: 

asan- ‘stone’, with s from Ё. 

[азайа ‘semi-precious stone’, with s from Ё. 
VI. Miscellaneous: 

masc. kašciy, nt. cifciy, avaSciy, aniyasciy, with 
Sc from -s q*- and -d g*- respectively, in sandhi; 
no specific reason сап be assigned for the 
borrowing by OP of this type. 

Pürsa ‘Persia’, with s from Ё, cf. Paréava with 
0; the name seems to have been imposed by 
an outside source. 

patiyazbayam ‘I proclaimed’, with Med. -zb-, but 
h*zdnam (acc.) ‘tongue’ with OP -z-, both from 
ТЕ ди; see also $91. 

vasiy ‘at. will, greatly’, with s from Ё; but see 
=== lexicon ka ===
7865:ka-, probably with vriddhi; kapauta-ka-; kdsa-ka-; 
7930:ka-, vàhara- in 8üra-vahara-, ратіата-, see $154.I. 
18234:ka-; the suggestion has been made that the clauses have 
23224:ka-iš-ši-na, Akk. a-Si-na. Either borrowed from 
24838:ka- interrog.-indef. pron. ‘who’: Av. Skt. ka-, 
25676:ci- interrog.-indef. pron. ‘what, any’; col-
```


## [2026-09-06T22:33:37.852Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && sed -n '24835,24850p' kent_full.txt; echo ...; sed -n '25670,25695p' kent_full.txt; echo \"=== adakaiy ===\"; sed -n '23250,23258p' kent_full.txt"
}
```


### [2026-09-06T22:33:37.926Z] TOOL RESULT

```
DB 2.76, 91; 3.52, 92. 


ka- interrog.-indef. pron. ‘who’: Av. Skt. ka-, 
Gk. то-, Lt. quo-, NEng. wha-t, pIE *q*o- ($201). 
See also Ка, -katy, ci- (§132.2). With encl. -ciy, 
‘any’: kaš-ciy (89. VI, $09, $105) nsm. DB 1.49, 
53; DSe 37. 


kā, generalizing particle after 2d pers. pron.: 
probably isn. of ka- ($191.11; Kern ap. Caland, 
1. Syntax der Pron. im Av. 47; Kieckers, Etymol. 
Miszellen 1934.135; otherwise Gray, JAOS 23.60). 
DB 4.37, 41, 67°, 70, 87°; DSt 10°; XPh 46. 

...
Wackernagel, KZ 61.205-8. саат asn. DB 2.75, 
89 (Cameron found ст“ legible in 89, but only 
the final me in 75); caSa{m} (case and form uncer- 
tain) DSq 2. 


ci- interrog.-indef. pron. ‘what, any’; col- 
lateral stem (8201) to OP ka-. See also -ciy, cid, 
cind, cijükara-.  ciš-ciy asn. ‘anything’ (§9.VI, 
$105, 5132.2, §201) DB 1.58, Lt. quicquid, pIE 
*q*id-q*id: reduplicated form with Med. sandhi; 
see OP -ciy for exact cognates. 


-ciy encl. particle, emphasizing or generaliz- 
ing, nsn. or asn. of с1-: Ау, -Git, Skt. eid, СК. т, 
Tat. quid, pIE *q*id (840, §84, $113, 5191.11, §201, 
6998.11). In the following combinations: aciy 
(q.v.) ХРЇ 21. aniyaš-ciy nsn. DB 4.46; XPa 13; 
aniya&-c (452.1) XPh 41f; aniyai-ciy npm. XPf 
29. avas-ccy nsn. DNb 55; asn. DNb 53f, 57; 
XPa 20; XPc 14; XPf 48, alva}m-c* ($521) DB 
5.9. Ка&-сїу nsm. DB 149, 53; DSe 37. @& 
ciy asn. DB 1.58. paruvam-ciy DB 1.63, 67, 69. 
yaciy (q.v.) DNb 35, 36, 57. haw-cty DPe 
23f. hakaram-ciy DNb 34f. [haca-cily DSf 23: 
=== adakaiy ===
see also adakaty. — ada-taiy DNa 48, 45. 


adakaiy adv. ‘then’: OP ada- + -kazy, Gk. 
aly. то ‘somewhere’, pIE *q¥ei, Isn. to int.-indef. 
stem ($135). DB 2.11, 24; 4.81, 82; DNb 38. 


adam pron. “Р: Av. azam, Skt. adm, plE .
```


## [2026-09-06T22:34:09.155Z] TOOL CALL #25: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg297.png"
}
```


### [2026-09-06T22:34:09.498Z] TOOL RESULT

```

```


## [2026-09-06T22:34:09.496Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T22:34:17.467Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 217 (printed 196) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==218' HRN.txt | head -60"
}
```


### [2026-09-06T22:34:21.246Z] TOOL RESULT

```
=== HRN leaf 217 (printed 196) ===
— 196 -
'wer?' siyn. käi^ sar. ka *was für ein?' wa;^. kü, ki, sar.
ko *dass .
Np. ki setzt ein ap. ^kaya- voraus, vergl. ai. kaya-,
877. (2)kih ^klein; kihm (Sahn. I, 70 Vers 171).
g. kasük, kastar (Comp.); Käs. V. kessär, kesserUr,
K. Z. ias.
aw. kasyäo ^kleiner ; phlv. kih(i)st, kas,
2&y, kasr 'kleiner, jünger ; oss. Msfär (156) jünger,
jüngst'; bei. kasän, kassän 'klein, gering, wenig' (439;
Dames: kisän, kisäin, kisänak).
Zu np. kih vergl. unter bih (No. 241); phlv. kas,
g. kasük etc. stammen vom Positiv aw. kasu- 'klein,
gering.
878. {\)kei 'wann? wie?', jüd.-pers. '»>!!.
aw. kada *wann'; ai. kadd *wann?\
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
Rache (201).
*) f hat keinen etymologischen Wert wie in mehreren anderen
Wörtern, vergl. Indog. Forsch. I, 489.
```


## [2026-09-06T22:34:27.548Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==217' HRN.txt | tail -40"
}
```


## [2026-09-06T22:34:29.135Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"kudäm\" \"kugä\" \"kuǧä\" \"kudam\" \"hie\" \"hie 'nichts\" \"cand\" \"cīz\" \"ciz \" \"cün\" \"cih\"; do echo \"### $w\"; grep -n -- \"$w\" HRN.txt | head -4; done"
}
```


### [2026-09-06T22:34:29.308Z] TOOL RESULT

```
- 195 —
Note 32) wahrscheinlicher ist als die de Lagarde's
(Ges. Abh., 55), so nehme ich eine aw. Nebenform
"^kawza- an (vergl. unter np. ;ifMsprrfew, No. 483)^).
873. höliden graben, aufreissen.
kurd. Icölän ^aushöhlen, ausgraben'; wa/. parjkölam
*eine Grube, einen Brunnen graben .
Justi, Kurd. Gramm. S. 205 No. 88 vergleicht
deutsch 'hohl\ das gewöhnlich zu got. hulundi *Höhle\
lat. occulö etc. gestellt wird.
874. kün 'Hinterer.
phlv. kün, kün\marz.
kurd. LW. hm, qlng neben qin, km (H.-Sch.);
bei. LW. kün, n. IHn (208).
Geiger vergleicht ai. l^knü- einen bestimmten Ton
von sich geben*, aber diese Wurzel kommt nur im
Dhätup. vor.
875. höh *Berg', köhe 'Höcker.
Käs. Q. küfün *Höcker ; kauk.-bergjüd. knf,
ap. kaufa- 'Berg* ; aw. kaofa- 'Berg, Höcker; phlv.
köf, köfak *Berg, Höcker'.
AUg. entlehnt; echt bei. köpak, n. ßöfay (211)
'Schulter*, kurd. kuwi 'wild*.
876. {\)ki{h) wer, welcher? dass etc.'; /.^ (ältere Schreibung,
z. B. AM.; äähn. I, 39 Vers 81)-), sowie in käskl,
kaßi (Öähn. I, 95 Vers 609).
Käs. ke, kl, ko, kö.
ap. aw. ka- wer?'; päz. ka (Conjunction), ke (Pro-
nomen) , ku (Partikel) , doch werden diese drei Aus-
sprachen häufig verwechselt; ai. kd-,
kurd. LW. ki(h); oss. d. f^a wer, welcher, dass' (149);
bei. ke, kai, n. Mai 'wer?' (200); wa/. küi, kör, sar. <J(5/
*) Skr. kiihjä', dessen Bedeutung 'buckelig, krumm* schon nicht
zu 'Topf* passt, vermag ich auch lautlich nicht mit dem Awostaworto
zu vereinigen. Bei Osthoff, Perfectum S. 33 vermisst man aw. nhjyeife.
•) Repristinirt auf Inschriften in Indien, Hörn, Epigraphia in-
dica, Vol. II. Abu Mansür Muvaffaq schreibt das Pronomen wie auch
die Conjunction öfter mit Kesre, z. 11. S. CA Zeile 1 v. u., S. 70 Zoilo 13,
S. 75 Zeile 7.
13*
```


### [2026-09-06T22:34:31.053Z] TOOL RESULT

```
### kudäm
7343:843. hvjci *\vo?;* welcher^); kudäm^) Vas für ein?;
12727:, kudäm 843.
### kugä
### kuǧä
### kudam
### hie
35:von Land zu Land unterschiedlich sein. Öffentlich zugängliche Bücher sind unser Tor zur Vergangenheit und stellen ein geschichtliches, kulturelles
56:von Land zu Land verschieden. Wir können keine Beratung leisten, ob eine bestimmte Nutzung eines bestimmten Buches gesetzlich zulässig
83:schien und worüber andere anderer Meinung sind. Eine
85:sie zu protestiren, was öfter notwendig schien, wenn sich
### hie 'nichts
### cand
1606:ap. ai'ta- 'dieser'; aw. ae-m-, ae4ad; phlv. e, ecand
4117:aw. cvant' 'wie viel?'; phlv. cand.
10290:54. candTnltan 'erregen (AV.).
10291:bei. candng bewegen, schütteln' (54).
### cīz
### ciz 
### cün
2961:röz^ beperrär^ büd^ färbe ez an sude cünin
4140:450. cun Vie?\ cü, cünän {'^)i^^^)t, Is. 10, 11), cünln^), cünkL
4160:') Cu ist metrisQh nur kurz, die Länge dazu ist cün (Rüokert,
9334:standen, rergl. cün etc. s. v. yün (No. 946).
### cih
1256:Minöcihrl.
1926:*) FJ hat einen Vers Minöcihrl's als Beleg.
4167:aw. öa^warö Vier*; phlv. cahär, päz. cihär; ai.
4172:453. rlhr, cihre 'Ursprung; Angesicht'.
```


## [2026-09-06T22:34:38.321Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### 843\"; sed -n '7340,7370p' HRN.txt; echo \"### 450 cun\"; sed -n '4140,4166p' HRN.txt; echo \"### cand\"; sed -n '4110,4125p' HRN.txt"
}
```


### [2026-09-06T22:34:38.387Z] TOOL RESULT

```
### 843
FirdüsT kebüd auf düd (I, S. 5 Vers 77), numüd (I,
94 Vers 608), biid (L 115 Vers 937). Auch der PärasT-
prakäga hat w, kavütara (Weber, No. 285).
843. hvjci *\vo?;* welcher^); kudäm^) Vas für ein?;
jemand; hü 'wo?' (unbelegt).
aw. kü *wo?* -h np. Ja (No. 417), vergl. kva-, kuda
*wü?*, kudra 'wohin etc.; phlv. k(u)täm'^) (päz. kadäm)^
päz. kii *wo?', kiijä; ai. kä *wo?', küha *wo*? etc.
vergl. kurd. ku 'wer, was, wo?'; af/. vergl. küm
'was?'; oss. ku 'als, wenn, da, weil, wie (163); bei.
käy n. kü 'wo?' (144); minj. ko,
844. kedy kede^) 'Haus*, vergl. ked/udd {ket/iidä^)); iltes-
kede, meikede.
aw. kata- 'Graben (vd. 2, 26); Grabstätte'; phlv.
katak 'Grabstätte; Haus', katak\xutü^ katak\banüklh
(AV.), vergl. auch katik 'häuslich, zum Hause gehörig
{ätas).
wa/. ket, sar. c6d^ si/n. cid,
845. ker^ kerr 'taub'.
aw. karenäos[ca (yt. 5, 93) 'taub', Spiegel, ZDMG.
32, 721; 'd\. karnd- 'mit verstümmelten (gestutzten)
Ohren' (Geldner, Vedische Studien I, 138).
kurd. LW. ker 'taub'; af/. künr; oss. kurmafä 'die
Tauben' (Matth. 11, 5, Hübschmann, No. 164); bei.
*) Sogar Mass*, z. B. Vis und Rämln 67, Vers 2.
^) Das u ist jung, vergl. ai. katamä-^ mäz. kadänu
*j Das II kann auch erst neupersisch sein , vergl. phlv. katär^
aw. kafära-,
*) Käs. V. Ä-e, Q. kiyd^ kl etc. (s. v. ;^äMe) haben das bereits
neupersische d noch in y verwandelt. Solche zweite Lautverschiebung
findet sich auch sonst. Ein Beispiel für viele: Käs. tnelä, mele 'Büffel-
### 450 cun
450. cun Vie?\ cü, cünän {'^)i^^^)t, Is. 10, 11), cünln^), cünkL
phlv. digün *wie?* {ci + aw. gaona-), cigämh, vergl.
np. cigüne (vergl. zeryün aus aw. zairLgaona-, No.661).
451. ci(h), ci (AM.) was?, wie?\ cirä warum?*.
ap. üyakaram, -ciy (enclit.); aw. eis, cit; päz. ci/i
(phlv. no); ai. -6it (enclit.).
af}'. ca 'was?; einige*; oss. d. ci, ci, t. ci 'was, was
für ein, welch?' (322).
Als Encliticon hat Salemann, Mel.asiat.IX,241 altes
ap. ciy, aw. cit in den dialektischen tnvn ji auch ich*
(Lokalität Sih dih bei Isfahän), memc *ich auch*, öle
'er auch' (Güräni), sowie in mehreren gebräuchlichen
neupersischen Worten erkannt {kes, heö, hergiz^ mz^
egerci, herci temämter), die sämmtlich an ihrem Orte
aufgeführt sind. Im PehlevT wird das Encliticon noch
») Im Journal Bomb. Br. R. As. Sog. 1891, Vol. XVIII, 39 ff. hat
Jivanji Jamshedji Modi kürzlich die Stellen gesammelt, an denen
bei Firdüsl vom Ballspiel die Rede ist (The Game of Ball-Bai -- Chowgän-
gui — among the ancient Persians, as described in the Epic of Fir-
dousij.
') Cu ist metrisQh nur kurz, die Länge dazu ist cün (Rüokert,
ZDMO. 10, 133). Cünän z. B. äähn. I, 148 Vera 354, cümn 157 Vers 523.— 101 —
in weit ausgedehnterem Grade verwendet. Vergl. -J
(Nu. 53) unter 'Verlorenes Sprachgut*.
452. 6ehüv 'vier , ceharmn, cär^ darum (AM. neben öehärum),
cärlpäi, car[sa (syr. LW. ''1D1NTO*', arab. LW. cahdrsOg),
cdr[deh (Sahn. I, 211 Vers 1479) etc.
### cand
Zu np. cep 'links' (No. 435), gr. yAfiiJxct) 'biege',
adfinvXog (Nöldeke, mündliche Mitteilung).
Fick setzt als Wurzel für ai. capa- und gr. ad^iTiTO)
qep' an. Zu derselben Wurzel wird übrigens auch np.
xem, x^mm {*xeinp) — verschrieben in cem, Vullers s. v.
No. 12 — 'krumm, gebogen, yemtden etc. gehören.
447. eend 'einige*; wie viel?*, cendän, dendm, cendi,
aw. cvant' 'wie viel?'; phlv. cand.
kurd. LW. dend , dm; bei. cunt 'wie viel?' (64);
af;'. cof»[ira, com\ra wie viel?*; wa/. vum^ ciin, sar.
cund.
448. cöh 'Holz*.
phlv. 6öp 'Holz' (Guj. Ab.); kurd. cö, siw (H.-Sch.);
bei. LW. vöp (66); wa/. ^öpk, sar. /Jih,
7*--- 100 -^
Lässt sich lautlich nicht mit skr. kSupa- 'Staude,
```


## [2026-09-06T22:34:58.043Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in \"'Ding'\" \"kes 'Person\" \"heö\" \"hic 'nichts\" \"'jemand'\"; do echo \"### $p\"; grep -n -- \"$p\" HRN.txt | head -6; done; echo \"### index ciz/kes/hic\"; grep -n \"cJz\\|ciz\\|kes 4\\|heö 4\\|hec\" HRN.txt | head -20"
}
```


### [2026-09-06T22:34:59.838Z] TOOL RESULT

```
### 'Ding'
### kes 'Person
### heö
4152:neupersischen Worten erkannt {kes, heö, hergiz^ mz^
### hic 'nichts
### 'jemand'
7418:851. kes 'jemand', kesT {*kese), kesän,
### index ciz/kes/hic
1620:139. ec jemand, etwas', s. hec (No. 1114).
2939:aw. pairi (oder para) — V^vciz-, 'herum- bezw. weg-
3341:355. pes *Aussatz', pest leprös', pesl, pese Schecke*.
9566:(wie ec neben hec stehej, eine Bemerkung, die VuUers gleich vielem
9616:phlv. ec bezw. hec (päz. hec, hSöi),
```


## [2026-09-06T22:35:03.201Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### 851 kes\"; sed -n '7418,7440p' HRN.txt; echo \"### 1114 hec\"; sed -n '9600,9640p' HRN.txt; echo \"### ciz entry\"; grep -n \"^ *4[0-9][0-9]\\. c\\|ciz\\b\\|cJz\\|ciz'\" HRN.txt | head -20"
}
```


### [2026-09-06T22:35:03.290Z] TOOL RESULT

```
### 851 kes
851. kes 'jemand', kesT {*kese), kesän,
ap. kas[cit/ 'irgend wer, jemand'; aw. kas[cit jemand',
ka$[7iä ; päz. fcas, kasi[ca ; ai. vergl. käs.
LW. kurd. kes^ kesek; af/. bei. (129) kas, n. /ras.
Salemann, Mel. asiat. IX, 241.
852. kt(8 'weibliche Scliaam'.
skr. kuksi- 'weiblicher Leib' (ai. allgemein 'Bauch,
Unterleib').
LW. kurd. quz {^t*), H.-Sch.; bei. kus (206, wo auch
die Etymologie); af/. kus.
skr. kuksi' bedeutet auch 'Degenscheide', vergl. PW.
s. V. kuksi' und ähnlich WZKM. IV, 142: 'Der Penis
ist wie ein Schlüssel (lies kilid statt kältd) für den
Hals des Uterus und dieser wie eine Degenscheide für
den Penis'.
Dazu lit. kuszys 'weibliche Schaam'; über gr. ytvaog^
lat. cunnus vergl. die Literatur bei Johansson, Indog.
Forsch. II, 19 Anm. 1, der zwei ganz verschiedene
ai. kogu' und kosa- annimmt (in der Bedeutung 'Uterus'
hat Sngruta übrigens immer kosa-)^ womit Bartho-
lomae's Einsprache gegen die Zusammenstellung von
kösa- mit kuksi- Rechnung getragen wird (ib. I, 491 2).
853. kcs 'Achselhöhle' i).
### 1114 hec
Citat, dai>- Vullers übrigens gewiss nicht mala fide unterlassen hat,
deutlich zu erkennen. Die Lesung uner verbietet wohl die Etymologie.
M Vergl. Jacobi, KZ. 31, 315.
*) Sämmtliche Belege stammen von Herrn Prof. Nöldeke.
^) Ausführliche Angabe der Literatur pro und contra neuerdings
bei Johansson, BB. 18, 25.
*) Stellen aus dem Öähnärae bei Spiegel, Glossar, 368.- 249 —
4ll3. höm 'Haomastrauch, -pflanze*; vergl. hfun (d-majüH
. -^wo^ *Magierhaoma (eine nicht näher zu bestimmende
^^|j^' Pflanze, AM. 268).
'' aw. haowa-; phlv. hötn; ai. soma-.
bei. vergl. hörn (LW., 99).
V1114. Äe^ jemand, jemals*, mit Negation 'niemand, nichts;
ec (äähn. I, S. 4 Vers 59).
W^ Käs. K. Z. ec,
ap. *(tiva ~r ciy (Salemann, Mel. asiat. IX, 241);
phlv. ec bezw. hec (päz. hec, hSöi),
1115. herhud *Feuerpriester , herkede, hermend, {her *Feuer',
das man daraus erschlossen hat, ist aber bedenklich^).
aw. aeAlrapaiti' ; phlv. ehrpat (Inschriften), lierput,
herpatastän, herputlh bezw. erpat,
1116. lilrek, {^hereh?) 'Bockchen, Zickchen'.
ap. *yö*V7/ra- 'Jährling (Tomas chek, Centralasiat.
Studien II, 766).
si/n. yirk 'ausgewachsenes , männliches Schaaf,
Zuchtwidder.
Wenn die Etymologie richtig ist, so hätten wir
in diesem Worte die einzige neupersische Spur des
aw. yär-, ap. -yära-.
' 1117. hezutn (Is. 30, 88), hezem 'Brennholz*; Mme-).
^c^^ S- i^^i(^\ Käs. Q. K. hezem, ezem,
^ aw. a^sma^^') 'Brennholz'; phlv. esw (nur um-
schreibend), hEzam bezw. ezam (päz. hezam) ; ai. idlimd-.
kurd. ezink (H.-Sch.); minj. czma.
*) FJ hat zwar einen Vers von Emir Muizzi; im Awesta und
Pehlevl kommen ae^ra- oder ehr *Feuer* auch nicht vor.
*j Nicht gehört hierher syr XOPDi tal«»- NDVNi Nnom? Low,
Aramäische Pflanzennamen, 8. 146.
^) Das is in aesma- beruht auf einer 'Verschleppung*, wie in gr.
TTHOfiu., o(i/ur^ etc. (Joh. Schmidt, KZ. 27, 814, Bartholomae, Ar.
Forschungen II, 86).— 250 —
### ciz entry
2939:aw. pairi (oder para) — V^vciz-, 'herum- bezw. weg-
4036:436. cerh 'fett*, cerht (auch 'Milde, Sanftheit*), cerbis (AM.
4042:437. cert 'Rad*.
4052:438. cer^n Teil, Haut\
4057:439. cerTdeti, weiden', cerend, cerägah {^^irrrd, Is. 30, 23),
4069:440. cesm 'Auge 2).
4075:441. cespEden, cepsiden, cefslden (Inchoat.) 'packen, fassen*.
4106:446. cernber (geschrieben cenber) 'Kreis, Ring (z. B. Vis
4121:448. cöh 'Holz*.
4140:450. cun Vie?\ cü, cünän {'^)i^^^)t, Is. 10, 11), cünln^), cünkL
4143:451. ci(h), ci (AM.) was?, wie?\ cirä warum?*.
4182:455. ctden sammeln; schneiden', Praes. öm-em, ein, eine,
```


## [2026-09-06T22:35:19.775Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"kadām\" \"kadam\" \"kū \" \"kuǰā\" \"kas \" \"hēč\" \"čand\" \"čiyōn\" \"čē \" \"čiš\" \"kē \"; do echo \"### $w\"; grep -n -- \"$w\" PHD_mackenzie.txt | head -5; done"
}
```


### [2026-09-06T22:35:21.722Z] TOOL RESULT

```
### kadām
### kadam
3131:kadam [kt)m I M kd)m, N kudam] which, what.
7970:which ce, kadam, kadar, kc.            u'ooden daren.
7971:whichever kadam-iz-e(w).               woodland wesagestan.
9500:rahnimay               ~~          kadam
9502:raycnisn               \t-u~       kadam-iz-C( w)        ~C;~ l".!
### kū 
### kuǰā
### kas 
3250:kas [AYS < A )yfl M ks, N -] person, somebody.
12215:erkas                      ""O~              ewmog                     ,~ (6to'
### hēč
### čand
### čiyōn
### čē 
### čiš
### kē
```


## [2026-09-06T22:35:26.130Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"^ce \\[\" \"^cis\" \"^hec\" \"^cand\" \"^ku \\[\" \"^ciyon\" \"^ke \\[\" \"^kuja\" \"^ciz\"; do echo \"### $w\"; grep -n -- \"$w\" PHD_mackenzie.txt | head -5; done; echo \"--- broad\"; grep -n \"cis \\[\\|hec \\[\\|cand \\[\\|ciyon \\[\\|ku \\[\\|ke \\[\" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-06T22:35:27.944Z] TOOL RESULT

```
### ^ce \[
### ^cis
### ^hec
### ^cand
### ^ku \[
### ^ciyon
8518:ciyonih                  .AU,tu~      carag                       1~<;
8519:ciyon
### ^ke \[
3271:ke [MNW < A mn-w I M ky, N ki] who, which.
### ^kuja
### ^ciz
--- broad
3271:ke [MNW < A mn-w I M ky, N ki] who, which.
```


## [2026-09-06T22:35:30.879Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"somebody\\|nothing, none\\|anything\\|^cim\\|^cis\\|^ciy\\|^cand\\|^hec\\|^kii\\|^ku\\b\" PHD_mackenzie.txt | sed -n '1,40p'"
}
```


### [2026-09-06T22:35:30.931Z] TOOL RESULT

```
3250:kas [AYS < A )yfl M ks, N -] person, somebody.
3272:P kec [kyc I = P] person, somebody.
3340:kii [A YK < A )yk I M hw, N kit, /li] where; that; than.
3344:kiik [kwk'] small, short.
3353:kiin [STE < A ·ft-h; kW1Z I IN,...,] rump, buttocks, anus.
3360:kiin-marz [kwnmle] sodomite; sodomy.
7618:skin carm, dawal, post; toz; (a.) post-       somebody kas, P kec.
8345:kiinI                                    sasabigan
8462:cim                         -E.~      Cimig                       \~C;
8518:ciyonih                  .AU,tu~      carag                       1~<;
8519:ciyon
9555:kiiftan
9690:kiistan                        \\t(.UM     .s   kiirIg                        ,~~
9747:kiihisn                              \t-'U'V,s   zraw-                      -t.\~
```


## [2026-09-06T22:35:38.224Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^c\" PHD_mackenzie.txt | sed -n '1,60p'"
}
```


### [2026-09-06T22:35:38.274Z] TOOL RESULT

```
106:comes from this period.
116:compounds, given the elements and provided that the rules of
141:commonly used by Semitists), through the distinct forms used in
150:certain amount of interpretation is essential. This interpretation
151:can be based, either directly or by the use of analogy, on the less
223:c
243:capital letters. Thus the same letters ,~ are transliterated
262:corruption of the Aramaic root fl~d. Purists will find no difficulty
298:comparative evidence.
306:cited above. Within its terms all the entries in this dictionary are
388:cides with part of that of the infinitive, however much they differ
407:chaean Middle Persian (M) and/or Parthian (P) are given wherever
471:cal.      calendar
5873:cj.--conjunction; n.-noun; pn.-pronoun; pr.-preposition; v.-verb;
6135:calf gawdar.                            certainty abegumanih, tast.
6136:call xrostan, xwandan.                  chaJJ kith.
6137:calumny dusewiizih.                     chain zanJir.
6138:calyx kulafak.                          chalcedony karkehan.
6139:camel ustar.                            chamberlain dar-handarzbed.
6140:camp bunag.                             chance (n.) Jahisn.
6141:camphor kapur.                          chance (v.) Jastan.
6142:can sayistan, tuwan, P sah-; v. able.   change (n.) wardisn, wihirisn.
6143:canape bazmawurd.                       change (vi.) wastan, wihir-.
6145:cane graw, nay.                         changeable rozward, wardisnig.
6146:cane-brake nayestiin.                   channel Jo(y), kahas.
6147:cap kuHif(ak).                          chapter dar.
6148:capable adug.                           character 6yonih; ragih, xem, xog.
6149:capital sahrestan.                      characteristic daxSag.
6151:captive dastgir, griftiir, wardag; v.   chariot rah, wardyun.
6153:captivity dastgraw, wardagih.           charm nerang; v. spell.
6154:caravan kiirawan.                       chase (n.) naxcir.
6155:caravaneer karawanig.                   chase (v.) pazdenidan, taxtan,
6156:care (n.) nigahdar(isn)ih, pahrez;         tazenidan.
6158:care for pahrextan.                     chatter (v.) drayidan.
6159:cared for pad-nigerisn.                 cheek erwarag.
6160:carpenter durgar.                       cheese panir.
6161:carpet bob.                             cheetah yoz.
6162:carriage wardyun.                       cherish parwardan.
6163:carrion murdar, nasa.                   chess catrang; (pieces) K sah, Q
6164:carry burdan; ~ away wiizidan.             frazen, B pit, Kt asp, R madayiir,
6165:carry out hanJaftan.                       P payadag.
6166:case (law) dadestiin, jadag.            chest sen(ag); (box) tabangog.
6167:cast down hambastan.                    chestnut siihbalut.
6168:caste pesag.                            chew judan.
6169:castle, v. chess.                       chicken kark.
6170:cat gurbag.                             chick-pea naxod.
6171:cattle gospand, stor.                   chief (a.) miidayan, (daevic) kamalig.
6172:cattle-stall gostan.                    chief, spiritual- rad.
6173:cauldron deg.                           child aburnay(ag), frazand, rahig,
6174:cause (reason) Cim, wihan(ag); (case)      waccag, zadag, zahag.
6176:cavity gabr.                            childhood aburnayih, rahigih.
6177:ceiling askob.                          childless apus, starwan.
6178:celebrate yastan.                       choice (a.) pad-wizen.
6179:celebration Jasn.                       choice (n.) wizen.
6180:celerv karafs.                          ('hoose wextan, wizidan, wurroyistan.
6181:cemete.ry daxmagestan.                  chooser wizengar.
6182:ce11taur nernasp.                       Christian tarsag.
6185:chronicle karnamag.                         andar amadan; ""'"' to, upon abar
6186:circle <:ambar.                             rasidan; - to an end 0 ham madan.
6187:circular gird.                           comer madar.
```


## [2026-09-06T22:35:43.875Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\] what\\|\\] how\\|\\] thing\\|\\] why\\|\\] nothing\\|] anything\\|\\] some, any\\|] a few\" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-06T22:35:43.916Z] TOOL RESULT

```
1711: . tand [end I = M, N,...,] how many, much?; so many, much; some, a few.
1753:l~e [ME < A mh I M cy, N li] what, which.
1757:~e-ewenag [ME )dwynk ] how.
4996: tis [MNDOM < A mnd(m; ts 1M, J t)'s] thing, affair.
5560:xir [CBW' < A ~bw; hyll M xyr] thing, matter.
```


## [2026-09-06T22:35:56.094Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ec \\[\\|hec\\b\\|ec, hec\\|any(thing)\\|] any\" PHD_mackenzie.txt | head -15; echo \"--- tis ctx\"; sed -n '4994,4999p' PHD_mackenzie.txt; echo \"--- ce ctx\"; sed -n '1750,1760p' PHD_mackenzie.txt"
}
```


### [2026-09-06T22:35:56.162Z] TOOL RESULT

```
3251: --iz [-c] anybody, (with a negative) nobody.
3272:P kec [kyc I = P] person, somebody.
--- tis ctx
 Tir [tyll M tyr, N -] a god (confused with Tistar); astr. Mercury; cal.
    4th month; 13th day.
 tis [MNDOM < A mnd(m; ts 1M, J t)'s] thing, affair.
   --iz [-c I M ..yc] (with a negative) no ... at all.
 tiin [tyln ] thirst.
             '
--- ce ctx
~axAagih [ch.Pkyh] (sense of) taste.
~axMsn [cMln I M, J cxl-, N laf-] taste, flavour.
                           '
l~e [ME < A mh I M cy, N li] what, which.
  - ray: for what, why.
  -ih: quiddity, essence.
2~e [ME, v. l~e] for, because, since, as, that.
~e-ewenag [ME )dwynk ] how.
                                   '
  -ih: circumstances.
~egam-iz [cyk)m-c I M cyg)myc], ........-e(w): a little; whatever.
```


## [2026-09-06T22:36:03.037Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==133' BQT_v2_pages.txt | head -60"
}
```


### [2026-09-06T22:36:04.536Z] TOOL RESULT

```
 ‫‪۷‬‬                                                                                                    ‫‪۳‬‬
                               ‫ومضرب وشمال وجنوب ‪.‬‬           ‫و فتح میم » اسب رهواروتبزرو راگوبند ‪٩‬‏ ‪#.‬‬
‫چهار نظم ‪ -‬کناب از چپار عنصر‬                                ‫کنانه ازچپار عنصر‬           ‫کر کی د‬       ‫چهار‬

                                                   ‫باشد‬      ‫‪ ۰‬است ‪ -‬وتخت شداد را نیزکوبند ‪ -‬وبسنی‌تخت‬
                                                                                             ‫کوس رگفاته‌اند ‪. ۳‬‬
                                             ‫باشد ® ‪.‬‬
               ‫‪:‬‬                     ‫‪1‬‬
                                                             ‫کناباز چهارحدجهان‬              ‫چهار گلخن‬
‫چهر ` ‪ -‬بکراولبروزن مهر؛ رویرا‬                                                                   ‫‪ -‬وچھارعنصراست ‪.‬‬
‫‪ -‬و بمعنی اصل‬          ‫اجنهند‬
                            ‫وی و‬
                               ‫خرب‬
                                 ‫گویند که بع‬
                                  ‫ذات‌نیز | مده أست ‪.‬‬       ‫چهار گو شه = هر چیزی که مربع‬
‫جهر اراد ‪ 3‬با زای هوز بر وزن‬
                                                             ‫وچهارجانب ‪ -‬و مربند ‪ -‬وسفرة کوچك را نیز‬
 ‫همن‬   ‫و‬   ‫همن باشد‬      ‫دختر‬     ‫نام همای‬   ‫مهر ا باد ›‬
                                                                              ‫‪2‬‬          ‫کویند ‪. ۴‬٭‪#‬‬
‫جحکم شریمتی که تابع آن بود او را بتکاح خود‬
                    ‫درآ ورد وداراب ازو متولد شد ‪.‬‬
                                                             ‫جهارم منظر كنابه ازفلك چهارم‬
                                                                                        ‫است که فلك آفتاب ‪,‬اشد ‪.‬‬
‫چهرآزاد است که‬         ‫رتمعن‬       ‫راد‬   ‫جهر‬

‫دختر بپمن مادردار اب ناشلت و نام دخشس افراساب‬                ‫چهار منقو طه کنابه ازفلك کرسی‬
                                                             ‫باشد که فلكالبروح است باعتبارچهارقطة مشرق‬

  ‫بمناست آنکه در افاله ها آهده که تخت‬                      ‫‪- ۴‬‬                 ‫‪.‬‬   ‫مه‬    ‫‪ :‬چار‬   ‫رك‬   ‫‪_ 9‬‬

  ‫ور بارء کیکاوس نیز همین‬
                        ‫شداد را بر بال چهار کرکس بتند وشداد برآن نشت و بهوا رفت» د‬
                                                                                                  ‫افانه گفته اند ‪.‬‬
       ‫چهار کوشه ‪.‬‬                ‫ریسدش‬
                                      ‫تا ک‬                        ‫توشه‬   ‫وساخت‬           ‫گوشه نت‬      ‫در‬    ‫‪- ۴‬‬

  ‫«‪+‬کنجنه ‪٩.‬‏‬         ‫نظامی گنجوی‪.‬‬

                                  ‫کشانور اس‬
                                          ‫ش‬                               ‫‪.‬‬             ‫شاه‬
                                                                                          ‫گكو‪ :‬چ‬
                                                                                               ‫ر ر‬
                                                                                                 ‫‪۴‬‬
 ‫‪ - ۱‬پهلوی ‪( ۲1116‬تخم) «یبر گے ‪« »64‬مسینا ‪ 7116 ۷: ۲۳۱:۲۰‬ط(بیمت‪,‬نژاد‪.‬منظر )‬
  ‫«مناس ‪ )۰۷۲:۲‬ازاوستا ‪( 2۳1101‬تخمه؛نژاد)«بارتولمه ‪)۷۸۵‬پارسی باستان ‪( 871101-‬نوع‪.‬اصل)‬
  ‫‪« _ ۲‬خمانی ‪ ...‬ملقب بشهر آزاد»‬                       ‫اسشق و هوبدمان ‪۳‬‬             ‫ور که‬        ‫ص‪۰۷۱‬‬       ‫«اسفا ‪۱:۲‬‬

  ‫«طبری حص‪٠٤۲‬‏ دریپلوی )‪)011]- 262‬دیوستی‪.‬بندهش ‪»۲۲۱‬شاهنامه«چهرزاد» «فهرست ولف»‪:‬‬
           ‫و‪۲٩‬؟‪.‬‏‬    ‫التواریخ والقصص ‪» 6‬ور ‪۳ :‬‬             ‫«یادشاهی همای چهر آزاد سی سال بود“ «محمل‬

  ‫[ك ‪:‬گاه ]‪ .‬توایی از موسیقی ابرانی » معرب آن‬
                                            ‫چ‪#‬هارگاه _ بفتح اول و دوم ر‬
                                                                           ‫‪.‬‬        ‫«حهار گاء» «دزی ج ص‪۲۲‬‬
  ‫کن هفتم ( لپجهٌ مر کزی )‪ .‬بهلوی‬                     ‫چهار شنبه ‪ -‬بفتح اول و دوم و پنجم‬
  ‫‪« ۲2018۰‬منای ‪ , ۰۷۲۰‬کیلکر ‪7286 200۳۲8115‬؛ روز پنجم از ابام‌هفتةٌ ملمانان‪.‬‬                                       ‫‪۸‬‬

  ‫* چهارم ‪ -‬بفتح اول وضم راء از ‪ :‬چپار ‪ +‬ام ( سوند عدد )‪ .‬پهلوی ‪011۲0۵20‬‬
     ‫ما ‪۲٩ : ۱۳۱‬‏ با ‪« 00۵6۲20120‬مدای ‪ ۰۷۲‬؛ عدد ترتیبی برای چهار ‪ ,‬درمرئبةٌ چهار ‪.‬‬
  ‫‪ #‬چهل ‪ -‬بکراول‪ ,‬دوم بهلوی ‪« 100‬مسینا ‪ ۰ ۲۳۱‬دارسی‌باستان‪ ,‬ازلا‪820 )70‬‬
  ‫پارسی بامتان_ ‪ , 1۵00۳۷5۳0120‬اوستا ‪.259۳2۷۷0126,]-‬هندی‌باستانی ]‪ « 891۲2۷020‬اسفا ‪: ۱‬‬
```


## [2026-09-06T22:36:16.594Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 128 129 130 131 132; do echo \"=== leaf $n (printed ~$((n+540))) ===\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | grep -n \"پهلوی\\|اوستا\\|چه\\b\\|چون\\|چیز\\|چند\" | head -20; done"
}
```


### [2026-09-06T22:36:18.617Z] TOOL RESULT

```
=== leaf 128 (printed ~668) ===
24:‫از آنکه چیزی باجیزی بچبد (‪ )۲‬بابدست‬
52: ‫‪ - ۴‬پهلوی ‪rêc‬‏ ( نوعی‌قرقاول )‬                             ‫‪ - ٩‬بمعاتی اخیر‪ ,‬رك ‪ :‬چخیدن ‪ ,‬چفیدن‪. ‎‬‬
69:  ‫‪ -0‬پهلوی ‪« 60۷6‬بونکر ‪ »۳۵‬طبری ‪ (16‬کیر) «ضاب طبری ‪6۰۳٩‬‏ درعربی «شیق ‪۰‬‬
=== leaf 129 (printed ~669) ===
39:                 ‫وزن بوستان » وچکالرا گوبند ‪.۳۷‬‬                     ‫جکوات ^ ‪ -‬بروزن کوچك ‪ .‬چندرا‬
53:                                  ‫‏‪ = ٩‬چون ‪ +‬آن ‪ .‬رک ‪ :‬اسفا ‪ ۲ : ۱‬ص‪.۰۳,۰۲۱۰۵۹۱‬‬
54:  ‫لد این ‪.‬ر کث‪:‬‬         ‫چون‬      ‫=‬   ‫‪۱۱‬‬            ‫شده ‪.‬‬   ‫(ه‪.‬م‪ ).‬خاط و تخت‬           ‫با«چونن»‬   ‫ظ‪.‬‬       ‫‪--‬‬    ‫‪۶‬‬
59:                         ‫‪ #‬چون ‪ -‬پهلوی ‪ 0081‬از (»(چه) ‪ 201028 +‬گ‬
=== leaf 130 (printed ~670) ===
2:              ‫درجیم فارسی‌با ها مشتمل برسی و چهار لغت و کنات‬
4:‫نوعی ازخیمه باشد‬        ‫چهار اکارن ‏‬               ‫چه = بنتح اول و ظهور انی » مخفف‬
6:‫روانی‪ -‬وچپار حد عالم را نز کفته اند که مشرق‬        ‫اخفای ثانی افادءٌتصغ ر کند چون در اخر کلمه‬
7:                   ‫ومفرب وشمال وجنوب باشد ‪.‬‬        ‫غمچچوه وطاقچه ‪ - ۴‬و بكر اول‬
11:‫چهاراقر ان‪ -‬بسی چهار اران‬                          ‫وخفای ثالی " لفظی است که درمحل تعجب ودر‬
13:             ‫و‪-‬چهار بار رسول را لگیوزنند‪.‬‬           ‫‪-‬نی هرچه باشد ‪ -۵۰‬وجپت‌تعلیل‬
17:    ‫چهار آ لین‪ -‬بمعنی‌خیمة چگها‬                      ‫نم«تواند‬
20:                                                           ‫خواند» چه‌آوازش گرفته است » و‪۷‬عد‬
21:‫و چهار »ذهب را لىز‬        ‫خلفای اربعه هم هت‬        ‫لیز ازرآانده میشود باعتبار جيمو هابعنی سه‬
26: ‫چهار بالش = کنابه از چپار چز‬                      ‫‪E‬‏ وزن سواد ‪ ۰‬سر کوه را‬    ‫‪ ۹‬سفق‬   ‫جهاد‬
30:                                                    ‫چهار ] خرسنگیی د کنابه‌از چپارحد‬
32:‫حهات اربع کهمشرق و مغرب وجنوب و شمال‬               ‫جهان‪ -‬وچهارعنصر باشد که خاك وآب وبادوآ تش‬
37:   ‫‪ = ۴‬ابچه = ابچك (پپلوی) ا=بزه =ابزك = ابجك =‬                         ‫‪ - ۱‬رك‪ :‬چاه ‪۰‬‬
39:   ‫سفدی‪(.۷16‬چه‪,‬چرا)«ینونست ‪.۵*۲:۲‬‬          ‫‪۴‬‬
40:      ‫که خلق برسرمابرزمین بخواهد رفت !‬               ‫‪ _ ۴‬چه سالهای فراوان وعمرهای دراز‬
44:   ‫‪ ۰‬اوستا له (چطوره)‬      ‫یازند ‏‪ » C11‬پارسی باستان ‪yİChsic‬‏ ‪ < ayic marak‬اسفا ‪:1‬س‬
50:                                                                                      ‫اوستا ‪4‬‬
=== leaf 131 (printed ~671) ===
1: ‫چهار کامه‬                                                                                       ‫م‪۷‬‬
3:‫چهارذ یوار جهان ‏ کنابه از‬                                 ‫چهار بالش اکران ‪ -‬کنابه از‬
4:‫چهار طرف عالم ‪ -‬و کنابه اعنزاصر ارعه‬                               ‫خلفای اربعه ‪ -‬وخیمة چهار گوشه باشد ‪.‬‬
5:                             ‫‪.‬‬             ‫چهار بالشت = بممنی‌چهاربااش است | باشد ‪. ۴‬‬
8:               ‫چهار رکیس‬                                   ‫که کنابه ازتشت ومند مولک وچهار عنصر‪-‬‬
10:‫کنابه از شخضصی‬     ‫چهار ر بان‬                               ‫چهار بامك ‪ - ۴‬بنتح میم سوکون‬
14:‫چهار طاق ‪ -‬نوی از خیمه است که‬                          ‫چهار بسیطت کناب از عناص اریمه | _‬
17:                                       ‫چهار حمال ‪ -‬بىمنىچھاربپطا ى | کوشد ‪.۴‬‬
24:                                                           ‫چهاردر یچ سس کنابهاز کوش وچشم‬
29:                                                                           ‫(‪ )۱‬چش‪ :‬هرچیزی ‪.‬‬
30:  ‫‪ - ۴‬درحاشية چك بنقل ازمننسکی منقولاز‬                         ‫‪ - ۱‬رك ‪ :‬چاربالات وچهارباش ‪.‬‬
31:   ‫فرهنك شعوری «چهارواماگ ارا«طاهی صحیح»دانتهو کنته ‪ :‬این‌قول بابعضی سخ فرهنك جهانگیری‬
33:  ‫* چهاربا و چهاریای ‪ -‬پهلوی ‪« 1042۳720120‬مسینا‪ ۲۳۱‬با ‪« 20۳۲20120‬منلی‬
34:  ‫‪ ۰‬سفدی‪ « 010726 1‬بنوست ‪٥۱۲:۲٥‬‏ زباکی ‪ 20726‬ک«ربرسن؟‪»۷‬؛ دارای چهاریا‪.‬‬
36:                                                                   ‫‪ ¥‬چهارپایه ‏ رك ‪ :‬چاریابه ‪.‬‬
37:  ‫‪ › > ۱۳۱:۲‬اوسا‬    ‫ما‬           ‫‪«۱‬‬            ‫*‪ #‬چهارده ‪-‬بفتح اول و دوم وپنجم > بهلوی ‪7‬‬
39:                 ‫عدد اصلی‌میان سیزده و بانزده‪ ,‬ده سلاو چهار ‪.‬‬                 ‫کگلکی ‪«2‬‬            ‫است ‪۹‬‬
40:  ‫‪ #‬چهار دهم ‪ -‬بفتح اول ودوم و پنجم وضم ششم ‪ .‬بهلوی حناحا‪2‬تقطی › از‪:‬‬
41:                             ‫چهارده ‪٣‬‏ ام ) یوند عدد ) ؛ عدد ترئیبی چهارده ‪ ۰‬درمرتبةٌ چهارده ‪.‬‬
42:    ‫٭ چهارسو ‪ -‬فتح اول و دوم = چپارسوک = چارسوق » پپلوی ‪ 805‬هه‬
=== leaf 132 (printed ~672) ===
3:‫چهار نظم ‪ -‬کناب از چپار عنصر‬                                ‫کنانه ازچپار عنصر‬           ‫کر کی د‬       ‫چهار‬
9:                                                             ‫کناباز چهارحدجهان‬              ‫چهار گلخن‬
10:‫چهر ` ‪ -‬بکراولبروزن مهر؛ رویرا‬                                                                   ‫‪ -‬وچھارعنصراست ‪.‬‬
15:                                  ‫ذات‌نیز | مده أست ‪.‬‬       ‫چهار گو شه = هر چیزی که مربع‬
17:                                                             ‫وچهارجانب ‪ -‬و مربند ‪ -‬وسفرة کوچك را نیز‬
22:                                                             ‫جهارم منظر كنابه ازفلك چهارم‬
24:‫چهرآزاد است که‬         ‫رتمعن‬       ‫راد‬   ‫جهر‬
26:‫دختر بپمن مادردار اب ناشلت و نام دخشس افراساب‬                ‫چهار منقو طه کنابه ازفلك کرسی‬
27:                                                             ‫باشد که فلكالبروح است باعتبارچهارقطة مشرق‬
32:                        ‫شداد را بر بال چهار کرکس بتند وشداد برآن نشت و بهوا رفت» د‬
34:       ‫چهار کوشه ‪.‬‬                ‫ریسدش‬
44: ‫‪ - ۱‬پهلوی ‪( ۲1116‬تخم) «یبر گے ‪« »64‬مسینا ‪ 7116 ۷: ۲۳۱:۲۰‬ط(بیمت‪,‬نژاد‪.‬منظر )‬
45:  ‫«مناس ‪ )۰۷۲:۲‬ازاوستا ‪( 2۳1101‬تخمه؛نژاد)«بارتولمه ‪)۷۸۵‬پارسی باستان ‪( 871101-‬نوع‪.‬اصل)‬
48:  ‫«طبری حص‪٠٤۲‬‏ دریپلوی )‪)011]- 262‬دیوستی‪.‬بندهش ‪»۲۲۱‬شاهنامه«چهرزاد» «فهرست ولف»‪:‬‬
49:           ‫و‪۲٩‬؟‪.‬‏‬    ‫التواریخ والقصص ‪» 6‬ور ‪۳ :‬‬             ‫«یادشاهی همای چهر آزاد سی سال بود“ «محمل‬
54:  ‫کن هفتم ( لپجهٌ مر کزی )‪ .‬بهلوی‬                     ‫چهار شنبه ‪ -‬بفتح اول و دوم و پنجم‬
57:  ‫* چهارم ‪ -‬بفتح اول وضم راء از ‪ :‬چپار ‪ +‬ام ( سوند عدد )‪ .‬پهلوی ‪011۲0۵20‬‬
58:     ‫ما ‪۲٩ : ۱۳۱‬‏ با ‪« 00۵6۲20120‬مدای ‪ ۰۷۲‬؛ عدد ترتیبی برای چهار ‪ ,‬درمرئبةٌ چهار ‪.‬‬
59:  ‫‪ #‬چهل ‪ -‬بکراول‪ ,‬دوم بهلوی ‪« 100‬مسینا ‪ ۰ ۲۳۱‬دارسی‌باستان‪ ,‬ازلا‪820 )70‬‬
60:  ‫پارسی بامتان_ ‪ , 1۵00۳۷5۳0120‬اوستا ‪.259۳2۷۷0126,]-‬هندی‌باستانی ]‪ « 891۲2۷020‬اسفا ‪: ۱‬‬
```


## [2026-09-06T22:36:33.508Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 124 125 126 127 134 135 136; do echo \"=== leaf $n (printed ~$((n+540))) ===\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | grep -n \"چند\\|چیز\\|پهلوی\\|اوستا\" | head -12; done"
}
```


### [2026-09-06T22:36:35.349Z] TOOL RESULT

```
=== leaf 124 (printed ~664) ===
=== leaf 125 (printed ~665) ===
5:‫که چوب و هرچیز که برزمین افتاده باشد از‬         ‫‪-‬‬    ‫گا‬
34:  ‫* چوب ‏ پهلوی ‪۳0C‬‏ کردی ‪4۷1‬لا ‪k‬ة‪۷‬آ‪c‬‏ ‪۷ .‬اک « اسفا ‪۲ : ۱‬ص ‪۷۹۲‬و رکھ‬
=== leaf 126 (printed ~666) ===
=== leaf 127 (printed ~667) ===
31:      ‫‪ #‬چو پان (بدواومعروف) ‪ -‬همریشة شبان ( پهلوی ‪٩4°‬‏ ‪( )11[8‬ه‪.‬م‪ ( ).‬از افادات‌استاد‬
52:      ‫یناه برد ودربلغ بیاسود و چندی بد قتل رسید ‪.‬ک‪۶‬رستنن‪ .‬ساسان‪ ۳44.‬ببمد» ‪۵*۵۰ ۹۷:۰‬‬
=== leaf 134 (printed ~674) ===
12:‫چیز یز ‪ -‬بازای هوزبروزن پیش‌خیرز»‬                                                               ‫باازدفرای بونات ‪۳۱‬‬
26: ‫اوستا‬   ‫‪YT‬‏‬       ‫ب رگز ‪.‬دن) «منای ‪۰‬‬                    ‫(چدن ‪۰‬‬      ‫جیلان ‪ -‬بقتح سوم » بهلوی ‪natîc‬‏‬
30:  ‫زمین برداشتن مرغ و فروبردن ‪ -‬زدن شاخه هایکیاه‪ -‬بر بالای هم گذاشتن چیزی ‪ -‬گستردن‬
40:  ‫‪ #‬چیز ‪ -‬بپلوی ‪« 056‬منای ‪ »۰۷۲:۷‬پ=ارسی باستان ‪( 160516‬شینی) الزا‪.>0)1‬‬
42: ‫هرچه موجود باشدهربودنی» امور ظاهری وباطنی‪ «:‬وچیزهاء پنهانی والهی همیشه غالب‌تر وقوی‌نر‬
43:                             ‫بود از چیزهاء طبیمی‌و ظاهری‪ ».‬ک«شف المحجوب سجتالی ‪.*۲۷‬‬
=== leaf 135 (printed ~675) ===
3:                   ‫درخاله آویزند گ‪.‬وبند ر‬               ‫ابن کلمه ازتوابع است وبمعنی‌چیزی کم واند که‬
10:                                                         ‫چیزه بوڈ ‪ -‬بابایابجد (‪ )۱‬و ذال‬
12:‫بمعنی چیلان باشد که عناب است وآنرا سنجد‬                 ‫چه چیزه بوذ کرمیب را کویند که شتا فرین‬
51:  ‫‪ ۸‬اوستا‪ ۱ 42۷01 . ۷819290-‬حزو‬          ‫‪ - ۷‬یز بمعنی چیدن (هم) است ‪.‬‬
=== leaf 136 (printed ~676) ===
16:                                      ‫‪ - ۱‬پهلوی‪ ( 6201‬دام ) « منای‪» ۰۷۲:۲‬‬
24:  ‫اول قس اوستابی ‪ 182۷01-‬جدا شده ‪ .‬مفروق و جزو دوم بمعنی پل است ) ‪ ۶‬بارتولمه ‪540‬‬
32:  ‫حاصل آید چون حرکت کون وحرکت فاد ‪».‬‬           ‫کت‬  ‫ر از‬‫حچیز‬
33:                                                          ‫و آن‬‫دستی‬‫چستی آن‌چیزه وچ‬
```


## [2026-09-06T22:36:51.022Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && for p in 434 435 436 437; do echo \"=== pdf $p ===\"; awk -v P=\"[pdf page $p]\" 'BEGIN{RS=\"\\f\"} index($0,P)' BQT_v3_pages.txt | grep -n \"کس\\|پهلوی\\|اوستا\\|هیچ\" | head -12; done"
}
```


### [2026-09-06T22:36:52.964Z] TOOL RESULT

```
=== pdf 434 ===
39:© پارسی باستان ‎kash[ciy‏ (کسی؛ هررکس ) , اوستا ‎kas[cit‏ (کی):08 اف
44:. ‏کید‎ als ‏راز من که مرا مایت‎ de tp ‏کس‎
49:‏مجوی.‎ SS ‏بدو گفت کسری سخن راست کوی . مکن چاره و هیچ‎
=== pdf 435 ===
13:چیزی دیگر تر کیپ دکردماند و نان کساروآب.
15:کسار نگفثه‌اند ؛ و باکاف فارسی مشپور است .
17:‏نیزاین است چ هکساردن که مصدراست درفرهنگه
20:کساددن * - بنراول بروزن‌شماردن,
25:کسیر - یشم اول و بای ابجد وسکون
39:‏کسبره * - بنم اول وبای‌ابجد و ‎Co‏
46:‏کسیه نم اول و سکون ثانی و فقح
56:‏کستن ‎MO‏ بروزن ‎AS Gee PS‏
58:کسقه = بروزن خفته . غلة کوفتهباشد
66:‏۴ - (عی) 5 ‎alt, CH ol‏ کلیم » اکسیةکغلم‌جمم.»منتهی‌الارب».
70:‏۴ - میج «کار > ‎Ope)‏ است. راد کساردن
72:‏ات ۱ — محیح «کسارنده » است .
=== pdf 436 ===
5:و در عرف ابشان زنار خوانند ومعر بآ نکستیج
6:است؛ و کستین هم بنظ‌آمده است که مد از
8:کستیمه ۴ ‎Jol che‏ بروزن‌پمتیمه,
10:‏کسری ۴ = پکس اول وسکون شا
12:عادلاست؛ و هرباك ازپادشاهان عجم رابیز کسری
16:۱ -کتی = کشتی . ازپپلوی ‎sel kostik‏ است ‎Ls.‏ اخبر ‎We‏ در گزارش‌پهلوی
17:اوستا و در کتابهای پهلوی بمعنی کمربند منصوص زرتشتبان استبمال‌شده, ازآ نجمله درتفسیر بند
19:‎LS‏ مزبور از مادة 6050 ‎gies‏ است که در پهلوی بممنی ‎ghee‏ + سوی » جالب و ‎AT‏ است ودر
20:پارسی نیز کشت وکست بهمین‌معنیآمده, چنانکه درلاتینی 60508 و در انگلیسی 00854 و در
27:‎bd‏ من رن اکنون کز دستهای بسته باچون ‎gis pels‏ بای دگرفت کستی.
28:کتی زرتشتیان را « بند ‎5st op‏ گویند و معرب آن « کستیج» و ‎a”‏
31:‏این کستی از ۷۲ نخ از پشم سفید کوسفند تهیه میگردد و ‎OT‏ باید
=== pdf 437 ===
13:کسمه ‎=F‏ بنتح اود بر وزن وسمه »
17:خود گذارند ؛ و بعضی گویند که کسمه ‎OT‏ موی
21:کسناج ؟ » با ‎op‏ بر وزن ‎«le‏
28:کسندد ‎cle  *‏ اول و نانی و ضم
33:‎VEL‏ - پکس اول و نون بروزن
39:‏کسنی ۲ - بنتح اول و سکون ‎gt‏
41:گیاهی باشد دوائی وتلخ 4 ؛ ‎only‏ معنی بکس
45:‏۱ -«کسکه . غلیه بود ‎Gade gen‏ » محمودی گوید:
54:وآترا کسمه میکوبند »« جپانگیری» رشیدی ‎jt‏ غمین عبارت راآورده با افزودن « و عراق »
55:پن ازهفاری ».- ژاپااگوید: کسمه , شابد ‎hey pam‏ لیتوانی 6358 , روسی 6668 .کردی ‎Kast‏
59:‏شکته کسمه و بر ‎ISS yp‏ کلاب‌زده.
70:‎DF‏ کاسنی. ۵ از :کس ۲ اندر ‎(aig)‏ لفة بمعنی کس دمگر وکس‌غیر؛
```


## [2026-09-06T22:37:01.146Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && echo \"=== pdf 434 full-ish ===\"; awk -v P=\"[pdf page 434]\" 'BEGIN{RS=\"\\f\"} index($0,P)' BQT_v3_pages.txt | sed -n '30,50p'"
}
```


## [2026-09-06T22:37:02.775Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && for p in 539 540 541 542 543; do echo \"=== pdf $p (printed ~$((p+1207))) ===\"; awk -v P=\"[pdf page $p]\" 'BEGIN{RS=\"\\f\"} index($0,P)' BQT_v3_pages.txt | grep -n \"پهلوی\\|اوستا\\|پارسی باستان\\|^کو\\|کجا\\|کدام\" | head -12; done"
}
```


### [2026-09-06T22:37:03.037Z] TOOL RESULT

```
=== pdf 434 full-ish ===
مر و‌باشد ۵ چه ‎Wg‏ مردمی و ناکنی | فيز گفته‌اند - و نم اول موضع جماع زنا‌باشد

‎٩‏ - با لمت شب شکل مه . چون ناخن شیر سیه
با ‎de‏ را زرین ‎eS‏ بر سس نگوت ار آمده .
‎sal‏ خسرو دهلوی « رشیدی © .
۴ - یکی کزه ز دکان سپهر قصاب است که بهر سلخ بالا کشیده اند چنن .
امیرخسرو دهلوی > فرهنگه نظلم».
۴ - میدل «کژین» (هم) . ۴ - از : کر (هیم.) ین ( دبت ) قس :کو
‎ST‏ ,کزآکند .
© پارسی باستان ‎kash[ciy‏ (کسی؛ هررکس ) , اوستا ‎kas[cit‏ (کی):08 اف
پازد ‎kasifea ۰ kas‏ ۰ هندی باستان ‎kds‏ . کردی ع ‎ckesek , kes‏ اقغانی و بلوچی ع

‎. ) ‏استق ۸۵۱ ۰ . ۱ از : کی( ی ( حاصل مستر‎ » kas
: ‏یز بسنی عیچکی آمد‎ - ۷
. ‏کید‎ als ‏راز من که مرا مایت‎ de tp ‏کس‎

‎. ۰ ۵۰ ‏گلتان سس‎ . cue
‏(حامل‎ SHS (aT poate ‏اول و کر دوم ( در شم‎ ete ‏کژی‎ 6
: ‏مصدر ) » کجی »کج بودن , انحراف - دروغ‎
‏مجوی.‎ SS ‏بدو گفت کسری سخن راست کوی . مکن چاره و هیچ‎
.* ‏فردوسی طوسی . شاهنامة بخ ج ص۲۰۷‎ +
```


### [2026-09-06T22:37:06.016Z] TOOL RESULT

```
=== pdf 539 (printed ~1746) ===
2:کوعه
4:کوی ۱ بر وزن جوی » راه فرأخ
55:کوش است که ‎yl!‏ و ظروف دوغ و ماست
67:‎dy - ٩‏ :کو- در پهلوی 0 ( در ترجمة فارسی وندیداد]1 ۰ ۳۰ [ ‎(Lav‏ آمده
=== pdf 540 (printed ~1747) ===
16:کوی هفتاه داه- بکر ‎salt‏
49:‏( کوه, موج.) «هوبشمان ‎AVE‏ 3 = کوهان (ه.م.) ۷ - اوستا18512 (کوچك
51:بلوچی 18580 . 125587 ( کرچك ,کم ‎als‏ « اسشق ۰۸۸۷ , اوستا - لا89 « بارتولمه
52:۰ قی : پهلوی ‎kahishn‏ . 6251000-1025 » پی رکه س ۰۱۲۵ .
=== pdf 541 (printed ~1748) ===
33:پمعنی پلکه ؛ پمعنی از. ودر مورد دعا ‎JE‏ میرود . رك : ایضاً ‎Ne‏ ۸-۸4 .- درپهلوی8 .
34:‎ka‏ ابرانی ‎katy,‏ « بارتولمه ۸۳ ۰۰ اوستا ‎ae‏ پاستان- ‎ka‏ «که ‎٩‏ . چ هکس؟ ۰۰
36:استی 68 ( کدام ‎٩‏ که) . بلوچی ‎(tS an) kai KE‏ . وخی ۷6 , سریکلی ‎COT‏ (یهکسی؛).
37:‎tel. kdl ccs‏ وخی لأ.۷3 , سریکلی ‎OS) ko‏ که * فارسی باید از پارسی باستان ‎kaya‏
=== pdf 542 (printed ~1749) ===
3:کوه بودنده که عبارت از زاهد و عابد و .هرتاض کهبله ‎eae?‏ اول بر وزن بتکده ,
=== pdf 543 (printed ~1750) ===
39:کوهتان است - و نام ولابتی است از خراسان
43:کوز؛ پر آب را کونند ۷
54:کوهکنی ۱۱ .
```


## [2026-09-06T22:37:18.775Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kas\\b\\|hēč\\|hec\\|kas-\" SNS_pages.txt | head -20; echo \"--- leaves\"; grep -c \"\" SNS_pages.txt; awk 'BEGIN{RS=\"\\f\"} END{print NR\" leaves\"}' SNS_pages.txt"
}
```


### [2026-09-06T22:37:20.672Z] TOOL RESULT

```
1978:      Y*/Y^ «WP£. 190) kasica, kas :V kas:i>^J**
1999:                                                                                                                                                         •TA/VTJ "j^u-fckas-iz:                  <3_-*o*>*
2277:                                                                                                                                               akagya- kisate-             :   L    (   -v->=)kas:    ^ J+ a^>-^ *"
3092:                                          .    j»b     .   J>ji' :Ohrmazd:                       -"'                       kSsate :-L a+/kas:fc- .*KT -agah+( -»*£) n + a
4207:                                                                                                                 I                    -Y/1Y^           b^jlj^ib :hec           3   / 5c 3:         _>- e>~
6638:                                                                                   Wi».           kas- L^U*5a5a-: jU*****" casan- : L.
6682:                               ,                                        (AiW>.        :   /kas: 3   l     caksus-:                                               :£l-
14965:                                  58/14              kas 29/18                         cSksus- 158/7
16056:karkis/karkas 214/9      kirfag kunisnlh 216/15              kust 218/5-277/14      manSnd 211/6
16057:kas 29/17                kistan 220/6                        kustar 218/9           man I atasan 240/2
16059:kas-iz 30/3              kGf 216/8
--- leaves
16584
242 leaves
```


## [2026-09-06T22:37:26.088Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport bisect\n# compute leaf for a given line number\ndef leaf_of(lineno):\n    pos=sum(len(l)+1 for l in lines[:lineno-1])\n    return t[:pos].count('\\f')\nfor ln in [1978,1999,2277,4207,6638]:\n    print(ln, 'leaf', leaf_of(ln))\nEOF"
}
```


### [2026-09-06T22:37:27.916Z] TOOL RESULT

```
1978 leaf 30
1999 leaf 31
2277 leaf 35
4207 leaf 59
6638 leaf 94
```


## [2026-09-06T22:37:40.258Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (28,29,30,31,32,58,59,60):\n    p=pages[i]\n    nums=re.findall(r'(?m)^\\s*[-–—]?\\s*(\\d{1,3})\\s*[-–—]?\\s*$',p)\n    print(i, nums[:6], repr(p[:80]))\nEOF"
}
```


### [2026-09-06T22:37:41.761Z] TOOL RESULT

```
28 [] '         IU                              .___,,   .\n                            '
29 [] '     TY                                            iBMvUtelMjlj                 '
30 ['1'] '                                                                                '
31 [] '                                                                                '
32 ['1', '16'] '                                                                                '
58 [] '                                      Uicu-^U^U^Ij\nA6                           '
59 ['1', '1'] '                                            Lu ii-^U <uU »jlj                   '
60 [] '                                     Uje^Ut.b*^                                 '
```


## [2026-09-06T22:37:47.752Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(25,65):\n    p=pages[i].strip()\n    print(i, repr(p[:60].replace('\\n',' | ')))\nEOF"
}
```


### [2026-09-06T22:37:49.606Z] TOOL RESULT

```
25 '" |  |                                                          '
26 '" |          TI                                               '
27 'Tr                                      bc-^bi.L.jl, |        '
28 'IU                              .___,,   . |                  '
29 'TY                                            iBMvUtelMjlj  '
30 ': |  |  |                                                         '
31 'J                                                           '
32 ') |  |  |  |     rr                                       UjtiUMtfUt'
33 'ra                                              |4U   o—^U f'
34 'rY                                                  ,u a-U »'
35 'c |      ri                                                   '
36 '> * |      T1                                            L*L.)'
37 '™ —jt* d^L                                                  '
38 'Uj   o^L <uL     »)\\                    u |       T6 |          '
39 ':    I                                                      '
40 'r                                                           '
41 ',lu c-*ta **U •jlj                                 do |       '
42 'ar                               Ll. c^-,Li uL*}\\ |           '
43 '£Q                                    U_   __U 4.L    «;i   '
44 'LIT                                                         '
45 '61                                   Ui^^Li ^l.;l,          '
46 'J                                                           '
47 "' |  |  |  |  |       fix                                    r |        "
48 'fb                                    Uj tihafU -»-L »;l,   '
49 'Uj .l^UuI *jlj                                              '
50 'x                 :              » |   t    1 |                 '
51 ',Li*.L.;l,                           Yo |                     '
52 '> |  |  |  |  |                                      Lu uu-tfb 4-L *jl'
53 'Yfl |                                 bc-,Uub^                '
54 'Ufrtt^U 4.U«jlj |       YY |                                    '
55 'Li:   fi^bhUjlj                                             '
56 'j                                       v |  |  |  |                '
57 '- |  |  |  |  |                                          bj o—*L= «-L*'
58 'Uicu-^U^U^Ij | A6                                             '
59 'Lu ii-^U <uU »jlj                                           '
60 'Uje^Ut.b*^                                                  '
61 '\\ |  | \\\\ |                                                   Uj C'
62 '\\x                               Ui c*-.b *.b «jl,          '
63 'U*i»««U<»l"j1j                                              '
64 'U; *—-*Li-bo;1 5 | IY |  |  |  |  |           .**«» *>• "** "\' -^y |      '
```


## [2026-09-06T22:38:04.595Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (58,59):\n    print('==== leaf',i)\n    print(pages[i][:2500])\nEOF"
}
```


### [2026-09-06T22:38:06.196Z] TOOL RESULT

```
==== leaf 58
                                      Uicu-^U^U^Ij
A6                                                                                                      g^rUjc^U^L 4jL
                                                                                                                                       AT

               /ya jl abi+yata- ;b-                         «>W:ayyad / ayad

     WW. 224-26) %'d: j* V*                                 «j>» (OTP*.
                                                                ;
                                                                               250)

        1 T /4£ftj*jfefj
                         ayat zL{PS. 29) by't: i5*4*J*j


                                  .cm-3 j.jI*             :hayyar/hayar:        >^yO
                                                t-
 pft UiWb. 1286) yar*_ yavar <- yfi-varana-:
 Mir.   My'wr:,^ (Mir. Man. II, 55)hy'r (bwdyh)
                 (*j±rf)ayZ* i ^ Man. Ill, 48)
                         •




 .^^^S.^A.^thayyarOmandlh                                           :    .^tfA^
                              .
                                  To /w J               -(^Pf) aySrmafidl             :V




        .(*j»fr»)   ay3rl         :       ^       .jjl*   hayy3rlh:       -o±^X-
                                                                •   T/Xl ^ Ofi/i« J
                                                                                                                                            lo

     w,«5 .*tf«* :hayyarlh kardan:                                      t*»5 -J^-j



         .*»*,/-*<0'»*0*W                     l    :aivy3hanlh:




                aiwi^y^o                          aiwySnhana-: fa. aivyahan
                                                                                           *   mJ   J   '
                                                                                                            106) "P«".
                                                                                                                         hapta-   if
     ,jl :^)                          1




       .^^^^ ya^j' yaohana-+(                                            j^/'^'j'



                 jjl»- . Orf-lfr- (-   ^ij.^J: Svgad/Sbgad:                           »J
                                      'J— *C^-     •»

==== leaf 59
                                            Lu ii-^U <uU »jlj                                                                                                      Li_   c-^,Lt*.L.;l,
AY                                                                                                                                                                                                                    A*


                                                                                                                     j.i j
                                           *•»-'*
                   V>A** .*** :c5-hSt:
SstarSd/astarbrSd:      yw-^jij***^ ^u^ i^                                                                           ^"aibi + gata
                                                                                                                             -5   1

                                                                                                                                             "/ ,ji*H (-»£& «jlj c«l o^U _,J
                                                                                                                 >(*;*&•) aibigat: £ (Tavadia. £ n £. 126 :^) «-.-j. ij

     .-i-ilj"^^^" jibrlt + >i-T=astar ji ^S> ^•jl, > C-»|l                            l
                                                                                              1




  O o'r*-
      1
            'j       T
                             fJ->
                                    ** O*   (   Tavadia 5n5. p. 87
                                                                                                                     ^L.,1            aiwyaohana-oU^lj^l.j^Ljji; aivyang: jh-ooj *                                                 A

 ?/f £%. jjbj*- *j              jb^T        ^ ^^^T^^lj                                        .,     I




MiV2>.     18)       Stavant-                        :       ^j-ii. aStavam
          ./r»A61 3TA-TWr—1Y-U/T^ (•>>>*•; M""                                                       '
                                                                                                             V                                                                     etf**^(l     :h§c/5c:              O-**


                                                                                                                 I
```


## [2026-09-06T22:38:25.012Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 kʷo ===\"; grep -n \"q\\^o-\\|q\\^e-\\|Interrogativ\\|Fragepron\" incoming/WLD/WLD_Bd1_pages.txt | head -20"
}
```


### [2026-09-06T22:38:25.063Z] TOOL RESULT

```
=== WLD Bd1 kʷo ===
47928:            quc hinter Formen vom Interrogativ-Indefinitstamme zur Yerstiirkung
49081:         (nur im Adv.), St. des Interrogativums                   und Indefinitums; einzelsprach-
49166:einst“,    wozu auch note nach Interrogativen, z. B. u jzote „was dann“ und
49370:522                                                        q^o-, q; e -,       q“a;   qjji-;    q”u-
51050:cay dun gha), dem so.'to-Pron. ( set gha, sa ha), dem Fragepron. (z. B. lam ha),
51069:„ovye u ), dem so fo-Pron. (z. B. tie-gi ), dem Fragepron. Ckaip-gi „wie“), -gu
```


## [2026-09-06T22:38:27.078Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN who ===\"; grep -n \"^who,\\|^who \\|s\\. who\\|OE\\. hwa\\b\" KLN_1966.txt | head -10; echo \"=== KLN quality ===\"; grep -n \"^quality\\|^quantity\" KLN_1966.txt | head -6; echo \"=== SKT who ===\"; grep -n \"^WHO\\|^WHAT\\|^WHICH\" SKT.txt | head -8"
}
```


### [2026-09-06T22:38:27.160Z] TOOL RESULT

```
=== KLN who ===
3738:who  plays  the  father’,  fr.  ttocxyjp,  ‘father’.  The Gk.  suff.  -aaxfjp  was  adopted  by  the  Latin, whence,  in  the  form  -astre,  -atre,  it  came  into the  Old  French,  resp.  the  French.  Cp.  the  words medicaster,  oleaster,  pinaster,  poetaster.  Cp.  also -ster.
20406:who  makes  yu',  compounded  of  the  imitative base  *yU -,  ‘to  shout  for  joy,  shout’,  and  base *dhe-,  ‘to  place,  make,  do’.  The  first  element appears  also  in  Gk.  Myt],  ‘outcry’,  !ov|coc;, ‘shout  of  joy;  cry  of  pain’,  Eu^eiv,  ‘to  shout, yell’,  Lith.  yvas,  ‘owl’,  MHG.  ju,  juch,  ‘shout of  joy’,  juwen ,  juwezen ,  ‘to  jubilate’,  G.  jauch- zen,  ‘to  shout  for  joy,  exult’.  Base  *yd  is  rel.  to base  *yo-,  whence  MHG.  jodelnjolen,  ‘to  shout, yodel'.  See  yodel,  yowl  and  cp.  jynx.  For  the second  element  in  jubilate  see  do  and  cp.  fact, theme.  See  also  verbal  suff.  -ate.
22746:who  causes  to  forget’,  Pi‘el  part,  of  nashah,  ‘he forgot’  (see  Gen.  41:51),  rel.  to  Aram.  n6sha, Arab,  nasiya,  ‘he  forgot’,  Ethiop.  nahsdya,  ‘he condoned,  forgave’,  Akkad,  mashu,  ‘to  forget’, manatee,  n.,  any  of  aquatic  herbivorous  mammals of  the  order  Sirenia.  —  Sp.  manati,  a  Caribbean loan  word.
24660:who  served  in  the  Russian  army  against  the Turks;  pretended  author  of  a  book  of  wildly exaggerated  exploits  really  written  by  Rudolph Erich  Raspe  (1734-94),  and  entitled  Baron Munchausen,  Narrative  of  his  Marvellous  Trav¬ els  (published  in  1785).
28539:who  called  himself  91X600905,  instead  of  00- 965,  ‘wise  man’,  since  this  latter  term  was  sug¬ gestive  of  immodesty.
31316:Derivative:  qualitative-ly,  adv. quality,  n.  —  ME.  qualite,  fr.  OF.  qualite  (F. qualite),  fr.  L.  qudlitdtem,  acc.  of  qudlitas,  ‘qual¬ ity’,  fr.  qualis,  ‘how  consituted,  of  what  kind', which  derives  from  the  pronominal  base  *quo-, whence  also  L.  quis  ?  ‘who’,  quid ?  ‘what’,  qui, quae,  quod,  ‘who,  which,  what’,  Goth,  has,  OE. hwa,  ‘who’.  See  who  and  words  there  referred to,  and  cp.  the  first  element  in  kickshaw.  For  the ending  see  suff.  -ity.  L.  qudlitas  was  formed  by Cicero  fr.  qualis  as  loan  translation  of  Gk.
=== KLN quality ===
13921:quantity’,  fr.  ist  ex-  and  emere,  ‘to  take'.  See exempt  and  cp.  words  there  referred  to.  Cp. also  exemplar,  exemplify,  sample,  ensample.  For the  inserted  -p-  in  exemplum  (for  *ex-em-iom) cp.  L.  amplus,  ‘large’  (see  ample).
31323:quantity,  n.  —  ME.  quantite,  fr.  OF.  quantite  (F. quantile),  fr.  L.  quantitatem,  acc.  of  quantitas, ‘greatness,  amount,  quantity’,  fr.  quantus,  ‘how great,  how  much,  how  many’;  see  quantum.  L. quantitas  was  formed  fr.  quantus  as  loan  transla¬ tion  of  Gk.  7ioct6t7)i;,  fr.  noaoc,  ‘how  great,  how much’.  Cp.  L.  qudlitas,  loan  translation  of  Gk. 7TO',6tt)s  (see  quality).
=== SKT who ===
```


## [2026-09-06T22:38:36.643Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN who entry ===\"; grep -n \"who,  pron\\|who, pron\" KLN_1966.txt | head -4; echo \"=== KLN what ===\"; grep -n \"what,  pron\\|what, pron\" KLN_1966.txt | head -4; echo \"=== SKT ===\"; grep -n -i \"^who\\.\\|^who (\\|who, pron\" SKT.txt | head -6; grep -n \"Goth. hvas\\|hwa, who\\|A. S. hwa\" SKT.txt | head -6"
}
```


## [2026-09-06T22:38:36.680Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '49370,49400p' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-06T22:38:36.730Z] TOOL RESULT

```
522                                                        q^o-, q; e -,       q“a;   qjji-;    q”u-


„daB           nicht“,          av. ci             „wie“       (instr.,       Bthl. Wb. 584), arm. -c in in-c „etwas“
(= ai. kim-cid, Heillet Msl. 7, 162, Pedersen KZ. 39, 384), das auch im ersten
Glied hierher, mit Abfall des qt- wie i (z-i) „was ?“ ( *<ftid -), instr. i-v
„wodurch. womit“ (Meillet Zfarm.Ph. 1, 148, Hubsehmann Arm. Gr. I 450,
Pedersen KZ. 36, 316; 39, 3S4ff., Brugmann II 2 2, 349, s. auch oben zu
arm. o „wer“) zum Alb. s. o. unter 1
                                ;
                                          gr. rig (thess. xig, kypr. oig, ark.    ;


Mantineia qig ), n. n „wer? welcher, -e, -es?“ und rig, rl „(irgend)wer,
was“, acc. m. *nv erw. zu riva „wonach rivog, Tin, n. a. pi. n. q'ija in megar.
ad /uav „wieso ? rt juqv (Aristoph. Ach. 757, 784), boot, xd „warum“ = lat.
quia\ dafi aber          deswegen schon voreinzelsprachlich in der Bed.
„warum“ festgewesen sei, ist Wackernagel IF. 31, 267 f. nicht zuzugeben,
da auch sg. quid, xi die Entw. zu „warum“ zeigen, s. auch Hartmann
Gl. 6, 342),                 auch            in jon. aooci , att. ana „tivu n. pl.“ (durch falsche Trennung
aus ojroid. aaa                 ,
                                    s.       Wackernagel KZ. 27, 90; 28,                               121 ff.)   und mit dem rela-
tiven a verbunden daaa, att. dxxa.
     Lat. quis, quid „we r, was“ ( fragend, indefinit, relativ, s. zu letzterer Geltung
                   auch hinsichtlich qui), qu) Adv. „wodurcb, wovon (rel.)
Kroll Gl. 3, 3 ft'.,
wie denn, warum (frag.): irgendwie (in Wunschformeln)“ (konnte Abl. q'itd
sein, aber doch wohl auf Gd. eines Instr. *q'ii = av. ci, slov. ci „wenn“,
cech. ci „ob“, ags. usw. JnvT „wie, wozu, warum“, J. Schmidt KZ. 27, 291,
weitere Lit. bei Yf. LEWb. 2 s. v.), qui-n (aus -ne) „wie nicht; daB nicht,
ohne“ (Bgm. IF. 4, 226 ff.), quia-nam (Naevius) „warum“, quia „dafi, weil“
```


### [2026-09-06T22:38:36.757Z] TOOL RESULT

```
=== KLN who entry ===
=== KLN what ===
=== SKT ===
```


## [2026-09-06T22:38:43.861Z] TOOL CALL #53: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T22:38:43.868Z] TOOL RESULT

```


```


## [2026-09-06T22:38:47.036Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN hwa ===\"; grep -n \"hwa,  ‘who’\\|OE.  hwa\\|hwa,  'who'\" KLN_1966.txt | head -6; echo \"=== HUB kas/hic/ciz ===\"; grep -n \"kas\\b\\|hēč\\|hec\\b\\|čīz\\|ciz\\b\" HUB.txt | head -15; echo \"=== SYN interrog ===\"; grep -n \"13\\.3\\|Interrogative\\|WHO (interrog\" SYN.txt | head -10"
}
```


### [2026-09-06T22:38:47.120Z] TOOL RESULT

```
=== KLN hwa ===
20547:kata-,  combining  form.  -  A  var.  of  cata-. katabolism,  n.  —  See  catabolism, katha,  n.,  story  ( Indian  liter.)  —  OI.  kathd,  ‘nar¬ rative,  story’  twhence  kuthdyati,  'tells,  narrates  ), lit.  ‘how  (scil.  happened  this)?’,  from  the  I.-E. pronom.  stem  ka-,  whence  also  OI.  kah,  L.  qms, OE.  hwa,  ‘who’.  See  who.
31316:Derivative:  qualitative-ly,  adv. quality,  n.  —  ME.  qualite,  fr.  OF.  qualite  (F. qualite),  fr.  L.  qudlitdtem,  acc.  of  qudlitas,  ‘qual¬ ity’,  fr.  qualis,  ‘how  consituted,  of  what  kind', which  derives  from  the  pronominal  base  *quo-, whence  also  L.  quis  ?  ‘who’,  quid ?  ‘what’,  qui, quae,  quod,  ‘who,  which,  what’,  Goth,  has,  OE. hwa,  ‘who’.  See  who  and  words  there  referred to,  and  cp.  the  first  element  in  kickshaw.  For  the ending  see  suff.  -ity.  L.  qudlitas  was  formed  by Cicero  fr.  qualis  as  loan  translation  of  Gk.
31324:quantum,  n.,  quantity;  an  object  that  has  quan¬ tity.  —  L.,  neut.  of  quantus,  ‘how  great,  how much,  how  many',  rel.  to  Umbr.  pant  a  (=  L. quanta);  for  *quam-to,  fr.  quam,  ‘in  what  man¬ ner,  as  much  as’,  which  is  rel.  to  Oscan  pan, Umbr.  pane,  ‘as,  as  much  as’,  and  cogn.  with OE.  hii,  ‘how’,  hwa,  ‘who’ ;  see  how,  who,  and  cp. the  first  element  in  quasi.  The  second  element  in *quam-to  expresses  the  idea  of  greatness,  so  that E.  ‘how  great’  is  the  literal  rendering  of  L.  quan¬ tus  (=  *quam-to)  in  accordance  with  the  two elements  of  this  word.  Cp.  aliquant, quaquaversal,  adj.,  turning  in  all  directions  ( said of  geological  strata).  —  Formed  with  adj.  suff. -al  fr.  L.  quaquaversus,  ‘turning  in  whatever  di¬ rection’,  which  is  compounded  of  L.  quaqua, ‘wherever’,  fr.  reduplication  of  qua,  ‘in  what  di¬
31397:Derivative:  quid,  tr.  and  intr.  v.,  quidd-er,  n. quid,  n.,  essence,  quiddity.  —  L.,  ‘what,  some¬ thing,  anything’,  neut.  of  quis,  ‘who’,  cogn.  with OE.  hwa,  ‘who’,  hwiet,  ‘what’.  See  who,  what, and  cp.  quibble,  quiddity,  quiddle,  quip, quid,  n.,  pound  sterling,  sovereign  (Brit.  Slang).
31475:quod,  ‘which’,  in  L.  phrases,  as  e.g.  quod  vide  (ab¬ breviated  q.v.),  ‘which  see’,  quod  erat  demon¬ strandum  (Q.E.D.),  ‘which  was  to  be  demon¬ strated’.  —  L.,  neut.  of  qui,  ‘who,  which’ ;  cogn. with  OE.  hwa,  ‘who’.  See  who. quod,  n.,  prison  (Brit.  Slang).  —  A  var.  of  quad, abbreviation  of  quadrangle,  hence  lit.  ‘a  four¬ angled  court  enclosed  by  buildings  or  a  fence’. Derivative:  quod,  tr.  v.,  to  put  in  prison, quodlibet,  n.,  a  nicety,  subtlety.  —  L.,  ‘what  you please’,  compounded  of  quod,  ‘what’,  and  libel, ‘it  pleases'.  See  quod,  ‘which’,  and  libidinous, and  cp.  quillet.
31477:Derivatives:  quoin,  tr.  v.,  quoin-ing,  n. quoit,  n.,  an  iron  disk ;  quoits  (pi.,  but  construed as  a  sing.),  a  ring  for  throwing  at  a  peg.  —  ME. coite ,  fr.  OF.  coite,  w  hich  is  of  uncertain  origin. Derivatives:  quoit,  tr.  and  intr.  v.,  quoit-er,  n. quondam,  adj.,  former.  —  L.,  ‘formerly’,  for *quom-dam,  fr.  quom,  cum,  ‘when,  as’,  prop,  an¬ cient  acc.  of  qui,  ‘who,  which’  (see  who),  and  the emphatic  sufif.  -dam,  which  appears  also  in  qui- dam,  ‘somebody’,  and  is  rel.  to  the  suff.  -de  and the  prep,  de,  ‘of,  from’  (see  de-). quorum,  n.,  the  minimum  number  of  members necessary  for  the  transaction  of  business  at  an assembly.  —  L.  quorum,  ‘of  whom’,  gen.  pi.  of qui,  ‘who’,  which  is  cogn.  w'ith  OE.  hwa,  ‘who’ (see  who) ;  so  called  from  the  first  word  of  the commission  issued  to  certain  justices  in  Eng¬ land:  quorum  aliquem  vestrum  ...  unum  (duds, tres,  etc.)  esse  volumus  (‘of  whom  we  wish  one, two,  three,  etc.,  of  you  to  be’).
=== HUB kas/hic/ciz ===
111:dran u. s. w. die Vichtigere' Form sein, vgl. die kas.
116:etc.) nachweist, vgl. kas. orE^ are,
2556:ist spar anzusetzen. Der Infinitiv sipdrdan (vgl. kas.
2564:702. Zu den kas. Dialectformen mit l- stimmt jud. tat.
2662:tat. zugol^ zuwol (Miller p. 69), kas. zugol etc.
2896:1893, p. 257, kurd. s« ZDMG. 38, 76, kas. m Shuk.
3070:32, 535 ; 38, 80) mit kark etc. wechselt. Dazu kas.
3093:*Krahe = np. kaldy ZDMG. 32, 536, kas. kelo u. s. w.
3639:147, Shk. 260, jiid. tat. nuf aus nuh, kas. nuh-do)
4686:kareta- ; Osmdn 'HimmeF, paz. asman^ kas. osmnun etc., also
4717:§ 13. Anlautendes a ist geschwunden in g. kas. tas,
5500:'wachsen*, skr. vi + Wzl. vardh; guvdh 'Zeuge* = phi. gukas,
5671:'Erlangung ?; 8) gukas 'Zeuge' --= np. guvah, skr. "^vikaga-":^
5776:stellung Ton gukas mit skr. vi'kag, Yon gukdrdk mit skr. vi'kar (oben
7494:p. 214), g. maSy semn. mestn ZDM6. 32, 538, kas. mussdr
=== SYN interrog ===
23365:13.31 Norse on THE NUMERALS
23366:13.32 Onn
23367:13.33 Atonz, Onty
23368:13.34 Iimsr
23369:13.35 Last
23833:13.31. NOTE ON THE NUMERALS
23835:Except for some suffix-variation and actual substitution in the case of ‘one’ (13.32), the IE words for ‘one’ to ‘ten’ have persisted everywhere with only slight changes other than phonetic; like- wise the IE word for ‘hundred’, while for ‘thousand’ there are several different groups.
23842:The ordinals are formed from the cardinals, mostly with a -to- or -mo- suffix. Exceptions are those for ‘first’ (13.33), and many of those for ‘second’, which are literally ‘the other’ (Goth. anpar, OE oper, ChSl. witori, etc.) or ‘the following’ (Lat. secundus : sequi ‘follow’; similarly Grk. debrepos prob. orig. ‘the one after’, cf. Hom. debraros ‘last’).
23852:13.33 ALONE, ONLY (adj.; adv.)
23895:13.34 FIRST
```


## [2026-09-06T22:38:53.361Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7os",
 "prompt": "Give the reconstructed PIE interrogative/relative pronoun stem, its meaning, the related stems *kʷis/*kʷid, and the descendants listed for Proto-Indo-Iranian, Avestan, Old Persian, Proto-Germanic and Latin. Quote the etymology section."
}
```


## [2026-09-06T22:38:55.774Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%86%DB%8C%D8%B2",
 "prompt": "For the Persian entry چیز: give the full etymology (Middle Persian form, Old Persian / Proto-Iranian ancestor, PIE root) and the meaning, plus any cited references (Hasandust, MacKenzie, Cheung)."
}
```


### [2026-09-06T22:38:58.691Z] TOOL RESULT

```
# Proto-Indo-European *kʷos

**Reconstructed Stem:** *kʷos

**Meaning:** The page references "*kʷís" for the full meaning, indicating this is an interrogative/relative pronoun stem. See *kʷís for complete details.

**Related Stems:** The entry mentions *kʷís and *kʷid as related forms, though specific distinctions aren't elaborated on this page.

**Descendants Listed:** The page does not provide a descendants section listing Proto-Indo-Iranian, Avestan, Old Persian, Proto-Germanic, or Latin reflexes.

**Etymology Section:** "From *kʷ-."

---

**Note:** The Wiktionary entry is minimal and directs readers to the *kʷís entry for fuller information about this demonstrative/interrogative pronoun. The detailed inflection tables show masculine, feminine, and neuter forms across multiple grammatical cases, but specific daughter-language descendants are not documented on this particular page.
```


### [2026-09-06T22:39:02.431Z] TOOL RESULT

```
# Etymology of Persian چیز (čīz)

## Full Etymology Chain

**Proto-Indo-European Root:** *kʷís, *kʷos* ("who, which, what")

**Proto-Indo-Iranian:** *kíš* (derived from PIE root)

**Proto-Iranian:** *čiš-čid* or *čiš-čit* (compound form with *čiš* + suffix *čit* of unknown/possibly reduplicative origin)

**Classical Persian:** چیز (čīz)

## Meaning
"Thing," "matter," "object," or informally "thingamajig" (used vaguely when one cannot recall or prefers not to mention something's name).

## References Cited

The Wiktionary entry references:

1. Rastorgujeva, V. S. & Edelʹman, D. I. (2003), *Etimologičeskij slovarʹ iranskix jazykov* [Etymological Dictionary of Iranian Languages]

2. Nourai, Ali (2011), *An Etymological Dictionary of Persian, English and other Indo-European Languages*

**Note:** The page does not provide Middle Persian forms or cite Hasandust, MacKenzie, or Cheung specifically.
```


## [2026-09-06T22:39:11.255Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7%C3%ADs",
 "prompt": "Quote the reconstruction, meaning, and the descendant lists for Proto-Indo-Iranian, Avestan/Old Persian, Proto-Germanic, Latin, and any note on the relation to *kʷos."
}
```


## [2026-09-06T22:39:12.848Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%87%DB%8C%DA%86",
 "prompt": "For the Persian entry هیچ: give the full etymology (Middle Persian form, Old Persian ancestor such as *aiva-čiy, Proto-Iranian) and the meaning, and any references cited."
}
```


### [2026-09-06T22:39:18.670Z] TOOL RESULT

```
# Proto-Indo-European *kʷís

**Reconstruction and Meaning:**
The term "*kʷís" functions as both a pronoun and determiner meaning "who, what" in interrogative and relative contexts. According to the source, it represents "an interrogative-indefinite paradigm built from the stems *kʷi- and *kʷe-."

**Proto-Indo-Iranian Descendants:**
The entry lists "*kíš," "*kás," and "*kím" as Proto-Indo-Iranian continuants, with further development into Proto-Indo-Aryan forms. These evolved into Sanskrit किम् (kím, "what?"), कः (káḥ), and किस् (kís, "whether").

**Avestan/Old Persian:**
Old Persian derivatives include forms used instrumentally, while Avestan shows 𐬐𐬋 (kō) and 𐬗𐬌𐬱 (ciš) as reflexes of this root.

**Proto-Germanic:**
The entry documents "*hwaz" as the Proto-Germanic reflex, which produced widespread descendants across Germanic languages.

**Latin:**
Latin descendants include quis, quī, quam, and quoque, representing a significant branch of this interrogative-relative system.

**Relation to *kʷós:**
The source notes that "*kʷós," originally a separate o-stem adjective, "was originally separate, but in most languages there was some conflation with the other two."
```


### [2026-09-06T22:39:20.047Z] TOOL RESULT

```
# Etymology of Persian هیچ (hīč)

Based on the Wiktionary entry, here's what is documented:

**Middle Persian origin:** The word derives from Middle Persian (ʾyc /⁠ēč⁠/, meaning "not any"), though the entry notes that the Book Pahlavi script form is needed.

**Meaning:** The term means "not any" in its Middle Persian form.

**Incomplete etymology:** The entry explicitly states: "This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium." It indicates the *č* element possibly traces to Proto-Indo-European *kʷís, *kʷos ("who, which, what"), and questions whether the *hi* represents a phonetic shift from Proto-Indo-European *né ("not").

**References:** No specific academic sources are cited for the Middle Persian etymology itself—only references for Ottoman Turkish derivatives are provided.

The entry acknowledges significant gaps in tracing this word's full genealogy back through Old Persian and Proto-Iranian stages.
```


## [2026-09-06T22:39:27.998Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%AC%D8%A7",
 "prompt": "For the Persian entry کجا: give the full etymology (Middle Persian, Old Iranian/Avestan ancestor) and meaning, plus references cited. Also mention the compound analysis if given."
}
```


## [2026-09-06T22:39:29.123Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/who",
 "prompt": "Give the etymology of English 'who' (Old English hwa, Proto-Germanic *hwas, PIE root) and any mention of what, why, which, how, where, when, either, neither, and the root *kwo-."
}
```


### [2026-09-06T22:39:33.995Z] TOOL RESULT

```
# Etymology of Persian کجا (kojâ)

## Origin and Development

The word کجا derives from **Middle Persian** (script not provided in source). Through surface analysis, it combines کو (ku/ko, "where") + جا (jā, "place").

## Meaning

The primary meanings are:

1. **Interrogative adverb**: "where" — used to ask about location
2. **Secondary interrogative sense**: "how," "when," or "under what conditions"
3. **Obsolete conjunction** (pre-12th century): "because," with synonyms including زیرا (zirâ) and چون (čon)

## Linguistic Note

The entry indicates Middle Persian ancestry but does not provide the Old Iranian or Avestan precursor forms. The document states the etymological connection is from Middle Persian /⁠kū gyāg⁠/ but leaves the Middle Persian script itself as "[script needed]," suggesting incomplete documentation of earlier Iranian language stages in this source.
```


### [2026-09-06T22:39:36.320Z] TOOL RESULT

```
# Etymology of "Who"

**Old English Origin:**
The word "who" derives from Old English *hwa*, meaning "what person," which also could mean "what; anyone, someone; each; whosoever."

**Proto-Germanic:**
It descends from Proto-Germanic *\*hwas*, with cognates including Old Saxon *hwe*, Danish *hvo*, Swedish *vem*, Dutch *wie*, German *wer*, and Gothic *hvo*.

**Indo-European Root:**
All these forms trace back to the PIE root *\*kwo-*, described as the "stem of relative and interrogative pronouns."

**Related Interrogatives:**
The document confirms this same root (*\*kwo-*) underlies several other English question words:

- **"How"**: An adverbial form from the identical PIE root
- **"Which"**: Compounds *\*hwi-* (from *\*kwo-*) with *\*likan* meaning "body, form"
- **Related pronouns**: The page lists entries for *whose*, *whoever*, and *whoso* as linked terms

The etymology demonstrates how a single ancient root generated most English interrogative pronouns through various Germanic transformations and semantic specializations.
```


## [2026-09-06T22:39:45.306Z] TOOL CALL #61: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7%C3%ADs\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7os\" \"https://en.wiktionary.org/wiki/%DA%86%DB%8C%D8%B2\" \"https://en.wiktionary.org/wiki/%D9%87%DB%8C%DA%86\" \"https://en.wiktionary.org/wiki/%DA%A9%D8%AC%D8%A7\" \"https://www.etymonline.com/word/who\"; do python3 tools/fetch_source.py \"$u\" --note \"page 297, root Kwo/Kwi 1: PIE interrogative-relative stem and its Persian reflexes (čīz, hīč, kojā) and English who\" 2>&1 | tail -2; done"
}
```


## [2026-09-06T22:39:46.735Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ===\"; grep -n \"q^o-\\|qʷo-\\|kʷo-\\|interrog\" IEC.txt | head -10; echo \"=== ARY چیز/کس/هیچ/کجا ===\"; grep -n \"چیز\\|هیچ\\|کجا\\|کدام\" incoming/ARY/ARY_pages.txt | head -20"
}
```


### [2026-09-06T22:39:49.089Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c0df667ceccbd9fc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/77544de9c3cccba4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4b42ca67ff77651f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5407d7f8667c6d5d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ec90a43de05d2354.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/68bab213ed1419e5.txt
```


### [2026-09-06T22:39:49.145Z] TOOL RESULT

```
=== IEC ===
845:aut (auti, autim, autom) (out-, etc.) "but, yet, only'. Cf. autos, autios. WP I, 14, 188. Possibly a cpd. of a and ut(i), q.v. Skt. utá “also, even Av. uta; OPer. utà; Oss. cf. äftä, utà “thus? Gk. aŭ, aŭte, aütis, aütin, cf. also autí-ka ‘forthwith’ and autar “how- ever; Alb. veti (“of itself: Dor. auteí), veç Chur, from *autisi); vetëm ('only': Lat. au- tem); Lat. aut or, cf. OLat. aut ^neverthe- less? beside autem "at least’; Osc. aut, auti "but, or; Ir. cf. uath- (cpds. mono-, auto- and see autos below); OCS uto ‘if whether; ever” (as an interrog. particle: 'altogether")
1048:bha, bho ‘indeed’. WP II, 136. See next Skt. (Vedic) cf. bha-la; Per. ba-li ‘yes; Arm. ba (cj. ‘that, adv. ‘yes’. *a or *à); Olr. ba (an interrogative particle); Go. (infix) -ba- P; OCS bo (cj. *for); Li. cf. ar-ba ‘or’; bei indeed”
13852:qu- (residual element of the relative and interrogative pronoun, type quà, q.v.) Vedic kü ‘where’; (Skt. kva, id.); Alb. ku, id. Oss. ku, kwi ‘when, if”; Per. kü beside kujà ‘where’; OS.OFris. OE hü ‘how’; OCS cf. kù- de “where?
14044:(quiios, variant of type quoios quoiios, q. v.) Alb. cf. i ci-li, f: e ci-la (interr. & rel. “who, which"); OCS Om. f: oa, neut: Ce, interrog. ‘whose’
14115:quo-dhen (-dhən-, -dhə) ‘by, in what; to, from what; where’. WP I, 523 Av. kaða ‘how’; Per. -kada, -keda “-where, -place'; Hitt. (ambig.) cf. kwatan, kwatin ‘whither; why’; Gk. (ambig.) póthen ‘whence’; Alb. kah as prp. 'towards'; Osc. cf. puf, Umb. pufe “anywhere”; MIr. caidhe, interrog. ‘what; where’; Go. hwad, hwad- ‘whither’; ON hva- óan ‘whence’; (z-gde in) OCS küde ‘where’ (and com. Sl.); beside Srb. kod ‘among, care of; Li. cf. kadan-gi because’, fr. *quodhen- ghi or sim.)
14224:quos, retrospective prn. ‘who’. Cf. quis, quoios (quoiios), etc. WP I, 520 Skt. kas; Av. ko; OPer. ka; Per. kas (in hic kas *nobody); Oss. Dig. ka; Arm. o; beside ov; Go. hwas, id.; Li. Latv. interrog. & rel. kas, id.
=== ARY چیز/کس/هیچ/کجا ===
17:۱- هیچ واژه‌ی فارسی که ریشه‌ی هند و اروپایی آن ناشناخته است آورده نشده است. صدها
150:گهواره گاه این مردم هند و اروپایی کجا بود؟ واضح است که زبان هند و اروپایی خود بگی از
237:چیز باشد: ۱-کوج موی هدر اروپانیان از خاستگاهی واقم در مرکز به سوی حاشیه بوده است (از
338:اصلاً از کجا میدانیم که هند و اروپائیان بومی محل‌های فعلی خود نبودند واز.
374:هیچ دلیل مستندی برای چنین فرضیه‌ای وجود ندارد.... در مورد هند و اروپائیان هیچ گواه و
414:چیز دیگری که دریافتند این بو که هر چه به عقب برویم شباهت زبانها بهم پیشتر می‌شود. مثلاً
520:است که هیچ زبانشناسی نمی تواند هر سه را بررسی کرده و به این نتیجه نرسد که هر سه
585:نداشته‌اند و چیزی جز نشانه‌های مصنوعی برای نشان دادن فرگشت زبان‌های مختلف یستند. پرخی
707:اِ مردم شمال دریای سیاه را ناچیزتر از شباهت‌های فرهنگی میان ایرانیان و مردمان شمال و خاور
1263:سئولیت صحت ردیابی‌های دسته دوم مستقیماً به عهده‌ی من است. البته هرکجا که کاملاً مطمشن 8
1352:آلمانی: 1307) از کجا آمده و اجریشه‌ی هند و اروپایی آن چیست؟ ۸30۶ موی
1371:دارد ولی هیچکدام از پسگشت‌های در دسترس من اشاره‌ای همریشه‌های ایرانی و سانسکریت این
1390:-واژه‌ی فارسی «چیزه با واژه‌های فرانسوی 270873 و اسپانیایی ۲08۸ و پر تغالی 0018۸ از
1538:آشکار است). لازم به ترضیح است که در هیچ کدام از مراجع اشاره‌ای به رابطه‌ی "آرواره" با این واچریشه‌ی هند و
1744:۱- رابطه‌ی واژه‌ی "آستر"(پهلوی )) با دیگر واژه‌های این فهرست در هیچ کدام از پسگشت‌ها(مراجع) من
2787:این واژه را در هیچ فرهنگ فارسی نیافتم ولی واژه‌های اوستایی 11101۸۰ و پهلری 1101۸0 بنابه روایتی هنوز در
2806:۱ چون هیچکدام از پسگشت‌ها به رابطه‌ی واژه‌های فارسی و پهلری وکردی این فهرست با واژه‌ی اوستایی و دیگر
3966:۱ ریشه‌ی این واژه در هیچکدام از مراجع فارسی در دسترس من پیگیری نشده است.
6428:۱ هیچیک از پسگشت‌های فارسی ریشه‌ی اين واژه را نمی‌دهند.
6513:> هیچکدام از پسگشت‌های فارسی ریشه ی این واژه را نمی‌دهند. َ
```


## [2026-09-06T22:39:59.587Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"^چیز\\|^ *چیز \\|چیز:\\|چیز(\" ARY_pages.txt | head -10; echo \"--- latin index\"; grep -n -i \"CHIZ\\|KAS\\b\\|KOJA\\|KODAM\\|HICH\" ARY_latin_index_pages.txt | head -15"
}
```


### [2026-09-06T22:39:59.643Z] TOOL RESULT

```
237:چیز باشد: ۱-کوج موی هدر اروپانیان از خاستگاهی واقم در مرکز به سوی حاشیه بوده است (از
414:چیز دیگری که دریافتند این بو که هر چه به عقب برویم شباهت زبانها بهم پیشتر می‌شود. مثلاً
--- latin index
177:Gee shen Se Obj SF dba CEES were Se tI 9 WUT golly 9 Kas
688:aghs y dled obey y atily! abe Kas cheats I pp76 1) abe hyo dled pay
1849:KAZATI AKAS, AKASAT _;(AVESTAN) ghey! :
1850:AKAs, AGAH H(PAHLAVD 5 dy :
1923:BARNHART: a MATIKKAS: (LITHUANIAN) wily)
2043:ey foe Kas SANSKRIT) 2, Scaler
2334:rrr Lge Kas EvOD (WELSH) 533
2537:CHICHAT RUSSIAN) a3 SHNOSHAG :(PAHLAVI) «5 3hay
2739:10 Loe Kas AUT!
3204:CHICHU, (SANSKRIT) ey Sile CHUCHIK, KURDISH) «52,5
3207:BERNIAKAS BALI-
3560:BERNIAKAS, (LITHUANIAN) (gl 53 ABURNAY, (PAHLAVI) 6 shay
4252:OFT - OFA y OP OY i luskas abc! :(OLD SCANDINAVIAN) 254}
5647:ad tgs Kas (THROW) 1139, (TURN) 1176
5743:‘TEKINAS, TAKAS:(LITHUANIAN) .¢\ 33 -TACHINO, TACHAR, TAKA
```


## [2026-09-06T22:40:04.492Z] TOOL CALL #64: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T22:40:04.532Z] TOOL RESULT

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


## [2026-09-06T22:40:05.222Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"kas\" \"kē\" \"kū\" \"čē\" \"hēč\" \"čand\"; do echo \"### $w\"; grep -n -- \"$w\" NYB_vol2_glossary.txt | head -4; done"
}
```


### [2026-09-06T22:40:06.712Z] TOOL RESULT

```
### kas
334:ak [’k] Prth if, in unfulfilled condition, construed with past pt. + Prth. opt. of h- (v. I, p. 175) both in ners and in apo- dosis: ak šitv "dišt (HWY-ndy =) ahéndé 6 be Grak ākasī būt ahēndē if a cairn had been built it would have been visible from the outside HajA:9. — MPrth °g; < *hak < Av. (1742) hakat ‘at once, at the same time', ef hakar.
340:of -h; thus it cannot be connected with dkas (q. v.), which also differs in meaning. From Olr *ā-kāda-, derived through. the suff. -0a- (OInd -tha-) from *kä-, Skr cäyati ‘to notice, to be aware’ (v.s.v. cašm-kāi). As ws. formed by the suff. -tha- are abstracts we have to explain *ā-kāda- as ‘being with information, having good information’. cf Skr ā-manas- ‘being of favorable mind’. As to the spelling, cf
358:ākasī [’ksy] Prth: ~ bütan to be, become visible HajA:9. — From Av. (459) ā-kas-; FrO VIII viduš: ’ks; MPrth ?gs ‘apparent, visible’. The final -y is not the silent final -y abundantly written in Prs. in- scriptions and in the Ps.; this is wanting in Prth (quite exeptionally written in site, vitavané, q. v.). Here -y is a real ending, whether -č or - is not clear, found in some cases where a pred. adj.
409:. 644 ané the one... the other 407-5; be man an kas ... ne no one but I 34?; u an and others, ‘etc.’ 581; an otherwise (?) 4076 (1st ZK).
### kē
267:m-ic 5525-26; han katärcihe ke hac den ākāh, ~ 6716; har martom kē ..., ~-is 909; 5 kē.. up the thread of a narrative after a lengthy gualification: pas hac matani... —-išan 4018-19; 807-5; 871-2, — OP adakiy;
335:akah [’k’s] aware, knowing 39%, 574. 108?; ~ kartan to inform 10%, 11%; kē hac dén ~ he who is enlightened by Religion 6716; subst. pl. cas. obl. kam ~-Gn the ignorant, the witless 11077. — MPrs .g?
343:akahčh [’k’syh] information, message 32. 72. 4613. 594; — religious doctrine(s) and tradition(s) commonly accepted by the community (in contradistinetion to pat- tākēh, g. v.) 1095-28, 1117-15; ~ governing an inf.: the accepted doctrine (tradition) is that 111!!.2223. — Paz. NP ägähi; FrO VIII: vaččim [Av. (1321) vaédaya-]: ākāhēh. — V. kār-ākāhēh, visp-äkäheh. äkähönitan [~-ynytn'] to inform a p. of (hac) 1373-24, 4727,
347:a-kanārakēh boundlessness, endlessness, of Ohurmazd 637-28,
### kū
365:+tākēš [**kwš] a hug: kū-šān pat ~ frac grift gl. 43%, v.s. v. *hārēftan and v. griftan. — Text: ’knyh, meaningless. NP dgós, dyó&.
407:ümurZitan [’mwleytn'] to forgive, to absolve, with be 3114. 35%. 67°; to pity 76°; Gi hac 61... bē āmuržīt this (bull) shielded him 49°, with the gl. kū-š gāvān haciš apāc dašt. — Ps. pt. ’mwicyt; Paz. dmuržidan, NP ämurzidan; MPrth subst. ’mwjd ‘compassion’ (A-H III), "mwždyft ‘mercy’ (S); MPrs ’mwrzydn (S), pres. >muw(r)[2- (Sogd. 45); Verbum 168 sq. Av. (1175) moroždā- pres. ‘to forgive’, marazdika- "mercy'.— V. also an-āmuržišn. āmušt [Pmwšt'] crushed 2622-24, — < *a-murst < *d-mrsta- < à + Av. (1150) marod- ‘to destroy’, cf MPrth >mStn, pt. ’mst ‘to crush, to destroy’ (A-H III), which seem to go back, quite irregularly, to *āmdrsta-; as to -rst > -št cf dāštan, vaštan, vitaštan; the explanation given in Verbum 218 is not satisfactory. Ghi- lain 99.
459:~ ... kū where 3722, 401-2.16 868; refer- ring back to the rel. adv. ku: giyak ku... ~ the place where 74 = õi vyāk ki...
509:apar-āstišnēh [’pl’stSnyh] the act of ac- cepting and taking care of: ~ % én den rād 589, with the gl. kū tà? pat én den bē éstat (subju. 3d p. sg., v. estátan) ; 5919. — < apar + ēstātan; as to the alternation é-: à- cf ästenisn.
### čē
### hēč
### čand
```


## [2026-09-06T22:40:11.816Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '258,272p' NYB_vol2_glossary.txt"
}
```


### [2026-09-06T22:40:11.858Z] TOOL RESULT

```
a-bod [bwd] unconscious 103%. — V. béd (1).
a-burt-framanéh [?bwlt!-plm’nyh] insub- ordination 13$. — Cf framän-burtär.
Mew sa
a-buržišnīk [?bwlesnyk], comp. ~-tar dishonoured 7529-21, . Paz. aburzešni. V. buržišnik and buržitan.
aeürénitan [>c*lynytn'] to make ineffec- tive: bé acdrénét (sc. your work) with the explanation akartārēh-ic 6 šmāh dahét he will create ineffectiveness for you, he will make your work inefficacious 45?. — Den. of a-cär, v. car. V.s.v. axtäyisneh.
acišy [PcSy] Ps.: v. haciš.
adak [DYN], with encl. ’DYN-m = adak-im, 'DYN-š = adak-iš etc. (DYN-n — adak-in HajB:5, v. -n); 'DYN-e — adak-ic, then, by then, at that moment; in that case, this being so: 1. at the beginning of a sentence 28°. 2975 sq. 37— 61 passim, etc.; u ~ 399. 5421; u m-ic 377; — placed after the first w. of a sentence: api-$ ~ 417-8; 5022, 4118; v. also below. — 2. ~ ka at the time when 3615. 4117. 4415, — 3. introducing the apodosis a) after hakar HajB:9-10; 19'-5 and passim; b) after ka HajB:5; 183-1? and passim; ~ ka...
. at the time when ..., then the x“arrah 3615-16; — c) after other clauses: idi... rasdt, ~~... 4125-24; cë han hom dit
. —-iš 4074-25; pat et ku ..., vēhān
m-ic 5525-26; han katärcihe ke hac den ākāh, ~ 6716; har martom kē ..., ~-is 909; 5 kē.. up the thread of a narrative after a lengthy gualification: pas hac matani... —-išan 4018-19; 807-5; 871-2, — OP adakiy;
-hacadar.
., xtarrah =
md... 90, — 4. taking
MPrs ’yg = eg < *ayag; Paz. aig, ag; aigin, agin: thus not only FrP 25, but also Mx and SGV, probably the petri- faction of ’DYN-n HajB:5 (v. above) with the obsolete encl. pron. -n. - HajA: 10 ’dyn: v. adyàn.
a-dän [’d’n'] ignorant, foolish, of a man 415; dumb, brute, of an animal 122. — V. danistan.
```


## [2026-09-06T22:40:33.476Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\] when, if\\|\\] when\\b\\|AMT\" PHD_mackenzie.txt | head -8"
}
```


### [2026-09-06T22:40:33.518Z] TOOL RESULT

```
3110:ka [AMT < A )mty I M k), N ki] when; if, since.
3266:lkay [A YMT < A )ymt I N -] when?
```


## [2026-09-06T22:40:56.514Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"caeca\" \"cec\" \"cvant\" \"caiti\" \"cahya\" \"cis-ca\" \"cisca\"; do echo \"### $w\"; grep -n -i -- \"$w\" BRT.txt | head -4; done"
}
```


### [2026-09-06T22:40:58.616Z] TOOL RESULT

```
### caeca
### cec
5529:PS.:  armcil;  s.  aatct  airimt.  —  O  Them.,  vgl. 7PkuHaii;ä.  Hds.  'mSidö.  GcECn  DST.S  'möi- iäJi  spricht  Bi,  %  ig^.  I.
5917:VeI.  SBE-  47.  165.  —  ')  Der  Mann  hLess  im Non.  luDächst  *asnia  j^airrS,  ä.  i.  'lichter lllmmer;  der  rcEcIrechte  Gen.  dazu  ist  alnS i'.im-atö  Yt,  13.  96  2.  Stelle.  Aus  *asma i'anz-a  entstand,  indem  das  Nominaliv-a  durch riis  KooipositionS'D  ersetit  wurde,  asmöJ^atn-i Yt.  /.  30,  dem  dann  als  neuer  Gen.  asmS.. i'aTK-atff  Vl  7J.  96  I.  Stelle  mr  Seite  trat. l)et  Kompilaior  von  Yt.  /j  hat  iwei  Männer draus  gemacht.    NA.  trennt  ßlscblich.
13678:*duimaa)r-  m.,  red.  Bild.;  Et.?')  —  'iuiday-, lum  V.  iat>d-  {%  $3  I);  ai.  buddhiy  f.;  vgl. apailLbiuH.  —  Ri.;  sahm  nimäyiSnlh  'Angsl- erregen,  Inangstversetzen',  mit  der  Erl.:  an bavel  ka  gäaiit  ka:  pa  snlh  gcdklha  icmem ;  s. dazu  No.  1  und  Reichelt  WZKM.  1$.  143. —  I)  Das  Wort  steht  unter  den  strafrecht- lichen Term.  Cecbn. ,  aber  zu  Unrecht.  Man hat  die  mit  der  Straftat  beabsichtigte  Wirkung für  die  Straftat  selbst  genommen.  Nach  V. 4. 17  könnte  an  derSlelle,  der  das  Wort  ent- DOmmen  ist,  etira  gestanden  haben :  *yö  narim duiuwi^uida  datäili  aetaS  Ai  "?-  (Name  der Straftat).  —  »  Vil.  zu  nhd.  taub  usw.
15730:KompA.,  E. ;  AbleiL  —  ü.  pirvä-  Adj. ;  vgl. gr,  «/iJ».  —  Pa.:  ffi;  %,  noch  No.  12.  — 0  Vgl.  No.  3-4  und  S  3^8,  3,  36S.  43.  — ^)  fcur'.  —  1)  pauf.  —  Ki  poBut'.  —  S)  So K.  Stall  'raya  gcEchr.,  gebildet  wie  nmSnya, S  413.  —  6)  Vgl.  S  y>3-  7-  —  »  VgL  anter afäxlara-.  Bei  den  Peraern  geschah  die  Be- zeichnung der  Himmelsgegend  wie  bei  den Indem  (usw.)  mit  dem  Gesicht  nach  Osten.  — S)  NA.  faramiay.  f*  «tcht  fehlerhaft  für  r". Vgl.  ätauga-  No.  a.  —  «  Die  Bedeutungen a  und  3  sind  nicht  immer  icharf  zn  trennen.
### cvant
5092:Akk.  der  Beziehung:  astica  Im  tä  -vaili bqtS  yavaiti  fra'kasäi  Y,  ig.  7;  V.  2, 19 PüZ.  b)  mit  dem  Korrelat  cvant-:  cval M  nä  aiayaiti  ivai  aAmäi  ttatre  mlidgm anhati  . .  °v<^  As  nä  asayäiti  "val  akmai
6622:Yt  14-34',  —  c'^  airiAe  asti  usvar7Z3m  V.  j  —    cvants  anAin    alte   kata  V.  5, 1 1 ;  —
11221:•  j.  £avant-  Adj.:  s.  unter  cvant-.
11495:cvant-  n
### caiti
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
2554:nominale  Beifügung;  in  den  meisten  'tat  .  .yat  a:£'ar3t>m  Yt.  J9.48;  46;  — Fällen  entspricht  unser  bestimmter  Artikel  'te yä  spö.jataca  .  -  V.  7,  3;  —  Ue yöt  spatui (schwachtoniges  'der');  a)  adjektivisch:  V.ij.ai,  22,  43;  —  'taisqm yöi gius  sar?- caiti  'te  mi>fa  tava  yat  ahurahe  mazdat  oanqm  V,2.4i;  Ytj.9,  12;  —  'lat?hqm "wie  vielfach  sind  deine,  des  AhM.  Ver-  (GPm.)  yat  myazdanqm  N.  6j;  —  ku>a träge?"  V,4,2;  —  "te  daxma  .  .  aniarSt  (Stverz.)  ti  v>r>zyqn  He  yöi  masdayasna naSmät  iarürirva  V.5.51;  —  i-.a  Vam  ;  V.  5,  i  o  usw. ;  42,  J.18",  (/.3,  26,  9.49, (APm.)  aJsnt^m(s±)..paiti.bar,ltN.ioj;'—  *Vd.i8-20i;  —  't^m  (als  ASn.)  .\  yat °tayä  urvarayä  älan»irfs'V.8.i$;N.6j,'Vd.\spiln~'  .  .  X.ij.sS.  2)  auf  ein  Relati-
2899:•  j.,  g.  'ao}ah-  n.  '(physische)  Kraft,  Stärke': asistim  narl  alaotw  °Jö  Y.  60. 3;  —yakmi niyne  nars  'Jartha  Y.  /o.  a ;  —  ai-avaia '}arfka  yaia  yal  panca  narS  "mit  solcher Kraft,  als  wären  es  fünf  Männer"  V.  jj. loPaZ.;  Yt,2.i2,  14;  —  usla  U yd  ä"j 'jaiika  vasöjciairä  ahi  haoma  Y.9.25; —  kacaiti  dim  aspahe  "Jö  uitrahe  °Jö vlrahe  °j<>  Yt.  it).(i&;  8.2^^;  —  "jö  tanvö vispaya  Yt/.^.29;  —  -jö  vJspdMnüM  Y. 5.17;  —  drfahela  paiti  °)arakö  Yt,  i_j. 134;  ~-  y~'  itfsfro)  arinam  ..  matilüm 'jö  abaraiii  \t  14.12;  —  apa  .  .  buei'ä- °}5  , .  barahi  apa  pä',ayä  sävar»  Yt.  10. 23;  62;  —  haomö  asibil  yöi  ..  zävari "jssca  baxhili  Y.  9. 22; —  °Jasca  nn- S«)Wf'a..Y.  77.8,  yi.j.22,y.i,Y.  72.6;  — yS  nü  asSif  °janAil  vandayaÜJ  (sd.)  ., gae^am  Y.50,3.  a)  AS.  °jö  als  Adv,
3525:den  ist's  yü  andusat  *'tat'>  ajayaunia (sd.)  N.  54;  —  caiti  ta  syadhna  varlta .  .  fraSa  'ta  ■'  anusvarsta  aiAhat  hala I  syaohnavar»za  (sd.)  ,  .  "wie  vielfach  sind die  getanen  Taten  . .  —  begangen  (sind sie),  nicht  beglichen,  nicht  wieder  gut gemacht—:  es  werden  . ."  Y.i$.\.
### cahya
### cis-ca
### cisca
2649:•  j.  aenah'vant-  Adj.  -Gewalttat,  Frevel übend  an  — '  (Lok.):  yff  cisca  akmi  nmUne .  .  'nat^Aä  asH  masye  Y.i^.aS.
8859:gäiu*saste\t 5. 102.  a)  mit  Gen,  part: hamistayalca  .  ,  kahe  kahyäcU  drvatqm Y.  61. a,.  3)  mit  vorangehendem  Relativ und  folgendem  1)  clt  (hinter  ka-\  2)  ^a (hinter  i kay-)  'Jeder  der..,  quisquis,  qui- cunque',  nur  substantivisch;  1)  nur  gAw.: y3  dalnqm  vokB  *sänsttl  (sd.)  manatthä .  .  kas^l  Y.4p.  5;  —  «ÄJ  ahmäi  yahmai Ulla  (sd.)  iahmäicit  .  .  däyät  akurö  Y. 43- 1 ;  —  at  .  .  s?rao^  jantü  .  .  ahmäi yahmäi  vasi{%A^  Ikahmäi^i'^.  44.16;  — ^ao^anäi/.  .  pailyaogJt  {sA.)  tä  .  .  yä  Tm AuJyätSi/ (sd.)  payät  '.  käclt  (NPn.)  Y. 4tf.8.  2)  yS  lcisca'^>    ahmt   nmsne  .  .
11084:bilden,  uzw.  in  Verbindung  mit  1)  dem Pron.  intcrrog.  'kay:  cisca  "quisque"  H.  2. II   (Sp.  425  u.).  2)  demPron,  reljo-:
12404:—  aii'afitS  ahi  abatthö  tarn  yö  aAurS mazda  "V.  ig,  2q;  —  cisca  tarn  caraitis ahi  yqm..iäraitinqm..sraistqm  dädansa Vyt.57(?)*>;  — s.  noch  V.  2. 43  bei  i  und "  Bh.  4. 6,  15  bei  3.  3)  1  im  Ap.  voi dem  veraJlgemeineraden  kä  (Sp.  42a); tuvam  k3  Ayc^  aparam ..patiparsäAy'Bh. ^.6J>;  15^;  —  tuvam  kä  xsäya^iyt^  hy(^ aparam  *ahy  Bh.4, 19,  5,  14.  \  4)  sonst beliebig;  a)  an  der  Spitze  des  Satz(teil)es; o)  unmittelbar  vor  Vok.:  tvim  mazäa ahura  frs  mü  sXsä  ..Y.zS.w.  ß)  sonst: tarn  mafhanahe  pSta  nipäta  ahi  adrmqm Yt:  io.  80;  80,  29*,  V.  ig.  6,  VyL  22,  2^, —  iäm  aisqm  tbi^yatam  tum  aliqm tbalsaauhatqm  fialsä  sSndayeAiYtlo.'j6;\ 23'.  »9tJ,  78',  5-  87.  IS-  55-  b)  in andrer  Stellung;  a)  unmittelbar  vor  Vok.: aoa  nS  tarn  mi^ra  .  .  dayU  Yt.  10.  94;  Y. 37.36;  —  äatmltüm  aridvl  sUre  anakite .  .  piium  ralcaya  Yt5. 77;  —  aai  tarn sarahuitra  .  .  V.g.  12,  10.  18;  — -  3af ya/  /am  tara%uftra  .  .  V.  //.  4;  Vyt. 4-3-  ß)  sonst:  *pouru.narim  tarn  kin- näH  ..  Y.  io,  13;  —  i^a  ml  tsm  kam.- caranuha  .  .  Yt //,  60;  —  Aanalsa'  ta tarn  tat  mlzd^m  yal  ..  Y.  5p.  30;  — äa^  mqm  tQm  fiaonayeke  '^.ii.i;  V.  22. I.  9t  Vyt  13  rSt;  — •  aal  tarn  pascatta  .. V.  i".  4;  Vyt^/;  —  yat  tum  ainim  avaS- fiäiS  .  ,  H.a.  13;  — •  yaha  tarn  trftvd (sd.)  vaia/ghe  V,5. 17,  ai;  Vyt i2.
```


## [2026-09-06T22:41:21.726Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 297 -l 297 -r 500 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg297hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg297hi.png'); print(im.size)\nw,h=im.size\nim.crop((int(w*0.20),int(w*0.28),int(w*0.50),int(w*0.40))).save('p297_cav.png')\n\"; ls -la p297_cav.png"
}
```


### [2026-09-06T22:41:25.261Z] TOOL RESULT

```
(4250, 5500)
-rw-rw-r-- 1 sfmqrb sfmqrb 8787 Sep  6 18:41 p297_cav.png
```


## [2026-09-06T22:41:28.564Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg297hi.png')\nim.crop((900,1350,2100,1850)).save('p297_av2.png')\nim.crop((900,1850,1900,2400)).save('p297_op.png')\n\""
}
```


### [2026-09-06T22:41:30.554Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T22:41:32.889Z] TOOL CALL #71: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p297_av2.png"
}
```


### [2026-09-06T22:41:32.910Z] TOOL RESULT

```

```


## [2026-09-06T22:41:55.517Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg297hi.png')\nim.crop((880,2680,1700,2900)).save('p297_lat.png')\nim.crop((950,1950,1900,2400)).save('p297_op.png')\n\""
}
```


### [2026-09-06T22:41:57.764Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T22:42:00.067Z] TOOL CALL #73: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p297_lat.png"
}
```


### [2026-09-06T22:42:00.080Z] TOOL RESULT

```

```


## [2026-09-06T22:42:02.336Z] TOOL CALL #74: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p297_op.png"
}
```


### [2026-09-06T22:42:02.353Z] TOOL RESULT

```

```


## [2026-09-06T22:42:09.147Z] TOOL CALL #75: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg297.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/297.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/297.png"
}
```


### [2026-09-06T22:42:09.210Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 66500 Sep  6 18:42 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/297.png
```


## [2026-09-06T22:47:35.070Z] TOOL CALL #76: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk297.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_KWIS = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7%C3%ADs\"\nW_KWOS = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7os\"\nW_CIZ  = \"https://en.wiktionary.org/wiki/%DA%86%DB%8C%D8%B2\"\nW_HIC  = \"https://en.wiktionary.org/wiki/%D9%87%DB%8C%DA%86\"\nW_KOJA = \"https://en.wiktionary.org/wiki/%DA%A9%D8%AC%D8%A7\"\nE_WHO  = \"https://www.etymonline.com/word/who\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1,\n \"lang\": \"Avestan\",\n \"words\": \"kô, ka 1, kŭ 1, kŭ-thra, ka-hya; kâ 3; kam 1, kam-čit, katama; kat; ka-da, ka-tha; katâra\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Every form in this box is an Avestan reflex of the PIE interrogative-indefinite stem, and all of them stand \"\n  \"in Pokorny's entry itself (IEW 644-648). Nom. sg. m. Av. kō < PIE *kʷos (= Skt. káḥ, Goth. ƕas, Phrygian κος); \"\n  \"gen. sg. Gathic ka-hyā / ča-hyā < *kʷesyo (= Gk. τέο, OCS česo, OHG hwes); fem. kā, also adv. kā 'how?' (instr.). \"\n  \"kŭ = Av. kū 'where?' and kŭ-thra = Av. kuθra/kuδra 'where? whither?' belong to Pokorny's third stem *kʷu- \"\n  \"(so Skt. kú, kútra, kúha), which is the adverbial ablaut grade, not to *kʷo- proper - a nuance the chart flattens \"\n  \"but does not misstate. kat = Av. kaṯ, the neuter *kʷod used as an interrogative particle 'nun, ob?' (= Skt. kad, \"\n  \"Lat. quod, Lith. kad); kam / kam-čit = acc. *kʷom (Pokorny cites 'av. kam-cit in irgendeiner, jeder Weise' beside \"\n  \"Lat. quam, Goth. ƕan); katama- is the superlative formation *kʷo-tm̥mo- 'which of many' (= Skt. katamá-) and \"\n  \"katāra- the comparative *kʷo-tero- 'which of two' (= Skt. katará-, Gk. πότερος, Goth. ƕaþar, Lat. uter); \"\n  \"ka-da = Av. kada 'when?' (*kʷo- + -dā, = Skt. kadā) and ka-tha = Av. kaθa 'how, when?' (*kʷo-dhe/-tha). \"\n  \"The cross-reference ☞De 2 is to the deictic *-dhe/-de suffix and is correct.\"),\n \"derivation_fa\": (\"همهٔ صورت‌های این جعبه بازتاب‌های اوستاییِ ستاک پرسشی-نامعینِ هندواروپایی آغازین *kʷo-/*kʷi- هستند و \"\n  \"همگی در همان مدخل پوکورنی (صص ۶۴۴–۶۴۸) آمده‌اند: kō (نهادی مفرد مذکر) از *kʷos، هم‌ریشه با سنسکریت káḥ و گوتی ƕas؛ \"\n  \"ka-hyā (اضافیِ گاهانی) از *kʷesyo؛ kā «چگونه؟» صورت ابزاریِ مؤنث است. kū و kuθra «کجا؟ به کجا؟» به ستاک سومِ *kʷu- \"\n  \"بازمی‌گردند (قس سنسکریت kú، kútra) که پوکورنی جداگانه آورده است. kaṯ همان *kʷod خنثی در کاربرد ادات پرسشی است، \"\n  \"katama- ساخت عالی *kʷo-tm̥mo- «کدام از میان چند»، و katāra- ساخت تفضیلی *kʷo-tero- «کدام از میان دو» (قس یونانی πότερος و لاتینی uter). \"\n  \"kada و kaθa نیز با پسوندهای قیدیِ -dā و -θā ساخته شده‌اند. ادعای نورایی در این گره درست است.\"),\n \"sources\": [W_KWIS, W_KWOS],\n \"ref_check\": [\n   {\"ref\": \"POK:644\", \"status\": \"supports\", \"note\": \"IEW p.644 (POK_02.txt leaf ~300, line 4812): head-entry 'kʷo-, kʷe-, fem. kʷā; kʷei- ...; kʷu- (nur im Adv.); die betonten Formen sind Interrogativa, die unbetonten Indefinita' and immediately 'av. kō (Gen. gthav. ka-hyā, ča-hya), fem. kā wer?, welcher?; ... av. kā wie?'.\"},\n   {\"ref\": \"POK:648\", \"status\": \"supports\", \"note\": \"IEW p.648 (POK_02.txt, section '3. Stamm kʷu-'): 'Ai. kú, av. kū wo?; ... ai. kutra, av. kuδ-ra wo? wohin?; ... av. kuδ-a wie?' - i.e. Nourai's kŭ 1 and kŭ-thra.\"},\n   {\"ref\": \"BQT:1748\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' ed. Mo'in p.1748 = BQT_v3_pages.txt pdf page 541: Mo'in's footnote s.v. کو/کی reads '... در پهلوی kē. ایرانی *ka-, kay- «بارتولمه ۴۳۰», اوستا ka-, پارسی باستان ka- ... فارسی باید از پارسی باستان kaya- ...' - the Avestan/Old Persian ka- stem, exactly Nourai's claim.\"},\n   {\"ref\": \"HRN:196\", \"status\": \"supports\", \"note\": \"Horn, Grundriss p.195-196 (HRN.txt leaves 216-217), no. 876 '(1)ki(h) wer, welcher? dass etc. ... ap. aw. ka- wer?; päz. ka (Conjunction), ke (Pronomen), ku (Partikel); ai. ká-', and no. 878 '(1)kei wann? wie? ... aw. kada wann; ai. kadā wann?'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW I 644-648\", \"stance\": \"supports\", \"note\": \"the whole entry kʷo-/kʷe-/kʷei-/kʷu-; Avestan kō, kahyā, kā, kam-cit, kaṯ, kada, katāra, kū, kuδra all cited there.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 514-523 (p.522 read in WLD_Bd1_pages.txt line 49370)\", \"stance\": \"supports\", \"note\": \"running head 'q̯ᵘo-, q̯ᵘe-, q̯ᵘā; q̯ᵘi-; q̯ᵘu-'; this is the WP entry Pokorny abbreviates as 'WP. I 514ff'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kwo-\", \"stance\": \"supports\", \"note\": \"'kwo-. Also ki-. Stem of relative and interrogative pronouns ... [Pok. kʷo- 644.]'.\"},\n   {\"src\": \"BRT\", \"where\": \"AiW cols. 425 ff. (BRT.txt lines 8859, 11084)\", \"stance\": \"supports\", \"note\": \"Bartholomae's articles on ka-/kay- cite 'kahe kahyācit drvatam Y.61.2', 'kas-cit', 'čisca quisque', i.e. the same paradigm.\"}\n ]\n})\n\nnodes.append({\n \"id\": 2,\n \"lang\": \"Persian\",\n \"words\": \"kŭ «کو»; kojâ «کجا»; kodâm «کدام»; kay 1 «کی ۱»; kî «کی ۲»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"All five New Persian words continue the Old Iranian ka-/kū- stem through Middle Persian, and MacKenzie's \"\n  \"Concise Pahlavi Dictionary gives every link: 'kū [AYK < A ʾyk | M kw, N kū, ku] where; that; than' (p.51) > NP کو; \"\n  \"'kadām [ktʾm | M kdʾm, N kudām] which, what' > NP کدام (Horn no.843 adds the footnote that the -u- of kudām is late, \"\n  \"Pāzand kadām, and compares Skt. katamá-); 'kē [MNW < A mn-w | M ky, N kī] who, which' > NP کی/که, which Horn no.876 \"\n  \"traces to an Old Persian *kaya- (cf. Skt. kaya-); 'kay [AYMT | N -] when?' and MP ka 'when; if' > NP کی ۱ 'when?', \"\n  \"which Horn no.878 derives from Av. kada = Skt. kadā. کجا is a Middle Persian compound kū gyāg 'where place' > kujā \"\n  \"(Pāzand kūjā, Horn no.843), NP کجا; MP gyāg > NP جا, with -ū- + gy- > -jā-. The two homographs کی ۱ (kay 'when?') \"\n  \"and کی ۲ (kī 'who?') are correctly kept apart.\"),\n \"derivation_fa\": (\"هر پنج واژهٔ فارسی نو از راه فارسی میانه به ستاک ایرانی باستان *ka-/*kū- می‌رسند و مکنزی همهٔ حلقه‌ها را دارد: \"\n  \"پهلوی kū «کجا؛ که» ← «کو»؛ پهلوی kadām ← «کدام» (هرن ش ۸۴۳ یادآور می‌شود که ضمهٔ کُدام متأخر است و صورت پازند kadām بوده، \"\n  \"قس سنسکریت katamá-)؛ پهلوی kē ← «کی ۲/که»، که هرن (ش ۸۷۶) آن را از پارسی باستان *kaya- می‌داند؛ پهلوی kay «کی؟» و ka «چون، اگر» \"\n  \"← «کی ۱»، که هرن (ش ۸۷۸) آن را با اوستایی kada و سنسکریت kadā می‌سنجد. «کجا» ترکیبی است از فارسی میانه kū gyāg «کدام جای» \"\n  \"که به kujā بدل شده (پازند kūjā) و در فارسی نو «کجا» شده است. ادعای نورایی درست است؛ تنها باید افزود که پیوند از راه فارسی میانه است، نه مستقیم از اوستایی.\"),\n \"sources\": [W_KOJA],\n \"ref_check\": [\n   {\"ref\": \"BQT:672\", \"status\": \"partial\", \"note\": \"BQT_v2_pages.txt leaf 132 (printed ≈672) is the چهار.../چهر page; the Persian k- pronouns are NOT there - Mo'in's footnote on کو/کی is on p.1748 (checked, see node 1). p.672 is the page the author also cites for the چ- box, so this looks like one ref block copied to both Persian boxes.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, PHD_mackenzie.txt lines 3110, 3131, 3266, 3271, 3340\", \"stance\": \"supports\", \"note\": \"'ka [AMT < A ʾmty | M kʾ, N ki] when; if, since'; 'kadām [ktʾm | M kdʾm, N kudām] which, what'; 'kay [AYMT < A ʾymt] when?'; 'kē [MNW < A mn-w | M ky, N kī] who, which'; 'kū [AYK < A ʾyk | M kw, N kū, ku] where; that; than'.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 843 (p.190) and nos. 876, 878 (pp.195-196)\", \"stance\": \"supports\", \"note\": \"'843. kuǧā wo?; welcher?; kudām was für ein? ... aw. kū wo? ... phlv. k(u)dām (päz. kadām), päz. kū wo?, kūjā; ai. kú, kúha'; '878. (1)kei wann? wie? ... aw. kada wann'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann col. 13852 s.v. qu-\", \"stance\": \"supports\", \"note\": \"'qu- (residual element of the relative and interrogative pronoun) ... Per. kū beside kujā where'.\"},\n   {\"src\": \"BQT\", \"where\": \"Mo'in's ed. p.1748 (vol.3 pdf 541)\", \"stance\": \"supports\", \"note\": \"footnote: 'در پهلوی kē ... ایرانی *ka-, kay- «بارتولمه» ... اوستا ka- ... پارسی باستان ka- ... فارسی باید از پارسی باستان kaya- ...'.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt / ARY_latin_index_pages.txt\", \"stance\": \"silent\", \"note\": \"grep of کو/کجا/کدام as headwords returns only running prose; Aryanpur's root dictionary does not treat the interrogative pronouns.\"}\n ]\n})\n\nnodes.append({\n \"id\": 3,\n \"lang\": \"Avestan\",\n \"words\": \"č-, čŭ, čî 2; čiš 2, čiš-ca 2; čeč; cit; čaiti, chvant; ča-hyâ\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The box collects the palatal (*kʷi-/*kʷe-) half of the same paradigm, and almost all of it is verifiable: \"\n  \"Av. čiš 'wer?' < *kʷis (Pokorny 647: 'av. čiš wer, čišca = lat. quisque, gr. τίς τε, apers. čiš-čiy'); čiš-ca \"\n  \"(Bartholomae, AiW col. 425: 'čisca \\\"quisque\\\"'); čiṯ - printed here as cit - 'sogar, jedenfalls' < neuter *kʷid \"\n  \"(= Skt. cit, OP čiy, Lat. quid); čī 'wie?' (instr., Bartholomae AiW 584, quoted in WP I 522); čvaṇt- 'wie viel?' \"\n  \"and čaiti 'wie viele' < *kʷe-ti (Pokorny 646: 'daneben mit idg. e av. čaiti wie viele, bret. pet'); ča-hyā, the \"\n  \"Gathic genitive beside ka-hyā. The initial č- is the regular Indo-Iranian palatalisation of *kʷ before a front vowel, \"\n  \"so *kʷis > čiš while *kʷos > kō in the same paradigm. The one form I could not verify is 'čeč : whether': it is in \"\n  \"neither Pokorny 644-648 nor the Bartholomae text on disk, and it duplicates the sense already carried by čiṯ; \"\n  \"the printed page (checked at 500 dpi) really does read čeč, so this is the book's form, not a misreading - most \"\n  \"likely Nourai's own rendering of the čiṯ/čiš-ca particle, or a misprint. Hence 'plausible' rather than 'confirmed'.\"),\n \"derivation_fa\": (\"این جعبه نیمهٔ کامی همان صرف را گرد آورده و بیشتر صورت‌هایش راستی‌آزمایی‌پذیر است: اوستایی čiš «که؟» از *kʷis \"\n  \"(پوکورنی ص ۶۴۷: «av. čiš wer, čišca = lat. quisque»)، čišca (بارتولمه ستون ۴۲۵ «quisque»)، čiṯ «حتی، به هر روی» از *kʷid خنثی \"\n  \"(قس سنسکریت cid و لاتینی quid)، čī «چگونه؟» (ابزاری، بارتولمه ۵۸۴)، čvaṇt- و čaiti «چند؟» از *kʷe-ti، و ča-hyā اضافیِ گاهانی. \"\n  \"č آغازین حاصل کامی‌شدنِ منظمِ *kʷ پیش از واکهٔ پیشین در هندوایرانی است؛ از همین‌رو *kʷis به čiš و *kʷos به kō بدل شده است. \"\n  \"تنها صورتی که در هیچ منبعی نیافتم «čeč: whether» است؛ تصویر صفحهٔ چاپی نشان می‌دهد که خودِ کتاب همین را چاپ کرده (خطای خوانش اسکن نیست) \"\n  \"و احتمالاً خوانشِ خودِ نورایی از čiṯ/čišca یا خطای چاپی است. بدین سبب حکم گره «با احتیاط پذیرفتنی» است.\"),\n \"sources\": [W_KWIS],\n \"ref_check\": [\n   {\"ref\": \"POK:644\", \"status\": \"supports\", \"note\": \"IEW 644 opens the entry that includes the kʷei-/kʷi- stem; the Avestan palatal forms are set out under '2. Stamm kʷei-' on p.647.\"},\n   {\"ref\": \"POK:648\", \"status\": \"partial\", \"note\": \"p.648 is the kʷu- section ('av. kū wo?, av. čū wie, in welchem Maße? (č- nach čī wie?)'); it does give Av. čū, i.e. Nourai's 'čŭ', but the bulk of the palatal forms are on 647, not 648.\"},\n   {\"ref\": \"BQT:1748\", \"status\": \"not_found\", \"note\": \"checked BQT_v3_pages.txt pdf page 541 = printed 1748: it is the کو/کی page of Mo'in's Borhan and says nothing about the Avestan č- forms. This ref block is evidently the one belonging to the k- box, repeated.\"},\n   {\"ref\": \"HRN:196\", \"status\": \"partial\", \"note\": \"Horn p.196 (HRN.txt leaf 217) is the کِه/کی page; the Avestan č- forms are at Horn no.451 (p.101): 'či(h), či was?, wie? ... ap. čiyakaram, -čiy (enclit.); aw. čiš, čiṯ; ai. -cit'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 646-648\", \"stance\": \"supports\", \"note\": \"'av. čiš wer, čišca = lat. quisque, gr. τίς τε, apers. čiš-čiy; av. čī wie (Instr.)'; and 'daneben mit idg. e av. čaiti wie viele'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 522\", \"stance\": \"supports\", \"note\": \"'av. čī wie (instr., Bthl. Wb. 584)' in the same paragraph as Gk. τίς and Lat. quis, quid.\"},\n   {\"src\": \"BRT\", \"where\": \"AiW cols. 425, 584 (BRT.txt lines 11084, 12404, 5092)\", \"stance\": \"supports\", \"note\": \"'in Verbindung mit 1) dem Pron. interrog. čay: čisca \\\"quisque\\\"'; and the entry with the correlative čvant- ('čvaṯ nā ... čvaṯ ahmāi').\"},\n   {\"src\": \"HRN\", \"where\": \"no. 451 (p.101) and no. 447 (p.100)\", \"stance\": \"supports\", \"note\": \"'451. či(h) ... aw. čiš, čiṯ'; '447. čand einige; wie viel? ... aw. čvant- wie viel?; phlv. čand'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4,\n \"lang\": \"Persian\",\n \"words\": \"čeh «چه» (also چی); čŭn «چون»; čîz «چیز»; čand «چند»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Persian چه goes back to Middle Persian čē (MacKenzie: 'čē [ME < A mh | M cy, N čī] what, which'), from Old \"\n  \"Iranian *čiy / *čī, the neuter *kʷid of the same paradigm; the colloquial چی that Nourai prints in brackets is the \"\n  \"Manichaean MP cy / New Persian čī of the same entry. چون is not a simple continuation of Av. čū but a Middle Persian \"\n  \"compound: Horn no.450 and Mo'in's footnote in Borhan (p.669, BQT_v2 leaf 129: '#چون - پهلوی čigōn از (چه) + gōnag') \"\n  \"derive it from čē + gōn(ag) 'colour, kind', i.e. 'of what kind' > 'how' - hence also چگونه; Nourai's arrow is right \"\n  \"about the first element only. چیز is MP čiš/tis 'thing' (MacKenzie prints 'tis [MNDOM < A mndʿm; tš | M, J tys] thing, \"\n  \"affair'); Mo'in's footnote (Borhan p.674, BQT_v2 leaf 134) says outright 'چیز - پهلوی čiš، پارسی باستان čišciy', and \"\n  \"Wiktionary (after Rastorgujeva-Edelman) reconstructs Proto-Iranian *čiš-čid - so چیز actually belongs one step lower, \"\n  \"under the Old Persian čiš-čiy of box #5, though the stem is the same. Watkins lists it in the same root entry \"\n  \"('15. Persian chīz, thing: CHEESE²'). چند is MP čand (MacKenzie 'čand [cnd] how many, much?; so many; some, a few') \"\n  \"from Av. čvaṇt- 'how many', Horn no.447.\"),\n \"derivation_fa\": (\"«چه» از فارسی میانهٔ čē (مکنزی) و آن از ایرانی باستان *čiy/*čī، همان *kʷid خنثی، است؛ صورت گفتاری «چی» که نورایی \"\n  \"در کمانک آورده همان čī فارسی نو و cy مانوی است. «چون» بازماندهٔ سادهٔ صورتی اوستایی نیست، بلکه ترکیبی است فارسی‌میانه: \"\n  \"هرن (ش ۴۵۰) و حاشیهٔ معین بر برهان قاطع (ص ۶۶۹) هر دو آن را čigōn = «چه» + gōnag «گونه، رنگ» می‌دانند («چگونه» نیز از همین‌جاست)؛ \"\n  \"پس تنها جزء نخستِ آن به این ریشه بازمی‌گردد. «چیز» از فارسی میانهٔ čiš/tis است و معین در حاشیهٔ برهان (ص ۶۷۴) صریحاً می‌نویسد: \"\n  \"«چیز - پهلوی čiš، پارسی باستان čišciy»؛ بنابراین «چیز» در واقع دنبالهٔ همان čiš-čiy است که نورایی در جعبهٔ پارسی باستان آورده، \"\n  \"نه دنبالهٔ سادهٔ ستاک اوستایی. «چند» از پهلوی čand و اوستایی čvaṇt- است (هرن ش ۴۴۷). ادعای نورایی در کل درست است.\"),\n \"sources\": [W_CIZ],\n \"ref_check\": [\n   {\"ref\": \"BQT:672\", \"status\": \"partial\", \"note\": \"the exact page 672 (BQT_v2_pages.txt leaf 132) is the چهار.../چهر page, but the block pp.669-674 that Nourai is pointing at does carry all of Mo'in's relevant footnotes: leaf 129 (p.669) '#چون - پهلوی čigōn از (چه) + gōnag'; leaf 130 (p.670) the چه entry with its Pahlavi/Avestan footnote; leaf 134 (p.674) '#چیز - پهلوی čiš، پارسی باستان čišciy'. Off by one or two pages, presumably the OCR page-offset (±3) rather than a wrong citation.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, lines 1711, 1753, 1757, 4996\", \"stance\": \"supports\", \"note\": \"'čand [cnd] how many, much?; so many, much; some, a few'; 'čē [ME < A mh | M cy, N čī] what, which'; 'čē-ēwēnag how'; 'tis [MNDOM; tš | M, J tys] thing, affair' with 'tis-iz (with a negative) no ... at all'.\"},\n   {\"src\": \"HRN\", \"where\": \"nos. 447, 450, 451 (pp.100-101)\", \"stance\": \"partial\", \"note\": \"'450. čūn wie? ... phlv. čigōn wie? (či + aw. gaona-), čigāmīč, vergl. np. čigūne' - i.e. چون is a compound, not a bare reflex.\"},\n   {\"src\": \"BQT\", \"where\": \"Mo'in's Borhan pp.669, 674\", \"stance\": \"supports\", \"note\": \"footnotes quoted above; Mo'in's چیز note gives Old Persian čišciy explicitly.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kwo-, item 15\", \"stance\": \"supports\", \"note\": \"'15. Persian chīz, thing: CHEESE²' - Watkins puts Persian čīz under exactly this root.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5,\n \"lang\": \"Old Persian\",\n \"words\": \"ka 1, kam 1; kâi-gi; čiy 2; čiš-čiy, kaš-čiy; aiva-čiy\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"Four of the five items are straight out of Kent's Old Persian lexicon and are correct: 'ka- interrog.-indef. \"\n  \"pron. \\\"who\\\": Av. Skt. ka-, Gk. πο-, Lat. quo-, NEng. wha-t, PIE *kʷo-. With encl. -čiy, \\\"any\\\": kaš-čiy (DB 1.49, 53; \"\n  \"DSe 37)'; '-čiy encl. particle, emphasizing or generalizing ... Av. -čiṯ, Skt. cid, Gk. τι, Lat. quid, PIE *kʷid'; \"\n  \"'či- interrog.-indef. pron. \\\"what, any\\\" ... čiš-čiy asn. \\\"anything\\\" (DB 1.58), Lat. quicquid, PIE *kʷid-kʷid'; and \"\n  \"aiva-čiy, Kent's aivam-čiy (DB 5.9) 'anything (at all)', literally aiva- 'one' + -čiy - the ☞I 2 cross-reference to \"\n  \"the *oi-no-/*ai- 'one' root is right. The gloss 'if' on ka 1 / kam 1 is loose: Kent glosses OP ka- 'who' and OP kā \"\n  \"as a generalising particle, while the conditional sense belongs to Middle Persian ka 'when; if' (MacKenzie) and to \"\n  \"Pokorny's *kʷom > Lat. quom/cum 'wenn, als', Goth. ƕan, Lith. ką 'wenn'. The real problem is 'kâi-gi : what, how?': \"\n  \"there is no such Old Persian word - it is not in Kent's lexicon or in the DB/DNb texts. It is Old Prussian kai-gi \"\n  \"'wie?', which stands in Pokorny p.646, the very page Nourai cites: 'lit. kaĩ, kaĩ-p, apr. kai-gi wie? (= abg. cě)'. \"\n  \"Nourai has read Pokorny's 'apr.' (altpreussisch) as 'ap.' (Old Persian); the -gi is the Baltic particle, cf. Lith. -gi, \"\n  \"OPr. -gi. The printed page (rendered at 500 dpi, copy saved as sources/refs/ocr/BOOK/297.png) reads 'kâi-gi' exactly \"\n  \"as the JSON has it, so the extraction is faithful and the error is the author's.\"),\n \"derivation_fa\": (\"چهار صورت از پنج صورت این جعبه درست‌اند و عیناً در واژه‌نامهٔ پارسی باستانِ کنت آمده‌اند: ka- ضمیر پرسشی-نامعین «که»، \"\n  \"kaš-čiy «هرکس» (بیستون ۱:۴۹ و ۵۳)، -čiy ادات تأکید/تعمیم (قس اوستایی -čiṯ، سنسکریت cid، لاتینی quid)، čiš-čiy «هر چیز» \"\n  \"(بیستون ۱:۵۸، برابر لاتینی quicquid)، و aivam-čiy «هیچ چیز» از aiva- «یک» + -čiy — ارجاع «I 2» به ریشهٔ «یک» درست است. \"\n  \"معنیِ «اگر» برای ka/kam دقیق نیست: این معنی از آنِ فارسی میانهٔ ka «چون، اگر» و *kʷom هندواروپایی (لاتینی cum) است. \"\n  \"امّا «kâi-gi» اصلاً واژهٔ پارسی باستان نیست؛ این صورتِ پروسی باستان (Old Prussian) kai-gi «چگونه؟» است که در همان صفحهٔ ۶۴۶ \"\n  \"پوکورنی که نورایی ارجاع داده آمده است: «lit. kaĩ, kaĩ-p, apr. kai-gi wie?». نورایی اختصار apr. (پروسی باستان) را ap. \"\n  \"(پارسی باستان) خوانده است؛ جزء -gi همان ادات بالتیکی است. تصویر صفحهٔ چاپی نشان می‌دهد که استخراج درست است و خطا از خودِ کتاب است. \"\n  \"پژوهش امروزی این مدخل را رد می‌کند.\"),\n \"sources\": [W_KWIS],\n \"ref_check\": [\n   {\"ref\": \"POK:644\", \"status\": \"partial\", \"note\": \"IEW 644 has 'apers. ka-[šciy], als Indef. mit -čiṯ' and IEW 647 'apers. čiy sogar, jedenfalls; apers. čiš-čiy'; but the same entry's p.646 form 'apr. kai-gi wie?' is Old Prussian, not Old Persian - the source of Nourai's phantom OP 'kâi-gi'.\"},\n   {\"ref\": \"SNS:86\", \"status\": \"partial\", \"note\": \"Tavoosi's Shayast ne Shayast glossary, SNS_pages.txt leaf 58 carries the running page numeral ۸۵/۸۶ and leaf 59 has the entry 'hēč/ēč'; the glossary also has 'kas, kasica (AiW 190)' and 'kas-iz' (leaf 30-31). It is a Pahlavi glossary, so it can corroborate hēč/kas but not the Old Persian forms; OCR too poor to read the etymological note in full.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.vv. ka-, či-, -čiy, adakaiy\", \"stance\": \"partial\", \"note\": \"'ka- interrog.-indef. pron. who: Av. Skt. ka-, Gk. πο-, Lat. quo-, NEng. wha-t, pIE *kʷo-. With encl. -čiy, any: kaš-čiy'; 'čiš-čiy asn. anything DB 1.58, Lat. quicquid, pIE *kʷid-kʷid'; 'aivam-čiy DB 5.9'. Kent has NO entry kaigi/kāigi, and glosses ka- 'who', not 'if'.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 646\", \"stance\": \"contradicts\", \"note\": \"'lit. kaĩ, kaĩ-p, apr. kai-gi wie? (= abg. cě)' - the form is Old Prussian; there is no Old Persian kai-gi.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 851 (p.198) and no. 1114 (p.249)\", \"stance\": \"supports\", \"note\": \"'851. kes jemand ... ap. kaš-čiy irgend wer, jemand; aw. kas-čiṯ jemand'; '1114. heč jemand, jemals, mit Negation niemand, nichts ... ap. *aiva + čiy (Salemann); phlv. ēč bezw. hēč'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 line 3110\", \"stance\": \"partial\", \"note\": \"'ka [AMT < A ʾmty | M kʾ, N ki] when; if, since' - the conditional value Nourai assigns to OP 'ka 1' is in fact the Middle Persian one.\"}\n ]\n})\n\nnodes.append({\n \"id\": 6,\n \"lang\": \"Persian\",\n \"words\": \"kas «کس ۱»; hîč «هیچ»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Both words are Old Persian indefinites in -čiy that fossilised. کس 'person, somebody' < MP kas (MacKenzie: \"\n  \"'kas [AYŠ < A ʾyš | M ks] person, somebody', with kas-iz 'anybody, (with a negative) nobody') < OP kaš-čiy 'anyone', \"\n  \"Av. kas-čiṯ; Horn no.851 states it exactly so ('ap. kaš-čiy irgend wer, jemand; aw. kas-čiṯ jemand; päz. kas, kasī-ča'), \"\n  \"and Mo'in's own footnote in Borhan p.1641 reads 'پارسی باستان kaš[ciy (کسی؛ هر کس)، اوستا kas[cit'. The final -š-čiy \"\n  \"was reduced already in Middle Persian to -s. هیچ 'nothing, none' is OP *aiva-čiy 'anything at all' (Kent's aivam-čiy, \"\n  \"DB 5.9), literally 'one-ever', > MP ēč / hēč (MacKenzie's -iz/-č enclitic; Pāzand hēč, hēčī) > NP هیچ; the prothetic \"\n  \"h- is New Persian (the older Shahnameh spelling is اچ ēč, Horn no.1114). The negative value ('nothing') is a \"\n  \"polarity development: the word means 'any' and takes its negative sense from the negated clause, exactly as French \"\n  \"personne or English 'any' in 'not any'. Wiktionary's entry is incomplete here and even guesses at a hi- < *né; \"\n  \"Horn's *aiva-čiy (after Salemann) is the standard account and is what Nourai draws.\"),\n \"derivation_fa\": (\"هر دو واژه صورت‌های نامعینِ پارسی باستان با پی‌بستِ -čiy‌اند که سنگ‌واره شده‌اند. «کس» از فارسی میانهٔ kas و آن از \"\n  \"پارسی باستان kaš-čiy «هرکس» و اوستایی kas-čiṯ است؛ هرن (ش ۸۵۱) و نیز حاشیهٔ خودِ معین بر برهان قاطع (ص ۱۶۴۱) همین را می‌گویند: \"\n  \"«پارسی باستان kaš[ciy (کسی؛ هرکس)، اوستا kas[cit». خوشهٔ -šč در فارسی میانه به -s ساده شده است. «هیچ» از *aiva-čiy پارسی باستان \"\n  \"(کنت: aivam-čiy، بیستون ۵:۹) به معنیِ «یک‌چیزِ هرچه‌باشد» است که به ēč/hēč فارسی میانه و «هیچ» فارسی نو رسیده؛ «ه» آغازین \"\n  \"افزودهٔ فارسی نو است و در شاهنامه هنوز «اچ» می‌آید (هرن ش ۱۱۱۴). معنیِ منفیِ امروزیِ آن حاصل کاربرد در جملهٔ منفی است \"\n  \"(تحول قطبیت)، نه معنیِ اصلی. ویکی‌واژه در این مدخل ناقص است؛ روایت هرن/سالمان معیار است و نورایی همان را آورده. ادعای نورایی درست است.\"),\n \"sources\": [W_HIC],\n \"ref_check\": [\n   {\"ref\": \"BQT:1641\", \"status\": \"supports\", \"note\": \"BQT_v3_pages.txt pdf page 434 = printed 1641: Mo'in's footnote to کس reads 'پارسی باستان kaš[ciy (کسی؛ هر کس)، اوستا kas[cit ... پازند kas, kasi[ča، هندی باستان kás، کردی kes, kesek، افغانی و بلوچی kas' - precisely Nourai's arrow.\"},\n   {\"ref\": \"SNS:86\", \"status\": \"partial\", \"note\": \"SNS_pages.txt leaf 58 bears the numeral ۸۵/۸۶ and the adjacent leaf 59 has the glossary entry 'hēč/ēč'; leaves 30-31 have 'kasica, kas (AiW 190)' and 'kas-iz'. So Tavoosi's glossary does contain both words, but the Persian OCR is too poor to quote the etymological comment verbatim, and the exact printed page of the hēč entry may be 87-88 rather than 86.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"nos. 851 and 1114\", \"stance\": \"supports\", \"note\": \"'851. kes jemand ... ap. kaš[čiy irgend wer, jemand; aw. kas[čiṯ jemand; päz. kas, kasī[ča'; '1114. heč jemand, jemals, mit Negation niemand, nichts; eč (Šāhn. I,4 v.59) ... ap. *aiva + čiy (Salemann, Mél. asiat. IX,241); phlv. ēč bezw. hēč (päz. hēč, hēčī)'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 lines 3250-3251, 3272\", \"stance\": \"supports\", \"note\": \"'kas [AYŠ < A ʾyš | M ks, N -] person, somebody' with '--iz [-c] anybody, (with a negative) nobody'; 'P kēč [kyc] person, somebody'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann col. 14224 s.v. quos\", \"stance\": \"supports\", \"note\": \"'quos, retrospective prn. who ... Skt. kas; Av. kō; OPer. ka; Per. kas (in hīč kas nobody); Oss. Dig. ka; Arm. o; Go. hwas'.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Lexicon s.v. -čiy\", \"stance\": \"supports\", \"note\": \"'kaš-čiy nsm. DB 1.49, 53; DSe 37'; 'aivam-čiy (§521) DB 5.9'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 7,\n \"lang\": \"Germanic\",\n \"words\": \"hwa, hwi; hwatharaz\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Proto-Germanic *hwa-/*hwi- (nom. *hwaz) < PIE *kʷo-/*kʷi- by Grimm's law: PIE *kʷ > PGmc *hw (Goth. ƕ), so \"\n  \"*kʷos > Goth. ƕas, OE hwā, ON hverr, OHG hwer. *hwatharaz is the *-tero- comparative *kʷo-tero- 'which of two' > \"\n  \"Goth. ƕaþar, OE hwæþer 'whether', ON hvárr, OHG hwedar (whence German weder); the same formation as Skt. katará-, \"\n  \"Av. katāra- in box #1 and Gk. πότερος. Watkins sets it out in exactly these terms. The citation POK:464 is wrong: \"\n  \"IEW p.464 (POK_02.txt leaf ~120) is the entry gʷem- 'gehen, kommen'; the Germanic material of this root is on \"\n  \"pp.645-646. The printed page really does read 'POK:464' (500 dpi render checked), so this is the author's typo for 644, \"\n  \"not an extraction error.\"),\n \"derivation_fa\": (\"ژرمنی آغازین *hwa-/*hwi- (نهادی *hwaz) از *kʷo-/*kʷi- هندواروپایی است؛ بر پایهٔ قانون گریم، *kʷ هندواروپایی در ژرمنی \"\n  \"به *hw بدل شده است (گوتی ƕas، انگلیسی باستان hwā، آلمانی باستان hwer). *hwatharaz همان ساخت تفضیلی *kʷo-tero- «کدام از دو» است \"\n  \"که در گوتی ƕaþar و انگلیسی باستان hwæþer «کدام‌یک از دو» بازتاب یافته و با سنسکریت katará-، اوستایی katāra- و یونانی πότερος هم‌ریشه است. \"\n  \"ارجاع POK:464 نادرست است: صفحهٔ ۴۶۴ پوکورنی مدخل *gʷem- «رفتن، آمدن» است و مواد ژرمنی این ریشه در صص ۶۴۵–۶۴۶ آمده؛ \"\n  \"تصویر صفحهٔ چاپی نشان می‌دهد که خودِ کتاب «۴۶۴» چاپ کرده، یعنی خطای چاپیِ نویسنده به‌جای ۶۴۴ است، نه خطای خوانش اسکن.\"),\n \"sources\": [E_WHO, W_KWIS],\n \"ref_check\": [\n   {\"ref\": \"POK:464\", \"status\": \"not_found\", \"note\": \"read POK_02.txt at printed p.464 (leaf ~120, line 1800): the page carries '2. gʷem-' 'gehen, kommen' and Celtic bāid/bás - nothing Germanic and nothing pronominal. The Germanic forms of this root (got. ƕas, ƕaþar, ags. hwā, hwæþer) are on IEW 645-646. Clearly a misprint for 644; the printed book has '464' (page image checked).\"},\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. kwo-: '1. Germanic *hwa-, hwi- in: a. personal pronouns *hwas, *hwasa, *hwam in Old English hwā ...; 2. Germanic *hwatharaz in: a. Old English hwæther ... WHETHER; NEITHER; b. Germanic phrase *aiwo gihwatharaz ... EITHER.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 645-646\", \"stance\": \"supports\", \"note\": \"'got. ƕas (*kʷo-s) wer? ... ags. hwā wer; neutr. got. ƕa (*kʷo-d), ahd. hwaz, an. hvat, ags. hwæt was'; and 'got. ƕaþar, aisl. hvárr, ags. hwæþer wer von beiden (ahd. hwedar, nhd. noch in weder)'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. quality, quantum, quid\", \"stance\": \"supports\", \"note\": \"'Goth. ƕas, OE. hwā, who' repeatedly cited as the Germanic cognate of the pronominal base *quo-.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kwo-\", \"stance\": \"supports\", \"note\": \"quoted above; Nourai's Germanic box is a verbatim condensation of Watkins' items 1 and 2.\"}\n ]\n})\n\nnodes.append({\n \"id\": 8,\n \"lang\": \"English\",\n \"words\": \"who, what, why, which, how, where, when, either, neither\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"All nine English words are West Germanic *hw- forms of the same stem, and Watkins lists precisely this set \"\n  \"under kwo-: OE hwā > WHO; OE hwæt > WHAT; OE hwȳ (instr. *hwī) > WHY; OE hwilc/hwelc = *hwa-līk- 'what-like' > WHICH; \"\n  \"OE hū (< *hwō, the ablative adverb, = Lat. quō, Gk. πῶ) > HOW; OE hwǣr (*hwar-) > WHERE; OE hwenne/hwanne (*hwan-) > \"\n  \"WHEN; OE ǣghwæþer/ǣther, from *aiwō gi-hwatharaz 'ever each of two' > EITHER; and NEITHER = ne + either, built on \"\n  \"*hwatharaz > WHETHER. Initial OE hw- was written wh- from Middle English on, and the /hw/ > /w/ merger in most modern \"\n  \"accents is post-medieval. Etymonline gives the same chain for who and how and which.\"),\n \"derivation_fa\": (\"هر نُه واژهٔ انگلیسی صورت‌های *hw- ژرمنی غربی از همین ستاک‌اند و واتکینز دقیقاً همین فهرست را ذیل kwo- آورده است: \"\n  \"انگلیسی باستان hwā ← who؛ hwæt ← what؛ hwȳ (ابزاری *hwī) ← why؛ hwilc = *hwa-līk- «چه‌گونه، چه‌سان» ← which؛ hū (از *hwō، \"\n  \"همان قید ازی، برابر لاتینی quō و یونانی πῶ) ← how؛ hwǣr ← where؛ hwenne ← when؛ ǣghwæþer از *aiwō gi-hwatharaz «همیشه هر یک از دو» ← either؛ \"\n  \"و neither از ne + either. نگارش hw- انگلیسی باستان از انگلیسی میانه به wh- بدل شد. ادعای نورایی درست است.\"),\n \"sources\": [E_WHO],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book; checked against Watkins/AHD and Etymonline instead.\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kwo- items 1a-h and 2a-b\", \"stance\": \"supports\", \"note\": \"'WHO, WHOSE, WHOM ... WHAT ... WHY ... WHICH ... HOW ... WHEN ... WHERE ... WHETHER; NEITHER ... EITHER' - the identical list.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. quid, quod, quorum (cross-refs to who, what, how)\", \"stance\": \"supports\", \"note\": \"'L. quid, what, something, neut. of quis, who, cogn. with OE. hwā, who, hwæt, what. See who, what.'\"},\n   {\"src\": \"POK\", \"where\": \"IEW 645-648\", \"stance\": \"supports\", \"note\": \"'ags. hwǣr, ahd. as. hwār wo'; 'got. -hun ...; ags. hū wie; engl. how, afries. hū'; 'got. ƕi-leiks, ags. hwilc wie beschaffen'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 9,\n \"lang\": \"Latin\",\n \"words\": \"qu-, quantis, qualis\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": (\"The Latin box is right in substance but one form is misprinted. Latin qu- is the regular outcome of PIE *kʷ \"\n  \"(quis, quid, quī, quae, quod, quam, quot, quom); quālis 'of what kind' is *kʷā-li- (Pokorny 646 lists it beside Gk. \"\n  \"πηλίκος and Lith. kõl), and it is the base of quālitās, Cicero's calque on Greek ποιότης. The second word should be \"\n  \"quantus 'how great, how much' (< *quam-to-, from quam), the base of quantitās, Cicero's calque on ποσότης; 'quantis' \"\n  \"is only the dat./abl. pl. of quantus and is not the form any source cites here. Watkins gives '10. Latin quantus, how \"\n  \"great: QUANTITY. 11. Latin quālis, of what kind: QUALITY', which is evidently what Nourai was condensing. The 500 dpi \"\n  \"render of the printed page shows 'qu-, quantis, qualis', so the extraction is faithful and the misprint is the book's.\"),\n \"derivation_fa\": (\"محتوای این جعبه درست است ولی یک صورت غلط چاپ شده. qu- لاتینی بازتاب منظم *kʷ هندواروپایی است (quis, quid, quī, quod, quam, quot). \"\n  \"quālis «از چه گونه» از *kʷā-li- است (پوکورنی ص ۶۴۶ آن را در کنار یونانی πηλίκος می‌آورد) و پایهٔ quālitās، گرته‌برداریِ سیسرون از ποιότης یونانی. \"\n  \"امّا صورت درست دوم quantus «چه‌قدر، چه اندازه» (از *quam-to-) است که پایهٔ quantitās و گرتهٔ ποσότης است؛ «quantis» تنها صورت برایی/ازیِ جمعِ quantus است \"\n  \"و در هیچ منبعی چنین سرواژه‌ای نیست. واتکینز می‌نویسد: «Latin quantus, how great: QUANTITY؛ Latin quālis, of what kind: QUALITY». \"\n  \"تصویر ۵۰۰ نقطه‌ایِ صفحه نشان می‌دهد که خودِ کتاب «quantis» چاپ کرده است؛ پس خطای چاپی کتاب است، نه خطای خوانش اسکن.\"),\n \"error_in\": \"book\",\n \"book_prints\": \"quantis\",\n \"correct_form\": \"quantus\",\n \"sources\": [E_WHO],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. kwo-: '3. Latin quī, who ... 10. Latin quantus, how great: QUANTITY. 11. Latin quālis, of what kind: QUALITY. [Pok. kʷo- 644.]' - the source has quantus, not quantis.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. quantum, quality\", \"stance\": \"partial\", \"note\": \"'quantum, n. - L., neut. of quantus, how great, how much, how many; ... for *quam-to, fr. quam'; 'quality ... fr. L. quālitātem ... fr. quālis ... which derives from the pronominal base *quo-'. Both lemmatise quantus.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 645-646\", \"stance\": \"supports\", \"note\": \"'lat. quantus, umbr. panta quanta (S. 644)'; 'gr. πηλίκος wie groß?, lat. quālis wie beschaffen, lit. kõl wie lange'.\"},\n   {\"src\": \"LEW\", \"where\": \"Walde-Hofmann s.v. quantus/quālis\", \"stance\": \"silent\", \"note\": \"grep of LEW_1910.txt for 'quantis' returns nothing; the lemma there is quantus.\"}\n ]\n})\n\nnodes.append({\n \"id\": 10,\n \"lang\": \"English\",\n \"words\": \"quantity, quality\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Both are learned Latinisms that reached English through French. L. quantitās (acc. quantitātem), coined by \"\n  \"Cicero from quantus as a loan-translation of Gk. ποσότης, > Old French quantite > Middle English quantite > quantity; \"\n  \"L. quālitās, likewise Cicero's calque on Gk. ποιότης from quālis, > OF qualite > ME qualite > quality. Klein gives \"\n  \"exactly this chain for both words, and both are listed under kwo- by Watkins (QUANTITY, QUALITY). The English words \"\n  \"therefore descend from the root only through the Latin abstract nouns, as the chart draws it.\"),\n \"derivation_fa\": (\"هر دو وام‌واژه‌های عالمانهٔ لاتینی‌اند که از راه فرانسه به انگلیسی رسیده‌اند: لاتینی quantitās که سیسرون آن را از quantus \"\n  \"به‌عنوان گرته‌برداریِ ποσότης یونانی ساخت ← فرانسهٔ باستان quantite ← انگلیسی میانه quantite ← quantity؛ و لاتینی quālitās، باز گرتهٔ سیسرون از \"\n  \"ποιότης، از quālis ← qualite ← quality. کلاین همین زنجیره را برای هر دو می‌آورد و واتکینز نیز هر دو را ذیل kwo- فهرست کرده است. ادعای نورایی درست است.\"),\n \"sources\": [E_WHO],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference printed on this node; checked against Klein and Watkins.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. quantity, quality\", \"stance\": \"supports\", \"note\": \"'quantity, n. - ME. quantite, fr. OF. quantite (F. quantité), fr. L. quantitatem, acc. of quantitas ... fr. quantus ... L. quantitas was formed fr. quantus as loan translation of Gk. ποσότης'; 'quality, n. - ME. qualite, fr. OF. qualite, fr. L. qualitatem ... fr. qualis ... which derives from the pronominal base *quo-'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kwo- items 10-11\", \"stance\": \"supports\", \"note\": \"'10. Latin quantus, how great: QUANTITY. 11. Latin quālis, of what kind: QUALITY.'\"}\n ]\n})\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Kwo, Kwi 1\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *kʷo-/*kʷe- (fem. *kʷā), collateral stems *kʷi-/*kʷei- and adverbial *kʷu- - the interrogative-indefinite pronominal stem, in several branches also relative\",\n  \"note\": (\"Root, language label and gloss are all correct and the gloss is almost word-for-word Watkins': 'kwo-. Also ki-. \"\n   \"Stem of relative and interrogative pronouns.' Pokorny's entry (IEW 644-648) heads it 'kʷo-, kʷe-, fem. kʷā; kʷei- \"\n   \"(vermutlich einst nur im Nom. Akk. Sg.), kʷu- (nur im Adv.); die betonten Formen sind Interrogativa, die unbetonten \"\n   \"Indefinita; einzelsprachlich z.T. Relativum geworden' - so Nourai's twin root name 'Kwo, Kwi' matches the standard \"\n   \"reconstruction. Modern handbooks (Wiktionary after Beekes/Kloekhorst) treat *kʷis/*kʷid as the core interrogative-\"\n   \"indefinite paradigm and *kʷos as an originally separate o-stem adjective conflated with it in most branches; that is a \"\n   \"refinement of, not a break with, the chart. Cross-cutting findings on this page: (a) the Germanic box cites POK:464, \"\n   \"which is the entry gʷem- 'to go' - a misprint for 644 in the printed book; (b) the Old Persian box lists 'kâi-gi', \"\n   \"which is Old Prussian kai-gi 'how?' from Pokorny 646 misread as Old Persian; (c) the Latin box prints 'quantis' for \"\n   \"quantus; (d) BQT:1748 (the کو/کی page) and BQT:672 (the چه/چون/چیز block) each appear on both a k- and a č- box, so one \"\n   \"of the two placements in each pair is a copied ref block; (e) Persian چیز in fact continues the Old Persian čiš-čiy of \"\n   \"box #5 rather than the bare Avestan stem of box #3, per Mo'in's own footnote.\"),\n  \"note_fa\": (\"نام ریشه، برچسب زبان و معنی هر سه درست‌اند و معنیِ داده‌شده تقریباً واژه‌به‌واژه از واتکینز است: «kwo-. Also ki-. \"\n   \"Stem of relative and interrogative pronouns». پوکورنی (صص ۶۴۴–۶۴۸) مدخل را چنین می‌آغازد: «kʷo-, kʷe-, مؤنث kʷā؛ kʷei-؛ kʷu- \"\n   \"(تنها در قید)؛ صورت‌های تکیه‌دار پرسشی و بی‌تکیه نامعین‌اند و در برخی زبان‌ها موصولی شده‌اند». پس نامِ دوگانهٔ «Kwo, Kwi» با بازسازیِ \"\n   \"معیار می‌خواند. پژوهش امروزی *kʷis/*kʷid را هستهٔ صرفِ پرسشی-نامعین می‌داند و *kʷos را صفتی o-ستاک که در بیشتر شاخه‌ها با آن درآمیخته است؛ \"\n   \"این تنها ظرافتی بر همان تصویر است، نه ردّ آن. نکته‌های فراگیر این صفحه: ارجاع POK:464 در جعبهٔ ژرمنی خطای چاپیِ ۶۴۴ است؛ \"\n   \"«kâi-gi» در جعبهٔ پارسی باستان در حقیقت پروسی باستان kai-gi «چگونه؟» است؛ «quantis» لاتینی باید quantus باشد؛ \"\n   \"و «چیز» بنا بر حاشیهٔ خودِ معین دنبالهٔ čiš-čiy پارسی باستان است، نه ستاک سادهٔ اوستایی.\"),\n  \"sources\": [W_KWIS, W_KWOS, E_WHO],\n  \"ref_check\": [\n    {\"ref\": \"POK:644\", \"status\": \"supports\", \"note\": \"IEW p.644 (POK_02.txt, leaf ~300): the entry begins there - 'kʷo-, kʷe-, fem. kʷā; kʷei- ...; kʷu- (nur im Adv.); die betonten Formen sind Interrogativa, die unbetonten Indefinita; einzelsprachlich z.T. Relativum geworden. 1. Stamm kʷo-, kʷe-, fem. kʷā-; Gen. kʷeso, Instr. kʷi, Zeitadverb kʷo-tō.'\"},\n    {\"ref\": \"POK:646\", \"status\": \"supports\", \"note\": \"IEW p.646 is section 'B. Ableitungen, die sich durch mehrere Sprachen verfolgen lassen: kʷo-tero- wer von zweien?; kʷā-li- wie?; kʷo-ti-, kʷe-ti- wie viele?' with ai. katamá-, av. katāra-, av. kada, gr. πηλίκος, lat. quālis, av. čaiti - i.e. precisely the derivatives Nourai's boxes list.\"},\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985, AHD_watkins1985.txt line 655: 'kwo-. Also ki-. Stem of relative and interrogative pronouns. ... [Pok. kʷo- 644.]' - Nourai's root name and gloss are taken from here.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW I 644-648\", \"stance\": \"supports\", \"note\": \"full entry, with all three stems kʷo-/kʷei-/kʷu- and the Avestan, Old Persian, Germanic and Latin material of this chart.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 514-523\", \"stance\": \"supports\", \"note\": \"running head at p.522 'q̯ᵘo-, q̯ᵘe-, q̯ᵘā; q̯ᵘi-; q̯ᵘu-'; this is the 'WP. I 514ff.' that Pokorny cites at the end of the entry.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kwo-\", \"stance\": \"supports\", \"note\": \"same root, same gloss, Pok. 644.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, cols. 13852 (qu-), 14115 (quo-dhen), 14224 (quos)\", \"stance\": \"supports\", \"note\": \"'quos, retrospective prn. who ... Skt. kas; Av. kō; OPer. ka; Per. kas (in hīč kas nobody); Go. hwas'; 'quo-dhen ... Av. kaδa how; Per. -kada, -keda'.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.vv. quality, quantum, quid, quod, quorum\", \"stance\": \"supports\", \"note\": \"'the pronominal base *quo-, whence also L. quis? who, quid? what, quī, quae, quod, Goth. ƕas, OE. hwā, who'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 1949\", \"stance\": \"silent\", \"note\": \"Buck has no chapter for the interrogative pronouns (grep for 'Interrogative' in SYN.txt returns only numeral notes), so no entry to compare.\"}\n  ],\n  \"nodes\": nodes\n}\n\nout = {\n  \"pdf_page\": 297,\n  \"book_page\": 267,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [entry]\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-297.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk297.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-297.json > /dev/null && echo \"valid json\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 297"
}
```


### [2026-09-06T22:47:38.827Z] TOOL RESULT

```
written
valid json
nodes verified: 10/10
node verdicts: {'confirmed': 7, 'plausible': 1, 'disputed': 1, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 7, 'partial': 8, 'not_found': 2, 'not_checked': 2}
books consulted: {'supports': 29, 'silent': 2, 'partial': 4, 'contradicts': 1} | by book: {'POK': 6, 'AHD': 5, 'HRN': 5, 'PHD': 4, 'KLN': 4, 'WLD': 2, 'BRT': 2, 'IEC': 2, 'BQT': 2, 'KNT': 2, 'ARY': 1, 'LEW': 1}
```


## [2026-09-06T22:47:44.612Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"quantis:\"; grep -c \"quantis\" LEW_1910.txt; echo \"quantus:\"; grep -c \"quantus\" LEW_1910.txt; grep -n \"quantus\" LEW_1910.txt | head -3"
}
```


### [2026-09-06T22:47:44.673Z] TOOL RESULT

```
quantis:
0
quantus:
0
```


## [2026-09-06T22:47:49.833Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"LAT quantus:\"; grep -n \"quantus\" LAT.txt | head -3; echo \"LAT qualis:\"; grep -n \"qualis\" LAT.txt | head -3"
}
```


### [2026-09-06T22:47:49.898Z] TOOL RESULT

```
LAT quantus:
34729:libet, quantus-, qualis-, uter-, quam-, quot-, quo-, qua-, ut-libet,
47889:cf. Pl., Anp.106, quantusque amator [ Iuppiter ] sit, quod complacitumst
51456:apres autre radical dans v.sl .koliku "quantus". Les formations com¬
LAT qualis:
1706:aequalis, aequabilis, que la langue a diff6renci6s dans 1'emploi :
1707:i° aequalis (de aequus, comme socialis de socius): de meme taille, de
1711:Composta: coaequalis, inaequalis (6poq.imp.); inaequalitas (Varr.).
```


## [2026-09-06T22:47:51.966Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '51450,51470p' LAT.txt"
}
```


### [2026-09-06T22:47:52.012Z] TOOL RESULT

```
De qudlitds: iri. cailidecht.
De IA: quSliscumque "quel qu'il soit; quelconque"; qualis qualis :
de quelque nature que (Dig.), et qualiter qualiter', qualislibet (bas
latin); qualisnam (Apul.).
Pour la formation, cf,gr. TCqXCxoS (de 7 ictXLXoe) "de quel age, com¬
bien grand", lit.fedl, koliai "combien longtemps". Suffixe -Ii-, mais
apres autre radical dans v.sl .koliku "quantus". Les formations com¬
portant -a- tiennent une grande place en latin; cf.-drius, etc.
V. quis.
qualum ( qualus, quali- m. ), -i n. : panier d'osier tresse; sorte
de filtre en osier, etc. Ancien (Caton), technique. Joint a colum
par Vg., G.a,84i: tu spisso uimine qualos | colaque prelorum fumosis
deripe tectis. A qualum correspond le diminutif quasillus, quasillum
"petit panier; corbeille A laine", demeure en campidanien, M.L.Cy38.
De IA quasilldrius xocptvoxo uoc ( Gloss.), quasi l ISria: esclave filan-
diere.
L’s simple de quasillum s , explique si l'on suppose, avec M.Nieder-
mann, que qudlum repose sur *quas—lom et quasillum sur quassillum
( cf. mamma, mamilla), Qn rapproche v. sl. koSi "xocpovoc". Mot technique
auquel il serait risque de chercher une origine indo-europ 4 enne.
Emprunte comme asinus, casa, rosa , etc. (v. Stolz-Leumann, Lat.Grammfi ,
```


## [2026-09-06T22:48:04.125Z] TOOL CALL #80: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json\np='data/verification/page-297.json'\nd=json.load(open(p,encoding='utf-8'))\nn9=[n for n in d['entries'][0]['nodes'] if n['id']==9][0]\nfor c in n9['consulted']:\n    if c['src']=='LEW':\n        c['src']='LAT'\n        c['where']=\"Ernout-Meillet s.v. quālis (LAT.txt line 51450 ff.)\"\n        c['stance']='supports'\n        c['note']=(\"'De quālitās: irl. cailidecht ... Pour la formation, cf. gr. πηλίκος (de ποίκος?) \\\"de quel âge, combien grand\\\", \"\n                   \"lit. kõl, koliai \\\"combien longtemps\\\". Suffixe -li- ... V. quis.' Ernout-Meillet thus derives quālis (and quālitās) \"\n                   \"from the quis/quo- pronominal stem, as the chart does. A grep of LEW_1910.txt for both 'quantus' and 'quantis' returns \"\n                   \"nothing (that local scan does not reach the q- fascicle), and no Latin dictionary on disk lemmatises 'quantis'.\")\njson.dump(d, open(p,'w',encoding='utf-8'), ensure_ascii=False, indent=2)\nopen(p,'a',encoding='utf-8').write('\\n')\nprint('ok')\nPYEOF\npython3 -m json.tool data/verification/page-297.json > /dev/null && python3 tools/verify_check.py 297"
}
```


### [2026-09-06T22:48:05.992Z] TOOL RESULT

```
ok
nodes verified: 10/10
node verdicts: {'confirmed': 7, 'plausible': 1, 'disputed': 1, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 7, 'partial': 8, 'not_found': 2, 'not_checked': 2}
books consulted: {'supports': 30, 'silent': 1, 'partial': 4, 'contradicts': 1} | by book: {'POK': 6, 'AHD': 5, 'HRN': 5, 'PHD': 4, 'KLN': 4, 'WLD': 2, 'BRT': 2, 'IEC': 2, 'BQT': 2, 'KNT': 2, 'ARY': 1, 'LAT': 1}
```


## [2026-09-06T22:48:09.220Z] TOOL CALL #81: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | grep -i \"297\" | head -20; echo \"exit=$?\""
}
```


### [2026-09-06T22:48:14.056Z] TOOL RESULT

```
exit=0
```


## [2026-09-06T22:48:16.041Z] TOOL CALL #82: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | tail -20"
}
```


### [2026-09-06T22:48:18.632Z] TOOL RESULT

```
2746 cited URLs, 8 not yet archived
archived 8, failed 0
```


## [2026-09-06T22:48:35.869Z] AGENT

Page 297 (book p. 267) verified. Written to `/home/sfmqrb/git/rishe/data/verification/page-297.json`; `verify_check.py 297` reports **10/10 nodes, 0 PROBLEM lines**.

**Counts** — root: 1 confirmed. Nodes: 7 confirmed, 1 plausible, 1 disputed, 1 transcription_suspect. Ref checks: 7 supports / 8 partial / 2 not_found / 2 not_checked. Books consulted: POK, AHD(Watkins), HRN, PHD, KLN, WLD, BRT, IEC, BQT(Mo'in), KNT, LAT, ARY.

**Flagged items**
- **#5 Old Persian, `kâi-gi` — disputed.** No such Old Persian word (absent from Kent's lexicon). It is Old Prussian *kai-gi* "wie?", printed on Pokorny p. 646 — the very page Nourai cites; he read POK's `apr.` (altpreussisch) as `ap.` (Old Persian). Also, the gloss "if" on OP `ka 1 / kam 1` is really the Middle Persian value (MacKenzie: `ka` "when; if"). Rest of the box (čiy, čiš-čiy, kaš-čiy, aiva-čiy) is exactly Kent.
- **#9 Latin, `quantis` — transcription_suspect, error_in "book".** Should be `quantus` (Watkins: "10. Latin quantus, how great: QUANTITY"); `quantis` is only a dat./abl. pl. Page image confirms the book prints it.
- **#3 Avestan — plausible.** All forms check out in Pokorny/Bartholomae except `čeč : whether`, which is in no source; the 500 dpi render confirms the book really prints "čeč", so it is the author's form.

**Reference errors in the book (not extraction errors)**
- `POK:464` on the Germanic box: p. 464 of IEW is *gʷem-* "to go"; the Germanic material is on 645–646. Misprint for 644.
- `BQT:1748` and `BQT:672` each appear on both a k- box and a č- box; 1748 is the کو/کی page (supports the k- side only), 672 sits in the چه/چون/چیز block (supports the č- side only) — one placement in each pair is a copied ref block.

**Extraction errors for the owner: none.** The JSON matches the printed page in every particular (checked against a 500 dpi render; page image saved to `data/verification/sources/refs/ocr/BOOK/297.png`).

Substantive note carried in the entry: Persian چیز continues Old Persian *čiš-čiy* (Mo'in's own footnote, Borhan p. 674: «چیز - پهلوی čiš، پارسی باستان čišciy»), i.e. it belongs under box #5 rather than the bare Avestan stem of #3; and چون is the MP compound *čigōn* = čē + gōnag (Horn 450, Mo'in p. 669), so only its first element comes from this root. Six web sources archived via `fetch_source.py`.
