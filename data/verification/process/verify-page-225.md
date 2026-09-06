# Verification process log — verify-page-225


## [2026-09-06T15:18:44.464Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 225 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-225.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-225.json. Write /home/sfmqrb/git/rishe/data/verification/page-225.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 225` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:18:46.017Z] AGENT

I'll start by reading the instructions file.


## [2026-09-06T15:18:46.728Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:18:46.745Z] TOOL RESULT

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


## [2026-09-06T15:18:46.997Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-225.txt"
}
```


### [2026-09-06T15:18:47.020Z] TOOL RESULT

```
1	=== PDF page 225 (book page 195) ===
2	--- entry 0 ---
3	ROOT [Indo-European] I 2, Io, E : pronominal stem  (refs POK:281)  PART 2
4	#1 (parent #0) [Indo-European] refs=POK:73,75,281,286 | Au 3, Auo, Oi-no : one, this one ; Uě, Uo : or
5	  #2 (parent #1) [Avestan / Old Persian] refs=POK:73,75,286; BQT:2417; KNT:164 | ava 2, aiva, aěva, aeva, aivaka : one ; aeva-data, aeva-dasa : eleven ☞Dekm ; aiva-čiy : nothing ☞Kwo ; va, vâ : or
6	    #3 (parent #2) [Pahlavi] refs=BQT; SNS:91; GPL:41 | ěvak, yak : one ; yâcdah : eleven ; hěč : nothing ; ayâb, ayâ, ayâo : or
7	      #4 (parent #3) [Persian] refs=BQT:2417,2446; SNS:86,91 | yak, yek «یک» : one ; yâzdah «یازده» : eleven ; hîč «هیچ» : nothing, no ; yâ «یا» : or
8	  #5 (parent #1) [Avestan / Old Persian] refs=POK:74 | uta, utâ, uiti : and
9	    #6 (parent #5) [Sogdian] refs=SOD:72 | `ty : and
10	    #7 (parent #5) [Pahlavi] refs=SNS:256 | ud : and
11	      #8 (parent #7) [Persian] refs=BQT:2242; SNS:256; TZF:20; MON:4921 | o, va «وُ ، وَ» : and | NOTE: The Arabic "va" pronunciation has influenced the Persian pronunciation
12	  #9 (parent #1) [Old Persian / Sanskrit] refs=POK:75,286; BQT:199; TZF:13; SOD:85,220 | aina, ěna, aita, aěta : this one, this ; ima, imam : this
13	    #10 (parent #9) [Sogdian] refs=SOD:85,220 | `yd : this ; mw : this
14	    #11 (parent #9) [Pahlavi] refs=MON:345,421 | ěn : this ; im : this
15	      #12 (parent #11) [Persian] refs=MON; TZF:13 | în «این» : this ; em «اِم (امروز، امشب، امسال)» : this
16	  #13 (parent #1) [Germanic] refs=AHD | ainaz, ainigaz : one
17	    #14 (parent #13) [English] refs=None | one, an, none, eleven, alone, any
18	  #15 (parent #1) [Latin] refs=AHD | ŭnus : one ; ne-ŭllus : not any, null ☞Ne 1
19	    #16 (parent #15) [English] refs=None | union, onion, ounce, inch, unique, unite, unit, universe ; null
20	--- entry 1 ---
21	ROOT Iâ 1 -> redirect to Ei
22	--- entry 2 ---
23	ROOT Iâ 2 -> redirect to Yâ
24	--- entry 3 ---
25	ROOT Iag -> redirect to Yag
26	--- entry 4 ---
27	ROOT Iaro -> redirect to Ei
28	
```


## [2026-09-06T15:18:50.024Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-225.json",
 "description": "Read source JSON for page 225"
}
```


### [2026-09-06T15:18:50.061Z] TOOL RESULT

```
{
  "pdf_page": 225,
  "book_page": 195,
  "entries": [
    {
      "root": {
        "name": "I 2, Io, E",
        "lang": "Indo-European",
        "refs": "POK:281",
        "gloss": "pronominal stem"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "POK:73,75,281,286",
          "words": [
            {"translit": "Au 3, Auo, Oi-no", "gloss": "one, this one", "script": null},
            {"translit": "Uě, Uo", "gloss": "or", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan / Old Persian",
          "refs": "POK:73,75,286; BQT:2417; KNT:164",
          "words": [
            {"translit": "ava 2, aiva, aěva, aeva, aivaka", "gloss": "one", "script": null},
            {"translit": "aeva-data, aeva-dasa", "gloss": "eleven", "script": null, "see": ["Dekm"]},
            {"translit": "aiva-čiy", "gloss": "nothing", "script": null, "see": ["Kwo"]},
            {"translit": "va, vâ", "gloss": "or", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Pahlavi",
          "refs": "BQT; SNS:91; GPL:41",
          "words": [
            {"translit": "ěvak, yak", "gloss": "one", "script": null},
            {"translit": "yâcdah", "gloss": "eleven", "script": null},
            {"translit": "hěč", "gloss": "nothing", "script": null},
            {"translit": "ayâb, ayâ, ayâo", "gloss": "or", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:2417,2446; SNS:86,91",
          "words": [
            {"translit": "yak, yek", "gloss": "one", "script": "یک"},
            {"translit": "yâzdah", "gloss": "eleven", "script": "یازده"},
            {"translit": "hîč", "gloss": "nothing, no", "script": "هیچ"},
            {"translit": "yâ", "gloss": "or", "script": "یا"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Avestan / Old Persian",
          "refs": "POK:74",
          "words": [
            {"translit": "uta, utâ, uiti", "gloss": "and", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Sogdian",
          "refs": "SOD:72",
          "words": [
            {"translit": "`ty", "gloss": "and", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "Pahlavi",
          "refs": "SNS:256",
          "words": [
            {"translit": "ud", "gloss": "and", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "BQT:2242; SNS:256; TZF:20; MON:4921",
          "words": [
            {"translit": "o, va", "gloss": "and", "script": "وُ ، وَ"}
          ],
          "script_extra": null,
          "note": "The Arabic \"va\" pronunciation has influenced the Persian pronunciation",
          "quote": {"text": "من و اسب و شبدیز و شمشیر تیز - نگیرم فریب و ندارم گریز", "poet": "Ferdowsî"}
        },
        {
          "id": 9,
          "parent": 1,
          "lang": "Old Persian / Sanskrit",
          "refs": "POK:75,286; BQT:199; TZF:13; SOD:85,220",
          "words": [
            {"translit": "aina, ěna, aita, aěta", "gloss": "this one, this", "script": null},
            {"translit": "ima, imam", "gloss": "this", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Sogdian",
          "refs": "SOD:85,220",
          "words": [
            {"translit": "`yd", "gloss": "this", "script": null},
            {"translit": "mw", "gloss": "this", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 9,
          "lang": "Pahlavi",
          "refs": "MON:345,421",
          "words": [
            {"translit": "ěn", "gloss": "this", "script": null},
            {"translit": "im", "gloss": "this", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "MON; TZF:13",
          "words": [
            {"translit": "în", "gloss": "this", "script": "این"},
            {"translit": "em", "gloss": "this", "script": "اِم (امروز، امشب، امسال)"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 1,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "ainaz, ainigaz", "gloss": "one", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "one, an, none, eleven, alone, any", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 1,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "ŭnus", "gloss": "one", "script": null},
            {"translit": "ne-ŭllus", "gloss": "not any, null", "script": null, "see": ["Ne 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "union, onion, ounce, inch, unique, unite, unit, universe", "gloss": null, "script": null},
            {"translit": "null", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Iâ 1",
        "redirect": "Ei"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Iâ 2",
        "redirect": "Yâ"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Iag",
        "redirect": "Yag"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Iaro",
        "redirect": "Ei"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-06T15:18:52.178Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','KNT','SNS','GPL','SOD','TZF','MON','AHD','WLD','BRT','PHD','NYB','HRN','HUB','KLN','SKT','IEC','SYN','ARY','CHEUNG']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-06T15:18:53.952Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
GPL {"title": "J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911", "edition_found": "1911", "kind": "archive_djvu", "url": "https://archive.org/details/grammarofpersian0000plat", "identifier": "grammarofpersian0000plat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt", "page_offset": "leaf = printed + 12 (e.g. leaf 17 = p.5
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فار
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG null
```


## [2026-09-06T15:18:57.245Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,200p tools/verify_check.py"
}
```


### [2026-09-06T15:18:57.281Z] TOOL RESULT

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


## [2026-09-06T15:18:58.226Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-202.json'))\nprint(list(d.keys()))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'}, ensure_ascii=False, indent=1)[:2000])\nprint(json.dumps(e['nodes'][0], ensure_ascii=False, indent=1)[:2500])\n\""
}
```


### [2026-09-06T15:19:00.974Z] TOOL RESULT

```
['pdf_page', 'book_page', 'verified_by', 'verified_on', 'entries']
{
 "entry": 0,
 "root": "Gwa, Gwâ, Gwen 2",
 "verdict": "confirmed",
 "modern_form": "PIE *gʷem- 'to go, to come' (with the collateral root *gʷeh₂- / *gʷā- 'to step, go'); Pokorny IEW 463-465",
 "note": "Pokorny's entry, which begins on p.463 exactly as Nourai cites, is headed 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“', and it is deliberately a double entry (I. gʷā-, II. gʷem-), which is why Nourai's box carries two names, 'Gwa, Gwâ'. His third name 'Gwen 2' reflects the *gʷem- > *gʷen- variant Pokorny himself notes ('Unthematisch *(e)-gʷem-t (> *e-gʷen-t)', and Latin advenam / veniō with -n- for -m-); it is not a separate root in any modern handbook, so it is Nourai's own labelling convenience rather than an error of substance. Watkins/AHD 1985 heads the same material 'gʷā-. Also gʷem-. To go, come'; Cheung splits it into *gaH¹ (PIE *gʷeh₂-, Pok. 463 f.) and *gam¹ (PIE *gʷem-, Pok. 464 f.). The gloss 'to walk, to step, to come, to go' is an accurate rendering. Two words in the chart do not belong to this root: Avestan 'gâv' in node 6 (a misprint) and 'thamân' in node 12 (an unidentifiable form), and one Persian word, nîyâm (node 3), is derived by modern scholarship from a different root (*ni-dā-, not *ni-gam-). Everything else on the page is standard, well-attested Iranian etymology.",
 "note_fa": "جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۶۳ فرهنگ خود مدخل «gʷā-, gʷem-» را با معنای «رفتن، آمدن؛ به جهان آمدن، زاده شدن» آورده و همان‌جا نام‌های gʷm̥-ti-s و gʷem-tu-s «گام، رفتار» را می‌افزاید؛ پس هر دو صورت «Gwa/Gwâ» و «Gwem» از یک مدخل‌اند و برچسب «هندواروپایی» و معنای «راه رفتن، گام برداشتن، آمدن، رفتن» درست است. نام سوم «Gwen 2» گونهٔ *gʷen- است که خود پوکورنی (در *e-gʷen-t و در veniō لاتین) یاد کرده و در کتاب‌های امروزی ریشهٔ جداگانه‌ای به شمار نمی‌رود؛ این نام‌گذاری از خود نورایی است نه خطای علمی. واتکینز (پیوست AHD) نیز همین ماده را «gʷā-, also gʷem-: رفتن، آمدن» آورده و چونگ آن را به دو ریشهٔ *gaH¹ و 
{
 "id": 1,
 "lang": "Avestan / Old Persian",
 "words": "gam : to come, step; jam, jantu : to go",
 "verdict": "confirmed",
 "derivation": "Indo-Iranian inherits PIE *gʷem- as the root gam- (Skt. gam-, Av. gam-, OP gam-). In Avestan the root appears in two guises that Nourai lists side by side: (a) gam- proper, in the perfect and in nominal derivatives (gāman-, gata-), and (b) jam-, the regular Avestan outcome of the full-grade *gʷem- (PIE labiovelar *gʷ- > Indo-Iranian *ǰ before front vowel of the thematic/subjunctive stems: *gʷem-e-ti > Av. jamaiti 'goes'), beside the inchoative present jasaiti < *gʷm̥-sk̑e-ti. jantu- is the tu-stem *gʷem-tu- 'a going, coming' (= Skt. gántu-, Lat. adventus), which Pokorny prints on the same page. Old Persian has the root only in compounds (ā-gam-, ham-gam-, parā-gam-), and there too the reflexes with j- (ājamiyā 'may he come') alternate with the g- of the participles (paragmatā, hangmatā). Nourai's glosses 'to come, step' / 'to go' are correct.",
 "derivation_fa": "ریشهٔ هندواروپایی *gʷem- در هندوایرانی به‌صورت gam- بازمانده است (سنسکریت gam-، اوستایی gam-، پارسی باستان gam-). در اوستایی دو گونه در کنار هم دیده می‌شود که نورایی هر دو را آورده است: نخست gam- که در ستاک‌های اسمی و کامل می‌ماند (gāman-، gata-)، و دوم jam- که پیامد آوایی قانونمند *gʷ- در ایرانی است (واک‌گونهٔ لبی‌کامی هندواروپایی پیش از واکهٔ پیشین به ǰ بدل می‌شود: *gʷem-e-ti > اوستایی jamaiti «می‌رود»)؛ ستاک حال آغازی نیز jasaiti < *gʷm̥-sk̑e-ti است. jantu- همان ستاک tu-دار *gʷem-tu- «رفت، آمد» است (هم‌ریشه با gántu- سنسکریت و adventus لاتین) که پوکورنی در همان صفحهٔ ۴۶۵ آورده. در پارسی باستان این ریشه تنها با پیشوند به‌کار رفته (ā-gam-، ham-gam-، parā-gam-). ادعای نورایی در این گره درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷem-",
  "https://en.wiktionary.org/wiki/آمدن"
 ],
 "ref_check": [
  {
   "ref": "POK:463",
   "status": "supports",
   "note": "POK_02.txt p.464-465 (the continuation of the entry that begins on 463): 'thematisch: hochstufig ai. gámati, av. jamaiti „geht“', 'sk̑o-Präsens *gʷm̥-sk̑ō: ai. gácchati, av. jasaiti „er geht“', and 'nach Schwyzer … könnte das n auch von Formen wie av. jantu (*gʷem-tu-) … bezogen sein'. All three of Nourai's forms are there."
  },
  {
   "ref": "KLN:318",
   "status": "supports",
   "note": "KLN_1966.txt line 8320, s.v. 'come' (page number 318 printed at the foot of the block): 'fr. I.-E. base *gʷem-, “to go; to come”, whence also OI. gámati, gacchati, “he go
```


## [2026-09-06T15:19:15.620Z] TOOL CALL #7: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -80; echo ---; sed -n 1,120p /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T15:19:15.674Z] TOOL RESULT

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
---
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
```


## [2026-09-06T15:19:21.108Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"== $f\"; wc -c $f; grep -n -m3 -E '^\\s*(73|281|286)\\s*$' $f | head -5; done"
}
```


## [2026-09-06T15:19:21.812Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -m20 'oi-no' POK_full.txt | head -20; echo ===; grep -n -m10 'oinos' POK_full.txt | head"
}
```


### [2026-09-06T15:19:23.086Z] TOOL RESULT

```
== POK_01.txt
981836 POK_01.txt
977:73
4023:281
4095:286
== POK_02.txt
1137861 POK_02.txt
== POK_03.txt
1170809 POK_03.txt
5649:73
== POK_full.txt
3971883 POK_full.txt
```


### [2026-09-06T15:19:23.137Z] TOOL RESULT

```
Exit code 1
51593:Root / lemma: Roi-no- 
63378:Root / lemma: oi-no-, oi-uo- {*hei-uo-) 
69963:German rein. Modern High German /?a//7 'slope ' ds. (Celto-Germanic *roi-no-). 
71140:Root / lemma: roi-no- 
(eval):1: == not found
```


## [2026-09-06T15:19:26.486Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '63378,63430p' POK_full.txt"
}
```


### [2026-09-06T15:19:26.539Z] TOOL RESULT

```
Root / lemma: oi-no-, oi-uo- {*hei-uo-) 
See also: see above S. 286 (e-). 
Page(s): 774 

Root / lemma: oiua {*he/-ua-) 
See also: see above S. 297 {e/-). 
Page(s): 774 

Root / lemma: ok- 

Meaning: to think over, *understand, see 

Note: 

Root/ lemma: ok-: 'to think over, *understand, see' derived from a reduced Root/ lemma: 

ok''-: 'to see; eye'. 

Material: Gr. 6kvo(; ' dubiousness, hesitating ', okveoj ' hesitate ', OKvripoq ' dilatorily '; 



Gothic aha'sense, mind, understanding ', 5/775/7 "believe, mean', ahmam. "gliost'; 
ahaks'6ove' (as spirit bird); Old High German 5/7/5" observance, paying attention ' 
(Modern High German achtgeben). Old English eahti. " calculation, consultation, estimate 
', Old High German Old Saxon ahton. Old English ©5/7/75/7 "consider, observe, appraise ', 
Modern High German achten, beachten. Old Icelandic aetla {*ahtildii) "mean, think, intend, 
mean, aim'. 

References: WP. I 169; after Specht KZ 62, 21 1 to ok""-. 
Page(s): 774 

Root / lemma: oRtd(u) 

Meaning: eight 

Note: 

Root/ lemma: oRtd(u)\ eight derived from the extended Root/ lemma: ok-\ "to think over, 

*understand, see, count' + -/is attribute formant modelled after lllyrian attribute nouns, 

adjectives. Hence PIE numbers derived from previously ordinal numbers. 

Material: Old Indie asta, astau {besides asTtf-i. " eighty '), Avestan astaio Avestan asti- " 

width of four fingers ' (to Sg. *asta-), Henning TrPhSoc. 1948, 69; Armenian ^/'(probably 

from *optdW\Vc\ p assumed from seven p)\ gr. oktw; alb. tete {*oktd-t-)\ 

Note: 

Anatolian languages show a pattern similar to alb. So Lycian 5//5/5 "eight' : alb. /e/5 "eight';
```


## [2026-09-06T15:19:27.432Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'Page in Pokorny' POK_full.txt | grep -E ': (73|74|75|281|286)$' | head -20"
}
```


### [2026-09-06T15:19:29.003Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:19:31.747Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E '^Page\\(s\\): (7[3-6]|28[0-8])( |$)' POK_full.txt | head -40"
}
```


### [2026-09-06T15:19:33.436Z] TOOL RESULT

```
24006:Page(s): 287 
29159:Page(s): 281
```


## [2026-09-06T15:19:35.696Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E 'Page\\(s\\): *(7[3-6]|28[0-9])' POK_full.txt | head -40"
}
```


### [2026-09-06T15:19:35.758Z] TOOL RESULT

```
7647:Page(s): 73-75 
8499:Page(s): 75-76 
8541:Page(s): 76-77 
24006:Page(s): 287 
24067:Page(s): 289-290 
24235:Page(s): 287-289 
26183:Page(s): 281-286 
29133:Page(s): 280-281 
29159:Page(s): 281 
59350:Page(s): 730 
59416:Page(s): 730 
59449:Page(s): 730-731 
59468:Page(s): 731 
59767:Page(s): 732 
59794:Page(s): 732-733 
59808:Page(s): 738 
59827:Page(s): 738 
59843:Page(s): 738 
59867:Page(s): 738 
59871:Page(s): 738 
59911:Page(s): 738-739 
59952:Page(s): 739-740 
59968:Page(s): 740 
59990:Page(s): 739 
60013:Page(s): 733 
60090:Page(s): 734 
60114:Page(s): 734 
60174:Page(s): 735 
60311:Page(s): 735-737 
60328:Page(s): 737-738 
60334:Page(s): 741 
60353:Page(s): 743-744 
60450:Page(s): 744-745 
60468:Page(s): 745 
60607:Page(s): 741-743 
60612:Page(s): 745 
60645:Page(s): 743 
60657:Page(s): 745-746 
60673:Page(s): 746 
61109:Page(s): 731-732
```


## [2026-09-06T15:19:38.255Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== entry ending at 7647 (73-75)\"; sed -n '7540,7650p' POK_full.txt; echo; echo \"=== entry ending 8499 (75-76)\"; sed -n '8460,8500p' POK_full.txt"
}
```


### [2026-09-06T15:19:38.330Z] TOOL RESULT

```
=== entry ending at 7647 (73-75)

Root / lemma: au-4, u-{\ ue-, uo-) 

Meaning: that; other 

Material: auo: 0\d Indie Avestan Old pers. ava- " that '; Old Church Slavic Old Russian 

ovh-- ovh-' on the one hand - on the other hand which appears - other ', ovogda - ovogda 

" one time - the other time ' (from this correlative use only poln. dn/ corresponds to English 

deictic "I" and serb. ovaja deictic word meaning "that", also New Bulgarian -v [*uo-s] 

developed). 

u-:0\d Indie amu-{Akk. Sg. amum etc) 'that, yonder', arise from Akk. Sg. m. *am{= 
Indo Germanic *e-m 'eum') + *um (Akk. Sg. of ours stem u); s. Wackernagel-Debrunner III 
550 f. 

Tocharian A ok, B uk' still ', A o/r/' as, and ', A okak' up to ', perhaps only *u-g {zero 
grade to Gothic auk); from in addition B om(p)ne, omte " there '? 

Particle Old Indie u^ thus, also, on the other hand, there again, against it ', emphasizing 
esp. after verbal forms, Pron. and particles {no^ and not, not ' = na u, athd= atha u), gr. -u 
in TTOv-u " even very much ', 

Gothic -^interrogative particle (also the enclitic -uhirom -u-q^e, s. Brugmann IF. 33, 173); 
this ^also in Old Indie a-sau rw. f. "that, yonder', Avestan haum. f., ap. hauvxw. "that, 
yonder', Wackernagel-Debrunner III 529, 541. 



Particle Old Indie u-ta, in both parts " on the one hand - on the other hand, soon - soon, 

- as ', or only in the second part, a little bit opposing " and, thus ' (nachved. in ity-uta, kim- 
uta, praty-uta), 

Avestan uta, ap. ^/a'and, and also'; gr. huts " just as ' from *nF(£) + uts (originally ' as on 
the other hand ', " as, also '), but horn, euts "ote' from £u + t£ after Debrunner IF. 45, 185 
ff.; 5£0t£ is formed in addition to 5£upo; also ouToq, aurn, touto most probably from 6, a, to 
+ UT£ with additional final inflection; 

West Germanic -od\v\ Old Saxon thar-od. Old High German thar-of thither, there ', Old 
Saxon her-od. Old High German her-oV here ', whereupon also Old Saxon hwarod^ 
whither, where ', Old High German warot^ whither, where ' (from * ute? or iroxu * uta? A\so 
*aute, *auti, see below, would be possible basic form). 

Here Avestan uiti, Gatha-Avestan uitr so ', but not Latin i//and utT, Old Latin utei. 

Beside u, uta etc. stands with the ablaut grade Indo Germanic au-: 

gr. au " on the other hand, again ', *auTi " again' (extended to Ionian qutk;, gort. auTiv, 
after antique grammarians for ' right away, there ', where from auriKa " at the moment, 
straight away ', au-9ron the spot, here, there ', auT£ ' again, thus, further '; Latin aut{*aut/) 
" or', autem " however ' (to the form see WH. I 87), Oscan aut, auti^ or ' and " but, on the 
other hand, on the contrary, however ' (to meaning see v. Planta II 465); 

maybe alb. Geg o "or' from Italian o'or' 

Umbrian ute, o/e'aut'; perhaps Gothic auk^ then, but ', Old Norse 5^/r'also, and'. Old 
English eac. Old Saxon ok. Old High German ouh^ and, thus, but ', Modern High German 
also = gr. au-Y£ ' again '. 

Pedersen Pron. dem. 315 supposes gr. au suitable form in the initial sound of from 
alb. a-qe^ so much'. - Brugmann BSGW. 60, 23 a 2 lines up in gr. au-T6(; as " (he) himself 

- (he) of his own, self '; other interpretations see with Schwyzer Gr. Gr. I 613 f. 

Maybe alb. {*aut-) vete^seW [common alb. prothetic v- before bare initial vowels]. 

With A-forms airan. avar^ here', Lithuanian aure^ see there! ', zero grade Umbrian uru 
' that, that yonder, that one; emphatically, that well-known; in contrast with hie, the former 
', ura-ku^a6 illam', ures'WWs' (o/'e/'ose rather with d= uas = Lithuanian ad); perhaps 
5£upo " here, well, all right, well then (an obsolete interjection meaning "come now") ' 



(5£upaj after oniaaoj , inschr. SsOps after ays) from *5£-upo (5s " here ' + aupo " here '), 
SchwyzerGr. Gr. I 612, 632. 

ue-, UO-: meaning "or' (= " on the other hand ') esp. in Old Indie va^ or' (also " even, 
yet; meanwhile; probably, possibly '; also confirming vai), Avestan ap. 1/5' or' (particle of 
the emphasis and assurance). 

Old Indie Avestan va- va' either - or ', gr. r|-(F)e, n (with proclitic emphasis, proclitic stress 
for n-(F)£, as yet in the second part of the double question), 

Latin -ve'or' (also in ceu, sTve, seu, neve, neu), also probably Irish no, abret. nou^or' (if 
from *ne-ue " or not ' ' with fading the negative meaning originally in negative sentences, 
Thurneysen Grammar 551; 

not more probably after Pedersen KG. I 441 a grown stiff imperative * neue oi the verb Irish 
at-no/' he entrusts with him ', gr. veuoj); Tocharian B wa-t' where'. 

compare also Old Indie /-va (: va = \-bz: bt) " just as, exactly the same way ', e-va " in 
such a way, exactly the same way, just, only ', evam ' so, thus ' (behaves to be confirmed 
1/5/and va- vaas e-na- ' this ' to na- na' in different way ', originally ' thus and thus '; with 
e-va corresponds gr. oI(F)oc; " only' (" * just only '), Avestan aeva-. Old pers. a/va- "an, 
one' (compare with no- demonstrative Indo Germanic *of-no-s^ an, one '). 

References: S. esp. Brugmann Dem. 96 f., Grundr. II2 2, 341-343, 350, 731 f. m. 
Lithuanian II23, 987, 

Schwyzer Gr. Gr. I 629, 632, 804, Boisacq s. v. au, etc 

WP. I 187 f., WH. I 87, 209, Van Windekens Lexique 78, 80. 

Page(s): 73-75 

Root / lemma: aug^fh)-: uq'^fhj- and beside it probably as andere lengthened grade 


=== entry ending 8499 (75-76)
hvayate). 

d^-extension 1 . au-6'^-, 2. (a)u-eA^-, u-^^-: 

1 . Armenian z-aud^ strap ' {z-audem " connects, ties together '), y-a^o^'strap, limb, joint 
' {y-audem " join together '), aud^shoe'; 

Lithuanian audziau, audziu, aust/'to weave', ataudaTP\. " woof, udis^ a unique fabric, the 
weaving ', udas^ eel line ' (vowel as with augu^ increase, sprout ': ugys^ annual growth '); 

russ. uslo^ fabric ' {uzda^ bridle '?), see below eu-^ pull '. It goes back to the image of the 
weaving or spining and that of her assigned fate goddess: 

aud!"-^ luck, possession, wealth ': lllyrian PN Audarus, Audata{: QerxwavWc Audo-berht), 
paion. PN Audo-leon {Krahe IF. 58, 132), cymr. udd {*audos) " master, mister' (different 
Lewis-Pedersen 14), bret. ozac'h^ landlord ' {*udakkos). Loth RC. 41, 234; Old Saxon 
odan. Old English eaden. Old Norse audinn^ granted from the destiny, grants ', (under the 
influence of common Celtic -ns-, -nt- > -nn-). Old Norse audna' destiny, luck ', audr^ 
wealth ', Old English ead^ possession, wealth, luck ', Old Saxon do'" possession, 
prosperity ', Old High German al-od^ full and free possession ' (Middle Latin allodium). 
Middle High German klein-of jewel ', Gothic audahafts^ makes happy ', audags^ 
blessed, fortunate ', Old High German otac^ happy, rich '. 

2. Old Norse vad\. ' fabric, piece, stuff, as comes ready of the loom, drag net ', P\.vadlr 
" gowns, clothes ', Old English wsed {*wedi-) f. " clothes, rope ', Old Saxon wad^ clothes ', 
Old High German wat. Gen.-/' clothes, armament '; 

Old Norse vadrxw. ' rope, string, fishing line ', Swedish Norwegian vadu. 'drag net' (Old 
Norse vgzti. ' spot for fishing at sea from *wada-std). Middle High German wate, wadei. 
'drag net, trawl net ', Middle High German splnne-weV spinning web '. 

References: WP. I 16 f., WH. I 88. 

See also: Maybe here ^eb^-'to weave', ^ed^-' bind, connect ' (wherefore as nasal form 
probably £/e/7dh-),see there; also perhaps uei-^ twist, spin ', (a)ueg-io weave etc' {uer-" 
twist, spin '?), ues-^ wrap '. 



Page(s): 75-76
```


## [2026-09-06T15:19:46.886Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '960,1120p' POK_01.txt"
}
```


### [2026-09-06T15:19:46.978Z] TOOL RESULT

```
<persisted-output>
Output too large (30.5KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bage4c81p.txt

Preview (first 2KB):
■T-  au  Ausruf  des  Schmerzes,   der  Verwirrung,  Entrüstung.
Ai.  0,  lat.  au,  ags.  ea,  mhd.  ou(ioe),  nhd.  au,  lett.  aü,  äu  (zweisilb.  au, avu  bei  Unwillen,  Abweisung,  Überraschung),   poln.  au,  cech.  ou. WH.  I  78.
72
2.  au-,  au-es-,  aus-  ^übernachten,  schlafend
Arm.  aganim  ,übernachte';  vair-ag  ,au£  dem  Lande  lebend',  aut'  ,Über- nachten,  Nachtruhe,  Station^
Gr.  lavo)  ,scblafe^  aus  redupl.  "^i-ausö,  Aor.  i-avaai,  woneben  unredupl. Aor.  Usaa,  Inf.  äfea{o)ai]  avXtg,  -löog  , Aufenthaltsort,  Lager,  Stall,  Nacht- -  lager^,  avUlop^ai  ,bin  im  Hofe,  übernachte',  äygavXog  ,im  Freien  übernach- tend^, aiUj  ,Hof,  Wohnung^  (ursprüngl.  wohl  ,der  eingezäunte  Raum  ums Haus,  in  dem  das  Vieh  für  die  Nachtzeit  zusammengetrieben  wird');  von lavco  stammt  außer  lavd-i-iög  ,Nachtlager^,  ^r]?uavd^iA,6g  ,Schafstall^,  iviavd- (.lög  , Aufenthaltsort'  (:  hom.  inavstv  ,sein  Ruhequartier  haben')  auch  gr. Eviavxog  eigentlich  ,Rast,  Ruhestation',  daher  die  Sonnenwenden  als  Ruhe- stationen im  Sonnenlauf  {solstitium)^  dann  .Jahr,  Jahrestag'  (anders  Specht Idg.  Dekl.  15,  Schwjzer  Gr.  Gr.  l,  424^,  s.  auch  en-  ,Jahr').
Eine  schwere  Basis  *aue-,  ^auö-  in  den  wohl  anzureihenden  hom. dcoretg  ijTtvov  (von  Schulze  Qu.  ep.  72  unmittelbar  zu  lavo)  gestellt  unter formalem  Vergleich  von  ^q{J^)o)t&u)  :  eiQOiiai  aus  *£QJ^O[.iac)  und  äcogog (Sappho),  (hgog  (Kallimachos)  ,v7tvog^  (Benfey  Wzl.-Lex.  I  298),  wozu  ags. loerig,  engl,  loeary^  as.  wörag,  icörig  ,müde',  ahd.  louorag  , berauscht';  über ai.  väyati  ,wird  müde';  s.  aber  Wz.  awe-  ,sich  mühen,  anstrengen'.
WP.  I  19f.  Schwjzer  Gr.  Gr.  1  690.''
Über  ues-  ,verweilen'  s.  unter   besonderem  Artikel.
5.  aU'  (aue) ;  ue-  ,herab,  weg  von  — '.
...
</persisted-output>
```


## [2026-09-06T15:19:51.280Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=977 && NR<=1080' POK_01.txt | grep -n -E \"jener|oder|ap\\.|aeva|aiva|uta|uiti|va\" | head -40"
}
```


### [2026-09-06T15:19:53.094Z] TOOL RESULT

```
3:1  ett    Präverb  u-    (^it'e-,  i(^ci-)  , hierher^,    a-ica-an  ,hinweg^   (Sturtevant   Lg.
6:*>-üt  aiipja-  (N.  Sg.  *aupeis  oder  *aups)  ,'öde,  verlassen^  (*,abgelegen^), auhida  Wüste^,  ahd.  öcli,  nhd.  Öde,  anord.  audr  ,öde^;  air.  üathad  , Einzel- heit Vereinzelung^  —  Geht  auf  die  Schrecken  der  Einöde,  Wildnis  auch mir.  üath  _,Schrecken,  schrecklich'  (fernzuhalten  sind  cjmr.  uthr  , schreck- lich' corn.  uth,  euth,  bret.  euz  , Schrecken')  ?  Wenigstens  ist  deren  Ver- bindung mit  lat.  pavere  ,sich  ängstigen,  vor  Furcht  zittern'  alles  eher  als sicher,  s.  pou-  , Angst'.
9:lat.  *vS-  in  vescor  ursprüngl.  , wovon  abessen'  (:  escd)^  woraus  rückgebildet üßscMS  , gefräßig;  wählerisch  im  Essen  (*nur  abknabbernd);  abgezehrt';  ve- zur  Bezeichnung  eines  fehlerhaften  Zuviel  oder  Zuwenig,  ve-cors  , aber- witzig, verrückt,  tückisch',  ve-grandis  , nicht  groß,  winzig',  vesänus  ,ver- rückt',   Ve-jovis,  umbr.  ve-purus  (Abi.  PL),  wenn  .(legä)  ^nvqa^.
13:Verwandtschaft  von  idg.  *aw-,  iß-  mit  dem  Pron.-St.  au-,  u-  .jener'  als ,von  jenseits,  von  dorther'  ist  denkbar.
15:4-  au-,    u-    (:  ue-,    uo-)    Pronominalstamm   ,jener',   auch    gegenüberstellend , alter,    alius',   , andrerseits,   hinwiederum',    in   zwei    aufeinanderfolgen- den Satzgliedern  gesetzt  ,der  einerseits  —  der  andrerseits',  , einerseits —  andrerseits'. awo-:  Ai.  av.  apers.  ava-  ,jener';  aksl.  aruss.  ov^^  —  ov^-  ,der  einerseits —  der  andrerseits,   der  eine  —  der  andere',    ovogda  —  ovogda  ,das  eine
17:Mal  —  das  andere  Mal^  (aus  diesem  korrelativen  Gebrauche  erst  scheint das  jener-deiktische  poln.  öw  und  das  ich-deiktische  serb.  bvaj,  ebenso nbulg.  -V  [*uo-s]  entwickelt).
18:U-:  Ai.  amü-  (Akk.  Sg.  amüm  usw.)  ^jener^,  erwachsen  aus  Akk.  So_ m.  '-^am  (=  idg.  *ß-m  ,eum^)  -\-  *um  (Akk.  Sg.  unseres  St.  w);  s.  Wacker. nagel-Debrunner  III  550  f.  |
20:Partikel  ai.  u  ^auch,  andrerseits^  hinwiederum^  dag'eg'en^,  hervorheben^ bes.  nach  Verbalformen^  Pron.  und  Partikeln  (nö  ^und  nicht^  nicht^  =5 nd  u,  atliö  =  atha  u)j  gr.  -v  in  Tcav-v  ,gar  sehr^^  got.  -u  Fragepartikel (auch  die  Enklitika  -uh  aus  -u-que,  s.  Brugmann  IF.  33^  173);  dieses  % auch  in  ai.  a-säü  m.  f.  ^jener^^  av.  hau  m.  f.,  ap.  hauv  m.  j'ener^,  Wacker- nagel-Debrunner  III  529^  541.  l
21:Partikel  ai.  u-tä,  in  beiden  Gliedern  ^einerseits — andrerseits^  bald—* bald^  sowohl  —  als  auch^^  oder  nur  im  zweiten  Glieds  etwas  entgegensetzend ,und^  auch^  (nachved.  in  ity-uta,  kim-uta,  praty-uta),  av.  uta,  ap.  utä ^und_,  und  auch'^;  griech.  fjvxs  ^ebenso  wie^  aus  *iJ/(£)  -{- vzs  (ursprüngl.  ,wie andrerseits^;,  ,wie  auch^);  aber  hom.  evTs  ,ov8^  aus  ei  +  xe  nach  Deb runner IF.  45_,  185ff. ;  devxs  ist  zugebildet  zu  ösvqo]  auch  o^vog,  aijTJ],  tovvo  am wahrscheinlichsten  aus  6,  a,  to  +  vre  mit  nachträglicher  Endflexion; wgerm.  -od  in  as.  tliar-od,  ahd.  thar-ot  ^dorthin^  dort^^  as.  her-od,  ahd. her-ot  ^hierhin^^  wonach  auch  as.  hwarod  ^wohin^  wo^;,  ahd.  wai-ot  ^wohin' (aus  *ute?  oder  aus  *uta?  Auch  ^aute,  *auti,  siehe  unten_,  wäre  mögliche Grundform).
22:Hierher  av.  uiti,  gthav.  üiti  ^so^;  nicht   aber  lat.  ut  und  utl^  alat.  utei
24:gr.  (d  .andrerseits,  wiederum^;,  *a^rt  .wiederum"  (erweitert  zu  ion. a^Tig,  gort,  avxiv,  nach  antiken  Grammatikern  für  .auf  der  Stelle,  dort^. woher  amUa  .im  Augenblick,  sogleich',  av-d-i  .daselbst',  aixe  .wieder, auch,  ferner';  lat.  aut  {^auti)  .oder',  autem  .aber'  (zur  Form  s.  WH.  I  87), osk.  aut,  auti  .auf  und  .autem'  (zur  ßed.  s.  v.  Planta  II  465).  umbr.  ute,  ote .auf;  vielleicht  auch  got.  auk  .denn.  aber',  anord.  auk  .auch.  und',  ags.  eac,  as. ök  .auch',  ahd.  ouh  .und.  auch.  aber',  nhd.   auch  =  gr.  av-ys  .wiederum'.
26:Mit  r-Formans  airan.  avar  .hier',  lit.  aure  .siehe  da!',  tiefstufig  umbr. uru  .illo'.   ura-ku  .ad  illam'.   ures  .illis'    {orer  ose  eher   mit  ö  =  w  als
29:ue-    U0-:  'Die   Bed.  ^oder*  (==  _,andrerseits^)    bes.  in  ai.  vä  ,oder^  (auch
30:selbst    sogar;  indessen;  wohl,  etwa'^;  ebenso  bekräftigend  väi),  av.  ap.  vä
31:oder^  (auch  Partikel  der  Hervorhebung  und  Versicherung),  ai.  av.  vä — vä
32:eut\veder  —  oder'^,    gr.  ri-{f)i^    ^  (mit  Proklisenbetouung  für  ^-(/)£,  wie
33:noch  im  2.  Glied  der  Doppelfrage),  lat.  -ve  ,oder^  (auch  in  ceUy  slve,  spal,
34:n^ve    neu),  auch    wohl   ir.  nö,   abret.    nou   ,oder^   (wenn   aus    *ne-ue  ,oder
39:Vgl.  auch  ai.  i-vd  (:  va  =  l-Si :  ds)  ,gleichwie,  geradeso^,  e-vd  ,so,  ge- radeso, eben,  nur^,  evdm  ,so^  (verhält  sich  zu  bekräftigendem  väi  und vä — vä  wie  e-na-  ,dieser^  zu  nä—nä  ,auf  verschiedene  Weise^,  ursprüngl. ,so  und  so^;  mit  e-vd  deckt  sich  gr.  ol{f)og  ,allein^  (,*gerade  nur  der^), av.  aeva-,  apers.  aiva-  ,ein^  (^g'l-  i^it  dem  7?o-Demonstrativ  idg.  *oi-no-s  ,ein^).
42:Unerweitert  in:  ai.  ötum,  ötave  (von  der  set-Basis  vätave)  ,weben^,  Perf. üvuh,  Partiz.  ütd-,  vy-uta-  (auch  das  Präs.  vdyati  ,webt^  kann  nach  Wacker- nagel Ai.  Gr.  I  94  ein  -eto-Präsens  v-dyati  sein,  so  daß  Fut.  vayisyati, väya-  ,Weber*^  erst  dazu  neugeschaffen  wären),  ütu-  m.  ,Einschlag  des Gewebes^,  väna-  n.  ,das  Weben'^.
45:1.  Arm.  z-aud  ,Band^  (z-audem  ,verbinde,  verknüpfe'),  y-aud  ,Band, Glied,  Gelenk^  (y-audem  ,füge  zusammen^),  aud  ,Schuh^;  lit.  dudziau, dudziu,  dusti  ,weben^,  ataudai  PL  ,Einschlag^,  üdis  ,ein  einmaliges  Gewebe, das  x^bweben'^,  udas  ,Aalschnur^  (Vokal  wie  bei  diigu  ,wachse'^ :  ügys ,Jahreswuchs^);  russ.  uslo  ,Gewebe^  (uzda  ,Zaum^?),  s.  u.  eu-  ,anziehen^ Auf  die  Vorstellung  der  webenden  oder  spinnenden  Schicksalsgöttin  und des  von  ihr  Zuo:eteilten  führt  auch  zurück:
49:anord.  vadr  m.  ,Seil,  Schnur,  Angelschnur^,  schwed.  norw.  vad  n.  ;Zug- netz*^  (anord.  vgzt  f.  ,Fischplatz  auf  der  See'  aus  *wada-st5)^  mhd.  wate, wade  f.  ,Zugnetz,  Wate^,  mhd.  spimie-wet  ,Spinnweb^
54:Ai.  vddati  ,läßt  die  Stimme  erschallen,  redet^  (Perf.  üdimd,  Partiz. uditd-),  vddanam  ,das  Tönen,  Reden,  Mund^,  üditi-h  f.  ,Rede^,  vädayati ,läßt  ertönen,  spielt  (ein  Musikinstrument),  läßt  sprechen^,  väditram  ,musi- kalisches  Instrument,  Musik^,  väda-  ,ertÖnen  lassend,  m.  Laut,  Ruf,  Klang, Aussage,  Wortstreif^;  in  der  Dehnstufe  und  der  Bed.  vergleicht  sich  am nächsten  aksl.  vada  ,calumnia',  vaditi  ,accusare^;
55:nasaliert  ai.  vandate,  -ti  ,lobt,  preist,  begrüßt  mit  Ehrfurcht^,  vandanam ,Lob,  Preis,  ehrfurchtsvolle  Begrüßung^,  vandäru-  ,lobend,  preisend^; siehe  noch  Uhlenbeck  Ai.  Wb.  unter  vallakl  ,eine  Art  Laute*^,  vallahha-h , Günstling^.
57:Lit.  vadinü,  vadmti  ,rufen,  nennen^.
58:au-e-d'  in  d(J^)rjdd}v  ,NachtigalP  (äßr^ööva'  Scrjdöva  Hes.,  äol.  Scrjdcov  und drjdü),    die    Tiefstufe    ävd-    in    aidi]    ,Laut,    Stimme,    Sprache'    (äol.   ai'cJw
65:Ai.  dvati  ^verlangt,  begünstigt_,  fördert^  =  av.  avaiti  ^sorg-t,  hilft^  =  air. con-öi  jbeschützt^;  messap.  aftva^xi  ^valere  iubeö?^;  ai.  dvas-  n.  Befriedigung, Gunst  Beistand^  =  av.  avah-  n.  .Hilfe'^  (dazu  wohl  ai.  avasd-  n.  ^Nahrung*^)^ ytrl.  o-r.  iv-Tj'rjg  ^wohlwollend''  ("^'ev-ßfTJg)]  ai.  öman-  ^günstig,  helfend^  =  av. aoman-j  helfend,  beistehend^,  ai.  ömdn-  m.  , Gunst,  Beistand,  Schutz^,  öma-h Genosse^;  ai.  avitdr-  m.  ,Gönner,  Förderer*^  (von  der  zweisilbigen  Wzf.  wie Fut.  avisyati,  Perf.  2.  Sg.  avitha,  sowie  Partiz.  ütd-  und:)  üti-li  ,För- derung,  Hilfe';
69:air.  con  *  öi  ,beschützt',  cymr.  eioyllys  ,voluntas',  corn.  awell  ,Verlangen', abr.  a-iul  ,ultro',  mbret.  eoull,  youll  ,voluntas',  als  Namenbestandteil  in gall.  Ävi-cantus  (=  abret.  Eucant),  acymr.  Euilaun  u.  dgl.,  ebenso  in  ahd. Namen  wie  Awileih,  Äico]  vgl.  got.  awi-liu])  ^xägig,  svxaQiaTia^ ]  mcymr. ri-m-aiv  ,er  gewähre  mir',  cymr.  ad-aio  (mit  negat.  at-)  ,verlassen',  abret. di-eteguetic  ,destitutas'  {*di-at-aiü-etic).
71:Wenn  auch  altlit.  auUis  ,sich  erquicken',  atansimas  ,Erquickung',  lett. ataust  ,sich  erholen,  laben',  atauset  ,erquicken,  laben'  verwandt  sind,  liegt ihnen  die  Tiefstufe  *aus-  des  in  ai.  dvas-y  gr.  h-rjrjg  vorliegenden  es-St. zugrunde.  Oder  =  lit.  dusti  ,kalt  werden',  dusyti  ,kühlen'?
76:Ai.  -avati  mit  ud-  und  jpra-  ,auf merken,  beachten^,  aksl.  uim  ,Verstand' (Gdf.  ^au-mo-)]  hierzu  toch.  B  om-palokonne  ,meditation*^?  Anders  Pedersen, Tochar.  223  Anm.
77:Buis-:  dehnstufig  ai.  ävis  Adv.  ,offenbar,  bemerkbar^,  av.  ävis  Adv. ,offenbar,  vor  Augen^  (npers.  äsJcäi^  ,klar'^;  ai.  avistya-h,  av.  ävisya-  ,offen- kundig^;  aksl.  ave,  jave  Adv.  ,kund,  offenbar^  (im  Ausgang  nach  den Adjektivadverbien  auf  -e  umgebildet  aus  *avh,  wovon :)  aviti,  javiti  ,offen- baren,  kundmachen,  zeigen^  (lit.  ovytis  ,sich  im  Traume  sehen  lassen^ Lw.  aus  dem  Slav.).
84:ai.  avatd-h  m.  ,Brunnen^  (*awitos),  avatd-h  , Zisterne^  (mit  prakrit.  t  aus  t)^ ital.  FIN  Ävens  im  Sabinerland  (davon  Aventlnus  m.  Hügel  Roms?),  Aventia (Etrurien),  gall.  Aventia,  Quellnjmphe  von  Aventicum  >  frz.  Avenckes (Schweiz),  zahlreiche  FIN  Avantia  (*auntiä)  >  frz.  Avance,  La  Vence,  abrit. "^Avantisä  >  cymr.  Ewenni]  alit.  FIN  Avantä,  lett.  avuots  (*aicontos)  ,Quelle^
87:Ai.  undtti  (ju-n-ed-ti),  3.  PL  unddti  ,quellt,  benetzt^ ;  av.  vaidi-  f.  ,Wasser- lauf,  Bewässerungskanal.
95:Gr.  VöcüQ,  vdaxog  (*vö-n-Tog)  ^Wasser^  (mit  metr.  Dehnung  vÖcjq);  vom r-St.  abgeleitet  äwSgog  ^wasserlos^^^  ^äoog^  Vöoa  ^Wasserschlange^^  ivvöglg  f. Fischotter^;  vdagrjg,  tdagög  ^wässerig^  {vöaleog  ds.  mit  Suffixtausch;  ähn- lich ^llog  ^Wasser schlänge;,  Ichneumon^  :  ^öqog  =  lak.  kXXd  :  edQa)^  ijöagog Wassersucht^;  vögla  ^Wassereimer*^  (:  lat.  uter),  vom  i2-St.  (vgl.  ijövrjg wässerig^)  abgeleitet  I^Xogvövt]  eig.  ^Meereswoge^  (?);  Beiname  der  Amphi- trite  und  Thetis  (Johansson  Beitr.  117;  ob  auch  iJövov  ^TrüffeF  als  ^saftig^??); sowie  wahrscheinlich  KaX-vöcüv,  -vdva  (-vuvg),  KaXvövioi,  -vf.ivLOL  (s.  Boi- sacq998a)?
98:Alb.  uß  ;Wasser^  (nach  Pedersen  KZ.  34^  286;  36^  339  nicht  aus  *wcZ- n\d,  sondern  aus  *wc?-;  oder  doch  aus  *wcZö?).
99:Lat.  unda  f.  ^Welle^  Woge^  (mit  w-Infix  aus  dem  Präsens;  vgl.  apr. wundan  n.^  unds  m.  ^Wasser^  und  ai.  undtti,  unddti  sowie  lit.  vanduo, -eüs,  vdndeni,  zem.  unduo,  lett.  ildens  m.  f.  _,Wasser^;  und  dazu  Schulze EN.  243;  Brugmann  Grdr.  IP  3,  281;  283;  Trautmann  337);  iiter,  utris ;Schlauch''  (*-udri-s  ;*Wasserschlauch'^;  vgl.  gr.  vögla),  lutra  ;Fischotter^ (l-  nach  lutum  ;PfützeQ.
102:Got.  ivatö  (n-St.);  Dat.  PI.  watnam  ;Wasser^;  aschwed.  vcetur  (ce  =  idg.  e? eher  Umlaut  von  germ.  a  in  den  -in-KasuS;  s.  Bartolomae  aaO.);  aisl. vatn  n.  (o-St.  geAvordeU;  vgl.  got.  Dat.  PL  icatnam),  vatr,  nord.  Seename Vättern]  ahd.  wazzar,  as.  watar,  ags.  tcceter  (*iiodör)  ;Wasser^;  aisl.  otr, ags.  otor,  ahd.  ottar  m.  ^Otter^;  dazu  FIN  Otter,  alt  Uterna]  mit  Binnen- nasalierung  (vgl.  oben  zu  lat.  unda)  wahrscheinlich  got.  icintruSj  aisl.  vetr, ags.  Winter,  ahd.  as.  wintar  ;Winter^  als  ;nasse  Jahreszeit'^  (Liden  PBrB. 15^  522;  Falk-Torp  unter  vinter,  nicht  besser  zu  ir.  ßnd  ;Weiß'^;  s.  unter sueid-  ;g]änzen');
104:vielleicht  zu  Wassei-  auch  ahd.  ags.  wascan,  aisl.  vaska,  nhd.  wasche^ wusch  (^loat-sk-)-  mit  Dehnstufe  e  von  der  Wz.  aus  gebildet  aisl.  vätr ags.  wcet^  engl,  wet  _,naß_,  durchnäßt^.
```


## [2026-09-06T15:20:05.497Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '26050,26190p' POK_full.txt"
}
```


### [2026-09-06T15:20:05.547Z] TOOL RESULT

```
Note: 

This is all wrong etymology. Root / lemma: e-3, ei-, /-, fem. T-\ "this, etc. (demonstrative 
stem); one' derived from the reduced Root/ lemma: eg-, eg(h)om, ego: "I'. Indie 
languages display -g- > -y-, Germanic -g- > -g-, Italic -gh- > -cc, kk-, Slavic -gh- > -d-. 



Old Church S\a\/\c: Jed/nh "one' [num o]; Jedbnb "one' [num o] derived from eg(h)omn 
[common Baltic-lllyrian -gh- > -d-. Common prothetic Slavicy-, Baltic lllyrian i/- stand for the 
lost laryngeal /?-. 

Maybe zero grade in alb. {*g(h)omn) nje^oue' similar to alb. njoh {*gne-sRd) "know'. 

With formants -ko-{as Old Indie o'i///ra "consisting of two') Old Indie eka-^ one; only one; 
one and the same ', ekaffya^\he one', Proto Indie (in Hittite Text) aika-vartana^ a spin, one 
rotation ' (Kretschmer KZ. 55, 93); about Latin unicus, Gothic ainaha. Old Church Slavic 
inok-b see above e 

Maybe compound alb. Geg {*nie uka) nuk, Tosc nuku, nuke' {*not one) no, not' 

With formants -go- Gothic ainakis' single, spouseless ' (also above Old Norse einka 
etc.). Church Slavic inogb " solitary, of male beasts which have been driven from the herd: 
hence, savage, ferocious, a griffin or dragon '; s. Feist 22 f. 

Similar reverting together with e-(e.g. Old Indie asau) and 5/- (Old Indie aisamah, 
Armenian a/n etc.) see above. 

It seems that root lemma for number one spread spread from Indo European to Dravidian, 
then to to Semitic: 

Indo-European 

Germanic: Old Germanic+ *ainaz. Western: Old English+ an. Middle English+ an, English 
one, Scots ane. Old Frisian+ en, W.Frisian ien, Frisian (Saterland) aan, Dutch een, }/V/S 
Flemish \ev\, Brabants\en, Low Saxon een, Ems/and e\n, Mennonite Plautdietscheeu, 
Afrikaans een, German eins. Central Bavarian oaus, Swabian oes, Alsatian e'\r\s, Cimbrian 
oan, Rimellaais, /?/7e//7 Fran con ian aans, Pennsylvania eens, Luxembourgeois eent, 
Swiss German eis, Yiddish eyns. Middle High German+ ein. Old High German+ ein. 
Northern: Runic+ seinn. Old Norse+ einn, Norwegian en {Ny. ein), Danish en, Swedish en, 
Faroese ein. Old lcelandic+ einn, Icelandic einn. Eastern: Gothic+ ains, Crimean+ene, 
Italic: Oscan+ uinus, Umbrian+ uns, Latin+ u:nus, Romance: Mozarabic+ uno, Portuguese 
um, Galician un, Spanish uno, Ladino unu, Asturian uno, Aragonese un, Catalan un, 
Valencianu, Old French+ un, French un, l/Vaiioon onk, Jerriais \eune, Poitevin\n, Old 
Picard+ ung, Picard'm, Occitan (Provengal) un, Lengadocian un, Gascon un, Auvergnat 
vun, Limosin un, Franco-Provengal (Vaudois) on, Rumantsch Grischun\n, Sursilvan\n, 
Valladerun, Friulian u~ng, Ladin un, Dalmatian+ join, Italian uno, Piedmontese un, 
Milanese vun, Geno vese u n , Venetian o n , Parmesan v on , Corsican unu, Umbrian unu, 



Neapolitan \iv\e, S/c/7/an unu, Romanian unu, Arumanian unu, Meglenite unu, Istriot ur, 
Sardinian unu, Celtic: Proto-Celtic+ oinos, Gaulish+ *6nos, Brythonic (P-Celtic) : Welsh un, 
Cardiganshire^, Breton unan, Vannetaisuuau, Unified Cornish+ un, Common onan, 
i\4odern on, Devonian+ un, Goidelic (Q-Ceitic) : Old lrish+ oen, Irish aon, Scots Gaelic aon, 
Manx nane, IHellenic: Mycenean Greek+ e-me (*hemei). Classical Greek+ hei:s, Greelc 
ena, Cyprioteuas, Tsakonian ena, Tocliarian: Tocharian A+ sas, Tocharian B+ se, 
Albanian: Albanian nje, Gtieg (Qosaj) n'a, Tosl< (i\4andritsa)u\, Armenian: +Classical 
Armenian mi, Armenian mek, Baltic West: Old Prussian+ aims. East: Lithuanian vienas, 
Latvian viens, LatgaiianVv.us, Slavic East: Russian odin, odin, Belarussian adzfn, adzfn, 
Ukrainian odin, ody'n. West: Polish jeden, Kashubian jeden, Polabian+ janu, Czech jeden, 
Slovak jeden, M/es/jeden, Eas/jeden, Upper Serbian jedyn. Lower Serbian jaden, Soutii : 
Old Church Slavonic+ jedinu, Bulgarian edin, Macedonian eden, Serbo-Croat jedan, 
Slovene ena, Anatolian: Hittite+ *a:nt-, Luwian+ *a-, Lycian+ shta, Indo-lranian: Proto- 
lndo-lranian+ *aiwas, Iranian Eastern: Ossetian lron'\u, Digor\eu, Avestan+ ae:uua-, 
Khwarezmian+ 'yw, Sogdian+ 'yw, Yaghnobi i:, Bactrian+ io:go, Saka+ s's'au, Pashto yaw, 
Wakhi i:, Munji yu, Yidgha yu, Ishkashmi uk, Sanglechi vak, Shughn yi:w, Rushaniy\:\N, 
Yazgulami wu,; Sarikoli (Tashkorghani) iw, Parachi zhu, Ormuri so:, Westem Northwest: 
Parthian+ 'yw, Yazdi ya, Nayini yak, Natanzi yaek, Khunsari yag, Gazi yeg, Sivandi ya, 
Vafsi yey, Semnani i, Sangisari yaekae', Gilaki y^k, Mazanderani yak, Talysh i, Harzani i, 
Zaza zhew, Gorani yak, Baluchi y^k, Turkmenistan yak, E Hill yak, Rakhshani (Western) 
y^kk, Kermanji (S) Kurdish yak, Zaza (N) Kurdish e:k, Bajaiani'xVke:, Kermanshahi yak?'. 
Southwest: Old Persian+ aiva, Pahlavi+ e:vak, Farsi yak, Isfahan! ye{\(), Tajik yak, Tati 
yae, Chali\, Pars yek, Lari yak, Luri ya, Kumzari yek, Nuristani: Ashkun ach, Wasi-weri i 
pu:n, Kati ev, Kalasha-ala ew. Indie: Sanskrit+ eka, Prakrit+ ekko:, Ardhamagadhi+ e^e, 
Pali+ eka, Romany (Gypsy): Spanish yes, Welsh yek', Kalderashyek{\\), Syrian e.ka, 
Armenian \aku, Iranianyek, Sinhalese-Maldivian: Sinhalese eka, Vedda ekamay, 
Maldivian eke. Northern India: Dardic: Kashmiri akh, Shina ek, Brokskate.k, Phalura a:k, 
Bashkarik ak, Tirahi ek, Torwali ek, Wotapuri yek, Maiya ak, Kalasha ek, Khowar i, Dameli 
ek, Gawar-bati yok, Pashai i:, Shumashti yak, Nangalami yak, Dumaki ek. Western: 
Marathi ek, Konkani ek, Sindhi hiku, A77a//7hakro, Lahnda hikk. Central: Hindi/ Urdu ek, 
Parya yek, Punjabi yk, Siraikihxk, Gujarati ek, Rajasthani (Marwari) e:k, Banjari (Lamani) 
ek, Malvi e:k, Bhili e:k, Dogri ik, Kumauni e:k, Garhwali e:k, W Pahari e:k, Khandeshi e:k. 
East Central: Nepali ek, Maithili ek, Magahi ek, Bhojpuri e:k, Awadhi (Kosali) e:k, 
Chattisgarhi e:k. Eastern: Oriya ek, Bengali aek, Assamese ek, Mayang a: 



Dravidian 



Northwest: Brahui asi, Northeast: Kurukh onta:, Malto ort, Central: Kolami okkod, Naiki 
okko, Parji o:kuri:, Gadaba okur, Telugu okati, Gondi undi:, Koya orro, Konda unri, Manda 
ru, Pengo ro, Kui ro, Kuvi ro:ndi, South: Tulu onji, Koraga onji, Kannada ondu, Badaga 
ondu, Kodagu ond", Kurumba -onde, Toda wid, Kota vodde, Tamil onrru, Malayalam onnu, 
Irula vondunder 



Burushashki 

Hunza h\k, Yas/nhek 

Etruscan 

Etruscan+ thu(n) 

Semitic 

East: Akkadian+ ishte:n, Central: Arabic wa:hid, Kashka-Darya iad, Saudi \Naah\d, 

Yemen/ v\/aah\d, Syrian ^a.hed, Lebanese ^ahad, Cypriot Texen, iraqi\Naah\d, Egyptian 

wa:hid, E Libyan '^ahad, N African (Darja) ^a.hed, Moroccan ^ahed, Sudanese \Naah\d, 

Nigerian \Na:\\\d, Zanzibari\Na:\\\, Maltese wieh=ed, Phoenecian+ '-h-d, Ugaritic+ ahd; 

Moabite+: Classical Hebrew+ 'ahat, Modern Hebrew 'axat, Classical Aramaic+ xadh, 

Modern Aramaic ahad, Classical Syriac+ hadh, Syriac kha, Vanhe; 

South: Old S. Arabian+ '-h-d, South Arabian (l-iarsusi) \:a:d, fSheriJ i'ad, So co tra i' ad; 

N Ethiopia Geez+ ?ah=adu, Tigre worot, Beni Amir orot, Tigrinya hade; 

S Ethiopia. Amharic and, Argobba hand, Harari ahad, E Gurage ad, Gafat+ ajja, Soddo att 

Goggot quna, Muher at, Masqan at, CW Gurage at, Ennemor Attic 

References: WP. I 95 ff., WH. I 368 f., 399 f., 409, 671 , 720 ff., 869, Trautmann 3, 65, 72, 
1 05, Schwyzer Gr. Gr. I 548, 588, 608, 61 3 f., 628 f., 651 . 
Page(s): 281-286 



Root / lemma: errto'"/-, empi- 
Meaning: a kind of mosquito or bee 
Note: With taboo variation b^ : pi 
Material: Gr. spnic;, -i5oq 'a mosquito ';
```


## [2026-09-06T15:20:14.663Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=4023 && NR<=4100' POK_01.txt | grep -n -E \"oi-no|aiva|aeva|ima|aita|ap\\.|ena|aina\" | head -30"
}
```


### [2026-09-06T15:20:17.092Z] TOOL RESULT

```
19:ai.  aydm  ,er'  =  gthav.  ai/9w,  jav.  aem  (nach  ahdm  ,ich'  erweitertes  ar. *ai  =  idg.  *ei;  idg.  *ei  vom  St.  e-,  wie  *quo-i  vom  St.  kuo-^  nicht  Hoch- stufe zu  i-);  ai.  iddm  ,id'  (ohne  die  sekundäre  -aw-Erweiterung  ai.  ü^  av. it  als  hervorhebende  Partikel),  ai.  iydm  (erweitert  aus  *l-)  =  av.  Im  (d.  i. lyam),  apers.  iyam  ,sie,*  ea',  Akk.  Sg.  m.  ai.  imdm  (erweitert  aus  *im)  == apers.  imam  (darnach  f.  imäm  usw.).  Gen.  m.  n.  asyd,  dsya  =  av.  ahe, fem.  ai.  asydh  =  av.  aii^hä,  Dat.  m.  n.  asmäi,  dsmäi  =  av.  ahmäi,  Gen. PI.  m.  n.  esäm  =  av.  aesqm,  Dat.  Abi.  PI.  m.  ai.  ebhydh  =  av.  aeibyö usw.;  gthav.  asl-^it],  9  je  einmal  n.  Sg.  m.;  vom  St.  ä-  PL  fem.  Gen.  ai. äsäm  =  av.  är<fham,  Dat.  Abi.  äbhydlj.  =  av.  äbyö  usw.
```


## [2026-09-06T15:20:24.015Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=4023 && NR<=4110' POK_01.txt | grep -n -E \"aeta|ai-ta|oino|oi-no|^28[0-9]$|ains|ainaz|unus|einn\" | head -30"
}
```


### [2026-09-06T15:20:25.654Z] TOOL RESULT

```
1:281
27:283
43:284
58:285
73:286
76:ai.  e-^ä,  e-§ä,  e-tdt,  av.  aesa-,  aeta-  ,der  da'  (*ei-so,  -to-,  während  arm.  aidsL *äi-to-,  s.  oben;  osk.  umbr.  eiso-,  ero-  dag-egen   aus  dem  Gen.  PL  *ei5ö„^H!
80:oi-nos:  ai.  e-na-  ,er'  (kann  auch  *ei-no-  sein);
81:arm.  -in  der  Identitätsadverbia  andren  ,ebendort*,  asten  ,ebenhier',  viel, leicht  auch  der  Identitätspronomina  so-in  , derselbe  hier',  do-in  , derselbe da',  no-in  .derselbe  dort'  (,gerade  der.  ein  und  derselbe^;  *oino-s  zunächst zu  en,  noch  in  der  Bedeutung  ,(iott',  d.  h.  ,der  eine',  und  in  so-in  usw.  zu -in  geschwächt,  Junker  KZ.  43,  3^2;  für  so-in  erwägt  er  auch  *ko- -}- ^nos)' anders  Meillet  Esquisse  88;
85:got.  ains,  ahd.  ein,  anord.  einn  (hierher  gehört  altnord,  einka  , besonders^ und  weiter  ekkja  , Witwe',  ekkill  , Witwer');
86:apr,  ains  (f.  aina)  ,ein',  ablaut.  h't,  ynas  und  Inas  , recht,  wirklich'* daneben  mit  präfig.  Partikel  (V) :  •  v*t
88:aksl.  im  ,unus'  und  ,alius',  ino-rogz  .Einhorn',  v^  ing  ,in  einem  fort, immer',  inokh  ,solus'  ( =  got.  ainaha  , einzig",  lat.  ünicus,  anord.  einga, ags.  änga,  ahd.  einac,  as.  enag,  nhd.  einig),  woneben  aksl.  jed-im  (zum 1.  Glied,  wohl  id«:.  *ed,  s.  oben)  ,pin',  woraus  durch  Kürzung  in  längeren Flexionsformen  z.  B.  jednogo  (gesclirieben  jedtnogo).  russ.  odiivb,  odnogo.    '  .',.,^
```


## [2026-09-06T15:20:35.596Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=4095 && NR<=4112' POK_01.txt | cut -c1-1200"
}
```


### [2026-09-06T15:20:37.359Z] TOOL RESULT

```
286
9
D.  Zusammensetzungen  und  Ableitungen   (soweit   nicht  oben  ei gereiht) :
ai.  e-^ä,  e-§ä,  e-tdt,  av.  aesa-,  aeta-  ,der  da'  (*ei-so,  -to-,  während  arm.  aidsL *äi-to-,  s.  oben;  osk.  umbr.  eiso-,  ero-  dag-egen   aus  dem  Gen.  PL  *ei5ö„^H!
(m)arm.  i-sa,  i-ta,  i-na  Dem  in.  aus  *ei-ko-,  -to-,  no-  (Junker  KZ.  43  346f  yvil'
ai.  e-vd,  e-vd-m  ,so',  wozu  mit  der  Bedeutungs-Entw.  ,gerade  s6,  0^,-3^^*^^ der  —  nur  der  —  der  allein,  der  eine';
av.  aeva-,  apers.  aiua-  ,ein,  einzig,  allein*,  gr.  olog,  kypr.  olj=og  .allein' (idg.  *ome,  *qiuos);  s.  auch  oben  S.  75,
oi-nos:  ai.  e-na-  ,er'  (kann  auch  *ei-no-  sein);
arm.  -in  der  Identitätsadverbia  andren  ,ebendort*,  asten  ,ebenhier',  viel, leicht  auch  der  Identitätspronomina  so-in  , derselbe  hier',  do-in  , derselbe da',  no-in  .derselbe  dort'  (,gerade  der.  ein  und  derselbe^;  *oino-s  zunächst zu  en,  noch  in  der  Bedeutung  ,(iott',  d.  h.  ,der  eine',  und  in  so-in  usw.  zu -in  geschwächt,  Junker  KZ.  43,  3^2;  für  so-in  erwägt  er  auch  *ko- -}- ^nos)' anders  Meillet  Esquisse  88;
gr.  olyog,  oivrj  ,eiiis  auf  dem  Würfel*;
lat.  ünus,  alt  olnos]
air.   öen   ,ein';   cymr.   bret.  corn.  un  ,ein   (auch   unbestimmter   Artikel)'-
got.  ains,  ahd.  ein,  anord.  einn  (hierher  gehört  altnord,  einka  , besonders^ und  weiter  ekkja  , Witwe',  ekkill  , Witwer');
apr,  ains  (f.  aina)  ,ein',  ablaut.  h't,  ynas  und  Inas  , recht,  wirklich'* daneben  mit  präfig.  Partikel  (V) :  •  v*t
lit.  vienas,  lett.  viens  ,ein'  (wegen  lit.  vicoeinelis  .ganz  allein'  aus  *einö8\^ ablaut.  lett.  vin.^  ,er'  {^viiiias'^  vgl,  skr.  In  aus  *eino-)]  s.  Trautmann  3,  • Endzelin  Lett.  Gr.  356,  381  f.  'Zi
aksl.  im  ,unus'  und  ,alius',  ino-rogz  .Einhorn',  v^  ing  ,in  einem  fort, immer',  inokh  ,solus'  ( =  got.  ainaha  , einzig",  lat.  ünicus,  anord.  einga, ags.  änga,  ahd.  einac,  as.  enag,  nhd.  einig),  woneben  aksl.  jed-im  (zum 1.  Glied,  wohl  id«:.  *ed,  s.  oben)  ,pin',  woraus  durch  Kürzung  in  längeren Flexionsformen  z.  B.  jednogo  (gesclirieben  jedtnogo).  russ.  odiivb,  odnogo.    '  .',.,^
Mit  Formans  -ko-  (wie  ai.  dvlkd  .aus  zweien   bestehend*)  ai.  eka-  ,unus*,  „.rJ] ekatiya    ,der    eine",    urind.    (im   hitt.   Text)    aika-vartana    ,eine    Drehung* (Kretschmer  KZ,  55,  93);  über  lat,  ünicus,  got.  ainaha,  aksl.  inok^  s.  oben.
Mit  Formans  -go-  got.  aina kls  ,allein.stehend"  (auch  oben  anord.  einka usw.),  ksl.  inog^  ,y,ovio^,  VQ^Hf' '^  s.  Feist  22  f.
```


## [2026-09-06T15:20:45.810Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD oi-no\"; grep -n -i -A15 '^oi-no' AHD_watkins1985.txt | head -60; echo \"=== AHD i- pronominal\"; grep -n -B2 -A20 'Pronominal stem' AHD_watkins1985.txt | head -80"
}
```


### [2026-09-06T15:20:45.880Z] TOOL RESULT

```
=== AHD oi-no
=== AHD i- pronominal
557-gyeu-. Also geu-. To chew. Germanic *kewwan in Old English céowan, to chew: CHEW. [Pok. g(iJeu- 400.]
558-[hulé. Forest, timber, hence stuff, matter. Greek noun of unknown origin. -YL, YLEM; HYLOZOISM, METHYLENE.]
559:i-. Pronominal stem. 1. Germanic *is-lik-, same (*lik-, like; see lik-), in Old English ilca, same: ILK. 2. Germanic *jaino-, *jeno-, in Old English geon, that: Yon. 3. Ger- manic *jend- in Old English geond, as far as, yonder: YOND, (YONDER). 4. Extended forms *ydm, *ydi, in Ger- manic */d, *jai, in Old English géa, affirmative particle, and gése, yes (see es-): YEA, YES. 5. Old English giet, gieta (preform uncertain), still: yET. 6. Old English gif (preform uncertain), if: 1F. 7. Basic form *i-, with neuter *id-em, in Latin is, he (neuter id), and idem, same: 1D, IDEM, (IDENTICAL), IDENTITY; (IDENTIFY). 8. Suffixed form *i-tero- in Latin iterum, again: ITERATE; (REITER- ATE). 9. Suffixed and extended form ‘*iéa)-em in Latin item, thus, also: ITEM. 10. Suffixed variant form *e-tero- (see ko-). [Pok. 3. e- 281.]
560-ka-. To like, desire. Contracted from *kaa-. 1. Suffixed form *kd-ro- in: a. Germanic *héraz (feminine *hérén-), “one who desires,” adulterer, in (i) Old English hére, whore: WHORE (ii) Old Norse compound hérdémr, whore- dom (-démr, “condition”; see dhé-'): WHOREDOM; b. Latin cdrus, dear: CARESS, CHARITY, CHERISH. 2. Suf- fixed form *kd-mo- in Sanskrit kdmah, love, desire: Kama; KaMAsuTRA. [Pok. kd- 515.]
561-kad-. To fall. Latin cadere, to fall, die: CADAVER, CA- DENCE, CADENT, CADUCOUS, CASCADE, CASE!, CHANCE, CHUTE; ACCIDENT, CADUCICORN, DECAY, DECIDUOUS, ESCHEAT, INCIDENT, OCCASION, RECIDIVISM. [Pok. 1. kad- 516.]
562-kad-. Sorrow, hatred. Suffixed zero-grade form *kad-i- in: a. Germanic *hatiz in Old English hete, hate, envy (> Middle English hate): HATRED. b. Germanic *haton in Old English hatian, to hate: HATE; c. Germanic *hatjan in Old French hair, to hate: HEINOUS. [Pok. kdd- 517.]
563-kadh-. To shelter, cover. 1. Suffixed zero-grade form *kod-u- in Germanic *haduz in expressive form *hattuz in Old English Azxt(t), hat: HAT. 2. Basic form *kddh- in: a. Germanic *hdéda in Old English hdd, hood: HoopD!;
564-kamp-
565-b. Germanic *hédjan in Old English hédan, to heed, care for, protect: HEED. [Pok. kadh- 516.]
566-kae-id-. To strike. 1. Latin caedere, to cut, strike: CAE- SURA, CEMENT, CESTUS2, CHISEL, -CIDE, SCISSORS; AB- SCISE, CIRCUMCISE, CONCISE, DECIDE, EXCISE2, INCISE, PRECISE, RECISION. 2. Latin caelum (? < *caedum), sculptor’s chisel: CAELUM. [Pok. (s)k(h)ai- 917.] kagh-. To catch, seize; wickerwork, fence. 1. Germanic *hag- in: a. Old French hagard, wild, wild hawk (< “raptor”): HAGGARD; b. Germanic *hagén- in Old Eng- lish haga, hedge, hawthorn: HAW?; c. Germanic *hagj6é in Old English hecg, hedge: HEDGE. 2. Suffixed unaspirated form *kag-yon- in Gaulish caio, rampart, retaining wall (> Old French quai, quay): (CAY), KEY?, QUAY. 3. Possi- ble variant *kogh- in: a. Latin cohum, strap from yoke to harness: INCHOATE; b. possibly Latin cdlum, sieve (< wickerwork), and its derivative céldre, to filter: COLAN- DER, COULEE, (COULOIR), CULLIS; PERCOLATE. [Pok. kagh- 518.]
567-kaghlo-. Pebble, hail. Germanic *haglaz in Old English hagol, hxgel, hail: HAIL}. [Pok. kaghlo- 518.]
568-kai-. Heat. Extended form *kaid- in: a. Germanic *haitaz in Old English hat, hot: HoT; b. Germanic *haiti- in Old English h&tu, heat: HEAT. [Pok. kdi- 519.]
569-kaiko-. One-eyed. Latin caecus, blind: CAECILIAN, CAE- cum. [Pok. kai-ko- 519.]
570-kailo-. Whole, uninjured, of good omen. 1. Germanic *hailaz in: a. Old English Adal, hale, whole: HALE!, WHOLE; b. Old English *halsum, wholesome (> Middle English holsom): WHOLESOME; c. Old Norse heill, healthy: (HAIL?); WASSAIL. 2. Germanic *hailithé in Old English h#ith, health: HEALTH. 3. Germanic *hailjan in Old English h&lan, to heal: HEAL. 4. Germanic *hailagaz in: a. Old English hdlig, holy, sacred: HOLY; b. Germanic derivative verb *hailagén in Old English hdlgian, to consecrate, bless: HALLOW. [Pok. kailo- 622.]
571-kaito-. Forest, uncultivated land. 1. Germanic *haithiz in Old English A&th, heath, untilled land: HEATH. 2. Ger- manic *haithinaz in: a.Old English h@then, heathen, “savage” (< “one inhabiting uncultivated land”): HEA- THEN; b. Middle Dutch heiden, heathen: HOYDEN. [Pok. kaito- 521.]
572-kak-'. To enable, help. Sanskrit saknoti, he is able, he is strong: SHAKTI, SIKH. [Pok. kak- 522.]
573-[kak-2. A round object, disk. Germanic root. 1. Old Norse kaka, cake: CAKE. 2. Middle Dutch koeke, a cake: cooky. 3. Middle Low German koéke, cake: COCKAIGNE. 4. Old High German kuocho, cake: KUCHEN, QUICHE. [In Pok. gag- 349.]]
574-kakka-. Also kaka-. To defecate. Imitative root. 1. Old Norse *kiika, to defecate, akin to the source of Middle English cukken, to defecate: CUCKING STOOL. 2. Latin cacGre, to defecate: POPPYCOCK. 3. Greek kakos, bad: CACO-; CACODYL, CACOETHES, CACOPHONOUS, CACOPH- ony. [Pok. kakka- 521.]
575-kal-'. Cup. 1. Suffixed zero-grade form *l-ik- in: a. Latin calix, cup, goblet: CALIX, CHALICE; b. Greek kulix, cup: KYLIX. 2. Suffixed zero-grade form *kl-uk- in Greek kalux, seed-vessel, cup: CALYX. [Pok. 7. kel- 550.]
576-kal-2, Beautiful. 1. Suffixed form *kal-wo- in Greek kalos, beautiful: CALLISTO; CALOMEL, CALOYER, KALEIDO- SCOPE. 2. Suffixed form *kal-yo- in Greek kallos, beauty: CALLIGRAPHY, CALLIOPE, CALLIPYGIAN. [Pok. 2. kal- 524.]
577-kal-3. Hard. 1. Latin callum, hard skin: (CALLOSE), CAL- LOUS, CALLUS. 2. Celtic *kal-eto- in Welsh caled, hard, in Caledvwich, Excalibur: EXca.iBur. [Pok. 1. kal- 523.]
578-kamer-. To bend; a vault. 1. Greek kamara, a vault: (CABARET), CAMARILLA, (CAMERA), CHAMBER, (COM- RADE); (BICAMERAL). 2. Persian kamar, waist, girdle, oat something arched: CUMMERBUND. [Pok. kam-er- 524.
579-kamp-. To bend. 1. Suffixed form *kamp-dé in Greek kampé, a bending, a winding: (GAM2), (GAMBADO2), (GAM-
--
1055-swesor-. Sister. 1. Zero-grade form *swesr- in: a. Ger- manic “swestr- in Old English sweostor, sister: SISTER; b. suffixed form *swesr-ino- in Latin sobrinus, maternal cousin: COUSIN. 2. Latin soror, sister: SORORAL, SOROR- ITY. [Pok. suesor 1051.]
1056-swi-. To be silent. Expressive formation in Greek sidpé, silence: APOSIOPESIS. [Pok. sui- 1052.]
1057:swo-. Pronominal stem; so. Derivative of s(w)e-. 1. Ger- manic *swa- in: a. Old English swd, so: sol; b. Germanic compound *swa-lik-, “so like,” of the same kind (*/ik-, same; see lik-), in Old English swylc, such: sucH. 2. Ad- verbial form *swai in Latin si, if, in quasi (quam, as; see kWo- + si, if): NISI, QUASI. [In Pok. 2. seu- 882.] s(w)okwo-. Resin, juice. Variant form *sokvo- in Greek opos (< *hopos), juice: opruM. [Pok. s(wekvo-s 1044.] swombho-. Spongy. Germanic *swamba- in: a. Middle Low German sump, swamp: SUMP; b. Low German zwamp, swamp, akin to the Low German source of swamp. [Pok. suomb(hjo-s 1052.]
1058-swordo-. Black, dirty. 1. Germanic *swartaz in Old English sweart, swarthy: swaRT. 2. Zero-grade suffixed (stative) form *swrd-é- in Latin sordére, to be dirty: SORDID. [Pok. suordo-s 1052.]
1059-syi-. To bind, sew. I. Basic form *syi- in Germanic
1060-ta-
1061-*siwjan in Old English seowian, siowan, to sew: SEW. Il. Variant form *sd-. 1. Germanic *sawmaz in Old Eng- lish séam, seam: SEAM. 2. Latin suere (past participle stitus), to sew: SUTURE; COUTURE. 3. Suffixed form *sa-dhla- in Latin sibula, awl (< “sewing instrument”): SUBULATE. 4. Suffixed form *si-tro- in Sanskrit siitram, thread, string: suTRA; KamasuTRA. 5. Suffixed short- ened form *syu-men- in Greek humén, thin skin, mem- brane: HYMEN. [Pok. sii- 915.]
1062-ta-. To melt, dissolve. 1. Extended form *tdw- in Ger- manic *thdw6n in Old English thdwian, to thaw: THAW. 2. Extended form *tabh- in Latin tabés, a melting, wasting away, putrefaction: TABES. 3. Extended form *tak- in Greek tékein, to melt: EUTECTIC. [Pok. td- 1053.]
1063-tag-. To touch, handle. 1. Nasalized form *ta-n-g- in Latin tangere, to touch (> taxdre, to touch, assess, and tactus, touch): TACT, TANGENT, TANGIBLE, TASTE, TAX; ATTAIN, CONTACT, INTACT, TACTORECEPTOR, TANGORE- CEPTOR. 2. Compound form *n-tag-ro-, “untouched, intact” (*n-, negative prefix; see ne), in Latin integer, intact, whole, complete, perfect, honest: ENTIRE, INTE-
1064-GER. 3. Suffixed form *tag-smen- in Latin contémindre, to corrupt by mixing or contact (< *con-témen-, “bring- ing into contact with”; con-, com-, with; see kom): CONTAMINATE. [Pok. tag- 1054.]
1065-tag-. To set in order. Suffixed form *tag-yo- in Greek tassein, tattein, to arrange, and taxis (< *tag-ti-), ar- rangement: TACTICS, TAXIS, -TAXIS, TAXO-; ATAXIA, HY- POTAXIS, PARATAXIS, SYNTAX. [Pok. tdg- 1055.]
1066-tak-'. To be silent. Suffixed (stative) form *tak-é- in Latin tacére, to be silent: TACET, TACIT; RETICENT. [Pok. tak- 1055.]
1067-[tak-2. To take. Germanic root. Old Norse taka, to take: TAKE; WAPENTAKE.]
1068-[tap-. Germanic base of various loosely related deriva- tives; “plug, wad, small compact object, projecting part; to plug, strike lightly.” Variants *tap-, *tapp-, *topp-, *tupp-. 1. Old English teppa, spigot: TAP. 2. Dutch tap, spigot: TATTOO!. 3. Old French tampon, plug: TAMPON. 4. Old French taper, to strike lightly: TAP!. 5. Old Eng- lish top, summit: ToP!. 6. Old English top, a child’s plaything, perhaps a spinning top: ToP?. 7. Old French toup, top, tuft of hair: TOUPEE. 8. Old Norse typpi (> Middle English tip), end: TIP!. 9. Old French tof(fe, tuft: TUFT. 10. Old English téppe, strip of cloth: TAPE.]
1069-tauro-. Bull. Derivative of sta-, but an independent word in Indo-European. Greek tauros (> Latin taurus), bull:
1070-TAURINE!, TAURINE?, TAURUS, TOREADOR, TORERO, TAU- ROCHOLIC ACID. [In Pok. ¢éu- 1083.]
1071-[taw-. To make, manufacture. Germanic root. 1. Ger- manic *taw- in Old English tow-, spinning (only in compounds such as tow-hiis, spinning house or room): Tow. 2. Germanic *tawjan, *taw6dn, to fashion, in Old English tawian, to prepare: TAW!. 3. Germanic *gatawja- (*ga-, collective prefix; see kom), equipment, in Old English geatwa, geatwe, equipment: HERIOT. 4. Ger- manic variant *t6(w)lam, implement, in Old English ol, implement (possibly borrowed from the cognate Old Norse ¢6/): TOOL. [In Pok. 2. deu- 218.]]
1072-tegu-. Thick. Germanic *thiku- in Old English thicce, thick: THICK. [Pok. tegu- 1057.]
1073-tek-. To beget, give birth to. 1. Suffixed form *tek-no-, child, in: a. Germanic *thegnaz, boy, man, servant, warrior, in Old English thegn, freeman, nobleman, mili- tary vassal, warrior: THANE; b. possibly Germanic *the- wern6, girl, in Old High German thirona, diorna (> German Dirne), girl: DIRNDL. 2. Reduplicated form *ti-tk-, metathesized in Greek tiktein, to beget, and suffixed o-grade form *tok-o- in Greek tokos, birth: OXYXTOCIC, POLyTocous, TocoLocy. [Pok. 1. tek- 1057.]
1074-teks-. To weave; also to fabricate, especially with an ax; also to make wicker or wattle fabric for (mud-covered) house walls. 1. Latin texere, to weave, fabricate: TEXT,
1075-TISSUE; CONTEXT, PRETEXT. 2. Suffixed form *teks-/é in:
1076-69
1077-temp-
```


## [2026-09-06T15:20:51.775Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"ONION|OUNCE|Uniform, one\\.|oi-no\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T15:20:51.833Z] TOOL RESULT

```
<persisted-output>
Output too large (32.3KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bpov22uf6.txt

Preview (first 2KB):
127:complete agreement on the numerals from two to ten: dwo- (*duw6), trei- (*treyes), kvetwer- (*k”etwores), penk”e, s(w)eks, septm, oktd(u), newn, dekm. For the nu- meral “one” the dialects vary. We have a root sem-' in some derivatives, while the western Indo-European languages Germanic, Celtic, and Latin share the form oi-no-. The word for “hundred,” formed from dekm, “ten,” was *(d)kmtom. No common form for “thousand” or any other higher number can be reconstructed for the protolanguage.
492:TION), GENERIC, GENEROUS, GENRE, GENUS; CONGENER, (CONGENIAL), DEGENERATE, (ENGENDER), MISCEGENA- TION; b. Greek genos and genea, race, family: GENEAL- OGY, GENOCIDE, GENOTYPE, HETEROGENEOUS; c. Greek suffix -genés, ‘‘-born’”: -GEN, -GENY. 4. Suffixed full-grade form *gen-yo- in: a. Latin genius, procreative divinity, inborn tutelary spirit, innate quality: GENIAL!, GENIUS; b. Latin ingenium (in-, in; see en), inborn character: ENGINE, INGENIOUS. 5. Suffixed full-grade form *gen-d- in Latin indigena (indu-, within; see en), born in (a place), indigenous: INDIGEN, (INDIGENOUS). 6. Suffixed full-grade form *gena-wo- in Latin ingenuus (in-, in; see en), born in (a place), native, natural, freeborn: INGENUOUS. 7. Suffixed full-grade form *gen- men- dissimilated in Latin germen, shoot, bud, embryo, germ: GERM, GERMAN?, (GERMANE), GERMINAL, GERMI- NATE. 8. Suffixed full-grade form *gena-ti- in Greek genesis, birth, beginning: GENESIS, -GENESIS. 9. Redupli- cated form *gi-gn- in: a. Latin gignere (past participle genitus), to beget: GENITAL, GENITIVE, GENITOR, GENT!, (GINGERLY); CONGENITAL, PRIMOGENITURE, PROGENI- TOR, (PROGENY); b. Greek gignesthai, to be born: EPI- GENE. 10. Suffixed zero-grade form *-gn-o- in Latin benignus (bene, well; see deu-?), good-natured, kindly, and malignus (male, ill; see mel-5), evil-natured, malevo- lent: BENIGN, MALIGN. 11. Zero-grade form *gna- becom- ing *gnda- in Latin praegnds (prae-, before; see per’), pregnant: PREGNANT!. 12. Suffixed zero-g
...
</persisted-output>
```


## [2026-09-06T15:20:55.677Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -m2 -E \"^oi-no-\" AHD_watkins1985.txt; grep -n -o -E \"oi-no-\\..{0,1600}\" AHD_watkins1985.txt | head -3"
}
```


### [2026-09-06T15:20:57.821Z] TOOL RESULT

```
127:oi-no-. The word for “hundred,” formed from dekm, “ten,” was *(d)kmtom. No common form for “thousand” or any other higher number can be reconstructed for the protolanguage.
795:oi-no-. One, unique. I. Basic form *oi-no-. 1. Germanic *ainaz in: a. Old English dn, one: A1, AN!, ONCE, ONE; (ALONE), ANON, (ATONE), (LONE), (LONELY), NONE; b. compound *ain-lif-, “one left (beyond ten),” eleven (*lif-, left over; see leikw-), in Old English endleofan, eleven: ELEVEN; Cc. Old High German ein, one, in Ger- man vereinen, to unite: EINKORN, TURNVEREIN. 2. Latin anus, one: INCH}, OUNCE!, UNCIAL, UNI-, UNION, UNITE, UNITY; COADUNATE, QUINCUNX, TRIUNE, UNANIMOUS, UNICORN, UNIVERSE. 3. Latin ndn, not (< *ne-oinom, “not one thing”; ne, not; see ne). II. Suffixed form *oino-ko- in: a. Germanic *ainigaz in Old English &nig, one, anyone: ANY; b. Latin dnicus, sole, single: UNIQUE. III. Suffixed form *oino-lo- in Latin dllus, any (see ne). [In Pok. e- 281.] oito-. An oath. Probably derived from ei-1. Germanic *aithaz in: a. Old English dth, oath: OATH; b. Old High German eid, oath, in German Eidgenosse, confederate: Hucuenor. [In Pok. 1. ei- 293.] okt6(u). Eight. 1. Germanic *ahté in: a. Old English eahta, eight: EIGHT; b. Old Norse ditjan (tjan, ten; see dekm), eighteen: ATTO-. 2. Latin octé, eight: OcTANS, OCTANT, OCTAVE, OCTAVO, OCTET, OCTO-, OCTOBER, OCTONARY; OCTODECIMO, OCTOGENARIAN. 3. Greek okt6, eight: OcTAD; ocTopus. [Pok. okt6 775.]
```


## [2026-09-06T15:21:08.361Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\n\" 2>/dev/null; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['KNT','SNS','GPL','SOD','MON','BQT','TZF']:\n  print(k, json.dumps(d[k],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-06T15:21:10.320Z] TOOL RESULT

```
KNT {
 "title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953",
 "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/oldpers",
 "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt",
 "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.",
 "notes": "",
 "cites": "page number of Kent, Old Persian (1953); the lexicon starts p. 164"
}
SNS {
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
GPL {
 "title": "J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911",
 "edition_found": "1911",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/grammarofpersian0000plat",
 "identifier": "grammarofpersian0000plat",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt",
 "page_offset": "leaf = printed + 12 (e.g. leaf 17 = p.5). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Grammar organised by numbered paragraphs (§); grep the paragraph number or the Persian word in transliteration.",
 "notes": ""
}
SOD {
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
MON {
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
BQT {
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
TZF {
 "title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994",
 "kind": "website",
 "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)",
 "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": false,
 "notes": "PDF exists but not downloadable without login."
}
```


## [2026-09-06T15:21:18.443Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==180 || NR==179 || NR==181 {print \"----- leaf idx (0-based) \" NR-1; print substr($0,1,3000)}' KNT.txt"
}
```


### [2026-09-06T15:21:20.713Z] TOOL RESULT

```
----- leaf idx (0-based) 178
 : hya : Dārayavauš : XS : руё : Haxdmanigiya : Mitra : mam : paluv
Nore то АНЬ: Probably the demonstrative imam stood before apadānam at the beginning, and other
155
phrases of the protective prayer may have stood at the end.
TRANSLATION oF Á?Hb: This palace, of stone in its column(s), Artaxerxes the Great King built, the son of Darius the King, an Áchaemenian. May Mithras protect me ...
A'Hc = Artaxerxes II, HAMADAN C. 1 baga : vazraka : Auramazda :hya : тайа : 2 baganam : һуа :imàm : bümim : ada : 3 һуа : avam : asmánam : ada : hya : martiya 4 m : айа : һуа : &y&tim : ада : martiyahy 5 & : hya : Artaxšaçām : XSm : akunaug : ai 6 vam : parünàm : XSm : aivam : parünàm : 7 framataram : ðātiy : Artaxšaçā : XS : va 8 zraka : XŠ : XSyinim : X8 : DHyünám :XS 9 : ahydya : BUya : adam : Darayavausahy 10 à : XShyà : риса : DarayavauSahya : Artax И Sacahya : XShya : puça : ArtaxSacahy 12 & : XSayarSahy3 : XShya : риса : Хау 13 arsahya : Dàrayavausahyà : XShya : p 14 uça : Dārayavaušahyā : Vištāspahyā : nā 15 ma : puça : Haxämanišiya :ðātiy : Artaxša 16 (à : XS : vagna : Auramazdaha : adam : XS :8 17 hyaya : BUyà : vazrak&yà : düraiy :a 18 piy : amiy : Auramazda : xSagam : manā : frába 19 ra : màm : Auramazda : pátuv : uta : xSaca 20 m : tyamaiy : frábara : матау : vilam TRANSLATION OF A?He: M. 1-7. A great god is Ahuramazda, the great- est of gods, ... (= A!Pa 1-8). 82. 7-15.... (= A'Sa D: I (am) ... (= A'8a 1-2), son of Hystaspes by name, an Achaemenian. §3. 15-20. Saith Artaxerxes the King: By the favor of Ahuramazda I am king in this great carth far and wide; Ahuramazda bestowed the kingdom upon me. Me may Ahuramazda protect, and the kingdom which he bestowed upon me, and my royal house.
A?P = ARTAXERXES ÍT or IIT, PeRSEPOLIS.
: Parsa :
: Мада :
3 iyam : Üvja :
4 iyam : Parfava :
8 iyam : Uvarazmiya 9 iyam : така
10 1yam.: Harauvatiya
1 iyam 2 iyam
156
11 zyam 12 iyam 13 iyam 14 iyam 15 iyam 16 iyam 17 iyam 18 iyam 19 iyam 20 iyam 21 lyam 22 may 28 туат 24 iyam 25 туат 26 1yam 27 iyam 28 туат
80 iyam
: Gataguiya : Gadiraya : : Hiduya
: Зака : haumavargà : : бакё : tigraxauda : : Babirus :
: ABuriya
: Атарӯуа
: Mudráya
: Arminiya
: Katpatuka :
: Spardiya
: Yauna :
: Saka : paradraiya : : Skudra :
: Yauna : takabará : : Putàya :
: KüSiya
20 шат: : Karka :
Maciya
OLD PERSIAN -
Notes то А?Р: 4 @ataguiya Smith, Hz.; if correct, for Galaguviya; or a wrong writing for Satagudaya or 8atagudiya, cf. Gk. Larraybdar, 4 There із an extra verti- cal hasta between the g* and the a in haumavarga. ? imy*, miswritten for илт,
TRANSLATION ОЕ А?Р:
1. This is the Persian. 2. This isthe Меде. 3. This is the Elamite. 4. This is the Parthian. [5-7. This is the Arian, the Bactrian, the Sogdian.] 8. This is the Chorasmian. 9. This is the Drangian. 10. This is the Arachosian. |
11. This is the Sattagydian. 12. This is the
----- leaf idx (0-based) 179
8. This is the Arab. 19. This is the Egyptian. 20. This is the Armenian.
21. This is the Cappadocian. 22. This is the Sardian. 23. This is the Ionian. 24. This is the Scythian across the sea. 25. This is the Skudrian. 26. This is the Petasos-Wearing Ionian. 27. This is the Libyan. 28. This is the Ethiopian. 29. This is the man of Maka. 30. This is the Carian.
A’Pa = ARTAXERXES III, PERSEPOLIS А, B, C, D. 1 Бара : vazraka : Auramazda : hya :' 2 упал : bümàm :adà : һуа :a 8 vam : asmünàm : ada : һуа : marti 4 yam : adi : hya : &yatàm : adi : mart ` 5 ihyà : һуа : mim : Агіахёаса : х$ауз 6 буа, : akunaus : aivam : parüvnàm :
[4
Т xšāyaðiyam : aivam : parüvnüm. 8 : framatàram : Вапу : Artaxsagà : 9 xšāyaðiya : vazraka : xsayaftya 10 :xšāyaðiyanām : хёйуабуа : 11 DHyünàm : xSayafiya : ahyàyà : BUyā : ada 12 m : Ártax faga : хёйуа | 13 буа : puça : Artaxsacd : Darayavau 14 š :xšāyaðiya : puça : Darayavaus : A 15 rtaxéacà : xSaya@iya : puça : ArtaxSa 16 cà : XSayarsa : хїйуайуа : puça : X 17 šayāršā : Dárayavaus : xšāyað 18 iya : puça : Darayavaus : Vistaspa 19 hyà : пата : риса : Vistaspahya : 20 ÁrSàma : пата : puça : Haxàmanisi 21 ya :08tly : ArtaxSacd : xSiyafh 22 ya : imam : ustašanām : aðaganām : ma 23 m : upd : mam : kartā : 0tiy : Arta 24 xSacd : xSayabiya : mam : Auramazda : 25 ша : Міга : baga : pàtuv : uta : ima 26 m : DHyaum : uta : tya : mam : kartā : Notes TO АЗРа: The text is arranged according to the line-divisions of copy a, with faithful representation of all orthographic errors; all four copies have identical orthography, though the line-divisions vary somewhat. 12 The translation of lines 12-20 is intended to show the anacoluthic use of the nominative forms; the passage is obviously intended to convey the same ideas as Аа 1-3. 2 For ир@ тат ‘in my titne’ (here emphatic, only, ав it is otiose), сї. Аза 4 [u]pà ArtalxSacdm] ‘in the time of Artaxerxes’. | TRANSLATION ОР A’Pa: 81. 1-8. ... (= DNa 1-4), who made me, : Artaxerxes, king, ... (= DNa 6-8). 4 82. 8-21. ... (= Аа 1): I am the son (of)' Artaxerxes the King, (of) Artaxerxes (who was) ` the son (of) Darius the King, (of) Darius (who was) the son (of) Artaxerxes the King, (of) Artaxerxes (who was) the son (of) Xerxes the King, (of) "Xerxes (who was) the son (of) Darius
, the King, (of) Darius (who was) the son of
Hystaspes by name, of Hystaspes (who was) the son (of) Arsames by name, an Achaemenian.
83. 21-3. Saith Artaxerxes the King: This stone Staircase was built by me in my time.
$4. 23-6. Saith Artaxerxes the King: Me may Ahuramazda and the god Mithras protect, and this country, and what was built by me.
INSCRIPTIONS ON WEIGHTS.
Wa = Darius, WEIGHT A.
1 П Кага 2 adam : Dara
TEXTS WITH NOTES AND TRANSLATION
3 yavaus : xš 4 dyabiya : va 5 zraka : Vis 6 tàspahyà
7 : риса : Нах 8 amanisiya’
----- leaf idx (0-based) 180
d: LX (units) in weight.
‚.. (= Wb ЕЎ).-
157
INSCRIPTIONS ON SEALS SDa = Darius, SEAL A: adam : Darayavaus XS SDb = Darius, SEAL B: adam : Dàrayavaus
SXa = XERXES, SEAL A: 1 X Sayarsa 2: ХБ : vazraka SXb = XERXES, SEAL B: 1 adam : X Say
2 агба : XS SXc = Xerxes, Seat c: 1 adam : Xšayāršā : XS D mure Sa = SEAL A: 1 Arša 5 yüba 2 ka :n 6 ušna à ата: 7 hyä: ‚4 Adi 8 puça Sb = Sear B: 1 Hadaxaya PNE EE 9 Вадаба, : ...
Sc = SEAL c: Vasdasaka
Sd = белі р: Vahyavisdipaya
Se = SEAL E: 1 ma : Xa 2 га 3 dašyā
Sf = SEALF:lupà 2 Arta 3xSac 44am Notes: Se: For Justi’s reading Xifyáráü, see Lex.
s.v. Xaršadašyā. Sf: There is no word-divider after upd. TRANSLATION. OF THE SEALS:
SDa: I (am) Darius the King.
SDb: I (am) Darius. -
SXa: Xerxes the Great King.
SXb~c: I (am) Xerxes the King.
Sa: Arshaka by name, son of Athiyabaushna.
Sb-e: ???
Sf: Under Artaxerxes.
Vase INSCRIPTIONS.
XVs = XERXES, VASE: XSayar 84 : XS : vazraka AVsa = ARTAXERXES, VASE A:
: Ardaxeakea : XS : vazraka AVsb-d = ARTAXERXES, VASES B, C, D: ArtaxSaca : xSayabiya
TRANSLATION: XVs: Xerxes the Great King. AVsa: Artaxerxes the Great King. -
AVsb-d: Artaxerxes the King.
158
OLD PERSIAN
HISTORICAL APPENDIX |
I. THE ÅCHAEMENIAN DYNASTY
Darius and the other Persian Kings who have left us cuneiform inscriptions composed in Old Persian, all belonged to the Achaemenian line, so called because they were descended from Achaemenes. Full information may be found in PW 1.200-204 s.v. Achaimenidai, and under the names of the individual persons? a complete gene-
alogical table is given by PW facing 1.192. A table of the most important Achaemenians is given here; the names of the kings are in large and small capitals, with the dates of their reigns, and an asterisk marks those Achaemenians who are named in the Old Persian inscriptions.
Darius, in Behistan M, and again in Behistan
ACHAEMENES* | TEISPES* [ | CYRUS ARIARAMNES*
| | CAMBYSES ÅRSAMES*
| | Cyrus THE GREAT* Hystaspes*
559-29 ГА CamByses* Smerdis* 529-2
DARIUS THE GREAT* 521-486
XERXES [* 486-65 |
ARTAXERXES I Lonemmanus* 465-25
рте MEME
XERXES П
Artaxerxes 11 Mnemon* 405-359
SOGDIANUS Darius II Norgus* 425-4 424 424-05 po pes | Cyrus the Younger Artostes d. 401 | Arsames
Artaxerxes III Оснуѕ* 359-38
ARSES 888-6
|
Darius ПІ Copomannus 336-1
^ae rii rh E
TEXIS WITH NOTES AND TRANSLATION
a, States that there had been eight kings in their family before him, and that he was the ninth in order. We must count them thus: 1 Achaemenes, 2 Teispes, 3 Cyrus, 4 Cambyses, 5 Cyrus the Great, 6 Cambyses, 7 Ariaramnes, 8 Arsames, 9 Darius. The last three belong to the younger line of Áriaramnes, while Nos. 3 to 6 belong to the line of Teispes' older son. Hystaspes father of Darius is not included in the count, because he nowhere receives the title of King, even when mentioned as father of Darius—whereas the other kings all give to their fathers the title King in statements of parentage.
Herodotus 7.
```


## [2026-09-06T15:21:25.570Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"aiva\" KNT.txt | head -20"
}
```


### [2026-09-06T15:21:25.624Z] TOOL RESULT

```
122:І The Inscription and Sculptures of Darius the Great at Behistan.............. II The Gold Tablet of Hamadan ПІ The Daiva Inscription of Xerxes
1060:IIT. OP d from pIE d: pIE *deiyo- ‘deity’, OP daiva- (evil) god’, Av.
1768:Haraiva-, Haldita-.
1778:IIT. With no obvious simpler nominal or verbal form: ama- in Arsdma-, asa- aspa-, u-ba-, poss. ^upa-, kaufa-, kara-, daiva-, darga-, naiba-, Parsa-, pisa-, Máda-, raba- in u-rafa-, varka- in Varkána- and Varka-zana-, Saka-, späda- in Taxma-spáda-, spára- in Vdya-spara-; the restored hana- in hana- {й-; mayüra-, of uncertain etymology; the pos- sible vāra- in ^U-vára-zmi-.
1788:VI. The vocalism of the root varies in these for- mations, being either -a- (pIE -e- or -о- or -a-), as in baga-, bara-, daiva-; or à zero grade, as in karša-, u-zma-, darga- (see Lex. s.vv.); or a vriddhied or lengthened grade (§126), as in kdma-, asa-bāra-, Margava-.
1805:Expressing place: apa-dd-na-, daiva-di-na-, à- yada-na-, fem. us-tasa-nd-, d-vaha-na-, std-na-, varda-na-.
1981:Akaufaciya ‘Men of Akaufaka’; Unarazmiy and -miš ‘Chorasmia’; Gadára ‘Gandaritis’; 8ata- gu’ Sattagydia’; Рала ‘the Daae’; Maka or ethnic Maciya; Saka or fem. бака Scythia’ or Хака ‘the Scythians’; Sug(u)da ‘Sogdiana’; Haraiva ‘Aria’; Hidus Sind’.
3368:XPh = Xerxes, PERsEPOUIS н: The Daiva Inscription: Trilingual, on stone tablets, found in the building on the southeast corner of the ter- race; 2 OP copies, one complete in 60 lines, the other stopping in the middle of line 51; 1 Elam. сору in 50 lines, 1 АКК. copy in 50 lines. New York Times, Feb. 9, 1936; Univ. of Chicago Mag. 28.4.23-5 (Feb. 1936); EFSehmidt, Ill. London News, Feb. 22, 1936, page 328; Kent, JAOS 56.212-5 (1936); AfOF 11.91 (1936); Hz. AMI 8.56-77 (1936), RHRel. 113.21-41 (Jan.-Feb. 1936); HHartmann, OLZ 40.145-60 (1937) ; Kent, Lg. 13.292-305 (1937); Hz. Арі 27-35 No. 14 and Plates 10-3 (1938); Wb. Symbolae Koschaker 189-98 (1938; on the Elamite version); ILevy, Revue historique 185.105-22 (1939); EFSchmidt, 'The Treasury of Persepolis 12-5 (1939); Sen, OPI 148-56 (1941); VIAbayev, Hranskie Yazyki 1.134-40 (Izd. Ak. Nauk, Ҥашса vol. 3; Moscow- Leningrad, 1945).
3474:15 Qura : Arabaya : Mudraya : tyaiy : drayahya : Sparda : Yauna : Mada : Armina : Kat 16 patuka : Parfava : Zraka : Haraiva : Uvárazmiy : Bāxtriš : Suguda : Gadara : Sa
3861:71 ām : adam ; niyapaisam : imaiva : patikarà : mátya : vikandhy : yàvà : u
3871:77 yafiya : yadiy : imam : dipim : imaiva : patikarà : vaināhy : vikanah*dis : ut 78 ataiy : уйуй : tauma : ahatiy : natydiš : paribaráhy : Auramazdátaiy : jatà : b 79 iyā : ut&taiy : taumd : mà : biyá : uta : tya : kunav&hy : avataiy : Auramazd
4074:16 ka : Haraiva : Bāxtriš : Sug'da : Uv
4103:Tux Inscriptions or NaAQS-1-RugTAM. DNa = Darius, Nags-1-RustaMm A. 1 baga : vazraka : Auramazda : һуа : im 2 ām :bümtm :adà : hya : avam : asm 9 апат :adà : һуа : martiyam :adà : h 4 ya : Siyatim :adā : martiyahyà 5 :hya : D&rayavaum :xšāyaðiyam : ak 6 unau$ : aivam : parüvnàm : xSdyaé 7 iyam :aivam : parüvnàm : framátà 8 ram : adam : DarayavauS : xsayatiya : va 9 zraka : xSàyafiya : xSdyafiyanim 10 : xSdyaiya : dahyünàm : vispazaná 11 nam : х$йуайуа :abyáyà : шт ` 12 уа :уалаКауй : diiraiapiyf: Vistas 13 pahyà : puça : Haximanisiya : Parsa : P 14 àrsahyà : риса : Ariya : Ariya : ei 15 с̧а :0atiy : Darayavaus : xsaya 16 fiya : vašnā : Auramazdaha : ima : 17 dahyáva : {уй : adam : agarbáyam : 18 apataram : haeà : Ратѕа : adamsàm : 19 patiyaxSayaiy : manā : bàjim : abara 20 ha : tyasàm : hacdma :afahya :ava : a 21 kunava : dàtam : tya : mani : avadis : 22 adaraiya : Mada : Uvja : Parfava : Harai 23 va : Bàxtri$ : Suguda : Üvürazm 24 i$ : Zraka : Harauvatis : Gatagus : Ga 25 dara : Hidug : Saki : haumavargà : Sa 26 kā : tigraxaudà : Bābiruš : A 27 Gura : Arabàya : Mudràya : Armina
4214:DSe = Darius, Susa Е. 1 baga : vazraka : Auramazdà : hya : ima 2 т: bimim : adadé ; һуа : avam : as 3 татат : adadà : hya : martiyam : ad 4 ada : hya : &iyàülim : adad& : mart 5 iyahyü : hya : Darayavaum : XŠm : ak 6 unauš : айбат : parūvnām : XSm : a 7 шат : parüvnüm : framálàram : a 8 dam : Darayavaus : XS : vazraka : XS : XSy 9 anim : XS : dahyünám : vispazanü 10 nam : XS : ahyaya : bümiyà : vaz 11 rakàyà : düraiy : apiy : Vistas 12 pahyà : puça : HazamaniSya : Рат 13 sa : Pārsahyā : рисо : Ariya : Ari 14 ya : ciga : 08tiy : Dàrayavaus : XS : 15 уа&па : Auramazdaha : imá : dahy 16 āva : {уй : adam : agarbayam : apaia 17 ram : hacd : Parsa : adamsdm : pat 18 iyaxíayaty : manā : bajim : abara : 19 tyasam : hacéma : afahya : ava : aku 20 nava : datam : tya : mand : avadis : a 21 dáraya : Майа: Uja : Parðava : Haraiva : 22 Baatris : Suguda : Uvarazmis 23 : Zrdka : Наташайх : Bataguš : Maci 24 уй : Gadàra : Hidus : Зака : haumava 25 rgà : Saká : tigrazaudà : Babir 26 u$ : Авита : Arabéya : Мийгаа : 27 Armina : Katpatuka : Sparda : Yaun 28 à : аву : drayahya : ula : уа 29 y : paradraya : Skudra : Putayà : 30 Kuxiyd : Karka ; 6àtiy : Рата 31 yavau& : XS : vasiy : tya : duskarta 32 m : Gha : ava : naibam : akunavam : da 33 hyáva : ayauda : aniya : aniyam : 34 aja : ava : adam : akunavam : vašnā 39 : Auramazdaha : уаба : aniya : a 36 шуат : пау : jatiy : cind : gà 37 fava : kaSciy : astiy : дат : 38 tya : maná : haeá : avana : tarsat 39 y : улда : hya : tauviyd : tyam :s 40 kauéim : naiy : jatiy : naiy : vi 41 mardatiy : байу : Dérayavaus :
4239:4 yavaum : XSyam : akunauš : aivam ; parünüm : XS
4240:5 yam : aivam : parünàm : framátáram : adam : Dara
4330:7 Üja : BabiruS : Авита : Arabya : Mudrüya : Sparda : 8 Yauna : Майа: Armina : Katpatuka : Parbava : Zraka : 9 Haraiva : Uvürazmi$ : Báxtri& : Suguda : Gadára : 10 8atagut : Harawvati$ : Hidus : Skudra : Yound : taka
4418:7 hya : Dàrayavaum : xšāya 8 булаш : akunaus : aiva
4419:9 m : parünàm : х$йуа@ 10 iyam : aivam : parünàm 1l : framátàram : adam : 12 Dàrayavaus : xSdyaai 18 ya : vazraka : xSdya6tya : 14 xSiyaüryànàm : xà
4447:3 ada : hya : Syátim : ada : martiyahyà : һуа 4 : XSavarSim : xSiyafiyam : akunaué : aivam : 5 parünàm : xSayatiyam : aivam : parünàm : fram 6 àtàram : adam : XSayarsa : xSayafiya : vazraka : 7 xšāyaðiya : хёйуайїуйпаш : x&ayafiya : dahy _ 8 ünàm : paruv : zanànàm : хёйуадіуа : ahyay 9 & : bümlyà : vazrakáyà : düraiy : apiy : Da 10 rayavahaus : x&ayafiyahyà : риса : Haxémanis П iya : 0atiy : Xšayāršā : xšāyaðiya : vasna : 12 Auramazdáhà : imam : duvarfim : visadahyum 13 : adam : akunavam : vasiy : aniyascly : naibam 14 : kartam : апа : Parsi : tya : adam : akunavam : 15 utamaiy : tya : рія : akunaus : tyapatiy : ka 16 riam : vainataly : парага : ava : visam : vaSnà : А 17 uramazdaha : akumà : Qatiy : Xšayāršā : 18 xSayafiya : mam : Auramazda : pātuv : utamai 19 y : xSacam : ut& : tya : manā : kartam : uta : tyamai 20 y : pica : kartam : avaseiy : Auramazda : patuv
```


## [2026-09-06T15:21:29.775Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"aiva- |aiva-,\" KNT.txt | head; echo ===; grep -n \"LEXICON\" KNT.txt | head"
}
```


### [2026-09-06T15:21:29.833Z] TOOL RESULT

```
Exit code 1
1060:IIT. OP d from pIE d: pIE *deiyo- ‘deity’, OP daiva- (evil) god’, Av.
1768:Haraiva-, Haldita-.
1778:IIT. With no obvious simpler nominal or verbal form: ama- in Arsdma-, asa- aspa-, u-ba-, poss. ^upa-, kaufa-, kara-, daiva-, darga-, naiba-, Parsa-, pisa-, Máda-, raba- in u-rafa-, varka- in Varkána- and Varka-zana-, Saka-, späda- in Taxma-spáda-, spára- in Vdya-spara-; the restored hana- in hana- {й-; mayüra-, of uncertain etymology; the pos- sible vāra- in ^U-vára-zmi-.
(eval):1: == not found
```


## [2026-09-06T15:21:32.494Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=185 && NR<=190 {print \"----- leafidx \" NR-1; print substr($0,1,800)}' KNT.txt"
}
```


### [2026-09-06T15:21:34.445Z] TOOL RESULT

```
----- leafidx 184
I re- ject this interpretation of the series of sculptures, since it would oblige us to set the death of Frada at the very end of the series, dating his defeat not IX 23, 522/1, but IX 28, 521/0, and thus extending the series of events from 13 months 12 days to 14 months 13 days.
OLD PERSIAN
hered to Phraortes, declared himself King in Sagartia, a distriet of northern Media; he claimed to be of the family of Cyaxares. Darius sent а force of Medes and Persians under Takhmaspada, a Median officer, who defeated and captured Cicantakhma, bringing him to Darius. Darius mu- tilated him and put him to death with torture, at Arbela ($33). Thus ended rebellion in Media (884) ; but there was still a strong rebel force in Armenia, against which Darius sent an Armenian officer named Dadarshi. Dadarsh
----- leafidx 185
ugh not mentioned in the Behistan inscription, must have followed in the same or the next year.
V. THE ACCESSION OF XERXES.
In XPf, Xerxes gives us an account of his sue- cession to the throne: Darius had a number of sons, but—-as was Ahuramazda’s desire—he made Xerxes (presumably not his eldest son, though this is not stated in the inscription) the ‘greatest after himself; and when Darius ‘went from the throne,’ Xerxes—as was Ahuramazda's desire—became king on the throne of his father.
The account given by Herodotus 7.1-4 agrees with this, but gives more details: After Darius re- ceived the news that his forces had been defeated at Marathon and somewhat later that Egypt had risen in rebellion, he started preparations for one campaign against the Athenians and another again
----- leafidx 186
� asn. DPd 20; DNa 53; XPh 43, 59; XSc 4°. ata- таш DPd 22; DNa 54; XPh 60. aitä apf. XPh 30, 35.
Ainaira- sb. ‘Ainaira’, a Babylonian, father of Nidintu-Bel; Elam. ha-a-na-a-ra, АКК. a-ni-ri-’, Ainaliralhya gsm. DB 1.77f.
atva- adj. ‘one’ ($150; §204.1): Av. aéva- ‘one’, Gk. Hom. olos, Cypr. orros ‘alone’, pIE *ozyos. ашат, asm. DNa 6, 7; DSe 6°, 6f; DSf 4, 5; DE 8f, 10; XPa 4, 5; XPb 8f, 10; XPe 4, 5; XPd 6, 7; XPf 6, 7; XPh 5,6; XE 9, 10; XV 7, 8; A!Pa 6f°, 8°; A?He 5f, 6; А?Ра 6, 7.
aiš- vb. ‘hasten’, caus. azSaya- ‘send’: Av. aes-, caus. aéaya-, Skt. 15-, caus. esayatz (§117).
fra + aiš- caus. ‘send forth’: Av. fraei-, Skt. .
preg-. frdiSayam ist sg. imf. (§24, §72, 6181, §215) DB 1.82; 2.19, 30, 50, 72f, 82; 3.2, 18, 30, 84; 
----- leafidx 187
t built, unrepaired’; neg. a- + pte. of kar- ‘make’. {akarta] nsf. DSe 47 (conj. of Kent, JAOS 54.43).
azíaina- adj, with kdsaka-, ‘turquois’ (so Bleichsteiner, WZKM 37.103-4, and Konig, Burg- bau 63-4, but considered dubious by Hinz, ZDMG 95.235-6; hardly ‘gray amber’, with Hz. AMI 3.05—7, ApI 232; not ‘hematite’, with Scheil 21.29- 30): Av. arSaéna- ‘dark-colored’, borrowed in Gk. Порто “Atevos ‘Black Sea’ (‘in-hospitable’, by Gk. popular etymology, and euphemistically changed to Еф о), from neg. a- + z&atna-, cf. Av. xSaéta- ‘shining’ (§102, 5147.1). azšaina nsm. DSf 39.
axsata- adj. ‘unhurt, undisturbed’: neg. a- + pte. of xSan- ($102, §242.1), Skt. ksanóti ‘injures’, Gk. ктен, ‘kills’ (otherwise Foy KZ 35.49, Hz. Apl
----- leafidx 188
’, as taken by ТИМ. Aiw 322-3; otherwise Hz. Ap! 191-2: hadtya- ‘truth’, with late loss of h-, + deriv. of d-baud- ‘be fragrant’, cf. Av. baoót- ‘fra-
OLD PERSIAN
grance’, therefore ‘having the fragrance of the truth’).  <Aé@iydbausinahya gsm. Sa 4-7.
Aéura sb. ‘Assyria (and Syria)’, a province of the Persian Empire ($6, $106.11): Elam. aš- &i-ra, АКК. áš-šur, Gk. 'Аттурв‚ but Aram. абиг. Aéuré nsf. DB 1.14f; 2.7; DPe 11; DNa 26f; DSe 26°; DSm 7°; XPh 22. Aéurayd lsf. (5186) DB 2.58f.
A@uriya- adj. ‘Assyrian’: deriv. to preceding .
($144.1), perhaps with vriddhi in first syllable (8126; Aburiya- ?). A@uriya пет. DN xvii; DSf 32; А?Р 17.
Agina- sb. ‘Acina’, ап Elamite rebel: Elam. ka-iš-ši-na, Akk. a-Si-na. Either borrowed
----- leafidx 189
n., asn.); AÁuramazdü, АМ; ava (nsn.); avdkaram, avükaramca-; ucdram; uld, uta-; tya (nsn., asn.); dahydus; duvarayd; nat-; pati-; pasdva; уава; haw, hau-: Asl 12; DB 1.25 bis, 55, 87, 94; 2.24, 34, 40, 45, 54, 60, 68, 75, 79, 86, 90, 96; 3.6, 11, 17, 37, 441, 61, G6f, 87; 4.39, 46, 60, 64; DPd 28°; DPh 8, 10; DNa 50 (m° omitted, $52.VI), 52#, 544; DNb 13, 28, 28f, 31, 32f, 33, 48, 51, 52; DSe 51°, 52°; DSE 10, 19°, 20°, 58; Ds} 4°, 6°; DSk 5; DSI 4f; DSm 3°; D8s 7°; DSt 9°; DH 6, 8; Хра 15, 18f, 191; XPb 24, 29, 30; XPe 13 bis; ХРа 18f, 19; ХР 32, 38, 41, 45f, 47; XPg 14; XPh 32, 45, 58,
167
60; Хе 5° bis; XV 261°, 27°; A!Pa 23°, 24°: A’Sdb 4 (-may de, $52. VT); А?Не 20 bis.
-ma gsm. for -maty ($198.11); apan*yáka-ma А?За 3; [n"yà |kama for n*y
```


## [2026-09-06T15:21:46.650Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==187 {print}' KNT.txt | head -100"
}
```


### [2026-09-06T15:21:48.542Z] TOOL RESULT

```
� asn. DPd 20; DNa 53; XPh 43, 59; XSc 4°. ata- таш DPd 22; DNa 54; XPh 60. aitä apf. XPh 30, 35.
Ainaira- sb. ‘Ainaira’, a Babylonian, father of Nidintu-Bel; Elam. ha-a-na-a-ra, АКК. a-ni-ri-’, Ainaliralhya gsm. DB 1.77f.
atva- adj. ‘one’ ($150; §204.1): Av. aéva- ‘one’, Gk. Hom. olos, Cypr. orros ‘alone’, pIE *ozyos. ашат, asm. DNa 6, 7; DSe 6°, 6f; DSf 4, 5; DE 8f, 10; XPa 4, 5; XPb 8f, 10; XPe 4, 5; XPd 6, 7; XPf 6, 7; XPh 5,6; XE 9, 10; XV 7, 8; A!Pa 6f°, 8°; A?He 5f, 6; А?Ра 6, 7.
aiš- vb. ‘hasten’, caus. azSaya- ‘send’: Av. aes-, caus. aéaya-, Skt. 15-, caus. esayatz (§117).
fra + aiš- caus. ‘send forth’: Av. fraei-, Skt. .
preg-. frdiSayam ist sg. imf. (§24, §72, 6181, §215) DB 1.82; 2.19, 30, 50, 72f, 82; 3.2, 18, 30, 84; 5.7. frütsaya imf. DB 3.55, 60, 71.
Auliyüra- sb. ‘Autiyara’, a district in Ar- menia: Elam. ha-u-ti-ja-ru-i§, АКК. ú-ti-ņa-a-ri. Auliyàra nsm. DB 2.58f.
Aura- (Le. A*ura-) sb. ‘Lord, God’: Av. ahura-, Skt. dsura- ‘demon’, pIE *esuro- (6148.1). Aurahya Mazdaha gsm. ({36.ГУЬ, $44) XPe 10. Аита ism. DPe 24 (otherwise Bv. BSLP 30.1.70-3, Gr. §179, 8889; ‘downward’, isn. of aura-, zero- grade of avara-, comparative of *ava-, cf. Ау. aora ‘down’). Elsewhere always in cpd. Auramazdah-.
Auramazdāł- sb. ‘Wise Lord, Ahuramazda’, supreme deity of the Zoroastrian religion: Av. пет, ahurd mazda, РМ. óhrmazd, NPers. hormizd; Elam.. u-ra-más-da., Akky u-ra-ma-az-da. ü-ri-mt-
=
-
LEXICON
12-00 a-hu-ru-ma-az-da-’ ete., Gk. 'Opouacdys; in Av., always two words, usually separated in the Gathas and often in reverse order (Kent, Or. Stud. Hon. Pavry 200-8), but in OP always one word except ХРе 10 (844; for Ашт alone, see under Aura-). Cpd. of *ahura- (see Aura-) + *ma(n)dzdhà- with s-suffix (another! view by Pisani, ef. $185.n3); this is cpd. of pIE *menth- (or is the full grade pIE *math-?) seen in Gk. ёшабо› ‘I learned’, + pIE *dh&- ‘put’, see “da- (Pisani, Riv. Stud. Or. 81-2, takes prior element as *mns-, zero-grade to pAr. manas-, after Wacker- nagel-Debrunner, Altind. Gram. 3.282-3): for formation, ef. Skt. érad-dhà- ‘trust’, Lt. crédit. 670, $156.I, 5160.11; decl., $185.IV.
Auramazdà nsm. AmH 7, 10; AsH 5f, 12; DB 1.12, 60; 4.35, 55, 62, 74, 76, 79f; 5.15f; DPd 1, 7, 13, 15f, 23; DPh 8, 9; DNa 1, 31, 51f, 55; DNb 1, 46, 49: DSe 1; DSf 1,8, 14, 57; DSp 1; DSs 1^, 6f; DSt 1?, 7; DZe 1; DE 1; DH 6f, 8; XPa 1, 18, 20; XPb 1, 21; XPc 1, 12, 15; XPd 1, 17; XPf 1, 45, 48; XPg 12; XPh 1, 32, 49f, 52, 57, 60; XSc 4f°; XE 1; XV 1, 25; A!Pa 1°, 22°; A?8e 7; А?Не 1,18, 19; A?Pa 1, 24, Auramazdà-maiy DB 1.24f, 25, 55, 87, 94; 2.24, 34, 891, 45, 54, 60, 68, 86, 96; 3.6, 16f, 37, 44f, 61f, 661, 87; 4.60; DNa 50 -dà- iy, With omission of m* (§52.VI); DSf 19; XPh 45. Auramazdd-taiy DB 4.78. Auramazda-lay (852.11) DB 4.58. Auramazdd-|Sém] DB 5.311.
Auramazdàm asm. DB 1.54f (Auramazám, $52. VI); 5.16, 18f, 32, 34; DPd 211; DNa 54; DSf 15f, 18; XPf 211, 29; XPh 40, 50, 53, 59; XSe 4.
Auramazdéha gsm. AmH 7f; AsH 10; DB 111, 14, 18f, 22f, 26, 60, 68, 70, 88, 94f; 2.3, 25, 35, 40, АЎ, 54f, 60, 68, 86f, 97; 3.6f, 17, 38, 45, 62, 67, 87Ї; 44, 6, 41, 44, 46, 52, 60, 88; 5.16f, 32f; DSF 12, 21°; DSfv 55f°; D812f; XPb 26f; XPd 16; XPg 3,8; X881; XV19. | Auramazdáhà DPd 4,9; DPe 6f; DNa 16, 35, 49, 56{; DNb 6, 47f; DSe 15, 35, 42; XPa 12, 16f; А?Не 16. Auramazdahà (852.1II; $131; $185.IV) X Pf 34, 43; XPh 14, 33, 37, 44; A'Pa 18f.
AM nsm. (842) DSe 50°; DSi 3°; DS} 4, 6°; DSk 4; DSn 2^; D'Sa 3; A*Sa 4° (as gen., 5818.1), 4; A’Sd 3; А?На 5° (as gen), 6. АМташ DSk 5; D8m 3. AMm asm. DSk 4. AMha gsm. DSa 4; ligature ($42) DSk 4. AMha DS] 3°, 5; Аа 3. AMha or АМ№ DSd 3°; DSi 4°; DSm 5°; D8o 3°; D’Sb 4°.
165
Akaufaciya- adj. sb. ‘man of Akaufaka’; pl. a province of the Persian Empire: АКК. a-ku-pi-i-1$. Deriv. of * Akaufaka- ‘Kohistan’, prefix à + kaufa- ‘mountain’ + adj. suffix ($113, 814411; ef. Hz. AMI 8.72; Kent, Lg. 13.298-9). Akaufaciyd npm. XPh 27. |
akarta- adj. ‘not made, no
```


## [2026-09-06T15:21:55.778Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==54 {print substr($0,1,2500)}' GPL.txt"
}
```


### [2026-09-06T15:21:57.772Z] TOOL RESULT

```
the adjective precede the substantive the ی‎ or * of indefiniteness must be affixed to the noun; ۰.8. بندی دادی‎ ASS ‘good counsel hast thou given’; tS eB سکی‎ استخوانی می خورد‎ ‘a hungry dog was eating a dry bone’. Similarly, if the substantive is in the plural, it alone takes the زی‎ e.g. مردمانی خوب‎ ‘(some) good men’; بندگانی صادق‎ ‘ true (or loyal) servants’.
§ 39. Adjective used as a Subst. An adjective, whether Persian or Arabic, may be used substantively, and in that case it will be treated in every respect as a substantive; e.g. bls a learned man’; دانایان عصر‎ ‘the learned men of the age’; Jol» ‘an ignorant man’; yw ele ‘ignorant men’ ; بدهای آشعارش‎ ‘the bad things in (lit, of) his poems’,
In the rare cases which occur of a noun in the plural number in construction with what appears to be an adjective also in the plural it is generally considered that the ‘ adjective’ is used substantively in apposition. Such instances are—
Faithful servants بندگان مخلصان‎ Worldlywise sages asin پیران‎ Valiant heroes مردانن دلاوران‎
DEGREES OF COMPARISON §40 a. The comparative degree of adjectives (Persian or Arabic) is formed by adding the suffix ثر‎ tar to the positive, and the superlative by adding ین‎ in to the comparative ; e.g. ده‎ ‘good’, بهتر‎ ‘better’, بهترین‎ ‘best’; wo ‘bad’, بدتر‎ (generally contracted to بثر‎ battar, and often to بتر‎ batar) ‘worse’, بدترین‎ (contrac
```


## [2026-09-06T15:22:06.333Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i -E \"yazdah|yāzdah|eleven\" GPL.txt | head -10; echo \"=== hech\"; grep -n -i -E \"hech|hich|hīch\" GPL.txt | head -10; echo \"=== yak \"; grep -n -i -E \"\\bev[aā]k|yak\\b\" GPL.txt | head -10"
}
```


### [2026-09-06T15:22:06.415Z] TOOL RESULT

```
2573:b) The ordinals from eleventh to nineteenth are formed by adding the cardinal number عشر‎ ‘ten’ to the preceding ordinals, حادی‎ taking
2574:the place of J5l; as eleventh حادی عشر‎ (fem. زر (حادیه عشره‎ انی عشر‎ 3 and so on.
3155:These months are made to consist of 30 and 29 days alternately ; but in a period of 30 years, it is found necessary to intercalate the last month eleven times, so as to be reckoned 30 days instead of 29.
=== hech
38:In the portion of the book which treats of Arabic Grammar I have recast the paragraphs dealing with the Formation and Signification of the Derived Forms of the Arabic Conjugations.
42:felt at liberty to follow my own inclinations in the preparation of the portion of this work which deals with the Syntax of Persian.
43:The Series of Parallel Grammars by Mr. E. A. Sonnenschein seemed to me to be by far the most suitable model upon which to frame a Syntax of Persian, and a request made by me to that gentleman for permission to adopt his system in the execution of my task having met with a most courteous reception, I have made full, and, I hope, good use of the permission so graciously accorded me. I desire to tender my cordial thanks to him and to the publishers, Messrs. Swan Sonnenschein & Co., for allowing me to extend to Persian the system of treatment so ably and successfully inaugurated by them in the case of Greek and Latin.
44:The want of a systematic Syntax of Persian must have been long felt by others as it has by myself. For some reason no European scholar has hitherto attempted to systematise the syntactical structure of the Persian language, with the result that Persian has not met with the consideration it deserves as a medium for the expression of thought, and has been treated as though it were a mere vernacular with little or no claim to literary form or structural elegance. It is hoped that the present work may tend in some degree to remove that misconception, and to encourage the more critical study which the language so richly deserves.
46:In conclusion I desire to express my cordial thanks to the Delegates of the Clarendon Press for publishing this work, and for the extreme care and accuracy with which they have produced it.
121:§ 1. The alphabet of modern Persian consists of thirty-two letters, and the character in which these are written is the Arabic. Previous to the conquest of Persia by the Arabs, the Persian alphabet consisted of twenty-four letters, and the character used was the Pehlevi.t But after the Arab conquest, when the Persians came under the religion of Islam, they practically adopted the whole Arabic vocabulary, and, at the same time, the Arabic alphabet and characters. Thus eight more letters—letters peculiarly Arabic—were added to the original alphabet. Moreover, as four of the old Persian letters were unknown to the Arabic, a modified form of the Arabic character for the letter of the corresponding class was, in each case, given to these. The thirty-two letters so obtained are all considered as consonants, and are written and read from right to left. Several of them assume different forms, according to their position in the formation of a word or a combined group, as may be seen in the preceding Table, in which the letters peculiarly Persian are marked with an asterisk, and those peculiarly Arabic, with an obelisk.
127:1 Modern Persian is the language of Persia under Islam. Pehlevi was the language of Persia under the Sassanides, and is the direct parent of Persian. Old Persian was the language of Persia under the Achemenides—the language in which the inscriptions of the monarchs of that dynasty were written ; the character used was the cuneiform. The sister-language of the Old Persian was the Median, or (as it is commonly, though incorrectly, called) Zend. Pehlevi is a relative noun from pahlav = parthava (i.e. pehlert = parthaviya), and means ‘the language of the Parthava or Parthians’.
129:of a word or syllable it must necessarily be a consonant, and be accompanied by one of the short vowels. In Arabic, this alif is, except in a few instances, written with the mark * (called hamza) over it, e.g. {. The Persians drop this mark (+) at the beginning of a word, but generally retain it when it occurs at the beginning of a syllable in the middle of an Arabic word, e.g. sl5 ta-am-mul. As a matter of fact the Persians use this | simply as a prop to support the short vowel which accompanies it, and it is only when it occurs in the middle of a word, immediately preceded by a short vowel, that any effort of the throat in its pronunciation takes place, and, even then, the effort is so slight that it amounts to little more than a hiatus between the two short vowels.
149:& ‘, in Arabic, is a strong guttural. It is described as produced by a smart compression of the upper part of the windpipe and forcible emission of the breath. The Persians, however, make scarcely any distinction between it and the consonant ۱ al/f. It is simply pro- nounced with a slight trill; e.g. 12) baad; and when it begins a syllable in the middle of a word, there is (as in the case of alzf) a very perceptible pause and effort of the throat in the enunciation ; eg. ساعت‎ saat, 1285 daf-a, قلعه‎ gala. The رع‎ like |, takes its sound from the short vowel which accompanies it, and is represented by Ga, ts Nope
157:h, initial, medial, or final (especially after a long vowel), is an‏ ده aspirate like our A in hand, him. But at the end of a word, when‏ preceded by the short vowel fatha (§ 5, a), it is simply a prop for that‏ banda ‘slave’ 3 3315 dana ‘ grain’‏ کته vowel and is not sounded; e.g.‏ (in the transliteration of which the final silent & does not appear).‏ So also after the vowel kasra (§ 5, b), in the words ne ki, s> cht. The‏
=== yak 
319:6) When the singular ends in @ (\—) the letter ی‎ y is inserted (or restored) between it and the plur. suffix an; e.g. دانا‎ ‘ wise, a sage’, plur. دانایان‎ ‘the wise, sages’; دا‎ beggar’, ۰ plur. کدایان‎ ‘beggars’. But نیا‎ ‘a grandfather’, makes it plural, wis niyagan, the old form being Wls niyak.
320:Note. پایان‎ ‘feet, legs’, as plur. of ریا‎ is usually given in grammars as an illustration of the above rule. But پایان‎ is not formed from پا‎ ‘by the insertion of a euphonic :ی‎ it is the plur. of ,یای‎ the final ی‎ of which is a radical letter (pay or pai = O.P. pada) : با‎ is simply the apocopated form of .پای‎ It is an invariable rule that when a suffix with an initial vowel is to be added to a nominal stem possessing two forms, one of which is the curtailment of the other or primitive form (as and wh; جا‎ and رجای‎ &c.), the primitive form is the one chosen as stem. The case of such words as روی‎ and رو‎ ; بوی‎ and », &c., is analogous. Strictly speaking, the rule given above applies only to such nominal stems as do not possess a double form, and in which the ی‎ of the plural results from the reduction of a final & of the parent language; e.g. bls (= Phl. dan-ak), pl. دانایان‎ (= Phi. dan-ak-an). In one modern Persian word the primitive & of the Phl. (weakened, as usual, to g) is still preserved in the plural ; e.g. نیا‎ ‘ancestor’ (= Phl. niyak), plur. witty (= Phl. niyakan) as above stated. ۱
890:8) Yaki(Yaké). Indefinite noun or numeral adjective oe ‘one, some one, a certain one’; with a following negative, ‘ not one, no one, none’, It is used both adjectively and substantively, and in all the cases; €.g. ینکن مردٍ بیگانه دید‎ ‘he saw a (or some) strange man’; روز داهن بدرد‎ ae ‘one day a leopard will rend him’; یکی‎ yal از‎ سر بر نمیدارد‎ ‘not one of these holds up his head’; یکی دوستی بود‎ ‘a certain one had a friend’,
1753:§ 119, Verbal Adjectives. This suffix is generally regarded as forming imperfect participles (v. § 77); but the words formed by it are really verbal adjectives, many of which are also employed as substantives ; as دانا‎ ‘a learned man, a sage’ (= Phl. dan-ak). Some of them, indeed, do not admit of the participial sense, but occur as simple adjectives; e.g. بیدا‎ ‘manifest’ (=Phl. padtak, for patdak, patyak, petak); تخشا‎ ‘active, energetic’ (= Paz. tukhsha; Phi. tukhshak).
```


## [2026-09-06T15:22:13.209Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i -E \"CARDINAL NUMBER|NUMERALS\" GPL.txt | head; echo ===; grep -n -o -E \".{200}aevak.{200}\" GPL.txt | head; grep -n -o -E \".{100}[Aa]ivak.{200}\" GPL.txt | head"
}
```


### [2026-09-06T15:22:13.272Z] TOOL RESULT

```
Exit code 1
54:NoumERALS, 41. Words used Idiomatically in Numbering, 43. Dis- tributive Numerals, 44. Multiplicative Numerals, 45. Approxi- mate Numbers, 45. Fractional Numbers, 46. Adverbial Numbers, 46. Pronoun, 46. Independent Personal Pronouns, 47. Affixed Personal Pronouns, 50. Reflexive Pronouns, 52. Demonstrative Pronouns, 54. Relative Pronouns, 58. Inter- rogative Pronouns, 62. Indefinite Pronouns and Nouns, 65.
64:DrnominativE Nouns. Noun of Unity, 169. Noun denoting Vessel or Receptacle, 170. The Relative Adjective, 170. The Abstract Noun of Quality, 171. The Diminutive, 172. Formation of Feminines from Masculines, 172. Number, 173. The Dual, 173. Regular Plurals, 173. Broken Plurals, 174. The Plural of the Plural, 180. The Declension of Nouns, 180. The Numerals, 181.
66:Construction of the Numerals, 182. Fractional Numbers, 183. Pronominal Suffixes, 183. The Demonstrative Pronoun, 183.
242:§ 14. The twenty-eight letters of the Arabic alphabet are sometimes used as numerals. Their numerical order, however, differs from that given in the alphabet, being, in fact, the order of the Hebrew or Phoenician alphabet. ‘The letters in this order are grouped into the following eight meaningless words, to serve as a memoria technica, and are briefly called ‘the ۵ * ۶:
520:Numerals—The Cardinal Numbers Al
523:IV. THE NUMERALS (اسمای اعداه)‎ A. Tae دجم‎ NumBers (اسمای اعداد ذاتیه)‎ § 46. The following are the cardinal numbers :—
550:Note 2. In the language of the present day, the particle تا‎ (v. § 53) is affixed to the numerals to denote the individuals; 6.۵ دو تا‎ ‘two’, تا‎ sw ‘three’, تا‎ so ‘a hundred’, هزار تا‎ ‘a thousand’.
551:§ 48. The cardinals are not inflected. The exceptions to this rule are the numerals هزار‎ and رصد‎ which, as collective nouns, take the plural suffix; e.g. صدها‎ ‘hundreds’ ; Es هزارا‎ and هزارها‎ ‘thousands’.
552:Nor, with the exception of wh ‘ , do the numerals have the ya-t-tankir affixed to them.
571:C: Disrrisutive NUMERALS § 52. Distributives are formed 1) by the repetition of a simple ~
(eval):1: == not found
```


## [2026-09-06T15:22:18.695Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '518,550p' GPL.txt | cut -c1-900"
}
```


### [2026-09-06T15:22:18.744Z] TOOL RESULT

```
$45. The adjective of astonishment also belongs distinctly to the class of intensive adjectives. It is formed by adding the suffix تا‎ (sdle (الفب‎ to the simple adjective; as بدا‎ ‘how bad! or very bad’ (is) ; Te ‘how great, very great’ (is); Ly ‘how many’! خوشا‎ ۴ pleasant! how lovely’! In construction it usually precedes the sub- stantive, which often has a redundant |, called کلام‎ oe call ‘alif of ornamentation of speech’, or صوت‎ Se الف‎ ‘alif of extension of sound of the voice’, affixed to it; e.g. بدا سلطانیا که‎ ‘how bad (or very bad) is the king who . a0 1 بزرگا غلطا‎ “how great (is) the error’! خوشا شیرازا‎ ‘how beautiful (is) Shiraz’! ۱
Rem. The alif at the end of the adjective is by some termed ws? will ‘the .alif of astonishment’, and کثرت‎ will ‘the 0/7 of
Numerals—The Cardinal Numbers Al
excess’; while that at the end of the substantive is called زائد‎ Call ‘the redundant alzf’. It is the latter alzf that also occurs in the
word گفتا‎ (= wa) ‘he said’, This use of alifis not found in Phl. or O.P., it has its origin in modern Persian, and is probably derived from the Arabic: cf. the final ali in the Ar. وا زیدا‎ ‘Oh Zaid’ ! وا امیر الوم تن‎ 8 for the Conumander of the Belvo? ! This alif is called 433231 eet, or in Persian .الف ندیه‎
IV. THE NUMERALS (اسمای اعداه)‎ A. Tae دجم‎ NumBers (اسمای اعداد ذاتیه)‎ § 46. The following are the cardinal numbers :—
Units (احاد)‎ 1.1 eb (Phi. gvak; O.P. aiva). 5.0 5%) (O.P. paiicha).
2. ۲ 49 (OP. dea). 6. 4 شش‎ (O.P. khshvash). 3. ۳ sw (O.P. thre). 7. ۷ هفت‎ (O.P. hapta).
4. ۴ چهار‎ or le (O.P. ۲ 8. ۸ هشت‎ (O.P. ashta), 9. 4 35 (O.P. nava).
۱ Tens (عشرات)‎
0 دهد‎ (poet. also) sls (O.P. dasa).
11. ۱۱ یازده‎ (dialec.) 3335, (O.P. aivadasa).
12. ۳ دوانزده . وو دوازده‎ (O.P. dvadasa). 13. ۱۳ وو سیزده:‎ .  هدزنیس‎ (O.P. thridasa).
14. ۱۴ چهارده‎ or چارده‎ ) ۰ chathrudasa).
15. 10 بانزده‎ )0.۳۰ paiichadasa).
16. ۱۰ شانزده‎ )۰ khshvashdasa).
17, ۱۷  هدتفه‎ or هفده‎ (O.P. haptadasa).
18. ۱۸ هزده رهشتده‎ or رتجدة‎ (O.P. ashtadasa).
19. 44 $9353; ,وا زده‎ dialec. نوانزده‎ )۰ navadasa). 20. ۲۰ بیست‎ (Phl. vist; O.P. 0190860
30. r- سی‎ (Phi. sth O.P. thrisat).
40. ۰ 2 Je (Phl. chahal ; O.P. chatvaresata). 50. 0+ Ash (Phi. panchah ; O.P. patichasat).
60. 1. شصت‎ for orig. شست‎ (Phi. shasht; O.P. khshvashti). 70. هفتاد مب‎ (Phi. haftat; O.P. haptaiti).
80. a. هشتاد‎ (Phi. hashtat; O.P. ashtaittt).
90. ۰ - نود‎ (Phi. navat ; O.P. ۵۵۵۸۸(۰
42 A ccidence
Hunpreps (متات)‎ 100. 1.. صد‎ (orig. Jw; Phi. sat; 0:۳, sata), plural les. 200. ۲۰۰ دویست‎ (O.P. duye saite) and to 59. 300 ۳ شیک‎ 500. 6. wah,
THOUSANDS (آلوف)‎ ۱
1000. ۱۰۰۰ هزار‎ (Phi. hazar; O.P. hazanra), plural هزاران‎ or .هزارها‎ 10,000. _\j@ ده‎ or UJ, obs. بیور‎ (Phi. 0200۴ و‎ O.P. baévar).
100,000. 7
500,000. هزار‎ sail ne 1,000,000 = کرور‎ yo.
§ 47. The [0 which indicate numbers compounded of the units and the tens, hundreds, &c., are formed by placing the highest number first, the others following in order, and each being connected with the preceding number by the conjunction و‎ ‘and’; as eh بیست و‎ ‘twenty and one, twenty-one’; sy و نود و‎ do هزار و هشت‎ eh ���one thousand and eight hundred and ninety and three’.
Note 1. The same construction is occasionally employed by some of the older poets in the case of the numbers between 10 and 20; e.g. in the Shahnama we meet with ده و دو‎ and داة و دو‎ ‘ten and two, twelve’, The Turki word تومان‎ taman is also used to express 10,000 ; but only (according to Kazimirski) in such constructions as تومان‎ el ‘chief of 10,000 men’, and as the name of a gold-piece of the value of 10,000 dinars. (1 tu&man = 10 girans = 10,000 dinéirs.) The word ملیون‎ 7:29 ‘a million’, borrowed from Europe, is also used in the language of the present time.
Note 2. In the language of the present day, the particle تا‎ (v. § 53) is affixed to the numerals to denote the individuals; 6.۵ دو تا‎ ‘two’, تا‎ sw ‘three’, تا‎ so ‘a hundred’, هزار تا‎ ‘a thousand’.
```


## [2026-09-06T15:22:30.826Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; wc -l SNS_pages.txt; grep -n -i -E \"ēvak|evak|ēwak|ayāb|ayab|hēč|hec|^ud |\\bud\\b\" SNS_pages.txt | head -30"
}
```


### [2026-09-06T15:22:30.905Z] TOOL RESULT

```
16583 SNS_pages.txt
123:         rivSyat dar pahlavl az avistS ud zand.
127:en riv5yat ast az avista ud zand                               :   (s^V-^-)^
1358:                                                                                                                                        ,** i* j l« i*i   :6   pay ud   2     bahr:          ^^>r -O'Ci^y-
2501:                                             •TY/)Y^   (^U*5'j           '^) -o-^^ *          1       TYA:d5sad ud haftad ud hast: 278 -.^^^^                                                                       aJ'S*"
2979:     :5 vidast ud d6 angust:                              ya^Y*^*               i   yz*>i»i       -*i»f                                                           UiU :ham-giy3g: 3-ol«J^                       t
4207:                                                                                                                 I                    -Y/1Y^           b^jlj^ib :hec           3   / 5c 3:         _>- e>~
4321:                                                                                         l*:   ayab:      o^
4390:                                                                                                                 jM/1o J .^ji^^, :evak pad dit:jv ho
4444:                      J0^»:i)vi                  y       evak:   3*V tfWv        :    «t*i                  1A/H *$ .jiAi-^.j-*^^,:          Svkardagtar:^^^**^
5991:                        'car ud tawan: 2E*
8739:        *&/f<S .jl+t^yl+t :kust ud kust:     »«»»3    v*»»3                       i
8860:                   •/H^-U* J *""> tf ivlst ud dO, 22
8868:       fi/tM .(£M-<a*M)YA :vlst ud panj, 25: __>>«)
11117:                                                                                                                            {   r>^^ ^jM ^j->) j**Au :var ud gomSz: 0-6*
11538:           .r/T^.A/H«5          (       *»          ^)^ -evaklh: -u**
12348:                •A1/1T^ .^jo-A.ff:                sast ud sas, 66:_^>*M>»
12527:^..U^^M** :e sad ud panjah, 150:                                 <i<j>p*                                                                                                    -.
12535:      .ftUi^xaS,! iVA« :e sad ud pan]
12552:r/ n^.*bA*l*-«*'U«         :e   sad ud hastad, 180: -o~ £
12559:I*,.*taft»j44i   IA. :e    sad ud hastad, 180:                       *
12616:                                                                                                               .•j^ibjjl^.ioifie hazar ud sanzdah, 1016: _>s>*e».
12952:                                                                                                      Urf^j^jjj :duzldag ud appurdag: -£»^*r * *+*€X
15708:var ud goraSz 278/17
15721:                         vlst ud do 221/10               visbad 273/16             vizlnend 271/10
15723:                         vlst ud panj 221/11             visbedan 286/18           vizlnisnlh 271/8
15743:                         ud 256/1
15802:sust 191/18           sast ud lal 313/8                ifcyed 204/18          tav3n 145/7
15889:pes ud pas 143/2           pusih 138/19                      radSn 226/4            r€s 234/12
16137:                     havandlh 8/4                           hara-giyag 54/20        har evak 92/2
16147:                     haftad ud s5(h) 315/8                  hara-karzaglh 51/13     hast 74/3
```


## [2026-09-06T15:22:46.261Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# map line number -> leaf\nleaf=0\nlineleaf=[]\nfor ln in lines:\n    lineleaf.append(leaf)\n    leaf+=ln.count('\\f')\nfor n in [4207,4321,4390,4444,11538,15743,16137]:\n    print(n, 'leaf', lineleaf[n-1], repr(lines[n-1][:120]))\nprint('total leaves', leaf)\nEOF"
}
```


### [2026-09-06T15:22:47.838Z] TOOL RESULT

```
4207 leaf 59 '                                                                                                                 I      '
4321 leaf 61 '                                                                                         l*:   ayab:      o^'
4390 leaf 62 '                                                                                                                 jM/1o J'
4444 leaf 62 '                      J0^»:i)vi                  y       evak:   3*V tfWv        :    «t*i                  1A/H *$ .jiA'
11538 leaf 163 '           .r/T^.A/H«5          (       *»          ^)^ -evaklh: -u**'
15743 leaf 223 '                         ud 256/1'
16137 leaf 232 '                     havandlh 8/4                           hara-giyag 54/20        har evak 92/2'
total leaves 242
```


## [2026-09-06T15:23:07.247Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"^ *[0-9]+ +.?ty\\b\" SOD_pages.txt | head -10; echo \"=== search 'and' conj\"; grep -n -E \"\\bti\\b|'ty\" SOD_pages.txt | head -20"
}
```


### [2026-09-06T15:23:07.343Z] TOOL RESULT

```
4665:301 »ty(y)        M                                           j
17819:                                                                      4978 qty' C                                         ^
17839:                                                                      4982 qty' C                                     J-"X
17858:                                                                      4986 kty>k(h) B, S                       J^^\y\^c<^
17868:     4987 qty'wy C                           c^UxJ^jT
25750:7660 pty}8 M, C, S                 (</U^)*j^rU<<JU
25759:7661 pty^ B, C, S                                       Uw   7672 ptyrp- B                   j^.-H iJ^^t id>J^>Sj>
25767:7662 pty'mbry C                                   ^oj'fk            67, Dhy. 129; TSP 2.1230; STii 8.7; GMS 673
25774:7663 pty'mprymync       C                   cJUj <^»~w       7674 ptyrpyny M                                  •ju^_JL«(T7
25784:7665 pty'wS B                        JxyJ^x                  7676 ptyswc* C                            *-*~'j>t*jk&,*iSj*j
=== search 'and' conj
196:      iLJ jJ j)j tjLiT ^s jU;.« v>b ^J-^y^ j xt *>jj»l (^ (XL* ^_j» ^yLol                         b J j' Oj j' ^ c^-l ^i^i ^ <*V ^'>J tfW)^ j cy^-ti j' ^JUL- o^ j
251:                                                                                         * ^*J^** jS^                         I 6-ti I «ju- ^>-0 1 ^
404: <5* ^T tAj^Lr* x^Lj <xJ' -wJL »lj j-^>- uTU- o ^Ujj-^jJI^hJ                        <J^J J*>i jji- ^.jj^ti ^Uwl ji j-^ jj7l^l ji&^ji Jl^jj
697:dwf^>- (Jj^, <Xw *ti tOj>~j^ j' 'j^*J O^7^- J XJtS ^xiJ IjUy <;                                             j Lr3l_jJL<j ^    ■*)... .at- v <ii*-y» I ^^U^U     ^^^Llp o      o— I cr<>^-3>>-
741:ti^*J cfaJ^>* ^J-^o^^              oU-^LUI j <w^-l ^"LJU ^Uv^L^p-Ojj-^
861:O Jj Y ^ftjL^-i (_£<»b «-> .'■j ■ * j <(o«— J <-^>--r7 ^yj ^ jLoii-f 0-»^P             (--JU- f*^)^     .ij^ti ^j~i* i>y^ jt*-5« >> xl (j u5'Xu-' (j>^ tj*-^?^
1150:Lr-tjil Ij jL JUL*. c-jI^" (^«_>-A <4;L» ^L-- I jj ->^ ^ybltoU ftiaJ J^U                                        *-C 6j j ,j^j        ^!SL* p-ti j pjl^ JJ              j- C)T ^. >" j -^o^              jj^"
1182:^jL^i ^ ^ jUT ^-i»>^ j-i Y jl ^ jf jl r < z J( n ^jj                                                            J' t^i (^ J ^ •jL-i L>«:;ti" J>U>- J ^ «jUi J>A=!- -ti*. j) ^JU-' l*h-
1224:,c*J *£*&\j> \j J>* Uil >-T ^ jT ^yj j <^-' ^ti" ^>->j j*
1229:                                                                           -P *u>ti fj^J* <^        < J/j Ji. «jj^   jl$% J^jljJ* ja laii L ijljj
1233:                                                            tfOi* ^ti/l -^ Jjju-
1658:.ju>^-* <i^>; jewfyn j z'typk isyn t*yc Oj>-*o <f <(<£!*)
2221:However, the geographic limits of the territory of           of the emperor Wu-ti of the Han dynasty - crossed
4254:160 Mm'ty(y) M                                     <oU7   173 »mty>kh ^ fm>ty>kh
4354:192 »p»t B, M                    »p>y-, 'p'ty                          api/e-y aw
5552:                                                             632 >d'ty C                                     ^J^
5581:    (a) 6p(o)ti, 6p3ti/e -»Sptyk
6179:                                                                     (o)ku-ti, ku-tc ? (kwty, JkwZY)
6222:     kc-ti (kyty, >kyZY, >kytn)
6227:                                                               882 'm'ty C                                               ^uT
```


## [2026-09-06T15:23:14.782Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nleaf=0; ll=[]\nfor ln in lines:\n    ll.append(leaf); leaf+=ln.count('\\f')\nimport re\nfor i,ln in enumerate(lines):\n    if re.search(r\"\\b(301|302|303)\\s+[»'’]ty\", ln):\n        print('LINE',i+1,'leaf',ll[i],'printed~',ll[i]-66, repr(ln[:200]))\nprint('total leaves',leaf)\nEOF"
}
```


### [2026-09-06T15:23:17.364Z] TOOL RESULT

```
LINE 4665 leaf 77 printed~ 11 '301 »ty(y)        M                                           j'
total leaves 644
```


## [2026-09-06T15:23:25.083Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor lf in (77,138,151,286):\n    print('=== leaf',lf,'printed~',lf-66)\n    print(pages[lf][:700].replace('\\n',' | ')[:700])\nEOF"
}
```


### [2026-09-06T15:23:27.324Z] TOOL RESULT

```
=== leaf 77 printed~ 11
            >v |  |  |  |  | "trn'y |  |  |                                                                              awaz, awazc ? (sw'n(h) ?) ^wz'k                    12 |  295 »trn»y M |      atarne |                                                                              pool, 9.30; |                                                                              TSP    lake GMS 1056A; Bailey. Asica. 4; S W, |                                                   Oijj( 'tr-'" |       (o/)fire |                                                                               BSOAS 1983, 46, »w>nh |       S W, BSOAS            1981,236                          II |                           
=== leaf 138 printed~ 72
                                                                                                                  *wdyz- |  |  73 |                                                                         sleeping |  |        GMS     1399; EGSii 76, 116, 121; BBB 566; |        Tedcsco. ZII, 1926,95; SW,C2n          pl84; S W, TPS            GMS 961; C2, 51R28 |  |          1994t 43-50                                              1860 >wpy S*                                        >>y> |                                                                        uPT ©<ubaya =»wPyw | 1846 'w'ys => *w'ys                                                    both | 1847 Vnh        B =» *wz}k |           
=== leaf 151 printed~ 85
                                                                                                                     86 |  |  'yyrty^ |  |  |  2162 'yyrty'k       M                         4*-y,j.>^f |        iyartyak ? =»yyrty'k                                        im, Trna, Iman, Imax Cym, }ymn, 'ynVx) ©Sah\ |        extension, diffusion                                           m(,) |                                                               2175 >yOP    ahmahy ©lpl pres. ^'sty1, y-1, x-1 |        GMS 518, 1110                                               GMS 778; >ym\ STii 1.83, 41.25; Frag. Len. 92, 9; |  2163 }yjn =» yznyh                                                  >ymn, B
=== leaf 286 printed~ 220
                    mm |                                                                                                                       220 |                                                                                                                   u*y*"i £f |   mspn- |  |        them                                                    5512 rawy C, S |        STii 3.39                                                     muy ©ob. -y; nom. ace. -w> =*myw |                                                                      Magus, Magian |  5501 mspn- C                     j-^-^j^ ib^J'c^-\j^\               C2 gloss, ace. nom. mwYwt nom. mwYy pl97; |       maspan ©impf. ^spn-
```


## [2026-09-06T15:23:37.677Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor lf in (150,151,285,286,287,76,77,78):\n    p=pages[lf]\n    for m in re.finditer(r'.{0,120}(this|and\\b|dem\\.).{0,120}', p):\n        s=m.group(0).replace('\\n',' ')\n        if 'this' in s or 'dem.' in s:\n            print(lf, lf-66,'|',s[:200])\nEOF"
}
```


### [2026-09-06T15:23:39.659Z] TOOL RESULT

```
150 84 |                                                                          this 269, 1403, 1500; VJ 364; TSP 3.120 etc.,
151 85 | 2174 'ym-     C «* 'y'm-                                          this
286 220 |       this Ortymw) ©OP imam ^'mw, mwn'w,   'my2                    ace. -fw, C2, IV, 17, 29; loc. -ty, C2, 1R25
287 221 |       this                                                                                                       'J^S l^ S
287 221 |       this
```


## [2026-09-06T15:23:45.800Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[150][:2500])\nEOF"
}
```


### [2026-09-06T15:23:48.008Z] TOOL RESULT

```
                                                                                                                       'ySyCy)



  85

                                                                         obtained
 2137 >xz- C                                   j»j^<j=-^
      axaz, anxaz ©impf. mxz           ^Yz-, myz-, >xst-                 STSCiii; BSTii 905.9; C2, 57V9

        Oo)rise                                                     2151 »yc»t S, C                                  o-j^r'U
        GMS 55; C2, 51V11                                                ecat, icat ©<*uz-cyatd ?
                                                                         safe, sound
 2138 ^mnty      C                         j^^'^^^j
      axaz-amandc ^yz'mnty                                               MSP bl87 p42; S W, CI, 1991, 185, zwk>yc>h >ycH
      resurrection, rising                                                tfr-, CII 1990 p53 "keep firm"
      C2 gloss, ace. }xzymntw, C2, 40R16; BSTii 908.16             2152 >yc,t,wy S                               oL*l,^>U
 2139 y C                                  jUjoL^j;                      ecatawe ^'yc't
                                                                         security, health
        ay ©<ayw       =»*yn> V
                                                                         CII 1990 Fl p53
       period
       C2 gloss, n p75; Benv. JA 1959, 130f                        2153 >yct(y) =» >y5c, >yst
                                                                   2154 >y6 B, M, S                           (j^ ^^ ^)yj
2140 >y2 C                      :               (/x*^^)^7
     ay ©intcrj. voc.                                                   c5 ©<Av. aeta; OP aha
     C2 gloss.; Sund. AoF 1981 p2l3
                                                       - 1 iJ\Aj
                                                                         this 269, 1403, 1500; VJ 364; TSP 3.120 etc.,
                                                                         GMS
2141 ym       C
                                                                            17.28; Bcnv. Notcsiii 219
       ayam
       end        ^"y'm, 'ym2
                                                                   2155 >y5,k S-»»y5y(y)
       C2 gloss, ob. -y, C2, 51R13                                 2156 >yd'r- C                                        ^/
2142 ym-          C
```


## [2026-09-06T15:23:56.805Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[77]\ni=p.find('301')\nprint(p[max(0,i-1500):i+1500])\nEOF"
}
```


### [2026-09-06T15:23:59.178Z] TOOL RESULT

```
        *                                    /             auxane, aw-xanc ©pi. -t =>*wxJny
    atar-wartan Ontrwrtn)                                                   having the same house, housemate
    fire chariot                                                            Hen. Talcs. 485.1
    SCE 243
                                                                        312 MwYwn S                                   *S\jU>- <jujU
299 »tr xwrndy(y) M                                                         oyon ? auyon ?
                                                                            as so
    atar-xurande ©Parth. ddur xwarendag
    swallowing fire                                                         MSP bl74
    BBB bl5, b94
                                                                        313 "wkrsnyy  M            (\Sy^ \Sljs>~ fty*^- 0>^
300 »try swc»y 8ynh S     (^U ^ Oiy*)oijsJ J^                               awkarsne ('wqrsny(yXh)) ^'wqrsn'wt
    atarc-socc-Scn =>6ynh                                                   Column of Splendor (a Manichean god)
                                                                             BBB 540.3-, GMS 7, 351
     glowing fire(Af ani's teaching)                                  u^1
     Karab. Insc. 17.11, 25; Bcnv. Notcsiii 223                          314 "wqrsnyCyKh) => 'wkrsnyy
                                                                         315 "wm'n'k    B                          Js^iJ^
301 »ty(y)        M                                           j
                                                                            aw-mancusly
                                                                            unanimo , omane    ©<*hdmd~mdnaka         ^'wm'n
     at =>>rty\ 't1
     and
     GMS 76                                                                 GMS 351; TSP 2.266 n pl72
                                                                        316 "vvm'nty'kh                          ksJ^^^j^
302 »w'YS B                                Voyri^^-c^r
    awaxs (*w>xs, Wys)                                                      aumantya(k), aw-mandyak
                                                                            unanimity
    side, now ?
     BSTBL, Dhy. 223; Dhu. 229 n p47.229; TSP 3.298;                        KG p!77
                                                                        317 "wmr'z M, S                             jjklaJ^isJt
         MSP p39-40
                                                                            aumraz, aw-maraz     ©pi. -/; pi. ob. -ty
303 "w'ndi) ? =» "w'zh                                                        ^'wmr'z'nc ?
304 »w'rkpt ? =* »w}zypt ?                                                  helper
305 »w>rt- B                         jtfjltftfj                             BBB 540.1; GMS 351; Hen. BSOAS 11.68; KG
    awart (*wrt-) ©inf. -}y
```


## [2026-09-06T15:24:13.490Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor lf in (137,138):\n    print('=== leaf',lf)\n    print(pages[lf][:1400])\nEOF"
}
```


### [2026-09-06T15:24:16.055Z] TOOL RESULT

```
=== leaf 137
                                                                                                                                   72
  }t6rty



       BSTBL, Vim. 98, 110, Dhy. 173; Benv. Notes 4,                              BSOAS 1983, 46

             507; VJ 1046 ?; H6rmkW>ncK TSP 6.191 n p207;
             Hen. Sogdica. 60.13; Tales. 476.5                           1828 ataru
                                                                              »trwh(wYt-) S                              (o>j)J^~\

 1814 >t5rty     B
       o9r(3)t"i, asti =^csty, csty, >sty                                      {put <?/z)firc
                                                                               Anc. Lett. 2, 12; Hen. Date. 604.12 605 n5
       third
                                                                         1829 >trync C                                        ^-7
       VJ 1070; STii 10.9, 50; BSTBL, Dhu. 229, 248,                          atarenc ©f. adj.
         254; GMS 1331, 1337
                                                                               fiery, (d?/)fire
 1815 >t5rtyk B, S                                                             BSTii 890.35; C2, 60V3
                                                       r>
      30r(3)tik, ostik -*cst*yk\ »5rtyk, >styk, >cstyk
      third                                                          
=== leaf 138
                                                                                                                  *wdyz-

 73
                                                                        sleeping

       GMS     1399; EGSii 76, 116, 121; BBB 566;
       Tedcsco. ZII, 1926,95; SW,C2n          pl84; S W, TPS            GMS 961; C2, 51R28

         1994t 43-50                                              1860 >wpy S*                                        >>y>
                                                                       uPT ©<ubaya =»wPyw
1846 'w'ys => *w'ys                                                    both
1847 Vnh        B =» *wz}k
                                                                        GMS>w5(101A;
                                                                                h)   Anc. Leu. 2.27 pl5n5
1848 Vnkw        S(MD) => 'wn'kw
                                                                  1861 'wc' C                                          b*T
1849 Sv-'wt'qcyq           C                             j*3^
     aw-otakcik           ©pi. -f                                      oca ?, otsa   Owcy) ^wts'r, 'wrc ?, 'wrts^, >ws\
      fellow-countryman                                                 there
      S W, C2, 87R 13 & n p!63
                                                                       GMS 71, 358; STii 3.70, 2
```


## [2026-09-06T15:24:24.812Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'EOF'\nimport re\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nd={}\nfor p in pages:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m: d[int(m.group(1))]=p\nfor n in (500,529,325):\n    print('==== pdf',n,'printed',n+1917)\n    print(d.get(n,'MISSING')[:1500])\nEOF"
}
```


### [2026-09-06T15:24:27.010Z] TOOL RESULT

```
==== pdf 500 printed 2417
[pdf page 500]
4۱۷ بلس
کنان واراده کنان (۱)- وییمانه کنان باشد . وهبات باشد.
پازد۱ بروزن سازد » بعنی آراده کند پاز نده؟ « بروزن سازنده, بمعنی قضد
وقصد نماید ودراز سازه . وآهنگه واراده کننده باشد .
یازدن؟ - بکر نا و قم دال : پازه* « بروزن غازه, بممنی لرزه باشد
مخفف بازبدن است که قسد و آهنکه کردن که از لرزیدن است .
وبلند شدن ودست بچیزی درا ز کردن باشد.# پاز یدن؟ » بروزن ومعنی بالیدن‌است
پازش؟ « بروزن سازتی . بممنی قصد که نمو کردن باشد - و بمعتی قسد و آراده
وآهنگه واراده ولمو وبالید کی ودرازی باشد . | وآهنگه کردن - وبلند غدن هم هت .
باز ند < بر وزن پازند » بممنی شکل ِ یاس۷ * بروزن‌طای. مخفف پاسمن‌است.
() خم۳:۱وموکنان .
- مضارع از «یازیدن» («.م.) ۴ - از: باز («.م.) + دنت (پوند مصدری) سه
بازیدن (م.) ۴ - از: باز(هم.) دش (اسم مصدر):
به دراز ودراز پازش او امل‌خسم را کند کوتاه.
ابوالفرج رولی- «سروری» +
۴ - از: باز (ه.م.) ۳ نده (پوید آسم فاعل) . * - از؛ باز (۸.م.) ۰ (پوند
اسم مسدر) [ر4: اسم مصدر بقلم نگارنده ص۹۵ بیعد] ر4: تییازه, خمیازه ‏
‎٩‏ از باز (۸.م.) + بدن (یسوند مصدری) * بازدن (۸.م.) ۳ پاختن(۸.م.) ‏ آختن
(«.م.) «بازیدن, آهنگه کردن و بلند برشدن باشد » «سحاح الفری سخهٌ طاعتی» اسدی درلغت
فری (ی۱۸۹) کوید : «* درخت که ببألد گوبند «بیازید» ومردم که دست فرا چیزی کند گوبند
«بیازید...» ۷ - ر4: یاسمین:
چهار افروخته شمعند لیکن شان لگن بر سر
کزایشان‌است روشن چشم بای وت رکس وریحان:
یکی خندا ن کل سوری » دوم خیر هکل خیری,
سوم خرم کل سرین » چهارم لاله اسان .
فربد احول «رشیدی؟ .
بازده - بفح‌دال ۳ بانزده, اوستا 26۷841858 (بازدهم). پپلوی 28061210-050
( پازدهم ) + کردی‌ع 263 افغانی 70۵188 «اسشق ۱۱۲
==== pdf 529 printed 2446
[pdf page 529]
بیان چهاردهم
در بای حطی باکاف فارسی مشتمل بر سه لغت
یگان!- بفتح اول وئانی بالف کشیده یگانه؟ < بروزن زمانه , بمعنی‌بی‌مثل
وسکون نون بمعنی بك‌است که واحد باشد چه | ومانند وبیهمتا وموافق باشد .
بکان یگان يك‌,ك را کویند؟ - وبمعنی‌بی‌مثل یگانه گوی؟ - با کاف فارسی بر
ومانند هم هست. ۴ وزن بهانه جوی » فردم موحد را کوبند .
بیان پانردهم
در یای حطی با لام مشتمل بر سیزده لفت
یل - بفتح اول و سکون نانی » شجاع ۱ "ودلاور وبهادر وپهلوان را کوینده - ورهاکرده

۹ * بکان . از : يك ( <بکه )+ آن ( پسوند عدد توزیعی که سپس ور ت کان

درآمده), قی: بیگانه . «بیکان... بمنی بگانه نیز بود. سوزنی (سمرقندی) گفت :
وزرا نگویم از ارکان دولست یکی که او بجاه زارکان دولست بکان .>
رك : ح۲. «صحاح الفرس, سخهٌ طاعتی».

۴ - درتضی رکمبریج «یکان بکان» آمده: «ابلیی هرآن معلمان وحکیمان را وادیباترا
همه را یکان بکان نام همی‌برد وصفت همی کرد ومی‌ستود .» « تفر کمبریج ورق ۲*۰۳ ۸.1.8 >
ر4: براون..تفضیر ص4۹4 ۴ - از: يك (* بگه)+ آنه [پارسی باستان 81۷818
8 پوند] "دارمستتر. تتبعات ح۱س۱۵۲* ۰ یپلوی 6۷212881 (آنك * آنه . پوند
عدد توزیم ی که سپس صورت گانه درآمده) رك: دارمستتر. تتیعات جچ۱ ص۱۵۱ ۰

۴ - از: ریگانه ۳ کوی (کوننده) یعنی قائل بتوحید .

- «بل, مبارز بود. فرخی (سیستانی) کوید :

جابی که بر کشید (برکشند) مساف از پی مساف
و آهن سلب شوند بلان از پی پلان .
فردوسی (طوسی) گوید :
کنون چنبری گشت پشت بلی تشاب همی خنجر کابلی . >
«لغت فری ص۳۲۲*.
ورك: صحاح الفرس (طاعتی) .

۰ یگانگی - بفتح اول وچهارم, از: یگانه (یگارك) ی (<اصل مصدر, اسم همتی) ؛
اتحاد يك‌جتی, یگانه‌بودن - وحدت : * وشناختن آفرید كارهمة چیزها ویگانگی وی وبیوند
همه 
==== pdf 325 printed 2242
[pdf page 325]
و -۲1-
وبمعنی‌پازهم هت ۱ چنانکه گوینه «وانگوبی» | وکاهی بجای با کفته می‌شود ۴ چنانکه گوبند
یعتی باز نگوبی و « واکفت » پعنی با زکفت - « وا تومیگوم > بعنی‌باتومیگويم ۴ - ومخقف

۱- پیشوند فعلی است بمعتی «فرا > و « باز * و بنظر مبرسد که آنها «ستقرماً از 5۳2

( پیشوند) و 888 ناشی شده باشند . « دارمتنر . تبعات جچ۱ ص ۳*۹ .کردی ۷۵ ( باز )

« زابا س 4۳۵ ۰ قی :کردی ۷۷6 ( پیشوند قىلی بمعنی باز کردن , مراجمت ۰ دوباره انجام

دادن ) » زازا 2 «ژاباص ۰۲۹۷ دراراك ( سلطان آباد) ۷۸2 ( واکردن » با زکردن )

« مکی نژاد > » تهرانی نیز ۷2 کیلگی ۷8۵ ( ۷8۴۵۵ باز کن ) استاد بتولیست «وا» پیشوند

قعلی را در افعال نظیر * واکردن » درفارسی اصالی نمبدانند وبرآنند که درلهجهٌ تخاطب فارسی,

درنتيجةٌ تأثیر لهجه‌های شمالی‌مانند کیلکی‌ومازدرانی ایجاد شده » چه ازنظرعلم اسوات(فوتيك)

« و فارسی اصیل یت ( از افادات شفاهی استاد پنئویت ).

هزار یوسف کم گشته وا توالی‌باقت سر آستین جمال خود از بیققانی +
اجیب‌الدین جربادقانی « رشیدی».
۴ با (هم.) ابا (هم.) ۴ - کاه بجای «به» بکار رود :
گرچه ما وا سوی مأُوا میرویم با دل آشفته زینجا میّروم ‏
شاه داعی ۸« رشیدی >.
بفیه از حاغبة مفحة قبل

قدیم بوده و امروزه غالباً بدل به 09۷ - پا 0 میشود : تلفظ قدیم جو, 18۷ بوده » وتلفظ مولی
درعربی 132۷14 است وامروزه 109۷ وبا 0[ وق10۳:1 با 32012 (درفارسی) نلفظ کنند .

۸) - و(اصطلاحاً واوماقبل عضموم ) - وآن 09۷ - است که دو صوتی بشمار میرود و این تلفظ
امروز رایج است ( ومثال‌آن گذشت ).

و(عطف) - تلفظ درست‌این‌حرف درفارسی کنونی0 است. درپهلویا. پارسی‌باستان-118

« بارتولمه ۳۸۶۸ *. در اوراق تورفان ( لهجهٌ شمال غربی 1 «* لیب رکه ص ۲۲۹ ۰۶
```


## [2026-09-06T15:24:55.648Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'EOF'\nimport re\nt=open('BQT_v4_pages_faseng.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nd={}\nfor p in pages:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m: d[int(m.group(1))]=p\nfor n in (500,529,325):\n    p=d.get(n,'')\n    print('==== pdf',n,'printed',n+1917)\n    for line in p.split('\\n'):\n        if re.search(r'[A-Za-z]{3,}', line):\n            print(line.strip()[:300])\nEOF"
}
```


### [2026-09-06T15:24:57.661Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'BQT_v4_pages_faseng.txt'
```


## [2026-09-06T15:24:59.774Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; ls; "
}
```


### [2026-09-06T15:24:59.824Z] TOOL RESULT

```
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
```


## [2026-09-06T15:25:04.901Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 600 python3 tools/ref_page.py BQT:2417 --image 2>&1 | tail -30"
}
```


### [2026-09-06T15:25:10.694Z] TOOL RESULT

```
۹ مطارع از «یازیدن» («.م.) ۴ - از: باز («.م.) + دن (پوند مصدری) -
بازیدن (ه م.) ۴ - از: باز(ه م.) شش (اسم مصدر):

له دراز ودراز بازش او امل‌خسم را کند کوتاه.
ابوالفرج رولی۰ «سروری؟ .
ار - ازه باز («.م.) لا لده (پوند آسم فاعل) ۰ * - از باز («م.) ۰ (پوند
سم مصدر) [ر4: اسم مصدر بقلم نگارنده سرا بیعد] ر4: لبیازه» خمیازه .

‎٩‏ از: باز (ه.م.) ۳ بدن (پوند مصدری) * بازدن (ه.م.) ۳ پاختن(ه.م.) * آختن
(«.م.) «بازیدن, آهنگه کردن و بلند برشدن باشد » «سحاح الفری دغخهٌ طاعتی» اسدی درلفت
فرس (ی۱۸۹) کوید : « درخت که ببالد گوبند «بیازید» ومردم که دست فر! چیزی کند گوبند
«بیازید...» ۷ - ر4: یاسمین:

‏چهار افروخته شممند لیکن شان لگن بر اسر

‏کزایشان‌است روشن چشم بای وثر کس وربحان:
یکی خندان کل سوری » دوم خیر هکل خبری.
سوم خرم کل نسرین » چهارم لاله انسمان .
فرید احول «رشیدی» .

‏بازده - بفتح‌دال * پانزده, اوستا 26۷80888 (یازدهم). پپلوی 98021-050
( پازدهم ) »کردی‌ع 060 و. افغانی 30188 «اسشق ۱۱۲۲ کیلکی 328203؛ دء بعلاوة
يك. عدد بن ده ودءازده .
بقیه از حاشيةٌ صفحةٌ قبل
«یازان » آهنگه کنان باشد . شهرة آفاق گوید:

‏ز همه خوبان سوی و بدان یازم که همه خوبی شد سوی رخت یازان.»
«لفت فری *5۹-۳۸.
زهمه خوبان سوی تو بدان‌بازم من که همه خوبی سوی رخ نو پازان شلد ,
```


## [2026-09-06T15:25:13.551Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 600 python3 tools/ref_page.py BQT:2417 --image 2>&1 | head -20"
}
```


### [2026-09-06T15:25:15.259Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 500; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2417.png
REF: BQT:2417  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 500  OCR-lang: fas

-4۱۷- اس

کنان واراده کنان (۱)- وپیمانه کنان باشد . وهیأت باشد.

بارد۱ ‌- بروزن سازد ۰ بعثی آراده کند باز نده؟۴ « بروزن سازنده, بمعنی ۲
وقصد لماید ودراز سازه . وآهنگه واراده کننده باشد .

بازدن؟ ب بکر ثالك و ات دال » باره* ه بروزن غازه, بمعنی لرزه باشد
مخفف بازبدن است که قسد و آهنگه کردن | که از لرزیدن است .
وبلند شدن. ودست بچیزی درا زکردن باشد.۸ پاز یدن! - بروزن ومعنی بالیدن‌است

پازش؟ « بروزن سازی » بمعنی قسد | که نمو کردن باشد - و پمعنی قصد و آراده
وآهنگه واراده ولمو وبالیدگی ودرازی باشد . وآهنگه کردن - وبلند شدن هم هت ۰

پاز فد - بر وزن پازند , بممنی شکل یاس" » بروزن‌طای, مخفف‌یاسن‌است
```


## [2026-09-06T15:25:22.135Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nfrom PIL import Image\nim=Image.open('data/verification/sources/refs/ocr/BQT/2417.png')\nprint(im.size)\nw,h=im.size\nim.crop((0,int(h*0.62),w,int(h*0.80))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt2417crop.png')\n\""
}
```


### [2026-09-06T15:25:24.026Z] TOOL RESULT

```
(1650, 2546)
```


## [2026-09-06T15:25:26.487Z] TOOL CALL #49: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt2417crop.png"
}
```


### [2026-09-06T15:25:26.504Z] TOOL RESULT

```

```


## [2026-09-06T15:25:41.872Z] TOOL CALL #50: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2417.vision.txt <<'EOF'\n[read from image, BQT vol.4 printed p.2417 = pdf page 500; Mo'in's numbered footnote 5 at the foot of the page]\n\n۵ یازده ـ بفتح دال = یانزده، اوستا aevadasa (یازدهم)، پهلوی yâcdah-um\n( یازدهم )، کردی yânzdeh، افغانی yôlas «اشتق ۱۱۲۲»، گیلکی yânzdâ؛ ده بعلاوهٔ\nیک، عدد بین ده و دوازده .\n\n[i.e. Mo'in derives NP یازده from Avestan aēvadasa via Pahlavi yâcdah(-um),\nwith the modern cognates Kurdish yânzdeh, Pashto/\"Afghani\" yôlas, Gilaki yânzdâ.]\nEOF\necho saved; cd /home/sfmqrb/git/rishe; timeout 600 python3 tools/ref_page.py BQT:2242 --image 2>&1 | head -6"
}
```


### [2026-09-06T15:25:48.794Z] TOOL RESULT

```
saved
(no exact page map; using offset -1917 -> pdf page 325; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2242.png
REF: BQT:2242  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 325  OCR-lang: fas

و -۲41-
ویمعنی‌بازهم هت ۱ چنانکه گوبند «وانگوبی» | وگاهی بجای با گفته می‌شود ۴ چنانکه کوبند
```


## [2026-09-06T15:25:52.658Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nfrom PIL import Image\nim=Image.open('data/verification/sources/refs/ocr/BQT/2242.png')\nw,h=im.size\nim.crop((0,int(h*0.55),w,int(h*1.0))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt2242crop.png')\nprint(im.size)\""
}
```


### [2026-09-06T15:25:54.699Z] TOOL RESULT

```
(1650, 2546)
```


## [2026-09-06T15:25:57.063Z] TOOL CALL #52: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt2242crop.png"
}
```


### [2026-09-06T15:25:57.086Z] TOOL RESULT

```

```


## [2026-09-06T15:26:24.107Z] TOOL CALL #53: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2242.vision.txt <<'EOF'\n[read from image, BQT vol.4 printed p.2242 = pdf page 325; Mo'in's note s.v. «و»]\n\nو(عطف) ـ تلفظ درست این حرف در فارسی کنونی o است. در پهلوی ut، پارسی باستان utâ\n«بارتولمه ۳۸۴»، در اوراق تورفان ( لهجهٔ شمال غربی ) ut «لیبرکه ص ۲۲۹»، رک: اشتق‌ـ\nهوبشمان ۱۰۷۱؛ اوستایی uta، کردی u «ژابا ص ۴۲۸»؛ در فارسی معمولا o تلفظ گردد:\nنشست و برخاست، حسن و حسین؛ ولی در جایی که پس از آن حرف مصوت باشد، va تلفظ شود:\n    می‌آرد شرف مردمی پدید / و آزاده نژاد ازدم خرید.   (رودکی سمرقندی)\nاما اینکه این حرف را بسیاری معمولا va تلفظ کنند تقلید از حرف عطف عربی است. در عربی «وَ»\n( مفتوح )، در آشوری بابلی u، در عبری u، در آرامی «و»، در لغات جنوب الجزیره و حبشه\n«و» «ولفنسون ص۲۹۳». متأخران قواعدی برای مواردی که در فارسی o و مواردی که باید va خوانده\nترتیب داده‌اند ( رک : غیاث‌اللغات ).\nو( تصغیر ) ـ و آن u ـ تلفظ شود و پسوند است . رک : صرفه از دیباچهٔ مؤلف .\n\n[= Mo'in: NP «و» < Pahlavi ut, Old Persian utā (Bartholomae col. 384), Avestan uta;\nand the modern «va» pronunciation is an imitation of the Arabic conjunction wa-.]\nEOF\necho ok; cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor lf in (417,418,419,420,421):\n    p=pages[lf]\n    print('=== leaf',lf, repr(p[:200]))\nEOF"
}
```


### [2026-09-06T15:26:26.078Z] TOOL RESULT

```
ok
777
=== leaf 417 'ایقفه ه با فا بررزن و معلی ابفده\u200cاست\nکه بهوده گو و سبکار باشد که حرزه چانه\n۱9۳۳\nاون بکر او وسکون انی وفاف\nبواو وسیده و بنون زده ؛ بلفت رومي کلی است\nبغات بدیوی و کنده و بعربی\u200cوردالمنتن\u200cخوانند .\nرنگ آن '
=== leaf 418 'ابلا\nومردمان و جماعت را نیز گویند - وهیل را هم\nمبگوبند که له صفارباشد - و بکر اولوفتح\nانی مشدد گا و کوهی باشد . گوشد چون سمار\nشود بیتی خود را برسوراخ مارنهد و بنفم. مار\nرا بجاب خود کشد چنانکه مقناطیس '
=== leaf 419 'دنق\nو نام ییت النفدس هم\u200cهست - وبسینی کوبند تام\nعبت ان رت رادم کر از\nفتحهایعبرخطاب. ومعنی آن\u200cسدیق اکبرباشد.\nایم « بروزن جیم » مردی را گوبند که\nزنش مرده باشد ۱ .\n) ثمد \u200cِ بروژن\u200cایسد .کاوآهن\u200cرا گوبنده\nو '
=== leaf 420 'ایولز\nایو اد « بانانی مجهول بر وزن شیرازه\nبمعتی آراسته و بیراسته باشه ۱ .\nبسعنی ابواز است که آراسته و پیراسته باشد ۳ .\nالوان ه بروز نکوان . صقه و طاق را\nبند ۴ ,:\nابوانس بفتح\u200cاول وسکون ثانی\u200cوثالث\nبالف '
=== leaf 421 'و شش لت و نات\nبیان اول\nبا - , دمعم مع است که\u200cبجهت عصاحت\nباشد - ویمعنی به بفتح بای ابجد - و مضاف به\nاسامی آشها مانند ماست باوزیره با و کدوباوامثال\nآن ۱ - و مخفف باد و باشد» هم هست .\nبااوش « با حمزء بوا'
```


## [2026-09-06T15:26:35.241Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor lf in range(410,425):\n    p=pages[lf]\n    if 'این' in p:\n        for m in re.finditer(r'.{0,150}این.{0,250}', p.replace('\\n',' ')):\n            s=m.group(0)\n            if re.search(r'[A-Za-z]', s) or 'اوستا' in s or 'پهلوی' in s:\n                print(lf,'|',s)\nEOF"
}
```


### [2026-09-06T15:26:37.478Z] TOOL RESULT

```
410 | فرهنکگ دساثیر ۶۵ از : | ( علاعت‌تفی ) همه . ۴ - فردوسی در زمر طبقات چهارگانهٌ زمان جمشید کوید : ۰ چپارم که خوانند اهنوخوشی کجا کارثان هسگنان پیشه‌بود این کلمه محرف 12046750 پهلوی است و آن مر کب است از دوجزو : جزو اول هو بمعتی خوب و جزو دوم از مصدر توخشیتن (تخشیدن) بدمنی کوشیدن و ورزیدن است . هوتخش . بمنی خوب ورزنده و نیک وکوشنده و مراد از آن لبق صنعنگر است. بنابر این مصراع فردوسی بیکی ازصور ذبل صحیح 
411 | بنجکانةٌ کاتهاست وآن دارای‌هفث ها ( فصل ) ورویهم صد بند است . « هزدینا ۳۰۶ ۴, در پهلوی ۷2۵۲ ۸۵ با ۷2۶ ۸۵2 «رهارلهه۲۱۷ و روز اول پنجهةٌ دزدیده را بنام این کاتها خوانده‌اند . رك . اشتود واسفندمن . ۴ - اهوازجمم عریی کلمةٌ مفردهوز ۳102 (بجای خوز 2:012) که عمان 110226 سرباني‌باشد. این تسمیه در آغلز فقط بك قبیلهٌ ساکن این نلحیه اطلاق ميشده و ایرانیان - تحت نم‌سوزبان 6 - آن را بعنوان ابالئی برای تعیین ناحيه
412 | لوی اوستا بدون شرح و تفیر بوده است. اما ظاهراً بتدریج زند را بترجبه و تفمیر جمعاً اطلاقکردند . بدینوجه علت ندرت نسبی امت‌عمال کمها مار نك آشکار شود . اینکه کفتیم «سبی» , ازآ تجاست که تحقیق و مطالمهٌ کتب پپلوی هنوز بسی مانده است که ,بایان برسد و ما سیاری ازامور غبر مترقب در پیش خواهیم داشت ...» و هم درنامهٌمز بور اسناد مثاس ابارتك رابا 21۷2۳1671081 کد درتر جمة پهلوی کلم اوستابی۷266 بمعنی جوشیدن وجوشان
413 | هیچ. *- در ازمتا 276291011542 (فلز کداخته) مر کب از 29381 بریهلوی آسن ودر فارسیآهن وجزو دوم که خشوست باشد بمعنی مایم وروان است «خرده‌اوستا ۹4۱4۱ شابر این یو کلم ه آیخشست با شن و سین هر دوست . 0-- دهلوی ۲ بمممنی اینجا . مقاسه شود باساکرت فلاأتها6 «یب رگ۸. ۵ اه _ شمیرسوم شخص جیع , ره : مس , ۵ از ديباچة مولف .
414 | خراسان و آذربایجان و اهواز و طبرستان و بیشثر از دود شام را نز اعلحضرتمحمدرضاشاه گونند - بهلوی شاهنشاه ایران ایر ان‌شهر - بروزن وبران‌شهر » نام ۱ رل : اینند. . ۴ پپلوی ۵0۵8 سسمتی چنن» اینگونه. ازابرانی باستان 8102۷808 اوستابی؟3642:۷30<بار تولمه۱۸* #تب رک۹۸» «ارترالا۷۹۸> «مناس۲۷۳».  .‏ سرك: ص۷۹ج۷. ۴ رك : اردا و نز وبراف . ۳ پپلوی ارات +ویکشور ابران دز عید ساسانی 50024۴ - ۵۳80 (رك:ایرانشهر) عیگفتند. در 
415 | وناییکی را کوبند وفام یخ‌سوسن ۴ آسمان کون هم‌هست سس ۰اه ٩‏ پهلوی 50205 - 8640 . شتر(< شهر) بسمنی کشور ومملکت بوده که بمدها از وسمت مفپوم آنکاسته شده واین‌لفت م رکب‌بدمنی مملکت ابران استممال شده. راد: شمارٌ هفت وهفت کر نظامی بقلم ۳ از و هت ؛ یاقوت در ممجم اللان گوید : بلاذری گوید : خرا-ان دارای چهار ربم است : ربع اول ابران‌شهپر است و آن شامل‌ییثابور و فهتان و طبسان و هرات و پوشنگه و بادیس و طوس است . 
416 | ول‌وسکون‌نانیمجپول و زای هوز و غين قطه دار مضوم بنون و جیم بت درپپلوی ابریگان 20727820 مردمان ۳ب ات۱۴ 10 که بطبقة پیشواباندینی‌ورء‌حانبان اطلاق‌ميشد. این‌کمه در ادبیات‌بپلوی 287۳088 درشاهنامه سه‌بار ابرمان پمعنی مهمان آمده وایرمان‌سرای‌بمعتی مهمان‌سرای‌مستممل است .بدیدهی است که این واژه در غارسی ممنی اصلی خود را از دست داده حول بسبار بیدا کرده است . در ناتگرت واوستا 20" بمعتي بارودوست ونیز نامویکی از
417 | مورد خدابان مت‌برستان نیز ایشعمال یشود. «قاموس عقدس ۰۱:۲ ات 9 1 ابل بمعنی دست » حردم ۰ ملت » گروه , سال ؛ «طیم وتابم است «جغثابی۱۲» و ابلات جسم معمول این کمه‌است . ۵ ایستادن - بنتم ششم . پهلوی 0ها 650 «تاوادبا ۲۱۹۶ «عنای ۲۲۷۳ ۰ ایرآنی‌باستان 2 - 2۷1 جزو اول بشوند وجزو دوم‌مشتن از )5 (500 لهج جنوب غربی) *نبر 45۵5 ۷» در اوستا 562 (استادن) «بارنولمه ۲۱۹۰ » بمعنی برپا شدن , قیام کردن ؛ بر خاستن - متوفف ب
420 | نکنیسهرا تا سال آینده حاصلکنند » و سپار بفروشند » و اعتماد آن نواحی برآن باشد » و همه ناحیت از آن روغن بکاربرند و این از عجایب دناست .۰ 8 - هز 22۵۳)8(8 , پهلوی0۵5010. چشم «برنکر۹*. 1 - )016 ( درنسخهةٌ خطی شمار؛ ۱۶۷۱ کتا:ضانةٌ علی هارمس یادداشتی است که‌ابوحنیفه از ابوزید نقلکرده و ا و کوب که نام حفیقی « جرجر » النهق است و لبد از شمرای‌معلفه برای ضرورت شمر آنرا الابه
424 |  قبچاق بود وبعدها وی منگو را بمقام خانی بررگزید . رك : فهرست تاربخ مفول بقلم آ قای اقبال وداثرةالمعارف اسلام. ‏ ۷ - رل: بابوئه . ۸ - باج و باژ و باز باین معنی از ریشه 08 پارسی‌بامتان مشتق است «مزدیسنا ۵4-۲۵۳ » وآن از ريشة 2 اوستایی بمعنی بخش کردن وقسمت کردن‌است . ٩‏ - باح وبا وباز وواج و واژ باین‌معنی ازريشة اوستابی ۷۵6 ( گفتن)» سان‌کریت ۷۵6 ۰ درپهلوی [۷2 با ۷۵8 ۰ درلاتینی ۷۵۴ , درفرانه ۷۵۷۴ » در انگ
```


## [2026-09-06T15:26:51.894Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[419])\nEOF"
}
```


### [2026-09-06T15:26:53.606Z] TOOL RESULT

```
دنق
و نام ییت النفدس هم‌هست - وبسینی کوبند تام
عبت ان رت رادم کر از
فتحهایعبرخطاب. ومعنی آن‌سدیق اکبرباشد.
ایم « بروزن جیم » مردی را گوبند که
زنش مرده باشد ۱ .
) ثمد ‌ِ بروژن‌ایسد .کاوآهن‌را گوبنده
و آن اعنی است که زمین را بدان شدبار کنند
و بمتی کویند ایمد چوبی است که کاو آهن‌رابر
آن صب کنند و زمین را بنافند و آنراجربی
سنه خوانند ؟ .
اهر - بنتح اول بر وزن خنجر , آهن
سرنیزی را کوبند که‌برچوب قلبه‌صب کنندوبدان
زمین را ثبار کنند » و بکسر اول عم آعده
ت 9
ایمه - بفتح‌اول بروزن خیمه » بمعنی
اکنون و این دم باشد - وهرزه و یاوه وییهوده
را لیز کویند - و بکس اول بمعنی اینچنین
وهمجنین است 9
اینت ‏ بکسر اول و سکون ثانی و نون
و فوقانی » بمعنی امث بفتح نون است معنی‌ترا
این چنانکه کوبند «(بنت میرسد» یمنی‌ثرا این
عیرسد - و بمعنی زهی و په‌به وخدخه که کلمةٌ
تسین است» هم گفته‌اند.
ابوار
انس - بکسر اول و سکون تالی و فتح
الب و سین بی‌لقطه» هر چیر بته راگونن دکه
بدشواری وا شود و دبر حل کردد و ظاهراً این
لفت با انیسه با نون و بای حطی تصحیف خوانی
شده‌باشد ودر اصل اين لفت‌ابسته بروزن‌برجه
ست 9۵ چنانجه دربیان همزه بانون گذشت .
ایشت ۷ س بفتح ثالث بروزن میرفت »
بمعنی خاجت از کسی خواستن و استدعایمطلبی
نمودن باشد .
ا یناث ه پفتح ثالث بروزن ميرك » مصفر
این است که اشارت بفرب و ترديك باشد - ویضم
الث آبله را کوبند که از بدن اطفال برمی‌آید .
الثنك » بروژن ریوند » بممنی اند است
و آن عددی بائد مجپول میان سه و نه و آنرا
بعربی بضع خوانند ۷" و سخن عجیب و سخن
از روی شكو رب‌رانیز کوبند - و بمعنی‌چندان
و چندین هم آمده است .
اناد - با انی مجپول بروزن دبوار .
وقت عمر باشدکه «نماز دیگرش نیز میگویند
چثانکه ثبگیر صبح را خوانند- و رامرفتن وقت
صررا ابوار کردن و وقت صبح را شبگیر مودن
کونند ۸ .
ی ان :
۹ اف اس دروآینت» ۷ رك : آبدند ۰
ایزد هت آسمان کرده است ادرفران
۴ در پارسی باستان 1008 , در پهلوی تط,
۵ - همین وجه صحیح است. ر انبسته.
لمنت ایشندجای برئن‌دیودژم «عنوچهری 6۵6
بقبه ازصفحهً ۱۹۸
```


## [2026-09-06T15:27:02.325Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 300 python3 tools/ref_page.py BQT:199 --image 2>&1 | head -20"
}
```


### [2026-09-06T15:27:03.836Z] TOOL RESULT

```
no scan of BQT covers printed page 199 (see 'scans' in refs_online.json)
```


## [2026-09-06T15:27:21.495Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD ewak\"; grep -n -E \"ēwak|ewak|ēw |yazdah|yāzdah|hēč|hec |ayāb|ayab|^ud |ēn |im \" PHD_mackenzie.txt | head -30"
}
```


### [2026-09-06T15:27:21.546Z] TOOL RESULT

```
=== PHD ewak
68:without him many common words would have slipped through
120:   By its nature the dictionary cannot claim to contain the entire
538:       dus-nim [-n'm I (M dwjn'm), N ",j add ill-famed.
756: ,...,-bim [-bym] fearless.
808:a-bim [lbym] fearless.
1292:iiwiim ['wb'm I M )w'm] time, season.
1364: ayab- v. ayaftan.
1389:Ayfim ['dIm] moon.
1509:badniim [blfnwm] the major purification ritual.
1527:  im ....... : his Majesty. oy -: his late Majesty.
1572:bim [bym I = M, N ,....,] fear, terror.
1646:biim [bwm IN.....,] land, earth, country.
2962:huniyi'll1ar                        45                            im roz
3012:im [LZNE < A l-znh; >m 1M cYm , N --] this.
3013: -- l:im ray: for this reason.
3157:kim [k)m I = M, N~] will, desire, purpose.
3280:kim [kyn I = M, N kin(a)] hate, malice, revenge.
5051:ud [W < A w I M )wd, N u] and.
5061: Uris lim [lwlyflym I N -] Jerusalem.
5190:war-~aim [wlclm] with eye(s) in the breast.
5224:warz-biim [wlcbwm] cultivated land.
5703:yazdah [y)cdh I M y)zdh, N ......] eleven.
5914:acquisitive ayabag.                       agitate ayiirdenidan~
6194:claim pahikardan.                        commission gumardan.
6220:collaboration hamkarih.                  comprehension ayabagih; parwand.
6494:eleven yazdah.                               erring aband, aberah.
7193:nursing, nurture dayaganih.            or ayab.
7384:  yoJdahrih.                                   receptive ayabag.
7682:stone sa(n)g; fruit -- ast(ag).            successful kiimag-hanjiim I -widiir,
7734:swim snazidan.                                dan, etc.
```


## [2026-09-06T15:27:30.190Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"^(ew|ēw|hec|hēc|en|ēn|ayab|ay-ab)\" PHD_mackenzie.txt | head -20; echo \"===\"; grep -n -E \"\\bone\\b|\\bany\\b|\\bnothing\\b\" PHD_mackenzie.txt | grep -n -i -E \"ew|hec\" | head -20; echo \"=== raw\"; grep -n -E \"'w[kg]|ʾywk\" PHD_mackenzie.txt | head"
}
```


### [2026-09-06T15:27:30.268Z] TOOL RESULT

```
159:entails both confusion with the true letter r , and the introduc-
2202:en [ZNE < A znh I M <yn, N in] this.
2209:enya [)yny) I (M )n)y)] otherwise, moreover.
2248:ewan edw)n ] bridle.
2250:ewar eywll J )y,9)r] certain(ly), assured(ly).
2252:ewarzidan, ewarz- edwlc-ytn' ] move, travel.
2253:ewarzig [)dwlcyk ] moving.
2258:ew-bAr [)ywb)l] once.
2260:ewi!n edwynl I M )ywyn, (N ayin)] manner, custom, form, propriety.
2264:ew-kard(ag) eywkrt(k)l, -kltk l ] united, joined.
2266:ew-sAn eyws)n' I (N yak-san)] uniform, (a)like.
2268:ew-tAg eywt)k l I M (yw t)g, (N yakta)] alone, single, individual.
6502:enchant afsudan.                             essential gohrig, madagig, madagwar,
6503:encircle hambastan.                             madayan.
6540:ewe meso                                           fall on pahikaftan.
12239:ewan                       ,~tU'        ayaromandih        rlf.)'tG~~
12243:ewazig                '~o)Itu-          ayas-                    - ~..JC,Y'
12247:ewbar                  ~to'             ayastan                  "~--ltt"
12249:enya, henih               -'"U K)t      ayadgar              ~~~~
12250:ewen                      ,,.. KY.      asyag                      \~
===
2:104:tion of Pahlavi studies I have given elsewhere. I If one reason
26:7174:non-essential jadisnig.                one ek, ew.
=== raw
3878:llwon ['wgwn' I M ))wn] as, so.
5509:Woriibarst [w'wklwblft l = Av. wouru.bari1Iti-] the north-western con-
5511:WoriiJadt [w'wklwcllt = Av. wouru.jari1Iti-] the north-eastern con-
```


## [2026-09-06T15:27:36.124Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"^(ek|Ek|el<|hec|hech|hic|ec) \" PHD_mackenzie.txt | head; echo ---; sed -n '2190,2270p' PHD_mackenzie.txt | grep -n -E \"^e\" ; echo \"--- search hec\"; grep -n -i -E \"\\bhe[cč]\\b|nothing\" PHD_mackenzie.txt | head"
}
```


### [2026-09-06T15:27:36.201Z] TOOL RESULT

```
2194:ek (lywk I M yk, N yak] one.
---
1:edar [LTME < A I-tnh I M )ydr, N --] here.
2:edon [)ytwn l I N idun] thus, so.
4:eg [ADYNI < A )dyn I M )yg] then, thereupon.
5:ek (lywk I M yk, N yak] one.
7:ekiinag [)ywk)nk I N yagana] submissive, obedient.
10:ek-dad eywhd)t ] sole-created.
12:emed edmyt l ] hope.
13:en [ZNE < A znh I M <yn, N in] this.
20:enya [)yny) I (M )n)y)] otherwise, moreover.
28:erang [)ylng] blame, condemnation; error, heresy.
30:eranJ-,v. I, leraxtan.
38:er-kaA edlkf I M )yrkf] (hands under the amlpits in respectful) salutation,
48:erwarag edlw)lk l I J )rw)rh] jaw, cheek.
49:esm [)ysm] = ezm.
50:espo, v. spo.
55:ei [)yf I N xeI] plough.
57:e(w) [Ij HD < A 1;zd I M (yw, N -e] a, one.
59:ewan edw)n ] bridle.
61:ewar eywll J )y,9)r] certain(ly), assured(ly).
63:ewarzidan, ewarz- edwlc-ytn' ] move, travel.
64:ewarzig [)dwlcyk ] moving.
69:ew-bAr [)ywb)l] once.
70:e(w)-~and ey(w)cnd] some, a few.
71:ewi!n edwynl I M )ywyn, (N ayin)] manner, custom, form, propriety.
75:ew-kard(ag) eywkrt(k)l, -kltk l ] united, joined.
76:e(w)-mOg ey(w)mwk l ] wearing (only) one shoe.
77:ew-sAn eyws)n' I (N yak-san)] uniform, (a)like.
79:ew-tAg eywt)k l I M (yw t)g, (N yakta)] alone, single, individual.
80:ez-, v. yaz- .
--- search hec
```


## [2026-09-06T15:27:46.377Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"hyc|h1c|he[cç]\" PHD_mackenzie.txt | head -20; echo \"=== NYB\"; grep -n -E \"ēvak|ēwak|hēč|hēc|ayāb|ayāp|ud, |ēn\\b|ōy\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T15:27:46.439Z] TOOL RESULT

```
1340:axezidan ['hycytn'] = axistan.
1341:axistan, axez- ['hstn', )hyc- I M )xyst, )xyz-] rise, stand up.
3275: ....,igih [-ykyh] soothsaying, prophecy.
5373:wihez- [wyhyc- I M whyz-] move, progress.
5374:wihez(ag) [wyhyc(k )] movement, progression.
7331:prepare arastan, passaxtan, siixtan,           prophecy kedigih.
=== NYB
216:TYN?: TINÀ mud, clay
331:āivēn ['dwyn'] rites, customs 818; cas.obl. —-E [+1] nāmak 121%, the Sassanian code of courteous manners and conduct, NP dīn-nāmah, often referred to by Mus- lim authors. — < OIr "abi-dayana- from "day- (v. dītan),. whence NW-Prth ab- den, but SW-Prs *aibiden > *aiviyén .> diven. — KZŠPrth 1. 19 "bdyn = Prs l. 24 *dwyn, Gr. v. #00¢; Ps. ’dwyny translating Syr. nāmēsā = the Mosaic Law; MPrth 'bdyn ‘habit, custom’ (Hen- ning, TPhS 1944, 110-112); Arm. lw. aurēn-k* ‘institution, the Law ; the Eucha- rist’; Syr. lw. b-abden ‘similar to’, cf also hämöden; Paz. NP Gin, Skr. v. äcära; Arab. lw. °@in. V. Markwart, UJ VII, 1927, 89-121; Junker, WuS XII, 1919, 150.
333:äivenak [’dwynk'] kind, sort, species, genus 478, 3917, 7611, 8028, 9417-20, 1083.10; nature 100!4; — manner: pat han =, pat én ~ in this, in such a manner; being in such a state; thus: 1129-21, 3416, 8519; the thing (event, situation) being so, connected with ditan 21. 322, 917.27, ]]6.14, 123. 1215; with āšnūtan 814, — cë ~ A813, pat ce ~ 1620.21, 788 how?; pat ciš-ic ~ ma 708, pat hec ~ ... ne 792-3 in no way, by no means; pat han ~ ka griyét so that he is weeping 11"; — pat ~ i guaršet like the sun 441?; pat Susr ~ some- thing like a sperm 95!7; pat ēzanišn ~ by (means of) killing 103%; har 2 — in both respects 110%, — MPrs ’ywyng (S, A-H JI), yng (List 80); Paz. dina, ŠGV àinaa, Skr. v. prakära, SGV also vidhà, riti. [MPrth ”dyng, List 79, NP Ginah ‘mirror’ seems to go back to *ä- dayana-]. — Note: — NP ädinah ‘Friday’, for Islamic (yaumu-)l-jum'a, cannot be etymologically connected with ātvēnak, as Markwart has it (v. above s.v. ātvēn); it probably goes back to MIr *atēnak < Olr *ati-ayana- (OP ati-ay- ‘to go along’), ci MPrs 'dyn ‘entrance’ (S, A-H II), with secondary lengthening of the initial a-: *ādēnay ‘congregation’. — V. also ham-ātvēnak.
349:akārēnītan [~-ynytn'] to incapacitate, to destroy 42%, — Paz. ägärined, Skr. v. vināšayati (SGV XII, 43).
356:a-kartaréh [’krt’lyh] inactivity: šmāh dahēt gl. to bē acārēnēt (g. v.) 45?. — V. kartār, kartàreh.
374:amah [LNH, Prth LN] pers. pron. Ist. p. pl. 1. cas. rect. we: —-ic... āyēm 913-14; to —-ic dāt hem we have been created by thee 397; ētšān (v.s.v. 04) ~ hem ke 5778; - an, ~ an: v. lan. — 2. cas. obl. us: a) dir. obj.: —-ic äkäh framāi kartan please let us know 11%; — martoman 11%; ~ (twice) proleptic obj. of zanišn 409-7; — b) virtual dat.: franāmišn ~ we must proceed 405; ~ ap i tē pat kar ne apāyet we have no need of your water 14?3; 191-2; — c) the agent of a pret. pass.: pas =: framāt HajB:11; HajA: 5.10 (Prth LN); ~ ētēn āšnūt ku 34, ete.; - d) i ~ our: dar i ~ 39, etc.; e) after a prep.: andar, apük, o ~. — Av. (295 sg.) gen. ahmākom, OP amāzam; MPrthPrs ’m’h; Paz. ema; NP ma. V. also -màn.
413:Amahraspands 397-8; an amäh u Pw!] Gi 6 ham tuxšem [this reading should. be restored] andar äp, andar damik, andar urvar, andar gospand we and he will labour jointly in water, soil, plants, cattle 3915-16; an-ip to ... fräc vēnēnd for thee (dat. ethicus: thou mayest know:) they prophesy ... 51% (v. tē and -p); an 6 amäh asp vāzēnēt you there, bring the horse here to us 541° (cf Spanish nosotros, vosotros); an či gäv that (re- markable) bull 427. 49?-5-18-19; ang [ZK-y] či asp that (remarkable) horse 491’; an če that very man 5419; an alone for the Ist p. sg., v. the next w. — Av. (135 sqq.) anya-, ainya-, OP aniya-; MPrth ny; MPrs ^», "ny ‘another’ (also = 2an); Paz. han, with -c: hanica. In J-Prs hm, ’ny emphasizing a pron. as described above, v. Mackenzie, An early Jewish Persian argument (BSOAS XXXI, 1968, 249-269), L, 1. 14 (p. 262): whny "wy dd dyh ‘and He is the lawgiver’ (hesitatingly combined. with ^ny by M. p. 254); Utas, The Jewish- Persian fragment from Dandàn-Uliq, Or. Su. XVII, 1968 (1969), 129, 1. 13: ny man simply = ‘T, Ll 4: ny mr = anë mara ‘for me’. — Cf also änöd and. enyä.
463:Anēšē-zātān [/nw&yc?t?n'] patr. of Anošč- zat, the father (or ancestor) of Mihrak 1322, 1525. — From anos = anēšak + zat (q. v.) ‘Immortal-born’; as to the ending -ë in the composition cf s.v. mēnēt.
491:?apak [LWTH] 1. a) adv. together: (ka- nicak virtual dat.) andar ham Sap ~ bit in that same night he was together with the girl 16!-?; referring back to an encl. pron.: sih (restore the reading “30”, v. 28th) 4-$ ~ pat asp which was with him on the horse 8? (v.s.v. i and ef andar); Sih-& ... —-aš pat asp nišast estat 89: as prepositions do not govern an encl. pron. ~ must be the adv., and -aš refer to the following pat asp or to the whole sentence. — b) prep. together with, with, in all its senses, passim; in spite of 118; ~ man 5?*; ~ amäh 19, ~ smäh 1918, ~ disin 82; ēvak ~ dit with each other 7818. 799. 1071, — 2. adj. prostrate, knocked down, lying on one’s back: čvak apar, ~ dit, apar ēstūt hend o en kar they set about this act (making coition), the one above, the other lying on her back 4314-4; ka Ahriman ~ A. being knocked down (lying senseless) 914 (the enel. -4 after ~ belongs to the following, taking up the preceding subj. Ohurmazd which begins the period), a wordplay — not understood by the Pazandist — with — hämöden yazdan u amahraspandän |. 5—6, the first
497:apākēh [’p’kyh] 1. company; pat ~ together 5712, — 2. backward movement: pat ~ back 418; v. pat-apākēnītan. — 3. help, assistance 5919-20, 729-26 (opp. ha- mēstārēh). — V. lapāk and ?apäk. Paz. āvāgī. V. also apar-apākēh.
498:apäkenitan [—-ynytn'] to make a p., or a th., one's helper, or companion, or help: hakar vēnākēh apakéné [-yd] (if thou wilt make Clear Vision thy helper
516:apārīk [’p’ryk; Prs inser. ’p’lyk] other l. attribute, placed before its subst., passim; seldom inflected in pl. before a subst. in pl. cas. obl.: hac ~-dn giyākān u röstäkän 8617-18, — 2. independent: ~ other people 5026-27; han i evak ... the one ... and the other 1093; ēvak-ē ... u ~ one... and another 12115; ~ har cé all other things that ... 862. 10411, 1211; u ~ and others (z who) 10812; ‘ete.’ 11015. 12119; u ~-dn ‘et ceteri’ 11017; sak u dalman tdi <... except for dogs ... and vultures, (all the) other (animals) 9421-22, — MPrthPrs bryg (S, A-H II); apär- < *upārda < Olr upa- + *arda- ‘side’ (v. ärak): ‘standing by a p.s side, placed at the side of a th.’ = ‘his, its counterpart’ (HP II, 14); cf apärön. Paz. aware, which must be another w.: < *awarrég < *apar- rek < *upari-raika- ‘left over, remainder’ (from reztan, g. v.)?
535:scindo). This act. is generally supplanted by the secondary caus. apasihčnitan from apa-sih-. — Note: — There is a synonymous vb. of uncertain origin which may have been influenced by the apa-sih- vbs.: Paz. awasdinidan SGV XI" = Phl *apa-sāyēnītan; "ps'dín! = apa-sāyišn Mx 15% (wanting in Cod. K); *pys’synytn' = apēsāhēnītan (the second -s- inverse spelling of h) DkM 175°. 351! (in the MS 13419. 27015), *pys'hšnyh = apesahiš- neh ibd. 180° (= MS 13816); to be de- rived from *apa-sü- *apa-säy- ‘to rub away’, cf s. v. apa-sütak ?
554:apäyistan ['p'dstn'], apāyītan [’p’dytn'] apäy-, 3d p. sg. apāyēt [’p’dt', ^p'dyt'], 3d p. pl. apäyend ['p'dynd], pret. 3d p. sg. apāyist 1. to please a p. (pat) 83%; cigon mēnēyān apäyist as it had pleased (was predestinated by) the heavenly gods 405, v. below. — 2. impers. it is desirable: -m apāyēt 6 han ciš I desire, try to obtain, this 562%, — 3. to be needed 1211-2 also pat. kär. apāyet 14%. 375, andar apāyēnd 105%. — 4. to be proper, seemly 4015 (bē ~). — 5. impers. apäyet auxiliary vb.: must, ought to, shall, should, has to, is bound to, ete. with the p. as indir. obj. (virtual dat.), a) governing an inf., which is as a rule placed after: u api-t xvatāyēh i Ērān šahr vas sal apäyet kartan and thou shalt exercise dominion over Iran for many years 629-31; 918-19, ]014 ete.; in this case preverbs to the inf. are drawn to apäyet; bé — pursitan 1319; ba ~ hištan 1313; kār-ē i apar nē ~ kartan 104%; apārīk 6 [KN] ~ xtartan 94??; less often the inf. is placed before: ēzatan nē ~ 1017-19; pit u mat frazand i xueš rād En and kär u kirpak ... bē üámóxtan ~ the parents shall teach 6522-23; 6519-20; 9113; the inf. sometimes has to be supplied: -
668:asēmēn
671:aržānīkēnītan [~-ynytn'] to consider a p. worthy, governing a subordinated clause without an introducing particle, 5318 in a very complicated passage 5317-21, which only seems possible to understand on the following suppositions: a) kū-t bahr hac man bé burt l. 19 is not a gloss, as I have marked it, but is governed by anak tč bavat l. 17 ‘it shall be unhappy for thee that thou hast bereft ...'; b) the clause kē ... aržānīkēnīt hom 1.17-19 is loosely attached to tē l.17; c) for MNW-t L<y> (MS very clearly MNWtl) read MNW kw) LY» = kē tē man, to man being the exact counterpart of LK ^NH = tč an (v. žan) 1. 19 and both signifying ‘thou and I’; d) YBLWN-m l. 18 and 20, and HWH'-m 1. 19, are the Ist. p. pl. coinciding with the Ist p. sg.; e) there is a wordplay between *š = dé ‘food’ l. 18 and ’$ = as (demonic) eye’ 1. 20 (as burtan 'to have a vision', v. 'aš; bahr ‘ministry’, v. this w.). Text: anàk tč bavat, marak, ke t(0» man fratom hac ax" i astomand andar Rdg u Notar hac bahr barišneh āš barom frac aržānīkēnīt hom, kū-t bakr hac man bē burt. niin-ip tē an pat apar-barišneh aš barom u et bavēt kū-t dušcašmiha al zänak nikēram i-t nest ‘unhappy shall it be for thee, little scoundrel, (that thou) — as thou and I first of all men in the material world between Räg and Notar have been found worthy of earning food by perfor- mance of ministry — that thou hast bereft me of the ministry. Now thou and I shall be enraptured in an ecstatic vision, and then it will happen that I shall see thee evil-minded in another house that is not thine’. The passage is the immediate continuation of the incident related in 537-15, Zsprm XII, 7 epitomizes 5316-21 as follows: dwlyslwb BR’ L zltwšt gwpt' "VK cygwnt pltwm HWH'-m b’hl wlweyk BR’ ’pknd HWH'-m ZK tw "NH KR?
672:= Dūrēsrav bé 6 Zartušt guft ku: cigēn-at fratom ham (cf 209 ete.) bahr u rocik be apakand hom, an tč an (v. lan and ?an) har 2 aš apar barom api-t bē marnjēnēm "D. said to Z.: because thou hast deprived me, as the first, of both munistry and food, we both, thou and I, shall be enraptured in an ecstatic vision, and then I shall annihilate thee’.
686:āsēn ['syn'] iron 1105. — MPrth ”swn; MPrs ”hwn (List 79); Paz. āhin(-sāxt) (Aog.); NP āhan. Ci Benveniste, MSL 23, 1927, 132 sq.; 30, 1930, 60.
687:āsēnēn adj. of iron 2076. 2327, 241; ~-sumb v. sumb.
715:āstēnītan [’stynytn'] to set up, to erect 398, 10912, Caus. of östätan (g.v.), both < *aipi-sta; the alternation ē- : ā- is pos- sibly due to shifting accent: *aivi-sté- > *ayyi-stā- > "ai-sta- > Estä-, but áivi-stá- > *dv-std- > *āstā- (divergent explana- tion Verbum 224). Cf MPrth pt. ’wystn’d ‘to put, to place’ (S), Ghilain 78 sq.
```


## [2026-09-06T15:27:51.063Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in \"^ēvak\" \"^ayāp\" \"^ayāv\" \"^ut \" \"^hēč\" \"^ēn \" \"^im \" \"^yak\"; do echo \"== $w\"; grep -n -E \"$w\" NYB_vol2_glossary.txt | head -4; done"
}
```


### [2026-09-06T15:27:52.854Z] TOOL RESULT

```
== ^ēvak
== ^ayāp
== ^ayāv
== ^ut 
== ^hēč
== ^ēn 
== ^im 
2109:im [LZNH] dem. pron. this here, near to the speaker: im rēc to-day 51% ete.; im spah Erän this army of Eran (pre- sent here) 27??; 2626, 378.23. 5212. 1028; im bag Xösröi šāhān šāh the present King of Kings, Divine Khosroes 109?!, — Prth
== ^yak
6944:yak: evak yazešn, -ašni: izišn
```


## [2026-09-06T15:27:57.791Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '2109,2112p' NYB_vol2_glossary.txt | cut -c1-1200; echo \"=== evak\"; grep -n -E \"^[eēéc]vak|^èvak|^evak\" NYB_vol2_glossary.txt | head -5; echo \"=== ut/ayap\"; grep -n -E \"^u[tf] \\[|^ayā[pb]|^ayav\" NYB_vol2_glossary.txt | head -5; echo \"=== hec\"; grep -n -E \"^hē?[cč]\" NYB_vol2_glossary.txt | head -5; echo \"=== en\"; grep -n -E \"^[eē]n \\[\" NYB_vol2_glossary.txt | head -5"
}
```


### [2026-09-06T15:27:57.893Z] TOOL RESULT

```
im [LZNH] dem. pron. this here, near to the speaker: im rēc to-day 51% ete.; im spah Erän this army of Eran (pre- sent here) 27??; 2626, 378.23. 5212. 1028; im bag Xösröi šāhān šāh the present King of Kings, Divine Khosroes 109?!, — Prth
Jafar [y?pl] n. pr. Arab Ja‘far: abu [bw] ~ 117?! the calif al-Mansūr.
jahišn [yh&n'] 701: v. jayišn. jamān [ym’n'] v. zaman.
Jāmāsp [y’m’sp'] n. pr. the vizier of King Vistäspa 18!2, 21-29 passim. 351. 11019. — Av. (607) Jämäspa-; v. Bailey, BSOS VI, 1930, 63—64.
=== evak
1467:évak [HDwk'; on coins *ywky] num. one, passim; hàn + ~ Arjäsp A. alone 2416, 2927; ~ ~ one by one 92$; har ~ every- one 1045-%, 10617. 11318; ~~ bēvar ten thou- sand 244; 3 ~ one third 6329-22, 9316, 1025; 4 ~-é [-’y] one fourth 998; 5 ~-é [^y] 10015-17, 10227. 1031-2; — in correspon- dence with dit, ditikar, ane, v. these ws. — Av. ačva-. OP awa- + -ka-, v. s. v. žē; MPrs yk; Paz. yak, iak, NP yak — as against MPrth ‘yw ‘one’, *ywg ‘alone’.
1469:évak-x"atayéh [—-hwt'dyh] autocracy 8019.
=== ut/ayap
=== hec
1978:hče [hyc] any, in neg. sentences, placed before its headw.: — kas anyone; ~ ciš-č
1995:hčšmakan [hyšmkn'] angry 1422. abstr. x(a)šmagami Antià 1235. hešmēh [hšmyh] an outburst of fury 6815. — Probably only kēšm + the indef. art. -€: ~ mà kun, ce mart ka hešm kunet ... Paz. substitutes xašmgini (cf the preceding w.), Skr. v. kopa. hešm-kāmakihā [hšmk”mkyh”] in the manner of one whose volition is deter- mined by wrath, furiously 7425, Paz. zasm-kämihä.
2014:hči [hwd] left 222°. — MPrthPrs hwy, xwy; Av. (1736) haoya-. V. also höyak.
2024:hčšak [hwšky] ear of corn 1284, v. s. v. Iyextan. — Bal hošay; Psht wazai, Mor- — genstierne, EVP p. 95, no. 266; NP xösah.
=== en
```


## [2026-09-06T15:28:06.586Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in \"aēva-\" \"aeva-\" \"aēvan-dasa\" \"aēvandasa\" \"uiti\" \"aēta-\"; do echo \"== $w\"; grep -n -m4 -- \"$w\" BRT.txt | cut -c1-400; done"
}
```


### [2026-09-06T15:28:08.292Z] TOOL RESULT

```
== aēva-
== aeva-
2660:•  p.  aiva-,  j.,  g.  aeva-,  j.  oiva-'*  Zw. (fem,  'vn-)  'ein*  i)  als  eig.  Zw.,  im  Gegens. zu  anderen  Zw.  oder  einer  beliebigen Mehrheit  'ein;  einzig,  allein' :  tilm  '*  . .  di'a . .  tisrö  F.  /;  —  nöit  . .  °vo  nvit  dva  mit '^räyS  nöit  fräyankö  Y.44\  —  'vake  .  . *al>ntaoyaAe  .  .  dvaya  .  .  'irayqm  V.  iS. 11;  ^.0^,108;  —  ^riS"  ma
8922:•  j.  kaeva-  m.  EN.  eines  Gläubigen frinlspalu  'vahe  asuonii  "des  Fr.,  Sohns des  Ä".  .  ."  Yt.  13.122.
11398:•  j.  £ina-  Pron.  interrog.  'welcher?  wer?'; i)  als  Fragewort,  an  der  Spitze  des  Satzes: 'ntnt  i^ar>^3m  frabaräi  °ti?m  yaom  Jra- barati  ayatfhaltam  vä  srum  (sd.)  vä "worin  '*  soll  er  das  Essen,  worin  '*  das  Bier bringen?  In  einem  Gefäss  aus  Eisen.." V.  iü.  6.  z)  als  Indefinitum;  a)  im Relativsatz,  enkl.  hinter  dva-  'zwei  be- liebige, i
12448:'daeva- n
== aēvan-dasa
== aēvandasa
== uiti
2873:girfsaite  akur.li ..  uiti  aojanö  Yt/0.53; — yö  aoxta  a/iiiräi  ..uity aojanö''  Yt.  Ä 10;  J0.73,_V.2.io,j.2o;  —  fravasayö  .  .^ uityaojana^'  \\,tj.(>(>;  —  uifyaojana (NPm.)'>  mi>rHi  Yt.ro.41;  —  ätar! . . uiti  vacibii  aojanö  Yt.  19. 49;  5.76;  — ; aus. .uiti  vaülns  aojana  Yt/7.17;  22;i —  bulyqsta  . ,  uiti  aej^mna  uiti  daomna FrW.  10.  42. 
3170:Uta  %rayam  vahiltanqm  amiiyS  (sd.) bw^ata  . .  "^raj/am  'tatiqm  aiwi'hyö  buyata V.J.V  17;  —  'y,i  maiyä  Uä  (APn.)  daniö vaxhnii  dagi5jsuitif(%A..)  Y._32.  4; —  aya *mainiv3  varatä  (sd.)  yi  dngvH  'tä Timyö  . .  Y.  30. 5 ;  —  yi  ..  yazli  apä  . . 'bm    mantüm    (sd.)    Y.j;^.  4.  a)    mit
3211:'sagen':  äla  (sSPfA.)  F.-K;  —  mit ui/i  is±):  aöaica  (iSPfM.)"'  uiti  V.4.47, N._J7.  a)  Pass.  'genannt  werden,  heissen', mit  dopp.  Nom. :  yäia  . .  akarana  anayra asaonö  sfif  aili  Yt.Ä48.
3694:•  j.  '''aipi.karata'^  Inf.,  mit  asii  'er  ist eingedenk,  hat  Acht  auf  — '  (Gen.):  vis- paz'a  vilcS  mazds.fraoxta  .  .  ySi  huiti  "la dusmatahe  ".  .  die  Acht  haben  auf  das, was  übel  gedacht  ist"  Y.  71.7;  7*.
== aēta-
```


## [2026-09-06T15:28:17.681Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '3160,3175p' BRT.txt | cut -c1-600; echo \"=== aeta\"; grep -n -m6 -E \"aeta-|aeSa-|aêta\" BRT.txt | cut -c1-300; echo \"=== va oder\"; grep -n -m6 -E \"^• *[jgp]\\.? *v[āa]-|'oder'\" BRT.txt | cut -c1-300"
}
```


### [2026-09-06T15:28:17.768Z] TOOL RESULT

```
•  j,  a-£i9'öiri§ta-  Adj.  'nicht  durch  Busse zu  wenden,  unsiihnbar':  *paoirya  *vtträa (LS.)  asSqm  syaoian)in\c(i\  'tjm  "schon wenn  sie  sie  zum  ersten  Mal  begehen, ist  ihre  Tat  nicht  mehr  zu  sühnen"  N.  23.
Komp. !  niä.+'un-ii/a-,  PPfP.  lum  V.  :n;irs- ; zSchr.,s.  S  :6S.  44  aE.  —  Pü.:  atö£isn  (T.)
•  j.  a-ciBra-  Adj.  "nicht  offenbar,  undeut- lich': '^nJ  F.  7.
Pü.;  afai/ai:
•  j-,   g.   a^iäta-   Adj.   'der  schlechteste,
■übelste,  böseste"*:  dva  yaska..  -«(NDm.) I  V.  7. 70;  —  sHptibyasca  (sd.) . .  vispalibyasLa pairi  'taeibyö  \.  14.17;  —  °to«  rfuirfw- Aavö  'P.14;  —  nöil  hl . .  bvat  . .  zahistiJ anhuL.bi'ai  TTspariqm  *°/jm'^  *paosisl>mcix ya^  »riyat  daozaishum'^ . .  sondern  es  wird
dby  Google
53
a£i$t%e
flim  das  AUeischlechteste  und  stinkendste lu  Teil  werden  .  ."  ^.40;  —  mit  Inf.: y>  't)m  *vainariAe  (sd.)  aogidä  gqmcä  .  . hianiä  V.?-'.  10.  a)  bes.  van  an/iav- (sd.);  Aaia  -tat  auhaot  Y.7J.15; — okAus 'lö  V.jo,  4;  —  äi'a  't)m  aüa  ähüm  ä V-53S;  FrW.j.a;  —  -täi  auuhe'^.i,. 61.  A)    in    religiös- moralischem  Sinn:
Uta  %rayam  vahiltanqm  amiiyS  (sd.) bw^ata  . .  "^raj/am  'tatiqm  aiwi'hyö  buyata V.J.V  17;  —  'y,i  maiyä  Uä  (APn.)  daniö vaxhnii  dagi5jsuitif(%A..)  Y._32.  4; —  aya *mainiv3  varatä  (sd.)  yi  dngvH  'tä Timyö  . .  Y.  30. 5 ;  —  yi  ..  yazli  apä  . . 'bm    mantüm    (sd.)    Y.j;^.  4.  a)    mit
manaA-  n.  (sd);  hyat  v?T}niltä  (sd.)  'I}tn manS  Y.jo.ö;  —  ya  x/ä^rä  grihmö hiiatal  (sd.)  'tahya  d^mum  manatthö  Y. ^2.13.
SuperL  in  ata-.  —  Pü. ;  i'atlar,  Valium,  valtar- lum.  —  '»  Im  Gegens.  zu  t-ahiiiii:  —  ')  ilds. aulT-iraniim,  aber  Pü.;  lalldrlum.
•  j.  a-£istäe  Inf.  'zu  speisen,  zu  essen': ya  pipi^wa  vasö  a^  "feste  Nahrung  darf man  nach  Belieben  essen"  N.  (>2.
Zu  einer  w.  Basis  *t'äxs-  (mit  ö);  i  aas  > '}.  — VgL  mp.  (äil,  eäilai  'Mahl'  (N.  64),  np.  !ä!t, xna.  LW.  r'aL  —  fu.-./nt  i  fuxt  pa  kämak  x^a- rii>/^Vi\  pa  iirVi.  —  ')  Uhlenbeck's  Elyroo- logie  WAiSpr.  90  ist  falsch.
j.  ajayaui^aya  H-SJ:  Wei  a/nyaiinia  aya;  i. grai-.
=== aeta
2502:II  'a-  No.  —  ^aeta-  Et  I  i  a.  ii
2530:17  ^aeta-  II 2  z  b  —  aetavant-  18
2540:das  die  fehlenden  NSm.  und  f.  zu  ^aeta-
2549:1 5  3aeta-  H  I  3  b  —  %cta-  II  2  2  a.  16
2558:17  Jaeta-  U  2  a  b  —  aetavant-  i8
3496:•  j.  apa-kava- 1 )  Adj,  'der  hinten,  auf  dem Rücken  einen  Höcker  hat':  mit  ml  aeta- yiisäl  zao^rayä  /mnharintu  frakavö  nttl 'vB  Yt  5.  93.  2)  m.  Name  fUr  solches Gebrechen:  mä  (a%ra)  'vö  2.  29.
=== va oder
21952:V. /5.41:  streiche  vä  beide  Male".] KompE.  (s.  'novo).  —  si.  vä  Part,  'oder'; top.,  np.  u  {va')'),  mp.  aia\v  'oder'").  —  Pü. l)  im  jAw. :  aiäv  (meist  nur  vor  dem  zweiten und  den  folgenden  Gliedern,  einige  Male weggelassen  (iB.  V.  4.  50I;  2)  im  gAw
27868:Gebiss'oder'mitgold(beschlag)encm  Zügel', vom  Pferd;  aspahe  .  .  'nafie  YtS.  18.
```


## [2026-09-06T15:28:30.045Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '21940,21960p' BRT.txt | cut -c1-900; echo \"=== PHD ayab\"; grep -n -E \"ayab|ay-ab|'dwp|)dwp\" PHD_mackenzie.txt | head"
}
```


### [2026-09-06T15:28:30.122Z] TOOL RESULT

```
V  ai  vä  mananha  tastBibya  v°  Y._JJ.  2; 3.  a)  va  . .  va  .  .  im  Sinn  (fast)  von 'et  .  ■  ef  (s.  Sp.  1106  u.)";  a%rä  *vaam baraitl  mi^ahva^ä  V  ^»ns.vaiä  (sd.)  V vldvä  V  rvidvä  v°  Y.  31. 12.  c)  im jAw.;  1)  bei  zwei  Gliedern:  ya^  äauru.- upa.daratu  V  *n)mate.aiwi.varane  V  spä
V  na  v  irihyat  V.8.1;  —  kaiärS  (sdj a'^aurunpm  *parayat  näirika  V  nmänB.- paifis  v  N.  5;  —  aspalm  var3S?m  . .  val- naiti  katärB  ayrave  V  bunavS  v  YX.16. 10, ;4. 31;  —  spä  . ,  pasßm  v°  nar>m  v ralsyat  V.  13. 31 ;  —  spä  pasus.AaurvS  v vishaurvS  v°  Y.13.^^;  —  */rayar?ne  V usayarine  (ad.)  v°  *ayqn  ü.g;  —  *oim tat  v°  . .  ayar>  ä/asaiii . .  atva  i>°  xiapa Aog.  5/^;  —  rasmS.Jatim  v°  dim  jainti amö.jal.'m  v  Yt.  /O.  5  2 ;  —  paourum  V naim?m  *yar>  apanm  V  N.  4^ ;  — anaiwyästa  v*  anabdaiS  (si.)  V  V.  7ÄS4; ^  *maaB  v°  */ra  *»"*'  /aimnS N.jy ;  — US  V  hiHs  ni  v  paiiyamnS  Yt.J.  17; —  atwyätihanim  V  atwy^nhayamnS aiwyärshamm  v'  büjayamns  YtJ.  17;  — ya  nasaum  . .  appin  ä  V  airtm  a  v°  .  . frabarsnti  V.  7. 25";  —  daiingm  ä  V *bar}Snv5  V  
V  asni  paiti  v'  xia/ne  Yt/.  16;  —  pas^ v  parö  v  N.  J2;  —  pas^a  v  pairi v°  *paiti.bar>nti  N.  103;  —  hqm  v°  paiH stairis  hqm  V  paiti  bantis  V.5.3T,  — /rä  V'  apa  v°  sävayeite  H.103;  —  yd ndii  nanm  ajavamm  .  .  xsnaolta  V  xsna- vayäte  v  F-4<);  — yat  kis  spä  v°  aiwi- valnaiii  fra  v'  :^araiti  vayB  vä  (Sp. 1307m.) ..  FrW.//;  — yat. .  vyambura  .. vohunim  V  täcayeinti  Jrasalkfm  V  fraan- lanti  Yt.  14.  54;  —  ferner:  Yt  /.  1 7,  4-  S, Ä60,  //.  4,  /4.  36,  V.^.  25,  40',  ^.44, 5.39,  (7.10',  18,  20,  4J,  45,  46,  7.23,  29, 30,  36,  46,  8.  4,  8',  10,  13,  14,  S3,  g.  14, /j.  10,  40,  /4.1S.  '5-2.  3.  4.  8.  iO.(,, i6.ii„  N./o,  //,  14, 17,  24,37,  4h  4s,  43' (4:5,)"  ^8,  6r/',  83,  loi,  102\  10$,  log;  — s.  noch  Anhang  2;  —  beim  zweiten  Glied steht  yat  v
\yai  haad  V  zaururS  v  pairiita.xsmrö  V
dby  Google
1309
'väUI  2
6av3t  V.J.  19;  —  nairyh  v  pu%raAe  v haeyh  V  marfuyä  Y.ii.i; — yesi  a/sAaf upaOPm  V  aiwinaptlm  v°  . .  V  .  .  f  V. 7,  la;  —  pä^a  ayantim  v'  taBnhm  V V  ..V  V.6.26;  —  tiraos  v°  paiii  sBinma umm  V'  kaiat  V  paiti  siäaranqm  N.  loo; —  vännti  V  snaszinti  v°  bannti  v'  tima- nAqm  V  *aiwi^ais (sd.)  ayqn  v ..vantö. vire  (sd.)  jas»nti  V.  iV.  4;  —  yS  tat  draons ainät  t/'  tn/yät  v° apa  v yäsäiüY.ii.S',  — yS  gatwqm  ..janaiti  v  vayät'i  »*,.  v'  ,.V V-Zj.  5;*—  ferner:  Y.  (j2.  9,  Yt.4.4,  8.\\, JO.18,  J/.4,  75.50,  V.^.  44,  5.5, 12,27,45, 57,  6.46,  8.2,  12,  ß.  II,  y.37,  i4. 17. ^5-9.  14.  z»y-53.N.J5,  26',  J7,  P.i'/,  VyLJO, 2^\  —  s.  noch  Anhang  2;  —  im  Wechsel mW.  yai  vä  (Sp.  1261  f.):  hris  v  /ämaa yat  vä  xsvas  yat  vä  nava  V.5.  51;  — andus  v3  ay
Aus  dem  Zusammenhang  gerissene  oder wertlose  Stellen:  kqmlit  V  vaxlilqm  N. 91'>  —  ya%aca  dim  janal  .  .  yim  vipt}m V'  V.  7.  52  PüZ,; —  5rr  V  azaiti  sraoiö.- iaranaya  altraya  P.  9;  —  dahäiti  v°  ttBil
•va-I  1310
da^aiti  Nik.  s;  —  femer  V.  4.  i  PUZ.,  7.
43  PüZ.»,  H.sS,  Sj',  VyL 25,  26', 44';  — 1  0/  Vä,  yä^a  vä,  yai  vä,  yavat  vä  als  Part. 'sbes.        [V./J.31  i.St:  streiche  »J'";  —
V. /5.41:  streiche  vä  beide  Male".] KompE.  (s.  'novo).  —  si.  vä  Part,  'oder'; top.,  np.  u  {va')'),  mp.  aia\v  'oder'").  —  Pü. l)  im  jAw. :  aiäv  (meist  nur  vor  dem  zweiten und  den  folgenden  Gliedern,  einige  Male weggelassen  (iB.  V.  4.  50I;  2)  im  gAw.  (nur luV.  j/,  17);  aliv*,  (sonst):  u,  i'.i*  oder  weg- gelassen"); Sü.!  vä  oder  ca.  S,  noch  Ko. 3,  g.  —  <)  Das  gemeinsame  Praedikat  zu  zwei in  Disjcnklion  stehenden  singnlarischen  (Y. 31,  17)  oder  singnlarisch ,  weil  kottekliv  ge- dachten (Y.jy.  13)  Subjeklen  steht  im  Dual; vgl.  Bthl.  1F.  /.  226.  —  »)  Vgl.  die  Bedeu- tung des  lat.  vel  bei  Plaulus  und  in  nach- klassischer Zeit;  s.  Schmalz  LGr.J  347  (und 348  lu  live).  So  ergibt  «ich  die  Berechtigung, die  np.  Part,  u  (va')  "und'  »ut  air.  •«j  lurück- zulubren.  Das 
—  *)  ms.Jrävä:  vgl.  PI  4,  Ks,  J3  zu  Y. ig.  6.  —  i)  Die  Stellung  von  vä  erweist  En- klise des  lai  und  —  6)  des  ä.  —  7)  vä  hinter a-(tyd.!laoTim  entspricht  einerseits  dem  vä nach  atidii!  anderseits  dem  vä  und  y^  vä dahinter  (s.  Sp.   iz6i  f.).     Streng  richtig  wäre
—  8)  S.  N0.7.— 9)Pü.:  lässtfiaus.  — 'o)'Das ans  V.  13.  29  stammt.  —  ")  ^  ir.  adäl  (jAw. iiJii/)-)-lfii;  vgl.  dazu  ai.  alhavä.  —  ")  Bei  dem Charakter  der  Pahl.-Schrift  lisst  sich  » überall  ohne  weiteres   ergänzen;   vgl.  No.  a.
•  j.,  g.  'va-  enkl.  Pron.  1.  Pers.  Plur.;  die Formen  stehen  i)  hinter  dem  ersten  Wort des  Vers-  oder  SaUteils,  von  dem  sie aber  a)  durch  em  oder  auch  mehrere enklitische  Wörter  getrennt  sein  können; a)  selten  in  anderer  Stellung.  1)  g.  vh Akk.;  zu  1):  at  va  yazäi  stavas  mazdä ahurä  hadä  asä  . .  Y.50. 4;  8',  gl.  2;  — täii  vä  yasnäii  paitl  stavas  (sd.)  ayen- V-  50.  9 ;  —  mal  va  padäU  (sd.)  . .  patri- Jasai  Y.  50. 8;  —  tjm  *vä''>  ahüm  dr?g. vants  .  .  daOtä  nai^at  (sd.)  Y.  J/,  ao;  litf V,  5.  6  2 ;  —  yä  vS  .  .  *namqm  dadäl  . . hyat  vä  dadat  täis  vi  yaxamaide  V.  ^. 4; — yS  vi  mazda  ahurit  pairf.jasäiisA,) Y.  28.  a;  —  Kng  därayö  (sd.)  ySt  v  ä  daibi- sifUlY. 32.1; — yim  vh  *naeat  dänst  iti
dby  Google
13"
'va-  n
vaek-
13"
=== PHD ayab
ugrep: error: error at position 20
(?m)ayab|ay-ab|'dwp|)dwp
  mismatched ( )___/
```


## [2026-09-06T15:28:47.890Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"ayab\" PHD_mackenzie.txt | head -10; echo \"=== hec in PHD\"; grep -n -i -E \"^he|^hē\" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-06T15:28:47.997Z] TOOL RESULT

```
1364: ayab- v. ayaftan.
5914:acquisitive ayabag.                       agitate ayiirdenidan~
6220:collaboration hamkarih.                  comprehension ayabagih; parwand.
7193:nursing, nurture dayaganih.            or ayab.
7384:  yoJdahrih.                                   receptive ayabag.
10590:drayabiir
12220:ermanag              ,~~                     ayab                        Q)t\Y
12288:ayab-
12290:ayabag                             abun                          ,~
12292:ayabagih             ..&U~~        aburdframanih    .AU~Q)~~
=== hec in PHD
129:hereby made to all whose discoveries have been assimilated within.
2886:hen [hyn l I M hyyn] army.
2888:herbed [hylpt I N herbud] teacher-priest.
2891:herbedestan [hylptst)n l ] priestly school.
2893:heril1 [hylyk I N h/xeri] iris, wallflower.
2895:hezag [hyek I (M hyjg), N hez] pail.
6772:helmd targ.                                    honey anguben; ,..,-bee magas
6773:help (n.) ayarih, dastyarih, frayad,              anguben.
6776:helper ayar, dastgir, dastyar.                 honoured azarmig.
6777:helpful ayaromand, frayadisnig.                hoofsumb.
6778:helpfulness ayaromandih.                       hoop cambar.
6779:hemp san.                                      hope emed, ummed.
6780:hempen sanen.                                  hopeful ummedwar.
6781:hempseed sahdanag.                             hopeless anummed.
6782:hen kark.                                      horn sru; (trumpet) gawdumb.
6783:henbane bang, mang.                            horned srUwar.
6784:hence parron.                                  horny sruwen.
6785:herb marw, riirag ; fragrant ,....., sprahm.   horoscope zayc(ag).
6786:herd ram(ag).                                  horrible aryand; V. terrible.
6787:here edar.                                     horse asp, barag, star.
```


## [2026-09-06T15:28:55.098Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in \"jak\" \"jäzdah\" \"hîč\" \"hi:\" \"aiwaka\" \"êvak\"; do echo \"== $w\"; grep -n -m5 -- \"$w\" HRN.txt | cut -c1-350; done"
}
```


### [2026-09-06T15:28:56.983Z] TOOL RESULT

```
== jak
2582:phlv. aicejak 'rein, lauter'.
3481:bei. tajak 'frisch' (383); kurd. LW. taze,
3958:aw.yäkar- 'Leber; fhlv.jakar bezw. yakar (Bund.);
5980:Urform von zih ist "^jtjaka-,
6181:jänaklh, arm. LW. aspnjakan Gast', cliald. syr. LW.
== jäzdah
== hîč
== hi:
15841:dGhi:>lar 583.
== aiwaka
== êvak
```


## [2026-09-06T15:29:02.822Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"dieser'|'nichts'|,nichts'|,dieser'\" HRN.txt | head -20"
}
```


### [2026-09-06T15:29:02.880Z] TOOL RESULT

```
1604:Tat. i 'dieser'; mäz. ai; Käs. l (kann m mit Verlust
1606:ap. ai'ta- 'dieser'; aw. ae-m-, ae4ad; phlv. e, ecand
```


## [2026-09-06T15:29:04.976Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '1596,1625p' HRN.txt | cut -c1-500"
}
```


### [2026-09-06T15:29:05.024Z] TOOL RESULT

```
*j Hier scheint es aber ^schwach* zu bedeuten.— 32 —
öi und vei sind im Neupersischen zwei Doubletten
ohne jede Bedeutungsnüance ; vei wird dann auch im
Sinne des lat. -plex verwendet.
öweste (nnoziN) siehe unter pest (No. 316).
137. 7? 'dieser in Ider *hier, Jdrä (unbelegt), tderi (Näs.
Xosr.), erä 'desshalb*, edün, Uün (Kasan: etün s. v.
häla) so', Im jetzt', Ime jetzt', esän 'diese' ^).
Tat. i 'dieser'; mäz. ai; Käs. l (kann m mit Verlust
des Nasals sein), e\zün (= tu sän) s. v. cunin,
ap. ai'ta- 'dieser'; aw. ae-m-, ae4ad; phlv. e, ecand
(vd. 7 (27) 61., Var. WH-cawrf; Ganj-I ääyagän 1),
etar^ etün, päz. ercf, ^säw; ai. e-sa-, e-^arf.
kurd. ai 'dieser, ijsäl; oss. a«/; bei. e, f (170).
Auf a/-^a- wird auch das sog. yäi isäret oder
yäi t'arif zurückgeführt (Salemann-Shukovski,
Neup. Grammatik § 19); doch scheint es mir besser,
dasselbe mit dem e des unbestimmten Artikels (yäi
validet) zu identificiren, wie dies nach mündlicher Mit-
teilung Prof. Nöldeke's schon vor Jahren Ewald
gethan hat.
138. ei 'o!'
aw. äi o!'; phlv. ai (vd. 19 (32); N:n vd. 18 (48));
skr. di.
139. ec jemand, etwas', s. hec (No. 1114).
140. Irmän {*er?nan^) 'Gast'^).
aw. airyaman- N. pr. eines Genius; phlv. ermän^
ermänik^ ermämh (Aw.-Komm.); ai. aryamän- 'Busen-
freund, Kamerad'.
Wenn aw. "^a^d^ra- wirklich einmal Teuer' bedeutet
```


## [2026-09-06T15:29:11.548Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"^1114\\.|1114\\. hec|hec \" HRN.txt | head -5; echo ---; grep -n -E \"^\\s*1114\" HRN.txt | head; echo \"=== search 'in 'dieser''\"; grep -n -E \"\\bin\\b.{0,30}dieser\" HRN.txt | head"
}
```


### [2026-09-06T15:29:13.032Z] TOOL RESULT

```
1620:139. ec jemand, etwas', s. hec (No. 1114).
9566:(wie ec neben hec stehej, eine Bemerkung, die VuUers gleich vielem
9616:phlv. ec bezw. hec (päz. hec, hSöi),
---
=== search 'in 'dieser''
37:Gebrauchsspuren, Anmerkungen und andere Randbemerkungen, die im Originalband enthalten sind, finden sich auch in dieser Datei - eine Erin-
165:bücher kann man sich in dieser Beziehung gar nicht ver-
2959:beginnenden in dieser Bedeutung gewiss falsch sind. Als Beleg für
3634:kommen, während die Worte in dieser Form gewöhnlich nur ^Erstling
3680:ist im Neupersischen in dieser Bedeutung aufgegeben.
4980:zitternd', AV. , drafset Bund.); in dieser Bedeutung
8062:*) Natürlich in dieser Form nur das zurückgenommene aramäiHche
```


## [2026-09-06T15:29:15.134Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9605,9625p' HRN.txt | cut -c1-500"
}
```


### [2026-09-06T15:29:15.182Z] TOOL RESULT

```
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
```


## [2026-09-06T15:29:23.115Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"^[0-9]+\\. *j[aä]\" HRN.txt | head -20; echo \"=== u und\"; grep -n -E \"^[0-9]+\\. *u ['‘,]\" HRN.txt | head; echo \"=== in\"; grep -n -E \"^[0-9]+\\. *[iî]n \" HRN.txt | head"
}
```


### [2026-09-06T15:29:23.193Z] TOOL RESULT

```
3868:412. jäme 'Kleid, Gewand'.
=== u und
=== in
```


## [2026-09-06T15:29:26.693Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"aivaka|aiva-ka|ap\\. aiva|aw\\. aeva\" HRN.txt HUB.txt | head -10; echo \"=== HUB yak\"; grep -n -E \"jak |ēvak|evak|aêvak\" HUB.txt | head -10"
}
```


### [2026-09-06T15:29:26.757Z] TOOL RESULT

```
HUB.txt:4969:sammensetzungen Shk. 243 = ap. aiva-).
HUB.txt:5849:= ap. aiva-, paz. Pv- Shk. 243, Min. Gl. 74 ; xnrmd 'Battel',
HUB.txt:8105:ap. aiva- ein* und 6 = ci ^= ap. ciy zusammengesetzt^),
HUB.txt:8780:phi. Svak, ap. aiva-; pOk rein', skr. pavaka-^); nek gut,
HUB.txt:9487:heci any, any thing Shk. 250, Min. 61. 102, ap. aiva-
HRN.txt:9735:C"--' ap. ^aivaka-, vergl. am/- 'ein'; aw. a^oa-; phlv.
=== HUB yak
254:ahanzd = phi. ahanjak 'attracting* Shk. 227) gehort zu einer Wurzel hanj
1118:Im Phi. ist apSdak oder apejak zu lesen, wenn die Schreib-
4550:havar *Glaube ; derjak 'Schneider, np. darzT ; kerp 'Form' =
5475:= phi. vevak ZPGl. 5, 3 aus *viyavak = zd. vidava ZPGl. 5.
5966:(vgl. nek *gut, schon* = phi. nevak, ap. naiba-),
6006:-ewa- zu 5 in nek gut, seh5n* = phi. nevak, ap. naiba-
6405:b) = np. V in : n^v Vacker , phi. nevak schon (— np.
6417:oder V (nevak schon') wiedergegeben wird 2), da ein beson-
7087:= skr. vadhu^; beva 'Wittwe == phi. vevak, zd. Mava,
7925:derjak 'Schneider, Schuster', derjan Taden', handerj *Kleid',
```


## [2026-09-06T15:29:29.606Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9730,9742p' HRN.txt | cut -c1-400; echo \"=== HUB 8105\"; sed -n '8098,8112p' HUB.txt | cut -c1-400; echo \"=== HUB 8780\"; sed -n '8775,8785p' HUB.txt | cut -c1-400"
}
```


### [2026-09-06T15:29:29.678Z] TOOL RESULT

```
,J^o. ^ aw. yazatanqm; phlv. yaztün, yazdän , yaz<i\d\n
^{^y""'"" (Gemmen, Hörn, Mitteilungen Heft IV, 24 No. 2),
yazdaii (Bücher); vergl. ~ized (No. 141).
V4128. yek *ein*.
X Kä^- V. yav, ikt, Q. y, l, ik.
C"--' ap. ^aivaka-, vergl. am/- 'ein'; aw. a^oa-; phlv.
rwak, ev, phlv.-päz. yak (PPGL), ai. eka-,
kurd. Iki jemand' (H.-Sch.), yek (LW.); af;'. yö;
oss. d. yeii, t. yu *ein' (146); bei. eyök einzeln (171);
wa/. li\ ^, sij n. ylv, yu, yä, yi, sar. iv, f, ivj 'einzig,
allein*, ya/n. 7, minj. yao, sangl. vak.
Aus a/?;a- *ein' ist auch das yä-l validet -e ent-
standen.
=== HUB 8105
ha66a (oft bei Firdusi) Junges', das auf phi. *va66ak (aus
vat'Cak oder ahnl.) zuriickgeht und sein cd erst in neuerer
Zeit zu d vereinfacht hat ; xarcang 'Krebs* = phi. kardang
(volksetym. an xar 'Esel' und 6ang angeiehnt ? oben p. 54),
vgl. gr. yapyivog (Lehnwort?); ga6 *Kalk' = paz. gac, aus
phi. *gacc?y vgl. arab. ja?s 'Gips, syr. gessa, gr. yvxpog
(Lehnwort ?) ; hed^ ex *irgend ein', erst im Mp. aus g = gr =
ap. aiva- ein* und 6 = ci ^= ap. ciy zusammengesetzt^),
vgl. agat'ci, mamc (dial.) u. s. w. H. 451.
Aus jiingerer Zeit muss auch das Deminutivsuffix ^)
(fa, tea (VullerS; Gram. p. 234) stammen: bayda 'GtSiTtchen,
aluca 'Mirabelle* [dlu Tflaume'), baztca 'res lusoriae', darlca
'Thiirchen, Fenster, Gussform' = arm. daricak *Gussform'
(11.— 13. Jhd.), huzUa a kid' JRAS. 1894, 448, suroi^ca
*R5theln (auch surxtza, vgl. turbzza *Radieschen' *) von turb
=== HUB 8780
nazdik {nazd) *nahe' (afgh. nazdskl 'Nahe* von nazdB *nahe*,
kurd. nizek, nezik bei Socin, mit ^!); hank *diinn, fein ;
makdk 'WeberschiflPchen, arab. makkuk, syr. pIpD *aiiv(pog\
arm. makoik (5. Jhd.) *Boot, Nachen'; takok 'Weinkrug =
arm. fakoik (5. Jhd.) *Krug u. s. w. Ferner yak ein' =
phi. Svak, ap. aiva-; pOk rein', skr. pavaka-^); nek gut,
schOn = phi. nSvak, ap. naiba- ; bak Turcht' = *bhayaka- ?
dj Piir oder neben a aus ak erscheint ax, ah: surax,
sulax Xoch' = paz. sUla Shk. 268, phi. sUrak^ sUlak Gl.
and Ind. 166; istax = istak = phi. stak *surculus' Bdh. Gl.
175; asna = asnah *Schwimmen' H. 34; dSba = dsbah
```


## [2026-09-06T15:29:38.048Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"'und'|,und'|ut[āa]? 'und\" HUB.txt | grep -n -E \"\\bu\\b|uta\" | head -10; echo \"=== HUB uta\"; grep -n -E \"\\buta\\b\" HUB.txt HRN.txt | head -10"
}
```


### [2026-09-06T15:29:38.116Z] TOOL RESULT

```
=== HUB uta
HRN.txt:9274:ap. tää auch, und'; aw. uta; phlv. u (päz. ?/).
HUB.txt:4835:(u) und* = ap. uta; ustur (sutur) 'Kameel* = zd. mtra-;
HUB.txt:4868:uta *und*, upariy *uber' und upasta 'Beistand' zeigen ; er
```


## [2026-09-06T15:29:40.775Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9268,9280p' HRN.txt | cut -c1-400; echo \"=== HUB 4830\"; sed -n '4828,4840p' HUB.txt | cut -c1-400"
}
```


### [2026-09-06T15:29:40.835Z] TOOL RESULT

```
oder wohl nCi)yöxSUany vergl. nCOyo^s, wie nach MuqaddasI 418, 5 (Nöl-
d e k e ^ s Correktur nach mündlicher Mitteilung) die Bewohner Xüzistän^s
für *höre* sagten. Siehe auch Hörn, KZ. 82, 585 Xo. 18 und vorgl.
unter np. feyfere (No. 806).240 —
V, w.
1071. if, ü (§ähn. I, 25 Vers 37) und*.
ap. tää auch, und'; aw. uta; phlv. u (päz. ?/).
Bei diesem vielgebrauchten Worte ist die nicht
lautgesetzliche starke Verkürzung durchaus erklärlich.
Die Aussprache ve (die wohl AM. noch nicht hat,
vergl. z. B. S. 82, Zeile 3 v. u.) ist Nachahmung des
arab. va und* oder dieses ist selbst entlehnt worden.
Oder gehört np. ü und' zu gr. av, got. auk etc.
=== HUB 4830
§ 20. Ap. I (= idg. %) bleibt im Np. als I, vgl. s%r
'Milch'= skr. HVra- ; dldan *sehen', ap. didiy d. i. *didiy, skr.
dl glanzen ^) (ipt. didlhi und dTdihi)^ u. s. w.
Fiir t erscheint e in ^ir5 *Hals*, girebdn *Kragen*, skr.
grTva- 'Nacken*.
Kapitel 4: ap. u nnd u.
§ 21. Ap. u (= idg. u) bleibt im Np. als u, vgl. u
(u) und* = ap. uta; ustur (sutur) 'Kameel* = zd. mtra-;
xmk 'trocken = ap. uSka-, zd. huika-, skr. guska-; xusur
*Schwiegervater = zd. x^asura- ; Xusrav = zd. husravah-
(arm. Xosrov, gr. XoOpo^g).
§ 22. Anlaut. w vor einfachen Konsonanten in mittel-
persisch zwei- oder mehrsilbigen WSrtern wurde zu a und
```


## [2026-09-06T15:29:49.439Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o -E \".{0,80}I\\.-E\\. base \\*oi-no.{0,400}\" KLN_1966.txt | head -6"
}
```


### [2026-09-06T15:29:54.322Z] TOOL RESULT

```
ugrep: error: error at position 97
(?:[^\n\x80-\xbf][\x80-\xbf]*){0,400}
        exceeds complexity limits___/
```


## [2026-09-06T15:29:56.707Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"oi-no\" KLN_1966.txt | head -12 | cut -c1-500"
}
```


### [2026-09-06T15:29:56.791Z] TOOL RESULT

```
26300:ondoyant,  adj.,  wavy.  —  F.,  ‘waving’,  pres.  part, of  ondoyer,  ‘to  wave’,  fr.  onde,  ‘wave’,  fr.  L. unda.  See  undate  and  -ant. one,  adj.  —  ME.  oon,  on,  an,  fr.  OE.  an,  ‘one’,  rel. to  OS.  en,  ON.  einn,  Dan.  een,  Swed.  en,  OFris. an,  Du.  een,  OHG.,  MHG.,  G.  ein,  Goth,  ains, ‘one’,  fr.  I.-E.  *oi-nos,  whence  also  Gk.  olv3? 0 masc .),  o£vr]  (fern.),  ‘the  ace  (on  dice)’,  OL. oinos,  L.  urns,  ‘one’,  OSl
```


## [2026-09-06T15:29:58.941Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '26300p' KLN_1966.txt | cut -c1-3000"
}
```


### [2026-09-06T15:29:58.993Z] TOOL RESULT

```
ondoyant,  adj.,  wavy.  —  F.,  ‘waving’,  pres.  part, of  ondoyer,  ‘to  wave’,  fr.  onde,  ‘wave’,  fr.  L. unda.  See  undate  and  -ant. one,  adj.  —  ME.  oon,  on,  an,  fr.  OE.  an,  ‘one’,  rel. to  OS.  en,  ON.  einn,  Dan.  een,  Swed.  en,  OFris. an,  Du.  een,  OHG.,  MHG.,  G.  ein,  Goth,  ains, ‘one’,  fr.  I.-E.  *oi-nos,  whence  also  Gk.  olv3? 0 masc .),  o£vr]  (fern.),  ‘the  ace  (on  dice)’,  OL. oinos,  L.  urns,  ‘one’,  OSlav.  -inu  (in  jed-inu, ‘one’),  lit.  prob.  ‘hardly  one’,  and  rel.  to  jedva, ‘hardly’ ;  cp.  also  ino-rogu,  ‘unicorn’, Lith.  vienas, OPruss.  ains,  OIr.  din,  W.,  Co.,  Bret,  un,  ‘one’. The  indef.  article  an  is  derivatively  identical  with one.  Cp.  once,  only,  any,  the  first  element  in Angus,  the  second  element  in  alone,  anon,  atone, nonce,  none,  eleven  and  the  last  element  in  zoll- verein.  Cp.  also  inch,  ounce,  uncia,  uni-,  uni, Unio,  Uniola,  union,  unique,  unit,  unity,  the  first element  in  unanimous,  unison,  universe,  and  the second  element  in  triune.  Cp.  also  eka. Derivatives :  one,  n.  and  indef.  pron.,  one-ness,  n. -one,  a  suff.  indicating  an  organic  compound  of the  ketone  group,  as  in  acetone  (chem.)  —  Gk. -titvrj,  a  fem.  partronymic,  used  in  chemistry  to denote  a  weaker  derivative. oneiro-,  before  a  vowel  oneir-,  combining  form meaning  ‘dream’.  —  Gk.  ovsLpo-,  ovstp-,  fr. ovEtpop,  ‘dream’,  which  is  cogn.  with  Arm. anurj,  ‘dream’,  Alb.  Gheg  qdefe,  Tosk  endefe, ‘dream’.
```


## [2026-09-06T15:30:05.343Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -m1 -o \"onion,  n\\..\\{0,600\\}\" KLN_1966.txt; echo ===; grep -n -m1 -o \"null,  adj\\..\\{0,500\\}\" KLN_1966.txt; echo ===; grep -n -m1 -o \"ounce,  n\\..\\{0,400\\}\" KLN_1966.txt"
}
```


### [2026-09-06T15:30:07.279Z] TOOL RESULT

```
16431:onion,  n.,  the  point  at  the  angle  on  either  side of  the  lower  jaw  ( craniol .)  —  ModL.,  fr.  Gk. ytovla,  ‘angle,  corner’.  See  -gon. gonitis,  n.,  inflammation  of  the  knee  ( med .)  — Medical  L.,  formed  fr.  Gk.  yovu,  ‘knee’,  with suff.  -itis.  See  -gon.
(eval):1: == not found
```


## [2026-09-06T15:30:11.030Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o \"onion,  n\\.,  a  .\\{0,600\\}\" KLN_1966.txt | head -2; echo \"=== null\"; grep -n -o \"null[ ,].\\{0,400\\}nullus.\\{0,200\\}\" KLN_1966.txt | head -3; echo \"=== ounce1\"; grep -n -o \"uncia.\\{0,300\\}\" KLN_1966.txt | head -3"
}
```


### [2026-09-06T15:30:14.993Z] TOOL RESULT

```
26307:onion,  n.,  a  bulbous  plant,  Allium  cepa  —  ME. onion,  fr.  OF.  (=  F.)  oignon,  fr.  L.  unidnem, acc.  of  unid,  ‘onion’,  which  is  usually  derived  fr. unus,  ‘one’,  whence  unid  (fern.),  ‘unity,  union’, unid  ( masc .),  ‘a  kind  of  large  pearl’  (the  sense  of ‘onion’,  would  have  developed  through  the  inter¬ mediary  sense  ‘string  of  onions’ ;  see  one,  union). However,  the  diphthong  oi  in  F.  oignon,  shows that  the  u  in  L.  unid,  ‘onion’,  is  short  and  that, accordingly,  unid  in  this  sense  is  not  a  derivative of  unus,  unless  it  is  assumed  that 
=== null
ugrep: error: error at position 95
:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
      exceeds complexity limits___/


=== ounce1
187:unciation  like  an aleph
253:unciation.  In  this  Dictionary  FI ,  S  ,  3  ,  *1 , 1 , 3  ,  are  transliterated b,  g,  d,  k,  p,  t,  whereas  17 , 3 , 3  ,  "7 . 1 , 3  ,  are  rendered  by  bh,  gh,  dh,  kh,  ph,  th.
1151:unciation  habb-el-mosk,  lit.  ‘grain of  musk’.  See  hubba  and  musk, abelmosk,  n„  a  plant  of  the  mallow  family.  — Fr.  prec.  word.
```


## [2026-09-06T15:30:19.286Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '26307p' KLN_1966.txt | cut -c1-2200"
}
```


### [2026-09-06T15:30:19.339Z] TOOL RESULT

```
Derivatives:  onerous-ly,  adv.,  onerous-ness,  n. oneself,  pron.  —  Compounded  of  one  and  seif, -onic,  a  suff.  denoting  certain  acids  from  an  -ose compound  (sugar),  as  in  glyconic  (chem.) onion,  n.,  a  bulbous  plant,  Allium  cepa  —  ME. onion,  fr.  OF.  (=  F.)  oignon,  fr.  L.  unidnem, acc.  of  unid,  ‘onion’,  which  is  usually  derived  fr. unus,  ‘one’,  whence  unid  (fern.),  ‘unity,  union’, unid  ( masc .),  ‘a  kind  of  large  pearl’  (the  sense  of ‘onion’,  would  have  developed  through  the  inter¬ mediary  sense  ‘string  of  onions’ ;  see  one,  union). However,  the  diphthong  oi  in  F.  oignon,  shows that  the  u  in  L.  unid,  ‘onion’,  is  short  and  that, accordingly,  unid  in  this  sense  is  not  a  derivative of  unus,  unless  it  is  assumed  that  the  u  was shortened  in  Vulgar  Latin;  see  Walde-Hofmann, LEW.,  II,  820  s.v.  1 .  unid,  and  Bloch-Wartburg, DELF.,  p.  421  s.v.  oignon.  Cp.  OProven?. onhon,  ‘onion’,  which  also  comes  fr.  L.  unidnem. OE.  ynne,  ‘onion’,  is  a  Romance  loan  word, only,  adj.,  adv.,  and  conj.  —  ME.  only,  only,  fr. OE.  antic,  ‘unique,  single’,  formed  fr.  an,  ‘one’, with  suff.  -lie,  ‘like’.  See  one  and  -like,  -ly. Derivative:  onli-ness,  n.
```


## [2026-09-06T15:30:38.737Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; ls; python3 - <<'EOF'\nimport re\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\n# find page with '95' heading\nfor i,p in enumerate(pages):\n    if re.search(r'oi-no|oinos|oi-nos', p):\n        print('HIT leaf',i, p[:300].replace('\\n',' '))\n        break\nEOF"
}
```


### [2026-09-06T15:30:40.740Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
leaves 895
HIT leaf 61                             -                  ,                                                                       :                                                 am(m)a          — ames-, omes-                                        53     Uber ai. sam-umd-h „lang“ (Ausdehnung), samamya-h „in
```


## [2026-09-06T15:30:44.301Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; python3 - <<'EOF'\nimport re\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if re.search(r'oi-no', p):\n        s=p.replace('\\n',' ')\n        for m in re.finditer(r'.{0,300}oi-no.{0,600}', s):\n            print('leaf',i,'|',m.group(0)[:900]); print('---')\nEOF"
}
```


### [2026-09-06T15:30:47.279Z] TOOL RESULT

```
leaf 109 | f.)       ai.   5 -vd,    e-vd-ni „so“,         wozu mit der Bedeutungs-Entw. „gerade so, ge- rade der         — nur der — der allein, der eine“;      av. aeva-,           ap. aiva-       „ein,             einzig,           allein“,      gr. olog,   kypr. olfog „allein“ (idg. *oiue, *oiuos).       *oi-nos:       ai.    e-na- „er“ (kann auch *ei-no- sein);      mhd.       ein,       (                              g-einer wie got. j-ains, s. zum j- Brugmann                           einer „jener“ Grdr. II 2 2, 335 f.analog dem neben ahd. obd. ener „jener“ = gr. evt]                                  ;   stehenden iener); mit der Bedeutung „ein‘ ;                                             !       gr. oivog, omj „eins auf dem Wfirfel“, lat. anus, alt oinos, air. den „ein“, cymr. bret. corn, an „ein (als unbestimmter Artikel)“, got. dins, ahd. ein, anord. einn (hierher gehort altn. einka „be
---
leaf 197 | m rai und vd     —       va wie v-na- „dieser“ zu nci—na „auf verschiedene Weise“, ursprfing-                   ,   lich „so und so' ); mit e.-va deckt sieli gr. o\p)og „al]ein“ („*gerade nur                                      !     der‘ ), av. ap. aeva- „ein“ (vgl. mit dem rio-Demonstrativ idg. *oi-no-s „ein“);            :     sehr unsicher umbr. ri-re „citra, citerius(?)“.       S. bes.         Brugmann Dem. 96f., Grdr. II 2 2, 341                                                          — 343. 350, 731         f. m. Lit.  II    2                3. 9S7, Boisacq s. v. av usw. bei Brugmann                             ;                                                                                                                       nocli          Vermutungen fiber lett.           vita:        r- auch das von lett. eiens, lit. deltas „ein‘'                           ,.jener“        
---
leaf 828 |  v.); „gemellus“, zwiniling m., mhd. zwinilin n. Z willing", Himi-na- in     as. twene „zwei“, ahd. zwene ds. (mit e statt ei nach *zwe = got. twai, das es ersetzt hat), ahd. zwein-zug, as. twen-tig, ags. twen-tig „20“ („Doppelzehn“) daB got.   (     tains, ags. tan „Zweig“ eine zz-lose Nebenform *doi-no- enthalte, ist nieht glaublich; Lit. bei Falk-Torp u. ten); germ. *twiz-na- in anord. tvennr, toinnr „zweifach", pi. tvenner „zwei zusammengehorige" ( tvinna „verdoppeln“), ahd. zwirnen, -on „zweifach zusammendrehen", mhd. zwirn, mnd. twern „doppelt zusammengedrehter Faden" wohl = ags. twin, holl. tivijn „Zwirn, Leinen" (ags. getwinne „bini“, getwinnas „Zwillinge“ ist dann auf *twi-nja- zuruckzufiihren), s. Brugmann Grdr. I 2 779, Weyhe PBrB. 30, 56, 65, Falk- Torp     u.   tvinde liber die noch zu klarende Behandlung von -zn- im Wgerm. (fiir    *twlzna als Grundlage von twin fehlen weni
---
```


## [2026-09-06T15:30:55.216Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o \"13\\.11 ONE.\\{0,900\\}\" SYN.txt | head -2; echo \"=== oinos\"; grep -n -o \".\\{0,200\\}\\*oino.\\{0,400\\}\" SYN.txt | head -4"
}
```


### [2026-09-06T15:30:58.910Z] TOOL RESULT

```
=== oinos
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,400}
                        \___exceeds complexity limits
```


## [2026-09-06T15:31:01.464Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"oinos\\|oino-\" SYN.txt | head -6 | cut -c1-1200"
}
```


### [2026-09-06T15:31:01.512Z] TOOL RESULT

```
23849:dice, ace’, but as numeral replaced by ds; OLat. oinos, oenus, Lat. unus (> It., Sp. uno, Fr., Rum. wn); Ir. din, oen, Nir. aon, W. un, Br. unan, eun; Goth. ains, OB Gn, etc., general Gmce.; OPruss. ains, Lith. vienas, Lett. viens (init. v ob- gure); ChSl. ino- in epds., otherwise jdinit (jed-, ed- prefixed pronominal ele- ment), SCr. jedan, Boh., Pol. jeden, Russ. odin; cf. Skt. pron. ena-.
```


## [2026-09-06T15:31:03.722Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '23840,23855p' SYN.txt | cut -c1-1200"
}
```


### [2026-09-06T15:31:03.775Z] TOOL RESULT

```
-ginia, Skt. -gat-, etc.), and partly re- placed by more transparent phrases or epds. (as for 20 Goth. twaz tigjus, OB twen-tig, Lith. dvi-deSimt, Rum. doud- zect),
The decimal system, based on count- ing the fingers, prevails. But the in- fluence of a duodecimal or Sexagesimal system is indicated by certain breaks in the type of formation as that between 12 and 13 in Gmc., between 60 and 70 in Grk., Goth., ete.
The ordinals are formed from the cardinals, mostly with a -to- or -mo- suffix. Exceptions are those for ‘first’ (13.33), and many of those for ‘second’, which are literally ‘the other’ (Goth. anpar, OE oper, ChSl. witori, etc.) or ‘the following’ (Lat. secundus : sequi ‘follow’; similarly Grk. debrepos prob. orig. ‘the one after’, cf. Hom. debraros ‘last’).
For detailed discussion of the IE nu- merals, cf. Brugmann, Grd. 2.2.1 ff.
In the following we list and discuss only those for ‘one’ and ‘first’, and for ‘three’ with derivs., choosing these last as con- venient illustrations of the various types.
er ey ge eS tee ae ae ae
igitized by Arya Samaj Foundation Chennai and eGangotri
QUANTITY AND NUMBER 937 13.832 ONE Goth. ains Lith. vienas ds ON einn Lett. viens tyas Dan. en ChSl. jedint anus Sw. en SCr. jedan uno OE an Boh. jeden un ME oon Pol. jeden uno NE one Russ. odin oun Du. een Skt.  eka- gen OHG ein Av. aéva-, OPers. aiva aon MHG ein oun H i f a NHG em . ; 1B *oi-no-, ete-, derivs. of a pro- *oi-wo-. Av. aéva-, OPers. aiva-; cf. Al gi- beside 7- in Lat. zs, etc. | Grk. ofos, Cypr. offos ‘alone’, and Skt. Mt 1101, Ernout-M. 1127 f. eva ‘thus’,
ide-P. : Doe. Gri. olvés, olvy ‘one on the
dice, ace’, but as numeral replaced by ds; OLat. oinos, oenus, Lat. unus (> It., Sp. uno, Fr., Rum. wn); Ir. din, oen, Nir. aon, W. un, Br. unan, eun; Goth. ains, OB Gn, etc., general Gmce.; OPruss. ains, Lith. vienas, Lett. viens (init. v ob- gure); ChSl. ino- in epds., otherwise jdinit (jed-, ed- prefixed pronominal ele- ment), SCr. jedan, Boh., Pol. jeden, Russ. odin; cf. Skt. pron. ena-.
*oi-ko-. Skt. eka-, cf. aika- in Indic text in Hittite records.
2. Grk. els, gen. évés, fr. és (Cret.), *éus, fem. pla fr. *oula; Toch. A sas masc., sim fem., B se : Grk. duds, Skt. sama-, Goth. sama ‘same’, Grk. aya ‘to- gether’, Lat. semel, Skt. sa-krt ‘once’, etc. Walde-P. 2.488 ff. NG pop. #as with new nom. to acc. é&a.
13.33 ALONE, ONLY (adj.; adv.)
Whe , ‘only? i: oa adjectives ‘alone’ and Feed as in NE alone etentiat allein Vs. einzig, ete., the We of ben 18 idiomatic and mainly '0n, predicative vs. attribu-
VS. 0;
bloss
```


## [2026-09-06T15:31:33.289Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"oinos\\|oinō\\|oino-\" IEC.txt | head -8 | cut -c1-600; echo \"=== SKT\"; grep -n -o \"One, .\\{0,300\\}\" SKT.txt | head -3; grep -n -o \"ONE, single.\\{0,400\\}\" SKT.txt | head -3"
}
```


### [2026-09-06T15:31:35.403Z] TOOL RESULT

```
314:ainos, ainu-, see oinos, sinu-
6235:(in-, form of oin- (?) in Oss. innå “other” beside annà, id.; OCS inü, id. (Cf. inokü ‘monk’, fr. *oinokos (?) with conditioned pho- nology?). Go. jains ‘that’ is a composite prn. (cf. G jener & E yon) apparently a type *id- oinos ‘that one’. Pol. inny (other? suggests *id-ne = “not that ?; inszy is a comparat. form)
7364:kloinos, is, ios “lean, thin? OE hlæne, id.; Li. klienas, id.; OCS cf. (?) na-kljanü “bent
7485:ko-, px. ‘together’; intensive px. ‘very’. WP I, 458. Cf. kom Gk. cf. ko-nnéo (C(know', cf. noéo, noüs); ko-lophón ('peak,, cf. lóphos); kó-labos (*mor- sel”, cf. láb&); kokheuo (lift, fr. *ko-ue$h-?); koinós, adj. (common, cf. oinos "one: Lat. cf. c-0g0, co-actum; Olr. cf. cuman ‘he remem- bered'; cu-ing ‘yoke’; W cy-, cpds.; Blg. cf. kå (before a consonant); kám (before a vowel) ‘to’. (For Gk. kóruza ‘running cold”, cf. Kor-
7509:koinos, is common, united, friendly, mu- tual'. Cf. ko-, oinos & WP I, 370, 398 and 458 Hitt. kaenas wife's kinsman’; Gk. koinós ‘ommon, public, civil’; OIr. cóin, cáin, Ir. caoin “fair, gentle, pleasant’; Br. kün, id.; MW cun ‘kind’; W cun ‘lovely’; Li. dial. kainas (common, mutual. Lalis); Finn. LW kaino ‘modest, shy’; Est. kaine ‘pleasant, calm, pro- per! (?) (Y. H. Toivonen: SKES inconclusive)
8919:kleuinos (Klou-) — Kloinos, om, à, is, io
8933:Kloinos, om, à, is, io ‘sloping, leaning; slope, lean, incline'. WP 490. Cf. Klei-, Klit-, etc. Skt. (?) $rénih, f. "line, group, front’; OIr. MIr. Ir. cloín, clóen, claon 'sloping, bent, wrong, perverse, devious’; MIr. clóene, f. ‘slope’; Ir. claon, m. “trend, deviousness'; MW clun ‘hill;
9001:Kms, -Kms — Koinos, om, à, io
=== SKT
```


## [2026-09-06T15:31:38.640Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"^oinos\" IEC.txt | head -3; grep -n \"oinos, om\" IEC.txt | head -3 | cut -c1-1500"
}
```


### [2026-09-06T15:31:38.770Z] TOOL RESULT

```
12033:oinos, à “one; unit Skt. cf. -enah ‘he’; an-enah ‘this’; ená, adv. “here, there, then, so’; Tokh. winu ‘first’; Gk. oínos, e “ace on a die’; Lat. ünus, a, um; Oscan úin; Olr. oín, óen, Ir. aon; OBr. un-; W un; Cor. cen; Br. ünn, enn, cpds. ün-; Go. ains; MHG ein; OE ån; Du. een; Fris. ien; ON einn; OCS mp, prn. (fa certain; other. In sense (2) prob. fr. *jen-, q.v); OCS cf. vü-ing, vyno ‘always’; Slovene cf. ino-róg *uni-corn'; ino- küpen, adj. "total: OPr. ains "one: Li. viens, id.; Latv. viens, id.; vien ‘only’; Finn. LW ainoa ‘only’. Verbal derivative: Lat. unio, ire; OE &nan; MHG einen
8919:kleuinos (Klou-) — Kloinos, om, à, is, io
8933:Kloinos, om, à, is, io ‘sloping, leaning; slope, lean, incline'. WP 490. Cf. Klei-, Klit-, etc. Skt. (?) $rénih, f. "line, group, front’; OIr. MIr. Ir. cloín, clóen, claon 'sloping, bent, wrong, perverse, devious’; MIr. clóene, f. ‘slope’; Ir. claon, m. “trend, deviousness'; MW clun ‘hill;
9001:Kms, -Kms — Koinos, om, à, io
```


## [2026-09-06T15:31:43.688Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o \"ELEVEN\\..\\{0,300\\}\" SKT.txt | head -2; echo ===; grep -n -o \"ONE\\..\\{0,300\\}\" SKT.txt | head -2; echo ===; grep -n -o \"INCH (1)\\..\\{0,300\\}\" SKT.txt | head -2"
}
```


### [2026-09-06T15:31:45.475Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-06T15:31:48.505Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i -o \"eleven, .\\{0,320\\}\" SKT.txt | head -3; echo \"===\"; grep -n -i -o \"ounce (1), .\\{0,300\\}\" SKT.txt | head -2; echo \"===\"; grep -n -i -o \"inch (1), .\\{0,300\\}\" SKT.txt | head -2"
}
```


### [2026-09-06T15:31:50.595Z] TOOL RESULT

```
===
===
```


## [2026-09-06T15:31:53.334Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"endleofan\\|ellevu\\|ainlif\" SKT.txt KLN_1966.txt | head -5 | cut -c1-800"
}
```


### [2026-09-06T15:31:53.392Z] TOOL RESULT

```
KLN_1966.txt:12825:elevation,  n.  —  F.  elevation ,  fr.  L.  elevationem, acc.  of  elevatio,  ‘a  raising,  lifting’,  fr.  elevatus, pp.  of  elevare.  See  prec.  word  and  -ion. elevator,  n.  —  Late  L.  elevator,  ‘one  who  raises or  lifts’,  fr.  L.  elevatus,  pp.  of  elevare.  See  ele¬ vate  and  agential  suff.  -or. eleven,  adj.  and  n.  —  ME.  elevyn,  enleven,  fr.  OE. endleofan ,  endlufon,  endlyfon,  rel.  to  OS.  elle- Van,  ON.  ellifu,  Dan.  elve,  Swed.  elva,  OFris. andlova,  elleva,  Du.  elf,  OHG.  einlif  MHG. einlif  eilif  eilf  G.  eilf  later  elf  Goth,  ainlif These  words  are  formed  fr.  Teut.  *ain-,  ‘one’, and  I.-E.  base  *liqw-,  ‘to  be  left  over’,  whence also  Gk.  Xeittew,  ‘to  leave  behind,  leave’
```


## [2026-09-06T15:32:00.561Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls site/pages/225.jpg 2>/dev/null; pdftoppm -f 225 -l 225 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg225 && python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg225.png'); print(im.size)\""
}
```


### [2026-09-06T15:32:02.958Z] TOOL RESULT

```
site/pages/225.jpg
(1700, 2200)
```


## [2026-09-06T15:32:05.357Z] TOOL CALL #94: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg225.png"
}
```


### [2026-09-06T15:32:05.827Z] TOOL RESULT

```

```


## [2026-09-06T15:32:05.814Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:32:22.693Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"andasa\\|elf'\\|,elf\\|aevan\" BRT.txt | head -10 | cut -c1-400"
}
```


### [2026-09-06T15:32:22.746Z] TOOL RESULT

```
2685:sat  Kiof);  —  ^kahmai  (s  'vahmi  paüi  .  j.  aevandasa-  Adj.  'der  elfte':  garayd va^Ö  ..  H.  /.  I  s>;  —  yo  g,l%aHqm  dyim  ■>  uzuxiyqn  .  .  'sß  .  .  dvadasS  .  .  Yt.  /p.  2 ; väcim  apayäUi  "vqm^vä  vacastalnm  N.  /.8_  vl/^.g,  5.29  (statt  AS.J;  —  ^ssm 42;  *42,  43;    —    'vo    akunö    vairyS   ..   asar^hamca  V.V.ij.
3003:—  at  ..  dr?grai5  akäU  ^arihäii  (sd.)  •  j-  aka'tara-  Adj.  '(der  bösere,)  beson- paitiurvanöpaityeintl\.40-i\.  a)mitjders,  überaus  böse  (in  Wille  und  Tat) DaL  'Jmdm.  (gegenüber)  böse  (in  Wille  gegenüber-'  (Gen.)":  mtirim  ..  kam}- und  Tat)"':  tum  -kö  rahislasla  mi^ra  rs'.ö.jamm  daevanam  'nm  sraosyanqm ahi  masyJkaHbyS  "du  bist  (je  nachdem
4970:aväjanam  |  *startä   akatiy  "vaiy  (als  AP.)  mä  dauitH 'vaiy  .  .  parsä  Bh.4'i4i  —  hauv  karam fräiSaytr  .  .  vivana^  nilwa"  pärs^  mann 6a!'dakaf'    karj'uvatiyä    xsa>''apJVt1    abty Bli.j.9;  —  kärJ"  kyi^  hamth^iy^ manä  naiy  gaubataiy  °vam  /adiy'Eh.2.'},io; martiyä  tyaisaty  ..anuHyä  äka'tS 'vaiy {3\sAF.)../rdÄ^/am  Bh.  2. 13.-,        i)  II  
9424:blickte  mich  .  ."  V.  22.  2.  lAiiT'isches  Tier  gilt:  baevan  'panqm  ava.-
9755:S""  '■  r  1  «;'  '*■-w^  "■■■  -f^"«  '  ,'■  •  j-  gaevanay-  m.  EN.  eines  Gläubigen: No.  10  f.  —  *)  Hds.  ti-iiaufci;  s.  unten  No.  I4. '      '    "*.  v       ,  ,         v  ,..
15932:•  j.  pazdav-  m,  Name  schädlicher  Klein- tiere, etwa  'Käfer,  Made' :  baevan  'dunam gäks.varttanqm  (sd.)  ava.JanySl  V.  14.  6,
16259:•  j.  pouru.baevan-  Adj.  (auch  fem.)  Viele Zehntausende  betragend';  äatfra^mü  . . fravaiayS  paeins  pourujatk  .  .  pouru.- hazanrh  .  .  'vanS  (NPf.)  YLjj.  65;  — aoa  .  .  urvarä  baisaeyä  utbarym  paoiril pouru.sati  . .  pouru Jtazatsra  . .  *van3  (APC)
16320:•  ).  pouru-hazaura-  Adj,  {fem.  'rä-)  'viele  I Tausende  betragend':  äat  fralüstnti  .  , fravasayS  paoirll  pouru.sata  ,  .  'ra  .  .  \ pouru.daevans  Ytij.6$i  —  a&a  un}ara\ balsazyä  uzbanm  paoirjl  pouru^ala  . .  °rä  I . .  pouru.baevanS  V.  20. 4.
16470:•  j.  baevan-,  baevar-  n.  'Zehntausend, Myriade';  navaca  navaitlsca  navaca  saia navaca  hasattra  navasJs{sA.Ya  •v_qn{^.) Yt  13.  59,  V.  22.  2 ;  —  fravasays  .  .  yä mao^mitncil  myesäinam  °vam  (NP.)  upa- vazinle  "..die  (als  sva.)  inMyriaden . .  herzu- fahren" Yt.jj.  64;  —  urvarh  ..  satavaiti- nqm  hazanravaitinqm  °varf  'varanqm '' V.5.  19  GI.(?).
16636:—  marah)m  .  .  °y?m  raevant»m  Yt.  7. 5; S;  —  'yanqm  asti  (näml.  mihrs)  ai.xra- "iwashmB  Yt/o.  141;  —  tfm  'y^m^^  t?m rafUm  .  .  yiin    ahur?m    mazäam    V,  70.  i ;
```


## [2026-09-06T15:32:44.271Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,40p tools/fetch_source.py"
}
```


### [2026-09-06T15:32:44.314Z] TOOL RESULT

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


## [2026-09-06T15:32:49.640Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/óynos\" \\\n \"https://en.wiktionary.org/wiki/%DB%8C%DA%A9\" \\\n \"https://en.wiktionary.org/wiki/%D9%87%DB%8C%DA%86\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/aiwa\" \\\n \"https://www.etymonline.com/word/one\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 225, root I 2/Io/E: PIE *oinos, NP yak/hič, PIr *aiwa, English one\" 2>&1 | tail -2; done"
}
```


### [2026-09-06T15:32:56.208Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ca30d65bd0ce9212.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3b32677b4b261008.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5407d7f8667c6d5d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b9af9fed777538f7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5e09c32cd60c53bc.txt
```


## [2026-09-06T15:32:59.631Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in ca30d65bd0ce9212 3b32677b4b261008 5407d7f8667c6d5d b9af9fed777538f7; do echo \"########## $f\"; head -c 200 $f.txt; echo; grep -n -i -m6 -E \"Etymology|Proto-Iranian|Middle Persian|Old Persian|Avestan|From\" $f.txt | cut -c1-500; done"
}
```


### [2026-09-06T15:33:02.666Z] TOOL RESULT

```
########## ca30d65bd0ce9212
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/óynos
FETCHED: 2026-09-06T15:32:53Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/h₁óynos - Wiktionary, the free dict
62: Etymology 
145: From Wiktionary, the free dictionary
147: (Redirected from Reconstruction:Proto-Indo-European/óynos ) 
154: Etymology
157: Perhaps built on the pronominal stem *éy ( “ he, she, it ” ) , in which case the suffix would have been used in contradiction to its presumed usage. Homer's use of feminine ἴα ( ía , “ one ” ) , from *ih₂ , directly from the pronominal stem *i- has been suggested as a corroboration for this.
159: Alternative forms in PIE include *Hóywos , attested in Greek and Indo-Iranian (cf. Ancient Greek οἶος ( oîos ) , Avestan 𐬀𐬉𐬎𐬎𐬀 ( aēuua ) ) and *Hóykos , attested only in Indo-Aryan ( Sanskrit एक ( éka ) ).
########## 3b32677b4b261008
URL: https://en.wiktionary.org/wiki/%DB%8C%DA%A9
FETCHED: 2026-09-06T15:32:53Z
STATUS: 200
TITLE: یک - Wiktionary, the free dictionary

یک - Wiktionary, the free dictionary 

 Jump to content 

 M
84: Etymology 
110: Etymology 
127: Etymology 
225: From Wiktionary, the free dictionary
264: Etymology
267: Etymology tree
########## 5407d7f8667c6d5d
URL: https://en.wiktionary.org/wiki/%D9%87%DB%8C%DA%86
FETCHED: 2026-09-06T15:32:55Z
STATUS: 200
TITLE: هیچ - Wiktionary, the free dictionary

هیچ - Wiktionary, the free dictionary 

 Jump to co
62: Etymology 
82: Etymology 
167: From Wiktionary, the free dictionary
174: Etymology
177: Inherited from Old Anatolian Turkish هیچ ( hiç ) , [ 1 ] [ 2 ] from Persian هیچ ( hič ) [ 3 ] 
230: Etymology
########## b9af9fed777538f7
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/aiwa
FETCHED: 2026-09-06T15:32:55Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/aiwa
```


## [2026-09-06T15:33:05.672Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '260,300p' 3b32677b4b261008.txt; echo \"#### hich\"; sed -n '225,260p' 5407d7f8667c6d5d.txt"
}
```


### [2026-09-06T15:33:05.722Z] TOOL RESULT

```
 یه ( ye ) ( colloquial , Tehrani ) 

 یگ ( yag ) ( colloquial , Dari , Eastern Iran ) 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *óywos 
 Proto-Indo-Iranian *Háywas 
 Proto-Iranian *Háywah 
 Middle Persian ʾy 
 Middle Persian ʾywk' 
 Persian یک 

 From Middle Persian [Book Pahlavi needed] ( ʾywk' /⁠yak⁠/ ) , 𐫏𐫐 ( yk /⁠yak⁠/ ) , from Middle Persian: [Book Pahlavi needed] ( ʾy /⁠ē⁠/ ) , 𐭧𐭣 ( HD ) , 𐫙𐫏𐫇 ( ʿyw /⁠ēw⁠/ ) , from Proto-Iranian *Háywah , from Proto-Indo-Iranian *Háywas , from Proto-Indo-European *óywos .

 Indo-European cognates include Bactrian ιωγο , Sanskrit एक ( eka ) , Ancient Greek οἶος ( oîos ) , German ein , French un , English one , Latin ūnus , etc.

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈjak/ 

 ( Dari, formal ) IPA ( key ) : [jäk] 

 ( Dari, formal ) IPA ( key ) : [jäk] 
 ( Kabuli ) IPA ( key ) : [jäk] , [jäɡ] 

 ( Hazaragi ) IPA ( key ) : [jäk] 

 ( Iran, formal ) IPA ( key ) : [jekʰʲ] 

 ( Tajik, formal ) IPA ( key ) : [jäk] 

 Rhymes: -ak 

 Readings

 Classical reading ? 
#### hich
 Kélékian, Diran ( 1911 ), “ هیچ ”, in Dictionnaire turc-français ‎ [3] (in French), Constantinople: Mihran 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 From Middle Persian [Book Pahlavi needed] ( ʾyc /⁠ēč⁠/ , “ not any ” ) .

 This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium . 
Particularly: “The č is probably from Proto-Indo-European *kʷís, *kʷos ( “ who, which, what ” ) . Is the hi a phonetic shift from Proto-Indo-European *né ( “ not ” ) ?”

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈheːt͡ʃ/ 

 ( Dari, formal ) IPA ( key ) : [heːt͡ʃ] 

 ( Dari, formal ) IPA ( key ) : [heːt͡ʃ] 
 ( Kabuli ) IPA ( key ) : [ʔeːt͡ʃ] , [ʔeːd͡ʒ] 

 ( Hazaragi ) IPA ( key ) : [ʔeːt͡ʃ] 

 ( Iran, formal ) IPA ( key ) : [hiːt͡ʃʰ] 

 ( Tajik, formal ) IPA ( key ) : [het͡ʃ] 

 Rhymes: -eːt͡ʃ 

 Readings

 Classical reading ? 

 hēč
```


## [2026-09-06T15:33:17.861Z] TOOL CALL #100: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://en.wiktionary.org/wiki/%D9%88\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%DB%8C%D8%A7\" \\\n \"https://en.wiktionary.org/wiki/%DB%8C%D8%A7%D8%B2%D8%AF%D9%87\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 225, root I 2: Persian و 'and', این 'this', یا 'or', یازده 'eleven'\" 2>&1 | tail -1; done"
}
```


### [2026-09-06T15:33:24.761Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f18734e00b9a9696.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/07fa40f8dab6daca.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2fcb2c44a68e13d3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9c557055960fa7a0.txt
```


## [2026-09-06T15:33:28.100Z] TOOL CALL #101: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in f18734e00b9a9696 07fa40f8dab6daca 2fcb2c44a68e13d3 9c557055960fa7a0; do echo \"##### $f\"; grep -n -A6 -m3 \"^ Persian$\" $f.txt | grep -i -A5 -m2 \"Etymology\" | cut -c1-600; done"
}
```


### [2026-09-06T15:33:30.496Z] TOOL RESULT

```
##### f18734e00b9a9696
##### 07fa40f8dab6daca
##### 2fcb2c44a68e13d3
##### 9c557055960fa7a0
```


## [2026-09-06T15:33:33.548Z] TOOL CALL #102: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in f18734e00b9a9696 07fa40f8dab6daca 2fcb2c44a68e13d3 9c557055960fa7a0; do echo \"##### $f\"; grep -n -i -m8 -E \"From Middle Persian|from Old Persian|Proto-Iranian|Inherited from\" $f.txt | cut -c1-450; done"
}
```


### [2026-09-06T15:33:35.742Z] TOOL RESULT

```
##### f18734e00b9a9696
928: Borrowed from Classical Persian و ( wa ) , from Middle Persian 𐭠𐭥𐭣 ( ʾʿd /⁠ud⁠/ ) , 𐭠𐭥 ( ʾʿ /⁠u⁠/ ) , from Old Persian 𐎢𐎫𐎠 ( u-t-a /⁠utā⁠/ , “ and ” ) , from Proto-Indo-Iranian *(H)utá , *(H)u , from Proto-Indo-European *h₂u .
997: Inherited from Arabic ـُوا ( -ū ) .
1014: Inherited from Arabic ـهُ ( -hu ) .
1094: Inherited from Arabic وَ ( wa , “ and ” ) .
1122: Inherited from Arabic و ( w ) .
1151: Inherited from Arabic و ( w ) .
1225: Inherited from Arabic وَ ( wa , “ and ” ) .
1341: Inherited from Arabic وَ ( wa , “ and ” ) . Some derived terms additionally reflect its Arabic function of introducing an oath.
##### 07fa40f8dab6daca
180: Inherited from Proto-Turkic *īn ( “ lair, burrow ” ) ; [ 1 ] cognate with Old Turkic 𐰃𐰤 ( in ) , Kazakh ін ( in ) , Southern Altai ийин ( iyin ) , Turkmen hīn , Uzbek in and Yakut иин ( iin ) .
239: Inherited from Middle Persian 𐭦𐭭𐭤 ( ēn ) . Compare Mazanderani ام ( am ) , Central Kurdish ئەم ( em ) , Northern Kurdish ev , Alviri-Vidari ام ( am ) . Possibly related to Sanskrit एन ( ena ) .
305: Categories : Ottoman Turkish terms inherited from Proto-Turkic 
310: Persian terms inherited from Middle Persian 
311: Persian terms derived from Middle Persian 
##### 2fcb2c44a68e13d3
283: Inherited from Middle Persian 𐭠𐭩𐭥𐭯 ( ʾywp /⁠ayāb⁠/ ) / 𐫀𐫏𐫀𐫁 ( ʾyʾb /⁠ayāb⁠/ ) . Cognate with Parthian 𐫀𐫃𐫀𐫖 ( ʾgʾm /⁠āgām⁠/ ) . Further etymology unclear; not found in Old Persian.
461: Persian terms inherited from Middle Persian 
462: Persian terms derived from Middle Persian 
##### 9c557055960fa7a0
175: From Middle Persian 𐫏𐫀𐫉𐫅𐫍 ( yʾzdh ) , [Book Pahlavi needed] ( yʾcdẖ /⁠yāzdah⁠/ ) , from earlier *yvāzdah , from Old Persian *aivacadaθa .
238: Categories : Persian terms inherited from Middle Persian 
239: Persian terms inherited from Old Persian 
240: Persian terms derived from Middle Persian 
241: Persian terms derived from Old Persian
```


## [2026-09-06T15:34:34.296Z] TOOL CALL #103: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o \"این (ضمير.\\{0,200\\}\" MON_part1.txt | head -3; echo ===; grep -n -o \"این\\s*\\[.\\{0,200\\}\" MON_part1.txt | head -5; echo \"=== yak\"; grep -n -o \"یک\\s*\\[.\\{0,180\\}\" MON_part2.txt | head -5"
}
```


### [2026-09-06T15:34:36.328Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-06T15:34:39.116Z] TOOL CALL #104: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -c \"\" MON_part1.txt; grep -n -m5 \"این\" MON_part1.txt | cut -c1-300"
}
```


### [2026-09-06T15:34:39.174Z] TOOL RESULT

```
99339
69:این کتاب به سرمایه‌گذاری آقای حمید اله‌بیگی و غلامرضا صابر به چاپ رسیده و 
91:رشتة ادبیات و فلسفه و علوم تربیتی وارد گردید و در سال ۱۳۱۳ از این شعب 
119:دانشگاه؛ ریاست سازمان لفت‌نامه به عهدة وی محول گردید. وی این سمت را تا 
156:شد و تا آخر تابستان آن سال در فرانسه بود. در این مدت یکت سلسله سخنرانی 
187:ایران انتخاب شد و این انتخاب در پائیز ۱۳۴۰ از طرف هیئت وزیران محدداً
```


## [2026-09-06T15:34:43.833Z] TOOL CALL #105: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"^ *این ?\\[|این \\[په|این\\[\" MON_part1.txt | head -5 | cut -c1-300; echo \"=== search پهلوی ēn\"; grep -n -o \"ين \\[.\\{0,120\\}\\|این ‪.\\{0,120\\}\" MON_part1.txt | head -5; echo \"=== grep 'اِ ین'\"; grep -n \"(ضمير اشاره\" MON_part1.txt | head -5 | cut -c1-300"
}
```


### [2026-09-06T15:34:46.054Z] TOOL RESULT

```
=== search پهلوی ēn
=== grep 'اِ ین'
```


## [2026-09-06T15:34:52.657Z] TOOL CALL #106: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \"https://vajehyab.com/moein/%D8%A7%DB%8C%D9%86\" \"https://abadis.ir/fatofa/%D8%A7%DB%8C%D9%86/\"; do timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 225, node 11/12: Mo'in on Persian این\" 2>&1 | tail -1; done"
}
```


### [2026-09-06T15:34:56.632Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/26d8de24d6feebd0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/88ad8c50b199ec57.txt
```


## [2026-09-06T15:34:59.651Z] TOOL CALL #107: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; head -5 26d8de24d6feebd0.txt; grep -n -m5 \"معین\" 26d8de24d6feebd0.txt | cut -c1-400; echo \"#### abadis\"; head -5 88ad8c50b199ec57.txt; grep -n -m6 \"معین\" 88ad8c50b199ec57.txt | cut -c1-400"
}
```


### [2026-09-06T15:34:59.716Z] TOOL RESULT

```
URL: https://vajehyab.com/moein/%D8%A7%DB%8C%D9%86
FETCHED: 2026-09-06T15:34:54Z
STATUS: 200
TITLE: معنی این | فرهنگ انتشارات معین | واژه یاب

4:TITLE: معنی این | فرهنگ انتشارات معین | واژه یاب
9: معنی این | فرهنگ انتشارات معین | واژه یاب 
19: فرهنگ انتشارات معین
#### abadis
URL: https://abadis.ir/fatofa/%D8%A7%DB%8C%D9%86/
FETCHED: 2026-09-06T15:34:56Z
STATUS: 200
TITLE: این - معنی در دیکشنری آبادیس

30: این. ( ضمیر، ص ) ضمیر اشاره برای نزدیک. مقابل آن. ج ، اینها، اینان. ( فرهنگ فارسی معین ). کلمه اشاره که بدان به شخص یا شی حاضر اشاره میکنند. و چون این کلمه پس از موصوف واقع و موصوف بآن اضافه شود الفش در درج ساقط گردد. ( از ناظم ال
37:و گفت تتبع میکن تا این کیست که میگویند پیغمبر خواهد بود. ( فارسنامه ابن البلخی ). || برای اشاره بنزدیک. مقابل آن : این کتاب ، این خانه. ( فرهنگ فارسی معین ) : 
58:۱ - کجا۲ ? - یکی از مقولات نه گان. عرض است و آن بودن چیزی است در مکان معین و مخصوص .
61: فرهنگ معین
132:(در لغت از ادات استفهام و به معنی جا/کجا)؛ در اصطلاح منطق، از اجناس عالیه یا یکی از مقولات عشر ارسطویی. این مقوله بر بودن جسم در مکان خویش دلالت دارد؛ بدین معنی که از بودن چیزی در مکان معین، هیئتی پدید می آید که از آن به أین
255:منبع فرهنگ فارسی معین
```


## [2026-09-06T15:35:08.159Z] TOOL CALL #108: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; python3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    s=p.replace('\\n',' ')\n    for m in re.finditer(r'.{0,80}(یک|این|هیچ|یازده)\\s*[:.\\-].{0,200}', s):\n        g=m.group(0)\n        if re.search(r'[A-Za-z]{3,}', g) and re.search(r'(oi|ein|aiva|ēv|ev|ut|ena)', g):\n            print(i,'|',g[:280])\nEOF"
}
```


### [2026-09-06T15:35:12.210Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:35:15.847Z] TOOL CALL #109: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; grep -n -o \".\\{0,120\\}aivaka.\\{0,200\\}\" ARY_pages.txt | head -3; echo ===; grep -n -o \".\\{0,150\\}oinos.\\{0,200\\}\" ARY_pages.txt | head -3; echo ===; grep -n -o \".\\{0,150\\}évak\\|.\\{0,150\\}evak.\\{0,150\\}\" ARY_pages.txt | head -5"
}
```


### [2026-09-06T15:35:19.175Z] TOOL RESULT

```
Exit code 1
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,200}
                        \___exceeds complexity limits


(eval):1: == not found
```


## [2026-09-06T15:35:22.331Z] TOOL CALL #110: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; grep -n \"aivaka\" ARY_pages.txt | head -3 | cut -c1-400; echo \"=== oino\"; grep -n \"oino\\|oi-no\" ARY_pages.txt | head -3 | cut -c1-400; echo \"=== uta\"; grep -n \"évak\\|evak\" ARY_pages.txt | head -4 | cut -c1-400"
}
```


### [2026-09-06T15:35:22.408Z] TOOL RESULT

```
=== oino
=== uta
```


## [2026-09-06T15:35:27.746Z] TOOL CALL #111: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -m3 -o \"Old English an .\\{0,600\\}\" 5e09c32cd60c53bc.txt | cut -c1-800"
}
```


### [2026-09-06T15:35:29.512Z] TOOL RESULT

```
25:Old English an (adjective, pronoun, noun) "one," from Proto-Germanic *ainaz (source also of Old Norse einn , Danish een , Old Frisian an , Dutch een , German ein , Gothic ains ), from PIE root *oi-no- "one, unique."
91:Old English an (with a long vowel) "one; lone," also used as a prefix meaning "single, lone" (as in anboren "only-begotten," anhorn "unicorn," anspræce "speaking as one"). See one for the divergence of that word fr
```


## [2026-09-06T15:35:34.788Z] TOOL CALL #112: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg225.png data/verification/sources/refs/ocr/BOOK/225.png && ls -la data/verification/sources/refs/ocr/BOOK/225.png"
}
```


### [2026-09-06T15:35:34.854Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 80963 Sep  6 11:35 data/verification/sources/refs/ocr/BOOK/225.png
```


## [2026-09-06T15:36:19.719Z] AGENT

Now I'll write the verification file.


## [2026-09-06T15:49:13.172Z] TOOL CALL #113: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build225.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Indo-European\",\n \"words\": \"Au 3, Auo, Oi-no : one, this one ; Uě, Uo : or\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Every form in this box is real, but the box unites two entries that Pokorny keeps apart. (a) *oi-no- 'one' is genuinely a derivative of the root box's pronominal stem: Pokorny prints it inside the entry 'e-3, ei-, i-' at p.286 ('oi-nos: ai. e-na- „er“ ... gr. oinos „eins auf dem Würfel“, lat. ūnus, alt oinos ... got. ains, ahd. ein, anord. einn'), and Buck (Selected Synonyms 13.32) says the same in so many words: 'IE *oi-no-, *oi-wo-, derivs. of a pronominal stem *e-/*o-'. The parallel *oi-ṳo- (Nourai's 'Auo') is what gives Av. aēva-, OP aiva-, Gk. oios: Pokorny p.286 'ai. e-vā, e-vām „so“ ... av. aēva-, apers. aiva- „ein, einzig, allein“, gr. oios ... (idg. *oiṳe, *oiṳos)'. (b) 'Au 3' and 'Uě, Uo' are however Pokorny's SEPARATE root, IEW 73-75, printed there as '4. au-, u- (: ṳe-, ṳo-) Pronominalstamm „jener“', whose ṳe-/ṳo- branch means 'or' (skt. vā, Av./OP vā, Lat. -ve) and whose u-ta branch gives Av. uta 'and'. Pokorny cross-refers the two ('av. aēva-, apers. aiva- ... s. auch oben S. 75'), because the second element of *oi-ṳo- is the *-ṳ- particle, but he does not derive au-/ṳe- from e-/ei-/i-, and no modern handbook (Beekes, de Vaan, LIV) unites *h₁e-/*h₁i- with *h₂eu-. So the box is right about the words and about *oi-no-/*oi-ṳo-, but it hangs 'Au/Uě/Uo' (and hence node 5, uta) on a parent they do not descend from.\",\n \"derivation_fa\": \"همهٔ صورت‌های این جعبه اصیل‌اند، ولی در واقع دو مدخل جداگانهٔ پوکورنی را در یک جا آورده است. نخست، *oi-no- «یک» و *oi-ṳo- گونهٔ دیگر آن، راستی مشتق از همین ستاک ضمیری اند: پوکورنی در صفحهٔ ۲۸۶، درون همین مدخل e-3، می‌نویسد «oi-nos: سنسکریت e-na-، لاتین ūnus (کهن oinos)، گوتی ains» و همان‌جا «اوستایی aēva-، پارسی باستان aiva- «یک، تنها»». باک نیز در فرهنگ مترادفات (۱۳.۳۲) همین را می‌گوید. اما «Au 3» و «Uě، Uo» در پوکورنی ریشهٔ جداگانه‌ای است (صفحات ۷۳–۷۵: «4. au-, u- (: ṳe-, ṳo-) ستاک ضمیری «آن»») که شاخهٔ ṳe-/ṳo- آن معنای «یا» دارد و شاخهٔ u-ta آن اوستایی uta «و» را می‌دهد. پس ادعای نورایی دربارهٔ خود واژه‌ها درست است، ولی پیوند زدن «Au/Uě/Uo» به ریشهٔ E/I در پژوهش امروزی پذیرفته نیست و با احتیاط باید خوانده شود.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C3%B3ynos\"],\n \"ref_check\": [\n   {\"ref\": \"POK:73\", \"status\": \"supports\", \"note\": \"POK_01.txt, printed p.73 (line marker '73' at line 977): '4. au-, u- (: ue-, uo-) Pronominalstamm „jener“, auch gegenüberstellend „der eine — der andrerseits“' — Nourai's 'Au 3, Auo' (his own root numbering; Pokorny numbers it au- 4).\"},\n   {\"ref\": \"POK:75\", \"status\": \"supports\", \"note\": \"POK_01.txt p.75: 'ue-, uo-: Die Bed. „oder“ (= „andrerseits“) bes. in ai. vā „oder“ ... av. ap. vā „oder“' — exactly Nourai's 'Uě, Uo : or'. Same page: 'mit e-vā deckt sich gr. oios „allein“, av. aēva-, apers. aiva- „ein“ (vgl. mit dem no-Demonstrativ idg. *oi-no-s „ein“)'.\"},\n   {\"ref\": \"POK:281\", \"status\": \"supports\", \"note\": \"POK_full.txt 'Root / lemma: e-3, ei-, i-, fem. i- … Page(s): 281-286' — the entry under which *oi-no- is printed.\"},\n   {\"ref\": \"POK:286\", \"status\": \"supports\", \"note\": \"POK_01.txt p.286 (page marker at line 4095): 'oi-nos: ai. e-na- „er“ … gr. oinos, oine „eins auf dem Würfel“; lat. ūnus, alt oinos; air. óen; got. ains, ahd. ein, anord. einn' — Nourai's 'Oi-no : one'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I (WP I 95 ff.), pages file leaf 109\", \"stance\": \"supports\", \"note\": \"'*oi-nos: ai. e-na- „er“ … gr. oinos, oine „eins auf dem Würfel“, lat. anus [ūnus], alt oinos, air. óen „ein“ … got. áins, ahd. ein, anord. einn'; and leaf 197 (WP I 187 f., the au-/u- article): 'mit e-va deckt sich gr. oios „allein“, av. ap. aeva- „ein“ (vgl. mit dem no-Demonstrativ idg. *oi-no-s „ein“)' — i.e. Walde-Pokorny too prints the material in TWO separate articles.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. oi-no- and s.v. i-\", \"stance\": \"supports\", \"note\": \"'oi-no-. One, unique. I. Basic form *oi-no- … [In Pok. e- 281.]' and 'i-. Pronominal stem … [Pok. 3. e- 281.]' — Watkins files *oi-no- under Pokorny's e- 281, exactly as the chart does.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 13.32 ONE, p.937\", \"stance\": \"supports\", \"note\": \"'IE *oi-no-, *oi-wo-, derivs. of a pronominal stem *e-/*o-, cf. *i- beside *e- in Lat. is … *oi-wo-: Av. aēva-, OPers. aiva-; cf. Grk. oios, Cypr. oiwos „alone” … *oi-no-: … OLat. oinos, Lat. ūnus … Goth. ains, OE ān … cf. Skt. pron. ena-.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, s.v. oinos\", \"stance\": \"supports\", \"note\": \"'oinos, ā “one; unit” Skt. cf. -enaḥ “he”; an-enaḥ “this”; enā adv. … Gk. oinós; Lat. ūnus … Go. ains; OE ān … Verbal derivative: Lat. unio, ire.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Avestan / Old Persian\",\n \"words\": \"ava 2, aiva, aěva, aeva, aivaka : one ; aeva-data, aeva-dasa : eleven ; aiva-čiy : nothing ; va, vâ : or\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"aeva-data, aeva-dasa\",\n \"correct_form\": \"aēvandasa- (Av. 'eleventh', Bartholomae col. 2685) / aevadasa (Mo'in, BQT 2417); OP *aiva-daθa\",\n \"derivation\": \"Four of the five items are exactly right. (1) ava- 'that' is the aua-/aṳo- deictic of Pokorny 73 ('auo: ai. av. apers. ava- „jener“'). (2) Av. aēva-, OP aiva- 'one' < *oi-ṳo-: Kent, Old Persian, Lexicon p.164 s.v. 'aiva- adj. “one” (§150; §204.1): Av. aēva- “one”, Gk. Hom. oios, Cypr. oiwos “alone”, pIE *oiwos'; Bartholomae col. 2660 'p. aiva-, j., g. aēva-, j. ōiva- Zw. „ein“'. The -ka- form aivaka- is the Old Iranian ancestor of Pahlavi ēvak/yak (Nyberg II 66: 'ēvak … Av. aēva-, OP aiva- + -ka-'; Horn no.1128 'ap. *aivaka-'). (3) aiva-čiy 'not anything' = *aiva- 'one' + the indefinite enclitic -čiy (< PIE *kʷi-, Nourai's root Kwo): Horn no.1114 s.v. hēč derives it 'ap. *aiva + čiy (Salemann)', Hübschmann the same ('hēč, ēč „irgend ein“, erst im Mp. aus ē = *ēv = ap. aiva- “ein” und č = či = ap. čiy zusammengesetzt'). (4) va, vā 'or' = Pokorny 75 'av. ap. vā „oder“'; Bartholomae cols. 1306-1310 heads the article 'vā Part. „oder“'. THE ONE BAD FORM is 'aeva-data': no Avestan or Old Persian word of that shape exists. The attested Avestan is aēvandasa- 'the eleventh' (Bartholomae col. 2685 'j. aēvandasa- Adj. „der elfte“'), and Mo'in's own footnote on the page Nourai cites (BQT 2417) prints 'aēvadasa'. 'aeva-data' is therefore either a straight misprint for 'aeva-dasa' — the two stand side by side on the printed page — or a very loose rendering of an Old Persian *aiva-daθa (OP θ for Av. s from PIE *ḱ, as in the Dekm root itself) with θ set as t. I checked the printed page (pdf 225 = book p.195, image copied to data/verification/sources/refs/ocr/BOOK/225.png): the book itself reads 'aeva-data, aeva-dasa', so the extraction is faithful and the fault is the author's/printer's.\",\n \"derivation_fa\": \"چهار قلم از پنج قلم این گره درست است. ava- «آن» همان ضمیر اشارهٔ auo- پوکورنی (ص ۷۳) است؛ اوستایی aēva- و پارسی باستان aiva- «یک» از *oi-ṳo- است (کنت، فرهنگ پارسی باستان ص ۱۶۴؛ بارتولمه ستون ۲۶۶۰)، و گونهٔ پسونددار aivaka- نیای فارسی میانهٔ ēvak است (نیبرگ؛ هرن شمارهٔ ۱۱۲۸). aiva-čiy «هیچ» مرکب است از aiva- «یک» + پی‌بست نامعین -čiy (هرن شمارهٔ ۱۱۱۴؛ هوبشمان). vā «یا» نیز در بارتولمه ستون ۱۳۰۹ مدخل جداگانه دارد. اما صورت aeva-data در هیچ منبعی نیست؛ صورت مضبوط اوستایی aēvandasa- «یازدهم» است (بارتولمه ستون ۲۶۸۵) و حاشیهٔ معین بر برهان قاطع (ص ۲۴۱۷) هم aevadasa می‌نویسد. پس یا خطای چاپی کتاب است به جای aeva-dasa، یا نوشتن نادقیق پارسی باستان *aiva-daθa (تبدیل θ به t در حروف‌چینی). تصویر صفحهٔ چاپی (ص ۱۹۵ کتاب) را دیدم: خود کتاب «aeva-data» دارد؛ پس خطای خوانش اسکن نیست، خطای خود کتاب است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C3%B3ynos\", \"https://en.wiktionary.org/wiki/%DB%8C%DA%A9\"],\n \"ref_check\": [\n   {\"ref\": \"POK:73\", \"status\": \"supports\", \"note\": \"POK_01.txt p.73: 'auo-: Ai. av. apers. ava- „jener“' — Nourai's 'ava 2'.\"},\n   {\"ref\": \"POK:75\", \"status\": \"supports\", \"note\": \"POK_01.txt p.75: 'ue-, uo-: … av. ap. vā „oder“ (auch Partikel der Hervorhebung und Versicherung)' and 'av. aeva-, apers. aiva- „ein“'.\"},\n   {\"ref\": \"POK:286\", \"status\": \"supports\", \"note\": \"POK_01.txt p.286: 'av. aeva-, apers. aiva- „ein, einzig, allein“, gr. oios, kypr. oiwos „allein“ (idg. *oiue, *oiuos); s. auch oben S. 75.'\"},\n   {\"ref\": \"BQT:2417\", \"status\": \"supports\", \"note\": \"Read from the page image (vol.4 pdf p.500; saved as ocr/BQT/2417.vision.txt): Mo'in's footnote 5 'یازده – بفتح دال = یانزده، اوستا aevadasa (یازدهم)، پهلوی yâcdah-um' — supports 'aeva-dasa : eleven' (and node 3's yâcdah), but prints dasa, not 'data'.\"},\n   {\"ref\": \"KNT:164\", \"status\": \"supports\", \"note\": \"KNT.txt leaf 186 (Lexicon, printed p.164; the running number 165 stands after the following entry): 'aiva- adj. “one” (§150; §204.1): Av. aēva- “one”, Gk. Hom. oios, Cypr. oiwos “alone”, pIE *oiwos.' The same page also carries 'aita- … asn. DPd 20; DNa 53' (node 9).\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 2660 (aiva-/aēva-), col. 2685 (aēvandasa-), cols. 1306-1310 (vā)\", \"stance\": \"partial\", \"note\": \"'p. aiva-, j., g. aeva-, j. oiva- Zw. (fem. -yā-) „ein“'; 'j. aēvandasa- Adj. „der elfte“'; 'vā Part. „oder“; … np. u (va), mp. aiāv „oder“'. Bartholomae has aēvandasa-, NOT 'aeva-data' — the ground for the transcription flag.\"},\n   {\"src\": \"KNT\", \"where\": \"Lexicon p.164\", \"stance\": \"supports\", \"note\": \"aiva- 'one' with Av. aēva- and pIE *oiwos, as quoted above.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 1114 (hēč) and no. 1128 (yek)\", \"stance\": \"supports\", \"note\": \"'1114. hēč „jemand, jemals“, mit Negation „niemand, nichts“ … ap. *aiva + čiy (Salemann, Mél. asiat. IX, 241); phlv. ēč bezw. hēč'; '1128. yek „ein“ … ap. *aivaka-, vergl. aiva- „ein“; aw. aēva-'.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien, p. ~205 (č-chapter) and § on -ak\", \"stance\": \"supports\", \"note\": \"'hēč, ēč „irgend ein“, erst im Mp. aus ē = *ēv = ap. aiva- “ein” und č = či = ap. čiy zusammengesetzt'; and 'yak „ein“ = phl. ēvak, ap. aiva-'.\"},\n   {\"src\": \"GPL\", \"where\": \"Platts-Ranking, Grammar of the Persian Language, p.41 (running head 'Numerals—The Cardinal Numbers 41')\", \"stance\": \"supports\", \"note\": \"'1. یک yak (Phl. ēvak; O.P. aiva). … 11. یازده (dialec. یاوزده) (O.P. aivadasa).' Platts gives the eleven-word as aiva-dasa, again with -s-.\"}\n ]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Pahlavi\",\n \"words\": \"ěvak, yak : one ; yâcdah : eleven ; hěč : nothing ; ayâb, ayâ, ayâo : or\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Three of the four are textbook Middle Persian. ēvak/ēk (Book Pahlavi <ʾywkʹ>, Manichaean yk) 'one' = OIr. *aivaka-: MacKenzie, CPD s.v. 'ēk [ʾywk | M yk, N yak] one' and 'ē(w) [HD < A ḥd | M ʾyw, N -ē] a, one'; Nyberg II s.v. 'ēvak [HDwkʹ; on coins ʾywky] num. one … Av. aēva-, OP aiva- + -ka-, … MPrs yk; Paz. yak, iak, NP yak'. The Manichaean by-form yak, with the prothetic glide of ē- > yē- > ya-, is the direct ancestor of NP yak, so Nourai's listing 'ēvak, yak' inside one Pahlavi box is right. yācdah 'eleven' is simply the Book Pahlavi spelling <yʾcdh> of yāzdah: MacKenzie 'yazdah [yʾcdh | M yʾzdh, N -] eleven' — Nourai took the form from Mo'in's footnote on BQT 2417, which prints 'yâcdah-um'. hēč 'anything, (with negation) nothing' = *aiva-čiy, Nyberg II 'hēč [hyc] any, in neg. sentences, placed before its headword: ~ kas anyone'. The fourth item, ayāb (also read ayāw/ayāp) 'or' is where the arrow is only half right: Bartholomae, who gives 'aiāv' as the Pahlavi rendering of Avestan vā, analyses it in his footnote 11 as Old Iranian aδāt (jAw. aδāt) + vā, cf. Skt. athavā — that is, only its SECOND element is the vā of node 2; Wiktionary flatly says of the word 'Further etymology unclear; not found in Old Persian.' 'ayâo' is not a standard reading; the usual transliterations are ayāb / ayāw / ayāp (Paz. ayō).\",\n \"derivation_fa\": \"سه قلم از چهار قلم، فارسی میانهٔ استواری است. ēvak/ēk (به خط پهلوی کتابی <ʾywkʹ> و به خط مانوی yk) «یک» از ایرانی باستان *aivaka- است؛ مکنزی می‌نویسد «ēk [ʾywk | M yk, N yak] one» و نیبرگ صریحاً می‌گوید «ēvak … اوستایی aēva-، پارسی باستان aiva- + -ka-، فارسی نو yak». گونهٔ مانوی yak که با رویش یای آغازین از ē- پدید آمده، خود نیای مستقیم «یک» فارسی است. yācdah همان املای پهلوی کتابی <yʾcdh> برای yāzdah است (مکنزی: «yazdah [yʾcdh] eleven»)؛ نورایی آن را از حاشیهٔ معین (برهان قاطع ص ۲۴۱۷ «yâcdah-um») گرفته است. hēč هم در واژه‌نامهٔ نیبرگ آمده است. اما دربارهٔ ayāb «یا» باید احتیاط کرد: بارتولمه آن را مرکب از aδāt + vā می‌داند (قیاس کنید با سنسکریت athavā)، یعنی تنها جزء دوم آن همان vāی گرهٔ پیشین است؛ ویکی‌واژه نیز ریشهٔ دورتر آن را ناروشن می‌خواند. خوانش «ayâo» نیز معیار نیست؛ خوانش‌های رایج ayāb/ayāw/ayāp است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%DB%8C%DA%A9\", \"https://en.wiktionary.org/wiki/%DB%8C%D8%A7\"],\n \"ref_check\": [\n   {\"ref\": \"BQT\", \"status\": \"supports\", \"note\": \"Cited without a page; the relevant pages are the ones cited on the daughter node: BQT 2417 (Mo'in: 'پهلوی yâcdah-um') and BQT 2446 (یگان/یگانه 'از: یک (<یکه) + آنه … پهلوی ēvakānak'). Both support ēvak/yācdah.\"},\n   {\"ref\": \"SNS:91\", \"status\": \"not_found\", \"note\": \"SNS_pages.txt (Tavoosi's Shayast-ne-Shayast glossary, 242 leaves) does contain 'ēvak' (leaf 62) and 'ayāb' (leaf 61) and 'ēvakīh' (leaf 163), and the back index has 'har ēvak 92/2'; but the scan's printed page numbers are not readable in the OCR, and the numbers inside the glossary are page/line references INTO the Pahlavi text, not the book's own pages, so 'SNS:91' cannot be located with certainty.\"},\n   {\"ref\": \"GPL:41\", \"status\": \"supports\", \"note\": \"GPL.txt, running head 'Numerals—The Cardinal Numbers 41': '1. یک (Phl. ēvak; O.P. aiva)' and '11. یازده (dialec. یاوزده) (O.P. aivadasa)' — precisely the Pahlavi ēvak and the eleven-word Nourai puts in this box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.vv. ēk, ē(w), yazdah, ēn, im, ud, and the English index 'or ayab'\", \"stance\": \"supports\", \"note\": \"'ēk [ʾywk | M yk, N yak] one'; 'ē(w) [HD < A ḥd | M ʾyw, N -ē] a, one'; 'yazdah [yʾcdh | M yʾzdh, N -] eleven'; index 'or ayab.' MacKenzie reads <ʾywk> as ēk where the older tradition (Nyberg, Mo'in, Nourai) reads ēvak.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. ēvak and s.v. hēč\", \"stance\": \"supports\", \"note\": \"'ēvak [HDwkʹ; on coins ʾywky] num. one, passim … — Av. aēva-, OP aiva- + -ka-, v. s.v. ʾē; MPrs yk; Paz. yak, iak, NP yak — as against MPrth ʾyw “one”'; 'hēč [hyc] any, in neg. sentences, placed before its headw.'\"},\n   {\"src\": \"BRT\", \"where\": \"cols. 1306-1310 s.v. vā, note 11\", \"stance\": \"partial\", \"note\": \"'vā Part. „oder“; … mp. aiāv „oder“' with footnote 11 '= ir. aδāt (jAw. aδāt) + vā; vgl. dazu ai. athavā' — so Pahlavi ayāv contains vā but is a compound, not a simple continuation of it.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Persian\",\n \"words\": \"yak, yek «یک» : one ; yâzdah «یازده» : eleven ; hîč «هیچ» : nothing, no ; yâ «یا» : or\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All four are the regular New Persian continuations of the Pahlavi box above. یک yak/yek < MP <ʾywkʹ> ēvak/ēk, through the Manichaean-attested by-form yak (ē- acquires a prothetic y-, then the -v-/-ē- of the first syllable is lost): Horn no.1128 'yek „ein“ … ap. *aivaka- … phlv. ēvak, ēv, phlv.-pāz. yak'; Hübschmann 'yak “ein” = phl. ēvak, ap. aiva-'; Wiktionary gives the same chain NP یک < MP ʾywkʹ /yak/ < MP ʾy /ē/ < PIr. *Háywah < PIE *óywos. یازده yāzdah < MP yāzdah (Book Pahlavi <yʾcdh>) < *yēv-dah 'one-ten', with the -nz- of the dialectal یانزده an intrusive nasal; Mo'in (BQT 2417) traces it to Av. aevadasa. هیچ hīč < MP hēč/ēč < OP *aiva-čiy 'any one thing at all', which in negative clauses became the negative-polarity word 'nothing, no' — the h- is the secondary aspiration seen already in Pahlavi (ēč beside hēč). یا yā 'or' < MP ayāb, with loss of the final -b and of the initial a- (ayāb > ayā > yā), exactly the two by-forms Nourai lists in node 3; Wiktionary: 'Inherited from Middle Persian ʾywp / ʾyʾb (ayāb).' Nourai's glosses and Persian script are correct throughout.\",\n \"derivation_fa\": \"هر چهار واژه دنبالهٔ قانونمند گرهٔ پهلوی بالایند. «یک» از فارسی میانهٔ ēvak/ēk است و از راه گونهٔ مانوی yak (با رویش یای آغازین و افتادن واکهٔ کشیده)؛ هرن (شمارهٔ ۱۱۲۸) و هوبشمان همین را می‌گویند و ویکی‌واژه زنجیرهٔ یک < ʾywkʹ < ʾy (ē) < ایرانی آغازین *Háywah < هندواروپایی *óywos را می‌دهد. «یازده» از yāzdah پهلوی (املای <yʾcdh>) و در اصل *yēv-dah «یک–ده» است؛ گونهٔ گویشی «یانزده» نون میانجی گرفته است. «هیچ» از hēč/ēč پهلوی و آن از *aiva-čiy پارسی باستان «یک چیز هر چه باشد» است که در جملهٔ منفی معنای «هیچ» گرفته است. «یا» از ayāb پهلوی است با افتادن بای پایانی و الف آغازین (ayāb > ayā > yā). ادعای نورایی در این گره درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%DB%8C%DA%A9\", \"https://en.wiktionary.org/wiki/%D9%87%DB%8C%DA%86\", \"https://en.wiktionary.org/wiki/%DB%8C%D8%A7\", \"https://en.wiktionary.org/wiki/%DB%8C%D8%A7%D8%B2%D8%AF%D9%87\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:2417\", \"status\": \"supports\", \"note\": \"Page image read (ocr/BQT/2417.vision.txt): 'یازده – بفتح دال = یانزده، اوستا aevadasa (یازدهم)، پهلوی yâcdah-um (یازدهم)، کردی yânzdeh، افغانی yôlas …، گیلکی yânzdâ؛ ده بعلاوهٔ یک، عدد بین ده و دوازده.'\"},\n   {\"ref\": \"BQT:2446\", \"status\": \"supports\", \"note\": \"BQT_v4_pages.txt [pdf page 529] = printed 2446: entries یگان، یگانه، یگانگی with Mo'in's footnotes 'یگان. از: یک (<یکه) + آن' and 'از: یک (*یکه) + آنه [پارسی باستان aivaka …] پهلوی ēvakānak' — i.e. Mo'in's own یک < Pahlavi ēvak < OP aivaka, the chain of this node.\"},\n   {\"ref\": \"SNS:86\", \"status\": \"not_checked\", \"note\": \"Tavoosi's glossary: printed page numbers unreadable in the scan's OCR and the glossary's own numerals are references into the Pahlavi text; page 86 could not be located.\"},\n   {\"ref\": \"SNS:91\", \"status\": \"not_found\", \"note\": \"Same problem; the words themselves (ēvak, ayāb, hēč) are in the glossary (leaves 61-62) but not mappable to printed p.91.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 1128 (yek) and no. 1114 (hēč)\", \"stance\": \"supports\", \"note\": \"'1128. yek „ein“ … ap. *aivaka-, vergl. aiva- „ein“; aw. aēva-; phlv. ēvak, ēv, phlv.-pāz. yak, ai. eka-'; '1114. hēč „jemand, jemals“, mit Negation „niemand, nichts“ … ap. *aiva + čiy; phlv. ēč bezw. hēč (pāz. hēč, hēčī)'.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (chapter on -ak > -a, and on č)\", \"stance\": \"supports\", \"note\": \"'yak “ein” = phl. ēvak, ap. aiva-'; 'hēč, ēč „irgend ein“, erst im Mp. aus ē = *ēv = ap. aiva- “ein” und č = či = ap. čiy zusammengesetzt'.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt / ARY_latin_index_pages.txt\", \"stance\": \"silent\", \"note\": \"grepped 'aivaka', 'oino', 'evak', 'یک', 'هیچ' — no usable hit (the Persian OCR of Aryanpur is too poor to give an etymological line for these headwords).\"},\n   {\"src\": \"MON\", \"where\": \"vajehyab.com/moein/این and abadis.ir (فرهنگ فارسی معین section)\", \"stance\": \"partial\", \"note\": \"The online Mo'in gives the entries but, as the project's refs_online note says, strips the Latin-script Pahlavi/Avestan etyma of the print edition, so it can only confirm sense, not the etymology.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Avestan / Old Persian\",\n \"words\": \"uta, utâ, uiti : and\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Av. uta and OP utā 'and, and also' are exactly right and stand on the page Nourai cites: Pokorny 74 (inside the 73-75 article) 'Partikel ai. u-tá, in beiden Gliedern „einerseits — andrerseits“ … av. uta, ap. utā „und, und auch“'; Kent's lexicon lists utā among the OP particles, and Wiktionary derives Persian و from 'Old Persian 𐏢𐏫𐏠 (u-t-a /utā/, “and”), from Proto-Indo-Iranian *(H)utá, *(H)u, from Proto-Indo-European *h₂u'. The third form is glossed wrongly: Avestan uiti (Gathic ūiti) does NOT mean 'and'; it means 'so, thus', and is the standard adverb accompanying aoj- 'to say' ('uiti aojanō' = 'thus speaking', Yt.10.53, Yt.19.49). Pokorny prints it on the same page precisely with that gloss: 'Hierher av. uiti, gthav. ūiti „so“; nicht aber lat. ut und utī'. So the box's membership is right (uiti belongs to the u-/uta family) but its gloss 'and' is not.\",\n \"derivation_fa\": \"دو صورت نخست درست‌اند: اوستایی uta و پارسی باستان utā هر دو «و، و نیز» معنا می‌دهند و دقیقاً در همان صفحهٔ ۷۴ پوکورنی آمده‌اند؛ ویکی‌واژه نیز «و» فارسی را از utāی پارسی باستان و آن را از هندوایرانی *(H)utá و هندواروپایی *h₂u می‌داند. اما معنای uiti درست نوشته نشده: uiti (گاهانی ūiti) قید است به معنای «چنین، این‌گونه» که معمولاً با فعل aoj- «گفتن» می‌آید (uiti aojanō «چنین گویان»)، و پوکورنی هم همان‌جا آن را «so» معنا کرده است. پس عضویت uiti در این خانواده درست است ولی معنای «و» برای آن خطاست.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D9%88\"],\n \"ref_check\": [\n   {\"ref\": \"POK:74\", \"status\": \"supports\", \"note\": \"POK_01.txt, printed p.74 (inside the article 'au-, u-', pp.73-75): 'Partikel ai. u-tá … av. uta, ap. utā „und, und auch“' and, five lines further, 'Hierher av. uiti, gthav. ūiti „so“; nicht aber lat. ut und utī, alat. utei' — supports the forms, contradicts the gloss 'and' for uiti.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch s.v. uta and the uiti passages (col. ~384 for utā, cols. 405-6 for uiti aojanō)\", \"stance\": \"partial\", \"note\": \"The uiti citations in BRT.txt are all of the type 'uiti aojanō Yt.10.53', 'uity aojanā Yt.13.66', 'ātarš … uiti vacəbiš aojanō Yt.19.49' — i.e. 'thus/so speaking', never 'and'. Mo'in (BQT 2242) cites 'Bartholomae 384' for OP utā.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon (particles) and §§ on utā\", \"stance\": \"supports\", \"note\": \"utā 'and' is one of the commonest OP particles in Kent's texts and lexicon (e.g. DNa 'utā … utā'); the lexicon index leaf lists 'ucāram; utā, uta-'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Sogdian\",\n \"words\": \"`ty : and\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sogdian ʾty(y) / ʾt 'and' (Manichaean script), beside the far commoner ʾrty, is the regular Sogdian outcome of Old Iranian *uta: initial *u- is reduced to the prop-vowel written ʾ-, and the -t- stays intervocalically because Sogdian, unlike Middle Persian, does not voice it in this monosyllabic clitic. Gharib, Sogdian Dictionary, entry 301 (printed p.12) gives it exactly so: '301 ʾty(y) M — at ⇒ ʾrty¹, ʾt¹ — and — GMS 76', the reference being to Gershevitch's Grammar of Manichean Sogdian §76, where the particle is treated. The word is used as a sentence-connective in the Manichaean Sogdian texts.\",\n \"derivation_fa\": \"صورت سغدی ʾty(y)/ʾt «و» (در متون مانوی) در کنار گونهٔ پربسامدتر ʾrty، دنبالهٔ قانونمند *utaی ایرانی باستان است: واکهٔ آغازین u- فروکاسته و به صورت الف تکیه‌گاه نوشته شده و -t- میانی برخلاف فارسی میانه واک‌دار نشده است. قریب در فرهنگ سغدی، مدخل ۳۰۱ (صفحهٔ ۱۲)، همین را آورده است. ادعای نورایی درست است؛ تنها شمارهٔ صفحهٔ ارجاع (۷۲) نادرست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:72\", \"status\": \"not_found\", \"note\": \"SOD_pages.txt leaf 137 = printed p.72 (the printed numeral '72' is legible at the head of the leaf) holds entries ~1814-1829 (ʾtδrty 'third', ʾtrwh 'fire'); there is nothing about 'and'. The word IS in Gharib, but as entry 301 on printed p.12 (leaf 77): '301 ʾty(y) M — at ⇒ ʾrty¹, ʾt¹ — and — GMS 76'. Nourai's page number is wrong (his other two SOD numbers on this page, 85 and 220, are correct page numbers).\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian-Persian-English Dictionary, entry 301 (printed p.12)\", \"stance\": \"supports\", \"note\": \"'301 ʾty(y) M / at ⇒ ʾrty¹, ʾt¹ / and / GMS 76' — the word, the language and the gloss are exactly Nourai's.\"},\n   {\"src\": \"HENNING\", \"where\": \"HENNING_selected_papers.txt / GMS reference in Gharib\", \"stance\": \"silent\", \"note\": \"Gharib's own authority for the entry is Gershevitch, Grammar of Manichean Sogdian §76; no separate discussion found in the local Henning file.\"}\n ]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Pahlavi\",\n \"words\": \"ud : and\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian ud 'and', written with the Aramaic heterogram <W> in Book Pahlavi and phonetically <ʾywd> in Manichaean, continues Old Persian utā: the final -ā of the unstressed particle is lost and intervocalic/final -t- is voiced to -d- by the regular Middle Persian lenition. MacKenzie, CPD: 'ud [W < A w | M ʾywd, N u] and.' Mo'in's note s.v. و (BQT 2242) gives the same: 'در پهلوی ut، پارسی باستان utā «بارتولمه ۳۸۴» … اوستایی uta'. In Manichaean Middle Persian and Parthian the enclitic form -ud/-u is already the norm, which is why New Persian has the vowel alone.\",\n \"derivation_fa\": \"فارسی میانهٔ ud «و» که در پهلوی کتابی با هزوارش آرامی <W> و در مانوی به صورت <ʾywd> نوشته می‌شود، دنبالهٔ utāی پارسی باستان است: الف پایانی در واژهٔ بی‌تکیه افتاده و t در جایگاه میانی/پایانی برپایهٔ قاعدهٔ نرم‌شدگی فارسی میانه به d بدل شده است. مکنزی: «ud [W < A w | M ʾywd, N u] and»؛ معین در حاشیهٔ برهان قاطع (ص ۲۲۴۲) نیز «در پهلوی ut، پارسی باستان utā» می‌نویسد. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D9%88\"],\n \"ref_check\": [\n   {\"ref\": \"SNS:256\", \"status\": \"partial\", \"note\": \"The back index of Tavoosi's glossary (SNS_pages.txt leaf 223) has the line 'ud 256/1' — the word is certainly in the book and the number 256 is the one Nourai cites, but in the glossary that numeral is a page/line reference into the Pahlavi text, so I cannot confirm that Tavoosi's printed p.256 carries the entry; the etymology itself is confirmed elsewhere.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.v. ud\", \"stance\": \"supports\", \"note\": \"'ud [W < A w | M ʾywd, N u] and.' — Book Pahlavi heterogram W, Manichaean ʾywd, New Persian u.\"},\n   {\"src\": \"BQT\", \"where\": \"vol.4 p.2242, Mo'in's note s.v. و\", \"stance\": \"supports\", \"note\": \"'در پهلوی ut، پارسی باستان utā «بارتولمه ۳۸۴»، در اوراق تورفان (لهجهٔ شمال غربی) ut … اوستایی uta' (read from the page image; ocr/BQT/2242.vision.txt).\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II\", \"stance\": \"silent\", \"note\": \"grepped '^ut ', '^ud ' in NYB_vol2_glossary.txt — the particle is written with the heterogram and is not entered under a Latin headword in the OCR of the glossary.\"}\n ]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Persian\",\n \"words\": \"o, va «وُ ، وَ» : and\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian و, pronounced -o (enclitic, the normal reading) or va, is the direct continuation of Middle Persian ud/u < OP utā < PIE *h₂u-ta. Horn, Grundriss no.1071, is the classic statement and covers Nourai's whole box including his NOTE: '1071. u, ū „und“. ap. utā „auch, und“; aw. uta; phlv. u (pāz. u). Bei diesem vielgebrauchten Worte ist die nicht lautgesetzliche starke Verkürzung durchaus erklärlich. Die Aussprache ve … ist Nachahmung des arab. va „und“ oder dieses ist selbst entlehnt worden.' Mo'in says the same at BQT 2242: 'تلفظ درست این حرف در فارسی کنونی o است … اما اینکه این حرف را بسیاری معمولاً va تلفظ کنند تقلید از حرف عطف عربی است' — which is word for word the chart's NOTE, so the note is correct and is Mo'in's, and modern scholarship (Horn, Hübschmann, Wiktionary) takes the same side: the inherited Persian form is o/u, and va is a reading-pronunciation on the model of Arabic wa-. Nourai's Ferdowsi verse ('man o asb o Šabdiz o šamšir-e tiz') illustrates the enclitic -o. One dissenting older view exists: Bartholomae (footnote to his vā article) proposed tracing 'die np. Part. u (va) “und” auf air. vā zurück', i.e. to the 'or' particle of node 2 rather than to uta; that view has not been taken up, and MacKenzie, Mo'in, Horn, Hübschmann and Wiktionary all keep ud < utā.\",\n \"derivation_fa\": \"«و» فارسی که درست‌تر -o خوانده می‌شود، دنبالهٔ مستقیم ud/u فارسی میانه و آن از utāی پارسی باستان و utaی اوستایی است. هرن در شمارهٔ ۱۰۷۱ همین را می‌آورد و می‌افزاید که کوتاه‌شدگی شدید این واژهٔ پرکاربرد طبیعی است و اینکه تلفظ va «تقلید از وَ عربی» است؛ معین نیز در حاشیهٔ برهان قاطع (ص ۲۲۴۲) عیناً می‌نویسد «اما اینکه این حرف را بسیاری معمولاً va تلفظ کنند تقلید از حرف عطف عربی است». پس یادداشت نورایی دربارهٔ تأثیر عربی درست و مستند است. تنها نظر مخالف از بارتولمه است که در پاورقی مدخل vā پیشنهاد کرده بود «و» فارسی را به vāی ایرانی باستان (یعنی «یا») برگردانند؛ این رأی پذیرفته نشده است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D9%88\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:2242\", \"status\": \"supports\", \"note\": \"Read from the page image (ocr/BQT/2242.vision.txt): 'و(عطف) – تلفظ درست این حرف در فارسی کنونی o است. در پهلوی ut، پارسی باستان utā «بارتولمه ۳۸۴» … اوستایی uta … اما اینکه این حرف را بسیاری معمولاً va تلفظ کنند تقلید از حرف عطف عربی است.' This single page supports the whole node, including the chart's NOTE.\"},\n   {\"ref\": \"SNS:256\", \"status\": \"partial\", \"note\": \"'ud 256/1' in Tavoosi's index (leaf 223); see node 7.\"},\n   {\"ref\": \"TZF:20\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi — not on archive.org and only behind a ketabnak login (refs_online.json 'local_file': null).\"},\n   {\"ref\": \"MON:4921\", \"status\": \"not_checked\", \"note\": \"The six-volume Mo'in is not online in any form (only the two-volume Adena condensation, with different pagination); page 4921 cannot be reached.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 1071\", \"stance\": \"supports\", \"note\": \"'1071. u, ū „und“. ap. utā „auch, und“; aw. uta; phlv. u (pāz. u). … Die Aussprache ve … ist Nachahmung des arab. va „und“ oder dieses ist selbst entlehnt worden. Oder gehört np. ū „und“ zu gr. aὖ, got. auk etc.' — supports both the chain and the chart's NOTE (and Horn's alternative even names the Greek/Gothic members of Pokorny's au- article).\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien §21\", \"stance\": \"supports\", \"note\": \"'Ap. u (= idg. u) bleibt im Np. als u, vgl. u (ū) „und“ = ap. utā.'\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.v. ud\", \"stance\": \"supports\", \"note\": \"'ud [W < A w | M ʾywd, N u] and' — explicitly gives New Persian u as the outcome.\"},\n   {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, s.v. vā (col. 1310) with footnote\", \"stance\": \"contradicts\", \"note\": \"'So ergibt sich die Berechtigung, die np. Part. u (va) “und” auf air. vā zurückzuführen' — Bartholomae would derive the Persian particle from vā 'or' (node 2), not from uta (node 5). A minority position; recorded for completeness.\"}\n ]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Old Persian / Sanskrit\",\n \"words\": \"aina, ěna, aita, aěta : this one, this ; ima, imam : this\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The forms are all genuine, but they do not all hang where the chart hangs them. ēna- (Nourai's 'aina, ěna') is Sanskrit ena- 'he, this', which Pokorny prints under *oi-nos on p.286 ('oi-nos: ai. e-na- „er“ (kann auch *ei-no- sein)') — so for this word the arrow from node 1 is exactly Pokorny's. But aita- / aēta- 'this' and ima- / imam 'this' are formed straight from the root box's stem, not from *oi-no-: Pokorny p.286 lists them under 'D. Zusammensetzungen und Ableitungen' — 'ai. e-ṣá, e-ṣā, e-tát, av. aeša-, aeta- „der da“ (*ei-so, -to-)' — i.e. *ei- + the -to- particle; and 'ai. imám … = apers. imam' from the bare stem *i- with the accusative *im. A second inaccuracy is the language label: aita- is Old Persian (Kent's lexicon p.164 'aita- … asn. DPd 20; DNa 53; XPh 43'), aēta- is Avestan, ena- is Sanskrit, and ima/imam is both Old Persian (imam DNa 1, DSe 2, and OP iyam) and Sanskrit (imám); 'Old Persian / Sanskrit' therefore silently covers an Avestan form too. Mo'in's footnote at the page Nourai cites (BQT 199, the اینت/این entries, with the catch-line 'بقیه از صفحهٔ ۱۹۸') reads 'در پارسی باستان …، در پهلوی …' — the same OP imam / Pahlavi ēn pair that the chart draws.\",\n \"derivation_fa\": \"همهٔ صورت‌ها اصیل‌اند، ولی همه از گرهٔ پدر (یعنی *oi-no-) نیامده‌اند. سنسکریت ena- «او، این» را پوکورنی (ص ۲۸۶) راستی زیر *oi-nos آورده است؛ اما aita-/aēta- و ima-/imam مستقیماً از خود ستاک ریشه ساخته شده‌اند: پوکورنی در بخش «ترکیب‌ها و مشتقات» می‌نویسد «سنسکریت e-ṣá، e-tát، اوستایی aeša-، aeta- „این“ (*ei-so، -to-)» و «sanskrit imám = پارسی باستان imam». نکتهٔ دوم برچسب زبان است: aita- پارسی باستان است (کنت ص ۱۶۴)، aēta- اوستایی است و در عنوان جعبه نیامده است. با این دو اصلاح، ادعای نورایی پذیرفتنی است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"POK:75\", \"status\": \"partial\", \"note\": \"p.75 has the vā/aiva material, not the demonstratives; the demonstrative forms of this node are on p.286.\"},\n   {\"ref\": \"POK:286\", \"status\": \"supports\", \"note\": \"POK_01.txt p.286: 'ai. e-ṣá, e-ṣā, e-tát, av. aeša-, aeta- „der da“ (*ei-so, -to-)'; and 'oi-nos: ai. e-na- „er“'. Also p.285/286 'ai. imám (erweitert aus *im) = apers. imam (darnach f. imām usw.)'.\"},\n   {\"ref\": \"BQT:199\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 419 (the leaf ends with the catch-line 'بقیه از صفحهٔ ۱۹۸', so it is printed p.199): the اینه/اینت/اینک entries with Mo'in's footnote 4 'در پارسی باستان [imam], در پهلوی [ēn]' (the Latin forms are garbled by the OCR but the Persian frame is legible) — exactly the OP imam → Pahlavi ēn step drawn here and in node 11.\"},\n   {\"ref\": \"TZF:13\", \"status\": \"not_checked\", \"note\": \"Abolghasemi's Tarikh-e Mokhtasar is not available (no scan, login-only PDF).\"},\n   {\"ref\": \"SOD:85\", \"status\": \"supports\", \"note\": \"SOD_pages.txt leaf 150 (printed '85' at the head): entry '2154 ʾyδ B, M, S / eδ ©<Av. aeta; OP aita / this 269, 1403, 1500; VJ 364' — Gharib himself derives the Sogdian word from Av. aeta / OP aita, the very forms in this box.\"},\n   {\"ref\": \"SOD:220\", \"status\": \"supports\", \"note\": \"SOD_pages.txt leaf 286 (printed '220'): the mw entry 'this … ©OP imam ⇒ ʾmw, mwnʾw, ʾmy²; acc. -δw, C2, IV, 17, 29' — Gharib derives Sogdian mw from OP imam.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon p.164 (aita-) and p.~176 (ima-)\", \"stance\": \"supports\", \"note\": \"Leaf 186 of KNT.txt, the p.164 block: '… asn. DPd 20; DNa 53; XPh 43, 59; XSc 4. aitā apf. XPh 30, 35' — the tail of the OP aita- 'this' entry; ima-/imam is likewise a standard OP demonstrative in Kent (DNa 1 'imām būmim').\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 137\", \"stance\": \"supports\", \"note\": \"'137. ē „dieser“ in īdar „hier“ … ap. aita- „dieser“; aw. ae-m-, ae-taδ; phlv. ē, ēčand … pāz. ēδ, ēšān; ai. e-ṣa-, e-tad.'\"},\n   {\"src\": \"SOD\", \"where\": \"Gharib entries 2154 and 5512\", \"stance\": \"supports\", \"note\": \"as quoted in ref_check above.\"}\n ]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Sogdian\",\n \"words\": \"`yd : this ; mw : this\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both Sogdian demonstratives are drawn from precisely the etyma Gharib gives. ʾyδ (read eδ) 'this' is the Sogdian continuation of Old Iranian *aita- (Av. aeta-, OP aita-): intervocalic/final *-t- has become the voiced spirant -δ- by the regular Sogdian lenition, and the diphthong ai- is monophthongised to e-. Gharib, entry 2154: 'ʾyδ B, M, S / eδ ©<Av. aeta; OP aita / this'. mw (read mu) 'this' is the oblique of the *ima- demonstrative, with the initial i- lost in the unstressed proclitic and the case forms built on m-: Gharib, printed p.220, 'this (mw) ©OP imam ⇒ ʾmw, mwnʾw, ʾmy²; acc. -δw … loc. -ty', i.e. beside mw there survive the fuller ʾmw and ʾmy which show the lost vowel. Both words are used as the ordinary near-deictics of Buddhist, Manichaean and Christian Sogdian.\",\n \"derivation_fa\": \"هر دو ضمیر اشارهٔ سغدی دقیقاً از همان سرچشمه‌ای‌اند که قریب می‌گوید. ʾyδ (eδ) «این» دنبالهٔ *aita- ایرانی باستان است: دوواکهٔ ai به e ساده شده و t میانی برپایهٔ قاعدهٔ نرم‌شدگی سغدی به سایشی واک‌دار δ بدل شده است؛ قریب در مدخل ۲۱۵۴ می‌نویسد «از اوستایی aeta؛ پارسی باستان aita». mw (mu) «این» صورت غیرفاعلی ضمیر *ima- است که الف/یای آغازین در جایگاه پیش‌بست افتاده است؛ قریب در صفحهٔ ۲۲۰ صریحاً آن را به imam پارسی باستان بازمی‌گرداند و گونه‌های پرتر ʾmw و ʾmy را هم می‌آورد. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:85\", \"status\": \"supports\", \"note\": \"Gharib entry 2154 on printed p.85: 'ʾyδ B, M, S / eδ ©<Av. aeta; OP aita / this 269, 1403, 1500; VJ 364; TSP 3.120 etc.'\"},\n   {\"ref\": \"SOD:220\", \"status\": \"supports\", \"note\": \"Gharib, printed p.220: 'this (mw) ©OP imam ⇒ ʾmw, mwnʾw, ʾmy² … acc. -δw, C2, IV, 17, 29; loc. -ty, C2, 1R25'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary pp. 85 and 220\", \"stance\": \"supports\", \"note\": \"the two entries quoted above; both carry Gharib's own ©-etymology, which is Nourai's arrow.\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Dictionary of Khotan Saka (local file)\", \"stance\": \"silent\", \"note\": \"grepped for the Sogdian forms; nothing bearing on these two Sogdian demonstratives.\"}\n ]\n})\n\nnodes.append({\n \"id\": 11, \"lang\": \"Pahlavi\",\n \"words\": \"ěn : this ; im : this\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian has two inherited near-deictics side by side, exactly as the chart shows. ēn 'this' (Book Pahlavi with the Aramaic heterogram <ZNE>, phonetically Manichaean <ʾyn>) continues *aina-/*ai-na-, the *ei-no- form of the pronominal stem; MacKenzie: 'ēn [ZNE < A znh | M ʾyn, N in] this.' im 'this (here, near the speaker)' continues OP imam/ima-; MacKenzie: 'im [LZNE < A l-znh; ʾm | M cym, N -] this', and Nyberg II s.v. 'im [LZNH] dem. pron. this here, near to the speaker: im rōc to-day … im spah ērān this army of ērān … im bag Xōsrōi šāhān šāh the present King of Kings'. Both readings are standard and both parents in node 9 are the right ones (ēna-/aina- → ēn, ima- → im).\",\n \"derivation_fa\": \"فارسی میانه دو ضمیر اشارهٔ نزدیک دارد که هر دو در این جعبه آمده‌اند. ēn «این» (در پهلوی کتابی با هزوارش <ZNE> و در مانوی <ʾyn>) دنبالهٔ صورت *ai-na-ی ستاک ضمیری است؛ مکنزی: «ēn [ZNE < A znh | M ʾyn, N in] this». im «این، اینی که نزد گوینده است» ادامهٔ imam/ima- پارسی باستان است؛ نیبرگ نمونه‌های «im rōc» (= امروز)، «im spah ērān» و «im bag Xōsrōi» را می‌آورد. هر دو خوانش معیارند و ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"MON:345\", \"status\": \"not_checked\", \"note\": \"The six-volume Mo'in (Amir Kabir 1363) is not online in any edition — archive.org has only the two-volume Adena condensation with different pagination — so p.345 cannot be verified. The online Mo'in (vajehyab/abadis, archived) gives the این entry but without the print edition's Latin-script Pahlavi etymon.\"},\n   {\"ref\": \"MON:421\", \"status\": \"not_checked\", \"note\": \"Same reason.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.vv. ēn and im\", \"stance\": \"supports\", \"note\": \"'ēn [ZNE < A znh | M ʾyn, N in] this'; 'im [LZNE < A l-znh; ʾm | M cym, N -] this' with 'im rōz' in the running heads.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.v. im\", \"stance\": \"supports\", \"note\": \"'im [LZNH] dem. pron. this here, near to the speaker: im rōc to-day 51 … im bag Xōsrōi šāhān šāh the present King of Kings, Divine Khosroes 109.'\"},\n   {\"src\": \"BQT\", \"where\": \"vol.1 p.199 (leaf 419), Mo'in's footnote to این\", \"stance\": \"supports\", \"note\": \"'در پارسی باستان …، در پهلوی …' — the OP/Pahlavi pair; Latin forms garbled in the OCR but the structure of the note is unmistakable.\"}\n ]\n})\n\nnodes.append({\n \"id\": 12, \"lang\": \"Persian\",\n \"words\": \"în «این» : this ; em «اِم (امروز، امشب، امسال)» : this\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"این īn 'this' is the regular New Persian form of MP ēn: the Middle Persian long ē is raised to ī in New Persian (the same change as in šēr > šīr, dēn > dīn), so ēn > īn; Wiktionary, s.v. این: 'Inherited from Middle Persian 𐮦𐮭𐮤 (ēn). Compare Mazanderani ام (am), Central Kurdish ئەم (em), Northern Kurdish ev … Possibly related to Sanskrit एन (ena).' The second item is the fossilised proclitic em-/am- that survives only in the time-words امروز emrūz 'today', امشب emšab 'tonight', امسال emsāl 'this year'; it is Middle Persian im (node 11) petrified in exactly these collocations — Nyberg's glossary cites the Pahlavi original 'im rōc to-day' and MacKenzie prints 'im rōz' — so Nourai's parenthesis is precisely right, and ام- is a doublet of این within Persian rather than an independent word.\",\n \"derivation_fa\": \"«این» صورت قانونمند فارسی نو از ēn فارسی میانه است: ای کشیدهٔ فارسی میانه در فارسی نو به ی بدل شده است (همان دگرگونی که در شیر < šēr و دین < dēn دیده می‌شود). ویکی‌واژه نیز آن را وام‌ماندهٔ ēn می‌داند و همریشه‌های مازندرانی «ام» و کردی «ئەم/ev» را یاد می‌کند. جزء «اِم‌» در امروز، امشب و امسال بازماندهٔ همان im پهلوی است که تنها در همین ترکیب‌های زمانی فسیل شده است؛ نیبرگ و مکنزی هر دو صورت پهلویٔ «im rōc/im rōz» (= امروز) را می‌آورند. پس «ام-» دوگانهٔ درون‌زبانی «این» است. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D9%86\", \"https://vajehyab.com/moein/%D8%A7%DB%8C%D9%86\", \"https://abadis.ir/fatofa/%D8%A7%DB%8C%D9%86/\"],\n \"ref_check\": [\n   {\"ref\": \"MON\", \"status\": \"not_checked\", \"note\": \"Cited without a page; the six-volume Mo'in is not online. The online Mo'in text (vajehyab.com/moein/این and abadis.ir, both archived) gives 'این. (ضمیر، ص) ضمیر اشاره برای نزدیک. مقابل آن. ج، اینها، اینان (فرهنگ فارسی معین)' but no etymon.\"},\n   {\"ref\": \"TZF:13\", \"status\": \"not_checked\", \"note\": \"Abolghasemi's Tarikh-e Mokhtasar-e Zaban-e Farsi is not obtainable.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.v. im (with 'im rōz' in the head-line)\", \"stance\": \"supports\", \"note\": \"'im [LZNE < A l-znh; ʾm | M cym, N -] this' and the running head 'im roz' — the Pahlavi source of امروز.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. im\", \"stance\": \"supports\", \"note\": \"'im rōc to-day 51' — the very phrase behind Persian امروز.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 137\", \"stance\": \"partial\", \"note\": \"Horn treats the ē/ī deictic and its compounds (īdar, īdūn, īm 'jetzt') under ap. aita-; he does not give a separate این entry, but his 'phlv. ē' is the same word.\"},\n   {\"src\": \"MON\", \"where\": \"vajehyab.com/moein/این (archived)\", \"stance\": \"partial\", \"note\": \"Confirms Mo'in has the entry and the sense; the online text omits the Latin-script etyma of the six-volume print edition.\"}\n ]\n})\n\nnodes.append({\n \"id\": 13, \"lang\": \"Germanic\",\n \"words\": \"ainaz, ainigaz : one\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Proto-Germanic *ainaz 'one' is the regular outcome of PIE *oi-nos: *oi- > Gmc. *ai-, and the o-stem ending *-os > *-az by Grimm's law and Verner-neutral final position. Watkins/AHD s.v. oi-no-: 'I. Basic form *oi-no-. 1. Germanic *ainaz in: a. Old English ān, one: A¹, AN¹, ONCE, ONE; (ALONE), ANON, (ATONE), (LONE), (LONELY), NONE; b. compound *ain-lif-, “one left (beyond ten),” eleven …' The second form, *ainigaz, is Watkins's 'II. Suffixed form *oino-ko- in: a. Germanic *ainigaz in Old English ǣnig, one, anyone: ANY' — i.e. *oi-no- extended by the adjectival *-ko-/-ga-, the same suffix Pokorny cites for Latin ūnicus and Gothic ainaha (p.286). Cognates: Goth. ains, ON einn, OHG ein, all cited by Pokorny p.286 and Klein s.v. one.\",\n \"derivation_fa\": \"ژرمنی آغازین *ainaz «یک» دنبالهٔ قانونمند *oi-nos هندواروپایی است (*oi- > ai- ژرمنی، پایانهٔ *-os > *-az). واتکینز در پیوست AHD می‌نویسد «Germanic *ainaz in Old English ān» و برای گونهٔ دوم «Suffixed form *oino-ko- … Germanic *ainigaz in Old English ǣnig “any”»؛ یعنی *ainigaz همان *oi-no- است با پسوند صفتی *-ko-/-ga-، همان پسوندی که در ūnicus لاتین و ainaha گوتی دیده می‌شود (پوکورنی ص ۲۸۶). ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/one\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. oi-no-: 'I. Basic form *oi-no-. 1. Germanic *ainaz in: a. Old English ān, one … II. Suffixed form *oino-ko- in: a. Germanic *ainigaz in Old English ǣnig, one, anyone: ANY … [In Pok. e- 281.]' — both of Nourai's Germanic forms verbatim.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p.286\", \"stance\": \"supports\", \"note\": \"'got. ains, ahd. ein, anord. einn … aksl. inŭ „unus“ … inokŭ „solus“ (= got. ainaha „einzig“, lat. ūnicus, anord. einga, ags. ānga, ahd. einac, as. ēnag, nhd. einig)'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.v. one\", \"stance\": \"supports\", \"note\": \"'ME. oon, on, an, fr. OE. ān, “one”, rel. to OS. ēn, ON. einn … Goth. ains, “one”, fr. I.-E. *oi-nos'.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I (leaf 109 of WLD_Bd1_pages.txt)\", \"stance\": \"supports\", \"note\": \"'got. áins, ahd. ein, anord. einn (hierher gehört altn. einka „besonders“ …)'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 14, \"lang\": \"English\",\n \"words\": \"one, an, none, eleven, alone, any\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All six English words go back to Old English ān < PGmc *ainaz, and Watkins lists exactly this set under oi-no-. one < ME oon/on < OE ān; an (and a) is the same word reduced in proclisis to the indefinite article; none < OE nān = ne 'not' + ān 'one'; alone < ME al one 'all one, quite by oneself'; eleven < OE endleofan < PGmc *ain-lif- 'one left (over ten)', the second element being *lif- 'to leave' (Klein s.v. eleven: 'formed fr. Teut. *ain-, “one”, and I.-E. base *liqʷ-, “to be left over”'); any < OE ǣnig < PGmc *ainigaz, the -ig suffix form. Klein gathers the same list at 'one': 'Cp. once, only, any, … the second element in Angus, … alone, anon, atone, nonce, none, eleven.'\",\n \"derivation_fa\": \"هر شش واژه به انگلیسی کهن ān < ژرمنی *ainaz بازمی‌گردند و واتکینز همین فهرست را زیر oi-no- می‌آورد. an همان one است که در جایگاه پیش‌بست فروکاسته و به حرف تعریف نامعین بدل شده است؛ none از nān = ne + ān؛ alone از al one؛ eleven از endleofan < *ain-lif- «یک باقی‌مانده (از ده)» (کلاین)؛ any از ǣnig < *ainigaz. تحول معنایی همه روشن است و ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/one\"],\n \"ref_check\": [\n   {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None); checked Watkins/AHD, Klein and Etymonline instead — see 'consulted'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. oi-no-\", \"stance\": \"supports\", \"note\": \"'Old English ān, one: A¹, AN¹, ONCE, ONE; (ALONE), ANON, (ATONE), (LONE), (LONELY), NONE; b. compound *ain-lif- … in Old English endleofan, eleven: ELEVEN … Germanic *ainigaz in Old English ǣnig, one, anyone: ANY.'\"},\n   {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.vv. one, eleven\", \"stance\": \"supports\", \"note\": \"s.v. one: 'The indef. article an is derivatively identical with one. Cp. once, only, any, … alone, anon, atone, nonce, none, eleven'; s.v. eleven: 'fr. OE. endleofan … Goth. ainlif. These words are formed fr. Teut. *ain-, “one”, and I.-E. base *liqʷ-, “to be left over”.'\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls (local FSD volumes)\", \"stance\": \"silent\", \"note\": \"not consulted in detail: the chain OE ān > ME on > NE one is uncontroversial and is fully covered by AHD, Klein and Etymonline.\"}\n ]\n})\n\nnodes.append({\n \"id\": 15, \"lang\": \"Latin\",\n \"words\": \"ŭnus : one ; ne-ŭllus : not any, null\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin ūnus 'one' is the direct outcome of *oi-nos: Old Latin still has oinos (Pokorny p.286 'lat. ūnus, alt oinos'; Buck 13.32 'OLat. oinos, oenus, Lat. ūnus'), the diphthong oi passing regularly to ū in Latin of the 2nd c. BCE (cf. oinos > ūnus like poinos > poena kept only in learned words, or *oinikos > ūnicus). Nourai's second entry, 'ne-ŭllus', is the standard analysis of nullus: Watkins puts 'III. Suffixed form *oino-lo- in Latin ūllus, any (see ne)' under oi-no-, ūllus being the diminutive *oino-los > *ūnulus > ūllus, and nūllus = ne + ūllus 'not any'. Watkins also files under this root Latin nōn 'not' (< *ne-oinom 'not one thing'). One typographical point: the book prints the vowels with a BREVE, 'ŭnus' and 'ne-ŭllus', but the Latin quantities are long — ūnus, ūllus, nūllus (necessarily so, since ū here comes from the diphthong oi). The breve is a slip of the book, not an extraction error (verified on the page image, book p.195).\",\n \"derivation_fa\": \"لاتین ūnus «یک» پیامد مستقیم *oi-nos است؛ در لاتین کهن هنوز oinos بوده (پوکورنی ص ۲۸۶: «lat. ūnus, alt oinos»؛ باک ۱۳.۳۲) و دوواکهٔ oi به قاعده به ū کشیده بدل شده است. «ne-ŭllus» همان تجزیهٔ پذیرفتهٔ nūllus است: واتکینز می‌نویسد «Suffixed form *oino-lo- in Latin ūllus “any”» (یعنی مصغر *ūnulus > ūllus) و nūllus = ne + ūllus «هیچ». یک نکتهٔ حروف‌چینی: کتاب علامت کوتاهی (ŭ) گذاشته، در حالی که هر دو واکه کشیده‌اند (ūnus، ūllus)؛ این خطای چاپی خود کتاب است نه خطای خوانش اسکن (روی تصویر صفحه دیدم). در کل ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/one\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. oi-no-: '2. Latin ūnus, one: INCH¹, OUNCE¹, UNCIAL, UNI-, UNION, UNITE, UNITY; COADUNATE, QUINCUNX, TRIUNE, UNANIMOUS, UNICORN, UNIVERSE. 3. Latin nōn, not (< *ne-oinom, “not one thing”; ne, not; see ne). … III. Suffixed form *oino-lo- in Latin ūllus, any (see ne).'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p.286\", \"stance\": \"supports\", \"note\": \"'lat. ūnus, alt oinos' and, for the -ko- form, 'lat. ūnicus'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 13.32, p.937\", \"stance\": \"supports\", \"note\": \"'OLat. oinos, oenus, Lat. ūnus (> It., Sp. uno, Fr., Rum. un)'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. oinos\", \"stance\": \"supports\", \"note\": \"'Lat. ūnus, a, um; Oscan úin … Verbal derivative: Lat. unio, ire'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 16, \"lang\": \"English\",\n \"words\": \"union, onion, ounce, inch, unique, unite, unit, universe ; null\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Eight of the nine are exactly Watkins's list for Latin ūnus: union (L. ūniō, -ōnis 'oneness' via OF union), unite/unit/unity (L. ūnīre, ūnitas), unique (L. ūnicus, via F. unique, 17th c.), universe (L. ūniversus 'turned into one, whole' = ūnus + versus), inch (OE ynce < L. uncia 'one twelfth part' — a derivative of ūnus meaning 'a unit'), ounce (the same uncia borrowed a second time through OF unce, so inch and ounce are doublets), and null (F. nul / L. nūllus = ne + ūllus < *oino-lo-, i.e. the ne-ūllus of node 15). Watkins's entry names INCH¹, OUNCE¹, UNCIAL, UNI-, UNION, UNITE, UNITY, UNIVERSE and, under *oino-ko-, UNIQUE. The one uncertain member is onion: its immediate source is beyond doubt Latin ūniōnem (acc. of ūniō 'a single large pearl; onion') through OF oignon, but whether that ūniō is itself a derivative of ūnus is doubted — Klein: 'However, the diphthong oi in F. oignon shows that the u in L. ūniō, “onion”, is short and that, accordingly, ūniō in this sense is not a derivative of ūnus, unless it is assumed that the u was shortened in Vulgar Latin; see Walde-Hofmann, LEW., II, 820'. Watkins's oi-no- list indeed does NOT include ONION. So the box is right except that one word, for which the traditional (Etymonline, most handbooks) derivation from ūnus is probable but contested.\",\n \"derivation_fa\": \"هشت واژه از نه واژه عیناً همان‌هایی اند که واتکینز زیر ūnus لاتین می‌آورد: union (از ūniō)، unite/unit/unity (از ūnīre و ūnitas)، unique (از ūnicus)، universe (از ūniversus «به یک سو گردانده، کل»)، inch و ounce که هر دو از uncia «یک‌دوازدهم»‌اند (پس دوگانهٔ یکدیگرند)، و null از nūllus = ne + ūllus. تنها مورد مشکوک onion است: منبع بی‌واسطهٔ آن قطعاً ūniōnem لاتین (از راه oignon فرانسهٔ کهن) است، ولی کلاین به تبع والده–هوفمان یادآور می‌شود که دوواکهٔ oi در فرانسه نشان می‌دهد u در این واژه کوتاه بوده و پس شاید از ūnus نیامده باشد؛ واتکینز هم onion را در فهرست oi-no- نیاورده است. پس این گره جز در مورد onion درست است و آن یک مورد را باید با احتیاط پذیرفت.\",\n \"sources\": [\"https://www.etymonline.com/word/one\"],\n \"ref_check\": [\n   {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None); checked Watkins/AHD, Klein and Etymonline instead.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. oi-no-\", \"stance\": \"partial\", \"note\": \"'Latin ūnus, one: INCH¹, OUNCE¹, UNCIAL, UNI-, UNION, UNITE, UNITY; … UNIVERSE … II. Suffixed form *oino-ko- … b. Latin ūnicus, sole, single: UNIQUE. III. Suffixed form *oino-lo- in Latin ūllus, any (see ne).' Everything in Nourai's box except ONION, which Watkins does not list.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.vv. one and onion\", \"stance\": \"partial\", \"note\": \"s.v. one: 'Cp. also inch, ounce, uncia, uni-, uni, Unio, Uniola, union, unique, unit, unity, the first element in unanimous, unison, universe'; s.v. onion: '… fr. L. ūniōnem … which is usually derived fr. ūnus … However, the diphthong oi in F. oignon shows that the u in L. ūniō, “onion”, is short … not a derivative of ūnus, unless … shortened in Vulgar Latin.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary\", \"stance\": \"silent\", \"note\": \"grepped 'eleven', 'ounce (1)', 'inch (1)', 'endleofan' in SKT.txt — the OCR of the entry heads is too damaged to quote; no usable hit.\"}\n ]\n})\n\nentry0 = {\n \"entry\": 0,\n \"root\": \"I 2, Io, E\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *h₁e- / *h₁ey- / *h₁i- 'this, that' — the anaphoric-demonstrative pronominal stem; Pokorny IEW 281-286 'e-3, ei-, i-, fem. ī-'\",\n \"note\": \"The root box is right in every particular. Pokorny's article, which begins on exactly the page Nourai cites, is headed 'e-3, ei-, i-, fem. ī-: this, etc. (demonstrative stem); one' and runs 281-286; Watkins/AHD gives the same material as 'i-. Pronominal stem … [Pok. 3. e- 281.]', and files *oi-no- there too ('[In Pok. e- 281.]'). Nourai's three names 'I 2, Io, E' render the ablaut alternants i- / (o)i- / e- of that single stem, the language label 'Indo-European' is correct, and 'pronominal stem' is Pokorny's own and Watkins's own wording. Two cross-cutting observations for the whole page. (1) Node 1 gathers under this root, beside the genuine *oi-no-/*oi-ṳo- of p.286, the whole of Pokorny's SEPARATE article 'au- 4, u- (: ṳe-, ṳo-)' of pp.73-75 ('Au 3, Auo' and 'Uě, Uo'). Pokorny cross-refers the two articles but never unites them, and no modern handbook derives *h₂eu- from *h₁e-; so everything that reaches the page through uta (nodes 5-8: Av. uta, Sogd. ʾty, MP ud, NP و) hangs, strictly speaking, from the wrong root, even though each individual link in that chain is impeccable. (2) One printed form on the page, 'aeva-data' in node 2, corresponds to nothing in the sources (Avestan has aēvandasa-, Mo'in's footnote at the very page Nourai cites has aevadasa); I checked the printed page and the book itself carries it, so it is the author's misprint, not an extraction error. Everything else on the page — the Iranian chains yak, yāzdah, hīč, yā, و, این, the two Sogdian demonstratives, and the whole Germanic/Latin/English wing — is standard, well-documented etymology, and several of the arrows are confirmed word for word by the very books Nourai cites (Kent p.164, Platts p.41, Mo'in at Borhan 2417 and 2242, Gharib pp.85 and 220).\",\n \"note_fa\": \"جعبهٔ ریشه از هر نظر درست است: پوکورنی درست از همان صفحهٔ ۲۸۱ که نورایی یاد کرده، مدخل «e-3, ei-, i-، مؤنث ī-: این، و غیره (ستاک اشاره‌ای)؛ یک» را تا صفحهٔ ۲۸۶ می‌آورد، و واتکینز در پیوست AHD همین ماده را زیر «i-. Pronominal stem … [Pok. 3. e- 281]» می‌آورد و *oi-no- را هم زیر همین مدخل جا می‌دهد. سه نام «I 2، Io، E» همان گونه‌های ابدال آوایی یک ستاک‌اند و معنای «ستاک ضمیری» نیز عین عبارت پوکورنی و واتکینز است. دو نکتهٔ کلی دربارهٔ این صفحه: یکم، گرهٔ ۱ دو مدخل جداگانهٔ پوکورنی را یکی کرده است: *oi-no-/*oi-ṳo- (ص ۲۸۶) که راستی از همین ریشه است، و ریشهٔ جداگانهٔ au-/u- (ص ۷۳–۷۵) که uta «و» از آن می‌آید؛ پس زنجیرهٔ گره‌های ۵ تا ۸ (اوستایی uta، سغدی ʾty، پهلوی ud، فارسی و) درون خود درست است ولی از ریشهٔ دیگری آویخته شده است. دوم، صورت «aeva-data» در گرهٔ ۲ در هیچ منبعی نیست (اوستایی aēvandasa- است و معین در همان صفحهٔ برهان قاطع aevadasa می‌نویسد)؛ تصویر صفحهٔ چاپی را دیدم و خود کتاب همین را دارد، پس خطای چاپی کتاب است نه خطای استخراج. جز این دو، همهٔ زنجیره‌های ایرانی و ژرمنی و لاتینی این صفحه معتبر است و چند پیکان آن لفظ به لفظ با همان منابعی که خود نورایی یاد کرده (کنت ص ۱۶۴، پلاتس ص ۴۱، حواشی معین در صفحات ۲۴۱۷ و ۲۲۴۲ برهان قاطع، قریب صفحات ۸۵ و ۲۲۰) تأیید می‌شود.\",\n \"sources\": [\n   \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C3%B3ynos\",\n   \"https://en.wiktionary.org/wiki/%DB%8C%DA%A9\",\n   \"https://en.wiktionary.org/wiki/%D9%87%DB%8C%DA%86\",\n   \"https://en.wiktionary.org/wiki/%D9%88\",\n   \"https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D9%86\",\n   \"https://en.wiktionary.org/wiki/%DB%8C%D8%A7\",\n   \"https://en.wiktionary.org/wiki/%DB%8C%D8%A7%D8%B2%D8%AF%D9%87\",\n   \"https://www.etymonline.com/word/one\"\n ],\n \"ref_check\": [\n   {\"ref\": \"POK:281\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: e-3, ei-, i-, fem. ī-: “this, etc. (demonstrative stem); one” … Page(s): 281-286'; the printed page marker '281' stands at POK_01.txt line 4023 and the article runs to the marker '286' at line 4095. Nourai's page number, language label and gloss all match.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. i- (p. ~34) and s.v. oi-no-\", \"stance\": \"supports\", \"note\": \"'i-. Pronominal stem. 1. Germanic *is-lik- … 7. Basic form *i-, with neuter *id-em, in Latin is, he (neuter id), and idem, same … [Pok. 3. e- 281.]' — the same root, the same Pokorny page; and 'oi-no-. One, unique … [In Pok. e- 281.]'.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 95 ff. (WLD_Bd1_pages.txt leaf 109)\", \"stance\": \"supports\", \"note\": \"The predecessor article of Pokorny 281-286, containing the same demonstrative material and '*oi-nos: ai. e-na- … lat. ūnus, alt oinos'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck, Selected Synonyms 13.32 (p.937)\", \"stance\": \"supports\", \"note\": \"'IE *oi-no-, *oi-wo-, derivs. of a pronominal stem *e-/*o-, cf. *i- beside *e- in Lat. is, etc.' — an independent modern statement of exactly the relation the root box asserts.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IE Comparative Dictionary s.v. oinos\", \"stance\": \"supports\", \"note\": \"'oinos, ā “one; unit” Skt. cf. -enaḥ “he” … Lat. ūnus … Go. ains' — Mann too links the numeral to the pronominal ena-.\"}\n ],\n \"nodes\": nodes\n}\n\nout = {\n \"pdf_page\": 225,\n \"book_page\": 195,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [entry0]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-225.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build225.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-225.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 225"
}
```


### [2026-09-06T15:49:19.288Z] TOOL RESULT

```
written
JSON OK
nodes verified: 16/16
node verdicts: {'plausible': 5, 'transcription_suspect': 1, 'confirmed': 10}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 23, 'not_found': 3, 'not_checked': 10, 'partial': 3}
books consulted: {'supports': 36, 'partial': 8, 'silent': 6, 'contradicts': 1} | by book: {'HRN': 5, 'PHD': 5, 'BRT': 4, 'NYB': 4, 'AHD': 3, 'KNT': 3, 'HUB': 3, 'SOD': 3, 'KLN': 3, 'WLD': 2, 'SYN': 2, 'IEC': 2, 'MON': 2, 'BQT': 2, 'POK': 2, 'GPL': 1, 'ARY': 1, 'HENNING': 1, 'ISS_alt_DKS': 1, 'FSD': 1, 'SKT': 1}
```


## [2026-09-06T15:49:46.098Z] AGENT

Done. `verify_check.py 225` reports 0 PROBLEM lines.

**Page 225 (book p.195) — root `I 2, Io, E` [Indo-European], 16 nodes, 4 redirects skipped**

Verdicts: root confirmed; nodes 10 confirmed, 5 plausible, 1 transcription_suspect.
Ref checks: 23 supports, 3 partial, 3 not_found, 10 not_checked. 51 `consulted` entries across 21 books.

Flagged items:
- **transcription_suspect — node #2, "aeva-data" (eleven)**: no such Avestan/OP form exists. Bartholomae col. 2685 has `aēvandasa-` 'eleventh'; Mo'in's footnote on the very page Nourai cites (BQT 2417, read from the page image) prints `aevadasa`; Platts p.41 gives OP `aivadasa`. `error_in: book` — I rendered pdf p.225 and the book itself prints "aeva-data", so the extraction is faithful. Page PNG saved to `data/verification/sources/refs/ocr/BOOK/225.png`.
- **plausible — node #1**: the box merges two *separate* Pokorny articles — `*oi-no-/*oi-u̯o-` (IEW 286, genuinely under this root) and the whole of `au- 4, u- : u̯e-, u̯o-` (IEW 73-75). Everything reaching the page via `uta` (nodes 5-8) therefore hangs from the wrong root, though each individual link is sound.
- **plausible — node #5**: Av. `uiti` is glossed 'and'; it means 'so, thus' (Pokorny 74: "av. uiti, gthav. ūiti 'so'"; Bartholomae's citations are all `uiti aojanō` 'thus speaking').
- **plausible — node #3**: Pahlavi `ayāb` 'or' is only half from Av. `vā` — Bartholomae analyses it `aδāt + vā` (cf. Skt. athavā); Wiktionary calls the further etymology unclear. "ayâo" is not a standard reading (ayāb/ayāw/ayāp).
- **plausible — node #9**: `aita/aēta` and `ima/imam` descend straight from the root stem (`*ei-to-`, `*i-`), not via `*oi-no-`; also `aēta-` is Avestan, not covered by the "Old Persian / Sanskrit" label.
- **plausible — node #16**: eight of nine words are Watkins's own list under Latin `ūnus`; `onion` is the doubtful one (Klein/Walde-Hofmann: F. *oignon* points to short u, so L. `ūniō` may not derive from `ūnus`; AHD omits ONION).
- Minor, noted but not flagged: the book prints `ŭnus`/`ne-ŭllus` with a breve (node #15); the quantities are long.

**No extraction errors** — the JSON matches the printed page exactly at every node.

Notable positives: Kent p.164, Platts p.41, Horn nos. 1071/1114/1128, Hübschmann §21, MacKenzie, Nyberg, and Gharib pp. 85/220 confirm the Iranian chains word for word; BQT 2417 and 2242 were read from page images and saved as `.vision.txt` companions. Wrong citation found: **SOD:72** — Gharib p.72 has nothing about 'and'; Sogdian `ʾty` is entry 301 on p.12. SNS page numbers (86, 91, 256) could not be mapped (scan's printed numbers unreadable; the glossary's own numerals are text page/line refs) — the index line "ud 256/1" is the one near-match. MON:345/421/4921 unreachable (6-vol Mo'in still not online); TZF unreachable.
