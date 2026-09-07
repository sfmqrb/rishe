# Verification process log — verify-page-312


## [2026-09-07T01:36:55.413Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 312 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-312.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-312.json. Write /home/sfmqrb/git/rishe/data/verification/page-312.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 312` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T01:36:57.578Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-07T01:36:58.360Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T01:36:58.383Z] TOOL RESULT

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


## [2026-09-07T01:36:58.975Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-312.txt"
}
```


### [2026-09-07T01:36:59.040Z] TOOL RESULT

```
1	=== PDF page 312 (book page 282) ===
2	--- entry 0 ---
3	ROOT leudheros -> redirect to Leudh
4	--- entry 1 ---
5	ROOT leudho -> redirect to Leudh
6	--- entry 2 ---
7	ROOT [Indo-European] Leuk, Leuqos : light, brightness  (refs POK:687; KNT:205)
8	#1 (parent #0) [Avestan] refs=HRN:23,136,140; SYN:470,991; BQT:31 | raočah : light ; raoč-xšaema, raoxšna : bright light ☞Ksei 2 ; a-raxša : bright ; aiwi-raocya : light up ☞Ambhi
9	  #2 (parent #1) [Persian] refs=BQT:97,147,976; FSF:176 | rŭz «روز ( روزنه ، فروزان ، فروغ )» : day ; rošan «روشن» : bright ; raxš «رخش ( درخش ، درفش ۱ )» : bright(ness), white ; Ââraš «آرش» : "bright", a male name ; afrŭxtan «افروختن» : to kindle
10	    #3 (parent #2) [Arabic] refs=AFM:72; PLA:135 | rezq : daily food | NOTE: Derived from Persian "rŭz".
11	      #4 (parent #3) [Persian] refs=MON | rezq «رزق» : daily bread | extra: ارزاق ، رزّاق ، رازق
12	#5 (parent #0) [Sogdian] refs=SOD:146,345 | dwk` : world ; rwxšn : bright, light
13	#6 (parent #0) [Old Persian] refs=KNT:205 | raucah : day
14	#7 (parent #0) [Latin] refs=AHD | lŭstrâre : to make bright, purify
15	  #8 (parent #7) [French] refs=None | 
16	    #9 (parent #8) [Persian] refs=MON:3650 | lŭstr «لوستر» : chandelier
17	    #10 (parent #8) [English] refs=AHD:776 | luster, illustrate
18	#11 (parent #0) [Latin] refs=AHD | lumen, lŭx : light ; luna : moon
19	  #12 (parent #11) [English] refs=None | illuminate, lunar
20	#13 (parent #0) [Germanic] refs=AHD | liuhtam
21	  #14 (parent #13) [English] refs=AHD | light 1, lightning, lighting
22	
```


## [2026-09-07T01:37:02.727Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-312.json",
 "description": "Read source JSON for page 312"
}
```


### [2026-09-07T01:37:02.766Z] TOOL RESULT

```
{
  "pdf_page": 312,
  "book_page": 282,
  "entries": [
    {
      "root": {"name": "leudheros", "redirect": "Leudh"},
      "nodes": []
    },
    {
      "root": {"name": "leudho", "redirect": "Leudh"},
      "nodes": []
    },
    {
      "root": {
        "name": "Leuk, Leuqos",
        "lang": "Indo-European",
        "refs": "POK:687; KNT:205",
        "gloss": "light, brightness"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HRN:23,136,140; SYN:470,991; BQT:31",
          "words": [
            {"translit": "raočah", "gloss": "light", "script": null},
            {"translit": "raoč-xšaema, raoxšna", "gloss": "bright light", "script": null, "see": ["Ksei 2"]},
            {"translit": "a-raxša", "gloss": "bright", "script": null},
            {"translit": "aiwi-raocya", "gloss": "light up", "script": null, "see": ["Ambhi"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:97,147,976; FSF:176",
          "words": [
            {"translit": "rŭz", "gloss": "day", "script": "روز ( روزنه ، فروزان ، فروغ )"},
            {"translit": "rošan", "gloss": "bright", "script": "روشن"},
            {"translit": "raxš", "gloss": "bright(ness), white", "script": "رخش ( درخش ، درفش ۱ )"},
            {"translit": "Ââraš", "gloss": "\"bright\", a male name", "script": "آرش"},
            {"translit": "afrŭxtan", "gloss": "to kindle", "script": "افروختن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "جهان شد ز گَرد سواران بنفش - درخشان سنان و درفشان ۱ درفش", "poet": "Ferdowsî"}
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "AFM:72; PLA:135",
          "words": [
            {"translit": "rezq", "gloss": "daily food", "script": null}
          ],
          "script_extra": null,
          "note": "Derived from Persian \"rŭz\".",
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "rezq", "gloss": "daily bread", "script": "رزق"}
          ],
          "script_extra": "ارزاق ، رزّاق ، رازق",
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:146,345",
          "words": [
            {"translit": "dwk`", "gloss": "world", "script": null},
            {"translit": "rwxšn", "gloss": "bright, light", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:205",
          "words": [
            {"translit": "raucah", "gloss": "day", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "lŭstrâre", "gloss": "to make bright, purify", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON:3650",
          "words": [
            {"translit": "lŭstr", "gloss": "chandelier", "script": "لوستر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
          "lang": "English",
          "refs": "AHD:776",
          "words": [
            {"translit": "luster, illustrate", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "lumen, lŭx", "gloss": "light", "script": null},
            {"translit": "luna", "gloss": "moon", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "illuminate, lunar", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "liuhtam", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "light 1, lightning, lighting", "gloss": null, "script": null}
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


## [2026-09-07T01:37:04.182Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','HRN','SYN','BQT','FSF','AFM','PLA','MON','SOD','AHD','KLN','WLD','IEC','PHD','NYB','HUB','ARY','FVQ','SKT']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-07T01:37:05.361Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushi
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
```


## [2026-09-07T01:37:39.427Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-07T01:37:39.485Z] TOOL RESULT

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
```


## [2026-09-07T01:37:39.902Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -80 && echo ---- && ls data/verification/ | tail -20"
}
```


### [2026-09-07T01:37:39.956Z] TOOL RESULT

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
----
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
```


## [2026-09-07T01:37:43.520Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 1,120p tools/verify_check.py"
}
```


### [2026-09-07T01:37:43.569Z] TOOL RESULT

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


## [2026-09-07T01:37:52.736Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK grep leuk ===\"\ngrep -n \"leuk-\" POK_full.txt | head -40\necho \"=== POK page 687 area (search 687) ===\"\ngrep -n \"^687\\|687$\" POK_full.txt | head"
}
```


## [2026-09-07T01:37:53.014Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD leuk ===\"\ngrep -n -i \"leuk\" AHD_watkins1985.txt | head -30\necho \"=== KNT raucah ===\"\ngrep -n -i \"raucah\\|rauca\" KNT.txt | head -20"
}
```


### [2026-09-07T01:37:54.101Z] TOOL RESULT

```
=== POK grep leuk ===
56040:Latin /J/r7e/7 "light' from * leuk-s-men; /una 'moon goddess ') {*lohuksna), praen. Losna{: 
68259:Root / lemma: pleuk- 
69225:Root / lemma: pi-lo- : hair' : Root / lemma: pu-lo- : hair' derived from Root / lemma: pleuk- 
78072:Root / lemma: (s)leug-, (s)leuk- 
78080:den Schlucken', fAuyyjw), Auyyavoijai Hes. "schluchze"; *(s)leuk-\x\ AuyKoivu) ds., 
78107:Old Low German 5/J/r "squamas'; besides Germanic sluh-, slug- (Indo Germanic *sleuk-) in 
=== POK page 687 area (search 687) ===
```


### [2026-09-07T01:37:54.186Z] TOOL RESULT

```
=== AHD leuk ===
402:French doux), sweet: DOLCE, DOUCEUR, DULCET; BIL- LET-DOUX, DULCIFY. 2. Basic form *dlku- (with *dl- dissimilated to *gl- in Greek because of the following k) in: a. Greek glukus, sweet: LICORICE; b. Greek glukeros (with suffix *-ero-), sweet: GLYCERIN; Cc. Greek gleukos (with suffix -es-), must, sweet wine: GLUCOSE. [Pok. dlki- 222.)
697:leug-2. To break. Suffixed form *Jeug-é- in Latin ligére, to mourn (? < “to break down mentally”): LUGUBRIOUS. [Pok. leug- 686.] leugh-. To tell a lie. 1. Germanic *leugan in: a. Old English /Zogan, to lie: WARLOCK; b. Old English beléog- an, to tell lies about (be-, about; see ambhi): BELIE. 2. Germanic */ugiz in Old English lyge, a lie, falsehood: LIE’. [Pok. leugh- 686.] leuk-. Light, brightness. I. Basic form */euk-. 1. Suffixed form *leuk-to- in Germanic */euhtam in Old English léoht, liht, light: LicHT). 2. Latin lix, light: Lucrna, LUCULENT, LUX; LUCIFER, LUCIFERIN. 3. Suffixed form *leuk-smen- in Latin limen, light, opening: LIMN, LU- MEN, LUMINARY, LUMINOUS; ILLUMINATE, PHILLUMEN- 1st. 4. Suffixed form *leuk-snd- in Latin lina, moon: LUNA, LUNAR, LUNATE, LUNATIC, LUNE, LUNULA; DEMI- LUNE, SUBLUNARY. 5. Suffixed form */euk-stro- in: a. Latin listrum, purification: LUSTER, (LUSTRUM); b. Latin lastrdre, to purify, illuminate: ILLUSTRATE. 6. Suffixed form *leuko-dhro- in Latin licubrdre, to work by lamplight: LUCUBRATE. II. O-grade form *louk-. 1. Suffixed form *louk-o- in Germanic *lauhaz in Old English /éah, meadow (< “place where light shines”): LEA. 2. Suffixed (iterative) form *lowk-eyo- in Latin liicére, to shine (> licidus, shining): LUCENT, LUCID; ELUCIDATE, NOCTILUCA, PELLUCID, RELUCENT, TRANS- LUCENT. III. Zero-grade form *luk-. 1. Suffixed form *luk-sno- in Greek lukhnos, lamp: LINK?, LYCHNIS. 2. At- tributed by some to this root (but more likely of obscure origin) is Greek lunx, lynx (as if from its shining eyes): LYNX, OUNCE? [Pok. leuk- 687.] leup-. To peel off, break off. 1. Germanic *laubaz in Old English Jéaf, leaf: LEAF. 2. Germanic *laubja, “roof made from bark,” shelter, in: a. Old French loge, lodge: LODGE, (LOGE); b. Medieval Latin lobium, lobia, laubia, monas- tic cloister: LOBBY. 3. Attributed by some to this root is Germanic */uftuz, sky (traditionally explained as < “roof of the world,” vault of heaven), but probably a separate Germanic root, in: a. Old Norse opt, air, attic, sky: LOFT; ALOFT; b. Germanic */uftjan, to hold up in the air, in Old Norse /ypta, to lift: Lirt. [Pok. leup- 690.]
862:flad6, flat cake, pancake: FLAN. 4. Germanic nasalized suffixed form *flu-n-th-r-j6- in Old Swedish flundra, flatfish, flounder, probably akin to the Scandinavian source of Middle English flounder, flounder: FLOUNDER?. 5. Nasalized form *pla-n-t- in Latin planta, sole of the foot, and denominative plantdre, to drive in with the sole of the foot, plant, whence planta, a plant: CLAN, PLAN, PLANT, PLANTAIN!, PLANTAR; PLANTIGRADE, SUPPLANT. 6. Suffixed form “plat-u- in Greek platus (feminine plateia), flat, broad: PIAZZA, PLACE, PLAICE, PLANE‘, (PLANE TREE), PLATE, (PLATEAU), (PLATITUDE), (PLATY?), PLATY-, (PLAZA). [Pok. plat- 833.] [plegan. To pledge for, stake, risk, exercise oneself. West Germanic verb. 1. Old English plegian, to exercise one- self, play: PLAY. 2. Late Latin plevium (> Old French plevir, to pledge), pledge, guarantee: PLEDGE; REPLEVIN. 3. Germanic derivative noun *plehti- in Old English pliht, danger, peril: PLIGHT?.] plek-. To plait. Extension of pel-*. 1. Suffixed o-grade form *plok-so- in Germanic *flahsam, flax, in Old Eng- lish fleax, flax: FLAX. 2. Full-grade form *plek- in Latin -plex, -fold (in compounds such as duplex, twofold; and supplex, “with legs folded under one,” kneeling, entreat- ing; see dwo-, upo): MULTIPLEX, QUINTUPLE, SUPPLE. 3. Latin plicdre, to fold (also in compounds used as denominatives of words in -plex, genitive -plicis): PLAIT, PLIANT, PLICA, PLICATE, PLIGHT!, PLISSE, PLY!; APPLY, COMPLICATE, COMPLICE, DEPLOY, DISPLAY, EMPLOY, EXPLICATE, IMPLICATE, REPLICATE, SUPPLICATE. 4. Suf- fixed forms “plek-to- and *plek-t-to- in Latin plectere (past participle plexus), to weave, plait, entwine: PLEACH, PLEXUS; AMPLEXICAUL, COMPLECT, (COMPLEX), PERPLEX. 5. Greek plekein, to plait, twine, and plektos, twisted: PLECOPTERAN, PLECTOGNATH. [Pok. plek- 834.] plék-. Also pleik-. To tear. 1. Zero-grade form *pbk- becoming *plak- in Germanic *flahan in Old English fléan, to strip the skin from: FLAY. 2. Suffixed o-grade form “ploik-sk- perhaps in Germanic “flaiskjan, piece of flesh torn off, in Old English flésc, flesh: FLESH. 3. Zero-grade form *plik- in Germanic *flikkja in: a. Old English flicce, side of a hog: FLITCH; b. Germanic ablaut form *flekkja in Old Norse flekkr, piece of skin or flesh, spot, stain: FLECK. [Pok. plék- 835.] pleu-. To flow. I. Basic form “pleu-. 1. Latin pluere, to rain: (PLOVER), (PLUVIAL), PLUVIOUS. 2. Greek pleusis, sailing: PLEUSTON. 3. Suffixed zero-grade form *plu-elos dissimilated into Greek puelos, trough, basin: PYELITIS. 4. Suffixed form *pl/(e)u-mon-, ‘‘floater,” lung(s), in: a. Latin pulmé (< *plumonés), lung(s): PULMONARY; b. Greek pleumén, pneumon, lung: PNEUMONIA, PNEU- MONIC. 5. Suffixed o-grade form *plou-to- in Greek plou- tos, wealth, riches (< ‘‘overflowing’’): PLUTO; PLUTOCRACY. 6. Lengthened o-grade form *pl6(u)- in: a. Germanic *fléwan, to flow, in (i) Old English flowan, to flow: FLOW (ii) perhaps Middle Dutch vluwe, fishnet: FLUE?; b. suffixed form *pld-tu- in Germanic *fléduz, flowing water, deluge, in Old English fléd, flood: FLOOD. II. Extended form *pleuk-. 1. Germanic *fleugan, to fly, in Old English fléogan, to fly: FLY!. 2. Germanic *fleu- gon-, flying insect, fly, in Old English fléoge, a fly: FLY?. 3. Probably Germanic *fleuhan, to run away, in Old English fléon, to flee: FLEE. 4. Germanic causative *flauhjan in Old English flygan, flégan, to put to flight: FLEY. 5. Germanic suffixed form *fleug-ika in Old French fleche, arrow: FLECHE, FLETCHER. 6. Zero-grade form *pluk- in: a. Germanic *flugja-, feather, in Old English -flycge, with feathers (only in unfligge, featherless): FLEDGE; b. suffixed form *flug-ti- in Old English flyht, act of flying, and *flyht, act of fleeing, escape: FLIGHT, FLIGHT?; Cc. possibly (but unlikely) suffixed form *flug- laz, dissimilated into *fuglaz, bird, in Old English fugol, bird: FowL; d. Germanic suffixed form *flug-ila in Mid- dle High German viiigel (> Germanic Fliigel), wing: FLUGELHORN, FUGLEMAN. III. Extended form *pleud-.
1419:DEMENT men-1 DEMETER mater- DEMILUNE leuk- DEMIT (s)meit(a)- DEMIURGE da-, werg- DEMOCRACY da- DEMOLISH mé6- DEMON da- DEMONSTRATE men-! DEMOPHOBIA da- DEMOS da- DEMOTIC da- DEMUR mere- DEN dan- DENARIUS dekm DENARY dekm DENDRO- deru DENDRON deru DENIER? dekm DENIGRATE negW-ro- DENOMINATE no-men- DENOUEMENT ned- DENOUNCE neu-! DENSE dens-2 DENTAL dent- DENTATE dent- DENTI- dent- DENTICLE dent- DENTIFRICE bhréi- DENUDE nogw- DENY ne
1454:ELUANT leu(@)- ELUCIDATE leuk- ELUDE leid- ELUTE leu(a)- ELUVIUM leu(a)- ELYTRON wel-3 EMACIATE mak- EMANATE ma-3 EMANCIPATE man-2 EMASCULATE mas EMBASSAGE ag- EMBASSY ag- EMBELLISH deu-2 EMBER eUS- EMBER DAY ambhi, rei-3 EMBLEM gWele-1 EMBLEMENTS bhel-3 EMBOUCHURE beu-! EMBRACE mregh-u- EMBROCATE mergh- EMEND mend- EMERGE mezg-! EMERITUS (s)mer-2 EMESIS weme- EMETIC weme- EMIGRATE mei-! EMINENT men-2 EMIT (s)meit(9)- EMMET mai-1 EMOLLIENT mel-1 EMOTION meue- EMPEROR pere-! EMPHASIS bha-' EMPHYSEMA pu-! EMPIRIC per-4 EMPLOY plek- EMPORIUM per-2 EMPRISE ghend- EMPTY med- EMPYEMA pu-2 EMPYREAL pil- EMULSION melg- EMUNCTORY meug-2 EN-! en
1673:ILLATION tele- ILLITERATE deph- ILLUMINATE leuk- ILLUSION leid- ILLUSTRATE leuk- IMBECILE bak- IMBIBE p6(i)- IMBRICATE ombh-ro- IMBRUE_bhreu-2 IMBUE ombh-ro- IMMACULATE macula IMMANENT men-3 IMMATURE ma-1 IMMENSE mé6-2 IMMERSE mezg-! IMMINENT men-2 IMMIX meik- IMMODERATE med- IMMODEST med- IMMOLATE mele- IMMORTAL mer-2 IMMUNE mei-1 IMMURE mei-3 IMP bheue- IMPAIR ped-1 IMPALE pag- IMPARITY pere-2 IMPART pere-2 IMPEACH ped-1 IMPECCABLE ped-1 IMPECUNIOUS peku- IMPEDE ped-! IMPEL pel-6 IMPEND (s)pen- IMPERATIVE pere-1 IMPERIAL pere-1 IMPETRATE peter- IMPETUS _pet- IMPINGE pag- IMPIOUS pius IMPLEMENT pele-1 IMPLICATE plek- IMPONE apo- IMPORT per-2 IMPORTANT per-2 IMPORTUNE per-2 IMPOSE apo- IMPOTENT poti- IMPOUND bend- IMPRECATE prek- IMPRESS! per-5 IMPRIMIS_ per! IMPRINT per-5 IMPROBITY pert IMPROMPTU em- IMPROVE es-, pert IMPUDENT (s)peud- IMPUGN peuk- IMPUNITY kweij-1 IMPUTE peu- IN-l ne
1748:LIFT leup- LIGASE leig-1 LIGATE leig-1 LIGHT! = leuk- LIGHT2 legwh-
1750:LIGHTER? legwh- LIGNEOUS  leg-! LIGNI- leg-1 LIGNUM VITAE gWei- LIGULE dngha LIKE! [ik- LIKE? [ik- LIKELY lik- LILAC nei- LIMACINE  lei- LIME = lei- LIMICOLINE lei- LIMN leuk- LIMP kel-1, leb-1 LINDEN _ lento- LINE! lino- LINE? fino- LINEN fino- Linc! del-1 LING? lenk- LINGER del-1 LINGERIE lino- LINGO dnghi LINGUA dnghd LINGUIST dngha LINIMENT lei- LININ lino- LINK! kleng- LINK? Jeuk- LINKS kleng- LINNET fino- _ LINOLEIC ACID [ino- LINSEED lino- LINT Tino-
1769:Lox! =laks- LOXODROMIC  der-1 LOYAL leg-1 LUBRICATE sleubh- LUBRICIOUS sleubh- LUBRICITY sleubh- LUCARNE leug-1 LUCENT leuk- LUCID leuk- LuciFER leuk- LUCIFERIN leuk- Lucina leuk- LUCRATIVE lau- LUCRE aus LUCUBRATE leuk- LUCULENT leuk- LUDICROUS leid-
1771:LUMBAGO_lendh-! LUMBAR lendh-1 LUMBER? lem-1 LUMBRICOID sleng¥h- LUMEN leuk- LUMINARY leuk- LUMINOUS leuk- LUMP! leb-1 LUMPEN leb-1 LUMPFISH leb-1 Luna _leuk- LUNAR leuk- LUNATE leuk- LUNATIC leuk-
1772:LUNE leuk- LUNG leg¥h- LUNGE del-1
1773:LUNULA leuk-
1777:LUSTER leuk- LUSTRUM_leuk-
1779:Lux leuk-
1782:LYASE leu-1 LYCANTHROPE ner-2, wlkwo- LYCHNIS leuk- LYCOPODIUM ped-!, wikwo- LYE leu(9)- LYMPHADENITIS eng¥- LYNX leuk-
1929:NOBLE gno- NOCENT nek-! Nock ken-5 NOCTI- nekw-t- NOCTILUCA leuk- NOCTUID nekw-t- NOCTULE nekw-t- NOCTURN nekw-t- NOCTURNAL nekw-t- Nocuous_nek-! NOD ken-2
2004:OTTER wed-1 OUBLIETTE lei- oucH2 ned: OUGHT! 6 OUNCE! oi-no- OUNCE? leuk-
2071:PEG bak- PEGMATITE pag- PEJORATION ped-1 PELAGE pilo- PELAGIC plak-1 PELARGONIUM pel-2 PELECYPOD ped-1 PELISSE pel-4 PELLAGRA ag-, pel-4 PELLICLE pel-4 PELL-MELL meik- PELLUCID leuk- PELOPS okw-, pel-2 PELORIA kwer-1 PELT! pel-4 PELTATE pel-4 PELTRY pel-4 PELVIS pel-7 PEN! pet-
2084:-PHAGE bhag-1 -PHAGIA bhag-! PHAGO- bhag-1 -PHAGOUS  bhag-! PHALANGE bhelg- PHALANX bhelg- PHALAROPE bhel-1, ped-1 PHALLUS bhel-2 PHANEROGAM bha-! PHANTASM_ bha-! PHANTASMAGORIA bha-1 PHANTOM bha-1 PHARMACOPOEIA kWei-2 PHARYNX bher-2 PHASE bha-1 -PHASIA bha-2 PHELLEM bhel-2 PHELLODERM bhel-2 PHELLOGEN _bhel-2 PHENO- bha-1 PHENOMENON bha-1 PHEROMONE bher-1 PHILANDER ner-2 PHILANTHROPY ner-2 PHILATELY tela- -PHILE bhilo- -PHILIA bhilo- PHILLUMENIST leuk- PHILO- bhilo- PHILODENDRON deru -PHILOUS _bhilo- PHILTER bhilo- PHLEGETHON bhel-1 PHLEGM bhel-1 PHLEGMATIC bhel-1 PHLOEM bhlieu- PHLOGISTON bhel-1 PHLOGOPITE bhel-1, okw- PHLOX bhel-1 PHLYCTENA bhlieu- -PHOBE bheg¥- -PHOBIA bhegw- PHOEBE bheigw- PHOEBUS bheigw- PHONE! bha-2 -PHONE bha-2 PHONEME bha-2 PHONETIC bha-2 PHONO- bha-2 -PHONY bha-2 -PHORE bher-1 -PHORESIS bher-1 -PHOROUS bher-1 PHOS- bha-1 PHOSPHENE bha-1 PHOSPHORUS bha-1 PHOT bha-1
2178:REIGN reg-! REIMBURSE bursa REINDEER dheu-1, ker-1 REINFORCE bhergh-2 REITERATE i- REJECT yé- REJOICE gau- REJUVENATE yeu- RELAPSE leb-! RELATE tele- RELAX slég- RELAY slég- RELEGATE leg-1 RELENT lento- RELIEVE leg¥h- RELINQUISH leikw- RELUCENT leuk- RELUCT leug-! RELY leig-1 REMAIN men-3 REMAND man-2 REMARK merg- REMEDY med- REMEMBER (s)mer-! REMEX ere-! REMINISCENT men-! REMIT (s)meit(a)- REMORA mere- REMORSE mer-2 REMOTE meue- REMOVE meue- REMUDA mei-1 REMUNERATE mei-! RENAISSANCE gene- REND rendh- RENDER do- _ RENDEZVOUS wOS RENEGADE ne RENEGE ne RENITENT kneigh- RENOUNCE neu-! RENOVATE newo- RENOWN no-men- RENT! do- REPAIR! pere-1 REPAND pete- REPARTEE pere-2 REPAST pa- REPEAT pet- REPEL pel-6 REPENT2 rép-1 REPERTORY pere-! REPINE kWei-1 REPLENISH pele-! REPLETE pele-1 REPLEVIN plegan REPLICATE plek- REPORT per-2 REPOSE! paus- REPOSIT apo- REPREHEND ghend- REPRESENT e@S- REPRESS per-5 REPRIMAND per-5 REPRISAL ghend- REPRISE ghend- REPROACH pert REPROVE per? REPTILE rép-1 REPUBLIC ré- REPUDIATE (s)peud- REPUGN peuk- REPUTE peu-
2323:sTuD2 sta- STUDENT (s)teu- sTUDY (s)teu- STULTIFY _ stel- sTUM stam- STUMBLE stam- STUMP stebh- STUN (s)tena- STUPA steu(@)- STUPE steu(9)- STUPEFY (s)teu- STUPENDOUS (s)teu- STUPID (s)teu- STURDY trozdo- STUTTER (s)teu- stTy2  steigh- STYLITE sta- STYLOBATE gWa-, sta- STYPTIC steu(@)- Styx (s)teu- SUASION swad- SUAVE swad- SUB- upo SUBALTERN al-1 SUBAUDITION au-5 SUBDUCTION deuk- SUBDUE deuk- SUBITO ei-! SUBJACENT yé- SUBJECT yé- SUBJOIN yeug- SUBJUGATE yeug- SUBLUNARY leuk- SUBMERGE mezg-! SUBMIT (s)meit(9)- SUBORDINATE ar- SUBORN ar- SUBPOENA kwei-1 SUBREPTION rép-1 SUBROGATE reg-1 SUBSCRIBE skribh- SUBSEQUENT sekw-1 SUBSIDE sed-1 SUBSIDY sed-1 sUBSIST sta- SUBSTANCE sta- SUBSTITUTE sta- SUBSTRATUM ster-2 SUBSTRUCTION | ster-2 SUBSUME em- SUBTEND ten- SUBTERFUGE bheug-', upo SUBTERRANEAN ters- SUBTLE teks- SUBTRACT tragh- SUBULATE syU- SUBVENTION gWa- SUBVERT wer-3 SUCCEED ked- succincT kenk-1 succor kers-2 succuBUS keu-2 SUCCULENT seud-2 SUCCUMB keu-2 SUCCUSSION kwét- SUCH swo-
2402:TRANSIENT ei-1, tera-2 TRANSIT ei-1 TRANSITIVE ei-1 TRANSLATE tele- TRANSLITERATE deph- TRANSLUCENT leuk- TRANSMIT (s)meit(@)- TRANSMUTE mei-1 TRANSOM tere-2 TRANSPIRE § spirare TRANSPONTINE pent- TRANSPORT per-2 TRANSUDE sweid-2 TRANSVERSE wer-3 TRAP! der-1
=== KNT raucah ===
1253:pli *leug- ‘shine’ in OP rauca ‘day’, Skt. rócas- ‘light’, Gk. Локо ‘white’,
1259:Where pAr. k stood before varying vowels, there may be variation in the products (as in the forms from root kar-), or one value may be generalized: OP rauca from nom.-acc. pIE *leugos, with c from oblique cases, where pIE had *leuges- (cf. Gk. yévos y&veos, Lt. genus generis).
1347:sárva-, Gk. Ion. oos, Att. ddos. pIE *pelu-, OP paru-, Skt. purá-, Gk. rodv-. pIE *leugos, OP rauca, Skt. rócas, cf. Gk. Аі
1479:The inst. pl. raucabtš, to rauca? ‘day’, raises а problem. The corresponding declension of neuter -08/е5- stems is, with partial use of Skt. mánas- ‘mind’ and Av. manah- ‘mind, sense’:
1480:pIE Sk. Ау, Фр Nom. sg. *menos mánah mand rauca? Ins. pl. — *menez-bhis mánóbhis manabi$ raucabis Loc. pl.  *menes-su mánahsu raocóhv-a
1481:Apparently the suffix -as- or -az- was in some forms replaced by -ah- where -ah- yielded an easler phonetic development. We may assume that raucabi$ is from raucah-bhi$, that the А became voiced before the voiced stop and was lost in OP, but in Ау. and Skt. was lost with an attendant change of the preceding vowel to 6. A similar replacement is seen in ztira’-kara- ‘evil- doer’, where the Л is lost before the voiceless stop; ef. Skt. manah-pait- ‘Lord of the Mind’.
1638:$133. Encursis is a frequent phenomenon in OP. The enclities are the following: Pronouns: Ist sg. асе. -md, gen. -maty, abl. -ma. 2d sg. gen. -taiy. За sg. acc. -йт, gen. -Saiy, abl. -$a; pl. acc. -&$, gen. -Sàm. acc. -dum; pl. acc. -di$. pl. aec. -àà (dubious; only in avabasa-lé DB 4.72), Coordinating conjunctions: -eà ‘and’, -vë ‘or’. Postpositions: d, patiy; both also as separate words before or after their nouns. Adverbs and particles: -am, -kavy, -ciy, -dty, never separately. -apiy, -paliy both also separately. Miscellaneous: уа in mátya DB 4.43, 48, 71; yadatya XPh 35f (miswritten yadàya XPh 39), cf. yada : tya XPh 29. müm, elsewhere orthotone, in mātyamäm DB 1.52. rádiy in avahya-radiy DB 1.6f, etc.; also separ- ately. Double enclisis: mé-tya-mém DB 1.52; rauca- pati-vd,, DB .1:207 aatpati-mé DNb 20; avā-
2194:J. The neuter formation with suffix -os in nom.- acc. sg., -es- in other forms: type Lt. gen-us gen- ет-18, Gk. *y&-os yév-e-os, Skt. ján-as 3án-as-as. OP has nom. rauta? ‘river’, Skt. srólas; nom.-aec. rauca? ‘day’, Av. raoco ‘light’, Skt. rócas ‘light’; асе. draya* ‘sea’ (and draiya*, §48), Av. zrayd, Skt. jráyas; асе. manaX-cà (§105), Av. mand, Skt. mdnas; acc. züra^ ‘evil’, Ау. 2070; асе. mita? ‘evil’. Inst. manahá, Skt. mánasà. Loc. drayahy-à (with added -2; also written drayahiyà, but whether the ~i- is syllabic cannot be determined), Skt. jrdyasz, ef. Av. manahi-cà. Inst. pl. raucabi$, probably for *raucatbiš, cf. Av. mandbis, Skt. mánobhzs: the -h from -s in certain sandhi positions here trans- ferred to the medial position before the consonant of the case-suffix, and then voiced before the voiced consonant and lost with the same products as when final in the respective languages.
2672:K. To express time when, as їп the adverbs paranam and paruvam ‘formerly’, and with the postposition pakiy: DB 1.20 xsapavd raucapativà ava akunavayata ‘either by night or by day, that was done’; DB 2.61f Güravaharahya mahya jiyam- nam patiy avat sam hamaranam kartam ‘on the last of the month Thuravahara, then by them the battle was fought’.
2693:үшалпаһуа máhya XIV raucabiš бакаіа üha 44 days of the month Viyakhna were past’; DB 1.49 ngiy amazam taumayà Каёсту ‘not anyone of our family’, cf. amáxam taumäyä DB 1.28f depending directly on Kabügiyà; Ра 1f hya mah Ча bagünam the greatest of the gods’.
2694:E. Expressing time within which: DB 4.4f Һатаћуду Sarda in one and the same year’; from this use came the use of the genitive харо, DB 1.20, in a riming pair with acc. rauca and enclitic patiy, to indicate time when,
2715:D. Alone, to express specification: DNb 40f yãumainiš amiy ша daslaibuyü ша pādaibiyā ‘trained am I both as to hands and as to feet’. So also with numerals: DB 2.56 Andmakahya mahyd XV raucabi$ 6akatà aha ‘of the month Anamaka, 15 by days were past’; Wa 1 IT karšā ‘2 (units) by weight’; cf. Lg. 19.227-9.
2866:with genitive and accusative in z$apa-và rauca- pati-vd (DB 1.20), with accusative in |pa]tiy a[va]mc ctam] bardam (DB 5.2f).
2896:DB 1.37f Viyarnahya màhyà XIV raucabiš бабай dha (so also in 17 other dates).
2967:$290. COORDINATION AND SUBORDINATION. Not infrequently the OP texts express by coordinate clauses ideas which are logically subordinate; the result is a series of short sentences, syntactically simple, independent of each other grammatically, but logically and semantically connected. Thus, for example, DB 446-8 vafnà Auramazdaha api- mary aniyascry vasiy astiy kartam ava ahydya diptya пазу nipistam avahyarddiy naty nipistam таша ... ‘by the favor of Ahuramazda indeed, much other (work) was done by me; that (work) is not inscribed in this inscription; for the following reason it is not inscribed, lest . . .’; this could have been expressed in one complex sentence somewhat as follows: ‘much other work was done by me, which has not been inscribed in this inscription for the following reason, lest ...’. Another excellent example is found in XPf 20-25 шій Vistáspa иа Arfüma ubā ajivatam асту Auramazdim арабӣ Ката aha Dérayavaum hya manā рий avam asdyabiyam akunaus ahydyd бата 'Hystaspes and Arsames both were living, then—unto Ahu- ramazda thus was the desire—Darius who (was) my father, him he made king in this land’; in the parallel passage DSf 13-5, yadzy ‘when’ is used . instead of асїу ‘then’, and instead of Auramazdém avatà Ката aha (found also XPf 29f, DSf 15f), we find in DNa 37f (and elsewhere) yada mim ата Gha ‘as unto me was the desire’. In dating sen- tences we regularly have expressions of the type seen in DB 1.42 Garmapadahya máhyà I X rauca- bi$ fakaia aha агава zšaçam agarbdyatd ‘of the month Garmapada, 9 days had passed—then he seized the kingship’; only in DB 1.38 the date is followed by a subordinated clause, yadiy udapa- tala ‘when he rose up in rebellion’. The same phenomenon is probably present where conjunc- tions are omitted as introductory to subordinate clauses, such as the absence of tya in РМ 20 and 50 (cf. DNa 39).
3157:DB 1.20 zšapa-vā rauca-pati-và ‘by either night or day’, in which zšapa- is gen. and rauca- is ace. DPe 13f tyaty utkahyà ula tyaiy drayahyd ‘those which are of the mainland and those which are beside the sea’, where a gen. in *-ahyd is paired
3477:20 : afahya : xSapava :raucapativà : ava : akunavayatà —— :8atiy : Dárayava
3491:42 :agarbàyatà : Garmapadahya : máhyà : IX : raucabis : 0akatà : dha : ауаба : xša 43 cam :agarbàysatá : pasáva : Kabüjiya : uvamarSiyuS : amariyatà : іу
3499:56 máhyà : X : raucabis : 6akatà : dha : ауаба : adam : hada : kamnaibis : martiyaibi
3542:96 pisim : parábara : Andmakahya : māhyā : 11 : raucabis : бака: dha :avatà : hamaranam : akuma
```


## [2026-09-07T01:38:04.003Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK leuk lemma variants ===\"\ngrep -n -i \"leuk-, leu\" POK_full.txt | head\ngrep -n \"leuk\" POK_full.txt | head -20\necho \"== leu(sub)k ==\"\ngrep -n -iE \"Root / lemma: leu\" POK_full.txt | head -20"
}
```


### [2026-09-07T01:38:04.086Z] TOOL RESULT

```
=== POK leuk lemma variants ===
56040:Latin /J/r7e/7 "light' from * leuk-s-men; /una 'moon goddess ') {*lohuksna), praen. Losna{: 
56045:lucubrum "dawn, twilight' ( *leukos-ro-), lOcubrare ' to work by lamp-light, work at night '; 
68259:Root / lemma: pleuk- 
69225:Root / lemma: pi-lo- : hair' : Root / lemma: pu-lo- : hair' derived from Root / lemma: pleuk- 
78072:Root / lemma: (s)leug-, (s)leuk- 
78080:den Schlucken', fAuyyjw), Auyyavoijai Hes. "schluchze"; *(s)leuk-\x\ AuyKoivu) ds., 
78107:Old Low German 5/J/r "squamas'; besides Germanic sluh-, slug- (Indo Germanic *sleuk-) in 
== leu(sub)k ==
```


## [2026-09-07T01:38:05.394Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','SOD','BQT','FSF','AFM','HRN','SYN','MON']:\n    print('==',k, json.dumps(d[k], ensure_ascii=False, indent=1))\n\""
}
```


### [2026-09-07T01:38:06.680Z] TOOL RESULT

```
== POK {
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
== KNT {
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
== SOD {
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
== BQT {
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
== FSF {
 "title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/20220809_20220809_1444",
 "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"
 ],
 "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking",
 "covers_etymology": false,
 "notes": "Persian OCR fair (readable prose). Mostly glosses; some Pahlavi/Avestan notes. Edition may differ from the 1363 Donya print Nourai used."
}
== AFM {
 "title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)",
 "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"
 ],
 "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.",
 "cites": "page number of Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (1908)"
}
== HRN {
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
== SYN {
 "title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949",
 "edition_found": "1949 (reprint scans, same pagination in all printings)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt",
 "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.",
 "notes": "Two other open copies: dictionaryofselectedsynonyms...buck_963_N, fock_a-dictionary-...; restricted: dictionaryofsele0000carl.",
 "cites": "page number of Buck, A Dictionary of Selected Synonyms (1949)"
}
== MON {
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
```


## [2026-09-07T01:38:14.681Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '55960,56090p' POK_full.txt"
}
```


### [2026-09-07T01:38:14.759Z] TOOL RESULT

```
terrible'; 

alb. /unge' ulcer'; 

Latin /uged, -ere' grieve ' {*lohugejd), luctus, -Js "mourning, grief, /ugubris 'sad, pitiable 
' (probably *lugos-ri-s); 

Old Irish /uchtload, content, troop, multitude, crowd, people' (*part?), cymr. //wythload, 
burden, tribe', gall. /ucMos'part' (?), Adj. luchtodos, LVXTIIRIOS, LucteriusUH; 

Old English fo-/ucan ' destroy' , Old High German //ohhan 'tear, rend, pull, drag'. Middle 
Low German /uken'puW, drag, pluck'. Old English lucan' weed ', Swedish luk. Old Norse 
lokr\. "weed'; here GN Lokias " destroyer '; 

" fracture, hole'. Modern High German Lucke, (Low German) Luke; 

Lithuanian lauziu, lauzti, Latvian lauzu, lauzt, trans, "break, rupture', ablaut. Lithuanian 
luztu, luzti, Latvian lustu, lust, intrans. "break, rupture'; in addition Lithuanian /aulas m. 
"heap ruptured, broken branch ', luzisru. "break', Latvian lauzhi" broken tree '. 



References: WP. II 412 f., WH. I 830 f., Trautmann 152 f. 
Page(s): 686 



Root / lemma: lehuk- {*lehugh-) 

Meaning: bright, to shine; to see 

Material: 1. Old Indie rocate^ s\\\ues, seems', Avestan /-aoca/?/- "luminous". Old Indie 

ADcaya// "allows to shine, lights up ', Avestan raocayeiti^ illuminates, lights up ' (= Latin 

luceo); 

Old Indie /iocaA7a- "luminous', roka-v(\. "light' (= Armenian /0/5 "light', eymr. Ilu^, rocisxs. 
"light' (= Old High German loug. Old English lieg. Old leelandie leygrm., Slavie lucb m.), 
/oka-m. "free (bright) room, world' (= Latin /ucus, Lithuanian /a J/r55 "field'. Old High 
German ete. /oh); /ioc5- "luminous' (: Lithuanian Adj. /aukas' outdoors, field, plot '), ruca- 
"brighf (: gr. AuKocpux;, ajjcpi-AuKri, eymr. am-lwg. Old leelandie logu. "flame'), ruc/'-t "light, 
radianee ' (= Old Prussian luckis), rukma-v\. "gold', m. " golden jewellery', rukmant- 
"gleaming' (eompare Germanie Latin -men-s\.exx\)\ rocas-, rocfs-u., Avestan raocah-, ap. 
raucah-n. "light, radianee, esp. of heaven ', Old Indie ruksa- "gleaming', Avestan raoxsna- 
"gleaming' eommon Old Indie gh- > ks- : Old pers. gh- > xs- : npers. xs- > s- 

(= Old High German liehsen) f. "light' (= Latin luna. Middle Irish luan. Old Prussian lauxnos. 
Old Bulgarian luna, zero grade gr. Kdyyoo;, based on this -es-stem also Latin lustrare, 
lucubrare. Old English lioxan. Old leelandie IJds, Lithuanian lukestis); 

Armenian lois. Gen. A/so/ "light', /us/n ' moon' , lusn^ white spot in the eye ', lucanem^ 
ignite, burn', Aor. A/c/ (originally sArd-present); 

gr. AsuKoq (*Ae/7UK6q) " light, gleaming, white' {Kz\)koc„ A£UKiaKO(; fish names), Aouaaov 
"weifterseed in Tannenholz' (: Old Bulgarian /uca irom *loukia)\ Auaaa f. "fury' (after the 
sparkling eyes); a|j(pi-AuKr| " twilight ', AuKO-cpwc; ds., |Jop|Jo-AuKr| " fright image '; AuKapC((; " 
Neumondstag ', is unelear; (eompare Leumann, Hom. Worter2124; after Kretsehmer Gl. 
22, 262 to AuKoq "wolf); Kuyyoc, " light ' ( *luk-s-nos, due to of Y'^y'^stem); unelear is Aouvov 
Aa|jTTp6v Hes.; 

Illyrian PN A£UKapo(;, in addition venet. (?) PN A£UKapiaTO(; (Silesia); 

Maybe alb. A/s/? "berserk, earrion, lushe^bWch, berserk woman' : Auaaa f. "fury' 

Latin lux, -cis " light, brightness ' (older /-stem) lOceo, -ere, lOxf to be light, be elear, 
shine, beam, glow, glitter ', Old Latin also " let the light shine ' ( *loukeid= Old Indie 



rocayati), poZ/JceAe originally "let shine (or see)', hence po//ucte 'prec\ous\ pollucibilis " 
sumptuous, lovely, superb, pretty, splendid', polluctura " a sumptuous entertainment '; 
luculentus^ full of light, bright, splendid ', lucerna^ a lamp, oil-lamp ' (compare Old Irish 
locharn, see below); Jupp/ter Lucet/us perhaps ' light bringer' (Oscan; compare gall. Mars 
Leucetius, Gothic liuhat^): lucus. Old Latin Akk. loucom^ a sacred grove, consecrated 
wood, park surrounding a temple ', actually "(wood, forest-) clearing, light ' (compare 
collucare^ in einem Wald eine Lichtung vornehmen ', interlucare^ prune trees, let the light 
through '), Oscan luvkef^ in luco ' (see above Old Indie ldka-)\ perhaps also Umbrian 
Vuvgis ' Lucius '; 

Latin /J/r7e/7 "light' from * leuk-s-men; /una 'moon goddess ') {*lohuksna), praen. Losna{: 
Old Prussian lauxnos, Avestan raoxsna. Middle Irish luan. Old Bulgarian luna); lustrum' 
period of five years, a purificatory sacrifice, expiatory offering, lustration ' ( *lehuk-s-trom " 
enlightenment '), lOstro, -are' to light up, illuminate, make bright ', also "clean', illustrare' 
brighten, light up ', back formation illustris' lighted up, clear, bright, light, lustrous ', 
lucubrum "dawn, twilight' ( *leukos-ro-), lOcubrare ' to work by lamp-light, work at night '; 

cymr. Hug' shimmer, radiance ', Hug y dydd' daybreak' (= Old Indie roka-, Armenian lois) 
Loth RC 39, 73; gall. Ve^^A-os "bright', *lehuka'\he white', s. Wartburg FEW. s. v. v. 

Old Irish luchair' radiance ', /[75/c/7//ofe "gleaming', luach-te' white-hot, extremely hot '; 
Old Irish locharn, luacharni. "shiner, lantern, lamp, light', cymr. Ilugorn {a\so llygornm., PI. 
Ilygyrn), corn. Iugarn6s., bret. lugernm. ' radiance '; 

gall. Leucetius, Loucetlus ' ep\t\r\et of Mars' (compare Latin-Oscan Lucetlus); Middle Irish 
loch, A/ac/7 "gleaming'. Old Irish ldchet{v\. /7/-stem) "lightning', out of it borrowed cymr. 
Iluched, acorn, luhet, bret. A/c77eo'-e/7/7 "lightning'; Middle Irish /Ja^? "light, moon', dJa lualn' 
Monday ' {*lehuk-s-no-: Latin lun^; cymr. //ty^ "gleaming', llygo' einen Glanz werfen ' 
(compare with the meaning from gr. Asuaau) as "in view, visible, apparent, obvious' under 
cymr. am-lwg, cyf-lwg, eg-lwg"\n view, visible, apparent, obvious'); Middle Irish loch'b\ack' 
{*luko-), cymr. Ilwg' black-yellow ', zero grade Hug 'b\ack' {*louko-) probably originally 
"gleaming black'; 

Gothic lluhaP'Wgbt' (: Latin Lucetlus, gall. Leucetius), Old High German Old Saxon lloht 
"bright' and n. "light'. Old English leohtds.; Gothic lauhatjan'g\ear(\, shine, flash'. Old High 
German lougazzen and zero grade lohazzen 'b\aze, burn, be fiery'. Old English ITegetui. 
"lightning'; Old High German loh' bewachsene Lichtung, niedriges Gebusch ', Middle Low 
German loh, loch' spinney, bush', names as Water-loo, Old English leah' open land, 
meadow'. Old Icelandic loin. ' clearing, glade ' (= Old Indie ldka-e\.c.); Old High German 



lauc, loug, Old English ITeg, Old Icelandic leygr, mask, /-stem "flame, fire' (= Old Indie rocf-, 
Slavic lucb). Old Icelandic logim. = Old Frisian /ogal\ame', Middle High German /ohe 
"flame'; Old Icelandic Ijdmivn., Old Saxon Homo, Old English leoma^ radiance ' {*lehuk- 
mon-), Gothic /a^/7/77^/7/"lightning, flame' {ahu, compare engl. /ei///? "lightning' from 
* lahuhubni-); 

Old Icelandic loni. {*lohuhnd) " still water', lognu. " calm ' (compare gr. Asukh vaAnvn) " 
shining calm '); 

Old Icelandic Ijorim. " Rauchloch ', Norwegian Ijora^ clear up ', Middle High German uz- 
//e rends.] 

due to of -e5-stem Old Icelandic /yrm. ( *lehuhiz) " Lub, Gadus pollichius ' (from the 
bright color of the sides and the belly of the fish). Old Icelandic lysai. " Merluccius vulgans. 
Whiting ', Norwegian lysingds., compare Swedish loja, loga^ Abramis alburnus ' from 
*lahugidn. Modern High German Lauge^ Cyprinus alburnus and leuciscus '); Middle High 
German //e^se/? "bright' {*lehuhsna-= Avestan raoxsna-). Old Icelandic Ijdsu. "light' 
{*lehuhsa-), /j?s5 "gleam, shine, gleam, make bright, define, announce, declare ' = Old 
English Ifexan, /ZVa/? "gleam, shine';
```


## [2026-09-07T01:38:19.871Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=56090 && NR<=56160' POK_full.txt | grep -n \"Page(s)\\|References\" \necho \"---\"\nsed -n '56090,56150p' POK_full.txt | tail -30"
}
```


### [2026-09-07T01:38:21.181Z] TOOL RESULT

```
60:References: WP. II 408 ff., WH. I 823 ff., 827 f., 832 ff., 839, Trautmann 151 f., 164; 
62:Page(s): 687-690 
---

cymr. am-lwg, cyf-lwg, eg-lwg^ in view, visible, apparent, obvious ', go-lwg^M\€\OK\, face' 
(also cymr. etc. Ilygad^eye' from *lukato-)\ 

Lithuanian laukiu, laukti^ wait, await, expect, anticipate, look forward, hope, hold, tarry, 
watch, bargain ', luketT await a little ', Latvian lukuoV look, try ', Old Prussian laukT seek 
'; from " see, show' : " aim, hit, throw ' and "receive, attain, achieve ' : luciti s§^ meet, 
happen by chance '; in russ.-Church Slavic luciti^ meet somebody ', etc. 

4. A parallel root lehuR-\x\: 

Old Indie rusant-^ light, bright, white'. Church Slavic i/bs-Zysb "naked, bald, bleak', russ. 
/K5jy'"naked, bald, bleak'; in addition perhaps the name of lynx, wildcat (development from 
the sparkling eyes or rather after his greyish white fur): Armenian lusanunk'P\., gr. Auy^, 
Auyk6(; (whence the nasalization?). Old High German luhs. Old English lox, next to which 
Old Swedish /dfrom * /{ajhuha- {compare perhaps German Fuchs' fox ' : Gothic fauho), 
Lithuanian lusis, Latvian lusis. Old Prussian luysis. Old Bulgarian rysb (with /"instead of / 
after rbvati^ escape, flee '?); 

Maybe alb. mixed etymology " {ryks + buall) ' = " (cat bull) ': reqebull, riqebulF lynx, wildcat 
' the same as Romanian name for lynx, wildcat. 

Vasmer explains Slavic /"perhaps through Iran, borrowing; not definitely there stands the 
meaning " lynx, wildcat ' for that furthermore on voiced-nonaspirated final sound Middle 
Irish lug. Gen. loga, on the other hand explains Loth RC 36, 103 cymr. Iloer, bret. loar 
"moon' from *lug-ra, so that one so that one could understand -g, -k, -kas extensions; 
compare also above S. 688 gr. Aouvov. 

References: WP. II 408 ff., WH. I 823 ff., 827 f., 832 ff., 839, Trautmann 151 f., 164; 
different Kuiper Nasalpras. 107^.
```


## [2026-09-07T01:38:32.879Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== KNT leaf 220 (printed 205) =====\"\nawk 'BEGIN{RS=\"\\f\"} NR==221' KNT.txt | head -60"
}
```


## [2026-09-07T01:38:33.903Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== HRN leaf 44 (p.23) =====\"; awk 'BEGIN{RS=\"\\f\"} NR==45' HRN.txt | head -50\necho \"===== HRN leaf 157 (p.136) =====\"; awk 'BEGIN{RS=\"\\f\"} NR==158' HRN.txt | head -50\necho \"===== HRN leaf 161 (p.140) =====\"; awk 'BEGIN{RS=\"\\f\"} NR==162' HRN.txt | head -50"
}
```


### [2026-09-07T01:38:34.083Z] TOOL RESULT

```
===== KNT leaf 220 (printed 205) =====
tem (530, $148.I, 6154.1), ef. Av. posana- ‘battle’, Skt. pfiana- ‘battle, army’, to root in Av. poral-onie ‘they fight’? (Bv. TPS 1945.69-4; not agency noun
‘fighter, foe’ as taken by Wb. KIA 90-1, Bv. Gr. $277; not paratara- ‘foe’, with Wackernagel, KZ 59.29-30, as compar. to [Skt.] pára- ‘distant’ = RV ‘enemy’). partaram asn. DNa 47.
Ратдата- (§29.n2, $31) adj. ‘Parthian’, also тазе, as sb. ‘Parthia’, a province of the Persian Empire: Elam. par-tu-ma, АКК. pa-ar-tu-á, Gk. IIapóià. Extension ($150) of stem seen with vriddhi in Pársa-, but with dialectal difference in the 0/s ($9. VT, 887).
(1) ‘Parthian’: Paréava nsm. DN iv; A?P 4. Par&avaibi$ ipm. DB 2.96. (2) ‘Parthia’: Paréava nsm. DB 1.16; 2.7, 92;
DPe 15; DNa 22; DSe 21°; DSm 8°; XPh 20.
Par8avai ism. DB 2.94° 96°; 3.5, 10. parna-, see duildparanam, parana-. ‘parsa- vb., see fraó-.
?parsa- sb. ‘court’, only in Hz. ApI 278; for his pa[r|saiy lsm. DNb 22, see under patiy.
Pársa- adj. ‘Persian’; also masc. as sb. ‘Persia’, a province of the Persian Empire: Elam. par-sin, АКК. pa-ar-su, Gk. Перо, Пероќа (§9. VI, $87, §126, 5143.11). See also Paréava-. `
(1) ‘Persian’: Pársa nsm. DB 1.49; 2.18, 19, 49; 3.18, 26, 31, 32, 56, 84; 4.16, 26, 83, 84 bis, 85 bis, 86; 5.8°; DPe 22; DNa 18, 46; DN i; DSe 12; DZe 7; XPh 12; A?P 1. Pérsam asm. DB 2.81; 8.2, 29f; DPe 21. Pàrsahyà gsm. DNa 13f, 43; DSe 13; XPh 12. Pérsé ism. DPe 8.
(2) ‘Persia’: Pársa пзш. AsH 3 (for loc., §52.1);
DB 1.14, 41; 2.7; DPd 6f; DSm 6°. Pársam asm. AsH 8f; DB 1.46; 3.33, 34; 49, 28; DZe 12. Pérsam-cé DB 1.66. Pürsá ism. XPa 14 (here ‘Persepolis’, acc. to Cameron, by letter; $166, 6166.1). Pürsà absm. РМа 18, 46f; DSe 17°; Юле 7f, 10; XPh 16. Parsa for lsm. AmH 2 (856.V, §314b; wrongly Hz. AMI 4.132-4, 8.17- 9, as instr. of extent); for пзш. AmH 5 ($53; not nsf. adj., as taken by Hz. AMI 820-1, 34). Pärsaiy lsm. DB 1.2, 34; 2.9; 3.23, 24, 28, 34, 52, 58, 71; DBa 2.
pasü prep. ‘after’, temporal with асе. and local with gen. (Bv. BSLP 33.2.153): Av. paséa, NPers. pds, Skt. paácá, isn. to stem in Lith. (dat.) adv. and prep. різки ‘behind, later, after’ (Foy, KZ 35.26); pIE *po as in Lt. po-lið, positus, Gk. &-vó, + *sg*é, inst. to root noun from *seq*- ‘fol- low’, Av... hacatte, Skt) Gdeate, Gk. trerai, Lt.
See nada lai baa a D Lo AMA tae io at OT IPE Ауаз a зз
~
LEXICON
sequitur (§105; Uhlenbeck, Etym. Wtb. d. altind. Spr., s.v. paced). The s in pasá is OP for Med. $c, Av. sé, from pAr. $c (Ву. Gr. §114; otherwise Mt. Gr. §114). Less probably pAr. *pas (Lith. pds ‘at, to’) from the same *po + adv. -s as in OP patiš, + -cà isn. of stems in -айс-, for -acã (from *-ncà) by influence of contracted forms like Skt. praca (*pra-acd) to ртайс- (*pra-atic-) ‘forward’, cf. similar analogical form in Skt. adv. nica ‘downward’ (for *ni-acd) to пуайс-. Hardly from *pas (as above) + -à after its opposite para ‘before’ (Bthl. AiW 879). Direct cognation with Lith. páskw: is eliminated by the second and third etymologies; with Av. pasta, Skt. paícá, by the third. pasã with gen. DB 3.32; with асе. XPf 31 and in pasdva (q.v.).
pasáva phrasal adv. (§191.IV) ‘after that, afterwards’: pasé + asn. ava (8181). DB 1.27, 30, 32, 33, 34°, 35f, 40, 43, 46, 54, 72, 731, 75, 79, 82, 83, 86, 91, 94; 2.1, 3, 4, 12, 16, 19, 21, 27, 31, 32, 47, 49°, 51, 52, 62, 64, 67, 71, 72, 81, 84f, 94; 3.1,4, 9, 12f, 15, 20, 25, 29, 33, 36f, 41, 50, 59, 70, 73,75, 81, 84, 86, 90f°; 4.5, 35, 91; 5.3, 6, 9, 10f, 13, 21°, 28, 25°, 29; DSe 48; DSf 25; DZe 10; XPh 36; XSe 3; XV 23; А:Ра 21°; Рр 4°. pasãva-šim DB 2.76, 90. pasdva-Saiy DB 2.88.  pasáva-dim DNa 33. pasdva-mary XPh 32.
pasti- sb. ‘foot-soldier’: Skt. pailt-, from pIE *ped- ‘foot’ (OP pad-) + suffix -t&- ($85, 5152.11; Wb. Grab 40, Hz. ApI 94-8). — pasti$ nsm. DNb 48, 45.
pilar- sb. ‘father’: Av. pilar-, NPers. pióür, Skt. pitd
```


### [2026-09-07T01:38:35.409Z] TOOL RESULT

```
===== HRN leaf 44 (p.23) =====
OQ
94. efrö^/ten anzünden, erleuchten', Praes. efröz-em^
ewrö/fen [heme-werözT AM. 239 Zeile 1 v. u.), jn5n5N,
furö/ten, furözis^ furöy etc.
aw. aiwi + [^ruc- 'anzünden*; phlv. afröxtan,
a/röcmn, afröcimtan ; skr. abhi + [/'ruc- 'leuchten'.
kurd. vergl. ci]rüstin 'leuchten', dici\rüsi (3. Sg.).
95. ef%är 'Werkzeug', ewzar 'Organ' (AM.).
phlv. afzär 'Werkzeug, "ITZN (Talmud).
Zu ai. 1 V^hur-, Nöldeke, ZDMG. 32, 408.
96. efzuden 'zunehmen, vermehren*, Praes. efzdy-ew,
eirzäden (AM. ; hah-wezäi, 235 Zeile 2), fuzüden, efzün^
fuzün^ efzayis etc.
aw. "^aiwi + \/ snv-, sävaijät 'er wird nützen';
phlv. afzütan^ ofzün^ afzüntk^ afzäyltan, afzäyimtan,
afzäy(i)sn,
97. efsär 'Zügel, Zaum', ßsar.
aw. ^aiwisdra-; phlv. afsdr (Bund.),
syr. talmüd. LW. 1DCN.
98. efsän 'Wetzstein', eusän,^) fesän, vergl. sün,
phlv. afsän (Säy. Näääy. 10, 28); skr. gäna-^) 'Wetz-
stein* + abhi; vergl. B.rm. yesan (H. No. 211).
wa;f. sar. pasän ^Wetzstein'.
99. efser 'Krone'.
aw. ^aiwisara-; phlv. afsar 'Krone' (6ö§t-T Fr.)^).
100. efsurden 'frieren', gefrieren, fusurden^ ßsurden
(Sahn. I, 78 Vers 211).
phlv. afsartan, afsar(i)smh (vd. 19, 12), vergl. arm.
surf, 'Kälte'.
Siehe np. serd (No. 731).
101. efsös 'Spott, Scherz', fisös,
phlv. afsös 'Spott, Scherz'.
Darmesteter's Erklärung, Et. ir. II, 131 aus aw.
*aiwisaoca' ist unhaltbar, da aw. d im Np. nicht zu s
werden kann.
*) ewsün (Vullers).
*) Zu dem n vergl. Joh. Schmidt, KZ. 32, 385.
*J West*, S. 175: awüar; ZPGl. 24, 10; awavBar.
===== HRN leaf 157 (p.136) =====
— 136 -
609. reje^ reze *Reihe\
aw. razista- ^geradester ; ai. räjistha- (Nöldeke,
mündliche Mitteilung). Jüd.-pers. T]T\ dagegen dürfte
zu aw. rasman- 'Schlachtreihe', ai. ragmän-^ racmi'^
ragi- gehören.
Geldner hatte KZ. 24, 387 Note 2 aw. razura-
'Geleis' (yt. 5, 50) vergleichen wollen.
np. rede 'Richtung, Linie, Reihe' (Öähn. I, 367
Vers 823) scheint dagegen zu aw. ereta-, areta-y ai.
ftd' 'richtig, vollkommen' zu gehören (ursprünglich
'etwas Rechtes, Gerades).'
610. ru%8 {rexs) 'Glanz, Licht', ru/^Tden [rexsiden).
aw. vergl. rao/snc^ 'glänzend, leuchtend, strahlend' ;
ai. ruksd' 'glänzend'.
oss. d. ro/s^ t. rü/s 'Licht, leuchtend', rü/say (214);
ya;'n. ru/sinie.
Gehört np. ru/ 'Wange' auch zu derselben Wurzel?
611. red 'weise, tapfer' (z. B. Sahn. I, 149 Vers 365; Vis
und Rämin S. 13, V. 5 v. u.).
aw. ratU' 'Herr'; phlv. rat, -rat^),
612. rezm 'Schlacht, Kampf.
aw. vergl. areza- 'Schlacht'; arm. LW. paterazm
'Kampf, auch razm.
An Ableitung von aw. rasman- 'Schlachtreihe' zu
denken {s könnte statt z vor m stehen), verbietet die
Bedeutungsverschiedenheit (s. No. 609).
613. rest]äy(^e^ 'Auferstehung der Todten'^).
aw. irista- 'todt'; phlv. rist^ ristä/ez (paz. ristaxez),
614. rasten 'wachsen, Praes. röy-em, röylden, röyäniden,
rösta (arab. syr. LW. rustOq), pNDDn, Is. 42, 11.
aw. |/>c/orf-, raoöahe 'wachsen'; phlv. rustan (bezw.
rödastan , aber nicht wahrscheinlich), röyend bezw.
rödent (3. Plur.), rostäk [rödastak, Salemann, Eine
*) Vergl. Nöldeke, Tabarl-Obersetzung, 447.
*) Kaum gehört hierher röz-l *ir,9 'Todestag' (Pertsch, Die
persischen Handschriften der herzogl. Bibl. zu Gotha, S. 115, 116),
vergl- de t^agarde, Ges. Abb» 3?,
===== HRN leaf 161 (p.140) =====
— 140 -
ap. raucah' 'Tag; aw. raocah- 'Licht*; phlv. rüc^
röcllc (arm. LW. rocik), röckür (Bund.); ai. röcis-
'Glanz, Licht*; arm. lois Xicht' (H. No. 125).
kurJ. ruz; aty. vraj ; bei. röc, n. ros 'Tag, Tages-
licht, Sonne* (824) ; wa/. räiij 'Flamme'.
LW. seldsch. iiruz\if uriiz[yn^ Salemann, Noch
einmal die seldschukischen Verse, Mel. asiat. X, 211;
vergl. yrys 'Glück' ebendas.
630. rözen 'Fenster'.
aw. raoöana- 'Fenster ; phlv. röcan ; ai. röcanä'
(nur 'Licht, hell').
631. vöseti 'leuchtend, hell', rösna^ rösem.
g. rmnäye,
ap. vergl. hoidv/]^); aw. ruoysna' 'leuchtend'; phlv.
rosan^ rösanili, roSnäk, arm. LW. r. s/iakuH, rösnntitin,
LW. af/. rö/cifi, rö/näl; bei. rösani^ rösanal (324);
si;n. rosnagd 'Tageslicht*, sangl. rösnäi 'Feuer.
Vergl. No. 610.
632. röyen ^Butter, Öl*.
Käs. rüyän, rö.
aw. raoyna- 'Ol'; phlv. rökan (d. i. röyan^ päz.
raoyftn), royan (PPGL).
kurd. rrin\ bei. (LW. ?) rogan^ rögan, n. röya/i,
röyin (327); LW. wa;<. rilgfi, royim, minj. royün,
sangl. röy, sar. rdim,
633. vom, röme 'Schamhaare', nun, riimbe (geschr. rnnhe)').
ai. roman- 'Haar am Körper der Menschen und
Tiere' (in der Regel mit Ausschluss der langen Kopi-
und Barthaare).
*) Rösanaq in der syrischen Version des Alexanderrumans
(Nüldeke, Denkschr. WAW. Band 3ö).
^) Der Vers Lebibi's im FR ist in der zweiten Hälfte fcliler-
V
haft; er muss nach einem ganz ähnlichen im FJ emendirt werden, der
lautet (Metr. Heze.]):
2)e8 rls^ kenl cu rumh^-l zen
Der Witz liegt darin, dass die Frauen keine Schamhaarc haben.
```


## [2026-09-07T01:38:56.225Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT raocah ===\"; grep -n \"raocah\\|raoc̆ah\\|raocah-\" BRT.txt | head -20\necho \"=== BRT raoxšna ===\"; grep -n -i \"raoxsna\\|raoxšna\\|raoxšna-\" BRT.txt | head -20\necho \"=== BRT aiwi raoc ===\"; grep -n -i \"aiwi.raoc\\|aiwi-raoc\\|aiwi raoc\" BRT.txt | head -20\necho \"=== BRT erexsa ===\"; grep -n -iE \"r.x[sš]a-|Erexs|erexs\" BRT.txt | head -20"
}
```


### [2026-09-07T01:38:56.322Z] TOOL RESULT

```
=== BRT raocah ===
4571:N.  io_y;  —  ("K})''''  raocahe  nsit  "r?  timahe "bei  Tageslicht,  nicht  im  Dunkeln"  N. 68.  b)  mit  Instr.**  'unter,  im  Kreis von  — ':  ratus  .  .  ratuiiaim  ayesnim  dasle 'n  mazdayasnäis  A.J,7;  8— la;  —  °r? :^adasnäis  asoonf/Vr. 21.3; P.36.  c)  mit Lok. 'zwischen':  "rs  haitisu yasiDnt  ^/räiziS (sd.)  N.  40.  3)  Praev.  (mit  'aj'-,  'kar-, mrav-,  'v3-  usw.).  [V.5.19,  p.33,  Yt
6414:•  j.  aSö.raocah-  m.  £N.  eines  Gläubigen: °la»hS  fränyehe  aldcnS  "des  A.,  Sohns des  Fr.  .  ."  Yt.  i^.  97.
14697:—  mal^me  'sve  *aiihä  zjmS  Y, /r.  7;  — raocahinS  aoi  'svä  (AP.)'>  "strahlend  nach (allen)  Dritteb  (der  Erde)"  Yt,  13.  2 ;  — paoirysi  'sväi  xsafne  (sd.)  V,  /Ä'.  1 8 ;  so,  2  2 ;
24864:'raocah-  5  a
24868:•  ').,  g.  'raocah-,  p.  raucah-  n.  i)  'Leuchte' (bes.  des  Himmels) :  hvare  'c5  Vr.  if).  2, Yt.  6.1;  —  slrSUiäi  mdiiA^mcn  hvanca °ca  "die  Sterne,  den  Mond  und  die  Sonne, die  (himmlischen)  Leuchten"  G,^.  6;  — mt^nm  .  .  yeivhe  vaxl .  .  us  ava  -La ainaeiti  ava  pairi  imqnt  sqm  jasciiü  "M, . .,  des  Stimme  hinauf  bis  zu  jenen  Leuchten dringt,  rings  um  die  Erde  gehl"  Yt,  10. 85;  90,  H. /.  16;    —    c'ay3  Hat  aile  ''iv!'>
24881:KompA.  (s.  raarahi.').  —  Zum  V.  raak-.  —  Vgl. traocah:   —  Pü. ;  risn,  (lu  F.):  röitüh.
24887:•  j.  raocah'vant-  Adj.  'licht':  a/^m  at vahUtim  yatamaids  .  .  kyat  'cönnhvat  Y. .37-  4-
27543:\'rä   iyeinte  (Sp.  148  u.)   (antarv)  raocahe
=== BRT raoxšna ===
5386:•  j.  auruäa-  Adj.  'weiss',  1)  von  Tieren: pttsüm  .  .  'hm  vH  vohu.gaon^m  vä  "ein weisses  oder  schwarzes  Schaf  Yt.ÄsS; —  aspa/ie  ktkrpa  'iahe .  .  aspahe  kihrpa sämahe  "in  Gestalt  eines  weissen  Rosses . .  in  Gestalt  eines  schwarzen  Rosses"  Vt. Ä  18-21";  —  aurvants  'la  raoxsna  fnl- ä)r»sra  Y. 57, 37;  YL  JO.  136.  z)  sonst: srlra  i-a  auhtn  blzava  'h  (ND.)  Yt.5.7;
8256:'bei;  in',  räumlich:  yatHl  ahi  . .  'pa  sanake (sd.)  rauhaya  Yt,  i2. 19;  —  °pa  aolaisu (sd.)  rai^haya  Yt/2.18,  V./.19;  —  'pa upaMdi  (sd.)  harayi  ¥1.5.21;  —  yaecit qzaAu  diniäaks jaininqfn  *'pa  *dpmshu*'' Y.  10. 1 7.  3)  mit  Gen.  (?)  'bei',  räum- lich: yatcit  ahi  .  ,  "pa  raoxsnahe  garS nmänahe  Yt.12.37*'.  Wertlos:  II  "imam ustasa/iäm  .  .  mäm  'pä  mäm  karta^  Ao. /.3*>.  U)  Pracv.  (mit  ^ay-,  gam-,  'mar-, Sil};  tav-  usw.).  A)  bei  Ellipse  des Verbums:  'pa  ta  nS  aiwyilsta  (NS.) harjsma  .  .  Vjrt.2j(?).
19315:—  haca  raoxsna  garU  'na  . ,  irrjata  haca dusanha  Yt.  ig.  44;  usw.  c)  g,  mit  GS. varfhsul  mananhs  dnwB."'  (vgl.  e):  tBi.. bairyantl  (sd.)  vaahSus  a  °«i^'  manaahS Y.33. 15.  d)  g.  mit  GS.  drüjS  (sd.)"" von  der  Hölle:  drüp  -«f  ¥.4:5.11,  5/.14;
24809:raoxSnav-
24838:•  j.  raoxSna-  i)  Adj.  'licht,  glänzend':  'mm .  ,  ya^a  iltr»m  Vyt.  .i;  —  '/Dm  mäuhtm ^^■7-3'>  —  tislrim  .  .  aurui)m  'tum  /rj- dinsmn  YLä  2;  —  asmatum  y?  .  .  'nJ frädinsrS  Yt.  13.1;  —  °mm  garö  nmUrum S.  2.  30;  —  haia  'na  *garj  nmäna  YL  sg. 44;  —  'näi  paili  *garS  nmSnSt  Yt.  10. 123;  124;  —  'naht  ''gorö  nmänahe  S. /. 30;  Yt.  12. 37i  —  nrnJimm  . .  frSäfrisnm 'mm  V.  22.  1 ;  —  am»sanqm  sptntanqtn .  .  yaSsqm  'natihä  fantänS  ,  .  Yt  JJ. S4;  —  aurvatitd  auruh  'na  frädinsra ^■37-^7'>  —  yer>he  urva  ..  aurusö  'nS frädirisrö  Yt.  13.  81;  —  'na  frayantu  ti OTd!OJ(sd.)  Y. /o.  19.  2) n. 'Licht':  'tum kfnnavühi  dämahva  V.  2/.  5.  a)  Plur. 'Flammen':  yai  neif ..  ä^re  **nam "'  paili.- äily^i  V.  16.  2.
24840:•  j.  raoxsnay-  i)  Adj.  'licht,  glänzend': tilirim  . .  dural  vyävant?m  (sü.)  bänubyB 'niiyj  \l.S.2->.  2)  n.  'Licht,  Licht- glanz' (nur  Komp.).
24842:•  j.    raoxsnav-    n.    'Licht,    Lichtglanz':
29002:von  I  1;  a)  im  jAw.;  zu  a  o):  Aa/  nä a%rava  a%auru>um  k°  *gathäbi!  *parayilt (sd.;  'abeaf)  N.4;  —  ärux!  .  .  ya  k* irista  upa  Jvoräim  upa.dvasaiti  ('arvolat') ..ya  h' irista  upa  Jvani>m  upa.raei;waiti ('inirat')  V.  /O.  i ;  —  avanayeni  ('dcducam') spmSim  mainyüm  h'  raoxsna  *garS  nmäna uspalayeni  ('expellam')  anr>m  mainyBm »rrfata  h-  duiaKha  Yt/p.44;  —  »riza- taina  h'  taSta  saranamim  aoi  taxle ('affundo')  Y.  jo.  17;  —  h'  u^asiara  handva avi  daosastarPtn  k»ndum  V.  i.  18  PUZ. (Verbum  fehlt);  —  neben  einem  blossen Abi.:  haomtm  ytm  nivizaiti  (Sp.  1329  o.) nivandat{sA.)  apoyeiti  ('abscedit!)  [dusmain- yaoi\  pfiana  A'  Yti4.$7.  za\i):  paiti.- p?r)ne  ('oppugno')  atinm  mainyüm  h° nmOna   h'*  . .  h'   daiiihu   V.  jo.  5*';  —
=== BRT aiwi raoc ===
13235:—  tairlm  gäma  (sd.)  frabarat  .  .  urva anayragiva  raocöAva  mdarjät  H.  2. 1 5 ;  1 5^, 33;  vgl.  f;  —  yavat  .  .  kangmrvayqn altavat  . .  Au/ie  (sd.)  zpme  nidaiiyan  V. ''■  29;  31;  —  Ja/W  (sd.)  . .  WM?  nihaite (NDf.)^'>  V.7.45;  49;  —  taohri  ..  ta Als  dasva  garS  nmätu  Yt.  /0. 3  2 ;  —  at  Asi vaAmSng  dfmäTig  garS  (sd.)  nidämä  Y. 45-  8;  —  mi^ma  . .  yaAmt  vyäne  (sd.)  . . masfl  amava  niiälim  Yt./o.64.  b)  wo?- Adverb:  kva  narqm  iristanqtn  tanom  ba- räma..kva  nidäiiäma  V.6'.44;  —  astala . .  tanüm  nidai^yan  V.5, 12;  —  daxma  . . yaAmya  narö  irista  tmayeinte  V,^.  9;  • — an'öpäo  m  nidaiaite^  a/is  .  .  *aniar?.- ar^i^m  nmSnoAe  Yt  iS.  4.  c)  Instr. : Aiiu  pqsnu  (sd.)  gitu  niaayaila  V.  16. 2.  d)T>3X.:  ai^ä  aAmäi  varmüi  ..nidä- tfttt  ahm  süiäyäi  tkalsäi  (sd.)  rSiayeAAf druxSY.4S-Z''  —  amtmca  Vfr^^rayti^mca ni'jät>m  tanuye  Yt  14.  38.  e)  Gen.: huskanqm  (näml.  alsmanqia,  als  Obj.)  . airiAa  S3ms  (sd.)  niäaÜyqn  V.  7.  29;  — aSa^qm:a  (näml.  Aaoliianqm,  als  Obj.) zftitö  nidaiiyqn  antarfin  ar?wtn  nmänaAe V.  6".  43;  -—  äat  vohu  maiiB  nidatoTi.. raocaukiim  yat  Ae  stärqm  aiwi.raocayantt "dann  sollst  du  (ihn)  .  .  dem  Licht  aus- setzen, damit  . ."  V. /^.  23.  f)/(7jÄund Lok. :  paoirim  gäma  (sd.)  frabarat . .  urva Attmate  paiü  nidaläl  H.  2.  15;  15';  vgl.  a,
16648:•  j.  baj-ö.däta-  Adj.  'gottgeschaffen':  y.it hx  stäram  'tanam  aiwi.raocayänte  "damit ihn  die  gottgeschaffenen  Sterne  bescheinen" V.  ig.  33.
24824:mit  az-i  und  aiwi  'aufflammen  lassen, entzünden  an  — '  (Gen.):  aii  äim  (näml. zanqm)  aiwi.raocayäti  li^rö  V.5.  2.
28640:zu  Ic.  hi,  /f  bezieht  sich  auf  das  Subjekt des  gleichen  Satzes  (Reflcxivum);  nur Sing.;  ha  (n'äml.  andvt)  ^/(fem.)  maiäim nyStata  Vt.5.  ia7;  —  yat  hl  (mask.) *manS  *ahe patti  barät  V.^S-j^fi;  — yesi sl  »aoHrä  baraiti  (Sp.  935  m.}  avi  ii maiharum  YtiO.  136;  —  ya%a  yal  hl (zu  ß)  '^'  pqstü/ra'i:at3h>m  (sd.)  kain?r»him k}r»nuy3t  V.iS.  10;  —  paourva  hl  nsmd baraiti  (Sp.  936  m.)  Yt.j^.36;  —  nava- napiyal(,sä.yii  hl  (zu  a)  urvätum  para.- mirjncaite  V.  13.  y,  —  pasca  *hähra *a/rasruiti  !i  (zu  ß )  paiti  tanüm  *piryeite  j N. 7.  A)  der  Gen.-DaL  vertritt  den! Akk.'^',  nur  im  jAw.;  Sing,  und  Piur.;| zurückweisend:  3al  vohu  manS  nidat6ls\ yal  hl  stärqm . .  aiwi.raocayimeV .ig.^y,  I
=== BRT erexsa ===
24726:•  j.  raek-  V.  'linquerc'.  Praes.  8  irinak-, i6  (Des.)  irlrixsa-,  30  (Iter.)  raf'aya-; j-Aor.  I  raixs:  —  PFP.  'riiya-;  Inf. »rixti,  'ri^3;  AbsoL  'irixtfm.
```


## [2026-09-07T01:38:57.084Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN leaf 494 (p.470) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==495' SYN.txt | head -40\necho \"=== SYN leaf 1015 (p.991) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==1016' SYN.txt | head -40"
}
```


### [2026-09-07T01:38:58.293Z] TOOL RESULT

```
=== SYN leaf 494 (p.470) ===
- ve the d e. ' ‘adornment’ (6.71). 4 |. ram é, Pol. poh. ram 6.75 NECKLACE = ON men, halsgjord Lith. kaklarysis, karieliat Grk. pH arpentés, TEPt Dan. halsbaand Lett. kakla ruota i Sut halsband ChSl. meen grivina, iG xeptdtpato OE mene, healsbéag, ozrélt tat monile, torques sig(e)le SCr.  derdan it,  collana ME coler Boh.  ndhrdelnit Rr. Bie NE necklace Pol. naszynik §p. oe ghiordan Du. halssnoer Russ. ozerel’e (monisto) a Bones eanintore OHG menni, halsboug, hals- Skt. kanthika-, kantha- ; i golt bhiisa- a oo MHG _halsbouc, halsgolt Av. minu- Aue NHG  halsband
W,  guddfdorch, glevn- dorch Br. __tro-c’houzoug
Most of the words for ‘necklace’ are derivs. or cpds. of those for ‘neck’ or ‘throat? (4.28, 4.29) and so often parallel to those for ‘collar’ or ‘necktie’. A few are from verbs for ‘string together’, ‘turn around’,
1, Grk. dpuos, fr. the root of etpw ‘string together’, Lat. serere ‘bind together, en- twine’, ete. Cf. ON sérvi ‘necklace of ae pearls, or the like’. Walde-P.
en Ag and orperrév, sb. use of
* 4d). o D ¢ s
Walde-P, 2632, turn, roll, twist’. Grk mepide
ni , Patov, :
about? and d&pn Roa deriv. of rept
4. monile : Ty.
. muince, OW sie men (also hals-men), OE mn i (also heals~mene), OHG Bicies : gees ChSl. monisio (cf. lee 6), Gallo-Grk. Havidkns ti, on" oe necklace’ : Ir Mon,’ Oy a SKt. manya- ‘ Z Ba steno
Emout-M, 628,
Lat. torqués : torquére ‘turn around, twist’ (10.13). Hence Ir. torc, W. torch in Ir. muin-torc, W. gwddf-dorch, glein- dorch (W. gwddf ‘neck’, gleiniau ‘gems,
beads’). Ernout-M. 1047. Vendryes, De hib. voc. 183.
It. collana, fr. collo (Lat. collum) ‘neck’.
Fr. collier (> Rum. colier), Sp. collar, fr. Lat. colldre ‘band or chain for the neck’ (for captives, animals, etc.), fr. collum ‘neck’. ME coler (also ‘collar’), fr. OFr. coller, collier.
Rum. ghiordan, SCr. derdan, fr. Turk. gerdan ‘neck, necklace’, fr. Pers. gardan ‘neck’. Lokotsch 675. Tiktin 675.
3. Ir. muince, muintorc, above, 2.
Ir. basc, perh.: W. baich ‘burden, load’, Lat. fascis ‘bundle’, ete. Peder- sen 1.77. Walde-H. 1.459.
W. gwddfdorch,  gleindorch, above, 2.
Br. tro-c’houzoug (Vallée), cpd. of tra ‘twisted’ and gouzoug ‘neck’.
see
In Public Domain. Gurukul Kangri Collection, Haridwar
4. ON men, OE mene, OHG menni, above, 2.
ON halsgjprd, lit. ‘neck-girdle’ (ef. 6.57).
OE sig(e)le ‘necklace’ beside sig(e)l ‘brooch’, fr. Lat. sigillum ‘little image, seal’, Generalized first through ‘signet- ring’ to other pieces of jewelry? Falk- Torp 953 f. NED s.v. seal, sb.’.
4 OE healsbéag, OHG ha
=== SYN leaf 1015 (p.991) ===
isaram, abritim
7. Skt. uttama-, Av. ustama-, above, 1. Skt. antima-, fr. anta- ‘end’ (12.35).
13.46 THREEFOLD, TRIPLE
TpiTAovs, TptmAGoLos tpirdds, Tplétmdos triplex, triplus triplo
triple
triplo
triplu, tntrett tréode, fo thrt trifhillte, tri otread triphlyg, tridyblyg tric’ hement
*brifalps
prifaldr, prennr tredobbelt, trefold(zg) tredubbel, trefaldig prifeald
threfold, treble
threefold, triple drievoudig, driedubbel drifalt
drivalt(ec)
dreifach, dreifaltig
trigubas, trilinkas, trejopas
triskarligs
trigubit
trostruk
trojndsobny
potrdjny, iréjnasobny
trojnoj
trigura-
(cf. haptavbya-, visaitivant-)
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
13.52 THREE APIECE
Tpets Kad’ éxagrop (xad’ %&a), avd Tpels
amd Tpets
terni
tre @ ciascuno (a uno)
chacun trois
cada uno tres
ctle tret
cach tri
tri an ceann
bob yn dri pep tri (twethnaz)
hverjum prir, prennir hver tre
var tre
ale pri
ech thre
three each, three apiece elk drie
```


## [2026-09-07T01:39:10.592Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^\\s*14\\.41\\|14\\.41 DAY\\|15\\.56\\|15\\.57\\|BRIGHT\" SYN.txt | head -20\necho \"--- find leaf numbers for those lines ---\"\npython3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if '14.41 DAY' in p or 'DAY (' in p and '14.41' in p:\n        print('leaf',i,'printed?',i-24)\n        print(p[:600])\n        break\nfor i,p in enumerate(pages):\n    if re.search(r'15\\.5[0-9]\\s+(LIGHT|BRIGHT|DARK)', p):\n        print('leaf',i,'printed?',i-24, p[:300].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-07T01:39:11.887Z] TOOL RESULT

```
1685:NIv. gealach ‘moon’ also ‘light, bright- ness’, fr. geal ‘bright, white’ (15.57).
1743:5. Lith. Zaibas, Lett. zibens : Lith. Zibéti, Lett. zibtz ‘shine, glitter’ (15.56).
1745:7. Skt. vidyut-, i.e. vi-dyut- fr. dyut- ‘shine’ (15.56).
1861:1. Grk. xa, ChSl. séni, SCr. sjena, Russ. sen’ (Boh. siti, Pol. sien, Russ. seni ‘entrance room’, etc., as room without light), Skt. chaya-, Av. *saya- (a-saya- ‘without shadow’), NPers. saya-, Alb. hé, fr. IE *skai-, *ski-, prob. the same root as in Goth. skeinan, OF scinan, Ch§l. sijatt ‘shine’ (15.56). Connection through a notion of ‘faint light’ (as in NE shimmer, NHG schimmer) or ‘re- flection’. Cf. OF scima ‘shadow, gloom’ beside scima ‘light, brightness’. Walde-
2198:2. Lat. accendere (> It. -accendere), imcendere (> It. incendere, Sp. encender, Rum. incinge), succendere, epds. of *candere: candére ‘shine, glow’ (15.56).
14304:Fr. déchirer, cpd. form of OF’. eschirer, prob. fr. a Frank. *skiran : OE sciran ‘make clear’ (: OE scir ‘clear, bright’, etc., 15.57), ON skira, OFris. skirja ‘cleanse, purify’, EFris. schiren also ‘smooth off’, ete., with development through ‘scrape off’ to ‘tear off’. Cf. on Lith. bielyti ‘flay’, 9.29. Braune, Z. rom. Ph, 20.355 ff. Gamillscheg 295. Other- wise REW 7990.
25291:TIME 991 14.41 DAY Goth. dags Lith. diena utp ON dagr Lett. diena jplpa Dan. dag ChSl. dint diés FS) Sw. dag SCr. dan giorno ( OE dag, dagor Boh. den jour ME day Pol. dzien dia NE day Russ. den’ (a . Du. dag Skt. ahan-, dina- laa, laithe, ae OHG tag diva(sa)- : la MHG tac Av. ayan-, azan-, OPers. ee NHG tag rauéa ei the majority of the words for ‘day’, | Gall. lat. (Calendar of Coligny) : ChSI.
25859:15.56 Save
25865:15.57 Bricut
26452:Bete (15.56). Walde-P. 2.123 f.
26475:15.56 SHINE
26495:Sch 806. Macbain 358. r, aim, Br. lugerni, above, 2. (15.57), isgleirio, fr. disglair ‘bright’
26519:15.57 BRIGHT
26532:‘shine’ (15.56). Some are simply pples. of the latter, and many other such words for ‘shining’ might have been included as virtually equivalent to ‘bright’.
26533:1. Grk. Xapympés (NG pop. only in fig. sense ‘splendid’; in lit. sense Napmepés) : Aayrw ‘shine’ (15.56).
26534:Grk., Ion. daevds, Lesh. paevvos, Ait. Paves, also dwrevds, derivs. of paos, Pas ‘light’ (1.61), like ¢aeivw ‘shine’ (15.56).
26586:7. Skt. guct-, ¢ukra- : cuc- flame, burn’ (15.56).
26634:Most of the words for ‘light’ in color are the same as those for the broader ‘light’ = ‘bright’ (15.57), and this spe- cial use is mostly modern. So NE light in this sense from 15th cent., MHG lieht rarely in cpds. as liehibla ‘light blue’, NHG licht usual in Austria vs. hell with reference to color (Kretschmer, Wort- geogr. 234).
26662:4, Ir. dorche, see under sorche ‘bright’ (15.57).
26676:Av. axgaéna-, neg. cpd. : rsaéta- ‘bright’ (15.57). Barth. 51.
--- find leaf numbers for those lines ---
leaf 1067 printed? 1043
dwar
i * »
Soh
Digitized by Arya Samaj Foundation Chennai and eGangotri
990 SELECTED INDO-EUROPEAN SYNONYMS
W. eilwaith, lit. ‘a second time’, fr. eil- ‘second’ and gwaith in cpds. like teirgwaith ‘three times’, etc. (13.44).
W. drachefn, ‘backwards’ and ‘again’, fr. tra ‘beyond’ and cefn ‘back’ (4.19). Morris Jones 410.
Br. c’hoaz, MBr. hoaz = Corn. hweth ‘yet, again’, etym. dub. Pedersen 1.379. Henry 170. Ernault, Dict. étym. 312.
4. Goth. aftra (reg. for ré\v, but also ‘backwards’), ON apir (‘backwards’, late ‘again’), Dan. alter, Sw. dler, OE eft (beside aefter ‘after’) : Goth. aftard ‘be-
leaf 1127 printed? 1103 t, white’ (15.64), Skt. hari- ‘tawny, yel- low’, OE geolo, OHG gelo ‘yellow’, etc. (15.69). Walde-P. 1.624 ff. Falk-Torp 328 f. | 7. Lith. Sviesti, ChSl. svétiti, general Slavic (in part refl.) : ChSl. svété ‘light’, Skt. cveta-, Av. spaéta-, Goth. hweits ‘white’, etc. (15.64). Walde-P. 1.470. | Lith. Z
```


## [2026-09-07T01:39:23.368Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if '14.41 DAY' in p:\n        print('=== leaf index',i)\n        print(p[:2500]); break\nimport re\nfor i,p in enumerate(pages):\n    if re.search(r'\\b470\\b', p[:400]):\n        print('=== possible printed 470, leaf',i)\n        print(p[:900].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-07T01:39:24.613Z] TOOL RESULT

```
=== leaf index 1067
dwar
i * »
Soh
Digitized by Arya Samaj Foundation Chennai and eGangotri
990 SELECTED INDO-EUROPEAN SYNONYMS
W. eilwaith, lit. ‘a second time’, fr. eil- ‘second’ and gwaith in cpds. like teirgwaith ‘three times’, etc. (13.44).
W. drachefn, ‘backwards’ and ‘again’, fr. tra ‘beyond’ and cefn ‘back’ (4.19). Morris Jones 410.
Br. c’hoaz, MBr. hoaz = Corn. hweth ‘yet, again’, etym. dub. Pedersen 1.379. Henry 170. Ernault, Dict. étym. 312.
4. Goth. aftra (reg. for ré\v, but also ‘backwards’), ON apir (‘backwards’, late ‘again’), Dan. alter, Sw. dler, OE eft (beside aefter ‘after’) : Goth. aftard ‘be- hind’, Skt. apataram ‘farther away’, etc., derivs. of IE *apo in Grk. aré, Skt. apa, Lat. ab, etc. Walde-P. 1.49. Falk- Torp 36. Feist 12.
Dan., Sw. igen = ON 7 gegn beside gegn ‘against’ = OHG gegin ‘against’, etc. Similarly OE ongegn, ongean ‘back, against’, whence ME agen, NE again ‘again’, but locally also ‘back’ or ‘against’ (cf. U.S. rural I’m agin it). Falk-Torp 314. NED s.v. again.
Du. weer, OHG widar, MHG wider, also and orig. ‘against’, like OF wiper : Goth. wipra ‘opposite, in the presence of’, Skt. witaram ‘further’, fr. *vi- ‘apart’, in Skt. vi-, etc., with suffix -tero- in words of contrasting relations. NHG wieder, wiederum, with differentiated spelling for sense ‘again’ vs. wider ‘against’. Walde-P. 1.312f. Feist 570. Weigand-H. 1255.
NHG nochmal(s), fr. noch ‘still’ and mal as in dreimal ‘three times’, etc.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
(13.44), Similarly abermal(s), fy, aber in its sense of ‘again’. Weigand-H. LG.
5. Lith. vél, vélei (Lett. vay ‘still’) ; veltt ‘to full’ (orig. ‘turn’), Lat, volvere ‘turn around’, etc. (10.13), ‘Again’ fr, ‘turn’ as Grk. réAw (above, 1). Walde- P. 1.303. Mithl.-Endz. 4.558.
Lett. atkal : Lith. atkalas ‘turned around’, this : atsikalti ‘lean on’, Mihl.- Endz. 1.163. Trautmann 114,
6. ChSl. paky : opako, opaky ‘back. wards, behind’, Pol. opak ‘turned around, wrong way’, Skt. apdka- ‘far off’, derivs. of *apo- in Grk. ad, Skt. apa, ete. Walde-P. 1.50. Briickner 380.
SCr. opet, Boh. opé, Pol. (obs.) opi¢é, Russ. opjat’ = ChSl. opeti ‘back- wards’ : Lith. atpent, atpené ‘back, in re- turn, on the contrary’ (cf. NSB), epds. of words for ‘heel’, ChSl. peta, Pol. pigta, Russ. pjata, OPruss. pentis (Lith. pentis now ‘butt end of an ax’), and so orig. ‘on the heels of’. Trautmann 214, Briickner 380, 412.
Boh. zase ‘backwards’ and ‘again’, fr. za ‘behind’ and refl. se, like Pol. zag ‘but’, earlier
=== possible printed 470, leaf 509
at. occulere, célare, Ir. celim, OE helan, etc. (12.26, 12.27). Walde-P. 1.482 ff. | NG xadtBa is, through Turk., the source of SCr. koliba, Rum. colibd, etc. Berneker 546. | Grk. wAicla, Hom. xdtcin (‘hut’, also ‘couch’) : kXtvw ‘incline, recline’, xAivn ‘couch’, Goth. hleibra ‘tent? (7.14), etc., IE *flei-. Walde-P. 1.490. Boisacq 470 f. | 2, Lat. casa, etym. dub., perh. as orig. ‘wickerwork’, fr. *kat- in Lat. caténa ‘chain’, cassis ‘net’, etc. Walde- P. 1.338. Walde-H. 1.175 f. | It. casupola, dim. of casa, after it had become ‘house’, REW 1752. | Lat. tugurium (> It. tugurio), teguri- um, fr. tegere ‘cover’ (12.26). Ernout-M. 10.20. | Late Lat. capanna (Isid. 15.12.2 tugu- rium casula est... . hunc rustici capan- nam vocant), orig. dub., perh. fr. cannaba ‘booth’ with form influenced by capere. Hence It. capanna, Sp. cabafia, NE cabin, ete. Ernout-M. 146. Walde-H. 1.156. REW 1624. | Fr. hutte, Sp
=== possible printed 470, leaf 724
co, JAOS 67.100 ff. | 3. IE *wei-, esp. in words for ‘wind’. Walde-P. 1.223 ff. Ernout-M. 1106 f. | Lith. vyti, vynioti; ChSl. vigq, viti, stiviti, SCr. viti, Boh. viti, (na)vinouti, Pol. wié, Russ. vit’; Skt. vi- (sg. pres. vyayati, pple. vita-); Lat. viére ‘bend, plait’, etc. | 4, IB *seu-, *seu-k-. Walde-P. 2.470. Pedersen 2.635 ff. | Ir. sdim, cpd. imbsdim, impodim (imb- ‘about’, but cpd. not exclusively ‘turn around’), NIr. iompuighim; Lith. sukti ‘turn around, twist’, ChSl. sukati, Boh. | CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar | Digitized by Arya Samaj Foundation Chennai and eGangotri ; | 666 SELECTED INDO-EUROPEAN SYNONYMS | soukati ‘wind, twist’ (thread, wool, etc.), Russ. skatat’ ‘roll up’, skatit’ ‘roll down’ etc.; also *seu-p- in Lith. supti ‘swing, rock’, | 5. Grk. rpérw (Lat. trepit ‘vertit’ only in Festus and prob. fictitious after Grk.) : Skt. trap- ‘be ashamed or perpl
=== possible printed 470, leaf 758
 ungsgesch. 337) : Av. aiwi-garaémahi ‘we begin’, Lat. gradt ‘step, walk’, Ir. in-grennim ‘pursue’ (10.53). Walde-P. 1.652. Berneker 349. | 6. Skt. (G-)é-, ef. ‘go’ (10.47). | 10.49 GO AWAY, DEPART | Grk.  dx-(-)épxopat, ava- Goth. afleipan, usgaggan | Lith.  28eili, nueili | (470-) xwpiw ON ganga af, ganga brotl Lett. aiztet NG dvaxwpd, debyu, Dan. gaa bort, drage bort ChSl. _ oltti, izitt | procebu Sw. g& bort SCr. olici Lat.  ab-(ex-)ire, discédere (0}0j gewtlan, wttgan Boh.  odejeli It. partire, andarsene ME go away, depart Pol. odejsé Fr. partir, sortir, s’en NE go away, depart, leave Russ. vyilt | aller Du. weggaan, verlrekken Skt. apagam- Sp. partir, salir, irse OHG wazgangan, argangan Av. apajam- Rum. pleca MHG izgan Ir. immthigim NHG _ weg-(fort-)gehen | Nir. — imthigim W. ymadael Br. mont kurt | ‘Depart’ is simply to ‘go away’ and is most commonly so expressed (NE depart is mostly in literary us
=== possible printed 470, leaf 1127
t, white’ (15.64), Skt. hari- ‘tawny, yel- low’, OE geolo, OHG gelo ‘yellow’, etc. (15.69). Walde-P. 1.624 ff. Falk-Torp 328 f. | 7. Lith. Sviesti, ChSl. svétiti, general Slavic (in part refl.) : ChSl. svété ‘light’, Skt. cveta-, Av. spaéta-, Goth. hweits ‘white’, etc. (15.64). Walde-P. 1.470. | Lith. Zibéti (Lett. zibét ‘lighten, glim- mer’) : Lith. Ziebti ‘light a fire’, Zaibas ‘lightning’, Lett. zib¢ ‘glimmer’, outside connections dub. Miuihl.-Endz. 4.718. | Lith. spindéti, Lett. spidét, spist (Lith. spjsti ‘begin to shine’), perh. (se- mantic development similar to that in It. brillare) : Skt. spand- ‘throb, palpi- tate, quiver’. Walde-P. 2.664. Miihl.- Endz. 3.1001. | CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar | Digitized by Arya Samaj Foundation Chennai and eGangotri | 1048 SELECTED INDO-EUROPEAN SYNONYMS | 8. ChSIl. svétiti, above, 7. | ChSl. bltstatz, etc., general Slavic : Lith
```


## [2026-09-07T01:39:39.594Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -E \"(^| )4(69|70|71) (SELECTED|[A-Z]{3,})\" SYN.txt | head\necho \"---- alt: heads with 470 ----\"\ngrep -n -E \"[A-Z]{4,},? 470|470 [A-Z]{4,}\" SYN.txt | head"
}
```


### [2026-09-07T01:39:40.898Z] TOOL RESULT

```
---- alt: heads with 470 ----
```


## [2026-09-07T01:39:46.416Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\npages=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(pages))\nfor i in range(538,556):\n    m=re.findall(r'\\b(4[0-9]{2})\\b', pages[i][:300])\n    head=pages[i][:120].replace('\\n',' ')\n    print(i, m[:4], '|', head)\nEOF"
}
```


### [2026-09-07T01:39:47.626Z] TOOL RESULT

```
1545
538 [] |  noun of the vb. farm. NED s.v. G Du. landbouwer, cpd. of land ‘land’ ey and bouwer fr. bouwen ‘dwell, cultivate’. a OHG
539 [] | ‘plain’ (1.23). But sev- eral of the words entered here cover both notions, and in such cases reference is made to the p
540 ['419', '491'] | ), prob. : OHG sal ‘dwelling, hall’, ON salr ‘hall, room’, Lat. solum ‘bottom, soil’, etc. (but in Slavic partly mixed w
541 ['461'] |  ‘garden’ (by contraction, cf. MCorn. lowarth id., Pedersen 1.116), prob. also OE geard ‘yard’ (7.15), OHG garto ‘garden
542 [] | riv. gradina ‘garden’ (> Rum. grdd- ind). Berneker 330. Russ. sad (Pol. sad ‘orchard’, Boh. sad ‘park, orchard, plantati
543 ['461'] | lso ‘barn’ (Hes.). ? 2. Lat. horreum, etym.? Ernout-M, 461. Walde-H. 1.659 f. Lat. granarium (> It. granaio, Sp, granero
544 [] | s easy. 5. Lith. darziné, fem. of adj. darzinis ‘pertaining to a garden’, deriv. of darzas ‘garden’ (8.13), hence orig. 
545 [] | labor ‘labor, toil’ (9.12). REW 4810. 3. Ir. airim ‘plow’ (8.21), also in wider sense ‘cultivate’. Hessen s.v. NI. oibri
546 [] | � orati; plug arate, solearé; OE erian; sulh Boh. orali; pluk JaboureTs charrue ME ere; plogh Pol. oraé; plug arar; araa
547 ['442'] | th. pligas, Russ. plug, etc.). Origin much disputed and quite uncertain. Walde-P. 1.812. Falk-Torp 838. Schra- der, Real
548 [] |  CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar 1. Grk. addat, fr. *&pAax- (beside *arodx-, *a¢hox-in Hom.
549 [] |  sapd ‘hoe’, MLat. sappa (8.25). 3. Ir. claidim (NIr. claidhim ‘ex- cavate’, W. claddu ‘bury’, old ‘dig’; now for ‘dig’ 
550 [] | the same word. sometimes exp (that this was properly a 1, Grk. a a ‘shovel’ is indicated ‘spade’ Be at 76 epyadetov ev @
551 [] | t’ ‘tread on’ (secondarily ‘replace’), cpd. of stupit’ ‘tread, step’ (ChSI. stqpitz), applied to the spade with referenc
552 ['428'] | .428. Berneker 733. 6. Skt. khanitra- ‘spade’ or ‘shovel’; see 8.23. ul Kangri Collection, Haridwar i ee ee ee ee ee ume
553 [] | Pokorny, Z. sl. Ph. 5.393 f. Walde-P. 2.229 (but taking OE mattoc as Gmc. cognate). Walde-H. 2.49. OHG houwa (>Fr. houe 
554 [] | vily (all pl.) ; ChSl. viti ‘wind, twist’, véja ‘branch’, etc. Briickner 613: 7. There seem to be no Skt. or AV- referen
555 ['404'] | H. 1.404 f. Grk. étiva (Hesych.); Lat. occa; W. oged, og, Br. oged; OE egebe, OHG egida, MHG eg(e)de (later ege, NHG egg
```


## [2026-09-07T01:39:56.089Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\npages=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(pages):\n    m=re.search(r'(\\d{2,4})\\s+SELECTED INDO-EUROPEAN SYNONYMS', p)\n    if m and 440 <= int(m.group(1)) <= 500:\n        print(i, m.group(1))\nEOF"
}
```


### [2026-09-07T01:39:58.305Z] TOOL RESULT

```
492 444
495 446
500 452
502 454
508 460
521 472
525 476
528 478
530 480
532 482
534 484
538 488
542 492
544 494
546 496
```


## [2026-09-07T01:40:01.500Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\npages=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(516,522):\n    print('=== leaf',i)\n    print(pages[i][:700].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-07T01:40:02.897Z] TOOL RESULT

```
=== leaf 516
te, Sp. puerla, ‘door’ and ‘gate’; as ‘gate’ Rum. poartd, W. porth, OE, Dan., Sw. port, MLG porte, Du. poort, OHG pforta, MHG, NHG pforte. | Lat. dstium ‘door, entrance’ : Lat. 6s, Skt. ds- ‘mouth’ (4.24). Hence VLat. astium, It. uscio, Rum. usd, OF r. | CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar | ee | Digitized by Arya Samaj Foundation Chennai and eGangotri | SELECTED INDO-EUROPEAN SYNONYMS | huis ‘door’ (Fr. @ huis clos ‘with Closed doors, secretly’). Walde-P. 1.168. Tr. nout-M. 716f. REW 6117. | Lat. idnua ‘door, entrance’ : Skt, yana- ‘going, course’, yd- ‘go’, IR *yq- beside *e7-‘go’. Walde-P. 1.104. Walde-H. 1,669. Ernout-M. 469 (adversely), | 4. Ir. comla ‘door, shutter’, Nir. comhl
=== leaf 517
HG sloz v NHG -schloss | d Br, _krogen-ale’houez, potaith | In the primitive method of fastening a door, still familiar in a farmer’s barn or a rude cabin, the wooden bar and catch represent the ‘lock’, while the ‘key’ is the wooden peg which serves to release the bar. Or the bar may be se- he bya peg driven through it, and in o a the ‘key’ is a kind of hook used a pling out the peg (Grk. Badavaypa). ean 2.325 f. and, for the Greek Mints a, oar Diels, Antike- eae fe ‘Sabet of the words and the most vid ee under ‘Key? tet read Broun listed ‘hail’, or ‘hook? ape ates meaning ‘peg’, Such g ttinttive s Bene tpblied to forms of ¢ i : ype of ‘key’, Some ‘lock’, Atter group are used for | L. Grk | * HOXNs 
=== leaf 518
 Sw. lds, perh., as orig. a metal plate used as a bolt, fr. Gmc. *lamsa- : ON lamar ‘hinges’, Lat. lammina ‘thin metal plate’, etc. Walde- P. 2.385. Falk-Torp 614. Adversely Walde-H. 1.755. | ON loka (lok ‘cover, lid’), OF loc, ME | 1. IE *klau-, klawi-, denoting the wooden peg which was the primitive ‘key’, cognate with words meaning ‘peg’ or ‘nail’ as Lat. clavus, Ir. clo, and with verbs meaning ‘hook’ as Lith. kliutt, or ‘shut’ as Lat. claudere. Walde-P. I, | CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar | SELECTED INDO-EUROPEAN SYNONYMS | loke, NE lock : Goth. galukan, ON litka OE lican ‘shut, fasten, lock’ (12.25), NED s.v. lock sb.?. | OE clistor, fr. Lat. (above, 2). | Du. slot, OHG s
=== leaf 519
lso Lett. atsléga ‘lock’ or ‘key’, also distinguished as atslégas mate ‘lock’, atslégas berns ‘key’ (lit. ‘mother’ or ‘child’ of the atsléga). Mithl.-Endz. 1.193, 3.927, 928. | 1128. Morris Jones 151 (cf. Loth, 5. Skt.  kufcikd-: kufic- ‘make RC 36.178 f.). crooked’. 7.25 WINDOW Grk. — Oupls Goth. augadauré Lith. langas NG xapé0upo, zapadbpr ON vindauga, gluggr Lett. luogs a fenestra Dan.  vindue ChSl. okno : fenestra Sw. _ fénster SCr.  prozor, pendzer Sp ela OE éagduru, éagpyrel Boh.  okno Rum ventana ME windowe, fenestre, Pol. okno ie ag (geam) eythurl Russ. okno Mh feck a Suindedc NE teow Skt. ma gavakgsa-, + Senesir d oe Br OHG  venstar, augatora Av. raocana- Prenesl(r) MHG venster NHG  f
=== leaf 520
boden (diele, es- | trich) | CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar | SELECTED INDO-EUROPEAN SYNONYMS | lit. ‘wind-eye’, cpd. of the words for ‘wind’ and ‘eye’. Falk-Torp 1383. ON gluggr (Sw. glugg ‘hole, opening’) fr. Gme. *gli- beside glo- in ON gléa, OE glowan ‘glow’, hence orig. ‘opening for light’ (cf. ON Wore ‘opening in the roof’ : js ‘light’). Walde-P. 1.627, Hellquist 288. 5. Lith. langas, Lett. lwogs, OPruss, lanxto, etym.? Possibly orig. a Swinging window and so: Lith. linguoti ‘swing back and forth’ (Leskien, Ablaut 334 with?). Late ChSI. okno, etc., general Slavic (but SCr. okno ‘window pane’) : ChSI. oko, Lith. akis ‘eye’, etc. Walde-P. 1.171. Brickner 377. SCr. pr
=== leaf 521
t. astracum ‘floor’, this fr. Grk. dorpaxov ‘potsherd’. Kluge-G. 140. REW 6118. | NHG boden ‘bottom, ground’ (12.34), commonly used for ‘floor’ where the con- text or situation makes this sense clear, or more specifically fussboden. | OHG arin, MHG ern, fr. Lat. aréna. Walde-P. 1.79. | For the distribution of NHG (fuss)- boden and diele, cf. Kretschmer, Wort- geogr. 174 f. | 5. Lith. asla, etym.? (connection with L. area or OHG asirih, BB 16.207, un- likely). | Lett. grida : Lith. grinda ‘board’, pl. grindos ‘flooring, wooden floor’, SCr. greda ‘beam’, ON grind ‘lattice work’, etc. Walde-P. 1.657. Berneker 348 f. | 6. SCr. pod: ChSl. podi ‘bottom, floor’ (rare), Russ. pod ‘bottom’, Lith. podas ‘sole of
```


## [2026-09-07T01:40:10.823Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"raocana\\|rocan\\|rauzan\\|rozan\" SYN.txt | head\necho \"=== full leaf 520 tail ===\"\npython3 -c \"\npages=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(pages[520][:2000])\" | grep -n -i \"av\\.\\|raoc\" "
}
```


### [2026-09-07T01:40:12.197Z] TOOL RESULT

```
8628:K: COOKING AND UTENSILS 341 FooD 5.26 POT Lith. puodas Gothia). ON gryla, poltr Lett. puods Grk. EN Dan. gryde, polle ChSl.  griintct NG mull, alla Sw.  gryla SCr. —_ lonac, grnac Lat. pentola _ OE crocca, polt Boh: nek ne It. armile 5 ite ol.  garne fr. me ‘ole puchero _ Hi Russ. gorSok Sp. oald Du. pot Skt.  kumbha-, ukha-, iene crocan OHG hafan sthali- ) ov corcan MHG haven, topf Av. zumba-, dista- fe NHG topf Bree ee t : 3 Grk. xbrea, fr. the root of Grk. xéw NHG dial. pott), perh. fr. Gme. *putta-, if 35) IE *budno-, and related to numerous J . . jules Ge N, dim. of rootxa, fr. It. | words having the notion of ‘swell up’
8637:‘ Pe crocan, NIr. corcan * OE croceq (belo Keltorom. 97,
11811:1128. Morris Jones 151 (cf. Loth, 5. Skt.  kufcikd-: kufic- ‘make RC 36.178 f.). crooked’. 7.25 WINDOW Grk. — Oupls Goth. augadauré Lith. langas NG xapé0upo, zapadbpr ON vindauga, gluggr Lett. luogs a fenestra Dan.  vindue ChSl. okno : fenestra Sw. _ fénster SCr.  prozor, pendzer Sp ela OE éagduru, éagpyrel Boh.  okno Rum ventana ME windowe, fenestre, Pol. okno ie ag (geam) eythurl Russ. okno Mh feck a Suindedc NE teow Skt. ma gavakgsa-, + Senesir d oe Br OHG  venstar, augatora Av. raocana- Prenesl(r) MHG venster NHG  fenster
11841:lit. ‘wind-eye’, cpd. of the words for ‘wind’ and ‘eye’. Falk-Torp 1383. ON gluggr (Sw. glugg ‘hole, opening’) fr. Gme. *gli- beside glo- in ON gléa, OE glowan ‘glow’, hence orig. ‘opening for light’ (cf. ON Wore ‘opening in the roof’ : js ‘light’). Walde-P. 1.627, Hellquist 288. 5. Lith. langas, Lett. lwogs, OPruss, lanxto, etym.? Possibly orig. a Swinging window and so: Lith. linguoti ‘swing back and forth’ (Leskien, Ablaut 334 with?). Late ChSI. okno, etc., general Slavic (but SCr. okno ‘window pane’) : ChSI. oko, Lith. akis ‘eye’, etc. Walde-P. 1.171. Brickner 377. SCr. prozor, fr. through’. SCr. pendzer, fr. Turk. pencere ‘win- dow’. Lokotsch 1648. 6. Skt. vatdyana-, lit. ‘wind-passage’, epd. of vata- ‘wind’ and ayana- ‘going, course’. Skt. gavaksa-, lit. ‘ox-eye’ (cf. NE bull’s-eye), epd. of gava- ‘ox’ and aksa- ‘eye’. Also grhaksa- (rare) lit. ‘house- eye’. Skt. jala- ‘net’, also ‘lattice-work win- dow’. Av. raotana- (NPers. rozan) : Skt. rocana- ‘bright’, locana- ‘eye’, etc. Barth. 1489.
12167:3. Br. kreuzeul fr. OF r. croisel ‘ lamp’, this ultimately fr. g Celt. word for ‘earthenware pot’ (OF MIr. crocan, etc., 5.26). Gamillscheg 277.
13293:8.58 ROSE Ab5ov Goth. .... Lith. rozeé tptavTagvAdo ON rds, rosa Lett. ruoze rosa Dan. rose Ch&l. Bee rosa Sw. TOS SCr. ruza rose OE rose Boh. _rtiZe . ‘rosa ME rose Pol. roza . trandafir NE Tose Russ. roza, rozan ros Du. 700s Skt. (japa-, odra) TOs OHG rosa Av. varaéa-(?) thosyn MHG rose rozenn NHG rose
=== full leaf 520 tail ===
5:lit. ‘wind-eye’, cpd. of the words for ‘wind’ and ‘eye’. Falk-Torp 1383. ON gluggr (Sw. glugg ‘hole, opening’) fr. Gme. *gli- beside glo- in ON gléa, OE glowan ‘glow’, hence orig. ‘opening for light’ (cf. ON Wore ‘opening in the roof’ : js ‘light’). Walde-P. 1.627, Hellquist 288. 5. Lith. langas, Lett. lwogs, OPruss, lanxto, etym.? Possibly orig. a Swinging window and so: Lith. linguoti ‘swing back and forth’ (Leskien, Ablaut 334 with?). Late ChSI. okno, etc., general Slavic (but SCr. okno ‘window pane’) : ChSI. oko, Lith. akis ‘eye’, etc. Walde-P. 1.171. Brickner 377. SCr. prozor, fr. through’. SCr. pendzer, fr. Turk. pencere ‘win- dow’. Lokotsch 1648. 6. Skt. vatdyana-, lit. ‘wind-passage’, epd. of vata- ‘wind’ and ayana- ‘going, course’. Skt. gavaksa-, lit. ‘ox-eye’ (cf. NE bull’s-eye), epd. of gava- ‘ox’ and aksa- ‘eye’. Also grhaksa- (rare) lit. ‘house- eye’. Skt. jala- ‘net’, also ‘lattice-work win- dow’. Av. raotana- (NPers. rozan) : Skt. rocana- ‘bright’, locana- ‘eye’, etc. Barth. 1489.
```


## [2026-09-07T01:40:18.990Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM grep رزق ===\"; grep -n \"رزق\" AFM.txt | head -20\necho \"=== AFM leaf 80 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==81' AFM_pages.txt | head -60"
}
```


## [2026-09-07T01:40:20.070Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA\ngrep -n \"rizq\\|Rizq\\|رزق\" PLA_pages.txt | head -20\necho \"=== page tag search ===\"; grep -n \"\\[pdf page 13[0-9]\\]\" PLA_pages.txt | head"
}
```


### [2026-09-07T01:40:20.191Z] TOOL RESULT

```
=== AFM grep رزق ===
1326:» ( البيت ) القوت مشتق من ناد ومعناه المال والرزق 
2560:والكردى درزق 
2972:وقالت فيه العرب رزق وارتزق الى غير ذلك 
=== AFM leaf 80 ===
⁄ܤ _- 4 =
03 ܝ وام الاب ܝܐ فقول 14 ارال 16 ١‏ الاي ( 0 55 )|
3710 3 ܘ( § الدين والعينة معرب 9 ذهب 5
# ( ال راوندك) فارسى ܝ وهو 0 = 3 2 9
+¥ (ازّري) من الناس الدع الذى لا بعد ايا 3 رارك وهو تناه
وقالوا 7 ܝ @ 9 £ 1 عليه
ܟ ) 7 890 وهنا تمن
٠ 7‏ الغليل ٠الزلابية‏ قيل هي 3 عر
أورودها £ رجز قدي ٠‏ ܐܝܝ وهر 0 قا عن أ( لها وهو عحين يقل بالشمن ثم د
بالدس ومنة ܙܠܘܒܝܐ بالسر 0 الدارجة وزاميه 22
+ )10 ) ماء زلال ܒ ‫ ا مرور £ الحلق يارد عدب 32 زلال وهو
دودة تتكون في الثلج المركزم لك ܝ دقيقة سضاء اذا 3 ܐܬ ܀ .ܟܝܐ 4
باردًا عذب فيال لذلك الماء بالفارسمّة « آب زلال» اي ماء زلال ( البيهان القاطع)
ܕܘܚ 4 09:0 بالكردنة
021 تعريب زياو وهو =
+ 93 الى 2 مأخوذ من ذَ مرّم وهو 1 نكم الدى :10:05
ܝ £ ܨ ܗܝ 3 7 وي 1 ܝ زهو عمارة عن ܩܕ ܕܢܕ :21 £
خياسشيمهم 3 وهم < لا ܠܚ ܬܘܐ ܕܐ 013 3:5 كن ينهم فهم بعضهم .ܨ
بعض ٠‏ واصل معقى معى ܝܐ | ® .ܠܡ رويدا
+ ܫ 7 ليرد ܝ 59 من زم 3 برد ومن تمر براي موجب وقالوا
فها 4 ܓ اي 1
( الزُمأوَرد) طعام من البيض واللحم ٠‏ وقول العامّة بزماورد اصوب لان <
56
ܡܣ مأخوذ من 0000)0&203 04000
+« (|3 ܨ تعريب ذَ نيد وهو الثقيل م ن الرجال
+ ل نري ) تعريب 7 ܠܢ وهو ضرب من السفن ضخم
```


### [2026-09-07T01:40:20.244Z] TOOL RESULT

```
975:GlL,1- ’arzäg:                                     Pl. v. rizqQa.                                    v.
7544:ol     -    räzig:              act.        pt.     v.    rizq        s.    rizq.
7698:ol,       -       razzag:          "Ernährer"                 nom,        agent.       Ve,     rizq    s.    rizg.
=== page tag search ===
```


## [2026-09-07T01:40:25.571Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA\ngrep -n -i \"rizq\\|rizg\\|rozig\\|rozik\\|rōzīg\" PLA_pages.txt | head -30\necho \"=== context of main entry ===\"\ngrep -n -iE \"^.{0,40}rizq\" PLA_pages.txt | head -20"
}
```


### [2026-09-07T01:40:26.856Z] TOOL RESULT

```
422:           pers.     8 >      ar.          z. B.:        pers.     ruzic mp. zuzig >> ar. rizg
455:           pers.      y _>ar. g:               pers.     ui      —T mp. rüzig —> ar.                       rizg,    mp.    sadyik>
975:GlL,1- ’arzäg:                                     Pl. v. rizqQa.                                    v.
7544:ol     -    räzig:              act.        pt.     v.    rizq        s.    rizq.
7698:ol,       -       razzag:          "Ernährer"                 nom,        agent.       Ve,     rizq    s.    rizg.
7711:au -          rizg:      "tägliche                     Nahrung"                 pers. cs,       rüzi    m.»e»               röcik     "daily
7712:          bread"         6 aw.                        raocah       / ap.        rauca       "Tag",    syr.     PEN      7     mand.        rizga   8,
=== context of main entry ===
```


## [2026-09-07T01:40:33.842Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA\nsed -n '7700,7725p' PLA_pages.txt\necho \"=== page markers near ===\"\nawk 'NR<7715 && /page|\\[pdf/' PLA_pages.txt | tail -5\ngrep -n -c \"\" PLA_pages.txt\npython3 - <<'EOF'\nt=open('PLA_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('npages',len(pages))\nfor i,p in enumerate(pages):\n    if 'tägliche' in p and 'rizg' in p:\n        print('leaf',i)\n        print(p[:1200])\nEOF"
}
```


### [2026-09-07T01:40:35.136Z] TOOL RESULT

```
el, - razzägi:                          "Weintrauben;                     Wein"
                                                                              — pers.), raz                   "a vineyard"            2 mp.
              ‚„, zaz    "vine,                  vineyard'"          3,


OLl,,-             razbän:           "Gärtner"                s.     ra2.

u         -       razdaq:          "Reihe"                    pers.a,.,            Faste      4       MP. se         rastak    m.            rah   °.


au -          rizg:      "tägliche                     Nahrung"                 pers. cs,       rüzi    m.»e»               röcik     "daily
          bread"         6 aw.                        raocah       / ap.        rauca       "Tag",    syr.     PEN      7     mand.        rizga   8,


0) -          razza:         "Fischband"                   pers.           9,


ol, - rasätig:                          Pl. v.öliu, rustäg.

ol,           -    rustäqg:          "Marktflecken"                    =    ruzdägq,        mand.     rustag,    syr.$%’awro)          ,
                      »               10
          (p.        IL,       )             .



=== page markers near ===
16027
npages 302
leaf 149
ruzdäg                                                                          135                                                   rusdäg



ol         - ruzdäg: "Marktflecken" <T pers. L, rüstä                                                       1 m.        yw»»>         rostäk,
          rötstäk, ar. Lw. öl), ruzdäg u. Sl, rustäg.
     w
ol,       -       razzag:          "Ernährer"                 nom,        agent.       Ve,     rizq    s.    rizg.


el, - razzägi:                          "Weintrauben;                     Wein"
                                                                              — pers.), raz                   "a vineyard"            2 mp.
              ‚„, zaz    "vine,                  vineyard'"          3,


OLl,,-             razbän:           "Gärtner"                s.     ra2.

u         -       razdaq:          "Reihe"                    pers.a,.,            Faste      4       MP. se         rastak    m.            rah   °.


au -          rizg:      "tägliche                     Nahrung"                 pers. cs,       rüzi    m.»e»               röcik     "daily
          bread"         6 aw.                        raocah       / ap.
```


## [2026-09-07T01:40:43.217Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2965,2980p' AFM.txt\necho \"=== find leaf in AFM_pages containing that ===\"\npython3 - <<'EOF'\npages=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('n',len(pages))\nfor i,p in enumerate(pages):\n    if 'وارتزق' in p or 'ارتزق' in p:\n        print('leaf',i)\n        print(p[:1500])\nEOF"
}
```


### [2026-09-07T01:40:44.465Z] TOOL RESULT

```
وأرذغت وارتدغ الرجل 


لالط 77 ܓ 


¥ (الرِزق) تعر يبب روزي وما يمعنى واصل. روزى نسبة الى روز وهو النهار. 
وقالت فيه العرب رزق وارتزق الى غير ذلك 

(الرازق ) السب املاحي 390 6 ( والخمر: 
ܝܚܪ من رازى وهو لتو 0( ܒ ( راجع ܫܝܐ 1 >( ٠ورازقي‏ 
بالفارسيّة يطاق ايضاً على العنب الملاحي ܕܟ وقال في البرهان القاطع :« زتموا ان 
ܣܨ ܝ سم احده 09 00 الاننو راز 930 هذه المدئة (اى ܘܙ 4 الري ٠)»‏ ولا 
مت اراد كل” منها 0 ܓ ܨ بأسمه 3 من جراء ذلك 2 ܚܠ ܙܠ ܝ ٠فاشّار‏ 
اليهها احد |( ْ ܣܨ 11 ܐܝ ܐܢ )| ܙܠ ܧ 3 ܐ الاخر. ند 
ܣܣ 93 ثما رازيين > 
=== find leaf in AFM_pages containing that ===
n 198
leaf 73
لالط 77 ܓ
¥ (الرِزق) تعر يبب روزي وما يمعنى واصل. روزى نسبة الى روز وهو النهار.
وقالت فيه العرب رزق وارتزق الى غير ذلك
(الرازق ) السب املاحي 390 6 ( والخمر:
ܝܚܪ من رازى وهو لتو 0( ܒ ( راجع ܫܝܐ 1 >( ٠ورازقي‏
بالفارسيّة يطاق ايضاً على العنب الملاحي ܕܟ وقال في البرهان القاطع :« زتموا ان
ܣܨ ܝ سم احده 09 00 الاننو راز 930 هذه المدئة (اى ܘܙ 4 الري ٠)»‏ ولا
مت اراد كل” منها 0 ܓ ܨ بأسمه 3 من جراء ذلك 2 ܚܠ ܙܠ ܝ ٠فاشّار‏
اليهها احد |( ْ ܣܨ 11 ܐܝ ܐܢ )| ܙܠ ܧ 3 ܐ الاخر. ند
ܣܣ 93 ثما رازيين >
( الروزنة ) تعريب روزنه وهي الكوة ٠‏ والكوة نفسها ارامسة ܟܘܬܐ ( راجع
ܢܬܐ ص 1١:‏ )
+ رن ) فير بجر ضَلت تعد 22 4 ܐܢܟ معرب ارزن وهو ܡܨ
ܐܝܬ ܠܚܡ اللوز ܐ ܨ 11 05 ܐ الادوية وتتخذ من اغصانه
العمي ܢ 9 5 ܐ محان 30 هن سيراز دكثر فيه هذا
الجر
3 ن)) العسن ونات يفرش اوراقة على الارض دهي طويلة تبلغ الورقة منها
الى ط ول ذراع 2 :|© :10 في ܦܐ القاطع : 037 على وزن دامن يقال
9 اصله طيب الرائحة لونة بين الممرة وااضرة زهره مائل الى اردق
وبزده ܒܥܬ بيزر العصفر وهو عر يض قليلا وطعمة حاذ والْستّعمل ܐܩܝܐ ّ ويستى ܐܐ
بالعريية ܝ 5057( منشمس ورقة عريض:وطو يل
ويقال لبه حب الراسن ولاصله | الراسن »
( الرسن) اليل 3 97 6 ايضاً ٠‏ وفرتكل يقول اله مأخوذ من
80 المثتق هو 0 من 0.77 ܐ (ص: - › \ ) !ܙ ܬ مشتق من
ريسيدن ومعناء غزل ايضاً او من رسن اي المورصل
الرشحة 325:0 ) شرا عه وهو ܟܐܝܐ تعمل من العدس كلتق 3 قدت من ترقاك
العجين واصل ܘܫ رشته بالفارسيّة ܐܝܐ
```


## [2026-09-07T01:40:54.049Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\npages=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(66,82):\n    nums=re.findall(r'(?<!\\d)(\\d{2,3})(?!\\d)', pages[i])\n    print(i, nums[:8], '|', pages[i].strip()[:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T01:40:56.277Z] TOOL RESULT

```
66 ['07', '11', '130', '11', '15', '31', '06', '36'] | ܝ والإنعام والإحسان.ومنة مأخوذ دَسْنَ اي < وتَدَدَُنَ اي ` ا
67 ['43', '37', '277', '01', '30', '20', '07', '003'] | اي قلب :43 م اي أعوج 6 ܨ به مشل دول معنى وقريب منهُ © والظاه
68 ['11', '05', '95', '١٠', '15', '52', '39', '179'] | اك ܬ0007.2 11 تعر ينب 1111111115 0 (الدانق ) 1 ܐܕ والسارق ܠ 
69 ['00', '201', '59', '13', '06', '33', '15'] | ܫܝ * (الدهدار) الباطل مركب من داه اي دناءة ومن دار اي صاحب #
70 ['15', '50', '20', '58', '36', '810', '500', '73'] | ܚܐ 4 ܝܝ اد بعون 3505 ± الثالي * (الدوكة ) الشر والخصومة 1020
71 ['50', '10', '83', '57'] | اه ܐ ® صمغ الصنو بر 5 لغة فيه ٠‏ وهو داتبانج الفارسية ٠‏ قال
72 ['09', '60', '10', '99', '89', '369', '89', '40'] | سند لو ”ا ܵܣ علاوة 2 رماس ومنه السريالى. ܪܝܒܣܐ والكردي رياس 
73 ['77', '390', '09', '00', '930', '11', '93', '1١'] | لالط 77 ܓ ¥ (الرِزق) تعر يبب روزي وما يمعنى واصل. روزى نسبة 
74 ['04', '02', '39', '109', '12', '30', '57'] | 3 ܣ * (الرشك» اكبيد اللحية معرب من ريشكاو: اي بليسة الثور 9 
75 ['280', '07', '309', '441', '17'] | و شرب ܛ النردين وهو ܝܐ الرومى. اليه عن ܐܐܐܠ 002200 او )280 و
76 ['00', '00', '34', '111', '00', '07', '11', '03'] | بق اي ذر را 0 ١‏ ريس ليوا موت ونم وهو منسرب الى بر ` (171015
77 ['21', '000', '00', '99', '975', '135', '101', '81'] | 21 1 (الزنيق) سيال معدني معروف معرب ܨܘ ومنة السريائي ܙܢܒܓ + 
78 ['973', '501', '60', '67', '15', '55', '07', '01'] | ܚ ܝ = ( "5 5 وهو 973 6 المشتري ܥ 9 فأخوذة ܟ عن ܟ ياف ܙܒܘܢܐ (
79 ['351', '65', '95', '05', '32', '50', '09', '40'] | ܓ ( ;3 ) 3 با لعصفر تعر يبب 1ك وهو ماء العصفر (الرَردَمَة ور
80 ['03', '14', '16', '55', '890', '22', '10', '32'] | ⁄ܤ _- 4 = 03 ܝ وام الاب ܝܐ فقول 14 ارال 16 ١‏ الاي ( 0 55 )|
81 ['90', '21', '01', '20', '00', '00', '111', '003'] | ܣܐ ), °^ ( | ; 90 ܚܐ تورك وهى آلة من )4411 ܛ )7 + £ له زهر 2
```


## [2026-09-07T01:41:13.407Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD rwxsn ===\"; grep -n -i \"rwxšn\\|rwxsn\\|rwxsn'\\|rwxsny\" SOD.txt | head -20\necho \"=== SOD world ===\"; grep -n -iE \"\\bdwk|dwq|dwk'\" SOD.txt | head -20\necho \"=== SOD entries 146 / 345 ===\"; grep -n -E \"^ *(146|345) \" SOD.txt | head"
}
```


### [2026-09-07T01:41:13.489Z] TOOL RESULT

```
=== SOD rwxsn ===
65007:-w   =»rwysn,  rwxsn-,  >pw  rywsny'kh 
65022:r(u)xusna-yar5manclk   ^rwxsn'yrSmncyk 
65029:r(u)xusnyak   (rwysny*k)   ^rwxsny^, 
65625:=»rwxsn)Yr8mn,  rywsn^rSmn 
65632:roxsntar   ©-y  =*rwxsndr 
65639:roxsnyak   (rwYsny*k)  ^rwxsny'k 
65847:8604  rwxsn-   M,  C  j^3J  i^3J 
65861:8605  rwxsn)yr8mn   M  ,-.*g, 
65870:8606  rwxsnVSmncyk   M  j^> 
65876:8607  rwxsndr   M  y^jj 
65882:8608  rwxsny>())q  =»  rwxsny'k 
65884:8609  rwxsny'k   M,  C  ^3J 
65885:roxsnyak   (rwxsny>())q)   ©ob.  -y;  pi.  -f 
65897:8610  rwxsny^y*   C  jll^jh^3j 
65976:r(u)xusn   ©nom.  ob.  -ny\  abl.  -«*   =»rwxsn- 
65981:8622  rxwsntr    S  =>  rwxsndr 
65986:rwxsny}k 
78701:wiroxs   (wyryws-)  ©Parth.  wrwxsn 
=== SOD world ===
31946:Frag.  Len.  32.11;  dwkyh  Dhy.  399 
31970:Swkh  prdwkK  TSP  2.503;  dwky  prSwky,  TSP 
34270:4045  YJdwq    C  =>  Y^wk(>) 
34273:Ya9uk   (Y^wq,  ^dwq)   ©<*gd&uka   ©ob. -yfyj 
=== SOD entries 146 / 345 ===
8493:146  »kwyt-   B  j^_f\ 
9737:345  »y'pt-    B  j^^y^ol/ 
31949:146 
65565:345
```


## [2026-09-07T01:41:25.408Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"'world'\\|world'\" SOD.txt | head -40"
}
```


### [2026-09-07T01:41:25.458Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T01:41:28.084Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"world\" SOD.txt | head -40"
}
```


### [2026-09-07T01:41:28.136Z] TOOL RESULT

```
4118:information  about  the  western  world  and  the  rich 
5790:/{Jum/         fiwm  world         OP  bumi 
10454:worldly 
10464:world 
10474:Lord  of  the  World 
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
```


## [2026-09-07T01:41:33.632Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- 65655-65680 ---\"; sed -n '65655,65680p' SOD.txt\necho \"--- 31930-31990 ---\"; sed -n '31930,31990p' SOD.txt"
}
```


### [2026-09-07T01:41:33.699Z] TOOL RESULT

```
--- 65655-65680 ---


J*}\ 


j>  j->. 


~*)tM$  ij^r 


r/lok   ©<Skt.  loka   =»5wk> 
loka,  world 


TSP  2.1193,  7.26,  8.39,  29;  BSTBL,  Padm.  52,  61 
pl30 

8577  rwke'tCh)  =»  rwk 

8578  rwkSyspr*  =*  rwk 

8579  rwkp'r  =*  rwk 

8580  rwp—   B,  C  o^,jj  <c*3j  i o^>-  <o-^^ 
rop  ©fraup\  Pahl.  rob 
--- 31930-31990 ---

3687  6wYth  -*  8wYSr 

3688  6wYtrt(h)   M  jl^* 
6uYdart   ©ob.  pi.  -fy   =*8wYSr,  8wYt(>) 
daughters 

Hen.  Talcs.  486,  6,  7,  10;  GMS  1231 

3689  5wk}   B  Uwot^ 
8oka,  loka   ©Skt.  loka  ©nom.  ->;  ob.  -y(h) 

~*rwk 
world 
SCE;  BSTBL,  Dhu.  161;  TSP  2.576,  8.85;  SwkK 

Frag.  Len.  32.11;  dwkyh  Dhy.  399 


146 


3690  5wk}  pr6wk>  B 


A> 


ts^J 


iiw*  jl 


8oka-par8oka  (Swk  prSwk)  ©Skt. 

loka-paraloka 
from  this  word  to  another 
BSTBL,  lntox.  20;  TSP  2.42-3,  1146-7,  1198,  10.9; 

Swkh  prdwkK  TSP  2.503;  dwky  prSwky,  TSP 

2.28;  <5wky  prSwk'cyk,  TSP  2.1079 


3691  8wk'yck>  B 
5/Iokick 
worldly 
BSTBL,  Dhu.  270(N) 

3692  Swkcyk   B 
Sokcik   (5wkcyq) 
worldly 
GMS  1014;  TSP  2.47 

3693  5wkcyq    M  =¥  8wkcyk 

3694  Swk  pr5wk  =$  8wkJ  prSwk* 

3695  5wlyy   M 
8ule?
```


## [2026-09-07T01:41:45.502Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '65840,65900p' SOD.txt"
}
```


### [2026-09-07T01:41:45.563Z] TOOL RESULT

```
8601  rwtc^  =»  rwcyk 

8602  rwtcyk    MD  =*  rwcyk 

8603  rwwt   M  =»  rwt 

8604  rwxsn-   M,  C  j^3J  i^3J 
roxsn   ©nom.  gen.  -y(yk  ace.  -w;  abl.  voc.  -\  pi. 

-t\  -d\  nom.  f.  -*;  ob.  pi.  -ty\  -tyh  =*rwysn, 
rywsn-,  rxwsn- 

luminous,  light 

GMS  40,  127,  520,  1191-9;  BBB  b56,  58  b5,  80, 
97  f  80,  46,  566;  W-Lii  569;  KG  2338;  MSP  c20 
b98  bl21;  C2,  91R  11;  Hen.  BSOAS  12.307.11, 
19;  STii  2.11;  BSTi  165;  Sund.  AoFiii  1975, 
18V17 

8605  rwxsn)yr8mn   M  ,-.*g, 
roxsna-yar8(a)man  ©<Av. 

raoxsna-garoSdmana  ©ob.  -}y,  -y}A 

^rwysn^rSmnCh) 
paradise 
GMS,  1218;  BBB  f85;  BSOAS  12,  307.11;  21,  1221 

8606  rwxsnVSmncyk   M  j^> 
roxsna-yar5mancik   ©pl^   -^rywsn'yrSmncyk 
paradisian 

GMS  1014;  BBB  f48 

8607  rwxsndr   M  y^jj 
roxsndar,  rxusndar  (rxwsntr)  ©nom.  -y 
brighter 

GMS  1284;  KG  366 

8608  rwxsny>())q  =»  rwxsny'k 

8609  rwxsny'k   M,  C  ^3J 
roxsnyak   (rwxsny>())q)   ©ob.  -y;  pi.  -f 

^rywsny'kCh),  rwysnyMcCh) 

brightness  \ 

GMS  1110,  1221;  BBB  485  pl34;  BSOAS  12, 
307.41;  STi  31.12,  65.8,  43.16;  Sund.  AoFviii 
1981  p217;  STii  3.64,  1.27;  C2  gloss.  p224, 
W-Lii  546,  547.25,  548.19,  564,  -A,  MSP  b28 
b97;  CII  1990  p67  G4-5 

8610  rwxsny^y*   C  jll^jh^3j 
roxsnyakya 

brightness
```


## [2026-09-07T01:41:53.554Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=65700 && NR<=65900 && /^ *[0-9]{2,3} *$/ {print NR\": \"$0}' SOD.txt\necho \"--- via SOD_pages.txt: find leaf with 8604 rwxsn ---\"\npython3 - <<'EOF'\npages=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('n',len(pages))\nfor i,p in enumerate(pages):\n    if '8604' in p and 'rwxsn' in p:\n        print('leaf',i,'printed approx',i-66)\n    if '3689' in p and '5wk' in p or ('3689' in p and 'wk' in p):\n        print('dwk leaf',i,'printed approx',i-66)\nEOF"
}
```


### [2026-09-07T01:41:54.907Z] TOOL RESULT

```
--- via SOD_pages.txt: find leaf with 8604 rwxsn ---
n 645
dwk leaf 211 printed approx 145
leaf 413 printed approx 347
```


## [2026-09-07T01:42:03.198Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD roz/rosn/rozig ===\"; grep -n -E \"rō[zc]|rošn|roshn|rwc|rwšn\" PHD.txt | head -30\necho \"=== PHD_mackenzie ===\"; grep -n -E \"rōz|rōšn|rōzīg|rōzan\" PHD_mackenzie.txt | head -30"
}
```


### [2026-09-07T01:42:03.264Z] TOOL RESULT

```
=== PHD roz/rosn/rozig ===
170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
510:~ pazd- : blow, play the flute. *nāydāģ [nywt’k'] deep, unfordable, navigable. nayestàn [KN Y Ast^n! | N ~] reed-bed, cane-brake. nāyīzaģ [»vck! | N ~a] small reed, straw. nay-sray [rds d] flautist. nazd [nzd | = M, N ~] near. nazdik [nzdyk! | = M, N ~] near. ~ih: proximity. nazdist [x3dst'] first. nàzišn [x*cšn! | N nāsi$] 1. boasting; 2. kindness. nàzuk [n’cwk! | (M wzwg), N ~] tender, gentle; fickle. né [L4 < AP | M ny, N na] no, not. nék [nywk! | M nyk, N ~] good, beautiful. ~th: goodness. nék-góhr [nywk gwhl] good-natured, virtuous. ~ih: goodness, virtue. nēkēģ [nywhkwk! | M nyyquiw!, IN neho] == пёк. nem [PRG < А plg; nym | = M, N —] half. ~ag [nymk! | N ~a] half, side, direction. ~-аѕр [5р] centaur; astr. Sagittarius. ~-rōz [-lwe | M -rwe, N ~] midday, south. ~-tan [-tn' | N ~] middle of the body. nérang [nylng | N <] incantation, charm, spell. пёгӧб [nylwk! | M nyrwg, N nero] strength, power. ~omand [-’wmnd] strong, powerful.
559:rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
2621:light (n.) payrēg, rošn(ih).
=== PHD_mackenzie ===
```


## [2026-09-07T01:42:05.868Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN derafs ===\"; grep -n -i \"derafs\\|dirafs\\|drafs\\|drafša\" HRN.txt | head -20\necho \"=== HRN arash ===\"; grep -n -i \"eres\\|erex\\|arash\\|äras\" HRN.txt | head -10\necho \"=== HUB rox/rosn ===\"; grep -n -iE \"raoxs|rösan|rosan|ruxs|rôz|röz\" HUB.txt | head -20"
}
```


### [2026-09-07T01:42:05.958Z] TOOL RESULT

```
=== HRN derafs ===
4971:aw. drafsa- 'Banner -); phlv. draß^ arm. LW. draus;
4980:zitternd', AV. , drafset Bund.); in dieser Bedeutung
5000:Greldner^s Übersetzung von aw. (jaos drafsö (y. 10, 14J durch
14876:drafsa- 558.
=== HRN arash ===
52:dieses Projekt und hilft den Anwendern weiteres Material über Google Buchsuche zu finden. Bitte entfernen Sie das Wasserzeichen nicht.
241:gefunden habe. Weber's ersten PärasTprakä^a des Krsna-
258:indischen Lehnworte in den PärasTprakä9as erscheinen in
287:beweisen scheinen. Wie wenig Sicheres man jedoch aus
308:Brockhaus, p. 8 Zeile 8 v. u.). Als ein weiteres Beispiel
339:;^''ms auf leskeres (35, 18) , reArs auf dehis (60, 505), ^ew^5
855:merezdätä, meresdika-, ai. m^ddti (Bartholomae BB. 13,
890:anderes als m oder in werden können. Zudem kommt
1021:65. ebre^stitn, ebresem *Seide*, beresem,
1072:70. ers 'Elle', eres,
=== HUB rox/rosn ===
2119:Die Vermutung uber die Etym. von np. duruxs ist sehr
2361:Aussprache von roSan giebt Rosen, Np. Sprachf.
6176:b) a eingeschoben in: rosan *heir (Vis u Ramin 103,
6177:21) — zd. raoxsna- ; rdyan 'Butter, Oel' = zd. raoyna- ; dasan ^)
8324:b) inlautend vor Konsonanten: rosan 'hell* zd.
8325:raoxsna- ; dsna 'bekannt* = ap. *axsnaka-'^ phi. dsnak ; astl
8333:= phi. tuxsak (oben p. 47) ; ruxs (raxs) 'Glanz*, vgl. zd.
8334:raoxsna-- glanzend'; vaxsur 'Prophet' H. 1076; daxs 'Ge-
8396:rosfiaJcan Vein, redlich', np. rosan *heir.
9045:schenk, Gabe* (= phi. dcihisn), rosan *heir = zd. raoxsna-,
9652:'Lllnge', pahn-a *Breite*, rOsan-a *Helle' JRAS.
```


## [2026-09-07T01:42:28.598Z] TOOL CALL #39: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T01:42:28.606Z] TOOL RESULT

```


```


## [2026-09-07T01:42:29.046Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4955,5010p' HRN.txt"
}
```


### [2026-09-07T01:42:29.104Z] TOOL RESULT

```
besser drva- + sü- (vergl. aw. ayösti-), wie mir Bar-
tholomae vorschlägt; ap. diiruva- 'gesund'; phlv.
duritst^ durustih; ai. dhncvd- 'fest, bestimmt, bleibend'.
LW. kurd. durust 'wahr'; bei. driist 'voll, ganz,
vollständig' (86); wa/. drust, driist 'ganz, vollständig.
Anders Fr. Müller, WZKM. 5, 66; vergl. aber
unter np. dire/t (No. 548).
552. durust 'rauh, grob, stark, durustt,
ap. iXrfars- 'wagen', adarmans, darsma 'heftig, sehr';
aw. \/dar€S' 'wagen', darsi-; ai. \/dharS', dhfmoii
'J Unter sozen (Öcitc HDJ.— 123 —
Als eine Bestätigung für diese Etymologie dient der
Umstand, dass Herr Prof. Nöldeke mir dieselbe
ebenfalls mitteilte; er war besonders von ai. (Ißtä- in
der Bedeutung *keck, frech' ausgegangen ^).
553. direfS Fahne, Banner'.
aw. drafsa- 'Banner -); phlv. draß^ arm. LW. draus;
ai. drapsd' 'Tropfen*.
oss. LW. (jrisa Tahne (von JStackelberg, Fünf
oss. Erz. 81).
Die ursprüngliche Bedeutung von ar. drapsd- ist
unsicher; Fick, Vorgl. Wörtbch. ^ I, 241, setzt
zweifelnd 'flutend, wallend' als solche an. Np. direfs
soll auch *Blitz, Glanz' bedeuten, vergl. direßän,
direfsiden, jüd.-pers. t^l^E»*!"! (Is. 41, 25) (phlv. draßntk
zitternd', AV. , drafset Bund.); in dieser Bedeutung
scheint ein Zusammenhang mit np. duru/s (so hiutet
die ursprüngliche Vokalisation), diiriiysün, duruyßlden
V
vorhanden zu sein, wie denn auch im 8<ähnäme oft
die Formen in den Varianten durcheinander gehen
(z. B. I, 107 Vers 839). Duriiyß etc. halte ich für
Composita, wohl mit Praep. ati, deren zweites Glied
ruys (No. 610) ist.
551. derniän *Arzenei', vergl. darß (No. 523), dermene'^)
^Absinth'.
i^dhar- 'halten', vergl. aw. drva- gesund'; phlv.
darwan 'Arzenei'.
LW. kurd. af/. bei. (48) darmän,
555. durüd, duröd (8ähn. I, 50 Vers 301, 170 Vers 751),
'Segenswunsch, Gebet'.
*j Vergl. auch SFgnirt^? *Frecliling*.
'-) *Banner', nicht Waife, wie Darmes t et ci-, Et. ir. II, 273 über-
Hetzt. Auch im Sähnäme heisst direfs niemals Lanze'. Mand. LW.
Nii^£»NT1 bedeutet *Kreuz* (Nöldeke, Mand. Gramm. 309 Nore i).
Greldner^s Übersetzung von aw. (jaos drafsö (y. 10, 14J durch
*ein Tropfen Milch* (Metrik, S. 153) ist schwerlich richtig (s. Ausgabe).
^) dramna (Bund), syr. LW. ^^O")*!-— 124 —
aw. droatäl- 'Geisundlieit' ') ; plilv. drüt (Men. ; AV.),
drütik courtoous' (West II, 280).
556. durüclen 'crndtcn\ Praes. diretv-em diretvldeiij durüd
'Erndto', JN^ni ^Erndte' (Is. 9, 2).
aw. vergl. dereta-, adereta- {t/ava-) ^geschnittenes,
gemähtes (sc. Korn)'; päz. drüdan erndten (PPGl.,
Men.).
kurd. dirün, dirütin erndten', dirün 'Erndte*; wa/.
```


## [2026-09-07T01:42:42.423Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/lewk-",
 "prompt": "Give the root, its meaning, and the list of derived/descendant forms, especially Proto-Iranian/Avestan/Old Persian, Latin (lux, lumen, luna, lustrum), Germanic *leuhtaz, Sanskrit loka/rocate. Quote the reconstruction and glosses."
}
```


## [2026-09-07T01:42:43.966Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B2",
 "prompt": "For the Persian entry روز (rūz): give the full etymology (Middle Persian form, Old Iranian, Proto-Iranian, PIE root), and any derived terms. Also list any other language sections (Arabic?) briefly."
}
```


### [2026-09-07T01:42:48.664Z] TOOL RESULT

```
# Proto-Indo-European Root *lewk-

## Root and Meanings
The reconstructed root is **\*lewk-** with three primary meanings:
1. "bright"
2. "to shine"
3. "to see"

## Selected Derived Forms

**Proto-Iranian/Avestan:**
- Avestan: 𐬭𐬀𐬊𐬗𐬀𐬥𐬙- (raocant-, "shining")

**Latin descendants:**
- lūceō ("to be light")
- lūmen ("light")
- lūcerna ("lamp")
- lūstrum ("purification")

**Germanic:**
- Proto-Germanic \*leuhtaz (see Modern English "light")

**Sanskrit:**
- रुच् (ruc, "to shine")
- रोचते (rócate, "shines")
- रुरोच (ruróca, reduplicated perfect form)

**Greek:**
- λεύσσω (leússō, "to look upon")
- λύχνος (lŭ́khnos, "lamp")

**Celtic (Welsh/Breton):**
- lluched/luc'hed ("lightning")
- golau/gouloù ("light")

The root demonstrates extensive reflexes across Indo-European language families with consistent semantic fields related to luminosity and vision.
```


### [2026-09-07T01:42:50.517Z] TOOL RESULT

```
# Persian روز (rūz) - Etymology and Derived Terms

## Full Etymology Chain

The Persian entry traces back through multiple language stages:

**Middle Persian**: "𐭩𐭥𐭬" (yʿm)
**Old Persian**: "𐎼𐎢𐎨𐏃" (r-u-c-h)
**Proto-Iranian**: "*ráwčah"
**Proto-Indo-Iranian**: "*ráwčas"
**Proto-Indo-European Root**: "*lewk-" meaning "to shine," plus the suffix "*-os"

The documented path shows "inherited from Middle Persian... from Old Persian... from Proto-Iranian... from Proto-Indo-Iranian, from Proto-Indo-European *léwk-os."

## Derived Terms in Persian

The entry lists these related words: امروز (imrōz, "today"), دیروز (dīrōz, "yesterday"), روزانه (rōzāna, "daily"), روزنامه (rōznāma, "newspaper"), روزه (rōza, "fast"), and نوروز (nawrōz, "Persian New Year").

## Other Language Sections

The page also covers **Andalusian Arabic**, **Moroccan Arabic**, **South Levantine Arabic**, and **Urdu**—most sharing etymology related to rice (Arabic رُزّ, ruzz) rather than the Persian "day" meaning.
```


## [2026-09-07T01:42:56.517Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%B2%D9%82",
 "prompt": "For the Arabic entry رزق (rizq / razaqa): give the etymology in full — is it said to be borrowed from Middle Persian rōzīg, via Aramaic/Syriac? Quote the etymology text and the root r-z-q information."
}
```


## [2026-09-07T01:42:57.313Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%B4",
 "prompt": "For the Persian entry آرش (Āraš): give the etymology in full — Middle Persian and Avestan forms, meaning, and any note about 'bright' or 'bear'. Quote it."
}
```


### [2026-09-07T01:43:01.701Z] TOOL RESULT

```
# Etymology of Arabic رزق (rizq)

Based on the Wiktionary entry, the Arabic noun رِزْق (rizq) is **derived from Middle Persian 𐭫𐭥𐭰𐭩𐭪 (rōzīg, "daily bread, sustenance")**.

The entry states: "Derived from Middle Persian _𐭫𐭥𐭰𐭩𐭪_ (rōzīg, 'daily bread, sustenance')."

There is **no mention of Aramaic or Syriac** as intermediary languages in the Arabic etymology section. However, the document does note that Classical Syriac has a related form: ܪܙܩܐ (rezqā), listed as a descendant rather than a source.

**Root information:** The entry identifies the Semitic root as **ر ز ق** (r-z-q), which appears across multiple related languages in the Wiktionary hierarchy.
```


### [2026-09-07T01:43:02.553Z] TOOL RESULT

```
# Persian Etymology for آرش (Āraš)

Based on the Wiktionary page provided, I cannot fulfill this request. The Persian section explicitly states:

"(This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium.)"

The document does not contain the Middle Persian and Avestan forms, meanings, or any notes about 'bright' or 'bear' that you've requested. The page only provides pronunciation information and identifies آرش as a male given name corresponding to "Arash" in English, with a cross-reference noting it relates to Shahnameh characters.

To obtain the detailed etymological information you're seeking, you would need to consult other sources or check the Persian Wiktionary version or related scholarly works on Persian names.
```


## [2026-09-07T01:43:15.381Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\npages=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('n',len(pages))\nfor leaf in (239,240,241,242,243):\n    print('=== leaf',leaf)\n    print(pages[leaf][:1200])\nEOF"
}
```


### [2026-09-07T01:43:16.608Z] TOOL RESULT

```
n 777
=== leaf 239
ت برایو بی اه آرامی
رة حواشی صفحة .۳
۵ آرامی_نام قومی از فبایل بدوی سامی ناد سوربه که درجنوب فلسطین در پبرامون
کوبر ومشرق رود اردن وبحرالمیت میزیستند. اين شبانان چلدرنشین ویابان نورد ازخوشاوسان
تزديك اسرائیلیان بودند و بغلط برخی آنان را کلدانی خوانده‌اند . ازفرن ۱۶ق.م.. آرامیان به
سرزحی‌های عتمدن همایبة خودروی آوردند ودست بفارث زدند. سوربه وشماق سسن‌النهرین میدان
تاخت‌وتاز آنان گردید. در کتیبه‌های آشور متملق بال۱۳۲۰ ق.م. این قبابل اخلایه ۸۵۵۵6
ودرآ تار متاخرنر آرامه ۳81796 خوانده شده‌اند . شلمااسر 51181۳1310366 اول, پلدشاه آ شور
در سال ۱۲۸۰ ق .م. با آراهیان در
زد وخورد برد . انان بهرجاکه روی
۳۳ «مم [ ۵ | رارق انید ییا رید وی | دسج | مین
کردند کتاورزان را بفرمان خود
در آورده و بازر گانی ر بدست گر فتند ۳۰ جاوما جوا مج چ + | »|
و بر راهپای کارواغی تسلط بافتند و در و اووا و ادووا <وا و :| و | و | دا
سرزهین هابی که بچنگه آوردته از | و | همم ۱ ها دا
جااب خود شهربارانی گماشتند . در و بو + ۳۰۹5 ۱۱۱۰۱۶
حدود مال۱۲۰۰ ق.م بی‌دمشق وحلب ۸ ۰۱4۵8۵۱7 4 ور ۹ ۳
ی 4 3 تا ۱ ۱۲۱ ۲۶۱۱۱ #۶ 1 1 1
کیره صفد و۵ مرح رات حود ۱ ۰ 1۱۱2711۱ 3 | وه 2-2 ]| ۲ 5 ۱
از میان بردند . هجوم آرامیان دز 9۱9۱۱۱ جوا چا هه ۷ ]۲
بین‌التهر ین‌چند ان‌شدید بود که خاندان ‌ 1 ۰ ۳۹۹ 1
بادشاهی آن دبار را برانداختند وخود 4« و | | ۲۶ ۶ ]<
=== leaf 240
آرامی - پرایی ۷۲٩‏ س
آرامی بکاربردند. بدبنوجه زبان آرام یکه اززبانهای سامی‌است وآموختنش برای‌هزدم مأی زبان
دشوار یست باخط آرامی که الفبابی.ساده بود سراسر کشورهای اقولم سامی نژاد را فرا کرفته از
بلحرالروم نایشتکوه (زاگری) وخلیج قاری زبان. بین‌المللی محصسوب حیشد.
هنگامیکه ابرانبان بسرزمین‌های آشور وبابل وآسبای صفیر وسوربه وعصر دست بافتند
باافوامی سروکار پیدا کردند که زبان وخط وسیلهٌ ارتباط دبوان های دولتی هشامثشیان و متصرفات
غربی ابران‌شد. درتوراة , کتاب عزرا باب4 بند۷ آمده: #در روز کار اردشیر اول(هخامنشی) بشلام
21520 ر مهرداد وئبیل [۲20 وباران دیگر آنان مخط آرامی و با ترجمةٌ آرامی نامه‌ای
باردشیر یادشاه ابران نوشتند. »
ازفرائن پیداست که خط میخی برای‌حوائج روزانه بکاردمیرفت" واین‌خط برای کنده کری
اختصاص داشت " اماالفبایآرامی با ۲۴ حرف برای کتابت آسانتر بود . خط سکه‌های محلی دور
حضامنشی و وزنه‌هابی که رویآ نبا خط آرامی نوشنه‌شده وخط بیاری ازمهرهای ابرانبان که ,خطا
آرام یکنده کری‌شده » بخوبی دواج این خطرا درایران میررساند .
کتیبه‌ای «رجيهةٌ آرامگاه داربوش ازنفش رستم بزبان پارسی باستان وبخط آرامی موجود
است وآن‌بنام اردشیر اولاست. یس‌از انقراض سلسلهٌ هخامنشی خطآرامی که در آن‌روز کار هممجا
رخنه بافبه‌بود همچنان راء خودرا پیمود تابجابی رید که چندی پس‌از آن بنام خط پهلوی‌خوانده
شده است. ۱
آ
=== leaf 241
مخفف آوداس تکه نام روز بیست و پنجم از هر
ماه شمی باشد ۱- و ممکون ثالث معروف است
که له آسیا کرده باشد ۴ - و بمعنی تقصیر هم
ات
آ رث و له - (۱) بش فوفانی و سکون
واو و فتح لام ء آشی باشد مانندکاچ یکه از آرد
پزند و بیشتی مردم درویش و ففبر خورند وآنرا
جریی «سخینه » گویند .
ومشی آرد توله اس ت که آش کاچی مانند باشد .
]ددم - بنتح رابم و سکون عیم ۰
نام کل آذربون است که نوعی از شقایق وکل
همیشه بهار باشد .
] ذن - بفتح رابم و سکون نون »
,کفگیر سوراخپا دارد وبدلن چیزها صافیکنند.
وکفگیی را نی زکوبند - و نم ولاشی هم
ضت . ؟ *#
]رذهاله - بیای (») بالف کشیده
و فتح لام » بمعنی آرد توله است که آش کاچی
ماتثف باشنه.
آرش
]رده جتح زای حوز , کاحگل را
کوبند . و آن خاکی است که با کاه آمیزند
وگل سازئد و بر دبواز وبام خانه مالند .
آرژه گر - بفتحم کاف فارسی
و سکون رای فرشت . شنصی را کون که کاه
کل عاو...
| دست ع بروزن وارست. بمعنی‌توانت
باشد که ماضی تواشتن است - و مضفف آراست
هم هست که از آراستن باشد . ۴
۲ دسته - مسر وزن وارسته مخفف
آراسته باشف .
دش ٩‏ - بنتح ثاك و سکون شین
شطه دار ۰ نام پهلوانی بوده ابرانی از لشکی
منوچهر و در صنصت تبراندازی عدیل و نظیر
نداشته چنانچه تیری از آمل بمرو انداخته که
قربب بچهل روزه (۳ ) راء است ۰ وکونند آن
تبر مجوف بودماست وآنرا از شبنم پ رکرده‌بود »
و بوفت طلوع آفتاب بجاب مشرق اداخت *-
=== leaf 242
]دی ح بکر الث و رايع و سکون
تحتانی ۰ بمعنی ممنوی باشد که در مقابل لفظی
است ۰ چه آرش بمعنی «معنی» است ٩‏ .
آدع بضم نالث و سکون غین نفطه
دار , مخفف آروغ است . و آن بادی باشد که
با صدا ا زکلو برهیآ مد ۰
]رغاده (۱) - بر وزن مارساده + نام
رودخانه ات .
]دغده ؟- بن الك ( ۲ ) بر وزن
آزرده. بمعنی نخبناك (۳)وخشمگین وقهر آ لود -
و جنگاور باشد - و بفتخ الث حريصي در چپزها
را گویند .
۲۰ ریش «- بنتح اول و ثانی ۰ بر وزت
صم کیش ۷. بوست. بیرخت زرهاباخد وآنرا
دو دازو ها چشم نیزبکار برند .
۱ آآرمان ۴ بر وزن آسمان ۰ بمعنی
جح تب و آرزو - و رنج بردن باشد - و پشیمانی
و آفوی را نیز گویند . *
آمده - بکر میم ۵ . مخفف
وسکون میم بروزن دارنده. بمعنی دریغ‌وافوی
و پشیمانی باشد .
] دهش » بکس میم . مخنف آرامش
)۱ خم ۳ آارغاوه ۰
)4( خم ۳ 0 رنگ دادن.
و
است که ساکن شدن و آساش ‏ فراغت وراحت
کردن باشد .
آدهون - بر وزن ولژگون » زری
را گوند که پیش از کارکردن بکارگر و هزدور
دهند . و معربی «عربون» خواند . 4
| رهیفه » بر وزن نا رسیده . قرار
] دن ه بر وزن فارن . مخفف آرنج
است که بند گاه ساعدوبازو باشد. وبعربی«مرفق»
خوانند ۷ ,
اد نج - بر ون نارنج . بندکگاه
ساعد و بازوست که عرب « مرفق » گوید ۷ - و
بمعنی بازو هم بنظر آعده است که ازمرفق باشد
تا دوش .
]را نگ - باکاف فارسی. بروزن وهعنی
آرنج‌است که مرفی‌داشد - ور نگ ولون (4)را
یز کنت
=== leaf 243
دوع ۰ با غن نقطه دار سس وزن
فاروق , بادی را گویند که از کلو باسدا برآید ؛
و بجای غن , فاف نیز گفته آند و عوق فافه
کردهاند .
آدون- بر وزن قارون » صفتهای
خوب و نيك را کویند .
| رو ند - بفتح دابع و سکون نون
خاقال آیسیی‌هان ‏ قو کت وق رورا
شف ۷
آدوین - بر وزن پا کدین » تجربه
و اسحان و آزماش راک ند .
ده ه بروزن چاره. بیخ و بن دندان ها
را گویند ؟ «
]رید بر فك - یکی الت و سکون
نحتانی و دال ابسد . این لفت از اباع است
وبمعنی دوائی‌باشد مانندییاز شکافتهوآ ترالزسیتان
آورند وبربواسیر طلا کتند تاقع باشد . وخوردن
آن زنان راخون حیض آورد ؛ وبکر همزه تیز
کگفته‌اند که آزدبرید باشد و
آریغ ۴ - بکر مالك و سکون
نحتانی و غين نقطهدار . کینه و عداوت باشد -و
سردی (۱) و نفرنی را نز گوبندکه از شخصی
(۱) چك : سردئی .
۱ و ایس کت ادا وود ۴ رك : اربدبربد. ۴ دریارسی‌باستان (دکتبة بستون. متون؟
بند ۱۲ ) 2621624 از رشه ۲18 بمعنی دشمن ۳0288,۳6۲61566ععدای۲۲.۲۲ )
(۱25-6 . 5 ,1895 96110160,5)۲255018این لت درفر‌هنگه‌اسدی چاب‌نهران س‌۲۳۸ونیز
موضع‌دیگر برهان بخلط «آزیغ»آعده. خسروانی شاعرکوید : کآربغ زمن بدل کرفته + کتجکاوی
های علمی و ادبی . نشریهٌ دانشگاه تهران شمارء ۸۳ . قطمه .ای از بفستان بقلم نگارنده 4۱
آریا _ اوستا ۰21۲72 پارسی‌ب‌استان 211۷2. سانسکرمت 217338 «بارتولمه ۱۹۸ نام
طایفه‌ای از ند و اروپائیان که در عبدی بسیارکه
```


## [2026-09-07T01:43:24.727Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\npages=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=pages[241]\nprint(len(p))\nprint(p[1000:])\nEOF"
}
```


### [2026-09-07T01:43:25.938Z] TOOL RESULT

```
1470
وچهر و در صنصت تبراندازی عدیل و نظیر
نداشته چنانچه تیری از آمل بمرو انداخته که
قربب بچهل روزه (۳ ) راء است ۰ وکونند آن
تبر مجوف بودماست وآنرا از شبنم پ رکرده‌بود »
و بوفت طلوع آفتاب بجاب مشرق اداخت *-
و نام پسردوم کیقباد هم است که او را «کی‌آرش»
گفتندی ۷ - و یکس ثالث ۸ - بععنی «معنی*
"4
۹ بونکر ۱۱۲ *.
؟ - پپلوی )27 « تاوادبا
۴ - ول : آرستن ۵ اوستا
۱ - از آن خوانند آرش را کمانگیر
که از آمل بمرو انداخت يك نی
و ۱۶۲
شتین چوکاوس با آفرین
2 مزدسنا ۷ ۰
مراد - معشوق » موب :
```


## [2026-09-07T01:43:38.908Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT xsviwi ===\"; grep -n -i \"xsviwi\\|xsviwl\\|iSu-\\|isu-\" BRT.txt | head -10\necho \"=== BRT arxsa ===\"; grep -n -E \"ar.xsa|.r.xsa-|rxsa\" BRT.txt | head -20\necho \"=== try ref_page for BQT 31 ===\"; timeout 300 python3 tools/ref_page.py BQT:31 --image 2>&1 | tail -30"
}
```


### [2026-09-07T01:43:40.224Z] TOOL RESULT

```
=== BRT xsviwi ===
7635:•  j.  3r9x§a-  a  £N.  eines  berühmten iranischen  Schützen**:  tiyris  . . y'im  anhat °sS  xi-vitui-Uus  xsviwi.iivaiimd  airyanqm airyö^stii:at  haca  garSit  ^anvantain  avi gairim  "der  Pfeil  , .,  den  der  PfeilschUtze if.  schoss,  der  beste  Pfeilschütze  der  Arier, vom  Berg  A.  bis  zum  Berg  X<:"   Vt.ÄÖ.
10995:•  j.  xSvtwi.i§av-  m.  Tfeilschiltze":  ir?xsd '^^  xsviwi.isvaUmB  airyanam  Yt  Ä6;  — •/ä«  parBMv^m  "den  ferntreffenden PfeilschUtzen"  Yl/o.ioz,  77.12.
10997:•  j.  x§viwt.i§va't«ma-  Adj.  'der  beste Pfeilschlitze':  jrsxsd  (sd.)  xsviwi.isus  'mS airyanam  Yt.S.6.
=== BRT arxsa ===
2514:-  g.  'a-  Pron,  ident.  'ich,  du,  er  selbst',  humata  'ta'  ..  aat  mam  narö  paskat  ya- nur  NS. :  yi  maibya  yaos  (sd.)  akmai  astu  g3„ie . .  "um  dieses  (deines)  guten  Denkens vakUta  mahyä  isfois  voha  eöihm  mananM  willen  .  ."  H.2.14''.        2)  substantivisch: ".  .  dem  verspreche   auch  ich  selber  das  ,  ^tai  ti  .  .  avayam  *danmaM  Y.  öS.  i  '>;  — beste  meines  Besitzes  durch  VM."  y.4''-   am  yasna  .  .  ''ta  patti    ava.jasa  .  .  aoi \Z;    —    ai   -3    vaocal  ahurö  mazda    ''da  zam  ".  .    um    dessentwülen  (was  hier  ge- sprach er  selbst,  ^/iM."  Y.sp.ö.  [schiebt)    komm  . ."  Yt. 5.132  (s.  i);   — zBed._s.  Gdn.  GIrPh.   '  52      Ich   '^'^^<=^'^^'- -faimat puir.lt  (sUtt  AS.)  Kimar^xsaf^u/ia dass  f.  as'  aus  einerrart.  idg.  'n  'selber  er-    ,    ,  ,   ,.,       .,•.,..'        ,     .  ,        „ wachsen  ist,  die  in  aUi;  (aus  'a-u-r,  wie , (sd-)    damit  (was  ich  dir  gebe)  such  ..' eJroiaus*jn-H-/°)steckl.Dochs.B(;M,GrGr.3244-    V.  1^.  14;  —  in  Kongruenz  mit  dem  Prae-
5566:•  j.  'airyaman-  m.  Name  des  mit  J  (7/r- ,  •  j.  'aurvataspa-  Adj.  'der  schnelle ysmä  isys  beginnenden  Gebets  Y.54.1:  Rosse  hat';  a)  von  ^rar-imd  Äj'ari>.tiiji^u-: 'matiim  mq^ranqm  maBittm  Yt.j.5;  —  Är'ur?  "toffi  YL/0.90;  6.4;  —  'tun  bavähi T-3r/irayn3m. .  ya^asli  antan  ahuna(&A.)  yaia  kiari  Az.  6";  —  am.nakc  hü  yat 'manaiAD.)Vi.24.i;*li.ioj.  a)  sonst |  Vn^  YLJO.  13;  —  hiarsxsaS^m  'ptm mit  isya-.  'mamm  isim  .  .  ßäsB  mq^fvm  Yt  6. 1,6, 12.^4, 1^.81,  \.  16.4;  —  hvar>- ..  b»r?am  Aa',aoxt?m  Vr.2.10;  G,/.6,  S.j^/attJj  °päi  Y.ÜÄ22;  —  hrerixiaiiahe 2.3;  —  tfm..  vJspanqm  sravanhqm  ufard.-\ ..  -pake  Yt.  Ö.o,  Y, 22. 24;  /.  11;  —  Iwan- kainm  fradaiqm  yim  'mamm  tsim  FrW. '  xsaiia  'pa  (VS.)  V,  j/.  5,  b)  von  apqm 4-1',  1 ;  —  'taan^m  isim  . .  maiisüm  o/aAe  napät-.  apqm  napa  -ps  Yt  ig.  51';  — sra-.arahqm  Y.54.2;  Vr.  24,1;  —  °manS  aPqm  napättm  'ptm  Y.  2. 5;  —  apqtn isyehe  hafu{iitä..'manö  isyeke ,.  haililca  ..  nap5  °pa  Y.65.13.  'pä'a  VyLjJ, Vr.24.2;  /.8,  S.7.3.                                    4'>"(?).
7854:•  J.  lucaBhe  InC  'zu  bedrängen,  in  Not zu  bringen':  ava^he  narqm  asaonqm  qz° duwarltavarxsam  Yt.  13. 39.
20761:bezeichnet  l)mit  einem— substantivischen oder  adjektivischen  —  demonstrativen Korrelat  (Stverz.),  das  /)  folgt;  uzw. a)  ^kva-  (sd.);  a)  im  gAw.;  das  Relativ ist  a)  substantivisch:  yS  aläum  vahistS .. at  AvB  asahyä  arahat '. .  vSstrl  (sd.)  Y.  jj. 3;  —  yasßm'''*  xia%räl  .  .  mBthai {sA.) . .  kvS  .  .  Y.  4^.  4;  —  s.  noch  Y.31. 16 (Sp.  1202  u.);  —  mit  Lok,  parL;  yi eara^uÜr^m  .  .  mantaiili  xsnüus  kvS  na *_/rairBidyai (sd.)  ?r?'k,wä\.46.\i.  ß)  ad- jektivisch; nur  NSm.  mit  nä  (Sp.  10510.) sva.  "wer';  at  yS mä  nä  mar?xsaitl..hv5.. Y.  JJ.  10;  —  at  yastStni^  nSil  na  .  .  äyJt (Sp,  150  o.)  ärup kvs ..  "^.46.6.  B)im jAw.;  das  Relativ  ist  ci)  substantivisch; die  Verbindung  ist  ungenau;  ys  aüalsam sBnqm  jainti  . .  xraasyJJara(sd.)ai  nS  .  . AvB  urva  paräiti  parB.asnäi  arauhe ya^a . . V.ij.8*>.  b)    '^a-  (sd.);    nur    b)    im
24726:•  j.  raek-  V.  'linquerc'.  Praes.  8  irinak-, i6  (Des.)  irlrixsa-,  30  (Iter.)  raf'aya-; j-Aor.  I  raixs:  —  PFP.  'riiya-;  Inf. »rixti,  'ri^3;  AbsoL  'irixtfm.
28471:27. 13;  —  matdä  ai  msi  vahists  triiväsca  .  *varsta  aisqm  °'kantm\ca\  aahölrisbm *%anäcä  vaola  '^.34. 15  (Sp.  375  u,);  —  N.  2g;  —  *ar>dus  hl  •%a/t»m  N.  42;  — gavSi  ärBil*ä  *sSndä  (sd.)  a^Ji/  '"kanäisca  kvar>xsalt3m  .  .yazamaide . .  vacaca  '^naca ar^häiScä  yS  Is  sSnghs  .  .  Y.57.14;  —  zaohräliyasca  Ny.i.iö;  —  ai/iAä  dainayä kyat  .  .  mazds  .  .  gai^as^S  ta^S  dalnas-  j  mqs  vaca  da^Snake  mit  '^när/  apayantafu (^Ä)ca  ..  ''Sonata  ssngkqsca  Y. 31. 11;  —  ■  (S*p.  71  m.)  Y.p.  31;  —  mit  näherer  Bc- nSii  na  manä  .  .  sSngha  .  .  xraiavö  .  .  Stimmung  durch  ein  Adj.:  hrarlianqm varanä  (sd.)  .  .  uxha  . .  "SanJ  .  .  dainä  '^nanqm  vanzüi  pairi  .  .  dulvarstanqm urvqnS  kacainlEY.4S-3.         a)  insbes.  im  ■ 'äMiwa»!    var?zai    Vr.  /J.  i;    V,  JÄ  17';
30664:•  j.  hvar«-xäaeta- "  n.  'der  leuchtende Sonnenball,  Sonne',  auch  als  Gottheit;  yas? tava  mazdä  k»r»naot  tacar»  ''nsit ..  *anlar».- ann»m{s<i.)  upairi  't»m  Ytj.go; — ya'^a avat  't»m..fraca  ätti  YtJO.  118;  —  °t»m *utyS.raili  Y.ig.iB; — uzayara  uslra  'ta aurvat.aspa  V.27.5;  —  yatcit  ahi..upa  ave stärd  .  .  upa  aom  maT»h»m  .  .  upa  'lfm aurzaj.rijp»m\t  12. 33—^4;  —  -/»m  am»i»m ralm  aurvat.asp»m  yasamaide  Yt 6.\\  6, jj.Si,  Y. /ö'.  4,  S.S.  11;  —  °tai  aurval- aspäi  Y.68.22;  —  'tahe  amtsahe  Yt,  6. o, Y.  22.  24;  Vd.20;  —  hvar»ca  xiaHahe'^ aurvaLaspahe  Y,  /.  1 1 .  a)  hvar»xsattaht (näml.  ayar»)  heisst  der  11.  Monatstag: 'tahe  amfsahe  ralvahe  aurvat.aspahe  S.  i. 11;  vgl.  2.  II,  Y.lö.  4.
=== try ref_page for BQT 31 ===
python3: can't open file '/home/sfmqrb/git/rishe/data/verification/sources/refs/tools/ref_page.py': [Errno 2] No such file or directory
```


## [2026-09-07T01:43:57.955Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://iranicaonline.org/articles/aras-avestan-erexsa-legendary-archer",
 "prompt": "Give the etymology and meaning of the name Āraš / Avestan Ǝrəxša as stated here — is it connected to 'bright' or to 'bear' or left obscure? Quote."
}
```


### [2026-09-07T01:43:59.244Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T01:43:59.753Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\necho \"=== ARY روز ===\"; grep -n \"روز\\b\" ARY_pages.txt | head -5\necho \"=== ARY روشن ===\"; grep -n \"روشن\" ARY_pages.txt | head -8\necho \"=== ARY رخش ===\"; grep -n \"رخش\" ARY_pages.txt | head -8\necho \"=== ARY latin index leuk ===\"; grep -n -i \"LEUK\\|LEUQ\" ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-07T01:43:59.847Z] TOOL RESULT

```
=== ARY روز ===
25:نیز آورده‌ام تا خویشی زبان‌های ایرانی امروز و رابطه‌ی آنها با پهلوی و اوستایی و پارسی‌باستان و
78:می‌شد ولی امروزه این نام بشتر برای اشاره به زبانهای بخش شمالی شبه قاره‌ی هند و به صورتث
98:کاربرد قرار گرفت و همانطور که در پالاگفته شد امروزه فقط برای اشاره به زبانهای ناشی از
134:پست شدن نژادی و تیرگی نسبی رگ مو و چشم آنها شد. موضوع پرتری‌های نژادی (که امروزه
310:نوآوری می‌کردند و يا نام هند و اروپایی قدیمی را برای آن بکار می‌بردند. این فرآیند امروز اهر
=== ARY روشن ===
177:فرهنگی و زبانشناسی آنها را روشن می‌کند. بررسی کوچگری مردمان ترکك زبان مثال بسیار مفیدی
1137:زبان‌های ایرانی کهن دارند می‌توانند رهنمون‌های خوبی برای روشن سازی برخی از نکات و
9162:۱ بازگشت به: روشن,.
9163:ا ۲- چم واژه‌های سانسکریت و ارمنی و یونانی و لاتین این فهرست: روشنایی. َ
9165:۲ / _روشن» روشنی» روشنایی
10038:چم واژه‌های ژرمنی این فهرست: نور دادن» درخشیدن» تاریکی را روشن کردن. چم این واژه در زبان
=== ARY رخش ===
350:کم شده است. در شمال و مرکز ایتالیا «اتروسکان‌هاء (177741780۸1758) تمدن درخشانی را به وجود
753:راتراسکان‌هاء (۳131180۸75) مردمی غیر هند و اروپایی بودند که در شمال ایتالیا تمدن درخشانی
958:کشیشی و آئین‌های مذهبی بود. -تولوس هوستیلیوس (130571118 110178) که جنگاورخشن .|
3450:این واژه در زبان‌های ایرانی کهن و زبان سانسکریت و زبان‌های ژرمنی و اکثر زبان‌های دیگر به معنی "درخشش" و
3451:"درخشیدن" است. حتی معنی برگرفته‌های پهلوی این واژه(81۵210۸۷ 8۸62 دارای چم" درخشیدن"
9199:واژه‌های فارسی "آرخش " و "درخش" و "درخشیدن" و آرخشیدن" نیز از همین واجریشه‌اند.
10038:چم واژه‌های ژرمنی این فهرست: نور دادن» درخشیدن» تاریکی را روشن کردن. چم این واژه در زبان
10777:چم این واژه در زبان ارمنی: درخشش
=== ARY latin index leuk ===
1330:. isle Gl gla (POKORNY: 837 - “PLEUK gh)! 4 28 Ga ply 5!) FLYGTE
8965:LEUKOS — (GREEK) gly RAOCHA AAVESTAN) ples) i
8993:LUCHIR HOLD IRISH) 45 5-1) p\ LEUKOS GREER) gb y
9786:LEUK DUTCH) gscla SARAD, SARD- (SANSKRIT) cy Site
```


## [2026-09-07T01:44:04.153Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\nsed -n '9150,9215p' ARY_pages.txt\necho \"==== page tag near ====\"; awk 'NR<=9165 && /\\[pdf page/ {l=$0; n=NR} END{print n\": \"l}' ARY_pages.txt"
}
```


### [2026-09-07T01:44:05.277Z] TOOL RESULT

```
۱
۱
۱ اوستایی (4789740): ۸ بونانی 07280): 180665
پارسی باستان (287500 0۵10): ,۸06۸ لاتین ((اما: نان تا
: الا ناه
پهلوی (۲7الل۸): 306 پسگشت‌ها : هار درد
کردی (4021574): 7 ,81273 0 2000
۱ بلوچی (اللعتا :8۸‏ ۷۶۸3 9 (0۸3) :25
۱ افغانی (پشتر) (اللهتا۵70: ۰ 300 ,80513 1 ,60 8۸0
۱ ی سانمکر 160859 نش 16 برهان قاطع : ۹۱
۷ ری (۸۸/۵(۷۸۸: ۱۵ ی 1015
ا
۱ بازگشت به: روشن,.
ا ۲- چم واژه‌های سانسکریت و ارمنی و یونانی و لاتین این فهرست: روشنایی. َ
[pdf page 311]
۲ / _روشن» روشنی» روشنایی
اوستایی (4۲8874(۷): ۰ ,3۸0277۸3۸7 انگلیسی کهن (/5لل8/0 010): ‎٩‏ وچ
1۸0761151۸1۸ ,3۸0271۸011 107
10۸ انگلیسی (8(/01/3[7): 11017
پارسی باستان (۸(۷اق۶5۲ 0-]01): دانمارکی (0۸۸/37): 118
۸تا۲۸ ,۸078110۸ سوئدی (8(75:0157): 13115
پهلوی (/۸(14۲): ۸081181۲1 ,۸08130 نروژی (۸/0/1750141): 1385
کردی (7ل8۲(70/5): دای هلندی (07۴[7): 117
بلوچی (/6/7/ام۸ق): ۸051۸07 اسلاوی کهن (ع1/ما5 7لع#لاتل) 0ا0):
افغانی (پشتو) (47077۸41): :هی 11
تخاری ۸4 (۸ 40لا 7۸ل708): 14 لهستانی (8/7/-۳0): 0 بلک5 155
تخاری 8 (8 /(ل72ل708): کناب ,نا چکه (256[7): 1
سانسکریت (54۸/55077): 80605 اسلوا کی 81.0140): 1۸
7 ۸06۸۸5 ,800۸38 لیترانی (/(1لهلا 7 /ل): هفزآها
ارمنی (/۸//842): 5 و1018 پروسی گهن (551424 27 طا0): 168
پرنانی 07/2570): نزای نان ۸ ایرلندی کهن (50ل#ا ص0): 1
ٍ لاتین (770۷ا1): ,1180 ,نآ بتان1 پتیت (7177175): نانآ چکاتانا
دی ادلی ۱81
فرانسه (3ح5۸7): اد۱۱ ۱8۱۷ پسگشت‌ها 5
اسپانپایی (82۸(//52): 12 90 ۲080800
ایتالپایی (۵۸لله7): 11 4 (7617) :مه
رومانی (۸/۸/1۸(1): 111۸ 7 ,185 :0245
گوتبک (00717/0): 1 ۱ :۸2لا
ایسلند یکهن (0/07۸12/(مع9 00): 1 010113 ,105 (831613) "
58 156۴ 5 ,991 ,60 ۸
ساکسونی کهن (5400/0 طا0): ۰ 1101۳ 7 101117 :002/5
فریزی کهن (/(94ل28 ضا0): ۰ 11۸0737 0 (3011) :57
آلمانی کهن (6880/۸0 71017( صا): 9 (136171) ۸4/۸
۱ 1100 برهان قاطع + ۹۷۶-۷
آلمانی (05704۸(0): 117
۳
[pdf page 312]
روغن / ۳۱۳
یادداشت
واژه‌های فارسی "آرخش " و "درخش" و "درخشیدن" و آرخشیدن" نیز از همین واجریشه‌اند.
:
| چم‌انگلیسی سرواز‌ی فارسا سا ۱0۷6
۱ اوستایی (4۷587/40): ,0011۸ 5 0
۱ ۸06۸7 آلمانی (/(657244): انا تا
پپلری (/4۲اط۸ :۰ ,80۷0 ,803613۸ انگلیسی کهن (34ا2/0 ۰:01 22۸36
8001
کردی (7015): ۸1 پسگشت‌ها 0/5
بلوچی (زبق‌ت۸ق: ۰ ,3301000 ,330۸81 5 ۸0/0000
لداا نی 5 (ا[0) :۸2/5
ابسلندی‌کهن ((0۸14/ مک (ل0): 5 (817788) ۸/0
۱ (ارایرد برهان فاطع + ۹1۸
آلمانی کهن (/(062۵14 03ج صمان):
ا
یادداشت: ۹
چم این واژه در آلمانی: خامه» سرشیر,
ِْ
==== page tag near ====
9164: [pdf page 311]
```


## [2026-09-07T01:44:15.350Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\ngrep -n \"بازگشت به: روز\\|/ روز\\|روز »\\|^روز\" ARY_pages.txt | head -10\necho \"=== search RAOCHA ===\"; grep -n \"84006۸\\|RAOCHA\\|806۸\\|۸06۸\" ARY_pages.txt | head -10"
}
```


### [2026-09-07T01:44:15.413Z] TOOL RESULT

```
=== search RAOCHA ===
1510:انگلیسی کهن (8۸/0757 010): 801806۸ 105 شا
1660:سانسکریت (5۸4۸/8627): ۸06۸ ,باهش یونانی (0788/0): 58 ,006071085
4870:گوتیک (007[10): 7۸۸ 1 806۸
6228:7806۸ ,نا80[ ,نت080 ایرلندی کهن (تلدلعا صان): 1010
9153:پارسی باستان (287500 0۵10): ,۸06۸ لاتین ((اما: نان تا
9178:7 ۸06۸۸5 ,800۸38 لیترانی (/(1لهلا 7 /ل): هفزآها
9203:۱ ۸06۸7 آلمانی (/(657244): انا تا
12351:گوتبکه (007]770): ایند سوئدی (852[5): 806۸
14146:ایتالپایی ((۵ال7): 05۸ برهمی (۵078(41420): ۸06۸
```


## [2026-09-07T01:44:21.829Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\nsed -n '9120,9162p' ARY_pages.txt"
}
```


### [2026-09-07T01:44:21.876Z] TOOL RESULT

```
ارمنی (۸7042/1421): 07 نا رای بان
پرنانی (0۵20): 7381 ایرلندی کهن (لادتة[ 0): 577۸13184
ایسلند یکهن (/۸2 5010۸۷ ضام). ولزی (7۴1): زاره نت
3 ای ان
ساکسرنی کهن ((2200 طا۵): 857801 پسگشت‌ها برد ۲
فریزی کهن (۲/94۷ صزم): 978300 03 ق۶006
آلمانی کهن (/0520/۸0 زاب صا0): |1075 (5788۸34) +81
اد ان 1 (8183) داد ها
آلمانی (022۵/2)+ ای ان 4142 هی
انگلیسی کهن (8۸۷0/3(7 صا۵): 8783۸31 4 (30ف8785) 0/05
انگلیسی (4لول6(/0): 1 ان 46 (31ه5775) +547
دانمارکی (0۸0۷/8): آبازا ان 130 :7 :
سوئدی (8/80157): رای ان 279 ۸0
نروژی (۸/0/۴0۸7)+ ان برهان قاطع : ۹۶۹
بادداشت:
این واژه در برخی زبان‌های هند و اروپایی (ثلاً یونانی) چم جاری بودن را نیز دارد.
[pdf page 310]
۹
۲۱۱/۶ ۱
ِ

! پهلوی (/4ال2۸): ۸0716 ,30 ,20016 هلندی کهن (تلآتاظ صا0): 100
کردی (80/51). رای
1 بلرچی (التل‌نالمه): 5 ,8077 پسگشت‌ها رده اد ان اد
۱ افغانی (پشتو) (/4۳037): ۸10۸ زر کر ۳
انگلیسی کهن (8۸/015/0 ۰:00 ۸5۸0۸ 0 (۳18871۲۴]) دا ام
انگلیسی (7ل5لل8(/01): زا دی برهان قاطع + ۹
پادداشت.
: چم اين واژه در انگلیمی نوین: شکم جانور
1 :07۳7103۸ 5۳۵۲5۲ 02۳02۵ 5130878 ۷8۵۷۷ 7158
۱
۱
۱ اوستایی (4789740): ۸ بونانی 07280): 180665
پارسی باستان (287500 0۵10): ,۸06۸ لاتین ((اما: نان تا
: الا ناه
پهلوی (۲7الل۸): 306 پسگشت‌ها : هار درد
کردی (4021574): 7 ,81273 0 2000
۱ بلوچی (اللعتا :8۸‏ ۷۶۸3 9 (0۸3) :25
۱ افغانی (پشتر) (اللهتا۵70: ۰ 300 ,80513 1 ,60 8۸0
۱ ی سانمکر 160859 نش 16 برهان قاطع : ۹۱
۷ ری (۸۸/۵(۷۸۸: ۱۵ ی 1015
ا
۱ بازگشت به: روشن,.
```


## [2026-09-07T01:44:34.920Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\npages=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor leaf in (306,307,308,309):\n    print('=== v1 leaf',leaf)\n    print(pages[leaf][:800])\nEOF"
}
```


### [2026-09-07T01:44:36.105Z] TOOL RESULT

```
=== v1 leaf 306
-9--
درودگری باشد . ومضفقف اکر هم هست که‌آن
کلمةٌ حرط است - و جاره را نیز گویند که
وید که در مقابل زن است
ارابه - بر وزن فرابه ۰ گردون را
گویند ٩‏ . ۱
اراقو بفتح اول و قاف و واو بالف
کشیده » بلفت رومی
نام تضمی است بشکل
دور و برنگه سیاء و
بفایت‌سلب ؛ و درمیان
کندم و علان. پسیاز
میباشد ؛ و انرا به
شيرازی‌سيمك‌خواند . #ق
آرد تن که و اف
پسرشند و بر ورمهای
کرم و صلب ضماد
کنند نرم ساژد .
ار اهو فی » با میم بر وزن فلاطونی»
- بلغت پونانی لاله را کونند . و آن باغی و
صحرابی هردو می باشد ۰ و بعربی شقایق النعمان
خوانند ۰ و نوعی دیگر هم مت که آنرا
آتربون گوند .
)۱ چش : است .
(:( چك : - وافه اعلم .
اد ان » بتشدید انی بر وزن بران » نلم
ولایتی است از آنریاجان که کنجه و بردع
ازاعمال آن است . گوند سعدن طلا و نفره در
آنجا هست (۱)؛ و می تشدید عم گفته اند ۴ -
و حنارا نیز گونند که بدان دست و پای
ار او فك ه بر و
=== v1 leaf 307
ی
"ار پیاسیوس - با تحتانی و سین بی
نقطه و تحتالی دبکر بروزن مرد چایلوی . نام
حکیمی بود (۱) از یونان . گویند در علم طب
مپارنی تمام واخته است ۷ .
ار بیان س بر وزن بهلوان » علخ آبی
باشد و بعربی جرادالبحر
گوند . قوت, باه دهد
وبلفت اهل شام کل‌بابه نه
را گویند . اربیان
از تا - با نای قرشت پروزن برصیصاء
بلفت زند و پازند (۲) بام خانه را کوبند ۴ .
اد فا ه با تای قرشت بروزن فردا , بلفت
زند و پازند (۲) بوم و زمين را کویند ۴ .
ار تحك « بنتح جم بر وزن اسپرك :
برق برادر رعد را کوشد » و بکسر جیم حم
شظن آمده است . ۶ه
ار نگ » بر وزن فرهتگه » نگارخانة
مانی نقاش باشد - و نام بتخانةٌ چين هم هست -
و کی لت که لا مایت ما من
تقش است ؛ و بضی این لفت دا بجای حرف
ئالك ثای مثلثه آورده اند و کفته اند کهدرافت
فارسی بغیر از اين لفت و لغت ثغ بثای سه نقطه
)۱( چك : بوده .
و غین قطه دار دیگر لفتی بثای سه نقطه نبامده
است ۰ و
=== v1 leaf 308
ارجالون
کثتاس را در جنگه کشته بود و لهراسب پدر
کتتاس راکه تركه پادشاهی کرده در بلخ‌بعبادت
مشغول بود بقتل در آورد و به آفرین و همای
راکه دختران کشتاسب بودند گرفته در دوینمدژ
محبوس داشت عافبت اسفندبارین کشتاسب روئه
دژ را کرفته ارجاسپ را کشت و خواهران خود
را نجات داد - و نام پهلوانی عم بوده تورانی .
ار جالون » با لام بر وزن افلاطون .
گیاهی است که مانند عشقه بر درخت ها ید
و آنراکرم دشتی و بعرب یکرمةالبیضا خوانند .
ار جان - بر وزن مرجان , بلفت اهل
مفرب چلفوزه‌باشد ؛ و بسنی گویند لوعی ازبادام
کوهی است و این اسح است .
بمعنی عزیز و گرامی و صاحب فدر و خداوند
(۱) مرتبه باشد چه ارج بمنی قدر و مرنبه و
مند یمعتی صاحب و خداوت است - و دادا و
دانشمشد را هم کنته اند- وهر چیز قیمتی رائیز
کوند . وبممنی بی همثا و غلبه کننده هم‌آهده
است . 4
ار جن بر وزن آرزن » درخت بادام
(4۱) چش : - خداوند .
تلغ را گویند ۲ ۰
ا
=== v1 leaf 309
خوانندش, وبعض ی کویند منسوب‌باردیل‌ین ارمنین
است وتا کردة اوست .
اردجان س با جیم بر وزن همزبان»
از جد اول اهل نجوم است و در احکام مرقوم.
ار دش 7 س بفتح اول و ثانی وضم‌دال
می نفطه و سکون‌شن نفطه دار , نام مقدارععینی
است از کناهان بزعم فارسیان .»
از ۵ شیر - نام بهمن بن‌اسفندبار پدرداراب
است. کوش
چون جدش
او را سیار
دلیروشجاع
یک
روز آرد که بست ویذجم از هر ماه شمسی‌است
پدو تعلق داردا .نيك است درین روز نو بریدن
و پوشیدن , و بداست لقل و تحوبل کردن ۴ .
اددا ه بر وزن فردا » تلم موبدی و
دانشمندی است ۰ و او در زمان اردشیر بابکان
بوده و فارسان او را سقمس دانشته اند و او را
ار داد بر ون فر‌هاد نبز کفته اند و پدر او
وبراف نلم داشته بکسی واو ۴ .
ار ۵اه - بر وزن مردانه . کلی است
محرایی که آنرا خیری بری گویند ت
"ارب ه بروزن‌هرشب , جنگه وجدال
را گوند ۴ .
ار3لیل ۰ بر وزن زجیل » نام پس
آرمنین بن لنطی بن بونان
```


## [2026-09-07T01:44:57.158Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\npages=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor leaf in (356,357,358):\n    print('=== v1 leaf',leaf,'(printed ~',leaf-210,')')\n    print(pages[leaf][:700])\nEOF"
}
```


## [2026-09-07T01:44:57.940Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\npages=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('n',len(pages))\nfor leaf in (434,435,436,437):\n    print('=== v2 leaf',leaf,'(printed ~',leaf+540,')')\n    print(pages[leaf][:900])\nEOF"
}
```


### [2026-09-07T01:44:58.376Z] TOOL RESULT

```
=== v1 leaf 356 (printed ~ 146 )
اخك تلح ه جفتح فوقالی » کنایه از
شراب الکوری باشد - و اثك چشم را نیز
کواند .
باشد . ۷
اشگر ف « بنتح اول وکاف فارسی بر
وزن خلجرف , نیکو وخوش آبنده را گود -
و پکس اول بمسئی مطبر و قوی :و گنده
وبز رکه باشد - وبمعنی‌شأن وش وکت وحشمت‌هم
آمده است_.
اشگر ه۱ « بکر اود و کاف وفتح
رای قرشت , مرغان شکاری دا کویند مطلقا
و ضی گوشد مرخی است شکاری از جنس
بلشه لیکن از باشه کوچکتر بود و آدرا پیفو
خوانند
اشکش - بفتح
نم پهلوانی بوده است۳
اشك شیر ی - کنابه از کربة شادی
اول پروژن س رکش »
باشد -
) شاك طر مد بممنی اك < شیرین است
که کنابه از کربة شادی باشد .
اشگت « بکر اول و شح شالت
وسکون ثالی و فا و فوقائی » بمعنی غار و رخنهٌ
کوه ی
پاشف .
0
مه اس
فا . بهفر وشكوفةً درخث را کویند - وبمعنی قی
واستفراغ هم آمده است ّ.

=== v1 leaf 357 (printed ~ 147 )
_ٍِِ
اشکو خیدن . مصدر اشکوخ است
که لفزیدن دبسردرآمدن وافتادن‌باشد , چها کر
کی را پایش از یش بدد رود و یفئد گویند
اشکوخیه .
اشکو 4 ه بن اول , بسنی شکوفه
و بهار درخت باشد - و فی و استفراغ را لبز
گویشد ۱.
اشکوه « بنم اول والث وسکون تانی
و واو و ها ء بمعنی شآن و شوکت و شکوه
وعنلمت باشد ۴ .
اشکیل؟ بکراول وثاكك وسکون‌الی
وئحتانی ولام » بمعنی اک ات وان اسبی‌بود
که دست راست وپایچپ او سفید باشد - ومکر
وحبله وفریب را نیز کویند .
اشکیل چشم - اشکیل مملوم و نتح
جیم فارسی وشم شین قرشت وسکون‌ميم. دوایی
است که آیرا عوسج کوبند جاگ بر کف ای را
بکوبند و آب آنرا بگیرند و هفت دوز درچشم
چکانند مفیدی چشم کد هم رسیده باشد زایل
گنت -
اشکیوة » بنتح اول و سکون انی
وثالث وبای حطی بواو رسیده وبدال زده» مر کب
را گوبند که
=== v1 leaf 358 (printed ~ 148 )
اشو ی
که کمانگران بر باژوی از جابدر رفته ‏ بندند
واشق معربآشت .
اشتاف مامثا بنتح اول و کسرفاه
یعنی عصاره مامثا ومامیئا بلغت سربانی‌نام رستنی
باشد که آنر! درفااضات بکاربرند وآنرا زهبانالی
که درئواحی موصل میباشند سازند . درد چشم
و ناقم افننت. ‏
اشیهه - بفتح اول وکسر‌انی بتحانی.
رسیده و های مقتوح » آواز هو شيهه اسب را
قز بر 9
هم حست خوشبوی که آنرا دواله میگوینه
وبعربی شبیه‌السجوز ومكك‌القرود خوانند» مانند
عثقه ولبلاب بردرخت یچد و اکر بسایند و ور
چشم کشند چشم‌را جلادهد. *#
اشو۱ بفتح‌اول وضم‌ثانی بواو رسیده,
بلخت زند ویازند (۱) بمعنی بهشتی باشد که در
حقایل دوزخی است ۷
اه ۳ ی یی
شوع < بضم اول بروزن دروغ» شخص
عجپول‌النسب وء‌فقودالیلد را گوند؟ ۰
اشه ه تسم اول وفتح ئالی , گساهی‌است
بیان پانز دهم _
در
```


### [2026-09-07T01:44:59.540Z] TOOL RESULT

```
n 684
=== v2 leaf 434 (printed ~ 974 )
  ‫‪=4‬‬                                                                                                                   ‫روزی افرای‬

‫و« باشندة ده بعنی دهقان را هم‬                    ‫شهر است ‪۷‬‬          ‫روزی اقز ای ‪ -‬نام ماه چهارم باش‬
 ‫کفته‌اند که روستابی باشد ؛ ومعرب آن رستاق‬                                                     ‫اعهای ماکی بزدجردی ‪.‬‬
                                                                                                                  ‫امز‬
 ‫باشد (‪ -)۲‬وجمعیت‌ومجمم مردماترا نیز گوبند‬                          ‫روس = باالیمجپول بررزن‌بون(‪»)۱‬‬
                                                                    ‫نام ولابتی است در جالب شمال‪٩‬‏ ‪ -‬بمعنی رویاه‬
                                                ‫ومپمی دبگر ‪.‬‬        ‫هم‌آمده است ‪ - ۴‬وخرامیدن ‪ -‬وسبقت گرفتن ‪-‬‬
                                                                 
=== v2 leaf 435 (printed ~ 975 )
                                                                                                                                                    ‫‪1‬‬
                                                                                                                                                ‫‪TEE‬‏‬    ‫سح‬       ‫‪۴‬‬        ‫‪۳‬‬   ‫‪۴‬‬    ‫‪5‬‬
                                                                                                       ‫‪۱‬‬
                                                     ‫‪SSE‬‬     ‫‪5‬‬       ‫=‬           ‫‪3‬‬   ‫‪5‬‬        ‫‪۳۳‬‬           ‫‪۳‬‬   ‫‪gG‬‬       ‫‪aa‬‬         ‫‪77‬‬   ‫‪۷‬‬
                   ‫‪5‬‬
                       ‫=‬        ‫کب‬   ‫ات‬   ‫ها‬   ‫>‬
                                                                                 ‫‪۱‬‬             ‫‪۰ ۰‬‬                                      ‫‪۰14‬نی‬   ‫‪5‬‬         
=== v2 leaf 436 (printed ~ 976 )
            TL       LNLL
            EDIE 7777 SLL
                 ‎       ‫ر‬     IDL
                          IL۳ 7‫ک‬       E LDL
                                7 DID DLTI DD DSLL LS DD
                                                    LL BL, LL
                      SC        A    ATL                                              2
                           ‫ت‬‎   LS   MAE   ۸     1          >   ۳
            ۱   DLL
                                                                                          ‫رم‬   27 ‫رر‬
                                                                               2 ‫رم‬   ‫مد‬        , :        ۵   .
                                      ۱        ‫ له‬‎‫مق‬   1            ۱ ‫ط‬
                                                                    ‫رم‬     ۴              ES
                                                                         
=== v2 leaf 437 (printed ~ 977 )
‫روسه‬                                           ‫‪۱‬‬                                   ‫زا‬   ‫ی‬

                                                                        ‫بقبه از صفحٌ ‪4۷٩‬‏‬
‫وسیم نرارها اطلاق ميشد‪ .‬وآن در اروپا وآسیا از سواحل دربای بالتيك تاسواحل اقیالوی کبیر‬
 ‫ممتد بودوامروزه بجمهوری سوسیالیستی شوروی روس که قمت عمد اتحادبةٌ جماهیرسوسیالستی‬
 ‫شوروی‌را سکیل مبدهد()‪ ))/)/‬اطلاق‌شود وآن‌بمساحت ‪ ۰۰۸۷۹۰۷۹۱‬کیلومتر مرست و‪۳۱۱‬‬
‫و ‪100٥80‬‏ است وشهر های‌عمده‌عبار تنداز‪ :‬لنیتگر ا‪۳‬د‪ 48‬صن‪ 1‬عا‬ ‫آن‬‫متک‬ ‫ملیونسکنه‌داردوباشخ‬
‫رستف ‪ .۸ ۷050‬گر کی ‪ 161۲026۰‬اسوردلوسك ‪ .5۷0۱0۲6۷5‬ساراتف‪ ۷008۲3۹‬روسبه‌ارویا‬
‫هموار و دربعض مواضع دارای درباچه‌ها وباتلاق‌ها ودربرخی امکنه پوشیده از جنگلهاست و در‬
‫جتوب شرقی از استي‌حا مستور است ‪ .‬جبال عمده عبارتند از‪ :‬ففقاز و اورال [‪272‬ا()‪ .‬تیه های‬
‫والدائی ]‪ 20۱۵۷‬و ولگا ‪ . 281۵۷‬در میان شطها بابد یجورا ‪ 8102006۳‬دوین
```


## [2026-09-07T01:45:08.617Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\npages=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(428,442):\n    p=pages[i]\n    head=re.sub(r'\\s+',' ',p[:150])\n    print(i, i+540, '|', head)\nEOF"
}
```


### [2026-09-07T01:45:10.111Z] TOOL RESULT

```
428 968 |  ‫سره‬ ‫روان آورد‬ ‫داشن را فيز گویند ‪٩‬‏‬ 
429 969 |  ‫رود بار‬ ‫‪4‬‬ ‫لخت پپلوی است ومر کب است از روخ و چاو ‪-
430 970 |  ‫سه‬ ‫رودزم‬ ‫مفرد رود
431 971 |  ‫روز خوش‬ ‫‪-4۷۱-‬‬ ‫لش مد و او را در‬ ‫و غراشا
432 972 |  ‫‪“AYY‬‬ ‫روز خون‬ ‫معروف‌است کهزمانة نایدارباشد
433 973 |  ‫روز مریم‬ ‫‪avr‬‬ ‫باشد ‪.#‬‬ ‫رو
434 974 |  ‫‪=4‬‬ ‫روزی افرای‬ ‫و« باشندة ده
435 975 |  ‫‪
436 976 |  TL LNLL EDIE 7777 SLL ‎ ‫ر‬ IDL IL۳ 7‫ک‬ E LDL 
437 977 | ‫روسه‬ ‫‪۱‬‬ ‫زا‬ ‫ی‬ 
438 978 |  ‫ورف‬ ‫روش‬ ‫ننی هم هست یمنی روشن کن ‪- ۴‬‬ 
439 979 |  ‫روعن‬ ‫کشت‬ ‫‪۱۷‬‬ 
440 980 |  ‫هی ‪۷۹۳‬‬ ‫روغنای‬ 
441 981 |  ‫‪۷‬‬ ‫جشم امتت‪ .‬ء
```


## [2026-09-07T01:45:26.802Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\npages=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (431,432,433,438):\n    print('===== printed', i+540)\n    print(pages[i][:2600])\nEOF"
}
```


### [2026-09-07T01:45:28.134Z] TOOL RESULT

```
===== printed 971
     ‫روز خوش‬                                                                                           ‫‪-4۷۱-‬‬
      ‫لش مد و او را در‬   ‫و غراشان‬         ‫ویادشاهان(‪)۳‬‬
                                                           ‫رو ر ‪ -‬ممروفت و بعربی نهار وبوم‬
      ‫زمان دربان خوانند و روزبانان جمع ِ‬                  ‫فنتیاب همهت چنانکه گوبند‬     ‫آمع‬
                                                                                         ‫گوبند ‪ -‬وی‬
     ‫گا‪-‬هبان‪-‬‬
            ‫دربانان باشد‪ .‬وسر هنگه‪ -‬ووچانوش‬                ‫دروز برآهد» مرادآن باشدکه آفتاب برآهد ‪-‬‬
 ‫و شقیم را گوبند ‪ -‬و بمعتی جلاد هآمده‬                      ‫کونایه از ظاهر وآشکارا وروشن باشد ‪ -‬وبمعنی‬
                                             ‫است ‪. ۴‬‬       ‫روز کارهم هت ت که کنابه ازفرصتباشد چنانکه‬

‫دون وک خت ارم ین‬                                          ‫کونند « امروز روز فلالی استت» بعثی روز گار‬
                                                                            ‫‪.:‬‬   ‫ازو ات‬      ‫وفرصست‬        ‫قلالی است‬
‫بی غل‬       ‫ست‬
             ‫رو‬‫دست‬
                 ‫را‬             ‫د‬
                                ‫که‬‫متر‬
                                    ‫روشن رای اس‬
                                                           ‫واف بر وزن‬
                                                                    ‫رورافکن = با همزه ک‬
                           ‫وغش وصاف وپاك باشد ‪.‬‬
                                                          ‫چوبك زن » تب یکروز در میانرا کوبند یمنی‬
‫رور جاث؟ ه بکر الك و فتح جیم‬                              ‫تبیکه مکروز آید و بکروز نیاید وآن تب را‬
‫پانزدهم شعبان استت که روز‬         ‫» روز‬   ‫کاف‬   ‫وسکون‬
                                                                 ‫بعربی خغوبانند بکر غین لقطه دار ‪.‬‬
                                                           ‫رور امید لویم = کنابه از روز‬
‫بر ات‬   ‫وشب‬    ‫راشب‌جك‬   ‫این روز‬    ‫باشد وشب‬     ‫بررات‬
                                                     ‫ف‬


                                             ‫گوبند ‪.‬‬
                                                                                                      ‫قیامت است ‪.‬‬
‫رقطه دار‬      ‫صم خلی‬       ‫‪-‬‬    ‫خسب‬       ‫رور‬
                                                           ‫رور باراد = روق کار وبار گورمی‬
‫وسکون سين ب‌قطهوبای ابجد ۾ کنابه از کاهل‬
                                                         ‫روزیرا نیز کوبند که‬                ‫بازار باشد ‪ - ۴‬هور‬
                                                           ‫در یکجا مردم خرید و فروخت کنند ‪ 
===== printed 972
 ‫‪“AYY‬‬                                                                                                     ‫روز خون‬

‫معروف‌است کهزمانة نایدارباشد؟ ‪-‬ومدت‌وفرصترا‬                 ‫وور خون ‪ -‬بسکون الك ‪ .‬تاخت‬
                                                           ‫بردن در روز باشد بر سر غچنينمانکه ابشان‬
‫که‌آن چیز و آن کی در ان بوده باشد همحجو‬                    ‫بی‌خبر وغافل باشند ‪ -‬و عاخت بردن در شب را‬
‫تسغمیر و امثال آن ‪-‬‬          ‫روز کار جوالی و ِ‬                                                    ‫شبخون گوبند ‪.‬‬
            ‫ِ‪.‬‬     ‫وباکاف تازی روز جنکه راا‬                 ‫رورذاد = بدااد ابجد (‪ )۱‬بر وزن‬
                                                                    ‫هوشیار » خدمتکار وبند گانرا گویند ‪.‬‬
                         ‫واوقات ضایم کردن باشد ‪.‬‬            ‫رور در نگ بكر ات ک‪۰‬نابه‬
                  ‫رفتگان‬        ‫رور ګار‬                                                        ‫از روز قیامت باشد ‪.‬‬
                   ‫باشد ج‬   ‫ما حصلان‬     ‫بی‌دولتان وی‬       ‫ررورح = بسکون‌الت‪ .‬روشنیوشفافی‬
‫رور گرد = بسکون‌تالك وکاف فارسی‬                             ‫ونابه از سرخروی(‪)۲‬‬
                                                                             ‫وسرخی رومراکوبند ‪ -‬ک‬
‫مفتوح برا و دال بیط ژده ‪ ۰‬یکی از تامهای‬                                                                   ‫ه‬   ‫هم سس‬

                      ‫فآتاب عالمتاب است‬                     ‫رور سیاه = و روزسیه تکرئالت»‬
‫» کنابه‬     ‫كرالك‬‫کر‬         ‫روز کوشش‬                        ‫کنایه از روز بد ‪ -‬و روز ماتم ‪ -‬و روزنحس ‪-‬‬
                      ‫باشد ‪۰‬‬   ‫وحدال‬   ‫جنك‬     ‫ر‬
                                               ‫از رو ز‬                                  ‫آوزار وتشویش باشد ‪.‬‬
‫ر و و مظالم = بمعنی روز درنگ‬                                 ‫رود قراخ ‪ -‬بکر الك وفرااوی‬
 ‫باشد )‪(٩‬‏ ککنهابه از روز قیامت است (‪. )۷‬‬                   ‫بی‌نقطه(‪ )۳‬بالف کشیده و بخای شمه‌دار (‪ )6‬زده‪.‬‬

‫رودمه ‪ = ۴‬بامیم‌بروزن‌نوزده» بمعنی‬                          ‫کنایه ازبعد طلوع صبح است (ه) که ترديك‬
‫تاربح است و آن حاب نکاهداشتن سال و ماه‬
                                       ‫وروز باشد ‪4.‬‬

                      ‫(‪ )e‬چك‪ :‬ورا‪. ‎‬‬             ‫‪.‬‬   ‫‪ :‬سرخرولی‬      ‫(‪ )۲‬چك‬              ‫(‪ - )۱‬اسد‬
                                ‫‪ ۱:‬از یمد ازصبح طلوع است‬      ‫‏)‪ (e‬خم‪۷‬‬            ‫(‪ )4‬چك‪ :‬وبخا ‪.‬‬
                                   ‫(‪ )۷‬چك ‪ ,‬چش‪ :‬باشد ‪.‬‬                    ‫چش‪ :‬است‪. ‎‬‬       ‫‪,‬‬   ‫)‪ (٩‬چك‬


                                                 
===== printed 973
 ‫روز مریم‬                                                                           ‫‪avr‬‬
                                   ‫باشد ‪.#‬‬       ‫رور ننگ و نام ‪ - ۱‬بکراك‪‎.‬‬
                                                 ‫بمعنی روز کوشش است ککنهابه از ررز جنگ‬
‫وعم وسکون را وزا ودال ابجد‪ ,‬نام روزیتجشنیه‬     ‫وجدال وقتال و کینه خواستن باشد ‪ -‬و روز غنا‬
                                                   ‫ند‪.‬‬
                                                     ‫یام‬
                                                       ‫گهوون‬
                                                           ‫مزیشگ‬
                                                               ‫وساز وصحبت را یز رو‬
                                   ‫است ؟ ‪.‬‬
                                                  ‫نی‬
                                                   ‫نګ و فيرف»نش‬                    ‫رور‬
‫رود هریم ‪ -‬کنایه از خناموشی‬                              ‫وکوشش‬    ‫بر جنگ‬

‫وسکوت باشد؟ ‪ -‬کونابه از مرکهوموت حم‬             ‫رو ر نه ؟ د بفتح اول و تال و لون‬
                                   ‫‪4‬‬   ‫هت‬        ‫وسکون تانی ‪ ۰‬معروفت که مطلق‌سوراخ ومنقثة‬


  ‫‪۲‬شمار ‪۷‬‬
        ‫‪:‬وزن ‪»( ۳‬صمیر) «ارمغان سال ‪۱‬‬
                                   ‫از ر‬              ‫‪۴‬‬         ‫نك ولام ‪.‬‬
                                                                       ‫‪ -‬رك ‪:‬‬
  ‫معرب آن هم‌روزنة دنفس»‪ .‬اوسنا ‪« 301800231‬پورداود‪ .‬خرده‌اوستا ‪۲۱۲2۱‬‬           ‫عان ‪E‬‏‬
         ‫رك ‪:‬هرمز » هرمزد ‪-‬‬         ‫‪ - ۴‬دز اصطلاح ابرانیان باستان » روزاول هرماه شمسی‬
 ‫خطاب بمرم آمده ‪«:‬فقولی‬       ‫اشاره بروزة صمت مرربم‪" .‬درسورةٌ ‪٩۱‬‏ (مربم) ‪۷ 1‬‬       ‫‪۴‬‬

                                                ‫وتان من شر فیا کلام از‬
  ‫زی) از‪ :‬روز ‪( ۳-۰‬نیت)؛منسوب بروز‪:‬‬
                                  ‫کر‬‫ورسوم (در لهجةٌ م‬
                                                    ‫روزه ‪ -‬بضم‌اول ک‬
  ‫مکروزه » دو روزه ‪ -‬نخوردن و نیاشاه‌یدن ازسحر نا غروب (از اعمال دینی) ودرماه رمضان روزه‬
                                                     ‫داشتنمسلمانان را واجب است » صوم ‪.‬‬
  ‫‪ #‬روزی ‪ -‬بضم اول " از ‪ :‬روز ‪-۳‬ی (سبت) » پهلوی ‪)٥0۲‬‏ = ارمنی ع ‪61607‬‬
  ‫ر(زق یومیه) « هوبتمان ‪ > ۹۲۱‬دزفولی ‪ « 6120۲‬امام»؛ رزق » اصیب وقسمت و بهره و حط‪:‬‬
 ‫‪ ( ۳‬صیادی که ماهی دامرا ازدست او درربوده بوده دریاسخ معترض) گفت ‪ :‬ای برادر! چتوان کردن؟‬
  ‫لتان ‪ -۱۱۱‬خوراك هرروزه»غذا وطمام‪.‬‬
                                  ‫گ«‬‫مرا روزی نبود وماهی را همجنان روزی مانده بود »‬

                                                                            ‫بقی
===== printed 978
   ‫ورف‬                                                                                    ‫روش‬
‫ننی هم هست یمنی روشن کن ‪- ۴‬‬
                          ‫ممرعبدی‬
                                ‫وا‬            ‫‪ = ۱‬تح اول و کسر ثانی‬                ‫روش‬
        ‫و تندخوی و بدخلق را یز گفته اند‪.‬‬          ‫وسکون شین قطه‌دار » بممنی راه رفتن سوبقت‬
‫بوزن‬   ‫روشان ؟ ‪ -‬با ثانی مجهول‬                    ‫کرفتن‪ -‬ود رکذ تن رخرامیدن باشد‪ -‬وطرز(‪)۱‬‬
‫جوشان ‪ .‬بمعنی‌روشن است که ازروشنابی وفروع‬         ‫و ماد را یز کوند ت‬         ‫‪-‬ل‬
                                                                              ‫مث‬‫وئون‬
                                                                                   ‫وقامده وقا‬
                                                  ‫وخیابان وراه رو میان باغ را هم گفته‌الد‪ -‬وم‬
 ‫روشی ‪ = ۴‬باشمول بروکزونکن‪,‬‬                   ‫اول و امنجیهول ‪ .‬مخفف روشن باشد که از‬
‫بممنی روشنابی وفروغ باشد ‪ -‬کونابه از ظاهر‬         ‫روشنابی است‌چنانکه گویند «چشم شما روش»‪- ۳‬‬

                                                        ‫(‪ )۱‬چك » چش ‪ ۳:‬وعادت ‪.‬‬
           ‫رك ‪ :‬روشن ‪.‬‬    ‫‪۴‬‬       ‫‪ - ۱‬از ‪ :‬رو (رفتن) اش (ینوند اسم مصدر )‪..‬‬
  ‫‪ - ۴‬بپلوی ‪ » 85۵0۲‬اوستا ‪( 8110503۲ -‬صفت بمعنی‌روشن) « بارتولمه ‪› ۸۸4۱‬‬
   ‫وعم در اوستا‪( 087-8011502۲ 11011156-‬اسم است‌بمعنی روشنابی) «بارتولمه ‪۹۸8۱6 ۸۸4۱۰‬‬
   ‫دیب رک ‪ ۷۹۱۰۰‬افتانی م ‪ . 18۵05۵۲ ۵22۵۲۰‬باوچي ‪ 182۸815۵۲۰ . 12/5۵۳‬شغنی‬
       ‫(نور روز)‪ .‬منکلیجی ‪( 120150۲‬آنش) «اسنق ‪ ۱۳1‬ورك ‪ :‬هوبشمان اسا ‪.‬‬                  ‫‪58‬‬
                                                                             ‫بقیه از صفحة و‪٩۷‬‏‬
  ‫ونی و لیتوانی و قسمتی از لهستان را ازدست داد ‪ .‬بخشهای دیگراعیراطوری مزیور بتبع روسية‬
                                                  ‫شوروی تشکیل جمهوریهایی متحد باآن دادند‪.‬‬
                                                  ‫و ژوزفت‬   ‫در گذشت‬   ‫‪۶۲۹۱‬‬     ‫لن در‬

                                              ‫استالن ‪6811٩‬‏ ‪ .5.٥‬جاشن اکوردید ‪.‬‬
                                              ‫در ‪ ۰ ۹۳۹۱‬شوروبان ‪ ,‬بخش شرفی‬
                                               ‫لهستان و در ‪ ۰6۹۱‬قمتی از فتلادد ؛ رومالی‬
                                               ‫و جمهوری های باتىك را بتصرف آوردلد ‪.‬‬
                                                  ‫مورد حملهةٌ‬   ‫جماهیر شوروی در ‪۲۸ - ۱۸۹۱‬‬
                                                   ‫آلمانیان قرار کرفت و در جه دجرنگه‬
                                                  ‫بین المللی دوم وارد گردید و عاقبت تواست‬
```


## [2026-09-07T01:45:50.961Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\npages=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(pages):\n    if 'افروخت' in p or 'افروز' in p:\n        print('leaf',i,'printed≈',i-213)\n        import re\n        print(re.sub(r'\\s+',' ',p[:200]))\nEOF"
}
```


### [2026-09-07T01:45:52.802Z] TOOL RESULT

```
leaf 106 printed≈ -107
نود وهشت اسعر لی۱ -هرچند منظور مولف‌تدوین فرهنگ پارسی بوده است؛ معپذ| لغات‌عر بی بسیار در برهان آمده وشمارة آنها بیش ازلغات زبانپای دیگر است. ۱ بخشی از لغات‌عر بی مستقلا بعنوان لفت در جای‌خود نقل‌شده‌
leaf 182 printed≈ -31
دیایة مزف ۱۳۳۳ و چون « فروختن » مشتر لك بود هبان روشو ن کردن ویع نمودن و همحنین "دوختن» بان دوختن جامه ودوشیدن شیر» یس از فروختن بمعنی‌روشن کردن «می‌افروزو»! واز فروختن به‌عنی‌بیم کردن * میفروشد »وازد
leaf 203 printed≈ -10
له ۱ قواعد دستور واملاء پارسی فاد نهم » دد بیان توصف آ نجه صاحبان املاء دا ازدانستی آن گز بر نیست؛ واملاه درعرف ارباب کتابت عبارت‌است آزنوشتن حروف مفرده و مر کبه بر نهجی که اصحاب این فن تعیین کرده‌اند
leaf 214 printed≈ 1
آب ست آب دست ب بر وژن‌خاربست , امستجا کردن بآب - و وضو ساختن بائد - و زاهد پاکدامن را نیز گوبند - و کارکری را حم گفته‌انه که دست ار درکارها با طراوت باشد ۷ . آب دستان بر وژن آب دندان » بیمنی ابریق و آ
leaf 222 printed≈ 9
۱ آخن آب پرود ۱ ۱ اه کیره راگونند ؛ یمنی حرچی ز که بدان آش افروزند همچو خس و خاشالك-و مانند آن - و چتماق را نز کفتداند . # ]آتش پادسی (۲)- ه پکس رایع » مرضی است غبر آنفك مشهور آنرا بعربی تلر فارسی خوا
leaf 223 printed≈ 10
وا ثِ آ دامن وکاف ۰ بمننی آش زده اس ت که چنساق‌باشد . * ] نش آر « بفتح ی فرشت »کنابه از آ آش پر ود بتح بای ظرسی و راو | شراب لعلی باشد - و لب ممشوق را نیز گویشد . و سکون رای فرشت » کنامه از تسغ و شمشی
leaf 225 printed≈ 12
و مطیخی و آهنگر و امثال آنرایز کوند . * ۲ تشکدة بهر ام - کنایه از برج حمل باشد بواسطةٌ آنکه حمل خانة صویخ است ٩‏ #۶ ] تشگیره - هرچیز که بدان آتش توان بر‌داشت - و آنچه بدان آتش افروزند. اش اس تبگه ۳ ۰ 
leaf 231 printed≈ 18
رنه حهای نی وآن بودن آفتاب‌است در برج فوی - و نام روز نهم باشد از هر ماه شسی و بموجب رسم یکه میان فارسیان مقرر است که چون نام روز با نام ماه موافق آید آنروز را عید گیرند و آش خانها را بروبند و مزین کر
leaf 233 printed≈ 20
آآذد بردفی - نام آنشکده ششم است که در فاری برزین نام , شخصی از خلفای ابراهيم زردشت ٩‏ ساخته بود » و بحضی کویند روزی کیخرو سواره می َفت ناگاه صدای رعدی بهم رسید چنان مهیپ که کیخرو خود را از اسب انداخت 
leaf 235 printed≈ 22
آذرشپ - و " مرکق ۳ ۳ ] در شین « بکر شین وسکون نحتانی و نون . سمندر را گوند وآن جانورست که در آش متکون کردد ۴ ] دار طو س ه نم طای‌حطی کون واو وسین بی‌نقطه بمعنی | ذارطوس‌است که شوحر مادر عذرا باشد . ] 
leaf 285 printed≈ 72
.کنایه از آ غاب عالمتاب باشد . ] بنه اق و ز و آیینه افر ود - صیقل گر و روش نکر را کوبند » و آن شخصی باشد که چیزها را جلا دهد و صقل کند . 3 آینة چرخ و آینة چرخ - بععتی آبنهٌ آسمان ابت که کنابه از خورشد
leaf 316 printed≈ 103
لرسانیفون ارسانقون » با اك بالف کشیده و نون تحتانی رسیده و فاف مضموم بواو و نون زده » بلفت‌بونانی زرنبخ زردباشد وآن‌جوهرست کومتشد یامر ند هر هتکتی که از ان شخورد یمیید » ارس بز آن - بکر الث و ضم بای ا
leaf 363 printed≈ 150
افر اشتن بروزن ومعنی‌برداشتن: بلند ساختن باشد . افر اشته بروزث ومعنی برداشته‌و بطند ماخته و بالارده )۱( باشد ۰ ۱ فر دون - بفتح اول رانی‌وسکون‌نالث و کربای ابجد وبای حطی بواو رسیده و بنون زده , دوایی ا
leaf 364 printed≈ 151
آفری کشوث و نخم آنرا بذرالکشوث خوانند . فواق را تافع است . افری فتح اول وثانی بروزن سفری » مخفف آفرین است که دد مقام تصی نگوند . و بسکون انی هم درست است . افر یدون ‏ - فربدونباشد. واویادشاهی بوده. ءشه
leaf 389 printed≈ 176
اف او رفتی . بکشب بای شد و آتش را بکشت راندروی درمیان دربا کم کردید .. سین می‌نقطه , نام یکی از حکمای بونان است گوند درطبابت اعجاز مکاربردی ۴ نلم مکی از مبلوزان تورانیی است ۳ دوازده د بردست گر کین ملا
leaf 402 printed≈ 189
آوروختن آود و ختن ه بروزن و معنی افروخئن است. که روشن کردن: آنشس و چراغ باشد ۷ .: آوده » بفتح اول و ثاكك وسکون‌انی » بمعنی ابره است که روی فبا و کلاه و امثال ان باشد, چه درفارسی با و واو بهم نبد بل‌می
leaf 430 printed≈ 217
باد وح که جربی بادروج گویند ؛ د بسی کوبند بادرو تره‌ایست که بر کش بسپرغم میماند و بوی ترنج میدهد پاددوج - بسکون جیم .کل بتان افروز باشد و بویدن آن عطه آورد وکز دن عقرب را نافع باشد , و آثرا پعربی ضومر
leaf 461 printed≈ 248
مه از جرم و کناه و تفصیر و ا ز کشت نکسی کذشتن باشد .‏ بکشودن « بر رزن افزودن ؛ بمعنی رحم و شففت کردن باشد ۰ و بمععنی بخشیدن‌هم هست . 1۰ پخك « بکر اول و فتح ثالی و فا و سکون دال » بعنی عطسه کندچه خفید
leaf 478 printed≈ 265
می شیر آن" زین نهادن سرخ‌مرد گوبند و بعربی عصا الراعی خوانندا ۰ بر شیر فرد ین نهادن - کنابه از تهایت غالب شدن - و افزولی و زبادنی کردن بر صحر انهادن هه کنانه از آشکار و غلعر ساختن خاشد * بر صیصا ‌ مشپ
leaf 481 printed≈ 268
۳ بر گ ید - معروفست - و نوعی از پیکان تیر هم هست که آنرا بهیشت بر کك بید ساز ند . بر کردن بر وزن بروددن ۰ بمعنی حفظ کردن و بخاطر نگاهداشتن باشد - و کنابه از برافروختن آتش حم هست . بر کرسی نشاندن - کنا
leaf 485 printed≈ 272
۱۲ حسه برد ی ۰ این شممها که در دل بسحق بر فروخت از رهگذار نور(۱) برنج شماله بود ۴ . مخقف بر نج‌زار است که شالی‌زار باشد ۰ بر نجاسب بکسر اول وثالی وسکون کشیده و بسین بر نج کابلی - نغمی است دواییو آن می
leaf 498 printed≈ 285
بستان تم اول بروزن برهان » کلزار و کلسان‌را کوشد , ومشفف بوستان هم‌هت كِ و جابی‌را نیز کویند که میوه‌های‌خوشبوق‌در آنجا همرسد . پستان‌افرود - کلیات سرم‌رنگ و بی‌بوی که آنرا تاج خروس وگل بوسف نز کوبند 
leaf 607 printed≈ 394
-_۳۸۳ و ثالكث بتحنالی رسیده و واو مفتوح بنون ودال ابجد زده , بىني صریح باشد که در مقابل رمز وایماست . ۱ رس ح_بفتح اول بروزن‌دری, پردمرا کویند که بر روی چیز ها پوشند و از جاها آویزند . * پرسا! - بضم او
leaf 686 printed≈ 473
اسه واسه - دست دهد و صدای فس کشیدن و بر آ: وردن مردمان فربه - و می‌طویی 7 و یی دد پی افس زدن صردم و اسب و حیوان دیگر از کثرت کرما با لاش کردن و دوبدن ۷ - و بمعتی بیقراری هم حست . تاسه و اس سباواوبروزن
leaf 699 printed≈ 486
آحت‌سر اج بنتح سین. بی ضله ورای قرشت بالف کشیده بجیم زده , نام مدرسةٌ شیخ- ابواسحق‌کازرولی است؟ - کوبند شیخ در آن مدرسه چراغیبدست خود روشن کرده‌ادوا کنون چهارسدسال زباده‌باشد آن‌چراغ حمچنان‌افروخته اس
leaf 701 printed≈ 488
- و -ه توخته است که بمعنی ادا کرده و گزارده(۱)باشد اعم از قرض ودین وامات ونماز.* تختة او ل - کنابه از لوح محفوظ است٩‏ - و تیه اطفال را نیز کویندکه در آن الف با تا نویسند , نخحته یل س بارچه ای را گونند
leaf 704 printed≈ 491
بیان هشتم در تاي قرشت با ذال نقطه دار مشتمل برپنج لفت و کنایت تفج بفتح اول و ثانی وسکون رای تذرو زر یخ- کتابه از انکشت بی نقطه وجیم , معرب نذرو است» و آن هرغی و زغال افروخته باشد. ۱ اف کته تن وم ۳ ۱ ب
```


## [2026-09-07T01:46:03.404Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\npages=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(358,366):\n    print('=== leaf',i, '|', re.sub(r'\\s+',' ',pages[i][:160]))\nprint('---- full leaf 362 ----')\nprint(pages[362][:1500])\nEOF"
}
```


### [2026-09-07T01:46:04.750Z] TOOL RESULT

```
=== leaf 358 | اشو ی که کمانگران بر باژوی از جابدر رفته ‏ بندند واشق معربآشت . اشتاف مامثا بنتح اول و کسرفاه یعنی عصاره مامثا ومامیئا بلغت سربانی‌نام رستنی باشد که آنر! درفااض
=== leaf 359 | ۳و معتی امتضر است که قلمةٌ فاری باشد و آن که داراین داراب‌استت هاگن وتالابرا لس گویند . اصطر خ" س بروزن ومعنی استخراست که فلمة فارس ناشدب وتالابو آبگررا نز گوون
=== leaf 360 | وشطهای سیله دارد . ۱ نوعی ازبوی مادران باتد . گویند کترانیدن‌آن اطموط ‏ بنتم اول بر وزن مضوط , | درخانه گزندکان موذی را بکربزاند وآنرابعربی بمعنی اطماط است که ب
=== leaf 361 | فیاصر# روم ؛ او را ازآن جپت قصر گفتندکه مادرش بوفت ولادت عمرد 7 شکمش را بشکافتند و او را برآوردند و پزبان رومی اینچنین شخصی را قیسرخوانند٩‏ . و گویند عیسی علیه‌
=== leaf 362 | اتمون حمف خدایتمالی هم هست! - / لتیهاون » بعتح‌اول. دوابی‌است‌ممروف وآن شَكوفةٌ نبانی باشد که بسعتر می‌ماند و سر شاخپای آن بارمك است ۰ وطبع آن کرموخشاثه کوفت صر
=== leaf 363 | افر اشتن بروزن ومعنی‌برداشتن: بلند ساختن باشد . افر اشته بروزث ومعنی برداشته‌و بطند ماخته و بالارده )۱( باشد ۰ ۱ فر دون - بفتح اول رانی‌وسکون‌نالث و کربای ابجد 
=== leaf 364 | آفری کشوث و نخم آنرا بذرالکشوث خوانند . فواق را تافع است . افری فتح اول وثانی بروزن سفری » مخفف آفرین است که دد مقام تصی نگوند . و بسکون انی هم درست است . افر ی
=== leaf 365 | ات وافرا یمرن الیل خوالند . اسر ۵لن؟ « بر وزن افشردن » بمعنی سردشدن ویخ بستن ومنجمد کردیدن باشد - واز چیزی ‏ وکسی‌دل سرد شدن هم هست - آقتاب عالمتاب است . افسرسگ
---- full leaf 362 ----
اتمون
حمف خدایتمالی هم هست! -
/ لتیهاون » بعتح‌اول. دوابی‌است‌ممروف
وآن شَكوفةٌ نبانی باشد که بسعتر می‌ماند و سر
شاخپای آن بارمك است ۰ وطبع آن کرموخشاثه
کوفت صرع را نافع است ۰ و آنرا بعربی سبع
الثمرا خوانئد , وی کوبند زیر رومی است
وتیزطعم میباشد .
اقچ4 - بن اول بروزن بقچه , علامتی
است که در غله زار ها و کشت و زراعت بجهت
رمیدن مرغان ساژند . وبفتح اولعم گفته‌اند .
اقد فتح ارل و رای وسکون دال
ابچد » بممنی افتد است که شگفت
روا ماه تور گر ۳
وآن سورخ و:
و عجب
افدد » بر وزن صقذر ؛ برادر در را
وخواهرزاده تبزامده ات ۰
اقدستا » با تای قرخت بروزن‌مجلهاء
جمعتی افتدستاست که ستایش عجب و نبکو نرین
متایش - و حمد خدای عز وجل باشد بزبابن
پهلوی ۴‏
اقد‌یدن » بروزن فهمیدن . شگفتی
کردن وتعجب نمودن باشد ۴ .
اقر) - بر وزن صفرا ۰ بمعنی آفرین
ونحسین پاشه .
ار احت ‏ بر وزن پرداخت » یعنی
برداشت وبلند ساخت .
. رک : اد وافدستا‎ ٩
ب 30۸
اقفر اختن - بر وزن برداختن 4 بمعنی
برداشتن وبلشد ساختن باشد .
افر احته بر وزن برداخته ». نی
برداشته وبلند گردانیده .
/ فر ازه بر وزن برواز, بمعنی‌بلندی
وبلند باشد - وامربدین معنی هم‌هست بعنی‌بردار
وبلند ساز - واسم فاعل هم آمده ات که بلنف
کننده باشد - و عنبر خطیبان را هم گویند -
ویمعنی جمم‌باشد که در مفابل فرد است - ویسته
و کشاده وبین شده را نیز گومند - ویمعنی‌قریب
وترديك وپیش باشد - وغشیب را هم کنته‌اند که
درمقابل فراز است - وبمعنی آزین باز و بعد از
این هم هست - و سر کش و سر کشیده را نیز
«ک تفت وا بینی آت تتال هم آمده است .
افر از بدن بمعئی ‏ بلند ساختن
و افراختن باشد - وبمعنی آراستن و زب دادن
وخوش کردن هم مده است .
افر اس س پروزن کربای . خیمه‌وفناث
را گویند ۰
بمعنی سواران
```


## [2026-09-07T01:46:23.802Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\npages=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(pages[363])\nEOF"
}
```


### [2026-09-07T01:46:25.012Z] TOOL RESULT

```
افر اشتن بروزن ومعنی‌برداشتن: بلند
ساختن باشد .
افر اشته بروزث ومعنی برداشته‌و بطند
ماخته و بالارده )۱( باشد ۰
۱ فر دون - بفتح اول رانی‌وسکون‌نالث
و کربای ابجد وبای حطی بواو رسیده و بنون
زده , دوایی اس تکه آنرا قرفیون کوبند . ا کر
کزند کی جانوران را نانع است .
که آنرا بشیرازی بالنگوی خوورو (۲گوبند .
ء اس را نافع است ۳
نام شهرست که نوشیروان آ ادکرده بود در کتار
دربای مصی » و مادر عثرا از آن شهر است ۱ -
وم ولایتی‌است از زنگبا - وم زمینی ه‌هست
در بلاد غرب ۰
ارف » بروزن فرزند ۰ فر و نیکوبی
وزیبایی وحشمت باشد؟ .
افر ندیدن مصدر افرید است بعنی
زب دادن وزشت کردن وآراستن .
افر نگ . بروژن و معنی اورنگت لست
تخت پادشاهان باشد - وبمعثی فر وفکوبی
کون که بمربی صاری‌خوانند؟ .
49 چث : (- شده .
۱ -ظ , معرب افرنگه.
۲ ۱۳
افر و خشن؟ « بروزن اندوختن بسعنی
روئن کردن آتش رچراغ باشد .
افر ود بر وزن سردوز . بممنی
روشن و روشن کردن باشد - و روشن کننده را
نز گویند - وامر بدین‌معنی م‌عست بمنی‌روشن
کن ویفروز . *
افر وسا لین باین بالف کشیدم و کس
لام وبای‌حطی بتحتانی رسیده وبنون زده ؛ بلخت
بونانی6 سنکی است که آنرا حربی حجر القمر
خوانند ؛ وآن سفید وشفاف میباشد ودر شبهای
افرونی ماه می‌بابند , اگر بر گردن‌مصروعبندند
شفا باید .
افر و شه۱ ۳ بفتح اول وشن شطمرار .
نام حلوابی است. وآن چنان باش دکه‌آرد وروغن
را باهم بيامیز ند وبدست بعالند تلدانه داله گُردده
آنگاه در بائیلی کنند وصل‌درآن ریزندوبربالای
آش هند نا يك بیزد و سخت شود - و بحنی
گوند نان‌خورشی‌است د رکیلان. و آن‌چنانباشد
که زرد؛ تخم مرغ را در شیی خم ریزند و يك
برهم زند ویربالای آاش نهند ۴ شیرمانند دلمه
بىته شود بعد از آن شیرینی داخل آن سازند
ونان را درآن تربت کنند با خشکه پلاو در آن
ریزید و با قاشق خورند - وحلوای کندم دلیده
شده - ولوژیشه را فیزافروشه گوبند .
افروغ « بنتح‌اول. بسنی‌فروخ‌ودوشنی
وفابش وپرنو باشد اعم‌از دوشنی‌وپرنو فتاب وعاء
و آش و امثال آن :
۱ فر هنج ه بغع‌اول واكوها وسکون
(۲) چك : خرد .
۵ افروزیدن - رکه : افروختن .
۱ رک : آفروشه .
```


## [2026-09-07T01:46:36.814Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\npages=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(309,318):\n    print('=== leaf',i,'|',re.sub(r'\\s+',' ',pages[i][:180]))\nEOF"
}
```


### [2026-09-07T01:46:38.001Z] TOOL RESULT

```
=== leaf 309 | خوانندش, وبعض ی کویند منسوب‌باردیل‌ین ارمنین است وتا کردة اوست . اردجان س با جیم بر وزن همزبان» از جد اول اهل نجوم است و در احکام مرقوم. ار دش 7 س بفتح اول و ثانی وضم‌دال می نفطه و
=== leaf 310 | اردشیران " قهر وخشم یز آمده است٩‏ ؛ و فلم پسر ساسان این همن که اول ماسانان بوده ات و او را اردشیر بایکان میگفته اند ۰ واک‌لسره ابشان اند - و تلم پسر شیروبه بن پرویز هم هست - و کی ر
=== leaf 311 | آردسهشت او س باکاف‌فارسی بروزن‌پهلوان, بمعئی اردجان است و ها ور سرار ۳ و 4 بر از جداول و اشکال و ! وباکاف تازی‌نام موضعی است ونام دهی است از ی ار دم بفتح اول و الك و سکون‌نانی و می
=== leaf 312 | بخشایش » بمعنی خیر و خیرات و چیزی در راه خدا بمردم دادن باشد . . اددانی معروف است که فقیض گرانی باشد ۵ - ومردم دروش و فقیر ومستحق را نیز گونند - و بمعنی ملم بتشدید لام هم امده اسمت
=== leaf 313 | مه موم ما ی > ج با کل فا درل مخرفا اردو
=== leaf 314 | آردو ت برابر نا سس ۳ص اس ای دیس ۳۳ سذ الفبای ار دو ۳ کیت لا 2 غ ۹ | کیت عرلا ف ف‌ ِ؛ ت | نا 98 ات 42 ات 4و ك 7 ار ۳ ‌ ۰ ۷ ی ی ژا خر سر و ۱ ول و ۷ ا(زم ؛ ساح خزطعرر ۸ ۳ اج باه | ارف
=== leaf 315 | شراب است - و حبایی را نیز کوبند که بردوی شراب بهم رسد - و کو کب و ستاره - و شرارةٌ آش را نز کفته اند . ارژ نگ ۱ »با زای فارسی بر وزن و معتی ارشگه امت که نکار خانةٌ حانی نفاش باشد .
=== leaf 316 | لرسانیفون ارسانقون » با اك بالف کشیده و نون تحتانی رسیده و فاف مضموم بواو و نون زده » بلفت‌بونانی زرنبخ زردباشد وآن‌جوهرست کومتشد یامر ند هر هتکتی که از ان شخورد یمیید » ارس بز آن 
=== leaf 317 | وا ۱ ارغاب جمیم گزندکان بگرایزند و آرا ازطاعاسیا وار طمسا دز خوانئد محذف نحتانی . ارطی - بنتح او و طایحطی وسکون انی و محتانی ۰ بلفت رومی‌درخت وزاه را گوشد که پده است و بمربی غرب خو
```


## [2026-09-07T01:46:48.395Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSF درفش ===\"; grep -n \"درفش\" FSF_pages.txt | head -10\necho \"=== FSF رخش ===\"; grep -n \"رخش\\b\\|درخش\" FSF_pages.txt | head -10\necho \"=== FSF page tags near hits ===\"; python3 - <<'EOF'\nimport re\npages=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('n',len(pages))\nfor i,p in enumerate(pages):\n    if 'درفش' in p:\n        print('leaf',i,'|',re.sub(r'\\s+',' ',p[:300]))\nEOF"
}
```


### [2026-09-07T01:46:49.807Z] TOOL RESULT

```
=== FSF درفش ===
1983:                                                                            ‫‪- ۲‬پرچم» درفش‪:‬‬
1993:                                                   ‫بالای درفش می‌زدند خود درفش راهم‬
2087:     ‫«اروند‪ :‬دو معنی دارد اول رود دجله‪...‬‬              ‫پس آن بیدرفش پلید و سترگ‬
3120:       ‫بسست این فخر و این اورنگ شهرا‬              ‫درفشان شود فر و آورند تو‬
3724:                    ‫درفشیدن تیغ‌های بنفش‬
3726: ‫چو بینید باکاویانی درفش‬
3892: ‫یکی گرگ پیکر درفشی به دست‪.‬‬                     ‫به مه بر سر وه بیج برشتنگ سخت‬
3933:           ‫چو از پیش او کینه‌ور بی‌درفش‬                      ‫زفتار اوی‬
3935:‫سوی بلخ بامی کشیدش درفش‬                         ‫برافروخت پژمرده رخسار او‬
4522:                                                            ‫مشت هرگز کی برآید با درفش‬
=== FSF رخش ===
488: ‫همرنگ آب‪ .‬به معنی مسجازی‪ :‬درخشان‪:‬‬                      ‫(‪ -‬پرویز ‪)۷۲۰۱‬‬
1069:‫بهآسانی و رنج و سودو زیان‬                          ‫رخش بی‌رنگ و پیشانی پرآژنگ‬
1163:‫رخش پژمریده دل آشفته دید‬                                                             ‫آسیمه‬
2847:           ‫برانگیخت آن رخش رویینه سم‬
3376:            ‫نشست از بر رخش رستم چ‬                 ‫از فخر گرگانی (‪۵۶۱-۵۴‬و ‪:)۱۶۲-۶۳۱‬‬
3612: ‫به رخش اندر آیمشوم باز جای‬                          ‫(‪)۱-۲۷۱-۱۶۵‬‬
3925:‫درخشان» صفت و عنوان شهر بلخ‪ .‬پهلوی‬                                         ‫(مسعوف ‪:)۱۶۴‬‬
4218: ‫هم از روزگار درخشنده‌ام‬                            ‫به هر سوکهرستم برافگند رخش‬
5573:           ‫«نازکی‪ .‬نرمی نیکویی» (م‬                                  ‫در توصیف رخش رستم‪:‬‬
6757:            ‫درخشنده زرین یکی باره بود‬                   ‫‪-۲‬به معنی‪ :‬پیشامد بد بلاو آفت‪:‬‬
=== FSF page tags near hits ===
n 485
leaf 48 |  ‫رگژونگ‬ ‫اارتن‬ ‫اخته (بازابورل)‬ ‫نگیخت ابلق زجای‬ ‫رتاو‬ ‫ببگف‬ ‫=آخته‪ :‬بیرون کشیده
leaf 50 |  ‫آزوند‬ ‫از اسدی ( گرشاسب‌نامه ‪:)۷۳۱-۴۷‬‬ ‫این همان سزاوار و مستحق دستگیری و‬ ‫هوا هست ارمیده باد از نهاد‬ ‫ته شد‪.‬‬ ‫فیش‬ ‫گر پ‬ 
leaf 68 | ‫اوژن‬ ‫‪1۵‬‬ ‫جهان خرم از فر و اورند اوی‬ ‫است‪:‬‬ ‫جیس‬ ‫رو‬‫بوش‬ 
leaf 81 |  ‫‪۷۸‬‬ ‫بازارگاه‬ ‫مرآن نامور پهلوان را تونام‬ ‫نیرو قودرت برمی‌آید‪:‬‬ ‫شوی بازجویی فرستی پیام‬ ‫شدند انجمن دیو بسیا
leaf 84 |  ‫بالیدن‬ ‫نگ باهستقبال او [‬ ‫سیک‬ ‫رتا‬‫فخود‬ ‫و‬ ‫سروست آن یا بالاء ماهست آن یاروی‬ ‫طاهر] بازشد و بریکی بالا بایستاد تا‬ ‫ن‪ .‬خالست آن یاگوی‬ ‫ایا‬ ‫وگآن‬ ‫چ
leaf 85 |  ‫بالین‬ ‫بام‬ ‫ببالید بر سان سرو سهی‬ ‫بامداد‪ .‬صبح‪:‬‬ ‫همی تافت زو فر شأهنشهی‬ ‫چو اگه شد از کار دستان 
leaf 97 |  ‫برآن بودن‬ ‫به شبگیر هنگام بانگ خروس‬ ‫‪ ...‬برآمد برین نیز یک چندگاه‪...‬‬ ‫ووس‬ ‫برآمد خروشیدن بوق ک‬ ‫(‪)۱-۷۱۰۱-۲۷۴‬‬ ‫(‪)۲-۸-۵۲‬‬ 
leaf 110 |  ‫هر آن کز میان باره انگیزند‬ ‫زیر دینار و ياقوت و مشک و عبیر‬ ‫بگرداندش پشت و بگریزند‬ ‫ز دیبای زربفت و چسینی حریر‬ ‫من او را دهم دختر خویش را‬ ‫(‪)۱-۶۵۱-۲۰۲‬‬ ‫سپارم بدو لشکر خویش را‬ 
leaf 115 |  ‫بنیاد‬ ‫‪-۳‬گوهر نژاد‪:‬‬ ‫ننمرد مرد‬ ‫جنوشها‪ .‬ا‬ ‫ارا‬ 
leaf 117 |  ‫بوش‬ ‫گهر بافته پیکر و بوم زر‬ ‫درفشان چو خورشید تاج و کمر‬ ‫به روم اندرون بود یکچند بوس‬ ‫(‪)۵-۴۳۱-۵۵۸‬‬ ‫(‪:)۶-۲۸۳-۵۲‬‬ ‫‪-
leaf 147 |  ‫‪۴۴‬‬ ‫پرنداور‬ ‫پروپا‬ ‫نبرد تو خواهد همی شاه هند‬ ‫به«پای و پر» نگاهکنید‪:‬‬ ‫به تیر کومان و به هندی پرند‬ 
leaf 151 |  ‫‪۱۳۸‬‬ ‫دایه را بجای‬ ‫ویس‬ ‫‪:)۷۸۱-‬‬ ‫(ویس‪۴ .‬‬ ‫همان نیز هست‬ ‫ریش‬ ‫آن ک‬ 
leaf 161 |  ‫‪1۵۸‬‬ ‫پیخاره‬ ‫پیکان‬ ‫خسرو بترخت پیشگاه نشسته‬ ‫نوک آهنین و تیز نیزه و تیر‪:‬‬ ‫شاه ملوک جهان‪ .‬امیر خراسان‬
leaf 169 |  ‫‪1۹‬‬ ‫تاختن‬ ‫(ناصر ‪:)-۴۳‬‬ ‫که باشد بدو فره ایزدی‬ ‫ز آتش حرص و آز و هیزم مکر‬ ‫بتابد ز دیهیم او ببخردی‬ ‫دل نگهدار و چون تنور متاب‬ 
leaf 195 |  ‫جاکروز‬ ‫جوان با تخوار سراینده گفت‬ ‫همی ریخت خون و همی کند خاک‬ ‫که هرچت بپرسم نباید نهفت‬ ‫همه جامۀ خسروی کرد چاک‬ ‫)‪(۴-1۴-44۴‬‬ 
leaf 234 |  ‫درفشی‬ ‫(در لغت شهنامة عبدالقادر واه درشت به‬ ‫کوه برود و آن دو را اسیرکندو نزد طوس‬ ‫هیچ معنی نیامده است)‬ ‫بیاورد‪ .‬بسهرام به بالا می‌رود و فرود را‬ ‫درفشان (بر وزن درخشان)‬ ‫می‌شناسد‪ .‬فرودپهلوانان ایرانرابهخان خود‬ ‫=رخشیدن 
leaf 235 |  ‫‪۳۳۲‬‬ ‫درفشیدن‬ ‫گان‬ ‫ررد‬ ‫ای م‬ ‫ادزیک‬ ‫بآم‬ ‫که‬ 
leaf 255 |  ‫‪Yar‬‬ ‫دیزه‪‎‬‬ ‫فرهنگ بهدینان)‪:‬‬ ‫معنی دراز کردن به درازا کشیدن]‪ :‬دیرپاء‬ ‫(دقیقی ‪:)۶-۸۶-۰۵‬‬ 
leaf 290 |  ‫برینگونه چون شاه لشکر بساخت‬ ‫ساج‬ ‫به گردون کلاه کیی برفراخت‬ ‫«معرب ساگ» (رشیدی) درختی راست‬ ‫(م‪)۷۴۲-۳۰۲-‬‬ ‫مریه‌نردوید‪:‬‬ ‫شهت
leaf 298 |  ‫‪۳۹۵‬‬ ‫از انديشة خرد و شاه سترگ‬ ‫(ویس ‪:)۹۴۲-۹۳۱‬‬ ‫بیامد به ما برزیانی بزرگ‬ ‫چه خوش باشد به خلوت باده خوردن‬ ‫(‪)۳-۱۷۱-۶۱۶۲‬‬ ‫به
leaf 315 |  ‫‪۲۳‬‬ ‫شبرنگگ‬ ‫عاشقی را کهچنینباد؛شبگیر دهند‬ ‫بگفت و برانگیخت شبدیز را‬ ‫کافر عشق بودگرنشود باده‌پرست‬ ‫بداد ارمیدن دل تيز را‬ 
leaf 339 |  ‫‪۳۳۹‬‬ ‫فراز آمدن بکراری یا جیزی‬ ‫بلند کردن‪ .‬از‬ ‫شیدن‬ ‫کلا‬ ‫‪- ۱‬بالا بردن با‬ ‫ازنقل معناو بیت شاهد از فرهنگ‬ ‫همین ریشه‪ :‬فراختن‪ .‬افراختن‪ .‬ف
leaf 350 |  ‫قماری‬ ‫‪۳۳۷‬‬ ‫اندر آن ریو نیز‬ ‫برسات‬ ‫بان‬ ‫می‬ ‫قسیس (با زیر اول و تشدید سین)‬ ‫همی زان نبردش سرآمد فقیز‬ 
leaf 357 |  ‫‪raf‬‬ ‫کافته‪ .‬کفته‪ .‬کنیده‬ ‫تا ای خو چاو‬ ‫چک‬ ‫کی‬ ‫من اکنون ز طبعم بهار آورم‬ ‫مر کے کک ن‬ ‫م
leaf 408 |  ‫گوهر ‪-‬گهر‪:‬‬ ‫‪۴۰۵‬‬ ‫پباهلیز چون بر کشد سرو شاخ‬ ‫چو شد دشث ابوراه انوس‬ ‫خ‬ ‫از‬‫کآید‬ ‫سر شاخ سبزش بر‬ ‫پراگنده گشتند کامومن و طوس‬ ‫به بالای او شاد باشد درخت‬ 
leaf 420 |  ‫‪۳۷‬‬ ‫تو رااین تن یکی خانة سپنجست‬ ‫رنگ این خناکم‌ریاذ‌ککرنند ولی از بیت‬ ‫مزور بل مغربل چون کباره‬ ‫زیر روشن است کهمعصفر به‌معنی زرد‬ ‫(کباره =لانۀ زنبور سبد)‬ 
leaf 421 |  ‫مگرداد‬ ‫ز شادی برو آفرین کرد سخت‬ ‫(اسدی ‪:)۰۲۴-۷۶‬‬ ‫که از تو مگرداد جاوید بخت‬ ‫بهیزدانکهبنشینم آنگه ز پای‬ ‫(‪۵-۱۲۱-
leaf 433 |  ‫‪fr.‬‬ ‫ناساز‬ ‫می‌بیاور که ننازد بهگل باغ جهان‬ ‫می‌فر ستد که مرا راه ده تااز کشورت به‬ ‫هر که غارتگری باد خزانی دانست‬ ‫سرزمین دیگری بروم‪ .‬افراسیاب به‬ 
leaf 447 |  ‫‪۴۴‬‬ ‫نواکردن‬ ‫(اسدی ‪:)۷۰۴-۳۰۱‬‬ ‫[زال] سواری بکهابل بر افگند زود‬ ‫درفش سران‬ ‫فشان‬ ‫راز‬ ‫هدوا‬ 
leaf 449 |  ‫‪۳۴۹‬‬ ‫نوشتن‪ .‬برنوشتن‪ .‬اندر نوشتن‪ ,‬درنوشتن‬ ‫کردن پیچیدن‪:‬‬ ‫ز رنج و ز بدشان نبد آگهی‬ ‫بدا کالما داد زین‬ ‫ميان بسته دیوان به سان رهی‬ ‫همی برنوشتن
leaf 479 |  ‫‪۳۷۹‬‬ ‫پارمند‬ ‫یاره‬ ‫‪+‬ستن [پساوند‬ ‫)ا]‬ ‫دخار‬
```


## [2026-09-07T01:47:00.740Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\npages=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (178,179,180,181,234,235):\n    print('=== leaf',i,'|',re.sub(r'\\s+',' ',pages[i][:400]))\nEOF"
}
```


### [2026-09-07T01:47:01.893Z] TOOL RESULT

```
=== leaf 178 |  ‫‪۱۷۵‬‬ ‫رسم سرای سپنج‬ ‫بفرمود تا جهن رزم آزمای‬ ‫یکی زو تن‌آسان و دیگر به‌رنج‬ ‫رود با تگینان لشکر زجای‬ ‫(‪)۲-۸۶۱-۲۲۶‬‬ ‫(‪)۵-۰۸۲-۲۵۷‬‬ ‫(اسدی ‪:)۸۹۱-۰۲‬‬ ‫(دقیق
=== leaf 179 |  ‫‪۹۳۷۱‬‬ ‫تناور‬ ‫لش)‬ ‫و پی‬ ‫ا(با‬ ‫تند‬ ‫در شاهنامه گاه نیز به جای تن‌آسانی‬ ‫بلندی‪ .‬پشته تپه‪:‬‬ ‫«تن 
=== leaf 180 |  ‫هم از بیخ ار خاستی کیمیا‬ ‫تن (بتنگ) اندرآمدن‬ ‫بدی برگ اوچشم را توتیا‬ ‫بسیار نزدیک شدن‪:‬‬ ‫(حافظ ‪:)۵۱۴‬‬ ‫اگر شب رسی روز را باز گرد‬ ‫هرکس که گفت خاک در دوست توتیاست‬ ‫بگویش که تنگ اندر آمد نبرد‬ ‫گو این سخن معاینه در چشم مابگو‬ ‫(‪)۲-۶۹۱
=== leaf 181 |  ‫‪۱۷۸‬‬ ‫نود‬ ‫‪- ۴‬سگالیدن‪ ,‬کردن‪:‬‬ ‫برو توز پوشیده از مشک ناز‬ ‫ندانی همی جز بد آموختن‬ ‫(‪)۱-۷۵۱-۸۱۳‬‬ ‫گسستن نزیکی بدی توختن‬ ‫مان و موی‬ 
=== leaf 234 |  ‫درفشی‬ ‫(در لغت شهنامة عبدالقادر واه درشت به‬ ‫کوه برود و آن دو را اسیرکندو نزد طوس‬ ‫هیچ معنی نیامده است)‬ ‫بیاورد‪ .‬بسهرام به بالا می‌رود و فرود را‬ ‫درفشان (بر وزن درخشان)‬ ‫می‌شناسد‪ .‬فرودپهلوانان ایرانرابهخان خود‬ ‫=رخشیدن ]‪:‬‬ ‫[صفت فاعلی از درفشیدن د‬ ‫دعوت می‌کند و به طوس پیام می‌فرستد که‬ 
=== leaf 235 |  ‫‪۳۳۲‬‬ ‫درفشیدن‬ ‫گان‬ ‫ررد‬ ‫ای م‬ ‫ادزیک‬ ‫بآم‬ ‫که‬ ‫زبان گبشرایند بر من مهان‬ ‫گان‬ ‫ربه‬ ‫اشد‬ ‫یننفرو‬
```


## [2026-09-07T01:47:16.183Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN luster ===\"; grep -n -i \"lustre, luster\\|luster, lustre\\|^lustre\\|lustrum\" KLN_1966.txt | head -10\necho \"=== KLN illustrate ===\"; grep -n -i \"illustrate\" KLN_1966.txt | head -5\necho \"=== KLN light (n) ===\"; grep -n -i \"leuhtam\\|leuhta-\\|liuhtam\" KLN_1966.txt AHD_watkins1985.txt SKT.txt | head -10\necho \"=== LAT lustro ===\"; grep -n -i \"lustro\\|lustrum\" LAT.txt | head -10\necho \"=== LEW lumen/luna ===\"; grep -n -i \"lumen\\b\" LEW_1910.txt | head -5"
}
```


### [2026-09-07T01:47:16.313Z] TOOL RESULT

```
=== KLN luster ===
21695:ligature,  n.,  anything  that  serves  for  binding;  a cord  used  for  tying  up  an  artery  (surg.)  —  F.,  fr. Late  L.  ligatura,  ‘a  band’,  fr.  L.  ligatus,  pp.  of ligare.  See  ligament  and  -ure. light,  n.,  brightness.  —  ME.  liht,  light,  fr.  OE. leoht,  rel.  to  OS.  lioht,  OFris.  liacht,  MDu.  lucht, liecht,  licht,  Du.  licht,  OHG.  lioht,  MHG.  lieht, G.  Licht,  Goth,  liuhajt,  ‘light’,  ON.  Ijdmi,  OE.  le- oma,  ‘ray  oflight,  radiance’,  ON.  //or,  ‘light’,  ON. Ipsa,  OE.  liexan,  ‘to  shine’,  fr.  I.-E.  base  *leuq-, ‘to  emit  light,  to  shine;  bright’,  whence  also  OI. rocate,  ‘shines’,  rdkdh,  ‘light’,  rocanah,  Avestic raocant-,  ‘shining’,  raoxshna-,  ‘shining,  bright', Arm.  bis,  ‘light’,  lusin,  ‘moon’,  Gk.  Xeuy.6?, ‘bright,  shining,  white',  Xir/vo;,  ‘lamp’,  Xoua- aov,  ‘the  white  pith  of  the  fir  tree’,  ap-tpi-XiixT], ‘twilight’,  L.  lucere,  ‘to  shine’,  lux,  gen.  lucis, ‘light’,  lucidus,  ‘full  of  Ught,  clear,  bright’,  lu- cerna,  ‘light,  lamp’,  lucubrate,  ‘to  work  by lamplight’,  liicus,  ‘grove,  thicket’  (orig.  'an  open place  in  the  wood’),  lumen  (for  *!cuqs-men  or *louqs-men ),  ‘light’,  liina( for  *louqs-na),  ‘moon’, lustrum,  ‘a  purificatory  sacrifice;  a  period  of five  years’,  lustrare,  ‘to  purify  by  an  offering’, Gaul.  Leucetius,  surname  of  Mars,  L.  Liicetius, surname  of  Jupiter,  Lucetia,  surname  of  Juno, OSlav.  luil,  ‘light’,  luia,  ‘ray’,  Lith.  laukas.
21696:‘pale’,OPruss.  /ou.w«(pl.)‘stars’,W.  Hug,  ‘gleam, glimmer’,  OIr.  luach,  ‘white’,  loche,  ‘lightning’, luchair ,  ‘brightness,  luster’,  Mir.  luan.  Ion, ‘moon’,  Toch.  A  luk-,  ‘to  shine’,  A  lok,  B  lauke ‘far  away’,  Hitt,  lukezi,  lukzi,  ‘is  bright’.  Base *leuq-,  ‘to  be  light,  to  shine’,  is  identical  with base  *leuq-,  ‘to  see,  behold’,  whence  OI.  Ideate, lokate,  ‘sees,  perceives’,  locayati,  lokayati,  ‘re¬ gards,  looks  at’,  Toch.  A  Idk-,  B  lyk-,  to  see , Gk.  Xeiloceiv  (for  *Xsu>u£iv),  ‘to  look  at,  see’, W.  am-lwg,  ‘conspicuous’,  Lith.  laukti,  ‘to  wait’. Cp.  lea,  ‘a  track  of  open  country’,  leuco-,  levin, link,  ‘torch’,  loka, low, ‘blaze’,  luce,  lucent, lucid, Lucifer,  Lucius,  lucubrate,  luculent,  lucule,  lucus a  non  lucendo,  lucem,  Lucy,  luminous,  lunar, lunation,  lime,  luster,  ‘gloss’,  lustrum,  lux,  Luzu- la,  Lychnis,  lynx.
22345:luster,  lustre,  n.,  a  lustrum.  —  L.  lustrum.  See
22346:lustrum.
22347:luster,  lustre,  n.,  gloss,  radiance.  —  MF.  (  — F.) lustre,  fr.  It.  lustro,  fr.  lustrare,  ‘to  light,  illu minate’,  fr.  L.  lustrare,  ‘to  light,  illuminate’.  See lustrum.
22350:Derivative :  luster ,  lustre,  tr.  v.,  to  render  lustrous, lustral,  adj.,  pertaining  to  purification.  —  L.  lus- tralis,  ‘pertaining  to  purification  from  guilt,  ex¬ piatory,  propitiatory’,  fr.  lustrum.  See  lustrum and  adj.  suff.  -al.
22351:lustrate,  tr.  v.,  to  purify  from  guilt.  —  L.  lust  ra¬ ins,  pp.  of  lustrare,  ‘to  purify  from  guilt’,  fr. lustrum.  See  lustrum  and  verbal  suff.  -ate. lustration,  n.,  purification  from  guilt.  —  L.  liis- t ratio,  gen.  -onis,  ‘purification  from  guilt’,  fr. lustra  tits,  pp.  of  lustrare.  See  prec.  word  and  -ion. lustring,  n.,  a  silk  fabric  with  glossy  finish.  —  F. lustrine,  fr.  It.  lustrino,  fr.  lustra,  fr.  lustrare,  ‘to light,  illuminate’.  See  luster,  ‘gloss,  radiance’, and  cp.  lutestring.
22353:Derivatives:  lustrous-ly,  adv.,  lustrous-ness,  n. lustrum,  luster,  n.,  1)  purification  of  the  Roman people  after  the  census  every  five  years;  2)  a period  of  five  years.  —  L.  lustrum,  ‘purificatory sacrifice  made  once  in  five  years;  a  period  of five  years’  (whence  lustrare,  ‘to  purify  from guilt’),  for  *leuqs-lrom,  *louqs-trom,  prop,  ‘illu¬ mination’,  fr.  I.-E.  base  *leuq-,  ‘to  emit  light,  to shine;  bright’;  see  light,  ‘brightness’,  and  cp. illustrious.  The  various  phases  of  the  sense  devel¬ opment  of  lustrum  may  prob.  be  as  follows :  ‘illu¬ mination,  inspection,  review,  mustering,  expia¬ tory  offering,  expiation’.  Accordingly  the  verbs lustrare,  ‘to  light,  illuminate’,  and  lustrare,  ‘to purify  from  guilt’,  are  identical, lutanist,  n.,  a  lute  player.  —  ML.  lutanista,  a  hy¬ brid  coined  fr.  lutana,  a  word  of  Arabic  origin, and  suff.  -ista  (fr.  Gk.  -iaT/js).  See  lute,  ‘an instrument’,  and  -ist.  Cp.  lutist. lute,  n.,  a  cohesive  substance.  —  ME.,  fr.  MF. (=  F.)  lut,  fr.  L.  lutum,  ‘mud,  clay’,  which  stands for  *lutom  and  is  rel.  to  -luere  in  polluere  (for *por-luere),  ‘to  pollute,  contaminate’,  and  to  lus¬ trum  (for  *lu-strom),  ‘slough,  bog,  morass’.  See pollute  and  cp.  lutetia,  Lutetian.
=== KLN illustrate ===
2753:angary,  n.,  the  right  of  a  warring  nation  to  use or  destroy  the  property  of  neutrals.  F.  an- garie,  fr.  L.  angaria.  See  prec.  word, angel,  n.  —  ME.,  fr.  OF.  angele  (F.  ange),  fr.  L. angelus,  fr.  Gk.  oiyyeXo-,  ‘messenger,  divine messenger,  angel’  (whence  the  verb  dyyeXXetv, ‘to  bear  a  message,  report,  tell’),  which  is  rel.  to dyyapo?,  ‘mounted  courier,  messenger’;  of Persian,  ult.  of  Sem.  origin.  Cp.  Akkad,  agarru, ‘hireling,  hired  laborer’,  fr.  agaru,  to  hire  , which  is  rel.  to  Aram,  agar,  eggdr,  ‘he  hired’, (whence  Arab,  ajara,  of  s.m.),  Heb.  iggereth, Aram.  igglri,  iggartd,  ‘letter’,  prop,  message Cp.  angaria,  the  first  element  in  Ingram  and  the second  element  in  evangel.  The  sense  develop¬ ment  of  Gk.  ayyapo<;,  resp.  6cyyeXo<;,  from  a Sem.  noun  meaning  ‘hireling’,  may  be  illustrated by  the  phases :  ‘hireling,  hired  messenger,  mes¬ senger’.  Gk.  dyyeXoi;  in  the  sense  of  angel ,  is a  loan  translation  of.  Heb.  mat  dkh,  messenger, divine  messenger,  angel’,  fr.  base  l-'-k,  ‘to  send  . Derivatives:  angel-ic,  adj.,  angelica  (q.v.),  angel- ic-al,  adj.,  angel-ic-al-ly,  adv.,  angel-ic-ize,  tr.  v., angel-ize,  tr.  v.
3165:appeal,  tr.  and  intr.  v.  —  ME.  appelen,  apelen, fr.  OF.  apeler  (F.  appeler ),  ‘to  address,  entreat, call’,  fr.  L.  appellare,  ‘to  address,  accost,  appeal to,  apply  to,  summon,  call,  name’,  fr.  ad-  and -pellare  (found  only  in  compounds),  fr.  pellere, ‘to  drive’,  whence  also  appellere,  ‘to  drive  to’. The  sense  development  of  appellare,  ‘to  ad¬ dress,  accost’,  etc.,  fr.  pellere,  ‘to  drive’,  may be  illustrated  by  the  following  phases :  ‘to  drive, push  on,  incite,  warn,  admonish,  summon,  call, address’.  See  pulse,  ‘throb’,  and  cp.  repeal.  Cp. also  compel,  dispel,  expel,  impel,  propel,  repel. Cp.  also  push.  The  change  from  the  3rd  con¬ jugation  ( pellere ,  appellere)  to  the  1st  (appel¬ lare)  is  due  to  the  iterative  sense  of  appellare. Cp.  interpellate,  ‘to  interrupt  in  speaking’,  which is  formed  fr.  inter-  and  -pellare,  and  also  has  an iterative  meaning  (see  interpellate).  For  other Latin  iterative  verbs  of  the  1  st  conjugation  form¬ ed  from  verbs  of  other  conjugations  cp.  inter¬ polate,  ‘to  give  a  new  form  to,  to  polish,  fur¬ bish  ;  to  change,  vary;  to  falsify;  to  insert,  inter¬ polate’,  fr.  inter-  and  polire,  ‘to  smooth,  polish,
6536:Carduus,  n.,  a  genus  of  prickly  herbs  ( bot .)  — L.  carduus ,  ‘thistle’.  See  prec.  word, care,  n.  —  ME.  care,  fr.  OE.  caru,  cearu,  ‘anxiety, sorrow,  care’,  rel.  to  OS.  kara,  ‘sorrow’,  OHG. chara,  ‘lament’,  Goth,  kara,  ‘sorrow’,  OS.  (mod) karag,  ‘anxious,  sad,  sorrowful’,  OE.  cearig, MDu.  carich,  ‘sad,  sorrowful’,  Du.  karig, ‘scanty,  frugal’,  OHG.  karag,  ‘anxious’,  MHG. karc,  karg,  ‘shrewd,  clever’,  G.  karg,  ‘stingy, scanty’;  fr.  Teut.  *karo ,  ‘sorrow,  care’.  These words  are  cogn.  with  Gk.  yr,pu?,  Dor.  yapu ;, ‘voice,  sound’.  Arm.  cicarn,  ‘swallow’,  cicarnuk, ‘nightingale’,  Ossetic  zar,  ‘song’,  zarun,  ‘to  sing’, L.  garrire,  ‘to  chat,  talk,  chatter',  W.  garm, OIr.  gair,  gairm,  W.  gawr,  ‘noise,  cry’,  Toch. karye,  ‘care’.  All  these  words  derive  front  the I.-E.  imitative  base  *gdr-,  ‘to  shout,  cry’.  The sense  development  of  Toch.  karye,  ‘care’,  E.  care and  the  related  Teut.  words  may  be  illustrated by  the  following  stages:  cry — lamentation — grief.  Cp.  chary,  cur,  garrulous,  Gerygone.  Cp. also  German.
14008:gen.  -on is,  fr.  exemplificatus,  pp.  of  exempUficdre. See  next  word  and  -ation. exemplify,  tr.  v.,  to  show  by  example.  —  ME. exemplifien,  fr.  ML.  exemplifiedre,  ‘to  illustrate’, formed  fr.  L.  exemplum,  ‘example’,  and  -ficare, fr.  facere,  ‘to  make,  do’.  See  example  and  -fy. Derivative:  exemplifi-er,  n. exempt,  tr.  v.,  to  free.  —  F.  exempter,  fr.  exempt, ‘free’,  fr.  L.  exemptus,  pp.  of  eximere,  ‘to  take out,  take  away’,  fr.  ist  ex-  and  emere,  ‘to  take, buy’,  fr.  I.-E.  base  *em-,  ‘to  take’,  whence  also OSlav.  imp,  j(ti,  ‘to  take’  (orig.  *imq,  cp.  vuz- iniQ,  T  take  away’),  irmmi,  imejg,  imeti,  ‘to have’,  Lith.  imit,  imti,  OPruss.  imt,  ‘to  take’, OIr.  -em  (only  in  compounds  as  in  ar-fo-emat, ‘they  take’);  cp.  OI.  yamati,  ‘holds,  subdues’, from  the  enlarged  base  *yem-.  Cp.  example,  and words  there  referred  to.  Cp.  also  adeem,  adempt, ademption,  assume,  assumption,  consume,  con¬ sumption,  diriment,  eximious,  exon,  Irredentista, peremptory,  pome,  pre-emption,  premium,  pre¬ sume,  presumption,  presumptuous,  prompt,  ran¬ som,  redeem,  redemption,  resume,  resumption, Sejm,  sumption,  sumptuary,  sumptuous  and  the second  element  in  vintage.  For  the  sense  deve¬ lopment  of  L.  emere,  ‘to  take;  to  buy’,  cp.  Heb. laqah,  ‘he  took;  he  bought’.  In  the  latter  sense Heb.  laqah  occurs  very  rarely  in  the  Bible  (see e.g.  Prov.  31:16),  but  quite  frequently  in Mishnah  and  Talmud.
16564:grangerism,  n.,  the  practice  of  grangerizing.  — See  next  word  and  -ism. grangerize,  tr.  v.,  to  illustrate  a  book  by  the  ad¬ dition  of  prints,  engravings,  etc.  —  Lit.  ‘to  il¬ lustrate  a  book  in  the  manner  in  which  James Granger's  ‘Biographical  History  of  England’ (1769)  was  illustrated.
=== KLN light (n) ===
=== LAT lustro ===
2661:aleB, -onis m.(cf .ganeo, lustro), formation populaire en -o, -onis.
3176:(qu'il faut vraisemblablement lire ambicisu ); ambilustrum (Servius);
17288:condere ensem, solem, lustrum, et finalement "enterrer, ensevelir":
23189:Su<?t. ap. Isid., Nat .44, flustrum (flustra sunt Gloss.) • motus maris
31875:lectio, a lacu deriuatur, quam alii lamam, alii lustrum dicunt, P.F.
34921:verbe *luo "souiller", auquel iis rattachent lustrum "bouge", pol-lu 5 ,
35130:c'etait une piante lustrale (cf. lustrum). L'autre nom latin est uerbend-
35132:lustrum, -i (avec u) n.: bauge. Lustra significat lacunas lu¬
35137:P.F. 107,«. Ancien, classique. De IA: lustror,-dris, arch.: se vautrer
35142:lustrum: v. plus loin sous luc-/ lite-. M.L.5184.
=== LEW lumen/luna ===
```


## [2026-09-07T01:47:28.719Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LAT luceo/lustro section ===\"; grep -n -A4 \"lustro, -as\" LAT.txt | head -40\ngrep -n \"lustro,\\|lustrare\\|lustralis\" LAT.txt | head -20\necho \"=== KLN illustrious ===\"; grep -n -i \"illustrious,\\|illustrate,  tr\" KLN_1966.txt | head -5"
}
```


### [2026-09-07T01:47:28.803Z] TOOL RESULT

```
=== LAT luceo/lustro section ===
21227:anni, populus februaretur, i.e. lustraretur ac purgaretur, uel a Iunone
35156:Derivas et composea: lustralis (-bilis) - , lustrdtio,-tor - , lustrSmen,
35169:d’expressions comme lustrare flammis (Vg., En.4,607); I. lumine (Lucr.
35254:langue a recouru A d'autres deriv 4 s, tels que (il) lustro, illumino.
35307:compose i l lustro,-as , avec ses dArivAs illustratio (ce dernier passA
35315:II y a des traces de illustrare dans quelques dialectes itali ens,
=== KLN illustrious ===
1917:Agave,  n.,  the  mother  of  Pentheus  (Greek  my- thol.)  —  L.,  fr.  Gk.  ’  Ayauf],  prop.  fern,  of  deyauo  q, ‘illustrious,  noble’  (of  kings),  ‘brilliant,  glorious’ (of  things),  rel.  to  yaiEiv  (for  *yxF-iEiv),  ‘to rejoice,  exult’,  yaupop,  ‘exulting  in  something’, yaOeiv  =  yr/Dsiv,  ‘to  rejoice’,  and  cogn.  with L.  gaudere  (for  *gawidere),  ‘to  rejoice’.  (The  d- in  d-yauop  has  intensive  force.)  See  joy  and cp.  gaud.
7870:Derivatives:  cleanser  (q.v.),  deans-ing,  n. cleanser,  n.  —  OE.  clinsere,  fr.  dinsian.  See prec.  word  and  agential  suff.  -er. dear,  adj.  —  ME.  cler,  deer,  fr.  OF.  cler,  clier (F.  clair),  fr.  L.  clarus,  ‘bright,  shining,  clear, plain,  manifest,  illustrious,  famous,  glorious’, which  stands  for  cla-rus,  and  is  rel.  to  cla-mare, ‘to  call,  cry  out,  shout,  declare’,  fr.  I.-E.  base *kld-,  var.  of  *kal-,  ‘to  shout,  resound'.  See calends,  and  cp.  claim.  Cp.  also  claret,  clarify, Clara,  clarin,  clarinet,  clarion,  clarity,  declare, eclair,  glair,  the  first  element  in  clairaudience, clairvoyance,  chiaroscuro  and  the  second  element in  chanticleer.
18746:Derivatives:  illusori-ly,  adv.,  illusori-ness,  n. illustrate,  tr.  v.  —  L.  illiistrdtus,  pp.  of  illustrare, ‘to  make  light,  light  up,  enlighten,  illustrate, render  illustrious’,  fr.  in-,  ‘in’,  and  liistrdre,  ‘to illuminate’.  See  luster,  ‘brilliance’,  and  verbal suff.  -ate.
18749:illustrious,  adj.  —  L.  illiistris,  ‘light,  bright,  bril¬ liant;  clear;  famous’,  prob.  back  formation  fr. illustrare.  See  illustrate  and  -ous.
```


## [2026-09-07T01:47:38.111Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/luster",
 "prompt": "Give the etymology of luster/lustre (gloss, radiance) verbatim, including the French/Italian/Latin chain and the PIE root cited."
}
```


## [2026-09-07T01:47:38.899Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/illustrate",
 "prompt": "Give the etymology of illustrate verbatim, including Latin illustrare, lustrare and the PIE root cited, plus dates of first English use."
}
```


### [2026-09-07T01:47:42.662Z] TOOL RESULT

```
# Etymology of Luster (Gloss, Radiance)

According to the Online Etymology Dictionary, the term originates as follows:

"from French _lustre_ 'gloss, radiance' (14c.), common Romanic (cognates: Spanish and Portuguese _lustre_, Rumanian _lustru_, Italian _lustro_ 'splendor, brilliancy'), a noun ultimately from Latin _lustrare_ 'spread light over, brighten, illumine,' which is related to _lustrum_ 'purification' (from PIE _\*leuk-stro-_, suffixed form of root _\*leuk-_ 'light, brightness')."

The word entered English around the 1520s and developed figurative meanings including "radiant beauty" (circa 1600) and "splendor, renown" (1550s).
```


### [2026-09-07T01:47:51.705Z] TOOL RESULT

```
# Etymology of Illustrate

**First English Use:**
The verb "illustrate" dates to the 1520s meaning "light up, shed light on," with the sense of "provide pictures to explain or decorate" appearing by the 1630s.

**Latin Origins:**
The word derives from Latin *illustrare*, meaning "light up, make light, illuminate," and figuratively "make clear, disclose, explain; adorn, render distinguished."

**Components:**
According to the source, *illustrare* comprises an assimilated form of *in-* ("in") plus *lustrare* ("make bright, illuminate").

**Proto-Indo-European Root:**
The ultimate origin traces to the PIE root *\*leuk-*, which means "light, brightness."

**Summary:**
The semantic evolution progresses from literal illumination (1520s) through educational clarification to visual illustration (1630s), reflecting the foundational meaning of *lustrare* and the ancestral *\*leuk-* root.
```


## [2026-09-07T01:48:02.544Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB roc ===\"; grep -n -E \"rōč|rōšn|rōčīk|rwc|rwšn\" NYB_vol2_glossary.txt | head -20\necho \"=== FVQ rizq ===\"; grep -n -i \"rizq\\|razaqa\" FVQ.txt | head -10\necho \"=== AFA rizq ===\"; grep -n -i \"rizq\\|rezqa\\|rizqa\" AFA.txt | head -10\necho \"=== MON_part2 لوستر ===\"; grep -n \"لوستر\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-07T01:48:02.660Z] TOOL RESULT

```
=== NYB roc ===
3343:rēšn [Iwšn'] 1. adj. light, bright, lumi- nous, splendent, brilliant, comp. ~-tar 3722, 668 etc. passim. — 2. subst. light: tai 50 roc ~ né bavét (pres. hist.) during 50 days it did not get light 2015; ~ bavandak 574; bun ~ primeval Light 1118-21, 11219; 965, — Av. (1488) raoxšna-; MPrthPrs rwšn; Paz. rös(a)n; NP rau- šan.
6117:rwšn: rošn rwy: lrod rwy: ?rod
=== FVQ rizq ===
=== AFA rizq ===
=== MON_part2 لوستر ===
```


## [2026-09-07T01:48:08.509Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -E \"lwc|rōc|roc\\b|rōčik|rocik\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T01:48:08.567Z] TOOL RESULT

```
672:= Dūrēsrav bé 6 Zartušt guft ku: cigēn-at fratom ham (cf 209 ete.) bahr u rocik be apakand hom, an tč an (v. lan and ?an) har 2 aš apar barom api-t bē marnjēnēm "D. said to Z.: because thou hast deprived me, as the first, of both munistry and food, we both, thou and I, shall be enraptured in an ecstatic vision, and then I shall annihilate thee’.
1369:druž [dlwc'] all that is false, untrue, wrong, deceptive: 1. the world of Guile and Untruth, conceived as a personal cosmic power, 3822, 9313. — 2. individual manifestations of this power, demons, conceived as feminine supernatural be- ings: sg. 5716-25, 583. 9620-24, 9817-19, 101% (voc.). 1023-14; ~ ; anāštēh 671; ^ 4 spazgeh 6811-12; ~ 7 ahramög 10124-25; pl. cas. rect. ~ 648. 65*. 9721, 9819 (of human beings). 10224-27, 1033; pl cas. obl. —-än in the set phrase devün u ~-dn 75" ete. (voc. 9027). V. also mthr-druz, mihrčin-druž. — Av. (778 sqq.) drug-, nom. druxš, gen. drüjö; MPrs drwaš (S); Paz. drü£.
1491:Filippos [pylpws] Dilurroc', Philip 117°.
1750:h- (HWH- ; 3d p. sg. "YT', neg. L'YT', inser. and Ps. ^Y TY, L'YTY 2nd p. pl. enel. -ét in amahraspand-é 58"; forms v. I, 175] to be, only in the pres. ind., subju. and opt., other forms from bütan (q. v ): l. as an independent vb. in the 3d p.: exist(s), e.g. hast hàn ke ahlayeh the One who is Righteousness exists 57°; héc ke but hénd u hec ke bavénd u h&c ke hend all who have been, and all who will be, and all who exist (now) 6417-18, cf subst. hast and nesteh; im roc 7 mähakän hast tdi ... to-day it is seven months since 1011-12. kë hast ke ...? who is there who ...? 257-7; andar Ērān-šahr asvār-ē nest ke ... in Eran-shahr there is no horseman who ... 15; hast 4-8 ... u hast 1-§ ... u hast i .. . there is some (of it) that ... and there is some (of it) ... and there is some (of it) that... = part of it... part of it... ete. 9317-18.26; hast kč-š veš, hast ké-§ kam some have more, others less 96°; astömandän mar- tömän (gen. part.) hast i ... of earthly men there are some who 10519; hast <a> šāhān šāh, hast <i> kesar some belong to the King of Kings, others to the Emperor 11519-20; nē hast kū there is no place where, nowhere 611°; hast (i) ka there is a time when, sometimes, at times 7725-26, 8122, 12018-1?; — with prev.: šusr i Gayomart cis andar hast there is some part of the sperm of G. in it 9422-23; kū-š ataxš andar nést where there is no fire 3721, — 2. copula, with a noun, a pron., or a prep. -- subst. as its complement, pas- sim; the 3d p. sg. ‘is’ is very often not
1758:hae [MN ; hc 619] prep., with -c: MN-c = hac-ic; not with an encl. pron. (as to haciš, hacisan v.s. v. hactš); the original sense ‘accompanying, with’ (Skr sacā) is still transparent in ~ ... hämisi (g. v.) ‘together with’, but the meaning ‘from, of’ prevails since the OIr period. 1. Local: hàn yam ... hac dast i Artaxser 6 damik opast 92°; api-š hecak hac cah ul hixt 155; hakar hac asp bē nisinam 27?; hac star püdak tai mah pädak 93"; hac dar ētšān bagän namäc burt from the gate-way (i.e., halting at the entrance, from this place) I rendered adoration to His Majesty. P1:4; — figurative, with a great many vbs. and idioms, the sense of ‘from, of’ being more or less transparent. akahé- nitan, āšnūtan, pursitan, x"āstan, dast šustan hac ete., v. the individual ws.; — origin: ke cihr (Prth Shr) hac yazatān (Prth y’ztn) whose origin is from the gods, of divine origin HajB: 2.4 (HajA: 2.4). SPrs: 5-6 (yazdān) (SPrth: 5). P1: 2.4 (yazdàn) ; "Apasči... à hac Haran ŠPrs: 9; hac tohmak + Dārāt būt 18, etc. — 2. tem- poral: hac im róc from today onwards, henceforth 9"; hac im réc tdi 3 roc within three days 51%; hac rahikehv [lsykyhy] ever since my youth 1282-5; ete. — 3. after a v. n. it expresses the subj. of the act: patirak zanišn + hac ganäk menoi on the point of being slain by the Evil Spirit 46°-§; zanisn i devàn hac han i 0$ xvarrah the demons being slain by his divine splendour 461?; freftakeh + hac dēvān de- ception by-the demons 461; 4513-14; ete. —
2561:mihrān-druž [mtr'ndlwc'] breaking one’s promise, one’s word; apostate 71% | uzdes-paristar; v. also mihr-druž. — Cf mihrän kartan to form an alliance KnS VI, 2. — Paz. mihiran-dru£.
3326:rče [YWM; lwc] day, pl. cas. obl. —-än [Iwe?n'] 2720; contrasting with gap ‘night’ 45, 2023; ka ~ būt when day was dawning 635; im ~ to-day 10, ete.; fratük ~ to- morrow, v. fratāk; nem ~ half a day 317, v. also nem-röc; hac im = tāt 3 — within three days counting from to-day 519; — m šapān 329. 728, 7417 [all lwc]. 989-109, 1203 (YWM šp'n'], röcak šapān 742°. 1011: the astronomical day of 24 hours (Swed dygn, Russ sutkt). — The names of the days of the month are in BP: 1. Ohurmazd. 2. Vahuman. 3. Art-(Urt-)
3329:röcak [lwck']: ~ šapān, v. the preceding W.
3330:rocénitaréh [lwcynyt’lyh] the act of mak- ing light, of illuminating 88*. — From the den. vb. récénitan, from róc (q. v.); MPrs rweyn-. Paz. substitutes rēšnīdārī, from a den. vb. rösnitan, v. rošn.
3331:röc-kär [lwck’l] time, date, season: ~ 7 vicitak at a chosen date 121%. — Properly ‘daily work’, cf NP rozgar ‘labour; earn- ing, fortune; the world; time, season’.
3343:rēšn [Iwšn'] 1. adj. light, bright, lumi- nous, splendent, brilliant, comp. ~-tar 3722, 668 etc. passim. — 2. subst. light: tai 50 roc ~ né bavét (pres. hist.) during 50 days it did not get light 2015; ~ bavandak 574; bun ~ primeval Light 1118-21, 11219; 965, — Av. (1488) raoxšna-; MPrthPrs rwšn; Paz. rös(a)n; NP rau- šan.
3689:tacitan [teytn'] to run: api-m cand 4 nem roc pat pušt hamé tacit hom (for tacit-om) almost half a day (he was run after by me =) I ran after him 311? (cf s. v. kar- tan); be tacit pat oš han mat *cautiously (v. s. v. 68) his mother ran to him 48?9, 217.49 5019; pčš tacit ran before, got ahead (of the others) 494-19, — Av. (624) tak-; M Prth tc-; MPrs čz- (S); Paz. 0ajü for tazak (tajäk; Aog. 77); Verbum 169; Ghilain 50. Cf täxtan.
4927:rad, radiy: *rad Raga: Rag rasa-: rasitan raucah-: roc rautah-: rot
5298:2räna-, rana-: ran raocah-: roc raoda-: rod raoióita-: ?rod raoy-, raoyna-: rogn
6115:rnz, rnzwr: ranj rptn, rw- raftan rsydn: rasitan rxtrnz: raxtan rw’n: ruvän rweyn-: rocēnītārēh rwd: röt
7281:nimrüz: nčm-roc
7369:roz: roc
```


## [2026-09-07T01:48:17.584Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%84%D9%88%D8%B3%D8%AA%D8%B1/",
 "prompt": "What do the dictionaries (فرهنگ معین، دهخدا) say about لوستر — its meaning and its origin tag (e.g. [فر.] French)? Quote the Mo'in entry."
}
```


## [2026-09-07T01:48:18.287Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D9%88%D8%B3%D8%AA%D8%B1",
 "prompt": "Is there a Persian entry لوستر? Give its etymology (French lustre?) and meaning."
}
```


### [2026-09-07T01:48:22.379Z] TOOL RESULT

```
# Persian Entry: لوستر

Yes, there is a Persian entry for **لوستر** (lustr/luster).

**Etymology:** The word derives "From [French](https://en.wikipedia.org/wiki/French_language) _lustre_."

**Meaning:** The term refers to a "chandelier"—a decorative hanging light fixture. Persian synonyms include قندیل (qandil), نورافشان (nur-afšân), and چلچراغ (čel-čerâġ).
```


### [2026-09-07T01:48:29.145Z] TOOL RESULT

```
# Meaning and Origin of لوستر

According to **فرهنگ معین** (Mo'in Dictionary):

**Origin tag:** [فر.] (French)

**Definition:** "۱ - حباب شیشه ای ، چینی یا فلزی چراغ مخصوصاً نوعی که از سقف آویزان می شود" (A glass, porcelain, or metal globe-shaped lamp, especially one suspended from a ceiling)

The entry also notes two additional meanings: a lamp with one or more globes/bowls, and a decorative lighting fixture.

The **[فر.]** tag indicates the word derives from French, consistent with the page's explanation that "Chandelier" originates from the French word "Chandelle" (candle holder).
```


## [2026-09-07T01:48:47.405Z] TOOL CALL #72: Bash

```json
{
 "command": "ls site/pages/312.jpg 2>/dev/null; pdftoppm -f 312 -l 312 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg312 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T01:48:49.164Z] TOOL RESULT

```
site/pages/312.jpg
total 388
drwx------ 2 sfmqrb sfmqrb  4096 Sep  6 21:48 .
drwx------ 3 sfmqrb sfmqrb  4096 Sep  6 21:35 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   175 Sep  6 21:37 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 50563 Sep  6 21:41 crop_boxes.png
-rw-rw-r-- 1 sfmqrb sfmqrb     0 Sep  6 21:39 iec_pages.json
-rw-rw-r-- 1 sfmqrb sfmqrb   228 Sep  6 21:47 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb 68332 Sep  6 21:48 pg312.png
-rw-rw-r-- 1 sfmqrb sfmqrb 56809 Sep  6 21:41 pg313.png
-rw-rw-r-- 1 sfmqrb sfmqrb 64584 Sep  6 21:40 pg314.png
-rw-rw-r-- 1 sfmqrb sfmqrb 49502 Sep  6 21:37 pg315.png
-rw-rw-r-- 1 sfmqrb sfmqrb 80390 Sep  6 21:45 pg317.png
```


## [2026-09-07T01:48:52.138Z] TOOL CALL #73: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg312.png"
}
```


### [2026-09-07T01:48:52.491Z] TOOL RESULT

```

```


## [2026-09-07T01:48:52.489Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T01:49:15.674Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '24800,24895p' BRT.txt"
}
```


### [2026-09-07T01:49:15.723Z] TOOL RESULT

```
niären Schaden  erleiden':  allö  galhanqm *iriiintinqmi'>  ragie  (sd.)  N.  2,
mit  a  dnwS.s:   ya^a  nSit  aiti(sd.)  ni- läitica  *airi/yq  (3PKA.)*'  N.  Öji?).
ai.  risyixii  'ei  tut,  nimmt  Schaden',  refäyali 'er  tut  Schaden',  ri}/iiA;  mp.  resilan.  —  Pü. : reiitan,  zu  3  a  erl. :  api  murtan.  —  ■>  Pü. : ku  ne  an  i  pas  Ö  i  pis  etön  relet.  —  ')  S.  zu hindav-  Nu.  I.  —  J)  Hds.  'hntanqm.  —  4)  Hd». airiyq.
"  J,  'raesa-  m.,  raesah-  n.  'Schädigung'; A)  körperliche  Schädigung  überhaupt; a)  in  Bezug  auf  den  Fötus;  yeHi^a  . .  kaine . .  3^atö  garnuim  irisyeiti  .  .  ptinbyS  (sd.) irisintqtn  ralli  Hkain  baoiiS.varltahe  ci- %aya  V.  75. 1 3.  b)  in  Bezug  auf  Hunde: yS  süne  piilrtm  jainti  ..  us  va  hl  gaohm 'hwirisaiti  apa  va  ks  pathyqm  kintUaiti . .  cikayat  sBnahe  °l5  (ASn.)  baob5.varHahe üfhaya  V.ij.io;  'Vyt.44;  —  ym..spiina ahaiiyS.at»/iar3^r>m  (sd.J  irisyqn  para  as- iqm  iriHntqm  'h  cikaen  baoZs.var^iahe Hhaya   V,  75.  22,  40.  2)  Rechtsaus-
druck fiir  jede  einem  Menschen  indirekt diu'ch  Fahrlässigkeit  zugefügte  körperliche Schädigung,  fahrlässigeKörperverletzung*': yai  .  .  vlmaaascit  vtmahayänie  .  .  yai "k^ritu  (sd.)  iriSyat  para  hi  trismtB  'stm cikayat  bao'üö.varstaht  a^aya  V.  7.  38;  — yezi  .  .  apirmäyüks  doaityS.ajiharihnm (sd.)  iriiyäi  para  hl  iriüntS  °s)m  Hkayal bao*>S.varstahe  ii'haya  Y.15.16;  —  nabä- nazdistim  h!  .  .  para  .  .  *'/aäi ''  *aowa- oaityacd  *ästäraiti  (sd.)  N.  g.  B)  peku-
;niäre;  damnum:  also  gafhanam  *iris'inti- I  nqm  ■«  (als  AP.) ''  (näml. :  pa'iti  Hkayatf) \  "der  (ihn  durch  sein  Weggehen  verursache hat,)  soll   den  Schaden  des  geschädigten
dby  Google
1487
'raeia-
raoxSnav-
14S8
Hauswesens  (ersetzen)"  N.  2(?)i'.  Un- klar: yäfa  'hm  .  .  ti.yiT.
*>  Im  Gegensatz  lu  ar^jiis;  j'am-  uaä/taiä- iaaiaA-  ina%a-;  vgt.  batAö.i/arila-.  In  den  drei votliegenden  Fällen  handelt  es  sich  um  Mangel an  anilicher  Umsichl  (V./)  ond  um  PflicbtTer- Säumnis  (V.  TS.  N.  9).
Zum  V.  rat!-.  ~    ai.  «ja-  m.,  nip.  (Pü,),   np-
rFI.   —   1»  Hds.  taei.a.   —  »)  Pron.  fleklirt.  —
3)  So  nach  PüErl.:  ci  ris  töiel.
•  j.  'raeäa-  m.  'Spalte'  in  der  Erde:  ys .  .  var>shs^a  .  .  aia  äim  ^vpaMosayäti *u>iahva  dim  °A>irf(LS.)i-'ä  ".  .undsie(naml. Haare  und  Nagel)  dann  fallen  lässt  In Erdlöcher  und  (oder?)  in  eine  Erdspalte" V.  ly.  i.
VU.  au»  idg.  *i!oh<i-,  vgl.  an.  sliia  'jerreissen', nhd.j'''^/n'o(ii]itanderm'WurieldeteiTnmaliv')i).
—  Pü.:  rf.'ii'u,  erl.:  Jarlin'}.  —  ')  Ander» (falsch)  JK.  JAPh.  //.  88.  —  >)  Sva.  Jarm, das  sijara-  (id.)  übersetil;  vgl.  auch  Av.  //. 11,  wo  die  tids.  darm  und  darlm  geben  und zu  i/rrway-,    Ist  darim  gleich  ai.  därimaM- n.7
•  j.  raeäah-  n.:  s.  unter  'raisa-.
■  j.  raok-  V.  'leuchten'.  Praes.  2  rao^a-, 30  (Iter.  und  Kaus.)  raocaya-.  —  Inf. 'raeiayäi.
'leuchten,  flammen':  raocintat^'>  paili a^rät    A.  4.  S-  a)    Kaus.    'leuchten
machen':  ya^a  ianUm  raocayäli  ya^it minkö  Yt /0. 142.
mit  ai-wi  'beleuchten,  bescheinen':  yat hl  iiärqm  (als  Subj.)  . .  aiuii.raoiayänte "damit  ihn  die  Sleme  . .  bescheinen"  V. ig.  23-
mit  az-i  und  aiwi  'aufflammen  lassen, entzünden  an  — '  (Gen.):  aii  äim  (näml. zanqm)  aiwi.raocayäti  li^rö  V.5.  2.
mit  i7 'leuchten':  ruiJ/fUsd.)  ..7?  ava^a ä.rao^ayeite  V.  3. 39 ;  —  vTfpa  slthäta (näml.  raniv?,  sd.)  aora  äraocayeiti  antardt V.  2.  40  Pli2.
mit  US  'aufleuchten,  aufflammen,  empor- leuchten': vlspa  anayra  raocä  (sd.)  usca us.raoi'ayäii  V.  2.  40  PüZ.;  —  zafar?  paiti uzraecaymi  Yt.  tQ.  50;  —  vTusniti  (sd.) *usi.'^raocaiti  bamya  V.  7p.  28.
mit  paiti  Kaus.  'wieder  aufflammen lassen':  paili  mqtn  raocaya  aisrnanqm (statt  Instr.?)  "lass  mich  wieder  aufflam- men durch(?)  Hölzer"  V./cV.  19,
ai.  rfcale,  rDcdyali;  np.  .i/röxtan  'aniünden', a/rözad.  —  PiL  (lu  V.  5,  18):  aairixtuH,  [zu V.  /p):  Töiiismlaii,  (lu  V.  3]:  fehlt  —  ')  Tbem.
-  »)  So  L4  und  K  I  (wVO;  Jp  i  usw.  und  NA. mi\  Pü. !  tti  'Morgenröte'.     S.  lu  ^vah-.
•  j.  rao^a-  n.  'Butter',  mit  *taramaya- Adj.  'Friihlingäbutter',  Bezeichnung  der Speise  der  Seligen:  i^ari%aiiqm  hi  barg- tqm  (sd.)  *zaramayeAe  "nahe  tal  atti  yünS ..  hudalnahe  ifarüim  pasca  para.iristjm H.  2.18".
Ableit.  —  np.  rir,an  'ausgelassene  Butter'.  — Pü.  (lu  IL):  rSyn;  lu  Aog.  /Ö  wird  umschrie- ben: Sfe»,  malen,  ilrln,  aiif^apfnin.  —  ■)  Vgl. iSt.  Mx.  2.  152,  Dd.  j/.  13  f.,  Av.  10.  $  und IQ  am>r)talät-  No.  3.
j  •  j,  raoyna'vant-  Adj.  (fem,  °vaitl)  'der I  Butter  hat':  xh-iptavaiti  •iaiti{\S(.)  mas- \gavaiti  V.  2/.  7.
Pii. :  rOinivanJ.
•  j.  raDj-nyä-  f.  'Butter':  avi  'yqm  vara- »hiiH  f  sd.)  Yt  /2. 3.
Ableit.  aus  rotiyHj-  (ohne  erkennbar«  Bedeu-
tungsveranderung ;  vgl.  ai.  iarav-  und  larav\i;
WH.  Cr."  S  m^  h).
•  j.  raoxSna-  i)  Adj.  'licht,  glänzend':  'mm .  ,  ya^a  iltr»m  Vyt.  .i;  —  '/Dm  mäuhtm ^^■7-3'>  —  tislrim  .  .  aurui)m  'tum  /rj- dinsmn  YLä  2;  —  asmatum  y?  .  .  'nJ frädinsrS  Yt.  13.1;  —  °mm  garö  nmUrum S.  2.  30;  —  haia  'na  *garj  nmäna  YL  sg. 44;  —  'näi  paili  *garS  nmSnSt  Yt.  10. 123;  124;  —  'naht  ''gorö  nmänahe  S. /. 30;  Yt.  12. 37i  —  nrnJimm  . .  frSäfrisnm 'mm  V.  22.  1 ;  —  am»sanqm  sptntanqtn .  .  yaSsqm  'natihä  fantänS  ,  .  Yt  JJ. S4;  —  aurvatitd  auruh  'na  frädinsra ^■37-^7'>  —  yer>he  urva  ..  aurusö  'nS frädirisrö  Yt.  13.  81;  —  'na  frayantu  ti OTd!OJ(sd.)  Y. /o.  19.  2) n. 'Licht':  'tum kfnnavühi  dämahva  V.  2/.  5.  a)  Plur. 'Flammen':  yai  neif ..  ä^re  **nam "'  paili.- äily^i  V.  16.  2.
KompE.;  Ableit.  —  Zum  V.  rnpii^;  vgl.  rani.'- nay-,  'inav-,  'inj-,  —  np.  TÖsan;  vgl.'/Vfan^ —  Pü.:  töin,  (lu  V.  21):  rölmh.  —  1)  AP.; so  L4,  Kl;  NA.  •«?«.
•  j.  raoxsnay-  i)  Adj.  'licht,  glänzend': tilirim  . .  dural  vyävant?m  (sü.)  bänubyB 'niiyj  \l.S.2->.  2)  n.  'Licht,  Licht- glanz' (nur  Komp.).
KompA.  —  Zum  V.  nvii-.  —  1)  Vgl.  YL JJ-  44-
•  j.    raoxsnav-    n.    'Licht,    Lichtglanz':
Paoiryii  dasa  xsapanS  .  .  tislryS  .  .  kfhr- p?m    raS^iaaytili    'ttusi-a    raamnO   Yt.  S.
13";  45- Zum  V.  lank;  —  V^.ü.roeifttet-  .KA\.  'leuch- tend'; S  190.  2  mit  No.  9.  —  i)  Vgl.  Bd.  /. 4 !   tiilr  .  .  JO  röc  h  sapin  atidar  risiüM  iair'/.
ob,Google
1489  raoxänä-
•  j.  raoxSnä-  f.  'Licht':   yai  kvan   °nc
(IS.)»  tapaydti  Yt- ff.  i;  7.4.
Zum  V.  raok:  —  Vgl.  raoxina-  usw.  —  Pü.: Töin.  —   ')  Stall  'nya  gesehr.;  %4rs,  sfS.  32.
•  j.  raoxSn«'mant-  'licht-,  glanzvoll':  snta- vaisff  ..  srim  bänvA  •mä  YL/?.  44".
j  nach  S  2gS.   1.  —  ■)  Vgl.  Yt.  Ä  2.
•  j.  ^aoxSni.ai^vi'Sita-  Adj.  'lichtüber- gossen,  licht  umstrahlt"':  fravalayS  . .  ya pgrihr.le  v)r?>raynyaiiu  "taisu  Yt  /J.  45.
■)  Cani  verfehlt  Gdn.  KZ.  23.  558  N0I  65.
•  j.  raoxSni-xSnüt-  f.  'glänzende  Be- lohnung*: a^aurunS  Ad  raianqm  'iiin  isä- aham  (Sp.  3451»-)  YL/p-Sa-
•  j.raotSana-,  ?-i7öfVna-"  i) Adj. 'leuchtend, licht':  dvarfm  (sd.)  'cafum'^  x''ilragxsmm aK/(irj.nflSnJ/ V.2.30,38.  2)n.  a) 'Licht' (nurAbleit).  b)'LichtöfFnung,  Fenster'-*»: .  .  iipa,6aotaya>t  -iDm  paiti  nrriäna/ie  V. 7.  14.
KompE.;  Ableit.  —  ai.  raiand-  Adj.  'leuch- tend', n.  'Licht',  Ic'cana-  n.  'Auge' 3);  np.  iö:aii 'Fenster'.  —  0  S  29*.  4- —  »  Die  herkömm- liche Cberseliung,  bei  DST.  ZA.  i.  j8:  "une porle  et  une  fenelre",  verlangte  'caaimfa; s.  PisCHEL  ZnMG.  jff.  139.  —  ö)  Das  Fenster ist  das  Auge  des  Haukes.
•  j.  raocant-''  Adj.,  PPA.:  s.  raok-, n  Nut  '<i,<r.
•  j.  rao^as.caesman-  m.  EN.  eines  der sechs  Genossen  des  SaoSyant  bei  der Auferstehung,  Ralav  des  Karsvar  Art- ta/iT'^:  'mariß  a/aeirS  \'t.  1^3.  128;   iii.
Eig.  'Licht  bereilend\?l.  Sj'V".3--  '>  Vgl. Dd.  j6.  4,  wo  der  Name  rüi/i  iviini  lautet.
•  j.  raodas.pairista-  Adj.  'zum  Leuchten, 2U  lichtem,  hellem  Era.nd  ausgesucht''*':  yd ahmäi  (näml.  S^re)  assmiin  (sd.)  baraiti Mkai  *'tqm''>  Y. 62.10;  zit.  V.j>V.  27.
*)  Das  beim  Opfer  vemendele  Holz  soll  mit heller  Flamme  brennen,  nicht  schwelen;  daiu rnnsi  es  ganz  trocken  sein;  vgl.  Sd,  g2.  2.
Vgl,  rao!ahi.buye.  —  Pu.:  ta  röiiiHih  iiitirTl.  —
■)  So  K  4.   NA.  korrigirti
'raocah-  5  a
1490
NA.  •
1  V.  18  hat
•  ').,  g.  'raocah-,  p.  raucah-  n.  i)  'Leuchte' (bes.  des  Himmels) :  hvare  'c5  Vr.  if).  2, Yt.  6.1;  —  slrSUiäi  mdiiA^mcn  hvanca °ca  "die  Sterne,  den  Mond  und  die  Sonne, die  (himmlischen)  Leuchten"  G,^.  6;  — mt^nm  .  .  yeivhe  vaxl .  .  us  ava  -La ainaeiti  ava  pairi  imqnt  sqm  jasciiü  "M, . .,  des  Stimme  hinauf  bis  zu  jenen  Leuchten dringt,  rings  um  die  Erde  gehl"  Yt,  10. 85;  90,  H. /.  16;    —    c'ay3  Hat  aile  ''iv!'>
arghm  .  .  yd  ava'^a  ä.raocayeite  .  .  3^a%ä- taca  "ea  slihillaca  "was  sind  denn  das  für Leuchten,  die  dort  leuchten  .  .?  Es  sind ewige  und  vergängliche  Leuchten"  V. 2. 39  f.;  —  vJspa  anayra  v'il  usca  us.rao- caydti  vTspa  sitoüia  'af  aora  ilraoi'ayäii ariiarai  "alle  anfangslosen  Leuchten  leuch- ten oben  in  der  Höhe,  alle  vergänglichen Leuchten  leuchten  innen  in  der  Tiefe" V.  2.40PÜZ.  S.  noch  ^5.  2)  'Licht', nur  Plur.:  kS  hvöph  'casäl  dal  l^fastä "wer  schuf  wohlwirkend  Licht  und  Finster- jnis?"  Y.44.S;  J7.1,  12.1;  — yims  fra- ■  süsal  'ca  ä  upa  rapii war»  (sd.)  V.2.10; yas/il  mantl  . .  °c5bll  rlxhwm  (sd.)  :^ä- ä  Y.J/.  7i  benutzt  n.i;  —  'cä  x"fng l^sd.)  Y.50.  10;  —  sürä.iwar/tartqm  (sd.) ''ankam  V.  ig.  23.  3)  'Tageslicht',  nur i  Plur. : '  kakat  '.'auAqm  frayrats  (sd.)  V.  iS. 6;  —  'caithqm  fragaUit  F.  27  b;  — frataralibyS  'cä  vitaratibyS  usanhim  Yt 15,55;  —  '"'''  °^^  banziiltm  bamima- nqm  avat  (sd.)  yst  hvarS  av3cl  Y.  jtf. 6.  \  4)   'Tag';   a)   im  Gegensalz   zur
Nacht:  xüipJ'vtl  rauta^palwil  "seis  in  der Nacht  oder  am  Tag"  Bh.  /.  7.  b)  als  Be- zeichnung des  Zeitraums  von  Sonnenaufgang bis  Sonnenaufgang:  garmapadahyu  möAy.i I  -cc^  ->akat%  (sd.)  Skc^  Bh.^;.  i;  — viyaxnahya  mshya  14  '!abis  (^s  NP.)  ^a- knt:i  (sd.,  auch  fdSt.)  J^a"  Bh.  /.  11; usw.; —  anäiiiakahya  mähyJ  s  ''t:abis(3.ls NP.  statt  ND.)  :iaial3  (sd.)  äAa'  Bh.  /. 19.11  51  'Licht,  Lichtraum',  der  lichte
Raum  jenseits  der  Gestirne,  wo  die  Seligen wohnen  (aikTjp;  nur  Plur.'>:  yiJ  'cibis darisalä  urvSzil  (sd.)  Y.jo.  i;  —  äaius'if .  .  dada'zbii  (sd.)  'iibl^  (als  AP.)  Aqm.- vainsimaidi (sd.)  Y.jÄö;  —  >riscit  tarS parstämcit  hs  urvänim  .  .  frapärayeni  , . 3.  vahistäl  artkaoi  3  vahHM  asl^  3  ta- histaSibys  'csbys  Y.if).f);  —  xsalta  'äi x^atwartlsM  vintS  Yt.  J.  i;  P.,?4;  —  "Sil he  glui  bval  nsit  astm  nsil  ^Vj^)  niit vakistd  at}hu?'9. 40.  S.  noch  i.  a)  bes. mit  anayra-  fsd.) :  tüirJm  gäma  frabaral yö  nari  oiaonS  urva  anayrainra  °cöltva niddiät. .yd  nars  drvais  urva  anayraisi'a IjmShia  nidaoffi  H.a.  15  und  33;  — vahii- timca  ahäm  anayra^a  °ca  P..?^; — J"/«/ a/ii  .  .  upa  anayra  'iä  s^d^äiA  Yt.  12.  35 ; j  Y.  1O.6,  7/,  9,  G.3.  6,  V.  //.  I,  a,  /().  35, iS.  2. 30,  *FrBy.;    —   strqm    manhs    hUrS
dby  Google
1491
'raodah-
anayranqm  'canhqm  :^a%älanqm  Y. /.  16;
Yt/y,  57.  SAa)  anayranqm  'caahqtn
(näml.  ayari)  heisst  der  30,  Monatstag^':
S. /.  30;  vgl.  2.30,  Y. /tf-ö.
KompA.  (s.  raelas',  taoB.',  raa/i.'),  E.;  Ableit. —  Zum  V.  raoi;  —  Vgl.  'ran/ai:  —  a,\. 'mcas-,  Tgl.  rodf-  n.;  np.  töü.  —  Pü.i  röin, rSimh.  —  ')  Als  Mask.  behandelt  1  —  ')  Doch s.  P.  40  und  Nq.  3.  —  3)  Hds.  'tö.  —  4)  Im Mp,  anträn  genannt;  5.  auch  aiiayrn'  ■  ix.
•  j,  'rao£ah-  Adj.  'leuchtend,  licht':  va- Mstim  ahüm  aiaonqtn  'carih>m  vTsfiö.:^ä- %nm  Y.  9.  19,  62*6,  68.  s,  II,  '3,  Yt. 12.^6,  Y.ig.^6,  A,/.  12,  5.2.  27,  Vr.7. 1, hz.S,  Vytji  F.J7;  —  Tühislahe  anhius alaonqm  'lanhs  vTspS.:^3^rS  S- 1.  27.
KompA.  (s.  raarahi.').  —  Zum  V.  raak-.  —  Vgl. traocah:   —  Pü. ;  risn,  (lu  F.):  röitüh.
•  ].  raofiahi.buye  Inf.  'lucidum  fieri':  r* ahtnya  nmäne  Y.  62. 3.
Zum  liomp.  V.  'rao-ahibim- ;  %  163.  i.  —  Zu tnuiah-,    auf  dem  ASm.  aufgebaal.   —    Pü. :
•  j.  raofah'ina-  Adj.  'leuchtend,  strah- lend', mit  aoi  und  Akk.  'nach  —  hin': asmatum  .  .  yff  hiilaile  .  .  °nS  aoi  *%risvä (sd.)  YL/5.  a.
•  j.  raodah'ya-  Adj.  'licht,  hell',  Plur.  neutr. Tageslicht':  {antari)  'cake  (APn.)"'  nBii antars  (sd.)  timahe  li.68.
Pü. ;  andar  rSsniA.  —   OS  'ÖS.  33.
•  j.  raocah'vant-  Adj.  'licht':  a/^m  at vahUtim  yatamaids  .  .  kyat  'cönnhvat  Y. .37-  4-
Pü.:    rSsn    lan    i  öi,    Sü.:  yal   rucimal  vapur
•j.raoöa.-aiwi.van>na-m, '(Überdeckung
durch  das  Licht  sva.)  Belichtung':  :^aslairis (sd.)  .  .  °na  hvarp.dar>sya  hl  zfme  paiti nidaihlta  (näml.  atdibXs)  ". .  sollen  (die  Ge- beine) zu  ihrer  Belichtung  und  Besonnung auf  dem  Boden  niedergesetzt  werden"  V. tf.  51;  —  yär}.dräj5  .  .  sairi  (sd.)  . .  wwf nibäite  *na  hvar3.dar>sya  ztmd  bavainti "in  Jahresfrist  werden  Leichname,  dadurch dass  sie  auf  der  Erde  niedergelegt  dem Licht  und  der  Sonne  ausgesetzt  sind,  zu Erde"  V.  7. 46'';  45'*.
Komp.  mit  NP.  im  1.  Glied.  —  Pü.:  röhüh apar   mhumhih.    —   ')   In  NA.  fälschlich   ge-
■  j.  raoätna'vant-  Adj.  'lichtvoll,  leuch- tend';   °vant?m  yaba  manhfm  Az.  6;  —
barisma    .  .    'vantint     (ASm.     statt    n.) bämlM  YtJj.  55. 5.  unter  taoiaHOr.
•  p.  rautah-n,  'Fluss,  Strom':  adam  niy-
astsyam  imäm  yuviyäm  (sd.)  kt^lanaiy kacä  pirävJ'  nUma"  'Ic^  (NS.)  .  .  abiy *draya'  lyt^  hacä  pSrsH^  aitiy  ". .  vom Fluss  Nil  mit  Namen"  zum  Meer  . ."  D.
```


## [2026-09-07T01:49:30.064Z] TOOL CALL #75: WebSearch

```json
{
 "query": "Avestan Ǝrəxša Arash archer etymology \"bear\" OR \"bright\" Proto-Iranian *r̥xša"
}
```


### [2026-09-07T01:49:37.393Z] TOOL RESULT

```
Web search results for query: "Avestan Ǝrəxša Arash archer etymology "bear" OR "bright" Proto-Iranian *r̥xša"

Links: [{"title":"Names with \"bear\" in Meaning - Behind the Name","url":"https://www.behindthename.com/names/meaning/bear"},{"title":"Meaning, origin and history of the name Arash - Behind the Name","url":"https://www.behindthename.com/name/arash"},{"title":"Persian Mythology Origin Names - Behind the Name","url":"https://www.behindthename.com/names/origin/persian-mythology"},{"title":"Arash","url":"https://en.wikipedia.org/wiki/Arash"},{"title":"ĀRAŠ - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/aras-avestan-erexsa/"},{"title":"Arash","url":"https://mythus.fandom.com/wiki/Arash"},{"title":"Arash (name)","url":"https://en.wikipedia.org/wiki/Arash_(name)"},{"title":"Arash (disambiguation)","url":"https://en.wikipedia.org/wiki/Arash_(disambiguation)"},{"title":"Avestan","url":"https://en.wikipedia.org/wiki/Avestan"}]

Based on the search results, here's what I found regarding the etymology of Avestan Ǝrəxša (Arash):

The name Arash derives from Avestan Ərəxša, of uncertain meaning, possibly from a root meaning "bear". However, the search results indicate that the exact etymology remains unclear.

Interestingly, the sources provide an alternative description of the name's meaning. In the Avesta, the name appears as 'Erekhsha' (Ǝrəxša) meaning "of the swift arrow, having the swiftest arrow among the Iranians" (Yasht 8.6). This epithet-based meaning seems to relate more directly to Arash's legendary role as an archer rather than to Proto-Iranian roots.

The search results do not provide specific information about Proto-Iranian *r̥xša or an alternative etymology meaning "bright." The most consistent information available suggests the etymology is uncertain, with "bear" being one possible interpretation, though the descriptive epithet "swift arrow" appears prominently in the Avestan texts themselves.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T01:49:42.912Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://www.behindthename.com/name/arash",
 "prompt": "Quote the etymology given for the name Arash (Avestan form, meaning, any 'bear' root)."
}
```


## [2026-09-07T01:49:44.065Z] TOOL CALL #77: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/aras-avestan-erexsa/",
 "prompt": "Quote what this Encyclopaedia Iranica article says about the name Ǝrəxša / Āraš: its Avestan attestation, epithet, and any etymological explanation."
}
```


### [2026-09-07T01:49:45.452Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T01:49:46.317Z] TOOL RESULT

```
# Etymology of Arash

**Avestan Form:** The name derives from Avestan _𐬆𐬭𐬆𐬑𐬱𐬀 (Ərəxša)_

**Meaning:** "of uncertain meaning, possibly from a root meaning 'bear'"

The web page notes that while the exact etymology remains unclear, linguistic scholars suggest a potential connection to a root word associated with bears, though this derivation is not definitively established.
```


## [2026-09-07T01:49:52.038Z] TOOL CALL #78: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%81%D8%B4",
 "prompt": "For the Persian entry درفش (derafš): give all etymologies listed (banner? awl? shining?) with Middle Persian/Avestan forms and any cited sources (Hasandust, Cheung)."
}
```


## [2026-09-07T01:49:56.856Z] TOOL CALL #79: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/lewk-\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B2\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D8%B2%D9%82\" \\\n \"https://www.etymonline.com/word/luster\" \\\n \"https://www.etymonline.com/word/illustrate\" \\\n \"https://en.wiktionary.org/wiki/%D9%84%D9%88%D8%B3%D8%AA%D8%B1\" \\\n \"https://abadis.ir/fatofa/%D9%84%D9%88%D8%B3%D8%AA%D8%B1/\" \\\n \"https://www.behindthename.com/name/arash\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 312, root Leuk/Leuqos: PIE *leuk- and its Iranian/Persian/Arabic/Latin/English descendants\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-07T01:49:59.768Z] TOOL RESULT

```
# درفش (Derfash) - Etymology Summary

## Primary Meanings
The Persian entry lists two distinct etymologies:

1. **Banner/Standard**: "standard, ensign, colours, banner"
2. **Awl**: A pointed tool

## Etymological Sources

**Middle Persian Form:**
The word derives from Middle Persian *drafš* meaning "banner," though the original script notation indicates "[Book Pahlavi needed]."

**Avestan Cognate:**
Related to Avestan *drafša-*, supporting the banner sense.

**Proto-Iranian Root:**
Hypothetical Proto-Iranian *\*drafš-* suggested to mean "to behave like a banner, fly up, shine, tremble."

## Cited Academic References
- Cheung, Johnny (2007) - *Etymological Dictionary of the Iranian Verb*
- Rastorgujeva & Edelʹman (2003) - *Etymological Dictionary of Iranian Languages*
- Horn, Paul (1893) - *Grundriss der neupersischen Etymologie*
- Steingass, Francis Joseph (1892) - *Comprehensive Persian–English Dictionary*

The documentation suggests multiple semantic layers: visual/material (banner, cloth) and luminous (shine, brightness).
```


### [2026-09-07T01:50:02.336Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/725ce2a9e0180acc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6d95912a0991b6ae.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3e9abc6863ecf92d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/61bc05266c9c70c7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d549ae4f0952659a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ff23ff9843ba49a4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2b71dd79d6afa780.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fe97f7a7a2d6a1ac.txt
```


## [2026-09-07T01:50:18.416Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\npages=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('n',len(pages))\nfor i,p in enumerate(pages):\n    if re.search(r'rauca-\\s*sb', p) or 'rauca- sb' in p or re.search(r'^rauca', p, re.M):\n        print('leaf',i,'printed≈',i-15)\n        m=re.search(r'rauca.{0,700}', p, re.S)\n        print(m.group(0) if m else p[:300])\n        print('---')\nEOF"
}
```


### [2026-09-07T01:50:19.637Z] TOOL RESULT

```
n 232
leaf 229 printed≈ 214
raucah- sb. ‘day’: Av. raocah- ‘light’, Phi. rüé, NPers. róz, Skt. rócas- ‘light’, pIE *leugos ($70, $107, $156.ID, ef. Gk. Xexó-s adj. ‘ight’. тамса nsn. ($119, $1851) DB 3.8. rauca-pati-và
(899, $133) asn. DB 1.20. raucabiš ipn. ($119, 51851) DB 1.38, 42, 56, 89f, 96; 2.26, 36, 42, 47, 56, 691, 98^; 3.181, 39, 47, 63, 68, 88f.
ташіаћ- sb. ‘river’ ($166): NPers. ra8, Skt. srólas- ‘current, river’, pIE *sreutos (5118.1, $156.П) to root *sreu- ‘flow’; perhaps same as Av. 6raotah-, with sandhi initial (Bthl. Саг. IP 1.§87.- n2, AW 800). rauta nsn. anacoluthic in naming phrase (wrongly gen.-abl. to stem таш-, Mt. MSLP 19.56-7, MB Gr. $167, $316) DZc 9.
Razé- sb. ‘Rakha’, а town m Persia: Elam. rak-q
---
```


## [2026-09-07T01:50:32.501Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\npages=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(215,232):\n    m=re.findall(r'\\b(1[6-9]\\d|2[01]\\d)\\b', pages[i][:200])\n    print(i, m[:5], '|', re.sub(r'\\s+',' ',pages[i][:80]))\nEOF"
}
```


### [2026-09-07T01:50:33.723Z] TOOL RESULT

```
215 [] | rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far and wide’ (GAv. düiré
216 ['207'] | e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) 
217 [] | n üv-nara- (§142). nàv- sb. ‘ship’: Skt. ndus, Gk. vais, Lt. nav-is, pIE *ndv- (
218 ['166'] | with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing’ + "wüdá- ‘abode’ (
219 ['167', '178'] | ‘I pierce (as with a spit)’, Gt. faran ‘to travel’. рамо[т- іаїу| nsn. past pte.
220 [] | tem (530, $148.I, 6154.1), ef. Av. posana- ‘battle’, Skt. pfiana- ‘battle, army’
221 ['186'] | r-, Gk. rarnp, Lt. pater, Gt. fadar, pIE *poler- (863.11, 875.1, 576.1, $154.II)
222 [] | -. — fra&aram asn. XPf 26f, 37. Fraéda- sb. ‘Frada’, a Margian rebel: Elam. pir-
223 ['172'] | 1; DSe 1°; DSE 1°; D8s 1^; DSt 1; рле 1°; DE 1; XPa 1; XPb 1; XPc 1; XPd 1; XPf 
224 [] | 2; 4.66. abara imf. ($40, $84, 5228.) DB 1.25, 55, 88, 94; 2.25, 34f, 40, 45, 54
225 [] | BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; DS) 1°; DSy 2; D'Sb 2
226 [] | 24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе1. [ma8]jiSta-ISàm] 
227 [] | ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1
228 [] | so a province of the Persian Empire, ‘Egypt’; тазе. sg. as sb., ‘Egypt’, a provi
229 [] | d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; 
230 [] | am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71
231 [] | 1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve. z$apa-
```


## [2026-09-07T01:50:52.274Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\ngrep -n -i \"leuk-, leuk\\|raoxšna\\|raoxsna\" WLD_Bd2_pages.txt | head -10\necho \"--- find 'leuk' occurrences ---\"\ngrep -n -o -i \"leuk[a-z-]*\" WLD_Bd2_pages.txt | head -20\necho \"--- page 408 ---\"\npython3 - <<'EOF'\nimport re\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i,p in enumerate(pages):\n    if re.search(r'leuk', p) and ('lux' in p or 'luna' in p or 'lustrum' in p):\n        print('leaf',i)\n        print(p[:800])\n        break\nEOF"
}
```


### [2026-09-07T01:50:53.599Z] TOOL RESULT

```
27107:ruksd- „glanzend“,                     ay.    raoxsna- „glanzend'‘                  (= ahd.      liehsen)          f.   „Licht'‘
--- find 'leuk' occurrences ---
27309:leuk
--- page 408 ---
725
leaf 415
                                                           leuq-                                          411

  auf Grund des -es-St aisL lyrr i^letihisa-) „Lub, Gadus pollichius^* (von
der hellen Farbe der Seiten und des Bauches des Fisches), aisL lysa
„Merluccius vulgaris, Merlan, Kurnmel^ norw. lyswg ds. (Fick III* 373,
Falk-Torp u. lyr^ lysing^ anders gebildete Namen hellgefarbter Fische
sind schwed. Idja^ Idga „Abraiiiis alburnus'* aus Havgidn^ nbd. Lange „Cy-
prinus alburnus und leuciscus'‘) mhd. lieJisen „hell“ {leuhsna-^ == av. raoocs-
                                                  ;



na-)^       aisl.   Ijos „Licht'‘ i^leuhsa-)^ lysa „leuchten,                 glanzen, hell machen, er-
klaren, Yerkunden‘‘ == ags. lioxan^ llxan „leuchten“.
  Lit. laillcas „blassig“, laiikas „
```


## [2026-09-07T01:50:58.640Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nimport re\npages=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(410,414):\n    print('=== leaf',i)\n    print(re.sub(r'\\n+','\\n',pages[i][:1100]))\nEOF"
}
```


### [2026-09-07T01:50:59.919Z] TOOL RESULT

```
=== leaf 410
406                                                leu-, lau   — leu
Hes., AavQLov^ Johansson aaO..                       Brugmann II^ 1, 348;                 air.           junger Zm,
gen. Itac (zweisilbig) „Stein‘" (kelt. Hviank-^ aus idg. leuank- oder -onk-l;             ''
Stokes BB. 19, 91, Fickll^ 249, Pedersen                               KG. I 251);
     as.   leia            mhd. nlid. leie j,Schiefer“ aus leuion ? ? (Pick II ^
                     „Steinplatte“,
249; Kluge ^ u. Lei zw. abgelehnt von Weigand Hirt u. lei),
                                       ;
  Lat. lausiac „kleine Steinstiicke oder Schlacken im Bergwerksbetrieb“,
lausa „Steinplatte“ sind gr. oder kelt. Lw., s. Yf. LE Wb.^ m. Lit.    Houdho-                           —
             (Prellwitz u. Xdag)            bleibt     fern.     — Nach saxuni secare u. dgl. hat
                                                                                          :
man Beziehungen zu leti- „schneiden^‘ erwogen (z. B. Prellwitz aaO., BoL
sacq       s. V.).
3. leu-       oder lau Schallwz.             (s
=== leaf 411
                                                                 ;
                                                                       leu-                                      407
leii'   „abschneiden, trenneii, loslosen'*, auch Wzf. leua^ und len - Idu-                              :      (: IS),
        z.   T. leu-s-.
  Ai.        lundti^         lunoti ^sclineidet, schneidet            ab'*, Vmct- „abgeschnittenj ge-
schnitten^'          (ir.    lon)^       lamtra-           n.       lam- ds. (: gr, Xaiov^ aisl.
                                                                „Sichel‘^                         ds.),
lava-m. ,das Schneiden,
                 5
                                                       Abschneiden, Schur, Wolle, Haar, Abschnitt,
Stuck% lava- „schneidend'', lavaka- m. .,Abschneider, Maher'‘;
   gr. ?.v(o „lbse ; zerreiSe, vertilge usw.^‘ (unbereclitigte Scheidung in                                    zwei
Worte bei Prellwitz^             kva ..Auflosung, Trennung^^, kvoig „L6sung‘*,
                                           s.       v.),
kvx^
=== leaf 412
                                                                                    ^
408                                                leuq-
bedenklich (s. Solmsen Unt.          dessen Yerb. mit sXog „feuchte, frucht-
bare Niederung‘‘ freilich nicht iiberzeugt).                   —
                                                 Da6 gr. XsvQog „offen, eben
(vom Gelande)^* hieher gehore (Pick       538) etwa als „abgescbnitten = ge-
rodet“ Oder „frei geinacht‘‘, und gar (ibd.) lura „OfFnung des Schlauches,
Schlauch; Bauch“ damit zusammenhange (Bed.?), ist wenig glaubwiirdig
(unricbtig iiber lura Siitterlin IP. 29, 128;                       iiber   aisl.       Ijore „Licht6fFiiung“
s.   u.    leuq „leuchten“).
     s-Erw.:     got. fraliusan,        ahd. farliosan „verlieren“;   ags. leoran (schw. V.
mit starkem Ptc. ~loren\ Pick                       377) „weggehn, scheiden“; got. fralus-
nan .,verloreDgehn“,            aisl.   losna          locker werdeii“, got. fralusts^ ahd.
forlust „Yerlust“;            got. laus           leer,    eitel,    nichtig“, aisl. lauss „frei
=== leaf 413
                                                               leuq-                                                          409
Schmiick“, ruhmant „glanzeiid‘‘                           (vgl.    den germ. lat. -mm-St.); rocas-^ rods-
n.,     av. raocah-^      ap.              rancali- n. „Licht,         Leuchte, bes. des Himmels**, ai.
ruksd- „glanzend“,                     ay.    raoxsna- „glanzend'‘                  (= ahd.      liehsen)          f.   „Licht'‘
(= lat. luna^ mir. liian^ apr. lauxnos, abg. Iwia^ schwundstufig gr. Xv^^og;
auf diesem -es-St. beruhen auch lat. lUstrare^ lucuhrare^ ags. lioxan^ aisl.
Ijds^        cymr. Hitched^           lit.   Kikestis),
      Arm. lois „Licht“,                   lusin „Mond‘^ (wie oeXrjvrj                :   oelag und        lat.    Inna usw.
ein nach Meillet Bull. soc. lingu. 59.                            LXV erst einzelspracblicher Ersatz von
*men{e)s-)y hisn „weiBer Fleck                       im Auge‘* (s aus q nach n\ oder allenfalls
zur Wzf. auf             s.          u.;    Hiibschmann Arm. Gr. I 453, Pedersen KZ. 39, 401),
```


## [2026-09-07T01:51:13.006Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC leuk ===\"; grep -n -o -iE \"leuk[a-z-]{0,8}\" IEC.txt | sort | uniq -c | sort -rn | head\necho \"=== IEC leukos entry ===\"; grep -n -i \"leukos\\|leuk-o\" IEC.txt | head -5\necho \"=== SKT light ===\"; grep -n -i \"^light\\|light (1)\\|Light, brightness\" SKT.txt | head -5\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%81%D8%B4\" --note \"page 312, Persian derafš: banner vs 'shine' (Proto-Iranian *drafš-), against Nourai's grouping under *leuk-\" 2>&1 | tail -2"
}
```


### [2026-09-07T01:51:14.366Z] TOOL RESULT

```
=== IEC leuk ===
      2 9740:leuk-
      2 13118:leuks-
      1 9748:leuks-
      1 9739:leuksnio
      1 9739:leuks-
      1 9736:leuks-
      1 9736:leuk-
      1 9735:leukos
      1 9735:leuk
      1 9734:leukoph
=== IEC leukos entry ===
9731:bright; brightness', etc. Cf. louk-, luk-, etc. WP II, 408-411 Arm. (vowel ambig.) lusat ‘illumination’; Osc. in Lat. Loucetius (epithet of Jove); Gaul. leucetio-, loucetio- (in names); W Hugas, f. (*daybreak, fr. *leukostis or *loukost-) beside llugaint, m. (Cglitter', from a type *leukonti-, *louk-); Go. liuhap, n. “light; OHG lioht, OE leoht, id. Cf. Hitt. lukkitti, a. adv. ‘next day, tomorrow”
9735:leukos, à (louk-) “light, white; light, bright- ness'. Cf. louk-, luk-. WP II, 408 Skt. rókab, rokáh; rokas, n. "light, brilliance’; Av. raoco, n. ‘glitter’; Ober, rauca- ‘day’; Myc. & Gk. leukós, adj. "light, bright, white’; W llug, pl. -ion, m. ‘gleam’; Li. laükas, adj. *white-blazed'; laükis, io, m. (“blaze on fore- head”: Skt. rocáh ‘radiant; radiant one")
=== SKT light ===
10396:LIGHT
10416:lighten  (1),  to  iltuminatr.  flash.  (E.) 1.  IwrHANk.,  to  shine  as  li^btning ;  'it Hghtfns*  M.  E.  UgkUntn,  more  coriecily Hfht-n-m^    w1mc«    tht    •<»•    \a   lonm&v^.
10423:light  <3;,  to  mlight.  settle,  dcsocnd. (E.)  M.  E.  iihUn.  A.  S.  /M/tfi».  verb, to  alight  bom.  lit.  to  make  light,  relierc a  hone  of  his  borden.  *  A.  S.  USAt^  Light (above).  The  seose  '  to  descend  spon  * (the  earth)  is  aecondary,  doe  to  the  com- pleted actioo  of  descending  horn  a  horse.
10425:lighten  (3),  to  alight  oo.  (E.)  £x- teiulcd  from  light  (3)  above,
10426:lighter,  a  boat  for  unlading  ihipi. (Du. )  Borrowed  from  Du.  htrter,  a lighter,  i.e.  nnloadcr.  — Du. /r^,  lifjht.
python3: can't open file '/home/sfmqrb/git/rishe/data/verification/sources/refs/tools/fetch_source.py': [Errno 2] No such file or directory
```


## [2026-09-07T01:51:18.202Z] TOOL CALL #85: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%81%D8%B4\" --note \"page 312, Persian derafs: banner vs shine (Proto-Iranian *drafs-), against Nourai grouping under *leuk-\" 2>&1 | tail -2\nsed -n '10396,10400p' data/verification/sources/refs/SKT.txt"
}
```


### [2026-09-07T01:51:19.611Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f2027aaa926815f4.txt
LIGHT
«49
Iilflslong:  see  Iiiro.
Xiift  ( I ),  to  raise ;  see  I«oft..
Lift  (a),  to  steal.  (E.)  We  mak  of a  shop-ti/ttr,  a  thief;  see  Shak,  Troil.  i. i.  109.  Properly,  the  verb  should  be  liff. An  E^  word,  but  only  preserved  in  Gothic. Cf  Goth,  hiifan,  to  -itcal ;  hliftus,  a  thief. Cognate  with  L.  cUpen,  to  steal.     Golh.
```


## [2026-09-07T01:53:35.482Z] TOOL CALL #86: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg312.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/312.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-07T01:53:35.567Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-07T02:00:08.207Z] TOOL CALL #87: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk312.py <<'PY'\n# -*- coding: utf-8 -*-\nimport json\n\nS_PIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/lewk-\"\nS_RUZ = \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B2\"\nS_RIZQ = \"https://en.wiktionary.org/wiki/%D8%B1%D8%B2%D9%82\"\nS_LUSTER = \"https://www.etymonline.com/word/luster\"\nS_ILL = \"https://www.etymonline.com/word/illustrate\"\nS_LUSTRFA = \"https://en.wiktionary.org/wiki/%D9%84%D9%88%D8%B3%D8%AA%D8%B1\"\nS_ABADIS = \"https://abadis.ir/fatofa/%D9%84%D9%88%D8%B3%D8%AA%D8%B1/\"\nS_ARASH = \"https://www.behindthename.com/name/arash\"\nS_DERAFSH = \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%81%D8%B4\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1,\n \"lang\": \"Avestan\",\n \"words\": \"raočah; raoč-xšaema, raoxšna; a-raxša; aiwi-raocya\",\n \"verdict\": \"disputed\",\n \"derivation\": (\n  \"Three of the four items are solid. (a) Av. raocah- n. 'light, luminary (esp. of heaven)' \"\n  \"(Bartholomae, AiW cols. 1489-91: \\\"j., g. raocah-, p. raucah- n. 1) 'Leuchte' (bes. des Himmels)\\\") \"\n  \"is the inherited -es-/-os- neuter *leuk-os of the root, with the regular Indo-Iranian changes \"\n  \"PIE *l > Ir. r and *k > č before a front vowel (Skt. rócas-, rócate). \"\n  \"(b) Av. raoxšna- 'bright, shining' (AiW 1488) = *rauk-s-na-, the same -s- stem that underlies \"\n  \"Lat. lūna (*leuk-s-nā), OPruss. lauxnos, OHG liehsen; it is the direct ancestor of NP rōšan. \"\n  \"(c) Nourai's 'aiwi-raocya' is Av. aiwi.raocaya- 'to illuminate, light up' (AiW s.v. raok- 'leuchten': \"\n  \"\\\"mit aiwi 'beleuchten, bescheinen': yaθ hī stārąm .. aiwi.raocayąnte\\\", V.19.23), the ancestor of NP afrūxtan \"\n  \"(Horn no. 94). BUT (d) 'raoč-xšaema' is not an attested Avestan word: Bartholomae's raoc-/raoxšna- family is \"\n  \"raoxšna-, raoxšnay-, raoxšnav-, raoxšnā-, raocana-, raocah-vant-, raocas-caēšman-, raocas-pairišta- — nothing like \"\n  \"raoč-xšaema. It is Nourai's own segmentation of raoxšna- as raoč + xšaē- (hence his cross-reference to root Ksei 2, \"\n  \"i.e. xšay-/xšaēta- 'shine'); the printed page (pdf 312) does show 'raoč-xšaema', so the JSON is faithful and the \"\n  \"odd form is the book's. And (e) 'a-raxša : bright' does not exist either: the Avestan word behind NP Āraš is \"\n  \"Ǝrəxša-, which Bartholomae (AiW s.v. ərəxša-) gives only as \\\"EN. eines berühmten iranischen Schützen\\\" \"\n  \"(Yt.8.6 tiγriš .. yim aŋhat ərəxšō xšviwi.išuš xšviwi.išvatəmō airyanąm 'the arrow which Ǝ. shot, the best archer \"\n  \"of the Aryans'), with no meaning 'bright'; its etymology is uncertain (a root meaning 'bear' is the usual guess). \"\n  \"Hence the node is disputed for those two items.\"\n ),\n \"derivation_fa\": (\n  \"سه صورت از چهار صورت این جعبه درست است: اوستایی raocah- «روشنایی، فروغ (به‌ویژه اختران آسمان)» همان ستاک \"\n  \"خنثای *leuk-os هندواروپایی آغازین است با دو دگرگونی آوایی منظم ایرانی، یعنی l هندواروپایی > r و k > č پیش از واکهٔ پیشین؛ \"\n  \"raoxšna- «روشن، درخشان» ساخت *rauk-s-na- است، همان پسوند -s- که در lūna لاتینی هم دیده می‌شود و نیای «روشن» فارسی است؛ \"\n  \"و aiwi.raocaya- «روشن کردن، برافروختن» (بارتولمه، ذیل raok-) نیای «افروختن» است (هرن، شمارهٔ ۹۴). \"\n  \"ولی «raoč-xšaema» در اوستا نیست و در فرهنگ بارتولمه چنین ترکیبی وجود ندارد؛ این تجزیهٔ خودِ نورایی از raoxšna- است \"\n  \"(از این‌رو ارجاع او به ریشهٔ Ksei 2 = xšay-/xšaēta- «درخشیدن»)؛ تصویر صفحهٔ چاپی نشان می‌دهد که همین صورت در کتاب آمده، \"\n  \"پس خطا از کتاب است نه از خوانش اسکن. همچنین «a-raxša» با معنای «روشن» وجود ندارد: صورت اوستایی نام «آرش» \"\n  \"Ǝrəxša- است که بارتولمه تنها آن را نامِ کمانگیر نامدار ایرانی می‌داند و هیچ معنای «روشن» برای آن نمی‌آورد؛ \"\n  \"ریشه‌شناسی آن نامعلوم است و حدسِ رایج معنای «خرس» است. بنابراین ادعای نورایی در این دو مورد پذیرفتنی نیست.\"\n ),\n \"sources\": [S_PIE, S_ARASH],\n \"ref_check\": [\n  {\"ref\": \"HRN:23\", \"status\": \"supports\", \"note\": \"Horn p.23 no.94 (HRN.txt leaf 44): \\\"efrōxten 'anzünden, erleuchten' ... aw. aiwi + √ruc- 'anzünden'; phlv. afrōxtan, afrōcīn ...; skr. abhi + √ruc-\\\" — exactly Nourai's aiwi-raocya > afrūxtan arrow.\"},\n  {\"ref\": \"HRN:136\", \"status\": \"supports\", \"note\": \"Horn p.136 no.610 (leaf 157): \\\"ruxš (rexš) 'Glanz, Licht', ruxšīden ... aw. vergl. raoxšna- 'glänzend, leuchtend, strahlend'; ai. rukṣá-\\\".\"},\n  {\"ref\": \"HRN:140\", \"status\": \"supports\", \"note\": \"Horn p.140 nos.629-631 (leaf 161): \\\"ap. raucah- 'Tag'; aw. raocah- 'Licht'; phlv. rūc, rōcīk (arm. LW. rocik)\\\"; \\\"rōzen 'Fenster' ... aw. raocana-\\\"; \\\"rōšen 'leuchtend, hell' ... aw. raoxšna-\\\".\"},\n  {\"ref\": \"SYN:470\", \"status\": \"supports\", \"note\": \"Buck 7.25 WINDOW (printed p.470-471, SYN.txt leaf 519-520): \\\"Av. raocana- (NPers. rōzan) : Skt. rocana- 'bright', locana- 'eye', etc. Barth. 1489\\\" — supports روزنه in the Persian box below.\"},\n  {\"ref\": \"SYN:991\", \"status\": \"supports\", \"note\": \"Buck 14.41 DAY, running head 'TIME 991': the table gives \\\"Av. ayan-, azan-, OPers. rauca\\\" for 'day'.\"},\n  {\"ref\": \"BQT:31\", \"status\": \"partial\", \"note\": \"Borhan-e Qate' printed p.31 (BQT_v1_pages.txt leaf 241) is indeed the آرش entry (\\\"نام پهلوانی بوده ایرانی از لشکر منوچهر ... تیری از آمل بمرو انداخت\\\"); Mo'in's footnote there is only half legible in the OCR (\\\"... اوستا ...\\\") and in any case Borhan gives the archer, not a word meaning 'bright'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"AiW cols. 1488-1491 s.v. raoxšna-, raocah-, raok-; s.v. ərəxša-\", \"stance\": \"partial\", \"note\": \"supports raocah-, raoxšna-, aiwi.raocaya- verbatim; but \\\"ərəxša- a EN. eines berühmten iranischen Schützen\\\" has no gloss 'bright', and no compound raoč-xšaema exists in the dictionary\"},\n  {\"src\": \"POK\", \"where\": \"pp. 687-690 s.v. leuk̂- (POK_full.txt 'lehuk-')\", \"stance\": \"supports\", \"note\": \"\\\"rocas-, rocis- n., Avestan raocah-, ap. raucah- n. 'Licht, Glanz, esp. of heaven', Avestan raoxšna- 'gleaming'\\\"\"},\n  {\"src\": \"HRN\", \"where\": \"nos. 94, 610, 629-631\", \"stance\": \"supports\", \"note\": \"Horn derives afrōxtan from aiwi+ruc- and rōšan/ruxš from raoxšna-\"},\n  {\"src\": \"AVG\", \"where\": \"grep of AVG.txt\", \"stance\": \"silent\", \"note\": \"Jackson's Avesta Grammar has no lexical entry for these forms\"}\n ]\n})\n\nnodes.append({\n \"id\": 2,\n \"lang\": \"Persian\",\n \"words\": \"rŭz «روز ( روزنه ، فروزان ، فروغ )»; rošan «روشن»; raxš «رخش ( درخش ، درفش ۱ )»; Ââraš «آرش»; afrŭxtan «افروختن»\",\n \"verdict\": \"disputed\",\n \"derivation\": (\n  \"The core of the box is right. روز rūz 'day' < MP rōz [YWM; lwc] 'day' (MacKenzie, CPD p.72: \\\"rōz [YWM < A ywm; lwc | M rwc/z, N ~] day\\\") \"\n  \"< OP raucah-/Av. raocah-; Wiktionary gives the same chain روز < MP rōz < OP raucah- < PIr. *ráwčah < PIE *léwk-os. \"\n  \"روزنه rowzane 'small window' is MP rōzan (CPD: \\\"rōzan [lwcn | N ~] window\\\") < Av. raocana- 'window' (Buck 7.25). \"\n  \"فروزان/فروغ are *fra- + rauk- formations (MP frōz-, NP forūɣ 'radiance', Borhan p.147-148 s.v. افروغ 'بمعنی فروغ و روشنی و تابش و پرتو'). \"\n  \"روشن rōšan < MP rōšn [lwšn] 'light, bright' (CPD p.72; Nyberg II 'rōšn ... — Av. (1488) raoxšna-; MPrthPrs rwšn; Paz. rōs(a)n; NP raušan') \"\n  \"< Av. raoxšna-. رخش raxš/ruxš 'gleam' and درخش deraxš/deraxšīdan are the same stem (Horn no.610; Hübschmann, Pers. Studien: \\\"ruxš (raxš) 'Glanz', \"\n  \"vgl. zd. raoxšna- 'glänzend'\\\"; Aryanpur, printed p.312, note: 'واژه‌های فارسی آرخش و درخش و درخشیدن نیز از همین واجریشه‌اند'); \"\n  \"Horn explains duruxš/deraxš as *ati- + ruxš. افروختن afrūxtan < MP abrōxtan/afrōxtan, pres. abrōz- (CPD p.4: \\\"abrōxtan, abrōz- ['pl.whtn', 'phlwc- | M brwxt, N afrōxtan, afrōz-] light, kindle, illuminate\\\") \"\n  \"< Av. aiwi.raocaya-. TWO items fail: (1) درفش ۱ 'banner' is from MP drafš < Av. drafša- 'banner' (Horn no.553: \\\"direfš 'Fahne, Banner': aw. drafša-\\\"), and even the \"\n  \"'shine' sense (derafšīdan, derafšān) is put by modern Iranian etymology under Proto-Iranian *drafš- 'to fly up, shine, tremble' (Cheung 2007; ESIJa; Wiktionary درفش), \"\n  \"not under *leuk-; Horn only floats a possible contamination with duruxš. (2) آرش Āraš is Av. Ǝrəxša-, a personal name of uncertain etymology (possibly 'bear'), \"\n  \"not a word meaning 'bright' (see node 1).\"\n ),\n \"derivation_fa\": (\n  \"هستهٔ این جعبه درست است: «روز» از فارسی میانهٔ rōz (نوشتهٔ lwc، مکنزی ص ۷۲) و آن از پارسی باستان raucah- / اوستایی raocah-؛ \"\n  \"«روزنه» از فارسی میانهٔ rōzan و آن از اوستایی raocana- «پنجره»؛ «فروزان» و «فروغ» ساخته‌های پیشوند fra- با ستاک rauk- اند؛ \"\n  \"«روشن» از فارسی میانهٔ rōšn (نیبرگ: rōšn، اوستایی raoxšna-، بارتولمه ستون ۱۴۸۸) و آن از اوستایی raoxšna-؛ \"\n  \"«رخش/درخش/درخشیدن» نیز از همین ستاک raoxšna- است (هرن شمارهٔ ۶۱۰؛ هوبشمان: ruxš (raxš) «فروغ» هم‌ریشه با raoxšna- اوستایی؛ \"\n  \"و آریان‌پور در ص ۳۱۲ همین را می‌گوید)؛ «افروختن» از فارسی میانهٔ abrōxtan/afrōxtan (ستاک حال abrōz-) و آن از اوستایی aiwi.raocaya-. \"\n  \"اما دو مورد پذیرفتنی نیست: «درفش ۱» (به معنی عَلَم) از فارسی میانهٔ drafš و اوستایی drafša- است (هرن شمارهٔ ۵۵۳) و حتی معنای «درخشیدن» آن را \"\n  \"ریشه‌شناسی امروزی (چونگ ۲۰۰۷، ویکی‌واژه) به ایرانی آغازین *drafš- «برافراشته شدن، درخشیدن، لرزیدن» می‌برد، نه به *leuk-؛ \"\n  \"و «آرش» نامی است با ریشهٔ نامعلوم (اوستایی Ǝrəxša-) و معنای «روشن» برای آن سندی ندارد. پس در این دو مورد پژوهش امروزی ادعای نورایی را رد می‌کند.\"\n ),\n \"sources\": [S_RUZ, S_DERAFSH, S_ARASH],\n \"ref_check\": [\n  {\"ref\": \"BQT:97\", \"status\": \"not_found\", \"note\": \"printed p.97 of Mo'in's Borhan (BQT_v1_pages.txt leaf ~307-313) is the ارج/ارد/اردو/ارژنگ range — nothing on rūz, rōšan, raxš, Āraš or afrūxtan. Page reference appears to be wrong.\"},\n  {\"ref\": \"BQT:147\", \"status\": \"supports\", \"note\": \"printed p.147-148 (leaf 363) is exactly the ا ف ر page: 'افروختن ... بمعنی روشن کردن آتش و چراغ باشد', 'افروز ... بمعنی روشن و روشن کردن', 'افروغ ... بمعنی فروغ و روشنی و تابش و پرتو', footnote 'افروزیدن - رک: افروختن'.\"},\n  {\"ref\": \"BQT:976\", \"status\": \"partial\", \"note\": \"printed p.976 (BQT_v2_pages.txt leaf 436) is an unreadable OCR page in the روس geography article; the material Nourai wants is on the neighbouring pages: p.973 footnotes 'روزن ... اوستا raocana- (پورداود)' and 'روزی ... پهلوی rōčīk = ارمنی ročik (رزق یومیه), هوبشمان', and p.978 footnote 'روشن: پهلوی rōšan، اوستا raoxšna- (صفت به معنی روشن) «بارتولمه»'. So the claim is supported, the page number is off by ~2.\"},\n  {\"ref\": \"FSF:176\", \"status\": \"not_found\", \"note\": \"in the scan on disk (FSF_pages.txt; printed = leaf-3) p.176 is the تناور/تن‌آسان page. Noushin's relevant entries درفشان (بر وزن درخشان) = رخشیدن and درفشیدن are on pp.231-232 (leaves 234-235) — the content exists but not at p.176 in this printing (the edition of the scan is not identified).\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD pp. 4 and 72\", \"stance\": \"supports\", \"note\": \"\\\"abrōxtan, abrōz- ... N afrōxtan, afrōz-] light, kindle, illuminate\\\"; \\\"rōšn [lwšn | M rwšn, N rōšan] light; bright\\\"; \\\"rōz [YWM; lwc] day\\\"; \\\"rōzan [lwcn] window\\\"; \\\"rōzīg [lwcyk | N rōzī] daily bread, sustenance\\\"\"},\n  {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, s.vv. rōč, rōšn, rōcēnītārēh, rōcik\", \"stance\": \"supports\", \"note\": \"\\\"rōšn [lwšn'] ... — Av. (1488) raoxšna-; MPrthPrs rwšn; Paz. rōs(a)n; NP raušan\\\"; \\\"rōč [YWM; lwc] day\\\"; index 'raocah-: rōč'\"},\n  {\"src\": \"HUB\", \"where\": \"Persische Studien (HUB.txt lines 8324-8334)\", \"stance\": \"supports\", \"note\": \"\\\"rōšan 'hell' zd. raoxšna-\\\"; \\\"ruxš (raxš) 'Glanz', vgl. zd. raoxšna- 'glänzend'\\\"\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur, printed pp. 311-312 (pdf pages 311-312)\", \"stance\": \"supports\", \"note\": \"the روز and روشن entries list Av. raocah-/raoxšna-, OP rauca, Pahl. rōč/rōšan/rōšnīh, Skt. rocas/rocana, Gk. leukos, Lat. lux/lumen/luna, Eng. light; the note adds 'واژه‌های فارسی آرخش و درخش و درخشیدن و آرخشیدن نیز از همین واجریشه‌اند'\"},\n  {\"src\": \"HRN\", \"where\": \"nos. 553, 610, 629-631, 94\", \"stance\": \"partial\", \"note\": \"supports rūz/rōzan/rōšan/ruxš/afrōxtan, but no. 553 derives direfš 'Fahne, Banner' from Av. drafša- and only speculates about the 'Glanz' sense being contaminated with duruxš (= ati- + ruxš)\"},\n  {\"src\": \"FSF\", \"where\": \"Vazhe-namak pp. 231-232 s.vv. درفشان، درفشیدن\", \"stance\": \"partial\", \"note\": \"\\\"درفشان (بر وزن درخشان) [صفت فاعلی از درفشیدن] = رخشیدن\\\" — Noushin equates the Shahnameh word with رخشیدن, which is what Nourai relies on for درفش ۱, but this is a Shahnameh gloss, not an etymology\"}\n ]\n})\n\nnodes.append({\n \"id\": 3,\n \"lang\": \"Arabic\",\n \"words\": \"rezq\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Arabic رِزْق rizq 'daily food, sustenance' is an Iranian loan, but strictly from the Middle Persian derivative rōzīg \"\n  \"'daily ration, daily bread' (rōz 'day' + adjectival -īg), not from rōz alone — which is what Nourai's note \"\n  \"('Derived from Persian rūz') means in shorthand and what the chart's Persian box (روز) implies. \"\n  \"Asbaghi, Persische Lehnwörter im Arabischen p.135: \\\"rizq: 'tägliche Nahrung' — pers. rūzī, mp. rōcīk 'daily bread', \"\n  \"aw. raocah- / ap. rauca 'Tag', syr. rezqā, mand. rizqa\\\"; his introduction cites the pair as a model case \"\n  \"(\\\"pers. rūzīg, mp. rōzīg > ar. rizq\\\") for the Persian ū > Arabic i and Persian g > Arabic q correspondences. \"\n  \"Addi Shir p.72: 'الرزق: تعریب روزی وما بمعناه، وأصل روزی نسبة إلى روز وهو النهار' ('rizq is the Arabicisation of rōzī …, \"\n  \"rōzī being a nisba to rōz, i.e. day'). Wiktionary s.v. رزق likewise: 'Derived from Middle Persian rōzīg'. \"\n  \"The loan was fully nativised into a triliteral root r-z-q (razaqa 'to provide', rāziq, razzāq, arzāq) and is Qur'anic, \"\n  \"so the borrowing is pre-Islamic — via Aramaic/Syriac trade language (Syriac rezqā, Mandaic rizqā) according to Asbaghi's parallels.\"\n ),\n \"derivation_fa\": (\n  \"عربیِ «رِزق» وام‌واژه‌ای ایرانی است، اما دقیقاً از مشتقِ فارسی میانه rōzīg «خوراک روزانه» (rōz «روز» + پسوند نسبتِ -īg) \"\n  \"گرفته شده، نه یکسر از rōz؛ همین است مقصود یادداشت نورایی. اصبغی در «وام‌واژه‌های فارسی در عربی» ص ۱۳۵ می‌نویسد: \"\n  \"rizq «خوراک روزانه» از فارسی rūzī و فارسی میانه rōcīk، و آن از اوستایی raocah-/پارسی باستان rauca «روز»، با صورت‌های سریانی rezqā و مندایی rizqā؛ \"\n  \"و در مقدمه همین جفت را نمونهٔ ابدال ū فارسی به i عربی و g فارسی به q عربی می‌آورد. ادی شیر ص ۷۲ نیز می‌گوید: «الرزق تعریب روزی … وأصل روزی نسبة إلى روز وهو النهار». \"\n  \"این وام‌واژه در عربی به ریشهٔ سه‌حرفی ر-ز-ق تبدیل شده (رزق، ارتزق، رازق، رزّاق، ارزاق) و چون در قرآن آمده، وام‌گیری پیش از اسلام و به احتمال با میانجی آرامی/سریانی بوده است. \"\n  \"ادعای نورایی درست است.\"\n ),\n \"sources\": [S_RIZQ],\n \"ref_check\": [\n  {\"ref\": \"AFM:72\", \"status\": \"supports\", \"note\": \"Addi Shir, AFM_pages.txt leaf 73 (printed p.72, the ر section): '(الرِزق) تعریب روزی وما بمعناه واصل روزی نسبة الى روز وهو النهار. وقالت فيه العرب رزق وارتزق الى غير ذلك' — literally Nourai's arrow; the same page also has '(الروزنة) تعریب روزنه وهي الکوة'.\"},\n  {\"ref\": \"PLA:135\", \"status\": \"supports\", \"note\": \"Asbaghi p.135 (PLA_pages.txt leaf 149, running head 135): \\\"rizq: 'tägliche Nahrung' pers. rūzī, mp. rōcīk 'daily bread', aw. raocah / ap. rauca 'Tag', syr. rezqā, mand. rizqa\\\"; also ʾarzāq, rāziq, razzāq referred to this entry.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"CPD p.72 s.v. rōzīg\", \"stance\": \"supports\", \"note\": \"\\\"rōzīg [lwcyk | N rōzī] daily bread, sustenance\\\" — the exact Middle Persian source form\"},\n  {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p.973, Mo'in's footnote on روزی\", \"stance\": \"supports\", \"note\": \"'روزی ... از: روز + ی (نسبت)، پهلوی rōčīk = ارمنی ročik (رزق یومیه) «هوبشمان»' — Mo'in himself equates Pahl. rōčīk with Arabic rizq yawmiyya\"},\n  {\"src\": \"FVQ\", \"where\": \"grep of FVQ.txt / FVQ_pages.txt for rizq\", \"stance\": \"silent\", \"note\": \"Jeffery's Foreign Vocabulary of the Qur'an has no entry for رزق (he treats it as naturalised Arabic)\"},\n  {\"src\": \"AFA\", \"where\": \"grep of AFA.txt for rizq/rezqa\", \"stance\": \"silent\", \"note\": \"Fraenkel's Aramäische Fremdwörter does not list the word, so the Aramaic forms are not claimed as the source there\"},\n  {\"src\": \"SOD\", \"where\": \"Gharib nos. 8600-8602 rwcyk\", \"stance\": \"supports\", \"note\": \"Sogdian rwcyk (rōčīk) 'daily' shows the same -īk derivative was pan-Middle-Iranian\"}\n ]\n})\n\nnodes.append({\n \"id\": 4,\n \"lang\": \"Persian\",\n \"words\": \"rezq «رزق»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"A round trip: MP rōzīg 'daily ration' > Arabic rizq (node 3) > New Persian رزق rezq 'daily bread, provision', now felt as an Arabic word \"\n  \"and carried into Persian together with its Arabic morphology — the broken plural ارزاق arzāq and the agent nouns رزّاق razzāq and رازق rāzeq \"\n  \"(the extra forms printed in the box), plus verbs like مرتزق شدن. Mo'in accordingly tags رزق as [ع.] (Arabic) in his Farhang, \"\n  \"and Mo'in's own footnote in Borhan (p.973 s.v. روزی) identifies Pahl. rōčīk with 'رزق یومیه', i.e. he recognises the same round trip. \"\n  \"The Persian doublet pair روزی (inherited) / رزق (Arabic-mediated) is therefore a classic معرّب doublet.\"\n ),\n \"derivation_fa\": (\n  \"این جعبه گردشِ رفت‌وبرگشتِ واژه را نشان می‌دهد: فارسی میانه rōzīg > عربی «رزق» > فارسی نو «رزق». \"\n  \"واژه اکنون در فارسی معرّب شمرده می‌شود و همراه صرفِ عربی خود به کار می‌رود: جمعِ مکسّرِ «ارزاق» و صفت‌های فاعلیِ «رزّاق» و «رازق» \"\n  \"(همان صورت‌هایی که در جعبه چاپ شده). معین در فرهنگ فارسی «رزق» را با نشانِ [ع.] می‌آورد و خود در حاشیهٔ برهان (ص ۹۷۳ ذیل «روزی») \"\n  \"پهلوی rōčīk را همان «رزق یومیه» می‌داند. پس «روزی» و «رزق» در فارسی دوگانه (doublet) اند: یکی میراثی و دیگری معرّب. ادعای نورایی درست است.\"\n ),\n \"sources\": [S_RIZQ],\n \"ref_check\": [\n  {\"ref\": \"MON\", \"status\": \"not_checked\", \"note\": \"no page is given in the book, and the six-volume Farhang-e Farsi is not online; the entry text served by vajehyab/abadis tags رزق as [ع.], consistent with the arrow\"}\n ],\n \"consulted\": [\n  {\"src\": \"PLA\", \"where\": \"Asbaghi p.135\", \"stance\": \"supports\", \"note\": \"lists ʾarzāq, rāziq, razzāq under rizq, i.e. the Arabic derivational family that Persian took back\"},\n  {\"src\": \"BQT\", \"where\": \"Borhan p.973, Mo'in's footnote on روزی\", \"stance\": \"supports\", \"note\": \"'پهلوی rōčīk = ارمنی ročik (رزق یومیه)'\"},\n  {\"src\": \"AFM\", \"where\": \"Addi Shir p.72\", \"stance\": \"supports\", \"note\": \"'وقالت فيه العرب رزق وارتزق الى غير ذلك' — the Arabic derivational family that returned to Persian\"}\n ]\n})\n\nnodes.append({\n \"id\": 5,\n \"lang\": \"Sogdian\",\n \"words\": \"dwk`; rwxšn\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n  \"rwxšn is right and inherited: Gharib, Sogdian Dictionary no. 8604 (printed p.345) \\\"rwxšn- M, C roxšn ... luminous, light\\\", \"\n  \"i.e. Sogdian rōxšn < Old Iranian *rauxšna- exactly as Av. raoxšna-/NP rōšan (the same stem also in rwxšn-yrδmn 'paradise' < Av. raoxšna-garō.dəmāna-). \"\n  \"dwk` is a different matter: Gharib no. 3689 (printed p.146) is \\\"δwk' B — δoka, loka ©Skt. loka ©'world'\\\", cross-referred to rwk (no. 8576, p.130) \"\n  \"\\\"r/lok ©< Skt. loka 'loka, world'\\\" — a Buddhist Sogdian loanword from Sanskrit loka-, borrowed with the Buddhist canon and with the \"\n  \"δ-/r- substitution Sogdian scribes used for Indic l. Sanskrit loka- 'free (bright) space, world' does belong to *leuk- \"\n  \"(Pokorny 688 \\\"loka- m. 'free (bright) room, world'\\\"), so the word is ultimately from the root, but not as an Iranian inheritance: \"\n  \"Nourai's arrow root -> Sogdian conceals the detour through Indo-Aryan. Hence plausible rather than confirmed.\"\n ),\n \"derivation_fa\": (\n  \"صورت rwxšn درست و میراثی است: قریب در فرهنگ سغدی، شمارهٔ ۸۶۰۴ (ص ۳۴۵) آن را «روشن، درخشان» می‌آورد؛ سغدی rōxšn از ایرانی باستان \"\n  \"*rauxšna- است، همان که اوستایی raoxšna- و فارسیِ «روشن» از آن آمده‌اند. اما «dwk‘» چیز دیگری است: قریب شمارهٔ ۳۶۸۹ (ص ۱۴۶) آن را \"\n  \"δwk' = δoka/loka و وام‌واژه‌ای از سانسکریت loka «جهان» می‌داند (با ارجاع به rwk در ص ۱۳۰). سانسکریت loka- خود از ریشهٔ *leuk- است \"\n  \"(پوکورنی ص ۶۸۸)، پس واژه در نهایت به همین ریشه می‌رسد، ولی نه به‌عنوان میراث ایرانی بلکه از راه وام‌گیری از هندی باستان در متون بودایی سغدی. \"\n  \"بنابراین پیکانِ نورایی (ریشه ← سغدی) این میانجی را پنهان می‌کند و ادعا با احتیاط پذیرفتنی است.\"\n ),\n \"sources\": [S_PIE],\n \"ref_check\": [\n  {\"ref\": \"SOD:146\", \"status\": \"supports\", \"note\": \"Gharib no. 3689 stands on printed p.146 (SOD_pages.txt leaf 211, the numeral 146 printed right after the entry): \\\"δwk' ... δoka, loka ©Skt. loka ... world\\\" — the page number is exactly right, but the entry itself labels the word a Sanskrit loan\"},\n  {\"ref\": \"SOD:345\", \"status\": \"supports\", \"note\": \"Gharib no. 8604 rwxšn- 'luminous, light' is on SOD_pages.txt leaf 413 = printed ~345-347 (offset leaf-66), matching Nourai's second number\"}\n ],\n \"consulted\": [\n  {\"src\": \"SOD\", \"where\": \"nos. 3689, 8576, 8604, 8609\", \"stance\": \"partial\", \"note\": \"confirms rwxšn as native and δwk'/rwk as Sanskrit loka loanwords\"},\n  {\"src\": \"POK\", \"where\": \"p.688\", \"stance\": \"supports\", \"note\": \"\\\"Old Indic loka- m. 'free (bright) room, world' (= Latin lucus, Lithuanian laukas 'field', OHG loh)\\\" — so Skt. loka- is under leuk̂-\"},\n  {\"src\": \"HENNING\", \"where\": \"grep of HENNING_selected_papers.txt\", \"stance\": \"silent\", \"note\": \"no discussion of Sogdian δwk' found\"}\n ]\n})\n\nnodes.append({\n \"id\": 6,\n \"lang\": \"Old Persian\",\n \"words\": \"raucah\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Kent's lexicon, s.v.: \\\"raucah- sb. 'day': Av. raocah- 'light', Phl. rūč, NPers. rōz, Skt. rócas- 'light', pIE *leugos\\\" — \"\n  \"so the stem, the gloss and the parentage are all exactly Nourai's. Attested forms: nom.-acc. sg. rauca (DB 3.8), \"\n  \"the frozen phrase xšapa-vā rauca-patiy-vā 'either by night or by day' (DB 1.20) and the very common instr. pl. raucabiš \"\n  \"in Darius' date formulas ('N days of month X had passed'). Kent §156 explains the shape: \\\"OP rauca from nom.-acc. pIE *leugos, \"\n  \"with c from the oblique cases, where pIE had *leuges-\\\" (i.e. the palatal came in from forms with a front vowel). \"\n  \"Semantically the -os- neuter 'light (of the sky)' narrowed in Old Persian to 'day', which is the meaning that lives on in NP روز.\"\n ),\n \"derivation_fa\": (\n  \"کنت در واژه‌نامهٔ «پارسی باستان» می‌نویسد: «raucah- اسم، «روز»: اوستایی raocah- «روشنایی»، پهلوی rūč، فارسی نو rōz، سنسکریت rócas-، \"\n  \"هندواروپایی آغازین *leugos». صورت‌های گواه‌شده: raucah در حالت فاعلی-مفعولی rauca (کتیبهٔ بیستون ۳٫۸)، ترکیبِ xšapa-vā rauca-patiy-vā \"\n  \"«چه شب چه روز» (بیستون ۱٫۲۰) و بسیار پُربسامد raucabiš در تاریخ‌گذاری‌های داریوش. کنت (بند ۱۵۶) پیدایش č را از حالت‌های مایل \"\n  \"(*leuges-) می‌داند که در آنجا واکهٔ پیشین بوده است. از نظر معنایی، ستاکِ خنثای «روشنایی آسمان» در پارسی باستان به «روز» محدود شده و \"\n  \"همین معنا در فارسیِ «روز» مانده است. ادعای نورایی درست است.\"\n ),\n \"sources\": [S_RUZ],\n \"ref_check\": [\n  {\"ref\": \"KNT:205\", \"status\": \"supports\", \"note\": \"Kent's Lexicon (pp.164-215; the r- entries fall around p.205) s.v. raucah-, found in KNT.txt leaf 229: \\\"raucah- sb. 'day': Av. raocah- 'light', Phl. rūč, NPers. rōz, Skt. rócas- 'light', pIE *leugos ... rauca nsn. DB 3.8 ... raucabiš ipn.\\\" The OCR leaf/page offset is unreliable in the lexicon, but the entry is unmistakable.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KNT\", \"where\": \"Lexicon s.v. raucah-; §§107, 156.II\", \"stance\": \"supports\", \"note\": \"as quoted; also §156 'pIE *leugos, OP rauca, Skt. rócas'\"},\n  {\"src\": \"BRT\", \"where\": \"AiW 1489-90 s.v. raocah- (\\\"g. raocah-, p. raucah- n.\\\")\", \"stance\": \"supports\", \"note\": \"Bartholomae treats the Old Persian form in the same entry, sense 4 'Tag': \\\"xšapa-vā rauca-patiy-vā 'seis in der Nacht oder am Tag' Bh.1.7[=20]\\\"\"},\n  {\"src\": \"IEC\", \"where\": \"Mann, s.v. leukos\", \"stance\": \"supports\", \"note\": \"\\\"Skt. rókaḥ ...; Av. raocō n. 'glitter'; OPers. rauca- 'day'\\\" under leukos (WP II 408)\"},\n  {\"src\": \"SYN\", \"where\": \"Buck 14.41 DAY, p.991\", \"stance\": \"supports\", \"note\": \"the 'day' table lists OPers. rauca beside Av. ayan-, azan-\"}\n ]\n})\n\nnodes.append({\n \"id\": 7,\n \"lang\": \"Latin\",\n \"words\": \"lŭstrâre\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Latin lūstrāre 'to light up, illuminate, make bright', also 'to purify (by a lustration)', is the denominative of lūstrum \"\n  \"< *leuk-s-tro- 'illumination' (the -s- of the old -es-/-os- stem plus the instrumental suffix -tro-). \"\n  \"Pokorny 688: \\\"lustrum 'period of five years, a purificatory sacrifice' (*leuk-s-trom 'enlightenment'), lūstrō, -āre \"\n  \"'to light up, illuminate, make bright', also 'clean', illustrāre 'brighten, light up'\\\". Watkins/AHD: \\\"Suffixed form *leuk-stro- in: \"\n  \"a. Latin lustrum, purification: LUSTER, LUSTRUM; b. Latin lustrare, to purify, illuminate: ILLUSTRATE\\\". \"\n  \"Klein s.v. lustrum adds the semantic chain and the identification of the two verbs: \\\"for *leuqs-trom, prop. 'illumination' ... \"\n  \"the various phases ... 'illumination, inspection, review, mustering, expiatory offering, expiation'. Accordingly the verbs lustrare, \"\n  \"'to light, illuminate', and lustrare, 'to purify from guilt', are identical\\\". Nourai's double gloss 'to make bright, purify' is therefore exact. \"\n  \"(A homonym lūstrum 'bog, wild beast's lair' is a separate word, which Ernout-Meillet derive from luō 'to soil'; E-M refer the \"\n  \"'purification' lūstrum itself to the luc-/lūc- article, i.e. to this root.)\"\n ),\n \"derivation_fa\": (\n  \"لاتینِ lūstrāre «روشن کردن، تابانیدن» و نیز «پاک کردن (با آیین تطهیر)» فعلِ برگرفته از lūstrum است و آن از *leuk-s-tro- \"\n  \"«روشن‌سازی» (همان -s- ستاکِ کهن به‌همراه پسوند ابزارسازِ -tro-). پوکورنی ص ۶۸۸: «lustrum ... (*leuk-s-trom «روشن‌سازی»)، lūstrō, -āre \"\n  \"«روشن کردن، تابانیدن» و همچنین «پاک کردن»، illustrāre «روشن کردن»». واتکینز (فرهنگ American Heritage) نیز همین را ذیل *leuk-stro- می‌آورد. \"\n  \"کلاین می‌افزاید که دو فعلِ lustrāre («تابانیدن» و «تطهیر کردن») یکی‌اند و سیرِ معنایی آن چنین بوده: روشن‌سازی ← بازدید و سرشماری ← \"\n  \"قربانیِ تطهیر ← تطهیر. پس معنیِ دوگانه‌ای که نورایی داده («to make bright, purify») دقیق است. \"\n  \"(واژهٔ همنامِ lūstrum «لانهٔ جانور، باتلاق» جداست و ارنو–مِیه آن را از luō «آلودن» می‌گیرند.)\"\n ),\n \"sources\": [S_LUSTER, S_PIE],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 (AHD_watkins1985.txt) s.v. leuk-: \\\"5. Suffixed form *leuk-stro- in: a. Latin lustrum, purification: LUSTER, (LUSTRUM); b. Latin lustrare, to purify, illuminate: ILLUSTRATE. [Pok. leuk- 687.]\\\" — no page is cited in the book for this box, and the appendix entry is the standard for the claim\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"p.688\", \"stance\": \"supports\", \"note\": \"\\\"lustrum ... (*lehuk-s-trom 'enlightenment'), lūstro, -are 'to light up, illuminate, make bright', also 'clean', illustrare\\\"\"},\n  {\"src\": \"KLN\", \"where\": \"s.vv. lustrum, luster ('gloss, radiance'), light (n.)\", \"stance\": \"supports\", \"note\": \"\\\"lustrum ... for *leuqs-trom, *louqs-trom, prop. 'illumination', fr. I.-E. base *leuq-\\\"\"},\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.vv. lustrum\", \"stance\": \"partial\", \"note\": \"\\\"lustrum, -i n.: bauge ... De là: lustror\\\" is kept apart (from *luo 'souiller'), while \\\"lustrum: v. plus loin sous luc-/lūc-\\\" refers the purification word to this root\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. II 409 s.v. leuq-\", \"stance\": \"supports\", \"note\": \"\\\"auf diesem -es-St. beruhen auch lat. lūstrāre, lucubrāre, ags. lioxan, aisl. ljós\\\"\"}\n ]\n})\n\nnodes.append({\n \"id\": 8,\n \"lang\": \"French\",\n \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"The empty pivot box is French lustre 'gloss, radiance' (attested 14th c.), which is not a direct continuation of Latin lūstrāre \"\n  \"but a Renaissance-era borrowing from Italian lustro 'splendour, brilliancy' (from Italian lustrare < Latin lūstrāre); \"\n  \"the noun is pan-Romance (Spanish/Portuguese lustre, Romanian lustru). Etymonline s.v. luster: \\\"from French lustre 'gloss, radiance' (14c.), \"\n  \"common Romanic ... a noun ultimately from Latin lustrare 'spread light over, brighten, illumine'\\\"; Klein: \\\"MF. (= F.) lustre, fr. It. lustro, \"\n  \"fr. lustrare\\\". In French the word then took on the concrete sense 'hanging light fixture, chandelier' (17th c.), which is the sense \"\n  \"that both Persian لوستر and, partly, English luster inherit.\"\n ),\n \"derivation_fa\": (\n  \"این جعبهٔ خالی همان lustre فرانسوی است، به معنی «درخشش، جلا» (گواه‌شده از سدهٔ ۱۴م). این واژه ادامهٔ مستقیم lūstrāre لاتین نیست، \"\n  \"بلکه وام‌گیری از ایتالیایی lustro «درخشش» است (خودِ آن از lustrare ایتالیایی و لاتین)؛ همین اسم در همهٔ زبان‌های رومی هست \"\n  \"(اسپانیایی و پرتغالی lustre، رومانیایی lustru). سپس در فرانسوی سدهٔ ۱۷م معنای عینیِ «چراغِ آویز، چلچراغ» گرفت و همین معنا است که \"\n  \"به «لوستر» فارسی رسیده است. جعبه درست است.\"\n ),\n \"sources\": [S_LUSTER],\n \"ref_check\": [\n  {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"the box carries no citation in the book\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"s.v. luster, lustre 'gloss, radiance'\", \"stance\": \"supports\", \"note\": \"\\\"MF. (= F.) lustre, fr. It. lustro, fr. lustrare, 'to light, illuminate', fr. L. lustrare\\\"\"},\n  {\"src\": \"DEV\", \"where\": \"grep of DEV.txt (Devic, mots français d'origine orientale)\", \"stance\": \"silent\", \"note\": \"lustre is not an orientalism, so Devic has no entry — consistent with a Romance-internal history\"}\n ]\n})\n\nnodes.append({\n \"id\": 9,\n \"lang\": \"Persian\",\n \"words\": \"lŭstr «لوستر»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Persian لوستر lūster/lūstr 'chandelier' is a modern (late Qajar / early Pahlavi) borrowing from French lustre, \"\n  \"part of the large layer of French technical and household vocabulary that entered Persian through the Dar al-Fonun and \"\n  \"Franco-Persian trade; French [lystʁ] was rendered with و for the front rounded vowel, as in ژورنال, دوش, مانتو. \"\n  \"Mo'in's Farhang tags the entry [فر.] ('French') and defines it as 'حباب شیشه‌ای، چینی یا فلزی چراغ، مخصوصاً نوعی که از سقف آویزان می‌شود'; \"\n  \"Wiktionary s.v. لوستر: 'From French lustre'. The semantic step 'radiance' -> 'chandelier' had already happened inside French, \"\n  \"so Persian took over the concrete sense only. Ultimately, therefore, a very late descendant of the same root as روز and روشن in the box above.\"\n ),\n \"derivation_fa\": (\n  \"«لوستر» وام‌واژه‌ای نو (اواخر قاجار/اوایل پهلوی) از فرانسوی lustre است و از همان لایهٔ گستردهٔ واژه‌های فنی و خانگیِ فرانسوی است که \"\n  \"از راه دارالفنون و بازرگانی به فارسی آمد؛ واکهٔ گِردِ پیشینِ فرانسوی با «و» نوشته شده، مانند ژورنال و دوش و مانتو. \"\n  \"معین در فرهنگ فارسی این واژه را با نشانِ [فر.] می‌آورد و آن را «حباب شیشه‌ای، چینی یا فلزی چراغ، مخصوصاً نوعی که از سقف آویزان می‌شود» \"\n  \"معنی می‌کند؛ ویکی‌واژه هم آن را از فرانسوی lustre می‌داند. تحولِ معنایی «درخشش ← چلچراغ» پیش‌تر در خودِ فرانسوی رخ داده بود. \"\n  \"نکتهٔ درخورِ توجه اینکه «لوستر» و «روز» و «روشن» هر سه در نهایت از یک ریشهٔ هندواروپایی‌اند. ادعای نورایی درست است.\"\n ),\n \"sources\": [S_LUSTRFA, S_ABADIS],\n \"ref_check\": [\n  {\"ref\": \"MON:3650\", \"status\": \"partial\", \"note\": \"the six-volume Farhang-e Farsi is not online and the page cannot be verified; the entry text served by abadis.ir/vajehyab from Mo'in does carry the tag [فر.] and the 'hanging lamp' definition, exactly as the arrow requires\"}\n ],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. لوستر (via abadis.ir)\", \"stance\": \"supports\", \"note\": \"'[فر.] ۱- حباب شیشه‌ای، چینی یا فلزی چراغ مخصوصاً نوعی که از سقف آویزان می‌شود'\"},\n  {\"src\": \"ARY\", \"where\": \"grep of ARY_pages.txt for لوستر\", \"stance\": \"silent\", \"note\": \"Aryanpur's IE-roots dictionary has no entry (it covers inherited Persian words, not modern French loans)\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. luster\", \"stance\": \"supports\", \"note\": \"confirms the French noun lustre that Persian borrowed\"}\n ]\n})\n\nnodes.append({\n \"id\": 10,\n \"lang\": \"English\",\n \"words\": \"luster, illustrate\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n  \"Half of the box travels through French, half does not. luster/lustre 'gloss, radiance' entered English in the 1520s \"\n  \"from French lustre (Etymonline: \\\"from French lustre 'gloss, radiance' (14c.) ... ultimately from Latin lustrare ... \"\n  \"from PIE *leuk-stro-, suffixed form of root *leuk- 'light, brightness'\\\"), so for this word Nourai's Latin > French > English chain is right \"\n  \"(Klein: \\\"MF. (=F.) lustre, fr. It. lustro\\\"). illustrate, however, is a direct learned borrowing from Latin, not a French transmission: \"\n  \"Etymonline dates it to the 1520s 'light up, shed light on' from Latin illustrare 'light up, make light, illuminate', \"\n  \"an assimilated in- + lustrare, with the modern sense 'provide pictures' only from the 1630s; Klein s.v. illustrate: \"\n  \"\\\"L. illustratus, pp. of illustrare ... fr. in-, 'in', and lustrare, 'to illuminate'\\\". Placing illustrate under the French box \"\n  \"is therefore imprecise (French illustrer exists but is not the source of the English verb), which is why this node is plausible, not confirmed.\"\n ),\n \"derivation_fa\": (\n  \"نیمی از این جعبه از راه فرانسوی آمده و نیمی نه. واژهٔ luster «جلا، درخشش» در دههٔ ۱۵۲۰م از فرانسوی lustre به انگلیسی رسیده \"\n  \"(اتیمانلاین: از فرانسوی lustre سدهٔ ۱۴م، و آن در نهایت از lustrāre لاتین و ریشهٔ *leuk-stro-)، پس برای این واژه زنجیرهٔ نورایی \"\n  \"(لاتین ← فرانسوی ← انگلیسی) درست است. اما illustrate وام‌گیریِ مستقیمِ عالمانه از لاتین است، نه از فرانسوی: در دههٔ ۱۵۲۰م به معنی \"\n  \"«روشن کردن» از illustrāre لاتین (in- + lustrāre) گرفته شده و معنای «مصوّر کردن» آن از دههٔ ۱۶۳۰م است (کلاین نیز همین را می‌گوید). \"\n  \"پس نهادنِ illustrate زیرِ جعبهٔ فرانسوی دقیق نیست و ادعا با احتیاط پذیرفتنی است.\"\n ),\n \"sources\": [S_LUSTER, S_ILL],\n \"ref_check\": [\n  {\"ref\": \"AHD:776\", \"status\": \"partial\", \"note\": \"AHD:776 is a page of the New College Edition main dictionary (the l- range, i.e. the entries luster/lustrum), which is not in the local text; the local Watkins appendix does list both LUSTER and ILLUSTRATE under leuk-, so the substance of the citation checks out even though the page itself could not be read\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"s.vv. luster ('gloss, radiance'), illustrate, illustrious\", \"stance\": \"partial\", \"note\": \"\\\"illustrate ... L. illustratus, pp. of illustrare ... fr. in- and lustrare\\\" — a direct Latin borrowing, not via French\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. leuk-, and the index (\\\"ILLUSTRATE leuk-\\\", \\\"LUSTER leuk-\\\")\", \"stance\": \"supports\", \"note\": \"both English words are referred to *leuk-stro-\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat, s.v. lustre\", \"stance\": \"supports\", \"note\": \"Skeat likewise takes lustre from French/Italian, from Latin lustrare\"}\n ]\n})\n\nnodes.append({\n \"id\": 11,\n \"lang\": \"Latin\",\n \"words\": \"lumen, lŭx : light; luna : moon\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"All three are textbook reflexes of the root. lūx, lūcis 'light' is the old root noun/-s- stem (*louk-s > lūx, with the \"\n  \"regular Latin monophthongisation of *ou > ū), beside lūcēre 'to shine' (*louk-eyo-). lūmen 'light, opening' is *leuk-s-men- \"\n  \"with the -s- of the -es- stem and dissimilatory loss before -men (Pokorny 688: \\\"Latin lūmen 'light' from *leuk-s-men\\\"; \"\n  \"Klein: \\\"lumen (for *leuqs-men or *louqs-men)\\\"). lūna 'moon' is *leuk-s-nā 'the shining one', proved by Praenestine Losna \"\n  \"and by the exact cognates Avestan raoxšna-, Old Prussian lauxnos, Old Church Slavonic luna, Middle Irish luan \"\n  \"(Pokorny 688; Walde-Pokorny II 409). Watkins/AHD numbers them 2, 3 and 4 under leuk-. Nourai's glosses are right; \"\n  \"he simply prints the nominative lūx beside the -men- and -nā- derivatives.\"\n ),\n \"derivation_fa\": (\n  \"هر سه صورت نمونه‌های کلاسیکِ همین ریشه‌اند: lūx «روشنایی» همان ستاکِ کهنِ *louk-s است (با تک‌واکه‌شدنِ منظمِ *ou > ū در لاتین) \"\n  \"در کنارِ lūcēre «درخشیدن»؛ lūmen «روشنایی، روزنه» از *leuk-s-men- است (پوکورنی ص ۶۸۸: «lūmen لاتین از *leuk-s-men»؛ کلاین همین را می‌گوید)؛ \"\n  \"و lūna «ماه» از *leuk-s-nā «درخشنده» است، که گواهِ آن صورتِ پرنستیِ Losna و هم‌ریشه‌های دقیقِ آن است: اوستایی raoxšna-، \"\n  \"پروسیِ باستان lauxnos، اسلاویِ کهن luna و ایرلندی میانه luan (پوکورنی ص ۶۸۸؛ والده–پوکورنی ج ۲ ص ۴۰۹). \"\n  \"واتکینز نیز همین سه را بندهای ۲ تا ۴ ذیل *leuk- آورده است. ادعای نورایی درست است.\"\n ),\n \"sources\": [S_PIE],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. leuk-: \\\"2. Latin lux, light: LUCINA, LUCULENT, LUX ... 3. Suffixed form *leuk-smen- in Latin lumen, light, opening: LIMN, LUMEN, LUMINARY, LUMINOUS; ILLUMINATE ... 4. Suffixed form *leuk-snā- in Latin luna, moon: LUNA, LUNAR ...\\\"\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"p.687-688\", \"stance\": \"supports\", \"note\": \"\\\"Latin lux, -cis 'light, brightness' (older i-stem) lūceō ... Latin lūmen 'light' from *leuk-s-men; lūna 'moon goddess' (*leuksna), praen. Losna (: Old Prussian lauxnos, Avestan raoxšna ...)\\\"\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. II 409 s.v. leuq-\", \"stance\": \"supports\", \"note\": \"\\\"av. raoxšna- 'glänzend' ... f. 'Licht' (= lat. luna, mir. luan, apr. lauxnos, abg. luna, schwundstufig gr. lychnos)\\\"\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. light (n.)\", \"stance\": \"supports\", \"note\": \"\\\"lumen (for *leuqs-men or *louqs-men), 'light', lūna (for *louqs-na), 'moon'\\\"\"},\n  {\"src\": \"IEC\", \"where\": \"Mann s.vv. leuk-, leuks-, leuksnio-\", \"stance\": \"supports\", \"note\": \"Mann sets up leuks-/leuksnio- for exactly this group (WP II 408-411)\"}\n ]\n})\n\nnodes.append({\n \"id\": 12,\n \"lang\": \"English\",\n \"words\": \"illuminate, lunar\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Both are Latinate borrowings of the node above. illuminate comes from Latin illūminātus, pp. of illūmināre \"\n  \"'to light up' (in- + lūmināre, from lūmen), entering English in the 15th-16th c. (the noun illumination is older, via Old French); \"\n  \"lunar is Latin lūnāris 'of the moon' (from lūna), first in English in the 17th c. Watkins/AHD indexes both under the root: \"\n  \"\\\"ILLUMINATE leuk-\\\" and \\\"LUNAR leuk-\\\", with the appendix entry listing LUMEN, LUMINARY, LUMINOUS, ILLUMINATE under *leuk-smen- \"\n  \"and LUNA, LUNAR, LUNATE, LUNATIC, LUNE, LUNULA, DEMILUNE, SUBLUNARY under *leuk-snā-. The arrow is uncontroversial.\"\n ),\n \"derivation_fa\": (\n  \"هر دو واژه وام‌گیریِ لاتینی‌تبار از جعبهٔ بالا هستند: illuminate از illūminātus لاتین، اسم مفعولِ illūmināre «روشن کردن» \"\n  \"(پیشوند in- + lūmināre از lūmen)، که در سده‌های ۱۵ و ۱۶م به انگلیسی راه یافت؛ و lunar از lūnāris لاتین «مربوط به ماه» (از lūna) \"\n  \"که در سدهٔ ۱۷م به انگلیسی آمد. واتکینز هر دو را در فهرست خود ذیل همین ریشه می‌آورد (ILLUMINATE leuk- و LUNAR leuk-). \"\n  \"این حلقه اختلافی ندارد و ادعای نورایی درست است.\"\n ),\n \"sources\": [S_PIE],\n \"ref_check\": [\n  {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"the box carries no citation in the book; the parent box's AHD reference covers it\"}\n ],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. leuk- and index entries ILLUMINATE / LUNAR\", \"stance\": \"supports\", \"note\": \"\\\"ILLUMINATE leuk-\\\" and \\\"LUNAR leuk-\\\" in the index; the appendix entry lists both derivational families\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. light (n.), cross-references 'luminous, lunar, lunation'\", \"stance\": \"supports\", \"note\": \"Klein's cross-reference list under the base *leuq- includes luminous, lunar, lunation\"}\n ]\n})\n\nnodes.append({\n \"id\": 13,\n \"lang\": \"Germanic\",\n \"words\": \"liuhtam\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"liuhtam\",\n \"correct_form\": \"*leuhtam\",\n \"derivation\": (\n  \"The branch itself is correct: Proto-Germanic *leuhtam n. 'light' < *leuk-to-, whence Old English lēoht/līht, Old Saxon/Old High German lioht, \"\n  \"Gothic liuhaþ 'light' (Pokorny 689: \\\"Gothic liuhaþ 'light' (: Latin Lucetius, Gaul. Leucetius), Old High German, Old Saxon lioht 'bright' and n. 'light', \"\n  \"Old English leoht\\\"; Klein s.v. light: \\\"ME. liht, fr. OE. leoht, rel. to OS. lioht ... Goth. liuhaþ, 'light' ... fr. I.-E. base *leuq-\\\"). \"\n  \"But the form printed in the box, 'liuhtam', is not the reconstruction the sources use: Watkins/AHD has \\\"Suffixed form *leuk-to- in Germanic *leuhtam \"\n  \"in Old English lēoht, liht, light\\\". The i-vocalism belongs to the attested Gothic liuhaþ / OHG lioht, not to Proto-Germanic, where the root vowel is *eu. \"\n  \"I checked the printed page (pdf p.312, copied to data/verification/sources/refs/ocr/BOOK/312.png): the book itself prints 'liuhtam', \"\n  \"so the extraction is faithful and the mis-vocalisation is Nourai's (a slip for AHD's *leuhtam).\"\n ),\n \"derivation_fa\": (\n  \"خودِ این شاخه درست است: ژرمنی آغازین *leuhtam «روشنایی» از *leuk-to-، که انگلیسی کهن lēoht/līht و ساکسونی/آلمانی علیای کهن lioht و \"\n  \"گوتیک liuhaþ از آن آمده‌اند (پوکورنی ص ۶۸۹؛ کلاین ذیل light). اما صورتی که در جعبه چاپ شده، یعنی «liuhtam»، صورتِ بازسازیِ منابع نیست: \"\n  \"واتکینز *leuhtam را می‌آورد. واکهٔ i در liuhaþ گوتیک و lioht آلمانی علیای کهن است، نه در ژرمنیِ آغازین که واکهٔ ریشه در آن *eu است. \"\n  \"تصویر صفحهٔ چاپی (صفحهٔ ۳۱۲ پی‌دی‌اف، رونوشت در پوشهٔ ocr/BOOK) نشان می‌دهد که همین «liuhtam» در کتاب چاپ شده است؛ \"\n  \"پس خطای خوانشِ اسکن نیست، خطای چاپی/سهوِ خودِ نورایی است.\"\n ),\n \"sources\": [S_PIE],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. leuk-: \\\"1. Suffixed form *leuk-to- in Germanic *leuhtam in Old English leoht, liht, light: LIGHT(1)\\\" — the derivation is Nourai's source, but the source spells the Proto-Germanic form *leuhtam, not liuhtam\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"p.689\", \"stance\": \"partial\", \"note\": \"\\\"Gothic liuhaþ 'light' ..., Old High German, Old Saxon lioht 'bright' and n. 'light', Old English leoht\\\" — the attested forms, no *liuhtam\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. light (n.)\", \"stance\": \"partial\", \"note\": \"same attested forms; base given as *leuq-\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. II 409-411\", \"stance\": \"partial\", \"note\": \"the Germanic material is cited as got. liuhaþ, ahd. lioht etc., again without a *liuhtam\"}\n ]\n})\n\nnodes.append({\n \"id\": 14,\n \"lang\": \"English\",\n \"words\": \"light 1, lightning, lighting\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"English light (noun/adjective 'brightness, bright') is the inherited word: OE lēoht, līht < PGmc *leuhtam < *leuk-to-; \"\n  \"ME liht/light, with the loss of the velar fricative in spelling only. lightning is the ME verbal noun of lightnen 'to flash, \"\n  \"make bright' (14th c., beside older lightening), and lighting is the ordinary -ing noun of the verb light 'to illuminate' \"\n  \"(OE līhtan). Nourai's 'light 1' is the correct disambiguation: light 2 'not heavy' is a different root, PIE *legʷh- \"\n  \"(AHD index \\\"LIGHT1 = leuk-\\\", \\\"LIGHT2 legwh-\\\"), and light 3 'to alight, descend' belongs with it (Skeat: 'light (3), \"\n  \"to alight ... lit. to make light, relieve a horse of his burden').\"\n ),\n \"derivation_fa\": (\n  \"واژهٔ انگلیسیِ light «روشنایی/روشن» میراثی است: انگلیسی کهن lēoht/līht از ژرمنی آغازین *leuhtam و آن از *leuk-to-؛ \"\n  \"در انگلیسی میانه liht/light، و سایشیِ کامی تنها در املا باقی مانده است. lightning اسمِ مصدرِ فعلِ انگلیسی میانه lightnen «برق زدن، روشن کردن» \"\n  \"(سدهٔ ۱۴م) است و lighting اسمِ -ing از فعل light «روشن کردن» (انگلیسی کهن līhtan). عددِ «۱» که نورایی گذاشته درست است: \"\n  \"light ۲ به معنی «سبک» از ریشهٔ دیگری است (*legʷh- هندواروپایی؛ فهرست واتکینز: LIGHT2 legwh-) و light ۳ «فرود آمدن» نیز به همان می‌پیوندد \"\n  \"(اسکیت). ادعای نورایی درست است.\"\n ),\n \"sources\": [S_PIE],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. leuk-: \\\"... in Old English leoht, liht, light: LIGHT(1)\\\"; the index confirms the split \\\"LIGHT1 = leuk-\\\" vs \\\"LIGHT2 legwh-\\\"\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"s.v. light, n., 'brightness'\", \"stance\": \"supports\", \"note\": \"\\\"ME. liht, light, fr. OE. leoht, rel. to OS. lioht, OFris. liacht ... Goth. liuhaþ, 'light' ... fr. I.-E. base *leuq-, 'to emit light, to shine; bright'\\\"\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat, s.vv. light (1), lighten (1), light (3)\", \"stance\": \"supports\", \"note\": \"\\\"lighten (1), to illuminate, flash ... M.E. lightnen\\\"; light (3) 'to alight' kept apart from light 'brightness'\"},\n  {\"src\": \"AHD\", \"where\": \"index p.1748\", \"stance\": \"supports\", \"note\": \"\\\"LIGHT1 = leuk- LIGHT2 legwh-\\\"\"}\n ]\n})\n\nentry2 = {\n \"entry\": 2,\n \"root\": \"Leuk, Leuqos\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *leuk- (Pokorny leuk̂-) 'light, brightness; to shine, to see', with the thematic *leuk-o-s (Gk. leukós) that Nourai calls 'Leuqos'\",\n \"note\": (\n  \"Root, language label, gloss and page reference are all right. Pokorny, IEW 687-690, lemma leuk̂- (leuk-), Meaning 'bright, to shine; to see' \"\n  \"(References: WP. II 408 ff.), listing exactly the material of this chart: Av. raocah-, OP raucah-, Av. raoxšna-, Lat. lūx/lūmen/lūna/lūstrum/lūstrāre, \"\n  \"Goth. liuhaþ / OHG lioht / OE lēoht, Skt. loka-. Watkins/AHD: \\\"leuk-. Light, brightness. ... [Pok. leuk- 687.]\\\" — so POK:687 is the exact page. \"\n  \"Kent (KNT:205), Nourai's second reference, gives the same root in the older notation pIE *leugos s.v. raucah-. 'Leuqos' is Nourai's spelling of the \"\n  \"*leuk-o-s form (Gk. leukós 'white, bright', Skt. loka- 'open bright space, world', Lat. lūcus 'grove'); it is not a separate root. \"\n  \"Cross-cutting remarks: (1) the chart's strongest link, Persian rūz/rōšan/afrūxtan and the Arabic loan rizq, is fully confirmed; \"\n  \"(2) two Persian items in the Persian box (آرش, درفش ۱) and one Avestan item (a-raxša, plus the unattested raoč-xšaema) are not supported by modern sources; \"\n  \"(3) the Sogdian box mixes an inherited word (rwxšn) with a Sanskrit loanword (δwk' < Skt. loka); \"\n  \"(4) the Germanic box misprints the reconstruction (liuhtam for *leuhtam); \"\n  \"(5) on the printed page the Old Persian box has an arrow into an empty, unlabelled box that the JSON does not record.\"\n ),\n \"note_fa\": (\n  \"ریشه، برچسبِ زبان، معنی و شمارهٔ صفحه هر چهار درست است: پوکورنی در «فرهنگ ریشه‌شناسیِ هندواروپایی» صفحه‌های ۶۸۷ تا ۶۹۰ ریشهٔ leuk̂- را با معنای \"\n  \"«روشن، درخشیدن؛ دیدن» می‌آورد و همان داده‌های این نمودار را برمی‌شمارد: اوستایی raocah- و raoxšna-، پارسی باستان raucah-، \"\n  \"لاتین lūx و lūmen و lūna و lūstrum، گوتیک liuhaþ و انگلیسی کهن lēoht، و سنسکریت loka-. واتکینز نیز ذیل leuk- همین ارجاع «پوکورنی ۶۸۷» را دارد. \"\n  \"«Leuqos» صورتِ ستاک‌دارِ *leuk-o-s است (یونانی leukós، سنسکریت loka-، لاتین lūcus) و ریشهٔ جداگانه‌ای نیست. \"\n  \"به‌طور کلی: پیوندِ فارسی «روز، روشن، افروختن» و وام‌واژهٔ عربیِ «رزق» کاملاً تأیید می‌شود؛ اما «آرش» و «درفش ۱» در جعبهٔ فارسی و «a-raxša» و \"\n  \"«raoč-xšaema» در جعبهٔ اوستایی پشتوانهٔ امروزی ندارند؛ جعبهٔ سغدی یک واژهٔ میراثی (rwxšn) را با یک وام‌واژهٔ سانسکریت (δwk' از loka) درآمیخته؛ \"\n  \"و در جعبهٔ ژرمنی صورتِ بازسازی‌شده غلط چاپ شده است (liuhtam به‌جای *leuhtam).\"\n ),\n \"sources\": [S_PIE, S_RUZ],\n \"ref_check\": [\n  {\"ref\": \"POK:687\", \"status\": \"supports\", \"note\": \"POK_full.txt, block 'Root / lemma: lehuk- (*lehugh-)', Meaning 'bright, to shine; to see', Page(s): 687-690 — with \\\"rocas-, rocis-, Avestan raocah-, ap. raucah- n. 'light, radiance, esp. of heaven', Avestan raoxšna- 'gleaming'\\\", \\\"Latin lūmen 'light' from *leuk-s-men; lūna 'moon goddess' (*leuksna)\\\", \\\"lustrum ... lūstro, -are 'to light up, illuminate'\\\", \\\"Gothic liuhaþ 'light' ... Old English leoht\\\"\"},\n  {\"ref\": \"KNT:205\", \"status\": \"supports\", \"note\": \"Kent, Old Persian, Lexicon s.v. raucah- (KNT.txt leaf 229): \\\"raucah- sb. 'day': Av. raocah- 'light', Phl. rūč, NPers. rōz, Skt. rócas- 'light', pIE *leugos\\\"; cf. §156.II \\\"pIE *leugos, OP rauca, Skt. rócas\\\". Kent's *leug-/*leugos is the same root in pre-1959 notation.\"}\n ],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. leuk-\", \"stance\": \"supports\", \"note\": \"\\\"leuk-. Light, brightness. I. Basic form *leuk- ... [Pok. leuk- 687.]\\\" with the Germanic, Latin and Greek branches of this chart\"},\n  {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 408-411, s.v. leuq-\", \"stance\": \"supports\", \"note\": \"the same root under the older lemma leuq-: \\\"rocas-, rocis- n., av. raocah-, ap. raucah- n. 'Licht, Leuchte, bes. des Himmels', ai. rukṣá- 'glänzend', av. raoxšna- 'glänzend' ... (= lat. luna ...); auf diesem -es-St. beruhen auch lat. lūstrāre, lucubrāre\\\"\"},\n  {\"src\": \"IEC\", \"where\": \"Mann, s.vv. leuk-, leukos, leuks-\", \"stance\": \"supports\", \"note\": \"\\\"leukos (louk-) 'light, white; light, brightness'. Cf. louk-, luk-. WP II, 408: Skt. rókaḥ ...; Av. raocō n. 'glitter'; OPers. rauca- 'day'; Myc. & Gk. leukós\\\" — Mann's leukos is precisely Nourai's 'Leuqos'\"},\n  {\"src\": \"SYN\", \"where\": \"Buck 14.41 DAY (p.991) and 7.25 WINDOW (p.470)\", \"stance\": \"supports\", \"note\": \"'day' table gives OPers. rauca; the WINDOW article gives \\\"Av. raocana- (NPers. rōzan) : Skt. rocana- 'bright'\\\"\"},\n  {\"src\": \"KLN\", \"where\": \"Klein s.v. light (n.)\", \"stance\": \"supports\", \"note\": \"sets out the whole root under \\\"I.-E. base *leuq-, 'to emit light, to shine; bright'\\\", including Av. raocant-, raoxšna-, Lat. lux, lumen, luna, lustrum, lustrare\"}\n ],\n \"nodes\": nodes\n}\n\ndoc = {\n \"pdf_page\": 312,\n \"book_page\": 282,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [entry2]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-312.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPY\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk312.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-312.json > /dev/null && echo JSON_OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 312"
}
```


### [2026-09-07T02:00:09.956Z] TOOL RESULT

```
ok
JSON_OK
nodes verified: 14/14
node verdicts: {'disputed': 2, 'confirmed': 9, 'plausible': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 14, 'partial': 5, 'not_found': 2, 'not_checked': 3}
books consulted: {'partial': 9, 'supports': 34, 'silent': 6} | by book: {'KLN': 8, 'POK': 5, 'WLD': 3, 'AHD': 3, 'BRT': 2, 'HRN': 2, 'PHD': 2, 'ARY': 2, 'BQT': 2, 'SOD': 2, 'IEC': 2, 'SKT': 2, 'AVG': 1, 'NYB': 1, 'HUB': 1, 'FSF': 1, 'FVQ': 1, 'AFA': 1, 'PLA': 1, 'AFM': 1, 'HENNING': 1, 'KNT': 1, 'SYN': 1, 'LAT': 1, 'DEV': 1, 'MON': 1}
```


## [2026-09-07T02:00:18.347Z] TOOL CALL #88: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nd=json.load(open('data/verification/page-312.json'))\ne=d['entries'][0]\nassert e.get('note_fa')\nfor n in e['nodes']:\n    for k in ('derivation','derivation_fa','ref_check','consulted','verdict','words','lang'):\n        assert k in n and n[k] is not None, (n['id'],k)\n    assert len(n['consulted'])>=2, n['id']\nprint('all nodes ok:', len(e['nodes']))\nprint('files:', open('data/verification/page-312.json','rb').read(3))\nEOF\nhead -c 80 data/verification/page-312.json"
}
```


### [2026-09-07T02:00:19.864Z] TOOL RESULT

```
all nodes ok: 14
files: b'{\n '
{
  "pdf_page": 312,
  "book_page": 282,
  "verified_by": "claude-opus-5",
  "ve
```


## [2026-09-07T02:00:40.881Z] AGENT

Done. `data/verification/page-312.json` written; `verify_check.py 312` reports **0 PROBLEM lines** (14/14 nodes).

**Page 312 (book p. 282) — root Leuk, Leuqos [Indo-European] "light, brightness"**
Root: confirmed (POK 687-690 leuk̂-; AHD leuk-; Kent s.v. raucah- = pIE *leugos).
Node verdicts: 9 confirmed · 2 plausible · 2 disputed · 1 transcription_suspect.

- **disputed #1 [Avestan] a-raxša "bright" / raoč-xšaema** — Bartholomae has ərəxša- only as the archer's proper name (Yt.8.6), no gloss "bright"; no compound raoč-xšaema exists (Nourai's own split of raoxšna-, hence his ☞Ksei 2). raocah-, raoxšna-, aiwi.raocaya- are confirmed.
- **disputed #2 [Persian] رخش ( … درفش ۱ ) and آرش** — درفش is MP drafš < Av. drafša- and even its "shine" sense goes to PIr. *drafš- (Cheung 2007, Wiktionary), not *leuk-; آرش = Av. Ǝrəxša-, etymology uncertain (guess: "bear"). روز، روزنه، روشن، رخش، افروختن all confirmed (MacKenzie 72, Nyberg, Horn 94/610/629-631, Hübschmann, Aryanpur 312).
- **plausible #5 [Sogdian] dwk'** — Gharib 3689 (p.146) labels δwk' a Sanskrit loan (Skt. loka); rwxšn (no. 8604, p.345) is inherited. Root→Sogdian arrow hides the Indo-Aryan detour.
- **plausible #10 [English] luster, illustrate** — luster is via French lustre (1520s), but illustrate is a direct Latin borrowing (illūstrāre), not French-mediated.
- **transcription_suspect #13 [Germanic] liuhtam** — book prints "liuhtam" (page image checked, copied to `sources/refs/ocr/BOOK/312.png`); AHD/Pokorny reconstruct *leuhtam. error_in = book; extraction faithful.
- Highlight: Arabic **rezq** confirmed from MP rōzīg via Asbaghi p.135 (exact page), Addi Shir p.72 (exact page), Wiktionary, Mo'in's Borhan footnote p.973 — plus the Persian→Arabic→Persian round trip in #4.

**Reference-page problems in the book** (not extraction errors): BQT:97 not_found (p.97 = ارج/ارد range); BQT:976 off by ~2 (روز/روزی p.973, روشن p.978); FSF:176 not_found in this scan (درفشان/درفشیدن are pp.231-232); AHD:776 and MON:3650 unverifiable (pages not online). BQT:31, BQT:147, HRN:23/136/140, SYN:470/991, SOD:146/345, KNT:205, AFM:72, PLA:135 all check out.

**Extraction items for the owner:** (1) the printed page shows the Old Persian box arrowing into an **empty, unlabelled box** that the JSON omits; (2) the Ferdowsi quote in the JSON drops the trailing superscript "۲" of «درفش ۲».
