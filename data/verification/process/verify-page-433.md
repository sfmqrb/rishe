# Verification process log — verify-page-433


## [2026-09-14T01:23:11.490Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 433 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-433.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-433.json. Write /home/sfmqrb/git/rishe/data/verification/page-433.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 433` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:23:12.457Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:23:13.249Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:23:13.263Z] TOOL RESULT

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
226	Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
227	file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
228	`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.
229	
230	```json
231	{
232	  "pdf_page": 126,
233	  "book_page": 96,
234	  "verified_by": "claude-opus-5",
235	  "verified_on": "2026-09-05",
236	  "entries": [
237	    {
238	      "entry": 0,
239	      "root": "Dheigh, Dhigha",
240	      "verdict": "confirmed",
241	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
242	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
243	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
244	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
245	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
246	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
247	      "nodes": [
248	        {
249	          "id": 6,
250	          "lang": "Avestan",
251	          "words": "pairi-daeza",
252	          "verdict": "confirmed",
253	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
254	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
255	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
256	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
257	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
258	        }
259	      ]
260	    }
261	  ]
262	}
263	```
264	
265	Rules:
266	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
267	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
268	- `words` = the transliterations of the node joined by "; " (copy from the chart).
269	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
270	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
271	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
272	- If a node lists several words, cover each word; if they differ in verdict, use the worst
273	  verdict for the node and explain per word in `derivation`.
274	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
275	  scholarship takes.
276	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
277	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
278	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
279	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-09-14T01:23:13.777Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-433.txt"
}
```


### [2026-09-14T01:23:13.801Z] TOOL RESULT

```
1	=== PDF page 433 (book page 403) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Sâwel, Sŭ 3 : sun  (refs POK:881)  PART 2
4	#1 (parent #0) [Greek] refs=AHD | alos, helios : sun
5	  #2 (parent #1) [Persian] refs=MON:5091; TAD:75 | hâleh «هاله» : halo, hue
6	  #3 (parent #1) [English] refs=None | helium
7	#4 (parent #0) [Indo-European] refs=POK:1045 | Swel 2 : to shine, burn
8	  #5 (parent #4) [Greek] refs=AHD:611 | heleně : torch ; Heleně : goddess of light
9	    #6 (parent #5) [English] refs=AHD | Helen, Aileen
10	  #7 (parent #4) [Germanic] refs=AHD | swiltan : to perish from heat
11	    #8 (parent #7) [English] refs=AHD | swelter
12	--- entry 1 ---
13	ROOT [Arabic] Šay' : thing  (refs KLN:1756)
14	#1 (parent #0) [Persian] refs=MON; FVA:223 | šey' «شی ء» : thing | extra: اشیاء ، اشیا
15	#2 (parent #0) [Spanish] refs=PRT:813; KLN:1756 | X : a letter sounding "š,sh" used as a short form for the Arabic word "šay`: thing"
16	  #3 (parent #2) [English] refs=KLN:1756 | X : used in mathematics to mean an unknown "thing" ; x-ray : a kind of radiation that was not understood well when named so
17	--- entry 2 ---
18	ROOT [Arabic] S.d.a` : to split  (refs SAP:857; KLN:1468)
19	#1 (parent #0) [Arabic] refs=SAP:857 | sodâ` : a head-splitting headache
20	  #2 (parent #1) [Persian] refs=MON:2137 | sodâ` «صُداع» : headache
21	  #3 (parent #1) [Latin] refs=KLN:1468 | soda : headache ; sodanum : an alkaline used to cure headaches
22	    #4 (parent #3) [English] refs=None | soda ; sodium
23	      #5 (parent #4) [Persian] refs=MON:1947 | sodâ «سودا» : soda water
24	    #6 (parent #3) [French] refs=None | 
25	      #7 (parent #6) [Persian] refs=MON:1847 | sodyom «سدیم» : sodium
26	
```


## [2026-09-14T01:23:15.145Z] AGENT

I'll read the source JSON and reference infrastructure.


## [2026-09-14T01:23:16.557Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-433.json | head -200",
 "description": "Read source JSON page 433"
}
```


### [2026-09-14T01:23:17.727Z] TOOL RESULT

```
{
    "pdf_page": 433,
    "book_page": 403,
    "entries": [
        {
            "root": {
                "name": "S\u00e2wel, S\u016d 3",
                "lang": "Indo-European",
                "refs": "POK:881",
                "gloss": "sun"
            },
            "part": 2,
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Greek",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "alos, helios",
                            "gloss": "sun",
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
                    "lang": "Persian",
                    "refs": "MON:5091; TAD:75",
                    "words": [
                        {
                            "translit": "h\u00e2leh",
                            "gloss": "halo, hue",
                            "script": "\u0647\u0627\u0644\u0647"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": {
                        "text": "\u0645\u0647 \u062f\u0631 \u062d\u0635\u0627\u0631 \u0647\u0627\u0644\u0647 \u0646\u062e\u0648\u0627\u0647\u062f \u0645\u062f\u0627\u0645 \u0645\u0627\u0646\u062f - \u0627\u0632 \u0622\u0633\u0645\u0627\u0646 \u0628\u0631\u0648\u0646 \u062f\u0644 \u0622\u06af\u0627\u0647 \u0645\u06cc\u0631\u0648\u062f",
                        "poet": "S\u00e2eb"
                    }
                },
                {
                    "id": 3,
                    "parent": 1,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "helium",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 0,
                    "lang": "Indo-European",
                    "refs": "POK:1045",
                    "words": [
                        {
                            "translit": "Swel 2",
                            "gloss": "to shine, burn",
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
                    "lang": "Greek",
                    "refs": "AHD:611",
                    "words": [
                        {
                            "translit": "helen\u011b",
                            "gloss": "torch",
                            "script": null
                        },
                        {
                            "translit": "Helen\u011b",
                            "gloss": "goddess of light",
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
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "Helen, Aileen",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 4,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "swiltan",
                            "gloss": "to perish from heat",
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
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "swelter",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "\u0160ay'",
                "lang": "Arabic",
                "refs": "KLN:1756",
                "gloss": "thing"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Persian",
                    "refs": "MON; FVA:223",
                    "words": [
                        {
                            "translit": "\u0161ey'",
                            "gloss": "thing",
                            "script": "\u0634\u06cc \u0621"
                        }
                    ],
                    "script_extra": "\u0627\u0634\u06cc\u0627\u0621 \u060c \u0627\u0634\u06cc\u0627",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 0,
                    "lang": "Spanish",
                    "refs": "PRT:813; KLN:1756",
                    "words": [
                        {
                            "translit": "X",
                            "gloss": "a letter sounding \"\u0161,sh\" used as a short form for the Arabic word \"\u0161ay`: thing\"",
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
                    "lang": "English",
                    "refs": "KLN:1756",
                    "words": [
                        {
                            "translit": "X",
                            "gloss": "used in mathematics to mean an unknown \"thing\"",
```


## [2026-09-14T01:23:17.743Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -60 && echo \"---MATRIX---\" && head -80 data/verification/sources/SOURCE_MATRIX.md",
 "description": "List local refs and matrix"
}
```


### [2026-09-14T01:23:17.791Z] TOOL RESULT

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
---MATRIX---
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
```


## [2026-09-14T01:23:20.443Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-433.json | sed -n '200,400p'",
 "description": "Rest of source JSON"
}
```


### [2026-09-14T01:23:21.561Z] TOOL RESULT

```
                            "gloss": "used in mathematics to mean an unknown \"thing\"",
                            "script": null
                        },
                        {
                            "translit": "x-ray",
                            "gloss": "a kind of radiation that was not understood well when named so",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "S.d.a`",
                "lang": "Arabic",
                "refs": "SAP:857; KLN:1468",
                "gloss": "to split"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Arabic",
                    "refs": "SAP:857",
                    "words": [
                        {
                            "translit": "sod\u00e2`",
                            "gloss": "a head-splitting headache",
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
                    "lang": "Persian",
                    "refs": "MON:2137",
                    "words": [
                        {
                            "translit": "sod\u00e2`",
                            "gloss": "headache",
                            "script": "\u0635\u064f\u062f\u0627\u0639"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": {
                        "text": "\u0645\u0637\u0631\u0628 \u0639\u0634\u0642 \u0627\u06cc\u0646 \u0632\u0646\u062f \u0648\u0642\u062a \u0633\u0645\u0627\u0639 - \u0628\u0646\u062f\u06af\u06cc \u0628\u0646\u062f \u0648 \u062e\u062f\u0627\u0648\u0646\u062f\u06cc \u0635\u064f\u062f\u0627\u0639",
                        "poet": "Molav\u00ee"
                    }
                },
                {
                    "id": 3,
                    "parent": 1,
                    "lang": "Latin",
                    "refs": "KLN:1468",
                    "words": [
                        {
                            "translit": "soda",
                            "gloss": "headache",
                            "script": null
                        },
                        {
                            "translit": "sodanum",
                            "gloss": "an alkaline used to cure headaches",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "soda",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "sodium",
                            "gloss": null,
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
                    "lang": "Persian",
                    "refs": "MON:1947",
                    "words": [
                        {
                            "translit": "sod\u00e2",
                            "gloss": "soda water",
                            "script": "\u0633\u0648\u062f\u0627"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 3,
                    "lang": "French",
                    "refs": null,
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 6,
                    "lang": "Persian",
                    "refs": "MON:1847",
                    "words": [
                        {
                            "translit": "sodyom",
                            "gloss": "sodium",
                            "script": "\u0633\u062f\u06cc\u0645"
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


## [2026-09-14T01:23:22.829Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','MON','TAD','KLN','FVA','PRT','SAP','FVQ','SKT','WEB','LKT','ARY','BQT','HRN','HUB','IEC','SYN','WLD']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600] if v else 'MISSING')\n    print()\n\"",
 "description": "Look up ref abbreviations"
}
```


### [2026-09-14T01:23:24.007Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N

PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (also originsshortetym0000unse, bwb_P8-AVM-445, 1958)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q

SAP {"title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989", "kind": "purchase", "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample", "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side content, not Sayyah's pages).", "local_file": null, "page_offset": null, "c

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
```


## [2026-09-14T01:23:58.144Z] AGENT

Let me check a previous verification file for format, and start grepping local sources.


## [2026-09-14T01:24:00.148Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-385.json'))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'}, ensure_ascii=False, indent=1)[:1500])\nprint('---NODE---')\nprint(json.dumps(e['nodes'][0], ensure_ascii=False, indent=1)[:1800])\n\"",
 "description": "Inspect prior verification format"
}
```


### [2026-09-14T01:24:01.161Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Peg",
 "verdict": "plausible",
 "modern_form": "PIE *peg- / *pōg-, *pōk-s- 'armpit, hip, loin, side' (Pokorny 792); Watkins/AHD lists the same root as *peg- 'breast'",
 "note": "Pokorny 792 prints the headword as '(peg-:) pog-: pōg-, pōk-s-' and glosses it 'Achsel, Hufte, Lende, Seite' (armpit, hip, loin, side) — the full-grade *peg- is only a bracketed, inferred variant. Nourai's headword 'Peg' with the gloss 'breast' is copied verbatim from the AHD (Watkins) appendix, which prints 'peg-. Breast.' The 'breast' sense in fact rests only on Latin pectus and Tocharian A pässäṃ / B pāścane 'the two breasts'; Sanskrit pakṣa- and Latvian paksis point to 'side, flank'. Modern scholarship (de Vaan via Wiktionary) further doubts that Lat. pectus and Skt. pakṣa- belong together at all. Root is real and the language label is right; the gloss is a one-sided simplification.",
 "note_fa": "ریشهٔ هندواروپایی آغازین که نورایی آن را Peg با معنای «سینه» آورده، در فرهنگ پوکورنی (ص ۷۹۲) با سرواژهٔ «(peg-:) pog-: pōg-, pōk-s-» و معنای «زیربغل، ران، پهلو» ثبت شده است؛ صورت *peg- تنها گونه‌ای بازسازی‌شده و درون‌کمانک است. معنای «سینه» را نورایی از پیوست ریشه‌های هندواروپایی فرهنگ AHD (واتکینز) گرفته که همان‌جا «Breast» نوشته است، ولی این معنا فقط بر پایهٔ pectus لاتین و pāścane تخاری است، حال آنکه pakṣa- سنسکریت و paksis لتونیایی بر معنای «پهلو، سو» دلالت دارند. افزون بر این، پژوهش امروزی (دِ ڤان، به نقل ویکی‌واژه) در پیوند pectus لاتین با pakṣa- سنسکریت تردید می‌کند. پس: ر
---NODE---
{
 "id": 1,
 "lang": "Sanskrit",
 "words": "pakša",
 "verdict": "plausible",
 "derivation": "Sanskrit पक्ष (pakṣá-) m. is real and old (RV), but its meanings are 'wing, feather; side, flank; half (of a month); party, faction' — not 'breast'. Monier-Williams and Wiktionary give no 'breast' sense; the chart's 'breast' is imported from Nourai's root gloss. Formally pakṣa- goes back to Proto-Indo-Iranian *pakšás 'side, flank' < PIE *peg-/*pok-s-, with the regular Indo-Aryan treatment of *-ks- > -kṣ-; the Iranian cognate is Ossetic fæxs 'side'. So the arrow root -> Sanskrit is sound; only the gloss 'breast' is wrong.",
 "derivation_fa": "واژهٔ سنسکریت pakṣá- «بال، پر؛ پهلو، سو؛ نیمه (ماه)؛ دسته» از ریگ‌ودا به‌بعد گواهی شده است، اما معنای «سینه» برای آن ثبت نشده و نورایی آن را از معنای ریشه به این گره تسری داده است. از دید آوایی pakṣá- بازماندهٔ هندوایرانی آغازین *pakšás «پهلو، سو» است (خوشهٔ *-ks- در هندوآریایی به -kṣ- بدل می‌شود) و هم‌ریشهٔ آن در ایرانی، fæxs آسی به معنی «پهلو» است. بنابراین پیکان «ریشه ← سنسکریت» درست است و تنها معنای «سینه» نادرست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7"
 ],
 "ref_check": [
  {
   "ref": "AHD",
   "status": "partial",
   "note": "Watkins 1985 s.v. peg-: '2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA.' Watkins glosses the Sanskrit word 'wing' only, and marks the connection 'possibly'."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "IEW 792 (POK_03 leaf 25)",
   "stance": "partial",
   "note": "'Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"' — shoulder/wing/side, not breast."
  },
  {
   "src": "KLN",
   "where": "1966 ed. p.1272 s.v. punka (leaf 678)",
   "stance": "partial",
   "note": "'fr. OI. pakṣaḥ, pákṣas, \"wi
```


## [2026-09-14T01:24:01.798Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"swel-\" AHD_watkins1985.txt | head -20; echo \"=== helene ===\"; grep -n -i \"helen\" AHD_watkins1985.txt | head -20; echo \"=== sawel ===\"; grep -n -i \"sawel\\|s.wel-\\|sāwel\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins for swel and sawel"
}
```


### [2026-09-14T01:24:01.888Z] TOOL RESULT

```
120:For the notions of eating and drinking, the roots ed- and péi-' are most widespread. A root swel-' is attested in Avestan and sur- vives in English both in SWALLOW! and in as humble a word as SWILL. For drink, a root srebh- is found in some dialects (ABSORB). The metaphor in “drunk, intoxicated” seems to have been created independently a num- ber of times in the history of the Indo- European languages; Latin ébrius, “drunk”
754:‘ TAL), MORTGAGE, MORTIFY, MORTMAIN, POSTMORTEM; c. suffixed form *mr-yo- in Latin mori, to die: MORI- BUND, MURRAIN; d. prefixed and suffixed form *n-mr-to-, “undying, immortal” (*n-, negative prefix; see ne), in (i) Greek ambrotos, immortal, divine (a- + mbrotos, brotos, mortal): AMBROSIA (ii) Sanskrit amrta, immortal (a- + mrta, death): AMRITA. 2. Suffixed o-grade form *mor-t-yo- in Old Persian martiya-, a mortal man, in Iranian compound *martiya-khvdra- (attested in Persian mard-khvdr), ‘‘man-eater”’ (*khudra-, to eat; see swel-'), probable source of Greek mantikhoras (corrupted from martiokhéras), manticore: MANTICORE. See extended root smerd-. [Pok. 4. mer-, 5. mer- 735.]
905:sawel-. Also s(u)wel-, su(a)el-, su(@)en-, sun-. The sun. Contracted from *saswel-. 1. Variant forms *swen-, *sun- in: a. Germanic *sunndn- in Old English sunne, sun: SUN; b. Germanic compound *sunn6én-dagaz, “day of the sun” (translation of Latin diés sdlis), in Old English sunnandeg, Sunday: SUNDAY; c. Germanic de- rivative *sunthaz, “sun-side,” south, in Old English sith, south, and sitherne, southern: SOUTH, SOUTHERN. 2. Variant form *s(2)wol- in: a. Latin sd/, the sun: soL’, SOL, SOLAR, SOLARIUM; GIRASOL, INSOLATE, PARASOL, SOLANINE, TURNSOLE; b. Latin compound sdlstitium, “a standing of the sun,” solstice (-stitium, a standing; see sta-): SOLSTICE. 3. Suffixed form *sdwel-yo- in Greek hélios, sun: HELIACAL, HELIO-, HELIOS, HELIUM; ANTHE- LION, APHELION, ISOHEL, PARHELION, PERIHELION. [Pok. sdwel- 881.]
914:sécula, sickle: SICKLE. 8. Suffixed variant form *sak-so- in Latin saxum, stone (< “broken-off piece”): SAXATILE; SAXICOLOUS, SAXIFRAGE. See also extended roots sked-, skei-, sker-', sker-4. [Pok. 2. sék- 895, sken-(d)- 929.] s@k-. Slack, calm: relax. Greek (h)éka, slowly, a little (> héss6n, inferior): ESSONITE. [Pok. 3. sék- 896.] sekw-1, To follow. 1. Latin sequi, to follow: SECT, SEGUE, SEGUIDILLA, SEQUACIOUS, SEQUEL, SEQUENCE, SUE, SUITOR; CONSEQUENT, ENSUE, EXECUTE, OBSEQUIOUS, PERSECUTE, PROSECUTE, (PURSUE), SUBSEQUENT. 2. Latin sequester, “follower,” mediator, depositary: SEQUESTER, SEQUESTRUM. 8. Suffixed (participial) form *sekv-ondo- in Latin secundus, following, coming next, second: SECOND2, SECONDO, SECUND, SECUNDINES. 4. Suffixed form *sekv-os, following, in Latin secus, along, alongside of: INTRINSIC. 5. Suffixed form *sekv-no- in Latin signum, identifying mark, sign (< “standard that one follows”): SEAL!, SEGNO, SIGN; AS- SIGN, CONSIGN, DESIGNATE, INSIGNIA, RESIGN. 6. Suf- fixed o-grade form *sok’-yo- in Latin socius, ally, companion (< “follower”): SOCIABLE, SOCIAL, SOCIETY, SOCIO-; ASSOCIATE, CONSOCIATE, DISSOCIATE. [Pok. 1. seky- 896.] sekw-2, To perceive, see. 1. Germanic *sehwan, to see, in Old English séon, to see: SEE}. 2. Germanic abstract noun *sih-tiz in Old English sihth, gesiht, vision, specta- cle: SIGHT. [Pok. 2. sek¥- 872.] sekw-3, To say, utter. 1. O-grade form *sokv- in: a. suf- fixed form *sokv-yo- in Germanic *sagjan in Old English secgan, to say: SAY; b. suffixed form *sok-d- in Ger- manic *sag6, a saying, in (i) Old English sagu, a saying, speech: sAw? (ii) Old Norse saga, a saying, narrative: saGA. 2. Suffixed zero-grade form *sk~-e-tlo-, narration, perhaps in North Germanic “skathla in Old Norse skdid, poet, “narrator,” perhaps akin to the probable Scandina- vian source of Middle English scolde, an abusive person: SCOLD, SKALD. [In Pok. 2. sek¥- 897.] sel-1, Human settlement. 1. O-grade form *sol- in Ger- manic *sal-, room, in Italian sala, hall, room: SALON, (SALOON). 2. Suffixed form *sel-o- in Latin solum, bot- tom, foundation, hence sole of the foot: SOLE!, SOLUM; ENTRESOL. [Pok. 1. sel- 898, 3. (swel-) 1046.] sel-2, Also sele-. Of good mood; to favor. 1. Germanic lengthened form *sél- in Old English ges#lig, happy (ge-, completely; see kom): SILLY. 2. Suffixed lengthened o-grade form *sdl-d- in Latin sdlari, to comfort, console: SOLACE; CONSOLE}. 3. Possibly suffixed form *sels-ro- in Greek hilaros (< *helaros), gay: HILARITY; EXHILARATE. [Pok. 6. sel- 900.] sel-3, To take, grasp. 1. Suffixed o-grade (causative) form *sol-eyo- in Germanic *saljan, to offer up, deliver, whence West and North Germanic “‘to sell,” in Old English sellan, to sell, betray: SELL. 2. Germanic *sal-, giving, sale, in: a. Old Norse sala, sale: SALE; b. Old Norse compound handsal, giving of the hand (in closing a bargain): HANDSEL. [Pok. 3. sel- 899.] sel-4, To jump. 1. Suffixed zero-grade form *sal-yo- in: a. Latin salire, to leap: SALACIOUS, SALIENT, SALLY, (SAUTE); ASSAIL, DESULTORY, DISSILIENT, EXULT, IN- SULT, RESILE, RESULT, SOMERSAULT; b. Greek halles- thai, to leap, jump: HALTER2. 2. Perhaps Latin salmé (borrowed from Gaulish), salmon (< “the leaping fish”): SALMON. [Pok. 4. sel- 899.] sel-es-. Swamp, marsh, sea. Greek helos, marsh: ELODEA. [Pok. selos- 901.] selk-. To pull, draw. 1. Perhaps Germanic *selhaz, seal (the animal), “that which drags its body along with difficulty” (but more likely an early Germanic borrowing from Finnic), in Old English seolh, seal: SEAL?. 2. Suf- fixed o-grade form *solk-o- in Latin sulcus, furrow, groove (< “result of drawing or plowing”): (SULCATE), sucus. [Pok. selk- 901.] selp-. Fat, butter. 1. Germanic *salb- in Old English sealf, healing ointment: SALVE}. 2. Germanic denomina-
1044:s(w)eks. Six. I. Form *seks. 1. Germanic *seks in Old English s(iJex, six, six: sIx. 2. Latin sex (> Italian sei), six: SENARY, SEX-; SEICENTO, SEMESTER. 3. Suffixed form *seks-to- in Latin sextus, sixth: SESTET, SESTINA, SEXT, SEXTAN, SEXTANT, SEXTILE; SEXTODECIMO. II. Form *sweks in Greek hex, six: HEXA-, HEXAD. [Pok. sueks 1044.] swel-', To eat, drink. 1. Perhaps Germanic *swil- in Old English swilian, to wash out, gargle: swILL, 2. Extended form *swelk- in Germanic *swelgan, *swelhan in Old English swelgan, to swallow: SWALLOW!; GROUNDSEL!. 3. Iranian *khvdra- (attested in Avestan), to eat, in the probable source of Greek mantikhdras, manticore (see mer-?). [Pok. 1. suel(k)- 1045.] swel-2, To shine, burn. 1. Extended form *sweld- in Germanic *swiltan in Old English sweltan, to die, perish (perhaps < “be overcome with heat”): (SULTRY), SWEL- TER. 2. O-grade form *swol- in Germanic *swal- in Old Norse svalr, cool (< “lukewarm” < “hot”), akin to the Scandinavian source of Middle English swale, shade, shady place: SWALE. [Pok. 2. swel- 1045.]
1045:swel-3, Post, board. Germanic *suljé- in Old English sylXe), doorsill, threshold: stLL. [Pok. 2. sel-, swel- 898.] swem-. To move, stir, swim. Possibly an Indo-European root, but perhaps Germanic only. 1. Germanic *swimjan in Old English swimman, to swim: SWIM. 2. Suffixed zero-grade form *swum-to- in Germanic *sundam in: a. Old English sund, swimming, sea: SOUND’; b. Old French sonde, sounding line: SOUND‘; RADIOSONDE, ROCKETSONDE. [Pok. syem- 1046.]
1568:GROUNDSEL! ghendh-, swel-1
2257:SIGHT sekw-2 SIGN sekw-1 SIGNORY sen-1 SIKH kak-1 SILENT si-lo- SILL swel-3
2325:SUE sekw-1 SUFFER bher-1 SUFFICE dhé-1 SUFFICIENT dhé-1 SUFFIX dhig’- SUFFRAGAN bhreg- SUFFRAGE bhreg- SUFFUSE gheu- SUGGEST gerere SUICIDE s(w)e- SUINT sweid-2 SUITOR sekw-1 SULCATE selk- SULCUS selk- SULLEN s(w)e- SULTRY swel-2 SUM uper SUMMER! sem-2 SUMMIT uper
2328:SURE cilra, s(w)e- SURFACE dhé-1 SURFEIT dhé-1 SURGE reg-! SURGEON ghesor- SURGERY ghesor-, werg- SURLY sen-1 SURMISE (s)meit(9)- SURMULLET mel-2, saus- SURPLICE pel-4 SURPLUS pele-' SURPRISE ghend- SURRENDER d6- SURREPTITIOUS rep- SURROUND wed-! SURVEILLANT weg-2 SURVEY weid- SURVIVE gWei- SUSCEPTIBLE kap- SUSPECT spek- SUSPEND (s)pen- SUSPIRE spirare SUSTAIN ten- SUSURRATION swer-2 SUTLER seut- SUTRA syil- SUTTEE e@8- SUTURE syu- SVELTE wel-4 SWAB swep-2 SWAG sweng(W)- SWAIN s(w)e- SWALE swel-2 SWALLOW! swel-1 SWAMI s(w)e- SWAMP swombho- SWAN swen- SWANK sweng(w)- swaP swei-2 SWARF swerbh- SWARM swer-2 SWART swordo- SWASTIKA @S-, SU- SWEAR swer-1 SWEAT sweid-2 SWEET swad- SWELTER swel-2 SWERVE swerbh- SWIFT swei-2 SWILL swel-!
=== helene ===
1140:for strong-smelling animals. 1. Germanic *wisulén- in Old English wesle, weosule, weasel: WEASEL. 2. Suffixed form *wis-onto- in Germanic *wisand-, *wisunt-, Euro- pean bison (which emits a musky smell in the rutting season), in: a. Old High German wisunt, bison: WISENT; b. Latin bisdn (plural bisontés), bison: BISON. [Pok. 3. ueis- 1134.] weit(a)-. To speak, adjudge. Extended o-grade form *woito- in Russian véti, council (see sem-'). wekti-. Thing, creature. Germanic *wihti- in Old English wiht, person, thing: WIGHT!; (AUGHT?), NAUGHT, NOT. [Pok. wek-ti- 1136.] = wekv-. To speak. 1. O-grade form *wokv- in: a. Latin vox (stem vdc-), voice: VOCAL, VOICE, VOWEL; EQUIVOCAL, UNIVOCAL; b. Greek ops, voice: CALLIOPE. 2. Suffixed o-grade form *wok-d- in Latin vocdre, to call: VOCABLE, VOCATION, VOUCH; ADVOCATE, AVOCATION, CONVOKE, EQUIVOCAL, EVOKE, INVOKE, PROVOKE, REVOKE. 3. Suf- fixed form *wek-es- in Greek epos, song, word: EPIC, EPOS. [Pok. uekz- 1135.] wel-'. To see. 1. Suffixed zero-grade form *wl-id- in Germanic *wlituz, appearance, in Old Norse litr, appear- ance, color, dye, akin to the source of Litmus. 2. Suffixed form *wel-uno- perhaps in Sanskrit Varunah, “seer, wise one,” sovereign god: VARUNA. [Pok. 1. wel- 1136.] wel-2, To wish, will. 1. Germanic *wel- in Old English wel, well (< “according to one’s wish”): WELL?. 2. Germanic *welon- in Old English wela, weola, well-being, riches: WEAL!, WEALTH. 3. Germanic *wiljén- in Old English willa, desire, will power: WILL. 4. Germanic *wil(Ijan in Old English wyllan, willan, to desire: WILL?; NILL. 5. Ger- manic compound *wil-kumon- (see g¥a-). 6. O-grade form *wol- in Germanic *wal- in Old French galloper and Old North French waloper, to gallop: GALLOP, WALLOP. 7. Basic form *wel- in Latin velle (present stem vol-), to wish, will: VELLEITY, VOLITION, VOLUNTARY; BENEVO- LENT, MALEVOLENT. 8. Suffixed form *wel-up- in Latin voluptds, pleasure: VOLUPTUARY, VOLUPTUOUS. [Pok. 2. uel- 1137.] wel-3, To turn, roll; with derivatives referring to curved, enclosing objects. 1. Germanic *walt- in: a. Old High German wailzan, to roll, waltz: wALTz; b. Middle Dutch welteren, to roll: WELTER. 2. Germanic *weluka- in Old English weoluc, weoloc, mollusk (having a spiral shell), whelk: WHELK!. 3. Perhaps Germanic *wel- in Old Eng- lish welig, willow (with flexible twigs): wILLOw. 4. Per- haps Germanic *welk- in Old English wealcan, to roll, toss, and wealcian, to muffle up: WALK. 5. O-grade form *wol- in Germanic *wall- in: a. Old English wiella, wella, a well (< “rolling or bubbling water,” “spring”): WELL; b. Old High German waillén, to roam: GABERDINE. 6. Perhaps suffixed o-grade form *wol-d- in Germanic *walé in: a. Old English walu, streak on the skin, weal, welt: WALE; b. Old High German *-walu, a roll, round stem, in *wurzwalu, rootstock (see wrad-). 7. Extended form *welw- in: a. Germanic *walw6n in Old English wealwian, to roll (in mud): WALLOW; b. Latin volvere, to roll: VAULT!, VAULT2, (VOLT2), VOLUBLE, VOLUME, VO- LUTE, VOLUTIN, VOLVOX, VOUSSOIR; CIRCUMVOLVE, CON- VOLVE, DEVOLVE, EVOLVE, INVOLVE, OBVOLUTE, REVOLVE; C. suffixed o-grade form *wolw-d- in Latin vulva, volva, covering, womb: VOLVA, VULVA; d. suffixed zero-grade form *wlw-d- in Latin valva, leaf of a door (< “that which turns”): VALVE; e. suffixed form *welu-tro- in Greek elutron, sheath, cover: ELYTRON. 8. Suffixed form *wel-n- in Greek eilein (< *welnein), to turn: ILEUS; NEURILEMMA. 9. Perhaps variant *wall- in Latin vallés, vallis, valley (< “that which is surrounded by hills”): VAIL!, VALE!, VALLEY. 10. Suffixed form *wel-end, possi- bly identical with the Greek name Helené (earliest form Welend), Helen, in Greek helenion, elecampane: ELECAM- PANE, INULIN. 11. Suffixed form *wel-ik- in Greek helix, spiral object: HELIX. 12. Suffixed form *wel-mi-nth- in Greek helmis, helmins (stem helminth-), parasitic worm:
=== sawel ===
131:The other celestial bodies recognized were the sun, sawel-, and the stars, ster-3. There is evidence from several traditions for similar designations of the constellation Ursa Major, though these may not go back to the earliest Indo-European times. The movement of the sun dictated the names for the points of the compass. EAST is derived from a verbal root aus-', “to shine,” as is the word for “dawn” (Latin Aurora), divinized since Indo- European times on the evidence of Greek, Lithuanian, and Sanskrit. The setting sun furnished the word for “evening” and “west”:
905:sawel-. Also s(u)wel-, su(a)el-, su(@)en-, sun-. The sun. Contracted from *saswel-. 1. Variant forms *swen-, *sun- in: a. Germanic *sunndn- in Old English sunne, sun: SUN; b. Germanic compound *sunn6én-dagaz, “day of the sun” (translation of Latin diés sdlis), in Old English sunnandeg, Sunday: SUNDAY; c. Germanic de- rivative *sunthaz, “sun-side,” south, in Old English sith, south, and sitherne, southern: SOUTH, SOUTHERN. 2. Variant form *s(2)wol- in: a. Latin sd/, the sun: soL’, SOL, SOLAR, SOLARIUM; GIRASOL, INSOLATE, PARASOL, SOLANINE, TURNSOLE; b. Latin compound sdlstitium, “a standing of the sun,” solstice (-stitium, a standing; see sta-): SOLSTICE. 3. Suffixed form *sdwel-yo- in Greek hélios, sun: HELIACAL, HELIO-, HELIOS, HELIUM; ANTHE- LION, APHELION, ISOHEL, PARHELION, PERIHELION. [Pok. sdwel- 881.]
997:sta-. To stand; with derivatives meaning “place or thing that is standing.” Contracted from *stag-. I. Basic form *std-. 1. Extended form *stddh- in: a. Germanic *stéd- J6n- in Old English stéda, stallion, studhorse ( < “place for breeding horses”): STEED; b. Germanic *st6d6 in Old English stéd, establishment for breeding horses: sTuD2. 2. Suffixed form *std-lo- in Germanic *stdlaz in: a. Old English st6/, stool: sTooL; b. compound *faldistélaz (see pel-3). 3. Latin stdre (third person singular present subjunctive séet), to stand, with its past participle status (< “sta-to-) and derivatives statira, height, stature, and statuere, to set up, erect, cause to stand: STAGE, STANCE, STANCH, (STANCHION), (STANZA), STATOR, (STATUE), STATURE, STATUTE, STAY!, STET; ARREST, CIRCUM- STANCE, CONSTANT, CONSTITUTE, CONTRAST, (COST), DESTITUTE, DISTANT, ESTANCIA, EXTANT, INSTANT, IN- STITUTE, OBSTACLE, OBSTETRIC, (OUST), PROSTITUTE, REST?, RESTITUTE, RESTIVE, SUBSTANCE, SUBSTITUTE, SUPERSTITION. 4. Suffixed form *std-men- in Latin std- men, thread of the warp (a technical term): STAMEN, STAMMEL. 5. Suffixed form *std-mon- in Greek stémén, thread: PENSTEMON. 6. Suffixed form “s¢d-ro- in Russian staryi, old (“long-standing”): STARETS. II. Zero-grade form *st- (before consonants). 1. Nasalized extended form *sfa-n-t- in Germanic *standan in: a. Old English standan, to stand: STAND; b. Old English understandan, to know, stand under (under-, under; see ndher): UN- DERSTAND; Cc. Old French estandard, rallying place: STANDARD; d. secondary zero-grade form in Germanic *stund-6 in Old English stund, a fixed time, while: STOUND. 2. Suffixed form *sé-tyo- in Germanic *stath- Jon- in Old Norse stedhi, anvil: strTHY. 3. Suffixed form *sta-tlo- in Germanic *stathlaz in Old English stathol, foundation: STADDLE, STARLING?. 4, Suffixed form *sta-mno- in Germanic *stamniz in Old English stefn, stem, tree trunk: sTeM!. 5. Suffixed form *sta-ti- in: a. Germanic *stadiz in (i) Old English stede, place: STEAD (ii) Dutch stad, place: STADHOLDER (iii) Old High Ger- man stat, place: SHTETL; b. Latin stati6, a standing still: STATION; C. Latin -stitium, a stoppage (in solstitium, solstice; see sawel-): ARMISTICE; d. Greek stasis, a standing, a standstill: sTAsIs; HYPOSTASIS, ICONOSTASIS, IsOSTASY. 6. Suffixed form *sfo-to- in Greek statos, placed, standing: STATIC, STATICE, STATO-; ASTASIA, ASTATINE. 7. Suffixed form “sta-no- in: a. Latin désti-
1247:ANTA aneta ANTAGONIZE ag- ANTE ant- ANTEBELLUM duellum ANTECEDE ked- ANTEFIX dhig¥- ANTEPENDIUM (S)pen- ANTERIOR ant- ANTHELION sawel- ANTHELMINTIC wel-3 ANTHEM bha-2 ANTHEMION andh- ANTHER andh- ANTHESIS andh- ANTHO- andh- -ANTHOUS andh- ANTHROPIC ner-2 ANTHROPO- ner-2 ANTHURIUM ors- ANTI- ant-
1252:AORTA wer-2 APERIENT wer-5 APERITIF wer-5 APERTURE wer-5 APEX ap-! APHELION sawel- APHONIA bha-2 APLANATIC pele-2 APLOMB plumbum APNEA pneu-
1560:GEODE gé GEODESY da- GEOMETRY mé-2 GEOPONIC (s)pen- GEORGIC gé, werg- GERANIUM gera-2 GERENT gerere GERIATRICS gera-1 GERM gene- GERMAN? gena- GERMANDER deru, dhghem- GERMANE gene- GERMINAL gene- GERMINATE gene- GERONTO- gera-1 GERUND gerere GEST gerere GESTALT stel- GESTATION gerere GESTICULATE gerere GESTURE gerere GET ghend- GEYSER gheu- GHAT gher-4 GHOST gheis- GIDDY gheu(e)- Girt ghabh- GILD! ghel-2 GILL! ghel-una GILLS ghai- GILLYFLOWER bhel-3, kar-1 GILT2 ghel-3 GIMMAL yem- GINGERLY gene- GIRASOL sawel- GIRD gher-1 GIRDLE gher-1 GIRTH gher-1 GIST yé-
1590:HELIACAL sawel- HELIO- sawel- HELIos sawel- HELIUM sawel- HELIX wel-3
1672:IGNORE gno- ILEUS wel-3 ILK i-
1681:INQUIRE quaerere INSCRIBE skribh- INSECT sek- INSERT ser-3, s6-1 INSESSORIAL sed-1 INSIGNIA sekw-1 INSIST sta- INSOLATE sawel- INSOMNIA swep-! INSPECT spek- INSPIRE spirare INSTALL | stel- INSTALLMENT! | stel- INSTANT sta- INSTAURATION sta- INSTIGATE | steig- INSTINCT | steig- INSTITUTE sta- INSTRUCT  ster-2 INSULT sel-4 INSURE cura INTACT tag- INTEGER tag- INTEGUMENT (s)teg- INTELLIGENT leg-1 INTEND ten-
1691:Is es- ISALLOBAR gWere-2 ISCHEMIA segh- ISINGLASS bhié-2 ISLAND akwa- ISOBAR gWere-2 ISOCLINE klei- ISOGLOss glogh- ISOHEL sawel- ISOHYET seue-2 ISOMER (S)mer-2 ISOMETRIC mé-2 ISOPIESTIC sed-1 ISOPLETH pele-1 ISOSCELES skel-3 IsosTasy sta- ISSUE ei-1
2059:-PARA pere-1 PARABLE gWelg-1 PARABOLA gW¥ele-1 PARACHUTE pere-1 PARACLETE kele-2 PARADE pere-1 PARADIGM deik- PARADISE dheigh-, pert PARADOX dek-! PARAFFIN pau- PARAGRAPH gerbh- PARALLAX al-1 PARALLEL al-1 PARALLELEPIPED ped-! PARALOGISM leg-1 PARALYSIS leu PARAMECIUM mak- PARAMOUNT ad-, per! PARAMOUR amma, pert PARANOIA nous PARAPET peg- PARAPHERNALIA bher-1 PARAPHRASE gWhren- PARAPLEGIA plak-2 PARASOL pere-1, sawel- PARATAXIS tag- PARBOIL beu-! PARCAE pera-1 PARCEL pere-2 PARCENER pere-2 PARDON d6-
2061:PARGET per, yé- PARHELION sawel- PARI-MUTUEL pere-2 PARISH weik-1 PARITY2 pere-2 PARLAY pere-2 PARLEY gWelg-1 PARLIAMENT gWele-1 PARLOR gWelg-1 PARLOUS per-4 PARODY wed-2 PAROL gWele-1 PAROLE gWele-1_ PARONOMASIA n0-men- PARONYCHIA nogh- PARONYMOUS no-men- PAROTID GLAND ous- -PAROUS pere-) PAROUSIA es- PAROXYSM ak- PARRICIDE paso- PARRY pere-!
2079:PER- pert PERCEIVE kap- PERCENT dekm PERCH? perk-1 PERCOLATE kagh- PERCURRENT kers-2 PERCUSS kwét- PERDITION d6- PERDURABLE deue- PEREGRINE agro- PEREMPTORY em- PERENNIAL at- PERFECT dhé-1 PERFIDY bheidh- PERFORATE bher-2 PERFUME dheu-1 PERFUNCTORY bheug-2 PERFUSE gheu- PERGOLA perg- PERI- per! PERICARDIUM kerd-1 PERICLINE Klei- PERIGEE gé PERIHELION sawel- PERIL per-4 PERIMYSIUM mis- PERINEPHRIUM negWh-ro- PERIOD sed-2 PERIONYCHIUM nogh- PERIOSTEM ost- PERIPATETIC pent- PERIPETEIA pet- PERIPHERY bher-1 PERIPHRASIS gWhren- PERIPHYTON bheue- PERIPTERAL pet- PERISARC  twerk- PERISH ei-1 PERISSODACTYL per! PERISTALSIS | stel- PERISTYLE sta- PERITHECIUM dhé-1 PERITONEUM ten- PERITRICH _ thrix PERIWINKLE! weng- PERJURE yewes- PERMANENT men-3 PERMEATE mei-1 PERMIT (s)meit(a)- PERMUTE mei-1 PERNICIOUS nek-1 PERONEAL per-2 PERORAL 6s- PERORATE 6r- PERPEND (S)pen- PERPENDICULAR (S)pen- PERPETRATE peter- PERPETUAL pet- PERPLEX plek-
2273:SNIFF snu- SNIP snu- SNIVEL snu- SNOOP snu- SNORE sner- SNORKEL sner- SNORT sner- SNOT snu- SNOUT snu- SNOW sneig’h- SNUB snu- SNUFF! snu- SNUFFLE snu- SNUG! kes-1 sO swo- SOAK seua-2 sOAP_ seib- SOAVE swad- SOBER s(w)e- SOCIABLE sekw-1 SOCIAL sekw-1 SOCIETY sekw-1 SOCIO- sekw-1 SOCKET sU- SODALITY s(w)e- SODDEN seut- SOIL! sed-1 som? si- SOIREE sé@-2 SOJOURN deiw- SOKE sag- sol’ sawel-
2276:SoL sdwel- SOLACE sel-2 SOLANINE sAwel- SOLAR sawel- SOLARIUM sawel- SOLE! sel-1 SOLE? s(w)e- SOLEMN sol- SOLICITOUS_ kei-3, sol- SOLID sol- SOLILOQUY s(wW)es, tolkw- SOLIPSISM s(w)e- SOLITARY s(w)e- SOLITUDE s(w)e- SOLO s(w)e- SOLSTICE sawel- SOLUBLE leu-1 SOLUM sel-1 SOLUTE leu-1 SOLVE leu-! SOMA teue- SOMATO- teua- SOME sem-! -SOME! sem-1 -SOME2  teue- SOMERSAULT sel-4, uper SOMNI swep-! SOMNOLENT swep-! SON seue-! SONANT swen- SONATA swen- SONE swen- SONG sengWh- SONIC swen- SONNET swen- SONOROUS swen- sooT sed-1 SOOTH es- SOOTHE es-
2277:SOP seue-2 SOPOR swep-1 SOPORIFIC swep-1 SOPRANINO uper SOPRANO uper SORCERER ser-3 SORDID swordo- SORDINO swer-2 SORE sai- SORITES teue- SORORAL swesor- SORORITY swesor- SORREL! siiro- SORREL? saus- SORROW swergh- SORRY Sai- SORT ser-3 SORTILEGE leg-1, ser-3 SORUS teue- SOTERIOLOGY teue- SOUBRETTE uper SOUFFLE bhlé-2 SOUGH (s)wagh- SOUND! swen- SOUND2 swento- SOUND3 swem- SOUND4 swem- SOUP seue-2 sOUR siiro- SOURDINE swer-2 SOUSE sal-1 SOUTANE upo SOUTH sawel- SOUTHERN sawel- SOUVENIR gWa- SOVEREIGN uper SOVIET sem-! sow! sé-1
2326:SUMMON men-! sUMP swombho- SUMPTUARY em- SUMPTUOUS em- SUN sawel- SUNDAY sawel- SUNDER sen-2 SUNDRY sen-2 SUP! seue-!
2420:TUMID teue- TUMOR teue- TUMULUS teu@- TUNGSTEN | stei- TURBARY derbh- TURBID twer-1 TURBINE twer-1 TURD der-2 TUREEN ters- TURF derbh- TURN tere-1 TURNSOLE sawel-
2447:VARY wer-? VASSAL upo vaT ped-2 vaTic wet-1 VAULT! wel-3 VAULT2 wel-3 VAUNT eu-2 VEAL wet-2 VECTOR wegh- VEDA weid- VEDANTA ant- VEDETTE weg-2 VEER2 per! VEGETABLE weg-2 VEHICLE wegh- VEIL weg-! VELDT pele-2 VELIGER gerere VELLEITY wel-2 VELOCITY weg-2 VELOURS wel-4 VELUM weg-1 VELVET wel-4 VENAL wes-1 VENATIC wen-1 VEND d6-, wes-! VENDETTA deik- VENEER per! VENERATE wen-! VENEREAL wen-! VENERY! wen-1 VENERY2 wen-! VENIAL wen-! VENIRE gWa- VENISON wen-! VENOM wen-! VENT wé- VENTAIL wé- VENTER udero- VENTILATE weé-
2453:VICINITY weik-1 vicious wei-4 VICISSITUDE weik-4 VICTIM weik-2 vIcTOR weik-5 VICTUAL gWei- VIDE weid- view weid- VIGESIMAL wikmti VIGIL weg-2 VIGILANT weg-2 VIGILANTE weg-2 VIGOR weg-2 VILIPEND (S)pen- VILLA weik-1 VILLAGE weik-! VILLAIN weik-1 VILLANELLE weik-1 VILLEIN weik-1 VILLUS wel-4 vIM weie- VINACEOUS vinum VINCIBLE weik-5 VINDICATE deik- VINE vinum VINEGAR ak-, vinum VINI- vinum VINTAGE em- VIOLATE weia- VIOLENT weie- VIRAGO Wi-ro- VIREO virére VIRESCENT virére
```


## [2026-09-14T01:24:17.282Z] AGENT

Let me render the printed page and grep Pokorny.


## [2026-09-14T01:24:20.887Z] TOOL CALL #9: Bash

```json
{
 "command": "ls site/pages/433.jpg 2>/dev/null; pdftoppm -f 433 -l 433 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg433 && echo OK && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg433.png",
 "description": "Render PDF page 433"
}
```


## [2026-09-14T01:24:22.527Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['POK_01.txt','POK_02.txt','POK_03.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    pages=t.split('\\f')\n    print(f, 'leaves', len(pages))\nEOF",
 "description": "Check POK file leaf counts"
}
```


### [2026-09-14T01:24:22.685Z] TOOL RESULT

```
site/pages/433.jpg
OK
-rw-rw-r-- 1 sfmqrb sfmqrb 74286 Sep 13 21:24 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg433.png
```


### [2026-09-14T01:24:23.887Z] TOOL RESULT

```
POK_01.txt leaves 364
POK_02.txt leaves 434
POK_03.txt leaves 430
```


## [2026-09-14T01:24:25.737Z] TOOL CALL #11: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg433.png"
}
```


### [2026-09-14T01:24:26.325Z] TOOL RESULT

```

```


## [2026-09-14T01:24:26.314Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T01:24:46.656Z] TOOL CALL #12: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(d['POK']['page_offset']); print(d['POK'].get('lookup_hint'))\nprint('KLN:', d['KLN']['page_offset']); print(d['KLN'].get('lookup_hint'))\n\"",
 "description": "Get POK and KLN page offsets"
}
```


### [2026-09-14T01:24:47.574Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
KLN: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
```


## [2026-09-14T01:24:52.168Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: sāuel\\|lemma: sawel\\|lemma: sāwel\\|lemma: su̯el\\|lemma: suel\" POK_full.txt | head -20; echo \"===881===\"; grep -n \"Page(s): 881\" POK_full.txt | head; echo \"===1045===\"; grep -n \"Page(s): 1045\" POK_full.txt | head",
 "description": "Grep POK_full for sawel and page 881/1045"
}
```


### [2026-09-14T01:24:52.268Z] TOOL RESULT

```
73669:lemma: suel-2\ "to smoulder, burn'. 
83724:Root / lemma: suel-l(k-) 
83754:Root / lemma: suel-2 
83773:Root/ lemma: suel-2\ (to smoulder, burn). 
83833:Root / lemma: suel-4 
83878:Root / lemma: suelplo-s 
===881===
72314:Page(s): 881-882 
===1045===
```


## [2026-09-14T01:24:55.134Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '72290,72330p' POK_full.txt; echo \"=====SWEL2=====\"; sed -n '83754,83800p' POK_full.txt",
 "description": "Read POK entries"
}
```


### [2026-09-14T01:24:55.237Z] TOOL RESULT

```
That means Slavic *su/n/ka-n. in Old Church Slavic s/bnbce^ sun ' (-a?/- from * 0^/7/ "fire') is 
phonetically equal to Tocharian A swance, swanco, Tocharian B swancai- "ray [of light], 
(sun) beam', hence Slavic forms were created according to attribute nouns ans are late 
creations. 

Maybe gr. 'AnoAAojv, -ojvoc;; various dialectic forms: 'AheAAwv (Doric), 'AnsiAwv (Cypriot), 
A"ttAouv (Thessalian). - Seit J. Schmidt KZ 32, 327ff. all are linked to Cretan apsAioq Hes. 
(i.e. dFsAioi;) " sun '. It seems that the sun god 'AttoAAojv derived from Cretan apsAioi; Hes. 
(i.e. aPzhoc^) " sun '. The common in gr. Ai > AA has taken place. Both 'AheAAwv (Doric), 
'AnsiAojv (Cypriot), A'nAouv (Thessalian) and Cretan apsAiot; Hes. (i.e. aFsAiot;) " sun ' 
derived from the same root *sahue/' sun' where the common gr. hw > p, gw > b has taken 
place. 

Note: 

Khaskura gham (also Indie borrowing surj) " sun ', Gypsy Gk kham " sun ' : gr. aFeAioq 

reflect gr. -b- > -mb- > -m-. 

Maybe Etruscan aviT year ' a borrowing from gr. qFeAio^. 

References: WP. II 446 f., WH. II 553 f., Trautmann 251, A. Scherer Gestirnnamen 45 ff. 

Page(s): 881-882 

Root / lemma: sa-, sa- 

Meaning: satiated 

Material: Old Indie a-si-n-va-, asinvan^ insatiable ' (places ein Praes. *s9-neu-mi, *s9-nu-6 

ahead); 

Armenian a/-c»/r" "full, ausgewachsen'; had, /7aJoy"zufrieden' {*sadio-); 



gr. thematic present asrai "sattigt sich' (Hesiod; *S9-iS), athematic Wurzelaor. apsvai 
(Horn.) ' be satiated '; Aor. Inf. aaai " satiate ' and " satiated become', ewjjev (*riofj£v, Konj. 
Aor.), Fut. aasiv, etc.; a-aroc; ( *n-sa-tos) " insatiable ', a5r|v = Boeotian a5av 'bis zur 
=====SWEL2=====
Root / lemma: suel-2 

Meaning: to smoulder, burn 

Material: Old Indie 5i/a/'5//"radiates, shines '; svarga-x^. " sky '; 

gr. sTAri, sTAri- s^n f. ' solar warmth, sunlight ', ysAav auynv rjAiou, lak. psAa Hes., sAavr) " 
flambeau, torch ', assim. eAevh Hes., DEA£vr| originally a light goddess; zero grade aAsa f. 
" solar warmth ', aAsaivw ' warms up ', ixKtzwioc, "hot', aAuKpot; (Nikand.) 'warm'; 

uncertain affiliation from oiKo^c, n. ' Shine ', asAnvn, Aeolic ozkav\/a " moon ' (*a£Aaavc(), 
GsAaysTv " shine '; 

maybe alb. (*a£Aay£Tv) *xelageln, shkelqen' shines' 

maybe alb. (*a£Aavva) hana' moon ' similar to alb. {*sull-) hul or star, planet, *sun ' [the 
shift s> h\\ 

alb. and gr. prove that from Root/ lemma: sauel-, sauol-, suuel-, suel-, sul-\ (sun) derived 
Root/ lemma: suel-2\ (to smoulder, burn). 



Old English swe/an stem V. " burn, is ignited ', Middle Low German swelen sdcwN . V. 
(Modern High German schwelen). Old High German swilizdn; Old Icelandic svalr^ cold ' 
(actually "singeing'), Middle Low German swalm^ dense smoke ', Old English swolu. 
{*swula-), sw(e)olod(a)vc\. " the burning, heat '; 

maybe alb. {*sveri) Ke/7'north cold wind', {*sveri) Ke/7'north, cold' 

lengthened grade *swel-\v\ Old Icelandic svaela^ burn incense ', f. " thick smoke ', Old 
English swaelan^ incinerate, burn (trans.)', and *swdl- in Low German swdr sultry ' 
(umlaut. Modern High German schwul), Dutch zwoel, zoel6s:, 

- with Germanic /r.Low German swalk^ steam, smoke ', Middle High German swelk^ 
withered, dry ', Old High German swelchen. Middle High German swelken^ become wilted 
'. -the o^-present in Old High German swelzan' burn, incinerate (intr.)', for what 
presumably as " swelter ' (compare engl. sweltry, sultry^ extremely hot '), 

Old English Old Saxon sweltan s\ev(\ V. " die, pass away ', Middle Dutch swelten. Old 
Icelandic svelta siem V. " starve, die ', Gothic swiltan sierw V. ' to die ', zero grade Gothic 
swulta-wairt^ja^ he who leans toward death, he who is inclined toward death ', Old 
Icelandic sultrxw. ' hunger ', Old English swyltm. " death '; maybe to Armenian k'aic-nu-m 
" starve ', k'aic^ hunger' {*suld-sk-d)\ 

Lithuanian svilu, svlItT is being scorched (intr)., burn without flame ', causative svllintT 
to singe (tr.)', zem. sv'ilis' heat, fevers ', svelti^ smolder ', Latvian svel'u, svelV to scorch
```


## [2026-09-14T01:25:00.698Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '83800,83835p' POK_full.txt; echo \"=== root lemma sauel header ===\"; grep -n \"lemma: sauel\" POK_full.txt | head; ",
 "description": "Find POK suel-2 page and sauel lemma"
}
```


### [2026-09-14T01:25:00.773Z] TOOL RESULT

```
to singe (tr.)', zem. sv'ilis' heat, fevers ', svelti^ smolder ', Latvian svel'u, svelV to scorch 
(tr.)', svelmei. ' steam, glow ', svalsm. " steam ', svelains^ sharp, cold ' (compare 
meaning from Old Norse svali). 

Maybe alb. {*svala) vale'boW, steam', phr. merr nje va/e'to steam' [the common alb. shift 
SV > V]. 

References: WP. II 531 f., Scherer Gestirnnamen 49 f., Trautmann 296, Frisk 65 f.; 
See also: see above S. 881 f. sauel- 
Page(s): 1 045 

Root / lemma: {suel-3), suol-, sul- 

Meaning: foot sole; ground 

Material: Latin solea^ a sandal; a kind of fetter; a shoe for an animal; a fish, the sole '; 

solum' bottom, floor, foundation; the sole of the foot, or shoe; soil, ground, earth, land, 

country '; 



Middle Irish fol. i. bond^ foundation, foot sole ', Akk. Sg. folaig, Norn. PI. solaig, Dat. PI. 
Old Irish soilgib; 

zero grade gr. uAia (Hes.) ' foot sole '. 

Alb. sho//e 'so\e' (probably a Latin loanword). 

References: WP. II 552, WH. II 554 f. 
Page(s): 1 046 

Root / lemma: suel-4 

Meaning: ' arbor, joist, beam, timber, bar, rod ' 
=== root lemma sauel header ===
63677:trait)], hence alb. geg suni 'eye' : Old Irish {*su//-) suir eye ' : Root / lemma: sauel- sauol- 
71448:lemma: sauel- sauol- suuel- suel- sul-\ (sun). 
71617:Root / lemma: sauel- sauol- suuel-, sue/-, sul- , {*hauhuel-) 
83772:alb. and gr. prove that from Root/ lemma: sauel-, sauol-, suuel-, suel-, sul-\ (sun) derived
```


## [2026-09-14T01:25:03.764Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '71617,71680p' POK_full.txt",
 "description": "Read POK sauel- entry"
}
```


### [2026-09-14T01:25:03.826Z] TOOL RESULT

```
Root / lemma: sauel- sauol- suuel-, sue/-, sul- , {*hauhuel-) 
Meaning: sun 

Note: next to which suen-, sun-, thus of old ///7-stem; suel-^ smolder, burn ' is probably 

identical with it 

Material: 

Note: 

1. Old Indie ved. {*suuef} suvarn. = (zero grade) Avestan hvard'sun, light, sky'. Gen. 
{*suuela) surah = \ay. {*suuelio) huro. Old Indie surya- {* suluo-) m. (compare gr. nAio^, 
sura-m. "sun'; therefrom Old Indie sJ/Ya- "light, bright'. Old Indie svarnara-m. " bright 
space, ether', Avestan x'aranah-, ap. -farnah-' shining fame, magnificence '; 
Other forms in Indo-Aryan: {* suue/-a) *suuar- [\n names] "sun(god)' (Near-Eastern lA); 
Avestan: OAv. huuar9[n] (< *huuaf) "sun' (gen.sg. x^§ng< *huuanh); LAv. huuar9{gev\.sq. 
hu< *huuanh, next to hurd= Ved. suras), Sogd. (Man.) xwr^suv\\ Middle Persian xwr 
"sun', New Persian xwr^suv\\ Oss. xur/xor^suu' 

Maybe Afghan Imar, Waziri Imer, /77ye/'"sun' from Old Indie svarnara-m. " bright space, 
ether '; Armenian arew, aregak, arev, Singhalese ira "sun'. 

Maybe the oldest cognate is Luvian: {<hu-wa-ya-al-li) <huwayalla/i-' Epithet of the Sun- 
god'. 

gr. hom. n£AiO(;, Attic x\K\oc„ Doric bzk\oc„ aK\oq, Cretan ap£AiO(; Hes. (i.e. aFeAioq) "sun', 
further formations of n. *saue/to m. -/o-stem (compare Old Indie surya-); Latin so/, -/ism. 
"sun' (from neutr. *sa^e'/about *sauol, *saol); cymr. haul, acorn, heuul, mcorn. heul, houl, 
bret. heorsuu' {*sauel-); 



in addition Old Irish suili. "eye' from *suli-, ablaut equally with Old Indie surah, and alb. 

hull, uir star' {*sulo- or *suli-); 

Proto-Celtic: *sawol- / *suli- 'sun' [Noun] 

Old Irish: s^//[if] 'eye' 

Middle Welsh: haul 

Middle Breton: heuul, heul 

Cornish: heuulq\. sol, heol 

Proto-Indo-European: *seh2w6l 'sun' 

IE cognates: Skt. surya-, Latin sol, Go. saull 

Notes: The change of meaning in Olr. is understandable from the mythological context. 

'Sun' is viewed as 'the eye of the Sky'. It appears that there was still an ablauting paradigm 

in PCelt., Nom. s. *sawol, Gen. *sul-os, from which Olr. sullwas abstracted 



Note: 



[conservative definitive forms versus indefinite forms (alb. phonetic trait)], hence alb. geg
```


## [2026-09-14T01:25:19.247Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('nleaves',len(leaves))\nfor p in (1468,1756):\n    leaf=p//2+12\n    for l in range(leaf-3,leaf+3):\n        txt=leaves[l]\n        print('=====leaf',l,'for p',p,'=====')\n        print(txt[:120].replace('\\n',' | '))\nEOF",
 "description": "Locate Klein leaves for pp. 1468 and 1756"
}
```


### [2026-09-14T01:25:20.654Z] TOOL RESULT

```
nleaves 903
=====leaf 743 for p 1468 =====
ic  Greek  calendar  (corresponding  to  the  sec¬ ond  half  of  June  and  the  first  half  of  July).  — Gk.  Sxiptx
=====leaf 744 for p 1468 =====
 n.  —  It.  scopo,  ‘mark,  target,  thing  aimed at,  aim",  goal,  object’,  fr.  Gk.  avoitoq,  mark  to shoot  at, 
=====leaf 745 for p 1468 =====
.  escourgee,  ecourgee,  ‘whip, scourge’),  fr.  VL.  *ex-corrigiata,  ‘whip’,  fr.  L. ex-  (see  1st  ex-)  and  corr
=====leaf 746 for p 1468 =====
  referred  to. scriptorium,  n.,  a  writing  room  esp.  that  of  a  mon¬ astery.  —  Late  L.,  prop.  neut.  of  L.
=====leaf 747 for p 1468 =====
  ON.  skarpr, OE.  scearp ,  ‘sharp’  (see  sharp).  Cp.  Dan.  skurv, Swed.  skorv,  MDu.  scorf(t),  Du.  schurft,  O
=====leaf 748 for p 1468 =====
ence  also Swed.  sate,  Dan.  sxde;  rel.  to  OHG.  saze,  MDu. | seaward | secure | gesaete,  ‘seat’,  OHG.  gisdyi,  MHG. 
=====leaf 887 for p 1756 =====
rich’.  The  first  element  is  rel.  to  OE.  eedele, ‘noble’,  odel,  ‘home,  land',  ON.  odal,  ‘home, property’ ; 
=====leaf 888 for p 1756 =====
mbrella,  adj.  and  tr.  v. umbrette,  n.,  the  bird  called  Scopus  umbretta.  ■ — ModL.  umbretta,  fr.  F.  ombret
=====leaf 889 for p 1756 =====
nd  adj.,  understand- ing-ly,  adv.,  understand-ing-ness,  n, undertake,  tr.  and  intr.  v.  —  ME.  undertaken ;  s
=====leaf 890 for p 1756 =====
  universolog- ist,  n. | univocal,  adj.,  having  one  meaning  only.  —  Form¬ ed  with  adj.  suff.  -al  fr.  Late  L
=====leaf 891 for p 1756 =====
  the  past  participle. | urea,  n.,  crystalline  compound  found  in  the  urine of  animals  (biochem.)  —  ModL.,  fr
=====leaf 892 for p 1756 =====
us.  See  use, n.,  and  -age. | usance,  n.  —  ME.  usaunce,  fr.  OF.  ( —  F.)  usance, fr.  user,  ‘to  use’.  See  u
```


## [2026-09-14T01:25:29.072Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^soda,\\|^soda \" KLN_1966.txt | head; echo \"--- sodium ---\"; grep -n \"^sodium\" KLN_1966.txt | head; echo \"--- halo ---\"; grep -n \"^halo,\" KLN_1966.txt | head; echo \"--- helium ---\"; grep -n \"^helium\" KLN_1966.txt | head; echo \"--- X ---\"; grep -n \"^X-ray\\|^x-ray\\|^X,\\|^x,\" KLN_1966.txt | head",
 "description": "Grep Klein headwords"
}
```


### [2026-09-14T01:25:29.223Z] TOOL RESULT

```
--- sodium ---
--- halo ---
--- helium ---
--- X ---
```


## [2026-09-14T01:25:33.056Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sodanum\\|suwwad\\|sud[aā]'\\|ṣudā\" KLN_1966.txt KLN_1971.txt | head -20; echo \"=== soda any ===\"; grep -n \"soda, n\" KLN_1966.txt KLN_1971.txt | head -10; echo \"=== halo ===\"; grep -n \"halo, n\" KLN_1966.txt KLN_1971.txt | head",
 "description": "Grep Klein for soda/halo variants"
}
```


### [2026-09-14T01:25:33.176Z] TOOL RESULT

```
KLN_1971.txt:225591:sodanum, lit. ‘headache remedy’, fr. soda , 
KLN_1966.txt:35794:sod,  n.,  turf.  —  ME.  sodde,  sod,  fr.  MLG.  or MDu.  sode  (Du.  zode),  ‘turf’,  which  is  rel.  to OFris.  satha,  ‘sod’,  and  to  E.  sodden  and  seethe. Derivatives:  sod,  tr.  v.,  sodd-ing,  n. sod,  obsol.  past  tense  and  pp.  of  seethe, sod,  n.  — •  Contraction  of  sodomite, soda,  n.,  an  alkaline  substance.  —  ML.,  fr.  ML. sodanum,  lit.  ‘headache  remedy’,  fr.  soda, ‘headache’,  fr.  Arab.  sudd‘,  in  vulgar  pronun¬ ciation  $oda\  ‘splitting  headache’,  fr.  sdda‘a, ‘he  split’.  Cp.  sodalite,  sodium.
=== soda any ===
KLN_1971.txt:161871:ate of soda, natron* (stem nit hr- ; cp. Aram. 
KLN_1971.txt:225590:soda, n., an alkaline substance. — ML., fr. ML. 
=== halo ===
KLN_1971.txt:108954:halo, n., 1) a circle of light surrounding the sun
```


## [2026-09-14T01:25:39.877Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find('soda,  n.,  an  alkaline')\nleaf=t.count('\\f',0,i)\nprint('soda leaf',leaf, 'approx printed p', (leaf-12)*2, 'or', (leaf-12)*2+1)\nEOF\necho \"=== KLN1971 halo ===\"; sed -n '108954,108975p' KLN_1971.txt\necho \"=== KLN1971 helium ===\"; grep -n \"^helium, n\" KLN_1971.txt | head",
 "description": "Klein soda leaf and halo entry"
}
```


### [2026-09-14T01:25:41.160Z] TOOL RESULT

```
soda leaf 779 approx printed p 1534 or 1535
=== KLN1971 halo ===
halo, n., 1) a circle of light surrounding the sun 
or the moon; 2) radiance surrounding a head 

— F., fr. L. halo, acc. of halos, fr. Gk. aXwq, 
‘threshing floor; disk of the sun or of the moon’, 
which is of uncertain origin. Cp. halation, 
Haloa. 

Derivative: halo-ed, adj. 

halo-, combining form meaning 1) ‘salt; 2) sea’. 

— Gk. aXo-, fr. aX^, gen. ockbq (masc.), ‘salt’; 
(fern.) ‘sea’. See halieutic. 

Haloa, n., ancient Greek festival of harvest in 
honor 01 Derneter. — Gk. AAoxx or AXrpoc, 
prop, ‘threshing festival’, fr. aXtoc;, ‘threshing 
floor’. See halo. 

halogen, n., any of the four chemical elements 
chlorine, bromine, iodine, fluorine. — Lit. ‘salt- 
=== KLN1971 helium ===
111743:helium, n., name of a gaseous element (chem.) —
```


## [2026-09-14T01:25:56.857Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor pat in ['X-ray','x-ray','xanthic','xylophone','zymurgy']:\n    i=t.find(pat)\n    if i>0:\n        leaf=t.count('\\f',0,i)\n        print(pat,'leaf',leaf,'~p',(leaf-12)*2)\n        print(t[i-300:i+400].replace('\\n',' '))\n        print('---')\nEOF",
 "description": "Locate X-ray in Klein 1966"
}
```


### [2026-09-14T01:25:58.019Z] TOOL RESULT

```
X-ray leaf 689 ~p 1354
form  of  particles.  —  F.  radio¬ activity,  coined  by  the  French  physicists  and chemists  Pierre  Curie  (1859-1906)  and  his  wife Marie  (1867-1934)  in  1898  fr.  radio-  and  F.  acti¬ vity.  See  activity. radiograph,  n.,  1)  an  instrument  for  measuring radiant  energy;  2)  an  X-ray  picture.  —  Com¬ pounded  of  radio-  and  Gk.  fr.  vpa- 9Eiv,  ‘to  write’.  See  -graph. Derivatives:  radiograph-er,  n.,  radiograph-ic, radiograph-ic-al,  adjs.,  radiograph-ic-al-lv,  adv., radiograph-y,  n. Radiol  aria,  n.  pi.,  an  order  of  microscopic  marine animals  (zool.)  —  ModL.,  fr.  Late  L.  radiolus,  a little  ray’,  dimin.  of  L.  radius.  See  radius,  dimin.
---
x-ray leaf 73 ~p 122
  fr.  ttocxyjp,  ‘father’.  The Gk.  suff.  -aaxfjp  was  adopted  by  the  Latin, whence,  in  the  form  -astre,  -atre,  it  came  into the  Old  French,  resp.  the  French.  Cp.  the  words medicaster,  oleaster,  pinaster,  poetaster.  Cp.  also -ster. asteria,  n.,  a  gem  reflecting  a  six-rayed  light ( Greek  antiq.)  —  L.,  fr.  Gk.  aaxcpia,  ‘a  pre¬ cious  stone’,  prop.  fern,  of  daxipLo;,  ‘starred, starry’,  used  as  anoun,  fr.  aaxvjp,  ‘star’.  See  Aster, asterisk,  n.,  the  figure  of  a  star  (the  printing mark  *).  —  Late  L.  asteriscus,  fr.  Gk.  daxEptaxo;, dimin.  of  aaxr)p,  ‘star’.  See  Aster, asterism,  n.,  a  system  of  stars,  a  constellatio
---
```


## [2026-09-14T01:26:02.659Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor l in [860,870,880,895,900,902]:\n    print('leaf',l,repr(leaves[l][:200]))\nEOF",
 "description": "Check Klein 1966 tail leaves"
}
```


### [2026-09-14T01:26:03.862Z] TOOL RESULT

```
leaf 860 'rmine  the strength  of’,  fr.  titre,  ‘title;  right;  fineness  (of coinage),  strength,  titer  (of  solution)’,  fr.  OF. title.  See  titer.\nDerivative:  titrat-ion,  n. titre,  n.  —  A  var.  '
leaf 870 ',  v.,  and  -ation  and cp.  L.  transportatio,  gen.  -dnis,  ‘migration’. Derivatives:  transportation-al,  adj. transposal,  n.,  transposition.  —  See  next  word and  subst  suff.  -al.\ntranspo'
leaf 880 'orcer,  trusser,  trousser,  torser  (F.  trousser), ‘to  pack,  bind,  truss,  fr.  VL.  *torciare,  ‘to  twist’, a  derivative  of  *torca -  ‘bundle,  torch  .  See  torch and  cp.  torsel,  trouss'
leaf 895 ',  bodies  of  those  who were  slain  in  battle’,  wol,  ‘pestilence’,  OHG., MHG.  wal,  ‘battlefield;  slaughter’,  OHG.  wuol, ‘slaughter’,  and  cogn.  with  OIr .fuil,  ‘blood  ,  W. gweli,  ‘w'
leaf 900 'r’, vojina,  ‘war’,  Gk.  iep.ai  (for  ‘I  as¬\npire  to,  tend  to,  make  haste,  long  for’,  OE.  wap, ‘hunting’,  ON/  veidr,  ‘chase,  hunting,  fishing’, OHG.  weida,  MHG.,  G.  weidc,  ‘pastu'
leaf 902 '��true’,  and  Gk. ruov,  fr.  mtoraiv,  ‘to  look  at,  examine’.  See very  and  -scope.  The  correct  form  would  be alethoscope  (fr.  Gk.  dcXvjffrji;,  ‘true’  and  -rsy.6- mov ) .\nveratral,  '
```


## [2026-09-14T01:26:08.453Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"shai\\b\\|shai'\\|'thing'.*Arab\\|Arab.*shay\" KLN_1971.txt | head -20; echo \"=== X entries ===\"; grep -n \"^X, \\|^x, \\|^X-ray\\|^X-rays\\|^x-ray\" KLN_1971.txt | head",
 "description": "Grep Klein 1971 for X / shay"
}
```


### [2026-09-14T01:26:08.539Z] TOOL RESULT

```
212949:of s.m. Aram.-Syr. sdtana , Arab, shay tan , ‘ad- 
220281:tribe or clan. — Arab, shaykh, ‘an old man, 
268901:x, shortened fr. Arab, shay, ‘a thing, something’, 
=== X entries ===
199324:X-rays and other rays. — Compounded of ra- 
268900:X, x, principal unknown quantity ( alg .) — Sp. X, 
268901:x, shortened fr. Arab, shay, ‘a thing, something’, 
269151:X-rays ), to suggest that the exact nature of
```


## [2026-09-14T01:26:11.539Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '268890,268920p' KLN_1971.txt; echo \"=== xray ===\"; sed -n '269140,269160p' KLN_1971.txt; echo \"=== helium ===\"; sed -n '111743,111760p' KLN_1971.txt",
 "description": "Read Klein X, X-ray, helium entries"
}
```


### [2026-09-14T01:26:11.679Z] TOOL RESULT

```
(1324-1404), founder of the College. For the 
ending see suff. -ist. 

wynd, n., an alley (Scot.) — A spelling var. of 
wind, ‘a turning’. See wind, ‘to turn’, 
wyvem, n. — See wivern. 




X, x, principal unknown quantity ( alg .) — Sp. X, 
x, shortened fr. Arab, shay, ‘a thing, something’, 
used also in the sense of ‘unknown quantity’ (in 
Medieval Spanish x was pronounced sh ); in- 
troduced by Descartes. Cp. X rays, 
xanth-, form of xantho- before a vowel, 
xanthein, n., soluble yellow coloring matter in 
flowers {chem.) — Formed with suff. -in fr. Gk. 
£av&6i;, ‘yellow’. See xantho-. 
xanthelasma, n., a synonym of xanthoma ( med .) 

— Medical L., compounded of xanth- and Gk. 
6Xao(ia, ‘a metal plate’, which derives fr. £Xav, 
‘to drive, strike’. See elastic and cp. elasmo-. For 
the ending see suff. -ma. 

Xanthian, adj., pertaining to Xanthus. — Formed 
with suff. -Ian fr. Xanthus , name of a city in 
Lycia in Asia Minor. 

xanihic, adj., yellowish. — Formed with adj. 
=== xray ===

Xmas, n., Christmas. — Prop. = X, the Greek 
letter chi, as the initial letter of Xpiax6<; (see 
Christ) and -mas (in Christmas), 
xoanon, n., a primitive wooden image {Greek an- 
tiq.) — Gk. 56avov, ‘an image carved of wood’, 
from the stem of £etv ‘to scrape, scratch, pol- 
ish’, which is rel. to of s.m. See xyster. 
X rays, n. pi., Roentgen rays. — They were called 
by their discoverer Wilhelm Konrad von 
Roentgen (1845-1923) (in 1 896) X Strahlen (= 
X-rays ), to suggest that the exact nature of 
radiation was unknown. For such use of the 
letter x see X, x. 

xyl-, form of xylo- before a vowel, 
xylem, n., woody tissue in higher plants, the op- 
posite of phloem {bot.) — G. Xylem, coined by 
the botanist Karl Wilhelm von Nageli (1817-91), 
fr. Gk. 56Xov, ‘wood*. See xylo-. 
xylene, n., any of three isomeric hydrocarbons 
=== helium ===
helium, n., name of a gaseous element (chem.) — 
ModL., fr. Gk. t)Xw<;, ‘the sun’; so called by 
the English astronomer Sir Joseph Norman 
Lockyer (1836-1920) and the English chemist 
Sir Edward Frankland (1825-99), because it was 
first observed by them in the spectrum of the 
sun (in 1868, during an eclipse). See heliacal 
and -ium. 

helix, n., spiral line. — L., fr. Gk. gXd; (for 
*f£Xi£,)> ‘spiral, coil’, from the stem of £Xiooetv 
(for *fcX(xtetv), ‘to turn about, wind, roll’, 
fr. I.-E. base *wel-, ‘to bend, turn, twist, roll’. 
See volute and words there referred to and cp. 
esp. Helicon, helminth. 

hell, n. — ME. helle, fr. OE. hell, rel. to OS. hellja , 
ON. hel, OFris. helle , hille, Du. hel, OHG. hel-
```


## [2026-09-14T01:26:20.962Z] TOOL CALL #25: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-14T01:26:20.969Z] TOOL RESULT

```


```


## [2026-09-14T01:26:24.311Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%85%CE%BB%CF%89%CF%82",
 "prompt": "Give the Ancient Greek entry for ἅλως: etymology, meanings, and whether it is related to ἥλιος 'sun'. Quote Beekes or other cited views."
}
```


## [2026-09-14T01:26:25.880Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%87%D8%A7%D9%84%D8%A9",
 "prompt": "Give the Arabic entry هالة: etymology, meaning (halo around moon/sun), and any stated Greek origin. Also any Persian section."
}
```


### [2026-09-14T01:26:27.319Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T01:26:29.736Z] TOOL RESULT

```
# ἅλως (hálōs) - Ancient Greek Entry

## Etymology
The Wiktionary source states the word is "Probably from Pre-Greek." It notes a comparison with Albanian *lëmë* and its proto-form, but offers no connection to ἥλιος (hélios, 'sun').

## Meanings
The noun has eight primary senses:

1. Threshing floor
2. Grain on the floor
3. Disk (of sun, moon, or shield)
4. Halo
5. Serpent's coil
6. Bird's nest
7. Ciliary body of the eye
8. Circular piazza at Delphi

## Relationship to ἥλιος
The provided source does **not** discuss any connection between ἅλως and ἥλιος ('sun'). While meaning 3 involves solar imagery, no etymological link is established in this material. The Wiktionary entry attributes the word to a Pre-Greek substrate rather than Indo-European origins, suggesting independent development from Greek's sun-word.

No secondary sources like Beekes are cited in the excerpt provided.
```


## [2026-09-14T01:26:33.721Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%87%D8%A7%D9%84%D9%87",
 "prompt": "Persian هاله: etymology (Arabic هالة from Greek?), meaning. Quote the etymology section verbatim."
}
```


## [2026-09-14T01:26:34.768Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/halo",
 "prompt": "Give the full etymology of 'halo' as printed, including the Greek halos and its origin."
}
```


### [2026-09-14T01:26:36.756Z] TOOL RESULT

```
# Persian هاله Etymology

The etymology section states:

"Borrowed from Arabic _هالة_ (hāla, "halo"), from Ancient Greek _ἅλως_ (hálōs, "halo")."

In summary, the Persian word هاله traces back through Arabic to Ancient Greek origins, with the meaning of "halo" preserved across all three languages.
```


### [2026-09-14T01:26:39.059Z] TOOL RESULT

```
# Etymology of "Halo"

The word "halo" entered English in the 1560s from Latin *halos*, which derived from Greek *halos* meaning "disk of the sun or moon; ring of light around the sun or moon."

**Origin of the Greek term:** The Greek *halos* has "unknown origin," though etymologists suggest the primary sense was likely "threshing floor" — referencing "a circular path" made by oxen treading grain. The semantic progression moved from the circular path to "disk" and eventually to the modern sense of a luminous ring.

**Semantic evolution:** The religious meaning — "light around the head of a holy person or deity" — first appeared in the 1640s, significantly later than the astronomical sense. The word functioned as a verb starting in 1791.
```


## [2026-09-14T01:26:45.476Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%A5%CE%BB%CE%B9%CE%BF%CF%82",
 "prompt": "Ancient Greek ἥλιος: etymology (PIE root, Doric/Aeolic forms like ἅλιος, ἀέλιος), cited authorities."
}
```


## [2026-09-14T01:26:46.797Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/soda",
 "prompt": "Full etymology of 'soda' as printed, including any mention of Arabic suwwad or suda' (headache), and Medieval Latin sodanum."
}
```


### [2026-09-14T01:26:51.367Z] TOOL RESULT

```
# ἥλιος (Ancient Greek for "Sun")

**Primary Definition:**
The term means "sun" in Ancient Greek, functioning as a masculine noun in the second declension.

**Etymology:**
The word traces back through Proto-Hellenic *hāwélios* to Proto-Indo-European *sóh₂wl̥*. According to the source, it shares cognates across multiple language families, including Latin *sol*, Sanskrit *sū́rya*, and Old Church Slavonic *slŭnĭce*.

**Dialectal Variants:**
Different Greek dialects employed alternative forms:
- Epic/Ionic: ἠέλῐος (ēélĭos)
- Lyric/Aeolic/Doric: ᾱ̓έλῐος (āélĭos)
- Lyric: ᾱ̔́λῐος (hā́lĭos)

**Secondary Meanings:**
Beyond its primary sense, the word also denoted "east," "day," and "sunshine" in Ancient Greek usage.

**Historical Attestation:**
A notable example appears in Plutarch's *Life of Alexander the Great* (46–120 CE), where Diogenes famously requests Alexander to "stand a little out of my sun."
```


### [2026-09-14T01:26:52.674Z] TOOL RESULT

```
# Etymology of "Soda"

The word "soda" entered English in the late 15th century, referring to sodium carbonate extracted from ashes. It derives from Italian *sida* or Medieval Latin *soda*, tracing back to a saltwort plant used to produce the substance.

## Proposed Origins

The exact source remains uncertain, with several theories proposed:

- **Catalan connection**: Possibly from Catalan *sosa* (attested from the late 13th century), itself of unclear origin
- **Arabic origin**: An Arabic name for saltwort has been suggested but lacks attestation
- **Medical theory**: Some scholars trace it to Medieval Latin *sodanum*, a "headache remedy" allegedly derived from Arabic *suda* meaning "splitting headache," though this theory is "considered far-fetched in some quarters"

## Historical Development

Soda was a major medieval Mediterranean trade commodity before French commercial manufacturing began in the late 18th century. The term's meaning shifted dramatically in the 19th century—by 1834, it referred to carbonated water, specifically "a shortening of **_soda water_** (1802)." Modern usage typically denotes flavored, sweetened carbonated beverages, with "soda pop" first appearing around 1863.

Related terms include soda crackers (1863), soda bread (1850), and soda fountain (1824).
```


## [2026-09-14T01:26:59.437Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/soda",
 "prompt": "English 'soda' etymology section verbatim: all proposed origins (Arabic suwwad, sawwad, suda' headache, Medieval Latin sodanum, Catalan sosa), and what the entry says is most likely."
}
```


## [2026-09-14T01:27:01.219Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B5%D8%AF%D8%A7%D8%B9",
 "prompt": "Arabic صداع (ṣudāʿ): root, meaning, derivation from صدع ṣadaʿa 'to split'. Also any Persian section for صداع."
}
```


### [2026-09-14T01:27:05.318Z] TOOL RESULT

```
# Etymology of "Soda"

Based on the Wiktionary entry, the English word "soda" has a straightforward documented origin:

**Primary Source:** The entry states that English "soda" comes "From Italian _soda_." The word then traces back further through an etymology tree showing it ultimately derives from Arabic _سُوَيْدَاء_ (suwaydāʔ), which refers to the plant *Suaeda*.

**The Entry's Assessment:** Regarding multiple proposed origins, the source indicates these are historical variants in Arabic dialects, noting that certain forms "have several variants in Arabic dialects only recorded later."

**Secondary Meaning:** The entry notes that sense 4 (carbonated beverage) represents "an ellipsis of _soda water_," showing this usage developed as a shortening of the compound term rather than from independent etymology.

The documentation presents Italian as the immediate source language, with Arabic plant nomenclature as the ultimate origin—a path typical of words describing chemical compounds that entered European languages through trade and scientific exchange.
```


### [2026-09-14T01:27:06.011Z] TOOL RESULT

```
# صداع (Headache/Noise)

Based on the Wiktionary entry, **صداع** (ṣudāʕ) is an Arabic noun with the following definitions:

## Arabic
The primary meaning is **headache**. The word is masculine and uncountable, derived from the root "ص د ع" (ṣ d ʕ).

**Pronunciation:** /sˤu.daːʕ/

A derived term is صُدَاع نِصْفِي (migraine).

## Moroccan Arabic
In Moroccan Arabic dialect, the same word carries two distinct meanings:
- **Noise**
- **Ache**

The Moroccan form is pronounced /sˤdaːʕ/ and uses the plural **صداعات** (ṣdāʕāt).

The Moroccan Arabic version is inherited from the Classical Arabic term, showing how the word evolved differently across Arabic dialects while maintaining its connection to physical discomfort.
```


## [2026-09-14T01:27:15.081Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | grep -i \"MON\\|PLA\\|ARY\\|TAD\"; echo \"=== MON part1 head ===\"; head -c 500 MON_part1.txt; echo; echo \"=== grep هاله in MON ===\"; grep -c \"هاله\" MON_part1.txt MON_part2.txt 2>/dev/null",
 "description": "Check MON files"
}
```


### [2026-09-14T01:27:15.163Z] TOOL RESULT

```
MON_part1.txt
MON_part2.txt
NYB_vol2_glossary.txt
TAD_pages.txt
TAD.txt
=== MON part1 head ===
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س 


همجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نامه مدش نامع 

مه مر وه ود 

3 ور 133131313 


هم مشب جج جب بیج چم مدوجو 
چم وم 
جر 


درل ولو ونر نو تلا رت 
11 


مج جرج جر یی م�
=== grep هاله in MON ===
MON_part1.txt:11
MON_part2.txt:10
```


## [2026-09-14T01:27:24.151Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TAD هالة ===\"; grep -n \"هالة\\|هاله\" TAD_pages.txt | head -20; echo \"=== TAD leaves ===\"; python3 -c \"\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read(); print(len(t.split(chr(12))))\"",
 "description": "Grep TAD for هالة"
}
```


### [2026-09-14T01:27:25.230Z] TOOL RESULT

```
=== TAD هالة ===
581: ‫ايطالي ‪6001829‬م معناه نسيج يبلغالىالعقب ‪ .‬وقد جرى استهاله‬           ‫ينطلون‬
2830:                      ‫ونالى وهاه وهو الطنياوة والدارة حولالقمر واك‬                   ‫هالة ‪-‬‬
=== TAD leaves ===
87
```


## [2026-09-14T01:27:26.147Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in LKT.txt AFM.txt FVQ_pages.txt AFA.txt DOZ.txt DEV.txt; do echo \"=== $f ===\"; grep -n -i \"soda\\b\\|sodanum\\|suwwad\\|suwaida\" $f | head -5; done",
 "description": "Grep Arabism dictionaries for soda"
}
```


### [2026-09-14T01:27:27.285Z] TOOL RESULT

```
=== LKT.txt ===
3952:'Alaun';  hieraus  mit  ar.  Art.  sp.  (alt) axebe,  enxebe,jebe,  jepe  'dass.',  siz.  scerba 'Asche'  [wenig  gebräuchlich].  —  Aus sabb  knbti  'ägyptischer  Alaun'  [zu  kubti s.  hier  Nr.  1222]  wurde  sp.  mezacote 'Soda',  it.  tnarzacotto  'Glasur',  frz.  rnas- &icot  'Bleigelb'.  [DE  219.  Eguilaz  312. 423.  SEYBOLD  in  ZDMG  LXVHI,  623. ML  7677  a.  GrSVociSic  245.
=== AFM.txt ===
=== FVQ_pages.txt ===
=== AFA.txt ===
=== DOZ.txt ===
=== DEV.txt ===
2133:Soda.  Ancien  ternie  de  médecine,  violent  mal  de  tête. De  l'arabe  ^î*Xo  sodâ\  même  sens,  qui  se  rattache  à  ^*>wo sacla,  fendre  en  deux.
4330:Soda.
4917:^!js*s  voy.  Soda.
```


## [2026-09-14T01:27:35.486Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2125,2140p' DEV.txt; echo \"=== 4325 ===\"; sed -n '4322,4335p' DEV.txt; echo \"=== 4910 ===\"; sed -n '4910,4922p' DEV.txt; echo \"=== LKT Soda ===\"; grep -n \"Soda'\\|'Soda\\|Soda\\b\" LKT.txt | head -12",
 "description": "Read Devic soda entries and Lokotsch"
}
```


### [2026-09-14T01:27:35.607Z] TOOL RESULT

```
Sirop.  \  ieu\  français  essyrot  (xiif  siècle),  ijsserop  (xv" siècle),  provenir',  elssarop,  issarop,  yssarop ,  esp.  xarahe , nxarnbe,  axarave,  axnrope,  jarah,  jarope,  portug.  xaropc (^surrapa,  zurappa,  vin  qui  a  perdu  sa  force ^),  ital.  siroppo, mvoppo,  sciloppo,  bas  lat.  syrupus,  siruppus,  sciruppus.  De l'arabe  vlr^  charâh ,  boisson,  vin,  café,  venant  du  verbe LjJi*  charih,  boire.  On  voit  qu'un  grand  nombre  des  formes citées  ont  conservé  l'article  [ach-charâh);  plusieurs  ont  pu t'tre  faites  sur  cj^^àJI  ach-charoûb ,  boisson.
te  mot  arabe  cliarâh  a  aussi  signifié  sirop ,  comme  on peut  le  voir  par  les  dérivés  j,îyi  charâhi,  «  syruporum  ven- ditor»,  jL?iyi  charâbâll^,  cr qui  syrupos  conficit  aut  ven- dit. ??  (Freytag.)  Voy.  aussi  Dozy,  Gloss.  p.  218.
Smala  ou  Zmala.  Ce  mot  nous  est  venu  d'Algérie;  c'est l'arabe  ilUy  azmala  ou  iCA^^  zamala  (prononcé  zmala  par  les Algériens),  qui  signifie  la  famille  d'un  chef  et  son  mobilier, venant  de  la  racine  Juv  zamal,  porter.  De  cette  même  ra- cine est  venu  iCULÎi  az-zâmila,  qui  a  donné  l'espagnol  ace- mila,  bête  de  somme,  en  portugais  azemela,  azimela,  azc- mela,  azernala.
'  Dans  Bocthor.
^   Dans  la  Fabrica  lino-.  nrnh.  qui  donne  5j-^  ve\do  orientale ^  enrus ,  ol ^^-Li  sctrocco,  euronotiis. ^  Gloss.  p.  35fi.
'*  Compar.  ^^  =  ^,  ^^  -  ^'  >>yi  =  »xAj>,  <j>y'i  =  \Jd3,  etc. '■•  Siiroppa ,  zurappa  manquent  dans  le  Closs.  de  M.  Dozy. "  Pharmacien  ,  dans  llodhov,  iWi  mol  spatule.
1/.
210  DICTIONNAIRE  ÉTYMOLOGIQUE
Soda.  Ancien  ternie  de  médecine,  violent  mal  de  tête. De  l'arabe  ^î*Xo  sodâ\  même  sens,  qui  se  rattache  à  ^*>wo sacla,  fendre  en  deux.
Sofa  ou  Sopha.  Portug.  sofa.  De  l'arabe  iiÀ^  ^f^ff'h même  sens,  dans  Bocthor  et  dans  Gberbonneau,  scamnuni (Uscubitorium  dans  Freytag,  et  aussi  h  siêf^e  de  la  selle.
Solive.  Ce  terme  de  charpenterie,  dont  l'origine  ne  pa- raît se  rattacher  ni  au  latin  ni  aux  langues  du  même groupe,  offre  une  grande  analogie  de  son  et  de  sens  avec l'arabe  l^J^  salah,  salih ,  arbre  d'une  longueur  notable, et  <-^AkM  sahb ,  arbre  dépouillé  de  branches.  Est-ce  une pure  coïncidence?  Rappelons  que  l'art  du  charpentier  a emprunté  un  certain  nombre  de  mots  à  la  langue  arabe.
SoPHi.  ^^Le  nom  de  sopin  donné  aux  souverains  de  la Perse,  pendant  les  xvf  et  xvii'  siècles,  dit  M.  De^rémery^ doit  son  origine  à  ^^yu^  sefewi,  adjectif  relatif  ou  patrony- mique, dérivé  du  nom  du  cheikh  Séfi,  sixième  ancêtre  du chah  Ismaïl,  fondateur  de  la  dynastie  des  Séjis  ou  mieux Séfévis.  55  On  a  dit  soplu  sans  doute  par  confusion  avec  le terme  soufi,  ci-après.
SouFi.  Transcription  de  l'arabe  ^^ao  soiifi,  sage,  reli- gieux, qu'on  veut  tirer  de  Oy^  souf,  laine,  les  soufis  étant tenus  de  porter  des  vêtements  de  hiine  et  non  de  soie; d'autres  disent  du  grec  cTo(p6s,  sage.
Sourate.  Verset  du  Coran.  De  l'arabe  i^yM  soûra,  pro- noncé sourat  lorsque  le  mot  est  en  connexion  avec  celui qui  suit.
'   Jonrn.  (taiai.  aotU  1807,  p.  iSû.
DES  MOTS  D'ORIGINE  ORIENTALE.  2H
=== 4325 ===
Siroco,  esp.  voy.  Siroc.
Sirop.
Siroppo,  esp.  voy.  Sirop.
Sirucum,  lat.  voy.  Jargon.
Siruppus,  b.  lat.  voy.  Sirop,
Skoh,  gotli.  voy.  Escarpin,
Socoran,  voy.  Sucre.
Socouran,  voy.  Sucre.
Soda.
Sofa.
Soldan ,  e.sjt;.  voy.  Sultan,
Soldano,  ilal.  voy.  Sultan.
SoidSo,  pg.  voy.  Sultan.
Solive.
=== 4910 ===
jg-i  voy.  Cheikh,  Echecs.
yUa^  voy.  Satan.
^Ja-v-i  voy.  Cétérach.
j-^  voy.  Schiite.
45-^Lo  turc,  voy.  Chagrin.
^La3  voy.  Azerbe.
^30sj^  pei's.  voy.  Sadder.
^!js*s  voy.  Soda.
vjsoo  voy.  Zédaron.
^jj^yo  voy.  Astronomie,  38.
(SyJtMS  turc,  voy.  Chagrin.
xJua  voy.  Sofa.
yuo  voy.  Safre,  ChifTre.
=== LKT Soda ===
3952:'Alaun';  hieraus  mit  ar.  Art.  sp.  (alt) axebe,  enxebe,jebe,  jepe  'dass.',  siz.  scerba 'Asche'  [wenig  gebräuchlich].  —  Aus sabb  knbti  'ägyptischer  Alaun'  [zu  kubti s.  hier  Nr.  1222]  wurde  sp.  mezacote 'Soda',  it.  tnarzacotto  'Glasur',  frz.  rnas- &icot  'Bleigelb'.  [DE  219.  Eguilaz  312. 423.  SEYBOLD  in  ZDMG  LXVHI,  623. ML  7677  a.  GrSVociSic  245.
4839:'Provinz'  [von  tvcilä  'regieren,  verwalten', daher  ar.  wäli  'Gouverneur'  ^  frz.  mli, dtsch.  Wali];  über  tk.  tvilajet  hieraus frz.  vilayet,  dtsch.  Wilajet;  angloind. bilayut,  hiUa'it  Bezeichnung  für  'Europa' [daher  bind,  biläyati  päni  'europäisches Wasser',  d.  h.  'Sodawasser'].  [Devic  22.5. Hobson-Jobson  93/94.
```


## [2026-09-14T01:27:43.893Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT suwwad/soda plant ===\"; grep -n -i \"suwwäd\\|suwwad\\|suwaid\\|Natron\\|sodä\" LKT.txt | head -10; echo \"=== SKT soda ===\"; grep -n -i \"soda\" SKT.txt | head -10; echo \"=== FSD soda ===\"; grep -n -i \"sodanum\" FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt 2>/dev/null | head -5",
 "description": "Grep Lokotsch, Skeat, Funk for soda"
}
```


### [2026-09-14T01:27:44.005Z] TOOL RESULT

```
=== LKT suwwad/soda plant ===
982:[Aus  pers.  büräh]  'Borax,  borsaures Natron';  hieraus  mit  gleicher  Bedeutung sp.  borraj,  pg.  borax  [auch  tincal],  frz. borax,  it.  borrace;  ndl.  engl,  borax, dtsch.  Borax;  russ.  bulg.  bura,  serb. poln.  boraks.  cech.  borax.  [DE  241. Devic  DEt  70.
3601:'Natron'  [Prov.  25,20;  Jer  2.22;  wohl wie  aram.  niträ  aus  äg.  ntrj.],  hieraus gr.  vixpov,  lat.  nitrum  und  mit  lat.  sal zusammengesetzt:  it.  salnitro,  pg.  sp. salitre,  rum,  ^alitru;  dtsch.  Salniter, (dial.)  Saliter;  cech.  sahii/tr,  sanytr,  poln. saletra,  russ.  stlitra,  serb.  saliira  'Sal- peter'. Aus  ar.  natrün  ergab  sich  frz. engl.  7iatron,  dtsch.  Natron  und  mit  ar. Art.  sp.  anatron.
5852:3^a&ofe  1542 Nadir  1565 Nankint'gJ  1554 Naphtha  1538 J^a/-(/e  1548 Natron  1567 JV^afscfe  1530 Neschires  j.  127 iST/if/r/M  1569 Nirwana  1573 Nischan  1574
6105:nargeela  1556 I  narghile  1556 i  nargileh  1556 I  natron  1567 I  nautch  1530 I  »let'Z  1568
6635:narguilS  1556 j  natron  1567
9972:almojarife  1519 almojarra  1439 almojatre  1581 alnirineda  1511 almoraduj  1411 ahnotacen  1503 almozal(l)a  1511  a almucio  1520 almud  1490 almuecin  1485 almuidano  1485 aloque(ro)  803 aloqueria  803 alpargata  243 alpicoz  576 alquequenge  1016 alqueria  1096 alquez  1174 alquifol  1227 aquilar  1181 alquile(r)  1181 alquhnia  1157 alquitara  1130 alqmtrdn  1128 altramuz  2115 alubia  1333 «Zmc^cZ  2142 aluquete  2153 aZfaci/  2160 amacena  476 amalgama  1378 amapola  762  d amargaza  829 amarillo  70 mnbar  78 amoscarse  1436 amuco  71 amtileto  866 amusco  1515  a anacal(o)  1545 anadel  1566 «w«/?/  1537 anafre  130 anatron  1567 anazea  1583 andamio  520 annafe  130 ante(ado)  1305 antimonio  918 anzarote  86 afiacal  1545 anacea  1583 anaciar  1583 anafil  1537 öw«7  1568 «/Itr  1568 arac  92 arambel  811 arancel  1428 arfceZW  dial.  204 arhollön  204 arcaditz  988
=== SKT soda ===
553:Alkali,  a  salt.  tArab.^      AmK  «/, amlya//,  ashes  of  glass-wort,  ^\hich  al in  soda.
9388:euddoiL  (F.  *  L.)     M.  £.  sodain.  *  0»\
16912:aooial.  (L.)  L.  sodalis,  adj.,  from  nvjMi (above).
17685:Soda ;  see  Solid.
17762:soda.  '  a  kind  of  feame  iL»hcs  whereof  they
23447:lie,  signor  (signior),  size  ^a),  soda,
=== FSD soda ===
```


## [2026-09-14T01:27:47.204Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17755,17775p' SKT.txt; echo \"=== Solid ===\"; grep -n \"^Solid\\|Solid, firm\" SKT.txt | head -3",
 "description": "Read Skeat soda entry"
}
```


### [2026-09-14T01:27:47.274Z] TOOL RESULT

```
—  returning  at  the  end  of  a  complete  vear. The  O  Lat.  jc//ia-Gk.  o\ot,  cntirc'Skt. sarva,  all,  entire.     Der.  solemn-ity.  -he.
SolfJft,  to  tii^  the  notes  of  the  gamut. ^L.)  It  means  lo  sing  the  notes  oy  the names  si,  la,  toit/ot  mi,  re,  ut  (where,  for «/,  tio  i.<i  now  used).  These  names  arc  of L.  origin ;  see  Gamut.  Dor.  iol/tg^o. from  Ital.  solftg^o,  the  singing  of  the gamut ;  also  S(U-mi-sati<m,  coinen  from  s^l and  mi.
Solicit.  (F.  -  L.)  F,  solidter.  -  L. soUicitart,  lo  agitate,  arouse,  urge,  solicit.
—  L.  soUicitus,  lit.  wholly  agitated.  *  L. «//j-,  for  toih;  crude  form  of  sollus,  whole  ; ff'/wi.  aroused,  pp.  of  eiere,  to  shake,  excite. See  Solemn  and  Oite.  Der.  nt/ici/ot4s, for  L.  soilidtus;  sa/icitude,  F,  toliciiiuU, from  L.  soHiitndo,  anxiety.
Solid.  (F.-L.)  F.  ufidi.~t,.  seU'ifum, Bcc,  of  soliJuSy  firm.  Allied  lo  O.  Lat. Melius,  whole;  sec  Solemn.  Der.  ioliJ- ar-i-ty,  'n  word  which  we  owe  to  the  F. communists,  and  which  »ignifies  a  fellow- ship in  gain  and  loss,  a  being,  so  to  speak. all  in  ihe  same  bottom.'  Trench.  AUo solid'ify,  from  F.  soiidificr,  to  render solid.
consolidate.  (L.)  From  pp.  of  L. toit'sotidart,  to  render  solid.  — L.r£i/«-  {cum\ together :  soHdare,  to  make  solid,  from soTidui.  Der  totuols,  a  fajnilior  abbievia- tion  for  eoruoiidated  annuiiies.
8od&.  (Ital  w  L.)     IiaI.  loda,  O.  Ita!.
soda.  '  a  kind  of  feame  iL»hcs  whereof  they
make  glasses:'  Florio,     Fern  of  Ital.  rnib,
•oiide,  tough;*   ibid,     (bimtlariy   O.  F.
SOLVE.
toulde.   glasswort,    answers    (o   L prob.  from  the  hardness  of  the obtained    from    glasswort.^  ~  L solid,  hard.     Der.  sod-iumt  a  coined
soder,  solder,   a    firm    ceincot fuiible  metals.  (F.-U)     Fonnerty so-.OiUr,    sometimes    iPuUftr  i sod'ur.  —  O.  F.   soudurt^  alfo souldering,    and    pailiculaily    th soulder  which  fastens  Ihe  IrdJ glaise  window;'  Cot.     ^Mod.  r. »  O.  F.  souder,  seuidir,  to  codsoI firm.  •  L.  fvlidare,  to  make  firm.  •  L. ftrm.
Boldier.  (F.-L.)  M.  E.  mfiw'. our.  souJdur.  •  O.  F.  iolJur,  lomUin, doyer,  one  who  fights  for  pay:  li* jtf/i/ariJw.  —  Low  L-  soldum.  |4y.»Le* joUdus,  a  piece  of  money  iwhcnoe  0. sol,  F.  sou'w  orig^  'a  solid  pie**** jolidus,  solid  ;  cf.  £.  '  hard  cash.*
BOlipad,  an  animal  with  udcIovn (L.)     Short  for  sclidiffd.^\^.  m^ stem  of  lo/idipes.  solid-hoofed  ^Flinjl solidi;  for  s^idus,  solid  ;  /«r.  •  M« Foot.
•ou.  <F.  -  L.)    F.  torn.  O.  F.  mI,  t —  Low  L.  solidvs,  solid,  also  a  ecu /.  /.  d.,  L  e.  libra,  soiidi^  denarii. Soliloquy ;  see  LoQuaotoua. Soliped :  see  Solid. Solitary.  Solitude,   Solo ;  Me  H (.^). Solmisation  ;  aee  Solfa. Solstice;  see  Solar Soluble,  Solution  ;  sec  Batra. Solve.  iL  )     L.  solurwt,  lo  loosot.  rri ex.pUiD  :  pp.  Wu/mj— L.r^,  fo(  «-.t{fl imerty  to  looscu,  allie*!  to  t-ik.  Av-«ir.  tv free,  and  to  E.  Ijose.     Der.  t^StM.  b the  htein  of  (he  prcs.  pt.
absolute,  un  re  .strained,   complete  it L  absplutus,  pp.  of  adsctuert»  lo  »cl  i sec  Itelow.
absolve.  (U)    X^aAiotuttt.XatA ■>L.  ab,  awny ;  solue^t,  to   loowaa abi&lHt-ioH  iStom  j^p.  ahteiuiuM^
dissolute.    i.L.>      I.,  dissvimtm^  I tious :  pp.  of  L.  dtstfiiture  i,beliiw)k
dissolve.  (L.T  L  ditrcfmrr^ solve.  l<>osco.  relax  —  L.  dit  ,  aj^rt ; to  looiicn.  Der.  disj^^ui-ifim  i^irvm se/u/Hi').
resolute.  (U)  L.  ru«h*i, nseltute  (below).
=== Solid ===
17759:Solid.  (F.-L.)  F.  ufidi.~t,.  seU'ifum, Bcc,  of  soliJuSy  firm.  Allied  lo  O.  Lat. Melius,  whole;  sec  Solemn.  Der.  ioliJ- ar-i-ty,  'n  word  which  we  owe  to  the  F. communists,  and  which  »ignifies  a  fellow- ship in  gain  and  loss,  a  being,  so  to  speak. all  in  ihe  same  bottom.'  Trench.  AUo solid'ify,  from  F.  soiidificr,  to  render solid.
```


## [2026-09-14T01:27:55.939Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%87%D8%A7%D9%84%D9%87/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for هاله: the origin tag (e.g. [ع.] or [يو.]) and the definition, verbatim in Persian."
}
```


## [2026-09-14T01:27:56.784Z] TOOL CALL #41: WebSearch

```json
{
 "query": "Cajori Descartes x unknown quantity Arabic shay myth Spanish xei historians reject"
}
```


### [2026-09-14T01:28:01.726Z] TOOL RESULT

```
# فرهنگ معین Entry for هاله

**Origin tag:** (لِ) (اِ.)

**Definition:** "خرمن ماه ، دایرة نورانی که گاه گاه گرداگرد ماه ظاهر می شود"

(A luminous circle that occasionally appears around the moon, known as the lunar halo)

An additional entry notes: "عدل ، لنگه" (justice, a unit of weight)
```


### [2026-09-14T01:28:04.243Z] TOOL RESULT

```
Web search results for query: "Cajori Descartes x unknown quantity Arabic shay myth Spanish xei historians reject"

Links: [{"title":"The Mysterious Origins of 'X' in Algebra | Scientific American","url":"https://www.scientificamerican.com/article/mysterious-origins-of-x-in-algebra/"},{"title":"xay | WordReference Forums","url":"https://forum.wordreference.com/threads/xay.3038052/"},{"title":"Why We Use \"X\" as the Unknown in Math","url":"https://gizmodo.com/why-we-use-x-as-the-unknown-in-math-1657254357"},{"title":"The Origins of the Mathematical Convention of Using \"X\" as the Unknown","url":"http://www.todayifoundout.com/index.php/2014/11/origins-mathematical-convention-using-x-unknown/"},{"title":"Earliest Uses of Symbols for Variables","url":"https://www.math.hawaii.edu/~tom/history/variables.html"},{"title":"Earliest Uses of Symbols for Variables - MacTutor History of Mathematics","url":"https://mathshistory.st-andrews.ac.uk/Miller/mathsym/variables/"},{"title":"View question - Why do we use x to represent an unknown number?","url":"https://web2.0calc.com/questions/why-do-we-use-x-to-represent-an-unknown-number"},{"title":"why_x","url":"https://langnhist.weebly.com/why_x.html"}]

Based on the search results, here's what I found regarding Cajori, Descartes, and the origins of "x" as the unknown quantity:

## Key Findings

Florian Cajori's "A History of Mathematical Notations" (1929) notes that Descartes seems to be the creator of the practice of using "x" for an unknown, based on documented evidence.

However, regarding the Arabic/Spanish etymology myth:

Cajori says there is no evidence for the popular theory that x derives from the Arabic word "shei" (meaning "thing") transcribed as "xei" in medieval times. Similarly, there is no evidence in support of the hypothesis that x is derived ultimately from the medieval transliteration "xei" of Arabic "shei," used by the Arabs to denote the unknown quantity.

## What Descartes Actually Did

The introduction of x, y, z as symbols of unknown quantities is due to Descartes (Géométrie, 1637), who, in order to provide symbols of unknowns corresponding to the symbols a, b, c of knowns, took the last letter of the alphabet, z, for the first unknown and proceeded backwards to y and x for the second and third respectively.

So while historians like Cajori have thoroughly rejected the Arabic etymology myth, they attribute the modern use of "x" as an unknown directly to Descartes' systematic choice of the last letters of the alphabet.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T01:28:09.020Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://mathshistory.st-andrews.ac.uk/Miller/mathsym/variables/",
 "prompt": "Quote what is said about the origin of x as the symbol for the unknown: Descartes, Cajori, and the Arabic 'shei'/'xei' theory."
}
```


## [2026-09-14T01:28:10.894Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B5%D8%AF%D8%A7%D8%B9/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for صداع verbatim, including the origin tag such as [ع.] (Arabic)."
}
```


### [2026-09-14T01:28:14.048Z] TOOL RESULT

```
# Origins of X as the Unknown Symbol

**Descartes' Approach:**
Descartes introduced x, y, and z systematically in his 1637 *Géométrie*, using the last letters of the alphabet for unknowns and first letters for known quantities.

**Cajori's Position:**
Regarding the Arabic derivation theory, "Cajori says there is no evidence for this."

**The Arabic 'Shei'/'Xei' Theory:**
According to Webster's Dictionary, "X was used as an abbreviation for Arabic shei a thing, something, which, in the Middle Ages, was used to designate the unknown, and was then prevailingly transcribed as xei." However, the Oxford English Dictionary refutes this, stating: "There is no evidence in support of the hypothesis that x is derived ultimately from the mediaeval transliteration xei of shei 'thing'."
```


### [2026-09-14T01:28:14.473Z] TOOL RESULT

```
# فرهنگ معین Entry for صداع

According to the Farhang-e Mo'in dictionary displayed on this page, the entry reads:

"(صُ ) \[ ع . \] (اِ. ) ۱ - دردسر. ۲ - موجب زحمت . ۳ - مزاحمت ."

This indicates three meanings: (1) trouble/hardship, (2) something causing difficulty, and (3) annoyance. The notation [ع.] signifies the word's Arabic origin.
```


## [2026-09-14T01:28:17.846Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D8%AF%DB%8C%D9%85/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for سدیم verbatim, including the origin tag (e.g. [فر.] French)."
}
```


## [2026-09-14T01:28:20.145Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D9%88%D8%AF%D8%A7/",
 "prompt": "Show the فرهنگ معین (Mo'in) entries for سودا verbatim, including all origin tags (e.g. [ع.], [فر.], [انگ.]) and the senses — in particular any sense 'soda water' / آب گازدار and any sense 'black bile / melancholy'."
}
```


### [2026-09-14T01:28:22.025Z] TOOL RESULT

```
# Farhangi Mo'in Entry for سدیم

According to the Farhangi Mo'in dictionary section provided, the entry reads:

"(سُ یُ ) [ فر. ] (اِ. ) فلزی است نقره ای ، دارای جلای فلزی ولی در مجاورت اکسیژن خیلی زود کدر می گردد و آن چنان نرم است که با چاقو به آسانی بریده می شود و از آب سبک تراست ."

The origin tag "[فر.]" indicates the term derives from **French**.
```


### [2026-09-14T01:28:25.808Z] TOOL RESULT

```
# Farhang-e Mo'in Entry for سودا

According to the Mo'in dictionary section shown:

**(سَ یا سُ) (اِ.)** "داد و ستد، خرید و فروش" [trade; buying and selling]

**(سُ) [انگ.] (اِ.)** "آب دارای گاز کربنیک" [carbonated water]

**(سَ یا سُ) [ع. سوداء] (ص.)** Four senses listed:
1. Feminine of اسود; black
2. One of the four humors, located in the spleen
3. Obsession/rumination
4. Melancholia; delusion
5. Whimsy and desire
6. Love

The entry confirms two distinct meanings: carbonated water (the modern beverage sense) and black bile/melancholia (the classical humoral medicine sense). The origin tag "[انگ.]" indicates the carbonated water sense derives from English "soda."
```


## [2026-09-14T01:28:38.425Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B4%DB%8C%D8%A1/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for شیء verbatim, with origin tag and plural forms (اشیاء / اشیا)."
}
```


## [2026-09-14T01:28:41.156Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf of line 2830\nimport re\nidx=sum(len(l)+1 for l in lines[:2829])\nleaf=t.count('\\f',0,idx)\nprint('leaf',leaf)\npages=t.split('\\f')\nprint(pages[leaf][:2500])\nEOF",
 "description": "Read TAD leaf containing هالة"
}
```


### [2026-09-14T01:28:43.002Z] TOOL RESULT

```
# فرهنگ معین Entry for شیء

**Origin:** Arabic (ع.)

**Entry:** "(شَ یا ش ) [ ع . ] (اِ. ) ۱ - آن چه که بتوان از آن اعلام و اخبار کرد، چیز. ج . اشیاء. ۲ - مجهول (ریاضی )."

**Translation of key elements:**
- Primary meaning: "That which can be reported or announced; a thing"
- Plural form: اشیاء (ashya')
- Secondary meaning: "Unknown (in mathematics)"

The entry indicates this is an Arabic loanword denoting both a concrete entity and an abstract mathematical concept.
```


### [2026-09-14T01:28:44.033Z] TOOL RESULT

```
leaf 78
                                          ‫‪6» 8 5‬‬

                   ‫سكمس‬
                      ‫ونالى وهاه وهو الطنياوة والدارة حولالقمر واك‬                   ‫هالة ‪-‬‬


‫وعتكر دقاكنة‬          ‫ان‬       ‫صعغير من‬   ‫حرن‬    ‫وهو‬       ‫فارسي « هاون (‬       ‫هاون ‪-‬‬


                                                                             ‫الذرور دما نما‬
‫معنأه حزن القمح اليد والحنطة مرادفه‬                ‫اهراء عاي لاتيني لم‪610‬‬

                                                                                 ‫بايلتمؤونة‬
                                     ‫معناه بدعة وشيعة‬             ‫بوناني ‪5‬‬       ‫هرطفة‬

‫من هلل‬     ‫ازب وهو منحوث‬             ‫هلاو ‪ -‬عيرانى ‪ 2‬هاداونه ) معناه سحوأ‬


                                             ‫أي سبح وبه مقطوع ممنهوه أي ارب‬
‫هميان فى الفارسية « هميان ‪ 4‬معناهكيس الدراهم وَكان الئاس قدي‬
                                                                                                 ‫|‬
                                                                               ‫‪.‬يتمنطقون به‬
‫‪5‬‬          ‫‪.‬‬               ‫‪.‬‬                                 ‫عر‬          ‫‪2‬‬       ‫‪١‬‬         ‫‪.0‬‬    ‫!‏‬
‫حدق التركية «هماون» معناة سعيك وسلطاي عاد وق الفارسية‬                            ‫ا هاون‬
               ‫‪5‬‬      ‫‪2‬‬                    ‫‪0-7‬‬         ‫‪.‬‬    ‫‪5-5‬‬      ‫‪.‬‬   ‫‪5‬‬             ‫‪5‬‬         ‫‪1‬‬
     ‫يىز‬
       ‫زععن‬
          ‫عني‬
            ‫عأنيقاء أطوائر 'خر وون اداة النسبة ويا‬                       ‫ل‬                      ‫هو‬

                                                             ‫|جليوللا ينمتبهالالملك‬
                                                                                  ‫و‬
                                     ‫أ هندياء ‏ فى الايطالية ‪2111‬ه‪ 1‬وهي الللعاعة‬
‫فارسي (اندازه ) معناه ذراع ععنى مقيأسس ومنههندسأي قدر وقاس‬                     ‫إهنداز ‪-‬‬
                                                                                                 ‫‪/‬‬
                                                                                                  ‫‏‪١‬‬

                           ‫هندام ‪ 5-3‬فارسي ‪ 2,‬اندام ‪ 10‬معئاه قامة وقل ومئهة هندم‬


    ‫‪-‬بفرىانية ‪. 2‬هيكدل و»نى الاصل الاشوري ‪ 31‬كلو م»عناه‬
                                                      ‫اهيكاىلع‬
                                                                                                  ‫‪4‬‬
‫وانه فى اليونانية معناه‬
```


## [2026-09-14T01:28:56.003Z] TOOL CALL #48: Bash

```json
{
 "command": "python3 -c \"\nimport json; d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['TAD'],ensure_ascii=False,indent=1))\"",
 "description": "Check TAD ref metadata"
}
```


### [2026-09-14T01:28:57.056Z] TOOL RESULT

```
{
 "title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640",
 "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"
 ],
 "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair. Nourai's exact edition unknown; the Beirut reprint reproduces the 1932 pagination."
}
```


## [2026-09-14T01:29:04.970Z] TOOL CALL #49: Bash

```json
{
 "command": "python3 tools/ref_page.py TAD:75 --image 2>&1 | head -40",
 "description": "Render TAD page 75"
}
```


### [2026-09-14T01:29:06.054Z] TOOL RESULT

```
no scan of TAD covers printed page 75 (see 'scans' in refs_online.json)
```


## [2026-09-14T01:29:08.707Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"هالة\" TAD.txt | head; echo \"---context---\"; grep -n -A2 -B2 \"هالة\" TAD.txt | head -30",
 "description": "Grep TAD.txt for هالة with context"
}
```


### [2026-09-14T01:29:08.778Z] TOOL RESULT

```
2993:هالة - ونالى وهاه وهو الطنياوة والدارة حول القمر واكك سمس 
---context---
2991-6» 8 5 
2992-
2993:هالة - ونالى وهاه وهو الطنياوة والدارة حول القمر واكك سمس 
2994-
2995-هاون - فارسي « هاون ( وهو حرن صعغير من ان وعتكر دقاكنة
```


## [2026-09-14T01:29:21.925Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 leaves ===\"; python3 - <<'EOF'\np='incoming/WLD/WLD_Bd2_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nimport re\n# find leaf with 'sauel' or 'sāuel'\nfor i,pg in enumerate(pages):\n    if 'āuel' in pg or 'sauel' in pg or 'sā́uel' in pg:\n        print('HIT leaf',i, pg[:200].replace('\\n',' '))\nEOF",
 "description": "Search Walde-Pokorny Bd2"
}
```


### [2026-09-14T01:29:23.072Z] TOOL RESULT

```
=== WLD Bd2 leaves ===
leaves 725
HIT leaf 450                                                          ^     446                                sauel, suu41-,    siiel-, sul-,   suen-, sun-    Hurde zusammengepfercht^ vgl. zur Bed. frequens fmcio
HIT leaf 529                                    suenq-, sunq-   — suento-, sunto                              525  die Gdbed.           und senn- „ein Instrument spielen“ nach der Weise von dt. „Zitherschlagen'‘ z
HIT leaf 535               ;     2. suel- „schwellen“.    JTur im germ, sicher; ahd. as. ags. swellan^ aisl. svella „schwellen‘^; kaus. ahd. hiswellen „aiischwellen macheii“, got. ufswalleins ^Aufgeblasenheit, Hoc
HIT leaf 536 532                                            (suel-), suol-, sul-    „Danipf, Eauch‘*', mhd. sivelk „welk, diirr", ahd. siveUhen^ mhd. sivelhen „welk werden'^                —                   Ein
```


## [2026-09-14T01:29:26.769Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np='incoming/WLD/WLD_Bd2_pages.txt'\npages=open(p,encoding='utf-8',errors='replace').read().split('\\f')\nprint(pages[450][:2200])\nprint(\"=========== 535 (p531 suel-) ===========\")\nprint(pages[535][:2500])\nEOF",
 "description": "Read WLD pages"
}
```


### [2026-09-14T01:29:27.977Z] TOOL RESULT

```
                                                         ^




446                                sauel, suu41-,    siiel-, sul-,   suen-, sun-



Hurde zusammengepfercht^ vgl. zur Bed. frequens fmcio; nicht uber-                 :



zeugend dagegen Ehrlich TJnters. 75: sae-pe, wie nem-pe^ mit *sai „irgend-
wann*‘ als Vorstufe von sf „wenn“); gr. alpiaoid „Gestrupp znr Anlage einer
Umzaunung(Hoin.), Steinmauer als Einfriedigung (Herod.)“, aip,6g „Dickicht“
Aesch.), Gbf.               "^saip-mos (Froehde BB. 17, 318, Wackernagel
Verm. Beitr. 39).
  Abweichende Auffassungen verzeichnet Yf. LEWb.^ 669. Unsicher wird
die Gleichung dadurch, da6 die roman. Sprachen nicht ae^ sondem e vor-
aussetzen; ist dieser Einwand geniigend tragfahig, so konnte lat. sepi als
dehnstufiger St. (wie sMes) nach Fay Am. J. Phil. 31, 422 zu onXiag* AoxqoI
rovg TOTiovg IvoTg ovveXavvovxeg dqi'dpovai to. nQO^axa xal rd pooxYipaxa
Hes. gehoren.
  Nicht iiberzeugend ist Zerlegung von alpaoid in alp-aoid, dessen 2. Glied
zu ai. atasd- n. „Gestrupp, Gebiisch^ gehore (Uhlenbeck Ai. Wb. 5) oder
zu lat. scntis (doch s. u. qs-en-^ qes-) nach Schrader KZ. 30, 462 f. (beides
verbindet Siitterlin IF. 4, 104 unter idg. [s^net-, [s]nt--; verfehlt trotz Char-
pentier BB. 30, 157, gegen den auch Persson Beitr. 356 f.).


sauel-, suuel-, suel-, sul- „Sonne“,                   woneben snen-, sun-, so da6 sich sau-,
       sH- als Wz., -el und -en als Stammbildungssuffixe ergeben. suel „schwelen,
       brennen‘‘      ist   wohl damit wesenseins,
     Gr. horn.      fjsXtog^     att.   fjXiog,   dor. deXiog^       aXiog^   kret. d^iXiog   Hes.   (d.   i.


dpeXiog) „Sonne“, Weiterbildung des n.            zum m. -m-St. (vgl. ai. sur-
ya-h)\ lat. so/, -is m. „Sonne“ (aus neutr. ^^aw^^xiber ^sauol^ *5aoZ; Mahlow
AEO. 32, Schulze KZ. 27, 428, Solmsen Stud. 68, KZfsS, 454; 44, 207
Anm. 1 trotz Kretschmer KZ. 31, 351, 452 m. Lit., Sommer Krit. Erl. 15f.;
             ;


ob die TJmwandlung zum Masc. nach Ehrlich Z. idg, Sprachgesch. 7 1 Anm. 1
durch den gr. Gotternamen ^HXiog bewirkt sei, ist allerdings mit Sommer
zu bezweifeln);             cymr. hatd^   acorn, hetml^ mcorn. heid, Jtoul^ bret. heol
.,Sonne“ {
=========== 535 (p531 suel-) ===========
              ;




2. suel- „schwellen“.
   JTur im germ, sicher; ahd. as. ags. swellan^ aisl. svella „schwellen‘^; kaus.
ahd. hiswellen „aiischwellen macheii“, got. ufswalleins ^Aufgeblasenheit,
Hochmut‘‘, ahd. sivilo m., svil n. {"^siviliz-) „Schwiele“; ags. swile^ mnd.
sicul „Geschwulst“, aisl. suUr ds. mhd. sivulst ds, ; ahd. widersivalm ,jStrudel“,
                                                   ;



nhd. Schwall,
      Aber lat. insolesco^ -ere „zunehmen, unmassig, ixbermiitig werden% inso-
lens „uninaBig,     ubermutig“ (Pokrowsky KZ. 35, 230) gehort zu salio^ vgl.
das glossematische adsolentes                     = adsilientes und zur Bed. auch in^ultcire:
sallare (Dohriag Gl. 2, 255 f.).  Piir abg. chvaliti „loben“ denkt Berneker
406 f. selber nur mit starkem Zweifel an ein ^snoleio „mache schwellen“
als Grundlage; iiber gr, dhg .,genug“ s. u. uel- „drangen“: die Yerwandt-
schaft von ir. suit „Fett, Pr6hlichkeit“ (Pick         551) ist nicht glaubhaft.
Zur Verknupfung von suel- mit lat. solum u. dgl. s. u. solo- „wogend“, Bei
der Isoliertheit der germ. Sippe ist es auch fraglich^ ob sie rnit der Gruppe
von aisl. vella „sprudein, sieden, wallen'* (s. u. uel ,jdrehen‘‘) als 5-Yariante
vereinigt werden darf, zumal in letzterer das Wallen des Wassers bes. beim
Sieden der Bed.-Kern ist.

3. snel- „schwelen, brennen“.
      Ai. svarati „leuchtet, 8cheint“ (vielleicht aber das s el be wie svdrati j^tont,
schallt‘‘         und dann auszuscheiden               ;
                                                           ai.    svdrnara-, av. xvarmcih-      wegen des
ai.    Svarita zu silvar^                 svdr „3onne'',     s.    "^sauel-^    also   auf den Sonnenglanz
gehend)
      gi\ eil?],    elXrj^   eXrj    „Sonnenwarme, Sonnenlicht“, y€?Mv' avyi]v 7]/Jov, peXa'
ijXiog yML avyi], vjio              Aaxcovojv, eXa^ ijXiog^ ^Q7^]          ’   y^ovjua Hes., iXdvrj jjFackeP,
eXivTj'     Xa^ndg'          dart]    Hes., ^EXavri ursprgl. eine Lichtgottin: dXaa „Sonnen-
warme“,            dXeaiveo „er\Yarme‘^           aXad^oj „bin warm‘d dXaetvog „hei6“, dXvxoog
(Nikand.)          „warm“           (s.   zur gr. Sippe Solmsen Unters. 196, 248 ff.,               Sommer
Gr. Ltst. 111).
   Zugehorigkeit von oeXag n. „Glanz“, oeXrjvr], aol. oeXdvva „Mond“ {^oaXao-
ra), oeXayeTv „glanzen“, ist wegen des bevrahrten a- nicht unzweifelhaft;
Kechtfertigungsversuche bei Kretschmer KZ. 31, 422, Prellwitz^ s. v. (^[a]d-
suol-)^ Solmsen Unters. 209 Anm. 2 (*ksyxl-)'
```


## [2026-09-14T01:29:41.582Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC sawel ===\"; grep -n \"sāwel\\|sawel-\\|sāwl\\|sāuel\" IEC.txt | head -8; echo \"=== IEC swel ===\"; grep -n \"swel-\\|swelō\\|swelō \" IEC.txt | head -8; echo \"=== SYN sun ===\"; grep -n \"1.52 SUN\\|SUN$\\|hēlios\" SYN.txt | head -8",
 "description": "Grep Mann and Buck"
}
```


### [2026-09-14T01:29:42.706Z] TOOL RESULT

```
=== IEC sawel ===
=== IEC swel ===
987:bronkà, om, is ‘swelling’. Cf. bhronk- Alb. brángé&, bréngé (1) ‘swelling, tumour’; Sw. cf. práng (1) ‘swagger’; Li. brankà 'swel- ling’. (The Alb. & Li. forms are ambiguous)
4480:gumbulos, gambəlos (gumbh-, gum-) ‘swel- ling’. WP I, 573. See gumb- and next. Oss. gumbul ‘ball of cheese’; Alb. gúmull ‘mass, pile’; OE cumbl, cumul ‘swelling’: ON
=== SYN sun ===
1661:1.52 SUN
```


## [2026-09-14T01:29:44.132Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%99%CE%BB%CE%AD%CE%BD%CE%B7",
 "prompt": "Ancient Greek Ἑλένη: etymology — is it connected with ἑλένη 'torch' / σέλας 'light' / PIE *swel- 'to burn', or with *wel-? Quote what is said."
}
```


### [2026-09-14T01:29:49.039Z] TOOL RESULT

```
# Etymology of Ἑλένη

According to the Wiktionary entry, the name's etymology involves a solar deity connection rather than a torch/light connection:

The word is "most likely from Proto-Hellenic *Ηwelénā, from a pre-Hellenic or late Proto-Indo-European *Swelénā (a solar deity), ultimately from Proto-Indo-European *swel- ('to shine, warm, smoulder, burn')."

Importantly, the source explicitly states the name is "**unrelated to** ἑλένη (helénē), σέλας (sélas) or σελήνη (selḗnē)" — those being the torch, light, and moon-related terms. 

So while Ἑλένη shares the PIE root *swel-, it derives from an older solar deity name (*Swelénā) and is etymologically distinct from the common Greek words for torch and light, despite superficial similarity.
```


## [2026-09-14T01:30:12.017Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1661,1700p' SYN.txt",
 "description": "Read Buck 1.52 SUN"
}
```


### [2026-09-14T01:30:12.074Z] TOOL RESULT

```
1.52 SUN
Lo” i ial. aféAtos, Goth. sauzl, sunnéd Lith.  saulé So oe : ON _ sdl, sunna Lett. saule NG — #Xos Dan. sol Ch&Sl. _ sliintce Lat. sol Sw. sol SCr.  sunce It. sole OE sunne, sunna Boh. — slunce Fr. soleil ME sonne Pol. slovice Sp. sol NE sun Russ. solnce Rum. soare Du. zon Skt. suar (Ved.), strya-, Ir. grian OHG = sunna ravi-, etc. NIr. = grian MHG sunne Av. hvara, gen. hird and W. haul NHG __sonne x’éng Br. heol
Nearly all the usual words for ‘sun’ belong to a single inherited group.
1. IB *sawel-, etc., a group with vow- el gradation, parallel /- and n- forms (the Slavic fr. *sulno- with added dim. suffix), and variation in gender. Walde-P. 2.446. Ernout-M. 950f. Falk-Torp 1105. Feist 412, 460. Here belong all the words listed except the following.
2. Ir. grian, NIr. grian, fr. *greina, prob. formed fr. the weak grade of IE *g’her- seen in words for ‘hot, heat’, as Nir. gor, NE warm, Grk. Oepyds, Skt. gharma-, etc. This connection is ques-
tioned by Pedersen, KZ 38.197 (Walde- P. 1.688). But cf. esp. Skt. ghrna- ‘heat? and ‘sunshine’, and (fr. Skt. gharma-) Hind. ghém ‘sunshine’, Gypsy gam, k‘am ‘sun’ (Sampson, Dial. of Gypsies of Wales, 166).
3. Skt. ravi-, perh. the commonest class. word for ‘sun’, Arm. arev ‘sun’.: Skt. aruna-, arusa- ‘reddish’ (both often applied to the sun), Av. aurusa- ‘white’. Walde-P. 2.359. Uhlenbeck 246.
Among other Skt. words for ‘sun’ are : bhana- fr. bha- ‘shine’, bhas-kara-, lit. ‘light-making’, dina-kara- lit. ‘day-mak- ing’, arka- fr. arc- ‘shine’.
1.53 MOON Grk.  cedjvn Goth. ména Lith. ménuo, ménulis NG  devyapt (cedrv7 lit.) ON mani (poet.), tungl Lett. ménesis Lat. lina Dan. maane ChSl. luna, mésgct It. luna Sw. mane SCr.  mjesic Fr. lune OE mona Boh. _mésic Sp. -luna ME mone Pol.  ksigzyc Rum. lund NE moon Russ. luna Ir. ésce (luan) Du. maan Skt. (mGs-), candra-, ¢a- Nir. gealach, ré (éascd) OHG wmédno ¢cin-, etc. W. Ueuad, lloer MHG mane Av. mah- Br. loar NHG mond
1. IE *ménes-, *mén(n)s- ‘moon’ and | ‘moon’, ménesis ‘month’), Lett. ménesis,
‘month’, presumably fr. *mé- ‘measure’. Walde-P. 2.271f. Ernout-M. 607 f. Walde-H. 2.71. Berneker 2.51.
Here belong: (1) with the same form in both senses, Lith. ménuo, etc. (but here also with differentiation ménulis
ChSl. mésect (but mostly ‘month’; luna more common for ‘moon’), SCr. mjesic, Boh. mésic, Skt. mas- (as in Rigveda, later mostly ‘month’, rarely ‘moon’), Av. mah- (OPers. mah- ‘month’), NPers. mah-, Toch. A maf, or for ‘moon’ maf
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
THE PHYSICAL WORLD IN ITS LARGER ASPECTS 55
+ (nat ‘god, goddess’ used as a de- eS ay (2) with differentiation, all the Gme. forms, as Goth. ména ‘moon’, ménops ‘month’, NE ade month, etc.; Toch B mem ‘moon eae ‘month’ (so Benveniste, Festschrift Hirt. 2,234, but S. Levi, Fragments Koutsch. 1.121 gives ‘lune’ for both forms).
Elsewhere, namely in Greek, Italic, Celtic, Albanian, Armenian, and in some of the Slavic languages, the words of this group have persisted only in the sense of ‘month’ (Grk. piv, Lat. ménsis, Ir. mi, etc.; 14.61) and have been displaced in the sense of ‘moon’ by other words, most of them from the notion of ‘brightness’ as follows.
2. Grk. cedqvn, Dor. ceddéva, Lesb. cedavva : oédas ‘light, brightness’ (of fire or the heavenly bodies). Walde-P. 2.531. Boisacq 858.
NG g¢eyyap:, dim. of Grk. déyyos ‘light, splendor’ (of daylight or moon- light).
3. Lat. lina, fr. *leuksna- (cf. Praen. losna) : Lat. lia, lamen ‘light’, Grk. Aeuxds ‘bright’, Av. raoxsna- ‘light’, OPruss. lauxnos ‘stars’, ete. Here also as ‘moon’, Ch§l., Russ. luna, Arm. lusin, Ir. wan, (poet.; Thurneysen, Z. deutsch, Wortf. 1.189) and, fr. a parallel form of
the root, W. lleuad, lloer, Br. loar? Walde-P. 2.408 ff. Ernout-M. 570 ff.
From Lat. lina come It., Sp. luna, Fr. lune, and Rum. lund, the last both ‘moon’ and ‘month’, because of the double sense of Slavic més¢ci. —
4, Ir. ésce, NIr. éasca : Osc. eiduis, Lat. idus ‘ides’? Walde-P. 1.103.
NIv. gealach ‘moon’ also ‘light, bright- ness’, fr. geal ‘bright, white’ (15.57).
Ir. ré ‘period of time’, NIr. also esp. ‘moon’ Av. ravah- ‘space, room’, etc.(?). Wendryes, RC 28.141.
5. ON tungl, replacing manz in prose, beside himun-tungl ‘heavenly body’ : Goth. tuggl, OE tungol ‘heavenly body’, root connection? Walde-P. 1.792. Feist 481 f.
6. Pol. ksiezyc, displacing miesiac in the sense of ‘moon’, dim. of ksiqdz in its older meaning ‘prince’ (19.35). As the sun was the lord of the day, the moon of the night, the latter was the lesser ‘prince’. Briickner 277.
7. Skt. candra-, also (combined with mdas-) candramas- : (¢)candra- ‘bright’, (¢)cand- ‘shine’, Lat. candére ‘shine’, Alb. haéné ‘moon’, etc. Walde-P. 1.352.
Skt. cacin-, fr. gaga- ‘hare’, after the supposed resemblance of the markings on the moon.
1.54 STAR
a dorip, Razor Goth. stairné Lith.  Zvaigidé Lat. stella, aie ON _ sijarna Lett.  zvaigzne
It. stella’ Paes Dan. _ sijerne ChSl. © zvézda
Fr. toile Sw. —stjdirna SCr.  zvijesda
Sp. estrella OE sleorra Boh. hvézda
Rum.  stea ME sterre Pol. gwiazda
Ir, retglu, rind NE star Russ. zvezda
Nir, realt : Du. ster Skt. star-, ta: @-
W. en OHG - sterro, sterno Ay. star-
Br. steredenn vee slérne
```


## [2026-09-14T01:30:13.100Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://www.behindthename.com/name/aileen",
 "prompt": "What is the origin of the name Aileen? Is it from Helen or from Aveline/Eibhlín? Quote."
}
```


### [2026-09-14T01:30:17.149Z] TOOL RESULT

```
# Origin of the Name Aileen

Based on the webpage provided, Aileen's origin is traced back to Irish and Scottish Gaelic roots rather than directly to Helen.

The page states: **"Variant of Eileen."**

The related names section shows that Aileen connects to **Èibhlín** (Scottish Gaelic) and **Eibhlín** (Irish), indicating its primary lineage comes from Gaelic traditions. While the broader name family does include Evelina/Eveline variants across many European languages, the direct origin for Aileen specifically is established as a variant of the Irish/Scottish name Eileen rather than a direct derivation from Helen or Aveline.
```


## [2026-09-14T01:30:29.403Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT هاله ===\"; grep -c \"هاله\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null; echo \"=== BQT خرمن ماه ===\"; grep -n \"هاله\" incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | head -10; echo \"=== HRN halo/hale ===\"; grep -n -i \"hâle\\|hāla\\|halo\" HRN.txt | head -5; echo \"=== HUB ===\"; grep -n -i \"hāla\\|halo\" HUB.txt | head -5",
 "description": "Grep BQT, Horn, Hübschmann"
}
```


### [2026-09-14T01:30:29.529Z] TOOL RESULT

```
=== BQT هاله ===
incoming/BQT/BQT_v5_pages.txt:0
BQT_v1_pages.txt:2
incoming/BQT/BQT_v4_pages.txt:20
incoming/BQT/BQT_v3_pages.txt:6
BQT_v2_pages.txt:7
=== BQT خرمن ماه ===
incoming/BQT/BQT_v4_pages.txt:1547:است و بعریی لیل خوانند . درهاله باشد چه عاله را تیزخر گاه کوبند۴ (۱)
incoming/BQT/BQT_v4_pages.txt:2333:هاله- بنم اول و سکون ثانی » بمعنی | که مطبوط زن خود است بمنی مرد ی که مطیح
incoming/BQT/BQT_v4_pages.txt:11476:نوشین ۱ - بر وزن ژوبین » بمعنی | چمن است که نهالها و شاخهای نودمیدء و کلها
incoming/BQT/BQT_v4_pages.txt:11847:کردن وبیم بردن باشد . نهاله+ «بکس اول بروزن پیاله.درخت
incoming/BQT/BQT_v4_pages.txt:11854:میگوشرن ۹ نهاله‌گاه ۷۱ بکر اور 0
incoming/BQT/BQT_v4_pages.txt:11856:باشد - و کمین گاه صیاد را نیز کوبند. شکارگاه - و کمین گاه باشد » چه لهاله بمعنی
incoming/BQT/BQT_v4_pages.txt:11864:۴ - اسم مفعول از ۸ نهازیدن > . ۴ <نهاله ( «.م. )کردی 2081 (کیاه ۰
incoming/BQT/BQT_v4_pages.txt:11873:کاء ( پوند مکان ) * نپالگه ۳ نهاله کاه (هم). ۷ < نپانگاه < نهاله گاء (ه.م.)
incoming/BQT/BQT_v4_pages.txt:11876:عشق تو بر جان من نپاد تهاله ‏
incoming/BQT/BQT_v4_pages.txt:11878:*- باین معنی اصل « نهالهگاء » (ه.م.) است . ۱ از : هاله (ه.م.) + کاه
=== HRN halo/hale ===
=== HUB ===
```


## [2026-09-14T01:30:37.299Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2320,2345p' incoming/BQT/BQT_v4_pages.txt; echo \"--- page tag ---\"; awk 'NR<=2333 && /\\[pdf page/ {p=$0} END{}' incoming/BQT/BQT_v4_pages.txt; grep -n \"\\[pdf page\" incoming/BQT/BQT_v4_pages.txt | awk -F: '$1<2333' | tail -2",
 "description": "BQT v4 هاله context"
}
```


### [2026-09-14T01:30:38.700Z] TOOL RESULT

```
و قی : دی ده ( ر4 : لفت فری ص ۲۲۲ : دیش * پدهش ) -

۷ - شهرست برساحل بحر قلزم . محاذی تبوکه در حدود شش مرحله مافت ازآن,
وآن بز رک ازتبوك است وبدانجا چاهی است که موسی* چرند گان شعیب را آب داد ... قاضی
ابوعبداله قناعی گوید: مدین از خرء مصر قبلی است و حازمی کوید بین وادی القری و شام است
و گفته اند مدین روباروی تبوك است بین مدینه وشام بشش مرحله . . وگفته اند مدین همان
« کفرمندة > از اعمال طبربه است و چاه و سنگه بدالجاست. « ممجم‌البلدان >.
[pdf page 61]
مدیتا -۱۹۷۸-
هد‌یتا ۱ - بر وزن امینا : بلفت زند | وپازند(۱) بمعنی شهر است وبعربی‌مدینه گویند.
بیان دهم
درمیم با ذال نقطه دار مشتمل بر چهار لت
۰ ۰
هاله- بنم اول و سکون ثانی » بمعنی | که مطبوط زن خود است بمنی مرد ی که مطیح
ساحب و خداوند باشد و مرکب می آید همچو | و فرمان بردار زن خود باشد .
اسفتدارمذ ۴ (۲). هذانگ ۴ - بر وزن ومثی مدنکه
مذاپ ۴ - بنم اول بر وزن کلاب . است که کلید چوبین - و دندانةٌ کلید - و پر
بمعنی گداخته باعد ؛ و ختح اول هم آمده ] قفل و چوب کنده باشد (۳) که دریس دراندازند
است . تا در کشوده نگردد .
مِذ کرسماعی «کنایه از وهرست
بیان یازدهم
در میم با رای بی‌نقطه مشتمل بریکصد و سی و هفت لغت و کنایت
هر - بفتح اول و سکون ثانی , حاب | چیزی میدارد. چون همه شمرده شودآن‌چیزیرا
را گویند 6 - و هن عقدی باشد از اعداد ملد | که بازای هن صدی داشته است مر گوبند اگر
شخصی ده هزار میشمارن و در هر صدی يك عدو | ده‌شده باشد ده هروا کریشترشده باشدییشتر۹ -
() چك: ژند وپاژند . () چش : مز. () خم۱: - باشد.
--- page tag ---
2282:[pdf page 60]
2327:[pdf page 61]
```


## [2026-09-14T01:30:46.651Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"خرمن ماه\\|خرمن‌ماه\" incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt BQT_v2_pages.txt 2>/dev/null | head -10",
 "description": "Grep BQT for خرمن ماه"
}
```


### [2026-09-14T01:30:46.714Z] TOOL RESULT

```
BQT_v2_pages.txt:11366:‫اول را‬       ‫و آسمان‬     ‫است که خرمن ماه باشفد —‬
BQT_v2_pages.txt:11452:                                  ‫که هاله و خرمن ماه باشد ‪.‬‬
BQT_v2_pages.txt:31394:                                                      ‫هاله وخرمن ماه باشد ا‪-‬وریسمانیرا نیز گوبند‬
```


## [2026-09-14T01:30:49.936Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11360,11370p' BQT_v2_pages.txt; echo \"---\"; sed -n '11448,11456p' BQT_v2_pages.txt; echo \"--- pdf page tags ---\"; grep -n \"\\[pdf page\" BQT_v2_pages.txt | awk -F: '$1<11460' | tail -2",
 "description": "BQT v2 هاله/خرمن ماه context"
}
```


### [2026-09-14T01:30:51.046Z] TOOL RESULT

```
                                                                ‫ییراز ‪ -‬و تخته‌ای ناشد که‬
                                                                                        ‫ش‬                  ‫خر‬
                                                                                                            ‫س ف‬
                                                                                                              ‫هشت‬
                                                               ‫وناه کاران را برآن خوابانند و درهٌ‬
                                                                                                ‫مجرمان گ‬
‫اول را‬       ‫و آسمان‬     ‫است که خرمن ماه باشفد —‬
                                                               ‫و چوییرا نز گویند که استادان‬          ‫تادیب زتند ‪-‬‬
‫نکیوزیند ‪ -‬وکنابه از خط عذار مهوشان هم‬                         ‫هیمه در زر آن‬         ‫‪CA‬‏‬       ‫کنده شکن در وت‬
                                                    ‫‪۰‬‬     ‫هت‬
                                                               ‫کذار دوش کنند ‪ -‬وسه چوبه‌ای باشد که بربای‬
---
                                                                                               ‫کر‬
                                                                                                ‫گفته اند ( ‪) ۲‬‬
    ‫خر گه مه ه مخفف خرگاه ماه است‬
                                                                                              ‫لان الحمل است ‪.‬‬
                                  ‫که هاله و خرمن ماه باشد ‪.‬‬
                                                                                                   ‫وبارتنگه تخمی‬
    ‫بضم اول و فتح ثانی با قشدید ‪.‬‬              ‫حر"‬                                            ‫دوابی ‪٩‬‏ »وبایتمعنی‬
     ‫بمعنی شادمان وخوشوقت باشد ‪*٩-‬‏ ونام مامدی‬                                               ‫بساین بى نفطه هم‬
             ‫و‪.‬‬    ‫‪- :‬‬       ‫(‪ )۳‬چك‪ ,‬چش‬                ‫(‪ )۲‬چك‪ .‬چش ‪:‬گونن‪.‬‬              ‫(‪ )۱‬چش ‪ :‬آنرا ‪.‬‬
--- pdf page tags ---
```


## [2026-09-14T01:31:01.333Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D9%8A%D8%A1",
 "prompt": "Arabic شيء (šayʔ): etymology (root ش ي أ, relation to شاء 'to will'), meaning, plural أشياء. Also any Persian section."
}
```


## [2026-09-14T01:31:02.597Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/swelter",
 "prompt": "English 'swelter': etymology — Old English sweltan, Proto-Germanic *sweltaną, PIE *swel-. Quote."
}
```


### [2026-09-14T01:31:06.741Z] TOOL RESULT

```
# Arabic Word: شيء (šayʔ)

This Wiktionary entry documents the Arabic word **شيء** (šayʔ), pronounced /ʃajʔ/.

## Primary Meaning

The noun means **"thing"** in English. The entry includes a Quranic citation demonstrating classical usage: "God is Creator of all **things**" (Qur'an 13:16).

## Grammatical Details

- **Part of speech**: Masculine noun
- **Plural form**: أشياء (ʔašyāʔ) — a broken plural
- **Declension type**: Triptote singular, diptote plural
- **Secondary meaning**: Can mean "little" or "some" when used with the preposition من (min)

## Linguistic Relationships

The entry shows the word derives from the Semitic root ش ي ء (š y ʔ). Notably, it has generated descendants in multiple languages including Turkish (şey), Persian (شیء), and Maltese (xi).

## Etymology Note

A second entry documents شِيءَ as a passive verb form derived from شَاءَ (šāʔa, meaning "to will").
```


### [2026-09-14T01:31:07.256Z] TOOL RESULT

```
# Swelter: Definition and Etymology

**Swelter** is a verb meaning to suffer intensely from heat or perspire greatly. It can also function as a noun referring to intense heat itself.

## Etymology

The word traces back through several language stages. It derives from Middle English *swelteren*, a frequentative form of *swelten* ("to die; faint"). This ultimately comes from Old English *sweltan* meaning "to die," which originated in Proto-Germanic *sweltaną* and Proto-Indo-European *swel-* ("to smolder; burn").

## Usage Example

Samuel Taylor Coleridge employed the past participle in his 1796 poem *Fire, Famine, and Slaughter*: "To see the **swelter'd** cattle run" describing animals affected by extreme heat conditions.

The word is etymologically connected to the modern adjective "sultry," sharing the same linguistic roots related to heat and burning.
```


## [2026-09-14T01:31:15.132Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sodium",
 "prompt": "Etymology of 'sodium': Humphry Davy, coined from soda, date. Quote."
}
```


## [2026-09-14T01:31:16.192Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://www.behindthename.com/name/eileen",
 "prompt": "Origin of Eileen: Eibhlín, Aveline (Norman), and whether it is sometimes considered an Irish form of Helen. Quote exactly."
}
```


### [2026-09-14T01:31:18.914Z] TOOL RESULT

```
# Etymology of Sodium

**Coiner:** English chemist Humphry Davy

**Year:** 1807

**Origin:** The term was formed by combining "soda" with the suffix "-ium." Davy selected this name because the element was isolated from caustic soda (sodium hydroxide).

**Key Quote:** "So called because the element was isolated from caustic soda (sodium hydroxide). The chemical symbol Na is from natrium, the name for the element that had been proposed by Berzelius and coined from natron, a name of a type of soda."

The chemical symbol "Na" derives from an earlier Latin term, *natrium*, which itself came from *natron*—an earlier designation for a type of soda.
```


### [2026-09-14T01:31:19.309Z] TOOL RESULT

```
# Origin of Eileen

According to the page, Eileen is the "Anglicized form of Eibhlín." The name "is also sometimes considered an Irish form of Helen."

The page indicates that related name variants connect to Aveline through its etymology, though the direct lineage from Norman origins to Eileen is shown through the Irish Eibhlín form rather than explicitly through Aveline itself.
```


## [2026-09-14T01:31:30.494Z] TOOL CALL #65: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%E1%BC%85%CE%BB%CF%89%CF%82|page 433 entry0 node1/2: Greek halos 'threshing floor, disk, halo' Pre-Greek, not from *sawel-\" \\\n \"https://en.wiktionary.org/wiki/%D9%87%D8%A7%D9%84%D9%87|page 433 entry0 node2: Persian hale < Arabic hala < Gk halos\" \\\n \"https://www.etymonline.com/word/halo|page 433 entry0 node2: halo < Gk halos, origin unknown\" \\\n \"https://en.wiktionary.org/wiki/%E1%BC%A5%CE%BB%CE%B9%CE%BF%CF%82|page 433 entry0 node1: Gk helios < PIE *soh2wl, Doric halios\" \\\n \"https://www.etymonline.com/word/soda|page 433 entry2 node3/4: soda origin, sudaa theory far-fetched\" \\\n \"https://en.wiktionary.org/wiki/soda|page 433 entry2 node3: soda < Italian soda < Arabic suwayda (plant)\" \\\n \"https://en.wiktionary.org/wiki/%D8%B5%D8%AF%D8%A7%D8%B9|page 433 entry2 root/node1: Arabic sudaa 'headache' root s-d-3\" \\\n \"https://mathshistory.st-andrews.ac.uk/Miller/mathsym/variables/|page 433 entry1 node2/3: Cajori and OED reject the shei>xei>x story; Descartes 1637\" \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done",
 "description": "Archive web sources batch 1"
}
```


### [2026-09-14T01:31:35.803Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/82610ff6c9783a91.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2e16ab4bdbd31710.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4b52a81a1958af69.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fa632ab0fc2df34b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/df5654f4ef78f187.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/90869ab476d88c13.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ac4289f67623f736.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9cc50de617cb0665.txt
```


## [2026-09-14T01:31:45.826Z] TOOL CALL #66: Bash

```json
{
 "command": "for u in \\\n \"https://abadis.ir/fatofa/%D9%87%D8%A7%D9%84%D9%87/|page 433 entry0 node2: Mo'in entry for hale\" \\\n \"https://abadis.ir/fatofa/%D8%B5%D8%AF%D8%A7%D8%B9/|page 433 entry2 node2: Mo'in sodaa [Arabic]\" \\\n \"https://abadis.ir/fatofa/%D8%B3%D8%AF%DB%8C%D9%85/|page 433 entry2 node7: Mo'in sodyom [French]\" \\\n \"https://abadis.ir/fatofa/%D8%B3%D9%88%D8%AF%D8%A7/|page 433 entry2 node5: Mo'in soda [English] = carbonated water\" \\\n \"https://abadis.ir/fatofa/%D8%B4%DB%8C%D8%A1/|page 433 entry1 node1: Mo'in shey' [Arabic], pl. ashya\" \\\n \"https://en.wiktionary.org/wiki/%E1%BC%99%CE%BB%CE%AD%CE%BD%CE%B7|page 433 entry0 node5: Helene < *Swelena < PIE *swel-\" \\\n \"https://www.behindthename.com/name/eileen|page 433 entry0 node6: Eileen/Aileen < Eibhlin < Aveline, only sometimes equated with Helen\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D9%8A%D8%A1|page 433 entry1 root/node1: Arabic shay' 'thing', root sh-y-'\" \\\n \"https://en.wiktionary.org/wiki/swelter|page 433 entry0 node8: swelter < OE sweltan < PGmc *sweltana < PIE *swel-\" \\\n \"https://www.etymonline.com/word/sodium|page 433 entry2 node4: sodium coined by Davy 1807 from soda\" \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -1; done",
 "description": "Archive web sources batch 2"
}
```


### [2026-09-14T01:31:57.154Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8e075d65c78c3e7a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/76c39ce7669eb8e1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b9db07f550e72838.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2c4dc2fb8fd807d4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e69c9991d0c59125.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ed34ce9905ac4d76.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/32e3853d8fa82276.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/17c741176764db64.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c58f7d27903d72da.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9f823883f49a8000.txt
```


## [2026-09-14T01:33:35.807Z] TOOL CALL #67: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg433.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/433.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/433.png; echo \"--- verify_check usage ---\"; head -30 /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Copy page PNG and inspect verify_check"
}
```


### [2026-09-14T01:33:35.898Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 74286 Sep 13 21:33 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/433.png
--- verify_check usage ---
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
```


## [2026-09-14T01:33:37.456Z] AGENT

Now writing the verification file.


## [2026-09-14T01:41:11.626Z] TOOL CALL #68: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-433.json",
 "content": "{\n  \"pdf_page\": 433,\n  \"book_page\": 403,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Sâwel, Sŭ 3\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *sóh₂wl̥ / *seh₂w-el- ~ *sh₂-un- 'sun' (Pokorny 881–882 sāuel-, sāuol-, suuel-, suel-, sul-; also suen-, sun-)\",\n      \"note\": \"Pokorny prints 'Root/lemma: sāuel-, sāuol-, suuel-, suel-, sul-, Meaning: sun', Page(s) 881–882 — Nourai's headword, the language label 'Indo-European' and the gloss 'sun' are all right, and his second headword 'Sŭ 3' is Pokorny's short/zero-grade variant *su- (su-en-, sun-). Watkins (AHD appendix) has the same entry, 'sāwel-. Also s(u)wel-, su(a)el-, su(ə)en-, sun-. The sun. Contracted from *sāswel-. … [Pok. sāwel- 881.]'. Pokorny's own note 'suel- \\\"smolder, burn\\\" is probably identical with it' is the warrant for Nourai hanging Swel 2 (node 4) under this root. The weak point of the chart is not the root but the Greek box: Nourai runs the halo-word and the sun-word together (see nodes 1–2).\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *sóh₂wl̥ (صورت‌های بازسازی‌شدهٔ *sāuel-/*suuel-/*sul-/*sun-) به معنی «خورشید» است و پوکورنی آن را در صفحهٔ ۸۸۱ کتاب IEW با همین معنا آورده؛ پس سرواژه، برچسب زبانی و معنای نورایی درست است و «Sŭ ۳» همان گونهٔ کوتاه‌شدهٔ *su-/*sun- است. هم‌ریشه‌های آن در ایرانی، اوستایی huuarə / hū (صورت اضافی)، فارسی میانه xwar و فارسی نو «خور/خورشید» است که نورایی در بخش دیگر این ریشه آورده. پوکورنی خود یادآور می‌شود که ریشهٔ suel- «سوختن، دود کردن» احتمالاً با همین ریشه یکی است و همین، پیکان «ریشه ← Swel ۲» را توجیه می‌کند. کاستی نمودار در خانهٔ یونانی است، نه در ریشه: نورایی واژهٔ «هاله» و واژهٔ «خورشید» یونانی را یکی گرفته است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%E1%BC%A5%CE%BB%CE%B9%CE%BF%CF%82\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:881\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt (grep -n 'lemma: sauel'): 'Root / lemma: sauel- sauol- suuel-, suel-, sul- , (*hauhuel-) / Meaning: sun / Note: next to which suen-, sun-, thus of old n/n-stem; suel- \\\"smolder, burn\\\" is probably identical with it' … 'Page(s): 881-882'.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. II p. 446 (WLD_Bd2_pages.txt leaf 450)\",\n          \"stance\": \"supports\",\n          \"note\": \"'sāuel-, suuel-, suel-, sul- \\\"Sonne\\\", woneben suen-, sun-, so daß sich sāu-, sū- als Wz., -el und -en als Stammbildungssuffixe ergeben. suel \\\"schwelen, brennen\\\" ist wohl damit wesenseins.'\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, s.v. sāwel- (AHD_watkins1985.txt line 905)\",\n          \"stance\": \"supports\",\n          \"note\": \"'sāwel-. Also s(u)wel-, su(a)el-, su(ə)en-, sun-. The sun. Contracted from *sāswel- … [Pok. sāwel- 881.]'\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck 1.52 SUN (SYN.txt line 1661)\",\n          \"stance\": \"supports\",\n          \"note\": \"'Nearly all the usual words for \\\"sun\\\" belong to a single inherited group. 1. IE *sāwel-, etc., a group with vowel gradation, parallel l- and n- forms … Walde-P. 2.446.' Greek ἠέλιος/ἥλιος and Av. hvarə are listed in the same group.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Greek\",\n          \"words\": \"alos, helios\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The second word is right: Attic ἥλιος (hḗlios), Homeric ἠέλιος, Doric ἀέλιος / ᾱ̔́λιος 'sun' < Proto-Hellenic *hāwélios < PIE *sāwel-yo- (Watkins: 'Suffixed form *sāwel-yo- in Greek hēlios, sun: HELIACAL, HELIO-, HELIOS, HELIUM'); the initial s- of the root became h- by the regular Greek change *s- > h-, and intervocalic *-w- was lost in Attic-Ionic. The first word 'alos' is not a Greek word in this shape. Pokorny 881 lists the Doric forms as ἀέλιος and ἅλιος (hālios), so 'alos' could be a mangling of hālios; but the node feeds Persian hāleh 'halo' (node 2), which comes from a completely different word, ἅλως (hálōs) 'threshing floor; disk of the sun or the moon; halo' — a noun Klein calls 'of uncertain origin' and Wiktionary (after Beekes) assigns to the Pre-Greek substrate, i.e. NOT a derivative of *sāwel-. The printed page (pdf p. 433) itself reads 'alos, helios : sun', so the extraction is faithful: the defective form and the 'sun' gloss on the halo-word are Nourai's own. Verdict therefore applies to the first word only; 'helios : sun' is confirmed.\",\n          \"derivation_fa\": \"واژهٔ دوم درست است: ἥλιος آتیکی (هومری ἠέλιος، دوری ἀέλιος/ᾱ̔́λιος) «خورشید» از یونانی آغازین *hāwélios و آن از هندواروپایی *sāwel-yo-؛ س آغازین هندواروپایی در یونانی قاعده‌مند به ه بدل شده و -w- میان‌واکه‌ای در گویش آتیکی-یونیایی افتاده است. اما صورت «alos» به این شکل واژهٔ یونانی نیست؛ پوکورنی گونهٔ دوری را ἅλιος (hālios) می‌آورد، ولی واژه‌ای که «هالهٔ» فارسی از آن آمده ἅλως (hálōs) «خرمنگاه؛ قرص و دایرهٔ گرد ماه و خورشید» است که کلاین آن را «با خاستگاه نامعلوم» و ویکی‌واژه (به پیروی بیکس) پیش‌یونانی می‌داند و هیچ پیوندی با ریشهٔ *sāwel- ندارد. تصویر صفحهٔ چاپی (ص ۴۰۳ کتاب) همین «alos» را نشان می‌دهد؛ پس خطای خوانش اسکن نیست، خطای خودِ کتاب است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"alos, helios : sun\",\n          \"correct_form\": \"hálōs (ἅλως) 'disk/halo' — a separate, non-Indo-European word — beside hélios (ἥλιος) 'sun'; the Doric sun-word is hālios (ᾱ̔́λιος)\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E1%BC%A5%CE%BB%CE%B9%CE%BF%CF%82\",\n            \"https://en.wiktionary.org/wiki/%E1%BC%85%CE%BB%CF%89%CF%82\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"partial\",\n              \"note\": \"Watkins 1985 s.v. sāwel- §3: 'Suffixed form *sāwel-yo- in Greek hēlios, sun: HELIACAL, HELIO-, HELIOS, HELIUM' — supports 'helios' but says nothing about any 'alos', and gives no halo-word under this root.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 881 (POK_full.txt, s.v. sauel-)\",\n              \"stance\": \"partial\",\n              \"note\": \"'gr. hom. ἠέλιος, Attic ἥλιος, Doric ἀέλιος, ἅλιος, Cretan ἀβέλιος Hes. \\\"sun\\\"' — the Doric form is hālios, not 'alos'; ἅλως does not appear in the entry.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II p. 446 (leaf 450)\",\n              \"stance\": \"partial\",\n              \"note\": \"'Gr. hom. ἠέλιος, att. ἥλιος, dor. ἀέλιος, ἅλιος, kret. ἀβέλιος Hes. \\\"Sonne\\\", Weiterbildung des n. zum m. -io-St.' — same list, again no ἅλως.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"1971 ed. s.v. halo (KLN_1971.txt line 108954)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'halo, n. … F., fr. L. halo, acc. of halos, fr. Gk. ἅλως, \\\"threshing floor; disk of the sun or of the moon\\\", which is of uncertain origin.' Klein keeps the halo-word apart from ἥλιος.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"hâleh\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Persian هاله hāle 'halo, ring round the moon' is real and old in the literary language (Nourai's Sāʾeb line 'مه در حصار هاله نخواهد مدام ماند' is genuine usage), but it does not come from ἥλιος 'sun'. The route is Greek ἅλως (acc. ἅλω) 'disk of the sun or moon, halo' → Arabic هَالَة hāla (a well-established Greek loan in the Arabic astronomical vocabulary, glossed 'the ring around the moon') → New Persian هاله hāle, with the Arabic tāʾ marbūṭa realised as Persian -e. Wiktionary states the chain explicitly: 'Borrowed from Arabic هالة (hāla, \\\"halo\\\"), from Ancient Greek ἅλως (hálōs, \\\"halo\\\")'. Two things are therefore wrong with the arrow as drawn: the Greek etymon is ἅλως, not ἥλιος, so the word does not belong under PIE *sāwel- at all (ἅλως is Pre-Greek / of unknown origin); and the Arabic mediation, which Nourai's own reference TAD (Unaysi's dictionary of foreign words in Arabic) documents, is left out. The gloss 'hue' is a loose extension of the modern figurative sense ('aura').\",\n          \"derivation_fa\": \"«هاله» در فارسی واژه‌ای کهن و ادبی است (شاهد صائب که نورایی آورده درست است)، ولی از ἥλιος «خورشید» نیامده. راه وام‌گیری چنین است: یونانی ἅλως «قرص و دایرهٔ گرد ماه و خورشید» ← عربی «هالة» (وام‌واژه‌ای یونانی در اصطلاحات نجومی عربی، با معنی «دارهٔ گرد قمر») ← فارسی نو «هاله»، که تاء مربوطهٔ عربی در آن به هـ/ـه فارسی بدل شده است. ویکی‌واژه همین زنجیره را می‌آورد. پس دو ایراد بر نمودار وارد است: نخست آنکه واژهٔ یونانی ἅλως است نه ἥλιος و ریشهٔ هندواروپایی *sāwel- هیچ نقشی در آن ندارد (ἅλως را پیش‌یونانی می‌دانند)؛ دوم آنکه میانجی عربی — که خودِ مأخذ مورد استناد نورایی، فرهنگ دخیل‌های طوبیا العنیسی، آن را ثبت کرده — حذف شده است. پژوهش امروزی ادعای نورایی را در این حلقه رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%87%D8%A7%D9%84%D9%87\",\n            \"https://www.etymonline.com/word/halo\",\n            \"https://abadis.ir/fatofa/%D9%87%D8%A7%D9%84%D9%87/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:5091\",\n              \"status\": \"partial\",\n              \"note\": \"Mo'in's entry read on abadis.ir (فرهنگ معین): 'هاله (لِ) (اِ.) خرمن ماه، دایرهٔ نورانی که گاه گاه گرداگرد ماه ظاهر می‌شود' — the word and sense are Mo'in's, but he attaches no origin tag here, and p. 5091 falls in the aʿlām volumes (5–6) which are not online, so the exact page could not be opened.\"\n            },\n            {\n              \"ref\": \"TAD:75\",\n              \"status\": \"supports\",\n              \"note\": \"Unaysi, Tafsīr al-alfāẓ al-dakhīla, TAD_pages.txt leaf 78 (printed p. ≈ 73–75, the stated offset is leaf − 4…6): 'هالة - ونالى وهاه وهو الطنياوة والدارة حول القمر' — OCR-garbled, but the headword هالة is listed among the dakhīl (foreign) words with what reads as 'يوناني' + the Greek etymon, glossed 'the disk and the circle around the moon'. It thus supports a Greek source for هالة — i.e. ἅλως, not ἥλιος.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"abadis.ir/fatofa/هاله (فرهنگ معین)\",\n              \"stance\": \"partial\",\n              \"note\": \"'خرمن ماه، دایرهٔ نورانی که گاه گاه گرداگرد ماه ظاهر می‌شود' — meaning confirmed, no etymology given.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhan-e Qateʿ vol. 2, BQT_v2_pages.txt line 11452, s.v. خرگه مه\",\n              \"stance\": \"silent\",\n              \"note\": \"'خرگه مه … مخفف خرگاه ماه است که هاله و خرمن ماه باشد' — Borhan uses هاله as a current Persian gloss but offers no etymology for it.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"HRN.txt, grep 'hāle/halo'\",\n              \"stance\": \"silent\",\n              \"note\": \"Horn's Grundriss has no entry for هاله — expected, since he treats inherited Iranian vocabulary, not Greek/Arabic loans.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"HUB.txt, grep 'hāla/halo'\",\n              \"stance\": \"silent\",\n              \"note\": \"Hübschmann, Persische Studien: no entry.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"English\",\n          \"words\": \"helium\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Modern Latin helium, coined from Greek ἥλιος 'sun' + the chemical suffix -ium. Named by the English astronomer J. Norman Lockyer and the chemist Edward Frankland after the unexplained bright yellow D₃ line they observed in the solar chromosphere during the eclipse of 18 August 1868; the element was not obtained on Earth until Ramsay's cleveite experiment of 1895, so the name really does mean 'the sun-substance'. The arrow Greek → English is exactly right, and it is the one place on this chart where ἥλιος itself (not the halo-word) is the source.\",\n          \"derivation_fa\": \"«هلیم/هلیوم» واژه‌ای ساختگی در لاتین نو است: ἥλιος یونانی «خورشید» + پسوند شیمیایی -ium. لاکیر (اخترشناس) و فرانکلند (شیمی‌دان) در سال ۱۸۶۸م پس از دیدن خط زرد ناشناخته در طیف خورشید هنگام خورشیدگرفتگی این نام را نهادند؛ خودِ عنصر تا ۱۸۹۵م روی زمین جدا نشد. پس پیکان «یونانی ← انگلیسی» در اینجا کاملاً درست است و تنها جایی از این نمودار است که سرچشمه به‌راستی ἥλιος «خورشید» است، نه واژهٔ «هاله».\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E1%BC%A5%CE%BB%CE%B9%CE%BF%CF%82\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai cites no reference for this node; the claim was checked against Klein and Watkins instead (see consulted).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"1971 ed. s.v. helium (KLN_1971.txt line 111743)\",\n              \"stance\": \"supports\",\n              \"note\": \"'helium, n., name of a gaseous element (chem.) — ModL., fr. Gk. ἥλιος, \\\"the sun\\\"; so called by the English astronomer Sir Joseph Norman Lockyer (1836-1920) and the English chemist Sir Edward Frankland (1825-99), because it was first observed by them in the spectrum of the sun (in 1868, during an eclipse).'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. sāwel- §3 and index (AHD_watkins1985.txt lines 905, 1590)\",\n              \"stance\": \"supports\",\n              \"note\": \"'HELIACAL, HELIO-, HELIOS, HELIUM' listed as English derivatives of *sāwel-yo- > Greek hēlios; index line 'HELIUM sāwel-'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Indo-European\",\n          \"words\": \"Swel 2\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"PIE *swel- 'to smoulder, burn, shine' is Pokorny's 'Root/lemma: suel-2, Meaning: to smoulder, burn', Page(s) 1045 — so both the numbering '2' and the page citation are right, and Watkins independently prints 'swel-². To shine, burn. … [Pok. 2. swel- 1045.]'. Hanging it under *sāwel- is Pokorny's own suggestion, not Nourai's invention: the note at IEW 881 says 'suel- \\\"smolder, burn\\\" is probably identical with it', and the suel-2 entry cross-refers 'see above S. 881 f. sāuel-'. The relation is best described as a probable ablaut variant of the same root complex rather than a derivation in the ordinary sense, which is why the arrow is drawn root → root here.\",\n          \"derivation_fa\": \"ریشهٔ هندواروپایی *swel- «سوختن، دود کردن، درخشیدن» در فرهنگ پوکورنی با سرواژهٔ suel-2 و معنای «schwelen, brennen» در صفحهٔ ۱۰۴۵ آمده است؛ پس هم شمارهٔ ۲ و هم ارجاع POK:1045 نورایی درست است و واتکینز نیز همین را «swel-². To shine, burn» ثبت کرده. قرار دادن آن زیر ریشهٔ *sāwel- نیز پیشنهاد خودِ پوکورنی است: در صفحهٔ ۸۸۱ می‌نویسد که suel- «احتمالاً با همین ریشه یکی است» و در مدخل suel-2 به صفحهٔ ۸۸۱ ارجاع می‌دهد. البته این پیوند از گونهٔ «اشتقاق» نیست، بلکه گونه‌ای دگرگونی مصوّتی (ablaut) در همان مجموعهٔ ریشه است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/swelter\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:1045\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt: 'Root / lemma: suel-2 / Meaning: to smoulder, burn' … 'References: WP. II 531 f., Scherer Gestirnnamen 49 f., Trautmann 296, Frisk 65 f.; See also: see above S. 881 f. sauel- / Page(s): 1 045'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II p. 531 (WLD_Bd2_pages.txt leaf 535)\",\n              \"stance\": \"supports\",\n              \"note\": \"'3. suel- \\\"schwelen, brennen\\\"' — same root, numbered 3 in Walde-Pokorny and 2 in Pokorny's IEW.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. swel-2 (AHD_watkins1985.txt line 1044)\",\n              \"stance\": \"supports\",\n              \"note\": \"'swel-², To shine, burn. 1. Extended form *sweld- in Germanic *swiltan … [Pok. 2. swel- 1045.]' — identical gloss and page reference to Nourai's.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Greek\",\n          \"words\": \"heleně; Heleně\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both words are real and Pokorny does put them both under *swel-2: IEW 1045 lists 'ἑλάνη \\\"flambeau, torch\\\", assim. ἑλένη Hes. [i.e. the Hesychius gloss ἑλένη· λαμπάς, δᾷς], Ἑλένη originally a light goddess', beside εἵλη/ἕλη 'solar warmth, sunlight' and ἀλέα 'warmth' — an old Greek family of 'heat/shine' words with the regular *sw- > h- development. Modern opinion is split on how the pieces fit. Wiktionary derives the name Ἑλένη from Proto-Hellenic *Hwelénā < a late-PIE *Swelénā 'solar deity' < *swel-, which is precisely Nourai's arrow, but adds that the name is 'unrelated to ἑλένη (torch), σέλας or σελήνη' — i.e. it keeps the root but severs the link to the common noun in the same box. Watkins, the reference Nourai cites, is different again: he puts the name under wel-³ 'to turn, roll' ('Suffixed form *wel-enā, possibly identical with the Greek name Helenē (earliest form Welenā)'), with initial *w-, not *sw-. So the node is defensible on Pokorny's authority but not uncontested, and the citation to AHD points the wrong way.\",\n          \"derivation_fa\": \"هر دو واژه راستین‌اند و پوکورنی (ص ۱۰۴۵) هر دو را زیر ریشهٔ *swel- آورده است: «ἑλάνη \\\"مشعل\\\"، با همگونی ἑλένη نزد هسیخیوس، و Ἑλένη که در اصل ایزدبانوی روشنایی بوده»، در کنار εἵλη «گرمای آفتاب» و ἀλέα «گرما»؛ در همهٔ اینها *sw- آغازین هندواروپایی قاعده‌مند به h- یونانی بدل شده است. اما دیدگاه امروزی یکدست نیست: ویکی‌واژه نامِ Ἑλένη را از یونانی آغازین *Hwelénā و آن را از *Swelénā «ایزد خورشید» می‌داند — یعنی همان پیکان نورایی — ولی تأکید می‌کند که این نام با ἑλένη «مشعل» و σέλας و σελήνη هم‌ریشه نیست. از سوی دیگر واتکینز (همان AHD که نورایی به آن ارجاع داده) نام را زیر ریشهٔ wel- «چرخیدن» و با صورت کهن *Welenā می‌گذارد. پس ادعای نورایی با پشتوانهٔ پوکورنی پذیرفتنی است، اما اجماعی نیست و ارجاع او به AHD خلاف مدعایش را می‌گوید.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E1%BC%99%CE%BB%CE%AD%CE%BD%CE%B7\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD:611\",\n              \"status\": \"not_checked\",\n              \"note\": \"AHD:611 is a page of the main New College Edition dictionary (the 'Hel-' range), and every archive.org copy of that edition is lending-only, so the page itself could not be opened. The Watkins IE appendix of the same dictionary, which is on disk, does not put Helenē under swel-2 at all — see the 'consulted' AHD entry below.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 1045, s.v. suel-2 (POK_full.txt line 83754 ff.)\",\n              \"stance\": \"supports\",\n              \"note\": \"'gr. εἵλη, εἵλη- ἕλη f. \\\"solar warmth, sunlight\\\" … ἑλάνη \\\"flambeau, torch\\\", assim. ἑλένη Hes., Ἑλένη originally a light goddess'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II p. 531 (leaf 535)\",\n              \"stance\": \"supports\",\n              \"note\": \"'ἑλάνη \\\"Fackel\\\", ἑλένη· λαμπάς· δᾴς Hes., Ἑλένη ursprgl. eine Lichtgöttin'.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. wel-3 §10 (AHD_watkins1985.txt line 1140)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'10. Suffixed form *wel-enā, possibly identical with the Greek name Helenē (earliest form Welenā), Helen, in Greek helenion, elecampane: ELECAMPANE, INULIN.' Watkins assigns the name to *wel- 'to turn, roll', not to swel-2.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"Helen, Aileen\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Helen is straightforward: Greek Ἑλένη → Latin Helena → Old French Heleine/Elaine and Middle English Elyne/Helen, revived in its Latin form in the sixteenth century; whatever the ultimate PIE root, the English name does continue the Greek one. Aileen does not. It is a Scots/Irish spelling variant of Eileen, which is the Anglicised form of Irish Eibhlín, and Eibhlín is the Gaelic adaptation of the Anglo-Norman name Aveline (a Norman diminutive of a Germanic *Avi- name) brought to Ireland after 1169. Behind the Name records only that Eileen 'is also sometimes considered an Irish form of Helen' — a later, secondary equation made because the two names sound alike, not a line of descent. So half of this box is confirmed and half is a folk identification; the node takes the worse verdict.\",\n          \"derivation_fa\": \"«Helen» بی‌گمان دنبالهٔ همان نام یونانی است: Ἑλένη ← Helena لاتین ← Heleine/Elaine در فرانسوی کهن ← Elyne/Helen در انگلیسی میانه، که در سدهٔ شانزدهم به صورت لاتینی‌اش زنده شد. اما «Aileen» چنین نیست: این نام گونهٔ اسکاتلندی-ایرلندیِ Eileen است و Eileen خود صورت انگلیسی‌شدهٔ Eibhlín ایرلندی است که از نام آنگلونورمن Aveline (کوچک‌شدهٔ نامی ژرمنی با عنصر *Avi-) گرفته شده و پس از ۱۱۶۹م با نورمن‌ها به ایرلند رسیده است. فرهنگ Behind the Name تنها می‌گوید که Eileen را «گاه صورت ایرلندی Helen می‌شمارند» — یعنی همانندسازی پسین بر پایهٔ شباهت آوایی، نه پیوند نسبی. پس نیمی از این خانه درست و نیم دیگر ریشه‌شناسی عامیانه است.\",\n          \"sources\": [\n            \"https://www.behindthename.com/name/eileen\",\n            \"https://en.wiktionary.org/wiki/%E1%BC%99%CE%BB%CE%AD%CE%BD%CE%B7\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"not_checked\",\n              \"note\": \"The AHD reference is to the main dictionary (name entries), which is lending-only on archive.org; the Watkins appendix on disk lists no English name derivatives under swel-2 at all ('[Pok. 2. swel- 1045.]' yields only SULTRY, SWELTER, SWALE).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. swel-2 and index (AHD_watkins1985.txt lines 1044, 2325)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"The only English words the appendix derives from swel-2 are SULTRY, SWELTER and SWALE; 'HELEN' and 'AILEEN' do not appear in the index at all.\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"behindthename.com/name/eileen and /name/aileen (name-etymology reference used in place of Webster, whose vol. 2 is not on disk)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'Anglicized form of Eibhlín'; 'It is also sometimes considered an Irish form of Helen' — the Helen equation is explicitly a secondary association, the source being Norman Aveline.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Germanic\",\n          \"words\": \"swiltan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The form belongs to Gothic: Gothic swiltan 'to die', beside Old English and Old Saxon sweltan 'to die, perish', Old Icelandic svelta 'to starve, die', Middle Dutch swelten; the Proto-Germanic verb is *sweltaną, a strong class-III verb from an extended PIE *sweld-. Watkins, Nourai's source, writes exactly 'Extended form *sweld- in Germanic *swiltan in Old English sweltan, to die, perish (perhaps < \\\"be overcome with heat\\\")'. Two reservations: the label 'Germanic' is applied to what is really the Gothic shape (the reconstructed Proto-Germanic form is *sweltaną / *swiltaną in the zero grade), and the attested meaning of the verb everywhere in Germanic is simply 'to die' — 'to perish from heat' is Watkins's parenthesised guess about how the sense arose from the root 'burn', copied by Nourai as if it were the recorded gloss. Pokorny 1045 lists the same forms and sets the semantic bridge out through Old High German swelzan 'to burn' and English sweltry/sultry.\",\n          \"derivation_fa\": \"این صورت در واقع گوتی است: gothic swiltan «مردن»، در کنار sweltan در انگلیسی کهن و ساکسونی کهن، svelta در ایسلندی کهن «از گرسنگی مردن» و swelten در هلندی میانه؛ صورت بازسازی‌شدهٔ ژرمنی آغازین *sweltaną است، فعلی قوی از گسترش *sweld- هندواروپایی. واتکینز — که مأخذ نورایی است — دقیقاً می‌نویسد: «صورت گستردهٔ *sweld- در ژرمنی *swiltan، در انگلیسی کهن sweltan «مردن، هلاک شدن» (شاید در اصل: از گرما از پا درآمدن)». دو نکتهٔ احتیاط: برچسب «ژرمنی» بر صورتی گوتی نهاده شده، و معنای گواهی‌شدهٔ این فعل در سراسر زبان‌های ژرمنی تنها «مردن» است؛ «هلاک شدن از گرما» حدس درون‌کمانک واتکینز دربارهٔ چگونگی پیدایش معناست که نورایی آن را چون معنای ثبت‌شده آورده است. پس ادعا با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/swelter\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. swel-2: '1. Extended form *sweld- in Germanic *swiltan in Old English sweltan, to die, perish (perhaps < \\\"be overcome with heat\\\"): (SULTRY), SWELTER.' — Nourai's form, parent and gloss are taken verbatim from here.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 1045 (POK_full.txt s.v. suel-2)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Old English Old Saxon sweltan strong V. \\\"die, pass away\\\", Middle Dutch swelten, Old Icelandic svelta \\\"starve, die\\\", Gothic swiltan \\\"to die\\\" … the o-present in Old High German swelzan \\\"burn, incinerate\\\", for what presumably as \\\"swelter\\\" (compare engl. sweltry, sultry \\\"extremely hot\\\")'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II p. 531 f. (leaf 535)\",\n              \"stance\": \"supports\",\n              \"note\": \"Same Germanic set under '3. suel- \\\"schwelen, brennen\\\"'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"swelter\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle English swelteren, a frequentative in -er of swelten 'to faint, die (of heat)', itself from Old English sweltan 'to die' < Proto-Germanic *sweltaną < PIE *swel- 'to smoulder, burn'. The frequentative shifted the sense from the old 'die' to 'be oppressed by heat, sweat profusely', and the same root gave sultry (from the related verb sweltry). The chain Germanic → English is exactly as drawn.\",\n          \"derivation_fa\": \"swelter از انگلیسی میانهٔ swelteren است، صورت تکراری (frequentative) با پسوند -er از swelten «از گرما بیهوش شدن، مردن»، و آن از sweltan انگلیسی کهن «مردن» از ژرمنی آغازین *sweltaną و ریشهٔ هندواروپایی *swel- «سوختن». همین پسوند تکراری معنا را از «مردن» کهن به «از گرما در تب‌وتاب بودن، عرق ریختن» کشانده است و sultry نیز از همین خانواده است. پس پیکان «ژرمنی ← انگلیسی» درست است و ادعای نورایی در این گره تأیید می‌شود.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/swelter\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. swel-2 lists '(SULTRY), SWELTER' as the English outcome of Germanic *swiltan; index line 'SWELTER swel-2'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein/Wiktionary chain (KLN_1966 is truncated after 'veratral' and has no 'swelter' leaf)\",\n              \"stance\": \"silent\",\n              \"note\": \"The local Klein 1966 OCR breaks off in V, so the 'swelter' entry could not be read; Wiktionary supplies the same chain: 'From Middle English swelteren, frequentative of swelten … from Old English sweltan … from Proto-Germanic *sweltaną … from Proto-Indo-European *swel-'.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 1045\",\n              \"stance\": \"supports\",\n              \"note\": \"'presumably as \\\"swelter\\\" (compare engl. sweltry, sultry \\\"extremely hot\\\")'.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Šay'\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Arabic شَيْء šayʾ 'thing' (root ش ي أ š-y-ʾ, beside شَاءَ šāʾa 'to will')\",\n      \"note\": \"The root box itself is unobjectionable: شَيْء is a common Arabic noun 'thing, something' (Qurʾān 13:16 'خالق كل شيء'), plural أَشْيَاء ʾašyāʾ, formally a maṣdar-type noun of the root ش ي أ whose verb شَاءَ means 'to will' (so 'a thing' is etymologically 'what is willed'). Strictly this is a word, not a root, and Nourai's headword should be the consonantal root š-y-ʾ. The trouble on this chart is everything below node 1: the story that algebraic x is a Spanish abbreviation of šayʾ is repeated by Klein (and by Partridge and Webster), but it is rejected by the OED and by Cajori's History of Mathematical Notations, who show that x, y, z as unknowns were introduced by Descartes in the Géométrie of 1637 simply as the last three letters of the alphabet, matched to a, b, c for knowns.\",\n      \"note_fa\": \"خودِ خانهٔ ریشه ایرادی ندارد: «شَیء» اسمی عربی به معنی «چیز» است (قرآن ۱۳:۱۶ «خالق کل شیء»)، جمع آن «أشیاء»، از ریشهٔ «ش ی أ» که فعل آن «شاءَ» یعنی «خواستن» است؛ پس «شیء» در اصل «آنچه خواسته شده» است. البته آنچه نورایی سرواژهٔ ریشه گذاشته یک واژه است نه ریشه، و صورت درست ریشه «ش ی أ» است. اشکال اصلی این نمودار در گره‌های پایین است: داستان اینکه «x» در جبر کوتاه‌شدهٔ «شیء» عربی از راه اسپانیایی است، هرچند در فرهنگ کلاین و پارتریج و وبستر آمده، در فرهنگ آکسفورد و در تاریخ نمادهای ریاضی کاژوری به‌صراحت رد شده است: دکارت در «هندسه» (۱۶۳۷م) سه حرف پایانی الفبا را برای مجهول‌ها برگزید، در برابر a و b و c برای معلوم‌ها.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%B4%D9%8A%D8%A1\",\n        \"https://mathshistory.st-andrews.ac.uk/Miller/mathsym/variables/\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"KLN:1756\",\n          \"status\": \"supports\",\n          \"note\": \"Klein (1971 one-vol. text, line 268900) s.v. 'X, x, principal unknown quantity (alg.) — Sp. X, x, shortened fr. Arab. shay, \\\"a thing, something\\\", used also in the sense of \\\"unknown quantity\\\" (in Medieval Spanish x was pronounced sh); introduced by Descartes.' The Arabic word and its gloss are exactly as Nourai's root box has them.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"KLN\",\n          \"where\": \"KLN_1971.txt line 268900 s.v. X, x\",\n          \"stance\": \"supports\",\n          \"note\": \"See ref_check — Klein has šayʾ 'a thing, something'.\"\n        },\n        {\n          \"src\": \"FVQ\",\n          \"where\": \"FVQ_pages.txt, grep 'shay'\",\n          \"stance\": \"silent\",\n          \"note\": \"Jeffery's Foreign Vocabulary of the Qurʾān has no entry for شيء — as expected, since it is a native Arabic word and his book lists loanwords only.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"šey'\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian شیء šeyʾ is a direct Arabic loan of the ordinary literary kind, taken in with the rest of the scholastic and legal vocabulary from the third/ninth century onward; Moʿin tags it '[ع.]' and defines it 'آنچه که بتوان از آن اعلام و اخبار کرد، چیز. ج. اشیاء'. The Arabic hamza is kept in writing (شیء) but is regularly dropped in Persian pronunciation, giving šey. The two forms in the chart's extra field are the Arabic broken plural أشیاء ʾašyāʾ and its Persianised spelling اشیا, which drops the final hamza exactly as Persian does with انشا, املا, ابتدا. Moʿin also records the very sense that matters for the rest of the chart: '۲- مجهول (ریاضی)' — 'the unknown, in mathematics' — showing that Arabic-Persian algebra did indeed call the unknown šayʾ.\",\n          \"derivation_fa\": \"«شیء» وام‌واژه‌ای مستقیم از عربی است که همراه واژگان کلامی و فقهی از سدهٔ سوم هجری به بعد به فارسی راه یافته؛ معین آن را با نشان [ع.] می‌آورد: «آنچه که بتوان از آن اعلام و اخبار کرد، چیز. ج. اشیاء». همزهٔ عربی در نوشتار نگه داشته می‌شود ولی در تلفظ فارسی معمولاً می‌افتد و واژه «شِی» خوانده می‌شود. دو صورتی که نورایی در کنار واژه آورده جمع مکسّر عربی «أشیاء» و املای فارسی‌شدهٔ «اشیا» است که همزهٔ پایانی را می‌اندازد، درست مانند «انشا، املا، ابتدا». نکتهٔ مهم آنکه معین معنای دوم «مجهول (ریاضی)» را نیز ثبت کرده است؛ یعنی در جبر عربی-فارسی به‌راستی مجهول را «شیء» می‌نامیدند.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%B4%DB%8C%D8%A1/\",\n            \"https://en.wiktionary.org/wiki/%D8%B4%D9%8A%D8%A1\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON\",\n              \"status\": \"supports\",\n              \"note\": \"Moʿin via abadis.ir: 'شیء (شَ یا ش) [ع.] (اِ.) ۱- آن چه که بتوان از آن اعلام و اخبار کرد، چیز. ج. اشیاء. ۲- مجهول (ریاضی).' Arabic origin tag and both the plural and the mathematical sense are there; Nourai gives no page for MON here, so only the entry could be checked.\"\n            },\n            {\n              \"ref\": \"FVA:223\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nahvi's Farhang-e vāžehā-ye ʿarabi dar fārsi (1368/1989) has no digital copy on any permitted platform (refs_online.json: 'RE-SEARCH 2026-09: still no digital copy').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"abadis.ir/fatofa/شیء (فرهنگ معین)\",\n              \"stance\": \"supports\",\n              \"note\": \"'[ع.] … چیز. ج. اشیاء. ۲- مجهول (ریاضی)'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Wiktionary s.v. Arabic شيء, descendants list\",\n              \"stance\": \"supports\",\n              \"note\": \"Wiktionary lists Persian شیء among the descendants of Arabic شَيْء, alongside Turkish şey and Maltese xi.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Spanish\",\n          \"words\": \"X\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The premises are true but the conclusion is not attested. Medieval Spanish x did stand for /ʃ/ (as in dixo, Quixote, and in Arabisms such as xarabe > jarabe), and Arabic algebra from al-Khwārizmī onward did call the unknown شَيْء šayʾ — Latin translators rendered it res and the Italians cosa, which is why algebra was 'the cossic art'. What is missing is any medieval Spanish text abbreviating šayʾ as x. The OED states flatly: 'There is no evidence in support of the hypothesis that x is derived ultimately from the mediaeval transliteration xei of shei \\\"thing\\\"', and Cajori's History of Mathematical Notations reaches the same conclusion, attributing x, y, z to Descartes's Géométrie (1637), where he took the last letters of the alphabet for unknowns to match a, b, c for knowns. Klein and Partridge, Nourai's two references, are both repeating an older lexicographers' story (traceable to Webster) rather than a documented derivation; so the Spanish node is a folk etymology.\",\n          \"derivation_fa\": \"مقدمه‌ها درست‌اند ولی نتیجه گواهی ندارد. حرف x در اسپانیایی سده‌های میانه به‌راستی آوای /ش/ داشت (مانند dixo و Quixote و در وام‌واژه‌های عربی چون xarabe > jarabe)، و در جبر عربی از خوارزمی به بعد مجهول را «شیء» می‌نامیدند که مترجمان لاتینی آن را res و ایتالیایی‌ها cosa برگرداندند. اما هیچ متن اسپانیایی کهنی یافت نشده که «شیء» را به x کوتاه کرده باشد. فرهنگ آکسفورد صریح می‌گوید: «هیچ شاهدی بر این فرض نیست که x سرانجام از آوانگاشت قرون‌وسطایی xei از shei «چیز» آمده باشد»، و کاژوری نیز در «تاریخ نمادهای ریاضی» همین را می‌گوید و پیدایش x و y و z را به «هندسهٔ» دکارت (۱۶۳۷م) بازمی‌گرداند که سه حرف پایانی الفبا را برای مجهول‌ها در برابر a و b و c برای معلوم‌ها برگزید. کلاین و پارتریج، دو مأخذ نورایی، تنها روایتی دیرین از فرهنگ‌نویسان (با خاستگاه وبستر) را بازگو می‌کنند. پس این گره ریشه‌شناسی عامیانه است و پژوهش امروزی آن را رد می‌کند.\",\n          \"sources\": [\n            \"https://mathshistory.st-andrews.ac.uk/Miller/mathsym/variables/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"PRT:813\",\n              \"status\": \"not_checked\",\n              \"note\": \"Partridge's Origins is lending-only on archive.org (originsshortetym00part); the page could not be opened. Partridge is known to repeat the same story, which is why Nourai pairs him with Klein.\"\n            },\n            {\n              \"ref\": \"KLN:1756\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1971.txt line 268900: 'X, x, principal unknown quantity (alg.) — Sp. X, x, shortened fr. Arab. shay, \\\"a thing, something\\\", used also in the sense of \\\"unknown quantity\\\" (in Medieval Spanish x was pronounced sh); introduced by Descartes.' Klein says exactly what the node says — but see the consulted entries for why this is no longer accepted.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Jeff Miller, Earliest Uses of Symbols for Variables (MacTutor mirror), citing Webster, the OED and Cajori\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'According to Webster\\\\'s … X was used as an abbreviation for Arabic shei a thing, something, which, in the Middle Ages, was used to designate the unknown, and was then prevailingly transcribed as xei'; but 'The OED refutes this: There is no evidence in support of the hypothesis that x is derived ultimately from the mediaeval transliteration xei of shei \\\"thing\\\".' 'Cajori says there is no evidence for this.'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"SKT.txt, grep 'x, unknown'\",\n              \"stance\": \"silent\",\n              \"note\": \"Skeat's Concise Etymological Dictionary has no entry for the algebraic x.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"English\",\n          \"words\": \"X; x-ray\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The internal link is sound and the external one is not. X-ray is certainly named from the mathematical x for an unknown: Wilhelm Conrad Röntgen, announcing his discovery to the Würzburg Physical-Medical Society on 28 December 1895, called the new radiation X-Strahlen precisely because its nature was unknown, and Klein's entry says so ('They were called by their discoverer … X Strahlen (= X-rays), to suggest that the exact nature of radiation was unknown. For such use of the letter x see X, x'). But the English algebraic x is not inherited from a Spanish abbreviation of šayʾ: it comes to English with Descartes's notation from the Géométrie of 1637, which English mathematicians adopted in the later seventeenth century, and the OED denies any Arabic transmission. The node therefore takes the same disputed verdict as its parent, with the x-ray half confirmed.\",\n          \"derivation_fa\": \"پیوند درون این خانه درست است و پیوند بیرونی آن نادرست. «اشعهٔ ایکس» به‌یقین از همان xِ ریاضی به معنی «مجهول» نام گرفته است: ویلهلم کنراد رونتگن در ۲۸ دسامبر ۱۸۹۵م هنگام اعلام کشف خود در انجمن فیزیکی-پزشکی وورتسبورگ این پرتو را X-Strahlen نامید، زیرا ماهیتش ناشناخته بود، و کلاین نیز همین را می‌نویسد. اما xِ جبری انگلیسی از کوتاه‌نوشتِ اسپانیاییِ «شیء» به ارث نرسیده است؛ این نماد با نمادگذاری دکارت («هندسه»، ۱۶۳۷م) وارد انگلیسی شد و ریاضی‌دانان انگلیسی در نیمهٔ دوم سدهٔ هفدهم آن را پذیرفتند، و فرهنگ آکسفورد هرگونه انتقال از عربی را رد می‌کند. پس داوری این گره نیز مانند گرهٔ مادرش «ردشده» است، هرچند بخش «اشعهٔ ایکس» آن درست است.\",\n          \"sources\": [\n            \"https://mathshistory.st-andrews.ac.uk/Miller/mathsym/variables/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:1756\",\n              \"status\": \"supports\",\n              \"note\": \"Klein has both halves of the node: 'X, x, principal unknown quantity (alg.) — Sp. X, x, shortened fr. Arab. shay …' and 'X rays, n. pl., Roentgen rays. — They were called by their discoverer Wilhelm Konrad von Roentgen (1845-1923) (in 1896) X Strahlen (= X-rays), to suggest that the exact nature of radiation was unknown.' (KLN_1971.txt lines 268900 and 269147).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Jeff Miller, Earliest Uses of Symbols for Variables (MacTutor mirror)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'The introduction of x, y, z as symbols of unknown quantities is due to Descartes (Géométrie, 1637)' … 'The OED refutes this [the shei > xei story].'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1971.txt line 269147 s.v. X rays\",\n              \"stance\": \"partial\",\n              \"note\": \"Supports the x-ray naming (with the date given as 1896 — the announcement was 28 December 1895, the printed paper early 1896) but is the very source of the disputed Arabic claim.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"S.d.a`\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Arabic root ص د ع ṣ-d-ʿ, verb صَدَعَ ṣadaʿa 'to split, cleave'\",\n      \"note\": \"The root box is right in every particular: ص د ع is a productive Arabic root meaning 'to split, cleave, crack' (Qurʾān 15:94 'فاصدع بما تؤمر', 86:12 'والأرض ذات الصدع'), and Nourai's 'S.d.a`' with the final backtick for ʿayn is his usual notation. The chart's real problem is one step down, at the Latin node: the medical Latin soda 'headache' does continue Arabic ṣudāʿ, but soda the alkali — the ancestor of English soda and sodium — almost certainly does not, and Nourai (following Klein) treats them as one word. The two Persian tips are both modern European re-imports, sodâ via English and sodyom via French, so the Persian side of the page is a genuine round trip only if the disputed Latin link holds.\",\n      \"note_fa\": \"خانهٔ ریشه از هر نظر درست است: «ص د ع» ریشه‌ای زایا در عربی به معنی «شکافتن، ترکاندن» است (قرآن، «فاصدع بما تؤمر» و «والأرض ذات الصدع») و نویسهٔ «S.d.a`» با علامت ` برای عین، شیوهٔ همیشگی نورایی است. اشکال نمودار یک پله پایین‌تر، در خانهٔ لاتین است: واژهٔ پزشکی لاتین میانه soda «سردرد سخت» به‌راستی از «صُداع» عربی است، ولی soda به معنی قلیا — نیای soda و sodium انگلیسی — به احتمال بسیار از آن نیامده، و نورایی به پیروی کلاین این دو را یکی گرفته است. دو شاخهٔ فارسیِ پایین نمودار هر دو وام‌واژه‌های نو اروپایی‌اند: «سودا» از انگلیسی و «سدیم» از فرانسه؛ پس این «رفت‌وبرگشت» عربی-اروپایی-فارسی تنها در صورتی کامل است که حلقهٔ مورد اختلاف لاتین پذیرفته شود.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%B5%D8%AF%D8%A7%D8%B9\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"SAP:857\",\n          \"status\": \"not_checked\",\n          \"note\": \"Sayyāḥ's Farhang-e Sayyāḥ (the Persian rendering of al-Munjid) is sold only as a paid ebook (fidibo.com/book/142427); no accessible copy, so p. 857 could not be opened. The Arabic content it would carry was checked instead in Wiktionary and Devic.\"\n        },\n        {\n          \"ref\": \"KLN:1468\",\n          \"status\": \"partial\",\n          \"note\": \"Klein does say what Nourai's chart says — 'soda, n., an alkaline substance. — ML., fr. ML. sodanum, lit. \\\"headache remedy\\\", fr. soda, \\\"headache\\\", fr. Arab. sudāʿ, in vulgar pronunciation ṣodāʿ, \\\"splitting headache\\\", fr. ṣadaʿa, \\\"he split\\\". Cp. sodalite, sodium.' (KLN_1966.txt line 35794) — but in the archive.org scan of the 1966 two-volume edition that entry sits on leaf 779, i.e. printed p. ≈ 1531, whereas p. 1468 of that scan falls in the 'scr-/se-' range (leaf 748 = p. 1469 per the calibration in refs_online.json). The substance supports Nourai; the page number does not match this printing.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"KLN\",\n          \"where\": \"KLN_1966.txt line 35794 s.v. soda\",\n          \"stance\": \"supports\",\n          \"note\": \"See ref_check — Klein derives soda from Arabic ṣudāʿ via ML sodanum.\"\n        },\n        {\n          \"src\": \"FVQ\",\n          \"where\": \"FVQ_pages.txt, grep 'sudaa/suda'\",\n          \"stance\": \"silent\",\n          \"note\": \"Jeffery has no entry — ṣudāʿ is native Arabic, not a Qurʾānic loanword.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"sodâ`\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic صُدَاع ṣudāʿ 'headache' is a verbal noun of the fuʿāl pattern, the pattern Arabic reserves for ailments (زُكَام zukām 'head cold', سُعَال suʿāl 'cough', دُوَار duwār 'vertigo'), formed on ṣadaʿa 'he split, cleaved'. The literal sense is therefore exactly Nourai's 'a head-splitting headache' — the image of a skull being cracked open. Wiktionary gives the word as ṣudāʿ, masculine, uncountable, 'headache', 'derived from the root ص د ع'; Devic, describing the same word as the source of French medical soda, writes 'De l'arabe صداع sodâʿ … qui se rattache à صدع sadaʿa, fendre en deux'. Klein's note that the vulgar pronunciation is ṣodāʿ explains Nourai's transcription with -o-.\",\n          \"derivation_fa\": \"«صُداع» در عربی مصدری بر وزن فُعال است، همان وزنی که عربی برای نام بیماری‌ها به کار می‌برد (زُکام، سُعال، دُوار)، ساخته‌شده از فعل «صَدَعَ» یعنی «شکافت». پس معنای تحت‌اللفظی آن دقیقاً همان است که نورایی نوشته: «سردردی که سر را می‌شکافد». ویکی‌واژه آن را «صُداع، اسم مذکر، سردرد، از ریشهٔ ص د ع» می‌آورد و دُویک در شرح واژهٔ پزشکی فرانسوی soda می‌نویسد: «از عربی صداع sodâʿ … که به صدع sadaʿa \\\"به دو نیم شکافتن\\\" بازمی‌گردد». تلفظ عامیانهٔ ṣodāʿ که کلاین یاد می‌کند، آوانگاشت نورایی را با «o» توضیح می‌دهد. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B5%D8%AF%D8%A7%D8%B9\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"SAP:857\",\n              \"status\": \"not_checked\",\n              \"note\": \"Sayyāḥ's dictionary is not digitised (paid ebook only); the Arabic claim was verified independently in Wiktionary, Devic and Klein.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"DEV\",\n              \"where\": \"Devic, Dict. étym. des mots d'origine orientale, p. 210 (DEV.txt line 2133)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Soda. Ancien terme de médecine, violent mal de tête. De l'arabe صداع sodâʿ, même sens, qui se rattache à صدع sadaʿa, fendre en deux.'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt line 35794 s.v. soda\",\n              \"stance\": \"supports\",\n              \"note\": \"'fr. Arab. sudāʿ, in vulgar pronunciation ṣodāʿ, \\\"splitting headache\\\", fr. ṣadaʿa, \\\"he split\\\".'\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"sodâ`\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian صُداع sodāʿ is an ordinary Arabic loan of the classical literary register, in use from the Ghaznavid period onward and familiar from medical prose (Avicenna's Persian followers) as well as poetry — Nourai's Rumi line 'مطرب عشق این زند وقت سماع … خداوندی صُداع' is genuine. Moʿin gives it with the Arabic tag: 'صداع (صُ) [ع.] (اِ.) ۱- دردسر. ۲- موجب زحمت. ۳- مزاحمت', i.e. the word kept its literal 'headache' sense and also developed the figurative one 'nuisance, bother' — the same metaphor as native Persian دردسر. Phonetically nothing changes: Persian takes the Arabic form whole, with ʿayn written but not pronounced.\",\n          \"derivation_fa\": \"«صُداع» وام‌واژه‌ای عربی از لایهٔ ادبی و کلاسیک است که از دورهٔ غزنوی به بعد در نثر پزشکی و شعر فارسی به کار رفته؛ بیت مولوی که نورایی آورده اصیل است. معین آن را با نشان [ع.] ثبت کرده: «صداع (صُ) [ع.] (اِ.) ۱- دردسر. ۲- موجب زحمت. ۳- مزاحمت»؛ یعنی واژه هم معنای اصلی «سردرد» را نگه داشته و هم معنای مجازی «زحمت و مزاحمت» یافته است — همان استعاره‌ای که در ترکیب فارسی «دردسر» نیز دیده می‌شود. از نظر آوایی دگرگونی‌ای رخ نداده و عین عربی در فارسی نوشته می‌شود ولی تلفظ نمی‌گردد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%B5%D8%AF%D8%A7%D8%B9/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:2137\",\n              \"status\": \"supports\",\n              \"note\": \"Moʿin read on abadis.ir: 'صداع (صُ) [ع.] (اِ.) ۱- دردسر. ۲- موجب زحمت. ۳- مزاحمت.' The Arabic origin tag and the sense are exactly what the node claims; the online Moʿin carries no page numbers, so p. 2137 itself could not be confirmed.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"abadis.ir/fatofa/صداع (فرهنگ معین)\",\n              \"stance\": \"supports\",\n              \"note\": \"'[ع.] (اِ.) ۱- دردسر …' — tagged Arabic.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhan-e Qateʿ, grep صداع in BQT_v2/v3/v4_pages.txt\",\n              \"stance\": \"silent\",\n              \"note\": \"No entry: Borhan-e Qateʿ is a dictionary of Persian (and Zand-Pazand) words and normally excludes plain Arabic loans like صداع.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Latin\",\n          \"words\": \"soda; sodanum\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Two different medieval words have been rolled into one box. (a) Medical Latin/Old French soda 'violent headache' is a real Arabism: Devic p. 210 lists it as 'Ancien terme de médecine, violent mal de tête. De l'arabe صداع sodâʿ', and that much of Nourai's arrow stands. (b) Medieval Latin soda / Italian soda 'saltwort, the alkaline ash burnt from it' — the word that actually produced English soda and sodium — is now derived quite differently. Wiktionary takes English soda from Italian soda and the Italian word ultimately from Arabic سُوَيْدَاء suwaydāʾ, a name of the plant Suaeda; Etymonline reports the same plant etymology (via Catalan sosa, attested from the late 13th century) and says explicitly of the ṣudāʿ route that it is 'considered far-fetched in some quarters'; Skeat offers a third account, Italian soda as the feminine of sodo 'solid, hard' < Latin solidus, 'prob. from the hardness of the [ash] obtained from glasswort'. Klein's sodanum 'headache remedy', on which Nourai's gloss 'an alkaline used to cure headaches' depends, is a rare medical-Latin word and is exactly the link modern lexicography rejects. So: the headache-word yes, the alkali-word no.\",\n          \"derivation_fa\": \"در این خانه دو واژهٔ جداگانهٔ سده‌های میانه در هم آمیخته‌اند. نخست، soda در لاتین پزشکی و فرانسوی کهن به معنی «سردرد سخت» که به‌راستی وام‌واژه‌ای عربی است؛ دُویک (ص ۲۱۰) آن را «اصطلاح کهن پزشکی، سردرد شدید، از عربی صداع» می‌داند و تا اینجا پیکان نورایی درست است. دوم، soda در لاتین میانه و ایتالیایی به معنی «گیاه شور و خاکستر قلیایی آن» — همان واژه‌ای که soda و sodium انگلیسی از آن آمده — که امروز به‌گونه‌ای دیگر ریشه‌یابی می‌شود: ویکی‌واژه آن را از ایتالیایی soda و سرانجام از عربی «سُوَیداء» (نام گیاه Suaeda) می‌داند؛ اتیمانلاین نیز همین ریشهٔ گیاهی را (از راه sosa کاتالانی، گواهی‌شده از اواخر سدهٔ سیزدهم) می‌آورد و دربارهٔ راه «صداع» می‌نویسد که «در برخی محافل دور از ذهن شمرده می‌شود»؛ اسکیت روایت سومی دارد: soda مؤنث sodo ایتالیایی «سفت» از solidus لاتین. واژهٔ sodanum «داروی سردرد» در فرهنگ کلاین، که معنای نورایی بر آن تکیه دارد، همان حلقه‌ای است که فرهنگ‌نویسی امروز آن را رد می‌کند. پس: واژهٔ «سردرد» آری، واژهٔ «قلیا» نه.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/soda\",\n            \"https://en.wiktionary.org/wiki/soda\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:1468\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt line 35794: 'soda, n., an alkaline substance. — ML., fr. ML. sodanum, lit. \\\"headache remedy\\\", fr. soda, \\\"headache\\\", fr. Arab. sudāʿ … fr. ṣadaʿa, \\\"he split\\\".' Klein states precisely Nourai's chain (page caveat as in the root-level ref_check: the entry stands at p. ≈ 1531 of the 1966 scan).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"DEV\",\n              \"where\": \"Devic p. 210 (DEV.txt line 2133)\",\n              \"stance\": \"partial\",\n              \"note\": \"Supports the Arabic origin of the medical term only: 'Soda. Ancien terme de médecine, violent mal de tête. De l'arabe صداع sodâʿ …' — Devic gives no alkali sense at all under this head.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etym. Dict., s.v. Soda (SKT.txt line 17762)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'Soda. (Ital. — L.) Ital. soda, O. Ital. soda, \\\"a kind of ferne ashes whereof they make glasses\\\": Florio. Fem. of Ital. sodo, \\\"solid, tough\\\" … prob. from the hardness of the [ash] obtained from glasswort — L. solidus, solid, hard. Der. sod-ium, a coined [word].' No Arabic at all.\"\n            },\n            {\n              \"src\": \"LKT\",\n              \"where\": \"LKT.txt, grep 'Soda / suwwād / Natron'\",\n              \"stance\": \"silent\",\n              \"note\": \"Lokotsch's dictionary of European words of oriental origin has no 'Soda' entry from ṣudāʿ (only Natron < Arabic naṭrūn, no. 1567, and the unrelated mezacote); its silence on soda is itself evidence that he did not accept it as an Arabism.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"soda; sodium\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"English soda is first recorded in the late fifteenth century for the sodium carbonate obtained by burning saltwort ashes, taken from Italian/Medieval Latin soda through the Mediterranean glass and soap trade; the 'carbonated water' sense is a nineteenth-century shortening of soda water (1802, so used by 1834). Sodium was coined by Humphry Davy in 1807 from soda + the element suffix -ium, after he isolated the metal by electrolysis of caustic soda; the symbol Na comes from Berzelius's rival natrium (from natron < Arabic naṭrūn). The arrow Latin → English is therefore correct as a matter of form and date — it is only the Arabic ancestry drawn above it (node 3) that is contested, which is why the node is plausible rather than confirmed.\",\n          \"derivation_fa\": \"واژهٔ soda در انگلیسی نخستین‌بار در اواخر سدهٔ پانزدهم میلادی برای کربنات سدیمِ به‌دست‌آمده از سوزاندن گیاهان شور ثبت شده و از راه بازرگانی شیشه و صابون مدیترانه از ایتالیایی/لاتین میانه گرفته شده است؛ معنای «آب گازدار» کوتاه‌شدهٔ soda water (۱۸۰۲م) است که از ۱۸۳۴م رواج یافت. واژهٔ sodium را همفری دیوی در ۱۸۰۷م از soda و پسوند عنصری -ium ساخت، پس از آنکه این فلز را با برق‌کافت سود سوزآور جدا کرد؛ نشانهٔ شیمیایی Na از نام رقیب، natrium برتسلیوس (از natron و آن از «نطرون» عربی) است. پس پیکان «لاتین ← انگلیسی» از نظر صورت و تاریخ درست است و تنها نیای عربیِ بالای آن (گرهٔ ۳) مورد اختلاف است؛ از این رو داوری «با احتیاط پذیرفتنی».\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/sodium\",\n            \"https://www.etymonline.com/word/soda\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai gives no reference for this node; checked against Etymonline, Klein and Skeat instead (see consulted).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt line 35794 s.v. soda ('Cp. sodalite, sodium')\",\n              \"stance\": \"supports\",\n              \"note\": \"Klein derives English soda straight from Medieval Latin and sodium from soda.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"SKT.txt line 17762 s.v. Soda\",\n              \"stance\": \"partial\",\n              \"note\": \"'Der. sod-ium, a coined [word]' — agrees that sodium is coined from soda, disagrees about where soda itself came from.\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"etymonline s.v. sodium\",\n              \"stance\": \"supports\",\n              \"note\": \"'Coined 1807 by English chemist Humphry Davy from soda + -ium … So called because the element was isolated from caustic soda (sodium hydroxide). The chemical symbol Na is from natrium.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"sodâ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian سودا 'soda water, carbonated water' is a twentieth-century European loan, and Moʿin marks its source precisely: 'سودا (سُ) [انگ.] (اِ.) آب دارای گاز کربنیک' — '[English]'. Nourai's arrow English → Persian is thus exactly right. It must be kept apart from two homographs that Moʿin lists in the same article and that have nothing to do with this chart: سودا [ع. سوداء] 'black bile, melancholy, obsession, love', the feminine of أسود 'black' and one of the four humours; and native Persian سودا 'trade, buying and selling' (whence سوداگر). The spelling is identical, the pronunciations (sudā / sowdā) and the histories are not — a good example of how a modern European loan can land on top of an old Arabic and an old Persian word.\",\n          \"derivation_fa\": \"«سودا» به معنی «آب گازدار» وام‌واژه‌ای اروپایی از سدهٔ بیستم است و معین سرچشمهٔ آن را دقیق نشان داده است: «سودا (سُ) [انگ.] (اِ.) آب دارای گاز کربنیک» — یعنی از انگلیسی. پس پیکان «انگلیسی ← فارسی» نورایی درست است. اما باید آن را از دو هم‌نویسه جدا کرد که معین در همان مدخل آورده و هیچ ربطی به این نمودار ندارند: «سودا» [ع. سوداء] به معنی «صفرای سیاه، مالیخولیا، شیدایی، عشق» که مؤنث «أسود» و یکی از اخلاط چهارگانه است؛ و «سودا»ی فارسی به معنی «داد و ستد» (که «سوداگر» از آن است). املا یکی است، ولی تلفظ و تاریخ این سه یکی نیست — نمونه‌ای خوب از اینکه چگونه یک وام‌واژهٔ نو اروپایی می‌تواند بر روی واژه‌ای عربی و واژه‌ای فارسی کهن بنشیند.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%B3%D9%88%D8%AF%D8%A7/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:1947\",\n              \"status\": \"supports\",\n              \"note\": \"Moʿin via abadis.ir: 'سودا (سُ) [انگ.] (اِ.) آب دارای گاز کربنیک' — the '[انگ.]' tag confirms Nourai's English source exactly. (The same article also gives '(سَ یا سُ) (اِ.) داد و ستد، خرید و فروش' and '(سَ یا سُ) [ع. سوداء] (ص.) … یکی از اخلاط اربعه … مالیخولیا'.) Page 1947 itself is not verifiable in the online Moʿin, which carries no pagination.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"abadis.ir/fatofa/سودا (فرهنگ معین)\",\n              \"stance\": \"supports\",\n              \"note\": \"'[انگ.] … آب دارای گاز کربنیک'.\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"etymonline s.v. soda\",\n              \"stance\": \"supports\",\n              \"note\": \"'Meaning \\\"carbonated water\\\" is first recorded 1834, a shortening of soda water (1802)' — the sense Persian borrowed.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"An empty pass-through box: Nourai draws it only to carry the line from Latin soda down to Persian سدیم. What it stands for is French soude 'soda, the alkali' (16th century, from Italian/Provençal soda, the same Mediterranean trade word) and, on top of it, the learned chemical term sodium, which French adopted from Davy's English coinage almost at once and which appears in French chemical writing from the 1810s. The box is thus historically justified — French really is the language through which the chemical name reached Persian, as Moʿin's '[فر.]' tag on سدیم independently shows — but it records no French form of its own, so it cannot be verified as printed.\",\n          \"derivation_fa\": \"این خانه تهی است و نورایی آن را تنها برای کشیدن خط از soda لاتین به «سدیم» فارسی گذاشته است. آنچه این خانه نمایندهٔ آن است، واژهٔ soude فرانسوی «قلیا، سود» (از سدهٔ شانزدهم، از ایتالیایی/پروانسی soda، همان واژهٔ بازرگانی مدیترانه‌ای) و بر روی آن اصطلاح شیمیایی sodium است که فرانسه بی‌درنگ از ساختهٔ دیویِ انگلیسی گرفت و از دههٔ ۱۸۱۰م در متون شیمی فرانسوی دیده می‌شود. پس این خانه از نظر تاریخی موجه است — فرانسه به‌راستی زبان میانجی رسیدن این نام به فارسی است، چنان‌که نشان «[فر.]» معین در مدخل «سدیم» مستقلاً گواهی می‌دهد — ولی چون هیچ صورت فرانسوی در آن چاپ نشده، به همان شکل چاپی وارسی‌پذیر نیست.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%B3%D8%AF%DB%8C%D9%85/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The box carries no word and no reference; its justification is Moʿin's '[فر.]' tag on the Persian derivative (node 7).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"abadis.ir/fatofa/سدیم (فرهنگ معین)\",\n              \"stance\": \"supports\",\n              \"note\": \"'سدیم (سُ یُ) [فر.] (اِ.)' — Moʿin's French tag confirms that French is the transmitting language Nourai's empty box stands for.\"\n            },\n            {\n              \"src\": \"DEV\",\n              \"where\": \"Devic, s.v. Soda (DEV.txt line 2133) and index line 4330\",\n              \"stance\": \"partial\",\n              \"note\": \"Devic treats French soda only as the medical term; he has no entry for soude or sodium, so he neither supports nor contradicts the chemical line.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"sodyom\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian سدیم sodyom is a twentieth-century scientific loan from French sodium, taken over with the French pronunciation [sɔdjɔm] — hence the -yom ending, which is Persian's regular treatment of French -ium in chemical names (کلسیم kalsiyom, پتاسیم potâsiyom, اورانیوم urâniyom), quite different from the English -ium. Moʿin tags the word '[فر.]' and defines it 'فلزی است نقره‌ای، دارای جلای فلزی ولی در مجاورت اکسیژن خیلی زود کدر می‌گردد و آن چنان نرم است که با چاقو به آسانی بریده می‌شود و از آب سبک‌تر است'. The arrow French → Persian is exactly right, and سدیم and سودا (node 5) are doublets in Persian, the one through French and the other through English.\",\n          \"derivation_fa\": \"«سدیم» وام‌واژه‌ای علمی از سدهٔ بیستم است که از فرانسوی sodium و با تلفظ فرانسوی [sɔdjɔm] گرفته شده؛ پایانهٔ «-یم/-یوم» همان شیوهٔ همیشگی فارسی در برابر -ium فرانسوی در نام عنصرهاست (کلسیم، پتاسیم، اورانیوم) و با تلفظ انگلیسی آن یکی نیست. معین این واژه را با نشان [فر.] آورده و چنین تعریف کرده است: «فلزی است نقره‌ای، دارای جلای فلزی ولی در مجاورت اکسیژن خیلی زود کدر می‌گردد و آن چنان نرم است که با چاقو به آسانی بریده می‌شود و از آب سبک‌تر است». پس پیکان «فرانسوی ← فارسی» درست است و «سدیم» و «سودا» (گرهٔ ۵) در فارسی دوگانه (doublet) اند: یکی از راه فرانسه و دیگری از راه انگلیسی.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%B3%D8%AF%DB%8C%D9%85/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:1847\",\n              \"status\": \"supports\",\n              \"note\": \"Moʿin via abadis.ir: 'سدیم (سُ یُ) [فر.] (اِ.) فلزی است نقره‌ای، دارای جلای فلزی … و از آب سبک‌تر است.' The '[فر.]' tag confirms the French source Nourai's chart draws; the printed page 1847 is not verifiable in the online Moʿin.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"abadis.ir/fatofa/سدیم (فرهنگ معین)\",\n              \"stance\": \"supports\",\n              \"note\": \"'[فر.]' — French.\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"etymonline s.v. sodium\",\n              \"stance\": \"supports\",\n              \"note\": \"'Coined 1807 by English chemist Humphry Davy from soda + -ium' — the term French then passed on to Persian.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-14T01:41:11.666Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-433.json (file state is current in your context — no need to Read it back)
```


## [2026-09-14T01:41:15.377Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-433.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 433",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-14T01:41:16.717Z] TOOL RESULT

```
JSON OK
nodes verified: 18/18
node verdicts: {'transcription_suspect': 1, 'disputed': 5, 'confirmed': 8, 'plausible': 4}
root verdicts: {'confirmed': 3}
ref checks: {'partial': 2, 'supports': 11, 'not_checked': 8}
books consulted: {'partial': 7, 'contradicts': 7, 'silent': 7, 'supports': 21} | by book: {'KLN': 7, 'MON': 6, 'WEB': 6, 'POK': 4, 'WLD': 4, 'AHD': 4, 'SKT': 3, 'DEV': 3, 'BQT': 2, 'HRN': 1, 'HUB': 1, 'LKT': 1}
```


## [2026-09-14T01:41:35.993Z] AGENT

Done. `verify_check.py 433` reports 0 PROBLEM lines (18/18 nodes).

**Page 433 (book p. 403) — 3 entries, 18 nodes**

Verdicts: roots 3 confirmed; nodes 8 confirmed, 4 plausible, 5 disputed, 1 transcription_suspect.

Disputed / flagged:
- **Sâwel / Greek "alos"** (node 1) — `transcription_suspect`, error_in **book**: the printed page really reads "alos, helios : sun". No Greek "alos" exists; the sun-word is Doric hālios (ᾱ̔́λιος), while the word the chart actually needs for hāleh is ἅλως *hálōs* "disk, halo", which Klein calls "of uncertain origin" and Wiktionary/Beekes assign to Pre-Greek — i.e. not from *sāwel-. Page PNG saved to `data/verification/sources/refs/ocr/BOOK/433.png`.
- **Sâwel / Persian هاله hâleh** — disputed: real chain is Gk ἅλως → Arabic هالة → NP هاله (Wiktionary); not from ἥλιος, and the Arabic mediation (documented by Nourai's own TAD:75) is omitted.
- **Sâwel / English Helen, Aileen** — disputed: Aileen is a variant of Eileen < Irish Eibhlín < Anglo-Norman Aveline; the Helen equation is a later sound-alike association (Behind the Name).
- **Šay' / Spanish X** and **English X, x-ray** — disputed: OED ("no evidence … that x is derived ultimately from the mediaeval transliteration xei of shei") and Cajori attribute x/y/z to Descartes, *Géométrie* 1637. Klein (KLN:1756) does say what Nourai says; it is the outdated lexicographers' story. The x-ray half is fine (Röntgen's X-Strahlen, Dec 1895).
- **S.d.a` / Latin soda, sodanum** — disputed: medical Latin *soda* "headache" < Arabic ṣudāʿ is genuine (Devic p.210), but the alkali *soda* (ancestor of soda/sodium) comes from the saltwort plant name (Wiktionary: Ital. soda < Arab. سُوَيْداء; Etymonline calls the ṣudāʿ route "far-fetched"; Skeat: Ital. sodo < L. solidus). Nourai, following Klein, merges two words.

Confirmed highlights: POK:881 and POK:1045 both check out verbatim; helium (Klein: Lockyer & Frankland 1868); swelter < OE sweltan; Persian صداع [ع.], سودا [انگ.], سدیم [فر.] all match Moʿin's own origin tags exactly.

Reference-page caveat (not an extraction error): **KLN:1468** — Klein's *soda* entry says precisely what Nourai claims, but in the archive.org scan of the 1966 two-volume edition it sits at printed p. ≈ 1531 (leaf 779), not 1468; recorded as `partial`. Not checkable at all: SAP:857, PRT:813, FVA:223 (no digital copies), AHD:611 (lending-only) — and note that the Watkins IE appendix, which *is* on disk, puts Helenē under *wel-³*, not swel-2, contradicting Nourai's AHD citation.

**No extraction errors found** — the JSON matches the printed page throughout, including "alos" and "swiltan".
