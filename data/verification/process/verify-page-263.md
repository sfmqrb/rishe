# Verification process log — verify-page-263


## [2026-09-06T20:34:18.863Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 263 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-263.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-263.json. Write /home/sfmqrb/git/rishe/data/verification/page-263.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 263` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T20:34:20.539Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T20:34:21.173Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T20:34:21.189Z] TOOL RESULT

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


## [2026-09-06T20:34:21.191Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-263.txt"
}
```


### [2026-09-06T20:34:21.212Z] TOOL RESULT

```
1	=== PDF page 263 (book page 233) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Keu 3, Kou, Skeu 3, Skou : to watch, see, hear  (refs POK:587)
4	#1 (parent #0) [Avestan] refs=HRN:196; FAF:504 | kavi : sovereign ; kâvâ-usân : rich king
5	  #2 (parent #1) [Pahlavi] refs=HRN:196 | kay : king ; kayos : rich king
6	  #3 (parent #1) [Sogdian] refs=SOD:202 | qwy : giant, hero
7	    #4 (parent #2) [Persian] refs=BQT:1749-1751; MON:3147; FAF:491,504 | kay 2 «کی ۳» : king ; Kâvŭs «کاووس» : "rich king", a male name ; kîyâ «کیا» : a respected person in a group ; kîyân «کیان» : kings | extra: کیقباد ، کیخسرو ، کیکاووس
8	قابوس
9	کیانوش
10	کیانی
11	#5 (parent #0) [Persian] refs=POK:588; ZAW:81 | šokuh «شُکوه» : glory
12	#6 (parent #0) [Sanskrit] refs=POK:587; HRN:196 | kavî : wise, sovereign
13	#7 (parent #0) [Avestan] refs=WLD:1369; POK:587 | čevîšî : attend, expect, hope
14	  #8 (parent #7) [None] refs=None | 
15	#9 (parent #0) [Old Persian] refs=POK:588 | au-šaudîhtwei : to trust
16	  #10 (parent #9) [None] refs=None | 
17	#11 (parent #0) [Greek] refs=AHD | akavein : to hear ; kudos : glory
18	  #12 (parent #11) [French] refs=None | acoustique
19	    #13 (parent #12) [Persian] refs=VOP:15 | âkŭstîk «آکوستیک» : acoustic
20	  #14 (parent #11) [English] refs=None | acoustic ; kudos : glory
21	#15 (parent #0) [Latin] refs=AHD | cavěre : to watch
22	  #16 (parent #15) [English] refs=None | caveat, caution, precaution
23	#17 (parent #0) [Germanic] refs=AHD | haujjan : to hear ; skauuon : to look, show
24	  #18 (parent #17) [English] refs=None | hear, show
25	--- entry 1 ---
26	ROOT Keu 3 -> redirect to Skeu 2
27	
```


## [2026-09-06T20:34:24.227Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-263.json",
 "description": "Read source JSON page 263"
}
```


### [2026-09-06T20:34:24.266Z] TOOL RESULT

```
{
  "pdf_page": 263,
  "book_page": 233,
  "entries": [
    {
      "root": {
        "name": "Keu 3, Kou, Skeu 3, Skou",
        "lang": "Indo-European",
        "refs": "POK:587",
        "gloss": "to watch, see, hear"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HRN:196; FAF:504",
          "words": [
            {"translit": "kavi", "gloss": "sovereign", "script": null},
            {"translit": "kâvâ-usân", "gloss": "rich king", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:196",
          "words": [
            {"translit": "kay", "gloss": "king", "script": null},
            {"translit": "kayos", "gloss": "rich king", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:202",
          "words": [
            {"translit": "qwy", "gloss": "giant, hero", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1749-1751; MON:3147; FAF:491,504",
          "words": [
            {"translit": "kay 2", "gloss": "king", "script": "کی ۳"},
            {"translit": "Kâvŭs", "gloss": "\"rich king\", a male name", "script": "کاووس"},
            {"translit": "kîyâ", "gloss": "a respected person in a group", "script": "کیا"},
            {"translit": "kîyân", "gloss": "kings", "script": "کیان"}
          ],
          "script_extra": "کیقباد ، کیخسرو ، کیکاووس\nقابوس\nکیانوش\nکیانی",
          "note": null,
          "quote": {
            "text": "ای دربر سران قوی دل نهفته سر - وی بر دل کیان مبارز نهاده کی",
            "poet": "Osmân Mokhtârî"
          }
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Persian",
          "refs": "POK:588; ZAW:81",
          "words": [
            {"translit": "šokuh", "gloss": "glory", "script": "شُکوه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:587; HRN:196",
          "words": [
            {"translit": "kavî", "gloss": "wise, sovereign", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Avestan",
          "refs": "WLD:1369; POK:587",
          "words": [
            {"translit": "čevîšî", "gloss": "attend, expect, hope", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:588",
          "words": [
            {"translit": "au-šaudîhtwei", "gloss": "to trust", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "akavein", "gloss": "to hear", "script": null},
            {"translit": "kudos", "gloss": "glory", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "acoustique", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "VOP:15",
          "words": [
            {"translit": "âkŭstîk", "gloss": "acoustic", "script": "آکوستیک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 11,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "acoustic", "gloss": null, "script": null},
            {"translit": "kudos", "gloss": "glory", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "cavěre", "gloss": "to watch", "script": null}
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
            {"translit": "caveat, caution, precaution", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "haujjan", "gloss": "to hear", "script": null},
            {"translit": "skauuon", "gloss": "to look, show", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "hear, show", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Keu 3",
        "redirect": "Skeu 2"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-06T20:34:24.659Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T20:34:24.699Z] TOOL RESULT

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


## [2026-09-06T20:34:29.305Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','FAF','SOD','ZAW','VOP','WLD','BQT','MON','AHD']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:900])\n    print('---')\n\""
}
```


## [2026-09-06T20:34:29.326Z] TOOL CALL #6: Bash

```json
{
 "command": "head -60 data/verification/page-259.json"
}
```


### [2026-09-06T20:34:31.222Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
---
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
---
FAF {"title": "A. Daneshgar, Farhang-e A'lam-e Farsi, Hafez Novin 1370/1991", "kind": "none", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}
---
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "loca
---
ZAW {"title": "C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 1906", "edition_found": "1906 - Google Books record only", "kind": "google_books", "url": "https://books.google.com/books?id=agDP0HdEssEC (full view; PDF downloaded) ; also 8q0zAQAAMAAJ (full view) ; HathiTrust coo.31924026891675 (pdus)", "identifier": "agDP0HdEssEC", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW/ZAW_pages.txt"], "page_offset": "ZAW_pages.txt: 306 leaves; printed = leaf(1-based) − 24 (leaf 60 = p.36; leaf 20 = p.X).", "lookup_hint": "Google Books page reports 'Preview' from this location, but the 1906 book is public domain and is listed on Google Play Books, so full view may be available depending on region; t
---
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}
---
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_
---
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
---
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
---
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
---
```


### [2026-09-06T20:34:31.255Z] TOOL RESULT

```
{
  "pdf_page": 259,
  "book_page": 229,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-06",
  "entries": [
    {
      "entry": 0,
      "root": "Kerd 1, Kred",
      "verdict": "confirmed",
      "modern_form": "PIE *ḱḗr, oblique stem *ḱr̥d- (root *ḱerd-) 'heart'; with the compound *ḱred-dʰeh₁- 'to place one's heart, trust'",
      "note": "Pokorny p.579 bottom–580 heads the entry exactly '(kered-:) kerd-, kērd-, kr̥d-, kred- ‘Herz’', so Nourai's headword 'Kerd 1, Kred', the language label 'Indo-European' and the gloss 'heart' all reproduce his source correctly; AHD (Watkins) has 'kerd-1. Heart. [Pok. kered- 579.]'. The one substantive caveat concerns the 'kred-' half: Pokorny himself (p.580) says the kred-dhē- 'believe' group is 'nicht hierher' (not to be connected with 'heart'), and Buck 17.15, Klein s.v. heart and Ernout–Meillet s.v. cor agree; modern standard works (Watkins/AHD, de Vaan 2008 s.v. crēdō, Wiktionary) do connect it, analysing *ḱred-dʰeh₁- as 'to place one's heart'. Nourai therefore follows the newer, now dominant, view — but not the page of Pokorny he cites. The Iranian branch has a further complication that the chart passes over: Indo-Iranian shows a voiced aspirate initial (Skt. hṛd-, Av. zərəd-, PII *ȷ́ʰā́rd) where *ḱ- is expected, 'unexplained voiced aspiration' (Wiktionary), 'mit init. as if fr. IE gh, due to a blend with some other word' (Buck 251).",
      "note_fa": "ریشهٔ هندواروپایی آغازین *ḱḗr (ستاک غیرفاعلی *ḱr̥d-، ریشهٔ *ḱerd-) به معنی «دل، قلب» است و پوکورنی در ص ۵۷۹–۵۸۰ سرواژه را دقیقاً «kerd-, kērd-, kr̥d-, kred-: Herz» آورده؛ پس نام ریشه، برچسب زبانی و معنایی که نورایی داده درست است. تنها نکتهٔ محل بحث بخش kred- است: خودِ پوکورنی در ص ۵۸۰ پیوند kred-dhē- «باور داشتن» را با «دل» رد می‌کند و باک و کلاین و ارنو–مه‌یه نیز همین نظر را دارند، اما واتکینز (AHD)، دِ وان و ویکی‌واژه آن را می‌پذیرند و *ḱred-dʰeh₁- را «دل نهادن» می‌دانند؛ یعنی نورایی از دیدگاه نو پیروی کرده است نه از صفحه‌ای که به آن ارجاع داده. نکتهٔ دیگر آنکه در هندوایرانی به جای *ḱ- انسدادی واکدارِ دمیده دیده می‌شود (سنسکریت hṛd-، اوستایی zərəd-) که هنوز توضیح قطعی ندارد.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1%E1%B8%97r",
        "https://en.wiktionary.org/wiki/credo%23Latin",
        "https://www.etymonline.com/word/heart"
      ],
      "ref_check": [
        {
          "ref": "POK:579",
          "status": "supports",
          "note": "Pokorny IEW p.579 (bottom) – 580, read in POK_02.txt leaf 239–240 (awk 'BEGIN{RS=\"\\f\"} NR==239'): '(kered-:) kerd-, kērd-, kr̥d-, kred- ‘Herz’. Arm. sirt … gr. καρδία (att.), κραδίη (hom.) … lat. cor (aus *cord) … got. hairto, ahd. herza, ags. heorte, anord. hjarta n. ‘Herz’ (*ḱērd-on-)'. Exactly Nourai's root name and gloss."
        },
        {
          "ref": "SYN:251",
          "status": "supports",
          "note": "Buck, Selected Synonyms p.251 = §4.44 HEART (SYN.txt leaf 289, page number '251' printed in the running head above '4.44 HEART'): 'Most of the words for ‘heart’ belong to an inherited group … 1. IE *ḱerd-, etc., with gradation. Walde-P. 1.423 ff. Ernout-M. 219 f.'"
        }
      ],
      "consulted": [
        {
          "src": "AHD",
          "where": "Watkins 1985, s.v. kerd-1 (AHD_watkins1985.txt line 621)",
          "stance": "supports",
          "note": "'kerd-1. Heart. 1. Suffixed form *kerd-en- in Germanic *hertōn- in Old English heorte, heart: HEART. 2. Zero-grade form *kr̥d- in: a. Latin cor (stem cord-), heart … b. suffixed form *kr̥d-yā in Greek kardia … 3. Possibly *kred-dhə-, “to place trust” … in Latin crēdere, to believe. [Pok. kered- 579.]' — the whole chart in one entry."
        },
        {
          "src": "WLD",
          "where": "Walde-Pokorny I 423 f. (cited by POK and by Buck 4.44; only Band III index available locally, WLD_band3.txt line 2965 'kerd- 423')",
          "stance": "supports",
          "note": "Both Pokorny and Buck refer the 'heart' root to WP. I 423 f.; the local library holds only the Register volume, whose index line points to that page."
        },
        {
          "src": "IEC",
          "where": "Mann, s.vv. Kerd- and Kr̥d- (IEC.txt lines 8676, 9088)",
          "stance": "supports",
          "note": "'Kerd- (Kerdis, ā, io) “heart, core, centre”. Cf. Kr̥d-. WP I, 424' and 'Kr̥d- (Kr̥ds, Kr̥diiom, iio) “core, centre, heart” … Hitt. kar-, ds kardi … Gk. kardia; Lat. cor, gs cordis …'"
        },
        {
          "src": "LAT",
          "where": "Ernout–Meillet p.254–255 s.v. cor (LAT.txt leaf 272–273)",
          "stance": "partial",
          "note": "'Le nom du “coeur” … est au fond le même dans toutes les langues indo-européennes. Il est probable que le nominatif-accusatif était de la forme *ḱerd, conservée dans hitt. kir … gr. κῆρ, v.pruss. seyr, et que les autres cas reposaient sur *ḱr̥d-'; but adds 'Pour le rapport qu'on a envisagé, sans raison, avec crēdō, v. ce mot' — i.e. rejects the 'Kred' half."
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Avestan",
```


## [2026-09-06T20:34:58.031Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==243||NR==244||NR==245' POK_02.txt | head -200"
}
```


## [2026-09-06T20:34:59.022Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"keu-\" AHD_watkins1985.txt | head -30; echo ===; grep -n -i \"kudos\\|akouein\\|acoustic\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T20:34:59.833Z] TOOL RESULT

```
f.  , Brassen,  Blei  (Fisch)*, Icirslys  m.  ,Asche';    die  Intonation  von  kersas  paßt  aber   nicht  zum  Ai.;
schwed.  norw.  harr  , Asche'  (*harzu-)]  ags.  Jieard-hara,  heardra-  m., nhd.  holL  harder,  herder  , Meer- Asche'.
WP.  I  428 f.,  Trautmann  118,  134 f.
/.  ker(s)-  , Borste,  steifes  Haar;  starren,  rauh  und  kratzig  sein'.
Ai.  *sala  in  kapucchala-  n.  ,Haar  am  Hinterhaupt';
mir.  carrach  ,schorfig,  räudig,  steinigt;  anders  oben  S.  532;
ahd.  Jiursti  ,cristas',  norw.  herren  , steif,  hart',  aisl.  herstr  ,rauh,  barsch^, mhd.  hersten  ^erstarren' ;  vielleicht  ahd.  as.  aisl.  här,  ags.  hcer  ,Haar'  von einer  s-losen  kürzeren  Wurzelf.  (Dehnstufe) ;
lit.  §erys  , Borste',  Seriüos,  sertis  , haaren,  Haare  lassen',  Hurkstüs,  siurg- zdüs  ,rauli';  ablaut.  ostlit.  §er§as  , Schauer';  lett.  sari  , Borsten';
slav.  *shrsth  {=  ahd.  hurst)  in  russ.-ksl.  shrsth  f.  , Wolle',  sloven.  srst , Tierhaar',  russ.  sersth  , Wolle',  ablaut.  russ.  söro§  m.  , rauhe  Oberfläche', abg.  v^sor^  ,rauh' ;  slav.  *shrch^  in  sloven.  srh  m.  , Schauer',  russ.-ksl. srhch^k^  ,TQaxvs\  sloven.  srhsk  , struppig'.
WP.  I  427,  Trautmann  305.
2.  kers-  jlaufen';  krso-s  , Wagen'.
Für  palatales  %  spricht  adgaai '  äfia^ac  Hes.,  das  wie  lat.  sarräcum,  serracum (ital.  -rr-  aus  -rs-)  ,ein  ausländischer  Wagen'  ein  illyr.  *sarsa  =  idg.  *Äfsä zur  Quelle  haben  könnte;
gr.  STti-novQog  ,zu  Hilfe  eilend'  (*korsos)]
lat.  curröj  -ere  , laufen'  (*krsö),  cursus  ,Lauf',  currus  , Wagen',  equirria »Wagenrennen'  {*equi-curria,  woraus  assimilatorisch  *equi-quinna  und haplologisch  equirria) ;
gall.  carros,  latinisiert  carrus  , Karren,  Wagen',  air.  mcymr.  carr,  bret. kai^r  ,biga,  vihiculum'  (*krsos)]  vgl.  mcymr.  carrawc  f.,  ncymr.  carrog , Sturzbach'  (*karsäkä  ,die  Laufende'?),  anders  oben  S.  532.
mhd.  hurren  ,sich  rasch  bewegen' ;  unsicher  ahd.  hros,  -ses,  aisl.  as.  hross, ags.  hors  , Pferd,  Roß'  (^himssa-),  and.  hers  ds.  (*herssa-),  da  das  -ss-  bei einer  auf  -s  ausl.  Wz.  höchstens  als  Konsonantenschärfung  in  einem  Kurz-
584  9
namen  verständlich  wre;  daher  eher  zu   einer   Dentalerweiterung   (:  ai. Urdati  ,hüpft,  springt')  der  nicht  palatalen  Wz.  {s)Jcer-  ,springen' ;
arm.  JcarJt  , Wagen'  ist  wohl  Lw.  aus  dem  Galatischen.
WP.  I  428  f.,  WH.  I  315  f.
kert-,  kerst-,  krät-  ,drehen^  zusammendrehen',  vielfach  vom  Biegen  und  Ver- flechten von  Ästen  zu  Flechtwerk ;  ,fest  zusammengedreht  =  kompakt, massiv,  Knorren',  Erweiterung  von  7.  ker-,  S.  574;  krti-  /Flecht- werk';  s.  unten  3.  (s)Jce
r-.
Air.  hrndtti  ,dreht  den  Faden,  spinnt',  Icarttar-  ,der  Spinner',  crtdH ,bindet,  heftet  zusammen',  Jcata-  m.  , Geflecht,  Matte'  (mind.  für  Vcrta-), wohl  auch  huti-,  kutl  f.  ,Hütte'  (""Jcrti),  Jcudya-  n.  {Hftya-)  ,(*geflochtene) Wand',  päli  Jcoccha-  ,Flechtwerk'  (ai.  Hrtsa-)-^  ai.  Jcrtsnd-  , vollständig, ganz'  (vgl.  lat.  crassus,  slav.  *(i'brstv^)]
gr.  yiCiQTal{X)og  m.  ,Korb',  ycQorcjvT]  ,Astknorren'  (*x^aTwvä);  mit  u-far- biger  Reduktionsstufe  ytvQrog,  y,vQTr]  ,Binsengeflecht,  Fischreuse,  Käfig-^^ -KVQtla  ,Flechtwerk' ;
alb.  hjerthull  ,Kreis,  Garnwinde,  Haspel'  (:  mir.  ceirtle  s.  unten);
lat.  crätis  ,Flechtwerk  aus  Ästen  oder  Ruten,  Hürde,  Rost,  Faschinen', crätes  dentatae  ,Eggen',  crätiö,  -Ire  ,eggen'  {^h^rdti-,  oder  *hräti-,  vgl.  lett. hrdüM,  lit.  Icrötai)  •  crassus  ,dick,  derb,  grob' ;  wahrscheinlich  cartilägo ,Knorpel'  (wohl  A*,r[a]^,  vgl.  palma:  Ttaldf^r])]
mir.  ceirtle  f.  ,Knäuel'  (^hertelia) ;  cert  f.  ,Fetzen,  Kleinigkeit' ;
got.  haürds  (*Jc2'tis)  ,Tür',  anord.  hurd  ds.,  as.  hurth  ,Geflecht',  ahd. hurd,  PI.  hu7'di  ds.,  nhd.  ,Hürde',  ags.  hyrdel  und  (alt)  hyrpil  , Flechtwerk';
unsicher  (^Tcert-s-to-,  *'krt-s-ti-?)  as.  liarst  m.  ,Flechtwerk,  Rost',  harsta ,Rost',  mnd.  harst  ds.,  ,Reisig,  Gebüsch,  Rost'  (wovon  mnd.  harsten^  ahd. hersten,  ags.  hierstan  ,rösten'),  norw.  dial.  rust  , Gehölz',  ags.  hyrst  m. ,Wald',  mnd.  hörst,  hurst  ,Gebüsch',  ahd.  hörst,  hurst  m.  ,Gebüsch',  nhd. Horst  ,Raubvogelnest' ;
apr.  corto  ,Gehege';  nasaliert  (wie  slav.  h'^[t]nci,ti)  vielleicht  lett.  Tcrietn» (wäre  lit.  "^kreMnas)  ,tüchtig,  tapfer'  (wenn  ursprüngl.  soviel  wie  russ. 'krut^,  s.  unten);
lit.  hrantas  ,steiles  Ufer';  vgl.  klr.  krutyj  ,gewunden,  steil,  schroff', hrüca  ,steiles  Ufer'  (Trautmann  142);
r.-ksl.  cr^stv^,  chrstv^  ,fest;  lauter,  echt',  russ.  fSerstVT>  ,hart,  trocken; fühllos;   altbacken',  serb.    cvrst   ,fest,  hart;  vollfleischig'  usw.   {^TcYt-tu-os)]
nasaliert  slav.  *lretati,  *lir^\t]nqti,  russ.  Irdtath,  krdnuth  ,von  der  Stelle bewegen,  umwerfen;  berühren',  sloven.  hr^tati  ,wenden,  lenken,  drehen, rücken'  usw.,  ablautend  *'kr(;>t^  in  russ.-ksl.  lzrut^  ,tortus,  immitis',  russ. 'krut^   ,drall;    jäh,  steil  (s.  oben   zu   lit.  hrantas)]    dick   eingekocht;   kalt;
585
hart;  strengt,  serb.  hrüt  ,heftig';  poln.  Ir^ty  ^drall;  gewunden,  krumm; o-edreht;  gekräuselt^,  ksl.  h-c^Uq,  krqtiti  s^  ,torqueri^,  russ.  Jcruiith  ^drehen, finden,  wirbeln,  schnüren^  usw.,  sloven.  hrotic
a  ,Knoten  im  Gespinst^, ßech.  Jcrutina  ,ds. ;  Windung:  Wiege^,  poln.  sTir^tka  ,WeidenseiF;
nach  Pedersen  Toch.  Sprachg.  hierher  toch.  B  Jcercclye  ,Palast^
WP.  I  421  f.,  WH.  I  285  f.,   Trautmann  142,  146.
^eS'  ,kratzen,  kämmen^;  ksu-ro-  ,Schermesser^
Gr.  'ASOTisov  (zur  Form  asg-äLov  s.  ßoisacq)  ,Werg^  {*'kes-'kes-)]
mir.  clr  f.  ,Kamm^  (*te-rä);
anord.  haddr  m.  ,Kopfhaar  der  Frau^  (*hazda-z)'^  ags.  heord  f.  ,Haar' (*hezda),  dazu  heordan  PL  ,Werg^,  engl,  hards,  mnd.  Jierde  ,Flachsfaser' ; Ude,  mnd.  hede,  heide  (ndl.  nhd.  Hede)  ,Werg^;
lit.  Jcasä  ,Haarflechte,  Zopf,  Jcasaü,  -yti  ,fortgesetzt  gelinde  kratzen^, 'kasii,  Jcästi  ,umgraben^,  lett.  Jcast  ,harken^,  Icasit  ,schaben;  scharren,  harken, kratzen^,  dazu  hasa  f.,  Jcasus  m.  kasJcis  m.,  , Krätze^;  ap'r.  hexti  f.  ,Zopfhaar, (entw.  von  einem  Partiz.  *Jcestas  oder  einem  *]coz-dho- =  germ.  *hazda-)'^
aksl.  cesg^  cesati  ,kämmen;  streifen,  abstreifen  (z.  B.  Beeren)^,  bulg. (usw.)  cesel  ,Kamm^,  Öech.  pa-ces  m.  ,Hede,  Werg^,  russ.  ceska  ,Hede,  Werg% Se^ujd  ,Schuppe^,  ^esotka  ,Krätze^;  ksl.  kosa  ,Haar^,  russ.  (usw.)  kosd , Flechte,  Zopf^,  ksl.  kosrm  ,Haar^;  aksl.  kosnqti  ,berühren,  anrühren^,  kasati s^  ,berühren^  (aus  ,zupfen^),  serb.  koslm^  -iti  ,laeerare,  vellere^  wohl  Iterativ zu  Cesati]  öech.  (usw.)  kochati  ,ergötzen,  liebkosen^  lieben^  (zu  kosnqtl  als ,liebkosend,  zärtlich  berühren^,  vielleicht  ,krauen';  vgl.  Berneker  152,  491, 538,  580  ff.).
Wurzelerweiterungen:
ks-en-  in  gr.  ^alvü)  (*ks7}iö)  ,kratze,  kämme;  walke,  prügle^,  ^dviov ,Kamm  zum  Wollekrempeln^,  ^dai^ia  ,gekrempelte  Wolle'^,  ini^rjyov  , Klotz, Haublock^ ;
lat.  sentis  {*ksen-tis)  ,Dornstrauch*,  sentus  ,horridus'^  (bei  Prudeniius ,dornig^) ;
ks-n-eu-  in :
ai.  ksnäuti  ,schleift,  wetzt,  reibt^,  ksnötra-  n.  ,Schleifstein^,  Partiz. ksnutd-  av.  hu-xsnuta-  ,gut  geschärft^;
lat.  novacula  ,Schermesser,  Rasiermesser^  (auf  Grund  eines  Verbums *novä7'e  aus  "^ksneuä-)]
anord.  snegg?'  _,kurzgeschoren^,  snodenn  ,kahl  geschoren^ ;  snaud?'  ,un- verhüllt,  arm',  ags.  besnyddan  ,berauben^,  mhd.  hesnoten  ,spärlich,  arm^, mcede  ,gering,  schwach^,  nhd.  schnöde.
ks-es-  in:  gr.  ^eco  (^ks-es-o),  Aor.  ^iaaat  ,schaben,  glätten^,  ^eorög  ,ge- schabt^;
586  9
ks-eu-  in:
ai.  Jcsurd-  m.  .Schermesser,  Dornpflanze';  npers.  sor  .salzig',  kurd. §ür  ds.;
gv.  ^iü)  .schabe,  reibe,  glätte',  Partiz.  ^varög  ,geschabt,  geglättet',  -(j^i ,(geglätteter)  Speerschaft',  ^va^ia  .Abschabsei',  ^varga  .Striegel'.  Jwtijq .Schabeisen',  ^
```


### [2026-09-06T20:34:59.890Z] TOOL RESULT

```
Exit code 1
622:keu-?
623:(SCARCE). 3. Greek karpos, fruit: -cARP, CARPEL, CARPO-, -CARPOUS. [In Pok. 4. sker- 938.] kers-'. Dark, dirty. 1. Suffixed form *ker(s)-no- in Rus- sian chérnyi (feminine chérnaya), black: CHERNOZEM. 2. Suffixed zero-grade form *krs-no- in Sanskrit krsna-), black, dark: KrisHNa. [Pok. kers- 583.] kers-2. To run. Zero-grade form *krs-. 1. Latin currere (past participle cursus), to run: CORRIDOR, (CORSAIR), COURANTE, COURIER, COURSE, CURRENT, CURSIVE, CUR- SOR, CURULE; CONCOURSE, CONCUR, DECURRENT, DIS- COURSE, EXCURSION, HUSSAR, INCUR, INTERCOURSE, OCCUR, PERCURRENT, PRECURSOR, RECOURSE, RECUR, succor. 2. Suffixed form *krs-o- in Gaulish carros, a wagon, cart, in: a. Latin carrus, a two-wheeled wagon: CAR, CAREER, CARGO, CARICATURE, CARIOLE, CAROCHE, (CARRY), CHARGE, CHARIOT; b. Latin carpentum, a two- wheeled carriage: CARPENTER. [Pok. 2. fers- 583.] kert-. To turn, entwine. I. Zero-grade form *krt-. 1. Suf- fixed form *krt-i- in Germanic *hurdiz, wickerwork frame, hurdle, in: a. Old English hyrdel, hurdle, frame: HURDLE; b. Old French hourd, fence, hurdle, scaffold: HOARDING. 2. Suffixed form “*krt-sti- in Germanic *hur- sti- in Old High German hurst, thicket: Horst. II. Per- haps suffixed variant form *krot-i- in Latin crdatis, wickerwork hurdle: CRATE, GRATE?, (GRID), GRIDDLE; (GRIDIRON). [Pok. kert- 584.] kes-'. To scratch. 1. Germanic *hezd6 in Old English heordan, coarse parts of flax: HARDS. 2. Extended form *kseu- in Greek xuein, to scrape: XYSTER. 3. Nasalized form *ks-n-eu- in: a. Germanic *snaww- in Old Norse snéggr, “close-cropped,” perhaps akin to the source of snuG!: b. Latin novdcula, razor: NOVACULITE. [Pok. kes- 585.] kes-2. To cut. Variant kas-. 1. Suffixed form *kas-tro- in: a. Latin castrare, to castrate: CASTRATE; b. Latin cas- trum, fortified place, camp (perhaps “separated place”): CASTLE. 2. Suffixed form *kas-to- in Latin castus, chaste, pure (< “cut off from, free of, faults”): CASTE, CHASTE; CASTIGATE, INCEST. 3. Suffixed (stative) form *kas-é- in Latin carére, “to be cut off from,” lack: CARET. 4. Ex- tended geminated form *kasso- in Latin cassus, empty, void: (CASHIER), QUASH. [Pok. hes- 586.] kes-°. To order. Suffixed 0-grade form *kos-mo- in Greek kosmos, order: COSMOS; MACROCOSM, MICROCOSM. keu-' Also ekeu-. To perceive, see, hear. O-grade form *akou-. 1. Extended form *kous- in: a. Germanic *haus- Jan in (i) Old English hieran, to hear: HEAR (ii) Old English he(o)rcnian, to harken: HEARKEN; b. suffixed form *9-kous-yo- in Greek akouein, to hear: ACOUSTIC. 2. Variant *skou- in: a. Germanic *skauwon in (i) Old English scéawian, to look at: SHOW (ii) Flemish scauwen, to look at: SCAVENGER; b. Germanic *skaunjaz in Mid- dle Dutch schoon, beautiful, bright (< “conspicuous, attractive”): SCONE; Cc. Germanic *skauniz in Old Eng- lish sciene, bright, sheen: SHEEN. [Pok. 1. keu- 587.] keu-?. Base of various loosely related derivatives with assumed basic meaning “to bend,” whence “a round or hollow object.” I. Extended forms *keub-, *keup-. 1. Ger- manic *haup- in: a. Old English héap, heap: HEAP; b. Dutch hoop, heap, troop: FORLORN HOPE. 2. Germanic *hupp-, to leap (by first bending the legs), in Old English hoppian, to hop: HoP!. 3. Germanic *Aupiz in Old Eng- lish hype, hip: H1P!. 4. Zero-grade form *kup-, vessel, in: a. suffixed form *kup-s- in Greek kupselé, chest, hollow vessel: CYPSELA; b. long-vowel form *kip- in (i) Ger- manic *Aifi- in Old English hyf, hive: HIVE (ii) suffixed form *kip-a in Latin cupa, tub, vat: CUPOLA, CUPULE; c. expressive form *kupp- in Late Latin cuppa, drinking vessel: cup. 5. Zero-grade form *kub- in: a. Greek kubos, cube: CUBE; b. suffixed form *kub-@- in (i) Latin cubdre, to lie down on (< “to bend down, prostrate”): COUVADE, COVEY, CUBICLE; CONCUBINE, INCUBATE, SUCCUBUS (ii) Latin cubitum, elbow: CUBIT; Cc. nasalized form *ku-m-b- in (i) Latin -cumbere, to lie down, recline: ACCUMBENT,
625:DECUMBENT, INCUMBENT, PROCUMBENT, RECUMBENT, SUCCUMB (ii) Greek kumbé, boat, bowl: (CEMBALO), (CHIME!), CYMBAL, CYMBIDIUM; d. aspirated long-vowel form *kiibh- in Greek Ruphos, bent: KYPHOSIS. II. Ex- tended o-grade form *kouk-. 1. Suffixed form *kouk-o- in: a. Germanic *hauhaz, “arched,” high, in Old English héah, high: HIGH; b. Germanic *hauhitho in Old English héhthu, héahthu, height: HEIGHT. 2. Germanic *huk- in: a. Middle Low German héken, to bend, squat, bear on the back, peddle: HAWKER; b. Old Norse hokra, to crouch, akin to the Scandinavian source of HUNKER; c. Middle Dutch hokester, “one who squats,” peddler, perhaps akin to the source of Middle English hukster, peddler: HUCKSTER. III. Reduplicated form *ka-ku-bh- in Latin caciimen, summit, point (< “arch, vault’): CACUMINAL. [Pok. 2. keu- 588.]
627:keub-. Thorn. Germanic *heup- in Old English héope, brier, seed vessel of the wild rose: HIP’. [Pok. keub- 595.] keue-!. To pay attention, perceive (preternaturally). 1. Suffixed o-grade form *kous-o- becoming *kaw- in denominative

... [11898 characters truncated] ...

nk(h)o- CONCHO- konk(h)o- CONCIERGE servus CONCILIATE kela-2 CONCISE kae-id- CONCLAVE kleu-3 CONCLUDE kleu-3 CONCOCT pekw- CONCOMITANT ei-1 CONCORD kerd-1 CONCOURSE kers-2 CONCRESCENCE ker-3 CONCRETE ker-3 CONCUBINE keu-2 CONCUPISCENCE kwép- CONCUR kers-2 CONCUSS kwét- CONDEMN dap- CONDENSE dens-2 CONDESCEND skand- CONDIGN dek-1 CONDIMENT dhé-1 CONDITION deik- CONDOLE del-3 CONDONE do- CONDOTTIERE deuk- CONDUCE deuk- CONDUCT deuk- CONDUPLICATE dwo- CONE k6-
1397:COUPLE ap-! COURAGE kerd-1 COURANTE kers-2 COURIER kers-2 COURSE kers-2 COURT gher-1 COURTEOUS gher-1 COURTESAN gher-1 COURTESY gher-' COURTIER gher-1 COUSIN swesor- COUTH gnd- COUTURE syi- COUVADE keu-2 COVE! ku- COVEN gWa- COVENANT gWa- COVER wer-5 COVET kwép- COVEY keu-2 cow! gWou- cow2 ku- COWER ku- COWSLIP gWou-, sleubh- coxa koksa
1402:CUBE keu-2 CUBICLE keu-2 CUBIT keu-2 CUCKING STOOL kakka- CUD gWet-1 CUDGEL ku- CUESTA kost- CUIRASS sker-1 CUISINE pekw- CUISSE koksa CULET (s)keu- CULINARY pekw- CULLET kwel-1 CULLIS kagh- CULM! kolem- CULMINATE kel-6 CULOTTES (s)keu- CULT kWel-1 CULTIVATE kwel-1 CULTRATE skel-1 CULTURE kvel-1 CULVER kel-5 cum kom CUMMERBUND bhendh-, kamer- CUMULATE keue-2 CUMULUS keue-2 CUNCTATION konk- CUNNILINGUS leigh-, (s)keu- CUNNING gné- CUNT ku-
1403:cup keu-2
1404:CUPID kwép- CUPIDITY kwép- CUPOLA keu-2 CUPULE keu-2 CUR gere-2 CURATE cura CURATOR cira CURB sker-3 CURD greut- CURE cira CURETTE cira CURIA wWi-ro- CURIO cira CURIOUS cira CURL ger-2 CURRENT kers-2 CURRIER sker-1, CURSIVE kers-2 CURSOR kers-2 CURT sker-1 CURTAL sker-1 CURTILAGE gher-1 cuRTSY gher-* CURULE kers-2 CURVATURE sker-3 CURVE sker-3 CURVET sker-3 CUSHION koksa
1406:cUsK ters- CUSPIDOR spyeu- CUSTOM s(w)e- CUTANEOUS (s)keu- CUTICLE (s)keu- CUTIN (s)keu- cuTIs (s)keu- cuTLass skel-1 CUTLET kost- CUTTLE ku- CYCLE kwel-1 CYCLO- kwel-1 CYCLOID kwel-1 CYCLONE kWel-1 CYCLOSIS kwel-1 CYGNET keuk- CYGNUS keuk- CYLINDER skel-3 CYMA keue-2 CYMBAL keu-2 CYMBIDIUM keu-2 CYNIC kwon- CYNOSURE kwon-, ors- CYPRIPEDIUM ped-1 CYPSELA keu-2 cysT kwes- CYSTO- kwes- -CYTE (s)keu- cyTo- (s)keu-
1416:DECEIVE kap- DECEMBER dekm DECEMVIR dekm, wi-ro- DECENARY dekm DECENNIUM at-, dekm DECENT dek-! DECI- dekm DECIDE kae-id- DECIDUOUS _ kad- DECIMAL dekm DECIMATE dekm DECK! (s)teg- DECK? (s)teg- DECKLE (s)teg- DECLAIM kele-2 DECLARE kele-2 DECLINE klei- DECLIVITY kKlei- DECOCT pekw- DECOLLATE! kWwel-1 DECOLLETE kwel-1 DECOR dek-! DECORATE dek-1 DECOROUS dek-1 DECORTICATE sker-1 DECOY keue-2, to- DECREASE ker-3 DECREE krei- DECREPIT ker-2 DECREPITATE ker-2 DECUMBENT keu-2 DECUPLE dekm, pel-3 DECURRENT kers-2 DECUSSATE dekm DEDANS en DEDICATE deik- DEDUCE deuk- DEDUCT deuk- DEED dhé-1
1533:FORE- pert FORECLOSE dhwer- FOREFATHER per, peter- FOREGO! ghé- FOREIGN dhwer- FOREMOST per! FORENSIC dhwer- FOREST dhwer- FORESTALL | stel- FORFEIT dhé-1, dhwer- FORFICATE bherdh- FORGE! dhabh- FORGET ghend- FORGIVE ghabh- FORGO ghé- FORLORN leu-! FORLORN HOPE keu-?, leu-1 FORM merph- FORMAL merph- FORMER? per! FORMIC morwi- FORMICARY morwi- FORMICIVOROUS morwi- FORMULA merph- FoRNAX gWher- FORNICATE gWher- FORSAKE sag- ForT bhergh-2 FORTALICE bhergh-2 FORTE! bhergh-2 FORTE? bhergh-2 FORTH pert FORTIFY bhergh-2 FORTIS bhergh-2 FORTISSIMO bhergh-2 FORTITUDE bhergh-2 FORTRESS bhergh-2 FORTY kWetwer- FORUM dhwer- Fossa bhedh- FOSSE bhedh- FossIL bhedh- FOSSORIAL bhedh- FOSTER pa- FOUDROYANT bhel-1 FOUL pu-2
1579:HAG2 kau-2 HAGGARD kagh- HAGGLE kau-2 HAGIO- yag- HAIL! kaghlo- HAIL? kailo- HAKE keg- HALBERD bhardha, kelp- HALE! kailo- HALE? kele-2 HALF skel-1 HALIBUT bhau- HALL kel-2 HALLOW kailo- HALO-  Sal-1 HALT! kel-3 HALT? kel-1 HALTER! kelp- HALTER? § sel-4 HAM konemo- HAMADRYAD deru, sem-! HAME_ tkei- HAMLET tkei- HAMMER ak- HANDIWORK kom HANDSEL sel-3 HANG konk- HANKER konk- HANUMAN genu-2 HAP kob- HAPLESS kob- HAPLOID pel-3, sem-1 HAPPEN kob- HAPPY kob- HARANGUE koro- HARBINGER koro- HARBOR koro- HARD kar-1 HARDS_ kes-! HARDY! = kar-1 HARE kas- HARM kormo- HARMONY ar- HARNESS _nes-1 HARPOON  serp-1 HARPSICHORD ghere- HARQUEBUS keg- HARRY koro- HART ker-1 HARTEBEEST ker-1 HARUSPEX ghere- HARVEST kerp- HASH! =skep- HASLET ghasto- HASTATE ghasto- HAT kadh- HATCHET skep- HATE kad- HATRED ar-, kad- HAUBERK kWel-1 HAUGH kel-2 HAUGHTY al-3 HAUL kele-2 HAULM kolem- HAUNT tkei- HAUSTELLUM aus-2 HAUSTORIUM aus-2 HAUTBOY al-3, busk- HAVE kap- HAVEN kap- HAW2 kagh- HAWK! kap- HAWKER keu-2 HAWSE kWel-1 HAWSER al-3 HAY kau-2 HAZEL koselo- HE! ko-
1580:HEAD kaput HEAL kailo- HEALTH kailo- HEAP keu-2 HEAR keu-! HEARKEN keu-! HEART kerd-* HEARTH ker-4 HEAT kai- HEATH kaito- HEATHEN kaito- HEAVE kap-
1587:HEEL? kel-4 HEGEMONY sag- HEIFER per-3 HEIGHT keu-2 HEINOUS kad-
1605:HIDE! (s)keu- HIDE? (s)keu- HIDE? kei-1 HIDROSIS sweid-2 HIE kigh- HIEMAL = ghei-2 HIERARCH eis-! HIERARCHY eis-! HIERATIC  eis-1 HIERO- eis-1
1608:HIEROPHANT bha-!, eis-1 HIGH keu-2
1618:HINGE konk- HINTERLAND ko-, lendh-2 HIP! keu-2
1625:HIVE keu-2
1627:HOARD (s)keu- HOARDING kert- HOCK! kenk-3
1645:HOP! keu-2
(eval):1: == not found
```


## [2026-09-06T20:35:10.232Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=246 && NR<=248' POK_02.txt"
}
```


## [2026-09-06T20:35:10.986Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '626,630p' AHD_watkins1985.txt"
}
```


### [2026-09-06T20:35:11.953Z] TOOL RESULT

```
vgöv  (:  ai.  ksurd-)  ,Schermesser',  ^vgöv  toiiöv,  loy(y6v^  d^v Hes. ;  ^oavov  (*ks-ou-,nom)  ,alles  Geschnitzte',  bes.  ,Götterbild';  ^
gr.  ^(barga'  xpr]yirgig,  iprjTcrgta  Hes.  (,Striegel'),  eher  mit  ]csö[u]-  hierher, als  mit  *Jcsös-  zur  Wurzelf.  Jcs-es-;
hierher  wohl  mit  Metathese  halt.  *skuuö  ,rasiere'  in  lett.  sJcuvu,  sJcüt, lit.  sJcutü,  sküsti  ds.  ij
WP.  I  449  ff.,  WH.  I  178  f.,  Trautmann  119  f.,  268,  Specht  Idg.  Dekl 239,  250,  Kuiper  Nasalpräs.  85  a.
kes-  .schneiden' ;   kcS-tro-m  ,Schneidewerkzeug,  Messer'.
Ai.  Sästi,  sdsati  ,schneidet.  metzelt'.  §asta-li  .niedergemetzelt',  sdstrd-  n? .Messer.  Dolch',  säsd-  m.  .Schlachtmesser';
gr.  ytsdKo)  .spalte'.  ev-y.€aTog  .leicht  zu  spalten',  y.eagvov  ,Axt,  Schuster- ahle':
alb.  thadre  (*Jcas-dhrä)  ,zweischneidige  Axt';
lat.  careö^  -ere  ,entbehren,  sich  enthalten,  vermissen',  osk.  hasit  .oportet'; ^o-Partizip.  lat.  castus  .frei  (von  Fehlern),  rein,  enthaltsam',  ursprüngl. .abgeschnitten,  getrennt';  davon  castigö  .rüge,  strafe';  Neubildung  ist cassus  ,leer.  eitel,  nichtig';  *kastrom  .Schneidewerkzeug'  (:  ai.  Sastrdm) wird  vorausgesetzt  von  lat.  caströ,  -äre  .abschneiden,  verschneiden,  kastrie- ren', castrum  .Lager'  als  .abgeschnittenes  Stück  Land',  osk.  Gen.  Sg. castrous  .fundi'.  umbr.  castruo,  Tcastruvuf  .fundos'  (ti-St.  nach  peku-  .Vieh');
mir.  cess  f.  .Speer'  (*kestä) ;
anord.  hes  f.  .Zapfen  im  Kuhstrick';
aksl.  kosa  f.  .Sichel.  Sense'  (k-  statt  s-  durch  Dissimil.  gegen  das  fol- gende s?).
WP.  I  448  f..  WH.  I  167.  178  ff.
kBt-,  kot-  .Wohnraum'  (ursprüngl.  .Erdloch  als  Wohngrube'?).
Av.  kata-  m.  .Kammer.  Vorratskammer.  Keller  od.  dgl.'  (:  got.  hepjö), npers.  kad  .Haus',  woraus  finn.  kota;  aber  über  anord.  kot  .schlechte Hütte',  kytja  .Hütte',  ags.  cot  .Hütte,  Kammer'  usw.  s.  oben  S.  393 f.;
got.  hepjö  , Kammer';
ksl.  kothcb  jcella,  Nest'  usw.;  falls  ,Wohngrube,  Loch  in  der  Erde'  die ursprüngliche  Bedeutung,  würden  sich  anreihen  lassen:
587
gr.   yiorvlriy  -KÖrvXog  ,Höhlung^,  weiter  ^hohles   Gefäß^  Schale^   Becher^: lat.  catlnui  ,eine  Schüssel  zum  Speisenauftragen^  (Demin.  catülus,  daraus
got.  hatilsy  dt.  Kessel,  daraus  wieder  abg.  Icotbh,  lit.  hätilas)  =  ags.  heden
^Kochgeschirr^
WP.  I  383  f.,  WH.  I  176,  182.
j.  keu-,  skeu-,  dehnstufig  keu-  _, worauf  achten  (beobachte"n,  schauen)^,  dann ^hören,  fühlen,  merken^;  schwere  Basis  kouQ-]  «-Erweiterung  keu-s-\ über  Formen  mit  anlaut.  s-  s.  am  Schlüsse;  irouo-s, sorgsam^;  cf-Erwei- terung  keud-  :  küd-  in  keudos  :  küd
os  ,Ruhm^
1.  Ai.  kavi-  ,klug,  weise;  Seher,  Dichter^,  Jcaväri-  ^eigennützig,  karg', d-kava-  ,nicht  geizig';  ä-küvatB  ,beabsichtigt',  a-hüta-  n.,  ä-hüti-  f.  , Absicht';
av.  (Sdvlst  1.  Sg.  Med.  Aor.  ,ich  erhoffte,  versah  mich';
gr.  Y.oe(ü  , merke,  höre'  (Denomin.  von  *houos]  =  lat.  caveö);  "^-Kofag  steckt in  ion.-att.  äva^wg  e'xsLv  ,Sorge  tragen' ;  dor.  ey,oäjj.€g '  '^y.ovaafMSv  Hes. ; xo/i^g,  y,0LÖX7jg'  Isgsvg]  y.oTov,  hcülov  svsxvqov,  xodcc,  y.wa'  ivixvQcc  Hes.; maked.  xotog, Zahl';  PN  ylGo-y,ö(f)a)v,  ^ao-y,6a}aa,  usw.;  y,vdog  n.  ,Ruhm' (s.  unten  zu  slav.  cudo);
von  der  Basis  keu-s- :  dxovo)  ,höre'  (*<Jxövö'iw),  äxorj,  hom.  dxovt]  ,Ge- hör'  (*äy,ovad),  v7trjy,oog  ,gehorsam,  Untertan',  lak.  iTrä-aoog  ,Zeuge',  dKSvsi' TTjQsZ  Hes.,  gort,  d'/.svovrog  (mit  altem  e-Vok.,  während  dy.ov(ü  von  *dy.ovad abhängt);  über  y,vöog  s.  unten;
dKOVü)  usw.  zunächst  mit  got.  hausjan  usw.,  s.  unten,  verwandt;  d-  ist kaum  =  n  ,^v',  sondern  =  ä-  (*ha-y.ovhtco,  *ha-'/.svhü))  durch  Hauchdissi- milation, oder  idg.  S7n-  ,zusammen';  anders  oben  S.  18,  wobei  dxsva)  Ab- ,  lautneubildung  sein  müßte  oder  fernzuhalten  wäre,  was  wenig  wahr- scheinlich ist;
lat.  caveö,  -Ire  ,sich  in  acht  nehmen,  sich  vorsehen'  {^covire,  Denom. von  *kouos)j  cautus  ,vorsichtig',  umbr.  kutef  wohl  ,*cautens',  ,vorsichtig' ;
got.  hausjan,  aisl.  heyra,  ags.  hieran,  as.  hörian,  ahd.  hör{r)en  , hören' (s.  oben);  dehnstufiges  "^keu-  in  ags.  häwian  ,schauen';
lett.  kavet  (:  lat.  cavere)  ,zaudern,  zögern';
wruss.  s-humd-ju,  -6  ,verstehen',  cech.  koumati,  s-koumati  ,merken,  ge- wahr werden'  (Denominativ  eines  {s)hou-mo-,  -mä);  abg.  cujg,  cuti  ,fühlen, merken',  serb.   cujem  cüti  ,hören,  fühlen'  (usw.;  *keu-)',
abg.  cudo,  -ese  ,Wunder',  cuditi  s§  ,sich  wundern'  (*keu-dos,  ablautend mit:)
gr.  ^vSog  ,Ruhm,  Ehre',  y-idiaTog  ,ruhmreichst',  eigentlich  ,wovon  man hört';
serb.  cüvati  ,hüten';  ursl.  *cevg,  *ceviti  in  aöech.  v^-Heviti,  na-v§-dieviti, heute  navHiviti  ,besuchen'.
588  9
keu-s-  in  russ.  dial.  cüchath  ^wahrnehmen,  hören',  sloven.  öiüia-m,  -u ,spüren/ ahnen';   6ech.   cicJi   ,Sinn,  Witterung-,  Spur';    vgl.  oben  zu  dxorw.
2.  Mit  anlautendem  s-:
miran.  iköli,  np.  silöh,  ^uJcöh  (uriran.  *islcaua&a-)  ,Pi-aeht,  Herrlichkeit, Majestät,  Würde' ;
arm.  cucanem  ,lasse  schauen,  zeige',  coyc  ,das  Zeigen,  Schau'  (sJceu-skö)-^
gr.  d'voayiöog  ,Opferschauer'^ ;
got.  us-skaws  ,(*ausschauend  =)  besonnen^,  ags.  sceawian^  as.  sJcauwön^ ahd.  scomvön  ^schauen' ]  aisl.  sJcygn  ,sehend',  skygginn  ,klar'_(*sZ;wüi;ini
-)^ wovon  skygna  ,spähen';  got.  skauns  ,schön^  (ihna-skauns  ,von  gleicher  Ge- stalt'), ahd.  scöni  ds.,  aisl.  skjöni,  as.  sköni  ,glänzend,  schön',  ags.  sclene ds.  (eigentlich  ,conspicuous') ;  tiefstufiges  *sku-ni-  in  aisl."  6%n  f.  n.  ,Ord- nung,  Bescheid,  Einsicht',  skynja  ,untersuchen,  verstehen';  aisl.  skoda ,spähen';
apr.  aw-sc/ia«c?i^i(;ei., vertrauen'.
WP.  I  368  ff.,  WH.  I  186  f.,  Trautmann  132.
2.  keu-,  keup-,  of   mit   labialen   oder   gutturalen    Erweiterungen:   ,biegen'
in  verschiedenen  Sonderungen  wie  ,im  Gelenk  biegen,   Gelenk,  sich
bücken,  sich  drehen^;   ,Einbiegung,  Einwölbung,  Höhlung^-   ,Ausbie-
gung,  Buckel,  runder  Haufen';  kubo-s,  kubbo-s  ,gehöhlt,  gekrümmt',
kumb{ti)o-s  ,Gefäß',  kupro-s  , Buckel',  küpä  ,Höhlung,  Hohlgefäß',
koupo-s  ,Berg,   Haufen^,   kouko-s    ,gewölbt^,    ka-kud-    ,Wölbung^
Zahlreiche  Parallelbildungen  von  der  Wz.  geu-  s.  dort,  vgl.  bes.  die
Gegenüberstellungen  bei  Persson  Beitr.  100  f.,  104  Anm.  1.  —  Über
den  Versuch  einer  Vermittlung  mit  (s)keu-  ,bedecken'  s.  dort.
Die  einf.  Wz.  in  ai.  kora-  m.  ,bewegliches  Gelenk^;  av.  fra-j  apa-kava-
,vorn,  hinten  buckelig'^;  klr,  külity  ,sich  zusammenziehen,  vor  Kälte^,  poln.
kulic  ,zusammenziehen,  krümmen'.
Ebenso  ist  die  Vorgeschichte  von  lett.  kuza  ,Kropf'  u.  dgl.  wegen  des Reimverhältnisses  zu  guza  usw.  nicht  sicher  zu  beurteilen,  s.  unter  geit- ,biegen'  oben  S.  395.
Unter  einer  Anlautvariante  kh  will  Petersson  KZ.  47,  277  hierher  stellen ai.  khölaka-  , Ameisenhaufe'  (auch  lit.  külys  ,Bund  Stroh'),  zuversichtlicher arm.  xoyl,  Gen.  xuli  ,struma,  scrofula',  russ.  suljata  ,Hoden',  serb.  Hljevi ,goldene  Ader'.
A.  Dentalerweiterung  (redupl.)  ka-ku-d-  ;  ai.  kakud-  ,Kuppe,  Gipfel', käküd-  ,Mundhöhle,  Gaumen',  kaküdmant-  ,mit  einem  Gipfel  oder  Hocker .    versehen';  lat.  cacümen  ,Spitze,  Gipfel'  (die  wew -Weiterbildung  wohl  nach acümen),  Grundbed.  ,Wölbung';    auf  ein  germ.  *hagu  =  ai.  kaküd-  führt    1
589
man    auch    afries.    heüa   ,Kopf^   zurück    {*hagila-,   mit   Suffixwechsel   für hagu-la-)]  vgl.  auch  ai.  kalcübh-  ^GipfeF  unter  ^Labialerweiterungen^
B.  Gutturalerweiterungen.
B.  I.  keu-g-:
aisl.  hüJca  ^kauern,  hocken^  (hüJcta,  st.  Partiz.  hohinn),  hoha,  hohra  ^krie- chen^;  heylciask  ^zusammensinken^  zusammenkriechen'^;.  mhd.  hüchen  , kauern, sich  ducken^,  nhd.  hocJcen-^  Schweiz,  hoch  m.  ^Haufe^,  tirol.  hocken  m. Haufe  Heu^;  mit  anlaut.  s-  mhd.  schoche  m.  .aufgeschichteter  Haufe  Heu u.  dgl/;  (mityfc/c:)  asächs.  sJcoJc  m.  ,60  Stück"^,  mhd.  schoc(7ces)  ,Haufe  Büschel, Anzahl  von  60  Stück^,  mengl.  shocJc  ,Haufe
```


### [2026-09-06T20:35:11.986Z] TOOL RESULT

```
kéu-. To burn, Zero-grade form *kau- becoming *kaw- in suffixed form *kaw-yo- in Greek kaiein, to burn: CALM, CAUSTIC, CAUTERY; ENCAUSTIC, HOLOCAUST, (INK). [Pok. 2, kéu- 595.]
keub-. Thorn. Germanic *heup- in Old English héope, brier, seed vessel of the wild rose: HIP’. [Pok. keub- 595.] keue-!. To pay attention, perceive (preternaturally). 1. Suffixed o-grade form *kous-o- becoming *kaw- in denominative (stative) Latin cavére, to beware, watch, guard against: CAUTION, CAVEAT; PRECAUTION. 2. Suf- fixed zero-grade form *ki-dos (< *kua-dos) in Greek kudos, magical glory: kuDos. [In Pok. 1. keu- 587.] keue-2. To swell; vault, hole. I. O-grade form *kouo-. 1. Basic form *kous- becoming *kaw- in Latin cavus, hollow, and cavea, a hollow: CAGE, CAVE, CAVERN, CA- VETTO, GABION, JAIL; CONCAVE, DECOY, EXCAVATE. 2. Suffixed form *kow-ilo- in Greek koilos, hollow: (-CELE2), -CELIAC, -COEL, COELOM. 3. Suffixed lengthened-grade form *kéw-o- in Greek kdos, hollow place, cavity (> kddeia, poppy head): CODEINE. II. Zero-grade form *ki- (< *kua-). 1. Suffixed shortened form *ku-m-olo- in Latin cumulus, heap, mass: CUMU- LATE, CUMULUS; ACCUMULATE. 2. Basic form *kd- in: a. suffixed form *ki-ro-, “swollen,” strong, powerful, in Greek kurios (vocative kurie), master, lord: CHURCH, (KIRK), KYRIE; b. suffixed form *kuw-eyo- in Greek kuein, to swell, and derivative kiima (< *ki-mn), “a swelling,” wave: CYMA. [Pok. 1. feu- 592.]
keuk-. To be white, be bright, shine. Suffixed zero-grade form *kuk-no- in Greek kuknos, swan: CYGNET, CYGNUS. [Pok. keuk- 597.]
kéwero-. North, north wind. 1. Germanic *skiira- in Old English scir, shower, storm: SHOWER}. 2. Germanic *skiré in Old Norse skiar, a shower, akin to the probable Scandinavian source of Middle English scouren, to range over: scour?, [Pok. kéuero- 597.]
kigh-. Fast, violent. Germanic *hig- in Old English higian, to strive, exert oneself: HIE. [Pok. kei-gh- 542.] kista. Basket. Greek kisté, basket (> Old English cest, box): CHEST, CIST!, CISTERN. [Pok. kista 599.]
```


## [2026-09-06T20:35:49.921Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN grep kavi/kai ===\"; grep -n \"196\\.\" HRN.txt | head -5; echo \"--- leaf for p196 = 217\"; awk 'BEGIN{RS=\"\\f\"} NR==217' HRN.txt | head -60"
}
```


## [2026-09-06T20:35:50.238Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"giant\\|qwy\" SOD_pages.txt | head -40"
}
```


### [2026-09-06T20:35:52.117Z] TOOL RESULT

```
=== HRN grep kavi/kai ===
11083:196. tuf/ 'stark, Held', takik (für aw. ta/ma-)^ takikth,
11919:bürden 196.
14289:p^6«r- * tragen* 196.
15053:I^fear- 'tragen* 196.
15698:bar am 196.
--- leaf for p196 = 217
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


### [2026-09-06T20:35:52.167Z] TOOL RESULT

```
941:UJJU; < (Giants.) ujy- v1^ <( Sogdica. ) u. jl, c—^i                   j JJU
2665:Book of the Giants" in BSOAS 11, 1945, pp. 52-74;
3530:    Ancient Letters". BSOAS 12, 1948, pp. 601-615; AI          Giants. Henning, W. B. "The Book of the Giants".
3599:   Ancient Letters". BSOAS 12, 1948, pp. 601-615; AI           Giants. Henning, W. B. "The Book of the Giants".
4092:   TSP; BSTBL; Frag. Len; STi 77.1; Hen. Giants.              BBB; W-Li, ii; GMS 865; Frag. Len.; KG pl77;
4193:      248, 356; TSP 2.585, 16.32; VJ 1233                     akuyde      (*qwytyy) ©pp.
4196:    space, void                                           148 "qwytyy   M =^ "kwyty
6706:       Giants. 70; }nYttc, STii 575                                    anyon     ©*hama-gauna-, MP; Parth. hangon
6780:      GMS 48, 141, 245; Hen. Giants. 68.14n6
7822:      aquatic                                                              GMS 99; *pzVykw, Hen. BSOAS 11; Giants. 70.4
8318:        sqwyny                                             1586 Wn     M                                          juJ
9778:                                                                          GMS 1084; BBB b69; Hen. Giants. 74.18; KG 536;
10020:       C2, 83V6 n pl63; Sund. AoFviii 1981, 91 V2                          43; Hen. Giants. 70.1; MSP; Frag. Len. 95.7
10112:         Hen. BSOAS    11 Giants. 69; MSP >yn*k(w)                        ind(e) 0yn8>y) ©Wakh. indi, gunfc Yidg. idiko
10222:           Giants. 70.17
11801:2805 bryny     C =* Pryny                                         Przkwe ? (Przqwyy)
11805:                                                             2819 przqwyy        M =* Przkwy(y)
16888:        GMS 1103; +ptJ3nd "life-line", Hen. Giants.          4609 jyyyr- M                              j^*'^ <o*'y-
17919:         kaw (kw'yst) ©nom. qwy; pi. kw(})yst =»qwy             ku5e/ynde/e ? ©<Skt. kudana; <*kudantaka
17920:         giant, hero                                            cangue(flrt instrument of torture)
17921:         C2, 13V19; Hen. Giants. BSOAS 11, 70.5                 Benv. TSP 1065; Hen. Texts. 724
17925:    5001 kvv'yst M =» qwy, qw1                                  quds(a) ©<Syr,
17932:         Mack. BSTBL, Dhu. 219 n p46; Bailey. Prolexis.         kuyune (qwywnyy)
17942:          qwywnyy
17949:         5015 qwywnyy -* kwywn>k
18119:5072 qwy      M, C, S ^o ^yU oy     j*)£ <ol^T «lAo«S <6y-        who, which, whose
18122:        giant, hero                                                 BSTBL, Dhu. 88; -kyywt, Anc. Lett. 2.49
18124:          128; BSTii 886.5 pi. kw(>)yst "giants" GMS 1186;   5086 ky'ty -» qyt
18126:5073 qwy'q C                                                      kec
18136:5075 qwynt C                                            ^k        worm
18148:5077 kwyt     S(AL)-* qwynt                                       whoever
18266:         TSP 7.82; STii 9.16, 18; GMS 953, 1585; Hen. AM           kiwand (qywnO) ^kym'nt, qwynt, k-
20012:     MDii; B Hen. Orientalia. 8, 94; MDiii p58-59               GMS 1049; Hen. BSOAS 11, Giants. 54n3                   ,
21834:       nis(t)ca (nscO ©f. pp. -^nyst'y, nsty                         niskaw     (nysq'w-) ©pres. & impf. =»nysqwyt-,
21867:                                                               6322 nysqwydV-        C                          u-^^Oj^
21874:         n pl84; 281 Add.; BSTBL pi 17 MD; Frag. Len.          6323 nysqwyt-       C                           0*1^03^
21877:6313 nys-1 B, M, C                 o^TjuIs < o^J'^j*-                GMS 56; BSTi 121, pp. nysqwYty
21879:       n*stk, nst-                                             6324 nysqwxd'r- ^ nysqwyd'r-
22825:      (to)address, OcOsay                                          packwerne     (pcqwyrny) ©pi. -tt
22829:                                                             6670 pcqwyrny      C =* pckwyrn'y
```


## [2026-09-06T20:36:03.102Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=18124' SOD_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -2; echo \"---- context\"; sed -n '18110,18130p' SOD_pages.txt; echo \"==== entry 5000 ctx\"; sed -n '17910,17930p' SOD_pages.txt; awk 'NR<=17925' SOD_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -1"
}
```


## [2026-09-06T20:36:03.915Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT kavi ===\"; grep -n \"kavi-\\|kav\\[a\\]y\\|kauua\" BRT.txt | head -30"
}
```


### [2026-09-06T20:36:05.147Z] TOOL RESULT

```
---- context
        crore, ten million                                        EGSii 131; GMS 402, 1503-7, 1581; S W, C2
        BSTBL, Dhy.; TSP 2.179, 8.107
                                                                    p214 n p84.4; kfty, kyy Hyy% "who", GMS
5069 kwty =* >kwt-(y), }kw(-)ty                                     1506, 1523
                                                             5083 qy C =* ky
5070 kww' *» kwl
                                                             5084 ky> B,M,S                       Jrf^i&itf
5071 kww2 -» kw2
                                                                  kya (kyy\ >kyZY, qy>) ©*kahya- ^>ky
5072 qwy      M, C, S ^o ^yU oy     j*)£ <ol^T «lAo«S <6y-        who, which, whose
                                                                  GMS 1450, 1508; BBB 758; TSP 5.18; STii 1.49;
        kawi (kw*yst) ©<Av. kavi ^qw1
        giant, hero                                                 BSTBL, Dhu. 88; -kyywt, Anc. Lett. 2.49
        Hen. BSOAS 11.53f; C2, 13V19; Benv. JA 1959,         5085 qy> C, M -» ky>
          128; BSTii 886.5 pi. kw(>)yst "giants" GMS 1186;   5086 ky'ty -» qyt
          Hen. BSOAS 11,70.15,68.12                          5087 kyc B                         (^r^W      jU^g/
5073 qwy'q C                                                      kec
                                              JjM^J^              stupefied, giddy
     kawyak    ©f. n.
     heroism, bravery
                                                                  Benv.
==== entry 5000 ctx
         ku (qw3, kww7) ©adv. postp. conj. =»'kw?, k'w'
         where
                                                           5010 kwS1     B, M                             -(T^jUitr
         EGSii 151f; GMS 1515, 1531; BBB 579; C2 gloss.         until
                                                                ko5a, kuS(a) ^'kwd*
           & n p66; S W, Sogdian kw and Slavonic ku,
           Sbornik IV, Moskva 1986, 116-21                      GMS p40
                                                                     1581; Hen. Tales. 476.4
    4998 qw' M, C                               uU^<J>     5011 kwS'ynty B                    {«*&. cJT ^y)*xt
         kaw (kw'yst) ©nom. qwy; pi. kw(})yst =»qwy             ku5e/ynde/e ? ©<Skt. kudana; <*kudantaka
         giant, hero                                            cangue(flrt instrument of torture)
         C2, 13V19; Hen. Giants. BSOAS 11, 70.5                 Benv. TSP 1065; Hen. Texts. 724
    4999 qw3    C -> k'w1, kw1                             5012 kwSprm => 'kw5prm
                                                                                                              -U7 i^S
    5000 qw3 C «* kw2                                      5013 qwds> C
    5001 kvv'yst M =» qwy, qw1                                  quds(a) ©<Syr,
    5002 kwb B                                                  consecration
                                                   ^r                                                                   j?

         ku/of ©<Av. kafa; Khwar. kfuk; Khot. kuva              C2 gloss.
         foam
```


### [2026-09-06T20:36:05.193Z] TOOL RESULT

```
=== BRT kavi ===
```


## [2026-09-06T20:36:12.134Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"pdf page\" SOD_pages.txt; grep -o \"\\[pdf page [0-9]*\\]\" SOD_pages.txt | head -3; echo \"===\"; grep -n \"pdf page\" SOD_pages.txt | awk -F: '$1<18119' | tail -2"
}
```


## [2026-09-06T20:36:13.303Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kavi\" BRT.txt | head -20; echo \"=== kav ===\"; grep -n \"^kav\\|kav\\[ay\\]\" BRT.txt | head -20"
}
```


### [2026-09-06T20:36:14.483Z] TOOL RESULT

```
0
===
```


### [2026-09-06T20:36:14.554Z] TOOL RESULT

```
9128:kaTucS  vlltaspö  Y.^j.a;  —  iava  vistiispö Ytj.  io8  usw.5>;  —  kavaitn  kaviltim  Yt IQ-Ti  usw.»;  —  iavöii  aipivai^A)us  \t. Ij.i3^  nsv/ß;  —  kai'aSm  usaöaium  Vt. 1(^-71  usw.**;  —  kti7-a  usa  VLJ.4S  usw.; —  iavdis  arsnö  Vt.  13.132  usw.** ;  —  iarms fisinaulß  Vt  JJ.  13z  usw.";  —  kavöis byarsiinS  Vt;_j.  132  usw. 5';  —  iavaim syävarsämm  Vt. /fj.?!  usw.*';  —  kavoU haosravaijhahe  Ny.  5.  5  usw. 5';  —  yat baun  Vispe  *d,iri'i.Aaire  kai'c  (NF.)  Vi.  /(?. 71*'.  2)  jAw,  Name  für  gewisse  Feinde des  Volks  und  Glaubens  der  Masdayasn^T: vTspamitn  tbihatqm  tbuuiii  diUvunam  mai- yänamra  y'f'ircum  pairikannmi'a  sä^rmii iaoyiim  {Gl'.)    'iara/nami'a 'Y.  (/■  tS;    Vt.
9513:?■  1,3, 9, 14;    —    pasävi^     adam     'ranA*   g-    kavi'tät-   f.   'die   Ä'<«/a>'(sd.)schaft': '''madyakä''uvS   aväkanam   (sd)  Bh.  i.  iB-/ '"'^"' ä  vlnJ/iasa  *iarap/^JSs(S{sd.) 'ihcJ
15404:•  j.  *para.kavist3ma-  Adj.  'der  das  Feme am  besten  trifft':  rasnvü  °ma  YL12.  7.
17398:Zum  J-Aor.  [büs-)  dtsV.bav-;  vgl. iültay- und ai.  prabAüfiSni.  Wegen  der  Bed,  s,  'nas-  No.  3. —  Pü.:  tardär  bin/isnlA  apiir  J^arläl U  amurtäl; Sü. :  svämino  bkaviiyanti,
21120:—  ava'ia  hz  boEsasim  {^A^  upBtsaytn  y*  ..  avai-antim  mas3  vikänayät  y  hi dahmäicil  V.  i_j.  35;  —  asti  U  haem  y  tanu!  ar?hat  V.  7,  51;  — -  xrüm  aiwi.pai- aiaunttu  V.  jj.  44;  44';  —  aiti  sZ  kaim  naiti  ai-avatcit  y  sükaya  nafum  (nämL y  tayaofy.j3.47-,  45-48^;  —  der  Ver-  asti)  Yl  14. 33;  33,  V.Ä  11,  39,  76, 9. 29; gleich  ist  unvollständig  ausgeführt:  aita  —  ya  vasttym  upattharitaiti  .  .  aruval yatna  .  .  faiii  avajasa  . .  avatthe  .  .ydia  aipi  y  narl  *ä'S:ravana  (nämL  slö)  V.  S. <za\}  ii  vUpe  auri'onla  zaziat»ha  paiti.-  23;  24t*; —  avavat  sJtdil  una  *Uaili jasitn  y  kavi'if  vlstäspahe  ".  .  auf  dass  y  visp^m  tnial  {aimV  usii)  yai  juyJ  ai^/ius all  (meine)  Helden  siegreich  heimkehren  (nämL  Haiti)  H.2.  z;  —  pairi  dim  tanma w-ie  (die)  des  KV.'^  Yt.  5.  131;  —  yai^a  .  .  un'äii^m  .  .  avavattya  -  .  y  Im  sJ (Sp.  1245  m.)  tanüm  raoüiyäti  y  jiiavhd  Y.  if).  7;  lit,  F.  ^a;  —  yeti/te  arava^  . . ". .  (ipsiusj  corpus  . .  velut  (corpus)  lunae"  tltA  äpi)  aiaJ>ar»nie  y  vuph  imä  äpS Yt/0.i42;  —  s.  noch  Anhang.  a)  mit  (näml.  Atnli)  VL5.15;  —  ya£  miavavat 'i-ä:  j'ui'a  fSp.  12460.)  Ua  väiim  riäsima  datvayasnanqm  nijai^m  y  *säivma  *i-ani-
24108:•  j.  vi8£öi§ta-  Adj.  'der  am  besten  zu entscheiden  weiss':  rasmiS  vasatsta  ..  'ta . .  parakavistima  Yt  12.  7.
=== kav ===
8101:kavüEiit  ifaniiö  Yt.  /<).  9,  1
9578:kava  haosrava  *t?m  's>tn  upa  tarn  cantam  *  ,  „  .     ,  ,       ,      ,
10716:kavä  vistäsps  magaAyä(^.)  'hrä  nasal., astlm  Y.5J.  16;  —  tu  v7  masdil  .  .'dSisä möi  isteis  (%A.)  -'hnm  Y.j/.a;  benutzt Vyt.  46.  b)  mit  InE:  ial  vi  xsair^m kii  Jltis  (sd.)  syadäaiiifi  mazda  Y.  34. j.  2)  'Henschgebiet"';  i)  II  im  Ap.-, mäm  ^ur^mazdi  päluv  utamaiy  °~ii''am via  tyt^  maiui  tartam  X.J.  4;  2.3,  4. 3.  2)   im  jAw.:  ya>a  .  .  masa  °>ra
22558:kavahe  (urunO)  vanaiti  N.  84;  —  sraeiim  j
```


## [2026-09-06T20:36:23.558Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9120,9132p' BRT.txt; echo \"=== usadan ===\"; grep -n \"usa8an\\|usaSan\\|usadan\\|usaöan\" BRT.txt | head -10"
}
```


### [2026-09-06T20:36:23.628Z] TOOL RESULT

```
EL?  —  •)  Um  ausiudriicken,  dass  'du'  nicht von  einer  bestimmten  anwesenden,  sondern von  einer  beliebigen,  gedachten  Person  zu gelten  habe.  Vgl.  Htiil.  KU  i.  17  (falsch neuerdings  GltPli.  /  b.  I21)  lind  Ali.  lU  Bh. 4.  14  (mamm  alla  .wn<  "quiüliet  In  rei");  s. auch  Ker.-j  bei  Cld.  Pron.  47.
•  g.  'kä  Adv.  'wie?',  an  der  Spitze  des Satzes:  i:,l  mS  urv3  voha  *urväxsal ^ag»maUä  (sd.)  V.  44. 8.  a)  einfach fni geeinleitend  'iium?:  kä  tei ..  xsa'i^raAyit t/ti/isd.)  iä  töi  asois  ..  niaibyS ..kä  'iwsi ..  nka  (sd.)  ..  Uva  Y.4^.8.
ISn.  aus  la-.  —  got  h..\  —  Pü.  (zu  Y.  44). ä^-ffn,  SQ.:  kmham,  (lu  V.  4S):  kalär,  Sü. : kadä,
•  j.,  g.,  p.  ka-  (fem,  kä-),  'kay-  (auch fem.)  Pron.  interrog.  'welcher?,  wer?'; I)  als  eigentliches  Fragewort,  an  der Spitze  desSatzes;  1 )  substantivisch :  fc  mqm
yasaife  kd^  .  .  kahmai  raisca  Kfarmasca kakinäi ..  dn'atuhm  ..  baxsäni . .  kahmäi'' ., Vt  /0.108-110;  —  kS  nS  stai-ai  kö*  .  . kake  nd  i'ia  nijma  äyatryHl  kahmai  nS  tat dä'ir?m  dayiit  yat  .  .  Vt.y.50;  5.8^  Ä 15',  /J.47J;  — ■  60  "iviam  . .  inaoili  ks .  . tbaesayeiti  V./A'.öi;  Y.p.8  PuZ.,  V.:j.42i —  kas)  ^ji-aiji  paoiryü  . .  masys . .  Aunüla y-9-ii  V.J.  12,  20.1;  —  kahmai  mä ■  "iwarSldUm  ks  ma  talat  'H.2').\\  —  k7  .  . raocasca  dst  timäscä  Y.44.5;  5",  3,  4', ,  7',  4^-14,  5/.  1 1';  —  kasif  vohü  maiianhä ^y}  i  däy.il  (sd.)  \.-2i/.t,  —  koi  *dr^g7-i>.' dibü  . .  rämam  dih/ii:  "v/er  sind  sie,  die.." Y,  4iS'.  II;  —  kirn  nii  mavaiis  (sd.)  päyürn dadat\.4/i.T,  —  *kaAe^'>  *nä  *gara  ratu- friS  N.54:  —  kirn  höi  ustä  (sd)  ahurim Y.29.2;  —  tclm  {\Sm.)  /rrmraelt  asa- \vatum  ..  \.ig.io;  20.2;  —  kat  va/iY.
dby  Google
443
'kavay-
kaTucS  vlltaspö  Y.^j.a;  —  iava  vistiispö Ytj.  io8  usw.5>;  —  kavaitn  kaviltim  Yt IQ-Ti  usw.»;  —  iavöii  aipivai^A)us  \t. Ij.i3^  nsv/ß;  —  kai'aSm  usaöaium  Vt. 1(^-71  usw.**;  —  kti7-a  usa  VLJ.4S  usw.; —  iavdis  arsnö  Vt.  13.132  usw.** ;  —  iarms fisinaulß  Vt  JJ.  13z  usw.";  —  kavöis byarsiinS  Vt;_j.  132  usw. 5';  —  iavaim syävarsämm  Vt. /fj.?!  usw.*';  —  kavoU haosravaijhahe  Ny.  5.  5  usw. 5';  —  yat baun  Vispe  *d,iri'i.Aaire  kai'c  (NF.)  Vi.  /(?. 71*'.  2)  jAw,  Name  für  gewisse  Feinde des  Volks  und  Glaubens  der  Masdayasn^T: vTspamitn  tbihatqm  tbuuiii  diUvunam  mai- yänamra  y'f'ircum  pairikannmi'a  sä^rmii iaoyiim  {Gl'.)    'iara/nami'a 'Y.  (/■  tS;    Vt.
*)  Ijteriitiir  unter  ki/;--  und  iataj;<ii-.  Y.  4S. 10  siebt  neben  ka>\ipam<  »tati  k,r,-:  i!i:sj.\ui%>i^ dijHymiqvi.  S.  noch  i/i/f^Tniil-  mit  No.  2.  IHe  I eigentliche  Bedcutunj;  des  Worts  hat  sich  spater verdunkelt.  In  den  Fällen  unter  A  inuss  das Wort  schon  zu  /..„„^uUiOi  Zeit  mit  den  EN. verwichsen  gewesen  sein.  Vgl.  die  Vermutung JusTls  l'rj.  i\S.  246.  —  "1  Stammbaum  bei JusT<  NB.  39S.
KompA.;  AUntl.  {s.  k.i.-ya-,  ij:-r\  —  Vgl. tiavay-  EN.  —  ai.  Air-.if-  m.  (IIB.  S.  227).  — P6.!  (kdk,  voM.)  tiiyii-,  s.  iinttt  <.ic-f/.iK- mit No.  —  ">  iKI.  s.  C1.0.  KZ.  fj.  300  und  No.  2, 3,  S-  -  ^)  S  i'"''-  3  ai  vgl.  No.  5.  --  3)  IF. /.  191,  193  No. ;  S  ^<>S.  I  b,  MeILLeT  bei Bgm.  Grdr.'  /.  1091.  —  t)  Doch  s.  auch  Komp. \Ln:i').  —  i>  Stven.  nnter  dem  EN.  —  <•)  -f statt  -va,  S  3Ö1V.  31,  Abi;esehcn  von  11  ftjr -0,  formell  gleieli  /'Jrvyi/j-Äi.
•  j,  'kavay-  m,  EN.  eines  Gläubigen: 'j'eis  asaom  Vt.7j.119;  — garslahe  "vöU asaonS  "des  G.,  Sohns  des  A'.  . ."  Vt.  /  J. 123;  —  pouruslöis  'vöis  asaonö  "des  F., , Sohns  des  K.  .  ."  Vt.  y.  114.
Vgl.  ^km-ay-.  —  ai.  km'oy-  m.  EN.
=== usadan ===
8509:•  j.  usaSan-  m.  EN.  zweier  Gläubiger; i)  eines  iranischen  Fürsten,  der  auch  usan- (sd.)  heisst:  kavOis  'oana  Yl/j.  133;  — yimca  kavalm  °oarum  Yti^.ji.  2)  'häng ma^ayasnahe  a^aone  Ytij.121.
```


## [2026-09-06T20:36:24.635Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ===\"; grep -n \"^kay\\|kay \\[\\|kayān\\|kay(\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n \"kay\\b\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T20:36:24.714Z] TOOL RESULT

```
=== PHD ===
PHD.txt:426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
PHD_mackenzie.txt:3266:lkay [A YMT < A )ymt I N -] when?
PHD_mackenzie.txt:3267:2kay [kd I N -] title of the dynasty of Wistasp (patron of Zoroaster),
PHD_mackenzie.txt:3270:kayk [kdyk' I N -] flea.
PHD_mackenzie.txt:9755:kayk                                   \y~       zard
=== NYB ===
1149:citan [cytn'] cin-, to gather: 1. to put inlay- ers HajB : 12 (pt. cit" = pret. pass. 3d p. sg.). 10 (cit HWH. = hé cond.). - 2. apar ~ to pluck off, to remove (NP bar-cidan) 12019-20 (3d p. pl. eynnd = cinend). — MPrth pt. cyd, pres. cyn- ‘to collect, to fish ; to choose’ (S, A-H III); MPrs cyydn cyn- ‘to gather, to put in layers’ (A-H II); Paz. NP cidan cin-. Av. (441) kay- ‘to choose, to select’; cf Skr cinoti 1. to put together, in layers’, 2. ‘to discern, to search’. — V. also citak and vicitan.
1727:gukài [gwk?y] witness, testifier: ~ bütan apar to bear witness to 457. — Also gwk's gukah attested. Olr "vikaya- *observer’ and *'observation' < vi + *kāya- from Skr cdyati ‘to observe, to become aware of’; Arm. lw. (Prth) vkay; MPrth wyg’h, abstr. wyg’hyft; MPrs gwg’y, abstr. gug’yy; Ps. abstr. gwk’dyhy gukāyēh(ē); Paz. guvāh, guvāī, NP guvāh guvāhī or guvā'i (Paz. NP < *guydi); Av. (1436) vikaya- FrO VIII, a spotlessly authentic Av. w., as shown by vi and by the shortening of -āya- to -ay(y)a- regular in Av. The alternation -di : -Gh (spelt ^s in BP) as usual in Milr, cf s. v. cašm-kāt, whose last element is etymologically identical with -kāt in gukäi. Earlier discussions: Schaeder, UJ XV, 1936, 567 sq.; Benveniste, JA 228,
1731:1936, 225sq. (because of Av. vikaya-, Sogd we’w ‘witness’ cannot be compared). Henning, Weller Vol. p. 297, combines Av. vikaya- with Sogd. wcw, deriving the Av. form from *vikäuya- with assi- milation of -uy- to -yy- and then short- tening of -à- > -d-. However, -uy- is not assimilated in Av.: zaoya-, haoya-, hvay- haoya-, kaoya-, gaoya-, adaoya-, mainyao- ya- (v. m&nó3), kqsaoya-, snāuya-. gukün- [gwk’n-] pres. to destroy 90?6 (Paz. substitutes vdnom, v. vànitan). — Av. (438) vi-?kan- = OP; MPrth w(y)g’- ny$n, Ghilain 71; MPrs pres gwg?n-, v. n. gwg’nysn, Verbum 189. V.s. v. kandan. gukayitan [gwk'dtn'] to bear witness, pt. = pret. pass. 3d p. sg. tgukāyīt ['gwk?dt'] 50%, — Cf Arm. lw. vkay-em.
2157:kad 1. ['YMT] interrog. when? 75, — 2. Prth ['MT] relative adv. and conj. when HajA:5. — 1. MPrs kyy = kay < kad; NP kai. — 2. MPrth kd. — Av. (434) kada, kača. The habit which some Iranists have taken of rendering SW (BP and inscriptions) "MT with kad is wholly re- jectable, v. s. v. ka.
2161:kai [kd] king, sovereign, the title of the ancient kings of Eastern Iran: —-Kavät, the founder of the. dynasty; ~-X6sr61, ~-Luhrasp, ~-Vistasp, cf Käyös; pl.cas. obl. kayān [kd’n'] 2727, zuarrah i —-ān, ~-dn xLarrah, v. xuarrah; Artaxser is addressed as ~ before becoming king 618; — the seven assistants of Saosyant who perform the eschatological actions are called ~ 64; also Krišāsp 997°; cf also s. v. Xosrči. — Av. (442 sg.) kavi-; MPrth kw, pl. cas. obl. q’w’n ‘giant’; Prs on coins kd, kdy = FrP 12, with the explanation mas ‘great’; Paz. ka; NP kai ‘great king’ and borrowed from the NW language kav ‘valiant, grand, of fine figure’.
4131:vieitan vicin-, to separate = to pull off 294; to distinguish 63; *dö-cin [dwen ?] nē vicinend they do not even distinguish between the two 103°[? cf Av. (595) cina- and (762) dva-; cf PY 30%%?]; to choose 698. 11215 (hac from). — Av. (441) vi-kay-; MPrth wjyd (pt.), wjydg, weydg ‘chosen’ ; MPrs weydn wzy- (! A-H II); Paz. vajidan vajin- or vazidan vazin; NP guzidan guzin- Arm. lw. včit ‘clear, limpid’. Verbum 181-182; Ghilain 85.
4345:of the priests: ~ i xatdyéh 7%. (81); ~ i kayän u äturän šah 12%; kayān ~ u han 4 herpat — 554; yazdan ~ i Erän šahr 52-61; in a more general sense 427. 11918; in names of towns 1165-22, — 5. fate 1311. — Av. (1870 sq.) x%aronah-, in Old Median farnah- in proper names: Vinda-farnah-, also in OP: Tioox-pepvng < *tica- (SW form of cidra-) + farnah, ’Apraptpvng etc.; MPrthPrs frh, MPrs also prh, pl. fren; Paz. xareh, xYarahé, zurahe; NP zur(r)ah, farrah. — V. also zat-xa"arrah,
5222:katäma-: katam katära- (katarascit): katarcihé Kavärasman-: Karazm kaväta-: kavät kavi-: kai kavi-: kayak kavi-(usan-): Käyös kay-: citan kohrp-: karp keresaspa-: Krišāsp kū (kuda): kū kutaka-: kötak xrafstra-: xrafstr xratu-: xrat xrvidru-: xurdruš ni-xšata-: šastan xša0ra-: šahr xSa0ra-vairya-: šahrēvar pati-xSay: pätixsäi xšinaka-: šmah xŠnā-: šnāxtan xšnav: Šnāyišn (ava/avi-) xšnav-: ošntitak xšusta-: šustan x$viwra-: "šif(a)rg xUaöna-ayah-: xYan-asén xUačpal0ya-: xVēš xVafna-: xYamn x"üirizam-: xVārizm xUanat.caxra: x"andan
```


## [2026-09-06T20:36:42.821Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==218' HRN.txt"
}
```


## [2026-09-06T20:36:43.804Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Käyös\\|Kayos\\|kayos\" NYB_vol2_glossary.txt | head; echo \"=== HUB sukoh ===\"; grep -n -i \"sukoh\\|šukōh\\|skoh\\|ikoh\" HUB.txt | head -20"
}
```


### [2026-09-06T20:36:44.682Z] TOOL RESULT

```
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


### [2026-09-06T20:36:44.733Z] TOOL RESULT

```
878:bag [bg, bk'; inser. bgy, Prs RHY”, Prth ’LH?] 1. god 381! [bk', a quotation from Y. 1019]; pl. eas. obl. —-an [bg?n!] 75! (opp. dēvān). 1131?; garān —-än kof the mountain of the mountain gods 20? (v. s. v. gar). — 2. lord: Ohurmazd ~O. the Lord, of the supreme god 211’. 2224; — of kings: Käyös ~ 458; ~ Päpak HajA:4. B:4. SPrs:8. Prth:8; ~ Artaz- šahr HajA:3. B:3. SPrs:6. Prth:6; 1091, 111%; ~ Sähpuhr HajA:1. B:1. SPrs:4. 11. Prth:4. 6. 8. P1:1. P2:9; ~ Ohurmazd P1:3; ~ Xēsrēi 10921; pitar ~ P1:10; — pl. cas. obl. —-än [SRHY?-n, bg'n'] as a pl. majestatis: öisän —-ān Šahpuhrv P 2:8, without the king's name Pl:4; šmāh ~-dn addressing the king
975:Religion 1097-8; hac kunišn 4 im bē out of the activity of this man 5212; — c) late, for pat, as NP bi-: bē ravākēh bavet 37? (gl.); 4717 (gl.); 502° (editorial summary). - 4. adversative conj. but: a) after a negative sentence or a negative part of the sentence: andar déh ne, be pat kustak-é € deh vitart 61%; nē ozančt, bé apäc 6 Käyös Sut 4527, ete.; ne ēvāc ... bé not only...
2120:*jānakān [HY°-k’n'!] designed for the soul, "place of the soul of a deceased, a sepulchre: Sugud, 1 haft ~ andar but, api-š haft-jänakäneh ēt kū haft x“ataidan andar but Sogdiana, in which seven *soul-places" existed; and its possession of “seven soul-places" is explained by the fact that seven royal tombs (v.s. v. axvatātdān) existed there 1131-14: those of Yam, of Frētēn, of Manūcihr, of Käyös of Kai-Xösröi, of Luhräsp, and of King Vištasp (ll. 15-17; Az Dahāk is a spurious addition). — The reading ET Y?-k?n-handed down by such a careful and competent scribe as Mihrapan should never have been doubted; Jamasp Asana’s ''emen- dations” haft (hwt’d’n =) xtatdydn, haft (hwt’d’nyh =) xatdydnéh (a horrid form!) are sheer corruptions. Mihrapan must be taken seriously. Certainly the idea of a place for the jan is absolutely contrary to the Iranian way of thinking,
2161:kai [kd] king, sovereign, the title of the ancient kings of Eastern Iran: —-Kavät, the founder of the. dynasty; ~-X6sr61, ~-Luhrasp, ~-Vistasp, cf Käyös; pl.cas. obl. kayān [kd’n'] 2727, zuarrah i —-ān, ~-dn xLarrah, v. xuarrah; Artaxser is addressed as ~ before becoming king 618; — the seven assistants of Saosyant who perform the eschatological actions are called ~ 64; also Krišāsp 997°; cf also s. v. Xosrči. — Av. (442 sg.) kavi-; MPrth kw, pl. cas. obl. q’w’n ‘giant’; Prs on coins kd, kdy = FrP 12, with the explanation mas ‘great’; Paz. ka; NP kai ‘great king’ and borrowed from the NW language kav ‘valiant, grand, of fine figure’.
2275:Käyös [k'dws] n. pr. a king of the Kavi dynasty : ~ bag 455-461; 782, 9012, 1137-16, ~ Av. (406) kavi- usan-, nom. kava usa; Paz. Kahés.
2276:Käyösän patron. of Käyös 1138.
3957:to man by the gods 90%; varc-é given by the gods to the bull of Käyös 45°; men- tioned together with z"arrah, amävandeh
4225:viškaftan [wškptn'] to crook, to pervert: menišn à Käyös apar hàn gāv viškaft pre- judiced K. against this bull 4516-17, - NP šikaftan.
5222:katäma-: katam katära- (katarascit): katarcihé Kavärasman-: Karazm kaväta-: kavät kavi-: kai kavi-: kayak kavi-(usan-): Käyös kay-: citan kohrp-: karp keresaspa-: Krišāsp kū (kuda): kū kutaka-: kötak xrafstra-: xrafstr xratu-: xrat xrvidru-: xurdruš ni-xšata-: šastan xša0ra-: šahr xSa0ra-vairya-: šahrēvar pati-xSay: pätixsäi xšinaka-: šmah xŠnā-: šnāxtan xšnav: Šnāyišn (ava/avi-) xšnav-: ošntitak xšusta-: šustan x$viwra-: "šif(a)rg xUaöna-ayah-: xYan-asén xUačpal0ya-: xVēš xVafna-: xYamn x"üirizam-: xVārizm xUanat.caxra: x"andan
6676:Kahčs: Käyös
=== HUB sukoh ===
```


## [2026-09-06T20:37:00.854Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB ===\"; grep -n \"kōh\\|koh 'Pracht\\|Pracht\" HUB.txt | head -20; echo \"=== HUB skauaθa ===\"; grep -n \"skaua\\|shauadha\\|iskau\" HUB.txt POK_02.txt | head"
}
```


### [2026-09-06T20:37:00.915Z] TOOL RESULT

```
=== HUB ===
=== HUB skauaθa ===
```


## [2026-09-06T20:37:01.938Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v3 near 1749 ===\"; grep -n \"pdf page\" incoming/BQT/BQT_v3_pages.txt | head -3; grep -c . incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T20:37:02.005Z] TOOL RESULT

```
=== BQT v3 near 1749 ===
1:[pdf page 1]
3:[pdf page 2]
24:[pdf page 3]
37437
```


## [2026-09-06T20:37:06.364Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -c HUB.txt POK_full.txt IEC.txt SYN.txt KLN_1966.txt SKT.txt; echo \"=== hub sample ===\"; head -c 600 HUB.txt"
}
```


### [2026-09-06T20:37:06.412Z] TOOL RESULT

```
  527491 HUB.txt
 3971883 POK_full.txt
 3311889 IEC.txt
 4502081 SYN.txt
10837854 KLN_1966.txt
 2656202 SKT.txt
25807400 total
=== hub sample ===
Google
This is a digital copy of a book that was preserved for generations on Hbrary shelves before it was carefully scanned by Google as part of a project
to make the world's books discoverable online.
It has survived long enough for the copyright to expire and the book to enter the public domain. A public domain book is one that was never subject
to copyright or whose legal copyright term has expired. Whether a book is in the public domain may vary country to country. Public domain books
are our gateways to the past, representing a wealth of history, culture and knowledge that's often diffic
```


## [2026-09-06T20:37:07.251Z] TOOL CALL #24: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nprint(d.get('page_offset'));print(d.get('lookup_hint'))\nprint(json.dumps(d.get('scans'),ensure_ascii=False)[:1500])\""
}
```


### [2026-09-06T20:37:10.262Z] TOOL RESULT

```
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
[{"volume": "3", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "first_printed": 1208, "last_printed": 1925, "pdf_offset": -1205, "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json", "lang": "fas", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"}, {"volume": "4", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf", "first_printed": 1920, "last_printed": 2475, "pdf_offset": -1917, "lang": "fas", "offset_note": "printed = pdf+1917, checked at pdf 150 and 500", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt"}, {"volume": "5", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf", "first_printed": 1, "last_printed": 290, "pdf_offset": 5, "lang": "fas", "note": "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt", "requires_volume": true}]
```


## [2026-09-06T20:37:15.330Z] TOOL CALL #25: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1749 2>&1 | head -60"
}
```


## [2026-09-06T20:37:16.400Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /pdf page 544\\]/,/pdf page 547\\]/' incoming/BQT/BQT_v3_pages.txt | head -80"
}
```


### [2026-09-06T20:37:23.140Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 544; check the printed number and re-run with --pdf-page if off)
REF: BQT:1749  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 544  OCR-lang: fas

-۱۷4۷- مج
اسلوب .کنایه از اسب وشتن باشد - فر‌هاد را | نام قلمه‌ایست قدرم از قلاع بدخشان وممرب‌آن
پیز کویند که عاشق شیربن بوده * قندزگ است » والحال نیز شندز اشتهار دارد *

گهلم - بنتح اول ولام بروزن‌شلنم « گهن‌دبر» کنایه ازآساست- وکنایه
پیمنی بادنجان است . از دیا وجهان هم هست -
گهله - بنتح اول بروزن بهله » ریزها کهنزه * بح آول وئثانی و زای هحوژ
و کاورسهای زر وسیم را گوبند. و زر سفید ‎)٩(‏ سکون ثالك خماه است ,۰۳۲
را نیز گفته‌اند وبتر کی آقچه خوانند .* وسخود مطتی کمیازه است و01 2
۰ ام : شدن دست وپا باشد بسیب غلیةٌ خواب یا خملر
کهنباد. بنتح اول و بای ایجد ردنت | پاآمدن تب وبمریی تمطی کویند ۴ .
قلم‌کار» مخفف کاه آنبار است که آنبار کاه باشد - 8 ۰
وجم‌اول بمعنی خانه‌است که بعریی بیت‌خوانند- که فرش - بنتح فا ؛کنایه اززمن
و بارگاه را نیز کونند- و زردشت گفته اس ت که است که بعربی ارض کوبند *
رو ز کار کهن بارهاکرده است وبهرباری کونه ای گهنی - بکی اول وسکون ثانی‌ونون
آفریده است چون آسمان و زمین وکیاه و | بتحتان ی کشیده (۲) . خانةً ازمتانی باشد 6 اب
جانودان؛ وجهانرا بامردم بالیآفریده وهر يك | وخری رالیز کوبند و آن جانوری‌استمعروف۹ *
ازی نکهن بارها پنج‌روز است ونامغان‌هم کهن‌بار کهی > بکراول وئانی‌بتختانی‌مجپول
است باضافة اول ودوم همچ وکهن باراول و کپن ۹ :
۰ رصیده »۰ نام قلمه!است از ولابت سستان۷ ۰
بار دویم وکپن‌بار سیم وفارسیان بهر کهن باری : 7 0
جشنی سازند وعید کنند چنانکه درکاهنبار,تفصیل کهیانا « بر وزن احیالنا ». دوائی
هذ کور شد ‎٩‏ . است که آنرا بعربی‌عودالصلی بکویند" برحصروع
گهی‌خر ابات ه کنایه از دنیای آويزند نافم باشد -
فانی‌است . کهیج - بفتح ارلوتانی بتحتانیمجهول
گهن در ی « بازای‌هوز بر وزن‌مهندس,» | کشیده وبجیم فارسی زده » بمعنی کهی اس ت که

(۱) چش : سفیدی. (۷) خم ۱ : کشیدنی ۰

سا

۱ - صحیح «کیهنبار» است مخفف«*گاهنبار» . رك :گاه بارها » کاهنبار -

۴ - اسم عام است بمعنی قامةٌ قدیم (معرب آن قعندز و مخفف آن فندز) و علم برای
چند قَلعةٌ قدیم است. ۴ - رك : قندز . ۴ - «کهنزه . کمانکش که قبل از تب آدمی
را واقع شود بعربی تمطی کویند » وکسی راکه این حالت واقع شودکونند : میکهنزد .>
«رشیدی» . 8 - رغیدی » جهانگیری . ‎٩‏ - جهانگیری . ۷ - مخقف
«کهیج» (.م.) ۸ - در فهرست مخزن‌لادویه آمده: «کیهانا بسربانی عودالصلیب‌است.» ۱

کهن - جم اول و دوم ( در قدیم ) وانیز بفتح دوم < کهنه . پهلوی 8808
«تاوادیا ۲:۱۹۴* » در اوراق مانوی (پپلوی) ‎٩۳۷۷8‏ ( کهنه) » بپارتی ۲۷۷۲۵

(.8505,12,1,0.84 و..83678128 31140416 0۶ 1151 ۸ ,ع۲1060210])؛ کردی

51 کهونه ۰ پیر)» ۴83082 ,6۷10 .زازا 628028« ژابا ص ۳۳۸ ؛ قدریم. قدریمی«پیره

هسن -. فرسوده .

تگهته - بنم اول وفتح سوم (در قدیم) ولیز ابکسر سوم * کین (ه.م.) ۰
```


### [2026-09-06T20:37:24.756Z] TOOL RESULT

```
[pdf page 544]
۱۷۷
‎Syl‏ کنابه از اسب وشتر ‎ash‏ - فرهاد را
‎ps‏ گونن که عاشق شیرین بود» ۰

کهلم ‎ch‏ اول ولام بروزن‌شلفم +
پمعنی بادنجان است =

‎AG”‏ - بنتم اول بروزن بهله ۰ ریزها
وکاورسهای زر وسیم را گویشد- و زر سفید (۱)
را نیز کفته‌اند ویترکی آقجه خوانند ‎He‏

‏کهنیاد. بفتح اول و بای ابجد بروزن
قلم‌کار. مخفف ‎Ll OW‏ است که انبار کام باشد -
ویضم‌اول بمعنی خانه‌است که بعربی بیت‌خوانند
و بارگاه را نیز گویند و زردشت گفته است که
رو زکار کهن بارها کرده است وبهرباری گونه ای
آفریده است چون آسان و زمن وکیاء ۳
جالوران؛ ‎Valery‏ بامردم بسالیآفریده وهر يك
ازین کهن بارها پن‌روز است ونامشان‌هم کهن‌بار
است ‎Jol GEL‏ ودوم همچوکهن باراولو کین
بار دویم و کپن‌بار سیم وفارسیان بهرکهن باری
جشنی سازند وعید کنند چنانکه درکاهنبار,تفصیل
‎ae‏ کور شد ۷ .
کهن خرابات - کنابه از دای
قانی‌است .
کهی ذذ © - بازای‌هوزبروزن‌مبتس,

‏نام قلمه‌است قدیم از فلاع بدخثان وممرب‌آن
قندز؟ است » والحال نیز بقندز اشتهار دارد *

‎Pot‏ کنابه ازآسماست_ وکنابه
از دنیا وجهان هم هت ۰

‏کهنزه = بفتح ‎IN‏ وانی و زای هوز
وسکون ثالث » بمعنی خمیازه است ‎AAT OM‏
شدن دست و پا باشد بسبب ‎Ue‏ خواب یا خمار
باآمدن تب وبعربی تمعلی گویند ۴ .

‏کهن فرش - بنتح ا ‎BAT‏
‏است که بعربی ار کوبند *

‎GF‏ - بکس اول وسکون انی‌ویون
بتحتانی کنیده (۷) ‎bE.‏ زمتانی باشد 6 -
وخری رائیز گویند وآن جانوری‌است‌معروف؟ *

‏گهی = بکراول وانیبتستالی‌مجهول
رسیده ؛ نام قلمه‌است از ولابت سیستان۷ .

‏کهیانا 4- بر وزن احیانا .. دوائی
است که ‎LAT‏ بعربی‌عودالصلی بگوند* برحصررع
آوبزند نافع باشد -

‎BT‏ - بنتح اولونانی بتحتابیمجهول
کشیده وبجیم فارسی زده ؛ بمعنی کهی است که

‏(۱) چش : سفیدی. )1( خم ۱ : کشیدنی .

‏۱ - صحیح ‎OLS‏ است مخفف« گاهنبار» » رك :گاه بارها . کاهنبار .
۴ - اسم عام است بمعنی ‎LG‏ قدیم (ممرب ‎OT‏ فهندز و مخنف ‎OT‏ قندز) و علم برای

‏چند ‎b‏ قدیم است. ۴ رك : فندز .

‏۴ «کهنزه , کمانکش که قبل از تب آدمی

‏را واقع شود بعربی تمطی کویند , وکسی راکه اين حالت واقع شود گوند : می‌کهنزد . »

‎. Gat?

‏«کهیج» )» 0

‏۵ - رشدی » جهانگیری ۰
۸ - در فپرست مخزن‌الادوبه آمده: « کیهانا بربانی عودالسلیب‌است.؟ |

‎ine ۷

‏3 - جهانگیری .

‏* کهن - یم اول و دوم ( در قدیم ) و نیز بفتح دوم = کهنه » پهلوی ‎kahun‏
‏«تاوادبا ‎٩۲:۱۷‏ ۰ در اوراق مائوی (پپلوی) ‎٩۷۵‏ (کهنه) » بپارتی ]16
```


## [2026-09-06T20:37:32.237Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /\\[pdf page 54[6789]\\]/' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T20:37:34.287Z] TOOL RESULT

```
[pdf page 546]
uw -۱۷-

پادشاهان بزرکتر باشد و بعربی ملك الملوك | وترجمةٌسلطان هم هست ‎٩‏ - وبعضی کوینداین
خوانند ۱ - و پادشاه فهار و جبار ‎ath‏ مرتبه دا | تلم را زال پدر رستم بقباد گذاشت وکیقباد
لي زکویند ۱ , واين تام را در بلندی وقدر از | ‎Vals‏ - و در عربی بتشدید ثانی . بمعنی‌داغ
‎whe Sol”‏ ؟ چد اوبلندترین کواکبسباره | باشد که بردست ‎by‏ واعنای دیگر نهند - ولکه
است » وبعضی کوبند معنی لفوی کی پادشاه قباد ] ونان را هم کنته‌اید ۷.
است ودر قدیم اين چپار پادشاء را که کیکاوی کیا «پکر اول و ثانی بالف کشیده .
وکیضرو وکیقباد وکی لهراسب باشد «کی» .

بمعتی کی است که یادشاء بز رکف جبارباشد -
میگفته‌اند ۴ وسنی پنج میگوبند و کیومرترا | * ی
داخل میدانند ۴ - وهريك از عناصر ‎aw)‏ را و مرزبالرا یز کوبند که زمین دار باشد یعنی
نیز کمته‌اند ۵ - وبسمنی پا کیزه واطیف‌هم آمده | پادشاء كوچك - وپپلواندا ‎we‏ سویمعئی
است ۷ - واصیل وتجیب را نیز میگویند صاحب وخداوند نیز آمده است . ‎٩‏ - ویمعنی

۱ - در اوستا 12۷1 ‎ot‏ شده . از کانها بر میآید که «کری » بمعنی پادشاه و امیر
و فرمانده است ۰ با اين کلمه درکانها در مورد شهرباران و امیران ‎Lage‏ ( مخالف ‎eT‏
‏زرتشت ) یز بکار رفته » و عم لین عنوان بشپربار مماصر و حامی زرتشت » یمتی کشتاسب
داده شده - در دیگر قمتهای اوستاکاهی بیفتن ‎peal‏ ستمکار و کمراء کننده استعمال شده و گاه
یز عنوان یکی از پادشاهان کیانی است . در ودای هندوان این‌کمه در مورد ستابشگران دبوان
(خدابان هند) بکار رفته است . (وئیز « کوی» در اوستا نام طایفه ایست ازپیشوایان کیش آریابی
که آیبین آنان غیر آمن زرتشی ‎oy‏ وزرنشت از ابشان ‎AF‏ میکند ) بنا بر آلج هگفته شد. کوی
‎LU‏ عنوان ولقبی بوده وبعد بعنوان اطلاق عام بخاص ؛ بيك ‎TL‏ مخصوص -کمدرداستانه ای
ایرانی یس از ‎DL‏ پیشدادی ذکر میهود - اطلاق گردیده . از برخی موارد اوستا مستفادمشود
که این عنوان از همان ‎ape‏ باستانی بخاندان مخصوص اکیانی ) تخصیص افته . چه در بند ۷۱
زامیادبشت از : کیقباد .کی ‎opal‏ . کی‌کاوس؛ کی آرش » کی‌پشین » کی‌وبارش » کی سیاوش باد شده
ودر بند بعد آمده که کیالیان همه چالاك و پهلوان و پرهیزکار وبزر که منش وبی‌بالاند ۰ رل" :
پورداود ۰ یشتها ‎te‏ ص۲۱۷- ۲۲۲؛ شاهان کیالی وهخامنشی در آثار الباقیه بقلم ‎Mane ott SS‏
آموزش وپرورش ۱۵: ۸ - ۱۰ ص۲۸ ‎see‏ در پهلوی/181 ‎(Kavi)‏ «منای ‎٩۲۷۸‏ قس ‎US:‏
‏۴ - فقه‌اللفةٌ عامیانه . ۴ - ‎Lobe‏ اساطیری « کیانی» را در ادیبات‌پهلوی.
وپازند وپارسی زرتعتی «کی» مرگفتند :کیقباد. کیکاوس » کیضرو , کی‌لهراسب »کی گشتاسپ.
‎ee‏ ۴ جزو اول ‎pl‏ نام «گی» <۳ کیه) است نه «کی» ۰ رلك: کیومرث ۰
- جهالگیری هم یکی از ممانی «کی» را ‎pate‏ نوشته » لیکن در آن معنی«کیان»

است «فرهنگه لظام. ‎OLS: Ay‏ ورك : کیا ۰ ۱ - این بت را شاهدآورده اند :
شدستم بی‌شك ویی‌شبهه بروی پذیرتم مراورا از دلکی.

زرانشت بهرام یژدو مجهالگیری*درشیدی» .

۲ - رگ : محیطالمحیط. اقرپ‌الموارد ومنتهی‌الارب ۰

۸ -قی :کی. مازندرانی ‎Fy hyd JAS,‏ بز رکه ناحیه) که‌مخصوصاً بطبقهای
از سادات زیدی طبرستان اطلاق شود؛ کردی ‎kia‏ (دحضدا) [ ژاباس ۲۵۲ این کلمه را ازفارسی
> کتخدا»میداند] . ‎٩‏ = درتر ‎alls.‏ : ده کیا (دهشدا) .کا رکیا (سرکار ومصدر امور) .
[ رك : کار کیابی ]

[pdf page 547]
کیابلد
وعقال هم هست - و طبایع را نیز کوبند که
پرودت وحرارت ورطوبت وببوست باشد٩‏ سوهر
يك از عناصر اریمه را نیز ۴ - وبمعنی پاکیزه
ولطیف هم کنته‌اند ۴ - وبلت سربانی مسطکی
‎aS,‏ وآنرا بعربی علك رومی خوانندوبسنی
کوبند ‎tlle‏ رومی تومی از مسطکی است ۴ -
ویمعتی دهان هم بنظر آمده است که بعربی قم
گویند .

‎ULF‏ - بادال ‎sen!‏ بروزن‌خرابات,
‎gine‏ جبروت است همچنانکه روان کرد پممنی
ملکوت باشد -

‏کیاچود = ‎pe‏ اول بروزن بلادور ؛
عاقل وفاضل ‎bby,‏ راکویند ‎٩‏ +

‏کیاخره ۲ - بکر اول و شم خای
‎babs‏ وقتح رای ‎abi‏ توربراکویند که‌از
‎Slate‏ بیادشاهان‌فایش(۱) کردد چه کیا ‎eet‏
‏پلدشاه وخره نوری باشد از ‎ile‏ خدای تعالی
فایض(۱) بربند کان‌خود که بسبب آن‌رباست کنشد؛
وباواو معدوله هم آمده است که کیاخورهباشد.

‏پوت

‏" کیاخن - بر وزن فلاخن » بسنی
‎Kaaba pal‏ واستواری ورمی‌وهمواری
کاری کردن ‎Auth‏ - وسخن چرب وشیرین راهم
کفته‌انه ؛ وباکاف فارسی هم آمده است.

‏کیاخوده ‎٩‏ - با واوسسدوله‌بروزن
ومعتی کیاخره است » وآن لوری و پرنوی باشد
ازجاب خدای تعالی بسوی خلق که بسبب آن‌لور
‎sam‏ یادشاه ‎gems‏ رئیس شوند وبسنی صنعت و
‎rod‏ فت آموزه .

‏کیاده © 9 ورن ‎carly‏ بمعنی رسوا
باشد ‎Ne‏

‎AST‏ بکر اول بروزن ‎abe‏ بمعنی
کاهلی باشد ۰۱۱ ‎pang‏ اول هم‌آمده است- ونم
‎ol‏ هم هست *

‏کیارا ‎cee‏ اول ‎sls‏ ورابم هر دو
پالف کشیده . اندوه وملالت وثیر کی روی باشد
پیب کلو فشردن و خفا کردن یا چیزی بیار
خوردن وآنرا بعربی‌طفت کویند - وبمعنی تاسه
حم آمده است وآن ‎Je‏ وخواهش بهم‌رسانیدن

‏(۱) خم۱. چك. چش: فائز . رك حکمت اشراق بقلم ‎ot KG‏ ص۲۸.

‎Com) ‏مصتف «کیان»‎ - ٩
‏چوثخص‌راین لبای تن‌براو‎ ole

‏همچنین هتی ‎lle‏ را ‎cot‏

‏۴ - این ابیات مولوی‌را شاهدآورده‌اند :

‏جنبش ما را ازو دان له ز ما
چون‌لباسی‌دان بروچار این کیا
مولوی «جپانگیری»

‏بمعنی‌عنص « کیان»(ه.م.) است . پس‌در شعرمولوی ‎LS‏ بمعنی پادشاه بزر که(وفرمانروا)
است «فرهنکه نظام» ‎LS ery‏ لغة چهارفرماتروا ومجازاً امطلاح شده برای عناصی اربعه. قس:
چهار ‎fy‏ (عناصر ‎(and‏ . ۴ - رك :کی . ۴ - رشیدی بنفل از ‎Sob;‏
‏همين معتی را آورده . 8 - ‎Sol,‏ دساتیر"*فرهنگه دساتیر ‎AN‏
‎٩‏ -جپانگری ورشیدی‌لیز بهمین معتی‌آورده اد بدون شاهد. ‏ ۷ - رك :کیان خره .
‎A‏ «کیاخن . ‎Sal‏ ولرمی باشد . رود کی (سمرقندی) کفت :
درنگه ‎oT‏ ای سپپر چرخ ‎Us‏ کیاخن ترت باید کرد کارا . »
‎SENT cal?‏
‎٩‏ را .کیان خره . 0- «کیار,کاهلی بود.رودکی
(سمرقندی) کوبد :
مرد مزدور اندرآ غازیدکار

‏یز رك : رسوا .

‏پیش او دستان همی‌زد بی ‎AS‏
‎cal?‏ فرس ‎٩۱۲۷‏ .

[pdf page 548]
۱۷۵۱

بخوردنی ‎ath‏ واین حال بیشتر زان آبستن را
چم رت ۱ ۰

کیادش- بفتع اول و دابع بر وزت
جفاکشی .نام یکی از چهار پسر کیتباد
است؟ ۰

کیا دهین © ‎eek‏ پروزن فروردین»
ام یکی ازچهار پس رکیقیاد است (۱) ۰

‎LST‏ » با کاف فارسی در آخر
پروزن‌دماوند. رنگه‌پا کیژه ولطیف رااگویند؟ -
ویسعنی سفید جم آمده است ۰

‎HILT‏ - بکاول ‎py‏ زای‌شلمدار
وسکون نون ودال ‎vine latin‏ پادشاء‌بز رکه
وعظیم باشد چه کیا پادشاه و زند بز رکه ‎fan)‏
‏را گویند .

‏(۱) چش : -کی‌ارمین ... کیقباد است ۰

‎ws
‎. ‏اول بر وزن چراغ‎ Ge rel”

‏بمعت یگیاءه است که علف باشد ۰

‎LF‏ - بائاف درم ظرسی بر وزت
مساکن» بمعتی مخالف باشدودرشت وتاهموار
را یز گوبند 6 *

‏کیان - ‎ca‏ اول جم عکی باشد بستی
پادشاهان ‎she‏ بز رکه ۷ - وپادشاهان ‎SAMS‏
‏کفته‌الد که کیقباد و کیضرو وکیکاری و کی
لهرامب باشد ۲ - و یشم اول ‎tse‏ کردیوا
کون دکه بيكستون بریای‌باشد و آتراکنبدی حم
میگوبند , و بس یکوند ‎bas‏ کردان ( ۷)
وعربان صحرا شین باشد ۸ » ویک راول.هم‌باین
ممنی‌آمده است - وهم ستاره وک وکب - ‎Bag‏
‏پرکار ‎Sp SS,‏ دایره امت ‎٩‏ ۰

‎Lb ‏بروزن زبالا » بسستی‎ -۷" ULE

‎. OS: ‏چش‎ )۷(

‏۱ رگ تعلیقات ( ‎UT. )۵ ale‏ تاسه ‎aS zs‏ . » «جپانگیری» بمعتی اخبر

‏اکنون ۷۷8۲ مستممل است .
کی وشهربار دلیر) .
شتن چر کاوی با آفرین
چپارم کی ارمین کجا ‎thon‏

‏۴ - از :کی آرش + در اوستا ‎arshan‏ 58۷ (بسعتی

‏کی آرش دوم بد. سوم کی‌پشین
سپردند کیتی بآرام و کلم

‎So ‏«فردوسی‎

‏اين نام در اوستا ‎cals‏ وبجای ‎Kavi Byarshan oT‏ ذ کر شده است « پورداود .

‏بشتهاج ۲ ص ۲۲۲۵ . رك : مزدیسنا ص ۸۰۷ .

‎+ ‏رك : رشیدی‎ - ۵ is

‏۴ رك: کیاءکی. ‎:4,-f‏

‏- رك :کی ختح اول .

‎A‏ «کیان . خيمةً کرد وعرب بود . بوشکور(بلضی) کوبد:
همه باز بته بدین رسمان ‎LET)‏ . دهضدا) ‏ که بر پرده (برده . دهشدا) بینی بان‌کیان»

‎{ ۳  یلابرس ‏اول و قتح دوم ) از‎ SG) ‏بیز «کیان»‎ - ٩

‎۳04 ‏فری‎ cal?
6 ‏طبیمت‎ )

‎mettre ‏«دزی‎ Physica auscultatio= ‏الکیان‎ (UL: 9) wT age
‏مقدحه ومخصوصاً‎ ۱۳۱٩ ‏محمد علی فروغی تهران‎ Lied ‏سماع طبیعی. رك : فنون سماع‌طبیعی.‎

‏ص ۲۶ ح ۱ .

‎(Henning, Sogdian Loan_ (cat) kyand ‏از سربانی‎ -*

‎: ‏کیانا , طبایع باشد بزبان فلاسفه . خسیوی کفت‎ «۲۷۵۲5... BSOS,X, I, p.93)

‏همه آزادکی همت تو

‏قهر کرده است م رکیانارا .> «لفت فری‌مسححاقبالس۱۷*.

‎* ‏خوانند ۰ «للت فرس طبع هون ص ه‎ OLS? US ob LS . ‏طبایع باشد‎ LS?
Ag ‏وهمان یت خسروی را شاهد آررده (منتهی در مصراع اول : همه آزادگیست عمت‎

[pdf page 549]
کیان خره
باشد که حرارت وبرودت ورطوبت ‎mel pty‏
وعناصراربمه را یز کوبند - واصل وبنای‌هرچیز
‎wld‏ - و مرزبالرا هم میکوند که زمين
دار ‎oa ath‏
گیان‌خره ۴ بن خای شطه دار
وقتح رای بی‌قطه بممنی کیاخرء است و آن‌نوری

باشد از جااب ‎a‏ بسوی یادشاهان. چه کیان

پادشاهان وخره لوری و پرتوی را کویند که از
جالب‌خدای‌تعالی به‌بند کان فایض(۱)شود که‌بدان
سبب بعضی پادشاهی ورباست کنند وبسنی‌ستمت
وحرفت آموزند +

کیان‌خوده ۳ - با واو مسوله,
‎ae‏ کیان خره است که نوری باشد از جالب
اه فاییض(۱) بیادشاهان ورژسا -

کیپا ۴ = بفتح ‎Shy Jol‏ فارسی بروزن
شیدا » بلفت زند وپازند نقره را کگوند و بعریی

فنه خوانند .

کی بشین* ‎bo‏ بای فارسی و شن

۱۷۵۲

قطه دار بروزن درگزین » نام .یکی ازچهارپس
کیقباد است ؛ وبجای بای فارسی نون مکسورهم
پنظ آمده است +

کیبو - بکسراول وم بای ابجدیروزن
تیهوه مرغی‌است بزر کهآ نرا دبنارهم‌میگوبند؛
وبسنی گوبند مرغکی است کوچك و رنگهای
مختلف دارد و آشبانی سازد که کوبی از رسمان
پامته‌اند واز درخت آویزان کند ۷ .

‎Osten”‏ () - بابای ابجد بر وزن
پیچیدن , بیکو رفتن وتحاشی لمودن واز جای
کنتن و از ‎gle ale‏ کشیدن و کردایدن
‎ask‏ .۰

‎ST‏ با ‎st‏ قرشت بروزن تبهو ۰ نام
‎colt»‏ دهبیشتراوقات ‎ogy Ke‏ خورد -

‎ty ‏مجهول‎ gts ‏فیالا * - با‎ SS
‏حطی رسیده و لام بالف‎ GL ‏مثلثه بواو و فا‎
" ‏ومعنی‌آن بقارسی از‎ lity, ‏کشیده , لفتی است‎
cole ‏و آن صمفی است‎ cath ‏سنگه ساخته‎

‎athe oe )۱(‏ چش: فابز. رك: حکمت اشراق بقلم نگارنده ص۲۸ .

‏(۷) چش :کی سدن .

‏۱ - در رشیدی آمده : « ‎ded polis US‏ جمع کیا » و بیت خسروالی (خسروی)
مت کور درحاشه*۱صفحدُقبل را شاهد آورده, محشی فرهنگه رشیدی بوشته ‎WLS?‏ را جمع کیا
کفتن عجیست ودر فرهنگه ( جهانگیری ) جمع کی گفته وترد صاحب ‎Che‏ صحیح « کیانان»

‏بنوست جمع

‏کیان که بمعنی اصل و عنصر است ‎LS? ASV UT yo‏ (بوزن ‎(Uy‏ بمعنی طبایم

‏اریمه گفته‌اند. تخطثه کرده و گفته که درشعر خسروالی «کیانان» بنوست . * این احتجاج صحیح

‏لیست, رجوع بحاشی»۱ ‎Jeb nie‏ شود +

‎gis = ۴‏ » در اوستا 26۷8۳906 ‎Kavaénem‏ . رك : خوره » خره » فر .

‏۳ رد : کیان خره .
(سیم » ‎ON Sip? (sit‏
» اوستا ‎Kava Pishina‏ :
‎coats‏ چوکاوی باآفرین
رك : مزدیستا ‎op‏ 1۰۲ ۰

‏۴ هز . ۷۵108 . با ‎k(a)spa‏ ۰ پپلوی ‎asim‏
‎٩‏ کی‌پشین صحیح است که به « کی‌نشین» تصحیف شده,

‏کی آرش‌دوم بد. سوم کی‌پشین.
۱ - در عربی « تنوط * < مهذب‌الاسماء » « صاب » < فرهنگه

‏فردوسی‌طوسی.

‎fell‏ + ۲- «کیب , از راستی بکژی شبن با فریفتن بعشق بود .» « لفت فرس چاپ

‏اقبال ‎Otay‏ . ( کیب » ربشة کیبیدن است) :
یارب ییافربدی روبی بدین مثال

‏خود رحم کن‌برامت وازراهشان مکیب.

‏شهیدبلخی. «لفت‌فری چاپ‌هرنس*۱*.

‏۸ - مرغ‌سنگخوار که‌پیدترسنگه ‎apy‏ خورد هرشیدی» . ‎By ٩‏ فهرست‌مخزن‌الادوبه.
```


## [2026-09-06T20:37:50.172Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN acoustic ===\"; grep -n -o \"acoustic.\\{0,400\\}\" KLN_1966.txt | head -3; echo \"=== KLN kudos ===\"; grep -n -o \"kudos.\\{0,350\\}\" KLN_1966.txt | head -3; echo \"=== KLN caveat ===\"; grep -n -o \"caveat.\\{0,350\\}\" KLN_1966.txt | head -3"
}
```


### [2026-09-06T20:37:51.838Z] TOOL RESULT

```
=== KLN acoustic ===
1473:acoustic  and  meter,  ‘poetical  rhythm  . -acousia,  -acousis,  combining  forms  meaning ‘hearing’.  —  Fr.  Gk.  dxooaic,  hearing ,  fr. axouEiv,  ‘to  hear’.  See  acoustic, acoustic,  adj.  —  F.  acoustique,  fr.  Gk.axouoxtxo^, pertaining  to  hearing’,  fr.  axoucrxi;,  ‘heard, audible’,  verbal  adj.  of  dxoueiv,  ‘to  hear’,  which stands  for  *dxou<n.Etv,  and  is  prob.  formed  fr. copul.
1473:acoustic-al,  adj.,  acoustic-al-ly, •dv.,  acoust-ics,  n.
11217:acoustic,  adj.,  pertaining  to  the  refraction  of sounds.  —  Formed  fr.  di-  (form  of  dia-  before a  vowel)  and  acoustic.
=== KLN kudos ===
20879:kudos,  n.,  fame,  renown  ( colloq .)  —  Gk.  xOSoq,
35051:kudos,  and the  second  element  in  Laocoon.
=== KLN caveat ===
6865:caveat
6868:caveat,  n.,  i)  notice  that  no  action  is  to  be  taken (law)\  2)  a  warning.  —  L.,  ‘let  him  beware’,  3rd p.  sing.  pres.  subj.  of  cavere.  See  prec.  word, cavendish,  n.,  tobacco  pressed  into  cakes.  —  Prob. so  called  from  the  name  of  the  producer  or exporter.
```


## [2026-09-06T20:37:51.902Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT hear ===\"; grep -n -o \"HEAR,.\\{0,300\\}\\|Hear, .\\{0,300\\}\" SKT.txt | head -5; echo \"=== SKT show ===\"; grep -n -o \"SHOW,.\\{0,300\\}\" SKT.txt | head -5; echo \"=== SKT acoustic ===\"; grep -n -o \"ACOUSTIC.\\{0,300\\}\" SKT.txt | head -3"
}
```


### [2026-09-06T20:37:54.175Z] TOOL RESULT

```
=== SKT hear ===
=== SKT show ===
=== SKT acoustic ===
351:ACOUSTIC.
```


## [2026-09-06T20:38:00.281Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20879,20882p' KLN_1966.txt; echo \"=== cave/caution ===\"; sed -n '6860,6872p' KLN_1966.txt; echo \"=== caution ===\"; grep -n -o \"caution,  n.\\{0,300\\}\" KLN_1966.txt | head -3"
}
```


## [2026-09-06T20:38:01.319Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"hear,  intr\\.\\{0,500\\}\\|hear,  tr\\.\\{0,500\\}\" KLN_1966.txt | head -3; echo \"=== show ===\"; grep -n -o \"show,  tr\\.\\{0,500\\}\" KLN_1966.txt | head -3"
}
```


### [2026-09-06T20:38:01.931Z] TOOL RESULT

```
kudos,  n.,  fame,  renown  ( colloq .)  —  Gk.  xOSoq,
‘glory,  fame’,  which  stands  for  *qudos  and  lit. means  ‘that  which  is  heard  of’.  It  is  cogn.  with OSlav.  cudo,  gen.  -esc  (for  *qeudos),  ‘wonder’, lit.  ‘that  which  is  heard  of’,  fr.  cujq,  cuti,  ‘to feel,  perceive,  hear’.  Cp.  Gk.  xoeoj,  ‘I  mark, perceive,  hear’,  and  see  show, kudu,  n.,  a  large  S.  African  antelope  (Strepsiceros kudu).  —  Hottentot.
Kufic,  Cufic,  adj.,  1)  pertaining  to  the  town  Kufa;
2)  applied  to  a  form  of  Arabic  letters  used  at Kufa  by  copyists  of  the  Qoran.  —  Formed  with
=== cave/caution ===
Derivatives:  cautious-ly,  adv.,  cautious-ness,  n. cavalcade,  n.,  a  procession  of  horsemen.  —  F.,  fr. It.  cavalcata  (with  the  Piemont  pronunciation cavalcada),  prop.  fern.  pp.  of  cavalcare,  ‘to  ride
on  horseback’,  used  as  a  noun,  fr.  Late  L.  cabal- licdre,  fr.  L.  caballus.  See  cavalry.
Derivative:  cavalcade,  intr.  v. cavalier,  n.,  a  horseman;  a  gentleman  serving  as a  lady’s  escort.  —  F.,  fr.  It.  cavaliere,  orig. ‘horse-soldier’,  fr.Late  L.  caballarius  (whence  al¬ so  Proven?,  cavalier,  Sp.  Caballero,  Port,  caval- leiro),  fr.  L.  caballus.  See  cavalry  and  cp.  cheva¬ lier,  which  is  a  doublet  of  cavalier.
Derivatives:  cavalier,  adj.,  cavalier-ly,  adv. cavalla,  n.,  any  of  various  fishes  of  the  genus Carangus.  —  Port,  cavalla,  rel.  to  Sp.  caballa, prop,  a  feminine  form  of  Port,  cavallo,  resp.  Sp. cabalto,  ‘horse’,  fr.  L.  caballus.  See  cavalry, cavalry,  n.  —  F.  cavalerie,  fr.  It.  cavalleria,  fr. cavallo,  ‘horse’,  fr.  L.  caballus,  ‘an  inferior horse,  a  nag’,  which  is  prob.  a  loan  word  from a  language  of  Asia  Minor  or  the  Balkan  pen¬ insula.  Cp.  Gk.  xa(3xXX7)i;,  ‘horse’,  the  Gaulish PN.  Caballos  and  OSlav.  kobvla,  ‘mare’,  which also  derive  prob.  from  the  same  language  as  L: caballus.  Mir.  (=  lr.)  capatl,  Bret,  caval,  W. ceffyll,  ‘horse’,  are  Latin  loan  words.  Cp.  chival¬ ry,  which  is  a  doublet  of  cavalry.  Cp.  also  caval¬ cade,  cavalier,  cavalla,  cheval-de-frise,  cheval glass,  chevalier,  capercailzie, cavatina,  n.,  a  short  song  or  melody  (mus.)  —  It .,  fr. cavata,  prop.  fem.  pp.  of  cavare,  ‘to  hollow(out), dig  (out)’,  fr.  L.  cavdre,  of  s.m.  See  next  word, cave,  n.  —  F.,  fr.  L.  cava,  fem.  of  the  adjective owes, ’hollow,  concave’,  used  as  a  noun.  L.  cavus prob.  stands  for  *cowos  and  is  cogn.  with  Gk. xooc  (Hesychius),  ‘chasm’,  xoiop,  ‘prison  (lit.
‘a  hollow  place’),  xovSeix,  ‘poppy  head",  xoTXo; (for  *x65i>.o?),  ‘hollow’,  xuap.  ‘eye  of  a  needle; orifice  of  the  ear’.  OI  r.  cita,  ‘hollow’,  cuass,  ’cave’, Bret,  keo,  ‘cave’,  OI.  svdyatc,  ‘swells’,  sitndh, ‘swollen’,  savas-,  ‘strength,  heroism’,  sdvirah, surah,  ‘strong’,  Gk.  y.-iz iv.  x'isiv,  ’to  become  or be  pregnant’,  /.Oar.,  ‘anything  swollen;  a  wave’, xopo:,  ’authority’,  xOpt 0;.  ‘lord,  master'.  All these  words  prob.  derive  fr.  I.-E.  base  *kcw(e)-, *kewd-,  *kii-,  ‘to  vault',  whence  developed  the further  meanings  'to  bend  inward,  be  hollow  or concave',  on  the  one  hand,  and  'to  bend  out¬ ward,  swell  out,  be  convex'  on  the  other.  See Waldc-Hofmann,  LEW.,  1.  pp.  191-92  s.v. cavus.  Boisacq,  DELG..  p.qSi  s.v.  xau’/zk  and Frisk,  GEW„  p.  38  s.v.  v-iy.z.  Cp.  cabinet,  ca- book,  cadger,  cage,  casserole,  cavatina,  cave  ne, cavity,  church  and  words  there  referred  to,  co¬ deine.  codon,  coelo-,  concave,  cumulus,  cyma, decoy,  excavate,  excavation,  gabion,  hound ( naut .),  jail.  Cp.  the  related  base  *keu-.  'toswell ; hollow',  for  the  derivatives  of  which  see  hole. Derivatives:  care,  tr.  and  intr.  v.,  cav-ing.  n. cave,  interj.,  beware!  —  L.  cave,  itnper.  of  cavere, ‘to  be  on  one’s  guard,  take  care,  beware',  which stands  for  *co\ere  and  is  cogn.  with  Gk.  x oeto (for  *vcori(d),  ‘I  mark,  perceive’,  fr.  I.-E.  base *(s)qeu-,  *(s)qeu-,  ‘to  look  at,  observe’,  whence also  OE.  sceawian,  ‘to  look,  see,  behold'.  See
caveat
bCICI  I
254
show  and  words  there  referred  to  and  cp.  esp. caution.  Cp.  also  next  word, caveat,  n.,  i)  notice  that  no  action  is  to  be  taken (law)\  2)  a  warning.  —  L.,  ‘let  him  beware’,  3rd p.  sing.  pres.  subj.  of  cavere.  See  prec.  word, cavendish,  n.,  tobacco  pressed  into  cakes.  —  Prob. so  called  from  the  name  of  the  producer  or exporter.
cavern,  n.,  a  cave.  —  F.  caverne,  ‘cave’,  fr.  L. caverna,  fr.  cavus,  ‘hollow’.  See  cave,  n.  For  the Latin  suff.  -erna,  which  is  of  Etruscan  origin, cp.  cistern ,  tavern.
cavernous,  adj.,  full  of  caverns  or  cavities.  —  L. cavernosas,  fr.  caverna.  See  prec.  word  and  -ous. cavesson,  n.,  a  kind  of  noseband  for  a  horse.  — F.  cavegon,  fr.  It.  cavezzone,  ‘halter  with  a  nose¬ band',  augment,  of  cavezza,  ‘halter’,  fr.  VL. *capitia,  fr.  L.  capitium,  ‘a  covering  for  the head’,  fr.  caput,  gen.  capitis,  ‘head’.  See  capital, adj.
Cavia,  n.,  the  genus  of  cavies,  the  guinea  pig (zool.)  —  ModL.,  fr.  F.  cabiai,  from  a  Carib¬ bean  native  word.  Cp.  cavy,  capybara. caviar,  caviare,  n.  —  F.  caviar,  fr.  It.  caviaro  (now caviale),  fr.  MGk.  xaptxpiov,  fr.  Turk,  khavidr, fr.  Kaffah  (=  Theodosia),  name  of  a  trading town  on  the  SE.  shore  of  the  Black  Sea. cavicorn,  adj.,  hollow-horned.  —  Compounded of  L.  cavus,  ‘hollow’,  and  cormi,  ‘horn’.  See cave,  n.,  and  horn  and  cp.  corn,  ‘hardened  skin’. Cavicornia,  n.  pi.,  another  name  for  Bovidae (zool.)  —  Lit.  ‘hollow-horned’.  See  prec.  word, cavil,  intr.  v.,  to  find  trivial  faults,  to  carp.  — OF.  caviller,  fr.  L.  cavilldri,  ‘to  jest,  joke,  make captious  objections,  to  cavil  at’,  fr.  cavilla,  ‘jest, quibble,  trick’,  dissimilated  fr.  *calvilla,  and rel.  to  calvi,  ‘to  devise  tricks,  use  artifice’,  calum- nia,  ‘false  accusation,  chicanery';  see  calumny and  cp.  challenge.  For  the  suff.  cp.  L.  favilla, 'glowing  ashes,  embers'  which  is  rel.  to  fovere, ‘to  warm,  keep  warm'.
Derivatives:  cavil,  n.,  cavillation  (q.v.),  cavill¬ er,  n.,  cavil(l)-ing,  adj.,  cavil(l)-ing-ly,  adv.,  ca- vil(l)-ing-ncss,  n.
=== caution ===
6858:caution,  n.  —  F.,  fr.  L.  cautidnem,  acc.  of  cautio, ’wariness,  carefulness,  heedfulness',  fr.  cautus, ‘wary,  careful,  heedful',  pp.  of  cavere,  'to  be  on one’s  guard,  take  heed’.  See  cave,  interj. Derivatives:  caution,  tr.  v.,  caution-ary,  adj.  and n.,  caution-er,  n.
29951:caution,  n.  —  F.  precaution,  fr.  Late  L.  prae- cautionem,  acc.  of  praecautio,  fr.  L.  praecautus, pp.  of  praecavere,  ‘to  guard  against  beforehand’, fr.  prae  (see  pre-)  and  cavere,  ‘to  be  on  one’s guard’.  See  caution.
```


### [2026-09-06T20:38:04.333Z] TOOL RESULT

```
17351:hear,  tr.
34915:hear,  tr.
=== show ===
```


## [2026-09-06T20:38:12.134Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17351,17356p' KLN_1966.txt; echo \"==== show ====\"; grep -n \"^show,\\|show,  tr\" KLN_1966.txt | head; grep -n -o \"OE.  sceawian.\\{0,600\\}\" KLN_1966.txt | head -4"
}
```


### [2026-09-06T20:38:14.780Z] TOOL RESULT

```
hear,  tr.  and  intr.  v.  —  ME.  heren,  fr.  OE.  hieran, hyran,  heron,  rel.  to  ON.  heyra,  Swed.  hdra, Dan.  here,  OS.  horian,  OFris.  hera,  hora,  Du. horen,  OHG.  horan,  horren,  MHG.  haren,  G. horen,  Goth,  hausjan,  fr.  I.-E.  base  *(s)qeu-, *{s)qeu-,  ‘to  look  at,  observe,  perceive’,  whence also  OI.  kavlh,  ‘wise’,  Gk.  jtoeiv,  ‘to  mark,  per¬ ceive,  hear’,  and  prob.  also  axouetv  (with  copul. pref.  a-),  ‘to  hear’.  See  show  and  cp.  hark,  hear¬ ken.  Cp.  also  acoustic.
Derivatives:  hear-er,  n.,  hear-ing,  n. heard,  past  tense  and  pp.  of  hear.  —  ME.  herde, fr.  OE.  herde,  fr.  heron,  ‘to  hear’.  See  hear, hearken,  intr.  and  tr.  v.  (the  latter  is  archaic).  — ME.  herknien,  herknen,  fr.  OE.  heorcnian, hyrcnian,  rel.  to  OFris.  harkia,  herkia  and  to E.  hark  (q.v.)
Derivative:  hearken-er,  n. hearse,  n.  —  ME.  herce,  herse,  fr.  MF.  herce (F.  herse),  ‘harrow;  portcullis;  triangular  frame for  holding  candles’,  fr.  L.  hirpicem,  acc.  of hirpex,  ‘harrow’,  fr.  Samnite  hirpus,  ‘wolf’; so  called  in  allusion  to  the  teeth  of  the  harrow, which  resemble  the  teeth  of  a  wolf.  Samnite hir-pus  is  rel.  to  L.  hir-cus,  ‘he-goat’.  Both  these words  are  prob.  rel.  to  L.  hir-sutus,  ‘shaggy, prickly,  bristly’.  See  hirsute  and  cp,  rehearse. Derivative:  hearse,  tr.  v.
heart,  n.  —  ME.  herte,  hert,  fr.  OE.  heorte,  rel. to  OS.  herta,  ON.  hjarta,  OFris.  herte,  hirte, ODu.  herta,  Du.  hart,  OHG.  herza,  MHG. herze,  G.  Herz,  Goth,  halrto,  ‘heart’,  and  cogn. with  Hitt,  kardiash  (gen.),  ‘of  the  heart’,  Arm. sir!  (for  *kerdi-),  Gk.  xapSta,  poet.  >a)p,  L.  cor (gen.  cordis),  OSIav.  srudice,  Russ,  serdce, ‘heart’,  Lith.  Sirdis,  ‘heart’,  OPruss.  seyr  (for *kerd),  acc.  siran,  OIr.  cride,  Ir.  croidhe,  ‘heart’, W.  craidd,  ‘heart;  center’,  Bret,  kreiz,  ‘middle’, OSIav.  sridd,  Russ,  seredd,  ‘middle’,  Avestic zlrl6aya-,  ‘middle’.  For  sense  development  cp. Heb.  lebh,  ‘heart’,  and  lebh  yam,  ‘the  midst  (lit. the  heart)  of  the  sea’,  lebh  ha'eli <*,  ‘the  midst of  the  terebinth’,  Akkad,  libbu,  ‘heart;  middle’. Cp.  cordate,  cordial,  core,  accord,  accordion, codling,  ‘a  variety  of  apple’,  courage,  concord, discord,  misericord,  record.  Cp.  also  cardiac, cardio-,  carditis,  endocardium,  epicardium,  peri¬ cardium.  L.  credere,  ‘to  believe’,  is  not  related to  L.  cor,  ‘heart’  (see  creed).
Derivatives:  heart,  tr.  and  intr.  v.,  heart-ed,  adj., heart-ed-ly,  adv.,  heart-en,  tr.  and  intr.  v.,  heart- en-er,  n.,  heart-y,  adj.,  heart-i-ly,  adv.,  heart-i- ness,  n.,  heart-less,  adj.,  heart-less-ly,  adv.,  heart- less-ness,  n.
hearth,  n.  —  ME.  berth,  fr.  OE.  heord,  rel.  to  OS., OFris.  herth,  MDu.  hert,  Du.  hoard,  OHG.
==== show ====
35051:show,  archaic  spelling  shew,  tr.  and  intr.  v.  — ME.  schewen,  schowen,  shewen,  showen,  fr.  OE. sceawian,  ‘to  look,  see,  behold’  (in  modern English  the  sense  is  causative:  ‘to  cause  to  be seen’);  rel.  to  OS.  skauwon,  ‘to  look  at’,  OFris. skawia,  Du.  schouwen,  OHG.  scouwon,  MHG. schouwen,  G.  schauen,  ‘to  look  at’,  OE.  sciene, scene,  scyne,  OS.,  OHG.  skoni,  MDu.  scone, Du.  schoon,  Goth,  skaunjai  (nom.  pi.),  ‘beauti¬ ful’,  orig.  ‘conspicuous’,  fr.  I.-E.  base  *{s)qeu-, *(s)qeu-,  ‘to  look  at,  observe,  perceive",  whence also  OI.  kavilt,  ‘wise,  sage;  seer,  poet’,  d-kuvate, ‘intends’.  Arm.  cucanem,  ‘I  show’,  Gk.  xosco (for  ‘xofico),  .‘I  mark,  perceive,  hear’,  xG8o<; (for  qudos),  'glory,  fame’  (lit.  ‘that  which  is heard  of’),  the  second  element  in  Ouo-axoo?, (for  ’'■Ouo-oxofoc),  ‘sacrificing  priest’,  L. cavere,  ‘to  beware’,  OSlav.  cujQ,  cuti,  ‘to  fee), perceive,  hear’,  cudo,  gen.  -ese  (for  *qeudos ), ‘wonder’,  lit.  (‘that  which  is  heard  of’),  Czech ( z)koumati ,  ‘to  perceive,  be  aware  of’.  See  hear and  cp.  scavage,  scavenger,  sheen.  Cp.  also acoustic,  caution,  cave,  interj.,  Kavi,  kudos,  and the  second  element  in  Laocoon.
6864:OE.  sceawian,  ‘to  look,  see,  behold'.  See
20554:OE.  sceawian,  ‘to  look, see'.  See  show  and  cp.  words  there  referred  to. kayak,  n.,  an  Eskimo  canoe  made  of  sealskin stretched  on  a  wooden  frame.  —  Eskimo, kea,  n.,  a  large  New  Zealand  parrot.  —  Maori, keck,  intr.  v„  to  retch.  —  Imitative.
33988:OE.  sceawian,  ‘to  look  at’,  and  see show  and  -age.  Cp.  scavenger.
```


## [2026-09-06T20:38:20.717Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20548,20556p' KLN_1966.txt"
}
```


### [2026-09-06T20:38:20.772Z] TOOL RESULT

```
Katharine,  Katherine,  fem.  PN.  —  See  Catherine, katydid,  n.,  an  insect  of  the  locust  family.  —  So
841
called  from  the  stridulous  sound  of  the  insect, suggestive  of  the  words  katy  did.
Derivative:  katydid,  intr.  v. kauri,  n.,  a  tall  tree  of  New  Zealand  ( Agathis australis).  —  Maori.
kava,  n.,  a  Polynesian  pepper  shrub.  —  Native name.
kavass,  n.,  a  Turkish  policeman.  —  Turk,  qawas, fr.  Arab,  qawwds,  ‘bowman’,  fr.  Arab,  qaus, ‘bow’,  which  is  rel.  to  Heb.  qesheth,  Aram. qashtd ,  Syr.  qeshtd,  Akkad,  qasthu,  Ethiop. qast ,  ‘bow’,  Heb.  qashshdth,  Aram,  qashshathd, Syr.  qushshathd,  ‘bowman’.
Kavi,  Kawi,  n.,  the  ancient  language  of  Java.  — Javanese  kavi,  ‘poetic  (scil.  language)’,  fr.  OI. kavih,  ‘wise,  sage;  seer,  poet’,  which  is  rel.  to kavarifi,  ‘stingy’,  a-kuvate,  ‘intends’,  and  cogn. with  Gk.  xoew  (for  *xoF£u),  ‘I  mark,  perceive, hear’,  fr.  I.-E.  base  *(s)qSu-,  ‘to  look  at,  observe, perceive’,  whence  also  OE.  sceawian,  ‘to  look, see'.  See  show  and  cp.  words  there  referred  to. kayak,  n.,  an  Eskimo  canoe  made  of  sealskin stretched  on  a  wooden  frame.  —  Eskimo, kea,  n.,  a  large  New  Zealand  parrot.  —  Maori, keck,  intr.  v„  to  retch.  —  Imitative.
Kedar,  n.,  a  tribe  of  northern  Arabia.  —  Heb. Qedhdr,  fr.  Qedhdr,  son  of  Ishmael  (see  Gen. 25:3,  IChr.  1:29),  rel.  to  qadhar,  ‘was  black, dark,  swarthy’,  whence  also  qadhruth,  ‘dark¬ ness,  gloom’,  qedhorannlth,  ‘gloomily,’  QidhrSn, name  of  a  wady  and  valley  east  of  Jerusalem, Mishnaic  Heb.  qldherdh,  ‘pot’,  qadddr,  ‘potter’, and  to  Aram,  qidhrd,  qedherd,  Syr.  qedhrd,  ‘pot’, Arab,  qddhura,  qadhira,  ‘was  dirty’.
Derivative:  Kedar-ite ,  adj.  and  n. keddah,  n.,  an  enclosure  for  entrapping  ele¬ phants  (India).  —  Hind,  khedd,  rel.  to  khedna ‘to  chase,  hunt’,  fr.  OI.  akhetah,  khetah,  ‘hun¬ ting’,  which  is  of  uncertain  origin, kedge,  tr.  v.,  to  warp  (a  ship);  intr.  v.,  to  move a  ship  by  kedging  ( naut .)  —  Of  uncertain  ori¬ gin;  perh.  a  var.  of  cadge, kedgeree,  n.,  a  mixture  of  rice  and  lentils  cooked together  (India)  — -  Hind,  khichri,  fr.  OI.  khicca, which  is  of  uncertain  origin.
```


## [2026-09-06T20:38:22.385Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC keu ===\"; grep -n \"^Keu-\\|^Kou-\\|^Skeu-\\|^Kau-\\|^Kaui\" IEC.txt | head -20; echo \"=== IEC kavi ===\"; grep -n -o \"Kaui.\\{0,200\\}\" IEC.txt | head -5"
}
```


### [2026-09-06T20:38:23.923Z] TOOL RESULT

```
=== IEC keu ===
8599:Kauio (1) “burn, scorch, dry’. Cf. Kaustos. WP I, 376 Myc. kaw- ‘kindle’; Gk. kaio, fut. kaúso ‘kindle; shrivel; burn’; Alb. thaj ‘dry’, OHG heian, MHG heien, intr. ‘burn’; cf. G hei, adj. ‘dry’; Swiss ge-hei, adj. (2), id.: cf. G He- rauch ‘smoke from burning moor’. The se- mantics of Go. hawi, OHG houwi, etc. ‘hay’ are uncertain. See kau- ‘hit’. A variant of the above root occurs apparently in Av. saoko, saoco, m. “burning, burn, fuel
8735:Keu- (Keuos, à) “death, famine'. Cf. Kouo Skt. savah, am ‘corpse’; Arm. sov, u-st. 'fa- mine’. (Isophone: Av. savo, savom *'use")
=== IEC kavi ===
8596:Kauið (1) and WP I, 376 Arm. cf. Sawt', Let (*cake; biscuit’; initial š- by induction); Gk. kaustós, kautós ‘dry’; Alb. i thatë, id.; ON haust, n. ‘autumn’; Sw. höst, id. beside ON hauór, n. ('earth' fr. 
8599:Kauio (1) “burn, scorch, dry’. Cf. Kaustos. WP I, 376 Myc. kaw- ‘kindle’; Gk. kaio, fut. kaúso ‘kindle; shrivel; burn’; Alb. thaj ‘dry’, OHG heian, MHG heien, intr. ‘burn’; cf. G hei, adj. ‘dry’; Swiss ge
```


## [2026-09-06T20:38:32.020Z] TOOL CALL #35: Bash

```json
{
 "command": "ls site/pages/263.jpg 2>/dev/null; pdftoppm -f 263 -l 263 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg263 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-06T20:38:34.440Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"369\" incoming/WLD/WLD_Bd1_pages.txt | grep -i \"pdf page\" | head -3; echo \"---\"; grep -n \"pdf page\" incoming/WLD/WLD_Bd1_pages.txt | head -3; echo \"=== search keu in WLD Bd1 ===\"; grep -n \"keu-\\s*:\\|(s)qeu\\|qeu-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20"
}
```


### [2026-09-06T20:38:34.490Z] TOOL RESULT

```
site/pages/263.jpg
total 264
drwx------ 2 sfmqrb sfmqrb  4096 Sep  6 16:38 .
drwx------ 4 sfmqrb sfmqrb  4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   132 Sep  6 16:34 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb  4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb  5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb   228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb 71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb 92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb 57862 Sep  6 16:35 pg264.png
```


### [2026-09-06T20:38:34.554Z] TOOL RESULT

```
---
=== search keu in WLD Bd1 ===
20843:qau-, qeu- „hauen, schlagen". 
22145:dies sicher zu lat. ctlpa usw., Wz. qeu-p-) usw. (germ. Basis *hanaf-). 
22762:eber zu sqeu- „bedeeken“, wie das von Noreen Ltl. 205 mit an. hy „Flaum“ 
23178:keu- — qeu- 
23228:1. qeu-, dehnstufig qeu- „woraufachten(beobachten, schauen? s. u.), worauf 
23242:qeu- 
23255:jueXcog , sorglich" sucbt); xvdog (s. u. zu slav. cudo)-, von der Basis qeu-s- axovoo 
23272:dann etwa an (s) qeu-s- „bedecken“ ankniipfen und nicht iiberzeugend d- 
23281:„*cautens“ (v. Planta Gr. 1 473); iiber das vielleicht zur s-Erw. qeu-s ge- 
23282:horige lat. custos (Bezzenberger aaO.) s. u. *sqm-, *sqeu-s- „bedecken“. 
23287:*sqeu- „bedecken“ und lcci- in Farbbezeichnungen). 
23296:„Wunder“ : diviti se „schauen“; *qeu-dos, ablautend mit gr. xvdog „Ruhm, 
23307:qeu- 
23313:*qeu-s- in mss. mdartl. ciklmib „wahrnehmen, horen", sloven, cuha-m, -fi 
23327:Msl. 8, 296, Scheftelowitz BB. 28, 294; sqeu-sko); gr. dvoonoos „Opfer- 
23348:mit qeu - „worauf achten, merken" ganz fraglich; jedenfalls war sqeu- gegen- 
23349:iiber qeu- bereits ursprachlich auf die Wahrnehmung durchs Auge ein- 
23350:geschrankt. Hirts TF. 37, 231 Yereinigung von sqeu- mit scq'i- „sehen“ 
23351:(got . saih'.m usw.) unter seqeu- : sqeu- : sequ- ist aber trotzdem nicht wahr- 
23358:2. qeu- bes. mit labialen oder gutturalen Erweiterungen: „biegen“ in ver-
```


## [2026-09-06T20:38:39.209Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23220,23260p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-06T20:38:39.272Z] TOOL RESULT

```
keu-bh ai. gubhate „ist schmuck, stattlicb, nimmt sich schon aus", 
gobhand- „schmuck, gliinzend", gubha- „schmuck, hiibsch, angenehm, er- 
freulich", gubhrd- „schmuck, schon, glanzend, hellfarbig" = arm. surb „rein, 
heilig", srbem „reinige, heilige" (Hubschmann Arm. Gr. I 492). 

Icu-en- „feiern, heiligen"? s. u. bes. Schlagwort. 
ku-eit- s. u. bes. Schlagwort. 

1. qeu-, dehnstufig qeu- „woraufachten(beobachten, schauen? s. u.), worauf 

horen, fiihlen, merken"; set-Basis qoue-, auch (urspriinglicher?) qouei- 

(s. Hirt Abl. 102, 109, Persson Beitr. 726); s-Erw. qeit-s-; iiber Formen 

mit anl. s- s. am Schlusse. 

Ai. kavi „klug, weise ; Seher, Dichter" (Bildung wie gr. r goyjg), kavl- 

yas- , kluger", kavari „eigennutzig, karg" {kavatnu- vielleicht ds.), a-kava- 



qeu- 


369 


„nicht karg‘ ; ; a-kucate „beabsichtigt“, a-ktlta- n., d-kuti- f. „Absicht“ (vgl. 
bes. Osthoff MU. IV 92, 105); av. covisi l. Sg. med. Aor. „icb erhoffte, 
veraah mich“ (vgl. Bartholomae BB. 13, 66, Airan. Wb. 442). 

Gr. xoeco „merke“ (kann ebensowenig wie lat. caveo als sicherer Beleg 
der set-Basis qoue- gelten, da beide vielleicht Denominative eines *kouo-s, 
Zupitza KZ. 40, 251, Prellwitz 2 38, der dieses :f xofog in jon .att. dva-xmg „em- 
jueXcog , sorglich" sucbt); xvdog (s. u. zu slav. cudo)-, von der Basis qeu-s- axovoo 
„hore“ ( *axovoico ), dxoiq, liom. axovrj „Gehor“ ( *dxovoa ), vm'jxoog „gehor- 
sam, untertan“, lak. endxoog „Zeuge“, dxevei * itjosT Hes., gort. axsvovrog 
(nicht nacb dh'jXovda : ekevoo/aai zu *axrjxova neugeschaffen, sondern mit 
altem e-Vok., wahrend ay.ovco von *d.y.ovod abhangt).
```


## [2026-09-06T20:38:40.035Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23300,23360p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-06T20:38:40.088Z] TOOL RESULT

```
s. qeud-); 



370 


qeu- 


serb. ciivati „hiiten" (anders, aber in der Bed. unbefriedigend, Birt BB. 
24, 254) ; ursl. *cecq, *ceviti in acech. vs-cieviti, na-vs-cieviti , heute navsti- 
viti „besuchen“ (s. Berneker 162 m. Lit., wozu noch Zupitza KZ. 40, 251); 
*qeu-s- in mss. mdartl. ciklmib „wahrnehmen, horen", sloven, cuha-m, -fi 
„spiiren, ahnen", cech. cich „Sinn, Witterung, Spur" (Berneker aaO. m. Lit.). 

Dasselbe d wie cudo scheint im s-anl. apr. au-schaudltwei „vertrauen“, 
auschaude „er traut" vorzuliegen (Trautmann Apr. 308). Dagegen ist lit. 
kavoti , verwahren, pflegen" Lw. aus poln. choivac (Bruckner Lw. 92). Unter 
einer Bed. -Entw. „sich verseben, sich bedenken" — „zaudern, zogern" 
will Persson Beitr. 726 lett. kavet „zaudern, zogern" (wiire = lat. cavSre), 
ktitrs „trag, faul" anreihen. 

Mit anl. s-: miran. skoh, np. sikoh, sukoh (uriran. *skaua!)a-) „Pracht, 
Herrlichkeit, Majestat, Wiirde" (Bartholomae ZfdtWtf. 9, 19); 

arm. cucanem ,,lasse schauen, zeige", coyc „das Zeigen, Schau" (Meillet 
Msl. 8, 296, Scheftelowitz BB. 28, 294; sqeu-sko); gr. dvoonoos „Opfer- 
schauer" = got. us-slmvs „(*ausschauend =) besonnen", ags. sceaunan , as. 
skauivdn , ahd. scouwon „sckauen“; aisl. si yqn „sehend, scharfsichtig" (*skuv- 
vini -), wo von skygna „spahen“; got. skanns ,.schon“, ahd. sconi ds., as. 
skoni „glanzend, schon", ags. sclene ds. (eigentlieh „conspicuus“; auf eine 
Gdbed. „Aussehen“ weist auch got. ibna-skauns „von gleicher Gestalt", 
guda-skaunei „Gottesgestalt“), woneben tiefstufiges *skn-ni- als Grundlage 
von aisl. skyn f. n. „Ordnung, Bescheid, Verstandnis, Einsicht", skynja 
„untersucben, verstehen" (schwed. skiinja noch mit der urspriinglicheren 
Bed. „mit dem Auge unterscheiden, gewahr werden" neben der abgelei- 
teten „einsehen", Ealk-Torp u. skj<fni „Gutacbten“) ; aisl. skoda „spahen“. 

Dagegen ahd. scuwo „Schatten“, got. skuggtva ,,Spiegel" usw. s. u. sqen - 
„bedecken“. — Als s-lose Wechselform neben got. skauns usw. erwagt 
FickII 4 89 cymr. cun ..anziehend, liebenswurdig" gall. EN. Counos , air. 
Cuan, cuan-dae ,,schon, angenehm", doch scheint die Gdbed. verschieden 
zu sein (zu lit. ha units „brav, tiichtig" ebenda?? doch s. iiber letzteres 
keu- „schwellen“). 

Weil diese s-anl. Formen durckweg die spezielle Bed. „schauen“ auf- 
weisen (freilich nicht so apr. auschaudltwei , s. o ), ist ihre Yerwandtschaft 
mit qeu - „worauf achten, merken" ganz fraglich; jedenfalls war sqeu- gegen- 
iiber qeu- bereits ursprachlich auf die Wahrnehmung durchs Auge ein- 
geschrankt. Hirts TF. 37, 231 Yereinigung von sqeu- mit scq'i- „sehen“ 
(got . saih'.m usw.) unter seqeu- : sqeu- : sequ- ist aber trotzdem nicht wahr- 
scheinlich. 

Ygl. im allgem Curtius 5 152, Zupitza Gutt. 152 (m. Lit.), Berneker IF. 
10, 151, Yf. LEWb. 2 u. caveo, Berneker Wb. 161, 1 6 2 f . , 643, und bes. 
Bezzenberger BB. 27, 145f. 

2. qeu- bes. mit labialen oder gutturalen Erweiterungen: „biegen“ in ver- 
schiedenen Sonderungen wie „i m Gelenk biegen, Gelenk, sich biicken, 
sich drehen"; „Einbiegung, EinwOlbung. Ilohlung"; „Ausbiegung, Buckel,
```


## [2026-09-06T20:38:52.053Z] TOOL CALL #39: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/263.jpg"
}
```


### [2026-09-06T20:38:52.073Z] TOOL RESULT

```

```


## [2026-09-06T20:39:14.125Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 263 -l 263 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf p263hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('p263hi.png'); print(im.size)\nw,h=im.size\n# crop Latin/Germanic area: roughly y 780-900 of 1100-tall preview -> fraction\nim.crop((int(0.20*w),int(0.68*h),int(0.80*w),int(0.80*h))).save('crop_lat.png')\nim.crop((int(0.55*w),int(0.53*h),int(0.82*w),int(0.60*h))).save('crop_ak.png')\n\""
}
```


### [2026-09-06T20:39:17.136Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-06T20:39:19.561Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_lat.png"
}
```


### [2026-09-06T20:39:19.657Z] TOOL RESULT

```

```


## [2026-09-06T20:39:19.654Z] INPUT

[Image: original 2040x528, displayed at 2000x518. Multiply coordinates by 1.02 to map to original image.]


## [2026-09-06T20:39:25.675Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('p263hi.png'); w,h=im.size\nim.crop((int(0.20*w),int(0.545*h),int(0.85*w),int(0.63*h))).resize((int(0.65*w*1.2),int(0.085*h*1.2))).save('crop_lat2.png')\nim.crop((int(0.55*w),int(0.42*h),int(0.85*w),int(0.50*h))).save('crop_ak2.png')\n\""
}
```


### [2026-09-06T20:39:28.069Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T20:39:30.361Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_lat2.png"
}
```


### [2026-09-06T20:39:30.472Z] TOOL RESULT

```

```


## [2026-09-06T20:39:30.470Z] INPUT

[Image: original 2652x448, displayed at 2000x338. Multiply coordinates by 1.33 to map to original image.]


## [2026-09-06T20:39:35.433Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_ak2.png"
}
```


### [2026-09-06T20:39:35.452Z] TOOL RESULT

```

```


## [2026-09-06T20:39:40.197Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('p263hi.png'); w,h=im.size\nim.crop((int(0.20*w),int(0.415*h),int(0.55*w),int(0.50*h))).save('crop_gr.png')\nim.crop((int(0.18*w),int(0.30*h),int(0.60*w),int(0.42*h))).save('crop_op2.png')\n\""
}
```


### [2026-09-06T20:39:43.277Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T20:39:45.507Z] TOOL CALL #46: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_gr.png"
}
```


### [2026-09-06T20:39:45.533Z] TOOL RESULT

```

```


## [2026-09-06T20:39:52.441Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==105' incoming/ZAW/ZAW_pages.txt | head -60"
}
```


## [2026-09-06T20:39:53.230Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"شکوه\" MON_part1.txt MON_part2.txt | head -10; echo \"=== کیان ===\"; grep -n \"کیان\" MON_part1.txt MON_part2.txt | head -5; wc -c MON_part1.txt MON_part2.txt"
}
```


### [2026-09-06T20:39:54.751Z] TOOL RESULT

```
                             Zum AirWb . 1.        Exkurs § 82, 83 .                     81



           d) išqôhân 88 ; s. bp. 19 skoh, np. šikōh, šukōh 1) ;
      iškêft 832 ; s. bp. škaft; vgl. § 26 ; –
            e) išnûd 68, 87, 90, išnavâgân (MÜLLER ʻišnuvº) 88 ; s. np .
     śunūd-a, ušnūd- a, šinavāyān ; vgl. dazu HÜBSCHMANN PSt. 822) ;
=
         ʻišnâsêd 93, išnâsând 21; s. ap. xšnāsātiy ;                        'îšnôg 79, 'iš-
     nôhrag (M. harag) 51; s. jAw. xšnaogram und das arm. Lehn-
     wort šnorh ;
           f) išmâh 90, 463), išma 51 ; s. gAw. xšmākəm, np. šumā ;
         unklar 'išmag //// 65.
           Dazu die Bruchstücke is //// 66 und iš /// 73.
            § 83. Was die unter a bis e fallenden Wörter angeht, so      C


Be   kommen gegenüber den über 70 Fällen, darin ' s und ' š ge-
     schrieben wird, die wenigen Fälle mit abweichender Schreibung
     kaum in Betracht. Nach Ausscheidung von 'ašnásênd 27, das
     zump.           - anak np. ‫ آشنا‬ašnā, und von 'ašnûd 62, 68, ' aš-
     navâgân 25, die zu mp. ۱۱۳۱۳۳ āšnutan (s. HÜBSCHMANN PSt. 82)
     gehören - vgl. z. B. SWienAW. 67832                           ‫ آشنا‬ānavā u. a.
     belegt werden -, somit anlautendes a enthalten, bleiben nur die
     folgenden Wörter übrig : zu a) îstûd 74, îstâyand 69, îstâyišn
     1014), îstûn 413, îstûn 41, ' istávám 63, 'istâyišn 56, zu b) ispa-
     sag 65 und das zweifelhafte, von MÜLLER mit ?? versehene
          1( Aus ar. *skau - ath wie bp. ۳۲۳ handoh, np. ‫ اندوه‬andoh Sorge,
     Kummer' aus *san - day- ath , vgl. ai. davathu-h ' Brand, Schmerz' (anders
     GIrPh. 1 b. 186) . Das Wort gehört zu nhd. schauen, asächs. skauwōn. Wegen
     der Bedeutung ' Würde, Herrlichkeit, Pracht vergleiche man unser schön und
     Ansehen .

            2( Über das š von np. ‫) شنوده شود‬sinavad, sunuda) vgl. mein
     AirWb . 359. Ich mache darauf aufmerksam, daß sich im Mp. zu einem dem
     ksl. znayetŭ entsprechenden Präsens *šnāyēt cognoscit leicht ein PPP . *šnūt
     einstellen konnte ; selbstverständlich rein analogisch, vgl. HÜBSCHMANN PSt.
     135.*) Aus der Verschweißung der beiden Präsentien * šnāyēt und *sinnavēt
     (s. ai . śrnóti) ergab sich das übliche Präsens * šnavēt, np. šinavad.
               3) ' ismah, wie hier steht, ist doch wohl Druckfehler.
               4) In dem zweiten Abdruck des Blattes, S. 103 steht istâyišn.

       *) Von einem Übergang' des ā inū                    S. HÜBSCHMANN a. O., SALEMANN
          GIrPh . 1. 271, HORN GIrPh. 1b . 130             kann doch nicht wohl gesprochen
          werden.       Ich bemerke übrigens, daß dem mpI. framāt befohlen' gegen-
          über np. ‫ فرموده‬farmīda und dem mpB.                    nimat gezeigt' gegenüber
          .np ‫ نموده‬numuda            s . GIrPh . 1. 308      im MpT . framûd 83 und ni-
          mâd 83 entspricht .
        Idg. Forschungen XIX, Beiheft .                                         6
```


### [2026-09-06T20:39:54.816Z] TOOL RESULT

```
MON_part2.txt:5415:گله و رمه و ثروت و شکوه برخوردار و 
MON_part2.txt:10168:آشکوهشنتها کنبه: شته 
MON_part2.txt:15213:برخلاف زیبایی و شکوهی که در سطح آب 
MON_part2.txt:20153:جاه و جلال»؛ شکوه) شوکت. 
MON_part2.txt:21488:کردن. جولان کردن. جلال و شکوه» 
MON_part2.txt:34812:رضایت» شکایت» شکوه. ضعح.- در تداول 
MON_part2.txt:34857:شکایت کردن؛ شکوه کر دن. 
MON_part2.txt:40424:غضب يا غصه؛ ژکیدن. شکایت. شکوه. 
MON_part2.txt:49194:شکوه دارنده؛ ذو احتشام. خداوند خدم و 
MON_part2.txt:68942:مهابت: ۵۲50۸ ۱ع. سهابة | (.) شکوه» 
=== کیان ===
MON_part1.txt:228:1 -شاهان کیانی و هخامنشی در آثار الباقیه (در آموزش و پرورش سال ۱۵ 
MON_part1.txt:4321:سرم خون از آن شکیان بر هرد هاده بیاض 
MON_part1.txt:14882:گیاهی از تيرة پیچکیان که شبیه سس می‌باشد 
MON_part1.txt:19139:خاص) ج. ایچکیان. 
MON_part1.txt:21035:بنیرکیان که یکك ساله است و ساقه‌اش به 
4377831 MON_part1.txt
4331421 MON_part2.txt
8709252 total
```


## [2026-09-06T20:40:10.699Z] TOOL CALL #49: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T20:40:10.708Z] TOOL RESULT

```


```


## [2026-09-06T20:40:14.778Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1ewH-",
 "prompt": "What is this PIE root's meaning and what descendants (Sanskrit kavi, Avestan, Greek akouein/koeo/kudos, Latin caveo, Germanic hausjan/skawwon) are listed?"
}
```


## [2026-09-06T20:40:16.836Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%DA%A9%D9%88%D9%87",
 "prompt": "Give the full Persian etymology of شکوه (shokuh) 'glory, majesty' — Middle Persian form, Proto-Iranian reconstruction, and any cognates or cited sources."
}
```


### [2026-09-06T20:40:17.724Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T20:40:23.500Z] TOOL RESULT

```
# Persian Etymology of شکوه (shokuh)

Based on the Wiktionary entry provided, here is the etymological information available:

**Middle Persian origin:** The word is "Inherited from Middle Persian [script needed] (škwh /⁠škōh⁠/, 'dignity, majesty, fear')."

**Proto-Iranian reconstruction:** The document does not provide a Proto-Iranian reconstruction.

**Cognates or sources:** No cognates are listed in this entry. The document notes that for the meaning of "complaint," the term was "Borrowed from Arabic شَكْوَة (šakwa)," but this represents a different etymology and sense than the primary "glory, majesty" meaning.

The entry indicates that the primary sense derives from Middle Persian with meanings encompassing "dignity, majesty, fear," but etymological information beyond the Middle Persian stage is not included in this dictionary source.
```


## [2026-09-06T20:40:27.076Z] TOOL CALL #52: WebSearch

```json
{
 "query": "Wiktionary Reconstruction Proto-Indo-European ḱewh₁- to perceive kavi akouein",
 "allowed_domains": [
  "en.wiktionary.org"
 ]
}
```


## [2026-09-06T20:40:28.024Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/acoustic",
 "prompt": "Give the full etymology of acoustic, and any note on French acoustique and Greek akouein and the PIE root."
}
```


### [2026-09-06T20:40:35.593Z] TOOL RESULT

```
# Etymology of Acoustic

**Origin and Development:**
The word "acoustic" dates to circa 1600, meaning "pertaining to hearing or sound." It derives from French *acoustique*, which came from the Latinized form of Greek *akoustikos*.

**Greek Foundation:**
Greek *akoustikos* means "pertaining to hearing," stemming from *akoustos* (heard, audible). This verbal adjective comes from *akouein*, "to hear," which likely originated from "a copulative prefix a- plus *koein* 'to mark, perceive, hear.'"

**Proto-Indo-European Root:**
The ultimate source is the PIE root *\*kous-*, meaning "to hear." This same root is "also the presumed source of English hear," creating a direct etymological connection between these two words.

**Later Developments:**
The meaning expanded in 1924 to reference materials designed to dampen sound. By 1932, it applied to mechanically reproduced sound (gramophones), and "acoustic guitar" (distinguishing it from electric versions) appeared by 1958.
```


### [2026-09-06T20:40:35.649Z] TOOL RESULT

```
Web search results for query: "Wiktionary Reconstruction Proto-Indo-European ḱewh₁- to perceive kavi akouein"

Links: [{"title":"Reconstruction:Proto-Italic/kaweō - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Italic/kaw%C4%93%C5%8D"},{"title":"Reconstruction:Proto-Indo-European/ḱewh₁- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1ewh%E2%82%81-"},{"title":"κῦδος - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%CE%BA%E1%BF%A6%CE%B4%CE%BF%CF%82"},{"title":"Reconstruction:Proto-Indo-European/(s)kewH- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewH-"},{"title":"Reconstruction:Proto-Indo-European/(s)kewh₁- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewh%E2%82%81-"},{"title":"Reconstruction:Proto-Indo-European/kʷyeh₁- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7yeh%E2%82%81-"},{"title":"Reconstruction talk:Proto-Indo-European/ḱewh₁- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction_talk:Proto-Indo-European/%E1%B8%B1ewh%E2%82%81-"},{"title":"Reconstruction:Proto-Indo-European/kʷeys- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7eys-"},{"title":"Reconstruction:Proto-Indo-European/kʷey- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7ey-"},{"title":"Reconstruction:Proto-Indo-European/kew(H)- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%C5%AB-"}]

Based on the search results, I found relevant information about the Proto-Indo-European root you're asking about:

The Proto-Indo-European root *(s)kewh₁- means "to perceive". 

This root is related to several descendant words across different languages, including Sanskrit कवि (kaví, "wise, poet, seer, sage"), Greek κοέω (koéō), and Latin caveō. The search results indicate these words all derive from the same Proto-Indo-European etymological source related to perceiving and attention.

Regarding "akouein" (Ancient Greek ἀκούειν, "to hear"), the search results don't establish a direct connection to this root ḱewh₁-, though both relate to perception more broadly. The Wiktionary reconstruction page for *(s)kewh₁- focuses on the Sanskrit and Greek cognates mentioned above rather than connecting it to the root that would underlie akouein.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T20:40:41.197Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewh%E2%82%81-",
 "prompt": "Give the root's meaning, its reconstruction notes, and the full list of descendants (Indo-Iranian kavi, Greek koeo/kudos/akouein, Latin caveo, Germanic hausjan/skawwon, Balto-Slavic)."
}
```


## [2026-09-06T20:40:42.582Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%E1%BF%A6%CE%B4%CE%BF%CF%82",
 "prompt": "Give the etymology of Ancient Greek κῦδος 'glory' — PIE root, cognates, and any dispute."
}
```


### [2026-09-06T20:40:47.269Z] TOOL RESULT

```
# Proto-Indo-European Root *(s)kewh₁-

**Meaning:** The root signifies "to perceive" and "to observe," with related synonyms including *kʷey-, *sent-, and *h₂ew-.

**Reconstruction Notes:** This is a reconstructed Proto-Indo-European root marked with an asterisk (*) because it's not directly attested but "hypothesized to have existed based on comparative evidence." The root exhibits s-mobility, appearing both with and without an initial s-.

**Major Descendants across Language Families:**

- **Indo-Iranian:** Sanskrit ākuváte ("to intend")
- **Greek:** κῦδος (kudos) and related compounds
- **Latin:** caveo (to beware)
- **Germanic:** Proto-Germanic *skawwōną and *skawaz
- **Balto-Slavic:** Proto-Slavic čuti and čuvati; Lithuanian kavoti

The root manifests through various formations including s-aorist, thematic presents, iteratives, and nominal derivatives across these ancient language families, illustrating how a single reconstructed root diversified into cognate terms with related semantic ranges.
```


### [2026-09-06T20:40:48.461Z] TOOL RESULT

```
# Etymology of Ancient Greek κῦδος

**Proposed PIE Root:** The word is assumed to derive from Proto-Indo-European "**(s)kewh₁-**" meaning "to perceive, pay attention."

**Cognates include:**
- Ancient Greek κοέω (koéō)
- Latin caveō
- Sanskrit कवि (kaví, "wise, poet, seer")
- Persian کی (kay, "poet-king")
- Lithuanian kavoti ("safeguard, tend")
- Polish cześć ("glory") and cud ("miracle")
- Old East Slavic кудесникъ (kudesnikŭ, "wizard")

**Scholarly Dispute:** Linguist Robert Beekes rejects the above etymology. He instead proposes that both κῦδος and Proto-Slavic "*čudo*" ("miracle") stem from an alternative Proto-Indo-European root "**kewd-s-**" meaning "miraculous power."
```


## [2026-09-06T20:40:54.714Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%DB%8C",
 "prompt": "Persian کی — give all etymology sections, especially the one meaning 'king, Kayanian title' (Middle Persian, Avestan kauui, PIE root)."
}
```


## [2026-09-06T20:40:54.987Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/kudos",
 "prompt": "Etymology of kudos: Greek kudos, PIE root, date of entry into English."
}
```


### [2026-09-06T20:41:01.714Z] TOOL RESULT

```
# Persian کی (kī) - Etymology Overview

## Primary Etymology (King/Kayanian Title)

The noun meaning "king" derives from **Middle Persian** via a complex linguistic pathway. The entry states it was "Inherited from Middle Persian" and ultimately "borrowed from Avestan."

The Avestan root is **𐬐𐬀𐬎𐬎𐬌 (kauui)**, defined as "poet, bard; vision-poet, Mazdean sacrificer." This traces back through:

- **Proto-Iranian**: *káwHiš
- **Proto-Indo-Iranian**: *káwHiš  
- **Proto-Indo-European**: *(s)kewh₁-

## Mythological Significance

In Iranian mythology, کی refers to "the title of a number of legendary kings of Iran, belonging to the mythical Kayanian dynasty." The Wiktionary entry notes an important historical detail: "The visionary poets of the Avesta were mistakenly interpreted as ancient kings by the Sasanian Zoroastrian priests."

## Related Forms

Derived terms include کی‌قباد (Key-Qobad), کی‌کاووس (Key-Kavus), and کی‌خسرو (Key-Khosrow), representing major figures in Persian legendary history.
```


### [2026-09-06T20:41:07.354Z] TOOL RESULT

```
# Etymology of Kudos

**Origin:** The word kudos comes from Greek *kydos*, meaning "glory, fame," particularly in battle contexts. It appears frequently in ancient Greek epic poetry like the Iliad and Odyssey.

**Literal Meaning:** The Greek term literally means "that which is heard of," suggesting its connection to reputation and renown.

**Proto-Indo-European Root:** Kudos traces back to the PIE root *keu-, which means "to see, observe, perceive."

**Entry into English:** The word entered English around 1799, initially through university slang, meaning "fame, renown, glory."

**Linguistic Note:** A common misconception arose because English speakers mistook the final "-s" in this Greek singular noun for a plural suffix, leading to the creation of the singular form "kudo" by 1936. As the source notes, this represents a "barbarous back-formation" that doesn't align with the word's actual grammatical structure.
```


## [2026-09-06T20:41:15.302Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/kayanian-i-the-word-kavi/",
 "prompt": "Summarise: origin and meaning of the word kavi/kay, its Avestan and Middle Persian forms, its Indo-Iranian background, and the Sogdian/Parthian 'giant' sense."
}
```


## [2026-09-06T20:41:16.718Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D9%88%D9%88%D8%B3",
 "prompt": "Persian کاووس (Kāvus) — give etymology: Middle Persian, Avestan kauui usan, meaning."
}
```


### [2026-09-06T20:41:16.733Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T20:41:18.543Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T20:41:22.753Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%DB%8C%DA%A9%D8%A7%D9%88%D9%88%D8%B3",
 "prompt": "Persian کیکاووس / Kay Kāvus — etymology, Middle Persian Kay Us, Avestan Kauui Usan."
}
```


## [2026-09-06T20:41:23.189Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/caution",
 "prompt": "Etymology of caution and caveat and precaution: Latin cavere, PIE root."
}
```


### [2026-09-06T20:41:24.798Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T20:41:30.206Z] TOOL RESULT

```
# Etymology of Caution

The word "caution" originates from Old French *caution*, meaning "security, surety," which derives from Latin *cautionem*. This Latin term comes from *cavere*, "to be on one's guard," tracing back to the PIE root *keu- meaning "to see, observe, perceive."

## Semantic Evolution

Originally (c. 1300), caution referred to "bail, guarantee, pledge." The sense of "prudence in regard to danger" emerged later around the 1650s. By c. 1600, it acquired the meaning of "word of warning, monitory advice."

## Related Terms

The verb form emerged in the 1640s meaning "warn, exhort to take heed." Connected words include *cautious* (1640s, from caution + -ous) and *cautionary* (1590s, from caution + -ary), both conveying careful attention to potential danger.

This etymological family reflects a progression from the concrete legal sense of providing security to the more abstract modern understanding of prudent vigilance.
```


## [2026-09-06T20:41:34.382Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/show",
 "prompt": "Etymology of show (verb): Old English sceawian, Proto-Germanic *skauwojanan, PIE root, and the connection to hear/caution."
}
```


## [2026-09-06T20:41:35.536Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/hear",
 "prompt": "Etymology of hear: Old English hieran, Proto-Germanic *hauzjan, Gothic hausjan, PIE root *kous-."
}
```


### [2026-09-06T20:41:40.739Z] TOOL RESULT

```
# Etymology of "Show"

The verb "show" traces back through multiple language layers. It originates from Middle English *sheuen*, derived from Old English *sceawian*, meaning "to look at, see, gaze, behold, observe."

The word's ancestry extends through Proto-Germanic *skauwojanan* and ultimately to the Indo-European root *skou-, a variant of *keu-, both signifying "to see, observe, perceive."

## Semantic Evolution

Interestingly, the meaning shifted around 1200. The original sense of "to look at" evolved into "let be seen; put in sight, make known." As the entry notes, this causative meaning "seems to be unique to English" and "displaced the older meaning" within a century. By 1300, a new sense emerged: "explain, make clear."

## Notable Details

The spelling *shew* (rhyming with "view") remained popular through the 18th century but is now obsolete. The horse-racing sense meaning "finish third or in the top three" appears by 1903, possibly borrowing from earlier card-playing terminology.
```


### [2026-09-06T20:41:42.046Z] TOOL RESULT

```
# Etymology of "Hear"

The word "hear" originates from Old English *hieran* (West Saxon) and *heran* (Anglian), tracing back through Proto-Germanic *hausejanan* to the Proto-Indo-European root *kous-*, meaning "to hear."

## Key Historical Points

**Original Meanings:** Beyond simple auditory perception, the Old English verb encompassed "listen to," "obey," "follow," and "judge."

**Linguistic Relatives:** The word shares cognates across Germanic languages, including German *hören*, Dutch *horen*, and Old Norse *heyra*.

**Spelling Evolution:** "The distinction between hear and here developed between 1200-1550," establishing the modern differentiation between the two homonyms.

**Semantic Development:** The meaning "be told, learn by report" emerged in the early 14th century, expanding the verb's application beyond direct perception.

## Notable Expressions

The exclamation "Hear, hear!" originally functioned as an imperative command to direct attention to speakers' words, dating to the 1680s. It later evolved into a general expression of approval, as commonly heard today.
```


## [2026-09-06T20:41:49.176Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%DB%8C%D8%A7/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for کیا and any origin tag, plus the Dehkhoda entry summary."
}
```


## [2026-09-06T20:41:51.058Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A2%DA%A9%D9%88%D8%B3%D8%AA%DB%8C%DA%A9/",
 "prompt": "Is آکوستیک listed? Give the definition and any note of its French origin (فر.) in فرهنگ معین or other dictionaries."
}
```


### [2026-09-06T20:41:53.670Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T20:41:54.868Z] TOOL RESULT

```
# کیا - Farhang-e Mo'in Entry

## Mo'in Dictionary Definition

According to Farhang-e Mo'in, کیا is defined as:

1. "بزرگ، سرور" (great one, master)
2. "پادشاه، حاکم" (king, ruler)
3. "مرزبان، پهلوان" (border chief, champion)

## Dehkhoda Entry Summary

The Dehkhoda lexicon indicates that کیا fundamentally means "a great/mighty king." It notes the term historically applied to governors and chiefs, particularly in regions like Tabaristan and Gilan. Over time, the designation expanded to encompass various administrators and even scholars. The entry documents that "مرزبان" (border administrator) and "پهلوان" (champion) also served as meanings, while in figurative usage it denoted "master" or "dignitary."

## Origin

The word traces back to Middle Persian heritage, derived from ancient Iranian linguistic roots connected to royalty and sovereignty.
```


## [2026-09-06T20:42:03.824Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%95%E0%A4%B5%E0%A4%BF",
 "prompt": "Sanskrit कवि (kavi) — etymology and meanings; Proto-Indo-Iranian and PIE root; Avestan cognate."
}
```


## [2026-09-06T20:42:05.289Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://iranicaonline.org/articles/kayanian-i",
 "prompt": "Summarise the article on the word kavi/kay: Avestan kauui, meaning 'poet-priest'/'prince', Middle Persian kay, Kayanian dynasty, and Sogdian/Parthian 'giant'."
}
```


### [2026-09-06T20:42:07.589Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T20:42:10.812Z] TOOL RESULT

```
# कवि (Kavi) - Word Analysis

**Primary Meaning:** The word कवि (kavi) means "poet" across Hindi, Marathi, and Pali. In Sanskrit, it carries broader significance.

**Sanskrit Definitions:** In Sanskrit, कवि functions as both noun and adjective. As a noun, it refers to a "wise man, sage, seer, prophet," and also "singer, bard, poet." The adjective form means "gifted with insight, intelligent, knowing, wise, skillful."

**Etymology:** The term originates from Proto-Indo-Iranian *káwHiš* ("seer, saint, poet"), ultimately deriving from Proto-Indo-European *(s)kewh₁-* meaning "to observe, to perceive."

**Cognates:** Related words appear across Indo-European languages, including Avestan kauui, Ancient Greek κῦδος (kûdos), Latin caveō, and English "show."

**Historical Usage:** An example from the Rigveda (c. 1500-1000 BCE) demonstrates the term's ancient application, where it describes wise individuals who "burst the mountain" and worked "amid the sages."

**Modern Descendants:** The word has influenced numerous languages including Bengali, Hindi, Kannada, Tamil, Telugu, and Thai through learned borrowing.
```


## [2026-09-06T20:42:22.924Z] TOOL CALL #68: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D8%B4%DA%A9%D9%88%D9%87' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewh%E2%82%81-' \\\n 'https://en.wiktionary.org/wiki/%CE%BA%E1%BF%A6%CE%B4%CE%BF%CF%82' \\\n 'https://en.wiktionary.org/wiki/%DA%A9%DB%8C' \\\n 'https://en.wiktionary.org/wiki/%E0%A4%95%E0%A4%B5%E0%A4%BF' \\\n 'https://www.etymonline.com/word/acoustic' \\\n 'https://www.etymonline.com/word/kudos' \\\n 'https://www.etymonline.com/word/caution' \\\n 'https://www.etymonline.com/word/show' \\\n 'https://www.etymonline.com/word/hear' \\\n 'https://abadis.ir/fatofa/%DA%A9%DB%8C%D8%A7/' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 263, root Keu 3 (PIE *(s)kewh1- watch/hear): kavi/kay/Kavus, shokuh, kudos, acoustic, caution, hear/show' 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T20:42:29.610Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/eb0f5639e691b598.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7c7ac4ba18b81630.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1e59e779943212db.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d6937d5cb7398b19.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/625ec22e9aeee6f5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/810be2ec14148402.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b91e538cb48315f4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/30fbfe560cc70547.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e2e0f3bc84eb0124.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/196f3ecce8cdbbbe.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c1e50bee8ccb5cdd.txt
```


## [2026-09-06T20:42:36.306Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC Kouos/Keudos ===\"; grep -n -o \"Keudos.\\{0,250\\}\\|Kouos.\\{0,250\\}\\|Kous-.\\{0,250\\}\\|Skeuo.\\{0,250\\}\" IEC.txt | head -8; echo \"=== SYN hear ===\"; grep -n -o \"15.41 HEAR.\\{0,600\\}\" SYN.txt | head -2"
}
```


## [2026-09-06T20:42:37.407Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSF kayan/kavus ===\"; grep -n \"کیان\\|کاووس\\|کاوس\" FSF_pages.txt | head -10; echo \"=== ARY latin index kavi ===\"; grep -n -i \"KAVI\\|SKEU\\|KEU\" incoming/ARY/ARY_latin_index_pages.txt | head -15"
}
```


### [2026-09-06T20:42:38.453Z] TOOL RESULT

```
=== IEC Kouos/Keudos ===
8585:Kouos, Kauos), à
8601:Kouos, Kauos), à ‘hollow, hole’. WP I,
9081:Kouos, variant of Kouos, q. v.
=== SYN hear ===
26181:15.41 HEAR
```


### [2026-09-06T20:42:38.511Z] TOOL RESULT

```
=== FSF kayan/kavus ===
249: ‫بر شیر بگشای و چنگ کیان‬                    ‫‏‪ ٩‬بدو گفت بر تاز و برکش ميان‬
511:      ‫که هرکو به خون کیان دست آخت‬                                                   ‫آبکیر‬
975:‫ولی کاوس سبکسرانه رستم راسرزنش‬                      ‫ه‌سخاتند‪ .‬هر‬       ‫دان‬
1685:                ‫همه بوم شد زیر نعل اندرون‬          ‫گزند از آتش می‌گذرد‪ .‬کاوس به سوادبه‬
1773:              ‫که فر کیان دارد و چنگ شیر‬                       ‫از منوچهری (دیوالن» ‪:)۲۳‬‬
1870: ‫نه رسم کیان بد نه آیین پیش‬                           ‫برآهیخت جنگی نهنگ از نیام‬
1919:               ‫بینداخت رستم کیانی کمند‬                ‫انش خون‬
2014:‫مرانام بر تاج و تخت کیان‬                   ‫)‪(۲-4۶-۷11‬‬
2583:‫کسی راکهبد نیکخواه کیان‬                         ‫بلند و به یکسو ز انبوه بود‬
3101:             ‫چو کاوس رادیددستان سام‬                ‫(‪)۵-۶۸۲-۱۵۸‬‬
=== ARY latin index kavi ===
10158:ala SKEU- | KSEUs gly! y stn Gat, aly jt) Cai cal lan jly BUCK ~¥
11098:SCHOUWEN (DUTCH) gute KAVIS SANSKRIT) x Suis
12129:irr sebi iby KUKAVIKA oy
```


## [2026-09-06T20:42:43.323Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26181,26200p' SYN.txt | head -30; echo \"=== page ===\"; awk 'NR<=26181' SYN.txt | grep -c $'\\f'"
}
```


## [2026-09-06T20:42:43.746Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11090,11105p' incoming/ARY/ARY_latin_index_pages.txt; awk 'NR<=11098' incoming/ARY/ARY_latin_index_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -1"
}
```


### [2026-09-06T20:42:45.014Z] TOOL RESULT

```
15.41 HEAR
Gtk. dxobw (KAbw)
NG = dxobw, yporxd Lat. audire
It. sentire, udire I, entendre
Sp. ofr
Rum. auzi
Ir. cluinim
Nir. cluinim, cloisim
W. — clywed Br. klevout ei hausjan N  hgyra (heyra Dan. hére ura) Sv. héra OE hgran ME here as hear .  hooren ic ho(r)ran UG how ia héren Tan sirdeea hs; dzirdet Sr, piles Poe Slubati R slyszeé i eee
sru-
‘plear-eyed’, and with rr ‘damp earth, dung’. 9,518. Falk-Torp 1206.
m ’, (acid, pungent’, hence also ie a Gigre (above, 1). NED
Stas (Lett. rugts ‘bitter’) : ferment’, é-rugere,
épeb'youar fr. ‘fermented’. Walde-P. 9367, Exnout-M. 874 f. ‘Lett. skabs (Lith. dial. skobas 1ds)ae Lett. skabrs, Lith. skabus ‘sharp’, skabéte ‘out, hew, shoot forth (branches)’, Lat. scabere ‘Scrape, scratch’, etc. Walde-P. 9563, Miihl.-Endz. 3.878 f.
SENSE PERCEPTION
Digitized by Arya Samaj Foundation Chennai and eGangotri
1035
Lett. skan’§ : Lith. skanus ‘good tast- ing’, skonis ‘taste’ (15.34)? Endz. 3.879. Leskien, Ablaut 373.
6. ChSl. kyslii, etce., general Slavic, fr. the root of ChSI. -kysnati, Russ.
Miuhl.-
=== page ===
1111
```


### [2026-09-06T20:42:46.906Z] TOOL RESULT

```
ONIONS: (sur sat = Poko. =—SSSC=~S~S~«é
JAMINDAROY: , _\fSs {BREAK) 194 DELAMARRE:
ot . * ° (COUPER, SEARER) 281
. lethal
; PS ab 9 S95 K2 Shir ES 05!) ot! al
BSF CASA Daa Seas gad SOIL) 22 0319 atl pF
SKUE (DANISH) Sail SHKOH PAHLAVI) 5.94,
SKYGNE NORWEGIAN) «5335 SHKULA AFGHAN) (5-4) gli!
SCHOUWEN (DUTCH) gute KAVIS SANSKRIT) x Suis
CHUCHATU — (gow}(RUSSIAN) 5-9, ARMENIAN) ga)
CHICH CZECH) Soy CHCANEM, SHUKEGH
| CHUHAM ASLOVAR) 51 jlo GREEK) gli
' OLD PRUSSIAN) oS +9. THYOSK60S, -SKOWOS, KOEO
| AU. SCAUDITWEI CAVERE,COVERE = (LATIN) gi
USKAWS GOTHIC) Ss
‘REFERENCES ecnthag (OLD SCANDINAVIAN) «4S 5h!
[pdf page 381]
```


## [2026-09-06T20:42:57.078Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"hausjan.\\{0,700\\}\" SYN.txt | head -4"
}
```


## [2026-09-06T20:42:57.914Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"شکوه\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-06T20:42:58.613Z] TOOL RESULT

```
5902:hausjan ‘hear’, OF scéawian ‘look at’, etc. (15.41, 15.52). Henry 243. Win- disch ap. Ernault, Dict. étym. 377. Less probably Pedersen 2.53.
7009:hausjan, etc. ‘hear’, etc, IE *keu-. Walde-P. 1.368 ff. Berneke, 162.
25949:hausjan ‘hear’, etc. (15.41). Berneker 162f. Walde-P. 1.369.
26189:hausjan N  hgyra (heyra Dan. hére ura) Sv. héra OE hgran ME here as hear .  hooren ic ho(r)ran UG how ia héren Tan sirdeea hs; dzirdet Sr, piles Poe Slubati R slyszeé i eee
```


### [2026-09-06T20:42:58.684Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T20:43:05.524Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7003,7012p' SYN.txt; echo \"=== leaf ===\"; awk 'NR<=7009' SYN.txt | grep -c $'\\f'; echo \"=== 25949 ctx ===\"; sed -n '25944,25952p' SYN.txt; awk 'NR<=25949' SYN.txt | grep -c $'\\f'"
}
```


### [2026-09-06T20:43:07.415Z] TOOL RESULT

```
Phrases with the noun, like It. tirar pelt, Rum. da bdsini, etc., are omitted, though these are more or less popular in all Janguages and in some are in more common use than the verbs listed.
1. TE *perd-. Walde-P. 2.49.
Grk. répdouat, aor. érapSov (sb. ropih, hence NG zropéitw); W. rhechain (denom. of rhech fr. *prd-ka-); ON freta, Dan. Sjerte, Sw. fjarta, OE feortan, ME ferte, NE fart, OHG ferzan, MHG verzen, late MHG varzen, and denom. vurzen, NHG Jarzen, furzen; Lith. persti, Lett. pirst, SCr. prditi, Boh. prdéti, Pol. pierdzieé,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
SELECTED INDO-EUROPEAN SYNONYMS
mundrus ‘lively, arrogant’, OHG mun- tar ‘zealous, lively’ (NHG munter), eto, Walde-P. 2.270 £.
8. Pol. czuwwaé (only ‘be awake’). ChSI. éutz ‘feel, notice’, Russ. Cujat! ‘ex. perience, feel’, Slov. éuti ‘hear, wake’ etc., Grk. xoéw ‘notice’, Lat. cavére Gai heed’, Goth. hausjan, etc. ‘hear’, etc, IE *keu-. Walde-P. 1.368 ff. Berneke, 162.
Russ. prosnut'sja (refl.), apparently new formation after usnut’ ‘fall asleep’, Ch&l. ustinatz, etc. id. : Russ. son, Ch], stint ‘sleep’, etc. (4.62).
Russ. perdet’; Skt. prd- (Dhatup.; now quotable pardate), Av. porad- (8 pl. paradan); Alb. pjerth (sb. pordhé fr. NG zropé7).
2. IE *pezd-, *bzd-, of imitative orig., but prob. through ‘blow’ (as in words pointing to IE *pes- ‘blow’). Walde-P. 2.68 f. Ernout-M. 748. Briickner 54.
=== leaf ===
309
=== 25949 ctx ===
» Lett. juteklis, prob. : Skt. api-
SENSE PERCEPTION
Digitized by Arya Samaj Foundation Chennai and eGangotri
1021
vat-, Av. aipi-vat- ‘understand’. Walde- P. 1.216. Meillet, BSL 23.77.
6. ChSl. poéuti, perfect. of éuli ‘rec- ognize, notice’, SCr. uti ‘hear’, Boh. iti ‘perceive, notice, smell’, Pol. czué ‘perceive, smell’, with sbs. ChSl. éuvisivo, Russ. éuvstvo (SCr. éuvstvo, old in this sense), whence Russ. ¢uvstvovat’ ‘feel, perceive’ : Grk. xoé ‘notice’, Lat. ca- vere ‘be on one’s guard, heed’, Grk. axobw, Goth. hausjan ‘hear’, etc. (15.41). Berneker 162f. Walde-P. 1.369.
SCr. osjetiti, with sb. osjet, cf. do- sjecati ‘take notice of’, epds. of sjetity se, late ChSI. sétiti se ‘remember’ (17.31).
SCr. éutjeti (as ‘perceive’ dial.), Russ. o-Séutit’, with sb. SCr. éut, éutilo : ChSI. Stutiti ‘feel’, etym.? Walde-P. 1.369. Osten-Sacken, IF 33.197. Miklosich 357.
Boh. smysl, Pol. zmyst (smyst), also ‘meaning, mind’ = SCr. smisao, Russ. smysl ‘meaning’, cpd. of ChSl. myslt ‘thought’, etc. Miklosich 208. Briick- ner 350.
1097
```


## [2026-09-06T20:43:15.885Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"Hear\\..\\{0,300\\}\\|Show\\..\\{0,300\\}\\|Acoustic\\..\\{0,300\\}\\|Caution\\..\\{0,300\\}\\|Caveat\\..\\{0,300\\}\" SKT.txt | head -10"
}
```


### [2026-09-06T20:43:17.531Z] TOOL RESULT

```
3145:Caveat.
14700:Caveat.
16607:Show.
17089:Show. Sheep.  (E.)    A.  S.  ued/,  scip;   pi.  the mc.  +  Du.  sihaap,  G.  uhaf.     Cf  Polish a    wether,    from    Charch   Slaronic *J*tli,  to  castrate.
17109:Show.
```


## [2026-09-06T20:43:20.695Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17105,17120p' SKT.txt; echo \"=== hear ===\"; grep -n -o \"Hear,.\\{0,350\\}\" SKT.txt | head -4; echo \"=== acoustic ===\"; sed -n '348,356p' SKT.txt; echo \"=== caution ===\"; sed -n '3140,3150p' SKT.txt"
}
```


### [2026-09-06T20:43:22.708Z] TOOL RESULT

```
Sherd;  see  Shear.
Sheriff,  see  Shire.
Sheriy,  (Span.-L.)    Formerly/^
—  Span.    Xtrts,   a    town    in    Sf>ain,   n Cadiz.  — L»  drsaris,  gen.  case   of proper  name  (Dozy).
Shew ;  see  Show.
Shibboleth,  a  test-word.  (Heb.)    B shibb6U(k^  an  ear  of  com,  also  a  river; Judges,  xii.  6.
Shide,    a    thin    piece    of   board; Shed  ( i).
Shield.  (E.)  A.  S.  sdUi,  sttU,  +  1 sckiUt  IceL  skJBldr,  Dan.  skiiild^  Sw skiiid,  Golh.  skildus,  G-  sehtld.
shelter.  (E.)  A  curious  corruption M.  £.  jkeldtrumtt  a  body  of  guards troops,  a  squadron ;  frequently  spelt  skeUr skelirun;  it  came  to  mean  a  guard  or  p tection  of  any  kind,  perhap^  throi confuMon  with  sktal,  q.  v.  —  A.  S.  sn tnima,  lit  *  shield-troop,*  a  guard. —A. scild,  shield ;  trumOy  a  band  of  men.
Shieling ;  see  Shoal.
Shift.  (E.)  M.  E  sckiJiefL,  to  divi change,  shift,  remove;  orig.  'to  divi( A.  S.  sci/tan,  to  divide.  +  ^"1.  ski^ (for  skifta),  to  diride.  part,  shift,  choof Swcd.  skifta,  Dan.  skiftt,  the  same.  All to  Icel.  ski/a,  to  cut  into  slices,  skifa slice,  prov.  E.  skiv*^  a  slice,  sheav€t wheel  of  a  pulley.     See  Shiver  (3).
Shilling.  (E.)  A.  S.  sciiiiHg.  +  I scheiling;  Icel.  skiHingri  Dan.  Sw tki/Un^i  Goth,  skiili^  (for  skUh'ngi G.  schilling,  p.  The  sulTix  -ling  is double  diminutive;  the  base  is  SKLL, divide;  see  Skill.  Reason  for  the  na uncertain;  but  cf.  Swed,  lAtVjcmytU^  D ikiiUmynt^  &ixui\\  (^Ka^,^nw\xnQ<cw)
43a
SHIMMER,
Shimmer,  to  glimmer.  (E.)  A.  S. ui/MT-ian,  fret^uent.  loim  of  sc/mOM.ttimioM, to  shine,  allied  to  sciftaM,  to  shine ;  tee Bhine.  4*  J^u-  tcMtmertn ;  Swed.  skimm ; G.  schimmem.  Cf.  O.  H.  G.  scirufi,  ft brieht  light^  Icel.  skimi,  a  gleam.
Shin.  (I£.)  A.  S.  scina;  whence  scin- btin,  shin-bone.  +  Du.  tchten  ;  G.  schime^ also  a  splint ;  Swed.  iktn-btn,  Dao.  ikinne- Uen,  sliin-bonc.  Orig.  sense  perhaps  'thin slice/  from  the  sharp  edge  in  front  See Skin.
=== hear ===
=== acoustic ===
Aconite;  &ee  Aold. Accra.  (E)     M.E  acorm,  A.S.  trry fruit ;    properly  '  fruit   of  the   field,'    fro A.  S.  Avr,  A  field ;  sec  Aore.-4-  IccL  oka Dan  <^vfM,  Goth,  o^t/^sn,  (tvuVi  (tow  (tx\.
i
kin  ^^
ACOUSTIC.
ADVANCE.
air,  Dan.  <^^,  Gotb.  aJkrs,  a  field.    %  Not from  aai. Aoouatlo.  (Gk.)    Gk.  6Movmtii6$,  relat- ing to  heanng  (or  sound).  —  Gk.  djmvur, to  hear. Acquaint.  (F,-L.)    M.E.  tKipte/nfen, eoriier  tuohtftn.^O.  F.  araiHler,  {uointier, to  acquaint  with.  *  Low  L.  A/tV^iVa/r,  to. mnkc  known  (Brachct).  —  L.  4ui,  to;  and fognifan*.   formed  from  (Qgnttus,  pp.   of €i>^&s(€rt^    to    know.      See    oogniMUDoe, quaint.  i.v.  Noble. AoquieBce ;  sec  Quiet. Acquire ;  sec  Query. Acqiut :  5c«  Quiet. Aore.  (E.)     M.E.  aktr.    A.S,  <««•.+ I      Du.  aiJtert  lotX.aJkr,  SwoihAker,  Dan.  ager, ^^Both.  aJ^n,  G.  acker^  L,  agxr^   Gk.  ^ypi*, ^^Bkt  ajra.    The  orig,  sense  was  cither  *  pas> ^^■ue/  or  'hunting-ground.*  (^AG.)    Dor. ^^^or-Ht  q.v.
^■Aorid,  Acrimony;  see  AoW. Acrobat^  Acropolis  ;  see  Acid. Across.  (K.  and  Scaiitl.)     For  on  cfws; lee  A-  i2)'and-^OBS. ,        Acrostic :  see  Aaid. Act;  fteeAffent. Acumen,  Acute :  see  Aoid. A.d-,  prtfix.  (L.)  L.  Of/,  lu,  cognate  with E  At.     ^  L.  aU  becomes  or-  before  t ;  a/- bef.  /;    (xy-   bcf.  ^;    aA    bef. /;    a«-  bef. H  ;  a/-  bef.  / ;  ar-  bef.  r;  *i-  bci".  / ;  a/- bef./. '         Adn^o,  a  saying.    (F.^L.)      F.  ada^ I       *L.  Oiia^ium.^V..  ad\  and  agium,  a  say- '       ing;  cf.au>.  1  iav.   (V  AGII.)
Adamant  (F.  -  L.  -  Gk.)  M.  E. ^^miatiuiimtt  a  diamond,  a  magnet.  —  O.  F. ^H|tf!a//;aM/.  —  L.  aJamanta,  ace.  of  otiamas.  — ^^Bk.  d^ftat,  a  very  hanl  metal  or  slone  ;  lit. ^^nnconquemhle.'  — Gk.  d-  (  =  E.  ««  );  and hafuiuv.  \o  com)uer.  lame;  see  Tama, diamond.  tF.-L.-(;k.>  M.E. ///a- «/.  — O.  F.  diamante  coiruplion  o{  ada- nt;    SO   also    Ital.   Span.  diartianUf  G.
ant. d&pt ;  see  Apt.
=== caution ===
recusant,  opposing  an  opinion   (P. L.)     F.    ri(usa*it,  'rejecting.*    Cot-i  ^ pi.    of  Hcuser.  —  L.    recuiart,   to    i oppose  a  cause  or  opinion.  — L.  rr-, from ;  and  causa.
ruse,  a  trick.  (F.  — L.)    F  ntse^  a —  F.  ruscr,  to  beguile;  contr.  from  O rciiscr,  to  rcfus<:,  recoil,  escape.  do4^ L.  rctiisart,  to  nelusc ;  sec  above.
Causeway ;  kc  Calx.
Caustic.  (L.  — Gk.)  L.  caustina.^ icavoriK6s,  burning.  —  Gk.  nufif  (ful.  mh to  bum.
cautariao.   (F.  •  Low  U  —  Gk^ caittcriser. ^Lovf  L.  cautcnaart.  to  scar Gk.  ifam^/KciftiK  to  sear  — Gk.  ♦nv^, a  branding-iiou.  — Gk   xttUw,  II holocaust.  (L.-Gk.)   L.  : Gca.  xxii.  8.  — Gk.  6KiiKavtrrQv,  .. burnt    whole;  ncut.  of  ^K.'.nnviTai,  Um whole. —  Gk.  t\o-f,  whole;  and  Kolt^w^ burn.
Caution :  see  Caveat.
Cavalier.  (F.-Iial.-L.)    F.  rarwld a  hur^eman.  — Ital.  cavaliere,  the  canK llal.  cavalh^  a  hor^e.  — L.  ace.  cabaHum, horse ;  nom.  cabalius.
oavaloada  tF. -ItaL— L.)  F. rdij!r.  — Ital.  razwi/ra/a.  atroop  of  horvema orig.  fcm.  of  pp.  of  cava/rare,  lo  rid<c Ital  cat'a//o.  a  horw;  as  above.
cavalry.  (F.-lial.-L.)  O.  F.  m9 ierie.  —  Ital,  ravaiUria,  cavalry,  m  I ca-faiurf,  a  knight ;  sec  CavaUsr.
chevalier.  \V.  -  L.)  K.  ekfwiUim hnrscman.— F,  cheni/,  a  bocM.*>L-  •« caiKil/umt  a  horse  (above).
CAVE.
```


## [2026-09-06T20:43:28.915Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14695,14712p' SKT.txt; echo \"=== HEAR ===\"; grep -n -o \"Hear\\b.\\{0,300\\}\" SKT.txt | head -6"
}
```


### [2026-09-06T20:43:30.883Z] TOOL RESULT

```
Prebend :  sec  Habit.
Precarious.    <L.)    U   prtcanta,  01 taincd  by  prayer  or  as  a  farour,  douM precarious.  — L  prtcari,  to  pray.  — 1. stem  q{ prtx,  a  prayer.  -4-  Skt.  pmei\ /frsi>en.  to  ask.     (VI'AKK.l
deprecate.    (L.)     From    pp,   of depraari^  lo  pray  against,  pray  to  re —  L.  iit.  away ;  pucari  vnbove).
imprecate,    il..)     From     \-^    "f imprecar-i.  to  call  down  upon  : L.  Jiw-  (i>(\  upon ;  prtcari  {&)'■
pray.  (F.-L.)    M.  E.  /rryw.-O, preier  (F.   /«Vr),  —  L.  prtcart   (aboMJ Der.  pray-cr,  M.  E.  prtiert,  O.  F, from   \..  pretaria    fein    Qi  pte<.'axiMS, see  Prooarious  (sbove).
Precaution ;  sec  Caveat.
Precede:  see  Code.
Precentor;  see  Cant  (1).
Precept;  see  Gapacioaa,
Precinot :  see  Cincttxre.
Precious.  (F.-L.)  O.  V.tftcitm  A pritieux).  —  I*,  pretiatui,  valuable.  •I pretium,  price,  value.  Allied  to P<ma  (i.e.  panux^"),  wages,  ri-i"- wip-t'vut,  I  sell  (VT'AR,  to  ^ appraise.  (F.-L.)  M.  i: value  — 0.  F.  apreiscr  (^:-!*-  - Roquefort).—©.  F,  a-,  pi  .iv. value,  from  pnis.  value,  pnce.  — 1.  <u.  * prrtium,  a  price.
appreciate,    (L)     From    pp    <i appretiart,   to    value  at  a  («ioe.— I-  ^ {aJ^  at;  prefiym,  n  price.
depreioiata.    (L.)      From    pp.   of  t tif.pretiart,  to   lower  the  price  01.  — L down .  pretium^  price.
praise.    (F,  -  1-.)    O,  F.  prtU» value,  merit  (hence,  tribute  to  roaitV-l' prctinm^  price,  value.     Der.  dij  fraist.
price.  (F.  -  1*)    M.  !■:    rn'.,  -  0  ? Pris.  by-form  of  O.  F.  /'  - .
prize  (2).  to  value M,  v.. pristn.^V - priser, !..  . O. F./rij,aprice,  value:  w-.  p'
Precipice ;  see  Capital  \i).
Preciso ;  sec  Ccatira.
=== HEAR ===
22136:Hear-;  see  Betro-.
```


## [2026-09-06T20:43:38.869Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kaHu\\|\\*kau\\b\\|kauH\" CHEUNG.txt | head -10; echo \"=== RCH kia ===\"; grep -n -o \"Kiyá.\\{0,150\\}\\|kiyán.\\{0,150\\}\" RCH.txt | head -5"
}
```


### [2026-09-06T20:43:40.475Z] TOOL RESULT

```
16369:k’üxt ‘to see’, ? Yi. kös-/kist ‘to search for’ (rather *kau£? ?) || (+ *pari-) Oss. L 
16517:*kaué ‘to bend, draw into, contract’ 
16680:*kauš! ‘to fight, struggle; to kill’ 
16737:0 The Iranian evidence for a root *kauš is confined to Sogd. and possibly Khot. / 
22328:semantically similar roots: *dauH and *skauH. 
22686:*skauH 347 
22712:*skauH ‘to poke, touch; to earmark, ? to cover’ 
22727:displayed by these forms, a connection with *skauH can hardly be doubted: *kauH 
55598:*Hrais, *said' (s.v.), *skauH 
55880:(s.v.), *skauH (s.v.), *tard 
=== RCH kia ===
```


## [2026-09-06T20:43:44.696Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22712,22740p' CHEUNG.txt"
}
```


### [2026-09-06T20:43:44.738Z] TOOL RESULT

```
*skauH ‘to poke, touch; to earmark, ? to cover’ 

*KHOTANESE: OKh. skau- (sko-, sku-), Khot. skauy- (sku-), Khot. *skav- (skü-/skv-) 
‘to touch, play an instrument’ || (+ *abi- ?) buskuta- ‘burst? © SGS: 134, 128 
*SOGDIAN: (+ *ni-) ? BSogd. nsk’w, CSogd. nysq’w, MSogd. nysk’w ‘to remove, 
bring out, take out’ 

Pres.: IND. 3pl. BSogd. nsk’wnt, OPT. 1pl. CSogd. nySq’wym, CSogd. nySqwym, IMPV. 25р. CSogd. 
nyšq `w; Impf.: IND. 3sg. MSogd. nyšq w, 3р1. CSogd. nysSq’wnt, Pret.: tr. 25р. CSogd. nysSqwyd ry, 3sg. 
CSogd. nysqwyd'rt; Fut.: IND. 1sg. CSogd. nysq’wmq’, CSogd. nySqwmq’ 

*CHORESMIAN: k’w- ‘to scratch, rub’; m/kw- ‘to pluck’ || (+ *pari-) prk’w- ‘to curry’ 
|| m/sksy- (pass./intr.) ‘to be split, slit’ || (+ *fra-) m/skwnd- (tr.) ‘to earmark’. ç The 
Chor. forms were considered to have an unclear etymology, cf. Samadi, Le: 99, 
despite the apparently precise Pamir correspondences. In view of the meanings 
displayed by these forms, a connection with *skauH can hardly be doubted: *kauH 
would then be the s-less variant. The sibilant may have been re-interpreted as prefix 
*us- and removed accordingly ? || Chor. m/Skwnd- ‘to earmark’ has a peculiar, 
probably secondarily arisen, -d-, cf. Sh. sikund ("with secondary -nd", EVS: 73b). 
c» Samadi: 99, 105, 153, 192, 194 

*NEIR: Oss. I. sk’,ynyn/sk’,yd, D. (&)sk’unun/(z)sk’ud ‘to vomit; to tear up; to 
destroy’, (old pass.) I. sk’,yjyn/sk’.yd, D. (&)sk’ujun/(z)sk’ud ‘to vomit; to be torn 
up, to be transferred, in transition, wither away, disappear’, I. sk’awyn/sk’awd, D. 
(z)skawun/(z)sk’awd ‘to pluck; to comb’, I. sqawyn/sqawd, D. (&)sgawun/ 
(z)sgawd (old caus.) ‘to peck; to chip; to pull at; to wipe (eyes)’, Pash. sköy- ‘to 
scrape, scratch, rub; [lex.] to shear’, ? Pash. skastol/skal-, skustal/skul- ‘to shear, 
clip’, Sh. sikünd ‘pitch-fork’, || Yi. &ü-/£üvd-, M. jüv-/juvd, ўйу-/ўйуа- ‘to pick’, Sh. 
cäw-t, Rosh. céw-t, Bart. Cäw-t/Eüd, Sariq. čew-/čid ‘to comb, scratch’, Ishk. kow-
```


## [2026-09-06T20:43:48.974Z] TOOL CALL #81: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T20:43:49.018Z] TOOL RESULT

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


## [2026-09-06T20:43:51.513Z] TOOL CALL #82: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T20:43:51.565Z] TOOL RESULT

```
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


## [2026-09-06T20:44:47.145Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && python3 - <<'EOF'\nimport json,glob\nfor f in sorted(glob.glob('page-2*.json'))[-8:]:\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e['nodes']:\n            if not n.get('words'):\n                print(f, n.get('id'), n.get('lang'), n.get('verdict'), '|', (n.get('derivation') or '')[:160])\nEOF"
}
```


### [2026-09-06T20:44:48.644Z] TOOL RESULT

```
page-256.json 2 Pahlavi confirmed | The empty pass-through box stands for Middle Persian sar 'head', written with the Aramaic ideogram LOYŠE (< Aram. rēšā) and phonetically sl. Avestan/Old Iranian
page-256.json 9 Middle Latin confirmed | The empty box stands for Medieval Latin carratus (also caratus), the form in which Arabic qīrāṭ entered western Europe — through the alchemical and assaying lit
page-256.json 10 French confirmed | The empty box stands for French carat, attested from the 14th century, taken from Italian carato (the Italian goldsmiths and bankers of Genoa, Venice and Floren
page-256.json 18 Different Languages confirmed | A collector box: Nourai uses 'Different Languages' for the several branches through which the root reached English independently of the Greek and Iranian lines 
page-258.json 6 French confirmed | An empty pass-through box: the French link between Latin carbō and Persian کربن is carbone, the element name coined by Lavoisier's commission in 1787 (Méthode d
page-258.json 12 French confirmed | Another empty pass-through box, and the only node on the page with no reference at all. The intended French link is céramique, attested from 1806 as an adjectiv
page-259.json 7 French confirmed | An empty pass-through box: the French stage through which the Latin cor-family reached English and (later) Persian. The relevant Old/Modern French forms are aco
```


## [2026-09-06T20:45:06.878Z] TOOL CALL #84: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg263.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/263.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-06T20:45:06.948Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T20:53:13.696Z] TOOL CALL #85: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-263.json",
 "content": "{\n  \"pdf_page\": 263,\n  \"book_page\": 233,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Keu 3, Kou, Skeu 3, Skou\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *(s)kewh₁- 'to perceive, observe, pay attention' (Pokorny 1. keu-, skeu-, lengthened kēu- p.587; Watkins keu-¹ / keuə-¹)\",\n      \"note\": \"Pokorny IEW p.587 heads the entry '1. keu-, skeu-, dehnstufig kēu- „worauf achten (beobachten, schauen)“, dann „hören, fühlen, merken“; schwere Basis keuə-; s-Erweiterung keu-s-; … d-Erweiterung keud- : kūd- in keudos : kūdos „Ruhm“' — so Nourai's four headword shapes are exactly the variants his source lists: Keu = keu-, Kou = the o-grade *kou- of *kouos (whence Gk. koéō, Lat. caveō), Skeu/Skou = the s-mobile variants (§'2. Mit anlautendem s-', p.588). Language label 'Indo-European' and gloss 'to watch, see, hear' both reproduce Pokorny faithfully. Modern handbooks write the root *(s)kewh₁- 'to perceive'. Two caveats the chart does not show: (a) Walde-Pokorny I 370 itself warns that the s-initial group is semantically restricted to seeing and that 'ihre Verwandtschaft mit qeu- „worauf achten, merken“ ganz fraglich' ist — i.e. Nourai's merging of Skeu with Keu is the traditional but not uncontested arrangement; (b) Watkins/AHD splits what Nourai unites into keu-¹ ('to perceive, see, hear': hear, show, acoustic) and keuə-¹ ('to pay attention': cavēre, kudos), the two halves that feed Nourai's Latin/Greek and Germanic branches respectively. Beekes (per Wiktionary s.v. κῦδος) rejects the derivation of kudos from this root altogether, positing *kewd-s- 'miraculous power'.\",\n      \"note_fa\": \"ریشهٔ هندواروپاییِ آغازینِ *(s)kewh₁- به معنی «نگریستن، دریافتن، شنیدن» است. پوکورنی در صفحهٔ ۵۸۷ فرهنگ خود سرواژه را چنین آورده است: «keu-، skeu-، و با کشیدگی kēu-: توجه کردن (نگریستن)، سپس شنیدن، احساس کردن، دریافتن»؛ پس هر چهار صورتی که نورایی نوشته (Keu، Kou، Skeu، Skou) همان گونه‌های آوایی‌اند که منبعش برشمرده است: Kou صورت o-دار *kouos است که لاتینی caveō و یونانی koéō از آن برآمده، و Skeu/Skou همان گونهٔ دارای «سِ متحرک» (s-mobile) است. برچسب زبانی و معنای داده‌شده هر دو درست‌اند. تنها دو نکته: نخست آنکه والده-پوکورنی (جلد ۱، ص ۳۷۰) خودْ پیوند گونه‌های s-دار را با keu- «مشکوک» می‌خواند؛ دوم آنکه واتکینز این خانواده را به دو ریشهٔ جداگانه (keu-¹ و keuə-¹) بخش کرده است. در مجموع ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewh%E2%82%81-\",\n        \"https://en.wiktionary.org/wiki/%CE%BA%E1%BF%A6%CE%B4%CE%BF%CF%82\",\n        \"https://en.wiktionary.org/wiki/%E0%A4%95%E0%A4%B5%E0%A4%BF\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:587\",\n          \"status\": \"supports\",\n          \"note\": \"Pokorny IEW p.587, read locally in POK_02.txt (awk 'BEGIN{RS=\\\"\\\\f\\\"} NR==247', the leaf whose running head is '587'): '1. keu-, skeu-, dehnstufig kēu- „worauf achten (beobachten, schauen)“, dann „hören, fühlen, merken“; schwere Basis keuə-; s-Erweiterung keu-s-; über Formen mit anlaut. s- s. am Schlusse; kouo-s „sorgsam“; d-Erweiterung keud- : kūd- in keudos : kūdos „Ruhm“'. Root name, language and gloss all as Nourai gives them.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Walde-Pokorny I 368-370 (WLD_Bd1_1930_dli_70244_djvu.txt lines 23228-23356; running heads '369', '370')\",\n          \"stance\": \"supports\",\n          \"note\": \"'1. qeu-, dehnstufig qēu- „worauf achten (beobachten, schauen? s. u.), worauf hören, fühlen, merken“; set-Basis qouə-, auch (ursprünglicher?) qouei-; s-Erw. qeu-s-; über Formen mit anl. s- s. am Schlusse.' — the source Pokorny abridged. But p.370 adds: 'Weil diese s-anl. Formen durchweg die spezielle Bed. „schauen“ aufweisen …, ist ihre Verwandtschaft mit qeu- „worauf achten, merken“ ganz fraglich.'\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985 s.vv. keu-¹ and keuə-¹ (AHD_watkins1985.txt lines 623, 627)\",\n          \"stance\": \"partial\",\n          \"note\": \"'keu-¹ Also akeu-. To perceive, see, hear. O-grade form *akou-. 1. Extended form *kous- in: a. Germanic *hausjan in Old English hieran, to hear: HEAR … b. suffixed form *ə-kous-yo- in Greek akouein, to hear: ACOUSTIC. 2. Variant *skou- in: a. Germanic *skauwōn in Old English scēawian, to look at: SHOW … [Pok. 1. keu- 587.]'; separately 'keuə-¹. To pay attention, perceive (preternaturally). 1. Suffixed o-grade form *kous-o- becoming *kaw- in denominative (stative) Latin cavēre, to beware …: CAUTION, CAVEAT; PRECAUTION. 2. Suffixed zero-grade form *kū-dos … Greek kudos, magical glory: KUDOS. [In Pok. 1. keu- 587.]' — same material, but split into two roots.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck, Selected Synonyms §15.11 'PERCEIVE' p.1021 and §15.41 'HEAR' p.1035 (SYN.txt lines 25949, 26181)\",\n          \"stance\": \"supports\",\n          \"note\": \"'… : Grk. κοέω „notice“, Lat. cavēre „be on one's guard, heed“, Grk. ἀκούω, Goth. hausjan „hear“, etc. (15.41). Berneker 162f. Walde-P. 1.369.' — Buck gathers exactly Nourai's Greek + Latin + Germanic branches under one IE etymon, citing WP I 369 (= Nourai's WLD:1369).\"\n        },\n        {\n          \"src\": \"KLN\",\n          \"where\": \"Klein s.vv. show, hear, Kavi (KLN_1966.txt lines 35051, 17351, 20554)\",\n          \"stance\": \"supports\",\n          \"note\": \"s.v. show: 'fr. I.-E. base *(s)qeu-, *(s)qēu-, „to look at, observe, perceive“, whence also OI. kaviḥ „wise, sage; seer, poet“, ā-kuvate „intends“, Arm. cucanem „I show“, Gk. κοέω …, κῦδος … „glory, fame“ (lit. „that which is heard of“), L. cavēre „to beware“, OSlav. čujǫ, čuti … Cp. also acoustic, caution, cave interj., Kavi, kudos' — Nourai's whole chart in a single Klein entry.\"\n        },\n        {\n          \"src\": \"ARY\",\n          \"where\": \"Aryanpur, Latin index, pdf page 381 (ARY_latin_index_pages.txt line 11098)\",\n          \"stance\": \"supports\",\n          \"note\": \"One index block lists together: 'SKUE (DANISH) … SHKOH (PAHLAVI) … SCHOUWEN (DUTCH) … KAVIS (SANSKRIT) … CHUCANEM (ARMENIAN) … AU-SCAUDITWEI (OLD PRUSSIAN) … USKAWS (GOTHIC) … KOEO (GREEK) … CAVERE, COVERE (LATIN)' — the same family, and (see node 9) it labels au-scauditwei OLD PRUSSIAN.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"kavi; kâvâ-usân\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Avestan kauui- (stem kavay-, Bartholomae AiW col. 442-443 '*kavay- m.') is the direct Iranian continuation of PIE *(s)kewh₁-i- 'one who perceives' (= Skt. kaví-), through Proto-Indo-Iranian *káwHiš; PIE *ḱ/*k before the front vowel gives Indo-Iranian k, and the -i- stem is unchanged. Its Avestan sense is 'poet-priest, seer, vision-poet' in the Gāthās (where kauui- are often opponents of Zaraθuštra) and dynastic 'prince/ruler' in the Younger Avesta, where the Kauui line runs Kauui Kauuāta, Kauui Usan, Kauui Haosrauuah, Kauui Vīštāspa (Yt.13.132-133, Yt.19.71). 'kâvâ-usân' renders the attested nominative kauua usa (Yt.5.45) / genitive kauuōis usaδanō (Yt.13.133) = 'Kavi Usan'. Two reservations: (a) Nourai's gloss 'sovereign' for kavi is the later, Sasanian reinterpretation — Wiktionary, following Skjærvø, notes that 'the visionary poets of the Avesta were mistakenly interpreted as ancient kings by the Sasanian Zoroastrian priests'; (b) 'rich king' for kāvā-usān is a folk gloss: usan-/usaδan- is a proper name (Bartholomae: 'usaδan- m. EN. zweier Gläubiger … eines iranischen Fürsten, der auch usan- heisst'), cognate with Vedic Uśanas Kāvya, not a word for 'rich'.\",\n          \"derivation_fa\": \"واژهٔ اوستایی kauui- (ستاک kavay-) دنبالهٔ مستقیم *káwHiš ایرانی باستان و آن از ریشهٔ هندواروپایی *(s)kewh₁- است و با kaví- سنسکریت یکی است. معنای آن در گاهان «شاعرِ بینا، پیشوای دینیِ نامزرتشتی» و در اوستای نو عنوان دودمان کیانی است (کَوی کَواتَ، کَوی اوسَن، کَوی هَئوسرَوَه، کَوی ویشتاسپ). دو نکته: نخست آنکه معنی «پادشاه» که نورایی داده تعبیر متأخر روزگار ساسانی است، نه معنای اصلی اوستایی؛ دوم آنکه ترجمهٔ «پادشاه توانگر» برای kāvā-usān ریشه‌شناسی عامیانه است، زیرا usan-/usaδan- نام خاص است (بارتولومه، ستون ۴۰۶ و ذیل usaδan-) و هم‌ریشه با اوشَنَس کاویه در ودا، نه واژه‌ای به معنی «توانگر». پس ادعای نورایی در اصلِ اشتقاق درست ولی در معنا با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%A9%DB%8C\",\n            \"https://en.wiktionary.org/wiki/%E0%A4%95%E0%A4%B5%E0%A4%BF\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:196\",\n              \"status\": \"supports\",\n              \"note\": \"Horn, Grundriss p.196 no.879 (HRN.txt, awk 'BEGIN{RS=\\\"\\\\f\\\"} NR==218'): '(2)kei „Herrscher“ (wie ḫusrev „Herrscher“ ursprünglich N. pr.). aw. kavi-; phlv. kē … ai. kavi- „weise“. Dazu got. us-skava „vorsichtig, nüchtern“, ahd. scouwōn „schauen“, Brugmann Grundriss I §528.' — Horn's entry is precisely Nourai's Avestan→Pahlavi→Persian line plus the Sanskrit and Germanic cognates.\"\n            },\n            {\n              \"ref\": \"FAF:504\",\n              \"status\": \"not_checked\",\n              \"note\": \"FAF = Daneshgar, Farhang-e A'lam-e Fārsi (1370/1991); refs_online.json records kind 'none' — no digitised copy on any permitted platform, so p.504 could not be seen.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, AiW col. 442-443 s.v. *kavay-, and col. 406 s.v. usaδan- (BRT.txt lines 9128, 8509)\",\n              \"stance\": \"supports\",\n              \"note\": \"col.443 '*kavay-': 'kavā vīštāspō Y.46.2; … kavaēm kavaēm Yt.19.71 …; kavaδm usaδanm Yt.19.71 …; kavā usa Yt.5.45 …; kavōis haosravaŋhahe Ny.5.5 … 2) jAw. Name für gewisse Feinde des Volks und Glaubens der Mazdayasnier'; and 'usaδan- m. EN. zweier Gläubiger; 1) eines iranischen Fürsten, der auch usan- (s.d.) heisst: kavōis °ana Yt.13.133; yimca kavaēm °δarum Yt.19.71.' — attests both kavi- and Kavi Usan, but glosses usan- as a name, not 'rich'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. Kavi (KLN_1966.txt line 20554)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Kavi, Kawi, n., the ancient language of Java. — Javanese kavi „poetic“, fr. OI. kaviḥ „wise, sage; seer, poet“ … cogn. with Gk. κοέω … fr. I.-E. base *(s)qēu-, „to look at, observe, perceive“, whence also OE. sceawian.'\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II, Glossary s.v. kai and the Avestan index (NYB_vol2_glossary.txt lines 2161, 5222)\",\n              \"stance\": \"supports\",\n              \"note\": \"'kai [kd] king, sovereign, the title of the ancient kings of Eastern Iran … — Av. (442 sq.) kavi-'; index: 'kavi-: kai', 'kavi-(usan-): Kāyōs'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"kay; kayos\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Middle Persian kay (Book Pahlavi <kd>, on coins kd/kdy) continues Old Iranian *kavi- with the regular loss of the Old Iranian -i stem-vowel and monophthongisation of the resulting *kavi > kay; it survives only as the dynastic title of the Kayanians (the line of Kay Kawād, Kay Us, Kay Husraw, Kay Wištāsp), with the oblique plural kayān 'the Kayanids'. 'kayos' is MP Kāyōs / Kay-Us [k'dws], the compound of kay with the name of the second Kayanid, Av. Kauui Usan (gen. usaδanō): Av. usan- > MP -ōs by the usual Middle Persian raising of Old Iranian a before a nasal-final syllable and loss of the final -n. Nyberg's glossary gives exactly this equation. As at node 1, the gloss 'rich king' for kayos has no support: Usan is a name, and Nyberg, MacKenzie and the Pahlavi Bundahišn treat Kāyōs simply as a personal name. MacKenzie's dictionary also warns that the ideographic spelling <kd> makes kay 'when?' and kay 'Kayanian' homographs.\",\n          \"derivation_fa\": \"«کی» فارسی میانه (پهلوی <kd>، بر سکه‌ها kd/kdy) دنبالهٔ *kavi- ایرانی باستان است؛ افتادن واکهٔ پایانی و تک‌واکه‌شدن *kavi به kay دگرگونی آوایی منظم فارسی میانه است. این واژه در پهلوی تنها به‌صورت لقب دودمانی به‌کار می‌رود (کی‌کواد، کی‌اوس، کی‌هوسرَو، کی‌ویشتاسپ) و جمع مضاف‌الیهی آن kayān است. «kayos» همان Kāyōs (کی‌اوس) پهلوی است، مرکب از kay و نام دومین شهریار کیانی، اوستایی Kauui Usan؛ نیبرگ در واژه‌نامهٔ خود به‌روشنی می‌نویسد: «Kāyōs … Av. (406) kavi- usan-, nom. kava usa». باز هم ترجمهٔ «پادشاه توانگر» درست نیست، چون Usan نام خاص است. بنابراین اشتقاق نورایی پذیرفتنی است ولی معنایی که برای جزء دوم آورده تأیید نمی‌شود.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%A9%DB%8C\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:196\",\n              \"status\": \"supports\",\n              \"note\": \"Horn p.196 no.879 (see node 1): 'aw. kavi-; phlv. kē, vergl. Kērat (Gemme, Horn, ZDMG. 44, 675 No. 139)' — Horn's Pahlavi form is written kē, Nyberg's and MacKenzie's kay; the arrow Avestan → Pahlavi is exactly what Horn draws.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.50 s.v. ²kay (PHD.txt line 426; PHD_mackenzie.txt line 3267)\",\n              \"stance\": \"supports\",\n              \"note\": \"'¹kay [ʾYMT < A ʾymt | N ~] when? ²kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-k'] ruler hostile to Zoroaster.'\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II s.vv. kai and Kāyōs (NYB_vol2_glossary.txt lines 2161, 2275)\",\n              \"stance\": \"supports\",\n              \"note\": \"'kai [kd] king, sovereign, the title of the ancient kings of Eastern Iran: ~-Kavāt, the founder of the dynasty; ~-Xōsrōi, ~-Luhrāsp, ~-Vištāsp, cf Kāyōs; pl. cas. obl. kayān [kd'n'] … — Av. (442 sq.) kavi-; MPrth kw, pl. cas. obl. qʾwʾn „giant“; Prs on coins kd, kdy … NP kai „great king“'; and 'Kāyōs [kʾdws] n. pr. a king of the Kavi dynasty … — Av. (406) kavi- usan-, nom. kava usa; Paz. Kahēs.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sogdian\",\n          \"words\": \"qwy\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian qwy /kaw/ (Manichaean, Christian and Sogdian-script texts; oblique/plural kwʾyst 'giants') is the same Old Iranian *kavi- continued in the north-eastern branch, where the -i- stem was lost and the diphthong preserved as -aw. The semantic shift 'Kavi > giant, hero' is Manichaean: in the Sogdian and Middle Persian versions of Mani's Book of Giants the antediluvian giants are called kawān/kawi, because the Iranian translators equated the Enochic giants with the pre-Zoroastrian Kavis of Iranian legend (Henning, 'The Book of the Giants', BSOAS 11, 1943, pp. 52-74, esp. pp. 53, 68, 70 — cited in Gharib's entry). Parthian shows the same word and sense (Nyberg: 'MPrth kw, pl. cas. obl. qʾwʾn „giant“'). Strictly the arrow should read 'Old Iranian *kavi-' rather than 'Avestan', since Sogdian does not descend from Avestan; Gharib's own note '<Av. kavi' uses the Avestan form as the standard citation shape, exactly as Nourai does.\",\n          \"derivation_fa\": \"واژهٔ سغدی qwy (خوانش kaw، جمع kwʾyst «غولان») همان *kavi- ایرانی باستان است که در شاخهٔ شمال‌شرقی ایرانی، با افتادن واکهٔ ستاکی و نگاه‌داشت دوواکهٔ -aw، به این صورت رسیده است. تحول معنایی «کَوی ← غول، پهلوان» زادهٔ ادبیات مانوی است: در ترجمهٔ سغدی و پارسی میانهٔ «کتاب غولان» مانی، غولانِ پیش از طوفان kawān خوانده شده‌اند، زیرا مترجمان ایرانی آنان را با کَویانِ پیش‌زرتشتی یکی گرفتند (هنینگ، BSOAS ۱۱، ص ۵۳ و ۷۰). در پارتی نیز همین واژه با همین معنا هست (نیبرگ: qʾwʾn «غول»). تنها نکتهٔ دقیق آن است که سغدی از اوستایی نمی‌آید، بلکه هر دو از ایرانی باستان‌اند؛ قریب هم صورت اوستایی را تنها به‌عنوان صورت شاهد آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%A9%DB%8C\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"SOD:202\",\n              \"status\": \"supports\",\n              \"note\": \"Gharib, Sogdian Dictionary, entry 5072 (SOD_pages.txt line 18119): '5072 qwy M, C, S … kawi (kwʾyst) © <Av. kavi ⇒ qw¹ / giant, hero / Hen. BSOAS 11.53f; C2, 13V19; Benv. JA 1959, 128; BSTii 886.5 pl. kw(ʾ)yst „giants“ GMS 1186; Hen. BSOAS 11, 70.15, 68.12'; cf. entry 4998 'qwʾ M, C … kaw (kwʾyst) © nom. qwy; pl. kw(ʾ)yst ⇒ qwy / giant, hero'. The dictionary itself writes '<Av. kavi', i.e. Nourai's arrow. (Gharib's numbers are entry numbers, not pages; Nourai's '202' matches the printed page of the entry rather than the entry number 5072.)\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II s.v. kai (NYB_vol2_glossary.txt line 2161)\",\n              \"stance\": \"supports\",\n              \"note\": \"'MPrth kw, pl. cas. obl. qʾwʾn „giant“' — the Parthian counterpart of the Sogdian word, with the same 'giant' sense, under the Avestan kavi- etymology.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Cheung, Etymological Dictionary of the Iranian Verb, s.v. *skauH (CHEUNG.txt lines 22712 ff.)\",\n              \"stance\": \"silent\",\n              \"note\": \"Cheung's only *skauH root is 'to poke, touch; to earmark, ? to cover' (Khot. skau-, Sogd. nyskʾw-, Chor. kʾw-) — a different etymon; he has no Iranian verbal root 'to perceive/see' for this family, so the noun kavi- falls outside his scope.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"kay 2; Kâvŭs; kîyâ; kîyân\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian کی kay 'king (of the Kayanian line)' continues MP kay unchanged; the compounds کیقباد، کیخسرو، کیکاووس that Nourai adds beside it are the Šāhnāma forms of MP Kay-Kawād, Kay-Husraw, Kay-Kāwus. کاووس Kāvus is MP Kāyōs/Kay-Us with the Persian spelling -او- for the long ō; its Arabised doublet قابوس Qābūs (Nourai's parenthesis) is the same name taken into Arabic with the regular substitution of q- for k- and ب for the Persian -w- (the Ziyarid Qābūs b. Wušmgīr). کیان kayān is the inherited Middle Persian oblique plural of kay, reused in New Persian as an ordinary plural 'kings', whence the adjective کیانی 'Kayanian'; کیانوش is a Šāhnāma proper name built on the same element. کیا kiyā, a Caspian title ('a great man, a lord, a margrave' — Mo'in), is the same word with the -ā of the vocative/emphatic; it is the title of the Kiā dynasty of Gilān and of the Zaydī sayyids of Ṭabaristān. Mo'in's footnote in Borhān records a competing view for the Kurdish form (Jaba deriving Kurdish kia from Persian کدخدا), but keeps کیا itself under کی.\",\n          \"derivation_fa\": \"«کی» فارسی نو دنبالهٔ بی‌تغییر kay پهلوی است و ترکیب‌های کیقباد، کیخسرو و کیکاووس همان Kay-Kawād و Kay-Husraw و Kay-Kāwus پهلوی‌اند. «کاووس» صورت فارسیِ Kāyōs پهلوی است که در آن ō کشیده به «او» نوشته شده؛ «قابوس» معرّب همان نام است (ابدال ک به ق و و به ب، مانند نام قابوس بن وشمگیر زیاری). «کیان» جمعِ مضاف‌الیهیِ به‌ارث‌ماندهٔ پهلوی است که در فارسی نو جمع عادی «پادشاهان» شده و صفت «کیانی» از آن ساخته شده است. «کیا» عنوانی مازندرانی–گیلانی است به معنی «بزرگ ناحیه، پادشاه کوچک، مرزبان» (معین) و از همین ریشه است. برهان قاطع به تصحیح معین در صفحات ۱۷۴۹–۱۷۵۱ همهٔ این واژه‌ها را زیر «کی» و «کیا» و «کیان» آورده و در حاشیه به اوستایی kavi بازگردانده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%A9%DB%8C\",\n            \"https://abadis.ir/fatofa/%DA%A9%DB%8C%D8%A7/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1749-1751\",\n              \"status\": \"supports\",\n              \"note\": \"Borhān-e Qāṭeʿ ed. Moʿin, vol.3 (printed pp.1749-1751 = BQT_v3_pages.txt pdf pages 546-548; offset printed = pdf+1203, checked against the running head '۱۷۴۷' on pdf 544). p.1749 «کی» with Moʿin's footnote 1: «در اوستا kavi ذکر شده. از گاهان بر می‌آید که «کوی» بمعنی پادشاه و امیر و فرمانده است … در پهلوی kai (Kavi)»; p.1749-1750 «کیا … بمعنی کی است که پادشاه بزرگ جبار باشد … و مرزبان را نیز گویند که زمین‌دار باشد یعنی پادشاه کوچک», with footnote 8 «مازندرانی … بزرگ ناحیه … که مخصوصاً بطبقه‌ای از سادات زیدی طبرستان اطلاق شود»; p.1751 «کیان — بکسر اول جمع کی باشد بمعنی پادشاهان بزرگ … که کیقباد و کیخسرو و کیکاوس و کی لهراسب باشد». Exactly the four words and the two script-extras of the node.\"\n            },\n            {\n              \"ref\": \"MON:3147\",\n              \"status\": \"not_checked\",\n              \"note\": \"Moʿin, Farhang-e Fārsi vol.3 p.3147: only the 2-volume Adena abridgement is on disk (MON_part1/2.txt), with different pagination, and vajehyab/abadis give the entry text without page numbers. The online Moʿin entry for کیا («بزرگ، سرور؛ پادشاه، حاکم؛ مرزبان، پهلوان», abadis.ir) agrees with the node's gloss, but p.3147 itself could not be checked.\"\n            },\n            {\n              \"ref\": \"FAF:491,504\",\n              \"status\": \"not_checked\",\n              \"note\": \"FAF (Daneshgar, Farhang-e Aʿlām-e Fārsi) is not digitised anywhere reachable (refs_online.json kind 'none').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg II s.v. kai (NYB_vol2_glossary.txt line 2161)\",\n              \"stance\": \"supports\",\n              \"note\": \"'pl. cas. obl. kayān [kdʾn'] … NP kai „great king“ and borrowed from the NW language kav „valiant, grand, of fine figure“' — the direct MP source of NP کی and کیان.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Moʿin s.v. کیا, read on abadis.ir\",\n              \"stance\": \"supports\",\n              \"note\": \"Moʿin: «۱- بزرگ، سرور ۲- پادشاه، حاکم ۳- مرزبان، پهلوان»; Dehkhodā adds that the title was borne by governors in Ṭabaristān and Gīlān — the sense Nourai glosses 'a respected person in a group'.\"\n            },\n            {\n              \"src\": \"FSF\",\n              \"where\": \"Nushin, Vāžanāmak (Shāhnāma glossary), s.vv. کیان / کاوس (FSF_pages.txt lines 249, 975, 1773, 1870)\",\n              \"stance\": \"supports\",\n              \"note\": \"The Shāhnāma citations gathered there («چنگ کیان», «فر کیان دارد و چنگ شیر», «نه رسم کیان بد نه آیین پیش», «چو کاوس را دید دستان سام») attest کیان as the ordinary Persian plural 'the Kayanian kings' and کاوس as the king's name, the usage Nourai's node records.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"šokuh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian شکوه šokuh/šukōh 'glory, majesty, grandeur' goes back to Middle Persian škōh (Book Pahlavi <škwh>, Manichaean MP ʾyšqwhʾn) from Old Iranian *skauaθa-, a -θa- abstract to the s-mobile form *skau- 'to look at' of this very root: the formation is exactly parallel to MP handōh > NP اندوه andōh 'sorrow' from *san-day-aθa-, as Bartholomae showed. The semantic path is 'what is looked at' > 'imposing appearance, dignity' > 'splendour, majesty' — Bartholomae compares German schön and Ansehen, and Pokorny prints the equation verbatim. Initial *sk- gives Middle Persian š(k)-, and prothetic i-/e- appears in the Manichaean spelling ʾyšqwh-. Modern Persian has the doublets شکوه šokuh and شکوه šekuh/شکوهیدن; the homophone شکوه 'complaint' is a separate Arabic loan (شَكْوَة šakwa) and is not involved here. Nourai attaches the node directly to the root, which is right, since the s-form does not pass through the Avestan kavi- branch.\",\n          \"derivation_fa\": \"«شُکوه» فارسی از فارسی میانهٔ škōh (پهلویِ کتابی <škwh>، مانوی ʾyšqwhʾn) و آن از ایرانی باستان *skauaθa- است، یعنی اسم‌مصدری با پسوند -aθa- از گونهٔ s-دارِ همین ریشه (*skau- «نگریستن»). بارتولومه این ساخت را دقیقاً با «اندوه» سنجیده است: andōh < handōh < *san-day-aθa-. تحول معنایی چنین بوده است: «آنچه دیده می‌شود» ← «هیبت و آبرو» ← «شکوه و بزرگی»؛ خودِ بارتولومه واژهٔ آلمانی schön و Ansehen را برای همین دگرگونی معنایی شاهد می‌آورد. خوشهٔ آغازینِ *sk- در فارسی میانه به š(k)- بدل شده و در نگارش مانوی «ای» آغازی افزوده شده است. «شکوه» به معنی «شکایت» واژه‌ای جداگانه و معرّب از عربی «شَکْوة» است و به این ریشه ربطی ندارد. ادعای نورایی و هر دو ارجاع او درست‌اند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B4%DA%A9%D9%88%D9%87\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewh%E2%82%81-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:588\",\n              \"status\": \"supports\",\n              \"note\": \"Pokorny IEW p.588, section '2. Mit anlautendem s-' (POK_02.txt, awk 'BEGIN{RS=\\\"\\\\f\\\"} NR==247'): 'miran. škōh, np. šikōh, šukōh (uriran. *skauaθa-) „Pracht, Herrlichkeit, Majestät, Würde“' — Nourai's node word for word.\"\n            },\n            {\n              \"ref\": \"ZAW:81\",\n              \"status\": \"supports\",\n              \"note\": \"Bartholomae, Zum altiranischen Wörterbuch, Exkurs §82 d, p.81 (ZAW_pages.txt leaf 105, printed = leaf−24): 'd) išqôhân 88; s. bp. škoh, np. šikōh, šukōh ¹)', with footnote 1: 'Aus ar. *skau-atha wie bp. handōh, np. andōh „Sorge, Kummer“ aus *san-day-atha … Das Wort gehört zu nhd. schauen, asächs. skauwōn. Wegen der Bedeutung „Würde, Herrlichkeit, Pracht“ vergleiche man unser schön und Ansehen.' This is the very passage Pokorny is quoting, and it is exactly Nourai's arrow.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny I 370 (WLD_Bd1_1930_dli_70244_djvu.txt line ~23310)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Mit anl. s-: miran. škōh, np. šikōh, šukōh (uriran. *skauaθa-) „Pracht, Herrlichkeit, Majestät, Würde“ (Bartholomae ZfdtWtf. 9, 19)' — but the same page adds that the connection of the s-forms with qeu- 'to notice' is 'ganz fraglich'.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Latin index pdf p.381 (ARY_latin_index_pages.txt line 11098)\",\n              \"stance\": \"supports\",\n              \"note\": \"'SHKOH (PAHLAVI)' stands in the same index block as SCHOUWEN (Dutch), USKAWS (Gothic) and CAVERE (Latin), i.e. Aryanpur too files Persian شکوه under this IE root.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien (HUB.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep for 'kōh', 'skoh', 'Pracht', 'skaua' in HUB.txt returns nothing; the local Google scan's OCR does not yield the entry, so Hübschmann could not be used here.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"kavî\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Sanskrit kaví- m. 'wise man, sage, seer, prophet; singer, bard, poet', adj. 'gifted with insight, intelligent, wise', is the Indic twin of Av. kauui-, both from Proto-Indo-Iranian *káwHiš, an -i- stem to PIE *(s)kewh₁- 'to perceive': the root's laryngeal survives as the Vedic hiatus/length in derivatives (kāvyá-), and the meaning is the concrete agent noun 'the one who perceives'. Pokorny p.587 and Horn p.196 both cite it in exactly this shape. The one point that overstates the evidence is Nourai's second gloss 'sovereign': that sense belongs only to the Iranian branch (and there only from the Younger Avesta on); no Sanskrit dictionary gives kaví- the meaning 'king'. Formally, too, the accepted lemma is kaví- (short i), not the kavî of the chart.\",\n          \"derivation_fa\": \"سنسکریت kaví- به معنی «فرزانه، بینا، غیب‌دان؛ سراینده، شاعر» همتای هندیِ kauui- اوستایی است و هر دو از *káwHiš هندوایرانی آغازین و آن از ریشهٔ *(s)kewh₁- «دریافتن» می‌آید؛ ساخت آن اسم فاعلی با ستاک -i است، یعنی «آن که درمی‌یابد». پوکورنی (ص ۵۸۷) و هرن (ص ۱۹۶) هر دو همین صورت و معنا را آورده‌اند. اما معنی دومی که نورایی داده — «فرمانروا» — تنها به شاخهٔ ایرانی تعلق دارد و در هیچ فرهنگ سنسکریتی برای kaví- نیامده است؛ افزون بر این صورت درست kaví- با «ای» کوتاه است نه kavî. پس ادعا در اصلِ هم‌ریشگی درست، ولی در معنا با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E0%A4%95%E0%A4%B5%E0%A4%BF\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewh%E2%82%81-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:587\",\n              \"status\": \"supports\",\n              \"note\": \"POK p.587, first paragraph of '1. keu-': 'Ai. kavi- „klug, weise; Seher, Dichter“, kavāri- „eigennützig, karg“, a-kava- „nicht geizig“; ā-kūvate „beabsichtigt“, ā-kūta- n., ā-kūti- f. „Absicht“.' — 'wise' yes, 'sovereign' no.\"\n            },\n            {\n              \"ref\": \"HRN:196\",\n              \"status\": \"partial\",\n              \"note\": \"Horn p.196 no.879 ends 'ai. kavi- „weise“' — he gives the Sanskrit cognate under NP kei, i.e. supports the equation, but glosses it only 'wise', not 'sovereign'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny I 368-369\",\n              \"stance\": \"supports\",\n              \"note\": \"'Ai. kavi „klug, weise; Seher, Dichter“ (Bildung wie gr. τροφός), kavī-yas- „klüger“, kavāri „eigennützig, karg“ … ā-kucate „beabsichtigt“ (vgl. bes. Osthoff MU. IV 92, 105)'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. Kavi and s.v. hear (KLN_1966.txt lines 20554, 17351)\",\n              \"stance\": \"supports\",\n              \"note\": \"'OI. kaviḥ „wise, sage; seer, poet“' in both entries, filed with Gk. κοέω and OE sceawian under I.-E. *(s)qēu-.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, IE Comparative Dictionary (IEC.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep for Kauio/Kouos/Keudos/Skeuo yields only Mann's homonymous roots Kauiō 'burn, scorch' and Kouos 'hollow'; he has no lemma for the 'perceive' root, so Mann is silent on kaví-.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Avestan\",\n          \"words\": \"čevîšî\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan čəuuīšī is the 1st singular middle sigmatic aorist of the verb kav-/čav- 'to look out for, expect', translated by Bartholomae 'ich erhoffte, versah mich' ('I hoped, I expected'), i.e. exactly Nourai's 'attend, expect, hope'. The initial č- is the regular Iranian palatalisation of *k- before the front vowel of the s-aorist stem *kau-i-š- (the same alternation as Av. kav- : čəuu-), and -š- is the aorist marker; the form is attested once and is discussed by Bartholomae, BB 13.66 and AiW col. 442. It stands beside Skt. ā-kūvate 'intends' as the verbal use of the root. Note that the node's word is an inflected form, not a lemma, because Nourai copies it straight out of the two references he cites, both of which print it in exactly this shape.\",\n          \"derivation_fa\": \"صورت اوستایی čəuuīšī اول‌شخص مفرد ماضیِ سیگماتیک میانه از فعل kav-/čav- «چشم به راه بودن، انتظار داشتن» است و بارتولومه آن را «ich erhoffte, versah mich» (امید داشتم، چشم داشتم) ترجمه کرده است — همان معنایی که نورایی آورده. «چ» آغازین نتیجهٔ کامی‌شدنِ منظمِ *k پیش از واکهٔ پیشین ستاکِ ماضی است (مانند جفتِ kav- : čəuu-) و -š- نشانهٔ ماضی سیگماتیک. این صورت یک‌بار در اوستا آمده و بارتولومه در ستون ۴۴۲ فرهنگ ایرانی باستان و در BB ۱۳:۶۶ آن را بررسیده است. نکته آنکه این یک صورت صرف‌شده است نه ستاک، چون نورایی آن را مستقیم از همان دو مرجع خود برداشته است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewh%E2%82%81-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"WLD:1369\",\n              \"status\": \"supports\",\n              \"note\": \"Walde-Pokorny Band I p.369 (WLD_Bd1_1930_dli_70244_djvu.txt, running head '369' at line ~23237): 'av. čəvīšī 1. Sg. med. Aor. „ich erhoffte, versah mich“ (vgl. Bartholomae BB. 13, 66, Airan. Wb. 442)'. Nourai's 'WLD:1369' = Walde-Pokorny volume 1, page 369, and it prints his form and gloss exactly.\"\n            },\n            {\n              \"ref\": \"POK:587\",\n              \"status\": \"supports\",\n              \"note\": \"Pokorny p.587, in the same paragraph as Skt. kavi-: 'av. čəvīšī 1. Sg. Med. Aor. „ich erhoffte, versah mich“' — Pokorny's abridgement of the WP line.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, AiW col. 442 (the kav-/kavay- column, BRT.txt line 9128 area)\",\n              \"stance\": \"supports\",\n              \"note\": \"Both WP and Pokorny cite 'Airan. Wb. 442' for this form; the local OCR of BRT.txt at that column is too corrupt to quote the line itself, but the column reference is the one printed in both dictionaries.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Cheung, EDIV (CHEUNG.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"Cheung has no root *kauH 'to perceive/expect'; his only near match, *skauH 'to poke, touch; to earmark' (p.347), is a different etymon with Khotanese and Chorasmian evidence, so this Avestan aorist is not treated in EDIV.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": null,\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"An empty box in the printed chart: the rectangle to the right of the Avestan čevîšî node carries no language label, no word and no reference (confirmed on the page image, site/pages/263.jpg). Nourai's layout normally puts a descendant here; nothing was filled in, and no descendant of čəuuīšī can be reconstructed from the box, so there is nothing to verify. The extraction is faithful to the page.\",\n          \"derivation_fa\": \"این خانه در نمودار چاپی خالی است: مستطیل کنارِ «čevîšî» نه برچسب زبانی دارد، نه واژه‌ای و نه ارجاعی (بر روی تصویر صفحهٔ ۲۶۳ بازبینی شد). در چیدمان نورایی معمولاً در این جایگاه واژهٔ بازمانده می‌آید، ولی این خانه پر نشده است؛ بنابراین چیزی برای راستی‌آزمایی وجود ندارد. خوانش اسکن با صفحهٔ چاپی مطابق است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference in the book.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BOOK\",\n              \"where\": \"printed page 233 (pdf 263), image at data/verification/sources/refs/ocr/BOOK/263.png\",\n              \"stance\": \"silent\",\n              \"note\": \"The box is drawn empty on the page; nothing to consult.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Old Persian\",\n          \"words\": \"au-šaudîhtwei\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"Old Persian ▭ POK:588 | au-šaudîhtwei : to trust\",\n          \"correct_form\": \"Old Prussian auschaudītwei (au-schaudīt-wei) 'to trust'\",\n          \"derivation\": \"There is no Old Persian word of this shape, and Old Persian has no infinitive in -twei. The form comes straight from the page Nourai cites: Pokorny p.588, last line of the s- section, reads 'apr. au-schaudītwei „vertrauen“', where 'apr.' is Pokorny's abbreviation for altpreußisch = OLD PRUSSIAN, a West Baltic language, not Old Persian (Pokorny's abbreviation for that is 'ap.'). Walde-Pokorny I 370 gives the fuller statement: 'Dasselbe d wie čudo scheint im s-anl. apr. au-schaudītwei „vertrauen“, auschaude „er traut“ vorzuliegen (Trautmann Apr. 308)'. The word is thus Old Prussian au-schaudī-twei, a prefixed (au- 'off, away') stative to the d-extension *(s)keud- of the root, with the Baltic infinitive suffix -twei, and it belongs to the same d-extension as OCS čudo 'wonder' and Gk. κῦδος. The mistake is Nourai's own — the printed page (image saved as data/verification/sources/refs/ocr/BOOK/263.png) reads 'Old Persian' — so the extraction is faithful and the JSON needs no change; the entry is simply attached to the wrong branch of Indo-European. Aryanpur, working from the same Pokorny page, labels the identical form correctly as OLD PRUSSIAN.\",\n          \"derivation_fa\": \"چنین واژه‌ای در پارسی باستان وجود ندارد و پارسی باستان اصلاً مصدرِ پایان‌یافته به -twei ندارد. صورتِ یادشده مستقیماً از همان صفحه‌ای گرفته شده که نورایی به آن ارجاع داده است: پوکورنی در صفحهٔ ۵۸۸، پایانِ بخشِ s-دار، می‌نویسد «apr. au-schaudītwei „vertrauen“»؛ و «apr.» در پوکورنی کوته‌نوشتِ altpreußisch یعنی «پروسی باستان» (زبانی بالتیک غربی) است، نه «ap.» که کوته‌نوشتِ پارسی باستان است. والده-پوکورنی (جلد ۱، ص ۳۷۰) نیز می‌گوید: «همان d که در čudo هست در پروسی باستانِ au-schaudītwei „اعتماد کردن“ و auschaude „اعتماد می‌کند“ دیده می‌شود». پس این واژه پروسی باستان است، با پیشوند au- و پسوند مصدرسازِ بالتیکی -twei، از گسترشِ d-دارِ ریشه (*keud-) که کلمهٔ اسلاوی čudo و یونانی κῦδος نیز از آن‌اند. این خطا از خودِ کتاب است — در صفحهٔ چاپی «Old Persian» نوشته شده — نه خطای خوانش اسکن؛ آریان‌پور نیز که از همین صفحهٔ پوکورنی کار کرده، همین صورت را درست «OLD PRUSSIAN» برچسب زده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewh%E2%82%81-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:588\",\n              \"status\": \"contradicts\",\n              \"note\": \"POK p.588 (POK_02.txt, awk 'BEGIN{RS=\\\"\\\\f\\\"} NR==247'), closing line of section '2. Mit anlautendem s-': 'apr. au-schaudītwei „vertrauen“.' The reference has the word Nourai gives, but assigns it to Old PRUSSIAN, not Old Persian — the citation supports the form and contradicts the language label.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny I 370 (WLD_Bd1_1930_dli_70244_djvu.txt line ~23306)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'Dasselbe d wie čudo scheint im s-anl. apr. au-schaudītwei „vertrauen“, auschaude „er traut“ vorzuliegen (Trautmann Apr. 308).' — apr. = altpreußisch; Trautmann's Altpreußische Sprachdenkmäler p.308 is the source.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Latin index pdf p.381 (ARY_latin_index_pages.txt line 11098)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"The index block prints '(OLD PRUSSIAN) … AU-SCAUDITWEI' immediately beside 'USKAWS (GOTHIC)' and 'CAVERE, COVERE (LATIN)' — an independent Persian-language reference work that files the identical form under Old Prussian.\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian: Grammar, Texts, Lexicon (KNT.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"Kent's Old Persian lexicon has no verb of this shape and no infinitive formation in -twei (Old Persian infinitives end in -tanaiy), confirming that the form cannot be Old Persian.\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": null,\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"A second empty box in the printed chart, drawn to the right of the mislabelled 'Old Persian' node and carrying no language, word or reference (checked on the page image). As with node 8 the box was never filled in, so there is no claim to test; the extraction reproduces the page correctly.\",\n          \"derivation_fa\": \"دومین خانهٔ خالیِ نمودار، کنارِ خانهٔ «پارسی باستان»؛ نه زبانی دارد، نه واژه‌ای و نه ارجاعی (روی تصویر صفحه بررسی شد). مانند خانهٔ ۸، این مستطیل هرگز پر نشده است و ادعایی برای سنجیدن در آن نیست؛ خوانش اسکن با صفحهٔ چاپی مطابق است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference in the book.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BOOK\",\n              \"where\": \"printed page 233 (pdf 263), image at data/verification/sources/refs/ocr/BOOK/263.png\",\n              \"stance\": \"silent\",\n              \"note\": \"The box is drawn empty on the page; nothing to consult.\"\n            }\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Greek\",\n          \"words\": \"akavein; kudos\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"akavein : to hear\",\n          \"correct_form\": \"akouein (ἀκούειν)\",\n          \"derivation\": \"The second word is right: Greek κῦδος kūdos 'glory, fame (esp. in battle)', Homeric and frequent in the Iliad, literally 'that which is heard of', is a neuter s-stem *kūd-os to the d-extension *keud-/*kūd- of this root, ablauting with OCS čudo 'wonder' — Pokorny prints 'd-Erweiterung keud- : kūd-os „Ruhm“' and Klein glosses it 'lit. means „that which is heard of“'. (Beekes dissents, deriving κῦδος and Slavic *čudo from a separate *kewd-s- 'miraculous power'.) The first word, however, is not Greek: 'akavein' is a misprint for ἀκούειν akouein 'to hear', the form that stands in Nourai's own reference — Watkins/AHD keu-¹ has 'suffixed form *ə-kous-yo- in Greek akouein, to hear: ACOUSTIC'. Greek ἀκούω goes back to *ə-kous-yō, with copulative ἀ- (< *sm̥-, 'together, with') prefixed to the s-extension *kous- of the root, so the -ou- is the inherited o-grade diphthong and can never appear as -av-. The printed page (data/verification/sources/refs/ocr/BOOK/263.png) shows 'akavein', so the error is the book's, not the extraction's; the JSON should be left as it stands.\",\n          \"derivation_fa\": \"واژهٔ دوم درست است: یونانی κῦδος «شکوه، آوازه (به‌ویژه در نبرد)» — که در ایلیاد پرکاربرد است — اسمی خنثی با ستاک s از گسترشِ d-دارِ ریشه (*keud-/*kūd-) است و تحت‌اللفظ یعنی «آنچه از آن می‌شنوند»؛ پوکورنی می‌نویسد «d-Erweiterung keud- : kūdos „Ruhm“» و کلاین همان معنای تحت‌اللفظی را می‌آورد. (بیکس این را نمی‌پذیرد و κῦδος و čudo اسلاوی را از *kewd-s- «نیروی شگفت» می‌داند.) اما واژهٔ نخست یونانی نیست: «akavein» غلط چاپی است به‌جای ἀκούειν (akouein) «شنیدن» — همان صورتی که در مرجعِ خودِ نورایی، یعنی واتکینز، آمده است: «Greek akouein, to hear: ACOUSTIC». ἀκούω از *ə-kous-yō است، با پیشوندِ همراهیِ ἀ- بر سرِ گسترشِ *kous- ریشه؛ پس دوواکهٔ -ου- به‌ارث رسیده است و هرگز -av- نمی‌شود. صفحهٔ چاپی «akavein» دارد، پس خطای چاپیِ کتاب است، نه خطای خوانش اسکن.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/acoustic\",\n            \"https://www.etymonline.com/word/kudos\",\n            \"https://en.wiktionary.org/wiki/%CE%BA%E1%BF%A6%CE%B4%CE%BF%CF%82\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"partial\",\n              \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 623) s.v. keu-¹: 'b. suffixed form *ə-kous-yo- in Greek akouein, to hear: ACOUSTIC'; s.v. keuə-¹ (line 627): '2. Suffixed zero-grade form *kū-dos (< *kuə-dos) in Greek kudos, magical glory: KUDOS.' Both words are in Nourai's reference — but as akouein, and split between two AHD roots.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"Pokorny IEW p.587-588\",\n              \"stance\": \"supports\",\n              \"note\": \"'von der Basis keu-s-: ἀκούω „höre“ (*ἀκούσι̯ω), ἀκοή, hom. ἀκουή „Gehör“ … ἀ- ist kaum = n̥ „ἀν-“, sondern = ἁ- … durch Hauchdissimilation, oder idg. sm̥- „zusammen“'; and 'gr. κῦδος „Ruhm, Ehre“, κύδιστος „ruhmreichst“, eigentlich „wovon man hört“.'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.vv. acoustic and kudos (KLN_1966.txt lines 1473, 20879)\",\n              \"stance\": \"supports\",\n              \"note\": \"'acoustic, adj. — F. acoustique, fr. Gk. ἀκουστικός „pertaining to hearing“, fr. ἀκουστός „heard, audible“, verbal adj. of ἀκούειν „to hear“, which stands for *ἀκουσιειν and is prob. formed fr. copul. [ἀ-]'; 'kudos, n., fame, renown (colloq.) — Gk. κῦδος „glory, fame“, which stands for *qūdos and lit. means „that which is heard of“.'\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck §15.41 HEAR, p.1035 (SYN.txt line 26181)\",\n              \"stance\": \"supports\",\n              \"note\": \"Buck's HEAR row opens 'Grk. ἀκούω' and runs through 'Goth. hausjan … OE hīeran … NE hear', the same set Nourai distributes over nodes 11 and 17.\"\n            }\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"French\",\n          \"words\": \"acoustique\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"French acoustique is a learned 17th-18th century formation on the Latinised Greek acousticus < ἀκουστικός 'pertaining to hearing', the verbal adjective of ἀκούειν; it is first used as a noun for the science of sound by Joseph Sauveur in 1701 ('j'ai donc cru qu'il y avoit une science supérieure à la musique, et je l'ai appelée Acoustique'), the sense in which it then spread to the other European languages. The node carries no reference in the book, but Klein makes French the intermediary for the English word as well: 'acoustic, adj. — F. acoustique, fr. Gk. ἀκουστικός'.\",\n          \"derivation_fa\": \"«acoustique» فرانسوی واژه‌ای عالمانه است که در سده‌های هفدهم و هجدهم از صورت لاتینی‌شدهٔ acousticus (از یونانی ἀκουστικός «مربوط به شنیدن»، صفت فعلی ἀκούειν) ساخته شده است. ژوزف سووُر در سال ۱۷۰۱ آن را نخستین بار به‌عنوان نام دانشِ صوت به‌کار برد و از همان‌جا به دیگر زبان‌های اروپایی رفت. این خانه در کتاب ارجاعی ندارد، اما کلاین نیز فرانسه را واسطهٔ ورود واژه به انگلیسی می‌داند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/acoustic\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai gives this node no reference; the parent Greek node's reference is AHD, whose keu-¹ entry ends the chain at English ACOUSTIC without naming the French stage.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. acoustic (KLN_1966.txt line 1473)\",\n              \"stance\": \"supports\",\n              \"note\": \"'acoustic, adj. — F. acoustique, fr. Gk. ἀκουστικός, „pertaining to hearing“, fr. ἀκουστός, „heard, audible“, verbal adj. of ἀκούειν, „to hear“.'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.v. Acoustic (SKT.txt line ~351)\",\n              \"stance\": \"partial\",\n              \"note\": \"'Acoustic. (Gk.) Gk. ἀκουστικός, relating to hearing (or sound). — Gk. ἀκούειν, to hear.' Skeat marks the word '(Gk.)' and passes over the French stage that Klein, Etymonline and Nourai insert.\"\n            }\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Persian\",\n          \"words\": \"âkŭstîk\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian آکوستیک ākustik 'acoustics' is a 20th-century European technical loan, taken with the French shape: the initial آ- renders French /a/ in an open first syllable as Persian long ā (as in آنتن antenne, آسفالت asphalte), -ou- gives Persian و /u/, and the French ending -ique is regularly rendered -یک -ik in the Persian scientific vocabulary built from French in the Dār al-Funūn and post-Reza-Shah period (کلاسیک, تکنیک, فیزیک, الکتریک). An English source would have given *اکوستیک with initial short a and a different stress. The chart's route Greek → French → Persian is therefore right; it is simply the Persian end of the same chain that produced English acoustic.\",\n          \"derivation_fa\": \"«آکوستیک» وام‌واژه‌ای اروپایی از سدهٔ بیستم است و صورت فرانسویِ acoustique را نشان می‌دهد: «آ»ی آغازین برابرِ a فرانسوی در هجای باز است (مانند آنتن، آسفالت)، «و» برابرِ -ou- فرانسوی، و پایانهٔ -یک برابرِ -ique است — همان الگویی که در واژه‌های علمیِ برگرفته از فرانسه در فارسی دیده می‌شود (کلاسیک، تکنیک، فیزیک، الکتریک). اگر واژه از انگلیسی می‌آمد، صورت آن «اکوستیک» با «الف» کوتاه می‌شد. پس مسیر یونانی ← فرانسوی ← فارسی که نورایی کشیده درست است. تنها مرجع او (مشیری، فرهنگ واژه‌های اروپایی در فارسی، ص ۱۵) در دسترس نبود.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/acoustic\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"VOP:15\",\n              \"status\": \"not_checked\",\n              \"note\": \"VOP = Mahshid Moshiri, Farhang-e Vāžehā-ye Orupāyi dar Fārsi (Alborz 1371/1992); refs_online.json records kind 'none' — searched archive.org, ketabnak, noorlib and the open web with no copy found, so p.15 could not be read.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. acoustic (KLN_1966.txt line 1473)\",\n              \"stance\": \"supports\",\n              \"note\": \"Confirms the French form acoustique as the modern international shape from which the Persian was taken; Klein also lists the combining forms '-acousia, -acousis … fr. Gk. ἀκόυσις, „hearing“'.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Moʿin / abadis.ir lookup for آکوستیک\",\n              \"stance\": \"silent\",\n              \"note\": \"abadis.ir returned HTTP 400 for the آکوستیک query and no Moʿin entry could be retrieved; Moʿin's volume 4 (foreign compounds) is not online.\"\n            }\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"English\",\n          \"words\": \"acoustic; kudos\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English acoustic (c.1600, 'pertaining to hearing or sound') is taken from French acoustique, itself from Latinised Greek akoustikos (Klein, Etymonline); Skeat marks it simply '(Gk.)'. English kudos entered much later, in 1799, as Oxford and Cambridge university slang for 'fame, renown, glory', a direct book-borrowing of Greek κῦδος; the familiar back-formed singular 'kudo' (1936) rests on mistaking the Greek -s for an English plural. Both words therefore reach English from Greek, exactly as the chart's arrow says — with the qualification that acoustic came by way of French (which is why Nourai's own chart puts a French box in the parallel Persian line).\",\n          \"derivation_fa\": \"«acoustic» انگلیسی (حدود ۱۶۰۰ م.) از فرانسوی acoustique و آن از یونانیِ لاتینی‌شدهٔ akoustikos گرفته شده است (کلاین و اتیمانلاین؛ اسکیت آن را یکراست یونانی می‌داند). «kudos» بسیار دیرتر، در سال ۱۷۹۹، به‌عنوان اصطلاح دانشگاهی آکسفورد و کیمبریج به معنی «آوازه، افتخار» از یونانی κῦδος وام گرفته شد؛ صورتِ مفردِ ساختگیِ kudo (۱۹۳۶) از آنجا پیدا شد که -s پایانیِ یونانی را نشانهٔ جمع انگلیسی پنداشتند. پس هر دو واژه از یونانی به انگلیسی رسیده‌اند، همان‌گونه که نمودار می‌گوید؛ تنها با این توضیح که acoustic از راه فرانسه آمده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/acoustic\",\n            \"https://www.etymonline.com/word/kudos\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node itself carries no reference; the parent Greek node cites AHD, whose keu-¹ and keuə-¹ entries end at 'ACOUSTIC' and 'KUDOS' respectively — i.e. AHD does support this arrow.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.vv. acoustic, kudos (KLN_1966.txt lines 1473, 20879)\",\n              \"stance\": \"supports\",\n              \"note\": \"'acoustic, adj. — F. acoustique, fr. Gk. ἀκουστικός'; 'kudos, n., fame, renown (colloq.) — Gk. κῦδος „glory, fame“ … It is cogn. with OSlav. čudo … Cp. Gk. κοέω „I mark, perceive, hear“, and see show.'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.v. Acoustic (SKT.txt line ~351)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Acoustic. (Gk.) Gk. ἀκουστικός, relating to hearing (or sound). — Gk. ἀκούειν, to hear.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Latin\",\n          \"words\": \"cavěre\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin caveō, cavēre 'to be on one's guard, take heed, beware' is a stative/denominative in -ē- built on the o-grade noun *kouos 'watchful' (Pokorny: 'lat. caveō, -ēre „sich in acht nehmen, sich vorsehen“ (*covēre, Denom. von *kouos)'), the same *kouos that underlies Greek κοέω 'I mark, perceive' — intervocalic *-ow- gives Latin -av-, hence cavēre beside the participle cautus (< *kaw-i-tos) and umbr. kutef. Watkins files it under keuə-¹ '1. Suffixed o-grade form *kous-o- becoming *kaw- in denominative (stative) Latin cavēre, to beware'. The gloss 'to watch' is a shade concrete for a verb whose Latin sense is 'to be wary, guard against', but the connection to the root's basic 'watch, pay attention' is exactly what the sources give. The book prints the vowel as cavěre with a breve; the Latin second-conjugation infinitive is cavēre with a long ē — a diacritic slip in the book, not a wrong word, and the extraction reproduces the page correctly.\",\n          \"derivation_fa\": \"لاتینی caveō / cavēre «برحذر بودن، پاییدن، احتیاط کردن» فعلی حالتی با پسوند -ē- است که بر پایهٔ اسمِ o-دارِ *kouos «هوشیار» ساخته شده — همان *kouos که یونانی κοέω نیز از آن است. پوکورنی می‌نویسد: «lat. caveō, -ēre … (*covēre، مشتق از *kouos)». دگرگونی آوایی -ow- میان‌واکه‌ای در لاتین به -av- بدل شده و از همین‌جاست جفتِ cavēre و اسم مفعول cautus. واتکینز نیز آن را ذیل keuə-¹ می‌آورد. معنی «نگریستن» که نورایی داده اندکی عینی‌تر از معنای لاتینی («پرهیز کردن، پاس داشتن») است، ولی پیوند با معنای پایهٔ ریشه همان است که منابع می‌گویند. در کتاب واکهٔ فعل با نشانهٔ کوتاه («cavěre») چاپ شده، حال آنکه مصدر صرف دومِ لاتین cavēre با «ای» کشیده است؛ این لغزشِ چاپیِ کتاب است نه خطای خوانش اسکن.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/caution\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewh%E2%82%81-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. keuə-¹ (AHD_watkins1985.txt line 627): '1. Suffixed o-grade form *kous-o- becoming *kaw- in denominative (stative) Latin cavēre, to beware, watch, guard against: CAUTION, CAVEAT; PRECAUTION.' — Nourai's node and its English child in one line.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"Pokorny IEW p.587\",\n              \"stance\": \"supports\",\n              \"note\": \"'lat. caveō, -ēre „sich in acht nehmen, sich vorsehen“ (*covēre, Denom. von *kouos), cautus „vorsichtig“, umbr. kutef wohl „*cautens“, „vorsichtig“.'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. cave, interj. (KLN_1966.txt line ~6864)\",\n              \"stance\": \"supports\",\n              \"note\": \"'cave, interj., beware! — L. cave, imper. of cavēre, „to be on one's guard, take care, beware“, which stands for *covēre and is cogn. with Gk. κοέω (for *κοϝέω), „I mark, perceive“, fr. I.-E. base *(s)qeu-, *(s)qēu-, „to look at, observe“, whence also OE. sceawian, „to look, see, behold“. See show … and cp. esp. caution.'\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck §15.11 PERCEIVE, p.1021 (SYN.txt line 25949)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Grk. κοέω „notice“, Lat. cavēre „be on one's guard, heed“, Grk. ἀκούω, Goth. hausjan „hear“, etc. (15.41). Berneker 162f. Walde-P. 1.369.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"English\",\n          \"words\": \"caveat, caution, precaution\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are Latin-derived: caveat is Latin cavēre's 3rd singular present subjunctive cavea(n)t 'let him beware', taken over unchanged as a legal term (a notice that no action be taken) and generalised to 'warning'; caution comes through Old French caution 'security, surety' from Latin cautiōnem (acc. of cautiō 'wariness'), the abstract to cautus, past participle of cavēre — attested in English c.1300 in the legal sense 'bail, pledge', with 'prudence in regard to danger' only from the 1650s; precaution is French précaution from Late Latin praecautiōnem, to praecavēre 'to guard against beforehand' (prae- + cavēre). Skeat and Watkins group all three under cavēre exactly as the chart does.\",\n          \"derivation_fa\": \"هر سه واژه از لاتین آمده‌اند: «caveat» همان صیغهٔ التزامی سوم‌شخص مفردِ cavēre («بگذار برحذر باشد») است که دست‌نخورده به‌عنوان اصطلاح حقوقی به انگلیسی رفته و سپس معنای عام «هشدار» یافته است؛ «caution» از راه فرانسهٔ کهن از لاتینی cautiōnem (اسم مصدر از cautus، اسم مفعول cavēre) آمده و در انگلیسی از حدود ۱۳۰۰ م. به معنی حقوقیِ «وثیقه، ضمانت» و از دههٔ ۱۶۵۰ به معنی «احتیاط» به‌کار رفته است؛ «precaution» از فرانسوی précaution و آن از لاتینی متأخر praecautiōnem از فعل praecavēre («پیشاپیش پاییدن»، prae- + cavēre) است. اسکیت و واتکینز نیز هر سه را زیر cavēre آورده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/caution\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node has no reference of its own; the parent Latin node's AHD entry (keuə-¹) ends 'Latin cavēre … : CAUTION, CAVEAT; PRECAUTION', i.e. AHD supports precisely this list of three English words.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.vv. caveat, caution, precaution (KLN_1966.txt lines 6868, 6858, 29951)\",\n              \"stance\": \"supports\",\n              \"note\": \"'caveat, n., 1) notice that no action is to be taken (law); 2) a warning. — L., „let him beware“, 3rd p. sing. pres. subj. of cavēre'; 'caution, n. — F., fr. L. cautiōnem, acc. of cautiō, „wariness, carefulness“, fr. cautus, „wary, careful“, pp. of cavēre'; 'precaution, n. — F. précaution, fr. Late L. praecautiōnem … fr. L. praecautus, pp. of praecavēre, „to guard against beforehand“.'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.vv. Caution, Precaution (SKT.txt lines ~3145, ~14700)\",\n              \"stance\": \"supports\",\n              \"note\": \"Skeat cross-refers both words to one head: 'Caution: see Caveat.' and 'Precaution; see Caveat.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"Germanic\",\n          \"words\": \"haujjan; skauuon\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"haujjan : to hear\",\n          \"correct_form\": \"hausjan / Proto-Germanic *hauzjan(ą) (Gothic hausjan)\",\n          \"derivation\": \"The second word is right: Proto-Germanic *skauwōn 'to look at' (Old Saxon skauwōn, Old High German scouwōn, Old English scēawian, Gothic in us-skaws 'circumspect') from the s-mobile variant *skou- of the root — Nourai's 'skauuon' is simply the OS/PGmc form with uu for w, and both AHD ('Germanic *skauwōn in Old English scēawian, to look at: SHOW') and Pokorny print it in that shape. The first word is a misprint: the Germanic verb 'to hear' is *hauzjan-, attested as Gothic hausjan, ON heyra, OE hīeran, OS hōrian, OHG hōr(r)en, from the s-extension *kous- of the root with Verner's-law voicing of the *s. There is no Germanic *haujjan; the -jj- has arisen in the book by dropping the -s- and doubling the glide. AHD, the node's own reference, prints 'Germanic *hausjan'. The printed page (data/verification/sources/refs/ocr/BOOK/263.png) reads 'haujjan', so the fault is the book's and the extraction is faithful. A second, milder point: 'Germanic' here means Proto-Germanic reconstructions, not an attested language, and skauuon is quoted in its Old Saxon shape.\",\n          \"derivation_fa\": \"واژهٔ دوم درست است: ژرمنی آغازین *skauwōn «نگریستن» (ساکسونی کهن skauwōn، آلمانی علیای کهن scouwōn، انگلیسی کهن scēawian، گوتیِ us-skaws «دوراندیش») از گونهٔ s-دارِ ریشه، یعنی *skou-؛ نگارشِ «skauuon» همان صورت است با uu به‌جای w، و واتکینز و پوکورنی نیز آن را به همین شکل آورده‌اند. اما واژهٔ نخست غلط چاپی است: فعلِ ژرمنیِ «شنیدن» *hauzjan- است (گوتی hausjan، نروژی باستان heyra، انگلیسی کهن hīeran، ساکسونی کهن hōrian، آلمانی علیای کهن hōr(r)en) از گسترشِ *kous- ریشه، با واکدارشدنِ *s بر پایهٔ قانون وِرنِر. صورتی به شکل *haujjan در ژرمنی وجود ندارد؛ در کتاب «س» افتاده و غلتان دوتایی شده است. خودِ مرجعِ این خانه، یعنی واتکینز، «Germanic *hausjan» چاپ کرده است. صفحهٔ چاپی «haujjan» دارد، پس این خطای چاپیِ کتاب است نه خطای خوانش اسکن.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/hear\",\n            \"https://www.etymonline.com/word/show\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"contradicts\",\n              \"note\": \"Watkins 1985 s.v. keu-¹ (AHD_watkins1985.txt line 623): '1. Extended form *kous- in: a. Germanic *hausjan in (i) Old English hieran, to hear: HEAR … 2. Variant *skou- in: a. Germanic *skauwōn in (i) Old English scēawian, to look at: SHOW.' The reference has skauwōn as printed but hausjan, not haujjan — so it contradicts the first form of the node.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"Pokorny IEW p.587-588\",\n              \"stance\": \"contradicts\",\n              \"note\": \"p.587: 'got. hausjan, aisl. heyra, ags. hieran, as. hōrian, ahd. hōr(r)en „hören“; dehnstufiges *kēu- in ags. hāwian „schauen“'; p.588: 'got. us-skaws „(*ausschauend =) besonnen“, ags. sceawian, as. skauwōn, ahd. scouwōn „schauen“.' Confirms skauuon, contradicts haujjan.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.vv. hear and show (KLN_1966.txt lines 17351, 35051)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"s.v. hear: 'ME. heren, fr. OE. hīeran, hyran, hēran, rel. to ON. heyra … Goth. hausjan, fr. I.-E. base *(s)qeu-'; s.v. show: 'fr. OE. sceawian … rel. to OS. skauwōn, „to look at“, OFris. skawia, Du. schouwen, OHG. scouwōn.' Klein's Gothic is hausjan.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck §15.41 HEAR p.1035 (SYN.txt line 26189)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"Buck's Germanic column for HEAR reads 'Goth. hausjan, ON heyra, Dan. høre, Sw. höra, OE hīeran, ME here, NE hear, Du. hooren, OHG hōr(r)an, MHG hœren' — hausjan again.\"\n            }\n          ]\n        },\n        {\n          \"id\": 18,\n          \"lang\": \"English\",\n          \"words\": \"hear, show\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"hear < Middle English heren < Old English hīeran (West Saxon) / hēran (Anglian) < Proto-Germanic *hauzjan- (Gothic hausjan) < *kous-, the s-extension of the root; the OE verb already covered 'listen to, obey, follow, judge' as well as 'perceive by ear', and the modern spelling was separated from here between 1200 and 1550. show < Middle English sheuen < Old English scēawian 'to look at, see, gaze, behold' < Proto-Germanic *skauwōjan- < the s-mobile variant *skou-; around 1200 English alone turned the verb causative, 'let be seen, put in sight', and this displaced the older 'look at' within a century — which is why Nourai's Germanic gloss 'to look, show' carries both senses. The pair thus preserves in one modern language the two extensions (*kous- 'hear', *skou- 'see') that the root box heads.\",\n          \"derivation_fa\": \"«hear» از انگلیسی میانهٔ heren و آن از انگلیسی کهنِ hīeran (وسکس) / hēran (انگلی) و آن از ژرمنی آغازین *hauzjan- (گوتی hausjan) از گسترشِ *kous- ریشه است؛ فعل انگلیسی کهن افزون بر «شنیدن» معنای «گوش سپردن، فرمان بردن، داوری کردن» هم داشت. «show» از انگلیسی میانهٔ sheuen و آن از انگلیسی کهنِ scēawian «نگریستن، دیدن» از ژرمنی آغازین *skauwōjan- از گونهٔ s-دارِ *skou- است؛ نکتهٔ چشمگیر آنکه تنها در انگلیسی، حدود سال ۱۲۰۰ م.، این فعل معنای سببی «نشان دادن» یافت و در کمتر از یک سده معنای کهنِ «نگریستن» را کنار زد — و به همین سبب است که نورایی برای صورت ژرمنی هر دو معنی «نگریستن» و «نشان دادن» را آورده است. این دو واژه هر دو گسترشِ ریشه را در یک زبان زنده نگاه داشته‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/hear\",\n            \"https://www.etymonline.com/word/show\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No reference on the node; the parent Germanic node cites AHD, whose keu-¹ entry ends in exactly these two English words ('… Old English hieran, to hear: HEAR'; '… Old English scēawian, to look at: SHOW').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.vv. hear, show (KLN_1966.txt lines 17351, 35051)\",\n              \"stance\": \"supports\",\n              \"note\": \"s.v. show: 'fr. I.-E. base *(s)qeu-, *(s)qēu-, „to look at, observe, perceive“, whence also OI. kaviḥ … Gk. κοέω …, κῦδος …, L. cavēre, „to beware“ … See hear and cp. scavage, scavenger, sheen. Cp. also acoustic, caution, cave, interj., Kavi, kudos' — Klein's two entries link precisely the same set of words Nourai's chart draws.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck §15.41 HEAR p.1035 and §15.52 (SYN.txt lines 26181, 5902)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Goth. hausjan „hear“, OE scēawian „look at“, etc. (15.41, 15.52)' — Buck treats the two English verbs as the two branches of one IE etymon.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T20:53:13.734Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-263.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T20:53:17.792Z] TOOL CALL #86: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-263.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 263"
}
```


### [2026-09-06T20:53:21.103Z] TOOL RESULT

```
JSON OK
nodes verified: 18/18
node verdicts: {'plausible': 3, 'confirmed': 10, 'unverified': 2, 'transcription_suspect': 3}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 10, 'not_checked': 10, 'partial': 2, 'contradicts': 2}
books consulted: {'supports': 28, 'silent': 8, 'contradicts': 5, 'partial': 1} | by book: {'KLN': 10, 'NYB': 4, 'SYN': 4, 'WLD': 3, 'POK': 3, 'SKT': 3, 'BRT': 2, 'CHEUNG': 2, 'MON': 2, 'ARY': 2, 'BOOK': 2, 'PHD': 1, 'FSF': 1, 'HUB': 1, 'IEC': 1, 'KNT': 1}
```


## [2026-09-06T20:53:38.901Z] AGENT

Verification of PDF page 263 (book p. 233) is complete: `/home/sfmqrb/git/rishe/data/verification/page-263.json`. `verify_check.py 263` reports 18/18 nodes, 0 PROBLEM lines.

**Counts** — root: 1 confirmed. Nodes: 10 confirmed, 3 plausible, 3 transcription_suspect, 2 unverified (the two blank boxes #8/#10, which the printed page really does leave empty).

**Flagged items**
- **#9 "Old Persian" au-šaudîhtwei 'to trust' — transcription_suspect (error in the book).** Pokorny 588 and Walde-Pokorny I 370 read `apr. au-schaudītwei "vertrauen"`, where *apr.* = altpreußisch = **Old Prussian** (Baltic). Nourai mis-expanded the abbreviation; the printed page shows "Old Persian", so the extraction is faithful. Aryanpur, working from the same Pokorny page, labels the identical form OLD PRUSSIAN.
- **#11 Greek "akavein" — transcription_suspect (book misprint)** for ἀκούειν *akouein*; Nourai's own reference (AHD keu-¹) prints "Greek akouein". *kudos* in the same node is correct.
- **#17 Germanic "haujjan" — transcription_suspect (book misprint)** for *hausjan* / PGmc *hauzjan- (AHD, Pokorny 587, Klein, Buck all give hausjan). The sister form *skauuon* is correct.
- **#1, #2, #6 — plausible:** the gloss "rich king" for Av. *kāvā-usān* / MP *kayos* is a folk gloss (Bartholomae and Nyberg treat *usan-/usaδan-* as a proper name, cognate with Vedic Uśanas); and Sanskrit *kaví-* means 'wise, seer, poet', never 'sovereign' — that sense is Iranian only.

**Extraction errors for the owner:** none of substance. One cosmetic point: in node #4 the parenthetical Persian extras were merged into a single `script_extra` blob; on the page they belong word-by-word (kay 2 → کیقباد/کیخسرو/کیکاووس, Kâvūs → قابوس, kîyâ → کیانوش, kîyân → کیانی).

**Best confirmations:** ZAW:81 (Bartholomae) and POK:588 support شکوه < *skauaθa- verbatim; WLD:1369 = Walde-Pokorny vol. I p. 369 prints Av. čəvīšī exactly; SOD entry 5072 states "<Av. kavi" for Sogdian qwy; BQT 1749–1751 carries کی/کیا/کیان with Mo'in's Avestan footnote. Unreachable refs: FAF, VOP, MON:3147 (page numbers not mappable online).
