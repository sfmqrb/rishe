# Verification process log — verify-page-194


## [2026-09-06T02:14:35.158Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 194 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-194.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-194.json. Write /home/sfmqrb/git/rishe/data/verification/page-194.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 194` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T02:14:36.793Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T02:14:37.658Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T02:14:37.671Z] TOOL RESULT

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


## [2026-09-06T02:14:38.230Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-194.txt"
}
```


### [2026-09-06T02:14:38.283Z] TOOL RESULT

```
1	=== PDF page 194 (book page 164) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ghou-ro-s : terrifying  (refs POK:453)
4	#1 (parent #0) [Sanskrit] refs=POK:453 | Ğôrâh : terrifying
5	  #2 (parent #1) [Persian] refs=HRN:210 | gŭr «گور» : grave ; gŭrâb «گوراب ۱ (گورابه)» : the dome built over a grave
6	--- entry 1 ---
7	ROOT [Indo-European] Ghrebh : seize  (refs POK:455)
8	#1 (parent #0) [Avestan / Old Persian] refs=POK:455; SOD:237 | grab : to grab ; paiti-grab : accept ☞Per 3 ; gerew-âiti, gerewn-aîti : he seized ; gâuru-ayeiti, garb-âyaiti : he seized ; ni-gerepto : to be pressed down ☞Ni 1
9	  #2 (parent #1) [Persian] refs=BQT:374,1797,1802 | gereftan «گرفتن» : to grab, take ; pazîroftan «پذیرفتن (پذیر ، دلپذیر)» : accept ; gero «گرو (گروگان)» : collateral | NOTE: SNS:322 claims that Persian "gero: collateral" is derived from "garîveh: neck" meaning to accept responsibility. See root "Gwer 3".
10	#3 (parent #0) [Sogdian] refs=SOD:167 | grb : to grab, understand
11	#4 (parent #0) [Germanic] refs=AHD | grab : to grab
12	  #5 (parent #4) [English] refs=None | grab, grasp
13	--- entry 2 ---
14	ROOT Ghrěi -> redirect to Gher 3
15	--- entry 3 ---
16	ROOT [Indo-European] Ghrem : anger  (refs POK:458)
17	#1 (parent #0) [Avestan] refs=POK:458 | gram : anger
18	  #2 (parent #1) [Persian] refs=POK:458; MON:2413; FRS:187 | gozm, gožm «غزم ، غژم» : anger
19	#3 (parent #0) [Germanic] refs=AHD | grimmaz, grum
20	  #4 (parent #3) [English] refs=None | grim, grumble
21	--- entry 4 ---
22	ROOT Ghreu -> redirect to Gher 3
23	
```


## [2026-09-06T02:14:41.288Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-194.json",
 "description": "Read source JSON for page 194"
}
```


### [2026-09-06T02:14:41.326Z] TOOL RESULT

```
{
  "pdf_page": 194,
  "book_page": 164,
  "entries": [
    {
      "root": {
        "name": "Ghou-ro-s",
        "lang": "Indo-European",
        "refs": "POK:453",
        "gloss": "terrifying"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:453",
          "words": [
            {"translit": "Ğôrâh", "gloss": "terrifying", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:210",
          "words": [
            {"translit": "gŭr", "gloss": "grave", "script": "گور"},
            {"translit": "gŭrâb", "gloss": "the dome built over a grave", "script": "گوراب ۱ (گورابه)"}
          ],
          "note": null,
          "quote": {
            "text": "فریبت کمتر از جور و ستم نیست - که چاه گور از گورابه کم نیست",
            "poet": "Rashîdî"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Ghrebh",
        "lang": "Indo-European",
        "refs": "POK:455",
        "gloss": "seize"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:455; SOD:237",
          "words": [
            {"translit": "grab", "gloss": "to grab", "script": null},
            {"translit": "paiti-grab", "gloss": "accept", "script": null, "see": ["Per 3"]},
            {"translit": "gerew-âiti, gerewn-aîti", "gloss": "he seized", "script": null},
            {"translit": "gâuru-ayeiti, garb-âyaiti", "gloss": "he seized", "script": null},
            {"translit": "ni-gerepto", "gloss": "to be pressed down", "script": null, "see": ["Ni 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:374,1797,1802",
          "words": [
            {"translit": "gereftan", "gloss": "to grab, take", "script": "گرفتن"},
            {"translit": "pazîroftan", "gloss": "accept", "script": "پذیرفتن (پذیر ، دلپذیر)"},
            {"translit": "gero", "gloss": "collateral", "script": "گرو (گروگان)"}
          ],
          "note": "SNS:322 claims that Persian \"gero: collateral\" is derived from \"garîveh: neck\" meaning to accept responsibility. See root \"Gwer 3\".",
          "quote": {
            "text": "درهمه دیرمغان نیست چومن شیدایی - خرقه جایی گرو باده و دفتر جایی",
            "poet": "Hâfez"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:167",
          "words": [
            {"translit": "grb", "gloss": "to grab, understand", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "grab", "gloss": "to grab", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "grab, grasp", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {"root": {"name": "Ghrěi", "redirect": "Gher 3"}, "nodes": []},
    {
      "root": {
        "name": "Ghrem",
        "lang": "Indo-European",
        "refs": "POK:458",
        "gloss": "anger"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:458",
          "words": [
            {"translit": "gram", "gloss": "anger", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:458; MON:2413; FRS:187",
          "words": [
            {"translit": "gozm, gožm", "gloss": "anger", "script": "غزم ، غژم"}
          ],
          "note": null,
          "quote": {
            "text": "شیر غژم آورد و جست از جای خویش - وآمد آن خرگوش را آلغده پیش",
            "poet": "Rŭdakî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "grimmaz, grum", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "grim, grumble", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {"root": {"name": "Ghreu", "redirect": "Gher 3"}, "nodes": []}
  ]
}
```


## [2026-09-06T02:14:43.331Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','HRN','SOD','BQT','MON','FRS','AHD','SNS','WLD','PHD','NYB','HUB','CHEUNG','ARY','KLN','SKT','IEC','SYN','BRT','KNT']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-06T02:14:45.249Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_p
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG null
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
```


## [2026-09-06T02:14:51.742Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','HRN','SOD','BQT','MON','FRS','AHD','SNS','WLD','PHD','NYB','HUB','ARY','KLN','SKT','IEC','SYN','BRT','KNT','TTS','LKT','FSD','WEB']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print('===',k)\n    for f in ['kind','local_file','page_offset','lookup_hint','scans']:\n        if f in v: print('  ',f,':',str(v[f])[:300])\n\"; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -80"
}
```


## [2026-09-06T02:14:51.781Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,200p /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T02:14:53.813Z] TOOL RESULT

```
=== POK
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
   page_offset : POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
=== HRN
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
   page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
=== SOD
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt']
   page_offset : printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
   lookup_hint : Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (retur
=== BQT
   kind : archive_djvu+local_scan_ocr
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/re
   page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vo
   lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
   scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'o
=== MON
   kind : website+archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/in
   page_offset : None
   lookup_hint : Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
=== FRS
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt']
   page_offset : different edition — no mapping
   lookup_hint : Look up the headword (entries grouped by final letter); FRS_pages.txt has \f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.
=== AHD
   kind : archive_djvu+website+archive_restricted
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
   page_offset : 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
   lookup_hint : Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
=== SNS
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt']
   page_offset : 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
   lookup_hint : grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
=== WLD
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verificat
   page_offset : Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.tx
   lookup_hint : Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
=== PHD
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt
   page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
=== NYB
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt
   page_offset : Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
=== HUB
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt
   page_offset : leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
=== ARY
   kind : local_scan_ocr
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt']
   page_offset : printed page = pdf page + 1
   lookup_hint : Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
   scans : [{'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf', 'first_printed': 1, 'last_printed': 546, 'pdf_offset': -1, 'lang': 'fas+eng', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.tx
=== KLN
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
   page_offset : KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/detai
   lookup_hint : Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
=== SKT
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt
   page_offset : leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
=== IEC
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
   page_offset : TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
=== SYN
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
   page_offset : leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
=== BRT
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt
   page_offset : Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th 
   lookup_hint : Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
=== KNT
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt
   page_offset : leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
=== TTS
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt']
   page_offset : TTS_pages.txt: 253 leaves; printed page N = leaf N+30.
   lookup_hint : Not searched exhaustively (3 citations); the 1878 original is public domain - try IA query 'vambery etymologisches wörterbuch turko-tatarischen' or Google Books.
=== LKT
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt
   page_offset : leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
=== FSD
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
   page_offset : vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf inde
   lookup_hint : Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
=== WEB
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt
   page_offset : not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.
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


### [2026-09-06T02:14:53.854Z] TOOL RESULT

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


## [2026-09-06T02:15:17.713Z] AGENT

Now let me research. Starting with Pokorny for the three roots.


## [2026-09-06T02:15:19.848Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt; do echo \"== $f\"; grep -n \"ghrebh\\|ghrem\\|ĝhou-ro\\|ghou-ro\" $f | head -20; done; echo \"=== POK_full\"; grep -n \"lemma: ghrebh\\|lemma: ghrem\\|lemma: ĝhou\\|lemma: ghou\" POK_full.txt | head -20"
}
```


## [2026-09-06T02:15:20.383Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 45[0-9]\\|Page(s): 458\" POK_full.txt | head -40"
}
```


### [2026-09-06T02:15:21.383Z] TOOL RESULT

```
== POK_01.txt
== POK_02.txt
1430:2.  gher-  ,hart    worüber    streichen,    reiben';    vgl.    auch    die   Erweiterungen ghrei-,  ghreu-,  ghrem-,  ghren-,  sowie  oben  gröd-, Gr.  -/.eyxQog  , Hirse,  Korn',  Y.axQvq  , geröstete  Gerste'  (diss.  aus  *gher-ghro- und  *ghn-ghru-);   xegadog  n.  und   x^Q^Q'>  -d^og   f.    , Geröll,   Kies'    {*gherdd- oder  *ghernd-  ?) ;    x^Quaq^  -adog  f.  , Kiesel,  Schleuderstein' ;
1676:ghou-ro-s  ,furchtbar'  und  ,voller  Furcht'.
1701:Wurzelerweiterung  ghrebhä-i
1704:2.  ghrebh-  , kratzen,  scharren,  graben'.  (Nicht  immer  sicher  von  gJirebh- , ergreifen,  rechen*  zu  scheiden;  mit  ihm  identisch?;  siehe  Persson Beitr.  728  A.  1.)
1707:lett.  grebju,  grebt  ,aushöhlen,  mit  dem  Grabstichel  eingraben',  greblis  m. ,Hohleisen,  Schrapmesser'  (auch  Rechen,  s.  unter  ghrebh-  , ergreifen') ;
1724:ghreih-  .greifen,  ergreifen'.  Vgl.  auch  ghrebh-,
1729:1.  ghrem-  ,scharf  worüber  reiben,  zerreiben,  abkratzen',  Erw.  von  gJier-  ds.
1733:2.  ghrem-  ,laut  und  dumpf  tönen,  donnern,  grollen,  zornig  sein* ;  ghromo-s^
== POK_03.txt
=== POK_full
33501:Root / lemma: ghou-ro-s 
33523:Root / lemma: ghous- 
33551:Root / lemma: ghou(e)- 
33797:Root / lemma: ghrem-1 
33827:Root / lemma: ghrem-2 
64521:Root / lemma: dus2. aus- : us- : ear', derived from zero grade of Root / lemma: ghous- :
```


### [2026-09-06T02:15:21.471Z] TOOL RESULT

```
33232:Page(s): 450 
33259:Page(s): 450 
33279:Page(s): 451 
33363:Page(s): 451 
33404:Page(s): 451 
33437:Page(s): 452 
33450:Page(s): 452 
33499:Page(s): 453 
33521:Page(s): 453-454 
33549:Page(s): 454 
33583:Page(s): 453 
33602:Page(s): 452 
33661:Page(s): 455 
33733:Page(s): 455-456 
33766:Page(s): 456-457 
33795:Page(s): 457-458 
33825:Page(s): 458 
33868:Page(s): 458-459 
33895:Page(s): 459-460 
33943:Page(s): 459 
33975:Page(s): 457 
34143:Page(s): 454 
38029:Page(s): 451 
38054:Page(s): 451-452
```


## [2026-09-06T02:15:24.154Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '33480,33525p;33620,33680p;33790,33900p' POK_full.txt"
}
```


### [2026-09-06T02:15:24.210Z] TOOL RESULT

```
to gostb probably also Old Bulgarian gospodb "master, mister' etc. as Kurzung from 
gostbpot-. 

Maybe alb. ^os//"feast, party' a Slavic loanword. 

Barely credible is the apposition from gr. Attic tpjoo,, Ionian ^sTvoq, kor. ^£vFo(; "foreigner, 
stranger, guest's friend ' due to a present *ghs-enu-d, lengthened grade of alb. {h)uai, Geg 
{h)uj^ strange ' (from *ghsen-l s. Jokl IF. 37, 93); 

Maybe the transposition of Alb. Geg {*heuva-) huej, Tosc hua/lore\gner, stranger, guest's 
friend '. 

quite incredible SchwyzerGr. Gr. I 329; about New Phrygian ^suvs vocative {*ghs-enue7) 
s. V. Blumenthal Gl. 20, 288. 

References: WP. I 640, WH. I 660 f., 662 f. 
Page(s): 453 

Root / lemma: ghou-ro-s 

Meaning: frightened 

Material: Old Indie ^/7o/-a-/7 "dreadful, imposing, venerable ', n. " scary force, might, magic 

power '; 

Maybe alb. gjor " pitiful person' 

Gothic gaurs^ grieving ', gaunPa^ sorrow ', (75^/75/7 "mortify'. Old High German gorag' 
woeful, wretched, miserable, arm, small'; Old Icelandic gaurrm. " pitiful person' 
(Johansson KZ. 67, 221); perhaps here with ablaut and /?- further formations: Old English 
gyrn, gryn n. "mourning, grief, also gnorn, grorn m., gnyrni. 6s., gryre m. " horror ', with 
variant assimilation and dissimilation, in addition Old Saxon gornon, gnomon, grornon^ 
grieve ', grun'm. " horror '; 

kiruss. zuryty 'affWct, sadden', zurba^ care ', russ. zurftb " scold '. 

References: WP. I 636, Feist 208. 
Page(s): 453-454 

Root / lemma: ghous- 
Meaning: to sound; hear 
Note: Only indoiranisch. 
grabba-m. " selzer, handful '; 

Avestan grab-' grasp ' In b§ngrabam {casmainl) " I captured (with the eye) ', Perf. 
jigaurva, gdurvaye/t/ {compare Old IndIc grbbayant) " seizes, holds firmly, agrees. 



perceives ', participle Perf. Pass, garapta-, grab-' structure of words, sentence '; Akk. 
garabqm' the holding on, seizing '; npers. giriftan' gripe ', gTrad' seizes '; 

Old Norse grapa' snatch, grasp ' (pin support in grlpal). Old English graeppian' gripe ', 
engl. grapple' grip, grasp '; besides Swedish grabba' grapple, pack ', Middle Low 
German grabben, grabbelen' catch fast, heap ' (out of it engl. grab, grabble). Middle High 
German grappein' grope ', Norwegian dial, grafsa, grapsa' scratch, scrape ', deutsch 
grapsen; in addition nasalized Swedish dial, gramma' snatch ', Swiss grame' creep ', 
Swedish gramsa' take with full-hand ', Swiss gramseds.; asachs. garva' fascicle, sheaf ', 
Old High German garba' a handful, bundle ', Middle High German Modern High German 
Garbe, 

Lithuanian grabCis, grabnus' adroit, skilful in the stealing ', grabinetl, graballoti, grabotr 
grope, reach for something ', grabstytr gripe, pack ', lengthened grade grebiu, grebtr 
rake, gripe, rob'; previous iterative, groblu, grobtr gripe, snatch, rob', groblsm. ' robbery, 
booty'; Latvian grebju, grebt a\so ' grasp ', grabasi. PI. " the bundled together ', greblls 
"small rake ', grabju, grabf grasp, catch, rake ', grabat \teraWve in addition ' rake, gather 
together '; 

Old Church Slavic grebg, gretroar, row', russ. grebu, grestr pile, rake, oar, row', 
Bulgarian greba' rake, scratch, scrape, comb, oar, row, (water) scoop ', greblo' rake, 
rudder '; iterative Old Church Slavic grabljg, grabltrrob\ Serbo-Croatian grabitr grasp, 
pile ', Czech hrabatr scratch, dig, burrow, rummage, rake ', etc. 

Maybe alb. grabif rob ' a Slavic loanword. 

root extension ghr&i^a-: 

Old Indie grbhnati, grbhayatr seizes, sticks, attains '; innovations are: agrabhTV griped 
', Infin. grahJtum, participle grbhJta-' reigned, caught, held on ', grabhJtr, grahltr' seizor'; 
Avestan garawnaiti, gaurvayeitl. Old pers. garbayaiti' seizes, conquers, agrees, 
perceives, understands '. 

References: WP. I 652 f., Trautmann 95 f.; different Kuiper Nasalpras. 232. 
Page(s): 455 

Root / lemma: ghrdo^-2 
Meaning: to scratch, dig 



Note: (Not always certain from ghr^^-^ gripe, rake ' to divide; identical with it?; see 

Persson Beitr. 728 A. 1). 

Note: 

Root / lemma: ghrdo^-2\ to scratch, dig; derived from Root/ lemma: ghrdo^-1, ghefti^-, 

root widening ghr^^a- : to grab. 

Material: Gothic graban^6\0)\ Old Icelandic grafa^ notch, dig, prick ornaments ' (Plur. 

preterit Old Icelandic grgfum indicating to a present grefa, really records Old Norwegian 
Lithuanian griebiu, griebt/ {besides greibiu, grelbti) " snatch at, seize, gripe ', intensive 
graibau, graibyti, gribsn/sm. " quick grasp, grabbing ', Latvian gribai. " wish, volition ', 
gribef want ' (originally " reach for something '). 

References: WP. I 647, Trautmann 96. 
Page(s): 457-458 

Root / lemma: ghrem-1 

Meaning: to scratch, rub 

Note: extension from grier-6s. 

Material: Gothic gramsta Dat Sg. "wooden splinter' (Persson Beitr. 99); East Frisian grum 

" residuum, smut ' (such meaning also by grireu-an6 ghrei-), mnl. nnl. grom^ intestines, 

entrails, smut ', Low German nl. groom 6s., Norwegian Dialectal grumen^ cloudy, mixed 

with deposit, residuum ', ablaut. West Frisian gram, grim " intestines, entrails, esp. from 

fish ', Modern High German Bavarian grameF cracklings ', Old Icelandic grom, gromr 

"smut'; Modern High German Swiss grummen^ pick out, pick up, collect; pinch, rummage ' 

(Falk-Torp under ^/i//77s); 

Maybe alb. grumbuir pile, collection', grumbulloj^ collect '. 

Lithuanian gremziu, gremzti' scxa'^e', gramdau, -///"scratch, scrape', Latvian grerrizu, 
grerfizV gnaw, bite ', grarfistJV snatch ' (against another division of Baltic words see below 
ger-, ^Ae/T?- "catch'); different MiJhlenbach-Endzelin I 637, 649. compare Lithuanian 
grendziu, gr^st/ under under ghren-. 

References: WP. I 655. 
Page(s): 458 

Root / lemma: ghrem-2 



Meaning: heavy sound, thunder, grumble 

Material: Avestan gram- " become angry, feel rage ' (only in participle present gramantqm^ 
of those who are to us grimm ' and participle Perf. Pass. granta-irorc\ *ghram/ta-' becomes 
angry'), npers. yaram 'fierceness'; 

gr. xpspi^w, xP^M^tI^w " neigh ', xp6|ja5o(; m. " creakiness ', XPO|JO(; (= Old Church 
Slavic gromh) "noise, neighing ' (Hes.); 

Old Icelandic gramr^ enraged, hostile ', Old English gram. Old Saxon gram. Old High 
German gram 6s., Middle High German ^/"a/r? 'angry, irate, uncourageous ', Gothic 
gramjan^ enrage ', isl. gremia' make angry, irate ', Old English gremman^ infuriate, revile 
', Old High German gremmen^ enrage, infuriate ', Middle High German gremen^ cause 
grief, refl. ' grieve ', Old High German gramiz^ becomes angry, sad, infuriated ', Old 
Icelandic grimmr^i\erce, grim, hostile, excited, aroused ', Old English Old Frisian Old 
Saxon Old High German gr/mm'wM, cruel, savage'; Old English grimman^ rage ', Old 
Saxon grimman "wheeze, rage, bawl, blaster'. Middle High German grimmen " rage before 
anger or pain ', zero grade Old High German umbegrummon^ gnaw at ', Middle High 
German Middle Low German grummen^^roue, grumble, murmur'. Modern High German 
grummen, grumme/n^ murmur, scold, grumble, sound vaguely ', Norwegian grymta 'grur\t'. 
Old English grymettan^ growl '; 

Lithuanian gramCi, grameti^ fall with noise ', grumiu, grumetT thunder ', grumenu, 
grumentr drone vaguely, grumble, murmur, threaten'; with extension -zd- (see Persson 
Beitr. 349) grumzdziu, grurnstT gnash, creak, threaten'; Latvian gremju, gremV mumble, 
murmur, threaten, grumble, rumble; talk with passion ', Old Prussian gruminsm. " distant 
thunder ', ^/';777c»/75"sung, chanted', grJmikan^ ditty '; 

Maybe alb. gumezhiC sour\6' a Slavic loanword. 

Old Church Slavic vi^zgrbmitb, -grbmeti^ thunder ', russ. gremetb " thunder, clang, 
clink', Serbo-Croatian grm?, g'rmljeti, Czech hrmfti, poln. grzmiec^ thunder ', wherefore the 
intensive in Church Slavic gr/mat/" sour\6, clink', Serbo-Croatian dial, grimat, Czech hrfmati 
" thunder, fulminate '; Old Church Slavic gromh, russ. grom "thunder', Serbo-Croatian 
^AO/T? "thunder, lightning', Czech ^ao/t? "thunder', poln. ^/io/t? "thunder, thunderbolt '. 

References: WP. I 655 f., Trautmann 97. 
Page(s): 458-459 

Root / lemma: ghrenA^- 



Meaning: beam 

Material: Latin grundai. " a gutter ', suggrundai. " the lower border of a roof, the eaves; 

rafter ' from *ghron6!^a\ 

Old Icelandic grind\. " latticework, grid door, harbour ', Old English grindel. Old Saxon 
grindiTbar, bolt'. Old High German grintiVbar, bolt, crossbeam of the plow ', Middle Low 
German grindel, grander transom, bar, bolt, crossbeam of the plow '; 

Lithuanian grindis, grihdas, grinda^ planking board ', PI. grihdos' board layer, boarded 
floor', grindoti, grindyti, grindziu gqsti^ cover with boards ', granda^ bridge plank ', Latvian 
gr'ida, also gr'ids^ floor, plank ', gruodixw. PI. " planks, balks, beams ', Old Prussian 
grandicoi. 'plank, balk', grandan {f\Vk.) "man, husband' (to meaning compare E. Lewy IF. 
32, 162 with Lithuanian); 

Slavic ^/'(^o'a in russ. grjada^beA, row', Serbo-Croatian greda^ba\k, beam', Czech hfada 
" shaft, pole, balk, beam, scaffold, trestle', poln. grzQda^ shaft, pole, furrow, bed'; besides 
Slavic gr^db in sloven, gr^d. Gen. gred?^ shaft, pole'. 

References: WP. I 657, WH. I 623 f., Trautmann 98. 
Page(s): 459-460 

Root / lemma: ghren- 

Meaning: to rub, stroke roughly
```


## [2026-09-06T02:15:40.446Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1670,1690p;1729,1760p' POK_02.txt"
}
```


### [2026-09-06T02:15:40.516Z] TOOL RESULT

```
WF.  f  640,  WH.  I  660  f.,  662  f. i
ghou{e)-  .wahrnehmen,  Rücksicht  nehmen  auf.
Lat.  faveö,  -ere,  fcLvt,  fautum  ,bin  gewogen,  bin  günstig,  schweige  beim Gottesdienst';  favtre  aus  "^fovire  wegen  umhr.fons  ,favens',  foner  ,faventes' aus  ^-fouenis]
aisl.  gä  (*gawön)  .achtgeben,  sich  kümmern',  got.  gaumjan  ,bemerken, sehen,  seine  Aufmerksamkeit  richten  auf,  anord.  geyma  ,beachten,  sorgen für,  hüten',  ags.  gieman,  as.  gömian,  ahd.  goumen  ds.,  aisl.  gaumr  m.  und gaum  f.  , Aufmerksamkeit',  ahd.  gouma  , Aufmerken.  Schmaus',  Schweiz. gaume  ,kleine  Kinder  hüten'  (aus  dem  Germ.  lett.  gaüme  , Geschmack', gßümet  ,sich  merken,  beobachten,  schmecken'),  as.  göma  , Mahlzeit,  Gast- mahl', wovon  as.  gömian  , bewirten'.  (Die  Bedeutungsverhältnisse  sind  im einzelnen  noch  zu  klären;  s.  Slotty  IF.  46,  369.)  Dazu  ablautend  ags. ofergumian  , vernachlässigen',  as.  fargumön  .versäumen',  isl.  guma  ,achten auf ;
aksl.  govdjg,  goveti  ,verehren',  russ.  goveth  , fasten',  sloven.  dial.  goveti .mürrisch  schweigen',  skr.  ghvijem,  gbvjeti  , gehorchen',  cech.  hoveti  , be- günstigen, schonen,  nachsehen';  aus  dem  Russ.  stammt  lit.  gavUi  , fasten', lett.  gavet  ds.
WP.  I  635  f.,  WH.  I  465.
ghou-ro-s  ,furchtbar'  und  ,voller  Furcht'.
Ai.  ghörd-h  , furchtbar,  ehrfurchtgebietend',  n.  ,unheimliche  Gewalt,  Zauber- macht';
got.  gaurs  , betrübt',  gauripa  ,Betrübnis',  qaurjan  ,kränken',  ahd.  görag .elend,    arm,    gering';    aisl.   gaurr  m.    ,erbärmlicher   Mensch'   (Johansson
454  •
KZ.  67,  221);  vielleicht  hierher  mit  Ahlaut  und  n -Weiterbildung gyrn,  gryn  n.  ,TrauerS  auch  gnorn,  grorn  m.,  gnyrn  f.  ds.,  gryre  j^ ,SchreckS  mit  verschiedenen  Assimilationen  und  Dissimilationen,  dazu  as. gornön,  gnornön,  grornön  ^trauern',  gruri  m.  , Schreck';
klruss.  zuryty  ^betrüben',  zurha  , Sorget  russ.  zurith  , ausschelten'.
WP.  I  636,  Feist  208.
ghous'  ,tönen,  hören'?   Nur  indoiranisch.  J^
Ai.  ghö^ati  , ertönt,  verkündet  laut,  hört',  ghösdyati  ,findet  Erhörung bei  (Akk.)'  (Geldner  Rigveda  in  Auswahl  I  58),  ghösa-h  m.  , Getön,  Qe, schrei,  Ruf,  Lärm',  Asvaghösa  EN  ,Pferdeohr',  Harighösa  EN  ,GelbohrV (=  av.  zairigaosa) ;
av.  gao^-  ,hören',  Kaus.  in  güsayat-uxöa-  ,sein  Wort  zu  Gehör  bringend*/ npers.  niyösidan  ,hören,  horchen,  lauschen',  bal.  gösay  , hören',  niyöSay ,hören,  horchen,  lauschen',  afgh.  ngvaf.ql  ,horchen,  gehorchen',  apers. gausa-,  av.  gaosa-  m.  ,Ohr',  npers.  ^ös  ,Ohr',  skyth.  EN  ^Pad-aywaog  ,init dem  Kriegswagen  rasselnd',  av.  zairi-gaoSa-  ,mit  gelben  Ohren';  '.•^-
über  lat.  heus  ,he,  holla,  höre'   s.  vielmehr  WH.  I  643  f.  y-
WP.  I  569,  WH.  I  643  f.  ^5-
(ghre- :)  ghrö-i  gbro-  , wachsen,  grünen';  ghrös-  :  gbrds-  ,Gras,  Pflanzen- trieb'; nur  germanisch  (und  slavisch?). Got.  gi^as  n.  ,Gras,  Kraut',  aisl.  as.  gras,  ags.  grcBs,  gcers  ds.,  ahd.  gras, nhd.  Gras]    vollstufig   mhd.  gruose   f.  ,junger   Pflanzentrieb,   Pflanzensaft', mnd.  gröse  f.  , Pflanzensaft',  mnl.  groese  ,junges  Grün,  junges  Gras';
ohne  die  5- Ableitung:  aisl.  gröa  , wachsen,  geheilt  werden',  ags.  gröwan , grünen,  blühen',  engl,  grotv,  ahd.  gruoen,  gruowan,  mhd.  griiejen  ,wachseD, gedeihen,  grünen';  aisl.  grödi  m.  ,Wachstum',  mhd.  gruot  f.  ,das  Grünen, frischer  Wuchs';  ahd.  gruoni,  mhd.  grüene,  ags.  gräene,  aisl.  grenn  ,grün, neu,  gut';   Grenaland  , Grönland'.
Mit  Dentalerweiterung:  ags.  gr'^d  m.  ,Gras',  mhd.  graz, -zzes  Junge Zweige  von  Nadelholz'  aus  ghre-t-,  ghrd-t-'j
1.  ghrem-  ,scharf  worüber  reiben,  zerreiben,  abkratzen',  Erw.  von  gJier-  ds.
Got.  gramsta  Dat.  Sg.  »Holzsplitter*  (Persson  Beitr.  99);  ostfries.  grum ,Bodensatz,  Schmutz'  (solche  Bedd.  auch  bei  ghreu-  und  ghrei-),  mnl.  nnl. grom  ,Eingeweide,  Schmutz',  nd.  nl.  groom  ds.,  norw.  mdarjl.  grumen jtrübe,  mit  Bodensatz  vermischt',  ablaut.  wfries.  gram,  grim  ,Eingeweide,  bes. von  Fischen',  nhd.  bair.  gramel  , Griebe',  aisl.  gröm,  grömr  , Schmutz' j nhd.  Schweiz,  grummen  ,klauben,  stöbern',  grummelig  ,brockig'  (Falk-Torp unter  grums) ;
lit.  gremziu,  gremzti  ,schaben',  grdmdau,  -yti  ,kratzen,  schaben',  lett. gremzu,  gremzt  , nagen,  beißen',  graffistU  , zusammenraffen'  (gegen  eine  andere Einreihung  der  halt.  Worte  s.  unter  ger-,  grem-  , fassen') ;  anders  Mühlen- bach-Endzelin  I  637,  649.  Vgl.  lit.  grendziu,  gresti  unten  unter  ghren-.
WP.  I  655.
2.  ghrem-  ,laut  und  dumpf  tönen,  donnern,  grollen,  zornig  sein* ;  ghromo-s^
, Getöse'.
Av.  gram-  , ergrimmen,  Grimm  hegen'  (nur  im  Partiz.  Präs.  grdmdntam , derer,  die  uns  grimm  sind'  und  Partiz.  Perf.  Pass.  granta-  aus  *ghramita' , ergrimmt'),  npers.  yaram  , Grimm' ;
gr.  xQeixit,(ji},  x$£^£t/^w  , wiehere',  XQOf^ccSog  m.  ,Knirschen',  XQ6i.iog  (=  aksl. grom'b)  , Geräusch,  Gewieher'  (Hes.);
aisl.  gramr  , ergrimmt,  feindlich',  ags.  gram,  as.  gram,  ahd.  gram  ds., mhd.  gram  , zornig,  unmutig',  got.  gramjan  , erzürnen*,  isl.  gremia  , zornig machen',  ags.  gremman  , erbittern,  beschimpfen',  ahd.  gremmen  ,erzürnen, erbittern',  mhd.  gremen  ,gram  machen',  refl.  ,sich  grämen',  ahd.  gramiz jtraurig,  erzürnt,  ergrimmt',  aisl.  grimmr  , grimmig,  feindlich,  erregt',  ags. afries.  as.  ahd.  grimm  , wild,  grausam';  Sigs.  ginmman  , wüten',  a.s.  grimman  j , schnaufen,  wüten,  tosen',  mhd.  grimmen  ,vor  Zorn  oder  Schmerz  'wüten*, schwundstuf.  ahd.  umbegrummön  , benagen',  mhd.  mnd.  grummen  , brummen,  | murren',  nhd.  grummen,  grummeln  ,murren,  schelten,  dumpf  ertönen',  | norw.  grymta  , grunzen',  ags.  grymettan  ,fremere' ;
lit.  gramü,  grameti  ,mit  Gepolter  fallen*,  grumiü,  grumeti  , donnern', grumenü,  grumenti  , dumpf  dröhnen,  murren,  drohen*;  mit  Erweiterung -zd-  (s.  Persson  Beitr.  349)  grumzdziü,  gruihsti  ,knirschen,  knarren,  drohen' ; lett.  gremjii,  gremt  , murmeln,  im  Affekt  reden,  drohen,  grollen*,  apr. grumins  m.  ,ferner  Donner*,  grtmons  ,gesungen*,  grimikan  , Liedchen* ;
459
aksl.  vzzg7^mitb,  -grhmeti  , donnern',  russ.  gremeh  , donnern,  klirren',  skr. g7"fni,  Q'f'mljeti,  öech.  hrmiti,  poln.  grzmiec  , donnern',  wozu  das  Intensivum in  ksl.  grimati  , tönen',  skr.  dial.  grimät,  cecli.  hrimati  , donnern,  wettern' ; aksl.  grorm,  russ.  grom  ,Donner',  skr.  gr5m  ,Donner,  Blitz',  cech.  Jirom Donner',  poln.  grom  , Donner,  Blitzschlag'. WP.  I  655  f.,  Trautmann  97.
0
ghten-  , scharf  worüber   streifen,    zerreiben'.    Erw.    von   2.  gher-  ds.,    meist mit  dentaler  Erweiterung  (ursprüngl.  präsentisch?). Gr.  xQaivü)  , streife,  bestreiche';
dazu  mit  Formans  -tu-  (-to-),  aisl.  grunnr  m.  (nn  aus  np)  ,Boden,  Grund' (Grundbed.  ,Sand,  Sandboden'  als  ,*Zerriebenes'),  grunn  n.  , seichte  Stelle im  Wasser',  grund  f.  (m.  gramm.  Wechsel)  ,Feld,  Erde',  got.  grundn- toaddjus  , Grundmauer',  ags.  as.  grund,  ahd.  grünt  , Grund,  Boden'.
ghren-d- :
Gr.  xövÖQog  m.  , Graupe,  Korn'  (diss.  aus  "^XQOvd-Qog)'^ alb.  {-d-  oder  -dli-)  gründe,  krunde  , Kleie'  (*ghrn-d\}i\a)] lat.  frendö,  -ere  , zermalmen,  die  Zähne  knirschen'; aisl.  grotti  m.  ,Mühle'.
ghren-dh- :
Ags.  grindan  , zerreiben,  zermalmen',  engl,  to  grind  ,ds.,  schärfen'  (ags. grindan  mit  töpum),  engl,  to  grind  ones  teeth  ,die  Zähne  knirschen';  nhd. (ndd.)  Grand  ,Sand',  ndd.  grand  f.  , grober  Sand,  grobes  Mehl,  Kleie', ahd.  in  grente  ,in  argillosa  terra',  risI.  grandi  m.  , Sandbank,  Kies';  ndd. grind  f.  , Kieselsand;  , Schorf,  nid.  grind,  grint  , grobes  Mehl,  grober  Sand'. 'ahd.  mhd.  grint  , Grind,  Schorf,  got.  grinda-frapjis  ,kleinmütig'  (von  einem adj.  *grinds  ,*zerrieben') ;
lit.  grendu,  gresti  und  grendziu,  gresti  , tüchtig  reiben,  scheuern'  (dehnst. Präs.),  Iter.  grdnd-au,  -yti  (vgl.  gremzti  oben  unter  1.  glirem-)]  russ.  grjada.
WP.  I  656  f.,  WH.  I  545  f.,  Trautmann  96  f.
ghrendh-  ,Balken'.
Lat.  grunda  f.  ,GTeyri\  suggrunda  f.  , Dachstuhl'  aus  '^ghrondhäy aisl.  g7'ind   f.    , Gitterwerk,    Gittertür,    Hafen',   ags.   grindel,   as.   grindil , Riegel',  ahd.  grintil  ,Riegel,  Pflugbaum',  mnd.  grindel,  grendel  , Querholz, Riegel,  Pflugbaum';
lit.  grindis,  grindas,  grindä  , Dielenbrett',  PI.  grindos  , Bretterbelag,  ge- dielter Fußboden',  grindöti,  grindyti,  grindziü  grlsti  ,mit  Brettern  belegen', grandä  ,Brückenbohle',  lett.  gr\da,  auch  grzds  , Fußboden,  Diele',  gruodi m.  PI.  , Bohlen,  Balken',  apr.  grandico  f.  , Bohle',  grandan  (Akk.)  ,Mann' (zur  Bedeutung  vgl.  E.  Lewy  IF.  32,  162  mit  Lit.);
460  f
slav.   greda  in   russ.   grjadd   ,Bett,    Reihe',   skr.   greda   ,Balken',   Sech. Jifada  ,Stange,  Balken,  Gerüst^  poln.  grzeda  ,Stange,  Furche,  Beet' ;  daneben  -. slav.  gr^db  in  sloven.  gred,  Gen.  gredi  , Stange'.
WP.  I  657,  WH.  I  623  f.,  Trautmann  98.
1.  ghreu-  :  ghrau-  :  ghrü-  ,zusaninienstürzen,  einstürzen,  auf  etwas  stürzen'.
Hom.  Aor.  exqccov  (ßxQaJ^ov)  ,überfiel,  bedrängte*,  ^axQrjrjg  ,heftig  andrän-
gend,  ungestüm'  (-XQ^-f^-VO)  j
lat.  ingruö,  -ere  ,mit  Heftigkeit  hereinstürzen,  hereinbrechen',  congrua^ -ere  »zusammenfallen,  zusammentreffen';
lit.    griäuju,    grioviau,    griduti    ,niederbrechen    (trans.    intr.);    donnern* (iau  aus  eu;  daraus  das  r  von:)  griüvü  {griy,vü,  Trautmann  100),  griuvaü griüti  ,zusammenf allen,  in  Trümmer  fallen*  (griüvü  =  lat.  -gruö  aus  ^ghruuö)'^    ' lett.  ^J^aw;w,  grävu,  gi^aut  ,zertrümmern',  grüstu,  gruvu,  grut  ,einstürzen*,  ■ gfuveli  m.  PI.  , Schutt';  Anlautdoublette  neben  qreu-  (s.  dort)?
```


## [2026-09-06T02:15:41.088Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==231' HRN.txt | head -70"
}
```


### [2026-09-06T02:15:42.708Z] TOOL RESULT

```
- 209 -
aw. gaifiti- 'Gestank'; phlv. gand 'Gestank', gandak
stinkend*, gandakth ; ai. gandhd- *Geruch, Duft (wohl-
riechend)'.
af}'. ganda 'stinkend'; bei. LW. gand 'Kot, Mist'
(97) — gandag, n. ganday schlecht, böse' dagegen stellt
Bartholomae, ZDMG. 44, 552 zu ap. gasta- *übel,
widerwärtig* ; sar. yofid.
935. gend/um *Weizen', ar. LW. jandum in jauz-i jandum.
skr. gödhüma- 'Weizen* (dagegen iran. ^gandhüma-^
Hübschmann, ZDMG. 44, 556 2)); phlv.-paz. gantum
d. i. gandum (PPGl.).
LW. kurd. genim (vergl. g. gamim); af/. yanum;
wa/. yid%m, sangl. minj. yanddm, sar. zandani, sandum,
^\yn. zindum, yidg. yadum; bei. gandtm (98).
936. gunde *Hefenballen (für ein BrotV.
aw. gunda- (vd. 3, 32) 'Teig (Geldnor, KZ. 24,
549 Note 4); phlv. gundak.
Unsicher.
937. gv/ng 'stumm' 8).
skr. [/^guüj-, gufijati summen, brummen' (Geiger:
'das Brummen bezeichnet die tierischen Laute des
Stummen im Gegensatz zur menschlichen Sprache').
Unsicher.
LW. afy. bei. (77) gung stumm*.
938. gor 'Wildesel*, gür/er,
ai. gäurd' 'weisslich, gelblich, rötlich; eine Büflfel-
art: Bos Gaurus* (Spiegel, Ar. Periode 55); phlv. gör
(Papyrus, Hörn ZDMG. 43, 51 und 619).
LW. kurd. gör; afy. yyara; bei. gör 'Wildesel' (80).
^) Das angebliche phlv. ganäk, ganräk erklärt Bartholomae
a. a. O. auch nicht richtig, es ist höchst wahrscheinlich mit Andreas
druväk zu lesen. — Nach der ganz anderen Auffassung Thumb*s von
KRa 56 ff., KZ. 32, 132 wäre ap. gasta- mit Kern zu skr. l'^gad-
'sprechen' zu stellen.
*) Das Yerhältniss des ai. ö zu dem iran. an ist unklar.
') Hierher wird geng bei AM. gehören (von der Stimme, 203
Zeile 5, von Schmerzen, 236 Zeile 8, vom Kopf gesagt, 90 Zeile 12),
dofl zu yeng *gekrummt' jedenfalls nicht passt.
U o r n , Grundriss d. neup. Etymologie. 1 4
```


## [2026-09-06T02:16:28.930Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==232' HRN.txt | head -80"
}
```


## [2026-09-06T02:16:30.431Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN gram/gazm\"; grep -n -i \"yazm\\|gazm\\|yaram\\|garam\\|Grimm\" HRN.txt | head -30; echo \"== HUB\"; grep -n -i \"yazm\\|gazm\\|yaram\\|Grimm\" HUB.txt | head -30"
}
```


### [2026-09-06T02:16:30.586Z] TOOL RESULT

```
— 210 —
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
942. göspendj gösfend 'Kleinvieh, Schaaf, Widder, Ziege'.
aw. gaospenta- (vd. 21, 1); phlv. göspaud.
943. gas 'Ohr*.
ap. gausa- 'Ohr'; aw. gaosa- 'Ohr*; phlv. gös; ai.
ghoSa- 'Lärm, Getön .
kurd. güh; afy. yvay; oss. d. yos, t. qüs (94); bei.
gös (125); wa/. yws, yis etc.
np. gösvär^ ^öst^äre 'Ohrgehänge*: aw. frä.[gaosävara-,
mat,[gaosävare; phlv. gösvär,
944. gast 'Fleisch*.
aw. gäv, Nom. gän§ 'Fleisch' ; phlv. göst^ göstm (GFr.).
LW. afy. yva/a 'Fleisch'; kurd. güst; bei. gö$t, n.
göM (128); wa/. gust, minj. yös, sar. gü^t, siyn. goß,
^) Zuerst hat dies wohl Bückert, ZDMG. 10, 183 ausgesprochen.
«) Vergl. Fr. Müller, WZKM. 5, 263.
```


### [2026-09-06T02:16:30.662Z] TOOL RESULT

```
== HRN gram/gazm
2396:bang 'RsLiif; nhd. Bangenkraut 'Schierling* (Grimm,
9434:schwed. franz. hurrn (s. Grimm, Wörterbuch).
21723:w. uezyaram 36.
== HUB
```


## [2026-09-06T02:16:46.720Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD gor\"; grep -n \"^gōr\\|^gwr\\|^gōr \" PHD.txt | head; grep -n \"grave\" PHD.txt | head -20; echo \"=== PHD grift/grab\"; grep -n \"^griftan\\|^gīr\\|^padīr\\|^graft\\|^grōw\\|^graw\" PHD.txt | head -20"
}
```


### [2026-09-06T02:16:46.801Z] TOOL RESULT

```
=== PHD gor
455:mand [mnd | = M] house. miindag [m?ndk! | M m'ndg, N ~a] tired; remiss; fault, sin. “Аһ: tiredness. māndan, !màn- [K TLWN-tn! < A У ktr | M mnd, N ~] stay, remain; v. also % *mán-. mang [mng] henbane. mänig [mnyk'] household member. mānistan [{KTLWNstn'] = mandan. māništ [m?nyst!] abode, dwelling. ~ag [-k'] sedentary, settled. mānsār [mnsl = Av. ma0ra-] (holy) word, spell. -~-bar [-b/] priest. ~spand [-spnd = Av. spanta-] holy word; v. máraspand. imar [ml | M mr, N ~] number, reckoning, account; class. *mar [m/] scoundrel, felon. таг [ml | N ~] snake. mār-, —išn, v. mārdan., тагар [mik!] number. тпагар [mPk!] perceptive, sensitive. Māraspand [mrspnd | N ~] (= máns?rspand), cal. 29th day. *martabuk [mic”5wk'] brave, valiant. ~ith: bravery, valour. mard [GBRA < A gbr; mlt' | M m(y)rd, N ~) man. mārdan, màr- [ml-tn'] perceive, notice, feel. ~i$n: perception. „išnūmaud [-£rwmnd] perceptive. mardanag [mit?nk! | N ~a] manly, brave. ~ih: manliness, bravery. mardóm [ANŠWTA < A?niwt?; mltwm | M mrdwhm, N mardum] man, mankind, people. ~th: humanity, humanness. mardóm-zàádag [mltwm 2tk' | N mardum-zād] human being. ~ih: humanity. marģ [mlg | M mrg, N ~] death. ~-arzan [-lc’n'] deserving death. ~ih: = marg. --0mand [-”wmnd] mortal. mārīģ [m'Lyk! | M mryg-] word, spell. marw [mlw! | M mrw, N —, (mary)] herb. marz [mlc | M mrz, N ~] boundary, march; astr. term. marzanģēūš [mlengws | N ~] marjoram. marzidan, marz- [mlc-ytn! | М mrzyst, mrz-] copulate. išn(īh): copulation, fornication. marz(o)bàn [mlcp’n' | № ~] margrave, warden of the marches. -masāy [-ms'd] suffix, -sized. mast [mst! | = M, N ~] bemused, intoxicated.
2728:march (border) marz; ~ warden, margrave marzoban.
=== PHD grift/grab
2133:griftan.
5279:griftan!, kardan!
5372:graw(a)gin TONS galog ` sy drubuštīh ^U үез | ov» drubušt ITED aor druz a, >
```


## [2026-09-06T02:16:48.519Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB\"; grep -n \"grave\\|gōr\\b\" NYB_vol2_glossary.txt | head -20; echo \"=== NYB grift\"; grep -n \"^grift\\|^gīr\\|^padīr\\|grav-\\|grabaya\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T02:16:48.598Z] TOOL RESULT

```
=== NYB
1632:garän [gl'n'] heavy, hard, grave, comp, tar, 125. 14! etc. passim. — Derived from OIr *garu-, Av. (524) gouru- in compounds, Skr guru-; MPrthPrs gr’n; Paz. garg, gira; NP girän.
2164:*kai-bāg [kdb’(g)] “having share with the kat", "sharing with the king" = co-regent 221’, v. also ném-vécak. — Coin- cides graphically with KDB’ = drag ‘lie’, which is sheer nonsense in this context. Np kiyd ‘a king, protector; a lord, a margrave’, also n. pr.
2196:kandan [HPLWN-tn', kndn'] kan- 1. to dig, pl. kand engraved 113%. — 2. to destroy 4271, 7114. 9918; to tear up by the root 3316, — 3. bé ~ to throw out, to drive away 34’. — Two different vbs.: 1. Av. OP (437 sg.) 2kan-‘ to dig’, whence also gukān- (g. v.); 2. kan- ‘to throw’, whence also apakandan, frakandan, par- gandan, Morgenstierne, AO I, 249; Ver- bum 172. MPrs and NP ‘to dig’, Paz. cadan, xan- with an initial x- confirmed by the Arab. lw. randag ‘trench’ and Skr khan- (pt. khāta-). V. also kanišn.
2477:marz-pän [mlep’n'] governor of a border district, margrave 1*. 115°. 117’. — Av. (1153) maraza- ‘border district’, MPrth mrz (A-H III, BBB) + pin ‘protector’, v. pünak; borrowed in Arm: marzapan, in Aram: Syr marzbänä = Talm, and in Arab: marzubün; NP marzbün.
3377:?sak [sk'] stone 10224, — Ps. sky; MPrs sygyn ‘of stone’ (A-H II) suggesting stk, NW form of OP ikä ‘gravel’.
=== NYB grift
1708:griftan [HDWN-tn'], pres. gīr- [SHDWN-], pt. = pret. pass. 3d p. sg. grift (HDWN-t'; glpt' 325], to take, to seize, to catch, to take possession of 527. 613, 75.10-13.20 82.11.16, 910. 1010, 1615, 2221, 2417, 301. 328-11.20, 408, 7425; — apar ~ 1615, frdc ~ 98% id.; {frac ~ to embrace 4315; — hešm ~ to get angry 3%, 15%; martömän pat kunisn girénd they (the heavenly gods) call men to account for what they do 65?, cf next w. — Av. OP (526 sg.) grab-; MPrth gryfin gyrw-, Ghi- Jain 89; MPrs gryptn gyr-, Verbum 205; Paz. griftan (pt. girift, girft) gir-; NP giriftan gir-. — As to 35%, v. *gir-; as to 10215, v. gil-. — The ideogr. "HDWN coin- cides graphically with the ideogr. BYD- WN-; all passages containing ‘HDWN- are enumerated above. — V. also pati- griftan.
1709:griftar [glpt’]] a p. who "catches”, i.e. incurs, liability: 1. ku pat dat 1 dévan ~ né bavé lest thou shouldst be subject to the law of the demons 6916-17; [ruvan pat ménoyan pat kunišn aržānīkēh ~ kunénd in the heavenly world they (the gods) call the soul to account according to the value of her deeds Mx ch. 382-6 (~ kunénd = girénd 65°, v. griftan)]. — 2. condemned to (šahrē-karān, v. s. v. kar) 92; prisoner: ~ kartan to imprison, to capture 615; [more general, to catch hold of: api-§ — kunēt u apāc 6 rah i yazdān āvarēt Mx ch. 1525]. — Cf NP gér?ftàr; v. also a-griftär.
```


## [2026-09-06T02:16:54.609Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in PHD_mackenzie.txt PHD_pages.txt PHD.txt; do echo \"=== $f\"; grep -n -o \"gōr \\[[^]]*\\][^.]*\\.\\|griftan[^.]*\\.\\|padīr[a-zē]* \\[[^]]*\\][^.]*\\.\\|graw \\[[^]]*\\][^.]*\\.\\|grawgān[^.]*\\.\" $f | head -12; done"
}
```


## [2026-09-06T02:16:55.387Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT grab\"; grep -n \"garəw\\|gərəw\\|grab-\\|gaurvay\\|garəb\" BRT.txt | head -30"
}
```


### [2026-09-06T02:16:56.316Z] TOOL RESULT

```
=== PHD_mackenzie.txt
1912:griftan) I N --] I.
2361:griftan: undertake, perform; appoint, decide.
2570:graw [glwb I N giraw] pledge, security.
5290:griftan: say 'grace'.
5932:griftan, gumardan,histan.
6341:griftan.
6687:griftan.
6808:griftan.
7247:griftan,!kardan,wizardan.
7408:griftan.
7745:griftan, stadan; ,.
7863:griftan,     upside down er ud abar, nig1in.
=== PHD_pages.txt
1912:griftan) I N --] I.
2361:griftan: undertake, perform; appoint, decide.
2570:graw [glwb I N giraw] pledge, security.
5290:griftan: say 'grace'.
5932:griftan, gumardan,histan.
6341:griftan.
6687:griftan.
6808:griftan.
7247:griftan,!kardan,wizardan.
7408:griftan.
7745:griftan, stadan; ,.
7863:griftan,     upside down er ud abar, nig1in.
=== PHD.txt
310:griftan) | N ~] 1.
310:graw [dstglwb!] captivity.
347:griftan: undertake, perform; appoint, decide.
380:griftan.
540:griftan: take refuge with.
649:griftan: say ‘grace’.
816:griftan, gumārdan,hištan.
1514:griftan.
2133:griftan.
2289:griftan.
3090:griftan,kardan,wizārdan.
3359:griftan.
```


### [2026-09-06T02:16:56.373Z] TOOL RESULT

```
=== BRT grab
10400:•  j.    garapta-    Adj,    (fem.    'lä-),    VVlP.:\aAur3m    Tim  Yt.  70.25;  —  tattuATs'  Tii s.  grab-.  (näml  fravasays)  Yt.  /J.30.
10405:'grab-  3
10436:•  j-,  g.,  p.  'grab-  V.  'greifen'.  Praes. i  grab-,  11%  g^rminä'^,  15  girißa-*'"'^ , 23  garb.tya-,  gSun'aya-'^,  24  gSurvaya-'^, <)-^  24 ^3r?mbaya-'^,2T g)r3bya-,gpr)uya-^'>; Perf  I  jagaurv-*^,  jayaurv-^^,  ftgaurv-^^, 2  jag»r»b-.  —  PPf P.  g^r^ta-'');  Inf.  gfnbqm.
10452:'grab-  mit  ham
10467:5*9  'grab-  Noten  —  yzar-  mit  aiwi  530
10472:geschr.;  S  i^^S.  39.  —  »)  S  5J  H.  —  3)  Stall  [  j-  .f™":  s.  unter  ^grab-.
10487:.   j,    'grab-    (Fassung  uzw.  von  Wortern,        _  p^..  t„nsskr.,    erL.:  /.Fw-f  'Geschenk.  Be-
10508:Ei.f  —  mp.'(Pü.)  grm<,  np.  7rtrr'.  —  ')  Oder   yiaroutJs    (IP.    als    NP.)    * antari.ar»o)m ■,^0«.  (S  268.  37);  ob  zum  V.  grab-t  .  -^rt/«,^^^  V.J.  19.
14928:Eig.  'receplaculum',  zum  V.  grab-.  —  ai.  vgl. praligraAana-  n.  —  ')  Es  könnte  'nä  auch NPn.  »ein.
15590:Nach  Pü.  zum  V.  grab-;  also  'girimby''!  — Pa.;  fratam  kac  dahmän  ke  apar  glrlt pätixiäh
29346:•  j.  han-gnt^-amna-  Adj.,  PPM.:  s. grab-.
```


## [2026-09-06T02:17:06.157Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"wild ass\\|onager\\|grave\\b\" PHD_pages.txt | head -20; echo \"---- gor lines\"; grep -n \"g[ōo]r \\[\" PHD_pages.txt | head -20; echo \"---- context 2565-2580\"; sed -n '2560,2580p' PHD_pages.txt"
}
```


### [2026-09-06T02:17:06.237Z] TOOL RESULT

```
2546: 110r [gwll N -] onager, wild ass.
7045:  margrave marzoban.                       melt widaxtan.
7172:noise pattan; v. sound                 onager gor.
---- gor lines
---- context 2565-2580
l1~z [gwe IN-] walnut.
  -enag [gwzynk l IN gozina] a walnut sweetmeat.
GOzihr [gweyhl I Ar. jawzahr] astr. the Dragon.
  - dumb: the descending node of the moon.
  - sar: the ascending node of the moon.
grab [gl)l> I P gr)b] womb.
grlmag [gl)mk l I P gr)mg] possessions, wealth.
Ilrimlg [gl)myk l I M gr)myg, N girami] treasured, dear.
  -ih: affection, respect.
19raw [glwb l I P grww] cane.
zgraw [glwb I N giraw] pledge, security.
                 '
  -ih, -(a)l1ln [glwk)n' I M grwg)n, N giraugan] = Igraw.
grayidan, grAy- [gl)d-ytn' I P gr)y-,N giray-] lean, incline; intend, desire.
grtftan, l1ir- [OHDWN-tn l < A"'; )lzd; glptn', gyl- I M grypt, gyr-, N
    ginftan, -] take, hold, restrain.
  -iAnig: tangible.
grtftar [glpt)ll N gir-] held, taken; captive.
 -Omand [-)wmnd] tangible.
grih [glyh I N ginh] knot.
19riw [CWLE < A Iwr-h; glyw l ] neck, throat.
```


## [2026-09-06T02:17:06.959Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index gor/grab\"; grep -n -i \"GHREBH\\|GHOU\\|GHREM\" incoming/ARY/ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-06T02:17:07.039Z] TOOL RESULT

```
=== ARY latin index gor/grab
2429:. pls GME ow els ghoul 9 te Gd Sz PTY cal wt
13963:(OLD CHURCH SLAVIC) A 5 MELUI, MEGHOU :(ARMENIAN) | ‘
```


## [2026-09-06T02:17:16.820Z] TOOL CALL #20: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-06T02:17:16.826Z] TOOL RESULT

```


```


## [2026-09-06T02:17:18.308Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY گور\"; grep -n \"گور\" incoming/ARY/ARY_pages.txt | head -20; echo \"=== ARY گرفتن\"; grep -n \"گرفتن\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY غژم\"; grep -n \"غژم\\|غزم\" incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-09-06T02:17:18.397Z] TOOL RESULT

```
=== ARY گور
324:و استپ‌های آسیای مرکزی گورهایی یافت شده که دارای ویژگی‌های خاصی هستند. جسد پا اجساد
325:در درون گور ساخته شده از سنگه‌های تراشیده شده قرار دارند و روی گور تپه‌ی کوچکی
332:بودند. یافت گورهای تقریباً مشابه این گورکان‌ها (1780۸15) در سایر نواحی هند و اروپایی ۱
616:قبر و روی گنجانه‌های سفالین. وجود گورهای برجسته (1)1180۸) و آثار ویرانی ساختمان‌ها و
699:زبانهای قفقاز و گورهای سبکك کورگان (1180۸) در شمال آذربایجان مسیر کوچ این اقوام
700:ایرانی را نشان می‌دهد. گورهای آذربایجان (مثل کورگان‌های اوکرائین) دارای دیواره‌ی چوبی بوده
1360:۳-واژه‌ی «گوره با واژه‌های انگلیسی 07۸7 و آلمانی 0۸ همسانی چشمگیری دارد. آیا
4102::۱ چم این واژه در زبان‌های لاتین و ایرلندی کهن و ولزی: درخت انگور) تاک.
8947:رز (به چم*درخت انگور) / ۲۰۳
13229:۶ | گور (به چم "قبر" *آرامگاه»)
14417:شراب از انگور مرسوم‌تر شد). امروزه واژه شراب در اکثر زبان‌های اروپایی از واژه‌ی لاتین ۷1۸۷0086 آمده است و
=== ARY گرفتن
647:ایران راگرفتند ولی آثار و بقایای زبان هندی در بین‌النهرین بجا ماند.
1029:می‌گرفتند. در حماسه‌ی ابلیاد (1۸0ن11) اثر هومر آمده است که پریام (/۳۸1۸3) شاه تروا دو زن
1058:پردندکه نه تنها در بسیاری از امور مورد مشورت شاه قرار می‌گرفتند بلکه گهگاه نیز در برکنار سازی
2481:و فرار گرفتن" و دبگری 818۳ (۱۰۱۹) به معنی "ایستاندن" و ار دادن", 8
3523:۱ این واژه در اکثر زبان‌های هند و اروپائی دو چم دارد: بردن؛ گرفتن.
6572:۲ چم اين واژه در زبان‌های ژرمنی کهن "گرفتن" برده ولی در زبان‌های ژرمی نوین چم آن اپا زور بلند کردن*
6574:۳ چم این واژه در زبان‌های لاتین و -لنی؛ اسیر گرفتن.
=== ARY غژم
```


## [2026-09-06T02:17:24.571Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13200,13260p' incoming/ARY/ARY_pages.txt; echo \"########## 1340-1375\"; sed -n '1340,1375p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-06T02:17:24.640Z] TOOL RESULT

```
روسی (8314(7/): هتاختاه 19497 ۸002 أ
لینوانی (/(1777114(74.)): این ان 3 (لت۸ه8) رد هس :
90908 ناه ۱
برهان قاطع : ۶ و ۱۸۶۴ ۱
یادداشت: ۲
چم این واژه در زبان یونانی: فرورفتگی؛ گودی :
چم این واژه در زبان لاتین:کیسه‌ی چرمی ۱
1
ِ
اوستایی (4/88727): 3171 روسی (۲/5514/۷): 1
پهلوی (/۸۷ا۳۸): ,۸ انا چکه (28077)): زد ۷۸:۱
606330۸ لینرانی (۷(فسابز ).03830 ,6883
سانسکریت (8478617): ال
ارمتی (/47۸48(14): ود ده پسگشت‌ها ند دنت
برنانی 022/0): ۰ 81871108162100 ,803 زر ار 1 را
لاتین (7100مل): 0 ,۷۵۵05 8 وی
فرانسه (۳8۵۸04): ۷۵۸ 2 ۷۵8۸۳۵ :
اسپانیایی (82۸(/37): ۷0۸2 9 (۷۸83ه) 1
ایتالیابی ((74/14): " اد ۵( 0 (016557) :0/2[5ت) لا
پرتغای (82ق070010: ۷۶ 6 (5ت۷۵8۸6101) :0100/5
اسلاوی کهن (10لمل5 70674 صا۵): 5 ۷۵5۸0۳ 147
ی 271 برهان قاطع : ۳۷
بادداشت:
۱- هوبشمان این واژه‌ی فارسی را با واژه‌ی سانسکریت ۷1۰1۳۸18 همريشه می‌داند (برهان قاطع :: ۱۸۴۷) ْ
۲ پسوند ۰۷030178 (مثلاً در واژه‌ی 0۸71۷030118) نیز از همین واجریشه است.
۳ چم این واژه در زبان‌های سانسکریت و اوستایی و یونانی و چکه: بلمیدن. ۱
۴ هیچکدام از پسگشت‌ها (مراجع) من به رابطه‌ی واژه‌های ایرانی این فهرست با دیگر واژه‌های این فهرست اشاره
نکرده‌اند و بهمین دلیل در جلو واجریشه‌ی هند و اروپایی (شاید) آورده‌ام. ۱
[pdf page 445]
۶ | گور (به چم "قبر" *آرامگاه»)
کردی (80157ل). ما6 اد زاین
افغانی (پشتو) (//۸۳0/1۸2): 00 لهستانی (۳0.157):. ری نی
سانسکریت (84(55777): ان روسی (7551۸ا#): زاین
گرتیک (007/0): ۸ بقف28 چک (ل280): 1105
اپسلندی کهن (۱۵۵۷ ۸1۸۷ ظ شک صام). برهمی (80/78۸4۵۷4): 108
35 ,605 اسلرا کی (51.01/۸4): 108
ساکسونی کهن ((54300 صاه): تفع آلبانی (00مالمقلم: دراد
آلمانی کهن (/08804 6#ابز صام): قطان
آلمانی (08801۸00): زا دی پسگشت‌ها رد۲۳
انگلیسی گهن (0ل8ل2001 صام: جفون رم
۱ انگلیسی (بلولاه/(8): دیاب 7 (08۸78) نب
دانمارکی (0۸(/3[7): دیدن 3 ,293 ناه
سوئدی (8108215/7): هه 1 (63۸78) :00/70/5
نروژی (/0/0777501۸: لیات نی 8 (8۸15ع) +37
هلندی (7ع007). ان برهان قاطع : 1۸۵۰
اسلاوی کهن (۲10شا5 17ع#نابل) صا۵):
یادداشت:
چم پیشین این واژه در زبان‌های ژرمنی: کندن» چال کردن,
َ اوستایی (/4۲/8574). 811 ,۸083۸ افغانی (پشتو) (/۸۳017۸۸۷).
پارسی باستان (امفای۲۶۴ صا0):. هلاقتاهج 7 ما۸6 17۷
پهلری (7ماتزمه): 03 سانسکریت (54(/5877): 7105۸
اوستی (0558716): 8 ,01108 آرمنی (۷ل۸7248(/[4): 1
کردی (82015/7ن۸): ای پونانی (0765/0): 0585
بلوچی (7677انل8۸): انا لاتین (۸700ل: هانا۲ت3تا۸ ,قاتا
[pdf page 446]
گوشه / ۴۴۷
فرانسه (نل۳6۸): نت0۶۵ هلندی (07677): 008
اسپانیایی (8۸۸/157): 023۸ اسلاوی کهن (۲16ها5 بل#6ناتل) 0ا0):
ایتالیایی (/هفلله7): 0۵00 10
رومانی ((۸4۸(/14ن): هد زا لهستانی (54/ءا۳0): 10
پرتغالی (070010532): 0۸ روسی (894(7/): 10
########## 1340-1375
رویداد نام تبریز چه پود؟
امید برای پژوهشهای آینده :

همانطور که در بالاگفته شد» این کتاب عبارت است از گامی نخستین در راه یافتن همه‌ی
واجریشه‌های هند و اروپایی زبان فارسی.گام‌های نختین معمولاً خالی از کاستی و لغزش نیستند.
امید من این است که پژوهشگران دیگر به تدریج کاستی‌ها را برطرف کرده و فرهنگه‌های کاملتری از
ریشه‌های هند و اروپایی زبان فارسی ارائه دهند.
هنوز صدها واژه‌ی ناب فارسی وجود دارند که یافتن واجریشه‌ی هند و اروپایی آنها به

بن‌بست برخورده است. برای مثال به واژه‌های زیر توجه کنید:

۱- واژه‌ی «هاله» (یونانی: 05له) لاتین:13۸7.058 ؛ انگلیسی: هل فرانسه: ۲۸,0 ؛
آلمانی: 1307) از کجا آمده و اجریشه‌ی هند و اروپایی آن چیست؟ ۸30۶ موی

۲ آیا واژه‌ی «شور» (پهلوی: 50) با واژه‌های انگلیسی:ن501 و آلمانی: ن8۸1
(واجریشه‌ی هند و اروپایی:81-08" - 1039 :۳010507۷) همربشه است۹* ۰ ۵4 بن

۲- واژه‌ی «لوج» فارسی با واژه‌های 1.0112778 فرانسوی و 17821158 لاتین هسانی جالبی"
دارد. آیا این همبانی اتفاقی است؟

۳-واژه‌ی «گوره با واژه‌های انگلیسی 07۸7 و آلمانی 0۸ همسانی چشمگیری دارد. آیا
این واژه‌ها همریشه‌اند؟ ۰ 010۴

۴-گفته شده است که واژه‌ی فارسی «شیرین» از واژه‌ی فارسی «شیر» درست شده است (همانگونه

که «سنگین» از «سنگه» آمده) ولی هسانی نسبی آن با واژه‌های سانسکریت 5۷۸008 و انگلیسی

7 و آلمانی 83[ کنجکاری‌انگیز است. ۳

۵- واژه‌ی فارسی «فرار؛ با واژه‌های انگلیسی ۳1.88 و آلمانی ۳1.137 و دانمارکی اس
78 (از واجریشه‌ی هند و اروپایی ۶181716" - 837 :۳01۳0379) همسانی‌های جالبی
دارد ولی هیچکدام از پسگشت‌های در دسترس من اشاره‌ای همریشه‌های ایرانی و سانسکریت این
واژه‌ها نمی‌کنند. آیا میان این واژه‌ها خویشی وجود دارد؟
[pdf page 49]
۰ / ریشه‌های هندو اروپایی زبان فارسی
```


## [2026-09-06T02:17:41.367Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /\\[pdf page 445\\]/{print NR\": \"; print}' incoming/ARY/ARY_pages.txt | head -60"
}
```


### [2026-09-06T02:17:43.040Z] TOOL RESULT

```
445: 
[pdf page 445]
۶ | گور (به چم "قبر" *آرامگاه»)
کردی (80157ل). ما6 اد زاین
افغانی (پشتو) (//۸۳0/1۸2): 00 لهستانی (۳0.157):. ری نی
سانسکریت (84(55777): ان روسی (7551۸ا#): زاین
گرتیک (007/0): ۸ بقف28 چک (ل280): 1105
اپسلندی کهن (۱۵۵۷ ۸1۸۷ ظ شک صام). برهمی (80/78۸4۵۷4): 108
35 ,605 اسلرا کی (51.01/۸4): 108
ساکسونی کهن ((54300 صاه): تفع آلبانی (00مالمقلم: دراد
آلمانی کهن (/08804 6#ابز صام): قطان
آلمانی (08801۸00): زا دی پسگشت‌ها رد۲۳
انگلیسی گهن (0ل8ل2001 صام: جفون رم
۱ انگلیسی (بلولاه/(8): دیاب 7 (08۸78) نب
دانمارکی (0۸(/3[7): دیدن 3 ,293 ناه
سوئدی (8108215/7): هه 1 (63۸78) :00/70/5
نروژی (/0/0777501۸: لیات نی 8 (8۸15ع) +37
هلندی (7ع007). ان برهان قاطع : 1۸۵۰
اسلاوی کهن (۲10شا5 17ع#نابل) صا۵):
یادداشت:
چم پیشین این واژه در زبان‌های ژرمنی: کندن» چال کردن,
َ اوستایی (/4۲/8574). 811 ,۸083۸ افغانی (پشتو) (/۸۳017۸۸۷).
پارسی باستان (امفای۲۶۴ صا0):. هلاقتاهج 7 ما۸6 17۷
پهلری (7ماتزمه): 03 سانسکریت (54(/5877): 7105۸
اوستی (0558716): 8 ,01108 آرمنی (۷ل۸7248(/[4): 1
کردی (82015/7ن۸): ای پونانی (0765/0): 0585
بلوچی (7677انل8۸): انا لاتین (۸700ل: هانا۲ت3تا۸ ,قاتا
```


## [2026-09-06T02:17:50.274Z] TOOL CALL #24: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py ARY:446 --image 2>&1 | tail -40"
}
```


### [2026-09-06T02:17:56.653Z] TOOL RESULT

```
(no exact page map; using offset -1 -> pdf page 445; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ARY/0446.png
REF: ARY:446  PDF: data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf page 445  OCR-lang: fas+eng

۶ | گور(به چم "قبر" *آرامگاه»)
کردی (82157): ,ناهن زد ری نم
افغانی (پشتو) (۸7017۸(/1): 00 لهستانی (۳0[/./5/7): زرزای دی
سانسکریت (77ل54(/57): 011-7 روسی (/5540): رزوی دم
گرتیک (ع007/71): 6۸۸ ,78۸3 چکه (7ل)25): 1110
ایسلندی کهن (/012۸۷1۸۸/ی5 صا0): برهمی (/]80785۸1): ۱۱۱
50 ,0305 اسلوا کی (5].014): 1110
ساکسونی کهن ((54340 ص0): همع آلبانی (0۷ما#لمقلم: دای
آلمانی کهن (/05704۸0 7/0 صا0): هی
آلمانی (/(0880/۸): زا ی پسگشت‌ها شید درد
۱ انگلیسی کهن (#اعلاه20 صام: جفوه 8 وم
انگلیسی (5لا8۸0): 63 7 (08۸8) نا
1 دانمارکی (0۸(7/5[7): دید 3 ,293 8۸0
سوئدی (7ل815015): ید 1 (63۸۷8) :0/7075
نروژی (077501۸/): یات ی 8 (68۸78) وا ادن
هلندی (77ع076): دا ان برهان قاطع + ۱۸۵۰
اسلاوی کهن (۷12شا5 7ل#6ناتل) صام):
بادداشت:
جم پیشین این وازه در زبان‌های ژرمنی: کندن» چال کردن.
۱ اوستایی (488744): آ151 ,۸0573 افغانی (پشتو) (1/ل7۸ا70م:
پارسی باستان (مفای۲8۲ ص01). هلادتاهج 5 017۷۸6
پهلری (1ماتلمه): 005 سانسکریت (54(58477): 010577۸
اوستی (08587/۳): 5 ,611085 ارمنی (۸7۸/5۷1491): 1
کردی (771317): 011 یرنانی (072): 0085
بلوچی (8۸72777): | لاتین (7120ما): ۰شآت۲۲تتاخ۸ ,قتقاتا۸
```


## [2026-09-06T02:17:58.704Z] TOOL CALL #25: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ARY/0446.png"
}
```


### [2026-09-06T02:17:59.320Z] TOOL RESULT

```

```


## [2026-09-06T02:17:59.295Z] INPUT

[Image: original 1500x2400, displayed at 1250x2000. Multiply coordinates by 1.20 to map to original image.]


## [2026-09-06T02:18:18.798Z] TOOL CALL #26: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py | grep -n \"vision\" ; grep -n \"vision\" tools/ref_page.py | head"
}
```


### [2026-09-06T02:18:18.888Z] TOOL RESULT

```
10:matching PDF page to PNG (for reading with a vision model), OCRs it with tesseract in
18:save that transcription as <printed page>.vision.txt next to the .txt; from then on this
10:matching PDF page to PNG (for reading with a vision model), OCRs it with tesseract in
18:save that transcription as <printed page>.vision.txt next to the .txt; from then on this
83:    vision = base + ".vision.txt"   # a transcription made by reading the PNG; preferred over OCR
86:    if os.path.exists(vision):
88:        print(open(vision, encoding="utf-8").read())
```


## [2026-09-06T02:18:19.796Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v3 gerow/gereftan pages\"; grep -n \"\\[pdf page 59[0-9]\\]\\|\\[pdf page 60[0-9]\\]\" incoming/BQT/BQT_v3_pages.txt | head -30"
}
```


### [2026-09-06T02:18:19.858Z] TOOL RESULT

```
=== BQT v3 gerow/gereftan pages
43223:[pdf page 590]
43276:[pdf page 591]
43362:[pdf page 592]
43432:[pdf page 593]
43484:[pdf page 594]
43551:[pdf page 595]
43640:[pdf page 596]
43702:[pdf page 597]
43778:[pdf page 598]
43874:[pdf page 599]
43972:[pdf page 600]
44055:[pdf page 601]
44144:[pdf page 602]
44244:[pdf page 603]
44341:[pdf page 604]
44423:[pdf page 605]
44499:[pdf page 606]
44597:[pdf page 607]
44682:[pdf page 608]
44743:[pdf page 609]
```


## [2026-09-06T02:18:23.811Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '43362,43432p' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T02:18:23.866Z] TOOL RESULT

```
[pdf page 592]
۱۷۹7

گرست « بفتح اول و ابی و سکون
ثالث و ‎sigh‏ بمعنی سیاه همست باشد وبعریی
طافع گویند ۱ - و بزبان علمی هند فرو بردن
لقمه و امثال ‎OT‏ باشد و عربان ‎ab‏ خوانند.

گرسقن ۴ - بکر اول وانی :مخف
کربستن است که کربه کردن باشد .

گر ستودن ۴ بفتح‌اول وئالی‌بروزن
تیغرودن » بمعنی ‎OS‏ است وآن ترازو مانندی
است که بستها و تنگهای ‎gh‏ را بدان سنجند .

گرستون ۴ © بفتح اول وئالی بروزن
شف ق کون + بمعت ی گرستودن است که ‎methods‏
‏وبه‌عنی کیل ‎Ulan‏ بزر که همآمده است‌ومعرب

گرسنه چشم - بت ول تا ناه
از ‎Ste‏ و ممسك ‎ath‏ - و مردم ‎ad‏ وکدا را
‎e‏ میگویند ۵ - وکنابه از مردمی‌هم هست که
از قحط وغلا برآمده پاشتد .

گرسنه چشمان کنعان - کنایه
از برادران ‎Gey‏ علیه‌اللام است .

گرسیان - با بای ونون وحرکت
غیرمملوم « نوعی‌ازسنگه باشد ‎OT;‏ درهتدوستان
‎re‏ میرسد ودر صثمت کیمیا ‎ale‏ 1

‎Sg F‏ = بتادرستا مود
بروزن بخنی‌پز » نام برادر افراسیاب است ؛ وبا
کاف تازی هم بنظ رآمده است .

‏آن قرسطون ‎Fath‏

‏گر شاسب ۲ = با تین قطمدلر بروزن

‎٩‏ باز رسید مت ما داد قدح بدست ما

‏کر دهدی بدست نو شاد و خوشی و کرمتی -

‏مولوی بلخی رومی «جهانگیری» وبنابرین بیت با اول وسوم مفتوح وسکون دوم است -

‏۴ مخففگرستن: رك: لفت ‎EB‏ ۴ - ظ. مصحف «کرستون*.رثك: کرستون.

‏۴ = کرستون (.م.) < فرسطون. رك: فرسطون ‎ .‏ 8 - وحاصل مصدر(اسم‌ععنی)آن
«گرسته چشمی » است . ۲ = ‎jp‏ ؛ در اوستا ‎Keresavazda‏ ( از دو جزء :
2 لاغر واندك , ۷۵28 فوت » پابداری ) ( بمعنی استقامت و بابداری کم دارندء ) تم
برادر افراسیاب است « پورداود . يشتها ج ۱ ص ‎VV‏ ۷ - در شاهنامه ‎pelt Syl‏
پرميخوريم ‎ :‏ ۱- در برخی ازسخ شاهنامةٌ فردوسی( ‎GLEE‏ بخ ج ۱ ص ‎۱۰٩‏ ح ) اسرعنوان
( ناخت کردن منوچهر برسپاهء‌تور ) داستان بمیدان آمدن شیروی پپلوان نورانی و برزم طلبیدن
گرشاسب جهان پهلوان ابرانی ؛ در شمن می‌وشش یبت آعده »که درتیجه شیروی کشته شدم.
۲ - از گرشاسب پسر زو ( زاب ) ودهمین پادشاه پیشدادی که نه سال پادشاهی کرد , باد ‎wat‏
‎a lela: (‏ ج ۱ ص ۷۸۲ ) . موضوع کرشاسب ‎LU‏ اسدی طوسی همان گرشاسب دختی‌است.
کرشاسب در اوستا صورت 16676585۳2 و درسانسکریت 168528۷8 آمده مر کب از دوجزه:
ارل 66۳658 بیمنیلاغر , جزء دوم 2508 همان اسب فارسی است [ دو ۸ در اوستا تبدیل به 4
شده ] مجموعاً بیمنی ‎tah‏ اسب لاغر ,کی که اسبش لاغر است. بنابرین لفة اصح کرشاسب

‏بقیه در مفعةً ۱۷۹۹

‏گرسته - نم اول وکسر دوم و چپارم ( در ‎bend)‏ مر‌کزی ) و نیز جضم اول و دوم و
فتح چهارم» و در شعر بضرورت ‎pie‏ اول و سکون دوم وفتح سوم و چپارم » پهلوی 80758 .
‎gursakih‏ «استو ‎acy‏ تهرانی ‎glam . Vishta SLO, gushna‏ «کری» ‎aS‏
‏ک ی که محتاج‌بخوردن غذاست ‎SGT.‏ احساس احتیاج بخورد نکند :

‏ب سگرسنه خفت وکس ندانت که کیست بس جان بلب آمدکه بروکس نگرست.

‎2h ۳۵ IT >
[pdf page 593]
```


## [2026-09-06T02:18:34.215Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"گرفتن\\|گرو -\\|گرو ‎\\|گروگان\" incoming/BQT/BQT_v3_pages.txt | sed -n '1,40p'"
}
```


### [2026-09-06T02:18:34.309Z] TOOL RESULT

```
3773:شدن -وسخت گرفتن - وقوی کردانیدن - وبلند
5611:‏و تحمل نمودن وقرارگرفتن باشد.
5617:صبر کردن و تحمل فمودن - وفرار وآرام گرفتن
5990:تندی و غلبه کردن وبستم و زور چیزی گرفتن
8117:ملك او بهیچ لمبگرفتند .
10860:طر فگرفتن - کنایه از ‎cle‏
13875:است - و بمعنی خشم گرفتن و قهر کردن ‎As‏
14521:ستجر قوت گرفتند و خراسان را بتصرف آوردند
16830:کوه. « منتهی‌الارب » . ‎٩‏ - (مر) ‎sled‏ وفجات ( از باب فتح وسمع ( ناگاه گرفتن
17077:‎fra_‏ در - ‎_fra[keresta‏ 610072 ]۲۵] , در : فراخور , فرارسی‌دن » فرا گرفتن آمده
19405:ماه ‎ster‏ میگرفتند . بیرونی درآثار الباقیه ص ‎۲۱٩‏ گوید : « روز نوزدهم ( ازماه فروردین) »
21654:فریفته شدن ومفروزگردیدن۷ - وآرام گرفتن-
26282:ازدو هزار ‎IT‏ و گوسفند فرارمیگرفتندوجانوران
27034:‎Oat‏ (پوندمصدری) . رشیدی (ص۱۲۱ و۱۲4) «کالیدن»آورده بمعنی‌دورشدن وکنار گرفتن.
29195:بمعنی‌خراش وخراشیدن ‎Fark‏ - وبمعنی گرفتن
36791:‏نگداری زبورهای ‎Jee‏ وعلگرفتن از ‎WT‏ سازند .
37537:‏۴ - ۶ و مرغانگردانیدنگرفتند و خابه وکواژء و آنچه ‎LY‏ روزمپر کان است‌ملواد
38564:پااوهمراه بودند وازهردکانی‌بکدرم سیم‌میگرفتند
40439:‏طلمی بته‌الد وهیچکس ‎ond‏ بررگرفتن ‎OT‏
41134:‏در رشیدی« کالیدن» بمعنی دور شدن و کناره گرفتن آمده .
42754:۴ رك : رشیدی . ‎٩‏ - ازمسدر «گرفتن».  ‎٩‏ - ازکرد (کردیدن)ج- | (یوند
43453:‎GT .‏ هر دو بنظر آمده است که ماه گرفتن
43463:۵ - مصدر مرخم »و سوم شخص مفرد ماضی از «گرفتن» . رك : کرفتن » گرفته .
43517:۱ - اسم مقمول از «گرفتن» . رك :گرفتن » گرفت . ۴ - رك: گرفته زدن .
43529:» گرفتار - بکراول و دوم » پهلوی 48۲ - ]871 از : کرف (گرفتن ) + تار(یسوند
43533:‎oo S sles!) 888702200 , grab _‏ گرفتن ) » ‎ta)‏ اوستابی - ‎wgeriwnaiti . grab‏
43594:اعرج» سر کوییرا کوبند که بجهت گرفتن قلعه‌از
43964:6 گرو - پکتر اول و فتح دوم » ارمنی ع 878۷ ( رهن ) ۰ پهلوی 872۷ ] نوشته
44153:از گرفتن باشد ۴ - و با تحتانی مجهول, بمعنی
44205:‎. ‏رك :گرفتن‎ F
44831:بزبان ‎٩‏ - و بدندان گرفتن را هم میگویدخواه
45416:منم فرمود درآسال درختان بارنگرفتند. بعرض
49408:(گرفتن )+-و ( عطف )+ دار ( داشتن ) ‎By‏ : دار وگیر - ‎V‏ - در فپرست ولفچنین
49409:نام‌نيامده . ظ . مصحف «گروی > (هم.) است . ۸ - از :کی (گرفتن )-» ‎tye)‏
```


## [2026-09-06T02:18:42.150Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '43520,43545p' incoming/BQT/BQT_v3_pages.txt; echo \"#### PAGE TAG for 43529\"; awk 'NR<=43540 && /\\[pdf page/{p=$0; n=NR} END{}' incoming/BQT/BQT_v3_pages.txt; grep -n \"\\[pdf page\" incoming/BQT/BQT_v3_pages.txt | awk -F: '$1<43530' | tail -2; echo \"==== 43955-43985\"; sed -n '43955,43985p' incoming/BQT/BQT_v3_pages.txt; grep -n \"\\[pdf page\" incoming/BQT/BQT_v3_pages.txt | awk -F: '$1<43964' | tail -2"
}
```


### [2026-09-06T02:18:44.178Z] TOOL RESULT

```
‎oS?‏ مزن در ‎de‏ افکنی کرفته ‎BSS by‏ زنی .
نظام یکنجوی «کنجینه ۱۳۱*.
6 - باين معنی«ک رکن» و «ک رکن» است . ۲ - پارسی باستان_ 2۳802 ۷.
اوستابی - ۷۵/۵۲2 ‎(eS)‏ پهلوی ‎BUTE‏ » حندی‌باستان - ۷۳۵ (ک رک ). ارمنی ‎gail‏
‏کاشانی ۷۵۲ ۰ ۷۵۲۵ ۰ ۷6۲8 , مازسرانی ۷۷۵۲۵ . کردی ۷۵۲8»افنابی 108 , استی08880.
‎.biraegh] birdgh‏ »4 . است ۱۱4] پلوچی ‎gurk , gvark‏ . بودفا ۷۷۵۲۵ ۰ فنویی
ه«اسشق ‎Are‏ ؛ جانوری است وحشی ازتیر# کربه‌سانان از راستة گوشتخواران که در روسیه
و تروژ و امریکای شمالی فراوان است و در ايران نیز هست ۰ جانور خطرداکی است وبچاریایان
وانان نیز بهتگام گرسنگی حمله ميکند.
» گرفتار - بکراول و دوم » پهلوی 48۲ - ]871 از : کرف (گرفتن ) + تار(یسوند
ساختن ‎Cie‏ مقعولی ) « تیبر ‎CAR EE‏ ورك : اسم مصدر بقلم ‎oe ot NG‏ ۱۰۹-۱۶۵ ؛محبوی:
زلدالی- اسیر » برده - مبتلای رنج و محنت - مشفول.
‎AO‏ - یک اول و دوم و فتح چهارم ( درلبجة مررکزی ) » ازرمشة پارسی‌باستان
‎oo S sles!) 888702200 , grab _‏ گرفتن ) » ‎ta)‏ اوستابی - ‎wgeriwnaiti . grab‏
پهلوی ‎.garaftan‏ حندی باستان - ‎girtin 65,5. grabh‏ . بلرچی ‎giragh , girag‏ .
‎Vaghréigh_am JC‏ «اسشق ‎٩۰۵‏ > ,4 : هوبشمان ‎Cel‏ ؛ ‎griftam syle ji‏ «تاوادیا
۱ ۷ *؛ بدست آوردن » دربافت کردن 6 قبض کردن » اخذ کردن ؛ ستاندن- حبس کردن -
تسغی رکردن -

می‌خوابنددفن کنند
همه گوسفند ان
بتدریج‌بمیر ندوا گر
دم‌اورا ‎gles‏ که

os

#### PAGE TAG for 43529
43432:[pdf page 593]
43484:[pdf page 594]
==== 43955-43985

‏یکی دیگری زن برین هم شان

‏کروغ از کناه است پرسر کشان .

‏ولی اين کلمه در فهرست ولف ‎ols‏ و ظ ۰ مصحف « دروغ » است .
۳- از : کرو(ه.م.) ‎OWT‏ ( پوند اصاف وسبت ). در اوراق‌انری پهلوی8۳۷870

‏(رهن ) ( 0.83 ,1 ‎Henning, A list of Middle Persian... , 505 , IX,‏ (
6 گرو - پکتر اول و فتح دوم » ارمنی ع 878۷ ( رهن ) ۰ پهلوی 872۷ ] نوشته

‏میشود "8۳6101 ] ( رهن ) , از پارسی باستان - 82208 ‎OWS.‏ فارسی ازهمین ماده‌است:
اققالی ع 872۷ (رهن ) . « هوبشمان سس ‎٩۷‏ * ؛ پول یا مال باچیزی دیگر که قرض گیرنده
تزد قرش دهنده ( با امیر وپادشاه مغلوب و زیر دست نزد پادشاه ‎ME‏ و زبردست) گذارد ‎calle‏

‏از ادلی قرض ( با اجرای تکالیف ) مسترد شود . رهن - مرهون . ۲
۱ ( برهان قاطع ۳۳۸ )
[pdf page 600]
۱۳

فارسی بروزن خروشان, آلت تناسل را گویندا -
‎Ks‏ اولوفتح ثانی» کر وکردتی رآبعنی‌مهون
- وبمعنی بنده وصد هم پنظرآمده است ۴ .

گر و گر « بفتح اول و اف فارسی
بروژن ‎HF‏ یکی از نامهای‌خدای‌تمالی است‌ومعنی
‎OT‏ مرادبخش باشد .

گره ۴ ‎ee‏ اول و ثانی بر وزن
‎ag‏ جماعت مردم را کوبند و بعربی قوم
خوانند .
43778:[pdf page 598]
43874:[pdf page 599]
```


## [2026-09-06T02:19:04.060Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 593 594 595 598 599 600; do echo \"--- pdf $n:\"; awk -v n=$n 'f&&c<6{print;c++} $0==\"[pdf page \"n\"]\"{f=1;c=0}' incoming/BQT/BQT_v3_pages.txt | head -6; done"
}
```


### [2026-09-06T02:19:05.549Z] TOOL RESULT

```
--- pdf 593:
--- pdf 594:
--- pdf 595:
--- pdf 598:
--- pdf 599:
--- pdf 600:
```


## [2026-09-06T02:19:07.683Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '43432,43440p;43484,43492p;43874,43882p' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T02:19:07.754Z] TOOL RESULT

```
[pdf page 593]
کرشاسف ‎wae‏
‏طهماسب ؛ تلویکی از اجداد رستم زال ات واو | سرعست » رستنيی باشد خود روی شبیه باسفناج
پر اترد باشدکه از نباثر جمشید است - و نام | که در غلعزارها و کنارهای جوی آب روید ودر
‎ee ae ees‏ عوض اسفناج درآش وشله کنند .
بادشاه شد وهمان در حیات جنگه اس فد
: وهمان در حیات پدر ‎ND‏ قت * ‎Ge‏ اول و ثا ‘
کشته شد .# ۱ ‎x‏ بکس 7 بی وسکون
گرشاسف ۱ -با فا . بروزن و معنی فا وفوقانی » بمنی‌طعنه است که زدن نیزه‌باشدب
[pdf page 594]
—Avay—

کاری کرد نکه شمه لرزان بگوشآید ‎a.‏
‎of‏ ۱ © بروزن فرشته ۰ بمعنی‌طعنه
است که زدن لیزه - و گفتن‌سخنانبطریق‌سرزش
باشد ۴ - و بمعنی تاوان و غرامت هم هست -
وبمعنیلاف و ‎GIS‏ لیز آمده‌است- واسیر و ‎HIS‏
‏را لیز کویند؟ - ومردم خنیس وبخیل ومسك
[pdf page 599]
کر می‌خونابه .
گر می خو نابه = کتابه از ‎he‏
‏وشتاب وتصجیل درکربه باشد .

گر نج - بضم اول ‎Ty‏ ثانی وسکون
نون و جیم » بممنی چین وشکنج باشد- و کنج
‎Dyers,‏ خانه را نیز گوبند- وبر نج‌خوردنی
را ه مکفته‌اند ۱ که بعربی ارز خوانند ؛ و بابن
```


## [2026-09-06T02:19:17.862Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"پذیرفتن\\|پذیر ‎\\|پذیرا\" BQT_v1_pages.txt | head -20"
}
```


### [2026-09-06T02:19:17.922Z] TOOL RESULT

```
5280:ابچد درمقابل فاباشده و * گرفتن » وه پذیرفتن » و «نهفتن » و« آلفتن »
5282:و« بگیر » واز پذیرفتن «میپذیرد » و«بپذیر» آمده است, ونهفتن وآلفتن
24239:۱ - از: پدید ار (پسوند). ۲ - رك:پذیرفتن.
24252:کنندهرا کومند,چه پذیرابی بمعلنی فرمان‌برداری
24261:ماضی پذیرفتن است عنی فول کرد؟ 3
24275:۴ - رك : پذیرفتن.
26592:کردن زصبحت پذیرفتن وصیحت شنیدن وقبول
```


## [2026-09-06T02:19:20.664Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24230,24285p' BQT_v1_pages.txt; echo \"#### page tags\"; grep -n \"\\[pdf page\" BQT_v1_pages.txt | awk -F: '$1<24240' | tail -2"
}
```


### [2026-09-06T02:19:22.211Z] TOOL RESULT

```
۱ - پهلوی 04ت +08 «نولدکه . کارنامه »٩۵‏ (قس : درود) «اسشق ۲۸۸ : «( علی
فریب) بامن (بوصر مشکان) خالی کرد و گفت : بدرءدیادای دوست نك که بروز کار دراز بیکجا
بودمييم و ازنکدیگر آزار ندارم .» «بیهقی ۵۳*. ؟ ‏ مخقف پدراندر. ۳ - از
شواهدی که بدواز درآ نها آحدهه چنن مستفاد میشود که آن جای عرغعان شکاری وشاید شنک
دد ان درمحلی مرتفع باکوهی باشد. « لفت نامه » وركث: پتواز.
فهناه:طاوناه وباآنام0ظ «ناتی۱۹۱۹* :
این نج درختند که مي‌نارد بار بید ویده وسرو وسفیدار وچنار.«لفت نامه».
۵ عطات باذ چوباران دل موافق خوید اهب آش و جان مخالفان پده باد .
شهید بلخی. «لفت امه» ورك: بد.
۱ - از: پدید ار (پسوند). ۲ - رك:پذیرفتن.
» بدید -بفتح اول. بهلوی 4 0۵ د«یرند که .کرنامه 44۰ ؛ فر اوستانااه 00۳02
«اسشق ۲۷۸۹ , نبرک پهلوی آنرا 16 084 نوشنه. «یب رکه 0۷»؛ آشکار. سامان,پر قتتکاد ۱ سباعان بالفکنیدوبرای
قرشت زده ؛ بستی فبول کننده و فرماببردار
وهقر و معترفی باشد .
فد فلقی» بروزن دد جردن » بمعنی‌فبول
کردن و اعتراف نمودن باشد ۴ .
فد لته » بروزن دل برده: بمعنی‌افرار
واعتراف کرده و قبول نموده باشد ۴ .
فیرح بی +زن وزیس ۰ قبول کننده را
کوینن - وامرباینممنی‌هم‌هست,منی‌قبولکن ۴ .
پدیر | ۴ بر وزن اصیر اه روان‌شو نده
و پیش رونده - و سخن‌شنونده وفرمانبرداروقبول
کنندهرا کومند,چه پذیرابی بمعلنی فرمان‌برداری
باشد - و بمعنی هیولی نیز بنظر آمده است که
در برابر صورت است ۵ - و نضیر مفبول حم
هست که‌فبول کرده شده‌باشد.- وبمعئی پیشواز(۱)
واستقبال هم گفته‌اود ۹
پذپرش ۱ ه تم اول و کر رابع
)۱ چش : پشوا.
وسکون شین نقطه دار پسعنی قبول و فرمان -
برداری باشد .
ماضی پذیرفتن است عنی فول کرد؟ 3
پذبر فتکار با کاف بالف کشیده
و برای قرشت زده » بمعنی فرمان بردار - وقبول
کننده - و مقر و معثرف باشدب و سردار ورش .
سفید قوم را نیز کوبند۷ .
پل یر م4 - مضدر است بممتی فرمان
برداری کردن و قبول نمودن باشد .
پفیر قت4 - بمعنی پنرفته است که
قبول سودن بائده .#۷
بد بر ٩۵‏ بر وزن کییره» ببشواز )۱
و استقبال کسی .با چیزی‌بافرمانی باشد۷۹-وبمعنی
قبولکردن و فرمان برداری - و پی شکسی‌رفتن.
و اعر کی قبو لکننده - و راهگنر هم آمده
است ,
۴ - رك : پذیرفتن.
خوانند ومادت‌خوانند . » « دانثنامه۷۳ *.
۷۲ - ر: بذرتکار .
(بکرفتن) « اسنو۷۵۰ .
- پپلوی
۳ بب رکه ۱۸۰و رك: اسشق ٩۲۹۱‏ .
٩‏ - « چون خفل بزرکه علی بابات آعددر بای فارسی
بر - فتح اول و سکون ثانی» هحروف
است که بال و پر باشد و عربان رش‌خوانند ۷
واز سر کتف نا سرانگشتانرانیز گوشد - وروشنی
وشماع و پرتو را هم کنته‌اند؟ - و دامن و کناره
#### page tags
```


## [2026-09-06T02:19:35.771Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD grb\"; grep -n \"γrβ\\|grb\\|ɣrβ\" SOD_pages.txt | head -20; echo \"=== SOD 167 / 237 entry numbers\"; grep -n \"^ *167 \\|^ *237 \\| 167 \\| 237 \" SOD_pages.txt | grep -i \"grb\\|γr\\|seize\\|grasp\" | head"
}
```


### [2026-09-06T02:19:36.480Z] TOOL RESULT

```
=== SOD grb
3195:              YrP-                   *grba-
15710:4196 yr'yk^ B                             J^^                   yarP, yorJ3 ? (yrb-, >yrp-) ©<*grb; <*grab; OP
25202:                                                                   Aiam.psgrb* =*Yrvw
=== SOD 167 / 237 entry numbers
```


## [2026-09-06T02:19:36.765Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FRS غژم\"; grep -n \"غژم\\|غزم\" FRS_pages.txt FRS.txt | head -20; echo \"=== MON\"; grep -n \"غژم\\|غزم\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -20"
}
```


### [2026-09-06T02:19:36.845Z] TOOL RESULT

```
=== FRS غژم
FRS.txt:7257:تر است زمین ز دیدگان* من چون پی بنهم همی فرو لغزم | 
FRS.txt:8017:۳ گونهة سیاهی چشمست غژم او هم بر مثال م‌دهك * چشم ازو تکس 
FRS.txt:8034:استخوان انگور بود که درهیان غژم بود. ؟ -ل : بهرامی آشییه کند انگوررا ۰ 
FRS.txt:8114:+ - ن : غرس تندی باشد و خشم ۰ چ : غرس و غزم [ صحیح : غرم ] خشم باشد » 
FRS.txt:10569:چو مشك بویا لیکش نافه بوده زغژم۸ 
FRS.txt:13107:ب کون سیاهی چشم است غژم او هم بر مثال مد مك چشم از او تکس ۱ ] 
FRS.txt:13463:غژم 
FRS_pages.txt:4494:                                      ‫غزمی‬
FRS_pages.txt:7881:   ‫چون پی بنهم همی فرو لغزم |‬                   ‫تر است زمین ز دیدگان* من‬
FRS_pages.txt:8686:‫هم برمثال م‌دهك * چشم ازو تکس‬               ‫غژم او‬     ‫‪ ۳‬گونهة سیاهی چشمست‬
FRS_pages.txt:8708: ‫؟ ‪-‬ل ‪ :‬بهرامی آشییه کند انگوررا ‪۰‬‬          ‫استخوان انگور بود که درهیان غژم بود‪.‬‬
FRS_pages.txt:8795:  ‫‪ - +‬ن ‪ :‬غرس تندی باشد و خشم ‪ ۰‬چ ‪ :‬غرس و غزم [ صحیح ‪ :‬غرم ] خشم باشد »‬
FRS_pages.txt:11456:                                    ‫چو مشك بویا لیکش نافه بوده زغژم‪۸‬‬
FRS_pages.txt:14488:                         ‫همب م‬                    ‫ب کون سیاهی چشماست غژم او‬
FRS_pages.txt:14960:                                      ‫غژم‬
=== MON
MON_part2.txt:1708:غژّم: «زه [- غزمه - غجمه | (.) (گیا.) هر 
MON_part2.txt:1714:غزم : 7020 [ + - غزم] (.) خشم» قهر» غضصب 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:1708:غژّم: «زه [- غزمه - غجمه | (.) (گیا.) هر 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:1714:غزم : 7020 [ + - غزم] (.) خشم» قهر» غضصب
```


## [2026-09-06T02:19:44.020Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON_part2 1695-1730\"; sed -n '1695,1730p' MON_part2.txt; echo \"=== FRS 13455-13475\"; sed -n '13455,13478p' FRS.txt; echo \"=== FRS 8100-8125\"; sed -n '8100,8125p' FRS.txt"
}
```


### [2026-09-06T02:19:44.105Z] TOOL RESULT

```
=== MON_part2 1695-1730
غذب: «۶ه(.) دانٌ انگوری که از خوشه 
وت بر هر مد اج وی 
حبهٌ انگور. هستة انگور» تکس انگور. 
غزْغز: رنه (اصت.) صدای کفش و مانند 
ان. 

غژک: ,۵22( [- جک - جک - 
فیچک - قیچکد] () (س..) سازی است از 
مطلقات ذوات الاوتار و آن دارای کاسه‌ای 
است و بر سطح آن پوست کشند و به کمانه 
در عمل آورند و بر روی آن ده وتر (سیم) 
نک ت: 

غژّم: «زه [- غزمه - غجمه | (.) (گیا.) هر 
دانة میوهٌ انگور که به خوشه متصل است؛ 
یک عدد از میوةٌ انگور به خوشه متصل 
است؛ یک حبه انگور؛ غذمه: حبه» گله 
غجمه. 

غزم : 7020 [ + - غزم] (.) خشم» قهر» غضصب 
غعژنده: (۵-)2۵2-۸0۵ (افا.) نشسته 7 
رونده» خر ند ۵. رو نده. 

غعزیدن.: 7۵2-0 | - فا یدن» قس. 
خزیدن] (مصل.) نشسته راه رفتن چنانکه 
کودکان و مردم شل و زمینگیر روند) 
خزیدن. برهم نشستن دو چیز؛ بهم چسبیدن. 
(مص‌م.) طبقه طبقه روی هم گذاشتن 
عزیده: (۵-)۸2-102( (امف.) نشسته به راه 
رفته. . برهم دسسته ) بهم تچسییل ۵. 

عشات: ۶۱ عساة» ف. غسا] (.) 
غوزه خرماء خرمای ار سیده. 

غساق: ۱۸۹)۹(۲ [معر . قس. غساکك] (ص.) 
سرد و گندیده. (!.) خون و چرکی که از بدن 
=== FRS 13455-13475
معنی و رونق باشد » شهید گفت : 
دعوی کنی که شاعر دهرم ولك نیست 
در شعر تو نه حکمت و نه لذات و نه حم ) 
رود کی کوید : 
چراهمی نچمم تا کند چراتن من که نیز تانچمم کار من نگیرد حم 
شا ک رکوید : 
چه جویی آن ادبی کان ادب ندارد نام 
چه وین از سخلی کان سجن ندارد حم 
غژم 
هیبت باشد » رودکی گفت : 
شیرغو م آوردو جست ازجای‌خویش وامد این خر گوش را الفغده بیش 


1 


سرمایی بود که بامداد بر کشته نشیند سبید چونآبی تنك فسرده تازش 

صقیم است ؛ فرالاوی گفت : 

چون‌موردبودسب زگهی‌موی من‌همه ‏ درد کهبرنشست ب رآن‌مویسبز بشم 
۱ - نقط درچ بجای بت قبل ۲ - فقط در چ و حاشبان ۳ -ن ( درحاشه) 

يك بار + چم رونق و نظام بود ( با پیت رودکی مذکور در متن ) و بار دیگر « چم 
=== FRS 8100-8125
عرس 


خشم و تندی | باشد رودکی گفت : 
گرنه بد بختمی مرا که فکند بیکی جاف جاف زود غرس 
او مُ مش شیر سنندد ب من‌نتاوم؟ بروونشسته مکس ۷ ] 


۷ 3 ۸ 
داس و دلوس 
اتباع است نی سفله چون تار و مار و خراب و ساب و تسیر ان قاش 
و قماش [ کذا؟ ]بود [ منحيك کوید : 
- این ست فقط در چ هست  .‏ ۲ _ س : کیوس کز بود بعنی نا راست ۰ چ : 
کیوس کز باشد » لن : کیوصوریب باشد - ۳ اس : اصافه دارد : 7 و ابله 
+ - ن : غرس تندی باشد و خشم ۰ چ : غرس و غزم [ صحیح : غرم ] خشم باشد » 
س این لت را نداد ه - در چ که فقط آن بر این مشتمل است : نسندد » 
٩‏ - از مصدر تأویدن سنی طاقت آوردن ۰ ۷- این ست را چ اضانه دارد . 


۸ - تن : داس و و داوس اتباع است چون که وکوی ۱ کدا ؟ و تیاه و سامت و تار 
و مار و قاش و قماش [ کذا از هر چه بود مرده‌را ۰ چ : داس و داوس چون تباه 


و تست است معنیش ۶اش و قماش است .
```


## [2026-09-06T02:20:04.214Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"granta-\\|gram-\\|gr.m.nt\" BRT.txt | head -20"
}
```


### [2026-09-06T02:20:04.309Z] TOOL RESULT

```
10495:•  j.  gram-  V.  'erglimmen,  Grimm  hegen'. ;     "  I"»  Gegens.  lu  manueSfi-,
10497:yr  manS  bara  gramfntam  "weg  schaff  i  nur  mit  Praev.     Praes.  30  (Kaus.)  yxra- den  Anschlag  derer,  die  (uns)  grimm  sind"   iaya-.
10503:•  j.  gramant-  Adj.,  PPA.:  s.  gram-.
13863:Zum  V.  'bar-.  —  ■)  Ob  richtig  überliefert? J  10  hat  •bariHtö.  Jedenfalls  ist  didh'  gram- matisch entsprechend  dem  hubiritöHx..  10.  11»
16898:ks  ava%a  dafnqm  ..  vl.barai  V,  2.  42;  —  , aat  "hwa  (näml.  haonam) . .  trurrfa  viivanca  , vXbann  Y.  10.  11;  —  mit  Abi.  des  woher? und  Dat  des  wohin?:  yahmäl  iahmäiat (sd.)  nalmanqm  vätB  ahrS  baoi\im  vi- baraiti..  V.S.80.  3)  '(Daevisches)^'^ weg-, fortschaffen':  vT nS  tbiyvatqm  (bal^bl^ vi  manS  bara  gramintam  "schaff  fort  unsrer Feinde  Feindschaften,  fort  der  ergrimmten Anschlag"  Y.5. 28.
```


## [2026-09-06T02:20:05.270Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD ghrebh\"; grep -n -A12 \"^ghrebh\\|^ghrem\\|^gheu-ro\\|^ghou-ro\" AHD_watkins1985.txt | head -60"
}
```


### [2026-09-06T02:20:05.382Z] TOOL RESULT

```
=== AHD ghrebh
```


## [2026-09-06T02:20:10.944Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ghrebh\\|ghrem\\|gher∂-\\|ghou-ro\" AHD_watkins1985.txt | head -20; echo \"=== grab/grasp/grim/grumble in AHD\"; grep -n \"^grab\\|^grasp\\|^grim\\b\\|grumble\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T02:20:11.011Z] TOOL RESULT

```
526:TRANSFUSE. II. Extended form *gheus-. 1. Germanic zero-grade form *gus- in: a. suffixed form *gustiz in Old Norse gustr, a cold blast of wind: cusT!; b. Icelandic gusa, to gush, perhaps akin to Middle English gushen, to gush: GUSH. 2. Germanic suffixed o-grade form *gausjan in Old Norse geysa, to gush: GEYSER. III. Suffixed form *gheu-ti- in Latin fatilis, “(of a vessel) easily emptied, leaky,” hence untrustworthy, useless: FUTILE. IV. Basic form *gheu- in Greek khein, to pour: CHOANA, CHYLE, (CHYME); CHOANOCYTE, ECCHYMOSIS, PARENCHYMA. [Pok. gheu- 447.] ghéu-. To yawn, gape. Compare ghai-. 1. Germanic suffixed form g6-ma- in Old English goma, palate, jaw: GuM?, 2. Variant form *ghau- in Greek khaos, chasm, empty space, chaos: CHAOS, GAS. [Pok. ghéu- 449.] gheu(e)-. To call, invoke. Suffixed zero-grade form *ghu-to-, “the invoked,” god, in Germanic *gudam, god, in: a. Old English god, god: Gop; b. Germanic *gud-igaz, possessed by a god, in Old English gydig, gidig, possessed, insane: GIDDY. [Pok. ghau- 413.] gh6. Behind, after. Slavic *za in Russian za, by, to: SASTRUGA. [Pok. 26 451.] ghos-ti-. Stranger, guest, host; properly “someone with whom one has reciprocal duties of hospitality.” 1. Basic form *ghos-ti- in: a. Germanic *gastiz in Old Norse gestr, guest: GUEST; b. Latin hostis, enemy (< stranger): HOST?, (HOSTILE). 2. Compound “ghos-pot-, *ghos-po(d)-, “guest-master,” one who symbolizes the relationship of reciprocal obligation (*pot-, master; see poti-), in Latin hospes (stem hospit-), host, guest, stranger: (HOSPICE), (HOSPITAL), (HOSPITALITY), HOST!, (HOSTAGE), (HOSTEL), (HOSTLER). See also xenos. [Pok. ghosti-s 453.] ghow-é-. To honor, revere, worship. 1. Germanic *gaw6n in Old Norse gd, to heed: GAWK. 2. Basic form *ghow-é- in Latin favére, to favor, be favorable: FAVOR, (FAVOR- ITE). [Pok. ghou(é)- 453.] ghré-. To grow, become green. Contracted from “ghreo-. 1. O-grade form “ghré- in Germanic *grd(w)an in Old English gréwan, to grow: GROW. 2. Suffixed o-grade form *ghro-nyo- in Germanic *grénjaz, green, in Old English gréne, green: GREEN. 3. Suffixed zero-grade form *“ghro-so- in Germanic *grasam, grass, in Old English grees, grass: GRASS. [Pok. ghré- 454.] ghrebh-'. To seize, reach. 1. Zero-grade form *ghrbh- in Sanskrit grbhndati, grhndati, he seizes: SATYAGRAHA. 2. Parallel (imitative) Germanic creations with base *grab-, *grap- in: a. Middle English graspen, to grasp: GRASP; b. Middle Dutch and Middle Low German grab- ben, to seize: GRAB. [Pok. 1. ghrebh- 455.] ghrebh-?. To dig, bury, scratch. 1. O-grade form “ghrobh- in: a. Germanic *graban in (i) Old English grafan, to dig, engrave, scratch, carve: GRAVE3; (EN- GRAVE) (ii) Old High German graban, to dig: GRABEN (iii) Old French graver, to engrave: GRAVURE; b. Germanic *grabam in Old English grzf, trench, grave: GRAVE}. 2. Germanic *grub(byan (with secondary ablaut) in Old English *grybban (> Middle English grubben), to dig: GRUB. 3. Germanic *gr6b6 in Middle Dutch groeve, ditch: GROOVE. 4. Perhaps Germanic *greub- in Low German greven, fibrous refuse of tallow: GREAVES. [Pok. 2. ghrebh- 455.] ghredh-. To walk, go. Suffixed zero-grade form ghrdh-yo- in: a. Latin gradi (past participle gressus), to walk, go: GRESSORIAL; AGGRESS, CONGRESS, DEGRESSION, DI- GRESS, EGRESS, INGRESS, PLANTIGRADE, PROGRESS, RE- GRESS, RETROGRESS, TRANSGRESS; b. Latin gradus (< deverbative *grad-u-), step, stage, degree, rank: GRADE; CENTIGRADE, DEGRADE, DEGREE, RETROGRADE. [Pok. ghredh- 456.] ghréi-. To rub. A derivative of gher-4. 1. Germanic *gris-, to frighten (< “to grate on the mind”), in Old English grislic, terrifying: GRISLY. 2. Germanic *grim-, smear, in Middle Dutch grime, grime, akin to the source of Middle English grime, grime: GRIME. 3. Extended form *ghris-
528:in Greek khriein, to anoint: CHRISM, CHRIST, CHRISTEN, (CHRISTIAN); (CHRISTMAS). [Pok. ghréi- 457.] ghreib-. To grip. 1. Germanic *grip- in Old English gripe, grasp, and gripa, handful: crip!. 2. Germanic *gripan in: a. Old English gripan, to grasp: GRIPE; b. Old French gripper, to seize: GRIPPE. 3. Suffixed o-grade form *ghroib-eyo- in Germanic *graipjan in Old English grd- pian, to feel for, grope: GROPE. [Pok. ghreib- 457.] ghrem-. Angry. 1. Germanic *grimmaz in: a. Old English grim(m), fierce, severe: GRIM; b. Old French grimace, a grimace: GRIMACE. 2. Germanic *grum- in Middle Dutch grommen, to mutter angrily, probably akin to Middle English grummen, to grumble: GRUMBLE. 3. Suffixed o-grade form *ghrom-o- in Russian grom, thunder: Po- crom. [Pok. 2. ghrem- 458.] ghrendh-. To grind. 1. Germanic “grindan in Old Eng- lish grindan, to grind: GRIND. 2. Germanic *grinst-, a grinding, in Old English grist, the action of grinding: GRisT. 3. Latin frénum (< frendere, to grind), horse’s bit (on which its teeth grind), bridle: FRENULUM, FRENUM; REFRAIN). 4, Variant form *ghrend- is sometimes but improbably regarded as the root of Greek khondros, granule, groats, hence cartilage: CHONDRO-; HYPOCHON- DRIA, MITOCHONDRION. [Pok. ghren- 459.] ghréu-. To rub, grind. Extension of gher-4. 1. Germanic *greut- in Old English gréot, sand, gravel: GRIT. 2. Ger- manic *grut- in Old English grotan, pieces of hulled grain, groats: GROATS. 3. Germanic “grit- in: a. Old English griit, coarse meal: GRouT; b. Old French gruel, porridge: GRUEL. 4, Germanic *grautaz, coarse, thick (< “coarsely ground”), in: a. Old English gréat, coarse, thick, bulky, large: GREAT; b. Middle Dutch groot, thick: Groat. 5. Germanic *griiw-, to recoil from (< “to be offended, be grated on by”), in Middle Dutch griiwen, to abhor, akin to Middle English grue, horrible: GRUESOME. 6. Variant form *ghrow- in Greek khrés, skin (< “rough surface” ?), hence flesh, complexion, color: RHODOCHRO- SITE. 7. Suffixed variant form *ghré-mn in Greek khréma, skin, complexion, color (semantic development as in 6. above): CHROMA, CHROMATIC, CHROMATO-, CHROME, -CHROME, (CHROMIUM), CHROMO-; ACHRO- Matic. 8. Probably Celtic *graw- in Old French grave, greve, coarse sand, gravel: GRAVEL. 9. Probably Latin *grau-, to touch, graze, in con-gruere, to agree (com-, together; see kom): CONGRUENT. [Pok. 2. ghréu- 460.] ghwer-. Wild beast. 1. Suffixed form *ghwer-o- in Latin ferus, wild: FERAL, FIERCE. 2. Compound *ghwero-okv-, “of wild aspect” (*-ak-, “-looking”; see okw-), in Latin feréx (stem feréc-), fierce: FEROCIOUS. 3. Length- ened-grade form *ghwér- in Greek thér, wild beast: TREACLE; THEROPOD. [Pok. ghuér- 493.] gladh-. Smooth. Suffixed form “gladh-ro- in Latin gla- ber, smooth, bald: GABRO, (GLABELLA), GLABROUS. gleubh-. To cut, cleave. 1. Germanic *k/euban in Old English cléofan, to split, cleave: CLEAVE!. 2. Germanic *klub-, a splitting, in: a. Old English clufu, clove (of garlic): CLOVE*; b. Middle Dutch clove, a cleft: KLOOF. 3. Germanic *k/aubri- in: a. Old Norse kleyfr, easy to split, perhaps akin to Middle English cliver, “expert in seizing,” skillful: CLEVER; b. Old Norse lofi, a cleft, akin to English clevi, “cleft instrument,” clevis: CLEVIS. 4. Zero-grade form *glubh- in Greek gluphein, to carve: GLYPH, GLYPTIC; ANAGLYPH, HIEROGLYPHIC. 5. Suffixed zero-grade form *glubh-md- in Latin glima, husk of grain: GLUME. [Pok. gleubh- 401.] glégh-. Thorn, point. 1. Suffixed form *glégh-i- in Greek glokhis, barb of an arrow: GLOCHIDIUM. 2. Suffixed form *glégh-ya in Greek gléssa, glétta, tongue, hence also language: GLOSS2, (GLOSSARY), GLOTTIS; BUGLOSS, GLOS- SOLALIA, ISOGLOSS, POLYGLOT, PROGLOTTID. [Pok. glégh- 402.] gno-. To know. Contracted from *gnoo-. 1. Variant form *gné- in Germanic *kné(w)- in Old English cndwan, to know: KNOW. 2. Zero-grade form *gno- in: a. Germanic
1459:ENERVATE (s)neeu- ENFILADE gWhi- ENFLEURAGE bhel-3 ENFORCE bhergh-2 ENGAGE wadh-! ENGAGE wadh-! ENGENDER gene- ENGINE gene- ENGRAVE ghrebh-2 ENGROSS gW¥res- ENHANCE al-3 ENIGMA ai-2 ENJOIN yeug- ENJOY gau-
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1567:GREAT ghréu- GREAVES ghrebh-2 GREEDY gher-5 GREEN ghré- GREET gher-2 GREGARIOUS ger-1 GRENADE gre-no- GRESSORIAL ghredh- GREYHOUND gher-3 GRID kert- GRIDDLE kert- GRIDIRON kert- GRIEF gWera-2 GRIEVE gWere-2 GRIM ghrem- GRIMACE ghrem- GRIME ghréi- GRIND ghrendh- Grip! ghreib- GRIPE ghreib- GRIPPE ghreib- GRISAILLE gher-3 GRISEOUS gher-3 GRISETTE gher-3 GRISLY ghréi- GRISON gher-3 GRisT ghrendh- GRIT ghréu- GRIZZLE gher-3 GROAT ghréu- GROATS ghréu- GROCER gWres- GROOVE ghrebh-2 GROPE ghreib- GROSCHEN gWres- GROSS gWres- GROSSULARITE ger-2 GROSZ gWres-
1570:GRUB ghrebh-2 GRUDGE gru- GRUEL ghréu- GRUESOME ghréu- GRUFF kreup- GRUMBLE ghrem- GRUNION gru- GRUNT gru-
2111:POETIC kWej-2 POGROM apo-, ghrem- -POIESIS kwej-2 -POIETIC kwej-2 POIGNANT peuk- POIKILOTHERM peig-1 POILU pilo-
2215:SATISFY sa- SATRAP pase, tké- SATURATE sa- SATYAGRAHA es-, ghrebh-1 SAUCE sal-1 SAUERBRATEN bhreu-2, stiro- SAUERKRAUT siro- SAUTE sel-4 SAVANT sep-1 SAVE!  sol-
=== grab/grasp/grim/grumble in AHD
528:in Greek khriein, to anoint: CHRISM, CHRIST, CHRISTEN, (CHRISTIAN); (CHRISTMAS). [Pok. ghréi- 457.] ghreib-. To grip. 1. Germanic *grip- in Old English gripe, grasp, and gripa, handful: crip!. 2. Germanic *gripan in: a. Old English gripan, to grasp: GRIPE; b. Old French gripper, to seize: GRIPPE. 3. Suffixed o-grade form *ghroib-eyo- in Germanic *graipjan in Old English grd- pian, to feel for, grope: GROPE. [Pok. ghreib- 457.] ghrem-. Angry. 1. Germanic *grimmaz in: a. Old English grim(m), fierce, severe: GRIM; b. Old French grimace, a grimace: GRIMACE. 2. Germanic *grum- in Middle Dutch grommen, to mutter angrily, probably akin to Middle English grummen, to grumble: GRUMBLE. 3. Suffixed o-grade form *ghrom-o- in Russian grom, thunder: Po- crom. [Pok. 2. ghrem- 458.] ghrendh-. To grind. 1. Germanic “grindan in Old Eng- lish grindan, to grind: GRIND. 2. Germanic *grinst-, a grinding, in Old English grist, the action of grinding: GRisT. 3. Latin frénum (< frendere, to grind), horse’s bit (on which its teeth grind), bridle: FRENULUM, FRENUM; REFRAIN). 4, Variant form *ghrend- is sometimes but improbably regarded as the root of Greek khondros, granule, groats, hence cartilage: CHONDRO-; HYPOCHON- DRIA, MITOCHONDRION. [Pok. ghren- 459.] ghréu-. To rub, grind. Extension of gher-4. 1. Germanic *greut- in Old English gréot, sand, gravel: GRIT. 2. Ger- manic *grut- in Old English grotan, pieces of hulled grain, groats: GROATS. 3. Germanic “grit- in: a. Old English griit, coarse meal: GRouT; b. Old French gruel, porridge: GRUEL. 4, Germanic *grautaz, coarse, thick (< “coarsely ground”), in: a. Old English gréat, coarse, thick, bulky, large: GREAT; b. Middle Dutch groot, thick: Groat. 5. Germanic *griiw-, to recoil from (< “to be offended, be grated on by”), in Middle Dutch griiwen, to abhor, akin to Middle English grue, horrible: GRUESOME. 6. Variant form *ghrow- in Greek khrés, skin (< “rough surface” ?), hence flesh, complexion, color: RHODOCHRO- SITE. 7. Suffixed variant form *ghré-mn in Greek khréma, skin, complexion, color (semantic development as in 6. above): CHROMA, CHROMATIC, CHROMATO-, CHROME, -CHROME, (CHROMIUM), CHROMO-; ACHRO- Matic. 8. Probably Celtic *graw- in Old French grave, greve, coarse sand, gravel: GRAVEL. 9. Probably Latin *grau-, to touch, graze, in con-gruere, to agree (com-, together; see kom): CONGRUENT. [Pok. 2. ghréu- 460.] ghwer-. Wild beast. 1. Suffixed form *ghwer-o- in Latin ferus, wild: FERAL, FIERCE. 2. Compound *ghwero-okv-, “of wild aspect” (*-ak-, “-looking”; see okw-), in Latin feréx (stem feréc-), fierce: FEROCIOUS. 3. Length- ened-grade form *ghwér- in Greek thér, wild beast: TREACLE; THEROPOD. [Pok. ghuér- 493.] gladh-. Smooth. Suffixed form “gladh-ro- in Latin gla- ber, smooth, bald: GABRO, (GLABELLA), GLABROUS. gleubh-. To cut, cleave. 1. Germanic *k/euban in Old English cléofan, to split, cleave: CLEAVE!. 2. Germanic *klub-, a splitting, in: a. Old English clufu, clove (of garlic): CLOVE*; b. Middle Dutch clove, a cleft: KLOOF. 3. Germanic *k/aubri- in: a. Old Norse kleyfr, easy to split, perhaps akin to Middle English cliver, “expert in seizing,” skillful: CLEVER; b. Old Norse lofi, a cleft, akin to English clevi, “cleft instrument,” clevis: CLEVIS. 4. Zero-grade form *glubh- in Greek gluphein, to carve: GLYPH, GLYPTIC; ANAGLYPH, HIEROGLYPHIC. 5. Suffixed zero-grade form *glubh-md- in Latin glima, husk of grain: GLUME. [Pok. gleubh- 401.] glégh-. Thorn, point. 1. Suffixed form *glégh-i- in Greek glokhis, barb of an arrow: GLOCHIDIUM. 2. Suffixed form *glégh-ya in Greek gléssa, glétta, tongue, hence also language: GLOSS2, (GLOSSARY), GLOTTIS; BUGLOSS, GLOS- SOLALIA, ISOGLOSS, POLYGLOT, PROGLOTTID. [Pok. glégh- 402.] gno-. To know. Contracted from *gnoo-. 1. Variant form *gné- in Germanic *kné(w)- in Old English cndwan, to know: KNOW. 2. Zero-grade form *gno- in: a. Germanic
```


## [2026-09-06T02:20:11.658Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>10380 && NR<10520 && /^ *[0-9]{3} *$|^ *5[0-9][0-9]/' BRT.txt | head -20; echo \"---\"; sed -n '10490,10512p' BRT.txt"
}
```


### [2026-09-06T02:20:13.441Z] TOOL RESULT

```
527  _,!£^'  ^
---
bewahren  die  Wörter  und  Sätze  des  M."  :     ^l  ^^4:7^; j,7k.  ^Isl'iof  v^S.  i  IS
i-9-3b.  _  4)  Pü.;  öiän  ^ahmak  kac  a/ir.iiiA  döSailat
Zum  V.  grai->).—  ai.  vgl.  ^t-M-  f.  'GrifP.  — .  i^  iat/  h<nä..i4  ^.''sfjUh  x'ähiad pa  drS'Jhi. Pü.!    an  i  dräi   a/ar  rawisiiiA  isle pa  mänsr;,
da»  Wort  fehlt  also;  aber  So.:  dli-gkam  .•  j.  grivä-  f.  'Nacken'  UZW.  (fofflTScher u/if/iapravraim  yävai  gfüio 'd mäniAravJttyä.  Wesen":  atfZBraAe [s,A.)  "i-aj-a  (LS.)  V.J.7. —  '>  S  ^^S.  37.  I      ii.gräia-i.;mp.l^ä.)grhai,Tt^.sar7va'iiä^t\',
.  j.  rran«.  Adj.  PPfP.  s.  V--         |    °3%Tjg'',;rSöS''b»r' b""''-
•  j.  gram-  V.  'erglimmen,  Grimm  hegen'. ;     "  I"»  Gegens.  lu  manueSfi-,
Praes.  1  grama-.  —  PPiT.  ^rnw/a-"',       |  »j.  yzrid-V. 'fliessen,  wallen',  vom  Wasser;
yr  manS  bara  gramfntam  "weg  schaff  i  nur  mit  Praev.     Praes.  30  (Kaus.)  yxra- den  Anschlag  derer,  die  (uns)  grimm  sind"   iaya-.
\,f).2Z;    —  mi^rS  graiits  upa.tbHtd  YL  !      niit  ä  Kaus.  'aufwallen  lassen':  hg srayS ro.'iS,  19,  39,  43J  23,  98,  \o();  —  ahurahe  ^•rii'iaydli  Yt.Ä3i. (näml.  niii-rahe)  grantahe'^l.i0.i>ii,^%-,\      mit  i'f  Kaus.   'auseinander,  tiberwallen —  varäsahe  ..  grantahe  Yt. /^ig.  lassen':  Jt3  zrayo  viyzr.ioayeiti  Yt.Ä3i,
mp.  ä-granä-lum  Dk./.  6.  7  (West:  'the  most !      -prod- :  izar-  (sd.)  =  gr.  il^l-io  :  ai.  fi-par.d;
horrid');   vgl.  np.  taram  'Grimm',  ahd.  g>-am\      %  48-
■      ■        —       ■  'nmän^fatil.?,ii.:k<,,!am  \ ,  j.  yjar-  V.  'iÜessen'.     Praes.  4  fzära-, "  """""'  t^i   7  (Jnt)  yiari.yiar-,  2oyiaurv;  30  (Kaus.)
ie;    IF.    /.    70, r,  47-
•  j.  gramant-  Adj.,  PPA.:  s.  gram-.
•  j.  grava-"  m.  'Rohrstock,  Stock':  graom jytis^ii. .  nava.pixim  (sd.)  adrinjayHl  aom
•/z-lraya-.  —  Absol.  'ylär^m.
'fliessen,  strömen':  kma  x^  .  .  afam yiäram  (3PKA.)"  aiwiyiannn  (sd.)  Vt. S.^2.  a)  Kaus.  'fliessen  lassen,  pro- fundere': p^r.msbyö  (sd.)  paiti  yl(irayat.by5
1  paurva.nalmäX  (sd.)  ahe  gravahe  V.  ,  Yt  /j.  2.         A)  Int  'hin-  und  herfliessen, €f.  14.  '  auf  und  ab  wallen':  ti  kist.uiti  (sd.)  yzan.-
Ei.f  —  mp.'(Pü.)  grm<,  np.  7rtrr'.  —  ')  Oder   yiaroutJs    (IP.    als    NP.)    * antari.ar»o)m ■,^0«.  (S  268.  37);  ob  zum  V.  grab-t  .  -^rt/«,^^^  V.J.  19.
j.  gravaira  Y.  p.  26  r  s.  \grai-.  ,      mit  «yi/  'fliessen,  (dünn)flüssig  sein',  von
•  j.gravä'ratav- m.EN.  eines  Gläubigen:  <i"  frischen  Milch,  im  Gegensatz  zur fradatMaraAe-tlus  asaone"A^S  Fr.,  SoYmi  ^"^^^^^  Mi'ch:  aipi.yzaurvatam  .  . des  Gr.  .."  Yty.i23.  payaakqm  ¥.5,52.
Eig.  Bed.?    VgL  JusTi  NB.  507.  1      nüt  irnft  'herzufliessen':  s.  Absol.
dby  Google
```


## [2026-09-06T02:20:35.980Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 233 303; do echo \"===== leaf $L\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' SOD_pages.txt | head -30; done"
}
```


### [2026-09-06T02:20:37.558Z] TOOL RESULT

```
===== leaf 233
                                                                GtObuy
       yraw ?
       GcOmoan                                                  TSP 2.265; trans, pret. YryytSyr-x VJ 1401
       TSP 3.246, Frag. 3.36
                                                           4201 xarltc
                                                                yr'ytk ©pp.
                                                                       B'                                      0x>
 4191 yr'ws   B                           tiftf«3±f
                                                                bought
      yrus ?                                                    TSP 2.231
      short, little
       BSTBL, Dhu. 35, 335; Benv. Notesii 217, Yr'ws            C2, 54 R16
         Yryws, Dhy. 86, 100, 107, 145; Intox. 19
                                                          4202 Y^ywcyk05 B                                   J'&kJ*
 4192 yr'y S                                   JU~<jf
      yar(e), yirc ©<*griya\ Yaghn. Yirek\ Khot.                material, corporal
                                                                yriweik
        griha; Gk. g/ia -*yr}yk(>\ Yryk                         TSP 5.123; BSTBL, Dhu. 379, 380, Dhy. 88; Frag.
      mud, clay                                                   Len. 7 V3
      MDii p57.7; Bailey. BSOAS 15.540; Asica. 6
                                                          4203 yr'ywCh) B, S          (J>> y^> j->)o* 'a*^- <->y-
 4193 Yr}yc(h) B                :                   ju>        yriw ©<Av. griva-, Khwar. Yryw; Parth. gryyw
      xaric ©<*xriti =*xryc, yr'yt-                              ©f. body
                                                               self,  n. ob. -y(h) =*yryw, CWRH
      purchasc
      CMS 275, 1002                                             GMS 207-, VJ; TSP; BSTBL, SCE; Gcrsh. apud.
                                                                  Sund. MSP p45
 4194 yHych 'ync B                        (-Ji>- Oj^jj
      xaric-cne                                           4204 yrp B, S                     (jy* ^^     j>)&S<Jl~*
      prostitute                                                yarf ©<*Ya(r)fu <*farYu <*faruwu <*faruwam
===== leaf 303
                                                                                                                     236
  nftt

      Hen. JRAS 1944, 143.26                                          niyund (nywnt-) ©<*nigunda ©impf.
 5888 nftt M                                                            nyYywnt\ inf. nYywnty
          naft =»nPtc>(hXn|3ty(y)                                     (to)dress, (r<?)put on(clothes)
          naphtha                                                     VJ 1361, 93; TSP 3.244; SCE 30-, GMS 186;
          Hen. BSOAS 11, 69.38; GMS 76                                  Gharib. AI 4250; AVS 78, 113
 5889 ny^kh B                                                    5900 ny'wnt'k B                                    jW,,;
       ©niyaSak ^ny^                                                  niyunde (ny'wnl'y) *=>nywnty
                                                                      blanket
          prayer
          BSTBL, Intox. 36                            ijt^*^*         VJ 1129,1367
 5890 nyMin B ^ ny'm                                            5901 ny'wnt'y =* ny'wnt'k
 5891 nyW C -» ny*'                                             5902 ny'ws- B, M, 5 yj^ ^)d^^            O^j^      < 0-^
 5892 nyW M                                          U?Ur fUj

          niya6a (ny'dO ©*ni-gadaka ©f. n.                            niyos (nyws-, nyyws) ©<*ni~gausa-; Parth.
          prayer, request S
                                                                        ngws-, MP nyws-     ©impf. nyY(y)ws ^nywst-,
          Hen. Tales. 472.1; GMS 676; STSC 134.29; STii
            2.15; BSTi 140; BSTii: C2 gloss. +fiar- "to              0^)hear, (glisten
                                                                        nywsdV-
                                                                     GMS 676, nx>w$-, STii 1.29.30; STi; Sund.
        pray", "to ask"
                                                                       AoFviii 1981 p216; AVS 128
 5893 ny'm B, M, C                                 uU><f&*
      niyam (ny*m) ©<*ni-gama ©ob. -y                           5903 ny'ws'kt M, S                     ^l^oif*^
      time, moment                                                   niyosakt (nys'kt) ©ob. pl.; pi. -ty ^nyws'k
                                                                     Auditors
```


## [2026-09-06T02:20:49.614Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"yrp-\\|Yrp-\\|yrft\\|yrβ\" SOD_pages.txt | head -20; echo \"=== leaf 234\"; awk 'BEGIN{RS=\"\\f\"} NR==234' SOD_pages.txt | head -40"
}
```


### [2026-09-06T02:20:51.323Z] TOOL RESULT

```
11632:2737 prStp'y- S                                              2749 pryrp- B                              o^b^o*^
14701:3865 fr»yrp- B                                                        (ro)spoil
14775: 3890 fryrp-      B                              u*b<uJui*»                 framandar ©ob. pi. ~ty ^prm'n^r
14776:      frayarP ©^fra-garba        ©impf. fr'Yrp-                             governor, tutor
14777:        =>fr»yrp-, pryrp-                                                   STi 83.4; GMS 1135
15709:     BSTBL, Vim. 153; CMS 976; S W, C2 n pl78             4205 yrp-    B, M, S jj)    ^^ i&J'Sj* < j-*^ tj^\*
15710:4196 yr'yk^ B                             J^^                   yarP, yorJ3 ? (yrb-, >yrp-) ©<*grb; <*grab; OP
15717:       yYsyfitk, "mud-milky" Vim. 25                      4206 yrb-    C => yrp-
15812:      yarfi-smarak                                                      4254 yrftyct M, C                             U>>- J^
15813:                                                                             yarft-est (yrftyst)
15819:4242 yrpzng'n M                                                         4255 yrftyst     C =» yrftyct
22726:6615 pcyrp- B, S                       tf*j>M*o*J*fj>             GMS 56, 509; BBB; C2 p54.29; AVS 130
25480:7562 pt>yYrp- B                       ^Ju^Li                     7578 ptp>y8- =» ptbd-
25759:7661 pty^ B, C, S                                       Uw   7672 ptyrp- B                   j^.-H iJ^^t id>J^>Sj>
26913:8044 ptyyrp- =* pt>yyrP-
36469:    11261 zy^r-     B =» zy>yr-, zyyr-                          11274 zyrp-     B                   jAiJljtfrJ%<o>jL*
=== leaf 234
 yrb'q

           2.1068; Yrfi'kw, Hen. Tales. 480.1; MSP b 130;     4224 yrpV        S =* yrPy
           YrjPku YrVqu TSP 8.24; Tales. 467.60; BBB          4225 yrpV B                        «wf 7 ij>€ 7 <o^j
           f90; STii 4.42, 10.5; STi 6.8; C2 gloss.                yarPaw, yarP(a)u ©n. adv. prcs. inf.
 4211 yrb'q      C =» yrP>k                                        knowledge, conscience, conscicnt
 4212 yrb'qywny C                                 oSU^UlTT          VJ 381, 391, 393; TSP 5.108, Yrfi'wk Yrp>y; C2
      yarPak-yone
      wisely                                                          gloss. prYrft'w
                                                              4226 yrp'y B                                  ^L^lfT.Ub
         GMS 1115; STi 43.15                                       yarpe ©in compd. =»yrbyq
                                                                   knowing
 4213 yrp'kstr B                          yJiU<>lfT
      yarpakstar (yrb'qstr) ^yrP'k, yrb>qystr                      nw Yrp>yy VJ 393; 'xs-Yrby "knowing conflicts"
      wiser                                                          C2, 31R 21
         TSP 12.68, 69; STi 43.16; GMS 1288, 1306             4227 yrp'y ywV'k/'y B                          j^>t
 4214 yrb'qstr      C =* yrP'kstr                                  yarfi-xware -^yw'^y
                                                                   eating much
 4215 yrp'kt'nyOi) B                '            /j-^tjjh          SCE 290
      yarPak-tani/-tanya
      wisdom
                                                              4228 yrp'y ywVy =* yw'r'y
         TSP 2.690, 7.124, 15.10; GMS 1074a                   4229 yrp'yn'k B                            jT ^ J,li ,Ub
4216 yrp'ky' B, M, S          (jy^ ^^ jj)^\fl<jjh                  yarPene (yrpyyny(y)) ©pi. -r
                                                                   wise, understandable
     yarPakya (yrfrqy*, yrP*ky\ yrp'ky'h)
                                                                   TSP 2.1184, 11.10; BSTBL, Dhu. 209; GMS 890,
       -»mndyrp,ky>
     wisdom                                                          1157; CH, 1990 E4
         GMS 1136, 1266; BBB 636; TSP 2.1098, 14.36,          4230 yrpcy      B                           ^p J,G <(^jb
           10.12, 16.41; BSTBL, Dhy. 360; xrP'ky\ STii 7-
           6; Sogdica. 18-, MSP; Sund. AoFviii 1981, 24            knowablc(w/taf one must know)
                                                                   yarPci
           R3, 4 pl89-, C2 gloss.-, ob. -<y, W-Lii: Gropp.         BSTBL, Vim. 36, 178, GMS 1009
           p38; Yrpykty. Frag. Len, 67.3, Yrp'ky'y, BBB       4231 yrbd'r-       C                                   ^b
           627, 637; YrP*ky\ BSTBL, Intox. 9                       yarP5ar       (yrPt'r-) ©trans, pret. st. =4yrP-,
4217 yrb'qy'      C -* yrP>ky>
4218 yrp'ky'h =» yr^ky*                                            0ST^i)k4n2o.4w & etc.
4219 yrp'ky^h S                                         ^fT
     yarPakyak                                                4232 yrph -» yrP>
```


## [2026-09-06T02:21:02.145Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15700,15716p' SOD_pages.txt; echo \"=== leaf 304 (printed ~237)\"; awk 'BEGIN{RS=\"\\f\"} NR==304' SOD_pages.txt | head -45"
}
```


### [2026-09-06T02:21:03.808Z] TOOL RESULT

```
                                                                  Sund. MSP p45
 4194 yHych 'ync B                        (-Ji>- Oj^jj
      xaric-cne                                           4204 yrp B, S                     (jy* ^^     j>)&S<Jl~*
      prostitute                                                yarf ©<*Ya(r)fu <*farYu <*faruwu <*faruwam
      SCE 356, -wA                                                <OP paruvam ©adv. -w, -y, -h *=»yrf, yrPy
                                                                much, many
4195 yr>yck> B                                ^3J
     xaricik, xaricak ? ~»xrycyq                                EGSii 161; GMS 485, 526; S W, BSOAS 1983, 49
     prostitute
     BSTBL, Vim. 153; CMS 976; S W, C2 n pl78             4205 yrp-    B, M, S jj)    ^^ i&J'Sj* < j-*^ tj^\*
4196 yr'yk^ B                             J^^                   yarP, yorJ3 ? (yrb-, >yrp-) ©<*grb; <*grab; OP
     yrik, yirck ©Khwar. Yr% Khot. griha; Yaghn.
                                                                  garbdya; Av. gdrobya-, Yaghn. Yiriv ^yrP't-
        Yirek ©ob. -yh; -y\ -y    =*yryk, yr*y                  (ro)know, GcOunderstand, (to)take
      mud, clay, muddy
                                                                GMS 485; AVS 108; YrSfi}<Yrfl-6y 2pl. impv.
     SCE 160; TSP 2.275; BSTBL, Vim. 0,28; Yryyk>                 TSP 2.676; Hen. Textes. YrSf
=== leaf 304 (printed ~237)
                                          M^.M^^.MMMM^MBMM^^HHlMH



     237

     5909 nynp'k S                                   j,jUJ>U       5923 nysn(h) B                           jUwo^UO^
          nayn- pak -^nynwp'c                                           niyasn ? =*prysnh                           nywst-
                                                                        mark, sigh
i
f
          baker
          MDiii                                                          TSP 5.25; BSTBL, Dhy. 50; pi. nYsnth, Frag. Len.
                                                                           24.1
     5910 nynwp'c M                                  j-jUj*
          naynupac =»nynp}k                                        5924 nysy>kr(w) S                           J^'^fji
I         baker
          Hen. Tales. 486.21
                                                                        naxsire
                                                                        wild goat
                                                                         MDii B-3, 10; nYsyr crm, naxsir- carm, MDiii
     5911 nyr^y- B                         ax-*^ *o>j^>
          ni-yray (nyr'y-) ©<*m-£ra; Av. gar-gd; IE
                                                                   5925 nysyr B, S                 j^^/y.^^^
            OcOpraise, (ro)honour                                       naxsir ©<*naxu-scrya ©ob. -y; pi. -t; ob. pi.
            SCE 542; BSTBL, Vim. l8lvDhy. 320, nYr*y>U                    -fypl24^nys'yrCh)
              Dhy. 319, pt. st.                                         wild beast
                                                                        TSP 3.142-, MDii B-19, 2, 5; Hen, Tales. 475, 5,
    5912 nyr*my      C = n+ yr'my =» n-, yrWk
                                                                          10.13; Gersh. UMV 92
    5913 nyr'n rwc S           (o^'-^j^)^^ \s*<jjj(iP
         niyran-rf3c (nyrn* rwc) ©Pahl. anagrdn; Av.               5926 nyw*y- B                          o±±£ iozJ'sJ*-
           anaYranam ~»nry                                              nixway ~*ny}y-, nxwJy-
         thirtieth day of the month                                     (ro)pound, 0o)crush
                                                                        GMS 477; TSP 3.175, 273, 288, 7.111, 19.22, 16;
           MDii A-16, 13; MDiii A-12, 3.1, 2, Bll, 1 pl24;                AVS 95
             CII 1990 n p67 G4-5
                                                                   5927 nywp- B                                  ub*"Ju
    5914 nyr'y- ■* nyr*y-
                                                                        nay(u)J3 ©nom. -y =>nyP-, nPy-
    5915 nyrf C = n +yrf -> n-, yrf                                     excellent, kind, fine
    5916 nyrn* rwc -» nyr'n rwc                                         BSTBL, Dhy. 153, 363; GMS 445
    5917 nyrs- -* ^yrs-                                            5928 nywp'w'k B                                ><^>^
    5918 nyrwps- S                  0-^»->^j> <ooiojjii                 nayuPawe
         nayrup/fs ©Av. nig2rdpta ©med, pass. st.                       excellence
```


## [2026-09-06T02:21:17.172Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"گوراب\\|گورابه\" incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt | head -10; echo \"=== gor entry\"; grep -n \"^6 گور\\|گور -\\|گور ‎\" incoming/BQT/BQT_v3_pages.txt | head -10"
}
```


### [2026-09-06T02:21:17.239Z] TOOL RESULT

```
incoming/BQT/BQT_v3_pages.txt:47882:گورابه * ‎gli‏ مجهول بر وزن
=== gor entry
9084:‎gine jot - ۱‏ عصارة میوه‌ها مانند انجیر و انگور - و نیز عصاره و جوهر منزها وتخمها
13207:و الگور ‎ay FI,‏ خصوماً .
34626:وثانی. نام نوعی از انگور ‎Le‏ است ‎٩۶‏ وآن در
48012:‏گور ‎pl‏ = بکر ‎eit‏ و فتح نون
```


## [2026-09-06T02:21:19.293Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%B1",
 "prompt": "Give the full Persian entries for گور: both 'grave/tomb' (gūr) and 'wild ass' (gōr). Quote the etymology sections verbatim, including any Middle Persian, Proto-Iranian reconstructions, and any mention of Sanskrit ghora- or of a Semitic/Aramaic loan."
}
```


### [2026-09-06T02:21:25.938Z] TOOL RESULT

```
# Persian گور Entries

## Etymology 1: Grave/Tomb (gōr/gur)

**Etymology:** "Inherited from Middle Persian [Book Pahlavi needed] (gpl /⁠gabr⁠/), [script needed] (gwbl /⁠gabr⁠/, 'hollow, cavity, womb'). Akin to Manichaean Middle Persian [script needed] (gbr /⁠gabr⁠/)."

**Definition:** 1) grave, tomb; 2) desert

---

## Etymology 2: Wild Ass (gōr/gur)

**Etymology:** "From Middle Persian gwl (gōr, 'onager, wild ass')"

**Definition:** 1) wild ass, onager; 2) (archaic) zebra

---

## Etymology 3: Alternative Form (gawr/gowr)

This entry provides "alternative form of گبر" without independent etymology beyond referencing the Dehkhoda Dictionary.

**Note:** The page contains no Sanskrit ghora- or Semitic/Aramaic loan references in the Persian sections. Aramaic etymology appears only in the Baluchi Etymology 6 entry for a different sense (Zoroastrian/non-Muslim person).
```


## [2026-09-06T02:21:38.574Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '47870,47900p' incoming/BQT/BQT_v3_pages.txt; echo \"#### page tag\"; grep -n \"\\[pdf page\" incoming/BQT/BQT_v3_pages.txt | awk -F: '$1<47882' | tail -1; echo \"==== 48005-48030\"; sed -n '48000,48030p' incoming/BQT/BQT_v3_pages.txt; grep -n \"\\[pdf page\" incoming/BQT/BQT_v3_pages.txt | awk -F: '$1<48012' | tail -1"
}
```


### [2026-09-06T02:21:40.166Z] TOOL RESULT

```
شوراب , نام شهری است که از مروشاه جان تا

با نجاچپارده روژ راء ‎col‏ -ومیدالیرا نیز گوبند
که بجهت اسب دوالی ساخته باشند - وگندی
که برسر قبرها میسازند ۴ - وچاقشور(۱) ‎SL‏
‏کوتاء یشمیرا یز کفته‌اند که بجهت دفع سرما
۳

درزیر موزه یوشند ومعرب‌آن جوراب است ۴ -
و زمین شوره زاری باشد در صحرا که ازدوربآب
مالد وآلرا سراب میگویند :

گورابه * ‎gli‏ مجهول بر وزن
رودابه :نام موضبی است که ‎Rese‏ پمران رستم
درآنجاست ‎ -‏ وگنبدی را لي زگوبند که بر سر
قبرها سازند .

گوراگور ۱ - منم کاف فارسی بر
وزن زوراژور » بمعتی زودازود است که مبالغه‌در

(۱) خم ۱ : چاخشور .

کورخان

زودی و ‎Gale‏ و تندی و تیزی باشد .

۰ ‏بتم اول و قح تالت‎ a WI
‏کوناء پشمی باشد که درزمستان‎ GL )۱( ‏چاقشور‎
‏در زیر کفش و موزء پوشند و معرب آن جورب‎
. ‏را هم کفته‌اند‎ wast ‏است - و کفش‎

#### page tag
47858:[pdf page 648]
==== 48005-48030

‏خوانند 9 .
گو ز ‎cole‏ - ماستی راگونند که از
شیر کورخر باشد - و ماستی هم هست که صحرا
شینان سازند وآن ماست چکیده‌ایست که شبر
خام درآن داخل کنند و برهم زنند وخورند.
گودن ۱ - منم ‎Jl‏ و ثانی مجعول

‏وقتح ثالث وسکون نون ۰ بممنی‌حلقه زدن مردم

‏باشد ؛ و ‎gare‏ کویند ‎inh‏ معتی ‎SN TF‏

‏گور ‎pl‏ = بکر ‎eit‏ و فتح نون
و فا و سکون سین بی‌تقطه ‎Sab,‏ تن وبدن
آدمی است .

‏گوره - ‎ttt Jo! ate‏ نامقبیله‌ایست
در ملك هندوستان .

‏گوری ‎eee‏ اول پر وزن حوری ۰
بمعنی‌عشرت ونشاط وبمثرت ونشاط ‎yy‏ باشد-
و دویدن پمانندگورخر را هم گفته‌اند 5

‎ce = IF‏ اول و ثانی و سکون زای

‏نقطه‌دار. مشفف گوزنست ک هکاو کوهی‌باشد ۸ -
و بسکون ثانی » کردکان راکویند و معرب آن
جوز است ‎٩‏ — و ‎gin‏ اول هم بععنی ‎ATS‏
‏وهم بادی راکویند که با صدا از ‎aT pce ly‏
— و بدرا نیز کفته‌اند 9۶ که در مقابل تيك است

47962:[pdf page 649]
```


## [2026-09-06T02:21:59.431Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%88",
 "prompt": "Quote verbatim the Persian entry for گرو (garow/gerow) 'pledge, collateral': its etymology (Middle Persian form, Old Iranian root), and definitions. Also any related terms such as گروگان."
}
```


## [2026-09-06T02:22:01.164Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%81%D8%AA%D9%86",
 "prompt": "Quote verbatim the Persian entry for گرفتن (gereftan) 'to take, seize': the full etymology section including Middle Persian, Proto-Iranian and Proto-Indo-European reconstructions and any cited scholars (Cheung, Hasandust, MacKenzie)."
}
```


### [2026-09-06T02:22:05.981Z] TOOL RESULT

```
# Persian Entry for گرو

**Etymology:** The word derives from Middle Persian [script needed] (glwb' /⁠graw⁠/), ultimately from Proto-Indo-European *gʰrebʰ-. It's cognate with Avestan and Sanskrit equivalents.

**Definitions:** The Persian noun گرو (giraw/gerov) means:
1. "mortgage; security; pawn"
2. "pledge"
3. "wager; bet"

**Related Term:** The entry notes a connection to گرفتن (gereftan, "to take"), though the specific term گروگان isn't mentioned in this particular dictionary entry.
```


### [2026-09-06T02:22:07.211Z] TOOL RESULT

```
# Etymology of Persian گرفتن (gereftan)

Based on the Wiktionary entry, here's the etymology:

The word is **inherited from Middle Persian** (/⁠griftan⁠/), which came from **Old Persian** (/⁠grab-⁠/, "to seize"), ultimately derived from **Proto-Indo-European** *gʰrebh₂- ("to grab, seize").

The entry traces related cognates across multiple Indo-European languages, including Central Kurdish girtin, Sanskrit gṛhṇāti, Russian grábitʹ, German greifen, and English grab.

**Note on sources:** The page cites Cheung's 2007 *Etymological Dictionary of the Iranian Verb* (pages 119-21) as the primary reference for this etymology. The Middle Persian and Old Persian forms are marked as requiring verification in the original text.
```


## [2026-09-06T02:22:11.993Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"GRAB\\|\\*grab\\|gr̥b\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T02:22:12.044Z] TOOL RESULT

```
8554:*grabH 119 
8589:*grabH ‘to grab, seize, take’ 
8618:120 *grabH 
8658:different continuations of *grabH in Chor., see Humbach 1973: 95. = Samadi: 234 
55324:*grabH (s.v.), *uat, *zanH?
```


## [2026-09-06T02:22:13.198Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/grab",
 "prompt": "Quote the etymology entries for 'grab' and, if shown, 'grasp' and 'grip' — the Middle Dutch/Middle Low German source, dates, and the PIE root given."
}
```


### [2026-09-06T02:22:27.775Z] TOOL RESULT

```
# Etymology Entries

## Grab (verb)
**Source and date:** "1580s, from Middle Dutch or Middle Low German _grabben_ "to grab"" 

**PIE root:** "_ghrebh-_ (1) 'to seize, reach'"

## Grasp
**Source and date:** The entry shows "mid-14c., 'to reach, grope, feel around,' possibly a metathesis of grapsen, from Old English *græpsan 'to touch, feel,' from Proto-Germanic *grap-, *grab-"

**Germanic connection:** It shares the same Proto-Germanic root (*grap-, *grab-) as grab, though the exact PIE root is not explicitly stated in the visible excerpt.

## Grip
Grip does not appear as a separate entry in the provided web page content, so no etymology information is available for it from this source.
```


## [2026-09-06T02:22:29.904Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8586,8660p' CHEUNG.txt"
}
```


### [2026-09-06T02:22:29.974Z] TOOL RESULT

```
*PIE— = LIV: – | Pok.: 


*grabH ‘to grab, seize, take’ 

*AVESTAN: grab- (garab-) ‘to grab, seize, take’ || (+ *a-) ‘to grab (to)’ || (+ *uz-) "to 
lift, raise; to stretch out; to take out’ || (+ *fra-) ‘to seize; to accept, receive’ || (+ 
*ham-) ‘to seize (with the hands)’. Q YAv. goropta- forms are very late, being 
transposed from BMP /griftan/. = Liste: 20f. 

Pres. {1} nä-: IND. 3sg. YAv. goroBnaiti (Yt 10.13), 3р1. YAv. "fragroBnonti (Yt 10.104), SUBJ. Zeg, 
Y Av. *gorofnat (F 21), 3р1. YAv. garoBnan (Y 57.25); Pres. {2} aja-: IND. 35р. YAv. hangouruuaiieiti (Y 
10.2), 3pl. med. YAv. uzgouruuaiieinte (Yt 13.147), INJ. 3sg. YAv. gouruuaiiat (He 5.65), med. YAv. 
hangouruuaiiata (Yt 19.35 f£), 3р1. YAv. fora gouruuain (Y 28.0), SUBJ. 3sg. ҮАУ. gouruuaiiat (Yt 8.60, 
Yt 14.52), YAv. uzgeuruuaiiat (V 19.23, V 19.25), 3pl. YAv. auua.gouruuaiian (Yt 11.6), ҮАУ. 
hangouruuaiian (V 6.29), OPT. 35р. YAv. gouruuaiiöit, IMPV. 2sg. YAv. gouruuaiia (Y 9.28); Pres. {3} 
ta-: IND. 3pl. goroptaiieinti (Vn 80), SUBJ. 35р. uzgoroptaiiat (FrK 16), Y Av. porogoroptaiiat (Nik 18), 
3pl. YAv. goroptaiianti (Vn 80); Aor. {1} athem.: INJ. 1sg. OAv. hongrabam (Y 31.8); Aor. {2} s- (or 
pres. inch.?): SUBJ. med. Isg. YAv. hangrofsane (Yt 19.49, Yt 19.51); Perf.: IND. 15р. YAv. "jayauruua 
(H 2.8), 3sg. ҮАУ. à.jayauruua (N 54); Partic.: pres. {1} YAv. *%әгәВпапі- (Fr.), aor. {2} med. YAv. 
hangrafSamna- (Yt 10.105), perf. ? YAv. jagorobus?(V 4.48) 

*OLD PERSIAN: grab- ‘to seize (as possesion), seize (as prisoner)’ — Kent: 183b 

Pres. aja-: impf. IND. 1sg. agrbayam <a-g-r-b-a-y-m> (DB 2.4, DB 4.7, DB 4.32), < a-g-r-b-a-y-[m]> 
(DNa 17), <[a]-g-r-b-a-y-[m]> (DSe 16), <a-g-r-b-a-[y]-m> (DZc 8), 35р. agrbaya <a-g-r-b-a-y> (DB 
2.88, DB 3.74, DB 5.12), <[a]-[g]-[r]-[b]-[a]-[y]> (DB 3.90), med. 3sg. agrbayata <a-g-r-b-a-y-t-a> (DB 
1.42 f, DB 1.81), <a-g-r-b-a-y-t-a> (DB 3.82), 3pl. agrbaya" <a-g-r-b-a-y> (DB 2.13, DB 3.48 f), 
<a-g-r-b-a-[y]> (DB 5.27); Pass.: impf. IND. 3sg. "agrbiya <a-g-r-b-i-y> (DB 2.73, v. Hoffmann 1956: 
18) 


120 *grabH 


*MIDDLE PERSIAN: MMP gyr-, BMP gyl- (OHDWN-) /gir-/ ‘to take, seize’ || (+ 
*pati-) MMP pdyr- ‘to take, receive, accept’, BMP ptgyl- (MKBLWN-) /padir-/ ‘to 
accept, receive’ = DMMPP: 170a, 272b 

Pres.: SUBJ. 25р. MMP gyr’y, 3sg. MMP gyr’d, 3р1. MMP "gyr’nd, IMPV. 2sg. MMP gyr, MMP gyyr, 
Partic.: perf. pass. MMP "gryptg, MMP grypt, grypt, gryft, gryft || (+ *pati-) Pres.: IND. 1sg. MMP 
pdyr’m, MMP pdyrym, 3sg. MMP pdyryd, BMP ptglyt /padiréd/, 3р1. MMP pdyrynd, MMP pdyrnd, 
BMP ptglynd /padirend/, SUBJ. jee MMP pdyr’y, 3sg. MMP pdyr’d, 1р1. MMP pdyr’m, 3pl. MMP 
pdyr’nd, IMPV. 2sg. MMP pdyr, 2pl. MMP pdyryd; Partic.: perf. pass. MMP pdyryft, pdyrypt; Inf.: 
MMP pdyrptn, BMP ptglptn /padiriftan/ 

*PARTHIAN: gyrw- ‘to take, seize’, grysp- (pass./inch.) ‘to be taken, be held’ || (+ 
*uz-) ‘zgyrw- ‘to take out’, 'zerysp- (pass./inch.) ‘to be removed, taken away, out’ || 
(+ *pati-) pdgyrw- ‘to receive; take’ = Ghilain: 79, 89 | DMMPP: 170a f., 102a, 
101b, 269a 

Pres.: IND. 3sg. "gyrwyd, 3р1. “gyrwynd; Partic.: perf. pass. gryft, Pass.(/Inch.): pres. IND. 3pl. gryspynd, 
SUBJ. 2sg. gryysp’, grysp’h; Inf.: gryfin || (+ *uz-) Pres.: IND. 3sg. ‘zgyrwyd, 3pl. ‘zgyrwynd, SUBJ. 
lsg. *‘zgyrw’n, IMPV. 2sg. *‘zgyrw, 2р1. ‘zgyrwyd; Partic.: perf. pass. ‘zgryft, ‘zgryftg, П inch. ‘zgrysp’d 
|| (+ *pati-) Pres.: IND. 35р. “pdgyrwyd, 3р1. pdgyrwynd, SUBJ. 2sg. "pdgyrw, pdgyrw’h, pdgyrw’h, 3sg. 
pdgyrw’, IMPV. 25р. pdgyrw; Partic.: perf. pass. pdgryft 

*KHOTANESE: (+ *ham-) hamgrih- ‘to raise; uphold’ = SGS: 138 

*SOGDIAN: SSogd. (yrB- BSogd. yrf-, CSogd. yrb-, MSogd. yrß- ‘to take, 
understand, know, be acquainted with’ || (+ *uz-) BSogd. zyrf- ‘to exalt’, BSogd. 
zyrwDs- (pass./inch.) ‘to be raised (?) || (+ *pati-) SSogd. ptyr(y)B-, BSogd. ptyrB-, 
BSogd. pcyrB- ‘to accept, receive; understand’ || (+ *fra-) BSogd. fryrB- ‘to offer’ 
Widely attested: Pres.: IND. 1sg. SSogd. ’yıß’m, SSogd. yrB'm, BSogd., MSogd. yıß’m, dur. CSogd. 
yrb’msq, CSogd. yrb’msqn, 2sg. MSogd. yrbyy, dur. SSogd. yrBy skwn, CSogd. yrbysq, 3sg. BSogd. 
yrBty, etc. || (+ *pati-) Pres.: IND. 3sg. BSogd. ptyrBty, SUBJ. 1sg. pcyrB’n, 3sg. BSogd. ptyrB’t, OPT. 
2р1. BSogd. pty’ysö, BSogd. pcyrBty, POT. 3sg. BSogd. pcyrB't wnty (SCE: 369); Impf.: IND. 3pl. 
BSogd. ptyyrB’nt, Partic.: pres. MSogd. (pl.) “ptyrBynyt (Sogdica: 25), perf. pass. SSogd. ptyryBt, Inf.: 
BSogd. ptyıß’y || (+ *fra-) Pres.: OPT. 3sg. BSogd. BryxB’y; Impf.: IND. 3pl. BSogd. fr’’yrß’nt 
*CHORESMIAN: xf- ‘to take, grasp; to befall (of illnesses)’ (*grfsa-), yBy- ‘to 
consider, take (for), regard as; to grab’ ( *grbaja-), yfs- (intr./inch.) ‘to be silent, keep 
quiet’, xFs- ‘to be covered’ || (+ *api- or *upa-) byBy- ‘to sense, find’. © On the 
different continuations of *grabH in Chor., see Humbach 1973: 95. = Samadi: 234 
f., 76 f., 236, 18
```


## [2026-09-06T02:22:43.719Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN grab\"; grep -n \"^grab,\\|^grasp,\\|^grim,\\|^grumble,\" KLN_1966.txt | head; echo \"=== SKT\"; grep -n \"^GRAB\\|^GRASP\\|^GRIM\\|^GRUMBLE\" SKT.txt | head"
}
```


### [2026-09-06T02:22:43.788Z] TOOL RESULT

```
=== KLN grab
16500:grab,  tr.  and  intr.  v.,  to  seize  suddenly.  —  MDu. grabben,  rel.  to  OS.  garva,  MDu.  garve,  OHG. garba,  ‘sheaf’,  lit.  ‘that  which  is  gathered  up  or together’,  fr.  I.-E.  base  *gherebh-,  *ghrebh-,  ‘to seize’,  whence  also  OI.  gfbhndti,  gfhndli,  ‘seizes’, OSlav.  grabiti,  ‘to  seize,  rob’,  Lith.  grebiu,  grebti, ‘to  rake’.  Cp.  garb,  ‘sheaf’,  grabble. Derivatives:  grab,  n.,  a  sudden  grasp,  grabb¬ er,  n.
16501:grab,  n.,  a  kind  of  vessel  used  in  the  Indian ocean.  —  VArab.  ghrab,  fr.  Arab,  ghurdb, ‘raven;  galley’,  of  imitative  origin.  Cp.  Heb,
16789:grumble,  intr.  and  tr.  v.  —  F.  grommeler,  fr. MDu.  grommelen,  freq.  of grommen,  ‘to  grumble’ (see  freq.  suff.  -le),  which  stands  in  gradational relationship  to  MDu.  grimmen,  grimmelen,  ‘to grumble’,  and  to  OE.  grimm,  grim,  ‘cruel, fierce,  terrible,  severe’.  See  grim  and  cp.  words there  referred  to.  The  b  in  grumble  is  intrusive. Cp.  ramble.
=== SKT
8007:GRIM.
```


## [2026-09-06T02:22:44.246Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/grim",
 "prompt": "Quote the etymology entries for 'grim' and 'grumble' — Old English form, Proto-Germanic reconstruction, and the PIE root given."
}
```


### [2026-09-06T02:22:49.652Z] TOOL RESULT

```
# Etymology of 'Grim' and 'Grumble'

## Grim

**Old English form:** _grimm_

**Proto-Germanic reconstruction:** _\*grimma-_

**PIE root:** _\*ghremno-_ "angry," possibly imitative of thunder sounds

## Grumble

The page does not provide a dedicated etymology entry for "grumble." It only appears in a list of "Entries linking to _grim_" but without detailed etymological information about the word itself.
```


## [2026-09-06T02:22:57.072Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^grasp\\|^grim\\b\\|^grim,\" KLN_1966.txt | head; echo \"---\"; grep -n \"grasp,  \" KLN_1966.txt | head -3; echo \"=== SKT lines\"; sed -n '8000,8020p' SKT.txt; echo \"=== SKT GRAB/GRASP\"; grep -n \"GRAB\\.\\|GRASP\\.\\|GRUMBLE\\.\" SKT.txt | head"
}
```


### [2026-09-06T02:22:57.188Z] TOOL RESULT

```
---
2630:analects,  also  analecta,  n.  pi.,  collected  writings; literary  gleanings.  —  Gk.  dvdXexxa,  ‘things, chosen’,  neut.  pi.  of  dvdXexxot; ,  ‘select,  choice’, verbal  adj.  of  dvaXcyEiv,  ‘to  pick  up,  gather up,  collect’,  fr.  avd  (see  ana-)  and  XeyEiv,  ‘to speak’,  prop,  ‘to  choose  (words)’,  which  is  cogn. with  L.  legere ,  ‘to  read’.  See  lecture, analemma,  n.,  an  orthographical  projection  of  the sphere  on  the  plane  of  the  meridional  (geom.)  — L.,  ‘a  sundial  showing  the  meridian  and  latitude of  a  place’,  fr.  Gk.  dvdXv;pi(xa,  ‘sundial’,  fr. dvzXapLpdvEtv,  ‘to  receive,  take  up,  restore’, fr.  dvd  (see  ana-)  and  XapifidvEiv,  ‘to  receive’. See  lemma  and  cp.  words  there  referred  to. analeptic,  adj.,  restorative,  tonic  (said  of  a  medi¬ cine);  n.,  a  restorative  medicine,  a  tonic.  —  Gk. dvaXrj-Ttx'k,  ‘restorative’,  fr.  dvxXajrfSdveiv,  ‘to receive’,  take  up,  restore’,  fr.  dvd  (see  ana-)  and Xap.(3dvEtv,  ‘to  take,  grasp,  seize;  to  receive’. See  prec.  word.
3218:apprentice,  n.  —  ME.  aprentis,  fr.  OF.  aprentiz (F .  apprenti),  fr.  aprendre  (F.  apprendre).  ‘to learn,  teach’,  fr.  L.  apprehendere,  ‘to  seize,  take hold  of,  grasp,  apprehend’,  whence  also  It.  ap- prendere.  OProven?.  aprendre,  Catal.  apendrer, Sp.,  Port,  aprender,  ‘to  learn’.  See  apprehend. Derivative:  apprentice,  tr.  v.
3250:‘arch,  vault’,  fr.  Gk.  &[>(?,  Ion.  ‘a  fastening, felloe  of  a  wheel’  (whence  (rivals,  ‘contact, point  or  line  of  junction’),  from  the  stem  of fircxeiv,  ‘to  fasten,  to  kindle’,  usually  in  the middle  voice  fiirresllat.,  ‘tq  grasp,  touch , whence  also  atpr;,  ‘a  touching,  handling  ,  acpav,
=== SKT lines
Grig,  a  small  eel,  a  cricket  (Scand.) Weakened  form  of  ertck,  still  preserved  in criik-ii;  cf.  Lowl.  Sc  tritk,  a  lick,  loose. —Swed.  dial,  krik,  AraJt,  a  creeping  crea- ture. —  Swed.  dial,  kraka^  to  creep ;  cf.  G. kritcken,  to  creep.  ^  In  phr.  *aa  merry as  a  grig*  grig  is  lor  Greek  (Troil.  i,  i. 118);  Merygreek  \»  a  chamcicr  in  UiUH'a KuisSer  Doister ;  from  L.  gnKmrit  to  liv« like  Greeks,  i.e.  luxuriously.
OiiU  [  M«  Grata.
1 I
I
I I
I
i86
GRIM.
GROSS.
Grtm,  fierce  (E.)  A.  S.  grim  \  «llied to  gram,  fierce,  aiiKiy,  furious.  +  ^ct\. grimmr,  grim,  gt-amr,  angry ;  Dan.  griMf grim,  gram,  angry ;  G.  grimm,  fury,  gram, hostile.  AUic'l  to  Gk.  \p«/iv»  XP'Vos^i  noise. (VGHAKM,  from  VGHAR,)
Qriinace.  (F.  — Scaml.)  F.  grimace^  *a crabd  loolce,'  Cot.'-Icel.  grlmay  a  mask, hood  ;  whence  grimuma^r,  a  man  in  dis- giii-^e.  A  grimace  disguises  the  face.  Cf. AS-^T/z/m.  amask.  Perhaps  allied  to  Grin.
Grimalkin,  a  cat.  (E. ;  partly  O.  H.  G.) Prob.  for  gray  Afalkiu,  the  latter  being  a cafs  name.  Malkin  =  Maid-kin,  dimin.  of Mahi^Maud,  i.e.  Matilda  ;  from  O.  H.(;. Mahthilt.  Here  maht  =  might ;  hilt  means hatlle.
Grime.  (Scand.)  Swed.  dial,  grima,  a smut  on  the  face ;  Dan.  grim^griim^  lamp- Mack,  soot,  grime ;  Icel.  grima,  a  disguise, mask.     Allied  tn  Qrimaoe.
Grin,  to  snarl,  grimace.  (E.)  "  M.  E. grcmten,  A.  H.  grcnnian,  to  gnn.  +  Da. gn'Jmn.  to  weei^.  fiet :  \ce\. grcttja,  to  howl. i'ia.w.grine,  to  grin,  simper,  Swcfl.  grina,  G. grfincn.     Allied  to  Groan,  and  to  Grim.
Grind.  (E.)  \.  S.  grimlan,  pt.  t  grand, pp.  gruiiden.  Allied  to  h.friare,  to  rub, Gk.  xpitiv.  to  graze,  Ski.  gkiish,  to  grind (VGHAR.)
grist,  a  supply  of  com  to  be  ground. (E.)  A.  S.  grisf.  From  the  base  gri-  of grind ;  cf.  blast  from  blow.
gristle.  (E.")  A.  S.  gristle,  cartilage; allied  to  grist,  and  A..S.  ^'''  islhiiian,  to  gnash the  teeth.  Kroin  the  base  of  grind,  wilh reference  to  the  nece-sity  of  crunching  it  il eaten.  Su  aUo  Du.  knarsbeen^  griitle. from  knarsen,  to  crunch.
Gripe  (E.)  A.  S.  grifan,  pi.  t.  grdp, pp.  gj-ipen,  to  seize.  +  Du.  grijpen.  Icel. gri  pa.  Sttxd.  gri  pa,  Dan.  gribe^  Goth. greipan.  G,  greifcn,  Ruiis.  grabite,  .Skt. grah  {yftiX\^grahh).  to  seize.  (VGARBII.) Allied  to  grab,  grasp.
grip,  sh.  (E.'^  yi.E.  gripe.  A.  S  gripe, a  grip;  ftom  the  pp.  oi ^rlpan    above).
grope.  {V.)  .VS.  grapian,  to  seize, handle;  hence,  to  feci  one%  way.  —  A.  S grip.  pt.  t.  oi gripnn  (aliovc).    .Sec  Gra«:p.
Grisette.  Grislod;  see  GriBsly.
=== SKT GRAB/GRASP
```


## [2026-09-06T02:23:06.462Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 645 661 664; do echo \"=== leaf $L\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' incoming/WLD/WLD_Bd1_pages.txt | head -25; done"
}
```


### [2026-09-06T02:23:08.189Z] TOOL RESULT

```
=== leaf 645
636                                     ghou-ros   — gouax (gaua x
                                                          -          -?)   :   gu-


schmecken", s. Miihlenbach-Endzelin I 61 mit Lit.), daneben as. goma anfkr.
                                                              1
                                                                                         ,


goume, ahd. goiimci „Mahlzeit, Gastmahl“, wovon as. gdmian ,.bewirten“,
ahd. goumen und goumon „erquicken und schmausen". (Die Bedeutungs-
verhaltnisse sind im einzelnen noch zu klaren; daS von gouma „Mahlzeit“
auszugehen sei, bat Rooth, Altgerm. Wortstudien 16ff. nieht bewiesen,
s. Slotty IF. 46, 369.)  Dazu ablautend ags. ofergumian „vernachlassigen“,
as. fargumon „versaumen“, isl. guma „acbten auf".
   Aber aisl. gaita „Waehe balten, bewachen, hiiten“ nicht mit Fick III 4
 121 <*gawatjan sondern am besten mit Noreen Urgerm. Ltl. 201, Kock
                                   ,


Ark. f. nord. Fil. 13, 164, Wadstein IF. 5, 32 und Neckel Eddaglossar 68
< *gaahtjan.
      Aksl. govejq     ,
                         „verehren“, russ. govetb „sich durch Fasten zum hi.
                               goveti
=== leaf 661
                                          ,                                                           ;:




(552                                          ghrebh-. gherebli-, glirebha x i-


gelircn“             — an einer Stelle zugeschriebene Bed.2 „sehreitet weit aus, holt
aus    L
           ‘
               ist   kaum richtig,
                        s. PW., und berechtigt nicht dazu, „ist gierig“ aus

.,schreitetworauf los“ herzuleiten, trotz der Bed.-Parallelen bei Wood Min.
11. 227, s. Uhlenbeck Ai. Wb. s. v., GotWb. u. grid us);
      lat.      grudior, -7 „sehreiten“, grail us, -us „Schritt, Stufe“, grallae „Stelzen“
(lat. grad aus gJire dh    s. Vf. IF. 19, 99, LEWb. s. v. Ablautstufe wie in      ;


lit .grkbju): lit. gruliju, -yti iJuskevicz) „gekn. wandern“ (Trautmann KZ.

42, 969; die Yereinzelung des      Wortes im Lit. ist kein geniigender AnlaB,
mit v. d. Osten-Saeken IF. 33, 216 Entlehnung aus dem Germ, anzunehmen)
got. grips (nur Acc. sg. grid) „Schritt, Stufe“ (wo fur allerdings Siebs KZ.
=== leaf 664
                                             ghrem-                                         655

mit anderer Erweiterung in arm. kork „Schmutz, Ivot           norw. dial, korg.
korge „Bodensatz, Hefe“, isl. korgr ds., lit. graimas ..Saline, Rahm“, isl.
him ,, Schmutz, Schleim" (nicht aisl. !), norw. krim ,,Schnupfen", schw. dial.
krime entfaltet sein soil. Jedenfalls lafit sich das von ihm ersonnene
Paradigma nicht durch ir. lat. grunna „palus“ stiitzen, da dies nach Zimmer
(ZfdA. 35, 170a 2, Nennius vindicatus       I) aus an. grundr ..Talgrund. Wie-
                                                 1   1


sengrund" entlehnt ist.
  Nicht hierher gr. figtyoj „benetze" s. u. mercgh-.


1. ghreni-         „scharf woriiber reiben, zerreiben, abkratzen", Erw. von ghcr- ds.
                 yremzti „schaben‘\ grdmdau, -yti ..kratzen, schaben", pa-
     Lit. grcmziu,
gramdis ,,Nachschrapsel“, lett. grem'Zu, gremzt „nagen, beifien", gramstit
„zusammenraffen“ (gegen cine andere Einreihung der bait. Worte s. u. gcr-.
grem- .,fassen“); anders Miihlenbaeh-Endzelin I 637, 649.
  got. gramsta dat. sg. „Holzsplitter“ (Persson Beitr. 99): ostfries. gram
„Bodensatz, Schmutz" isolche Bedd. auch bei ghrcit- und ghrT-i-), mnl. nnl.
grom „Eingeweide, Schmutz", nd. nl. groom ds., norw. mdartl. g rumen ..triibe,
mit Bodensatz vermischt", abl. fries, gram, grim ..Eingeweide, bes. von
```


## [2026-09-06T02:23:16.370Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ghou-ros\" incoming/WLD/WLD_Bd1_pages.txt | head; echo \"---\"; grep -n -A14 \"^ghou-ros\" incoming/WLD/WLD_Bd1_pages.txt | head -25"
}
```


### [2026-09-06T02:23:16.449Z] TOOL RESULT

```
60387:636                                     ghou-ros   — gouax (gaua x
60437:ghou-ros „furchtbar“ und „voller Furcht‘
---
60437:ghou-ros „furchtbar“ und „voller Furcht‘
60438-   Ai. ghord ,.furchtbar, grausam, bose“, n. „unheimliche Gewalt, Zauber-
60439-macht“, (fernbleibt ir. gilr „scharf, schmerzhaft trotz Stokes IF. 12, 126); got.
60440-                                                                  11
60441-                                                                       ,
60442-
60443-
60444-gaurs „betriibt‘ gauripa ,.Betrubnis“, gaurjan „kranken“, ahd. gorag „elend,
60445-                           -
60446-
60447-
60448-                               ,
60449-
60450-arm, gering '. (Nicbt zu entscheiden ist, ob ags. grornian as. grornon
60451-                                                                                     ,
```


## [2026-09-06T02:23:38.337Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT grab\"; grep -n \"^grab\\|garbaya\\|agarbaya\\|agrbaya\" KNT.txt | head -10; echo \"=== HRN giriftan/girav\"; grep -n \"giriftan\\|girav\\|giraw\\|gerev\" HRN.txt | head -10; echo \"=== HUB\"; grep -n \"giriftan\\|griftan\" HUB.txt | head -6; echo \"=== IEC\"; grep -n \"^ghrebh\\|^grebh\\|^ghrem\\|^grem-\\|^ghour\\|^gour\" IEC.txt | head -10"
}
```


### [2026-09-06T02:23:38.450Z] TOOL RESULT

```
=== KNT grab
568:agarbayam, ägarbīla = -grb-, Skt. agrbhdyat, Av. gaurvayal.
1473:But OP abara"tà, Skt. dbharanta; OP agarbayata,
2521:OP garba-ya- in imf. agarbéyam agarbdya' agarbd- уа" agarbayatd; to pAr. *grbha-, ef Skt. grbhäyati; 1 But pAr. *dhanva- may be merely *dha-nu- made
2765:III. Plural pronouns are often used where the antecedent is ‘men’ implied in a preceding kara ‘people, army’ or dahydus ‘province’ or the like: thus DB 1.65 -diš goes back to 64 kärahyä; DB 2.19-21 -šīm in two occurrences and the two plural imperatives go back to kéram; DB 3.11f akunava"tà is plural by the meaning of dahydué, as are agarbdya” 3.48 and agarbaya” 3.49 by refer- ence to kära 3.45. DNa 36f -&m refers back to -šim 36, denoting ‘men’ (cf. II, above) implied from bümim32. DB 4.5f -šim has the meaning ‘foe(s)’ by reference to hamaraná ‘battles’ (see JAOS 85.844—50, 41.74-5).
3530:81 Sacam : tya : Bàbirauv : hauv : agarbayata
3586:Техт or DB, Сошмх П: 1 :98ty : Dárayavaus : xSayafiya : paeüva : Naditabaira : ha 2 dà : kamnaibis : asabaraibis : amufa : Bübirum : ašiya 3 va: pasàva : adam : Babirum : ašiyavam : vasnd : Auramazdiha : uta : Ba 4 birum : agarbiyam : uta : avam : Naditabairam : agarbüyam : pasáva : ava 5 m : Naditabairam : adam : Babirauv : avüjanam —— :0ütüy : Dārayavauš : x 6 Sdyabiya : yātā : adam : Bübirauv : àham : ima : dahydva : tyà : hacàma : ha 7 migiyà : abava : Рагва : Üvja : Mada : Aðurā : Mudráya : Parfava : Margus : Өз 8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā Q ma : Cicixrais : puca : Kuganakà : пата : vardanam : Pársaty : avada : adaraya : 10 hauv : udapatatà : Uvjaiy : Кагаһуй : avaðā : afaha : adam : Imanis : amiy : 0 11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 12 iy : àham : abiy : Üvjam : pasáva : hac&ma : alarsa : Üvjiy& : avam : Marti 13 yam :agarbaya : hyašām : mafista : dha : шат : avàjana — : 00у: D 14 árayavaus : xSiyafiya : І martiya : Fravartiá : пата : Мада : hauv : udapatat 15 à : Madaiy : Катаһуй : ауаба : абала : adam : XSa6rita : amìy : Uvaxdtrah 16 уй : taumàyá : pasáva : kāra : Mada : hya : v'àpaliy : haw : hacáma : hamiciya : a 17 bava : abiy : avam : Fravartim : aSiyava : hauv : тёйуайтуа : abava : Madaiy 18 9àtry : Dárayavaus : xšāyaðiya : kara : Parsa : ша : Мада : bya : ира : mim : 4 19 ha : hauv : kamnam : aha : раѕауа : adam : kdram : fraiSayam : Vidarna : пата : Pársa : man 7 20 à : badaka : avam&àm : mafistam : akunavam : avataSaám : afaham : parait : avam : К 2] dram : tyam : Madam : jatà : hya : mand : пау : gaubataiy : pasiva : hauv : Vidarna : ha 22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 23 дау : ауада : hamaranam : akunaus : hada : Мада : һуа : Màdaisuvà 24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàram : t 26 yam : hamiciyam : aja : vasiy : Animakahya : mähyä : XXVII : raueabis : fakat 27 à : аһа : avatüsám : hamaranam : kartam : pasáva : hauv : Ката : һуа : manā : Карада : пат 28 à : dahydus : Mádaiy : avadà : mam : amánaiya : y8tà : adam : arasam : Mada ' 20m : 08у : Dàrayavaus : xšāyaðiya : адаг х : nàma : Arminiya : man 30 à : badaka : avam : adam : frāišayam : Árminam : avafasazy : aaham : paraidiy : ka 31 ra : һуа : hamigiya : mană : naiy : gaubataiy : avam : jadiy : pasiva : Dadarsi 32 š : aSiyava : yafà : Arminam : parárasa : pasáva : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09akatà : dha : ava 87 à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бакаќа : аһа : ауабадат : hamaranam : kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha : ауада ат : hamaranam : kartam : pasava 48 : Dadarsis : citā : mim : amánaya : Arm/niyaiy : yiti : adam : arasam : Ма
3631:88 igataxmam : agarbaya : anaya : abiy : mim : pasdvaSaly : adam : ша : n
3751:72 15 : asabaraibis : айтуауа : Aršādā : пата : didà : Harauvatiyà : а 73 vapara : atiy&i$g pasáva : Vivàna : hada : kara : nipadiy : tyaiy :aNya © 7777 74 va : avadāšim : agarbaya : ula : martiya : tyaisaly : fratama : anuSiya :
3758:81 racara : amiy : hya : Nabunaitahya : puça : pasàva : kara : Bübiruviya : hacáma : Һа 82 migiya : abava : abiy : avam : Arxam : aSiyava : Babirum : hauv : agarbayat
3765:90 gaubaté : uti : martiyà : tyaiSaly : fratamà : anuSiy& : аћаіб : agarbaya : pa
=== HRN giriftan/girav
=== HUB
1287:warum heisst es nicht: *paigriftan, *paigiram?
4480:giriftan *nehmen siehe Kap. 7. Kein lautlicher Grund ist
5084:'Schwefel', bal. gokurd, afgh. gOgar, gogil; giriftan'^) er-
5085:greifen , paz. griftan Shk. 246, zd. gerepta- (vgl. bal. giray,
6063:Tahne = zd. dtafsa-; giriftan *ergreifen', girau^) *Pfand*y
6484:pr. von giriftan ergreifen*, das auf *grwyamiy (vgl. ap.
=== IEC
4254:goureið “drive; dash; chase. Cf. WP I, 636 and geur- ` ON keyra ‘flog; drive; chase’; Sw. köra ‘travel, go, drive’; Srb. guram, ati (“jostle, push’, fr. *gourãið); Blg. gúram ‘dive’; Ukr. cf. hurma, R gur'ma “mass, throng’. E-gde in Srb. žurim se ‘hurry’
4885:ghrebh-, ghrebhlo-, -ió-, io ‘scraper; rake: oar. See next Cz. hřeb 'nail'; hřeben ‘comb’; OCS grebení, gs ene, id.; OCz. hfeblo ‘oar’; OCS greblja, id.; Latv. greblis *spokeshave, gouge’; (Ukr.
4895:ghrebho ‘dig’. Cf. ghrobhos, ghrabh-, ghrobh- OCz. hfebu, hřésti ‘bury’; Cz. po-hfeb, gs -hřbu ‘burial’; OCS grebü ‘grave’; Latv. grebe ‘vault’. (Big. greb ‘handful seems to represent a variant of type *ghrib-, cf. G Griff)
4896:ghrebhs-, extn. of ghrebh-, q.v. and cf. ghrebs- Arm. cf. gerpiğ (‘harrow, currycomb’, fr. *ghrebhsitio-); OCS cf. grebo, gresti ‘rake, scrape’; Latv. grebju, gerecht ‘scrape’; Li. (*-8-) grébiu, -ti (1) ‘rake’
4907:ghrem- (2) ‘hawk, cough up? Gk. cf. khrémma  expectoration' beside khrémptomai 'expectorate'; o-gde in Li. gra- mai 'expectoration, phlegm'. Isophonic are Lith. grémziu, -ti ‘scrape, upbraid'; Latv. gremZu, gremzt ‘gnaw; roar. See guhrem- however. For Alb. gromé ‘belch’: Latv. gre- mens, see guhrem-)
4913:ghrem- — ghribos, à
```


## [2026-09-06T02:23:48.606Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4880,4912p' IEC.txt | cut -c1-400; echo \"=== HUB 6055-6070\"; sed -n '6055,6070p' HUB.txt; echo \"=== HUB 5080-5090\"; sed -n '5078,5090p' HUB.txt"
}
```


### [2026-09-06T02:23:48.702Z] TOOL RESULT

```
ghrauo, ið ‘scrape, rasp’ Gk. khráo (1) & khraúð ‘graze, wound’; Lat. rav10, ire “be hoarse’; cf. also råvus (2) ‘hoarse, gruff, harsh’; rāvis, i-st. ‘hoarseness’; Li. griáuju, ti, pf. grióviau: Latv. grauju, pf. grāvu, inf. graut, v. ‘destroy’; Li. cf. grióva ‘boor’; griovis, gs -io ‘ditch’
ghrauos (ghrēuos) ‘dun, grey’. WP I, 602. For vocalism cf. bhlàuos Lat. ravus (1) ‘dun’; OHG grao, ON grár ‘grey’; OE cf. græg, id. fr. *ghreuio-. (The vocalism is that of Lat. flavus: OHG blao). Cf. also perb. Slovene gruj (émuraena' = “gray- ling'?). (Variant: ON grjár 'grey")
ghré-, see ghréio and ghrésó
ghrébo, io ‘seize, grapple’ MLG gràpen, id.; ON (alleged) grápa, id.; Li. grébiu, -ti (2), id.
ghrebsó (ghrebhs-) ‘seize’. Cf. ghrebh- Arm. gerpem ‘grab; ravage’; LG gripsen ‘seize’; grips ‘grasp’; cf. also Av. garofS$-, id.; LG grapsen, E grasp, id.
ghrebh-, ghrebhlo-, -ió-, io ‘scraper; rake: oar. See next Cz. hřeb 'nail'; hřeben ‘comb’; OCS grebení, gs ene, id.; OCz. hfeblo ‘oar’; OCS greblja, id.; Latv. greblis *spokeshave, gouge’; (Ukr.
ghránis, os — ghrem-
20
25
30
35
40
45
336
hreblja ‘dike, embankment? is isophonic). Long-grade in OE græfa ‘brushwood’ and in Li. grébiu, -ti (1) ‘rake’
ghrebho ‘dig’. Cf. ghrobhos, ghrabh-, ghrobh- OCz. hfebu, hřésti ‘bury’; Cz. po-hfeb, gs -hřbu ‘burial’; OCS grebü ‘grave’; Latv. grebe ‘vault’. (Big. greb ‘handful seems to represent a variant of type *ghrib-, cf. G Griff)
ghrebhs-, extn. of ghrebh-, q.v. and cf. ghrebs- Arm. cf. gerpiğ (‘harrow, currycomb’, fr. *ghrebhsitio-); OCS cf. grebo, gresti ‘rake, scrape’; Latv. grebju, gerecht ‘scrape’; Li. (*-8-) grébiu, -ti (1) ‘rake’
(ghred-, see &hred-, ghrod-)
(ghredh-, see ghréio, ghrés-)
ghreibó, io ‘seize, clutch’. WP I, 647 Go. greipan; MHG sien: OE gripan; ON grípa, id.; Li. griebiu, -^ti, id.
ghreiió (1) ‘grab’. Cf. ghreimn, ghres-, (ghrs-), ghreim- (1) Gk. cf. khráo, fut. khréso (1) ‘seize’, get: Du. graaien ‘filch, scrounge, scrabble’; Li. grieju, -ti (1) ‘grab’; cf. greitas ‘quick’
ghreiið (2) ‘scrape, wear, gnaw’. Cf. ghreim- (2) & ghriið Li. grieju & greju, inf. grieti ‘skim’; Alb. cf. (ambig.) gri, gs grini ‘whetstone’: Srb. grinja ‘moth’; perh. also ON gríss ‘pig
ghreim- (1), (ghreimn) ‘seizure’. Cf. ghreiió (1)
OE cf. grin ‘snare’; Li. greimas ‘attack’ ghreim- (2) ‘surface, crust’. Cf. ghreiio (2) Gk. cf. khrima (Cunguent,, vbi. n. fr. khrío “touch, rub'); OE grima, m. (*mask, helmet, ghost’; cf. the o-gde form of Gk. khroiá *skin); EME grime “coating of soot, grime'; ON gríma
“mask, visor’; Li. greimas ‘film, top skin (ghreio, ghreiio (?) “requirement, responsi- bility, need, debt, obligation. see ghrées-. The evidence is limited to Gk., cf. khr&, khreía, khreía, f. beside khréos, Do- ric: khréos, id., and khr&me, id. A possible iso- phone is Skt. hràsah ‘decrease, detriment’, of uncertain origin. Per. garàyam = ‘incline, tend' ghrem- (1) ‘roar, 
337
Gk. cf. khremetízo ‘neigh, snort’; MHG grim- men “rage, roar; ON grimmast, refl. id.; R cf. greméti, id. Cf. also MHG grim(me) ‘grim, furious’; ON grimmmr, id.; OE grimman, grims- ian ‘rage’; grimm as MHG. O-gde gram ‘fierce, raging’; MHG gram, id. (and "rage
ghrem- (2) ‘hawk, cough up? Gk. cf. khrémma  expectoration' beside khrémptomai 'expectorate'; o-gde in Li. gra- mai 'expectoration, phlegm'. Isophonic are Lith. grémziu, -ti ‘scrape, upbraid'; Latv. gremZu, gremzt ‘gnaw; roar. See guhrem- however. For Alb. gromé ‘belch’: Latv. gre- mens, see guhrem-)
ghrendhilos (ghrendhlo-) “bar, shaft. Cf. ghrendhos (2) and WP I, 657 OHG grintil; MHG.OE grindel; MLG.Du. grendel; OCz. hřiedel, Cz. hřídel & *axle-tree; plow-handle’; hfedlo ‘windlass’; Pol. gradziel *plowbeam; shaft of cart). (It is uncertain if the SI. forms derive from Germanic)
(ghrendho “crush, grind, trample; grunt, growl, bellow’. See guhrendh-)
ghrendhos (1), (gherndos) ‘scrapings, scab, dandruff, rubble’ Gk. kherádos, n. ‘gravel, rubble, wrack’; Alb. (ambig.) grêndë ‘rock, cliff; OIr. grend, grenn ‘bristle, beard’; MIr. greann, id.; Olr. cf. grinn ‘sharp’; grinne ‘keenness; spearhead’; Ir. cf. grinn-eall ‘seabed, lake-bed’; OE grinde ‘shingle’; MHG grint, gs -des, sm. 'scurf'. Cf. guhrendh-
ghrendhos, is (2) ‘bar, pole, shaft. Cf. ghrndh- ON grind ���hurdle; pen’; Sw. grind "lattice gate’; OE cf. grindel “bar; hurdle’; OCS gredü, greda (*beam": *-en- or *-n-); Cz. hfada, hředa ‘perch’; Big. gredà ‘beam’; Srb. greda, id. and ‘joist’; Li. cf. grendžiu, v. ‘pave, floor’; beside grindis, f. Let ‘floorboard’; grandà ‘plate, lamina’; LW in Hung
ghrësð (1) “fail, wane, lack, desire, want. Cf. ghreio Skt. hrasami, pf. jahrasam ('diminish', intr.); hrasvah 'stunted'; hrasah ‘diminution’; Gk. khréo, khreío need: khré, impers. “it is necessary; khrëizð, khréjzo “need, desire’;
=== HUB 6055-6070
(siehe oben); ispar {sipar) 'Schild*, afgh. spar, phi. spar;
isparl (= sipart) Vollendet', phi. spurlk (oben p. 73) ; isped
(= siped) weiss, zd. spaeta-; istabr = sitabr H. 713;
Istaxr = phi. Sfaxr; istanba = sitanba H. 718; iskara
(Vullers: iskira) *Jagdhabicht* = sikara, u. s. w.
d) Einschub von i in: biradar *Bruder = ap. bra-
tar-; biristan *braten', iran. brij, skr. bhrjj; Jinn/ *Kupfer, =
arm. pUnj; diraz ^) 'lang = zd. drajah-; diraxt *Baum'; dirafs
Tahne = zd. dtafsa-; giriftan *ergreifen', girau^) *Pfand*y
*) Neben daraz JASB. XXXVII, 1, p. 37.
') Ueber giravidan *glauben* siehe § 53,- 172 -
ap. grab *ergreifen' ; gir^ 'Hals* = zd. grwH- ; giran 'schwer ,
afgh. LW. gran; girtstan *klagen'; xirad 'Verstand' = zd.
xratU' ; xirdmldan schreiten*, skr. kram; firistCLdan schicken ,
firista *Bote' = ^rz. frMa Shk. 245; firEsta *Bote, Engel' =
arm. hrestak; firod (fiirDd) *hinunter' = paz. fro^; fireftan
=== HUB 5080-5090
--- ^hrstan), 3. pr. hUad (aus ap. *hrdatiy) = skr. srjdii, zd.
herezaiti; gila 'Klage' = zd. gerezd-; kistan saen', skr.
krsdti; kirm 'Wurm', phi. k(i)rm oder k{a)rm GI. and Ind.
198, skr. krmi~; -gird in Namen =^ arm. -kert, zd. kereta-,
skr. krta-, vgl. § 7; girda 'rundes Brot' = arm. grtak
'Laib Brot'; xirs 'Bar = zd. aresa-, skr. rkSa-; gdgird
'Schwefel', bal. gokurd, afgh. gOgar, gogil; giriftan'^) er-
greifen , paz. griftan Shk. 246, zd. gerepta- (vgl. bal. giray,
ptc. gipfa). Ueber den Reim girift : biraft bei Firdusi
s. Horn, Grundriss, p. XIV der Einleitung.
Fiir i ist a eingetreten in kard 'machte' = zd. kereta-
nach kardan (inf.) und karddr, KZ. 27, 111, vgl. -gird in
Namen ; tarsfdan sich fiirchten', 3. pr. tarsad = ap. trsatiy,
```


## [2026-09-06T02:24:10.471Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B0%DB%8C%D8%B1%D9%81%D8%AA%D9%86",
 "prompt": "Quote the Persian entry for پذیرفتن (pazireftan) 'to accept': its full etymology (Middle Persian padīriftan, the prefix pati- plus the root grab-, any Proto-Iranian reconstruction) and definitions."
}
```


## [2026-09-06T02:24:12.620Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%BA%DA%98%D9%85/",
 "prompt": "What do the Persian dictionaries (Dehkhoda لغت‌نامه, Mo'in فرهنگ معین, عمید) say for the headword غژم? Quote the definitions verbatim, including any variant spellings such as غزم and any citation of Rudaki's verse."
}
```


### [2026-09-06T02:24:15.964Z] TOOL RESULT

```
# Persian Entry: پذیرفتن (paziroftan)

**Etymology:**
From Middle Persian padīriftan, composed of the prefix *pati-* combined with *grab-* ("to grab"), ultimately derived from Proto-Indo-European *gʰrebʰ-*. This root also appears in Sanskrit gṛhṇāti and Proto-Germanic *grab-.

**Definitions:**
1. To accept, to agree with, to embrace
2. To receive, to admit

The entry notes a synonym: قبول کردن (qabul kardan), and includes a 13th-century literary example from Rumi's Masnavi demonstrating the verb's usage in context.
```


### [2026-09-06T02:24:19.849Z] TOOL RESULT

```
# Definitions of غژم from Persian Dictionaries

**Dehkhoda (لغت‌نامه دهخدا):**
"دانه انگور که پخته و تازه باشد" (a grape seed that is ripe and fresh). The dictionary also lists meanings including anger/wrath, and cites Rudaki's verse: "شیر غژم آورد و جست از جای خویش / و آمد آن خرگوش را آلغده پیش."

**Mo'in (فرهنگ معین):**
Two main entries are given—"خشم، قهر" (anger, fury) and "هر دانة میوة انگور که به خوشه متصل است" (each grape berry attached to the bunch).

**Amid (فرهنگ عمید):**
Lists three senses: "۱. خشم، غضب، قهر" (anger, rage, fury), "۲. حمله" (attack), and "دانۀ انگوری که از خوشه جدا شده باشد" (a grape separated from its cluster).
```


## [2026-09-06T02:24:31.158Z] TOOL CALL #62: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%B1|page194 root Ghou-ro-s: Persian gur 'grave' etymology (MP gabr), vs Nourai's Skt ghora-\" \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%88|page194 root Ghrebh: Persian gerow 'pledge' < MP graw < PIE *ghrebh-\" \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%81%D8%AA%D9%86|page194 root Ghrebh: Persian gereftan < MP griftan < OP grab- < PIE *ghrebh2-, cites Cheung 119-21\" \"https://en.wiktionary.org/wiki/%D9%BE%D8%B0%DB%8C%D8%B1%D9%81%D8%AA%D9%86|page194 root Ghrebh: Persian paziroftan < MP padiriftan < pati-+grab-\" \"https://www.etymonline.com/word/grab|page194 root Ghrebh: English grab 1580s < MDu/MLG grabben, PIE ghrebh-(1); grasp < PGmc *grap-/*grab-\" \"https://www.etymonline.com/word/grim|page194 root Ghrem: English grim < OE grimm < PGmc *grimma-, PIE *ghremno- 'angry'\" \"https://abadis.ir/fatofa/%D8%BA%DA%98%D9%85/|page194 root Ghrem: Persian ghazhm - Dehkhoda/Moin/Amid senses 'anger, wrath' and 'grape berry', Rudaki verse\"; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done"
}
```


### [2026-09-06T02:24:36.319Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fc95bb38961ea794.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f5c41ff5165c4207.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/83a3b72522c649d5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c77d42bed1b12610.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/79bab154e5094462.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/624e9dd5b49a13a7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0640acaef406d489.txt
```


## [2026-09-06T02:25:00.006Z] TOOL CALL #63: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ARY/0446.vision.txt <<'EOF'\n[read from the page image by a vision model — Aryanpur Kashani, Farhang-e Rishe-ha-ye Hend-o-Orupayi-ye Zaban-e Farsi, printed p. 446 (pdf page 445)]\n\nRunning head: ۴۴۶ / گور (به چم \"قبر\"، \"آرامگاه\")\n\nEntry 1:\n  فارسی (PERSIAN):            گور (به چم \"قبر\"، \"آرامگاه\")      GŪR\n  چم انگلیسی سرواژه‌ی فارسی:   TOMB, GRAVE\n  هند و اروپایی (INDO-EUROPEAN):  *GREBH-, *GROBH-, *GRABH-, *GHREBH\n  کردی (KURDISH): GŪR, GŌRN        لهستانی (POLISH): GRÓB\n  افغانی (پشتو) (AFGHANI): GOR      روسی (RUSSIAN): GROB\n  سانسکریت (SANSKRIT): GIRI-H       چک (CZECH): HROB\n  گوتیک (GOTHIC): ZRAB, GRABA       بوهمی (BOHEMIAN): HROB\n  ایسلندی کهن (OLD SCANDINAVIAN): GROF, GRABŌ    اسلواکی (SLOVAK): HROB\n  ساکسونی کهن (OLD SAXON): GRAF     آلبانی (ALBANIAN): GUR\n  آلمانی کهن (OLD HIGH GERMAN): GRAB\n  آلمانی (GERMAN): GRAB\n  انگلیسی کهن (OLD ENGLISH): GRAF\n  انگلیسی (ENGLISH): GRAVE\n  دانمارکی (DANISH): GRAVE\n  سوئدی (SWEDISH): GRAV\n  نروژی (NORWEGIAN): GRAVE\n  هلندی (DUTCH): GRAF\n  اسلاوی کهن (OLD CHURCH SLAVIC): GROBŪ\n\n  پسگشت‌ها (REFERENCES):\n    POKORNY: 455\n    BARNHART: (GRAVE) 447\n    BUCK: 293, 593\n    ONIONS: (GRAVE) 411\n    SKEAT: (GRAVE) 248\n    برهان قاطع: ۱۸۵۰\n\n  یادداشت: چم پیشین این واژه در زبان‌های ژرمنی: کندن، چال کردن.\n\nEntry 2 (same page, following):\n  فارسی (PERSIAN): گوش   GUSH ; چم: EAR\n  هند و اروپایی (INDO-EUROPEAN): *GHOUS-, *ŌUS-, *∂US-, *US-\n  اوستایی (AVESTAN): GAOSHA, ŪSHI ; پارسی باستان (OLD PERSIAN): GAUSHA ;\n  پهلوی (PAHLAVI): GŌSH ; اوستی (OSSETIC): GHOS, QUS ; کردی: GUH ;\n  بلوچی: GŌSH ; افغانی: GHVAGH, GHWAZH ; سانسکریت: GHŌSHA ;\n  ارمنی: UNKN ; یونانی (GREEK): OŪS ; لاتین (LATIN): AURIS, AURICULA\n\n[Relevance: Aryanpur assigns Persian گور \"grave, tomb\" to the Indo-European root\n*ghrebh- \"to dig, bury\" (Pokorny 455 = Pokorny's 2. ghrebh-), i.e. the source of\nEnglish grave / German Grab — NOT to Pokorny's ghou-ro-s \"terrifying\" (Skt. ghorá-),\nwhich is what Nourai's chart on book p. 164 draws. In his introduction (printed p. 40,\npdf page 49) Aryanpur nevertheless lists گور among the Persian words whose IE root is\nstill a dead end: «واژه‌ی «گور» با واژه‌های انگلیسی GRAVE و آلمانی GRAB همسانی چشمگیری\nدارد. آیا این واژه‌ها همریشه‌اند؟»]\nEOF\necho saved; ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ARY/"
}
```


### [2026-09-06T02:25:00.084Z] TOOL RESULT

```
saved
total 1784
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  5 22:25 .
drwxrwxr-x 11 sfmqrb sfmqrb   4096 Sep  5 16:42 ..
-rw-rw-r--  1 sfmqrb sfmqrb 328629 Sep  4 13:39 0051.png
-rw-rw-r--  1 sfmqrb sfmqrb   1571 Sep  4 13:39 0051.txt
-rw-rw-r--  1 sfmqrb sfmqrb   1003 Sep  4 14:18 0051.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 360766 Sep  5 02:04 0136.png
-rw-rw-r--  1 sfmqrb sfmqrb   1990 Sep  5 02:04 0136.txt
-rw-rw-r--  1 sfmqrb sfmqrb   2061 Sep  5 02:05 0136.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 331276 Sep  5 16:11 0291.png
-rw-rw-r--  1 sfmqrb sfmqrb   1453 Sep  5 16:11 0291.txt
-rw-rw-r--  1 sfmqrb sfmqrb 355916 Sep  4 14:43 0297.png
-rw-rw-r--  1 sfmqrb sfmqrb   1663 Sep  4 14:43 0297.txt
-rw-rw-r--  1 sfmqrb sfmqrb   1854 Sep  4 14:52 0297.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 391269 Sep  5 22:17 0446.png
-rw-rw-r--  1 sfmqrb sfmqrb   1688 Sep  5 22:17 0446.txt
-rw-rw-r--  1 sfmqrb sfmqrb   2664 Sep  5 22:25 0446.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb   1980 Sep  5 16:48 441.vision.txt
```


## [2026-09-06T02:25:02.396Z] TOOL CALL #64: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T02:25:02.434Z] TOOL RESULT

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


## [2026-09-06T02:26:02.370Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"paiti\\.grab\\|paiti.gr\\|pati-grab\" BRT.txt CHEUNG.txt | head; echo \"=== col markers near grab\"; sed -n '10430,10440p' BRT.txt; awk 'NR>10390 && NR<10445' BRT.txt | grep -n \"^ *52[0-9]\" "
}
```


### [2026-09-06T02:26:04.350Z] TOOL RESULT

```
=== col markers near grab
•  j.  "«^<y  jTiyäi  ustS/ia"  Nik,  2.
•  j.  yamata-,  ymata-,  p,  gmata-  Adj. (fem.  'iä-),  PPfP.:  &.gam:
KompE.  (s.  auch  *mymala').
■  %.gva-,  j.  *»«-''  (fem.  i'J-",  wr-'')'*:  sva. ^av:
KompE.  —  ai.  'gi'n-,  gr,  T«-;  Bthl.  IF.  12.
13a    ~    O  S  271,  27s.    —    ')   Nur   in    adj.
•  j-,  g.,  p.  'grab-  V.  'greifen'.  Praes. i  grab-,  11%  g^rminä'^,  15  girißa-*'"'^ , 23  garb.tya-,  gSun'aya-'^,  24  gSurvaya-'^, <)-^  24 ^3r?mbaya-'^,2T g)r3bya-,gpr)uya-^'>; Perf  I  jagaurv-*^,  jayaurv-^^,  ftgaurv-^^, 2  jag»r»b-.  —  PPf P.  g^r^ta-'');  Inf.  gfnbqm.
i)  'ergreifen,  festhalten  an  — '  (Akk.): hä  hl  b^zava  gmrvayat  "sie  hielt  ihn  an seinen  Armen  fest"  Yt  j.  65 ;  —  s.  noch Inf  2)  B  'in  seine  Gewalt  bringen,   er-
obern; gefangen  nehmen',  Akt  und  Med.: xsiii-^atn  lycr  bäbirauv  hauv  agarbJyatS Bh.J.16;  11";  —  imil  dahyavJ^  tyä  adam agarbiiyam  D.tf.3;  ij-y,^-  *vi"da''/am3 bilbirum  agarbSya''  Bh.y.  14;  2.  i;  — bäbirum  hauv  agarbilyatä'&i.^.iy,  —  utä g  xsaya'iiyä  agarbSyam  Bh.  4. 2;  3;  — avam  vahyazdätam  agarbsy^  utä  martiyä tyaisaiy  fratamä  anusiya  äh^tä  agarbaya"
Uiflitized  by  VjOOQ  IC
527  _,!£^'  ^
50:527  _,!£^'  ^
```


## [2026-09-06T02:33:33.299Z] TOOL CALL #66: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /home/sfmqrb/git/rishe/data/verification/page-194.json <<'JSONEOF'\n{\n  \"pdf_page\": 194,\n  \"book_page\": 164,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ghou-ro-s\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ǵʰou-ro-s (Pokorny ghou-ro-s) 'frightful; full of fear'\",\n      \"note\": \"The root box is a faithful copy of Pokorny: POK_02 (leaf with printed pp. 453/454) prints 'ghou-ro-s ,furchtbar' und ,voller Furcht'', with Ai. ghōrá-ḥ, Goth. gaurs 'betrübt', OHG gōrag, ON gaurr; = Walde-Pokorny I 636 (WLD_Bd1_pages.txt leaf 645 running head '636 ghou-ros'). Language label (Indo-European) and gloss ('terrifying') are right. Caveat on modern currency: the lemma rests on a Sanskrit–Germanic equation only, it has no Iranian material in either Pokorny or Walde-Pokorny, and Watkins/AHD does not carry it at all (no 'ghou-ro-s' headword and no index entry in AHD_watkins1985.txt), because no English word descends from it. The problem on this page is therefore not the root but the Persian node hung under it.\",\n      \"note_fa\": \"ریشهٔ «Ghou-ro-s» درست همان چیزی است که پوکورنی در صفحهٔ ۴۵۳ می‌آورد: *ǵʰou-ro-s «ترسناک؛ ترسیده»، با گواه سنسکریت ghōrá- و گوتی gaurs. برچسب زبانی (هندواروپایی) و معنای آن نیز درست است. اما باید توجه داشت که این ریشه تنها بر پایهٔ برابری سنسکریت–ژرمنی ساخته شده و در واتکینز/AHD اصلاً نیامده است؛ نه پوکورنی و نه والده‑پوکورنی هیچ صورت ایرانی زیر آن نمی‌آورند. پس ایراد این مدخل در خودِ ریشه نیست، بلکه در گرهِ فارسی «گور» است که نورایی زیر آن آویخته است.\",\n      \"sources\": [],\n      \"ref_check\": [\n        {\"ref\": \"POK:453\", \"status\": \"supports\", \"note\": \"POK_02.txt line 1676: 'ghou-ro-s ,furchtbar' und ,voller Furcht'. Ai. ghōrá-ḥ ,furchtbar, ehrfurchtgebietend'... got. gaurs ,betrübt'... WP. I 636, Feist 208.' The page break '454' falls inside the entry, so Nourai's page 453 is the first page of the lemma — correct.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"POK_02.txt line 1676 (printed pp. 453-454); POK_full.txt 'Root / lemma: ghou-ro-s ... Page(s): 453-454'\", \"stance\": \"supports\", \"note\": \"'ghou-ro-s ,furchtbar' und ,voller Furcht''; material is Skt ghōrá-, Goth. gaurs/gaurjan, OHG gōrag, ON gaurr, plus Slavic žuriti.\"},\n        {\"src\": \"WLD\", \"where\": \"Band I p. 636 (WLD_Bd1_pages.txt line 60437, leaf 645)\", \"stance\": \"supports\", \"note\": \"'ghou-ros „furchtbar“ und „voller Furcht“. Ai. ghorá ,,furchtbar, grausam, böse“ ... got. gaurs „betrübt“' — the source Pokorny abbreviates as WP. I 636. No Iranian form is cited.\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt, root list and index (grep 'ghou-ro', 'ghou-')\", \"stance\": \"silent\", \"note\": \"Watkins 1985 has ghóu- 'to yawn', gheu(e)- 'to call', ghow-ē- 'to honor' — but no ghou-ro-s entry and no index reference to one; the root has no English reflex.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"Ğôrâh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Nourai's 'Ğôrâh' is the Sanskrit nominative singular ghorá-ḥ (his Ğ = gh), an adjective 'terrible, awful, frightful; venerable, sublime' already in the Rigveda (e.g. RV 10.34.14 of the dice, and of the Aṅgirases), with a neuter substantive ghoram 'uncanny power, magic'. It is a thematic -ro- adjective built to the base seen in Pokorny's ghou-, exactly the formation the root box names: *ǵʰou-ro- > Skt ghorá-. Pokorny 453 and Walde-Pokorny I 636 cite this word as the head witness of the root and equate it with Gothic gaurs 'grieved', OHG gōrag 'wretched', ON gaurr 'wretch', the semantics running 'inspiring dread' ~ 'feeling dread'. The arrow root→Sanskrit is therefore the standard textbook one; the only reservation is that later handbooks (Mayrhofer) treat the further origin of ghorá- as not firmly established, since the Germanic equation is the sole support outside Indic.\",\n          \"derivation_fa\": \"«Ğôrâh» در کتاب همان ghorá-ḥ سنسکریت است (Ğ نزد نورایی برابر gh)، صفتی به معنای «هراس‌انگیز، سهمگین؛ باشکوه، سزاوار حرمت» که از ریگ‌ودا به بعد گواه دارد و صورت خنثای ghoram آن «نیروی رازآلود، جادو» معنی می‌دهد. این واژه صفتی است با پسوند ‑ro‑ بر ستاک *ǵʰou‑، یعنی دقیقاً همان ساختی که در جعبهٔ ریشه آمده است. پوکورنی (ص ۴۵۳) و والده‑پوکورنی (ج ۱ ص ۶۳۶) همین واژه را شاهد اصلی ریشه می‌گیرند و آن را با گوتی gaurs «اندوهگین» و آلمانی علیای کهن gōrag «بیچاره» هم‌ریشه می‌دانند. پس این پیکان درست است؛ تنها یادآوری آنکه ریشه‌شناسان امروزی (مایرهوفر) خاستگاه دورترِ ghorá- را قطعی نمی‌دانند، چون تنها تکیه‌گاهش همان برابری ژرمنی است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:453\", \"status\": \"supports\", \"note\": \"POK_02.txt line 1677: 'Ai. ghörd-h ,furchtbar, ehrfurchtgebietend', n. ,unheimliche Gewalt, Zaubermacht''— the Sanskrit word and gloss the chart gives.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"printed p. 453 (POK_02.txt line 1677)\", \"stance\": \"supports\", \"note\": \"'Ai. ghōrá-ḥ ,furchtbar, ehrfurchtgebietend', n. ,unheimliche Gewalt, Zaubermacht''.\"},\n            {\"src\": \"WLD\", \"where\": \"Band I p. 636 (WLD_Bd1_pages.txt lines 60437-60444)\", \"stance\": \"supports\", \"note\": \"'Ai. ghorá ,,furchtbar, grausam, böse“, n. „unheimliche Gewalt, Zaubermacht“ ... got. gaurs „betrübt“, gauriþa „Betrübnis“, gaurjan „kränken“, ahd. gorag „elend, arm, gering“'.\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt (grep 'ghorá', 'ghou-ro')\", \"stance\": \"silent\", \"note\": \"Watkins does not list this root or the Sanskrit word; no English derivative exists.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"gŭr «گور»; gŭrâb «گوراب ۱ (گورابه)»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Both Persian words are real and glossed correctly: Borhan-e Qate' (BQT_v3_pages.txt pdf p. 648 = printed ~1853) has گوراب '... و گنبدی که بر سر قبرها می‌سازند ...' and گورابه '... و گنبدی را نیز گویند که بر سر قبرها سازند', i.e. exactly Nourai's 'the dome built over a grave'; گور 'grave' needs no defence. What is wrong is the arrow. Nourai's own reference is the page that refutes him: Horn, Grundriss p. 210 (HRN.txt leaf 232) says 'gōr ,Grab', dagegen, das Geiger neuerdings (Lautl. des Bal. 53) mit ai. ghōrá- ,grausig, furchtbar' verglichen hat, ist nach Nöldeke, Pers. Stud. II, 41 ein semitisches Lehnwort' — Horn names precisely the Skt ghorá- comparison the chart draws (Geiger's) and rejects it in favour of a Semitic loan. The other books point elsewhere too: MacKenzie has no Middle Persian gōr 'grave' at all (PHD_pages.txt: 'gōr [gwl | N ~] onager, wild ass' only), so there is no Pahlavi link in the chain; Wiktionary derives NP گور 'grave, tomb' from MP gabr (gwbl) 'hollow, cavity, womb'; and Aryanpur (printed p. 446) files گور 'tomb, grave' under IE *GREBH-/*GROBH-/*GRABH- with Pokorny 455 — that is Pokorny's 2. ghrebh- 'to dig, bury', the source of English grave and German Grab (and hence the neighbouring root on this very page, not this one), while noting in his introduction (printed p. 40) that the equation is still an open question. Phonologically, moreover, Skt ghorá- ~ NP gūr would require an Iranian *gaura-/*gauro- 'terrifying' that is nowhere attested (Avestan gaurvaya- belongs to grab-; Av./MP gōr is 'onager' < Av. gaura-), and the semantic step 'terrifying' → 'grave' is asserted, not shown. gūrāb/gūrāba 'dome over a grave' is transparently built on گور itself (گور + ‑آب/‑ابه, alongside the homonymous گوراب 'salt marsh, stocking'), so it inherits whatever verdict گور gets and adds nothing independent to the root.\",\n          \"derivation_fa\": \"هر دو واژه واقعی‌اند و معنای‌شان درست آمده است: برهان قاطع (چاپ معین، صفحهٔ چاپیِ حدود ۱۸۵۳) ذیل «گوراب» می‌آورد «... و گنبدی که بر سر قبرها می‌سازند ...» و ذیل «گورابه» «... و گنبدی را نیز گویند که بر سر قبرها سازند»؛ «گور» به معنی قبر هم که نیاز به گواه ندارد. ایراد در خودِ پیکان است. جالب آنکه مأخذِ خودِ نورایی همان صفحه‌ای است که ادعایش را رد می‌کند: هرن در «گروندریس» ص ۲۱۰ می‌نویسد که گایگر تازگی gōr «گور» را با ghōrá- سنسکریت «سهمگین، ترسناک» سنجیده است، ولی به گفتهٔ نولدکه (Persische Studien II، ص ۴۱) این واژه وام‌واژه‌ای سامی است. مکنزی نیز در فرهنگ پهلوی هیچ gōr به معنی «گور/قبر» ندارد و تنها gōr [gwl] «گورخر» را ثبت کرده است، پس حلقهٔ فارسیِ میانه در این زنجیره وجود ندارد. ویکی‌واژه «گور» را از فارسی میانهٔ gabr «گودی، حفره» می‌گیرد و آریان‌پور (ص ۴۴۶) آن را زیر واجریشهٔ *GREBH- (پوکورنی ۴۵۵، یعنی «کندن، چال کردن»، خاستگاه grave انگلیسی و Grab آلمانی) می‌آورد. از نظر آوایی هم برای رسیدن از ghorá- به «گور» به یک صورت ایرانی *gaura- «ترسناک» نیاز است که هیچ‌جا گواه ندارد (اوستایی gaura- همان «گورخر» است). نتیجه: ادعای نورایی را پژوهش امروزی نمی‌پذیرد. «گوراب/گورابه» نیز آشکارا ساختهٔ خودِ «گور» است و سرنوشتش به آن بسته است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:210\", \"status\": \"contradicts\", \"note\": \"Horn, Grundriss der neupersischen Etymologie p. 210 (HRN.txt, form-feed block 232, immediately after no. 938 'gōr Wildesel'): 'gōr ,Grab', dagegen, das Geiger neuerdings (Lautl. des Bal. 53) mit ai. ghōrá- ,grausig, furchtbar' verglichen hat, ist nach Nöldeke, Pers. Stud. II, 41 ein semitisches Lehnwort.' The cited page states the very comparison Nourai draws and rejects it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"printed p. 210 (HRN.txt leaf 232)\", \"stance\": \"contradicts\", \"note\": \"'... ist nach Nöldeke, Pers. Stud. II, 41 ein semitisches Lehnwort' — Horn follows Nöldeke against the ghōrá- etymology.\"},\n            {\"src\": \"PHD\", \"where\": \"PHD_pages.txt line 2546 s.v. gōr\", \"stance\": \"contradicts\", \"note\": \"'gōr [gwl | N ~] onager, wild ass.' MacKenzie's only gōr; no Middle Persian word for 'grave' under this shape, so the Old-Iranian→MP→NP chain the chart needs is missing.\"},\n            {\"src\": \"ARY\", \"where\": \"printed p. 446 (pdf page 445; image saved as sources/refs/ocr/ARY/0446.png, transcription 0446.vision.txt)\", \"stance\": \"contradicts\", \"note\": \"Aryanpur's entry 'گور (به چم «قبر»، «آرامگاه») GŪR — TOMB, GRAVE' gives INDO-EUROPEAN '*GREBH-, *GROBH-, *GRABH-, *GHREBH', references 'POKORNY: 455; BARNHART (GRAVE) 447; BUCK 293, 593; ONIONS (GRAVE) 411; SKEAT (GRAVE) 248; برهان قاطع ۱۸۵۰', with the note 'چم پیشین این واژه در زبان‌های ژرمنی: کندن، چال کردن' — i.e. Pokorny's 2. ghrebh- 'dig, bury', not ghou-ro-s. In his introduction (printed p. 40) he still lists گور among the unsolved cases: «واژه‌ی «گور» با واژه‌های انگلیسی GRAVE و آلمانی GRAB همسانی چشمگیری دارد. آیا این واژه‌ها همریشه‌اند؟»\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' printed ~1853 (BQT_v3_pages.txt pdf page 648, lines 47870-47885)\", \"stance\": \"supports\", \"note\": \"Supports the words and glosses only: گوراب '... و گنبدی که بر سر قبرها میسازند ...'; گورابه '... و گنبدی را نیز گویند که بر سر قبرها سازند'. No etymology is offered there.\"},\n            {\"src\": \"WLD\", \"where\": \"Band I p. 636\", \"stance\": \"silent\", \"note\": \"The ghou-ros article lists Indic, Germanic and Slavic only; no Iranian reflex is claimed.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Ghrebh\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *gʰrebʰ₂- 'to seize, grab' (Pokorny 1. ghrebh- 455; Watkins ghrebh-1 'to seize, reach'; Cheung *grabH)\",\n      \"note\": \"Root, language label and gloss all correct, and Nourai has correctly kept it apart from Pokorny's homophonous 2. ghrebh- 'to scratch, dig' (455-456), which is the one that yields grave/Graben/grub. Modern notation writes the root with a laryngeal, *gʰrebʰ₂- (so Wiktionary, following LIV and Cheung's *grabH), because of the Indo-Iranian ā-forms (Skt gṛbhāyati, OP agarbāyam). The Iranian branch of this root is one of the best-documented families in the whole book, and Nourai's chart reproduces it accurately.\",\n      \"note_fa\": \"ریشه، برچسب زبانی و معنا هر سه درست است، و نورایی به‌درستی آن را از همریشه‌نمای دیگرِ پوکورنی (2. ghrebh- «خراشیدن، کندن»، همان که grave و Graben از آن است) جدا نگاه داشته است. در نگارش امروزی این ریشه را با حنجره‌ای می‌نویسند: *gʰrebʰ₂- (ویکی‌واژه بر پایهٔ LIV، و چونگ با صورت *grabH)، چون صورت‌های ā‑دارِ هندوایرانی (سنسکریت gṛbhāyati، پارسی باستان agarbāyam) چنین می‌طلبند. خانوادهٔ ایرانیِ این ریشه از مستندترین بخش‌های کل کتاب است و نمودار نورایی آن را درست بازتاب می‌دهد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%81%D8%AA%D9%86\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:455\", \"status\": \"supports\", \"note\": \"POK_full.txt 'Page(s): 455' block: '...Avestan grab- ,grasp'... npers. giriftan ,gripe', gīrad ,seizes'... Middle Low German grabben... root extension ghrebhā-: Old Indic gṛbhṇāti, gṛhṇāti... Avestan garəwnaiti, gaurvayeiti, Old Pers. garbayaiti ,seizes, conquers'. References: WP. I 652 f.' — Pokorny's 1. ghrebh- 'ergreifen, erraffen' begins on p. 455, exactly as cited.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"printed p. 455 (POK_full.txt, 'Page(s): 455')\", \"stance\": \"supports\", \"note\": \"1. ghrebh- 'to seize, grasp'; explicitly names Av. grab-, OP garbayaiti and npers. giriftan.\"},\n        {\"src\": \"WLD\", \"where\": \"Band I p. 652 (WLD_Bd1_pages.txt leaf 661, running head 'ghrebh-, gherebh-, ghrebhā-')\", \"stance\": \"supports\", \"note\": \"The WP article Pokorny cites as 'WP. I 652 f.' is indeed headed ghrebh-/gherebh-/ghrebhā-.\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt p. 526 (root list), index p. 1565 'GRAB1 ghrebh-1', 'GRASP ghrebh-1'\", \"stance\": \"supports\", \"note\": \"'ghrebh-1. To seize, reach. 1. Zero-grade form *ghṛbh- in Sanskrit gṛbhṇāti, gṛhṇāti, he seizes... 2. Parallel (imitative) Germanic creations with base *grab-, *grap- in: a. Middle English graspen: GRASP; b. Middle Dutch and Middle Low German grabben, to seize: GRAB. [Pok. 1. ghrebh- 455.]'\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt (Mann) s.vv. ghrébō and ghrebsō\", \"stance\": \"partial\", \"note\": \"Mann splits the family: 'ghrébō, iō \\\"seize, grapple\\\" MLG grāpen; ON grápa; Li. grébiu' and 'ghrebsō (ghrebhs-) \\\"seize\\\"... cf. also Av. gərəfš-; LG grapsen, E grasp' — same material, finer subdivision.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"grab; paiti-grab; gerew-âiti, gerewn-aîti; gâuru-ayeiti, garb-âyaiti; ni-gerepto\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Every form but one is exactly right. Av./OP grab- 'to seize' is Bartholomae's verb 'grab- V. \\\"greifen\\\"' (Altiranisches Wörterbuch col. 526, cited as such by Nyberg s.v. griftan) and Cheung's *grabH 'to grab, seize, take' (Etymological Dictionary of the Iranian Verb pp. 119-121). 'gerew-âiti, gerewn-aîti' = the nasal present YAv. gərəβnaiti (Yt 10.13, Y 57.25 garəβnąn); 'gâuru-ayeiti, garb-âyaiti' = the aya-present YAv. gouruuaiieiti / hangouruuaiieiti (Y 10.2) beside OP garba-ya- (imperfect agarbāyam DB 2.4, agarbāya DB 2.88, passive agṛbiya DB 2.73), Kent's Lexicon: 'OP garba-ya- in imf. agarbāyam ... to pAr. *gṛbha-, cf. Skt. gṛbhāyati' — the two stems Pokorny 455 lists side by side. 'ni-gerepto' is YAv. ni-gərəpta-, the ta-participle 'seized, held down', which Gharib quotes as the etymon of Sogdian nayruβ/fs- (Sogdian Dictionary p. 237, entry 5918 'nyrwβs- ... ©Av. nigərəpta ©med. pass. st.'); Nourai's gloss 'to be pressed down' is the Pahlavi-influenced reading of that passive, acceptable if loose. The weak item is 'paiti-grab': Cheung's inventory of Avestan preverb compounds of grabH lists *a-, *uz-, *fra- and *ham- only, not *pati-, and Bartholomae's article does not have paiti.grab-; the compound is securely Old Iranian all the same, since it is continued by MMP pdyr- / BMP padīr- 'accept, receive', Parthian pdgyrw-, Sogdian ptyrβ-/pcyrβ- 'to accept, receive, understand' — so *pati-grab- belongs on the chart, but under a reconstructed Old Iranian label rather than as an attested Avestan word.\",\n          \"derivation_fa\": \"همهٔ صورت‌ها جز یکی دقیق‌اند. grab- اوستایی/پارسی‌باستان همان فعلی است که بارتولومه در ستون ۵۲۶ «فرهنگ ایرانی باستان» با معنی «گرفتن» آورده و چونگ آن را *grabH «گرفتن، ستاندن» بازسازی کرده است (فرهنگ ریشه‌شناختی فعل ایرانی، ص ۱۱۹–۱۲۱). «gerew-âiti / gerewn-aîti» همان ستاک خیشومیِ اوستایی متأخر gərəβnaiti است، و «gâuru-ayeiti / garb-âyaiti» ستاک aya‑دارِ gouruuaiieiti اوستایی در کنار garba-ya- پارسی باستان (ماضی نقلی agarbāyam در بیستون، و مجهول agṛbiya). کنت در واژه‌نامهٔ خود می‌نویسد: «OP garba-ya- ... to pAr. *gṛbha-, cf. Skt. gṛbhāyati». «ni-gerepto» همان ni-gərəpta- اوستایی است؛ قریب در «فرهنگ سغدی» (ص ۲۳۷، مدخل ۵۹۱۸) صورت سغدی nyrwβs- را از همین Av. nigərəpta می‌گیرد. تنها صورتِ سست «paiti-grab» است: چونگ در فهرست پیشوندهای اوستاییِ این فعل *pati- را نمی‌آورد و بارتولومه هم مدخل paiti.grab- ندارد؛ ولی این ترکیب به‌یقین ایرانیِ باستان است، چون در فارسی میانه padīr-، در پارتی pdgyrw- و در سغدی ptyrβ- «پذیرفتن» دنبالهٔ آن است. پس باید آن را «ایرانی باستان بازسازی‌شده» برچسب زد، نه «اوستایی گواه‌دار».\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:455\", \"status\": \"supports\", \"note\": \"Pokorny p. 455: 'Avestan grab- \\\"grasp\\\" ... gaurvayeiti ... participle Perf. Pass. garapta-'; and in the root extension ghrebhā-: 'Avestan garawnaiti, gaurvayeiti, Old pers. garbayaiti \\\"seizes, conquers, agrees, perceives, understands\\\"' — all four of Nourai's present stems.\"},\n            {\"ref\": \"SOD:237\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, printed p. 237 (SOD_pages.txt form-feed block 304), entry 5918: 'nyrwβs- S — nayruβ/fs ©Av. nigərəpta ©med, pass. st.' — the page Nourai cites is exactly where Av. ni-gərəpta- is quoted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 526 (BRT.txt line 10436; column marker 527 at line 10467)\", \"stance\": \"supports\", \"note\": \"'j., g., p. grab- V. \\\"greifen\\\". Praes. 1 grab-, 11 gərəmnā-, 15 gr̥βa-, 23 garb.ya-, gəurvaya-, 24 gəurvaya- ... Perf. jagaurv-, jayaurv-, hangaurv- ... PPfP. gərəpta-; Inf. gərəbqm', with the Old Persian passages 'xšaθram hya bābirauv hauv agarbāyatā Bh. 1.16', 'bābirum agarbāya' — Bartholomae files Avestan and Old Persian under one lemma, exactly as the chart's combined 'Avestan / Old Persian' node does.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon (KNT.txt lines 568, 2521)\", \"stance\": \"supports\", \"note\": \"'agarbāyam, āgarbīta = -gr̥b-, Skt. agr̥bhāyat, Av. gaurvayat'; 'OP garba-ya- in imf. agarbāyam agarbāya agarbāyatā; to pAr. *gr̥bha-, cf. Skt. gr̥bhāyati'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt lines 8589-8620 (*grabH, pp. 119-121)\", \"stance\": \"partial\", \"note\": \"'*grabH \\\"to grab, seize, take\\\" *AVESTAN: grab- (garab-) ... || (+ *a-) || (+ *uz-) || (+ *fra-) || (+ *ham-)'; presents gərəβnaiti, gouruuaiieiti, gərəptaiieinti, aor. hangrabam, ppp. gərəpta-; *OLD PERSIAN: grab- 'to seize (as possession), seize (as prisoner)' — Kent: 183b. Supports every form except paiti-grab: the *pati- compound is listed only for Middle Persian, Parthian and Sogdian, not for Avestan.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"gereftan «گرفتن»; pazîroftan «پذیرفتن (پذیر ، دلپذیر)»; gero «گرو (گروگان)»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three Persian words go back to Old Iranian *grab- exactly as drawn. (1) گرفتن gereftan < MP griftan, pres. gīr- (MacKenzie: 'griftan, gīr- [OHDWN-tn' ...| M grypt, gyr-, N giriftan, -] take, hold, restrain'), < OP grab-/garbāya-; the ppp. *gr̥pta- gives MP grift > NP -graft-/-reft-, while the present stem gīr- continues *gr̥nā-/gərəβnaiti with regular Middle Persian loss of the nasal infix and ī < *r̥ before the cluster; Hübschmann, Persische Studien pp. 171-172 files it under the anaptyctic i-insertion type: 'giriftan \\\"ergreifen\\\", girau \\\"Pfand\\\" ... ap. grab \\\"ergreifen\\\"'. (2) پذیرفتن pazīroftan < MP padīriftan (Book Pahlavi ptglptn, Manichaean pdyrptn) = *pati- 'back, in return' + grab-, i.e. 'to take towards oneself, receive'; the intervocalic -t- of pati- voiced and lenited to -d- > -z- in the New Persian cluster, and the present stem padīr- > پذیر gives the productive nominals پذیر, دلپذیر. Parthian pdgyrw- and Sogdian ptyrβ-/pcyrβ- 'accept, receive, understand' show the same compound across the Middle Iranian area. (3) گرو gerow 'pledge, collateral' < MP graw [glwb'] 'pledge, security' with its derivative grawgān [glwk'n'] > گروگان 'hostage, pawn'; Mo'in's own footnote in Borhan-e Qate' (printed ~1804) reads 'گرو — ... ارمنی grav (رهن)، پهلوی grav [نوشته می‌شود grw']( رهن)، از پارسی باستان grab-... افغانی grav (رهن). هوبشمان'. The semantics is 'what is taken/held' — the same nominal type as English pledge beside 'take'. Regarding the chart's own NOTE: the SNS:322 claim that gerow comes from garīveh 'neck' (i.e. 'to take responsibility on one's neck') is rejected by every source consulted here — گریوه/گریو goes back to Av. grīvā- 'neck' (Bartholomae col. 527 'j. grivā- f. \\\"Nacken\\\"'; Hübschmann p. 172 'girē \\\"Hals\\\" = zd. grīvā-'), an entirely separate etymon, whereas Pahlavi graw is attested in the sense 'pledge' and is derived from grab- by Mo'in, Hübschmann and Wiktionary alike. Nourai is right to record the claim and right to leave it aside.\",\n          \"derivation_fa\": \"هر سه واژه دقیقاً از *grab- ایرانی باستان می‌آیند. ۱) «گرفتن» از فارسی میانهٔ griftan (ستاک حال gīr-)، از پارسی باستان grab-/garbāya-؛ مکنزی می‌آورد: 'griftan, gīr- ... N giriftan'. اسم مفعولِ *gr̥pta- به grift پهلوی و سپس ‑رفت‌ـ فارسی نو رسیده، و ستاک حال gīr- دنبالهٔ ستاک خیشومیِ gərəβnaiti است که در فارسی میانه پسوند خیشومی را از دست داده است. هوبشمان (ص ۱۷۱–۱۷۲) آن را در بخش «افزودن i میانجی» می‌آورد: «giriftan 'ergreifen', girau 'Pfand' ... ap. grab». ۲) «پذیرفتن» از فارسی میانهٔ padīriftan، مرکب از پیشوند *pati- «باز، در برابر» + grab-؛ ت میان دو واکه نرم و سپس در فارسی نو به ذ بدل شده و ستاک حال padīr- به «پذیر» رسیده که «دلپذیر» و مانند آن از آن ساخته شده است. همین ترکیب در پارتی pdgyrw- و سغدی ptyrβ- «پذیرفتن» نیز هست. ۳) «گرو» از پهلوی graw «رهن، وثیقه» و مشتق آن grawgān «گروگان». حاشیهٔ معین بر برهان قاطع (ص چاپی ~۱۸۰۴) خود می‌گوید: «گرو ... ارمنی grav (رهن)، پهلوی grav ... از پارسی باستان grab-». دربارهٔ یادداشتِ خودِ نمودار: ادعای SNS که «گرو» را از «گریوه = گردن» گرفته است پذیرفتنی نیست؛ «گریوه/گریو» از grīvā- اوستایی «گردن» است (بارتولومه ستون ۵۲۷؛ هوبشمان ص ۱۷۲) و ریشه‌ای جداست، حال آنکه graw پهلوی به معنی «رهن» گواه دارد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%81%D8%AA%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D9%BE%D8%B0%DB%8C%D8%B1%D9%81%D8%AA%D9%86\",\n            \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%88\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:374\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' vol. 1, the پذیر- block (BQT_v1_pages.txt lines 24239-24275): headwords پذیرفتن, پذیرا, پذیرش, پذیرفتار, پذیره with Mo'in's cross-references '۲ - رك: پذیرفتن' and the etymological footnote '(بگرفتن) «اسشق ۷۵۰»', i.e. Mo'in explicitly refers پذیرفتن to گرفتن. Vol. 1 covers آ–ت and p. 374 falls in the پ range, so the citation is in the right place (this scan has no printed-page tags in vol. 1, so the exact page could not be re-read).\"},\n            {\"ref\": \"BQT:1797\", \"status\": \"partial\", \"note\": \"In this scan (BQT_v3_pages.txt) printed p. 1797 = pdf page 592 and carries گرست…گرسنه; گرفتار/گرفتن with Mo'in's footnote stand two pages later, printed p. 1799 (pdf 594): 'گرفتن ... از ریشهٔ پارسی باستان grab, grabāyatiy (بمعنی گرفتن)، اوستایی grab-, gərəwnaiti؛ پهلوی garaftan؛ هندی باستان grabh؛ کردی girtin؛ بلوچی girag, giragh ... هوبشمان ... تاوادیا ... griftan'. Content fully supports the arrow; only the page number is off by two (a printing/edition difference).\"},\n            {\"ref\": \"BQT:1802\", \"status\": \"partial\", \"note\": \"Likewise, گرو with Mo'in's footnote is on printed p. 1804 in this scan (pdf page 599): 'گرو - بکسر اول و فتح دوم، ارمنی grav (رهن)، پهلوی grav [نوشته می‌شود grw'] (رهن)، از پارسی باستان grab-... افغانی grav (رهن). «هوبشمان»'. Substance exactly as Nourai claims; page number off by two.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD_pages.txt lines 2570-2578)\", \"stance\": \"supports\", \"note\": \"'graw [glwb | N giraw] pledge, security. ~īh, ~(a)gān [glwk'n' | M grwg'n, N giraugān] = graw.' and 'griftan, gīr- [OHDWN-tn' < A; glptn', gyl- | M grypt, gyr-, N giriftan, -] take, hold, restrain.'\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt line 8618 ff. (*grabH, p. 120)\", \"stance\": \"supports\", \"note\": \"'*MIDDLE PERSIAN: MMP gyr-, BMP gyl- (OHDWN-) /gir-/ \\\"to take, seize\\\" || (+ *pati-) MMP pdyr- \\\"to take, receive, accept\\\", BMP ptgyl- (MKBLWN-) /padir-/ ... Inf.: MMP pdyrptn, BMP ptglptn /padiriftan/'.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien pp. 171-172 (HUB.txt lines 6063, 6064-6065) and p. 141 (line 5084)\", \"stance\": \"supports\", \"note\": \"'giriftan \\\"ergreifen\\\", girau \\\"Pfand\\\"' … 'ap. grab \\\"ergreifen\\\"; girē \\\"Hals\\\" = zd. grīvā-'; and 'giriftan \\\"ergreifen\\\", paz. griftan Shk. 246, zd. gərəpta- (vgl. bal. girag, ptc. gipta)'. Note that Hübschmann keeps girau 'pledge' with giriftan and girē 'neck' with grīvā- — decisive against the SNS:322 note.\"},\n            {\"src\": \"BQT\", \"where\": \"printed pp. 1799 and 1804 (pdf pages 594, 599)\", \"stance\": \"supports\", \"note\": \"Mo'in's footnotes quoted in ref_check above; گرفتار is likewise derived '[از] گرف (گرفتن) + تار'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sogdian\",\n          \"words\": \"grb\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian γrβ- (Buddhist γrβ-, Christian γrb-, Manichaean and Sogdian-script γrβ-) is the regular continuation of *grab-: Old Iranian *gr̥β-/*grab- gives Sogdian γrβ- with the standard Sogdian lenition of intervocalic/postconsonantal *b to β and the change of initial *g- to γ- before r. Gharib's Sogdian–Persian–English Dictionary, entry 4205 (printed p. 167), spells this out: 'γrβ- B, M, S — γarβ, γorβ ? (γrb-, > γrp-) © <*grb; <*grab; OP garbāya; Av. gərəbya-, Yaghn. γiriv — (to) know, (to) understand, (to) take'. The double meaning Nourai records ('to grab, understand') is real and is the semantic hallmark of this verb in Sogdian: from it are formed γarβāk 'wise', γarβākyā 'wisdom', γarβaw 'knowledge, conscience', γarβē 'knowing' (entries 4212-4230) — the shift 'grasp' → 'comprehend' familiar from Latin comprehendere and English grasp. The *pati- compound ptyrβ-/pcyrβ- 'accept, receive; understand' shows the same double sense. The chart's bare transliteration 'grb' is Gharib's consonantal spelling, not a vocalised form.\",\n          \"derivation_fa\": \"γrβ- سغدی دنبالهٔ منظم *grab- ایرانی باستان است: *b در سغدی به β نرم شده و *g آغازین پیش از r به γ بدل گشته است. قریب در «فرهنگ سغدی» (مدخل ۴۲۰۵، ص چاپی ۱۶۷) می‌نویسد: «γrβ- B, M, S — γarβ, γorβ؟ ©<*grb؛ <*grab؛ پارسی باستان garbāya؛ اوستایی gərəbya-؛ یغنابی γiriv — (to) know, understand, take». دو معنایی که نورایی آورده («گرفتن» و «فهمیدن») واقعی و نشانِ ویژهٔ همین فعل در سغدی است؛ از آن γarβāk «دانا»، γarβākyā «دانایی» و γarβaw «آگاهی» ساخته شده است — همان تحول معنایی «گرفتن ← دریافتن» که در comprehendere لاتین و grasp انگلیسی هم دیده می‌شود. صورت «grb» در نمودار همان املای بی‌واکهٔ قریب است، نه صورت واکه‌دار.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:167\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, entry 4205 on printed p. 167 (SOD_pages.txt form-feed block 233, line 15710 ff.): 'γrβ- B, M, S | γarβ, γorβ ? (γrb-, >γrp-) ©<*grb; <*grab; OP garbāya; Av. gərəbya-, Yaghn. γiriv →γrβ't- | (to)know, (to)understand, (to)take'. Both the meaning pair and the derivation from *grab- are Gharib's own.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"printed p. 167, entries 4205 and 4212-4230 (SOD_pages.txt leaves 233-234)\", \"stance\": \"supports\", \"note\": \"Beside γrβ- itself: 'γrβ'k(str) yarβak(star) wise(r)', 'γrβ'ky' yarβakya wisdom', 'γrβ'w yarβaw knowledge, conscience', 'γrβ'y yarβē knowing' — the 'understand' branch of the verb.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt line 8650 ff. (*grabH, p. 120)\", \"stance\": \"supports\", \"note\": \"'*SOGDIAN: SSogd. γrβ-, BSogd. γrβ-, CSogd. γrb-, MSogd. γrβ- \\\"to take, understand, know, be acquainted with\\\" || (+ *uz-) ... || (+ *pati-) SSogd. ptyr(y)β-, BSogd. ptyrβ-, pcyrβ- \\\"to accept, receive; understand\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Germanic\",\n          \"words\": \"grab\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The Germanic verbal base *grab-/*grap- 'to snatch, seize' — Swedish grabba, Middle Low German and Middle Dutch grabben, grabbelen 'to catch, snatch', MHG grappeln 'to grope', Norwegian dial. grafsa/grapsa, German grapsen — is assigned to this root by Pokorny (p. 455, listing exactly these forms), by Klein ('MDu. grabben, rel. to OS. garva, MDu. garve, OHG. garba \\\"sheaf\\\", lit. \\\"that which is gathered up or together\\\", fr. I.-E. base *gherebh-, *ghrebh-, \\\"to seize\\\"') and by Watkins/AHD, the reference Nourai cites here. The formation is the zero/e-grade *gʰrbʰ-/*gʰrebʰ- with Grimm's Law *gʰ > g and *bʰ > b, so the Germanic shape grab- is phonologically the expected one. One caveat worth recording: Watkins hedges these forms as 'parallel (imitative) Germanic creations with base *grab-, *grap-', i.e. he suspects expressive re-formation rather than straight inheritance, precisely because the -pp-/-bb- geminates of the West Germanic forms are of an expressive type; the assignment to ghrebh-1 is nevertheless unanimous in the handbooks. Also note that the Germanic noun *graba- 'grave' (OHG grab, English grave) belongs NOT here but to Pokorny's 2. ghrebh- 'to dig, bury' — a distinction Nourai keeps.\",\n          \"derivation_fa\": \"ستاک فعلیِ ژرمنی *grab-/*grap- «چنگ زدن، ربودن» — سوئدی grabba، آلمانی سفلای میانه و هلندی میانه grabben/grabbelen، آلمانی grapsen — در همهٔ مراجع زیر همین ریشه جای می‌گیرد: پوکورنی (ص ۴۵۵ همین صورت‌ها را می‌شمارد)، کلاین («MDu. grabben ... from I.-E. base *gherebh-, *ghrebh- \\\"to seize\\\"») و واتکینز/AHD که خودِ مأخذ نورایی است. از نظر آوایی *gʰ در قانون گریم به g و *bʰ به b بدل شده، پس شکل grab- ژرمنی همان صورت مورد انتظار است. یک نکتهٔ احتیاطی: واتکینز این صورت‌ها را «ساخت‌های موازی و آوایی‑نمای ژرمنی» می‌خواند، یعنی گمان می‌برد بازساخته‌ای بیانی باشند نه میراثِ مستقیم، چون دوگانه‌شدنِ ‑bb‑/‑pp‑ در ژرمنی غربی نشانهٔ واژه‌های بیانی است؛ با این حال جای‌گیری آن‌ها زیر ghrebh-1 در همهٔ فرهنگ‌ها یکسان است. یادآوری: نام ژرمنی *graba- «گور» (Grab آلمانی، grave انگلیسی) به این ریشه نمی‌رسد، بلکه به 2. ghrebh- «کندن، دفن کردن» — تمایزی که نورایی رعایت کرده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/grab\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt (root list p. 526): 'ghrebh-1. To seize, reach. ... 2. Parallel (imitative) Germanic creations with base *grab-, *grap- in: a. Middle English graspen, to grasp: GRASP; b. Middle Dutch and Middle Low German grabben, to seize: GRAB. [Pok. 1. ghrebh- 455.]'; index p. 1565 'GRAB1 ghrebh-1'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"printed p. 455\", \"stance\": \"supports\", \"note\": \"'besides Swedish grabba \\\"grapple, pack\\\", Middle Low German grabben, grabbelen \\\"catch fast, heap\\\" (out of it engl. grab, grabble). Middle High German grappeln \\\"grope\\\", Norwegian dial. grafsa, grapsa ... deutsch grapsen'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. grab (KLN_1966.txt line 16500)\", \"stance\": \"supports\", \"note\": \"'grab, tr. and intr. v., to seize suddenly. — MDu. grabben, rel. to OS. garva, MDu. garve, OHG. garba, \\\"sheaf\\\", lit. \\\"that which is gathered up or together\\\", fr. I.-E. base *gherebh-, *ghrebh-, \\\"to seize\\\", whence also OI. gṛbhṇāti ... OSlav. grabiti ... Lith. grebiu, grebti.'\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt s.v. ghrébō\", \"stance\": \"supports\", \"note\": \"'ghrébō, iō \\\"seize, grapple\\\" MLG grāpen, id.; ON (alleged) grápa, id.; Li. grébiu, -ti (2), id.' — the Germanic grab-/grap- family under a ghrebh- lemma.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"grab, grasp\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both English words belong to the Germanic *grab-/*grap- base of the node above, though by different routes and this is worth stating precisely. GRAB is not inherited from Old English at all: it first appears in the 1580s, borrowed from Middle Dutch or Middle Low German grabben 'to grab' in the era of intensive Dutch–English maritime contact (Etymonline: 'grab (v.) 1580s, from Middle Dutch or Middle Low German grabben \\\"to grab\\\" ... PIE root *ghrebh- (1) \\\"to seize, reach\\\"'); the noun grab and grabble are later English formations on it. GRASP is native but irregular: Middle English graspen 'to reach, grope, feel around' (mid-14c.), most probably a metathesis of *grapsen, from an unrecorded Old English *græpsan, from Proto-Germanic *grap-, the s-extension seen also in Low German grapsen and (per Mann) in *ghrebhs- with Armenian gerpem and Av. gərəfš-. Klein and Skeat file both under the same base as gripe/grip (Skeat s.v. Gripe: 'Allied to grab, grasp. (√GARBH)'). So Nourai's Germanic→English arrow is right in substance; only 'grab' is a loan within Germanic rather than a direct inheritance.\",\n          \"derivation_fa\": \"هر دو واژهٔ انگلیسی به همان ستاک ژرمنیِ *grab-/*grap- گرهِ بالا می‌رسند، اما از دو راه که بهتر است تفکیک شود. «grab» اصلاً میراثِ انگلیسی کهن نیست: نخستین بار در دههٔ ۱۵۸۰ پیدا می‌شود و وام‌واژه‌ای است از هلندی میانه یا آلمانی سفلای میانه grabben، در دورهٔ داد و ستد دریاییِ فشردهٔ انگلیسی–هلندی (اتیمانلاین: «grab (v.) 1580s, from Middle Dutch or Middle Low German grabben»). «grasp» بومی است ولی بی‌قاعده: انگلیسی میانه graspen (میانهٔ سدهٔ چهاردهم)، به احتمال زیاد از راه قلب (metathesis) از *grapsen و آن از انگلیسی کهنِ ناگواهِ *græpsan، از ژرمنی آغازین *grap-، همان گسترشِ s‑دار که در grapsen آلمانی سفلا و در بازسازیِ *ghrebhs- (با ارمنی gerpem و اوستایی gərəfš-) نزد مان دیده می‌شود. اسکیت هر دو را با gripe/grip زیر یک ریشه می‌آورد. پس پیکانِ ژرمنی ← انگلیسیِ نورایی در اصل درست است؛ تنها باید افزود که «grab» وامی درون‑ژرمنی است نه میراث مستقیم.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/grab\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference of Nourai's own (refs=None); it inherits the AHD citation of its Germanic parent, which was checked there and supports the chain (AHD index: 'GRAB1 ghrebh-1', 'GRASP ghrebh-1').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. grab (KLN_1966.txt line 16500)\", \"stance\": \"supports\", \"note\": \"'grab ... — MDu. grabben ... fr. I.-E. base *gherebh-, *ghrebh-, \\\"to seize\\\" ... Derivatives: grab, n., a sudden grasp, grabber, n.' (Klein's second entry, 'grab, n., a kind of vessel used in the Indian ocean. — VArab. ghrāb, fr. Arab. ghurāb', is a different, Arabic word and is not what the chart means.)\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary p. 186 s.v. Gripe (SKT.txt line ~8007 block)\", \"stance\": \"supports\", \"note\": \"'Gripe (E.) A.S. grīpan ... + Du. grijpen, Icel. grípa, Swed. gripa, Dan. gribe, Goth. greipan, G. greifen, Russ. grabit(e), Skt. grah (older grabh), to seize. (√GARBH.) Allied to grab, grasp.'\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt index p. 1565\", \"stance\": \"supports\", \"note\": \"'GRAB1 ghrebh-1' and 'GRASP ghrebh-1' — both English words assigned to this root.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"Ghrem\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *gʰrem- 'to sound loudly and dully, thunder, growl; be angry' (Pokorny 2. ghrem- 458-459; Watkins ghrem- 'angry')\",\n      \"note\": \"Correct, and correctly disambiguated. Pokorny has two homophonous roots: 1. ghrem- 'scharf worüber reiben, zerreiben, abkratzen' (p. 458) and 2. ghrem- 'laut und dumpf tönen, donnern, grollen, zornig sein' (pp. 458-459). Nourai's gloss 'anger' and his material (Avestan gram-, Germanic grimmaz/grum) belong to the second, which begins on p. 458 — so the citation POK:458 lands on the right lemma. Watkins reduces the gloss to 'ghrem-. Angry.' and Nourai follows him. The only nuance worth recording is that the older sense reconstructed by Pokorny is the acoustic one ('to rumble, thunder', whence OCS gromŭ, Russian grom 'thunder', Greek khremízō 'to neigh'), with 'be angry' a specialisation of 'growl at' that is shared by Iranian and Germanic; the chart's bare 'anger' therefore states the derived sense as if it were the root sense.\",\n      \"note_fa\": \"درست است و درست هم تفکیک شده. پوکورنی دو ریشهٔ هم‌آوا دارد: 1. ghrem- «سخت بر چیزی ساییدن، خراشیدن» (ص ۴۵۸) و 2. ghrem- «بلند و گرفته آوا دادن، غرّیدن، تندری شدن، خشمگین شدن» (ص ۴۵۸–۴۵۹). معنایی که نورایی داده («خشم») و گواه‌هایش (اوستایی gram-، ژرمنی grimmaz/grum) به ریشهٔ دوم مربوط‌اند که از ص ۴۵۸ آغاز می‌شود؛ پس ارجاع POK:458 درست جای‌گیر است. واتکینز نیز معنا را به «ghrem-. Angry» فرو کاسته و نورایی از او پیروی کرده است. تنها نکته آنکه معنای کهن‌تر نزد پوکورنی آواییِ محض است («غرّیدن، تندر»، از همین‌رو gromŭ اسلاوی کهن و grom روسی «تندر»)، و «خشمگین شدن» تحول معناییِ مشترک ایرانی–ژرمنی از «بر کسی غرّیدن» است؛ نمودار معنای ثانوی را همچون معنای اصلی نشانده است.\",\n      \"sources\": [],\n      \"ref_check\": [\n        {\"ref\": \"POK:458\", \"status\": \"supports\", \"note\": \"POK_02.txt line 1733: '2. ghrem- ,laut und dumpf tönen, donnern, grollen, zornig sein'; ghromo-s ,Getöse'. Av. gram- ,ergrimmen, Grimm hegen' ... npers. γaram ,Grimm'; ... aisl. gramr ,ergrimmt, feindlich', ags. gram, as. gram, ahd. gram ... aisl. grimmr ... WP. I 655 f.' The lemma starts on p. 458 (the marker 459 falls later in the article), so the page is right.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"printed pp. 458-459 (POK_02.txt line 1733; POK_full.txt 'Root / lemma: ghrem-2 ... Page(s): 458-459')\", \"stance\": \"supports\", \"note\": \"'2. ghrem- \\\"heavy sound, thunder, grumble\\\"' with Avestan gram-, Greek khremízō, ON gramr, OHG gram, ON grimmr, MHG grummen, OCS gromŭ.\"},\n        {\"src\": \"WLD\", \"where\": \"Band I p. 655 (WLD_Bd1_pages.txt leaf 664, running head 'ghrem- 655')\", \"stance\": \"supports\", \"note\": \"The page where '1. ghrem- „scharf worüber reiben...“' ends and the acoustic/angry ghrem- follows — the article Pokorny abbreviates as 'WP. I 655 f.'\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt p. 528 (root list); index p. 1567 'GRIM ghrem-', p. 1570 'GRUMBLE ghrem-'\", \"stance\": \"supports\", \"note\": \"'ghrem-. Angry. 1. Germanic *grimmaz in: a. Old English grim(m), fierce, severe: GRIM ... 2. Germanic *grum- in Middle Dutch grommen, to mutter angrily ...: GRUMBLE. 3. Suffixed o-grade form *ghrom-o- in Russian grom, thunder: POGROM. [Pok. 2. ghrem- 458.]'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt s.v. ghrem- (1)\", \"stance\": \"supports\", \"note\": \"'ghrem- (1) \\\"roar, ...\\\" Gk. cf. khremetízō \\\"neigh, snort\\\"; MHG grimmen \\\"rage, roar\\\"; ON grimmast; R greméti ... MHG grim(me) \\\"grim, furious\\\"; ON grimmr; OE grimman, grimsian \\\"rage\\\" ... O-gde gram \\\"fierce, raging\\\"'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"gram\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan gram- is a real verbal root, and it is the Iranian witness on which Pokorny's 2. ghrem- rests: Bartholomae, Altiranisches Wörterbuch col. 527, 'j. gram- V. \\\"ergrimmen, Grimm hegen\\\". Praes. 1 grama-. — PPfP. granta-', citing Y 57.28 'vī manō bara gramǝntąm \\\"schaff fort der ergrimmten Anschlag\\\"' and Yt 10.19 etc. 'miθrǝ grantō \\\"angry Mithra\\\"'; Bartholomae adds the comparison himself: 'vgl. np. γaram \\\"Grimm\\\", ahd. gram'. Pokorny 458 repeats it: 'Av. gram- \\\"ergrimmen, Grimm hegen\\\" (nur im Partiz. Präs. grǝmǝntam ... und Partiz. Perf. Pass. granta- aus *ghramita- \\\"ergrimmt\\\")'. The participle granta- < *gram-ta- < *gʰrem-to- shows the regular Avestan development of *-mt- to -nt-. The one small liberty in the chart is grammatical: gram- is a verb 'to become angry', not the noun 'anger', so Nourai's gloss states the abstract for the verbal root; and the form as printed is the bare root, which is how Bartholomae lemmatises it.\",\n          \"derivation_fa\": \"gram- اوستایی ریشهٔ فعلیِ گواه‌داری است و همان تکیه‌گاه ایرانیِ ریشهٔ 2. ghrem- نزد پوکورنی است. بارتولومه در ستون ۵۲۷ می‌آورد: «j. gram- V. \\\"ergrimmen, Grimm hegen\\\"؛ حال: grama-؛ اسم مفعول: granta-»، با شاهدهای yasna ۵۷٫۲۸ («vī manō bara gramǝntąm») و یشت‌ها («miθrǝ grantō»)، و خود می‌افزاید: «vgl. np. γaram \\\"Grimm\\\", ahd. gram». پوکورنی (ص ۴۵۸) نیز همین را تکرار می‌کند و granta- را از *ghramita- می‌گیرد. صورت granta- از *gram-ta- با تحول منظم ‑mt‑ > ‑nt‑ در اوستایی به دست آمده است. تنها آزادیِ کوچکِ نمودار دستوری است: gram- فعل است («خشمگین شدن») نه اسم («خشم»)؛ نورایی معنای مصدری را به‌جای آن نشانده است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:458\", \"status\": \"supports\", \"note\": \"POK_02.txt line 1734: 'Av. gram- ,ergrimmen, Grimm hegen' (nur im Partiz. Präs. grǝmǝntam ,derer, die uns grimm sind' und Partiz. Perf. Pass. granta- aus *ghramita- ,ergrimmt'), npers. γaram ,Grimm''.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 527 (BRT.txt lines 10495-10503)\", \"stance\": \"supports\", \"note\": \"'j. gram- V. \\\"ergrimmen, Grimm hegen\\\". Praes. 1 grama-. — PPfP. granta-. ... vī manō bara gramǝntam \\\"weg schaff den Anschlag derer, die (uns) grimm sind\\\" Y. 57.28; — miθrǝ grantō ... ahurahe (nāml. miθrahe) grantahe ... vgl. np. γaram \\\"Grimm\\\", ahd. gram'; and 'j. gramant- Adj., PPA.: s. gram-'.\"},\n            {\"src\": \"POK\", \"where\": \"printed p. 458\", \"stance\": \"supports\", \"note\": \"Quoted in ref_check; Avestan gram- heads the article's material.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt (grep 'gram-', 'granta')\", \"stance\": \"silent\", \"note\": \"Cheung's Etymological Dictionary of the Iranian Verb has no *gram- lemma of this shape in the searched text — unsurprising, since the verb has no New Iranian continuant that he tracks.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"gozm, gožm «غزم ، غژم»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Persian words exist with the meaning given and the Rudaki verse Nourai quotes is genuine, but the specific form he attaches to Avestan gram- is not the form his own references print. What Pokorny 458 and Bartholomae col. 527 both cite as the New Persian reflex of gram- is 'np. γaram \\\"Grimm\\\"' — i.e. غرم ġaram, not غژم/غزم. That matters phonologically: Old Iranian *gram-/*ghram- yields NP ġaram/garm by ordinary anaptyxis, whereas -žm-/-zm- in غژم requires an extra assibilation that is not a regular Persian sound change; the most one can say is that غژم and غزم are variants of one word which the lexicographers themselves confuse with غرم (Asadi's Loghat-e Fors carries a marginal note on the neighbouring entry غرس reading 'غرس و غزم [صحیح: غرم] خشم باشد', explicitly emending غزم to غرم). The lexical evidence is likewise mixed: Mo'in's Farhang has غزم '(اِ.) خشم، قهر، غضب' — Nourai's gloss exactly — but files غژم separately as a botanical term 'هر دانهٔ میوهٔ انگور که به خوشه متصل است'; Dehkhoda and Amid, on the other hand, give غژم both 'خشم، غضب، قهر' and 'حمله' as well as the grape sense, and Dehkhoda cites precisely Rudaki's 'شیر غژم آورد و جست از جای خویش'; and Asadi Tusi, in the entry Nourai cites, glosses غژم in that very Rudaki line not as 'anger' but as 'هیبت' (awe, dread). So: the root connection Pokorny–Bartholomae draw for a Persian ġaram is sound and this Persian word is very probably the same lexeme, but the equation of the exact form غژم with Av. gram- rests on the Persian lexicographers' variant spellings rather than on a regular sound law, and the gloss 'anger' is only one of the senses attested for it.\",\n          \"derivation_fa\": \"واژه‌های فارسی وجود دارند و معنای «خشم» برای‌شان گواه دارد، و بیت رودکی هم اصیل است؛ اما صورتی که نورایی به gram- اوستایی می‌بندد همان صورتی نیست که مأخذهای خودش چاپ کرده‌اند. پوکورنی (ص ۴۵۸) و بارتولومه (ستون ۵۲۷) هر دو بازماندهٔ فارسی نوِ gram- را «np. γaram ‹Grimm›» می‌نویسند، یعنی «غرم»، نه «غژم/غزم». این تفاوت آوایی مهم است: *gram- ایرانی باستان با میانجی‌گیریِ معمول به ġaram/garm فارسی می‌رسد، حال آنکه ‑ژم/‑زم در «غژم» به دگرگونیِ سایشی‌شدنی نیاز دارد که قاعدهٔ منظم فارسی نیست. بیشترین چیزی که می‌توان گفت آن است که «غژم» و «غزم» گونه‌های یک واژه‌اند که خودِ فرهنگ‌نویسان هم آن‌ها را با «غرم» می‌آمیزند؛ اسدی طوسی در حاشیهٔ مدخل «غرس» می‌نویسد «غرس و غزم [صحیح: غرم] خشم باشد». گواه واژگانی هم دوگانه است: معین «غزم» را «(اِ.) خشم، قهر، غضب» می‌آورد — دقیقاً معنای نورایی — ولی «غژم» را جداگانه اصطلاحی گیاهی می‌داند («هر دانهٔ میوهٔ انگور که به خوشه متصل است»)؛ دهخدا و عمید در برابر، «غژم» را هم «خشم، غضب» و «حمله» و هم «دانهٔ انگور» می‌گیرند و دهخدا همان بیت رودکی را شاهد می‌آورد؛ و اسدی در همان مدخلی که نورایی ارجاع می‌دهد «غژم» را در همین بیت رودکی «هیبت» معنی می‌کند نه «خشم». نتیجه: پیوند ریشه‌ای با احتیاط پذیرفتنی است، ولی برابر نهادن دقیقِ «غژم» با gram- بر گونه‌نویسیِ فرهنگ‌نویسان تکیه دارد نه بر قانون آوایی.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%BA%DA%98%D9%85/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:458\", \"status\": \"partial\", \"note\": \"Pokorny p. 458 does give a New Persian reflex of Av. gram-, but it is 'npers. γaram \\\"Grimm\\\"' (POK_02.txt line 1734) — غرم, not the غژم/غزم of the chart. The root connection is Pokorny's; the exact Persian form is not.\"},\n            {\"ref\": \"MON:2413\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Farsi (MON_part2.txt line 1714): 'غزم : [ = غژم] (اِ.) خشم، قهر، غضب' — the word and Nourai's gloss 'anger', with غژم given as the variant. (The page number could not be checked: the available scan is the 2-vol Adena reprint with its own pagination.) Note that line 1708 lists a homonym 'غژّم [= غزمه = غجمه] (اِ.) (گیا.) هر دانهٔ میوهٔ انگور که به خوشه متصل است'.\"},\n            {\"ref\": \"FRS:187\", \"status\": \"partial\", \"note\": \"Asadi Tusi, Loghat-e Fors: the entry غژم is present (FRS.txt line 13463) and is illustrated by exactly Nourai's verse — 'غژم / هیبت باشد، رودکی گفت: شیر غژم آورد و جست از جای خویش / وآمد آن خرگوش را آلغده پیش' — but Asadi glosses it 'هیبت' (awe, dread), not 'خشم'. A separate entry غرس 'خشم و تندی باشد' carries the variant note 'غرس و غزم [صحیح: غرم] خشم باشد' (FRS.txt lines 8114, 8100 ff.). Page 187 could not be checked: the local scan is Eqbal's 1319 edition, whose pagination differs from the Kharazmi 1365 edition Nourai cites.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 527 s.v. gram-\", \"stance\": \"partial\", \"note\": \"'vgl. np. γaram \\\"Grimm\\\", ahd. gram' — Bartholomae's New Persian comparandum is ġaram, not ġažm.\"},\n            {\"src\": \"MON\", \"where\": \"MON_part2.txt lines 1708 and 1714\", \"stance\": \"partial\", \"note\": \"Supports 'غزم = خشم، قهر، غضب' but separates 'غژم' as a grape-berry word, so Mo'in does not treat the two spellings as one lexeme meaning 'anger'.\"},\n            {\"src\": \"FRS\", \"where\": \"FRS.txt lines 13463-13466 (غژم) and 8100-8114 (غرس)\", \"stance\": \"partial\", \"note\": \"غژم glossed 'هیبت' with the Rudaki verse; the anger sense appears under غرس/غزم with the emendation '[صحیح: غرم]'.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt (grep 'γaram', 'gazm', 'yazm')\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no entry for this word under any of the searched spellings.\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt (grep 'غژم', 'غزم')\", \"stance\": \"silent\", \"note\": \"Aryanpur has no entry for غژم/غزم at all.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Germanic\",\n          \"words\": \"grimmaz, grum\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *grimmaz 'fierce, savage' (< *gʰrem-nó-, with the assimilation *-mn- > *-mm- typical of Germanic) yields OE grim(m), OS/OFris./OHG grimm, ON grimmr 'grim, fierce, hostile'; the o-grade/zero-grade *gram- gives ON gramr 'enraged', OE/OS/OHG gram, MHG gram 'angry', with the causative *gramjan (Goth. gramjan 'to enrage', OHG gremmen); and the zero-grade *grum- gives OHG umbi-grummōn 'to gnaw at', MHG/MLG grummen, MDu grommen 'to mutter angrily, growl', NHG grummen/grummeln 'to grumble, mutter, rumble dully'. Both of Nourai's forms are therefore exactly the two Germanic bases the handbooks set up under this root, and both are cited under it by the reference he gives: AHD/Watkins 'ghrem-. Angry. 1. Germanic *grimmaz ... 2. Germanic *grum- ...'. Pokorny lists the whole set on pp. 458-459.\",\n          \"derivation_fa\": \"ژرمنی آغازین *grimmaz «سهمگین، درنده‌خو» (از *gʰrem-nó- با همگونیِ ویژهٔ ژرمنی ‑mn‑ > ‑mm‑) به grim(m) انگلیسی کهن، grimm آلمانی علیای کهن و grimmr نورس کهن رسیده است؛ گونهٔ *gram- به gramr نورس «خشمگین» و gram آلمانی و انگلیسی کهن، با فعل سببیِ *gramjan (گوتی gramjan «به خشم آوردن»)؛ و گونهٔ صفرِ *grum- به umbi-grummōn آلمانی علیای کهن، grommen هلندی میانه «غرغر کردن» و grummeln آلمانی. پس هر دو صورتی که نورایی آورده دقیقاً همان دو ستاک ژرمنی‌اند که فرهنگ‌ها زیر این ریشه می‌نهند، و مأخذ خودِ او (AHD/واتکینز) نیز همان دو را می‌آورد: «ghrem-. Angry. 1. Germanic *grimmaz ... 2. Germanic *grum- ...». ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt p. 528: 'ghrem-. Angry. 1. Germanic *grimmaz in: a. Old English grim(m), fierce, severe: GRIM; b. Old French grimace: GRIMACE. 2. Germanic *grum- in Middle Dutch grommen, to mutter angrily, probably akin to Middle English grummen, to grumble: GRUMBLE. [Pok. 2. ghrem- 458.]' — both of the chart's forms, under this root.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"printed pp. 458-459 (POK_02.txt line 1735 ff.)\", \"stance\": \"supports\", \"note\": \"'aisl. gramr ,ergrimmt, feindlich', ags. gram, as. gram, ahd. gram ds., mhd. gram ,zornig' ... got. gramjan ,erzürnen' ... aisl. grimmr ,grimmig, feindlich, erregt', ags. afries. as. ahd. grimm ,wild, grausam' ... schwundstuf. ahd. umbegrummōn ,benagen', mhd. mnd. grummen ,brummen, murren', nhd. grummen, grummeln'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. grumble (KLN_1966.txt line 16789)\", \"stance\": \"supports\", \"note\": \"'grumble ... MDu. grommelen, freq. of grommen, \\\"to grumble\\\" ... which stands in gradational relationship to MDu. grimmen, grimmelen, \\\"to grumble\\\", and to OE. grimm, grim, \\\"cruel, fierce, terrible, severe\\\". See grim' — Klein explicitly relates the *grum- and *grimm- bases by ablaut.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt s.v. ghrem- (1)\", \"stance\": \"supports\", \"note\": \"'MHG grimmen \\\"rage, roar\\\"; ON grimmast ... MHG grim(me) \\\"grim, furious\\\"; ON grimmr; OE grimman, grimsian \\\"rage\\\" ... O-gde gram \\\"fierce, raging\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"grim, grumble\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"GRIM is the direct native reflex: Old English grim(m) 'fierce, cruel, severe, painful' < Proto-Germanic *grimma- < *gʰrem-nó-, unbroken into Middle and Modern English (Etymonline: 'grim, Old English grimm ... Proto-Germanic *grimma- ... PIE *ghremno- \\\"angry\\\", perhaps imitative of the sound of thunder'); Skeat s.v. Grim: 'A.S. grim; allied to gram, fierce, angry, furious. + Icel. grimmr, gramr; Dan. grim, gram; G. grimm, gram. Allied to Gk. khremizo, khromos, noise. (√GHRAM, from √GHAR.)'. GRUMBLE reaches English by a detour but from the same base: Middle French grommeler, itself from Middle Dutch grommelen, frequentative of grommen 'to grumble, mutter angrily', beside native Middle English grummen; the -b- is intrusive, as in ramble (Klein). So Nourai's Germanic→English arrow holds for both words, with the qualification that grumble is a 16th-century borrowing of a Germanic word through French rather than an inherited Old English form.\",\n          \"derivation_fa\": \"«grim» بازماندهٔ مستقیم و بومی است: انگلیسی کهن grim(m) «سهمگین، بی‌رحم، سخت» از ژرمنی آغازین *grimma- و آن از *gʰrem-nó-، بی‌گسست تا انگلیسی امروز (اتیمانلاین: «Old English grimm ... Proto-Germanic *grimma- ... PIE *ghremno- \\\"angry\\\"»)؛ اسکیت هم می‌نویسد: «Grim (E.) A.S. grim؛ allied to gram ... + Icel. grimmr, gramr؛ G. grimm, gram». «grumble» از راهی چرخشی ولی از همان ستاک آمده است: فرانسهٔ میانه grommeler، خود از هلندی میانه grommelen، مکررسازِ grommen «غرولند کردن»، در کنار grummen انگلیسی میانه؛ «ب» در آن میانجیِ افزوده است، چنانکه در ramble (کلاین). پس پیکان ژرمنی ← انگلیسی برای هر دو واژه درست است، با این توضیح که «grumble» وامی است از راه فرانسه در سدهٔ شانزدهم نه میراثی از انگلیسی کهن.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/grim\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference of Nourai's own on this node (refs=None); it inherits the AHD citation of its Germanic parent, which was verified there — AHD index p. 1567 'GRIM ghrem-' and p. 1570 'GRUMBLE ghrem-'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary p. 186 s.v. Grim (SKT.txt line 8007 block)\", \"stance\": \"supports\", \"note\": \"'Grim, fierce (E.) A.S. grim; allied to gram, fierce, angry, furious. + Icel. grimmr, grim, gramr, angry; Dan. grim, gram; G. grimm, fury, gram, hostile. Allied to Gk. khremizo, khromos, noise. (√GHRAM, from √GHAR.)'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. grumble (KLN_1966.txt line 16789)\", \"stance\": \"supports\", \"note\": \"'grumble, intr. and tr. v. — F. grommeler, fr. MDu. grommelen, freq. of grommen, \\\"to grumble\\\" ... to OE. grimm ... The b in grumble is intrusive.'\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt index pp. 1567, 1570\", \"stance\": \"supports\", \"note\": \"'GRIM ghrem-'; 'GRUMBLE ghrem-'.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-194.json > /dev/null && echo \"VALID JSON\""
}
```


### [2026-09-06T02:33:36.003Z] TOOL RESULT

```
VALID JSON
```


## [2026-09-06T02:33:39.625Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 tools/verify_check.py 194"
}
```


### [2026-09-06T02:33:41.297Z] TOOL RESULT

```
nodes verified: 11/11
node verdicts: {'confirmed': 8, 'disputed': 1, 'plausible': 2}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 9, 'contradicts': 1, 'partial': 4, 'not_checked': 2}
books consulted: {'supports': 25, 'silent': 5, 'contradicts': 3, 'partial': 4} | by book: {'POK': 4, 'CHEUNG': 4, 'KLN': 4, 'AHD': 3, 'BRT': 3, 'WLD': 2, 'HRN': 2, 'PHD': 2, 'ARY': 2, 'BQT': 2, 'IEC': 2, 'SKT': 2, 'KNT': 1, 'HUB': 1, 'SOD': 1, 'MON': 1, 'FRS': 1}
```


## [2026-09-06T02:33:58.936Z] AGENT

Done — `data/verification/page-194.json` written, valid JSON, `verify_check.py 194` shows 0 PROBLEM lines (11/11 nodes).

**Page 194 (book p. 164) — 3 entries (2 redirects skipped), 11 nodes**
- Root verdicts: 3 confirmed. Node verdicts: 8 confirmed, 2 plausible, 1 disputed.
- Ref checks: 9 supports, 4 partial, 1 contradicts, 2 not_checked (nodes with `refs=None`).

**disputed**
- *Ghou-ro-s* → Persian `gŭr «گور» "grave"` / `gŭrâb`: Nourai's own citation refutes him. Horn, Grundriss p. 210 (the exact page cited) says Geiger's comparison with Skt. ghōrá- is wrong and that gōr "Grab" is, per Nöldeke (Pers. Stud. II 41), a Semitic loanword. MacKenzie has no MP gōr "grave" (only "onager"); Wiktionary derives it from MP gabr "hollow, cavity"; Aryanpur p. 446 files گور under *GHREBH- (Pokorny 455, = English *grave*). Borhan-e Qate' (~p. 1853) does confirm the words and glosses.

**plausible**
- *Ghrebh* → Av./OP node: all forms check out (Bartholomae col. 526, Kent, Cheung 119-21, Gharib p. 237 for Av. ni-gərəpta-) except `paiti-grab`, which Cheung lists only for MP/Parthian/Sogdian, not Avestan — Old Iranian *pati-grab- rather than an attested Avestan word.
- *Ghrem* → Persian `gozm, gožm «غزم ، غژم»`: Pokorny 458 and Bartholomae 527 both give the Persian reflex as **γaram (غرم)**, not غژم; Asadi glosses غژم as "هیبت" in the very Rudaki verse quoted, and Mo'in separates غژم "grape berry" from غزم "خشم". Root link fine, exact form not regular.

**transcription flags / extraction errors:** none — the JSON matches the chart, no page image needed for the data.

**Notes for the owner:** BQT:1797 and BQT:1802 are each ~2 pages low against the local scan (گرفتن is at printed 1799, گرو at 1804); content supports Nourai fully. The chart's SNS:322 NOTE (gerow < garīveh "neck") is rejected by every source — Hübschmann p. 172 and Bartholomae col. 527 keep گریوه with Av. grīvā-, while Mo'in's own BQT footnote derives گرو from OP grab-. ARY p. 446 was read from the page image; transcription saved to `sources/refs/ocr/ARY/0446.vision.txt` (PNG alongside). 7 web pages archived via fetch_source.py.
