# Verification process log — verify-page-191


## [2026-09-06T02:13:19.085Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 191 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-191.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-191.json. Write /home/sfmqrb/git/rishe/data/verification/page-191.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 191` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T02:13:21.078Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T02:13:21.788Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T02:13:21.821Z] TOOL RESULT

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


## [2026-09-06T02:13:21.985Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-191.txt"
}
```


### [2026-09-06T02:13:22.007Z] TOOL RESULT

```
1	=== PDF page 191 (book page 161) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gheslo : thousand  (refs POK:446)
4	#1 (parent #0) [Avestan] refs=POK:446 | hazanrem, hazangra : thousand
5	  #2 (parent #1) [Persian] refs=POK:446; BQT:2331 | hezâr «هزار» : thousand
6	#3 (parent #0) [Greek] refs=POK:446 | xilio : thousand
7	  #4 (parent #3) [French] refs=AHD | kilo-
8	    #5 (parent #4) [Persian] refs=MON:3156 | kîlo «کیلو» : thousand | extra: کیلوگرم ، کیلومتر ، کیلووات
9	    #6 (parent #4) [English] refs=AHD | kilo, kilogram, kilometer, kilowatt
10	  #7 (parent #3) [Latin] refs=AHD; KLN:979; BQT:2080 | smî-gžlî : one thousandth ☞Sem 1 ; milia pasuum : thousand steps ; milie : a measure of distance | NOTE: Derivation of "millia" or "millie" from "smî-gžlî" is not quite certain.
11	    #8 (parent #7) [Arabic] refs=None | 
12	      #9 (parent #8) [Persian] refs=MON:4505; BQT:2080 | mîl «میل» : a mile, a road marker
13	    #10 (parent #7) [French] refs=AHD | 
14	      #11 (parent #10) [Persian] refs=MON:4507 | mîlî- «میلی» : one thousandth | extra: میلیمتر ، میلیگرم ، میلیون ، میلیارد
15	      #12 (parent #10) [English] refs=None | mile, millimeter, milligram, million, milliard
16	--- entry 1 ---
17	ROOT [Indo-European] Ghesto, Ghosto : hand  (refs POK:447)
18	#1 (parent #0) [Avestan / Old Persian] refs=POK:447; KLN:707; KNT:190 | zasta : hand ; dasta : hand ; dasta-karta : hand-made ☞Kwer ; abi-dasta, a-dsta : over hands, sleeve ☞Ambhi
19	  #2 (parent #1) [Persian] refs=BQT:854; AHM:220; MON | dast «دست» : hand ; âstîn «آستین» : sleeve | extra: دستار ، دستگاه ، آستن ، آستیم
20	  #3 (parent #1) [Sogdian] refs=SOD:144 | dst : hand
21	#4 (parent #0) [Sanskrit] refs=POK:447 | hastah : hand
22	  #5 (parent #4) [English] refs=KLN:707 | hasta : symbolic position of the hands in dancing
23	
```


## [2026-09-06T02:13:24.953Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-191.json",
 "description": "Read source JSON for page 191"
}
```


### [2026-09-06T02:13:24.998Z] TOOL RESULT

```
{
  "pdf_page": 191,
  "book_page": 161,
  "entries": [
    {
      "root": {
        "name": "Gheslo",
        "lang": "Indo-European",
        "refs": "POK:446",
        "gloss": "thousand"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:446",
          "words": [
            {"translit": "hazanrem, hazangra", "gloss": "thousand", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:446; BQT:2331",
          "words": [
            {"translit": "hezâr", "gloss": "thousand", "script": "هزار"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:446",
          "words": [
            {"translit": "xilio", "gloss": "thousand", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {"translit": "kilo-", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:3156",
          "words": [
            {"translit": "kîlo", "gloss": "thousand", "script": "کیلو"}
          ],
          "script_extra": "کیلوگرم ، کیلومتر ، کیلووات",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "kilo, kilogram, kilometer, kilowatt", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 3,
          "lang": "Latin",
          "refs": "AHD; KLN:979; BQT:2080",
          "words": [
            {"translit": "smî-gžlî", "gloss": "one thousandth", "script": null, "see": ["Sem 1"]},
            {"translit": "milia pasuum", "gloss": "thousand steps", "script": null},
            {"translit": "milie", "gloss": "a measure of distance", "script": null}
          ],
          "note": "Derivation of \"millia\" or \"millie\" from \"smî-gžlî\" is not quite certain.",
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Arabic",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON:4505; BQT:2080",
          "words": [
            {"translit": "mîl", "gloss": "a mile, a road marker", "script": "میل"}
          ],
          "note": null,
          "quote": {
            "text": "زیک میل کرد آفریدون نگاه - یکی کاخ دید اندر آن شهر شاه",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 10,
          "parent": 7,
          "lang": "French",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON:4507",
          "words": [
            {"translit": "mîlî-", "gloss": "one thousandth", "script": "میلی"}
          ],
          "script_extra": "میلیمتر ، میلیگرم ، میلیون ، میلیارد",
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "mile, millimeter, milligram, million, milliard", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ghesto, Ghosto",
        "lang": "Indo-European",
        "refs": "POK:447",
        "gloss": "hand"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:447; KLN:707; KNT:190",
          "words": [
            {"translit": "zasta", "gloss": "hand", "script": null},
            {"translit": "dasta", "gloss": "hand", "script": null},
            {"translit": "dasta-karta", "gloss": "hand-made", "script": null, "see": ["Kwer"]},
            {"translit": "abi-dasta, a-dsta", "gloss": "over hands, sleeve", "script": null, "see": ["Ambhi"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:854; AHM:220; MON",
          "words": [
            {"translit": "dast", "gloss": "hand", "script": "دست"},
            {"translit": "âstîn", "gloss": "sleeve", "script": "آستین"}
          ],
          "script_extra": "دستار ، دستگاه ، آستن ، آستیم",
          "note": null,
          "quote": {
            "text": "ای دل بیا که ما به پناه خدا رویم - زآنچ آستین کوته و دست دراز کرد",
            "poet": "Hâfez"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:144",
          "words": [
            {"translit": "dst", "gloss": "hand", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:447",
          "words": [
            {"translit": "hastah", "gloss": "hand", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:707",
          "words": [
            {"translit": "hasta", "gloss": "symbolic position of the hands in dancing", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-06T02:13:25.855Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && ls data/verification/sources/refs/ | head -80",
 "description": "List verification dir and refs"
}
```


### [2026-09-06T02:13:25.909Z] TOOL RESULT

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
---
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


## [2026-09-06T02:13:29.359Z] TOOL CALL #5: Bash

```json
{
 "command": "head -c 4000 data/verification/page-127.json && echo && echo === && cat data/verification/sources/SOURCE_MATRIX.md | head -100",
 "description": "Sample verification file and matrix"
}
```


### [2026-09-06T02:13:29.409Z] TOOL RESULT

```
Exit code 1
{
 "pdf_page": 127,
 "book_page": 97,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05",
 "entries": [
  {
   "entry": 0,
   "root": "Dhem",
   "verdict": "confirmed",
   "modern_form": "PIE *dʰemH- (LIV² *dʰmeh₁-) 'to blow, breathe; to smoke, raise dust'",
   "note": "Pokorny IEW 247-248 heads the entry 'dhem-, dhemə- \"stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)\"', so Nourai's language label (Indo-European) and his gloss 'to make vapor, raise dust' are an accurate short rendering of the German. Cheung (Etym. Dict. of the Iranian Verb, *damH³) writes the same root «PIE *dʰmeH- 'to blow' = LIV: 153 | Pok.: 247 f.»; Wiktionary reconstructs *dʰemH-. Watkins/AHD carries no dhem- root (its list goes dhembh- → dhen-¹), simply because no English word reaches it through Latin or Greek, so its silence is not a disagreement. Two weak spots in the chart: the Avestan node's gloss (node 1) and the name Damāvand (node 2), which Nourai's own source BQT:878 derives from a different root.",
   "note_fa": "ریشهٔ نمودار همان ریشهٔ هندواروپاییِ آغازینِ *dʰemH- «دمیدن، فوت کردن؛ دود و بخار برخاستن» است. پوکورنی در صفحهٔ ۲۴۷ کتاب خود آن را با معنای آلمانیِ «stieben, rauchen … wehen, blasen» آورده و برگردانِ کوتاهِ نورایی («بخار ساختن، گرد برانگیختن») با آن می‌خواند؛ چونگ نیز همین ریشه را *dʰmeH- «دمیدن» (LIV ۱۵۳) می‌نویسد. پس جعبهٔ ریشه، برچسبِ زبان و معنای آن درست است و ادعای نورایی در این حد پذیرفتنی است. تنها دو نقطهٔ سست در نمودار هست: معنایی که برای صورتِ اوستایی داده شده (گرهٔ ۱) و نامِ «دماوند» (گرهٔ ۲) که خودِ مأخذِ نورایی، یعنی حاشیهٔ معین بر برهان قاطع ص ۸۷۸، آن را از ریشهٔ دیگری می‌گیرد.",
   "sources": [
    "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86",
    "https://en.wiktionary.org/wiki/%D8%AF%D9%85"
   ],
   "ref_check": [
    {
     "ref": "POK:247",
     "status": "supports",
     "note": "POK_01.txt (grep -n 'dbem-' → line 3513), IEW p.247: 'dbem-, dhemo- ,stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben == düster, dunkel), wehen, blasen (hauchen = riechen)'; the page continues 'Ai. dhámati ,bläst', av. daδmainya- …, npers. damīdan ,blasen, wehen', dam ,Atem, Atemzug''. Exactly the root box as drawn."
    }
   ],
   "consulted": [
    {
     "src": "WLD",
     "where": "Bd. I 851 f. (WLD_Bd1 djvu line 53642)",
     "stance": "supports",
     "note": "'dhem-, dhemə- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)“. Bedeutungsumfang wie bei Wz. *dheu- „stieben“.' — the source Pokorny 247 abridges."
    },
    {
     "src": "CHEUNG",
     "where": "s.v. *damH³ (CHEUNG.txt line 4670 ff.)",
     "stance": "supports",
     "note": "'*damH³ \"to blow, breathe; to swell\" … «PIE *dʰmeH- \"to blow\" > LIV: 153 | Pok.: 247 f.»'"
    },
    {
     "src": "AHD",
     "where": "Watkins 1985, d-list (AHD_watkins1985.txt line 377)",
     "stance": "silent",
     "note": "the appendix runs 'dhembh-. To bury. … [Pok. (dhembh-), dhmbh- 248.] dhen-¹. To run, flow.' — no dhem- entry at all, since no English word descends from it via Latin/Greek."
    },
    {
     "src": "IEC",
     "where": "Mann, d-section (grep 'dhem' in IEC.txt)",
     "stance": "silent",
     "note": "Mann has dhen- (2) 'forehead', dhenguhó, dhinió etc. but no *dhem- 'blow, smoke' headword."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Avestan",
     "words": "dam; da-dhmainya",
     "verdict": "plausi
(eval):1: == not found
```


## [2026-09-06T02:13:31.488Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','BQT','MON','KNT','SOD','AHM','HRN','HUB','PHD','NYB','BRT','WLD','IEC','SYN','ARY','CHEUNG']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400])\n\"",
 "description": "Inspect refs_online for relevant keys"
}
```


### [2026-09-06T02:13:33.211Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
AHM {"title": "I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959", "edition_found": "1959", "kind": "archive_djvu", "url": "https://archive.org/details/gershevitch-ilya-the-avestan-hymn-to-mithra-cambridge-university", "identifier": "gershevitch-ilya-the-avestan-hymn-to-mithra-cambridge-university", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHM.txt", "page_offset": 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG null
```


## [2026-09-06T02:13:38.790Z] TOOL CALL #7: Bash

```json
{
 "command": "cd data/verification/sources/refs && grep -n \"heslo\" POK_full.txt POK_01.txt POK_02.txt POK_03.txt | head -20; echo ===; grep -n \"hesor\\|ĝhes\\b\\|hesr\" POK_full.txt POK_01.txt POK_02.txt | head -20",
 "description": "Grep Pokorny for gheslo/ghesor"
}
```


### [2026-09-06T02:13:38.859Z] TOOL RESULT

```
Exit code 1
POK_03.txt:1824:lat.   sem-per  ,in   einem   fort,   immer'  {*sem  =  gr.   ev,  vgl.   unten  germ.      \ sin-)]   simitu  .zugleich',  Ablat.  von  *si'mitus  <i*sem-eitus  ,das  Zusammen»      1 gehen*,  vgl.  air.  emith  ,tanquam,   quasi',   cymr.   hefyd  ,auch*   aus  "^semitL zu  ai.  sdm-iti- ;  mllle  ,1000'  aus  *swi  ghesll  ,eine  Tausendheit'  (irrig  S.  44( vgl.  das  in  *s7n-gheslom  zerlegte  ai.  sahdsra-m^  av.  hazaidva-  ,eintausend'F air.  cumme  .ähnlich'  aus  *kom-svino-  ,ganz  der  eine,   der  gleiche';  germ, *sin  (d.  i.  idg.  *sem  in  adv.  Erstarrung)  ,*in  einem'  =  , zusammen'  oder^J , immerwährend'  oder  .durchaus,  sehr'  in  as.  ahd.  sin-hiun,  ags.  sin-hxwwk .conjuges,   Ehegatten',   got.   sin-teins   .täglich',    as.    sin-nahti^    ags.   sin-nxki^ .ewige  Nacht',  mhd.  sin-grüene,   ags.   sin-grene^   aisl.   sl-grenn   ,immergrUn* ags.   sin-here  , großes   Heer',   ahd.   sin-fluot   ,große   Flut',   aisl.   si-valr, sine-wealty  and.  sinu-iuel  ,ganz  rund'  usw. ;
POK_02.txt:1552:Ai.  sa-hdsram  n.  ,Tausend'  (sm  -gheslom^  zu  sem-  ,eins'),  sa-hasriya-  ,tausend- ^ fach',  av.  hazarirdm  n.  ,Tausend',  npers.  hazär,  woraus  arm.  hazar  entlehnt;  ^ sogd.  2V  (=  *zär),  afgh.  z^r;
POK_full.txt:37127:Root / lemma: gheslo- 
POK_full.txt:37133:Root / lemma: gheslo- : thousand' derived from Root / lemma: ghesor-1, ghesr- : "hand, 
POK_full.txt:37137:Material: Old Indie sa-hasramn. " thousand ' {sm -gheslom, to sem- " one '), sa-hasriya- 
POK_full.txt:73331:from * smF ghes/r e\ne Tausendheit' (wrongly S. 446), compare das in *sm-gheslom 
(eval):1: == not found
```


## [2026-09-06T02:13:40.396Z] TOOL CALL #8: Bash

```json
{
 "command": "cd data/verification/sources/refs && python3 -c \"\nimport json\nd=json.load(open('../refs_online.json'))\nfor k in ['POK','SOD','KLN','BQT','MON','KNT','AHM']:\n    print(k, json.dumps(d[k], ensure_ascii=False)[:1200]); print()\n\"",
 "description": "Full ref metadata"
}
```


### [2026-09-06T02:13:42.059Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/p

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"], "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)", "covers_etymology": true, "notes": "

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-styl

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe/data/verification/source

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.", "notes": "", "cites": "page number of Kent, Old Persian (1953); the lexicon starts p. 164"}

AHM {"title": "I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959", "edition_found": "1959", "kind": "archive_djvu", "url": "https://archive.org/details/gershevitch-ilya-the-avestan-hymn-to-mithra-cambridge-university", "identifier": "gershevitch-ilya-the-avestan-hymn-to-mithra-cambridge-university", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHM.txt", "page_offset": "leaf = printed + 14 (e.g. leaf 18 = p.4). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Commentary is by stanza/note number; the Glossary (end of book) lists Avestan words. grep the Avestan word in transliteration.", "notes": ""}
```


## [2026-09-06T02:13:44.980Z] TOOL CALL #9: Bash

```json
{
 "command": "cd data/verification/sources/refs && sed -n '37120,37180p' POK_full.txt",
 "description": "Pokorny gheslo- entry"
}
```


### [2026-09-06T02:13:45.040Z] TOOL RESULT

```
only under assumption a of guttural change (above S. 18, Anm. 1) has made Lithuanian 
g/rsa " darnel ' here place (see below ghers-2). 

References: WP. I 611, WH. I 414, 657, Specht Indog. Dekl. 
Page(s): 446 

Root / lemma: gheslo- 

Meaning: thousand 

Note: 

Root / lemma: gheslo- : thousand' derived from Root / lemma: ghesor-1, ghesr- : "hand, 

*hand count' [///allophones] 

Material: Old Indie sa-hasramn. " thousand ' {sm -gheslom, to sem- " one '), sa-hasriya- 

"tausendfach', Avestan hazanr9mr\. "thousand', npers. hazar, from which borrowed 

Armenian hazar, sogd. z'/'(= *zai), afgh. zar. 

Perhaps also Latin mTlle' thousand; a thousand ', whether from *smTgzhlT{ghslT) " one 
thousand '; *smT: gr. |jia. 

gr. Ionian xsiAioi, Aeolic xsAAioi (xsAAnoTuq " a division of the people at Ephesus '), Attic 
XiAioi (*x£aAioi). 

The basic word component *x£aAo- has been found in Sakisch ysara ar\(i^ in loanwords 
of Finno-Ugric languages (Jacobsohn Arier and Ugrofinnen 105 ff.). 

References: WP. I 633, II 488, 491 , WH. II 88 f., Schwyzer Gr. Gr. I 593. 
Page(s): 446 

Root/ lemma: ghesor-1, ghesr- {*ghestoi), {*ghestai) 

Meaning: hand 

Note: 

Both Root/ lemma: ghesor-1, ghesr-'. hand' and Root/ lemma: ghesto-2\ "hand, arm' 

derived from an extended archaic root ghes+ reduced form of the common PIE suffix 

variants -tar, -ter, -tra, -tre. 



Material: Armenian Jern {*ghes-r-m), P\.Jer-k' "hand' (Meillet Esquisse 83); 

gr. xsip f- "hand", Gen. x^'poc;, Doric XHPO^. Dat. PI. x^PCfi (thereafter the form x^P-); 

Tocharian A tsar, B sa^'hand' (after Pedersen Tochar. 236 from *kesar=) (common 
labialized gr. - Tocharian k"-> t-). 

Hittite ki-es-sar {kessar) n. and ki-es-si-ra-as {kesseras) m., f., Dat. Sg. ki-is-sa-ri{kesri 
= gr. X£ipi?); 

The earlier Hittite form was probably ghes-tar > ghessar common lllyrian suffix -tar, -tor
```


## [2026-09-06T02:13:45.934Z] TOOL CALL #10: Bash

```json
{
 "command": "cd data/verification/sources/refs && grep -n \"lemma: ghesor\\|lemma: ĝhesor\\|ghesor-1\" POK_full.txt | head",
 "description": "Find ghesor entry"
}
```


### [2026-09-06T02:13:46.014Z] TOOL RESULT

```
18344:lemma: ghesor-1, ghesr-: hand'; Root/ lemma: ghesto-2\ "hand, arm' through lllyrian 
18379:Anatolian languages Root/ lemma: ghesor-1, ghesr-: "hand' because of the common alb. 
23366:Two other roots, respectively Root/ lemma: ghesor-1, ghesr-: "hand' and Root/ lemma: 
23376:*gheus'[^ar\d, arm' and Root /lemma: ghesor-1, ghesr- {* gheus-): hand' and Root/ 
37133:Root / lemma: gheslo- : thousand' derived from Root / lemma: ghesor-1, ghesr- : "hand, 
37155:Root/ lemma: ghesor-1, ghesr- {*ghestoi), {*ghestai) 
37161:Both Root/ lemma: ghesor-1, ghesr-'. hand' and Root/ lemma: ghesto-2\ "hand, arm' 
37188:lemma: ghesor-1, ghesr-: hand'; Root/ lemma: ghesto-2\ "hand, arm' through lllyrian 
37198:Both Root/ lemma: ghesor-1, ghesr-: hand' and Root/ lemma: ghesto-2\ "hand, arm' 
64985:Two other roots, respectively Root/ lemma: ghesor-1, ghesr-: hand' and Root/ lemma:
```


## [2026-09-06T02:13:48.237Z] TOOL CALL #11: Bash

```json
{
 "command": "cd data/verification/sources/refs && sed -n '37180,37260p' POK_full.txt",
 "description": "Pokorny ghesto- entry"
}
```


### [2026-09-06T02:13:48.295Z] TOOL RESULT

```
about Latin /?, /7/?"hohle hand' (from Oscan-Umbrian *her< *ghesrai7) s. WH. I 649. 

Maybe alb. {*ghestor) dore^ hand ' 

Note: 

Clearly Root / lemma: der-1{. dor-, der-) or dor-, dor-: "hand span' derived through Root/ 
lemma: ghesor-1, ghesr-: hand'; Root/ lemma: ghesto-2\ "hand, arm' through lllyrian 
intermediary. 
Page(s): 447 

Root / lemma: ghesto-2 {* ghes-toi) 

Meaning: hand, arm 

Note: 

Both Root/ lemma: ghesor-1, ghesr-: hand' and Root/ lemma: ghesto-2\ "hand, arm' 

derived from an extended archaic root ghes+ reduced form of the common PIE suffix 

variants -tar, -ten -tra, -tre. 

Material: Old Indie hasta-hm. "hand', Avestan zasta-. Old pers. dasta- ds.; 

Maybe alb. {* dasta) djathta ' r\g\r\t hand' 

Maybe Latin /?, /7/?"hohle hand' 

Note: 

Common Old Indie : Latin gh-> h-. 

Maybe alb. {*ghestoi) dore^ hand ' 



Latin praesto' at hand, ready, present, here ' from * prae-hestod {EM 805f.)?; different 
see below sta-, 

Lithuanian pa-zaste, pa-zastist " place under the arm, armpit '. 

Note: common Baltic-lllyrian gh- > z. 

There Armenian ye/77 also in *gher-m q,o\}\A also go back to gr. forms could have 
expounded better from *gher-s, there further alb. dorei. "hand', PI. konson. o'i/a/' required 
a basic form *gher- {ghesr- has produced *dostr^, with Belardi (Riv. Studi Orient. 23, 69 
ff.) could be considered, if not for the Hittite and Tocharian metathesis from -rs- to -sr- is to 
be accepted, and to be placed the group 1 from 2 to separate and to gher-^ grasp '. 

References: WP. I 541, 603, WH. I 243, Trautmann 367, Duchesne-Guillemin BSL. 39, 
211, Schwyzer Gr. Gr. I 446, 569, Specht Indo Germanic Dekl. 75. 
Page(s): 447 

Root / lemma: gheu- 

Meaning: to pour 

Material: Old \x\^\z juhoti, juhute^ pours in fire, sacrifices ', Passiv huyate, huta-h^ 

sacrificed ', homan-u. " sacrificial downpour, sacrifice, oblation' (= gr. xsujja), homa-hm. 

6s., hotar- " offerer, sacrificer, priest', hotrai. " oblation ', hav/s-n. 6s., havanamn. 

"sacrifice, oblation'; 

maybe alb. d/y'ame lat' : gr. 5r|M6(; "fat' [common alb. gh- > d-]; 

Avestan zaotar, zao&r-m. "priest, priest of sacrifice ', Middle Persian zot, Avestan 
zao&rau., zao&rai. " liquid sacrificial donation, sacrificial drink, sacrificial downpour', 
npers. zor^ holy water', Avestan azutay-t "fat, lard, luxuriance, abounding fullness, 
wealth'; 

Note: 

First of all Old Indie then Avestan, Middle Persian, npers. and alb. seem to employ Root / 
lemma: gheu- : to pour + -tra suffix. 

Armenian yby/" poured' (< gheu/o-), Jew lorm, shape'; here also yb/"" valley' (< ghouer- 
o)l
```


## [2026-09-06T02:13:56.341Z] TOOL CALL #12: Bash

```json
{
 "command": "cd data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==102||NR==103||NR==104 {print \"=== BLOCK \" NR \" ===\"; print}' POK_02.txt | head -160",
 "description": "Print Pokorny scan leaves near p.446"
}
```


### [2026-09-06T02:13:58.039Z] TOOL RESULT

```
=== BLOCK 102 ===
Plur.  ,Wohnung',  ahd.  gart m.  ,Kreis'  in  mittügart  ,orbis',  heimgart  ,forum'  usw. ;  got.  garda  ,Hürde, Viehhof,  afries.  garda  , Garten',  as.  gardo,  ahd.  garto  ds.  (oder  aus  idg. *ghor-tö-]  vgl.  x<5^rog  unter  4.  gher-);
lit.  gardas  m.  ,Pferch',  gardis  f.  , Gatter,  Gitter';
slav.  *gordh  in  aksl.  grad^  ,Burg,  Stadt,  Garten',  russ.-ksl.  ogradz  , Garten' (davon  aksl.  grazdh  m..  , Stall'),  russ.  görod  ,Stadt',  bulg.  gradz,  skr.  gräd, sloven.  gräd  ds.,  dech.  hrad  ,Burg,  Schloß',  poln.  gröd  ds. ;  tief  stuf.  slav. zbrdh  in  aksl.  zrbdh  ,Holz',  russ.  zerdb  ,lange,  dünne  Stange',  poln.  ierd£, sloven.  zrd  ,Wiesbaum';
toch.  B  kerclye"*  ,Palast'  bleibt  fern  (Pedersen  Toch.  Sprachg.  34 f.);
hitt.  gurtas  ,Festung'  (Benveniste  BSL.  33,  139)?;  s.  auch  4.  gher-.
über  lat.  urhs  , Stadt',  angeblich  aus  *ghordhoSf  s.  Georgiev  IF.  56,  200.
B.  iherdh-z
Phryg.  -zordum  ,Stadt'  (in  Manezordum,  s.  oben); lit.  zdrdas  , Gestell  zum  Trocknen  von  Korn  oder  Flachssaat,  Viehhürde',
lett.  zärds  , Gestell  zum  Trocknen,  Holzschicht,  Scheiterhaufen',  mit  In- tonations Wechsel  lit.  zardis  ,Roßgarten'  m.,  pr.  sardis  ,Zaun'  (=  ,unge- zäunter  Roßgarten');
russ.  zoröd  , Scheuer,  Schober',  weißruss.  azoröd  ,Darrhürde'.
WP.  I  608  f.,  WH.  I  242  f.,   Trautmann  78  f.,  366.
1
445
X.  ghers-,  ghres-  , Widerwille,  Abscheu,  Ekel'.
Av.  gr^hma-  , Sünder,  Frevler' (?);
arm.  garsim  ,habe  Abscheu  vor' ;
[mir.   goirt   , bitter'   (*ghorstis),   air.   gortae   ,Hunger' ;    besser  zu  guher-"] ;
mhd.  mnd.  garst,  nhd.  nl.  garstig  , verdorben,  ranzig';  ahd.  gersti  , Bitter- keit';  aisl.  gersta  , reizen,  verbittern';    s.  auch  guJier-]
lit.  grasä  f.  , Drohung,  Strenge*,  grasüs  , drohend,  ekelhaft',  gresiü,  grZsti , drohen,  abgewöhnen',  gristit,  grtsti  ,überdrüssig  werden',  grasinü,  grasmti , drohen',  lett.  grasät,  graslt  , drohen'.
WP.  I  610 f.,  WH.  I  461,    Trautmann  95.
2.  ghers-  in  Unkrautbezeichnungen?
Ahd.  gers,  giers,  girst  (Grassmann,  Dt.  Pflanzennamen  100  ff.,  Björkmann ZfdWtf.  3,  268)  , Giersch,  Aegopodium  Podagraria';
lit.  garsas  m.,  garsvä  f.  Angelica  Archangelica;  garsve  f.  ,
=== BLOCK 103 ===
 Giersch', lett.  gärsa,  gärsa,  gärsi  ds. ;  dazu  auch  lit.  girsa  f.  =  dhrse  ,Trespe' (Bromus),  lett.  dzirsi  , Trespen'  (diese  nach  Endzelin  KZ.  44,  58  zu  lat. hordeum  [s.  unter  gJierzd(h)]  , Gerste' ;  vgl.  Mühlenbach-Endzelin  I  555, 618  f.).
WP.  I  611,  Trautmann  79  f.
ghers-  und  z.  T.  gher-  , starren'  (s.  auch  3.  gher-) ;  gher-s  , Stacheltier'.
Ai.  hdrsate,  hfsyati  ,wird  starr,  sträubt  sich,  schaudert,  ist  erregt,  freut sich';
av.  zarsayamna-  ,die  Federn  aufsträubend*  (zars-  =  zf^-  =  lat.  horreö) ; '     zarstva-  n.  , Stein';
arm.  jar  (-2,  -iv)  ,Mähne  des  Pferdes'  (*^ä,W-)  ;
gr.  xsQOog  (att.  xeqQog)  f.  ,Festland',  nachhom.  auch  Adj.  ,unfruchtbar, trocken,  fest* ;  vielleicht  dehnstufiges  Nomen  von  der  s-losen  Wzf.  gher- (oder  gher-):  yrjQ  XVQ^9  Jgel'  (=  lat.  er,  eris  ds.,  erlciuSy  erinäceus,  herinäceus ds.);  gr.  xoXooq  (<  *ghorios)  , Ferkel^  (als  Borstentier),  %ofpag  ^angeschwollene Drüse  am  Halse;  Klippe'  (oder  zu  3.  gher-  ^hervorstechen',  s.  dort);
alb.  derr  , Schwein'  (<  *ghör-n-  mit  Dehnstufe  wie  in  X'^jQ)i  derk  ,Ferkel, Sau^  (<  *ghör-n-k) ;
lat.  horreö^  -ere  ,rauh  sein,  starren ;  schaudern,  sich  entsetzen'  (=  av. zarsaya-) ;  auf  *gher-kuo-  mit  dial.  i  aus  e  vor  r  +  Gutt.  (z.  B.  stircus :  stercus)  beruht  lat.  hircuSj  sabin.  fircus  , Ziegenbock'  {hirquinus,  hirclnus ,vom  Bock')  =  osk.-sab.  hirpus  ,lupus'  (wovon  der  Volksname  Hirpini)] dazu  auch  hirtus  , borstig',  hirsütus  , struppig,  rauh' ;  auf  parallelem  *ghers- kvos  beruht  (als  osk.-umbr.  Lw.)  hispidus  ,rauh';  mars.  sabin.  herna  n. PI.  ,saxa'  i^ghers-no-)  ]
446
air.  garhj  cymr.  garw  ,rauh'  (gh'UO-)]
ags.  gorst  ,Steckginster*  und  die  etymologisch  verwandte  Gruppe  gherzd,
Gerste'
'    Vgl.  im  allg.  Fick  P  219,  435,  IP  107,   IIP  130  (und   Falk-Torp  u. gjers    m.    Lit.    über    den    Fischnamen    norw.    gjers    ,lucioperca,    Sander^ schwed.  gers  ,acerina,  Kaulbarsch',   prakrit.  jhasa-  ,ein  gewisser  Fisch*). WP.  1  610,  WH.  I  413  f.,  650,  659.
gherto-  ,Milch,  Butter';  nur  ar.  und  kelt.
Ai.  ghrtdm  ,Rahm,  Butter,  Schmelzbutter';
nach  ühlenbeck  zu  jigharti  {gharati)  , besprengt,  beträufelt',  npers.  ä-yör-" dan  , vermischen,  einweichen' ; mir.  gert  , Milch'. WP.  I  607,  II  166.
gherzd{h),   Gen.  ghrzd{h)-es]  gherzdä  ,die  Stachlige,  das   Grannenkorn,^ Gerstel
Gr.  y,QT  n.  (kons.  St.,  wie  alb.  drith)  ,Gerste',  wohl  aus  idg.  '^ghrzdh,] woraus  urgr.  *kfth ;  yiQi&rjy  meist  PI.  ,Gerste',  Sg.  (später  belegt)  ,Gerstea- korn';
alb.  drith  (*ghrzdh),  drith'e  m.  n.  ,Gerste,  Getreide';
lat.  hordeum  
=== BLOCK 104 ===
(dial.  fordeum)  n.  ,Gerste'  (aus  *ghxzd{h)eiom  ^Grannen- getreide',  substantiviertes  Stoffadjektiv) ;
hochstufig:  ahd.  gersta  ^Gerste'  (* gherzdä).
Dazu  vielleicht  gr.  ä-x^gSog  f.  ,wilder  Birnbaum,  Hagedorn',  maked. ä-ysQÖaj  gr.  d-xQ(xg  ,wilder  Birnbaum'  (d  <  *s^-),  alb.  dardhe  ,Birne,  Birn- baum' (*ghor-d-)  und  der  antike  VN  JagöavoL  5
nur  unter  Annahme  eines  Gutturalwechsels  (oben  S.  18,  Anm.  1)  läßt sich  lit.  girsa  ,Trespe'  hierher  stellen  (s.  unter  2.  ghers-).
WP.  I  611,  WH.  I  414,  657,   Specht  Indog.  Dekl.
§h6slO'  ,tausend'.
Ai.  sa-hdsram  n.  ,Tausend'  (sm  -gheslom^  zu  sem-  ,eins'),  sa-hasriya-  ,tausend- ^ fach',  av.  hazarirdm  n.  ,Tausend',  npers.  hazär,  woraus  arm.  hazar  entlehnt;  ^ sogd.  2V  (=  *zär),  afgh.  z^r;
gr.  ion.  %eilioL,  äol.  xelXioi  (xeXkr^axvg  ,Tausendschaft'),  att.  yrthoi  (^xialioC),  m
Das  Grundwort  *yßo'ko-  findet  sich  in  sakisch  ysära  und  in  Lehnwörtern    1 finnisch-ugrischer  Sprachen  (Jacobsohn  Arier  und  Ugrofinnen   105  ff.).
Vielleicht  auch  lat.  mille  ,tausend;  ein  Tausend',  falls  aus  *sml  gzhll (ghsll)  ,eine  Tausendheit' ;  *sml :  gr.  ^/a.
WP.  I  633,  II  488,  491,  WH.  II  88  f.,  Schwyzer  Gr.  Gr.  I  593.
447
1.  ghesor-,  ghesr-  ,Hand'?
Arm.  jern  (*ghes-r-7n),  PI.  jer-k'  ,Hand^  (Meillet  P]squisse  83) ;
o-v.  x^iQ   f-  ,Hand^,   Gen.  xeiqdgj  dor.   xVQog,   Dat.  PI.  x^odt   (danach  die
Form  yjQ-)',
tocb.  A  tsa)%  B  sar  ,Hand^  (nach  Pedersen  Tochar.  236  aus  *kesar  =) bitt.    ki-es-sar    (kessa?-)    n.  und    ki-es-si-ra-as    (kesseras)    tu.,  i..    Dat.    Sg.
ki-ls-sa-ri  (kesri  =  gr.  x«^^^'?);
über  lat.  Jr,  hir  ,hohle  Hand^  (aus  osk.-umbr.  *Äer  <  ^ghesrä?)  s.  WH.  I  649.
2.  ghesto-  ;Hand;  Arm^
Ai.  hdsta-h  m.  ,Hand^,  av.  zasta-,  apers.  dasta-  ds. ; lat.  praestö  ,zur  Hand'  aus  ^^prae-liestod  (EM  805  f.)?;  anders  s.  unter  stä-] lit.  pa-zastZ,  pa-zastis  f.  ,Raum  unterm  Arm,  Acbselböhle^ Da  arm.   jefn  auch   auf  *gher-7n   zurückgehen   könnte  und   ebenso    die o-r.  Formen  besser  aus  *gher-s  erklärt  werden  können,  da  ferner  alb.  dor'6 f.  ^Hand',  PI.  konson.  duar  eine  Grundform  *gher-  erfordert  (ghesr-  hätte *dostr6  ergeben),  wäre   mit  Belardi   (Riv.  Studi  Orient.  23,  69  ff.)   zu   er- wägen,  ob   nicht   fürs   Hitt.   und   Tech.   Metathese  von   -rs-   zu   -sr-  anzu- nehmen sei,   und   die   Gruppe  1  von  2  zu   trennen  un
```


## [2026-09-06T02:14:37.113Z] TOOL CALL #13: Bash

```json
{
 "command": "cd data/verification/sources/refs && echo \"== AHD watkins ghes ==\" && grep -n \"ghes-\\|gheslo\" AHD_watkins1985.txt | head -20",
 "description": "Watkins AHD ghes root"
}
```


### [2026-09-06T02:14:37.176Z] TOOL RESULT

```
== AHD watkins ghes ==
382:blind: TYPHUS; TYPHLOSOLE. 11. Extended form *dheubh., “beclouded in the senses,” in suffixed o-grade form *dhoubh-o- in: a. Germanic *daubaz in Old English déaf, deaf: DEAF; b. nasalized form *dhu-m-bho- in Germanic *dumbaz in Old English dumb, dumb: pumps; c. Germanic *diibén- in Old English *dife, dove (< “dark-colored bird”): DOVE!. 12. Extended zero-grade form *dhwel- in: a. Germanic *dwelan, to go or lead astray, in Old English dwellan, to deceive (but influenced in sense by cognate Old Norse dvelja, to tarry): DWELL; b. Germanic *dulaz in (i) Old English dol, dull: DoL- DRUMS (ii) Middle Low German dul, dull: (DOLT), DULL. 13. Extended zero-grade form *dhwes- in Greek suffixed form *th(wjes-es-, smoke, whence Greek *th(w)es-es-yon, becoming theion, brimstone, sulfur: THIO-, THION-. 14. Perhaps Old English docce, dock (< “dark-colored plant”): Dock‘. 15. Perhaps Irish did, pipe: DUDEEN. [Pok. 4. dheu- 261.] dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English déaw, dew: DEW; b. compound *melith-dauwaz, “honeydew” (see melit-). [Pok. 1. dheu- 259.] dheu-’. To become exhausted, die. 1. Suffixed o-grade form *dhou-to- in Germanic *daudaz in Old English déad, dead: DEAD. 2. Suffixed o-grade form *dhou-tu- in Germanic *dauthuz in Old English déath, death: DEATH. 3. Suffixed o-grade form *dhow-yo- in Old Norse deyja, to die: DIE}. 4. Suffixed extended zero-grade form *dhwi-no- in Germanic *dwinan in Old English dwinan, to diminish, languish: DWINDLE. [Pok. 2. dheu- 260.] dheub-. Deep, hollow. 1. Germanic *deupaz in Old Eng- lish déop, deep: DEEP, DEPTH. 2. Germanic expressive denominative *duppjan in Old English dyppan, to im- merse, dip: pip. 3. Parallel root form *dheubh- in Ger- manic *deub-, *dub- in verb *diibjan in Old English dyfan, to dip, and difan, to sink, dive: pivE. [Pok. dheu-b- 267.] dheubh-. Wedge, peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek teukhos (< *theukhos), gear, anything produced, tool: HEPTATEUCH, HEXATEUCH, PENTA- TEUCH. [Pok. dheugh- 271.] dhghem-. Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, “earthling,” in Germanic *gumén- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth: CHTHONIC; AUTOCH- THON. 3. Zero-grade form *dhghm- in Greek khamai, on the ground: CHAMAEPHYTE, CHAMELEON, CHAMOMILE, GERMANDER. 4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth: HUMBLE, (HUMILIATE), (HUMILITY), HUMUS; EXHUME, INHUME, TRANSHUMANCE. 5. Suffixed o-grade form *(dh)ghom-on-, “earthling,” in: a. Latin homé, human being, man: HOMAGE, HOMBRE!, HOMINID, HOMO!, HOMUNCULUS, OMBRE; BONHOMIE, HOMICIDE; b. (in part) Latin himdnus, human, kind, humane: HUMAN, (HUMANE). 6. Suffixed form *(dh)ghem-ya in Russian zemlya, land, earth: SIEROZEM, ZEMSTVO. 7. Full-grade form *(dh)ghem- in Persian zamin, earth, land: ZAMINDAR. [Pok. ghdhem- 414.] dhghut-. Fish. Greek ikhthus, fish: 1cHTHYO-. [Pok. ghdha- 416,] dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic “ges-ter- in Old English geo- stran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.] dhgvhei-. To perish, die away. Zero-grade form *dhgvhi- in Greek phthinein, to die away: PHTHISIS. [Pok. gthdhei(a)- 487.)
524:gher-’. To shine, glow; gray. Hypothetical base of various Germanic forms. 1. Germanic *gréwaz, gray, in: a. Old English greg, gray: GRAY; b. probably Old English grighund, greyhound: GREYHOUND. 2. Germanic *gris- Jaz, gray, in: a. Old French gris (> French gris), gray: GRISAILLE, (GRISETTE), (GRISON), GRIZZLE; AMBERGRIS; b. Medieval Latin griseus, gray, grayish: GRISEOUS. [Pok. 3. gher- 441.] gher-4. To scrape, scratch. 1. Extended zero-grade form *ghr(e)-k- in: a. Greek kharax, a pointed stake, also a kind of sea bream: CHARACIN; b. Greek kharassein, to sharpen, notch, carve, cut: CHARACTER, GASH. 2. Ex- tended form *ghers-.in suffixed zero-grade form *ghrs-to- perhaps (but unlikely) in Sanskrit ghattah, ghat: GHAT. See also extensions ghréi- and ghréu-. [Pok. 2. gher- 439.] gher-5. To like, want. 1. Suffixed form *gher-n- in Ger- manic “*gernjan in Old English giernan, gyrnan, to strive, desire, yearn: YEARN. 2. Extended form *ghré- possibly in: a. Germanic *gréduz, hunger, forming *grédagaz, hungry, in Old English grédig, hungry, covetous, greedy: GREEDY; b. Greek khré, it is necessary, whence krésthai, to lack, want, use: CATACHRESIS, CHRESARD, CHRESTOM- ATHY. 3. Suffixed zero-grade form *ghr-td- in Latin hortari, to urge on, encourage (< “to cause to strive or desire”): HORTATIVE; EXHORT. 4. Suffixed zero-grade form “ghr-i- in Greek kharis, grace, favor: CHARISMA; Eucnarist. [Pok. 1. gher- 440.] ghere-. Gut, entrail. 1. Suffixed form *ghero-no- in Ger- manic *garn6, string, in Old English gearn, yarn: YARN. 2. Suffixed form *ghero-n- in Latin hernia, “protruded viscus,” rupture, hernia: HERNIA. 3. Suffixed o-grade form *ghoro-d- in Greek khordé, gut, string: (CHORD?), CORD, (CORDON); HARPSICHORD, TETRACHORD. 4. O-grade form *ghors- in Greek khorion, intestinal membrane, afterbirth: CHORION. 5. Possible suffixed zero-grade form *ghr-u- in Latin haruspex (-spex, “he who sees” < *spek-, “to see”; see spek-), “he who inspects entrails,” diviner (but perhaps borrowed from Etruscan): HARUSPEX. [Pok. 5. gher- 443.] ghers-. To bristle. 1. Extended zero-grade form *ghrzd-, prickly plant, in: a. Germanic *gorst- in Old English gorst, furze, gorse: GORSE; b. Latin hordeum, barley: ORGEAT. 2. Lengthened-grade form *ghér(s)- in Latin hér, ér, hedgehog: URCHIN. 3. Suffixed lengthened-grade form *ghér(s)-ika in Latin ériica, caterpillar: ROCKET?. 4. Suffixed full-grade form *gher-tu-, remade to *hirsu- in Latin hirsitus, bristly, shaggy, hairy: HIRSUTE. 5. Suf- fixed full-grade form *ghers-ko- in Latin hispidus (prob- ably a dialectal borrowing), bristly, shaggy, prickly: HISPID. 6. Suffixed o-grade form “ghors-eyo- in Latin horrére, to bristle, shudder, be terrified, look frightful: HORROR; ABHOR, ORDURE. 7. Suffixed full-grade form *ghers-o- in Greek khersos, dry land: CHERSONESE. [Pok. Bhers- 445.] gheslo-. Seen by some as a base for words meaning “thousand.” 1, Suffixed form *ghesl-yo- in Greek khilioi, thousand: CHILIAD, KILO-. 2. Latin mille, thousand, which has been analyzed as *smi-, “one” + a form *ghsli-, is of obscure origin: MIL!, MIL2, MILE, MILLE- NARY, MILLESIMAL, MILLI-, MILLIEME, MILLION; MIL- FOIL, MILLENNIUM, MILLEPORE, MILLIARY, MILLIPEDE. [Pok. ghéslo- 446.] ghesor-. Hand. Reduced form “ghesr- in Greek kheir, hand: CHIRO-; (CHIRURGEON), ENCHIRIDION, (SURGEON), SURGERY. [Pok. 1. 8hesor- 447.] gheu-. To pour, pour a libation. I. Extended form *gheud-. 1. Zero-grade form *ghud- in Germanic *gut- in Old English guttas, intestines: GuT. 2. Nasalized zero-grade form *ghu-n-d- in Latin fundere, to pour: FOISON, FONDANT, FONDUE, FONT, FOUND2, FUNNEL, FUSE?, FUSILE, FUSION; AFFUSION, CIRCUMFUSE, CON- FOUND, CONFUSE, DIFFUSE, EFFUSE, INFUSE, PERFUSE, PROFUSE, REFUND!, (REFUSE!), (REFUSE?), SUFFUSE,
1350:CHIEF kaput CHIEFTAIN kaput CHILIAD gheslo- CHILL gel-3 CHILOPOD ghel-una CHIME! keu-2
1714:KILO- gheslo-
1869:MICROPYLE pulé MICTURATE meigh- MID! medhyo- MIDDLE medhyo- MipcaRD medhyo- MIDGE mu-2 MIDRIFF krep- MIDWIFE me-2 MIGHT! magh-! MIGRAINE ker-1 MIGRATE mei-1 MIL! gheslo-
1870:MIL? gheslo- MILCH melg- MILCHIG melg- MILD mel-? MILDEW melit- MILE gheslo- MILFOIL bhel-3, gheslo- MILIEU medhyo- MILIUM mele- MILK melg-
1871:MILL! mele- MILLENARY gheslo- MILLENNIUM _at-, gheslo- MILLEPORE gheslo- MILLESIMAL gheslo- MILLET mele- MILLI- gheslo- MILLIARY gheslo- MILLIEME gheslo- MILLION gheslo- MILLIPEDE gheslo-, ped-! MILT mel-1
```


## [2026-09-06T02:14:37.814Z] TOOL CALL #14: Bash

```json
{
 "command": "cd data/verification/sources/refs && echo \"== KNT dasta ==\" && grep -n \"^dasta\\|dasta-\\|dastakarta\" KNT.txt | head -30",
 "description": "Kent Old Persian dasta"
}
```


### [2026-09-06T02:14:37.864Z] TOOL RESULT

```
== KNT dasta ==
1175:pIE *ghosto-, OP dasta- ‘hand’, Av. zasta-, Skt. hasta-.
1428:est; pIE *ghosto- ‘hand’, OP dasta-, Av. zasta-,
1798:$45. NOUN AND ADJECTIVE STEMS WITH SUF- prx. -ta- found in OP are mostly participles ($242), superlatives (8190.1), and ordinal numerals (8204). The remaining examples are aruvasta-, a neuter abstract seemingly formed upon an adjec- tive *aryani- (see Lex. s.v.); XSaérita-, а hypo- corstie to a compound personal name; ardata- ‘silver’, perhaps an -a- extension of a participle in -ni-, cf. Lat. arg-ent-um; dasta- ‘hand’, which can- not be related to any simpler extant root; and three feminine abstracts arsid-, hanalü-, avaslá-, the last two of which are dubious and the third is taken as having acquired concrete meaning.
2236:The inst. dastathiya and pddaihiyd have the stems dasta- and pida-, with the pronominal plural element -2, plus the inst. ending -bhi + -й, as in Av. dat. du. aspačibya ‘two horses’ = *aspaibyd: the dat., inst., loc. are identical in the dual, in Aryan languages. Skt. has in this form dSvabhydm, with -bhyä (as in Iranian) added to the dual in -à as a stem, and a final -m attached; OP udibiyd is the same formation to uXiy, cf. Skt. aksibhyüm to akşī ‘two eyes’. OP wsiyd seems to be an inst. dual (it, has the same use and meaning as wibiyd) formed on the dual stem with the iust. sg. ending -à; gausáya is а like formation to gaušā. The i before the -à in usiyd is responsible for the glide -y-, which has spread to gaušāyā as а vowel-separator; the prior à m gauXiyü indicates that the -i- in usiyé also is long!
5252:karonaoitt, Skt. kr-, pres. krndti karóti (809, $122, $132.2, 5182.3). See also akarta-, ucára-, kara-, dastakarta-, duskarta-, hakarta-.
5537:dasta- sb. ‘hand’: Av. zasta-, N Pers. 0051, Skt. hdsta-, pIE *ghosto- (§88, $116, $145). See also dastakarta-. даѕіауа ism. DR 4.35. dastaibiya idm. (§189) DNb 41.
5538:dastakarta- adj. ‘handmade’: dasta- + pte. .
```


## [2026-09-06T02:14:43.909Z] TOOL CALL #15: Bash

```json
{
 "command": "cd data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'dastakarta- adj' in p:\n        print('leaf index',i,'-> printed page approx',i-15)\n        print(p[:1500])\nEOF",
 "description": "Locate Kent dasta page"
}
```


## [2026-09-06T02:14:44.944Z] TOOL CALL #16: Bash

```json
{
 "command": "cd data/verification/sources/refs && grep -n \"^hasta,\\|^hasta \" KLN_1966.txt | head; echo \"=== mile ===\"; grep -n \"^mile,\" KLN_1966.txt | head",
 "description": "Klein hasta and mile"
}
```


### [2026-09-06T02:14:45.395Z] TOOL RESULT

```
leaf index 213 -> printed page approx 198
5-6).
Dérayava'u- sb. ‘Darius’ (I, son of Hystaspes, king 522-486 ».c.; IT, son of Artaxerxes I, king 426-04 в.с.): Elam da-ri-a-ma-u-ts, Akk. da-ri- ja-mus, Gk. Дарєюѕ (by haplology for *Aapetaios; Keiper, Acta Sem. Phil. Erlangen, 1.253). From pAr. *dháragat-, pic. to root in OP dar- (§162, §240), + pAr. *yasu asn. ‘the good’ (5158.1), see OP vau-: ‘He who holds firm the good’ (Hz. Arch. Hist. Iran 40, ApI 255, 267, takes as hypocoris- tie of *ddraya-vahu-manah- ‘Holder of Good Thought’; this is rejected by Nyberg, Rel. 361).
Dérayavaus nsm. (8118.IV, 5124.2) DB 1.1, 4, 6,9, 11, 13, 171, 201, 24, 27, 35, 44, 48, 61, 71, 73, 81, 83, 90; 2.1, 5, 8, 11, 13f, 18, 29, 37, 42f, 49, 57, 64, 70, 78, 91, 92; 3.1, 9, 10f, 19f, 21, 29, 40, 49, 53, 54, 64, 69, 75, 76, 83; 4.1, 2f, 31, 33, 36, 40, 43, 45, 50, 58, 57, 59, 611, 67, 69f, 72, 76; 80, 86, 88; 5.1, 14, 18, 20, 30, 34^; DBa 1, 41,9, 14; DPa 1;
190 OLD PERSIAN
DPb; DPd 4f, 5, 12; DPe 1, 5f, 19; DPh 1, 3f; DNa 8, 15, 30f, 40, 47t; DNb 5; DSa 1, 3; DSb 1f°; DSc; рва 1°, 3°; DSe 8, 14, 30f°, 41^, 49f; DSf 5f, 8, 55; DSg 1, 3; DSi 1, 3; DSj 1, 2, 5; DSk 1, 3f; DSI 1; DSm 1, 3°; DSn 1°; DSo 2f; D8q 2; DSt 7°, DSy 1; DZa; DZb 1; DZe 4, 7; DE 12; DH 1, 8; XPc 11; XPf 16f, 30, 38; XPg 6; XSa 2; XV 17; D*Sa 2; D'Sb 1°, 3°; Аа 3; Wa 21; Wb 1; We 2; Wd 2; SDa; SDb. Dérayavahaus as nsm. XPf 25 (851; Lg. 9.39).
Dérayavaum asm. DPd 2; DNa 5; ОХЬ 4; DSe 5^; DSf 3f; DSn 2; DSp 1f°; DSt 5°; DZe 3; DE 7; XPf 221; D'Sa 2f.
Dérayavahaus gsm. (8118
```


### [2026-09-06T02:14:45.461Z] TOOL RESULT

```
=== mile ===
23882:mile,  n.  —  ME.,  fr.  OE.  mil,  pi.  mila,  mile,  fr.  L. milia,  pi.  of  milte,  ‘a  thousand’  (in  .  .  .  milia  pas- suum,  ‘. .  .  thousand  paces’,  i.e.  ‘.  . .  miles’).  L. milte  is  of  uncertain  origin.  It  is  perh.  cogn. with  Gk.  xtkioi,  OI.  sa-hasram,  ‘a  thousand’; see  Walde-Hofmann,  LEW.,  II,  88  s.v.  mille. Cp.  mil,  millennium,  millesimal,  million.  Cp. also  kilo-.
```


## [2026-09-06T02:14:53.632Z] TOOL CALL #17: Bash

```json
{
 "command": "cd data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if re.search(r'\\nmile,  n\\.', p) or 'mile,  n.  —  ME.,  fr.  OE.  mil' in p:\n        print('leaf',i, 'approx printed', (i-12)*2)\n        # print page markers\n        print([m for m in re.findall(r'\\n\\s*(\\d{3,4})\\s*\\n', p)][:10])\nEOF",
 "description": "Klein leaf for mile"
}
```


## [2026-09-06T02:14:54.581Z] TOOL CALL #18: Bash

```json
{
 "command": "cd data/verification/sources/refs && grep -n \"hasta\" KLN_1966.txt | head -20; echo ==KLN1971==; grep -n \"^hasta\\b\\|hasta,  n\" KLN_1971.txt | head",
 "description": "Klein hasta"
}
```


### [2026-09-06T02:14:55.491Z] TOOL RESULT

```
leaf 525 approx printed 1026
['979', '980']
```


### [2026-09-06T02:14:55.546Z] TOOL RESULT

```
Exit code 1
1142:Abderite,  n„  i)  an  inhabitant  of  Abdera;  2)  a fool.  —  L.  Abderita ,  fr.  Gk.  ’A(38r)ptnr]!;,  ‘in¬ habitant  of  Abdera’,  fr.”A[38if]pa  (pi.),  ‘Abdera’, a  town  proverbial  for  the  stupidity  of  its  in¬ habitants.  For  sense  development  cp.  Gotha¬ mite.  For  the  ending  see  subst.  suff.  -ite. abdest,  n.,  the  Mohammedan  rite  of  washing  the hands  before  prayer.  —  Pers.  dbddst,  lit.  ‘water for  the  hand’,  fr.  ab,  ‘water’,  and  dost,  ‘hand’. Pers.  ab,  ‘water’,  is  rel.  to  Avestic  dp-,  OI.  dpah (fern,  pi.),  ‘water’;  sec  amnic  and  cp.  the  first element  in  abkari  and  the  second  element  in doab  and  in  julep.  Pers.  dost,  ‘hand’,  is  rel.  to Avestic  zasta,  ‘hand’,  fr.  I.-E.  base  *ghosto -, whence  also  OI.  hastah,  ‘hand’.  See  hasta  and cp.  hath.
3807:-ate,  subst.  suff.  forming  names  of  salts  from acids  whose  names  end  in  -ic,  as  nitr ate,  fr. nitric  acid  (chem.)  —  L.  -arum,  neut.  of  pp.  suff. -dtus.  See  adj.  suff.  -ate. atelectasis,  n.,  incomplete  expansion  of  the  lungs (med.)  —  Medical  L.,  compounded  of  Gk. a-tdkTfi,  ‘incomplete’,  and  £xxa ait;,  ‘extension, expansion'.  The  first  element  is  formed  fr.  d- (see  priv.  pref.  a-)  and  x£Xo 9,  ‘end’;  see  teleo-. For  the  second  element  see  ectasis. atelier,  n.,  workshop,  studio.  —  F.,  fr.  OF.  aste- /  lier,  fr.  astelle,  ‘shiver  of  wood’,  fr.  Late  L.  as- tella,  fr.  L.  astula,  which  is  prob.  a  blend  of assula,  ‘shiver  of  wood’  and  hastula,  ‘a  little spear’.  Assula  is  a  dimin.  of  assis,  ‘board,  plank’ ; see  ashlar.  Hastula  is  a  dimin.  of  hasta,  ‘spear’; see  hastate.*
6710:castor,  caster,  n.,  a  small  wheel  fixed  below  a chair  leg.  —  Formed  fr.  cast  in  the  obsolete sense  'to  turn’.  See  prec.  word, castor,  n.,  callosity  on  a  horse’s  leg.  —  Prob.  a corruption  of  ME.  castane,  castanie,  fr.  ONF. castaine  which  corresponds  to  OF.  chastaigne (F.  chdtaigne),  lit.  ‘chestnut’.  See  chestnut, castoreum,  n.,  castor  (a  secretion  of  the  beaver). —  L.  fr.  Gk.  xaaxoptov,  fr.  xdaTtop,  gen.  xaa- ropoq,  ‘beaver’.  See  castor,  ‘beaver’.
7363:chestnut,  n.  —  Shortened  fr.  chesten  nut,  fr.  ME. chesteine,  chasteine,  fr.  OF.  chastaigne  (F.  chatai- gne),  fr.  L.  castanea,  fr.  Gk.  (xapua)  xaa-rave  ia, fr.  xotaravov,  ‘chestnut’,  which  is  commonly derived  fr.  KaaravL;,  a  town  in  Pontus,  but  in reality  a  loan  word  from  a  language  of  Asia Minor ;  cp.  Arm.  kask,  ‘chestnut’,  kaskeni,  ‘chest¬ nut  tree’.  The  town  Kaoravl?  is  named  after  the fruit  and  lit.  means  'Chestnut  Town’.  Cp.  castanet. Derivative:  chestnut,  intr.  v.
17275:haslet,  harslet,  n.,  edible  viscera  of  an  animal.  — ME.  hastelet,  hastlet,  fr.  OF.  hastelet  (F.  hate- lette).  The  original  meaning  was  ‘something roasted  on  a  spit’,  fr.  haste,  ‘a  spit’,  fr.  L.  hasta, ‘a  spear’.  See  hastate  and  -et.  The  r  in  harslet  is due  to  the  influence  of  OHG.  harst,  ‘gridiron’, hasp,  n.,  a  clasp.  —  ME.  haspe,  hespe,  fr.  OE. hsrsp,  heepse,  rel.  to  ON.  hespa,  Dan.  haspe, Swed.  haspe,  hasp,  Norw.  hasp,  MLG.,  MDu., MHG.,  G.  haspe,  OHG.  haspa,  ‘hasp,  hook', and  cogn.  with  L.  capsa,  ‘chest,  box’.  See  case, ‘box’.  E.  hasp  is  not  cognate  with  L.  cuspis (see  cusp).
17278:Derivative:  hassock-y,  adj. hasta,  n„  1)  symbolic  position  of  the  hands  in
17280:dancing;  2)  a  cubit  (measure).  —  OI.  hdstah, ‘hand;  trunk  of  an  elephant’,  rel.  to  Avestic zasta-,  OPers.  dasta-  (whence  Pers.  deist),  ‘hand’, and  cogn.  with  Lith.  pazaste,  ‘armpit’.  Cp.  hath and  the  second  element  in  abdest. hastate,  adj.,  spearlike;  resembling  the  head  of  a spear  ( bot .)  —  L.  hastatus,  ‘armed  with  a  spear’, fr.  hasta,  ‘shaft,  spear’,  which  is  cogn.  with Goth,  gazds,  ‘goad’,  OE.  gierd,  geard,  ‘rod, stick,  yard’.  See  yard,  ‘unit  of  length’,  and  adj. suff.  -ate.
17281:Derivative :  hastate-ly,  adv. haste,  n.  —  ME.  hast,  haste,  fr.  OF.  haste  (F. hate),  fr.  Frankish  *haifst,  ‘violence’,  which  is rel.  to  OE.  hast,  ‘violence,  fury’,  OFris.  hast, ‘haste’,  OHG.  heisti,  OFris.  haste,  OE.  hzeste, ‘violent’,  OHG.  heiftig,  of  s.m.,  ON.  heipt  (for *heift),  heifst,  ‘war,  hatred’,  Goth,  haifsts, ‘struggle,  strife’.  Du.  haast  (whence  MLG.  hast, whence  G.,  Dan.,  Swed.  hast),  ‘haste,  hurry’,  is borrowed  fr.  OF.  haste.
17291:lit.  ‘the  hand’,  fr.  OI.  hdstah,  ‘hand’.  See  hasta. Hathor,  n.,  the  goddess  of  love  and  joy  in  Egyp¬ tian  mythology.  —  Gk.  'Affcop,  fr.  Egypt.  Het- Hert,  lit.  ‘the  house  above’.
(eval):1: =KLN1971== not found
```


## [2026-09-06T02:15:03.440Z] TOOL CALL #19: Bash

```json
{
 "command": "cd data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'symbolic  position  of  the  hands  in' in p:\n        print('leaf',i)\n        print(re.findall(r'\\n\\s*(\\d{3,4})\\s*\\n', p)[:10])\n    if re.search(r'\\nmille', p) and 'thousand' in p and i>500 and i<540:\n        pass\nEOF",
 "description": "Klein leaf/page for hasta"
}
```


### [2026-09-06T02:15:05.082Z] TOOL RESULT

```
leaf 381
['707', '708']
```


## [2026-09-06T02:15:05.258Z] TOOL CALL #20: Bash

```json
{
 "command": "cd data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[525]\nimport re\ni=p.find('mil,')\nprint(p[:200])\nprint('...')\nfor kw in ['mil,','milli-','million','milliard','mille']:\n    j=p.find(kw)\n    print('---',kw,j)\n    if j>0: print(p[j:j+700])\nEOF",
 "description": "Klein page 979 area content"
}
```


### [2026-09-06T02:15:10.140Z] TOOL RESULT

```
ere  referred  to.
midst,  n.  —  ME.  middest,  midest,  formed  with intensive  suff.  -t  fr.  middes,  mides,  adverbial  gen. of  mid.  See  mid,  adj.,  and  cp.  amid,  amidst. Cp.  also  again
...
--- mil, 4801
mil,  n.,  a  unit  of  length  equal  to  one-thousandth part  of  an  inch.  —  L.  milte,  ‘a  thousand".  See mile.
milarite,  n.,  a  silicate  of  potassium,  calcium  and aluminum  {mineral.)  —  Named  after  Val  Milar. The  name  is  due  to  the  erroneous  belief  that this  mineral  is  found  in  Val  Milar  in  Switzer¬ land.  In  reality,  it  occurs  in  Val  Giuf  in  the  same
country.  For  tne  ending  see  suosi.  sun.  -lie. milch,  adj.,  giving  milk.  —  ME.  milche,  fr.  OE. -milce  (in  pri-milce,  ‘May’  (i.e.  the  month  in which  cows  can  be  milked  three  times  daily), rel.  to  ON.  mjolkr,  milkr,  Du.  melk,  OHG., MHG.  melch,  G.  melk,  ‘giving  mi
--- milli- -1
--- million 7444
million.  Cp. also  kilo-.
mileage,  n.,  distance  in  miles.  —  Formed  fr.  mile with  suff.  -age.
Milesian,  adj.,  pertaining  to  Miletus,  an  ancient city  of  Asia  Minor;  n.,  a  native  of  Miletus.  — Formed  with  suff.  -an  fr.  L.  Milesius,  fr.  Gk. MiXr,<Jioi;,  fr.  MtXrjxoc,  ‘Miletus’.
Milesian,  adj.,  Irish;  n.,  an  Irishman.  —  Formed with  suff.  -an  fr.  Milesius,  Latinized  form  of Miledh,  name  of  a  legendary  Spanish  king, whose  sons  are  said  to  have  conquered  Ireland. This  name  derives  fr.  Ir.  mileadh,  ‘champion’, fr.  OIr.  mil,  gen.  miled,  ‘soldier’,  which  is  a  loan word  fr.  L.  miles,  gen.  militis.  See  militia, milfoil,
--- milliard -1
--- mille 7400
mille. Cp.  mil,  millennium,  millesimal,  million.  Cp. also  kilo-.
mileage,  n.,  distance  in  miles.  —  Formed  fr.  mile with  suff.  -age.
Milesian,  adj.,  pertaining  to  Miletus,  an  ancient city  of  Asia  Minor;  n.,  a  native  of  Miletus.  — Formed  with  suff.  -an  fr.  L.  Milesius,  fr.  Gk. MiXr,<Jioi;,  fr.  MtXrjxoc,  ‘Miletus’.
Milesian,  adj.,  Irish;  n.,  an  Irishman.  —  Formed with  suff.  -an  fr.  Milesius,  Latinized  form  of Miledh,  name  of  a  legendary  Spanish  king, whose  sons  are  said  to  have  conquered  Ireland. This  name  derives  fr.  Ir.  mileadh,  ‘champion’, fr.  OIr.  mil,  gen.  miled,  ‘soldier’,  which  is  a  loan word  fr.  L.  mi
```


## [2026-09-06T02:15:20.503Z] TOOL CALL #21: Bash

```json
{
 "command": "cd data/verification/sources/refs && grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -3; echo ---; python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('n pages',len(pages))\n# find printed page 854\nfor i,p in enumerate(pages):\n    if 'دست' in p and re.search(r'85[3-6]', p):\n        print('leaf',i, p[:80].replace('\\n',' '))\nEOF",
 "description": "Locate BQT vol2 page 854"
}
```


### [2026-09-06T02:15:22.226Z] TOOL RESULT

```
---
n pages 684
leaf 569
```


## [2026-09-06T02:15:26.302Z] TOOL CALL #22: Bash

```json
{
 "command": "cd data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (0,1,2,300):\n    print('=== leaf',i,'===')\n    print(pages[i][:300])\nEOF",
 "description": "Inspect BQT vol2 structure"
}
```


## [2026-09-06T02:15:27.368Z] TOOL CALL #23: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py",
 "description": "Read ref_page.py header"
}
```


### [2026-09-06T02:15:28.276Z] TOOL RESULT

```
=== leaf 0 ===

=== leaf 1 ===
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
              ‫لض‌بال ‪ ۰ ۲۶‬رک‬
‫‪۱‬‬       ‫اسا تعدولیدیارتم و‬
                                     ‫‪7‬‬
‫‪ ۰‬و زل رسوا »وا روون لات سا روصا مواقم‬      ‫وتان‬

                      ‫‪۴2 ۱‬‬

=== leaf 2 ===
                   ‫م‬ ‫و‬
‫نآکو سخنیم بیاموزد مرا‬
                       ‫د‬ ‫د‬ ‫ل‬ ‫ج‬ ‫م‬ ‫ة‬ ‫چ‬ ‫ا‬ ‫ی‬ ‫د‬
‫على ‪۰‬‬             ‫بند گر دا ند ‪۰‬‬                       ‫‪۳‬‬      ‫‪۳7‬‬

‫داربان مقدمهٌ مجلد اول برحان قاطع ( صفحدٌ صد وسی ودو ) نگارنده از‬
                                   
=== leaf 300 ===
        ‫رح‬

 ‫ولام وسکون‌الی‬      ‫در لك ‪ = ۳‬تکراول‬                         ‫در لك = بقتح اول بروزن قدك‪,‬دستارجه‬
‫وکاف ‪ .‬جام کوناه قد آستن کوناه پیش واز را‬                 ‫رگاونند که رومال ورویاك باشد ؛ و باين معثی‬
                                               ‫وتف‬        ‫بجای حرف ان
```


### [2026-09-06T02:15:28.315Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Fetch ONE cited page of a scanned reference, on demand.

    python3 tools/ref_page.py BQT:918          # printed page 918 of Borhan-e Qate'
    python3 tools/ref_page.py IRN:119 --image  # also print the path of the page image
    python3 tools/ref_page.py BQT:918 --pdf-page 375   # override the offset mapping

Looks up the reference in data/verification/sources/refs_online.json
(`scans`: list of {file, first_printed, last_printed, pdf_offset, lang}), renders the
matching PDF page to PNG (for reading with a vision model), OCRs it with tesseract in
the reference's language(s), caches both under
data/verification/sources/refs/ocr/<ABBR>/<printed page>.{png,txt}, and prints the
OCR text. Only the cited page is ever processed — never the whole book.

`pdf_offset` means: pdf page index (1-based) = printed page + pdf_offset.

If the OCR is too poor and you transcribe the relevant passage(s) from the PNG yourself,
save that transcription as <printed page>.vision.txt next to the .txt; from then on this
tool prints the transcription instead of the OCR, so no page is ever read twice.
"""
import sys, os, json, subprocess, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "verification", "sources")
TABLE = os.path.join(SRC, "refs_online.json")
REFS = os.path.join(SRC, "refs")
OCR = os.path.join(REFS, "ocr")
TESSDATA = os.path.join(REFS, "tessdata")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    m = re.match(r"^([A-Z]+)(\d*):(\d+)$", args[0])
    if not m:
        print("expected ABBR:page (e.g. BQT:918 or MON5:528)"); return 2
    abbr, vol, page = m.group(1), m.group(2), int(m.group(3))
    table = json.load(open(TABLE, encoding="utf-8"))
    ref = table.get(abbr, {})
    scans = ref.get("scans") or []
    if vol:
        scans = [s for s in scans if str(s.get("volume", "")) == vol] or scans
    scan = None
    for s in scans:
        if s.get("requires_volume") and not vol:
            continue
        if s.get("first_printed", 0) <= page <= s.get("last_printed", 10**9):
            scan = s; break
    if "--pdf-page" in argv:
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
```


## [2026-09-06T02:15:31.881Z] TOOL CALL #24: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/ 2>/dev/null; ls data/verification/sources/refs/ocr/BQT 2>/dev/null | head -40",
 "description": "Check OCR cache"
}
```


### [2026-09-06T02:15:31.939Z] TOOL RESULT

```
AFM
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1225.png
1225.txt
1225.vision.txt
1275.png
1275.txt
1339.png
1339.txt
1357.png
1357.txt
1382.png
1382.txt
1385.png
1385.txt
1385.vision.txt
1445.png
1445.txt
1445.vision.txt
1452.png
1452.txt
1455.png
1455.txt
1462.png
1462.txt
1465.png
1465.txt
1471.png
1471.txt
1472.png
1472.txt
1488.png
1488.txt
1492.png
1492.txt
1624.png
1624.txt
```


## [2026-09-06T02:15:34.634Z] TOOL CALL #25: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2331 2>&1 | head -60",
 "description": "Fetch BQT page 2331 (هزار)"
}
```


### [2026-09-06T02:15:42.095Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 414; check the printed number and re-run with --pdf-page if off)
REF: BQT:2331  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 414  OCR-lang: fas

-- ۳۳۱ هزاراسه
و زن فاحشه راهم میگوبند ‎٩‏ . ۱
بیان هفتم
در های هوز با زای نقطه دار مشتمل بریست وشش لفت وکنایت
هزار - بنتح اول ده صد را گویند ارد هم هست که ده هزار باشد و درین زمانه
که بعربی‌الف خواشد ۴ - و پلبل راهم کفته‌انن | داو (۱) هزار میگوبند ۴ +
که عربان عندلیب خوانند ۴ - و بازی چهازم هزار اسب بفتح اول‌وهمزه درچهارم
(۱) چش : دراو (۱)
۱ - در فرهنگها (جهانگیری . رشیدی » فرهنگه نطام) این‌شسر شهید بلخی را شاهد
آورده‌اند :
چند پردارد آن (این) هربوه خروش نشود باده بر سرودش نوش
راست گوبی که در گلو شکسی پوشکی را همی بمالدگوش.
آقای نقیسی « تعلیقات تاربخ بیعقی مس ۸4۹ پس از ذکر این معنی و شم مزبور , نوشته‌اند:
باشد » و ممکن است که درین‌جا هم مراد شهید بلخی از هریوه یکی ازمردم هرات بوده باش د که
آواز را بد میخوانده و بانگه زنده داشته‌است . و بیشتن بدان مینماید که در یکی از فرهنگها
3 هروه ۳ زری که دتباله آن ضفْمّی مانند آممته پا لطس آن‌آورده باشند هعنی کرده‌اندومثلا
ثرکیب « زرآمفته » با چیزی ماشد آن به « زن فاحشه > تحریف شده باشند .> اما ‎٩‏ زرآغشته»
با ممنی «زر خالص» که پیشترگفته شد (رك : ح ه ص‌قبل) متناقش است . ممکن است حدص زد
هربوه » مصوف 3« هره > باشد که در بمشی لفجه‌ها ( از جمله سمنالی ) بمعنی خروس است
(ر4 : خروس ) ۰
اس ‌ اوستا ‌- ۱۳۳۱۱ [۱ هزار).. پهلوی هط [۱ رك : جزارم) ارنی اج
04 (حزارید ) » هندی باستان -9838878 ۰ افقالی227 (عزار) ؛ ایمنی عم 88287
« اسدق ۰۱۹۳ کردی 86287 (هزار ) , 85287 . ۵۳2247 , 7ق2ه3 ؛ زاز؟ 6228۴
« ژابا صس 44۳ > ؛ زباکی 82۵47 «گربرسن ص ۷4 ؛ گیلکی 88287 .
۴ - قی : هزاردستان . هزارآوا . از قول بیرولی ( رك.: هزاز دستاق ) و بیت ذبل‌ر
میآید که «هزار» جز عندلیب (بلیل): ات ::
عندلیبابرا چه پیش‌آعد » هزارابرا چه هد:؟
حافظ شیرازی . دبوان ض ۱۱۵ *.
۶ نود نود هرازه نوم زاران:» اهزاوان -.
```


## [2026-09-06T02:15:45.987Z] TOOL CALL #26: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2080 2>&1 | head -70",
 "description": "Fetch BQT page 2080 (میل)"
}
```


### [2026-09-06T02:15:56.265Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 163; check the printed number and re-run with --pdf-page if off)
REF: BQT:2080  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 163  OCR-lang: fas

میل اسف یه سا
هل » بکسر اول بر وزن فیل » مقدار میلاد - بروزن بیداد » نام شهری است
یلك مدجی باشد ازروی زمین ۱ - وآنچه باآن | که‌کید پادشاه قنوج که یکی‌از رایان هند بوده
توتیا و سرمه درچشم کشند ۳ - و قلم ی که روی آبرا دارالملك ساخته بوده است ‎٩‏ - و نام یکی
تخته و مانند آنرا بدان تش‌کنند ۴ ء و.بستی | ازیپلوانان ابران‌است که چون کیکاوی بمازندران
میل را قلم تخَهٌ خاك کنته‌اند ۴ - و نشالی ی که رفت ایران را باو سپرد » وکر کین پر اوست۷ ۰
هرراهها بجهت تشخیص فرسنگه ودرمیدان بجهت میلامیل ‎٩‏ - یمنی میل تا میل ومیل
چ وکان‌بازی اسب سازند ۴ - وبفتح‌اول» درعربی | در میل ومیل اندر میل - و بمعنی پی دراپی
بمعنی خواهش و توجه ورغبت دل باشد ؛ وبعنی | وتواتر - وهمه وجمیع - وممزوج ودرهم آميشته
کوبند بهمةٌ معالی عریی است 9 - هم هست .
۱ - لانینی 21112 , ۳۳112 ( 02991102 2211112 ) هزار کام ۶ مرچنت 6۳۸4
(ر4 : ح 4( انگلو ساکسن آ5۵1 , انگلیسی 1[6ْ1 , میل در روم قدیم براینر ۱۹۴۶ « بارد »
انگلسی با ۱۶۸۲ مترفراسوی بود « وبتن » - این کلمه معرب شده ۰ در عریی « مقدارمنتهای
درازی ی از زمین » با « مسافت زمین متراخيةٌ بی‌حد » و « سه يك فرسنگه > « منتهی‌الارب»
آمده . در نزد قدمای اهل هیلت ۳۰۰۰ ذراع و در نزد متأخران 4*۶۰ نراع است و خلاف‌لفظی
است » زبرا آنان اتفاق دارند بربن که مقدار آن ۹۹*۰۰ اصبع ( انگشت ) است بحسب اختلاف
ایغان در فرسخ که آپا فرسخ ۹۰*۰ ذراع قدماست ویا ۱۲*۰۰ ذراع متأخران . جمع کلمه :
امیال » امیل » میول « اقرب‌الموارد بنقل از مصباح » . ۴ - (عر) «میل بالکس, چوب
سرمه کش» « منتهی‌الارب ». اصممی کوید : * قول العامة المیل ماتکحل به المین خطاً , انما هو
الملمول » ۶۸ اقرب الموارد » و ظ . معرب است . ۴ - (عر) « میل فلم تخته خاکه »
منتپی‌آلارب » . ۴ - لالینی 1[1127105 از 11010[ بمعنی هزار ( 81[112۳۵ فر)
وآن بستونهایی اطلاق میشده که برای تعیین مافتی, برابر ۱۰۰۰ کام در جاده‌ها نب میکردند
« مرچنت ۳44 » « لاروی بز رکه » و رك : ح ۱ - در عربی نیز بمعتی لشانهٌ راهها وانیز بمعتی
مناری که برای راهتمایی مافران در مرتفعات زمین بناکنند » بکار رفته « اقرب الموارد » و در
فارسی هم باین ممانی مستعمل است ( مثلا «میل‌نادری» ) 8 - نیز (عر) آلنی‌است جراح
راکه بدان عمق‌زخم ومانند آنرا بیازماید « اقرب‌الموارد » » آهن جراح و کحال « منتهی‌الارب >
بان معنی درفارسی غالبا « میله »کوبند .- نیز میل ( فراتسوی 8۵11 ) « لاروس بز رکه >نوعی
از دبو س که یکسرآن ضخیم‌تر از سر دیگر است وآنرا در ورزش بکار برند .
‎۹٩‏ - رك : فعرست ولف . ۷ - نام قهرمائی ایرانی پدرکر کین « فپرست ولف»
وآن بقول نلد که ومار کوارت نام پادشاه اشکانی است دراصل «حماسةٌ ملی ایران . نلد که ص۷.
مار کوارت کوید این نام محرف « مپرداد » * ۸11112۳8021 است که نام چندتن آزشاهان‌اشکانی
بوده » از آن جمله است نام یکی از دشمنان کوترزی (کودرز ) که در کناب تاسيتئوی صورت
8 خبط شده . درفهرستی که پوستی ازپادشاهان اشکانی ترتیب داده بنام‌شش«مپرداد»
برمیخوریم که یکی ازآدان مماصن کوترزی » ومانند او بیستمین پادشاه اشکانی وازممارشان اوست.
رك : دکترصفا. حماسه سرائی ص ۵44 ببعد - و این مهرداد پر ولن ( شم اول ودوم ) و نواده
. فرهاد چهارم بود . رك : پیرنیا . ابران باستان ج ۳ ص ۲۶۱۸ بیعد .
۸ از : میل ۱۲ ( واسطه )۲ میل (قن : سراسن » دمادم »کشاکش ).
```


## [2026-09-06T02:16:05.825Z] TOOL CALL #27: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:854 2>&1 | head -70",
 "description": "Fetch BQT page 854 (دست)"
}
```


### [2026-09-06T02:16:07.592Z] TOOL RESULT

```
no scan of BQT covers printed page 854 (see 'scans' in refs_online.json)
```


## [2026-09-06T02:16:12.510Z] TOOL CALL #28: Bash

```json
{
 "command": "cd data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if re.search(r'[۸8]۵[۳۴۵]', p[:400]) or '۸۵۴' in p:\n        print('leaf',i, repr(p[:120]))\nEOF",
 "description": "Find BQT v2 printed page 854"
}
```


### [2026-09-06T02:16:14.243Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T02:16:17.862Z] TOOL CALL #29: Bash

```json
{
 "command": "cd data/verification/sources/refs && grep -n \"دست\" BQT_v2_pages.txt | head -5 ; echo ---; python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\n# print first line of some leaves to see numbering\nfor i in range(250,262):\n    head=' '.join(pages[i].split()[:12])\n    print(i, head[:150])\nEOF",
 "description": "Inspect BQT v2 leaf headers"
}
```


### [2026-09-06T02:16:19.542Z] TOOL RESULT

```
35:‫اجات کردند وشغاهاً وکا اطلاعاتی دردسترس مصحح گذاشتند‪ .‬وماآنچهرا که‌توانستيم‬
168:‫جمع در ز بان فار سی ‪ .‬محمد معین (طرح دستور‬                             ‫‪ .‬قاعده‌های‬         ‫‪۲‬‬
402:                             ‫آن برآید ‪.‬‬          ‫وموبدان و دستوران وهیربدان شده باشد گرفته‬
483: ‫بود که درعهد طالوت بدست یغمبری کشته‌شد‪.‬‬                ‫بمعنی آوردن باشد که در مقابل بردن است ‪.‬‬
521:  ‫لهوت بطالوت ( شاژل ) حدله کرد و بدست داود‬   ‫اک‬‫جده‬‫در فرآن سور ‪ ۲‬آیهٌ ‪ ۰۵۲-۲۵۲‬آم‬
---
250 
251 ‫خوزی‬ ‫‪۱۷۱‬‬ ‫بروزن‌شولتان ؛ نم‬ ‫خورستان ‪۱‬‬ ‫غله کنند و چنان بر
252 ‫‪۳-۲‬‬ ‫خوزی خوار‬ ‫بو سه م‬ ‫و دمعمی‬ ‫هم گفته‌اند ‪۸‬‬ ‫شوهر‬
253 ‫خوشة سیهر‬ ‫‪-۷۹۳-‬‬ ‫وعم بروزن احمداگ ‪ .‬طعامی رگاوین که نمك‬ ‫خوش
254 ‫باس‬ ‫حو شی ه با نانی مجهول بوزن کوشی؛‬ ‫وفتح‌کاف فارسی ورایبی‌نقطة
255 ‫روانند که سپاهیان‬ ‫ویفتح اول‌قندیل و تیردان گ‬ ‫تالف لوام مان كف
256 ‫‪- ۷۹‬‬ ‫از شراب لملی‬ ‫خون بکطن_اب‬ ‫خون‌دل بناخن آ و ردن
257 ‫خوید‬ ‫‪۷۷‬‬ ‫ابلای‬ ‫تشدح‪۷‬ت‪-‬و‬ ‫با‬ ‫ن‬ ‫دنیهآب‬ ‫تحتالی ‪ ۰‬بمع‬ ‫خوه =
258 ‫‪۷ 6‬‬ ‫خوی درد‬ ‫‪-‬‬ ‫هم هت‬ ‫باشد ‪ - ۴‬و نمعتی
259 ‫یه‬ ‫وعربان خراطین میگوند (‪. )۲‬‬ ‫وحرف خیرمعاف دارد ‪١‬‏ ‪4 .‬‬
260 ‫—‬ ‫س‬ ‫خپله‬ ‫خهی ‪ - ۲‬بفتحاولبروزن زهی کلم‬ ‫خهله ‪ »
261 ‫سب‬ ‫ست ‪۵ ۱‬‬ ‫خر د بکسراول بروزن هیر» سر گشته‬ ‫خیتال
```


## [2026-09-06T02:16:25.417Z] TOOL CALL #30: Bash

```json
{
 "command": "cd data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(312,318):\n    print('=== leaf',i,'(printed ~',i+540,') ===')\n    print(pages[i][:1400])\nEOF",
 "description": "Print BQT v2 leaves around 854"
}
```


### [2026-09-06T02:16:27.064Z] TOOL RESULT

```
=== leaf 312 (printed ~ 852 ) ===
                                                                                                                        ‫جد‬
      ‫ح‬
      ‫ب‪ ۷‬ی‬                                                                                                           ‫درا لون‬



‫دلنواز» بمعنی زشت خوی ‪ -‬وبدلما و لا زیبا ‪-‬‬                                 ‫‪۰‬‬   ‫وقهر آ لود باشد‬       ‫ومهم ناك‬        ‫خشمگین‬

                                                                                                                 ‫~~‬
‫وخشم| لود وسهمگین ‪ -‬وخام طمعوعیب جوی‬                            ‫در | لون ‪ -‬بروزن طلا کون ‪ ۰‬تمعتی‬
‫باشد ؛ وبفتح انوفلزدرست است ؛ وبابای فارسی‬                      ‫حیف ودریغ وافوی باشد ودرمۇ‪,‬دالفضلا بهمین‬
                          ‫هم امده است ‪.‬‬
                                                                ‫ممنی بعد از واو الف نوشته بودند که دژالوان‬
‫دز براران ‪ -‬و داژتیر‌ابنابای ابجد‬                                                                                        ‫باد ‪.‬‬
‫‪ ۱‬است که بمعنی‬              ‫از‬
                             ‫رجمم‬
                                ‫بی ‪.‬‬
                                   ‫ژارس‬
                                      ‫دای ف‬
                                          ‫وب‬                ‫نظام‬    ‫فارسی‌بروزن‬       ‫ماف‬   ‫‪a‬‏‬   ‫‪۱‬‬    ‫درانگاه‬


               ‫عیب جوبان ولا‪.‬زی
=== leaf 313 (printed ~ 853 ) ===
   ‫آ‬    ‫‏‪a‬‬
  ‫دروا‬                                                                                                                                      ‫‪۳ ۵۳۳‬‬


                                        ‫وبفتح اول‌هم آمده‌است ‪.‬‬               ‫ثالیو نحتانی و ظهور ها *بمعنی «ژیهاستکه‬
                                                              ‫‪4‬‬
                                                                                   ‫بعربی‌غدد گویند ونآرا دژیدهه بفتح‌های هوز(‪)۱‬‬
 ‫دکزام ‪ °‬۔ بروزن اکرام‪ ۰ ۴‬سهمناه‬
‫وختمگن راکویند وبمعنی زاهد وپرهیز گار‬
                                                                                   ‫گهفمته‌اند ودژیبه بینزظرآمده است که بروزن‬
                                                                                                                                        ‫عجیبه باشد ‪.‬‬
             ‫سرا را نگیفزته‌اند ‪.‬‬              ‫‪-‬جه‬
                                                 ‫وا‬‫هومخهت‬
                                                              ‫‌‬                    ‫دز خم ‪ = ۱‬یکر اول و خای تقطه‌دار‬
‫امه = بکر اول؟ و فتح آخر »‬    ‫دز‬‫ک‬
‫بمعنی‌دژکام استکه سهمنالك‪ -‬وخشمگین‪ -‬وزاهد‬                                          ‫وسکون ثانی وهیمء بدخوی وبدطبیمت راگویند‬
            ‫و پرهیز گاروخواجه سرا باشد ‪.‬‬                                           ‫چه دژ بمعنی بد وخم بم‌عنی‌خوی‌وطبیمت باشفب‬

=== leaf 314 (printed ~ 854 ) ===
      ‫لیس‬
        ‫ب‪4‬‬‫‪-‬‬

 ‫دز هخت گسگه ‪ ۰ ۱‬با کاف فارسی‬                                ‫وجلافت را گوءنه ‪ -‬وبه‌عنی‌نقاهت هم‌آمده ات‬

‫واف دیگر زده ‪ ۰‬بمعنی دژهخت‬
                         ‫مفتوح بنون ک‬                                                    ‫که ازییهاری برخاستن باشد ‪۰‬‬
                                                            ‫=بفتح اوبلروزن الوان »‬                            ‫روان‬
                                                              ‫اه‬   ‫‪۱‬‬           ‫و‬         ‫‪۱‬‬      ‫ف‬       ‫‪۱‬‬     ‫‪“4‬‬       ‫‏‪EC‬‬


 ‫ذارهر ج ‪ ۲‬د بفتح الك وسکون رای‬
                                         ‫‏‪a‬‬


                                                             ‫وبکسراول‬              ‫وتأسف ودریع باشد ‪4‬‬              ‫یمه‌نی سرت‬
‫که‬    ‫کنك اس‬   ‫بی‌نقطه (‪)۴‬وجیم ‪ ۰‬یمعتی دژهخت‬
                                                                                                                   ‫نز آمده ی‬
 ‫بیت‌المقدس باد » و باين معنى بنم الث هنم‬                                                                              ‫‪4‬ھ‬




                                                                                   ‫ار کین و‬
                                                            ‫و ثالی » برختم‬               ‫بفتح اول ‪۴‬‬         ‫‪- ۲‬‬    ‫دژه‬

           ‫ومتضاله را همکوبند ‪#*.‬‬       ‫است )‪۳ (4‬‬
             
=== leaf 315 (printed ~ 855 ) ===
 ‫دستاران‬                                                                                           ‫‪-‬وو ارات‬

 ‫هست ‪ -‬وفتح و نصرت وفیروزی ‪ -‬و فرصت ‪ | -‬لومسند همچنان که اسب را سر وشتررا لوففریل‬
‫ودمعتی اندازه‪.‬‬  ‫را ز اسر "‪ ۳‬و ‪.‬مع‌تی ىك عدد ‪-‬‬ ‫وظفر بافتن را نگیفزته‌اند ‪ -‬وصدر ومسند ماش‬
‫و بکبار باختن قمار‪ -‬وبازی سه تیر ‪ -‬و بمعنی‬                                       ‫وسلاطین و اکابر باشد ‪ -‬وقوت‬
                   ‫‪۰‬‬   ‫است‬     ‫هم و‬           ‫و ده‬   ‫حرفت‬
                                                                                 ‫وقدرت و توانابی‌را نیز گویند‪-‬‬
‫بروزن پتا‪ .‬مخفف وعرخم‬
            ‫ورء ياك باشد ‪۳‬‬      ‫که مادیل‬
                                            ‫دستا ‪۱‬‬
                                                  ‫ات‬    ‫دار‬
                                                                                 ‫و لاء چیز تمام راهم میگوبند‬
                                                                                ‫همچو بکذست رخت ممنی از‬
‫دست بدرجسنت اساتتبرجکهن ‪ -۴‬بنتح‌همزه‪,‬بسنی‬
        ‫‪2‬‬

‫دة زنان باشد و آن‬
                       ‫‪۳۲‬‬       ‫‪۳‬‬             ‫‪۳‬‬
                                                                                 ‫مندیل تاشلوار وسکدست سلاح‬

 ‫دست‬   ‫‪1‬ن که در‬    ‫وامال‬      ‫مبلی نود از طلا ونعره‬                    ‫دست‬       ‫که ازخود تا موزه آهنی باشد‬
   
=== leaf 316 (printed ~ 856 ) ===
    ‫س‬‫ای‬                                                                                              ‫دستاربندان‬
 ‫از رقاصی‬    ‫افغاندن = کنانه‬              ‫دست‬                ‫ویمعنی شگاردانه ومژد گانی‌هم آ هده است (‪.)۱‬‬
 ‫کردن ‪ -‬وآشکارا ساختن باشد ‪ -‬وابا نمودن ‪-‬‬
                                                             ‫«ابه‌ازسادات وصدور‬
                                                                              ‫دستار بند ان کن‬
                 ‫وترك دادن چیزها را نیز گوینه ‪۱‬‬
                                                             ‫وتبا وعلماوقنات وفطلا (‪ )۲‬ومفتیان ودروشان‬
 ‫دست اقگی» با كاف بر وزن دستك‬                               ‫و امتال ایشان باشد » و بعربی ارباب العمائم‬
 ‫»نایه از خادم و خدمتکار باشد ‪ -‬و عاجز‬
                                     ‫زن ک‬                                                                  ‫خوائند ‪.‬‬
 ‫و اتوانرا نیز کویند ‪ -‬وبمعنی پاکار هم آمد‪.‬‬                  ‫دستار جه = بروژن سکیارچه‪ .‬روپاك‬
                                                   ‫اس‬
                                                            ‫ودستمال رکاوبند ‪ -‬وپارچه را نگیفزته اند که‬
‫دست ]موز ‪ -‬مرفی را کوبند که‬                                  ‫برسر نیزه و علم بندند و آنرا طره و شقه هم‬
                ‫بپرد وبرود وباز بگرشته بیاید ‪.‬‬                                                             ‫خوانند ‪.‬‬

        
=== leaf 317 (printed ~ 857 ) ===
  ‫برد‬   ‫دست‬                                                                                              ‫س‬
                                                                                                         ‫وی‬‫‪۲۷‬‬


‫بی حاب ‪.‬باشد ‪ -‬و ذخصی را نیز گوبند که در‬                ‫دہ ت اند از ست تعدی وحوالهٌبی‌حساب‬

  ‫متانرا‬
       ‫هدس‬
         ‫نیدکه‌‬
              ‫ه‌ا‬
                ‫نهره‬
                   ‫دبهر آ لتیوم‬
                              ‫شوطنررنج‬                  ‫راگوند ‪ -‬وکنابها زرقاس‪ -‬وشناورت وکیسه‌بر۔‬
                                      ‫بازی کند ‪.‬‬        ‫وتبرانداز را نیز گومتب‬        ‫وتاراج باشد ‪۳‬‬          ‫وعارت‬


‫دست پاك ه کنابه از دست خالی‬                             ‫صنر‬   ‫وشخصکه‬         ‫زند‬   ‫د که ویهلویکسی‬       ‫وکسکه‬


                                                        ‫لت نمعئی صدر و سند‬             ‫اند خه‬          ‫یگ‬       ‫و‬
 ‫وفظر و مسکنت ‪ -‬وپرهیز کار و متدین باشد ‪-‬‬
                       ‫ودستمال را نز کویاد ‪. ۵‬‬                                            ‫‪۰‬‬   ‫‪۱‬‬    ‫عم مده است‬



 ‫دست بد ند‌ان کندن د ر دست‬                              ‫دستان رند ‪ ۲‬د بزاای هوز بروزن‬
‫بدندان گر هدن‪ .‬کنا‪:‬ه ازحصرت وندامت وتاسف‬

          ‫|‬                ‫خوردن و رشیمانی باشد ‪.‬‬       ‫رستم باشد‪ .‬گوبند زال را سیمرغ این نام نهاده‬
 ‫دست بر آوددن د کنابه از دا‬
```


## [2026-09-06T02:16:32.897Z] TOOL CALL #31: Bash

```json
{
 "command": "cd data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (314,315):\n    print('=== leaf',i,'FULL ===')\n    print(pages[i][1000:])\nEOF",
 "description": "Print full BQT leaves 314-315"
}
```


### [2026-09-06T02:16:34.856Z] TOOL RESULT

```
=== leaf 314 FULL ===
ى بنم الث هنم‬                                                                              ‫‪4‬ھ‬




                                                                                   ‫ار کین و‬
                                                            ‫و ثالی » برختم‬               ‫بفتح اول ‪۴‬‬         ‫‪- ۲‬‬    ‫دژه‬

           ‫ومتضاله را همکوبند ‪#*.‬‬       ‫است )‪۳ (4‬‬
                                         ‫‏‪a‬‬                                                                                   ‫أت‬
 ‫‪ -‬بر وزن می‌دوخت »‬           ‫تو*‬
                                ‫سه‬‫دز‬
     ‫بمعئی دزهرج ‪ ۷‬اعت که ببت‌آلمقدی باشف ‪.‬‬

                                                         ‫)<( ‪ 0‬قبلة‬                ‫تای فرشت‬         ‫تخد (‪ )۱‬و‬          ‫ای‬    ‫ثالی و‬


 ‫کنك است که قبلةٌ پیشینیان و بیت‌المقدی‬                     ‫پیشینیان باشد و آنرا بریانی ایلیا © و بعربی‬
                                              ‫باشتد ‪.‬‬



                                                 ‫بیان نهم‬


 ‫مخفف دیس هم حت که شبیه ونظیراست ‪٩‬‏ ‪-‬‬                     ‫دس = بفتح اول وسکون انی» بمعنی‬
‫ده را کوبند *‪ ۱‬که‌بعریی عشره‬      ‫عدد‬     ‫و بهندی‬
                                                         ‫عنی آن هم‬     ‫ی ‪٩‬م‏‪-‬‬
                                                                            ‫وشد‬
                                                                              ‫شبیه و ثیر ومانند با‬
                                      ‫خواند ‪.‬‏‬           ‫هم هت کهلمة اشاره است ‪ -‬و بضم اول گل‬
‫است‬       ‫قق‬    ‫خم‬         ‫ن‬        ‫دست‬
                                                          ‫ول پخته لآیمزبدنظهر‌است‬‫سخت راکویند ‪ ,‬ک‬
‫بمعنی فایده و نفع هم‬   ‫و‬    ‫و بعربی بد کویند ‪-‬‬            ‫اة اعلم > وبکراول بیوتالی بمعئی‌هندسه باشلب‬


                ‫وسکون را‪۰ ‎‬‬   ‫(‪ )e‬چك‪:‬‬                   ‫(‪ )۲‬چك ‪ :‬وتا‬                           ‫وخا ‪۳‬‬   ‫جڃك‪:‬‬       ‫(‬


                                                                                          ‫‪E‬‏‬           ‫)‪ (£‬وك‬


                       ‫)‪.‬‬     ‫از‪ :‬دژ ( هم‪ ) .‬ط هو( بت‬                      ‫‪۴‬‬                  ‫رك‪ :‬دزمان ‪۰‬‬     ‫=‬    ‫‪۱‬‬

                     ‫‪ .‬رك‪ :‬دژ هشت كنك ‪.‬‬             ‫رژهوخت‬     ‫=‬       ‫‪۳‬‬                     ‫‪ - ۴‬لفة بضم اول‬
  ‫«رژهوخ» مخفف‬        ‫صحف‬
                        ‫م‪-‬‬‫‪۲‬‬                     ‫‪۰‬‬   ‫دژهشت‬    ‫رك‪:‬‬           ‫‪۹‬‬              ‫‪.‬‬     ‫‪:‬ا‬
                                                                                                 ‫لی‬‫انرك‬
                                                                                                      ‫‪۵‬‬
      ‫‪.‬‬   ‫دژهوخت ‪ .‬رك ‪ :‬دژهشت‬     ‫=‬      ‫‪۸‬‬              ‫ورك‪ :‬دزهر ج(‪)۱‬‬               ‫‪۰‬‬   ‫‪ . ۴‬رك ‪ ۳‬درهخت‬            ‫» دزهوخت‬

     ‫سا_نىكرىت‬
             ‫‪°‬‬                      ‫(ھ‪.‬م‪» (.‬رك ‪ :‬صله دىداچة مولف‬                         ‫دس“‬         ‫ففف‬

  ‫‪ _ ۱‬بهلوی ‪ “ 521‬يارسى باستان ‪« 4541 -‬بارتولمه‬         ‫« ورایامز ‪. ۰ ۳: ۱۷1‬‬                                                 ‫‪2‬‬
  ‫‪,‬ردی ‪ » 56‬بلوچی‬  ‫‪, 6‬یب رگ ‪٩4‬‏ ‪. » ۰۵-‬اوستا ‪ » 21582 -‬هندی باستان_‪ 21540‬ک‬                                                   ‫‪۵‬‬
  ‫‪ .‬وخی ‪ , 052110‬شغنی ‪ » 0560۳4‬سریکلی ‪45‬لا‪ , 01‬منکلیچی ‪ 4521‬منجی ‪۰ 4521‬‬                                                        ‫‪0‬‬
  ‫بقیه در صفحهٌ ‪۵۵۸‬‬

 ‫(برهان فاطع ‪)۳۱۱‬‬

=== leaf 315 FULL ===
چو بکذست رخت ممنی از‬
‫دست بدرجسنت اساتتبرجکهن ‪ -۴‬بنتح‌همزه‪,‬بسنی‬
        ‫‪2‬‬

‫دة زنان باشد و آن‬
                       ‫‪۳۲‬‬       ‫‪۳‬‬             ‫‪۳‬‬
                                                                                 ‫مندیل تاشلوار وسکدست سلاح‬

 ‫دست‬   ‫‪1‬ن که در‬    ‫وامال‬      ‫مبلی نود از طلا ونعره‬                    ‫دست‬       ‫که ازخود تا موزه آهنی باشد‬
                                                                  ‫وبك دست خانه کهازشمن وخوایگاه نا طویله‬
‫بفتح دال ابجد (‪)۲‬‬             ‫د ستاد ست ‪۴‬‬                          ‫باشد‪ -‬وهرچیز که اجتماعی درآن امرلازم بود‪-‬‬
                                                                  ‫وبمعنی بکدست هم هست که بمعنی برابر باشد‬
‫وسکون سین سعقص و تای قرشت (‪ » )۳‬بمعنی‬
‫سودای نقدانقدباشد؟ یعنی چیزی‌بگیر ندوهمان‬                          ‫همچو بکطرز وبکروش وبك قم و يك جنس‬
                                                                  ‫وبك بات وامثال آن ‪ -‬و بمعنی اعده و قانون‬
                                ‫لحظه قیمت بدهند ‪.‬‬
                                                                   ‫وطرزوروش‌هم بنظرآمده است ‪ -‬و کرت ومرنبه‬
‫رفتار ‪ .‬مندیل وروياك‬        ‫بروزن‬       ‫=‬    ‫دبتار‬            ‫‪0‬‬
                                                                  ‫ولوت‌رانیز گفتهاندهمچوبکدست دیگر شطرنج(‪)۱‬‬

                                                                   ‫وبك دست دهگراردبازی کنید ‪ -‬وبممنی دستور‬
 ‫دستار ان ‪ -‬بر وزن زرداران ا»جرت‬                                  ‫باشد ‪ -‬و مرغان شکاری مئل‬      ‫ر‬‫که‬
                                                                                                  ‫زتب‬
                                                                                                    ‫و هس‬
                                                                                                       ‫هم‬
 ‫ومزدی باشد که یش ازکار کردن ممز دور دهد‬                           ‫باز وباشه و چرغ وشاهین را نیز باعتباری دست‬

  ‫(‪ )۳‬جك ‪ :‬وسکون سن وت ‪.‬‬                             ‫(‪ )۱۷‬چك ‪ - :‬اند ‪.‬‬           ‫(‪ )۱‬چش ‪ :‬شطرلج‪.‬‬
  ‫رك ‪ :‬دست اوراجن‪ ,‬دست برجن » دست برلسن » برای‬                            ‫‪۴‬‬        ‫‪.‬‬   ‫ار‬
                                                                                        ‫ت‪:‬‬‫دمرك‬
                                                                                             ‫‪۱‬‬
  ‫‪ - ۴‬از‪ :‬دست ‪( ۲-۱‬واسطه) ‪+‬‬                            ‫جن » اجبرين » اورنجن » اورنجین ‪.‬‬
                                                                                      ‫جزو دوم » رك ‪ :‬انبر‬
   ‫‪+‬‬   ‫از ‪ :‬دست‬        ‫‪۵‬‬                ‫‪.‬‬    ‫(اه)‬      ‫‪ - ۴‬برابر پشادست (سلم ) و پادست‬                ‫‪.‬‬   ‫دست‬

                                                                                             ‫)‪:‬‬   ‫ار ( يوند‬

       ‫بجز دراعه و دستار ونقش روش ‪.‬‬                                      ‫بآدمی وان گفت ماند این‌حیوان‬
  ‫«گلتان ‪.* ۲۱۱‬‬
                  ‫دست آورنده ‪.‬‬               ‫‪ - ۴‬عنی اسم فاعل =‬               ‫‪ - ۷‬یمثی دست بباور ‪-‬‬

                                                                                           ‫بقبه از صفحهٌ ‪6۵۸‬‬
  ‫بودغا ‪« 501‬اسشق ‪ , ۷۹۵۶‬ارمنیع ‪( 630520‬مفصل ‪ .‬بند)‪ .‬اففانی ‪( 20520‬دسته) «هوبشمان‬
  ‫«ربرسن ‪ , ۸۲۰‬اورامانی ‪* 5620‬ك‪ .‬اورامان‬
                                       ‫انکاشمی كلا و ‪ . 500‬زباکی ‪ 6520‬گ‬                                   ‫‪۷‬‬
   ‫‪ , ۰‬گیلکی ‪ , 058‬فبرزندی ‪ .‬برنیء‪:‬نطنزی ‪۱ ۰4 520‬ص ‪ ۰۰ ۹۸۲‬سمنانی» سنگری‬
   ‫ولاسگردی ]‪ , 520‬شهمیرزادی ‪ , 521‬سرخه‌بی ‪۲. ۰2 4520‬ص ‪ .» ۹۸۱‬دزفولی ‪ .524‬معرب‬
                                    ‫‪۰‬‬       ‫آن فز «دست» برای معانی آن درغر بی رك‪ :‬دزی حاص ‪06-۱44‬‬
                                                       ‫‪ ۶#‬رژهوخت ‪ -‬رك‪ :‬دژهخت ودژهخت گنگ ‪.‬‬
                              ‫‪#‬سالیر ‪ -‬بفتح اول » رك‪ :‬ص‌بنجاه و دو ‪ -‬پنجاه ونه مقدمه ‪.‬‬
                                                                                     ‫و‬
```


## [2026-09-06T02:16:48.831Z] TOOL CALL #32: Bash

```json
{
 "command": "cd data/verification/sources/refs && grep -n -i \"astin\\|āstīn\\|dastāna\\|dastana\\|sleeve\" AHM.txt | head -20",
 "description": "Grep Gershevitch for sleeve/astin"
}
```


### [2026-09-06T02:16:48.890Z] TOOL RESULT

```
520:Younger Avestan Zoroastrianism to two, monotheistic (viz. ZarathuStrian) and pantheistic Mazdahism, enables us ta redefine the term daéva. It always seemed a contradiction in terms that Zoroastrian hymns to Mithra, Anahita, etc., expressed strong dis- like of daévas, when one might well suspect that these divinities themselves were counted as daévas by ZarathuStra. The obvious answer is that they were not. But, in that case, which gods are daévas? Presumably those who were rejected as evil by pantheistic _ Mazdahians from the time when they were still *Vourunians. That it should be a prerogative of worshippers of the ahura *Vouruna and the gods with whom he was associated to detest the gods of the daéva class is only natural, seeing that the Vedic Varuna is the chief dsura. ZarathuStra, who by means of the “ridge of Truth’ had recognized Ahura Mazdah in *Vouruna (see above, p. 43), could hardly hel sharing with *Vouruna-worshippers the detesta- tion of the anti-*Vourunian da&vas. These were therefore equally disliked ‘yy Zarathu&trians and the non-Zarathuatrian pantheists whom the ZarathuStrians absorbed in about 430 3.c., following, according to our theory, the Achaemenian religious pattern of the time. Hence, in all likelihood, that pattern alsa excluded the daévas from worshi); Xerxes’ prohibition of their cult seems to have had a lasting effect. However, on the fringe of the two all-pervading Mazdih cults, the monotheistic and the pantheistic, the prapitiatory worship of da&vas continued to exist, as Zaehner, Zurvan, 14 s97., has aptly pointed out; we shall revert to this subject below, py. 63 sq.
1039:tim ta? frastindayehi®
1130:97. from whom the Fiendish Spirit, very deadly, recoils in fear, fram whom malignant Wrath, his body forfeited, recoils in fear, from whom long-handed Procrastination? recoils in fear, fram whom all supernatural evil gods, and the concupiscent owners of Falsehood, recoil in
1288:134. now it is the Fiendish Spirit, very deadly, who recoils in fear, now malignant Wrath, his body forfeited, now long-handed Procrastination; now recoil in fear all supernatural evil gods and the concupiscent owners of Falsehood (, all of them erying):?
1547:§ Viz. the time af the atone out af which Saslan was to de born after a period af ‘pregnancy’ lasting nine months.
1978:There is a different *zus-, from which Morgenstierne derived Sanglechi 2d! (ete.} ‘sleeve’, see IZFL, 11, 424, This can Se recognized in Av. 2usa in the Frahang t oim (‘jewel’ according to Bth.), and in Av. frazuf-, epithet of aSfa- ‘gaat’ in Yet 5.126 (quoted note 124%), which is generally thought to mean ‘precious’, As Skt. pra-hasta means ‘long-handed’, cf, Wn., 11, 1, 234, 89 fra- sus- could mean ‘long-sleeved’; cf. A. Waag, Nirangistan, 134, who souzht in aka- a coat with long sleeves. The Pahl. transl. of frazug-, which also accurs in N, looks like fre sew’stk, that of susa in F like xwstwk. Bearing in mind Yidya avldsta ‘sleeve’ < *uda-dasta- (Morz., TFL, 1, 194), and the Pahl. word which Nyberg reads *gpasast and translates ‘Handschutz' (idfsduch des Pehlevi, 1, >. x1), one might read *’wstn% instead of Pahl. xwsiwk, and, with a slight emendation, *wystk instead of xw’sth. *wyst- and ’wst- could represent un older *abi-sta-, amplified by -ka~ and -na-ka- respectively, "Ihe develagment will be as in *abi-stdla-> MPers. *wyst’d> Neers. gsta3, usta3 ‘teacher’, or *ai-stana- > MPers. *wyst’m, Arm. estan, > Pers.-Ar. ustan ‘province’, see Henning, ZI, IX, 195, 224 sg. As to *abista(na)ka-, this may be a reduction of *a37-d(2)sta- (za)ka-, comparable to that which according to H. W. Bailey (personal com- munication) took glace in Oss. fiston, Diz. festone ‘handle’ < *sati-dastanae, cf. Khot. dastgnya ‘handle’, Asia Major, n.3,, 1, 32 (48.1). Perhaps NPers. aszfn ‘sleeve’ similarly goes Yack to *d-d(a)st-. As to zuf in Ye 5.7 Ufa srira zug sispata urvaiti basu.staoyehi) one would agree with 3th, that it ought to be an epithet of Anahita in the nom. sing., if one did nat thereby have to attribute to the goddess also the strange epithet ‘stouter than the arm’, which is scarcely explained by the assumption that Anghita is here a river. The epithet would, however, suit wide sleeves, and the ending -i may be of the neuter dual. Has then zus replaced an earlier zusi, possibly because an attridute of Anadhita, srira. ans ‘having Seautiful sleeves’, was sought in this line? If so, translate ‘she, the beautiful, shows off her flowing sleeves which are armpler than her arms’, the comparative deriving its point from the earlier description of Anahita’s arms as being ‘stauter than horses’ (asd. staayehis).
2194:97°. The explanation of Baiygsta- as ‘procrastination’ was first pro- posed by Wi. in his commentary to this passage. It was repeated by 3th. in KZ, 29 (1838), p. 547, n. 2, and Benv. in Rev. hist. reliz. 139 (1945), 16.
2210:tor. Wo.: ‘an sie verteilt er, (der) die Herrschaft fibrt, gleichmi3ig (seine)...Pfeile. Und wenn er fahrend dahin kommt, wo die mi9ra- feindlichen Lander (liegen), schmettert der als erster die Keule auf RoB und Mann nieder’. Lo.: ‘auf jene (Mithra-feindlichen Valker) schleudert (comparing Ved. ava-dhy, abht-Sra-bhr) er—(denn) er vermag es—auf einmal seine... Pfeile, dann, wenn er dorthin geht, wo die m. Volker sind; er als erster schleudert...’, Wa.’s translation agrees with Spi.’s and Da.’s; the other translators take avi.di¥ to mean ‘against them’, in support of which interpretation Gdn. refers to st. 37. But on the one hand what precedes avi.dzi are Mithra’s assistants, not his opponents, on the other hand the very use of av1-hara- in st. 37 (where Lo. translates ‘bringt er auf sie’) goes against Lo.’s interpretation of this verd as ‘schleudern’ in the present case. The stanza is therefore best under- stoad as contrasting the fighting weapan used by Mithra with thase he distributes among his assistants.
2370:Opinion thus differs on the meaning of 797d, and the value of the second component of satdyus, etc. On the first point, seeing that up to hazanra@s the partics concerned are always twa, it seems obvious that mio here stands for ‘contract’; those who deny this have the obligation, as yet unfulfilled, of producing strong proof to the contrary. In the case of the ten-thousandfold contract of the Mazdayasnian Religion the can- tracting parties can safely e held to be the Religion on the ane hand, and each of the faithful on the other. As regards the second paint it is unlikely that numeral adjectives of different function should have been used in dassing from ninety ta higher figures. I see no objection to assuming that satdyu-, etc., contain ayu- ‘duration’ (cf. Lo.’s translation, and Duch., Com. 177), Yut would conclude from the present passage that ‘lasting one hundred’ had come to 5e used in the sense of ‘hundredfold’.
2410:124", Bth, took vavazanam as an ‘adsolutive’, ‘beim Fahren, Yeim Lenken (des Wagens)’, comparing vavhanom in Yt 5.126: aradvi siira anihita...frazusam a3kam vanhinam pouru.paxstam zaranaznam. Here one may prefer to assume that an original *vawhdna, nom. sg. fem. of the pres. participle middle of vah-, was changed to °nam under the influence of the surrounding masc. accusatives: ‘Arodvi Sira Andhita, ... wearing a long-sleeved (see adove, >. 220, n.}, much-embroidered, golden coat’. As to vavazana-, it is best regarded as a regular shortening of *vavazana- (see note 103!, first para.), an adjectival intensive middle perfect participle of vaz-, comparable to OInd. vavasand, vavasand, etc.,
3080:*abi-dasta(ua)-, 220 n. *dvya-, 200 0. *apavant-, 201 *cam-, 184 *dug-gva-, 230 *havya-, 200 n. *7i(va)Ora-, 260 *lakata-, 182 n. *ndxar|n-, °aka-, 277 *niba-, 282 *pati-dastana-, 220 n. *pati-mauga-, 203 *pitt-, 231
```


## [2026-09-06T02:16:49.586Z] TOOL CALL #33: Bash

```json
{
 "command": "cd data/verification/sources/refs && echo ==HRN==; grep -n -i \"āstīn\\|astin\\|Ärmel\" HRN.txt | head -20; echo ==HUB==; grep -n -i \"astin\\|Ärmel\" HUB.txt | head -20",
 "description": "Horn/Hübschmann astin"
}
```


### [2026-09-06T02:16:49.648Z] TOOL RESULT

```
Exit code 1
(eval):1: =HRN== not found
```


## [2026-09-06T02:16:59.558Z] TOOL CALL #34: Bash

```json
{
 "command": "cd data/verification/sources/refs && echo \"==HRN astin==\"; grep -n \"stin\\|Ärmel\\|Aermel\" HRN.txt | head -20",
 "description": "Horn astin/sleeve"
}
```


### [2026-09-06T02:16:59.610Z] TOOL RESULT

```
==HRN astin==
1172:stT' in stinik (vd. 5 (38), aw. ereöwa-) ^b^%stm 'aufrecht
1263:kurd. vergl. ci]rüstin 'leuchten', dici\rüsi (3. Sg.).
2159:kurd. birzdndin (H.-Sch.), braztin, LW. beristin *braten,
2296:kurd. bastin, bandim; oss. d. battun, t. bäffin (59);
2954:kurd. pärlstin, dispärise 'ist enthaltsam, enthält sich*.
3034:(vd. 15 (26) 61.); ai. stdna-; arm. stin (H. No. 259).
3170:skr. püyati (Brahm., Sütr.), ai. piiti- *faul, stinkend'.
3784:') Vielleicht zu emendiren in törak', Justins Polemik (Bund. s. v.)
4280:/'td'iiw ai. Ytriji. >cj*iiid' Selbst I-Hrstininiung'.
5185:*) Np. dend ist wohl nur eine repristinirte Form,
6790:phlv. sustan, söyBnd^ söy(i)sn; kurd. LW. sustin
6791:'waschen' (vergl. g. sustinUu neben sustmün) ; bei.
6846:des Erdteils, die Euphratländer, Persien, Palästina
6892:kurd. LW. sikestin, sikinändin (Causat.); oss. sädfjn,
7406:karkatas 'Geier scheint nach aw. kahrkatas- repristinirt
7454:kurd. LW. (?) kustin 'tödton*; bei. L\V. (?) kuäag,
7625:•) Repristinirt auf Inschriften in Indien, Hörn, Epigraphia in-
8099:934. yend 'Gestank', gmda stinkend', gendah 'Pfuhl*, gend-
8116:stinkend*, gandakth ; ai. gandhd- *Geruch, Duft (wohl-
8118:af}'. ganda 'stinkend'; bei. LW. gand 'Kot, Mist'
```


## [2026-09-06T02:17:00.322Z] TOOL CALL #35: Bash

```json
{
 "command": "cd data/verification/sources/refs && echo \"==HUB==\"; grep -n \"stin\\|Ärmel\\|Aermel\\|dast\" HUB.txt | head -30",
 "description": "Hübschmann astin/dast"
}
```


### [2026-09-06T02:17:00.387Z] TOOL RESULT

```
==HUB==
373:skr. avasthita 'dastehend, verbleibend, bestandig' etc.
393:gewiesene phi. st^n, stinik 'stehend* ist auflfallend.'*) Auch
838:189. Fiir *avatasti' wiirde ich *ddast, tnr *abitasti- : *awdast,
839:audast erwarten.
994:riickzufiihren.^) Vgl. biskofa ^^ phi. viskofak, bidast r=
1358:'abstinence* GI. and Ind. 88, *Vorsicht* Yatk. i. Zar.
1756:433. Np. ^aSt, dasta, daStl Trahstiick', phi. dast morning
2185:Anm. bemerkt. Dazu arm. LW. dastak 'Handwurzel'
2186:(np. dasta 'Handvoll, Griflf), afgh. dasta f. a handle*.
2187:508. Die Etymologie von dastilr 'Vorschrift', paz. dastur
2192:sie audi dSfig in dEng patOis und dB durch dastvar,
2195:durch regie' (Zend-Avesta I, p. 299). Np. dastan
2248:*) VgL afgh. LW. las = np. dast *Hand*.— 65 -
3186:paz. gazldan *to bite, sting, gazd(u)m 'Scorpion Gl.
3215:ist Causativum zu gudastan Voriibergehen , vorbei-
3340:ganda 'stinkend' finde ich nicht bei Raverty.
3381:952. Np. Idf Trahlerei' (afgh. LW. Ictfa, lapa f. 'boasting,
3665:1067. Dazu afgh. LW. nes 'the sting of any venomous
4319:dadistdn 'Urtheil' = paz. dadastan. phi. datastan, arm. da-
4470:des folgenden y) ; dadistan 'Urtheir = paz. dadastan, u. s. w. ;
4535:arm. aSakert 'Schiller* — np. sagird; arm. dastakert *An-
4536:siedelung* = mp. AaatayB()d, arab. dastajird oder daskara
4772:risk *Nisse' = skr. liksd-; bidast *Spanne' = skr. vitasti-;
4963:aussen, heraus* (s. oben p. 33), pindastan 'dafiir halten' ^^
5491:plain , vazaresn 'distinction, release* Shk. 272, phi. v(i)dartan
5547:zu gu-) : bidast, gidast *Spanne' = zd. vitasti- ; gustax *frech'
5592:(Sebeos 24) = phi. Veh-Artaslr, np. Beh-Ardastr (Seleu-
5752:= phi. gukarak 'digesting Shk. 246, np. guvara, da gu^
6011:ganjur (skr. ganjavara-), dastUr = paz. dastur,
6012:phi. dastuvar; muzdur, afgh. LW. mazdUr =
```


## [2026-09-06T02:17:08.611Z] TOOL CALL #36: Bash

```json
{
 "command": "cd data/verification/sources/refs && grep -n \"dast 'Hand\\|dast \\*Hand\\|hazär\\|hazar 'tausend\\|hazär 'tausend\" HRN.txt | head -20; echo \"=== HRN dast entries ===\"; grep -n \"^[0-9]*\\.\\s*dast\\|\\bdast\\b\" HRN.txt | head -20",
 "description": "Horn dast/hazar"
}
```


### [2026-09-06T02:17:08.681Z] TOOL RESULT

```
9445:aw. hazatlra- 'tausend'; phlv. ha zur, hazärak
=== HRN dast entries ===
5105:ap. dasta- Hand'; aw. zasta-; phlv. dast; ai. hdsta-.
5107:ter, LXIII, Npte) , dast; bei. dast (51); wa;^. ^ast,
5108:siyn. döst, sar. düst, sangl. dast, minj. last, yidg. lust.
5124:aw. da/stavaitl-; phlv. dastän (arm. LW. dasfan;
8315:dastän[marz, dösak[marz vd. 1 (18), marz(i)sn, 'Coitus*
```


## [2026-09-06T02:17:11.064Z] TOOL CALL #37: Bash

```json
{
 "command": "cd data/verification/sources/refs && sed -n '5095,5130p' HRN.txt; echo \"=== hazar ===\"; sed -n '9435,9460p' HRN.txt",
 "description": "Horn dast and hazar entries"
}
```


### [2026-09-06T02:17:11.136Z] TOOL RESULT

```
Mit duZ'j dtiS' gebildete Composita, deren Zu-
sammensetzung vollständig durchsichtig ist, wie
duz/lm, dmnüm, dmmen sind im Folgenden nicht
aufgeführt.
560. deSe ^Siegel*.
aw. i^daJ/Z', dazaiti Verbrennen'; phlv. dazitan; ai.
[/dali- ddhatl 'brennen, verbrennen',
bei. n. diday, pp. da/fa 'brandmarken' (433).
507. dest 'ITand', vergl. destek^ deste (arab. dastaj ^)), destl
'Hilfe'.
ap. dasta- Hand'; aw. zasta-; phlv. dast; ai. hdsta-.
Allgemein entlehnt: kurd. dest; afy. las (Darmeste-
ter, LXIII, Npte) , dast; bei. dast (51); wa;^. ^ast,
siyn. döst, sar. düst, sangl. dast, minj. last, yidg. lust.
508. destur 'Minister, Vertrauter; Verhaltungsmassregel,
Vorschrift'.
') (^Iml.l. LW. pppi, arm. LW. (htsfnk.- 127 -
ap. "^dastabara-; phlv. dastwar, dastbar.
Nicht zu dest *Hand\ sondern zu der in aw. dqsfva-
etc. steckenden Wurzel dmts- (Darmestetor, Et. ir.
I, 115 Note)'). Zu derselben Wurzel stellt Nöldeke
(mündliche Mitteilung) auch np. dästan-), destan *Go-
schichte, Erzählung .
5()9. duH^^är, duSvär 'schwierig*, dus/'ün, dusvan,
aw. vergl. duzadra- (Geldner, KZ. 25, 478, Studien
I, 17 folgg.); phlv. dus/J'är, dmx'arlh.
Die neup. phlv. Formen sind Neubildungen aus
dus+x"^'^ (No. 49G).
570. destän 'menstruirende Frau'.
aw. da/stavaitl-; phlv. dastän (arm. LW. dasfan;
chald. LW. ]P\'^'^)j dastan(i)stan^ vorgl. dayßak,
571. dil *Herz', diler (reimt auf ser, Sahn. I, 195, 1194).
aw. zered- (y. :n, 12), zaredaya- *lIorz*; phlv. dil,
päz. diler (Men.); ai. hfd-, hfdaya-; arm. sirf (IT.
No. 250).
kurd. zar 'Herz*; af/. zra; oss. d. zärdd^ t. z'ardä
=== hazar ===
Sollten die germanischen Worte, etwa durch
türkische Verniittelung (wo ich ein hurrä aber nicht
nachweisen kann), aus dem Persischen entlehnt sein ?
\ }(^92. hergiz jemals, je*, mit Negation 'niemals'.
ap. Vmkaramöiy *ein Mal' (Darmesteter, Et. ir.
I, 245 ; unsicher) ; phlv. akarc bezw. hakaix, luxharj,
phlv.-päz. hargij bezw. hargiz (PPGl.), püz. hargizi.
Np. hergiz gegen phlv. hakarc ist wohl durch her
beeinflusst.
i '1093. hezär 'tausend'.
aw. hazatlra- 'tausend'; phlv. ha zur, hazärak
'Millennium' , vergl. a^apanursTg' oi staayysXsTc nngd
üspaaig Hesych, arm. LW. hazarapet {/Mag/og,
oiaovo/iiog^ enirpoTrog); ai. sahdsra-,
af/. zar 'tausend*; LW. arm. hazar^ kurd. hazdr
etc.
1093**^^ hii^tr, hujir, yujlr 'schön', auch N. pr. (Sahn. III,
1191 Vers 985; 1239 Vers 1927; 1240 Vers 1936;
1503 Vers 127 u. ö. im DaqiqTstück).
aw. huci&ra-; phlv. hucihr.
Nöldeke, ZDMG. 46, 137.mi
245 —
)94. hest 'er ist, existirt', hestl *Sein, Existenz'.
liest ist ursprünglich nur ein aspirirtes est —
nach der 3. Plur., ap. Iia(n)tiy etc. — (vergl. jüd.-
pers. DPI neben em oben unter No. 107), das
```


## [2026-09-06T02:17:16.112Z] TOOL CALL #38: Bash

```json
{
 "command": "cd data/verification/sources/refs && grep -n \"hand\" SOD_pages.txt | grep -in \"8st\\|dst\\|δst\" | head -20; echo ===; grep -n \"^[0-9]* *[δd8]st \" SOD_pages.txt | head -20",
 "description": "Gharib Sogdian dst"
}
```


### [2026-09-06T02:17:16.181Z] TOOL RESULT

```
Exit code 1
17:14134:      handtowel                                                 3653 dstwb'ry C
(eval):1: == not found
```


## [2026-09-06T02:17:18.511Z] TOOL CALL #39: Bash

```json
{
 "command": "cd data/verification/sources/refs && grep -n \"dst\" SOD_pages.txt | head -30",
 "description": "Gharib dst entries"
}
```


### [2026-09-06T02:17:18.576Z] TOOL RESULT

```
2521:   The longest Buddhist Sogdian text is a version of               lately translated into Persian: B. Gharib, Ddstdn-e
7951:      TSP 2.235 n pi 72; Hen. Texts. 734; Bailey. Asica.            armc ? © A v. aerime-, Oss. armdst
8045:                                                                        *artaxwdst    ^'rtxwst, Jrtyw rwc, 'rtywst rwc
8121:1503 Ytwspy*     M =» >rt,wspy,h                                       221nl, drwdst
14119:                                                                      5astpare (dstb'ry)
14123:       TSP 2.333, 9.32; BSTii 897, 87; C2, 55R 27; MSP                  pi. dst&ryu C2, 60V 29
14124:         b36 cl6? GMS 1331; Ssmykw* MSP bl24                    3648 dstb'ry C =» 8stJ3'ry
14126:      Sasme/T                                                   3650 dstbr =* Sstpry
14128:       BSTBL, Dhu. 231, 264, Wmy, 269, 10smy; GMS                    Sast-Pare (dstbr)
14134:      handtowel                                                 3653 dstwb'ry C
14140:      8ast- (dst) <D<OP dasta- ©nom.; ob. -y; ace.                      57V 20 p52-5R
14145:     GMS 364, 516, 1171, 1179, 1183-4, Sstwfir-                       Hen. BSOAS 11, 65; GMS 1131 n 1; dst fir, Frag.
14146:3641 dst C ** 5st
14150:                                                                3656 dstysn'm C                              o-o^y^i
14162:     Sastu-Pare (SstwPry) ^dstwb'ry                                  GMS 109, 276, 443
14207:        VJ 14b; dsty, Sund. AI 28, 1988 pl8l
14211:     5(a)stwan (dstw'n) ©*dus-tuwdn            ©pi. -(•, ob.
14220:3665 dstw^      C => Sstw>n                                          bisexuaK/iavzng two kinds of pudenda)
14223:     6ostauc (dstwc) ^Sst'wch                                   3679 5w>ts M                                   .jjiji
14227:3667 dstwc      C => Sstwc
19711: 5575 my'm- C                           o>UjW; «jj/fU                  STi 38.1; STii 2.5; ob. postp. myd}nyt "amidst,
21016:        pcrf. st. ^np^s-, npxst-, np'xst-Cy)                        Pahl. nibdy-, nibdstan =*nyp8-, np»st-
```


## [2026-09-06T02:17:23.713Z] TOOL CALL #40: Bash

```json
{
 "command": "cd data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if '8ast- (dst)' in p or 'δast- (dst)' in p:\n        print('leaf',i,'printed ~',i-66)\n        j=p.find('8ast- (dst)')\n        print(p[max(0,j-600):j+400])\nEOF",
 "description": "Locate Sogdian dast page"
}
```


### [2026-09-06T02:17:25.746Z] TOOL RESULT

```
leaf 209 printed ~ 143
     3652 6stprtr -» prtr-
      Saspartar ©<Sast-partar -»sprtry
      handtowel                                                 3653 dstwb'ry C
                                                                     Sastu-Pare =*8st}wPry              j^-ijlT tv^-i jiT
       STi 47.14; LW 101; GMS 481; Sogd. Cpds. 1945,                 handiwork
         139
                                                                     BSTii 905, 19; Benv. JA 1955, 316, C2 gloss,,
 3640 6st B, M, S                        (oy> ^^ ^^                     Sstfiry, Schwartz. AoF 1, 26a, S W, C2, 5R 29,
      8ast- (dst) <D<OP dasta- ©nom.; ob. -y; ace.                      57V 20 p52-5R
        -w; loc. -y\-yh\ abl. -}; pi. J^}; ob. 6sty} =»pr       3654 Sstw pr- M, S                         jj^^jUlo-o
        6stw, pr 8stw wn-                                            Sastu-par
      hand, arm
                                                                      0{?)lay hand
     GMS 364, 516, 1171,
```


## [2026-09-06T02:17:35.098Z] TOOL CALL #41: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-06T02:17:35.103Z] TOOL RESULT

```


```


## [2026-09-06T02:17:38.554Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%87%D8%B2%D8%A7%D8%B1",
 "prompt": "Give the Persian etymology of هزار (hazār) 'thousand': Middle Persian form, Old Iranian/Proto-Iranian form, Avestan form, PIE root, and any cited sources."
}
```


## [2026-09-06T02:17:40.345Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0%C3%A9slom",
 "prompt": "What is the reconstruction, meaning, and descendants of this PIE root for 'thousand'? Include Greek, Indo-Iranian, Latin mille discussion."
}
```


### [2026-09-06T02:17:44.692Z] TOOL RESULT

```
# Persian Etymology of هزار (hazār) 'thousand'

**Middle Persian Form:**
The entry cites Middle Persian hcʾl /hazār/ in both Book Pahlavi and Manichaean scripts.

**Proto-Iranian Form:**
Proto-Iranian *hajáhram is listed as the source.

**Proto-Indo-Iranian Form:**
The etymology traces back to Proto-Indo-Iranian *saȷ́ʰásram.

**PIE Root:**
The ultimate source is Proto-Indo-European *sm̥-ǵʰéslom, combining the root for "one" with the suffix *-lom.

**Cited Source:**
"MacKenzie, D. N. (1971), 'hazār', in A concise Pahlavi dictionary, London, New York, Toronto: Oxford University Press, page 43" provides lexicographic support for the Middle Persian form.

The etymology demonstrates a documented path from PIE through Indo-Iranian languages to modern Persian, with cognates appearing in Sanskrit सहस्र (sa-hásra), Kurdish, Baluchi, and other related languages.
```


### [2026-09-06T02:17:46.586Z] TOOL RESULT

```
# Proto-Indo-European *ǵʰéslom: "Thousand"

## Reconstruction & Etymology
The PIE word **\*ǵʰéslom** means "thousand." It derives from "\*ǵʰes- (hand) + \*-lom," literally meaning "full hand."

## Key Descendants

**Greek**: The derivative \*ǵʰesl-i-yoy developed into Proto-Hellenic \*kʰehliyoi, yielding Ancient Greek χῑ́λιοι (khī́lioi, "thousand").

**Latin**: Through the formation \*sm-ih₂-ǵʰésl-ih₂ (combining "one" with the root), Proto-Italic \*smīɣeslī emerged, ultimately producing Latin **mīlle** ("thousand"), which has numerous modern descendants.

**Indo-Iranian**: The variant \*sm̥-ǵʰéslom (again prefixed with "one") became Proto-Indo-Iranian \*saȷ́ʰásram, with its own documented descendants.

These cognates across three major language families demonstrate the ancient Indo-European system for denoting large numerical values.
```


## [2026-09-06T02:17:51.597Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/kilo-",
 "prompt": "Etymology of kilo- and kilogram/kilometer: French coinage date, Greek source."
}
```


## [2026-09-06T02:17:52.313Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mile",
 "prompt": "Etymology of 'mile': Old English mil, Latin milia passuum, route of borrowing. Also any note on French."
}
```


### [2026-09-06T02:17:57.303Z] TOOL RESULT

```
# Etymology of Kilo-

**Origin and Introduction:**
The prefix kilo- was "introduced in French 1795, when the metric system was officially adopted there." It derives from Greek *khilioi* meaning "thousand," which traces back to the Proto-Indo-European root *gheslo-.

**Historical Context:**
The term emerged during the French Revolution's scientific reforms, when standardized measurement systems were being established. The Greek foundation connects to related words in Sanskrit (*sahasra-*) and Avestan (*hazanjra-*), all meaning "thousand."

**Modern Application:**
In the metric system, kilo- functions as a multiplier, increasing base units by a factor of 1,000. This contrasts with the prefix milli-, which divides by 1,000. Common modern applications include kilogram, kilometer, kilowatt, and kilobyte (coined in 1970).

**Related Terms:**
The page lists numerous derivatives showing how widely this prefix has been applied across scientific and technical fields, from weight measurements to electrical units to digital storage capacity.
```


### [2026-09-06T02:17:59.593Z] TOOL RESULT

```
# Etymology of "Mile"

**Origin Path:** The word "mile" traveled from Latin into Old English and eventually modern English through Germanic languages.

**Latin Foundation:** The term derives from Latin *milia*, meaning "thousands" (plural of *mille*). According to the source, "the neuter plural was mistaken in Germanic as a fem. singular," establishing the Germanic form *milja*.

**Germanic Distribution:** From this West Germanic root, the word spread across multiple languages: Middle Dutch *mile*, Old High German *mila*, and German *Meile*.

**French Connection:** The Latin word also influenced Romance languages, becoming French *mille*, Italian *miglio*, and Spanish *milla*.

**Historical Context:** A Roman mile measured 1,000 double paces (approximately 4,860 feet), though "many local variants developed" over time. Medieval European miles varied significantly—the medieval English mile was 6,610 feet, while the old London mile measured just 5,000 feet. England standardized its mile at 5,280 feet during Elizabeth I's reign through legal statute.

The word expanded metaphorically in Middle English to denote "about 20 minutes" of walking time, and by the 1580s began functioning generically for "a great distance."
```


## [2026-09-06T02:18:04.895Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%DB%8C%D9%84",
 "prompt": "List the Persian entries for میل: which are from Arabic ميل (inclination, m-y-l), which mean 'mile' (from Arabic from Greek/Latin), and which mean 'rod, milestone/tower'. Give the etymologies given."
}
```


## [2026-09-06T02:18:06.816Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%8A%D9%84",
 "prompt": "Arabic ميل: give etymologies of the homonyms — mayl 'inclination' (root م ي ل), mīl 'mile' (borrowed from where?), mīl 'kohl stick/probe'. Quote the borrowing chain for 'mile'."
}
```


### [2026-09-06T02:18:10.446Z] TOOL RESULT

```
# Persian entries for میل

Based on the Wiktionary content, there is **only one Persian entry** for میل listed:

## Persian میل (meyl)

**Etymology:** "Borrowed from Arabic مَيْل (mayl)"

**Meaning:** Inclination (described as "deferential, formal")

---

## What's NOT in the Persian section:

The Wiktionary page does **not** include Persian entries meaning:
- "Mile" (from Arabic/Latin origin)
- "Rod, milestone, or tower"

Those definitions appear only under **Ottoman Turkish** and **Urdu** sections. The Ottoman Turkish entries show "mile" and "milestone/column/obelisk" derived from Latin *mīlle passuum*, but these are not attributed to Persian.
```


### [2026-09-06T02:18:12.161Z] TOOL RESULT

```
# Arabic ميل: Etymologies of Homonyms

## Mayl (inclination)
From the root **م ي ل** (m y l), meaning "to incline, to bend, to lean." This noun denotes inclination, tendency, goodwill, sympathy, taste, or disposition.

## Mīl (mile)
Borrowed from Latin **mīlle passuum** (literally "a thousand of paces"). The borrowing chain includes: Classical Syriac **ܡܝܠܐ** (mīlā) and Hebrew **מַיְל** (mayl). The folk etymology explaining "reach of the eye" derives from the distance one can see before the horizon curves.

## Mīl (medical probe)
From Ancient Greek **μήλη** (mḗlē, meaning "probe"). This term, now obsolete, referred to "a kind of metal probe in form of a needle for applying collyrium or other treatments."
```


## [2026-09-06T02:18:17.489Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%B3%D8%AA",
 "prompt": "Persian دست (dast) 'hand': give the full etymology — Middle Persian, Proto-Iranian, Old Persian, Avestan, Proto-Indo-Iranian, PIE root, and cited sources."
}
```


## [2026-09-06T02:18:19.149Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D8%AA%DB%8C%D9%86",
 "prompt": "Persian آستین (āstin) 'sleeve': what etymology is given? Middle Persian form, reconstructed Old Iranian form, and any connection to dast 'hand'. Cite sources named."
}
```


### [2026-09-06T02:18:23.932Z] TOOL RESULT

```
# Etymology of Persian دست (dast) - "hand"

**Proto-Indo-European Root:**
The word derives from PIE *ǵʰes- ("hand")

**Proto-Indo-Iranian:**
From *ȷ́ʰástas ("hand")

**Old Persian:**
From 𐎭𐎿𐎫 (dasta)

**Middle Persian:**
From 𐭩𐭣𐭤 (YDH /dast/)

**Persian:**
Inherited as دست (dast)

**Cognates cited in sources include:**
- Northern Kurdish dest
- Avestan 𐬰𐬀𐬯𐬙𐬀 (zasta)
- Sanskrit हस्त (hasta)
- Ancient Greek χείρ (kheír)
- Latin hīr
- Albanian dorë
- Tocharian A tsar

The entry references Rastorgujeva & Edelʹman's 2003 *Etymological Dictionary of Iranian Languages* (Moscow: Vostochnaya Literatura) as a primary scholarly source for this etymological chain.
```


### [2026-09-06T02:18:25.667Z] TOOL RESULT

```
# Etymology of Persian آستین (āstin) "sleeve"

Based on the Wiktionary entry, the etymology is described as follows:

The word is "of unknown etymology due to not having any clear cognates," but scholars propose it may be **borrowed from Southeastern Iranian languages**. 

Herzenberg's analysis suggests a connection to **Pashto لستوڼي (lastúṇay, "sleeve")**, which relates to Pashto لاس (lás, "hand"). The theory involves a /d-/ to /l-/ sound shift occurring in some Eastern Iranian languages.

The entry notes that "dialectal Persian terms borrowed from Pashto or a related language" show the initial /l-/ has been dropped, potentially explaining the Persian form's development.

**No Middle Persian or reconstructed Old Iranian forms are provided** in this entry. The earliest attestation cited is from Firdawsī around 1010 AD.

The connection to "dast" (hand) is implicit in the Pashto comparison, as lás means hand, but the entry does not explicitly discuss a Persian hand-related etymology.
```


## [2026-09-06T02:18:36.221Z] TOOL CALL #50: Bash

```json
{
 "command": "cd data/verification/sources/refs && ls | tail -40",
 "description": "List remaining refs files"
}
```


### [2026-09-06T02:18:36.308Z] TOOL RESULT

```
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


## [2026-09-06T02:18:41.701Z] TOOL CALL #51: Bash

```json
{
 "command": "cd data/verification/sources/refs && echo \"==WLD3 gheslo==\"; grep -n \"ghesl\\|ĝheslo\" WLD_band3.txt | head; echo \"==WLD3 ghesto/ghesor==\"; grep -n \"ghesto\\|ghesor\\|ghesr\" WLD_band3.txt | head; echo \"==IEC==\"; grep -n \"gheslo\\|ĝheslo\\|ghesto\\|ghesr\" IEC.txt | head",
 "description": "Walde-Pokorny register and Mann"
}
```


### [2026-09-06T02:18:41.793Z] TOOL RESULT

```
==WLD3 gheslo==
==WLD3 ghesto/ghesor==
==IEC==
4659:gheslos, -io-, -i 'yardstick, tally’ (?) (w. *sm-, smi- thousand") (?) Cf. Skt. sa-hasram *1000'; Gk. kheílioi, pl. ‘thousands’; Lat. mille (thousand', fr. *smi- ghesli- ?)
```


## [2026-09-06T02:18:43.186Z] TOOL CALL #52: Bash

```json
{
 "command": "cd data/verification/sources/refs && ls incoming 2>/dev/null; echo ===; grep -rn \"WLD\" ../refs_online.json | head -3; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(json.dumps(d['WLD'],ensure_ascii=False)[:1500])\"",
 "description": "Check WLD availability"
}
```


### [2026-09-06T02:18:44.983Z] TOOL RESULT

```
Exit code 1
AHD
ARY
BLY
BQT
CEL
FFD
IRN
ISS
KGW
MAG
MFL
MON
OEW
PLA
PRT
_tessdata
TTS
TYL
VIE
WLD
ZAW
فرهنگ ریشه های زبان فارسی (2).pdf
(eval):1: == not found
```


## [2026-09-06T02:18:48.037Z] TOOL CALL #53: Bash

```json
{
 "command": "cd data/verification/sources/refs/incoming/WLD && ls",
 "description": "List WLD incoming"
}
```


### [2026-09-06T02:18:48.079Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
```


## [2026-09-06T02:18:48.696Z] TOOL CALL #54: Bash

```json
{
 "command": "cd data/verification/sources/refs && sed -n '4650,4670p' IEC.txt; echo \"== IEC ghes hand ==\"; grep -n \"^ghes\\|ghest\\|ĝhesr\" IEC.txt | head",
 "description": "Mann context"
}
```


### [2026-09-06T02:18:48.764Z] TOOL RESULT

```
ghelüs (?) ‘tortoise’. WP I, 631 Gk. khélus, id. LLat. cf. (Cilician?) golaia, id. (Diosc.); OCS cf. žíly, Zelivi, gs Zilüve, id.
gheluos, see gheleuos
ghend-, see ghed-, ghnd-. (The evidence is ambig.) Gk. cf. kheísomai ‘will contain’; Alb. gjej (?) “find; guess? beside gjíndem “am found, oc- cur’; Lat. cf. prae-hendo; Pol. cf. Zadac dest. re’; Li. cf. pa-si-gendu, inf. -gesti, pf. -gedau *keep watch, observe'
ghendh- (ghondh-, ghndh-) ‘smell, stink’? Li. gendu, gesti ‘rot, turn bad’; (o-gde in) Skt. gandháh ‘smell’; Per. gand, id.; gande ‘stinking’; gandana ‘leek’; Arm. (?) gon£ (i- st. adj. *mangy"); (z-gde in) Go. gund ‘canker’; OHG gunt, OE gund ‘pus’
gher- (1), ghor- “cry” Arm. ger ‘wail; Lat. cf. hir-undo ‘swallow’ beside (expressive) hirrio, ire *growl; MIr. (o-gde) goirim ‘call
gher- (2) ‘fat Arm. gẹr, gs giri, adj. id.; Ir. geir, f. id.; Oss. cf. dzälarä ‘blob of fat (?)
gher- (3) ‘desire’. See gherio-
ghergho, ið ‘roughen; make rough, become rough, harsh or hoarse ` Gk. kérkhō ‘roughen, make harsh’; kerkhnós, adj. “harsh, hoarse’; Ir. geargaim ‘blotch, mar’: cf. gearg ‘rash’; Li. cf. gergždžiù, inf. geřgžti ‘be hoarse’
gherios, io ‘avid; desire’; gherið ‘desire, wish, need’. WP I, 600 Skt. háryami, v.; Hes. cf. khérna ‘poverty, want, need’; khernés, gs khernétos ‘needy’; Lat. heries ‘desire’; Osc. her súm ‘I wish’; beside heriiad, Umb. heriiei (3s. “he may wish"), Umb. (also) heriest, id.; Osc. heriam, acc.f. ‘delight; OHG gër ‘desirous’; MHG géren, v. 'desire";.gér, f. ‘desire’; OHG géren, OFris. geria, v. id.; Icel. ger ‘greedy’
gheslos, -io-, -i 'yardstick, tally’ (?) (w. *sm-, smi- thousand") (?) Cf. Skt. sa-hasram *1000'; Gk. kheílioi, pl. ‘thousands’; Lat. mille (thousand', fr. *smi- ghesli- ?)
gheughilos, gheughos "Tool" Cf. geugos Ir. cf. guag ‘folly; fool’; guagaire ‘vagrant’;
ghelüs — ghíghono
20
25
30
35
40
45
320
(*-u- in) gogaille ‘fool’; dim. cf. guaigin “little foo; MHG gege, giegel, id. (Isophonic are OCS ZuZelí ‘beetle’; Blg. ZüZel ‘snaiľ; OCz. žúžela ‘earthworm’; cf. Slovene žuželka ‘insect and žužek ‘corn-weeviľ. Preferably to geugos on semantic grounds)
gheus-, see ghus-
== IEC ghes hand ==
814:auk- (2) (?) full-grown, tall’ Lat. cf. -ūca in plant-names festūca, lactūca; verrūca ‘wart’ also qua ‘growth’; Br. cf. éog ‘tipe’; Go auhuma ‘highest’; Li. auklēti
816:auks- (auksomo-) “high; height, growth?. Cf. auk- (2) Gk. cf. aükse, aüksimos; Lat. cf. auxilium; beside Auximum (a town in S. Italy: Osimo) beside Uxama (a town in Spain: Borgo de Osma); Ir. cf. uachtar ‘top’; W uchaf ‘highest’, beside OW uch, W uwch (‘higher’. Phonology obscure, but not as JMJ § 148 (14))
4659:gheslos, -io-, -i 'yardstick, tally’ (?) (w. *sm-, smi- thousand") (?) Cf. Skt. sa-hasram *1000'; Gk. kheílioi, pl. ‘thousands’; Lat. mille (thousand', fr. *smi- ghesli- ?)
6013:ghesmn-, see ghes- G cf. Germ ‘barm’; Icel. gisinn ‘leaky, thin, sleazy’?
19574:upoto-, upəti- Av. upato, adj. “high, long’; Hitt. upati- (que- ried: *east'); Gk. cf. hüpatos, adj. ‘highest’; Ir. cf. fada “long: faide, s. “length”
20091:uersi- (?). Cf. WP I, 267 Skt. cf. vargi-sthah ‘highest’; Per. bi$, adj. “much, more’; Olr. ferr, Ir. fearr, adj. “better”. (ISophonic: Go. waírsiza, OHG wirsiro, ON verri ‘worse’; G wirs, wirsch “bad, raging’; Du. cf. wars 'averse") (!)
```


## [2026-09-06T02:18:53.711Z] TOOL CALL #55: Bash

```json
{
 "command": "cd data/verification/sources/refs/incoming/WLD && grep -n \"ghesl\\|ĝheslo\\|gheslo\" WLD_Bd1_pages.txt | head; echo \"== ghesto/ghesor ==\"; grep -n \"ĝhes\\|ghesor\\|ghesr\\|ghesto\" WLD_Bd1_pages.txt | head -20",
 "description": "Grep Walde-Pokorny Bd I"
}
```


### [2026-09-06T02:18:53.805Z] TOOL RESULT

```
60198:gheslo- „tausend '?      1
== ghesto/ghesor ==
```


## [2026-09-06T02:18:57.129Z] TOOL CALL #56: Bash

```json
{
 "command": "cd data/verification/sources/refs/incoming/WLD && sed -n '60180,60230p' WLD_Bd1_pages.txt; echo \"=== find page tag ===\"; awk 'NR<60230 && /\\[pdf page/ {l=$0; n=NR} END{}' WLD_Bd1_pages.txt; grep -n \"\\[pdf page\" WLD_Bd1_pages.txt | awk -F: '$1<60198' | tail -2",
 "description": "WP I gheslo entry"
}
```


### [2026-09-06T02:18:58.765Z] TOOL RESULT

```
kunstelt zu vermitteln ware (eher als „beiBend, pikant" zu slay, gonk a
„bitter“   — s. u. g'iher- „hei£S“ — unter formellem.  z. T. auch semasiologi-

schem Anschlufi an saldus), noch auf air. gorte „Hunger“ (auch nir. gorta,
also mit idg. t nicht aus dim herleitbar; vielmehr nach Pedersen KG. I
                   ,


33 zu mir, gout „bitter“, slav. gonk* ds.)        endlich weicht got. gredns
                                                                      ;


„Hunger“ von ai. gardha-h in der Vokalstellung ab (s. u. gher- „begehren“).

ghes- „essen,      fressen, verzehren"             s.       unter ghos-.
            *


gheslo- „tausend '?      1




  Ai. sahasra n. „Tausend“, sahasriya „tausendfach“, av. hazanora n.
„Tausend“, np. hazSr woraus arm. hazar entlehnt (Hubschmann Arm. Gr.
                             ,

I 174);     gr. jon. yeiXioi ,     aeol.       ysXXioi,       att.   ytXioi    (-iXi-   < -eli-   s.   Wacker-
nagel IF. 25, 329), fiber das unerklarte aeol. -/jXXyoTvg                           s.       Brugmann-Thumb
254 mit Lit.
                        (zuletzt Wb. I* 55, 437) behauptete Yerwandtschaft
      Die zuerst von Fick
ist auf zweierlei Weise moglich: 1 sahasra ist ein Kompositum mit idg.
                                                        .



*sm, sei es, dad man dieses a) mit Fick, Joh. Schmidt u. aa. als ,.eins“,
oder b) mit Brugmann IF. 21, 10, Grdr. 2 II 2, 47 zw. als „zusammen mit‘-
oder c) nach dem germ, sin- als „groB, gewaltig“ fibersetzt. 2. Das gr.
arische Wort fur tausend ist mit Jacob Grimm, Brugmann aaO., Wacker-
nagel sprachl. Enters, z. Homer 8 A 4, Hirt idg. Gr. Ill 314 eine Weiter-
bildung von idg. *seghes -, bedeutet also ,,Kraft(hundert)“. Gegen 1 a, b
und c spricht die Schwundstufe srn (Wackernagel zuletzt aaO.), gegen
1 a, b auBerdem die Bedeutung. Bei 2 ist gr. yihoi nur auf komplizierte
Weise zu erklaren (Versuche bei Brugmann aaO. und Wackernagel aaO.).
   Abzulehnen ist Sommers IF. 10, 216ff., 11, 323 f. Heranziehung von lat.
mille aus *smi ghsll, eigentlich „eine Tausendheit" s. unten u. *sem- ,,eins“
1     u. 3 (II 488 u. 491).


=== find page tag ===
```


## [2026-09-06T02:19:08.440Z] TOOL CALL #57: Bash

```json
{
 "command": "cd data/verification/sources/refs/incoming/WLD && grep -n \"ghes-to\\|ghes-or\\|ĝhesto\\|hasta-h\\|zasta-\" WLD_Bd1_pages.txt | head -20; echo ===; grep -n \"pazaste\\|pa-zaste\\|paZasti\\|Achselhohle\\|Achselh\" WLD_Bd1_pages.txt | head",
 "description": "WP I ghesto hand"
}
```


### [2026-09-06T02:19:08.500Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-06T02:19:11.878Z] TOOL CALL #58: Bash

```json
{
 "command": "cd data/verification/sources/refs/incoming/WLD && grep -n \"ghesto\\|ghesor\" WLD_Bd1_pages.txt | head -20; echo \"--- try hasta\"; grep -n \"sahasra\" WLD_Bd1_pages.txt | head -5; echo \"--- ghos\"; grep -n \"^ghes\\|^ghos\" WLD_Bd1_pages.txt | head -20",
 "description": "WP I ghesto search"
}
```


### [2026-09-06T02:19:11.970Z] TOOL RESULT

```
--- try hasta
60203:  Ai. sahasra n. „Tausend“, sahasriya „tausendfach“, av. hazanora n.
60212:ist auf zweierlei Weise moglich: 1 sahasra ist ein Kompositum mit idg.
--- ghos
54152:ghost von XeiBer BB. 20, 73 n. konstatiert), ghd&ayati „findetErhorung bei
60194:ghes- „essen,      fressen, verzehren"             s.       unter ghos-.
60198:gheslo- „tausend '?      1
60748:ghos- „essen, fressen, verzehren".
60766:ghosti-s .,Fremder, Gast“.
```


## [2026-09-06T02:19:17.508Z] TOOL CALL #59: Bash

```json
{
 "command": "cd data/verification/sources/refs/incoming/WLD && grep -n \"tsar\\|kessar\\|ki-es-sar\\|jern\\|jer-k\" WLD_Bd1_pages.txt | head -20",
 "description": "WP I hand entry search"
}
```


### [2026-09-06T02:19:17.568Z] TOOL RESULT

```
11230:   abg .jernl’q, imati          ,,nehmen“, imq, jeti ..nehmen* {*emq, vgl mn-             1
18674:Inschr.   Kretschmer ZfoG. 57, 495 ff.), jurgo iniuria pdr)ierdre, ejernre,
23405:  Ai. rutsa-, vatsard- m. „Jahr“, vatsd- m. „Jahrling, Kalb, Kind“. rat-
57022:ags. cicrau, engl. clmrn ds., Pick III 4 38, Falk-Torp u. kjerne II).
57237:     Tochar.    tsar,     sar ,.Hand    "
57239:                                                 arm. jern   ds.   (Hiibschmann Arm. Gr. I 470);
```


## [2026-09-06T02:19:19.982Z] TOOL CALL #60: Bash

```json
{
 "command": "cd data/verification/sources/refs/incoming/WLD && sed -n '57225,57270p' WLD_Bd1_pages.txt",
 "description": "WP I hand entry text"
}
```


### [2026-09-06T02:19:20.039Z] TOOL RESULT

```
Bartholomae Ai.Wb. 1856 mit leicht beleidigt“ iibersetzt; es gehort ebenso
wie *asnrdta in anasarata nicht erziirnt ‘, das Uhlenbeck 357 zw. heran-
                                        ,.


zieht, zu ai. lignite, vgl. np. azard ,.gekrankt und azardcin „kranken-‘ siehe
                                                                   :




Hiibschmann Pers. Stud. 6, 146.)
     Tochar.    tsar,     sar ,.Hand    "
                                             ;
                                                 arm. jern   ds.   (Hiibschmann Arm. Gr. I 470);
alb. dors ds. (< *?jhera s. G. Meyer Alb.         Wb. 72, Alb. Stud. Ill 86), plur. kon-
sonant. duar         (< *gheres       s. Thumb DLZ. 1913, 805,  Jokl lingu. kulturhist.
Unters. 90 f.).
  Gr. yeiQ „Hand    dor. gen. yrjQos, aeol. acc. pi. x s 8Q a s (<
                             ‘,                                       nach
Wackernagel KZ. 29, 134, Verm. Beitr. 15? s. Bechtel Gr.Dial. I 38, II 315
und die bei Brugmann-Thumb Gr. Gr. 141, 148,209 genannte Literatur),
evyegij? „leicht zu handhaben, leicht, leichtsinnig ", dvayegg? ,,schwer zu
handhaben, schwierig“, yogtos eingehegter Platz, Hof, Weideplatz ‘, hier-
                                                 ,


her auch yogos (nach Curtius 199) „Tanzplatz, Chortanz‘‘ als urspriinglich
..eingehegter Platz“ oder nach Froehde BB. 10, 301 als .,Reihenfolge,
Ordnung“ zu lit. zdras ,.Lauf, Weg, Runde, Wendung“ ? Vgl. Boisacq 1067,
Vf. LEWb. 2 311. Ganz zweifelhaft trotz Boisacq s. v. yooiov ,,Nachgeburt,
aus Milch und Honig bereitete Speise, Haut, Leder‘\        Kaum zutreffend     —
stellt endlich auch Brugmann IF. 37, 239 (im AnschluB an Curtius 199)
her ygfjodai „gebrauchen, benutzen“, yggya „Sache, die man gebraucht'
       :
                                                                                              -

                                                                                                  ,


ygrj ,,es ist notig  yged) „Bediirfnis, Bedarf ', ygecog, ygrjog „Bediirfnis,
Verlangen, Schuld*; wahrscheinlicher ist die Verbindung mit yeigwv usw>
s.   u. 6.   *gher- „kurz, klein“.
   Osk. heriiad „capiat“, herrins „ceperint“, lat. cohors „Hofraum, Gehege,
Viehhof, Haufe, Menge, Schar, Gefolge“, hortus „Garten‘-' (im Altlatein                      =
villa s. Paul. Fest. 73 ThdP.), osk. lmrz „hortus, lucus“.    (Nicht zu *gher-
```


## [2026-09-06T02:19:25.326Z] TOOL CALL #61: Bash

```json
{
 "command": "cd data/verification/sources/refs/incoming/WLD && sed -n '57190,57226p' WLD_Bd1_pages.txt | head -40; echo \"=== search ghesto in Bd2 ===\"; grep -n \"ghesto\\|zasta\\|hasta-\" WLD_Bd2_pages.txt | head",
 "description": "WP I root headword for hand"
}
```


### [2026-09-06T02:19:25.399Z] TOOL RESULT

```
      304 A., der yoigog auch zu unsrer Wurzel ghcr ,strahlen“ ziehen
 Beitr.
mochte, vgl. unter *ghers- „starren“).
      [ghereu-], ghrii-.
   In aisl. gryiandi „Morgenrote“, aschw. gry „(vom Tage) grauen, dammern ',                      1




dan. gry ds., gry n. „das Grauen ', aisl. qsgrua „das Aschgraue ‘, <C*qsy.ogrua
s. Bugge Norr. Skrift. af sagnhist. indhold 339); hierber auch aisl. grey n.

„Hiindin, Feigling      greyhundr „Windhund', ags. grighund ..Windhund ‘?
  Vgl. im allgem. Vanicek 98, Fick I 4 418, III 4 142 f., 144, Falk-Torp 338,
348, 354, Persson aaO., Trautmann Bsl.Wb. 366.


4.    gher- „greifen,         fassen, umfassen, einfassenA

     Ai. harati      ,
                                  nimmt“ (nicht aus bhar- s. Wackernagel
                         bringt, tragt, holt,
AiGr. I 248, 251), hdrana n. „das Bringen, Nehmen, Spenden usw., haras n.
,
  Nehmen, Ergreifen, Griff, Energie, Ungestiim, Kraft, Gewalt‘.
     (Av. sara -, asara - Bedruckung“, die Wackernagel I 248 zu liar- stellt,
                                  ,



belegt         Avesta Handbuch 148 nur durch Imdsara- V. 13, 45, was
             Justi
Bartholomae Ai.Wb. 1856 mit leicht beleidigt“ iibersetzt; es gehort ebenso
wie *asnrdta in anasarata nicht erziirnt ‘, das Uhlenbeck 357 zw. heran-
=== search ghesto in Bd2 ===
19663:im Fluge^^, mit fra- „wegfegeii‘^^, zasta-marsta- „durch Handschlag (d. i.
```


## [2026-09-06T02:19:31.264Z] TOOL CALL #62: Bash

```json
{
 "command": "cd data/verification/sources/refs/incoming/WLD && grep -n \"hdsta\\|hasta-h\\|hasta- m\\|Ai. hdsta\\|pazasti\\|zastp\\|apers. dasta\" WLD_Bd1_pages.txt | head -10; echo ---; grep -n \"dasta-\" WLD_Bd1_pages.txt | head -10",
 "description": "WP I hasta/dasta"
}
```


### [2026-09-06T02:19:31.337Z] TOOL RESULT

```
---
```


## [2026-09-06T02:19:33.676Z] TOOL CALL #63: Bash

```json
{
 "command": "cd data/verification/sources/refs/incoming/WLD && grep -n \"Hand“\" WLD_Bd1_pages.txt | sed -n '1,40p'",
 "description": "WP I 'Hand' occurrences"
}
```


### [2026-09-06T02:19:33.739Z] TOOL RESULT

```
4252:Vgl. Yf. LEWb. 2 50.             Stokes erklart nicht iiberzeugend               ir.    Cm „Hand“ als
4808:manes „Hand“ als „die fassende" (s. auch met- „miihen“??), so daB eine
32504: Meyer IF. 35, 224 — 237. Ygl. ghabh- in ai. gabhasti-h „Ar orderarm, Hand“
43558:dec  und hendec „behende“, dagegen zu handus „Hand“; a. zur germ. Sippe
48942:„tuend,  machend“, m. „Hand, EIefantenrussel“ (kaum in der Bed. „Hand“
50967:  Ai. hastu m. „Hand“, hastavant „ hand verse hen", av. zastu apers. (last a m.             ,
50976:  Abzulehnen die Anreihung von gr dyoarog „flache Hand“ (de Saussure
51387:  norw. dial, keiv schief, gedrekt, verkehrt", keiva „linke Hand“, kctv,
58861:zuriick mir. gil „Hand“, gel-fine „handfamily“ (s. Stokes BB. 21, 126) und
60471:  Av. gava du., gavo a. pi. ,,Hande“; gr. *yvfa oder kons. *yv-g „Hand“
60521:Liden Arm. St. 120; „ergreifen" dann erst von „Hand“ aus oder wie dt.
74222:dt.Hand wobei de-kmt entweder als „zwei Hande“ oder „Hand“ seiber als
76161:o/?oAo«“), dga^, -yog f. „Hand“, pi. ddgxeg deopai Hes.;
76838:              Arm, Hand“. Oder zu mnd. timpe „Spitze, Gipfel“, ndl. timp
79878:mhd. tener m. „flache Hand“, Curtius 5 255 (samt ai. dhanns-. s. u.), Fick
```


## [2026-09-06T02:19:35.910Z] TOOL CALL #64: Bash

```json
{
 "command": "cd data/verification/sources/refs/incoming/WLD && sed -n '50955,50985p' WLD_Bd1_pages.txt",
 "description": "WP I ghesto entry"
}
```


### [2026-09-06T02:19:35.972Z] TOOL RESULT

```
  KiD.yas. -uvtos EN.: ags. gealg, galg ,.traurig, finster“. Ilolthausen IF. 20.
  322: s. auch Boisacq s. v.
                                             ,




                                         ghasto-      — glie-, gho-                                        541


ghasto- „Hand, Arm".
  Ai. hastu m. „Hand“, hastavant „ hand verse hen", av. zastu apers. (last a m.             ,



„IIand, und zwar ahurischer AVesen", zastu vant „tatkraftig“ lit. pazast'ts f..             ;


pagaste „Raum unterm Arm, Achselkohle".
  Fick I 4 420, 433, Wackernagel ai. Gr. I 248, Trautmann Bsl. Wb. 367.
  Abzulehnen die Anreihung von gr dyoarog „flache Hand“ (de Saussure
                                                       .



Memoire 53 A. 1, oft nachgesprocken, s. die Literatur bei Boisacq 9) vgl.
unter *ger- „fassen, zusammenfassen". — Uber aksl. pazucha „xoA7iog“ sielie
Berneker SlEWb. 233 f., Trautmann aaO. 64.

ghasto-, ghazdho- „Rute, Stange".
```


## [2026-09-06T02:19:43.125Z] TOOL CALL #65: Bash

```json
{
 "command": "cd data/verification/sources/refs && echo \"==BRT zasta==\"; grep -n \"zasta-\" BRT.txt | head -5; echo \"==BRT hazanra==\"; grep -n \"hazaŋra\\|hazanra\\|hazayra\" BRT.txt | head -5; echo \"==PHD==\"; grep -n \"hazār\\|hazar\\|^dast\\b\" PHD_mackenzie.txt | head -10; echo \"==NYB==\"; grep -n \"hazār\\|dast \" NYB_vol2_glossary.txt | head -10",
 "description": "Bartholomae, MacKenzie, Nyberg lookups"
}
```


### [2026-09-06T02:19:43.225Z] TOOL RESULT

```
==BRT zasta==
2745:•  j.  aesmö.zasta-  Adj.  'Brennholz  in  der  Dat  'etwas  (Akk.)  haben  wollen,  begehren, Hand  haltend,  mit  Brennholz  in  der  Hand' :  erstreben  für  -':  yö  . .  tanuye  tsaite  >rä- yas3  ^WJ  .  .  frayazaite  "stö  Y.62.1;  V.  ^r^m  V.  ij,  19;  —  ä'irava  .  .  manmtam 3.1.  isimtiö  dalnayäi   am^m   iamnö  tanuye
4867:ayanho-zasta-
4868:•  j.  ayanhö.zasta-  Adj.  'mit  nietallenen (eisernen)  Klauen';  varäzahe  ('eines Ebers'; ayüahs^äiahe  'saslahe  Yt.  ro.  70.
8546:•  ].,  g.  ustäna-zasta-  Adj.  'mit  (zum Gebet,  zur  Bitte)  ausgestreckten  Händen';
9878:•  j.  gao-zasta-  Adj.  'Milch  in  der  Hand habend,  mit  M.  in  der  Hand':  yasß  %wä .  .  fräyazSite  .  .  'td  Y.  62.  i ;  V.J.  1.
==BRT hazanra==
4509:•  j.  anu-maya-  Adj.  'mäh  machend,  blö- kend', vom  Schaf;  mit  pasaf-:  bis  kapta pasvS  °ya  .  .  nisirinuyHt  V.  14~  16;  — pasius  *g3r>bul  'yiie  V.5. 38;  —  koU. 'pecus  ovillum':  pasiui  °yche  pawm  Y.  2. 24.  A)  als  Subst  'Schaf:  hazanram "yanqm  frSvinuyJl  vtspanqmca  aitaisqm pasvqm  ,.  V./Äyo;  —  saUm  aspanqm.. /lazaanm  gavqm  ba^oarj  "yanqm  Yt  5. 2i;  0.3,  V.i'2.4;  —  niiinmn  staor?m bisazy.lt  "malm  anj5  V.  7. 43;  43;  — 'yanqm  arsnqmV  .22.20.  a)  sva. 'Schaf- fleisch': hazat3nm  gSus  j^anüiiiqm  (sd.) baivan  'yanqm  H.;.s'*.
15074:da^anam   hazanrai  haza„,S  p'  bagvarSi\^''"f'f^^^)Z^-'^  amahe  p'  srimaht bafvans  ahaxHäi  ahaxitavö  i'  nämäm  .  .  P' JaiSas^ehf  YLy.S^i  K      
16470:•  j.  baevan-,  baevar-  n.  'Zehntausend, Myriade';  navaca  navaitlsca  navaca  saia navaca  hasattra  navasJs{sA.Ya  •v_qn{^.) Yt  13.  59,  V.  22.  2 ;  —  fravasays  .  .  yä mao^mitncil  myesäinam  °vam  (NP.)  upa- vazinle  "..die  (als  sva.)  inMyriaden . .  herzu- fahren" Yt.jj.  64;  —  urvarh  ..  satavaiti- nqm  hazanravaitinqm  °varf  'varanqm '' V.5.  19  GI.(?).  a)  mit  Gen.:  saümca kasaiirTmca  'vanla  *parianqm  Yt/5. 71; JO.82,  5.21,  $.3,  H./.S,  sVar.,  12,  Y. öiS'-iS.  V.J.  31,  5'.  81,  i4.'i-i.(>"-\—  ys janai  azsqm  äaivanqm  . .  °r5i '>  'vand  (soll heissen)  "..  10000  mal  loooo"  Yt.j.  10; 4.2,  VytJß.  A)  attributiv  gebraucht: *vafv  yjnqnh  nisirinaoiH  Yt.  /o-  a  7 ;  — kakra  . .  yatataiibyS  . .  pan^asaiblsca  sa- täflca  /lasaarSisca  'variblsca  ahaxitäisca Vr.Äi.
25913:—  panea  'ta  upäsananqm  V.J.  36;  36,  ä 83,  *F.  10;  —  xsvas  'taif  Aala.H'kanqm  V. 4-(>;  13';  —  hapita  'ta  us'tranqm  Ytg. 30; V.4.7,  13';  —  aita  'ta  upusananqm  V. 4. 14;  14,  8;  —  ye^ke  avavat  hatnanqtn (sd.)  «(wa  **W(/  (als  Nom.)  hasatirimea Yt.5. 120;  V.4.9,  15'.  b)  adjekL  ge- braucht: Äfl^ra.._yiisfl/'aÄ^jiT.,^anfaj(i/to"o Hailca  hazanraisca  Vr.  Ä  i.  a)  mit attiib.  Einerzahlen:  hazatanm  narqtn  .  . iaoxma  . .  xlvas  'ta  . .  tisrS  'ta  (als  Gen.) "den  Samen  von  1000  Männern  . .  von 600  . .  von  300"  V.  2. 30.
27474:•  j.  srutgaoSa-  Adj,  'des  Ohren  hören, scharfhörig"':  mt^raiaf  .  .  °lS  hazanra.- yaoxsHS  YtJO.107;  19.35.
==PHD==
291:   The orthographic principles followed, in seemingly haphazard
1911:dast(a)~ird [YDE-, dst-krt l I M dstygyrd, N dastgird] estate.
1912:dast-l1ir [dst OHDWN, (v. griftan) I N --] I. helper; 2. captive.
1913:dast-~raw [dstglwb ' ] captivity.
1914:dast-karih [YDEk'lyh I N --i] handiwork.
1915:dast-Aoy [dstfwd] = ~omez.
2882:hazar [I,OOO, he)ll M hz)r, N -] thousand.
7766:ten dah.                                  thousand hazar.
9307:hazar:-l
9316:hazarag~                       ,~~     rozwarag
==NYB==
483:apa-dast [’pdst!] “what is on the hand” = glove, or the like, 8518. — < *upa-dasta-,
1205:dast [YDH, Prth YD’; dst'], with the indef. art. dast-ē [YDH + 1] 1. hand HajA:11.14. B:12.16. 9% and passim; power 1924, 24%. 304; — ~~ apar nihātan to put one's hand to 6215; — ~ avis burtan to deal with a th. 8119-29; — frac ~ Sustan to wash one’s hands 443-9, with hac to dissociate oneself from, to break off all relations with 384; — a ~ 4... rasitan to come to close quarters with a p. 24?, — pat ~ daštan to have a hold on, to hold sway over 87%, — 2. ~ i yāmak a set of clothes 2; FrP 29. — 3. game: 3 ~ hae ... burt he won three games (of chess) against... 11915; ~ 4 vat vāzītan
1758:hae [MN ; hc 619] prep., with -c: MN-c = hac-ic; not with an encl. pron. (as to haciš, hacisan v.s. v. hactš); the original sense ‘accompanying, with’ (Skr sacā) is still transparent in ~ ... hämisi (g. v.) ‘together with’, but the meaning ‘from, of’ prevails since the OIr period. 1. Local: hàn yam ... hac dast i Artaxser 6 damik opast 92°; api-š hecak hac cah ul hixt 155; hakar hac asp bē nisinam 27?; hac star püdak tai mah pädak 93"; hac dar ētšān bagän namäc burt from the gate-way (i.e., halting at the entrance, from this place) I rendered adoration to His Majesty. P1:4; — figurative, with a great many vbs. and idioms, the sense of ‘from, of’ being more or less transparent. akahé- nitan, āšnūtan, pursitan, x"āstan, dast šustan hac ete., v. the individual ws.; — origin: ke cihr (Prth Shr) hac yazatān (Prth y’ztn) whose origin is from the gods, of divine origin HajB: 2.4 (HajA: 2.4). SPrs: 5-6 (yazdān) (SPrth: 5). P1: 2.4 (yazdàn) ; "Apasči... à hac Haran ŠPrs: 9; hac tohmak + Dārāt būt 18, etc. — 2. tem- poral: hac im róc from today onwards, henceforth 9"; hac im réc tdi 3 roc within three days 51%; hac rahikehv [lsykyhy] ever since my youth 1282-5; ete. — 3. after a v. n. it expresses the subj. of the act: patirak zanišn + hac ganäk menoi on the point of being slain by the Evil Spirit 46°-§; zanisn i devàn hac han i 0$ xvarrah the demons being slain by his divine splendour 461?; freftakeh + hac dēvān de- ception by-the demons 461; 4513-14; ete. —
2710:darraky — to put one’s feet on the rock HajB:6-7.12-13; tigr andar kamān ~ to put the arrow to the bow (-string) 100%; catrang ~ to arrange a game of chess 11914.20.21. gartänäk be ~ to cast the dice 1202122; pat ... ~ to deposit in... 10719, 11312; apar ~ to put (wood) on (the fire) 95°; dast apar ~ to put one's hand (to work) 6215; bé ~ to deposit 4216, to take off (a garment) 5717; — nam m to give a name, to name 1025-36, 11421, 11623; pat nām i ... ~ to name after 1201-2; mēnišn ~ 6 to ponder on 5?2-?3, — Av. (721 sq.) ni-dä-; MPrs nh’dn, nyh?dg, Verbum 194; Ps. nyd?t; Paz. nahādan; NP nihādan; only SW.
3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
3029:patigriftan [ptglptn', MKBLWN-], pati- gruftan [ptglwptn'] pačir- [MKBLWN-, ptyl-], pt. = pret. pass. 3d p. sg. patigrift [ptglpt'; MKBLWN.t, MKBLWN-x, 2876, 299. 611; -x, 21, 18%] patigruft [ptglwpt'] 5811. 6015: to receive, to ac- cept, to take up, often with the prev. frac: 1. Bastvar (PLK”) pat dast fräc patigrift B. caught *the battle-axe (just swung by the attacking enemy) with his hand 2875-26; barak xvēš pat dast frac patirét he himself takes command of the steed (by grasping the reins) with his hand 299. — 2. en den i mäzdesnän hac Ohurmazd patigrift he received the Maz- dayasnian religion from O. 18%2?sq. 1919, ete.; hàn 4 Evak frāc patigrift u apārīk hac dastavar hist the one (doctrine) he accepted and the other he excluded from the canon 10954. — 3. to agree 215; to accept, to comply with 381; göbiön ~ to receive the (divine) command 5811, 6028. — 4. pat fradandeh ~ to adopt as one's son 275; pat zanēh ~ to espouse 161; pat nikühdareh ~ to take charge of 8213. — 5. kē hac šmāh hàn patirét marnjénitan ? who among you takes it upon himself to slay this man? 4217; oišan-ic . . . baxtan
3109:must go back to *pati-yam- ‘to take hold of’, from Av. (1262sg.) yam-, chiefly with preverbs. I find *pāyam as a v. n. in two passages: 1. DkM 285 aköman ... menisn päyam ‘A. holding Mind in his grasp’; 2. ibd. 501? páyam hešm andar ménisn “Wrath taking Mind in his grasp’ (?). — Zsprm VIII, 4 has a somewhat divergent, perhaps more original version of the story 441-9: ^L ZLWN ‘L y’twk’n, MH-t L>? HWH-nd byšznyt'l, BR’ L'WHL ‘L h'nk' ZLWN, YDH BYN ml PWN "MŠH' ZY TWR’ ZY MDM thé YDLWN-t', hysme bwd wt'p' PWN NPSH-tn' zhk' MNW-t PWN 'škmb' = mà šav o yātūkān, cē-t nē hend bēšazanī- tar, bē apāc 6 xanak šav, dast andar mal pat rógn % gāv i apar ātaxš burt, hésm-ic bod vitāp pat x"ēš-tan zahak ké-t pat aš- kamb ‘do not go to the sorcerers, for they cannot heel thee, but go back home, rub thy hand with ox-tallow which has been. set on fire, and burn fragrant fuel for the benefit of thy offspring which is in thy womb’.
3668:šustan [šwstn'; HLLWN-tn ] $öd- [HLL- WN-] to wash, with the prev. apar 41?-1; — with frde: frāc dast ~ hac to wash one’s hands of a p. = to break off all relations with him 3814. 443-9; — with ul 417. — Av. (555) pt. xšusta- ‘liquid’ (from *xšaod-), cf ayo-xšust; MPrth šwstn Swwd-
3703:129-19; the vb. in opt.: framüt ku ~ dast à yamak ... avis üvurt he [HWH-d] that a set of clothes should be brought to him 217-18; — 2. temporal: ~ 6 dat à 7 sülak mat until he attained the age of seven years 1076-2"; ~ 6 han giyāk rasēt ki... 262°; as long as, as far as, with a nominal clause: ~ yazdän hayydr as long as the gods are helpers F:7; — en- larged by other elements: ~ ka, — han % ka until, so that; hamé ~ ka... apar šust always, as long as he was washing 414; 4112-18; with an inf.: kame ~ ka... akür kartan 4215; v. also han-tčit. — Notice the following idioms: im röc 7 mähakän hast täi āpustan hom to-day there are 7 months going on during which I am pregnant = to-day I am in the seventh month of pregnancy 1041-12; 3 rēc apāc but tai pas bē zat three days were left until he was born = three days before his birth 4416; 30 sal būt täi hamäi [thus to be read] raft thirty years elapsed until (= before) he had gone over the whole (creation) 9519-29; ta, € mäh during a whole month 20!?; tāt 3 rēc-šapān ruvān
4031:vat [SLY”; wt' 61%] evil, bad 61%. 7822. 791.2; dast i ~ vāzītan to play the game badly 121'7; more common is the comp. (= sup.) vattar [SLY-tl; 79?! SLY^-tl] worse, the worst, generally used as an emphatic pos. instead of vat (cf veh); hence the sup. vattartom [SLY-tltwm] 7168; vāi i veh... vai i vattar 729-19;
```


## [2026-09-06T02:19:50.419Z] TOOL CALL #66: Bash

```json
{
 "command": "cd data/verification/sources/refs && grep -n \"^zasta-$\\|^zasta-\\|zasta- n\\|zasta-  m\\|zasta-.*'Hand'\" BRT.txt | head -10; echo \"=== find headword lines ===\"; grep -n \"^hazanra\\|^hazayra\\|^hazaöra\\|hazayra-\" BRT.txt | head -10",
 "description": "Bartholomae headwords"
}
```


### [2026-09-06T02:19:51.942Z] TOOL RESULT

```
28005:Ableit.  ans  larjtva-.  —  Pia.:  lanjäi, •  i-,  g.  zasta-,  p,  dasta-  m.  'Hand',  uzw, uÄKnscher  Wesen"';  i)  in  eigentlicher  Be- deutung, von  Menschen  und  Göttern:  in yazaiU  .  .  gaomata  °ta  (IS.)  Yt.y.  50;  — tara%ustrS . .  asünS  'la  draiimnB  V.  ip.  4; 19;  —  mtknm  ..yS ..vazr?m  °taya[lS.) ^draiimnB    Yt. /O.  96;  Y,57.  31,  V.  /p.  ig;
=== find headword lines ===
29679:hazanra-
29737:hazanra.y.
```


## [2026-09-06T02:19:54.133Z] TOOL CALL #67: Bash

```json
{
 "command": "cd data/verification/sources/refs && sed -n '29679,29695p' BRT.txt",
 "description": "Bartholomae hazanra entry"
}
```


### [2026-09-06T02:19:54.190Z] TOOL RESULT

```
hazanra-
1796
voD  iveien  (die  Gä^as)  aufsagt,  ist  nicht r.,  wer  sie  für  eine  Veisammlung  von  dreien au&agt,  ist  r.    Wie  gross  muss  eine  Ver- sammlung  mindestens  sein,    damit   man die  Ji.  befriedigt?    Eine  Versammlung  von dreien."  N.jj. KompE.  —  Zum  V.  'Ani;  eig.  'Siuung'.    — u.  tiUb-d.  n.  'Feier,  Feit';   s.  daia  IFAni.  Ä 15.    —    Pü.:  haHJaman.    —     ')  Der  folgende Text   iit    Dicht   in  OTdnone.    Auch    die   Pü. nicht.     Abweichend  überielit  DsT.  ZA.  3.  99. S.   noch   No.   3  ff.    —    1)   Liei   aratu/f.    — J)  Erginze  rahtfr'.  —  *)  Liei  %Tii.hattnm ;  td.  '
•  j.,  %.  haz- V.  'sich  bemächtigen'.  Praes.  3 sa-%  s  2fli-'';  Pert  i  zaz-^K
i)  'sich  bemächtigen,  in  seinen  Besitz bringen,  gewinnen';  a)  mit  Akk.;  tri- %mttm  xia'hnm  zazaiti  (3SKPA.)''  Yt. 5.  i3o(?).  b)    mit    Lok.:    hanaema(3
*awia{i  POP  A.  Va . .  ^wahml  rafinakl  dary- gäyau  "verdienen  möchten  wir  uns  und  ge- winnen deine  tangdauemde  Unterstützung" Y.  4r.  4;  —  ysi  zciantl''>  vanAäu  sravaAi "die  sich  einen  guten  Leumund  erwerben" Y.^.  10;  —  xa*ji>  (NS.)  6uyi'>  va^hüvca müde  vanhauca  sravahe  urunaiia  darrte havanhe  "damit  ich  mir  den  guten  Vor- teil erwerbe  und  . ."  A.  /.  1 1 ;  —  fUSit iahmi  sazva  (NS.)  yö  nBil  urune  xasva "nichts  hat  gewoimen,  wer  (es)  nicht  für seine  Seele  gewonnen  hatf'  FrD.^*>;  — nSit  cahmi  *zatus^  (NS.)  yS  nSii  *urune *tä3ui^>    FrD.^".  2)    absolut    'im
Kampf  gewinnen,  den  Sieg  davontragen': ya^a  U  vtspe  aurvania  xazvävÄa  (liF.) paiti.jasqn  ydka  (Sp.  1 243  o.) . .  vistäspahe YL  5.  13a»);  —  «ae»/a  (LP.)  vupaisu vanhusu  tazusu  vlspaUu  aiff.eihralsu P.  27.
Ü.  sähate ,  sähvan ;  gr.  a%if,  'tX"'  —  ^"-  ■ gri/ian ,  gri/tär  Ulan  -  eiL :  ö  j'ii  iartan  -, (ru  Y.  41):  sinävttndetälan  -  Sü. :  sädkaTtayi- tuM,  —  >)  S  51-  2.  lOi  L  1  mit  No.  a,  311, 313.  9,  Jjolb;  Bgm.  Grdr.»/.  558,  BN.Stud. /.  397.  —  >)  Thom.  —  3)  Man  könnte  natür- lich auch  einen  Stamm  vaa-  anietien,  s.  va- vana:  Zu  Y.  6i.  6  sind  die  WStter  in  NA. ^schlich  verbunden.  —  *)  Vgl.  iSt,  Mx.  /.  a8. —  M  So  nach  der  Var,  —  *)  Hds.  Jaiu}.  — ?)  Scheint  nur  eine  Variante  des  vorherg. Satzes  zu  sein.  Pü.  hat  freilich  für  xaxva grift,  für  M3w/  dagegen,  das  DsT.  ZA,  ^.  IJI für  einen  Aorist  sa-m-i  halt,  sirit.  —  ä)  VgL Y.  57.  12  unter  gam-  mit  paiS.
*  %■  (•  jO  ha-zao6a-  Adj.  'gleichen  Willens, gleichgewillt  mit  — '  (Instr.):  vahistfm  '^wä vahiitä   ySm    aiä    vahtstä    'Am    ahunm
".  .  dich,  o  bester,  den  mit  dem  besten A.  gleichgewillten  Ah."  Y.  21?.  8 ;  —  ahuri . .  ala  'SB  masdä  "AAM.,  der  mit  A.  gleich- gewillte"  V.2p.  7;  —  tat  vS  nS  'iäoha (VP.)  vUpänkB  daidyäi  savB  "diesen  euren Nutzen  sollt  ihr  uns  gewähren,  ihr  gleich- gewillten (Götter)  alle"  Y.5/.  20.
KompE.  —    aL  laj'ifa-  Adj.  —    Pü. :  fia  ikam
äBÜitilh.
•  j,  yim  vä  ainim  *Ad6B^al%a  (sd.) "hazaoäyä  paanha"  layqn  N.  /.
Pü. ;  undeutlich.  Vll. :  pa  dSHSn  -  pa  kämak  - i  ^eJ  u  S/räi  -  dastatoarih  -  1  öiän  i  haat- trätarän  i  apärllan  d.  i-  "auf  seinen  eignen Wunsch  (WUlen)  und  mit  Genehmigung  (Be> votlmächtigung)  der  andern  Genossen".  Da- nach vll.  kva  toBsa  uta  iänha'1  zu  lesen').  — ')  Ai.  Jäia-  m.,  vgl.  jämä-,  wofür  Npft. ämüxtuH  hat,  ebenso  wie  für  öfräs,  die  Ubier- setzung von  "paiaha  c=  sin/vi,  in  Mx.  — >)  Anders  HoKN  KZ.  34.  5S3.
•  j.  hazanra-  neutr.  Zw.  'tausend':  hist^nti .  .  yazalänhs  iattmla  'rtmca  YL  Ö,  i ;  — yä  .  .  paica  vazinti  xsvai  tatäü  •rtm'a Yt  5.  95.  a)  mit  Gen.:  ydi^a  'nrn narqm  "Htm  nartm  arwyaxiaySit  Yt  /.  1 9 ; Ä  55,  io.  69,  128-131*,  Y.65.  4';— _yaäa na  satimca  "tfmca  baivanca  *parsanqm ''ni/abmlsd.)  Ayät \t  13.  JI -,3.31,  63,  120, Ä4S-5-3.  10,  JO.82,  A.J.7-11*,  V.J.31, 37',  /A'.  70-73»,  74'',  2/.  7,  22.3-4,*,  Y. 6S.1S,  N.42',  H./.s,sVar.,  10;  —  'rai (ab  Gen.)  bar>sna  vlranqm  YL  5.  96; £49;  —  'r»m  (statt  Instr.)  ha<ia.cikanqm (sd.)  V.4-ioi  —  y^ /"""i  fl^q^t  daei-a- nqm  'rai  'rB  pairi  Yt_j.  10  •';  4.  2  ",  Vyt ig'K  a)  mit attrib. Einerzahlen:  ioiitfa- rasca  a^a  garayB  . .  ca'^aiargsatfm{sd.)/a
.dvaiea  satte  dvaica  =«  (ND.)  Yt/p.  7; '  —  nava^a  yaskS  navailisca  navaca  sata j  navaca  'ra  navas!s{sd.)ia  baivqn  V.  22.  3; !  Ytij-sg.  i)mAGK^\duyfrevpap€tnam j  V.  7tf.  73;  73%  Vd.  6  (-rohe).  b)  adjekt i  gebraucht:  ha'^ra  . .  yasata^byO  . .  panäx- \saiblica  laiaisca  'räiS^a  batvanbls^a  Vr. ,8.\;  —  'nm  vq%wh  bavatti  YLj<S'.5";5*'; I  —  'nmyanm  Vytf"; — 'raw^alsNom.) I  sünXs  strX.nSmanS  'räis  sunit  nairyS.- .itämanB  V.  y,  51;  14.1';  —  *rw«  (als I  Gen.)  narqm  .  .  taoxma  ,  .  xiva^  lata  . . tisrB  sata  (sd.)  V.  2. 30.
KompA.,  E.;  Ableit.  —  ai.  sahätra'  n.,  np. kiuär.  —  Pü. :  tOOO.  —  ')  Wo  'um  statt  duye •rt  lu  lesen.  Die  Abschreiber  haben  den Wechsel  von  V.  18.  73  auf  74  übertrafen.  — 1}  Werllose  Stellen.
```


## [2026-09-06T02:19:59.223Z] TOOL CALL #68: Bash

```json
{
 "command": "cd data/verification/sources/refs && sed -n '27995,28010p' BRT.txt | cat -n",
 "description": "Bartholomae zasta column"
}
```


### [2026-09-06T02:19:59.294Z] TOOL RESULT

```
     1	daxHanya  (sd.)  Yt.  10. 39.
     2	Ableit.    —    VrL   mars.,    «ab.    hemat   *sai»';
     3	vonPi.anta  OUCr.  /.  439.  ^-  S9i.  —  Pu.  (lu
     4	V.  8.  8);   lOBfO,    (zu  V.  8.  Io)i    iattghi.  -
     5	>)    Oeschr.    krba  —^  sai  *Hund'{l)i    s.  DsT.
     6	ZA.  2.  iza
     7	•  j.  zarätvaena-  i)  Adj.  (fem.  *nr-)  'aus Stein':  yezi  anhat  zar/naiai/ (sd.)  . .  'ms
     8	Uiflitized  by  VjOOQ  IC
     9	1685  zasta-
    10	(NSf.)  V.  7. 74f.  2)  D.  ein  aus  Stein bestehender  Gegenstand:  ait?m  irishtn  m- dar>saym  (sd.)  .  .  ayaahatmm  (sd.)  vä °ti»n  vä  ".  .  ein  Stück  Eisen  oder  ein Stein"  V.  6. 46.
    11	Ableit.  ans  larjtva-.  —  Pia.:  lanjäi, •  i-,  g.  zasta-,  p,  dasta-  m.  'Hand',  uzw, uÄKnscher  Wesen"';  i)  in  eigentlicher  Be- deutung, von  Menschen  und  Göttern:  in yazaiU  .  .  gaomata  °ta  (IS.)  Yt.y.  50;  — tara%ustrS . .  asünS  'la  draiimnB  V.  ip.  4; 19;  —  mtknm  ..yS ..vazr?m  °taya[lS.) ^draiimnB    Yt. /O.  96;  Y,57.  31,  V.  /p.  ig;
    12	—  hyat  ta  ua  (IS.)  yä  ia  Äa/st(sd.)  .  . Y.  43.  4;  —  vom  göttlich  gedachten  Ur- rinderpaar:  at  vä  ustänäü  ahvä  °tsil  frl- fumna  (sd.)  .  .  mJ  urvä  gJuscä  azyi  Y, 2(J,  5;  —  sonst  Du.:  'la  (AD.)  Ar., frainütaystt  V.Ä40,  i6.-},  iS.ic,;  ^".40', g.  49,  18.  19,  Y.  (»2.8,  F.Jg,  20,  yyt.31;
    13	—  aoa  Stars  'ta  paiti  apa.g3urvayat  Yl //7.48i  —  yat  *haima  (sd.)  'iff  (AD.)  .  . miiamt  V.  5. 59;  —  ava  paZo  ava  'ts {AD.)  .  .Järayalw?m  Vr. /j.  i;  Yt,  y.  147;
    14	—  pä\aiibya  .  .  -toiibya  V.  5.  1 1 ;  — palnubya  ..  'taiibya  V.  2.  31;  ö".  29,  4".  40, s8.  19,  A.  4-  5.  Yd,  72;  —  Äiiz'fl  mrBihi hsxtim  . .  *°tagibya  variza  kvarltjm  Syao- 'kmm  Aog.  söf.;  —  manaahasca  *humaiti hisvasca  *häxii  'iayas{LS.)'Va  *hvarsii P.  2c?.  a)  gAw.  ID.  sva.  'durch  Handeln, Tun' 3':  at  yJ  aktm  dngvSitl  vacankä  vü ai  vä  manatskä  'tsibyä  va  vanlaitl  "wer aber  dem  Zlrv^enossen  mit  Worten  oder mit  Gedanken  oder  mit  seiner  Hände Werk  Übles  tut"  Y.  jj.  2.  et)  in  Ver- bindung mit  Syaö^ana-.  vahistim  hisvä uxiäi/. .  Sfdnä  . .  'tSibyä  syaö^anä  vimyat (Sp.  1377  0.)  Y.47-  2.  b)  Pv  gAw.  Lok! (Sg.  oder  Du.)  mit  V.  da-  oder  'kar-  'alicui (Dat,  Gen.)  in  manu  ponere':  'pasavJ'- di/  a*ura''rnasdä  manS  'tays  (LS.)''  aku- naui  "dann  gab  sie  AM.  in  meine  Hand" Bh.  4.  4;  —  kdka  asäi  drupm  dyam  "tayd (LD.)  "ob  ich  wohl  dem  A.  (dem  Reich der  Wahrheit)  die  Dr.  (das  Reich  der Lüge)  in  dieHände  liefern  kann?"  \.4.4. 1 4; jo.  85'.  2)  übertr.,  von  den  Klauen des  Ebers  (nur  Komp.).  1
    15	KoinpA. {sasts-, las/d;  HD.),  E. ;  Ableit,  —  ai.  . käsSa-  in.,  np.  äasl.  —  Po, :  dait,  har  a  dost.  — >)  Im  GcgenE.  la  4f  iTC^,  id.  No.l.  —  >)  Zweifel- haft, s.  S  32;  No.  nnd  hiiü-  No.  6.  —  J)  S.  | läaiä,  kiaiä,  AiaitS  unter  Uta-  t.  —  4)  FaUcb  '
    16	^za8t5.niaza-
```


## [2026-09-06T02:20:11.208Z] TOOL CALL #69: Bash

```json
{
 "command": "ls site/pages/191.jpg 2>/dev/null; pdftoppm -f 191 -l 191 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg191 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 191"
}
```


### [2026-09-06T02:20:13.317Z] TOOL RESULT

```
site/pages/191.jpg
total 26360
drwx------ 2 sfmqrb sfmqrb   12288 Sep  5 22:20 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   68775 Sep  5 16:43 ary440.png
-rw-rw-r-- 1 sfmqrb sfmqrb  752374 Sep  5 16:12 bqt362_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  624515 Sep  5 16:12 bqt362.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 1032029 Sep  5 16:13 bqt362_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  385716 Sep  5 16:13 bqt363_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  338175 Sep  5 16:13 bqt363_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  692415 Sep  5 16:13 bqt363.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  100925 Sep  5 16:52 bqt_pdf600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62948 Sep  5 16:36 build134.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50861 Sep  5 16:34 build148b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17908 Sep  5 16:44 build151a.py
-rw-rw-r-- 1 sfmqrb sfmqrb   15986 Sep  5 16:46 build151b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11172 Sep  5 16:47 build151c.py
-rw-rw-r-- 1 sfmqrb sfmqrb   19592 Sep  5 16:50 build151d.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6433 Sep  5 16:50 build151z.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51529 Sep  5 16:51 build152.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51266 Sep  5 16:51 build154.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61639 Sep  5 16:53 build155.py
-rw-rw-r-- 1 sfmqrb sfmqrb   70485 Sep  5 16:53 build156.py
-rw-rw-r-- 1 sfmqrb sfmqrb   72953 Sep  5 16:48 build158.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74140 Sep  5 16:56 build160.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53286 Sep  5 16:55 build161.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67253 Sep  5 16:56 build162.py
-rw-rw-r-- 1 sfmqrb sfmqrb   45662 Sep  5 16:49 build164.py
-rw-rw-r-- 1 sfmqrb sfmqrb   82221 Sep  5 16:56 build168.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53542 Sep  5 16:57 build169.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58105 Sep  5 17:02 build171.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51583 Sep  5 17:08 build173.py
-rw-rw-r-- 1 sfmqrb sfmqrb   59926 Sep  5 17:11 build174.py
-rw-rw-r-- 1 sfmqrb sfmqrb   64448 Sep  5 17:12 build175.py
-rw-rw-r-- 1 sfmqrb sfmqrb   69033 Sep  5 17:13 build177.py
-rw-rw-r-- 1 sfmqrb sfmqrb   75374 Sep  5 17:12 build180.py
-rw-rw-r-- 1 sfmqrb sfmqrb   43965 Sep  5 17:11 build181.py
-rw-rw-r-- 1 sfmqrb sfmqrb   64481 Sep  5 17:11 build182.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47920 Sep  5 17:11 build183.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62604 Sep  5 17:16 build184.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63773 Sep  5 17:17 build186.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62923 Sep  5 22:13 build189.py
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5391 Sep  5 17:02 g2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2929 Sep  5 17:02 g3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5607 Sep  5 17:02 g4.png
-rw-rw-r-- 1 sfmqrb sfmqrb  163996 Sep  5 16:46 gar2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124975 Sep  5 16:47 gar3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77205 Sep  5 16:46 gar.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14924 Sep  5 17:01 geus_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10247 Sep  5 17:01 ghaido_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4197 Sep  5 17:01 ghaido_low.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3536 Sep  5 17:04 jang.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     310 Sep  5 22:16 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57696 Sep  5 16:46 mk153.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49505 Sep  5 16:50 mk157.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56703 Sep  5 16:54 mk166.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61790 Sep  5 16:57 mk167.py
-rw-rw-r-- 1 sfmqrb sfmqrb   30384 Sep  5 16:51 mk170.py
-rw-rw-r-- 1 sfmqrb sfmqrb   84301 Sep  5 17:17 mk176.py
-rw-rw-r-- 1 sfmqrb sfmqrb   68808 Sep  5 17:15 mk178.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4344 Sep  5 16:49 n12b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3969 Sep  5 16:49 n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24939 Sep  5 17:01 n14.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2692 Sep  5 16:49 n16.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3293 Sep  5 17:01 n17b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   17771 Sep  5 17:01 n17c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6463 Sep  5 17:01 n17.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7472 Sep  5 17:01 n19.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3278 Sep  5 17:01 n5b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2334 Sep  5 17:01 n5c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3215 Sep  5 17:01 n5.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35268 Sep  5 16:59 p162a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14337 Sep  5 16:59 p162b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:59 p162.png
-rw-rw-r-- 1 sfmqrb sfmqrb   41788 Sep  5 16:53 p173_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32898 Sep  5 16:53 p173_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161412 Sep  5 17:01 p174hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  173427 Sep  5 17:01 p176hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2762 Sep  5 17:02 p189_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24596 Sep  5 17:02 p189_greek2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   20222 Sep  5 17:02 p189_khoris.png
-rw-rw-r-- 1 sfmqrb sfmqrb   33994 Sep  5 17:02 p189_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1688 Sep  5 22:17 p190_eb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1093 Sep  5 22:17 p190_emptybox.png
-rw-rw-r-- 1 sfmqrb sfmqrb  102711 Sep  5 22:17 p190hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5540 Sep  5 22:17 p190_skt.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:52 p600_350.png
-rw-rw-r-- 1 sfmqrb sfmqrb  139701 Sep  5 16:52 p600_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  183909 Sep  5 16:52 p600_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1717 Sep  5 16:52 p600_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5162 Sep  5 16:52 p600_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1189 Sep  5 16:57 p600_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17147 Sep  5 16:44 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb   15703 Sep  5 16:46 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10974 Sep  5 16:47 part_c.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19420 Sep  5 16:50 part_d.json
-rw-rw-r-- 1 sfmqrb sfmqrb   53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80793 Sep  5 16:15 pg131.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46793 Sep  5 16:20 pg133.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66991 Sep  5 16:16 pg135.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45014 Sep  5 16:12 pg137.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63658 Sep  5 16:13 pg144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60631 Sep  5 16:11 pg147.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81770 Sep  5 16:20 pg148.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72186 Sep  5 16:30 pg149.png
-rw-rw-r-- 1 sfmqrb sfmqrb  131595 Sep  5 16:32 pg151_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154426 Sep  5 16:36 pg152_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62516 Sep  5 16:35 pg152.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb  101504 Sep  5 16:43 pg156.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169880 Sep  5 16:34 pg158_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168057 Sep  5 16:34 pg161_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76745 Sep  5 16:34 pg161.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110270 Sep  5 16:42 pg162_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:42 pg162.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8523 Sep  5 16:42 pg162_verse.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61265 Sep  5 16:40 pg165.png
-rw-rw-r-- 1 sfmqrb sfmqrb  116877 Sep  5 16:46 pg167.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68420 Sep  5 16:42 pg169.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37351 Sep  5 16:44 pg170.png
-rw-rw-r-- 1 sfmqrb sfmqrb  120612 Sep  5 16:49 pg171_450.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73551 Sep  5 16:43 pg171.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73400 Sep  5 16:56 pg172.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52970 Sep  5 16:53 pg173.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70664 Sep  5 17:00 pg174.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54907 Sep  5 16:54 pg175.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83583 Sep  5 17:00 pg176.png
-rw-rw-r-- 1 sfmqrb sfmqrb   88207 Sep  5 17:02 pg177.png
-rw-rw-r-- 1 sfmqrb sfmqrb   98352 Sep  5 17:01 pg178_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64024 Sep  5 17:01 pg178.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57139 Sep  5 16:54 pg179.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81598 Sep  5 16:58 pg180.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56794 Sep  5 17:00 pg181.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66020 Sep  5 17:01 pg182.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53414 Sep  5 17:03 pg183.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77310 Sep  5 16:58 pg184.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79537 Sep  5 17:09 pg185.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72425 Sep  5 17:08 pg186.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53749 Sep  5 17:02 pg187.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77516 Sep  5 17:01 pg189.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65970 Sep  5 22:17 pg190.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78016 Sep  5 22:20 pg191.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71828 Sep  5 22:17 pg192.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78587 Sep  5 22:19 pg199.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75609 Sep  5 22:18 pg203.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  561602 Sep  5 16:57 t598.png
-rw-rw-r-- 1 sfmqrb sfmqrb  632359 Sep  5 16:57 t599.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:57 t600.png
-rw-rw-r-- 1 sfmqrb sfmqrb  545905 Sep  5 16:57 t601.png
-rw-rw-r-- 1 sfmqrb sfmqrb       0 Sep  5 22:19 tad60.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top598.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top599.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top601.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24918 Sep  5 16:58 tops2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  5 16:57 tops.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
-rw-rw-r-- 1 sfmqrb sfmqrb     738 Sep  5 17:04 xang.txt
```


## [2026-09-06T02:20:16.211Z] TOOL CALL #70: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg191.png"
}
```


### [2026-09-06T02:20:16.747Z] TOOL RESULT

```

```


## [2026-09-06T02:20:16.739Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T02:20:36.620Z] TOOL CALL #71: Bash

```json
{
 "command": "cd data/verification/sources/refs && grep -n \"آستین\\|آستن\\|آستیم\" BQT_v1_pages.txt | head -20",
 "description": "BQT vol1 astin variants"
}
```


### [2026-09-06T02:20:36.672Z] TOOL RESULT

```
1002:میگریانید . یس‌از آستین طنبوری‌بر آورد وچنم‌میغواند : ابااین‌تیمار باید
4157:آزمودن »]زوری » آسان »]سایش »آستانه » آستین » آسودن؛ [سیابان»
5983:آستن » بارچةٌ جامه را گوین که بدن مرده را
7842:اسقی » بر وزن راستی » بمعنی آستن
7843:است که مخفف آستن (۱) باشد.
7844:] سقیم » با میم» بروزن و معنی آستین
7861:آستین فشافدن - بسنی آنتین
11942:استیم » بنتع اول بروزن تسلیم. آستین
13845:گوبند . چه هرگاه در زیر زنان آستن دود
13848:بوفت جماع بخود بر گیرد آستن قود.. گو یف
15066:زده ۰ آستن جامه راگونند - و بمشی خون
15089:۵ م رك : اوستم . ۱ -رك : آستیم و استیم . ۷ رك : سو که
16898:باشتبن بروزن آستین» باری ومیوه‌ای
29731:که قبای آستن کوغاه پیش واز باشد .
30622:وبکسراول وفتحثالی‌جامة پیش‌واز وآستین کوتامرا +کاف . میوه ای بود شبیه بشفتالو - و نم اول
```


## [2026-09-06T02:20:45.473Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%DA%A9%DB%8C%D9%84%D9%88",
 "prompt": "What does Mo'in's dictionary (فرهنگ معین) say for کیلو — origin tag (e.g. [فر.]) and definition? Quote it."
}
```


## [2026-09-06T02:20:48.068Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%DB%8C%D9%84/",
 "prompt": "In the فرهنگ معین section, what entries are given for میل — list the origin tags (e.g. [ع.], [فر.], [یو.]) and glosses, especially any meaning 'mile' or 'road marker/tower' (ستون، مناره، نشانه راه)."
}
```


### [2026-09-06T02:20:49.328Z] TOOL RESULT

```
According to Mo'in's dictionary, the entry for کیلو includes:

**Origin tag:** [فر.] (abbreviated for French)

**Definition:** "به معنی هزار است و برای تعیین واحدهای دستگاه متری به کار می رود" — meaning it denotes one thousand and is used to specify units of the metric system, with examples given as kilogram and kilometer.
```


### [2026-09-06T02:20:56.091Z] TOOL RESULT

```
# میل entries in فرهنگ معین

According to the dictionary section, the entries for میل are:

**Origin tags and definitions:**

1. **[ع.] (اِ.)** – "۱ - سیخ فلزی . ۲ - یکی از ادوات ورزش باستانی که از چوب ساخته می شود" (a metal rod; one of ancient athletic tools made from wood)

2. **(مِ) [ع.] (اِ ص .)** – "۱ - خمیدن . ۲ - برگردیدن . ۳ - رغبت ، آرزو" (to bend; to turn; desire, wish)

The section does not contain entries specifically labeled for "mile" or "road marker/tower" (ستون، مناره، نشانه راه). Those architectural and measurement meanings appear in other dictionary sections like فرهنگ عمید and دانشنامه آزاد فارسی, but not in the فرهنگ معین excerpt provided.
```


## [2026-09-06T02:21:10.271Z] TOOL CALL #74: Bash

```json
{
 "command": "cd data/verification/sources/refs && echo \"==SKT mile==\"; grep -n \"^MILE\\|^MILE,\" SKT.txt | head -3; echo \"==KLN kilo==\"; grep -n \"kilo-,\\|kilogram,\" KLN_1966.txt | head -3; echo \"==SYN thousand==\"; grep -n \"13\\.13\\|Thousand\" SYN.txt | head -10",
 "description": "Skeat, Klein kilo, Buck thousand"
}
```


### [2026-09-06T02:21:10.361Z] TOOL RESULT

```
==SKT mile==
==KLN kilo==
20682:kilo-,  combining  form  meaning  ‘one  thousand’. —  F.  kilo-,  fr.  Gk.  yt'/.ior.  (Ion.  y^ioi),  ‘a thousand’,  which  is  of  uncertain  origin.  It  is perh.  cogn.  with  L.  mille,  ‘a  thousand  ;  see
20685:kilogram,  kilogramme,  n.  —  F.  kilogramme,  lit. ‘one  thousand  grams’,  coined  fr.  kilo-  and  gram, ‘the  metric  unit  of  weight’, kiloliter,  kilolitre,  n.  —  F.  kilolitre,  lit.  ‘one thousand  liters',  coined  fr.  kilo-  and  liter, kilometer,  kilometre,  n.  —  F.  kilometre,  lit.  ‘one thousand  meters’,  coined  fr.  kilo-  and  Gk. [jirpov,  ‘measure’.  See  -meter.
29345:poignant,  adj.  —  ME.  poinaunt,  fr.  OF.  (=  F.) poignant,  pres.  part,  of  poindre,  ‘to  prick,  sting’, fr.  L.  pungere.  See  point,  v.,  and  cp.  pungent. Derivative:  poignant-ly,  adv. poikilo-,  before  a  vowel  poikil-.  —  A  var.  spelling of  poecilo-,  poecil-.
==SYN thousand==
23353:13.13 WHOLE
23429:13.13 WHOLE
28759:Goth. aljan (renders fos as ‘jeal- ousy’, Rom. 13.13, otherwise ‘zeal’) = ON eljan ‘energy, endurance’, OE ellen ‘strength, vigor, courage’, OHG ellen ‘zeal, strength’, etc., etym. dub., perh. : Lat. alacer ‘lively, eager, glad’. Walde- P. 1.156. Falk-Torp 188. Feist 38. Walde-H. 1.25.
```


## [2026-09-06T02:21:11.667Z] TOOL CALL #75: Bash

```json
{
 "command": "cd data/verification/sources/refs && echo \"==LKT==\"; grep -n -i \"mille\\|Meile\" LKT.txt | head -10; echo \"==PLA==\"; grep -n \"mīl\\|ميل\" PLA.txt 2>/dev/null | head -10; ls PLA* 2>/dev/null",
 "description": "Lokotsch and Asbaghi"
}
```


### [2026-09-06T02:21:11.724Z] TOOL RESULT

```
Exit code 1
==LKT==
319:[Aus  syr.  'akar  kärhä  ZDUG  XLVI,  258] eine  Kamillenart  Anthemis  pyrethrum; über  das  tk.  wurde  hieraus  wohl  runi. cärcü,  cäräu  'echter  Bertram,  Speichel- wurzel'.
704:Hieraus  angloind.  hungalow,  die  ge- bräuchlichste Art  Häuser,  welche  Euro- päer im  Innern  Indiens  bewohnen.  Sie bestehen  nur  aus  einem  Stockwerk  und sind  mit  einem  pyramidalen  Dach  ver- sehen, das  gewöhnlich  mit  Stroh,  manch- mal mit  Ziegeln  gedeckt  ist.  Gegensatz dazu  puckahouse  [s.  hier  Nr.  1614].  — Mit  hind.  däk  'Post,  Relais  von  Pferden u.  Leuten,  auch  Briefpost'  verbunden, ergibt  sich  angloind.  daw-Oungalow,  ein Rasthaus  zur  Bequemlichkeit  der  Rei- senden, das  früher  und  z.  T.  auch  jetzt noch  von  der  indischen  Regierung  unter- halten wird.  Einfach  eingerichtet,  ent- halten sie  doch  alles  Wesenthche  für die  Bedürfnisse  des  Reisenden,  auch einen  Diener,  der  für  mäßigen  Preis Nahrung  liefert.  Sie  sind  entweder  in Abständen  von  10  bis  15  engl.  Meilen, so  daß  ein  Tagesmarsch  ohne  Mitnahme eines  Zeltes  erfolgen  kann,  oder  von 40  bis  50  Meilen  angelegt,  die  in  einer Nacht  von  Palankinträgern  durchlaufen werden  können.  [Hobson-Jobson  128/1 29. 299/300.
1249:Auch  bind,  'ein  Hügel,  Erdwall  oder erhöhte  Batterie',  als  n.  pr.  in  Bengalen Namen  einer  militärischen  Niederlassung, 4V2  engl.  Meilen  nordwestlich  von  Cal- cutta,  die  70  Jahre  lang  (1783—1853) Hauptquartier  des  berühmten  Korps  der bengalischen  Artillerie  war.  Im  dortigen Arsenale  wurden  zuerst  mit  stumpfem Vorderende  versehene,  daher  stark  zer- reißende Geschosse  liergestellt,  die  man engl,  dum-dum,  dtsch.  Dimidumgeschosse nennt.    [Hobson-Jobson  330.
1848:Eine  Labiate,  die  nicht  genau  definiert ist:  'Basihkkraut,  Majoran,  Kamille, AVasserminze' ;  hieraus  sp.  alfabega,  al- habega,  alabega,  albaheca,  kat.  alfäbrega, frz.  fabregue  'Basilikenkraut'  [mit  ad- ventivem r  wie  in  sp.  pg,  marlota,  hier Nr.  1380,  sp.  alferce,  hier  Nr.  597,  und öfter].  [Devic  DEt  113/4.  Lammens Rem  109/110.
2518:'Hoher  Berg',  N.  pr.,  ein  Berg,  der  we- nige Meilen  nordwestlich  von  der  Stadt King-te-chen  (290  gg'  n.  Br.,  1"  10'  ö.  L. von  Peking)  liegt.  Hier  wurden  große Mengen  einer  besonderen  Art  Feldspats als  Rohmaterial  für  die  Porzellanher- stellung gewonnen.  Eine  Beschreibung der  grofäen  Fabrikstadt  K.  gab  zuerst P.  D'ENTRECOLLES,  der  sie  im  Jahre 1712  besuchte.  Aus  dem  Namen  des Berges  ^vurde  frz.  caolin,  dtsch.  Kaolin, engl,  kaolin  'Porzellanerde'.  [Hirth  Chin FW  206/^07.
2817:'Kohle,  Holzkohle'  [Stamm  k'dj  'brennen, glühen,  Glut,  Brand',  also  *küjmiir 'Brennmaterial',  Vämbery  TktEtWb S.  105,  Nr.  116];  hieraus  bulg.  k'iimur., k'imur  'Kohle',  kiimurica  'Kohlenmeiler', serb.  cumur  'Kohle'.  [Bern  SiEtWb  681.
4692:2093.  Tk.  torluk: 'Kohlenmeiler'  [Kelekian  Kämüs  815  a;- vom  gleichen  Stamme  wie  hier  Nr.  2092, eigentlich   'das  Aufgestellte'];  hieraus rum.  turluc  'dass.'.
==PLA==
(eval):1: no matches found: PLA*
```


## [2026-09-06T02:21:17.660Z] TOOL CALL #76: Bash

```json
{
 "command": "cd data/verification/sources/refs && echo \"==SYN mille==\"; grep -n \"sahasra\\|χίλιοι\\|khilioi\\|'thousand'\" SYN.txt | head -10; echo \"==SKT format==\"; grep -n -i \"mile\" SKT.txt | head -5",
 "description": "Buck and Skeat searches"
}
```


### [2026-09-06T02:21:17.732Z] TOOL RESULT

```
==SYN mille==
24190:Av. visaitivant- ‘twenty fold’, deriv. of visaiti ‘twenty’ with suffix -vant- (so éabwarasapwant- ‘forty fold’, paricéasaé- want ‘fifty fold’, etc., long series in Yt. 10.116). Cf. Ved. catavant, sahasravant- in similar use.
==SKT format==
1428:Bamaole  (1),  a  kind  of  goose.  (Low L.  — C.  'i)  Dmiin.  from  F.  bttttaqtu  (Cot.), Liiw  L.  bermua.  *  Bernaca,  aues  aucis palu^tribus  similes;'  Ducange.  Used  by Giraldus  Catubrcnsis,  and  presumably  of Celtic  origin.  (Sec  Max  Miillcr,  Lecturef, tnd  Series.)
1887:KinaD  buMile  or  blister. tr,  a  bultMe  nn  waier ;
2692:camlet,    a    «tuft.     ^Arah )      Formerly fdm^^/.supposedto  be  named  from  coittAin- iiiK  iitmel's  nair.    Really  iVoro  Arab,  kham^ /at,  khamalat,  camlet;  Kicb-  Diet  p.  c'ljs. Camellia.    (Personal   name.)     A   plant named  after  Geo.  Jos.  Kamcl,  a  Moravian Jesuit,   who    dt'&cjibed   the    plants    Ui   the ishuid  of  Liuon. Camelopard :  see  CameL Cameo.  (Ital.)     Ital.  cammeo,  a  cameo, piecious  stune  carved  ic  relief.     Origin  tin* known. Camera.  (L.)     L.  camera,,  a  chamber; hence  camera  odsatra.  a  dork  chamber,  box for  photography  ;  see  Chamber. Camlet ;  see  CameL Camomile ;  .%ec  Chamomile. Camp.  (L.)     We  find  F.  camp  (Cot.)  ; bnt  the  E.  word   was  prob.  taken  directly from  L.  eamfus.  a  field,  ground  held  by  an army.  +  Gk.  w^»o»,  a  garden.
6216:fac-Btmile.  (L.>  Shurt  for  ft simile,  made  like  L.>^/wM,  neuLOf^ o(facert,  to  make ;  simi/e*  ncul.  of  siMihSf like ;  see  Similar.
7233:furlong,  ^ih  of  n  mile.  (K.)  A.S  fur- htij;,  orijj.  a  furrow-long,  or  the  length  of  a liirrow,  —  A.  S./urA,  a  iurrow  ;  i'an^,  lon^.
```


## [2026-09-06T02:21:23.778Z] TOOL CALL #77: Bash

```json
{
 "command": "cd data/verification/sources/refs && grep -n \"Mile\\.\\|Mile,\" SKT.txt | head -5; echo ---; grep -n \"milia\\|mille\" SKT.txt | head -8",
 "description": "Skeat mile entry"
}
```


### [2026-09-06T02:21:23.854Z] TOOL RESULT

```
14721:Mile,  adapled  for  piping.  (L.) rith  suffix  'iU  ^L.  -ilii)  (rom  L. /,  pp.  of  prehcndirt,  prttiden,  to jf.  •»  L.  /r(f ,  before ;  obsolete  A/m- rasp,  oogT-.atc  with  E.  0«t.  q.  v. bend.  ^L.)  L.  apprtfundere, mj  hold  of.^L.  ap-  {ad)f  to,  at; 1^  to  gi^sp  (above). "Ice.  (F.  — L.)  From  a  dia- I,  snch    as  the  Walloon  ap-
15843:5*1 ;  icc  r«Ral  (above). Mile.  «b.  (K-L)  M.  E.  reuU,  riwle.^ F.  riuit^  rtult  (F.  rtgft).^L,  riguia,  a ■*.  — L  rtgert,  to  rule. ■ortle.  (F.  -  L.)  F.  «frtV,  a  going tti;  fern.  o(  sflrfi,  pp.  ci  soriir,  to  sally tiL  Cr  Span,  ndrtta'a,  a  sortie,  from  O. Mirtir,  to  rtse  fl.  F.  wrtVr.  Sjinn. pocwer  to  a  Low  L  ionn  mrruttft*. 1^  —  L.  rurrtttum,  supine  of riae  «p;  tec  aorge   (below).
---
2714:coddle.  (E.)  Put  for  f(»iiM//,  frequent, form  of  M.  E.  ku\^n  {kuihtkfn\  to  be familiar,  embrace.  — A.  S.  kUti,  known,  fa- miliar; !.ee  Can,  5  Y-
5283:DoU  (Du.  or  Gk,)  (1)  Pcrhaoi  from O.  Du.  dol.  a  whippinff  top:  Dn  dolUn.  to sport,  be  frolicsome,  I  fence  perhaps 'a  plav- Ihing.'  See  dally,  onder  Dwell,  (a)  Other- wile,  from  Dell,  for  Dorothy  \  %  familiar name,  of  Gk.  origin.    %  History  obscure.
5567:donkey.  (C)   Double  diiaia.  wtik fix  •Jt-iy  [  -Lowl.  So.  -idk'ii,  u  \ ickie,  a  little  little   hoisc,   tlanHab. duH,  familiar  name  for  a  hone,  fl colour  (Koiiico,  t.  4.  41).    ^  So  I don  ek,  a  hedge-sparrow,  ^m  it»
8731:w  a  familiar  invitation
8954:humiliate.  {L. )  From  pp.  of  L. kttmn'mre,  to  btunble.  — L.  ^«/ni/i>f  hiunble ',ab«:>\e).
8963:Humiliate,  Humility;  sec  Humble.
10081:eldpe,  to  run  away.  (Du.)  From  Dn. amtloifpen^  to  evade,  elope,  run  away ;  by substituting  the  familiar  prefix  e-  for  Du. ont-.  This  prefix  •  G.  ent-  =  A.  S.  and-  \ see  Anawer.  Dn.  loosen,  to  ran.  is  cog- nate with  leap  (above).
10879:mademoiaelle,  miss.  (F,  -  L )  F. ma,  my;  dtmoiselle,  riamitel  ;  see  Damsel, madonna.mylady.  U^bI*-!'-)  Ital.wa. my;  donna^  laHy.fiomL.  i/i?wma;  see  Dame. monkey,  an  ape.  (ItAl.~L.)  Corrapted from  O.  Ital.  nwHuchw,  'a  pugge.  a  mun- kie.  an  ape  ; '  Florio.  Dimin.  of  O.  Ilal. mono,  monna,  'an  ape,  a  munkte.  a  mun- kie-face;  also  a  nickname  for  women,  as we  say  gammer,  goodie ;  *  Florio.  Afonna is  a  familiar  corruption  of  madattna,  i.e. my  lady,  mistress  ;  Scott  introduces  ^/i7M/ia r.iuhi  in  the  Fortunes  of  NigeU  See  above.
```


## [2026-09-06T02:21:30.428Z] TOOL CALL #78: Bash

```json
{
 "command": "cd data/verification/sources/refs && for f in FSD_vol1 FSD_vol2 FSD_vol3 FSD_vol4; do echo \"== $f ==\"; grep -c \"\" $f.txt; grep -n \"mille, a thousand\\|L. mille\\|milia passuum\\|mille passuum\" $f.txt | head -4; done",
 "description": "Funk & Wagnalls mile"
}
```


### [2026-09-06T02:21:32.334Z] TOOL RESULT

```
== FSD_vol1 ==
95562
== FSD_vol2 ==
79820
== FSD_vol3 ==
253700
38323:Ulus, under yarrow. [OF , < L. millefohum, < mxlle,
== FSD_vol4 ==
121688
```


## [2026-09-06T02:21:35.763Z] TOOL CALL #79: Bash

```json
{
 "command": "cd data/verification/sources/refs && grep -n \"^mile\\b\\|mile (mil)\\|mile, n\" FSD_vol3.txt | head -5; echo ---; sed -n '38300,38340p' FSD_vol3.txt | head -50; echo \"=== kilo ===\"; grep -n \"kilo-\\|kilogram\" FSD_vol2.txt FSD_vol3.txt | head -5",
 "description": "FSD mile and kilo"
}
```


### [2026-09-06T02:21:35.894Z] TOOL RESULT

```
222:mile, mill, minute, module, modulus, month, moon, morn-
22728:mile***
22746:mile***
38268:mile'afe, 1 moil'ij; 2 mll'a^, n. 1. The entire length or
86661:mile eompasH, and Is
---
planu. -downy ns. 1. A dtaeoso of higher plants caused b> Of or pertaining U the elty of Miletus Aato Minor; so the
a speolss of peronosporaoeous fungus bel o n gi ng to iht genus Milsrtoa tales. II. n A native or Inhahlunt of MUetus.U7S
Xbt 1: alBle;ma(ntt;«ll; Ittsfeud; dhin; go; Jet; QaBin 0 ;to; ilUp;fhlD«fhIe; ajure; F. boA,dline;R «8 loch. variant. mlKrftlne
Kbt 9: bdbk, bAt; fqll, rule, cQre, bttt, bftrn; 911,b5jr; €as k; fas; fo, tem; ink; fas; thin, this; F. bod, dilne; nssloch. nilUc
m-le'stoB** I. a. Of or pertaining to the fourth and lat<>flt
of the Irlah races, the ** Milesians ” or followers of Mlled,
or to Ireland. 11. n. A member of this race fabled to
have oome from Spain to Ireland, which they are reputed
to have vanquished and reorganised, 1300 B C
By a . . mlsundentandins of the epithet Mdmlh. or * wamor,’
applied to Fion by the Oaelia banle, there eree generated a myttii-
eal hero, Mdeaiua, and the sobriquet ’MtUnan,' oolloquially oni«
ploy^ la spenking of the Irish
Vtm Myth* imd MvthPMaktTB P.11 (o. a oo 1873]
[< MUetiuit legendary king of Spain.]
MMe'slas, I nii-iiShus; i ml-ieahOs, n same as miled
mios O'Eellly. Pen-name of Charles G. Halplno.
m-le'tuniflmi-ll'Miin.ginl-ie'tam. n. Mb gl'im. Iv, 20
Ml-le'tua, 1 mi-irtos: 2 ml-irtOs, n. A Bible city In Ionia,
Aaia Minor {Aeu zx. 16)
mlle'waytf n. Ono-tblrd of an hour.
mlPfolt, 1 inil'foii; 2 nifl'fdii. n. A common perennial
asteraooouB herb (Achillea mMefohum), yarrow. 8 uo
Ulus, under yarrow. [OF , < L. millefohum, < mxlle,
thousand, + /oM«m, leaf.)
mi'ford, 1 mil't’erd. 2 mirford. n 1. A town In New
Haven county. Conn. 9. A town In Kent and Sussex ooun-
tle '• Del S. A village In Derbyshire, ICnglaud 4. A tnwn-
■hlp and village In Iroqiiols county. Ill 6 . A town in i i r .u
Woroester county, Maas •- A township and vlllaice in Bill I- tn-ry, « A body of soinicrn or the whole of the
Oakland county. Mloh. 7. A town in HtUsboru county, soldiers of a at ate or nation, soldiers : usually with
N. H. b. A village In Clermont and Hamilton counties, O the definite article; as. the military syn.: ••ee army.
HU 'ford Hr ' von. A borough and seaport In Pembroke- Bfll'l ta ry Fron'tler. A former territory in llungarv, on the
shire, S Wales Turkish frontier, irom the Transylvanian Alps to l>ulmatia
Mirhon'. n BameasMiLLAU
mll-hon'ry* n Same as MiLLiBCzncr.
mll'I-o, 1 mll'i-e, 2 mll'I-a, » Pl* !• PatM Small vesleira tion): followed by apatnsf or mfh, or more rarely /or
that appear on the body in mUlary fever. 9t. A mlUet-aecd. - '
intl'*l-R'eoous» 1 mll*i-6'ihiis, 2 miri-A'shhs. a 1. Dto-
playing the dhtfactenatlos of mllla. 9. Resembling mil-
lot siiotl [department, Algeria.
=== kilo ===
FSD_vol3.txt:35334:16.482 grains) • 1 kilogram* • weight of 840 in U B. subsidiary silver coin.
FSD_vol3.txt:35340:mum density, will eountorpolso the standard kilogram In a vacuum, the
FSD_vol3.txt:35344:*2.0418 gallons (liquid)]* 10,000 grams- 10 kilograms- 1 myrlagram.
FSD_vol3.txt:35346:gallons (liquid)] - ion kilograms - I quintid
FSD_vol3.txt:35363:1 in weiaht In vanuo ia thn aanie aa that of the " kilogramme dea ArehivM " Tho
```


## [2026-09-06T02:21:40.399Z] TOOL CALL #80: Bash

```json
{
 "command": "cd data/verification/sources/refs && grep -n \"milia, pl\\|mtlia\\|milia, thousands\\|AS. mil\" FSD_vol3.txt | head -8; echo ---; sed -n '38260,38275p' FSD_vol3.txt",
 "description": "FSD mile etymology"
}
```


### [2026-09-06T02:21:40.492Z] TOOL RESULT

```
8353:fumtlias to another by the ceremony of mancipation If
---
TRAiN-MiLB Scc TRAIN — pmssciiger^m., ton«m. (RaU~
road ), a standard measure of traffle, based on the rate of
carriage per mile of each passenger or ton of freight.—
statute m., the legal mile of the United States, Great
Britain, etc . 5,280 feet: fixed In the reign of Queen Ellsii^
beth The Scottish mile was 1,084 yards, the Irish 2,340;
the old Prussian 8,237 — traffic m. (Railroad ), a unit made
by adding passeniier- and ton-miles for a given period
mile'afe, 1 moil'ij; 2 mll'a^, n. 1. The entire length or
amount of anything that is or may be measured in miles,
especially when stated in miles; aggregate number of
miles of track, wire, etc , traversed, made, or used
Id th 0 Uaited StatM railway mtlaaga now toadi to iDcrsaso
at the rate of alightly over A.OOO miloe a yMr.
Enoye. Brti. 1 1th ed. vol. xxil, p. 882.
2. Compensation reckoned at so much per mile, allowed
```


## [2026-09-06T02:21:48.110Z] TOOL CALL #81: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D9%85%DB%8C%D9%84%DB%8C",
 "prompt": "What does Mo'in (فرهنگ معین) give for میلی — origin tag and gloss (e.g. [فر.] one thousandth)? Quote it."
}
```


## [2026-09-06T02:21:48.808Z] TOOL CALL #82: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/million",
 "prompt": "Etymology of 'million' and 'milliard': Italian/French route, and relation to Latin mille."
}
```


### [2026-09-06T02:21:49.874Z] TOOL RESULT

```
The server returned HTTP 500 Internal Server Error.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T02:21:55.782Z] TOOL RESULT

```
# Etymology of Million and Milliard

## Origin Route

The word "million" traveled from Latin through Italian and French to English. It entered English in the late 14c. from Old French *million*, which derived from Italian *millione*—literally "a great thousand," using an augmentative form of Italian *mille* (thousand).

## Latin Foundation

The root traces back to Latin *mille* meaning "thousand," though the document notes this origin is "of uncertain origin." In classical Latin, there was no single word for a million; instead, it would be expressed as "decies centena milia" (literally "ten hundred thousand").

## Milliard Connection

"Milliard" developed later as an alternative term. The entry on billion explains that France originally used *billion* to mean a million million, but later adopted "a thousand million" instead—creating the need for *milliard* as a clarifying term for thousand million.

## Historical Development

Interestingly, mathematicians in the Western world didn't commonly use "million" until the 16th century, while India had names for numbers exceeding a billion much earlier. The ancient Greeks couldn't name numbers above ten thousand, and Romans couldn't exceed one hundred thousand.
```


## [2026-09-06T02:21:58.529Z] TOOL CALL #83: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%DB%8C%D9%84%DB%8C/",
 "prompt": "In the فرهنگ معین section, what is given for میلی — origin tag (e.g. [فر.]) and gloss? Quote it."
}
```


### [2026-09-06T02:22:02.960Z] TOOL RESULT

```
Based on the content provided, the فرهنگ معین section does not include an origin tag (like [فر.]) or a separate gloss entry for میلی. 

The section only provides:
- An adjective meaning: "منسوب به میل" (related to میل)
- An example: "مادر هشت میلی جزیره بودیم"
- A note about the prefix meaning: "یکهزارم واحد اصلی"

There is no origin tag displayed in this particular dictionary section.
```


## [2026-09-06T02:22:12.303Z] TOOL CALL #84: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D9%87%D8%B2%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0%C3%A9slom\" \\\n \"https://www.etymonline.com/word/kilo-\" \\\n \"https://www.etymonline.com/word/mile\" \\\n \"https://www.etymonline.com/word/million\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D9%8A%D9%84\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%DB%8C%D9%84\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D8%B3%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D8%AA%DB%8C%D9%86\" \\\n \"https://vajehyab.com/moein/%DA%A9%DB%8C%D9%84%D9%88\" \\\n \"https://abadis.ir/fatofa/%D9%85%DB%8C%D9%84/\" \\\n \"https://abadis.ir/fatofa/%D9%85%DB%8C%D9%84%DB%8C/\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 191 (Gheslo / Ghesto): verification of thousand/hand chains\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-06T02:22:20.674Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e9a72a9bdf8b1054.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1031b762754828fc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c44e5a2b43c6bb62.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/64b1c54e2d9ff11e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c73e13dadaca5f02.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d089dc7e1fdc3857.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/85fe78e29b20cc99.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f7b5ffd49b3fe535.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/30cfae5fd997b9f3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c1f7df80afb910d6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a687090bc740363f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f12e03e6d7a13dad.txt
```


## [2026-09-06T02:22:23.264Z] TOOL CALL #85: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T02:22:23.312Z] TOOL RESULT

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


## [2026-09-06T02:23:14.048Z] TOOL CALL #86: Bash

```json
{
 "command": "cd data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if \"dasta- sb. ‘hand’\" in p or \"dasta- sb.\" in p:\n        print('leaf',i)\n        print(re.findall(r'\\n\\s*(\\d{3})\\s+OLD PERSIAN|OLD PERSIAN\\s+(\\d{3})', p)[:4])\n        j=p.find('dasta- sb.')\n        print(p[max(0,j-200):j+500])\nEOF",
 "description": "Kent dasta- leaf and page"
}
```


### [2026-09-06T02:23:16.648Z] TOOL RESULT

```
leaf 213
[('190', '')]
10.1, $228.11) DB 1.53.
darsam adv. ‘mightily’: asn. to adj. darsa- ($143.1), to root dar§- (against this, Hz. Apī
135-6). DB 1.50 (MB Gr. $366; wrongly Kent, ·
JAOS 35.336-42); 4.37; DNb 14, 15, 50.
dasta- sb. ‘hand’: Av. zasta-, N Pers. 0051, Skt. hdsta-, pIE *ghosto- (§88, $116, $145). See also dastakarta-. даѕіауа ism. DR 4.35. dastaibiya idm. (§189) DNb 41.
dastakarta- adj. ‘handmade’: dasta- + pte. .
karta- (5160.10), to kar- ‘make’. [dasta|kartam (restored after the Elam., Wb. ZDMG 91.85,
```


## [2026-09-06T02:23:22.152Z] TOOL CALL #87: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg191.png data/verification/sources/refs/ocr/BOOK/191.png && ls -la data/verification/sources/refs/ocr/BOOK/191.png",
 "description": "Copy page image for audit"
}
```


### [2026-09-06T02:23:22.225Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 78016 Sep  5 22:23 data/verification/sources/refs/ocr/BOOK/191.png
```


## [2026-09-06T02:31:54.040Z] TOOL CALL #88: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-191.json <<'JSONEOF'\n{\n \"pdf_page\": 191,\n \"book_page\": 161,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Gheslo\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ǵʰéslo- / *ǵʰeslom 'thousand' (in the compound *sm̥-ǵʰéslom 'one thousand')\",\n   \"note\": \"Pokorny IEW 446 heads the entry 'ĝhéslo- ,tausend'' and lists exactly the material Nourai draws on: Skt. sa-hásram (< *sm̥-ǵʰeslom, to sem- 'one'), Av. hazaŋrəm, NPers. hazār, Sogd. z'r, Gk. Ion. χείλιοι / Att. χίλιοι, and — with 'Vielleicht' — Lat. mille from *smī gzhlī. Nourai's root box (language label 'Indo-European', gloss 'thousand', ref POK:446) is therefore accurate. Wiktionary reconstructs *ǵʰéslom and, like Pokorny's own note in the IED dump ('gheslo- : thousand derived from ghesor-1, ghesr- : hand'), analyses it as *ǵʰes- 'hand' + *-lom, i.e. literally 'a full hand' — which incidentally ties this chart to the next one on the same page. The one soft spot in the entry is the Latin box: Walde-Pokorny I 633 (1930) explicitly REJECTED Sommer's derivation of mille from *smī ghslī ('Abzulehnen ist Sommers … Heranziehung von lat. mille aus *smi ghslī'), Pokorny 1959 downgraded it to 'vielleicht', Watkins calls mille 'of obscure origin', and only de Vaan (2008) again accepts *sm-ih₂-ǵʰsl-ih₂. Nourai's own NOTE flags this uncertainty, which is to his credit; the printed forms in that box, however, are corrupt (see node 7). The second soft spot is the English box (node 12), where 'mile' is routed through French although it is a direct West-Germanic borrowing from Latin.\",\n   \"note_fa\": \"جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۴۶ فرهنگ خود مدخل «ĝhéslo- ,tausend'» را آورده و همان مواد نمودار را برمی‌شمارد: سنسکریت sa-hásram (از *sm̥-ǵʰeslom، با sem- «یک»)، اوستایی hazaŋrəm، فارسی نو هزار، سغدی z'r، یونانی χίλιοι و ــ با قید «شاید» ــ لاتینی mille از *smī gzhlī. ویکی‌واژه نیز *ǵʰéslom را بازسازی می‌کند و آن را *ǵʰes- «دست» + پسوند ‑lom، یعنی «یک مشت/یک دستِ پُر» می‌داند؛ از همین رو این نمودار با نمودار دوم همین صفحه (ریشهٔ «دست») پیوند می‌خورد. دو نقطهٔ سست در نمودار هست: نخست جعبهٔ لاتینی که والده‑پوکورنی (جلد ۱ ص ۶۳۳) اشتقاق mille از *smī ghslī را «مردود» شمرده و واتکینز آن را «تاریک» می‌خواند (خودِ نورایی هم در یادداشت به این تردید اشاره کرده است) و صورت‌های چاپ‌شده در آن جعبه غلط چاپی‌اند؛ دوم جعبهٔ انگلیسی که واژهٔ mile را از فرانسه گرفته، حال آنکه mile وام‌واژه‌ای مستقیم از لاتینی به ژرمنی غربی است.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0%C3%A9slom\",\n    \"https://www.etymonline.com/word/kilo-\"\n   ],\n   \"ref_check\": [\n    {\n     \"ref\": \"POK:446\",\n     \"status\": \"supports\",\n     \"note\": \"POK_02.txt, form-feed leaf 104 (= printed p. 446, the page number '446' is printed in the block): 'ĝhéslo- ,tausend'. Ai. sa-hásram n. ,Tausend' (sm̥-gheslom, zu sem- ,eins'), sa-hasriya- ,tausendfach', av. hazaŋrəm n. ,Tausend', npers. hazār, woraus arm. hazar entlehnt; sogd. z'r (= *zār), afgh. zar; gr. ion. χείλιοι, äol. χέλλιοι …, att. χίλιοι … Vielleicht auch lat. mille ,tausend; ein Tausend', falls aus *smī gzhlī (ghslī) ,eine Tausendheit'; *smī: gr. μία.' Same text in POK_full.txt lines 37127-37150 with 'Page(s): 446'. Root, language label and gloss are exactly as drawn.\"\n    }\n   ],\n   \"consulted\": [\n    {\n     \"src\": \"AHD\",\n     \"where\": \"Watkins 1985, g-list (AHD_watkins1985.txt line 524)\",\n     \"stance\": \"supports\",\n     \"note\": \"'gheslo-. Seen by some as a base for words meaning \\\"thousand.\\\" 1. Suffixed form *ghesl-yo- in Greek khilioi, thousand: CHILIAD, KILO-. 2. Latin mille, thousand, which has been analyzed as *smi-, \\\"one\\\" + a form *ghsli-, is of obscure origin: MIL, MIL2, MILE, MILLENARY, MILLESIMAL, MILLI-, MILLIEME, MILLION; MILFOIL, MILLENNIUM, MILLEPORE, MILLIARY, MILLIPEDE. [Pok. gheslo- 446.]' — the root itself confirmed; the Latin link explicitly called 'of obscure origin'.\"\n    },\n    {\n     \"src\": \"WLD\",\n     \"where\": \"Walde-Pokorny Bd. I 633 (incoming/WLD/WLD_Bd1_pages.txt line 60198 ff.)\",\n     \"stance\": \"partial\",\n     \"note\": \"'gheslo- „tausend“? Ai. sahasra n. „Tausend“ … av. hazaŋra n. „Tausend“, np. hazār … gr. jon. χείλιοι, aeol. χέλλιοι, att. χίλιοι …' — the root is there (with a question mark), but the page ends: 'Abzulehnen ist Sommers … Heranziehung von lat. mille aus *smi ghslī, eigentlich „eine Tausendheit“'. Walde-Pokorny therefore rejects precisely the Latin arrow Nourai draws.\"\n    },\n    {\n     \"src\": \"IEC\",\n     \"where\": \"Mann, An IE Comparative Dictionary, s.v. gheslos (IEC.txt line 4659)\",\n     \"stance\": \"partial\",\n     \"note\": \"'gheslos, -io-, -i \\\"yardstick, tally\\\" (?) (w. *sm-, smi- \\\"thousand\\\") (?) Cf. Skt. sa-hasram \\\"1000\\\"; Gk. kheílioi, pl. \\\"thousands\\\"; Lat. mille (\\\"thousand\\\", fr. *smi- ghesli- ?)' — same word family, but Mann glosses the base 'yardstick, tally', not 'thousand', and queries every step.\"\n    }\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"hazanrem, hazangra\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The book's ASCII spellings render Younger Avestan hazaŋrəm (neuter, nom./acc. sg.) and its stem hazaŋra- 'thousand' — Nourai writes the velar nasal ŋ once as 'n' and once as 'ng'. The form continues Proto-Iranian *hazahram < Proto-Indo-Iranian *saȷ́ʰásram < PIE *sm̥-ǵʰéslom 'one thousand' (*sm̥- 'one' + *ǵʰeslo-); Indo-Iranian *s > Iranian h word-initially (cf. Skt. sa-hásram beside Av. hazaŋrəm), and intervocalic *-sr- gives Avestan -ŋr- (Skt. -sr- : Av. -ŋh r-/-ŋr-). It is well attested in the Yašts, e.g. Yt. 5.21 'hazaŋrəm gavąm' and Vd. 2.30 'hazaŋrəm narąm … taoxma'.\",\n     \"derivation_fa\": \"صورت‌های «hazanrem، hazangra» در کتاب همان اوستایی hazaŋrəm (نام خنثی) و ستاک hazaŋra- «هزار» است؛ نورایی واکِ خیشومیِ ŋ را یک بار «n» و یک بار «ng» نوشته است. این واژه از ایرانی آغازین *hazahram و آن از هندوایرانی آغازین *saȷ́ʰásram و سرانجام از هندواروپایی *sm̥-ǵʰéslom «یک هزار» می‌آید؛ س ِ آغازینِ هندوایرانی در ایرانی به «ه» بدل شده (سنسکریت sa-hásram در برابر اوستایی hazaŋrəm) و خوشهٔ ‑sr‑ میان‌واکه‌ای در اوستایی ‑ŋr‑ شده است. بارتولومه در ستون ۱۷۹۶ فرهنگ ایرانی باستان همین را آورده است. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0%C3%A9slom\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"POK:446\",\n       \"status\": \"supports\",\n       \"note\": \"POK_02.txt leaf 104 (p. 446): 'av. hazaŋrəm n. ,Tausend'' stands in the entry ĝhéslo- immediately after Ai. sa-hásram — the arrow root→Avestan as drawn.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"BRT\",\n       \"where\": \"Bartholomae, Altiran. Wb. col. 1796 (BRT.txt line 29679 ff.)\",\n       \"stance\": \"supports\",\n       \"note\": \"'j. hazaŋra- neutr. Zw. \\\"tausend\\\": … hazaŋrəm narąm … Yt. 1.19 … KompA., E.; Ableit. — ai. sahasra- n., np. hazār. — Pü.: 1000.' Bartholomae gives the Avestan word, the Sanskrit cognate and the New Persian continuation in one line.\"\n      },\n      {\n       \"src\": \"AHD\",\n       \"where\": \"Watkins 1985 s.v. gheslo- (AHD_watkins1985.txt line 524)\",\n       \"stance\": \"silent\",\n       \"note\": \"Watkins lists only the Greek and Latin branches of *gheslo-, no Iranian forms; his silence is a matter of scope (no English word comes from the Avestan branch), not disagreement.\"\n      }\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"hezâr «هزار»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NPers. هزار hazār 'thousand' continues Middle Persian hazār (Book Pahlavi written with the arameogram-like spelling ⟨hcʾl⟩, Manichaean hz'r; MacKenzie, CPD 43), from Old Iranian *hazahra- = Av. hazaŋra-. The Middle Persian outcome of Old Iranian *-zahr-/-zaŋr- is -zār-, whence the New Persian form unchanged since the Sasanian period; Armenian borrowed it as hazar already in the Parthian/Sasanian period (Hübschmann, Arm. Gr. I 174), and the Sogdian cognate is z'r. Note that Nourai draws the arrow Avestan→Persian; strictly the Persian word is not descended from Avestan but from the parallel Old Persian/Old Iranian form, Avestan simply being the attested Old Iranian witness — a shorthand Nourai uses throughout the book.\",\n     \"derivation_fa\": \"«هزار» فارسی نو دنبالهٔ فارسی میانهٔ hazār (پهلوی کتابی ⟨hcʾl⟩، مانوی hz'r؛ مکنزی، فرهنگ کوچک پهلوی ص ۴۳) است، و آن از ایرانی باستان *hazahra- که همان اوستایی hazaŋra- است می‌آید؛ خوشهٔ ‑zaŋr‑/‑zahr‑ ایرانی باستان در فارسی میانه به ‑zār‑ بدل شده و از آن پس بی‌تغییر مانده است. ارمنی hazar را در همان دورهٔ اشکانی/ساسانی وام گرفته و صورت سغدی آن z'r است. معین در حاشیهٔ برهان قاطع (ص ۲۳۳۱) دقیقاً همین زنجیره را می‌آورد. تنها نکتهٔ فنی این است که فارسی نو فرزندِ اوستایی نیست بلکه هر دو از ایرانی باستان‌اند؛ نورایی در سراسر کتاب اوستایی را نمایندهٔ ایرانی باستان می‌گیرد. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D9%87%D8%B2%D8%A7%D8%B1\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"POK:446\",\n       \"status\": \"supports\",\n       \"note\": \"POK_02.txt leaf 104 (p. 446): 'npers. hazār, woraus arm. hazar entlehnt; sogd. z'r (= *zār), afgh. zar' — the Persian word placed directly under the root.\"\n      },\n      {\n       \"ref\": \"BQT:2331\",\n       \"status\": \"supports\",\n       \"note\": \"Borhan-e Qateʿ ed. Moʿin, printed p. 2331 (vol. 4 scan, pdf p. 414; fetched with tools/ref_page.py BQT:2331), headword «هزار - بفتح اول ده صد را گویند»; Moʿin's etymological footnote reads: «اوستا hazaŋra- [= هزار]، پهلوی … [رك: هزارم]، … (هزارید)، هندی باستان sahasra-، افغانی zār (هزار)؛ ارمنی hazar … کردی hazār (هزار) … زازا hazār … گیلکی hazār». Exactly the arrow drawn.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"HRN\",\n       \"where\": \"Horn, Grundriss der neupersischen Etymologie no. 1093 (HRN.txt line 9445)\",\n       \"stance\": \"supports\",\n       \"note\": \"'1093. hezār \\\"tausend\\\". aw. hazaŋra- \\\"tausend\\\"; phlv. hazār, hazārak \\\"Millennium\\\", vergl. ἀζαραπατεῖς … arm. LW. hazarapet …; ai. sahásra-. afγ. zār \\\"tausend\\\"; LW. arm. hazar, kurd. hazār etc.'\"\n      },\n      {\n       \"src\": \"PHD\",\n       \"where\": \"MacKenzie, Concise Pahlavi Dictionary p. 43 (PHD_mackenzie.txt line 2882)\",\n       \"stance\": \"supports\",\n       \"note\": \"'hazār [1,000, hcyl | M hz'r, N -] thousand.' — the Middle Persian link between Avestan and New Persian, with the New Persian form identical (the dash means 'same as MP').\"\n      },\n      {\n       \"src\": \"BRT\",\n       \"where\": \"Altiran. Wb. col. 1796\",\n       \"stance\": \"supports\",\n       \"note\": \"s.v. hazaŋra- the cognate list ends 'ai. sahasra- n., np. hazār'.\"\n      }\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Greek\",\n     \"words\": \"xilio\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Nourai's 'xilio' is the Attic χίλιοι (khī́lioi) 'thousand', transliterated with x for χ. The Ionic form is χείλιοι and the Aeolic χέλλιοι; all three go back to *χέσλιοι < PIE *ǵʰesl-iyo-, a yo-derivative of *ǵʰeslo-. The Aeolic geminate -λλ- from *-σλ- and the Ionic/Attic compensatory lengthening (-σλ- > -λ- with lengthening of the preceding vowel, ει/ῑ) are the regular reflexes, which is what makes the Greek word the best witness for the root; the Saka (Khotanese) noun ysāra 'thousand' preserves the bare base *ǵʰeslo-.\",\n     \"derivation_fa\": \"«xilio» در نمودار همان χίλιοι یونانیِ آتیک «هزار» است (نورایی χ را x نوشته). صورت ایونی χείλιοι و اِئولی χέλλιοι است و هر سه از *χέσλιοι و آن از هندواروپایی *ǵʰesl-iyo-، مشتقِ yo‑دارِ *ǵʰeslo-، می‌آیند. مصوّتِ کشیدهٔ آتیک/ایونی نتیجهٔ جبرانِ افتادنِ س در خوشهٔ ‑σλ‑ است و مضاعف‌شدنِ ‑λλ‑ در اِئولی همان تحول را به شکل دیگری نشان می‌دهد. پوکورنی همین‌ها را در ص ۴۴۶ آورده است. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0%C3%A9slom\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"POK:446\",\n       \"status\": \"supports\",\n       \"note\": \"POK_02.txt leaf 104 (p. 446): 'gr. ion. χείλιοι, äol. χέλλιοι (χελλιοστύς ,Tausendschaft'), att. χίλιοι (*χέσλιοι) … Das Grundwort *χέσλο- findet sich in sakisch ysāra …'.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"AHD\",\n       \"where\": \"Watkins 1985 s.v. gheslo- (AHD_watkins1985.txt line 524)\",\n       \"stance\": \"supports\",\n       \"note\": \"'1. Suffixed form *ghesl-yo- in Greek khilioi, thousand: CHILIAD, KILO-.'\"\n      },\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein 1966 s.v. kilo- (KLN_1966.txt line 20682, leaf 260 area)\",\n       \"stance\": \"supports\",\n       \"note\": \"'kilo-, combining form meaning \\\"one thousand\\\". — F. kilo-, fr. Gk. χίλιοι (Ion. χείλιοι), \\\"a thousand\\\", which is of uncertain origin. It is perh. cogn. with L. mille, \\\"a thousand\\\"…'.\"\n      },\n      {\n       \"src\": \"IEC\",\n       \"where\": \"Mann s.v. gheslos (IEC.txt line 4659)\",\n       \"stance\": \"supports\",\n       \"note\": \"'Gk. kheílioi, pl. \\\"thousands\\\"' listed under the same base.\"\n      }\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"French\",\n     \"words\": \"kilo-\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"French kilo- is a learned coinage, not an inherited word: it was introduced in French in 1795 by the law establishing the metric system (7 avril 1795, loi sur les poids et mesures), the commission taking Greek prefixes for the multiples (kilo-, hecto-, déca-) and Latin ones for the submultiples (déci-, centi-, milli-). It is taken directly from Greek χίλιοι 'thousand' with the -oi ending dropped and the combining -o- kept. Hence kilogramme, kilomètre (both 1795), kilowatt (1881, Congrès international des électriciens).\",\n     \"derivation_fa\": \"«kilo-» فرانسوی واژه‌ای وام‌گرفته و ساختگیِ علمی است، نه واژه‌ای موروثی: در سال ۱۷۹۵ میلادی و با قانونِ برقراری دستگاه متری در فرانسه ساخته شد؛ کمیسیونِ اوزان و مقادیر برای مضرب‌ها پیشوندهای یونانی (kilo-، hecto-، déca-) و برای کسرها پیشوندهای لاتینی (déci-، centi-، milli-) برگزید. این پیشوند یکراست از χίλιοι یونانی گرفته شده و پایانهٔ ‑οι افتاده است. از همین‌جاست kilogramme و kilomètre (هر دو ۱۷۹۵) و kilowatt (۱۸۸۱). ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/kilo-\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"AHD\",\n       \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. gheslo- routes KILO- through the Greek branch ('Suffixed form *ghesl-yo- in Greek khilioi, thousand: CHILIAD, KILO-'); the index line 1714 reads 'KILO- gheslo-'. The French mediation is not spelled out by Watkins but is standard (Klein, Etymonline).\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein 1966 s.v. kilo-, kilogram, kilometer (KLN_1966.txt lines 20682-20685)\",\n       \"stance\": \"supports\",\n       \"note\": \"'kilo-, … — F. kilo-, fr. Gk. χίλιοι'; 'kilogram, kilogramme, n. — F. kilogramme, lit. \\\"one thousand grams\\\", coined fr. kilo- and gram'; 'kilometer, kilometre, n. — F. kilomètre, lit. \\\"one thousand meters\\\", coined fr. kilo- and Gk. μέτρον'. The French coinage is explicit.\"\n      },\n      {\n       \"src\": \"Etymonline\",\n       \"where\": \"etymonline.com/word/kilo- (archived)\",\n       \"stance\": \"supports\",\n       \"note\": \"'introduced in French 1795, when the metric system was officially adopted there', from Greek khilioi.\"\n      }\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Persian\",\n     \"words\": \"kîlo «کیلو»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian کیلو kilu/kilo is a 19th–20th c. loan from French kilo(-)/kilogramme, taken over with the whole metric vocabulary (the metric system was made official in Iran by the law of 1304 š./1925 and enforced from 1311 š./1933). The compounds in the box — کیلوگرم kilugeram, کیلومتر kilumetr, کیلووات kiluvāt — are likewise French kilogramme, kilomètre, kilowatt with Persian phonetic adaptation (French -gramme > -geram with an epenthetic vowel breaking the final cluster). Persian کیلو also functions alone for 'kilogram', a French colloquial usage borrowed with the word. Nourai's gloss 'thousand' is the etymological, not the current, meaning.\",\n     \"derivation_fa\": \"«کیلو» فارسی وام‌واژه‌ای است از فرانسویِ kilo(-)/kilogramme که در سدهٔ سیزدهم و چهاردهم خورشیدی همراه با کل واژگان دستگاه متری وارد فارسی شد (دستگاه متری با قانون ۱۳۰۴ رسمی و از ۱۳۱۱ اجباری شد). ترکیب‌های داخل جعبه ــ کیلوگرم، کیلومتر، کیلووات ــ نیز برگرفته از kilogramme، kilomètre و kilowatt فرانسوی‌اند با سازگاری آواییِ فارسی (افزودن واکهٔ میانجی در «گرم» برای شکستن خوشهٔ پایانی). معین در فرهنگ خود این واژه را با نشانِ [فر.] یعنی فرانسوی آورده است. معنای «هزار» که نورایی داده معنای ریشه‌شناختی است نه معنای امروزی. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://vajehyab.com/moein/%DA%A9%DB%8C%D9%84%D9%88\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"MON:3156\",\n       \"status\": \"partial\",\n       \"note\": \"The 6-vol. print pagination cannot be checked online (only the 2-vol. abridgement is scanned), but the entry itself is verifiable: Moʿin s.v. کیلو gives the origin tag [فر.] (= French) and the definition «به معنی هزار است و برای تعیین واحدهای دستگاه متری به کار می‌رود» — i.e. exactly Nourai's gloss and exactly the French→Persian arrow. Page number not verified.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"MON\",\n       \"where\": \"vajehyab.com/moein/کیلو (archived)\",\n       \"stance\": \"supports\",\n       \"note\": \"«[فر.] … به معنی هزار است و برای تعیین واحدهای دستگاه متری به کار می‌رود» with کیلوگرم/کیلومتر as examples.\"\n      },\n      {\n       \"src\": \"HRN\",\n       \"where\": \"Horn, Grundriss (grep 'kilo' in HRN.txt)\",\n       \"stance\": \"silent\",\n       \"note\": \"Horn (1893) has no کیلو: the word entered Persian after his book, which is itself evidence that it is a modern European loan and not an inherited form.\"\n      }\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"kilo, kilogram, kilometer, kilowatt\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English took the whole set from French: kilogram(me) 1795 (attested in English 1797), kilometre 1810, kilo (short for kilogram) 1870, kilowatt 1883 — each a direct borrowing of the French metric coinage rather than an independent formation on Greek. The chart's arrow French→English is therefore right, and Nourai keeps kilo- separate from milli- (node 10-12), which is the correct division: kilo- multiplies, milli- divides.\",\n     \"derivation_fa\": \"انگلیسی همهٔ این مجموعه را از فرانسه گرفته است: kilogramme در ۱۷۹۵ ساخته شد و در ۱۷۹۷ به انگلیسی راه یافت، kilometre در ۱۸۱۰، kilo (کوتاه‌شدهٔ kilogram) در ۱۸۷۰ و kilowatt در ۱۸۸۳. پس پیکانِ فرانسه ← انگلیسی در نمودار درست است و این‌ها ساخت‌های مستقلِ انگلیسی بر پایهٔ یونانی نیستند. کلاین نیز هر چهار واژه را «از فرانسوی» می‌داند. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/kilo-\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"AHD\",\n       \"status\": \"supports\",\n       \"note\": \"Watkins 1985 index (AHD_watkins1985.txt line 1714) 'KILO- gheslo-' and the root entry 'in Greek khilioi, thousand: CHILIAD, KILO-'.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein 1966 s.v. kilogram / kilometer (KLN_1966.txt line 20685)\",\n       \"stance\": \"supports\",\n       \"note\": \"'kilogram, kilogramme, n. — F. kilogramme … coined fr. kilo- and gram'; 'kilometer, kilometre, n. — F. kilomètre … coined fr. kilo- and Gk. μέτρον'.\"\n      },\n      {\n       \"src\": \"Etymonline\",\n       \"where\": \"etymonline.com/word/kilo- (archived)\",\n       \"stance\": \"supports\",\n       \"note\": \"kilo- 'introduced in French 1795'; kilobyte 1970 shows the prefix still productive.\"\n      }\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"Latin\",\n     \"words\": \"smî-gžlî; milia pasuum; milie\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"Two of the three forms printed in this box are corrupt, and the gloss of the first is wrong. (a) 'smî-gžlî' is Nourai's rendering of Pokorny's reconstruction *smī gzhlī (ghslī), which Pokorny glosses 'eine Tausendheit', i.e. 'a thousand-unit, one thousand' — NOT 'one thousandth'; the modern shape of the reconstruction is *sm-ih₂-ǵʰsl-ih₂ (de Vaan), the feminine 'one' *sm-ih₂ (= Gk. μία) plus the root noun. (b) 'milia pasuum' is a misprint for milia passuum 'thousands of paces', the Roman mile (mille passus, 1000 double paces ≈ 1479 m). (c) 'milie' is a misprint for mille 'thousand' — Nourai's own NOTE below spells it 'millia'/'millie', with the same double-l inconsistency, so the corruption is in the printed book, not in the extraction. As to the substance: the derivation of mille from *smī-ǵʰslī was rejected outright by Walde-Pokorny I 633 (1930), softened to 'vielleicht' by Pokorny 1959, called 'of obscure origin' by Watkins and 'of uncertain origin' by Klein, and only re-accepted by de Vaan (2008). Nourai's NOTE ('not quite certain') is thus a fair statement of the position, and the link itself is plausible rather than established.\",\n     \"derivation_fa\": \"دو صورت از سه صورتِ این جعبه غلط چاپی است و معنای صورت نخست هم نادرست است. یکم: «smî-gžlî» همان بازسازیِ *smī gzhlī پوکورنی است که او آن را «eine Tausendheit» یعنی «یک هزارگان، یک هزار» معنی می‌کند، نه «یک‌هزارم»؛ صورت امروزی این بازسازی *sm-ih₂-ǵʰsl-ih₂ است (دِ ڤان). دوم: «milia pasuum» غلط چاپیِ milia passuum «هزار گام» است. سوم: «milie» غلط چاپیِ mille است؛ خودِ نورایی در یادداشتِ زیر جعبه «millia»/«millie» نوشته که همان ناهماهنگی را نشان می‌دهد. پس خطا از کتاب چاپی است نه از خوانشِ اسکن. در اصلِ مطلب نیز: اشتقاق mille از *smī-ǵʰslī را والده‑پوکورنی (جلد ۱ ص ۶۳۳) یکسره مردود شمرد، پوکورنی ۱۹۵۹ آن را «شاید» خواند، واتکینز «تاریک» و کلاین «نامطمئن» گفتند و تنها دِ ڤان (۲۰۰۸) دوباره آن را پذیرفت. پس یادداشتِ خودِ نورایی («کاملاً مسلّم نیست») منصفانه است و این پیوند «با احتیاط پذیرفتنی» است.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"smî-gžlî : one thousandth ; milia pasuum : thousand steps ; milie : a measure of distance ; NOTE: Derivation of \\\"millia\\\" or \\\"millie\\\" from \\\"smî-gžlî\\\" is not quite certain.\",\n     \"correct_form\": \"*smī-ǵʰslī 'one thousand' ; milia passuum 'thousands of paces' ; mille 'thousand'\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/mile\",\n      \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0%C3%A9slom\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"AHD\",\n       \"status\": \"partial\",\n       \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 524): 'Latin mille, thousand, which has been analyzed as *smi-, \\\"one\\\" + a form *ghsli-, is of obscure origin' — he records the analysis but declines to endorse it, i.e. weaker than the arrow drawn.\"\n      },\n      {\n       \"ref\": \"KLN:979\",\n       \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 525 (the leaf carries the printed page numbers '979' and '980'), s.v. mile: 'fr. L. milia, pl. of mille, \\\"a thousand\\\" (in … milia passuum, \\\"…thousand paces\\\", i.e. \\\"…miles\\\"). L. mille is of uncertain origin. It is perh. cogn. with Gk. χίλιοι, OI. sa-hasram, \\\"a thousand\\\"; see Walde-Hofmann, LEW., II, 88 s.v. mille.' Klein confirms both the phrase milia passuum (with -ss-) and the cautious cognation with the Greek/Indic 'thousand' words.\"\n      },\n      {\n       \"ref\": \"BQT:2080\",\n       \"status\": \"supports\",\n       \"note\": \"Borhan-e Qateʿ ed. Moʿin p. 2080 (vol. 4 scan, pdf p. 163; tools/ref_page.py BQT:2080), footnote 1 to میل: «لاتینی mille, millia (millia passuum) هزار گام … انگلوساکسن mīl، انگلیسی mile، میل در روم قدیم ۱۴۷۹ متر … بود» — Moʿin gives the Latin phrase and its meaning, i.e. the same Latin box.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"POK\",\n       \"where\": \"Pokorny IEW 446 (POK_02.txt leaf 104)\",\n       \"stance\": \"partial\",\n       \"note\": \"'Vielleicht auch lat. mille ,tausend; ein Tausend', falls aus *smī gzhlī (ghslī) ,eine Tausendheit'; *smī: gr. μία.' — 'perhaps' and 'if', and the gloss is 'a thousand', not 'one thousandth'.\"\n      },\n      {\n       \"src\": \"WLD\",\n       \"where\": \"Walde-Pokorny Bd. I 633 (incoming/WLD/WLD_Bd1_pages.txt line ~60225)\",\n       \"stance\": \"contradicts\",\n       \"note\": \"'Abzulehnen ist Sommers IF. 10, 216 ff., 11, 323 f. Heranziehung von lat. mille aus *smi ghslī, eigentlich „eine Tausendheit“' — a flat rejection of exactly this arrow in 1930.\"\n      },\n      {\n       \"src\": \"IEC\",\n       \"where\": \"Mann s.v. gheslos (IEC.txt line 4659)\",\n       \"stance\": \"partial\",\n       \"note\": \"'Lat. mille (\\\"thousand\\\", fr. *smi- ghesli- ?)' — the question mark is Mann's.\"\n      },\n      {\n       \"src\": \"BOOK\",\n       \"where\": \"printed page 191 of the PDF, copied to data/verification/sources/refs/ocr/BOOK/191.png\",\n       \"stance\": \"supports\",\n       \"note\": \"The page image shows 'smî-gžlî : one thousandth', 'milia pasuum : thousand steps', 'milie : a measure of distance' and the note with 'millia'/'millie'. The JSON extraction reproduces the page exactly; the errors are the book's.\"\n      }\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"Arabic\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"An empty pass-through box standing for Arabic مِيل mīl 'mile', which is a loan from Latin mīlle (passuum) — reaching Arabic through the Roman-Byzantine road system and the Aramaic/Syriac milieu (Classical Syriac ܡܝܠܐ mīlā, Jewish Aramaic/Hebrew מיל mīl are the intermediaries; Greek μίλιον milion is the Byzantine form of the same word). In Arabic usage the mīl is defined by the lexicographers as 3000 or 4000 cubits and as one third of a farsakh, i.e. it was fitted into the Islamic system of itinerary measures; the same word also came to mean the road-marker itself and then a tower/minaret set up as a landmark.\",\n     \"derivation_fa\": \"این جعبهٔ خالی نمایندهٔ عربیِ «میل» به معنای «میل، واحد مسافت» است که وام‌واژه‌ای است از لاتینیِ mīlle (passuum)؛ راهِ ورود آن جاده‌های رومی‑بیزانسی و محیط آرامی/سریانی بوده است (سریانی ܡܝܠܐ mīlā و یونانیِ بیزانسی μίλιον واسطه‌اند). واژه‌نگارانِ عرب میل را ۳۰۰۰ یا ۴۰۰۰ ذراع و «سه‌یکِ فرسنگ» تعریف کرده‌اند، یعنی آن را در دستگاه مسافت‌سنجیِ اسلامی جای داده‌اند؛ سپس همین واژه بر خودِ نشانهٔ کنارِ راه و آنگاه بر برج و منارهٔ راهنما نیز اطلاق شده است. ادعای نورایی (لاتینی ← عربی) درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D9%85%D9%8A%D9%84\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"None\",\n       \"status\": \"not_checked\",\n       \"note\": \"Nourai gives no reference for this box; it is an unlabelled pass-through. The claim is checked below against Klein, Moʿin's footnote in BQT and Wiktionary instead.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"BQT\",\n       \"where\": \"Borhan-e Qateʿ ed. Moʿin p. 2080, footnotes 1 and 4 (ocr/BQT/2080.txt)\",\n       \"stance\": \"supports\",\n       \"note\": \"footnote 1: «… این کلمه معرب شده. در عربی «مقدار منتهای درازی از زمین» یا «مسافت زمین متراخیة بی‌حد» و «سه یک فرسنگ» «منتهی‌الارب» آمده. در نزد قدمای اهل هیئت ۳۰۰۰ ذراع و در نزد متأخران ۴۰۰۰ ذراع است»; footnote 4: «لاتینی milliarius از mille بمعنی هزار … و آن به ستون‌هایی اطلاق می‌شده که برای تعیین مسافتی برابر ۱۰۰۰ گام در جاده‌ها نصب می‌کردند … در عربی نیز بمعنی نشانهٔ راه‌ها و نیز بمعنی مناری که برای راهنمایی مسافران … بنا کنند بکار رفته». The Latin→Arabic step is explicit ('معرب شده').\"\n      },\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein 1966 leaf 525 (pp. 979/980) s.v. mil, mile\",\n       \"stance\": \"supports\",\n       \"note\": \"'mil, n., a unit of length equal to one-thousandth part of an inch. — L. mille, \\\"a thousand\\\". See mile.' Klein derives the whole mil/mile family from L. mille, the source of the Arabic loan too.\"\n      },\n      {\n       \"src\": \"Wiktionary\",\n       \"where\": \"en.wiktionary.org/wiki/ميل (Arabic section, archived)\",\n       \"stance\": \"supports\",\n       \"note\": \"Arabic mīl 'mile' is 'borrowed from Latin mīlle passuum', with Classical Syriac ܡܝܠܐ (mīlā) and Hebrew מַיְל in the borrowing chain; the separate mīl 'medical probe, kohl-stick' is from Ancient Greek μήλη (mḗlē), and mayl 'inclination' is native to the root م ي ل — three different words that must not be confused.\"\n      }\n     ]\n    },\n    {\n     \"id\": 9,\n     \"lang\": \"Persian\",\n     \"words\": \"mîl «میل»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian میل mīl 'a mile; a road marker, a landmark tower' is an Arabic-mediated Latinism: Lat. mīlle (passuum) → Arabic mīl → NPers. mīl, taken over in the early Islamic centuries together with the Abbasid road-measuring vocabulary (barīd, farsakh, mīl). The semantic step 'unit of distance' → 'the marker that shows the distance' → 'tower, minaret erected as a landmark' happened already in Arabic and is fully lived in Persian, where the standing brick towers of the Seljuq and later periods are called میل (e.g. میل نادری, میل رادکان, میل گنبد). The Ferdowsī hemistich printed in the box — «ز یک میل کرد آفریدون نگاه / یکی کاخ دید اندر آن شهر شاه» — uses it in the sense 'at one mile's distance', showing the word naturalised by c. 1010 CE. This میل must be kept apart from two homonyms: میل mayl 'inclination' (Arabic root م ي ل) and میل mīl 'kohl-stick, probe' (Arabic from Greek μήλη), both of which Moʿin's footnotes on the same page distinguish.\",\n     \"derivation_fa\": \"«میل» فارسی به معنای «میل (واحد مسافت)» و «نشانهٔ کنارِ راه، برجِ راهنما» وام‌واژه‌ای است لاتینی که از راه عربی آمده است: لاتینی mīlle (passuum) ← عربی «میل» ← فارسی «میل»؛ ورود آن به سده‌های نخست اسلامی و همراه با واژگانِ راه و برید (فرسخ، برید، میل) بازمی‌گردد. تحول معنایی «واحد مسافت» ← «نشانه‌ای که مسافت را می‌نماید» ← «برج و منارهٔ راهنما» در خودِ عربی رخ داده و در فارسی زنده است؛ برج‌های آجریِ دورهٔ سلجوقی و پس از آن را «میل» می‌نامند (میل نادری، میل رادکان، میل گنبد). بیتِ فردوسی در همین جعبه («ز یک میل کرد آفریدون نگاه») نشان می‌دهد که واژه تا حدود سال ۴۰۰ هجری کاملاً فارسی شده بود. این «میل» را نباید با دو هم‌آوای دیگر اشتباه گرفت: «مَیل» به معنای گرایش (از ریشهٔ عربی م‑ی‑ل) و «میل» به معنای سیخِ سرمه‌کشی (عربی از یونانیِ μήλη). ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D9%85%D9%8A%D9%84\",\n      \"https://abadis.ir/fatofa/%D9%85%DB%8C%D9%84/\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"MON:4505\",\n       \"status\": \"partial\",\n       \"note\": \"The 6-vol. pagination is not checkable online. The abridged Moʿin available at abadis.ir gives under میل only «[ع.] (اِ.) ۱- سیخ فلزی. ۲- یکی از ادوات ورزش باستانی» and «(مِ) [ع.] … خمیدن، رغبت، آرزو» — i.e. the 'rod' and 'inclination' homonyms, with the 'mile/road-marker' sense not present in the abridgement (it is in the 6-vol. print and in Moʿin's BQT footnote). Supports the Arabic tag [ع.] but the page and the exact sense could not be verified.\"\n      },\n      {\n       \"ref\": \"BQT:2080\",\n       \"status\": \"supports\",\n       \"note\": \"Same page as node 7. The headword «میل، بکسر اول بر وزن فیل، مقدار مسافتی باشد از روی زمین» is followed by Moʿin's footnote 4, «لاتینی milliarius از mille بمعنی هزار … و آن به ستون‌هایی اطلاق می‌شده که … در جاده‌ها نصب می‌کردند … و در فارسی هم باین معانی مستعمل است (مثلاً «میل نادری»)» — precisely Nourai's gloss 'a mile, a road marker' and precisely his Latin→Arabic→Persian route.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"BQT\",\n       \"where\": \"Borhan-e Qateʿ ed. Moʿin p. 2080 (ocr/BQT/2080.txt)\",\n       \"stance\": \"supports\",\n       \"note\": \"In addition to footnote 4, footnote 2 separates the homonym: «(عر) میل بالکسر، چوب سرمه‌کش … اصمعی گوید: قول العامة المیل ما تکحل به العین خطأ، انما هو المِلمول … و ظ. معرب است» — Moʿin himself keeps the kohl-stick apart from the road-mile.\"\n      },\n      {\n       \"src\": \"HRN\",\n       \"where\": \"Horn, Grundriss (grep 'mil' / 'Meile' in HRN.txt)\",\n       \"stance\": \"silent\",\n       \"note\": \"Horn treats only inherited Iranian words, and has no میل; his silence is consistent with the word being an Arabic loan rather than an inherited form.\"\n      },\n      {\n       \"src\": \"LKT\",\n       \"where\": \"Lokotsch, Etym. Wb. der europ. Wörter orient. Ursprungs (grep 'mille'/'Meile' in LKT.txt)\",\n       \"stance\": \"silent\",\n       \"note\": \"Lokotsch registers only Oriental words that entered European languages; میل travelled the other way, so it is absent — the direction Nourai draws (Latin → Arabic → Persian) is the one the literature assumes.\"\n      }\n     ]\n    },\n    {\n     \"id\": 10,\n     \"lang\": \"French\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"An empty pass-through box for French, standing for (a) the inherited French mille 'thousand' < Latin mīlle and (b) the learned metric prefix milli- coined in 1795 from Latin mīlle for the submultiples of the metric system (millimètre, milligramme, both 1795), plus (c) French million (borrowed from Italian milione, an augmentative of mille, 14th c.) and milliard (16th c., French formation on million with the suffix -ard). It is this French box, not the Latin one directly, that feeds the modern Persian and English words below.\",\n     \"derivation_fa\": \"این جعبهٔ خالی نمایندهٔ فرانسه است و سه چیز را دربر می‌گیرد: نخست mille «هزار» که واژه‌ای موروثی از لاتینیِ mīlle است؛ دوم پیشوندِ علمیِ milli- که در ۱۷۹۵ برای کسرهای دستگاه متری از mille لاتینی ساخته شد (millimètre و milligramme هر دو ۱۷۹۵)؛ سوم million (وام از ایتالیاییِ milione، صورت بزرگ‌ساز از mille، سدهٔ چهاردهم) و milliard (ساختِ فرانسویِ سدهٔ شانزدهم بر پایهٔ million). همین جعبهٔ فرانسوی است ــ و نه یکراست لاتینی ــ که واژه‌های فارسی و انگلیسیِ پایینِ نمودار را تغذیه می‌کند. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/million\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"AHD\",\n       \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. gheslo- lists MILLI-, MILLIEME, MILLION, MILLENARY, MILLESIMAL among the Latin-mille derivatives, i.e. the whole French-mediated set hangs on this box.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein 1966 leaf 525 (pp. 979/980), s.v. mile and cross-references\",\n       \"stance\": \"supports\",\n       \"note\": \"'Cp. mil, millennium, millesimal, million. Cp. also kilo-.' Klein groups the milli-/million family under L. mille exactly as the chart's French box does.\"\n      },\n      {\n       \"src\": \"Etymonline\",\n       \"where\": \"etymonline.com/word/million (archived)\",\n       \"stance\": \"supports\",\n       \"note\": \"'from Old French million …, from Italian millione (now milione), literally \\\"a great thousand\\\", augmentative of mille \\\"thousand\\\", from Latin mille'; milliard discussed s.v. billion as the French term for a thousand million.\"\n      }\n     ]\n    },\n    {\n     \"id\": 11,\n     \"lang\": \"Persian\",\n     \"words\": \"mîlî- «میلی»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian میلی milli- is the metric submultiple prefix, borrowed from French milli- along with the whole metric system in the first half of the 20th century, and it is used exactly as in French: میلی‌متر millimetr, میلی‌گرم milligeram. The two other words in the box are borrowings of the same family but of a different type: میلیون milyun 'million' (French million / Italian milione, in Persian since the Qajar period) and میلیارد milyārd 'milliard, thousand million' (French milliard). Moʿin defines the prefix as «یک‌هزارم واحد اصلی» 'one thousandth of the base unit', which is Nourai's gloss word for word. Because the prefix is French and not inherited, there is no Middle Persian stage and no sound change to describe — only orthographic adaptation (French -ll- reduced to a single ل, final -i written ی).\",\n     \"derivation_fa\": \"«میلی» در فارسی پیشوندِ کسرهای دستگاه متری است که همراه با خودِ دستگاه متری در نیمهٔ نخست سدهٔ چهاردهم خورشیدی از فرانسویِ milli- وام گرفته شد و درست مانند فرانسه به کار می‌رود: میلی‌متر، میلی‌گرم. دو واژهٔ دیگرِ داخل جعبه از همان خانواده‌اند اما گونهٔ دیگری از وام‌گیری: «میلیون» از million فرانسوی (اصلاً milione ایتالیایی) که از دورهٔ قاجار در فارسی رایج شده و «میلیارد» از milliard فرانسوی. معین این پیشوند را «یک‌هزارم واحد اصلی» تعریف کرده که واژه‌به‌واژه همان معنایی است که نورایی داده است. چون واژه وام‌واژهٔ فرانسوی است، نه مرحلهٔ فارسی میانه دارد و نه دگرگونی آواییِ درخوری؛ تنها سازگاریِ املایی رخ داده است (‑ll‑ فرانسوی به یک «ل»). ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://abadis.ir/fatofa/%D9%85%DB%8C%D9%84%DB%8C/\",\n      \"https://www.etymonline.com/word/million\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"MON:4507\",\n       \"status\": \"partial\",\n       \"note\": \"Page of the 6-vol. print not checkable online; the entry is, however, confirmed: Moʿin s.v. میلی gives «منسوب به میل» for the adjective and, for the prefix, «یک‌هزارم واحد اصلی» — Nourai's gloss 'one thousandth' exactly. The French origin tag is not shown in the abridged online text.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"MON\",\n       \"where\": \"abadis.ir/fatofa/میلی (فرهنگ معین section, archived)\",\n       \"stance\": \"supports\",\n       \"note\": \"«یک‌هزارم واحد اصلی» for the metric prefix.\"\n      },\n      {\n       \"src\": \"Etymonline\",\n       \"where\": \"etymonline.com/word/million (archived)\",\n       \"stance\": \"supports\",\n       \"note\": \"for میلیون/میلیارد: 'from Old French million, from Italian millione … augmentative of mille', and milliard as the French 'thousand million'.\"\n      }\n     ]\n    },\n    {\n     \"id\": 12,\n     \"lang\": \"English\",\n     \"words\": \"mile, millimeter, milligram, million, milliard\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Four of the five words fit the arrow, one does not. millimeter (1802), milligram (1802), million (late 14th c.) and milliard (1793) are indeed French borrowings, so for them French→English is right. But 'mile' is NOT French: Old English mīl (pl. mīla) is a West Germanic borrowing made from Latin milia (passuum) in the Roman period, the Latin neuter plural having been reinterpreted as a feminine singular *milja — whence also Middle Dutch mile, Old High German mīla, German Meile. Klein states it flatly ('mile, n. — ME., fr. OE. mil, pl. mila, mile, fr. L. milia, pl. of mille'), and Etymonline says the same, adding 'the neuter plural was mistaken in Germanic as a fem. singular'. French mille never gave an English 'mile'. The chart should have drawn mile straight from the Latin box; as printed, the node is wrong for its first and most prominent word.\",\n     \"derivation_fa\": \"از پنج واژهٔ این جعبه چهار تا با پیکانِ نمودار می‌خوانند و یکی نمی‌خواند. millimeter و milligram (هر دو ۱۸۰۲)، million (پایان سدهٔ چهاردهم) و milliard (۱۷۹۳) براستی وام‌واژه‌های فرانسوی‌اند. اما mile فرانسوی نیست: انگلیسی باستان mīl (جمع mīla) وام‌واژه‌ای است که ژرمنیِ غربی در دورهٔ روم یکراست از لاتینیِ milia (passuum) گرفته و جمعِ خنثای لاتینی را مفردِ مؤنث *milja پنداشته است؛ از همین‌جاست هلندی میانه mile، آلمانی علیای باستان mīla و آلمانیِ Meile. کلاین (ص ۹۷۹) و اتیمولاین هر دو همین را می‌گویند. پس پژوهش امروزی این پیکان را رد می‌کند: mile باید یکراست از جعبهٔ لاتینی می‌آمد، نه از فرانسه. حکم این گره «رد‌شده» است، هرچند چهار واژهٔ دیگرِ همان جعبه درست‌اند.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/mile\",\n      \"https://www.etymonline.com/word/million\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"None\",\n       \"status\": \"not_checked\",\n       \"note\": \"No reference is given for this box in the book; the claim is tested against Klein (p. 979), Watkins and Etymonline below.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein 1966 leaf 525 (printed pp. 979/980) s.v. mile\",\n       \"stance\": \"contradicts\",\n       \"note\": \"'mile, n. — ME., fr. OE. mil, pl. mila, mile, fr. L. milia, pl. of mille, \\\"a thousand\\\" (in … milia passuum …).' No French stage at all: Old English straight from Latin.\"\n      },\n      {\n       \"src\": \"Etymonline\",\n       \"where\": \"etymonline.com/word/mile (archived)\",\n       \"stance\": \"contradicts\",\n       \"note\": \"'from Latin milia \\\"thousands\\\" … the neuter plural was mistaken in Germanic as a fem. singular', giving West Germanic *milja > OE mīl, MDu. mile, OHG mīla, German Meile; French mille, Italian miglio, Spanish milla are listed as the separate Romance line.\"\n      },\n      {\n       \"src\": \"AHD\",\n       \"where\": \"Watkins 1985 index (AHD_watkins1985.txt lines 1869-1871)\",\n       \"stance\": \"partial\",\n       \"note\": \"'MILE gheslo- … MILLI- gheslo- … MILLION gheslo-' — the root is right for all of them, but Watkins does not distinguish the routes, so he neither supports nor refutes the French mediation.\"\n      },\n      {\n       \"src\": \"FSD\",\n       \"where\": \"Funk & Wagnalls vol. 3 s.v. mile / mileage (FSD_vol3.txt lines 22728, 38268 ff.)\",\n       \"stance\": \"silent\",\n       \"note\": \"The scan's OCR of the etymology brackets in this column is unreadable; only the definitional matter ('statute m., the legal mile of the United States, Great Britain, etc., 5,280 feet: fixed in the reign of Queen Elizabeth') comes through. No etymological evidence obtainable from this copy.\"\n      }\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Ghesto, Ghosto\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ǵʰes-to- 'hand, arm' (beside *ǵʰes-ōr / *ǵʰesr- 'hand'), from a base *ǵʰes-\",\n   \"note\": \"Pokorny IEW 447 has two consecutive entries: '1. ghesor-, ghesr- ,Hand'?' and '2. ghesto- ,Hand; Arm'', the second containing exactly Nourai's material — 'Ai. hásta-ḥ m. \\\"Hand\\\", av. zasta-, apers. dasta- ds.; … lit. pa-žastė, pa-žastis f. \\\"Raum unterm Arm, Achselhöhle\\\"'. Walde-Pokorny I 541 has the same headword ('ghesto- \\\"Hand, Arm\\\"'). The second name in Nourai's box, 'Ghosto', is not a variant he invented: it is the o-vocalism written by Kent (Old Persian, p. 190: 'dasta- sb. \\\"hand\\\": Av. zasta-, N Pers. dast, Skt. hásta-, pIE *ghosto-') and by Klein (s.v. abdest: 'Pers. dast, \\\"hand\\\", is rel. to Avestic zasta, \\\"hand\\\", fr. I.-E. base *ghosto-'), both of which Nourai cites in node 1. So the root box, its language label and its gloss are all right, and the doublet of names is sourced. Two caveats worth recording: (a) Watkins/AHD carries only 'ghesor-. Hand.' and no *ghes-to-, because no English word descends from the to-stem; (b) Pokorny himself, following Belardi, wonders whether the whole 'hand' group should not be separated from a root *gher- 'grasp', and Walde-Pokorny puts Gk. kheír, Arm. jern, Toch. tsar under '4. gher- \\\"greifen, fassen\\\"' (WP I 603) rather than under *ghesor-. None of this touches the Indo-Iranian branch that the chart actually uses. Note also that Wiktionary derives the *ǵʰeslom 'thousand' of the previous chart from this very *ǵʰes- 'hand' ('a full hand'), so the two entries on page 161 are, on the modern view, one family.\",\n   \"note_fa\": \"پوکورنی در صفحهٔ ۴۴۷ دو مدخلِ پیاپی دارد: «۱. ghesor-، ghesr- «دست»؟» و «۲. ghesto- «دست؛ بازو»»، و مدخل دوم دقیقاً همان مواد نمودار را دارد: «سنسکریت hásta-، اوستایی zasta-، پارسی باستان dasta-؛ لیتوانیایی pa-žastė «زیر بغل»». والده‑پوکورنی نیز در جلد ۱ ص ۵۴۱ همین سرواژه را با معنای «دست، بازو» آورده است. نامِ دومِ جعبه، یعنی «Ghosto»، ساختهٔ نورایی نیست: صورتِ o‑دار را کنت در فرهنگ پارسی باستان (ص ۱۹۰) و کلاین (ذیل abdest) نوشته‌اند و هر دو در همان گره ۱ استناد شده‌اند. پس جعبهٔ ریشه، برچسبِ زبان و معنا درست است. دو نکته را باید ثبت کرد: نخست آنکه واتکینز تنها ghesor- را آورده و ghesto- ندارد، زیرا هیچ واژهٔ انگلیسی از آن نمی‌آید؛ دوم آنکه خودِ پوکورنی به پیروی از بلاردی تردید می‌کند که آیا نباید این خانواده را از ریشهٔ *gher- «گرفتن» جدا کرد ــ ولی هیچ‌یک از این دو نکته به شاخهٔ هندوایرانیِ مورد استفادهٔ نمودار آسیبی نمی‌زند. جالب آنکه ویکی‌واژه ریشهٔ «هزار» در نمودارِ پیشین را از همین *ǵʰes- «دست» («یک دستِ پُر») می‌گیرد؛ یعنی دو نمودارِ این صفحه در دیدگاه امروزی یک خانواده‌اند.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%D8%AF%D8%B3%D8%AA\",\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0%C3%A9slom\"\n   ],\n   \"ref_check\": [\n    {\n     \"ref\": \"POK:447\",\n     \"status\": \"supports\",\n     \"note\": \"POK_02.txt leaf 104 (the page number '447' is printed in the block): '1. ghesor-, ghesr- ,Hand'? … 2. ghesto- ,Hand; Arm'. Ai. hásta-ḥ m. ,Hand', av. zasta-, apers. dasta- ds.; lat. praestō ,zur Hand' aus *prae-hestōd (EM 805 f.)?; … lit. pa-žastė, pa-žastis f. ,Raum unterm Arm, Achselhöhle'.' Same text in POK_full.txt lines 37188-37225, 'Page(s): 447'.\"\n    }\n   ],\n   \"consulted\": [\n    {\n     \"src\": \"WLD\",\n     \"where\": \"Walde-Pokorny Bd. I 541 (incoming/WLD/WLD_Bd1_pages.txt line 50967; the running head 'ghesto- — ghe-, gho-  541' is on the same leaf)\",\n     \"stance\": \"supports\",\n     \"note\": \"'ghesto- „Hand, Arm“. Ai. hasta- m. „Hand“, hastavant „hand versehen“, av. zasta-, apers. dasta- m. „Hand, und zwar ahurischer Wesen“, zastavant „tatkräftig“; lit. pažastis f., pažastė „Raum unterm Arm, Achselhöhle“.' The source of Pokorny's entry, with the identical gloss.\"\n    },\n    {\n     \"src\": \"AHD\",\n     \"where\": \"Watkins 1985, g-list (AHD_watkins1985.txt line 524)\",\n     \"stance\": \"partial\",\n     \"note\": \"'ghesor-. Hand. Reduced form *ghesr- in Greek kheir, hand: CHIRO-; (CHIRURGEON), ENCHIRIDION, (SURGEON), SURGERY. [Pok. 1. ghesor- 447.]' — Watkins gives the r-stem only; the to-stem that the chart uses is absent from his list, so he is silent on 'Ghesto/Ghosto' as such while confirming the base and its meaning.\"\n    },\n    {\n     \"src\": \"IEC\",\n     \"where\": \"Mann, An IE Comparative Dictionary (grep 'ghest' / 'ghesr' in IEC.txt)\",\n     \"stance\": \"silent\",\n     \"note\": \"Mann has gheslos and ghesmn- but no *ghesto-/*ghesor- headword; his dictionary simply does not carry this root.\"\n    }\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan / Old Persian\",\n     \"words\": \"zasta; dasta; dasta-karta; abi-dasta, a-dsta\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"zasta- is the Avestan and dasta- the Old Persian word for 'hand' (Av. zasta- m., Bartholomae col. 1685 'j.-, g. zasta-, p. dasta- m. \\\"Hand\\\"'; OP dasta-, attested in the instrumental dual dastaibiya DNb 41 and dastayā DB 4.35). Both continue *ǵʰes-to-: PIE *ǵʰ gives Indo-Iranian ȷ́ʰ > Av. z, while Old Persian shows the regular Persic reflex d (the same correspondence as Av. zim- : OP dim-, Av. zasta- : OP dasta-, later NPers. dast). dasta-karta- 'hand-made' is genuinely attested in Old Persian (Kent p. 190 'dastakarta- adj. \\\"handmade\\\": dasta- + pte. karta-, to kar- \\\"make\\\"'), and survives as MP dastgird / Arm. dastakert 'estate' (Hübschmann, Pers. Stud., 'arm. dastakert \\\"Ansiedelung\\\" = mp. dastagird, arab. dastajird oder daskara'); Nourai's cross-reference to the root Kwer (*kʷer- 'to make') for -karta- is correct. The last item, 'abi-dasta, a-dsta : over hands, sleeve', is different in kind: these are not attested Old Iranian words but Gershevitch's starred reconstructions *abi-dasta(na)- and *ā-d(a)st- proposed to explain āstīn 'sleeve' (Avestan Hymn to Mithra p. 220 n., and index p. 291 '*abi-dasta(na)-, 220 n.'; '*pati-dastana-, 220 n.'). Since the box prints them without asterisks alongside two attested words, the node as a whole can only be called plausible.\",\n     \"derivation_fa\": \"zasta- صورتِ اوستایی و dasta- صورتِ پارسی باستانِ «دست» است (بارتولومه، ستون ۱۶۸۵: «اوستایی متأخر و گاهانی zasta-، پارسی باستان dasta- «دست»»؛ در پارسی باستان به صورتِ dastaibiya در DNb ۴۱ و dastayā در DB ۴٫۳۵ گواهی شده). هر دو دنبالهٔ *ǵʰes-to- هندواروپایی‌اند: *ǵʰ در هندوایرانی ȷ́ʰ و در اوستایی z شده، حال آنکه پارسی باستان بازتابِ ویژهٔ پارسی یعنی d را نشان می‌دهد (همان تناظری که در zim- اوستایی برابرِ dim- پارسی باستان دیده می‌شود). dasta-karta- «دست‌ساخت» براستی در پارسی باستان گواهی شده (کنت، ص ۱۹۰) و در فارسی میانه «دستگرد» و در ارمنی dastakert «آبادی» بازمانده است؛ ارجاعِ نورایی به ریشهٔ Kwer برای جزء ‑karta- درست است. اما آخرین قلم، یعنی «abi-dasta، a-dsta»، از جنسِ دیگری است: این‌ها واژه‌های گواهی‌شدهٔ ایرانی باستان نیستند بلکه بازسازی‌های ستاره‌دارِ گرشویچ‌اند (*abi-dasta(na)- و *ā-d(a)st-) که برای توضیحِ «آستین» پیشنهاد شده‌اند. چون کتاب آن‌ها را بی‌ستاره و در کنارِ دو واژهٔ گواهی‌شده چاپ کرده، حکمِ این گره «با احتیاط پذیرفتنی» است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D8%AF%D8%B3%D8%AA\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"POK:447\",\n       \"status\": \"supports\",\n       \"note\": \"POK_02.txt leaf 104 (p. 447), s.v. 2. ghesto-: 'Ai. hásta-ḥ m. ,Hand', av. zasta-, apers. dasta- ds.' — the Avestan and Old Persian forms exactly as drawn.\"\n      },\n      {\n       \"ref\": \"KLN:707\",\n       \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 381 (printed pp. 707/708), s.v. hasta: 'OI. hástaḥ, \\\"hand; trunk of an elephant\\\", rel. to Avestic zasta-, OPers. dasta- (whence Pers. dast), \\\"hand\\\", and cogn. with Lith. pažastė, \\\"armpit\\\".' Klein's related entry abdest adds 'fr. I.-E. base *ghosto-', which is where Nourai's second root name comes from.\"\n      },\n      {\n       \"ref\": \"KNT:190\",\n       \"status\": \"supports\",\n       \"note\": \"KNT.txt form-feed leaf 213 carries the running head '190 OLD PERSIAN' and the entry: 'dasta- sb. \\\"hand\\\": Av. zasta-, N Pers. dast, Skt. hásta-, pIE *ghosto- (§88, §116, §145). See also dastakarta-. dastayā ism. DB 4.35. dastaibiya idm. (§189) DNb 41.' followed immediately by 'dastakarta- adj. \\\"handmade\\\": dasta- + pte. karta- (§160.10), to kar- \\\"make\\\".' Kent supports both dasta- and dasta-karta- and is the source of the spelling *ghosto-.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"BRT\",\n       \"where\": \"Bartholomae, Altiran. Wb. col. 1685 (BRT.txt line 28005)\",\n       \"stance\": \"supports\",\n       \"note\": \"'j.-, g. zasta-, p. dasta- m. \\\"Hand\\\", uzw. ahurischer Wesen … KompA. (zasta-, zastō-; HD.), E.; Ableit. — ai. hásta- m., np. dast. — Pü.: dast, har a dast.' Avestan, Old Persian, Sanskrit, Middle and New Persian in one entry.\"\n      },\n      {\n       \"src\": \"AHM\",\n       \"where\": \"Gershevitch, The Avestan Hymn to Mithra p. 220 n. (AHM.txt line 1978; index line 3080)\",\n       \"stance\": \"partial\",\n       \"note\": \"'Bearing in mind Yidγa avlásta \\\"sleeve\\\" < *uda-dasta- (Morg.), and the Pahl. word which Nyberg reads *apasast … *abista(na)ka-, this may be a reduction of *abi-d(a)sta-(na)ka-, comparable to that which according to H. W. Bailey … took place in Oss. fiston, Dig. festonæ \\\"handle\\\" < *pati-dastanæ, cf. Khot. dastānya \\\"handle\\\" … Perhaps NPers. āstīn \\\"sleeve\\\" similarly goes back to *ā-d(a)st-.' The index confirms the page: '*abi-dasta(na)-, 220 n.'; '*pati-dastana-, 220 n.'. So the forms are Gershevitch's, but explicitly hypothetical ('perhaps').\"\n      },\n      {\n       \"src\": \"HUB\",\n       \"where\": \"Hübschmann, Persische Studien (HUB.txt lines 4535-4536, 2185-2186)\",\n       \"stance\": \"supports\",\n       \"note\": \"'arm. dastakert \\\"Ansiedelung\\\" = mp. dastagird, arab. dastajird oder daskara' and 'arm. LW. dastak \\\"Handwurzel\\\" (np. dasta \\\"Handvoll, Griff\\\"), afgh. dasta f. \\\"a handle\\\"' — the afterlife of dasta-karta- and of the stem generally.\"\n      }\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"dast «دست»; âstîn «آستین»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"دست dast 'hand' is the straightforward continuation: OP dasta- > MP dast (Book Pahlavi written with the arameogram YDH, Manichaean dst') > NPers. dast, with loss of the final thematic vowel in the Middle Persian period and no further change; Nyberg's glossary and MacKenzie both list it, and Moʿin's footnote on BQT 854 gives the whole cognate row. The compounds shown, دستار dastār 'turban' and دستگاه dastgāh 'apparatus, workshop, (musical) mode', are Persian formations on dast. آستین āstīn 'sleeve' is the doubtful item. Nourai follows Gershevitch (AHM 220 n.) in taking it from *ā-d(a)st- / *abi-dasta(na)-, i.e. 'that which is over/around the hand', with loss of the intervocalic d after the prefix and the -ān(a)- suffix giving -īn. This is only one of several proposals: Wiktionary calls āstīn 'of unknown etymology due to not having any clear cognates' and reports Herzenberg's alternative, a borrowing from a south-eastern Iranian language of the type of Pashto lastúṇay 'sleeve' (itself from lās 'hand' < *dasta-, with the eastern d- > l- shift), the Persian form having lost the initial l-. Both accounts start from *dasta- 'hand', so the arrow's family is safe; the specific prefix is not. The variants printed in parentheses on the page, آستن and آستیم, are genuine: Borhan-e Qateʿ has both as headwords (BQT vol. 1: «آستیم، بفتح اول بروزن تسلیم، آستین»).\",\n     \"derivation_fa\": \"«دست» دنبالهٔ بی‌دردسرِ پارسی باستانِ dasta- است: dasta- ← فارسی میانهٔ dast (به خط پهلوی با هزوارشِ YDH، مانوی dst') ← فارسی نو «دست»؛ تنها تحول، افتادنِ واکهٔ پایانیِ ستاک در دورهٔ میانه است. ترکیب‌های «دستار» و «دستگاه» ساخت‌های فارسیِ همین واژه‌اند. اما «آستین» قلمِ تردیدآمیزِ این جعبه است. نورایی به پیروی از گرشویچ (ص ۲۲۰ حاشیه) آن را از *ā-d(a)st- / *abi-dasta(na)- یعنی «آنچه بر/گردِ دست است» می‌گیرد، با افتادنِ «د» پس از پیشوند و بدل‌شدنِ پسوندِ ‑ān(a)‑ به ‑īn. این تنها یکی از چند پیشنهاد است: ویکی‌واژه ریشهٔ «آستین» را «ناشناخته» می‌خواند و پیشنهاد هرتسنبرگ را می‌آورد که آن را وام‌واژه‌ای از زبانی ایرانیِ جنوب‌شرقی از گونهٔ پشتوِ lastúṇay «آستین» (از lās «دست» با ابدالِ d ← l در ایرانیِ شرقی) می‌داند که «ل» آغازینش افتاده است. هر دو تبیین از *dasta- «دست» آغاز می‌کنند؛ پس خانوادهٔ واژه درست است ولی پیشوندِ ویژه مسلّم نیست. گونه‌های داخل پرانتزِ صفحه، «آستن» و «آستیم»، ساختگی نیستند و در برهان قاطع سرواژه‌اند («آستیم، بفتح اول بروزن تسلیم، آستین»). حکم: با احتیاط پذیرفتنی است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D8%AF%D8%B3%D8%AA\",\n      \"https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D8%AA%DB%8C%D9%86\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"BQT:854\",\n       \"status\": \"supports\",\n       \"note\": \"Borhan-e Qateʿ ed. Moʿin, printed p. 854 = form-feed leaf 314 of BQT_v2_pages.txt (the leaf carrying the دژ…/دس entries just before دست on p. 855). Moʿin's footnote 1 there runs: «پهلوی dast، پارسی باستان dasta- «بارتولمه» … اوستا zasta-، هندی باستان hasta-، کردی dest، بلوچی … وخی dast, شغنی dōst, سریکلی dūst, منجی last …» and is continued on the next page («بقیه در صفحهٔ ۸۵۴/۸۵۵») with «سغدی δst … ارمنی dastak … افغانی dasta (دسته) «هوبشمان» … اورامانی dast … گیلکی dast … معرب آن …». Exactly the Old Iranian → Persian arrow, and it even supplies the Sogdian cognate of node 3.\"\n      },\n      {\n       \"ref\": \"AHM:220\",\n       \"status\": \"partial\",\n       \"note\": \"Gershevitch p. 220 n. (AHM.txt line 1978): 'Perhaps NPers. āstīn \\\"sleeve\\\" similarly goes back to *ā-d(a)st-.' The reference does say what Nourai's arrow says, but with 'perhaps'; Gershevitch's own preferred reading there is *abi-sta-/*abista(na)ka- as a reduction of *abi-d(a)sta-(na)ka-.\"\n      },\n      {\n       \"ref\": \"MON\",\n       \"status\": \"not_checked\",\n       \"note\": \"Nourai gives 'MON' without a page, so nothing specific can be looked up; the online Moʿin s.v. دست carries the tag [په.] (Pahlavi), consistent with the chart but not a page-verifiable citation.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"HRN\",\n       \"where\": \"Horn, Grundriss no. 567 (HRN.txt lines 5105-5108)\",\n       \"stance\": \"supports\",\n       \"note\": \"'567. dest \\\"Hand\\\", vergl. destek, deste (arab. dastaj), destī \\\"Hilfe\\\". ap. dasta- \\\"Hand\\\"; aw. zasta-; phlv. dast; ai. hásta-. Allgemein entlehnt: kurd. dest; afγ. lās …, dast; bel. dast; waχ. δast, šiγn. δōst, sar. δūst, sangl. dast, minj. last, yidγ. lust.'\"\n      },\n      {\n       \"src\": \"PHD\",\n       \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD_mackenzie.txt lines 1911-1915)\",\n       \"stance\": \"supports\",\n       \"note\": \"The dast- family is fully entered: 'dast(a)gird [YDE-, dst-krt | M dstygyrd, N dastgird] estate', 'dast-karīh [YDEk'lyh] handiwork' etc., i.e. MP dast written with the arameogram YDE/YDH — the Middle Persian stage the chart passes over silently.\"\n      },\n      {\n       \"src\": \"NYB\",\n       \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt lines 1205, 483)\",\n       \"stance\": \"supports\",\n       \"note\": \"'dast [YDH, Prth YD'; dst'], with the indef. art. dast-ē [YDH + 1] 1. hand … ; power …' and, relevant to āstīn, 'apa-dast [ʾpdst!] \\\"what is on the hand\\\" = glove, or the like, 85¹⁸. — < *upa-dasta-' — a real Middle Persian *prefix + dasta-* compound of exactly the type Nourai's abi-dasta assumes.\"\n      },\n      {\n       \"src\": \"BQT\",\n       \"where\": \"Borhan-e Qateʿ vol. 1 s.vv. آستن, آستیم (BQT_v1_pages.txt lines 5983, 11942)\",\n       \"stance\": \"supports\",\n       \"note\": \"«آستن، پارچهٔ جامه را گویند …» and «آستیم، بفتح اول بروزن تسلیم، آستین» — the two parenthesised variants on the chart are Borhan's own headwords, so the extraction and the book are both right there.\"\n      },\n      {\n       \"src\": \"Wiktionary\",\n       \"where\": \"en.wiktionary.org/wiki/آستین (archived)\",\n       \"stance\": \"partial\",\n       \"note\": \"'of unknown etymology due to not having any clear cognates'; Herzenberg's proposal connects it to Pashto لستوڼي lastúṇay 'sleeve' (to لاس lās 'hand'), with the eastern Iranian d- > l- shift and loss of l- in the Persian form; first attested in Ferdowsī, c. 1010. So the *ā-dasta- derivation is one hypothesis among several.\"\n      }\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Sogdian\",\n     \"words\": \"dst\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Sogdian ẟst is the consonantal spelling of δast 'hand, arm', the regular Sogdian outcome of Old Iranian *dasta- (Sogdian shifts initial *d- to the fricative δ, written ẟ/δ in Gharib's transcription; the Christian Sogdian orthography writes it d, whence the 'dst' of the chart). Gharib's entry 3640 gives it with its case forms and derives it explicitly from Old Persian dasta-; her entry 3653 ẟstwβ'ry 'handiwork' and 3652 ẟstβrtr show the stem in compounds. Note that Nourai draws the arrow from the Avestan/Old Persian box, which is right: Sogdian is a sister of Persian, not its descendant, and both go back to the same Old Iranian *dasta-.\",\n     \"derivation_fa\": \"«dst» سغدی همان δast «دست، بازو» است که بازتابِ منظمِ ایرانی باستانِ *dasta- در سغدی است؛ در سغدی «د» آغازین به سایشیِ δ بدل می‌شود (غریب آن را ẟ می‌نویسد و املای سغدیِ مسیحی آن را d می‌نگارد، و همین املا در نمودار آمده است). غریب در مدخل ۳۶۴۰ این واژه را با صورت‌های صرفی‌اش می‌آورد و آشکارا از پارسی باستانِ dasta- می‌گیرد؛ مدخل‌های ۳۶۵۳ (ẟstwβ'ry «دست‌ساخته») و ۳۶۵۲ نیز همین ستاک را در ترکیب نشان می‌دهند. پیکانی که نورایی از جعبهٔ اوستایی/پارسی باستان کشیده درست است، چون سغدی خواهرِ فارسی است نه فرزندِ آن و هر دو از یک صورتِ ایرانی باستان می‌آیند. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D8%AF%D8%B3%D8%AA\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"SOD:144\",\n       \"status\": \"supports\",\n       \"note\": \"Gharib, Sogdian Dictionary, entry 3640, on form-feed leaf 209 of SOD_pages.txt (printed page ≈ 143/144 by the leaf−66 offset given in refs_online.json — i.e. Nourai's page number is right to within the scan's one-page tolerance): '3640 ẟst B, M, S | δast- (dst) < OP dasta- ⟨nom.; ob. -y; acc. -w; loc. -y/-yh; abl. -ɂ; pl. -tɂ⟩ … hand, arm | GMS 364, 516, 1171, 1179, 1183-4'. Neighbouring entries 3652-3654 (ẟstβrtr, ẟstwβ'ry 'handiwork', ẟstw pr-) are on the same leaf.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"SOD\",\n       \"where\": \"Gharib entry 3640 (SOD_pages.txt leaf 209)\",\n       \"stance\": \"supports\",\n       \"note\": \"See the quotation above; Gharib's own etymological note '< OP dasta-' is the same arrow the chart draws.\"\n      },\n      {\n       \"src\": \"BQT\",\n       \"where\": \"Moʿin's footnote to دست, continued on BQT p. 855 (BQT_v2_pages.txt leaf 315)\",\n       \"stance\": \"supports\",\n       \"note\": \"The cognate row printed there includes the Sogdian form alongside Ossetic, Armenian and Pashto, with references to Hübschmann and Pedersen.\"\n      },\n      {\n       \"src\": \"HRN\",\n       \"where\": \"Horn, Grundriss no. 567 (HRN.txt line 5107)\",\n       \"stance\": \"partial\",\n       \"note\": \"Horn lists the eastern-Iranian cognates 'waχ. δast, šiγn. δōst, sar. δūst, sangl. dast, minj. last, yidγ. lust' — the same δ- reflex as Sogdian, though he does not name Sogdian itself.\"\n      }\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Sanskrit\",\n     \"words\": \"hastah\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Sanskrit हस्त hásta-ḥ (nom. sg. of the masculine a-stem hásta-) 'hand; forearm; trunk of an elephant; the 13th lunar mansion' continues *ǵʰes-to- directly: PIE palatal *ǵʰ gives Indo-Iranian ȷ́ʰ, which in Old Indic becomes h (the same h as in hi-, hima- etc.), while Iranian gives z (Av. zasta-) and Persic d (OP dasta-). The word is Vedic (RV hásta- passim, e.g. hástena 'with the hand'), so the arrow root→Sanskrit is as well founded as such an arrow can be.\",\n     \"derivation_fa\": \"«hastah» همان हस्त hásta-ḥ سنسکریت است (صورتِ فاعلیِ مفردِ ستاکِ a‑دارِ مذکرِ hásta-) به معنای «دست، ساعد، خرطومِ فیل». این واژه یکراست دنبالهٔ *ǵʰes-to- است: کامیِ *ǵʰ هندواروپایی در هندوایرانی ȷ́ʰ و در هندیِ باستان h شده، حال آنکه در ایرانی z (اوستایی zasta-) و در پارسی d (پارسی باستان dasta-) داده است. این واژه ودایی است (در ریگ‌ودا بارها آمده)، پس پیکانِ ریشه ← سنسکریت استوارترین حالتِ ممکن را دارد. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D8%AF%D8%B3%D8%AA\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"POK:447\",\n       \"status\": \"supports\",\n       \"note\": \"POK_02.txt leaf 104 (p. 447), s.v. 2. ghesto-: 'Ai. hásta-ḥ m. ,Hand'' is the first form cited under the root.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"WLD\",\n       \"where\": \"Walde-Pokorny Bd. I 541\",\n       \"stance\": \"supports\",\n       \"note\": \"'Ai. hasta- m. „Hand“, hastavant „hand versehen“' heads the entry ghesto- 'Hand, Arm'.\"\n      },\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein 1966 p. 707 s.v. hasta\",\n       \"stance\": \"supports\",\n       \"note\": \"'OI. hástaḥ, \\\"hand; trunk of an elephant\\\", rel. to Avestic zasta-, OPers. dasta- …, and cogn. with Lith. pažastė, \\\"armpit\\\".'\"\n      },\n      {\n       \"src\": \"BRT\",\n       \"where\": \"Altiran. Wb. col. 1685 s.v. zasta-\",\n       \"stance\": \"supports\",\n       \"note\": \"the cognate line 'ai. hásta- m., np. dast' pairs the Sanskrit and Persian forms under the Avestan headword.\"\n      }\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"English\",\n     \"words\": \"hasta\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English 'hasta' is a technical Indological borrowing of Sanskrit hásta-, current in two senses: (1) the codified hand-gestures of Indian classical dance and iconography (hasta / hasta-mudrā, from the Nāṭyaśāstra tradition), and (2) the cubit measure of hasta = 24 aṅgula. It entered English through 19th-c. Orientalist scholarship, not through any inherited route, and Nourai's gloss reproduces Klein's wording exactly. It must be kept apart from the unrelated Latin hasta 'spear' (whence hastate, haslet), which Klein files separately and connects with Gothic gazds 'goad'.\",\n     \"derivation_fa\": \"«hasta» در انگلیسی وام‌واژه‌ای فنی از سنسکریتِ hásta- است که از راهِ خاورشناسیِ سدهٔ نوزدهم وارد شده، نه از راهِ میراثِ زبانی، و دو کاربرد دارد: نخست حرکاتِ رمزیِ دست در رقص و پیکرنگاریِ کلاسیک هند (hasta/hasta-mudrā در سنتِ ناتیه‌شاستره) و دوم واحدِ درازای «هَستَه» برابرِ ۲۴ انگشت. معنایی که نورایی داده واژه‌به‌واژه از کلاین (ص ۷۰۷) گرفته شده است. این واژه را نباید با hasta لاتینی به معنای «نیزه» (که hastate و haslet انگلیسی از آن است) اشتباه گرفت؛ کلاین آن را مدخلِ جداگانه و هم‌ریشه با گوتیِ gazds «سیخ» می‌داند. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D8%AF%D8%B3%D8%AA\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"KLN:707\",\n       \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 381, which carries the printed page numbers 707 and 708: 'hasta, n., 1) symbolic position of the hands in dancing; 2) a cubit (measure). — OI. hástaḥ, \\\"hand; trunk of an elephant\\\", rel. to Avestic zasta-, OPers. dasta- (whence Pers. dast), \\\"hand\\\", and cogn. with Lith. pažastė, \\\"armpit\\\". Cp. hath and the second element in abdest.' Nourai's gloss is Klein's sense 1 verbatim, and the page number is exactly right.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein 1966 p. 707, entries hasta, hastate, hath, and p. 2 s.v. abdest\",\n       \"stance\": \"supports\",\n       \"note\": \"Klein separates 'hastate, adj., spearlike … — L. hastatus … fr. hasta, \\\"shaft, spear\\\", which is cogn. with Goth. gazds' from the Indic hasta, and at abdest writes 'Pers. dast, \\\"hand\\\", is rel. to Avestic zasta, \\\"hand\\\", fr. I.-E. base *ghosto-, whence also OI. hastah, \\\"hand\\\". See hasta and cp. hath.'\"\n      },\n      {\n       \"src\": \"HJB\",\n       \"where\": \"Hobson-Jobson (grep 'hasta' in HJB.txt)\",\n       \"stance\": \"silent\",\n       \"note\": \"Yule & Burnell have no 'hasta' article — the word is a scholarly Sanskritism rather than an Anglo-Indian colloquialism, which is consistent with the learned route described above.\"\n      },\n      {\n       \"src\": \"FSD\",\n       \"where\": \"Funk & Wagnalls (grep 'hasta' in FSD volumes)\",\n       \"stance\": \"silent\",\n       \"note\": \"Not carried by the Standard Dictionary; the term belongs to specialist Indological vocabulary, so its absence from a general dictionary is expected.\"\n      }\n     ]\n    }\n   ]\n  }\n ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-191.json > /dev/null && echo \"JSON OK\"",
 "description": "Write verification file for page 191"
}
```


### [2026-09-06T02:31:57.490Z] TOOL RESULT

```
JSON OK
```


## [2026-09-06T02:32:01.590Z] TOOL CALL #89: Bash

```json
{
 "command": "python3 tools/verify_check.py 191",
 "description": "Run verify_check for page 191"
}
```


### [2026-09-06T02:33:11.820Z] TOOL RESULT

```
nodes verified: 17/17
node verdicts: {'confirmed': 13, 'transcription_suspect': 1, 'disputed': 1, 'plausible': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 17, 'partial': 5, 'not_checked': 3}
books consulted: {'supports': 33, 'silent': 7, 'partial': 6, 'contradicts': 3} | by book: {'KLN': 8, 'HRN': 5, 'Etymonline': 5, 'BRT': 4, 'BQT': 4, 'AHD': 3, 'PHD': 2, 'IEC': 2, 'MON': 2, 'WLD': 2, 'Wiktionary': 2, 'FSD': 2, 'POK': 1, 'BOOK': 1, 'LKT': 1, 'AHM': 1, 'HUB': 1, 'NYB': 1, 'SOD': 1, 'HJB': 1}
```


## [2026-09-06T02:33:30.014Z] AGENT

Page 191 (book p. 161) verified; `verify_check.py 191` reports **0 PROBLEM lines**, 17/17 nodes.

**Counts** — roots: 2 confirmed. Nodes: 13 confirmed, 2 plausible, 1 disputed, 1 transcription_suspect. Ref checks: 17 supports, 5 partial, 3 not_checked. 20 books/sites consulted (POK, WLD Bd I, AHD/Watkins, IEC, KLN, KNT, BRT, HRN, HUB, PHD, NYB, SOD, AHM, BQT vols 1/2/4, MON, LKT, HJB, FSD, Wiktionary, Etymonline).

**disputed**
- *Gheslo* #12 English `mile, millimeter, milligram, million, milliard` — the box hangs all five off French, but `mile` is not French: OE mīl is a West-Germanic borrowing straight from Latin *milia (passuum)*, the neuter plural reanalysed as fem. sg. *milja (Klein p. 979; Etymonline). The other four are genuine French loans.

**transcription_suspect** (`error_in: "book"` — extraction is faithful; page image saved to `data/verification/sources/refs/ocr/BOOK/191.png`)
- *Gheslo* #7 Latin — the book prints `milia pasuum` (for *milia passuum*), `milie` (for *mille*, while its own NOTE writes "millia"/"millie"), and glosses `smî-gžlî` as "one thousandth" although Pokorny's *smī gzhlī is "eine Tausendheit" = *one thousand*. Substance is only *plausible* anyway: Walde-Pokorny I 633 rejects mille < *smi-ghslī outright, Pokorny 1959 says "vielleicht", Watkins "of obscure origin"; only de Vaan re-accepts it. Nourai's own NOTE fairly flags the doubt.

**plausible**
- *Ghesto* #1 — `abi-dasta, a-dsta` are printed unasterisked beside two attested words, but they are Gershevitch's reconstructions (*abi-dasta(na)-, *ā-d(a)st-, AHM p. 220 n. — page confirmed via the book's index). `zasta`, `dasta`, `dasta-karta` all attested (Kent p. 190 verified, leaf carries the running head "190 OLD PERSIAN").
- *Ghesto* #2 — `dast` confirmed, but `âstîn` is called "of unknown etymology" by Wiktionary (Herzenberg: loan from a SE Iranian language of the Pashto *lastúṇay* type); Gershevitch himself says only "perhaps".

**No extraction errors found.** The JSON matches the printed page throughout. One structural nicety for the owner, not an error: on the page, `دستار ، دستگاه` belong to *dast* and `( آستن ، آستیم )` are parenthesised variants of *âstîn*; the JSON flattens both into one `script_extra` string. Both variants are real Borhan-e Qateʿ headwords (BQT vol. 1), so nothing needs correcting unless you want the association preserved.
