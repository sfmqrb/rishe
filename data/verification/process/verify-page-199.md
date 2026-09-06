# Verification process log — verify-page-199


## [2026-09-06T02:16:15.160Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 199 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-199.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-199.json. Write /home/sfmqrb/git/rishe/data/verification/page-199.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 199` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T02:16:16.715Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T02:16:17.437Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T02:16:17.452Z] TOOL RESULT

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


## [2026-09-06T02:16:17.565Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-199.txt"
}
```


### [2026-09-06T02:16:17.586Z] TOOL RESULT

```
1	=== PDF page 199 (book page 169) ===
2	--- entry 0 ---
3	ROOT [Sanskrit] Gôtra : race, origin, substance  (refs HRN:211)
4	#1 (parent #0) [Pahlavi] refs=HRN:211 | gôhar : substance, material
5	  #2 (parent #1) [Persian] refs=BQT:1862; PLA:101; ARK:249; FSF:302 | gohar «گوهر» : substance, anything of value, gem | extra: گهر ، گوهران ، جوهر ، جواهر
6	--- entry 1 ---
7	ROOT [Indo-European] Gras : to eat  (refs POK:404)
8	#1 (parent #0) [Greek] refs=POK:404 | gangraina, gagrajna : decay of tissue (in a limb)
9	  #2 (parent #1) [Arabic] refs=BQT:1339 | 
10	    #3 (parent #2) [Persian] refs=MON:2383 | ğânqrâyâ «غانقرایا» : gangrene | extra: غانقرایا
11	  #4 (parent #1) [Latin] refs=AHD:542 | gangraena
12	    #5 (parent #4) [English] refs=None | gangrene
13	--- entry 2 ---
14	ROOT [Indo-European] Gredh : to walk, go  (refs POK:456)
15	#1 (parent #0) [Avestan / Old Persian] refs=POK:456: FFD:71 | aiwi-grad-mahi : we begin ; gerezdi : agreement ; grâ : to lean toward
16	  #2 (parent #1) [Pahlavi] refs=FFD:71 | grây : to lean toward
17	    #3 (parent #2) [Persian] refs=FFD:71; BQT:1783; VSF:16 | grâyîdan «گراییدن» : to be inclined | extra: گرایستن ، گرای ، گرایش
18	#4 (parent #0) [Latin] refs=POK:456 | gradi, gressus : to walk, go ; gradus : step
19	  #5 (parent #4) [French] refs=AHD | grade ; congres
20	    #6 (parent #5) [Persian] refs=MON:3102,3212 | kongereh 2 «کنگره ۲» : congress | extra: گراد ، سانتیگراد
21	    #7 (parent #5) [English] refs=AHD | grade ; congress ; centigrade ; degree ; gradient
22	  #8 (parent #4) [English] refs=AHD | aggressive ; progress ; regression ; ingredient ; graduate
23	--- entry 3 ---
24	ROOT Greios -> redirect to Glei
25	--- entry 4 ---
26	ROOT Greno -> redirect to Ger 2
27	--- entry 5 ---
28	ROOT Gu -> redirect to Gěu 1
29	--- entry 6 ---
30	ROOT Ğuěl -> redirect to Dhogh
31	
```


## [2026-09-06T02:16:20.816Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-199.json",
 "description": "Read source JSON for page 199"
}
```


### [2026-09-06T02:16:20.862Z] TOOL RESULT

```
{
  "pdf_page": 199,
  "book_page": 169,
  "entries": [
    {
      "root": {
        "name": "Gôtra",
        "lang": "Sanskrit",
        "refs": "HRN:211",
        "gloss": "race, origin, substance"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "HRN:211",
          "words": [
            {"translit": "gôhar", "gloss": "substance, material", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1862; PLA:101; ARK:249; FSF:302",
          "words": [
            {"translit": "gohar", "gloss": "substance, anything of value, gem", "script": "گوهر"}
          ],
          "script_extra": "گهر ، گوهران ، جوهر ، جواهر",
          "note": null,
          "quote": {
            "text": "جوان بود و از گوهر پهلوان - خردمند و بیدار و روشنروان",
            "poet": "Ferdowsî"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Gras",
        "lang": "Indo-European",
        "refs": "POK:404",
        "gloss": "to eat"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:404",
          "words": [
            {"translit": "gangraina, gagrajna", "gloss": "decay of tissue (in a limb)", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "BQT:1339",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:2383",
          "words": [
            {"translit": "ğânqrâyâ", "gloss": "gangrene", "script": "غانقرایا"}
          ],
          "script_extra": "غانقرایا",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Latin",
          "refs": "AHD:542",
          "words": [
            {"translit": "gangraena", "gloss": null, "script": null}
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
            {"translit": "gangrene", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gredh",
        "lang": "Indo-European",
        "refs": "POK:456",
        "gloss": "to walk, go"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:456: FFD:71",
          "words": [
            {"translit": "aiwi-grad-mahi", "gloss": "we begin", "script": null},
            {"translit": "gerezdi", "gloss": "agreement", "script": null},
            {"translit": "grâ", "gloss": "to lean toward", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "FFD:71",
          "words": [
            {"translit": "grây", "gloss": "to lean toward", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "FFD:71; BQT:1783; VSF:16",
          "words": [
            {"translit": "grâyîdan", "gloss": "to be inclined", "script": "گراییدن"}
          ],
          "script_extra": "گرایستن ، گرای ، گرایش",
          "note": null,
          "quote": {
            "text": "گهی دل برفتن گرایش کند - گهی خواب را سرستایش کند",
            "poet": "Nezâmî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:456",
          "words": [
            {"translit": "gradi, gressus", "gloss": "to walk, go", "script": null},
            {"translit": "gradus", "gloss": "step", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {"translit": "grade", "gloss": null, "script": null},
            {"translit": "congres", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:3102,3212",
          "words": [
            {"translit": "kongereh 2", "gloss": "congress", "script": "کنگره ۲"}
          ],
          "script_extra": "گراد ، سانتیگراد",
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "grade", "gloss": null, "script": null},
            {"translit": "congress", "gloss": null, "script": null},
            {"translit": "centigrade", "gloss": null, "script": null},
            {"translit": "degree", "gloss": null, "script": null},
            {"translit": "gradient", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "aggressive", "gloss": null, "script": null},
            {"translit": "progress", "gloss": null, "script": null},
            {"translit": "regression", "gloss": null, "script": null},
            {"translit": "ingredient", "gloss": null, "script": null},
            {"translit": "graduate", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Greios", "redirect": "Glei"},
      "nodes": []
    },
    {
      "root": {"name": "Greno", "redirect": "Ger 2"},
      "nodes": []
    },
    {
      "root": {"name": "Gu", "redirect": "Gěu 1"},
      "nodes": []
    },
    {
      "root": {"name": "Ğuěl", "redirect": "Dhogh"},
      "nodes": []
    }
  ]
}
```


## [2026-09-06T02:16:21.497Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T02:16:21.551Z] TOOL RESULT

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


## [2026-09-06T02:16:48.406Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['HRN','BQT','PLA','ARK','FSF','POK','MON','AHD','FFD','VSF','KLN','SKT','LEW','LAT','ARY','CHEUNG','PHD','BRT','WLD','IEC','SYN']:\n    v=d.get(k)\n    print('==',k,json.dumps(v,ensure_ascii=False)[:700])\n\""
}
```


## [2026-09-06T02:16:48.432Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && sed -n 1,60p data/verification/page-124.json"
}
```


### [2026-09-06T02:16:50.108Z] TOOL RESULT

```
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
== ARK {"title": "M.H. Rokn-zadeh Adamiyyat, Arkan-e Sokhan, Sharq 1347/1968", "kind": "catalog", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}
== FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page 
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/ref
== VSF {"title": "K. Mehravand, Vazhe-sazi dar Zaban-e Farsi, Rasti 1349/1970", "kind": "none", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== CHEUNG null
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
```


### [2026-09-06T02:16:50.158Z] TOOL RESULT

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
{
  "pdf_page": 124,
  "book_page": 94,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "entries": [
    {
      "entry": 0,
      "root": "Dhě 2",
      "verdict": "confirmed",
      "modern_form": "PIE *dʰeh₁- 'to put, place; to do' (Pokorny 235-239 dʰē-2; Watkins/AHD dhē-¹)",
      "note": "The root box is right on all three counts. Pokorny's own lemma reads 'Root / lemma: dʰe-2, Meaning: to put, place, say' with 'Page(s): 235-239', so Nourai's 'Dhě 2 : to do, set' with POK:235 reproduces Pokorny's numbering and gloss exactly; Watkins in the AHD appendix has 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235]', and Wiktionary's reconstruction page glosses *dʰeh₁- 'to do; to put, place'. The Iranian material of the chart is likewise Pokorny's own: 'with full grade Avestan Old pers. dāta-', 'Avestan ni-δaiti- „laying down, putting away, hiding“', 'Avestan gao-δi- / gao-δana- „milk container“', 'Avestan dāman-, dąman- n. „site, creature“'. Three things in Part 1 need correcting rather than the root itself. (1) The Avestan mouth-veil is paiti.dāna-, not 'paiti-dâma' (node #3) — a misprint in the printed book, and one that Mo'in's footnote on the very page Nourai cites (Borhān p.418) refutes. (2) apa-dāna- (node #6) is Old Persian, not Avestan, and means 'palace, columned hall'; 'the concealed part of a palace' is Kent's etymological comparison with Skt. apadhā-, not the word's attested sense. (3) Pahlavi dast-war (node #13) does not belong to this root at all: Horn p.127, the page Nourai cites, and Nyberg II 61 both derive it from the root daṇs-/dąh- 'to teach', and Wiktionary offers only *dasta-bara- 'hand-bearer' or *danh- 'to teach'. A fourth, smaller point: the gloss 'to settle, to give' on node #11 mixes this root with PIE *deh₃- 'to give', a distinction Nourai's own reference FFD:52 (Abolghasemi p.52) draws explicitly. Two of the four boxes on the Persian side, the Sogdian box and both of the Persian outcomes of the law-branch check out completely, and Gharib's Sogdian entry γwδʾak even carries the Avestan etymology Nourai draws.",
      "note_fa": "خودِ ریشه کاملاً درست است: پوکورنی در صفحات ۲۳۵–۲۳۹ مادهٔ dʰē-2 را با معنای «نهادن، قرار دادن» آورده و واتکینز در پیوست فرهنگ American Heritage همین را می‌گوید؛ مواد ایرانی نمودار (dāta-، ni-δaiti-، gao-δana-، dāman-) هم عیناً از همین مادهٔ پوکورنی است. سه لغزش در بخش یکم هست: ۱) صورت اوستایی «پنام» paiti.dāna- است نه paiti-dāma — خطای چاپی کتاب؛ ۲) apadāna پارسی باستان است نه اوستایی و معنایش «کاخ، تالار بار» است؛ ۳) پهلوی dastwar هیچ ربطی به این ریشه ندارد و هرن (ص ۱۲۷) و نیبرگ (ج۲ ص ۶۱) آن را از ریشهٔ daṇs-/dąh- «آموختن» می‌گیرند. نکتهٔ کوچک‌تر آنکه معنای «دادن» در خانهٔ ۱۱ متعلق به ریشهٔ دیگر *deh₃- است و ابوالقاسمی در همان FFD:52 این دو را جدا کرده است. در مجموع، ادعای نورایی دربارهٔ خودِ ریشه درست است.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-"
      ],
      "ref_check": [
        {
          "ref": "AHD:1512",
          "status": "supports",
          "note": "Watkins's Indo-European appendix (local file AHD_watkins1985.txt line 375): 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235.]' — the same list Nourai cites by its 1975 New College page 1512 (roots are alphabetical over pp.1505-1550, so 'dhē-' falls in the right place); the copy on disk is the 1985 standalone reprint with different pagination."
        },
        {
          "ref": "POK:235",
          "status": "supports",
          "note": "POK_full.txt lines 22276-22510: 'Root / lemma: dʰe-2 / Meaning: to put, place, say' ... 'References: WP. I 826 ff ... Page(s): 235-239'."
        }
      ],
      "consulted": [
        {
          "src": "POK",
          "where": "pp.235-239, dʰē-2",
          "stance": "supports",
          "note": "supplies not only the root but every Iranian form of the chart: 'Avestan Old pers. data-', 'Avestan ni-δaiti- f. „laying down, putting away, hiding“', 'Avestan gao-δi- „milk container“', 'Avestan gao-δana- n. „milk container“', 'Avestan daman-, dąman- n. „site, creature“'."
        },
        {
          "src": "WLD",
          "where": "Bd. I pp.826-830 (p.828)",
          "stance": "supports",
          "note": "the parent article of Pokorny's; p.828 carries 'av. ni-δaiti- f. „das Niederlegen, Ablegen, Verbergen“', 'Ai. dhāna-m „Behälter“ ... av. gao-dana- n. „Milchgefäß“', 'av. dāman-, dąman- n. „Stätte, Wohnstätte; Geschöpf“'."
        },
        {
          "src": "AHD",
          "where": "Watkins 1985, s.v. dhē-¹",
          "stance": "supports",
          "note": "'To set, put. Contracted from *dheə.' Same gloss as Nourai's 'to do, set'."
        },
        {
          "src": "Wiktionary",
          "where": "Reconstruction:Proto-Indo-European/dʰeh₁-",
          "stance": "supports",
          "note": "'*dʰeh₁- (perfective): to do; to put, place.'"
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Avestan",
          "words": "ma[n]dz-dha; ahura-mazdha",
          "verdict": "confirmed",
```


## [2026-09-06T02:16:56.634Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN grep gauhar/gohar ===\"\ngrep -n -i -E 'gauhar|gôhar|gohar|gōhr|gotra' HRN.txt | head -30\necho \"=== HRN page 211 (leaf=printed+21 => leaf 232, 0-based) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==233' HRN.txt | head -60"
}
```


### [2026-09-06T02:16:58.195Z] TOOL RESULT

```
=== HRN grep gauhar/gohar ===
=== HRN page 211 (leaf=printed+21 => leaf 232, 0-based) ===
mmtmmmmmmm^mmmmi^^^m^^^
— 211 —
945. göSe 'Winkel, Ecke .
KäS. gm.
aw. *gaosaha-.
kurd. güi, güse 'Winkel*; bei. LW. gösak (127).
de Lagard e, Ges. Abb. stellt auch küsk *Kiosk'
hierher, das, im türkischen Munde zu kföik geworden,
als kuSk und kü§k zu den Persern zurückgewandert
sei ; arab. LW. jausäq, syr. LW. pK'i;! *Kiosk' sprechen
dafür, phlv.-päz. küSk bezw. köSk (PP61.) als späte
Form nicht dagegen.
^46. gün 'Farbe; Art und Weise*, güne,
ap. 'Podo]y(wvrj, 'AXojyovvrj; aw. goona- *Farbe'; phlv.
günak, gün, arm. LW. goin^),
afy. LW. yüna,
Vergl. ctln (No. 450), zeryün (No. 661); ebenso
äderyün, humäyün (d. i. Humä + gün) und loääfwe,
947. güh *Schmutz, Kot'.
aw. güd-a- in güSö.lvareta- *im Schmutz kriechend*,
matlgü&a-; phlv. güh in gühvart {\d. 14, 16); skr.
gütha- Exkremente*; arm. ku 'Mist' (H. No. 149); ksL
got>tno,
kurd. gü 'Exkremente'; afy. yul; bei. n. gtd^ (436);
wa/. g'w, jrf, kasm. gUs,
V
948. göher 'Edelstein ; Materie, Ursprung, Geschlecht (Sahn.
I, 149 Vers 366; 170 Vers 741)*2), arab. LW. jauhar
'Edelstein; Substanz'.
skr. jfö^m- 'Geschlecht, Ursprung*; phlv. göhr bezw.
göhar 'Materie, Substanz'.
Die Bedeutung 'Edelstein* ist erst sekundär; sie
findet sich noch nicht im Mittelpersischen ausser an
einigen späten Stellen.
*) Dass arm. ffofn persisohes LW. ist, beweist sicher goinagoin
'bunt* — np. gündgün.
*) äshn. II, 765 Vers 10 folgg. wird goher im Gegensatz zu
nizlid als die von Gott in den Menschen gelegte gute Natur definiert.
14*
```


## [2026-09-06T02:16:59.043Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD gwhl / gohr ===\"\ngrep -n -i -E 'g[oō]hr|gwhl|gōhr' PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB ===\"\ngrep -n -i -E 'gōhr|gohr|gwhl' NYB_vol2_glossary.txt | head -20\necho \"=== HUB ===\"\ngrep -n -i -E 'gauhar|gōhr|gohar' HUB.txt | head -20"
}
```


### [2026-09-06T02:16:59.125Z] TOOL RESULT

```
=== PHD gwhl / gohr ===
PHD.txt:380:gawazn [gw’sn' | N ~] deer. gawdar [0011 | N ~] calf. ģāw-dumb [g'bdwmb | N —dum] horn, trumpet. ģāw-mēš [TWR Amyš | N gā(w)mēš] buffalo. £áy-, v. ģādan. Gayómart [g”ywkmlt! = Av. gayó marata | (M gyhmwrd), N ~] the First Man. gaz [gc | N ~] tamarisk. gaz-, —išn, v. gazidan. gazag [gc’k'] biting. ģāzar [g'cl | N gázur] fuller, washerman. £azdum [gcdwm | N každum!] scorpion; astr. Scorpio. £azidag [ezytk! | N gazid] poll-tax. gazidan, gaz- [gc-, gz-ytn! | N ~] bite, sting. ~išn: biting. gëg [gdk' | M gyyg] thief. gēhān [gy)?>n! | = M, N gihān, jahān] world. ~ig [-yk'] worldly, mortal. -ģēn [-k(y)n! | M -gyn, N -gin] suffix forming adjectives of quality. gês [гуз | (M gyswg, N gēsū)] curls, locks. £étig [gytyk, gytydy | M gytyg, N géti] 1. the material world; 2. worldly. ~ig [-yk'] worldly. gil [ТУМА < A tym; gl | N ~] clay. gilag [g(y)lk! | N gila] complaint, lamentation. —-Obàr [wp] swallowing complaint, suffering in silence. ģilēn [T YN Ayn! | N gilin] (made of) clay. gilistag [g/ystk!] home, dwelling of demons. gir-, ~iSnig, v. griftan. gird [git! | M gyrd, N ~] round, circular; gathered. (9) — āmadan: gather, collect (intr.). — kardan: gather, collect (tr.). ~ih: roundness. girdag [gitk' | N ~a] disk, round. gisnag [gink' | P gyfng] short, small. ģišnīz [ginyc | N —] coriander. giyā(h) [gy^h, gy^h | (M gy'w), N ~] grass. ~izag [-yck'] a straw, blade of grass. gizistag [gcystk' | J w/Bzsth] accursed, hateful. gogird [оо | M gwgyrd, N ~] sulphur. ~ӧтапа [-’wmnd] sulphurous. gohr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage. goóhrag [gwhlk'] = göhr. ~-danag [-d^m k!] physicist. 1g6hrig [gwhlyk'] natural, essential. *ģūhrīg [gw(’)hlyk'] equivalent, substitute, indemnity,
PHD.txt:392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
PHD.txt:510:~ pazd- : blow, play the flute. *nāydāģ [nywt’k'] deep, unfordable, navigable. nayestàn [KN Y Ast^n! | N ~] reed-bed, cane-brake. nāyīzaģ [»vck! | N ~a] small reed, straw. nay-sray [rds d] flautist. nazd [nzd | = M, N ~] near. nazdik [nzdyk! | = M, N ~] near. ~ih: proximity. nazdist [x3dst'] first. nàzišn [x*cšn! | N nāsi$] 1. boasting; 2. kindness. nàzuk [n’cwk! | (M wzwg), N ~] tender, gentle; fickle. né [L4 < AP | M ny, N na] no, not. nék [nywk! | M nyk, N ~] good, beautiful. ~th: goodness. nék-góhr [nywk gwhl] good-natured, virtuous. ~ih: goodness, virtue. nēkēģ [nywhkwk! | M nyyquiw!, IN neho] == пёк. nem [PRG < А plg; nym | = M, N —] half. ~ag [nymk! | N ~a] half, side, direction. ~-аѕр [5р] centaur; astr. Sagittarius. ~-rōz [-lwe | M -rwe, N ~] midday, south. ~-tan [-tn' | N ~] middle of the body. nérang [nylng | N <] incantation, charm, spell. пёгӧб [nylwk! | M nyrwg, N nero] strength, power. ~omand [-’wmnd] strong, powerful.
PHD.txt:536:pa(č)čēn [pcgn!] copy. *pa(č)čībāg [pcyp k', PWNe- | N *pajiw] *deceptive. ^h : deceit, hypocrisy. *pa(č)čībāy- [pcyp'd-, PWNc-] deceive. pad [PWN, for *pty | M pd, N pa] to, at, in, on. pad- [pt- | M *pd-) fall. padam [pd”m | (IN pandm)] mask for the mouth, worn by a celebrating priest. !Ipádan, pày- (UIN TLWN-tn! < А V ntr; Ptn, pd- | M pd, p’y-, N páyidan] protect, watch, defend. *pádan, pāy- [N TLWN-tn!, etc.] stand, wait. pādāšn [p?td?fn! | M p’d’syn, N pàdàs] reward, retribution. padēx [ptyhw'] flourishing, prosperous. ~ih: prosperity. padéxénidan, padéxén- [ptyhwyn-ytn'] make flourish, prosper. pādēz [p'tyc | M p'dyz, N pāyēz] autumn. pad-góhr [PW Ngwhl] т. jewelled; 2. of good stock, well-born. padifrah [p’tpl’s | M p'dypr?h, N *pādafrāh] punishment, retribution. padir-, ~išn, v. padiriftan. padirag [ptylk' | M pdyrg, N paóira] towards, against, counter-. (6) — madan: come to mect. ~ih: meeting, opposition.
PHD.txt:605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
PHD.txt:1802:essential gohrig, madagig, madagwar, madayan.
PHD.txt:2364:ill-born wad-gohr | -toóhm.
PHD.txt:2414:indemnity gohrig.
PHD.txt:2640:lineage gohr(ag).
PHD.txt:2682:low-born wad-gohr | -tóhm.
PHD.txt:4230:virtuous даһа, hunarāwand, kir- bagig, nék-gohr.
PHD.txt:4705:рапа, (пет!) poy- penih pus | frazand frazandih panir pondik pēyišnīg pad!, pen padgohr padnérog
PHD.txt:5121:wadgohr wider-
PHD.txt:5468:gūhragdānāg gohrag dwāzdahān dwāzdah duxt, Just 1-*dūxtun duxtar ldaw-, gūw- gūwāg 12а} dwàr- dwārīdan dwiristan dwārišn jy)
PHD_mackenzie.txt:2487:gawazn                                   36                              gOhrig
PHD_mackenzie.txt:2533:gOhr [gwhll M gwhr, N gauhar] substance, essence, nature; jewel; stock,
PHD_mackenzie.txt:2535:gOhrag [gwhlk 1] = gOhr.
PHD_mackenzie.txt:2537:19Ohrig [gwhlyk l ] natural, essential.
PHD_mackenzie.txt:2538:·gOhrlg [gw(')hlyk l ] equivalent, substitute, indemnity.
PHD_mackenzie.txt:2750: ham-gOhr [hmgwhl I M hmgwhr] of the same substance or nature,
=== NYB ===
1687:göhr [gwhl] 1. gem, jewel 1218. 118°; adj. pat-~ set with gems 6°. — 2. substance 4114-24, 492.10.25.27 433.18, 787.12, 791.2, 928-16, 9312, 1098; adj. pat-~ of noble birth 698. — MPrs. gwhr ‘substance’ (A- H II); Paz. NP göhar. Cf Bailey, BSOS VI, 1930, 82; ZP 83. — V. also ham-göhr.
1688:Göhram [gwhlm] n. pr. 11323. — Cat. 39.42.
1832:ham-göhr [hmgwhl] of the same sub- stance 88%, — MPrs hmgwhr (A-H II).
2281:. he whose virtue and sin are equal 7924-25; seldom % ke: cigon mart-ē ké-§ vēhēh veš u ēvak i ke vēhēh kam as a man whose goodness preponderates and an- other whose goodness is deficient 96°’ ; — it cannot be governed by a prep.; in such cases, a) the prep. is placed in the rel. clause and governs a dem. pron. referring to the antecedent: (dätär) ke hac & aštak veh (the Creator) from whom a good Messenger (has come) 5711; ke... hac ēišān ēvak ravēt (the three sons of Zartuxšt) of whom one ... shall appear 7115-16, 181; kē-š pat han urvar bē barēt [YDLWN-x-] by which he removes the plants 569-10; han kas ke yuvat hac či nē vicarét the man without whom you will not get on 416-1’; b) the prep., changed into an adv. and assuming its special form if there exists any, is placed in the rel. clause and may refer directly or through an encl. to kč: hàn ke én x"amn patiš dit the one about whom this dream was dreamt 21-9 (patiš for pat referring to ke); Hutös ke ... 30 haciš zàt H. of whom 30 children have been born 24? (haciš for hac); han gàv pem kē tan gohr à Zartuxst avis mat ēstāt the cow-milk into which the bodily element of Z. had entered 4225-26 (avi$ for 0); hamäk cis ke-š martömän rämisn ... haciš everything from which men derive pleasure 10020-21 (haciš for hac referring to ke through the intermedium of the encl. -š in ke-$); han keš pātiyāvandtar kē-š pätix$äych apāk bavēt that religion is most powerful to- gether with which there is royal power (which is joined with royal power) 8018-12 (apak here adv., referring to ké through the intermedium of the enel. in ké-8); béstan-é ke-š hamäk urvarihā u spramīhā andar a garden in which there are all sorts of plants and flowers 105! (ké-§ . . .
2688:Nēvak-gāv [ndwk' TWR?»] n. pr. one of the Ātwiyān (Aspikän) family 47°. névak-gohréh [ndwkgwhlyh] the quality of being of good substance 793.
3571:-š encl. pron., cas. obl. of the pers. pron. 3d p. sg.; regularly attached to the first w. of the sentence, preferably to particles: api-š, adak-iš, be-š, cigon-aš, ka-š, etc., or to a pron., v. ce, 2, ké, sometimes to a w. in the interior of the sentence (406, v.s.v. pat-frācēh; 48°. 914, v. below); if it is attached to a subst. it never depends on it as its poss., but refers to another w. in the sentence; it is never governed by a prep. (single exception 54%, v. s. v. apar); it has an independent form aš (g. v.). It expresses 1. the gen. his, her, its: api-š bar xrat and its fruit is Wisdom 6613; fravahr i Zartuxst api-$ tan gohr Z.’s fra- vashi and his corporeal substance 4226-27; 4-$ his, her, its: tāt matan 1-š 0... 4714; — 2. for, to him (ete.): apt-š... 6 patirak āyēnd go to meet him 741-2; api-š vát-ic hayyār bavet 25°; — 3. dir. obj.: api-š nod be barem 3915; ka-š vir royét x"arét he who believes in it eats 1002; (he said) ku-"'$ man be 6 vahist ne hilom” 3425 (dir. speech aš); — 4. the agent, passim: cigon- aš dit as soon as by him was seen 19!?; ka-š hàn saxtan āšnūt 2219; Pourušāsp hac Zartuzšt, pat višopišn i haciš, -(a)š škujt tarsenit P. was terribly frightened by him (the Karap) because of Z. that he should suffer destruction by him 488-9; still unexplained is the construction in api-š ... šamšēr HDWN-yt' (commonly for pres. girét) u tak BYDWN.x, (com- monly for kunēt, but cf hištan) 2220-21, — Proleptically, anticipating a subst.: cigon- aš dit kanicak as soon as she, the girl, saw 15°; adak-iš mčnit Pouruščisp kü then he, P., thought 40%; api-§ guft, apar apäc vast, Pourušāsp and he, P., returning said 5117-18; — anaphorical, taking up a
4038:vatéh [wtyh] abstr. the evil 62”. vat-gohr [wtgwhl] of evil substance, es- sence; ill-natured, ill-disposed 708. vat-göhröh the quality of being of evil substance 79%.
4343:x"arrah [GDH] a divine essence, a special form of the Eternal Light, a splendour, a glory I. manifested in the gods: one swears by (pat) ~ % Ohurmazd bag u den imāzdēsnān 2117-22-28 (without bag). 2321-22 ; zor u ~ + visp-ākāh spēnāk meno datar Ohurmazd 1063-24, — 2. a cosmic essence 9215.19, — 3. Zartuxst’s divine essence 36-38. 43-45 passim; the elements con- stituting his individuality are his ~, fravahr and tan gohr 433-18; his rdi u ~ 51-52; v. also s: v. purr. — 4. the splen-
5977:gwhr: gohr
=== HUB ===
3369:lauten sollte. Afgh. LW. gauhar *Edelstein, Substanz,
7331:Ueber gohar s. oben p. 96.
8814:gohar 'Ursprung H. 948, oben p. 96; ges^ gesU 'Locken\
9146:Shk. 248), hamgohar *like-natured', hamguna alike', hamkdr
10470:gOhar 96.
```


## [2026-09-06T02:17:14.471Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK gras / gangraina ===\"\ngrep -n -i -E 'gangraina|gangrän|gangrä' POK_full.txt | head -20\necho \"--- lemma gras\"\ngrep -n -E 'Root / lemma: gras|lemma: gras|grēs-|gras-' POK_full.txt | head -20"
}
```


### [2026-09-06T02:17:14.550Z] TOOL RESULT

```
=== POK gras / gangraina ===
--- lemma gras
34441:Root / lemma: gras- : gros-
```


## [2026-09-06T02:17:15.551Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK ghredh ===\"\ngrep -n -i -E 'ghredh|ghrēdh|g?redh-|Page\\(s\\): 456' POK_full.txt | head -30"
}
```


### [2026-09-06T02:17:15.616Z] TOOL RESULT

```
=== POK ghredh ===
20774:alb. drefh {stem *dredh-), Aor. drodha^ turn round, turn together, twine, spin ', alb.- 
33766:Page(s): 456-457
```


## [2026-09-06T02:17:17.950Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '34435,34500p' POK_full.txt\necho \"=====GHREDH=====\"\nsed -n '33700,33780p' POK_full.txt"
}
```


### [2026-09-06T02:17:18.026Z] TOOL RESULT

```
Page(s): 403 



Root / lemma: gras- : gros- 

Meaning: to gnaw, to devour 

Material: Old Indie ^/"ssa/e "gobbles (esp. from animals), devours' {*grasd), grasa-h^ 

mouthful, morsel, bite of food '; 

gr. Ypaw " gnaw, devour ' (= Old Indie grasati) Ypaaric; ' grass, green fodder ' (Attie 
KpaoTK; through assimilation in voieeless internal eonsonanee), yQCJtpk; ' gormandizer, 
gourmand, voraeious eater ', Ypaao(; m. ' smell of a goat: henee, of men ' from *Ypaa-ao(; 
(originally he-goat; billy goat as nibbler, as i^&ioc, : Tpcbyw, TpayeTv), yaaTrip f. 'belly' 
(*Ypaa-Tnp " devourer', eompare Kpaarripiov ' raek, manger (of horse); in pi., bed-posts ', 
assimil. from Ypaar-; yaaTpa " the lower part of a vessel bulging out like a pauneh '); 
redupl. due to a *yay-ypa£iv ' devour ': yayypaiva ' gangrene, the eating uleer '; yp(I)vo(; ' 
eaten out; eroded, hollowed ' {*grds-no-s), ypcbvri "eavity, kneading or dough trough; 
dough tray; huteh ' (eompare ipcbyAri "eave': rpcbyu)); 

Latin gramen {*grasmen) n. " grass, turf; any plant or herb ' (esp. as feed herb); about 
Germanie gras eompare under ghre- 

References: WP. I 657 f., WH. I 616 f. 
Page(s): 404 

Root / lemma: gred- : grod- 

Meaning: to serateh 

Note: Only alb. and Germanie 

Material: Alb. gerruse, gerrese, krus(e)^ rasper' (from its first grade derives Latin grosa 

ds.), to lengthened grade present gerruanj, kruanj, kruj, also gerruej, geruj^ scratch, serape 

' (from *grdd-, Indo Germanie gred-); 

Old Norse krota {*grd-) ' engrave ', ablaut, (with intensive gemination) Old Swedish 
krafta' scratch, serape'. Old High German krazzon. Middle High German Modern High 
German kratzen6s. (Germanie *krattdn), besides /verbs mnl. cretten {ar\d cretsen). 
Middle High German kretzen6s., kretze^ seabies '; 

here with expressive voealism Old High German krizzon. Middle High German kritzen " 
earve, seribble ', also Middle High German krfzen^ draw a eirele ', with seeondary ablaut 
Old High German Middle High German kreiz {* kraita-) " eirele' ("*earved magie eirele '); 
expressive probably also the s-extension in ndd. kratsen, krassen^ scratch, serape'. 



References: WP. I 607, 651, WH. I 622 f., Wissmann Norn, postverb. 175 f. 
Page(s): 405 

Root / lemma: grem- 

Meaning: damp; to sink 

Material: Latin gramiaei. PI. " a viscous liumor, rheum, that collects in the corners of the 

eyes ', oculi grammosi^eye drip; pus in the eye '; 

Old Icelandic Ara/??/'" humid, wet, half-melted (of snow)', perhaps also Gothic qrammiPa^ 
=====GHREDH=====
Frisian gref. Old Saxon graf. Old High German grab^grave'; Old Icelandic grgptrm. " 

graving, grave, burial, funeral ', Old English grseftvn. " sculpture, engraving ' (Germanic 

*graftu). Old Frisian grefti. " ditch, trench, channel ' (Germanic *^/'a/?/), nid. grachtds.. Old 

High German grafti. "monumentum, sculpture, engraving ' (but Old High German gruft\s 

folk etymology reshuffling from gr.-Latin crypta); 

Latvian grebju, grebV hollow out, dig with a chisel; scrape, excavate, seize ', greblism. 
" gouge, type of chisel ' (also rake, see below ghr^^-^ gripe '); 

Old Church Slavic pogrebg, pogreti^bury', Serbo-Croatian grebem, grebsti^ dig, 
scratch, scrape', with prefix po- "bury', Czech (old) hrebu, hrebst/^d'\g, bury', poln. grzebg, 
grzesc^ scratch, scrape, dig, bury'; zero grade Slavic *grbbet/"\n Old Czech brb/'et/' lie 
buried ', nowadays pobrb/t/" bury'; iterative Old Church S\av\c pogrebat/, gr/bat/^bury', russ. 
pogrebatbds., Serbo-Croatian (old) zagribati^ bury', Czech hrebati^ upbraid, rebuke', 
poln. grzebig, grzebac^ curry, scratch, scrape', with po- "bury'; Church Slavic grebent 
"comb', russ. grebent ds., Serbo-Croatian greben^ comb, sting, prick, carding, ridge ', 
Czech breben' comb, garden rake '; 

Maybe alb. {*hreben) kreben ' comb' : Russian: grebeh^ comb'. 

poln. grzebien ds.; Old Church Slavic grobt "grave', Serbo-Croatian grob (Gen. groba), 
Czech hrob, russ. grob{Qer\. groba). 



Maybe alb. graba 'eros\on, hollowing out', also a zero grade noun *graba, grath 'iooth, 
prong (for digging) ', ^/'e/7i/// "thicket'. 

References: WP. I 653 f., Trautmann 96. 
Page(s): 455-456 

Root / lemma: ghred^- 

Meaning: to march 

Material: Avestan a/w/'-garadmah/" we begin, advance, go forward, march, proceed ', 

gsrszd/'-t ' (*lineup =) the captured, gained '; but Middle Indie (Asoka-lnschr.) adh/g/cya' 

initiating, commencing ' = Old Indie adhi-krtya-, S. LeviGA 1912; 

Latin gradior, -f to take steps, step, walk, go, advance ', gradus, -us' a step; a step as 
made, a pace; an approach; a step as climbed, a stair; hence any tier, gradation; a braid of 
hair; abstr., degree, stage; rank, position; milit., station, post', grallae' stilts ' (Latin grad- 
from *ghr^^-, ablaut grade as in Lithuanian gridiju); 

Gothic gnPs (only Akk. Sg. grid) " footstep, grade' (but Middle High German grit' 
footstep ', griten' spread the legs apart ', Modern High German Bavarian gritt, grittenAs. 
and - indeed definitely the /-row belonging - graitein " lock the fingers or legs apart ' belong 
to Germanic *grT-' straddled, gaping ', the strange link so far is missed); 

Lithuanian gridiju, -y//(Juskevicz) " go, wander, err about '. 

Present nasals: 

Old Irish in-grenn-, to-grenn-' pursue ' (-e/7/7-from -n6^-n-, themat. /7-present, 3. 
Sg. *giirn-6'^-ne-t), (common Celtic -ns-, -nt- > -nn-), compare Thurneysen KZ. 63, 1 14f., 
Kuiper Nasalpras. 170 f.; 

Old Church Slavic gr§dg, grgsti' go, come ', russ. grjadu, grjasti' go, march ' etc. 

References: WP. I 651 f., WH. I 615 f., Trautmann 98. 
Page(s): 456-457 

Root / lemma: ghreib- 

Meaning: to grab 

Note: compare also ghrdd^-. 

Material: Gothic greipan^ grasp ', Old Icelandic grfpa' grasp, gripe ', Old English Old 

Saxon grTpan6s., Old Frisian grfpa. Old High German grTfan6s., in addition as iterative 



Old English grapian, Old High German greifon^ caress ', and Norn, agentis Old Icelandic
```


## [2026-09-06T02:17:33.482Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG grāy ===\"\ngrep -n -i -E 'gray|grāy|grāi|garəd|gard-|grd' CHEUNG.txt | grep -i -E 'gray|grāy|grāi' | head -20\necho \"=== BRT garəd / gərəzdi ===\"\ngrep -n -i -E 'g.r.zdi|garədmahi|aiwi-gar|aiwi.gar' BRT.txt | head -20\necho \"=== HRN gerâyîdan ===\"\ngrep -n -i -E 'gräjfden|grâjîdan|gräjîden|grajlden|grâj|gerâj' HRN.txt | head -20"
}
```


### [2026-09-06T02:17:33.590Z] TOOL RESULT

```
=== CHEUNG grāy ===
=== BRT garəd / gərəzdi ===
=== HRN gerâyîdan ===
```


## [2026-09-06T02:17:35.640Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins ghredh ===\"\ngrep -n -i -E 'ghredh|gangrene|gangraena' AHD_watkins1985.txt | head -20\necho \"=== KLN gangrene ===\"\ngrep -n -i -E 'gangrene|gangraena|gangraina' KLN_1966.txt | head -10\necho \"=== LEW gangraena/gradior ===\"\ngrep -n -i -E 'gradior' LEW_1910.txt | head -10"
}
```


### [2026-09-06T02:17:35.732Z] TOOL RESULT

```
=== AHD watkins ghredh ===
526:TRANSFUSE. II. Extended form *gheus-. 1. Germanic zero-grade form *gus- in: a. suffixed form *gustiz in Old Norse gustr, a cold blast of wind: cusT!; b. Icelandic gusa, to gush, perhaps akin to Middle English gushen, to gush: GUSH. 2. Germanic suffixed o-grade form *gausjan in Old Norse geysa, to gush: GEYSER. III. Suffixed form *gheu-ti- in Latin fatilis, “(of a vessel) easily emptied, leaky,” hence untrustworthy, useless: FUTILE. IV. Basic form *gheu- in Greek khein, to pour: CHOANA, CHYLE, (CHYME); CHOANOCYTE, ECCHYMOSIS, PARENCHYMA. [Pok. gheu- 447.] ghéu-. To yawn, gape. Compare ghai-. 1. Germanic suffixed form g6-ma- in Old English goma, palate, jaw: GuM?, 2. Variant form *ghau- in Greek khaos, chasm, empty space, chaos: CHAOS, GAS. [Pok. ghéu- 449.] gheu(e)-. To call, invoke. Suffixed zero-grade form *ghu-to-, “the invoked,” god, in Germanic *gudam, god, in: a. Old English god, god: Gop; b. Germanic *gud-igaz, possessed by a god, in Old English gydig, gidig, possessed, insane: GIDDY. [Pok. ghau- 413.] gh6. Behind, after. Slavic *za in Russian za, by, to: SASTRUGA. [Pok. 26 451.] ghos-ti-. Stranger, guest, host; properly “someone with whom one has reciprocal duties of hospitality.” 1. Basic form *ghos-ti- in: a. Germanic *gastiz in Old Norse gestr, guest: GUEST; b. Latin hostis, enemy (< stranger): HOST?, (HOSTILE). 2. Compound “ghos-pot-, *ghos-po(d)-, “guest-master,” one who symbolizes the relationship of reciprocal obligation (*pot-, master; see poti-), in Latin hospes (stem hospit-), host, guest, stranger: (HOSPICE), (HOSPITAL), (HOSPITALITY), HOST!, (HOSTAGE), (HOSTEL), (HOSTLER). See also xenos. [Pok. ghosti-s 453.] ghow-é-. To honor, revere, worship. 1. Germanic *gaw6n in Old Norse gd, to heed: GAWK. 2. Basic form *ghow-é- in Latin favére, to favor, be favorable: FAVOR, (FAVOR- ITE). [Pok. ghou(é)- 453.] ghré-. To grow, become green. Contracted from “ghreo-. 1. O-grade form “ghré- in Germanic *grd(w)an in Old English gréwan, to grow: GROW. 2. Suffixed o-grade form *ghro-nyo- in Germanic *grénjaz, green, in Old English gréne, green: GREEN. 3. Suffixed zero-grade form *“ghro-so- in Germanic *grasam, grass, in Old English grees, grass: GRASS. [Pok. ghré- 454.] ghrebh-'. To seize, reach. 1. Zero-grade form *ghrbh- in Sanskrit grbhndati, grhndati, he seizes: SATYAGRAHA. 2. Parallel (imitative) Germanic creations with base *grab-, *grap- in: a. Middle English graspen, to grasp: GRASP; b. Middle Dutch and Middle Low German grab- ben, to seize: GRAB. [Pok. 1. ghrebh- 455.] ghrebh-?. To dig, bury, scratch. 1. O-grade form “ghrobh- in: a. Germanic *graban in (i) Old English grafan, to dig, engrave, scratch, carve: GRAVE3; (EN- GRAVE) (ii) Old High German graban, to dig: GRABEN (iii) Old French graver, to engrave: GRAVURE; b. Germanic *grabam in Old English grzf, trench, grave: GRAVE}. 2. Germanic *grub(byan (with secondary ablaut) in Old English *grybban (> Middle English grubben), to dig: GRUB. 3. Germanic *gr6b6 in Middle Dutch groeve, ditch: GROOVE. 4. Perhaps Germanic *greub- in Low German greven, fibrous refuse of tallow: GREAVES. [Pok. 2. ghrebh- 455.] ghredh-. To walk, go. Suffixed zero-grade form ghrdh-yo- in: a. Latin gradi (past participle gressus), to walk, go: GRESSORIAL; AGGRESS, CONGRESS, DEGRESSION, DI- GRESS, EGRESS, INGRESS, PLANTIGRADE, PROGRESS, RE- GRESS, RETROGRESS, TRANSGRESS; b. Latin gradus (< deverbative *grad-u-), step, stage, degree, rank: GRADE; CENTIGRADE, DEGRADE, DEGREE, RETROGRADE. [Pok. ghredh- 456.] ghréi-. To rub. A derivative of gher-4. 1. Germanic *gris-, to frighten (< “to grate on the mind”), in Old English grislic, terrifying: GRISLY. 2. Germanic *grim-, smear, in Middle Dutch grime, grime, akin to the source of Middle English grime, grime: GRIME. 3. Extended form *ghris-
531:gras-. To devour. 1. Germanic *krasjon-, fodder, in Old English cresse, czrse, cress: CRESS. 2. Suffixed form *gras-men in Latin gradmen, “fodder,” grass: GRAMA, GRAMINEOUS. 3. Suffixed form *gras-ter-, ‘the de- vourer,” dissimilated in Greek gastér, stomach, belly: (GASTRIC), GASTRO-, GASTRULA; EPIGASTRIUM. 4. Redu- plicated form “*gar-gr- dissimilated in Greek gangraina, gangrene: GANGRENE. [Pok. gras- 404.]
1218:AEDILE aidh- AEGIS aig- AENEOUS ayes- AEOLIPILE pulé AEPYORNIS OrF- AERIAL wer-2 AERO- wer-2 AEROBE gWei- AERODYNE deu-2 AERONAUT nau-2 AESIR ansu- AESTHETIC au-5 AESTIVAL aidh- AETHER aidh- AFFABLE bha-2 AFFAIR dhé-1 AFFECT! dhé-1 AFFECT? dhé-1 AFFECTION dhé-1 AFFERENT bher-1 AFFIANCE bheidh- AFFIANT bheidh- AFFIDAVIT bheldh- AFFILIATE dhé(i)- AFFIRM dher-2 AFFIX dhigy- AFFLATUS bhié-2 AFFLICT bhiig- AFFLUENT bhleu- AFFORD pert AFFOREST dhwer- AFFRAY  pri- AFFRICATE bhréi- AFFUSION gheu- AFTER apo- AFTERMATH mé-4 AGAIN gagina AGAINST gagina AGALACTIA melg- AGAPANTHUS andh- AGE aiw- AGENDUM ag- AGENT ag- AGERATUM gere-1 AGGLOMERATE gel-1 AGGLUTINATE gel-1 AGGRAVATE gWere-2 AGGREGATE ger-? AGGRESS ghredh- AGGRIEVE gWere-2 AGHAST gheis- AGILE ag-
1340:CELLA kel-2 CELLAR kel-2 CELLARER kel-2 CEMBALO keu-2, kleu-3 CEMENT kae-id- CEMETERY kei-1 CENACLE sker-1 -CENE_ ken-3 CENOBITE gWei-, kom CENOGENESIS ken-3 CENOTAPH dhembh-, ken-4 Cenozoic ken-3 CENSOR kens- CENSUS kens- CENT dekm CENTAL dekm CENTAVO dekm CENTENARIAN dekm CENTENARY dekm CENTENNIAL dekm CENTER kent- CENTESIMAL dekm CENTESIS kent- CENTI- dekm CENTIGRADE ghredh- CENTIME dekm CENTNER dekm CENTO kentho- CENTRIFUGAL bheug-'
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1426:DIET? deiw- DIFFER bher-! DIFFICULTY dhé-1 DIFFIDENT bheidh- DIFFRACTION bhreg- DIFFUSE gheu- DIG dhigw- DIGEST gerere DIGIT deik- DIGNIFY dek-1 DIGNITY dek-1 DIGRESS ghredh- DIKE dhig¥- DILATE stela- DILATORY tela- DILIGENT leg-1 DILUTE leu(@)- DIME dekm DIMENSION mé-2 DIMER (s)mer-2 DIMINISH mei-2 DIMITY mei-4
1444:EGOIST eg EGOTISM EGREGIOUS ger-! EGRESS ghredh- EIDER &ti- EIDERDOWN dheu-! EIDETIC weid- EIDOLON weid- EIGHT oktd(u) EINKORN gre-no-, oi-no- EISTEDDFOD bheue-, sed-' EITHER kWo- EJACULATE yé- EJECT yé-
1553:GAMBOL kamp- GAMBREL kamp- GAMETE geme- GAMMON3 kamp- GAMO- geme- GAMOSEPALOUS geme- -GAMOUS gema- -GAMY geme- GANDER ghans- GANG! ghengh- GANGLING ghengh- GANGLION gel-1 GANGRENE gras- GANGUE ghengh- GANNET ghans- GANOID gau- GAP ghai-
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1567:GREAT ghréu- GREAVES ghrebh-2 GREEDY gher-5 GREEN ghré- GREET gher-2 GREGARIOUS ger-1 GRENADE gre-no- GRESSORIAL ghredh- GREYHOUND gher-3 GRID kert- GRIDDLE kert- GRIDIRON kert- GRIEF gWera-2 GRIEVE gWere-2 GRIM ghrem- GRIMACE ghrem- GRIME ghréi- GRIND ghrendh- Grip! ghreib- GRIPE ghreib- GRIPPE ghreib- GRISAILLE gher-3 GRISEOUS gher-3 GRISETTE gher-3 GRISLY ghréi- GRISON gher-3 GRisT ghrendh- GRIT ghréu- GRIZZLE gher-3 GROAT ghréu- GROATS ghréu- GROCER gWres- GROOVE ghrebh-2 GROPE ghreib- GROSCHEN gWres- GROSS gWres- GROSSULARITE ger-2 GROSZ gWres-
1678:INERTIA ar- INEXORABLE 6r- INFAMOUS bha-2 INFANT bha-2 INFANTRY bha-2 INFARCT bhrekw- INFECT dhé-1 INFELICITY dhé&(i)- INFER_ bher-1 INFERIOR ndher- INFERNAL ndher- INFERNO ndher- INFEST dhers- INFEUDATION peku- INFIDEL bheidh- INFIRM dher-2 INFIRMARY dher-2 INFIX dhigw- INFLAME bhel-1 INFLATE bhié-2 INFLICT  bhiig- INFLUENCE bhieu- INFLUENZA bhleu- INFRA- ndher- INFRACT bhreg- INFRANGIBLE bhreg- INFRINGE bhreg- INFUSE gheu- INGENIOUS gene- INGENUOUS gene- INGEST gerere INGRATE gWere-3 INGRATIATE gWere-3 INGRESsS ghredh- INGUINAL engW- INGURGITATE gWere-4 INHABIT ghabh- INHERE ghais- INHERIT ghé- INHIBIT ghabh- INHUME dhghem- INIMICAL amma INITIAL ej-1 INITIATE ei-1 INJECT yé- INJUNCTION yeug- INJURY yewes- INK kéu-
2100:PLAN plat- PLANARIAN pele-2 PLANCHET plak-1 PLANE! pele-2 PLANE? pelo-2 PLANES pele-2 PLANE‘ plat- PLANET pele-2 PLANE TREE plat- PLANGENT plak-2 PLANISH pele-2 PLANK plak-1 PLANK-SHEER plak-1 PLANKTON plak-2 PLANO- pelo-2 PLANT plat- PLANTAIN! plat- PLANTAR plat- PLANTIGRADE ghredh-, plat- PLANULA pele-2 -PLASIA pele-2 PLASMA pele-2 PLASMODESMA dé- -PLAST pele-2 PLASTER pele-2 PLASTIC pele-2 PLASTID pele-2 -PLASTY pele-2 PLATE plat- PLATEAU plat- PLATITUDE plat- PLATTDEUTSCH teuta- PLATY2 plat- PLATY- plat- PLATYHELMINTH wel-3 PLATYPUS ped-1 PLAY plegan PLAYA plak-1 PLAZA plat-
2136:PRO-2 per? PROBABLE per! PROBE pert PROBITY per! PROBLEM gWele-1 PROBOSCIS g¥6- PROCEED ked- PROCLAIM kele-2 PROcLITIC § klei- PROCLIVITY klei- PROCREATE ker-3 PROCTITIS prdkto- PROCTOLOGY prdkto- PROCTOR cura PROCTOSCOPE prdkto- PROCUMBENT keu-2 PROCURATOR cura PROCURE cura PROCYON kwon- PRODIGAL ag- PRODIGY ég- PRODROME der-1 PRODUCE deuk- PROFANE dhés- PROFESS bha-2 PROFESSOR reg-! PROFFER bher-1 PROFICIENT dhé-1 PROFILE gWhi- PROFIT dhé-1 PROFLIGATE bhiig- PROFOUND bhudh- PROFUSE gheu- PROGENITOR gene- PROGENY gene- PROGLOTTID glégh- PROGNOSIS gnd- PROGRAM gerbh- PROGRESS ghredh- PROHIBIT ghabh- PROJECT yée- PROLAN al-3 PROLAPSE leb-1 PROLATE tele- PROLEGOMENON leg-! PROLEPSIS (s)lag¥- PROLETARIAN al-3 PROLIFEROUS _al-3 PROLIFIC al-3 PROLIX wleik- PROLOCUTOR tolkw- PROLOGUE leg-1 PROLONG del-1 PROLUSION leid- PROMENADE men-2 PROMINENT men-2 PROMISCUOUS meik- PROMISE (s)meit(e)- PROMOTE meue- PROMPT em- PRONE per! PRONEPHROS _ negwh-ro- PRONOUN no-men- PRONOUNCE neu-! PROOF per! PROPAGATE pag- PROPEL pel-6 PROPEND (8)pen- PROPER pert PROPERTY per? PROPHET bha-2 PROPHYLACTIC phulax PROPINQUITY per? PROPIONIC ACID peie- PROPITIOUS pet- PROPOLIS pele-3 PROPORTION pere-2 PROPOSE apo- PROPRIOCEPTION per! PROPRIOCEPTOR per? PROPTOSIS pet- PROPYLAEUM pulé PROPYLON pulé PROROGUE reg-1 PROS- pert PROSCRIBE skribh- PROSE wer-3 PROSECUTE sekw-1 PROSELYTE leudh-1 PROSOMA teue- PROSOPOPEIA kWwel-2, per! PROSPECT spek- PROSPER spé-1 PROSTATE sta- PROSTHESIS dhé-1 PROSTITUTE sta- PROSTOMIUM ste-men-
2177:REFRAIN? bhreg- REFRIGERATE Srig- REFRINGENT bhreg- REFUGE bheug-! REFULGENT bhel-1 REFUND! gheu- REFUSE! gheu- REFUSE? gheu- REFUTE bhau- REGAL reg-! REGENT reg-1 REGICIDE reg-1 REGIME reg-? REGIMENT reg-1 REGION reg-! REGISTER gerere REGIUS reg-! REGLET reg-1 REGOLITH reg-3 REGRATE grat- REGRESS ghredh- REGULAR reg-! REGULATE reg-1 REGULUS reg-! REGURGITATE gWere-4 REIFY ré-
2181:RETE era-2 RETIARY era-2 RETICENT tak-1 RETICLE era-2 RETICULE ere-2 RETIFORM ere-2 RETINA era-2 RETINACULUM  ten- RETORT! terkw- RETRACT tragh- RETRAL re- RETRIEVE trep-2 RETRO- re- RETROACTIVE ag- RETROCEDE ked- RETROGRADE ghredh- RETROGRESS ghredh- RETRORSE wer-3 RETROSPECT spek- RETURN tera-1 RETUSE (s)teu- REVEAL weg-1 REVEILLE weg-2 REVEL duellum REVENANT gWa- REVENGE deik- REVENUE gWa- REVERBERATE wer-3 REVERE! wer-4 REVERT wer-3 REVEST wes-4 REVIEW weid- REVIVE gWei- REVOKE wekw- REVOLVE wel-3 REVULSION wel-4 REWARD wer-4 RHABDOMANCY wer-3 RHABDOVIRUS wer-3 RHAPSODY wed-2, wer-3 RHEO- sreu- RHETOR wer-6 RHEUM sreu- RHINOCEROS ker-1 RHIZO- wrad- RHIZOBIUM gWei- RHIZOME wrad- RHODIUM wrod- RHODO- wrod- RHODOCHROSITE ghréu- RHODODENDRON deru RHODOPSIN OkW- RHOMBUS_ wer-3 RHONCHUS  srenk- RHYME sreu- RHYNCHOCEPHALIAN srenk- RHYOLITE sreu- RHYTHM = sreu-
2400:TRAIN OIL dakru- TRAIT tragh- TRAITOR d6- TRAJECT yé TRAMMEL macula, trei- TRAMP der-! TRAMPOLINE der-1 TRANCE ei-1 TRANQUIL kweie-2 TRANS- tere-2 TRANSACT ag- TRANSCEND skand- TRANSCRIBE  skribh- TRANSDUCER deuk- TRANSECT sek- TRANSFER bher-1 TRANSFIGURE dheigh- TRANSFIX dhig¥- TRANSFUSE gheu- TRANSGRESS ghredh-
=== KLN gangrene ===
15774:gangrene,  n.,  mortification;  decay.  —  L.  gan- graena,  fr.  Gk.  yaYYpaiva,  lit-  ‘that  which  eats away’,  formed  through  reduplication  fr.  ypav, Ypodetv,  ‘to  gnaw,  eat’,  whence  also  y P<x<m<;, ‘green  fodder’.  See  gastro-.
15775:Derivatives:  gangrene,  tr.  and  intr.  v.,  gangren¬ ous,  adj.
15841:gastro-,  before  a  vowel  gastr-,  combining  form meaning  ‘stomach’  or  ‘belly’.  —  Gk.  yaaxpo-, yaaxp-,  fr.  yaaxqp,  gen.  yaaxp6;,‘stomach,  belly, womb’,  which  is  dissimilated  fr.  *ypxaxY]p  anp lit.  means  ‘eater,  devoured,  fr.  ypav,  ‘to  gnaw, eat’,  whence  also  ypaaxi;,  ‘green  fodder’,  yaa- xpi;  (dissimilated  fr.  ‘ypxaxptp),  ‘pot-bellied; glutton’;  prob.  cogn.  with  OI.  grasati,  ‘eats, devours’.  See  cress  and  cp.  gangrene, gastrocnemius,  n.,  the  largest  muscle  of  the  calf of  the  leg  (anal.)  —  Medical  L.,  fr.  Gk.  yaa- xpoxvqpda,  ‘the  calf  of  the  leg’,  which  is  com¬ pounded  of  yaaxqp,  gen.  yaaxpo;,  ‘belly’,  and xvfjpLT],  ‘part  between  knee  and  ankle,  leg, shank’.  For  the  first  element  see  gastro-,  for the  second  see  cnemial.
28425:-phag,  -phage,  combining  form  meaning  ‘eater’, as  in  x ylophage.  —  From  the  stem  of  Gk. (payeiv,  ‘to  eat’.  See  -phagous. phagedena,  phagedaena,  n.,  gangrene  (med.)  —  L. phagedaena,  fr.  Gk.  (poqxSouva,  ‘cancerous  sore, cancer’,  lit.  ‘voracity’,  fr.  (paystv,  ‘to  eat’.  See -phagous.
36207:Derivatives:  spew,  n.,  spew-er,  n.,  spew-ing,  n. sphacelate,  intr.  v.,  to  become  gangrenous.  — Medical  L.  sphacelat(us),  pp.  of  sphacelare,  ‘to mortify’,  fr.  sphacelus,  ‘gangrene’.  See  sphacelus and  verbal  suff.  -ate.
36209:suff.  -ous  fr.  Gk.  mpax-cXoc;,  ‘gangrene’.  See  next word.
36210:sphacelus,  n.,  gangrene  (med.)  —  Medical  L.,  fr. Gk.  ocpaxeXoc,  ‘convulsive  movement,  gan¬ grene’,  which  possibly  derives  fr.  *sp(hfk-,  -k- enlargement  of  I.-E.  base  *spe(i)-,  *spi-,  ‘to draw,  stretch,  spread,  extend’;  see  Hofmann, EWG.,  p.  345,  s.v.  <rq pdtxcXo;,  See  space  and  cp. sphygmus.
36243:sphygmus,  n.,  the  pulse  (rued.)  —  Medical  L.,  fr. Gk.  o'puypo;,  ‘pulsation’,  fr.  <j9u£eiv,  (for *<j9uy-iEw),  ‘to  beat,  pulsate’,  whence  also £-<j9uxto<;,  ‘pulseless’;  possibly  derived  fr. *sphuk-,  a  gradational  var.  of  *sphek-,  ‘to  move convulsively’,  whence  aodxEXoc,  ‘convulsive movement,  gangrene’;  see  sphacelus  and  cp. sphygmo-,  asphyxia.  See  Hofmann,  EWG.,  p. 347  s.v.  cnpu^co.
=== LEW gangraena/gradior ===
```


## [2026-09-06T02:17:48.460Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT grəd/gar əd ===\"\ngrep -n -i -E 'gar\\^d|garad|gərəd|g\\^r\\^d|aiwi.g|aiwi\\.gar' BRT.txt | head -30\necho \"=== BRT grezdi ===\"\ngrep -n -E 'rəzdi|rezdi|razdi|rozdi' BRT.txt | head -20"
}
```


### [2026-09-06T02:17:48.561Z] TOOL RESULT

```
=== BRT grəd/gar əd ===
3374:'sd.)  sacinte  "ija  aiwi.game  V.  5. b)  'drum,  so  —  denn',  vor  Imp., Inj.,  Konj.,  Opt  und  Inf.:  tsmca..  laibyo dat  sarim  °%a  Asm  foraSua  %wa  xra^toä ^-  53-3'  —  "^'i  ^^'  västs  (sd.)  xsmat anyö  'äa  möi  sqs/a  (sd.)  veAs  vastrya  Y. 2ij.i;  3l.iS,34-7i —  °^«  «f  ii  humayd.- tara  anAm  Vr,  72.4;  4;  ~  "'ia  tu  n9 gayasca..Rya  y,4'-S'> — "^^  »■'  sasdyai (sd.)  usia  V.57. 16.  4)  anschliessend 'und';  a)  ein  Nomen:  i^a  i  Aaiiyaisd.) nare  "'^ä  jsnayö  Y.  5_J,6  3\  b)   einen
3925:•  j.  aiwi-gasta  laf.  'aufzusitzen,  zu  be- steigen (vom  Reiter)':  mä  buyä  aarvatqm yäxta  (sd.)  . .  aiwis°  Y.  /;.  z.
4115:FrW.  4.3;  —  'rahe  mainySus  dämanam ^'^  '5'  3i  —  y^t  titarat  °rS  matnyus dähim  alahe  .  .  antan  pairi.aväit^m  (sd.) fokuca  mattö  atarsca  /J  hg  taurvayatsm tba^ä  °rahe  mainySus  drvats  Yt  7_J,  7  7  f. ; 13;  — yint  nöit  tiurr/pttte  'rS  mainym nsit  yatavS  fairikssca  Vt  1^.44;  —  ailm dahakim..yqm..  drujim  fraca  k>rmlat  'rS mainyus  Y.(?.8;  —  aal  ahe  paityarim  frä- ijrMiat  'rö  mainyus . .V.l. 2;  'J0.3,Aog.2^; —  pairiAä  .  .  yä  uzdtihat  'rS  mainyuS  .  , paiHj>r)tSe  Yt,  A",  39;  —  taxm?m  urupi  .  . yat  barata  'tvm  mainyBm  framitim  (sd.) aspake  JaArpa  ^risatjm  aiwi.gämanam Vt./^.  29;  — paiti.psrme  'nm  mainyBm V, /o.  5;  —  fränämiliti  duhjarstavari'  °r3 mainyus  ax^amanS  Yt/p.  96;  3.^;  — naiHs  xsayät  °rö  mainyus  duzdalnS  FrW. 4.  a ;  —  xsnagiira  akurahe  mazdä  tarSidlti 'raAe  mainyius  Yt.  i.  o;  —  daxstanam  ydi Amli  'rahe  ntainySus  daxstim  V.  2.  29;  P, 2-2,  Y,  7i>,  11;  —  apayafUamah^a  'rahe mainyius  xrafstra  Yt.  21.1;  —  'rif  mainyus . .  dtävanam  daivS  V.  ig.\;  —  vJspB.mahr- käatca  pairi  drvatat  yat  -rst  mainyaot VL/_j.7i;  /0.118,  Y.2-j~-i,  V.'/o.ie;  — ai  duida  °ra  mainyS  V.ii).^;  g,  1,44,  lt. 10,  Yt//.  19; —  iaÖx  dusda  'ra  mainyö V.  i^,  1 2 ;  —  *'rahe ''  *mainy9us  duzdamanH Y.  Ö/.  2;  V. /p.6;  —  skutara  "ra  mainyö V.  79. 3;  —  "rS  mainyus  pouru.mahrkS (Stveri.)  Yt  10. 97 ;  usw.
7899:yeie  dus:^arm3:  nSit  imat  .  .  mihr/f  vat- naili  Ytio.105;  —  aeü/a  (sd.)  ti  sävan .  .  framrava  .  .  °5«  tl  zävan  .  .  fra- ifiraomi {sd.)  YLJj.r-ig;  —  "äil  mainya matnanäitl  Y.  j_y.  4;  4';  —  °äa  ät  yaza- maide  ahurtm  Y.jj.i;  39-1;  —  ät  '%ä yazamaidi  .  .  Y.  jtj?.3;  —  °äa  f  hai^ya (sd.)  nard  d^ä  jjnayö  Y.5^.6;  ■ —  Aaca ..pairi.sa^äiti  °äa  *aiwi.game  Hat  hama.. "sie  dauert  von  . .  bis  ,  .;  so  im  Winter; aber   im   Sommer  .  ."   N. 4Ö;  47,  ^SO^"^;
7902:sehr,  tarn':    m3   tl  (nämL  kaomahe)    nJre (sd.)    .  .    '"isa    raivanto    ar»jahe    Y,  10. '7-         3)  'ebenso,  gleicher  Weise,  item', mit  Ellipse  des  Verbums^:  vasS /raxitäiteisA.)  aiwi.gäme  '^a  hama Winter;  ebenso  (kann  er  es  tun)  im  Som-
7979:•  j.  isav-  Adj.  'frostig,  eisig";  pasia  "saos Z3mö  aiwi.gaitTm  "nach  Eintritt  des  eisigen Winters"  V.9.6.
10226:garad-  mit  aiwi
10242:•  j.  garad-  V.  'gradi',  nur  mit  Praev. Praes.  i  g>r>d-.
10244:aiwi.g3rihmahi      yasnahe       haptatihätäis
17282:•  j.  bi-piSTwa-  Adj.  'der  zwei  Mahlzeiten bekommt';  ^än^iäwif  (sd.)  *el  asii  ätars .  .  iama  '%w3  aiwi-gäme  F.  25b.
23133:•  so patca^a  fi-axstäite  aiwi-gäme  iha  hama V.  i^.  45 ;  12. 3^;  —  a^sa  ä/iyaoiäya  bavaiti *s3  ami/.x'afy%a  pasubya  vira^bya  V. 6^.31;  43;  — yä pspi^wa  'sS  aiS'/ü» (sd.) N.  62.  a)  in  Verbindung  mit  xsä{y)- ava.  'unbeschränkt':  'sasca  ta  .  .  uslsüa xla!ia  havanqm  dsmanam  'sS  3pB  'sH urvarh  *sS  vispa  vohä  Y.  Ä5;  —  ultä ahmai yahmai  uä3  (Sp.  1382  0,)  kahmsi- hl  *'i5  *x^ayqs'>  mazdä  däyat  Y.4^.1; —  yaää  aidii  maMyä  °sS  xlayä  (si)  Y, SO.');  —  ySng  daintt  nöil  jyatSus  (sd.) x!ayamnSng  'iS  Y. J2. 15;_J7, 19;  —  'sS *pascaUa  xsayamna  jasVit  Vd.  4\  Vyt.  3J.
25875:a\a  aiwi^gämeN.^.  10,         2)  'enden  sva,
29390:•  j. 'ham-,  °/a»i-m. 'Sommer':  *ä«^'äa'J .  .  äfari  .  .  'ma  (IS.)  ^ii/i^wS  aiwi.gäme F.  25  b;  V.5.4a,  i5.4S,  Ä  74  PüZ.  {?),  N. 46,  *4j'-\  48,  50,  5/,  */0j'>;  —  yat  vä 'ma  . .  yat  vä  . .  zalna  V.16.12;  — •uia  al  zayem  Y.  16.10;  —  /■wca (GS.)  aiwi^gaUm  V.5.6.  a)  Plur. 'Sommerzeit';  /rä  •>Hfl(NP,)3)  sacinte  a'ha aitui^äme  "die  Sommerzeit  ist  vorbei;  tm Winter  also  . ."  V.5. 10.
=== BRT grezdi ===
6054:•  j.  *a-zrazdi-''  Adj.  'ungläubig':  Vihrkai kavam  dalaiH yy  °dai*mq'ir)m  /aste"dem Wolf  schenkt  seine  Zunge,  wer  den  Ungläu- bigen das  heilige  Wort  lehrt"  N.  ij.
28339:•  g.  *zrazdiSta-''  Adj.  'der  gläubigste': 3i»/(sd.)  'dtüö  Y.5^.  7.
```


## [2026-09-06T02:17:50.097Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD\necho \"=== FFD page 71 ===\"\ngrep -n '\\[pdf page' FFD_pages.txt | head -5\nawk 'BEGIN{RS=\"\\f\"} NR>=70 && NR<=74 {print \"----LEAF\",NR; print}' FFD_pages.txt | head -120"
}
```


### [2026-09-06T02:17:52.903Z] TOOL RESULT

```
=== FFD page 71 ===
1:[pdf page 1]
24:[pdf page 2]
59:[pdf page 3]
70:[pdf page 4]
75:[pdf page 5]
----LEAF 70
[pdf page 70]
ماده‌های ماضی و مضارع قارسی دری سس ۶۵
ی یف ۰
شیفت + ایرانی باستان 33۳۵-۲1۵*. برای 1۵ -> آراست. 0ه7537 صورت اصلی
آنه5۷* است. 0 پیش از 1 بدل به آ شده است. ريشهٌ 8۷۵10*به معنی «جنبیدن) است.
شیب < فارسی میانه 580 + ایرانی باستان 35۷/۵10-۵*. برای 2 > آرای.
«شیفته» صفت فاعلی گذشته از «شیفتن» است و در بیت زیر از گرشاسبنامةٌ اسدی
«(مشیب) به معنی («ناراحت مشو) به کار رفته است:
شکیب آور از درد و بر من مشیب که از مهر بسیار بهتر شکیب
فراموشیدن, فرموشیدن
فراموشید. فرموشید + فارسی میانه 1 ماد ماضی جعلی است. از ماده
مضارع ساخته شده است. در فارسی دری «فرامشت» بازماندة 11371۵31 فارسی میانه
است. 1۳30۵1 بازمانده 112-3-7108-1۵* ایرانی باستان است. برای 2 > آراست. 3و 5۵
هر دو پیشوند فعلی هستند. ريشةٌ کار" ظاهراً به معنی «فراموش‌کردن» است.
فراموش, فرموش < فارسی میانه 137۵5 < ایرانی باستان 172۵-3-۳۵5-۵*. برای 2
> آرای. 13۵05 صورت افزودةٌ ریشهٌ 05 است.
فرجامیدن
«فرجامید» مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
فرجام + فارسی میانه 17[300 < ایرانی باستان 370-2[-17۵*. برای ۵ -> آرای. 370[/ظ
صورت بالاندهٌ ريشةٌ 8/[278 است. 8/1270 به معنی «حرکت کردن» است. صورت بالاندةٌ
آن با پیشوند فعلی ۵ به معنی «به پایان‌رساندن» است. در فارسی میانه ماد ماضی :
به صورت 178[31۲ آمده است» از ایرانی باستان 17[348*, با آمدن 31[ به‌جای
«آمدن) و «انجامیدن» هم از 8/۵7 آمده‌اند -> «آمدن) و «انجامیدن).
فرستادن
فرستاد + فارسی میانه 1۲68130 1138110 هر دو ماده ماضی جعلی هستند. از 11

----LEAF 71
[pdf page 71]
و فعلهای فارسی دری
ماده مضارع.
فرست س فارسی میانه 1۳681 ج ایرانی باستان - ها5زه ۳ *: فرستاده. قاقنه۲؟ صفت
[ مفعولی گذشته است از پیشوند فعلی 8 و هاگٌذ: صفت مفعولی گذشته از فا صورت
ضعیف ريشهٌ قَة: «روانه‌شدن ‏ وکردن» و برای پسوند 2 > آراست.
قرشته از 121512-1۵ آمده است.
فرسودن
فرسودن. فرسای در فارمسی دری بسیط است. اما از نظر تاریخی از پیشوند 2 و
«سودن» و «سای) ساخته شده است + سودن.
فرمودن
فرمود « فارسی میانه 1۳۵7004 + 1۳2۵034 < ایرانی باستان 1۳۵-3-12*. برای 12 -> .
آراست. 178 پیشوند فعلی است. 33 ريشه است به معنی «اندازه گرفتن». 1۳۵/14 به‌قیاس
با فعلهایی چون 8737 و ۹۳84 به وجود آمده است. :
فرمای < فارسی میانه 172۵08 < ایرانی باستان ۴1۳۵-3-8 12 نشانه‌ای برده که
برای ساختن مادهٌ مضارع از ريشه به کار می‌رفته است.
فروختن
فروخت < فارسی میانه 1۳071 < ایرانی باستان 1۵-0-1۵ *. برای ۵ > آراست. ۲۵
پیشوند فعلی است. 1 صورت اصلی 0 است. ۴ پیش از 1 به # بدل شده است. ۷1
صورت ضعیف ۷۷۵و آن به معنی «گفتن» است. ۱
فروش دج فارسی میانه 1۳05 ج 105 «<ایرانی باستان ۲۳۵-۵55 *. ‎٩‏ برای ساختن
ريشةٌ جدید به کار می‌رفته و 1 پیش از 5 به #بدل شده است.
فرهیختن
فرهیخت + فارسی میانه 1۳80451 < فارسی باستان 0۵-1۵ -1۳۵*. < ایرانی باستان

----LEAF 72
[pdf page 72]
ماده‌های ماضی و مضارع قاری دری سس ۶۷
۴1۳-4۵ برای 1۵ > آراست. 2۵ پیشوند فعلی است. ۹38 صورت اصلی 83 است. 8
پیش از 1به #بدل شده است. ۹88 صورت ضعیف ريشةٌ ۹228 است. «برای ضعیف کردن
ريشه حذف شده است. 5288 به معنی «کشیدن» است.
فرهنج ج فارسی میانه [112822 < فارسی باستان 8-[0۵0 -8۵* < ایرانی باستان
2-[172-8۵2*. برای 2 - آرای. [به جای 8 آمده است. + آهختن.
«آهنگ» و «فرهنگ» هم از ريشةٌ 988 گرفته شده‌اندء به شرح زبر:
آهنگ + فارسی میانه 30228 < فارسی باستان 0208-8 -3* < ایرانی باستان
۶3-8288-2. 3 پیشوند و 2 پسوند است.
فرهنگ < فارسی میانه 13022 < فارسی باستان 0۵88-8 -8۸* < ایرانی باستان
۳۵-۵28۵
۱ فریفتن
فریفت < فارسی میانه 17211 < ایرانی باستان ۳2۵-427-1۵]*. برای 18 > آراست. 18
پیشوند فعلی است. 420 صورت اصلی ريشه است. پیش از 1 به ؟ بدل شده است. ريشهٌ
0 به معنی «فریفتن) است.
فریپ < فارسی میانه 1۳80 < ایرانی باستان 18-420-2*. برای ۵ -> آرای.
کاستن
کاست < ایرانی باستان 1:39-12*. برای ۵) -> آراست. 139 صورت بالاندةٌ ريشه 1۵5
است به معنی «کوچک بودن». صورت بالانده در معنی واداری به کار رفته است» به معنی
«ک و چککردن».
کاه « فارسی میانه 13 < ایرانی باستان 139-۵*. برای 2 - آرای.
کاشتن
کاشت < ایرانی باستان 37-5-12 *. برای 1۵ -> آراست. 837 صورت بالاندةٌ ريشة 1۵7
به معنی «زراعت کردن» است. 5 برای ساختن ريشهٌ جدید از ريشه به کار می‌رفته است.

----LEAF 73
[pdf page 73]
0 فارسی درق
کار + فارسی میانه 3 < ایرانی باستان ۸37-۵*. برای 2 -> آرای.
«کشت» مادةٌ ماضی دیگر است برای «کار» از فارسی میانةٌ 151 < ایرانی باستان
۵ا-65ا*. 1 صورت ضعیف ريشةٌ 1۵7 است.
کافتن
کافت + فارسی میانه 1311 + ایرانی باستان ۸3-1۵*. برای 18 -> آراست. 131 صورت
بالاندهٌ ریش 81 به معنی «شکاقتن» است.
کاو +کاف < فارسی میانه 13۶ < ایرانی باستان ۴32*. برای 2 -> آرای.
« کفت»» که مادهٌ مضارع آن «کف» است. از ريشةٌ ۵ به معنی «شکافتن» آمده است.
به شرح زیر
کفت « ایرانی باستان 1۵1-1۵* کف « ایرانی باستان 1۵1-8*.
«کفتن»در فارسی دری هم لازم و هم متعدی به‌کار رفته‌است. در شاهنامه آمده است:
نیامد جز احستتشان بهره‌ام
بکفت اندر احسنتشان زهره‌ام
کامستن
کامست < فارسی میانه 1300191 1370181 مادةٌ ماضی جعلی است. از مادهٌ مضارع
ساخته شده است.
کام « فارسی میانه 2/0 « ایرانی باستان 28*. 8308* در ایرانی باستان اسم
است که به عنوان مادهٌ مضارع به کار رفته است.
کردن :
کرد (به کسر و فتح اول) + فارسی میانه 876 و ۴۵۲۵ < ایرانی باستان 7-1۵* و
۵۶-۵*. برای 4۵ آراست. 7 صورت ضعیف ريشهٌ ۵7 به معنی «کردن» است.
کن + فارسی میانه 18 < فارسی باستان ۴۵۵ < ایرانی باستان ۴17-۵۷ 7 به ۵
بدل شده است. 24۷ برای ساختن ماده از ريشه به کار می‌رفته است.

----LEAF 74
[pdf page 74]
ماده‌های ماضی و مضارع فارسی دری شش و۶۱
اک کت
+کاشتن
کف
کشت + فارسی میانه 1934 + ایرانی باستان ۴*10۵5-12. برای 18 > آراست.
کش < فارسی میاته 1005 < ایرانی باستان 10۵3-۵*. برای 2- آرای. ریشهٌ 63 به معنی
«نبرد کردن» است. «کوشیدن» هم از ریشةٌ 05 آمده است.
کشفت.
کشفت < فارسی میانه ۷1811 < ایرانی باستان ۷807-1۵" برای 18 ->آراست. ۷:1
پیشوند فعلی است. 00ا75صورت اصلی ريشةٌ ۶ا3«است» پیش از 1به 1 بدل شده است.
0 صورت ضعیف ريشهٌ 35200 است. ريشهٌ 5200*به معنی «لرزیدن» است. «آشفتن)
```


## [2026-09-06T02:18:01.155Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10220,10270p' BRT.txt"
}
```


### [2026-09-06T02:18:01.202Z] TOOL RESULT

```
•)  Sra.  vahiilä  aahus  und  aJiajra  taoii;  vgl. iB.  V.  /p.  3a  und  Y.  lg.  6.  Vielleicht  wurde aber  das  G.  auch  als  besonderer,  d.  i.  besonders heiliger  Raam  innerhalb  des  Paradieses  be- tracbtel.
Zum  V.  'gar-i').  —  ai.  ^-  f.'),  —  PQ.  (lu  Y.  V)i girihi,  (zu  A):  ^iv/m4iB(Transskr,). —  ■)  Nicht völlig  sicher.  Vgl.  SAderbloh  La  vie  future 98.  —  >)  NA.  schreibt  ohne  erkennbaren Gmnd  bald  gatS  um',  bald  garS.nm'  (s.  *).
•  j.*gar-  i)  Adj. 'schluckend,  verschlingend' (nur  Komp.).  2)  f.,  Plur.  ■>  'Kehle,  Hals'  '> : aictl  ai3in  (näml. o^/)  tanUn  aguze  aiairi maisahe  -rö  Yt.  J7.  56.
KompE.  —  Zum  V.  igar-.  —  ai.  'gir-  Adj. ;  vgl. ai.  gala-  m.,  np.  giilü  'Kehle'.  —  •)  Auch -ariman-  (sd.)  ist  Flur,  lant  —  =)  Gans  un- wahrscheinlich Gdn.  3Yt.   lao.
•  j.  garay-  :  gairi-  m.  'Berg,  Gebirgszug, Gebirg"':  -rayi^^^.)  b^nzantB  Ytio.  14; ig.z,  7,  8,  16.  3;  —  'rayd  (als  AP.)"  aSa- ^ä^rä  Y.2.14;  /0.3,  7/.  10;  —  'rayasca (als  AP.)  ySi  hrnaniö  Yty.  9;  —  ma- sits  Urli{AP.)  Yt.j4.4ii  —  bar^dstaiibyö 'triiyS  V.  2.  aa;  —  'irl/c3'^  aßtaHnS  Y. 42.3; —  iarfshus  paiti  'irinam  Y.5.  26, JO.3,  V.2.23i>;  Y.j.14^, /o.  17.  YLÄ24, 14-  21.  iS.  6,  ig.  6,  Vr.  /.  6,  V.5.  I',  2, 10.28;  —  haoma  raose  'ra  (LS.)  paiti Y./0.4;  —  ytzi  ahi  'rS  (LS.)*'  dtr^hm (sd.)  \.2i.  5;  —  paoiryB  °iris  hqm.hiiial .  .  haraiii  bars  . ,  bitys  ztrihazB  HrU  Yt.
BAITHOLOHAa,  AlÜHD.  Wb.
garad-  mit  aiwi
514
ig.  i;  6',  66;  —  'rsU  ^uHjIar^nahe  Y.i. 14,  22.36;  Ny.5.  5,6,  FrW.5.  i;  —  airyB.- xs'uiai  haca  'rsit  :^anvant»m  avi  HrXm Yt5.6;  i.zZ,  5.4s,  &33,  Y.2.14,  Ny./. 8,  V.  22. 19,  S.  2. 9';  —  *aoi  spitagaona (sd.)  Hri  (AP.)  4>  Y.  jo.  1 1 .  [FrBy. :  lies gairi  ifrpzB.]
•)  Die  Gesammtiahl  der  Berge  wird  Vt  lg.  7 'auf  2244  angegeben;  vgl.  die  Aufiahlung  Yt. /g.  1  ff.,  woiu  Bd.  M.  1  ff. KompA.  —  ai.  giräy-  in.;  mp.  gar,  glrft),  afy, yar.  -  Pü.!  gar;  s.  noch  No.  2,  4,  —  ')  Mit der  Var.  gairyS,  %  406.  —  ')  Pii.i  Idna  ^ gil  'I^hm'l  Statt  ^(>6).  Sü.:  giri^.  —  3)  Mit der  gut  bezeugten  Var.  ^lurcanqiB  6) ;  s.  'varay- No.  I.  ~  4)  iSt.  yg\.  Gdn.  sYt.  120.  Pü.: garölmän.  —  5)  Gebildet  wie  dahnaiiiyü,  htnda, S  1^7.  S.  aber  lu  sßia.gama-  No.  —  *)  S. lu  '%raotah-  No.    l.
•  j.  garav  (:  °yrav-)  Adj.  1)  'schwer, schwerflüssig'.  2)  fem.  i°yrs-)  'gravida, schwanger'.
KompA.  (s.  goutu''),  E.  —  ai.  guräv-  ['grav-) Adj,;  np.  vgl.  girän.
•  g.  garah-  n.  "Lob-,  Preislied';  pairi- gal'iw  (sd.)  xsmUvatö  vahms  mazda  °rSbll stBiqm  Y.34.2.
Zum  V.  'gar:  —  Pß,  j  vatän  andar  gardtmän släyim.
•  g.  gaire  Inf.  'zu  wachen  über-'  (Akk.); yS  *urvqtiim  min  g°  . .  dadl  aslscä  vldus (sd.)  . .  yavat  isät  (sd.)  .  .  avai  xsäi  aesl asahyä  "der  ich  des  eingedenk  bin  über die  Seele'*  zu  wachen  .  .  und  .  .  sie  .  , lehren  will,  das  A.  zu  suchen"  Y.  2S.  4.
Zum  V.  ^gar-,  —  Pü.;  ki  ruvän  andar  garöl- män dahci,  —  ■)  Des  Menschen,  die  dem Propheten  anvertraut  ist.
•  j.  *gairi.b9r9z-'>  f. 'Bergeshöhe,  -tiefe"': ''snu.b^Kö  n3rf.b3r3zS  °zd  mänö(sA.)  FrBy.
Npü. !  iüh  biilä.  —  ')  Hds.  i;arayö  t'.  —  'I  Oder Adj.
•  j.  gairi.masab-  Adj.'*  'von  der  Grösse eines  Bergs';  °s!J  aahB  (sd,,  Sp.  iio  m.) aetahe  V.5.9  PüZ.
1)  Oder  auch  ntr.
•  j.  gairi-äak-  Adj.  (auch  fem.)  'was  mit den  Bergen  zusammen,  in  ihnen  heimisch ist':  aurunaca  (sd.)  "iJÄJ  (NPm.)  siidraca ravascaraid  Yt.  Ä36;  —  paotris  3pB  .  . '/äcB  (NPf.)  Yt./p.66.
Komp.;  gataf-  +  'Aai:
•  j.  garad-  V.  'gradi',  nur  mit  Praev. Praes.  i  g>r>d-.
mit  aiiui  'ingredi,  anheben,  beginnen':
aiwi.g3rihmahi      yasnahe       haptatihätäis
dby  Google
515  gar»d-  mit  avi  —  garäta-  516
AumataSa   hastaca  hvar^aca;    aiwi^trü-  bleiben  oder  sich  im  Hals  festsetzen"  V,
mahi  ahm  vohü  Vr.iy.i;  —  aiwi^ßnl-'  i^.^.
mahi  apqm  .  .  fräitlmca  .  .  Y,  Ö2.  n.         1     Vgl.  <'gat-  f.  —  Pü. :  galäk  (=  np.  gulü\
mit  avi  dn.:    avi  apqm^a  «m/r«- 1      ■  ^„^y.  ^  -Hitze' :  vJ  >i<y/.7  äp«ä
namca  . .  yasn,mg,f^r,n,aht  vaAm?mca  ,  .   ,,an%aüyw>m  frak»rmtatar,rSmainyus\. "7.  ■  ■  r^T         vi"-'-  V  P-      '"'''>^T»f^a  'maum  (AS.)' V.  m8.
Ut  vgl.  gradier.   —     VeL  gjnzday-.    —    Pü.!,       ,,  ,  d-  -i
•  j.   gaMWa-   m.    l)   'Mutterleib,   Uterus':  I         i-  Sanmü.vataahim  A.  J,  ?;  lies  a^arim-,
j.«   (näml.  aridvt,    mpunqm   hlmSimm' ,  ■    „„„s.starana-   m.   ein   bei    der Mää,  ••<™,.>^...v4,M,«  Y.65.=;-Arp^i„»        gebrauchtes    Gerät:    ymiäMi
(oaml,  arpdvi)  arsnqm  xsudm  m  xlaä^rt- 1  ,  ,  .       °  /  Fp  \  y  »4  7
nqm    *'wqn  ■>   (näml.  yaeidalaiÜ)    Y.  65.  |  >,i,ara„a-  n„  vll.  lü  lit.   'skilti  -Feuer  anschlü-
5.  2)  'Leibesfrucht,  _/W«j'':  ma  . .  iaiiie]  gen'O.  -  IMi,:  oddamk  (Jamaspji  Gloss.547;
mafySnam  pard  fsanmat  {sA.)  :^atU  °W3m^  ".^j/.imi;  Utensils  med  in  the/äi' »j^*-^/(highet
ra?sayät\.  15.11;    ij.   "  "r?'"l'"i    of    'he    Zoroastrian     rdigion^)
..i-^Ma-  m.  I)  -Uterus,  i) 'fetus  ;  mp-  (P";)  (^o !,/„/«/  5,™r^«rf.   -    ■)  Np.  >mr  'Kohk'
■^r.  -    .)  NA.  -,«,;    s.  aber  Var.  und  Yt.  1^,   '^Q^^  „^^^  jjpp_j_  ^g^  fernzuhalten!    i-
j.  gartiai;  lies  giribiü.
•  j.  gar«nav-  m.  'Krätze':  altaliva  dax- maeiva  Aqm.iavainti  axtii^a  'mdc'a  ..\.y.
jelil  Glrili.  /  b.  87.
•  j.,   g.   garaz-  V.   'klagen',     Praes. ,gii-}Z;  S  Jlg»r3z-  [,  25  g»r?zanä\.
57;  —päilistJUe  -näuica  (GS.)  /.rAffW-ii  1      '•''"S^"'  wehklagen,  jammern';   i)  ohne
Yt.y.i,
Obj.:  yeühe  vlxs  gpn
mp.  (Pö.)V'rr.  np.  ^^  -KritK';  so  nseh  JN. ' '■''^''«  (^d.)  a/naoiti  Yt./o.Ss;  —  «d.Vffi JAOS.  14.  cxxv.  g)r>zänä  (NPf.,  näml.  fravalay^)  /ilra-
.  j.,  g.  gamma-  (,  p,  .r«""«»-)  i)  Adj.  {""•  ■  ■  W'l-'Sr.  'S-^'S  -  f"  ffr.! 'heiss,  (Obertrieben)  warm':  aM  a/l .. ��mal  /'■«»« /nf»«i (f.) ..  »«™»'.w- (sd.) . . Yt;o.so,  V.2.S;  -  -»»».ä,  vmm  mlimla  y5»""«(3PPrA,)'>i««äimi^I  ««V,»J "2u  waimen  und  zu  kalten  Wind"  Yt.o.io:''""*'  •  '''  T*?  ■«  J™""» '»  ■?=»■ ««.«».  M  „faJ.Sal  "wenn  (ihm)  die  m  »opheten'  Y.^ja.ij  a)  mit  Dal  der heissen  Speisen  Maul  oder  Zunge  «er-  P="<"'-/"''t; '',?™''  '  .''  » '"''«»^. brennen"  V.,5.4.  2)  n.  'Hitze,  Gluf:  K^ä-)   "''":'  ^iti.Kr..  "'™,'?-"'  •?*'
```


## [2026-09-06T02:18:02.037Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD\nawk 'BEGIN{RS=\"\\f\"} NR>=76 && NR<=79 {print \"----LEAF\",NR; print}' FFD_pages.txt"
}
```


### [2026-09-06T02:18:03.549Z] TOOL RESULT

```
----LEAF 76
[pdf page 76]
ماده‌های ماضی و مضارع فارسی دری سا ۷۱
پیشوند فعلی است. 136 صورت اصلی 135 است» ۴ پیش از + به #بدل شده است. 13
صورت بالاندةٌ ريشةٌ 12۳ به معنی «دویدن» است.

گداز < فارسی میانه 432 < ایرانی باستان -۳۹۷1-130. برای 2 - آرای. 6 به جای 1
آمده است.

گذاردن, گذاشتن

گذارد. گذاشت < فارسی میانه 14374 ۷14331 . ۷14370 از ایرانی باستان
-۳۷۷-137. برای 1۵ -> آراست. ۷1 پیشوند فعلی است. 137 صورت بالاندةٌ ریشهٌ 1۵7 به
معنی «عبورکردن» است. 137 صورت بالاندهٌ ريشه در معتی واداری به کار رفته است و
7 صورت افزودهٌ ریشه در معنی لازمی > گذردن. ۷1۵0351 به قیاس با 137 و 381 به
وجود آمده است. َ

گذار < فارسی میانه ۷1۵27 < ایرانی باستان 9۷-13۳-۵*. برای ۵ > آرای.

گذردن, گذشتن

گذرد., گذشت < فارسی میانه ۳1427۵ ۷1۵۵51 .۷14276« ایرانی باستان ۷:1-1۵7-1۵*.
برای ۵ > آراست. پیشوند فعلی است. ريشهٌ 187 به معنی «عبور کردن» است. ۲۷۷1۵۵51
به قیاس با 137و 1351 به وجود آمده است.

گذر < فارسی میانه ۷1۵1۲ + ایرانی باستان ۷1-1۵7-78*. 98 نشانه‌ای بوده که برای
ساختن مادهٌ مضارع از ريشه به کار می‌رفته است.

گراییدن

گرایید < فارسی میانه 70ر8۲3. مادةٌ ماضی جعلی استء از ماده مضارع ساخته شده ۱
است.

گرای < فارسی میانه 8739 + ایرانی باستان 872-78*. ۷8 نشانه‌ای بوده که برای
ساختن مادهٌمضارع از ريشه‌به کار می‌رفته است. ریشةٌ 8۲3 به معنی «خم‌شدن) است.

----LEAF 77
[pdf page 77]
کچ یا ی فعلهای فارسی دری
گرفتن
گرفت + فارسی میانه 878 < ایرانی باستان 87۳-4۵ *. برای 13 > آراست. 870 صورت
: اصلی 871 است» ۳ پیش از ۲ به / بدل شده است. 870 صورت ضعیف ريشةٌ 8780 به
معنی «گرفتن» است.
گیر + فارسی میانه 8۲3 < ایرانی باستان 8۲8-72*. 72 نشانه‌ای بوده که برای ساختن
ماده از ريشه به کار می‌رفته است.
گروستن, گرویدن
گروست + فارسی میانه ۷۷07۲2۷۷181. ۱۷۷۵۳۷۷/۶1 مادةٌ ماضی جعلی از مادهٌ مضارع
است. «گروید» در فارسی دری مادهٌ ماضی جعلی است. از مادهٌ مضارع.
گرو + فارسی میانه ۷۷۵۶۶۷۷ + ایرانی باستان ۴۷۶۵۷ ۷۲ صورت ضعیف ريشةٌ
57 به معنی «گُزیدن) است. 1820 برای ساختن ماده مضارع از ريشه به کار می‌رفته است.
گریختن ۱
گریخت + فارسی میانه ۷۷788 + ایرانی باستان ۷۷1-۵0-1۵*. برای 18 -> آراست. ۷:1
پیشوند فعلی است. 7211 صورت اصلی 731 است» 1 پیش از 1 به تابدل شده است. ريشةٌ
جه به معنی «ترک کردن» است. (ریختن» از ریشةٌ انة7 آمده است + «ریختن».
گریز + فارسی میانه ۷762« ایرانی باستان ۷1-۵16-2*. برای ۵ -> آرای. ابه جای ۸
آمده است.
گریست < فارسی میانه افاولاع. 81اررزتع ماده مأضی جعلی است» از مادهٌ مضارع
ساخته شده است.
گری + فارسی میانه 1تع + فارسی باستان 8۲4-78* « ایرانی باستان 8۳۵2-78 *. 2
برای ساختن مادةٌ مضارع از ريشه به کار می‌رفته است. ريشهٌ 8792 به معنی «گله کردن»

----LEAF 78
[pdf page 78]
ماده‌های ماضی و مضارع قارسی دری ۷۳
است. «گله» فارسی دری از 81188 فارسی میانه آمده است و 8128 از 874-42* فارسی
باستان. 874 صورت ضعیف ريش 8۵74 / 8720 است. 218 پسوند بوده است.
۱ گزاردن
گزارد + فارسی میانه ۷12274 < ایرانی باستان 3۳-1۵.-۷*. برای ۵ -> آراست. ۷:۱
پیشوند فعلی است. لَن صورت بالاندةٌ ريشهٌ 27 به معنی «حرکت کردن» است.
«(چریدن) از ریشهٌ 47 آمده است > چریدن.
گزار < فارسی میانه ۷1237 < ایرانی باستان 2۲-۵.-۷۷*. برای 2 > آرای.
گُزیدن
گُزید ج فارسی میانه ۷127۵ < ایرانی باستان ۶۷-6۲-1۵ برای ۵ > آراست. ۷
پیشوند فعلی است. آت صورت ضعیف ریشةٌ له به معنی «گزیدن» است.
گزین ج فارسی میانه ۷۵217 < ایرانی باستان ۹1-61-۵*. 120 نشانه‌ای بوده که برای
ساختن ماده مضارع از ريشه به کار می‌رفته است.
گزیدن
۰ کِ شت.+
گستردن
گسترد < فارسی میانه ۷181۵74 < ایرانی باستان ۴۷۷1-81۵۳-12. برای ۵ -> آراست. ۷1
پیشوند فعلی است. ريشهٌ 5187 به معنی «پاشیدن» است.
گستر < فارسی میانه ۷۷۶17 < ایرانی باستان ۷1-۹1۵۳-۵*. برای 2 -> آرای.
ا گسست < فارسی میانه ۷9181 < ایرانی باستان ۷:1-918-1۵*. برای 2 > آراست. ۷:1
؛ پیشوند فعلی است. 814 صورت اصلی ريشه به معنی «بریدن» است و 4 پیش از ]به بدل

----LEAF 79
[pdf page 79]
4۳ نفعلهای فارسی دری
شده است. 814 صورت ضعیف ريشهٌ ۶210 است.

«گسل» در فارسی دری مادهٌ مضارع «گسستن) است. در فارسی میانه مادةٌ مضارع

: اقا ملع آمده است و آن از ۷۷۹-۹18۵* ایرانی باستان آمده است. ۶104 از ادخال 8

پیش از آخرین صامت ريشه برای ساختن مادهٌ مضارع از ريشه به کار رفته است.

در فارسی دری «گسیخت» به جای «گسست» به کار رفته است.

گشادن, گشودن

گشاد < فارسی میانه ۴834 < ایرانی باستان ۷1-33-1۵*. برای 1۵ > آراست. ۷۷
پیشوند فعلی است. ۳3 صورت اصلی 3 است» « پس از ابه 5 بدل شده است. ريشة ۲3
به معنی «بستن» است. «گشود» در فارسی دری به قباس با «سرود»» «سرای» به وجود
آمده است.

گشای + فارسی میانه 152 < ایرانی باستان ۳-52-78*. # برای ساختن ماده از
ريشه به کار می‌رفته است.

گید(

گشت < فارسی میانه ۷251 < ایرانی باستان ۹279-12*. برای 1۵ -> آراست. ۷۷۸۲۲
صورت اصلی ۷۷279 است. 1 پیش از ۲ به 8بدل شده است. ‏ -

گرد + فارسی میانه ۷۷۵۲ < ایرانی باستان ۳:۵۳-۵*. برای 2 -> آرای,

گاشت. مادةٌ ماضی گاشتن» از ۷37۳-۲۵ آمده است. ۷371 صورت بالاندةٌ 8۶۲ است.

گشت. ()

گشت < پهلوی اشکانی 8281 < ایرانی باستان 8۵3-12*. برای 1۵ -> آراست. 8۵7
صورت اصلی 825 است» 2 پیش از + به 5بدل شده‌است.ريشةٌ 822 به‌معنی «گزیدن» است.

گز + فارسی میانه 822 < پهلوی اشکانی 82۵7 < ایرانی باستان 827-2" برای ۵ ->
آرای.
```


## [2026-09-06T02:18:21.125Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -E 'g\\)r\\)zd|g>r>zd|g\\^r\\^zd|gsrszd|g3r3zd|gjrjzd|garszd|gerezd' BRT.txt | head -20\necho \"--- try WLD Bd I 651\"\ngrep -n -i -E 'ghredh|gr̥dh|gradior' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20"
}
```


### [2026-09-06T02:18:21.195Z] TOOL RESULT

```
--- try WLD Bd I 651
37848:mit ghredh- „schreiten". so dab „begehren" aus „worauf losgehn" (so 
39861:m. Lit., Yf. LEWb. 2 u. horior , gradior, Feist GWb. 2 162) kann sich weder 
40997:greus- — ghredh- 
41558:(neben *ghrpd- steht *ghredh- in ags. gresdan „rufen, schreien“, s. Ilolt-
```


## [2026-09-06T02:18:23.365Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '40990,41060p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-06T02:18:23.425Z] TOOL RESULT

```
malmen, zerquetschen“, ahd. kroselQi) eigentlich „Krachbein“, d. i. „Knorpel“, 
mnd. krossen, schwed. kro-ssa, kryssa „zermalmen“; got. krms-tan „knirschen“, 
krusts „das Knirschen“, aschwed. krysta „Zahne knirschen'' und „quetschen“, 
ahd. krustila , nhd. Krustel , Krostel „Krachbein‘''; 



greus- — ghredh- 


651 


ahd. krus-k „furfur“, ahd. Krii-sch „Kleie‘- (auch Grusch, Griist durch 
Kreuzung mit Grics, Griitze ); 

ahd. kros-pel, nhd. Kruspel, Krorpcl „Knorpek‘, kruspeln „knirschend 
zerbeiBen". 

Daneben eine i- Wz. in boll, krijzelen „Zahneknirschen‘', ahd. krisgrim- 
mon ds , nd. krisel „Brosame, Krume ! , anord. kreista „pressen, umarmen. 
zerdriicken“. 

Serb, griihati „krachen (von der Kanone), mit Krachen schlagen ; durch 
Schlagen enthiilsen“, yruiiti „sto£Sen, enthiilsen“, yruh .,kleine Steine“, 
slov. yruli „Steingerolle“, gnUciti „zerbrockeln“, gn'tsa ..grober Sand"', russ. 
griichnutbsja „mit Geriiusch zusammenstiirzen*’, poln. yruchac „girren“, 
gruchnqc „ertonen, mit Krachen hinfallen, fest schlagen 14 , -sit „zerbr6ckeln' 4 ; 
lit. grukseti „knirschen, knistern, vom Sand' 4 (/„--Einschub ? iiber grnuzus 
.,Graus, Kies 44 u. dgl. s. unter *ylireucjh- S. 650). 

Persson Beitr. 333 (z. T. nach Fick BB. 6, 213). Ahnliches, das Knir- 
schen ebenfalls durch gr- malendes *yre-gh- in lit. yiieziu , knirsche 44 = grl- 
czti ,.auf einem Instrument spielen 4 ' ; unsicherer ist, ob das nach gr. fjovyoj 
mit y'ir- anzusetzende *g'ireugh- „beiBen, nagen, Zahneknirschen 41 (seit Fick 
aaO. mehrfach mit *yreus- vereinigt, welchenfalls y?,reu-s- anzusetzen ware) 
ursprgl. „Knirsehen“ war und einer ahnlichen Lautnachahmung entsprungen 
ist (anders, nicht uberzeugend, Falk-Torp 587 : als „zerreiben“ zu j'ierd 1 - 
..Miihlstein das eher zu g'itr- ,,schwer 44 , s. d.). 

kriustan nicht nach Grienberger WSB. 142, VIII, 142 zu ags. crucian 
„driicken“ (s ,*yreitt- „drangen -4 ) und lit. grtuP.iu, ynlsti ,.sto£5eu, stampfen * 
(s. *ghreud-). 

2. greus- „brennen, schwelen 4- ?? 

Gr. yguvog oder ygovvog „durres Holz, Fackel 44 , I'gvvttov, I'gvvot .,Stadt 
in der Aeolis 44 Fick BB. 23, 22, 213) verbindet Prellwitz 2 101) zw. mit lett. 
gruzdet ,, schwelen, glimmen“, grust ds. Doch ist ganz fraglich, ob die 
gr. Worte ursprgl. , Brennstoff, durch Feuer gerodetes Land - ' 4 und nicht 
eher „Geholz u. dgl.“ bedeutet haben. Miihlenbach-Endzelin I 666 mit Lit. 

gred- „kratzen“. 

Dehnstufig in alb. yeruaii , krmu „kratze, schabe 41 , gtruse, ycrese, ki lire 
„Schabeisen“ (woraus nach Jokl SBdAk. Wien 168, I 23 lat. yroru „Schab- 
eisen des Silberarbeiters“ bei Arnobius entlehnt). krome „Kriitze, Aus- 
satz“, kros ds., kros „raudig“ (s. Jokl IF. 37, 99). 

An. krota „eingravieren“, mndl. krettai , ahd. mit Intensivgemination 
krazzon „kratzen, zerkratzen, zerfleischen“, mhd. kratzen, kretzen (w'oraus 
lcratz m. „Kratzen, Wunde, Schramme“ riickgebildet), krctze „Kratze u (nicht 
zu mhd. schratzen mit s-Verlust s. unten II 580 u. sqcrd-). 

G. Meyer Alb. Wb. 130, Fick III 4 51, Falk-Torp 572. 

gliredk- „schreiten 4 ‘. 

Av. aiivi-yorddmahi „wir beginnen, ingredimur 44 , yjrszdi- f. „das (' An- 
treten =) Inbesitznehmen, Bekommen 44 (Bthl. Wb. 514 f . , 524); ind. (Asoka- 
Inschr.) adhigicya „beginnend“ (= skr. * udhi-grdhija nach Michelson IF. 27,
```


## [2026-09-06T02:18:33.656Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -E '52[34] ' BRT.txt | sed -n '1,40p'\necho \"---- search Inbesitznehmen\"\ngrep -n -i 'Inbesitznehmen\\|Besitznehmen' BRT.txt | head"
}
```


### [2026-09-06T02:18:33.743Z] TOOL RESULT

```
28092:•  j.  zära-  m.  'Galle':  'ras(HS.ya  F.^g. Vgl.  gr.  x»^»,-,  Bthl,  ZDMG.  j;.  155;  s.  noch No.  i.  —  Pü.:  zahrat.  —  ")  Oder  ist  das Wort  als  zSt's  a  lu  denken  und  j  lu  S  J04 n.  2  lu  stellen?  Der  idg.  NS.  *iA^/d  wUre wie  gr.  i.f^  gebildet  (BB.  //.  119,  125)  und verhielte  sich  zu  *j;jr^/-  (Sp.  523  o,)  wie  gr. afp  zu  lat.  i^rd-i  zur  Anlautsdilferenz  s.  Ugv. Grdr.  />.  545.  \.a.t. /ellis  enihält  doch  eher altes  ida.lsln,  wie  So.MMERLatl.aut&t'ornient. 394  "'iU-
---- search Inbesitznehmen
10383:g.   garazday-  f  'Inbesitznehmen;  Be- kommen': yqm   ..   isyqm  dtltü   ..   ahurö
```


## [2026-09-06T02:18:35.629Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10380,10392p' BRT.txt"
}
```


### [2026-09-06T02:18:35.709Z] TOOL RESULT

```
garazä-  t  'Klage':  paoiryqm   'sqm gsrssacfa  (sd.)  asÜ  \t.  ij. 57;  58,  59.
Zum  V.  ganz-,  —  np.  S'la  'Klage'.
•  j.   garazäna-  Adj.  (fem.  •«:/■),  PPNL:
g.   garazday-  f  'Inbesitznehmen;  Be- kommen': yqm   ..   isyqm  dtltü   ..   ahurö
•  j.  garaSö-karata-  Adj.  'die  Galle  heraus- schneidend"':    kat    tä    tiara  yaozdayqn aiih>n  .  .  ya  rrasiuin  franuharat  sänS  i  "   ' para.iristahe  masyelu  väl  .  .  ayaozäayqn  ■ atihm  . .  lalJ'a  narS  'l^sca  (NPm.)  z^maö.- k?ntas^a  taica  tiarS  spiti.dsi'^ra  casmanal  * haca  itilbar>nti  "Sind  die  Männer  zu  pui fiziren,  die  .  .?  .  .  Sie  sind  nicht  zu  put fiziren,   und   (ebensowenig)   die  Männer, '
die  die  Galle  und  die  das  Herz  (aus  dem' Jir/cJ/Csd.)  "ä^«  Y.5/.17;  —  ai*hudäi. Hunde-  oder  Menschenleichnam)  heraus-  iVa/w  (sd.)  'dJ  (LS.)  Ryim  Y.50. 9. schneiden,  und  (ebensowenig)  die  Männer, '     Zum  v.  ,i,™vfl^-i   %  S3}-    Kig. 'Antreten'.  — (die  ihnen)  die  Augäpfel  aus  der  Augen- 1     ^"-  (''K"-)'  .?"■■".  X''fl"'- höhle  herausreissen"  V./.isf.".  E-  S"-nm-%  lies,^«*™-.
Vgl.  lat.  fei,  ßilis,  k<!.  iiüü  'Galle'.  —  Pü. : .  •  j.  gouru.zaoSra-  Adj.  (mask.  °ra-)  'des Hak  tirrcnihiSniouii ,  dam  als  Weihgüsse  schwer,  zähflüssig  Sind"':  ^»«•n'J "■■''*■"""'  t  Yt./o.ri3.
Ansicht  ^/ura/s :  gtii/ak  sä»  ap2  ii Hohle  ist  in  zerstören".  S.  dazu  such  Sd. //.  2.  —  ')  Ich  kann  die  hergebrachte,  an Pu.  sich  an  sc  hl  i  einsende  Fassung  der  Stelle (DsT.  ZA.  2.  100;  "de  ces  hommes  il  faul ditruire  le  tcrrier  et  arracher  Ic  coeur;  h  ces hommeü,  on  enlevera  l'oeil  clair  de  l'orbite"; ebensowenig  (ur  richtig  ansehen,  vie  die  von Gdn.  KZ.  25.  562  vorgeschlagene.  Zu  Heti und  Auge  passt  am  besten  ein  dritter  Körper- ■  "'     "      '■     lusschneiden  aus  dem  Kadai
s  Zaubers  ge- i  Yt. /j.a?. I      ai.  .i'Wfl-  I ,  nur  KompA.;  sva.  'ginoa-.l         .'  ■^^*  '
bestehen 5-  357.
j.  gaii'a  N.  /J;  lies  ^jäii™.
'  j  guSa-  m.  Name  einer  Abzweigung, ;ines  Seitenarmes  der  Ranhä:  Um  yazata .k3r?säsp5  upa  -Mm  apay:är>m  rankay^
;  •  j.  gül^a-  n.  'Schmutz,  Kot'.
```


## [2026-09-06T02:18:47.498Z] TOOL CALL #22: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py && echo \"=====\" && sed -n '1,50p' tools/ref_page.py"
}
```


### [2026-09-06T02:18:47.619Z] TOOL RESULT

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
    fetch_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc.encode("idna").decode(),
                                         urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;="),
                                         urllib.parse.quote(parts.query, safe="=&%:/?+"), parts.fragment))
    os.makedirs(WEB, exist_ok=True)
    path = os.path.join(WEB, h + ".txt")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        print(path); return 0
    status, title, text = 0, "", ""
    try:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Language": "en"})
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
=====
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
```


## [2026-09-06T02:18:53.081Z] TOOL CALL #23: Bash

```json
{
 "command": "for p in 1862 1339 1783; do echo \"=========== BQT:$p\"; timeout 600 python3 tools/ref_page.py BQT:$p --image 2>&1 | head -60; done",
 "timeout": 900000
}
```


## [2026-09-06T02:18:56.182Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON غانقرایا / قانقرایا ===\"\ngrep -n 'غانقرا\\|قانقرا\\|غانغرا\\|غانقر' MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10\necho \"=== MON کنگره ===\"\ngrep -n 'کنگره' MON_part1.txt MON_part2.txt 2>/dev/null | head -10\necho \"=== PLA jauhar ===\"\ngrep -n -i 'gauhar\\|ǧauhar\\|jauhar\\|gōhr' incoming/PLA/PLA_pages.txt | head -20"
}
```


### [2026-09-06T02:19:09.340Z] TOOL RESULT

```
=========== BQT:1862
(no exact page map; using offset -1205 -> pdf page 657; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1862.png
REF: BQT:1862  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 657  OCR-lang: fas

کوکردايك ی شاخ

ممدنی است وآن بخاری باشد دخانی که بعضی | است و آن پرنده‌است منحوی که در وبراما

ازآن درزیر زمین منجمد میشود وبعطی ازفرجها | و خرابپا بسربرد و بیشتر شبها پروا زکندوبفتح

و تراکهای کوه برمباید و در اطراف‌آنها برروی | اول؛ پشمینه‌است‌با موبهای آويخته و آنرادروبشان

هم می‌نشیند وکوکرد میشود . گوگرداخمر | پوشند و بعربی دلق کویند -

از جواهر است ومعدن‌آن دروادی موران میباشد گولاج ۷ - بنم اول و ثانی مجپول

د موران آجا مقابل پزی میشوند. گوبند درشب و لام بالف کشیده وجیم ساکن ؛ نام حلوائی‌است

مانند آتش میدرخشد چنانکه روشتای ان چند که‌آنرا لابرلا میگویند .

فرسخ میرود » وچون از ممدن بیرون آورنداین :

‌ 2 ‌ مر ود ین لاد ‌ زان ۰ 1 ۱
خاصیت ندارد وآن جزواعظم | کسیر است‌چنانکه ۱ گو بر وزن فولاد , نام پهلوانی
8 ست ابرالی .

سدماب را ایوالارواح خوانند و آبرا ابوالاجا

غماب را ابوا«رواح و و آلرا ایوااجاد ۸ 1

بامند .گرم و خشك است در چهارم و اقام آن گولانج < بسکون نون و جیم »

مناقع بسیار دارد (۱). بمعنی گولاج است که نوعی از حلوا باشد ؛وبسنی
گو گر دانك ۱ - با دالبالف کنید. گوبند ای است در غایت تراکت که ازسنید

و فتح نون و اسکون‌کاف » سر کین گردانك باشن | ام مرح دا پز رد کر 2

واو را عربان (۹) جعل و خنفاء خوانندوترکان و خورئا , .۰ 1

قیقو رگوبند . گولح « با انی مجعول بر ون

8 زخ .» خرن باش که آشگاه حما

گو که - بنم اول و ثانی مجهول وفتح ددع بمعنی گلخن باشد ۴

کاف فارسی » بمعنی اول گوساله باش د که‌بچة کاو ولخ. ۱۰ اب 0

است ۲ - وبمعنی کوك هم‌هست که کو ی گرببان لخن « با ثانی مجپول بر وزن

و تکمه باشد ۴ - و دانپایی را نیز گوبند سخت کوهکن » بمعنی گاخن است که آنشگاه حمام

که در اعضای آدمی بهم میرسد و درد نمیکند باشد. . :

و پخته نمیشود وآنر! بفارسی آژخ وبعربی ثوّلول گولغنچه ۱ پم اول وغین نقطه‌دار

خوانند ۴ » و معربآن قوقه است . وسکون نون و فتح جیم فارسی, غازه و کلگوه
کول - بنم اول بر وزن غول » بمعنی زنان راگویند و آن سرخبی باشد. که بر دوی

ابله و نادان باشد - و بمعنی مکر و فرب هم | مالند ۰

=========== BQT:1339
(no exact page map; using offset -1205 -> pdf page 134; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1339.png
REF: BQT:1339  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 134  OCR-lang: fas

گفتار شانردهم

از کناب بردان قاطع در حروف طای ,ی نقطه با حروف

تمجی «بتنی بر دوازده بیان و محنوی بر بکصد و هفتاد

وشش!؟ لغت و کنایت و بك انجام که آ نم محتوی است

برشش لغت و کذایت که اول ۱۸۲ ظای تقطه دار باشد)

بیان اول
در طای بی نقطه با الف مشتمل بر سی و نه لغت و کنایت

* طاخگ - با خای شله دار (م) بر | اکر بهایم بر که آلرا بخورند بمیرند.
وزن آحك ۰ لوعی از درخت است که آنرا طاق طار طقه - بذتح‌رای بی‌قطه(2 اوسکون
کوبند و بعربی علقم حوانند , و بعشی کوبند | طای حطی (0) و قاف مفتوح . دانه‌ایست که‌آبرا
طاخك میوء درخت طاق است, وبعضی کوبندنمره | ماءوب دانه ‎)٩(‏ کوبند و پعربی حب الملو3
درختی‌است که آن‌رادر گر کانزهرزمین کوبند۱ . | خوانند ۴ . واین غیر حب اللاطین است.

(۱) چك : ۰.۱۷۲ () چك : ظا باشد. (۳) چك : با خا.

(4) چك : بفتح راء (م) چك : طا .

‎)٩(‏ چك : ماهورانه . رك : ماهودانه . ماهوب دانه.

‏*#ط (طاء) - حرف نوزدهم از الفبای فارسی و حرف شانزدهم از الفیای عربی » و دز
حاب<ملآ ترانه ۳ کگیرند این حرف در لغات‌بارسی‌یت ودر کامات دخیل‌آبرا مانند (ت) تلفظ
کنند و درعربی تلفظ آن از چسبالیدن حصهٌ مقدم زبان بسقف دهان ودمیدن لس صورت کیرد.

‏۹« مننسکی بنند فرهنگه شموری می دربسد که لفظ طاخك بزبان طبرستان بممنی‌درختی

‏" است که بعضی آبرا طفك با طاوغین وطاق نیز کوبند ودرتدتیق‌انت طنك بسند کتاب عذ کور می

‏نود که آن شیبه بدرخت سرو وبا درخت صنوبر است > «چك ص4۹۷ ح». « طاخك * زیتون
بلخ * 820087265 هناه۸4 ۰ نابتی ۱۹۹*. ۲ دمو نام (ض) دنك یس۳۹۹

=========== BQT:1783
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1783.png
REF: BQT:1783  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 580  OCR-lang: fas

۱۷۸۳۳-< کرایید
ومیل کنندمرا نیز کوبند که‌فاعل‌باشد۱ -ویمعلی | وبنده را نیز گفته‌اند که در مقابل آزاداست۸ .
شبه و مانند هم آمده است چنانکه اکرکسی گراید * - یک اول وفتح‌اولهردو
بکسی شباهتی داشته باشد کوبند که بفلانی | آمده‌است پروزن‌بباید ونباید» یمتی قصدوآهنگه
میگراهد (۱) یمتی بفلانی میماند ۴ . کند ومیل و رغبت لماید - و بمعنی پیچد هم
گرای ؟ -بکر اول وثانی بالف آمده است (۲)) بعنی نافرمانی کند چنانکه
کشیده و بتختانی زده » بمعنی هیل و رغبت گفته‌اند :
وخواهش وقصد و آهنگه باشد ۴ - و بمعنی شپنشاها توآن شاه ی که کردون
گرفتن دست‌وپای ودامن ‏ و کمرهم هت-وبمعنی نیارد کز جنات سر کراید ۰
سنگین ونقیل وگران م آمده است* -وحمله گرایستن*۱- یبکراول وفتح‌اول‌هر دو
را نیز کوبند پعنی چیزبرا مانند چوب و اسنگه آمده است بر وزن بداستن و نداستن » بمعنی
وامثال آن برداشتن و بجانب کسی اندا ز کرون | قصدکردن و آهنگه‌نمودن ومیل وخواهش کردن
و نبنداختن و پا دویدن بطرف کی بتصد زون | باشد - و بمعنی پیچیدن هم آمده است که
ونزدن - و امر باین معنی هم هست بمنی میل نافرمانی کردن باشد .
نمای وقصد و حمله کن - و میل وقصد و حمله گرایش ۱مبکراول‌وفتح اول بروزن
کننده را نیز کوبن د که فاعل باشد ‎٩‏ - و بفتح. نمایش وستاش هر دو آمده است » بمعنی قصد
اول و تخفیف نانی » هم بمعنی مذ کوره واهم | وآهنگه - ومیل وخواهش ۱۳- و پیچش باشد
لقب‌پادشاهان نانار باشد ۷ چنانکه پادشاهان عجم | که از نافرمانی کردن است .
را کی‌وروم را قیصر ونركرا خان کوبند-وباتشدید گر انید؟۱- یکسراول وفتح‌اول,ماضی
ثانی. دلاه وسرنراش و حجام را میگویند ۸ - | کراییدن است بمنی‌ضد وآهنگه‌ومیل‌وخواهش
(۱) چك. چش, خم۱: میگرآیده و صحیح قباسی‌است. ‏ (۷) چش : پیجاند هم هست.
۱ - اسم فاعل مرخم. ۴ - «اکر کسی‌یکی ماند کوبند : بفلان همی کراهد :
پمنی همی ماند . رودکی (سمرفندی) گفت :
ای دربخ آن حر هنگام سخا حاتم قش ای دربخ آن کو هنگام وغا سام کراه . >
«لغت فرس چاپ هرن‌س ۰۴*۱۱۷
۳ <کراه (ه.م.) رد :گرایدن »گرایتن ۳ - رك : لغت فرسی چاپ اقبالص ۰.۵۷4
۵-اظ . مصحف «کران» . ‎٩‏ - اسم فاعل مرخم . ۷ -کرای ( بکس
اول) عنوان خانان قربم (کریمه) بود وایشان از خاندان طفا تیموری از اعقاب چنگیزخان‌هتند.
اولین‌خان این‌سلسله حاجی کرای (حدود۸۷۱-۸۲۳ ۸.) است وآخرین‌آنان شاهین کرای(۱۱۹۱-
۷ ) است.رجوع بطبقات سلاطین اسلام. لي پول ترجمهٌ اقبال ۲۱۲-۲۰۷ و قاموس‌الاعلام
سامی «کرای؛شود. ‏ ۸ - ر4:کرا. ‎٩‏ - فل‌مضارع ازهکراییدن» و«کرایتن». ‏ ۱۶ از :
کرای (ه.م.) + ستن (یوند مصدری) * کراییدن : جزواول دراوراق‌مانوی بپارتیلا*87 (متمایل
شدن, لیز خوردن ‏ افتادن ) , 3505 ,و ...۳۵۲۹1۵8 ۸/1:04016 ۵۲ 191 ۸ ,02008ع17)
(0.82 و1 ,126 ۱۱ از :کرای (ه.م.)+ش (اسم‌مضدر). رك: اسم مصدر بقلم نگارنده ص۲۸
۴۳- کهی دل برفتن کرایش کند کهی خواب را س ستایش‌کند. -
نظامی کنجوی . بنقل فرهنگه سروری .
۴ ماضی از «گراییدن» .
```


### [2026-09-06T02:19:09.458Z] TOOL RESULT

```
=== MON غانقرایا / قانقرایا ===
MON_part2.txt:461:غانغرایا: |[ - غانقرایا» معر. فساد؛ 
MON_part2.txt:463:وسیع از یکك عضو. پیدایش غانغرایا بر اثر 
MON_part2.txt:469:مشخص از یکك عضو ابتلابه غانغرابا و 
MON_part2.txt:476:موضعی می‌باشند. غانغرابای خشک تقر سا 
MON_part2.txt:477:بدون بو است ولی غانغرایای مرطوب دارای 
MON_part2.txt:7300:و گیاهی. فساد عضو: (ز.) قانقرایا. فساد 
MON_part2.txt:36554:دیر پر د. و مرده: کت غانغرایا. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:461:غانغرایا: |[ - غانقرایا» معر. فساد؛ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:463:وسیع از یکك عضو. پیدایش غانغرایا بر اثر 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:469:مشخص از یکك عضو ابتلابه غانغرابا و 
=== MON کنگره ===
MON_part2.txt:12488:۵ کنگره یی می‌سازد. جام گل دارای ۵ 
MON_part2.txt:25513:فلاخن. سوراخ‌هایی که در زیر کنگره‌های 
MON_part2.txt:27404:کنگ ۲ (- کنگری - کنگره] (.) 
MON_part2.txt:27427:کنگره: 6 (.) مجمعی از سران دول 
MON_part2.txt:28942:قانونی. سنگی که بر کنگره‌های قلعه 
MON_part2.txt:62184:کنگره‌دار. 
MON_part2.txt:63118:گوناگون گچ‌بری کنند+ کنگرهدار» قرنیزدار. 
MON_part2.txt:66242:رایت؛ درفش. رایتی که بر کنگره‌های برج 
MON_part1.txt:31169:با سه کنگره شده است. جام گل این گیاهان 
MON_part1.txt:48347:کنگره بیشاهنگان. 
=== PLA jauhar ===
5889:       gauhar            (p. s)                 a
5896:»2rs> - Jauhar-fard:                                 "Atom"       s.    Zauhar,
```


## [2026-09-06T02:19:35.404Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON 455-480\"; sed -n '455,480p' MON_part2.txt\necho \"=== MON 27400-27435\"; sed -n '27400,27435p' MON_part2.txt\necho \"=== PLA 5880-5900\"; sed -n '5880,5900p' incoming/PLA/PLA_pages.txt\necho \"=== PLA pdf page tag near\"; awk 'NR>=5700 && NR<=5900 && /pdf page/' incoming/PLA/PLA_pages.txt | tail -5"
}
```


## [2026-09-06T02:19:37.327Z] TOOL CALL #26: Bash

```json
{
 "command": "pdftoppm -f 199 -l 199 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg199 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T02:19:37.447Z] TOOL RESULT

```
=== MON 455-480

جنگل‌های شمالی ايران نیز می‌روید؛ شجرة 
التامول» توس » قان» غوش. سندر» سندر 
آغاجی؛ غوش آغاجی» غین» قین» غو شه» 
شجرة البتو لا. 

غانغرایا: |[ - غانقرایا» معر. فساد؛ 
عفونت ] (.) (پز.) مردکی يا ناحيةٌ کم و بیش 
وسیع از یکك عضو. پیدایش غانغرایا بر اثر 
عفونت‌های مزمن موضعی در اعضا حاصل 
می‌شود ولی چون امروزه آنتی‌بیو تیک‌های 
ای دیده 
می‌شو د. ها عانغرایا در انساج مختلف 
نمهای گونا گون خوانده می‌شود. ریا 
مشخص از یکك عضو ابتلابه غانغرابا و 
مردگی بیدا کر ده باشد بنام اسفاسل خوانده 
می‌شود و مردگی قسمت کمتری از اعضا را 
یو زا بنام نکروز می‌نامند و قطعات مردة 
جدا شده از استخوان را بنام سکستر می‌نامند 
و همچنین غانفرایای انساج نرم را بنام اسکار 
یا بنفش رنگ می‌شوند و دارای سردی 
موضعی می‌باشند. غانغرابای خشک تقر سا 
بدون بو است ولی غانغرایای مرطوب دارای 
بوی گندیدگی می‌باشد. 


=== MON 27400-27435
سانتیمتر و سافه‌اش دارای انشعابات سیار 
هک در آفر یقای شمالی و اروپا و 
آسیای غربی به فراوانی می‌روید؛ خرشوف 
بری» زندالعید» انگنار وحشی؛ کارلین 
کنگ ۲ (- کنگری - کنگره] (.) 
(مس.) سازی است که در هندوستان متداول 
است و آن م رکب است از چوبی بلند که بر 
آن دو تار بسته است و بر هر طرف چوب 
کدوبی نصب شده. 

کنگر: 09۱080۲( (.) قسمی گدا که شاخی و 
شانهٌ گوسفندی بدست گیرد و بر در خانه‌ها 
و دکان‌های مردم آید و آن شاخ را بر آ 
شانه مالد تا از آن صدای غرغری یدید آید 
و بدین وسیله چیزی طلبد. اگر احیاناً در 
دادن بول اهمال کنند وی کاردی بر اعضای 
خویش زند و خود را مجروح سازد و یا کارد 
را بدست فرزند خود دهد تا وی این کار را 
بکند؛ شاخ‌شانه کش. (ص.) (مسج.) بیحیا؛ 


کنگر ۰ ۵۲۵0۲ (۱.) (جاذ.) بوم» جغد 

کنگر: ییا دای | () کنگر کیر ی 
کنگر ه: (2۵۳0-)0280۲۸[- کنگر ] ((.) پستی 
و بلندی مرتب بالای دبوار؛ دندانه‌های 
بالای دیوار قصر و حصار قلعه» شر فه. 
کنگره: 6 (.) مجمعی از سران دول 
نمایندگان ممالک با دانشمندان که دربارة 
مسایل سیاسی اقتصادی» عملی و غیره بحث 
کنند. مجلس قانون‌گذاری ابالات متحدة 
ارگ 

کنگلک: (مذ.)] (.) پیراهن» 
کنند: ۲۸۰2۰۵ (.) افزاری است چاه کنان 

=== PLA 5880-5900
11.       Mackenzie               s.    v.
12.       Brockelmann                  s.    v.
%ün                                                                          101                                                     Baisarän

                                                                                                                   _
&»-      3ün:       eine         Stadt           in    der    Provinz             Fars      aus     pers.    ©)    gun    1,


>=e - Bauhar:                   "Juwel"              aus    dem    pers. ‚- göhar 2 m.                            Zr      göhr       3, mand.
       gauhar            (p. s)                 a

el. -         $awähir:              Pl.         v.    Bauhar       s.       Zauhar        5


Dep - $auhardi:                           "Juwelier"              s.    Zauhar.

»2rs> - Jauhar-fard:                                 "Atom"       s.    Zauhar,


 oPr-              £auhara:              "ein         Schmuckstück"                nom.       un.   v.    Bauhar     6 G-      ve.

=== PLA pdf page tag near
```


### [2026-09-06T02:19:39.717Z] TOOL RESULT

```
total 26280
drwx------ 2 sfmqrb sfmqrb   12288 Sep  5 22:19 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top598.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top599.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top601.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24918 Sep  5 16:58 tops2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  5 16:57 tops.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
-rw-rw-r-- 1 sfmqrb sfmqrb     738 Sep  5 17:04 xang.txt
```


## [2026-09-06T02:19:48.929Z] TOOL CALL #27: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg199.png"
}
```


### [2026-09-06T02:19:49.451Z] TOOL RESULT

```

```


## [2026-09-06T02:19:49.449Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T02:20:04.598Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 199 -l 199 -r 450 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg199hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg199hi.png'); print(im.size)\nw,h=im.size\n# greek box approx x 0.23-0.40, y 0.30-0.34 of page (from 1700x2200 view: x 370-600, y 600-650)\nim.crop((int(w*0.20),int(h*0.263),int(w*0.40),int(h*0.30))).save('p199_greek.png')\nim.crop((int(w*0.50),int(h*0.255),int(w*0.78),int(h*0.30))).save('p199_pgang.png')\n\"\nls -la p199_greek.png p199_pgang.png"
}
```


### [2026-09-06T02:21:16.523Z] TOOL RESULT

```
(3825, 4950)
-rw-rw-r-- 1 sfmqrb sfmqrb 2361 Sep  5 22:21 p199_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb 2503 Sep  5 22:21 p199_pgang.png
```


## [2026-09-06T02:21:24.244Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg199hi.png'); w,h=im.size\nim.crop((int(w*0.20),int(h*0.285),int(w*0.42),int(h*0.325))).save('p199_greek.png')\nim.crop((int(w*0.52),int(h*0.285),int(w*0.80),int(h*0.325))).save('p199_pgang.png')\n\" && ls -la p199_greek.png p199_pgang.png"
}
```


### [2026-09-06T02:21:26.705Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 3718 Sep  5 22:21 p199_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb 4112 Sep  5 22:21 p199_pgang.png
```


## [2026-09-06T02:21:28.968Z] TOOL CALL #30: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p199_greek.png"
}
```


### [2026-09-06T02:21:28.996Z] TOOL RESULT

```

```


## [2026-09-06T02:21:33.018Z] TOOL CALL #31: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p199_pgang.png"
}
```


### [2026-09-06T02:21:33.040Z] TOOL RESULT

```

```


## [2026-09-06T02:21:56.245Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg199hi.png'); w,h=im.size\nc=im.crop((int(w*0.66),int(h*0.297),int(w*0.79),int(h*0.318)))\nc=c.resize((c.width*3,c.height*3), Image.LANCZOS)\nc.save('p199_pgang_zoom.png')\nprint(c.size)\""
}
```


### [2026-09-06T02:21:58.138Z] TOOL RESULT

```
(1491, 312)
```


## [2026-09-06T02:23:08.758Z] TOOL CALL #33: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p199_pgang_zoom.png"
}
```


### [2026-09-06T02:23:08.774Z] TOOL RESULT

```

```


## [2026-09-06T02:23:30.000Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/%DA%AF%D9%88%D9%87%D8%B1' \\\n 'https://en.wiktionary.org/wiki/gotra' \\\n 'https://en.wiktionary.org/wiki/%CE%B3%CE%AC%CE%B3%CE%B3%CF%81%CE%B1%CE%B9%CE%BD%CE%B1' \\\n 'https://www.etymonline.com/word/gangrene' \\\n 'https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D8%A7%DB%8C%DB%8C%D8%AF%D9%86' \\\n 'https://www.etymonline.com/word/grade' ; do\n echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note 'page 199 verification (Gôtra/gohar, Gras/gangrene, Gredh/grāyīdan, grade)'\ndone",
 "timeout": 600000
}
```


### [2026-09-06T02:23:38.400Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%DA%AF%D9%88%D9%87%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/2962869496df17af.txt
### https://en.wiktionary.org/wiki/gotra
/home/sfmqrb/git/rishe/data/verification/sources/web/3faa9dfd66ec3bdc.txt
### https://en.wiktionary.org/wiki/%CE%B3%CE%AC%CE%B3%CE%B3%CF%81%CE%B1%CE%B9%CE%BD%CE%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/66286b1b8b1d434e.txt
### https://www.etymonline.com/word/gangrene
/home/sfmqrb/git/rishe/data/verification/sources/web/5dc3f850d38b01df.txt
### https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D8%A7%DB%8C%DB%8C%D8%AF%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/1ebda902b2fade4c.txt
### https://www.etymonline.com/word/grade
/home/sfmqrb/git/rishe/data/verification/sources/web/b35570b9aa7c3bbd.txt
```


## [2026-09-06T02:23:41.475Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 2962869496df17af 3faa9dfd66ec3bdc 66286b1b8b1d434e 5dc3f850d38b01df 1ebda902b2fade4c b35570b9aa7c3bbd; do\necho \"########## $f\"; grep -n -i -A12 'Etymology' $f.txt | head -70; done"
}
```


### [2026-09-06T02:23:43.158Z] TOOL RESULT

```
########## 2962869496df17af
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
--
172: Etymology
173- [ edit ] 
174-
175- Inherited from Middle Persian gwhl ( /⁠gōhr, gōhar⁠/ , “ substance, essence; jewel ” ) . See there for more.
176-
177- Pronunciation
178- [ edit ] 
179-
180- ( Classical Persian ) IPA ( key ) : /ɡaw.ˈhar/ 
181-
182- ( Dari, formal ) IPA ( key ) : [ɡäw.háɾ] 
183-
184- ( Dari, formal ) IPA ( key ) : [ɡäw.háɾ] 
########## 3faa9dfd66ec3bdc
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.3 
68- Anagrams 
69-
70- Toggle the table of contents 
71-
72- gotra 
73-
74- 3 languages 
--
141: Etymology
142- [ edit ] 
143-
144- PIE word 
145- *gʷṓws 
146-
147- From Sanskrit गोत्र ( gotra ) .
148-
149- Noun
150- [ edit ] 
151-
152- gotra ( plural gotras ) 
153-
########## 66286b1b8b1d434e
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Inflection 
75-
76- 1.4.2 
77- Derived terms 
--
174: Etymology
175- [ edit ] 
176-
177- In antiquity it was compared with γράω ( gráō , “ to devour ” ) (a theory which Etymonline corroborates), but this is likely incorrect. It is most probably a Pre-Greek word.
178-
179- Pronunciation
180- [ edit ] 
181-
182- IPA ( key ) : /ɡáŋ.ɡrai̯.na/ → /ˈɣaŋ.ɡrɛ.na/ → /ˈɣaŋ.ɡre.na/ 
183-
184- ( 5 th BCE Attic ) IPA ( key ) : /ɡáŋ.ɡrai̯.na/ 
185-
186- ( 1 st CE Egyptian ) IPA ( key ) : /ˈɡaŋ.ɡrɛ.na/ 
########## 5dc3f850d38b01df
4:TITLE: Gangrene - Etymology, Origin & Meaning
5-
6:Gangrene - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
13- Apps 
14- Premium 
15-
16- Log in 
17-
18- Advertisement Remove Ads 
--
89: <a href="https://www.etymonline.com/word/gangrene">Etymology of gangrene by etymonline</a> Copy 
90-
91- APA Style :
92: Harper, D. (n.d.). Etymology of gangrene. Online Etymology Dictionary. Retrieved September 6, 2026, from https://www.etymonline.com/word/gangrene Copy 
93-
94- Chicago Style :
95: Harper Douglas, "Etymology of gangrene," Online Etymology Dictionary, accessed September 6, 2026, https://www.etymonline.com/word/gangrene. Copy 
96-
97- MLA Style :
98: Harper, Douglas. "Etymology of gangrene." Online Etymology Dictionary, https://www.etymonline.com/word/gangrene. Accessed 6 September, 2026. Copy 
99-
100- IEEE Style :
101: D. Harper. "Etymology of gangrene." Online Etymology Dictionary. https://www.etymonline.com/word/gangrene (accessed September 6, 2026). Copy 
102-
103- Remove Ads 
104- Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
105-
106- Trending 
107-
108- Dictionary entries near gangrene 
109- ganglia 
110- gangling 
111- ganglion 
112- gangly 
113- gang-plank 
########## 1ebda902b2fade4c
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Verb 
72-
73- 1.4.1 
74- Conjugation 
75-
76- 1.4.2 
77- Derived terms 
--
155: Etymology
156- [ edit ] 
157-
158- Inherited from Middle Persian [Book Pahlavi needed] ( HYMNN-stn' /⁠wurrōyistān⁠/ , “ to believe, to choose (a religion) ” ) , ultimately from Proto-Iranian *war- ( “ to choose, to believe ” ) . [ 1 ] Compare Avestan 𐬬𐬀𐬭- ( var- , “ to believe ” ) .
159-
160- Pronunciation
161- [ edit ] 
162-
163- ( Classical Persian ) IPA ( key ) : /ɡa.raː.jiː.ˈdan/ , /ɡi.raː.jiː.ˈdan/ 
164-
165- ( Dari, formal ) IPA ( key ) : [ɡä.ɾɑː.jiː.d̪án] , [ɡɪ.ɾɑː.jiː.d̪án] 
166-
167- ( Dari, formal ) IPA ( key ) : [ɡä.ɾɑː.jiː.d̪án] , [ɡɪ.ɾɑː.jiː.d̪án] 
########## b35570b9aa7c3bbd
4:TITLE: Grade - Etymology, Origin & Meaning
5-
6:Grade - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
13- Apps 
14- Premium 
15-
16- Log in 
17-
18- Advertisement Remove Ads 
--
104: <a href="https://www.etymonline.com/word/grade">Etymology of grade by etymonline</a> Copy 
105-
106- APA Style :
107: Harper, D. (n.d.). Etymology of grade. Online Etymology Dictionary. Retrieved September 5, 2026, from https://www.etymonline.com/word/grade Copy 
108-
109- Chicago Style :
110: Harper Douglas, "Etymology of grade," Online Etymology Dictionary, accessed September 5, 2026, https://www.etymonline.com/word/grade. Copy 
111-
112- MLA Style :
113: Harper, Douglas. "Etymology of grade." Online Etymology Dictionary, https://www.etymonline.com/word/grade. Accessed 5 September, 2026. Copy 
114-
115- IEEE Style :
116: D. Harper. "Etymology of grade." Online Etymology Dictionary. https://www.etymonline.com/word/grade (accessed September 5, 2026). Copy 
117-
118- Remove Ads 
119- Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
120-
121- Trending 
122-
123- Dictionary entries near grade 
124- grad 
125- -grad 
126- gradate 
127- gradation 
128- gradational
```


## [2026-09-06T02:23:54.328Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"##### etymonline gangrene body\"; sed -n '20,70p' 5dc3f850d38b01df.txt\necho \"##### etymonline grade body\"; sed -n '20,80p' b35570b9aa7c3bbd.txt"
}
```


### [2026-09-06T02:23:54.376Z] TOOL RESULT

```
##### etymonline gangrene body

 Origin and history of gangrene 

 gangrene (n.) 

 "putrefaction or necrosis of soft tissues," 1540s, cancrena , from Latin gangraena (Medieval Latin cancrena ), from medical Greek gangraina "an eating or gnawing sore," literally "that which eats away," a dissimilated, reduplicated form of gran- "to gnaw," from PIE root *gras- "to devour" (see gastric ).
 also from 1540s 

 Entries linking to gangrene 

 gastric (adj.) 

 1650s, from Modern Latin gastricus , from Greek gast ē r (genitive gastros ) "stomach, paunch, belly," often figurative of gluttony or greed, also "womb, uterus; sausage," by dissimilation from *graster , literally "eater, devourer," from gran "to gnaw, eat," from PIE root *gras- "to devour" (source also of Greek grastis "green fodder," Latin gramen "fodder, grass," Old English cærse "cress").

 gangrenous (adj.) 

 1610s, from gangrene + -ous . Perhaps modeled on French gangréneux .

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 slough 

 "muddy place in a road or way, mudhole, swamp, deep quagmire," Middle English slough, from Old English sloh "soft, muddy ground," a word of uncertain origin. Compare Middle Low German sloch "muddy place," Middle High German sluoche "ditch." Figurative use (in reference to moral s

 mortify 

 late 14c., mortifien, "to kill, destroy the life of," from Old French mortefiier "destroy, overwhelm, punish," from Late Latin mortificare "cause death, kill, put to death," literally "make dead," from mortificus "producing death," from Latin mors (genitive mortis) "death" (from 

 mortification 

 late 14c., mortificacioun, "mortifying of the flesh, act of subduing the passions and appetites, suppression of bodily desires," from Late Latin mortificationem (nominative mortificatio) "a killing, putting to death," from past-participle stem of mortificare (see mortify). Meanin

 tor 

 "high, rocky hill," Old English torr "rock, crag;" said to be a different word than torr "tower." Obviously cognate with Gaelic torr "lofty hill, mound," Old Welsh twrr "heap, pile;" and perhaps ultimately with Latin turris "high structure" (see tower (n.)). But sources disagree 

 rot 

 Middle English roten, from Old English rotian, of animal substances, "to decay, putrefy, undergo natural decomposition" (intransitive), also of vegetable matter," from Proto-Germanic *rutjan (source also of Old Saxon roton, Old Norse rotna, Old Frisian rotia, Middle Dutch roten, 

 sweat 

 Middle English sweten, from Old English swætan "perspire, excrete moisture from the skin," also "toil, labor, work hard," from Proto-Germanic *swaitjan "to sweat," from the source of sweat (n.). Compare Frisian swette, Dutch zweeten, Danish svede, German schwitzen. The meaning "b

 pathology 

 "science of diseases," 1610s, from French pathologie (16c.), from medical Latin pathologia "study of disease," from Greek pathos "suffering" (from PIE root *kwent(h)- "to suffer") + -logia "study" (see -logy). In reference to the study of abnormal mental conditions from 1842. Anc

 carpenter 
##### etymonline grade body

 Origin and history of grade 

 grade (n.) 

 1510s, "degree of measurement," from French grade "grade, degree" (16c.), from Latin gradus "a step, a pace, gait; a step climbed (on a ladder or stair);" figuratively "a step toward something, a degree of something rising by stages," from gradi (past participle gressus ) "to walk, step, go," from PIE root *ghredh- "to walk, go." It replaced Middle English gree "a step, degree in a series," from Old French grei "step," from Latin gradus .

 Meaning "inclination of a road or railroad" is from 1811. Meaning "class of things having the same quality or value" is from 1807; meaning "division of a school curriculum equivalent to one year" is from 1835; that of "letter-mark indicating assessment of a student's work" is from 1886 (earlier used of numerical grades). Grade A "top quality, fit for human consumption" (originally of milk) is from a U.S. system instituted in 1912. To figuratively make the grade "be successful" is from 1912; early examples do not make clear whether the literal grade in mind was one of elevation, quality, or scholarship.
 also from 1510s 

 grade (v.) 

 1650s, "to arrange in grades," from grade (n.). Meaning "to reduce (a road, etc.) to a level or degree of inclination" is from 1835. Meaning "assign a letter mark to" is from 1931. Related: Graded ; grading .
 also from 1650s 

 Entries linking to grade 

 downgrade (v.) 

 also down-grade , "to lower in rank, status, etc.," 1930, from down (adv.) + grade (v.). Related: Downgraded ; downgrading . As a noun, "a downward slope," from 1858.

 grader (n.) 

 1868, of machines; 1870, of persons, agent noun from grade (v.).

 gradient 
 high-grade 
 intergrade 
 low-grade 
 upgrade 
 *ghredh- 
 See All Related Words (8) 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 level 

 mid-14c., "tool to indicate a horizontal line," from Old French livel "a level" (13c.), ultimately from Latin libella "a balance, level" (also a monetary unit), diminutive of libra "balance, scale, unit of weight" (see Libra). Spanish nivel, Modern French niveau are from the same

 class 

 c. 1600, "group of students," in U.S. especially "number of pupils in a school or college of the same grade," from French classe (14c.), from Latin classis "a class, a division; army, fleet," especially "any one of the six orders into which Servius Tullius divided the Roman peopl

 form 

 c. 1200, forme, fourme, "semblance, image, likeness," from Old French forme, fourme, "physical form, appearance; pleasing looks; shape, image; way, manner" (12c.), from Latin forma "form, contour, figure, shape; appearance, looks; a fine form, beauty; an outline, a model, pattern

 rating 

 Meaning "a classification according to grade or rank" is from 1764....

 honky-tonk 

 about 1893 in newspapers in Texas and Oklahoma; a much-reprinted snippet defines it as "a particularly vicious and low-grade...

 promote 

 late 14c., promoten, "to advance (someone) to a higher grade or office, exalt or raise to a higher post or position," from...
```


## [2026-09-06T02:23:55.240Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"##### گراییدن full\"; sed -n '100,220p' 1ebda902b2fade4c.txt\necho \"##### گوهر descendants\"; sed -n '185,260p' 2962869496df17af.txt"
}
```


### [2026-09-06T02:23:55.301Z] TOOL RESULT

```
##### گراییدن full

 Read 

 Edit 

 View history 

 Tools 

 Tools

 move to sidebar 
 hide 

 Actions

 Read 

 Edit 

 View history 

 General

 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Cite this page 
 Get shortened URL 

 Print/export

 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Alternative forms
 [ edit ] 

 گرایستن ( garāyistan  / garâyestan, girāyistan  / gerâyestan ) 

 Etymology
 [ edit ] 

 Inherited from Middle Persian [Book Pahlavi needed] ( HYMNN-stn' /⁠wurrōyistān⁠/ , “ to believe, to choose (a religion) ” ) , ultimately from Proto-Iranian *war- ( “ to choose, to believe ” ) . [ 1 ] Compare Avestan 𐬬𐬀𐬭- ( var- , “ to believe ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ɡa.raː.jiː.ˈdan/ , /ɡi.raː.jiː.ˈdan/ 

 ( Dari, formal ) IPA ( key ) : [ɡä.ɾɑː.jiː.d̪án] , [ɡɪ.ɾɑː.jiː.d̪án] 

 ( Dari, formal ) IPA ( key ) : [ɡä.ɾɑː.jiː.d̪án] , [ɡɪ.ɾɑː.jiː.d̪án] 
 ( Kabuli ) IPA ( key ) : [ɡä.ɾɑː.jiː.d̪án] , [ɡɪ.ɾɑː.jiː.d̪án] 

 ( Hazaragi ) IPA ( key ) : [ɡä.ɾɔː.ji.d̪án] , [ɡi.ɾɔː.ji.d̪án] 

 ( Iran, formal ) IPA ( key ) : [ɡʲæ.ɹɒː.jiː.d̪ǽn] , [ɡʲe.ɹɒː.jiː.d̪ǽn] 

 ( Tajik, formal ) IPA ( key ) : [ɡä.ɾɔ.ji.d̪án] , [ɡi.ɾɔ.ji.d̪án] 

 Rhymes: -an 

 Readings

 Classical reading ? 

 garāyīdán, girāyīdán

 Dari reading ? 

 garāyīdan, girāyīdan

 Iranian reading ? 

 garâyidan, gerâyidan

 Tajik reading ? 

 garoyidan, giroyidan

 Verb
 [ edit ] 

 گراییدن • ( garāyīdan  / garâyidan, girāyīdan  / gerâyidan ) ( present stem گرا ( garā  / garâ, girā  / gerâ ) or گرای ( garāy  / garây, girāy  / gerây ) , Tajik spelling гароидан ) 

 to incline , to lean (e.g. towards a position, a stance)

 to convert (to a religion)

 Conjugation
 [ edit ] 

 Conjugation of گراییدن ( literary Iranian Persian )

 infinitive

 گراییدن ( gerâyidán ) 

 stem

 present

 گرای ( gerây ) 

 past
##### گوهر descendants
 ( Kabuli ) IPA ( key ) : [ɡä.wáɾ] 

 ( Hazaragi ) IPA ( key ) : [ɡä.wáɾ] 

 ( Iran, formal ) IPA ( key ) : [ɡ̥ow.hǽɹ] 

 ( Iran, formal ) IPA ( key ) : [ɡ̥ow.hǽɹ] 
 ( Tehrani ) IPA ( key ) : [ɡ̥oː.ɦǽɹ] 

 ( Tajik, formal ) IPA ( key ) : [ɡäw.háɾ] 

 Rhymes: -ar 

 Readings

 Classical reading ? 

 gawhar

 Dari reading ? 

 gawhar

 Iranian reading ? 

 gowhar

 Tajik reading ? 

 gavhar

 Audio ( Iran ) : ( file ) 

 Noun
 [ edit ] 

 گوهر • ( gawhar / gowhar ) ( plural گوهرها ( gawhar-hā / gowhar-hâ ) , Tajik spelling гавҳар ) 

 jewel , gem 
 Synonym: جواهر ( jawāhir  / javâher ) 

 pearl 
 Synonym: مروارید ( murwārīd  / morvârid ) 

 essence 
 c. 1260s , Jalāl ad-Dīn Mohammad Rūmī , translated by Reynold A. Nicholson , مثنوی معنوی [ Masnavi-ye-Ma'navi ], volume I, verse 3529: هل مرا تا پرده‌‌ها را بر درم
تا چو خورشیدی بتابد گوهرم hil marā tā parda-hā rā bar daram
tā čō xwarshēd bitābad gawhar -am Let me be, that I may rend the curtains asunder,
that my (spiritual) substance may shine forth like a sun 

 Derived terms
 [ edit ] 

 گوهران ( gawharān  / gowharân ) 
 گوهرخانه ( gawharxāna  / gowharxâne ) 
 گوهرستان ( gawharistān  / gowharestân ) 
 گوهرشناس ( gawharšinās  / gowharšenâs ) 
 گوهرشناس ( gawharšinās  / gowharšenâs , “ lapidary ” ) 
 گوهرفروش ( gawharfurūš  / gowharforuš , “ jeweler ” ) 
 گوهرفروشی ( gawharfurūšī  / gowharforuši ) 
 گوهری ( gawharī  / gowhari ) 

 Descendants
 [ edit ] 

 → Arabic: جَوْهَر ( jawhar ) ( see there for further descendants )

 → Azerbaijani: gövhər 

 → Bashkir: гәүһәр ( gäwhär ) 

 → Chagatai: گوهر ( gwhr ) 
 Uyghur: گۆھەر ( göher ) 

 Uzbek: gavhar
```


## [2026-09-06T02:24:23.299Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG gray/graH ===\"\ngrep -n -E '\\*gra|GRAY|GRA[HYĀ]|grāy' CHEUNG.txt | head -30\necho \"=== PHD grāy ===\"\ngrep -n -o -E '.{80}gr.y-?[ ,\\[].{80}' PHD_mackenzie.txt | head -10\necho \"=== HRN neigen ===\"\ngrep -n -i 'neigen' HRN.txt | head -10\necho \"=== IEC ghredh ===\"\ngrep -n -i -E 'ghredh|gr̥dhi|gradior' IEC.txt | head -10\necho \"=== SYN gohar/gotra ===\"\ngrep -n -i -E 'gauhar|gōhr' SYN.txt | head"
}
```


### [2026-09-06T02:24:25.011Z] TOOL RESULT

```
=== CHEUNG gray/graH ===
8126:*MIDDLE PERSIAN: MMP gry-, BMP gl(y)dy- /griy-/ ‘to weep’ (< OP *grad-ya-) || 
8554:*grabH 119 
8589:*grabH ‘to grab, seize, take’ 
8618:120 *grabH 
8658:different continuations of *grabH in Chor., see Humbach 1973: 95. = Samadi: 234 
8671:*grait/grai0 ? 121 
8713:*graH ? ‘to smell’ 
8726:*grait/graiO ? ‘to roar, scold’ 
8730:122 *gram 
8770:© The variant *gran- with final -n, attested in several ЕП. languages, is no doubt 
55324:*grabH (s.v.), *uat, *zanH? 
57486:*graH, *sad 
57644:*earj , *grait/erai9, *eram, 
57680:*grait/graiG, *Hrais (s.v.), 
58224:*earj', *gram, *nar 
=== PHD grāy ===
=== HRN neigen ===
23280:Meinung zuzuneigen, dass ai. löhd- etc. keine echt-
=== IEC ghredh ===
4898:(ghredh-, see ghréio, ghrés-)
=== SYN gohar/gotra ===
```


## [2026-09-06T02:24:32.078Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG lean/incline ===\"\ngrep -n -i -E \"'to (lean|incline|bend)\" CHEUNG.txt | head -20\necho \"=== CHEUNG index gerayidan ===\"\ngrep -n -i -E 'gerāyīdan|gerayidan|garāy|grāy' CHEUNG.txt | head -20\necho \"=== IEC 4890-4910 ===\"\nsed -n '4890,4910p' IEC.txt"
}
```


### [2026-09-06T02:24:32.161Z] TOOL RESULT

```
=== CHEUNG lean/incline ===
=== CHEUNG index gerayidan ===
=== IEC 4890-4910 ===
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
“mask, visor’; Li. greimas ‘film, top skin (ghreio, ghreiio (?) “requirement, responsi- bility, need, debt, obligation. see ghrées-. The evidence is limited to Gk., cf. khr&, khreía, khreía, f. beside khréos, Do- ric: khréos, id., and khr&me, id. A possible iso- phone is Skt. hràsah ‘decrease, detriment’, of uncertain origin. Per. garàyam = ‘incline, tend' ghrem- (1) ‘roar, rage, rumble’. WP I, 655. Cf. guhrem- and next
337
Gk. cf. khremetízo ‘neigh, snort’; MHG grim- men “rage, roar; ON grimmast, refl. id.; R cf. greméti, id. Cf. also MHG grim(me) ‘grim, furious’; ON grimmmr, id.; OE grimman, grims- ian ‘rage’; grimm as MHG. O-gde gram ‘fierce, raging’; MHG gram, id. (and "rage
ghrem- (2) ‘hawk, cough up? Gk. cf. khrémma  expectoration' beside khrémptomai 'expectorate'; o-gde in Li. gra- mai 'expectoration, phlegm'. Isophonic are Lith. grémziu, -ti ‘scrape, upbraid'; Latv. gremZu, gremzt ‘gnaw; roar. See guhrem- however. For Alb. gromé ‘belch’: Latv. gre- mens, see guhrem-)
ghrendhilos (ghrendhlo-) “bar, shaft. Cf. ghrendhos (2) and WP I, 657 OHG grintil; MHG.OE grindel; MLG.Du. grendel; OCz. hřiedel, Cz. hřídel & *axle-tree; plow-handle’; hfedlo ‘windlass’; Pol. gradziel *plowbeam; shaft of cart). (It is uncertain if the SI. forms derive from Germanic)
(ghrendho “crush, grind, trample; grunt, growl, bellow’. See guhrendh-)
ghrendhos (1), (gherndos) ‘scrapings, scab, dandruff, rubble’ Gk. kherádos, n. ‘gravel, rubble, wrack’; Alb. (ambig.) grêndë ‘rock, cliff; OIr. grend, grenn ‘bristle, beard’; MIr. greann, id.; Olr. cf. grinn ‘sharp’; grinne ‘keenness; spearhead’; Ir. cf. grinn-eall ‘seabed, lake-bed’; OE grinde ‘shingle’; MHG grint, gs -des, sm. 'scurf'. Cf. guhrendh-
```


## [2026-09-06T02:24:47.987Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/gwhl' \\\n 'https://en.wiktionary.org/wiki/%D8%AC%D9%88%D9%87%D8%B1' \\\n 'https://www.etymonline.com/word/congress' \\\n 'https://www.etymonline.com/word/degree' ; do\n echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note 'page 199 verification (MP gōhr; Arabic jawhar; congress; degree)'\ndone",
 "timeout": 600000
}
```


### [2026-09-06T02:24:53.960Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/gwhl
/home/sfmqrb/git/rishe/data/verification/sources/web/3ffaad62030861f4.txt
### https://en.wiktionary.org/wiki/%D8%AC%D9%88%D9%87%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/c90d1a1b94dad307.txt
### https://www.etymonline.com/word/congress
/home/sfmqrb/git/rishe/data/verification/sources/web/f8f3349a9b9772ae.txt
### https://www.etymonline.com/word/degree
/home/sfmqrb/git/rishe/data/verification/sources/web/b0ef1c1c16423c42.txt
```


## [2026-09-06T02:24:57.667Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"##### gwhl\"; grep -n -A8 'Middle Persian' 3ffaad62030861f4.txt | sed -n '1,60p'\necho \"##### jawhar\"; grep -n -B2 -A8 'Etymology' c90d1a1b94dad307.txt | sed -n '30,90p'\necho \"##### congress\"; sed -n '20,35p' f8f3349a9b9772ae.txt\necho \"##### degree\"; sed -n '20,32p' b0ef1c1c16423c42.txt"
}
```


### [2026-09-06T02:24:57.779Z] TOOL RESULT

```
##### gwhl
57: Middle Persian 
58-
59: Toggle Middle Persian subsection 
60-
61- 1.1 
62- Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
--
133: Middle Persian
134- [ edit ] 
135-
136- Etymology
137- [ edit ] 
138-
139- Inherited from Old Persian *gauθrā , borrowed from Old Median *gauθrā , from Proto-Iranian *gawθraH ( “ jewel ” ) , related to *gawθrám ( “ family, lineage, growth ” ) . Cognate with Northern Kurdish gewher , Bactrian γωυριγο ( gōurigo ) , Pashto غوره ( ǧwëra ) .
140-
141- Noun
--
180: Categories : Middle Persian terms inherited from Old Persian 
181: Middle Persian terms derived from Old Persian 
182: Middle Persian terms derived from Old Median 
183: Middle Persian terms inherited from Proto-Iranian 
184: Middle Persian terms derived from Proto-Iranian 
185: Middle Persian lemmas 
186: Middle Persian nouns 
187-
188- Hidden categories: Pages with entries 
189- Pages with 1 entry 
190: Middle Persian terms with redundant script codes 
191- Aramaic terms with redundant script codes 
192-
193- This page was last edited on 15 June 2026, at 03:27.
194-
195- Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 
196-
197- Privacy policy 
198-
##### jawhar
114- Pronunciation 
115-
116- 3.3 
117- Noun 
118-
119- 3.3.1 
--
206- [ edit ] 
207-
208: Etymology
209- [ edit ] 
210-
211- Borrowed from Classical Persian گَوهَر ( gawhar ) .
212-
213- Pronunciation
214- [ edit ] 
215-
216- IPA ( key ) : /d͡ʒaw.har/ 
--
734- [ edit ] 
735-
736: Etymology
737- [ edit ] 
738-
739- Borrowed from Arabic جَوْهَر ( jawhar , “ jewel, gem, precious stone ” ) , from Classical Persian گَوهَر ( gawhar , “ jewel, gem ” ) , from Middle Persian gwhl ( gôhr ) .
740-
741- Noun
742- [ edit ] 
743-
744- جوهر • ( cevher ) ( definite accusative جوهری ( cevheri ) , plural جواهر ( cevâhir ) or جوهرلر ( cevherler ) ) 
--
807- Wikipedia fa 
808-
809: Etymology
810- [ edit ] 
811-
812- Borrowed from Arabic جَوْهَر ( jawhar ) , itself from Early Classical Persian گَوهَر ( gawhar ) , from Middle Persian gwhl ( gôhr ) .
813-
814- Pronunciation
815- [ edit ] 
816-
817- ( Classical Persian ) IPA ( key ) : /d͡ʒaw.ˈhar/ 
##### congress

 Origin and history of congress 

 congress (n.) 

 c. 1400, "a body of attendants; also "meeting of armed forces" (mid-15c.); the sense of "a coming together of people, a meeting of individuals" is from 1520s; from Latin congressus "a friendly meeting; a hostile encounter," past participle of congredi "to meet with; to fight with," from assimilated form of com "with, together" (see con- ) + gradi "to walk, step," from gradus "a step" (from PIE root *ghredh- "to walk, go").

 The meaning "sexual union" is from 1580s. The specific sense of "a meeting of delegates, formal meeting of persons having a representational character" is recorded by 1670s. It has been used in reference to the national legislative body of the American states (with a capital C- ) since 1775 (by 1765 in America as a name for proposed bodies).

 The three sittings of the Continental Congress , representing the 13 rebellious American colonies, met 1774, 1775-6, and 1776-81. The Congress of the Confederation met from 1781-89, and the Congress of the United States met from March 4, 1789. The Congress of Vienna met Nov. 1, 1814, to June 8, 1815, and redrew the map of Europe with an eye to creating a balance of powers after the disruptions of Napoleon.
 also from c. 1400 

 Entries linking to congress 

 congressional (adj.) 

##### degree

 Origin and history of degree 

 degree (n.) 

 c. 1200, "a step, a stair," also "a position in a hierarchy," and "a stage of progress, a single movement toward an end," from Old French degré (12c.) "a step (of a stair), pace, degree (of relationship), academic degree; rank, status, position," which is said to be from Vulgar Latin *degradus "a step," from Latin de- "down" (see de- ) + gradus "a step; a step climbed;" figuratively "a step toward something, a degree of something rising by stages" (from PIE root *ghredh- "to walk, go").

 A word of wide use in Middle English; in 14c. it also meant "way, manner; condition, state, standing." Most extended senses in Middle English are from the notion of a hierarchy of steps. Genealogical sense of "a certain remove in the line of blood" is from mid-14c.; educational sense of "an academic rank conferred by diploma" is from late 14c. By degrees "gradually, by stages" is from late 14c.

 Other transferred senses are from the notion of "one of a number of subdivisions of something extended in space or time," hence "intensive quality, measure, extent." The meaning "1/360th of a circle" is from late 14c. (The division of the circle into 360 degrees was known in Babylon and Egypt; the number is perhaps from the daily motion of the sun through the zodiac in the course of a year.) From 1540s as "a measure of heat;" the specific use as a unit of temperature on a thermometer is by 1727. In reference to crime, by 1670s as "one of certain distinctions of culpability;" in U.S. use by 1821 as "one of the phases of the same kind of crime."
 also from c. 1200 

 Entries linking to degree
```


## [2026-09-06T02:25:11.136Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSF گوهر ===\"; grep -n 'گوهر' FSF_pages.txt | head -10\necho \"=== LAT gangraena/gradior ===\"; grep -n -i -E 'gangraena|gradior' LAT.txt | head -10\necho \"=== SKT grade/gangrene ===\"; grep -n -i -E '^grade|gangrene|gradus' SKT.txt | head -10\necho \"=== WEB gangrene ===\"; grep -n -i -o -E '.{0,60}gangraena.{0,120}' WEB_vol1.txt | head -5\necho \"=== SYN 'go' ghredh ===\"; grep -n -i -E 'gradior|ghredh' SYN.txt | head -5"
}
```


### [2026-09-06T02:25:15.354Z] TOOL RESULT

```
=== FSF گوهر ===
1016:        ‫جهان راگوهر آمد زشتکاری‬                     ‫ز کین جویی شده چونان بیآزرم‬
3939:‫مرانیز در تخمه هم گوهرست‬
3954:    ‫چو ناسفته گوهر‪ .‬سه دخترش بود‬                                                             ‫باهو‬
4140:‫(مصحح کتاب‪ .‬سخنور بلندپایه» بهار‬                        ‫بگوی»‪ .‬زن می‌گوید گوهر فروشم و برای‬
5469:                            ‫‪-۳‬گوهر نژاد‪:‬‬            ‫ننمرد مرد‬     ‫جنوشها‪ .‬ا‬
5621:                                                     ‫همه گوهرش پیکر و‬
5625: ‫(‪)۲-۴۰۱۰-۷۲۵‬‬                                  ‫روم که نقش و نگارش از گوهر بود و‬
5842:‫کسی گوهرش را ندانست ارز‬                               ‫(‪)۶-۱۱۳-۹۹۴۱‬‬
5897:      ‫بهبالا ز صد رش فزون هر درخت‬                        ‫گوهری سرخ رنگ شبیه به ياقوت که‬
6627:     ‫خردباید و گوهر نامدار‬                   ‫بریده دل از ترس گیهان خدیو‬
=== LAT gangraena/gradior ===
3292:synonyme de e 5 , gradior, uado avec le sens de "marcher (au pas)",
15510:aation, cf. gradus en face de gradior, et impetus en face de peto);
19498:En coapoaition, ex aarque 1 'idee de sortir: eo/exeo, gradior/egre¬
25435:gangraena ( gangrena, can-), -ae£: gangrene. Emprunt an. gr. yaYYP 011 '"
26595:gradluus: epithete de Mars, ddriv£ de gradior par les Latins,
26607:Gradus est A gradior comme impetus A impeto. - A gradus plutSt
26608:qu'A gradior se rattachent graddtio "gradin" et dans la 1 . de la rhdtor.
26614:gradior,-eris, gressus sum, gradi: marcher. Rare, quoique ancien
26617:doute parce que 1'aspect indetemine de gradior ne comportait guere
26625:duratif de gradior : aarcher, s f avancer; au sena aoral: proc^der.
=== SKT grade/gangrene ===
3233:oentigrrade.  (L.)     Divided drcd   d^recs.  — L.  cen/i-,  for  cenfuw drcd  ;  gradus,  a  degree  ;  see  Qrads
7851:Grade,  a  degree.  (F.»L)    ¥.  g^-oM,  a
7852:GRADE.
7857:degree.  (F.-L.)    O  K  tffgrt,  t'tgrH, step,    rank;    orig.  a  step  down  (used stairs).  —  L.  tie,  down  ;  gradus,  a  step.
=== WEB gangrene ===
ugrep: error: error at position 87
0-\xbf][\x80-\xbf]*){0,120}
                           \___exceeds complexity limits


=== SYN 'go' ghredh ===
```


## [2026-09-06T02:25:26.275Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nlines=open('FSF_pages.txt',encoding='utf-8').read().split('\\n')\npg=0\nfor i,l in enumerate(lines):\n    m=re.match(r'\\[pdf page (\\d+)\\]',l.strip())\n    if m: pg=int(m.group(1))\n    if 'گوهر' in l and 300<=pg<=320:\n        print(pg,i,l.strip()[:120])\nEOF\necho \"---- what pdf pages exist\"\ngrep -n 'pdf page 3[01][0-9]\\]' FSF_pages.txt | head -25"
}
```


### [2026-09-06T02:25:29.326Z] TOOL RESULT

```
---- what pdf pages exist
```


## [2026-09-06T02:25:32.896Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c 'pdf page' FSF_pages.txt; grep -o 'pdf page [0-9]*' FSF_pages.txt | tail -3\npython3 - <<'EOF'\nimport re\nlines=open('FSF_pages.txt',encoding='utf-8').read().split('\\n')\npg=0\nhits=[]\nfor i,l in enumerate(lines):\n    m=re.search(r'pdf page (\\d+)',l)\n    if m: pg=int(m.group(1))\n    if 'گوهر' in l:\n        hits.append((pg,l.strip()[:100]))\nfor h in hits[:20]: print(h)\nEOF"
}
```


### [2026-09-06T02:25:34.807Z] TOOL RESULT

```
0
(0, '\u202bجهان راگوهر آمد زشتکاری\u202c                     \u202bز کین جویی شده چونان بیآزرم\u202c')
(0, '\u202bمرانیز در تخمه هم گوهرست\u202c')
(0, '\u202bچو ناسفته گوهر\u202a .\u202cسه دخترش بود\u202c                                                             \u202bباهو\u202c')
(0, '\u202b(مصحح کتاب\u202a .\u202cسخنور بلندپایه» بهار\u202c                        \u202bبگوی»\u202a .\u202cزن می\u200cگوید گوهر فروشم و برای\u202c')
(0, '\u202b\u202a-۳\u202cگوهر نژاد\u202a:\u202c\u202c            \u202bننمرد مرد\u202c     \u202bجنوشها\u202a .\u202cا\u202c')
(0, '\u202bهمه گوهرش پیکر و\u202c')
(0, '\u202b(\u202a)۲-۴۰۱۰-۷۲۵\u202c\u202c                                  \u202bروم که نقش و نگارش از گوهر بود و\u202c')
(0, '\u202bکسی گوهرش را ندانست ارز\u202c                               \u202b(\u202a)۶-۱۱۳-۹۹۴۱\u202c\u202c')
(0, '\u202bبهبالا ز صد رش فزون هر درخت\u202c                        \u202bگوهری سرخ رنگ شبیه به ياقوت که\u202c')
(0, '\u202bخردباید و گوهر نامدار\u202c                   \u202bبریده دل از ترس گیهان خدیو\u202c')
(0, '\u202bنژاد گوهر اصل و نسب\u202a:\u202c\u202c                            \u202bنخست آفرین کرد یڑ پهلوان\u202c')
(0, '\u202bبسی بر زمین پست کردم سپاه\u202c                                            \u202bمرگوهر خود را نپساود\u202c')
(0, '\u202bزیاقوت و هر گوهری مايه داشت\u202c')
(0, '\u202bاز آن گوهران درهم افتاده تاب\u202c             \u202b(\u202a)۳-۱۴۲-۵۴۶۲\u202c\u202c')
(0, '\u202bبسرفتند گردان کابلستان\u202c                                       \u202bزگوهر که پرمایه\u200cتر یافتند\u202c')
(0, '\u202bگفت\u202a :\u202cسامری گوساله\u200cای ساخت از\u202c                                  \u202bداشتند گوهر باخود بردند)\u202c')
(0, '\u202bتو بشناس کاین مرد گوهر فروش\u202c')
(0, '\u202b(اسدی\u202a:)۸۶۱-۹۶ ,\u202c\u202c                \u202bچو یزدان گوهر مردم بپالود\u202c')
(0, '\u202bز خاک سیه جان گویاکند\u202c                                  \u202bپدید آورد مردم راز گوهر\u202c')
(0, '\u202b(ناصر\u202a:)۱۵-۳۱ .\u202c\u202c           \u202bبر آن هم گوهران بر کرد مهتر\u202c')
```


## [2026-09-06T02:25:45.886Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nlines=open('FSF_pages.txt',encoding='utf-8').read().split('\\n')\nfor i,l in enumerate(lines):\n    if 'گوهر اصل و نسب' in l:\n        print('\\n'.join(x.strip() for x in lines[i-3:i+4])); print('---')\nEOF\necho \"=== HUB p.96 area ===\"\nsed -n '7320,7340p' HUB.txt"
}
```


### [2026-09-06T02:25:47.522Z] TOOL RESULT

```
‫پروز (بهفتح اول و سوم)‬                                  ‫شکل درامده است‪:‬‬

‫نژاد گوهر اصل و نسب‪:‬‬                            ‫نخست آفرین کرد یڑ پهلوان‬

‫بدو گفت من خویش گرسیوزم‬                  ‫که بیدار دل‌باش و روشن روان‬
‫به شاه آفریدون کشد پروزم‬                             ‫تکته اول آنکه واریانت تسه لندن‬
---
=== HUB p.96 area ===
spihr^ ap, ^m&paiaTtjg, JSmd^ptddrjjg (Ktesias, Xenoph.
Anab., Arrian) Noldeke, Pers. Stud. I, 36, skr. gvitrd-;
ArdasTr, arm. sassanid. Artasir, arsacid. Artas^, phi. Ar-
taxsir BB. 4, 35, alter Artaxsatr (historische Schreibung')
im 3. Jhd. p. Chr.), hebr. Artaxsastd, Artaxsastd (Esra
4, 7 u.s.w.), ap. Artaxsad^'d; Bahram = phi. Vahram,
alter Varahran = zd. vered^rayna- \ zahr 'Gift*, arm. iahr
u.s.w. (siehe oben p. 71 und § 89) = zd. ^jfa&ra-; zor
'Weihwasser (Parsenwort !) == paz. zor Min. Gl. 225, phi.
zohr Gl. and Ind. 150, arm. zoh 'Opfer, syr. N'imT *Opfer-
kuchen', zd. zao&ra- 'Opferspende, Opfertrank, Weihwasser.
Ueber gohar s. oben p. 96.
Ausser in pUr, Sdpui% MUddy Ardaslr und zdr liegt r
fiir hr noch vor in: ddra 'Gehalt* = zd. dddra- 'Gabe';
x^dr *leicht*, phi. x^'dr, zd. x^dd^ja-; dusvdr, dnsx^dr^schwie-
rig', phi. dusx^dr Gl. and Ind. 277, arm. dzvar *schwer,
schwierig', zd. duzddra- (vgl. § 108); paz. padasx^drgar
Min. Gl. 151, phi. patasx^drgar Phi. Vd. p. 6, Z.3-2 v. u.,
BB. 4, 47, padaSx^'drgar Bdh. p. 22, 1 ; 23, 9 ein Gebirge
in Gelan --^ zd. "^paitisx^ddra-] arm. Parxar ein Gebirge
nahe dem Lande der Chalder [xalti-K) Laz. Pharp. 219 —
```


## [2026-09-06T02:25:52.266Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3350,3385p' HUB.txt"
}
```


### [2026-09-06T02:25:52.312Z] TOOL RESULT

```
dauen' = phi. gukar-Uan zu skr. vi-kar umwandeln .
940. Arm. vkay gehdrt nicht zu np. guvdh, vgl. meine
Abhandlung *Arisches und Armenisches*, Idg. Forsch. 4,
p. 119.
941. Ich fasse gosdla *Kalb* als Compos, von go- = np.
gav, gav *Kuh' und sdla *Jahrling (von sal *Jahr ab-
geleitet wie in den Zusammensetzungen mit Zahl-
wortern -sdla = jahrig' ist), also = 'Kuh-jahrling,
vgl. unser 'Jahrlingskalb'. Kurd. LW. gilsile ZDMG.
38, 85.
^4. Np. gost 'Fleisch' = ap. *gausta-?
946. Arm. goin ist Lehnwort, aber aus anderen Griinden.
Ebenso arm. gunak =n np. guna* Afgh. yuna f. 'Haare
[~ 96 —
am Korper, Poren, Farbe' ist nicht entlehnt (Geiger).
Zu letzterem doch wohl osset. yun, qun *Haar, Farbe
des Haares'.
948. Die Etymologie ist bedenklich, da gotrd- im Veda
'Kuhstair bedeutet und im Np. *g(ihr (nicht gdhar)
lauten sollte. Afgh. LW. gauhar *Edelstein, Substanz,
Natur ist in der Aussprache wohl von juuhar = arab.
pers. jauhar beeinflusst.
949. Np. get^ = paz. ge^T (adj. und subst.) Shk. 246 setzt
phi. gettk 'irdisch' und phi. g^tth *Welt' (nicht geHh)
•-= syr. gBdlh (Noldeke, Syr. Polemik gegen die pers.
Religion) voraus.
950. Dazu afgh. LW. geSM a side-lock*. Arm. gBs, meist
pi. ges-K = 'das lange Haar des Kopfes', gisah-Jc =
Xocken'. — Syr. ges existirt nicht (Noldeke).
951. Arab, jfihan liegt leider nicht vor. Dazu nach Geiger
afgh. yele pi. fem. 'Heerden*.
952. Np. Idf Trahlerei' (afgh. LW. Ictfa, lapa f. 'boasting,
self-praise, vanity', lafuk a boaster) setzt ein skr.
*laph voraus. Afgh. lavdal, 3. pr. lam *to perform,
to pronounce, to utter, to give' gehOrt, wie es
scheint, zu Inl 'to perform, pronounce, utter, give',
```


## [2026-09-06T02:26:14.600Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for p in 1864 1865; do echo \"===== BQT:$p\"; timeout 600 python3 tools/ref_page.py BQT:$p 2>&1 | head -45; done",
 "timeout": 900000
}
```


### [2026-09-06T02:26:28.779Z] TOOL RESULT

```
===== BQT:1864
(no exact page map; using offset -1205 -> pdf page 659; check the printed number and re-run with --pdf-page if off)
REF: BQT:1864  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 659  OCR-lang: fas

کون ژده ۱۸۹۳۳
گون ژده (۷) - بقتح زای‌فارسی‌ودال گرانرا - وریسمانی را هم میگوبند که استادان
اجد بروزن شورمزه » بمعنی زنجره است و آن بنا چون )۲( خواهند عمارتی بسازند آنرابکشند
جانوری باشد شبیه بملغ که شبها آواز طولانی ورنگه عمارت بريزند .
کند . گوواره « بفتح اول و واو » بر وزن
و ز هك ۱ بروزن کل ته» هرطرف و معنی کهواره است و بعربی مهد کوبند ۷ -
سرین و کفل راگویند . و گله گاو و گاومیش را نیز کفته‌اند ۸ .
گونند ه بروزن موبند ؛ جوالدوز را گوه ‌ هم اول و فتح ثالی وظپورها ۰
گوبند . مخفف کواه ات ۹ .
گو فه - بنم اول و فتح نون » بمعنی گوهر *۱- بر وزن جوهر . بمنی
رنگه و لون باشد ۴ - و گلگونه و غازه را نیز | مروارید است که بعربی لوْلو خوانند - و مطلق
کونند که زنان بر رخاره مالند - وبمعنی‌عارش | جواهر را نیز گفته‌اند - و بمعنی اصل و نژاد
و رخسار هم‌هست که بعرپی خد گوبند - و هردو و فرزند باشد - وبمعنی ذات هم‌آمدء است چه
طرف سرین وکفل را نیز کفته اند ۴ وترجمهةٌ هرگاه گوهری > گوبند مراد از آن ذاتی‌باش
لفظی‌است که بعربی جنس‌میگویند واجنای‌جمم. | و بمعنی سرلهانی و صفات پوشیده که ظاهرشود-
این » وکونپا و گوناکون جمم آن ۴ . و عغل و فرهنگك هم هست - و بمعنی‌عوض‌وبدل
گو نه گون* - بسنی کوناگون‌ا_ن | نیز آمده است و باین معنی غربب است؛ وجوهر
که زنگارنگه و جنس بجنس و انواع باشد . ممرب‌آن باشد (۳) ۰ ۱
گو نیا ۱ - بنم اول و سکون نانی گوهر ۴۵ - بسسنی ذات واسلآدم
و ثالث وتحتائی بالف کشیده » نخته‌ای باشد مثلك | باشد - و فرزند آدم را نیز کوبند - و خاك را
قائم‌الزاوبه مراستادان بنا را که کجی و رامتی | هم گفته‌اند و عربان تراب خوانند .
عمارتر! از آن یایند - و نیز افزاری باشد درود گوهر آسمان - کدبه از اسل

(۱) چش :کون زده ‎ )۱(‏ " (۲) خم۱ : - چون . (۳) چش : است .

مسحف کونته («.م.) ۰ ۲ - رك : گون؛ ورد : ص‌ لو.از مقدمه کتاب.

۴ - باین ممنی ممحف «کوله »۳ کون ۰ ۴ - رك :۵ فرهنگه دساتین
ص ۰۲۹4 ۵ - ر4: کوناگون . ‎٩‏ - ازس‌بانی هدر < دلده۵ او
(93. 0 ۱۶ ,2 ,8505 و.. ۳6۲۶182 114016 اه اوزا ۸ , وعند۶ه )

۷ کپواره ** گاهواره ۳ کواره («.م.) ۰ ۸ کواره («م.)

‎٩‏ -رك : کواه .- کوه پم اول و های ملفوظ بمعنی سرکین » اوستا 8۵102 [در
- ۷2۵۳۵۱۵ ] 80186 بمعنی که کردان بعنی جمل . رك : کوکار ) ؛ پهلوی 800 ( در
4 اما که‌گردان » جمل ) » سانکربت - 801112 » آرمنی 1 ( کود » فنله) :
کردی 80 ۰ افغانی أناطلع ۰ بلوچی 81110 » وخی فا8 » 81 » اشکاشمی 8088 ۶ اسشق ۹۸۷ *.

‏یگ پهلوی ۵۵ج ( جوهر ۰ هاده ( 2 تاوادیا ۹۱۹۹ » با #ط۵ع معرب آن جوهر
« نیب رکه ۸۲« منای ۲۷۸ : ۲ > » ورك : اسشق - هویشمان ۹4۸. « پارسی ترصبع » گوهر
برشته کردن بود . > ۶ ترجمان البلاغه » چاپ احمدآتش . پخش عکی ص ۲۳۹ ب > ۰

===== BQT:1865
(no exact page map; using offset -1205 -> pdf page 660; check the printed number and re-run with --pdf-page if off)
REF: BQT:1865  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 660  OCR-lang: fas

-۱۸۹۳- گوحری
و جرم آسمان است - و کنایه از کواکب هم کردن باشد .
هت . گوهر کش - بنتح‌کان تازی‌وسکون
گوظر آ گین ۱ - هرچیز که درآن | شین نقطه‌دار » دست براجن و دستینةٌ مرصع را
جواهر نشانده باشند - و کنایه از مردم شجاع کوبند 9 ؛ و بکر کاف فارسی هم آمده است
ودلاور و پهلوان هم هست. . بعتی کوهردل » چه کش بمعنی دل باشد .
گوهران ی < بروزن جوشقان؛ چهار گوهر مرخ صفت - کنایه از
عنصر را گوبند که کرء خاك و آب وهوا وآتش | انگشت و زغال باشد » وآن راکوهرصفت مریخ
گو ۵ وآر » بکر رابعم و قتح فوقالی گوهر مطهر - بکر رابع. هر چیز
وسکون رای فرشت ,کنایه از اغك چتم باشد. | پاك و پاکیزه و سره و پا4 اصل و نیکو را
گوهرخانه خیز -کنابه ازحنرت | کوبند .
رسالت پناه محمدی صلوات‌ال علیه وآله است. گلوهر ملک - بنم میم و سکون لام
گوهرخای ۴ « بممنی کوهر خانه | وکاف «کنایه از پادشاه زاده باشد - و پادشاء را
خبزاست که کنابه ازحضرت رسالت پناه محمدی | نیز گونند .
صلواتانٌ علیه وآله باشد . گوهر نیم سفت - ممروف است -
گوهرزذای ؟ - بسنی بز رکه زاده | وکنایه از کلام سربسته باشد یعنی چنان کوبند
و اسیل‌زاده باشد چه کوهر بمعنی اصل و نژاد | که همه‌کس نشپمد - وکنایه ا زکلامی‌است که
هم‌آمده است - وبمعئی‌پیکوکار وعادل_وهنرمند | تمام قواعد و قوانین و صنایم و بدایم سخن در
وضیح لیزهست . آن صرف شده باشد ‎.)٩(‏
‏گوهرسفتن * کنایه از انشای سخن گوهری ۹ « بروزن جوهری,چیزی
کردن - وقصه خوانی باشد وآنرا کهرسفتن هم | را کویند که ا زگوهر ساخته باشند - وخداوند
میگویند . اصل و دبت را نیز کفته‌اند - و جواهر فروش
گوهرشکستن - کنابه ازدست‌دادن | وجواهرشنای را هم کفته‌اند ۷ - و بمعنی ذاتی
دولت و منصب ۴ - وکنابه ازخندیدن و خنده | هم هست که در مقابل عرضی است .
(۱) چش : - بعنی .... شده باشد .
۹ -رك : آگین . ۲ - جمع :کوهر. ۴ - از: گوهر ۳ خای(خاینده).
۴ - از :کوهر ۲-زای ( زاینده ). ۴ -رفتن دولت :
چو بد گوهران را قوی کرد پغت جهان بین که کوهربرو چون‌شکست.
نظامی کنجوی « رشیدی » .
8 -ز بهر ساعد شاخ اير ساخت کوهر کش
که قطره در خوعابت و سبزه شبه دوال ۰
رفیع لنبانی ۶ رشیدی > .
‎٩‏ - از :کوهر ی ( پوند دبت ) ؛ پهلوی الط ۵ع ( اساسی » اصلی ) ۶ منلیس
تمفهههه ۷ - کردی ع 808671 ( جواهر فروشی ) « ژاباص ۳۷۲ . امروژه
« جواهری ۲ (معرب) کوبند .
```


## [2026-09-06T02:26:51.969Z] TOOL CALL #48: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T02:26:52.018Z] TOOL RESULT

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


## [2026-09-06T02:28:00.296Z] TOOL CALL #49: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg199.png data/verification/sources/refs/ocr/BOOK/199.png && ls -la data/verification/sources/refs/ocr/BOOK/199.png"
}
```


### [2026-09-06T02:28:00.374Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 78587 Sep  5 22:28 data/verification/sources/refs/ocr/BOOK/199.png
```


## [2026-09-06T02:35:24.259Z] TOOL CALL #50: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-199.json",
 "content": "{\n  \"pdf_page\": 199,\n  \"book_page\": 169,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Gôtra\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Sanskrit गोत्र gotra- 'cow-pen, herd; family, lineage' (< PIE *gʷṓws 'cow' + *-tro-); the Persian word is its COGNATE, from Proto-Iranian *gawθraH / *gawθram, not its descendant\",\n      \"note\": \"The root box is a real word with a defensible gloss, but the arrow is genealogically wrong in the way Nourai's own reference already warns about. Horn no. 948 (p. 211 — exactly the page cited) reads: 'göher \\\"Edelstein; Materie, Ursprung, Geschlecht\\\", arab. LW. jauhar \\\"Edelstein; Substanz\\\". skr. gōtra- \\\"Geschlecht, Ursprung\\\"; phlv. göhr bezw. göhar \\\"Materie, Substanz\\\". Die Bedeutung \\\"Edelstein\\\" ist erst sekundär.' Horn adduces Sanskrit gōtra- as a comparandum (cognate), never as the source of the Iranian word — Sanskrit is not an ancestor of Middle Persian. Hübschmann, Persische Studien p. 96, in his numbered note to precisely this Horn paragraph, goes further: '948. Die Etymologie ist bedenklich, da gotrá- im Veda \\\"Kuhstall\\\" bedeutet und im Np. *gōhr (nicht gōhar) lauten sollte.' Modern reconstruction resolves both objections: Middle Persian gwhl /gōhr/ goes back to Old Persian *gauθrā, itself from Proto-Iranian *gawθraH 'jewel', beside *gawθram 'family, lineage', an exact formal match to Sanskrit gotra- (*gaw- 'cow' + *-θra-), the shared semantics being 'cow-pen, herd' → 'stock, lineage' → 'inborn nature, essence' → 'gem'. So the material is right, the direction of the arrow is not, and the gloss 'substance' belongs to the Iranian branch, not to Vedic gotra-. Hence 'plausible' rather than 'confirmed'.\",\n      \"note_fa\": \"واژهٔ سنسکریت gotra- «آغل گاو؛ گله؛ تبار و خاندان» واقعی است، اما «گوهر» فارسی از آن گرفته نشده، بلکه با آن هم‌ریشه است: فارسی میانه gōhr از پارسی باستان *gauθrā و آن از ایرانی باستان *gawθraH/*gawθram (از *gaw- «گاو» + پسوند *-θra-)، درست همان ساختی که در گوتره سنسکریت دیده می‌شود. هرن در بند ۹۴۸ (ص ۲۱۱) همین را می‌گوید و گوتره را تنها «هم‌ریشه» می‌آورد، نه اصلِ واژه؛ هوبشمان نیز در «مطالعات فارسی» ص ۹۶ در حاشیهٔ همان بند می‌نویسد این ریشه‌شناسی «مشکوک» است، چون gotrá- در وداها «آغل گاو» است و در فارسی نو باید *gōhr می‌شد نه gōhar. تحول معنایی «آغل/گله ← تبار ← ذات و سرشت ← جواهر» است. پس ادعای نورایی با احتیاط پذیرفتنی است، اما جهت پیکان (سنسکریت ← پهلوی) نادرست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/gwhl\",\n        \"https://en.wiktionary.org/wiki/gotra\",\n        \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%D9%87%D8%B1\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"HRN:211\",\n          \"status\": \"partial\",\n          \"note\": \"Horn, Grundriss p. 211 no. 948 (local HRN.txt, leaf 233; grep '948. göher'): 'göher \\\"Edelstein; Materie, Ursprung, Geschlecht\\\" ... skr. gōtra- \\\"Geschlecht, Ursprung\\\"; phlv. göhr bezw. göhar \\\"Materie, Substanz\\\".' The page has all three of Nourai's boxes and the glosses, but Horn treats Skt. gōtra- as a cognate, not as the etymon, so the arrow Sanskrit→Pahlavi is Nourai's own reading of Horn.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"HUB\",\n          \"where\": \"Persische Studien p. 96, note to Horn no. 948\",\n          \"stance\": \"contradicts\",\n          \"note\": \"'948. Die Etymologie ist bedenklich, da gotrá- im Veda \\\"Kuhstall\\\" bedeutet und im Np. *gōhr (nicht gōhar) lauten sollte. Afgh. LW. gauhar \\\"Edelstein, Substanz, Natur\\\" ist in der Aussprache wohl von juuhar = arab. pers. jauhar beeinflusst.' (HUB.txt lines 3367-3372)\"\n        },\n        {\n          \"src\": \"Wiktionary\",\n          \"where\": \"Middle Persian gwhl\",\n          \"stance\": \"partial\",\n          \"note\": \"'Inherited from Old Persian *gauθrā, borrowed from Old Median *gauθrā, from Proto-Iranian *gawθraH (\\\"jewel\\\"), related to *gawθrám (\\\"family, lineage, growth\\\").' Sanskrit gotra- is a cognate of *gawθram, not the source.\"\n        },\n        {\n          \"src\": \"PHD\",\n          \"where\": \"MacKenzie p. 36 s.v. gōhr\",\n          \"stance\": \"supports\",\n          \"note\": \"'gōhr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage' — the Middle Persian word and all of Nourai's senses, including 'lineage'.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"gôhar\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The word is real: MacKenzie's Concise Pahlavi Dictionary p. 36 has 'gōhr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage', with derivatives gōhrag, gōhrīg 'natural, essential' and the compounds ham-gōhr 'consubstantial', wad-gōhr 'ill-born', nēk-gōhr 'good-natured'; Nyberg II 258 has 'gōhr [gwhl] 1. gem, jewel; 2. substance ... MPrs. gwhr \\\"substance\\\"; Paz. NP gōhar.' The canonical Book-Pahlavi form is gōhr (spelled gwhl); the disyllabic gōhar Nourai prints is the Pāzand/New Persian shape, which is why Hübschmann objected that a regular descendant of *gauθra- should be NP *gōhr. The word does not come FROM Sanskrit gotra-: Middle Persian gōhr continues Old Persian *gauθrā (itself a Median form) from Proto-Iranian *gawθraH, of which Vedic gotra- is the Indic sister form (*gaw- 'cow' + *-θra-/-tra-, 'cow-pen, herd' → 'stock' → 'inborn nature'). So the box is right and the arrow is a cognate relation drawn as a descent.\",\n          \"derivation_fa\": \"این واژه در پهلوی حقیقی است: مکنزی (ص ۳۶) gōhr را با املای gwhl به معنی «ذات، سرشت، مادّه؛ گوهر؛ تبار» آورده و ترکیب‌هایی چون ham-gōhr و wad-gōhr و nēk-gōhr را نیز ثبت کرده؛ نیبرگ (ج۲) هم gōhr را «گوهر» و «ذات» معنی کرده است. صورت اصیل پهلوی gōhr است و gōhar که نورایی نوشته صورت پازند/فارسی نو است — همان ایرادی که هوبشمان می‌گیرد. این واژه از سنسکریت گرفته نشده؛ فارسی میانهٔ gōhr بازماندهٔ پارسی باستان *gauθrā و ایرانی باستان *gawθraH است و گوتره سنسکریت خواهرِ هندیِ آن است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/gwhl\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:211\",\n              \"status\": \"supports\",\n              \"note\": \"Horn p. 211 no. 948 gives exactly this box: 'phlv. göhr bezw. göhar \\\"Materie, Substanz\\\"' — the Pahlavi form and Nourai's gloss 'substance, material'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie 1971 p. 36\",\n              \"stance\": \"supports\",\n              \"note\": \"'gōhr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage.'\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II, s.v. gōhr\",\n              \"stance\": \"supports\",\n              \"note\": \"'gōhr [gwhl] 1. gem, jewel ...; adj. pat-~ set with gems. — 2. substance ...; adj. pat-~ of noble birth. — MPrs. gwhr \\\"substance\\\" (A-H II); Paz. NP gōhar.' (NYB_vol2_glossary.txt line 1687)\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Persische Studien p. 96\",\n              \"stance\": \"contradicts\",\n              \"note\": \"the expected New Persian outcome would be *gōhr, 'nicht gōhar'; Hübschmann suspects the -a- of gōhar/gauhar was carried in from Arabic jauhar.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"gohar «گوهر»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian گوهر gawhar/gowhar continues Middle Persian gwhl /gōhr, gōhar/ directly (Wiktionary: 'Inherited from Middle Persian gwhl (gōhr, gōhar), \\\"substance, essence; jewel\\\"'), the vowel of the first syllable being the regular Classical Persian aw < MP ō before h. All three senses Nourai lists are attested: 'essence, substance' (Rūmī, Masnavi I 3529 'تا چو خورشیدی بتابد گوهرم'), 'stock, lineage' — the Shāhnāma sense of the Ferdowsī line quoted in the box, 'جوان بود و از گوهر پهلوان', matched by Noushin's Shāhnāma glossary entry 'گوهر: اصل و نسب' — and 'jewel, gem', which Horn rightly calls secondary ('Die Bedeutung \\\"Edelstein\\\" ist erst sekundär; sie findet sich noch nicht im Mittelpersischen ausser an einigen späten Stellen'). گهر is the metrically shortened poetic doublet and گوهران a regular -ān plural/derivative. The two remaining forms in the box, جوهر and جواهر, are an Arabic-mediated round trip: Arabic borrowed Persian gawhar in the early Islamic period as جَوْهَر jawhar (Persian g → Arabic ǧ, the standard substitution), used it as the technical term for 'substance' in kalām and falsafa against عَرَض 'accident', formed the broken plural جَوَاهِر jawāhir, and Persian took both back as جوهر/جواهر — Asbaghi's Persische Lehnwörter im Arabischen p. 101 states it flatly: 'Ǧauhar: \\\"Juwel\\\" aus dem pers. گوهر gōhar, MP gōhr'.\",\n          \"derivation_fa\": \"«گوهر» فارسی نو بازماندهٔ مستقیم فارسی میانهٔ gōhr/gōhar است؛ ōِ فارسی میانه در فارسی کلاسیک به aw بدل شده (gawhar). هر سه معنی که نورایی آورده گواه دارد: «ذات و سرشت» (مولوی، مثنوی دفتر یکم بیت ۳۵۲۹)، «اصل و نژاد» — که همان معنای بیت فردوسی در همین خانه است و نوشین در «واژه‌نامک» ذیل «گوهر» آن را «اصل و نسب» معنی کرده — و «جواهر»، که هرن آن را معنایی ثانوی می‌شمارد و می‌گوید در فارسی میانه جز در متن‌های متأخر دیده نمی‌شود. «گهر» صورت کوتاه‌شدهٔ شعری و «گوهران» جمع/مشتق آن است. اما «جوهر» و «جواهر» وام‌گیری دوسویه‌اند: عربی «گوهر» فارسی را به صورت «جَوْهَر» معرّب کرد (ابدال گِ فارسی به ج عربی)، آن را در کلام و فلسفه در برابر «عَرَض» به کار برد و جمع مکسّر «جواهر» ساخت، و فارسی هر دو را دوباره وام گرفت — اصبغی در «وام‌واژه‌های فارسی در عربی» ص ۱۰۱ همین را می‌گوید. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%D9%87%D8%B1\",\n            \"https://en.wiktionary.org/wiki/%D8%AC%D9%88%D9%87%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1862\",\n              \"status\": \"partial\",\n              \"note\": \"the page number is two pages early. Rendering Borhān-e Qāṭeʿ printed p. 1862 (tools/ref_page.py BQT:1862, vol. 3 pdf p. 657) gives the entries گوگرد / گوگردانک / گوکه / گول / گولاج / گولانج — no گوهر. گوهر stands on printed p. 1864: 'گوهر - بر وزن جوهر. بمعنی مروارید است که بعربی لؤلؤ خوانند - و مطلق جواهر را نیز گفته‌اند - و بمعنی اصل و نژاد و فرزند باشد - وبمعنی ذات هم آمده است ... وجوهر معرّب آن باشد', with Moʿin's footnote 10 on the same page: 'پهلوی gōhr (جوهر، مادّه) ... معرّب آن جوهر ... رک: هوبشمان ۹۴۸'. Content supports Nourai exactly (including the Arabic round trip); only the pagination is off. The offset was verified against BQT:1783, which renders its own printed number ۱۷۸۳ correctly.\"\n            },\n            {\n              \"ref\": \"PLA:101\",\n              \"status\": \"supports\",\n              \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen p. 101 (PLA_pages.txt line 5889): 'Ǧauhar: \\\"Juwel\\\" aus dem pers. گوهر gōhar, MP gōhr', with the derived entries Ǧawāhir (pl.), Ǧauharī 'Juwelier', Ǧauhar-fard 'Atom', Ǧauhara — exactly the جوهر/جواهر of Nourai's box.\"\n            },\n            {\n              \"ref\": \"ARK:249\",\n              \"status\": \"not_checked\",\n              \"note\": \"Rokn-zadeh Adamiyyat, Arkān-e Sokhan (1347/1968) is not digitised on any accessible platform (refs_online.json: 'Not found ... nothing digitised on any permitted platform').\"\n            },\n            {\n              \"ref\": \"FSF:302\",\n              \"status\": \"partial\",\n              \"note\": \"Noushin's Vāzhe-nāmak (FSF_pages.txt has no page tags, so the printed page cannot be located) does carry the entry 'نژاد گوهر اصل و نسب:' — i.e. گوهر glossed 'اصل و نسب, lineage', the Shāhnāma sense Nourai's Ferdowsī line illustrates. Entry found, page number unverifiable.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhān-e Qāṭeʿ printed p. 1864 with Moʿin's footnote 10\",\n              \"stance\": \"supports\",\n              \"note\": \"'گوهر ... بمعنی اصل و نژاد و فرزند باشد - وبمعنی ذات هم آمده است ... وجوهر معرّب آن باشد', footnote: 'پهلوی gōhr (جوهر، مادّه) ... معرّب آن جوهر'. Moʿin himself derives it from Pahlavi and marks جوهر as the Arabicised form.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"p. 211 no. 948\",\n              \"stance\": \"supports\",\n              \"note\": \"'göher \\\"Edelstein; Materie, Ursprung, Geschlecht\\\" (Šāhn. I,149 V.366; 170 V.741), arab. LW. jauhar \\\"Edelstein; Substanz\\\" ... Die Bedeutung \\\"Edelstein\\\" ist erst sekundär.'\"\n            },\n            {\n              \"src\": \"Wiktionary\",\n              \"where\": \"گوهر / جوهر\",\n              \"stance\": \"supports\",\n              \"note\": \"گوهر: 'Inherited from Middle Persian gwhl (gōhr, gōhar), \\\"substance, essence; jewel\\\"'; Descendants: '→ Arabic جَوْهَر (jawhar)'. Persian جوهر: 'Borrowed from Arabic جَوْهَر (jawhar), itself from Early Classical Persian گَوهَر (gawhar), from Middle Persian gwhl (gōhr)' — the round trip Nourai draws.\"\n            },\n            {\n              \"src\": \"FSF\",\n              \"where\": \"Vāzhe-nāmak s.v. گوهر\",\n              \"stance\": \"supports\",\n              \"note\": \"'نژاد گوهر اصل و نسب' — Noushin glosses the Shāhnāma's گوهر as 'origin, lineage', the sense of the Ferdowsī hemistich in the box.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Gras\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *gras- : *gros- 'to gnaw, to devour' (Pokorny 404; Watkins/AHD gras-)\",\n      \"note\": \"Root, language label and gloss are all right, and the cited page is the right one: Pokorny's lemma reads 'Root / lemma: gras- : gros- / Meaning: to gnaw, to devour ... References: WP. I 657 f., WH. I 616 f. / Page(s): 404', and Watkins's appendix has 'gras-. To devour. ... 4. Reduplicated form *gar-gr- dissimilated in Greek gangraina, gangrene: GANGRENE. [Pok. gras- 404.]' The whole chain of the chart — Greek → (Arabic) → Persian, Greek → Latin → English — is Pokorny's and Watkins's own. Two caveats belong on the page rather than to the root: (a) the Greek box prints a second form 'gagrajna' which is not a Greek word (see node 1); (b) the derivation of γάγγραινα from this root, standard in Pokorny, Klein, Watkins and Etymonline, is rejected by Beekes and by Wiktionary in favour of a Pre-Greek substrate origin, so the root→Greek arrow is the one weak link in an otherwise clean entry.\",\n      \"note_fa\": \"ریشه، برچسب زبانی و معنی هر سه درست است و شمارهٔ صفحه هم درست: پوکورنی در ص ۴۰۴ مادهٔ gras- : gros- «جویدن، بلعیدن» را آورده و واتکینز در پیوست فرهنگ American Heritage همین را با ارجاع «[Pok. gras- 404]» تکرار کرده و صریحاً می‌گوید یونانی gangraina صورت دوگان‌شدهٔ (reduplicated) همین ریشه است. تمام زنجیرهٔ نمودار (یونانی ← عربی ← فارسی؛ یونانی ← لاتین ← انگلیسی) از همین دو مرجع می‌آید. دو نکته باقی می‌ماند: نخست آنکه در خانهٔ یونانی صورت دومی به شکل gagrajna چاپ شده که هیچ منبعی آن را نمی‌شناسد (خطای چاپی کتاب)، و دوم آنکه بیکِس و ویکی‌واژه ریشه‌شناسی سنتی γάγγραινα را رد می‌کنند و آن را واژه‌ای پیش‌یونانی (بازمانده از زیرلایهٔ بومی) می‌دانند.\",\n      \"sources\": [\n        \"https://www.etymonline.com/word/gangrene\",\n        \"https://en.wiktionary.org/wiki/%CE%B3%CE%AC%CE%B3%CE%B3%CF%81%CE%B1%CE%B9%CE%BD%CE%B1\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:404\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt lines 34441-34460: 'Root / lemma: gras- : gros- / Meaning: to gnaw, to devour ... redupl. due to a *γαγ-γραίνειν \\\"devour\\\": γάγγραινα \\\"gangrene, the eating ulcer\\\" ... References: WP. I 657 f., WH. I 616 f. / Page(s): 404'.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985 s.v. gras-\",\n          \"stance\": \"supports\",\n          \"note\": \"'gras-. To devour. ... 3. Suffixed form *gras-ter-, \\\"the devourer,\\\" dissimilated in Greek gastēr ... 4. Reduplicated form *gar-gr- dissimilated in Greek gangraina, gangrene: GANGRENE. [Pok. gras- 404.]' (AHD_watkins1985.txt line 531)\"\n        },\n        {\n          \"src\": \"KLN\",\n          \"where\": \"Klein s.v. gangrene / gastro-\",\n          \"stance\": \"supports\",\n          \"note\": \"'gangrene, n., mortification; decay. — L. gangraena, fr. Gk. γάγγραινα, lit. \\\"that which eats away\\\", formed through reduplication fr. γράω, γρᾶν, \\\"to gnaw, eat\\\", whence also γράστις, \\\"green fodder\\\". See gastro-.' (KLN_1966.txt line 15774)\"\n        },\n        {\n          \"src\": \"Wiktionary\",\n          \"where\": \"γάγγραινα\",\n          \"stance\": \"contradicts\",\n          \"note\": \"'In antiquity it was compared with γράω (gráō, \\\"to devour\\\") (a theory which Etymonline corroborates), but this is likely incorrect. It is most probably a Pre-Greek word.'\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Greek\",\n          \"words\": \"gangraina, gagrajna\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The first form is right: Ancient Greek γάγγραινα gángraina 'an eating sore, gangrene', a medical term of the Hippocratic corpus (5th-4th c. BCE), explained since antiquity as a reduplicated formation on γράω / γρᾶν 'to gnaw, eat' — Pokorny p. 404 writes it out, 'redupl. due to a *γαγ-γραίνειν \\\"devour\\\": γάγγραινα \\\"gangrene, the eating ulcer\\\"', and Klein and Watkins say the same, with the same dissimilation *gar-gr- > gang-gr- that turned *γραστήρ into γαστήρ. The second form 'gagrajna' is not a Greek word and not a possible transliteration of one: -jn- renders nothing in Greek. The printed page (pdf 199, rendered at 450 dpi, copied to data/verification/sources/refs/ocr/BOOK/199.png) shows 'gangraina, gagrajna' verbatim, so the extraction is faithful and the garbling is the book's own — evidently a mangled doubling of the same word (or of Pokorny's reduplicated stem *gag-grain-). Substantively, the arrow root→Greek is also the weakest link of the entry: Beekes and Wiktionary judge γάγγραινα 'most probably a Pre-Greek word' and the comparison with γράω 'likely incorrect', while Pokorny, Walde-Pokorny I 657, Klein, Watkins and Etymonline all keep it under *gras-.\",\n          \"derivation_fa\": \"صورت نخست درست است: یونانی باستان γάγγραινα «زخم خورنده، قانقاریا»، اصطلاحی پزشکی در مجموعهٔ بقراطی (سدهٔ پنجم–چهارم پیش از میلاد)، که از دیرباز آن را صورت دوگان‌شدهٔ (reduplicated) γράω «جویدن، خوردن» دانسته‌اند؛ پوکورنی (ص ۴۰۴)، کلاین و واتکینز هر سه همین را می‌گویند، با همان ناهمگونی (dissimilation) *gar-gr- > gang-gr- که *γραστήρ را به γαστήρ بدل کرده است. اما صورت دوم، gagrajna، هیچ واژهٔ یونانی نیست و -jn- در یونانی معادلی ندارد. تصویر صفحهٔ چاپی (ص ۱۹۹ پی‌دی‌اف) عیناً «gangraina, gagrajna» را نشان می‌دهد، پس خطای خوانش اسکن نیست بلکه خطای چاپی خودِ کتاب است. افزون بر این، بیکِس و ویکی‌واژه این ریشه‌شناسی سنتی را رد می‌کنند و γάγγραινα را واژه‌ای «پیش‌یونانی» می‌شمارند.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"gangraina, gagrajna\",\n          \"correct_form\": \"gangraina (γάγγραινα); Pokorny's reduplicated stem is *gag-grain- / *γαγ-γραίνειν\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%B3%CE%AC%CE%B3%CE%B3%CF%81%CE%B1%CE%B9%CE%BD%CE%B1\",\n            \"https://www.etymonline.com/word/gangrene\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:404\",\n              \"status\": \"supports\",\n              \"note\": \"'redupl. due to a *γαγ-γραίνειν \\\"devour\\\": γάγγραινα \\\"gangrene, the eating ulcer\\\"' — Pokorny p. 404 gives the Greek word, the gloss ('the eating ulcer' = Nourai's 'decay of tissue') and the derivation from gras-; he knows no form 'gagrajna'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. gangrene\",\n              \"stance\": \"supports\",\n              \"note\": \"'Gk. γάγγραινα, lit. \\\"that which eats away\\\", formed through reduplication fr. γράω, γρᾶν, \\\"to gnaw, eat\\\".'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. gras-\",\n              \"stance\": \"supports\",\n              \"note\": \"'Reduplicated form *gar-gr- dissimilated in Greek gangraina, gangrene: GANGRENE.'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny I 657 (gras-)\",\n              \"stance\": \"supports\",\n              \"note\": \"the parent article of Pokorny's lemma, cited by Pokorny himself as 'WP. I 657 f.' for the reduplicated γάγγραινα.\"\n            },\n            {\n              \"src\": \"Wiktionary\",\n              \"where\": \"γάγγραινα\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'It is most probably a Pre-Greek word' — i.e. not from *gras- at all.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Arabic\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"An empty pass-through box: the printed page shows the header 'Arabic  BQT:1339' and no word at all, so nothing is asserted beyond the route. The route itself is historically right. Greek medical terminology reached Persian not directly but through the ninth-century Baghdad translation movement — Ḥunayn ibn Isḥāq and his school rendering Galen and the Hippocratics into Arabic, often via Syriac — and γάγγραινα was carried over as an unassimilated transcription, غانغرايا / غانقرايا, rather than translated (the native Arabic word for the condition is آكِلة 'the eater', a calque). Moʿin's dictionary tags the Persian outcome معرّب, 'Arabicised', which is precisely the claim of this box. Nourai names no Arabic form, which is the one thing that keeps this from 'confirmed'.\",\n          \"derivation_fa\": \"این خانه در کتاب تهی است: در صفحهٔ چاپی تنها عنوان «Arabic BQT:1339» آمده و هیچ واژه‌ای نوشته نشده، پس ادعایی جز مسیر وام‌گیری در کار نیست. خودِ مسیر درست است: اصطلاحات پزشکی یونانی در سدهٔ سوم هجری از راه نهضت ترجمهٔ بغداد (حنین بن اسحاق و شاگردانش، غالباً به واسطهٔ سریانی) به عربی رفت و γάγγραινα نه ترجمه بلکه آوانویسی شد: «غانغرایا / غانقرایا» (معادل عربی بومی آن «آکِلة» است). معین نیز صورت فارسی را «معرّب» می‌داند، یعنی همین واسطهٔ عربی. تنها ایراد آن است که نورایی صورت عربی را ننوشته است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1339\",\n              \"status\": \"not_found\",\n              \"note\": \"Rendering Borhān-e Qāṭeʿ printed p. 1339 (tools/ref_page.py BQT:1339, vol. 3 pdf p. 134) gives the opening of the chapter on ط: 'گفتار شانزدهم از کتاب برهان قاطع در حرف طای بی‌نقطه ...' with the entries طاخک and طارطقه. There is no gangrene word on it (and Borhān, a Persian dictionary, would carry غانغرایا under غ, not here). The page mapping was verified with BQT:1783, whose rendering prints its own page number ۱۷۸۳.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"Moʿin s.v. غانغرایا\",\n              \"stance\": \"supports\",\n              \"note\": \"'غانغرایا: [| - غانقرایا، معر. فساد؛ عفونت] (اِ.) (پز.) مردگی یا ناحیهٔ کم و بیش وسیع از یک عضو' — the tag معر. (= معرّب, 'Arabicised') is exactly the Arabic mediation this empty box stands for. (MON_part2.txt line 461)\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"printed p. 1339\",\n              \"stance\": \"silent\",\n              \"note\": \"the cited page is the ط chapter opening and says nothing about gangrene.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"ğânqrâyâ «غانقرایا»\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The etymology is sound and the word is real, but the JSON's Persian script is not what the page prints. The printed box (data/verification/sources/refs/ocr/BOOK/199.png) carries TWO forms, غانغرایا first (with غ in third position) and غانقرایا second; the extraction has غانقرایا in both the word's `script` field and in `script_extra`, so the headword form غانغرایا has been lost and the variant duplicated. Moʿin's own headword is the first of the two: 'غانغرایا: [| - غانقرایا، معر. فساد؛ عفونت] (اِ.) (پز.) مردگی یا ناحیهٔ کم و بیش وسیع از یک عضو' — i.e. غانغرایا with غانقرایا as the alternate, exactly the pair the book prints. The word itself is a straight transcription of Greek γάγγραινα taken over through the Arabic medical literature: Greek γ before a back vowel was rendered by غ (as in غانغرایا for gan-), the second γ likewise غ or, in the by-form, ق, and the Greek -aina ending appears as -ایا. It is a learned nineteenth/twentieth-century medical term in Persian, not an inherited word, and it stands beside the modern loan گانگرن from French gangrène.\",\n          \"derivation_fa\": \"ریشه‌شناسی درست است و واژه هم واقعی، اما املای فارسیِ ثبت‌شده در داده‌ها با صفحهٔ چاپی نمی‌خواند: در کتاب دو صورت آمده است، نخست «غانغرایا» و سپس «غانقرایا»، حال آنکه در استخراج هر دو جا «غانقرایا» ضبط شده و صورت اصلی از میان رفته است. معین نیز مدخل را «غانغرایا» گرفته و «غانقرایا» را صورت دیگر آن آورده و آن را «معرّب» و به معنی «فساد، عفونت» و در اصطلاح پزشکی «مردگی عضو» دانسته است. خود واژه آوانویسی مستقیم γάγγραινα یونانی است که از راه متون پزشکی عربی به فارسی رسیده: γ یونانی پیش از واکهٔ پسین به «غ» (و در صورت دوم به «ق») بدل شده و پایانهٔ -aina به «-ایا». این واژه‌ای است کتابی و متأخر، در کنار وام‌واژهٔ امروزی «گانگرن» از فرانسه. پس: خطای خوانش اسکن.\",\n          \"error_in\": \"extraction\",\n          \"book_prints\": \"غانغرایا ، غانقرایا\",\n          \"correct_form\": \"word script غانغرایا, script_extra غانقرایا\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:2383\",\n              \"status\": \"supports\",\n              \"note\": \"Moʿin, Farhang-e Fārsi s.v. غانغرایا (MON_part2.txt lines 461-478): 'غانغرایا: [| - غانقرایا، معر. فساد؛ عفونت] (اِ.) (پز.) مردگی یا ناحیهٔ کم و بیش وسیع از یک عضو ... غانغرایای خشک تقریباً بدون بو است ولی غانغرایای مرطوب دارای بوی گندیدگی می‌باشد.' Both spellings of the box, the gloss 'gangrene', and the معرّب tag. The printed page number cannot be mapped (only the 2-vol. Adena reprint is on disk), but the entry is verbatim.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"s.v. غانغرایا\",\n              \"stance\": \"supports\",\n              \"note\": \"'معر. فساد؛ عفونت' — Moʿin marks it an Arabicised borrowing, matching the Greek→Arabic→Persian route.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhān-e Qāṭeʿ\",\n              \"stance\": \"silent\",\n              \"note\": \"the cited p. 1339 is the ط chapter opening; a modern medical term of this kind is not in the 17th-century Borhān at all.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"gangraena\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin took the word over from Greek unchanged as a medical technicality: Ernout-Meillet's Dictionnaire étymologique de la langue latine has 'gangraena (gangrena, can-), -ae f.: gangrène. Emprunt au gr. γάγγραινα', and it is used by Celsus and the later medical writers. The variant cancrena of Medieval Latin, from which the English 1540s form cancrena comes, is a folk-etymological reshaping under the influence of cancer 'crab, canker'. Nourai's AHD:542 points at the main-dictionary entry 'gangrene' of the 1975 New College Edition rather than at Watkins's appendix, but the appendix entry gras- carries the same chain.\",\n          \"derivation_fa\": \"لاتینی این واژه را دست‌نخورده و همچون اصطلاحی پزشکی از یونانی وام گرفت: ارنو و می‌یه در «فرهنگ ریشه‌شناختی زبان لاتینی» می‌نویسند «gangraena (gangrena, can-)، مؤنث: قانقاریا. وام‌گرفته از یونانی γάγγραινα»؛ کِلسوس و پزشکان بعدی آن را به کار برده‌اند. صورت cancrena در لاتینی میانه که صورت انگلیسی سدهٔ شانزدهم از آن آمده، ریشه‌شناسی عامیانه و زیر تأثیر cancer «خرچنگ، قانقاریا» ساخته شده است. ارجاع نورایی به AHD:542 به مدخل خودِ فرهنگ اشاره دارد نه به پیوست ریشه‌های هندواروپایی، ولی همان پیوست هم همین زنجیره را می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/gangrene\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD:542\",\n              \"status\": \"not_checked\",\n              \"note\": \"the 1975/76 New College Edition (p. 542 would be the main-dictionary entry 'gangrene') is lending-only on archive.org and not readable from here. The Watkins appendix on disk (AHD_watkins1985.txt line 531) does state 'Reduplicated form *gar-gr- dissimilated in Greek gangraina, gangrene: GANGRENE. [Pok. gras- 404.]', which covers the Latin-to-English step implicitly.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout-Meillet s.v. gangraena\",\n              \"stance\": \"supports\",\n              \"note\": \"'gangraena (gangrena, can-), -ae f.: gangrène. Emprunt au gr. γάγγραινα' (LAT.txt line 25435).\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. gangrene\",\n              \"stance\": \"supports\",\n              \"note\": \"'L. gangraena, fr. Gk. γάγγραινα' — the same borrowing.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"gangrene\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English gangrene is first attested in the 1540s, initially in the Medieval Latin shape cancrena, then remodelled on the classical Latin gangraena, partly through French gangrène; Etymonline: '\\\"putrefaction or necrosis of soft tissues,\\\" 1540s, cancrena, from Latin gangraena (Medieval Latin cancrena), from medical Greek gangraina \\\"an eating or gnawing sore\\\" ... from PIE root *gras- \\\"to devour\\\"'. Klein gives the same short chain. The adjective gangrenous (1610s) is an English formation, perhaps after French gangréneux.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی gangrene نخستین بار در دههٔ ۱۵۴۰ میلادی و در آغاز به صورت cancrena (از لاتینی میانه) به کار رفته و سپس بر پایهٔ صورت کلاسیک gangraena و تا اندازه‌ای به میانجی فرانسهٔ gangrène بازساخته شده است؛ اتیمانلاین همین را می‌گوید: «از لاتینی gangraena، از یونانی پزشکی gangraina «زخم خورنده»، از ریشهٔ هندواروپایی *gras- «بلعیدن»». کلاین نیز همین زنجیره را دارد. صفت gangrenous (دههٔ ۱۶۱۰) ساختی انگلیسی است، شاید به قیاس فرانسهٔ gangréneux. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/gangrene\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"the box carries no reference of its own; it inherits AHD:542 from the Latin box above.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. gangrene\",\n              \"stance\": \"supports\",\n              \"note\": \"'gangrene, n., mortification; decay. — L. gangraena, fr. Gk. γάγγραινα ... Derivatives: gangrene, tr. and intr. v., gangrenous, adj.'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985, index and s.v. gras-\",\n              \"stance\": \"supports\",\n              \"note\": \"'GANGRENE gras-' in the word index; the root entry routes it through Greek gangraina.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Gredh\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *gʰredʰ- 'to walk, go, march' (Pokorny 456-457 gʰredʰ-; Watkins/AHD ghredh-)\",\n      \"note\": \"Correct on all counts, page number included. Pokorny: 'Root / lemma: gʰredʰ- / Meaning: to march / Material: Avestan aiwi-gərədmahi \\\"we begin, advance, go forward, march, proceed\\\", gərəzdi- \\\"(*lineup =) the captured, gained\\\" ... Latin gradior, -ī \\\"to take steps, step, walk, go\\\", gradus, -ūs \\\"a step ...\\\" ... Page(s): 456-457'; Watkins: 'ghredh-. To walk, go. Suffixed zero-grade form *ghrdh-yo- in: a. Latin gradi ... b. Latin gradus ... [Pok. ghredh- 456.]' Nourai's headword 'Gredh' drops the aspiration of the initial (Pokorny writes gʰredʰ-), which is his usual convention for the voiced aspirates, not an error of substance. The Latin-Romance-English half of the chart is Watkins's own list almost word for word (GRADE, CENTIGRADE, DEGREE, AGGRESS, CONGRESS, PROGRESS, REGRESS, GRESSORIAL). The Iranian half is where the entry is soft: the Avestan material is genuine but one gloss is wrong ('agreement' for gərəzdi-), and the Persian branch rests on Abolghasemi's reconstructed Old Iranian root *grā- 'to bend', which no comparative handbook actually attaches to gʰredʰ-.\",\n      \"note_fa\": \"این ریشه از هر سه جهت درست است و شمارهٔ صفحه هم درست: پوکورنی در ص ۴۵۶–۴۵۷ مادهٔ gʰredʰ- «گام برداشتن، رفتن» را با همین مواد اوستایی و لاتینی آورده و واتکینز نیز «ghredh-. To walk, go» را با ارجاع «[Pok. ghredh- 456]» ثبت کرده است. نورایی به عادت همیشگی خود «ه»ی دمیدگی را از آغاز ریشه انداخته و Gredh نوشته که خطای معنایی نیست. نیمهٔ لاتینی–رومیایی–انگلیسی نمودار تقریباً واژه‌به‌واژه از فهرست واتکینز گرفته شده است. نیمهٔ ایرانی سست‌تر است: صورت‌های اوستایی واقعی‌اند اما معنی gərəzdi- («توافق») نادرست است، و شاخهٔ فارسی بر ریشهٔ بازسازی‌شدهٔ *grā- «خم شدن» در کتاب ابوالقاسمی استوار است که هیچ فرهنگ تطبیقی آن را به gʰredʰ- نبسته است.\",\n      \"sources\": [\n        \"https://www.etymonline.com/word/grade\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:456\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt lines 33745-33770: 'Root / lemma: gʰredʰ- / Meaning: to march / Material: Avestan aiwi-garədmahi \\\"we begin, advance, go forward, march, proceed\\\", gərəzdi-t ... Latin gradior, -ī ... gradus, -ūs ... References: WP. I 651 f., WH. I 615 f., Trautmann 98. / Page(s): 456-457'.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985 s.v. ghredh-\",\n          \"stance\": \"supports\",\n          \"note\": \"'ghredh-. To walk, go. Suffixed zero-grade form *ghrdh-yo- in: a. Latin gradi (past participle gressus), to walk, go: GRESSORIAL; AGGRESS, CONGRESS, DEGRESSION, DIGRESS, EGRESS, INGRESS, PLANTIGRADE, PROGRESS, REGRESS, RETROGRESS, TRANSGRESS; b. Latin gradus ... GRADE; CENTIGRADE, DEGRADE, DEGREE, RETROGRADE. [Pok. ghredh- 456.]'\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Walde-Pokorny I 651\",\n          \"stance\": \"supports\",\n          \"note\": \"'gʰredʰ- \\\"schreiten\\\". Av. aiwi-gərədmahi \\\"wir beginnen, ingredimur\\\", gərəzdi- f. \\\"das (Antreten =) Inbesitznehmen, Bekommen\\\" (Bthl. Wb. 514 f., 524); ind. (Asoka-Inschr.) adhigicya \\\"beginnend\\\"' (WLD_Bd1 djvu line 41047 ff.).\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, IECD col. 336\",\n          \"stance\": \"partial\",\n          \"note\": \"Mann does not give ghredh- an article of its own — '(ghredh-, see ghréio, ghrés-)' — and puts Persian garāyam 'incline, tend' under ghreio/ghreiio, not under ghredh-; i.e. a different grouping from Pokorny's.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"aiwi-grad-mahi; gerezdi; grâ\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Three words of unequal standing. (1) aiwi-gərəδmahi is genuine and is Pokorny's own witness for the root: Bartholomae, Altiranisches Wörterbuch col. 514 s.v. 'garəd- V. \\\"gradi\\\", nur mit Praev. Praes. i gərəd-. mit aiwi \\\"ingredi, anheben, beginnen\\\": aiwi.gərəδmahi yasnahe haptaŋhātāiš ... Lat. vgl. gradior', so 1 pl. pres. 'we begin/enter upon', literally 'we step into', from the zero-grade *gʰr̥dʰ- with the preverb aiwi- 'upon'; Nourai's 'aiwi-grad-mahi' normalises the schwa vowels but is the same form. (2) 'gerezdi' is likewise a real Gathic word, but the gloss is wrong: Bartholomae col. 524 has 'g. gərəzday- f. \\\"Inbesitznehmen; Bekommen\\\"' and Walde-Pokorny I 651 'gərəzdi- f. \\\"das (Antreten =) Inbesitznehmen, Bekommen\\\"' — 'taking possession, obtaining', an abstract of the same 'step up to' semantics, not 'agreement'; it is also Gathic Avestan only, so the 'Old Persian' half of the box label is unsupported. (3) 'grā \\\"to lean toward\\\"' is not an attested Avestan or Old Persian word at all: it is the Old Iranian root Abolghasemi posits in the source Nourai cites, Feʿl-hā-ye Fārsi-ye Dari p. 71, 'ریشهٔ grā به معنی خم شدن است' ('the root grā means \\\"to bend\\\"'), reconstructed backwards from the Persian verb. Attaching that *grā- to gʰredʰ- is Nourai's own step, and it is phonologically awkward: gʰredʰ- has a root-final dental that *grā- lacks.\",\n          \"derivation_fa\": \"سه واژه با اعتبار نابرابر. یکم، aiwi-gərəδmahi اصیل است و خودِ گواه پوکورنی برای این ریشه: بارتولومه در «فرهنگ ایرانی باستان» ستون ۵۱۴ ذیل garəd- می‌نویسد این فعل «gradi» است و تنها با پیشوند به کار می‌رود، و با aiwi معنی «آغاز کردن، درآمدن» می‌دهد، و خود لاتینی gradior را به مقایسه می‌آورد؛ صورت نورایی همان است با ساده‌سازی واکه‌های کوتاه. دوم، gərəzdi- نیز واژه‌ای گاهانی و حقیقی است اما معنی‌اش «توافق» نیست: بارتولومه (ستون ۵۲۴) و والده-پوکورنی (ج۱ ص ۶۵۱) آن را «به‌دست‌آوردن، تصرف کردن» معنی کرده‌اند؛ افزون بر این تنها اوستایی گاهانی است و ربطی به پارسی باستان ندارد، پس برچسب «اوستایی/پارسی باستان» این خانه بی‌پشتوانه است. سوم، grā «متمایل شدن» اصلاً واژهٔ اوستایی یا پارسی باستان نیست، بلکه ریشهٔ بازسازی‌شدهٔ ایرانی باستان در کتاب ابوالقاسمی («ماده‌های فعل‌های فارسی دری» ص ۷۱: «ریشهٔ grā به معنی خم شدن است») است که از روی فعل فارسی بازسازی شده. پیوند دادن این *grā- به gʰredʰ- کارِ خودِ نورایی است و از نظر آوایی هم آسان نیست، چون در gʰredʰ- یک دندانیِ پایانی هست که در *grā- نیست.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:456\",\n              \"status\": \"partial\",\n              \"note\": \"Pokorny p. 456 has 'Avestan aiwi-garədmahi \\\"we begin, advance, go forward, march, proceed\\\", gərəzdi-t \\\"(*lineup =) the captured, gained\\\"' — the first two words, but glossing gərəzdi- 'the captured, gained', not 'agreement', and knowing no Iranian *grā-.\"\n            },\n            {\n              \"ref\": \"FFD:71\",\n              \"status\": \"supports\",\n              \"note\": \"Abolghasemi, Feʿl-hā-ye Fārsi-ye Dari p. 71 (FFD_pages.txt pdf leaf 76, header ۷۱), s.v. گراییدن: 'گرای < فارسی میانه grāy < ایرانی باستان *grā-ya-. ya نشانه‌ای بوده که برای ساختن مادهٔ مضارع از ریشه به کار می‌رفته است. ریشهٔ grā به معنی «خم شدن» است.' — this is exactly Nourai's third word and his Pahlavi box, but Abolghasemi does not link *grā- to gʰredʰ- or to the Avestan forms.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Altiranisches Wörterbuch cols. 514-515 and 524\",\n              \"stance\": \"partial\",\n              \"note\": \"col. 514: 'j. garəd- V. \\\"gradi\\\", nur mit Praev. Praes. i gərəd-. mit aiwi \\\"ingredi, anheben, beginnen\\\": aiwi.gərəδmahi ... Lat. vgl. gradior. — Vgl. gərəzday-'; col. 524: 'g. gərəzday- f. \\\"Inbesitznehmen; Bekommen\\\"'. Both forms confirmed, the gloss 'agreement' contradicted, and no entry *grā-.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny I 651\",\n              \"stance\": \"partial\",\n              \"note\": \"'Av. aiwi-gərədmahi \\\"wir beginnen, ingredimur\\\", gərəzdi- f. \\\"das (Antreten =) Inbesitznehmen, Bekommen\\\" (Bthl. Wb. 514 f., 524)' — same two forms, same corrected gloss, nothing Old Persian.\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian lexicon\",\n              \"stance\": \"silent\",\n              \"note\": \"no Old Persian reflex of this root is listed; the box's 'Old Persian' label has no support.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Etymological Dictionary of the Iranian Verb\",\n              \"stance\": \"silent\",\n              \"note\": \"Cheung has no root *graH 'to incline' (his *graH ? is glossed 'to smell') and no *grad- of this meaning; his only grad- material is MMP gry-, BMP gl(y)dy- /griy-/ 'to weep' (< OP *grad-ya-), a different verb (Persian گریستن).\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"grây\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"A Middle Iranian grāy- 'to incline' is attested, though not in the Zoroastrian Book-Pahlavi corpus: Moʿin's own footnote 10 to Borhān-e Qāṭeʿ p. 1783 (the page Nourai cites for the Persian box) says of گرایستن that 'جزو اول در اوراق مانوی به پارتی grāy- (متمایل شدن، لیز خوردن، افتادن)' — 'the first element appears in the Manichaean leaves in Parthian as grāy- \\\"to incline, to slip, to fall\\\"' — citing Boyce/Henning's Manichaean reader. Abolghasemi (FFD p. 71) posits the same Middle Persian present stem: 'گرای < فارسی میانه grāy < ایرانی باستان *grā-ya-', with -ya- the regular Old Iranian present-stem suffix (so *grā-ya- > grāy, exactly as *sāt-aya- > sāy- and other -ya- presents). MacKenzie's Concise Pahlavi Dictionary and Nyberg's glossary both lack the verb, so it is Parthian/Manichaean rather than Book-Pahlavi evidence. The form and its meaning are therefore well supported; what remains unproven is the parent arrow, since neither Abolghasemi nor Moʿin traces grāy- to gʰredʰ-.\",\n          \"derivation_fa\": \"فعل ایرانی میانهٔ grāy- «متمایل شدن» گواه دارد، هرچند در پیکرهٔ پهلوی زردشتی نیست: معین در حاشیهٔ ۱۰ برهان قاطع ص ۱۷۸۳ (همان صفحه‌ای که نورایی برای خانهٔ فارسی آورده) می‌نویسد جزو اول «گرایستن» در اوراق مانوی به پارتی grāy- «متمایل شدن، لیز خوردن، افتادن» آمده است و به گزیدهٔ متون مانوی هنینگ/بویس ارجاع می‌دهد. ابوالقاسمی (ص ۷۱) همین ستاک را می‌نهد: «گرای < فارسی میانهٔ grāy < ایرانی باستان *grā-ya-»، که در آن -ya- پسوند معمول ساخت مادهٔ مضارع در ایرانی باستان است. مکنزی و نیبرگ این فعل را ندارند، پس گواه از پارتی مانوی است نه از پهلوی کتابی. صورت و معنی پذیرفتنی است؛ آنچه اثبات نشده پیوند آن با ریشهٔ gʰredʰ- است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"FFD:71\",\n              \"status\": \"supports\",\n              \"note\": \"'گرای < فارسی میانه grāy < ایرانی باستان *grā-ya-' (FFD_pages.txt pdf leaf 76 = printed p. 71) — precisely Nourai's Pahlavi box and its gloss.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhān-e Qāṭeʿ p. 1783, Moʿin's footnote 10\",\n              \"stance\": \"supports\",\n              \"note\": \"'گرایستن: جزو اول در اوراق مانوی به پارتی grāy- (متمایل شدن، لیز خوردن، افتادن)' with a reference to the Manichaean Middle Persian and Parthian reader.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie 1971, letter g\",\n              \"stance\": \"silent\",\n              \"note\": \"no grāy- between gōhr and griftan; the verb is absent from Book Pahlavi.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II\",\n              \"stance\": \"silent\",\n              \"note\": \"no entry grāy- in the glossary.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"grâyîdan «گراییدن»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Persian material of the box is exactly right. Borhān-e Qāṭeʿ p. 1783 — the cited page, whose rendering prints its own number ۱۷۸۳ — carries all four forms in a row: 'گرای: بمعنی میل و رغبت و خواهش و قصد و آهنگ باشد'; 'گراید ... یعنی قصد و آهنگ کند و میل و رغبت نماید'; 'گرایستن: بمعنی قصد کردن و آهنگ نمودن و میل و خواهش کردن باشد'; 'گرایش: بمعنی قصد و آهنگ و میل و خواهش', the last illustrated with the very Nezāmi couplet the chart quotes, 'گهی دل برفتن گرایش کند / گهی خواب را سرستایش کند'. Morphologically گراییدن is a secondary infinitive built on the present stem گرای (Abolghasemi: 'گرایید ... مادهٔ ماضی جعلی است، از مادهٔ مضارع ساخته شده'), گرایستن the older -istan formation, گرایش the verbal noun in -iš. What is not settled is the ancestry: Abolghasemi's *grā-ya- backs Nourai, but Wiktionary (following Hasandust) instead derives گراییدن from Middle Persian wurrōyistān 'to believe, to choose (a religion)' < Proto-Iranian *war-, conflating it with گرویدن, and Mann's Indo-European Comparative Dictionary col. 336 files Persian garāyam 'incline, tend' under gʰrēi-/gʰreiio, not under gʰredʰ-. Three incompatible etymologies for one verb, of which Nourai's is one respectable option.\",\n          \"derivation_fa\": \"مواد فارسی این خانه کاملاً درست است. برهان قاطع ص ۱۷۸۳ — همان صفحه‌ای که نورایی آورده و شمارهٔ ۱۷۸۳ روی تصویرش خوانده می‌شود — هر چهار صورت را پشت سر هم دارد: «گرای: بمعنی میل و رغبت و خواهش و قصد و آهنگ باشد»؛ «گراید ... یعنی قصد و آهنگ کند و میل و رغبت نماید»؛ «گرایستن: بمعنی قصد کردن و آهنگ نمودن»؛ «گرایش: بمعنی قصد و آهنگ و میل و خواهش»، و این آخری را با همان بیت نظامی می‌آورد که در نمودار نقل شده است. از نظر ساخت، «گراییدن» مصدر جعلی است که از مادهٔ مضارع «گرای» ساخته شده (ابوالقاسمی: «گرایید ... مادهٔ ماضی جعلی است»)، «گرایستن» صورت کهن‌تر با پسوند -ستن، و «گرایش» اسم مصدر با پسوند -ش. آنچه قطعی نیست تبار واژه است: ابوالقاسمی *grā-ya- را می‌نهد و پشتیبان نورایی است، اما ویکی‌واژه (به پیروی حسن‌دوست) «گراییدن» را از فارسی میانهٔ wurrōyistān «گرویدن، دین گزیدن» و ریشهٔ *war- می‌گیرد و آن را با «گرویدن» یکی می‌داند، و مان در «فرهنگ تطبیقی هندواروپایی» فعل garāyam فارسی را ذیل gʰrēi- می‌آورد نه gʰredʰ-. پس سه ریشه‌شناسی ناسازگار در کار است و رأی نورایی یکی از آن‌هاست: با احتیاط پذیرفتنی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D8%A7%DB%8C%DB%8C%D8%AF%D9%86\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"FFD:71\",\n              \"status\": \"supports\",\n              \"note\": \"printed p. 71 s.v. گراییدن: 'گرایید < فارسی میانه grāyīd. مادهٔ ماضی جعلی است، از مادهٔ مضارع ساخته شده است. گرای < فارسی میانه grāy < ایرانی باستان *grā-ya- ... ریشهٔ grā به معنی «خم شدن» است.'\"\n            },\n            {\n              \"ref\": \"BQT:1783\",\n              \"status\": \"supports\",\n              \"note\": \"Borhān p. 1783 (tools/ref_page.py BQT:1783, vol. 3 pdf p. 580; the rendered page prints ۱۷۸۳) has گرای, گراید, گرایستن, گرایش and گرایید with the meanings 'میل و رغبت و خواهش و قصد و آهنگ' and Moʿin's Parthian footnote — every form of Nourai's box including the extras and the Nezāmi verse.\"\n            },\n            {\n              \"ref\": \"VSF:16\",\n              \"status\": \"not_checked\",\n              \"note\": \"Mehravand, Vāzhe-sāzi dar Zabān-e Fārsi (1349/1970) is not digitised anywhere accessible (refs_online.json: 'kind: none, Not found').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BQT\",\n              \"where\": \"p. 1783 and its footnotes 10-13\",\n              \"stance\": \"supports\",\n              \"note\": \"'گرایش ... بمعنی قصد و آهنگ - و میل و خواهش - و پیچش باشد که از نافرمانی کردن است' + the Nezāmi couplet 'گهی دل برفتن گرایش کند / گهی خواب را سرستایش کند' quoted from Farhang-e Sorurī, exactly as in the chart.\"\n            },\n            {\n              \"src\": \"Wiktionary\",\n              \"where\": \"گراییدن\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'Inherited from Middle Persian (HYMNN-stn' /wurrōyistān/, \\\"to believe, to choose (a religion)\\\"), ultimately from Proto-Iranian *war- (\\\"to choose, to believe\\\"). Compare Avestan var- \\\"to believe\\\"' — a different origin altogether, treating گراییدن as one lemma with گرویدن.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, IECD col. 336 s.v. ghreio/ghreiio\",\n              \"stance\": \"partial\",\n              \"note\": \"'Per. garāyam = \\\"incline, tend\\\"' is listed there, i.e. Mann attaches the Persian verb to gʰrēi- and explicitly cross-references '(ghredh-, see ghréio, ghrés-)'.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Etymological Dictionary of the Iranian Verb\",\n              \"stance\": \"silent\",\n              \"note\": \"no entry for a root yielding grāy- 'to incline'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"gradi, gressus; gradus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin gradior, gradī, gressus sum 'to step, walk, go' continues the zero grade *gʰr̥dʰ-yo- (Watkins: 'Suffixed zero-grade form *ghrdh-yo- in Latin gradi'), with the regular Latin development of syllabic r̥ to ra and of the voiced aspirate to d; the supine stem gress- is from *gradh-to- by assimilation. Pokorny p. 456 prints exactly this ('Latin gradior, -ī \\\"to take steps, step, walk, go\\\", gradus, -ūs \\\"a step; a step as made, a pace ... abstr., degree, stage; rank, position; milit., station, post\\\"; Latin grad- from *gʰr̥dʰ-, ablaut grade as in Lithuanian gridiju'), with Gothic grids 'footstep', Old Irish in-grenn- 'pursue' and Old Church Slavonic gręd-, gręsti 'go, come' as cognates. gradus is the u-stem deverbative; Ernout-Meillet: 'Gradus est à gradior comme impetus à impeto.'\",\n          \"derivation_fa\": \"فعل لاتینی gradior, gradī, gressus sum «گام برداشتن، رفتن» بازماندهٔ درجهٔ صفر *gʰr̥dʰ-yo- است؛ واتکینز نیز همین را می‌گوید. rِ هجایی هندواروپایی در لاتینی به ra بدل شده و dʰ دمیده به d ساده؛ ستاک مفعولی gress- از *gradh-to- با همگونی پدید آمده است. پوکورنی در ص ۴۵۶ عیناً همین دو واژه را می‌آورد و gradus را «گام؛ پله؛ پایه و رتبه» معنی می‌کند و گوتی grids «گام»، ایرلندی کهن in-grenn- «تعقیب کردن» و اسلاوی کلیسایی کهن gręsti «رفتن» را هم‌ریشه می‌شمارد. gradus اسمِ فعلیِ ستاک -u است؛ ارنو و می‌یه می‌نویسند «نسبت gradus به gradior همان نسبت impetus به impeto است». ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/grade\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:456\",\n              \"status\": \"supports\",\n              \"note\": \"'Latin gradior, -ī \\\"to take steps, step, walk, go\\\", gradus, -ūs \\\"a step ...\\\" (Latin grad- from *gʰr̥dʰ-, ablaut grade as in Lithuanian gridiju)' — Nourai's two words with his two glosses.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout-Meillet s.v. gradior / gradus\",\n              \"stance\": \"supports\",\n              \"note\": \"'gradior, -eris, gressus sum, gradī: marcher' and 'Gradus est à gradior comme impetus à impeto. — À gradus plutôt qu'à gradior se rattachent gradātio ...' (LAT.txt lines 26607-26625).\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. ghredh-\",\n              \"stance\": \"supports\",\n              \"note\": \"'Suffixed zero-grade form *ghrdh-yo- in: a. Latin gradi (past participle gressus), to walk, go ...; b. Latin gradus (< deverbative *grad-u-), step, stage, degree, rank.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"French\",\n          \"words\": \"grade; congres\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both French words are learned sixteenth-century borrowings straight from Latin, not inherited: grade (16c.) 'grade, degree' from Latin gradus (Etymonline, s.v. grade: '1510s ... from French grade \\\"grade, degree\\\" (16c.), from Latin gradus'), and congrès from Latin congressus 'a meeting, an encounter', the perfect participle of congredī 'to come together' (com- 'with' + gradī). French had already inherited a popular reflex of the same Latin noun in degré (12c.) from Vulgar Latin *degradus. The box spells congres without the accent, as the book does throughout for French forms.\",\n          \"derivation_fa\": \"هر دو واژهٔ فرانسوی وام‌واژه‌های کتابی سدهٔ شانزدهم‌اند که یکراست از لاتینی گرفته شده‌اند، نه بازماندهٔ تحول طبیعی: grade «درجه، پایه» از gradus لاتینی (اتیمانلاین ذیل grade: «از فرانسهٔ grade سدهٔ شانزدهم، از لاتینی gradus») و congrès از congressus لاتینی، اسم مفعول congredī «گرد هم آمدن» (com- «با هم» + gradī «گام برداشتن»). فرانسوی پیش‌تر بازماندهٔ عامیانهٔ همین اسم لاتینی را در degré (سدهٔ دوازدهم، از لاتینی عامیانهٔ *degradus) داشت. در کتاب congres بدون علامت نوشته شده، چنان‌که با صورت‌های فرانسوی همه‌جا چنین می‌کند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/grade\",\n            \"https://www.etymonline.com/word/congress\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"partial\",\n              \"note\": \"Watkins's appendix (AHD_watkins1985.txt line 526) lists GRADE and CONGRESS under ghredh- but routes both directly through Latin (gradus, gradi) without naming a French stage; the French intermediary for grade is supplied by Etymonline and Skeat.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.v. Grade\",\n              \"stance\": \"supports\",\n              \"note\": \"'Grade, a degree. (F.-L.) F. grade ...' — Skeat's (F.-L.) tag is exactly the French-from-Latin route of this box (SKT.txt line 7851).\"\n            },\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout-Meillet s.v. gradior\",\n              \"stance\": \"supports\",\n              \"note\": \"'En composition, ex- marque l'idée de sortir: eo/exeo, gradior/egredior' — the compound type congredior/congressus that gives French congrès.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"kongereh 2 «کنگره ۲»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A twentieth-century French loan, kept apart in the dictionaries from the homophonous inherited کنگره 'battlements, crenellation'. Moʿin's Farhang-e Fārsi gives them as two entries in succession: 'کنگره: [- کنگر] (اِ.) پستی و بلندی مرتب بالای دیوار؛ دندانه‌های بالای دیوار قصر و حصار قلعه، شرفه' and then 'کنگره: [Fr.] (اِ.) مجمعی از سران دول، نمایندگان ممالک یا دانشمندان که دربارهٔ مسایل سیاسی، اقتصادی، عملی و غیره بحث کنند. مجلس قانون‌گذاری ایالات متحدهٔ آمریکا' — the second is Nourai's 'kongereh 2', with the French tag, borrowed from congrès with the -eh that Persian regularly adds to French words ending in a consonant cluster (cf. کمیته, کمدی). The two extras of the box, گراد and سانتیگراد, are the same kind of loan from French grade and centigrade, current in Persian since the metric and thermometric vocabulary was adopted.\",\n          \"derivation_fa\": \"«کنگره ۲» وام‌واژه‌ای فرانسوی از سدهٔ چهاردهم خورشیدی است که فرهنگ‌ها آن را از «کنگرهٔ» اصیل فارسی (دندانهٔ دیوار و باروی قلعه) جدا نگه می‌دارند. معین این دو را پشت سر هم و در دو مدخل آورده است: نخست «کنگره: پستی و بلندی مرتب بالای دیوار؛ دندانه‌های بالای دیوار قصر و حصار قلعه، شرفه» و سپس «کنگره: [فر.] مجمعی از سران دول، نمایندگان ممالک یا دانشمندان که دربارهٔ مسایل سیاسی، اقتصادی، عملی و غیره بحث کنند؛ مجلس قانون‌گذاری ایالات متحدهٔ آمریکا» — همین دومی مقصود نورایی است، وام‌گرفته از congrès فرانسوی با «ه»ی پایانی که فارسی معمولاً به وام‌واژه‌های فرانسویِ مختوم به همخوان می‌افزاید (مانند کمیته، کمدی). دو واژهٔ افزودهٔ این خانه، «گراد» و «سانتیگراد»، نیز از همان راه و از grade و centigrade فرانسوی آمده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/congress\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:3102,3212\",\n              \"status\": \"supports\",\n              \"note\": \"Moʿin, Farhang-e Fārsi (MON_part2.txt line 27427): 'کنگره: [Fr.] (اِ.) مجمعی از سران دول نمایندگان ممالک یا دانشمندان که دربارهٔ مسایل سیاسی اقتصادی، عملی و غیره بحث کنند. مجلس قانون‌گذاری ایالات متحدهٔ آمریکا', immediately after the inherited کنگره 'دندانه‌های بالای دیوار قصر و حصار قلعه' — Nourai's two page numbers correspond to the two homonyms and to the گراد/سانتیگراد entries; the printed pagination of the 6-vol. Amir Kabir edition cannot be mapped from the copy on disk.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"s.v. کنگره (both entries)\",\n              \"stance\": \"supports\",\n              \"note\": \"the French tag [Fr.] on the 'congress' entry is Moʿin's own statement of the borrowing.\"\n            },\n            {\n              \"src\": \"Etymonline\",\n              \"where\": \"congress\",\n              \"stance\": \"supports\",\n              \"note\": \"'from Latin congressus \\\"a friendly meeting; a hostile encounter\\\", past participle of congredi \\\"to meet with; to fight with\\\", from ... com \\\"with, together\\\" + gradi \\\"to walk, step\\\", from gradus \\\"a step\\\" (from PIE root *ghredh- \\\"to walk, go\\\")' — the ultimate source of the Persian loan.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"grade; congress; centigrade; degree; gradient\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"All five belong to the root, but only three of them came through French, so the box's parentage is right for some words and wrong for others. Via French: grade (1510s, 'from French grade \\\"grade, degree\\\" (16c.), from Latin gradus', Etymonline; Skeat tags it (F.-L.)), degree (c. 1200, 'from Old French degré (12c.) ... from Vulgar Latin *degradus', Skeat: 'degree. (F.-L.) O.F. degre ... L. de, down; gradus, a step'), and centigrade (a French coinage of the 1790s thermometric reform, on Latin centum + gradus; Skeat: 'centigrade. (L.) Divided into a hundred degrees. — L. centi-, for centum; gradus, a degree'). Not via French: congress, which entered English about 1400 straight from Latin congressus, long before the French word could have mediated ('c. 1400, \\\"a body of attendants\\\" ... from Latin congressus', Etymonline), and gradient, a nineteenth-century learned formation on the Latin present participle gradientem. Watkins lists all five under ghredh- but routes them through Latin, not French. So: root membership confirmed, the French box a partial overreach.\",\n          \"derivation_fa\": \"هر پنج واژه به همین ریشه بازمی‌گردند، اما تنها سه‌تای آن‌ها از راه فرانسه به انگلیسی رسیده‌اند، پس والدِ این خانه برای برخی درست است و برای برخی نه. از راه فرانسه: grade (۱۵۱۰ میلادی، از grade فرانسوی از gradus لاتینی)، degree (حدود ۱۲۰۰، از degré فرانسوی کهن از لاتینی عامیانهٔ *degradus؛ اسکیت هم آن را (F.-L.) نشانه زده) و centigrade (ساختهٔ فرانسویان در اصلاح دماسنجی دههٔ ۱۷۹۰، از centum + gradus لاتینی). نه از راه فرانسه: congress که نزدیک سال ۱۴۰۰ یکراست از congressus لاتینی وارد انگلیسی شد، و gradient که ساختی کتابی از سدهٔ نوزدهم بر پایهٔ اسم فاعل لاتینی gradientem است. واتکینز هر پنج را ذیل ghredh- می‌آورد اما همه را از لاتینی می‌گیرد نه از فرانسه. پس عضویت در ریشه تأیید می‌شود ولی خانهٔ «فرانسوی» بیش از اندازه گسترانده شده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/grade\",\n            \"https://www.etymonline.com/word/degree\",\n            \"https://www.etymonline.com/word/congress\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"partial\",\n              \"note\": \"Watkins (AHD_watkins1985.txt line 526 and index lines 1340, 1392, 1418, 1553) has all five words under ghredh- — 'GRADE ghredh-', 'CENTIGRADE ghredh-', 'CONGRESS ghredh-', 'DEGREE ghredh-', and gradient under the same root via Latin gradi — but derives them from Latin gradus/gradi directly, without a French stage, so it supports the root assignment and not the French parent.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.vv. Grade, Degree, Centigrade\",\n              \"stance\": \"supports\",\n              \"note\": \"'Grade, a degree. (F.-L.) F. grade'; 'degree. (F.-L.) O.F. degre, degrе́, step, rank; orig. a step down (used of stairs). — L. de, down; gradus, a step'; 'centigrade. (L.) Divided into a hundred degrees. — L. centi-, for centum; gradus, a degree; see Grade' — note that Skeat tags centigrade (L.), not (F.-L.).\"\n            },\n            {\n              \"src\": \"Etymonline\",\n              \"where\": \"congress, degree, grade\",\n              \"stance\": \"partial\",\n              \"note\": \"congress 'c. 1400 ... from Latin congressus' (no French stage); degree 'from Old French degré (12c.)'; grade 'from French grade (16c.)'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"aggressive; progress; regression; ingredient; graduate\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All five are learned borrowings from Latin compounds of gradī and gradus, and Watkins puts each of them under ghredh-: aggressive from aggredī (ad- + gradī) 'to step toward, attack', progress from prōgressus (prō- + gradī) 'a going forward', regression from regressiō (re- + gradī) 'a going back', ingredient from ingrediēns, the present participle of ingredī 'to step into' — the same compound Bartholomae uses to gloss the Avestan aiwi-gərəδmahi ('mit aiwi \\\"ingredi, anheben, beginnen\\\"'), which makes this box and node #1 formal twins across the family — and graduate from Medieval Latin graduātus 'admitted to a degree', a denominative of gradus. In each the root-final dental appears as the Latin -d- of grad-/-gred- (unstressed vowel weakening a > e in the compounds), with -gress- < *grad-to- in the participial stem.\",\n          \"derivation_fa\": \"هر پنج واژه وام‌گیری کتابی از ترکیب‌های لاتینیِ gradī و gradus هستند و واتکینز همه را ذیل ghredh- می‌آورد: aggressive از aggredī (ad- + gradī) «به‌سوی کسی گام برداشتن، حمله کردن»، progress از prōgressus «پیش رفتن»، regression از regressiō «بازگشت»، ingredient از ingrediēns، اسم فاعل ingredī «درآمدن» — همان فعلی که بارتولومه با آن aiwi-gərəδmahi اوستایی را معنی می‌کند و از این رو این خانه و خانهٔ ۱ همزادِ ساختاری یکدیگرند — و graduate از graduātus لاتینی میانه «دارندهٔ درجه»، مشتق از gradus. در همهٔ این‌ها دندانیِ پایانی ریشه به صورت -d- در grad-/-gred- دیده می‌شود (با ضعیف‌شدن a به e در ترکیب‌ها) و در ستاک اسم مفعولی به -gress- (< *grad-to-) بدل شده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/grade\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins s.v. ghredh- lists 'GRESSORIAL; AGGRESS, CONGRESS, DEGRESSION, DIGRESS, EGRESS, INGRESS, PLANTIGRADE, PROGRESS, REGRESS, RETROGRESS, TRANSGRESS' under Latin gradi and 'GRADE; CENTIGRADE, DEGRADE, DEGREE, RETROGRADE' under gradus; the index confirms 'AGGRESS ghredh-', 'PROGRESS ghredh-', 'REGRESS ghredh-', 'INGRESS ghredh-'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. ghredh- and word index\",\n              \"stance\": \"supports\",\n              \"note\": \"the whole Latin-compound family is listed there under this root.\"\n            },\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout-Meillet s.v. gradior\",\n              \"stance\": \"supports\",\n              \"note\": \"'En composition, ex- marque l'idée de sortir: eo/exeo, gradior/egredior' and 'duratif de gradior: marcher, s'avancer; au sens moral: procéder' — the compound pattern behind aggredior, progredior, regredior, ingredior.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T02:35:24.290Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-199.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T02:35:28.325Z] TOOL CALL #51: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-199.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 199"
}
```


### [2026-09-06T02:35:30.749Z] TOOL RESULT

```
JSON OK
nodes verified: 15/15
node verdicts: {'plausible': 6, 'confirmed': 7, 'transcription_suspect': 2}
root verdicts: {'plausible': 1, 'confirmed': 2}
ref checks: {'supports': 11, 'partial': 5, 'not_checked': 4, 'not_found': 1}
books consulted: {'supports': 26, 'contradicts': 3, 'silent': 7, 'partial': 4} | by book: {'BQT': 5, 'AHD': 4, 'LAT': 4, 'Wiktionary': 3, 'KLN': 3, 'MON': 3, 'PHD': 2, 'NYB': 2, 'WLD': 2, 'CHEUNG': 2, 'SKT': 2, 'Etymonline': 2, 'HUB': 1, 'HRN': 1, 'FSF': 1, 'BRT': 1, 'KNT': 1, 'IEC': 1}
```


## [2026-09-06T02:35:47.826Z] AGENT

Done — `data/verification/page-199.json` written, valid JSON, `verify_check.py 199` reports 0 PROBLEM lines.

**Page 199 (book p. 169) — 3 entries, 15 nodes**
- Root verdicts: 2 confirmed (Gras/POK 404, Gredh/POK 456), 1 plausible (Gôtra).
- Node verdicts: 7 confirmed, 6 plausible, 2 transcription_suspect.
- Ref checks: 11 supports, 5 partial, 1 not_found, 4 not_checked (ARK:249, VSF:16 not digitised; AHD:542 lending-only).

Flagged items:
- **Gôtra, root + node #1 (Pahlavi gōhar)** — plausible, not confirmed: Skt. *gotra-* is a **cognate**, not the ancestor. MP *gōhr* < OP \*gauθrā < PIr \*gawθraH. Horn p. 211 no. 948 (the cited page) only adduces *gōtra-* as a comparandum; Hübschmann, Pers. Stud. p. 96, note to that very paragraph, calls the etymology "bedenklich" (Vedic *gotra-* = 'cowshed'; NP should be \*gōhr, not *gōhar*).
- **Gras #1 (Greek) — transcription_suspect, error in the BOOK**: the printed page really shows "gangraina, **gagrajna**"; *gagrajna* is no Greek form (extraction faithful). Separately, Beekes/Wiktionary reject the *gras-* etymology of γάγγραινα as "most probably a Pre-Greek word" (Pokorny, Klein, Watkins, Etymonline keep it).
- **Gras #3 (Persian) — transcription_suspect, error in the EXTRACTION** → **owner fix needed**: the book prints two forms, **غانغرایا ، غانقرایا**; the JSON has `script: "غانقرایا"` and `script_extra: "غانقرایا"` (headword form غانغرایا lost, variant duplicated). Moʿin's headword is غانغرایا.
- **Gredh #1** — Pokorny/Bartholomae/Walde-Pokorny gloss *gərəzdi-* 'taking possession, obtaining', **not "agreement"**; it is Gathic only, so the "Old Persian" label is unsupported; *grā* is Abolghasemi's reconstructed root, not an attested Avestan/OP word.
- **Gredh #7** — French parent is only partly right: *grade*, *degree*, *centigrade* via French; *congress* (c. 1400) and *gradient* come straight from Latin.
- Wrong page number (not an extraction error): **BQT:1862** — گوهر is on printed p. **1864** (1862 = گوگرد…گول). **BQT:1339** = the ط chapter opening, nothing on gangrene → not_found.
- Page image archived at `data/verification/sources/refs/ocr/BOOK/199.png`; 10 web sources archived via `fetch_source.py`.
