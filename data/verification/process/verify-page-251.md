# Verification process log — verify-page-251


## [2026-09-06T16:03:29.939Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 251 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-251.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-251.json. Write /home/sfmqrb/git/rishe/data/verification/page-251.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 251` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T16:03:31.598Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T16:03:32.460Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T16:03:32.476Z] TOOL RESULT

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


## [2026-09-06T16:03:32.960Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-251.txt"
}
```


### [2026-09-06T16:03:32.978Z] TOOL RESULT

```
1	=== PDF page 251 (book page 221) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kel 3 : to shout, call  (refs POK:548)
4	#1 (parent #0) [Greek] refs=POK:548; AHD:412 | ek-kalein : to call out ; ekklesia : an assembly of people
5	  #2 (parent #1) [Pahlavi] refs=MON:3050 | kilîsyâk : church
6	    #3 (parent #2) [Persian] refs=BQT:1688 | kelîsâ «کلیسا ( کلیسیا )» : church
7	  #4 (parent #1) [Aramaic] refs=TAD:65 | kenušta : assembly of people ; K.n.s, K.n.š : he gathered
8	    #5 (parent #4) [Arabic] refs=SAP:1448 | k.n.s : he gathered, collected, swept ; kanîseh : Jewish temple
9	      #6 (parent #5) [Persian] refs=MON:3105,3096 | kans «کَنس» : sweeping of the house ; kannâs «کَنّاس» : cleaning person ; kanîseh «کَنیسه» : Jewish temple
10	    #7 (parent #4) [Hebrew] refs=KLN:849 | kânas : he gathered ; keneseth : assembly
11	      #8 (parent #7) [Pahlavi] refs=MON:3096 | kanašya : Jewish assembly
12	        #9 (parent #8) [Persian] refs=BQT:1709 | kenešt «کِنِشت ، کَنِشت» : Jewish assembly
13	      #10 (parent #7) [English] refs=AHD:724; KLN:849 | Kneseth : Israeli parliament
14	#11 (parent #0) [Latin] refs=POK:548; AHD | classis : summons, a group of people
15	  #12 (parent #11) [French] refs=AHD:248 | classe
16	    #13 (parent #12) [Persian] refs=MON:3015 | kelâs «کلاس» : class
17	    #14 (parent #12) [English] refs=None | class
18	#15 (parent #0) [Latin] refs=AHD | concilium : a meeting
19	  #16 (parent #15) [French] refs=AHD:303 | concilie : assembly
20	    #17 (parent #16) [Persian] refs=MON:3097 | konsŭl «کنسول ، قونسول» : council, consul
21	    #18 (parent #16) [English] refs=None | council, consul
22	#19 (parent #0) [Latin] refs=AHD | clâmâre : to call ; kalendae : first day of month (for announcements) ; clârus : clear
23	  #20 (parent #19) [English] refs=None | claim, calendar, clear, declare
24	
```


## [2026-09-06T16:03:39.574Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-251.json",
 "description": "Read source JSON for page 251"
}
```


### [2026-09-06T16:03:39.669Z] TOOL RESULT

```
{
  "pdf_page": 251,
  "book_page": 221,
  "entries": [
    {
      "root": {
        "name": "Kel 3",
        "lang": "Indo-European",
        "refs": "POK:548",
        "gloss": "to shout, call"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:548; AHD:412",
          "words": [
            {
              "translit": "ek-kalein",
              "gloss": "to call out",
              "script": null
            },
            {
              "translit": "ekklesia",
              "gloss": "an assembly of people",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "MON:3050",
          "words": [
            {
              "translit": "kilîsyâk",
              "gloss": "church",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1688",
          "words": [
            {
              "translit": "kelîsâ",
              "gloss": "church",
              "script": "کلیسا ( کلیسیا )"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "صلیب و خاج بسوزد کلیسیا بکند - بنای مدرسه بر گنبد گران آرد",
            "poet": "Kamâl Esmâîl"
          }
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Aramaic",
          "refs": "TAD:65",
          "words": [
            {
              "translit": "kenušta",
              "gloss": "assembly of people",
              "script": null
            },
            {
              "translit": "K.n.s, K.n.š",
              "gloss": "he gathered",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Arabic",
          "refs": "SAP:1448",
          "words": [
            {
              "translit": "k.n.s",
              "gloss": "he gathered, collected, swept",
              "script": null
            },
            {
              "translit": "kanîseh",
              "gloss": "Jewish temple",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:3105,3096",
          "words": [
            {
              "translit": "kans",
              "gloss": "sweeping of the house",
              "script": "کَنس"
            },
            {
              "translit": "kannâs",
              "gloss": "cleaning person",
              "script": "کَنّاس"
            },
            {
              "translit": "kanîseh",
              "gloss": "Jewish temple",
              "script": "کَنیسه"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 4,
          "lang": "Hebrew",
          "refs": "KLN:849",
          "words": [
            {
              "translit": "kânas",
              "gloss": "he gathered",
              "script": null
            },
            {
              "translit": "keneseth",
              "gloss": "assembly",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Pahlavi",
          "refs": "MON:3096",
          "words": [
            {
              "translit": "kanašya",
              "gloss": "Jewish assembly",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "BQT:1709",
          "words": [
            {
              "translit": "kenešt",
              "gloss": "Jewish assembly",
              "script": "کِنِشت ، کَنِشت"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "تنها نه منم خانهٔ دل بتکده کرده - در هر قدمی صومعه‌ای هست و کنشتی",
            "poet": "Hâfez"
          }
        },
        {
          "id": 10,
          "parent": 7,
          "lang": "English",
          "refs": "AHD:724; KLN:849",
          "words": [
            {
              "translit": "Kneseth",
              "gloss": "Israeli parliament",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:548; AHD",
          "words": [
            {
              "translit": "classis",
              "gloss": "summons, a group of people",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "French",
          "refs": "AHD:248",
          "words": [
            {
              "translit": "classe",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "MON:3015",
          "words": [
            {
              "translit": "kelâs",
              "gloss": "class",
              "script": "کلاس"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 12,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "class",
              "gloss": null,
              "script": null
            }
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
            {
              "translit": "concilium",
              "gloss": "a meeting",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "French",
          "refs": "AHD:303",
          "words": [
            {
              "translit": "concilie",
              "gloss": "assembly",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "Persian",
          "refs": "MON:3097",
          "words": [
            {
              "translit": "konsŭl",
              "gloss": "council, consul",
              "script": "کنسول ، قونسول"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 16,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "council, consul",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {
              "translit": "clâmâre",
              "gloss": "to call",
              "script": null
            },
            {
              "translit": "kalendae",
              "gloss": "first day of month (for announcements)",
              "script": null
            },
            {
              "translit": "clârus",
              "gloss": "clear",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 19,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "claim, calendar, clear, declare",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-06T16:03:39.857Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T16:03:39.894Z] TOOL RESULT

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


## [2026-09-06T16:04:04.749Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','MON','BQT','TAD','SAP','KLN','LEW','LAT','AFA','FVQ','SKT','FSD','WEB','PLA','ARY','LKT','AKD','IEC','SYN','WLD','PHD','NYB','HRN','HUB']:\n    v=d.get(k)\n    print('---',k, json.dumps(v,ensure_ascii=False)[:900] if v else 'MISSING')\n\""
}
```


### [2026-09-06T16:04:07.149Z] TOOL RESULT

```
--- POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
--- AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
--- MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
--- BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
--- TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"], "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the pa
--- SAP {"title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989", "kind": "purchase", "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample", "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side content, not Sayyah's pages).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only. Google Books no-view records 4yQPAQAAMAAJ (1977), NoplAAAAMAAJ (1985), HcGipwAACAAJ (2001)."}
--- KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
--- LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.", "notes": ""}
--- LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_
--- AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Arabic/Aramaic in script (not OCRed) with German glosses; grep the German meaning or transliteration.", "notes": "Built from djvu.xml."}
--- FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)", "covers_etymology": true, "notes": "Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.", "cites": "page number of Jeffery, The Foreign Vocabulary of the Qurʾān (19
--- SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.", "notes": "Nourai says '1882-1967'; the
--- FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leave
--- WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword bold at line start; e
--- PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py P
--- ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1
--- LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.", "notes": "", "cites": "entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)"}
--- AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt", "page_offset": "leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by semantic field; Akkadian words in transliteration with Aramaic/Arabic/Persian loans. grep the word.", "notes": "39 citations; check that the 1st-ed. page is within a page or two of Nourai's."}
--- IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": "", "cites": "column/page number of Mann, An Indo-Europea
--- SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head
--- WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_
--- PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsian
--- NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.", "notes": " local_files: /home/sfmqrb/
--- HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
--- HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", "notes": "Built from djvu.xml (no hocr); OCR quality moderate.", "cites": "page number of Hübschmann, Persische Studien (1895)"
```


## [2026-09-06T16:04:11.748Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==557' POK_01.txt | head -80"
}
```


## [2026-09-06T16:04:11.829Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kelə-\\|kel-\\b\" POK_01.txt | sed -n '1,60p'"
}
```


### [2026-09-06T16:04:14.209Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-06T16:04:14.258Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:04:16.373Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"== $f $(wc -c <$f) bytes, $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f) pages\"; done"
}
```


### [2026-09-06T16:04:18.059Z] TOOL RESULT

```
== POK_01.txt 981836 bytes, 363 pages
== POK_02.txt 1137861 bytes, 433 pages
== POK_03.txt 1170809 bytes, 429 pages
== POK_full.txt 3971883 bytes, 1 pages
```


## [2026-09-06T16:04:20.591Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 204 205 206; do echo \"=== NR=$n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' POK_02.txt | head -60; done"
}
```


### [2026-09-06T16:04:22.129Z] TOOL RESULT

```
=== NR=204 ===
ngl.  auch  hulvir,  anord.  hulfr  ds. ;
aksl.  klas^  ,Ähre'  (,die  Stechende*),  russ.  kölos  =  alb.  kall  ds.,  kashte (*kallshte)y  Jokl  IF.  36,  124,  , Stroh,  Spreu*  (-s-Formans  dann  wie  in  hüls)  ;
alb.  (Jokl  IF.  37,  95)  re-kuall  ,Distel*  (*per-kel  ,Durchstich,  Stachel*).
g(h)-ETW.  in  mir.  colg  , Schwert,  Granne  der  Gerste,  Stachel*,  acyrar. colginn  ,aristam*,  ncymr.  cola  , Granne*,  col  , Spitze,  Granne*,  colyn  ,Stachel*, cal,  cala,  caly  ,penis*,  bret.  kalc'h  ds.  Auf  Grund  keltischer  Formen nehmen  Meillet  MSL.  14,  374,  Kretschmer  KZ.  38,  lOOf.  auch  eine  gleich- bed.  Wurzel  kjfel-  ,stecken,  graben'  an:  cymr.  palu  ,graben*^,  pal,  corn. bret.  pal , Spaten'  (aus  lat.  päla  ?  freilich  fraglich  wegen  ligur.  pala  ,Grab*, cymr.  paladr  ,hastile*,  auch  ,Balken,  Strahl*).
kol-no-s  in  ai.  känd-h  , durchstochen,  durchlöchert^  einäugig*  (*kolno-] zum  ä  vgl.  Wackernagel  Ai.  Gr.  I  168)  ==  air.  (acymr.  ?)  coli  ,luscum, einäugig*,  mir.  (mit  sekundärer  Media)  goll  ,blind*;  ablautend  gr.  yisXldg- ^ovdcpd-aXuog  Hes.
WP.  I  435.
j.  kel-,  kel9-f  klä-,  erweitert  kläd-  ,schlagen,  hauen*;   kläro-  m.   , Holz- stück, Brett*,  klädo-  , Abgehauenes,  Ausgestochenes*,  Icoio- , geschlagen*, koldo-,  gebrochen*,  kldo-  , Gespaltenes* ;  Trennung  von  kel-  , stechen* und  von  skel-  ,schneiden*  ist  kaum  durchführbar;   beachte  bes.  slav. *kolti  , stechen*  =  balt.  kalti  , schlagen*. Gr.  y.sXs6g  (*y,eX£j^6g)  , Grünspecht*  (wie  ÖQVKoXdcTZTrjg) ;  yislsl'g '  d^lvr]  Hes. ; neXoL  ,?t;Aa*  nach  Hes.  unter  ytsXeovrag ]  diy.slXa  ,zweizinkige  Hacke*;  vgl. aycaXlg   ,Hacke'   unter   skel-  ,schneiden*;    xöXog  ,verstümmelt,   ungehörnt*, xöX-ovQog  ,mit  gestutztem  Schwänze*,  ytoXa^o)  ,verstümmle,  hindere ;  züchtige*, y.oXov(o  ,verstümmle;  hemme';  yioXsToäv  , treten*;
mit  Formans  -bo-  :y,oXoß6g  ^verstümmelt*  (vgl.  auch  die  Wurzelf.  *k(e)lemb-)j mit  Formans  -bho-:  xöXaq)og  ,Ohrfeige,  Backenstreich*,  davon  abgeleitet 'KoXdjrTü)  ,behaue,  behacke*,
von  der  schweren  Basis  xAc^w  ,breche*  (ytXäüü),  exXäaa,  äno^Xag,  xXaaTÖg), Tdaaig  ,das  Brechen,  Beschneiden  der  Zweige*,  xXda^  ^Bruchstück*,  xXfjfia n.  ,Zweig;  Weinranke,  -rebe',  Demin.  vliq^arig  bes.  PI.  ,Reisig';  %XfiQog, dor.  vXäqog  m.  ,Holzstückchen  als  Los,  Los,  Anteil'  (=  air.  cZär,  cymr. clawr  jBrett,  Tafel',  bret.  kleur  , Gabelbaum  am  Wagen') ;
35
546
T
ytX(bv,  Tilcjvög  m.  ^Schößling,  Trieb,  Reis',  xAwy«xö'  qctßdov  Hes.,  xAcuvßj. yCkädog  Hes.  (nähere  Verwandtschaft  mit:  aisl.  hlunnr  , Rollwalzen  fti^. Fahrzeuge*,  hlu(m)mr  ,der  obere  dicke  Teil  des  Ruders*  aus  *hlunma-'^) —  Aö
=== NR=205 ===
jfia^,  -ayiog  m.  , Steinhaufen,  Felsen*;
lat.  calamüas  ,Schaden*  (von  *calamo-  aus  *calimo-,  idg.  *kgle-mo-  ,ge, schlagen'),  dazu  incolumis  ,unversehrt* ;  ferner  aus  *kel-nö  :  jpercellö,  ^cuU ,schlage  zu  Boden,  zerschmettere*,  se  procellere  ,sich  hinwerfen',  procella f.  »heftiger  Sturm*,  recellö  ,schnelle  zurück' ;  nicht  *kel-dö  wegen  des  gall. GN  Su-cellus  ,guter  Schläger*;
air.  dar  usw.  s.  oben   S.  545;
lit.  kalü,  kdltij  lett.  kal'u,  kalu,  kalt  »schlagen,  schmieden',  lit.  päkalag^ , Sensenkeil',  prie-,  prei-kälas  ,Ambos',  apr.  kalo-peilis  , Hackmesser',  Ht. kdltas  ,Meißel',  apr.  calte  ,Mark  (Münze)',  d.  i.  ,geschlagenes  =  geprägtes Geld',  lit.  kdlvis  , Schmied',  Kausativ  lit.  kdldinti  ,schmieden  (lassen)', lett.  kcddtt  ds. ;  lit.  kuliü,  külti  , dreschen',  lett.  kul'u,  külu,  kult  ,schlagen, prügeln,  dreschen^;  lit.  kelmas  ^Baumstumpfs,  kann  auch  ^geschnitten,  ge- spalten^  sein;
abg.  usw.  koljg  klaii  ^stechen,  schlachten^  (a-bg.  auch  ,opfern*),  russ. kolöth  ^stechen,  schlachten;  spalten,  hacken^;  abg.  koh  ,Pflock',  russ.  koi^ Gen.  koid  ,Stange,  Pfahl',  ablaut.  *kzh  in  klr.  koi  (Gen.  kia)  ,Eckzahn^ Hauzahn',  sloven.  kel  (Gen.  klä)-,  öech.  klanice  ,StangeS,  poln.  kionica , Seitenholz  am  Wagen^  (auf  Partiz.  *kolno-  zu  klati  beruhend);  serb. kldto  ,Art  Halsjoch  für  Schweine^,  6ech.  kldt  ,Baumstumpf,  Klotz,  Knüppel' (=  lit.  kdltas  s.  oben);  ksl.  pro-kleju,  -kUti  ,keimenS,  russ.  (usw.)  klin  ,KeiP (Bildung  wie  mlim  zu  meljg);  unsicher  sI&y..  *kolt-jgj  -iti  in  abg.  klaStq,  _ klatiti  ,bewegen,  schütteln,  stoßen^,  russ.  koloM,  kolotit  ,schlagen,  klopfen; plappern^  usw.;   ob  dazu  tiefstufig  r.  koltdttsja  ,sich  bewegen,  wackeln'?
d- Er  Weiterung  kelod-,  kläd-:
Gr.  TiXaöaQÖg  (^khdjos)  ,zerbrechlich ;  abgelebt',  yLXaö&aai  *  astaai  Hes.,. ablaut.  T^aladia '  Qvxdvr]  Hes.,  xXdöog  m.  ,Zweig',  kons.  c2-St.  *xXdg,  yddöeai usw.   ds.,  yiXadcjVj  -ovog  Hes.   ds.,  -alaardta)  ,beschneide  den  Weinstock';.
lat.  clädes  f.  ,Verletzung;  Schaden,  Unheil,  Niederlage^;
mir.  claidim  ,grabe'  (mit  ad-  ,verfolgen,  jagen,  fischen^  usw.),  cymr^ claddu,  bret.  claza  ,graben',  mir.  clad,  cymr.  cladd  ,Graben';  dehnstufig cymr.  clawdd,  com.  claud  ,Graben',  bret.  Ä:Zew2  , Graben,  Hecke'  (*klädo-)'f cymr.  cleddyf  ,Schwert',  bret.  kleze  ,Schwert,  Klinge^  {cleddyf  diss.  aus *cledyd,  kelt.  *kladios),  ir.  claideb  ist  Lw.  aus  dem  Cymr.,  lat.  gladiu» aus  dem  Kelt.;
mir.  caill  (Gen.  caille)  ,Wald',  cymr.  celli  ,Walds,  com.  kelli  ,nemus^ (kelt.  *kaldi)]
i
547
air.  cymr.  coli,  bret.  koll  ^Verderben^  Scbaden';  mir.  cellach  ,Krieg^ und  die  damit  verwandten  aisl.  hüdr  f.  ^Kampf,  Kampfgöttin',  as.  ags. jiild  ^Kampf,  Krieg',  ahd.  h
=== NR=206 ===
iltia,  Jiilta  ^Kampf  Laben  idg.  -dh-  und  wohl schlagen;,  dreinhauen'  als  Grundbed. ;
got.  halts,  aisl.  haltr,  ags.  healt,  ahd.  Jialz  ,lahm'  (=  air.  coli]  Grundbed. ^gebrochen');  etwa  zunächst  von  gebrochenen  Gliedmaßen;
aisl.  ags.  holt^  ahd.  holz  ,Holz,  Wald'  (=  'Älädog),  dazu  aisl.  hjalt  n. ^Schwertgriff',  ags.  Mit  f.  ds.,  ahd.  helza  , Schwertgriff,  Heft',  as.  helta ^Handgriff  am  Ruder*;
abg.  klada  ,Balken,  Block',  russ.  kolöda  ,Holzblock,  Klotz,  Baumstamm, von  einem  Stamme  abgehauenes  Stück'  usw. ;  ksl.  kladivo  ,Hammer' (ursl.  *kläd- :  lat.  clädes).
Labialerweiterung:
klon2b(h)o-  in:  gr.  nXai^ßög  ,verstümmelt',  ags.  laempi-halty  lamp-healt ;,hinkend'  (Specht  Idg.  Dekl.  262);  vgl.  lit.  klumbas  ,lahm'.
WP.  I  436  ff.,  WH.  I  135  f.,  225  f.,  691,  Specht  Idg.  Dekl.  130  f.,  262, 322,  Trautmann  114  f.
4.  kel-  und  käl-  in  den  Worten  für  helle  und  dunkle  Flecken,  graue  und  schwärz- liche Farbentöne;  kel-zno-  ,Fleck';  vgl.  auch  3.  ker-  und  1.  kers-.
I.  Ai.  kalaidka-  m.  ,Fleck,  Rost',  kalana-  n.  ,Fleck,  Schmutz',  kdlusa- ,schmutzig,  schwarz',  kalmasa-  m.  ,Fleck,  Schmutz',  kalmäsa-  ,bunt,  ge- sprenkelt'; mit  Formans  -ko-i  karkd-  ,weiß',  m.  ,Schimmel^,  karkl  vaiä , weiße  Kuh',  karkä  ,weiße  Stute'  (Persson  Beitr.  169),  kalkd-  m.  ,Kot,  Dreck', cäsa-  m.  ,der  blaue  Holzhäher'  (*kel-so-)]
npers.  carma  , Schimmel',  kurd.  Öerme  ,weiß'  (:  Schweiz,  helm)-^
gr.  'Ks'kaLvoq  ,schwarz',  y.iXl6g  ,grau',  yiiXkog  ,Esel'  und  ,Zikade'  (Vokal wie  in  Ttilvög  neben  nekLÖg-^  -H- aus -Av- ?) ;  sehr  wahrscheinlich  x(5At'^/?og (*kolu-mbhos)  ,Taucher  (Vogelart)',  wovon  yiolvfißdo)  ,tauche',  von  der dunklen  Farbe  genannt;  hierher  auch  y.iXX-ovQog  ,Bachstelze'  Hes. ;
lat.  columha  f.,  -us  m.  ,Taube(r)'  aus  *kol-on-bho-  oder  *kolu-mhho- ,  dann identisch   mit  -/.oXvfxßog]    zum  -mh-  aus  -mhh-  s.  Schwyzer  Gr.  Gr.  I  333;
nhd.  Schweiz,  heim  ,weißer  Fleck  beim  Vieh  auf  der  Stirn',  helme ,Name  einer  Kuh  mit  weißgeflecktem  Kopf,  schwed.  dial.  hjälm  ,blässiger Ochs  oder  blässiges  Pferd'  (vgl.  zum  m-Formans  ai.  kalmasa-)]  wahr- scheinlich mhd.  Mlwe  f.  ,feiner  Nebel',  bair.  gehilb  ,Nebel,  Herdrauch'  {^-w- in  Beziehung  zum  u  von  ai.  kdlusa-h),  wozu  ahd.  huliwa  ,uligo,  sordes limi  vel  aquae',  mhd.  hülwe  ,Pfütze,  Pfuhl,  Sumpflache'  im  Ablaut  steht;
hierher  (von  den  schwarzen  Beeren)  auch  ahd.  holuntar,  holantar ,Holunder',  aschwed.  hylle  ds. ;  s.  Berneker  473  m.  Lit.,  der  auch  für  russ. kalina  ,Viburnum  opulus'  Zugehörigkeit  zu  kah  (s.  unten)  erwägt.
35*
548  f
II.  Wurzelform  käl-  :  kdl-  (mit  unklarem  Verhältnis  zu  kel-) : .  Gr.   yirjXtg,   -löog   (dor.    y,älig)    ^Fleck^,    ycrjXMoj    ^beflecke,    beschmutze', yc7}lr)vi)-  fieXaiva  Hes.,   ycrjXdg'  ve
```


## [2026-09-06T16:04:26.423Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 207 208; do echo \"=== NR=$n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' POK_02.txt; done"
}
```


### [2026-09-06T16:04:28.023Z] TOOL RESULT

```
=== NR=207 ===
cpelt]  ävvöoog  y,at  xeiiiSQivt}  '^^leqa'  y,al  cc|§^ fJTLg  ytarä  rd  ^hwrtov  aiqixsLOv  e%si  xvlosLÖeg  Hes. ;
lat.  cälidus,  calUdus  (Gl.)  ,weißstirni^  *(von  Pferden)'  =  umbr.  kalef-uf (huf)  ,calIidos  (boves)^;  lat.  caligo  f.  ,Nebel,  Finsternis^;
air.  caile,  mir.  gaile  ,Fleck';
lit.  kalyhasj  kalyvas  ^weißhalsig^ ;
aksi.  kah  jTtrjlögj  Kot*^  mit  den  Bedeutungen  ^Sumpf,  Morast,  mit  Kot beschmutzen^ ;  dazu  (nach  der  Farbe)  russ.  kalina  ,Viburnum  opulus^,  wie auch  sloven.  kalina  ,Pfütze^   und  russ.  kalü-ga  ^Morast^,  kalu-za  ,Lache'.
WP.  I  440ff.,  WH.  I  139 f.,  249,  Specht  Idg.  Dekl.  118,  140,  143==, Trautmann  113  f.,  Petersson  Heterokl.  146  f.
5.  kel-  ,treiben,  zu  schneller  Bewegung  antreibend
Ai.  kUldyati  ,treibt,  trägt,  nimmt  wahr,  hält' ;
alb.  geg.  qilj  sizil.  qel  ,bringe,  trage^,  shqütse  ,Lab,  d.  i.  co-agulum^, wohl  auch  kal  ,stifte,  stelle  an^  (Jokl  IF,  30,  198);
gr.  xsXXü)  ,treibe  (das  Schiff  ans  Land);  lande^  (Präs.  nur  bei  Gramm, und  in  d-^sXX(jü  trans.  ,treibe  das  Schiff  ans  Land;  strande,  scheitere^; sonst  nur  Aor.  Fut.  ey^XacXj  -/.eXact)),  y-iXrjgj  -rjTog  ,Renner  (Pferd);  schnell- segelndes Schiff' ;  y,X6vog  ,heftige  Bewegung',  'AXoveo)  ,vor  sich  her  treiben' (vgl.  d^Q-övog,  %Q-6vog ;  Boisacq  s.  v.  m.  Lit.) ;  vielleicht  (Persson  Beitr.  179) y.oXbiv'  iX&stv  und  xoAior,  xoXia  ,Art  Tanz'  Hes.;
lat.  celer  , schnell,  rasch^  (wie  y,eXrjg)y  celeber,  -bris,  -bre  ,betrieben,  be- fahren (via),  "belebt  {locus,  oppidum),  häufig,  gefeiert'  (*kele-dhlo-,  -dhli-)]
als  ^Präs.  got.  haldan  ,Vieh  weiden^  (zum  a-Vok.  s.  Brugmann  IF.  32, 181),  ahd.  haltan  ,hüten,  halten',  as.  haldan,  ags.  healdan,  aisl.  halda, aschwed.  halla  (*halpan)  ,halten',  mnd.  hilde,  kille  ,rasch,  eifrig'^.
WP.  I  442f.,  WH.  I'l94f.;  wohl  identisch  mit  6.  kel--,  s.  auch  keleu- ,wandern^.
6,  kel-,  k(c)le-,  k{e)l^-  oder  kl-7  ,rufen,  schreien,  lärmen,  klingend
Ai.  usä-kala-  m.  ,Hahn'  (j^t-xaydg'),  kalädhika-,  kalävika-  ds~kala- vitdka-  ,Sperling',  kala-  ,leise  tönend,  undeutlich  vernehmbar',  kalakala- m.  ,verworrenes  Geschrei,  Geräusch';
gr.  %aXs(a  (statt  *xaAw)  ,rufe,  nenne,  rufe  herbei^  (äol.  ycdXrjfML),  Futur. xaXeaü)^  att.  naXw,  Perf.  xixXjjTtay  ycXrjTÖg;  inUXriaig  ,BeinameS  vXfiaig ,Ruf,  Einladung,  Vorladung',  ^XriTrig,  yi(a)Xrjru}Q  ,Rufer',  df^oxXrj  ,Zuruf' (zum  1.  Glied  s.  unter  om9-);   Tuydrjaxü)  (oder  xixAi^'crxw)  ,rufe  an,  flehe^.
549
yclrjt^oi,  xlfj^ü)  ;,nemie^  (*xA?;-/«-g-£^co ?) ;  hochstufig-  x5A(a)-  in  yielofuai  ^treibe an  (durch  Zurufy,
=== NR=208 ===
  hom.  Aor.  (i)'H€y,XeTO,  dor.  xfVro  =  (I^xs^to;  [über  y.eXsvü) s.  unter  kleu-]]  ycslaovLu)  _,rausche;  riesle  (Wasser  u.  dgl.y,  tisXwq'  cpcüvrj Hes. ;  Erweiterung  neXadog  , Getöse^  Lärm^,  xeXdöcov,  yisXadetvög  ,brausend% neXadiio  ^tose;  lasse  (einen  Gesang)  erklingen^;
umbr.  kafitu,  kafetu,  carsitu  ^calato^  appellato^  {*kaletöd) ;  daß  ein  ent- sprechendes lat.  *caleö  einst  in  der  Ausruf ungsformel  der  Kalenderdaten J)ies  te  quinque,  bzw.  Septem,  calo,  luno  Covella  gestanden  habe  und  daß calendae  ^der  erste  Tag  des  Monats^  von  diesem  Ausrufen  benannt  sei, ist  wahrscheinlich  (Salonius  Z.  röm.  Dat.  1  ff.) ;
lat.  calöy  -äre  ^Ausrufen^  Zusammenrufen^  (:  lett.  kaVuot),  calätor ,Rufer_,  Ausrufer^,  nömen-cläior  ^Namennenner^  (aus  nömen  caläre  rückge- bildet), calähra  {curia)  ,die  zum  Ausrufen  der  Kalenderdaten  bestimmte Kurie^,  vielleicht  concilium  ^Zusammenkunft,  Versammlung,  Vereinigung" von  Dingen,  geschlechtliche  Verbindung^  (*cön-caliom),  con-ciliäre  ,ver- einigen,  verbinden,  gewinnen  usw.',  clämö,  -äre  ,rufen^  (vgl.  ahd.  hlamön usw.),  clämor  ,Schrei^,  clärus  ,lauttönend,  fernhin  schallend;  berühmt; klar^,  umbr.  anglar  Nom.  PL,  anglaf  Akk.  PL  ,oscines^  (^an-klä  ,avis inclamansQ;  lat.  classis  ,Aufgebot:  Heer,  Flotte;  Klasse,  Abteilung^  (*klad- ti-:  TieXaöog?)]
air.  cailech,  ogam  Gen.  caliäcl,  cymr.  ceiliog,  corn.  chelioc  ,Hahn' (*kaljäkos) ;
ags.  hlöwan  ,rugire,  boare^,  ahd.  {}i)löian,  (h)luoen^  mhd.  lüejen  ,brüllen^; ags.  hletan  ,grunzen%*  ahd.  hluoticla  ,latratus^;  mit  Hochstufe  der  ersten Silbe  ahd.  hei  ,laut,  tönend'  (nhd.  hell  ,glänzend'),  hellan  ,ertönen',  mhd. hal  ,Hall,  Schall',  anord.  hjala  ,schwatzen',  hjal  n.  , Geschwätz',  hjaldr ,Gespräch,  Kampfgetöse,  Kampf;  afries.  halia  ,herbeiholen,  heimführen, nehmen',  ags.  geholian  ,bekommen',  asächs.  halön  ,berufen,  herbeibringen', ahd.  halön  und  ablaut.  holön,  holen  ,rufen,  holen',  ndd.  halen  ,ziehen'.
lett.  kaVuot  ,schwatzen'  {kalada  ,Geschrei,  Lärm'  ist  russ.  Lw.),  lit. kalhä  ,Sprache',  apr.  kaltzä,  kelsäi  ,sie  lauten'  (lit.  *kalsöti)]  redupl.  lit. kankalas  (*kalkalas)  ,Schelle',  aksl.  klakoh,  russ.  kölokoh  ,Glocke',  kolo- kölith  , läuten,  klingen;  schwätzen,  klatschen',  Trautmann  BsL  Wb.  115.
hitt.  sa-ra-a  kal-li-is-ta  (sarä  kallesta)  ,rief  (lockte)  herauf.
Erweiterung  *k(e)len2-  (vgl.  lat.  clä-m-äre) :  ai.  Ä:raw<^aii , schreit,  brüllt, wiehert'  (*klem-d-?)]  ags.  hlimman,  hlymman  ,klingen,  tönen,  rauschen, brüllen',  hlimme  ,reißende
```


## [2026-09-06T16:04:33.237Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"ecclesia\\|kela-\\|kel\\b.*shout\\|to shout\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-06T16:04:33.297Z] TOOL RESULT

```
606:small hollow: HAUGH; e. Dutch holster, holster, (< “that which covers”): HOLSTER. 2. Suffixed Germanic form *hulfti- in Medieval Latin hultia, protective covering: HOUSING?. 3. Suffixed form *kl-to- in Latin occultus (see III. 5. below). 4. Extended form *kld (< *kl-) in Latin clam, in secret: CLANDESTINE. 5. Suffixed variant form *kal-up-yo- in Greek kaluptein, to cover, conceal: Ca- LYPSO, CALYPTRA; APOCALYPSE, EUCALYPTUS. III. Full-grade form *kel-. 1. Germanic *helmaz, “‘protec- tive covering,” in: a. Old English helm, protection, cover- ing: HELM?; b. Frankish *helm, helmet, akin to the source of Middle English helmet, helmet: HELMET. 2. Latin occulere (part participle occultus; see Il. 4. above), to cover over (ob-, over; see epi): OCCULT. 3. Suf- fixed form *kel-os- in Latin color, color, hue (< “that which covers”): COLOR. 4. Suffixed form *kel-nd in Latin cella, storeroom, chamber: CELL, CELLA, CELLAR, CELLARER; (RATHSKELLER). 5. Suffixed form *kel-yo- in Latin cilium, lower eyelid: CILIUM, SEEL; SUPERCILIOUS, (SUPERCILIUM). IV. Lengthened-grade form *kél-d- in Latin céldre, to hide: CONCEAL. See extension klep-. [Pok. 4. kel- 553.] kel-3. To drive, set in swift motion. Hypothetical base of various loosely connected derivatives. 1. Extended form *kelt- or *keldh- possibly in Germanic *haldan, to drive flocks, keep or pasture cattle, in: a. Old English healdan, to hold, retain: HOLD!; b. Old High German haltan, to stop, hold back: HALT!; c. Middle Dutch houden, to hold: AVAST. 2. Suffixed form*kel-es- in: a. Latin celer, swift: CELERITY; ACCELERATE; b. possibly further suffixed form *keles-ri- in Latin celeber, (of a place) much fre- quented, hence famous: CELEBRATE, CELEBRITY. 3. Suf- fixed zero-grade form *kl-on- in Greek klonos, turmoil, agitation: CLONUS. [Pok. 5. kel- 548.] kel-4. To lean, tilt. Germanic *halthjan in Old English hieldan, to tilt: HEEL2. [Pok. 2. kel- 552.] kel-5. Gray, black, dark. Suffixed form *kel-omb(h)- in Latin columba, dove, pigeon: COLUMBA, COLUMBARIUM, COLUMBINE, CULVER. [Pok. 4. kel- 547.] kel-*, To be prominent; hill. 1. Zero-grade form *k/- in: a. suffixed Germanic form hul-ni- in Old English hyll, hill: HILL; b. suffixed Germanic form *hul-ma- in Old Norse holmr, islet in a bay, meadow: HOLM. 2. Suffixed form *kel-d- in Latin excellere, to raise up, elevate, also to be eminent (ex-, up out of; see eghs): EXCEL. 3. O-grade form *kol- in: a. Greek kolophén, summit: COLOPHON; b. suffixed form *kol(u)men- in Latin culmen, top, summit: CULMINATE; C. extended and suffixed form *kolumna in Latin columna, a projecting object, column: COLONEL, COLONNADE, COLUMN. [Pok. 1. kel- 544.] kel-7. To prick. Germanic *hulin- in Old English holen, holly (from its spiny leaves): HOLLY. [Pok. 2. kel- 545.] kel-®. To deceive, trick. Extended form *kelu-, variant *kalu-, in: a. Latin calvi, to deceive, trick: CALUMNY, CHALLENGE; b. Latin cavilla (< *calvilla), a jeering: CAVIL. [Pok. Rél- 551.] kelb-. To help. Germanic *helpan in Old English helpan, to help: HELP. [Pok. kelb- 554.] kele-1. Warm. Variant *klé-, contracted from *kleo-. 1. Suffixed variant form *k/é-wo- in Germanic *hléwaz in Old English hléo, hléow, covering, protection (as from cold): LEE. 2. Suffixed zero-grade form *kip-é- in: a. Lat- in calére, to be warm: CALENTURE, CHAFE; DECALES- CENCE, NONCHALANT, RECALESCENCE; Db. Latin derivative adjective calidus, warm (> French chaud, warm): CALDRON, CAUDLE, (CHOWDER); CHAUDFROID, SCALD'. 3, Suffixed zero-grade form *fl-os- in Latin calor, heat: CALORIC, CALORIE; CALORECEPTOR, CALO- RIFIC, CALORIMETER, CALORIMETRY. [Pok. 1. kel- 551.] kele-2. To shout. I. Variant form *kld- (< *klaa-). 1. Ger- manic Aljé- in Old English hléwan, to roar, low: Low?. 2. Suffixed form *k/d-mé- in Latin clamare, to call, cry out: CLAIM, CLAMANT, CLAMOR; ACCLAIM, DECLAIM, EXCLAIM, PROCLAIM, RECLAIM. II. O-grade form *kob-.
608:Germanic *hal6n, to call, in: a. Dutch halen, to haul, pull (2? < “to call together, summon”): KEELHAUL; b. Old French haler, to haul: HALE?, HAUL. ITI. Zero-grade form *klo- (> *kal-). 1. Suffixed form *kal-yo- in Latin conct- lium, a meeting, gathering (< “a calling together”; con-, together; see kom): CONCILIATE, COUNCIL. 2. Suffixed form *kal-énd- in Latin kalendae, the calends, the first day of the month, when it was publicly announced on which days the nones and ides of that month would fall: CALENDAR, CALENDS. 3. Suffixed form *kal-e- in Greek kalein (variant klé-), to call: ECcLESIA, PARACLETE. 4. Suffixed form *kal-d- in Latin caldre, to call, call out: INTERCALATE, NOMENCLATOR. 5. Suffixed form *klp-ro- or suffixed variant form *klaa-ro- contracted to *kld-ro- in Latin clarus, bright, clear: CLEAR, GLAIR; CHIARO- SCURO, CLAIRVOYANCE, DECLARE, ECLAIR, ECLAIRISSE- MENT. IV. Possibly extended zero-grade form *kid-, becoming *klad- in suffixed form *klad-ti- in Latin classis, summons, division of citizens for military draft, hence army, fleet, also class in general: cLAss. [Pok. 6. kel- 548.] kelp-. To hold, grasp. O-grade form *kolp- in Germanic *halb- in: a. Old English hielfe, handle: HELVE; b. suf- fixed form *halb-ma- in (i) Old English helma, rudder, tiller: HELM! (ii) Middle High German helm, handle: HALBERD; C. suffixed form *half-tra- in Old English helftre, halter: HALTER}. [In Pok. 1. (s)kel- 923.] kem-1, Hornless. 1. Germanic *skamm- in Old Norse skammr, “hornless,” short: SCANT. 2. Suffixed form *kem-tydé in Germanic *hinthj6 in Old English hind, doe: HIND?, [Pok. 2. kem- 556.] kem-?. To compress. Germanic *hamjam, a compressing, hence a doubling, in Old English hem/(m), a doubling over, a hem: HEMI, [Pok. 1. kem- 555.] kem-3. To hum. Germanic *hum- in Middle English hummen, to hum: HUM. [Pok. 2. kem- 556.] keme-. To be tired, to tire. Suffixed lengthened o-grade form *kém-n proposed by some as the preform of Greek k6ma, deep sleep, which is more likely of obscure origin: coma}. [Pok. 4. kem(g)- 557.] ken-'. To be active. 1. Suffixed o-grade form *kon-o- in Greek diakonos, servant, attendant (dia-, thoroughly): DEACON. 2. Lengthened o-grade form *kdén-d- in Latin condari, to endeavor: CONATION. [Pok. 4. ken- 564.] ken-2. Hypothetical base of a number of loosely related Germanic words referring to pinching, closing the eyes, and other obscurely associated notions. 1. Old English hnappian, to doze, nap: NAP!. 2. Old English népfléd, neap tide (fléd, tide; see pleu-): NEAP TIDE. 3. Middle Dutch nipen, to bite: n1P!. 4. Old Norse hnéggr, miserly, akin to the Scandinavian source of Middle English nigard, miser: NIGGARD. 5. Middle Dutch noppe, pile: NAP?. 6. Low German nibbein, to nibble: NIBBLE. 7. Mid- dle High German notten, to nod, perhaps akin to Middle English nodden, to nod: Nop. [Pok. 2. ken- 559.] ken-3, Fresh, new, young. 1. Suffixed form *ken-t- in Latin recens, young, fresh, new (re-, again; see re-): RECENT. 2. Suffixed zero-grade form kn-yo- in Greek kainos, new, fresh (> kainotés, newness): -CENE; CAINO- TOPHOBIA, CENOGENESIS, CENOZOIC, KAINITE. [Pok. 3. ken- 563.] ken-4, Empty. Suffixed form *ken-wo- in Greek kenos (< *kenwos), empty: KENOSIS; CENOTAPH. [Pok. ken- 564.] ken-5, Hypothetical base of several roots associated with the notions “to compress,” “something compressed.” 1. Germanic root *hnekk-, “neck” (a narrow or com- pressed part), in: a. Old English hnecca, neck: NECK; b. Old Norse hnakkur, saddle, and Old Norse hnakki, back of the neck, perhaps akin to the source of KNACKER. 2. Root *knu-, nut (< “small hard object”), in: a. extend- ed form *knud- in Old English hnutu, nut: NUT; b. ex- tended form *knuk- in Latin nux, nut: NEWEL, NOUGAT, NUCELLUS, NUCLEUS. 3. Germanic root *hnukk-, sharp projection, tip, in: a. Middle Dutch nocke, tip of a bow,
621:hréc, rook: RooK!. 4. Germanic *hraban, *hrabnaz, raven, in Old English hrefn, raven: RAVEN}. 5. Extended form *krep- in Latin crepdre, to crack, burst, creak: CREPITATE, CREVICE; DECREPIT, DECREPITATE, QUEBRA- cHo. 6. Extended form *kri- in Germanic *krik- in Old French criquer, to creak, click: CRICKET!. II. Variant form *skr-. 1.Germanic *skrik- in Old English scric, thrush: SHRIKE. 2. Germanic *skrékjan- in Old Norse skrekja, to shriek: SCREAK, SCREECH. 3. Germanic *skrainjan, to shout, shriek, in Old Norse screma, to scream, perhaps akin to the possible Scandinavian source of Middle English scremen, to scream: SCREAM. III. O-grade form *kor-. 1. Latin corvus, raven: CORBEL, CORBINA, CORMORANT, CORVINE, Corvus. 2. Greek ko- rax, raven (> korakias, chough): CORACIIFORM, CORA- com. [Pok. 1. ker- 567.] ker-3. To grow. 1. Suffixed form *ker-es- in Latin Cerés, goddess of agriculture, especially the growth of grain: CEREAL, CERES. 2. Extended form *kré- (< *krea-) in: a. suffixed form *kré-yd- in Latin credre, to bring forth, create, produce (< “to cause to grow”): CREATE, CREOLE; PROCREATE; b. suffixed form *kré-sko- in Latin créscere, to grow, increase: CRESCENDO, CRESCENT, CREW!; AC- CRUE, CONCRESCENCE, CONCRETE, DECREASE, EXCRES- CENCE, INCREASE, RECRUIT. 3. Suffixed o-grade form *kor-wo-, “growing,” adolescent, in Greek kouros, koros, boy, son: DIOSCURI, HYPOCORISM. 4. Compound *sm-kéro-, “of one growth” (*sm-, same, one; see sem-'), in Latin sincérus, pure, clean: SINCERE. [Pok. 2. ker- 577.) ker-4, Heat, fire. 1. Suffixed form *ker-té in Germanic *herthé in Old English heorth, hearth: HEARTH. 2. Zero-grade form *kr- in: a. Latin carbé, charcoal, ember: CARBON, CARBUNCLE; b. extended form *krem- in Latin cremdre, to burn: CREMATE. 3. Possibly suffixed and extended form *kera-mo- in Greek keramos, potter’s clay, earthenware: CERAMIC. 4. Possibly variant ex- tended form *krds- in Russian krasa, beauty (< “bril- liance of fire”): CRASH?. [Pok. 3. ker(a)- 571.] ker-5. Also kere-. To injure. Suffixed zero-grade form *kro-yé- in Latin cariés, decay, caries: CARIES. [Pok. 4. her- 578.] ker-8. A kind of cherry. 1. Suffixed zero-grade form *kr-no- in Latin cornus, cornel tree: CORNEL. 2. Full- grade form *ker- probably in Greek kerasos, cherry: CHERRY. [Pok. 4. ker- 572.] kerd-', Heart. 1. Suffixed form *kerd-en- in Germanic *hertén- in Old English heorte, heart: HEART. 2. Zero-grade form *krd- in: a. Latin cor (stem cord-), heart: CORDATE, CORDIAL, COURAGE, QUARRY!; ACCORD, CONCORD, CORDIFORM, DISCORD, MISERICORD, RECORD; b. suffixed form *krd-yd- in Greek kardia, heart, stom- ach, orifice: CARDIA, CARDIAC, CARDIO-; DIPLOCARDIAC, ENDOCARDIUM, EPICARDIUM, MEGALOCARDIA, MYOCAR- DIUM, PERICARDIUM. 3. Possibly *kred-dha-, “‘to place trust” (an old religious term; *dho-, to do, place; see dhé-'), in Latin crédere, to believe: CREDENCE, CREDI- BLE, CREDIT, CREDO, CREDULOUS, GRANT; MISCREANT, RECREANT. [Pok. kered- 579.] kerd-2. Craft. Suffixed form *kerd-d in Old Irish cerd, art, artist: CAIRD. [Pok. 2. kerd- 579.] kerdh-. Row, herd. Suffixed form *kerdh-d@ in Germanic *herdo in Old English heord, herd: HERD. [Pok. kerdho- 579.] kere-. To mix, confuse, cook. 1. Variant form *kra- (< *kraa-) in Germanic *hrdr- in: a. possibly Old English hrér, lightly boiled, half-cooked: RARE?; b. Middle Dutch roer, motion: UPROAR. 2. Zero-grade form “krp- in: a. suffixed form *kro-ti- in Greek krasis, a mixing: IDIOSYNCRACY; b. suffixed form *kro-ter- in Greek kra- ter, mixing vessel: CRATER. [Pok. hero- 582.] kerp-. To gather, pluck, harvest. Variant karp-. 1. Ger- manic *harbistaz in Old English herfest, harvest: HAR- VEST. 2. Latin carpere, to pluck: CARPET; EXCERPT,
785:neu-'. To shout. Suffixed (participial) o-grade form *now-ent-(yo-), “shouting,” in Latin niintius, “announc- ing,” hence a messenger, also a message, and ndéntium, message: NUNCIO; ANNOUNCE, DENOUNCE, ENUNCIATE, PRONOUNCE, RENOUNCE. [Pok. 1. neu: 767.] neu-2, To nod. 1. Latin *nuere, to nod (attested only in compounds), frequentative nutdre, to nod: NUTATION; INNUENDO. 2. Suffixed form *neu-men- in Latin niimen, “a nod,” hence “command,” divine power, deity: NUMEN. [Pok. 2. neu- 767.] neud-. To make use of, enjoy. Germanic *nautam, “thing of value, possession,” in: a. Old English néat, bovine
1331:CALM kéu- CALOMEL kal-2 CALORECEPTOR kela-! CALORIC kele-! CALORIE kele-1 CALORIFIC kela-1 CALORIMETER kela-1 CALORIMETRY kela-1 CALOYER gere-!, kal-2 CALUMET kolem- CALUMNY kel-8 CALVARIUM klewo- CaLypso_ kel CALYPTRA kel-2 CALYX kal-1
1389:cons deuk- CONATION ken-1 CONCAVE keue-2 CONCEAL kel-2 CONCEDE ked- CONCEIVE kap- CONCERN krei- CONCESSION ked- CONCH konk(h)o- CONCHA konk(h)o- CONCHO- konk(h)o- CONCIERGE servus CONCILIATE kela-2 CONCISE kae-id- CONCLAVE kleu-3 CONCLUDE kleu-3 CONCOCT pekw- CONCOMITANT ei-1 CONCORD kerd-1 CONCOURSE kers-2 CONCRESCENCE ker-3 CONCRETE ker-3 CONCUBINE keu-2 CONCUPISCENCE kwép- CONCUR kers-2 CONCUSS kwét- CONDEMN dap- CONDENSE dens-2 CONDESCEND skand- CONDIGN dek-1 CONDIMENT dhé-1 CONDITION deik- CONDOLE del-3 CONDONE do- CONDOTTIERE deuk- CONDUCE deuk- CONDUCT deuk- CONDUPLICATE dwo- CONE k6-
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
1485:EXAMINE ag- EXAMPLE em- EXANTHEMA andh- EXARCH arkhein EXCALIBUR kal-3 EXCAVATE keue-2 EXCEED ked- EXCEL kel-6 EXCEPT kap- EXCERPT kerp- EXCISE? kae-id- EXCITE kei-3 EXCLAIM kela-2 EXCLUDE kleu-3 EXCORIATE sker-1 EXCREMENT krei- EXCRESCENCE ker-3 EXCURSION kers-2 EXECRATE Sak- EXECUTE sekw-1 EXEDRA sed-1 EXEGESIS sag- EXEMPLARY em- EXEMPLIFY em- EXEMPLUM em- EXEMPT em- EXERCISE arek- EXERGONIC werg- EXERGUE werg- EXERT ser-3 EXFOLIATE bhel-3 EXHAUST aus-2 EXHIBIT ghabh- EXHILARATE sel-2 EXHORT gher-5 EXHUME dhghem- EXIGENT ag-
1682:INTER en, ters- INTERCALATE kela-2 INTERCEDE ked- INTERCEPT kap- INTERCOSTAL kost- INTERCOURSE kers-2 INTERDICT deik- INTEREST es- INTERIM en INTERIOR en INTERJECT yé- INTERLOCUTION  tolkw- INTERLOPE klou- INTERLUDE leid- INTERMEDIATE medhyo- INTERMIT (S)meit(a)- INTERNAL en INTERNECINE nek-1 INTERPELLATE pel-6 INTERPOSE apo- INTERPRET per-68 INTERREX reg-1 INTERROGATE reg-1 INTERRUPT reup- INTERSECT sek- INTERSPERSE (s)preg- INTERSTICE sta- INTERVAL walso- INTERVENE gWa- INTERVIEW weid- INTESTINE en INTIMA en INTIMATE? en INTINCTION  teng- INTINE en
1768:Low? kela-2
1930:NODE ned- NODULE ned- NODUS ned- NOEL gene- NOESIS nous NOISE nau-2 NOISOME od-2 NOMA nem- NOMAD nem- NOMBRIL nobh- NOME nem- ie NOMENCLATOR kela-2, no-men- NOMINAL no-men- NOMINATE no-men- NOMOGRAM nem- NOMOGRAPH nem-
1932:NONAGENARIAN dekm, newn NONAGON newn NONANOIC ACID newn NONCHALANT kela-1 NONE ne, oi-no- NONES newn NONJUROR yewes- NONPAREIL pera-2 NONPLUS_ pele-1 NOOK ken-5
2225:SCHISM skei- SCHIST skei- SCHIZO-  skei- SCHIZONT es- SCHLEP |leij- SCHLIEREN sleu- SCHLOCK | slak- SCHMALTZ mel-1 SCHMEER (s)mer-3 SCHMUCK meug-2 SCHNAUZER snu- SCHNITZEL sneit- SCHNORRER sner- SCHNOZZLE snu- SCHOLAR segh- SCHOLASTIC segh- SCHOLIUM segh- SCHOOL! segh- SCHOOL? §skel-1 SCHUss skeud- SCIENCE skei- SCILICET skei- SCINTILLA skeei- SCINTILLATE skeei- SCIOLISM skei- SCION géi-1 SCIRE FACIAS dhé-1, skei- SCISSION  skei- SCISSORS kae-id- SCLERA skele- SCLERO- skele- SCLEROMA §skela- SCLEROSIS skela- SCLEROTIC skelo- SCLEROTIUM skela- SCLEROTIZATION skela- SCLEROUS skelo- SCOFF skeubh- SCOLD sekw-3 SCOLEX skel-3 SCOLIOSIS skel-3 SCONCE? dhé-1 SCONE keu-! SCOOP skep- Scop skeubh- -SCOPE spek- -SCOPY spek- SCORCH skerbh- SCORE sker-1 SCORIA_ sker-4 scoT skeud- SCOT AND LOT skeud- SCOTOMA  skot- SCOUR! cira SCOUR2 kéwero- SCOURGE reig-1 SCOUT! ous- scouT? skeud- SCRABBLE  sker-! SCRAG gWere-4 SCRAP!  sker-1 SCRAPE sker-1 SCRATCH grat- SCREAK ker-2 SCREAM ker-2 SCREECH ker-2 SCREED skreu- SCREEN sker-1 SCREW sker-! SCRIBBLE skribh- SCRIBE skribh- SCRIMP_ skerbh- SCRIPT skribh- SCRIPTORIUM skribh- ScRIPTURE  skribh- SCROBICULATE sker-1 SCROD skreu- SCROFULA  sker-1 SCROLL skreu- SCROTUM skreu- SCRUB!  sker-1 SCRUTINY skreu- SCUDO skei- SCUFF skeubh- SCUFFLE! skeubh- SCUFFLE? skeubh- SCULPTURE skel-1 SCUM (s)keu- SCUTCH kwét- SCUTTLE! skeud- SCUTUM  skei- SCYPHISTOMA skep-, ste-men- SCYPHOZOAN skep- SCYTHE sek- SEAL! sekw-1 SEAL? selk- SEAM syi- SEANCE sed-! SEAR! saus-
```


## [2026-09-06T16:04:34.143Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"classis\\|clamare\\|calendae\\|concilium\\|ecclesia\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-06T16:04:34.236Z] TOOL RESULT

```
606:small hollow: HAUGH; e. Dutch holster, holster, (< “that which covers”): HOLSTER. 2. Suffixed Germanic form *hulfti- in Medieval Latin hultia, protective covering: HOUSING?. 3. Suffixed form *kl-to- in Latin occultus (see III. 5. below). 4. Extended form *kld (< *kl-) in Latin clam, in secret: CLANDESTINE. 5. Suffixed variant form *kal-up-yo- in Greek kaluptein, to cover, conceal: Ca- LYPSO, CALYPTRA; APOCALYPSE, EUCALYPTUS. III. Full-grade form *kel-. 1. Germanic *helmaz, “‘protec- tive covering,” in: a. Old English helm, protection, cover- ing: HELM?; b. Frankish *helm, helmet, akin to the source of Middle English helmet, helmet: HELMET. 2. Latin occulere (part participle occultus; see Il. 4. above), to cover over (ob-, over; see epi): OCCULT. 3. Suf- fixed form *kel-os- in Latin color, color, hue (< “that which covers”): COLOR. 4. Suffixed form *kel-nd in Latin cella, storeroom, chamber: CELL, CELLA, CELLAR, CELLARER; (RATHSKELLER). 5. Suffixed form *kel-yo- in Latin cilium, lower eyelid: CILIUM, SEEL; SUPERCILIOUS, (SUPERCILIUM). IV. Lengthened-grade form *kél-d- in Latin céldre, to hide: CONCEAL. See extension klep-. [Pok. 4. kel- 553.] kel-3. To drive, set in swift motion. Hypothetical base of various loosely connected derivatives. 1. Extended form *kelt- or *keldh- possibly in Germanic *haldan, to drive flocks, keep or pasture cattle, in: a. Old English healdan, to hold, retain: HOLD!; b. Old High German haltan, to stop, hold back: HALT!; c. Middle Dutch houden, to hold: AVAST. 2. Suffixed form*kel-es- in: a. Latin celer, swift: CELERITY; ACCELERATE; b. possibly further suffixed form *keles-ri- in Latin celeber, (of a place) much fre- quented, hence famous: CELEBRATE, CELEBRITY. 3. Suf- fixed zero-grade form *kl-on- in Greek klonos, turmoil, agitation: CLONUS. [Pok. 5. kel- 548.] kel-4. To lean, tilt. Germanic *halthjan in Old English hieldan, to tilt: HEEL2. [Pok. 2. kel- 552.] kel-5. Gray, black, dark. Suffixed form *kel-omb(h)- in Latin columba, dove, pigeon: COLUMBA, COLUMBARIUM, COLUMBINE, CULVER. [Pok. 4. kel- 547.] kel-*, To be prominent; hill. 1. Zero-grade form *k/- in: a. suffixed Germanic form hul-ni- in Old English hyll, hill: HILL; b. suffixed Germanic form *hul-ma- in Old Norse holmr, islet in a bay, meadow: HOLM. 2. Suffixed form *kel-d- in Latin excellere, to raise up, elevate, also to be eminent (ex-, up out of; see eghs): EXCEL. 3. O-grade form *kol- in: a. Greek kolophén, summit: COLOPHON; b. suffixed form *kol(u)men- in Latin culmen, top, summit: CULMINATE; C. extended and suffixed form *kolumna in Latin columna, a projecting object, column: COLONEL, COLONNADE, COLUMN. [Pok. 1. kel- 544.] kel-7. To prick. Germanic *hulin- in Old English holen, holly (from its spiny leaves): HOLLY. [Pok. 2. kel- 545.] kel-®. To deceive, trick. Extended form *kelu-, variant *kalu-, in: a. Latin calvi, to deceive, trick: CALUMNY, CHALLENGE; b. Latin cavilla (< *calvilla), a jeering: CAVIL. [Pok. Rél- 551.] kelb-. To help. Germanic *helpan in Old English helpan, to help: HELP. [Pok. kelb- 554.] kele-1. Warm. Variant *klé-, contracted from *kleo-. 1. Suffixed variant form *k/é-wo- in Germanic *hléwaz in Old English hléo, hléow, covering, protection (as from cold): LEE. 2. Suffixed zero-grade form *kip-é- in: a. Lat- in calére, to be warm: CALENTURE, CHAFE; DECALES- CENCE, NONCHALANT, RECALESCENCE; Db. Latin derivative adjective calidus, warm (> French chaud, warm): CALDRON, CAUDLE, (CHOWDER); CHAUDFROID, SCALD'. 3, Suffixed zero-grade form *fl-os- in Latin calor, heat: CALORIC, CALORIE; CALORECEPTOR, CALO- RIFIC, CALORIMETER, CALORIMETRY. [Pok. 1. kel- 551.] kele-2. To shout. I. Variant form *kld- (< *klaa-). 1. Ger- manic Aljé- in Old English hléwan, to roar, low: Low?. 2. Suffixed form *k/d-mé- in Latin clamare, to call, cry out: CLAIM, CLAMANT, CLAMOR; ACCLAIM, DECLAIM, EXCLAIM, PROCLAIM, RECLAIM. II. O-grade form *kob-.
608:Germanic *hal6n, to call, in: a. Dutch halen, to haul, pull (2? < “to call together, summon”): KEELHAUL; b. Old French haler, to haul: HALE?, HAUL. ITI. Zero-grade form *klo- (> *kal-). 1. Suffixed form *kal-yo- in Latin conct- lium, a meeting, gathering (< “a calling together”; con-, together; see kom): CONCILIATE, COUNCIL. 2. Suffixed form *kal-énd- in Latin kalendae, the calends, the first day of the month, when it was publicly announced on which days the nones and ides of that month would fall: CALENDAR, CALENDS. 3. Suffixed form *kal-e- in Greek kalein (variant klé-), to call: ECcLESIA, PARACLETE. 4. Suffixed form *kal-d- in Latin caldre, to call, call out: INTERCALATE, NOMENCLATOR. 5. Suffixed form *klp-ro- or suffixed variant form *klaa-ro- contracted to *kld-ro- in Latin clarus, bright, clear: CLEAR, GLAIR; CHIARO- SCURO, CLAIRVOYANCE, DECLARE, ECLAIR, ECLAIRISSE- MENT. IV. Possibly extended zero-grade form *kid-, becoming *klad- in suffixed form *klad-ti- in Latin classis, summons, division of citizens for military draft, hence army, fleet, also class in general: cLAss. [Pok. 6. kel- 548.] kelp-. To hold, grasp. O-grade form *kolp- in Germanic *halb- in: a. Old English hielfe, handle: HELVE; b. suf- fixed form *halb-ma- in (i) Old English helma, rudder, tiller: HELM! (ii) Middle High German helm, handle: HALBERD; C. suffixed form *half-tra- in Old English helftre, halter: HALTER}. [In Pok. 1. (s)kel- 923.] kem-1, Hornless. 1. Germanic *skamm- in Old Norse skammr, “hornless,” short: SCANT. 2. Suffixed form *kem-tydé in Germanic *hinthj6 in Old English hind, doe: HIND?, [Pok. 2. kem- 556.] kem-?. To compress. Germanic *hamjam, a compressing, hence a doubling, in Old English hem/(m), a doubling over, a hem: HEMI, [Pok. 1. kem- 555.] kem-3. To hum. Germanic *hum- in Middle English hummen, to hum: HUM. [Pok. 2. kem- 556.] keme-. To be tired, to tire. Suffixed lengthened o-grade form *kém-n proposed by some as the preform of Greek k6ma, deep sleep, which is more likely of obscure origin: coma}. [Pok. 4. kem(g)- 557.] ken-'. To be active. 1. Suffixed o-grade form *kon-o- in Greek diakonos, servant, attendant (dia-, thoroughly): DEACON. 2. Lengthened o-grade form *kdén-d- in Latin condari, to endeavor: CONATION. [Pok. 4. ken- 564.] ken-2. Hypothetical base of a number of loosely related Germanic words referring to pinching, closing the eyes, and other obscurely associated notions. 1. Old English hnappian, to doze, nap: NAP!. 2. Old English népfléd, neap tide (fléd, tide; see pleu-): NEAP TIDE. 3. Middle Dutch nipen, to bite: n1P!. 4. Old Norse hnéggr, miserly, akin to the Scandinavian source of Middle English nigard, miser: NIGGARD. 5. Middle Dutch noppe, pile: NAP?. 6. Low German nibbein, to nibble: NIBBLE. 7. Mid- dle High German notten, to nod, perhaps akin to Middle English nodden, to nod: Nop. [Pok. 2. ken- 559.] ken-3, Fresh, new, young. 1. Suffixed form *ken-t- in Latin recens, young, fresh, new (re-, again; see re-): RECENT. 2. Suffixed zero-grade form kn-yo- in Greek kainos, new, fresh (> kainotés, newness): -CENE; CAINO- TOPHOBIA, CENOGENESIS, CENOZOIC, KAINITE. [Pok. 3. ken- 563.] ken-4, Empty. Suffixed form *ken-wo- in Greek kenos (< *kenwos), empty: KENOSIS; CENOTAPH. [Pok. ken- 564.] ken-5, Hypothetical base of several roots associated with the notions “to compress,” “something compressed.” 1. Germanic root *hnekk-, “neck” (a narrow or com- pressed part), in: a. Old English hnecca, neck: NECK; b. Old Norse hnakkur, saddle, and Old Norse hnakki, back of the neck, perhaps akin to the source of KNACKER. 2. Root *knu-, nut (< “small hard object”), in: a. extend- ed form *knud- in Old English hnutu, nut: NUT; b. ex- tended form *knuk- in Latin nux, nut: NEWEL, NOUGAT, NUCELLUS, NUCLEUS. 3. Germanic root *hnukk-, sharp projection, tip, in: a. Middle Dutch nocke, tip of a bow,
```


## [2026-09-06T16:04:43.869Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -on \"CONSUL[A-Z]* [a-zé-]*-\\?[0-9]*\" AHD_watkins1985.txt | head -10; echo ---; grep -n \"COUNCIL\" AHD_watkins1985.txt | head -5 | cut -c1-200"
}
```


### [2026-09-06T16:04:43.965Z] TOOL RESULT

```
1707:CONSULT yewes-
---
608:Germanic *hal6n, to call, in: a. Dutch halen, to haul, pull (2? < “to call together, summon”): KEELHAUL; b. Old French haler, to haul: HALE?, HAUL. ITI. Zero-grade form *klo- (> *kal-). 1. Suf
1396:COTE! ku- COTTAGE ku- COUCH GRASS gVei- COULEE kagh- COULOIR kagh- COUNCIL kele-2 COUNT! peu- COUNT? ei-t COUNTER! kom COUNTER- kom COUNTERFEIT dhé-1 COUNTERMAND man-2 COUNTERVAIL wal- COUNTRY k
```


## [2026-09-06T16:04:44.024Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"consul\" LEW_1910.txt | head -20"
}
```


### [2026-09-06T16:04:44.082Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:04:50.455Z] TOOL CALL #15: Bash

```json
{
 "command": "ls site/pages/251.jpg 2>/dev/null; pdftoppm -f 251 -l 251 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg251 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T16:04:52.794Z] TOOL RESULT

```
site/pages/251.jpg
total 9320
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 12:04 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    1100 Sep  6 12:04 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  180887 Sep  6 11:56 bqt1637_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50592 Sep  6 11:56 bqt1637_kaz.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67391 Sep  6 11:49 build225.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71757 Sep  6 11:47 build232.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49952 Sep  6 11:57 build234b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   32265 Sep  6 11:51 build234.py
-rw-rw-r-- 1 sfmqrb sfmqrb   24770 Sep  6 12:01 build243.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  6 11:28 c224_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3203 Sep  6 11:28 c224_n7.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:27 c229_bibua.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5308 Sep  6 11:27 c229_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5313 Sep  6 11:27 c229_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9059 Sep  6 11:50 c237_n18.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2389 Sep  6 11:50 c237_n3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4987 Sep  6 11:52 c239_kandid2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4734 Sep  6 11:52 c239_kandid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12852 Sep  6 11:52 c239_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4087 Sep  6 11:52 c239_sandarus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   15240 Sep  6 11:54 c246_caiique.png
-rw-rw-r-- 1 sfmqrb sfmqrb   36354 Sep  6 12:02 c246_casaque.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84366 Sep  6 11:54 c246_n2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51690 Sep  6 11:54 c246_n6.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13719 Sep  6 12:02 c248_p3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   30759 Sep  6 12:02 c248_p4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2750 Sep  6 12:02 c248_persian2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3046 Sep  6 12:02 c248_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12347 Sep  6 11:20 c_hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12691 Sep  6 11:20 c_ieuo.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2071 Sep  6 11:26 c_ijlak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14654 Sep  6 11:20 c_ijlak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12239 Sep  6 11:20 c_latis.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169482 Sep  6 11:58 crop_1648b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45260 Sep  6 11:57 crop_1648.png
-rw-rw-r-- 1 sfmqrb sfmqrb  305924 Sep  6 11:57 crop_1731.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb  111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83691 Sep  6 11:19 gen215.py
-rw-rw-r-- 1 sfmqrb sfmqrb    2303 Sep  6 11:25 j.json
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb   77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67513 Sep  6 11:27 mk217.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74459 Sep  6 11:33 mk218b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17605 Sep  6 11:25 mk218.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50138 Sep  6 11:24 mk222.py
-rw-rw-r-- 1 sfmqrb sfmqrb   78297 Sep  6 11:32 mk223.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47928 Sep  6 11:38 mk224.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53093 Sep  6 11:40 mk226.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51303 Sep  6 11:39 mk228.py
-rw-rw-r-- 1 sfmqrb sfmqrb   29152 Sep  6 11:37 mk229.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47535 Sep  6 11:47 mk230.py
-rw-rw-r-- 1 sfmqrb sfmqrb   64267 Sep  6 11:59 mk235.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73422 Sep  6 12:02 mk237.py
-rw-rw-r-- 1 sfmqrb sfmqrb   81037 Sep  6 12:03 mk240.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:52 p233
-rw-rw-r-- 1 sfmqrb sfmqrb   33321 Sep  6 11:51 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb  141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb  194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb  147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71937 Sep  6 11:19 pg219.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb  118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb   90848 Sep  6 11:22 pg224hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55412 Sep  6 11:15 pg224.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80963 Sep  6 11:32 pg225.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161218 Sep  6 11:26 pg226hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74322 Sep  6 11:19 pg226.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54381 Sep  6 11:31 pg227.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52519 Sep  6 11:25 pg228.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78760 Sep  6 11:27 pg229hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42112 Sep  6 11:26 pg229.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65310 Sep  6 11:32 pg230.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69894 Sep  6 11:34 pg231.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67111 Sep  6 11:35 pg233.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82071 Sep  6 11:44 pg234.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47149 Sep  6 11:44 pg236.png
-rw-rw-r-- 1 sfmqrb sfmqrb  125593 Sep  6 11:50 pg237hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67972 Sep  6 11:50 pg237.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168221 Sep  6 11:52 pg239hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81026 Sep  6 12:03 pg239.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83594 Sep  6 12:03 pg239_small.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81131 Sep  6 11:51 pg240.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97613 Sep  6 11:49 pg242.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80947 Sep  6 11:59 pg244.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80632 Sep  6 11:55 pg245.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79253 Sep  6 11:54 pg246.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64208 Sep  6 12:04 pg247.png
-rw-rw-r-- 1 sfmqrb sfmqrb  142780 Sep  6 12:02 pg248hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49887 Sep  6 12:02 pg248.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75263 Sep  6 12:04 pg251.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   53545 Sep  6 12:03 w241.py
```


## [2026-09-06T16:04:55.546Z] TOOL CALL #16: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg251.png"
}
```


### [2026-09-06T16:04:55.985Z] TOOL RESULT

```

```


## [2026-09-06T16:04:55.982Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T16:05:16.600Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN 1966 knesset/kanas ===\"; grep -n -i \"kneseth\\|knesset\\|kanas\\|k^enesth\\|keneseth\" KLN_1966.txt | head -20; echo \"=== KLN ecclesia ===\"; grep -n -i \"ecclesia,\" KLN_1966.txt | head -5 | cut -c1-400"
}
```


### [2026-09-06T16:05:16.680Z] TOOL RESULT

```
=== KLN 1966 knesset/kanas ===
17579:Tj-aTixit;,  ‘of  the  liver’,  fr.  •SjTOxp,  gen.  TjmxToi;, ‘liver’,  fr.  I.-E.  base  *ylqw-r(t),  gen.  yeqw-nis, whence  also  OI.  ydkpt,  gen.  yaknah,  Avestic yakar1,  MPers.  jakar,  ModPers .jigar,  L.  jecur, OLith.  jeknos,  jekanas,  Lith.  jaknos  (pi.),  Lett. aknas,  aknis  (pi.),  ‘liver’.  Cp.  hepar,  heparin, jecoral.
20769:knar,  n.,  a  knot  in  wood.  —  ME.  knarre;  rel.  to  Kneseth,  n.,  the  Israeli  Parliament.  —  Mishnaic MHG.  gnarren,  knarren,  G.  knarren,  ‘to  creak,  Heb.  keneseth,  ‘gathering,  assembly’  (cp.  beth
20771:knave,  n.,  1 )  a  boy,  a  servant  (archaic) ;  2)  a  rascal ;  from  the  stem  of  Heb.  kanas,  ‘he  gathered,  as-
37843:synagogical,  adj.  —  See  synagogue  and  -ical. synagogue,  synagog,  n.  —  ME.  synagoge,  fr.  OF. sinagoge  (F.  synagogue),  fr.  Late  L.  synagoga,  fr. Gk.  auvavciiyir],  ‘assembly,  synagogue’,  lit.  ‘a bringing  together’,  fr.  ouvaystv,  ‘to  lead  or  bring together’,  which  is  formed  fr.  auv  (see  syn-)  and Syciv,  ‘to  lead’.  See  agent,  adj.,  and  cp.  agon¬ istic.  Gk.  auvaycoyr;  is  prop,  a  loan  translation of  Heb.  keneselh ,  ‘assembly’  (whence  beth  ke- neseth,  ‘synagogue’)  (lit.  ‘house  of  assembly’), fr.  kdnas,  ‘he  assembled'.  Cp.  Kneseth. synallagmatic,  adj.,  expressing  reciprocal  obliga¬ tions.  —  Gk.  auvaXXaypaxixo;,  fr.  auvaX- Xavpa,  gen.  auvaXXdyuxxo;,  ‘covenant,  con¬ tract’,  fr.  auv  (see  syn-)  and  SXXaypx,  ‘a  thing taken  in  exchange’,  from  the  stem  of  aXXaaaeiv, ‘to  exchange,  barter’,  prop,  ‘to  make  other  than it  is’,  fr.  aXXo;,  ‘another’,  which  is  cogn.  with  L. alius,  of  s.m.  See  else  and  cp.  alias.  For  the  end¬ ing  see  adj.  suff.  -ic.
=== KLN ecclesia ===
12590:ecchymosis,  n.,  extravasation  of  blood  (med.)  — Medical  L„  fr.  Gk.  IxyjVoou;,  ‘bruise,  extra¬ vasation’,  lit.  ‘a  pouring  out’,  fr.  Ixxupoua^ai, ‘to  pour  out,  extravasate’,  fr.  lx  (see  ec-)  and yynto',  ‘juice’.  See  chyme  and  -osis. ecclesia,  n.,  1)  assembly  of  citizens  in  ancient Athens;  2)  a  church.  —  L.  ecclesia,  ‘assembl
```


## [2026-09-06T16:05:17.534Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ===\"; grep -n -i \"klys\\|kilis\\|church\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n -i \"kanis\\|klys\\|church\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T16:05:17.604Z] TOOL RESULT

```
=== PHD ===
=== NYB ===
1256:én apčcak ~ i mäzdesn 244; veh ~ 4 apčcak 5914; (En) apécak veh ~ 4 maz- desnān 819. 844; ~ i Ohurmazd 60%; ~ stayitan, ~ yastan: v. these ws; — in particular: the authoritative canonical texts of this religion: én ~, cigon hamäk apastak u zand namely, the whole Avesta and commentary 1078; the quotations from these texts are introduced by the following formula: cigén ~ göbet followed by ku 3613-14, 421-13, 4520, 4615, 484-18, 491-16. 5224, 53%. 541-17; followed by hat (q. v.) 387-8. 4375-26, 4414-15, 503-5; without following particle 41196; (7) cigon et i ~ gobet ku 5323-24, 563. 581. 608. 617-8; cigon pat ~ 7718, pat hàn i ~ göbet kū 4345; andar ~ guft estet 8011; an-ic ~ gobet ku 3819; hac ~ (čičn) paitäk kü 341. 8612-115; cigón hac apécak veh- ~ i mäzdesnän paitäk 819-9; v. further paitäk and paitakéh; v. also s.v. dipivareh. — Av. (662 sqq.) daenä-; Arm. lw. den; MPrthPrs dyn religion, religious community, church; Paz. din. — Cf ak-dénéh, dén-burtàr, denik, dušden, huden.
2199:ibd.; 222, 422-71 passim; 971; 14-16 pas- sim. — MPrs knycg; NP kanizah. Dimin. of kanik; v. also kanisk. (Ps. 122% knysky, v. Barr s.v.).
2205:"kanisk [knysky] female slave SPrs: 16, perhaps coll. — Reading and phonetical development not quite clear.
```


## [2026-09-06T16:05:25.574Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i,p in enumerate(pages):\n    if 'Kneseth,  n.,  the  Israeli' in p:\n        print('leaf',i,'printed p ~',(i-12)*2)\n        # print context\n        j=p.find('knar,')\n        print(p[j:j+1600])\n        break\nEOF"
}
```


### [2026-09-06T16:05:27.294Z] TOOL RESULT

```
leaf 457 printed p ~ 890
knar,  n.,  a  knot  in  wood.  —  ME.  knarre;  rel.  to  Kneseth,  n.,  the  Israeli  Parliament.  —  Mishnaic MHG.  gnarren,  knarren,  G.  knarren,  ‘to  creak,  Heb.  keneseth,  ‘gathering,  assembly’  (cp.  beth
rattle’,  and  to  E.  gnarl  (q.v.)  Cp.  knur,  knurl.  klneseth,  ‘synagogue’  lit.  ‘house  of  assembly’),
knave,  n.,  1 )  a  boy,  a  servant  (archaic) ;  2)  a  rascal ;  from  the  stem  of  Heb.  kanas,  ‘he  gathered,  as-
3)  a  playing  card;  the  jack.  —  ME.  knaue  sembled,  collected’,  which  is  rel.  to  Aram.
(=  knave),  ‘boy,  servant,  knave’,  fr.  OE.  crtafa,  klnash,  ‘he  gathered,  assembled,  collected’
‘boy,  youth,  servant’,  rel.  to  OHG.  knabo,  ‘boy,  (whence  be  kfnishtd,  ‘synagogue’,  lit.  ‘house  of
youth,  servant’,  MHG.,  G.  knabe,  ‘boy,  lad’,  assembly’).
and  to  OE.  cnapa,  ‘boy,  youth,  servant’,  ON.  knew,  past  tense  of  know.  —  ME.  knew,  fr.  OE. knapi,  ‘servant  boy’,  MLG.  k/iqpe,  ODu.  knapo,  endow,  ‘he  knew’,  past  tense  of  cnawan.  See
MDu.  knape,  Du.  knaap,  ‘a  youth,  servant’,  know.
OHG.  knappo,  MHG.  knappe,  ‘a  young  squire’,  knez,  kniaz,  n.,  a  Slavonic  title.  —  Russ,  knyaz', G.  Knappe,  ‘squire,  shieldbearer,  attendant’.  The  ‘prince’,  fr.  OSlav.  kunfgu,  kun?zi,  of  s.m.,  of
orig.  meaning  of  these  words  prob.  was  ‘stick,  Teut.  origin.  Cp.  OHG.,  OS.  kuning,  kunig,
peg,  piece  of  wood’;  cp.  dial.  G.  Knabe  and  dial.  ‘king’,  and  see  king.
Swed.  knabb,  knappe,  ‘peg’,  ON.  knefill,  ‘cross-  Knickerbocker,  n.,  a  desc
```


## [2026-09-06T16:05:36.957Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i in range(454,460):\n    p=pages[i]\n    nums=re.findall(r'\\b(8[0-9]{2}|9[0-9]{2})\\b',p)\n    print(i, p[:60].replace('\\n',' '),'|| nums:',nums[:6])\nEOF"
}
```


### [2026-09-06T16:05:38.421Z] TOOL RESULT

```
454  its  OS., ON.,  OHG.  equivalents.  See  comb  and  cp. kem || nums: ['842', '843']
455 ‘stalk,  blade’, Lett,  zeiju,  ziet,  ‘to  rise’  (said  of || nums: ['844', '845', '846']
456  n.,  a  kind  of  East  Indian  brocade. Hind,  kimkhab,  f || nums: ['848']
457 yoav,  ‘to  wail, groan,  weep’,  yooq,  ‘wailing,  groaning || nums: ['849']
458 f  a  small  hill.  —  ME.  knot,  fr.  OE. cnoll,  ‘hill  t || nums: ['850', '851', '920']
459 ,  fr.  Krieg,  ‘war’,  and  Spiel,  ‘game’. The  first  ele || nums: ['852', '853']
```


## [2026-09-06T16:05:43.392Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor key in ['ecclesia,  n.,  1)','class,  n.','council,  n.','consul,  n.','calendar,  n.','clear,  adj','claim,  tr','church,  n.']:\n    i=txt.find(key)\n    print('=====',key, i)\n    if i>0: print(txt[i:i+900].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T16:05:45.035Z] TOOL RESULT

```
===== ecclesia,  n.,  1) 3070462
ecclesia,  n.,  1)  assembly  of  citizens  in  ancient Athens;  2)  a  church.  —  L.  ecclesia,  ‘assembly of  the  people’,  in  Eccles.  L.,  ‘church’,  fr.  Gk. exxXrjOta,  ‘an  assembly  of  citizens’,  in  Eccles. Gk.  ‘church’,  fr.  IxxXtjtoc,  ‘called  out,  sum¬ moned’,  verbal  adj.  of  IxxaXeiv,  ‘to  call  out, summon  forth’,  fr,  lx  (see  ec-)  and  xaXetv,  ‘to call,  summon’.  See  calends  and  cp.  words  there referred  to.  Cp.  also  Ecclesiastes,  Ecdesiasticus. ecclesiast,  n.,  member  of  an  ecclesia.  —  Gk.  ix- xXrjauxaTTjC.  See  next  word. k Ecclesiastes,  n.,  name  of  one  of  the  5  Scrolls  of the  Hagiographa,  corresponding  to  Heb.  Qohe- leth  (Bible).  —  L.  ecclesiastes,  fr.  Gk.  IxxXvj- auxa-rrj?,  ‘speaker  in  an  assembly’,  fr.  IxxXr.ata, ‘assembly’ ;  see  ecclesia  and  -ast.  (For  the  mean¬ ing  of  lxxXr)ataoT7)c  cp.  Plat
===== class,  n. 1846398
class,  n.  —  F.  classe,  fr.  L.  classis,  ‘army  fleet, class,  division",  esp.  ‘one  of  the  six  classes  of  the Roman  people’,  which  prob.  stands  for  *qlad- t-is,  and  is  related  to  calare,  "to  call,  proclaim'. See  claim,  v.,  and  cp.  calends. Derivative:  class,  tr.  v. classic,  adj .  —  F.  classique,  fr.  L.  dassicus,  "relat¬ ing  to  the  classes  of  the  Roman  people",  esp. "relating  to  the  first  class'.  See  prec.  word  and -ic. Derivatives:  classic,  n.,  classic-al,  adj.,  classic- al-ly,  adv.,  classic-al-ness,  n.,  classic-ism,  n., classic-ist ,  n.,  dassic-i:e,  tr.  and  intr.  v. classification,  n.  — -  See  classify  and  -ation. classificatory,  adj.  —  See  next  word  and  adj. suff.  -ory. classify,  tr.  v.  —  F.  classifier,  fr.  fictitious  L. classificdre,  fr.  L.  classis,  "class",  and  -fiedre,  fr. facere,
===== council,  n. 2241808
council,  n.  —  OF.  cuncite,  fr.  L.  concilium,  ‘a gathering,  meeting,  assembly’,  which  stands  for *con-caliom,  and  prop,  means  ‘a  calling  to¬ gether’,  fr.  con-  and  caldre,  ‘to  call,  proclaim’. See  calends  and  cp.  conciliar,  conciliate.  For  the change  of  Latin  a  (in  * con-caliom)  to  1  (in  con¬ cilium)  see  abigeat  and  cp.  words  there  referred to.  Council  was  often  confused  with  counsel. councilor,  councillor,  n.  —  Formed  from  prec. word  with  agential  suff.  -or. counsel,  n.  —  ME.  conseil,  counseil,  fr.  OF.  con- seil,  counseil  (F.  conseil),  fr.  L.  consilium,  ‘deli¬ berative  assembly;  consultation,  deliberation, plan,  design,  advice,  counsel’,  which  is  prob. rel.  to  consulere,  ‘to  take  counsel,  deliberate’. See  consult,  v. counsel,  tr.  v.  —  ME.  conseillen,  fr.  F.  eonseiller, ‘to  advise,  co
===== consul,  n. 2118671
consul,  n.  —  L.  consul,  ‘either  of  the  two  chief magistrates  of  the  Roman  state’.  This  word prob.  meant  orig.  ‘convener,  convoker’,  and  is 341 contaminate rel.  to  consulere,  ‘to  take  counsel,  deliberate’. See  consult. consular,  adj.  —  L.  consular  is,  fr.  consul.  See  prec. word  and  -ar. consularity,  n.,  the  office  of  a  consul.  —  Late  L. consuldritds,  ‘the  office  of  a  consul’,  fr.  L.  con- suldris.  See  prec.  word  and  -ity. consulate,  n.  —  L.  cdnsulatus,  ‘the  office  of  a  con¬ sul,  consulate’,  fr.  consul.  See  consul  and  subst. suff.  -ate. consult,  tr.  and  intr.  v.  —  F.  consulter,  fr.  L.  con- sultare,  ‘to  take  the  advice  of,  consult ;  to  con¬ sider  maturely,  weigh,  ponder’,  freq.  formed  fr. consultus,  pp.  of  consulere,  ‘to  take  counsel;  to consider,  reflect,  deliberate’.  The  verb  c
===== calendar,  n. 1395815
calendar,  n.  —  L.  calendarium,  ‘an  account  book’, fr.  calendae,  kalendae,  ‘the  first  day  of  the month’  (see  calends).  The  account  book  was called  calendarium,  because  it  contained  the  first days  of  the  months,  on  which  the  accounts  were due. Derivatives:  calendar,  tr.  v.,  calendar-er,  n., calendar-ial,  adj.,  calendar-ian,  adj.  and  n., calendar-ic,  adj. calender,  n.,  a  mendicant  dervish.  —  Pers. qalender. calender,  n.,  machine  with  rollers  for  pressing cloth.  —  F.  calandre ,  ‘calender,  roller,  mangle’, fr.  earlier  *colandre,  fr.  VL.  *colendra,  fr.  Gk. xuXivSpoc,  ‘roller,  cylinder’.  See  cylinder, calender,  tr.  v.  —  F.  calandrer,  fr.  calandre.  See prec.  word. Derivative :  calender-er,  n. calends,  kalends,  n.  pi.,  the  first  day  of  the  an¬ cient  Roman  month.  —  ME.  kalendes,  fr.  OE. calend,  ‘m
===== clear,  adj 4073660
clear,  adj. Derivatives :  glair,  tr.  v.,  glair-eous,  glair-y,  adjs., glair -i-ness,  n. glaive,  n.,  sword;  spear.  —  ME.,  fr.  OF.  (=  F.) glaive,  a  blend  of  L.  gladius,  ‘sword’,  and  clava, ‘knotty  branch,  cudgel,  club’,  which  is  rel.  to clavus,  ‘nail’.  See  gladiator  and  close,  adj. glamour,  glamor,  n.,  magic;  alluring  charm.  — Corruption  of  grammar,  used  in  the  sense  of gramarye;  popularized  by  Sir  Walter  Scott (1771-1832). Derivatives:  glamo(u)r,  tr.  v.,  g!amo(u)r-ous, adj.,  glamo(u)r-ous-ly,  adv.,  glamo(u)r-y,  adj. glance,  intr.  and  tr.  v.,  to  glide  off  obliquely;  to flash;  to  look  quickly.  —  ME.  glacen,  fr.  OF. glacier,  ‘to  slip,  slide’,  fr.  glace,  ‘ice’ ;  see  glacier. The  word  glance  was  prob.  influenced  both  in form  and  meaning  by  ME.  glenten,  ‘to  shine’ (see  glint).  Cp.  glissade. 
===== claim,  tr 1836035
claim,  tr.  and  intr.  v.  —  ME.  claimen,  fr.  OF. claim-,  accented  stem  of  clamer,  ‘to  call,  cry  out, claim’,  fr.  L.  clamare ,  ‘to  shout,  cry  aloud,  call, declare’,  which  is  rel.  to  cld-rus,  ‘clear,  bright’,’ fr.  I.-E.  base  *kla-,  var.  of  *kal-,  ‘to  shout,  re¬ sound’.  See  calends  and  cp.  clear.  Cp.  also  low, ‘to  make  the  sound  of  a  cow’.  Cp.  also  acclaim, chamade,  clamant,  clamor,  clarity,  class  and the  second  element  in  council,  declaim,  de¬ clamation,  disclaim,  exclaim,  exclamation,  no- menclator,  nomenclature,  paraclete,  proclaim, proclamation,  reclaim,  reclamation. Derivatives:  claim,  n.  (q.v.),  claim-able,  adj., claimant  (q.v.),  claim-er,  n. claim,  n.  —  ME.,  fr.  OF.  claime,  fr.  clamer,  ‘to call,  cry  out,  claim’.  See  claim,  v. claimant,  n.  —  OF.,  pres.  part,  of  clamer.  See claim,
===== church,  n. 1786462
church,  n.  —  ME.  chirche,  churche,  fr.  OE.  cirice, cyrice  (whence  ON.  kirkja),  fr.  MGk.  xGptxdv, fr.  Gk.  xuptaxov  (scil.  86S|za),  ‘the  Lord’s  house’. OS.  kirika ,  ON.  kirkia  (Dan.  kirke,  Swed. kyrka),  OFris.  kerke,  MDu.  kerke  (Du.  kerk), OHG.  kirihha,  chirihha  (MHG.,  G.  kirche), ‘church’,  also  derive  fr.  MGk.  xuptxov.  OSlav. cruky  (Russ,  cerkov')  is  prob.  a  Teut.  loan  word. Gk.  xupiaxov  is  prop,  the  neut.  of  the  adjective xuptaxop,  ‘belonging  to  the  Lord’,  fr.  xupto?, ‘lord,  master’,  from  the  adj.  xupioq,  ‘having power,  having  authority’,  fr.  xOpo?,  ‘authority’, which  is  cogn.  with  OI.  sdvirah,  sQrah,  ‘strong, brave,  courageous’,  Avestic  sura-,  sura-,  ‘strong, mighty’,  Gaul.  Kauapo?,  OIr.  caur,  ‘hero’,  Co. caur,  W.  cawr,  ‘giant,  hero’.  These  words  prob. derive  fr.  I.-E.  base  *kew(e)-
```


## [2026-09-06T16:05:54.067Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nprint(len(pages))\nfor i,p in enumerate(pages):\n    if 'كنيسة' in p or 'كنوشتا' in p or 'كنشتا' in p:\n        print('--- leaf',i, p[:80].replace('\\n',' '))\nEOF"
}
```


## [2026-09-06T16:05:55.327Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"Synagoge\\|kanisa\\|kanîsa\\|knista\\|kenischta\" AFA.txt | head -20"
}
```


### [2026-09-06T16:05:55.634Z] TOOL RESULT

```
87
--- leaf 6 ‫معاه أخبار تارمحية وقد استعمابا العرب ععى‬           ‫اساطير ‏ بوناني ‪8‬‬     
--- leaf 19  ‫بير| ح ايطالى همءنط من المرمانية «عنة عرببها جعة تصنم من مخمير الشعير‬        
--- leaf 22                                      ‫« بيت ثور » في الارامية أي ببتالنار‬      
--- leaf 28                                     ‫د‬   ‫لاه‬     ‫مفئاه وعاءمننحاس مرادقه مرك
--- leaf 39                    ‫ناس وسممان نت أرامي ‪ 3‬سفسارا م©عتاه المساوم‬  ‫إسفين وسَفي
--- leaf 63                                     ‫ساي سم‬       ‫وناتي ‪80‬م ومنه الانكيزي مو
--- leaf 76                                  ‫يي للد‬   ‫سس‬     ‫اصل سكن معبد أي مكان الرحا
```


### [2026-09-06T16:05:55.703Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:06:00.293Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i in [69,70,71,72,76]:\n    print('===== leaf',i)\n    print(pages[i][:2500])\nEOF"
}
```


### [2026-09-06T16:06:02.089Z] TOOL RESULT

```
===== leaf 69
                               ‫اخسب سد‬
                            ‫الكشك مرادفه المبضوم أي مطبوخ المعدة والخثارة‬
 ‫بوناني تسطنةمعم‪ -‬أواتك معناه الف غرام وهو بساوي ؟الم‬        ‫كيلوغرام‬    ‫[ْ‬


          ‫‪.٠‬‏‬   ‫‪73‬‬                    ‫ة‬   ‫‪8‬‬           ‫‏‪٠.‬‬
 ‫يمس معئاه سيال وعصارة وف العلب هو‬              ‫وين ‪ -‬وونابي ‪5‬‬
‫استحالة الطعام فى المدة بعد الحضم الجوعر اشر هو مادة عتنة” الى الامقراد‬
          ‫تأخذ لونها غالبامنلونالغذاء الذي تتحلبمنهمرادفه عصارة الحضم‬
 ‫كيميا ‏ في اليونانية ‪#‬نسيرا معنا اختلاط وامئزاج وهو الاكير عند‬
                               ‫القدماء كانوا حولون به المعادن الى ذهب وفضبة‬
‫م كيورة فثر هامر الطعم يطرد‬        ‫كيناوكينهوقينااوري‬

                                      ‫فى امريكا‬
                                              ‫الحمّئ ومنشأها بلاد ابرط‬


                          ‫عل النارسة كوه الاراية‬
                                               ‫ل ان س اممز‬

                                     ‫ل‬
      ‫لازورد ‪ -‬فارسي « لازورد ولاجورد ‪ 6‬وهو حجر ‪ 3 1‬أزرق اللون‬
‫اللات ‪ -‬صم هو مؤنث إل األياله افلىاشورية فيكون معنىاللات الالة‬
‫‪,‬لأمع‪ 1‬معناه فرقة‬    ‫وناني لمعم وى الللانيتي‪9‬‬    ‫ا لحنة ولدة ولاجدون ‪0‬‬

                                                             ‫عسكر وجيش‬
                     ‫لعل حجركم أجمر س‪ -‬فارسبي ‪ 2‬لال » معنا أحمر‬
‫ىليونانية معناه حمْرة‬
                    ‫ل م ‪ -‬تركي « (لن »م معناه قناةوعهرى و ‪807‬هلاه ف ا‬
                ‫والمرادبه حشوة‪ 0‬ندس فى ثقب الص<ور فتنسفبا مرادفه نسفة‬

‫لعن و[لكوت فقالارشية ‪ 2‬لكن ‪ 6‬وف اليونانية ‪ 888101‬وى الارامية‬

===== leaf 70
                                 ‫ف أفنا© ممناه ست من محاس يفسل فيه‬
‫ا وقد يكال‬        ‫الث ‪ -‬فارسي‪ 0‬نك © وهوصبغأجمريصبغبهويطلى‬
                                      ‫الابطالية و‪ 21‬والى الافر نسية ‪6921‬‬
              ‫لما نونالي ‪ 580021‬معنأه لامعوالمراد به السراج والمصباح‬
‫أوجادت اللقنازيية ليهولزها ‪#‬جنقا عن اتناك يلاهالحتد كرت انيه‬
‫هندي وهو نبات يعرش له سنوف فها حبوب لونما أبيض وأحمر ويقال له‬
                   ‫‪1‬‬                                           ‫الدرجر والثامر‬
‫تركواو قدا شعوق التو ‪:‬ولوذا فىالنازسية لاون عن‬                        ‫‪0‬‬
                             ‫القريشة عندهم أما الِبّأ فهو أول الابن فى النتاج‬
‫اقدفه تزلومزل‬
            ‫رند‬
              ‫داهن ايطالي ‪202‬نه‪ !0‬معناه للانجار وبراد يمهف‬
                                                         ‫ف‬

‫مشتقمن ولا! كك وهو الاصل فىكي اللمائعات‬       ‫ار ولمثر ل وناني ‪11‬‬

  ‫ليتورجية ‪ -‬بوناتى هاعتنامانها معناه الحرفي خدمة عمومية والعرفي قداس‬
‫مون ‪ -‬فارمي «ليسو» وأصل هذه الشجرة من الهند فيكون اسمبا هندي‬
‫أموناصة ‏ ايطالي ‪8‬ا‪ !88001‬معناه به ليون وهو عيارة عن ماء يارد يُعصر‬
                       ‫فيه يمون ويذر عليه ار فشر مرادفه شربة مون‬


        ‫ظ‬                           ‫‪0‬‬
‫مادلا ‪| 53‬يطالي ‪ 411830211‬معئاه قرصة معدن صغيرة ‪ 60‬مرادفه الوط‬

                                                                 ‫يعاق بالعئق‬
  ‫ماخور ‪ -‬فارسي منحوت معناه شرب الخر واأراد به بدت الربية والفسق‬
 ‫أرابي «ماري» معئأة سيدي ‪.‬‬   ‫مار عبت أراني «مارا» معناه السيد وماري ‪-‬‬

===== leaf 71
                                   ‫بين‬
                                     ‫عدؤ‬
                                       ‫مع‬

                    ‫ومارعندنا وعندم بر داد به قدرس أمام أسمالقديس خاصة‬
        ‫مالاريا ‪ -‬ايطالي ‪ 21312‬معناه هواء ردي مرادفه الحمى الخبيثة‬
                  ‫« ماله » وعربيه الميسيعة والمملط‬    ‫‪-‬ي‬
                                                       ‫رقس‬
                                                         ‫امال‬
                                                            ‫فلج و‬
                                                                ‫ما‬
 ‫‪-‬ن الاراي ‪2,‬ل ‪ 6‬أي نش ونتف وهو كووة ورا امتوك‬
                                             ‫مالوش م‬
                                                 ‫الننات وف اللاتينية ‪5‬ناداءناءط‬

            ‫بوناني ‪ 8001621‬معناه قباس وهو الاصل فى قياس المساحة‬        ‫مر‬

  ‫مجوس ‪ -‬ف الارامية « مجوشا »‪ 6‬وف اليونانية ‪ 60825‬وف اللائينية كندهةم‬
 ‫ذفالمبرانية‪,٠‬مج‏ ‪ 4‬ورب مج رئيس المهوس ارميا ليق وصّجٍأوماج لفل‬
 ‫أشوري معتاة ع ناظيم وذكرهرودط ان الجوس زوج ‪2‬م كانوا السبط السادش من‬
 ‫حكاء ‪ .‬وقال أحد الملماء ان انظ مجوس منذ القرن‬           ‫أسباط مادي ‪0‬‬
                                      ‫الثاألث صار يدل على ااسحرة وعبدة الدار‬
                 ‫مل‪ -‬بوناني دوااءمدد مخلس وعرببه المتلة والزبرة‬
 ‫ا‪-‬يطالى ‪ 263‬واهليمسحاة أيجر تيا آنأ التيتشبه الرفش فيقال‬
                                                                    ‫ها‪0‬‬
  ‫مرجان ‪(١) -‬‏ صغار الاؤلؤ(؟) الخرز الاحمر (م) عزوق حمر تطلع ناملبحر‬
  ‫(طر حيط ) فى اليونائية‬
                       ‫كاصابع الكف وهو المشهور (‪ )4‬بقل ربيعي ق‬
 ‫اهعمو مقه ‪,‬قغالتدوتهد وق اللائينية هاتتوععويم معناه نولو ودر وهو مادة‬
 ‫كلسة تتكون فى مغابن الحيوان اهلايالذي يميش فى جوف الصدفه البحرية‬
 ‫والمهرية وهو ‪:‬وافق الامعلنىاول وهذا ‪5‬ل له بالفارسية مُرواريد أاليلؤلؤ ‪.‬‬
 ‫أما الذي بالممنى الثالث فيقاللهفى اليونائية «هنالهدها أي المرجان وهو يكون‬
‫غالبا أمر اللون وقديكون أبيض به نقط حمر ‪ .‬أما الذي بالمعتى الرابع فيقال له‬

===== leaf 72
                                                      ‫سسيم اإ‪#‬ا‪ 9‬اصمع‬




‫بالابطالية هنائةودعدده على سبيل الاستعارة وهو الاقحوان زهر معروف ‪ .‬أما‬
                                                              ‫الذي بالمعنى الثاى فاستماله مجازي ظاهر ‪:‬‬

    ‫ء“ِانطو امدتات ومري انس نورمي سما للش الح‪0‬راق وقد‬
                                            ‫ارصاص المّحرق المتحول الى مادة حخراء شل جدا‬
     ‫‪70‬‬    ‫‪0‬‬         ‫‪7‬‬           ‫‪٠‬‏‬          ‫‪5‬‬        ‫‪5‬‬         ‫‪5‬‬       ‫‪1 .‬‬        ‫‪ -‬ا ام‬      ‫‪*.‬‬
‫هدفارسي «مدرز ن كوش»‬                             ‫عو‬       ‫مول وم‬               ‫و‬   ‫قوس‬      ‫مره لوت مر‬


‫معناهاذان القار وهو ضرب من الرياحين دقيق الورق أبيض الزهر طب الراهحة‬
                                      ‫سميسيخ ن وقل عرالوه سمسقا‬                    ‫وى اللونانة ‪3250‬‬
                                 ‫‪1‬‬               ‫كه‬       ‫‪-‬‬         ‫ب‬         ‫‪.#‬‬                ‫*‪-‬‬   ‫عإز‪.‬‬   ‫‪4‬‬




           ‫فارسي ‪ 2,‬مرزيان ‪ 6‬معناه حافظط الحدود وحارص التخوم‬                                   ‫مرزبان ع‬


                                                                          ‫مارستان ‪ -‬راجع بمارستان‬
‫‪-‬‬     ‫‪5‬‬        ‫‪0‬‬         ‫‪5‬‬   ‫‪-‬‬         ‫‪5‬‬

‫عاسم وارم و رقة‬                  ‫اي‬         ‫أيطالى ت‪ 1911101 --‬مشتق من هع ظفلا‬                 ‫مر كيز م‬

‫سمّي بذلك لانهكان مستوليا فى الاعصر المتوسطة على اقطاعات ذات أعلام‬
                                           ‫والآن اما هو اقب شرف دون الوق وفوق الكونت‬
 ‫‪:‬‬        ‫'‬              ‫‪5‬‬     ‫ع‬                     ‫‪.‬‬      ‫حلم‬
‫مرزمر ‪--‬وتالى ‪ 00222‬ةنم معناة لاممأبيض بق وبراد به الرخام المعروف‬

                   ‫‪ 50261000012‬معناه وحيد القرن وهو الىكدن‬                                  ‫نسا‪-‬نى‬
                                                                                                 ‫ومي‬
                                                                                                   ‫مر‬

                                           ‫معناه رأب" الخردل‬                  ‫مسترده ‪ -‬ايطالى ‪9‬‬

          ‫مسطرة ‪ -‬أيطالي ‪ 801502‬معناه عر"ض البضاعة وغيرها مرادفه مثال‬
    ‫مصطكي ‪ -‬ونانى ‪8‬وعناموه هو عصارة شجرة نشبه الفستق واليطم تمد‬
                                                                         ‫فتتعقد صمعا بعلك مرادفه السك‬

    ‫مكروب ‪ -‬وثانى منحوت من "‪ 804116‬أي صغير و ‪ 5101015‬أي جى وهو‬

                             ‫أن حي يا رغ بالوعن امجردة بعش فى ا
===== leaf 76
                                 ‫يي للد‬   ‫سس‬




‫اصل سكن معبد أي مكان الرحال في‬
                             ‫انالهلفي‬
                                    ‫‪-‬ذلى وموم مع‬
                                               ‫نأووس و‬
     ‫الكنيسة ولماكان الناس يقبرون موتام فيالكنائس صار يطلق على القبر أيضا‬
                                    ‫»هو الزمكارة‬
                                               ‫ناي ‪ -‬فارسي « ناي و‬
           ‫نبراس ‪ -‬أرامي « نبرشتا » معناه اللهبوالضياء مرادفه المصباح‬
                           ‫نيربعم ‪ -‬فارمي « مارييج ‪ 6‬معناهتحية ملتوية‬
‫‏‪ ١‬ويسم فلار ‪ 5‬اموق الآمال اقبران ل نوت علىوس سناء‬
 ‫فوارأغجوف ومحفور ويراد بمها بايلنعقدتين من القصب فتقل الى الاتكليزية‬
      ‫‪6‬زم يعنى الانبوب وهو قصبة جوقاء ينفخ فها للعزمير وقد تكون من معدن‬
 ‫‪ 3‬في ‪--‬حبثي « نيجومي » معناهملكج ناجاستي ماوك ( جيممصرية )‬
‫في الفارسية ‪ 9‬رك > والفيونانية ‪ 5055111120‬وهو جنس من‬              ‫‪02‬‬

                    ‫ليض ‏‬
                        ‫يأب‬
                          ‫جعزمهره‬
                                ‫الرباحين زهره أصفر وله ستون نوعا منها نو‬
‫أو‬      ‫رس‬
         ‫فلك‬
           ‫لم‬‫اشير‬
                ‫راد فى الفارسية « ترد » وهو لعبة اخترعها ارد‬
                              ‫بزرجهبر أوغيرها وتعرف عندالعامة بلعبة الطاولة‬
 ‫ناشااف‪-‬افريسية « نشاسته »©ومهاودة بيضاءمتفركة تستخرج متقنيع‬
                                                ‫الارز والقمح والشعير والبطاطا‬
               ‫انرق الفارسية ن«وشادر » برادباهلمالمحونيا كا‬
                         ‫رة غزال اليسك‬
                                     ‫سهو‬
                                       ‫نافجة ‪ -‬فارمي « نافه ‪ 6‬و‬
                   ‫ثفير ‏ فارمي < نبور » وهو البوق والناقور ينفخ فيه‬
                                               ‫كر ‪ -‬ف اللاتينية ‪#‬تدوهه‬
                                  ‫عمعذأه عدد ودثم‬    ‫كزرة سب ايطالي ‪0‬‬
```


## [2026-09-06T16:06:12.928Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if re.search('كني|كنش|كنو|نيسة',p):\n        print('--- leaf',i)\nfor i in [66,67,68]:\n    print('===== leaf',i); print(pages[i][:2200])\nEOF"
}
```


### [2026-09-06T16:06:15.420Z] TOOL RESULT

```
--- leaf 6
--- leaf 19
--- leaf 22
--- leaf 28
--- leaf 30
--- leaf 39
--- leaf 46
--- leaf 62
--- leaf 63
--- leaf 76
===== leaf 66
‫فاتدير سموا به وحيد القرن على سبيل المشاعبة أدذمهها ‪:50‬عتاوهاء فراسوه‬
‫وعر وه كروكدحنأييد القرن الهنديويوز أنيكون الاسمفينيقي« قرنإحد»‬
                                                        ‫أي وحيد القرن‬
               ‫كستك وكشتبج فارمبي ‪ 9‬ع ‪ 6‬معناه خبط غليظ‬

‫الوا ‪:‬فاه ونيفاة‬            ‫“كتوفت لعن بوالقين الفولة حمر‬
‫تقممان النوروقدتكسف الشمس لهاولة القمربينهاويين الارض مرادفه احتجي‬
‫"ابح لاتق دءمفادن وهو شجر وف اليونانية «م«ماوةا سمي‬
                                   ‫باسممدينة فى بلاد اليونان مهدا الامبر‬

        ‫"تان حب فارسي « انكشتانه » معناه اصبعي مرادفه فمالخباط‬

  ‫رديبطهة‬
        ‫خمرا‬
           ‫معناهجامكل شيء وال‬        ‫‪ 1-‬ب أرامي‪ 8‬كر‪0‬‬
‫ل المذكور « كناش » فى قالون ان سينا‬        ‫امتكدي يجمم فها رزقه ومن‬
                           ‫وهودقتريكتب فيهالانسان ماينغي أن محنظه‬
                                   ‫تعريب «كاك ‪ 6‬القارسبى‬        ‫“كيك‬

 ‫معناه غطاء عقب الرجل ‪ .‬وجورب‬       ‫كاسات وقاشين ‪ -‬لانيني ‪3‬ع‬

       ‫‪0‬‬            ‫رلارجدلفه لفافة الرجل‬
                                        ‫ججوارب فارسيمعناهقبمر ا‬
‫وتالى ‪5‬ه معناه إرث ونصيب واللمراد به كبئةاليعةلان‬           ‫كليرس‬
                                                                ‫لله نصيمهم‬
 ‫كاله د ايطال مده 'مضاة ورقة مدل يتوه ‪:‬مزادفة تنك للامز‬
                                                            ‫والصك والوثيقة‬
                           ‫ونطروي معتاه بدل التقود وصرفبا‬         ‫‪00‬‬

===== leaf 67
  ‫‪ 1‬وبراد به منطقة من شعر ‪1‬‬            ‫فارسي « كر ‪ 4‬ا‬              ‫‪0‬‬      ‫‪3‬‬

                                                                       ‫اعلحىقوين‬
‫اه فى الغارسية والتركية مرادفه دار التمكس وما يؤخد‬           ‫كلك سوم‬
                                   ‫على البضائع والسلم ‪ 0‬له مكساج مكوس‬
   ‫كنحة ‪ 9‬فسارسي «كانجه » وهيآلةطرب ذات أوتار تشبه الربابة‬
              ‫كنار مدفازني‪ «:‬كنار »وهو اقيق أ بهل شير المدد‬
 ‫“نار أتوار تسرهو عماتور مقن "لزان يللد الوص ال غار‬
                                                       ‫كناريا فى غرى افريقية‬
        ‫‪ 0-5‬فارسي « كنار » براد به حاشية الثوب والطرف والساحل‬
‫فى الارامية ك«نارا © وفى العبرانية « و » وعي لشبه‬                       ‫‪00‬‬
                                   ‫اليونانة أي قيثار ذات هسة ‪1‬‬              ‫‪2‬‬

‫كناثة كناش باق ‪:‬تارق التو سياه وقتق ردي كنتنة الارابي‬
                         ‫أي جسعوالمرادبه دقتر يدرج فيه ما براد استذكاره‬
‫فى مقدمة ابن خلدون ‪ -‬اسباتي قدم تررمء معناه ىق الاصل ركار‬              ‫نان‬

‫مقداستعماوه لقياس سمت الارتفاع فكان لمكحك مهتدون به فى سفر البحر‬
     ‫ا‬
                                                       ‫كفل ووش أي غطاء‬

                      ‫‪ (0‬لبانق به مأ‪,‬وضم فيه الدراعم‪ 5‬ونوا ل أن‬
         ‫(؟) قااللنشيفاء الكمتجه رياب معروف معربكانجه عر بهحادلئون ا قيل‬
                ‫‪+‬إلى جام تسيصيا‬          ‫اليس حلجق وناك‬
                 ‫ما‬
                 ‫‪5‬ن‬   ‫وراح عناا‬          ‫اليس من صدا يبآ‬
                        ‫واذا سميت بالقيدثار يكون أولى اذ جرى عايها اهر الكتاب‬

===== leaf 68
                               ‫به اسه‬   ‫سكم‬




‫نونانى عترمهط وهي حشيشة تقتل برائحنها البراغيث والختافس‬              ‫‪5‬‬
                                                         ‫اشةغيث‬
                                                              ‫رشي‬
                                                                ‫اقالل لبهاح‬
                                                                          ‫وي‬
‫«نوشتا » الارامية لا من ‪8‬زهقاكاتاه إليونانية ومعناها‬
                                                   ‫كندسة ‏ من ك‬
                                                                  ‫اهمع والجاعة‬
 ‫كن م«نكاه ‪ 4‬أي تبن ومن « ربا » أجياذب‬                       ‫ار‬       ‫ال‬
‫فنا ‪ 5‬اص الاجسام التي اذا حكنت جذبت الاجسام الحفيغة‬
                                                  ‫وطزلمقان‬
                                              ‫‪...‬‬      ‫صتاب‬
                                                          ‫عحرك‬
                                                             ‫ار و‬
                                                                ‫للنو‬
                                                                   ‫اثت ا‬
                                                                       ‫وبع‬
‫‪6‬عيرانية‬
       ‫كورة ‪ -‬فالييونانية ‪#‬دوطه معناها بلاد وهي مأخوذة منق‪2‬ريه ال‬
     ‫بممنىبلادثمنقلتالىالسريانية ‏ كورا و‪6‬الى العربية كورةبممنىقرية‬
 ‫فو‬‫كروك هيوق ‪١‬ك‏رس" الازاية والسرائية وميا الكامن ‪:‬ومتان‬
                                           ‫الكأس والقدح والمشربة‬
‫كوقة و كقة حتإشاق متو تجا داغطا الرأس وعز هعم افلىبونائتة‬
                                                                     ‫معيأه راس‬


‫كولر نل ‪ -‬ايطالي العهناهاهه معناه قائد فيل "وهو رتبة ولقب فيقيادة‬
                      ‫|‬                                           ‫انود عندم‬
 ‫كوت ‪ -‬لاتيتي ‪, 81‬وعنممء معناه رفيق المليك وملازم الامير وهو‬
‫‪ 0‬وفوق البارون فعربتهالعر ب في الاعصر المتوسعلة‬
                                              ‫‪ 5‬شرف عندهم دون المر‬
                  ‫« قوس » عفنىالامير و« قسسّس » يعنى الرجل الشريف‬
                  ‫ط‪1‬إك! معناه يأرب ارحم‬             ‫كيريالسون ‪ 5-3‬وناني ‪13‬‬

 ‫كيلوس ‪ -‬بونانيودالزناه خ
```


## [2026-09-06T16:06:28.871Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nimport re\nfor i in range(60,74):\n    m=re.findall(r'\\[pdf page (\\d+)\\]',pages[i])\n    nums=re.findall(r'(?<![\\d])([4-8][0-9])(?![\\d])',pages[i][-300:])\n    print(i,m,nums[:5])\nEOF"
}
```


### [2026-09-06T16:06:30.595Z] TOOL RESULT

```
60 [] []
61 [] []
62 [] []
63 [] []
64 [] []
65 [] []
66 [] []
67 [] []
68 [] []
69 [] []
70 [] ['53', '60']
71 [] []
72 [] []
73 [] []
```


## [2026-09-06T16:06:35.765Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"kanisa\\|kanisat\\|kenischta\\|Synagog\\|Kirche\" AFA.txt | head -25"
}
```


### [2026-09-06T16:06:35.822Z] TOOL RESULT

```
9484:»Leuchter in der Kirche** gewesen.
9488:tern und Kirchen, die «ixJv«« , imponiert zu haben. Durch
9593:Die Kirche LLu Agäni IH. 16, 12; Y. 142, 5 a. f.;
9601:Natürlich ist auch (}X2i als »Kirche**, wie es yon A^iä
```


## [2026-09-06T16:06:36.187Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"kanisa\\|kanîsa\\|kanisah\\|synagogue\" FVQ_pages.txt | head -20"
}
```


### [2026-09-06T16:06:36.257Z] TOOL RESULT

```
1431:7 " The Jews in North Arabia and Syria read the Bible in Synagogues in the
7193:they are in general agreed that it means the synagogue of the Jews,
7201:is derived, of course, from the notion that the word means synagogues.
```


## [2026-09-06T16:06:40.316Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9585,9615p' AFA.txt; echo \"=== which leaf?\"; python3 - <<'EOF'\ntxt=open('AFA.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i,p in enumerate(pages):\n    if 'Die Kirche LLu Agäni' in p:\n        print('leaf',i,'printed p ~',i-30)\nEOF"
}
```


## [2026-09-06T16:06:40.577Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7185,7210p' FVQ_pages.txt"
}
```


### [2026-09-06T16:06:42.137Z] TOOL RESULT

```
mek^^räb Dillmann 836 übernommen ist. Nur bei der
Annahme einer Entlehnung ist die Möglichkeit da, die Ab-
weichung Yon der üblichen Lautentsprechung zu erklären.
Dann ist natürlich auch nicht mit Dillmann mek^^räb
zur arab. Wurzel V;^ zu ziehen, deren einziges hierher
gehöriges Derirat eben t^Ls^uo ist, sondern \^\y^jf ge-
hört zur äthiop. und arab. Wurzel v^«5^ zu der yermuthlich
auch 0^3113 zu stellen ist.
Die Kirche LLu Agäni IH. 16, 12; Y. 142, 5 a. f.;
XV. 7, 5a.f:; XV. 133,7; Div. Hud. 3,5 ist schon durch
die Lautrerschiebung als aramäisch gesichert» Denn aram.
lASiO >Ei** dann »Kuppel" entspricht arabischem L^Ij ,
also muss &juj fremd sein.
"- s
[Wohl nur missbräuchlich findet sich JSjuj einmal (Agäni
XIX. 97 , 11 a. f.) Ton einem jüdischen Bethause gebraucht.]
Natürlich ist auch (}X2i als »Kirche**, wie es yon A^iä
ZDMG. XXXIII. 216; ^Antara Appendix 16, 3 gebraucht
wird , sicher erst aus ILa^oi übernommen. Ich möchte aber
glauben, dass dies Wort überhaupt nicht arabisch ist,
sondern ursprünglich »grosses Gebäude** bedeutete, und so
erst auf das Kameel Amr^r. Mu^all. 17 übertragen worden
ist. Ich werde in dieser Vermuthung unterstützt durch
Tebrizi zur Hamasa29, 5 »UJI ^ «JLol f^S^^y ^'*
\
i
*
■wA A^- 1^ . . %. ; ^M ^ .*
•i
»_-•■-_.»■■sf^' *.* «-.r*»'
275
=== which leaf?
leaf 304 printed p ~ 274
```


### [2026-09-06T16:06:42.184Z] TOOL RESULT

```
y * V
Syriac Influence, 86, claims that it was from Syr. rather than from
Jewish Aram, that the word came to Arabic, and as the Eth.
seems to be of this origin, 1 it may be so. 2
(Salawdt).
xxii, 41.
Places of worship.
Though the Commentators are not unanimous as to its meaning
they are in general agreed that it means the synagogue of the Jews,
and as such many of them admit that it is a borrowing from Heb.
(Baid. and Zam. on the passage 3 : al-Jawaliql, Mu'arrab, 95 ; as-Suyuti,
1 The form fl ft/fl is later and derived from the Arabic (Noldeke, Neue Beitrdge, 35).
2 So Ahrens, Christlichefi, 40.
3 That it was a borrowing is evident from the large crop of variant readings of
the word noted by al-'Ukbari, Imla\ ii, 89.198 FOREIGN VOCABULARY OF THE QUR*AN
Itq, 322 ; al-Khafaji, 123 ; as-Sijistam, 201). This idea that it is Hebrew
is derived, of course, from the notion that the word means synagogues.
It could be from the Aram. KIT) /X which means prayer, but the
theory of Ibn Jinni in his MuUasab, quoted by as-Suyuti, Mutaw, 55,
that it is Syriac, is much more likely, 1 for though U<> means
prayer, the commonly used UCL^. AJLO means a place of prayer,
i.e. Trpoa-evxf), which Eudolph, Abhdngigkeit, 7, n., 2 would take
as the reference in the Qur'anic passage. As we find X1 & = chapel
in a S. Arabian inscription, 3 however, it is possible that the word first
passed into S. Arabian and thence into the northern language.
(Salld).
```


## [2026-09-06T16:06:53.363Z] TOOL CALL #31: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-06T16:06:53.371Z] TOOL RESULT

```


```


## [2026-09-06T16:06:57.530Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%84%DB%8C%D8%B3%D8%A7",
 "prompt": "Give the full Persian entry for کلیسا: etymology (source language, Syriac/Aramaic/Greek forms, Middle Persian form), meaning, and any citations."
}
```


## [2026-09-06T16:06:59.083Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%83%D9%86%D9%8A%D8%B3%D8%A9",
 "prompt": "Give the Arabic entry for كنيسة: etymology (Aramaic/Syriac source, root k-n-s), meaning, and related terms; also any note on the root ك ن س 'to sweep'."
}
```


### [2026-09-06T16:07:03.733Z] TOOL RESULT

```
# Persian Entry: کلیسا

**Meaning:** Church

**Etymology:** The word is borrowed from Ancient Greek *ἐκκλησία* (ekklēsía), which derives from *ἔκκλητος* (ékklētos) plus the suffix *-ῐ́ᾱ* (-ĭ́ā). The entry does not provide Syriac, Aramaic, or Middle Persian intermediate forms.

**Citation:** A 1520 classical Persian text by Selim I of the Ottoman Empire includes this usage: "When the beloved is affectionate and the wine-glass is a companion by my side, / Even if it is a **church**, it is better than the highest paradise."

**Alternative Forms:** کلیسیا (kalīsiyā), کلسیا (kalisiyā), کلیسه (kilīsa)

**Descendants:** The term evolved into Tajik калисо (kaliso), Bakhtiari کلسیا (kalesiyâ), Hindi कलीसिया/कलीसा, Urdu کلیسیا/کلیسا, and Turkmen kilise.
```


### [2026-09-06T16:07:05.820Z] TOOL RESULT

```
# Arabic Entry: كنيسة (kanīsa)

## Etymology
The term derives from the root ك ن س (k-n-s), which refers to "congregation and sweeping together." However, the synagogue sense appears to be "a semantic loan from Aramaic" sources like כְּנִישְׁתָּא (kənīštā).

## Meanings
1. Church (building and organization)
2. Synagogue (building and organization)
3. (Obsolete) A type of concealed palanquin or litter

## Related Terms
- **Synonym**: بِيعَة (bīʕa) — church or synagogue
- **Derived form**: كَنَسِيّ (kanasiyy)

## Linguistic Note
The root ك ن س fundamentally means "to sweep" or denotes gathering/congregation. The connection between sweeping and assembly likely reflects the idea of bringing things together, which then extended metaphorically to religious gatherings.

## Language Descendants
The word spread to multiple languages: Maltese *knisja*, Egyptian Arabic *kinīsa*, Swahili *kanisa*, Malay *kanisah*, and others including Hindi and Urdu variants.
```


## [2026-09-06T16:07:12.873Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%86%D8%B4%D8%AA",
 "prompt": "Persian کنشت: etymology (Aramaic/Syriac knishta?), meaning, Middle Persian form, related کنیسه."
}
```


## [2026-09-06T16:07:14.711Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%9B%D7%A0%D7%A1%D7%AA",
 "prompt": "Hebrew כנסת (keneset): etymology, root כ־נ־ס kanas, relation to Aramaic knishta, Knesset the Israeli parliament."
}
```


### [2026-09-06T16:07:20.294Z] TOOL RESULT

```
# کنشت (Kuništ) - Wiktionary Entry

## Key Information

**Definition**: کنشت is a Persian noun meaning a non-Muslim place of worship, including synagogues, fire temples, churches, temples/mandirs, and gurdwaras. It is marked as dated in modern Persian usage.

**Etymology**: The word was "borrowed from Aramaic כְּנִישְׁתָּא (kənīštā)" and shares a connection with Hebrew כְּנֶסֶת (kəneset̲). It is a doublet of کنیسه (kanise, "synagogue"), which entered Persian through Arabic.

**Language Coverage**: The entry documents the word in:
- Persian (with multiple regional pronunciations including Classical, Dari, Iranian, and Tajik variants)
- Urdu (marked as poetic)

**Historical Usage**: The word appears in classical Persian literature, such as in Nāṣir-i Khusraw's 11th-century travel narrative and Saʿdī of Shiraz's 13th-century Bōstān.

**Related Terms**: Connected words include آتشکده (fire temple), معبد (temple), کلیسا (church), and کنیسه (synagogue).
```


### [2026-09-06T16:07:20.885Z] TOOL RESULT

```
# כנסת (Knesset)

Based on the Wiktionary entry, **כנסת** is a Hebrew word with multiple meanings:

## Primary Definitions

The noun refers to "a coming together, a congregating, an assembly, a meeting." It can also mean "a synagogue, a congregation," with the related term being **בית כנסת** (bet k'néset).

In Mishnaic Hebrew, it historically denoted "the Sanhedrin, historical Jewish, judicial congregation of wise men."

## Proper Noun Usage

When capitalized as **הַכְּנֶסֶת** (hak'néset), it refers to "the Knesset, the Israeli Parliament."

## Etymology

The word derives from the Semitic root **כ־נ־ס** (k-n-s), which connects to **כנס** (kénes), meaning "a conference" or "a convention."

The pronunciation in Modern Israeli Hebrew is /ˈkneset/, and the word is feminine in gender.
```


## [2026-09-06T16:07:30.515Z] TOOL CALL #36: Bash

```json
{
 "command": "grep -n -i \"knst\\|kynšt\\|kaništ\\|kynst\" data/verification/sources/refs/PHD.txt data/verification/sources/refs/PHD_mackenzie.txt data/verification/sources/refs/NYB_vol2_glossary.txt | head; echo \"=== HUB/HRN ===\"; grep -n -i \"kunist\\|kuništ\\|kanisa\\|kalisa\\|kilisa\" data/verification/sources/refs/HUB.txt data/verification/sources/refs/HRN.txt | head"
}
```


## [2026-09-06T16:07:30.539Z] TOOL CALL #37: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1688 --image 2>&1 | tail -40"
}
```


### [2026-09-06T16:07:30.591Z] TOOL RESULT

```
=== HUB/HRN ===
data/verification/sources/refs/HRN.txt:4982:die ursprüngliche Vokalisation), diiriiysün, duruyßlden
data/verification/sources/refs/HRN.txt:7382:kunis, kunist (»Sahn. II, 048 Anm. 11, (/alc), kunisn
data/verification/sources/refs/HRN.txt:12745:kunist 847.
```


### [2026-09-06T16:07:38.678Z] TOOL RESULT

```
کلید ابمان -۱۹۸۸-
کلید اپمان -کنایه از کلمهٌ غهادت | كوچك بوذ که بعربی خنص رکویند ‎٩‏ .
باشد. . کلیکان < بفتح اول بروزن کنیزان ۰
کلیز دم او ما رس | رونت پرکیند یاون سای
زور باشد ‎٩‏ . گوبند اکر زنبوری برموش‌مرده ای ۰ ی
نشته باشد وکسیرا بگزدآنکی علاه ی | معروف که‌خورند وآ نرا بشیرازی ترخانی کویند؛
کل داد | وبع ی کوبند کیاهی باشد که‌آنرا طرخون‌خوانند
کلیز س با دال ابجد بر وزن عزبیز وییخ‌آترا عافرقرحا نامند . :
خان . خانهٌ زنبورراگوبند چه کلیز بمعنی زنبور ۱
باشد ‏ کلیکرون * بکسراول وفتح رابع‌ورای
: : ۹ : : بی نقطه بواو کشیده وبنئون زده ؛ بلغفت بونانی
5 کلیزه - بفتح اول‌بروزن عررضه,سبوی رستنیی باشد که آن را کهزك خوانند وآن‌خردل
آب راکونند ۲ .۹ ۹ :
7 بوستانی است.آب آنرا گرفته درپای درخت انار
کلیحاء ۴ » بکس اول و نانی بتختانی | ترش بريزند شیررین شود وبعتی کویند ترهنیز4
مجهول رسیدء واسین بی‌نقطه بالف رسیده,مخفف | است که بزبان عرپی جیرجیر خوانند.
کلییا است که جای پرستش و معبد ترسایان کلیکی ۷ » بروزن حقیقی.کاج واحول
باشد . راکوبند هرچند می‌بایست که بمعنی احولی‌باشد
کليك - بفتح اور بروزن شريك »تخم چه كليك بمعنی احول است لیکن همه‌جا بمعنی
کل راگوبند وعربان‌بز رالوردخوانند -ویرنده‌ای | لوج و احول‌آمده است واین‌هم درست است.
را نیز گوبند که پنحوست هشهوراست وآ نراجفد کلیم دست - بمعنی مبارك دست ونادر
و کوف وبوم نیز کوبند ۴ - و بمعنی‌کاژ و لوچ | دست و پاکیزه دست باشد پعنی در کارها بدییضا
واحول هم بنظر آمده است 9 - و یکسر اول » | نماید ۸ .
هم باین معن ی که احول باشد - وهم‌بممنی|انگشت کلیواج ‎٩‏ - با اك مجهول, بروزن
- آن میوه که درحلاوتش نیت بدل بارب نرسد بهیچ نوعیش اخلل
هردانه‌از آن تخم » کلیز عصل است یکدانه‌از آن‌شود کدوهای‌عل.
در صفت خربزه « جهانگیری ».
۴ - رك : رشیدی. کردی 8۴6102 ( کوزه . سبو) « ژاباص ۳۸۱ > قس : کراز(ه.م.).
طبری 818 (کوزه ) « واژه نامه *۵۹ ۲ . ۴ - رك : کلیا .
۴ «د کنك (هم.) . ۵ - کلك («.م.) :
چون بینیم ترا » ز یم ود " خویعتن را كليك مازم زود .
مظفری « لغت فرس ۷ و رك : انا ص۱۷۹ :کار
۹ < كلك (م.م.) * كليچك . ۲
۷ - ر4 :كليك. ۸ - مانند موس ی کلیم‌اظ ۰ 1
‎٩‏ «غلیواز < کلیواژ. وس
۰ یا ییا - ازبوانی هاوقاط اک دزاا ۷ 0
س ‏ دربهلوی 1۵ژه1انط کاء در مورد مسب ساری بر اوه
رفته ( داراب دستور پشوتن سنجانا : ملاحظاتی در باب فرضیهٌ :
دارمتتر درخصوص نامه تشر ص٩۱۹)‏ . ر4 :کنشت . کلیا
```


## [2026-09-06T16:07:52.409Z] TOOL CALL #38: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1688 2>&1 | head -12; echo \"############\"; timeout 900 python3 tools/ref_page.py BQT:1709 --image 2>&1 | tail -45"
}
```


### [2026-09-06T16:08:00.047Z] TOOL RESULT

```
REF: BQT:1688  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 481  OCR-lang: fas

کلید ابمان -۱۹۸۸-
کلید اپمان -کنایه از کلمهٌ غهادت | كوچك بوذ که بعربی خنص رکویند ‎٩‏ .
باشد. . کلیکان < بفتح اول بروزن کنیزان ۰
کلیز دم او ما رس | رونت پرکیند یاون سای
زور باشد ‎٩‏ . گوبند اکر زنبوری برموش‌مرده ای ۰ ی
نشته باشد وکسیرا بگزدآنکی علاه ی | معروف که‌خورند وآ نرا بشیرازی ترخانی کویند؛
کل داد | وبع ی کوبند کیاهی باشد که‌آنرا طرخون‌خوانند
کلیز س با دال ابجد بر وزن عزبیز وییخ‌آترا عافرقرحا نامند . :
خان . خانهٌ زنبورراگوبند چه کلیز بمعنی زنبور ۱
باشد ‏ کلیکرون * بکسراول وفتح رابع‌ورای
############
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1709.png
REF: BQT:1709  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 502  OCR-lang: fas

۹ کنشن
گنز ۱ - بفتح اول و انی‌وسکون زای | بهودان ‎٩‏ - وجای بستن خوکانرا نیز گویند -
نقطه‌دار ‏ بن و بیخ خوشةٌ خرما را کوبند .متی و بمعنی کردار هم آمده است چنانکه کویند
جایی که بدرخت چبیده است. « ب دکنشت > بعنی بدکردار ۷ .
گنست ؟ - بفتح اول و نانی و سکون کنشتی « بفتح اول بر وزن ارسطو ,
سان بی نقطه وفوقانی, آتشکده وآتشخانه راکوبند. | بمعتی‌غوره باش د که انگور نارسیده است و بعربی
کنستو ۴ « بر وزن ارسطو , اغنان حصرم خوانند ۸ - وگیاهیرا نیز کوین دکه‌بدان
باشد وآن کیاهیست که با یخ آن جامه شوبی | جامه شوبند ‎٩‏ .
و بی گوت کنو رستنیی باشد شبیه باشنان کنشتو لك "۱- بروزن پرستوك. بمعنی
وآن بیشتر در ولایت یمن و فرغانه رویدویعرپی دوم کنشتواست وآ ن گیاهی باشد که بدان جامه
محلب خوانند . شوبند .
نش - بنم اول وکسر ثانی وسکون کنشت - بکر اول بر وزن سرشك .
شین لقطه‌دار , بممنی کرداراست ۴ -خواء کردار | نیرزدن اعضا راکویند بسیب دردمندی‌وآ ترابمربی
نيك باشد و.خواه کردار بد - ومخفف کذفت‌هم | وجع خوانند .
هت که آتشکده و معید بهودان باشد 8 . کنشن - بنم اول وکسر ثانی و سکون
گذشت - بنم اول وکسرنانی وسکون ‏ ثاك وانون » بمعنی کنش است که کردار ليك
شبن و تای فرشت » بمعنی‌آنشکده است و معبد و بد باشد ۱۱ -وبمعنی کنشت ۱۴۳ هم آمده‌است
۹ - مخفف دکاناز» و« کناز» (ه.م.) رك : رشدی . ۲ - رك :کنشت .
۴ - رك : کنشتو » کنفتوك . ۴ - پهلوی و پازند ۴۱۷018138 « نیب رک ص
۴ منای ۲۷۸ : ۲ > ام مصدر از :کن (کردن) + ش ( انم مصدر ) . رك : اسم مصدر
بغلم نگارنده ۹ :
معجز بیفمبر مکی توبی بکنش و بمنش و بگوشت .
محمدین مخلد سگزی « تاریخ سیتان ص4۲۱
8 -رك :کنشن ,کنشت . ۹ - در رسم‌الخط پهلوی ۷8۳281298 ( مجمع )
« بلوشه . دستور پهلوی ص۷۵ > عبری 1680686111 ( جامعه ) ر4 : 11190077 , ۳.۸/1167۲
9 . 0 , ۸1250199 30۷190 0۳ آرامی «کنوشتا > (کنیه) « تفی » . بنابرین بفتح
اول صحیح است » رك4 : کنست کنیسه (معرب) » کلیسا ؛کلیمیا .
۷ - بدین معنی سم اول * کنش(ه.م.)
بگفتار گرسوز بد کنعت بنوی درختی زکینه یکشت .
« فردوسی طوسی طبق شاهنامةٌ چاپ ماکان » کلکنه ۱۸۲۹ ؛ فهرست ولف » قس : شاهنامهٌ بخ
چ ۳ص ۹4۸ ور : آسم مصدر پقلم نگارنده ص 4۳ ۸ * کنو (هم.).
‎٩‏ - «کنشتو (ن‌ل :کنستو ) نبانی است » بتازی محلب کوبند . شهید (بلخی) کوید:
تا کی دوم از کرد در تو کاندر تو تمی بینم چربو
ایمن بزی ا کنو ن که بشستم دست از تو باشتان ‏ و کنشتو .>
« لغت فری 2*۸ ۰ .
و رك : کنتو » کنفتوك4 . 4 رك :کنشتو کنو . ۱ لغت پپلوی است
0 ۳ کش (هم.) ‏ رك :انم مصدراص ۸ ۴ مصحف «کنفت >.
```


## [2026-09-06T16:08:15.899Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt; do echo \"== $f\"; grep -c \"\" $f; grep -n \"کنیسه\\|کناس\\|کلیسا\\|کنسول\" $f | head -8; done"
}
```


### [2026-09-06T16:08:17.738Z] TOOL RESULT

```
== MON_part1.txt
99339
956:اجداد. کشیشان (مسیحی)» آناء کلیسا» آباء 
958:پدران آسمانی. آباء کلیسا: کشیشان مسیحی؛ 
959:آناء کتسته. آباء کتسته: آباء کلیسا, 
5843:کلیسا. اب و این و روح‌القدوس 
10199:ست و غالبا در کلیساها نوازند. 
12921:اسکناس: عقجعمه (.) نوعی کاغذ بهادار 
12924:نشر اسکناس: چاپ کردن و انتشار دادن 
12925:اسکناس در میان مردم. 
== MON_part2.txt
94500
15142:پیوسته در کلیسا آویخته باشند. قندیل چرخ: 
17560:حق قضاء کنسول‌ها (کاپیتولاسیون) در ایران 
17563:داشت که سر و کار او با کنسول‌های ممالکک 
17567:(سیا.) ژنرال کنسول» جنرال قنسول الذ.) 
21516:کلیسا و غیره)؛ مق. آریا؛ سلو. 
24991:و کناس که بدان س رگن و پلیدی‌ها کشند. 
25894:کنشت» کنیسه (معر.)] معبد ترسایان» محل 
26757:کناس: 85 [ع.] (ص.) کسی که 
== incoming/MON/MON_2vol_Adena_v2_djvu.txt
94500
15142:پیوسته در کلیسا آویخته باشند. قندیل چرخ: 
17560:حق قضاء کنسول‌ها (کاپیتولاسیون) در ایران 
17563:داشت که سر و کار او با کنسول‌های ممالکک 
17567:(سیا.) ژنرال کنسول» جنرال قنسول الذ.) 
21516:کلیسا و غیره)؛ مق. آریا؛ سلو. 
24991:و کناس که بدان س رگن و پلیدی‌ها کشند. 
25894:کنشت» کنیسه (معر.)] معبد ترسایان» محل 
26757:کناس: 85 [ع.] (ص.) کسی که
```


## [2026-09-06T16:08:20.614Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25885,25905p' MON_part2.txt; echo \"-----کناس\"; sed -n '26750,26775p' MON_part2.txt; echo \"-----کنسول\"; sed -n '17550,17575p' MON_part2.txt"
}
```


### [2026-09-06T16:08:20.699Z] TOOL RESULT

```
وسیلهٌ کلید بسته شدن. کلید شدن 
دندان(های) کسی: (عم.) چفت شدن 
دندان‌های وی بر اثر سرمای شدید یا 
نزدیکی م رگ. ۱ 

کلیزه: (همدآاما (کوزه» سبو] (.) سبوی 
آب. 

۱ 3 [- کلسا - کلسه. قس. 
کنشت» کنیسه (معر.)] معبد ترسایان» محل 
عبادت مسیحیان. 

کلیشه: (۲۰17500(.) (چا.) تصویر یا 
نوشته‌ای که بر فلز پا چوب حکث کنند و آن 
را به هنگام چاپ کردن کتاب؛ مجله و غیره 
بکار برند. ضح.- (چا.) وقتی بخواهند خطی 
را عیناً چاپ کنند اول عکس آن را در روی 
فیلم یا شيشةٌ حساس می‌گیرند» سپس یکث 
قطعة ز نک را حساس کرده و همان شیشه با 
فیلم را به روی آن کییه می‌کنند. بعد زینکگ 
را ظاهر کرده و به روی آن مررکب می‌مالند 
-----کناس

کناره: (۵-)۷۵۱8۲2 [ - قناره. معر .| (.) قلابت 
آهنین (عموماً). قلابی که قصابان بر آن 
گوشت نند کنند (خصوصا). 
کناره‌جویی: ]-1۷[-, (حامص.) دوری 
کر دن» اعتزال» کناره گیری. 

کناس: 85 [ع.] (ص.) کسی که 
خاشاکک و خاکر وه از خانه‌ها برد» رفتگر» 
زباله کش. کسی که چاه مستراح را پاکك و 
بلیدی‌های آن را حمل کند. 

ک‌ناش: ۲۰۰55 [سعر. آرا. سر.] (.) 
مجموعه بادداشت‌های طبی. 

کناع: ۲022 (.) (جان.) کرمی که بر ابریشم 
تند؛ کرم پیله. تار (ریسمان» ابریشم» دیبا و 
غبره). تار عنکوت. 

کناک: 7-5 (.) (پز. قد.) پیچش شکم» 
ریز 

کنام: (ا.) آشیانه انسان و جانوران 
(جرنده» برنده دد و دام). 

کنام: ((.) جرانیدن اشتر. 
-----کنسول
کار بر داز 
مخلوطی بسیار سریع آتش می‌گیرد و هیچ 
وی رای از ود سن. ری نب آي 
نمی کذارد. ار تناسب اختلاط بنزین با هوا 
تغییر کند سرعت اشتعال مخلوط کم می‌شود 
و اگر از حد معین هم تجاوز کند» مخلو ط 
بهیجو چه ارم نی کرد سو خت آما (فر ه.) 
کاریرداز: 2 [- کار بردازنده] 
(ص‌فا.) آنکه تدییر و اجرای کاری در عهدة 
وی باشد؛ کارکن» عامل. (سیا. قد.) آنگاه که 
حق قضاء کنسول‌ها (کاپیتولاسیون) در ایران 
بر جای بود؛ دولت ایران در شهر های مهم 
کشور یک يا چند مامور بنام « کار پرداز» 
داشت که سر و کار او با کنسول‌های ممالکک 
خارجه و وظیفهً وی دفاع از حقوق یکی از 
متداعبین .در صورت ابر نیت - وده است. 
رتشا فد )سول تشون کار وان او 
(سیا.) ژنرال کنسول» جنرال قنسول الذ.) 
(نو.) (فره.) رثیس مباشرت و ملزومات؛ 
رئیس ادارةٌ کار پردازی. (یشاهنگی). (نو.) 
متصدی لوازم پیشاهنگی. (نو.) هر یکث از 
سه تن نمایندهٌ مجلس شورای ملی که در 
کار پردازی کار می کند. 

کارپردازی: آ-0:۳087-.1 (حامص.) 
مباشرت در انجام دادن کاری؛ تدبر در کار.
```


## [2026-09-06T16:08:28.691Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('MON_part2.txt',encoding='utf-8').read().split('\\n')\nfor i,l in enumerate(t):\n    if re.match(r'^\\s*(کنیسه|کنس|کلاس|کنشت|کنسول)\\s*[::]', l.strip()):\n        print(i, '|', '\\n   '.join(t[i:i+6]))\n        print('---')\nEOF"
}
```


### [2026-09-06T16:08:30.546Z] TOOL RESULT

```
24541 | کلاس: 5 (.) طسبقه» درجه» مرتبه. 
   ضح. به این معنی احتراز از استعمال این 
   کلم بیگانه اولی است. هر یک از اطاق‌های 
   مدرسه که در آن معلمان به شاگردان درس 
   دهند ؟ اطاق در س. 
   
---
27180 | کنس: 1315 [ع.] (مص‌م.) روفتن خانه را 
   (غم.) 
   
   کنس: 65 (.ص.) (عسم.) خسس 
   ممسکت. 
   
---
27183 | کنس: 65 (.ص.) (عسم.) خسس 
   ممسکت. 
   
   کنسرت: ۲067 (.) (مس.) هماهنگی 
   صداهای ابزارهای موسیقی» هماهنگی 
   صداها و سازها. (مس.) قطعه‌ای موسیقی که با 
---
27211 | کنسول: انادهه۲ [- قسول] () در روم 
   قدیم» عامل دولتی که از طرف مردم برای 
   
   
   کنسو لتاسیو. 
   یکسال انتخاب می‌شد و با شخص دیگری 
---
27253 | کنشت: ۲۰ ,۷۵068 (ک شتا قس. کلیساء 
   کنیسه ] (ا.) معبد بهودان (خصوصا). عبادتگاه 
   
   
   فر هنک فار سی‌معین 
   
---
```


## [2026-09-06T16:08:37.733Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"کنیسه\" MON_part2.txt | head; echo ...; sed -n '27255,27300p' MON_part2.txt"
}
```


### [2026-09-06T16:08:37.834Z] TOOL RESULT

```
25894:کنشت» کنیسه (معر.)] معبد ترسایان» محل 
27255:کنیسه ] (ا.) معبد بهودان (خصوصا). عبادتگاه 
27542:ضح.- کنیسه در عربی معبد یهود و نصاری را 
...
کنیسه ] (ا.) معبد بهودان (خصوصا). عبادتگاه 


فر هنک فار سی‌معین 


۱۴۰۵ 
کافران (عموما). 

عنف: اد (ا,) (گیا.) گیاهی است از تبره 
پثیرکیان که مانند کتان از الیاف آن جهت 
تهیهٌ طناب و گونی و بارچه‌های ضسخیم 
استفاده می‌کنند؛ کنب؛ شاهدانه مسصری. 
شاهدان؛ صحرایی» ثل بلدی» قنب بری. 
کنف آبی: ( گیا.) گیاهی است بکساله از ره 
مر کبان به ارتفاغ ۱۵ تا ۱۱ سانتیمتر تر و گاهی 
یکك متر که در دشت‌ها و تواحی کوهستانی 
همه نقاط اروپ و ايران می‌روید. بر گگ‌هایش 
متقابل و به ۳ تا ۵ قطعه دندانه‌دار 
است. یت ۳ آن شامل گل‌های لوله‌یی زرد 
رنگ و برگه‌های برگ مانند است؛ ثیل 
ماثی. دو دندان. کنف هندی: ( یا ۰) شاهدانه. 
کف اهستا [ع.] (.) حمایت؛ پناه؛ 
نگاهداری. طل؛ سابه. کرانه» جانب؛ ج. 
| کناف. 

کنئف: 16:۰0 (ص.) (عسم.) شرمرده و 
افسر ده؛ و جهه خود را از دست داده. دارای 
چین و چروک و کثیف شده (پارچه و مانند 
آن). 

کنف: 000۲ ,۵۸۲ [ع. ۰ (.) ج. . کنیف)؟ 
مستراح‌ها مبال‌ها. 

کعتفت ستلان: 606/۱7 (مسص‌ل.) 
شرمزده و افسرده گشتن» و جهه خود را از 
دست دادن. دارای چین و چروک و کف 
شدن (پارچه و مانند آن). 

کنقد را اسیو ل (.) (سبا.) 
اتحادیة چند ناحبه که جمعاً دولتی واحد 
تشه دهند اما هر یکك در داخل اتسحادبه 
استقلال داخلی و خودمختاری دارند» 
چنانکه کشور سویس را که از ۲۲ کانتون 
تشکیل گردیده نامند. اتحاد به.
```


## [2026-09-06T16:08:41.076Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27530,27552p' MON_part2.txt"
}
```


### [2026-09-06T16:08:41.143Z] TOOL RESULT

```
پرستار زن» جاریه. برده‌ای که دختر یا زن 


کنیزک: -۸۵]2 (ا.مصف.) زن خرد (عم.) 
دخت رکك. پرستار زن خرد. دخترک با زنکی 
که بر ده باشد. کنیز. 

کنیس: 5 (معر. ارمی؛ آرا. - کنشت] 
(.) معبد بهود. 

کت تمه (۳۱5۸)۵: [معر. ارمی؛ 0 
1 قس. کلیس ] (۱.) معند بهود و نصاری. 
ضح.- کنیسه در عربی معبد یهود و نصاری را 
گفته‌اند و امروزه در عربی معبد بهود را 
رکتیس» و معبد تصاری را« کنستة» و معید 
مسلمانان را رجسامع» (و مسجد) و معید 
بت‌پرستان را هیکل گویند. (اقرب الموارد). 
کستفت: 201 [ع.] ۸( بوشش » پرده. سبر. 
سایبانی از شاخ‌های درخت برای مواشی. 
نهانخانه: مستراح. 

کو: (۳)۰0۷:[- کاو] (ص.) زب رک و 
هوشیار.
```


## [2026-09-06T16:08:51.998Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ecclesiastic",
 "prompt": "Give the etymology chain for ecclesiastic/ecclesia: Greek ekklesia, ekkalein, ek + kalein, PIE root."
}
```


## [2026-09-06T16:08:53.162Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/consul",
 "prompt": "Etymology of consul: Latin consul, its origin (consulere? *kom-sel-?), and whether it is related to concilium/council."
}
```


### [2026-09-06T16:08:57.311Z] TOOL RESULT

```
# Etymology Chain for Ecclesiastic

Based on the Online Etymology Dictionary entry, here's the etymological progression:

**Modern English** → **French/Medieval Latin** → **Greek** → **Proto-Indo-European**

The word "ecclesiastic" (late 15c.) derives from French *ecclésiastique* and Medieval Latin *ecclesiasticus*, which came from Greek *ekklesiastikos*, meaning "of the (ancient Athenian) assembly" and later "of the church."

The Greek root breaks down further: *ekklesiastes* (speaker in an assembly) comes from *ekkalein*, which combines two elements:
- *ek* = "out" 
- *kalein* = "to call"

The ultimate source is the PIE root *\*kele-* (2), meaning "to shout."

This semantic journey reflects the word's evolution from describing someone who speaks to an assembly in ancient Athens to its specialized religious meaning in Christian contexts.
```


### [2026-09-06T16:08:59.904Z] TOOL RESULT

```
# Etymology of Consul

Based on the Online Etymology Dictionary, here's what we know about consul's origins:

## Latin Root and Meaning

The word comes from Latin *consul*, originally referring to "one of the two chief magistrates in the Roman republic." The likely origin is "one who consults the Senate," derived from the verb *consulere* meaning "to deliberate, take counsel."

## The Verb's Structure

According to the etymology provided, *consulere* probably combined *com* ("with, together") with *selere* ("take, gather"), yielding an original sense of "gather (the Senate) together." The source notes: "Since *consulere* does not look like a derivative of *consul* (we would rather expect *consulare*), it appears that the verb was original and meant 'to get together, deliberate'."

## Relationship to Council

The page doesn't explicitly address whether *consul* relates to *concilium* (council), though both appear etymologically connected through the Latin root *selere* meaning "to take" or "gather."

## Modern Usage

By around 1600, the term expanded to designate merchant representatives in foreign lands, and eventually modern diplomatic agents protecting citizens' interests abroad.
```


## [2026-09-06T16:09:06.503Z] TOOL CALL #46: WebSearch

```json
{
 "query": "Middle Persian kilisyāk church Syriac qlēsyā Persian kelisā etymology ekklesia"
}
```


## [2026-09-06T16:09:07.791Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7375,7392p' HRN.txt; echo \"== HRN index 847\"; grep -n \"kunist\" HRN.txt"
}
```


### [2026-09-06T16:09:07.848Z] TOOL RESULT

```
LW. karr, Jcar, n. l^ar (120); w^./. LW. kar^ sar. ctum,
la/ni. kannä.
). keräu Ufer, Seite, Ende', keräne, meist kenür^ keyiüre.
aw. karana- 'Seite, Knde*; phlv, kaiiär, kanärak,
a\kanarak.
oss. Mro« Endo' (155); LW. kurd. af/. kinür,
7. kerden 'tun , inaclien', Praes. kun-ent , kuj/dnlden 0,
kunis, kunist (»Sahn. II, 048 Anm. 11, (/alc), kunisn
(Wörterbücher).
ap. y'kctr-, kiinavahy *tnn , maclien'; aw. K/kar-,
kerenaoiti] yihlv. kartan, kartär, kunäk (vergl. Justi,
ZDMG. 40, 287), kun(i)sn, päz. knnom; ai. l^/:ar-, k^ntdi.
kurd. Ä:2?7w, Praes. A-em 'machen'; oss. d. känmi,
t. /'ä/?//* (152); bei. kanag, n. XVi//a/ (185); wa;^. rar-
am, siyn. kin-am, sar. kan-am.
Die np. Dialekte haben den J^-aesensstamm Aim-
nicht (vergl. aber gel. /j«f/e« (Inf.) neben kei\hn).
Vax V^kar- 'machen* gehört auch Kns. Q. ha\ugör(leii,
== HRN index 847
7382:kunis, kunist (»Sahn. II, 048 Anm. 11, (/alc), kunisn
12745:kunist 847.
```


### [2026-09-06T16:09:15.382Z] TOOL RESULT

```
Web search results for query: "Middle Persian kilisyāk church Syriac qlēsyā Persian kelisā etymology ekklesia"

Links: [{"title":"ἐκκλησία - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E1%BC%90%CE%BA%CE%BA%CE%BB%CE%B7%CF%83%CE%AF%CE%B1"},{"title":"Shuaeklesia","url":"https://en.wikipedia.org/wiki/Shuaeklesia"},{"title":"Ecclesia","url":"https://en.wikipedia.org/wiki/Ecclesia"},{"title":"CHRISTIANITY i. In Pre-Islamic Persia: Literary Sources - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/christianity-i/"},{"title":"Church of the East","url":"https://en.wikipedia.org/wiki/Church_of_the_East"},{"title":"کلیسیا - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%DA%A9%D9%84%DB%8C%D8%B3%DB%8C%D8%A7"},{"title":"CHRISTIANITY iv. Christian Literature in Middle Iranian Languages - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/christianity-iv/"},{"title":"(PDF) “How Persian was Persian Christianity?” (1996)","url":"https://www.academia.edu/36292920/_How_Persian_was_Persian_Christianity_1996_"},{"title":"0% found this document useful (0 votes)","url":"https://www.scribd.com/document/605889068/CFED"}]

Based on the search results, I can provide you with information about the etymological connections between these terms:

Persian کلیسیا (kalīsiyā) was borrowed from Classical Persian کَلِیسَا (kalīsā), which was borrowed from Ancient Greek ἐκκλησία (ekklēsía).

The Greek ekklēsia gave rise to various forms across languages, including Persian: کِلیسا (kelisâ), کلیسیا (kalīsiyā / kelisiyâ), کلسیا (kalisiyā / kalesiyâ), کلیسه (kilīsa / kelise).

The search results also demonstrate the connection between Syriac and Persian terminology in Christian contexts. In Middle Persian texts, there are terms used for Christians including KLSTYDʾN, which represents Syriac kristyānē, showing how Syriac religious terminology was adopted into Middle Persian.

While the search results don't explicitly discuss the specific Syriac term "qlēsyā" or Middle Persian "kilisyāk," they confirm the broader etymological path from Greek ekklēsia through to Persian and related Iranian languages used in Christian communities during the Middle Persian period.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T16:09:26.264Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC kel-\"; grep -n \"^kal-\\|^kalē-\\|^kel-\\|^klā-\\|^klāmō\\|^klassis\" IEC.txt | head -20; echo \"=== LAT classis/concilium/calo\"; grep -n \"^classis\\|^concilium\\|^calo,\\|^clamo\\|^clarus\\|^calendae\" LAT.txt | head"
}
```


## [2026-09-06T16:09:26.286Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"classis\" LEW_1910.txt LAT.txt | head -10"
}
```


### [2026-09-06T16:09:26.345Z] TOOL RESULT

```
LAT.txt:4782:rable A celui qu'on observe dans legiS, classis. Le Bens de "armle"
LAT.txt:4784:opposent exercitus k classis ou k equitatus. Exercitus Itant ainsi
LAT.txt:8818:indiquer des bruits. V. aussi clarus et classis ?
LAT.txt:11162:48); cf. 1 'evolution de sens de classis. Un autre sens de centuria
LAT.txt:11889:(defini par Serv. Ae.7,613); classis,in procinctu "armee en tenue de
LAT.txt:12237:classis
LAT.txt:12263:classicus, -um: v. classis. ,
LAT.txt:12264:classis, -ls f.: le sens premier est aans doute "appel", classis
LAT.txt:12265:iuniorum "appel des j eunes gens" par opposition a classis seniorum.
LAT.txt:12269:quee sous les armes dans classis clipeata, classis procincta- cf. P.F.
```


### [2026-09-06T16:09:26.354Z] TOOL RESULT

```
=== IEC kel-
6653:kal- (1) (kalt-) ‘slope’. Cf. WP I, 430 and kalt- Skt. cf. katakah 'slope'; Go. wilja-halpei, f. ‘favour’; OHG hald, adj. ‘inclined’; G Halde ‘slope’; Du. cf. hellen, v. ‘tilt’; ON hella *de- cant’; R cf. po-kolét ‘die off”; Li. kaliuos, kal- tis ‘lean’; üZ-kaliu, -kalti ‘lean’; at-kaltis, f. “back of chair; LW in Finn. kaltto, kalteva ‘sloping’
6654:kal- (2) ‘bright, white’. Cf. WP I, 429 Gk. kalós (‘bright, beautiful’. Despite Boeot. kalwós?); cf. kállos, n. ‘beauty’; (-a- in) kelás, gs -ádos ‘goat w. white blaze’; Lat. cf. calidus (or calidus) *white-blazed'; Latv. cf. kaleju, et ‘bleach’. (Link w. Lat. caleo, ere "be bot, and w. LG hellig ‘thirsty’ uncertain). Cf. kali-
6665:kal- (3) (kalaio, kaleio) “call, name, summon, invite, accuse'. Skt. cf. usa-kalah ‘cockerel’; Hitt. cf. kalles- “invite, entice’; Gk. kaléo; Alb. kall ‘slander’; OLat. caló, are ‘call’, cf. concilium ‘council; Mir cf. cailech, mod. coileach ‘cockerel’ be- side Ir. caileachas (‘cocksfoot’, bot.); W cei- liog ‘cockerel’; OHG halon, v. ‘call, invite’; MHG haln, id.; Li. cf. kal-bà ‘speech’, kaltas, adj. ‘accused’; kaltis, ies, f. ‘accusation’; cf. also kalenti ‘gabble, as cranes’
6666:kal- (4) ‘fix, fasten, hold’. Cf. WP I, 437. Same as (5) and (6)? Skt. kalami, kalayami, id.; Arm. kalnum, ka- lanem, id.; kalank ‘arrest’; Alb. cf. ngel (“hold, stop”, fr. *en-kalio); Lat. cf. inter-calō, -calāre (2) “delay, stop’; Li. ap-kalinti ‘imprison’
6667:kal- (5) ‘thrust’. (Same as (4) and (6)?). Cf. WP I, 437, but cf. kol- Skt. kalāmi, kalayāmi (2) ‘thrust, drive’; Arm. cf. kal, o-st. ‘threshing floor” (fr. *kalios); Alb. kall (2) ‘thrust, insert, bung’; Lat. cf. inter- calo, are (1) “insert”; OCS (here or under (6)) koljọ, klati ‘stab’; Li. kalù, kálti ‘drive in; forge’; Latv. kaļu, -t, id.
6668:kal- (6) ‘strike’. Same as (4) and (5)? Cf. WP I, 437 Per. cf. kaland ‘spade’; Arm. cf. kal, o-st. (‘threshing floor’, but equally to kal- (5)): Gk. kalís *adze'; Lat. cf. hordi-calia (for *fordi-°: ‘sacrifice of cows in calf; ON heljast (toil but equally to kal- (5); OCS koljo, klati (‘stab’, equally to (5))
6669:kal- (kaleio, -āið) “lure, deceive’. WP I, 446 Gk. kéléo (allure, if w. IE *-a-); Go. holon ‘curse’; OHG huolian, v. ‘cheat’; ON hoela ‘flatter, praise’; Du. heulen ‘conspire’
=== LAT classis/concilium/calo
8655:calendae: v. colo,-os 1.
8767:calo, -onls m.: cf. cala.
12237:classis
12243:clarus, -a, -um; clair. Apparente a clamo et calo, clarus a du
12264:classis, -ls f.: le sens premier est aans doute "appel", classis
12274:classis s'est sp 4 cialis <5 dans le sens de "flotte", et classiarius a
12284:classis a calando; mais la derivation ne s'explique pas. Les mots en
13327:concilium, —I n.: convocation, a concalando, i,-e, uocando, t P.F.
32967:classis. Derivas: legionarius', legiuncula (t.L. ). Cf. osq. leginum "le -
49605:clarus, praecellti, etc. De la praenimium, praenimiti (Gloss.). Du sens
```


## [2026-09-06T16:09:29.571Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12237,12295p' LAT.txt; echo \"=== concilium\"; sed -n '13320,13345p' LAT.txt"
}
```


### [2026-09-06T16:09:29.686Z] TOOL RESULT

```
classis
V. Ia remarque sous calo.
clarnus, -i m.: se tronve seulement dans le schol.de Perse, in
prol., satira est genus clarni uel lancis multis ac uariis frugum gene¬
ribus plena. Clarnus potest appellari discus uel mensa quae referta
sacrificiis Veneri consueuit offerri, itrusque ?
clarus, -a, -um; clair. Apparente a clamo et calo, clarus a du
s’appliquer a la voix et aux sons, clara uox, etc.(c£ declarer, clariso¬
nus, traduction du gr. XoyucpOoYfOC); pnis il s’est etendu aux sensations
de la vue, clara lUx, clarum caelum, "clair, brillant", puis aux choses
de 1'esprit, clara consilia, exempla, etc., et Hieme aux individua et
aux choses "illustre, brillant, glorieux" (par opposition A obscurus),
d’ou la formule uir cldrissimus . Ancien, usuel. Panronan, M.L.1963.
Ces divers sens se retrouvent dans les derives: claritas et clari¬
tudo-, cldro,-are (ni claratus,-us , ni clarator,-t io, mais declaratio-,
claro est rare, la fonne a preverbe d'aspect "determin^" declaro est
la seule frequente); clareU et cl SrSscd, - ere . Un terme de la langue
rituelle est clarigo,-as "reclamer a haute voix de 1'ennemi ce qu'il
a pris" (se dit des f^tiaux), clarigatio, meme formation que dans litigo,
purtijgo, etc.; d'ou peut-etre clarigito dans Lucr. 5, 947 ). A basse
epoque apparaissent clari ficus (d'aprbs magnificus ) et clarifico sur-
tout dans la 1 . de l'igl.; claricans (Apul. d'apres albicans).
Oomposes: declaro,-as: manifester, annoncer a voix haute, declarer;
avec les derives ordinaires; exclaro: eclairer, illuminer (Vitruve),
M.L.8978, et .8973 *excldriare; inclaresco.
V. calo.
classicus, -um: v. classis. ,
classis, -ls f.: le sens premier est aans doute "appel", classis
iuniorum "appel des j eunes gens" par opposition a classis seniorum.
Designe ensuite les diverses sortes de "classes" de citoyens suscepti-
bles d’etre appel^s sous les armes: et partes populi classes uocamus
quae quinque fuerunt, Serv., Ae.7,716, et d'autre part la " troupe" convo-
quee sous les armes dans classis clipeata, classis procincta- cf. P.F.
48,88, classes clipeatas antiqui dixerunt, quos nunc exercitus uocamus;
et 49,10, classis procincta: exercitus instructus (cf.894,3; 395,3).
Vetustius enim fuit multitudinem hominum quam nauium classem appellari,
P.F.851,30. Puis exercitus ayant servi A designer 1 'armee de terre,
classis s'est sp 4 cialis <5 dans le sens de "flotte", et classiarius a
signifi^ "de la flotte, marin". D^nominatif: conclassare: classem
iungere (Gloss.). M.L.susa? Iri. class. Mais classiciis a gard^ le sens
ancien, cf. Varr. L.L.5,91, classicos a classe, qui item cornu canunt,
ut tum, cum classes comitiis ad comitiatum uocant. De IA classicum
(sc. cornu): trompette, clairon qui sert A appeler les classes. M.L.
1964. Le pl. classici (sc.cluSs) designe aussi les citoyens appartenant
A la premibre des classes creees par Servius Tullius; de IA le sens
de scriptores classici "^crivains de premier ordre", d'ou "classiques".
Les anciens rattachent classis A caldre, cf. Quint. 1, 6, 33, sit et
classis a calando; mais la derivation ne s'explique pas. Les mots en
-ssis sont rares en latin, et partout 1'origine du groupe -ss- est
reconnaissable, cassis, messis, tussis. L'emprunt A un imaginaire gr.
xXacnC (= ion.-att.xXrjai,c;), qu'indique Denys, Ant.4,18, xXaaei,S, xaxa
xac 'EXXr|Vi,xac "xX^aeoc" 7BXpovo|i.acavTec.. . xou xas xXaaeoc ap^aoov
exaXouv "xaXeCTeog" n^st qu’une etymologie populaire. Terme techniqueclatri
994
qui peut etre emprunt^ a. 1'etrusque.
V. calo.
clatri m. et clatra, -orum n. (forme populaire cracli, issue de
clatri par metathese reciproque (clatri > *crdt li > crdcli) dana l'App.
Probi 309): barreaux, treilli3 de bois ou de metal destine a fermer
=== concilium
D 4 riv 4 s: conchatus, concheus; conchula {conc(u)la), M.L. «113. A laconchis
344
meae famille appartient conchylium {conchi-, conci-, conquilium Gloas.):
coquillage, pourpre. M.L.au4<
conchis, -ls f. {cunchis forne ancienne, cf. Prisc. GLK II 36,36):
ffeve ayec a a robe. Cf. gr.xoyxpc. De la conc( hjic (uj la et concicldtus
(Apic.).
concilium, —I n.: convocation, a concalando, i,-e, uocando, t P.F.
33>27J d'oh "aasemblee, r6union" (dans lea villes d*Italie), en parti-
cnlier "assembl^e de la plhbe" (par oppoaition aux comitia), pnis
"r^union, enaemble" en gen£ral. Anci en, nanel. M.L.3H4a. Le lien oh
se tenaient dea assembl^es s'appelait conciliabulum, mot qui a fini
par designer 1 'assembl£e elle-mSme (cf. c 5 ns ilium). Comme c'6tait dans
ces assembl^es qu'on ae r^unissait pour conclure des affairea, traiter
des march£s, terminer des differenda, former des alliances, etc., le
verbe concilio, -Ss qni signifiait tont d*abord "assembler, reunir" a
pris dea sens divers correspondant k cette activite des concilia,
conciliabula: concilier, se concilier (par oppoaition k abalienare );
procnrer, acheter, acqnerir, cf. Pl. Tri. 856 eo conductor melius de me
nugas conciliauerit-, et anssi P.F.54,36 conciliatrix dicitur quae uiris
conciliat uxores, et uxoribus uiros. C'est dn sens de "acheter" qne
derive celni de inconciliare, verbe plantinien (Ba. 550-1; Mo.613;
Pe. 883-4, cf. incomitiSre Cn.400) qni vent dire "tromper (dans nne
vente),mettre dedans", c£ P.F.95,7 inconciliasti: comparasti, commen¬
dasti, uel, ut antiqui, per dolum decepisti, et dans leqnel in- a nn
sens p^joratif comme dans inlicio (cf. an contraire allicio), illaqueS,
```


## [2026-09-06T16:09:36.208Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/kelh%E2%82%81-",
 "prompt": "Proto-Indo-European *kelh₁-: meaning, Pokorny reference, derived terms in Greek (kaleo), Latin (calare, calendae, clamare, clarus, classis, concilium), Germanic."
}
```


## [2026-09-06T16:09:38.271Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%9B%D7%A0%D7%99%D7%A9%D7%AA%D7%90",
 "prompt": "Aramaic כנישתא (kenishta): meaning, root k-n-sh, relation to Hebrew keneset and Arabic kanisa, descendants in Persian/Arabic."
}
```


### [2026-09-06T16:09:42.800Z] TOOL RESULT

```
# Proto-Indo-European Root *kelh₁-

## Core Meaning
The reconstructed root *kelh₁- means "to call out to," based on comparative evidence across Indo-European languages.

## Alternative Forms
Scholars propose several variants: *kalh₁-, *kel-, *kleh₁-, and *ḱelh₁-, reflecting different reconstruction approaches.

## Major Descendant Languages

**Greek**: The root produced kaléō ("to call, summon"), along with related forms like kiklḗskō and κληδών (klēdṓn).

**Latin**: Multiple derivatives emerged, including:
- clāmō ("to cry out, clamor")
- clārus ("clear, loud")
- classis ("assembly, fleet")
- concilium ("council, meeting")

**Germanic**: Produced *hulōną ("to call for, summon") and *hellaną ("to sound, resound"), with descendants in Old Norse hjal ("babbling").

**Celtic & Other Branches**: Extended to Proto-Celtic forms meaning "rooster" and Latvian kaļuôt ("talk idly").

## Formation Types
The root appears in various grammatical formations including thematic presents, nasal-infix presents, s-presents, aorists, and reduplicated forms, demonstrating its productivity in Proto-Indo-European.
```


### [2026-09-06T16:09:42.951Z] TOOL RESULT

```
# כנישתא (Aramaic)

Based on the Wiktionary entry, **כנישתא** is an Aramaic adjective meaning "gathered" or "collected." 

The term has an IPA pronunciation of /kniʃtaʔ/. Its masculine form is כנישא, while the plural remains כנישתא.

A notable descendant appears in Lishana Deni, where **כנשתא** (knəšta) evolved to mean "synagogue"—a semantic shift from the original adjective meaning.

The entry cites authoritative lexicographic sources including the Comprehensive Aramaic Lexicon Project and classical Aramaic dictionaries by Marcus Jastrow and Jessie Payne Smith.
```


## [2026-09-06T16:09:54.546Z] TOOL CALL #53: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%A9%D9%84%DB%8C%D8%B3%D8%A7' --note 'page 251, root Kel 3, node 3: Persian کلیسا from Greek ekklesia' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%83%D9%86%D9%8A%D8%B3%D8%A9' --note 'page 251, node 5: Arabic kanisa, root k-n-s, semantic loan from Aramaic kenishta' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%A9%D9%86%D8%B4%D8%AA' --note 'page 251, node 9: Persian کنشت borrowed from Aramaic kenishta, doublet of کنیسه' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D7%9B%D7%A0%D7%A1%D7%AA' --note 'page 251, nodes 7/10: Hebrew keneset, root k-n-s, Knesset' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D7%9B%D7%A0%D7%99%D7%A9%D7%AA%D7%90' --note 'page 251, node 4: Aramaic kenishta gathered/synagogue' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/kelh%E2%82%81-' --note 'page 251, root Kel 3 = PIE *kelh1- to call out' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/ecclesiastic' --note 'page 251, node 1: Greek ekklesia < ekkalein < ek + kalein, PIE kele- (2)' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/consul' --note 'page 251, node 18: Latin consul < consulere, NOT from concilium' 2>&1 | tail -3"
}
```


### [2026-09-06T16:09:59.769Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4daa56ebf780f714.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/044437dd95a9dd37.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f44926dc6ab11a68.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/45ee1822d27b00c1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a51ef95da574605d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ef2f1a54e18e39c2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3a02bd24b7c44c4f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b66b9b6c6f9db6c5.txt
```


## [2026-09-06T16:10:11.647Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"18.41\\|CALL (vb.)\\|22.15\\|CHURCH\" SYN.txt | head -10"
}
```


### [2026-09-06T16:10:11.698Z] TOOL RESULT

```
3995:3. Ir. ingairim, usual word for ‘herd- ing’ (cattle, etc.) in Laws; epd. of gairim ‘call’ (18.41).
4048:Ir. agaire ‘shepherd’, NIr. aodhaire ‘shepherd’ and ‘herdsman’ (cf. aodhaire bo ‘cowherd’), cpd. of uz ‘sheep’ (3.25), and the root of gairim ‘call’ (18.41).
13189:4. Skt. mila-, perh. (as the plant’s organ of drinking; cf. pdadapa- ‘tree, plant’, lit. ‘drinking with the foot’) : OHG mila ‘mouth, snout’, etc. (4.24) Wackernagel, Berl. Sitzb. 1918.410.
14807:ice’, same word as Ir. acra ‘suing, claim’ vbl. n. to ad-gairim ‘sue, claim’, epd, of gatrim ‘call’ (18.41): K. Meyer, Con. trib. 12.
25959:1022 SELECTED INDO-EUROPEAN SYNONYMS 15.21-24 SMELL 15.21 15.22 15.23 15,24 vb. subj. vb.obj. sb. subj. sb. obj. Grk.  dc¢palvopar ofw dogpyots éou7 (65%) NG pupltw, -ouac nupltw pupword pupwitd Lat. olfacere, odorari olére, fragrare odordtus odor It. sentire, odorare odorare odorato odore Fr. sentir, flairer sentir odorat, flair odeur Sp. oler oler olfato olor Rum, mirost mirost miros mtros Ir. boltigur bolad, boltunud with vb. boltanugud bolad, boltunud Nir. —bolinuighim boladh with vb. boladh boladh W. arogli arogli arogliad arogl Br. chouesa c’houez with vb. c’houesa c’houez Goth. dauns dauns ON pefja, pefa(ilma) pefa, befja(ilma) ilming Pefr (ilmr, daunn) Dan. lugte lugte lugt lugt Sw. lukta lukta lukt lukt OE gestincan, gesweccan stincan slenc, swacc slenc, swacc ME smelle smelle smelle smelle NE smell smell smell smell, odor Du. ruiken ruiken reuk reuk OHG - stincan slincan, riohhan, swehhan  stanc stanc, rouh, sweche MHG riechen, smecken riechen, smecken geruch ey rouch, geruch (stanc, smac) smac NHG riechen riechen geruch geruch Lith. _uostz, uostyti kvepeti uoslé kvapas Lett. uost, uostit uost, smakuot uoza smaka, uoza ChSI. obonjati, achati vonjalt obonjantje, vonja achanije SCr.  mirisati mirisali, vonjali njuh, njusni miris, vonj osjet Boh. iti, Gichati padchnouli, vonéli éich zépach, viiné Pol. wachaé pachnqé wech zapach, wor Russ. njuchat' pachnit’ obonjanie zapach Skt.  ghra- gandha- with vb. ghrana- gandha-, ghrana- Av. bud- baosi-, ganti-
28895:OHG (h)ruom (gl. clamor, gloria, etc., mostly ‘fame, renown’), MHG ruom, NHG ruhm, Du. roem, prob. fr. the same root as Goth. hréps ‘cry’, OHG ruof ‘call’ (NHG ruf), etc. (18.41). Walde-P. 1.353. Weigand-H. 2.621.
31430:18.41 Cau (vb. = Summon) 18.42 Catt (vb. = Name) 18.43 ANNOUNCE
31460:4. Ir. guth, etym. dub., perh. : Skt. havate, Av. zavaiti ‘calls’, etc. (18.41). Walde-P. 1.529 (vs. Pedersen 1.108).
31501:Most of the words for ‘shout, cry out’ are of imitative origin, as are numerous others covering ‘scream, screech, shriek, yell’, etc. (cf. also 18.14). Several of those listed here are also used for ‘call’ = ‘summon’ (18.41).
31522:(now esp. ‘call’, 18.41) with sbs. rufer ie c ) . Goth. hrops, OHG ruof ‘cry’, etc., root ponnection dub., perh. of imitative origin. Walde-P. 1.353. Falk-Torp g65. Feist 270.
```


## [2026-09-06T16:10:12.417Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/class",
 "prompt": "Etymology of class: Latin classis, French classe, relation to calare; also council entry if mentioned."
}
```


### [2026-09-06T16:10:18.628Z] TOOL RESULT

```
# Etymology of Class

The word "class" originated around 1600, initially referring to "group of students." It derives from French *classe* (14th century), which came from Latin *classis*, meaning "a division; army, fleet." 

The Latin term originally referred to "one of the six orders into which Servius Tullius divided the Roman people for taxation purposes." Scholars trace *classis* back to the Latin verb *calare*, meaning "to call (to arms)," which connects to the Proto-Indo-European root *kele- meaning "to shout."

The meaning evolved significantly over time. By the 1660s, it encompassed "an order or rank of persons sharing certain characteristics." The natural history application ("group of related plants or animals") emerged in 1753. The sense describing "high quality" appeared in 1874, while the sociological meaning referencing "division of society according to status" (upper class, lower class, etc.) was documented by 1763.

The related term "class-consciousness" entered English in 1903, borrowed from German *Klassenbewusst*.

As a verb, "class" dates to 1705, meaning "to divide into classes, place in ranks or divisions."
```


## [2026-09-06T16:10:21.371Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '31430,31460p' SYN.txt"
}
```


### [2026-09-06T16:10:21.420Z] TOOL RESULT

```
18.41 Cau (vb. = Summon) 18.42 Catt (vb. = Name) 18.43 ANNOUNCE
18.44 THREATEN
18.45 Boast (vb.)
18.51 Write
18.52 Reap
18.53 Lerrer (of the Alphabet) 18.54 Letrer (= Epistle) 18.55 TABLET
18.56 PAPER
18.57 Pen
18.58 Ink
18.59 Penci
18.61 Boox
18.62 Pace
18.63 Line
18.64 Print (vb.)
18.65 LiTERATURE
18.66 AuTHor, WRITER 18.67 Portr
1247
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1248 SELECTED INDO-EUROPEAN SYNONYMS
18.11 WOICE (sb.)
Grk. dw Goth.  stibna Lith. balsas NG gw ON rodd, raust Lett. balss Lat. vor Dan.  stemme, r¢st ChSl.  glasi It. voce Sw. rést, stamma SCr.  glas Fr. voix OE stefn, reord Boh. hlas Sp. voz ME vois, steven Pol. gtos Rum. voce, glas NE voice Russ. golos Ir. guth Du. stem Skt. vac- Nir. — guth, glor OHG _ stimma, stimna, rarta Av. vdé- W. ais MHG ss stimme
Br. mouez NHG = stimme
Words for ‘voice’ are mostly connect- ed with verbs for ‘speak, say’ (18.21, 22) or are words for the more generic ‘sound’ (15.44), several of which (besides those repeated here) are, as including vocal
-sound, also frequently ‘voice’.
1. Derivs. of IH *wekv- ‘speak, say’ (18.21). Walde-P. 1.245f. Ernout-M. 1185 f.
Grk. dy (poet.); Lat. vdx (> It. voce, Fr. voiz, Sp. voz, Rum. lit. voce); Skt. vdc-, Av. vié- (nom. sg. Skt. vak, Av. vars); Toch. A wak, B wek.
2. Grk. guava : dnl ‘say, speak’ (18.21).
Grk. $0éyyos, see ‘sound’ (15.44).
3. Rum. glas, fr. Slavic (below, 7), but largely replaced in modern lit. lan- guage by voce (above). Tiktin 686.
4. Ir. guth, etym. dub., perh. : Skt. havate, Av. zavaiti ‘calls’, etc. (18.41). Walde-P. 1.529 (vs. Pedersen 1.108).
```


## [2026-09-06T16:10:25.896Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"καλέω\\|kalein\\|Grk. καλῶ\\|calare\\|calāre\" SYN.txt | head -10; echo ===; grep -n \"18.41 CALL\\|18.41 Cati\\|CALL (vb. = Summon)\" SYN.txt | head"
}
```


### [2026-09-06T16:10:25.956Z] TOOL RESULT

```
Exit code 1
17869:OHG halén, holén, MHG, NHG holen, Du. halen (also ‘draw’, cf. ME hale, NE haul) : OE ge-holian ‘get’, perh. Arm. k'atem ‘collect, take away’, Toch. kdl- ‘ead, bring’ (SSS 480). The old com- parison with Lat. calare, Grk. xahéew ‘call’, etc. (Falk-Torp 373, Walde-H. 1.141) is based on the frequent use as ‘call’ in OHG. But the evidence as a whole indicates that this sense is second- ary. Mansion, PBB 33.547 ff. Franck- v. W. 226.
31507:2. Lat. clamare : calare ‘call, out, pro- claim, summon’, Gri. xadéw ‘call, name’, kéhados ‘noise’, Lett. kal’uot ‘chatter’, Lith. kalba ‘language’, etc. Walde-P. 1.443 f. Ernout-M. 136,192. Walde-H. 1.141 f.
31619:calare ‘call together’, clamdre ‘call’, etc. Walde-P. 1.445.
31703:Sp. callar, fr. VLat. *cal@re (It. calare ‘let down the anchor’), fr. Grk. xadéw ‘slacken, let down’. REW 1487.
(eval):1: == not found
```


## [2026-09-06T16:10:28.001Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '31612,31626p' SYN.txt"
}
```


### [2026-09-06T16:10:28.084Z] TOOL RESULT

```
Dan. snakke, lit. ‘chatter, chat’, but also pop. ‘talk, speak’ (snakke dansk, engelsk, etc.), with sb. snak, like Sw. snacka, snak ‘chatter’, fr. MLG snacken, snack ‘talk, chatter, prattle’ (NHG schnacken ‘prattle’), belonging with NE snack ‘snap, bite, seize’, Dan. snage ‘snuff about’, etc., prob. of imitative origin. Falk-Torp 1089. Walde-P. 1.397.
OE sprecan and (later) specan, ME speke, NE speak, Du. spreken, OHG sprehhan (rarely also spehhan), MHG, NHG sprechen, with sbs. OE spréc, NE speech, OS spraka, MLG sprake (> Dan. sprog, Sw. sprék, whence vb. spréka ‘talk’), OHG spracha, NHG sprache, etc. (the history of the r-less forms is obscure, but they are undoubt- edly of secondary origin) : ON spraka, Dan. sprage ‘crackle’, Grk. odapayéw ‘erackle, sputter, hiss’, Lith. spragét ‘erackle’, Skt. sphirj- ‘crackle, rustle, rumble’. Cf. NE crack, dial. ‘chat, talk’ (NED s.v. 7). Walde-P. 2.673. Falk- Torp 1134.
Du. praten, cf. MLG praten, proten, Icel., Sw. prata ‘chatter, prate’, NE prate, etc., prob. of imitative origin. Falk-Torp 847. NED s.v. _ prate. Franck-v. W. 520 (: Pol. bredzié ‘chat- ter, prattle’, but cf. Berneker 83).
6. Lith. kalbéti, with kalba ‘speech, language’ : Lett. kaluot ‘chatter’, OPruss. kelsai ‘they sound’, Grk. xé\a- dos ‘noise, din’, xadéw ‘call, name’, Lat.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1256 SELECTED INDO-EUROPEAN SYNONYMS
calare ‘call together’, clamdre ‘call’, etc. Walde-P. 1.445.
OPruss. billit (renders NHG sprechen and sagen, but wattiatun for reden), OLith. bilti, bylott, common word for ‘speak, say’ (byloti now ‘litigate’), Lett. bilst ‘speak, say’ (not common) : Lith. balsas ‘voice’, OE bellan ‘roar’, Skt. bhas- (*bhel-s-) ‘speak’, etc. Walde-P. 2.182.
Lett. runat, with sb. runa, prob. loan- word fr. some form of the Gme. group seen in OE riinian, OHG rinén ‘whisper’, ON rina ‘speak confidentially’ (with Goth. rina ‘secret’, ON, OE rin ‘secret, rune’, Ir. rin, W. rhin ‘secret’, etc.; Walde-P. 2.350). Miihl.-~Endz. 3.560 (but regarding Lett. form as cognate, not loanword).
7. ChSl. glagolati (cf. Russ. dial golo- golit’ ‘babble, joke’), beside glagolit ‘word’, etc., fr. redupl. form of root in glasti ‘voice’, etc. (18.11). Walde-P. 1.588. Berneker 321.
Ch&l. véstati, with otti-véstati ‘answer’, viz-véstiti, -véstati ‘announce’, vé = ele : OPruss. waitiatun ‘speak’, . fur- ther connections dub. Walde-P. 1.246. Trautmann, Altpreuss. 455 f.
SCr. govoriti, Russ. govorit’ (but Boh. hovoriti ‘chat, converse’) = ChSI. govo- ritt ‘make a noise’, fr. the sb. govorit ‘noise’ (in modern Slavic freq. ‘speech,
language, dialect’) : Lith. gausti ‘how? OE ciegan ‘call’, OHG gikewen ‘call, name’, Grk. yodw ‘lament’, Skt. gy, ‘sound’, etc. Walde-P. 1.635. Ber ker 339.
Boh. mluviti, Pol. méwié = Russ molvit’ ‘ater’, ChSl. mliiviti ‘make a dis. turbance’, beside sbs. Boh. mluva ‘speech’, etc., ChSl. mltiva ‘tumult? prob. : Skt. bra-, Av. mra- ‘speak, say’, but disputed (see below, 8).
```


## [2026-09-06T16:10:38.488Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== RCH\"; grep -n -i \"kunisht\\|kalísá\\|kalisa\\|kanísa\\|kanisa\" RCH.txt | head -12; echo \"== WLD Bd1 kel- rufen\"; grep -n \"rufen, schreien\\|kaléō\\|kal-ā\\|calare\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-06T16:10:38.568Z] TOOL RESULT

```
== RCH
15690:p   bad-kunhh  (or  JJ  bad-kunisht)^  Bad,  evil.
67637:A   kattaniSy  (pi.  of  kanisat)  Birds’  crops.
70938:p   kunisht^  A   fire-temple.  A   Jews’  syna^o^ue.  A
70939:pigsty.  Profession,  occupation,  bad-kunishty  Ma-
== WLD Bd1 kel- rufen
13860:Got. wopjan schw. Y. „schreien, rufen'- £ , aisl.p/xs schw. Y. „rufen, schreien, 
22293:„berichten, melden“ (ahd. haren, heren „rufen, schreien“, Holthausen AfnSpr. 
22302:„rufen, schreien", ahd. ( h)ruoft , mhd. geriiefte , geruofte n. „Ruf, Schrei“, 
22615:huren (s. auch u. qar- „preisen") „rufen, schreien“ haben ihre Bed. kaum 
27922:kel- „rufen, schreien, larmen, klingen". 
33116:Red. -Weise zur Wz. ghel- „rufen, schreien 11 zu sein, wie Berneker 31Sf. 
33771:gar- „rufen, schreien", daneben einzelsprachliches *garr- entw. aus idg. 
33854:2. gal- „rufen, schreien“. 
35631:lit. gausti s. u. gou- , rufen, schreien". Trotz des nicbtpalatalen Wurzel- 
35669:Ygl. *gheup- ds. Erw. beider Wzformen aus (jhan- „rufen, schreien"
```


## [2026-09-06T16:10:40.916Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27922,27960p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-06T16:10:40.971Z] TOOL RESULT

```
kel- „rufen, schreien, larmen, klingen". 

Ai. usa-kala- ,,Hahn“ ( „rji-xavog “ ), kaladhika-, kaldvika- ds., kola- ,,leise 
tonend, undeutlich vernebmbar", kalurmka- „Sperling“ (und anderes von 
noch zweifelhafterem idg. Hintergrund, s. Uhlenbeck Ai. Wb. 48) kalakala- 
m. „verworrenes Geschrei, Gerausch" (kalaha- „Streit, Zank“; vielleicht als 
*kaludha- eine alte Bildung?); Erw. krandati „schreit, briillt, wiehert, 
rauscht, knarrt" (s. xeXadog). 

Gr. Basis x(a)Xrj- in : xaXeco „rufen, nennen, herbeirufen", Futur. xaXeaco, 
att. xaXdj, Pf. xexXrjxa, xXrpcog, imxXtjaig „Beiname“, x.Xrjoig „Ruf, Ein- 
ladung, Vorladung", xaXrjrwg ,.Rufer“, d/ioxXr/ „Zuruf‘‘ (zum I. Glied s. u. 
*omo-; o/uoxXa Aesch. ist nach Jacobsohn KZ. 42, 159f. entweder kunst- 
licher Dorismus oder von einem Adj. *6/uoxXog abgeleitetes Abstraktum; 
ein dem lat. cola-, cld- entsprechendes gr. xaXd-, xXa- gibt es nicht, siehe 
Fraenkel aaO., Persson Beitr. 701, Reichelt KZ. 46, 325 f. gegen Hirt 
Abl. 86, Gr. Laut- und Formenlehre 127), xixXijoxo) (oder xixXrjoxco) „rufe 
an, flehe", -/.X-rji^co, xXrj£ai „nenne“ (von *xXi]-fo-g, s. Fraenkel Gl. 4, 36); 
hochstufig xeXa- in xeXaQv^m „rausche, riesle (Wasser u. dgl. .“, xeXcoq' 
<pmvp Hes., xeXcoqveiv fioav Phot. (s. Boisacq s. v.); Erw. xeX.adog „Getose, 
Larm“, xeXadcov, xeXadeivog „brausend“, xeXadeco „tose; lasse (einen Ge- 
sang) erklingen" (gr. xeXad- vielleicht mit a = n zu ai. Iranduti, cakrade, 
Zupitza KZ. 36, 55). 

Sehr unsicher arg. xaXatg, -Idog „Hahn? Henne?" (Meister BSG\Y. 1899, 



444 


kel- 


15-4 f., Dittenberger Syll. 3 998) — sicher verschieden davon -y.dU.aiov 
„Hahnenkamm, Hahnenbart, die schillernden Schwanzfedern des Hahns", 
das wohl als „Zierstuck" zu to y.dllog. 

Umbt'. kafitu, karsetu , cars'du „calato, appellato" (*A aletbcl-, Lit. bei Yf.
```


## [2026-09-06T16:10:50.252Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\" incoming/ARY/ARY_latin_index_pages.txt; grep -n -i \"CLASS\\|KELAS\\|KELISA\\|CONCIL\\|CALARE\\|EKKLESIA\" incoming/ARY/ARY_latin_index_pages.txt | head; echo \"== ARY persian\"; grep -n \"کلاس\\|کلیسا\\|کنشت\\|کنسول\" incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-09-06T16:10:50.328Z] TOOL RESULT

```
15967
725:Jeb y Kind 9 065 iI Lp pa a gl ‘pF (CLASSICAL GREEK)
9012:het aly oat Nis "oat" “okt” "ty SS eulh class
9823:($42: POKORNY) atlas arly cae jl id “a2yn" 9 "Oe" y dagle” goth classy -¥
== ARY persian
743:بعد از حدود ۸۰۰ سال پیش از میلاد به نوشته‌های فراوانی به زبان یونانی کلاسیک
749:آثار فلسفی و تاریخ ی گوناگون. زبان یونانیکلاسیکه به ندریج تبدیل به یونانی نوین شد. سخنگویان
898:هندوستانی پونانی کلاسیک :
```


## [2026-09-06T16:11:08.750Z] TOOL CALL #62: Bash

```json
{
 "command": "ls -la data/verification/sources/refs/ocr/BQT/ | grep -E \"1688|1709\""
}
```


### [2026-09-06T16:11:08.790Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb 171693 Sep  6 12:07 1688.png
-rw-rw-r--  1 sfmqrb sfmqrb   3776 Sep  6 12:07 1688.txt
-rw-rw-r--  1 sfmqrb sfmqrb 163959 Sep  6 12:07 1709.png
-rw-rw-r--  1 sfmqrb sfmqrb   3832 Sep  6 12:08 1709.txt
-rw-rw-r--  1 sfmqrb sfmqrb 168820 Sep  5 16:29 1819.png
```


## [2026-09-06T16:11:14.328Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 -c \"\nfrom PIL import Image\nim=Image.open('data/verification/sources/refs/ocr/BQT/1688.png')\nprint(im.size)\nw,h=im.size\nim.crop((0,int(h*0.80),w,h)).resize((int(w*1.8),int(h*0.20*1.8))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1688_fn.png')\nim2=Image.open('data/verification/sources/refs/ocr/BQT/1709.png')\nw,h=im2.size\nim2.crop((0,int(h*0.72),w,h)).resize((int(w*1.7),int(h*0.28*1.7))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1709_fn.png')\n\""
}
```


### [2026-09-06T16:11:17.416Z] TOOL RESULT

```
(1650, 2546)
```


## [2026-09-06T16:11:19.852Z] TOOL CALL #64: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1688_fn.png"
}
```


### [2026-09-06T16:11:20.092Z] TOOL RESULT

```

```


## [2026-09-06T16:11:20.089Z] INPUT

[Image: original 2970x916, displayed at 2000x617. Multiply coordinates by 1.49 to map to original image.]


## [2026-09-06T16:11:32.331Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1709_fn.png"
}
```


### [2026-09-06T16:11:32.670Z] TOOL RESULT

```

```


## [2026-09-06T16:11:32.667Z] INPUT

[Image: original 2805x1211, displayed at 2000x863. Multiply coordinates by 1.40 to map to original image.]


## [2026-09-06T16:11:38.797Z] TOOL CALL #66: Bash

```json
{
 "command": "python3 -c \"\nfrom PIL import Image\nim=Image.open('data/verification/sources/refs/ocr/BQT/1709.png')\nw,h=im.size\nim.crop((0,int(h*0.60),w,int(h*0.76))).resize((int(w*1.9),int(h*0.16*1.9))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1709_fn2.png')\n\""
}
```


### [2026-09-06T16:11:40.740Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:11:43.467Z] TOOL CALL #67: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1709_fn2.png"
}
```


### [2026-09-06T16:11:43.672Z] TOOL RESULT

```

```


## [2026-09-06T16:11:43.670Z] INPUT

[Image: original 3135x773, displayed at 2000x493. Multiply coordinates by 1.57 to map to original image.]


## [2026-09-06T16:12:13.309Z] TOOL CALL #68: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BQT data/verification/sources/refs/ocr/BOOK && cat > data/verification/sources/refs/ocr/BQT/1688.vision.txt <<'EOF'\n[read from the page image by vision, 2026-09-06; Borhan-e Qate' ed. Mo'in, printed p. 1688 = BQT_v3_picofile.pdf page 481]\n\nHeadword (right column, entry «کلیسا ۵»):\nکلیسا ۵ » بکسر اول و ثانی بتخفیف یائی مجهول رسیده، و سین بی‌نقطه بالف رسیده، مخفف\nکلیسیا است که جای پرستش و معبد ترسایان باشد.\n\nMo'in's etymological footnote 5 at the foot of p. 1688 (verbatim):\n«۵ ـ کلیسا ، کلیسیا ـ از یونانی ékklēsía ، «زابا ص ۳۴۱» ، در پهلوی kilîsyâk گاه در مورد\nمعبد ساری بکار رفته ( داراب دستور پشوتن سنجانا : ملاحظاتی در باب فرضیهٔ دارمستتر\nدرخصوص نامهٔ تنسر ص ۱۶ ) . رک : کنشت .»\n\n[i.e. \"kilīsā, kilīsiyā — from Greek ékklēsía ('Zābā' p. 341); in Pahlavi kilîsyâk, sometimes\nused of the temple of Sāri (Darab Dastur Peshotan Sanjana, Remarks on Darmesteter's\nhypothesis concerning the Nāma-i Tansar, p. 16). See: kiništ.\"]\nEOF\ncat > data/verification/sources/refs/ocr/BQT/1709.vision.txt <<'EOF'\n[read from the page image by vision, 2026-09-06; Borhan-e Qate' ed. Mo'in, printed p. 1709 = BQT_v3_picofile.pdf page 502]\n\nHeadword (entry «کنشت»):\nکنشت ـ بفتح اول و ثانی و سکون سین بی‌نقطه و فوقانی ، آتشکده و آتشخانه را گویند …\n… و مخفف کنشت هم هست که آتشکده و معبد یهودان باشد ۶ .\n\nMo'in's etymological footnote 6 at the foot of p. 1709 (verbatim):\n«۶ ـ در رسم‌الخط پهلوی kanashyâ ( مجمع ) « بلوشه . دستور پهلوی ص ۲۵ » ، عبری\nkeneseth ( جامعه ) رک : E. Müller , History of Jewish Mysticism , p. 109 ، آرامی\n«کنوشتا» ( کنیسه ) « تفس » ، بنابرین بفتح اول صحیح است ، رک : کنست ، کنیسه (معرب) ،\nکلیسا ، کلیسیا .»\n\n[i.e. \"in Pahlavi orthography kanashyâ 'assembly' (Blochet, Dastur-e Pahlavi p. 25); Hebrew\nkeneseth 'congregation' (see E. Müller, History of Jewish Mysticism, p. 109); Aramaic\nkᵉnūštā (= kanīsa). Therefore the form with fatha on the first letter is the correct one.\nSee: kanist, kanīsa (Arabicised), kilīsā, kilīsiyā.\"]\nEOF\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg251.png data/verification/sources/refs/ocr/BOOK/251.png && ls -la data/verification/sources/refs/ocr/BOOK/251.png data/verification/sources/refs/ocr/BQT/*.vision.txt"
}
```


### [2026-09-06T16:12:15.138Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 75263 Sep  6 12:12 data/verification/sources/refs/ocr/BOOK/251.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1076 Sep  4 15:27 data/verification/sources/refs/ocr/BQT/103.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   818 Sep  6 11:40 data/verification/sources/refs/ocr/BQT/1219.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1254 Sep  4 14:18 data/verification/sources/refs/ocr/BQT/1225.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   741 Sep  6 11:43 data/verification/sources/refs/ocr/BQT/1280.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1085 Sep  5 22:32 data/verification/sources/refs/ocr/BQT/1294.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   573 Sep  5 22:32 data/verification/sources/refs/ocr/BQT/1299.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   238 Sep  5 22:32 data/verification/sources/refs/ocr/BQT/1300.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   284 Sep  5 22:32 data/verification/sources/refs/ocr/BQT/1302.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2008 Sep  4 14:34 data/verification/sources/refs/ocr/BQT/1385.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1790 Sep  4 19:14 data/verification/sources/refs/ocr/BQT/1445.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   797 Sep  6 11:43 data/verification/sources/refs/ocr/BQT/1564.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1691 Sep  6 11:41 data/verification/sources/refs/ocr/BQT/1572.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2183 Sep  6 11:32 data/verification/sources/refs/ocr/BQT/1578.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1332 Sep  6 11:56 data/verification/sources/refs/ocr/BQT/1637.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   580 Sep  6 12:02 data/verification/sources/refs/ocr/BQT/1648.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1084 Sep  6 12:12 data/verification/sources/refs/ocr/BQT/1688.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2123 Sep  6 11:45 data/verification/sources/refs/ocr/BQT/1689.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1192 Sep  6 12:12 data/verification/sources/refs/ocr/BQT/1709.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1484 Sep  5 16:15 data/verification/sources/refs/ocr/BQT/172.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3319 Sep  6 11:37 data/verification/sources/refs/ocr/BQT/1774.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1117 Sep  5 22:20 data/verification/sources/refs/ocr/BQT/1786.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3889 Sep  6 11:01 data/verification/sources/refs/ocr/BQT/1803.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1288 Sep  5 01:39 data/verification/sources/refs/ocr/BQT/180.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1196 Sep  5 01:39 data/verification/sources/refs/ocr/BQT/181.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   979 Sep  6 11:00 data/verification/sources/refs/ocr/BQT/1854.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   668 Sep  6 11:00 data/verification/sources/refs/ocr/BQT/2023.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1063 Sep  5 02:20 data/verification/sources/refs/ocr/BQT/220.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1558 Sep  6 11:26 data/verification/sources/refs/ocr/BQT/2242.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   805 Sep  4 19:14 data/verification/sources/refs/ocr/BQT/2246.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   561 Sep  6 11:25 data/verification/sources/refs/ocr/BQT/2417.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2009 Sep  6 11:17 data/verification/sources/refs/ocr/BQT/2420.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1757 Sep  5 16:28 data/verification/sources/refs/ocr/BQT/2427.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2615 Sep  4 15:28 data/verification/sources/refs/ocr/BQT/31.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1339 Sep  5 16:12 data/verification/sources/refs/ocr/BQT/333.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1508 Sep  4 15:27 data/verification/sources/refs/ocr/BQT/58.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1931 Sep  4 15:02 data/verification/sources/refs/ocr/BQT/70.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1606 Sep  4 14:54 data/verification/sources/refs/ocr/BQT/72.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1152 Sep  5 01:39 data/verification/sources/refs/ocr/BQT/733.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1658 Sep  5 16:20 data/verification/sources/refs/ocr/BQT/902.vision.txt
```


## [2026-09-06T16:12:17.726Z] TOOL CALL #69: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T16:12:17.775Z] TOOL RESULT

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


## [2026-09-06T16:13:45.098Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/council",
 "prompt": "Etymology of council: Old French concile/cuncile, Latin concilium, con- + calare, and the note about confusion with counsel."
}
```


### [2026-09-06T16:13:50.097Z] TOOL RESULT

```
# Etymology of "Council"

The word **council** originates from early 12th-century Anglo-French *cuncile*, derived from Old French *concile* and Latin *concilium*, meaning "a meeting, a gathering of people."

The Latin root combines the prefix *con-* ("with, together") with *calare* ("to announce, summon"), which traces back to the Proto-Indo-European root *\*kele-* meaning "to shout." As the source notes, "the notion is of a calling together."

Interestingly, as stated in the dictionary, "the tendency to confuse it in form and meaning with counsel has been consistent since 16c." This confusion persists today, though *councilor* (a member of a council) and *counselor* (one who counsels) represent the modern distinction—though both words historically shared overlapping origins and meanings.
```


## [2026-09-06T16:13:54.184Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://www.etymonline.com/word/class' --note 'page 251, nodes 11-14: class < F classe < L classis < calare, PIE kele- (2)' 2>&1|tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/council' --note 'page 251, nodes 15-18: council < OF concile/cuncile < L concilium < con- + calare' 2>&1|tail -2"
}
```


### [2026-09-06T16:13:56.793Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c4c6313ab9e4aaf7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/df29197cad8fa202.txt
```


## [2026-09-06T16:23:44.985Z] TOOL CALL #72: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk251.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_KELISA = \"https://en.wiktionary.org/wiki/%DA%A9%D9%84%DB%8C%D8%B3%D8%A7\"\nW_KANISA = \"https://en.wiktionary.org/wiki/%D9%83%D9%86%D9%8A%D8%B3%D8%A9\"\nW_KENESHT = \"https://en.wiktionary.org/wiki/%DA%A9%D9%86%D8%B4%D8%AA\"\nW_KNESSET = \"https://en.wiktionary.org/wiki/%D7%9B%D7%A0%D7%A1%D7%AA\"\nW_KNISHTA = \"https://en.wiktionary.org/wiki/%D7%9B%D7%A0%D7%99%D7%A9%D7%AA%D7%90\"\nW_PIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/kelh%E2%82%81-\"\nE_ECCL = \"https://www.etymonline.com/word/ecclesiastic\"\nE_CONSUL = \"https://www.etymonline.com/word/consul\"\nE_CLASS = \"https://www.etymonline.com/word/class\"\nE_COUNCIL = \"https://www.etymonline.com/word/council\"\n\nPOK_Q = (\"POK_02.txt leaf NR=207-208 (= printed pp. 548-549): \"\n         \"„6. kel-, k(e)lē-, k(e)lə- oder kl-? ‚rufen, schreien, lärmen, klingen‘“, \"\n         \"with gr. καλέω, lat. calō -āre, calendae, concilium (*cōn-caliom), \"\n         \"clāmō, clārus, classis (*klad-ti-)\")\n\nnodes = []\n\ndef N(i, lang, words, verdict, deriv, deriv_fa, sources, refc, cons, **extra):\n    d = {\"id\": i, \"lang\": lang, \"words\": words, \"verdict\": verdict,\n         \"derivation\": deriv, \"derivation_fa\": deriv_fa,\n         \"sources\": sources, \"ref_check\": refc, \"consulted\": cons}\n    d.update(extra)\n    nodes.append(d)\n\nN(1, \"Greek\", \"ek-kalein; ekklesia\", \"confirmed\",\n  \"Greek kaléō 'I call, summon' continues PIE *kelh₁- 'to call out' (Pokorny 6. kel- 548). \"\n  \"The compound ek-kaleîn 'to call out, summon forth' (ek 'out' + kaleîn) yields the verbal adjective \"\n  \"ékklētos 'called out', whence ekklēsía, in classical Athens the assembly of citizens summoned \"\n  \"by the herald (5th c. BCE, Thucydides, Aristophanes). The Septuagint used ekklēsía to render Hebrew \"\n  \"qāhāl 'congregation', and in New Testament and patristic Greek it became 'church', the sense in which \"\n  \"it travelled east (Syriac, Middle Persian, Armenian) and west (Latin ecclesia). Root, language and glosses \"\n  \"in the chart are all correct.\",\n  \"یونانی kaléō «خواندن، فراخواندن» دنبالهٔ ریشهٔ هندواروپایی آغازین *kelh₁- «بانگ زدن، صدا کردن» است (پوکورنی ص۵۴۸). \"\n  \"از پیوند ek- («بیرون») و kaleîn فعل ek-kaleîn «فراخواندن» و از صفت مفعولی آن (ékklētos) اسم ekklēsía \"\n  \"«انجمن شهروندان آتن» ساخته شده است. در ترجمهٔ سبعینی این واژه برابر «قهال» عبری نشست و در یونانی مسیحی معنای «کلیسا» گرفت. \"\n  \"ادعای نورایی درست است.\",\n  [W_PIE, E_ECCL],\n  [{\"ref\": \"POK:548\", \"status\": \"supports\", \"note\": POK_Q + \" — the Greek members of the root are given first.\"},\n   {\"ref\": \"AHD:412\", \"status\": \"not_checked\", \"note\": \"AHD:412 is a page of the 1975 New College main dictionary (s.v. ecclesia/ecclesiastic), not on disk; the Watkins IE-roots appendix of the same AHD does list ECCLESIA under kelə-² 'To shout' (AHD_watkins1985.txt leaf 608: 'Suffixed form *kal-e- in Greek kalein (variant klē-), to call: ECCLESIA, PARACLETE. [Pok. 6. kel- 548.]').\"}],\n  [{\"src\": \"POK\", \"where\": \"Bd. I pp. 548-549 (POK_02.txt leaf 207)\", \"stance\": \"supports\", \"note\": POK_Q},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, kelə-² (leaf 608)\", \"stance\": \"supports\", \"note\": \"'Suffixed form *kal-e- in Greek kalein (variant klē-), to call: ECCLESIA, PARACLETE.'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. ecclesia (KLN_1966.txt)\", \"stance\": \"supports\", \"note\": \"'ecclesia ... fr. Gk. ἐκκλησία, ‘an assembly of citizens’, in Eccles. Gk. ‘church’, fr. ἔκκλητος, ‘called out, summoned’, verbal adj. of ἐκκαλεῖν, ‘to call out, summon forth’, fr. ἐκ ... and καλεῖν, ‘to call, summon’.'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p. 443 (WLD_Bd1 djvu line 27922 ff.)\", \"stance\": \"supports\", \"note\": \"'kel- „rufen, schreien, lärmen, klingen“ ... Gr. Basis κ(α)λη- in: καλέω „rufen, nennen, herbeirufen“.'\"}])\n\nN(2, \"Pahlavi\", \"kilîsyâk\", \"plausible\",\n  \"Mo‘in's own etymological footnote to Borhan-e Qate‘ p. 1688 gives exactly this form: 'از یونانی \"\n  \"ékklēsía ... در پهلوی kilîsyâk گاه در مورد معبد ساری بکار رفته', citing Darab Dastur Peshotan Sanjana. \"\n  \"Phonetically a Middle Persian *kilīsyāk is a regular adaptation with the productive MP suffix -āk on a \"\n  \"borrowed stem kilīsyā-, and the loss of the Greek initial e- (aphaeresis) matches the eastern Christian \"\n  \"forms. The route, however, is almost certainly not direct: Sasanian Christian vocabulary reached Iran \"\n  \"through Syriac (Syr. ʾeqlēsyā / qlēsyā 'church'), and Nourai's arrow Greek → Pahlavi silently omits \"\n  \"that Syriac stage. The form is absent from MacKenzie's Concise Pahlavi Dictionary and from Nyberg's \"\n  \"glossary, so it rests on Mo‘in's citation alone — hence 'plausible' rather than 'confirmed'.\",\n  \"معین در حاشیهٔ برهان قاطع (ص ۱۶۸۸) خود صریحاً می‌نویسد «در پهلوی kilîsyâk گاه در مورد معبد ساری بکار رفته»؛ \"\n  \"پس صورت فارسی میانه از نظر منبع مورد استناد نورایی مستند است. پسوند -āk پهلوی و افتادن e- آغازین یونانی دگرگونی‌های معمول وام‌گیری است. \"\n  \"اما وام‌گیری اغلب بی‌واسطه از یونانی نبوده، بلکه از راه سریانی (qlēsyā) به ایران رسیده و نورایی این حلقه را حذف کرده است؛ \"\n  \"مکنزی و نیبرگ نیز چنین مدخلی ندارند. پس با احتیاط پذیرفتنی است.\",\n  [W_KELISA],\n  [{\"ref\": \"MON:3050\", \"status\": \"partial\", \"note\": \"Only the 2-vol Adena abridgement of Mo‘in is on disk; its کلیسا entry (MON_part2.txt l.25894) reads '[- کلسا - کلسه. قس. کنشت، کنیسه (معر.)] معبد ترسایان، محل عبادت مسیحیان' — the abridgement drops the Latin-script Pahlavi form, so p. 3050 of the full Farhang could not be seen; but Mo‘in's identical footnote in BQT:1688 does give kilîsyâk.\"},\n   {\"ref\": \"BQT:1688\", \"status\": \"supports\", \"note\": \"not cited by Nourai for this node but by the same editor: footnote 5, p. 1688, 'در پهلوی kilîsyâk گاه در مورد معبد ساری بکار رفته' (read from the page image; saved to data/verification/sources/refs/ocr/BQT/1688.vision.txt).\"}],\n  [{\"src\": \"BQT\", \"where\": \"p. 1688 footnote 5 (BQT_v3_picofile.pdf p. 481)\", \"stance\": \"supports\", \"note\": \"'کلیسا ، کلیسیا ـ از یونانی ékklēsía ، «زابا ص ۳۴۱» ، در پهلوی kilîsyâk ...'\"},\n   {\"src\": \"PHD\", \"where\": \"grep 'klys', 'kilis', 'church' in PHD.txt / PHD_mackenzie.txt\", \"stance\": \"silent\", \"note\": \"MacKenzie has no entry for a Middle Persian word for 'church'; nothing found.\"},\n   {\"src\": \"NYB\", \"where\": \"grep 'kanis', 'klys', 'church' in NYB_vol2_glossary.txt\", \"stance\": \"silent\", \"note\": \"Nyberg's glossary has kanicak/kanisk 'female slave' only; no kilīsyāk.\"}])\n\nN(3, \"Persian\", \"kelîsâ\", \"confirmed\",\n  \"New Persian کلیسا / کلیسیا 'church'. Borhan-e Qate‘ p. 1688 defines it 'مخفف کلیسیا است که جای \"\n  \"پرستش و معبد ترسایان باشد' — i.e. kilīsā is the shortened form of kilīsiyā, exactly the pair the chart prints. \"\n  \"Phonetically: Gk. ekklēsía → (Syriac/MP) kilīsyā(k) with loss of the initial e- and of the final -k in New \"\n  \"Persian; the Greek long ē is rendered by Persian ī, and the ending -iyā was contracted to -ā. Kamāl \"\n  \"Esmā‘īl (13th c.) already uses کلیسیا, the form the chart quotes.\",\n  \"«کلیسا» در فارسی نو از یونانی ekklēsía است که از راه سریانی و فارسی میانه (kilīsyāk) به ما رسیده؛ همزهٔ آغازین و کاف پایانی افتاده و -iyā به -ā بدل شده است. \"\n  \"برهان قاطع (ص ۱۶۸۸) می‌نویسد «مخفف کلیسیا است که جای پرستش و معبد ترسایان باشد»؛ همان دو صورتی که در نمودار آمده است. ادعای نورایی درست است.\",\n  [W_KELISA],\n  [{\"ref\": \"BQT:1688\", \"status\": \"supports\", \"note\": \"Headword «کلیسا ۵»: 'مخفف کلیسیا است که جای پرستش و معبد ترسایان باشد' + footnote 5 'از یونانی ékklēsía' (page image read by vision, saved as data/verification/sources/refs/ocr/BQT/1688.vision.txt).\"}],\n  [{\"src\": \"MON\", \"where\": \"کلیسا (MON_part2.txt l.25892-25894)\", \"stance\": \"supports\", \"note\": \"'[- کلسا - کلسه. قس. کنشت، کنیسه (معر.)] معبد ترسایان، محل عبادت مسیحیان.'\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org کلیسا\", \"stance\": \"supports\", \"note\": \"'Borrowed from Ancient Greek ἐκκλησία (ekklēsía)'; alternative forms کلیسیا, کلسیا, کلیسه.\"},\n   {\"src\": \"HRN\", \"where\": \"grep 'kalisa', 'kilisa' in HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss does not treat this loanword.\"}])\n\nN(4, \"Aramaic\", \"kenušta; K.n.s, K.n.š\", \"disputed\",\n  \"The Aramaic word is real — kᵉnīštā / kᵉnūštā 'assembly, synagogue', the determined feminine of the \"\n  \"passive participle of the common Semitic root k-n-š / k-n-s 'to gather' (cf. Heb. kānas, Akk. kanāšu) — \"\n  \"but the arrow that makes it a descendant of Greek ekklēsía is wrong. The two words share nothing beyond \"\n  \"the accident that both mean 'assembly': ekklēsía is a Greek deverbal from kaleîn (PIE *kelh₁-), while \"\n  \"kᵉnīštā is transparently built on a triliteral Semitic root that is attested independently in Akkadian, \"\n  \"Hebrew and Arabic. Nourai's own cited source, al-‘Unaysi (TAD), states the opposite of his arrow in so \"\n  \"many words. Modern Semitic lexicography (Jastrow, Payne Smith, CAL, Klein) knows no Greek etymology for it.\",\n  \"واژهٔ آرامی kᵉnīštā/kᵉnūštā «انجمن، کنیسه» از ریشهٔ سه‌حرفی سامی ک‌ن‌ش (= ک‌ن‌س) «گرد آوردن» ساخته شده و هم‌ریشهٔ کاناس عبری و کنس عربی است؛ \"\n  \"هیچ ربطی با ekklēsía یونانی ندارد و تنها در معنا با آن هم‌نشین است. جالب آنکه منبعی که خود نورایی ارجاع داده (طوبیا العنیسی) صریحاً می‌نویسد \"\n  \"«کنیسة من کنوشتا الارامیة لا من ekklēsía الیونانیة». پژوهش امروزی این پیوند را رد می‌کند.\",\n  [W_KNISHTA, W_KANISA],\n  [{\"ref\": \"TAD:65\", \"status\": \"contradicts\", \"note\": \"al-‘Unaysi, Tafsir al-alfaz al-dakhila, TAD_pages.txt leaf 68 (printed p. ≈ 63-65, i.e. Nourai's page): 'کنیسة — من «کنوشتا» الارامیة لا من ἐκκλησία الیونانیة ومعناها المجمع والجماعة' — 'from Aramaic kᵉnūštā, NOT from Greek ekklēsía'. The very reference Nourai cites denies his arrow.\"}],\n  [{\"src\": \"KLN\", \"where\": \"p. 849 s.v. Kneseth (KLN_1966.txt leaf 457)\", \"stance\": \"partial\", \"note\": \"'... Heb. kanas, ‘he gathered, assembled, collected’, which is rel. to Aram. kᵉnash, ‘he gathered, assembled, collected’ (whence bē kᵉnishtā, ‘synagogue’)' — the Aramaic word and its Semitic root, with no Greek source.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"כנישתא (Aramaic)\", \"stance\": \"partial\", \"note\": \"'gathered, collected' (adj., det. כנישתא), descendant Lishana Deni knəšta 'synagogue'; sources CAL, Jastrow, Payne Smith — no Greek etymology anywhere.\"},\n   {\"src\": \"BQT\", \"where\": \"p. 1709 footnote 6\", \"stance\": \"supports\", \"note\": \"Mo‘in likewise cites 'آرامی «کنوشتا» (کنیسه)' as the Semitic form, without any Greek link.\"}])\n\nN(5, \"Arabic\", \"k.n.s; kanîseh\", \"plausible\",\n  \"Arabic كنس kanasa 'he swept (a house); he gathered up' is an inherited Semitic root, not a loan; the \"\n  \"chart's gloss 'he gathered, collected, swept' is right. كنيسة kanīsa 'synagogue, church' has native \"\n  \"faʿīla shape, but its religious meaning is a loan from Aramaic kᵉnīštā (the Jewish and Christian \"\n  \"communities of Iraq and Syria supplied the term to Arabic before Islam); Wiktionary calls it 'a semantic \"\n  \"loan from Aramaic', and Mo‘in marks the Persian reflex کنیسه ‘معرّب آرامی’. So the Aramaic → Arabic \"\n  \"arrow is right for the word kanīsa but wrong if read as the source of the root k-n-s itself, and the \"\n  \"Greek grandparent above it is wrong (see node 4).\",\n  \"ریشهٔ عربی ک ن س «روفتن، گرد آوردن» ریشه‌ای اصیل سامی است و وام‌واژه نیست؛ اما معنای دینی «کنیسة» (عبادتگاه یهود و نصارى) وام‌گیری معنایی از آرامی kᵉnīštā است. \"\n  \"از این رو پیکان آرامی ← عربی در مورد خود «کنیسه» پذیرفتنی است، ولی در مورد خود ریشهٔ ک‌ن‌س نه؛ و نیای یونانی آن به کلی نادرست است. با احتیاط پذیرفتنی است.\",\n  [W_KANISA],\n  [{\"ref\": \"SAP:1448\", \"status\": \"not_checked\", \"note\": \"Sayyah's Farhang (Persian translation of al-Munjid) is purchase-only (refs_online.json: 'RE-SEARCH 2026-09: purchase only'); no copy on disk or online.\"}],\n  [{\"src\": \"MON\", \"where\": \"کنیس/کنیسه (MON_part2.txt l.27536-27545)\", \"stance\": \"supports\", \"note\": \"'کنیس: [معر. آرمی؛ آرا. ← کنشت] معبد یهود' ... 'کنیسه ... معبد یهود و نصاری. ضح.— کنیسه در عربی معبد یهود و نصاری را گفته‌اند ... (اقرب الموارد).'\"},\n   {\"src\": \"Wiktionary\", \"where\": \"كنيسة (Arabic)\", \"stance\": \"supports\", \"note\": \"root ك ن س 'congregation and sweeping together'; the synagogue sense is 'a semantic loan from Aramaic כְּנִישְׁתָּא (kənīštā)'.\"},\n   {\"src\": \"AFA\", \"where\": \"Fraenkel p. 274 (AFA.txt leaf 304)\", \"stance\": \"silent\", \"note\": \"Fraenkel discusses بيعة bīʿa 'Die Kirche ... schon durch die Lautverschiebung als aramäisch gesichert' but has no kanīsa entry in the OCR.\"},\n   {\"src\": \"TAD\", \"where\": \"leaf 68 (printed p. ≈ 63-65)\", \"stance\": \"contradicts\", \"note\": \"'کنیسة — من «کنوشتا» الارامیة لا من ἐκκλησία الیونانیة' — contradicts the Greek ancestry, supports the Aramaic one.\"}])\n\nN(6, \"Persian\", \"kans; kannâs; kanîseh\", \"confirmed\",\n  \"All three are Arabic loans in Persian and the arrow Arabic → Persian is right for each. کَنس kans is the \"\n  \"Arabic verbal noun (maṣdar) of kanasa, which Mo‘in glosses exactly as the chart does: '[ع.] (مص م.) \"\n  \"روفتن خانه را'. کَنّاس kannās is the faʿʿāl intensive/professional noun 'sweeper, street-cleaner, \"\n  \"night-soil man' ('[ع.] (ص.) کسی که خاشاک و خاکروبه از خانه‌ها برد، رفتگر'). کَنیسه kanīse \"\n  \"'synagogue' is the Arabicised (معرّب) form of the Aramaic word, so it is a doublet of the directly \"\n  \"borrowed کنشت of node 9 — the same Aramaic etymon reaching Persian twice, once through Arabic and once \"\n  \"not.\",\n  \"هر سه واژه وام‌واژهٔ عربی‌اند: «کَنس» مصدر عربی از کَنَس «روفتن خانه»، «کَنّاس» بر وزن فَعّال (اسم شغل و مبالغه) «رفتگر»، \"\n  \"و «کَنیسه» معرّب همان واژهٔ آرامی است. پس «کنیسه» و «کنشت» دوگانه (doublet) یکدیگرند؛ یکی از راه عربی و دیگری مستقیم از آرامی. \"\n  \"در این حلقه ادعای نورایی درست است.\",\n  [W_KANISA],\n  [{\"ref\": \"MON:3105,3096\", \"status\": \"supports\", \"note\": \"Mo‘in (2-vol abridgement, MON_part2.txt): 'کنس: [ع.] (مص م.) روفتن خانه را' (l.27180); 'کناس: [ع.] (ص.) کسی که خاشاک و خاکروبه از خانه‌ها برد، رفتگر، زباله‌کش' (l.26757); 'کنیسه: [معر. آرمی …] معبد یهود و نصاری' (l.27540). All three glosses match the chart.\"}],\n  [{\"src\": \"BQT\", \"where\": \"p. 1709 footnote 6\", \"stance\": \"supports\", \"note\": \"cross-reference 'رک: کنست، کنیسه (معرب)، کلیسا، کلیسیا' — Mo‘in explicitly labels کنیسه the Arabicised form.\"},\n   {\"src\": \"ARY\", \"where\": \"grep کنیسه/کناس in ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"Aryanpur's dictionary of Indo-European roots of Persian has no entry — as expected for Semitic loans.\"},\n   {\"src\": \"HRN\", \"where\": \"grep 'kanisa', 'kannas' in HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn excludes Arabic loanwords; nothing found.\"}])\n\nN(7, \"Hebrew\", \"kânas; keneseth\", \"plausible\",\n  \"Both words are real: Biblical/Mishnaic Hebrew kānas 'he gathered, assembled' and keneset 'assembly, \"\n  \"congregation' (bêt ha-keneset 'synagogue', a calque behind Greek synagōgē). But the drawn descent \"\n  \"Aramaic → Hebrew overstates the relation: Klein, Nourai's own source, says the Hebrew stem 'is rel. to \"\n  \"Aram. kᵉnash' — i.e. cognate, both continuing a Common Semitic root k-n-s/k-n-š, not a borrowing. What \"\n  \"is genuinely Aramaic-influenced is the Mishnaic usage (bêt ha-keneset modelled on bē kᵉnishtā). The \"\n  \"ultimate Greek/PIE ancestry implied by the chart is wrong.\",\n  \"هر دو واژهٔ عبری درست‌اند: kānas «گرد آورد» و keneset «انجمن». ولی پیکان «آرامی ← عبری» دقیق نیست؛ کلاین می‌گوید \"\n  \"ریشهٔ عبری «هم‌ریشه» (cognate) با kᵉnaš آرامی است نه وام‌گرفته از آن؛ هر دو ادامهٔ یک ریشهٔ مشترک سامی‌اند. \"\n  \"تنها کاربرد «بیت الکنیست» در عبری مشنایی زیر تأثیر آرامی است. نیای یونانی در نمودار رد می‌شود.\",\n  [W_KNESSET],\n  [{\"ref\": \"KLN:849\", \"status\": \"partial\", \"note\": \"KLN_1966.txt leaf 457 (= printed pp. 848-849), s.v. Kneseth: 'Mishnaic Heb. keneseth, ‘gathering, assembly’ (cp. beth kᵉneseth, ‘synagogue’ lit. ‘house of assembly’), from the stem of Heb. kanas, ‘he gathered, assembled, collected’, which is rel. to Aram. kᵉnash'. Klein has the words and the Aramaic connection, but as cognacy, not descent — and no Greek/IE source.\"}],\n  [{\"src\": \"Wiktionary\", \"where\": \"כנסת (Hebrew)\", \"stance\": \"supports\", \"note\": \"'a coming together, a congregating, an assembly'; 'derives from the Semitic root כ־נ־ס (k-n-s)' — Semitic, not Greek.\"},\n   {\"src\": \"BQT\", \"where\": \"p. 1709 footnote 6\", \"stance\": \"supports\", \"note\": \"Mo‘in lists 'عبری keneseth (جامعه)' beside the Aramaic and Pahlavi forms, i.e. as parallel Semitic cognates.\"},\n   {\"src\": \"TAD\", \"where\": \"leaf 68\", \"stance\": \"contradicts\", \"note\": \"explicitly rules out the Greek source for this Semitic word-family.\"}])\n\nN(8, \"Pahlavi\", \"kanašya\", \"plausible\",\n  \"The form is not Nourai's invention: Mo‘in's footnote to Borhan-e Qate‘ p. 1709 records 'در رسم‌الخط \"\n  \"پهلوی kanashyâ (مجمع)', citing Blochet's Dastur-e Pahlavi p. 25 — a Pahlavi/Pazand spelling of the \"\n  \"Aramaic word, of the same type as the many Aramaic religious and chancery terms taken into Middle \"\n  \"Persian. Two things in the chart are wrong: the parent should be the Aramaic kᵉnīštā/kᵉnūštā, not \"\n  \"Hebrew kāneseth (Wiktionary derives Persian کنشت straight from Aramaic, and MP had constant Aramaic, \"\n  \"not Hebrew, contact), and the ultimate Greek ancestry is spurious. Neither MacKenzie's CPD nor Nyberg's \"\n  \"glossary lists the word, so the form rests on Blochet via Mo‘in.\",\n  \"صورت kanašyā را معین در حاشیهٔ برهان قاطع (ص ۱۷۰۹) از بلوشه نقل کرده است: «در رسم‌الخط پهلوی kanashyâ (مجمع)»؛ \"\n  \"پس واژه مستند است، هرچند در فرهنگ مکنزی و نیبرگ نیامده است. اما پدر آن باید «کنوشتای» آرامی باشد نه کنست عبری؛ \"\n  \"زبان واسط فارسی میانه همواره آرامی بوده است. با احتیاط پذیرفتنی است.\",\n  [W_KENESHT],\n  [{\"ref\": \"MON:3096\", \"status\": \"partial\", \"note\": \"Mo‘in's کنشت entry in the 2-vol abridgement (MON_part2.txt l.27253) reads 'کنشت: [کنشتا. قس. کلیسا، کنیسه] (ا.) معبد یهودان' — it gives the Aramaic kᵉnīštā as the source and no Hebrew intermediate; the full Farhang p. 3096 is not on disk.\"},\n   {\"ref\": \"BQT:1709\", \"status\": \"supports\", \"note\": \"footnote 6, p. 1709: 'در رسم‌الخط پهلوی kanashyâ (مجمع) «بلوشه. دستور پهلوی ص ۲۵»' (read from the page image, saved to data/verification/sources/refs/ocr/BQT/1709.vision.txt).\"}],\n  [{\"src\": \"BQT\", \"where\": \"p. 1709 fn 6\", \"stance\": \"supports\", \"note\": \"gives kanashyâ (Pahlavi), keneseth (Hebrew) and kᵉnūštā (Aramaic) as a set of parallel forms.\"},\n   {\"src\": \"PHD\", \"where\": \"grep 'knst', 'kynšt', 'kaništ' in PHD.txt\", \"stance\": \"silent\", \"note\": \"MacKenzie has no such headword.\"},\n   {\"src\": \"NYB\", \"where\": \"grep 'kaniš', 'knš' in NYB_vol2_glossary.txt\", \"stance\": \"silent\", \"note\": \"only kanicak/kanisk 'female slave'; nothing for 'assembly'.\"}])\n\nN(9, \"Persian\", \"kenešt\", \"confirmed\",\n  \"New Persian کِنِشت / کَنِشت, a non-Muslim house of worship (in the classical poets a synagogue, but also \"\n  \"a fire-temple or church); attested from Nāṣer-e Khosrow (11th c.) and Sa‘di, and the Hāfez line the chart \"\n  \"quotes. Borhan-e Qate‘ p. 1709 gives the headword ('آتشکده و معبد یهودان باشد') and Mo‘in's \"\n  \"footnote argues from the Pahlavi form kanashyā that the vowel should be a: 'بنابرین بفتح اول صحیح \"\n  \"است', which is precisely why the chart prints both کِنِشت and کَنِشت. The word is a direct borrowing \"\n  \"of Aramaic kᵉnīštā (Aramaic -štā > Persian -št with loss of the determined ending), a doublet of کنیسه \"\n  \"which came the long way round through Arabic.\",\n  \"«کنشت» در فارسی نو عبادتگاه غیرمسلمانان (به‌ویژه یهودیان) است و از ناصرخسرو و سعدی تا حافظ به کار رفته است. \"\n  \"از آرامی kᵉnīštā وام گرفته شده (پایانهٔ معرفهٔ -ā افتاده) و دوگانهٔ «کنیسه» است که از راه عربی آمده است. \"\n  \"معین بر پایهٔ صورت پهلوی می‌گوید «بنابرین بفتح اول صحیح است»؛ همین سبب دو ضبط نمودار است.\",\n  [W_KENESHT],\n  [{\"ref\": \"BQT:1709\", \"status\": \"supports\", \"note\": \"Headword 'کنشت — بفتح اول و ثانی و سکون سین بی‌نقطه و فوقانی، آتشکده و آتشخانه را گویند ... و مخفف کنشت هم هست که آتشکده و معبد یهودان باشد' with footnote 6 (Pahlavi kanashyâ, Hebrew keneseth, Aramaic کنوشتا).\"}],\n  [{\"src\": \"MON\", \"where\": \"کنشت (MON_part2.txt l.27253)\", \"stance\": \"supports\", \"note\": \"'[کنشتا. قس. کلیسا، کنیسه] (ا.) معبد یهودان (خصوصا). عبادتگاه کافران (عموما).'\"},\n   {\"src\": \"RCH\", \"where\": \"Richardson, RCH.txt l.70938\", \"stance\": \"supports\", \"note\": \"'kunisht, A fire-temple. A Jews’ synagogue.' — the same double sense.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"کنشت (Persian)\", \"stance\": \"supports\", \"note\": \"'Borrowed from Aramaic כְּנִישְׁתָּא (kənīštā)'; 'doublet of کنیسه (kanise), which entered Persian through Arabic'.\"}])\n\nN(10, \"English\", \"Kneseth\", \"confirmed\",\n  \"The Israeli parliament, named in 1949 after the Knesset ha-Gedolah ('Great Assembly') of the Second \"\n  \"Temple period; from Mishnaic Hebrew keneset. The spelling 'Kneseth' with -th is not an error of the \"\n  \"chart: Klein p. 849, which Nourai cites, has the headword exactly as 'Kneseth'. The immediate parent \"\n  \"(Hebrew) is right; only the PIE ancestry at the top of the tree is wrong, the word being Semitic.\",\n  \"«کنست» نام پارلمان اسرائیل است که در ۱۹۴۹ م. از روی «کنست بزرگ» دوران معبد دوم برگزیده شد؛ از عبری مشنایی keneset. \"\n  \"ضبط Kneseth خطای کتاب نیست؛ همین صورت در کلاین ص ۸۴۹ آمده است (امروز Knesset معمول است). پیوند مستقیم با عبری درست است، \"\n  \"ولی نیای هندواروپایی در بالای نمودار نادرست است.\",\n  [W_KNESSET],\n  [{\"ref\": \"KLN:849\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 457 = printed p. 849: 'Kneseth, n., the Israeli Parliament. — Mishnaic Heb. keneseth, ‘gathering, assembly’ ... from the stem of Heb. kanas'. Nourai's spelling and gloss come straight from here.\"},\n   {\"ref\": \"AHD:724\", \"status\": \"not_checked\", \"note\": \"a page of the 1975 New College main dictionary (K section), not on disk; the Watkins IE-roots appendix that is on disk lists no KNESSET under kelə-², consistent with the word being Semitic.\"}],\n  [{\"src\": \"KLN\", \"where\": \"p. 849\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"כנסת\", \"stance\": \"supports\", \"note\": \"'הַכְּנֶסֶת (hak’néset) — the Knesset, the Israeli Parliament'; root כ־נ־ס.\"}])\n\nN(11, \"Latin\", \"classis\", \"confirmed\",\n  \"Latin classis, first 'the summons/levy' (classis iuniorum 'the call-up of the young men'), then 'one of \"\n  \"the six property classes of the Roman people' instituted by Servius Tullius, then 'army', then 'fleet', \"\n  \"and finally 'class, division' generally. Pokorny p. 548 derives it *klad-ti- (zero grade of *kelh₁- plus \"\n  \"the d-extension and -ti-), beside kelados; Watkins has 'Possibly extended zero-grade form *klə-, \"\n  \"becoming *klad- in suffixed form *klad-ti- in Latin classis'. The connection to calāre was already \"\n  \"Roman doctrine (Quintilian 1.6.33 'sit et classis a calando'). Caveat: Ernout–Meillet accept 'appel' as \"\n  \"the original sense but warn 'la dérivation ne s'explique pas' and suspect a technical Etruscan loan, so \"\n  \"the link is orthodox but not beyond dispute.\",\n  \"لاتین classis نخست به معنای «فراخواندن (به سلاح)» بود، سپس «طبقهٔ شهروندان»، آنگاه «سپاه، ناوگان». \"\n  \"پوکورنی (ص ۵۴۸) و واتکینز آن را *klad-ti- از همین ریشه می‌دانند و کوینتیلیانوس نیز آن را از calāre گرفته بود. \"\n  \"تنها ارنو‌مییه می‌گوید دگرگونی آوایی آن توجیه‌پذیر نیست و شاید وام‌واژه‌ای اتروریایی باشد؛ با این حال ادعای نورایی نظر معیار است.\",\n  [W_PIE, E_CLASS],\n  [{\"ref\": \"POK:548\", \"status\": \"supports\", \"note\": POK_Q + \"; specifically 'lat. classis ‚Aufgebot: Heer, Flotte; Klasse, Abteilung‘ (*klad-ti-: κέλαδος?)'.\"},\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt leaf 608, kelə-² IV: 'Possibly extended zero-grade form *klə-, becoming *klad- in suffixed form *klad-ti- in Latin classis, summons, division of citizens for military draft, hence army, fleet, also class in general: CLASS. [Pok. 6. kel- 548.]'\"}],\n  [{\"src\": \"POK\", \"where\": \"p. 548\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. classis (LAT.txt l.12264-12290)\", \"stance\": \"partial\", \"note\": \"'le sens premier est sans doute “appel”, classis iuniorum ... Les anciens rattachent classis à calāre, cf. Quint. 1,6,33, sit et classis a calando; mais la dérivation ne s'explique pas ... Terme technique qui peut être emprunté à l'étrusque.'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. class\", \"stance\": \"supports\", \"note\": \"'L. classis ... which prob. stands for *qlad-t-is, and is related to calare, ‘to call, proclaim’.'\"},\n   {\"src\": \"LEW\", \"where\": \"grep 'classis' in LEW_1910.txt\", \"stance\": \"silent\", \"note\": \"the headword is not recoverable in this OCR of Walde 1910.\"}])\n\nN(12, \"French\", \"classe\", \"confirmed\",\n  \"Old/Middle French classe (14th c.), a learned borrowing of Latin classis rather than an inherited form \"\n  \"(an inherited outcome would not have kept -cl- and -ss- intact). It is the immediate source of English \"\n  \"class and of the modern international word taken over by Persian.\",\n  \"فرانسوی classe (سدهٔ ۱۴ م.) وام‌واژه‌ای عالمانه از لاتین classis است نه صورت موروثی آن (وگرنه خوشهٔ cl- و -ss- دگرگون می‌شد). \"\n  \"همین صورت فرانسوی سرچشمهٔ class انگلیسی و «کلاس» فارسی است. ادعای نورایی درست است.\",\n  [E_CLASS],\n  [{\"ref\": \"AHD:248\", \"status\": \"not_checked\", \"note\": \"a page of the 1975 New College main dictionary (s.v. class), not on disk; the appendix entry cited at node 11 covers the same chain.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. class\", \"stance\": \"supports\", \"note\": \"'class, n. — F. classe, fr. L. classis.'\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/class\", \"stance\": \"supports\", \"note\": \"'from French classe (14c.), from Latin classis ‘a division; army, fleet’.'\"}])\n\nN(13, \"Persian\", \"kelâs\", \"confirmed\",\n  \"کلاس is a modern European loan taken into Persian through French classe in the 19th–20th century with \"\n  \"the vocabulary of the new schools (Dār al-Fonūn onwards): 'classroom', then 'year of study', then \"\n  \"'rank, class'. Mo‘in gives 'classe' as the source form and glosses 'طبقه، درجه، مرتبه ... هر یک از \"\n  \"اطاق‌های مدرسه که در آن معلمان به شاگردان درس دهند؛ اطاق درس', and adds a purist note that \"\n  \"the foreign word is better avoided. French -sse gives Persian -s and the stress-final ā of کلاس is the \"\n  \"regular treatment of French a in an open syllable.\",\n  \"«کلاس» وام‌واژه‌ای اروپایی است که از راه فرانسوی classe در دوران دارالفنون و مدرسهٔ نوین وارد فارسی شده است. \"\n  \"معین مأخذ آن را classe می‌گیرد و معنای «طبقه، درجه» و «اطاق درس» را می‌آورد. ادعای نورایی درست است.\",\n  [E_CLASS],\n  [{\"ref\": \"MON:3015\", \"status\": \"supports\", \"note\": \"Mo‘in کلاس (MON_part2.txt l.24541): 'کلاس: [classe] (ا.) طبقه، درجه، مرتبه ... هر یک از اطاق‌های مدرسه که در آن معلمان به شاگردان درس دهند؛ اطاق درس'; page number of the full Farhang not verifiable from the abridgement.\"}],\n  [{\"src\": \"MON\", \"where\": \"کلاس\", \"stance\": \"supports\", \"note\": \"as quoted; Mo‘in also warns 'احتراز از استعمال این کلمهٔ بیگانه اولی است'.\"},\n   {\"src\": \"ARY\", \"where\": \"grep کلاس in ARY_pages.txt / 'class' in ARY_latin_index_pages.txt\", \"stance\": \"silent\", \"note\": \"Aryanpur treats only inherited Indo-European vocabulary of Persian; the modern French loan is absent.\"}])\n\nN(14, \"English\", \"class\", \"confirmed\",\n  \"English class (c. 1600, first 'a group of students') from French classe, reinforced by direct use of \"\n  \"Latin classis; the modern senses 'order or rank of persons' (1660s), taxonomic 'class' (1753) and \"\n  \"social class (1763) are later English developments.\",\n  \"انگلیسی class (حدود ۱۶۰۰ م.، نخست به معنای «گروه دانشجویان») از فرانسوی classe و با تأثیر مستقیم لاتین classis. \"\n  \"معنای «طبقهٔ اجتماعی» از سدهٔ ۱۸ م. به بعد پیدا شده است. ادعای نورایی درست است.\",\n  [E_CLASS],\n  [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. class\", \"stance\": \"supports\", \"note\": \"'class, n. — F. classe, fr. L. classis.'\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/class\", \"stance\": \"supports\", \"note\": \"'c. 1600, “group of students”, from French classe (14c.), from Latin classis ... traced to calare “to call (to arms)”, PIE root *kele- “to shout”.'\"}])\n\nN(15, \"Latin\", \"concilium\", \"confirmed\",\n  \"Latin concilium 'a meeting, assembly' < *con-caliom, literally 'a calling together', from con- 'together' \"\n  \"+ calāre 'to call, proclaim' (the same verb behind kalendae); the -a- of *con-caliom was raised to -i- in \"\n  \"the medial open syllable, the regular Latin vowel weakening. Festus/Paulus already give the derivation \"\n  \"('concilium ... a concalando, i.e. uocando'). Watkins puts it under kelə-² III.1 'Suffixed form *kal-yo- \"\n  \"in Latin concilium'; Pokorny p. 549 lists it with a 'vielleicht'.\",\n  \"لاتین concilium «گردهمایی» از *con-caliom است، یعنی con- «با هم» + calāre «فراخواندن»؛ الف در هجای بازِ میانی به i بدل شده (قاعدهٔ تضعیف مصوت لاتین). \"\n  \"پائولوس-فستوس نیز می‌گوید concilium a concalando. واتکینز آن را ذیل kelə-² می‌آورد. ادعای نورایی درست است.\",\n  [W_PIE, E_COUNCIL],\n  [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt leaf 608, kelə-² III.1: 'Suffixed form *kal-yo- in Latin concilium, a meeting, gathering (< “a calling together”; con-, together; see kom): CONCILIATE, COUNCIL.'\"}],\n  [{\"src\": \"POK\", \"where\": \"p. 549 (POK_02.txt leaf 208)\", \"stance\": \"supports\", \"note\": \"'vielleicht concilium ‚Zusammenkunft, Versammlung, Vereinigung von Dingen‘ (*cōn-caliom), con-ciliāre ‚vereinigen, verbinden‘' — with a hedging 'vielleicht'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. concilium (LAT.txt l.13327)\", \"stance\": \"supports\", \"note\": \"'concilium, -ī n.: convocation, a concalando, i.e. uocando, P.F. 33,27; d'où “assemblée, réunion”.'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. council\", \"stance\": \"supports\", \"note\": \"'L. concilium ... which stands for *con-caliom, and prop. means ‘a calling together’, fr. con- and calāre.'\"}])\n\nN(16, \"French\", \"concilie\", \"transcription_suspect\",\n  \"There is no French noun 'concilie'. The word is concile (m.) 'council, synod', a learned borrowing of \"\n  \"Latin concilium; the Old French/Anglo-French form behind English council is concile / cuncile (Klein \"\n  \"s.v. council: 'OF. cuncile'; Etymonline: 'early 12c. Anglo-French cuncile, from Old French concile'). \"\n  \"The printed page (pdf p. 251, copied to data/verification/sources/refs/ocr/BOOK/251.png) really does \"\n  \"read 'concilie : assembly', so the extraction is faithful and the odd form is Nourai's own; it looks \"\n  \"like a contamination with the French verb concilier. Apart from the spelling the node is right: French \"\n  \"is the intermediary between Latin concilium and English council.\",\n  \"در فرانسوی واژه‌ای به صورت concilie وجود ندارد؛ صورت درست concile «شورا، مجمع کلیسایی» است و صورت فرانسوی کهن آن cuncile/concile. \"\n  \"بررسی تصویر صفحهٔ چاپی نشان می‌دهد خود کتاب همین «concilie» را چاپ کرده؛ پس خطای چاپی کتاب است نه خطای خوانش اسکن؛ \"\n  \"شاید آمیزش با فعل concilier رخ داده باشد. جز این ضبط، حلقهٔ فرانسوی درست است.\",\n  [E_COUNCIL],\n  [{\"ref\": \"AHD:303\", \"status\": \"not_checked\", \"note\": \"a page of the 1975 New College main dictionary (s.v. concilium/council), not on disk.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. council\", \"stance\": \"supports\", \"note\": \"'council, n. — OF. cuncile, fr. L. concilium' — the Old French form is concile/cuncile, never 'concilie'.\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/council\", \"stance\": \"supports\", \"note\": \"'early 12c. Anglo-French cuncile, from Old French concile, from Latin concilium.'\"}],\n  error_in=\"book\", book_prints=\"concilie\", correct_form=\"concile\")\n\nN(17, \"Persian\", \"konsŭl\", \"disputed\",\n  \"Persian کنسول / قونسول is the European consul — first the Roman magistrate, then the modern \"\n  \"diplomatic officer — borrowed through French consul in the Qajar period. Mo‘in defines it exactly so: \"\n  \"'در روم قدیم، عامل دولتی که از طرف مردم برای یکسال انتخاب می‌شد'. Latin cōnsul, however, does \"\n  \"not belong to *kelh₁- at all: it is a derivative of cōnsulere 'to deliberate, take counsel', for which \"\n  \"de Vaan and Watkins reconstruct *kom- + *selh₁- 'to take' (Watkins indexes CONSULT under yewes-, and \"\n  \"only COUNCIL under kelə-²). Nourai's chain French concile → Persian konsul therefore attaches the word \"\n  \"to the wrong Latin ancestor; the chart's second gloss 'council' also has no Persian counterpart (that \"\n  \"sense is شورا, not کنسول).\",\n  \"«کنسول / قونسول» در فارسی همان consul فرانسوی است که در دورهٔ قاجار وام گرفته شده و معین آن را «عامل دولتی روم قدیم» و سپس مأمور کنسولگری می‌داند. \"\n  \"اما لاتین cōnsul از cōnsulere «رای‌زدن» است (*kom- + *selh₁- «گرفتن») و هیچ پیوندی با concilium و ریشهٔ *kelh₁- ندارد؛ \"\n  \"واتکینز CONSULT را ذیل yewes- آورده است. معنای «council» نیز در فارسی برای این واژه نیست (معادل آن «شورا» است). پژوهش امروزی این حلقه را رد می‌کند.\",\n  [E_CONSUL],\n  [{\"ref\": \"MON:3097\", \"status\": \"partial\", \"note\": \"Mo‘in کنسول (MON_part2.txt l.27211): 'کنسول: [consul] [- قنسول] (ا.) در روم قدیم، عامل دولتی که از طرف مردم برای یکسال انتخاب می‌شد و با شخص دیگری ...' — the word and its French/Latin source, but nothing linking it to concilium.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. consul\", \"stance\": \"contradicts\", \"note\": \"'consul, n. — L. consul ... This word prob. meant orig. ‘convener, convoker’, and is rel. to consulere, ‘to take counsel, deliberate’.' Klein files it away from concilium/calāre.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins index (AHD_watkins1985.txt l.1707, l.1396)\", \"stance\": \"contradicts\", \"note\": \"'CONSULT yewes-' but 'COUNCIL kelə-2' — the appendix assigns consul-words to a different root.\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/consul\", \"stance\": \"contradicts\", \"note\": \"'from Latin consul ... probably “one who consults the Senate”, from consulere ... probably from com- + *selere “take, gather”.'\"}])\n\nN(18, \"English\", \"council, consul\", \"disputed\",\n  \"Two words with two different origins are put in one box. Council is right: ME/AF cuncile, OF concile, \"\n  \"from Latin concilium 'a calling together' — the whole chain of nodes 15–16 works for it (and English \"\n  \"council has been confused with counsel, from consilium, since the 16th c.). Consul is wrong: it is \"\n  \"Latin cōnsul, tied to cōnsulere and to the root *selh₁- 'to take', not to calāre/*kelh₁-; Watkins \"\n  \"indexes CONSULT under yewes-, Klein under consulere, Etymonline under com- + *selere. Because the \"\n  \"worse of the two verdicts governs the node, it is marked disputed.\",\n  \"در این خانه دو واژهٔ بی‌ربط کنار هم نشسته‌اند. council درست است: از فرانسوی کهن concile/cuncile و لاتین concilium. \"\n  \"ولی consul از لاتین cōnsul و فعل cōnsulere است و به ریشهٔ *selh₁- «گرفتن» می‌رسد نه به *kelh₁-. چون بدترین حکم ملاک است، این حلقه «ردشده» شمرده می‌شود.\",\n  [E_COUNCIL, E_CONSUL],\n  [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.vv. council, consul\", \"stance\": \"partial\", \"note\": \"council 'OF. cuncile, fr. L. concilium ... fr. con- and calāre' (supports); consul 'L. consul ... rel. to consulere' (contradicts the shared parentage).\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins index\", \"stance\": \"partial\", \"note\": \"'COUNCIL kelə-2' but 'CONSULT yewes-'.\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/council and /consul\", \"stance\": \"partial\", \"note\": \"council < concilium < con- + calare, PIE *kele- 'to shout'; consul < consulere, com- + *selere 'take, gather'.\"}])\n\nN(19, \"Latin\", \"clâmâre; kalendae; clârus\", \"confirmed\",\n  \"All three are standard members of the root. clāmāre 'to shout, call out' is the m-extension \"\n  \"*k(e)lə-m- (Watkins *klā-mā-); kalendae, the first day of the Roman month, is a *kal-ēnd- formation \"\n  \"from calāre, so named because the pontifex minor then proclaimed on which day the nones would fall \"\n  \"(the formula 'dies te quinque calo, Iuno Covella'); clārus 'loud-sounding' (clara uox) shifted to \"\n  \"'bright, clear' and then 'illustrious'. Pokorny p. 549 lists calō/-āre, calātor, calendae, clāmō, \"\n  \"clārus together; Ernout-Meillet: 'clarus ... Apparenté à clamo et calo, clarus a dû s'appliquer à la \"\n  \"voix et aux sons'.\",\n  \"هر سه واژه از همین ریشه‌اند: clāmāre «بانگ زدن» با گسترش -m-؛ kalendae «روز نخست ماه» از calāre، زیرا در آن روز کاهن تقویم ماه را جار می‌زد؛ \"\n  \"و clārus که نخست «پرآوا» بوده و سپس به «روشن» و «نامدار» تحول معنایی یافته است. پوکورنی و ارنو‌مییه هر سه را یکجا می‌آورند. ادعای نورایی درست است.\",\n  [W_PIE],\n  [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt kelə-²: 'Suffixed form *klā-mā- in Latin clamare: CLAIM, CLAMANT, CLAMOR ...'; III.2 '*kal-ēnd- in Latin kalendae ... CALENDAR, CALENDS'; III.4 '*kal-ā- in Latin calāre'; III.5 'in Latin clarus, bright, clear: CLEAR ... DECLARE'.\"}],\n  [{\"src\": \"POK\", \"where\": \"pp. 548-549\", \"stance\": \"supports\", \"note\": \"'lat. calō, -āre ‚Ausrufen, Zusammenrufen‘ ... calābr(a) ... calendae ‚der erste Tag des Monats‘ von diesem Ausrufen benannt ... clāmō, -āre ‚rufen‘ ... clārus ‚lauttonend, fernhin schallend; berühmt; klar‘.'\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. clarus (LAT.txt l.12243)\", \"stance\": \"supports\", \"note\": \"'clarus, -a, -um; clair. Apparenté à clamo et calo, clarus a dû s'appliquer à la voix et aux sons, clara uox.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 18.13/18.41 (SYN.txt l.31507)\", \"stance\": \"supports\", \"note\": \"'Lat. clamare : calare ‘call out, proclaim, summon’, Grk. καλέω ‘call, name’, κέλαδος ‘noise’, Lett. kal’uot ‘chatter’, Lith. kalba ‘language’.'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. claim, calendar, calends\", \"stance\": \"supports\", \"note\": \"'L. clamare ... which is rel. to clā-rus ... fr. I.-E. base *klā-, var. of *kal-, ‘to shout, resound’'; 'calendar — L. calendarium ... fr. calendae, kalendae'.\"}])\n\nN(20, \"English\", \"claim, calendar, clear, declare\", \"confirmed\",\n  \"All four come into English from French/Latin members of the same root: claim (13th c.) < OF claim-, \"\n  \"accented stem of clamer < clāmāre; declare < L. dēclārāre (dē- + clārus); clear < OF cler < clārus; \"\n  \"calendar < L. calendārium 'account book' (so called because debts fell due on the kalends) < kalendae. \"\n  \"Klein files claim, clamor, clear, class, calends and the second element of council under one base \"\n  \"*klā-/*kal- 'to shout, resound'.\",\n  \"هر چهار واژه از راه فرانسوی/لاتین به انگلیسی رسیده‌اند: claim از clamer فرانسوی کهن (< clāmāre)، declare از dēclārāre، \"\n  \"clear از cler فرانسوی کهن (< clārus) و calendar از calendārium «دفتر حساب» (< kalendae). کلاین همه را ذیل یک ریشه می‌آورد. \"\n  \"ادعای نورایی درست است.\",\n  [E_ECCL],\n  [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.vv. claim, calendar\", \"stance\": \"supports\", \"note\": \"'claim ... fr. OF. claim-, accented stem of clamer ... fr. L. clamare ... fr. I.-E. base *klā-, var. of *kal-, ‘to shout, resound’. See calends and cp. clear. Cp. also ... clarity, class and the second element in council, declaim, declamation ...'; 'calendar — L. calendarium, ‘an account book’, fr. calendae'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins kelə-²\", \"stance\": \"supports\", \"note\": \"CLAIM, CLAMOR, CALENDAR, CALENDS, CLEAR, DECLARE all listed under this root.\"}])\n\ndoc = {\n  \"pdf_page\": 251,\n  \"book_page\": 221,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Kel 3\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *kelh₁- 'to call out, shout' (Pokorny 6. kel-, k(e)lē-, k(e)lə- p. 548; Watkins kelə-² 'to shout')\",\n      \"note\": \"The root box is right: Pokorny p. 548 has '6. kel-, k(e)lē-, k(e)lə- oder kl-? ‚rufen, schreien, lärmen, klingen‘' and Watkins's appendix has kelə-² 'To shout' with the cross-reference [Pok. 6. kel- 548] — exactly Nourai's POK:548. The label 'Indo-European' and the gloss 'to shout, call' are both correct; the modern notation is *kelh₁-. The Indo-European half of this chart (nodes 1, 11-20) is sound. Its Semitic half is not: the arrow from Greek ekklēsía to Aramaic kᵉnūštā (node 4) joins a Greek deverbal to a Semitic triliteral root k-n-š/k-n-s, and Nourai's own cited authority for that node (al-‘Unaysi, TAD) says in as many words 'من کنوشتا الارامیة لا من ekklēsía الیونانیة'. Everything hanging below node 4 (Arabic k-n-s, kanīsa, Persian kans/kannās/kanīse, Hebrew kānas/keneset, Pahlavi kanašyā, Persian kanešt, English Knesset) is genuine Semitic material correctly related to one another, but wrongly attached to this Indo-European root. A separate slip is at the bottom right: Persian کنسول and English consul are not from concilium at all.\",\n      \"note_fa\": \"خانهٔ ریشه درست است: پوکورنی در ص ۵۴۸ ریشهٔ «6. kel-, k(e)lē-, k(e)lə- رفتن بانگ، فریاد، طنین» را آورده و واتکینز نیز ذیل kelə-² همین صفحه را ارجاع داده است؛ صورت امروزی آن *kelh₁- است. نیمهٔ هندواروپایی نمودار (یونانی، لاتین، فرانسوی، انگلیسی، کلیسا و کلاس) پذیرفتنی است. ولی نیمهٔ سامی آن نه: پیوندزدن ekklēsía یونانی به «کنوشتای» آرامی ریشه‌شناسی عامیانه است، زیرا واژهٔ آرامی از ریشهٔ سه‌حرفی سامی ک‌ن‌ش است و خود منبع مورد استناد نورایی (طوبیا العنیسی) می‌نویسد «من کنوشتا الارامیة لا من ekklēsía الیونانیة». همهٔ حلقه‌های زیر آن (کنس، کناس، کنیسه، کنشت، کنست) میان خود درست‌اند ولی به ریشهٔ نادرست بسته شده‌اند. لغزش دیگر در پایین نمودار است: «کنسول» و consul از concilium نیستند.\",\n      \"sources\": [W_PIE, E_ECCL],\n      \"ref_check\": [{\"ref\": \"POK:548\", \"status\": \"supports\", \"note\": POK_Q + \" — Nourai's page number is exact.\"}],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"Bd. I pp. 548-549 (POK_02.txt leaves 207-208)\", \"stance\": \"supports\", \"note\": POK_Q},\n        {\"src\": \"WLD\", \"where\": \"Bd. I p. 443 (WLD_Bd1_1930 djvu l.27922)\", \"stance\": \"supports\", \"note\": \"'kel- „rufen, schreien, lärmen, klingen“' with the same Sanskrit, Greek, Umbrian and Latin material — Pokorny's own earlier version of the entry (cited by Pokorny as WP. I 443 ff.).\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kelə-² (leaf 606-608)\", \"stance\": \"supports\", \"note\": \"'kelə-². To shout.' with CLAIM, CLAMOR, ECCLESIA, CONCILIATE, COUNCIL, CALENDAR, CLEAR, DECLARE, CLASS. '[Pok. 6. kel- 548.]'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 1949 p. 1250 ff. (SYN.txt l.31507, 31619)\", \"stance\": \"supports\", \"note\": \"'Lat. clamare : calare ‘call out, proclaim, summon’, Grk. καλέω ‘call, name’ ... Lith. kalba ‘language’. Walde-P. 1.443 f.'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann s.v. kal- (3) (IEC.txt l.6665)\", \"stance\": \"supports\", \"note\": \"'kal- (3) (kalaio, kaleio) “call, name, summon, invite, accuse”. Skt. usa-kalah ‘cockerel’; Hitt. kalles- ‘invite’; Gk. kaléo; OLat. calō, are ‘call’, cf. concilium ‘council’; W ceiliog ‘cockerel’; OHG halon ‘call, invite’; Li. kal-bà ‘speech’.'\"}\n      ],\n      \"nodes\": nodes\n    }\n  ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-251.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('ok', len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk251.py"
}
```


### [2026-09-06T16:23:48.154Z] TOOL RESULT

```
ok 20
```


## [2026-09-06T16:23:52.989Z] TOOL CALL #73: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-251.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 251"
}
```


### [2026-09-06T16:23:54.768Z] TOOL RESULT

```
JSON OK
nodes verified: 20/20
node verdicts: {'confirmed': 12, 'plausible': 4, 'disputed': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 12, 'not_checked': 8, 'partial': 4, 'contradicts': 1}
books consulted: {'supports': 37, 'silent': 10, 'partial': 6, 'contradicts': 5} | by book: {'KLN': 12, 'Wiktionary': 6, 'BQT': 5, 'Etymonline': 5, 'POK': 4, 'AHD': 4, 'MON': 4, 'LAT': 3, 'PHD': 2, 'NYB': 2, 'HRN': 2, 'TAD': 2, 'ARY': 2, 'WLD': 1, 'AFA': 1, 'RCH': 1, 'LEW': 1, 'SYN': 1}
```


## [2026-09-06T16:24:15.317Z] AGENT

Page 251 (book p. 221), single entry — root **Kel 3** "to shout, call", 20 nodes. `verify_check.py 251` reports 20/20 nodes, 0 PROBLEM lines.

**Verdicts:** root confirmed · nodes 12 confirmed, 4 plausible, 3 disputed, 1 transcription_suspect.

**Disputed**
- **#4 Aramaic kenušta / K.n.s, K.n.š** — drawn from Greek *ekklēsía*. It is the Semitic triliteral k-n-š/k-n-s. Nourai's own cited source refutes him: TAD (al-ʿUnaysi) leaf 68 ≈ p. 63–65 reads «کنیسة من «کنوشتا» الارامیة **لا من** ἐκκλησία الیونانیة». Everything below it (nodes 5–10) is genuine Semitic material hung on the wrong root.
- **#17 Persian konsŭl (کنسول، قونسول)** — from French *consul* < Lat. *cōnsul* < *cōnsulere* (*kom- + *selh₁-), not from *concilium*; Watkins indexes CONSULT under **yewes-**, only COUNCIL under kelə-². Chart's gloss "council" has no Persian counterpart (شورا).
- **#18 English "council, consul"** — two unrelated words in one box; *council* is correct, *consul* is not.

**transcription_suspect**
- **#16 French "concilie"** — no such French noun; the word is *concile* (OF *concile/cuncile*, Klein s.v. council). `error_in: book` — the printed page really prints "concilie"; extraction is faithful. Page image copied to `data/verification/sources/refs/ocr/BOOK/251.png`.

**Plausible:** #2 Pahlavi *kilîsyâk* (real — Moʿin's BQT p. 1688 fn. 5 gives it verbatim after Sanjana — but the route ran through Syriac, and MacKenzie/Nyberg have no entry); #5 Arabic *kanīsa* (native root, Aramaic **semantic** loan only); #7 Hebrew *kānas/keneseth* (Klein: cognate with Aram. kᵉnash, not descended from it); #8 Pahlavi *kanašya* (attested via Blochet in BQT p. 1709 fn. 6, but its parent is Aramaic, not Hebrew).

**No extraction errors** — the JSON matches the printed page throughout (Persian scripts, poet attributions, refs all check out).

Notable positive finds: BQT p. 1688 fn. 5 and p. 1709 fn. 6 are literally Nourai's sources for nodes 2/3 and 8/9, down to the transliterations `kilîsyâk` and `kanashyâ`; both footnotes read by vision and saved to `data/verification/sources/refs/ocr/BQT/{1688,1709}.vision.txt`. SAP:1448 was the only wholly inaccessible reference (Sayyāh is purchase-only); the four `AHD:nnn` refs point at 1975 New College main-dictionary pages that aren't on disk, though the Watkins appendix covers the same claims.

Files: `/home/sfmqrb/git/rishe/data/verification/page-251.json`; 10 web sources archived via `fetch_source.py`.
