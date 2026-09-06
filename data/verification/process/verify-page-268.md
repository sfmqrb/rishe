# Verification process log — verify-page-268


## [2026-09-06T20:51:25.058Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 268 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-268.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-268.json. Write /home/sfmqrb/git/rishe/data/verification/page-268.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 268` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T20:51:26.455Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-06T20:51:27.197Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T20:51:27.215Z] TOOL RESULT

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


## [2026-09-06T20:51:27.435Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-268.txt"
}
```


### [2026-09-06T20:51:27.459Z] TOOL RESULT

```
1	=== PDF page 268 (book page 238) ===
2	--- entry 0 ---
3	ROOT [Akkadian] Kîru : wax  (refs AKD:60)
4	#1 (parent #0) [Latin] refs=KLN | crassus : fat, oil ; crassia : thickness (of liquids)
5	  #2 (parent #1) [Old French] refs=None | 
6	    #3 (parent #2) [English] refs=KLN; AHD | grease
7	      #4 (parent #3) [Persian] refs=VFO:24 | grîs «گریس» : grease
8	#5 (parent #0) [Greek] refs=AHD:718 | kěros : wax
9	  #6 (parent #5) [Aramaic] refs=None | qîra : wax, tar
10	    #7 (parent #6) [Arabic] refs=AKD:60 | qîr : tar ; târ : tar
11	      #8 (parent #7) [Persian] refs=MON:2765; BQT:1550 | qîr «قیر» : tar
12	#9 (parent #0) [English] refs=KLN:843 | kerosene
13	--- entry 1 ---
14	ROOT Kitintu -> redirect to Kitu
15	--- entry 2 ---
16	ROOT [Akkadian] Kitu, Kitintu, Kitunnŭ : cotton clothing  (refs BQT:1594)
17	#1 (parent #0) [Arabic] refs=BQT:1594 | qutun : cotton
18	  #2 (parent #1) [Persian] refs=BQT:1594; MON:3543 | katân «کتان» : cotton
19	  #3 (parent #1) [Spanish] refs=AHD | coton
20	    #4 (parent #3) [French] refs=None | coton
21	      #5 (parent #4) [English] refs=KLN:360 | cotton
22	#6 (parent #0) [Hebrew] refs=KLN:1664 | kuttoneth : cotton clothing
23	  #7 (parent #6) [Aramaic] refs=KLN:1664 | kittunâ
24	    #8 (parent #7) [Latin] refs=KLN:1664 | ctunica, tunica : cotton clothing, tunic
25	      #9 (parent #8) [Persian] refs=MON:1154 | tonekeh «تُنکه» : underwear | NOTE: "tonekeh" is probably from "tonok: thin, soft". See root "Ten 1".
26	      #10 (parent #8) [French] refs=None | 
27	        #11 (parent #10) [English] refs=None | tunic
28	          #12 (parent #11) [Persian] refs=VOP:154 | tonîc «تونیک» : a piece of women clothing
29	    #13 (parent #7) [Greek] refs=KLN:1664 | kiton : cotton shirt
30	      #14 (parent #13) [English] refs=AHD:236 | chiton
31	--- entry 3 ---
32	ROOT Kitunnŭ -> redirect to Kitu
33	--- entry 4 ---
34	ROOT Klâu -> redirect to Klěu 2
35	
```


## [2026-09-06T20:51:29.551Z] AGENT

I'll read the source JSON and the reference metadata.


## [2026-09-06T20:51:30.937Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-268.json",
 "description": "Read page 268 extracted JSON"
}
```


### [2026-09-06T20:51:30.975Z] TOOL RESULT

```
{
  "pdf_page": 268,
  "book_page": 238,
  "entries": [
    {
      "root": {
        "name": "Kîru",
        "lang": "Akkadian",
        "refs": "AKD:60",
        "gloss": "wax"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Latin",
          "refs": "KLN",
          "words": [
            {"translit": "crassus", "gloss": "fat, oil", "script": null},
            {"translit": "crassia", "gloss": "thickness (of liquids)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Old French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "KLN; AHD",
          "words": [
            {"translit": "grease", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "VFO:24",
          "words": [
            {"translit": "grîs", "gloss": "grease", "script": "گریس"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:718",
          "words": [
            {"translit": "kěros", "gloss": "wax", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Aramaic",
          "refs": null,
          "words": [
            {"translit": "qîra", "gloss": "wax, tar", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Arabic",
          "refs": "AKD:60",
          "words": [
            {"translit": "qîr", "gloss": "tar", "script": null},
            {"translit": "târ", "gloss": "tar", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON:2765; BQT:1550",
          "words": [
            {"translit": "qîr", "gloss": "tar", "script": "قیر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "English",
          "refs": "KLN:843",
          "words": [
            {"translit": "kerosene", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Kitintu", "redirect": "Kitu"},
      "nodes": []
    },
    {
      "root": {
        "name": "Kitu, Kitintu, Kitunnŭ",
        "lang": "Akkadian",
        "refs": "BQT:1594",
        "gloss": "cotton clothing"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "BQT:1594",
          "words": [
            {"translit": "qutun", "gloss": "cotton", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1594; MON:3543",
          "words": [
            {"translit": "katân", "gloss": "cotton", "script": "کتان"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "مرا اگر چه به بستر لَت کتان انداخت - ز روی صوف نظر بر نمیتوان انداخت",
            "poet": "Nezâm Qârî"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Spanish",
          "refs": "AHD",
          "words": [
            {"translit": "coton", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "coton", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:360",
          "words": [
            {"translit": "cotton", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:1664",
          "words": [
            {"translit": "kuttoneth", "gloss": "cotton clothing", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Aramaic",
          "refs": "KLN:1664",
          "words": [
            {"translit": "kittunâ", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Latin",
          "refs": "KLN:1664",
          "words": [
            {"translit": "ctunica, tunica", "gloss": "cotton clothing, tunic", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON:1154",
          "words": [
            {"translit": "tonekeh", "gloss": "underwear", "script": "تُنکه"}
          ],
          "script_extra": null,
          "note": "\"tonekeh\" is probably from \"tonok: thin, soft\". See root \"Ten 1\".",
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
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
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "tunic", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "VOP:154",
          "words": [
            {"translit": "tonîc", "gloss": "a piece of women clothing", "script": "تونیک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 7,
          "lang": "Greek",
          "refs": "KLN:1664",
          "words": [
            {"translit": "kiton", "gloss": "cotton shirt", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": "AHD:236",
          "words": [
            {"translit": "chiton", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Kitunnŭ", "redirect": "Kitu"},
      "nodes": []
    },
    {
      "root": {"name": "Klâu", "redirect": "Klěu 2"},
      "nodes": []
    }
  ]
}
```


## [2026-09-06T20:51:32.678Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AKD','KLN','AHD','MON','BQT','VFO','VOP','POK','WLD','FVQ','AFM','PLA','SKT','WEB','FSD','LKT','AFA','ARY','IEC','SYN']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-06T20:51:34.441Z] TOOL RESULT

```
AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verif
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
VFO null
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09:
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
```


## [2026-09-06T20:52:06.520Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -80 && echo \"=== matrix ===\" && sed -n 1,120p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T20:52:06.564Z] TOOL RESULT

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
=== matrix ===
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


## [2026-09-06T20:52:08.572Z] TOOL CALL #6: Bash

```json
{
 "command": "pdftoppm -f 268 -l 268 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg268 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T20:52:11.858Z] TOOL RESULT

```
total 1228
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 16:52 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    176 Sep  6 16:51 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb  25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb  23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb  10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb  11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb  10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb  19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb  19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb  12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb  12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb  12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb  14174 Sep  6 16:50 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb  14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb  25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb 105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb  84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb  92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82276 Sep  6 16:46 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb  69592 Sep  6 16:52 pg268.png
```


## [2026-09-06T20:52:15.576Z] TOOL CALL #7: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg268.png"
}
```


### [2026-09-06T20:52:15.914Z] TOOL RESULT

```

```


## [2026-09-06T20:52:15.912Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T20:52:35.760Z] AGENT

Extraction matches the printed page. Now the reference checks.


## [2026-09-06T20:52:39.254Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AKD grep kiru/qiru ===\"; grep -n -i -E 'k[iî]ru|q[iî]ru|qîr|Wachs' AKD.txt | head -40\necho \"=== AKD page 60 (offset?) ===\"; python3 - <<'EOF'\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['AKD'],ensure_ascii=False,indent=1))\nEOF"
}
```


## [2026-09-06T20:52:40.059Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN grease ===\"; grep -n -i 'grease' KLN_1966.txt | head -20\necho \"=== KLN kerosene ===\"; grep -n -i 'kerosene' KLN_1966.txt | head -20\necho \"=== KLN crassus ===\"; grep -n -i 'crassus' KLN_1966.txt | head -20"
}
```


### [2026-09-06T20:52:41.164Z] TOOL RESULT

```
=== AKD grep kiru/qiru ===
235:Das  im  Akk.  übliche  Wort  für  das  Anwachsen  der  Zinsen,  rabn, eig.  großwerden,  wachsen,  büdet  wohl  erst  den  Ausgangspunkt  fiii-  hebr. marhä  u.  tarhit  Zins,  aram.  rehhUft  (daraus  jüd.-deutsch  Bebhes  ?),  arab.  rihan.
692:4)  Falls  nicht  vielmehr  zu  akk.  kirubu  Stück  Land,  gehörig,  s.  oben  S.  40.
981:3)  Jedenfalls  zu  trennen  von  jüd.-aram.  qerd  Wachs  <;^  griech.  xTj^öq.
1114:wachsen,  sprossen  :  ^  wahrsch.  aram.  sdwah.
=== AKD page 60 (offset?) ===
{
 "title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)",
 "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/akkadischefremdw00zimmuoft",
 "identifier": "akkadischefremdw00zimmuoft",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt",
 "page_offset": "leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Organised by semantic field; Akkadian words in transliteration with Aramaic/Arabic/Persian loans. grep the word.",
 "notes": "39 citations; check that the 1st-ed. page is within a page or two of Nourai's."
}
```


### [2026-09-06T20:52:41.238Z] TOOL RESULT

```
=== KLN grease ===
1631:adipose,  adj.,  fatty.  —  ModL.  adiposus  (=  L.  adi- patus),  ‘filled  with  fat,  fatty’,  fr.  L.  adeps,  gen. adipis,  ‘fat  of  animals’,  fr.  Gk.  aXs^oc,  'un¬ guent,  oil,  fat’,  fr.  aXelcpsiv,  ‘to  anoint’.  The change  of  /  to  d  is  prob.  due  to  Umbrian  in¬ fluence.  Gk.  aXeLtpsiv  is  rel.  to  Gk.  Xirax;, ‘grease,  fat’,  Xutapoq,  ‘fat,  oily’,  and  is  cogn. with  L.  lippus,  ‘blear-eyed’,  OE.  be-Ufan,  ‘to  re¬ main’.  See  leave  v.,  and  cp.  words  there  referred to.  Cp.  also  synaloepha,  aliphatic.  For  the  ending see  adj.  suff.  -ose.  Derivative:  adipos-itv,  n. adiposis,  n.,  fatness  (med.)  —  A  Medical  L.  hy¬ brid  coined  fr.  L.  adeps,  gen.  adipis,  ‘fat’  (see adipose),  and  -osis,  a  suff.  of  Greek  origin, adipsia,  n.,  the  absence  of  thirst  (med.)  —  Medical L.,  fr.  Gk.  &8u[io;,  ‘not  suffering  from  thirst’, fr.  d-  (see  priv.  pref.  a-)  and  8('yx,  ‘thirst’,  which is  of  unknown  origin.  Cp.  dipsomania,  Dipso- saurus,  dipsosis.  For  the  ending  see  suff.  -ia. adit,  n.,  entrance.  —  L.  aditus,  ‘approach,  en¬ trance’,  fr.  adit-(um),  pp.  stem  of  adire,  ‘to  ap¬ proach’,  which  is  formed  fr.  ad-  and  ire,  ‘to  go’, fr.  I.-E.  base  *ei-,  •/-,  ‘to  go’,  whence  also  L. iter,  'a  journey.’  See  itinerate  and  cp.  aditus. Aditi,  n.,  the  endless  heaven,  mother  of  the  Adi- tyas  (Vedic  mythol.)  —  OI.  adilih ,  ‘boundless¬ ness,  infinity’.  See  Aditya  and  cp.  daitya. aditus,  n.,  an  entrance  (zool.,  anal.,  etc.)  —  L. aditus.  See  adit.
4175:axunge,  n.,  lard.  —  Earlier  F.  axunge  (F.  axonge), fr.  L.  axungia,  ‘axletree  grease,  grease,  fat’, which  is  compounded  of  axis,  ‘axletree,  axis’, and  ungere,  ‘to  grease’.  See  axis  and  unguent.
9567:crass,  adj.  —  L.  crassus,  ‘thick,  solid,  dense,  fat’, for  *qr(r-tos,  fr.  I.-E.  base  *qerat-,  'qert-,  ‘to  roll or  twist  together’,  whence  also  L.  erdtis,  ‘wicker¬ work,  hurdle’.  See  crate  and  cp.  words  there referred  to.  Cp.  also  Crassula,  cresset,  incras- sate.  Cp.  also  degras,  grease,  and  the  first  ele¬ ment  in  grampus.
9651:cress,  n„  plant  of  the  mustard  family.  —  ME. cresse,  fr.  OE.  cxrse,  cerse,  cresse,  rel.  to  MDu. kersse,  Du.  kers,  OHG.  kresso  (masc.),  cressa (fern),  MHG.,  G.  kresse,  ‘cress’,  and  cogn. with  Gk.  Ypaovn;,  ‘grass,  green  fodder’,  ypistv, ‘to  gnaw,  eat’,  OL  grasati,  ‘eats’.  Cp.  gastro-. Cress  orig.  meant  ‘the  edible  plant’.  See  Kluge- Mitzka,  EWDS.,  p.403  s.v.  Kresse.  F.  cresson and  It.  crescione,  ‘cress’,  are  Teut.  loan  words, cresset,  n.,  an  iron  vessel  for  holding  oil  or  grease. —  ME.,  fr.  OF. .  craisset,  fr.  craisse,  graisse.
9654:‘grease’,  fr.  VL,  *crassia,  fr.  L.  crassus,  ‘thick’. See  crass.
14432:Derivatives :  fastuous-ly,  adv.,  fastuous-ness,  n. fat,  adj.  —  ME.  fatt,  fat,  fr.  OE.  fatt,  contraction of f letted,  pp.  of fxttian,  ‘to  fatten’,  rel.  to  ON. feitr,  OFris.  fatt,  fet,  MLG.,  MDu.,  Du.  vet, OHG.  feijit,  MHG.  vei3(e)t,  G.  feist,  ‘fat’  (G. fell,  ‘fat’,  is  a  LG.  loan  word).  These  adjectives are  prop.  pps.  of  Teut.  *faitian,  ‘to  feed,  fatten’ (appearing  in  ON.  feita,  OHG.  fei^eri),  fr.  I.-E. base  *poid-,  *pld-,  ‘to  abound  in  water,  milk, fat,  etc.’,  whence  also  Gk.  irTSueiv,  ‘to  gush forth’,  nlSod;,  ‘spring,  fountain’,  7u8 faiq,,  ‘rich in  springs’.  Base  *poid-,  *ptd-,  is  a  -^-enlarge¬ ment  of  base  *poi-,  *pt-,  ‘sap,  juice ;  to  abound in  sap  or  juice,  etc.’,  whence  OI.  payate,  ‘swells, exuberates’,  payas-,  ‘water,  milk’,  Lith.  pienas, ‘milk’.  Cp.  OI.  pituh,  ‘juice,  sap,  resin,  drink’, pivan,  ‘fat,  fatty’,  ptvah  ‘fat,  grease’,  Gk.
16636:Derivative:  graze,  n.,  pasturage, graze,  tr.  v.,  to  touch  slightly.  —  Formed  from prec.  word  and  orig.  used  in  the  sense  ‘to  touch the  (grassy)  ground’  (said  of  bullets  that  touched the  ground  and  rebounded).  Cp.  G.  grasen,  ‘to feed  on  grass’  (fr.  Gras,  ‘grass’),  which  is  used also  in  the  above  mentioned  military  sense. Derivative:  graze,  n.,  a  slight  contact, grazier,  n.,  one  who  grazes  cattle.  —  Formed  fr, graze,  ‘to  feed’,  with  agential  suff.  -ier. grazioso,  adj.,  graceful  (musical  direction).  —  It., fr.  L.  grdtidsus.  See  gracious, grease,  n.  —  ME.  gresse,  grese,  fr.  OF.  gresse, graisse  (F.  graisse),  fr.  VL.  *  crass  ia,  ‘thickness, fatness',  fr.  L.  crasstts,  ‘thick,  fat’,  Cp.  Olt. grascia,  OProveny.  graissa,  Catal.  graxa.  Port, grai.xa ,  ‘fat’.  It.  grasce  (pi.),  ‘victuals’  [Sp.^raso, ‘fat’,  n.,  is  formed  fr.  graso,  ‘fat’,  adj.,  a  col¬ lateral  form  of  craso,  fr.  L.  crassus],  and  see crass.  Cp.  also  degras.
16637:Derivatives:  grease ,  tr.  v.,  greas-er,  n.,  greas-y, adj.,  greas-i-ly,  adv.,  greas-i-ness,  n. great,  adj.  —  ME.  great,  gret,  greet,  grete,  fr.
21357:leave,  tr.  and  intr.  v.  —  ME.  leven,  fr.  OE.  He  fan, ‘not  to  take  away,  to  leave,  bequeath’,  rel.  to OE.  Idf,  ‘what  remains,  remnant’,  OE.  belifan, OS.  biliban,  OHG.  biliban,  MHG.  beliben,  G. bleiben,  Goth,  bileiban,  ‘to  remain’,  and  prob. also  to  OE.  Ilf,  ‘life’,  libban,  lifian,  ‘to  live’,  orig. ‘to  remain’ ;  cogn.  with  Gk.  Xinoq,  ‘grease,  fat’, Xi-xpo;,  ‘oily,  fat,  greasy’,  XiTrocpr)?,  ‘persist¬ ing,  persevering’,  lit.  ‘sticky’,  Xlrrapeiv,  ‘to  per¬ sist,  persevere’,  lit.  ‘to  stick’,  OI.  limpdti, 'smears’, liptdh,  ‘sticking  together’,  lepah,  ‘unguent’,  L. lippus,  ‘blear-eyed’,  Lith.  limpit,  lipti,  ‘to  stick, adhere’,  OSlav.  pri-linqti,  of  s.m.,  lepu,  ‘bird¬ lime’,  Alb.  Vaparos,  ‘I  soil’,  gl’ep,  gel'epe,  sklepe, ‘mucus  secreted  by  the  glands  of  the  eyelid’,  and possibly  also  Hitt,  lippanzi,  ’they  smear,  paint’ (but  Gk.  Xet7toi,  L.  linquo,  ‘I  leave’,  are  not  cog¬ nate).  All  these  words  derive  fr.  I.-E.  base  *leip-, ‘to  anoint;  to  stick,  adhere;  to  remain,  perse¬ vere,  continue,  live’.  Cp.  life,  live,  liver  and  the second  element  in  Olaf.  Cp.  also  adipose,  Lipa- ris,  lipase,  lipo-,  ‘fat’,  lipoma,  the  first  element in  liparoid  and  the  second  element  in  celibate. Derivative:  leav-ing,  n.
21861:liparo-,  before  a  vowel  lipar-,  combining  form meaning  ‘oily’.  —  Gk.  Xutapo-,  XLTrap-,  fr. Xi7tap6;,  ‘oily,  fat,  greasy’,  fr.  /.ir.oc,  ‘fat, grease’.  See  lipo-,  ‘fat’.
21864:lipase,  n.,  a  class  of  enzymes  ( biochem .)  —  Form¬ ed  with  suff.  -ase  fr.  Gk.  Xlnoq  ‘fat,  grease’. See  lipo-,  ‘fat’.
21866:lipo-,  combining  form  meaning  ‘fat’,  as  in  lipo- lysis.  —  Gk.  Xttro-,  fr.  Xforo;,  ‘fat,  grease’, which  is  cogn.  with  L.  lippus,  ‘blear-eyed’,  OE, be-lifan,  ‘to  remain’.  See  leave,  v.,  and  cp.  Li¬ paris,  lipoma.
21873:lipoma,  n.,  a  fatty  tumor  ( med .)  —  Medical  L., coined  by  the  French  physician  Alexis  Littre (1658-1726),  fr.  Gk.  Xirro ;,  ‘fat,  grease’.  See lipo-,  ‘fat’,  and  -oma.
23314:M6doc,  n.,  a  kind  of  claret.  —  So  called  from Medoc,  name  of  the  plain  between  the  Gironde and  the  Atlantic,  where  it  is  produced, medulla,  n.,  the  marrow  of  bones  (anat.)  —  L., ‘marrow;  pith  of  plants’,  of  uncertain  etymolo¬ gy;  perh.  fr.  orig.  *(s)merulla  (with  -d-  for  -r-, under  the  influence  of  medius,  ‘middle),  fr. I.-E.  base  *smeru,  ‘fat’,  whence  also  OE.  smeoru, ‘fat,  grease’,  OIr.  smiur,  ‘marrow’,  W.  mer,  of s.m.  See  smear,  n.,  and  words  there  referred  to. Derivatives:  medull-ar,  adj.,  medullary  (q.v.), medullat-ed,  adj.,  medullation  (q.v.),  medull-iz- ation,  n.,  medullose  (q.v.) medullary,  adj.,  pertaining  to,  or  consisting  of, the  medulla.  —  L.  medullaris,  ‘situated  in  the marrow’,  fr.  medulla.  See  prec  word  and  adj. suff.  -ary.
33880:Derivatives:  say,  n.,  say-er,  n.,  say-ing,  n. say,  n.,  a  fine  cloth  resembling  serge.  —  ME.,  fr. OF.  (=  E.)  sale,  fr.  L.  saga,  pi.  of  sagum,  ‘a mantle  worn  by  the  ancient  Roman  soldiers’, the  pi.  saga  having  been  mistaken  in  VL.  for  a fern.  sing.  noun.  See  sagum. saynete,  n.,  tidbit;  a  short  play.  —  F.,  ‘playlet, sketch’,  fr.  Sp.  sainete,  ‘any  delicate  bit;  a  one- act  farce’,  derived  fr.  sain,  ‘grease’,  fr.  VL. *sagimen,  fr.  L.  sagninare,  ‘to  fatten’,  fr.  sagina, ‘a  fattening,  feeding;  stuffing’,  which  is  of  un¬ certain  origin.
34353:sebaceous,  adj.  —  L.  sebaceus,  fr.  sebum,  ‘tallow, suet,  grease’,  which  is  prob.  rel.  to  L.  sapo, ‘soap’.  See  soap,  and  cp.  suet.  For  the  ending see  suff.  -aceous.
34356:seborrhea,  seborrhoea,  n.,  discharge  of  sebaceous matter  (med.)  —  A  Medical  L.  hybrid  coined  fr. L.  sebum,  ‘tallow,  suet,  grease’,  and  Gk.  poia, ‘flow,  flux’,  fr.  psiv,  ‘to  flow’.  Sec  sebaceous  and rheo-.
35643:smatter,  intr.  v.,  to  talk  with  a  superficial  knowl¬ edge.  —  ME.  smateren,  ‘to  make  a  noise’,  of imitative  origin.  Cp.  Swed.  smattra ,  ‘to  crackle’. Derivatives:  smatter-er,  n.,  smatter-ing,  n.  and adj.,  smatter-ing-ly,  adv.,  smatter-y,  adj. smear,  n.  —  ME.  smere,  fr.  OE.  smeoru,  smeru, ‘fat,  grease’,  rel.  to  OS.,  OHG.  smero,  ON. smjor,  smdr,  Dan.  smer,  Swed.  smor,  MDu. smere,  Du.  smeer,  MHG.  smer,  G.  Schmer, ‘grease,  fat’,  Goth,  smairpr,  ‘fatness’,  fr.  I.-E. *smeru-,  ‘grease’,  whence  also  Gk.  piupov,  ‘un¬ guent,  balsam’,  ptupt^av,  opL'jpi^Etv,  ‘to  rub  with ointment’  (but  not  crpujpu;,  ‘emery’,  see  emery), Toch.  B.  $mare,  ‘smooth’,  OIr.  smi(u)r,  ‘mar¬ row’,  W.  mer,  of  s.m.,  and  perh.  also  Lith. smdrsas,  ‘fat’.  Cp.  Myristica,  Amyris,  and  the first  element  in  myrobalan,  Myroxylon.  Cp.  also medulla.
35644:Derivatives:  smear,  v.  (q.v.),  smear-y,  adj., smear-less,  adj.,  smear-i-ness,  n. smear,  tr.  v.  —  ME.  smeren,  fr.  OE.  smervan, smiervan,  rel.  to  ON.  smyrva,  smyrja,  Dan. smere,  Swed.  smorja,  Du.  smeren,  OHG.  smir- wen,  MHG.  smir(we)n,  G.  schmieren,  ‘to  smear’, and  to  OE.  smeoru,  smeru,  ‘fat,  grease’.  See smear,  n.
35693:Derivatives:  smuggl-er,  n.,  smuggl-ing,  n. smut,  n.,  1)  soot;  2)  smudge.  ■ —  LG.  smutt,  rel. to  MHG.  smuz,  ‘grease,  dirt’,  G.  Schmutz, ‘dirt’,  MHG.  smutzen,  G.  schmutzen,  ‘to  make dirty’,  ME.  smoten,  bi-smoteren,  of  s.m.  See mother,  ‘dregs’,  and  cp.  words  there  referred  to. Derivatives:  smut,  tr.  and  intr.  v.,  smutt-er,  n., smutt-y,  adj.,  smutt-i-ly,  adv.,  smutt-i-ness,  n. smutch,  n.  and  tr.  v.  —  See  smudge.
=== KLN kerosene ===
20627:—  Formed  with  subst.  suff.  -ite  fr.  Gk.  xr)p6?, ‘wax’.  See  cere,  n.,  and  cp.  kerosene.
20628:kermes,  n.,  the  bodies  of  the  females  of  an  insect found  on  the  kermes  oak.  —  F.  kermis,  fr. Arab,  qirmiz,  ult.  fr.  OI.  kfmi-dza-,  ‘produced by  a  worm’.  See  crimson  and  cp.  carmine, kermess,  kermis,  n.,  1)  an  annual  outdoor  fair in  the  Low  Countries;  2)  in  the  United  States, an  indoor  fair.  —  Du.  kermis,  ‘church-mass’, contraction  of  kerk  mes,  fr.  kerk,  ‘church’,  and mis,  ‘mass’.  See  church  and  Mass, kern,  kerne,  n.,  a  light-armed  foot  soldier  in  an¬ cient  Ireland.  —  Ir.  ceatharn,  ‘a  band  of  sol¬ diers,  a  soldier’.  Cp.  cateran. kernel,  n.  —  ME.,  fr.  OE.  cyrnel,  dimin.  of  corn. See  com,  ‘grain’,  and  dimin.  suff.  -el. Derivatives:  kernel,  tr.  v.,  kernel(l)-ed,  adj. kerosene,  n.,  an  illuminating  oil.  —  Formed  with suff.  -ene  fr.  Gk.  xr)p6 q,  ‘wax’.  See  cere,  n.,  and cp.  Kerite.
=== KLN crassus ===
9567:crass,  adj.  —  L.  crassus,  ‘thick,  solid,  dense,  fat’, for  *qr(r-tos,  fr.  I.-E.  base  *qerat-,  'qert-,  ‘to  roll or  twist  together’,  whence  also  L.  erdtis,  ‘wicker¬ work,  hurdle’.  See  crate  and  cp.  words  there referred  to.  Cp.  also  Crassula,  cresset,  incras- sate.  Cp.  also  degras,  grease,  and  the  first  ele¬ ment  in  grampus.
9568:Derivatives:  crass-ly,  adv.,  crass-ness,  n. crassitude,  n.,  grossness.  —  L.  crassitudo,  ‘thick¬ ness,  density,  fatness’,  fr.  crassus.  See  crass  and -tude.
9569:Crassula,  n.,  a  genus  of  herbs  ( bot .)  —  ModL., a  dimin.  noun  formed  fr.  L.  crassus,  ‘thick’.  See crass  and  -ule.
9576:crate,  n.  — -  L.  cratis,  ‘wickerwork,  hurdle’,  fr. I.-E.  base  *qerat-,  *qert-,  ‘to  roll  or  twist  to¬ gether’,  whence  also  L.  crassus,  ‘thick,  solid, dense,  fat’,  OI.  kptsnah,  ‘complete,  whole’, Russ. -Church  Slav,  cristvu,  cirstvu,  ‘firm,  solid genuine’,  Russ,  krutu,  ‘firm,  thick’,  OE.  hyrd, ‘door’  (orig.  ‘door  of  wickerwork’),  hyrdel, ‘hurdle’.  See  hurdle  and  cp.  cartilage,  crass, creel.  The  above  base  is  a  -/-enlargement of  base  *qer-,  ‘to  turn,  twist’,  whence  L.  curvus , ‘bent,  crooked’.  See  curve  and  cp.  words  there referred  to.
9654:‘grease’,  fr.  VL,  *crassia,  fr.  L.  crassus,  ‘thick’. See  crass.
10657:Derivatives:  degrad-ed,  adj.,  degrad-ed-ly,  adv., degrad-ed-ness,  n.,  degrad-ing,  adj.,  degrad-ing- ly,  adv.,  degrad-ing-ness,  n. degras,  n.,  fat  recovered  by  dressing  skins  with fish  oil.  —  F.,  formed  fr.  de-  (see  de-)  and  gras, fern,  grasse,  ‘fat’,  fr.  L.  crassus,  ‘thick’,  whence also  It.  grasso,  Rum.  gras,  OProven?.,  Catal. gras,  Sp.  graso.  Port,  graxo,  ‘fat’.  See  crass, degree,  n.  —  ME.  degre,  fr.  OF.  degret,  later degre  (F.  degre),  which  is  usually  derived  fr. Late  L.  *degradus,  lit.  ‘a  step  down’,  fr.  Late  L. degradare ,  ‘to  deposit  from  one’s  rank’,  in  VL. prob.  meaning  also  ‘to  descend’,  fr.  de-  and  L. gradus,  ‘degree’.  It  is  more  probable,  however, that  OF.  degret,  degre  was  formed  from  the prep,  de  (see  de-)  and  L.  gradus.  See  grade  and cp.  degrade.
16547:Gramophone,  n.,  trademark  used  for  a  type  of phonograph.  —  Coined  by  its  inventor  Emile Berliner(i85i-I929)  fr.  Gk.  ypapt(ia,  ‘something written’,  and  96)vfj,  ‘sound,  voice’.  See  -gram and  phone,  ‘speech  sound’,  and  cp.  phonograph, gram-positive,  adj.,  holding  the  purple  dye  when stained  by  Gram's  method;  saidesp.  of  bacteria. —  So  called  after  the  Danish  physician  Hans Christian  Joachim  (1853-1938). grampus,  n.,  a  cetacean  (Grampus  griseus).  —  Fr. earlier  graundepose,  altered — after  grand — fr.  ME.  graspeys,  grapeys,  fr.  OF.  craspeis, graspeis,  lit.  ‘fat  fish’,  fr.  L.  crassum  piscem,  acc. of  crassus  piscis.  See  crass  and  Pisces, granadilla,  n.,  the  fruit  of  certain  kinds  of  passion flower.  —  Sp.,  dimin.  of  granada,  ‘pomegra¬ nate’.  See  pomegranate.
16636:Derivative:  graze,  n.,  pasturage, graze,  tr.  v.,  to  touch  slightly.  —  Formed  from prec.  word  and  orig.  used  in  the  sense  ‘to  touch the  (grassy)  ground’  (said  of  bullets  that  touched the  ground  and  rebounded).  Cp.  G.  grasen,  ‘to feed  on  grass’  (fr.  Gras,  ‘grass’),  which  is  used also  in  the  above  mentioned  military  sense. Derivative:  graze,  n.,  a  slight  contact, grazier,  n.,  one  who  grazes  cattle.  —  Formed  fr, graze,  ‘to  feed’,  with  agential  suff.  -ier. grazioso,  adj.,  graceful  (musical  direction).  —  It., fr.  L.  grdtidsus.  See  gracious, grease,  n.  —  ME.  gresse,  grese,  fr.  OF.  gresse, graisse  (F.  graisse),  fr.  VL.  *  crass  ia,  ‘thickness, fatness',  fr.  L.  crasstts,  ‘thick,  fat’,  Cp.  Olt. grascia,  OProveny.  graissa,  Catal.  graxa.  Port, grai.xa ,  ‘fat’.  It.  grasce  (pi.),  ‘victuals’  [Sp.^raso, ‘fat’,  n.,  is  formed  fr.  graso,  ‘fat’,  adj.,  a  col¬ lateral  form  of  craso,  fr.  L.  crassus],  and  see crass.  Cp.  also  degras.
19098:Derivatives:  incorruptibil-ity,  n.,  incorruptible¬ ness,  n„  incorruptibl-y,  adv. incorruption,  n.  —  Late  L.  incorruptio,  gen.  -dnis, ‘incorruptibility’,  fr.  in-,  ‘not’,  and  L.  corruptio, gen.  -dnis,  ‘corruption’.  See  corruption, incrassate,  tr.  and  intr.  v.,  to  thicken.  —  L.  in- crassatus,  ‘made  thick’,  pp.  of  incrassare,  ‘to make  thick’,  fr.  in-,  ‘in’,  and  crassus,  ‘thick’. See  crass  and  verbal  suff.  -ate.
```


## [2026-09-06T20:52:54.647Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### AKD leaf 68 (printed p.60) ###\"\nawk 'BEGIN{RS=\"\\f\"} NR==69' AKD.txt | head -60\necho \"### context of line 981 ###\"\nsed -n '975,990p' AKD.txt"
}
```


## [2026-09-06T20:52:55.773Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN cotton ===\"; grep -n -i 'cotton,  n' KLN_1966.txt | head -5\necho \"=== KLN tunic ===\"; grep -n -iE 'tunic,  n|kuttoneth|kittun|chiton' KLN_1966.txt | head -20"
}
```


### [2026-09-06T20:52:56.834Z] TOOL RESULT

```
### AKD leaf 68 (printed p.60) ###
murrd, arab    murr  O  griech.  fiv^^a  usw.,  3iyrrlie)).\  [akk.  lardii  :  hebr.
ncrd,  aram.  nardd,  griech.  vöqSos  usw.,  Narde,  wohl  <]  ind.  ndlddd.] [akk.  ladunu  jedenfalls  Premdw.  :  griech.  XtjSov,  h'jSavoy,  Ladanum;  dazu viell.  hebr.  löf.  dem  vieU.  auch  im  Aklc.  luffti  entspricht.]  akk.  a))iru
eine    Spezerei,    vieU.    zu    :    äfiß^a   O    arab.    'anbar)    Ambra   (Liquid- ambar).  [akk.  budulhii  :  hebr.  hddölnli,  griech   ßSfKliov,  Bdellium.]
15.  Mineralien.
akk.   huräm   Gold    (wolil    von    St.  l/rs  gelb   sein)  :  >  hebr.  Mriis,
      59  
auch  pliön.  und  Klmw-Inschr.  /?r.s.  Aus  dem  Semit.  ^  griech.  x9*"^ög. [Zu  sum.  gitsqi  Gold,  gehört  viell.  armen.  osM  Gold,  finn.  vaski  Kupfer,  Erz.]
akk.  Icaspii,  st.  c.  Msap  Silber,  Geld  :  >  wohl  hebr.  Msep,  lasp-, aram.  laspd,  lespä.     S.  auch  schon  oben  S.  17  f.  akk.  sarpii  Silber
(eig.  das  geläuterte,  von  sumqm  läutern,  schmelzen) :  >  südarab.  .>■;•/'  Silber, wie  wohl  überhaupt  der  St.  ^rp  i.  d.  Bed.  (Metalle)  läutern,  schmelzen, löten  im  Hebr.  und  Aram.  O  im  Arab.),  s.  schon  oben  S.  27.  Desgleichen wohl  auch  syr.  sarrfipd,  arab.  mirfif  Geldwechsler,  jüd.-aram.  sarrep  Geld wechseln,  wie  viell.  auch  (mit  sekundärem  Lautübergang)  syr.  'arrcp  Geld wechseln  (nebst  Ableitungen).  ayr.  sinn  eine  Art  Silber  geht  zurück
auf  den  bab.  Mondgott  Sin,  dem  das  Silber  als  Metall  eignet.
akk.  eril,  älter  auch  warn,  urspr.  wohl  Kupfer,  dann  Bronze  (wohl ■<^  sum.  urtid);  damit  viell.  zus.  hängend  idg.  Wörter  wie  mittelpers.  röd, altind.  lohd-,  lat.  raiidus  Kupfer.  akk.  siparrii  Kupfer  :  >  viell.
hebr.  sej^er  an  einigen  Stelleu  (Jes.  30,  8;  Hi.  19,  23;  Ex.  17,  14);  ferner arab.  sifr,  sufr.
akk.  anaJiu  Zinn  (wohl  <^  sum.  *anag,  belegt  anna,  amma,  nagga, niggi)  :  hebr.  'annk,  syr.  'anJchä  O  wohl  arab.  'finuk),  äth.  na'sk.  Dazu jedenfalls  armen,  anag,  skr.  näga.     Unsicher,  wo  ursprünglich  heimisch.
akk.  jmrzillu  Eisen  :  daraus  zunächst  wohl  ]>  hebr.  barsei,  in  N. pr. harsill-,  aram.  parsel,  })arz9lä  O  arab.  firzil  Eisenfessel),  südarab.  frzn. Unsicher,  wo  ursprünglich  heimisch,  viell.,  worauf  auch  die  Endung  -ill weisen  könnte,  im  nordösü.  Kleinasien.  akk.  suhhi  Rost  :  ]>  wohl  syr.
suhtä,  mand.  sfitä.
akk.  abcirti  angeblich  Magnesit i,  aber  wohl  doch  besser  Blei  :  ]>- wohl  aram.  'äbärä,  'ahbärä  Blei  O  arab.  'abär).  Hebr.  'öpäret  Blei,  das sicher  auch  dazu  gehört,  steht  formell  etwas  abseits,  desgl.  armen,  kapar Blei.     Unsicher,  wo  das  Wort  ursprünglich  heimisch.
akk.  esniarfi  wahrsch.  Bez.  eines  Edelmetalls  :  dazu  vieU.  hebr. Ijasmal  bei  Ez.,  sowie  ägypt.  hsrnn,  beides  vieU.  Silbergold,  Elektrum.
akk.   siibil   ein   Edelste
### context of line 981 ###
alck.  naptu  Erdöl,  Naphtha  :  >  aram.  naptä,  neptä  O  arab.  naft, pers.  neft,  sowie  griech.  vätpfia^  usw.,  NapJdha).  akk.  etrdnu  wohl
Teer  od.  ä.  :  >  wohl  aram.,  trotz  des  ',  'atränä,  'etrcinä  Teer*  O,  mit auffälligem  q,  arab.  qaträn,  qitran).  akk.  wahrsch.  Jcuprrtu^  Schwefel,
dann  :  >  hebr.  goprtt,  aram.  guprlta,  kuhritä,  Jcebritä  O  arab.  kibrit).
akk.  uhtdu  eine  Alkalienart  :  ;>  syr.  'aJjla,  'vhlä  Lauge.  [akk.
1)  K.  996,  Rev.  10  ff.  (Harper  VI  570).  Es  ist  hier  anscheinend  vom  Erhitzen  des 6u?'a?ZM-Steines  die  Rede.  Daraus  darf  man  vielleicht  schließen,  daß  die  Babylonier  die eigenartige  Krystallhildung  des  Berylls  gekannt  und  verwertet  haben.
2)  Wörtl.  wohl  Schmiere,  von  kapärti  bestreichen,  beschmieren;  vgl.  dazu  unten  S.66.
3)  Jedenfalls  zu  trennen  von  jüd.-aram.  qerd  Wachs  <;^  griech.  xTj^öq.
4)  Die  Stelle  2  Maik.  1,  36  ist  natürlich  für  die  Etymologie  des  "Wortes  väip»a vollständig  belanglos.  5)  Wohl  ganz  zu  trennen  von  PI.  'etrSne  Räuoherwerk.
6)  Bab.  Exp.  Univ.  Penns.  XIV  Nr.  148,  52.  kupritu  könnte  einfach  WeiterbUdimg von  kupru  Erdpeoh,  sein.
      61      
nitiru  wohl   Natron,   nur  vereinzelt   zu   belogen,   wohl,   wie   liebr.  näter, arani.  nitro,  netrö,  griech.  vItqov,  Utqov  usw.,  Natron,  <C  ägypt.  ntrj.] akk.  si];l;ii  und  sHihttu  eine  Art  Alaun  :  >>  s^^r.  SekM}  [akk.  tß-
hat  Amanhn  wahrsch.  Amon-Salz  d.  i.  als  ä(x[^oiviax6v^  Sal  amnioniacum, urspr.  Steinsalz  aus  der  Libyschen  "Wüste,  also  wohl  in  Anleluiung  an  eine ägypt.  Bez.  entstanden.]
akk.  guhlu  Spießglanz,  Antimon,  Stibium  (als  Augenschminke)  : aram.  laMft  (^  spätliebr.  Mhal  die  Augen  schminken,  sowie  arab.  liuhl O  Alkohol),  äth.  hiehel).     Urspr.  Heimat  des  "Wortes  unsicher.  akk.
sadidu  wohl  aucli  Antimon ^  (als  Augenschminke)  :  >  aram.  sodnli'i. akk.  amämfi,  gleichfalls   ein  Schmink  mittel,  aber  viell.  pflanzlicher  Her- kunft.^    Davon  die  Bez.  der  Göttin  Istar  als  Amamitu  :  >  mand.  'Anin- mzt  als  Bez.  des  Planeten  Venus.
akk.  serser{r)i(,  rote  Paste  :  >  hebr.  säscr.  akk.  stjm  Paste  :
>  wohl  syr.  .iijjü  Paste,  sowie  sajäpä  Augensalbe  O  arab.  sijöf,  sowie armen,  vereinzelt  sup'ai),  wie  auch  das  i.  d.  Bed.  bestreichen,  einsalben,  wohl erst  denom.  Verbum  säp.
```


### [2026-09-06T20:52:56.897Z] TOOL RESULT

```
=== KLN cotton ===
9386:cotton,  n.  —  ME.  coton,  fr.  F.  coton,  fr.  Sp.  coton.
9389:cotton,  intr.  v.,  to  agree.  —  Fr.  cotton,  n.  The orig.  meaning  of  the  verb  was  ‘to  stick  together like  cotton' .
=== KLN tunic ===
7461:chit,  chitty,  n.,  a  short  letter.  —  Hind.  chif(hi,  fr. OI.  citrdh,  ‘bright,  marked,  spotted’.  See  cheetah, chit-chat,  n.  —  Reduplication  of  chat, chitin,  n.,  a  substance  forming  the  hard  covering of  insects  and  other  invertebrates  (biochem.)  — F.  chitine,  fr.  Gk.  yittov,  ‘undergarment,  coat  of mail,  any  coat  or  covering’.  See  chiton, chitinous,  adj.,  of  the  nature  of  chitin.  —  Formed fr.  chitin  with  suff.  -ous.
7462:chiton,  n.,  a  garment  worn  by  both  sexes  in  ancient Greece.  —  Gk.  yi-rciv,  Ion.  xiffcov,  borrowed — through  the  medium  of  the  Phoenicians — from the  Semites.  Cp.  Heb.  kuttSneth,  Aram,  kittand, Arab,  kattdn,  Akkad,  kitinnu,  ‘linen’,  Akkad. kitintu,  ‘linen  garment’.  Cp.  also  chitin,  tunic. Xirtov  occurs  in  Mycenaean  Greek  as  early  as the  15th  century.  See  Michael  Ventris  and  John Chadwick,  Documents  in  Mycenaean  Greek (Cambridge  University  Press),  Index,  s.v.  Semitic Loanwords.  Cp.  the  words  chrysalis,  cumin,  se- sam.
7611:the  15th  century.  See  Michael  Ventris  and  John Chadwick,  Documents  in  Mycenaean  Greek (Cambridge  University  Press),  Index,  s.v.  Se¬ mitic  Loanwords.  —  Cp.  the  words  chiton, cumin,  sesam.
9912:cumin,  also  cummin,  n.  —  ME.  cumin,  comin,  fr. OE.  cymen,  cymyn,  fr.  L.  cuminum,  fr.  Gk.  xu- (xtvov,  which  is  of  Semitic  origin.  Cp.  Heb. kammdn,  of  s.m.,  Aram,  kammond,  Syr.  kam- miind,  Ugar.  kmn,  Akkad,  kamunu,  Punic  yoty.av, ‘cumin’.  Cp.  also  cymene,  kilmmel.  —  Kuptvov entered  into  Mycenaean  Greek  as  early  as  the 15th  century.  See  Michael  Ventris  and  John Chadwick,  Documents  in  Mycenaean  Greek (CambridgeUniversity  Press),  Index,  s.v.  Semitic Loanwords.  Cp.  the  words  chiton,  chrysalis, sesam.
17808:himation,  n.,  Greek  garment  worn  over  the  chiton (Greek  antiq.)  —  Gk.  tpcmov,  for  slpdmov, fr.  ‘a  garment’,  which  stands  for  *fia-
34736:Derivatives:  servile-ly,  adv.,  servile-ness,  n., servil-ism,  n.,  servil-ity,  n. servitor,  n.,  servant.  —  ME.  servitour,  fr.  OF. servitour  (F.  serviteur),  fr.  Late  L.  servitorem, acc.  of  servitor,  ‘servant’,  fr.  L.  servire,  ‘to serve’.  See  serve  and  agential  suff.  -or. Derivatives :  servitor-ial,  adj.,  servitor-ship,  n. servitude,  n.,  bondage.  —  ME.,  fr.  OF.  ( —  F.) servitude,  fr.  L.  servitudd,  ‘slavery’,  fr.  servus, ‘slave’.  See  serve  and  -tude. sesame,  n.,  1)  an  East  Indian  plant,  whose  seeds yield  an  oil  and  are  used  as  food;  2)  its  seeds.  — F.  sesame,  fr.  L.  sesamum,  fr.  Gk.  arjoapiov, ‘seed  or  fruit  of  the  sesame  plant’,  crqa dtjarj,  ‘ses¬ ame  plant’,  fr.  Dor.  ai.aczp.ov,  which  is  a  Semit¬ ic  loan  word.  Cp.  Aram.  shumshlma,  ‘sesame’, Arab,  simsim,  Akkad,  shamashshamu,  of  s.m. Through  the  medium  of  the  Phoenicians  this Semitic  word  was  borrowed  by  the  Greeks  very early.  It  is  found  in  15th  cent.  Mycenaean Greek.  See  Michael  Ventris  and  John  Chad¬ wick,  Documents  in  Mycenaean  Greek  (Cam¬ bridge  University  Press),  Index,  s.v.  Semitic Loanwords.  Cp.  the  words  chiton,  chrysalis, cumin.
40452:tunic,  n.,  1)  a  shirtlike  garment  worn  by  men  and women  in  ancient  Greece  and  Rome ;  2)  a  blouse¬ like  garment;  3)  a  military  coat;  4)  a  tunicle.
40453:—  ME.  tunice ,  tunece,  fr.  F.  tunique,  (or  direct¬ ly)  fr.  L.  tunica,  which  stands  for  *ctunica  and was  borrowed,  prob.  through  the  medium  of  the Phoenicians,  fr.  Aram,  kittund,  fr.  Heb.  kutto- neth,  ‘tunic’,  whence  also  Gk.  yytcnv).  See  chiton and  cp.  tourniquet.  For  the  disappearance  of  the initial  k  cp.  ptisan.
```


## [2026-09-06T20:53:09.986Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9386,9390p' KLN_1966.txt\necho \"--- page marker probe near cotton ---\"\nawk 'NR>=9330 && NR<=9390 && /^[[:space:]]*[0-9]{3,4}[[:space:]]*$/ {print NR\": \"$0}' KLN_1966.txt\necho \"--- near kerosene ---\"\nawk 'NR>=20560 && NR<=20640 && /^[[:space:]]*[0-9]{3,4}[[:space:]]*$/ {print NR\": \"$0}' KLN_1966.txt\necho \"--- near tunic ---\"\nawk 'NR>=40400 && NR<=40460 && /^[[:space:]]*[0-9]{3,4}[[:space:]]*$/ {print NR\": \"$0}' KLN_1966.txt\necho \"--- near chiton ---\"\nawk 'NR>=7420 && NR<=7470 && /^[[:space:]]*[0-9]{3,4}[[:space:]]*$/ {print NR\": \"$0}' KLN_1966.txt"
}
```


## [2026-09-06T20:53:11.699Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins kerat/ker ===\"; grep -n -iE 'krat-|kerat-|crassus|wickerwork' AHD_watkins1985.txt | head -20\necho \"=== LEW crassus ===\"; grep -n -i 'crassus' LEW_1910.txt | head -10\necho \"=== LAT crassus/tunica ===\"; grep -n -iE 'crassus|tunica' LAT.txt | head -20"
}
```


### [2026-09-06T20:53:12.527Z] TOOL RESULT

```
cotton,  n.  —  ME.  coton,  fr.  F.  coton,  fr.  Sp.  coton.
fr.  Arab.  qu/un,  whence  also  It.  cotone,  OProv- en?.  coton.  Port,  cotao,  Du.  katoen,  and (through  the  medium  of  Dutch)  G.  Kattun,  ‘cot¬ ton’.  Cp.  acton,  kittel.
Derivatives;  cotton,  adj.,  cotton,  v.  (q.v.),  cot- ton-y,  adj.
cotton,  intr.  v.,  to  agree.  —  Fr.  cotton,  n.  The orig.  meaning  of  the  verb  was  ‘to  stick  together like  cotton' .
cotula,  n.,  an  ancient  Greek  measure  ( Greek  an- tiq.)  —  L.  cotula,  cotyla,  ‘a  small  vessel;  a measure  of  capacity’,  fr.  Gk.  xoruXr;.  See
--- page marker probe near cotton ---
9368: 360
9369: 361
--- near kerosene ---
20593: 842
20594: 843
--- near tunic ---
--- near chiton ---
```


### [2026-09-06T20:53:12.592Z] TOOL RESULT

```
=== AHD watkins kerat/ker ===
198:kagh-. To catch, seize; wickerwork, fence. pele-2. Flat; to spread. mu-', Imitative of inarticulate sounds.
532:[grat-. Also krat-. To scratch. Germanic root. 1. Ger- manic *krattén in Middle Dutch cratsen, to scrape: SCRATCH. 2. Germanic *grat- in Old French grater, to scrape: GRATE}; REGRATE. [Pok. gred- 405.]]
566:kae-id-. To strike. 1. Latin caedere, to cut, strike: CAE- SURA, CEMENT, CESTUS2, CHISEL, -CIDE, SCISSORS; AB- SCISE, CIRCUMCISE, CONCISE, DECIDE, EXCISE2, INCISE, PRECISE, RECISION. 2. Latin caelum (? < *caedum), sculptor’s chisel: CAELUM. [Pok. (s)k(h)ai- 917.] kagh-. To catch, seize; wickerwork, fence. 1. Germanic *hag- in: a. Old French hagard, wild, wild hawk (< “raptor”): HAGGARD; b. Germanic *hagén- in Old Eng- lish haga, hedge, hawthorn: HAW?; c. Germanic *hagj6é in Old English hecg, hedge: HEDGE. 2. Suffixed unaspirated form *kag-yon- in Gaulish caio, rampart, retaining wall (> Old French quai, quay): (CAY), KEY?, QUAY. 3. Possi- ble variant *kogh- in: a. Latin cohum, strap from yoke to harness: INCHOATE; b. possibly Latin cdlum, sieve (< wickerwork), and its derivative céldre, to filter: COLAN- DER, COULEE, (COULOIR), CULLIS; PERCOLATE. [Pok. kagh- 518.]
623:(SCARCE). 3. Greek karpos, fruit: -cARP, CARPEL, CARPO-, -CARPOUS. [In Pok. 4. sker- 938.] kers-'. Dark, dirty. 1. Suffixed form *ker(s)-no- in Rus- sian chérnyi (feminine chérnaya), black: CHERNOZEM. 2. Suffixed zero-grade form *krs-no- in Sanskrit krsna-), black, dark: KrisHNa. [Pok. kers- 583.] kers-2. To run. Zero-grade form *krs-. 1. Latin currere (past participle cursus), to run: CORRIDOR, (CORSAIR), COURANTE, COURIER, COURSE, CURRENT, CURSIVE, CUR- SOR, CURULE; CONCOURSE, CONCUR, DECURRENT, DIS- COURSE, EXCURSION, HUSSAR, INCUR, INTERCOURSE, OCCUR, PERCURRENT, PRECURSOR, RECOURSE, RECUR, succor. 2. Suffixed form *krs-o- in Gaulish carros, a wagon, cart, in: a. Latin carrus, a two-wheeled wagon: CAR, CAREER, CARGO, CARICATURE, CARIOLE, CAROCHE, (CARRY), CHARGE, CHARIOT; b. Latin carpentum, a two- wheeled carriage: CARPENTER. [Pok. 2. fers- 583.] kert-. To turn, entwine. I. Zero-grade form *krt-. 1. Suf- fixed form *krt-i- in Germanic *hurdiz, wickerwork frame, hurdle, in: a. Old English hyrdel, hurdle, frame: HURDLE; b. Old French hourd, fence, hurdle, scaffold: HOARDING. 2. Suffixed form “*krt-sti- in Germanic *hur- sti- in Old High German hurst, thicket: Horst. II. Per- haps suffixed variant form *krot-i- in Latin crdatis, wickerwork hurdle: CRATE, GRATE?, (GRID), GRIDDLE; (GRIDIRON). [Pok. kert- 584.] kes-'. To scratch. 1. Germanic *hezd6 in Old English heordan, coarse parts of flax: HARDS. 2. Extended form *kseu- in Greek xuein, to scrape: XYSTER. 3. Nasalized form *ks-n-eu- in: a. Germanic *snaww- in Old Norse snéggr, “close-cropped,” perhaps akin to the source of snuG!: b. Latin novdcula, razor: NOVACULITE. [Pok. kes- 585.] kes-2. To cut. Variant kas-. 1. Suffixed form *kas-tro- in: a. Latin castrare, to castrate: CASTRATE; b. Latin cas- trum, fortified place, camp (perhaps “separated place”): CASTLE. 2. Suffixed form *kas-to- in Latin castus, chaste, pure (< “cut off from, free of, faults”): CASTE, CHASTE; CASTIGATE, INCEST. 3. Suffixed (stative) form *kas-é- in Latin carére, “to be cut off from,” lack: CARET. 4. Ex- tended geminated form *kasso- in Latin cassus, empty, void: (CASHIER), QUASH. [Pok. hes- 586.] kes-°. To order. Suffixed 0-grade form *kos-mo- in Greek kosmos, order: COSMOS; MACROCOSM, MICROCOSM. keu-' Also ekeu-. To perceive, see, hear. O-grade form *akou-. 1. Extended form *kous- in: a. Germanic *haus- Jan in (i) Old English hieran, to hear: HEAR (ii) Old English he(o)rcnian, to harken: HEARKEN; b. suffixed form *9-kous-yo- in Greek akouein, to hear: ACOUSTIC. 2. Variant *skou- in: a. Germanic *skauwon in (i) Old English scéawian, to look at: SHOW (ii) Flemish scauwen, to look at: SCAVENGER; b. Germanic *skaunjaz in Mid- dle Dutch schoon, beautiful, bright (< “conspicuous, attractive”): SCONE; Cc. Germanic *skauniz in Old Eng- lish sciene, bright, sheen: SHEEN. [Pok. 1. keu- 587.] keu-?. Base of various loosely related derivatives with assumed basic meaning “to bend,” whence “a round or hollow object.” I. Extended forms *keub-, *keup-. 1. Ger- manic *haup- in: a. Old English héap, heap: HEAP; b. Dutch hoop, heap, troop: FORLORN HOPE. 2. Germanic *hupp-, to leap (by first bending the legs), in Old English hoppian, to hop: HoP!. 3. Germanic *Aupiz in Old Eng- lish hype, hip: H1P!. 4. Zero-grade form *kup-, vessel, in: a. suffixed form *kup-s- in Greek kupselé, chest, hollow vessel: CYPSELA; b. long-vowel form *kip- in (i) Ger- manic *Aifi- in Old English hyf, hive: HIVE (ii) suffixed form *kip-a in Latin cupa, tub, vat: CUPOLA, CUPULE; c. expressive form *kupp- in Late Latin cuppa, drinking vessel: cup. 5. Zero-grade form *kub- in: a. Greek kubos, cube: CUBE; b. suffixed form *kub-@- in (i) Latin cubdre, to lie down on (< “to bend down, prostrate”): COUVADE, COVEY, CUBICLE; CONCUBINE, INCUBATE, SUCCUBUS (ii) Latin cubitum, elbow: CUBIT; Cc. nasalized form *ku-m-b- in (i) Latin -cumbere, to lie down, recline: ACCUMBENT,
1085:LOUS, TERRIGENOUS, VERDITER. 3. Suffixed o-grade form *tors-eyo- in Latin torrére, to dry, parch, burn: TOAST!, TORRENT, TORRID. 4. Suffixed zero-grade form *trs-o- in Greek tarsos, frame of wickerwork (originally for drying cheese), hence a flat surface, sole of the foot, ankle: TaRSUS. [Pok. ters- 1078.]
=== LEW crassus ===
=== LAT crassus/tunica ===
1303:aclassls: tunica ab [h^umeris non consuta. P.F.18,31. Pas d'autre
6992:bassus, -a, -um (Gloss.): crassus, non altus. M.L.978; britt. bas.
12326:s^nateurs ou des chevaliers"; Varr., L.L. 9, 4,7, tunicam ita consuere
14291:crassus
14329:crassus, -a, -um: gros, epais (3ens physique et aoral), gras; s'op-
14331:Panroaan. M.L.2999. Crassus, appuye sur grossus d'aprbs lequel il a
14335:Crassus est eaploye coaae surnoa, aais non pinguis. Les 1 . roaanes
21122:cf. Plin..19,19, regum inde funebres tunicae corporis fauillam ab reliquo
26967:grlcenea: funis crassus, P.F.88,8. Sans autre exenple, et sans
29774:exter-nus, etc.); 1 'autre, tardif et rare, interulus:-a tunica. A
32521:l&ti-clauuius,-a,-um adj.derive de latus clauus: -a tunica, et subst.
33324:lerla (e?): ornamenta tunicarum aurea, P.F.io«,a3. Sans doute grec;
37729:Diogenem postea pallium solum habuisse, et habere Ulixem meram tunicam.
45614:patagium, -In.: — est quod ad summam tunicam adsui solet, quae
46052:pihten-, celt. gall. pei thyn-, et pais de pexa ( scii, tunica) : robe;
47599:concurrencd par crassus que soutenait grossus, pinguis n f a -subsisti
52620:dico (230): tunicam rallam, tunicam spissam, Non.530,15. Cf.Isid.,995
60170:on d' 4 cailles, cf.Vg;, Ae. 10,314 per tunicam squalentem auro', G.4,
60459:On trouve aussi dans les gloses stica ( strica, stiga, stigia ): tunica,
61777:tunicae genere notum est omnibus, F.403,95« I*a glose de Festus semble
```


## [2026-09-06T20:53:21.787Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- KLN page markers around tunic (40452) ---\"\nawk 'NR>=40350 && NR<=40460 && /^[[:space:]]*1[0-9]{3}[[:space:]]*$/ {print NR\": \"$0}' KLN_1966.txt\necho \"--- around chiton (7462) ---\"\nawk 'NR>=7380 && NR<=7470 && /^[[:space:]]*[0-9]{3}[[:space:]]*$/ {print NR\": \"$0}' KLN_1966.txt\necho \"--- LAT crassus ---\"; sed -n '14326,14340p' LAT.txt\necho \"--- LAT tunica ---\"; sed -n '61770,61790p' LAT.txt"
}
```


## [2026-09-06T20:53:23.762Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT cotton/tunic/chiton/grease ===\"; grep -n -iE '^.{0,40}(cotton|tunic|grease)\\b' SKT.txt | head -20\necho \"=== LKT Baumwolle qutn ===\"; grep -n -iE 'qutn|kutun|Baumwolle|kattan|qatran|qir' LKT.txt | head -30"
}
```


### [2026-09-06T20:53:24.029Z] TOOL RESULT

```
--- KLN page markers around tunic (40452) ---
40369: 1661
40398: 1662
--- around chiton (7462) ---
7408: 276
7409: 277
--- LAT crassus ---
sieurs langues (cf. heri), il n 1 en subsiste pour "deaain" aucun qui se
trouve dans deux langues. Skr. (,:vah "deaain" est isol£ tout coaae lat.
cras, qui doit neanaoins etre ancien.
crassus, -a, -um: gros, epais (3ens physique et aoral), gras; s'op-
pose k tenuis, k liquidus, k macer. - Ancien, usuel et classique.
Panroaan. M.L.2999. Crassus, appuye sur grossus d'aprbs lequel il a
tendu k devenir grassus (cf. Thes. IV 1103,52, Martyrius dans GLK VII
176,14 et M.L. s.u. et 4427 *ingrassiare) a eu une vie plus active
que pinguis, qui n'est guere repr^sente en dehors du doaaine italien.
Crassus est eaploye coaae surnoa, aais non pinguis. Les 1 . roaanes
attestent aussi *crassia, M.L.2298.
Derives: crassitudo, ancien et frequent; crassitas, crassities, crds-
sedo forae coaae pinguedo, sont de 1'epoque iap^riale; crasso, -ds
(epoq. iap.), et crassesco, -is, crassamen et Crassamentum: depot, lie;cratera - 364 -
crassundia, -orun: gros intestin (cf. crepundia ); crassiuus , 7 KX)(U vou £
--- LAT tunica ---
chaine", cf. subtemen qui d 4 signe les fils les plus fins delatra-
me, v.Rich, s.u.telo. M.L.8399 et 8398 subtiliare (attest 4 dans les
gloses: attenuat, suptiliat , CGL V 437 , 34 )«
subtus: v.sub.
subQcula: ▼. exu 5 .
subQcula, -ae f.: -* Aelius Stilo et Cloatius isdem fere uerbis
demonstrant uocari quod dis detur ex alica et oleo et meile; nam de
tunicae genere notum est omnibus, F.403,95« I*a glose de Festus semble
r 4 unir deux mots diff 4 rents. Sur subucula (cf.ex-, ind-uo ) "vStement
de dessous", v.M.L.8361 *subicula.
sabula, -ae f,: alfene; par analogie "petit 4 pieu", d*oii subulo,
-Snis m. "daguet". Attest 4 seulement depuis S 4 nbquej aais sans doute
ancien. M.L.8403,8404. De *su-dhl-S, Y.sud. Pour la formation, cf.
fibula et palpebrae, palpetrae, pSbulum; subella, M.L.8356. Compos 4 s:
insubulum (ayec u?) "ensouple" (isid.), M.L.4474, insubuld, - 5 s.
subulcus: y. sOs.
subulo, -onis m.: joueur de flute. Mot 4 trusque d'apros Varr.,
L.L.7,35 et F.403,3. D 4 jA dans Enn. Cf .sibilus.
succSnseo: v. censeo.
succrotllla: — tenuis diceba<tur et alta uox>« litinius in (771)
...<feninina> fabulare succro<tilla uocula. Afra^nius in Bpistol<a
```


### [2026-09-06T20:53:25.811Z] TOOL RESULT

```
=== SKT cotton/tunic/chiton/grease ===
2034:BomboAt,  ong.  cotton>«radding; padding,  affeclea  language.   (h>l  ■'^'
2036:Lev  L.  fvmf'ast  cotton  ; «  Gk.  0A^$v(,   silk. Item  I    iiom    Pen.
4174:Cotton  (0»  »  downy  substance.  (F. — Spnn,  — Arab.)  M.  £.  <otoun.^Y.  cofam. —  Span,  cotottt  aigtniffn,  cotton  \ where  ai  is the  Arab.  art.). —  Arab.  i/u/h,  ^uiun,  cotton, cudwreed,  a pUnt.  ^F.— Span.— Arab. ; anj  E.)  Also  called  iotton-.otid,  of  which cuii-weeJ  is  a  contraction.
4175:Cotton  (a),  lo  agree.  From  a  technical u&c  of  Cotton  1 1 ; ;  sre  Nares.
4468:Cudweed  ;  see  Cotton  (i ).
7598:Qingham,  a  kind  of  cotton  cloth.  (F. ) Modem.  —  F.  guingan  ;  corruption  of GuiHgamfi\  the  name  of  ft  place  in  Brit- tany where  such  fabrics  were  made.
20293:Tunic.  (L.)  A.S.  /KH/or  — L.  tunica, an  under-garment.  Dot.  tmmC'U,  tunic- at'€d.
=== LKT Baumwolle qutn ===
327:[Kelekian  Kämos  31]  'gestreifte)',  bunter BaumwoUstofi'  [auch  ins  Ar.  überge- gangen, vgl.  SBKAW  Wien  CHI,  189:  'ge- streifter Stoff  aus  Baumwolle  u.  Seide']; hieraus  rum.  alagea  'feiner  gedruckter Kattun'.
520:Npr.  Ein  Urenkel  von  UMAIJJA,  dem Stammvater  der  Umaijjadendynastie, gab  einem  Stadtviertel  Bagdads  den Namen,  also  al-'aifäbija.  In  diesem Viertel  wurden  die  bunten  StolTe  aus Seide  und  Baumwolle  hergestellt,  die nach  dem  Ursprungsorte  einfach  'Attäbl- Stoffe  genannt  wurden.  Hieraus  mit W eglassung  des  ar.  Art.  it.  sp.  pg.  tabi, frz.  tabis  [wozu  das  Vb.  tabiser  'wäs-
571:'Gürtel  od.  Frauenmantel  ohne  Ärmel'; hieraus  pg.  bedeni  'maurischer  Mantel, Regenmantel  aus  Leder,  Spartgras  oder Binsen  [Constancio  Dicc  167  b]  und  siz. piddemia  'Frauenmantel  aus  Leinen  od. Baumwolle'  [in  scherzendem  Tone  od. vei-ächtlichem  Sinne  gebraucht].  [GrS- VociSic  243.
1767:'Art  Stoff'  [Pijn  195b,  vollständig  käin ginggmxg  'gestreiftes  Baumwollenzeug', wohl  ursprünglich  javanesisch  'ver- bleichend, vergänglich'];  hieraus  anglo- ind.  engl,  gingham  'Baumwollstoff  aus gefärbtem  Garn,  gestreift,  kariert  oder in  anderen  Mustern',  familiär  auch 'Sonnenschirm',  ndl.  gingam,  gingang, dtsch.  Bchwed.  dän.  gingang,  dtsch.  Ging- gang, Ginghati ;  frz.  guinyan,  guinganip, sp.  gingen,  pg.  giiingäo,  it.  guingano, ghingano.  —  [Französische  Etymologen führen  den  Namen  auf  die  trz.  Stadt Guingamp  [Dep.  Cötes  du  Nord]  zurück, wo  tatsächlich  Textilindustrie  betrieben wird.]   [JAOS  XVII,  142/144.
1798:737.  Ar.  gubba: 'Baumwollenes  Unterkleid'  [Dozy  V6tem i07ff.\;  hieraus  mit  verschiedenartiger Bedeutungsentwicklung :  it.  giuppa  (alt), giubba  'Jacke,  Wams',  frz.  jupe,  jupon 'Frauenrock,  Unterrock',  demin.  it.  giu- betto,  gitibetta,  augm.  it.  giuppone,  siz. jippuni;  prov.  jubo,  kat.  gipö,  sp.jubön, pg.  jubäo,  gibäo,  rum.  giubca  'langes Oberkleid  der  Bauern',  ^ubea,  sp.  aljuba,
2038:beherrschten.  Aus  dem  tk.  Grundwort entstand:  russ.  Kitai  'China',  kitaika 'BaumwüUstofif,  Nanking  [s.  hier  Nr. 1554]',  poln.  kitaj  'chin.  I3aumwollen- zeug  oder  Glanzleinwand',  kitajha  'Taf- fet',  klruss.  kytaj,  kytajka  'Taflet,  Seiden- zeug', bulg.  kitajka  'Nanking',  serb. Kitaj  'China',  citajka  'baumwollener Stoff';  rum.  chitaiü  'Wollfutter'.  [Hob- son  Jobson  274.   Bern  SlEtWb  505/506.
2534:1067.  Mal.  käpok: 'Baumwollkattun'  [Fijn  171;  aus  dem Jav.] ;  hieraus  frz.  capoc,  der  Baum  capo- qiiier;  dtsch.  Kap>ock  'eine  Art  seiden- artiger Baumwolle'  aus  Ostindien,  die man  nicht  spinnt,  sondern  nach  Art der  Watte  verwendet.    [Devic  DEt  82.
2973:1272.  4r.  kutnn: 'Baumwolle',  vulg.  koton  [selbst  Fremd- wort, wohl  äg.  oder  ind.  ZDMG  L,  633; vgl.  hebr.  kuttöne^,  woraus  gr.  x'^div; hieraus  wahrscheinlich  dtsch.  Kittel]; hieraus  it.  cotone,  sp.  algodön,  pg.  algo- däo,  frz.  coton  'Baumwolle';  pg.  cotäo 'Panzerhemd  mit  großen  Maschen',  prov. alcoto  'Wams,  das  die  Ritter  unter  der Rüstung  trugen  und  das  innen  mit  Kattun gefüttert  war',  afrz.  auqueton,  nfrz.  ho- queton  'gestepptes  Wams  aus  BaumwoU- zeug';  mndl.  acotoen  'dass.',  ndl.  katoen, dtsch.  Kattun,  Katun  'Baumwollstoff, engl,  cotfon;  poln.  katun,  cech.  kartoun. —  Aus  dem  ar.  Adj.  kutiini  'baumwollen' wurde  tk.  ktdny  'Halbzeug  von  Satin und  Baumwolle'  [Kelekian  Kämüs  965  b] ; hieraus  russ.  kutnja  'asiatisches  halb- seidenes Zeug'.  [DE  127.  Eguilaz  162. ML  6910.  Lammens  Rem  264.  Bern SlEtWb  653.    MWiD  94.
3128:1345.  Ar.  inadrasa: 'Hochschule'  [vom  Vb.  darasa  'studieren' mit  Präfix  ma-  des  Ortes],  als  N.  pr. Name  der  Stadt  Madras  an  der  mittleren Ostküste  Vorderindiens.  Hieraus  die Bezeichnung  für  einen  dort  verfertigten hellen  Stoff  mit  seidenen  Quer-  und baumwollenen  Längsfäden:  engl,  (ver- altet) madras,  frz.  madras  'halbseidenes Zeug'.    (Hobson-Jobson  .532/534.
3195:'Stoff  aus  feiner,  weißer  Baumwolle', der  Musseline  ähnlich;  hieraus  engl. muhmil  und  durch  Verkürzung  auf  eine Silbe  engl.  muH,  dtsch.  Mull.
3425:Klassische  Form:  Mausil  [Suffix  »na-des Ortes  und  Vb.  wasala  'vereinigen',  also eigentlich:  'Ort,  wo  etwas  vereinigt  wird', nämlich  Vereinigungsstelle  der  Wege  aus dem  oberen  Mesopotamien  und  dem 'Irak],  früher  Fabrikort  eines  feinen, weißen  baumwollenen  Gewebes  [den  die Araber  heute  säs  nennen,  s.  WETZ- STEIN in  ZUMG  XXII,  161].  Hieraus it  mussolo,  mussolina  'Nesseltuch',  frz. mousseline,  sp.  muselina,  pg.  musselina, murselina,  rum.  muselina ;  dtsch.  Mus- seline, ndl.  mousselien,  engl,  muslin; bulg.  muselina,  serb.  muselin,  öech. muselin,  poln.  muslin.  Heutzutage  gibt es  sowohl  Woll-  wie  Ba  um  wo II- musseline.  [DE  325.  Eguilaz  491.  ML 5700.    Hobson-Jobson  600/601.
3578:N.  pr.,  große  Stadt  am  Unterlauf  des Jang-tse-kjang,  wörtlich  'südlicher  Hof, d.  h.  Hauptstadt  des  Südens  [wie  Peking 'Hauptstadt  des  Nordens'];  nach  dieser Stadt  wurde  ein  baumwollener  Stoff  von bräunlich-gelber  Farbe  mit  meist  ka- riertem Muster  benannt,  da  er  hier  ur- sprünglich ausgeführt  wurde  Engl. 7iankin,narikeen,  disch.  Nanking,  Nankin, ndl.  nanking;  frz.  nankin;  poln.  serb. nankin,  6e  'h.  nankyn,  aber  russ.  nanka 'chines.  Leinwand'.  [Hobson  Jobson  6 16. Hirth  ChinFW  209.
3701:1617.  Pers.  piiiibä: 'Baumwolle',  hieraus  tk.  pembe  'dass., rosafarben';  hieraus  rum.  pambria 'Schafwolle',  jmnbeii  'blaßrot'.  Aus  der pers.  Form  pänbäk  ergaben  sich  tk. pambuk  'Baumwolle'  und  gr.  udiußaE, ■iraiißdKiov  'dass.';  hieraus  rum.  bumbac, buig.  bubak,  serb.  panmk  'Baumwolle', FUSS,  bumaga,  klruss.  buniaha,  bamaha 'Papier'  sowie  mlat.  bambaqium,  it.  bam- bagin  'Baumwolle';  aus  lat.  bombacium wurde  frz.  bombasin,  engl,  bombasine, bombazine;  dtsch.  Bombasin,  russ.  bu- mazeja  'Art  Barchent'.  [Bern  SIEtWb 100/lül.
3730:'Paradies'  ['Wonnegarten'  aus  altpers. pairidaeza  'Umzäunung,  Garten'],  gr. irapdbeiooq,  lat.  paradisum;  hieraus  frz. paradis,  sp.  paraiso,  it.  paradiso,  rum. paradis;  engl,  paradise,  dtsch.  Paradies. Lautgesetzlich  entwickelt  mit  volks- etymologischer Umgestaltung  trz.  parvis 'Vorhof  der  Kirche'.  Nfrz.  paradis  war bei  den  Mysterien bühnen  im  Gegensatz zur  im  Vordergrunde  gelegenen  Hölle ein  Platz  auf  einer  Anhöhe  des  Hinter- grundes, jetzt  der  oberste  Teil  des  Zu- schauerraums auf  der  Galerie  [sonst  frz. poulailler;  vgl.  dtsch.  'Himmelreich, engl,  up  among  the  Gods].  Vgl.  Otto Driesen,  Der  Ursprung  des  Harlekin. Berlin  1904.  (Forschungen  zur  neueren Literaturgeschichte,  herausgegeben  von Muncker.  XXV.)  S.  83, 163iJ.  Fers,  pärgal: 'Leichtes  Linnen  oder  Kleidungsstück daraus';  hieraus  sp.  percal  [Dicc  Gast 1531  c]  'Baumwollstoff',  weiß  oder  bunt, mehr  oder  weniger  fein,  percalina  'ein- farbiges percal',  frz.  percal,  perkal,  per- caline  'weifses  Baumwollenzeug';  dtsch. Perkal.
4219:'Behälter,  bes.  Scheide  für  den  Kris; Art  Rock'  [Pijn  127  ;  vielleicht  aus  sskr. särana];  hieraus  engl,  sarong,  dtsch. Sarong  'ein  langer  Rock,  gewöhnlich von  buntem  Seidenstoff  oder  Baumwolle', das  Hauptbekleidungsstück  der  Malayen und  Javanesen,  ndl.  saroeng.  [Hobson- Jobson  796.
4318:'Matratze ;  langes,  breites,  mit  Baumwolle gefüttertes  Polster,  auf  dem  man  bequem sitzen  kann'  [Kelekian  Kämüs  732b]; hieraus  rum.  saltea  'dass.'.
4790:gandin  'eine  Art  Mull ;  ein  glattes,  feines Baumwollengewebe  dichter  als  Musselin'. [Mfi  9082.  Karabacek,  Über  einige  Be- nennungen mittelalterlicher  Gewebe. I.  Wien  1882.  S.  21/22.
5463:kutun(t)  Tt"l
```


## [2026-09-06T20:53:41.891Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON files ===\"; ls -la MON_part*.txt; grep -c '' MON_part1.txt MON_part2.txt\necho \"=== page tags? ===\"; grep -n -m5 -E '\\[pdf page' MON_part1.txt\necho \"=== قیر ===\"; grep -n 'قیر' MON_part2.txt | head -10\necho \"=== کتان ===\"; grep -n 'کتان' MON_part1.txt MON_part2.txt | head -10\necho \"=== تنکه ===\"; grep -n 'تنکه' MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-06T20:53:42.032Z] TOOL RESULT

```
=== MON files ===
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
MON_part2.txt:94500
MON_part1.txt:99339
=== page tags? ===
=== قیر ===
1273:غرق چشمةٌ قیر: (کد.) فرو رفته در آب. 
3042:برخلاف فقیر که ذات و کمال او به دیگری 
6975:سفله. خوار» دلیل حقیر. بی‌هنر» بی‌دانش. 
8000:در حقیقت حق است و فقیر خلق و آن 
10111:قار؛ ۲ (ع.] (.) قیر» زفت. دودة مرکب» 
11161:قیرستان: 0 ی > + .| (امر.) جابی 
13531:(کد.) شین قلیل» چیزی کوچکد. نقیر و 
13534:قیره هر نقیرعادل یل هر یل معدل ۳ 
14869:اطوار از طرف با تحقیر و توهین یاد کنند 
14878:لحن 7 تحقیر). وقتی کسی زیاده از حد یا 
=== کتان ===
MON_part2.txt:4190:تفاوت بین دو امر. (.) ( گیا.) کتان. 
MON_part2.txt:8548:آنفن افکتان: ( کد.)سقرار گردانندن کسی 
MON_part2.txt:11253:(ص‌نسه.) مونث قبطی. ثیاب قبطیه: کتان 
MON_part2.txt:12871:پارچة ظریف که از کتان تنک نرم یا حسریر 
MON_part2.txt:12894:پارچه‌ای از قسمی کتان. 
MON_part2.txt:14549:از کرباس و کتان و غیره که بر آن به وسیلة 
MON_part2.txt:17770:مکتان) ]ردان جنک نگ : بجم ی 
MON_part2.txt:20644:کتانشر وشی اطلاق می‌شد ولی فرهنگستان 
MON_part2.txt:20693:کتان فرهنگک فارسی معین 
MON_part2.txt:20701:کتان: «قاها ,«قاها [ع.) (.) (گیا.) گیاهی 
=== تنکه ===
MON_part1.txt:19587:(جف.) تنکه میان دو خشکی. تمام» به تمام) 
MON_part1.txt:28179:فوق و تحت و میان هر دو تنکهٌ افقی بکار 
MON_part1.txt:44296:تنکه: (۵-)۱0۱۵۲۸ (.) تنان چرمی که تا سر 
MON_part1.txt:44301:تنکه: (۵-)0۲۵ه) [آهنن سشبد] (.) قر ص 
MON_part1.txt:44615:تنکه. شلوار کو تاه کشت یگیران.
```


## [2026-09-06T20:53:42.121Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/ref_page.py BQT:1594 2>&1 | head -60"
}
```


### [2026-09-06T20:53:44.674Z] TOOL RESULT

```
REF: BQT:1594  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 387  OCR-lang: fas

کنابه -۱۹-
کتابه - بکسر اول و قح بای ابید . | وسکون نون » نوعی از جامه باشد که آنرا از
این لفت راصاح موْبدالفتلا در سلك‌لغات‌فارسی | اطف سازند . طبیعمت آن سرد واخشك است
نوشته است ۱ بمعنی خطی که‌آبرا بقلم جلی در | و پوشیدش آشف رطوبت وعرق از بدن میکند.
روی کاغذ با پارچهٌ پاريك نوشته‌باشند . کوبند اگر کی خواهد که بدن او لاغر شود
کتاده ۴ - بفتح اول بر وزن هزاره . | در زمستان جامة کتان نو پوشد ودر تابستانجامة
خذف ها مشهور است . بعنی در زم‌تان جامة کنان شته پ ی
۳ رم تابستان‌نو؛ وبی‌تشدید هم‌درست است - ودانه‌ای را
کتاله ۴ « بالام . بروزن وممنی کتاره یز کوبند که از آن روغن چراغ کیردد ؛
ِ 2 اهل هند باشد.
است (۱) که حربة حل هند باشد و ی کوبند باین معنی بکر اول باشد و بی
کنام ۴ « بنتح اول و سکون میم . دید .۹
بمعنی تالار باشد وآن عمارتی است که از چوب کنخ بفتح اول وثالی وسکون خای
وتخته سازند . قطه‌دار » بمعنم کشك باش د که دوغ خعك شده
کتان * « بنتح اول و تشدید نالی | است واترکان قروت میگوبند ‎٩‏ ؛ و باینمعنی
(۱) چش: - است.
۹ - عربی است . رك : اقرب‌الموارد » قطرالمحبط . ۲ < کاله (هم. )از
ساسکریت ۴۵1۳8۲8 ۶ دکترراجا » ۰ قس : اردو 812۳8ا, 8218۳1 :
« و هندوان بسیستان آمدند و از آنجا بغزنین » من که بوالفضلم با امیر بخدمت رفته
بودم پباغ صدهزاره , مقدمان این هندوان را دیدم که آنجا آمده بودند و آمیر فرموده بود تا
اسان را درخانة بز رکه کهآ نجا دبوان رسالت دارند بنشانده بودلك وبوسفید مشرف پیغامهای‌درشت
میآورد سوی آیشان از مین وکار بدانجا رسی د که پیغامی آمد که شما را جواب فرموده آید ۰
شش‌تن مقدهتشر آشان‌خوبشتن ر بکتاره زدند چنانکه خون درآن‌خانه روان شد... این‌خبر بامفر
رسانیدند گفت این کتاره بکرمان باست زد .» ( تاریخ بیپقی چاپ دکتر فیاض 2۳۲-۶۳۱ *.
۴ -رك : کتاره . ۴ - کیلکی 61۵۲, ۳۸۱۵۵ هی
اطافکی که ازچوب و حصیر در مزارع و جالیز سازند وجایگاه نگهیان زد
مزرعه و جالیز باشد . 8 - (عر ) « کنان بالفتح و شدالتاء ۰ ار ۹
لبانی است بقدر ذرعی و ساق و برکش باريك و کلش لاجوردی است و ۹۸ 1
پوست وبرا همجون پنبه رسند . » « منتهی الارب » این کلمه در زبان رت ۱
اکدیبسورت ۴1۸۵ . 19101۷ و880ااذظ آمده بمعنی (جامکتانی) 2/76
ودر زبان عربی و دیگر زبانهای سامی نیز بدین معنی آمده. کلمةٌ کدی بر
درسر بانی صورت ۳۴02 ودرحبشی صورت 340 داخل‌شده بمعنی : ۱
پیراهن با جامه‌ای ا زکتان, وکلمه از سربانی وارد عربی شده ۶ معجمیات
عربیه- سامیه ۰۱۸۹ ‎٩‏ <کنعغ (ه.م.) ر4 :کنخ شیر. قس : کنان
فَتقءتر کی « رشیدی > * قالق, ترکی « فرهنگه نظام > .
۲ کایون - رد : کنابون .
(برهات قاطع ۳۰۴(
```


## [2026-09-06T20:53:57.419Z] TOOL CALL #18: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1594 --image 2>&1 | tail -5; ls data/verification/sources/refs/ocr/BQT/ 2>/dev/null | head"
}
```


### [2026-09-06T20:53:59.149Z] TOOL RESULT

```
عربیه- سامیه ۰۱۸۹ ‎٩‏ <کنعغ (ه.م.) ر4 :کنخ شیر. قس : کنان
فَتقءتر کی « رشیدی > * قالق, ترکی « فرهنگه نظام > .
۲ کایون - رد : کنابون .
(برهات قاطع ۳۰۴(

0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1219.png
1219.txt
1219.vision.txt
1223.png
1223.txt
```


## [2026-09-06T20:54:04.033Z] TOOL CALL #19: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/BQT/1594* && python3 -c \"\nfrom PIL import Image\nim=Image.open('data/verification/sources/refs/ocr/BQT/1594.png')\nprint(im.size)\nw,h=im.size\nim.crop((0,int(h*0.55),w,int(h*0.95))).resize((int(w*1.3),int(h*0.40*1.3))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1594_foot.png')\n\""
}
```


### [2026-09-06T20:54:06.917Z] TOOL RESULT

```
data/verification/sources/refs/ocr/BQT/1594.png
data/verification/sources/refs/ocr/BQT/1594.txt
(1650, 2546)
```


## [2026-09-06T20:54:09.245Z] TOOL CALL #20: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1594_foot.png"
}
```


### [2026-09-06T20:54:09.668Z] TOOL RESULT

```

```


## [2026-09-06T20:54:09.666Z] INPUT

[Image: original 2145x1323, displayed at 2000x1234. Multiply coordinates by 1.07 to map to original image.]


## [2026-09-06T20:54:33.964Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BQT\ncat > data/verification/sources/refs/ocr/BQT/1594.vision.txt <<'EOF'\n[read from image data/verification/sources/refs/ocr/BQT/1594.png = Borhan-e Qate' ed. Mo'in, p. 1594, s.v. کتان]\n\nHeadword (main text): کتان * ـ بفتح اول و تشدید تاء ... (5)\n\nMo'in's footnote 5 (verbatim):\n۵ ـ (عر.) «کتان بالفتح و شدّ التاء ، نباتی است بقدر ذرعی و ساق و برگش باریک و گلش\nلاجوردی است و پوست و برا همچون پنبه رسند.» «منتهی الارب». این کلمه در زبان اکدی\nبصورت kitû , kitintu , kitunnû آمده بمعنی (جامهٔ کتانی) و در زبان عربی و دیگر زبانهای\nسامی نیز بدین معنی آمده. کلمهٔ اکدی در سریانی بصورت kûtînâ و در حبشی بصورت kattân\nداخل‌شده بمعنی: پیراهن یا جامه‌ای از کتان، و کلمه از سریانی وارد عربی شده «معجمیات\nعربیه ـ سامیه ص۱۸۶».\n\nOther footnotes on the page: ۴ ـ کیلکی katâm, kutâm ; ۶ ـ کنغ ...\nPage footer: (برهان قاطع ۳۰۴)\nEOF\necho saved\npython3 tools/ref_page.py BQT:1550 2>&1 | head -50"
}
```


### [2026-09-06T20:54:36.500Z] TOOL RESULT

```
saved
REF: BQT:1550  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 343  OCR-lang: fas

بیان نو دهم
در قاف بایای حطی مشتمل بر بیست وشش لغت و کنایت
قیامت کر دن - کنابه از کارهای | که برشتران کرکین مالند » و صمفی هم هست
عجیب کردن وکارهای عجایب انگیختن باشد . سیاه و چسبنده که برکشتی وجهاز مالند تا آب
قیاو ار ۱ - با واو بر وزن سزاوار, | بدرون کشتی نرود - وسیاه را نی زگویند چه هر
بمعنی‌کار وشفل وعمل وصنعت باشد. چزساه را باو نسبت کنند .
قیدافه ۰ بفتح اول وسکون نانی ودال فیرس ْ - بفنح اول و کسرثالك‌وسکون
بی‌نقطه بالف کشیده وفای مفتوح, نام زنی است | تحتانی واسین بی‌نقطه » لفتی است بونانی بمعلی
که حاکم بردع و اندلی بود ۲ , وبردع‌ملکی موم که بعربی شمع کوبند .
است که استرخوب راهوار ازآنجا آورند.و اتثر قیردان ۹ بروزن شیروان » اطراف
بردعی مشهور است. . مجموعةٌ عالم راگوبند - ونام شهری هم هست‌در
قید - بفتح اول "و سکون ثالی و دال مغفرب ۷ - و مشرق و مغرب را نیز گوبند -
بی‌نقطه بواوکشیده » نام پادشاه مغلان‌است؟ .۰ | وبممنی کاروان هم‌آمده است.
قیر ۴ « بروزن هیر » روغنی پاشد سیاه قیروتی « بر وزن مخروطی » بلغفت
۹ مصحف « فیاوار » (ه.م.) .۴ -قیدافه طبق روایات مِلکهٌ اندلی ومعاصراسکندر بود:
زنی بود در الدلی شهربار خردمند و با لشکری بیشمار
جهانجوی وبخشنده قیدافه نام ز روز بهی بافته نام وکام .
« فردوسی . شاهنامةٌ بخ اج ۷ص ۲۱۸۶۸
و رك : مجمل‌التواریخ والقصص ص۵۷. رشیدی گوید : « قیدافه نام: نوشابه ملکهٌ بردع اما معرب
«کیدپا» ست.» و«نوشابه» ملک بردع ومعاصر اسکندر بود «شرفنامهٌ نظامی چاپ ارمغان ص۷۷۷
ببعد > و بردع قصبه‌ای در آران بوده ( رك : بردع و رك : ممج‌البلدان : برذعة ) - نیز قیدافه
نام شهری بود « فپرست ولف » . ۴ - قیدوخان پادشاه حدود جبال « تارباگاتای » نبدره
اوکتای» معاصرقوبیلای قاآن. رك: اقبال آشتیانی . تاریخ مقول اس ۱۹۲ ۰ ۲۰۷ ۰ ۰۷۶۱
۰ - ازیونانی ۴۵۲۵8 (شمع) » اهل مغرب شمع را قیر نامند . وقیر نوعی‌از101110106
است که‌بشکل قطران بکار رود, قار» زفت « دزی اج ۷ص*۸۳: ۲ « عقار۸ ۱۳ ۳6010 (1)
« فهرست ولف > . رك : قیری . 8 ره : حاشیهٌ قبل .
- باقوت گوید : * قیروان ( بفتح اول وضم سوم وفتح چهارم ) ازهری کوبد قبروان
معرب است وآن بفارمی «کاروان > است وعرب ازقدیم بدان تکلم کرده است. امروالقیس گوید:
وغارة ذات قیروان کان اسرایها الرعال .
وقیروان شهری بز رک بافربقاست.» «ممجم‌البلدان» وآن در جنوب تونی واقع است. رك:فپرست
نخبة‌الدهر . ورك: ح۷- درعربی قیروان (بفتح اول وسوم) بمعنی عمده يك‌کاروان با يك‌سپاه و نیز
بمعنی شهر عمدء مرکز ساخلو آمده « دزی ج ۲ اص 4۳۱ > ۷ -۳۵[۲0۷20(فر)
شهری سونی » دارای ۲۰۶۶۹ سکنه که درسال ۱۸۸۱ تصرف فرانسوبان درآمد ۰
```


## [2026-09-06T20:54:52.206Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### MON کتان (part2:20701) ###\"; sed -n '20698,20712p' MON_part2.txt\necho \"### MON تنکه (part1:44296) ###\"; sed -n '44290,44305p' MON_part1.txt\necho \"### MON قیر ###\"; grep -n '^قیر' MON_part2.txt | head; grep -n 'قیر:' MON_part2.txt | head"
}
```


### [2026-09-06T20:54:52.317Z] TOOL RESULT

```
### MON کتان (part2:20701) ###
سازند و آن جایگاه نگهبان مزرعه و جالیز 
است. 

کتان: «قاها ,«قاها [ع.) (.) (گیا.) گیاهی 
است از تبرهٌ کتانیان که یکی از تیره‌های 
نزدیک به سدابیان است. برخی از گونه‌های 
این گیاه بصورت درختچه نیز درمیآیند. 
برگ‌هایش متناوب و کامل و باریک و به 
شکتتسا س نیز ه است. گل‌هایش دارای 
تقسیمات ۵ تایی و زرد یا آبی سفید است. 
گل کتان صبح زود شکفته می‌گردد و 
بعداز ظهر مجددا بسته می‌شود. گل آذینش 
ری فد منهج کییرلن 
است و حامل ده دانٌ بیضی شکل صات 
قهوه‌بی رنگ می‌باشد. ساقةٌ کتان دارای 
### MON تنکه (part1:44296) ###
تسنکر: ۵۲ (ع.] (مسص‌ل.) ناشناس 
نودن» خود را ناشناس نشان دادن ناشناس 
شدن. از حالی به حالت زشت و اخوش در 
آمدن» دگر‌گون گشتن. (امص.) ناشناختگی؛ 
ج. تتکرات. 

تنکه: (۵-)۱0۱۵۲۸ (.) تنان چرمی که تا سر 
زانو باشد و کشتی‌گیران وقت کشتی گرفتن 
بوشند. شلوار کو تاه زنانه. زیر شلواری کو تاه 
مر دانه. 

تنکه: (۵-)0۲۵ه) [آهنن سشبد] (.) قر ص 
رایج از زر و سیم و مس. 

تنکیر: ۲ (ع.] (مص‌م.) مجهول کر دن» 
ناشناس ساختن. (دس.) نکره ساختن اسم؛ ج. 
### MON قیر ###
11161:قیرستان: 0 ی > + .| (امر.) جابی 
13534:قیره هر نقیرعادل یل هر یل معدل ۳ 
16434:قیر اسفهسلار: 01)(2۲عاناه- [تر. ف. 
16435:قیر در ترکی به معنی سرحد و ثغر است] 
16438:قیراط: ۱ [معر.] (بز. قد.) واحد وزن و 
16449:قیر گود: 7۰-۵ [معر . ف.] (ص‌مر. امر.) به 
16451:قیروطی: 1701:[- قیروتی؛ معر یو. قس. 
85116:قیر از میان آتش بگذرد» اگر آسیبی 
1273:غرق چشمةٌ قیر: (کد.) فرو رفته در آب. 
16433:(مثل) قیر: بسیار سیاه.
```


## [2026-09-06T20:54:54.005Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM (Addi Shir) قير / كتان ===\"; grep -n -E 'قير|كتان|قیر' AFM_pages.txt | head -20\necho \"=== AFA Fraenkel kittan/qir ===\"; grep -n -iE 'kattan|kittan|qir|qatran|Wachs' AFA.txt | head -25"
}
```


### [2026-09-06T20:54:54.070Z] TOOL RESULT

```
=== AFM (Addi Shir) قير / كتان ===
1195:(الجهرمية ) شاب من نحو السط ܚܨ من اتكتان منسوبة الى جهرم دهي
1510:مشاقة اتكتان
1809:0 ( ܕ ܝܡܝ ) الرجل التافه اي اللقير ينطق في امر العامة وهو غير اهل
1866:ܟ ܨ ) ¥ 3 مغرت ܐܘܐ عن رت اي العريان ام عن رت أي الفقير
1918:, 7 ( قير بالرجل يقال انه « رَوْس سو » اي رجل سو وهو معرب عن
2099:+ 1 القصير وزوتكل ® القصير ا-لقير النّة 399 وزو نلك
2130:90 ܒ 9 ܝܨ المقيرة تعريب ?< وهو
2683:02 ( )ܐܥܝܥܪ ) قير بالنوع ܝ تعر يب سيد وجعناه وهر التصنّع والرياء
2798:أطلق على كل من يديع أي جنس كان من العطر والعقاقير 07
3410:2210001 (621351112) وهى صرب م ܡ أب الكتانة ٠‏ وقا آل ܚ £
3468:لضيقة اللقيرة وتطلق ايضاً على الشتاء وعلى عش الطائر
=== AFA Fraenkel kittan/qir ===
5591:denen Reben wachsen'*. Die Schilderung betrifft aber Je-
6213:die in Sümpfen wachsende Kasia (ib. 110); gefahrvoll war
6699:Ableitung hat ') gewiss erst aus aram. p7 —ä] erwachsen,
7741:ßciv «B ^^i? PSm. 952 erwachsen.
```


## [2026-09-06T20:55:13.939Z] TOOL CALL #24: Bash

```json
{
 "command": "sed -n 1,40p tools/fetch_source.py"
}
```


### [2026-09-06T20:55:13.978Z] TOOL RESULT

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


## [2026-09-06T20:55:18.864Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/κηρός\" \\\n \"https://en.wiktionary.org/wiki/crassus\" \\\n \"https://www.etymonline.com/word/grease\" \\\n \"https://www.etymonline.com/word/kerosene\" \\\n \"https://en.wiktionary.org/wiki/قیر\" \\\n \"https://en.wiktionary.org/wiki/كتان\" \\\n \"https://en.wiktionary.org/wiki/قطن\" \\\n \"https://www.etymonline.com/word/cotton\" \\\n \"https://en.wiktionary.org/wiki/χιτών\" \\\n \"https://en.wiktionary.org/wiki/tunica\" \\\n \"https://www.etymonline.com/word/tunic\" \\\n \"https://en.wiktionary.org/wiki/כתונת\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 268 verification (Kiru / Kitu)\" 2>&1 | tail -1\ndone"
}
```


### [2026-09-06T20:55:27.225Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3b63a13618a8b307.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f6b9dddee77ffe96.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9eba46bd1a4ca493.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2468ada3ba792bec.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/50f4380074e64b6a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bcb589fb5536be7a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/978e59f8b3bbd7d9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/344ca7425ed31dfd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f3932c4f2a79a206.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4994d5a26ddab510.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c222490f2f48553f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6cbdfd5b2f4d7357.txt
```


## [2026-09-06T20:55:31.489Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=========== κηρός ===========\"; grep -n -A6 -i 'Etymology' 3b63a13618a8b307.txt | head -40\necho \"=========== crassus ===========\"; grep -n -A8 -i 'Etymology' f6b9dddee77ffe96.txt | head -40"
}
```


### [2026-09-06T20:55:31.555Z] TOOL RESULT

```
=========== κηρός ===========
65: Etymology 1 
66-
67- 1.2.1 
68- Noun 
69-
70- 1.2.1.1 
71- Declension 
--
80: Etymology 2 
81-
82- 1.3.1 
83- Noun 
84-
85- 1.4 
86- Further reading 
--
180: Etymology 1
181- [ edit ] 
182-
183- A foreign loan from a substrate language, cognate with Latin cēra and Albanian qiri , [ 1 ] and possibly also with Lithuanian korys , Latvian kāre . [ 2 ] 
184-
185- Noun
186- [ edit ] 
--
278: Etymology 2
279- [ edit ] 
280-
281- Noun
282- [ edit ] 
283-
284- κηρός • ( kērós ) 
=========== crassus ===========
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Adjective 
72-
73- 1.4.1 
--
172: Etymology
173- [ edit ] 
174-
175- Uncertain; suggested to be from Proto-Indo-European *kert- ( “ to wind ” ) , [ 1 ] and compared to crātis ( “ wickerwork ” ) , however this is semantically doubtful. Possibly connected to grossus ( “ coarse; thick ” ) , also of unknown origin. [ 2 ] 
176-
177- Pronunciation
178- [ edit ] 
179-
180- ( Classical Latin ) IPA ( key ) : [ˈkras.sʊs]
```


## [2026-09-06T20:55:39.710Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=========== grease ===========\"; sed -n '1,80p' 9eba46bd1a4ca493.txt | grep -n -i -m1 -A20 'grease(n' ; grep -n -i -m2 -A10 'Old French cras' 9eba46bd1a4ca493.txt\necho \"=========== kerosene ===========\"; grep -n -i -A10 'kerosene' 2468ada3ba792bec.txt | head -30\necho \"=========== cotton ===========\"; grep -n -i -A12 'cotton (n' 344ca7425ed31dfd.txt | head -30\necho \"=========== tunic ===========\"; grep -n -i -A12 'tunic (n' c222490f2f48553f.txt | head -30"
}
```


### [2026-09-06T20:55:39.859Z] TOOL RESULT

```
=========== grease ===========
=========== kerosene ===========
1:URL: https://www.etymonline.com/word/kerosene
2-FETCHED: 2026-09-06T20:55:22Z
3-STATUS: 200
4:TITLE: Kerosene - Etymology, Origin & Meaning
5-
6:Kerosene - Etymology, Origin & Meaning 
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
--
21: Origin and history of kerosene 
22-
23: kerosene (n.) 
24-
25- "mixture of liquid hydrocarbons used as an illuminating or heating fluid," 1852, from Greek kēros "wax" (see cere ) + chemical suffix -ene . Coined irregularly by Canadian geologist Abraham Gesner (1797-1864), who discovered how to distill it c. 1846. So called because it contains paraffin (hence the British English name, paraffin oil ).
26- also from 1852 
27-
28: Entries linking to kerosene 
29-
30- cere (n.) 
31-
32- "wax," late 15c., from French cire "wax" (12c.), from Latin cera "wax, wax seal, wax writing tablet," related to Greek kēros "beeswax," which is of unknown origin, perhaps a non-IE word. As a verb, "to wax, cover with wax" (cloth, for waterproofing), late 14c., from Latin cerare , from cera . Related: Cered .
33-
=========== cotton ===========
23: cotton (n.) 
24-
25- late 13c., "white fibrous substance containing the seeds of the cotton plant," from Old French coton (12c.), ultimately (via Proven ç al, Italian, or Old Spanish) from Arabic qutn , a word perhaps of Egyptian origin. Also ultimately from the Arabic word are Dutch katoen , German Kattun , Proven ç al coton , Italian cotone , Spanish algodon , Portuguese algodo .
26-
27- As "cloth made of cotton," from early 15c. The meaning "the cotton plant" is from c. 1400. As an adjective, "made of cotton," from 1550s. Cotton gin is recorded from 1794 (see gin (n.2)). Philip Miller of the Chelsea Physic Garden sent the first cotton seeds to American colony of Georgia in 1732.
28- also from late 13c. 
29-
30- cotton (v.) 
31-
32: 1560s, "to prosper, succeed;" of things, "to agree, suit, fit," a word of uncertain origin. Perhaps from Welsh cytuno "consent, agree;" but perhaps rather a metaphor from cloth-finishing and thus from cotton (n.). Hensleigh Wedgwood compares cot "a fleece of wool matted together." Meaning "become closely or intimately associated (with)," is from 1805 via the sense of "to get along together" (of persons), attested from c. 1600. Related: Cottoned ; cottoning .
33- also from 1560s 
34-
35- Entries linking to cotton 
36-
37- gin (n.2) 
38-
39- "machine for separating cotton from seeds," 1796, American English, used earlier of other machineries, especially of war or torture, from Middle English gin "ingenious device, contrivance" (c. 1200), from Old French gin "machine, device, scheme," shortened form of engin (see engine ). The verb in this sense is recorded from 1789. Related: Ginned ; ginning . Middle English had ginful "ingenious, crafty; guileful, treacherous" (c. 1300).
40-
41- cottonmouth (n.) 
42-
43: "venomous serpent of the U.S. South," 1849, so called for the white streak along its mouth; see cotton (n.) + mouth (n.).
44-
45- cottonocracy 
46- cotton-tail 
47- cottonwood 
48- See All Related Words (5) 
49-
50- Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
51-
52- More to explore
=========== tunic ===========
23: tunic (n.) 
24-
25- mid-12c., tunice , "ancient garment like a shirt or short gown, often worn as an undergarment," from Old French tunique (12c.) or directly from Latin tunica "undergarment worn by either sex" (source of Spanish tunica , Italian tonica , Old High German tunihha ), probably from a Semitic source (compare Hebrew kuttoneth "coat," Aramaic kittuna ). Compare chitin , from a Greek name for a similar garment, also probably from a Semitic source.
26-
27- The borrowing from Old French replaced Old English tunece , directly from Latin. In antiquity worn by either sex. In reference to modern costume from 1660s, extended as a general term to all garments worn depending from the neck; especially as a women's garment from mid-18c. A fine, thin, or delicate example is a tunicle .
28- also from mid-12c. 
29-
30- Entries linking to tunic 
31-
32- chitin (n.) 
33-
34- "organic substance forming the wing cases of beetles and other insects," 1836, from French chitine , from Latinized form of Greek khiton "frock, tunic, garment without sleeves worn directly on the body;" in reference to soldiers, "coat of mail," used metaphorically for "any coat or covering." "Probably an Oriental word" [Liddell & Scott]; Klein compares Hebrew (Semitic) kuttoneth "coat," Aramaic kittana , Arabic kattan "linen;" Beekes compares Phoenician ktn "linen garment." Related: Chitinous .
35-
36: supertunic (n.) 
37-
38- also super-tunic , "any garment worn over a tunic," 1620s, from super- + tunic .
39-
40- tunicate (adj.) 
41-
42- "coated or covered with integuments" (in zoology); having or enclosed in a tunic," 1760, from Latin tunicatus "clothed with a tunic only (i.e. without a toga), in shirt-sleeves," past-participle adjective from tunicare "to clothe in a tunic," from tunica (see tunic ). As a noun from 1848.
43-
44- Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
45-
46- More to explore
47-
48- kirtle
```


## [2026-09-06T20:55:48.977Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=========== grease ===========\"; sed -n '20,40p' 9eba46bd1a4ca493.txt\necho \"=========== wikt قیر ===========\"; grep -n -i -B2 -A8 'Etymology' 50f4380074e64b6a.txt | sed -n '1,80p'"
}
```


### [2026-09-06T20:55:49.039Z] TOOL RESULT

```
=========== grease ===========

 Origin and history of grease 

 grease (n.) 

 "oily fat of land animals," c. 1300, from Anglo-French grece , Old French gresse , craisse "grease, fat" (Modern French graisse ), from Vulgar Latin *crassia "(melted) animal fat, grease," from Latin crassus "thick, solid, fat" (source also of Spanish grasa , Italian grassa ), which is of unknown origin. Grease paint , used by actors, attested from 1880. Grease monkey "mechanic" is from 1918.
 also from c. 1300 

 grease (v.) 

 mid-14c., "smear, lubricate, or anoint with grease or fat," from grease (n.). Sense of "ply with bribe or protection money" is 1520s, from notion of grease the wheels "make things run smoothly" (mid-15c.). To grease (someone's) palm is from 1580s. Expression greased lightning , representing something that goes very fast, is American English, by 1832.
 also from mid-14c. 

 Entries linking to grease 

 degrease (v.) 

 also de-grease , "remove the grease from," 1855; see de- + grease . Related: Degreased; degreaser; degreasing .

 foie-gras (n.) 

=========== wikt قیر ===========
60-
61- 1.1 
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.3 
68- Adjective 
69-
70- 1.3.1 
--
148-
149- قیر 
150: Etymology
151- [ edit ] 
152-
153- Inherited from Proto-Turkic *kïr ( “ isolated mountain; steppe, wilderness ” ) .
154-
155- cognates
156-
157- Cognate with Azerbaijani qır , Bashkir ҡыр ( qır ) , Chuvash хир ( hir ) , Kazakh қыр ( qır ) , Kyrgyz кыр ( kır ) , Turkmen gyr , Uyghur قىر ( qir ) and Uzbek qir .
158-
```


## [2026-09-06T20:55:53.339Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"--- sections in قیر ---\"; grep -n -E '^ (Persian|Arabic|Uyghur|Ottoman|Urdu)' 50f4380074e64b6a.txt | head -20\ngrep -n -A12 'Persian' 50f4380074e64b6a.txt | sed -n '1,60p'"
}
```


### [2026-09-06T20:55:53.401Z] TOOL RESULT

```
--- sections in قیر ---
57: Ottoman Turkish 
146: Ottoman Turkish
228: Ottoman Turkish terms derived from Proto-Turkic 
229: Ottoman Turkish lemmas 
230: Ottoman Turkish nouns 
231: Ottoman Turkish adjectives
```


## [2026-09-06T20:55:58.398Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/قار\" \\\n \"https://en.wiktionary.org/wiki/qir\" \\\n \"https://en.wiktionary.org/wiki/kittānu\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/kittān-\" \\\n \"https://www.etymonline.com/word/tar\" \\\n \"https://en.wiktionary.org/wiki/tunique\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 268 verification (Kiru qir / Kitu kattan)\" 2>&1 | tail -1\ndone"
}
```


## [2026-09-06T20:56:00.137Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=========== wikt كتان ===========\"; grep -n -A10 'Etymology' bcb589fb5536be7a.txt | sed -n '30,110p'\necho \"=========== wikt قطن ===========\"; grep -n -A10 'Etymology' 978e59f8b3bbd7d9.txt | sed -n '30,120p'"
}
```


### [2026-09-06T20:56:03.755Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5b03215525b378ed.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/10bb1258713ac76b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1c3933edd8f8c7cb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dab9849a37e522e2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5495373f155d0978.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5f2145c208c61e21.txt
```


### [2026-09-06T20:56:03.810Z] TOOL RESULT

```
=========== wikt كتان ===========
105- Noun 
106-
107- 4 
108- Hijazi Arabic 
109-
--
113: Etymology 
114-
115- 4.2 
116- Pronunciation 
117-
118- 4.3 
119- Noun 
120-
121- 5 
122- Moroccan Arabic 
123-
--
127: Etymology 
128-
129- 5.2 
130- Pronunciation 
131-
132- 5.3 
133- Noun 
134-
135- 6 
136- Ottoman Turkish 
137-
--
144: Etymology 
145-
146- 6.3 
147- Noun 
148-
149- 6.3.1 
150- Declension 
151-
152- 6.4 
153- Adjective 
154-
--
232: Etymology
233- [ edit ] 
234-
235- Inherited from Arabic كَتَّان ( kattān ) .
236-
237- Noun
238- [ edit ] 
239-
240- كتان ( kettānn )  m 
241-
242- flax 
--
253: Etymology
254- [ edit ] 
255-
256- Borrowed from Classical Syriac ܟܶܬܳܢܳܐ ( kettānā , “ flax; linen ” ) .
257-
258- Pronunciation
259- [ edit ] 
260-
261- IPA ( key ) : /kat.taːn/ 
262-
263- Noun
--
372: Etymology
373- [ edit ] 
374-
375- Inherited from Arabic كَتَّان ( kattān ) .
376-
377- Pronunciation
378- [ edit ] 
379-
380- IPA ( key ) : /kit.taːn/ , [kɪt.tæːn] 
381-
382- Noun
--
392: Etymology
393- [ edit ] 
394-
=========== wikt قطن ===========
102- 2.2.2 
103- Verb 
104-
105- 2.2.2.1 
106- Conjugation 
107-
--
109: Etymology 3 
110-
111- 2.3.1 
112- Pronunciation 
113-
114- 2.3.2 
115- Noun 
116-
117- 2.3.2.1 
118- Declension 
119-
--
132: Etymology 
133-
134- 3.2 
135- Pronunciation 
136-
137- 3.3 
138- Noun 
139-
140- 4 
141- Gulf Arabic 
142-
--
149: Etymology 
150-
151- 4.3 
152- Pronunciation 
153-
154- 4.4 
155- Noun 
156-
157- 5 
158- Hijazi Arabic 
159-
--
163: Etymology 
164-
165- 5.2 
166- Pronunciation 
167-
168- 5.3 
169- Noun 
170-
171- 6 
172- Moroccan Arabic 
173-
--
177: Etymology 
178-
179- 6.2 
180- Pronunciation 
181-
182- 6.3 
183- Noun 
184-
185- 6.3.1 
186- Derived terms 
187-
--
194: Etymology 
195-
196- 7.2 
197- Noun 
198-
199- 7.2.1 
200- Derived terms 
201-
202- 7.2.2 
203- Descendants 
204-
--
214: Etymology 
215-
216- 8.2 
217- Pronunciation 
218-
219- 8.3 
220- Noun 
221-
222- 8.3.1 
223- Derived terms 
224-
--
```


## [2026-09-06T20:56:09.812Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nawk 'NR>=230 && NR<=340' 978e59f8b3bbd7d9.txt | grep -n -B3 -A8 -i 'etymolog\\|cotton\\|Egyptian\\|Akkad' | head -60"
}
```


### [2026-09-06T20:56:11.913Z] TOOL RESULT

```
67- Andalusian Arabic
68- [ edit ] 
69-
70: Etymology
71- [ edit ] 
72-
73: Etymology tree
74-
75- Aramaic כִיתָנָא  / כִיתָאנָא ( kittānā ) bor. 
76-
77- Classical Syriac ܟܶܬܳܢܳܐ ( kettānā ) bor. 
78-
79- Arabic قُطْن ( quṭn ) 
80- Andalusian Arabic قطن 
81-
--
91-
92- قطن ( quṭun ) 
93-
94: cotton 
95-
96- Descendants
97- [ edit ] 
98-
99- → Catalan: cotó 
100-
101- → Galician: algodón 
102-
```


## [2026-09-06T20:56:18.017Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -i 'kettānā\\|kittānā\\|Akkad\\|Egyptian\\|substrate\\|Wanderwort' 978e59f8b3bbd7d9.txt | head -30\necho \"--- Arabic section etymology 1 ---\"\nawk 'NR>=225 && NR<=300' 978e59f8b3bbd7d9.txt"
}
```


### [2026-09-06T20:56:19.537Z] TOOL RESULT

```
127: Egyptian Arabic 
129: Toggle Egyptian Arabic subsection 
304: Aramaic כִיתָנָא  / כִיתָאנָא ( kittānā ) bor. 
306: Classical Syriac ܟܶܬܳܢܳܐ ( kettānā ) bor. 
352: Borrowed from Aramaic כִיתָנָא  / כִיתָאנָא ( kittānā ) and its Classical Syriac equivalent ܟܶܬܳܢܳܐ ( kettānā ) , both meaning “flax; linen," from which also Arabic كَتّان ( kattān , “ flax ” ) . The same Aramaic root also gives rise to the apparel-name Aramaic כִּיתּוּנָא ( kittōnā ) and the Syriac forms ܟܝܬܘܢܐ ( kettōnā ) , and ܟܘܬܝܢܐ ( kuttīnā, kottīnā , “ tunic ” ) , especially the Classical Syriac byform ܟܘܬܘܢܐ ( kuttōnā, kottōnā ) .
1290: Egyptian Arabic
1487: Egyptian Arabic terms inherited from Arabic 
1488: Egyptian Arabic terms derived from Arabic 
1489: Egyptian Arabic terms with IPA pronunciation 
1490: Egyptian Arabic lemmas 
1491: Egyptian Arabic nouns 
1492: Egyptian Arabic masculine nouns 
1554: Egyptian Arabic entries referencing ambiguous etymons 
1555: Egyptian Arabic entries with etymon 
1556: Egyptian Arabic entries with etymology texts 
--- Arabic section etymology 1 ---
 Toggle the table of contents 

 قطن 

 12 languages 

 Español 
 فارسی 
 Français 
 Magyar 
 Kurdî 
 ລາວ 
 Malagasy 
 Polski 
 Русский 
 Svenska 
 Türkçe 
 中文 

 Entry 

 Discussion 

 English 

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

 Andalusian Arabic
 [ edit ] 

 Etymology
 [ edit ]
```


## [2026-09-06T20:56:31.353Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=========== χιτών ===========\"; grep -n -A8 -i 'Etymology' f3932c4f2a79a206.txt | sed -n '25,70p'\necho \"=========== tunica ===========\"; grep -n -A8 -i 'Etymology' 4994d5a26ddab510.txt | sed -n '25,80p'\necho \"=========== כתונת ===========\"; grep -n -A8 -i 'Etymology' 6cbdfd5b2f4d7357.txt | sed -n '20,70p'"
}
```


### [2026-09-06T20:56:31.420Z] TOOL RESULT

```
=========== χιτών ===========
=========== tunica ===========
103-
104- 3.3 
105- Noun 
106-
107- 3.3.1 
--
119: Etymology 
120-
121- 4.2 
122- Pronunciation 
123-
124- 4.3 
125- Noun 
126-
127- 4.3.1 
--
223: Etymology
224- [ edit ] 
225-
226- From Latin tunica . Doublet of tunic and maybe distantly related to chiton .
227-
228- Noun
229- [ edit ] 
230-
231- tunica ( countable and uncountable , plural tunicae or tunicas ) 
--
273: Etymology
274- [ edit ] 
275-
276- Borrowed from Latin tunica .
277-
278- Pronunciation
279- [ edit ] 
280-
281- IPA ( key ) : /ˈty.niˌkaː/ 
--
306: Etymology
307- [ edit ] 
308-
309- Borrowed from Latin tunica . Compare the inherited tonaca .
310-
311- Pronunciation
312- [ edit ] 
313-
314- IPA ( key ) : /ˈtu.ni.ka/ 
--
343: Etymology
344- [ edit ] 
345-
346- Possibly of Central Semitic origin as Ancient Greek χῐτών ( khĭtṓn ) , with a metathesis. [ 1 ] Compare Aramaic כִּיתּוּנָא ( kittōnā , “ tunic ” ) / ܟܘܬܝܢܐ ( kuttīnā, kottīnā , “ tunic ” ) , Hebrew כֻּתֹּנֶת ( kuttṓnĕṯ , “ tunic ” ) ; from the word for flax, Aramaic כּיתָּנָא ( kittānā , “ flax ” ) / ܟܬܢܐ ( kettānā , “ flax ” ) , Akkadian 𒃰 ( kitûm , “ flax ” ) , Sumerian 𒃰 ( gada , “ flax ” ) , ultimately a substrate word.
347-
348- However, Etruscan has been suggested as well. [ 2 ] 
349-
350- Compare also borrowed textile terms of unknown origin in Mycenaean Greek 𐀵𐀖𐀏 ( to-mi-ka ) and 𐀵𐀛𐀊 ( to-ni-ja ) , both descriptions of textile, as well as 𐀶𐀙𐀜 ( tu-na-no , “ kind of textile ” ) .
351-
=========== כתונת ===========
```


## [2026-09-06T20:56:46.822Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/کتان\" \\\n \"https://en.wiktionary.org/wiki/تنکه\" \\\n \"https://en.wiktionary.org/wiki/گریس\" \\\n \"https://en.wiktionary.org/wiki/χιτών\" \\\n \"https://en.wiktionary.org/wiki/تنک\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 268 verification (Persian nodes: katan, tonekeh, gris, chiton)\" 2>&1 | tail -1\ndone"
}
```


## [2026-09-06T20:56:48.663Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=========== قار ===========\"; grep -n -i -B2 -A8 'Aramaic\\|Akkad\\|Etymology' 5b03215525b378ed.txt | sed -n '1,80p'\necho \"=========== tar etymonline ===========\"; sed -n '20,32p' 5495373f155d0978.txt"
}
```


### [2026-09-06T20:56:50.880Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7b46505208860b87.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e597cec3df66ba3a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/92449cb678b87904.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f3932c4f2a79a206.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fd55177f33f8a313.txt
```


### [2026-09-06T20:56:50.929Z] TOOL RESULT

```
=========== قار ===========
60-
61- 1.1 
62: Etymology 1 
63-
64- 1.1.1 
65- Adjective 
66-
67- 1.1.1.1 
68- Declension 
69-
70- 1.2 
71: Etymology 2 
72-
73- 1.2.1 
74- Noun 
75-
76- 1.2.1.1 
77- Declension 
78-
79- 1.2.1.2 
--
89-
90- 2.1 
91: Etymology 
92-
93- 2.2 
94- Noun 
95-
96- 2.2.1 
97- Declension 
98-
99- 2.2.2 
--
117-
118- 4.1 
119: Etymology 
120-
121- 4.2 
122- Noun 
123-
124- 4.2.1 
125- Derived terms 
126-
127- 4.2.2 
--
148-
149- 6.1 
150: Etymology 
151-
152- 6.2 
153- Pronunciation 
154-
155- 6.3 
156- Noun 
157-
158- 6.3.1 
--
242- [ edit ] 
243-
244: Etymology 1
245- [ edit ] 
246-
247- Root 
248-
249- ق ر ر ( q r r ) 
250-
251- 18 terms 
252-
--
483- al-qārrāti 
484-
485: Etymology 2
486- [ edit ] 
487-
488- Noun
489- [ edit ] 
490-
491- قَار • ( qār )  m 
492-
493- alternative form of قِير ( qīr ) 
=========== tar etymonline ===========

 Origin and history of tar 

 tar (n.1) 

 type of thick, viscous, dark-colored liquid used as a salve (for sheep), caulking agent (for ships), and incendiary material, Middle English tēr , from Old English teoru , teru "tar, bitumen, resin, gum," literally "the pitch of (certain kinds of) trees," from Proto-Germanic *terw- (source also of Old Norse tjara , Old Frisian tera , Middle Dutch tar , Dutch teer , German Teer ).

 According to Watkins this is probably a derivation of *trewo- , from PIE *derw- , a variant of the root *deru- "be firm, solid, steadfast," with specialized senses "wood, tree" and derivatives referring to objects made of wood.

 Tar baby "a sticky problem" (American English) was popularized by a Joel Chandler Harris "Uncle Remus" story (1881), but the story and the idea are older in Black folklore (the dialect story was printed earlier as part of "Bushy and Jack" in Harper's Monthly Magazine, May, 1867, attributed to Mary Hose). It is attested by 1948 as a derogatory term for "Black person."

 To beat (or knock ) the tar out of someone is attested by 1884; the tar is perhaps euphemistic.
```


## [2026-09-06T20:57:01.074Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/قير\" --note \"page 268: Arabic qir 'tar' etymology\" 2>&1|tail -1\ncd data/verification/sources/web\necho \"=========== Persian کتان ===========\"; grep -n -A8 -i 'Etymology' 7b46505208860b87.txt | sed -n '20,70p'\necho \"=========== تنکه ===========\"; grep -n -A8 -i 'Etymology\\|Persian' e597cec3df66ba3a.txt | head -40\necho \"=========== گریس ===========\"; grep -n -A8 -i 'Etymology' 92449cb678b87904.txt | sed -n '10,50p'\necho \"=========== χιτών ===========\"; grep -n -A9 -i 'Etymology' f3932c4f2a79a206.txt | sed -n '15,60p'"
}
```


### [2026-09-06T20:57:05.445Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/13ac3bfc8987b636.txt
=========== Persian کتان ===========
--
179: Persian entries with etymology texts 
180- Pages using etymon with no ID 
181- Pages with entries 
182- Pages with 1 entry 
183-
184- This page was last edited on 15 August 2026, at 21:53.
185-
186- Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 
187-
=========== تنکه ===========
57: Persian 
58-
59: Toggle Persian subsection 
60-
61- 1.1 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
--
137: Persian
138- [ edit ] 
139-
140: Etymology
141- [ edit ] 
142-
143- From تنک ( tonok , “ thin, flimsy ” ) +‎ ـه ( -e ) .
144-
145- Pronunciation
146- [ edit ] 
147-
148: ( Classical Persian ) IPA ( key ) : /tu.nu.ˈka/ 
149-
150- ( Dari, formal ) IPA ( key ) : [t̪ʰʊ.nʊ.kʰá] 
151-
152- ( Dari, formal ) IPA ( key ) : [t̪ʰʊ.nʊ.kʰá] 
153- ( Kabuli ) IPA ( key ) : [t̪ʰʊ.nʊ.kʰá] 
154-
155- ( Hazaragi ) IPA ( key ) : [t̪ʰu.nu.kʰá] 
156-
--
206: Hayyim, Sulayman ( 1934 ), “ تنکه ”, in New Persian–English dictionary , Teheran: Librairie-imprimerie Béroukhim 
207-
208- Retrieved from " https://en.wiktionary.org/w/index.php?title=تنکه&oldid=91812301 "
209-
=========== گریس ===========
=========== χιτών ===========
177- Together with Mycenaean Greek 𐀑𐀵 ( ki-to ) and likely Latin tunica from some Central Semitic , as found in Aramaic כִּיתּוּנָא ( kittōnā , “ tunic ” ) / ܟܝܬܘܢܐ ( kittōnā , “ tunic ” ) , Hebrew כֻּתֹּנֶת ( kuttṓnĕṯ , “ tunic ” ) , which is derived from the local word for flax , found as Aramaic כּיתָּנָא ( kittānā , “ flax ” ) / ܟܬܢܐ ( kettānā , “ flax ” ) , Akkadian 𒃰 ( kitûm , “ flax ” ) , Sumerian 𒃰 ( gada , “ flax ” ) .
178-
179- Pronunciation
180- [ edit ] 
181-
182- IPA ( key ) : /kʰi.tɔ̌ːn/ → /çiˈton/ → /çiˈton/ 
183-
```


## [2026-09-06T20:57:13.992Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== Persian کتان full ===\"; awk 'NR>=100 && NR<=180' 7b46505208860b87.txt | grep -v '^ *$' | head -40\necho \"=== گریس ===\"; awk 'NR>=60 && NR<=160' 92449cb678b87904.txt | grep -v '^ *$' | head -30\necho \"=== قير Arabic ===\"; grep -n -A8 -i 'Etymology' 13ac3bfc8987b636.txt | sed -n '15,70p'"
}
```


### [2026-09-06T20:57:15.641Z] TOOL RESULT

```
=== Persian کتان full ===
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
 See also: كتان 
 Persian
 [ edit ] 
 Etymology
 [ edit ] 
 Borrowed from Arabic كَتَّان ( kattān ) .
 Noun
 [ edit ] 
 کتان • ( katân ) 
 flax ( the plant or fibers of Linum usitatissimum ) 
 linen ( thread or cloth made from flax fiber ) 
 شلوارِ کتان ― šalvâr-e katân ― linen pants, linen trousers 
 Descendants
 [ edit ] 
 → Middle Armenian: քթան ( kʻtʻan ) 
 Armenian: քթան ( kʻtʻan ) 
 → Armenian: քաթան ( kʻatʻan ) 
 → Gujarati: કતાન ( katān ) 
=== گریس ===
=== قير Arabic ===
95-
96- 2.2.1 
97- Descendants 
98-
99- 2.3 
--
108: Etymology 
109-
110- 3.2 
111- Pronunciation 
112-
113- 3.3 
114- Noun 
115-
116- 4 
--
122: Etymology 
123-
124- 4.2 
125- Noun 
126-
127- 4.3 
128- References 
129-
130- Toggle the table of contents 
--
209: Etymology
210- [ edit ] 
211-
212- Borrowed from Aramaic קִירָא / ܩܝܪܐ ( qīrā , “ bitumen; wax ” ) (also ܩܐܪܐ ( qārā ) ), from Akkadian 𒀀𒇒𒉈 ( /⁠qīru⁠/ , “ bitumen ” ) ; uncertain relation to Ancient Greek κηρός ( kērós , “ wax ” ) , Latin cēra ( “ wax ” ) which stem from an unknown substrate. Likely ultimately related to Akkadian 𒌋𒀜 ( /⁠kīru⁠/ , “ kiln ” ) from Sumerian 𒌋𒀜 ( gir , “ kiln ” ) , which also gave rise to Aramaic גִירָא , ܓܝܪܐ ( gīrā , “ lime ” ) , and Arabic جِير ( jīr , “ lime ” ) , Northern Luri قیل ( qil ) .
213-
214- Noun
215- [ edit ] 
216-
217- قِير • ( qīr )  m 
--
811: Etymology
812- [ edit ] 
813-
814: (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 
815-
816- Noun
817- [ edit ] 
818-
819- قَيِرْ ( qayır ) 
820-
821- sand 
822-
--
838: Etymology
839- [ edit ] 
840-
841: Etymology tree
842-
843- Proto-Indo-European *ḱe ? 
844- Proto-Indo-European *ḱóm
```


## [2026-09-06T20:57:33.436Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 68 69 70; do echo \"===== leaf $n =====\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' AKD.txt | head -45; done 2>/dev/null | grep -n -iE 'Wachs|qir|kir|Teer|Erdpech|kupru|60|61|62' | head -40"
}
```


### [2026-09-06T20:57:35.277Z] TOOL RESULT

```
54:      60      
61:akk.  gassu  Gips  s.  oben  S.  31  f.  akk.  hipru  Erdpech,   As-
64:Teer  od.  ä.  :  >  wohl  aram.,  trotz  des  ',  'atränä,  'etrcinä  Teer*  O,  mit au
```


## [2026-09-06T20:57:37.544Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==70' AKD.txt | sed -n '1,40p'"
}
```


### [2026-09-06T20:57:39.198Z] TOOL RESULT

```
in    :  >   wohl   hebr.   .idbö.  akk.  sämtu,
sändii,  ein  Edelstein  (eig.  der  rotbraune)  :  dazu  wolü  hebr.  suham. [akk.  barraqtu  ein  Edelstein,   auch  im  Akk.  Fremdw.,  spät  und  vereinzelt
1)  Daß  die  eine  Pariser  Sargontafel  aus  Magnesit  besteht,  ist  m.  E.  kein  zwingender Beweis  für  abäru  =  Magnesit;  denn  vgl.  neben  der  Aufzählung  in  dieser,  der  Silber- und Goldtafel  auch  diejenige  in  Khors.  159  f.  und  Ann.  420  f.  Es  könnte  daher  z.  B. auch  aspü  =  Magnesit  sein.
      60      
belegt  :  zunächst  viell.  >  späthebr.  iäräqet,  bänjat,  angeblich  Smaragd. Fraglich,  ob  das  Wort  semit.  Ursprungs  (dann  zu  St.  brq  blitzen);  idg. entspricht  skr.  maralcata,  griech.  fiÜQuySog,  of^dgaySog  usw.,  Smaragd.]
[akk.  aJpü,  auch  jasupü  und  jos^m  eine  Steinart,  viell.  Magnesit  (s. S.  59  Anm.  1)  :  dazu  wohl  späthebr.  jclspe  ein  Steinname,  und  doch  wohl auch  griech.  Xaam?  usw.,  Jaspis^  [akk.  algnmisu  eine  Steinart,  auch  im
Akk.  wohl  Fremdw.  :  dazu  wohl  späthebr.  'älgahts,  schwerlich  „Eisstücke", bei  Ez.  u.  vieU.  Sir.  46,  5  und  ägypt.  "rqhS  eine  besonders  harte  Steiuart.
[akk.  burallu^  eine  Steinart,  vieU.  Berj^ll,  dann  zu  :  griech.  ß^Qvlloe, deutsch  auch  noch  in  Brille,  sanskr.  vrlidüriya,  praki\  verulia,  Pali  velu- riya  (syr.  hellüra  und  heridlä,  arab.  ballftr,  äth.  hereile  und  hellnr).
[akk.  sassu  wohl  weißer  Marmor  bezw.  Alabaster  :  dazu  späthebr. sajis,  ses,  syr.  slsä,  ägypt.  ss.]  akk.  p%lu,  pidu  Kalkstein  :  dazu
wohl  armen,  hur  Kalk,  sowie  griech.  nüQog  eine  Kalksteinart.
akk.  gassu  Gips  s.  oben  S.  31  f.  akk.  hipru  Erdpech,   As-
phalt^ :  >  hebr.  Icöper  Gen.  6,14,  aram.  hiprä  O  arab.  kufr,  sowie armen.  fe«pr,  falls  nicht  direkt  <[  akk.).  Ygl.  noch  unten  zu  hipr7hi. Da  akk.  Mm  Ofen  (s.  oben  S.  32)  speziell  gerade  vom  Asphalt-,  Pechofen des  Schiffers  gebraucht  wird,  wäre  es  nicht  unmöglich  daß  :  >  syr.  und jüd.-aram.  qträ^  Asphalt,  Pech  (>>  arab.  qlr  und  qär);  desgl.  dann  aber wohl  auch  aram.  gir,  gträ  Kalk  O  wohl  späthebr.  gtr,  sowie  arab.  gajjär, aber  auch  glr,  auch  südarab.  gjr  und  äth.  in  gajjara  tünchen).
alck.  naptu  Erdöl,  Naphtha  :  >  aram.  naptä,  neptä  O  arab.  naft, pers.  neft,  sowie  griech.  vätpfia^  usw.,  NapJdha).  akk.  etrdnu  wohl
Teer  od.  ä.  :  >  wohl  aram.,  trotz  des  ',  'atränä,  'etrcinä  Teer*  O,  mit au
```


## [2026-09-06T20:58:09.725Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ngrep -rn \"VFO\" --include=*.json --include=*.md --include=*.txt data/ tools/ 2>/dev/null | grep -v 'refs=' | head -10\necho \"---\"; grep -rn '\"VFO\"\\|VFO:' data/verification/sources/refs_online.json | head\necho \"--- extracted bibliography? ---\"; ls data/extracted/ | head -20"
}
```


### [2026-09-06T20:58:09.800Z] TOOL RESULT

```
(eval):2: no matches found: --include=*.json
---
--- extracted bibliography? ---
batch
NEXT_CHUNK
RETRY.txt
test
```


## [2026-09-06T20:58:12.736Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ngrep -rn \"VFO\" data/verification/sources/refs_online.json | head -5\necho \"=== search repo for VFO bibliography ===\"\ngrep -rIl \"VFO\" . --exclude-dir=.git 2>/dev/null | head -20"
}
```


### [2026-09-06T20:58:12.847Z] TOOL RESULT

```
=== search repo for VFO bibliography ===
data/translations/fa.json
data/extracted/batch/page-494.json
data/extracted/batch/page-173.json
data/extracted/batch/page-268.json
data/extracted/batch/page-471.json
data/extracted/batch/page-44.json
data/extracted/batch/page-77.json
data/verification/page-241.json
data/verification/process/verify-page-257.jsonl
data/verification/page-77.json
data/verification/page-173.json
data/extracted/batch/page-241.json
data/verification/process/verify-page-56.jsonl
data/verification/process/verify-page-82.jsonl
data/verification/process/verify-page-231.jsonl
data/verification/process/verify-page-54.jsonl
data/verification/page-44.json
data/verification/process/verify-page-210.jsonl
data/verification/process/verify-page-133.jsonl
data/verification/process/verify-page-45.jsonl
```


## [2026-09-06T20:58:16.263Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json,glob,re\nfor f in ['data/verification/page-241.json','data/verification/page-77.json','data/verification/page-173.json']:\n    d=json.load(open(f))\n    s=json.dumps(d,ensure_ascii=False)\n    for m in re.finditer(r'.{200}VFO.{300}', s):\n        print(f, '::', m.group(0)[:500]); print('---')\n        break\nEOF"
}
```


### [2026-09-06T20:58:17.954Z] TOOL RESULT

```
data/verification/page-241.json :: ive.org lending copies; the local AHD file is the IE-roots appendix. Nourai's use of it is only for the 'gypsy < Egyptian' remark, which is standard and confirmed by Klein and Etymonline."}, {"ref": "VFO:24", "status": "not_checked", "note": "VFO is an unresolved abbreviation in this project's bibliography (MISSING_REFERENCES.md line 110: 'VFO | (unresolved abbreviation, probably = VOP) | skipped'); no book could be identified to check."}], "consulted": [{"src": "MON", "where": "Farhang-e Farsi 
---
data/verification/page-77.json :: rce consulted connects it with bādag/bādiye; the p-/b- alternation Nourai relies on (as in piring/biring below) is possible but unattested here, so this word is unverified. The chart's own NOTE, that VFO:18 links these to English 'pot', has no support: 'pot' is Late Latin pottus / Old English pott of obscure origin, unrelated to the batiākē family, and VFO is not even in the project's reference key.", "derivation_fa": "«باده» دنبالهٔ منظم فارسی میانهٔ bādag است؛ پسوند ‑ag فارسی میانه در فارسی نو
---
data/verification/page-173.json :: اژه در همین ماده خودِ کتاب نورایی (ص ۱۴۳) است و استدلال دوری پدید می‌آورد. پس: با احتیاط پذیرفتنی است.", "sources": ["https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%88%D9%87"], "ref_check": [{"ref": "VFO:25", "status": "not_checked", "note": "VFO = M. Ahmad Soltani, Vāžgān-e Fārsi dar Zabānhā-ye Orupā'i (Tehran 1372/1993). refs_online.json has no record for VFO (value null); no copy exists in the local library and none was found online, so the reference is unverifiable — as on pages 44 and 77, w
---
```


## [2026-09-06T20:58:28.222Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN qir/katan ===\"; grep -n -iE '\\bqîr|\\bkîr|Pech|Asphalt|katân|kattân' HRN.txt | head -15\necho \"=== HUB ===\"; grep -n -iE 'qîr|Pech|Asphalt|kattân' HUB.txt | head -15\necho \"=== ARY قیر / کتان / تنکه / گریس ===\"; grep -n -E 'قیر|کتان|تنکه|گریس|تونیک' incoming/ARY/ARY_pages.txt | head -20\necho \"=== FVQ qir / kattan ===\"; grep -n -iE 'qīr|qir\\b|kattān|kattan' FVQ_pages.txt | head -15\necho \"=== PLA (Asbaghi) ===\"; ls incoming/PLA/ 2>/dev/null; grep -rn -iE 'qīr|kattān' incoming/PLA/*.txt 2>/dev/null | head -10"
}
```


### [2026-09-06T20:58:28.362Z] TOOL RESULT

```
=== HRN qir/katan ===
=== HUB ===
3583:Hierzu arm. navf 'Erdharz, Erdpech, ErdSl* (5. Jhd.),
6602:far ein Orbelier (bei Vardan), np. kaftar *Hyane'; ^iwf 'Pech',
=== ARY قیر / کتان / تنکه / گریس ===
281:که آنرا می‌پذیرند» خود دلیل دیگریست در تأیید مکان گهواره در مبداً موجهای کوچگری مرکز
7719:۱ چم این واژه در زبان رومی: قیر. :
10069:انگلیسی و زبان‌های اسکاندنباوی نوین) چم آن "با لد بیرون کردن" و "با تحقیر رد کردن" شده است. ضناً چم
12897:گریه گرییدن گریستن / ۳۳۵
=== FVQ qir / kattan ===
=== PLA (Asbaghi) ===
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
```


## [2026-09-06T20:58:34.370Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7705,7730p' incoming/ARY/ARY_pages.txt\necho \"=== which pdf page ===\"; awk 'NR<=7719 && /\\[pdf page/ {p=$0} END{}' incoming/ARY/ARY_pages.txt; grep -n '\\[pdf page' incoming/ARY/ARY_pages.txt | awk -F: '$1<7719' | tail -2"
}
```


### [2026-09-06T20:58:36.408Z] TOOL RESULT

```
بلرچی (1ل۲لاله8): 87 ,026 پرومی کهن (/۲۸۷-39140 ۵0): 2۸615
افغانی (پشتر) (/4۳07۸۸): 27 ایرلندی کهن (۷افل#ا صا0):
تخاری ۸ (۸ ۸/7 م3ل707)+ 75 6 00-0
تخاری 8 (8 /(4تق708/۸): 786 ,)ک715۸ ولزی (1ک5): ی ات۱۱۱
سانسکریت (8(/5777): آلبانی (8۸/]40.له): 20
1 مم226 وشققق0 ,ت0۸
یونانی (078210): 718۳8۸۰ پسگشت‌ها کرت رد۲
لاتین (7100ل: ,0۷0 1 200
گرتبکه (007716): 05 3 (881188) نققمانما۸2
اسلاوی کهن (ع۷1ما؟ بل#ناتن صاه): 3 (88۸80) 1/0
71 ,217300 برهان قاطع + : ۸۵
روسی (/(4ا5ول): زددراند ۱۱
چکه (280(9): 2۸2788 ,105170۸
یادداشت:
۱ چم این واژه در زبان رومی: قیر. :
چم این واژه در زبان گوتیکه: روز,
۲ واژه‌ی انگلیسی 0۸3و آلمانی 1۸0 (هر ذو به چم "روز نیز از همین واجریشه‌اند.
۳"
[pdf page 262]
۱ دام (به چم *جانور اهلی") / ۲۶۳
اوستایی (4۲85744): 2۸ انگلیسی (57ل6۸01): 71۸315
پهلوی (7/1الل۳۸): 3 دانمارکی (0۸/784): 1۸۵
اوستی (0558770): ۰ 003/370 ,001112 سوئدی (8(۳20[5[7): 71۸6
سانسکریت (7ل5۸۸5): نروژی (07501۸۷/): 7131
0۸۸۰ , 0۸31 ,0۸۵۸ ,0۸۷۸7 " هلندی (4ع07): 1
یرنانی (02870): ایرندی کهن (0ا5ل۸/ ۰:۵۵ 20۸۸/3۸10
=== which pdf page ===
7666:[pdf page 260]
7693:[pdf page 261]
```


## [2026-09-06T20:58:46.168Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://abadis.ir/fatofa/قیر/\" \"https://abadis.ir/fatofa/تنکه/\" \"https://abadis.ir/fatofa/تونیک/\" \"https://abadis.ir/fatofa/گریس/\"; do\npython3 tools/fetch_source.py \"$u\" --note \"page 268: Mo'in/Dehkhoda entries for qir, tonekeh, tonik, geris\" 2>&1|tail -1; done"
}
```


### [2026-09-06T20:58:53.195Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/52f2f619a2619ffa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b33dfc6c6e5f2dce.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4d6f6af97fc2b76b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0230c6bc222ce0ef.txt
```


## [2026-09-06T20:58:56.183Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 52f2f619a2619ffa b33dfc6c6e5f2dce 4d6f6af97fc2b76b 0230c6bc222ce0ef; do echo \"########## $f ##########\"; grep -n -i -A6 'معین\\|دهخدا' $f.txt | head -40; done"
}
```


### [2026-09-06T20:58:57.665Z] TOOL RESULT

```
########## 52f2f619a2619ffa ##########
18: لغت نامه دهخدا
19-
20- قیر. [ ق َی ْ ی ِ ] ( ع ص )تیرانداز ماهر و زیرک و حاذق در آن. ( منتهی الارب ).
21: قیر. ( معرب ، اِ ) جسم جامد غیرمتبلور سیاه رنگی که سطح شکستگی آن مانندشیشه ناصاف است و در اماکن نفتی قدیمی یافت میشود. ترکیب قیر همان ترکیبات هیدروکربورهای نفت است که درنتیجه اکسیداسیون حالت جمود پیدا کرده است. قیرهای طبیعی که به نام مومیایی و زفت رومی نیز نامیده میشوند و وزن مخصوص آنها بین 1/1 و 1/2 و سختی آنها کم و تقریباً 2 میباشد، علاوه بر ترکیبات هیدروکربور در ترکیب آنها ازت و اکسیژن و حتی گوگرد هم وجود دارد. در طبیعت ممکن است قیرهای معدنی با سنگهای آهکی آمیخته یا آنها را آغشته کرده باشد و در این صورت به نام آسفالت طبیعی نامیده میشوند. ساختن آسفالت مصنوعی هم با استفاده از همین آسفالتهای طبیعی صورت میگرفته.در پالایشگاههای نفت در ته دیگهای تصفیه مقادیر زیادی هیدروکربورهای خمیری یا جامد باقی میماند و آن همان قیرهای مصنوعی است که به بازار عرضه میشود و همه خواص قیرهای طبیعی را دارد. در بناها جهت جلوگیری ازنفوذ رطوبت قیر را به کار میبرند. قیر در حدود 100 درجه حرارت ذوب میشود. زفت رومی. مومیایی. قیر طبیعی. حجر قیر. اشبنت. قطران نفت. ( فرهنگ فارسی معین ).
22-- قیراندای ؛ که بقیر انداید.
23-- قیراندود ؛ مقیر. قیراندوده. قیرمالید. اندوده قیر.
24-- قیراندوده ؛ قیرمالیده.
25-- قیراندودی ؛ حاصل مصدر است از قیراندود کردن.
26-- قیرفام ؛ سیاه برنگ قیر.
27-- قیرگون ؛ بمانندقیر سیاه : 
--
42: فرهنگ معین
43-
44- [ ع . ] (اِ. ) جسم جامد یا نیمه جامد به رنگ سیاه مایل به قهوه ای که چسبنده است و بر اثر گرما نرم و سیُال می شود. 
45-
46- فرهنگ عمید
47-
48- مادۀ غلیظ، سیاه رنگ، و چسبناکی که از نفت گرفته می شود و در ساخت آسفالت و عایق کاری بام ساختمان ها به کار می رود. 
--
99:فرهنگ فارسی معین از کتاب راحه الصدور قیر را به زبان ترکی به معنی سرحد و ثغر مربوط می داند که محافظ سرحد مملکت و آن ظاهراً عنوانی بوده مثل قیر خان و مانند آن. 
100-جمعیت این شهر طبق سرشماری سال ۱۳۹۵، برابر با ۲۰٫۰۱۰ تن بوده است. [ ۱] 
101-شهر قیر سابقه ای نسبتاً کهن دارد و مورخان و سیاحانی همچون ابن حوقل بغدادی، اصطخری، ابن بلخی، مستوفی ودیگران بدین شهرستان اشاراتی داشته اند. نقش پارتی در فاصله ۳ کیلومتری قیر مربوط به دوره پارت ها و قلعه های به جامانده از زمان پیش از اسلام نشان دهندهٔ قدمت این شهر است. ( قلعهٔ شاپریون یا پرگون و قلعه گبری ) [ ۵] 
102-در ۲۱ فروردین سال ۱۳۵۱ شمسی زلزله ای به شدت ۶٫۸ در مقیاس ریشتر باعث تخریب گسترده این شهر تاریخی شد؛ و تعداد زیادی از مردم در این فاجعه عظیم جان باختند. [ ۶] 
103-علاوه بر کشاورزی و باغداری شهر می توان به وجود سد سلمان فارسی قیر و کارزین ( سد قیر ) اولین سد بتنی قوسی وزنی ایران واقع در حدود ۲۰ کیلومتری شمال شرقی شهرستان قیر و کارزین و میدان های بزرگ گاز و ذخایر انرژی در منطقه اشاره نمود. [ ۷] محصولات خرمای این شهرستان نیز از لحاظ کمّی قابل توجه و به لحاظ کیفی از بهترین خرماهای منطقه است. [ نیازمند منبع] 
104-• تفرجگاه و چشمه سرآسیاب، تفرجگاهی در فاصله پنجاه متری شرق شهرک الهادی شهر قیر واقع شده است. 
105-• سنگ نگاره قیر و کارزین، در فاصله ۳ کیلومتری قیر مربوط به دوره پارت ها. [ ۵] این اثر در بین گردنه گلومشک و گردنه سم دلدل در جاده قیر - فیروزآباد قرار دارد. [ ۸] 
--
107:• قلعه پرگان: علامه دهخدا در مورد این قلعه چنین آورده است مردم منطقه به آن قلعه پرگون یا پریون یا پریان نیز می گویند. این قلعه در دو کیلومتری شهر قیراست و هم اکنون به صورت تپه ای از دور در میانه دشت نمایان است. با وقوع زلزله ۱۳۵۱ ه‍. ش تعدادی از برجک های داخل قلعه که هنوز پابرجا بود ویران شد. [ ۸] 
108-• مسجد کردشول[ ۵] 
109-• مسجد و حمام قدیمی کارزین[ ۵] 
110-• مقبره سید تاج الدین محمد[ ۵] 
111-• امامزاده سبزپوشان[ ۵] 
112-• قلعه شاه بربر[ ۵] 
113-• آب انبارهای متعدد قدیمی[ ۵] 
--
241: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
242-
243- لینک ها 
244-
245- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
########## b33dfc6c6e5f2dce ##########
18: لغت نامه دهخدا
19-
20: تنکه. [ ت َ ک َ / ک ِ / ت َ ن َ ک َ / ک ِ / ت ُ ن ُ ک َ / ک ِ ]( اِ ) قرص رائج خواه از زر باشد خواه از نقره یا مس.( غیاث اللغات ) ( آنندراج ) ( از فرهنگ فارسی معین ). برگه ای از هر فلزی و ورق طلا و ورق نقره و پول رایج و قسمی از سکه. ( ناظم الاطباء ). مقداری از زر و سیم باشدبه اصطلاح هر جایی... ( انجمن آرا ) : معبر گفت دو تنکه بده تا تعبیر آن بگویم. ( منتخب لطائف عبید زاکانی چ برلین ص 125 ). رجوع به دزی ج 1 ص 153 شود.
21: تنکه. [ت ُ ن ُ ک َ / ک ِ ] ( اِ ) تنبان چرمی که تا سر زانو باشد، وقت کشتی گرفتن پوشند. ( غیاث اللغات ) ( آنندراج ) ( از فرهنگ فارسی معین ) ( از ناظم الاطباء ) : 
22-تنکه در قدمش زود ز هم می پاشد
23-هرکه رویش تنک افتاد چنین می باشد. میرنجات ( از آنندراج ).
24:|| زیرجامه کوتاه زنان. ( یادداشت بخطمرحوم دهخدا ). || در اصطلاح نجاران ، تخته ٔپهن که میان دو پاسار یا دو آلت در درها و پنجره ها بکار برند. ( یادداشت بخط مرحوم دهخدا ). 
25-
26- فرهنگ فارسی
27-
28- قسمت پایین دروپنجره که ازتخته ساخته میشود، شلوارکوتاه که تاسرزانوباشد، شلوارکوتاه زنانه
29-( اسم ) قرص رایج از زر و سیم و مس .
30-تنبان چرمی که تا سر زانو باشد وقت کشتی گرفتن پوشند . یا زیر جامه کوتاه زنان . 
--
32: فرهنگ معین
33-
34- (تُ نُ کِ یا کَ ) (اِ. ) ۱ - شلوار کوتاه که تا سر زانو باشد. ۲ - شلوار کوتاه زنانه یا مردانه .
35- (تَ کِ یا کَ ) (اِ. ) قرص رایج از زر و سیم و مس . 
36-
37- فرهنگ عمید
38-
--
85:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
86-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
87-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
88-
89- تنکه کلمه ای تورکی است که در اصل تونوکه می باشد که از کلمه تون به معنی لباس گرفته شده و به معنی شورت می باشد تنبان هم از همین تون است دیوان الغات تورک
90-
91- برابر پارسی شورت ( short )
--
109: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
110-
111- لینک ها 
112-
113- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
114-
115- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
########## 4d6f6af97fc2b76b ##########
16: فرهنگ معین
17-
18- (تُ ) [ فر. ] (اِ. ) ۱ - بلوز یا ژاکت کوتاه زنانه تا بالای ران که معمولاً با شلوار یا دامن پوشیده می شود. ۲ - داروی بهداشتی مقوی . ۳ - نت پایة یک قطعه موسیقی . ۴ - نت اول در یک گام . 
19-
20- فرهنگ عمید
21-
22- ۱. ژاکت یا بلوز زنانۀ بلند که بخش بالای ران ها را هم می پوشاند.
--
57: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
58-
59- لینک ها 
60-
61- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
62-
63- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
########## 0230c6bc222ce0ef ##########
18: لغت نامه دهخدا
19-
20: گریس. [ گ ِ ] ( اِ ) مصحف «کربس »، «کربش » ( دهخدا ) و گربز، و کریس. ( حاشیه برهان چ معین ). مکر و حیله و فریب. ( برهان ). گریسته بمعنی فریب. ( آنندراج ). || چاپلوسی. ( برهان ). 
21-
22- فرهنگ فارسی
23-
24- یوان نقاش کوبیست اسپانیایی ( و. مادرید ۱۸۸۷ - ف. ۱۹۲۷ م . ) .
25-پیه، روغن، چربی
26-( اسم ) یکی از محصولات نفتی و آن روغنی است بصورت نیمه جامد که در صنعت از آن جهت لغزنده کردن لولا ها و نقاط تماس استفاده میشود . 
--
28: فرهنگ معین
29-
30- (گِ ) [ انگ . ] (اِ. ) روغن ، چربی . 
31-
32- فرهنگ عمید
33-
34- مادۀ جامد یا نیمه جامد که از چربی های گوناگون و استئارین ها به دست می آید و به منظور روان کردن قطعات صنعتی و جلوگیری از زنگ زدن آن ها به کار می رود. 
--
89: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
90-
91- لینک ها 
92-
93- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
94-
95- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است.
```


## [2026-09-06T20:59:19.046Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK crassus ===\"; grep -n 'crassus' POK_full.txt | head -10\necho \"=== POK kērós/Wachs ===\"; grep -n -E 'κηρός|kērós|kēros|Wachs' POK_full.txt | head -15\necho \"=== AHD watkins cere/wax ===\"; grep -n -iE '\\bCERE\\b|kerosene|beeswax' AHD_watkins1985.txt | head -10\necho \"=== IEC Mann keros/krassos ===\"; grep -n -iE 'k[eē]ros.*wax|krassos|crassus' IEC.txt | head -10\necho \"=== SYN Buck flax/linen/wax ===\"; grep -n -iE 'kuttoneth|kittan|kitu|χιτών|chiton|flax' SYN.txt | head -15"
}
```


### [2026-09-06T20:59:19.148Z] TOOL RESULT

```
=== POK crassus ===
46478:Indie *krtsa-)\ Old Indie /r/'/s/7a- 'complete, whole' (compare Latin crassus, Slavic *cbrstvh); 
46485:{*kerati-, or *krati-, compare Latvian kratihs, Lithuanian krotai); crassus ^\h\ck, strong, 
85491:Old Church Slavic tgph 'obtusus, crassus'? perhaps from "gedunsen"; russ. tepst/'strafi 
=== POK kērós/Wachs ===
64942:Old Irish as{a)/d' it grows' (" increases '), Middle Irish 55' Wachsen ' {*pat-to-)\ Gothic 
75644:"verkijmmern, in Wachstum zuriJckbleiben', nus-kurd§s'\v\ Wachstum verkijmmert'. 
75708:German Bavarian schratz"\n Wachstum zuriJckgebliebener Mensch'; Norwegian skrinn 
79815:Wachstum zuriJckgeblieben', become better to a particular family the meaning 
=== AHD watkins cere/wax ===
618:ker-1. Horn, head; with derivatives referring to horned animals, horn-shaped objects, and projecting parts. I. Zero-grade form *kr-. 1. Suffixed form *kr-n- in: a. Ger- manic *Aurnaz in (i) Old English horn, horn: HORN, (HORNBEAM) (ii) German Horn, horn: ALPENHORN, ALT- HORN, FLUGELHORN, HORNBLENDE; Db. Latin cornd, horn: CORN2, CORNEA, CORNEOUS, CORNER, CORNET, CORNICULATE, CORNU; BICORN, CADUCICORN, CAPRI- CORN, CLAVICORN, CORNIFICATION, LAMELLICORN, LON- GICORN, TRICORN, UNICORN. 2. Suffixed and extended form *krs-n- in Germanic *hurznuta in Old English hyrnet, hornet: HORNET. 3. Suffixed form *kr-ei- in: a. Germanic *hraina- in Old Norse hreinn, reindeer: REINDEER; b. Germanic *hrinda- in Old High German hrind, ox (> German Rinder, cattle): RINDERPEST. 4. Suffixed extended form *kros-no- in Greek kranion, skull, upper part of the head: CRANIUM; MIGRAINE, OLECRANON. 5. Suffixed form *kr-a- in: a. Greek karé, kara, head: CHARIVARI; CHEER; b. Greek karoun, to stupefy, be stupefied (< “to feel heavy-headed”): ca- ROTID; c. Greek kardton, carrot (from its hornlike shape): CARROT. 6. Possibly extended form *kri- in Greek krios, ram: CRIOSPHINX. II. Suffixed form *ker-wo-. 1. Latin cervus, deer: CERVINE, SERVAL. 2. Latin cervix, neck: CERVIX. III. Extended and suffixed form *keru-do- in Germanic *herutaz in: a. Old English heorot, hart, stag: HART; b. Dutch hart, deer, hart: HARTEBEEST. IV. Extended form *keras-. 1. Greek keras, horn: CARAT, CERASTES, KERATO-; CERATODUS, (CERATOID), CHELIC- ERA, CLADOCERAN, KERATIN, RHINOCEROS, TRICERA- Tops. 2. Persian sar, head: SIRDAR. 3. Suffixed form *keras-ro- in Latin cerebrum, brain: CEREBELLUM, CERE- BRUM, SAVELOY. V. Extended o-grade form *koru-. 1. Greek Rorumbos, uppermost point (< “head”): CoR- yMB. 2. Greek koruphé, head: CORYPHAEUS. 3. Suffixed form *koru-do- in Greek korudos, crested lark: coRY- DALIS. 4. Suffixed form *koru-ndé in Greek koruné, club, mace: CORYNEBACTERIUM. [Pok. 1. ker- 574.]
=== IEC Mann keros/krassos ===
7808:krop ‘torture’; R kropát, v. ‘botch, mangle? kraps- ‘grab, snatch; rapacious; grab, sei- zure’ Br. krafa ‘seize, snatch; scratch, engrave’; kraf ‘seizure’; kraf, m. ‘stylus’: kraf, krav ‘stitch’; W craff ‘quick, keen; secure’; m. pl. -au ‘clasp, cramp’; craffu, v. ‘secure, grip’; Cor. crafa, v. ‘grip’; crāf, adj. ‘tenacious’; s. pl. crafow "basting-stitch"; cf. crefny, adj. ‘grasping, gree- dy’; OE hrespan ‘strip, despoil’; hresp ‘spolia- tion’ krās- (?) ‘glory, praise’ ON hrósa, v. ‘praise’; hrósan, f. ‘praise; boast- ing’; hræsni, f. id.; mod. Icel. hrós, n. ‘praise’; OCS krasa ‘beauty’ (and com. Sl.); Latv. cf. krāšns 'splendid'. See Supt. K : krās- (krast-, see karst-). Variant in W cras ‘toasted, parched, arid’; Br. kraz, id. krateið ‘overpower’. See kratos Gk. kratéo ‘rule’; OCS krostọ, krotiti (tame' and com. Sl.) kratos, is, us “strong; strength, power, force’. WP I, 354 Skt. krátuh “power, will, ability’; Av xratus ‘wisdom’; Ober xraQu-, id.; Gk. kratüs *power- ful”; krátos, n. ‘power’; W crad, craid, m. (“vig- our, force’, fr. *kratos, *kratis); OHG hrad ‘swift; OE hrad “swift, active; ON hraór, id.; OCS cf. krotükü ('tame', lit. overpower- ed"). Isophonic: Li. kratüs (rough, uneven’ krátos, à, is 'enclosure, envelope” W crawd “coating, surface’; OE hréóa 'goat- skin cover, mantle’; cf. hroó-girela ‘crown’; Li. krótai, krótos, mfpl. "lattice, grille’; Latv. krats ‘cage, prison’. (W and OE ambig.) kratsos, ios (?) Lat. crassus ‘fat, gross’; ON hress “hale, hear- ty’; hressa, Lat v. ‘cheer’ (kraug-, variant of krauk-, q. v.). (WP I, 417, 477 & II, 573) Hes. kraugós ‘woodpecker’; Gk. kraugé ‘croak, caw’ krauk- ‘caw, croak; crow, raven’. (Variant: krauk-) EMAIb. krak, mod. krrak ‘a bird of crow type’; OE hrēa (Crumble in the bowels’? Cf. hream ‘uproar’, fr. *kraukmo-?); Pol. Ukr. kruk ‘raven’; Latv. kraukjs ‘rook’ beside krauklis
8089:krksKios trough, harsh’. Cf. krs- (2) Skt. cf. kréchráh ‘severe’; (Lat. crassus “thick, coarse’, ambig. and of uncertain phonol.); W crych (1) “rough, rugged"; OE horsc (1) “sharp, keen, daring’; Srb. cf. krhak ‘brittle’; krš ‘rock’; Li. kiršùs, adj. ‘irascible’
=== SYN Buck flax/linen/wax ===
9188:4. Ir. men, NIr. min: Lith. minti ‘tread, break flax, prepare skins’, ChSI. meti, ‘compress’, etc. Walde-P. 2.263.
9994:6.28 LINEN; FLAX
9995:Grk.  Alvov Goth. lein Lith. audeklas, drobe; linat NG avd wav; Awvepe ON lin, lérept, hérr Lett. audekls; lint Lat. linum, linteum Dan. _lerred, linned; h¢r ChSI. plattno; linit Si tela (di lino), lino Sw. _ Larft, linne; lin SCr. _platno, bez; lan Fr. toile (de lin); lin OE linen; lin, fleax Boh.  pldino; len Sp. lienzo, lino ME Linen; lin, flex Pol. _—plotno; len Rum. pinzd; in NE linen; flax Russ. polotno, cholst; len Ir. lin Du. linnen, lijnwaad; vlas Skt. kgauma-; kgumda- Nir. lion OHG _ linin; lin, flahs, haru W. Uiain; lin MHG linen, linwat; lin, Br. lien; lin vlahs, har
9998:Linen, considered here as a material for clothing parallel to wool, cotton, etc., was originally denoted by the same word as that for the raw material, flax. But ‘linen’ and ‘flax’ are now generally differentiated, partly by parallel forms
10001:for _ first the words | jist Ben’ and ‘flax’, and adding J
10003:tase? +]ino- ‘flax, linen’. piel j, Bu rade, Reallex. 1.323 ft au 1.555, Walde-H. 1.810.
10005:‘flax, linen’, NG wd ravl rape ‘flax’. ae
10006:Fi whence It., Sp. no Max, a i Rum. in ‘flax’. For It. ‘ile ‘cloth’, see 6.21. Ir. linge fr. Lat. adj. lineus Gamillscheg
10007:an tot he (clothes, etc.), iof linen’. REW 5060. 563. eat weeny ir. lin ‘linen’, NIr. lion ‘flax, linen , V. lin, Br. lin ‘flax’, fr. Lat. linwm (Vendryes, De hib. voc. 151; Loth, Mots lat. 182), but W. Uliain, Br. lien finen’ are perh. cognate, though the for- mation is obscure. Goth. lein ‘linen’, ON lin ‘flax, linen’, Norw., Sw. lin, OF, OHG, MHG lin, ME lin, NHG lein ‘flax’. Hence OF linen, OHG linin, etc., orig. adjs. ‘flaxen, linen’, ON lérept, Dan. lerred, Sw. larft ‘inen (goods)’, for *lin-rept, epd. of ript ‘piece of cloth’ : ON riptt ‘veil’ (6.59). Dan. linned (with -d after at Sw. linne, fr. MLG linne = aL ae (above). Falk-Torp 636, quist 577, 609,
10009:ON va0 ‘cloth? (6.21). : linai, Lett, lini, ChSI. lint, ae + Pol. len, Russ, len ‘flax’. , Uinteum textum, or simply “a aes), the proper term ©, obscure, blend of linum
10015:3. ON hérr ‘flax, linen’, Dan. hgr, OHG haru, MHG har, OFris. her ‘flax’, etym. dub. Walde-P. 1.356. Falk- Torp 454.
10016:OE fleaz, ME flex, NE flax, Du. vlas, OHG fiahs, MHG vlahs, NHG flachs, prob. fr. the root of Grk. whé&w, Lat. plectere, OHG flehtan ‘plait, braid’ (9.75). Walde-P. 2.97. NED s.v. flaz.
10024:6. Skt. ksd@uma- ‘linen’, fr. ksuma- ‘flax’, perh. : ksu-pa- ‘shrub, bush’, Russ. chmyz ‘brush’, chvorost ‘bush’, all dub. H. Petersson, KZ 46, 145f. Walde-P. 1.501.
12684:Nit. braea (also a carding imple- ment), fr. NE brake ‘instrument for breaking flax’ and ‘harrow’ (NED brake, sb.*).
14521:jntens. kraikyti, beside eading’, kraikas of flax’, Lett. 2,270),
```


## [2026-09-06T20:59:29.147Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '46470,46492p' POK_full.txt\necho \"=== page marker ===\"; awk 'NR<=46485 && /^ *[0-9]{3,4} *$/ {p=$0; n=NR} END{print n\": \"p}' POK_full.txt\necho \"=== POK Wachs / kēros entry ===\"; grep -n -iE 'kar-.*Wachs|kēro|kāro|cera .Wachs|cēra' POK_full.txt | head -10"
}
```


### [2026-09-06T20:59:31.221Z] TOOL RESULT

```
Note: extension from ker-7, S. 574; see below (s)ker-3. 

Material: Old Irish krnatti^ twists the thread, spins ', karttar- "the spinner ', crtati^ binds, 

fixes together', kata-m. 'netting, mat ' (Middle Indie for *krta-), probably also kutf-, kutTi. 

'cottage' {*krfi), kudya-n. {*krtya-) ' (*geflochtene) Wand ', pali koccha-' wickerwork ' (Old 

Indie *krtsa-)\ Old Indie /r/'/s/7a- 'complete, whole' (compare Latin crassus, Slavic *cbrstvh); 

gr. KapTaA(A)o(; m. 'basket', KpoTwvr) ' excrescence on trees, esp. on the olive, 
fragments of bronchial cartilage ' (*KpaTU)va); with ^/-colored reduced grade KupTO(;, Kuprn 
' a fishing-basket, fish snaring net, cage', Kupria ' wickerwork '; 

Latin cratis' wicker-work, a hurdle ', crates dentatae^ harrow ', cratio, -/?e 'harrow' 
{*kerati-, or *krati-, compare Latvian kratihs, Lithuanian krotai); crassus ^\h\ck, strong, 
coarse'; probably cartilage 'gristle' (probably ker[a]t-, compare paima : naAapn); 

In e-grade: 

alb. kjerthuii^ circle, thread reel, thread coil, windlass ' (: Middle Irish ceirtiesee below); 
Maybe alb. kerthiza ' navel, navel cord ' : sloven, kretica ' knot in the weave ': alb. kurth ' 
trap, (net) '. 
=== page marker ===
: 
=== POK Wachs / kēros entry ===
```


## [2026-09-06T20:59:45.625Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=40400 && NR<=40520 && /^[[:space:]]*1[0-9]{3}[[:space:]]*$/ {print NR\": \"$0}' KLN_1966.txt | head\necho \"--- crass page ---\"; awk 'NR>=9500 && NR<=9600 && /^[[:space:]]*[0-9]{3}[[:space:]]*$/ {print NR\": \"$0}' KLN_1966.txt | head\ncd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://www.ahdictionary.com/word/search.html?q=cotton\" --note \"page 268: AHD entry for cotton (Nourai cites AHD for Spanish coton)\" 2>&1|tail -1"
}
```


### [2026-09-06T20:59:47.793Z] TOOL RESULT

```
40520: 1666
--- crass page ---
9521: 366
/home/sfmqrb/git/rishe/data/verification/sources/web/4fc7318244bb1eb6.txt
```


## [2026-09-06T20:59:50.510Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -i -A4 'cotton' 4fc7318244bb1eb6.txt | grep -i -B1 -A3 'arab\\|origin\\|Middle English' | head -20"
}
```


### [2026-09-06T20:59:50.563Z] TOOL RESULT

```
55-
56- [Middle English cotoun , from Old French coton , from Old Italian cotone , from Arabic qu ṭ n, qu ṭ un ; see q ṭ n in the Appendix of Semitic roots .]
57- (click for a larger image) 
58: cotton cotton plant with bolls 
59-
```


## [2026-09-06T21:01:00.034Z] TOOL CALL #52: Bash

```json
{
 "command": "sed -n 1,120p tools/verify_check.py"
}
```


### [2026-09-06T21:01:00.074Z] TOOL RESULT

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


## [2026-09-06T21:01:12.795Z] TOOL CALL #53: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg268.png data/verification/sources/refs/ocr/BOOK/268.png && ls -la data/verification/sources/refs/ocr/BOOK/268.png"
}
```


### [2026-09-06T21:01:12.861Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 69592 Sep  6 17:01 data/verification/sources/refs/ocr/BOOK/268.png
```


## [2026-09-06T21:08:26.487Z] TOOL CALL #54: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk268.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_KEROS = \"https://en.wiktionary.org/wiki/κηρός\"\nW_CRASSUS = \"https://en.wiktionary.org/wiki/crassus\"\nE_GREASE = \"https://www.etymonline.com/word/grease\"\nE_KEROSENE = \"https://www.etymonline.com/word/kerosene\"\nW_QIR_AR = \"https://en.wiktionary.org/wiki/قير\"\nW_QAR = \"https://en.wiktionary.org/wiki/قار\"\nW_KATTAN = \"https://en.wiktionary.org/wiki/كتان\"\nW_QUTN = \"https://en.wiktionary.org/wiki/قطن\"\nE_COTTON = \"https://www.etymonline.com/word/cotton\"\nW_KHITON = \"https://en.wiktionary.org/wiki/χιτών\"\nW_TUNICA = \"https://en.wiktionary.org/wiki/tunica\"\nE_TUNIC = \"https://www.etymonline.com/word/tunic\"\nE_TAR = \"https://www.etymonline.com/word/tar\"\nW_KATAN_FA = \"https://en.wiktionary.org/wiki/کتان\"\nW_TONAKE = \"https://en.wiktionary.org/wiki/تنکه\"\nA_QIR = \"https://abadis.ir/fatofa/قیر/\"\nA_TONAKE = \"https://abadis.ir/fatofa/تنکه/\"\nA_TONIK = \"https://abadis.ir/fatofa/تونیک/\"\nA_GERIS = \"https://abadis.ir/fatofa/گریس/\"\nAHD_COTTON = \"https://www.ahdictionary.com/word/search.html?q=cotton\"\n\nAKD60 = (\"Zimmern, Akkadische Fremdwörter, printed p. 60 (local AKD.txt, form-feed leaf 70): \"\n         \"«Da akk. kīru Ofen (s. oben S. 32) speziell gerade vom Asphalt-, Pechofen des Schiffers \"\n         \"gebraucht wird, wäre es nicht unmöglich daß : > syr. und jüd.-aram. qīrā Asphalt, Pech \"\n         \"(> arab. qīr und qār)»; and p. 61 n. 3: «Jedenfalls zu trennen von jüd.-aram. qērā Wachs \"\n         \"< griech. κηρός.»\")\n\nentries = []\n\n# ---------------- entry 0 : Kîru ----------------\ne0_nodes = [\n dict(\n  id=1, lang=\"Latin\", words=\"crassus; crassia\", verdict=\"disputed\",\n  derivation=(\"Latin crassus is an adjective 'thick, dense, solid, fat' (Plautus onward), not a noun \"\n              \"'oil'; crassia is not classical Latin at all but the reconstructed Vulgar Latin \"\n              \"*crassia 'melted animal fat' that the Romance forms (Old French craisse/gresse, \"\n              \"Italian grascia, Catalan graxa) presuppose — Klein and Etymonline both print it with \"\n              \"an asterisk. Its origin is Indo-European or unknown, never Semitic: Klein derives it \"\n              \"from IE base *qerat-/*qert- 'to roll or twist together' (whence also Latin crātis \"\n              \"'wickerwork'), Pokorny lists crassus under kert-, kerət-, krāt- 'drehen, flechten' \"\n              \"(IEW 584), Mann sets up kratsos, and Wiktionary calls it uncertain (perhaps PIE \"\n              \"*kert-, perhaps contaminated with grossus). Nothing connects it to an Akkadian word \"\n              \"for wax or kiln: neither the form (Akk. k-/q- + -īru vs. Lat. crass- with geminate -ss-) \"\n              \"nor the sense ('wax'/'kiln' vs. 'thick, fat') can be bridged.\"),\n  derivation_fa=(\"واژهٔ لاتینی crassus صفت است به معنی «ستبر، چرب، غلیظ»، نه اسمی به معنی «روغن»؛ و \"\n                 \"crassia نیز صورتی است بازسازی‌شده از لاتینی عامیانه *crassia «پیهِ گداخته» که \"\n                 \"صورت‌های رومیایی از آن برآمده‌اند. کلاین آن را از ریشهٔ هندواروپایی *qerat-/*qert- \"\n                 \"«تابیدن، بافتن» می‌گیرد (همانند crātis «حصیر»)، و پوکورنی نیز آن را ذیل kert- در \"\n                 \"صفحهٔ ۵۸۴ آورده است؛ ویکی‌واژه ریشه را نامعلوم می‌داند. هیچ منبعی آن را وام‌واژه‌ای \"\n                 \"سامی نمی‌شمارد؛ نه از نظر آوایی و نه از نظر معنایی راهی از «کیرو»ی اکدی به crassus \"\n                 \"لاتینی نیست. پس ادعای نورایی را پژوهش امروزی رد می‌کند.\"),\n  sources=[W_CRASSUS, E_GREASE],\n  ref_check=[dict(ref=\"KLN\", status=\"contradicts\", note=(\"Klein, KLN_1966.txt p. 366 s.v. 'crass': «L. crassus, \"\n             \"'thick, solid, dense, fat', for *qr̥t-tos, fr. I.-E. base *qerat-, *qert-, 'to roll or twist \"\n             \"together', whence also L. crātis, 'wickerwork, hurdle'» — an IE, not a Semitic, etymology; \"\n             \"Klein's page on grease gives VL. *crassia (asterisked).\"))],\n  consulted=[\n    dict(src=\"POK\", where=\"IEW 584, s.v. kert-, kerət-, krāt-\", stance=\"contradicts\",\n         note=\"POK_full.txt line 46485: «Latin cratis 'wicker-work, a hurdle' … crassus 'thick, strong, coarse'» — crassus is filed under an IE root, with no Semitic source.\"),\n    dict(src=\"LAT\", where=\"Ernout–Meillet s.v. crassus\", stance=\"contradicts\",\n         note=\"LAT.txt line 14329: «crassus, -a, -um: gros, épais (sens physique et moral), gras … Les l. romanes attestent aussi *crassia, M.L.2298» — Latin-internal, no loan noted.\"),\n    dict(src=\"IEC\", where=\"Mann, s.v. kratsos\", stance=\"partial\",\n         note=\"IEC.txt line 7808: «kratsos, ios (?) Lat. crassus 'fat, gross'; ON hress 'hale, hearty'»; at line 8089 Mann adds «(Lat. crassus 'thick, coarse', ambig. and of uncertain phonol.)» — IE but disputed within IE.\"),\n    dict(src=\"AHD\", where=\"Watkins 1985 s.v. kert-\", stance=\"silent\",\n         note=\"AHD_watkins1985.txt line 623 gives kert- 'to turn, entwine' with Latin crātis (CRATE, GRATE) but does not list crassus at all.\"),\n  ]),\n dict(\n  id=2, lang=\"Old French\", words=\"\", verdict=\"confirmed\",\n  derivation=(\"The empty pass-through box is Old French craisse / gresse / graisse 'grease, fat' \"\n              \"(12th c.), the regular Gallo-Romance outcome of Vulgar Latin *crassia: intervocalic \"\n              \"-ss- was kept, the -ia gave -e, and initial cr- was voiced to gr- under the influence \"\n              \"of gras 'fat' < crassus (the by-form craisset 'oil lamp' > English cresset preserves \"\n              \"the older cr-). Modern French graisse.\"),\n  derivation_fa=(\"این خانهٔ خالی همان فرانسوی کهن craisse/gresse (فرانسوی امروز graisse) «چربی» است که \"\n                 \"دنبالهٔ منظم لاتینی عامیانهٔ *crassia است: خوشهٔ -ss- برجا مانده، پایانهٔ -ia به -e بدل \"\n                 \"شده و کاف آغازین (cr-) زیر تأثیر gras «چرب» به گ (gr-) واک‌دار شده است. صورت کهن‌تر با \"\n                 \"cr- در craisset «چراغ روغنی» (انگلیسی cresset) بازمانده است.\"),\n  sources=[E_GREASE],\n  ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"Nourai gives no reference for this node; checked against Klein and Etymonline instead (see consulted).\")],\n  consulted=[\n    dict(src=\"KLN\", where=\"KLN_1966.txt s.v. grease (p. 674 region, line 16636)\", stance=\"supports\",\n         note=\"«grease, n. — ME. gresse, grese, fr. OF. gresse, graisse (F. graisse), fr. VL. *crassia, 'thickness, fatness', fr. L. crassus, 'thick, fat'».\"),\n    dict(src=\"SKT\", where=\"Skeat, s.v. grease\", stance=\"supports\",\n         note=\"Skeat likewise routes English grease through Old French graisse from Late Latin *crassia; SKT.txt has no separate Semitic claim.\"),\n  ]),\n dict(\n  id=3, lang=\"English\", words=\"grease\", verdict=\"confirmed\",\n  derivation=(\"Middle English gresse / grese (c. 1300) 'oily fat of land animals', borrowed from \"\n              \"Anglo-French grece and Old French gresse/craisse; the modern spelling with -ea- \"\n              \"reflects the ME long vowel. The verb 'to grease' is mid-14c. from the noun. The \"\n              \"Latin > Old French > Middle English chain is uncontroversial; only the Akkadian \"\n              \"starting point of the whole branch is not.\"),\n  derivation_fa=(\"انگلیسی grease از انگلیسی میانهٔ gresse/grese (حدود ۱۳۰۰ م.) است که از انگلونورمان \"\n                 \"grece و فرانسوی کهن gresse وام گرفته شده؛ املای -ea- بازتاب واکهٔ کشیدهٔ انگلیسی میانه \"\n                 \"است. این زنجیرهٔ لاتینی ← فرانسوی کهن ← انگلیسی میانه بی‌چون‌وچرا پذیرفته است و تنها \"\n                 \"سرآغاز اکدیِ کل این شاخه پذیرفتنی نیست.\"),\n  sources=[E_GREASE],\n  ref_check=[\n    dict(ref=\"KLN\", status=\"supports\", note=\"KLN_1966.txt line 16636 s.v. grease: «ME. gresse, grese, fr. OF. gresse, graisse … fr. VL. *crassia … fr. L. crassus».\"),\n    dict(ref=\"AHD\", status=\"not_checked\", note=\"Nourai cites AHD without a page; the local AHD file is only the Watkins IE-roots appendix, which has no entry for grease (crassus is absent from it).\"),\n  ],\n  consulted=[\n    dict(src=\"KLN\", where=\"KLN_1966.txt s.v. grease\", stance=\"supports\", note=\"see ref_check.\"),\n    dict(src=\"SKT\", where=\"Skeat s.v. grease\", stance=\"supports\", note=\"same French–Latin chain; no Semitic element.\"),\n    dict(src=\"WEB\", where=\"Webster's New Twentieth Century, vol. 1 (A–?)\", stance=\"silent\", note=\"the open scan is volume 1 only, so 'grease' could not be looked up.\"),\n  ]),\n dict(\n  id=4, lang=\"Persian\", words=\"grîs «گریس»\", verdict=\"confirmed\",\n  derivation=(\"Persian گریس gerīs/gerīs 'lubricating grease' is a 20th-century technical loan from \"\n              \"English grease, taken in with the oil industry (Abadan refinery vocabulary) rather \"\n              \"than through French; Mo'in marks it «[انگ.]» = English. The final -s of English \"\n              \"grease [griːs] is rendered by س and the long [iː] by ی. The older Persian گریس \"\n              \"recorded by Dehkhoda ('trickery, flattery', a miswriting of کربس/گربز) is an unrelated \"\n              \"homograph.\"),\n  derivation_fa=(\"«گریس» وام‌واژه‌ای امروزی و صنعتی از انگلیسی grease است که با صنعت نفت (اصطلاحات \"\n                 \"پالایشگاه آبادان) وارد فارسی شده است؛ معین در فرهنگ فارسی آن را با نشان «[انگ.]» \"\n                 \"می‌آورد: «(گِ) [انگ.] (اِ.) روغن، چربی». واکهٔ کشیدهٔ [iː] انگلیسی با «ی» و [s] پایانی \"\n                 \"با «س» نوشته شده است. «گریسِ» کهنِ لغت‌نامهٔ دهخدا («مکر و حیله»، مصحّف کربس/گربز) \"\n                 \"واژه‌ای دیگر و هم‌نویسه است. ادعای نورایی درست است.\"),\n  sources=[A_GERIS, E_GREASE],\n  ref_check=[dict(ref=\"VFO:24\", status=\"not_checked\", note=\"VFO is an unresolved abbreviation in this project's bibliography (refs_online.json has no VFO record; MISSING_REFERENCES.md marks it 'probably = VOP, skipped'). No copy exists locally or online, so the citation cannot be checked — the same situation as on pages 44, 77 and 241.\")],\n  consulted=[\n    dict(src=\"MON\", where=\"Farhang-e Farsi s.v. گریس (via abadis.ir)\", stance=\"supports\",\n         note=\"«(گِ) [انگ.] (اِ.) روغن، چربی.» — Mo'in explicitly labels the word English.\"),\n    dict(src=\"BQT\", where=\"Borhan-e Qate' (17th-c. text)\", stance=\"silent\",\n         note=\"a 20th-century industrial loan cannot appear in Borhan; Dehkhoda's گریس is the unrelated old word 'مکر و حیله' (مصحّف کربس).\"),\n    dict(src=\"ARY\", where=\"ARY_pages.txt\", stance=\"silent\", note=\"grep for گریس in Aryanpur's IE-roots dictionary returns nothing.\"),\n  ]),\n dict(\n  id=5, lang=\"Greek\", words=\"kěros\", verdict=\"disputed\",\n  derivation=(\"The Greek word is real: κηρός kērós 'beeswax' (Homer onward; the book's 'kěros' with \"\n              \"a breve mis-marks the long η). But its source is not Akkadian. Wiktionary (following \"\n              \"Beekes) calls it «a foreign loan from a substrate language, cognate with Latin cēra \"\n              \"and Albanian qiri, and possibly with Lithuanian korys, Latvian kāre»; Etymonline s.v. \"\n              \"cere says κηρός is «of unknown origin, perhaps a non-IE word»; Pokorny has no root \"\n              \"for it. Decisively, Zimmern — the very page Nourai cites — separates the two families: \"\n              \"the Aramaic 'wax' word qērā is a loan FROM Greek κηρός, while the pitch word qīrā \"\n              \"comes from Akkadian. Greek would in any case not take an Akkadian k-word and give it \"\n              \"an -ος nominative with unexplained η.\"),\n  derivation_fa=(\"خودِ واژهٔ یونانی درست است: κηρός «موم» (از هومر به بعد؛ نشانهٔ کوتاهِ «ě» در کتاب \"\n                 \"برای η کشیده نادرست است). اما خاستگاه آن اکدی نیست: ویکی‌واژه به پیروی از بیکس آن را \"\n                 \"وام‌واژه‌ای از زبانِ زیرلایهٔ اروپایی می‌داند، هم‌ریشه با cēra لاتینی و qiri آلبانیایی و \"\n                 \"شاید korys لیتوانیایی؛ اتیمانلاین نیز آن را «با خاستگاه نامعلوم، احتمالاً غیرهندواروپایی» \"\n                 \"می‌خواند و پوکورنی برای آن ریشه‌ای ندارد. مهم‌تر آنکه تسیمرن — همان مأخذی که نورایی \"\n                 \"به آن ارجاع می‌دهد — در پانوشت صفحهٔ ۶۱ صریحاً واژهٔ آرامیِ «موم» (وام از یونانی) را از \"\n                 \"واژهٔ اکدیِ «قیر» جدا می‌کند. پس این پیوند را پژوهش امروزی رد می‌کند.\"),\n  sources=[W_KEROS, E_KEROSENE],\n  ref_check=[dict(ref=\"AHD:718\", status=\"not_checked\", note=(\"AHD:718 is a page of the 1975 New College dictionary body (around the K entries), not of the \"\n             \"IE-roots appendix; only the appendix (Watkins 1985) is on disk and it has no entry for kēros, \"\n             \"correctly, since the word is not Indo-European. The online AHD gives κηρός only inside the \"\n             \"kerosene/cere entries, with no Semitic source.\"))],\n  consulted=[\n    dict(src=\"POK\", where=\"IEW, searched for κηρός / 'Wachs'\", stance=\"silent\",\n         note=\"grep of POK_full.txt for κηρός, kēros and Wachs-as-headword finds no root — Pokorny sets up no IE etymon, consistent with a substrate word.\"),\n    dict(src=\"AHD\", where=\"Watkins 1985\", stance=\"silent\", note=\"no IE root for 'wax'; kēros appears in no root article.\"),\n    dict(src=\"AKD\", where=\"Zimmern p. 61 n. 3\", stance=\"contradicts\",\n         note=\"«Jedenfalls zu trennen von jüd.-aram. qērā Wachs < griech. κηρός» — Zimmern makes Greek the SOURCE of the Aramaic wax word and separates it from the Akkadian pitch word; he nowhere derives κηρός from Akkadian.\"),\n    dict(src=\"SYN\", where=\"Buck, Dictionary of Selected Synonyms\", stance=\"silent\", note=\"no 'wax' article bearing on the origin of κηρός was found in SYN.txt.\"),\n  ]),\n dict(\n  id=6, lang=\"Aramaic\", words=\"qîra\", verdict=\"disputed\",\n  derivation=(\"Aramaic/Syriac qīrā ܩܝܪܐ is genuine, but the chart merges two homonyms and reverses the \"\n              \"arrow. (a) Syriac/Jewish-Aramaic qīrā 'asphalt, pitch, bitumen' comes from Akkadian \"\n              \"qīru 'bitumen' — Zimmern (AKD p. 60) connects it with Akkadian kīru 'kiln', «speziell \"\n              \"gerade vom Asphalt-, Pechofen des Schiffers gebraucht», and Wiktionary s.v. قير says \"\n              \"«Borrowed from Aramaic קִירָא/ܩܝܪܐ (qīrā, 'bitumen; wax'), from Akkadian qīru 'bitumen'; \"\n              \"uncertain relation to Ancient Greek κηρός». (b) Jewish-Aramaic qērā 'wax' IS from Greek \"\n              \"κηρός, and Zimmern's footnote insists the two are «jedenfalls zu trennen». So the \"\n              \"'tar' sense reached Aramaic from Akkadian, not from Greek; only the 'wax' sense is Greek.\"),\n  derivation_fa=(\"واژهٔ آرامی/سریانی qīrā ܩܝܪܐ واقعی است، اما نمودار دو هم‌آوا را در هم آمیخته و جهت \"\n                 \"پیکان را وارونه کرده است: qīrā «قیر، زفت» از اکدی qīru «قیر» آمده است — تسیمرن در صفحهٔ \"\n                 \"۶۰ آن را با kīru اکدی «کوره» می‌پیوندد که «به‌ویژه برای کورهٔ قیرِ کشتی‌بان به کار می‌رفته» \"\n                 \"— و ویکی‌واژه نیز همین را می‌گوید. در برابر، qērā آرامی یهودی به معنی «موم» وام از یونانی \"\n                 \"κηρός است و تسیمرن تأکید می‌کند که این دو «به هر روی باید جدا شوند». پس معنی «قیر» از \"\n                 \"اکدی به آرامی رسیده، نه از یونانی؛ ادعای نورایی در این حلقه نادرست است.\"),\n  sources=[W_QIR_AR],\n  ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"Nourai gives no reference for this node; the claim was tested against his own AKD:60 (see consulted) and against Wiktionary.\")],\n  consulted=[\n    dict(src=\"AKD\", where=\"Zimmern, printed p. 60 (leaf 70) and p. 61 n. 3\", stance=\"contradicts\", note=AKD60),\n    dict(src=\"AFA\", where=\"Fraenkel, Die aramäischen Fremdwörter im Arabischen\", stance=\"silent\",\n         note=\"grep of AFA.txt for qir/qār/kittān returns only OCR noise; the relevant page could not be located in the scan.\"),\n    dict(src=\"KLN\", where=\"Klein s.v. kerosene / Kerite\", stance=\"silent\",\n         note=\"Klein derives kerosene from Greek κηρός but says nothing about an Aramaic intermediary.\"),\n  ]),\n dict(\n  id=7, lang=\"Arabic\", words=\"qîr; târ\", verdict=\"transcription_suspect\",\n  derivation=(\"Arabic قِير qīr 'pitch, tar' is right and is exactly what Nourai's cited page gives: \"\n              \"Zimmern (AKD p. 60) writes «syr. und jüd.-aram. qīrā Asphalt, Pech (> arab. qīr und \"\n              \"qār)», and Wiktionary s.v. قير repeats it (Aramaic qīrā < Akkadian qīru). The second \"\n              \"word 'târ' is not Arabic: there is no Arabic تار meaning 'tar'. The printed page (PDF \"\n              \"p. 268, copied to sources/refs/ocr/BOOK/268.png) does read «târ : tar» inside the \"\n              \"Arabic box, so the extraction is faithful and the error is the book's — it stands for \"\n              \"the قار qār that Zimmern names beside qīr (Wiktionary: «قَار qār, alternative form of \"\n              \"قِير qīr»). English 'tar', by contrast, is Germanic (OE teoru, PGmc *terw-), unrelated \"\n              \"to the Semitic word.\"),\n  derivation_fa=(\"عربی «قِیر» درست است و دقیقاً همان است که مأخذ مورد استناد نورایی می‌گوید: تسیمرن در \"\n                 \"صفحهٔ ۶۰ می‌نویسد «سریانی و آرامی یهودی qīrā «قیر، زفت» ← عربی qīr و qār». اما واژهٔ \"\n                 \"دوم، «târ»، عربی نیست؛ در عربی «تار» به معنی قیر وجود ندارد. تصویر صفحهٔ چاپی نشان \"\n                 \"می‌دهد که خودِ کتاب «târ : tar» نوشته است، پس خطای خوانشِ اسکن نیست بلکه خطای چاپی \"\n                 \"کتاب است و صورت درست «قار» qār است — همان که تسیمرن در کنار qīr آورده. واژهٔ انگلیسی \"\n                 \"tar نیز ژرمنی است (انگلیسی کهن teoru) و ربطی به این خانواده ندارد.\"),\n  error_in=\"book\", book_prints=\"târ : tar\", correct_form=\"qâr «قار»\",\n  sources=[W_QIR_AR, W_QAR, E_TAR],\n  ref_check=[dict(ref=\"AKD:60\", status=\"supports\", note=AKD60 + \" — supports qīr (and shows that the second Arabic word should be qār, not târ), but glosses Akkadian kīru as 'Ofen (kiln)', not 'wax'.\")],\n  consulted=[\n    dict(src=\"KLN\", where=\"Klein, searched for qir/qar\", stance=\"silent\", note=\"Klein's English dictionary has no entry for the Arabic word.\"),\n    dict(src=\"FVQ\", where=\"Jeffery, Foreign Vocabulary of the Qur'an\", stance=\"silent\", note=\"grep of FVQ_pages.txt for qīr/qir finds no entry — the word is not Qur'anic.\"),\n    dict(src=\"AFM\", where=\"Addi Shir, al-Alfaz al-Farisiyya al-Mu'arraba\", stance=\"silent\", note=\"grep of AFM_pages.txt for قير returns only unrelated words (فقير، قصير); Addi Shir lists Persian loans in Arabic, and qīr is Aramaic, not Persian.\"),\n  ]),\n dict(\n  id=8, lang=\"Persian\", words=\"qîr «قیر»\", verdict=\"confirmed\",\n  derivation=(\"Persian قیر qīr 'pitch, tar, bitumen' is a loan from Arabic قير qīr, which came from \"\n              \"Aramaic/Syriac qīrā and ultimately from Akkadian qīru 'bitumen' — the direct route \"\n              \"Nourai draws for the last two links. Dehkhoda labels the word «(معرب، اِ)» = an \"\n              \"Arabicised form, and Mo'in «[ع.]» = Arabic. Borhan-e Qate' p. 1550 (the page Nourai \"\n              \"cites) has قیر «روغنی باشد سیاه … و صنفی هم هست سیاه و چسبنده که بر کشتی و جهاز مالند» \"\n              \"with Mo'in's footnote 5 «از یونانی kēros (شمع)» — Mo'in prefers the Greek route, a \"\n              \"minority view against Zimmern's and Wiktionary's Akkadian one, but either way the \"\n              \"Persian word is a Semitic-mediated loan, not inherited Iranian.\"),\n  derivation_fa=(\"«قیر» فارسی وام‌واژه‌ای است از عربی «قِیر» که خود از آرامی/سریانی qīrā و در نهایت از \"\n                 \"اکدی qīru «قیر» گرفته شده است. دهخدا آن را «(معرب، اِ)» و معین «[ع.]» نشانه‌گذاری \"\n                 \"می‌کنند. برهان قاطع در همان صفحهٔ ۱۵۵۰ که نورایی به آن ارجاع می‌دهد مدخل «قیر» را دارد \"\n                 \"و معین در حاشیهٔ ۵ می‌نویسد «از یونانی kēros (شمع)»؛ یعنی معین راه یونانی را می‌پسندد، \"\n                 \"برخلاف تسیمرن و ویکی‌واژه که راه اکدی را ترجیح می‌دهند. به هر روی «قیر» واژه‌ای ایرانی \"\n                 \"و موروثی نیست، بلکه از راه سامی به فارسی رسیده است. ادعای نورایی در این حلقه درست است.\"),\n  sources=[A_QIR, W_QIR_AR],\n  ref_check=[\n    dict(ref=\"MON:2765\", status=\"supports\", note=\"Mo'in, Farhang-e Farsi s.v. قیر (read via abadis.ir, section فرهنگ معین): «[ع.] (اِ.) جسم جامد یا نیمه جامد به رنگ سیاه مایل به قهوه‌ای که چسبنده است» — the «[ع.]» label marks it as an Arabic loan, exactly Nourai's arrow.\"),\n    dict(ref=\"BQT:1550\", status=\"supports\", note=\"ref_page.py BQT:1550 (BQT_v3_picofile.pdf p. 343) is indeed the قیر page: «قیر ـ بروزن هیر، روغنی باشد سیاه … که بر کشتی و جهاز مالند تا آب بدرون کشتی نرود»; Mo'in's footnote 5: «از یونانی kēros (شمع)، اهل مغرب شمع را قیر نامند … قار، زفت «دزی ج ۲ ص ۴۸۳»». The same page also carries Borhan's «قیرس ـ لغتی است یونانی بمعنی موم که بعربی شمع گویند».\"),\n  ],\n  consulted=[\n    dict(src=\"HRN\", where=\"Horn, Grundriss der neupersischen Etymologie\", stance=\"silent\", note=\"grep of HRN.txt for qīr/Pech/Asphalt finds no entry — Horn treats inherited Iranian vocabulary, not Semitic loans.\"),\n    dict(src=\"HUB\", where=\"Hübschmann, Persische Studien\", stance=\"silent\", note=\"grep of HUB.txt finds only the unrelated Armenian naft 'Erdpech' discussion (line 3583); قیر is not treated.\"),\n    dict(src=\"MON\", where=\"Mo'in s.v. قیر\", stance=\"supports\", note=\"see ref_check MON:2765.\"),\n    dict(src=\"ARY\", where=\"ARY_pages.txt\", stance=\"silent\", note=\"Aryanpur's IE-roots dictionary has no قیر article (the single hit at line 7719 is an unrelated footnote under the *dyeu- 'day' entry).\"),\n  ]),\n dict(\n  id=9, lang=\"English\", words=\"kerosene\", verdict=\"plausible\",\n  derivation=(\"Kerosene was coined in 1852–54 by the Canadian geologist Abraham Gesner (1797–1864), \"\n              \"who had learned to distil illuminating oil from bitumen and coal: Greek κηρός 'wax' \"\n              \"(the distillate contains paraffin wax) plus the chemical suffix -ene, an irregular \"\n              \"formation. Klein p. 843 (the page Nourai cites) has «kerosene, n., an illuminating \"\n              \"oil. — Formed with suff. -ene fr. Gk. κηρός, 'wax'», and Etymonline dates it 1852. \"\n              \"The English word is therefore correctly attached to Greek κηρός — but the chart draws \"\n              \"it straight from the Akkadian root box, and the Akkadian source of κηρός is itself \"\n              \"rejected by modern scholarship (node #5), so the arrow as drawn overshoots.\"),\n  derivation_fa=(\"«کروسین/نفت سفید» (kerosene) را در ۱۸۵۲–۱۸۵۴ م. آبراهام گِسنر، زمین‌شناس کانادایی، \"\n                 \"ساخت: یونانی κηρός «موم» (زیرا این فراورده پارافین دارد) به‌علاوهٔ پسوند شیمیایی -ene. \"\n                 \"کلاین در همان صفحهٔ ۸۴۳ که نورایی یاد می‌کند می‌نویسد: «kerosene … formed with suff. \"\n                 \"-ene fr. Gk. κηρός, 'wax'». پس پیوند انگلیسی با یونانی درست است؛ ولی نمودار این واژه را \"\n                 \"یکراست از خانهٔ ریشهٔ اکدی می‌کشد، حال آنکه اکدی‌بودنِ خودِ κηρός پذیرفته نیست (بند ۵). \"\n                 \"بنابراین این حلقه با احتیاط پذیرفتنی است.\"),\n  sources=[E_KEROSENE],\n  ref_check=[dict(ref=\"KLN:843\", status=\"supports\", note=\"KLN_1966.txt, page marker '843' at line 20594, entry at line 20628: «kerosene, n., an illuminating oil. — Formed with suff. -ene fr. Gk. κηρός, 'wax'. See cere, n., and cp. Kerite.» — page number exactly right.\")],\n  consulted=[\n    dict(src=\"KLN\", where=\"KLN_1966.txt p. 843 s.v. kerosene\", stance=\"supports\", note=\"see ref_check.\"),\n    dict(src=\"SKT\", where=\"Skeat, Concise Etymological Dictionary\", stance=\"silent\", note=\"grep of SKT.txt finds no kerosene entry (the word post-dates much of Skeat's core vocabulary).\"),\n    dict(src=\"AHD\", where=\"Watkins 1985\", stance=\"silent\", note=\"no IE root; kerosene is a modern learned coinage from a non-IE Greek word.\"),\n  ]),\n]\n\nentries.append(dict(\n  entry=0,\n  root=\"Kîru\",\n  verdict=\"disputed\",\n  modern_form=\"Akkadian kīru 'kiln, (pitch-)oven' (< Sumerian gir) / Akkadian qīru 'bitumen, pitch' — not 'wax'\",\n  note=(\"Nourai's own citation refutes his gloss. Zimmern, Akkadische Fremdwörter p. 60, glosses \"\n        \"akk. kīru as 'Ofen' (kiln) — it is the shipwright's pitch-oven — and derives from it \"\n        \"Syriac/Jewish-Aramaic qīrā 'asphalt, pitch' > Arabic qīr and qār; Wiktionary s.v. قير makes \"\n        \"Arabic qīr a loan from Aramaic qīrā < Akkadian qīru 'bitumen', 'likely ultimately related to \"\n        \"Akkadian kīru \\\"kiln\\\" from Sumerian gir'. The word never means 'wax'. The Greek/Latin \"\n        \"branch of the chart (kēros, crassus, grease, kerosene) has no Akkadian source at all: κηρός \"\n        \"is a substrate word cognate with Latin cēra, and Zimmern explicitly separates the Greek-derived \"\n        \"Aramaic qērā 'wax' from the Akkadian pitch word. What survives is the right-hand tail \"\n        \"Akkadian > Aramaic > Arabic > Persian قیر, which is solid.\"),\n  note_fa=(\"گلوسِ نورایی («موم») را همان مأخذی که خودش یاد می‌کند رد می‌کند: تسیمرن در صفحهٔ ۶۰ کتاب \"\n           \"«وام‌واژه‌های اکدی» واژهٔ اکدی kīru را «کوره» (Ofen) معنی می‌کند — کورهٔ قیرِ کشتی‌سازان — و از آن \"\n           \"سریانی و آرامی یهودی qīrā «قیر، زفت» و سپس عربی qīr و qār را می‌گیرد؛ ویکی‌واژه نیز عربی «قیر» را \"\n           \"وام از آرامی qīrā و آن را از اکدی qīru «قیر» می‌داند و می‌افزاید که این واژه احتمالاً با kīru «کوره» \"\n           \"از سومری gir پیوند دارد. این واژه هرگز معنی «موم» نداشته است. شاخهٔ یونانی–لاتینی نمودار \"\n           \"(κηρός، crassus، grease، kerosene) هیچ خاستگاه اکدی ندارد: κηρός واژه‌ای از زیرلایه است، \"\n           \"هم‌ریشه با cēra لاتینی، و تسیمرن صریحاً qērā «موم» را که وام از یونانی است از واژهٔ اکدیِ قیر جدا \"\n           \"می‌کند. آنچه از این نمودار برجا می‌ماند دنبالهٔ اکدی ← آرامی ← عربی ← فارسی «قیر» است که استوار است.\"),\n  sources=[W_QIR_AR, W_KEROS],\n  ref_check=[dict(ref=\"AKD:60\", status=\"partial\", note=AKD60 + \" — the page really is about this word-family and really does yield Arabic qīr/qār, so the citation is apt; but it glosses Akkadian kīru as 'kiln/oven', not 'wax', and it explicitly excludes the Greek wax word from the chain.\")],\n  consulted=[\n    dict(src=\"AKD\", where=\"Zimmern printed p. 60 (form-feed leaf 70) and p. 61 n. 3\", stance=\"partial\", note=AKD60),\n    dict(src=\"POK\", where=\"IEW\", stance=\"silent\", note=\"an Akkadian root is outside Pokorny; and no IE root is set up for κηρός (see node #5).\"),\n    dict(src=\"KLN\", where=\"Klein s.v. cere, kerosene, crass, grease\", stance=\"contradicts\", note=\"Klein gives κηρός no Semitic source and derives crassus from IE *qerat-; nothing in Klein supports an Akkadian 'wax' etymon.\"),\n  ],\n  nodes=e0_nodes,\n))\n\n# ---------------- entry 2 : Kitu ----------------\nBQT1594 = (\"Borhan-e Qate' ed. Mo'in p. 1594 s.v. کتان, footnote 5 (read from the page image, saved to \"\n           \"data/verification/sources/refs/ocr/BQT/1594.vision.txt): «(عر.) «کتان بالفتح و شدّ التاء…» \"\n           \"«منتهی الارب». این کلمه در زبان اکدی بصورت kitû, kitintu, kitunnû آمده بمعنی (جامهٔ کتانی) و در \"\n           \"زبان عربی و دیگر زبانهای سامی نیز بدین معنی آمده. کلمهٔ اکدی در سریانی بصورت kûtînâ و در حبشی \"\n           \"بصورت kattân داخل‌شده بمعنی: پیراهن یا جامه‌ای از کتان، و کلمه از سریانی وارد عربی شده \"\n           \"«معجمیات عربیه ـ سامیه ص۱۸۶».»\")\n\nKLN1664 = (\"Klein, KLN_1966.txt s.v. tunic (line 40452; nearest page markers 1662 at line 40398 and 1666 at \"\n           \"line 40520, so printed p. 1664 as cited): «tunic, n. … — ME. tunice, tunece, fr. F. tunique, \"\n           \"(or directly) fr. L. tunica, which stands for *ctunica and was borrowed, prob. through the \"\n           \"medium of the Phoenicians, fr. Aram. kittunā, fr. Heb. kuttoneth, 'tunic', whence also Gk. \"\n           \"χιτών. See chiton … For the disappearance of the initial k cp. ptisan.»\")\n\ne2_nodes = [\n dict(\n  id=1, lang=\"Arabic\", words=\"qutun\", verdict=\"plausible\",\n  derivation=(\"Arabic قُطْن quṭn / قُطُن quṭun 'cotton' is a real and very old word, but its link to \"\n              \"Akkadian kitû is contested and its meaning is cotton, not flax. Wiktionary does derive \"\n              \"it from the same Semitic flax-word — «Borrowed from Aramaic כִיתָנָא (kittānā) and its \"\n              \"Classical Syriac equivalent ܟܶܬܳܢܳܐ (kettānā), both meaning 'flax; linen', from which \"\n              \"also Arabic كَتّان (kattān)» — which would make Nourai's arrow right, at the cost of an \"\n              \"irregular k > q and t > ṭ. But AHD files it under a native Semitic root («see qṭn in the \"\n              \"Appendix of Semitic roots»), Etymonline calls it «a word perhaps of Egyptian origin», \"\n              \"and Lokotsch no. 1272 says «Ar. quṭn 'Baumwolle' … selbst Fremdwort, wohl äg. oder ind.». \"\n              \"Hence plausible, not confirmed.\"),\n  derivation_fa=(\"عربی «قُطْن/قُطُن» به معنی پنبه واژه‌ای کهن و اصیل است، اما پیوند آن با kitû اکدی محل \"\n                 \"اختلاف است و معنایش پنبه است نه کتان. ویکی‌واژه آن را وام از آرامی kittānā و سریانی \"\n                 \"kettānā «کتان» می‌داند — همان سرچشمه‌ای که kattān عربی از آن است — که در این صورت پیکان \"\n                 \"نورایی درست می‌شود، هرچند به بهای ابدال‌های نامنظم k>q و t>ṭ. در برابر، فرهنگ American \"\n                 \"Heritage آن را ذیل ریشهٔ سامیِ q-ṭ-n می‌آورد، اتیمانلاین خاستگاهش را «شاید مصری» می‌داند و \"\n                 \"لوکوچ (شمارهٔ ۱۲۷۲) می‌نویسد «خودِ آن وام‌واژه است، احتمالاً مصری یا هندی». پس این حلقه با \"\n                 \"احتیاط پذیرفتنی است.\"),\n  sources=[W_QUTN, E_COTTON, AHD_COTTON],\n  ref_check=[dict(ref=\"BQT:1594\", status=\"partial\", note=BQT1594 + \" — the footnote traces the Akkadian word into Syriac and thence into Arabic as كتّان kattān; it does not mention قطن quṭn at all, so it does not support this particular arrow.\")],\n  consulted=[\n    dict(src=\"LKT\", where=\"Lokotsch no. 1272\", stance=\"partial\",\n         note=\"LKT.txt line 2973: «Ar. quṭn: 'Baumwolle', vulg. koton [selbst Fremdwort, wohl äg. oder ind. …; vgl. hebr. kuttōneṯ, woraus gr. χιτών]» — Lokotsch compares the Hebrew word but calls quṭn itself a foreign word of probably Egyptian or Indian origin.\"),\n    dict(src=\"KLN\", where=\"KLN_1966.txt p. 360 s.v. cotton\", stance=\"partial\",\n         note=\"«fr. Arab. quṭn, whence also It. cotone, OProvenç. coton, Port. cotão, Du. katoen …» — Klein stops at Arabic and gives no Akkadian source.\"),\n    dict(src=\"AHD\", where=\"ahdictionary.com s.v. cotton\", stance=\"contradicts\",\n         note=\"«from Arabic quṭn, quṭun; see qṭn in the Appendix of Semitic roots» — AHD posits a native Semitic root q-ṭ-n, not a loan from kitû.\"),\n  ]),\n dict(\n  id=2, lang=\"Persian\", words=\"katân «کتان»\", verdict=\"disputed\",\n  derivation=(\"Persian کتان katān means FLAX / LINEN, not cotton (that is پنبه), and it comes from \"\n              \"Arabic كَتَّان kattān, not from Arabic quṭn. Wiktionary s.v. کتان: «Borrowed from Arabic \"\n              \"كَتَّان (kattān)», defined 'flax (Linum usitatissimum); linen'; Arabic kattān in turn is \"\n              \"«Borrowed from Classical Syriac ܟܶܬܳܢܳܐ (kettānā, 'flax; linen')», which is the Akkadian \"\n              \"kitû word — exactly the route Mo'in's own footnote on the page Nourai cites lays out \"\n              \"(«کلمهٔ اکدی در سریانی بصورت kûtînâ … داخل شده … و کلمه از سریانی وارد عربی شده»). So the \"\n              \"Persian word does descend from the Akkadian root, but through Arabic kattān; the parent \"\n              \"box (quṭn) and the gloss ('cotton') are both wrong. Mo'in's dictionary entry likewise \"\n              \"defines کتان as «گیاهی است از تیرهٔ کتانیان» — the flax plant.\"),\n  derivation_fa=(\"«کتان» فارسی به معنی گیاه و پارچهٔ کتان است، نه پنبه (که «پنبه» است)، و از عربی «کَتّان» \"\n                 \"گرفته شده، نه از «قُطْن». ویکی‌واژه می‌نویسد «وام از عربی كَتَّان» و خودِ kattān عربی را «وام از \"\n                 \"سریانی کلاسیک ܟܶܬܳܢܳܐ (kettānā) «کتان»» می‌داند — یعنی همان واژهٔ اکدی. این دقیقاً همان راهی \"\n                 \"است که معین در حاشیهٔ همان صفحهٔ ۱۵۹۴ که نورایی به آن ارجاع می‌دهد ترسیم کرده است: «کلمهٔ \"\n                 \"اکدی در سریانی بصورت kûtînâ … داخل شده … و کلمه از سریانی وارد عربی شده». پس واژهٔ فارسی \"\n                 \"به‌راستی از ریشهٔ اکدی می‌آید، اما از راه «کتّان» عربی؛ هم خانهٔ پدرِ نمودار (qutun) نادرست \"\n                 \"است و هم معنی «cotton». معین نیز کتان را «گیاهی از تیرهٔ کتانیان» تعریف می‌کند.\"),\n  sources=[W_KATAN_FA, W_KATTAN],\n  ref_check=[\n    dict(ref=\"BQT:1594\", status=\"partial\", note=BQT1594 + \" — supports the Akkadian ancestry of Persian کتان and its Syriac > Arabic route, but through kattān, not quṭn; and it makes the word mean flax/linen (جامهٔ کتانی), not cotton.\"),\n    dict(ref=\"MON:3543\", status=\"supports\", note=\"Mo'in, Farhang-e Farsi (MON_part2.txt line 20701) s.v. کتان: «[ع.] (اِ.) (گیا.) گیاهی است از تیرهٔ کتانیان …» — an Arabic loan naming the flax plant, confirming the word and the Arabic source but not the gloss 'cotton'.\"),\n  ],\n  consulted=[\n    dict(src=\"MON\", where=\"MON_part2.txt line 20701 s.v. کتان\", stance=\"partial\", note=\"see ref_check MON:3543 — «[ع.]» = Arabic loan, glossed as the flax plant.\"),\n    dict(src=\"BQT\", where=\"BQT p. 1594 main text and Mo'in's footnote 5\", stance=\"partial\", note=BQT1594),\n    dict(src=\"HRN\", where=\"Horn, Grundriss\", stance=\"silent\", note=\"grep of HRN.txt for katân/kattân finds nothing — Horn covers inherited Iranian words, not Arabic loans.\"),\n    dict(src=\"ARY\", where=\"ARY_pages.txt\", stance=\"silent\", note=\"grep for کتان in Aryanpur returns no article.\"),\n  ]),\n dict(\n  id=3, lang=\"Spanish\", words=\"coton\", verdict=\"plausible\",\n  derivation=(\"Old Spanish had both algodón (with the Arabic article, al-quṭn) and a shorter coton; \"\n              \"Klein p. 360 and Skeat both route the English word «F. coton, fr. Sp. coton, fr. Arab. \"\n              \"quṭn», which is Nourai's line. But the reference he cites for it, AHD, says something \"\n              \"else: «Middle English cotoun, from Old French coton, from Old Italian cotone, from \"\n              \"Arabic quṭn, quṭun», and Etymonline hedges — «from Old French coton (12c.), ultimately \"\n              \"(via Provençal, Italian, or Old Spanish) from Arabic qutn». The Spanish step is one of \"\n              \"three competing intermediaries, so the node is plausible rather than confirmed.\"),\n  derivation_fa=(\"در اسپانیایی کهن هم algodón (با حرف تعریف عربی، al-quṭn) بود و هم صورت کوتاه coton. \"\n                 \"کلاین (ص ۳۶۰) و اسکیت هر دو راهِ «فرانسوی coton ← اسپانیایی coton ← عربی quṭn» را \"\n                 \"می‌دهند که همان خط نورایی است. اما مأخذی که نورایی برای این حلقه یاد می‌کند، یعنی AHD، \"\n                 \"چیز دیگری می‌گوید: «از فرانسوی کهن coton، از ایتالیایی کهن cotone، از عربی quṭn»؛ \"\n                 \"اتیمانلاین نیز می‌گوید «از راه پرووانسی، ایتالیایی یا اسپانیایی کهن». پس واسطهٔ اسپانیایی \"\n                 \"یکی از سه گزینه است و این حلقه با احتیاط پذیرفتنی است.\"),\n  sources=[E_COTTON, AHD_COTTON],\n  ref_check=[dict(ref=\"AHD\", status=\"contradicts\", note=\"ahdictionary.com s.v. cotton: «[Middle English cotoun, from Old French coton, from Old Italian cotone, from Arabic quṭn, quṭun…]» — AHD makes the intermediary Old Italian, not Spanish, so the reference Nourai cites does not support the Spanish box.\")],\n  consulted=[\n    dict(src=\"KLN\", where=\"KLN_1966.txt p. 360 s.v. cotton\", stance=\"supports\", note=\"«cotton, n. — ME. coton, fr. F. coton, fr. Sp. coton, fr. Arab. quṭn» — Klein does have the Spanish step.\"),\n    dict(src=\"SKT\", where=\"SKT.txt line 4174 s.v. Cotton\", stance=\"supports\", note=\"«Cotton … (F.—Span.—Arab.) M.E. cotoun … F. coton. — Span. coton, algodon 'cotton' (where al- is the Arab. art.). — Arab. quṭn, quṭun».\"),\n    dict(src=\"LKT\", where=\"Lokotsch no. 1272\", stance=\"partial\", note=\"lists «it. cotone, sp. algodón, pg. algodão, frz. coton» side by side without making Spanish the source of French.\"),\n  ]),\n dict(\n  id=4, lang=\"French\", words=\"coton\", verdict=\"confirmed\",\n  derivation=(\"Old French coton is attested from the 12th century (Marco Polo-era trade texts and \"\n              \"earlier), taken from the Ibero- or Italo-Romance form of Arabic quṭn during the \"\n              \"Mediterranean cloth trade; it is the immediate source of Middle English coton. Klein \"\n              \"and Etymonline agree on this link, which is uncontroversial.\"),\n  derivation_fa=(\"«coton» فرانسوی کهن از سدهٔ دوازدهم میلادی گواهی شده و از صورت‌های رومیایی ایبری یا \"\n                 \"ایتالیایی واژهٔ عربی quṭn در جریان تجارت پارچه در مدیترانه گرفته شده است؛ همین صورت \"\n                 \"سرچشمهٔ بی‌واسطهٔ coton انگلیسی میانه است. کلاین و اتیمانلاین در این حلقه هم‌داستان‌اند و \"\n                 \"مناقشه‌ای در آن نیست.\"),\n  sources=[E_COTTON],\n  ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"no reference given by Nourai for this box; checked against Klein p. 360 and Etymonline (see consulted).\")],\n  consulted=[\n    dict(src=\"KLN\", where=\"KLN_1966.txt p. 360 s.v. cotton\", stance=\"supports\", note=\"«ME. coton, fr. F. coton».\"),\n    dict(src=\"SKT\", where=\"SKT.txt line 4174\", stance=\"supports\", note=\"«M.E. cotoun … F. coton».\"),\n  ]),\n dict(\n  id=5, lang=\"English\", words=\"cotton\", verdict=\"confirmed\",\n  derivation=(\"Middle English coton/cotoun, late 13th century, 'white fibrous substance containing the \"\n              \"seeds of the cotton plant', from Old French coton; the sense 'cloth made of cotton' \"\n              \"follows in the early 15th century. Klein p. 360 (the page Nourai cites) has exactly \"\n              \"this, as does Etymonline.\"),\n  derivation_fa=(\"انگلیسی cotton از انگلیسی میانهٔ coton/cotoun (اواخر سدهٔ سیزدهم) است، از فرانسوی کهن \"\n                 \"coton؛ معنی «پارچهٔ پنبه‌ای» از آغاز سدهٔ پانزدهم پیدا شده است. کلاین در همان صفحهٔ ۳۶۰ که \"\n                 \"نورایی یاد می‌کند دقیقاً همین را می‌گوید و اتیمانلاین نیز همین‌گونه. ادعای نورایی درست است.\"),\n  sources=[E_COTTON],\n  ref_check=[dict(ref=\"KLN:360\", status=\"supports\", note=\"KLN_1966.txt: page marker '360' at line 9368, entry at line 9386: «cotton, n. — ME. coton, fr. F. coton, fr. Sp. coton, fr. Arab. quṭn, whence also It. cotone, OProvenç. coton, Port. cotão, Du. katoen, and (through the medium of Dutch) G. Kattun» — page number exactly right.\")],\n  consulted=[\n    dict(src=\"KLN\", where=\"KLN_1966.txt p. 360\", stance=\"supports\", note=\"see ref_check.\"),\n    dict(src=\"SKT\", where=\"SKT.txt line 4174\", stance=\"supports\", note=\"same chain.\"),\n    dict(src=\"FSD\", where=\"Funk & Wagnalls\", stance=\"silent\", note=\"the DLI scans could not be searched for this word (OCR of the C volume is too degraded to locate the entry).\"),\n  ]),\n dict(\n  id=6, lang=\"Hebrew\", words=\"kuttoneth\", verdict=\"plausible\",\n  derivation=(\"Hebrew כֻּתֹּנֶת kuttṓneṯ is real — it is the word for the 'coat' of Genesis 37:3, the \"\n              \"kətōneṯ passīm — but it means a TUNIC of linen, not 'cotton clothing'. It belongs to the \"\n              \"Northwest Semitic flax family (Aramaic kittānā 'flax', Syriac kettānā, Akkadian kitûm \"\n              \"'flax' < Sumerian gada), so the arrow from the Akkadian root box is right in substance. \"\n              \"Klein p. 1664 and Etymonline both cite it in exactly this position. Modern treatments, \"\n              \"though, do not make Hebrew the source of the Aramaic form (node #7) but treat the two as \"\n              \"parallel reflexes of the same borrowed flax-word.\"),\n  derivation_fa=(\"عبری «כֻּתֹּנֶת» (kuttōneṯ) واژه‌ای واقعی است — همان «جامه»ای که در سفر پیدایش ۳۷:۳ آمده \"\n                 \"(kətōneṯ passīm) — اما به معنی پیراهنِ کتانی است، نه «جامهٔ پنبه‌ای». این واژه از خانوادهٔ \"\n                 \"سامیِ شمال‌غربیِ «کتان» است (آرامی kittānā، سریانی kettānā، اکدی kitûm از سومری gada)، پس \"\n                 \"پیکانی که نورایی از خانهٔ ریشهٔ اکدی می‌کشد در اصل درست است. کلاین (ص ۱۶۶۴) و اتیمانلاین نیز \"\n                 \"همین جایگاه را برای آن قائل‌اند. با این همه، پژوهش امروزی عبری را سرچشمهٔ صورت آرامی \"\n                 \"نمی‌داند، بلکه هر دو را بازتاب‌های موازیِ یک وام‌واژهٔ واحد می‌شمارد. تنها ایراد جدی، معنیِ \"\n                 \"«پنبه‌ای» است که نادرست است.\"),\n  sources=[W_TUNICA, E_TUNIC],\n  ref_check=[dict(ref=\"KLN:1664\", status=\"supports\", note=KLN1664 + \" — Klein does put Heb. kuttoneth at the head of the chain, as Nourai draws it (Klein's chiton entry, p. 277, adds «Akkad. kitinnu, 'linen', Akkad. kitintu, 'linen garment'» — note LINEN).\")],\n  consulted=[\n    dict(src=\"KLN\", where=\"KLN_1966.txt p. 277 s.v. chiton and p. 1664 s.v. tunic\", stance=\"supports\",\n         note=\"«borrowed — through the medium of the Phoenicians — from the Semites. Cp. Heb. kuttōneth, Aram. kittanā, Arab. kattān, Akkad. kitinnu, 'linen', Akkad. kitintu, 'linen garment'.»\"),\n    dict(src=\"FVQ\", where=\"Jeffery\", stance=\"silent\", note=\"grep of FVQ_pages.txt finds no kattān/kuttoneth entry; the word is not among the Qur'anic foreign vocabulary Jeffery treats.\"),\n    dict(src=\"LKT\", where=\"Lokotsch no. 1272\", stance=\"partial\", note=\"«vgl. hebr. kuttōneṯ, woraus gr. χιτών» — Lokotsch makes Hebrew the source of Greek, as Nourai's branch does.\"),\n  ]),\n dict(\n  id=7, lang=\"Aramaic\", words=\"kittunâ\", verdict=\"plausible\",\n  derivation=(\"Aramaic כִּיתּוּנָא kittōnā / Syriac ܟܘܬܝܢܐ kuttīnā, kottīnā 'tunic' is well attested, and it \"\n              \"is the immediate donor of Latin tunica and (with Greek) of χιτών. Klein p. 1664 derives \"\n              \"it from Hebrew kuttoneth exactly as the chart does. Wiktionary, however, treats the \"\n              \"Aramaic 'tunic' word and the Hebrew one as parallel derivatives of the Aramaic flax-word \"\n              \"kittānā (< Akkadian kitûm < Sumerian gada) rather than as mother and daughter, so the \"\n              \"Hebrew > Aramaic direction is Klein's, not the current consensus. The form and meaning \"\n              \"themselves are right; only the internal Semitic direction is uncertain.\"),\n  derivation_fa=(\"آرامی «כִּיתּוּנָא» (kittōnā) و سریانی ܟܘܬܝܢܐ (kuttīnā) به معنی «پیراهن» به‌خوبی گواهی شده و \"\n                 \"همان صورتی است که lat. tunica و (در کنار یونانی) χιτών از آن برآمده‌اند. کلاین در ص ۱۶۶۴ \"\n                 \"آن را دقیقاً مانند نمودار از عبری kuttoneth می‌گیرد. اما ویکی‌واژه واژهٔ آرامیِ «پیراهن» و \"\n                 \"واژهٔ عبری را دو بازتاب موازی از واژهٔ آرامیِ kittānā «کتان» (از اکدی kitûm و سومری gada) \"\n                 \"می‌داند، نه مادر و دختر. پس صورت و معنی درست است و تنها جهتِ درون‌سامیِ وام‌گیری مورد \"\n                 \"تردید است.\"),\n  sources=[W_TUNICA, W_QUTN],\n  ref_check=[dict(ref=\"KLN:1664\", status=\"supports\", note=KLN1664 + \" — «fr. Aram. kittunā, fr. Heb. kuttoneth», Nourai's exact arrow.\")],\n  consulted=[\n    dict(src=\"KLN\", where=\"KLN_1966.txt p. 1664 s.v. tunic\", stance=\"supports\", note=\"see ref_check.\"),\n    dict(src=\"AFA\", where=\"Fraenkel, Die aramäischen Fremdwörter im Arabischen\", stance=\"silent\", note=\"grep of AFA.txt for kittān/kittunā returns only OCR noise; the entry could not be located in the scan.\"),\n    dict(src=\"KLN\", where=\"KLN_1966.txt p. 277 s.v. chiton\", stance=\"supports\", note=\"«Cp. Heb. kuttōneth, Aram. kittanā …».\"),\n  ]),\n dict(\n  id=8, lang=\"Latin\", words=\"ctunica, tunica\", verdict=\"confirmed\",\n  derivation=(\"Latin tunica 'undergarment worn by either sex' is a Semitic loan, taken (Klein and \"\n              \"Etymonline agree, probably through Phoenician traders) from Aramaic kittunā. Klein \"\n              \"reconstructs an intermediate *ctunica to explain the loss of the initial k- («For the \"\n              \"disappearance of the initial k cp. ptisan») — the chart's 'ctunica' is that \"\n              \"reconstruction and should carry an asterisk; it is not an attested Latin word. The gloss \"\n              \"'cotton clothing' is again wrong: tunica is a linen undergarment. Wiktionary adds that \"\n              \"the Latin form shows a metathesis relative to Greek χιτών.\"),\n  derivation_fa=(\"لاتینی tunica «جامهٔ زیرین» وام‌واژه‌ای سامی است که — به گفتهٔ کلاین و اتیمانلاین، احتمالاً \"\n                 \"از راه بازرگانان فنیقی — از آرامی kittunā گرفته شده است. کلاین برای توضیح افتادن کافِ \"\n                 \"آغازین صورت میانی *ctunica را بازسازی می‌کند («برای افتادن k آغازین ptisan را بسنجید»)؛ \"\n                 \"پس «ctunica»ی نمودار همان صورت بازسازی‌شده است و باید ستاره داشته باشد، چون واژه‌ای \"\n                 \"گواهی‌شده در لاتینی نیست. معنیِ «جامهٔ پنبه‌ای» نیز نادرست است: tunica جامهٔ زیرینِ کتانی \"\n                 \"است. ویکی‌واژه می‌افزاید که صورت لاتینی نسبت به χιτών یونانی قلب (metathesis) نشان می‌دهد. \"\n                 \"جز این دو نکته، ادعای نورایی درست است.\"),\n  sources=[W_TUNICA, E_TUNIC],\n  ref_check=[dict(ref=\"KLN:1664\", status=\"supports\", note=KLN1664)],\n  consulted=[\n    dict(src=\"KLN\", where=\"KLN_1966.txt p. 1664 s.v. tunic\", stance=\"supports\", note=\"see ref_check — Klein gives both *ctunica and the Aramaic source.\"),\n    dict(src=\"LAT\", where=\"Ernout–Meillet, LAT.txt (tunica passim, e.g. lines 12326, 29774, 32521)\", stance=\"silent\",\n         note=\"the OCR of the tunica headword itself is not recoverable in LAT.txt; only citations of the word in other articles appear, so Ernout–Meillet could not be made to speak on the etymology.\"),\n    dict(src=\"SKT\", where=\"SKT.txt line 20293 s.v. Tunic\", stance=\"partial\",\n         note=\"«Tunic. (L.) A.S. tunece — L. tunica, an under-garment.» — Skeat stops at Latin and offers no Semitic source.\"),\n  ]),\n dict(\n  id=9, lang=\"Persian\", words=\"tonekeh «تُنکه»\", verdict=\"disputed\",\n  derivation=(\"Persian تنکه tonoke is not from Latin tunica. It is a native formation from تنک tonok \"\n              \"'thin, flimsy' plus the noun/adjective suffix ـه -e — Wiktionary s.v. تنکه: «From تنک \"\n              \"(tonok, 'thin, flimsy') + ـه (-e)», with the Classical Persian reading /tu.nu.ˈka/. \"\n              \"Nourai's own NOTE on the chart concedes as much («'tonekeh' is probably from 'tonok: \"\n              \"thin, soft'. See root 'Ten 1'»), so he is arguing against his own arrow. Mo'in (the page \"\n              \"cited) gives «(تُ نُ کِ یا کَ) (اِ.) ۱- شلوار کوتاه که تا سر زانو باشد ۲- شلوار کوتاه زنانه \"\n              \"یا مردانه» with no foreign-language label at all — and Mo'in does label loans (compare \"\n              \"his «[ع.]» on قیر and «[فر.]» on تونیک). There is no phonetic route from tunica to \"\n              \"tonoke that would preserve the -k-.\"),\n  derivation_fa=(\"«تُنکه» از tunica لاتینی نیست. ساختی است فارسی از «تنک» (نازک، سست) به‌علاوهٔ پسوند «ـه»؛ \"\n                 \"ویکی‌واژه می‌نویسد «از تنک + ـه» و تلفظ فارسی کلاسیک را /tu.nu.ˈka/ می‌دهد. خودِ نورایی نیز \"\n                 \"در یادداشت نمودار همین را می‌پذیرد («احتمالاً از tonok: نازک، نرم؛ نگاه کنید به ریشهٔ Ten 1»)، \"\n                 \"یعنی در برابر پیکان خودش استدلال می‌کند. معین در همان صفحه‌ای که یاد شده هیچ نشانِ \"\n                 \"زبان بیگانه نمی‌گذارد («(تُ نُ کِ یا کَ) (اِ.) ۱ـ شلوار کوتاه که تا سر زانو باشد…») حال آنکه \"\n                 \"او وام‌واژه‌ها را نشانه‌گذاری می‌کند (سنجید «[ع.]» در قیر و «[فر.]» در تونیک). راه آوایی‌ای \"\n                 \"هم از tunica به «تنکه» نیست که کافِ میانی را نگه دارد. پس پژوهش امروزی این پیوند را رد می‌کند.\"),\n  sources=[W_TONAKE, A_TONAKE],\n  ref_check=[dict(ref=\"MON:1154\", status=\"partial\", note=\"Mo'in, Farhang-e Farsi s.v. تنکه (MON_part1.txt line 44296; read also via abadis.ir): «تنبان چرمی که تا سر زانو باشد و کشتی‌گیران وقت کشتی گرفتن پوشند. شلوار کوتاه زنانه. زیر شلواری کوتاه مردانه.» The page supports the word and the gloss 'underwear', but carries no etymology and no foreign-language label, so it does not support the Latin arrow.\")],\n  consulted=[\n    dict(src=\"MON\", where=\"MON_part1.txt line 44296 s.v. تنکه\", stance=\"partial\", note=\"see ref_check — word and gloss confirmed, etymology absent.\"),\n    dict(src=\"BQT\", where=\"Borhan-e Qate' / Dehkhoda's citations from it\", stance=\"partial\",\n         note=\"Dehkhoda s.v. تنکه (quoting غیاث اللغات، آنندراج، ناظم الاطباء) gives «تنبان چرمی که تا سر زانو باشد، وقت کشتی گرفتن پوشند» and the Mirnajat verse «تنکه در قدمش زود ز هم می‌پاشد / هرکه رویش تنک افتاد چنین می‌باشد» — the pun on تنک shows the native association.\"),\n    dict(src=\"HRN\", where=\"Horn, Grundriss\", stance=\"silent\", note=\"no entry for تنکه/تنک in HRN.txt.\"),\n  ]),\n dict(\n  id=10, lang=\"French\", words=\"\", verdict=\"confirmed\",\n  derivation=(\"The empty box is French tunique (12th c.), the learned/semi-learned continuation of \"\n              \"Latin tunica: the Latin form was taken over with the stress-vowel kept and -ica \"\n              \"regularly giving -ique. Etymonline s.v. tunic gives «from Old French tunique (12c.) or \"\n              \"directly from Latin tunica».\"),\n  derivation_fa=(\"این خانهٔ خالی همان «tunique» فرانسوی (سدهٔ دوازدهم) است، دنبالهٔ عالمانهٔ tunica لاتینی: \"\n                 \"واژهٔ لاتینی با نگه‌داشتِ واکهٔ تکیه‌بر وام گرفته شده و پایانهٔ -ica به‌طور منظم -ique شده است. \"\n                 \"اتیمانلاین می‌نویسد «از فرانسوی کهن tunique (سدهٔ ۱۲) یا مستقیماً از لاتینی tunica».\"),\n  sources=[E_TUNIC],\n  ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"no reference given; checked against Klein p. 1664 and Etymonline (see consulted).\")],\n  consulted=[\n    dict(src=\"KLN\", where=\"KLN_1966.txt p. 1664 s.v. tunic\", stance=\"supports\", note=\"«ME. tunice, tunece, fr. F. tunique, (or directly) fr. L. tunica».\"),\n    dict(src=\"SKT\", where=\"SKT.txt line 20293\", stance=\"partial\", note=\"Skeat routes English tunic straight from Latin via A.S. tunece, without the French step.\"),\n  ]),\n dict(\n  id=11, lang=\"English\", words=\"tunic\", verdict=\"confirmed\",\n  derivation=(\"English tunic is attested from the mid-12th century (tunice), from Old French tunique or \"\n              \"directly from Latin tunica; the borrowing replaced Old English tunece, which had been \"\n              \"taken from Latin centuries earlier. Klein p. 1664 and Etymonline agree; the chart's \"\n              \"Latin > French > English route is one of the two Etymonline allows, and the commoner one \"\n              \"for the Middle English form.\"),\n  derivation_fa=(\"انگلیسی tunic از میانهٔ سدهٔ دوازدهم (tunice) گواهی شده، از فرانسوی کهن tunique یا \"\n                 \"مستقیماً از لاتینی tunica؛ این وام‌گیری جایگزین tunece انگلیسی کهن شد که سده‌ها پیش‌تر از \"\n                 \"لاتینی گرفته شده بود. کلاین (ص ۱۶۶۴) و اتیمانلاین هم‌داستان‌اند و راهِ لاتینی ← فرانسوی ← \"\n                 \"انگلیسیِ نمودار یکی از دو راهی است که اتیمانلاین می‌پذیرد. ادعای نورایی درست است.\"),\n  sources=[E_TUNIC],\n  ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"no reference given for this box; checked against Klein p. 1664 and Etymonline (see consulted).\")],\n  consulted=[\n    dict(src=\"KLN\", where=\"KLN_1966.txt p. 1664 s.v. tunic\", stance=\"supports\", note=KLN1664),\n    dict(src=\"SKT\", where=\"SKT.txt line 20293 s.v. Tunic\", stance=\"partial\", note=\"«Tunic. (L.) A.S. tunece — L. tunica, an under-garment.» — Skeat has no French step.\"),\n  ]),\n dict(\n  id=12, lang=\"Persian\", words=\"tonîc «تونیک»\", verdict=\"plausible\",\n  derivation=(\"Persian تونیک tonik 'a long women's blouse worn over trousers or a skirt' is a \"\n              \"20th-century European loan, but Mo'in marks it «[فر.]» — from FRENCH tunique — not from \"\n              \"English tunic: «(تُ) [فر.] (اِ.) ۱- بلوز یا ژاکت کوتاه زنانه تا بالای ران که معمولاً با \"\n              \"شلوار یا دامن پوشیده می‌شود». The Persian shape تونیک with final -k rather than *تونیک/\"\n              \"تونیکْ from French -ique is equally compatible with either donor, but the standard \"\n              \"Persian lexicon assigns it to French, so the chart's English parent is questionable.\"),\n  derivation_fa=(\"«تونیک» وام‌واژه‌ای اروپایی و امروزی است، اما معین آن را با نشان «[فر.]» یعنی از فرانسوی \"\n                 \"tunique می‌آورد، نه از انگلیسی tunic: «(تُ) [فر.] (اِ.) ۱ـ بلوز یا ژاکت کوتاه زنانه تا بالای \"\n                 \"ران که معمولاً با شلوار یا دامن پوشیده می‌شود». صورت فارسی با «ک» پایانی با هر دو زبانِ \"\n                 \"وام‌دهنده سازگار است، ولی چون فرهنگ معیارِ فارسی آن را فرانسوی می‌داند، خانهٔ پدرِ انگلیسیِ \"\n                 \"نمودار محل تردید است. پس با احتیاط پذیرفتنی است.\"),\n  sources=[A_TONIK],\n  ref_check=[dict(ref=\"VOP:154\", status=\"not_checked\", note=\"VOP = Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi (Alborz 1371/1992). refs_online.json records kind 'none': no copy was found on archive.org, ketabnak, noorlib or the open web, so the citation is unverifiable.\")],\n  consulted=[\n    dict(src=\"MON\", where=\"Mo'in, Farhang-e Farsi s.v. تونیک (via abadis.ir)\", stance=\"partial\", note=\"«(تُ) [فر.] (اِ.) ۱- بلوز یا ژاکت کوتاه زنانه…» — the «[فر.]» label makes the donor French, not English.\"),\n    dict(src=\"ARY\", where=\"ARY_pages.txt\", stance=\"silent\", note=\"grep for تونیک finds nothing; Aryanpur covers inherited IE vocabulary, not modern European loans.\"),\n    dict(src=\"BQT\", where=\"Borhan-e Qate'\", stance=\"silent\", note=\"a 20th-century loan cannot appear in a 17th-century dictionary.\"),\n  ]),\n dict(\n  id=13, lang=\"Greek\", words=\"kiton\", verdict=\"transcription_suspect\",\n  derivation=(\"The Greek word is χιτών khitṓn (Ionic κιθών kithṓn) 'tunic, undergarment worn next to \"\n              \"the skin' — a linen shirt, not a 'cotton shirt'. The printed page (PDF p. 268, copied to \"\n              \"sources/refs/ocr/BOOK/268.png) does read «kiton», so the extraction is faithful and the \"\n              \"form is the book's own: 'kiton' matches neither the Attic χ- nor the Ionic -θ-. The \"\n              \"derivation itself is sound: Wiktionary s.v. χιτών says it comes «together with Mycenaean \"\n              \"Greek ki-to and likely Latin tunica from some Central Semitic, as found in Aramaic \"\n              \"kittōnā 'tunic', Hebrew kuttṓneṯ 'tunic', which is derived from the local word for flax \"\n              \"… Akkadian kitûm, Sumerian gada»; Klein (p. 277) notes that χιτών is already in \"\n              \"Mycenaean Greek of the 15th century BCE, borrowed through the Phoenicians.\"),\n  derivation_fa=(\"واژهٔ یونانی χιτών (khitṓn، در گویش ایونی κιθών kithṓn) است به معنی «پیراهنِ زیرین» — \"\n                 \"پیراهنی کتانی، نه «پیراهن پنبه‌ای». تصویر صفحهٔ چاپی نشان می‌دهد که خودِ کتاب «kiton» \"\n                 \"نوشته است، پس خطای خوانشِ اسکن نیست بلکه خطای آوانگاریِ کتاب است: «kiton» نه با χ آتیکی \"\n                 \"می‌خواند و نه با θ ایونی. اما خودِ اشتقاق درست است: ویکی‌واژه می‌نویسد این واژه همراه با \"\n                 \"صورت میسنی ki-to و احتمالاً tunica لاتینی از زبانی سامیِ مرکزی آمده است — آرامی kittōnā، \"\n                 \"عبری kuttōneṯ — که خود از واژهٔ بومیِ «کتان» (اکدی kitûm، سومری gada) گرفته شده؛ کلاین \"\n                 \"نیز یادآور می‌شود که χιτών در یونانی میسنیِ سدهٔ پانزدهم پیش از میلاد گواهی شده و از راه \"\n                 \"فنیقیان وام گرفته شده است.\"),\n  error_in=\"book\", book_prints=\"kiton : cotton shirt\", correct_form=\"khitōn (χιτών), Ion. kithōn (κιθών) 'linen tunic'\",\n  sources=[W_KHITON, E_TUNIC],\n  ref_check=[dict(ref=\"KLN:1664\", status=\"supports\", note=KLN1664 + \" — Klein's tunic entry names Gk. χιτών as the parallel outcome of the same Aramaic/Hebrew word, which is Nourai's arrow; his chiton entry (p. 277) spells out the Semitic source.\")],\n  consulted=[\n    dict(src=\"KLN\", where=\"KLN_1966.txt p. 277 s.v. chiton\", stance=\"supports\",\n         note=\"«chiton, n. … — Gk. χιτών, Ion. κιθών, borrowed — through the medium of the Phoenicians — from the Semites. Cp. Heb. kuttōneth, Aram. kittanā, Arab. kattān, Akkad. kitinnu, 'linen', Akkad. kitintu, 'linen garment'. … χιτών occurs in Mycenaean Greek as early as the 15th century.»\"),\n    dict(src=\"POK\", where=\"IEW\", stance=\"silent\", note=\"no IE root: χιτών is a Semitic loan and Pokorny does not treat it.\"),\n    dict(src=\"SYN\", where=\"Buck 6.28 'LINEN; FLAX'\", stance=\"silent\", note=\"SYN.txt line 9994ff. lists the IE linen words (λίνον, linum, lein) but says nothing about χιτών.\"),\n  ]),\n dict(\n  id=14, lang=\"English\", words=\"chiton\", verdict=\"confirmed\",\n  derivation=(\"English chiton, first used in English archaeology and classical scholarship for the \"\n              \"Greek garment, is a direct learned borrowing of Greek χιτών; the same word underlies \"\n              \"the biochemical term chitin (French chitine, 1836), named because the insect's covering \"\n              \"was likened to a coat. Klein p. 277 gives the Greek etymon and the Semitic background; \"\n              \"the English step is uncontroversial.\"),\n  derivation_fa=(\"انگلیسی chiton وام‌گیری مستقیم و عالمانه از یونانی χιτών است که در باستان‌شناسی و \"\n                 \"مطالعات کلاسیک برای آن جامهٔ یونانی به کار می‌رود؛ همین واژه پایهٔ اصطلاح زیست‌شیمیایی \"\n                 \"chitin (فرانسوی chitine، ۱۸۳۶ م.) نیز هست، چون پوشش سختِ حشره را به جامه تشبیه کرده‌اند. \"\n                 \"کلاین در ص ۲۷۷ ریشهٔ یونانی و پیشینهٔ سامیِ آن را می‌آورد و این حلقه بی‌مناقشه است.\"),\n  sources=[E_TUNIC, W_KHITON],\n  ref_check=[dict(ref=\"AHD:236\", status=\"not_checked\", note=\"AHD:236 is a page of the 1975 New College dictionary body (the 'chi-' entries), not of the IE-roots appendix; only the Watkins appendix is on disk, and it has no article for chiton (correctly — the word is a Semitic loan into Greek, not IE).\")],\n  consulted=[\n    dict(src=\"KLN\", where=\"KLN_1966.txt p. 277 s.v. chiton\", stance=\"supports\", note=\"«chiton, n., a garment worn by both sexes in ancient Greece. — Gk. χιτών, Ion. κιθών, borrowed — through the medium of the Phoenicians — from the Semites.»\"),\n    dict(src=\"SKT\", where=\"SKT.txt\", stance=\"silent\", note=\"grep finds no chiton entry in Skeat's concise dictionary.\"),\n  ]),\n]\n\nentries.append(dict(\n  entry=2,\n  root=\"Kitu, Kitintu, Kitunnŭ\",\n  verdict=\"plausible\",\n  modern_form=\"Akkadian kitû(m), kitinnû, kitintu 'flax, linen; linen garment' (< Sumerian GADA) — 'linen', not 'cotton'\",\n  note=(\"The three Akkadian forms are exactly those printed in Mo'in's footnote on the page Nourai \"\n        \"cites (BQT p. 1594 s.v. کتان), and they are well attested: Wiktionary s.v. tunica and χιτών \"\n        \"gives «Akkadian 𒃰 (kitûm, 'flax'), Sumerian 𒃰 (gada, 'flax'), ultimately a substrate word», \"\n        \"and Klein s.v. chiton has «Akkad. kitinnu, 'linen', Akkad. kitintu, 'linen garment'». The one \"\n        \"systematic error runs through the whole chart: Mo'in's Persian gloss «جامهٔ کتانی» means LINEN \"\n        \"clothing, and Nourai has rendered it 'cotton clothing'. Everything downstream inherits the \"\n        \"mistake — Arabic quṭn 'cotton' is a different Arabic root (q-ṭ-n) from kattān 'flax' (k-t-n), \"\n        \"Persian کتان is flax/linen, Hebrew kuttōneṯ and Latin tunica are linen tunics, and Greek χιτών \"\n        \"is a linen shirt. The Semitic > Greek/Latin branch is otherwise sound and is Klein's own; the \"\n        \"Arabic quṭn branch is the contested one.\"),\n  note_fa=(\"سه صورت اکدیِ ریشه دقیقاً همان‌هایی است که معین در حاشیهٔ صفحهٔ ۱۵۹۴ برهان قاطع (ذیل «کتان») \"\n           \"آورده و به‌خوبی گواهی شده‌اند: ویکی‌واژه ذیل tunica و χιτών می‌نویسد «اکدی kitûm «کتان»، سومری \"\n           \"gada «کتان»، در نهایت واژه‌ای از زیرلایه»، و کلاین ذیل chiton «اکدی kitinnu «کتان»، اکدی \"\n           \"kitintu «جامهٔ کتانی»» دارد. یک خطای سراسری در کل نمودار هست: عبارت فارسیِ معین «جامهٔ کتانی» \"\n           \"یعنی جامهٔ کتان، و نورایی آن را «cotton clothing» (جامهٔ پنبه‌ای) ترجمه کرده است. همهٔ شاخه‌های \"\n           \"پایین‌دست این خطا را به ارث برده‌اند: عربی «قُطْن» (پنبه) از ریشهٔ q-ṭ-n است و «کَتّان» از ریشهٔ \"\n           \"k-t-n؛ «کتان» فارسی هم کتان است نه پنبه؛ kuttōneṯ عبری و tunica لاتینی جامه‌های کتانی‌اند و \"\n           \"χιτών یونانی پیراهن کتانی است. جز این، شاخهٔ سامی ← یونانی/لاتینی استوار است و همان است که \"\n           \"کلاین می‌دهد؛ شاخهٔ عربیِ «قطن» محل مناقشه است.\"),\n  sources=[W_TUNICA, W_KHITON, W_KATTAN],\n  ref_check=[dict(ref=\"BQT:1594\", status=\"supports\", note=BQT1594 + \" — the three Akkadian forms and their transmission through Syriac into Arabic are exactly as Nourai's root box has them; only his English rendering of «جامهٔ کتانی» as 'cotton clothing' departs from the source. (ref_page.py resolves BQT:1594 to BQT_v3_picofile.pdf p. 387; the printed page number on the image matches.)\")],\n  consulted=[\n    dict(src=\"BQT\", where=\"p. 1594, Mo'in's footnote 5 s.v. کتان (image read; saved as ocr/BQT/1594.vision.txt)\", stance=\"supports\", note=BQT1594),\n    dict(src=\"KLN\", where=\"KLN_1966.txt p. 277 s.v. chiton\", stance=\"partial\",\n         note=\"«Cp. Heb. kuttōneth, Aram. kittanā, Arab. kattān, Akkad. kitinnu, 'linen', Akkad. kitintu, 'linen garment'» — same etyma, but glossed LINEN.\"),\n    dict(src=\"LKT\", where=\"Lokotsch no. 1272\", stance=\"partial\", note=\"links Hebrew kuttōneṯ and Greek χιτών to the Arabic cotton word but calls quṭn itself a foreign word of probably Egyptian origin.\"),\n  ],\n  nodes=e2_nodes,\n))\n\nout = dict(pdf_page=268, book_page=238, verified_by=\"claude-opus-5\",\n           verified_on=\"2026-09-06\", entries=entries)\nwith open(\"data/verification/page-268.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk268.py && python3 -m json.tool data/verification/page-268.json > /dev/null && echo \"valid json\" && python3 tools/verify_check.py 268"
}
```


### [2026-09-06T21:08:29.389Z] TOOL RESULT

```
written
valid json
nodes verified: 23/23
node verdicts: {'disputed': 5, 'confirmed': 10, 'transcription_suspect': 2, 'plausible': 6}
root verdicts: {'disputed': 1, 'plausible': 1}
ref checks: {'contradicts': 2, 'not_checked': 10, 'supports': 11, 'partial': 3}
books consulted: {'contradicts': 5, 'partial': 13, 'silent': 29, 'supports': 21} | by book: {'KLN': 17, 'SKT': 10, 'MON': 5, 'AHD': 4, 'BQT': 4, 'ARY': 4, 'POK': 3, 'HRN': 3, 'LKT': 3, 'LAT': 2, 'AKD': 2, 'SYN': 2, 'AFA': 2, 'FVQ': 2, 'IEC': 1, 'WEB': 1, 'AFM': 1, 'HUB': 1, 'FSD': 1}
```


## [2026-09-06T21:08:49.245Z] AGENT

0 PROBLEM lines. Page 268 verification complete.

**Page 268 (book p. 238) — 2 charts, 23 nodes, 3 redirects skipped**

Verdicts: nodes — 10 confirmed, 6 plausible, 5 disputed, 2 transcription_suspect. Roots — 1 disputed (Kîru), 1 plausible (Kitu).

Disputed / flagged:
- **ROOT Kîru "wax"** — Nourai's own source refutes him: Zimmern AKD p. 60 glosses Akkadian *kīru* as **"Ofen" (kiln)** — the shipwright's pitch-oven — and derives from it Aram. *qīrā* 'pitch' > Arab. *qīr, qār*; p. 61 n. 3 explicitly *separates* the Greek-derived Aramaic *qērā* 'wax'. The word never means 'wax'.
- **Kîru #1 Latin crassus/crassia** — Klein (p. 366), Pokorny (IEW 584 *kert-*), Ernout-Meillet and Mann all make it IE/unknown, never Semitic; *crassia* is Vulgar Latin **\***crassia*, not a Latin word.
- **Kîru #5 Greek kěros** — κηρός is a substrate word cognate with Lat. *cēra* (Wiktionary/Beekes, Etymonline "perhaps non-IE"); no Akkadian source.
- **Kîru #6 Aramaic qîra** — the 'tar' sense comes from Akkadian *qīru* directly, not from Greek; the chart merges two homonyms.
- **Kîru #7 Arabic "târ"** — `transcription_suspect`, **error_in: book**. No Arabic تار 'tar'; the page really prints "târ : tar", and it stands for **qâr قار** (the form Zimmern names beside *qīr*).
- **Kitu #2 Persian katân کتان** — means flax/linen, not cotton, and comes from Arabic **كتّان kattān** (< Syriac *kettānā*), not from *quṭn*; this is exactly what Mo'in's footnote on the very page cited (BQT 1594) says.
- **Kitu #9 Persian تنکه tonekeh** — from تنک *tonok* 'thin' + ـه (Wiktionary; Mo'in gives no loan label), as Nourai's own chart NOTE concedes.
- **Kitu #13 Greek "kiton"** — `transcription_suspect`, **error_in: book**. Greek is χιτών / Ion. κιθών; "kiton" is neither, and the gloss should be 'linen tunic'.

Systematic (non-fatal) error across chart 2: Mo'in's «جامهٔ کتانی» = *linen* clothing; Nourai renders it "cotton clothing" throughout, so every gloss in the Kitu tree says cotton where linen is meant.

**No extraction errors** — the JSON matches the printed page everywhere I checked (including all five Persian scripts and the Nezâm Qârî verse).

Artefacts written: `data/verification/page-268.json`; `data/verification/sources/refs/ocr/BQT/1594.vision.txt` (Mo'in's footnote, read from the page image); `data/verification/sources/refs/ocr/BOOK/268.png`; 28 web sources archived via `fetch_source.py`.
