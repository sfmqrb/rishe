# Verification process log — verify-page-174


## [2026-09-05T20:49:06.044Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 174 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-174.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-174.json. Write /home/sfmqrb/git/rishe/data/verification/page-174.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 174` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:49:07.690Z] AGENT

I'll start by reading the instructions file.


## [2026-09-05T20:49:08.401Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:49:08.420Z] TOOL RESULT

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


## [2026-09-05T20:49:08.816Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-174.txt"
}
```


### [2026-09-05T20:49:08.839Z] TOOL RESULT

```
1	=== PDF page 174 (book page 144) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ger 2, Greno : to become ripe, grow old  (refs POK:390)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:390 | zar 2 : to grow old ; zarmân : old man ; zarwân, zaurva : old age ; â-zarema-dugedâ : ageless woman ☞Ne 1,Dheugh ; zara-uštra : "with old camels" ☞Wes 1 | NOTE: Some references (BQT:1011) link "zara" to the Indo-European root "Ghel:yellow", thus "zara-uštra" means (with) yellow camels.
5	  #2 (parent #1) [Persian] refs=HRN:143; POK:390; BQT:36,1015,1017 | zar 2 «زر ۲» : old ; zâl «زال» : old ; zâr 1 «زار ۱» : ill, weak ; zarvân «زروان» : time ; Âzarmîdoxt «آزرمیدخت» : "ageless woman" ; Zartošt «زرتشت ، زردشت» : Zoroaster | extra: زرمان
6	#3 (parent #0) [Pahlavi] refs=MON:199 | arzan : millet
7	  #4 (parent #3) [Persian] refs=IEC:406 | arzan «ارزن» : millet | extra: ارژن
8	#5 (parent #0) [Persian] refs=IEC:406 | zîreh «زیره» : caraway seed | extra: زیره با
9	#6 (parent #0) [Sanskrit] refs=IEC:406 | jîrna : caraway seed
10	#7 (parent #0) [Latin] refs=AHD | granum : grain
11	  #8 (parent #7) [Italian] refs=None | granito : grained, grained rock
12	    #9 (parent #8) [French] refs=KLN:674 | granite
13	      #10 (parent #9) [Persian] refs=MON:3223 | gerânît «گرانیت» : hard rock
14	      #11 (parent #9) [English] refs=KLN:674 | granite
15	  #12 (parent #7) [English] refs=AHD | grain, granule, gravy, pomegranate
16	#13 (parent #0) [Middle German] refs=AHD | karl : (grown and mature) man
17	  #14 (parent #13) [French / English] refs=None | 
18	    #15 (parent #14) [Persian] refs=MON |  | extra: کارل، شارل، چارلی، کارولینا، کارلوس
19	  #16 (parent #13) [English] refs=None | Carl, Karl, Carolina, Charles
20	#17 (parent #0) [Germanic] refs=AHD | karnam : grain
21	  #18 (parent #17) [English] refs=None | corn
22	
```


## [2026-09-05T20:49:12.129Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-174.json",
 "description": "Read source JSON for page 174"
}
```


### [2026-09-05T20:49:12.163Z] TOOL RESULT

```
{
  "pdf_page": 174,
  "book_page": 144,
  "entries": [
    {
      "root": {
        "name": "Ger 2, Greno",
        "lang": "Indo-European",
        "refs": "POK:390",
        "gloss": "to become ripe, grow old"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:390",
          "words": [
            {"translit": "zar 2", "gloss": "to grow old", "script": null},
            {"translit": "zarmân", "gloss": "old man", "script": null},
            {"translit": "zarwân, zaurva", "gloss": "old age", "script": null},
            {"translit": "â-zarema-dugedâ", "gloss": "ageless woman", "script": null, "see": ["Ne 1", "Dheugh"]},
            {"translit": "zara-uštra", "gloss": "\"with old camels\"", "script": null, "see": ["Wes 1"]}
          ],
          "note": "Some references (BQT:1011) link \"zara\" to the Indo-European root \"Ghel:yellow\", thus \"zara-uštra\" means (with) yellow camels.",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:143; POK:390; BQT:36,1015,1017",
          "words": [
            {"translit": "zar 2", "gloss": "old", "script": "زر ۲"},
            {"translit": "zâl", "gloss": "old", "script": "زال"},
            {"translit": "zâr 1", "gloss": "ill, weak", "script": "زار ۱"},
            {"translit": "zarvân", "gloss": "time", "script": "زروان"},
            {"translit": "Âzarmîdoxt", "gloss": "\"ageless woman\"", "script": "آزرمیدخت"},
            {"translit": "Zartošt", "gloss": "Zoroaster", "script": "زرتشت ، زردشت"}
          ],
          "script_extra": "زرمان",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "MON:199",
          "words": [
            {"translit": "arzan", "gloss": "millet", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "IEC:406",
          "words": [
            {"translit": "arzan", "gloss": "millet", "script": "ارزن"}
          ],
          "script_extra": "ارژن",
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:406",
          "words": [
            {"translit": "zîreh", "gloss": "caraway seed", "script": "زیره"}
          ],
          "script_extra": "زیره با",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:406",
          "words": [
            {"translit": "jîrna", "gloss": "caraway seed", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "granum", "gloss": "grain", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Italian",
          "refs": null,
          "words": [
            {"translit": "granito", "gloss": "grained, grained rock", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "French",
          "refs": "KLN:674",
          "words": [
            {"translit": "granite", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "MON:3223",
          "words": [
            {"translit": "gerânît", "gloss": "hard rock", "script": "گرانیت"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 9,
          "lang": "English",
          "refs": "KLN:674",
          "words": [
            {"translit": "granite", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 7,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "grain, granule, gravy, pomegranate", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Middle German",
          "refs": "AHD",
          "words": [
            {"translit": "karl", "gloss": "(grown and mature) man", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "French / English",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Persian",
          "refs": "MON",
          "words": [],
          "script_extra": "کارل، شارل، چارلی، کارولینا، کارلوس",
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 13,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "Carl, Karl, Carolina, Charles", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "karnam", "gloss": "grain", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "corn", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:49:12.707Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:49:12.738Z] TOOL RESULT

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


## [2026-09-05T20:49:27.455Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','BQT','MON','IEC','AHD','KLN','WLD','BRT','PHD','NYB','SYN','ARY','HUB','LEW','LAT','SKT']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-05T20:49:29.255Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
```


## [2026-09-05T20:49:34.147Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_01 leaf 398 (p.390) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==399' POK_01.txt | head -80"
}
```


### [2026-09-05T20:49:35.855Z] TOOL RESULT

```
=== POK_01 leaf 398 (p.390) ===
```


## [2026-09-05T20:49:36.043Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD gerə ===\"; grep -n -i -E \"^\\s*(g|ǵ)er[əe]-|zarathustra|karlaz|\\bkarl\\b\" AHD_watkins1985.txt | head -40\necho \"=== AHD grə-no ===\"; grep -n -i \"granum\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T20:49:36.117Z] TOOL RESULT

```
=== AHD gerə ===
585:[karlaz. Man. Germanic root. 1. Old English ceor/, man, churl: CHURL. 2. Old Norse karl, man, freeman: CARL, CARLING. [In Pok. ger- 390.]]
1334:CANDENT kand- CANDID kand- CANDIDA kand- CANDIDATE kand- CANDLE kand- CANDOR kand- CANESCENT kas- CANICULA kwon- CANINE kwon- CANKER kar-1 CANNABIS kannabis CANOROUS_ kan- CANT? kan- CANTABILE kan- CANTEEN kanto- CANTICLE kan- CANTILLATE kan- CANTO kan- CANTON kanto- CANTOR kan- CANVAS kannabis CANZONE kan- CAPABLE kap- CAPACIOUS kap- CAPE2 kaput CAPELLA kapro- CAPIAS kap- CAPITAL! kaput CAPITAL? kaput CAPITATE kaput CAPITATION kaput CAPITELLUM kaput CAPITULATE kaput CAPITULUM kaput CAPO! kaput CAPON skep- CAPRIC ACID kapro- CAPRICE kaput CAPRICORN kapro-, ker-1 CAPRIFIG kapro- CAPRIOLE kapro- CAPROIC ACID kapro- CAPSICUM kap- CAPSID kap- CAPSTAN kap- CAPSULE kap- CAPTAIN kaput CAPTION kap- CAPTIOUS kap- CAPTIVATE kap- CAPTIVE kap- CAPTOR kap- CAPTURE kap- CAR kers-2 CARAMEL kolem- CARAT ker-1 CARAVANSARY tere-2 CARBON ker-4 CARBUNCLE ker-4 CARCINO-  kar-1 CARCINOGEN kar-1 CARCINOMA kar-1 CARD? kars- CARDIA kerd-1 CARDIAC kerd-1 CARDIO- kerd-1 CARDOON kars- CARE gar- CAREEN kar-1 CAREER kers-2 CARESS ka- CARET kes-2 CARGO kers-2 CARICATURE kers-2 CARIES ker-5 CARILLON kWetwer- CARINA kar-1 CARIOLE kers-2 CARL karlaz CARLING karlaz CARMINATIVE kars- CARNAGE sker-1 CARNAL sker-1 CARNASSIAL_ sker-1 CARNATION sker-1 CARNET kWetwer- CARNIVAL legh-, sker-1 CARNIVOROUS = sker-1 CAROCHE kers-2 CAROL aulo- CAROTID ker-1 CAROUSE ud- CARP! ger-2 “CARP kerp- CARPAL kwerp- CARPEL kerp- CARPENTER kers-2 CARPET kerp- CARPO- kerp-
1357:CHOLE- ghel-2 CHOLER ghel-2 CHOLERA ghel-2 CHOLESTEROL ster-1 CHOLINERGIC werg- CHOLLA g(e)u-lo- CHONDRO- ghrendh- CHONDROMALACIA mel-1 CHOOSE geus- CHORAGUS_§ ag-, gher-1 CHORAL gher-1 CHORALE gher-1 CHORD? ghere- -CHORE ghé- CHORIC gher-1 CHORION ghere- CHORISTER gher-! CHOROGRAPHY ghé- CHORUS gher-1 CHOWDER kele-1 CHRESARD gher-5 CHRESTOMATHY gher-5, mendh-1 CHRISM ghréi- Curist ghréi- CHRISTEN ghréi- CHRISTIAN ghréi- CuRIsTMas ghréi- CHROMA ghréu- CHROMATIC ghréu- CHROMATO- ghréu- -CHROME ghréu- CHROMIUM ghréu- CHROMO- ghréu- CHROMONEMA (s)né- CHRONAXY ag- CHRYSANTHEMUM § andh- CHTHONIC dhghem- CHUFA swei-! CHUKAR kau-! CHUKKER kwel-1 CHURCH keue-? CHURL karlaz CHUTE kad-
=== AHD grə-no ===
```


## [2026-09-05T20:49:41.054Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"$f: $(wc -c <$f) bytes, $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f) leaves\"; done\necho \"--- grep zaurva in POK ---\"\ngrep -n \"zaurva\\|zarma\\|azarəm\\|zarǝ\" POK_full.txt | head -20"
}
```


### [2026-09-05T20:49:42.744Z] TOOL RESULT

```
POK_01.txt: 981836 bytes, 363 leaves
POK_02.txt: 1137861 bytes, 433 leaves
POK_03.txt: 1170809 bytes, 429 leaves
POK_full.txt: 3971883 bytes, 1 leaves
--- grep zaurva in POK ---
35628:(: gr. Ypau(;? Old Norse kgr, see below) zaurvan-xx\. " hoariness, old age, grayness, 
35647:one YpaO(;); perhaps in relationship to Avestan zaurvan-m. ' hoariness, old age, grayness
```


## [2026-09-05T20:49:46.732Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_02 leaf 46/47 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==46 || NR==47' POK_02.txt | head -100"
}
```


## [2026-09-05T20:49:47.275Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '35590,35680p' POK_full.txt"
}
```


### [2026-09-05T20:49:48.313Z] TOOL RESULT

```
=== POK_02 leaf 46/47 ===
(über  ahd.  krüsel  , Schmelztiegel'  usw.  s.  Falk-Torp  unter  krus  m.  Nachtrag) zur  Erwägung  steht.  Über   nhd.  Kriechbaum  s.  Kluge  ^^  unter  Krieche.
2.  Labialerweiterungen:
greu-p-:  gr.  ygvTtög  ,gekrümmt,  mit  einer  Adlernase',  ygVTtöa)  ,krümme', ygvyjj  ygVjtög  m.  , Greif  (nach  dem  krummen  Schnabel  und  den  krummen Fängen'),  nasaliert  ygvfxrtdvsLv'  ygvTtova&aL,  0vyy.d^7tT6Lv  Hes.,  wozu  wohl zunächst  ags.  usw.  krumh  , krumm'  (s.  oben  S.  387).
greu-b-:  hierher  vielleicht  schott.-gäl.  groban  ,top  or  point  of  a  hill' (*grubb-) ;
anord.  krjüpa,  ags.  creopan,  mnd.  krüpen  , kriechen'  (,*sich  krümmen wie  ein  Wurm'),  ags.  cryppan  , beugen,  biegen',  nhd.  mdartl.  sich  krüpfen ,sich  krümmen'  (schweiz.  chrüpfen  , etwas  so  biegen,  daß  es  eine  rundliche Vertiefung  bekommt'),  mnd.  kroppen  , krummbiegen',  norw.  kreypa  (*kraup- jan)  ,krümmen' ;  anord.  kryppa  f.  , Buckel',  kryppil,  ags.  crypel  , Krüppel*, mnd.  kr'öpel  ds.  (holl.  kreupel]  mhd.  hnlp{jp)el,  nhd.  Krüppel  aus  dem Ndd.),  hochstufig  ags.  creopel  , Krüppel' ;  ags.  cropp  ,Büschel  von  Beeren oder  Blumen,  Ähre,  Kropf;  mit  expressiver  Verschärfung:  ahd.  kröpf ,Kropf,  Vogelkopf',  mnd.  krop  ,Beule,  Auswuchs,  Kropf,  Vogelkopf;  Rumpf, (toter)  Körper',  nur  in  letzterer  Bed.  anord.  kroppr  ,Rumpf';  mit  einfachem b:  anord.  krof  n.  , Rumpf,  geschlachteter  Tierkörper',  kryfia  ,ausweiden'; ein  ^krufta-  , Ausbiegung,  Hügel'  in  mndl.  krocht  , Hügel,  Acker  in  den Dünen',  ags.  croft  , kleines  Feld' ;
lit.  wahrscheinlich  grubineti  , straucheln,  stolpern',  grixb{l)as  m.  , rauhe Unebenheit,  Erdhügel'.
390
#
3.  s-Er Weiterung  greu-s-:  mlid.  mnd.  krüs  ,kraus,  lockig';  q^^^^ krüse  ,Gekröse,  Bauchfett^  (,*das  Krause');  mit  germ.  -au-  ndd.  krös  ;^ geweide  von  GänsenS  mhd.  (ge)krcese,  nhd.  Gekröse,  ndd.  kriise  (""krUsä ,Runzel,  Falte,  Furche,  Locke',  hoU.  kreus  ,Falz  in  Faßdauben* ;  ags.  cr^^ 'zierlich',  wfries.  kreas  .aufgeputzt';  ahd.  mhd.  krol  (-11-)  ,kraus'  (*krudd:)^ mhd.  krol(le),  krillle  ,LockeS  norw.  krull  ds.;  norw.  mdartl.  kruskn] krusken  ,hinfällig',  ndd.  krusch  ,crispus',  mhd.  h-üsp  ,kraus',  nhd.  obd. kraust  , kraus'.  ^
WF.  I  593  ff.,  WH.  623,    Trautmann  94  f.,  97,  99  f.
^.  ger-,  grei-  , wachsen,  wecken'.
Ai.  jdrate  ,erwacht',  jä-gar-ti  ,wacht',  Perf.  jä-gdra,  Partiz.  jä-gr-vdihs- munter,  eifrig',  jdgrvi-  ,aufmerksam,  wach,  munter',  av.  jayärayant^m ,den  wachenden',  Perf.  jagära,  Partiz.  Perf.  Akt.  jagäicrvah-,  jigäurvah ,wach,  wachsam',  Kaus.  ä-garayeiti  ,weckt',  mit  /ra-inchoativ  fra-yrisdmnö ,erwachend'  (*grl-sk-),  Kaus.  fra-yrä-yräyeiti,  dissimil.  fra-yrä-rayeiti  ,er.„ weckt',  mpers.  vigräs  , erwache',  vigräsenäg  ,Erwecker' ;  I
gr.  iysiQOj  , wecke'  (oh  i-  das  Adv.  *e?  vgl.  e  oder  ö  in  av.  ä-ga
rayeitl und  oben  S.  280 ;  anders  Schwyzer  Gr.  Gr.  1  648  ^)j  Aor.  eygsTo,  syQea^ai^ Perf.  i-ygrj-yoQa  (für  s-yrj-yoga  —  vgl.  ai.  jä-gdra  —  mit  dem  g  von " iygiad-ai]  Med.  (spät)  i-yrj-ysQ-fxac ]  vom  Perf.  gingen  aus  iyorjyoQxl  ,im Wachen',  iyQrjyoQaig) ;  iyQrjaao)  ^wache'  zu  ^ygr^-r-  (vgl.  av.  fra-^rätö  ,beim Erwachen');  kaum  aus  *iyQr]omcx)  (Schwyzer  Gr.  Gr.  I  708 2);
alb.    tosk.    ngre    (woraus   ngre),    geg.    ngrei   ,hebe   auf,    errichte,  wecke, spanne  ein  Gewehr'  (*n-grd-n-iö),  Partiz.  n-grite  {^-grl-t-)\
vermutlich  anord.   karskr,   kerskr  , frisch,   lebhaft',   mnd.  karsch    , frisch, munter',  alem.  chärzsch.
WP.  I  598  f.,  WH.  I  429  f.  .
ger-,  gero-,  gre-  ,morsch,  reif  werden,  altern',  auch,  bes.  in  Bildungen  mit Formans  -rzo-,  ,Korn,  Kern'  (nur  NW-Idg.) ;   die  älteste  Bed.  scheint , reiben'    (daher    ,Reibefrucht,   klein   Zerriebenes')    gewesen    zu    sein, intr.-pass.  , aufgerieben  werden,  von  Alter  oder  Krankheit';  nominal: ger-ont-  ,alt;  Greis',  ger-ger-o-s  ,hinfällig',  gr-no-m  ,Reibefrucht, Korn'. Ai'.  jdrant-   ,gebrechlich,    alt,    Greis'   (=  osset.  zärond  ,alt',  gr.  ysgcjv] vgl.   auch   npers.    zar   , Greis,    Greisin'),  jdrati    ,macht   gebrechlich,   läßt altern'   (,*reibt  auf),  jarand-    ,hinfällig,   alt',  jards-   f.   (Nom.    Sg.  jardh, idg.  -ös)  und  jarä  , Altwerden,  Alter' ;  redupl.  jarjara-  , zerbrechlich,   hin- fällig' (:gr.  ysQyeQtfiog) ;  dehnstufig  Jö?'a- , alternd'  (=  npers.  zär  , schwach, elend',  zär  , Greis,  Greisin';  auch  im  Aor.  järisuli)]   schwere   Basis   in  ai. jarimdn-  m.  ,hohes  Alter,  Altersschwäche',  jiryatij  jiiryati  ,wird  gebrechlich.
391
morsch,  altert',  Partiz.  jürnd-^  jlimd-  ,geb rechlich,  abgelebt,  abgenutzt, zerfallen,  morsch,  alt' ;  av.  azardsant-  ,nicht  alternd'  (Partiz.  des  s-Aor.), azardma-  ,nicht  abnehmend'  (von  *zardma-  m.  ,das  Verkommen'),  zairina- , aufreibend,  erschlaffend',  zardta-  ,altersschwach'  (wohl  =^  ai.  "^jirta-)^  mit formantischem  u  (:  gr.  yQav(;?  anord.  kor,  s.  u.)  zaurvan-  m.  , Greisenalter, Altersschwäche',  zaurura-  , altersschwach,  gebrechlich',  vielleicht  auch zrvan- :  zrnn-  ,Zeit'  ;
arm.  cer  ,alt,  Greis'  (*§e7'o-) ;
gr.  ysQCüv  , Greis'  {yiqovT-),  ysgovoLog  ,den  Geronten  zukommend',  yeQOv- oia  , Ratsversammlung  (der  Ältesten)^,  yiqag  n.  (idg.  *gerd-s,  von  der schweren  Basis)  ursprüngl.  ,*  Alter,  *  Altersvorrecht',  daher  , Ehrengabe, Ehrenstellung,  Belohnung',  yegagög  , ehrwürdig,  stattlich,  ansehnlich',  später auch  ,alt,  greisenhaft'^  ysgaiög  ,alt'  wohl  aus  *y€Qa(T-t6g',  in  der  Bed. jAlter'  ist  yegag  ersetzt  durch  y^gag]  das  r]  von  yrjgdayco)  ^altere'^,  Partiz. Präs.  yrjgdg  .alternd^,  themat.  Impf,  eyrigä,  usw.  auf  yrjgag  (für  yegag)  über- tragen, ebenso  auf  yiqgau)  ,altere,  rei
```


### [2026-09-05T20:49:48.365Z] TOOL RESULT

```
cymr. gyrrxw. " drive, impel, drift, propel, push, thrust, livestock drive ' {*gersjo-), 
therefrom gyrruds.7; 

Old Norse kjarrn., kjgrrm. {*kerza-, kerzu-) "shrubbery, bush ', Swedish dial, kars, karse 
m. 'basket from withe, small bag, net bag ', Old Norse kassf/Jm. {*kars-) ' wicker basket, 
back basket ', Swedish karsat "creel, net bag ', Norwegian A/iessa "basket, bast netting ' 
{*kars/dn). 

In addition probably Middle High German kerren^ turn ' {*karzjan) = Old English cierran 
"wend, in a certain position bring, intr. turn ', becierran^iuru', cierrm. {*karzi-) "time, one 
time, business '. 

References: WP. I 609 f., WH. I 594, 596, Loth RC 40, 375 f. 
Page(s): 392-393 

Root / lemma: ger-, gera-, gre- 
Meaning: to rub; to be old; grain 

Note: also, esp. in formations with formants -no-, "corn, grain, seed ' (only NW-lndo 
Germanic); the oldest meaning seems to have been "rub' (hence " fruit grater, neatly 
pulverized, ground into fine particles; crushed '), intr.-pass. " become faded, from age or 
disease, malady'. 

Material: Old \x\6\c jarant-^ fragile, easily broken; unstable, dilapidated, old, graybeard' (= 
osset. zarond^o\(i\ gr. yspojv; compare also npers. zar^ graybeard, hag '),ya/'a//" makes 
fragile, easily broken; unstable, dilapidated, allows to grow old ' ("*rub, chafe '), jarana-^ 
frail, o\(i\jaras-i. (Nom. Sq. jarah, Indo Germanic -os) and Jam ^ age, grow older, 
senescence, aging process, process of growing older, age'; redupl. jarjara- "frail, 
breakable, decrepit ' (: gr. Y£pY£pi|jO(;); lengthened grade yara- " aging, maturing; growing 
older ' (= npers. za/'"weak, woeful, wretched, miserable ', zar^ graybeard, hag '; also in 
Aor. jarisuh); heavy basis in Old \n6\c Jar/man- m. " old age, senility ', jTryati, juryatT 
become fragile, easily broken; unstable, dilapidated, rotten, decayed, decomposed; brittle, 
grows old ', participle yi7/77a-, y7/77a- " fragile, easily broken; unstable, dilapidated, decrepit, 
antiquated, worn out, old, decompose, rotten, decayed, decomposed; brittle, old'; Avestan 
azarssant-^ noi aging, maturing ' (participle of s-Aor.), azarsma-'not decreasing, 
lessening, diminishing, declining ' (from *zarama-rr\. "the abandoned, depraved, unkempt, 
withered, shabby, dilapidated, neglected '), zairina-^ attritional, tiring, languishing, 
wearying, exhausting ', z5/'a/a-"altersschwach' (probably = Old Indie *jTrta-), with formant u 
(: gr. Ypau(;? Old Norse kgr, see below) zaurvan-xx\. " hoariness, old age, grayness, 



senility ', zaurura- " decrepit, infirm, feeble, weak, frail, aged, fragile, easily broken; 
unstable, dilapidated ', perhaps also zrvan- .■z/'J/7-'time'; 

Armenian ce^'old, graybeard' {*gero-)\ 

gr. Yspwv " graybeard' (yspovT-), yspouaioc; " pertaining to the council of the elders, 
senatorial ', yspouaia ' Council of Elders, senate, esp. at Sparta, sacred college ', yspac; n. 
(Indo Germanic *ger9-s, from the heavy basis) originally "*age, * age prerogative ', hence " 
honorific title; award, prize, honorary position, guerdon, reward, recompense, prize, trophy 
', yspapoc; ' venerable, stately, respectable ', later also 'old, senile ', yspaioc; 'old' probably 
from *Y£paa-i6c;; in the meaning 'age' is Y£pa(; replaced through ynpac;; n from ynpaaKCjo ' 
grown old ', participle present ynpcic; ' aging, maturing; growing older ', themat. Impf. 
EVnpa, etc. auf ynpac; (for yspac;) figurative, also in ynpau) ' get old, grow old, mature, ripen 
', YHpaAsoc; (by Hes. also yspaAsoc;) 'old'; Attic ypauc;. Gen. Ypa(*F)6c; (hom. Dat. YpnO 'old 
wife, woman' (hom. ypnu*; probably later inscription of a right one *Ypr|(F)i(; after the usual 
one YpaO(;); perhaps in relationship to Avestan zaurvan-m. ' hoariness, old age, grayness 
', perhaps originally Nom. *ger-us .Gen. *ger9-u-6s, from which ypaFoc;; s. Schwyzer Gr. 
Gr. I, 574; redupl. yspyspifjoc; ' dropping by itself or ripe fig or olive ' (see above); 

Old Norse A^A/'man, husband, old man, husband, husband, free man, husband' = Old 
High German karal6s., with ablaut Old English ceorr free man of the lowest class, 
husband ', engl. churr rude person, person from the country, fool ', Middle Low German 
ker/elree, common man, husband, sturdy man, husband'. Modern High German (from 
Ndd.) Ker/^, basic meaning probably ' aged man, husband'; 

Old Church Slavic zi./"©// "ripen', ztre/b ' mature, ripe, mellow, seasoned ', causative 
Sbzori^ ripe '. 

In the meaning ' corn, grain, seed ': 

Latin granum^corn, grain, seed ' {*gr-ndm, = Old \n6\cj7rna-, see above) = Old Irish 
gran, cymr. etc. grawn {Sg. gronyn) ds. (borrowing from Latin is not provable) = Lithuanian 
zirnis, Latvian zirnisxw. 'pea'. Old Prussian syrnei. 'corn, grain'; Old Church Slavic zrtno, 
Serb, zfnou. 'corn, grain'; Gothic kaurn. Old High German Old English Old Norse korn. 
Modern High German Korn, Old English cyrner seed ', next to which zero grades Old 
High German kerno. Old Norse kjarnixw., ds. (probably also Modern High German 
Dialectal /re/77' milk cream, milk skimmings ' granular becoming as in butter. Middle High 
German /re/77' churn, vessel in which butter is made ', Old Norse kjarni, kirna6s.. Old 
English ciern, engl. churn 6s.). 



Maybe alb. {*kjern) thjerre^ lentil ' not from Armenian sisern' chickpea ' 

*graros {*gr-r6s) " pulverized, ground into fine particles; crushed ' is continual probably in 
Latin glarea {* grareja) ' gravel '; o'-present 'ig/'d-o'd perhaps in Gothic ^5/r/io/d/7 ' crunch '. 

References: WP. I 599 f., WH. I 605 f., 618 f., Trautmann 371 f., Schwyzer Gr. Gr. I 514, 
574, 682 under Anm. 5.
```


## [2026-09-05T20:50:06.260Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD ger?- entries ===\"; grep -n -E \"^\\[?(ger|gera|gra-no|grəno|grano)\" AHD_watkins1985.txt | head -30\necho \"=== AHD grain/corn/kernel ===\"; grep -n -E \"GRAIN|GRANULE|GRAVY|POMEGRANATE|\\bCORN\\b\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T20:50:06.332Z] TOOL RESULT

```
=== AHD ger?- entries ===
491:ger-?
493:gerbh-
=== AHD grain/corn/kernel ===
163:The Indo-Europeans practiced agriculture and the cultivation of cereals. We have sev- eral terms of Indo-European antiquity for grain: gre-no- (CORN), yewo-, and pdro-, which may have designated wheat or spelt. Others of more restricted distribution are wrughyo-, “rye,” and bhares-, “barley.” Two roots for grinding are attested, al-* and mele- (MEAL?, MILL). The latter is confined to the European branches of the family. Another European term is sé-', “to sow,” not found in Greek, Armenian, or Indo-Iranian. The verb “to plow” is are-, again a common European term, with the name of the plow, *ara-trom.
535:gre-no-. Grain. 1. Germanic *kornam in: a. Old English corn, grain: CORN}; b. Old English derivative noun cyr- nel, seed, pip: KERNEL; c. Old High German korn, grain: EINKORN. 2. Latin grdnum, grain: GARNER, GRAIN, GRAM2, GRANADILLA, GRANARY, GRANGE, GRANITE, GRANULE, GRENADE; FILIGREE. [In Pok. ger- 390.]
618:ker-1. Horn, head; with derivatives referring to horned animals, horn-shaped objects, and projecting parts. I. Zero-grade form *kr-. 1. Suffixed form *kr-n- in: a. Ger- manic *Aurnaz in (i) Old English horn, horn: HORN, (HORNBEAM) (ii) German Horn, horn: ALPENHORN, ALT- HORN, FLUGELHORN, HORNBLENDE; Db. Latin cornd, horn: CORN2, CORNEA, CORNEOUS, CORNER, CORNET, CORNICULATE, CORNU; BICORN, CADUCICORN, CAPRI- CORN, CLAVICORN, CORNIFICATION, LAMELLICORN, LON- GICORN, TRICORN, UNICORN. 2. Suffixed and extended form *krs-n- in Germanic *hurznuta in Old English hyrnet, hornet: HORNET. 3. Suffixed form *kr-ei- in: a. Germanic *hraina- in Old Norse hreinn, reindeer: REINDEER; b. Germanic *hrinda- in Old High German hrind, ox (> German Rinder, cattle): RINDERPEST. 4. Suffixed extended form *kros-no- in Greek kranion, skull, upper part of the head: CRANIUM; MIGRAINE, OLECRANON. 5. Suffixed form *kr-a- in: a. Greek karé, kara, head: CHARIVARI; CHEER; b. Greek karoun, to stupefy, be stupefied (< “to feel heavy-headed”): ca- ROTID; c. Greek kardton, carrot (from its hornlike shape): CARROT. 6. Possibly extended form *kri- in Greek krios, ram: CRIOSPHINX. II. Suffixed form *ker-wo-. 1. Latin cervus, deer: CERVINE, SERVAL. 2. Latin cervix, neck: CERVIX. III. Extended and suffixed form *keru-do- in Germanic *herutaz in: a. Old English heorot, hart, stag: HART; b. Dutch hart, deer, hart: HARTEBEEST. IV. Extended form *keras-. 1. Greek keras, horn: CARAT, CERASTES, KERATO-; CERATODUS, (CERATOID), CHELIC- ERA, CLADOCERAN, KERATIN, RHINOCEROS, TRICERA- Tops. 2. Persian sar, head: SIRDAR. 3. Suffixed form *keras-ro- in Latin cerebrum, brain: CEREBELLUM, CERE- BRUM, SAVELOY. V. Extended o-grade form *koru-. 1. Greek Rorumbos, uppermost point (< “head”): CoR- yMB. 2. Greek koruphé, head: CORYPHAEUS. 3. Suffixed form *koru-do- in Greek korudos, crested lark: coRY- DALIS. 4. Suffixed form *koru-ndé in Greek koruné, club, mace: CORYNEBACTERIUM. [Pok. 1. ker- 574.]
1394:CONVOLVE wel-3 CONVULSE wel-4 cook pekw- cOoKY kak-2 cooL gel-3 COOPER ku- COOPERATE op-1 CO-OPT op-2 COORDINATION ar- COPE! kel-1 COPEPOD kap- COPIOUS op-1 COPRO- kekw- COPULA ap-! COPULATE ap-1 COPY op-1 CORACIIFORM ker-2, merph- CORACOID ker-2 CORBEL ker-2 CORBINA ker-2 CORD ghere- CORDATE kerd-1 CORDIAL kerd-1 CORDIFORM kerd-1 CORDON ghere- COREOPSIS sker-! CORGI kwon- CORIACEOUS sker-1 CORIUM §sker-1 cOoRM sker-! CORMORANT ker-2 CORN! gre-no- CORN2 ker-1 CORNEA ker-1 CORNEL ker-6 CORNEOUS ker-1 CORNER ker-1 CORNET ker-1 CORNICULATE ker-1 CORNIFICATION ker-1 CORNU_ ker-1 CORNUCOPIA op-! CORONA sker-3 CORONOID  sker-3 CORPORAL! kWrep- CORPORAL’ kWrep- CORPORATE kWrep- CORPOREAL kWrep- CORPOSANT kWrep-, sak- CORPS kWrep- CORPSE kWrep- CORPULENCE kWrep- CORPUS krep- CORPUSCLE kWrep- CORRADE réd- CORRECT reg-! CORRIDOR kers-2 CORRIE kWer-2 CORROBORATE reudh-! CORRODE réd- CORRUGATE ruk-2 CORRUPT reup- CORSAGE kWrep- CORSAIR kers-2 CORSE kWrep- CORSET kWrep- CORTEGE gher-1 CORTEX sker-1 CORUSCATE sker-2 CORVEE reg-! CORVINE ker-2 Corvus ker-2 CORYDALIS_ ker-1 CORYMB_ ker-1 CORYNEBACTERIUM bak-, ker-1 CORYPHAEUS_ ker-1 COSMONAUT nau-2 COSMOPOLITE pele-3 cosmos kes-3 cost sta-
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1869:MICROPYLE pulé MICTURATE meigh- MID! medhyo- MIDDLE medhyo- MipcaRD medhyo- MIDGE mu-2 MIDRIFF krep- MIDWIFE me-2 MIGHT! magh-! MIGRAINE ker-1 MIGRATE mei-1 MIL! gheslo-
```


## [2026-09-05T20:50:07.289Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC leaf 218 (p.406) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==218 || NR==219' IEC.txt | head -60"
}
```


### [2026-09-05T20:50:08.993Z] TOOL RESULT

```
=== IEC leaf 218 (p.406) ===
se ap- pear to be fr. Gk. (via Lat.?), cf. Gk. krossós “bucket, pitcher’, LLat. *crossa > OFr cruise) (Variant: gurü£h-) Arm. krcem ‘gnaw’; krčem (iotacised form: *enash)); Ir. brüghaim, brüighim ‘pound, crush’; OCS gryzgo, grysti ‘gnaw’; gryZa ‘gripes’ (and com. Sl.); Li. gružinti ‘gnaw, nibble’ be- side grugzdu, -eti and grukšiu, ep ‘crunch’; grūžtis, f. ‘gnawing pain, gripes’; o-gde in grau- Ziu, ti ‘gnaw’. Variant (*gurügho) in Gk. brū- khō ‘gnash’ and in Go. krusts, m. ‘gnashing of teeth’ beside kriustan ‘gnash’
gurü£os, å ‘neck, throat; pitcher w. narrow neck, pot'. Cf. gurðu-, gur- (1) Arm. kurck, pl. type: ‘chest; throat’; OS krūka, wf. ‘pot, pitcher’; OE crūce beside crocca, id.; MHG krūche, id.; G Krauche beside (LG type in) Kruke, id.; Du. kruik, Fris. krük; LG Krūk, wf. (Variant of type *gurugh- in Gk. brúx, acc. sg. brükha “depth of sea")
gurus, see gurus and following entries
gurütos (1) “heavy, big'. WP I, 685 Skt. gurut-amah ‘heaviest’; Tokh. B wrotse, orotse ‘big’; OLat. brütus “heavy”; Class. Lat. ‘clumsy, boorish’; MHG krude, sf. *oppres- sion, force, violence, cruelty’; Latv. grūts ‘heavy’
gurütos (2) ‘teeming, thriving’. Same as (1)? WP I, 685 Gk. brütos, on ‘fermer ted liquor’; brútea, npl. ‘lees’; cf. brüsis, f. (^welling-up'. Vbl. n. to next); W brid, pl. iau, m. ‘eruption; scab’ (?), but cf. bhrütos (1) & (2). (Isophonic: MHG krüt ‘herb’, qua *gurütóm)
guruuó ‘teem, be full’. Cf. gurütos (2) Gk. brúð; Lat. (?) con-, in-gruo, but cf. gruuo
gur- (1) ‘devouring; gulp; throat. WP I, 683 Skt. cf. gilami, gire, grnàmi ‘devour’; Av. gar-, xwar-, id. beside garð ‘throat’: Skt. galah, id. and -garáh *-vorous'; Tokh. B kor ‘throat’; Oss. gwr, id. and ‘abyss’; Arm. kur 'eatables' beside
373
orkor, o-st. (throat, fr. *guoreus; Gk. br-, -bros in br-ágkhos, br-ógkhos, -okhthos, br- ókhos, br-ókhó, -ükho, molo-brós, etc.; Alb. cf. gur-mac, -maz ‘throat’; Lat. voro, are; OCS Zro, Zréti ‘devour’; Li. cf. girà small beer, sour milk’; girtas ‘drunk’; girtüs ‘heady’, of wine; Latv. dzira ‘drink’; dzīres ‘feast’
gur- (2) ‘heavy’. See gurus
gur- (3) ‘appellation, song, praise; revere, sacrifice, worship’. Cf. gurdh- (1) and gurtos Skt. giráh, gir ‘praise’; Lat. au-gur, gs -guris, au-guria (here despite WH); Li. giriü, ti ‘praise’; gyrà ‘boasting’
gurbh- (?) ‘thrive’. Evidence ambig. Vedic grbhnámi “welcome, accept, be fruitful; pp. grbhitáh, pp. ‘fruitful’; Li. gurbstü, gurbti ‘thrive’; gurbüs *Iuxuriant?
gurdos, us (form of gurdos, us, q.v.) “slug- gish, stupid, stiff, awkward'. Cf. WP I, 641 & II, 278 and gurndis Per. gül “idiot”; Oss. qal ‘proud’: Dig. $àla (‘stu- pid'. Abaev); Arm. (Iran. LW?) kurt ‘eunuch’; Gk. bradüs ‘sluggish’; LW in Lat. bardus 'slug- gish, stupid; Lat. gurdus “stupid? (in LL: *blunt); W brydd ‘weak’; Pol. gardy ‘finicky’; Blg. grád ‘ugly’; Srb. grd ‘ugly, monstrous, dirty, nasty’; Slovene gfd also: ‘naughty’; Cz. hrd ‘proud’; Lusat. hordy, id.; Pol. cf. also wz- garda ‘contempt’ beside gardzić ‘despise’; Li. gurdùs ‘sluggish, ailing, weak’; Latv. gurds ‘tired, faint’
gurdh- (1). Cf. gur- (3). Cf. WP I, 686 Av. goroóo, adj. ‘howling’; Arm. kardam “call; read out’; Li. girdžiù, girdéti ‘hear’; girdà f. ‘hearing’; Latv. dzirdu, et
 ‘hear’ O-gde in Skt. garha “abuse”
gurdh- (2) 'stir, rouse'. Cf. gurgotio Gk. brásso, aor. ébrasa; Alb. cf. ngrydh (stir up, foment': Gk. embrásso ‘cast up’ ofthe sea)
gurdhlom, gurdhrom, à, ios, iə ‘crop, throat, gorge, gorging animal Skt. grdhrah ‘vulture’; Gk. bárathron ‘gorge, abyss’; OCS grülo, Zrülo, n. ‘throat’; Pol. gard- 1o, Cz. hrdlo, wd R górlo, id. beside Zerló, Zérlo ‘mouth’; Li. gurklys ‘crop, adam's apple; bottleneck’; Latv. cf. padzirkle ‘throat?
gureió, gurið, see gurð (2)
gurgont- variant of gurgot-, q. v.
gur- —gurio
10
20
25
30
35
40
45
374
gurgot- (gurgot-) “neck, throat, gullet’. WP I, 683 Per. gulü; Oss. qür ‘throat’; qürtt ‘gulp’; Arm. cf. kokord, i, av, a-st. ‘throat, gullet; Lat. gur- ges, gs -itis ‘whirlpool, glutton’; OI gorgozza *windpipe, throat' beside gargata, gargozza, id.; Mir bráge, gs brágat, beside bráighe, gs bráighid ‘throat’; Mod. Ir. brágha & brághad, pl. bráighde, id.; W cf. breuant, brefant *wind- pipe; OBr. brouant, id.; Cor. cf. breiansen, bryonsen ‘throat’; Srb. cf. grgocem, grgotati *gargle'. See next
gurgotio (gurgotaio) ‘gurgle, gulp’. Cf. gur- dhio, (2) and following entries Arm. karkacem ‘burble, gurgle’; karka£, i-st. s., id.; LLat. re-gurgito, äre: Srb. grgocem, gr- gotati ‘gurgle, gargle’; grgaca ‘gurgle’; Blg. cf. grăgutiv, adj. ‘stammering’
gurgo, io ‘choke, block? (alternative form of type gurg-, q. V.) Arm. karkem, v.id.; ON kyrkja ‘strangle’ be- side (alleged) kvirkja, id. cf. Icel. korka “ill- health’
gurgho, ið ‘creak, squawk'. Cf. gurks- Gk. brákho ‘creak’; Li. (1-basis) girgu, Eti, id. beside (u-basis) Li. gurgu, eti ‘growl’. (Both bases arise also in Li. girgZdeti and gurgZdeti ‘creak, screech, be hoarse’. See next)
gurgul-, gurgur-, see gurg-, gurgul- (1) & (2) Gk. cf. borbo-rugé (‘rumbling of bowels’, fr. *gurgu-) beside gorgüra, f. (^sewer', fr. *gur- gur-); Slovene grgráti ‘gargle’, ambig. cf. gurg-, as also Alb. gürgull ‘gurgle’ and Lat. gurgulio ‘throat’, a LW in Alb. gérgélac, gérgilac, id. (fr. Slav.?)
guris, os, us, io ‘wooded hilltop, hill, woog’. WP I, 682 Skt. girih, m. ‘mountain’; Av gairis, m. id.; Per. girive ‘steep acclivity’; Tokh. B karāś "wood": Hes. barües ‘trees’; Ir. (?) brab ‘summit’; Slo- vak hora (wood; mountain’, but ‘mountain’ in Cz. & E S1.); OCS gora, Blg. gorà “forest; mountain’; Li. eng (forest: i-basis) beside guras (“hilP: u-basis); Latv. dam ‘wood, thicket'. (The e-gde Gk. form deré, deiré (2) ‘hill, height" is of uncertain origin)
gurió ‘sing, praise’. An ambiguous formula, cf. giró & ghiro
375
Sk. grnámi ‘sing, praise, announce"; gir, giráh ‘song, praise’; G cf. kurren ‘croon’ beside quorren “make mating-call — of woodcock’; Li. giriù, ti ‘praise’; Latv. dzirties, refl. ‘boast’
gurksið (gurksKó, gursKo) “call, cry, appeal". Cf. gur-, gurió Alb. grish “call, shout, invite’; Li. girksēti *squawk, as geese’; Latv. gurkstu, gurkstet (u- basis “creak, screech")
gurndis “heavy, bulky'. WP I, 699. Cf. gurus, gurdos (gurdos) Per. cf. garan ‘heavy; expensive’; Alb. (LW?) i rándé, i rëndë, adj. “heavy”; Lat. grandis ‘big’; Tokh. A. (ambig.) krant, krent “lovely”
gur-nou- (analytical form of) gurnüs, à, gur- uoni, guernus, à, guernouos, etc. (cf. gurus ‘heavy’ and nàus, nous "boat from the shape of the nether stone of the handmill when worn down by an upper stone rolled upon it). Arm. erkan, a-st.; Oss. cf. kwrói, krói (for *gür-?) ‘mill’; Gk. cf. güris Tine flour”; Olr. bráu, Ir. bró; Cor. brow; OW breuan; MHG kürne; OCS Zrüny,
```


## [2026-09-05T20:50:17.593Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /(^|\\n)[[:space:]]*406[[:space:]]*(\\n|$)/{print \"LEAF \" NR}' IEC.txt | head\necho \"--- grep jirn/zire/arzan ---\"\ngrep -n -i \"jirna\\|jīrṇa\\|zireh\\|zīra\\|arzan\\|jiraka\" IEC.txt | head -20"
}
```


### [2026-09-05T20:50:19.342Z] TOOL RESULT

```
LEAF 236
--- grep jirn/zire/arzan ---
5862:Skt. cf. jirnå *caraway-seed' beside jirnah, jūt- nabh ‘decrepit, withered, corny’; Oss. cf. dzárná ‘frumenty’; Per. cf. are ‘caraway seed, ani- seed” beside arzan (?) ‘millet’; Gk. cf. gág- graina, a cpd. like gag-glíon, see gliu-); Alb. grüné, grurë (wheat; pl. in Tosk); Lat. grà- num; Ir. grán ('grain', coll.); MIr. cf. gráne ‘acorn’; W grawn (‘grain’, coll. also ‘berries; roe’); Cor. Br. græn, coll id.; Go. kaúrn; OHG ON Sw. korn; Du. koren; Fris. koarn; OE corn; OCS zrüno and zírno ('grain, berry’, and com. S1.); Srb. zrno; Pol. ziarno; R zernó all i-basis; Li. Zirnis, gs -io, m. ‘pea’; Latv. zirnis, id. Cf. also Lat. granea, coll.: MHG kürne, sn. (Note: Ger. ‘rye’; Sw. & Fris. ‘barley’; Eng. ‘wheat’; Scots ‘oats’; Du. ‘wheat’; U.S. ‘maize’ when ‘corn’ is used in a specific sense)
```


## [2026-09-05T20:50:22.438Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5845,5875p' IEC.txt\necho \"=== which leaf ===\"\nawk 'BEGIN{RS=\"\\f\"} /jirnå/{print \"LEAF \" NR}' IEC.txt"
}
```


### [2026-09-05T20:50:24.224Z] TOOL RESULT

```
gor- (1) ‘ripe, old, mature’. Cf. ger-, gordos, $aros . Arm. (?) car, o-st. ‘tree’; OCS cf. sü-zorí ‘ripe’; OCz. s-zoliti, v. ‘ripen’, tr; Li. Záras “dry twig’; pl. ‘stubble’; (Latv. zars “branch, twig’? to ĝaros, q.v. Li. is ambig. also)
g0r- (2) ‘gleam, glow’. Cf. gér- (1) Cz. zora, zote ‘dawn’; Pol. zorza, id.; Li. Zarà *gleam, glow’; Cz. cf. (long-gde) záře, OCS zar- ja ‘radiance’
$or- (3), £oros ‘hollow, basin, depression, valley' Arm. cf. cor-cor, o-st ‘valley’; MHG kar “bowl; hive; clough, hollow in mountainside’; ON ker “tub, goblet’, cf. also kerald ‘tub’
?ordos (?), see ger-, gor- (1) OE ceart ‘rough land’; E chert ‘siliceous sedi- mentary rock’; Li. Zárdas (‘drying-rack; island; granary’. Basic mng. obscure); Latv. zards ‘drying-rack’
ĝounos ‘chap, jowl; gill’. Form of ĝeunos, q.v. and cf. ĝenus Du. koon (jaw, jowl’; dial. ‘gil’); Li. (e-gde in view of Latv. ž-) žiáuna ‘jawbone’; pl. ‘gills’; Latv. Zauna ‘gill’. (Du. -00- is fr. Gmc. -au-. VW:EWNT)
$rnàtos, -itos ‘grained, of grain’. Sce grnóm Alb. i grynjtë ‘wheaten’; Lat. grānātus ‘granu- lar, grained’; It. granato, id. and ‘robust’; gra- nito ‘robust’; s. ‘granite’; OE cyrnod; Norw. kornet; Cz. zrnatý & zrnitý ‘granular
grndó(n) granular formation. Cf. grnóm Lat. grando, gs -dinis "hal": Ir. gráinne “granu- le
$rnóm “cultivated grain, corn, staple grain of the country’. WP I, 600
$onà — gustos, is, us
10
20
25
30
35
40
45
406
Skt. cf. jirnå *caraway-seed' beside jirnah, jūt- nabh ‘decrepit, withered, corny’; Oss. cf. dzárná ‘frumenty’; Per. cf. are ‘caraway seed, ani- seed” beside arzan (?) ‘millet’; Gk. cf. gág- graina, a cpd. like gag-glíon, see gliu-); Alb. grüné, grurë (wheat; pl. in Tosk); Lat. grà- num; Ir. grán ('grain', coll.); MIr. cf. gráne ‘acorn’; W grawn (‘grain’, coll. also ‘berries; roe’); Cor. Br. græn, coll id.; Go. kaúrn; OHG ON Sw. korn; Du. koren; Fris. koarn; OE corn; OCS zrüno and zírno ('grain, berry’, and com. S1.); Srb. zrno; Pol. ziarno; R zernó all i-basis; Li. Zirnis, gs -io, m. ‘pea’; Latv. zirnis, id. Cf. also Lat. granea, coll.: MHG kürne, sn. (Note: Ger. ‘rye’; Sw. & Fris. ‘barley’; Eng. ‘wheat’; Scots ‘oats’; Du. ‘wheat’; U.S. ‘maize’ when ‘corn’ is used in a specific sense)
(ruis, cf. geru-, geur-. Skt. jirvib, jívrih *de- crepit")
Sübh- (&übhs-) ‘surge, uprising, violence” Arm. cf. cupk (“surge, stir”, fr. *&ubhs-); cpem ‘surge’, v.; ON kúfan “force, violence’; Sw. kuva, v. “force, oppress’; R zybí ‘swell’; zy- bletsa ‘swell, surge’, v. (Isophones: OHG küba “tip'; Du. kuif “tuft, crest
(£üg-, see 818- (1). Thus in Du. kuiken ‘peep’; ambig. in Ukr. zyzo-okyj, adj. ‘cross- eyed")
$üos, ios ‘knot, tangle; brain. (For seman- tics, see mosgh-)
Arm. cuc, gs cco ‘pith, marrow, brain’; E cf.
cockle, v. ‘wrinkle’; Li. ZiuZis, io, m. ‘torque’ $ür- (güros, ios) (1) (turned, bent; turn,
bend”
Arm. curi, gs cro ‘bent’; Gk. güros ‘circle’;
gurós “bent, round?
$ür- (2) (£ürio, -eio) “see, spy, look MLG küren “look, spy’; Du. kuren ‘blink’; Li. Ziüriü, éti ‘see’; Ziürà ‘sight’. (Variants in MHG kieren ‘ogle’, fr. *&eur-, and in OCS zrjo, zréti ‘see’, po-zirajo ‘look’; Li. Zyrü, Zirti (2) ‘glint, shine’, fr. *$ir-)
$ür- (3) “mix; tangle, mixture”
Norw. kurre “twist, tangle’; R cf. zrja “higgledy- piggledy'; Li. Ziüre ‘porridge’
$ustos, is, us “pleasant: taste, liking’. Cf. Seuso Skt. jüstah, justáh “acceptable; justih ‘favour’;
=== which leaf ===
LEAF 236
```


## [2026-09-05T20:50:38.493Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf for p.143 (leaf=printed+21 -> 164) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==165' HRN.txt | head -60"
}
```


## [2026-09-05T20:50:40.079Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD arzan / zarman ===\"; grep -n -i \"arzan\\|zarmān\\|zarman\\|zaruwan\\|zurwān\\|zurwan\\|zardu(x)št\\|zardušt\" PHD.txt PHD_mackenzie.txt | head -30"
}
```


### [2026-09-05T20:50:40.344Z] TOOL RESULT

```
=== HRN leaf for p.143 (leaf=printed+21 -> 164) ===
- 143 -
z.
644. ^U", Praefix, w-2-, vergl. suparden (No. 697), siperT
(No. 703).
ap. US' {ustasana-) 'hinauf; aw. us-, uz- 'heraus,
empor ; phlv. uz- (auch w/-, uö- geschrieben); ai. ud,
oss. 'S, -is (216), e- in oss. z[mänfin *zusammenrühren,
vermischen (133) ist unsicher.
645. xäden *gebären ; geboren werden*, 'Praes. zay-em,
zad 'Geburt' {-zad, mlrzä), zaj^ zaje 'Wöchnerin*,
zOq ') junges Huhn', zeh * Junges, Kind', zehdan 'Uterus*,
zehistän 'Fehlgeburt, Placenta' (AM.), jüd.-pers. TIM
(Salemann, Litbl. f. or. Phil. II, 81), zatjlden.
aw. [/'zan-, zayata gebären; geboren werden, us
zayfAte, zata-; phlv. zatan, zay(i)sn, zak (aw. zqda-,
y. 42, 5 b); ai. [/"^aw-, Jdyate, ^ki\ jfati- *6eburt'; arm.
ein 'Geburt', cnanim 'erzeugen' (H. No. 136).
kurd. zain gebären ; af/. zez\edal geboren werden',
zez\avul 'erzeugen*, s'opmZ 'gebären'; oss. -eäwclr// 'wachsou*,
zayi (125); bei. zäyag, n. zay 'gebären, hervorbringen*
(423), 'Za/t 'Sohn' aus "^zatk (418) ; wa/. yäz-am, sar.
zay -am,
646. {\)xär 'Klagen', zäri^ zäre^), zandefi.
ai. 3 l/^ar-, jdrate 'rauschen, schnattern, rufen*,
afy. Sarai 'klagen'; oss. d. zarw?, t. zarin singen'
(128).
647. {^)»är 'schwach, elend*.
Wohl zu aw. [/'zar- 'altern' (vergl. np. zer, No. 655) ;
phlv. zär, zarth (Bund.).
648. zäl 'Greis, Greisin'.
aw. i^zar- altern', vergl. zaurvan-, zatirura-; ai.
1 l/yar-, jdra- 'alternd*.
*) Arm. LW. jag 'junger Hund*, syr. LW. j|T fdo Lagardo,
T
Ges. Abh. 41).
-) Xp. zävp (VuUcrs) ist vorloaon fius zäre.
```


### [2026-09-05T20:50:40.394Z] TOOL RESULT

```
=== PHD arzan / zarman ===
PHD.txt:214:a-pus [' BRE] without a son, childless. ár-, v. árdan. 5 āranj "Inc | N ~] elbow.. 9-43. "Ant *a-rāst Prst'] untruth. ārāstan, ārāy- [Pstn!,^Pd- | N ~] prepare, arrange, adorn. ~ién: arrangement, adornment. a-rawüg [”/wbk!] immobile. Ard р | M?yrd, N ~] a goddess; cal. 25th day. ard [KHM A < А gm; п | N ~] flour. агаа [py | (M rd?w)] righteous, truthful. ardan, ār- [THNN-tn' < А V thn; ?l-tn'] grind, mill. ardāyīh ['i?dyh | M?rd?yyh] righteousness, rectitude. ardig [/tyk! | M ?rdyg] battle. ardikkar рук], -kl | M?rdyqr] warlike, warrior. ~ith: doing battle. arduš [”ldwš = Av. aroduš-] a degree of sin. Ardwahišt Prtwhst' | M ?rdywhyst, (N urdībihist)] Right, the second Amahraspand, guardian of fire; cal. 2nd month; 3rd day. arešk [lysk' | M ()rysk, N rašk] envy, jealousy. ~én [-yn'] envious, jealous. ārešn Pim! | M ”7ysn-, N (a)rif] cubit. aryand [?/епа | N ~] horrible. arģawān [*/gwk'*n! | N aryawān] purple. armēšt ["/myst'] inactive, infirm. ~ih: infirmity. armēšt-ģāh [-g’s] secluded place for the infirm. агбуї&п [/wdšn'] growth. ~ig [-y&!] growing, vegetable. ars Dis | M?rs, N ~] tear (drop). artēštār УЯ? | N artēšdār!] warrior. „īh: warriorhood. arus [2/00] white. arwand [wnd] swift, valiant; river Orontes. ~ih: swiftness, valour. arwés [lwys | M ?rwys, N ~] rope. arz [KSP! < А Ар; с | N ~] worth, value. Arzah [Iz h == Av. arazahi-] the eastern continent of the earth. arzan [PE < А prg’; len! | N <) millet. arzàn Plen | M *rz'n, N ~] valuable, worthy. ~ig [-yk'] worthy. ~igih: value, worth, worthiness. arzidan, arz- [?/с-уїп! | N ~] be worth. ~išn: value, worth. arziz (сус | M ?rzyz, N ~] tin, lead. —ën [-yn'] tin, leaden. ārzōg Picwk! | M'wrzwg, N àrzó] desire, lust,
PHD.txt:225:ayābāģ Dy'p()£!] acquisitive, receptive. ~ih: comprehension. ayād Pbyd?t' | M? yd, N yad] memory. ~ kardan; remember. ~gar LEI | N —gàr] memoir. āyaft Pdypt' | M ?ypt, N āyift] boon, favour, gift. ayāftan, ayüb- [5?5-tn! | M *3pt,*?b-, N yāftan, yab-] obtain, acquire, attain. ayār [kdybl | M hy’r, N yar] helper, friend. ~th: help, friendship. ayārdēnīdan, ayārdēn- ['4?/tyn-ytn!] boil, agitate. ~i&n: agitation. ayārdīdan, ayārd- Py’lt-ytn! | M ?y^rd-] be agitated, seethe. ayārīdan, ayür- [hdyb'l-ytn! | N yār-īdan] 1. help, assist; 2. be able, dare. ayürómand [hdyb’Pwmnd | N yarmand] helpful, friendly. ~ih: helpfulness, friendliness. ayāsīdan, ayās- [’byq’s-yin' | M ?y^s-] remember, be mindful of. „išn(īh): memory. ayāstan [by@’sin' | M *)*st] = ayāsīdan. āyišm [dšm] moon. aydxšust [ywhhhwst! = Av. ayóxfusta- | M ”ywxšyst 1] metal. ~€n [-yn'] metallic. āydoxtan, āyēz- ['ywhtn!, ?ywc-] join, yoke. ~išn: union, alliance. 14ydzidan Pyweytn'] = āyēūxtan. tāyozīdan, āyoz- Pywe-ytn' | Р уші, ?ywz-] trouble, disturb; strive, struggle. ^-i$n(ih): endeavour, strife. laz [MN < A mn; hc | Mc, ?z, N ~] from, than. žaz Dell dragon. *az [ANE < A?nh | P >z] I. āz Pc | M ?z, N ~] greed, lust. Ba, z- azabar [hcpl | M?c?br, № zabar] above. 7 āzād Pot! | M ?zd, N ~] r. noble; 2. free. āzādīh Petyh] т. freedom; 2. gratitude, thanks. ~ ģuftan, ~ hangardan, ~ kardan, pad ~ dāštan: thank, give thanks. атат [?с?[ | N ~] torment. āzardan сіп! | M ”zyrdn] = azardan. āzārdan, āzār- Pc/-tn! | № ~] torment, injure. ~išn: torment, injury. lāzarm [clm | M ??zrm, N ~] honour, respect. *'ázarm [?clm | M ?zrm-] harm, injury. a-zarmān Pz/mn!] ageless, unaging. āzarmīģ [clmyk'] honoured, respected. ~th: honour, respect.
PHD.txt:356:frazand [prznd | M frzynd, N farzand] child, son, offspring.
PHD.txt:426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
PHD.txt:455:mand [mnd | = M] house. miindag [m?ndk! | M m'ndg, N ~a] tired; remiss; fault, sin. “Аһ: tiredness. māndan, !màn- [K TLWN-tn! < A У ktr | M mnd, N ~] stay, remain; v. also % *mán-. mang [mng] henbane. mänig [mnyk'] household member. mānistan [{KTLWNstn'] = mandan. māništ [m?nyst!] abode, dwelling. ~ag [-k'] sedentary, settled. mānsār [mnsl = Av. ma0ra-] (holy) word, spell. -~-bar [-b/] priest. ~spand [-spnd = Av. spanta-] holy word; v. máraspand. imar [ml | M mr, N ~] number, reckoning, account; class. *mar [m/] scoundrel, felon. таг [ml | N ~] snake. mār-, —išn, v. mārdan., тагар [mik!] number. тпагар [mPk!] perceptive, sensitive. Māraspand [mrspnd | N ~] (= máns?rspand), cal. 29th day. *martabuk [mic”5wk'] brave, valiant. ~ith: bravery, valour. mard [GBRA < A gbr; mlt' | M m(y)rd, N ~) man. mārdan, màr- [ml-tn'] perceive, notice, feel. ~i$n: perception. „išnūmaud [-£rwmnd] perceptive. mardanag [mit?nk! | N ~a] manly, brave. ~ih: manliness, bravery. mardóm [ANŠWTA < A?niwt?; mltwm | M mrdwhm, N mardum] man, mankind, people. ~th: humanity, humanness. mardóm-zàádag [mltwm 2tk' | N mardum-zād] human being. ~ih: humanity. marģ [mlg | M mrg, N ~] death. ~-arzan [-lc’n'] deserving death. ~ih: = marg. --0mand [-”wmnd] mortal. mārīģ [m'Lyk! | M mryg-] word, spell. marw [mlw! | M mrw, N —, (mary)] herb. marz [mlc | M mrz, N ~] boundary, march; astr. term. marzanģēūš [mlengws | N ~] marjoram. marzidan, marz- [mlc-ytn! | М mrzyst, mrz-] copulate. išn(īh): copulation, fornication. marz(o)bàn [mlcp’n' | № ~] margrave, warden of the marches. -masāy [-ms'd] suffix, -sized. mast [mst! | = M, N ~] bemused, intoxicated.
PHD.txt:605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
PHD.txt:677:zamān [ОЮМА < А ‘dw; gwn’, zmn! | M zmn, N ~] time, hour. ~ag [zm)nk!] = zaman. *zamānīģ [zm”nyk'] prescribed. zāmēnīdan, zāmēn- [p myn-ytn' | M z?myn-] lead, send. zamestān [z7nst?n! | (М dmyst?n), N ~] winter. zamīģ [z-, zmyk! | M zmyg, N zami] earth. ~ig [-yk'] terrestrial, earthly. ---paymānīh [-pim’nyh] geometry. zāmyād [*zmd't! (misreading of z'myzdt! = zām-yazd?) | М myd, N —] cal. 28th day. zan[NYSE < A nth; zn! | = M, N ~] (ĝl. -ān, -in) woman, wife. zan- , —i$n, v. zadan. 1zand [znd | N ~] commentary, explanation, Zend. *zand [zzd | = M] district, tribe. zandag [zndk! | N zanda] rampant. zandbed [zndpt' | M zndbyd] headman of a district, tribe. zandik [zndyk' | N ~] heretic, Manichaean. rmih: heresy. zang [zng] ankle, shank. zangig [zngyk! | N zangi] negro. zanjir [zncyl | (P zyncyhr), N —] chain. zānūg [2”nwk! | P z^nwg, N zānū] knee. zard [21 | N ~] yellow. ~1һ : yellowness. zardaģ [z/tk! | N zarda] (egg) yolk. zardak [zltk! | N ~] safflower. zard|-alüg [zit?hwk! | N ~ü] apricot. ~-tdbag [-cwpk! | N —čēba] turmeric. Zardu(x)&t [zltw(h)st' | (M zrdrwšt), N Zardust] Zaraduštra, Zoroaster. zargon [zlgwn' | P zrgwng, N zaryün] golden, green, fresh. ^ jh: greenness. zarig [zlyk' | M zryg] sorrow, grief. ~6mand [-’wmnd] sad, sorrowful. zarmān [zin?n! | M zrwn-, N ~] old man; old age, decrepitude. ~ih: old age. zarr [ZH BA < А zhb’; DHBA < A dhb | M zr-, N ~] gold. ~én [ZH B Aua. zlyn! | M zryn, N —in] golden. ~(i)gar [zlykl | N ~gar] goldsmith. zarwan [2/wp?n! | P zrw’n] old age. zastan, zāy- [zstn!, z())d-] ask, demand. zaxm [ztm, z?hm | (P jxm), N ~] wound. тау [zyd$ = Av. zaya-] instrument, weapon. ZÁy-, v. zastan. zay-, -išn(-ig), v. zádan. Zāyč(aģ) [z'yc(k') | N zāyča) horoscope. zayistan [2”dstn'] = zastan.
PHD.txt:683:zurwan [zwlw’n'] time; the god Time, Zurvan.
PHD.txt:752:age dad, -sālagīh; old -- pīrīh, zarman(ih), zarwan. aged pir.
PHD.txt:753:ageless azarman. aggression hénih. aggressive mustabarmand. agile čābuk.
PHD.txt:1148:Cancer Karzang.
PHD.txt:1431:crab karzang.
PHD.txt:1527:decrepitude zarman.
PHD.txt:2714:man mard, wir; (—kind) mardēm; the First ~ Gayómart; old ~ zarmān; young — mérag.
PHD.txt:2731:marjoram marzangēš.
PHD.txt:2811:millet alum, arzan; giant ~ gahl, gawars.
PHD.txt:4108:unaging azarmān.
PHD.txt:4169:unworthy anarzanig.
PHD.txt:4355:worth arz, arzanigih, arzišn, arz- ómandih; be ~ arzidan.
PHD.txt:4381:Zoroaster Zardu(x)št.
PHD.txt:4407:Way ī weh Zurwān
PHD.txt:4743:padrazm sò rey о) pādifrāh © teras arzan!, gāwars! 5o)
PHD.txt:4851:marzangūš
PHD.txt:4996:kulang kirrdg sett kargās karkēhan kark karm, kirm karmīr karb, kirb karafs karbunag karzang kardār
PHD.txt:5074:zāy-! zāyišnīgi zāyišnī! zādan! 1-2zrëh zarrën | zargónih - zargon zarigomand zarig zarr(i)gar kàr-! kistárt kištant zalüg zraw- zarwan zruftan zarmānīh zarmān zardālūg zardīh zard Zardu(x)št
PHD_mackenzie.txt:1192:arzan [PC < A prg); 'len' I N ---] millet.
PHD_mackenzie.txt:1193:arzan [)/e'n I M: 'rz'n, N -] valuable, worthy.
PHD_mackenzie.txt:2372:frazanag [plc)nk I P frz)ng, N farzana] wise, intelligent.
PHD_mackenzie.txt:2376:frazand [pr~nd I M frzynd, N farzand] child, son, offspring.
PHD_mackenzie.txt:3249:·karzang [klcng I M kyrzng, (N xarcang)] crab; astr. Cancer.
```


## [2026-09-05T20:51:02.170Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 165-166 more (p.144) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==166' HRN.txt | head -40\necho \"=== HRN grep zer 655 / arzan / zire ===\"\ngrep -n \"655\\.\" HRN.txt | head\ngrep -n \"arzan\\|zTre\\|zire\\|zTra\" HRN.txt | head -10"
}
```


## [2026-09-05T20:51:03.651Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT zaurvan / zarǝman / azarǝma / zaraθuštra ===\"\ngrep -n \"zaurvan\\|zaurura\\|zarǝman\\|zarəman\\|azarǝma\\|azarəma\\|zaraθuštra\\|zara9uštra\\|zarathuštra\" BRT.txt | head -30"
}
```


### [2026-09-05T20:51:03.870Z] TOOL RESULT

```
=== HRN leaf 165-166 more (p.144) ===
— 144 —
bei. LW. zal 'Frau', spec. 'Ehefrau, Gattin (419);
af/. zör; yidg. zör 'alter Mann, Greis.
Hier stehen r und / im Neupersischen neben einander
(vergl. zer, No. 655). Nach den persischen Wörter-
büchern ist dieser Fall sehr häufig, doch läuft hier
viel Dialektisches mit unter. Meine Sammlungen über
den Gegenstand sind noch nicht abgeschlossen, so dass
ich über die Stellung des Neupersischen zu Brug-
mann's Erwartung (Grundriss I, 210, 211) noch kein
Urteil habe gewinnen können. Doch glaube ich nicht
an wichtige, positive Ergebnisse.
G48*^'« i^änü 'Knie .
aw. zänti' 'Knie' in zänu,[dräjao , vergl. frasnu-
(skr. prajUn-) ^) ; phlv. zünük, jfänäk (letzteres entweder
dialektisch oder auch zänük zu lesen); 2l\, jdnu- 'Knick-
arm, cunr 'Knie* (H. No. 138).
kurd. zCLna; af/. zangün^ cangün; bei. zän (421);
wa;^. zatij sar. zm^ sangl. zong.
649. t^äiv 'Spalt, Riss'.
Zu [/"gap" {Jap-) 'klaifen, tief sein , vergl. aw. Ja/ra-
jqfnH' (Nöldeke, mündliche Mitteihmg).
i)i}0, ^ehän, zuhän (AM.) 'Zunge*, zefan-),
g. izvFin (Käs. Q. ilzün ist natürlich arab. lisän).
ap. izavani'^) 'die Zunge*; aw. hizü'\ phlv. nzvän
bezw. huzDän, ziivän bezw. zavän ; ai. jikvä-,
kurd. azmän 'Zunge'; af/. ziha\ oss. t. äuzdg (4);
hol. LW. ztivan^ n. zavan (311); siyn. zev, sar. ziv,
wa/. zik.
Über die indogerm. Grundform hat zuletzt Johans-
son Indog. Forsch. II, 1 folg. gehandelt.
051. lieber 'über, darüber, auf, zewer, vergl. zehet'dest 'die
Oberhand besitzend'.
') Über znii' wird hoffentlich die neue Ausgabe Klarheit bringen.
2j z/f/. X^'ärezm. Fol. 656 r (Berliner Handschrift); jedenfalls
dialektisch, vielleicht ;^^'ärezmisch.
'j Vordflchti<»o Form; Bartholoniao, BB. XIV, 245 vermutet
hiznrani.
=== HRN grep zer 655 / arzan / zire ===
5812:655. {2).'^er 'Greis, Greisin'.
14091:^fr 654, 655.
14706:Z(-™s-Hs(,-n- 655.
21376:t. zarond 655.
22170:tvr 655.
6006:681. zirek 'klug, entschlossen', äHr,
```


### [2026-09-05T20:51:03.932Z] TOOL RESULT

```
=== BRT zaurvan / zarǝman / azarǝma / zaraθuštra ===
4803:mit  upa  i)  'hinzugehen,  kommen  zu—' (Akk.):  upa  tqm  vanqm  asiü  V.5.2;  — aS?m  . .  asisi>m  zaurvan>m  (sd.)  upaitt'^ yal  spatiS  Y.ij.28.  a)  spez.  'in  die Schule  gehen  zu  — ':  Jt^m  *afm  at  (sd., No.  6)  afirapaitim  upayat  (3SKA.)  "zu welchem  Lehrer  soll  er  dann  in  die  Schule gehen?"  N.  r2.  2)  I!  'gelangen  nach  — ',
27934:Zum  ai.  V.  jiryaü,  jiiyati  'er  wird  gebrech- lich', yara/i  'er  macht  gebrechlich'.  S.  noch azarima;  azanianl-,  zaunira-,  'zanta-,  zaurvan-, :ara%uilra-.  —  Vgl.  np.  aar,  aast,  sätoiid 'Greis'.  —  Pü. :  izäriar,  erl. :  xärkarih  i  tu  ke vas  ^apcl  :är  apc  bavet.
27947:•  j.  zaurura-  Adj.  'altersschwach,  gebrech- lich':   han^  vä  'rö  vä  pairiitä.xludrS  vcl
27978:•  j.  zaurvan-  m.  'Greisenalter,  Alteis- schwäche':  tail  'va  . .  »i»Y  vanhyus  Y. 9.5;  —  ■»«  °vqm{,h&^a  mpffkyümca  Yt g.  10;  ■ —  'va  *duidq  (sd.)  f^rS  Jonttaoiti V.  ig.  43;  F.  20;  —  amm  ..  Osistsm •vJfum  upäiti  yat  spStts  ySi  . .  "das  . , kommt  am  raschesten  zur  Gebrechlichkeit des  Alters,  (was)  die  Himde  (sind),  die  . ." V.  13.  a8.
```


## [2026-09-05T20:51:11.790Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '27915,27950p' BRT.txt\necho \"=== BRT azarǝma / azarǝmant ===\"\ngrep -n \"azariiiia\\|azarima\\|azarəm\\|azarima;\\|a  zarima\\|azaman\" BRT.txt | head -10\necho \"=== BRT zaraθuštra headword ===\"\ngrep -n \"ara%uilra\\|arathuUra\\|Zarathustra\\|zara9u\\|arauuštra\\|arathustra\" BRT.txt | head -10"
}
```


## [2026-09-05T20:51:11.844Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5805,5825p' HRN.txt"
}
```


### [2026-09-05T20:51:11.875Z] TOOL RESULT

```
•  j.  zaranyö.viir«9inan-  Adj.  'des  Brust- wehr von  Gold  ist':  mi^nm,.*man3m  Yt,
•  j.  zaranyö.vääa-"  Adj.  'des  Wagen  aus Gold  ist':  valm  *i»m  '*  . .  zaranyS.caxr9m Yt.  15.  57.
■)  Die  guten  Hds.  haben  'vaUm,  das  allen- falla  zum  V.  vas-  gehören  könnte  (S  JJ  U); geringe  Stelle.
•  j.  zaranyö.tuvix&na- Adj. 'mit  goldener Verschnüning':  andvl . .  ao%ra  *päili. smuxta  'na  ". .  mit  Schuhwerk  angetan, das  mit  goldenen  SchnUrbändem  befestigt ist"  Yt.5.  64.
aby  Google
lar;  Npii. :  sah  rang;.  —  0  Vgl,  RV.9.65.8;
•  j.  zairi.gaosa-  Adj.  "mit  gelben,  gold- farbigen Ohren':  spanim  .  .  spaStim  'sim V.if.  16'  17,  18;  —  aspahe  ..  aurus'afie .  .  'sähe  Yt.Äi8.
Pii.:   -.<xri  gö's.
•  j.  zairi£i-  f.  EN.  einer  gläubigen  Frau: 'cyi  asaonyä  ¥17^,139.
Eig.  fem.  la  ^zairyank-;  sd.  und  sairit:  Also eig.  'die  Reibliche';  Kurinamc?  —  Vgl,  S  S, 164-  3  (lä),  wozu  aber  Hbm.  IFAnz.  6.  32.
•  j.  "zairita-  Adj.  'gelb,  fahlgelb':  span>in 'hm  ca%ru.(asm3in  V.J.  16',  17,  18;  — ffiftM  .  .  yim  .  .  "iim  Y.  p.  1 1 ;  —  aisis 'iahe  Y.p.30; — yim  upairi  ^vis'^rao&at .  .  'hm  Y.g.ii.
aX.  Aärita-  Adj.;  np.  vgl,  lard,  woiu  S  202 No.  —  Vgl.  'zairita-  EN.  —  Pü.r  zart,  SQ.; bkilah,  pS/alai.
•  j.  zairita-  in.  EN.  eines  Gläubigen: datahahe  'Iahe  Yt  13.  98.
Vgl.  'sairita-.  —  Eig.  'der  gelbüehe';  Kurt- name? —  ai.  harita-  m.  EN.
•  j.  zairi.döiSra-"  Adj.  'mit  gelben,  gold- farbenen Augen':    haomü  frasmü'  .  .  'rS
Y.57. 19.
Pü.:  :arren  äiiir,  erL;  kus  (aim  latanak  [sva lar,  V.  3.  26;    Npü.!  Töin).    —    ■)  NA.  ima
•  j.  zairi-päSna-  Adj.  'mit  gelber,  gold- farbener Ferse  (?):  gattdarswan  (sd.)  yim 'n>m  YL5.  38,  75.41-
•  j.  zairina-  Adj,  (fem.  '«ä-)  'aufreibend, erschlaffend',  von  der  BsHyastä  (sd.): bU^yasia  yä  'na  V.U.  9;  —  ÖBsyashm 'mm  Yt  18.  2.^
Zum  ai.  V.  jiryaü,  jiiyati  'er  wird  gebrech- lich', yara/i  'er  macht  gebrechlich'.  S.  noch azarima;  azanianl-,  zaunira-,  'zanta-,  zaurvan-, :ara%uilra-.  —  Vgl.  np.  aar,  aast,  sätoiid 'Greis'.  —  Pü. :  izäriar,  erl. :  xärkarih  i  tu  ke vas  ^apcl  :är  apc  bavet.
•  j.  tairimya-  n.  'festes  Haus,  Gehäus'. KompA.;  Ableit  —  ai.  vgl.  harmyi-  n.;  s. daiu  IF.  /.  70.
•  j.  zairimyafsinan-  Adj.  -  ?  -'':  'ma {NSm.,  näml.  ist  der  Hund)  %ryafsma yaka  vals3 . .  °ma  %rya/sma  ya%a  jahika V.  13.  46  und  48.
Wohl  Komp.:  *zairimya-.^afimati:  —  Pü.: ni:är  patmän  ^J,  erl. ;  Jrahang  1  val  (a/)  itintnd. —  O  DsT.  ZA.  3.  207  'mal  dress«',  nach PQ.  —  »)  Vgl.  lu  '.airi^ia-.
•  j.  zairimyaDUra-  m.  Name  eines fAiftischen  Tiers,    'Schildkröte"':    da^m
1682
yim  'rpm  nqma  ..yim  maiyäka  avi  duiva- ^avJtS zairimyaksm^&A.)  nqma  ao/ai/e"dcn Dasva  Z.  mit  Namen,  den  die  Übel- redenden Leute  Z,  nennen"  V.  13.  ö. Komp.;  zairimya-  +  *a/mra-  'des  Glieder  (oder Zehen)  in  einem  festen  Gehaus  stecken';  a  in der  KompFuge  statt  £  (bi.  i,  %  sgS.  ^),  %  36S. 3  b.  *aoura-  (statt  'angura-,  %  268. 47  c)  m. 'Glied'  oder  "Finget,  Zehe';  vgl.  ai.  anga- n.  'Glied',  aiigülof-  f.  'Füiger,  Zehe';  woss. ong  'Glied',  änguljä  'Finger*.  —  Vgl.  ioirim- yäia:  —  ai.  vgl.  harinu/a-  m.  'Schildkröle'.  — Pü, :  transskr.  [larimangur),  Npü. :  läi  fait.  — <)  Sa  nach  Npü.  nnd  Gü. ,  deren  Angaben von  der  Etymologie  nnterstätit  werde«.  GcR. OK.  160  denkt  vielmehr  an  den  Maulwurf. S.  noch  Sp.  Komm.  i.  297.
•  j.  zairimyäka-  m.  anderer  Name  des zairimyamtra-:  daiumyim  tairimyatiunm (sd.)  nqma  yim  maiySka  avi  duivaiaaAS 'hm  nqma  aojaite  V.  13.  6.
Abkürz,  aus  lairirnyauura-,  mit  KosesafT,  — Pü. ;  unverändert  in  Aw.-Buchst.
•  j.  zairimyä'vant-  Adj.  'der  ein  festes Haus  besitzt',  vom  Mond:  mätthim  . . •vanfym  Yt  7.  5.
FB.;  sabiSmand,  Npü.:  saiz  rang,  ei\.:  Jihän sar  sabt  kunad;  daher  DsT.  ZA.  2.  409  'maitre de  la  verdure'.
•  j.  zairi.varay-  m.  EN.  eines  Helden der  iranischen  Sage;  Sohn  des  Aurvat.- aspa  und  Bruder  des  Vlitäspa:  tarn  yasata aspsyaols  'vairii  *falne  apS  daityayS  Yt. J.  112;  117');  —  •»■^»7  asaonS  Yt  13.  101.
Eig.  'der  eine  gelbe  (eherne)  Brustwehr  trägt'. —  Zum  np.  larer  usw.  s.  Hbm.  PSt.  69,  170, JusTI  NB,  382.  —  «)  Hier  trotz  £tlr.  a.  929 eingeschoben.
•  j.  zaurura-  Adj.  'altersschwach,  gebrech- lich':   han^  vä  'rö  vä  pairiitä.xludrS  vcl
V..5.I9-
Zum  ai.  V.  jiryali;  s,  zu  sairino'.  —  Bildung wie  ai.  qiurd-,  bahulä:  —  PD, :  sarmäH.
•  j.  'zar«ta-  Adj.  (fem.  'tu-),  PPfP.: s.  zar:
=== BRT azarǝma / azarǝmant ===
27934:Zum  ai.  V.  jiryaü,  jiiyati  'er  wird  gebrech- lich', yara/i  'er  macht  gebrechlich'.  S.  noch azarima;  azanianl-,  zaunira-,  'zanta-,  zaurvan-, :ara%uilra-.  —  Vgl.  np.  aar,  aast,  sätoiid 'Greis'.  —  Pü. :  izäriar,  erl. :  xärkarih  i  tu  ke vas  ^apcl  :är  apc  bavet.
=== BRT zaraθuštra headword ===
27793:zara9u£tra-  b
27829:KompA.;  Ablcit.  —  Komp.:  *zarant-  Adj, 'alt'  {ek.  j'ärant-  Adj.,  OOSS.  täron//)>)-\-uslra; eig.  'des  Kamele  alt  sind';  S  3^*4  ^  44! weiteres  bei  Jn.  Zor.  13.  —  i)  Man  erwartete tara%uilrahyäi    %  412    Bem.  I.    —    i>   S.   m
27934:Zum  ai.  V.  jiryaü,  jiiyati  'er  wird  gebrech- lich', yara/i  'er  macht  gebrechlich'.  S.  noch azarima;  azanianl-,  zaunira-,  'zanta-,  zaurvan-, :ara%uilra-.  —  Vgl.  np.  aar,  aast,  sätoiid 'Greis'.  —  Pü. :  izäriar,  erl. :  xärkarih  i  tu  ke vas  ^apcl  :är  apc  bavet.
30213:Pourucislä,  die  jüngste  Tochter  Zara%uilras\
```


### [2026-09-05T20:51:11.889Z] TOOL RESULT

```
Mitth. aus d. er. Samml. d. K. Mus., Heft lY, S. 25), wie der Eigenname
Zerer (yergl. Nöldeke, Pers. Studien II, 2, Anra.).
') Trotz der Schwierigkeit, die Form mit ap. diivar- zu vereinigen,
erklärt G. Hoffmann, Zeitschr. f. Assyr. II, 49 folg. (JapHxds als
^königl. persische Hof- und Reichsmunze im Gegensatz zur ausser-
persischen Währung'.
Hörn, Grtindriss d. neup. Etymologie. 10.._ 146 —
655. {2).'^er 'Greis, Greisin'.
aw. vergl. Zarad'lustra" ; ai. jdrant-; arm. cev
'Greis' (H. No. 135). Vergl. np. ^ol (No. 648).
oss. t. zärond alt' (129).
656. zerd gelb', vergl. zerd[ab^ zerde 'Galle'.
aw. zairita- 'gelb' ^) ; plilv. zart, zartth, syr. LW.
plDI; ai. hdrita-.
kurd. LW. zercl ; af/. ziyar; bei. LW. ;earf/ (303);
wa/. LW. 2;arrf, si;'n. ^f/Y?, sar. ^-^Vd.
657. ^nrd, zurt 'Art Hirse' (arab. LW. öurat)),
g. jurda 'Getreide'.
phlv. jtirtäk bezw. zurtäk 'Getreide'; bei. (LW.?)
zurf 'jowar'.
Die Vereinigung mit arm. gari (H. No. 65), lat.
```


## [2026-09-05T20:51:33.855Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['KLN']['page_offset']);print(d['BQT'].get('page_offset'));print(d['BQT'].get('lookup_hint'))\"\necho \"=== KLN granite ===\"\ngrep -n \"granite\" KLN_1966.txt | head -10"
}
```


### [2026-09-05T20:51:35.706Z] TOOL RESULT

```
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
=== KLN granite ===
16525:grain,  n.,  seed,  com.  —  F.,  fr.  L.  grdnum,  ‘grain, seed,  small  kernel’.  See  com,  ‘grain’,  and  cp. gamer,  garnet,  gram,  ‘chick-pea’,  granadifia, granary,  grange,  granilla,  granite,  granule,  gre¬ nade,  grenadier,  grenadine,  engrain,  filigrane, pomegranate,  grogram.  Cp.  also  gravy.
16566:graniferous,  adj.,  producing  grain.  —  Formed with  suff.  -ous  fr.  L.  granifer,  ‘grain-bearing’,  fr. granum,  ‘grain’,  and  the  stem  of  ferre,  ‘to  bear, carry’.  See  grain,  ‘seed,  com’,  and  -ferous. granilla,  n.,  the  refuse  of  cochineal.  —  Sp.,  di¬ min.  of  grana,  ‘cochineal’,  rel.  to  grano,  ‘grain’, fr.  L.  granum.  See  grain,  ‘seed,  com’, granite,  n.  —  F.,  fr.  It.  granito,  lit.  ‘grainy’,  pp. of  granire,  ‘to  make  grainy’,  fr.  grano,  ‘grain’.
16570:Derivative:  granit-ic,  adj. granitiform,  adj.,  shaped  like  granite.  —  Com¬ pounded  of  granite  and  -form, granivorous,  adj.,  feeding  on  grain.  —  Com¬ pounded  of  L.  granum,  ‘grain’,  and  vorare,  ‘to devour’.  See  grain,  ‘seed,  corn’,  and  -vorous. granny,  also  grannie,  n.,  a  familiar  form  of  grand¬ mother.  —  Formed  from  the  first  syllable  of grandam  and  dimin.  suff.  -y,  resp.  -ie. granophyre,  n.,  a  porphyritic  igneous  rock  (pe- trogr.)  —  G.  Granophyr,  formed  from  the  first syllable  of  Granit  and  the  second  syllable  of Porphyr.  See  granite  and  porphyry.
21264:Laurentian,  laurentian,  n.,  a  kind  of  granite  and granitic  gneiss  in  Canada  ( geol )  —  Named  from the  Laurentian  Mountains  in  Canada,  them¬ selves  called  after  the  St. Lawrence  River.  For  the ending  see  suff.  -ian.
27887:spring’,  is  folk  etymology, pegmatite,  n.,  a  coarse  granite  rock  ( geol .)  —  F., coined  by  the  French  mineralogist  Rene-Just Haiiy  (1743-1822),  fr.  Gk.  7trjYp.a,  gen.  nipf- [xaTop,  ‘something  fastened  together’,  from  the stem  of  7TY]YvuvaL,  ‘to  make  firm’,  fr.  I.-E.  base * pag -,  *pdk-,  ‘to  join  together’.  See  pact  and words  there  referred  to  and  cp.  esp.  parapegm. For  the  ending  see  subst.  suff.  -ite. pegomancy,  n.,  divination  by  fountains.  —  Com¬ pounded  of  Gk.  7nr]Y7),  ‘fountain,  spring’,  which is  of  uncertain  origin,  and  fxavTEioi,  ponma, ‘oracle,  divination’,  for  which  see  -mancy. peignoir,  n.,  lady's  loose  robe.  —  F.,  fr.  peigner, ‘to  comb  the  hair',  fr.  peigne,  ‘comb’,  fr.  L.  pec- linem,  acc.  of  pecten,  ‘comb’.  See  pecten. pejorate,  tr.  v.,  to  depreciate.  —  Late  L.  pejordtus, pp.  of  pejordre,  ‘to  make  worse’.  See  pejorative. Derivative:  pejorat-ion,  n. pejoration,  n.,  depreciation.  —  Formed  with  suff. -ation  fr.  L.  pejor,  ‘worse’.  See  next  word. Derivative:  pejoration-ist,  n. pejorative,  adj.',  depreciative,  disparaging.  — Formed  with  suff.  -ive  fr.  L.  pejordtus,  pp.  of
28160:peridot,  n.,  a  yellowish  green  variety  of  chrysolite ( petrogr .)  —  F.  peridot,  of  unknown  origin. Derivative:  peridot-ic,  adj. peridotite,  n.,  any  of  a  group  of  granitelike  rocks. (mineral.)  — •  F.  peridotite,  fr.  peridot.  See  prec. word  and  subst.  suff.  -ite. perigee,  n.,  the  point  at  which  the  moon  (or  anoth¬ er  celestial  body)  is  nearest  to  the  earth.  —  F. perigee,  fr.  ML.  perigeum,  perigaeum,  fr.  Gk. raptvetov,  prop.  neut.  of  the  adjective  rapiyeioc, ‘around  the  earth;  near  the  earth’,  but  used  by- Ptolemy  as  a  noun  for  r.epiye tov  aijustov,  ’the sign  near  the  earth",  i.e.  ’perigee',  neptveio?  is formed  fr.  rapt  (see  peri-)  and  yij,  ‘earth'.  See geo-  and  cp.  apogee.
37777:syenite,  n.,  a  gray,  igneous  rock  allied  to  granite (petrogr.)  —  L.  Syenites  (lapis),  lit.  ‘(stone) from  Syene',  coined  by  Pliny  as  loan  translation of  Gk.  2ur(vfrv);  XiSoc  (a  term  used  by  Diodorus Siculus),  lit.  ‘stone  from  Syene’,  fr.  So ryr,  (L. Syene),  name  of  a  town  in  Upper  Egypt,  fr. Egypt.  5hv!  (Copt.  Suan,  Heb.  Scweneh,  Arab. Aswan;  now  called  Assuan);  so  called  because it  was  anciently  quarried  at  Syene.  For  the  end¬ ing  see  subst.  suff.  -ite.
```


## [2026-09-05T20:51:44.305Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /granite,  n\\.  —  F\\.,  fr\\.  It\\.  granito/{print \"LEAF \"NR}' KLN_1966.txt\nawk 'BEGIN{RS=\"\\f\"} NR==350' KLN_1966.txt | grep -o \"67[0-9]\" | head\necho \"--- KLN corn ---\"\ngrep -n \"^corn,  n\\.,  grain\\|corn,  n\\.,  grain\" KLN_1966.txt | head -3\necho \"--- KLN carl/churl ---\"\ngrep -n \"^carl,  n\\.\\|churl,  n\\.\" KLN_1966.txt | head -5\necho \"--- KLN Charles ---\"\ngrep -n \"Carolus\\|^Charles\" KLN_1966.txt | head -5"
}
```


### [2026-09-05T20:51:47.191Z] TOOL RESULT

```
LEAF 365
--- KLN corn ---
9210:corn,  n.,  grain.  —  ME.,  fr.  OE.  corn,  rel.  to  OS., ON.,  OFris.,  OHG.,  MHG.,  G.  korn,  MDu. coren,  corn,  Du.  koren,  Goth,  kaurn,  ‘grain’, and  cogn.  with  L.  granum,  ‘grain,  seed,  small kernel’,  Gk.  ytyxpTov,  ‘grapestone,  olivestone’, OSlav.  zrino,  zruno,  ‘grain’,  OPruss.  syrne,  ‘ker¬ nel’,  Lith.  zirnis,  Lett,  zirnis,  ‘pea’,  W.  grown, pi.,  Olr,  gran,  ‘granule’,  fr.  I.-E.  base  *ger(e)-, ‘to  become  ripe,  grow  old’,  whence  also  OI. jarati,  jfryati,  ‘makes  old,  grows  old’,  jaran, ‘old’,  jarimdn-,  ‘old  age’,  jdra/t,  ‘growing  old’.
--- KLN carl/churl ---
6559:carl,  n.,  a  fellow  (Scot.)  —  ON.  kart,  ‘a  man’,  rel. to  OE.  ceorl,  ‘a  man  of  low  degree’.  See  churl and  cp.  Carl,  Charles.
7637:chuprassy,  n.,  a  messenger  wearing  a  badge (Anglo-Ind.)  —  Hind,  chaprasi,  fr.  chapras. ‘badge  plate’,  a  word  of  uncertain  origin.  The usual  derivation  of  chapras  fr.  Pers.  chap-u- rast,  ‘left  and  right’,  is  folk  etymology, church,  n.  —  ME.  chirche,  churche,  fr.  OE.  cirice, cyrice  (whence  ON.  kirkja),  fr.  MGk.  xGptxdv, fr.  Gk.  xuptaxov  (scil.  86S|za),  ‘the  Lord’s  house’. OS.  kirika ,  ON.  kirkia  (Dan.  kirke,  Swed. kyrka),  OFris.  kerke,  MDu.  kerke  (Du.  kerk), OHG.  kirihha,  chirihha  (MHG.,  G.  kirche), ‘church’,  also  derive  fr.  MGk.  xuptxov.  OSlav. cruky  (Russ,  cerkov')  is  prob.  a  Teut.  loan  word. Gk.  xupiaxov  is  prop,  the  neut.  of  the  adjective xuptaxop,  ‘belonging  to  the  Lord’,  fr.  xupto?, ‘lord,  master’,  from  the  adj.  xupioq,  ‘having power,  having  authority’,  fr.  xOpo?,  ‘authority’, which  is  cogn.  with  OI.  sdvirah,  sQrah,  ‘strong, brave,  courageous’,  Avestic  sura-,  sura-,  ‘strong, mighty’,  Gaul.  Kauapo?,  OIr.  caur,  ‘hero’,  Co. caur,  W.  cawr,  ‘giant,  hero’.  These  words  prob. derive  fr.  I.-E.  base  *kew(e)-,  *kewa-,  *kii-,  ‘to swell  out’,  whence  also  Gk.  xueiv,  also  xueiv, ‘to  become  or  be  pregnant’,  L.  cavus,  ‘hollow’. See  cave,  n.,  and  cp.  kirk,  kermess,  ‘fair’.  Cp. also  curiologic,  Cyril,  Kyrie  eleison,  acyrology. Derivatives :  church,  tr.  v.,  church-ing,  n.,  church- ly,  adj.,  church-li-ness,  n.,  church-y,  adj. churchite,  n.,  a  hydrous  cerium  calcium  phos¬ phate  (mineral.)  —  Named  after  the  English chemist  Arthur  H.  Church  (1834-1915).  For  the ending  see  subst.  suff.  -ite. churl,  n.,  1)  a  peasant;  2)  a  boor.  —  ME.  cheorl, cherl,  churl,  fr.  OE.  ceorl,  ‘a  freeman  of  low degree,  man,  husband,  male’,  rel.  to  MLG. kerle,  Du.  kerel,  ‘freeman  of  low  degree’,  G. Kerl,  ‘fellow’,  ON.  karl,  ‘old  man,  man,  servant’ (whence  OE.  carl,  ‘man’),  Norw.  kar,  ‘man’, kail,  ‘an  old  man’,  OHG.  karal,  ‘man,  husband, lover’  [whence  MHG.  karl,  of  s.m.,  and  the ML.  PN.  Carolus,  the  G.  PN.  Karl ;  cp.  also  Lith. karalius,  OSlav.  kralji  (Russ,  korol',  Pol.  krol, Czech  krdl),  ‘king’,  which  go  back  to  Carolus  = Charles  I  (Charlemagne),  king  of  the  Franks]; fr.  I.-E.  base  *ger(e)-,  ‘to  become  ripe,  grow old’,  whence  also  OI.  jarati,  ‘grows  old’,  Gk. vepojv,‘old  man',-fTr.pGa(ic,  y-rprxXioq,  ‘old’,  Goth. kaurn,  OE.  corn,  ‘grain’.  See  corn,  ‘grain’, and  cp.  next  word.  Cp.  also  Carl,  carling, Caroline,  Caroline,  ‘old  woman’,  Carolus,  Char¬ les,  Charles’s  Wain,  housecarl.  Cp.  also  geronto- and  words  there  referred  to.
--- KLN Charles ---
3307:arbor  vitae,  n.,  an  evergreen  tree  of  the  genus Thuja.  —  L„  ‘tree  of  life’;  a  name  given  by  the French  physician  and  botanist  Charles  de  Le- cluse,  latinized  into  Carolus  Clusius  (1525- 1609),  to  trees  of  the  genus  Thuja.  See  arboreal and  vital.
6561:carline,  n.,  an  old  woman  (Scot.)  —  ON.  ker- ling,  fern,  of  karl,  ‘man’.  See  carl  and  cp.  Carl, Charles.  Cp.  also  carting, carline  thistle.  —  F.  carline,  fr.  ML.  carlina,  for cardina.  fr.  L.  carduus,  ‘thistle’.  See  card,  ‘ma¬ chine  for  combing’,  and  cp.  words  there  referred to.  ML.  carlina  was  influenced  in  form  by  Char¬ lemagne  ( Carolus  Magnus),  with  whom  this plant  was  associated  by  legend, cariing,  n.,  one  of  the  timbers  running  length¬ wise  (naut.)  —  F.  carlingue,  fr.  ON.  kerling,  lit. ‘an  old  woman'.  See  carline,  ‘an  old  woman’. Carlovingian,  adj.,Carolingian.—  F.  carlovingien, a  blend  of  carolingicn  and  merovingien.  See Carolingian  and  Merovingian, carmagnole,  n.,  t)  jacket  (worn  by  the  French Revolutionaries  in  1793);  2)  a  revolutionary dance.  —  F.,  fr.  Carmagnola,  name  of  a  dis¬ trict  in  Piedmont,  Italy.  The  word  orig.  denoted a  coat  worn  in  Carmagnola  and  brought  to France  by  workmen  from  Piedmont.
6581:Carol,  masc.  PN.  —  ML.  Carolus.  See  Charles and  cp.  Carl.
6584:Caroline,  adj.,  belonging  to  the  time  of  Charles  I or  II  of  England.  —  Formed  fr.  ML.  Carolus, ‘Charles',  with  suff.  -ine  (representing  L.  -inus). See  Charles  and  cp.  Carol.
6585:Caroline,  fem.  PN.  —  F.,  fr.  It.  Carolina,  orig.  a fem.  adj.  derived  fr.  ML.  Carolus,  ‘Charles’,  and lit.  meaning  ‘of,  or  pertaining  to,  Charles’.  See Caroline,  adj.
```


## [2026-09-05T20:52:01.794Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==365 || NR==366' KLN_1966.txt | grep -nE \"^[0-9]{3}$|[0-9]{3}\" | head -20\necho \"=== raw head of leaf 365 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==365' KLN_1966.txt | head -5\necho \"=== tail ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==365' KLN_1966.txt | tail -5\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-05T20:52:03.885Z] TOOL RESULT

```
6:Gramophone,  n.,  trademark  used  for  a  type  of phonograph.  —  Coined  by  its  inventor  Emile Berliner(i85i-I929)  fr.  Gk.  ypapt(ia,  ‘something written’,  and  96)vfj,  ‘sound,  voice’.  See  -gram and  phone,  ‘speech  sound’,  and  cp.  phonograph, gram-positive,  adj.,  holding  the  purple  dye  when stained  by  Gram's  method;  saidesp.  of  bacteria. —  So  called  after  the  Danish  physician  Hans Christian  Joachim  (1853-1938). grampus,  n.,  a  cetacean  (Grampus  griseus).  —  Fr. earlier  graundepose,  altered — after  grand — fr.  ME.  graspeys,  grapeys,  fr.  OF.  craspeis, graspeis,  lit.  ‘fat  fish’,  fr.  L.  crassum  piscem,  acc. of  crassus  piscis.  See  crass  and  Pisces, granadilla,  n.,  the  fruit  of  certain  kinds  of  passion flower.  —  Sp.,  dimin.  of  granada,  ‘pomegra¬ nate’.  See  pomegranate.
8:674
23:grangerism,  n.,  the  practice  of  grangerizing.  — See  next  word  and  -ism. grangerize,  tr.  v.,  to  illustrate  a  book  by  the  ad¬ dition  of  prints,  engravings,  etc.  —  Lit.  ‘to  il¬ lustrate  a  book  in  the  manner  in  which  James Granger's  ‘Biographical  History  of  England’ (1769)  was  illustrated.
26:675
43:graphite,  n.,  a  form  of  carbon,  black  lead,  plum¬ bago  (mineral.)  —  G.  Graphit,  coined  by  the German  mineralogist  Abraham  Gottlob  Wer¬ ner  (1750-1817)  in  [789  fr.  Gk.  ypc^Eiv,  ‘to write’;  so  called  by  him  because  this  mineral  is used  for  making  pencils.  See  -graph  and  subst. suff.  -ite.
44:Derivatives:  graphite,  tr.  v.,  graphit-ic,  adj. grapho-,  combining  form  meaning  ‘pertaining  to, or  used  for,  writing’,  as  in  graphology.  —  Gk. ypatpo-,  fr.  ypatpeiv,  ‘to  write’.  See  -graph, graphology,  n.,  the  study  of  handwriting.  —  F. graphologie,  coined  by  Abbe  Jean-Hippolyte Michon  (1806-81)  in  1868  fr.  Gk.  yp^E'.v,  ‘to write’,  and  -Xoyti,  fr.  -Xoyo;,  ‘one  who  speaks (in  a  certain  manner);  one  who  deals  (with  a certain  topic)’.  See  grapho-  and  -logy. Derivatives:  grapholog-ic,  grapholog-ic-al,  adjs., grapholog-ist,  n.
46:graphomaniac,  n.,  one  suffering  from  grapho¬ mania.  —  See  prec.  word  and  maniac, graphometer,  n.,  surveyor’s  instrument  for  meas¬ uring  angles.  —  F.  graphometre,  coined  by  the French  engraver  Philippe  Danfrie  (1535-1606) in  1597  fr.  Gk.  ypiLpeiv,  ‘to  write’,  and  piTpov, ‘measure’.  See  grapho-  and  meter,  ‘poetical rhythm’.
48:676
70:677
83:Graves’  disease.  —  Named  after  the  Irish  physi¬ cian  Robert  James  Graves  (1796-1853). graveward,  adv.  and  adj.,  gravewards,  adv.,  to¬ ward  the  grave.  —  Compounded  of  grave  and -ward,  resp.  -wards.
86:gravitate,  intr.  v.  —  ModL.  gravitatus,  pp.  of gravitare,  coined  by  Sir  Isaac  Newton  (1642- 1727)  fr.  L.  gravitas,  ‘weight’.  See  gravity  and verbal  suff.  -ate.
=== raw head of leaf 365 ===
tter’, lit.  ‘that  which  is  written’,  from  the  stem  of ypatpEiv,  ‘to  write’.  See  -graph  and  cp.  gramarye, grammatical.
grammarian,  n.,  a  student  of,  or  an  expert  in, grammar.  —  ME.  gramarien,  fr.  OF.  gramarien (F.  grammairien ),  fr.  OF.  gramaire  (F.  gram¬ maire),  ‘grammar’.  See  prec.  word  and  -ian. grammatical,  adj.  —  L.  grammaticdlis,  fr.  gram- maticus,  ‘pertaining  to  grammar’,  fr.  Gk.  ypajj.- jAotTt xo?,  ‘knowing  one’s  letters;  knowing  gram¬ mar’.  See  grammar.
Derivatives:  grammatically,  adv.,  grammatical¬ ness,  n.
grammaticaster,  n.,  a  petty  grammarian.  —  ME., fr.  L.  grammaticus,  ‘grammarian’,  fr.  gram- maticus,  ‘pertaining  to  grammar'.  See  prec. word  and  -aster.
grammaticize,  tr.  v.,  to  make  grammatical;  intr. v.,  to  discuss  points  of  grammar.  —  See  gram¬ matical  and  -ize. gramme,  n.  —  See  gram.
=== tail ===
676
graphophone,  n.,  an  instrument  for  sound  record¬ ing.  —  Lit.  ‘that  which  writes  the  sounds’ ;  com¬ pounded  of  grapho-  and  Gk.  qicovfj,  ‘sound, voice’.  See  phone,  ‘speech  sound’.
-graphy, combining  form  denoting:  i) processes of  writing,  drawing,  representing,  recording,  as in  phonography ;  2)  names  of  descriptive  scien¬ ces,  as  in  geography.  —  F.  or  G.  -graphie,  fr. L.  -graphia,  fr.  Gk.  -ypacpta,  ‘description  of’, fr.  vpa-peiv,  ‘to  write’.  See  -graph  and  -y  (rep¬ resenting  Gk.  -la),  and  cp.  -graphia. grapnel,  n.,  a  small  hook.  —  ME.  grapenel,  di- min.  formed  fr.  OF.  grapin,  ‘hook’.  See  grape. Derivative :  grapnel,  tr.  v. grapple,  n.,  grappling  iron,  grapnel.  —  OF.  *gra - pelle,  dimin.  of  grape,  ‘hook’.  See  grape  and  cp. prec.  word.
Derivatives:  grapple,  tr.  and  intr.  v.,  grappl-er, n.,  grappl-ing,  n.
grapsoid,  adj.,  pertaining  
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
```


## [2026-09-05T20:52:12.118Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==365' KLN_1966.txt | grep -n \"^6[0-9][0-9]$\\|granite,  n\\.  —  F\\.\\|grain,  n\\.,  seed\" "
}
```


### [2026-09-05T20:52:13.813Z] TOOL RESULT

```
8:674
25:graniferous,  adj.,  producing  grain.  —  Formed with  suff.  -ous  fr.  L.  granifer,  ‘grain-bearing’,  fr. granum,  ‘grain’,  and  the  stem  of  ferre,  ‘to  bear, carry’.  See  grain,  ‘seed,  com’,  and  -ferous. granilla,  n.,  the  refuse  of  cochineal.  —  Sp.,  di¬ min.  of  grana,  ‘cochineal’,  rel.  to  grano,  ‘grain’, fr.  L.  granum.  See  grain,  ‘seed,  com’, granite,  n.  —  F.,  fr.  It.  granito,  lit.  ‘grainy’,  pp. of  granire,  ‘to  make  grainy’,  fr.  grano,  ‘grain’.
26:675
48:676
```


## [2026-09-05T20:52:20.547Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 leaf 468 (p.1011) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==469' BQT_v2_pages.txt | head -40"
}
```


### [2026-09-05T20:52:22.217Z] TOOL RESULT

```
=== BQT v2 leaf 468 (p.1011) ===
                                                 ‫بیان سوم‬
                     ‫در زای نقطه دار باجیم مشتمل بر چپار لغت‬

                     ‫عنکبوت را گویند ‪۱‬‬       ‫مال‬        ‫* رج ‪ -‬بضم اووسلکون انی » تیر‬
                                                                        ‫پرتاب‌باشدکه پیکانآ براازاستخوان‬
‫رجمول ‪ -‬با میم بر وزن معقول ‪.‬‬
                                                                        ‫فیل وشاخ‌قوج کواومیش وامثال آن‬
‫حبی امت دوابی و آلرا بفارسی یخم کشوث‬
                                                                        ‫مازید ‪ _ ۱‬و کوتاه ثرین نیرها را‬
‫خواند ‪ .‬طبیمت آن معتدل امت در گرمی‬
                                                                        ‫و بمعنی چیزی باشد‬           ‫نکیوزبند ‏‬
                                         ‫‪۰‬‬   ‫وسردی‬
                                                                         ‫کهآ راازدوغ ترش سازند وبتر کی‬
 ‫زجه ‪ = ۴‬بفتح‌اول وثانی» زلی گروابند‬                                      ‫قراقروت خوانند؟ ؛ وباجیم فارسی‬
‫که زاییده (‪ )۱‬باشد و او را تا چهل روز زجه‬                                    ‫یز همه معانی آمده است ‪.‬‬
‫میتوان گفت ‪ :‬وباجیم فارسی‌هم درست امت ‪.۶٩‬‏‬                               ‫بفتح‌اول بروزن‬        ‫رجال‬


                                              ‫يان چهارم‬

          ‫کتنوات‬
               ‫دزرای نقطه دار با خای نقطه دار مشتمل بر هفت لغ‬
‫و اسب را بهم میرسد و آنرا ازخ فيز گونند‬                  ‫رخ = بفتح اول و سکون ثالی‪ ۰‬آواز‬
‫ولالةٌ حزین راگویند؟ ‪ -‬وبانگ وصدای زنگه | و بعربی تژلول خوانند © ‪ -‬و مخفف زخم هم‬
                                             ‫تن ‪۱‬‬        ‫و جرس را همگفته‌اند ‪ - ۴‬و فرو بردن چیزی‬
‫بر وزن شراره » شاخ‬            ‫رخاره ‪= ۲‬‬                  ‫باشد بزور وعنف درمة‌اك ‪ -‬وعلتی باشد کهآ دمی‬

                                                                          ‫(‪ )۱‬چسش ‪ ۲ :‬شده ‪.‬‬

  ‫‏‪( - ٩‬عر) زح (بضم اول وتشدید دوم) «نیزی آرنج » آهن بن لیزه وپیکان تیر ‪ .‬زجاح‬
  ‫‪_ ۴‬طبری سرج (کشك سیاء [قرقوروت] )» مازندرانی‬                          ‫وزججه ‏‪ ٠‬جمم» «منتهی الارب؟ ‪.‬‬
                             ‫رك ‪ :‬زاح » زادن ۔‬   ‫‪- ۴‬‬            ‫‪.‬‬   ‫‪۸۲4‬‬     ‫کتوی زهك ‪ « 15» .‬واژه نامه‬

         ‫رك‪ :‬زخم ‪.‬‬   ‫‪-‬‬   ‫‪۱‬‬           ‫ازخ ‪ ۰‬آزخ » ژخ ‪.‬‬       ‫_رك‪:‬‬    ‫‪۵‬‬         ‫‪.‬‬   ‫ژخار‬    ‫رك‬    ‫‪۴‬‬


                                              ‫‪-‬ك‪ :‬زخناره » ازغ » اژغ » آزغ ‪ 7‬آژغ ‪.‬‬
                                                                                 ‫‪ ۷‬ر‬
                                                       ‫تتفرقة پابان کتاب ‪.‬‬
                                                                         ‫لمخا‬            ‫‪:‬‬
```


## [2026-09-05T20:52:29.888Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"زرتشت\" \"زردشت\" \"زروان\" \"زال\" \"ارزن\"; do echo \"=== $w ===\"; awk -v w=\"$w\" 'BEGIN{RS=\"\\f\"} index($0,w){print \"LEAF \" NR}' BQT_v2_pages.txt | head -20; done"
}
```


### [2026-09-05T20:52:31.648Z] TOOL RESULT

```
=== زرتشت ===
LEAF 14
LEAF 135
LEAF 191
LEAF 238
LEAF 249
LEAF 329
LEAF 355
LEAF 378
LEAF 390
LEAF 404
LEAF 411
LEAF 459
LEAF 475
LEAF 476
LEAF 481
LEAF 500
LEAF 596
LEAF 667
LEAF 676
=== زردشت ===
LEAF 12
LEAF 249
LEAF 324
LEAF 356
LEAF 370
LEAF 374
LEAF 458
LEAF 459
LEAF 460
LEAF 472
LEAF 473
LEAF 474
LEAF 475
LEAF 476
LEAF 481
LEAF 482
LEAF 494
LEAF 499
LEAF 500
LEAF 501
=== زروان ===
LEAF 204
LEAF 302
LEAF 473
LEAF 474
LEAF 478
LEAF 480
LEAF 481
LEAF 482
LEAF 517
=== زال ===
LEAF 5
LEAF 9
LEAF 62
LEAF 75
LEAF 108
LEAF 125
LEAF 151
LEAF 175
LEAF 188
LEAF 210
LEAF 221
LEAF 227
LEAF 232
LEAF 237
LEAF 262
LEAF 267
LEAF 277
LEAF 278
LEAF 318
LEAF 332
=== ارزن ===
LEAF 34
LEAF 53
LEAF 94
LEAF 186
LEAF 282
LEAF 296
LEAF 485
LEAF 522
LEAF 523
LEAF 535
LEAF 552
LEAF 580
LEAF 586
LEAF 617
LEAF 639
LEAF 644
```


## [2026-09-05T20:52:35.658Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 473 474 475; do echo \"########## LEAF $((n-1)) (printed ~$((n-1+543))) ##########\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt; done 2>/dev/null | head -160"
}
```


### [2026-09-05T20:52:37.417Z] TOOL RESULT

```
########## LEAF 472 (printed ~1015) ##########
    ‫—‬        ‫)‪0‬‬
                                                                                                                       ‫زراوه‬

 ‫ونفس ناطفه ‪ -‬و عقل فلك عطارد ‪ -‬ونورمجرد‪-‬‬                                 ‫تام خوای ابت که آن دونوع میباشد ‪ :‬یکی‬
        ‫وعفل فعال ‪ -‬ورب‌النوع انان وراست کوی‬
                                                                          ‫را زراوند طوبل میگوبند یمتی‌دراز وآترا شجرة‬
‫رالیز گوبن دکه‬               ‫ورردشت‬              ‫و لور ردان باشف ‪۷‬‬        ‫رستم و قتاءالحیه میخوانند » وآن نر باشد و از‬
                      ‫یشرو ویشوایا شس برستان است ‪.‬‬                         ‫انگشت بر گنده‌تر »گرم است در سیمو خشك‬
 ‫زر لك س با ای قرشت بر وزن‬                                                ‫است دردویم ؛ ودیگربرا زراوند مدحرج خوانند‬
‫کل کاو شه‬               ‫وخق‬      ‫باشف ‪۰‬‬          ‫خق‬     ‫آب‬   ‫که ‪۰‬‬   ‫زرد‬
                                                                           ‫است‬     ‫روف‬
                                                                                     ‫عو‬‫مشد‬
                                                                                         ‫بعتی هدور ؛ وآن ماده ای ما‬
                                                                           ‫»آن‬
                                                                             ‫مشامی(‪ .)۱‬بهترین‌آن زرد زعفرانی باشد و‬
                                                       ‫را لیز گفته‌اند‪.‬‬           ‫ودیرم و خشك است درسیم ‪.‬‬
                                                                                                        ‫کرم ادست‬
‫«کر انی فووقانی و لام‬
                    ‫رترلی؟ ب‬                                               ‫زاروه = بروزن کجاوه ‪ .‬پهلوالی است‬
                        ‫‪٠‬‏ زر طلا را گونند ‪۰‬‬            ‫بحتالی رصیده‬


 ‫زرر = بفتح اول وکسر انی و سکون‬
                                                                                       ‫گوبند وبعربی بحر خوانند ‪.‬‬
 ‫‪,‬بك راگوبند و آن پرنده ایت‬
                          ‫جیم فارسی ك‬
                                                                          ‫زراه ‪| ۲‬کفوده ؟ ‪ .‬بفتح همزه‬
 ‫ابی‌و آن دوقم میباشد‪ :‬دری و غیر دری ؟‬
                                                                           ‫وسکون‌کاف وضم فا پروزن افزوده » دربای خزر‬
                   ‫و دری بزر کت از غبر دری میشود ‪.‬‬
                                                                          ‫اکفوده نامآن در با است همحر دربای‬           ‫باشف جه‬

 ‫در جامی »با جیم بر وزن بدنامی‪,‬‬                                                             ‫عمان ودربای فازم وامثال آن ‪۰‬‬

                                         ‫لومی از انگور باشد ‪.‬‬              ‫دکر !ول و الك و سکون‬
                                                                                              ‫زرا لو ب‬
 ‫زجرعفری « بکرنانی» طلای‌خالس‬                                             ‫وبوند را‬
                                                                                 ‫راب‬
                                                                                   ‫حتوانی مجهول وواو » نق‬
                                                                                                        ‫تنی‬
                                                                                                          ‫ثا‬
‫‪:‬‬           ‫پودمنسوب سعفر نامی کهکیمیا کر بوده اڪ‬                                                    ‫گوگ ‪.‬‬
 ‫وبعضی گوبند پیش ازجعفر برمکی زرقلب سکه‬                                   ‫را‬   ‫لب بروزن‌در بان» پیرسالشورده‬   ‫رربان‬

‫او وزير شد حکم فرمود که‬                                ‫میکردند چون‬        ‫گویند؟ ‪-‬ونام‌حضرت ابراهیمعله‌اللام‌است ‪۵‬؛‬
    ‫طلا را خالص کردند و سکه زدند و باو منسوپ‬                              ‫و باين معتی بجای بای ابجد فای سعقص و میم‬
                                                                    ‫قرف‬            ‫نیز آمده است که زرفان وزرمان باشد ‪۰‬‬
                                                                           ‫زر شت ‪٩‬‏ ‪ -‬بشم تای قرشت بوزرن‬
 ‫قطه‌دار وسکون شن وکاف » طلای خالص بی‌غل‬                                   ‫و نفس کل ‪-‬‬      ‫وبمعنی آفربدة اول ‪-‬‬    ‫‪۰‬‬    ‫ازنگشت‬


                                                                                            ‫(‪ )۱‬چش ‪ :‬بشاحی ‪.‬‬

             ‫اوستابی ‪2122‬‬                ‫‪۴‬‬                    ‫‪( 62100101510=2 ۱‬فر) « لك ‪ ۷‬ص ‪. » ۳۰۲‬‬
        ‫‪.‬‬    ‫‪ :‬اکفوده‬       ‫رك‬   ‫‪۴‬‬                     ‫(دربا) " پپلوی ‪ , 872‬بلوچی ‪ « 2۳12‬اسشق ‪۱٩۵‬‏ > ورك ‪ :‬درما ‪.‬‬
     ‫برائر وفق دادن نابجا‬                    ‫‪۴‬‬               ‫وك ‪ :‬زر » زال ‪۰‬‬
                                                                           ‫‪ - ۴‬مصحف «زرمان » (ه‪.‬م‪ ).‬ر‬
    ‫و تخلیط افکارابرالی بامعتقدات واساطیر سامی «زروان» ( که بهزر مان‌وزر بان صحصف شده) باابر اهیم‬

        ‫‪.‬‬      ‫زارت‬     ‫‪.‬‬    ‫زردشت‬   ‫‪:‬‬   ‫رك‬        ‫‪-‬‬   ‫‪۱‬‬            ‫‪. ۶۱۱‬‬
                                                                        ‫‪:‬زدستا ص ‪- ۳۱۱‬‬
                                                                                     ‫یپکنیداشته شده ‪ .‬رلا م‬
            ‫رکه ‪ :‬زرد کت » زرده‪.‬‬                 ‫‪۸‬‬               ‫ليه این معالی محمول است‪ .‬رك ‪ :‬زردشت‪.‬‬         ‫‪۷‬‬

                                                             ‫‏‪ ٩‬صحیح زر طلی وزر طلا است ‪ .‬ر کت‪ :‬زر طلی‪.‬‬

########## LEAF 473 (printed ~1016) ##########
       ‫زردشت‬                                                                        ‫‪۱‬‬

                            ‫ابتاده عبادت کرد ‪۰.‬‬                             ‫وغش راکونند ‪#. ۱‬‬
  ‫زرد خی بفتح اول وخای نقطه‌دار بر‬                ‫ازرداب ‪ - ۲‬بارالابجدبروزن غرقاب»‬
  ‫وزن مردرو » دام کیاعی است که بشتر در باغات‬      ‫نخالمطی است که بعربی صفرا کوبند ‪ -‬و آبی‬
                ‫روید و کلی زرد وخوشبوی دارد ‪.‬‬     ‫ککهااجزکیلره بوقت شستن آن برمی‌آید =‬
  ‫ررد رخ کنابه از شرمنده و متفعل‬                      ‫کوتایه ازشراب زعفرانی رنگه هم عدت ‪.‬‬
      ‫یه تارزسنده وترسناك همهست ‪.‬‬
                                ‫او‬‫کشدن ‪-‬‬
                                       ‫با‬         ‫ررذاب رهز ‪-‬کنابه ازخرن ریختن‬
  ‫زرد ساٹ مھ بکسرثالت وسین یی‌نقطه‬                ‫باشد ‪ -‬و کنابه ازغصه کردن وبدخویی لمودن ‪-‬‬
       ‫یی باآشدنکرها‬
                   ‫ا»‬‫لال‬
                       ‫طحد‬
                         ‫بالف کشیده و فت‬          ‫ودل‌خالی کردن از فهرونغضب هم‌هست‪ -‬وشخصی‬
                       ‫باشند‪۰‬‬   ‫لو ازکان وره‬
                                                          ‫که بدخوبی وقهر و غضب ونصه کند ‪.‬‬
      ‫د طلای دست‬       ‫افثار‬    ‫رردست‬
  ‫افشار مشهور است که خسرو پرویز داشت ومانتد‬
                                                  ‫زردان ‪ ۴‬بروزن مردان ‪ .‬یکی از‬
                                                   ‫اکابر مجوس امت واهل‌او را زردانیه ‪ ۴‬گوننده‬
      ‫موم ارم میشد و هرصورتی که از آن میخواست‬     ‫ئت که بزدان اشضاص مار از‬     ‫واعتقاد اشان آ‬
      ‫بان رنه‬    ‫را‬
                  ‫تمل‬
                    ‫آل ع‬
                       ‫گوشد اه‬  ‫می‌اخت ‪.‬‬          ‫روحالبات احداث نموده است و زردان ‪ ۴‬اعظم‬
                         ‫رسانیده بودند ‪. ۷۱‬‬
                                                  ‫بزر کترین روحالیات است و اهرمن افزکر او‬
 ‫زدرشت ‪ = ۲‬نم دالابجد» شخصیکه‬                     ‫بهم رسید و زردان له هزار ولهسد ولود وله‌سال‬

                  ‫صندوق عثیر » بخروار مشك ‪.‬‬         ‫‪ - ۱‬برون از طبقهای پر زر خشك‬
       ‫نظامی کنجوی « کنجته ‪. ۸۷‬‬
                                                  ‫از‪ :‬زرد( آب (آب زردرنگه)‪.‬‬         ‫‪۴‬‬
‫خیم‬                                                     ‫«زروان» (ھ (‪.e‬‏ ‪۰‬‬   ‫مصحف‬    ‫‪۳‬‬
                                                           ‫مصحف « زروالبه > ‪.‬‬       ‫‪۴‬‬
                                                            ‫آفشارده ‏‬   ‫فعميي دست‬   ‫®‬

                   ‫‪۶‬‬                              ‫‪ _ ۱‬رك‪:‬زرمشت افشار » مشت افشار ‪:‬‬
                                                                 ‫ملك را زر دست افشار درمشت‬
                                                    ‫کز افشردن‌برونمبشد زادگشت‪.‬‬
                                                   ‫نظامی کنجوی « گنچینه ‪. ۸۷‬‬
                                                  ‫یین اران پاستان در‬
                                                                   ‫‪ ۲‬ام مآوس‬
                                                  ‫فارسی صورت‌های زردشت » زرنشت» زردهشت ‪۰‬‬
                                                  ‫زراتشت‪ .‬زارتشت» زره‌تشت؛ زاردهشت» زاردشت»‬
                                                  ‫زارتهشت ‪ ,‬زارهوشت ‪ .‬زرادشت ‪ ,‬زراهشت‬
                                                  ‫رزمدشت‪ 0 .‬ردخ ‪١‬آم‏د و همول تر از همه‬
                                                  ‫زردشت و زرنشت است ‪.‬این نام درکانها صورت‬
                                                  ‫‏_‪. Zat busbtra‬هدشداب وزجرد مود ارتشا‬
                                                  ‫(بمعنی شتر) اختلافی نیست‌ولی در وجه اشتقاق‬
                                                  ‫جزو اول‌سخن بيار رفته‪ .‬باحةمال قوی بمعنی‬
                                                   ‫زرد است [ رك ‪ :‬زرد او جمعاً پممنی دارنده‬
                                                    ‫بقیه دصرفحة ‪۱۰۲۱‬‬

########## LEAF 474 (printed ~1017) ##########
 ‫ات‬                                                                                     ‫زردشت‬

‫زردشت بز رگ ‪ -‬بازن‌پهلوی دام‬                     ‫دين تش برستی رایهم رالد واحوال او درلغت‬
                                                 ‫زارتشت ييتهفصب لهذ کورشد‪ .‬وبعضی گویند رردشت‬


                           ‫بزبان سربانی ‪*. ۴‬‬     ‫بزبان سریانی نام‌ابراهیم علیه‌اللام است وبعضی‬
‫رردك ‪ = ۴‬بفتح اول وثالث وسکون‬                    ‫ویرزین هر دو امامان‬   ‫دیگر گویند که زردشت‬
‫وآلراکزر فز گونه‬      ‫اس‬   ‫ثالی وکاف ‪ ۰‬معروف‬                             ‫‪.‬‬   ‫ملت ابراهیم بودندا‬




  ‫‪ - ۴‬بمناست تعدد ام زرتشت در ابران باستان » زرتشت‬            ‫‪ ۱‬رك ‪ :‬زارتعت ‪.‬‬
  ‫وخشور ابران باستان را« زرتشت بزر گك » نامیده اند از جملهٌ کان دیگر که این نامرا داشتند‬
 ‫زرنشت پر آذرباد مهرسیندان است که در عصر ساسالی موبدان موبد بوده * اما طبیق زرتشت با‬
  ‫بسنا ص‪ ۳۸‬سعف‪.‬‬
              ‫دز‬‫ابراهیم براثر تخلیطی است که در روابات ایجاد شده ‪ .‬رك‪ :‬زارنشت وکرک‪ :‬م‬
  ‫‪ - ۴‬چنانکه درح ‪۲‬صفحهٌ قگبفلته شد بی‌شك زرتشت (اوستا؛زرئوشتره) ایرالی است ‪.‬‬
               ‫پهلوی )‪ ( 3(۲42‬زرد نخم مرغ )< لیر کک ‪ = » 4۵۷‬زرده ‪.‬‬                  ‫‪۴‬‬
  ‫‪ #‬زدرشتی ‪ -‬بفتح اول وضم سوم ‪.‬از ‪ :‬زردشت ‪ ۳‬ی ( نسبت) ؛ منوب بزردشت» بدرو‬
                                                               ‫‪:‬‬   ‫زردشت »‪ ۰‬دارای آين رردشت‬
        ‫کنون که لاله برافروخت آتش‌لمرود‪.‬‬                  ‫اخ تازه کن آبین دين زردشتی‬
  ‫‪ ۵‬حافظ شرازی ‪44۱٩‬‏ ‪.‬‬
  ‫تن زردشتی در ابران ( بخش اعظم آنان در بزد وکرمان ) و حدود‬            ‫اکتون ‪۰۶‬‬
  ‫تن در هندوستان و ا کان کی دارند ‪ .‬رك‪ :‬پور داود ‪ .‬ایرانشاه » از انتشارات‌انسمن‬           ‫‪۰‬‬
  ‫زرنشتیان بمیی ‪ ۵۲۹۱ .‬؛ مزدبسنا ص ‪ ۸۱ - ۲۱‬؛ تاریخچه‌زردشتیان ابران بقلم ابرح افشار ‪.‬‬
                                    ‫اطلاعات ماعانه سال سوم ( ‪ ) ۹۲۳۱‬شمار؛ ‪ ۸‬ص ‪٩۱‬‏ ببعث ‪.‬‬

                                                                             ‫یه از صفحهٌ ‪۱۱۰۱‬‬
  ‫شتر زرد‪ .‬نام خانوادکی او سینمه ‪20120109-‬است که در بهلوی سییتمان با سینتهان شده ‪ .‬در‬
  ‫زادگاه او اختلاف است‪ .‬برخی وبرا از آتربایکان وبرخی از ری و غالباً از شمال شرقی ابران‬
   ‫داند ‪ .‬در باب زمان او نیز سخن‌ای بار گفته شده ‪ .‬سنت زرتشتان زمان اورا در حدود ‪۰۰4‬‬
         ‫ق ‪ .‬م‪ .‬تین میکند و غالب خاور شناسان همین تاریخرا باجزلی تفاوت پذیرفته‌الد کر‬
   ‫ووهدبگر‬
   ‫پورشپ (ه‪.‬م‪ ( .‬ومادر اودغدو‬     ‫زمان اورا در هزار دوم دش از میااد قرار داده‌اند ‪ .‬بدر زردشت‬
```


## [2026-09-05T20:53:16.963Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=466 && NR<=478 {printf \"LEAF %d: \", NR-1; n=0; if (match($0,/بقیه[^\\n]{0,60}/)) print substr($0,RSTART,RLENGTH); else print \"(no continuation note)\"}' BQT_v2_pages.txt\necho \"=== leaf 470,471 heads ===\"\nfor n in 470 471 472; do echo \"--- leaf $((n-1)) ---\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -12; done"
}
```


### [2026-09-05T20:53:18.507Z] TOOL RESULT

```
LEAF 465: (no continuation note)
LEAF 466: (no continuation note)
LEAF 467: (no continuation note)
LEAF 468: (no continuation note)
LEAF 469: (no continuation note)
LEAF 470: (no continuation note)
LEAF 471: (no continuation note)
LEAF 472: (no continuation note)
LEAF 473: بقیه دصرفحة ‪۱۰۲۱‬‬
LEAF 474: (no continuation note)
LEAF 475: (no continuation note)
LEAF 476: (no continuation note)
LEAF 477: (no continuation note)
=== leaf 470,471 heads ===
--- leaf 469 ---
 ‫زدن‬                                                                                ‫و ‪—| ۵ ۵‬‬




‫چویکی باشد که سنادزهابدان سازنوازند ویعربی‬                                  ‫درخت رگاوند ‪۶.‬‬
                              ‫مراب خوانند ‪.‬‬      ‫زخم بریان س بمعنی دم پفت است‪.‬‬
‫رخناره ‪ = ۴‬بانون پروزن انگاره »‬                                      ‫‪۱‬‬   ‫وآن طعامی باشد معروف‬

      ‫بمعنی زخاره است که شاخ درخت باشد ‪۰‬‬         ‫زخم ناخ د بمنی باناخن رش‬
                                                 ‫ونابه از رفوم منجمان هم‌هت‪.‬‬
                                                                           ‫کردن باشد ک‬
--- leaf 470 ---
‫—‬        ‫‪۵۵‬‬
                                                                                                      ‫زدوار‬

‫ردو نتن ‪» ۴‬با نون و تای قرشت مر‬                          ‫وجماغ باشد‪ -.‬و چون مرکب شود معنی بیار‬
‫وزن سبوشکن » بلغت زند و یازند (‪ )۱‬بمعنی‬                                                       ‫اهل‬         ‫دارو‬
                                       ‫خریدن باشث ‪.‬‬
                                                          ‫= بر وزن ومعنی‌جدواراست‬         ‫ردوار‪۱‬‬
‫زده ‪ - ۴‬بنتح‌اول وثالی» بمعنی خورده‬                                                  ‫که ماه پروین باشد ‪.‬‬
‫بداتکه ازچیزی خوردن است‪ -‬وآراسته ومزین‬
‫وزینت داده را هم‌میگویند‪ -‬وپبراسته وبربدرا‬                ‫ردودن ‌ ت بکراول بروزن‌فزودن»‬
‫نیز کوبند که از قطم کردن باشد ‪-‬‬
                                                          ‫بمعنیازالهکردن وبالساختن باشدعموماً چنانکه‬
--- leaf 471 ---
 ‫زراوند‬                                                                                                       ‫ت‬
                                                                                                              ‫اهن ‪۵‬‬‫‪-‬‬



          ‫و نام مبارزی از اران بوده ‪.‬‬            ‫نود ‪7‬‬        ‫رراتشت ‪ ۱‬س نم فوفالی ‪ ۰‬زردشت‬
‫رراعش؟ = باغین قطه‌دار(‪ )۲‬بروان‬                              ‫راکوبند ‪ .‬وکیشآتش پرستی را او بهم‌رسانید؛‬
‫را‬   ‫زمین سخت‬    ‫و‬    ‫ياك‬       ‫زمین ریگ‬    ‫جفا کش ‪۰‬‬                                            ‫وتاب زند را اوآورد ‪.‬‬
                                                                                                                   ‫ک‬
                                             ‫گویند ‪.‬‬         ‫رراج = بروزن رواج ‪ ,‬زرشك باشد »‬
‫رداعی *ه بروزن فلاخن» جت نگلورا‬                              ‫زیست که در آشپا و طعامپا کنند‬
                                                                                         ‫چیآن‬
```


## [2026-09-05T20:53:49.937Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 leaves around 246 for آزرم ===\"\nfor w in \"آزرمیدخت\" \"آزرمی دخت\" \"آزرم\"; do echo \"--- $w ---\"; awk -v w=\"$w\" 'BEGIN{RS=\"\\f\"} index($0,w){print \"LEAF \" NR-1}' BQT_v1_pages.txt | head -10; done"
}
```


## [2026-09-05T20:53:51.243Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON grep گرانیت ===\"; grep -n \"گرانیت\" MON_part1.txt MON_part2.txt | head -5\necho \"=== MON grep ارزن ===\"; grep -c \"ارزن\" MON_part1.txt MON_part2.txt"
}
```


### [2026-09-05T20:53:51.642Z] TOOL RESULT

```
=== BQT v1 leaves around 246 for آزرم ===
--- آزرمیدخت ---
LEAF 137
LEAF 246
LEAF 326
LEAF 652
--- آزرمی دخت ---
--- آزرم ---
LEAF 67
LEAF 137
LEAF 246
LEAF 247
LEAF 326
LEAF 555
LEAF 652
```


### [2026-09-05T20:53:51.702Z] TOOL RESULT

```
=== MON grep گرانیت ===
MON_part2.txt:16775:شکل یافتن سنگ‌های آذرین گرانیتی یا 
MON_part2.txt:70392:می‌شود. البته برخی از گرانیت‌ها هم ممکن 
MON_part1.txt:54747:گرانیت. نوعی از بافتةٌ ابریشمی که مانند 
=== MON grep ارزن ===
MON_part2.txt:18
MON_part1.txt:27
```


## [2026-09-05T20:53:56.887Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 leaf 246 (printed ~36) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==247' BQT_v1_pages.txt | head -60"
}
```


### [2026-09-05T20:53:58.658Z] TOOL RESULT

```
=== BQT v1 leaf 246 (printed ~36) ===
آزدن
رذن . بازای فارسی » بروزن و معنی
آزدن بلشد که خلانیدن سوزن وامشالآنست .-
و استره زنب واژنه وگ اشفا زدن نزدمك
سکدیگر را کوبند .
]رده بروزن آمدم .یمعئی رنگهکرده
و خلانیدم شده بلشد » اعم از سوزن وغیره .
3 بازای‌ظرسی, بروزننو ععنی‌دوم
آزده است که خلانیده شده و اجده ده شده
باشی اعم ا ]که باسوزن با چبزی یگ اد
1رد یتح لت و وزن سور ز سغنت
آزار است - وامر بآزردن وآزار دادن هم هست-
و ومعنی کج طبع نیز آمده است - ودر عربی‌نام
آیرا اهیم علبه‌اللام است‌چه بدراین هي علیه‌اللام
۰ ترح » تلم داشته است لیکن سد ازفوت تار ی
آزر اورا پرورده است ۷ .
زر واه ۴ هه یابایایجد بروزن‌مادرزاد
تلم بسر عاراسیند است و او موبدی موده از اولاد
ژردشت معاصراردشیر بایکان ودر آن زمان‌حکیمی
مانتد او نبوده است گر اردای بر وبرانی ۳
که اعلم از او بوده است -
]ررخش ۴ س بر وزن تاج بخش ۰
شورش و صاعقه را گوند عتی. سرما ورعدوبرة
رده س بقتح ثاث وسکون رابع وداا.
ایجد » بمعنی رنگ» ولون باشد .
۲ رده پشت «کنابه از پ رکوژیشت
باشد - و چاروایی را نیز گوبند که پشت او ز انم
و جراحت شده باشد .
آ دم * - پتح ثاك و سکون دابع
و حیم» چند معنی دارد : ۱-.حیا" و شوم باشد .
۲ - بزرگی و عزت و حرمت را کوند . ۳ .
تاب و طاقت بود . ۶ب رحم وشفقت ومپروححبت
و نرمی ومردمی وآدمت. 4- غم واندوه وتشگی
وسختی‌والم را گویند. -٩‏ عدل واتصاف و یکدلی
باشد. ۷- طاهر و آشکارا را گویند . ه سلاحتی
وراحت بود ۰ - نگاهداشت وباس خاطر وتحمل
یائد. *۱ - غب و قهر ر خشم را گویند .
۱- بخواری و زاری گذاشتن باشد. ۷۲- تقصیی
و گذاه را کویند. ۱۳ - بمعنی حسامان شدن‌باشد.
6 - دام دختر خسرو پروم است ۰۸ واو چهار
ماه پادشاهی کرد .
]زر میداخت ۰۷ بکی مم و خم
دال , نام دخترخسرو پرویز است ؛ و آوچپازساه
و ببعنی گوبند شش‌عاه پادشاهی کرد- ونام شهری
هم‌هت که او بنا کرده است .
هيچيك از مدارد قدیمه اسن نام برای پدر ابراهیم نیامده و نام حقیقی او تارح با تارج است .
قرتکل126061] بدلابلی«عازر» و«آزرگرا ماود ازکلمه عبری ج و و(
دانته گوید آن تام‌خادم وفادار ابراهیم بود *جفری ۵۴ - ۵*
و رگ : * داش‌قائمعارف ابلام » و او به بت گرویت نراش معروف است : منت جاهلان است که
چون بدلیل از خس قرو مانند سلسلهٌ خصومت جنبانند چون آزر بت تراش‌ که . ۰۰« کلستان »
۶ لت نزمه * . ۴ صحیم آذرباد است . ره : آذرباد . ۴ - ره :
اردا وبراف. ۴ - تحرف «آترخش». . ۵ -بهپلوی222۳۳70 «منای ..»۲۹4‏ * - مراد
ِ صسلددوات است که اعتاهاً آنرا یر ۳ از آزرم ۱ آزرءنبخت ( داستهاند ۵ ره 4 آزرمیدخت.
۴- ۰ آژرمی ۲+ دخت . ج. اول در اوستا 8۰22۳6702 که خود مرکب است
از 2 علامت نی و 22۲6002 حم رد 2211۳102 و 2217188 که هر دو صفت است بمعنی
قرغوت و شکته و 281801 در سانسکریت 2۲201[ بپمن معنی است , 22117۷2 بمعنی پیری
بقه در صفحاٌ ۳۷
```


## [2026-09-05T20:54:09.862Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));m=d['MON'];print(m.get('page_offset'));print(m.get('notes'));print(m.get('local_files'))\"\necho \"---\"\nsed -n '54740,54755p' MON_part1.txt"
}
```


### [2026-09-05T20:54:11.628Z] TOOL RESULT

```
None
covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).
None
---
ضارا: ۱:25- خاره - خار] (.) (زم.) 
سنگی است از دستةً سنگ‌های آذرین 
دنت گنه خود دسته مشخصی رابنام 
سنگ‌های خارایی تشکیل می‌دهد سنگی 
است سخت و مرکب از بلورهای اصلی 
کوارتز» فلدسپات و میکا که به رنگ‌های 
خاکستری و پشت گلی و سبز دیده می‌شود؛ 
گرانیت. نوعی از بافتةٌ ابریشمی که مانند 
صسوف موجدار است و مخطط ؛ عتانی. 
رد بفته‌ای اسر 
خاراندن: 22۲ [ - خارانمدن] (مص م. 
ل: خارنیدن) (خاراند» خاراند» خواهد 
خاراند» بخاران» خاراننده» خارانیده) با سر 
ناخن روی وست بدن (خود یا دیگری) 
کشدن» خارش دادن.
```


## [2026-09-05T20:54:21.347Z] TOOL CALL #33: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py && echo \"=== verify_check ===\" && sed -n '1,60p' tools/verify_check.py"
}
```


### [2026-09-05T20:54:21.402Z] TOOL RESULT

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
=== verify_check ===
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
```


## [2026-09-05T20:54:23.080Z] AGENT

Now let me gather web sources.


## [2026-09-05T20:54:27.611Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5erh%E2%82%82-\" \\\n \"https://en.wiktionary.org/wiki/granite\" \\\n \"https://www.etymonline.com/word/granite\" \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D8%A7%D9%84\" \\\n \"https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D8%B1%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%B2%D9%86\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 174, root Ger 2/Greno\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-05T20:54:32.514Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6fad9586c75ec61e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/adb0785739a84a64.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/013e05c07e6ba085.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1bdf06fd715c0de3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/535f8a29227c4e5d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6178e070fb4b681c.txt
```


## [2026-09-05T20:54:35.419Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"############ PIE ǵerh₂- ############\"; grep -n -A4 -i \"Proto-Indo-European\\|Root\\|Derived terms\" 6fad9586c75ec61e.txt | head -60"
}
```


### [2026-09-05T20:54:35.485Z] TOOL RESULT

```
############ PIE ǵerh₂- ############
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5erh%E2%82%82-
2-FETCHED: 2026-09-05T20:54:30Z
3-STATUS: 200
4:TITLE: Reconstruction:Proto-Indo-European/ǵerh₂- - Wiktionary, the free dictionary
5-
6:Reconstruction:Proto-Indo-European/ǵerh₂- - Wiktionary, the free dictionary 
7-
8- Jump to content 
9-
10- Main menu 
--
57: Proto-Indo-European 
58-
59: Toggle Proto-Indo-European subsection 
60-
61- 1.1 
62: Root 
63-
64- 1.1.1 
65: Derived terms 
66-
67- 1.1.2 
68- Descendants 
69-
--
78: Reconstruction:Proto-Indo-European/ ǵerh₂- 
79-
80- Add languages 
81-
82- Reconstruction 
--
132: See also: Reconstruction:Proto-Indo-European/gerh₂- 
133-
134: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
135-
136: Proto-Indo-European
137- [ edit ] 
138-
139: Root
140- [ edit ] 
141-
142- *ǵerh₂- [ 1 ] [ 2 ] 
143-
--
146: Derived terms
147- [ edit ] 
148-
149: Terms derived from the Proto-Indo-European root *ǵerh₂- (74 c, 0 e) 
150-
151: *ǵérh₂-e-ti ( thematic root present ) [ 2 ] 
152- Proto-Indo-Iranian: *ȷ́árHati 
153- Proto-Indo-Aryan: *ȷ́árHati 
154- Sanskrit: जरति ( járati ) 
155-
--
273: ^ Watkins, Calvert ( 2000 ), The American Heritage Dictionary of Indo-European Roots , 2nd edition, Boston: Houghton Mifflin 
274-
275- ↑ 2.0 2.1 Rix, Helmut , editor ( 2001 ), Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr. Ludwig Reichert Verlag, →ISBN , pages 165-166 
276-
277- ^ Starostin, Sergei (1998). The Tower of Babel: An Etymological Database Project .
```


## [2026-09-05T20:54:38.172Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '140,272p' 6fad9586c75ec61e.txt"
}
```


### [2026-09-05T20:54:38.215Z] TOOL RESULT

```
 [ edit ] 

 *ǵerh₂- [ 1 ] [ 2 ] 

 to grow old, to mature [ 3 ] 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *ǵerh₂- (74 c, 0 e) 

 *ǵérh₂-e-ti ( thematic root present ) [ 2 ] 
 Proto-Indo-Iranian: *ȷ́árHati 
 Proto-Indo-Aryan: *ȷ́árHati 
 Sanskrit: जरति ( járati ) 

 *ǵorh₂-éye-ti ( eye-causative ) 

 *ǵr̥h₂-nó-m ( “ grain ” ) 

 *ǵerh₂-ós ( e-grade *-ós adjective ) 
 Proto-Armenian: 
 Old Armenian: ծեր ( cer ) Armenian: ծեր ( cer ) 

 *ǵerh₂-ró-s 
 Proto-Hellenic: 
 Ancient Greek: γεραρός ( gerarós ) 

 Proto-Iranian: *jár̥Hrah 
 Avestan: 𐬰𐬀𐬎𐬭𐬎𐬭𐬀 ( za u rura , “ weak through old age, decrepit ” ) 

 *ǵr̥h₂-yéw-s 
 Proto-Hellenic: *grayéus 
 Ancient Greek: γρᾱῦς ( grāûs ) 

 Proto-Albanian: *grāwā 
 Albanian: grua ( woman, wife ) 

 *ǵr̥h₂-yó-s 
 Proto-Hellenic: 
 Ancient Greek: γεραιός ( geraiós ) , γραῖᾱ ( graîā ) , Γραῖαι ( Graîai ) , Γραῖα ( Graîa , “ ancient city ” ) , Γραῖος ( Graîos ) 
 ⇒ Ancient Greek: Γραικός ( Graikós ) → Latin: Graecus , Latin: graecus ( see there for further descendants )

 → Latin: Grāius 

 *ǵērh₂-s 
 Proto-Hellenic: 
 Ancient Greek: γῆρας ( gêras , “ old age ” ) , γέρας ( géras , “ gift of honour ” ) 

 *ǵérh₂-ont-s 

 *ǵérh₂-u-s ~ *ǵr̥h₂-éw-s 
 Proto-Tocharian: *śërāw'ë- 
 Tocharian B: śrāy 

 *ǵérh₂-mn̥ ~ *ǵr̥h₂-mén-s 
 Proto-Indo-Iranian: *ȷ́árHma 
 Proto-Indo-Aryan: *ȷ́árHma 
 Sanskrit: जरिमन् ( jariman , “ old age, decrepitude ” ) 

 Proto-Iranian: *járHma 
 Middle Persian: ( “ old age ” ) 
 Manichaean script: 𐫉𐫡𐫖𐫀𐫗 ( zrmʾn /⁠zarmān⁠/ ) , 𐫉𐫡𐫖𐫀𐫗𐫏𐫆 ( zrmʾnyẖ /⁠zarmānīh⁠/ ) 
 Book Pahlavi script: [Book Pahlavi needed] ( zlm'n' /⁠zarmān⁠/ ) 
 Persian: زرمان ( zarmân ) , زرم ( zarm ) 

 Proto-Hellenic: 
 Ancient Greek: γήραμα ( gḗrama , “ old age ” ) 

 *ǵorh₂-o-s 
 Proto-Germanic: *karaz , *karilaz ( see there for further descendants )

 *ǵorh₂-wó-s 
 Proto-Iranian: *járHwáh ( “ old age ” ) 
 Avestan: 𐬰𐬀𐬎𐬭𐬎𐬎𐬁 ( za u ruuā , “ old age ” ) 

 Khwarezmian: [script needed] ( ʾzr ) 

 Sogdian: [Term?] ( “ old age ” ) 
 Manichaean script: 𐫉𐫡𐫇 ( zrw /⁠zarw⁠/ ) 
 Sogdian script: 𐼵𐽀𐼴𐼳 ( zrwh /⁠zarw⁠/ ) 
 Syriac script: ܙܪܘ ( zrw /⁠zarw⁠/ ) 

 Ossetian: 
 Digor Ossetian: зӕруӕ ( zærwæ ) , зӕруай ( zærwaj , “ old age ” ) 

 Pashto: زړوالۍ ( zaṛwā́lay , “ old age ” ) 

 Parthian: 𐫉𐫡𐫇𐫀𐫗 ( zrwʾn /⁠zarwān⁠/ , “ old age ” ) 

 *ǵorh₂-tó-s 
 Proto-Iranian: *járHtáh ( “ old; old age ” ) 
 Avestan: 𐬰𐬀𐬭𐬆𐬙𐬀 ( zar ə ta , “ old ” ) 

 → Manichaean Middle Persian: 𐫉𐫡𐫅 ( zrd /⁠zard⁠/ , “ infirm; old age ” ) 
 Persian: زال ( zâl , “ Zāl (a mythological person in Shahnameh who has an old face and white hairs); albino ” ) ; زر ( zar , “ old ” ) 

 Sogdian: [Term?] ( “ old age; old woman ” ) 
 Manichaean script: 𐫉𐫏𐫡𐫤𐫐 ( zyrtk /⁠zirt(a)⁠/ ) 
 Sogdian script: 𐼵𐼷𐽀𐽂𐼳 ( zyrth /⁠zirt(a), zert(a)⁠/ ) 

 Pashto: زړه ( zaṛa , “ old ” ) , زوړ ( zoṛ , “ old ” ) , زاړه ( zāṛə́ ) 

 *ǵorh₂-is-to-s 
 Proto-Iranian: *járH-ištah ( “ oldness ” ) 
 Pashto: زړښت ( zaṛǝ́x̌t , “ oldness ” ) 

 Unsorted formations 

 Sanskrit: जरा ( jarā́ , “ old age ” ) 

 Sanskrit: जरस् ( jarás , “ senescence, decay, old age ” ) 

 Sanskrit: जर ( jára , “ becoming old; the act of wearing out, wasting ” ) 

 Sanskrit: जरायु ( jarāyu , “ decaying; the cast-off skin of a serpent; a perishable covering; afterbirth ” ) 

 Proto-Albanian: *grāwā [ 4 ] 
 Albanian: grua , grue , gru — Gheg , gruo — Old Gheg 

 Proto-Balto-Slavic: 
 Proto-Slavic: *zьrěti > *zrělъ ( see there for further descendants )

 Descendants
 [ edit ] 

 Proto-Indo-Iranian: 
 Proto-Indo-Aryan: 
 Sanskrit: जॄ ( jṝ ) 

 References
 [ edit ]
```


## [2026-09-05T20:54:59.035Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/Zoroaster\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%9C%E0%A5%80%E0%A4%B0%E0%A4%95\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%9C%E0%A5%80%E0%A4%B0%E0%A5%8D%E0%A4%A3\" \\\n \"https://www.etymonline.com/word/corn\" \\\n \"https://www.etymonline.com/word/churl\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 174, root Ger 2/Greno\" 2>&1 | tail -1\ndone"
}
```


### [2026-09-05T20:55:07.187Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c5ab7a560ed68ad3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/36d2d99073f98331.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9921b02dbe3ff8f1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fef53652a74fc919.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bee7b79c6299f51b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3e1637a32174fff2.txt
```


## [2026-09-05T20:55:10.347Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"######## زیره ########\"; grep -n -i -B2 -A18 \"Etymology\" 535f8a29227c4e5d.txt | sed -n '1,60p'"
}
```


### [2026-09-05T20:55:10.399Z] TOOL RESULT

```
######## زیره ########
63-
64- 1.2 
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Derived terms 
75-
76- 1.4.2 
77- Descendants 
78-
79- Toggle the table of contents 
80-
81- زیره 
82-
83- 5 languages 
--
155- ژیره ( žire ) ( archaic ) 
156-
157: Etymology
158- [ edit ] 
159-
160: (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 
161-
162- Cognate with Baluchi زیرگ ( zirrag ) , Northern Kurdish zîre , Central Kurdish زیرە ( zîre ) , Southern Kurdish زیرە ( zîre ) , Sogdian [script needed] ( zyr'kk /⁠zîrê⁠/ ) , and distantly with Sanskrit जीरक ( jīraka ) . Further origins outside of Iranian unclear.
163-
164- Pronunciation
165- [ edit ] 
166-
167- ( Classical Persian ) IPA ( key ) : /ziː.ˈra/ 
168-
169- ( Dari, formal ) IPA ( key ) : [ziː.ɾá] 
170-
171- ( Dari, formal ) IPA ( key ) : [ziː.ɾá] 
172- ( Kabuli ) IPA ( key ) : [ziː.ɾá] 
173-
174- ( Hazaragi ) IPA ( key ) : [zi.ɾá] 
175-
176- ( Iran, formal ) IPA ( key ) : [ziː.ɹé] 
177-
178- ( Tajik, formal ) IPA ( key ) : [zi.ɾá]
```


## [2026-09-05T20:55:18.458Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"######## जीरक ########\"; sed -n '/^ Etymology$/,/^ References/p' 9921b02dbe3ff8f1.txt | head -40\necho \"######## जीर्ण ########\"; sed -n '/^ Etymology$/,/^ Further/p' fef53652a74fc919.txt | head -50"
}
```


### [2026-09-05T20:55:20.295Z] TOOL RESULT

```
######## जीरक ########
 Etymology
 [ edit ] 

 Traditionally considered a nominal formation related to जॄ ( jṝ , “ to grow old ” ) , presumably to the dusty and "old" nature and coloration of cumin, [ 1 ] though this appears to be folk etymology. More likely borrowed from some Iranian language; compare modern Persian زیره ( zira , “ caraway; cumin ” ) . [ 2 ] 

 Pronunciation
 [ edit ] 

 ( Vedic ) IPA ( key ) : /d͡ʑíː.ɾɐ.kɐ/ 

 ( Classical Sanskrit ) IPA ( key ) : /d͡ʑiː.ɾɐ.kɐ/ 

 Noun
 [ edit ] 

 जीर॑क • ( jī́raka ) stem ,  m [ 1 ] 

 cumin 

 Declension
 [ edit ] 

 Masculine a-stem declension of जीरक 

 singular

 dual

 plural

 nominative

 जीरकः ( jīrakaḥ ) 

 जीरकौ ( jīrakau ) 
 जीरका¹ ( jīrakā¹ ) 

 जीरकाः ( jīrakāḥ ) 
 जीरकासः¹ ( jīrakāsaḥ¹ ) 

######## जीर्ण ########
 Etymology
 [ edit ] 

 Borrowed from Sanskrit जीर्ण ( jīrṇa ) .

 Pronunciation
 [ edit ] 

 ( Standard Hindi ) IPA ( key ) : /d͡ʒiːɾɳ/ 

 Adjective
 [ edit ] 

 जीर्ण • ( jīrṇ ) 

 old , ancient , aged 
 Synonyms: पुराना ( purānā ) , प्राचीन ( prācīn ) , वृद्ध ( vŕddh ) 

 decayed , decrepit , worn out , dilapidated 
 Synonyms: जर्जर ( jarjar ) , शिथिल ( śithil ) 
 Antonyms: नूतन ( nūtan ) , नया ( nayā ) , नवीन ( navīn ) 

 shattered , broken , tattered 

 Noun
 [ edit ] 

 जीर्ण • ( jīrṇ )  m 

 digestion 

 old age 

 benzoin 

 Declension
 [ edit ] 

 Declension of जीर्ण (masc cons-stem) 

 singular

 plural

 direct

 जीर्ण 
 jīrṇ 

 जीर्ण
```


## [2026-09-05T20:55:33.048Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"######## ارزن ########\"; sed -n '/^ Persian$/,/^ References/p' 6178e070fb4b681c.txt | head -60"
}
```


### [2026-09-05T20:55:34.841Z] TOOL RESULT

```
######## ارزن ########
 Persian
 [ edit ] 

 Persian Wikipedia has an article on: ارزن 

 Wikipedia fa 

 Etymology
 [ edit ] 

 From a Northwestern Iranian language.

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʔar.ˈzan/ 

 ( Dari, formal ) IPA ( key ) : [ʔäɾ.zán] 

 ( Dari, formal ) IPA ( key ) : [ʔäɾ.zán] 
 ( Kabuli ) IPA ( key ) : [ʔäɾ.zán] 

 ( Hazaragi ) IPA ( key ) : [ʔäɾ.zán] 

 ( Iran, formal ) IPA ( key ) : [ʔæɹ.zǽn] 

 ( Tajik, formal ) IPA ( key ) : [ʔäɾ.zán] 

 Rhymes: -an 

 Readings

 Classical reading ? 

 arzan

 Dari reading ? 

 arzan

 Iranian reading ? 

 arzan

 Tajik reading ? 

 arzan

 Noun
 [ edit ] 

 ارزن • ( arzan ) 

 millet 

 Further reading
 [ edit ] 

 Mallory, J. P. , Adams, D. Q. , editors ( 1997 ), Encyclopedia of Indo-European Culture , London, Chicago: Fitzroy Dearborn Publishers, page 237
```


## [2026-09-05T20:55:44.869Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"######## Zoroaster ########\"; sed -n '/^ Etymology$/,/^ Proper noun/p' 36d2d99073f98331.txt | head -40\necho; echo \"######## زر ########\"; sed -n '/^ Persian$/,/^ Descendants/p' c5ab7a560ed68ad3.txt | head -70"
}
```


### [2026-09-05T20:55:46.451Z] TOOL RESULT

```
######## Zoroaster ########
 Etymology
 [ edit ] 

 Learned borrowing from Latin Zōroastrēs , from Ancient Greek Ζωροάστρης ( Zōroástrēs ) , from Avestan 𐬰𐬀𐬭𐬀𐬚𐬎𐬱𐬙𐬭𐬀 ( zaraθuštra ) . Doublet of Zarathustra .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ˌzɒɹoʊˈæstəɹ/ , /ˈzɒɹoʊˌæstəɹ/ 

 Audio ( Southern England ) : ( file ) 

 Proper noun
 Etymology
 [ edit ] 

 Ultimately from Latin Zōroastrēs , from Ancient Greek Ζωροάστρης ( Zōroástrēs ) , from Avestan 𐬰𐬀𐬭𐬀𐬚𐬎𐬱𐬙𐬭𐬀 ( zaraθuštra ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ˌzoː.roːˈɑs.tər/ , ( Northern Standard Dutch ) [ˌzoː.roʊ̯ˈɑs.tər] 

 Hyphenation: Zo‧ro‧as‧ter 

 Rhymes: -ɑstər 

 Proper noun
 Etymology
 [ edit ] 

 Learned borrowing from Latin Zōroastrēs , from Ancient Greek Ζωροάστρης ( Zōroástrēs ) , from Avestan 𐬰𐬀𐬭𐬀𐬚𐬎𐬱𐬙𐬭𐬀 ( zaraθuštra ) . Doublet of Zaratustra and Zaratusztra .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /zɔ.rɔˈas.tɛr/ 

 Rhymes: -astɛr 


######## زر ########
 Persian
 [ edit ] 

 Persian Wikipedia has an article on: زر 

 Wikipedia fa 

 Etymology 1
 [ edit ] 

 From Middle Persian *zarr ( “ gold ” ) , from Parthian *zarn ( “ gold ” ) ; the inherited form would have started with a D, as is seen in Old Persian 𐎭𐎼𐎴𐎡𐎹 ( d-r-n-i-y ) . Ultimately from a derivative of Proto-Indo-European *ǵʰelh₃- ( “ green, yellow ” ) . Indo-Iranian cognates include Northern Kurdish zêrr , and Sanskrit हिरण्य ( hiraṇya ) . Other cognates include Old Church Slavonic злато ( zlato ) , Latvian zelts , and English gold and yellow .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈzarr/ 

 ( Dari, formal ) IPA ( key ) : [zäɾ(ː)] 

 ( Dari, formal ) IPA ( key ) : [zäɾ(ː)] 
 ( Kabuli ) IPA ( key ) : [zäɾ(ː)] 

 ( Hazaragi ) IPA ( key ) : [zäɾ(ː)] 

 ( Iran, formal ) IPA ( key ) : [zæɹ(ː)] 

 ( Tajik, formal ) IPA ( key ) : [zäɾ(ː)] 

 Rhymes: -arr 

 Readings

 Classical reading ? 

 zarr

 Dari reading ? 

 zarr

 Iranian reading ? 

 zarr

 Tajik reading ? 

 zarr

 Noun
 [ edit ] 

 Dari

 زر 

 Iranian Persian

 Tajik

 зар 

 زر • ( zar ) ( Tajik spelling зар ) 

 gold 
 Synonym: طلا ( talâ ) 

 Derived terms
 [ edit ] 

 زرگر ( zargar )
```


## [2026-09-05T20:55:56.241Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Zarathustra\" \\\n \"https://www.iranicaonline.org/articles/azarmigduxt\" \\\n \"https://en.wiktionary.org/wiki/Zurvan\" \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D9%88%D8%A7%D9%86\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 174, root Ger 2/Greno\" 2>&1 | tail -1\ndone\necho \"### zal ###\"\nsed -n '/^ Persian$/,/^ Pronunciation/p' data/verification/sources/web/1bdf06fd715c0de3.txt | head -40"
}
```


### [2026-09-05T20:56:03.645Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5736e12792dac7d1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7a5e4d0e5bd08859.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/99bbef29106cbf1f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/22c76f83bf215783.txt
### zal ###
 Persian
 [ edit ] 

 Persian Wikipedia has an article on: زال 

 Wikipedia fa 

 Dari

 زال 

 Iranian Persian

 Tajik

 Зол 

 Etymology
 [ edit ] 

 perhaps from Proto-Indo-European *ǵerh₂- ( “ to grow old, to mature ” ) 

 Pronunciation
```


## [2026-09-05T20:56:07.084Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"### Zarathustra ###\"; sed -n '/^ Etymology$/,/^ Proper noun/p' 5736e12792dac7d1.txt | head -30\necho; echo \"### Iranica azarmigduxt ###\"; head -60 7a5e4d0e5bd08859.txt\necho; echo \"### Zurvan ###\"; sed -n '/^ Etymology$/,/^ Proper noun/p' 99bbef29106cbf1f.txt | head -25"
}
```


### [2026-09-05T20:56:08.915Z] TOOL RESULT

```
### Zarathustra ###
 Etymology
 [ edit ] 

 From German Zarathustra , from Avestan 𐬰𐬀𐬭𐬀𐬚𐬎𐬱𐬙𐬭𐬀 ( zaraθuštra ) . Doublet of Zoroaster .

 Proper noun

### Iranica azarmigduxt ###
URL: https://www.iranicaonline.org/articles/azarmigduxt
FETCHED: 2026-09-05T20:56:02Z
STATUS: 200
TITLE: ĀZARMĪGDUXT - Encyclopaedia Iranica

ĀZARMĪGDUXT - Encyclopaedia Iranica Skip to main content 
 Search Iranica...

 search in 8,977 entries of Encyclopædia Iranica. 

 Close Search 

 search 
 account 
 Menu 

 Explore 
 News & Events 
 Editorial Current Board 
 Former Boards 

 Authors 
 Style Guide 
 About About Iranica 
 Ehsan Yarshater 
 Advisory Board 
 Board of Directors 
 FAQ 
 Contact 

 Donate 
 search 

 account 

 ĀZARMĪGDUXT

 Browse Iranica 

 ĀZARMĪGDUXT

 Article by 

 Philippe Gignoux 

 Last Updated September 24, 2018

 Print Detail Vol. III, Fasc. 2, p. 190

 Published December 15, 1987

 Print

 cite 
 share 

 ĀZARMĪGDUXT (Pers. Āzarmīdoḵt, Arzmīdoḵt, Arzmīndoḵt, Āzarūmīddoḵt), Sasanian queen who according to Ṭabarī ruled for a few months in 630. She was the sister of Queen Pūrān (r. 630 or 631), daughter of King Ḵosrow II Parvēz. Her name, meaning “daughter of the respected one,” refers to her father (see Nöldeke, Geschichte , p. 393 n. 2). We know little about this figure, who belongs to the troubled period at the end of the Sasanian monarchy, but her existence is confirmed by the evidence of coins.
 M. I. Moshiri discovered and published a coin of this queen ( Ētudes I, pp. 11-16); it was struck in the year 1 at a mint called WYHC, which has been thought to be Veh-az-Amīd-Kavād (= Arrajān). The piece bears the effigy of a man. Moshiri explains this anomaly by suggesting that it is the figure of Farroḵ-Hormozd, who supposedly wished to seize power, and who actually obtained it under the name Hormozd VI (cf. Ētudes II, pp. 209-12). He was able to reign simultaneously with the queen for a little more than a year. There are no coins of Hormozd VI struck in the year 1, only examples dated in the years 2 and 3. Two other coins of the queen are in the Bibliothèque Nationale (Paris), and the late M. Foroughi also possessed one. Only the mint WYHC is attested.
 The Islamic sources give the length of her reign variously as six months (Ṭabarī, I, p. 1065; Yaʿqūbī, I, p. 198; Bīrūnī, Chronology , p. 123; Ḥamza, p. 28; Ebn Meskawayh, Tajāreb I, p. 270), four months (Maqdesī, Badʾ III, p. 173; Kasrawī, apud Ḥamza, p. 22 [cf. p. 28]), and sixteen months (Masʿūdī, Morūj [ed. Pellat] I, p. 322; Ḥamza, p. 16; Mojmal , p. 83).
 Ṭabarī (I, pp. 1064-65) relates that Farroḵ-Hormozd, the military commander of Khorasan, asked for her in marriage. Not daring to refuse, the queen invited him to her private quarters, where she had him killed. To avenge him, his son Rostam apparently captured the capital Ctesiphon, then dethroned the queen and had her blinded and killed.

### Zurvan ###
```


## [2026-09-05T20:57:36.696Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"azariiiia\\|azarima-\\|azarsma\\|a  zar\\|• *g\\. *azar\\|azarama\" BRT.txt | head -10\necho \"--- search 'zarima' ---\"; grep -n \"zarima\\|zarsma\\|zar»ma\\|azar»m\" BRT.txt | head -10\necho \"--- dugdar ---\"; grep -n \"dugidar\\|dugsdar\\|dug»dar\" BRT.txt | head -5"
}
```


### [2026-09-05T20:57:36.780Z] TOOL RESULT

```
2872:aoxta  zaraiiuitrö:  mmö  /taomifi  "drauf, sprach  Z.:  'Verehrung  dem  .ff.'"  Y.(j.i6, 3,  /£>.  17;  -1.2,  Az.  I,  Yl  /.  5,  21,  j.  2, 5.83,  91,  95,  i<.io,  77.54.  V.  2.  40,  42,' 3.  26,  Vyt  24,  54,  Vd.  12,  20;  —  ,7a/! Aim  aoxta  p»r>sö  yö  narl  asaonö  un'a:\ as.'a  ..  "und  es  sagte,  ihn  fragend  ..: 'Und  wer  ..'"  H.  2. 10;  —  äal  aoxta  akurö  \ ..  yimii:  yima  srira  "und  es  sprach  Ah.^ zu  y.:  'y.  . .'"  V.2.22; — yö  naire  aoxte (3SP0.-  M  ml  aä  (sd.)  F.^d;  N.;,^,! tft;  —  aojUa  (jSPr.)"  ../raiaoitrazibya  ..: aiayata  . .  Vyt, //;  —  at  Aöi  aoß  (iSPr.) zara'httströ  paourvTm  "Drauf  sagte  ich zu  ihm  ersthch:  ^Zar.  (bin  ich)'"  Y.  43. 8.  a  )    mit    uili  (sd.):    mi^rim  .  .  yö
6264:lich bezeichneten  Personen:  frasaoslrs ''Opa  Y.7/.1;  —  'sava  jämäspö  N.Ä9; —  "hraMaomm  "Az/a»?«  FrW.  2. 2 ;  i;  — gayehe  mary^nH  °s'aonSY.26.5,  Yt/J.87; 95-138'",  Y.7J.7,  2(7.5';  —  Vä«m tu'taspa  Vyt.  4s;  ~-  hvüvi  'laoni  Y\..i6. 'S; —  kt^yä  'saonyä  Yt./^.  139;  139— 141'*;  —  »nsvä  sräts.sps(,a  'saonä  {GD.} YL/^.  115;  115,124, 125,127'.  A)insbes. von  Zara'^ustra  (Spitama):  zatS  bl  yö '!ai-a  sara'inus'tre  V.  75.46;  3,  4,  10,  Yl. i.104,  7J.41,  74.28,  Vr.  77. 19,  Y.77.13, ^■43^'t  Vyt  70;  — yS  'sava  zara%u/trd Y.72.6; —  'iäva  yäia  zara%ustre  Yyl..  2, Az.4;  —  *savat>3m  i:ara%ui'inm  V.1O.2, 71.1,  2,  Yt,5.i8,  76.15,  ^5-79.  81  (statt I^om.),  V.5.21;  —  *saonö  zar^uHrahe Y.^23,  76".  2,  27.1,  24.5,2S.o,S7.S,08. «.  77.2,  P.5Ö,   Vr.76.2,  Yt«2,  y.62,
10138:—  tistryS ..vaz»mnö  -Jus  k)hrpa  zaranyS.-  bagä  x^ar^mnif  (sd.)  Y. 32. 8;  —  "Su/x'ar»- srvahe  YLÄ16;  i4-l,  Y.ig.yi.  A)  Das  \%ahe  nr^yJ  V.7.  43; — 'Sul  vä  s^var3%ahe Rind  gilt  als  Repräsentant  aller  nützlichen  j  (sd.)  vä  W.14.1T,  —  '!us  i^ar/itinqm {ahumohtn)  Tiere,  daher  ^gav-  auch  inJH, /.  5;  —  yasca  ..  lanumazs {^A.)  'Jui weiterem  Sinn  gebraucht  wird*"':  para\da%at  "W-iS.!!);  —  °amla  ifsst)m  anäp»m •Su^  ca^war).paitistanaya  dänheit  para\{%d.)  V.5,  52;  S3f.',  7.55;  —  buiri 'aas  ,  . nars  asaotiB  bipaittstänahe  zq%st  Y.  /p.  8 ;  j  3far>^a  . .  VyL  4:5.  3)  'Milch',  bes.  zur
12347:•  j.  Jtüirya-  Adj.  (fem.  °yä-)  'der  vierte': paoiryS  . .  bityS  .  .  %rityS  ...  'ryS  ma^ Y.5.3~";  i3,V.^2,Yt74.ii,Vd.72;  — nmänyasca  vTsyasca  lantumasca  zara^ustrü 'ryS  Y.lf).iS;  /<¥.  53,  54;  — paeirim  .  . bitlm  ..  ^ritlm  ..  'rlm  yänttn  Y.^j.ijt;
12460:'äkirsnvS  vJspe  'va  zardhufira  yBt  para akmät  vtr5.rai^a  apataypn  paiii  äya  amS "du  hast  bewirkt,  dass  die  D.  sich  alle  in die  Erde  verkrochen,  die  sich  zuvor  in Männei^estalt  auf  der  Erde  herumtrieben" Y.p.  15;  FrW.4.3;  —  valtumnsm  akmat para  "va  patayjn  .  .  *apaJtarlay?n  (sd.) fainis  haca  maiyakaHbyS  aal  tä  .  .  hazB nivarKaym  (sd.)  'va  äat  tl  aivS  ahunS vaifyS  .  .  *zamangusa  avasai  vXipe  "va ayesnya  avahmya  Yt.  ig.  Za{.;  — ansürahe (sd.)  grlvaya  .  .  yat  ahmya  °va  handva- nnti  druj5  haca  girihSha  Y.^.j;  ig.44;  — alte  yei  "va  aBaisva  daxmalsva  gaafanü apaca  valpptttiY.j.$$; — Jha  'vanqm  han- dvarMS  kva  'vanqm  hantpatanS  kva  '-va hqmjivannti . .  /  . .  altaihßa  daxntaisva . .  V. 7.53 f.;  54^;  —  öAva  vyari%aAva{s,d.)  zpmS
14314:\tavaia  hüXimä  asaAyäl^ä  Y.  40.  a;  — hubfrfti  .  .  atari  Sfrinämi  huyesti  1  tnva ahuränt  äfrJnämi  Y.  68. 14;  —  äyese  yeili Aavanaeibya  .  .  tastai  . .  varfsäi  ..  I  tavafa bargsmanS  Vr.  70.  3;  —  avi  apqmla  .  . yasrmn  gsrpömaki..  I  avi  tava  zard^uitra Vr.  27.  if.;   z=.  zu  1  b):  \tava  ätars
14890:yaoiädhd  dakmayStparS  ä/ritstt.,  dairihu. paitlm yaozdd^ö  ustraAe'ti  arsnSV.Q.^T'^; 37  f.*.  a)  bes.  beim  V._>'a«-:  vanani^m .  .  yazamaide  amaheca  °ii  kuiastahe  Yt. Ä  I2J  12',  U- 133-135 '^  JJi;  —  yaf^a- maide  ^a/am  malfi^anahe  (sA)  °//*'  .  . drvaßaoi  Y.  7Ö'.  10;  —  ft«  yazata  . .  zara- %uitrS  v^fhraynaAe  'ti  manahi  Yt/^^aS; 78';  —  yqm  yasata  zard^uilrS  .  .  ava- he^a  'ti  yqnahe  yat  hi  da^a/  .  .  Yt.  16, 6f.  b)  aSahe  paiti  (Sp.  14  m.,  u.)  '(als
14891:Entgelt)  dafür':  äa^  mqm  tarn  *^aisaxyilii ..  dahäni  tl  aStahe  'ti  V.22.  2f.'3>;  — iat  astahe  'ti  ..  azaeta  (Sp.  2240.)  V. iK  68**;  —  ait»)n>m  ijaoiinanqm  .  . altahe  'ti  .  .  duye  saite  upaeananqm  upä- «3(V  (Sp.  224  m.)  V.  4.  2o'4).  '4)  zur Bezeichnung  der  Ursache  und  Urheber- schaft, sowie  des  Mittels  'per';  i)  mit  Akk.; a)  'mittelst':  frasnatse  .  .  ayryqm  (sd) 'ti  usnäitlm  V,  Ä  98;  —  mi^ra  ahura  .  . yasamaide  .  .  urvarä  'ti  batvsmanyä  Yt. 10. 145  (s.  2a);  —  yasiä  Hl . ,  väHm  °ti tofnis  {sd.)  anhat  V.  7^,  40;  — aitakmllyus 'ti'>^  AirÄ^w  V./5.ai,  43.  b)'wegen, propter':  aitahmSyiti  'ti"'''  varsla  syao^na V.  75. 10.  2)  mit  Lok.;  a)  'mittelst': ahura  mi>ra . ,  urvaräÄu  *ti  bar)smanyähu .  .  äyese  yati  Y.  2,  11  (s.  i  a);  —  */tahmäi tl  aioahmi  'ti  vaSs  . .  /ravaktm  (sd.)  H. /.  I*'; —  handaitim  staotanqm  yesnyanqm yasamaide  apan3J»may3  (sd.)  °tl  va^astaltä Y.sS.S'^-l  b)  'durch':  saräku^lrahe  . . yakmi  'ti  .  ,  *asim.srav3  (sd.)  vTsruyaia Yty.  91.  c)  'wegen,  propter':  nSil.. ahmi  'ti  nairi  dva  *mainyu  r}na  (sd.)  ava.- stäahat  V.  7. 52.  3)  mit  Gen, ;  a)  'mittelst'; yqm  yazata  zarä^uströ  . .  humatahe  °ti manavAlF    Yt.  16.  6;    6'.  b)    'wegen,
16417:•  j.  pisra-  m.  Bezeichnung  einer  Vor-  ^,^.^,^  ,^^  ^^J/^^^^aiW"  (sd.)  V.  5. nchtung  zum  Schweissen  von  MetaUen:  ^  ^)  '(Ausgequetschtes  sva.)  MehT: -rai  hüca  zaranyöaa!j,ät  . .  'rat  haca  ,r>-  ^^^  ,^^  ^  ^^  ia?  darva  «ru^J  "wenn ,aii^.sa^äi  'rat  haca  «ySsji^Pät .  .  'rai^;^  ^j^j^j  ^^^  Teiganmachen)  zurecht haca  haosaJnam5.,a^ilt  V.  8.  87-90.  ,  gelegt  wird,  dann  heulen  die  D."  V.  j.32.
17233:•  j.  be  Part  zur  Hervorhebung  des  ersten Worts  im  Satz:  zätS  b'  yS  asava  zara- ^u/irS  V.  ig.  46.
--- search 'zarima' ---
6273:—  ratavö  vispe  mazista  °l3um  {statt  Plur.) asahe  ratavS  Y.  7. 2  2 ;  —  asnya  'savana (als  AP.)  aiahe  ratavö, .  hävanJm  'savan^m asahe  ratum  Y.2.3;  3  ff.  (oft),  Vr.2.2ff. (oft),  G.7.7,  2.8,  j.5ff.,  ^.sff.,  5.5ff.,  S. 2.6;  —  hsvatiSe  'laone  alahe  ra%we  Y. 7.3;  3  ff.  (oft);  —  inai'iyöizarimayehe  'SaonS
27934:Zum  ai.  V.  jiryaü,  jiiyati  'er  wird  gebrech- lich', yara/i  'er  macht  gebrechlich'.  S.  noch azarima;  azanianl-,  zaunira-,  'zanta-,  zaurvan-, :ara%uilra-.  —  Vgl.  np.  aar,  aast,  sätoiid 'Greis'.  —  Pü. :  izäriar,  erl. :  xärkarih  i  tu  ke vas  ^apcl  :är  apc  bavet.
--- dugdar ---
```


## [2026-09-05T20:57:39.171Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/%D8%A2%D8%B2%D8%B1%D9%85\" \"https://en.wiktionary.org/wiki/%D8%A2%D8%B2%D8%B1%D9%85%DB%8C%D8%AF%D8%AE%D8%AA\"; do python3 tools/fetch_source.py \"$u\" --note \"page 174, Azarmidoxt\" 2>&1|tail -1; done"
}
```


### [2026-09-05T20:57:42.306Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/dfddd5bfa2c86a44.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2ddf9c6993d93db0.txt
```


## [2026-09-05T20:57:50.276Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"### آزرم ###\"; sed -n '/^ Persian$/,/^ Noun/p' dfddd5bfa2c86a44.txt | head -30\necho \"### آزرمیدخت ###\"; sed -n '/Etymology/,/Proper/p' 2ddf9c6993d93db0.txt | head -25\necho \"### Zurvan wikt ###\"; grep -n -A6 \"Etymology\" 99bbef29106cbf1f.txt | head -30"
}
```


### [2026-09-05T20:57:52.161Z] TOOL RESULT

```
### آزرم ###
### آزرمیدخت ###
### Zurvan wikt ###
```


## [2026-09-05T20:57:55.083Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in dfddd5bfa2c86a44 2ddf9c6993d93db0 99bbef29106cbf1f 22c76f83bf215783; do echo \"=== $f ===\"; sed -n '1,6p' $f.txt; wc -l $f.txt; done"
}
```


### [2026-09-05T20:57:56.869Z] TOOL RESULT

```
=== dfddd5bfa2c86a44 ===
URL: https://en.wiktionary.org/wiki/%D8%A2%D8%B2%D8%B1%D9%85
FETCHED: 2026-09-05T20:57:41Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found5 dfddd5bfa2c86a44.txt
=== 2ddf9c6993d93db0 ===
URL: https://en.wiktionary.org/wiki/%D8%A2%D8%B2%D8%B1%D9%85%DB%8C%D8%AF%D8%AE%D8%AA
FETCHED: 2026-09-05T20:57:42Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found5 2ddf9c6993d93db0.txt
=== 99bbef29106cbf1f ===
URL: https://en.wiktionary.org/wiki/Zurvan
FETCHED: 2026-09-05T20:56:03Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found5 99bbef29106cbf1f.txt
=== 22c76f83bf215783 ===
URL: https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D9%88%D8%A7%D9%86
FETCHED: 2026-09-05T20:56:03Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found5 22c76f83bf215783.txt
```


## [2026-09-05T20:58:10.437Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://www.iranicaonline.org/articles/zurvanism\" --note \"page 174, zarvan/time\" 2>&1|tail -1\npython3 tools/fetch_source.py \"https://abadis.ir/fatofa/%DA%AF%D8%B1%D8%A7%D9%86%DB%8C%D8%AA/\" --note \"page 174, Moin granit\" 2>&1|tail -1\npython3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%A7%D8%B1%D8%B2%D9%86/\" --note \"page 174, Moin arzan\" 2>&1|tail -1"
}
```


## [2026-09-05T20:58:12.000Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 grep ger-/granum ===\"; grep -n \"gerə-\\|ĝer-\\|gr̥-nom\\|granum\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20"
}
```


### [2026-09-05T20:58:20.053Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/46f7d14c9ced9d81.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/969b49a7f2a684fa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/66e8513c1a917555.txt
```


### [2026-09-05T20:58:20.099Z] TOOL RESULT

```
=== WLD Bd1 grep ger-/granum ===
37771:s Boisacq 159); lat. granum „Korn, Kern" (*g e rg-nom, = ai. jlrnd-, s. o.) 
46727:Cymr. talch „granum contritum", acorn, talcli „furfures“ (-«/- aus idg.
```


## [2026-09-05T20:59:31.651Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '37735,37790p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt\necho \"=== page tag ===\"\nawk 'BEGIN{RS=\"\\f\"} /granum „Korn, Kern\"/{print \"LEAF \"NR}' incoming/WLD/WLD_Bd1_pages.txt 2>/dev/null | head -3\ngrep -n \"granum „Korn\" incoming/WLD/WLD_Bd1_pages.txt | head -2"
}
```


### [2026-09-05T20:59:33.471Z] TOOL RESULT

```
durch yi]oa und dasselbe i] zeigt ygoam ,.altere“ (in die them. Konjugation 
iibergefuhrtes *yt)oa- l ui, das noeh ini Ptc. praes. ygodg „alternd", Inf. praes. 
yggdvai , Aor. iy/joana ; tliemat. Impf. ist syrjga, Osthoff aaO.', Aor. ,,pass." 
iyVQ r l v Ptc. yijgelg; dies yij o- ist (trotz Persson Beitr. 671) kaum alte 
Dehnstufe, sondern (nach Osthoffi zuerst in yggdco nach yfidw aufgekommen 
t fiir * yeoaco , alter *yegd-/a-, syggip- fiir eydgijv liber *eyegi]v) und von bier 
aus auf yijgag fiir yegug iibertragen (letzteres nur in der iibertragenen Bed. 
„Altersvorrecht“ bewahrt), ebenso auf yqgdoxo. j „altere, reife", yijga/.eog 
(bei Hes. nocli yega/Jog) „alt"; att. ygavg, gen ;’p«(*j:)dc thorn. Dat. ygtfl) 
„alte Frau" (hom. ygfjiig wohl spatere L’mschrift eines richtigen *yg)]\f)lg 
nach dem gewohnlichen ygavg; Schulzes Qu. ep. 44S Gdf. *ygaiyg lieSe gen. 
*ygnt(f og erwarten; s. Brugmann IP. 9,372: IS, 429f.; 22, 184: 29, 209; 
vielleicht in Beziehung zu av. zciurv-, zaaru -, etwa ursprgl. nom. *ger-us : 
gen. *g e ro-u-6s , woraus ygayog. Uber lat. gravastelhis s. Yf. LEWb. 1 2 * 352, 
anders Sommer Krit. Erl. 61. Persson Beitr. 301 Anm. 2 ; redupl. yegysgi- 
uog „von selbst abfallende oder reife Feige oder Olive" (s. o.); 

aksl. zwati, zreti „reifen“, zwh, zrvh ,,reif", szzon, „reif"; anord. lor 
..Bettliigrigkeit" (Bugge BB. 3, 119; wegen aschw. gen. Icarwalt alter -ivo- 
St., Persson Beitr. 963); anord. karl „Mann, alter Mann, verheirateter Mann, 
freier, gemeiner Mann" = ahd. kuml „Mann, Ehemann, Geliebter, Brauti- 
gam", mit Ablaut ags. ccorl ., freier Mann der niedrigsten Klasse, Ehemann", 
engl. churl , Bauer, Tdlpel", mnd. kerle „freier, gewohnlicher Mann, kraf- 
tiger Mann", nhd. (aus dem Ad.) Karl-, Gdbed. wohl „alter Mann", /-Suffix 
wie in gr. ygguUog (Noreen Urg. Ltl. 49, Pedersen IvZ. 32, 257). 

Unter einer Gdbed. „verschrumpfte Frucht, Knorren" reihen FickHI 4 
38 f.. Falk-Torp u. kart I auch an anord. kart-nagl, norw. kart m. „unreife 
Frucht. Knorren", ostfries. kret „verschrumpfte Frucht" an, ferner norw. 
mdartl. hark, 1. or pa „dicke, knorrige Rinde", harm „einschrumpfen, sich 
kriiuseln"; doch s. u. *ger- „drehen“. 

In der Bed. ,,Korn, Kern" : gr. ylyagzov „Weinbeerkern“ (aber wegen 
des Yok. und der Bed. ganz fraglich gr. yvgig „feinstes Weizenmehl"; 
s Boisacq 159); lat. granum „Korn, Kern" (*g e rg-nom, = ai. jlrnd-, s. o.) 
= air. gran, cymr. usw. gravm (sg. gronyri) ds. (Entlehnung aus dem Lat., 
A endryes De hib. voc. 145, ist nicht erweislich) = lit. zirnis , lett. sifnis 
,Erbse“, apr. syrne „Korn", aksl. znno, serb. zrno ,,Korn", got. kaum, ahd. 
ags. anord. horn, nhd. Korn, ags. cyrnel „Ivern“, woneben hochstufiges ahd. 
kerno , anord. kjarni (wohl auch nhd. mdartl. kern „Milchrahm“ als der beim 
Buttern kornig werdende, mhd. kern „ButterfaB", anord. kjarni, kirna ds, 
ags. cicrau, engl. clmrn ds., Pick III 4 38, Falk-Torp u. kjerne II). 

Ein *graros (*g e r9-rds) „zerrieben“ ist wohl in lat. gldrea „Kies“ fort- 
gesetzt (s. \ f . LEWb. 2 344), ein d-Praes. *gro-do vielleicht in got. gakro- 
fr>n ,.zermalmen“ (beide nicht wahrscheinlicher zu g«er- „schwer" durcli 
^ ermittlung eines "(/“>•«- „sch\verer Miihlstein"). 

1. gher- ..begehren, gern liaben' , z. T. mit Formen von einer Basis *gherc(i) 

: *gheri- is. zuletzt Persson Beitr. 72S). 

Ai. hdrynlt . findet Gefallen. begehrt' aber nicht hdrsate ..freut sich', 

=== page tag ===
LEAF 609
57009:s  Boisacq 159); lat. granum „Korn, Kern" (*gerg-nom, = ai. jlrnd-, s. o.)
```


## [2026-09-05T20:59:41.041Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=608 && NR<=611 {print \"--- LEAF \"NR-1\" ---\"; print substr($0,1,200)}' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-05T20:59:42.538Z] TOOL RESULT

```
--- LEAF 607 ---
                                     ger-, gere-                                 599

                                                    2
   gr. eyecgco „wecke“ (e- ist nach Brugmann II       3,
--- LEAF 608 ---
600                                                                       g-lier-




durch yi]oa                    und dasselbe i] zeigt ygoam ,.altere“                          (in die them.    K
--- LEAF 609 ---
             ( *yagi-tv
     Gr. yaigco         ), yagfjvat ,.sich freuen",
                                                    yaoig „Anmut, Gunst yaoa
..Freude", yaoondg „Kampfesfreude blitzend"
--- LEAF 610 ---
602                                                        gher-


2. gher- ,,kratzen, ritzen, seharren".
     Gr. yaoddoa „ErdriS, Erdspalte,                        Schlucht"; yagaoom,
```


## [2026-09-05T20:59:49.928Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### SYN granum/corn ###\"; grep -n \"granum\" SYN.txt | head -6\necho \"### SYN old ###\"; grep -n \"zarond\\|jarant\\|geron\" SYN.txt | head -6\necho \"### NYB ###\"; grep -n -i \"zarmān\\|zarman\\|arzan\\|zarwān\\|zurwān\\|zrw\" NYB_vol2_glossary.txt | head -10\necho \"### CHEUNG zar ###\"; grep -n \"zar-\\|\\*zarH\\|jarH\" CHEUNG.txt | head -10"
}
```


### [2026-09-05T20:59:50.015Z] TOOL RESULT

```
### SYN granum/corn ###
12358:Lat. granarium (> It. granaio, Sp, granero, Fr. grenier), usually in pl. gra- naria, fr. granum ‘grain’ (8.42), whence also Fr. grange (> Br. granch) fr. VLat, granica, fem. of an adj. *granicus ‘per- taining to grain’. REW 3839, 3845, Gamillscheg 482.
12706:3. Fr. graine ‘seed’, fr. VLat. grana sg. coll., orig. pl. of Lat. granum ‘grain, kernel’ (8.42).
12935:Lat. granum ‘a grain’, but generic ‘grain’ reflected in grdnarium ‘granary’, and common to the derivs., It., Sp. grano, +4 Fr. grain (> ME greyn, grayn, NE grain), Rum. grine (pl.; sg. griu ‘wheat’), also Du. graan; Goth. kaurn, OE corn, ete., general Gmc. (but NE corn special- A ized to ‘maize’ in U.S.; NHG korn mostly ‘rye’, Sw. korn esp. ‘barley’); but
14687:It. granata, deriv. of Lat. granum ‘grain’, prob. through a plant name. REW 3846.
### SYN old ###
2304:NHG kerl. Perh. as ‘full-grown man’ : | séri- ‘woman, female’) Lat. pibés Grk. yépw, Skt. jarant- ‘old man’. | ‘adult’. Walde-P. 2.83. Ernout-M, Walde-P. 1.600. Falk-Torp 497. | 819f. Kluge-G. 296. 2.22 WOMAN Grk. yur Goth. qiné Lith. moteris, moteriskeé, NG yuvaixa ON kona Zmona Lat. mulier, féemina Dan.  kvinde Lett. steva It. donna Sw. kvinna ChSl. Zena Fr. femme OE cwene, wif, wifman SCr. Zena Sp. mujer ME —  quene, wife, woman Boh. Zena Rum. femeie NE woman Pol. kobieta Tr. ben, fracc Du. vroww Russ. ZenSéina Nir. bean OHG  wib, quena Skt.  jani-, nari-, stri- W. gwraig, benyw, dynes MHG wip Av. Jant-, ndtri-, strz- Br. maouez NHG frau, weib
15279:a 9.60 SMITH IK, NG Nae 5 Goth. aizasmipa Lith.  kalvis lat. faber peers) ON (jarn-)smidr Lett. kalejs I. fabtro Dan. smed ChSl. kovaét R, Sorgeron Sw. smed SCr.  kovaé 8p. herrero OE smip Boh. _kovar * Sdurar, ferar ME smith Pol. Kowal gova NE smith Russ. kuznec gabha Du. — smid Skt. kdrmara-, lohakara- gof OHG  smid he gov MHG smit NHG  schmied
15287:Fr. forgeron, deriv. of forger ‘forge’ (9.61).
24378:Ay. zrvan-, cf. MPers. zarman ‘age, time’, prob. : Av. zaurvan- ‘old age, weakness of age’, Skt. jarant- ‘old, frail’,
24453:oman j e); jarant- ‘not tweak ed b: age’, ete. Fee. bs (NG pop. mahsos, mostly of things; of persons only in de- rogatory sense as matavOpwros worth- less fellow, rascal’), fr. adv. wadau ‘of old, Jong ago’ : THAE, Lesb. mfdue ‘far away’, W. pell ‘far distant’, Skt. carama- ‘the last’, ete, Walde-P. 1.517.
29258:~  Manuighin Du. begeeren (verlangen) Skt. _zs-, las-, vdiich- V. Giiighin OHG  geron Av. 18- Br Ymuno, chwant MHG (be) gern
### NYB ###
665:aržānīk [’le’nyk] worthy 119°; apar-~ exceedingly worthy 924, v.s. v. 'apar. — Paz. arzani; derived from arž through the intermediate adj. aržān ‘worthy’, Ps. len; MPrth ?r2n (S); MPrs 'rz'n (A-H II); Arm. lw. aréan ‘worth(y)’, also
885:1018, 1823-2712, passim; as a real pl. ‘lords’, of princes, noblemen, ete. 2019, — OP Av. (921) baga-, baya-; MPrth bg, pl. bg'n; MPrs by, pl. b?n, bn; MPrth >whrmyzd-bg; MPrs "whrmyzd-by ; by zrw’n (A-H II); Paz. pl. byan (FrP). — In 75! Paz. substitutes vehqn.
902:*bardanya-, SW form of *barzanya- from Av. (950) barazan- ‘top’.
1426:3.8 [the figure l; -’y, -y, -yh] the enel. indef. art.: tigr-é [-1] 339; duxt-ē [BRTH- ^y] 14%; gad-ē [gt'-”y] one stroke with the mace 312°, 4 ēvak-ē [HD-wk!-y] one fourth 998; vāt-ē [-1] 4 hubod 73°; hec ctš-ē [-l] nö 16%; har kas-ē PYS-1] 10018; and cand yašt-ē [-1] 651°; pat har 40 sal hac zan-ē u mart-é frazand-é [al -ē's spelt -1] zāyēt every forthieth year a child is born of a woman and a man (= of one couple) 8622-23; 6 artestäreh for 6 artēštār-ē 4517. — Identical with ?e; MPrs ‘yw placed after its subst.; Paz. -é, NP -é. — The spelling [-1] is sometimes erroneously used for other suffixes -é: mēd4-1 = mode cas. obl. 72??; har marg- arzanik+-1 = -aržānīkē for the abstr. -arzanikéh 10199.
1576:frazand [prznd; inser. plend], fradand [prdnd] child: 1. frazand 6522-25, 661"; with the indef. art. —-e [~ + 1] 86%; ~ varzitan to produce children 67%; pl. cas. rect. ~ 963, 9726, 10514; pl. cas. obl. ~-dn 6913, ~-in [plendyn] F:5. — 2. fra- dand 16, 1013-18, 1119.11.24, 123.12.21.25. 1526 (after numeral). 1676; pl. cas. obl. —-ān 210, 37186 99, 12% 1423-5, [51% 2217, = Av. (1004 sq.) frazanti- ; MPrthPrs frzynd, MPrs also przynd; Ps. plendy; Paz. far- zand frazand; NP farzand. — fradand is the authentic SW form, preserved as an orthographical archaism, and listed in FrP ll with the gl. frazand ; the first -d- of fradand is not a dwarfed z, which only occurs in ideograms, and in the inscript- ions has a form wholly different from d.
2446:marg-aržānīkē [~-yk+1] deadly sin 101, — Cf the spelling mlgle’n'+1 = marg-arzané(h) in the commentary to Vd. 73? (p. 27799).
2551:(Sitz.ber. d. Kön. bay. Ak. d. Wiss. 1890, 2. Bd, 43-84). Hübschmann read the three ws. myhk' [ZY] *plzyn 221 in one: mšk*plzyn, and identified it (AG 192) with Arm maškapačen (P‘aust. Buz. p.78; there in pl.), also maškavarzan (ibd. p. 240), or maš(k)aperčan (Sebčos, not accessible to me), translating them 'the tent of the Great King'. However, these ws., which are manifestly identical but re- present a foreign term imperfactly re- produced, signify ‘accounts’ (mask 'lea- ther’ being the material used for such documents); Nor Bargirk* explains it by the terms hisäb, daftardär, daftarxäneh, and the passages quoted above refer to the regimental treasurer or treasury forming part of the field army. The w. mask (of Ass. origin) never signifies ‘tent’, only ‘skin, leather’. The semantic con- nection between méxak ‘headquarter’ and mex ‘pole’ is obvious.
3793:tóxtan [twhtn'] čož- [twe-] to pay a debt, a fine; to give back, return anything (borrowed): ken tēžēt he will take his revenge 4522, — Cf (Paz.) men hom Ādīnē i xin-xaGh u xin-06é u xin i haft-anbadaa pa farzanda Gēžom (Adino for Adēnāi, xin for ken, anbädaa faulty reading for óbüda = öbätak v. I, XV n. 2) ‘I am Adönäi, desiring revenge and taking revenge, and I shall revenge myself upon the children during seven genera- tions’ SGV XIV, 5-7, reproducing Ex. 20: 5. — MPrth twj- ‘to pay, to atone for’, Ghilain 63; MPrs twzysn ‘penalty, ex- piation'; Paz. 0óxtan 002-; NP toxtan toz-, kin-toz ‘bellicose, one who foments dissension and lawsuits’. — V. also tēg.
4298:xrostan to cry, to shout: 6 didn dévan apar bē xrēst 43'-33; vàng urost 619. — MPrth xrwštn, xrws- (S, A-H III) ‘to call’, MPrs zrwstn, xrwh- (S); NP zurös ‘a loud cry’, xurošidan ‘to shout’; Ghilain 64; Verbum 185; Schaeder, IB I, 254;
4503:zarmän [zlm’n'] (the demon) Old Age 1038; karkās i ~ mēnišn the vulture whose mind is that of this demon, like- minded with him, having the same in- tention as he (inasmuch as he lives on dead bodies furnished by Old Age) 604. — NP zarman ‘an old decrepit man’; abstr. MPrs zrm’nyyh (A—H I).
### CHEUNG zar ###
502:from which the meanings of these languages could have developed, notably *zarH? 
3363:wcl- /wizar-/ ‘to get through’, MMP we’r-, BMP wc /wizär-/ (caus.) ‘to separate, 
3369:divide’. © BMP wel- /wizar-/ is deduced from the reading in KAP ii,28, which 
3371:/wizar-/, is uncertain. BMP wc'l- /wizar-/ with the meaning ‘to fulfil, (accomplish, 
3399:|| (+ *ui-) NP guzardan/guzar- ‘to accomplish [work, job, etc.], perform [e.g. prayer]; 
3401:select, distinguish’. 0 NP guzardan/guzar- with the meaning ‘to fulfil, (accomplish, 
7928:*4-) (old caus.) Sh. aZär- ‘to soak, wet (skin, clothes, etc.) || (+ *niZ-) Sh. nizar-/ 
8834:metathesized variant *yzar- (> Av. yZar-, s.v. *gzar). A different outcome would be 
30260:*zarH2 469 
30263:*zarH! ‘to hurt, wound, anger’
```


## [2026-09-05T20:59:58.022Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '30255,30300p' CHEUNG.txt"
}
```


### [2026-09-05T20:59:58.068Z] TOOL RESULT

```
*PIE— => LIV: - | Pok.: 
*REFERENCES: Skjervo, SVK III: 129 f. 


*zarH2 469 


*zarH! ‘to hurt, wound, anger’ 


*AVESTAN: zar- ‘to hurt, wound’ || (+ *2-) ‘to hurt, wound, offend’ = Liste: 67 f. 
Pres. them. nä-: OPT. 1р1. OAv. zaranaéma (Y 28.9); Caus.: med. 3pl. YAv. äzäraiiente (Yt 13.30), OPT. 
25р. Y Av. azaraiioi$ (FrD 4); Partic.: pres. ania- med. YAv. zaranimna- (Yt 10.47), perf. med. ҮАУ. 
zazarana- (Y 9.30, Yt 11.5), perf. pass. zarata- (Yt 11.5) 

*MIDDLE PERSIAN: (+ *ā-) MMP "z'r-, BMP el /azar-/ (orig. caus.) ‘to torment, 
offend; hurt" > DMMPP: 85a 

Caus.: pres. IND. 3sg. MMP "z'ryd, ’z’ryd, BMP cht /azaréd/, SUBJ. 3sg. MMP "z'r'd, IMPV. 2sg. 
BMP ’c’! /azar/; Inf: BMP ’c’Itn /azardan/; Partic.: pres. MMP ’’z’r’g, perf. pass. BMP ’clt /azard/, BMP 
‘см /azurd/ 


*PARTHIAN: zr- ‘to become angry’ || (+ *a-) ’z’r-, ’’z’r- ‘to injure’ = DMMPP: 
384a, 85a 

Partic.: perf. pass. П zr'd || (+ *a-) Pres.: IND. 3sg. ’z’ryd, 2р1. ’z’ryd, SUBJ. 25р. "z'r'h; Partic.: perf. 
pass. *’’zyrd 

*KHOTANESE: ysurra- ‘wrath’ 

*SOGDIAN: (+ *4-) BSogd. "z'yr ’’z’rt ‘to hurt, trouble’, MSogd. "zyr ‘to offend, 
hurt’ || (+ *upa-) BSogd. ’pz’rn ‘to disturb, afflict (?)’ || (+ *pati-) CSogd. ptzyr- ‘to 
afflict, torment’, MSogd. ptzrn ‘anger’ 

(+ *a-) Caus.: pres. IND. 159. MSogd. "om (BBB: 32), 35р. BSogd. ’’z’yrt, impf. 1sg. MSogd. m’zyrw 
(BBB: 34); Pass.: pres. SUBJ. 3sg. MSogd. "zyry (Sogd.Tales: 469) || (+ *upa-) Pres.: SUBJ. 35р. 
BSogd. ’pz’rn’t || (+ *pati-) Pres.: IND. 35р. dur. CSogd. ptzyrtq, CSogd. “ptzrtq; Impf.: OPT. 3pl. 
CSogd. ptyzyr.nt 

*CHORESMIAN: (+ *à-) m/’zry- ‘to be offended, feel offended’, (caus.) m/’z’ry- ‘to 
offend’, ’z’ryk ‘harm’ || (+ *upa-) pz’r- ‘to blame, rebuke’. 0 Samadi derives the 
Chor. formation pz’r- from *pa-zara(1a)-, with prev. *pa-, whose existence in Ir. was 
already doubted by Henning 1965: 246, fn. 29. The preverb may be rather *pati-, in 
view of CSogd. ptzyr (Sims-Williams 1989: 262). = Samadi: 11, 166
```


## [2026-09-05T21:00:01.027Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"zarH2\" CHEUNG.txt | head\nsed -n '30300,30360p' CHEUNG.txt"
}
```


### [2026-09-05T21:00:01.083Z] TOOL RESULT

```
30260:*zarH2 469 
view of CSogd. ptzyr (Sims-Williams 1989: 262). = Samadi: 11, 166 

*NWIR: Bal. zar ‘anger’ (but Bal. zar ‘lament’ < NP хаг, *zaHr) || (+ *а-) NP 
azurdan/azar- ‘to torment, injure’, NP azar ‘affliction, disease, grieve, vexation, 
injury; [in compounds] tormenting, reproaching’ (LW), Bal. 4zurt/azar- ‘to hurt, 
annoy, vex, molest’ (< NP ?) 

*NEIR: Pash. zor- ‘to vez, distress; blame’ 

*SANSKRIT: har ‘to be angry’ (RV+) > EWAia II: 805 


© No precise IE cognates of this Пг. root are attested. 
*REFERENCES: EVP: 103; DKS: 354a; Werba 1997: 448; NEVP: 102; Shahbakhsh: s.v. azar- 


*zarH? ‘to age, grow old’ 

*AVESTAN: Y Av. zar- ‘to age, grow old’ = Liste: 68 

Partic.: pres. s- (+ priv.) YAv. azarosant- (Yt 19.11, Yt 19.19, Yt 19.23), YAv. azarsant- (Yt 19.89); 
Partic.: perf. pass. zarata- ‘old’ (V 3.13, P 22) 


*MIDDLE PERSIAN: MMP zrd ‘infirm (from old age)’ > DMMPP: 384a 


470 *zarH3 


*KHOTANESE: ysir- (ysad-) ‘to become old’ => SGS: 113 

*NWIR: NP zal PN (in Shahn.), also ‘old (wo)man’ 

*NEIR: Oss. z&rond ‘old’, Pash. zor (m.), хага (Ё), Yi. zor ‘old (of people)’ 

*MISC: Orm. zal ‘old’ (LW ?) 

*SANSKRIT: jar’ ‘to age, grow old’ (RV+) > EWAia I: 577 

© This root has an impeccable IE etymology. 

«PIE *gerH>- ‘to age, grow old’ = LIV: 165 f. | Pok.: 390 f. 

*IE COGNATES: Gr. eynpa ‘became old’, Gr. yfipag ‘old age’, Gr. yepwv (m.) ‘old 
man’, Arm. cer ‘old; old man’, OCS ss-zpreti “о ripen’ 

*REFERENCES: IIFL I: 413b; DKS: 346b; Abaev, Slovar’ IV: 304 f.; Werba 1997: 289 f.; NEVP: 103 


*zarHË ‘to bewail the deceased, 5: JS ex ull” 

*MIDDLE PERSIAN: MMP zryg, BMP zlyk /zarig/ 'sorrow, suffering! (LW) 
c DMMPP: 380a 

*PARTHIAN: Z'r, Zryg ‘sorrow, suffering? > DMMPP: 380a 

*KHOTANESE: LKh. ysär- ‘to sing’, ysera- ‘wretched’. 0 On ysirum ‘wretched’ (not 
‘loud’, DKS: 353a) see Skjerve, SVK I: 107. © SGS: 112 

*SOGDIAN: BSogd. z’ry, z’r’k, z’r’y ‘compassionate; pitiful’, CSogd. z’ry (indecl.)
```


## [2026-09-05T21:00:09.741Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '30360,30390p' CHEUNG.txt"
}
```


### [2026-09-05T21:00:09.788Z] TOOL RESULT

```
*SOGDIAN: BSogd. z’ry, z’r’k, z’r’y ‘compassionate; pitiful’, CSogd. z’ry (indecl.) 
‘pitiful, pitiable, sympathetic’ 

*CHORESMIAN: zry- ‘to announce, reveal, speak about (sorrow)? > Samadi: 264 
*NWIR: NP zaridan ‘to weep, moan’ (LW), Bal. zarit/zar- ‘to be uneasy, pine for’, zar 
‘lament’? (< NP) || (+ *a-) Kurd. azar (f.) (Kurm.) ‘weeping, crying’, (Sor.) 
‘suffering’ 

*NEIR: Oss. I. zælyn/zæld ‘to sound’, І. zaryn/zard, D. zarun/zard (caus.-iter.) ‘to 
sing’ || (+ *aua-) Oss. I. uzalyn/uzeld ‘to nurse, tend; to coax; to show attention; to 
do something nice; to regale’ || (+ *a-) Oss. I. azelyn/azzld, D. azeelun/azaeld ‘to 
give sound, echo’ 

*MISC: Georg. (LW) zar-i ‘horror’, Abkh. (LW) a-zar ‘songs at memorial feast’ 

9 The Ir. forms appear to refer to the bewailing ceremony performed in memory/ 
honour of the deceased: this usually involves singing, comforting, calling and ritual 
lamentation (etc.). Ir. *zarH (connected to Skt. jar ‘to sing’ ?) should therefore be 
separated from *garH!, Skt. gar ‘to greet, praise’, which rather refers to the 
welcoming cermony given to a guest. 

«PIE *g(e)rH>- ‘to bewail the deceased (i.e. through lamenting, calling, singing (etc.) 
in honour/memory of the deceased)’ = LIV: 161 | Pok.: 352 

ЈЕ COGNATES: Gr. үйрос ‘voice’, Olrish -gair ‘to call’, OE cearu ‘sorrow, care’, 


Engl. care 
*REFERENCES: Abaev, Slovar’ I: 96 Ё; DKS: 349a f., 355a; Abaev, Slovar’ IV: 295 f., 23 f., 288 f£; 
Cabolov 2001: 105; Shahbakhsh: s.v. zar-; Korn 2005: 206, 379
```


## [2026-09-05T21:00:21.229Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### HUB zal/zar ###\"; grep -n \"zāl\\|zal '\\|zarman\\|zaurvan\" HUB.txt | head -10\necho \"### SKT corn/churl/granite ###\"; grep -n \"^Corn,\\|^Churl,\\|^Granite\\|^Grain,\" SKT.txt | head\ngrep -n -i \"granite, a hard\\|Corn (1)\\|Churl\" SKT.txt | head -8"
}
```


### [2026-09-05T21:00:21.315Z] TOOL RESULT

```
### HUB zal/zar ###
2422:659. Np. zarman 'senex deerepitus' ist allerdings == skr. jari-
2424:zaurvan- nach Bartholomae). Aber np. »arvan
2430:(d. i. zruvan-) *Zeit*. Np. zaman ist nicht aus zarman
### SKT corn/churl/granite ###
16864:surly,  proud,  churlish.  (F.-L.;  witk £.  svjix.)  Formerly  terfy  (Levins) ;  also Cfv:^,  SpCDicr,  Shep.  KaL  July,  aoj,    PbI
```


## [2026-09-05T21:00:22.516Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"ارزن\" \"زیره\" \"زال\" \"زرتشت\"; do echo \"=== ARY $w ===\"; grep -n \"$w\" incoming/ARY/ARY_pages.txt | head -4; done"
}
```


### [2026-09-05T21:00:24.291Z] TOOL RESULT

```
=== ARY ارزن ===
=== ARY زیره ===
344:جزیره) ایبری (اسپانیا و پرتغال) سنگك نیشته‌هایی پدست آمده که به یکك زبان غیر هند و اروپایی قبل
736:چندین دهه قبل» کاوشگران حدود سه هزار خشت سفالی دارای نوشتار در جزیره‌ی کرت و :
787:دریای سیاه کوج کرده بودند ولی در قرن چهارم میلادی توسط اقوام «هان» (11015) به شبه جزیره‌ی
809:شبه‌جزیره) بالکان به زیستگاه کنونی خودکو جکردند چون علاوه بر شواهد باستانشناسی و زبانشناسی
=== ARY زال ===
460:اتزال وا 010 0۷ | ۵0 ۲
2545:۱ واژه‌ی "ستور" هم ازالهمین ريشه است,
2941:51 ,۷271405 آلمانی ((05/0/۸): زالان
3868:۳ (0 07۳۵۵ نررژی (/۸ا۸/07750): زال۱1۹
=== ARY زرتشت ===
713:را وابسته به خود زرتشت می‌دانند و تاریخ حدود ۹۰۰ سال پیش از میلاد را برای زرتشت و کتابش
967:۱-روحانیون زرتشتی ۲- جنگاوران ۳- دهگانان.
1144:زرتشتی است. بخش قدیمی‌تر آن (گاتها) در سده‌های پازدهم تا ششم پیش از میلاد یعنی دوران کوج
8747:۲- هلت دگرگرنی چم این واژه در زبان‌های ایرانی این است که پس از ظهور زرتشت و آئین او "آهورامزدا" مورد
```


## [2026-09-05T21:00:29.430Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2415,2440p' HUB.txt\necho \"=== leaf ===\"\nawk 'BEGIN{RS=\"\\f\"} /659\\. Np\\. zarman/{print \"LEAF \"NR}' HUB.txt\necho \"=== ARY 3868 ctx ===\"\nsed -n '3860,3875p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-05T21:00:31.152Z] TOOL RESULT

```
656. N6ldeke hat Recht, np. zard gelb = ap. ^zarta-
(= zd. "^zareta- fiir zairita-) zu setzen. Dazu arm.
zartagoin (gelb-farbig') gelbe Blume zum Farben
dienend'.
657. Wo findet sich np. zurd, zurt 'Art Hirse? Arab. Surat
geh5rt nicht hierher.
658. Als »ganz unsicher** zu streichen.
659. Np. zarman 'senex deerepitus' ist allerdings == skr. jari-
man- 'hohes Alter und verwandt mit zd. zaurva-- (Thema
zaurvan- nach Bartholomae). Aber np. »arvan
'tempus' ist zoroastrisch = paz. zurvan *time* Shk. 275,
phi. zruvan Gl. and Ind. 148, arm. LW. Zruan (=
Zrvan) die Zeit als Urwesen, dessen S5hne Ormizd
und Arhmn waren, gr. Zovgovafx^ syr. Zurvan (N5ldeke,
syrische Polemik gegen die pers. Religion), zd. zrvan--
(d. i. zruvan-) *Zeit*. Np. zaman ist nicht aus zarman
entstanden, vgl. arab. zaman, zamCLn *Zeit', hebr. chald.
zeman *Zeit' (AT.), np. zamana *Zeit' = phi. zamCLnak,
arm. Samanak 'Zeit, Alter, Gelegenheit*.
660. Im Pehlevi ist wohl zreh = zreh, paz. zreh, arm.
zrah-fc zu lesen.
661. Np. zaryun bedeutet auch 2) viridis et amoenus —
afgh. zaryun green, verdant, fresh'.— 70 —
662. Np. ziSt 'hassHch, abscheulich' stellt Fr. Mtiller,
WZKM. 8, 96 zu zd. zdiMa- unrein', zdisnu- ^), zdista-
(nur in vizdiSta-f var. mzvdiSta- vd. 8, 10?), wie schon
=== leaf ===
LEAF 80
=== ARY 3868 ctx ===
پارسی‌پاستان (۷/ماق۳88 صا0): 0 آلمانی کهن (/(4۸ل082 7ا0ابز صام):
پهلری (۲1ماتله): 3/0 ۸ ,8۸1
کردی (0201577): 882101 ,8885710 آلمانی (088010): 0
آفغانی (پشنی) (017۸2/7): رانا انگلیسی کهن (4ل3لا80 طا۵):
سانسکریت (5/57877): ,210 0۸ ,815270
۱ 8۸011۸ انگلیسی (8لا8(0): 0
ده یونانی (080): 4 مف۳51526 دانمارکی (0۸(75/7): زرل ۱1۲۲
ُ ان 430 ,08785 3800 سوئدی (91/821327): رال
۳ (0 07۳۵۵ نررژی (/۸ا۸/07750): زال۱1۹
فرانسه (۳5۸/۳17): 0 هلندی (01۴17): 30
اسپانپایی (۸۸71577ط5): ۸0 لیتوانی (4لل 177 ). 30
ایتالیایی (متهت): 00 ایرلندی (3[7ل)): ان لد از
گرتیک (0077710): ازال ۱
ایسلندیکهن (/0701007۵م50 صا0): 8۸770
۳
[pdf page 133]
```


## [2026-09-05T21:00:41.366Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"### abadis گرانیت ###\"; grep -n -i -A6 \"معین\" 969b49a7f2a684fa.txt | head -40\necho \"### abadis ارزن ###\"; grep -n -i -A6 \"معین\" 66e8513c1a917555.txt | head -40"
}
```


### [2026-09-05T21:00:41.431Z] TOOL RESULT

```
### abadis گرانیت ###
21: فرهنگ معین
22-
23- (گِ ) [ فر. ] (اِ. ) سنگ خارا. 
24-
25- فرهنگ عمید
26-
27- سنگ خارا. 
--
69: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
70-
71- لینک ها 
72-
73- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
74-
75- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
### abadis ارزن ###
49: فرهنگ معین
50-
51- (اَ زَ ) [ په . ] (اِ. ) گیاهی از تیرة گندمیان دارای ساقه های کوتاه و دانه های ریز، دانه های آن را بیشتر به طیور می دهند. غالباً بعد از برداشت حاصل جو و گندم کاشته می شود. 
52-
53- فرهنگ عمید
54-
55- گیاهی از تیرۀ گندمیان با بوتۀ کوچک، ساقه های کوتاه و نازک، و دانه های ریز که بیشتر خوراک پرندگان است و گاهی از آرد آن نان می پزند. 
--
94:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
95-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
96-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
97-
98- اَرزَن در زبان پارسی پهلوی نشانه داشتن توانمندی بسیار علیرغم کوچکی است. یک دانه ریز و کوچک می تواند گیاهی با دانه های فراوان و خوراکی بسیار را فراهم کند. باید گفت که شوربختانه پس از یورش بیگانگان عرب و 
99- ... [مشاهده متن کامل] چنگیز و تیمور، نه تنها ما ایرانیان واژگان زبان و خودشناسی و همدیگر شناسی را از دست داده ایم که بر پایه چیم واژگان نیز می توان گفت که با یورش این بیگانگان، شیوه اندیشیدن ما ایرانیان از اَستیگ ( ) اندیشی به اَنَستیگ ( - ) اندیشی گراییده است چنانچه گویی یک دگرگونی شگرف بداندیشی در مغزهایمان رخ داده و اندیشه هایمان را از روشنایی به تاریکی سُوگ ( نه سُوق که معرّب همین واژه پارسی است ) داده است. برای نمونه ما در نام های شهرها و روستاهای میهنمان اوشتُورینان ( مقاوم کننده ) ، بُوزینان ( بُزینان: نجات بخش ) و ماهینان ( ؟ ) را داریم و نام های مارال ( خوش خط و نگار چون مار؛ دختر زیباروی ) و ماریون ( با همان چیم مارال، دختر زیباروی ) و مارالان ( جای دختران خوش خط و نگار، نام محله ای در تابریز یا تاوریز یا تاوریژ یا تبریز کنونی ) و نام بوزینَگ ( بوزینه، نجات بخش ) را داشته ایم که از یادگارهای زبان و فرهنگ و بینش ما ایرانیان پیش از یورش اعراب به ایران هستند که در همه این واژگان به جنبه مثبت جانداران نگریسته شده است و نه زانوی چرک و بدن کج شتر! و نیش و زهر مار! و نه بوزینه بسان یک جانور با چهره زشت و واژه ای برای ناسزا گفتن به کسی دیگر! که همه نشان از پندار نیک، گفتار نیک و کردار نیک هستند. ما اَرزن را چنان می شناخته ایم که کوچک و پُربازده و توانمند است و نه کوچک و خوار! آنچنان که بیشترمان و خودم نیز امروزه چنین می پنداریم. اکنون می بینید چه اندازه اندیشه و جهان بینی ما زشت شده است. این داستانی است که واژه ها به ما می گویند و روشن است که همین دگرگونی در پَریون ( ماورای ) واژگان در شیوه نگرش ما ایرانیان و شاید دیگر ایرانشهریگان به دیگر خیرهای ( موضوعات ) زندگی نیز رُخ داده است.
100-
--
188: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
189-
190- لینک ها 
191-
192- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
193-
194- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است.
```


## [2026-09-05T21:00:53.904Z] TOOL CALL #60: Bash

```json
{
 "command": "ls site/pages/174.jpg 2>/dev/null; pdftoppm -f 174 -l 174 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg174 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T21:00:56.239Z] TOOL RESULT

```
site/pages/174.jpg
total 23752
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 17:00 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb  163996 Sep  5 16:46 gar2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124975 Sep  5 16:47 gar3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77205 Sep  5 16:46 gar.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb    4344 Sep  5 16:49 n12b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3969 Sep  5 16:49 n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2692 Sep  5 16:49 n16.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   57139 Sep  5 16:54 pg179.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81598 Sep  5 16:58 pg180.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56794 Sep  5 17:00 pg181.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77310 Sep  5 16:58 pg184.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top598.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top599.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top601.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24918 Sep  5 16:58 tops2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  5 16:57 tops.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T21:00:59.336Z] TOOL CALL #61: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg174.png"
}
```


### [2026-09-05T21:00:59.710Z] TOOL RESULT

```

```


## [2026-09-05T21:00:59.706Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T21:01:14.458Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npdftoppm -f 174 -l 174 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf p174hi\npython3 -c \"\nfrom PIL import Image\nim=Image.open('p174hi.png'); print(im.size)\nw,h=im.size\n# node 17 germanic box: approx y 1200/1290 of 2200-scale -> fraction\nim.crop((int(0.20*w),int(0.535*h),int(0.80*w),int(0.575*h))).save('n17.png')\nim.crop((int(0.50*w),int(0.290*h),int(0.80*w),int(0.325*h))).save('n5.png')\n\"\nls -la n17.png n5.png"
}
```


### [2026-09-05T21:01:18.969Z] TOOL RESULT

```
(5100, 6600)
-rw-rw-r-- 1 sfmqrb sfmqrb 6463 Sep  5 17:01 n17.png
-rw-rw-r-- 1 sfmqrb sfmqrb 3215 Sep  5 17:01 n5.png
```


## [2026-09-05T21:01:21.492Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/n17.png"
}
```


### [2026-09-05T21:01:21.573Z] TOOL RESULT

```

```


## [2026-09-05T21:01:21.568Z] INPUT

[Image: original 3060x263, displayed at 2000x172. Multiply coordinates by 1.53 to map to original image.]


## [2026-09-05T21:01:22.195Z] TOOL CALL #64: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/n5.png"
}
```


### [2026-09-05T21:01:22.208Z] TOOL RESULT

```

```


## [2026-09-05T21:01:27.571Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npython3 -c \"\nfrom PIL import Image\nim=Image.open('p174hi.png'); w,h=im.size\nim.crop((int(0.18*w),int(0.575*h),int(0.55*w),int(0.615*h))).save('n17b.png')\nim.crop((int(0.55*w),int(0.310*h),int(0.80*w),int(0.345*h))).save('n5b.png')\n\""
}
```


### [2026-09-05T21:01:29.821Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T21:01:32.272Z] TOOL CALL #66: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/n17b.png"
}
```


### [2026-09-05T21:01:32.285Z] TOOL RESULT

```

```


## [2026-09-05T21:01:33.026Z] TOOL CALL #67: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/n5b.png"
}
```


### [2026-09-05T21:01:33.041Z] TOOL RESULT

```

```


## [2026-09-05T21:01:38.665Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npython3 -c \"\nfrom PIL import Image\nim=Image.open('p174hi.png'); w,h=im.size\nim.crop((int(0.20*w),int(0.600*h),int(0.45*w),int(0.630*h))).resize((int(0.25*w*1.2),int(0.03*h*1.2))).save('n17c.png')\nim.crop((int(0.62*w),int(0.325*h),int(0.80*w),int(0.352*h))).save('n5c.png')\n\""
}
```


### [2026-09-05T21:01:40.790Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T21:01:44.004Z] TOOL CALL #69: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/n17c.png"
}
```


### [2026-09-05T21:01:44.019Z] TOOL RESULT

```

```


## [2026-09-05T21:01:44.235Z] TOOL CALL #70: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/n5c.png"
}
```


### [2026-09-05T21:01:44.248Z] TOOL RESULT

```

```


## [2026-09-05T21:02:01.297Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"gravy,  n\\.\" KLN_1966.txt | head -3\necho \"--- BQT زیره با ---\"\nawk 'BEGIN{RS=\"\\f\"} index($0,\"زیره با\") || index($0,\"زیرها\"){print \"LEAF \" NR-1}' BQT_v2_pages.txt | head\ngrep -n \"زیره‌با\\|زیره با\\|زیرباج\" BQT_v2_pages.txt | head -5"
}
```


### [2026-09-05T21:02:03.089Z] TOOL RESULT

```
16631:gravy,  n.  —  ME.  graue  (pronounced  grave),  from misreading  of  OF.  grane,  ‘a  dish  powdered  with grains’,  lit.  ‘grained’,  fr.  ML.  granatus ,  pp.  of grcinare ,  ‘to  grain’,  fr.  L.  granum,  ‘grain’.  See grain,  ‘seed,  corn’.
--- BQT زیره با ---
LEAF 24
LEAF 208
```


## [2026-09-05T21:02:10.250Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==209' BQT_v2_pages.txt | grep -o \".\\{0,120\\}زیره با.\\{0,160\\}\"\necho \"---- search زیره in v2 around leaf 490-520 ----\"\nawk 'BEGIN{RS=\"\\f\"} NR>=485 && NR<=520 && index($0,\"زیره\"){print \"LEAF \" NR-1}' BQT_v2_pages.txt | head"
}
```


### [2026-09-05T21:02:14.547Z] TOOL RESULT

```
ugrep: error: error at position 91
n\x80-\xbf][\x80-\xbf]*){0,160}
  exceeds complexity limits___/


---- search زیره in v2 around leaf 490-520 ----
```


## [2026-09-05T21:02:17.082Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==209' BQT_v2_pages.txt | python3 -c \"\nimport sys\nt=sys.stdin.read()\ni=t.find('زیره با')\nprint(t[max(0,i-200):i+300])\""
}
```


### [2026-09-05T21:02:19.119Z] TOOL RESULT

```
 ‫‪Yg‬‬     ‫~‪m‬‬                                                                                      ‫‪‎‬هرو‬


‫بمعنی‬   ‫‪ -‬بر وزن رسیدن »‬         ‫خسدن‬                      ‫خسوره ه بم اول وفتح رای قرشت؛‬
‫استت که در زیر «ندان ترم کردن‬           ‫خایدن‬              ‫یمضی خور استت که پدر
```


## [2026-09-05T21:02:26.058Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"زیره‌با\\|زیرهبا\\|زیره با\" MON_part1.txt MON_part2.txt RCH.txt 2>/dev/null | head -5\npython3 - <<'EOF'\nimport re\nfor f in ['MON_part1.txt','MON_part2.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for m in re.finditer('زیره',t):\n        s=t[m.start()-60:m.start()+120].replace('\\n',' ')\n        if 'با' in s[60:90]:\n            print(f, '|', s); break\nEOF"
}
```


### [2026-09-05T21:02:27.821Z] TOOL RESULT

```
MON_part1.txt |  مصر علیا و سواحل نیل است و در ایران نیز  کشت می‌شود. ريشةٌ زیره دراز و باریک  مابل به رنگ سفید و ساقه‌اش راست و  منشعب و به تقسیمات دوتایی و خطدار  است. سس رک‌هایش متناوب و شفاف و
MON_part2.txt | یی تند و مزه‌ای تلخ دارد و دانه‌هایش سیاه  رنگ و ریز و شیبه زیره می‌باشد؛ کون بری»  عذبه» قرامن کیمیونی. کمون کوهی: (گٌیا.)  گیاهی است از تبرهة چتربان که دارای  برگ‌های مرکب شانه‌ی
```


## [2026-09-05T21:02:34.927Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -m1 -A6 \"granite(n\" 013e05c07e6ba085.txt | head -20\necho \"---corn---\"; grep -n -m1 -A8 \"corn(n\" bee7b79c6299f51b.txt | head -20\necho \"---churl---\"; grep -n -m1 -A6 \"churl(n\" 3e1637a32174fff2.txt | head -16"
}
```


### [2026-09-05T21:02:35.006Z] TOOL RESULT

```
---corn---
---churl---
```


## [2026-09-05T21:02:48.231Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 013e05c07e6ba085 bee7b79c6299f51b 3e1637a32174fff2; do echo \"=== $f ===\"; sed -n '1,5p' $f.txt; sed -n '6,40p' $f.txt | head -30; done"
}
```


### [2026-09-05T21:02:50.172Z] TOOL RESULT

```
=== 013e05c07e6ba085 ===
URL: https://www.etymonline.com/word/granite
FETCHED: 2026-09-05T20:54:31Z
STATUS: 200
TITLE: Granite - Etymology, Origin & Meaning

Granite - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of granite 

 granite (n.) 

 1640s, from French granit(e) (17c.) or directly from Italian granito "granite," originally "grained," past-participle adjective from granire "granulate, make grainy," from grano "grain," from Latin granum "grain" (from PIE root *gre-no- "grain"). In reference to the appearance of the rock. Used figuratively for "hardness" (of the heart, head, etc.) from 1839. New Hampshire, U.S., has been the Granite State at least since 1825.
 also from 1640s 

 Entries linking to granite 

 granitic (adj.) 

 1749, from granite + -ic .

 *gre-no- 

=== bee7b79c6299f51b ===
URL: https://www.etymonline.com/word/corn
FETCHED: 2026-09-05T20:55:06Z
STATUS: 200
TITLE: Corn - Etymology, Origin & Meaning

Corn - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of corn 

 corn (n.1) 

 [grain], Old English corn "single seed of a cereal plant; seeds of cereal plants generally; plants which produce corn when growing in the field," from Proto-Germanic *kurnam "small seed" (source also of Old Frisian and Old Saxon korn "grain," Middle Dutch coren , German Korn , Old Norse korn , Gothic kaurn ), from PIE root *gre-no- "grain."

 The sense of the Old English word was "grain with the seed still in" (as in barleycorn ) rather than a particular plant. Locally understood to denote the leading crop of a district. It has been restricted to the indigenous maize in America (c. 1600, originally Indian corn , but the adjective was dropped), usually "wheat" in England, "oats" in Scotland and Ireland, while Korn means "rye" in parts of Germany.

 Maize was introduced to China by 1550, it thrived where rice did not grow well and was a significant factor in the 18th century population boom there. Corn-starch is from 1850. Corn-silk is attested from 1852.

 corn (n.2) 

 "hardening or thickening of skin," early 15c., corne , from Old French corne (13c.) "horn (of an animal)," later "a corn on the foot," from Latin cornu "horn of an animal," from PIE root *ker- (1) "horn; head."

 Latin cornu was used of many things similar in substance or form to the horns of animals and of projecting extremities or points: It could mean "a wart, a branch of a river, a tongue of land, the end of a bow or sail-yard, the peak of a mountain, a bugle, a wing of an army," or "the stiff hair of the Germans."
=== 3e1637a32174fff2 ===
URL: https://www.etymonline.com/word/churl
FETCHED: 2026-09-05T20:55:07Z
STATUS: 200
TITLE: Churl - Etymology, Origin & Meaning

Churl - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 

 Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.

 About
 Who Did This 
 Sources 
 Introduction 
 Links 

 Support
 Premium 
 Patreon 
 Donate with PayPal 
 Merch 

 Apps
```


## [2026-09-05T21:03:06.396Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"POMEGRANATE [a-z()@-]*\" AHD_watkins1985.txt | head -3\ngrep -o \"GRAVY [a-z()@-]*\" AHD_watkins1985.txt | head -3\ngrep -o \"GRAIN [a-z()@-]*\" AHD_watkins1985.txt | head -3\npython3 tools/fetch_source.py \"https://www.etymonline.com/word/Charles\" --note \"page 174, Carl/Charles\" 2>&1|tail -1"
}
```


### [2026-09-05T21:03:08.098Z] TOOL RESULT

```
GRAIN gre-no-
python3: can't open file '/home/sfmqrb/git/rishe/data/verification/sources/refs/tools/fetch_source.py': [Errno 2] No such file or directory
```


## [2026-09-05T21:03:12.650Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"POMEGRANATE[^ ]* [a-zA-Z()@ -]\\{0,20\\}\" AHD_watkins1985.txt | head -3\ngrep -o \"GRAVY [a-zA-Z()@-]*\" AHD_watkins1985.txt | head -3\ngrep -n \"pomegranate\\|Pomum\" AHD_watkins1985.txt | head -5\npython3 tools/fetch_source.py \"https://www.etymonline.com/word/Charles\" --note \"page 174, Carl/Charles\" 2>&1|tail -1"
}
```


### [2026-09-05T21:03:14.319Z] TOOL RESULT

```
python3: can't open file '/home/sfmqrb/git/rishe/data/verification/sources/refs/tools/fetch_source.py': [Errno 2] No such file or directory
```


## [2026-09-05T21:03:17.239Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ngrep -o \"POMEGRANATE.\\{0,20\\}\" data/verification/sources/refs/AHD_watkins1985.txt | head -3\ngrep -o \"GRAVY.\\{0,20\\}\" data/verification/sources/refs/AHD_watkins1985.txt | head -3\npython3 tools/fetch_source.py \"https://www.etymonline.com/word/Charles\" --note \"page 174, Carl/Charles\" 2>&1|tail -1"
}
```


### [2026-09-05T21:03:39.065Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d85f7ad7ca600889.txt
```


## [2026-09-05T21:03:43.728Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -m1 -A4 \"Charles\" d85f7ad7ca600889.txt | sed -n '1,20p'; grep -n \"masc. proper name\\|Old High German\\|Karl\" d85f7ad7ca600889.txt | head -5"
}
```


### [2026-09-05T21:03:43.786Z] TOOL RESULT

```
1:URL: https://www.etymonline.com/word/Charles
2-FETCHED: 2026-09-05T21:03:39Z
3-STATUS: 200
25: masc. proper name, from French Charles , from Medieval Latin Carolus , from Middle High German Karl , literally "man, husband" (see carl ).
31: c. 1300, "bondsman; common man, man of low birth," from Old Norse karl "man" (as opposed to "woman"), "male, freeman," from Proto-Germanic *karlon- (source also of Dutch karel "a fellow," Old High German karl "a man, husband"). The same Proto-Germanic source produced Old English ceorl "man of low degree" (see churl ) and the masc. proper name Carl and, via French and Latin, Charles .
37: masc. proper name, from Old French Andreu (Modern French André ), from Late Latin Andreas (source also of Spanish Andrés , Italian Andrea , German Andreas , Swedish and Danish Anders ), from Greek Andreas , a personal name equivalent to andreios (adj.) "manly, masculine, of or for a man; strong; stubborn," from anēr (genitive andros ) "man" (from PIE root *ner- (2) "man").
```


## [2026-09-05T21:04:31.033Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg174.png data/verification/sources/refs/ocr/BOOK/174.png\nls -la data/verification/sources/refs/ocr/BOOK/ | head"
}
```


### [2026-09-05T21:04:32.613Z] TOOL RESULT

```
total 6204
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  5 17:04 .
drwxrwxr-x 11 sfmqrb sfmqrb   4096 Sep  5 16:42 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-05T21:04:48.068Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '1,5p' 46f7d14c9ced9d81.txt; python3 -c \"\nt=open('46f7d14c9ced9d81.txt',encoding='utf-8').read()\nimport re\ni=t.find('Zurvanism')\nprint(t[i:i+1200])\""
}
```


### [2026-09-05T21:04:50.344Z] TOOL RESULT

```
URL: https://www.iranicaonline.org/articles/zurvanism
FETCHED: 2026-09-05T20:58:17Z
STATUS: 200
TITLE: ZURVANISM - Encyclopaedia Iranica

Zurvanism, or the Zurvanite myth, were already given by him, even though not all later scholars cared to refer to his contributions (see Rezania, 2010, pp. 12-24, for a much fuller discussion of the history of the study of Zurvanism than can be given here).
 After Spiegel, Zurvanism became a standard subject in discussions of Zoroastrianism. Some scholars thought of it as a pre-Zoroastrian (Median) religion that was brought into Zoroastrianism with the conversion of the Medes to that religion (Nyberg, 1938, p. 388; Widengren, 1938, pp. 271-74) or as the religion of the Parthians (Widengren 1955, pp. 88-89). Others rightly stressed the fact that almost all sources are from the Sasanian period and saw a special role for the Sasanian kings as supporters of a Zurvanite version of Zoroastrianism (Christensen, 1944, pp. 150-55). Two discoveries considerably widened the discussion in the early twentieth century. The first was the discovery of Manichean Middle Persian texts from Central Asia, in which the Father of Greatness, the supreme God of the Manichean pantheon, was (sometimes) called Zurvān, suggesting a similar role for this god in third century Persian Zoroastrianism (see below).
```


## [2026-09-05T21:11:29.373Z] TOOL CALL #83: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build174.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_PIE  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5erh%E2%82%82-\"\nW_GRAN = \"https://en.wiktionary.org/wiki/granite\"\nE_GRAN = \"https://www.etymonline.com/word/granite\"\nW_ZAL  = \"https://en.wiktionary.org/wiki/%D8%B2%D8%A7%D9%84\"\nW_ZIRE = \"https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D8%B1%D9%87\"\nW_ARZ  = \"https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%B2%D9%86\"\nW_ZAR  = \"https://en.wiktionary.org/wiki/%D8%B2%D8%B1\"\nW_ZORO = \"https://en.wiktionary.org/wiki/Zoroaster\"\nW_ZARA = \"https://en.wiktionary.org/wiki/Zarathustra\"\nW_JIRK = \"https://en.wiktionary.org/wiki/%E0%A4%9C%E0%A5%80%E0%A4%B0%E0%A4%95\"\nW_JIRN = \"https://en.wiktionary.org/wiki/%E0%A4%9C%E0%A5%80%E0%A4%B0%E0%A5%8D%E0%A4%A3\"\nE_CORN = \"https://www.etymonline.com/word/corn\"\nE_CHAR = \"https://www.etymonline.com/word/Charles\"\nI_AZAR = \"https://www.iranicaonline.org/articles/azarmigduxt\"\nI_ZURV = \"https://www.iranicaonline.org/articles/zurvanism\"\nA_GRAN = \"https://abadis.ir/fatofa/%DA%AF%D8%B1%D8%A7%D9%86%DB%8C%D8%AA/\"\nA_ARZ  = \"https://abadis.ir/fatofa/%D8%A7%D8%B1%D8%B2%D9%86/\"\n\nPOK_Q = (\"POK_full.txt / POK_02 leaf 46: 'Root/lemma: ger-, gera-, gre-. Meaning: to rub; to be old; grain … \"\n         \"Page(s): 390-391'; the same article gives Lat. granum (*gr-nom), Got. kaurn/OE corn, ON karl/OHG karal \"\n         \"and Av. zaurvan-, zarata-, azarama-, npers. zar/zal.\")\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan / Old Persian\",\n \"words\": \"zar 2; zarmân; zarwân, zaurva; â-zarema-dugedâ; zara-uštra\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n   \"Av. zar- 'to age, grow old' (YAv. participles azarəsant- 'not ageing', zarəta- 'old') is the regular Iranian \"\n   \"reflex of PIE *ǵerh₂-: the palatal *ǵ gives Proto-Iranian *ź > Av./OIr. z, exactly as in Skt. jṝ / járati. \"\n   \"Cheung (Etym. Dict. of the Iranian Verb, s.v. *zarH2, pp. 469-70) calls the IE etymology of this root \"\n   \"'impeccable'. 'zaurva' is Av. zauruua-/zaurvan- 'old age, decrepitude' (Bartholomae col. 1682 'j. zaurvan- m. \"\n   \"Greisenalter, Altersschwäche'), from *ǵorh₂-wó-; the same stem gives Av. zaurura- 'decrepit'. 'zarwân', \"\n   \"however, is not Avestan but Parthian zrwʾn /zarwān/ and Book-Pahlavi zarwān 'old age' (MacKenzie p. 100), \"\n   \"and 'zarmân' likewise is Middle Persian zarmān 'old man; decrepitude' (MP zlmʾn', Man. MP zrmʾn) = Skt. \"\n   \"jariman- < *ǵérh₂-mn̥ — both are Middle-Iranian, not Old-Iranian, forms sitting in an 'Avestan/Old Persian' \"\n   \"box. 'â-zarema-dugedâ' is not an attested Avestan compound: Avestan has the adjective azarəma- 'not \"\n   \"decreasing/not ageing' (Pokorny 390: 'av. azarəma- „nicht abnehmend“, von *zarəma- m.'), and Moʿin, in \"\n   \"his footnote to Borhān-e Qāṭeʿ p. 36, builds *a-zarəma- + dugdā 'daughter' to explain Āzarmīdoxt; the compound \"\n   \"itself is a modern reconstruction. 'zara-uštra' = Av. Zaraθuštra-, second member uštra- 'camel' (undisputed); \"\n   \"for the first member Bartholomae (col. 1670) posits *zarant- 'old' (: Skt. járant-, Osset. zærond), eig. \"\n   \"'dessen Kamele alt sind' — i.e. Nourai's gloss follows Bartholomae, while Moʿin prefers 'yellow camels' \"\n   \"(see the chart's own NOTE, evaluated at node 2).\"),\n \"derivation_fa\": (\n   \"ستاک اوستایی zar- «پیر شدن، فرسوده شدن» (با صفت‌های azarəsant- «پیرنشونده» و zarəta- «پیر») بازتاب منظم ریشهٔ \"\n   \"هندواروپایی آغازین *ǵerh₂- است؛ کام‌شدهٔ *ǵ در ایرانی باستان به z بدل می‌شود، درست همانند jṝ / járati سنسکریت. \"\n   \"چونگ (ص ۴۶۹-۴۷۰) ریشه‌شناسی هندواروپایی این ستاک را «بی‌خدشه» می‌خواند. zaurva همان zauruua-/zaurvan- اوستایی \"\n   \"«پیری، فرتوتی» است (بارتولومه ستون ۱۶۸۲). ولی zarwân اوستایی نیست، بلکه پارتی zrwʾn و پهلوی zarwān «پیری» است، \"\n   \"و zarmân نیز فارسی میانهٔ zarmān «پیرمرد، فرتوتی» (هم‌ریشه با jariman- سنسکریت) است؛ هر دو ایرانی میانه‌اند و \"\n   \"جای‌دادنشان در جعبهٔ «اوستایی/پارسی باستان» دقیق نیست. â-zarema-dugedâ ترکیبی اوستایی گواهی‌شده نیست: اوستا \"\n   \"صفت azarəma- «کاهش‌نیابنده» را دارد (پوکورنی ۳۹۰) و معین در حاشیهٔ برهان قاطع ص ۳۶ آن را با dugdā «دختر» \"\n   \"می‌آمیزد تا آزرمیدخت را توضیح دهد؛ پس ترکیب، بازسازی امروزی است. zara-uštra همان Zaraθuštra- است که جزء دوم آن \"\n   \"uštra «شتر» بی‌گفتگوست و بارتولومه (ستون ۱۶۷۰) جزء نخست را *zarant- «پیر» می‌گیرد؛ یعنی ادعای نورایی بر پایهٔ \"\n   \"بارتولومه است. روی‌هم: با احتیاط پذیرفتنی است.\"),\n \"sources\": [W_PIE, W_ZAL, W_ZORO],\n \"ref_check\": [\n   {\"ref\": \"POK:390\", \"status\": \"supports\",\n    \"note\": \"Pokorny (POK_full.txt, 'Root/lemma: ger-, gera-, gre-', Page(s) 390-391) lists av. azarəsant-, azarəma-, zairina-, zarəta-, zaurvan-, zaurura- and zaraθuštra- under this root — the whole Avestan column of Nourai's box.\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 1670 (s.v. zaraθuštra-) and col. 1682 (zaurvan-, zaurura-, zairina-)\", \"stance\": \"supports\",\n    \"note\": \"grep 'zaurvan|ara%uilra' BRT.txt: 'Komp.: *zarant- Adj. „alt“ (ai. járant- Adj., osset. zäron(d)) + uštra; eig. „des Kamele alt sind“'; and 'j. zaurvan- m. „Greisenalter, Altersschwäche“'; the zairina- article cross-refers 'S. noch azarəma; azarəmant-, zaurura-, zarəta-, zaurvan-, zaraθuštra- … Vgl. np. zar, zāl, [osset.] zārond „Greis“'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"pp. 469-470, s.v. *zarH2 'to age, grow old'\", \"stance\": \"supports\",\n    \"note\": \"'YAv. zar- ‘to age, grow old’ … MMP zrd ‘infirm (from old age)’ … PIE *ǵerH2- ‘to age, grow old’ = LIV 165 f. | Pok.: 390 f. … This root has an impeccable IE etymology.'\"},\n   {\"src\": \"PHD\", \"where\": \"p. 12 (arzan), p. 100 (zarmān, zarwān), p. 15 (a-zarmān)\", \"stance\": \"partial\",\n    \"note\": \"MacKenzie: 'zarmān [zlmʾn' | M zrwn-, N ~] old man; old age, decrepitude', 'zarwan [zlwʾn' | P zrwʾn] old age', 'a-zarmān [ʾzlmn'] ageless, unaging' — the forms are Middle Persian/Parthian, not Avestan as the box implies.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 599-600, s.v. ǵer-, ǵerə-\", \"stance\": \"supports\",\n    \"note\": \"WLD_Bd1_pages.txt leaves 607-608: 'vielleicht in Beziehung zu av. zaurv-, zauru-, etwa ursprgl. nom. *ǵer-us : gen. *ǵerə-u-ós'.\"},\n   {\"src\": \"NYB\", \"where\": \"Glossary s.v. zarmān\", \"stance\": \"supports\",\n    \"note\": \"Nyberg II: 'zarmān [zlmʾn'] (the demon) Old Age 103⁸ … NP zarman ‘an old decrepit man’; abstr. MPrs zrmʾnyyh'.\"}]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"zar 2; zâl; zâr 1; zarvân; Âzarmîdoxt; Zartošt\",\n \"verdict\": \"disputed\",\n \"derivation\": (\n   \"Four of the six words are sound. NP زر zar 'old (man/woman)' and زال zâl 'old, white-haired' both continue \"\n   \"Old Iranian *zarata- (Av. zarəta- 'old'); Manichaean MP zrd /zard/ 'infirm from old age' is the intermediate, \"\n   \"and the r/l alternation zar : zāl is the familiar New Persian dialectal doublet that Horn discusses under \"\n   \"no. 648 ('Hier stehen r und l im Neupersischen neben einander, vergl. zer No. 655'). Wiktionary derives زال \"\n   \"and زر 'old' from *ǵorh₂-tó- via Proto-Iranian *járHtáh. زار zâr 1 'ill, weak' is Horn no. 647, 'zār \"\n   \"„schwach, elend“ … Wohl zu aw. √zar- „altern“', matching Pokorny's npers. zār 'schwach, elend' \"\n   \"(dehnstufe *ǵērh₂-). زرتشت / زردشت Zartošt is the regular New Persian form of MP Zardu(x)št < Av. Zaraθuštra \"\n   \"(Av. θ > MP d/t, -ra > -), and the Greek route Ζωροάστρης > Lat. Zōroastrēs gave European 'Zoroaster'. \"\n   \"TWO words are disputed. (a) زروان zarvân glossed 'time': the Zurvān of Zoroastrian speculation is Av. \"\n   \"zruuan- (= zruvan-) 'time', MP zurwān, Parthian/Manichaean zrwʾn, Arm. loan Zruan, Syr. Zurvān — a stem \"\n   \"kept apart from zar- 'to age' by Hübschmann, Persische Studien no. 659: 'Np. zarmān … ist verwandt mit zd. \"\n   \"zaurva-. Aber np. zarvān „tempus“ ist zoroastrisch = paz. zurvān ‘time’ … zd. zrvan-'. Pokorny only \"\n   \"says 'vielleicht auch zrvan- : zrun- ‘Zeit’'; MacKenzie keeps zarwān 'old age' and zurwān 'time' as two \"\n   \"entries. (b) آزرمیدخت Āzarmīdoxt: Nourai follows Moʿin's footnote at Borhān-e Qāṭeʿ p. 36, which analyses \"\n   \"آزرمی + دخت with Av. *a-zarəma- 'not ageing'. Modern scholarship (Nöldeke, Geschichte p. 393 n. 2, followed by \"\n   \"Gignoux in Encyclopaedia Iranica s.v. ĀZARMĪGDUXT) reads the Sasanian queen's name as MP Āzarmīgduxt \"\n   \"'daughter of the respected one', i.e. āzarmīg 'honoured, respected' (MacKenzie p. 15) + duxt — not 'ageless \"\n   \"woman'. The chart's own NOTE (BQT:1011) is essentially right about Moʿin's opinion: in his footnote to \"\n   \"زردشت (Borhān, printed p. ~1016, continued p. 1017) Moʿin writes that the second element uštra 'camel' is \"\n   \"undisputed but 'باحتمال قوی بمعنی زرد است … و جمعاً بمعنی دارنده شتر زرد', i.e. he does prefer 'yellow \"\n   \"camels'; today both readings are still current, with Bartholomae's 'old camels' the older and Mayrhofer's \"\n   \"'who can manage camels' a third option.\"),\n \"derivation_fa\": (\n   \"چهار واژه از شش واژه درست‌اند. «زر» و «زال» هر دو دنبالهٔ ایرانی باستان *zarata- (اوستایی zarəta- «پیر») اند؛ \"\n   \"میانجی، فارسی میانهٔ مانوی zard «فرتوت» است و جابه‌جایی ر/ل در «زر ~ زال» همان ابدال آشنای فارسی نو است که هرن \"\n   \"در شمارهٔ ۶۴۸ آورده. «زار ۱» به معنی «نزار، ناتوان» شمارهٔ ۶۴۷ هرن است: «zār „schwach, elend“ … وابسته به \"\n   \"√zar- اوستایی». «زرتشت/زردشت» صورت منظم فارسی نو از پهلوی Zardu(x)št < اوستایی Zaraθuštra است. اما دو واژه \"\n   \"پذیرفتنی نیست: (۱) «زروان» به معنی «زمان» از zruuan- اوستایی «زمان» (پهلوی zurwān) می‌آید و هوبشمان در \"\n   \"«پژوهش‌های ایرانی» شمارهٔ ۶۵۹ آن را به‌صراحت از zarmān/zaurva- جدا می‌کند؛ مکنزی نیز zarwān «پیری» و zurwān \"\n   \"«زمان» را دو مدخل جداگانه آورده است. (۲) «آزرمیدخت»: نورایی حاشیهٔ معین در برهان قاطع ص ۳۶ را دنبال می‌کند \"\n   \"(آزرمی + دخت از *a-zarəma- اوستایی)، ولی نولدکه و ژینیو (دانشنامهٔ ایرانیکا) نام این شهبانوی ساسانی را \"\n   \"Āzarmīgduxt «دخترِ آن ارجمند» از āzarmīg «محترم» می‌دانند، نه «زن پیرنشدنی». دربارهٔ یادداشت خودِ نمودار: معین \"\n   \"در حاشیهٔ «زردشت» می‌نویسد جزء دوم uštra «شتر» است و جزء نخست «باحتمال قوی بمعنی زرد است»؛ پس یادداشت درست \"\n   \"نقل شده، هرچند خوانش بارتولومه («شتر پیر») هنوز رایج است. حکم: پژوهش امروزی دو واژه از این جعبه را رد می‌کند.\"),\n \"sources\": [W_ZAL, W_ZAR, W_PIE, W_ZORO, W_ZARA, I_AZAR, I_ZURV],\n \"ref_check\": [\n   {\"ref\": \"HRN:143\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss p. 143 (HRN.txt leaf 164) nos. 646-648: '(2) zār „schwach, elend“. Wohl zu aw. √zar- „altern“ (vergl. np. zer, No. 655); phlv. zār, zarth' and '648. zāl „Greis, Greisin“. aw. √zar- „altern“, vergl. zaurvan-, zaurura-; ai. jara- „alternd“' — exactly Nourai's zâr 1 and zâl.\"},\n   {\"ref\": \"POK:390\", \"status\": \"supports\",\n    \"note\": \"Pokorny 390 s.v. ǵer-: 'vgl. auch npers. zar „Greis, Greisin“ … npers. zār „schwach, elend“, zār „Greis, Greisin“'.\"},\n   {\"ref\": \"BQT:36\", \"status\": \"supports\",\n    \"note\": \"Borhān-e Qāṭeʿ vol. 1 p. 36 (BQT_v1_pages.txt leaf 246), Moʿin's footnote 7 to آزرمیدخت: 'آزرمی + دخت. جزء اول در اوستا a-zarəma… که خود مرکب است از a علامت نفی و zarəm…, و zairina و zarəta که هر دو صفت است بمعنی فرسوده و شکسته و zarəta در سانسکریت jīrṇa بهمین معنی است, zaurva بمعنی پیری' — Nourai's 'ageless woman' comes straight from here.\"},\n   {\"ref\": \"BQT:1015\", \"status\": \"supports\",\n    \"note\": \"Borhān vol. 2, leaf 472 (printed ~1015): headwords زربان 'پیرسالخورده', with footnote 'مصحف «زرمان»' and 'زروان (که به زرمان و زربان تصحیف شده)' — supports the زرمان / زروان material of the box.\"},\n   {\"ref\": \"BQT:1017\", \"status\": \"supports\",\n    \"note\": \"Borhān vol. 2, leaves 473-474 (printed ~1016-1017), Moʿin's long footnote to زردشت: 'این نام در گاثاها صورت Zaraθuštra … در اینکه جزء دوم uštra (بمعنی شتر) اختلافی نیست ولی در وجه اشتقاق جزو اول سخن بسیار رفته. باحتمال قوی بمعنی زرد است [رک: زرد] و جمعاً بمعنی دارندهٔ شتر زرد'.\"},\n   {\"ref\": \"BQT:1011\", \"status\": \"partial\",\n    \"note\": \"Cited in the chart's NOTE for the 'yellow' reading. In this scan (BQT_v2_pages.txt, leaf ≈ printed − 543) p. 1011 falls in the زج/زخ section; the Moʿin passage that actually says 'زرد' about Zaraθuštra is the زردشت footnote at printed ~1016-1017 (leaves 473-474). So the claim is right, the page number is a few pages off (or the scan's offset is).\"}],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Persische Studien no. 659 (p. 69-70, HUB.txt leaf 80)\", \"stance\": \"contradicts\",\n    \"note\": \"'Np. zarman ‘senex decrepitus’ ist allerdings = skr. jariman- ‘hohes Alter’ und verwandt mit zd. zaurva-. Aber np. zarvan ‘tempus’ ist zoroastrisch = paz. zurvan ‘time’ …, phl. zruvan …, zd. zrvan- (d. i. zruvan-) ‘Zeit’.' — Hübschmann explicitly detaches زروان 'time' from the *ǵerh₂- family.\"},\n   {\"src\": \"PHD\", \"where\": \"p. 100 (zarmān, zarwān), p. 103 (zurwan), p. 15 (āzarmīg, a-zarmān), p. 100 (Zardu(x)št)\", \"stance\": \"partial\",\n    \"note\": \"MacKenzie has 'zarwan … old age' but a separate 'zurwan [zwlwʾn'] time; the god Time, Zurvan', and 'āzarmīg [ʾclmyk'] honoured, respected' beside 'a-zarmān ageless' — supporting Zartošt and zar/zāl but splitting zarvān 'time' and Āzarmīg-duxt off.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p. 470, s.v. *zarH2, NWIR section\", \"stance\": \"supports\",\n    \"note\": \"'NWIR: NP zal PN (in Shahn.), also ‘old (wo)man’' — Cheung derives زال from *zarH2 < PIE *ǵerH2-.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 1 p. 36 and vol. 2 pp. ~1015-1017\", \"stance\": \"supports\",\n    \"note\": \"quoted in ref_check above; Moʿin's footnotes are the immediate source of both the 'ageless woman' gloss and the 'yellow camels' NOTE.\"},\n   {\"src\": \"MON\", \"where\": \"6-vol. Farhang-e Fārsi not online; checked the 2-vol. Adena condensation (MON_part1/2)\", \"stance\": \"silent\",\n    \"note\": \"no separate entry for زروان or آزرمیدخت in the condensed text; the aʿlām volumes that carry these proper names are not digitised.\"}]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Pahlavi\", \"words\": \"arzan\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n   \"MP arzan 'millet' is well attested — MacKenzie p. 12: 'arzan [PE < A prgʾ; ʾlnʾ | N ~] millet' (with the \"\n   \"Aramaic heterogram PRG'), kept apart there from the homograph arzān 'valuable'. Semantically and formally it \"\n   \"belongs with Lat. grānum, Goth. kaurn from *ǵr̥h₂-nó-m 'grain': the palatal *ǵ gives Iranian z and the \"\n   \"syllabic *r̥ is resolved with a vowel. The initial ar- rather than the expected south-western *zar-/*zarn- \"\n   \"points to metathesis in a north-western (Median/Parthian) form — Wiktionary flags NP ارزن simply as 'from a \"\n   \"Northwestern Iranian language' (citing Mallory & Adams, EIEC p. 237), and Mann himself prints 'Per. cf. \"\n   \"zīre … beside arzan (?) ‘millet’' with a question mark. So the root connection is standard but not \"\n   \"phonologically straightforward, and Nourai's citation MON:199 is a Persian dictionary, not an Iranist study.\"),\n \"derivation_fa\": (\n   \"«ارزن» در فارسی میانه گواهی‌شده است: مکنزی ص ۱۲ «arzan [هزوارش PRG'] ارزن»، جدا از هم‌نگاشتِ arzān «ارزشمند». \"\n   \"این واژه از دید معنایی و صوری با granum لاتین و kaurn گوتی از *ǵr̥h₂-nó-m «دانه» می‌خواند: *ǵ کامی در ایرانی به \"\n   \"z بدل می‌شود و *r̥ هجایی با واکه گشوده می‌گردد. ولی آغازِ ar- به‌جای *zar- انتظاری، نشان قلب (metathesis) در \"\n   \"گونه‌ای شمال‌غربی (مادی/پارتی) است؛ ویکی‌واژه نیز ارزن را «از زبانی ایرانی شمال‌غربی» می‌داند و مان خود کنار \"\n   \"arzan علامت پرسش گذاشته است. بنابراین پیوند با ریشه پذیرفتنی است اما آواشناسی آن یکدست نیست.\"),\n \"sources\": [W_ARZ, A_ARZ],\n \"ref_check\": [\n   {\"ref\": \"MON:199\", \"status\": \"partial\",\n    \"note\": \"The 6-volume Moʿin is not digitised; the entry was read on abadis.ir (فرهنگ معین): 'ارزن (اَ زَ) [ په . ] (اِ.) گیاهی از تیرة گندمیان … دانه‌های ریز' — Moʿin does tag the word [په.] = Pahlavi, which is exactly what Nourai's 'Pahlavi arzan' box claims, but Moʿin gives no Indo-European root.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 12 s.v. arzan\", \"stance\": \"supports\",\n    \"note\": \"PHD_mackenzie.txt line 1192: \\\"arzan [PC < A prg); 'len' | N ---] millet\\\" — Middle Persian arzan 'millet' with the Aramaic heterogram, continued by NP arzan.\"},\n   {\"src\": \"IEC\", \"where\": \"p. 406, s.v. ǵr̥nóm 'cultivated grain, corn'\", \"stance\": \"partial\",\n    \"note\": \"'Per. cf. zīre ‘caraway seed, aniseed’ beside arzan (?) ‘millet’' — Mann puts arzan under the root but marks it with a query.\"},\n   {\"src\": \"POK\", \"where\": \"pp. 390-391, s.v. ǵer-, ǵerə-, ǵrē-\", \"stance\": \"silent\",\n    \"note\": \"Pokorny's 'In der Bed. „Korn, Kern“' paragraph lists Lat. granum, OIr. grán, Lith. žirnis, OCS zrьno, Goth. kaurn — but no Iranian millet word.\"},\n   {\"src\": \"NYB\", \"where\": \"Glossary (grep arzan)\", \"stance\": \"silent\",\n    \"note\": \"Nyberg II has only aržānīk 'worthy' and marg-aržānīk 'deserving death'; the millet word does not occur in his texts.\"}]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Persian\", \"words\": \"arzan\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"NP ارزن arzan 'millet' (Panicum miliaceum) continues MP arzan unchanged — MacKenzie prints the Pahlavi entry \"\n   \"with 'N ~', i.e. New Persian identical. The variant ارژن in the chart's parenthesis is the same word with \"\n   \"the common NP z ~ ž fluctuation (cf. ارژن/ارزن as a place- and tree-name). Mann, at the page Nourai cites, \"\n   \"puts it under *ǵr̥nóm beside Ossetic dzærnæ 'frumenty', Lat. grānum and Goth. kaurn.\"),\n \"derivation_fa\": (\n   \"«ارزن» فارسی نو همان arzan فارسی میانه است و مکنزی در برابر آن «N ~» می‌گذارد، یعنی صورت نو بی‌تغییر مانده است. \"\n   \"گونهٔ «ارژن» داخل پرانتز همان واژه با تناوب آشنای ز ~ ژ در فارسی است. مان در همان صفحه‌ای که نورایی یاد کرده \"\n   \"(ص ۴۰۶) آن را زیر *ǵr̥nóm در کنار dzærnæ آسی، granum لاتین و kaurn گوتی آورده است. ادعای نورایی درست است.\"),\n \"sources\": [W_ARZ, A_ARZ],\n \"ref_check\": [\n   {\"ref\": \"IEC:406\", \"status\": \"supports\",\n    \"note\": \"IEC.txt leaf 236 (printed p. 406), entry 'ǵr̥nóm ‘cultivated grain, corn, staple grain of the country’. WP I, 600': '… Oss. cf. dzárná ‘frumenty’; Per. cf. zīre ‘caraway seed, aniseed’ beside arzan (?) ‘millet’ …'.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 12 s.v. arzan\", \"stance\": \"supports\",\n    \"note\": \"'arzan … millet', with 'N ~' marking the New Persian continuation.\"},\n   {\"src\": \"MON\", \"where\": \"abadis.ir, فرهنگ معین s.v. ارزن\", \"stance\": \"supports\",\n    \"note\": \"'ارزن (اَ زَ) [ په . ] (اِ.) گیاهی از تیرة گندمیان … دانه‌های آن را بیشتر به طیور می‌دهند' — Moʿin marks the word as Pahlavi in origin.\"},\n   {\"src\": \"HRN\", \"where\": \"grep 'arzan' in HRN.txt\", \"stance\": \"silent\",\n    \"note\": \"Horn has no entry for ارزن; his no. 657 treats زرد/زرت 'Art Hirse' (a different millet word, which he refuses to connect with Arab. ḏura).\"}]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"zîreh\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n   \"NP زیره zīra/zīre 'cumin, caraway seed' is the word Mann puts under *ǵr̥nóm at the very page Nourai cites, \"\n   \"beside Skt. jīrṇa- and NP arzan; the semantic bridge would be 'grain, small seed' > 'cumin seed'. But this \"\n   \"is Mann's own construction and is not generally accepted: Wiktionary lists زیره with Baluchi zirrag, \"\n   \"Kurdish zîre, Sogdian zyrʾkk /zīrē/ and Skt. जीरक (jīraka) and states 'Further origins outside of Iranian \"\n   \"unclear'; the alternative Indian derivation from jṝ 'grow old, digest' (i.e. 'the digestive') is called folk \"\n   \"etymology on the Sanskrit side. The parenthetical form زیره با in the chart is not a second etymon but the \"\n   \"Persian dish-name zīre-bā 'cumin broth', a compound of the same word.\"),\n \"derivation_fa\": (\n   \"«زیره» را مان در همان ص ۴۰۶ زیر *ǵr̥nóm و کنار jīrṇa- سنسکریت و «ارزن» نشانده است؛ پل معنایی، «دانهٔ ریز» > \"\n   \"«دانهٔ زیره» می‌بود. ولی این بازسازی از آنِ خود مان است و پذیرش همگانی ندارد: ویکی‌واژه «زیره» را با zirrag \"\n   \"بلوچی، zîre کردی، zyrʾkk سغدی و जीरक (jīraka) سنسکریت هم‌ریشه می‌داند و می‌افزاید که خاستگاه آن بیرون از ایرانی \"\n   \"روشن نیست؛ پیوند سنسکریت با jṝ «کهنه/گوارده شدن» را نیز ریشه‌شناسی عامیانه می‌شمارد. «زیره با» در پرانتزِ کتاب \"\n   \"ریشهٔ دیگری نیست، بلکه نام آشِ «زیره‌با» است که ترکیبی از همین واژه است. حکم: با احتیاط پذیرفتنی است.\"),\n \"sources\": [W_ZIRE],\n \"ref_check\": [\n   {\"ref\": \"IEC:406\", \"status\": \"supports\",\n    \"note\": \"Mann p. 406 s.v. ǵr̥nóm: 'Per. cf. zīre ‘caraway seed, aniseed’ beside arzan (?) ‘millet’' — Nourai's node reproduces Mann exactly, gloss included.\"}],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian dictionary (Wiktionary's citation of Sogd. zyrʾkk)\", \"stance\": \"partial\",\n    \"note\": \"The Sogdian cognate zyrʾkk /zīrē/ 'cumin' is cited on the Wiktionary زیره page; it shows the word is old in Iranian but says nothing about a link to 'grain'.\"},\n   {\"src\": \"POK\", \"where\": \"pp. 390-391\", \"stance\": \"silent\",\n    \"note\": \"Pokorny's 'Korn, Kern' section has no cumin word in any language.\"},\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt s.v. زیره\", \"stance\": \"partial\",\n    \"note\": \"The condensed Moʿin describes زیره botanically ('ریشهٔ زیره دراز و باریک … در ایران نیز کشت می‌شود') without any etymological tag.\"}]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Sanskrit\", \"words\": \"jîrna\",\n \"verdict\": \"disputed\",\n \"derivation\": (\n   \"Sanskrit jīrṇá- is a real word of this root — it is the past participle of jṝ 'to grow old, wear out' and \"\n   \"means 'old, worn out, decayed; digested; old age', and Pokorny and Walde-Pokorny equate Lat. grānum \"\n   \"(*ǵr̥-nom) with it formally ('lat. granum „Korn, Kern“ (*ǵerə-nom, = ai. jīrṇá-)'). What is wrong is the \"\n   \"gloss: jīrṇá- does not mean 'caraway seed'. The Sanskrit word for cumin is जीरक jīraka (also जीर jīra), and \"\n   \"Wiktionary judges even that one 'more likely borrowed from some Iranian language; compare modern Persian \"\n   \"زیره', the traditional link to jṝ 'to grow old' being 'folk etymology'. Nourai is faithfully copying Mann, \"\n   \"who prints 'Skt. cf. jirnā ‘caraway-seed’ beside jirnah … ‘decrepit, withered, corny’' at IEC 406; the \"\n   \"printed page of the dictionary (checked at 600 dpi) really does read 'jîrna : caraway seed', so the \"\n   \"extraction is faithful and the fault lies with Mann's gloss, which Nourai took over.\"),\n \"derivation_fa\": (\n   \"jīrṇá- سنسکریت به‌راستی از همین ریشه است: صفت مفعولی jṝ «کهنه/فرسوده شدن» به معنی «کهنه، فرسوده، گواریده، \"\n   \"پیری»؛ پوکورنی و والده-پوکورنی نیز granum لاتین را از دید صوری برابر همین jīrṇá- می‌گیرند. آنچه نادرست است، \"\n   \"معنای داده‌شده است: jīrṇá- «زیره» نیست. واژهٔ سنسکریت زیره जीरक (jīraka) است و ویکی‌واژه همان را نیز «به‌احتمال \"\n   \"بیشتر وام از زبانی ایرانی، سنجیده با زیرهٔ فارسی» می‌داند و پیوند آن با jṝ را ریشه‌شناسی عامیانه می‌خواند. \"\n   \"نورایی در اینجا وفادارانه از مان (IEC ص ۴۰۶) نقل کرده که خود نوشته «jirnā ‘caraway-seed’». تصویر صفحهٔ چاپی \"\n   \"با تفکیک ۶۰۰ نقطه بررسی شد و همان «jîrna : caraway seed» را نشان می‌دهد؛ پس خطای خوانش اسکن نیست، خطا از \"\n   \"معنای مان و پذیرش آن در کتاب است.\"),\n \"sources\": [W_JIRK, W_JIRN, W_PIE],\n \"ref_check\": [\n   {\"ref\": \"IEC:406\", \"status\": \"supports\",\n    \"note\": \"Mann p. 406 does print the disputed gloss: 'Skt. cf. jirnā ‘caraway-seed’ beside jirnah, jūrnabh ‘decrepit, withered, corny’'. The reference supports Nourai's node, but the reference itself is what modern Sanskrit lexicography contradicts.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp. 390-391\", \"stance\": \"contradicts\",\n    \"note\": \"'Partiz. jūrṇá-, jīrṇá- „gebrechlich, abgelebt, abgenutzt, zerfallen, morsch, alt“' and 'lat. granum ‘Korn’ (*ǵr̥-nom, = ai. jīrṇá-, s. o.)' — for Pokorny jīrṇá- is 'decrepit, worn out', never a spice.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 599-600\", \"stance\": \"contradicts\",\n    \"note\": \"WLD_Bd1 leaf 608: 'lat. granum „Korn, Kern“ (*ǵerə-nom, = ai. jīrṇá-, s. o.)' — same formal equation, same 'worn out' meaning.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 8.42 GRAIN\", \"stance\": \"silent\",\n    \"note\": \"Buck's grain article lists Lat. granum, Goth. kaurn, OE corn etc. with no Sanskrit spice word.\"}]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Latin\", \"words\": \"granum\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Latin grānum 'grain, seed, kernel' is the classic zero-grade *ǵr̥h₂-nó-m of this root, matched exactly by \"\n   \"OIr. grán, Welsh grawn, Lith. žirnis / OPruss. syrne, OCS zrьno and Gothic kaurn — the *ǵ giving Latin g, \"\n   \"the syllabic *r̥ giving Latin -ra-, the *h₂ lost before the suffix. Watkins sets up the root variant \"\n   \"*grə-no- 'Grain' precisely for this set and refers it to 'Pok. ger- 390'.\"),\n \"derivation_fa\": (\n   \"grānum لاتین «دانه، مغز» صورت درجهٔ صفرِ کلاسیک *ǵr̥h₂-nó-m است و با grán ایرلندی کهن، grawn ولزی، žirnis \"\n   \"لیتوانیایی، zrьno اسلاوی کهن و kaurn گوتی برابری کامل دارد: *ǵ در لاتین g می‌شود، *r̥ هجایی به -ra- بدل \"\n   \"می‌گردد و *h₂ پیش از پسوند می‌افتد. واتکینز در پیوستِ AHD همین *grə-no- «دانه» را بازسازی و به «پوکورنی ۳۹۰» \"\n   \"ارجاع می‌دهد. ادعای نورایی درست است.\"),\n \"sources\": [E_GRAN, W_PIE],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 535: 'gre-no-. Grain. 1. Germanic *kornam in: a. Old English corn … 2. Latin grānum, grain: GARNER, GRAIN, GRAM2, GRANADILLA, GRANARY, GRANGE, GRANITE, GRANULE, GRENADE; FILIGREE. [In Pok. ger- 390.]'\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp. 390-391, section 'In der Bed. „Korn, Kern“'\", \"stance\": \"supports\",\n    \"note\": \"'lat. granum „Korn, Kern“ (*ǵr̥-nom, = ai. jīrṇá-) = air. grán, cymr. usw. grawn … = lit. žirnis, lett. zirnis „Erbse“, apr. syrne „Korn“; aksl. zrьno … got. kaurn'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 600\", \"stance\": \"supports\",\n    \"note\": \"identical wording in Walde-Pokorny I 600 (WLD_Bd1_pages.txt leaf 608).\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 8.42 GRAIN\", \"stance\": \"supports\",\n    \"note\": \"'Lat. granum ‘a grain’, but generic ‘grain’ reflected in granarium ‘granary’, and common to the derivs., It., Sp. grano, Fr. grain (> ME greyn, grayn, NE grain) … Goth. kaurn, OE corn, etc., general Gmc.'\"},\n   {\"src\": \"KLN\", \"where\": \"p. 673 s.v. grain\", \"stance\": \"supports\",\n    \"note\": \"'grain, n., seed, corn. — F., fr. L. grānum, ‘grain, seed, small kernel’. See corn, ‘grain’, and cp. garner, garnet, gram, granadilla, granary, grange, granilla, granite, granule, grenade …'.\"}]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Italian\", \"words\": \"granito\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Italian granito is the past participle of granire 'to make grainy, granulate', from grano < Lat. grānum; as \"\n   \"an adjective it means 'grained, granular' and was substantivised in the stone-cutters' language of \"\n   \"sixteenth- and seventeenth-century Italy for the speckled crystalline rock, i.e. 'the grained (stone)'. \"\n   \"Mann even reconstructs the Indo-European adjective for this type: 'ǵr̥nātos, -itos ‘grained, of grain’ … \"\n   \"Lat. grānātus ‘granular, grained’; It. granato … granito … s. ‘granite’'.\"),\n \"derivation_fa\": (\n   \"granito ایتالیایی صفت مفعولیِ granire «دانه‌دانه کردن» از grano < grānum لاتین است و در معنی «دانه‌دار» به کار \"\n   \"می‌رفت؛ در زبان سنگ‌تراشان ایتالیای سدهٔ شانزدهم و هفدهم به‌صورت اسم برای آن سنگ بلورینِ خال‌خال به کار رفت، \"\n   \"یعنی «سنگِ دانه‌دار». مان حتی صفت هندواروپاییِ این ساخت را بازسازی می‌کند: «ǵr̥nātos, -itos ‘دانه‌دار’ … \"\n   \"It. granato … granito … ‘granite’». ادعای نورایی درست است.\"),\n \"sources\": [E_GRAN, W_GRAN],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"the node carries no reference in the book; the claim was checked against Klein p. 674 and Etymonline instead.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 674 s.v. granite\", \"stance\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 365 (between the printed markers 674 and 675): 'granite, n. — F., fr. It. granito, lit. ‘grainy’, pp. of granire, ‘to make grainy’, fr. grano, ‘grain’.'\"},\n   {\"src\": \"IEC\", \"where\": \"p. 405-406, s.v. ǵr̥nātos, -itos\", \"stance\": \"supports\",\n    \"note\": \"'ǵr̥nātos, -itos ‘grained, of grain’. See ǵr̥nóm … Lat. grānātus ‘granular, grained’; It. granato, id. and ‘robust’; granito ‘robust’; s. ‘granite’'.\"},\n   {\"src\": \"WEB\", \"where\": \"grep 'granite' in WEB_vol1.txt\", \"stance\": \"silent\",\n    \"note\": \"the available Webster volume does not reach the letter G.\"}]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"French\", \"words\": \"granite\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"French borrowed the Italian mineralogical term in the seventeenth century as granit (also spelt granite), \"\n   \"which is the form that then passed on to English and, in the twentieth century, to Persian. Etymonline \"\n   \"dates the English word to the 1640s and says it comes 'from French granit(e) (17c.) or directly from Italian \"\n   \"granito'; Klein routes it through French only.\"),\n \"derivation_fa\": (\n   \"فرانسه این اصطلاح کانی‌شناسی ایتالیایی را در سدهٔ هفدهم به‌صورت granit (و نیز granite) وام گرفت و همین صورت \"\n   \"است که سپس به انگلیسی و در سدهٔ بیستم به فارسی رسید. اتیمآنلاین واژهٔ انگلیسی را به دههٔ ۱۶۴۰ می‌رساند و \"\n   \"می‌گوید «از فرانسویِ granit(e) سدهٔ ۱۷ یا مستقیماً از granito ایتالیایی»؛ کلاین تنها راه فرانسوی را می‌آورد. \"\n   \"ادعای نورایی درست است.\"),\n \"sources\": [E_GRAN, W_GRAN],\n \"ref_check\": [\n   {\"ref\": \"KLN:674\", \"status\": \"supports\",\n    \"note\": \"Klein p. 674: 'granite, n. — F., fr. It. granito …' — the French link is exactly what Nourai draws.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 674\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n   {\"src\": \"SKT\", \"where\": \"grep 'granite' in SKT.txt\", \"stance\": \"silent\",\n    \"note\": \"Skeat's Concise has no granite entry in the OCR text.\"},\n   {\"src\": \"DEV\", \"where\": \"grep 'granit' in DEV.txt\", \"stance\": \"silent\",\n    \"note\": \"Devic covers only French words of oriental origin; granite is not among them.\"}]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Persian\", \"words\": \"gerânît\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Persian گرانیت gerānīt is a twentieth-century learned loan from French granite/granit, taken with the French \"\n   \"vowels (gerānīt, not English 'granit'), and used for the igneous rock whose native Persian name is سنگ خارا. \"\n   \"Moʿin's dictionary tags it '[ فر. ]' — French — and defines it simply as سنگ خارا.\"),\n \"derivation_fa\": (\n   \"«گرانیت» وام‌واژه‌ای دانشی از فرانسویِ granite/granit است که در سدهٔ بیستم وارد فارسی شد و آوای فرانسوی خود را \"\n   \"نگه داشته است (گرانیت، نه صورت انگلیسی). برابر بومی آن «سنگ خارا» است. فرهنگ معین آن را «(گِ) [ فر. ] (اِ.) \"\n   \"سنگ خارا» می‌آورد، یعنی خودِ معین هم آن را فرانسوی می‌داند. ادعای نورایی درست است.\"),\n \"sources\": [A_GRAN, E_GRAN],\n \"ref_check\": [\n   {\"ref\": \"MON:3223\", \"status\": \"supports\",\n    \"note\": \"The 6-vol. Moʿin is not digitised; the entry was read on abadis.ir (فرهنگ معین): 'گرانیت (گِ) [ فر. ] (اِ. ) سنگ خارا.' — a French loan meaning 'hard rock', exactly Nourai's node.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"abadis.ir, فرهنگ معین s.v. گرانیت; MON_part1.txt s.v. خارا\", \"stance\": \"supports\",\n    \"note\": \"the condensed Moʿin defines خارا as 'سنگی است از دستهٔ سنگ‌های آذرین … گرانیت', confirming the equation گرانیت = سنگ خارا.\"},\n   {\"src\": \"ARY\", \"where\": \"grep in ARY_pages.txt\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur's Indo-European roots dictionary covers inherited Persian words; the modern European loan گرانیت is not in it, and the OCR of the scan is in any case too poor for reliable lookup.\"}]\n})\n\nnodes.append({\n \"id\": 11, \"lang\": \"English\", \"words\": \"granite\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"English granite is first recorded in the 1640s, borrowed from French granit(e) or directly from Italian \"\n   \"granito, 'in reference to the appearance of the rock'. The word is thus the same Latin grānum in a \"\n   \"petrographic disguise, and English keeps the Italian -ite spelling that French also had.\"),\n \"derivation_fa\": (\n   \"«granite» انگلیسی نخستین‌بار در دههٔ ۱۶۴۰ گواهی شده و از granit(e) فرانسوی یا یکسره از granito ایتالیایی وام \"\n   \"گرفته شده است، «به سبب نمای دانه‌دانهٔ سنگ». پس همان grānum لاتین است در جامهٔ اصطلاح سنگ‌شناسی. ادعای نورایی \"\n   \"درست است.\"),\n \"sources\": [E_GRAN, W_GRAN],\n \"ref_check\": [\n   {\"ref\": \"KLN:674\", \"status\": \"supports\",\n    \"note\": \"Klein p. 674 s.v. granite gives exactly this chain (F. < It. granito < grano < L. grānum).\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 674\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. gre-no-\", \"stance\": \"supports\",\n    \"note\": \"GRANITE is listed among the English descendants of Latin grānum under the root gre-no-.\"}]\n})\n\nnodes.append({\n \"id\": 12, \"lang\": \"English\", \"words\": \"grain, granule, gravy, pomegranate\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"All four go back to Latin grānum. grain is ME grain < OFr. grain < L. grānum. granule is L. grānulum, the \"\n   \"diminutive. pomegranate is OFr. pome grenate < ML. pōmum grānātum 'apple full of seeds'. gravy is the odd \"\n   \"one: ME graue, a scribal misreading of OFr. grané 'a dish sprinkled with grains (spices)', lit. 'grained', \"\n   \"from ML. grānātus, pp. of grānāre 'to grain', from grānum — the u/v of the manuscript hand being read for n. \"\n   \"Note that Watkins's appendix (the AHD reference Nourai cites) lists GRAIN and GRANULE under gre-no- but not \"\n   \"GRAVY or POMEGRANATE; for those two the authority is Klein.\"),\n \"derivation_fa\": (\n   \"هر چهار واژه به grānum لاتین می‌رسند. grain از grain فرانسوی کهن < grānum؛ granule از grānulum لاتین \"\n   \"(مصغّر)؛ pomegranate از pome grenate فرانسوی کهن < pōmum grānātum «سیبِ پردانه». gravy استثناست: صورت \"\n   \"انگلیسی میانهٔ graue، خوانش نادرست کاتبان از grané فرانسوی کهن «خوراکِ ادویه‌پاشیده، دانه‌دار» از grānātus \"\n   \"لاتین میانه است — n دست‌نوشته به u/v خوانده شد. یادآوری: پیوست واتکینز (همان AHD که نورایی یاد کرده) تنها \"\n   \"GRAIN و GRANULE را زیر gre-no- می‌آورد و GRAVY و POMEGRANATE در آن نیست؛ مرجع این دو کلاین است. ادعای \"\n   \"نورایی درست است.\"),\n \"sources\": [E_GRAN],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"AHD_watkins1985.txt line 535 lists under gre-no- only 'GARNER, GRAIN, GRAM2, GRANADILLA, GRANARY, GRANGE, GRANITE, GRANULE, GRENADE; FILIGREE'; a grep of the index shows 'GRAIN gre-no-' but no entry at all for POMEGRANATE or GRAVY. Two of Nourai's four words are therefore not in the reference he cites.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 673 (grain), p. 675 (gravy)\", \"stance\": \"supports\",\n    \"note\": \"'grain … fr. L. grānum … cp. … granule … pomegranate … Cp. also gravy'; and 'gravy, n. — ME. graue (pronounced grave), from misreading of OF. grané, ‘a dish powdered with grains’, lit. ‘grained’, fr. ML. granatus, pp. of granare, ‘to grain’, fr. L. granum.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 5.55 / 8.42\", \"stance\": \"supports\",\n    \"note\": \"'Fr. graine ‘seed’, fr. VLat. grana sg. coll., orig. pl. of Lat. granum ‘grain, kernel’ (8.42)'; and 'Lat. granarium (> It. granaio, Sp. granero, Fr. grenier) … fr. granum ‘grain’'.\"}]\n})\n\nnodes.append({\n \"id\": 13, \"lang\": \"Middle German\", \"words\": \"karl\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"OHG karal, MHG karl 'man, husband, grown man' (= ON karl 'man, old man, freeman', OE ceorl > churl, MLG \"\n   \"kerle, NHG Kerl) reflects Germanic *karlaz / *karilaz, an l-formation on the o-grade *ǵorh₂-o-, with the \"\n   \"basic sense 'grown, mature (hence old) man' — the same semantic move as Gk. gérōn 'old man'. Klein derives \"\n   \"the whole set 'fr. I.-E. base *ger(e)-, ‘to become ripe, grow old’, whence also OI. jarati, Gk. gérōn'; \"\n   \"Walde-Pokorny I 600 gives 'Gdbed. wohl „alter Mann“'. Nourai's language label 'Middle German' is loose \"\n   \"(the form is Middle High German, continuing Old High German karal), and Watkins prints *karlaz as a Germanic \"\n   \"root without an IE etymology of its own, though he still refers it to Pok. ger- 390.\"),\n \"derivation_fa\": (\n   \"karal آلمانی علیای باستان و karl آلمانی علیای میانه «مرد، شوهر، مردِ بالغ» (برابر karl نورس کهن، ceorl \"\n   \"انگلیسی کهن > churl و Kerl آلمانی) بازتاب ژرمنی *karlaz / *karilaz است؛ ساختی با پسوند -l بر درجهٔ o یعنی \"\n   \"*ǵorh₂-o-، با معنای پایهٔ «مردِ رسیده و سالخورده» — همان تحول معنایی که در yépωv یونانی «پیرمرد» می‌بینیم. \"\n   \"کلاین همهٔ این خانواده را «از پایهٔ هندواروپایی *ger(e)- ‘رسیدن، پیر شدن’» می‌گیرد و والده-پوکورنی (ج ۱ \"\n   \"ص ۶۰۰) معنای اصلی را «مرد پیر» می‌داند. برچسب «آلمانی میانه» در کتاب کمی نادقیق است (صورت، آلمانی علیای \"\n   \"میانه است) اما ادعا درست است.\"),\n \"sources\": [E_CHAR, W_PIE],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"AHD_watkins1985.txt line 585: '[karlaz. Man. Germanic root. 1. Old English ceorl, man, churl: CHURL. 2. Old Norse karl, man, freeman: CARL, CARLING. [In Pok. ger- 390.]]' — Watkins prints it in brackets as a Germanic root, i.e. he accepts the reference to Pokorny 390 but not an established IE derivation.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 296 s.v. churl\", \"stance\": \"supports\",\n    \"note\": \"'churl … OE. ceorl … rel. to … ON. karl ‘old man, man, servant’ …, OHG. karal ‘man, husband, lover’ [whence MHG. karl, of s.m., and the ML. PN. Carolus, the G. PN. Karl …]; fr. I.-E. base *ger(e)-, ‘to become ripe, grow old’, whence also OI. jarati, ‘grows old’, Gk. gérōn ‘old man’ … Goth. kaurn, OE. corn, ‘grain’.'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 600\", \"stance\": \"supports\",\n    \"note\": \"'anord. karl „Mann, alter Mann …“ = ahd. karal „Mann, Ehemann …“, mit Ablaut ags. ceorl …, engl. churl …, nhd. (aus dem Nd.) Kerl; Gdbed. wohl „alter Mann“, l-Suffix wie in gr. gerýllos'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 2.21 MAN\", \"stance\": \"supports\",\n    \"note\": \"'NHG kerl. Perh. as ‘full-grown man’ : Grk. gérōn, Skt. jarant- ‘old man’. Walde-P. 1.600.'\"}]\n})\n\nnodes.append({\n \"id\": 14, \"lang\": \"French / English\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"A pass-through box with no words of its own: it marks the route by which the Germanic personal name reached \"\n   \"the modern world. MHG Karl was latinised as Medieval Latin Carolus (the name of Charlemagne, Carolus \"\n   \"Magnus), which gave Old French Charles (with the northern French ca- > cha- palatalisation) and thence \"\n   \"English Charles; the unlatinised Norse/German form gave English Carl/Karl. Etymonline: 'Charles: masc. \"\n   \"proper name, from French Charles, from Medieval Latin Carolus, from Middle High German Karl, literally \"\n   \"‘man, husband’'.\"),\n \"derivation_fa\": (\n   \"این جعبه واژه‌ای از خود ندارد و تنها مسیر رسیدنِ نام ژرمنی به زبان‌های امروزی را نشان می‌دهد: Karl آلمانی \"\n   \"میانه در لاتین میانه Carolus شد (نام شارلمانی، Carolus Magnus) و از آنجا Charles فرانسوی کهن پدید آمد — با \"\n   \"همان تحول ca- > cha- در فرانسویِ شمالی — و سپس Charles انگلیسی؛ صورت لاتینی‌نشدهٔ ژرمنی/نورس نیز Carl/Karl \"\n   \"انگلیسی را داد. ادعای نورایی درست است.\"),\n \"sources\": [E_CHAR],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"the node carries no reference in the book; checked against Klein p. 296/p. 268 and Etymonline s.v. Charles.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 268 s.v. carl, carline; p. 296 s.v. churl\", \"stance\": \"supports\",\n    \"note\": \"'carl, n., a fellow (Scot.) — ON. karl, ‘a man’, rel. to OE. ceorl … See churl and cp. Carl, Charles'; and under churl the bracket '[whence MHG. karl … and the ML. PN. Carolus, the G. PN. Karl; cp. also Lith. karalius, OSlav. kralji ‘king’, which go back to Carolus = Charles I (Charlemagne)]'.\"},\n   {\"src\": \"SKT\", \"where\": \"grep 'Charles' in SKT.txt\", \"stance\": \"silent\",\n    \"note\": \"Skeat's Concise does not treat personal names.\"}]\n})\n\nnodes.append({\n \"id\": 15, \"lang\": \"Persian\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"The box holds only Persian spellings of European personal names: کارل (Carl/Karl, German and Scandinavian), \"\n   \"شارل (Charles, from French, with š- for French ch-), چارلی (Charlie, from English, with č- for English \"\n   \"ch-), کارولینا (Carolina/Caroline) and کارلوس (Carlos, Spanish). All are twentieth-century transcriptions \"\n   \"taken through French and English, and the two shapes شارل vs چارلی are a neat diagnostic of which European \"\n   \"language each came through. They are ultimately the same MHG Karl of node 13, so the arrow is right; but \"\n   \"they are names transliterated, not words inherited.\"),\n \"derivation_fa\": (\n   \"این جعبه فقط املای فارسی نام‌های اروپایی است: «کارل» (آلمانی و اسکاندیناویایی)، «شارل» (از فرانسوی، با ش در \"\n   \"برابر ch فرانسوی)، «چارلی» (از انگلیسی، با چ در برابر ch انگلیسی)، «کارولینا» و «کارلوس» (اسپانیایی). همه \"\n   \"آوانگاری‌های سدهٔ بیستم‌اند که از راه فرانسه و انگلیسی به فارسی رسیده‌اند و دوگانگی «شارل/چارلی» خود نشان \"\n   \"می‌دهد هر کدام از چه زبانی گرفته شده است. سرچشمهٔ همه همان Karl آلمانی میانهٔ گرهٔ ۱۳ است، پس پیکان درست است؛ \"\n   \"با این حال اینها نام‌های آوانگاشته‌اند، نه واژه‌های به‌ارث‌رسیده.\"),\n \"sources\": [E_CHAR],\n \"ref_check\": [\n   {\"ref\": \"MON\", \"status\": \"not_checked\",\n    \"note\": \"Nourai cites Moʿin without a page; the proper-name volumes (aʿlām, vols 5-6) of the 6-volume Farhang-e Fārsi are not digitised anywhere (checked archive.org, Google Books, HathiTrust per refs_online.json), and vajehyab/abadis carry no aʿlām entries.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 268 (Carol, Caroline), p. 296 (churl)\", \"stance\": \"supports\",\n    \"note\": \"'Carol, masc. PN. — ML. Carolus. See Charles and cp. Carl'; 'Caroline, fem. PN. — F., fr. It. Carolina, orig. a fem. adj. derived fr. ML. Carolus, ‘Charles’'. The Persian forms are these names in Persian script.\"},\n   {\"src\": \"MON\", \"where\": \"MON_part1/part2 (2-vol. condensation)\", \"stance\": \"silent\",\n    \"note\": \"the condensed Moʿin has no aʿlām section, so none of these names appears.\"}]\n})\n\nnodes.append({\n \"id\": 16, \"lang\": \"English\", \"words\": \"Carl, Karl, Carolina, Charles\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Carl and Karl are the Germanic name taken directly (ON karl 'man'), Charles is the same name through \"\n   \"Medieval Latin Carolus and Old French Charles, and Carolina is an Italian/Latin feminine adjective on \"\n   \"Carolus ('of, pertaining to Charles'), used as a woman's name (and, in America, as the name of the two \"\n   \"colonies chartered under Charles I/II). Klein: 'Caroline, fem. PN. — F., fr. It. Carolina, orig. a fem. \"\n   \"adj. derived fr. ML. Carolus, ‘Charles’'.\"),\n \"derivation_fa\": (\n   \"Carl و Karl همان نام ژرمنی‌اند که یکسره گرفته شده (karl نورس کهن «مرد»)؛ Charles همان نام است از راه \"\n   \"Carolus لاتین میانه و Charles فرانسوی کهن؛ و Carolina صفت مؤنث ایتالیایی/لاتین بر Carolus («وابسته به \"\n   \"شارل») است که نام زنانه شد (و در آمریکا نام آن دو مستعمره که به نام چارلز اول و دوم خوانده شدند). کلاین: \"\n   \"«Caroline, fem. PN. — از فرانسوی، از Carolina ایتالیایی، در اصل صفت مؤنث از Carolus لاتین میانه». ادعای \"\n   \"نورایی درست است.\"),\n \"sources\": [E_CHAR],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"no reference in the book for this node; checked against Klein pp. 268, 296 and Etymonline s.v. Charles.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 268 s.v. carl, Carol, Caroline\", \"stance\": \"supports\",\n    \"note\": \"'carl, n., a fellow (Scot.) — ON. karl, ‘a man’ … See churl and cp. Carl, Charles'; 'Caroline, fem. PN. — F., fr. It. Carolina … fr. ML. Carolus, ‘Charles’'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. karlaz\", \"stance\": \"supports\",\n    \"note\": \"'karlaz. Man. Germanic root. … 2. Old Norse karl, man, freeman: CARL, CARLING. [In Pok. ger- 390.]'\"}]\n})\n\nnodes.append({\n \"id\": 17, \"lang\": \"Germanic\", \"words\": \"karnam\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"karnam\",\n \"correct_form\": \"kornam\",\n \"derivation\": (\n   \"The Germanic etymon of English corn is *kornam (Watkins) / *kurnam (Etymonline, from the zero grade \"\n   \"*ǵr̥h₂-nom), the source of Goth. kaurn, OHG/ON korn, OE corn. The chart's 'karnam' is not a form any \"\n   \"handbook knows — the a-vocalism would give Germanic *karn-, which is the ablaut grade of the karl word, not \"\n   \"of the grain word. Checking the printed page at 600 dpi (data/verification/sources/refs/ocr/BOOK/174.png) \"\n   \"shows that the book itself prints 'karnam : grain', so the extraction is faithful and this is Nourai's own \"\n   \"misprint (or a slip of transcription from AHD's 'Germanic *kornam') for *kornam. Apart from the vowel, the \"\n   \"node is correct: the Germanic grain word does descend from this root and does give English corn.\"),\n \"derivation_fa\": (\n   \"صورت ژرمنیِ نیای «corn» انگلیسی *kornam (واتکینز) یا *kurnam (اتیمآنلاین) است، از درجهٔ صفر *ǵr̥h₂-nom، که \"\n   \"kaurn گوتی، korn آلمانی علیای باستان و نورس کهن، و corn انگلیسی کهن از آن آمده‌اند. «karnam» صورتی است که در \"\n   \"هیچ فرهنگ معتبری نیست؛ واکهٔ a صورت *karn- می‌داد که درجهٔ دیگرِ واژهٔ karl است نه واژهٔ «دانه». تصویر صفحهٔ \"\n   \"چاپی با تفکیک ۶۰۰ نقطه (نگهداری‌شده در refs/ocr/BOOK/174.png) نشان می‌دهد خودِ کتاب «karnam : grain» چاپ \"\n   \"کرده است؛ پس خطای خوانش اسکن نیست، خطای چاپی کتاب است و صورت درست *kornam است. جز همین واکه، بقیهٔ گره درست \"\n   \"است.\"),\n \"sources\": [E_CORN, W_PIE],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"contradicts\",\n    \"note\": \"AHD_watkins1985.txt line 535: 'gre-no-. Grain. 1. Germanic *kornam in: a. Old English corn, grain: CORN1 …' — the reference Nourai cites prints *kornam, not *karnam.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp. 390-391\", \"stance\": \"contradicts\",\n    \"note\": \"'got. kaurn, ahd. ags. anord. korn, nhd. Korn, ags. cyrnel „Kern“' — the Germanic vocalism is o/u, never a.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 358 s.v. corn\", \"stance\": \"contradicts\",\n    \"note\": \"'corn, n., grain. — ME., fr. OE. corn, rel. to OS., ON., OFris., OHG., MHG., G. korn … Goth. kaurn, ‘grain’, and cogn. with L. granum … fr. I.-E. base *ger(e)-, ‘to become ripe, grow old’.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 8.42\", \"stance\": \"contradicts\",\n    \"note\": \"'Goth. kaurn, OE corn, etc., general Gmc.'\"}]\n})\n\nnodes.append({\n \"id\": 18, \"lang\": \"English\", \"words\": \"corn\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"OE corn 'single seed of a cereal plant' < Germanic *kornam/*kurnam < PIE zero grade *ǵr̥h₂-nom, cognate with \"\n   \"Latin grānum; it is thus an inherited doublet of the borrowed grain of node 12. The sense stayed 'the \"\n   \"leading cereal of the district', which is why corn means wheat in England, oats in Scotland and maize in \"\n   \"America (from c. 1600, originally Indian corn).\"),\n \"derivation_fa\": (\n   \"corn انگلیسی کهن «دانهٔ غله» از ژرمنیِ *kornam/*kurnam و آن از درجهٔ صفر *ǵr̥h₂-nom هندواروپایی است و هم‌ریشهٔ \"\n   \"grānum لاتین؛ پس دوگانهٔ (doublet) به‌ارث‌رسیدهٔ همان grain وام‌گرفتهٔ گرهٔ ۱۲ است. معنای آن همواره «غلهٔ اصلی \"\n   \"همان ناحیه» ماند و از همین رو در انگلستان «گندم»، در اسکاتلند «جو دوسر» و در آمریکا از حدود ۱۶۰۰ «ذرت» \"\n   \"(نخست Indian corn) معنی می‌دهد. ادعای نورایی درست است.\"),\n \"sources\": [E_CORN, W_PIE],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"no reference on this node; checked against AHD (Watkins) gre-no-, Klein p. 358 and Etymonline.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 358 s.v. corn\", \"stance\": \"supports\",\n    \"note\": \"'corn, n., grain. — ME., fr. OE. corn … and cogn. with L. granum, ‘grain, seed, small kernel’ … fr. I.-E. base *ger(e)-, ‘to become ripe, grow old’, whence also OI. jarati, jīryati.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. gre-no-\", \"stance\": \"supports\",\n    \"note\": \"'Germanic *kornam in: a. Old English corn, grain: CORN1; b. Old English derivative noun cyrnel, seed, pip: KERNEL.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 8.42 GRAIN\", \"stance\": \"supports\",\n    \"note\": \"'Goth. kaurn, OE corn, etc., general Gmc. (but NE corn specialized to ‘maize’ in U.S., … NHG korn mostly ‘rye’, Sw. korn esp. ‘barley’).'\"}]\n})\n\ndoc = {\n \"pdf_page\": 174,\n \"book_page\": 144,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [{\n   \"entry\": 0,\n   \"root\": \"Ger 2, Greno\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ǵerh₂- 'to grow old, ripen, wear out' (with the derivative *ǵr̥h₂-nó-m 'grain')\",\n   \"note\": (\n     \"Pokorny 390-391 has exactly this lemma: 'ǵer-, ǵerə-, ǵrē- „morsch, reif werden, altern“, auch, bes. in \"\n     \"Bildungen mit Formans -no-, „Korn, Kern“ (nur NW-Idg.)'. Nourai's double name 'Ger 2, Greno' therefore \"\n     \"renders Pokorny's root plus its *ǵr̥-nom derivative, and both halves of the chart (the 'grow old' branch \"\n     \"and the 'grain' branch) belong to one article in Pokorny, in Walde-Pokorny I 599-600, and in Watkins \"\n     \"(gre-no- 'Grain … [In Pok. ger- 390.]'). Wiktionary's modern reconstruction *ǵerh₂- 'to grow old, to \"\n     \"mature' with the derivative *ǵr̥h₂-nó-m 'grain' matches. The language label 'Indo-European' and the gloss \"\n     \"'to become ripe, grow old' are right. The one caveat on the root box is the numbering: Nourai's 'Ger 2' \"\n     \"is his own, and does not correspond to Watkins's ger-2 (which is 'to gather', GRAPE); AHD's label for \"\n     \"this root is gre-no-.\"),\n   \"note_fa\": (\n     \"ریشهٔ هندواروپایی آغازین *ǵerh₂- «پیر شدن، رسیدن، فرسوده شدن» با مشتقِ *ǵr̥h₂-nó-m «دانه». پوکورنی در ص \"\n     \"۳۹۰-۳۹۱ همین مدخل را دارد: «ǵer-, ǵerə-, ǵrē- „پوسیده و رسیده شدن، پیر شدن“، و به‌ویژه در ساخت‌های \"\n     \"دارای پسوند -no- به معنی „دانه، مغز“ (تنها در شمال‌غرب هندواروپایی)». پس نامِ دوگانهٔ «Ger 2, Greno» در \"\n     \"کتاب، هم ریشه و هم مشتق آن را می‌رساند و هر دو شاخهٔ نمودار — شاخهٔ «پیری» و شاخهٔ «دانه» — در پوکورنی، در \"\n     \"والده-پوکورنی (ج ۱ ص ۵۹۹-۶۰۰) و در واتکینز یک مدخل‌اند. برچسب زبان و معنای ریشه درست است. تنها نکته، \"\n     \"شماره‌گذاری «Ger 2» است که از خودِ نورایی است و با ger-2 واتکینز (به معنی «گرد آوردن»، GRAPE) یکی نیست.\"),\n   \"sources\": [W_PIE, E_GRAN],\n   \"ref_check\": [\n     {\"ref\": \"POK:390\", \"status\": \"supports\", \"note\": POK_Q}],\n   \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. I 599-600 (WLD_Bd1_pages.txt leaves 607-608)\", \"stance\": \"supports\",\n      \"note\": \"the article 'ǵer-, ǵerə-' runs across pp. 599-600 with the same material: 'anord. karl … = ahd. karal …; Gdbed. wohl „alter Mann“' and 'In der Bed. „Korn, Kern“: … lat. granum „Korn, Kern“ (*ǵerə-nom, = ai. jīrṇá-)'.\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gre-no- and s.v. karlaz\", \"stance\": \"supports\",\n      \"note\": \"'gre-no-. Grain … [In Pok. ger- 390.]' and '[karlaz. Man. Germanic root … [In Pok. ger- 390.]]' — Watkins refers both branches to the same Pokorny page Nourai cites.\"},\n     {\"src\": \"IEC\", \"where\": \"Mann pp. 405-406, s.v. ǵr̥nóm, ǵr̥nātos, ǵor- (1) 'ripe, old, mature'\", \"stance\": \"supports\",\n      \"note\": \"Mann has both the 'ripe/old' root ('ǵor- (1) ‘ripe, old, mature’. Cf. ǵer-') and 'ǵr̥nóm ‘cultivated grain, corn, staple grain of the country’. WP I, 600' on the pages Nourai cites.\"},\n     {\"src\": \"SYN\", \"where\": \"Buck 8.42 GRAIN, 2.21 MAN, 14.15\", \"stance\": \"supports\",\n      \"note\": \"Buck ties Lat. granum / Goth. kaurn / OE corn together (8.42) and connects NHG Kerl with Gk. gérōn and Skt. jarant- 'old man' (2.21), i.e. the same two branches.\"},\n     {\"src\": \"CHEUNG\", \"where\": \"pp. 469-470 s.v. *zarH2\", \"stance\": \"supports\",\n      \"note\": \"'PIE *ǵerH2- ‘to age, grow old’ = LIV: 165 f. | Pok.: 390 f.' — the modern Iranist handbook cites the very page.\"}],\n   \"nodes\": nodes\n }]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-174.json','w',encoding='utf-8') as f:\n    json.dump(doc,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint('ok')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build174.py && python3 -m json.tool data/verification/page-174.json >/dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 174"
}
```


### [2026-09-05T21:11:33.184Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 18/18
node verdicts: {'plausible': 3, 'disputed': 2, 'confirmed': 12, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 13, 'partial': 4, 'not_checked': 5, 'contradicts': 1}
books consulted: {'supports': 31, 'partial': 5, 'contradicts': 6, 'silent': 12} | by book: {'KLN': 11, 'SYN': 6, 'MON': 5, 'POK': 5, 'PHD': 4, 'WLD': 4, 'AHD': 3, 'CHEUNG': 2, 'NYB': 2, 'IEC': 2, 'SKT': 2, 'BRT': 1, 'HUB': 1, 'BQT': 1, 'HRN': 1, 'SOD': 1, 'WEB': 1, 'DEV': 1, 'ARY': 1}
```


## [2026-09-05T21:11:41.623Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor pat in \"churl,  n\\.,  1)  a  peasant\" \"corn,  n\\.,  grain\\.\" \"carl,  n\\.,  a  fellow\" \"grain,  n\\.,  seed,  com\" \"gravy,  n\\.\" \"Caroline,  fem\\.  PN\"; do\npython3 - \"$pat\" <<'EOF'\nimport sys,re\npat=sys.argv[1]\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if re.search(pat,l):\n        nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$',l)\n        # position relative to page markers\n        idx=re.search(pat,l).start()\n        cur=None\n        for m in re.finditer(r'(?m)^\\s*(\\d{3,4})\\s*$',l):\n            if m.start()<idx: cur=m.group(1)\n        print(pat[:20],'-> leaf',i,'markers',nums,'page ~',cur)\n        break\nEOF\ndone"
}
```


### [2026-09-05T21:11:43.860Z] TOOL RESULT

```
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
  File "/usr/lib/python3.12/re/__init__.py", line 177, in search
    return _compile(pattern, flags).search(string)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/re/__init__.py", line 307, in _compile
    p = _compiler.compile(pattern, flags)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/re/_compiler.py", line 745, in compile
    p = _parser.parse(p, flags)
        ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/re/_parser.py", line 984, in parse
    raise source.error("unbalanced parenthesis")
re.error: unbalanced parenthesis at position 15
corn,  n\.,  grain\. -> leaf 196 markers [] page ~ None
carl,  n\.,  a  fell -> leaf 137 markers ['240'] page ~ 240
grain,  n\.,  seed,  -> leaf 363 markers [] page ~ None
gravy,  n\. -> leaf 365 markers ['677'] page ~ 677
Caroline,  fem\.  PN -> leaf 138 markers ['243'] page ~ None
```


## [2026-09-05T21:11:44.367Z] AGENT

You've hit your session limit · resets 7:40pm (America/Toronto)
