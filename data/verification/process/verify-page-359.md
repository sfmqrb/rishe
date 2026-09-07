# Verification process log — verify-page-359


## [2026-09-07T19:28:58.597Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 359 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-359.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-359.json. Write /home/sfmqrb/git/rishe/data/verification/page-359.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 359` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T19:29:00.831Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T19:29:01.553Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T19:29:01.635Z] TOOL RESULT

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


## [2026-09-07T19:29:02.167Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-359.txt"
}
```


### [2026-09-07T19:29:02.191Z] TOOL RESULT

```
1	=== PDF page 359 (book page 329) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Nem 1 : to assign, take  (refs POK:763)
4	#1 (parent #0) [Avestan] refs=POK:763; KLN:1048 | nemah 1 : loan, what is given back, a prayer
5	  #2 (parent #1) [Pahlavi] refs=BRT:1070 | namač : prayer | NOTE: BQT:2167, POK:764 and SYN:544 derive this word from Old Persian "nam: to bow in respect". See "Nem 2"
6	    #3 (parent #2) [Persian] refs=BQT:1070 | namâz «نماز» : prayer
7	#4 (parent #0) [Greek] refs=AHD | nomos : law
8	  #5 (parent #4) [Arabic] refs=BQT:2106; MON:4629 | nâmŭs : law, rules
9	    #6 (parent #5) [Persian] refs=None | nâmŭs «ناموس» : rules, dignity, family
10	  #7 (parent #4) [English] refs=AHD | -nomy, economy, astronomy
11	#8 (parent #0) [Latin] refs=AHD | numerus : a portion, a number
12	  #9 (parent #8) [Italian] refs=None | numero
13	    #10 (parent #9) [Arabic] refs=MON:4815 | nomreh
14	      #11 (parent #10) [Persian] refs=MON:4815 | nomreh «نمره» : number | extra: نمرات
15	  #12 (parent #8) [French] refs=AHD | nombre
16	    #13 (parent #12) [English] refs=AHD | number, numerous
17	#14 (parent #0) [Different Languages] refs=AHD | 
18	  #15 (parent #14) [English] refs=AHD | numb, nomad
19	--- entry 1 ---
20	ROOT [Indo-European] Nem 2 : to bend, bow in respect, also brush wood and twigs  (refs POK:764)
21	#1 (parent #0) [Avestan / Old Persian] refs=POK:764; WLD2:234; SYN:544 | nam : to bend, bow ; nemah 2 : bowing in respect ; namaiti : bends ; fra-namaiti, apa-namaiti ; nemata 1 : twigs
22	  #2 (parent #1) [Pahlavi] refs=BQT:2167 | namâč : bowing, prayer | NOTE: BRT:1070 derives it from Avestan "nemah: what one owes." See root "Nem 1".
23	    #3 (parent #2) [Persian] refs=BQT:2167; FSF:328 | namâz «نماز» : prayer
24	--- entry 2 ---
25	ROOT [Avestan] Nemata 2, Nimatâ : straw, grass  (refs NYB:135)
26	#1 (parent #0) [Pahlavi] refs=NYB:135; HRN:233 | namat : felt rug or cloth
27	  #2 (parent #1) [Persian] refs=BQT:2169; KLN:1026 | namad «نمد» : a thick felt cloth
28	#3 (parent #0) [Sogdian] refs=SOD:240 | nmt : felt
29	
```


## [2026-09-07T19:29:06.057Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-359.json",
 "description": "Read source JSON for page 359"
}
```


### [2026-09-07T19:29:06.103Z] TOOL RESULT

```
{
  "pdf_page": 359,
  "book_page": 329,
  "entries": [
    {
      "root": {
        "name": "Nem 1",
        "lang": "Indo-European",
        "refs": "POK:763",
        "gloss": "to assign, take"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:763; KLN:1048",
          "words": [
            {"translit": "nemah 1", "gloss": "loan, what is given back, a prayer", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BRT:1070",
          "words": [
            {"translit": "namač", "gloss": "prayer", "script": null}
          ],
          "script_extra": null,
          "note": "BQT:2167, POK:764 and SYN:544 derive this word from Old Persian \"nam: to bow in respect\". See \"Nem 2\"",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1070",
          "words": [
            {"translit": "namâz", "gloss": "prayer", "script": "نماز"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "چو نزدیک رستم فراز آمدند - پیاده به رسم نماز آمدند", "poet": "Ferdowsî"}
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "nomos", "gloss": "law", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Arabic",
          "refs": "BQT:2106; MON:4629",
          "words": [
            {"translit": "nâmŭs", "gloss": "law, rules", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "nâmŭs", "gloss": "rules, dignity, family", "script": "ناموس"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "-nomy, economy, astronomy", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "numerus", "gloss": "a portion, a number", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Italian",
          "refs": null,
          "words": [
            {"translit": "numero", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Arabic",
          "refs": "MON:4815",
          "words": [
            {"translit": "nomreh", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON:4815",
          "words": [
            {"translit": "nomreh", "gloss": "number", "script": "نمره"}
          ],
          "script_extra": "نمرات",
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 8,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {"translit": "nombre", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "number, numerous", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Different Languages",
          "refs": "AHD",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "numb, nomad", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Nem 2",
        "lang": "Indo-European",
        "refs": "POK:764",
        "gloss": "to bend, bow in respect, also brush wood and twigs"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:764; WLD2:234; SYN:544",
          "words": [
            {"translit": "nam", "gloss": "to bend, bow", "script": null},
            {"translit": "nemah 2", "gloss": "bowing in respect", "script": null},
            {"translit": "namaiti", "gloss": "bends", "script": null},
            {"translit": "fra-namaiti, apa-namaiti", "gloss": null, "script": null},
            {"translit": "nemata 1", "gloss": "twigs", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:2167",
          "words": [
            {"translit": "namâč", "gloss": "bowing, prayer", "script": null}
          ],
          "script_extra": null,
          "note": "BRT:1070 derives it from Avestan \"nemah: what one owes.\" See root \"Nem 1\".",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:2167; FSF:328",
          "words": [
            {"translit": "namâz", "gloss": "prayer", "script": "نماز"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "چو نزدیک رستم فراز آمدند - پیاده به رسم نماز آمدند", "poet": "Ferdowsî"}
        }
      ]
    },
    {
      "root": {
        "name": "Nemata 2, Nimatâ",
        "lang": "Avestan",
        "refs": "NYB:135",
        "gloss": "straw, grass"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "NYB:135; HRN:233",
          "words": [
            {"translit": "namat", "gloss": "felt rug or cloth", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2169; KLN:1026",
          "words": [
            {"translit": "namad", "gloss": "a thick felt cloth", "script": "نمد"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:240",
          "words": [
            {"translit": "nmt", "gloss": "felt", "script": null}
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


## [2026-09-07T19:29:07.168Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50; echo ---; cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-07T19:29:07.221Z] TOOL RESULT

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


## [2026-09-07T19:29:40.555Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','BRT','NYB','HRN','SOD','BQT','MON','KLN','SYN','WLD','WLD2','AHD','FSF','PHD','FVQ','PLA','AFM','SKT','LKT','IEC','HUB','LEW','LAT','ARY']:\n  v=d.get(k)\n  if not v: print(k,'MISSING'); continue\n  print('==',k, json.dumps({kk:v.get(kk) for kk in ('kind','url','local_file','page_offset','lookup_hint','scans','note') if v.get(kk) is not None}, ensure_ascii=False)[:900])\n\""
}
```


## [2026-09-07T19:29:41.319Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,60p' data/verification/page-317.json; echo ====; sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-07T19:29:41.852Z] TOOL RESULT

```
== POK {"kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbe
== BRT {"kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops."}
== NYB {"kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs."}
== HRN {"kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann."}
== SOD {"kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"], "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/me
== BQT {"kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login o
== MON {"kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"], "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (F
== KLN {"kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."}
== SYN {"kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line."}
== WLD {"kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf", "/home/sfmqrb/git/rishe/data/veri
WLD2 MISSING
== AHD {"kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word p
== FSF {"kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه)."}
== PHD {"kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB)."}
== FVQ {"kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296)."}
== PLA {"kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "scans": [{"file": "/home/sfmqrb/gi
== AFM {"kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير')."}
== SKT {"kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags."}
== LKT {"kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number."}
== IEC {"kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root."}
== HUB {"kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number."}
== LEW {"kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal."}
== LAT {"kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'."}
== ARY {"kind": "local_scan_ocr", "url": "", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "scans": [{"file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf", "first_printed": 1, "last_printed": 546, "pdf_offset": -1, "lang": "fas+eng", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources
```


### [2026-09-07T19:29:41.901Z] TOOL RESULT

```
Exit code 1
{
  "pdf_page": 317,
  "book_page": 287,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-06",
  "entries": [
    {
      "entry": 0,
      "root": "Mad",
      "verdict": "confirmed",
      "modern_form": "PIE *mad- (laryngealist *meh₂d-) 'wet, dripping; fat, well-fed', with the derived sense 'food, fattening' — Pokorny 694-695",
      "note": "The root is genuine and standard. Pokorny 694-695 has 'Root/lemma: mad-  Meaning: wet; glossy, fat, well-fed, intoxicating', and Watkins/AHD (1985 ed., p. 38) has 'mad-. Moist, wet; also refers to various qualities of food' — Nourai's gloss 'wet, also food' is essentially Watkins' wording, and the language label 'Indo-European' is right. Walde-Pokorny II 230-232 is the same article. What is remarkable is that Pokorny's article contains almost the whole of Nourai's chart in the same order: 'ai. madati, madate … mada- m. Rauschtrank = av. maδa-; ai. madgu- ein bestimmter Wasservogel, ein Fisch = np. māγ ein Wasservogel; ai. matsya- m., av. masya Fisch (der nasse; Ableitung von einem -es-St. *mades-); mastu- n. saurer Rahm (*mad-stu-) … arm. macun sauer, geronnene Milch … iran. Worte für Dickmilch, so npers. mast, masīdan … lat. madeō, mattus trunken (*madi-to-s) … ahd. mast Futter, got. mats Speise, ags. mete, mnd. mat(e) Kamerad'. Two modern caveats: (a) Cheung (2007) and LIV split the family into *mad¹ 'to become intoxicated' (PIE *med-) and a separate Indo-Iranian *mad 'to curdle', for which no PIE root is set up; (b) the 'fish' member is no longer taken as certain (see node #1).",
      "note_fa": "ریشهٔ هندواروپایی آغازین *mad- (در نگارش امروزی *meh₂d-) به معنی «خیس، تر، چکه‌کننده؛ فربه و پرورده» و از همین‌جا «خوراک»، ریشه‌ای شناخته و پذیرفته است: پوکورنی (ص ۶۹۴–۶۹۵) آن را با معنی «تر؛ چرب، فربه، مست‌کننده» می‌آورد و واتکینز در پیوست فرهنگ American Heritage نیز «mad-. نمناک، تر؛ همچنین دربارهٔ کیفیت‌های خوراک» دارد؛ پس برچسب زبانی و معنای «wet, also food» در نمودار نورایی درست است. نکتهٔ چشمگیر آنکه تقریباً همهٔ شاخه‌های نمودار — سنسکریت madati و mada-، اوستایی maδa-، سنسکریت madgu- برابر «ماغ» فارسی، سنسکریت mastu- و ارمنی macun برابر «ماست» و «ماسیدن»، لاتینی mattus و واژه‌های ژرمنی mast/mats/mete/mate — همه در همان مقالهٔ پوکورنی و به همان ترتیب آمده‌اند، یعنی نورایی مستقیماً از پوکورنی و واتکینز برداشته است. دو نکتهٔ احتیاطی: نخست آنکه چونگ (۲۰۰۷) و فرهنگ LIV دو ریشهٔ *mad «مست شدن» و *mad «بستن، دلمه شدن» را از هم جدا می‌کنند و برای دومی ریشهٔ هندواروپایی نمی‌سازند؛ دوم آنکه پیوند واژهٔ «ماهی» با این ریشه امروز قطعی دانسته نمی‌شود (بنگرید به گرهٔ ۱).",
      "sources": [
        "https://en.wiktionary.org/wiki/mattus",
        "https://en.wiktionary.org/wiki/meat"
      ],
      "ref_check": [
        {"ref": "POK:694", "status": "supports", "note": "POK_full.txt line 57036 ff. (= POK_02.txt line 5645 ff., German original): 'Root/lemma: mad-  Meaning: wet; glossy, fat, well-fed, intoxicating … References: WP. II 231 f., WH. II 6 f.  Page(s): 694-695'. The page number Nourai cites is exactly right, and the article's material list is the source of his whole chart."}
      ],
      "consulted": [
        {"src": "WLD", "where": "Bd. II 230-232 s.v. 'mad-'", "stance": "supports", "note": "incoming/WLD/WLD_Bd2_pages.txt line 15104: 'weitere iran. Worte für Dickmilch u. dgl., so np. mast \"saure Milch\", masī[dan]' — the article Pokorny cites as WP. II 231 f., same members."},
        {"src": "AHD", "where": "Watkins 1985 p. 38 (AHD_watkins1985.txt line 708) s.v. mad-", "stance": "supports", "note": "'mad-. Moist, wet; also refers to various qualities of food. 1. Sanskrit madati, \"it gladdens, it bubbles,\" hence madana-, delightful, joyful, hence madanah, a myna bird: MYNA. 2. Suffixed form *mad-i- in Germanic *mati- in: a. Old English mete, food: MEAT; b. Middle Low German (ge)mate … MATE. 3. Suffixed form *mad-sto- … Old English mest, fodder: MAST. [Pok. mad- 694.]'"},
        {"src": "IEC", "where": "Mann, leaves 553-556: 'mad- (1) feed; food', 'mad- (3) get wet; be wet', 'madtós (maditós, mastos)'", "stance": "partial", "note": "IEC.txt lines 10227, 10237, 10239: Mann splits the family into three lemmas — 'mad- (1) \"feed; food\". WP II, 232 …', 'mad- (3) … \"get wet; be wet\". WP II, 230  Skt. mádāmi, pp. mattáh \"get drunk\"; Lat. madeó …', and 'madtós … \"fed, fattened; food, fattening\" … Skt. cf. mástu, n. \"sour cream, whey\" … Per. māst \"sour milk\"' — the same words, but no single root box."},
        {"src": "SYN", "where": "Buck ch. 3.65 'Fish', p. 184 (SYN.txt line 4927)", "stance": "partial", "note": "'Skt. matsya-, Av. masya-, fr. an IE *mad- \"be wet\" in Grk. madáō, Lat. madēre, etc.? Walde-P. 2.230.' — Buck knows the root but puts a question mark on the fish member."},
        {"src": "CHEUNG", "where": "pp. 253-254, s.v. *mad¹ and *mad", "stance": "partial", "note": "CHEUNG.txt line 16801: '*mad¹ \"to become intoxicated, joyous\" … «PIE *med- … = LIV: 423 f. | Pok.: 694 f.'; line 16828: '*mad \"to curdle, coagulate\" 

... [2993 characters truncated] ...

as",
            "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%87%DB%8C"
          ],
          "ref_check": [
            {"ref": "POK:694", "status": "supports", "note": "POK_02.txt line 5647: 'ai. madgu- \"ein bestimmter Wasservogel, ein Fisch\" = np. māγ \"ein Wasservogel\", ai. mātsya- m., av. masya \"Fisch\" (\"der nasse\"; Ableitung von einem -es-St. *mades-)' and 'av. maδa- \"Rauschtrank, Rauschbegeisterung\"' — all three of Nourai's items, but the bird is Sanskrit/Persian, not Avestan."},
            {"ref": "SYN:184", "status": "supports", "note": "SYN.txt line 4919 ff.: page 184 is Buck's ch. '3.65 FISH', whose table lists 'Skt. matsya- / Av. masya-' and whose note 5 (line 4927) reads 'Skt. matsya-, Av. masya-, fr. an IE *mad- \"be wet\" in Grk. madáō, Lat. madēre, etc.? Walde-P. 2.230.' Nourai's page is right; the question mark is his to answer."}
          ],
          "consulted": [
            {"src": "BRT", "where": "AiW col. 1112 s.v. maδa- (BRT.txt line 19595); no bird lemma 'mad-'", "stance": "partial", "note": "'g. *mada-, j. maδa- m. 1) \"Rauschbegeisterung\" durch Haoma-Genuss … Ableit. — Zum V. maδ-. — ai. mada- m., np. mai.' Bartholomae has maδa- and the verb maδ-, and masiia- 'Fisch', but no Avestan water-bird word — confirming that Nourai's third item is misplaced."},
            {"src": "CHEUNG", "where": "p. 253 s.v. *mad¹", "stance": "supports", "note": "'*AVESTAN: Y Av. maδ- \"to become intoxicated, joyous\" — Liste: 42 … *SANSKRIT: mad \"to become exhilarated, intoxicated\" (RV+) = EWAia II: 299' — the Avestan verb and its Indic cognate as Nourai draws them."},
            {"src": "HUB", "where": "Persische Studien § 94, p. 101 (HUB.txt line 7170)", "stance": "supports", "note": "'§ 94. Ap. d vor y, m, n ist geschwunden: māγ \"ein Wasservogel\", skr. madgu-, ap. *maδgu-?' — Hübschmann derives the bird from an Old Persian, not Avestan, form."},
            {"src": "IEC", "where": "Mann, s.v. 'mesgus, os \"diving bird\"' (IEC.txt line 10687)", "stance": "contradicts", "note": "'mesgus, os \"diving bird\". Cf. mesgó (2). (mezg-)  Skt. madguḥ, m. id.; Lat. mergus, m., LLat. mergulus \"cormorant\"' — Mann assigns the water-bird word to *mezg- 'to dive' (Lat. mergus), not to *mad-."}
          ]
        },
        {
          "id": 2,
          "lang": "Persian",
          "words": "mâhî «ماهی» : fish; mast «مست ۱» : drunk; mâğ «ماغ» : a black water bird, mina",
          "verdict": "plausible",
          "derivation": "All three Persian words are real and the two central ones are textbook cases. ماهی māhī 'fish' < Middle Persian māhīg [m'hyk] (MacKenzie, CPD p. 54 'mahig … fish; astr. Pisces') < Proto-Iranian *mácyah < PII *mátsyas, cognate with Av. masiia-, Skt. mátsya-; the MP -g of māhīg is regularly lost in New Persian (cf. MP xānag > NP xāna). مست mast 'drunk' < MP mast [mst] 'bemused, intoxicated' (MacKenzie p. 54; Manichaean MP/Parthian mst, Cheung *mad¹), from Old Iranian *mad-ta-, the participle of maδ- — the Old Iranian cluster -dt- gives -st- (cf. *basta- > baste), exactly parallel to Skt. matta- and to Lat. mattus < *maditus in node #10. ماغ māγ 'a black water bird' is attested from the 10th c. (Loghat-e Fors, printed p. 235 of the Eqbal ed., quotes Daqīqī 'مرغی باشد سیاه فام و بیشتر در آب نشیند'), and Pokorny 694, Horn no. 961 and Hübschmann § 94 all equate it with Skt. madgu-, Hübschmann positing an Old Persian *maδgu- with loss of δ before g/m; that is Nourai's arrow, but Mann (IEC, s.v. mesgus) instead puts Skt. madgú- with Lat. mergus under *mezg- 'to dive', so the last word is only plausible. The Rudakī line in the chart is the verse Borhān-e Qāteʿ quotes for ماغ (Mo'in's edition attributes it to Daqīqī, not Rudakī).",
          "derivation_fa": "هر سه واژهٔ این جعبه فارسی راستین‌اند و دو تای نخست از نمونه‌های درسی‌اند. «ماهی» از فارسی میانهٔ māhīg (مکنزی، فرهنگ کوچک پهلوی ص ۵۴: mahig «ماهی») و آن از ایرانی باستان *mácyah و هندوایرانی *mátsyas، هم‌ریشه با اوستایی masiia- و سنسکریت mátsya-؛ ‎-g‎ پایانی فارسی میانه در فارسی نو به‌قاعده افتاده است (مانند xānag > خانه). «مست» از فارسی میانهٔ mast (مکنزی؛ مانوی و پارتی mst)، از ایرانی باستان *mad-ta-، صفت مفعولی ستاک maδ-؛ خوشهٔ ‎-dt-‎ ایرانی باستان به ‎-st-‎ بدل می‌شود (مانند *basta- > بسته)، درست همانند matta- سنسکریت و mattus لاتینی (گرهٔ ۱۰). «ماغ» از سدهٔ چهارم گواهی دارد (لغت فرس، ص ۲۳۵ چاپ اقبال، از دقیقی: «مرغی باشد سیاه فام و بیشتر در آب نشیند») و پوکورنی (۶۹۴)، هرن (شمارهٔ ۹۶۱) و هوبشمان (بند ۹۴) هر سه آن را برابر madgu- سنسکریت می‌دانند و هوبشمان صورت پارسی باستان *maδgu- را با افتادن ذ فرض می‌کند؛ ولی مان واژهٔ سنسکریت را با mergus لاتینی زیر ریشهٔ *mezg- «شنا رفتن، فرو رفتن» می‌گذارد، پس این یکی تنها پذیرفتنی‌است نه قطعی. بیتِ نمودار همان بیتی است که برهان قاطع ذیل «ماغ» آورده و در چاپ معین به دقیقی نسبت داده شده، نه رودکی.",
          "sources": [
            "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%87%DB%8C",
            "https://en.wiktionary.org/wiki/%D9%85%D8%B3%D8%AA"
(eval):1: === not found
```


## [2026-09-07T19:29:45.337Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-07T19:29:45.392Z] TOOL RESULT

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


## [2026-09-07T19:29:52.833Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full lemma nem\"; grep -n -i \"lemma: nem\" POK_full.txt | head -20\necho \"=== POK_02 around nem\"; grep -n \"^nem-\" POK_02.txt POK_01.txt POK_03.txt | head -20"
}
```


### [2026-09-07T19:29:52.897Z] TOOL RESULT

```
=== POK_full lemma nem
62524:Root / lemma: nem-1 {*he- nem-f) 
62530:Root/ lemma: nem-1 {* he- nem-1)\ to take; to put in order, count, curse, bad name, 
62575:Root / lemma: nem-2 {* he- nem-2) 
=== POK_02 around nem
```


## [2026-09-07T19:29:53.789Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD nem\"; grep -n -i \"^nem-\\|nem-1\\|nem-2\" AHD_watkins1985.txt | head -20\necho \"=== AHD numb/nomad context\"; grep -n \"NOMAD\\|NUMB\\b\" AHD_watkins1985.txt | head"
}
```


### [2026-09-07T19:29:53.856Z] TOOL RESULT

```
=== AHD nem
780:nem-. To assign, allot; also to take. 1. Germanic *nem- in: a. Old English niman, to take, seize: NIM, NUMB; (BENUMB); b. Old English n#mel, quick to seize, and numol, quick at learning, seizing: NIMBLE. 2. Greek nemein, to allot: NEMESIS. 3. O-grade form *nom- in: a. Greek nomos, portion, usage, custom, law, division, district: NOME, -NOMY; ANOMIE, ANTINOMIAN, AN- TINOMY, (ASTRONOMER), (ASTRONOMY), AUTONOMOUS, BINOMIAL, DEUTERONOMY, METRONOME, NOMOGRAM, NOMOGRAPH, NUMISMATICS; b. Greek nomé, pasturage, grazing, hence a spreading, a spreading ulcer: NOMA; c. Greek nomas, wandering in search of pasture: NOMAD; d. Greek nomimos, legal, probably borrowed in Latin nummus, coin: NUMMULAR, NUMMULATE. 4, Perhaps suffixed o-grade form *nom-eso- in Latin numerus, num- ber, division: NUMBER; ENUMERATE, SUPERNUMERARY. [Pok. 1. nem- 763.]
=== AHD numb/nomad context
780:nem-. To assign, allot; also to take. 1. Germanic *nem- in: a. Old English niman, to take, seize: NIM, NUMB; (BENUMB); b. Old English n#mel, quick to seize, and numol, quick at learning, seizing: NIMBLE. 2. Greek nemein, to allot: NEMESIS. 3. O-grade form *nom- in: a. Greek nomos, portion, usage, custom, law, division, district: NOME, -NOMY; ANOMIE, ANTINOMIAN, AN- TINOMY, (ASTRONOMER), (ASTRONOMY), AUTONOMOUS, BINOMIAL, DEUTERONOMY, METRONOME, NOMOGRAM, NOMOGRAPH, NUMISMATICS; b. Greek nomé, pasturage, grazing, hence a spreading, a spreading ulcer: NOMA; c. Greek nomas, wandering in search of pasture: NOMAD; d. Greek nomimos, legal, probably borrowed in Latin nummus, coin: NUMMULAR, NUMMULATE. 4, Perhaps suffixed o-grade form *nom-eso- in Latin numerus, num- ber, division: NUMBER; ENUMERATE, SUPERNUMERARY. [Pok. 1. nem- 763.]
1294:BENIGN deu-?, gene- BENTHOS gWadh- BENUMB nem- BEQUEATH gWet-2 BEQUEST gWet-2 BEREAVE reup- BERM bhrem-2 BERRY bha-1 BERSERKER bher-3 BESPEAK spreg- BESPRENT spergh- BEsT bhad- BETOKEN deik- BETRAY d6- BETROTH deru BETTER bhad- BETWEEN dwo- BETWIXT dwo- BEVEL bat- BEVERAGE pO(i)- BEWITCH weik-2 BEZOAR gWhen-1, pa- BHAGAVAD-GITA g@i-2 BI- dwo-
1930:NODE ned- NODULE ned- NODUS ned- NOEL gene- NOESIS nous NOISE nau-2 NOISOME od-2 NOMA nem- NOMAD nem- NOMBRIL nobh- NOME nem- ie NOMENCLATOR kela-2, no-men- NOMINAL no-men- NOMINATE no-men- NOMOGRAM nem- NOMOGRAPH nem-
1945:NULLIFY dhé-1, ne NULLIPARA ne NUMB nem- NUMBER nem- NUMEN neu-2 NUMISMATICS nem- NUMMULAR nem- NUMMULATE nem- NUN! nana
```


## [2026-09-07T19:29:57.051Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '62520,62620p' POK_full.txt"
}
```


### [2026-09-07T19:29:57.095Z] TOOL RESULT

```
References: WP. II 320 f., Schwyzer Gr. Gr. 1 , 600 f. 
Page(s): 758 

Root / lemma: nem-1 {*he- nem-f) 

Meaning: to take; to put in order, count, curse, bad name 

Note: 

Root/ lemma: nem-1 {* he- nem-1)\ to take; to put in order, count, curse, bad name, 

derived from a zero grade of Root/ lemma: en(o)mQ-, (o)nomQ, nomij'. name. 

Material: Avestan nsmah-u. "loan"; 

Maybe alb. Geg nem, Tosc nem^ give' imperative. 

gr. v£|j(jL) divide from, allow weiden ; later control, rule, Med. telle mirto, devour, weide , 
Herod. ava-vspsaOai 'allot, aufrechnen', vopn "distribution; meadowland ', vopat;, -ixboo, 



weioena^ne^mo^wanaenn^^oiJeu^TerasmE^ 

Wohnsitz', v6no(; " alignment, order', vopi^w 'see, observe as geltend an', vopiapa ' 
custom, custom, Einrichtung, gebrauchliche Geldwahrung'; lengthened grade vajpaw 
'divide to'; vt[izo\q "Unwille, gottliche revenge, vengeance ' (*v£tJ£Ti(;, actually "das 
Zurechnen'), v£|j£a(a)au), -aopai, -i^opai 'be angry with, rebuke, reproach', v£fj£TCL)p " 
avenger'; alb. name, neme'curse, oath, malediction, imprecation', formal = v6|J0(;; nemes 
" cursor, blasphemer, one who blasphemes '; here also Old Irish namae. Gen. nama/tl\end'7 

That \/t[ioq n. " meadowland ' here belongs, is not totally certain; see below nem-2, 

Latin /7i//77e/Y/s 'number' {*nomes-o-), nummus^ currency, coin' (from gr. v6piiJ0(; ' 
allowed, legitimate, lawful, ordinary '); 

Old Irish nemt, Middle Irish ne/'m' give ' (compare Modern High German G/ff: geben 
■give'); 

Gothic Old Saxon Old English niman. Old High German neman. Old Icelandic nema 
'take'; 

lengthened grade Gothic anda-nemr\. "reception'. Old High German nama^ forcible 
receiving, robbery '; Old English namt ' the griping ' from Old Icelandic namm. 'the 
receiving, learning '; Gothic 5/7o'a-/7e/77s' pleasant'. Old High German /7a/77/ "suitable, 
appropriate, acceptable '; Latvian >r7e/77/ (contaminated from nemt av\6 jemt) " take '; Lithuanian 
namas, mostly PI. /7a/775r dwelling, house', Latvian namsm. 'house'; ablaut. Lithuanian 
dial, numaf dwelling, house ' {*nom-)\ Lithuanian nuoma, Latvian nudma, 'interest, rental ' 
(vowel gradation as gr. vwijaw). 

References: WP. II 330 f., WH. II 158 f., Trautmann 193, 201, E. Laroche, La racine v£m-; 
E. Benveniste BSL. 32, 79 ff. 
Page(s): 763-764 

Root / lemma: nem-2 {* he- nem-2) 

Meaning: to bend 

Material: Old Indie namas- v\. = Avestan nemah-n. ' bowing, bending = worship, 

veneration, grace'. Old Indie namat/' bows, leans, bends' (Kaus. namayati), Avestan namaiti^ 

bends ' {namaiti, Kaus. namayeiti), with apa-, /^5- 'escape, flee'; participle Old Indie nata-^ 

bent, curved '; 



gr. vt[ioq n. " meadowland ' = Latin nemus, -oris' grove ', etc.; gall. v£pr|Tov ' sacred 
grove ', PN Nemeto-briga, VN Nemetes, Old Irish nemed' shrine ', then "privilege, privileged 
person'; asachs. nimidas' sacra silvarum '; Lithuanian FIN Nemunas' Neman, Niemen, a river 
of western Belarus ' (= ' marshy stream'), nemuoge' blueberry '; gall. nanfo\a\\ey', tr/nanto' 
three valleys ', VN Nantuates, cymr. nant'vaWey, stream, brook' {*nm-tu-, compare 
participle Old Indie nata-irom nmto-); savoy. /7a 'stream, brook'; perhaps here Old Irish 
nem'sky, heaven'; different above S. 315. 

References: WP. II 331 f., WH. II 158 f., E. Frankel REIE. 1, 405 ff. 
Page(s): 764 

Root / lemma: nepot- {*he- nemot^ 
Meaning: uncle; nephew, *descendant 
Grammatical information: fem. nepff- 

Material: Old Indie /74o^/ (secondary naptr-) " grandson, descendant ', Avestan napat-, 
naptar-, ap. napat- (is.. Old Indie apam napat, Avestan apqm napa-u. name of a divinity (" 
primeval offspring of the waters '); hom. vsnoSsq (5r|or|) " young ones, children ' from a N. 
Sg. *V£TTU)T(;; perhaps here lemnisch-tyrsenisch vacpoG "offspring, descendant, son' 
(Kretschmer, Glotta 28, 266); alb. nip' grandson, nephew '; Latin nepos, -tis^ grandchild, 
grandson ', later also ' nephew '; Old Lithuanian nepotis, /7e/0^c//s "grandchild, grandson'; 
Old High German nevo' nephew, kinsman, relative'. Old English /7e/& 'grandchild, 
grandson, nephew ', Old Icelandic nefe' nephew, kinsman, relative' {*nepdts); Middle Irish 
n'i'ae. Gen. n'lath' sister's son ' (for the form in the end Pokorny ZfceltPh. 10, 405 f.), cymr. 
nei, nai6s., corn. /7c»/"grandchild, grandson'. Middle Breton /7/" nephew '. 

Fem. Old Indie /7a,c^- "granddaughter, female descendant ', Avestan naptT- 
"granddaughter'; 

Latin nept/s {ior -///Sy) after the Astem) 'granddaughter', later 'niece'; Old Irish necht, 
cymr. abret. n/th. Middle Breton n/z, corn. /70///7 'niece'; (common alb. Celtic -f-, -ph- > -ch-,
```


## [2026-09-07T19:30:11.591Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_02 Darlehen/nemah\"; grep -n \"Darlehen\\|nəmah\\|nemah\\|namaiti\\|nemus\" POK_02.txt | head -30"
}
```


### [2026-09-07T19:30:11.651Z] TOOL RESULT

```
=== POK_02 Darlehen/nemah
3150:mir.  caill  (Gen.  caille)  ,Wald',  cymr.  celli  ,Walds,  com.  kelli  ,nemus^ (kelt.  *kaldi)]
6706:Av.  ndmah-  n.  .Darlehen';
```


## [2026-09-07T19:30:12.490Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT namaz/nemah\"; grep -n \"1070\" BRT.txt | head -20\necho \"--- BRT nemah\"; grep -n \"n∂mah\\|nemah\\|nəmah\\|Darlehen\" BRT.txt | head -30"
}
```


### [2026-09-07T19:30:12.573Z] TOOL RESULT

```
=== BRT namaz/nemah
18964:1070
--- BRT nemah
18975:•  j,  'n«inah-  n.  'Darlehen':  yS  natre  n»- mataAgnte  nBit  'mS  paitiiaraiti  täyus 'mariAs  bavaiti  AazaaAa  ivms.baraA£  "wer einem  Darleiher  das  Darlehen  nicht  wieder- gibt, wird  zu  einem  Dieb  des  Darlehens, zu  einem  Räuber  am  Darlehnsgeber"  V, 4.1.
18993:•  j.  nsmö.bara-  Adj.  'der  ein  Darlehen gibt" :  ys ,.  neit  n»mS  (Sp.  1 070  a)  paili.- baraiti  .  .  iavatii  hasatiha  'rahe  'V.4-  ^•
22580:aL  ipäsu  .,)  vanemahi;  ne.  in  win.  —  Vgl.  lu  , ^Jian;  —  Pü. ;  vänüan,  Sü. :  lälayilum;  s.  zu  . 'van.  mit  No.   16.
```


## [2026-09-07T19:30:20.356Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '18960,19010p' BRT.txt"
}
```


### [2026-09-07T19:30:20.399Z] TOOL RESULT

```
dby  Google
io69
namaohant-
n^mahi
1070
•  j.  n^manbant-  Adj.  'ausleihend' 1  yv tiaire  'Amte  nSit  u>mS  (sd.)  paitiMraiti  \ V.4.1.  "  i
Stall  'afihani-  geschr.  (S  2Ä*.  30),  aas  'ahyanl-,  1 PPA-,  zum  den.  Praes.  31  ^rvmahtj/a-,  aus' 'HjmaA:  —  Pii. :  nyäyiinSmand.
«  j.  namaohe  Inf.  'zu  verehren':  s.  unter ' ^mmah-  mit  No.  3.
Zum  V.  «am-,  |
•  j.,  g.  'namah-  n.  'Verehrung,  Ehrerbie- 1 tung,  Huldigung,  Ehrfurcht{sbezeigung)':  | parinavö  .  .  m^vyaAe  .  .  patmrva  hl  °mö  '■ baraiti  paourva  sfartnä  "wer  eine  Feder  \ des  . .  Vogels  hat,  der  gewinnt  sich  zuert Huldigung  .  ."  Yt.  14.  36;  —  sonst  nur  in ' Beziehung  auf  Gottheiten  gebraucht:  haomö .  .  yakmäi  kvan  .  .  dural  'mS  l/ao6ayeiü  1 Yt.  jo.  90;  —  namistaAyä  {sd.)  °maaAä'^ fiii  .  .  paitJ.jamyä  Y.jß.s;  ~~  tat  vS  11}  \ hazaosanks(f.d.)  . .  daiäySi  savH  ahm  vohü\ manatihä  .  .  yaz:>mniN/iS {sA.)  °mai^h3''*\ Y.j/.  20;  —  at  töi  myazdtm  ..  'maahä^ .  .  däm3  (sd.)  y.^^.  3;  —  tsm  ttS  staotais 'maahS  ^a.vlvanlö  (sd.)  Y.  45-  8 ;  —  'maaka  ' aoara  data  ajasani  upara  data  Yt.JO.  118; 118;  —  mi%rim  . .  pairi.jasäi  vantaca 'maahaca  Yt/o.  6;  —  kn  nS  (näml.yVa- Tialls)  stavät  .  .  asa.näsa  "maaha  Yt.  /J. 50; —  'maAT  fySntä  *akura.mazdä  'mahi (LS.  als  Inf)  usSmahi  'mat»ki  (DS,  als Inf.)  vTsilmaidJ  "wir  haben  Freude  an  deiner Verehrung,  o  AAM.,  wir  wünschen  (dich) zu  verehren,  wir  sind  bereit  (dich)  zu  ver- ehren" ^.58.  3JI;  —  mit  Dat  des  Gottes, dem  die  Huldigung  gilt:  'matgkä  a/ni  . . avat  ituyl'^.  12.  3;  —  a/  3  %waAmai  äkre rtltqm  (sd.)  'manAS  .  .  Y.  4j.  9.  a)  bes. NS.  in  elliptischen  Sätzen«;  der  Name  der Gottheit  folgt  im  a)  Vok,:  °m^  urvaireV. ig.  18;  YLi.  21;  —  'num^l  kttvatm  y^arms Yt  /.  2 1 ;  18.  7.  b)  Dat  oder  Gen. :  'mB ahuräi  mazdai  °mS  anDsaHbyH  sp^ntaeibyS *mS^  .  .  'ms  gsul  'mS  gayehe  'mS  lara- "kusirahe ..frava^e  'mstn^'^  vJspayh  afaonS stBis  Y.  68.  22;  g.3,  16,  JO.  13, 17',  2o',Yt /.2iJ,7.iS,  JO.91, V./5.25';  — gave  am^m gave  'm?mi*  Vt/i^.  61,  c)  Vok.  hinter dem  enkl.  Dat-Gen.  des  Fron.  2.  Person: n;mas>  ti  aAura  mazda  .  .  'mB  vS  amf^ä spinta  Ny.  /.  1 ;  j.  4,  Y.58. 7,  V.  21. 1*;  — •mS  vS  gaha  alaonilY.  28.0,  43.  o,  47.0, ^i.o,  SS-o-  d)  Lok.:  'mir  airyene  vai- JaAi  Ytl.21.  OhneWert:  'ttU!  tistrim
. .  'mS  vStS  darin  Yt.  18.  j.  A)  insbes. mit  Bitte  verbundene  Huldigung,  'Gebet': tat  vir?%r>m  dadftnaidE hyat  'mS  Auä%r3m Y.  5Ä  i;  —  ye^Ai  'manAs  ci^nm  Atima- t^mcä  . .  "das  Gebet,  dessen  Ursprung  das gut  Gedachte  ist  und  . ."  Y.  58.1;  —  /«/ nS  'm}  nipatü  pain  .  .  Ibadaahat  Y.5Ä 2;  —  ahmäi  'manhe  üvaidayamaiäl  gas- "hascd  .  .  "diesem  Gebet  vertrauen  wir  an die  .  ."  Y.  5Ä1;  —  °mS  vohü  aom/Tm atbagsftn  Vr.  2t.  3;  Yt.  11.  2;  —  manS  voAa urunascä  asaunqm  'mascä  yS  armaitü (Sp.335m.)*>  Tzkcä  Y.49.10;  —  mit(^n. subj.:  mal  vä  .  .  pairi/asäi  ..  aridrakyd- (sd.)f'ä  'tnanAa  Y.50.  8;  —  mit  Gen.  obj. der  Person  'an  — ' :  tat  hwä  p»r>sä . .  'manAs a  ya'^a  mm?  ximävatS  ", .  wegen  des  Ge- bets, wie  das  Gebet  an  einen  wie  ihr (sein  soll)"  Y.44.  i*' ;  —  der  Sache  'lun  -': aAya  yasä  (sd.)  'manhs  ustänasasiu  (sd.) raplraAya  Y.2S.1.  Undeutliche  oder wertlose  Stellen:  V.26  {'tnanAs),  Ü.31, 103,  Vd.  7  (°m5).
kompA,,  E, ;  Ableil.,  vAbleiL  —  Zum  V.  nani:
—  ai.  nimai-  a.  'Huldigung';  vgL  mp.  namät, np.  namäs  'Gebet'.  —  Pü.  1  nyäyäit ;  itamii-, a.  noch  No.  3ff.,  6f.  —  ')  Pfi.:  nyayihiamandih.
—  »)  Pü. !  änämiru  i5._,  «ber  Sü, :  namasirüh.  — J)  Pa.i  nyäyün  ^3kim  ökrmcad  hai  kasän  vam fia  »yäyim  ku  i^arsandih  i  pa  marlumän  pa an  iamän  ia  kör  u  katfai  hmind  tiyäyan pafirim.  Nicht  recht  deutlich.  —  1>  Wie  im Aiiid.    Es  ist  etwa  astu  oder  Ju^'ä/zueigäuzen.
—  S)  N»ch  der  o-Deltl,  —  6)  Fa.-  i«  1  nyä- yisnömand  spandaramal.  —  J)  PQ. :  nyäyÜn  5 {geschr.  ik,  Sp.  303  m.  No.  21)  k?  710»  nyä- yiiii  i  smäi,  er!.;  din.
•  j,  'n«inah-  n.  'Darlehen':  yS  natre  n»- mataAgnte  nBit  'mS  paitiiaraiti  täyus 'mariAs  bavaiti  AazaaAa  ivms.baraA£  "wer einem  Darleiher  das  Darlehen  nicht  wieder- gibt, wird  zu  einem  Dieb  des  Darlehens, zu  einem  Räuber  am  Darlehnsgeber"  V, 4.1.
KompA.;  »Ableil.,  —  Eig.  'Zuwendung'?; B.  gr.  M/nn,  Ijt.  nümas  'Zins'.  —  S.  iSt  Sp. Übers.  /.  91.  Komm.  /.  ilä,  Haug  Essa^> 237,  Gdn.  Slud.  /,  88,  95,  DsT,  ZA.  3.  49; Temer  Dk.  8.  44.  13  und  Pü.  —  Pü.:  it  5 marl  i  nyäyiinmaiid  -  Hi  afiäyel  dälait  os  ~  ni nyäyiin  apäl  barit  —  his  ni  daJül  -  duidiA  i nyäyän  bavil . .  vai  apar  i  nyäyiin  kai  bariia
—  ia  i^ähel  u  göuiet  ku :  astaia  rat  ne  dahäa ('ich  haba  wohl,  aber  ich  gebs  dir  nicht').
•  j.  namahi  In£  'zu  verehren':  s.  unter 'mmaA-  mit  No.  3.
Zum  V.  nam..
dby  Google
I07I
namaBya-
noit
072
•  g.,j.n»niafiya-deD.Praes.3i  i)'Cemer Gottheit,  Akk.)  Ehrfurcht  bezeugen,  hul- (Ügen':  tamakySmahl  isäidyämahj  (sd.) 5a»a  mazda  ahurä  Y.jö^.5;  —  yä  vS (nämL  afB)  . .  ahträ  . .  *namam  dadat lait  vä  yatamaid!  .  .  *fryqnmahl  .  ,  nt- mahyämahf  ,  .  UBidyamaAi  Y.JÄ4;  3g. 4.  2)  'etwas  (Akk.)  durch  Gebet  er- streben, erflehen  fiir  -'  {avi  mit  Akk.): tat  vJsp?m  frfnamahi  . .  mmahyamahi  avi imqm  tanüm  V.  20. 5.
W,  namasyami^,  —  Pu. :  nyäyiintnilan,  (luV.); nyäyätämand.
•  g.  namax^ant-  Adj.  (fem.  °3^aiti-)  'ehr- foichtsvoll' :  ävi/ nä  antan  fiSntU  'Haitis ..  ratayl>(s±)  Y.SJ.J.  I
Ableit.  (mit  vaitt-)  ans  tn^mai-.  —  ai.  ndmai- vani-  Adj.  —  P5. :  nyäyiinSmarui, ].  taimiia:  lies  rumaiia.
•  j.  yeii  tai  ''^äfrimari  (sd.,  auch  für  Pti.) oamö  Ryai  ..  N./2:-?-,
j.  nimS  vaatähoa  V.  75,  43;  lies  mmS-v*.
•  g.  nsmoi  Inf.  'um  auszuweichen,  zu  ent- fliehen':  *kqm  n°  zam  iu%rä  »'  ayenT  "in welches  Land  um  zu  entfliehen,  wohin  um zu  entfliehen  soll  ich  gehen"  Y.  46.  i'>; st  H,2.  20,  wo  n^Mlfi  . .  tt>me.
Zum  V.  «am-.  —  ai.  m-näme  Inf,  —  Pü.:  /a nyäyiin.  —  i)  Vgl.  iSt.  Gdn.  3Yt.  86.
•  j.  nsmö.bara-  Adj.  'der  ein  Darlehen gibt" :  ys ,.  neit  n»mS  (Sp.  1 070  a)  paili.- baraiti  .  .  iavatii  hasatiha  'rahe  'V.4-  ^•
Vü.:  B.  VKiti  'tamah-.
•  j.  namö.vaDhav-  m.  EN.  eines  Gläu- bigen: 'varahSiä  ^vailiaiakahe  asaonS  VL 13.  109.
Eig.  Bed.?  Vll.  aus  einem  «tlipt.  Satz,  etwa nmö  vaakavö  "Verehrung,  ihr  Guten!"  ent- , standen.  —  Vgl.  vohu.tamah:  \
•  j.  *nainö.vantä-"  f.,  Plur,  Bezeichnung dnes  zum  Lager  für  Tiere  geeigneten; weichen  und  warmen  Stoffs:  upaca  k!-^ (näml.  der  jungenden  Hündin)  gätüm  ba-' raym  (sd.)  'täkoa  kamcit  vä  sianta^inam
(Bd.)  V./5.43.
Pü.:  mlnn  vanasa  (in  Aw.-BuchiL).
•  j.  vJipa  äps  . .  urväzjttte  yä  . .  ustatatfm "n«mr5niii'>  FrG,
I)  Hat  jedenfalls   eine  3PIUT.  aus  mrav-  mit
«T  verdrängt:  'die  Wasser . .,  die  ..  sich  Glück
und  Erfolg  rerheissen',   vgl.  Vt  13.  93  usw.
j.  framä  ntrpgä  rayöS  N.  Ig ;   lies  frä  mä
nar,  gSraydii  i?,^.  5II  u.).
•  j.  nsra.gar-  Adj.  'männerverschlingend': ailm  .  .  yim   aspSganm  'garwt   Y.g.w.
Pu.:  mio-l  epär,
•  j.  n^ra.baraz-  f.  'Mannshöhe,   -tiefe':
a  zrtubyasal . .  ä  maityqnasaj''>  . .  3  'sasHi (Abis.)  ". .  bis  zur  Mannshöhe  (ins  Wasser gehend)"  V.Ö.27; — *2nu.b?r7zS°zö''^  *gairi.- ifmff  mäns(sä.)'BTBy.;  —  a  'ganqmYd.14.
Pü.  r  mari  iäläi.  —  i)  J  304  II.  2.  —  >)  Oder
```


## [2026-09-07T19:30:37.506Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT nemata/nimata\"; grep -n \"n»mata\\|nsmata\\|nimata\\|namata\\|Streu\\|Stroh\" BRT.txt | head -30"
}
```


### [2026-09-07T19:30:37.556Z] TOOL RESULT

```
=== BRT nemata/nimata
14428:Et.?  Falsch  Hbm.  ZL  76  (vgl.  PSt.  73),  un- vrahrscheinlich  FiCK  VElWb.4/.  23a  —  Pü.: späi  (Transskt.),  s.  noch  No.  i;  Npü.:  xüb loTx,  Sti. ;  httkacaJtram.  —  ■)  Pü.  hat  hier  1 /igen  vät  .  .  ka  Ici  äytt  daJt  fräl  mältt,  erl. ; kähilaiih  u  Sic  i  afic  barit  "wie  der  Wind .  .  wenn  er  rasch  geht  {vgl,  '*ici/B-),  die Ebene  (für  dahnä^  freifegt,  Stroh  usw.  tragt er  fort".
18438:—  sastaista  (sd.)  ya  nh  i^ahrf  dayat  Y. jo.  5;  —  zqm  .  .  yä  na  baraiti  Y.38.  i ; verwendet  Y.  rj,  i ;  —  pasukanqmi'a  ySi ni  Jijismtl  Y.  Jp.  i.  zu  i  a):  ahural nü  na  avar3  (sd.)  Y.  2ß.  ji";  —  täiizfn' fyaokanäis  byattZ  . .  Y..34.  8;  —  p^nsaia nh  ya  ..  Y.4J.10.  zu  2):  urvätHtS (sd.)  AvS  nä''^  .  .pain.jamya  Y.36.  2;  — namislahya  nimatahü  na^  .  .  paifl.jamy< Y.gG.i.  U!)  g.  «JGen.-Dat  Plur.;  zu  i) : täl  nS  mazda  . .  fradaxUä  (sd.)  Y.  JJ- 1 7 ;
26656:•  j.  stairii-  n.  'Streu,  Lager,  Bett*:  yö narö  hamSgätvS  nipa^yänte  kam  vä  paiti 'ril  harn  vä  paiti  barni!  V .  5.  ^T,  — ivat  alte  'risca  bamüia  aisa  ärtixi  .  . fräsnauiti  V.  7. 9 ;  —  uptma  [alte]  •ris[ca] aitt?ma  aiwi.var^a  (sd.)  V.J.  10; —  allat aitahe  äste  (Sp.  340  m.)  'n hqm.v3r»iiante  V.  5.  59.
```


## [2026-09-07T19:30:38.631Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB glossary namat\"; grep -n \"^namat\\|namat\\b\\|nmt\" NYB_vol2_glossary.txt | head -30"
}
```


### [2026-09-07T19:30:38.690Z] TOOL RESULT

```
=== NYB glossary namat
1792:Hamadan [hmd’n'] 115%. — The NP form; the Milr forms are: 1. h’nmt’n = Hän- matān, BdA p. 92!2, or hnpt’n = Han- batün, inser. of Mishkin, v. BSOAS
2628:namat [nmt'] felt 3117. — Av. (1068) nə- mata-, regarding which v. Benveniste, BSL 32, 1931, 82sq.; NP namad; bor- rowed in Aram and Arab (namaf-).
5247:nomata-: namat
7268:namad: namat .
```


## [2026-09-07T19:30:48.896Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /1068/ && /nam/ {print NR\": \"substr($0,1,50)}' BRT.txt | head\necho \"---- search col 1067/1068 leaf\"; grep -n \"^1068\\|^io68\\|1068$\" BRT.txt | head"
}
```


### [2026-09-07T19:30:50.167Z] TOOL RESULT

```
---- search col 1067/1068 leaf
```


## [2026-09-07T19:30:53.030Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"1068\" BRT.txt | head; echo ---; sed -n '18880,18965p' BRT.txt"
}
```


### [2026-09-07T19:30:53.106Z] TOOL RESULT

```
20853:vaoiä  (sd.)  ys  Im  dät  "novi  (cum)  qiii .  ■" Y.45-4;  ö,  31.  19;  —  *malni/(sd.)  ys dngvaiU  xsä^rfm  Aun{iiil(sd.)  . .  yS  nöii jyUtam  (sd)  vlnastl  .  .  "poena  (eius)  qui . ,  eius  qui . ."  Y.JJ.  15;  —  rumanhä  (Sp. 1068  u.)  y!  . .  cista  yS  .  ,  dasdl  "respec- tuosus  (ei)  qui.."  Y-Jl-Sf.;  8; — yekya {zu  3)  iavS  isänii  . .  ySi  . .  *a»haricä dvaHti(ßd.yä  ". .  (ei)  qui  . ."  Y.  45. 7;  — yeAy3  . .  vahiibm  . .  valäs  maidä  . .  ySi äaharfcä  htnücä  "cuius  .  .  (eonim)  qui fuerunt  et  sunt"  Y.j/.  aa;  —  pirisä  ySi pi^yeitUI  (sd.)  "interrogo  (eps)  qui  . ."  Y. 44.  JO;  —  ä  vS  *gSus.ä  ÄsmyarUa  ySi  . . sännti  .  .  yassqm  ta  .  .  fradaxlts  akl ". .  (cum  üs)  qui  . .  quorum . ."  Y.5J.  3;
30170:•  j.,  g.  hu-xratav-  Adj.  'des  Einsicht  gut ist,  ems  ich  tsvoll':  haomö ..  •tus\.g,  23;  — fratanmät  lg  (näml.  haomahe)  havamm  . . 'tvSiyS.)  Y.10.2;  3; —  vastryö ^ao^anäii snsvS  hqs  'tul  ntmanhä  (Sp.  1068  u.)  Y.
---
•  j.,  g.,  p.  näman-,  j.  n^tnan-"  n.  "Name":
äat  hi  'ma  fradai^yh  atr».dät)m  vä  . . Aqmät  va  ii/rf.dä/aAe  (sd.)   'ma  V. /Ä53;
dby  Google
1063  lumoan-  AI
Vd,/}";  —  ya^qmca  pars  mafyaia  ahoi- ta^a^a{&A.)..gaitinqm  'mqm{AS.)  däian Yt  IQ.  6;  —  yä  vs  vamtkU  (nämL  äp5) ahurS  mazdä  *°mqm'^  dadäi  .  .  täii  vi yazamaiäl  Y.  ^JÄ  4;  —  tq  yazsi  ifaii •w»ir/(IPO  pairicä  jasüi  (sd.)  vanta  Y. 57,22;  —  hyat  vä  töi  'manqtn  vözObm atan  . .  tä  äjoj  pairijasumaidi  Y.  j6'.  3;
—  anusS  ipfnti  vaakBi  sflräU  'mqn  (als IP.)  äiii^a  Y.  75.  1,  Vr.  tf.  i;  —  'tSm  .  . ahüirys  °«Är(als  IS.)  magda.vars  (sd.) . . yasamaiäf  Y.jj.^;  —  'mini  spu  yaza- maide  YtJ^,  79:79';  —  kaAe  nS  ila •ma  ayairydiiSp.  512  m.)  Yty.50;  — ahmä^m  'ma  . .  yat  amsSanqm  spintanqm tat  asH  mq^rake    spmiahe  amavästtmim
•  Yt7.3; — frsit  mg  tat  'ma  framrüm  Yt /.  S;  — yasia  me  .  .  tmi  •inlnli  (als  AP.) drfftJayS  . .  Yt/.  16;  11,  15;  —  ^vjsqs *taia  imi  'msnü  (als  NP.)  parltas^a  '.  . vismie  Yt /.  19;  —  l&sca  mg  °ma  (AP.) abaya^a  Yti5. 49,  50;  —  gSusca  'ma mazdaoätfm  Yt  Ä  2 ;  —  'mSni  amslanqtn sptnianqm  Ytrf-a;  7;  —  sPaitka  va  duyta va  'va'ni  V.  14. 15  (?) -ö.  a)  AS.  und  LS. (im  Sinn  des  IS.)^*  als  Adv.  'mit  Namen'; i)  im  jAw.  AS.  nqma,  hinter  dem  Nom. propr.ä':  iar^zahi ..yat  vaolii^A^ häkairJm °ffio  Yt/0.88;  12-7,  i^-SS';  — pairikayai .  .yS  duzyairya  yqm  mafyaka  . .  Auyäiryqm 'ma  ao/aiti!  (sd.)  YtÄ  51;  V. /j.  z,  6;  — tturf/S  .  .  yim  ma^aka  .  .  kahrkatas  'ma ac/ai/e  (sd.)  V.iS.i$;  17.31  —  vayui  bä 'ma  äkmi  Yt  75.  43 ;  43-48  (oft),  /.  7,  8, 12—15  (oft);  —  vairil yB  haosrava  'ma YtJp-sö;  59,62,  7.30,7^,129',  142,74. 59*,  V, /i".  15;  —  ar?dvi  'ma  apa  V.7.16;
—  ahm.ye^he.raocä  'ma  aiaonS  /ravalXm Yty.i2o;i2o'; — hinter  demNom.appelL: vJzari^  dagvs  'ma  N.ig.ii).  2)  Bim Ap.  LS-,  uzw.  a)  näma",  b)  namä";  ersteres folgt  dem  Namen  eines  mask.  oder  neutr., letzteres  dem  eines  fem.  Appellativs*'; a)  nämtf;  sowohl  der  Name  als  das Appellativum  stehen  unter  allen  Umständen im  Nominativ'';  al  das  Appellativum  geht voraus :  i  martiytr  magui  ähJ'  gaumntJ' •wo"  Bh.J.ii;  i6',  2.3,  5,  6,  i4,^-3.  S.  I3. 5,1'; — avahyS  k<^büjiyakya  bräta  bardiyt^ °m^  ak(^  "illius  Cambysis  firater  Bardiyas nomine  erat"  Bh.7. 10.  ast)  statt  des Appellativs  erscheint  i'*:  7  gaumäti^  'ma' äh<^  hauv  adurujiyj'  Bh.^  a ;  2*.       ß)  das
Appellativ    folgt:    *parg<^    'mii'    kauft^ avadä  , .  Bh,j,  7;  7. 11;  —  tOzäm^  'mii' vardanam  Bh,  7. 19;  2.3,  6,  12,  16,^.1,  5. 6,  8,  2.  7;   —  AaÜa  piravJ'  •««"  rauür D.77. 3".        7)  ohne  Appellativ;  wir  über- setzen dann  'einer  namens  , .'  oder  'ein  ge- wisser"*': kt^baßya*  °»w"  kärausptth^^ .. püruvam  ida  lüäya^iyi^  aAi/'  'Bh.i.io;  — taxmaspad^  'md'  mSd(^  manä  b(^dakt^ Bh.2.i4;io,j.3,6,q,  i4,^i8*,S.7.      Ohne Wert:     darayj'vcTus     vistaspakya     'mi^ /«ä'a*    Ao.  7.  2;   2.        b)    nätm/*;    das Appellativ  folgt:  hauv  udapatalä  habiraav dubali^  -ff/j"  äahyaus  haca  avadasa^  Bh. J-»3;3.  5.  »o.  ^-»S-i-ö,  10, 11, 13;— /«fra* -Ma"  dida  arminiyaiy  avadä  hamaranam akunav<i'  Bb.2,8;  9,   7.13, _j. 9,  11. KompA.  (n^iH'),  E.  —  tä.  tUiman-  n.,  np.  nän. —  P6,i  näm;  s.  nOch  No.  3.  —  >>  Nur  in  nfiu, aber  hier  stets.  —  >)  So  alle  Hds.,  mit  jinei Ausnahme,   J  3,   wonach  NA.  'oif  bietet  — 3)    Fü.:    nndeaüichi    a/ä^i  addpnark  ann (Jamaspji  Gloss.  569  u.)  paakann.  —   1)  S. No.  6.  —  5)  Von  dem  es  nur  durch  ein  Ed- klitikum  getrennt  sein  kann.  — ')  Die  Frage, wie     ap.    t^amf    beim     mask.    nnd     neutr., rfiamt^  beim  fem.  Appellativum   formal   and syntaktisch    zu    fassen    sei,    ist    noch  nicht gelöstj  luletit  darüber  FoY  IF.  la.  171,   wo weitre  Litt.  —    7)  S.  No.  9.-8)  Vgl.  FOV aO.   174.  -^  9)  Fovs  Fassung  von  ßiräva*  aU Abi.,  aO.  176  halte  ich  nicht  für  richtig;  ich verlange  auch  hier  den  Nom.j   s.  Sp.  907  o.
•  j.  "näyaäta  N.  4(5'',
Pa.i  fehlt  —  0  DsT.  liest  nä  yaHa.
j.  ava  niyn'ifiTm  P,  Jj:  lies  0x10.10/0/1/!!».
•  j.,  p.  nav-  f.  'Schiff"'.
KompA.  (s.  nmäta-);  Ableit  —  ai.  tiav-  f., np.  Mäti,  —  ')  S.  übrigens  näviyä-  No.  1.
•  3.  nävaya-  Adj.  (fem.  °ya-)  'schiffbar',  Be- zeichnung fli essenden  Wassers  von  grösserer Breite  und  Tiefe:  airysJayatam  ..yahmya apö  'y&  p^n%wi/  XiaoiartAa  %waxi?nU Yt  10. 14;  —  . .  'hraotS.siacS  apa  taänä 'yä  Yt/J.  ro;  — pxavS /raoirisyBti  tarasca apB  'ya  (APf.)  V.  14. 16;  7<y.  74;  —  tyaäa *nä  buyat . ,  hupirihwe  a/s*'ya''>  Yt.i6.y,
—  apqm  vä  'yanqm  paiti pfntBsYt.11.^;
—  dasanqm  apqm  'yanqm  aojS  ytÄ24; 74-39;  —  'yayai  .  .  ape  N.  ^7;  67;  — yai  nSit  spa  . ,  mag^e  va  cäiti  va  vaimi va  urüili  va  ape  va  'yä  (GSf.)  pai&yaiie
V.i?-37-
Ableit  ans  *näv:  —  Statt  «äviya-  getchr., S  S6S.  n  b;  vgl.  No.  I.  —  Pü.!  äfi  i  nis ISi'),  eri.  (in  V.  t4):  ktdd»  ;  äfiän  fia dan.    —    ')  So  J 10;    NA.   nach   Fl  nättya.
ob,Google
:o6s
naviya-
$36S.  13  a.—  >)  Statt  dessen  «uch  anap(t)>It. —  3)  S.  zu  parhiya:
•  p.  näviyä-  f.  'Schiffezeug,  Flotte,  Flottille' Uta  abis  'ya  ähJ'  "und  dabei  war  eine Flottille"  Bh.7. 18''.
Ableit,  aus  'näv.  —  ■)  Vgl.  Kbrn  ZDMG. 23.  237.  Anders  jeiit  FoY  ZBMG.  54.  371 (LS.  aus  Häti-\.
•  j.,  g.  näiri-  f.  'Frau',  bes.  die  verheiratete, als  Mitglied  der  Familie, 'Ehefrau',  im  Gegen- satz za^nar-  und/»&ra-:  huxsa%Tas{^A^tü «7  nä  vä  °rf  vü  xsailä  Y.  41.  2;  35. 6;  —  na  va  'ri  va  Yl  ii.  4;  —  narasca *'rlsca''>  (NP.)  Vytjo;  —  3  airySmä (sd.)  .  .  janta  mDhyascä  'ribyasca  zara- %ustrahl  Y.  54.  i;  FrW.  /.  i;  —  vTspa- nam  naram  'rinamca  taoxma  Y .2. 2"];  30, &12,  iz,^-SS.i2,yfä.2;  —  frinyä  'ryi usimtnanhö  "der  Fr.,  der  Frau  des  U'' Yt. /J.  140;  140*;  —  aat  niqm  tarn  fsaona- yeke  (sd.)  'rya  va  pu%Tahe  va  haoya  vä mariiiyi  (sd.)  Y.  //.  i ;  N.  54.  a)  mit asavan-  (Sp.  250  m.):  naram  'rinam  ., a/atmam  asaonitiqm  Y.  26.  7;  8,  10,  Vr. rö'.a,  Yt.y,i43— 145*;  —  asäunqm  fravasls narqmCä  'rinqmiä  '^.g-j.y,  $g.2,  [V. 5.37:  lies  hqm.ttairmqm?\
KompA.,  E.;  Ableit.  —  Ableit.  aus  nur-.  — ai.  närl-  L  —  Pü.:  n5irsf\  —  0  So  K4i Ausg.  'ryaica.  —  »)  S.  lU  näiriia-.
•  j.  nÜrikä-  f.  'Frau',  bes.  die  verheiratete,
'Hausfrau',  uzw.  der  a-4«rischenSchöpfung'': yat  ahtTti  nmane  yat  tnäzäayasnBts  °ka a^ravaiti  .  .  nisAihaj  V,  16.  i;  8;  —  yö 'kayä  ei^ravaihyä  .  .  x^an%>m  frabarät . .  hat  :far>%?m  frabaräli  dva  danar>  . . yesi  nSii  'ka  muruioyat  (sd.)  Y.16.5—7; a'i  13,  14,5.50;  —  yff  'kam  cdravaittm .  .  xhidrä  avi  franhartzaiti  V.  18.  67 ; y  ■  7 ;  —  anySJkaisa  (sd.)  -ka  pairi  xsudrh Jra»^artzaiti  tiik.  2;r;  — yaiAe . .  mazda- yasnanqm  °ka  avaya{%A^  xsudrä  *Aqm.- rai^wayeiti  .  .  ti.li;  —  y3  'kam  yqm apu%rqm  .  ,  xjudrä  avi  fratahrszaiti  V. i^.  8;  —yat  ahmt  nmäne  yal  mäzdayasnöis 'ka  upas.pükirlm  (sd.)  jasat . .  aSdla  alia °ka  la^a  apu%rJm  (sd.)  mjasai  uzuUana V.  5.  45;  59.  7-  70,  7I1  Vd.  igi;  —  yai fiairi.cinaivÄä  jasqn  upa  va  'kam  vä^ayaäa V.  4. 44;  —  'ka  (\AS.)  'kayä  (GD.)  'kanam (GP.)  F.2f.;  —  ratufris  -*'kaya'^  kihrpa N.  sg;  —  a^rS  .  .  av<^a  (sd.)  'kayäi  V. ■'5-4S;  —  naram..  °  rikqm  (GP.?)  Az.i, VytJ;  Vdy;   —   nar^m   va   *'iqm   va
Täx^na.y-  1066
pu%r?m  va  FrB. ;  —  Aai^a  na  paiHirütS haca    'ka  paiti.iriste  Y.  10.  $;  —  yat  ba
\paiti  nars  aSaorUS . .  °kala  apsnnsyäkasca varai^rm  (sd.)  pantqm  atBit  V.J.  11;  3; —  ,.  zaohrata  (sd.)  ratufris  'käscit  (GS.) apgrmäyükahecit  N.  .^0;  —  yS  anyahe'ka (IS.)  ..yS  anyehe  ^apirmSyüka  *anakaxt/T a'haurUTifm  *parar>kacaiti'ü.6i.;  6; — yHi.. 'kqm  vä  *ap}nnäyük>m  (vS)  a/t?m  dasli N.  105; —  'ka  kasujcra%wa  (sd.)  ^.40;  — ava%a  Ag  x"atg  (sd)  pu%rytn  ankat..aat yai  hvqtn  'ka^^  bavaiti(sd.)  ..yai dirftrqm \AfntiYd.2\  —  dahma  •^rf(NS.?)  ap^rma- yüke  kainike  Y.2^.3;  —  katärS  (sd.) '  a%aurumm  *parayat  'ka  va  nmänS.paiti^ va  N.5;5,  *5'>j — yai . .  nmanahe  nmOnB.- paitlm  'kam  .  .  daiöÄSui  daiiikupaitim 'kqm  bisazyätY.j.42;42',  is.$&.  a)mit asavan-  (Sp.  250  m.):  nanm  aiavanjm  . , 'kqm  a^aonlm  V.p.  33,  42,  75.12,  26,  rr.i, 2/7,  10  (statt  Ab!.),  Vr.j.4,  G.4.9;  — tat  asti  yUnO  . .  a^arihim  , .  tat  -kayai  . . ratuxsa^ray'ai  asaonyäi  H.  z.  1 8 ; — 'rikayh aiaonyä  Vd.  4-
Ableit.  aus  näiti-.  —  Pü. :  Ion,  näirU  (Transskr,). —  I)  Im  Gegensatz  za  jahikä-,  s.  H.  2.  18, 36.  Nik.  2  beweist  nichts;  s.  noch  No.  3.  — ^)  So  T,  —  3)  Pü.  erläutert  hier  (Vd.  2)  näirlk mit  pätixiäh  ian;  vgl.  d»iu  West  SBE,  J.  142 ('a  ruling'  or  •privileged  wife')  und  Houruu* Schindler  ZDMG.  36.  86  zu  ZDg.  Säkian.  — O  Ilds.  'käi.
•  j.  näiri'^'Wana-  n.  'Stand  der  (Ehe)&au, Ehestand':  o^anha  v3  duyoa  va  ..mrabyS a/avabys  *'%wanäi''>  upa.valayaaa  (sd.)  V.
14- 15-
Pü.!  »Si,mi.  —  ')  So  Jp  I  usw.;  NA-  •na.
•  j.  näiri.£mah-  Adj.  'eine  Frau,  Frauen
heischend"':  yai  'nankS  jasqn  upa  vä näirikqm  vähayagta  (sd.)  V.  ^44;  44.
Pü.:  tiäitik  iämaiih  rät.  —   •)  Vgl.  lu  laiß.-
Hnah-  No.  1.
•  j.  näiri'vant-  Adj.  'mit  einer  Frau  ver- sehen': nmämm  .  .  "vat  pu'^ravat  "ein mit  Frau  und  Kindeni  versehenes  Haus" V.  j.  2 ;  —  'vaite  .  .  aAmaj  pourum  fra- mraomi  . .  yaha  mayavö  (sd.)  fraväxlSi^ V.4.47-
Pü. :  n&irikSmand.
•  j.  närsnay-  Adj.  —  ?  — ,  bezeichnet  be- stimmte Handlungen:  avaisü  * dim pascalta 'ni  lyadhna  aiwi.daihlta  A.^.  13.
Et.?').  —  Pii.,  Sa.:  transskr.;  Pü.  erL:  kul lanäpuhr  Aaca}  ape  kartend.  —  ')  Greulich  DST. ZA.  2.  735.
dby  Google
io67  näs>m
•  j.  naspm  Inf.  'hinzugelangen  zu  -,  zu erlangen'.
KompE.  ~  Zum  V.  'nas-.  —  Pü.:  ariänik.
•  j-,  g.  näs-  V.  'tragen'.  Praes.  i  nä^-, 30  (Iter.)  näsaya-.  —  Inf.  °näsS.
'(tragen  sva.)  als  Träger,  Stütze  dienen für  — '  (Akk.):  ya^a  lia  väcim  näslma (iPOA.)  ya'ia  vä  saosyantd  dahyunam Y.70.4.
mit  ä:  s.  Inf.,  Sp.  331  u.
mit  fra  'herzutragen,  -bringen  zu  — ' (Akk.):  aesmanqmat  .  .  vasyäi/ (sd.)  .. ratSu^ nmätism /rSnSsayata{'i2.1)  K.3. 5;  5.
mit  tili  'wegbringen,  -schaffen':  ka^a drujtm  ms  ahmal  3  nis''>  naSämä  tsiig  a ava  ydi  . .  "ob  wir  wohl  die  (Anhänger der)  Driig  von  uns  wegschaffen  können hin  zu  denen,  die  .  ."  '^■44- 13;  —  «''■r-- na/ama  saosyantd  *ärußm;  ia%a  (sd.) nTs.naiamat  yaha  Mm  janama  Y.  6'/.  5''.
mit  nis  und  paüi  'wieder  wegbringen, fortschaffen':  *nis*tat  paiti  druxi  naSäite yaaat  (sd.)  aiwicit  jaymat  "die  Dr.  wird wieder  fortgebracht  werden  dahin,  woher.."
Yt.I(?.I2.
^"Eiweitening'  zu  lit.  ahiti,  kil.  nesli  'tragen' ; vgl.  ksl.  n&&,  j-Aor.;  S  338.  a.  —  Pü.  (lu  Y. 44,  61):  ntlaitl),  (lu  70):  nhiiiehilati,  (10  A): iurlan,  Sü,  (lu  A,):  samänetum.  —  •)  Nach dem  Metnim  zu  streichen.  —  ')  In  Anlehnung an  Y.  44.  13.  —  3)  Oder  kaillant  Vgl. West Sg.-Gloss.  353,  2Ö0.
•  j.  "nä^tanam  aajanka  Yt2. 12,  14,
j.  nähmea  Vyt.  25:  lies  tiäämna-,
•  j.  'ni§9nuia-  Ad}.,  Pj-AorM.:  s.  'nas-.
•  j.  'nääamna-  Adj.,  Pj-AorM.:  s.  'nas-.
g,  nä!ü  Y.  JA  5  1  E.  MOS-.
•  j.,  p.  nah-  m.  'Nase',  Sing,  und  Du.: Waäamsaiy  uta  nüham  utä  gausa  fraja- nam  Bh.  2. 14;  13;  —  yim  yava  vatim närahabya  hubaoüitim^m  ßgaurva  H. 2.8;  26;  —  t^m  vahm  ninhaya  (LS.)'> *uzgnmiiiysil.2.8;  a6;  —  «Jw^a  (ND.)'' F.jd; — yaha  *nänhai''  Aaca  *gaoSaäbya ydha  vä  gaosa  Aaca  *^raaAiiya  (sd.)  P.  28.
Vgl.  nSshan:  —  ai.  Has-:nas-  m.j  mp.  näk (?;  aus  *«äAail).  —  Pii.:  vinU.  —  ')  LS.  im Sinn  des  IS.;  oder  ist  die  Form  ein  zum  ND. neugehildeter  IS.?  S  22J.  3.  —  ')  Oder  IS., oder  allenfalls  auch  NS.  zu  niohan-.  —  3)  Hdi. ittha,  aber  Pu. :  vliük.
•  g.  n»  Part,:  s.  unter  ti3.
namaDhan-  i  oäS
j.  n>l}ma  N.  ^\  lies  nititna.
j.  tanf,  Verbalf.:  s.  unter  nam-.
•  j.  n«mata-"  m,  1)  'Reisig':  nasui  tga- 'kaite  .  ,  7flä(i  .  .  'tS  tarS  yan  "die  A''. verschwindet . .  wie  übers  Jahr  das  (dürre) Reisig"  V.p.  46'';  —  avi  Um  spayUt  . . vJspaca  avi  tiyra  *-ia  ".  .  und  auf  lauter spitzes  (dorniges)  Reisig"  V.J.35; — katgAus .  .  äraasca  *'taheca  ayanheca  "die  Nutz- niessung  von  Holz  und  Reisig  und  Eisen- gerät"  V.5.38.  2)  'Geflecht  aus  Reisig, Hürde'  (nur  Komp.),
KompA.,  E.;  vgl.  auch  *»^maÜj.  —  Zum  V. nam-  '(sich)  heraL beugen',  vgl.  nhd.  reit  und ags.  Aiissan  'liltem'.  S.  auch  JOHANSSON  IF. 3.  54.  —  np.  namad  'grober  Teppich;  Filz'  3).
—  Pü.:  namal;  (luV.j):  apdnnatdl,  un- klar. —  1)  NA.  schwankt  iwischen  niot'  und «im\  Vgl.  auch  das  ai.  LW.  namaJa-,  das ein  mp.  nam-  voraussetit.  —  =)  Die  dün  ge- wordenen  Reiser  der  Bäume  werden  von  den Frühjahrsstürraen  abgerissen  und  verwebt  — U  Vgl.  dazu  oben  Bed.  2.
•  j.  *namato.-aiwi.varana-'*  n.  'Unter- schlupf,   Hütte    aus  Reisiggeflecht"*:  yat
däuru.upa.darane  va  'ne  vä  spS  vs  nä  va
irihyat  V.S.i.
Eig.'ReisigCgeflechtjbedeckung',— Pü.:  nama' apar  nihumbih.  ~-  ')  NA.  tum".  —  s)  Im  Folgen- den als  nmäna-  bezeichnet.
•  j.  *nama8kä-"  f.  'Reisig'  als  Feuerungs- material'>:  yat  .,  mafyaAa  daluayasö  avi atnm  abarjnti  .  .  aft>m  alstmm  yS  vaoce 'ka  nqma  Yl/4-55-
Zu  tamaia-  wie  ai.  asialkä-  (BloouPIeld  SBE. 43-  278)  zu  avalä-  m.  —  0  Wegen  M  s.  S  36S. 50.  NA.  hat  lamAia,  was  ich  nicht  für awestisch  ansehen  kann.  Vgl.  Var.  —  >)  Das aber  zu  verwenden  verpönt  war.
■  j.,  g.  namaohan-  Adj.  1)  ehrfurchtig': *asaca  'tshana  (IS.)  ux^ne  (sd.)  xra'^we yaomm  (sd.)    aste  V.^,  45.  2)    'ehr-
furchtsvoll bittend,  betend' :  yi  mq%ra  (sd.) *vaam  .  .  baraitT  urvahu  aia  *nAa  (NS-) Y.50.  6;  —  vastryS  yyaoHanats  fnfys  Aas Auxratus  -»Aä  yS  . .  "der  Bauer,  der  in seinem  Tun  gerecht  ist,  der  einsichtsvolle, wenn  er  (zu  dem)  betet,  der  . ."  Y.  5/. 5  j  —  yH^i  'nAa  (NS.)  vaHm  baraili  yal gaosXsAyit  Yt  10.  85 ''.
Ableit.  aus  ^mmak:  —  ai.  vgl.  namaniB- Adj.
—  Pü.  (zu  Y.):  nySyünSmandlh,  (zu  Y.  57): ke  varzUar  fa  iuniSn  Kul  fa  Aiaaiän  Auxral Aä/  pa  nyäySn,  (zu  Y.  ySy.  aAräiih  nyäyisn giißär'),  erl.:  ö  iär  u  katpai  franämem.  — i>  Anscheinend  nach  Y.  jo.  ö  geformt.  — 3)  So  bei  Mills.
dby  Google
io69
namaohant-
n^mahi
1070
•  j.  n^manbant-  Adj.  'ausleihend' 1  yv tiaire  'Amte  nSit  u>mS  (sd.)  paitiMraiti  \ V.4.1.  "  i
```


## [2026-09-07T19:31:09.694Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'namat [nmt' in p:\n        print('leaf(0-based)',i,'=> printed',i-8)\n        print(p[:1500])\nEOF"
}
```


### [2026-09-07T19:31:11.065Z] TOOL RESULT

```
leaf(0-based) 150 => printed 142
tšān bagān ~ burt (from the door of =) at the court of His
Majesty I made the prostration (before :
him) P1:4; pat rod opast u ~ burt he bowed down on his face and paid (him)
homage 112° (the rpooxdvnotg); 119 (6).
135
Nam-x"ast
and woman)’, with mi- > mu- through the influence of the labial; cf also miĝwa = gumécak FrO XI.
muzrayik [mwel’dyk] Egyptian, of Alex- ander the Great 1075-12, - OP mudräya-, SW form presupposing a NW form muz-.
1418, 1820, 1927. 35? (be o). 104! (pat). — Av. (1069) namah-; MPrthPrs mmc; FrP 19 *SGDH = nm’c, but Cod. 8, XVII, 7 nm'š with NP gl. namäj; Paz. namāž; NP namaz.
nämak [n’mk'; inser. n’mky; SM-k'] in- scription P2:3; letter 3? etc.; book 1071, 12119; in book-titles: Kär-nämak, Pand-nāmak etc. - MPrs n’mg; NP nā- mah; from nam.
namat [nmt'] felt 3117. — Av. (1068) nə- mata-, regarding which v. Benveniste, BSL 32, 1931, 82sq.; NP namad; bor- rowed in Aram and Arab (namaf-).
näm-ävurt [n'm'wwlt'] *bringer of re- nown 2723, — -ävurt possibly from the nom. sg. of *ä-bartar-: *ā-bartā > *ävart remodeled after the pt. pass. ävurt; v. āvurtan.
näm-burtär [SM-bwlt’l] (child) who bears (and propagates) the name of a p. and his family 19. — V. burtan.
nàménitan [n’mynytn'] to call by name 11229,
nàmik [n’myk] renowned, comp. ~-tar 227, 916, 178. 4727; Baxl 1 ~ 1132; v. also fräc-nämik.
nām-cišt [n’mc$t'] especially, particularly 18°; pat ~ 8018. — = Paz.; from nām + cist, pt. of Av. (429 sqq.) kačš- ‘to teach, to assign’.
nāmcištīk special, particular
```


## [2026-09-07T19:31:22.973Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD\"; grep -n \"^namāz\\|^namaz\\|^namad\\|^namat\\|namāz\\|namat \" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== HRN 233 area namad\"; grep -n \"namad\\|Filz\" HRN.txt | head -20"
}
```


### [2026-09-07T19:31:23.030Z] TOOL RESULT

```
=== PHD
PHD.txt:494:nab [np | N nawa] grandson. nabānazdišt [nb”nzdšt! = Av. nabünazdista-] next of kin. паї [w | M mp] family. ~ag [-R! | N náf(a)] navel. !naft [npt! | = M, N ~] moist, damp; naphtha. *naft [npt'] descendant. nahang [жле] province. *nakkira [nkyl’y] denying, repudiating. ~yih: repudiation. nāl- [wl- | P (n’r-), N ~] groan, complain. nam [nm | N ~] moisture. nám [SM < A £m; m | = M, N ~] name, fame. namad [nmt' | N <) felt. námag [MGLTA < A melt: ттк! | M пто, N пата] book, letter. namak [nmk! | M nmyhk, N ~] salt. namāz [OSGDE < A sgdh; nm’c | = M, N ~] reverence, prostration, prayer. ~ burdan: pay homage. nām-burdār [л?т bwlt?l | N ~] heir, preserving the father's name. nāmčišt [?жт-, ŠMcst'], (pad) ~: in particular, especially. ~ig [-yk'] famous, well known.
PHD.txt:3202:prayer namāz, niyāyišn; ahunawār, āfrīnagān, hūmāst.
PHD.txt:3430:reverence namāz, tarsāgāhīh.
PHD.txt:5164:wardišnīgīh E 4) vo t | wardišnīg Véi ru re 1 wardišn i0 «e ` -om “G\- nam KA nimāy- -AAG A namāz °з^6 \ wimēhgen 1 5^6 nimüdan Viel namak 1361 namad VEGA, nasa, wisē А99 | wisāy- = A235 1 wisān- - ras "wisāndan x 75991 wë = 1693 1 wēxtan! Veras i wisānišnīh AS PO v351 wisānišn vu rudi namiz! «eX wasyar asi wisin(n)- — pai wasyar `Y, 9459 A nask V A35 \ nasruštīli ^ TANT 1
PHD_mackenzie.txt:3651:namad [nmt' IN .......] felt.
PHD_mackenzie.txt:3654:namaz [OSGDE < A sgdh; nm'c I = M, N .......] reverence, prostration,
PHD_mackenzie.txt:10021:namaz                           ~\          nirfsisn
PHD_mackenzie.txt:10030:namad                          \te.G \      warzag
PHD_mackenzie.txt:10047:namaz l
=== HRN 233 area namad
9023:1041. nemed grober Teppich, Filz', ar. LW. namat.
10212:(vergl. ai. ajina- 'Fell'; wa/. ijWj sar. Jein *Filz ; ksl.
```


## [2026-09-07T19:31:23.621Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD nmt felt\"; grep -n \"felt\" SOD_pages.txt | head -20\necho \"=== SOD numeric 240\"; grep -n \"nmt\" SOD_pages.txt | head -20"
}
```


### [2026-09-07T19:31:23.686Z] TOOL RESULT

```
=== SOD nmt felt
1962:Each time a newly published Sogdian text was received, the need would be felt of
2386:        influence, on the Turks of Central Asia was felt in              invent technical terms, in others, to stay too close to
20912:              namb «*nmp, nnp}k                                                 felt
38243: felt 6002                                finger     1044, 1067                     flesh-eater     1358, 10913
=== SOD numeric 240
20827:           nam ^nmy^, nmsy^Ch), nmtMkr'k, nmy, nynVn                        VJ; TSP; GMS 1061; Tales. 467.29; Frag. Len.
20907:             0o)judge                                                      6002 nmt B                                         ju;
20916:                                                                           6003 nmt^kr'k     B                     ^cjUl^T^y
20917:        5990 nmy'wn'y B      (ts^iJ^^j^fLZ.Aitj^^j                              namtat- kare (nmt'tkry) ©<*namtdt, "abuse"
20923:                                                                           6004 nmt'k   S(MD) => nmt
20926:                                                                           6006 nmt'tkry
20927:                                                                                      B =» nmt^tkr'k
```


## [2026-09-07T19:31:33.115Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if '1041. nemed' in p:\n        print('HRN leaf',i,'printed',i-21)\n        j=p.find('1041. nemed'); print(p[max(0,j-600):j+700])\nEOF"
}
```


### [2026-09-07T19:31:34.325Z] TOOL RESULT

```
HRN leaf 254 printed 233
 233 —
kurd. LW. tiem; afy. lünd 'feucht'; bei. wami *Tau,
Neber (252).
1040. nemäfi 'Gebet', TNOi: (Is. 1, 14).
aw. vergl. nemah- 'Gebet; ai. /ia/zias- ; phl v. nawäc
(päz. namaS).
LW. kurd. nimlz, nirm *Gebet'; afy. nmünj ; bei.
namäs, nawäs (251).
Da alle neuiranischen Formen auf die mittel-
persische charakteristische Neubildung natnäc zu-
rückgehen, so halte ich dieselben sämmtlich für
Lehnwörter.
Fr. Müller, (WZKM. 5, 67) nimmt als Grundform
ap. *namascij/ an; aber ap. sc konnte im Neuper-
sischen doch nicht zu ^ werden. Diesen Lautüber-
gang durch np. d^^, niz zu stützen, ist verfehlt.
1041. nemed grober Teppich, Filz', ar. LW. namat.
aw. netnata^j nimata- *Stroh, Gras'; phlv. nanmt
V
'Stroh, Gras*^); grober Teppich' (Säy. näääy. II, 101).
1042. numüdmi 'zeigen; erscheinen', Praes. numäy-em,
numüdar, numün^), Dt^'^NDi: (Qiss. Dan.).
ni + i^fnä-; phlv. n(i)mütan 'zeigen, erscheinen',
n(i)mayisn, n(i)mütär,
oss. d. niniäyun, t. njmam 'rechnen, zählen' (176);
sar. si/n. namäy-em 'sich zeigen, erscheinen*.
1048. numed 'hoffnungslos'.
phlv. anömet 'hoffnungslos'; vergl. ötwed, umed
(No. 109).
Der Bedeutung nach eine Doublette zu na-umed.
Die PehlevT-Schreibung D^DIWN, das doch gewiss
nicht anaumet gelesen werden kann, ergiebt wohl
auch für die Suffixendung I^DW die Lesung -ömaj
```


## [2026-09-07T19:31:34.403Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if '6002 nmt' in p:\n        print('SOD leaf',i,'printed approx',i-66)\n        j=p.find('6002 nmt'); print(p[max(0,j-800):j+800])\nEOF"
}
```


### [2026-09-07T19:31:35.705Z] TOOL RESULT

```
SOD leaf 306 printed approx 240
y-1 B                                                          milder, sweeter
              namay ? ©opt. of nam- ^nm-1                                       Sund. KG pl85
              (to)accept (w,ye<i with neg. (to)refuse)           ^^
              TSP 3.242, 247, 6.116; AVS 91                                6001 nmsy*k(h) M, S           *_a     '^Aj* >jy <*&&**


        5988 nm'y-' M, C                 a>_/ojUS < j-o^jj'j                    namsyak ©<*nams- ©ob. -y ^*nm-2
                                                                                (/ee///i#)despised, humiliated
             nimay ®<*ni-mdya- ©impf. nym^y ^nnVny*                             Sogdica. 2.19, 3; BBB p75, 607; GMS 550, 828 n 1
             0o)judge                                                      6002 nmt B                                         ju;
             GMS 676; STi 48.18, 63.15; GMS 626, 676, 918
                                                                                namat ©<Av. n?mata\ Khot. namata ©ob. -y
        5989 nmb M
                                                                      r
              namb «*nmp, nnp}k                                                 felt
                                                                                TSP 3.229; Benv. BSL 32 p71; Bailey. BSOAS
              dew                                                                  19.53 f; MDiii, nmOk
              BBB 577; GMS 524; ob. -y, BBB 497
                                                                           6003 nmt^kr'k     B
```


## [2026-09-07T19:31:56.525Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN nomad/nome/number/numb\"; grep -n \"^nomad,\\|^nome,\\|^-nomy\\|^number,\\|^numb,\\|^numerous,\\|^numnah\\|^namda\" KLN_1966.txt | head -20\necho \"=== KLN 1026/1048 area\"; grep -n \"namda\\|numdah\\|numnah\\|felt\" KLN_1966.txt | head -20"
}
```


### [2026-09-07T19:31:56.600Z] TOOL RESULT

```
=== KLN nomad/nome/number/numb
24924:namda,  numda,  n.,  a  felt  rug,  a  saddlecloth  {India)
25541:nomad,  n.,  member  of  a  wandering  tribe;  adj. wandering.  —  L.  nomas,  gen.  -adis,  ‘wanderer, member  of  a  pastoral  tribe  that  wander  about with  their  flocks’,  fr.  Gk.  vofia?,  gen.  vo[/a8o;, ‘roaming  about  for  pasture,  wandering  from  one place  to  another’,  fr.  vop.6<;,  ‘land  allotted, pasture;  district,  province’,  which  is  rel.  to ve|xetv,  ‘to  deal  out,  distribute,  allot;  to  allot pasture,  to  pasture,  drive  to  pasture’,  fr.  I.-E. base  *nem-,  ‘to  divide,  distribute,  allot’.  See nimble  and  cp.  Nemesis,  noma,  nome. Derivatives:  nomad-ic,  nomad-ic-al,  adjs.,  no¬ mad-ism.,  n.
25545:nome,  n.,  1)  a  province  in  ancient  Egypt;  2)  a province  in  modem  Greece.  —  F.,  fr.  Gk. vop.6<;,  ‘land  allotted,  pasture;  district,  prov¬ ince’.  See  nomad  and  words  there  referred  to. nomen,  n.,  a  name.  —  L.  See  nominal, nomenciator,  n.,  1)  an  announcer  of  names;  2)  an inventor  of  names,  esp.  of  scientific  names.  — L.  nomenciator,  ‘caller  of  a  name’.  Compounded of  nomen,  ‘name’,  and  calator,  ‘caller,  crier’,  fr.
25752:numb,  adj.  —  ME.  name,  lit.  ‘taken,  seized’,  pp. of  nimen  (fr.  OE.  niman),  ‘to  take’.  See  nim  and nimble.  The  b  in  numb  is  excrescent.  Cp.  benumb. Derivatives:  numb,  tr.  and  intr.  v.,  numb- ness,  n. number,  n.  —  ME.  nombre,  noumbre,  fr.  OF. (=  F.)  nombre,  fr.  L.  numerus  (for  *nomeros) ‘number’,  fr.  I.-E.  base  *nem-,  ‘to  divide,  dis¬ tribute,  allot’.  See  nimble  and  cp.  numeral,  nu¬ meric,  numero,  numerous.
25765:numerous,  adj.  —  L.  numerosus,  ‘numerous’,  fr. numerus.  See  number,  n.,  and  -ous.
=== KLN 1026/1048 area
32:On  this  occasion  I  would  like  to  extend  my  heartfelt  thanks  to  the  Canada  Council,  whose grant  made  it  possible  for  me  to  have  the  manuscript  of  my  dictionary  typed  in  order  to  pre¬ pare  it  for  the  press.  The  generosity  of  this  noble  institution  will  continue  to  serve  for  me  as  a precious  stimulus  for  further  scientific  work.
3027:anvil,  ME.  anvelt,  anfilt,  fr.  OE.  anfilte,  anvil , rel.  to  MDu.  anvilt,  anevilte,  aenbelt,  finebelt, Du.  aanbeeld,  aambeeld,  OHG.  anafalz,  Dan. ambolt,  ‘anvil’,  G.  falzen,  ‘to  fold’  (whence Fah,  ‘groove,  furrow’),  OHG.  vilz,  OE.  felt, ‘felt’ ;  see  felt  L.  pellere,  ‘to  strike’,  is  prob.  not cognate  with  the  above  Teut.  words. Derivative:  anvil,  tr.  v.
5474:Derivatives:  bowl-er,  n.,  round  felt  hat,  bowl-y, adj.,  bent.
6648:caryopilite,  n.,  a  hydrous  manganese  silicate  (min¬ eral.)  —  Compounded  of  caryo-,  Gk.  tuaoc;, ‘felt’,  and  >.(ho c,  'stone'  (see  pile  ‘hair’,  and -lite);  so  called  in  allusion  to  the  felty  appear¬ ance.
13039:enamdar,  n.,  holder  of  an  enam  (India).  —  Hind. in'amdar,  fr.  Pers.  inamdar,  a  hybrid  coined  fr. Arab,  in' dm  (see  prec.  word)  and  Pers.  -ddr, ‘holder,  possessor’.  See  aumildar  and  cp.  words there  referred  to.
14516:fedora,  n.,  a  kind  of  soft  felt  hat.  —  So  called from  Fedora,  a  play  written  by  Victorien  Sardou in  1882.  For  sense  development  cp.  trilby. fee,  n.,  cattle;  property;  money  ( obsol .)  —  ME. feoh,  fr.  OE.  feoh,  ‘cattle,  money,  property, wealth’,  rel.  to  OS.  fehu,  ON.  fe,  Dan.  fie, Swed.  fa,  OFris.  fid,  Du.  vee,  OHG.  feho,  fihu, MHG.  vibe,  vich,  G.  Vieh,  ‘cattle’,  Goth,  faihu, ‘money,  fortune’,  and  cogn.  with  OI.  pasu, pasu,  pasuh,  Avestic  pasu-,  L.  pecu,  ‘cattle’, pecus,  gen .  pecoris,  ‘cattle’,  pecus,  gen.  pecudis, ‘a  single  head  of  cattle’,  pecunia,  ‘money,  prop¬ erty’,  Umbr.  pequo,  Lith.  pekus,  OPruss.  pecku, ‘cattle’,  fr.  I.-E.  base  *peku-,  ‘the  woolly  ani¬ mal’,  whence  ‘sheep,  cattle,  property,  money’. This  base  is  an  enlargement  of  base  *pek-,  ‘to pluck  (wool  or  hair);  hairy,  woolly’,  whence OI.  pdkfman,  ‘eyebrows,  hair’,  Pers.  pashm, ‘wool’.  Arm.  asr,  gen.  asu,  ‘sheep’s  wool,  fleece’, Gk.  x£xog,  rx6xog,  Aeol.  ttcxxoc,  ‘uncombed wool,  fleece’,  Gk.  7x£xsi.v,  Att.  7texxew,  ‘to comb,  shear’,  Gk.  xxe (<;,  gen.  xxev^c  (for *pkten-),  ‘comb’,  L.  pexus,  ‘woolly’,  pectere, ‘to  comb,  shear’,  pecten,  ‘comb’,  pectus,  gen, pectoris,  ‘breast’,  Toch.  A  pdssdm,  B  pascane (dual.),  ‘the  breasts’  (prop,  ‘the  hairy  part  of the  body’),  OE.  feax,  OS.,  OHG.  fahs,  ‘hair’, ON.  fax,  ‘mane’,  OE.  feohtan,  ‘to  fight’  (orig. ‘to  pluck,  pull,  scuffle’).  Cp.  fee,  ‘estate’,  fight, and  the  first  element  in  fellow.  Cp.  also  cteno-, pashm,  paxwax,  Pecora,  pecten,  pectinate,  pec¬ toral,  peculate,  pecuniary,  impecunious,  peignoir, pekin,  ‘a  civilian’,  petto,  poitrel,  and  the  second element  in  parapet.
14548:felstone,  n.,  an  igneous  rock  containing  quartz and  feldspar  (petrogr.)  —  Altered  fr.  G.  Fels- stein,  lit.  ‘stone  of  a  rock’,  fr.  Feh,  ‘rock’,  and Stein,  ‘stone’.  See  fell,  ‘rocky  hill’,  and  stone, felt,  n.  —  OE.  rel.  to  OS.  fill,  OHG.  filz,  MHG. v/fe,  G.  Filz,  fr.  Teut.  *felti-,  ‘something  beaten’. The  same  base  appears  in  the  second  element of  OE.  an-fUte,  OHG.  ana-falz;  see  anvil.  The base  is  prob.  not  cognate  with  L.  pellere,  ‘to strike’  (see  Walde-Hofmann,  LEW.,  II,  p.  277). Cp.  felter,  filter.
14549:Derivatives:  felt,  tr.  and  intr.  v.,  felt-ed,  adj., felt-er,  n.,  felt-ing,  n.,  felt-y,  adj. felter,  tr.  v.  —  OF.  feltrer  (F.  feutrer),  fr.  feltre (F.  feutre),  ‘felt’,  fr.  ML.  feltrum,  filtrumf  felt.
14550:strainer  of  felt’.  See  filter, felucca,  n.,  a  small  coasting  vessel  used  in  the Mediterranean.  —  It.  feluca ,  fr.  Arab,  fulk, ‘ship’,  rel.  to  falak,  ‘circle’,  from  the  base  of fdlaka,  ‘was  round’;  rel.  also  to  Heb.  pelekh, ‘spindle’.  See  S.Fraenkel,  Die  aramaischen Fremdworter  im  Arabischen,  p.212. female,  n.  and  adj.  —  ME.  femele,  femelle,  as¬ similated  in  ending  to  male,  fr.  OF.  femelle,  fr.
14651:fr.  I.-E.  base  *peik-,  ‘evil-minded,  treacherous, hostile’.  See  foe  and  cp.  feud,  ‘enmity’, fez,  n.,  a  red  felt  cap  with  a  long  black  tassel.  — Fr.  Fez ,  a  town  in  Morocco, fiacre,  n.,  a  French  hackney  cab.  —  F.,  fr.  the Hotel  St.  Fiacre,  rue  St.  Antoine,  Paris,  where carriages  were  first  hired  (since  1640).  Fiacre  is the  French  form  of  the  name  of  the  Celtic  saint Fiachra.
14734:filter,  n.  —  ME.,  fr.  OF.  (=  F.)  fibre,  fr.  ML. filtrum,  ‘a  strainer  of  felt’,  fr.  Teut.  *felti-,  ‘felt’. See  felt  and  cp.  felter.
19515:Derivatives:  insensate-ly,  adv.,  insensate-ness,  n. insensibility,  n.  —  Late  L.  insensibilitas,  fr.  L. insensibilis.  See  next  word  and  -ity. insensible,  adj.  —  L.  insensibilis,  ‘that  cannot  be felt,  imperceptible,  insensible’,  fr.  in-,  ‘not’, and  sensibilis.  See  sensible.
23063:massacre,  n.,  indiscriminate  killing.  —  F.,  fr. earlier  mafacre,  rel.  to  OF.  macecle,  macecre, ‘shambles,  butchery’ ;  of  uncertain  origin, massage,  n.  —  F.  massage,  fr.  masser,  'to  mas¬ sage’,  fr.  Arab,  massa,  ’he  felt,  touched’,  which is  rel.  to  Heb.  mashash,  ‘he  felt,  touched’, mishshesh,  ‘he  felt  through,  groped’,  Aram. mashshesh,  ‘he  felt  through,  groped’,  Ethiop. marsasa,  ‘he  felt,  touched’,  Akkad,  mashdshu, ‘to  smear  over,  spread  over’.  The  practice  of massage  has  come  to  Europe  from  the  East  and consisted  originally  in  the  simple  touching  of the  superficial  parts  of  the  body.  This  word  has nothing  to  do  with  Gk.  y-iaae tv,  ‘to  knead’, with  which  it  is  connected  by  most  lexicogra¬ phers.  For  the  ending  see  suff.  -age.
24924:namda,  numda,  n.,  a  felt  rug,  a  saddlecloth  {India)
24925:—  Hind,  namda,  fr.  Pers.  namad,  ‘felt’, namby-pamby,  adj.,  insipid,  feebly  sentimental.
25756:numda,  numdah,  n.  —  See  namda. numen,  n.,  a  divine  spirit;  a  presiding  divinity.  — L.  numen,  ‘divine  will,  divine  command’,  prop, ‘divine  approval  expressed  by  nodding  the
26946:paint,  tr.  and  intr.  v.  —  ME.  peynten,  painten,  fr. OF.  (=  F.)  peint,  pp.  of  peindre,  ‘to  paint’,  fr. L.  pictus,  pp.  of  pingere,  ‘to  paint,  embroider,’ fr.  I.-E.  base  *peig-,  ‘to  adorn  by  coloring  or carving’,  whence  also  OI.  piitgah,  pihgalah, ‘reddish’,  Toch.  A  pik-,  pek-,  B  pink,  paik-,  ‘to write’,  OSlav.  pigii,  ‘variegated’.  Fr.  *peik-,  a related  base,  derive  OI.  pesaldh,  ‘adorned,  dec¬ orated,  lovely’,  pesah,  ‘shape,  form’,  pimsati, ‘cuts,  carves,  adorns’,  Avestic  paes-,  ‘to  adorn’, Gk.  noiKtXo?,  ‘variegated’,  T-ixpoc,  ‘sharp, bitter’,  OHG.,  OS.  felt,  ‘variegated’,  ON.  fd, OHG.  fehjan,  ‘to  adorn’,  OE.  fah,  ‘variegated’, fagian,  ‘to  adorn’,  OSlav.  piSp,  pisati,  Lith. pieSiii,  pieSti,  ‘to  write’,  Lith.  pieSd,  ‘soot’, OSlav.  pistrii,  ‘variegated’,  pisu,  ‘dog’,  pistrogu, ‘trout’.  Cp.  depict,  picric,  pictorial,  picture,  pig¬ ment,  pint,  pinta,  pintado,  poecilo-.  Cp.  also  file, ‘fool’.
28376:petard,  n.,  1)  a  case  filled  with  explosives;  2)  a kind  of  firecracker.  —  F.  petard,  it.  peter  (earlier peter),  ‘to  break  wind’,  fr.  pet,  ‘a  breaking  of wind',  fr.  L.  peditum,  prop.  neut.  pp.  of  pedere, ‘to  break  wind’,  used  as  a  noun.  See  pedicular. Petasites,  n.,  a  genus  of  plants,  the  sweet  colts¬ foot  (bot.)  —  ModL.,  fr.  Gk.  mrceaix-qq,  ‘colts¬ foot’,  fr.  nixatsoQ,  ‘a  broad-brimmed  hat’  (see next  word) ;  so  called  in  allusion  to  its  large leaves.  For  the  ending  see  subst.  suff.  -ite. petasus,  n.,  a  low-crowned,  broad-brimmed  hat worn  by  the  ancient  Greeks.  —  L.,  fr.  Gk.  rre- toKsoq,  ‘broad-brimmed  felt  hat’,  fr.  I.-E.  base *pet-,  ‘to  spread  out’.  See  petalon  and  cp.  prec. word.
28820:Derivative:  pile,  tr.  v.,  to  form  a  pile, pile,  n.,  soft,  fine  hair.  —  ME.,  fr.  L.  pilus,  ‘hair’, rel.  to  pila,  ‘ball,  playing  ball’,  prob.  also  to pilleus,  ‘a  felt  cap’,  and  cogn.  with  Gk.  7ttXo<;, ‘felt’.  Cp.  depilate,  peel,  ‘to  strip  off’,  pelage, pellet,  pelon,  pelota,  pelt,  ‘to  strike’,  Pilea,  pileus, pill,  ‘a  little  ball  of  medicine’,  pill,  ‘to  rob;  to peel’,  pilule,  platoon,  plot,  ‘to  press  into  cakes’, plot,  ‘conspiracy’,  pluck,  plush,  poilu,  and  the second  element  in  caryopilite,  caterpillar,  horri- pilate.
28822:Pilea,  n.,  a  genus  of  plants,  the  richweed  (bot.)  — ModL.,  fr.  L.  pileus,  more  exactly  pilleus,  ‘felt cap’.  See  pileus.
```


## [2026-09-07T19:31:57.690Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN pray\"; grep -n \"9.9[0-9] \\|PRAY\\b\" SYN.txt | head -20\necho \"=== WLD Bd2 nem\"; grep -n \"nem-\\|námas\\|Reisig\" incoming/WLD/WLD_Bd2_pages.txt | head -20"
}
```


### [2026-09-07T19:31:57.764Z] TOOL RESULT

```
=== SYN pray
2255:| CHAPTER 2 MANKIND: SEX, AGE, FAMILY RELATIONSHIP 9.1 Man! (Human Being) 2.47 GRANDMOTHER 9.91 Man? (vs. Woman) 2.48 GRANDSON 2.92 Woman 2.49 GRANDDAUGHTER 2.93 MALE’ 2.51 UNcLE 9.94 TeMALE 2.52 AUNT 9.942 Sex 2.53 NEPHEW | 9.25 Boy 2.54 NIECE 9.26 GIRL 2.55 CousIN | 2.27 CHILD 2.56 ANCESTORS 2.28 INFANT 2.57 DESCENDANTS 231 HUSBAND 2.61 Fatuer-1n-Law ~ 2.32 Wire 2.62 Morser-in-Law 2.33 Marry 2.63 Son-1n-Law 2.34 Marriage; WEDDING 2.64 DauGuHTEr-in-LAw 2.35 FaTHER 2.65 BrotuEr-in-Law 2.36 MoTHER 2.66 SisteR-1n-Law | 2.37 PARENTS 2.71 STEPFATHER 2.41 Son 2.72 STEPMOTHER 2.42 Daucuter 2.73 STEPSoN | 2.43 Cuiup (Son or Daughter) 2.74 STEPDAUGHTER 2.44 BroTuHEr 2.75 ORPHAN 2.45 SISTER 2.76 Wipow 2.452 BrotHEer(s) AND SISTER(s) 2.81 RELATIVES 2.46 GRANDFATHER 2.82 FamiIny 2.1 MAN! (Human Being) oy ae por Goth. manna Lith.  Zmogus, pl. Zmonés iy ae eee s oN maor, gumi Lett. cilveks It. heinb - an. —menneske ChSl. elovékit Tr. iter an menniska SCr. Eoujek Sp. hombre ME man(n), guma Boh. tlovtk Rum. om man Pol. czlowiek Tr. duine NE man Russ. elovek Nir. duine Du. mensch Skt.  manu-, purusa- W. dyn OHG man, mannisco, gomo Av. __masya-, masyaka-, Br. den MHG mensch OPers. martiya- NHG mensch
4397:Sp. cerdo ‘hog’, prob. of Basque orig. REW 9696 f.
13545:(as Artist) 9.943 Firrine, SurraBLe PAINTER E 966 PAINTING, icru® 9.95 Can, May 987 (sb.) , 9.96 Hasy nT : (@ 988 Fe (vb. ‘Paint 6 House’) 9.97 Dirricuir 989 Tans 9.98 Try! (Make Trial of, Test) v BE 9.99 Try? (Attempt, Endeavor) Me pecow® 9.992 Way, MANNER a NzED, ‘im 9.993 HarrEn T, UST 9,94 QuGH ? 911 DO, MAKE ; Goth. taujan, waurkjan Lith. (pra)daryti, veikti
15952:9.90 THING ee mpayua, Xpijna Goth. wazthts Lith.  daiktas Tat, “erHa (Pop. mp@ua) ON — hlutr Lett. lieta It, del Dan. ting, sag ChSl. vest Fr. chos Sw. sak, ting SCr.  stvar Sp. etd OE ping Boh.  vée Rum, luery ME _ thing Pol. —_rzecz Ir, ni, rat NE thing Russ. _veSé’, delo a: ni, rud ae ant nae Skt. vastu- , th inc, sacha Av. Br, ee MHG dine, sache iegtacr, NHG  sache, ding an har eral notion ae beamore vague gen- In several cases, partly due to se- *Y act, event, or ae thing’, covering | mantic borrowing, the development has ed on g ca object. Itis | been through ‘subject of litigation’. And most common] ‘eae notions, Other sources are ‘act, deed, work, e aN act, event, ee te G generalization share, thing needed, property’, ete. The oe ° 8 material ob; ir ls earlier than | use of the neuter of the indefinite pro- Ords listeg are stil] ne A few of the | noun for ‘anything, something’ and, with teria] object ot used for ‘thing’ negative, ‘nothing’ (Grk. 7, ot7., Lat.
15985:9.91 BE 1, etc. Goth. wisan, ist, was Lith. biti, esu, yra tu eas etc. ON vera, er, var Lett. but, esmu, tr N SC, reat fui, etc. Dan. va@re, er, var ChSl. byli, Jeslit i Bice é fui, stato Sw. vara, Gr, var SCr. biti, jest qh a e 1 jus, aé OE wesan, béon, béo(m), Boh. —byli, Je(st) | Sp, _ser, estar, es, ful, sido, is, wes Pol. _byé, jest B estado ME _be(n), 2s, was Russ. byt’, est’ Rum. fi, teste, ful NE be, zs, was Skt. as-, bha- Ir. tau, biuu, buith Du. zujn, ben, zs, was Av. ah-, bi- Nir. taim, bim, beith OHG_ wesan, bim, ist, was W. bod, ys, yw MHG wesen, bin, ist, was Br. _beza, bez NHG sein, bin, ist, war
16002:9.92 BECOME
16058:Grk 9.93 NEED, NECESSITY Ae ° NG a aren Goth. aurfts,naups Lith. _reikalas Tat, opus, vdyny e ON Aorf, purft, naud(r) Lett. vajadziba : cae nN Dan. _ behov, nd, ngdvendig- ChSl. potréba, nazda, ne- Hed) e881 the Cant? het volj ®. alae Sw. behov, néd, nédvan- SCr.  potreba, nuzda, ne- Un. trebui dighet volja Ir, ett OE pearf, néad Boh. otreba, nouze Nk. gabhadh, ps ME _snede, necessite Pol.  potrzeba, koniecznosé Bigin” ruachtanag, NE need, necessily Russ. polrebnost', nadob- He Qngen, rhaig Du. behoefle, nood nost" nuzda, neob- "  ezomm red OHG durft, nat chodimost ; MHG durft, nat Skt.  kartavya-, dvacgyaka-
16113:640 9.94 OUGHT, MUST (38sg.) rk. M, Get, ddeldet, Goth. skal Lith. reikia, tur, $ sae al et ON skal, verdr, @ with fut. of poe NG apie, dvayxn elvat Dan. b¢r, skal, maa Lett. vajaga (ir), phrase Lat. opus est, oportel, dé- Sw. bdr, mdste with fut. of ‘be’ bel, necesse est OE sceal, mot ChSl.  dlziny Jestii, podo- It. dovrebbe, deve, biso- ME shal, oughte, mote bajetit | gna ' NE ought, should, must, SCr. treba, mora Fr. devrait, doit, il faut has to Boh. must, md | Sp. debiera, debe, hay que, Du. (behoort) moet Pol. powinienes, trzeh A tiene que, ha de OHG - scal, muoz musi ! Rum.  ftrebue MHG sol, muoz Russ. dolien, nado, nadobno Tr. ts &cen NHG sollte, darf, muss Skt. (arh-) Nir. ba cheart, ba chdir, is Ay. eee éigin
16275:9.95 CAN, MAY (3 sg.)
16332:9.96 EASY Grk. — padtos, ebxodos Goth. azetizd (comp.) Lith. lengvas NG eixodos ON aud- Lett.  viegls Lat. facilis Dan. let ChSl. udobt It. Sacile Sw. latt SCr. lak Fr. facile OE ape, éapelic, léoht Boh. snadny Sp. facil ME eth, light, aisy Pol.  latwy Rum. ugor, lesne : NE easy Russ. legkij Tr. asse, réid, soirb Du. —_gemakkelijk Skt.  su-kara-, etc. Nir. furus OHG édi Av. W. hawdd MHG ade Br. aes NHG leicht
16385:9.97 DIFFICULT
16436:9.98 TRY} (= Make Trial of, Test) Grk.  doxtpatw, retpaw Goth. kiusan, kausjan, Lith. bandyti, méginti NG Soxtpatw fraisan Lett. még’inat, méedzinat Lat. experiri, temptare, ON reyna, freista ChSl.  iskusiti probare Dan. prgve SCr. pokuSati, probati It. provare, tentare Sw. préva Boh.  skouSeti, pokusiti Fr. essayer, éprouver, OE fandiun, costian Pol. prébowaé tenler ME sfonde, prove, assay, Russ. probovat! Sp. probar essay, trie Skt. —_pariks- Rum. incerca NE try Av. a; Ir. promaim Du. probeeren, beproeven Nir. fromhaim, triailim OHG  corén, costén W. profi MHG prueven, versuochen Br. esaat NHG probieren, prifen, versuchen
16485:9.99 TRY? (Try to = Attempt, Endeavor)
=== WLD Bd2 nem
8832:bhasqo-), auch kann die Gdbed. eine ganz andere gewesen sein, als „Reisig-
13115:„Gebu8ch'‘ (vgl. norw. bras „Reisig“ von *blires- „bersten“).         Eine nas.
21807:330                                nebh-    — nem-
21849:1* nem- „zuteilen,    nehmen‘' (aus ,,sich zuteilen“ oder von der gemeinsamen
21915:   Urspriingliche Gleichheit von nem- „zuteilen“ (etwa als „beibiegen“?)
21916:mit nem- „biegen‘' ist nicht wahrscheinlich zu machen, auch nicht in der
21918:   Neben nem- „zuteilen“ stehen mit ahnlicher Bed. iem- „halten'^ und em-
21921:iiberzeugend oder z. T. sicher verfehlt. iem-:nem- sucht Schmidt Krit. 154ff.
21923:keine idg. Yorgeschichte als ni- hat (s.u. em- „nehmen“). nem- deutet Pick I ^
21925:hingegen Osthoff Pf. 142 ff., IP. 5, 321 (m. Lit.) geht von nem- aus und
21935: 2,   nem- „biegen'\
21960:Gleichsetzbarkeit mit av. nsmafa-; 8ie alle eher zu nem- „zuteilen“; gall.
22271:8g.     f.),   nem-pe „denn doch, doch ja, allerdings, naturlich“; slav. na „da
25370:Maispflanzen‘‘, poln. ioboz, iobozie, lobuzie, labuz ie „Stengel, Stoppeln, Reisig,
29597:zeugend dagegen Ehrlich TJnters. 75: sae-pe, wie nem-pe^ mit *sai „irgend-
33299:i^sarp-men),sarmentum abgeschneiteltes Reis, Reisig“; mir. serr „Sichel‘‘,
37287:PI. „Reisigbeseii‘^,scopio^ ~onis „der Stiel, an dem die Beeren dei* Wein-
37966:hris jjReis, Rute, Reisig,   Gebusch“ („schwingende, sich biegende Zweige^'
37991:gultum“, nhd. Bispe „Reisig, Buschwerk, Biischel, Biindel, biischliger
39068:  Gr. Tidgcfog „durres Reisig, Spreu“,    HdQ(p'i] ,trockenes Holz, Heu“, xdqcpoy
```


## [2026-09-07T19:32:11.471Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\ntargets=['namda,  numda','nomad,  n.,  member','numb,  adj.','nimble,  adj']\n# find leaf index per target\noff=0\nlineno=1\nfor i,p in enumerate(pages):\n    for tg in targets:\n        if tg in p:\n            print(tg,'-> leaf',i,'approx printed pages',2*(i-12),2*(i-12)+1)\nEOF\ngrep -n \"^nimble,\" KLN_1966.txt | head"
}
```


### [2026-09-07T19:32:12.844Z] TOOL RESULT

```
namda,  numda -> leaf 549 approx printed pages 1074 1075
nimble,  adj -> leaf 561 approx printed pages 1098 1099
nomad,  n.,  member -> leaf 563 approx printed pages 1102 1103
numb,  adj. -> leaf 567 approx printed pages 1110 1111
25439:nimble,  adj.,  quick,  agile,  alert.  —  ME.  nimel, ‘quick,  nimble’,  prob.  with  the  original  mean¬ ing  ‘quick  to  take’,  and  formed  with  adj.  suff. -le  fr.  nimen,  ‘to  take’,  fr.  OE.  niman,  which  is rel.  to  OS.,  ODu.,  Goth,  niman,  ON.  nema, OFris.  nema,  nima,  OHG.  neman,  MHG.  nemen, G.  nehmen,  ‘to  take’,  fr.  I.-E.  base  *nem-,  ‘to divide,  distribute,  allot’,  whence  also  Avestic rfmah-,  ‘loan’,  Gk.  vlp.siv,  ‘to  deal  out,  dis¬ tribute,  allot’,  vepEm?,  ‘just  indignation,  jeal¬ ousy,  vengeance  (esp.  of  the  gods) ,  vop.6<;, ‘land  allotted,  pasture;  district,  province’, vop.o?,  ‘anything  allotted  or  assigned;  usage, custom;  law’,  L.  numerus,  ‘number’,  Lith.  nuo- ma ,  nudmas,  Lett,  nudma,  ‘rent,  interest’,  Mir. nos,  MBret.  naux,  ‘custom,  usage’.  See  numb, and  cp.  nim.  Cp.  also  Nemesis,  noma,  nomad, nome,  Nomeus,  Nomic,  nomistic,  nomo-,  -nomy, number,  numeral,  numeric,  numismatic,  num¬ mary,  nummular,  and  the  second  element  in gnome,  ‘a  dwarfish  person’,  and  in  withernam. The  b  in  nim-b-le  is  intrusive;  cp.  grumble, ramble.
```


## [2026-09-07T19:32:22.988Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(545,570):\n    nums=re.findall(r'\\b1[01]\\d\\d\\b',pages[i][:400])\n    print(i, nums[:6], repr(pages[i][:80].replace('\\n',' ')))\nEOF"
}
```


### [2026-09-07T19:32:24.337Z] TOOL RESULT

```
545 [] 'urrain’,  which  also  derive  fr. VL.  *morire.  Cp.  murrina. murre,  n.,  1) '
546 [] 'appoint,  something;  to  have  room; to  be  able;  to  be  obliged’,  d-degree'
547 [] '  ;  see  man.  Peas¬ ants  were  called  ‘little  men  ,  because  according to'
548 [] "d  fr  prec.  word  with  suff.  -aceae. myricaceous,  adj.  —  See  prec.  w'or"
549 [] "l  cured  of  leprosy  by  Elisha.  —  Heb. Na'aman,  lit.  ‘pleasantness’,  fro"
550 [] ' B  hem,  Hitt,  laman  (formed  with  dissim¬ ilation  fr.  *naman),  Arm.  a  '
551 [] '  of  coconut  shells, narial,  adj.,  pertaining  to  the  nares.  —  Formed fr'
552 [] 'us,  ‘birth,  des¬ cent,  origin,  race,  sort,  kind,  class’.  See  genus and '
553 [] 'd  of  navis,  ‘ship’,  and agere,  ‘to  set  in  motion,  drive,  lead,  conduc'
554 [] 'n.,  that  part  of  the  body  which  joins  the head  to  the  trunk;  the  na'
555 [] ' MF.  (=  F.)  negatif  (fern. negative),  fr.  OF.  negatif,  fr.  L.  negativu'
556 [] ' for  *ver og,  fr.  I.-E. •newos,  ‘new’,  whence  also  Goth,  niujis,  OE. ne'
557 [] '.  ve< pp4c,  ‘kidney’  (see  ne¬ phro-),  and  suff.  -it,  which  goes  back  '
558 [] '�blessed’.  See  nostal¬ gia. Nestorian,  adj.,  1)  pertaining  to  Nestonus,  '
559 [] " corpuscles  that is  neither  oxyphile  nor  basophile');  a  hybrid coined  by"
560 [] 's  (in  a  certain  manner); one  who  deals  (with  a  certain  topic)’.  See  '
561 [] '�. Nilotic,  adj.,  pertaining  to  the  Nile,  the  Nile  re¬ gion  or  the  Ne'
562 [] '  niter, nitro,  adj.,  containing  nitrogen.  —  From  nitro-. nitrogen,  n.,  '
563 [] ' See  nodule  and  -ous. nodus,  n.,  knot;  difficulty,  complication.  —  L. n'
564 [] '  before  the  ides’,  and  cp. words  there  referred  to. nonagon,  n.,  a  pl'
565 [] 'orman-ize,  intr. and  tr.  v.,  Norman-iz-ation,  n. Norn,  n.,  one  of  the  '
566 [] '  Sir  Richard  Owen  (1804-92)  in  1848  fr. vcoxo.;  (also  vcotov),  ‘the  b'
567 [] ' alpha¬ bet. —  Gk.  vu,  shortened  fr.  Heb.  nun,  name  of the  letter  n.  '
568 [] ' numeralis,  ‘of  numbers’,  fr.  L.  numerus. See  number,  n.,  and  adj.  suf'
569 [] '), contraction  of  *noven-dinom,  ‘nine  days’,  fr. novem,  ‘nine’,  and  *din'
```


## [2026-09-07T19:32:36.216Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1971.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if 'nimble' in p or 'namda' in p or ('nomad' in p and 'wandering' in p):\n        print(i, repr(p[:120].replace('\\n',' ')))\nEOF"
}
```


### [2026-09-07T19:32:37.466Z] TOOL RESULT

```
leaves 1
0 "Klein’s Comprehensive  Etymological Dictionary  of the English Language     UNABRIDGED ONL' r VOLU\\1E EDITION     ELSEVI"
```


## [2026-09-07T19:32:42.261Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1971.txt',encoding='utf-8',errors='replace').read()\nfor kw in ['nimble, adj','namda','nomad, n']:\n    i=t.find(kw)\n    print('==',kw,i)\n    if i>0:\n        # find nearest preceding standalone page number\n        seg=t[max(0,i-6000):i]\n        nums=re.findall(r'\\n\\s*(1[0-9]{3})\\s*\\n',seg)\n        print('preceding page nums:',nums[-5:])\n        print(t[i:i+300].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T19:32:43.634Z] TOOL RESULT

```
== nimble, adj 5822789
preceding page nums: []
nimble, adj., quick, agile, alert. — ME. nimel ,  ‘quick, nimble’, prob. with the original mean-  ing ‘quick to take’, and formed with adj. suff.  -le fr. nimen , ‘to take’, fr. OE. niman, which is  rel. to OS., ODu., Goth, niman, ON. nema,  OFris. nema, nima , OHG. neman, MHG. nemen,  G. nehmen, ‘t
== namda 2905370
preceding page nums: []
namdar, n., holder of an enam (India). — *Hind.  in'amddr, fr. Pers. inamdar , a hybrid coined fr.  Arab, in' dm (see prec. word) and Pers. -dar,  ‘holder, possessor’. See aumitdar and cp. words  there referred to.   enamel, tr. v. — ME. enamelen , fr. AF. ena-  mayller, fr. ist en- and amayl, fr. O
== nomad, n 5848186
preceding page nums: []
nomad, n., member of a wandering tribe; adj.  wandering. — L. nomas , gen. - adis , ‘wanderer,  member of a pastoral tribe that wander about  with their flocks’, fr. Gk. vop.dc:;, gen. vopaSo:;,  ‘roaming about for pasture, wandering from one  place to another’, fr. vop.6?, ‘land allotted,  pasture;
```


## [2026-09-07T19:32:54.477Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[568]\nprint(p[:3000])\nEOF"
}
```


### [2026-09-07T19:32:55.752Z] TOOL RESULT

```
 W. haidd, Br. heiz ‘barley’. Walde-P. 2.454.
8.48 WHEAT
Goth. hwwatteis Lith.  kvietiet, pirat rips ON _hweiti Lett. kvieSi, par'i ae Dan. hvede SOs. plone hs w.  hvele r.  psenica f hang) at On hw@te Boh.  piSenice peers ME whele Pol. pszenica fie NE wheat Russ. pSenica
? Er iechl tuirend Du. tarwe, weit Skt. godhtima- cruithneacht OHG weizz Av. gantuma- gwenith MHG weizze
NHG weizen
member Ir. -necht, W. -nith, Br. -niz : W. nithio, Br. niza ‘winnow’ (this : Lith. n(d)ekoti ‘winnow in a trough’, etc. Walde-P. 2.321), hence ‘wheat’ as ‘grain for winnowing’, like Lat. triticum as ‘srain for threshing’. First part of Ir. cruitnecht : Ir. cruth ‘red’, with refer- ence to the old red wheat of Ireland. First part of W. gwenith, Br. gwiniz prob. (despite the nm for nn) : gwynn, Br. gwenn ‘white’ (cf. Goth. hwaitets : hweits, below, 4). For full discussion, ef. Loth, RC 41.193 ff.
Ir. tuirend, etym. dub., perh. a epd. of rind ‘point’ and first used of a special kind of wheat. Loth, RC 41.199 ff.
4. Goth. hwaiteis, OE hw@te, etc., general Gmc., so called from the white meal therefrom: Goth. hweits, etc. ‘white’ (15.64). Walde-P. 1.469 f. Feist 280.
Du. tarwe (more popular than weit), MDu. tarewe, prob. (as first applied to some rank species of wheat?) : ME, NE tare ‘vetch, weed’, Skt. durva- ‘panic-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
516 SELECTED INDO-EUROPEAN SYNONYMS
grass’, also prob. Lith. dirva ‘field’ (8.12). Walde-P. 1.803. Franck-v. W. 689.
5. Lith. kvieciet, Lett. kviest, fr. Gmc. (Goth. hwaiteis, etc., above, 4).
Lith. pirat, Lett. piir’?, above, 1.
6. ChSI. pisenica, SCr., Russ. psenica, Boh. pSenice, Pol. pszenica, orig. ‘grain
destined for grinding’ : ChS]. Pichat; ‘strike’, pitSeno ‘meal’, I, titan ‘crush’, ete. Walde-P. 2.1. :
7. Skt. godhtima-, by Pop. etym, cpd. of go- ‘cow’ and dhiima- ‘smoke’) for *gandhuma- = Ay. gantuma-, NPerg gandum ‘wheat’, root connection? Barth, 493. Hiibschmann, Pers. Stud. Ofna
8.44 BARLEY Grk. «pid Goth. barizeins (adj.) Lith. mieSiat NG xpiOape ON bygg, barr Lett.  miezi Lat. hordeum Dan. byg ChSl.  jeetnénit, jetint (adj.) It. orzo Sw. bjugg, korn SCr.  jetam Fr, orge OE bere, berlic (béow) Boh. jeémen Sp. cebada ME bere, barli Pol. Jeczmien Rum. rz NE barley Russ. jaémen! Ir. eorna Du. __gerst Skt. —_ yava- Nir. corna OHG  gersta Av. Steiis W. haidd MHG §gerste Br. heiz NHG gerste
Apart from the inherited group, and some with specialization from ‘grain’ or ‘fodder, crop’, several words for ‘barley’ are from sources reflecting its sharp, prickly form.
1. IE *gherzd(h)-, *ghrzd(h)-, root connection uncertain and phonetic de- velopment in part obscure. Walde-P. 1.611. Ernout-M. 459, Walde-H. 1.657.
Grk. xpi#;, NG KpOapt; Lat. hordeum (> It. orzo, Fy. orge, Rum. orz); Du. gerst, OHG gersta, MHG, NHG gerste; (Alb. dridhé ‘grain’,
2
```


## [2026-09-07T19:33:02.051Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if re.search(r'\\b54[3-6]\\s+SELECTED INDO-EUROPEAN SYNONYMS', p) or re.search(r'RELIGION|WORSHIP|PRAY', p):\n        m=re.findall(r'\\b(\\d{3})\\s+SELECTED INDO-EUROPEAN SYNONYMS|SELECTED INDO-EUROPEAN SYNONYMS\\s+(\\d{3})',p)\n        if m: print(i,m[:3], p[:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T19:33:03.561Z] TOOL RESULT

```
595 [('544', '')] gitized by Arya Samaj Foundation Chennai and eGangotri EOUS 
597 [('546', '')] e together’, and | is not quotable in this sense. The adj. j
```


## [2026-09-07T19:33:06.814Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[594][-1500:])\nprint('=========594/595 boundary=========')\nprint(t[595][:3500])\nEOF"
}
```


### [2026-09-07T19:33:08.275Z] TOOL RESULT

```
 *kam- in Skt. kmarati (Dhatup.) ‘is crooked’, Av. kamarda- ‘girdle, Grk. xayépa ‘vault’, ete. Walde- P. 1.350.
Grk. \vyitw ‘bend, twist’ like a withe (cf. Abyos ‘“withe’), in NG the usual pop. word for ‘bend’ (trans. and intr.) : Lith. lugnas ‘pliable’, ON lykna ‘bend the knee’, ON lokkr, OE loce ‘lock of hair, curl’. Walde-P. 2.413 f.
(hence *fleclicare > fléchir), etym.? Er- Walde-H. 1.514 f. amillscheg 424. . > It. curvare, Fr. cour- : ), deriv. of curvus ‘bent, ropa, kuptés, Lith. ‘gS Russ. krivad, en ve alls reid) «it, widespread root CO = ee mie? 9.568 ff. Ernout-M.
ectere Lat. fl ir.
ihe Oe ena) es ‘r. plier (both also ‘told ),
iH Eee iat plicare ‘fold’ (9.15). Ben, tncovoia, fr. Slavic, of. Chl. kovali hammer, forge’ (9.61), EAMES:
od-kova, SCr. pot-kova horseshoe ; ra development through ‘bend in the form of a horseshoe’. Tiktin 790.
3. Ir, crommaim, Br. kromma derivs. of Ir. cromm, Br. kromm ‘crooked, bent’ (12.74).
Ir. fillim, also and orig. ‘fold’ (9.15). Nir. camaim deriv. of camm ‘crooked, bent? (12.74).
Ir, NI. labaim deriv. of Ir. lab ‘a loop, bend’, formerly taken as loanword fr, NE loop, but by Zupitza, KZ 36.244, : ch with ON laupr, OF léap ‘basket’.
W. plygu, Br. plega, also and ori
old’ (9.15), : ees _£ Goth. (ga)biugan (OE bigan ‘bow’ intr.), ME bowe (trans. and intr. due to ae with forms of OF bygan, cf. 8. bow, vb.), Du. buigen, OHG
’; here also pr
formation, ON , Sw. béja, OF % bégan), OHG bougen, atch a beugen (with idio-
OU rigid, di erentiation
Di
=========594/595 boundary=========
gitized by Arya Samaj Foundation Chennai and eGangotri
EOUS PHYSICAL ACTS, ETC. 543
from biegen; cf. Paul, Deutsches Wtb. s.v. biegen).
ON sveigja : svergr ‘flexible’, svigna ‘sive way’, fr. an extension of IE, *swe7- in words with the notion of ‘bend, turn, swing’. Walde-P. 2.518 ff. Falk-Torp 1212.
ON benda ‘bend a bow, bend’ (OE ben- dan ‘bind, bend a bow’), ME bende, NE bend, fr. Gme. *bandjan, deriv. of *bandja- (OE bend, ON band ‘band’), fr. the root of Goth., OE bindan ‘bind’, etc. (9.16). The semantic development is then ‘bind’, ‘restrain with a bond’, ‘Testrain a bent bow’, ‘bend a bow’, ‘make bow-shaped’, ‘bend’. NED s.v. bend, vb.
Sw. kréka deriv. of krok ‘a hook, curve, bend’: Dan. krog, ON krokr ‘hook’ (> ME, NE crook), OHG krako ‘hooked tool’, etc. Walde-P. 1.593 f. Falk-Torp 581.
MHG lenken : ON hlekkr ‘ring, link’, OE hlencan pl. ‘chain-armor’, ete. Walde-P. 1.498. Falk-Torp 676.
5. Lith. (pa)lenkiz, Lett. liekt, fre- quent. lwocit, ChSl. sti-lestz, -leka, (prob. lecett ‘set snares’, etc.) : Lith. linktt ‘bend’ intr., Lett. kt id., liks ‘curved’, ChSl. Iqkt ‘a bow’, ON lengja, OE -loh ‘strap’, fr. IE *lenk-. Walde-P. 2.435. Berneker 707 f.
6. (ChSI. st-giinati, pré-gybati ‘fold’), SCr. pregnuti, pregibati, Boh. ohnoutt, ohybati, Pol. giaé, nagiaé, Russ. gnut’, sgibat', fr. a Slavic root *gtib-, *gyb- : Lett. gubt ‘bend’ (intr.), perh. OF géap ‘crooked’, ete. (or gub- by transposition fr. bhug- in Skt. bhuj-?). Walde-P. 1.567 f. Berneker 366, 373. Briickner 140.
7. Skt. avic- (cf. attka- ‘bend, hook’): Grk. éyxév ‘elbow’, ayxidos ‘curved’, Lat. uncus ‘hook’, OE angel ‘hook’, ete. (12.75). Walde-P. 1.60f. Walde-H. 1.46.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
}
Digitized by Arya Samaj Foundation Chennai and eGangotri
544 SELECTED INDO-EUROPEAN SYNONYMS
Skt. namati mostly intr., Av. namaiti intr., caus. Skt. nd@mayati, Av. ndmayeiti trans., Skt. namas-, Av. namah- ‘bend- ing, homage’, Toch. ndm- ‘incline, bow’
(SSS 446), further connection, Walde-P. 2.331 f. Skt. bhuj- : Goth. biugan,
t (above, 4). cue
9.15 FOLD (vb. trans.)
Grk. — xrbcow Goth. falpan Lith. — stulpuoti
NG Sirddvw ON falda Lett. saluocit
Lat. _plicdre Dan. folde ChSI. — stigiingti, stigybati It. piegare Sw. vika SCr.  saviti
Fy. plier OE fealdan Boh. _ skladati, zahybat; Sp. plegar, doblar ME folde Pol. — fatdowaé
Rum. indot NE fold Russ. skladyvat!
Ir. fillim Du. vouwen Skt. Sa
Nir. fillim OHG  faldan, faltan Av.
W. plygu MHG alten
Br. plega NHG falten
For relations between ‘fold’ and ‘bend’, see 9.14. Among other semantic sources are ‘double, turn, wind, put to- gether’.
1. Grk. rricow, with wrrvx7 ‘a fold’, perh. fr. *r-vx-, a cpd., like Skt. py- uksna- ‘bow-case’, with prefix *pz besi
```


## [2026-09-07T19:33:17.018Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '21935,21975p' incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-07T19:33:17.067Z] TOOL RESULT

```
 2,   nem- „biegen'\
      Ai. ndynas- n.      = av. nmnah- n. „Yerbeugung =yerehrung, Huldigung^^,
 ah namati „beugt              sich,   neigt   sich,   beugt, biegt“   (kaus.   ndmayati), av.
      Walde,   Etymologischea Wi)rterbucb. II.                                        22
                  '




332                                ner-, aner- (ener-?)



mmaiti „beugt sich (weg)“ {namaiti, kaus. namayeiti), mit apa-, fra „ent-
fliehen“; Pto. ai. natd- ,,gebogen“;
   av. ndmaia- m. (auch nimafa-) „Rei8ig“ (*„biegsam, sich heranterbeugend“,
8. Bartholomae Airan. Wb. 1068).
   Gr. veyog      to yvvaixelov atdoTov xal vanog xal to tov ocp&aXyov xolXov
                                            '             '



Hes.; viel zweifelhafter veyog n. „Weideplatz“ = lat. nemus,- oris „Ham,
Wald mit Triften und Weiden, Baumgruppe, Lu8twald“, sowie gall, vsyrjiov,
air. nemed „sacellum“ und afrank. nimid „Weide“, trotz ihrer formalen
Gleichsetzbarkeit mit av. nsmafa-; 8ie alle eher zu nem- „zuteilen“; gall.
nanfo „valle“, trinanto „drei Taler“, Nanfuates, cymr. bret. nant „Yalli8“
(fnni-tu-, vgl. Ptc. ai. natd- aus nmtd-)-, aber air.         mm
                                                        „Himmel“, (n. es-St.)
nir. neamh, cymr. com nef ds., acorn, cam niuet „Regenbogen“ kaum als
,,W6lbung“ hieher, 8ondern nach Duvau Rc. 22, 82f., Pederaen KG. I 255,
387 mit schon air. y iiiv f = abg. mbo.
   S. Pick I* 97, II^ 192, III* 294 und bes. Curtius 313f., Johansson IP. 2,
54 ff. mit Lit., der aber nicht iiberzeugend auch ai. ndka- m. „Himmels-
w61bung“, gr. vdnrj, vdnog „Tal, Waldschlucht“ heranzieht.


1. ner-,  aner- (aner-?) Mann.
   Ai. ndr- {nd) „Mann, Mensch“, av. nar- {na) ds. (ai. nara-h, av. nara-
nach dem Acc. naram, nardm neugebildet) ai. wdn, av. ncdri „Frau“ (erst
                                                    ;
```


## [2026-09-07T19:33:27.149Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor i,l in enumerate(lines):\n    if re.match(r'^\\s*23[45]\\s{4,}\\S', l):\n        print(i, repr(l))\nEOF"
}
```


### [2026-09-07T19:33:28.571Z] TOOL RESULT

```
15282 '\x0c234                                mand-   — ‘^mari'
```


## [2026-09-07T19:33:39.059Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSF namaz\"; grep -n \"نماز\" FSF_pages.txt | head -10\necho \"=== TAD namus\"; grep -n \"ناموس\" TAD_pages.txt AFM_pages.txt 2>/dev/null | head -10\necho \"=== FVQ namus\"; grep -n -i \"nāmūs\\|namus\" FVQ.txt | head -10\necho \"=== LKT namus/numero\"; grep -n -i \"namus\\|nomos\\|numero\" LKT.txt | head -10"
}
```


### [2026-09-07T19:33:39.156Z] TOOL RESULT

```
=== FSF namaz
3274:     ‫[بیژن] پیاده شد از اسب و روی زمین‬        ‫در نمازم خم ابروی تو با یاد آمد‬
3609:                            ‫بمانم ت‬                  ‫نماز‬          ‫برآمد‪ .‬پری روی [رو‬
4208: ‫کرده بود» زمانی به نماز خواندن» زمانی‬                                ‫(اسدی ‪:)۱۸۱-۵۶‬‬
5293:        ‫تو از بسدتنان بسودی و بی‌بنان‬            ‫که همی بلبل بر سرو کندبانگ نماز‬
7489:                        ‫پنهان داشتن‪ .‬دنهفتن‪:‬‬                   ‫بیامد خحرامان و بردش نماز‬
9387:                           ‫جهنده یگزرنده‪:‬‬            ‫بی‌طاق ابروی تو نماز مرا جواز‬
14002:     ‫گودرز به پیران ویسه پیام می‌فرستد‪:‬‬                        ‫بیامد بر سام و بردش نماز‬
16531:                        ‫(اسدی ‪:)۳۵۲-۴۸‬‬                            ‫غریوید بسیار و بردش نماز‬
19258:                             ‫نماز» حق‪:)...‬‬            ‫شبیگر ز گل فاختگان بانگ برآرند‬
19287:               ‫اگر ماندست لختی زندگانی‬     ‫تاریخ سیستان ‪ :)۶۸‬بامداد برحاست نماز‬
=== TAD namus
TAD_pages.txt:2740:                     ‫معناه عادةوشربعة وسّنة‬         ‫ناموس ‪ -‬ووناني ‪89‬‬
AFM_pages.txt:3944:3 6 الاراعى ` ܢܡܩܐ و شربه اليونالي 94 اي الناموس
=== FVQ namus
=== LKT namus/numero
```


## [2026-09-07T19:33:47.347Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TAD context\"; sed -n '2730,2750p' TAD_pages.txt\necho \"=== AFM context\"; sed -n '3938,3950p' AFM_pages.txt"
}
```


### [2026-09-07T19:33:47.400Z] TOOL RESULT

```
=== TAD context
‫المأخوذمنالعبراني ‪. 9‬بد» وهونباتعرقهاسودليب الرائحهلهسنبلزهره‬
 ‫عطري يستخرج منهطيب بين ‪ .‬والاصح أينُسمى سبلالنرد األوسنبل‬
 ‫التردي أوالنرد علىالاصل العبراني ‪ .‬ومن حيث متبته يقال اللهسنبل الحندي‬
 ‫والسوري والرومي والسويسري ‪ ...‬ومنحيث طيبه يقال له سنبل الطيب ؤكتابته‬
‫دىّقه بنيح‬    ‫تصروداب علىالاصل العبراني وناردين غلط ‪ .‬ما دامامملحكف‬
                                                   ‫‪١:‬‬
                                                    ‫بردي رأمحته ‪ .‬نشيد ‪١‬‏ ‪١‬‬
  ‫ناقوس‪ -‬أرامي « ناقوشا ‪ 6‬معناه مُصوتت مشتق مننقدش أى ضرب‬
‫وقرعودق” وهوالملنمشبة لتحمديدة ثملطاس منمحاس ‪,‬قرعلاوقات الصلاة‬
                                                                 ‫افلكىثائس"‬
                     ‫معناه عادةوشربعة وسّنة‬         ‫ناموس ‪ -‬ووناني ‪89‬‬

              ‫معثاه عر الركن وجعل السفينة‬         ‫تاولون‪ -‬بوناني ‪00‬‬
                                 ‫يي للد‬   ‫سس‬




‫اصل سكن معبد أي مكان الرحال في‬
                             ‫انالهلفي‬
                                    ‫‪-‬ذلى وموم مع‬
=== AFM context
له بالتركية آلو بالو
( انرق والنئرقة ) فسرت بالوساحة الصناة نشكا علنها لد الا 70004
فوق الرحل مأخوذة من 2 وهو ܒܐ على كل سي ء ابن ناعم لطيف
* ( مش ) نم وكذب مأخوذ من فش اي المكر وا-قديعةܚܝܚ © ܘ | كك
11 ‫ 0[ )3 معرب وده
(3) الكتات الذي 4 فيه تعريب ثامه وبنوا.منة فملا وقالوا غقّ
3 6 الاراعى ` ܢܡܩܐ و شربه اليونالي 94 اي الناموس
جد ( العا 096 ܦ £ حجم الخردل .0 (08(8421¶÷ 0 2 93
106 ) تعريب 3( اللبز. والمب المذكور سني به لاه
ܝܣ
(التوردجة ) الضميمة وما أف من كل شىء ء 5 لورده
(التَاوق ) الطنشمة المنقؤرة التى يري فيها الماء في الدواليب 3 تاوه
00 ال لتيل اشىء مث عرس نذلاة ونان 99890
```


## [2026-09-07T19:33:48.987Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON namus\"; grep -n \"ناموس\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10\necho \"=== MON nomreh\"; grep -n \"نمره\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10\necho \"=== MON adena\"; grep -c . incoming/MON/MON_2vol_Adena_v2_djvu.txt; grep -n \"نمره\" incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -5"
}
```


### [2026-09-07T19:33:49.089Z] TOOL RESULT

```
=== MON namus
MON_part2.txt:3816:ناموس پرستی. (.) رشک. (تسص.) حمیت 
MON_part2.txt:3834:غیر تمند. غیور. آنکه به حفظ ناموس و آبرو 
MON_part2.txt:40859:فقت از دست دادن آن را. لو دادن ناموس 
MON_part2.txt:66129:آلوده کنندة ناموس کسی. مانده و فر سوده و 
MON_part2.txt:73100:ناموس: 05 (عادت» شر بعت ] (ا.) 
MON_part2.txt:73102:فرشته» ملکث. (اخ.) (کد.) جبرثیل. ناموس 
MON_part2.txt:73115:ناموس پرست: ۱۱۰-۱ [معر . ف. < 
MON_part2.txt:73116:ناموس پرستنده] (ص‌فا.) آنکه به عرض و 
MON_part2.txt:73117:ناموس خود بسیار علاقمند است؛ غیر تمند. 
MON_part2.txt:73128:ناموس گر 
=== MON nomreh
MON_part1.txt:86:دبیررستان نمره ۱ ( که بعدها بنام دبیرستان شاهپور خوانده شد) طی کرد. در اوان 
MON_part1.txt:16701:نمره‌هابی داده می‌شود که امتباز بد و خوب 
MON_part1.txt:46317:آن» نمره. حاصل» نتیجه» سودء فایده ج. 
MON_part1.txt:46320:نمره: (6-)2-]018 93 [ع. نمرة] (.) واحد 
MON_part1.txt:69250:گلوله‌ای روی نکن از نمره‌های لوحه‌ای 
MON_part1.txt:82972:برای نمره‌زنی دفتری بزرگک و مانند آن که 
MON_part1.txt:82984:عين حال نمره عوض می‌شود. اين عمل را 
MON_part1.txt:86523:اندازه. عدد. نمره. دانش (علم) شمار: علم 
MON_part1.txt:86539:شمارشمارة ترتیب: نمره‌ای که به شیثی یا 
MON_part1.txt:88251:شیفر: 6 (.) عدده رقم. نمره. ضسح.- 
=== MON adena
75975
17976:آن نمره‌های دروس و اخلاق و انضباط و 
60450:قسمت مجموع نمره‌های دروس هر شا گرد. 
79416:نمره: (0-)100172 [معر. عددء رقم] .( 
79427:نمره گیر: ۰-7 [معر. ف. و کر | 
79429:شامل نمره‌ها و با چرخاندن آن نمرة
```


## [2026-09-07T19:33:56.984Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON_part2 namus\"; sed -n '73095,73120p' MON_part2.txt\necho \"=== MON_part1 nomreh\"; sed -n '46310,46335p' MON_part1.txt\necho \"=== Adena v2 nomreh\"; sed -n '79410,79432p' incoming/MON/MON_2vol_Adena_v2_djvu.txt"
}
```


### [2026-09-07T19:33:57.071Z] TOOL RESULT

```
=== MON_part2 namus

نامور: ۲ (ص.) دارای نام. نام داده» 
مسمی. خداوند نام و اوازه» مشهوره 
معر وف. ممتاز» ارزنده. 

ناموس: 05 (عادت» شر بعت ] (ا.) 
شریعت» احگام الهی. قانون» قاعده. وحی. 
فرشته» ملکث. (اخ.) (کد.) جبرثیل. ناموس 
اکبر: قانون اعظم. (کد.) جبر ئیل. سر راز. 
کته تن تاموشن سانشان رای 
مکرء حیله تزویر. ریاء سالوس. سیاست؛ 
تدیر. بانگ. آوازه غوغا. اشتهاره صیت. 
عجب» کر خودسندی. آبروء عزت؛ 
احسترام. جنگ حرب. عفت؛ عصمت» 
پااکدامنی. زنان یکث خانواده وابسته به یکث 
مرد. (ف.) قاعده‌ای که حکیمان برای مصالح 
عامه مقرر دارند. (تص.) الف - توقع حرمت 
واه ای دار لت شپت و 
جاه و خودنمایی و خودستایی (اسرارنامه. 
چا. دکتر گوهرین. ۲۹۱) ج. نوامیس. 
ناموس پرست: ۱۱۰-۱ [معر . ف. < 
ناموس پرستنده] (ص‌فا.) آنکه به عرض و 
ناموس خود بسیار علاقمند است؛ غیر تمند. 


۱ 
=== MON_part1 nomreh
وزن ده عدد آن هشت مثقال بوده است. ایاء 
تمانیه: هشت فلک (افلا کك سعةً سباره و 
فلک البر وج). جنات تمانبه: هشت سبهشت؛ 
هشت خلد. رذایل تمانبه: دو طرف افراد و 
تفریط فضایل اربعه. 

تمر: ٩۲‏ [ع.] (.) میوه؛ بار» بر؛ واحد 
آن» نمره. حاصل» نتیجه» سودء فایده ج. 
تمار؛ جج. انمار. 

نمره: (6-)2-]018 93 [ع. نمرة] (.) واحد 
ثمر. یکی میوه» یکك بر. نتیجه» حاصل. 
نسل» فر زند. 

ثمن: 52210۳ [ع.] (.) بها» ارز» بر ج» قیمت) 
ج. ائمان. ثمن بخش: بهای کم. 


فر هنک فار 


نم سي معین ۱۱۵ 


نشمن: «صمد [ع. و .) هشت 
ی 29 باه ی جر دیهان 
=== Adena v2 nomreh
متگا» بالش؟ كی نمارق. 


نمرود. (دم)60۵۳4: [سعر .] (ا.) عنوان 
یادشاهان کلده؛ ج. نمارده. مخصوصا به 
پادشاه معاصر ابراهیم(ع) اطلاق شده. 
نمره: (0-)100172 [معر. عددء رقم] .( 
شماره؛» عدد. مجموع شماره‌هایی که از یک 
نشر به (روزنامه» مجله) در هر دفعه چاپ و 
منتشر می‌شود و دارای شمارة مسلسل است. 
عددی که معرف معلومات شاگرد و مدرسه 
است و آن را معلم پس از سوال و امتحان 
تعیین و در دفتر با ورقة مخصوص ثبت 
می‌کند؟ ج. نمرات. نمرءةٌ ترتیب: شماره 
مسلسلء شمارة ترتیب. (ص.) (عم.) شخص 
زرنگ و ناتو و اقلا. 

نمره گیر: ۰-7 [معر. ف. و کر | 
(ص‌فا. امر.) آلتی که در تلفون تعبیه شده» 
شامل نمره‌ها و با چرخاندن آن نمرة 
مطلوب را بدست آرند و با طرف مکالمه 
0 : ععه [ع.] ((.) راسو.
```


## [2026-09-07T19:34:23.789Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(json.dumps(d['MON'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-07T19:34:25.113Z] TOOL RESULT

```
{
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


## [2026-09-07T19:34:34.794Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nwc -l incoming/BQT/BQT_v4_pages.txt; grep -c '\\[pdf page' incoming/BQT/BQT_v4_pages.txt\ngrep -n \"نماز\\|نمد\\|ناموس\" incoming/BQT/BQT_v4_pages.txt | head -20"
}
```


### [2026-09-07T19:34:34.858Z] TOOL RESULT

```
22553 incoming/BQT/BQT_v4_pages.txt
553
300:دهنمد| که هموازه مرا درحل مشکلات لغت راهنماً ومشوق بوده‌اند, ودر
4050:ی زگوند . - وشخصیرا| هم میگوبند که نماز را بسرعت تمام
4256:۲ - مصلی » اسم مکان از تصلية , جای نماز « اقرب الموارد » .
7316:است . پا آنگه ملمانان همه نواحی زمین بهنگام نماز روی بدانکنند -
7539:5 نامزد ۱ - بسکون ثالك وفتح زای ناموس * - بر وزن قاموی » بممنی
7553:عربی « ناموس » ساحب رازآ کاه بر نهانی امن - با صاحب راز خبن - و نام جبرئیل علره‌اللاي
7555:نهانی - وخوایگاه شیر» ناموسة «ثله. > «منتهی‌الارب * وایز وحی - وخانةٌ راهب - و دروغزن -
7579:ناموس | کیر - کنایه ازجبرئیل ۶ .| نوسند۷ .
7581:ناموس گاه - کنایه از جنگه کاء قرآن باشد چه بعد از زبور وتوراة وانجیل تال
8969:چبانند و نقاشی کنند ؛ و بسنی کوبند یرم ۱ بلفت زند و پازند (۱) عبادت او نماز کردن را
8987:ح (۰)۸ ۴ - هز . (22512)82 ۰ پهلوی 82۳020 ( نماز ) ۶« پونکرص ۷۹ *.
9097:برآورده وخابيدة شتران وامثال آن باشد ۴ . ماشد نمد کرم خورده وآ ترا بعربی‌هرشفه ورغوة
9969:که ماضی نمودن است پعتی ظاهر شد و نمایان نماز ۴ » بنتح اول و ثابی بالف کشیده
10010:در طربقت کجا روا باشد دل به بتخانه رفته , تن به نماز. « سنالی غزلوی ص۲۵۹ ۶ ۰
10012:شهی که با رکه اوست مجدء گاه ملو همی برند بان مجده که ملوك نماز .
10047:نمد در آب داشتن کنایه از | میشود - و بفتح اول وکسر میم هم درعرب ی کاو
10075:‏لمد - بفتح اول و دوم » پپلوی 288181 «تاوادبا س ۱۹۳ > » استی 811381(نمده
10079:( قرش نید )۰ قی: لری 8600 (نمد) « ژابا س 4۲۳ ؛ پشم‌های روی عم گذاشته ومالید هکه
10080:ازآن فرش وکلاه وچاقه کنند .مارا هم آزین نمدكلاهي است (مثل).
10187:در ایرانی‌باستان -8812 ( خم شدن . تعبم کردن ) « پارتولمه ۱۰۶۱ 2 . رك : نماز . - و الیل
```


## [2026-09-07T19:34:40.299Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ncur=None\ntargets=[7539,7553,7555,8987,9969,10047,10075,10079,10187]\nfor i,l in enumerate(lines,1):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: cur=int(m.group(1))\n    if i in targets: print(i, 'pdfpage', cur, '|', l[:120])\nEOF"
}
```


### [2026-09-07T19:34:41.570Z] TOOL RESULT

```
7539 pdfpage 189 | 5 نامزد ۱ - بسکون ثالك وفتح زای ناموس * - بر وزن قاموی » بممنی
7553 pdfpage 189 | عربی « ناموس » ساحب رازآ کاه بر نهانی امن - با صاحب راز خبن - و نام جبرئیل علره‌اللاي
7555 pdfpage 189 | نهانی - وخوایگاه شیر» ناموسة «ثله. > «منتهی‌الارب * وایز وحی - وخانةٌ راهب - و دروغزن -
8987 pdfpage 225 | ح (۰)۸ ۴ - هز . (22512)82 ۰ پهلوی 82۳020 ( نماز ) ۶« پونکرص ۷۹ *.
9969 pdfpage 250 | که ماضی نمودن است پعتی ظاهر شد و نمایان نماز ۴ » بنتح اول و ثابی بالف کشیده
10047 pdfpage 252 | نمد در آب داشتن کنایه از | میشود - و بفتح اول وکسر میم هم درعرب ی کاو
10075 pdfpage 252 | ‏لمد - بفتح اول و دوم » پپلوی 288181 «تاوادبا س ۱۹۳ > » استی 811381(نمده
10079 pdfpage 252 | ( قرش نید )۰ قی: لری 8600 (نمد) « ژابا س 4۲۳ ؛ پشم‌های روی عم گذاشته ومالید هکه
10187 pdfpage 255 | در ایرانی‌باستان -8812 ( خم شدن . تعبم کردن ) « پارتولمه ۱۰۶۱ 2 . رك : نماز . - و الیل
```


## [2026-09-07T19:34:52.748Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9960,10010p' incoming/BQT/BQT_v4_pages.txt"
}
```


### [2026-09-07T19:34:52.795Z] TOOL RESULT

```
[pdf page 250]
بیان دیستم
در لون با میم مشتمل برسی و پنج لغت و کنایت

نم ۱ > بفتح اول وسکون نانی؛معروف | هم هست . ۱
است که رطوبت اندك باشد - و بمعنی طراوت‌هم مار ۴ - بر وزن سوار» بممنی ایما
آمده است. و اشاره باشد ؛ ونماران بمعنی آشارات » بواسطهةٌ

ماد - بروزن سواد ‏ بسمنی‌نمود باشد | آنکه جمع مار است .
که ماضی نمودن است پعتی ظاهر شد و نمایان نماز ۴ » بنتح اول و ثابی بالف کشیده
کردید ۴ - ویمعنی‌فاعل هم‌آمده است که ظاهر | و پزای نقطه‌دار زده » بمعنی بندکی و اطاعت
کننده باشد سوبممتی‌ظاهر کردونمایان گردانید۲ | وادای طامت (۱) وسجود «پرستش و خدمتگاری

() چش : - وادای طاهت .

۱ - فارسی 8880 از -882۵208 ۵ ۳ 88008 5 ماند 6۵08 از پارسی باستان .
- ۵ > 362008 آمده , افشای 2004 , 200۳۵ « حوبشمان ۱۶۰۳۹ * » پپلوی
0 . 3850 ۰ بلوچی 888210 ( شبنم » مه) « اسشق ۰۶۱۰۳۹ کردی 86۵1 ۰ 8678
( مرطوب ) « ژابا ص 4۲۳ .

زروی تو بچه معنی‌همی پرویدکل؟ . زچشم من بچه معنی‌همی پبارد ‎٩‏

« معزی لیشاپوری ی 2۹۹ ۰۹

۴ #نمود : « نماد » پعنی نمود . عنصری ( بلخی) کوید :

زان کماید فقم که بگشادی زان نماید ترا که پنمادی .»

« لغت فری ص ۱۱۶ ۰۴

۴ - از دساتیر « فرهنگه دسالیر ص ۷۷۰ > . آقای حکمت در « پارسی نغز . تهران
۳۰ سس ۱۸۸ این کلمه را مسحف « نماد » (۸.م.) پنداشته اند .

۴ - پپلوی 285026 ۰ ازایرانی باستان -88772 ( خم شدن » تعظیم کردن ) «پارتولمه
۱۹ بیبرگه اس ۱۵۶ ور : خوبشمان۱*۰4۰ ؛ ی : اوستایی -36122210 ( دعا ).هندی
باستان -860388 ۰ پازند 2220 , اضنابی زه3۳۵ ۰ بلوجی د8ق 52۳۵ ۰ 82855 -
رك : اسشق ۱۶۸۰ کردی 88 . 81 ( ساز) , زازا زةهرع2 « ژابا ی 4 *:اورامانی
8۳2 «که . اورامان ۴۱۲۵ » گیلکی 38782 - مجازاً عبادت مخصوس مسلمانان .
[pdf page 251]
ساد -ه۹۱۹<
وفرمان برداری باشد ‎٩‏ .۰ زمینی باشد سفید وشوره زا رکه درصحرا| وبیابان
نماد «بفتح اول بروزن هلاك , رواج | از دور باب مینماید .
و دولق وزیبایی راکوبند ۲ #۰ ماک - بفتح اول و سکون ثالی و شم
ماما ۴ - بروزن قواما . بلفت پونانی | فوقانی وکاف ساکن » میوه‌ای باشد صحرا ی که
سوستبر باشد وآن نوعی از نعناع است و بعریی | آبر| بمریی زعرور و مثلك‌المجم کویند ۴ باین
نمام الملك خوانند. آعتبا رکه دانهٌ اوسه پهلواست و درخراسان علف
نمایش آب « بمعتی سراست و آن | غیران 8 خوانند ؛ وبفتح اول وثانی هم گفته‌اند
چوووووححخخ-<حححححح۳ح۳ح .<< ی
۱ - در اسطلاح , عبادت مخصوس و واجب ملمانان که پنج بار در شبانه روز اداکنند
وآلرا بعریی صلا ةگوبند ( لمازهای متحب هم معمول است ) : ۹
در طربقت کجا روا باشد دل به بتخانه رفته , تن به نماز. « سنالی غزلوی ص۲۵۹ ۶ ۰
```


## [2026-09-07T19:35:09.722Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10035,10090p' incoming/BQT/BQT_v4_pages.txt"
}
```


### [2026-09-07T19:35:09.781Z] TOOL RESULT

```
لفت فری و در شم قربع آهده . اما در معنی آن اختلاف است. از شعر قربع برمیاید چیزست
سرخ رنگه ( برنگه بد ) وکم بها. ثابتی (س۱۷؟) نمتكرا ۳ آلووحشی ۳0۷۳8" 8۳۵2۵9
آورده است . 8 - در مشهد 512070 813 کوبند «کنابادی ».
دمام رك : ماما . ۱
[pdf page 252]
- ۱۹۹ سخته
اما بمعنی آلوبالو وآن‌میوه‌است شبیه‌بگیلای۱ | سین بی‌نقطه ؛ راسو را کویند و آن جانورست
- ویضم اول وثانی‌چیز ست سرخ مانندمرجان؟ » | مشهور بموش خرما وعربان این مرس خوافند.
وباین معنی بجای نای قرشت لون هم بنظرآمده مش ۱ - بنتح اول وسکون تانی‌وشین
است #۰ قرشت , مکر وحیله و دغابازبراکویند - وبفتح
نمچ ؟ - بفتح اول وسکون نانی وجیم : اول و میم در عربی‌خطها وشکلها و نقطهای سیاء
فارسی » بمعنی لم ام ت که رطوبت آلد4 باشد.3# و سفید باشد و آن علتی است که در آدمی پیدا
نمد در آب داشتن کنایه از | میشود - و بفتح اول وکسر میم هم درعرب ی کاو
مکر کردن ودر فکر حیله و دغا بودن باشد۴ . | کوهی را گوبند که برو نقطهای سیاه و سفید
فمد‌زیی « دی باشد که بروعت‌اسب | باشد .
بهند و زین را بر‌بالای آن گذارند و درین زملن نمشته ۷ « بفتح اول و کسرانی‌ومکون
تکلت و کویند . ثالك وفتح فوقانی (۱), بمعنی عقیده و اعتقاد
نمی *- جنم اول وثانی واسکون | باشد -

() چش :- وکسرئانی... قوقانی .

۱ سر ح #سفحة قبل. ۴ - این‌معنی را ازدعر قریم‌الدهر (ح4مفحهٌ قبل)
استخراج کرده اند . ۴ سم (هم.) مج « نمچ .انم باشد . عتصری (بلخی) گفت :

سنکه بی‌مج وآب بی*زایش همچو نادان بود بآرایش .*
« لفت فری چاپ هرن ص ۲۰ >.
در لفت فری مصحح اقبال ص ۹۸ و۷۶ «لمج» آمده . ۴ - رك : رشیدی .

8 - « دمن » جنمتین جانوری که‌آنرا بر گوبند .» «رشیدی» در بسشی نسخ ( رشیدی)
این جمله بسدازلفظط «کویند» آمده : « وشرح آن درلفت راس و گذشت » « حاشية رشیدی ».

‎٩‏ - (عر) ۶ امش بالفتح . خطهای کف دست و پیشانی - ولیژلمش مخن‌چینی - وچیدن
چیزی اززمین‌عمجو بیپوده‌کاران - ودروغ گفتن - وخوردن ملخ وآنچه برروی زمین باشد -لمش
محر كة خجکهای سپید وسیاء بالقطه‌های پوست کاو وج زآن مخالف رنگه‌آن - وخطهای نگارخانه
- وابلق وجهار شدن - دش ککتف کاوارچیار - و بعیر لمش : شت رکه در سپل آن اشانیی باشد
سوای اثر ه که بر روی زمین ظاهر کردد .> ۶ منتهی‌الارب > + ۷ - از دساتیر ۶« فرهنگه
دساتیر ص ۲۷۰ 2 ۸ هرمزدنامه ص ۳۱۸ > وظ. مقلوب با مصحف «منشت» ۳ منش‌است.

‏۰ مج رك : لمچ +

‏لمد - بفتح اول و دوم » پپلوی 288181 «تاوادبا س ۱۹۳ > » استی 811381(نمده
جبة دی ) , 5078086 . 03961 16۲ . 12011 020 :82 , 33008062020) ۰
(62. ,572730102862 .)0994 ۳۵۵۲ ,ع 5۵0۵1061 0.129:۸/([07 درساسکریت
-18۳2 (نند) متعار است « هوبشمان ۱۶۸۱ > و ر4 : اسشق ۰۱*۶۱ کردی 26260
( قرش نید )۰ قی: لری 8600 (نمد) « ژابا س 4۲۳ ؛ پشم‌های روی عم گذاشته ومالید هکه
ازآن فرش وکلاه وچاقه کنند .مارا هم آزین نمدكلاهي است (مثل).
[pdf page 253]
نمشك دیا
سس کی
تمنشات ۱ - بر وزن سرعك , عیربرا مکزی -« بنتم اول و ثانی و سکون
گوبند که ازبتان کوسفند و کاو بردوغ وماست | کاف وزای نقطه‌دار بتحتانی "اشیده , حلوائی‌است
بدوشند -ویمعنی‌قیماق دیرخام ومسکه‌ و کر»(۱) | که آنرا از آرد و شکر با عصل و دوشاب پزند
هم آمده است. ومغز گردکان وبادام و پسته وامتالآن‌داخل کنند
لمشیدن - بروزن فپمیدن , بممنی‌کام | وقند سوده ومشك و کلاب‌برآن پاشند وخورند؛
باقتن و بمراد رسیدن باشد * وبعی گوبند میوه های خشك شده داخل کنند.
نمك انگیزیدن - کنابه از کربه نمکسود ۴ - هرجیزراگوین دکه بر
```


## [2026-09-07T19:35:19.246Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7530,7600p' incoming/BQT/BQT_v4_pages.txt"
}
```


### [2026-09-07T19:35:19.329Z] TOOL RESULT

```
( ناله کردن . زاری کردن ) را .136 .۸۲8.۳7۴ و16 .12011 ۵۳۵4 31۷3۰ ,6۲ون0ه0
ترجیح میدهد مأخوق از ساسکریت 32۳6 ( غربدن » جیغ کشیدن ) . اففالی 8۳1 ( زوزه
کمیدن ۰ فرباد زدن ) بدانیم ؛ افغان کردن » با آواز بیان اندوه خوبش کردن , زاریدن :
پنال پلبل اگر با منت سر بارست که ما دو عاشق زاریم وکارما زارست .
« حافظ شیرازی س ‎4٩‏ *.
[pdf page 189]
فامور هنن
روز دهم است ازسالهای ملکی- و مردمان بپادر | نامآور است که‌خداوند ناموآواژه ومشهورومعروفق
وشجاع را دز کوبند .#۸ باعد ۴ .
5 نامزد ۱ - بسکون ثالك وفتح زای ناموس * - بر وزن قاموی » بممنی
هوز » لشکریراکونند که بجهت مهمی و کاری ۲ خانه و ۰
8 پانگك و آوازه۹ - و ساحب مرا وخانه و منزل
بطرفی روانه کنند ۴ - و دختری که بعد ازچند | * 8
کاء دیگر بخواهند . باشد - وبمعنی‌عسمت وعفت هم‌عست۷ - وجنگه
نامود ۴ - با وار بروزن دا دکر,مشفف | وجدال را هم کفته‌اند - و ملالکه ۸ - و احکام
۱- از : نام ۲ زد ( زده) ( آسم مفعول مرخم ).
۴ - یکی لشکری نامزدکرد شاه کنید آنگهی تور لشکر براه -
قردوسی طوسی « شاهنامةٌ بخ ج۱ ان ۴۷۸ 2
۴ - از: نام ور( پسوند اتصاف ودارندگی ) [ ازمسدر 827 بردن | . رك: هرمزدنامه
۰-۹ و ر4 : دارمتتن . تتبعات ج۱ ص ۲۹۳ .۰
۴ -هثر در جهان از من‌آمد پدید چو من نامور تخت شاهی ندید -
فردوسی طوسی «شاهنامةٌ بخ ج ص۲۹
- لزنازی, از یونانی 36۵1305 بمعنی عادت و شربمت « تفس > « ژابا ص 4۱۹ ۴ در
عربی « ناموس » ساحب رازآ کاه بر نهانی امن - با صاحب راز خبن - و نام جبرئیل علره‌اللاي
و مرد دانا ماهر‌درکار - ولظرف‌المدخل - و کازء صیاد ودامآن - ومرد سخن چین - ومکرو حيلهٌ
نهانی - وخوایگاه شیر» ناموسة «ثله. > «منتهی‌الارب * وایز وحی - وخانةٌ راهب - و دروغزن -
و شریمت « اقرب‌الموارد > و لیز درظفه بمعنی قالون و حکمآید . بمعانی دیگن مذ کور درمتن
متعمل در فارسی‌است ۰
‎٩‏ -کیست که پیغاممن بشهر شروان برد ابك سخن از من بدان مرد سخندان برد
گوید: خافایا ۱ اين‌همه ناموی چیست؟ نه هر که دو بیت گفت لقب زخاقان برد.
جمال‌الدین اصقپانی ۸« مجمع‌الفسحاء ج ‎٩‏ ص ۰۴۱۷۸
۷ - باین معنی امروزه بیشتر متداول است- ۸ - درعربی « ناموی > و « تاموی
آلاکبر» فقط جیرئیل راگوبند. رك : اقرب‌الموارد .
نام - پپلوی 2200 ۰ ابرانی باستان -32087 « بارتولمه ۱*۹۲ > « نیب رکه اص
۶ پارسی باستان 82۳1271 ( نام » اسم ‎ )‏ اوستا 321027 , هندی باستان -8228.
آرمنی 2818 ۰ اففابی 80772 ۰ بلوچی 8270 » استی 30770 ۰ 307 ۰ رك : امشق ۱۹۲۲ ‎٩‏
‏کردی/287 ( اسم » شهرت ) . 8۵۷ ۰ 88۲0 ۰ زازا 88106 « ژابا س 2۱۵ *؛ اورامانی 32817
* که . اورامان سس ۱۲۸ > , ختنی 3۳78 ( نام ) « رو زکارلو ج 4 شمارة ۳ص ۵۲ > ؛ لفظی
که بدا ن کی پا چیزی را بخوانند , اسم - شهرت وآوازه :
نام نیکوگر بماند ز آدمی به کزو ماند مرای زرنگار -
سعدی غیرازی « امثال وحکم دهخدا >.
2 لاه‌دار - از : بام دار (.دارنده ) » مشهور , معررف » نامی » نام‌آور :
بپرسیدشان از نژزاد کیان وزان نامداران قرخ کوان ...
فردوسی‌طوسی « شاهنامةٌ بخ ج اص ۸+
( برهان قاطع ۲۹۹ )
[pdf page 190]
-۱۳- نان‌آشروی
الهی را نیز کوبند ۱ - و بمعنی کمی نگاه صیاد هم آمده است ‎٩‏ - واخط تعلیق را نیز گویند
هم آمده است - ۰ باعتبار ایشکه احکام و فرامین را بآن خط می-
ناموس | کیر - کنایه ازجبرئیل ۶ .| نوسند۷ .
است ۲ . نامه چهاره - اغارء بفرقان است که
ناموس گاه - کنایه از جنگه کاء قرآن باشد چه بعد از زبور وتوراة وانجیل تال
باشد چه ناموی بمعنی جنگ هم آمده است. شده است .
نامو به ۴« بفتح تحتانی بر وزت نامی - بروزن جامی . بمعنی‌ناموربودن
واکوبه , زنی‌راگوبند که بقیراز يك‌شوهرندیده
| و شهرت کردن ونام برآوردن باغد ۸ - و تامه
و بمرد دیگر نرمیده باشد و مران او و شوهرش فرمانرا هم میکویند ‎٩‏ 1
نهایت الفت ومحبت و اتحاد بود ۴ . و فرمانر! هم میخوشد * - و جراعری بمعتی
نامه ه : ِ ۱ بالنده وه نموکننده باشد .۸
نامه < بروزن خامه . کتابت وفرمان
را گوبند - وبمعنی کتاب هم هست همچوشاهنامه نان آتش ری *۱- کنابه ا زآتاب
وفرس نامه و بازنامه وامثال‌آن - و بممتی‌سیلاب | عالمتاب است .

۱- « مینداری د که آمدم تا ناموی وتورت باط لکنم . نه نیامدم که منشو خکنتم .. >
( قول عیمی2 ) * انجیل فارسی ص*۹ >. ۲ - رد4 : اقرب الموارد - ۴ - رشیدی
کوید : ۰ معنی تر کیبی آن منسوب به « نام » بعنی درآن‌کار نامدار و نامو رکشته > ظ . از +
نام ۳ وبه ( پنوند ) <- که معرب آن « وبه > بفتح واو است [ قن : شیروبه » سیبویه .
مسکوبه ] رك: ند که. تبعات ابرانی. وین ۱۸۸۸ ص48 یمد .

۴ - سولت او دران صف ناورد زن نامویه بر کند از هرد -
```


## [2026-09-07T19:35:31.824Z] TOOL CALL #44: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-07T19:35:31.831Z] TOOL RESULT

```


```


## [2026-09-07T19:35:33.918Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ncur=None\nfor i,l in enumerate(lines,1):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: cur=int(m.group(1))\n    if 'نماز' in l and cur and 320<cur<345:\n        print(i,'pdf',cur,'|',l[:160])\nEOF"
}
```


### [2026-09-07T19:35:35.366Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T19:35:41.717Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ncur=None\nhits=[]\nfor i,l in enumerate(lines,1):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: cur=int(m.group(1))\n    if 'نماز' in l: hits.append((i,cur,l.strip()[:120]))\nfor h in hits: print(h)\nEOF"
}
```


### [2026-09-07T19:35:43.029Z] TOOL RESULT

```
(3274, None, '\u202b[بیژن] پیاده شد از اسب و روی زمین\u202c        \u202bدر نمازم خم ابروی تو با یاد آمد\u202c')
(3609, None, '\u202bبمانم ت\u202c                  \u202bنماز\u202c          \u202bبرآمد\u202a .\u202cپری روی [رو\u202c')
(4208, None, '\u202bکرده بود» زمانی به نماز خواندن» زمانی\u202c                                \u202b(اسدی \u202a:)۱۸۱-۵۶\u202c\u202c')
(5293, None, '\u202bتو از بسدتنان بسودی و بی\u200cبنان\u202c            \u202bکه همی بلبل بر سرو کندبانگ نماز\u202c')
(7489, None, '\u202bپنهان داشتن\u202a .\u202cدنهفتن\u202a:\u202c\u202c                   \u202bبیامد خحرامان و بردش نماز\u202c')
(9387, None, '\u202bجهنده یگزرنده\u202a:\u202c\u202c            \u202bبی\u200cطاق ابروی تو نماز مرا جواز\u202c')
(14002, None, '\u202bگودرز به پیران ویسه پیام می\u200cفرستد\u202a:\u202c\u202c                        \u202bبیامد بر سام و بردش نماز\u202c')
(16531, None, '\u202b(اسدی \u202a:)۳۵۲-۴۸\u202c\u202c                            \u202bغریوید بسیار و بردش نماز\u202c')
(19258, None, '\u202bنماز» حق\u202a:)...\u202c\u202c            \u202bشبیگر ز گل فاختگان بانگ برآرند\u202c')
(19287, None, '\u202bاگر ماندست لختی زندگانی\u202c     \u202bتاریخ سیستان \u202a :)۶۸\u202cبامداد برحاست نماز\u202c')
(19317, None, '\u202bآوردن (سپاس\u202a .\u202cوام نماز حق\u202a )...\u202cبه همه\u202c                             \u202bدر زمانه گزفته\u200cهای منست\u202c')
(21699, None, '\u202bبرفتند و بردند پیشش نماز\u202c                                     \u202bباآننگین نامه\u200cها را مهرمی\u200cکر دند\u202a:\u202c\u202c')
(21705, None, '\u202bز دور آفرین کرد و بردش نماز\u202c                                                        \u202bابورل)\u202c')
(21708, None, '\u202bنمازش برد و پوزش خواست بسیار\u202a...\u202c\u202c                               \u202bهمه شاد گشتند و خحرم شدند\u202c')
(21714, None, '\u202bتخت بردند ملک را نماز برد\u202a.\u202c\u202c            \u202b(\u202a)۵-۹۳۳-۹۶۷۱\u202c\u202c')
(21733, None, '\u202bکه را دارد ارزانی این تاج و تخت\u202c                                                       \u202bنماز (بردن)\u202c')
(21807, None, '\u202bنوان پیش او رفت و بردش نماز\u202c                    \u202bدارند\u202a ...\u202cتا هیچکس به\u200cسبب نوا در پادشاه\u202c')
(22206, None, '\u202bنماز و آفرین» تعظیم و تکریم\u202a:\u202c\u202c            \u202b(\u202a)۵-۲۴-۹۷۵\u202c\u202c')
```


## [2026-09-07T19:35:47.721Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('pages',len(pages))\nfor i,p in enumerate(pages):\n    if 'نماز (بردن)' in p or 'نماز (بردن' in p:\n        print('leaf',i)\n        print(p[:2500])\nEOF"
}
```


### [2026-09-07T19:35:48.926Z] TOOL RESULT

```
pages 485
leaf 444
‫نمایش‬                                            ‫‪۳۳۱‬‬


                ‫چو نزدیک رستم فراز آمدند‬                                                    ‫نگین‬
 ‫باه تس سار ان‬                                             ‫‪_۱‬گوهری کهبرروی انگشتر نشانند‪.‬‬
 ‫‪۱۵-۲۵-۱۶۷4‬‬                                            ‫ذشته نام‬
                                                              ‫گر‬‫‪-۲‬مهر (با پیش اول)» د‬
                 ‫پری روی گل رخ بتان طراز‬               ‫شخصی را روی نگین انگشتر می‌کندند و‬
‫برفتند و بردند پیشش نماز‬                                     ‫باآننگین نامه‌ها را مهرمی‌کر دند‪:‬‬
‫‏)‪(FVY-1۶۷-1‬‬                                                       ‫برآن نامه بنهاد خسرو نگین‬
                            ‫(اسدی ‪:)۰۴-۵۴‬‬              ‫فرستاده را داد و کرد آفرین‬

                ‫بيامد بر جم شه سرفراز‬                  ‫(‪)۵-۵۴۱-۶۴۰۱‬‬

‫ز دور آفرین کرد و بردش نماز‬                                                        ‫ابورل)‬
                                                                                        ‫نم(باز‬
                            ‫(ویس ‪:)۶۴-۴۲‬‬                                      ‫‪-۱‬اشک» سرشک‪:‬‬
     ‫نمازش برد و پوزش خواست بسیار‪...‬‬                               ‫همه شاد گشتند و خحرم شدند‬
‫(سیاست‌نامه ‪ :)۷۲‬چون حاجبان او را پیش‬                    ‫دم‪.‬‬
                                                           ‫نزن‬
                                                             ‫شدهدپرا‬
                                                                   ‫زادی دو دی‬
                                                                            ‫ش‬
                 ‫تخت بردند ملک را نماز برد‪.‬‬            ‫(‪)۵-۹۳۳-۹۶۷۱‬‬
                     ‫نمایش (اسم مصدر از نمودن)‬             ‫که مانام او [رستم] ازجهان کمکنیم‬
                               ‫‪-۱‬راهنمایی‪:‬‬             ‫دل و دی د؛ زال پر نم کنیم‬

                  ‫مرا اندرین گرنمایش کنید‬              ‫(‪)۶۶۲۳-۰۷‬‬
‫وزین بند راه گشایش کنید‬                                                      ‫(اسدی ‪:)۴۲۴-۷۵-‬‬
‫(‪)۱-۶۷۱-۸۲۶‬‬                                                    ‫گرفت آفرین» پشت راداد خم‬
                ‫به جای شما آکننم در جهان‬               ‫زشادی به چشم اندر آورد نم‬
‫که بکهاتران کس نکرد از مهان‪.‬‬                                                          ‫‪-۲‬باران‪:‬‬
                           ‫‪-۲‬دستون فرمان‪:‬‬                          ‫همان بدکهتنگی بد اندر جهان‬
                          ‫(اسدی ‪:)۹۱۴-۵۳‬‬
```


## [2026-09-07T19:36:02.089Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/nem-",
 "prompt": "Give the full reconstruction page: root form, meaning, and all descendants/derived terms listed (especially Greek nomos, Latin numerus, Germanic *neman, Indo-Iranian). Also note if there are two homonymous roots nem- (one \"to assign/take\", one \"to bend\")."
}
```


## [2026-09-07T19:36:04.198Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%85%D8%A7%D8%B2",
 "prompt": "Give the Persian entry نماز in full: etymology (Middle Persian form, Old Iranian/Avestan root, cited authorities such as Hasandust, MacKenzie, Cheung), meaning, and descendants/borrowings into other languages."
}
```


## [2026-09-07T19:36:05.834Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%85%D8%AF",
 "prompt": "Give the Persian entry نمد (namad) in full: etymology (Middle Persian, Proto-Iranian, Avestan nəmata-, Sanskrit namata, Sogdian), meaning 'felt', and any descendants/borrowings (Arabic namaṭ, Aramaic, Turkish, Hindi namda)."
}
```


### [2026-09-07T19:36:08.505Z] TOOL RESULT

```
# Proto-Indo-European Root *nem-

## Root Forms and Meanings

The page documents **two homonymous roots**:

**Etymology 1 (*nem-): "to distribute; to give, to take"**
- Possibly related to *h₁em- ("to take, to distribute")

**Etymology 2 (*nem-): "to bend"**
- Derived from Etymology 1 through semantic shift: "to distribute" > "to worship, sacrifice" > "to bend"

## Major Descendants

**Greek:** Ancient Greek νέμω (némō, "dispense, distribute") and νομός (nomós, "pasture, habitation, province"); also Νέμεσις (Némesis, goddess of retribution)

**Latin:** numerus and related forms, derived from *nom-ó-s

**Germanic:** *nemaną ("take"), with further modern descendants

**Indo-Iranian:** *námas (Sanskrit náma, "pasture-ground") and *námati ("to bow")

**Celtic:** Old Irish neim ("poison") from *neman; also *nemetom

**Baltic-Slavic:** Latvian ņemt ("take")

The page notes these roots generated approximately 73 derived terms across Indo-European language families.
```


### [2026-09-07T19:36:11.371Z] TOOL RESULT

```
# Persian Entry: نماز (namāz)

## Etymology

**Middle Persian Form:** 𐭥𐭮𐭢𐭣𐭤 (ʿsgdh /namāz/) or 𐬥𐬀𐬨𐬁𐬰 (namāz), meaning "reverence, prostration, prayer"

**Old Iranian Root:** Proto-Iranian *námah, derived from Proto-Indo-Iranian *námas ("to bow, prostrate")

**Proto-Indo-European Origin:** *némos, from *nem- ("to bend") + *-os

The etymology chain traces back through: Proto-Indo-European → Proto-Indo-Iranian → Proto-Iranian → Middle Persian → Classical Persian

## Meaning

The word denotes "regular, prescribed prayer" in Islamic contexts, specifically referring to salat. It also applies to obligatory prayers in the Baháʼí Faith. Notably, prayers not mandated by religious law are termed دعا (do'â) instead.

## Descendants & Borrowings

The term has dispersed widely into numerous language families:

- **Turkic:** Ottoman Turkish, Turkish, Uyghur, Uzbek, Tatar, Crimean Tatar, Bashkir, Kazakh
- **Indo-Aryan:** Urdu, Punjabi, Sindhi, Bengali, Assamese, Gujarati, Hindi
- **Caucasian & Other:** Georgian, Armenian, Russian, Albanian, Romanian, Polish
- **East Asian:** Mandarin Chinese (乃瑪子)
- **Southeast Asian:** Thai (ละหมาด)
```


### [2026-09-07T19:36:12.458Z] TOOL RESULT

```
# Persian Entry: نمد (namad)

## Etymology
According to the Wiktionary source, نمد is "Inherited from Middle Persian [Book Pahlavi needed] (nmt' /⁠namad⁠/, 'felt')." The entry notes this ancient Iranian word was borrowed into other languages, including Sanskrit नमत (namata, "felt") and Hungarian nemez ("felt").

## Meaning
The Persian noun نمد (namad) means **felt** — the dense textile material.

## Descendants and Borrowings
The documented linguistic descendants listed include:
- Uyghur: نەمەت (nemet)
- Uzbek: namat

**Note:** The source provided does not include all the etymological layers you mentioned (Proto-Iranian, Avestan, Sogdian) or the complete list of borrowings (Arabic, Aramaic, Turkish, Hindi). The Wikipedia entry shown contains only the information presented above regarding its Middle Persian origin and documented descendant languages.
```


## [2026-09-07T19:36:19.919Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%85%D9%88%D8%B3",
 "prompt": "Give the Arabic entry ناموس (nāmūs) and the Persian entry ناموس if present: etymology (Ancient Greek νόμος? Syriac mediation?), meanings (law, honour, chastity, Gabriel), and descendants (Persian, Turkish, Urdu)."
}
```


## [2026-09-07T19:36:21.336Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%85%D8%B1%D9%87",
 "prompt": "Give the Persian entry نمره (nomre) if present: etymology (French numéro? Italian numero? Arabic نمرة? Russian номер?), meaning, and any note on the plural نمرات."
}
```


## [2026-09-07T19:36:23.395Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/number",
 "prompt": "Give the full etymology of \"number\", including Old French nombre, Latin numerus, PIE root, and the related entries mentioned (numerous, numero). Also anything about Italian numero."
}
```


### [2026-09-07T19:36:26.179Z] TOOL RESULT

```
# Persian Entry: نمره (nomre)

**Etymology:** The word ultimately derives from Italian *numero*, possibly transmitted through Arabic *نُمْرَة* (numra). The entry notes "the Arabic plural."

**Meanings:** 
1. Mark, score, or grade (such as on a school exam)
2. Number

**Plural Forms:** The word has two documented plural forms: *نمرات* (nomarât) and *نمره‌ها* (nomre-hâ).

The term represents a linguistic borrowing that traveled westward from Romance languages into Persian, likely via Arabic intermediaries.
```


### [2026-09-07T19:36:29.116Z] TOOL RESULT

```
# Etymology of "Number"

**Root Origin:**
The word "number" traces back to the PIE root *nem- meaning "assign, allot; take."

**Language Path:**
- **Latin**: *numerus* ("a number, quantity")
- **Old French**: *nombre*
- **Anglo-French**: *noumbre*
- **English**: "number" (c. 1300)

**Semantic Development:**
The noun initially denoted "sum, aggregate of a collection" around 1300. By the late 14c., it evolved to describe "written symbol or figure of arithmetic value." Later applications include musical selections (1885), telephone dialing codes (1879), and magazine issues (1795).

**Italian Connection:**
The document mentions the mock-Italian form *numero uno* appearing by 1973, referring to the colloquial sense of "oneself" (attested from 1704 in English as "number one").

**Related Entries:**
The page lists numerous derivatives including numeracy, numeral, numerator, numerate, enumeration, innumerable, and others—all ultimately deriving from Latin *numerus*.

**Verb Form:**
The verb developed separately from Old French *nombrer* ("to count, reckon"), also dating to c. 1300.
```


### [2026-09-07T19:36:29.919Z] TOOL RESULT

```
# ناموس (nāmūs): Etymology and Development

## Etymology

**Arabic Entry:**
The Arabic term derives from Classical Syriac ܢܡܘܣܐ (nāmōsā), ultimately tracing to Ancient Greek νόμος (nómos, "usage, custom"). In pre-Islamic usage, the meaning broadened from "divine law" to encompass human law, doctrine, virtue, and natural law.

**Persian Entry:**
Persian borrowed the term from Arabic نَامُوس (nāmūs), which itself came from Ancient Greek through Syriac mediation.

## Key Meanings

**Arabic meanings include:**
- Namus (a concept of honor and moral reputation)
- Confidant trusted with secrets
- Hunting refuge or lair
- Cromlech (stone circle burial structure)
- Nematocerous insects (mosquitoes, gnats)
- Obsolete adjective: cunning, astute

**Persian meanings include:**
- "Notion of honor, moral reputation, and female chastity"
- Something whose loss would dishonor a person
- Female family member (from male perspective)
- Law or regulation

## Notable Descendants

The word spread widely through Ottoman Turkish influence:
- **Turkish:** namus
- **Urdu:** namūs (via Persian)
- **Slavic languages:** Through Ottoman contact (Russian намыс)
- **Caucasian languages:** Georgian ნამუსი, Armenian նամուս, Ossetian намыс
```


## [2026-09-07T19:36:53.213Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/nomad",
 "prompt": "Give the etymology of \"nomad\" (Greek nomas, nomos, nemein, PIE root) and, if the page includes them, the entries/links for \"numb\", \"economy\" and \"astronomy\" roots."
}
```


## [2026-09-07T19:36:54.634Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/numb",
 "prompt": "Give the etymology of \"numb\" — Middle English nome/nomen, Old English niman 'to take', PIE *nem-, and the excrescent -b."
}
```


## [2026-09-07T19:36:55.906Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%85%D8%B1%D8%A9",
 "prompt": "Give the Arabic entry نمرة: is there a sense 'number'? What etymology is given (Italian numero? Turkish?), and what dialects use it?"
}
```


### [2026-09-07T19:36:59.246Z] TOOL RESULT

```
# Etymology of "Numb"

The word "numb" traces back to Middle English *nome* (c. 1400), derived from the past participle of *nimen*, which came from Old English *niman* meaning "to take, seize, grasp." This ultimately derives from the Proto-Indo-European root *\*nem-*, meaning "assign, allot; take."

The literal sense of being "taken" with palsy or cold influenced the metaphorical meaning of "deprived of motion or feeling." The figurative usage emerged around the 1560s.

Notably, an "unetymological *-b*" was added in the 17th century "to conform to [other words like] comb, limb, etc." This insertion had no etymological basis but followed the orthographic pattern of similar words from that era.
```


### [2026-09-07T19:36:59.289Z] TOOL RESULT

```
# Etymology of "Nomad"

**Origin Chain:**
The word "nomad" (1550s) traces back through French *nomade* to Latin *Nomas*, then Greek *nomas*. The Greek term meant "roaming, roving, wandering" and connected to *nomos*, signifying "pasture, pasturage, grazing," literally "land allotted."

**Greek Terms:**
- *nomas* (genitive *nomados*): roaming/wandering behavior
- *nomos*: pasture or grazing land
- *nemein*: "to deal out"

**Proto-Indo-European Root (*nem-):**
Meaning "assign, allot; take," this root underlies numerous English words through its sense of distribution and allocation.

## Related Entries with Shared Roots

**Numb:** Derives from the *nem-* root, though through a different pathway involving Proto-Germanic influence.

**Economy:** Combines Greek *oikos* (house) with *nomos* (law/management), sharing the *nem-* root connection through the "allot/assign" sense.

**Astronomy:** Pairs Greek *astro-* (star) with *nomos*, using the root's sense of "law" or ordering principle rather than literal pasturage.

All three words leverage the fundamental *nem-* concept of allocation and ordering.
```


### [2026-09-07T19:37:00.899Z] TOOL RESULT

```
# Arabic Entry نمرة Analysis

**Sense of 'number':** Yes, the term denotes "number" across all three dialects documented.

**Etymology:** The entry attributes the South Levantine Arabic form to Italian origin. Specifically, it states the word was "Borrowed from Italian _numero_," tracing back through Latin _numerus_ to Proto-Indo-European. Turkish is not mentioned as a source.

**Dialects using this term:**
- Egyptian Arabic (nimra)
- Moroccan Arabic (namra)
- South Levantine Arabic (numra)

The etymological tree shows the South Levantine variant derives from Italian, while the page provides no alternative etymologies for the Egyptian and Moroccan variants.
```


## [2026-09-07T19:37:16.366Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW numerus\"; grep -n \"^numerus\" LEW_1910.txt LAT.txt | head\necho \"=== AFA namus\"; grep -n -i \"nāmūs\\|namus\\|νόμος\\|nomos\" AFA.txt | head\necho \"=== HUB 1041\"; grep -n \"1041\" HUB.txt | head\necho \"=== SKT number/nomad/numb\"; grep -n \"^NUMBER\\|^NOMAD\\|^NUMB\\|^NIMBLE\" SKT.txt | head"
}
```


### [2026-09-07T19:37:16.450Z] TOOL RESULT

```
=== LEW numerus
LAT.txt:39558:numerus multitudinis,' ob multitudf disigne le "pluriel"; multesimus
LAT.txt:42345:numerus
LAT.txt:42379:numerus, -I m,: partie de 1'ensemble class^e a son rang, cate-
=== AFA namus
=== HUB 1041
3601:1041. Zd. nimata- ist dunkel, vgl. Darmesteter, Zend-
=== SKT number/nomad/numb
```


## [2026-09-07T19:37:22.442Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB 1041 ctx\"; sed -n '3595,3615p' HUB.txt\necho; echo \"=== LAT numerus\"; sed -n '42375,42400p' LAT.txt\necho; echo \"=== SKT\"; grep -n -i \"^Number\\|^Nomad\\|^Numb\\|Nimble\" SKT.txt | head"
}
```


### [2026-09-07T19:37:22.512Z] TOOL RESULT

```
=== HUB 1041 ctx
Schon bei Vullers, Radices, s. v.
1039. Np. nam aus *namna- ~ *nabna- wie kam aus ap.
kamna- = *kabna'. Dazu afgh. numd, nUmd u. s. w.
(Geiger).
1040. Die iranischen Dialektformen sind schwerlich ent-
lehnt, also iran. ^namad- anzusetzen.
1041. Zd. nimata- ist dunkel, vgl. Darmesteter, Zend-
Avesta n, p. 45, Anm. — Dazu osset. nimdt, nmdt
Tilz, Filzmantel', s. Verfasser, Etym. und Lautl. der
osset. Sprache, p. 129, Miller-Stackelberg, Fiinf
osset. Erzahlungen p. 62. Skr. namata- Tilz' ist LW.
1043. In phi. anaumet (sprich anomef) ist die Anlaut-
schreibung beibehalten. Np. naumed (= afgh. LW.
naurmd) ist eine neue Zusammensetzung aus na und
umU. Vgl. naumed Fird. I, 133, Z. 2.
1044. Lallwort.
1045. Wird nau (now) gesprochen, wie die Ipt. saw, rau
{soUy rou),
1046. Heisst na/vdxtan urspriinglich : streicheln, streichen,
schlagen'? Es bedeutet ein Instrument spielen (oder
schlagen), singen; schmeicheln, streicheln, liebkosen'.

=== LAT numerus
la nunellatus, -a, -un " numella ligatus, i.e. uinculo quo quadrupedes
alligantur" , CGL Plac. V 34,8.
Etymologie inconnue.
numen: v. nuo.
numerus, -I m,: partie de 1'ensemble class^e a son rang, cate-
gorie, compte et "nombre". Numerus peut se dire de choses qui ne se
comptent pas, comme de cboses qui se comptent: magnus numerus frumenti,
Cic., Verr.8,8,78,17O et magnus piratarum numerus, id. ibid.8,S,a8.
Esse in numero ne veut pas dire exactement "etre au nombre de", mais
"etre dans la cat^gorie de"; cf; aussi parentis numero alicui esse,
Cic. Diu. in Caec.19,Gisqq., numerum alqm obtinere "occuper un certain
rang", par opposition a nullo numero esse; numeris omnibus "dans
toutes les parties". A 1 'epoque imperiale, numeri designe les divi-
sions d’une arm 4 e marquees par un numero d'ordre, les "unites". En
outre numerus a servi a rendre toutes les acceptions techniques du
gr. apl, 9 |xoS "nombre oratoire, mesure, rythme", "nombre grammatical" ,
"la foule, le nombre" (par opposition a la qualit^). Le pl. numeri
traduit Ctpl, 0 |ACH "la Science des nombres". Ancien (Liv., Andr. ), usuel,
class. Panroman sauf esp. et port. (de meme numero). M.L.S994. Celt.:
iri. (nJumir, britt. niner, nifer.
L'abi.numero s'emploie a 1 'epoque archaique avec le sens de "exac¬
tement, pr^cisement, a point nomme, a temps"; et par suite "vite",
et meme "trop vite" par un developpement de sens comparable a celui
de nimis et de fr. trop.Numidae
Ooo
Derivas et composes: numero, Ss: compter, d^nombrer, M.L.5993; nume¬

=== SKT
433:a«ae.  (F.-L.)  XVI  cent.  V.  agile. ^ L.  ttgiiii,  nimble.  liL  easily  driven  aboot.
3559:Clever.  (F.-L.;  tenfmed  with  E.)  !■ BnUcr's  Hudibnu  (1663).  It  took  the  pl«c« of  M.  E.  dtlivrr,  quick,  nimble.  Ch.  proL 84.«»0.  F.  dtlivrt.  free,  prompt,  alcit; compounded  from  L.  de^  prefix,  and  /IBrr. free ;  see  Deliver.  But  apparently  confused with  M.  K.  (livir^  ft  claw,  also  as  adj.  rci'!^ to&eiie,  allied  to  Climb.Cloavei*^  %  Not from  A.  S.  gltiiw,  M.  E.  ^rt(,  skilfal ;  itill less  from  G.  klugW
9841:Lad.  a  youth.  (C.)  M.  E.  Au^<r.«  Irish /aM,  a  youth,  champion;  W.  //oW,  o youth.  Allied  to  Irish  iuth,  nimble,  active. Gael,  iaidir,  ationg,  iuth,  strength;  and  to Goth.  JMgga-iautkt,  a  young  man  ^froni iimdan,  to  growl.
12304:numb.  (E.)  M.  £.  ncfm.  tt&m^H,  pp. aeized,  taki'o,  caught  with,  cvcrpoweied, deprivetl  of  sensation.  Pp.  of  M.  h.  mmen (A.  S.  nimari),  to  take;  see  Nimble. -f* Icel.  Humintt,  bereft,  pp  ol  nema.  to  l.;kc. Vine  (E.)  M.  E.  ni$u,  where  the  hnal •f  is  a  pi.  suffix,  and  ttiit-  is  for  »i;^f.  nine (Layamou),  A.  S.  ii'^ffn,  ttigrn.  nine  + Dit  Ttfj^ti,  Icel.  »/u.  Dan.  nt,  Sw.  M/'^t  G. rteuH,  Goth,  tiiufi,  W.  natt^,  1r.  ma^t,  L. $iouem,  Gk.  ivvt'a  (>l-W^-a).  Skt  «a;'»«rt» nine.
12413:Nomad,  wamlcring.  (Gk. )  Gk.  vofmb; stem  of  I'o/ias,  roaming  in  search  of  pasture. ~Gk.  ro/iof,  a  j>asture,  allotted  abode.— Gk.  vlfiur,  lo  assign.     (^NAM.)
12504:Numb ;  see  Nimble.
12505:Number.  \}t'.  —  ! ..)  F.  n^mhrt.  —  L. numtrum,  ace.  of  numenu,  a  number. .Mlicd  to  Nomad.  (V  NAM.)  I>«r.  oui- numbir.
16291:ble,  to  make  a  low.  heavy  sound. 'io».  E.  rvmmlt,  rnmmU\  M.  E. I  (with  txcrciCCTit  &").  Frequent. leaning  *  to  lepeat  the  sound  p-nm  \ ifun^r,  a  nininur ;  SkL  ru.  to  hum. umouT.  4-  Do.  rommclen,  Dan. lo  nimble,  buzr.
21461:Wight  (a),  nimble,  strong.  (Sd Spenser,  Shep  Kal.,  March,  ot. wight,  valiant.  —  Icel.  vigr,  fit neut.  vigt,  serviceable  (accountini final  /),  Swed.  vig,  oimble,  n, nimbly.  From  Icel  vig  ( •  A war. —  Icel.  vtga.  to  fi  ' weig;in  ^pt.  I.  waik),
```


## [2026-09-07T19:37:45.407Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LAT more\"; sed -n '42400,42418p' LAT.txt\necho; echo \"=== LEW num\"; grep -n \"numerus\\|nummus\" LEW_1910.txt | head\necho; echo \"=== IEC nem\"; grep -n \"^nem\\|^nomos\\|^nomes\" IEC.txt | head -20"
}
```


### [2026-09-07T19:37:45.481Z] TOOL RESULT

```
=== LAT more
Derivas et composes: numero, Ss: compter, d^nombrer, M.L.5993; nume¬
ratio, -tor , -bilis (nor. Oy. = ocpi, 0 p,T]TOC comme innumerabilis du reste
plus frequent et usite dans la prose classique = avcxpu 0 ^iT|TOC); cf.
aussi innumerus (= ocvapi, 0 p,oc)j innumeralis (Lucr.); innumerabilitas
(Cic.), -6i liter, tous mots savants; numeralis t. de gramm.: -e nomen
(Prisc.); numerarius (tardif): i° calculateur; 3 0 -i uocati sunt qui
publicum nummum aerariis inferunt, Isid.Or.9,4; numerius,-a,-um
(tres rare et tard.); numerosus:. i° conforme a la mesure; rythmique
ou rythme (sens classique); 2? abondant, nombreux (epoq. imper.); d'ou
numerositer, -tat, et innumerosus (rares et tardifs).
abnumero (Nigid. ap. Geli.15,3,4); ad- (class. et usuel ), con- (rare,
tardif), d i— (class.), e— (class.) "uis praepositionis perfectiua saepius
uiget" (Thes .), per- (class., mais rare), re- (arch. ), super- (b.lat.),
trans— (Rhet. ad Herenn. ) numero', super—numerarius : qui se trouve
en surnombre (Veg.). Le nom propre Xumerius remonte a ilumasios, cf.
pren. Humasioi datif CIL I 3 3, osq. Niumsle 1 s, et doit se rattacher
a Huma. Sans rapport avec numerus', v. W. Schulze, Lat. Eigenn. 164,197.
On rapproche gr. vejico "j e distribue, je partage"; et, pour le trai-
tement phonetique, on rappelle umerus. Le tout peu clair.

=== LEW num

=== IEC nem
11626:nemă (with variants) “unless; except. Cf. WP II, 336 Ir. namá, prp. & adv. “except; unless; W cf. nam, named, id. (for *nomet? with the re- duced vocalism of Lat. nam in relation to enim, for *et-nem in view ofthe hapax ennam? Speculations in WH:LEW & EM:DELL); ON nema, cj. ‘except; unless; but that; per- haps; say; but Br. némét, id.
11627:nemet- *partition; part, lot. Cf. nemos (1) Gk. némesis, f. ‘indignation; grudge; remorse; goddess of retribution'; Gaul. neméton, nimi- da, n. & f. ‘sacred grove’; OS nimid ‘copse, thicket
11628:nemo ‘turn, bend, bow’; nemos ‘curve, arch, heaven’ Skt. námāmi, v. id.: Av. nam-, v. intr. id.; Tokh. AB nåm-, B nem-, tr. id.; OIr. nem, n. ‘heaven’; Ir. neamb, pl. neimh, m. & f. id.; W nef, pl. nefoedd, f. id.; Br. énv, pl. -u, m. id.; Skt. námas, n. ‘bend, bow
11629:nemos (1) “holding, taking, share’. WP II, 330 Gk. némos, gs: -eos, n. “clearing, pasture, grove'; Lat. nemus, gs: -oris, n. id.; cf. Gaul. nemeto- & variant nimida ‘sacred grove’; OS nimid, s. ‘copse, thicket. (Isophone: Ir. neimb, gs: neimhe, f. ‘poison’, unless = *share'?); Go. niman, sv. 4 (and com. Gmc. *take")
11630:nemos, ios (2) “soft, moist’. See emnos, ios Av. námyo, id.; Per. nam, id.; Alb. i njomé, id.; cf. njom, v. ‘moisten’
11633:nemi — nëqu- (noqu-)
11836:nomos (1) “part, share, division, decision. Cf. nem- (2) Vedic námah ‘pasture’; Per. cf. name "book epistle’; Gk. nomós, nomé, m.f. ‘pasture; abode; district; nómos, m. “law, custom": Lat. cf. numerus, 1, m. ‘number’; Li. namai, mpl. ‘house’; Latv. nams, m. id. (and 'scullery). WP II, 330
11837:nomos, is (2) 'turn, bend'. Cf. nemo and nemos (1) Skt. cf. namráh ‘crooked’; Gk. nomeis, pl. ‘ribs of ship’
```


## [2026-09-07T19:37:48.011Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ namus\"; grep -n \"Namus\\|nāmūs\\|namous\\|nomos\" FVQ_pages.txt | head\necho \"=== FVQ greek nomos\"; grep -n \"νόμος\" FVQ_pages.txt | head\necho \"=== AFM namus page\"; python3 - <<'EOF'\nimport re\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\ncur=None\nfor i,l in enumerate(t,1):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: cur=int(m.group(1))\n    if 'الناموس' in l or 'ناموس' in l: print(i,cur,l[:200])\nEOF"
}
```


### [2026-09-07T19:37:49.328Z] TOOL RESULT

```
=== FVQ namus
=== FVQ greek nomos
=== AFM namus page
3944 None 3 6 الاراعى ` ܢܡܩܐ و شربه اليونالي 94 اي الناموس
```


## [2026-09-07T19:38:03.535Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/numerus",
 "prompt": "Give the Latin entry numerus: etymology (PIE *nem- / *nom-es-o-, de Vaan's view), meaning, and descendants (Italian numero, French nombre, Spanish número, English number)."
}
```


## [2026-09-07T19:38:05.293Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BD%CF%8C%CE%BC%CE%BF%CF%82",
 "prompt": "Give the Ancient Greek entry νόμος: etymology (from νέμω, PIE *nem-), meanings (custom, law), and descendants/derived terms including -νομία (economy, astronomy) and borrowings into Syriac/Arabic/Latin."
}
```


### [2026-09-07T19:38:09.526Z] TOOL RESULT

```
# Latin *numerus*: Etymology and Descendants

## Etymology

The Latin word derives from Proto-Italic *\*nomezos* through rhotacism, ultimately from Proto-Indo-European *\*nem-* meaning "to assign, allot; take." According to de Vaan's etymological dictionary, the word traces back through these ancient language stages to its earliest reconstructed form.

The grammatical sense represents "a semantic loan from Ancient Greek ἀριθμός (arithmós)."

## Meaning

Latin *numerus* carried multiple senses:
- **Number** (quantity)
- **Roman military unit** (a specific troop formation)
- **Collection or quantity** of things
- **Rank or position** (figurative use)
- **Musical rhythm or time**
- **Grammatical number** (singular/plural distinction)
- **Verse or poetry**

## Major Descendants

The word spread throughout Romance languages and beyond:

- **Italian**: *numero*
- **French**: *nombre* (via Old French)
- **Spanish**: *número*
- **English**: *number* (via Middle English from Old French)
- **Portuguese**: *número*
- **Romanian**: *număr*
- **German**: *Nummer*

These descendants demonstrate *numerus*' profound influence on European linguistic development.
```


### [2026-09-07T19:38:11.586Z] TOOL RESULT

```
# Ancient Greek νόμος

## Etymology
The word derives from the verb νέμω (némō, "to distribute") combined with the suffix -ος. This traces back to the Proto-Indo-European root *nem-, which relates to distribution and allocation.

## Primary Meanings
Ancient Greek νόμος carried several interconnected senses:
- Usage and custom (established practices)
- Law and ordinance (formal regulations)
- Melody and strain (musical contexts)
- An ancient song type in music
- A type of coin
- A course of masonry (in construction)

## Major Descendants and Derived Terms

**Compound formations with -νομία:**
- οἰκονομία (oikonomía) → economy
- αὐτόνομος (autónomos) → autonomous
- ἀστυνόμος (astunómos) → city-manager
- παράνομος (paránomos) → lawless

**Language borrowings:**
- Syriac: ܢܡܘܣܐ (nāmōsā)
- Arabic: نَامُوس (nāmūs)
- Latin: nummus (coin, via Doric variant)
- Coptic: ⲛⲟⲙⲟⲥ (nomos)

The word's journey through multiple language families demonstrates its cultural significance in legal and musical contexts across ancient Mediterranean civilizations.
```


## [2026-09-07T19:38:22.289Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ECONOMIC\\|ECONOMY\" AHD_watkins1985.txt | head -5\necho \"=== weik-1 ?\"; grep -n \"^weik-1\\|^weik-\" AHD_watkins1985.txt | head -5"
}
```


### [2026-09-07T19:38:22.371Z] TOOL RESULT

```
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
=== weik-1 ?
1136:weik-'
```


## [2026-09-07T19:38:33.415Z] TOOL CALL #64: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/nem-\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D9%85%D8%A7%D8%B2\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D9%85%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%85%D9%88%D8%B3\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D9%85%D8%B1%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D9%85%D8%B1%D8%A9\" \\\n \"https://en.wiktionary.org/wiki/numerus\" \\\n \"https://en.wiktionary.org/wiki/%CE%BD%CF%8C%CE%BC%CE%BF%CF%82\" \\\n \"https://www.etymonline.com/word/number\" \\\n \"https://www.etymonline.com/word/nomad\" \\\n \"https://www.etymonline.com/word/numb\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 359 (Nem 1/Nem 2/Nemata): PIE *nem-, namaz, namad, namus, nomre, numerus, nomos, number/nomad/numb\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-07T19:38:38.852Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a95b6d0e60668055.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/96de75a7c3f3071d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7edab48dfb0465c4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5c5058016bb5874b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/44085ba8e631c78c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/308a60af7566c049.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2544883c1b92f72e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/195d1d3a55c0dce4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bc5abb9965dff965.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4f4ad3af3068295c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d91cdb99250321d7.txt
```


## [2026-09-07T19:38:46.465Z] TOOL CALL #65: Bash

```json
{
 "command": "ls site/pages/359.jpg 2>/dev/null; pdftoppm -f 359 -l 359 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg359 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T19:38:48.449Z] TOOL RESULT

```
site/pages/359.jpg
total 32000
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 15:38 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61586 Sep  7 12:18 320-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115970 Sep  7 12:18 320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86272 Sep  7 12:18 320-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13284 Sep  7 12:18 320-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   107524 Sep  7 12:27 328-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43713 Sep  7 12:35 331-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135301 Sep  7 12:35 331-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52382 Sep  7 12:41 333-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88345 Sep  7 12:41 333-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68568 Sep  7 12:43 335-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105946 Sep  7 12:43 335-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:57 340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24993 Sep  7 13:57 340-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92337 Sep  7 13:59 342-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92697 Sep  7 13:56 343hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30778 Sep  7 13:56 343-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:52 346-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81599 Sep  7 14:37 350-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99691 Sep  7 14:40 351-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115624 Sep  7 14:43 355-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85914 Sep  7 14:35 358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19549 Sep  7 14:35 358-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74812 Sep  7 14:35 358-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1579505 Sep  7 14:24 afm76.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1055262 Sep  7 14:23 afm77.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1297 Sep  7 15:29 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   153966 Sep  7 13:44 bqt2014_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299343 Sep  7 15:34 bqt2173_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59998 Sep  7 15:38 bqt2210_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11800 Sep  7 14:19 c355_arab2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7474 Sep  7 14:19 c355_conn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10501 Sep  7 14:19 c355_runik2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7270 Sep  7 14:19 c355_runik.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46690 Sep  7 13:44 crop_av3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40759 Sep  7 13:44 crop_heb.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94819 Sep  7 13:44 crop_pers0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78732 Sep  7 13:40 ffd32.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30152 Sep  7 15:34 ffd77_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 15:34 ffd77.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 13:44 ffd82.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb    33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63978 Sep  7 12:35 mk330.py
-rw-rw-r-- 1 sfmqrb sfmqrb    64100 Sep  7 12:34 mk331.py
-rw-rw-r-- 1 sfmqrb sfmqrb    90456 Sep  7 12:42 mk332.py
-rw-rw-r-- 1 sfmqrb sfmqrb    99976 Sep  7 12:34 mk334.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57252 Sep  7 12:38 mk337.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83271 Sep  7 13:58 mk338.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74349 Sep  7 13:57 mk340.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59512 Sep  7 13:57 mk341.py
-rw-rw-r-- 1 sfmqrb sfmqrb    82502 Sep  7 13:57 mk342.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66284 Sep  7 13:55 mk343.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58811 Sep  7 13:57 mk344.py
-rw-rw-r-- 1 sfmqrb sfmqrb    36436 Sep  7 13:51 mk348b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    20510 Sep  7 13:47 mk348.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67410 Sep  7 14:53 mk353.py
-rw-rw-r-- 1 sfmqrb sfmqrb    87481 Sep  7 14:40 mk354.py
-rw-rw-r-- 1 sfmqrb sfmqrb    38634 Sep  7 14:34 mk358.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:42 navak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3021 Sep  7 13:42 navak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1525 Sep  7 13:41 p342_box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1759 Sep  7 13:41 p342_box3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1703 Sep  7 13:41 p342_box.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108903 Sep  7 13:41 p342hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10531 Sep  7 13:39 p343_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30408 Sep  7 13:39 p343_mus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103027 Sep  7 14:19 p355hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86505 Sep  7 14:27 p358_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114524 Sep  7 14:19 p358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    37883 Sep  7 14:20 p358_q2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36134 Sep  7 14:20 p358_q3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4274 Sep  7 14:19 p358_quote.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4152 Sep  7 15:38 p362_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3458 Sep  7 15:35 p362_germ1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2606 Sep  7 15:35 p362_germ2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135659 Sep  7 15:34 p363_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   223838 Sep  7 15:34 p363_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    21223 Sep  7 13:47 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb     5736 Sep  7 14:43 patch354.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb   146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb   128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75312 Sep  7 12:17 pg332.png
-rw-rw-r-- 1 sfmqrb sfmqrb   104609 Sep  7 12:27 pg333hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70886 Sep  7 12:26 pg333.png
-rw-rw-r-- 1 sfmqrb sfmqrb    41782 Sep  7 12:18 pg334_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    97297 Sep  7 12:18 pg334.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58407 Sep  7 12:18 pg334_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88659 Sep  7 12:22 pg335.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57846 Sep  7 12:31 pg336.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60414 Sep  7 12:19 pg337.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65267 Sep  7 13:37 pg338.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63922 Sep  7 13:44 pg339.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:44 pg340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64116 Sep  7 13:39 pg341.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75149 Sep  7 13:40 pg342.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64151 Sep  7 13:39 pg343.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60735 Sep  7 13:42 pg344.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168870 Sep  7 13:42 pg346hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76794 Sep  7 13:39 pg346.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59757 Sep  7 14:29 pg349.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70743 Sep  7 14:25 pg350.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86553 Sep  7 14:25 pg351.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69045 Sep  7 14:18 pg355.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78195 Sep  7 14:27 pg357.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49496 Sep  7 14:19 pg358.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82867 Sep  7 15:38 pg359.png
-rw-rw-r-- 1 sfmqrb sfmqrb    45536 Sep  7 15:36 pg360.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57895 Sep  7 15:38 pg361.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111691 Sep  7 15:34 pg362hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76202 Sep  7 15:29 pg362.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66511 Sep  7 15:33 pg363.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49805 Sep  7 15:37 pg364.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59224 Sep  7 15:34 pg367.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49419 Sep  7 15:35 pg368.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 13:36 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3120575 Sep  7 14:24 skeat1882.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2985742 Sep  7 14:25 skeatdli.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0022.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0158.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4676 Sep  7 14:29 sns_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   135853 Sep  7 14:30 sns_n157.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   129673 Sep  7 14:30 sns_n159.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   113320 Sep  7 14:30 sns_n21.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb      341 Sep  7 13:46 s.py
-rw-rw-r-- 1 sfmqrb sfmqrb   116699 Sep  7 14:30 t1.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


## [2026-09-07T19:38:51.408Z] TOOL CALL #66: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg359.png"
}
```


### [2026-09-07T19:38:51.759Z] TOOL RESULT

```

```


## [2026-09-07T19:38:51.756Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T19:39:09.604Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT nam\"; grep -n \"^nam\\|nāma-\\|nam-\" KNT.txt | head -20"
}
```


### [2026-09-07T19:39:09.653Z] TOOL RESULT

```
=== KNT nam
379:names of the Меде T'azmaspada and of the
1280:name Garma-pada-, c£. Lt. formus ‘hot’. pIE root *g*hen- ‘strike’, OP ja"tiy, Skt. Айли;
1468:name of a goddess with apparently an Iranian name based on an unidentifiable root; Haldite-, an Armenian; Hi"dus, a province-name from Indic, but with Iranian development of the initial s.
1861:name Va"da'-farnah-.
3072:I. The enclitic pronouns are attached to the first word of their sentence or clause or phrase, even though this be шй ‘and’: DB 1.25 Aura- mazdü-maty upastém frabara ‘Ahuramazda bore me aid’; РР} 8 tya-mary Auramazdà frübara ‘(the kingdom) which Ahuramazda conferred upon me’; DPh 9f тат Auramazdà pütuy utä-maiy ийат ‘me may Ahuramazda protect, and my royal house’. But the phrase vašnā Auramazdaha does not count in fixing the position of an enclitic: DB 1.13f vaina Auramazdàha адат-&ат х$йуабтуа Gham ‘by the favor of Ahuramazda I was king of them’; except in two partly restored passages, see under IIT. An enclitic in a dependent clause is sometimes attached to wd preceding a conjunc- tion or relative: DB 4.781 utd-tazy yàvà tauma ahatiy ‘and as long as strength shall be unto thee’; XPa 15 ша-тату tya рий akunaus ‘and what my father built’, but also XPa 19f шй tya-maiy pica kartam ‘and what was built by my father’; DNb 28f yabd-maiy tya kartam vatnühy ‘when thou shalt see what was built by me’. An attributive en- clitic genitive normally precedes the word which it modifies (cf. §309); but the meaning sometimes governs the position, as in Аа 3 apan?yüka-ma ‘my grandfather’s grandfather’, A*Sa 4 [n*yd|kama (for -am-ma, §138.1) ‘my grandfather’, both with am for -miy = -maiy (852.D. The abl. -ma is found only in hacd-ma ‘from me’, standing any- where in its clause. These formulations are vio- lated in three heavily restored passages, but the available space and the other versions favor these restorations: DSf 20 [ava исйтатату ( = -am-maty) akunaus} ‘that he made successful for me’; DSf 28 [hacd-cily ditradasa [arjanam-sary abariya) from afar its ornamentation was brought’; DNb 54f tya partalm-taty as]fiy ‘what is eommunicated to thee’ (this restoration is highly conjectural).
3100:nama-phrase of place intervenes, which has its own
5059:arjana- sb. ‘ornamentation’, as shown by АКК. : si-im-ma-nu-u ‘decoration’ (§84, §126, 8147.1): for meaning, see JAOS 51.208, 53.13, 53.19, Schaeder, Arch. Anz. 47.272-4, against Hz.’s ‘lime- stone’ (AMI 3.52-3) and ‘building material’ (ApI 88-93). Cf. Av. pres. arga- ‘be worth’, Skt. árhati, and Ars. РЫ, arzün, NPers. arzün, Av. arojah- ‘worth, value’, Skt. argha-. — arjanam nsn. DSI 41f; arjanam-Sary DSf 23°.
```


## [2026-09-07T19:39:20.593Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -A20 '\\*nam' CHEUNG.txt | head -60"
}
```


### [2026-09-07T19:39:20.638Z] TOOL RESULT

```
18246:(*nambV-), Awrom. nim ‘damp’ (< Kurd. ?), Gz. nám-o-nà ‘wet’ 
18247-
18248-*NEIR: Sangl. nav-, Yi. nov-/nivd, M. nav-, niv-/nivd- ‘to rain’, Wa. пыу-/поуа ‘to 
18249-moisten, make wet’, Pash. nund, numd ‘wet’, Pash. naw (m.), Sh. namb ‘moisture, 
18250-humidity’, Sariq. nom ‘wet, moist’ 
18251-
18252-*SANSKRIT: abhrá- ‘cloud’ (RV+), nábhas- (n.) ‘moisture, cloud, mass of clouds, 
18253-mist’ (RV+) > EWAia I: 94, II: 13 
18254-
18255-© The verbal forms of *nab are attested in some Pamiri languages. 
18256-
18257-«PIE *neb'- ‘to moisten, be wet’ > LIV: 448 | Pok.: 315 f. 
18258-
18259-*IE COGNATES: Gr. ovvvé get, Extveger ‘is cloudy, clouded; [Zeus] makes cloudy, 
18260-clouded’, Hitt. /nepis-/ (n.) ‘sky’, Gr. уёфос (n.) ‘cloud, mass of clouds’, OCS nebo, 
18261-
18262-
18263-nebes-e (n.) ‘heaven’, OHG nebul (m.), NHG Nebel, etc. 
18264-*REFERENCES: EVP: 52 f.; IIFL II: 233b, 532a, 405b; MacKenzie 1966: 103; MacKenzie, Pahlavi: 57; 
18265-EVS: 49a; WIM 1/2: 709 f.; DKS: 18b; Steblin-Kamenskij 1999: 252; NEVP: 59 
18266-
--
18483:280 *nam 
18484-
18485-
18486-*REFERENCES: Werba 1997: 204 
18487-
18488-
18489:*nam ‘to bend, bow’ 
18490-
18491-*AVESTAN: Y Av. nəm- (nam-) ‘to bend’ || (+ *apa-) ‘to yield, cede, depart, leave’ || 
18492-(+ *fra-) ‘to flee from’, caus. ‘to bend down’ || (+ *ui-) ‘to put, spread apart’ 
18493-= Liste: 40 
18494-
18495-MED. (exc. Caus.); Pres. them.: IND. 35р. YAv. ()fränsmaite (Yt 19.95 Ё), 3р1. YAv. franomonte (Y 
18496-57.18), INJ. 3sg. YAv. арапәтаіа (Yt 19.35 f£), SUBJ. 159. YAv. fra.nmane (Yt 9.4, Yt 17.25), 35р. 
18497-YAv. fränämäite' (Y 57.18, Yt 19.95), 3pl. YAv. frä nomante (Yt 9.4), IMPV. 2sg. YAv. fra(-ca) 
18498-nomar'ha (V 2.10, V 2.18), ҮАУ. vinamanha (V 2.10); Caus.: pres. 3pl. YAv. (fra) namaiieinti (Yt 13.39, 
18499-Yt 14.56), YAv. vi namaiieinti (Yt 13.39). 0 On the long stem vowel -ä- in YAv. “namäite see Kuiper 
18500-1939: 41, Kellens 1984: 115, fn. 6. 
18501-
18502-
18503-*MIDDLE PERSIAN: (+ *apa-) MMP ’bn’m- ‘to cause to go out, depart’ || (+ *abi-) 
18504-BMP ’dynpt /ayinaft/ (pret. stem) ‘to reach, get at, touch’ || (+ *а-) MMP ’n’m- ‘to 
18505-remove, drive away; to remove oneself, go away’ || (+ *fra-) MMP frnm-, prnm- ‘to 
18506-go, proceed’ = DMMPP: 11b, 43b, 156b 
18507-
18508-(+ *apa-) Pres.: SUBJ. 3sg. MMP *’bn’m’d, 3pl. MMP ’bn’m’nd || (+ *abi-) Partic.: perf. pass. BMP 
18509-’dynpt /ayinaft/ || (+ *a-) Pres.: SUBJ. 3pl. MMP ’n’m’nd, IMPV. 2р1. MMP ’n’myd; Partic.: perf. pass. 
--
18553:*namH ‘to strike, beat’ 
18554-
18555-*KHOTANESE: (+ *pati- ?) panam- ‘to touch, feel’ || (+ *pari-) OKh. parnam- ‘to 
18556-touch, feel’ = SGS: 75 
18557-
18558-*NEIR: Oss. I. nemyn/nad, D. nemun/nad ‘to hit, strike’, ? Sh. nimü, (Baj.) nimaw, 
18559-Khf. nimaw, Rosh. nimöw, Bart. nimaw, Orosh. namaw ‘reproach, abuse; regret ?’ 
18560-
18561:© The existence of an Пг. root *namH- ‘to strike, beat’ was first postulated by 
18562-Schmidt 1959: 113 ff., and accepted by Bielmeier 1979: 201; Abaev II: 169 f. The
```


## [2026-09-07T19:39:24.066Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '18510,18552p' CHEUNG.txt"
}
```


### [2026-09-07T19:39:24.115Z] TOOL RESULT

```
MMP "n pt, ’n’pt || (+ *fra-) Pres.: SUBJ. 3pl. MMP ртт па; Partic.: perf. pass. MMP prnpt, BMP plnpt 
/franaft/; Inf.: MMP prnptn 

*PARTHIAN: (+ *apa-) *bnf- ‘to withdraw, depart’ || (+ *abi-) ’bnft (pret. stem) ‘to 
approach, draw near to’ || (+ *fra-) fram- ‘to go forth, depart, proceed’, frn’m- 
(caus.) “о cause to depart, send away’ = Ghilain: 73 | DMMPP: 156b, 12a, 156b 

(+ *apa-) Partic.: perf. pass. ’bnft, ’bnft || (+ *abi-) Partic.: perf. pass. "bnft || (+ *fra-) Partic.: perf. pass. 
frnft, frnpt, Caus.: pres. IND. 3pl. frn?mynd 

*KHOTANESE: nonda-, LKh. nauda- ‘obeisance, worship’ || (+ *pati-) OKh. panam- 
‘to bend’ || (+ *fra-) OKh. hanam-, Khot. hanem- (hanaim-, hana-) ‘to bend down’ || 
(+ *ui-) Khot. binam- ‘to split apart’, LKh. binem- (caus.) ‘to split? = SGS: 69, 146, 
96 f. 

*SOGDIAN: SSogd. nm-, BSogd. nm-, CSogd. nm- ‘to consent, agree, accept’ || (+ 
*pati-) BSogd. ptn’ym- ‘to imitate’ 

Pres.: IND. 35р. dur. CSogd. nmtysq, INJ. 1sg. SSogd. nm’w, ОРТ. 2sg. BSogd. nm’y || (+ neg.) BSogd. 
L’ nm’y; Impf.: IND. 3sg. CSogd. nm’; ’z-Impf.: IND. 3sg. CSogd. nm’z || (+ *pati-) Pres.: IND. 3sg. 
BSogd. ptn’ymt 

*NWIR: Kurd. dà nawin, Awrom. (ara-)namiay/ (ara-)namia- ‘to bend down’ || (+ 
*abi-) NP inaft ‘petition, demand, need’ 

*NEIR: Oss. I. пута, D. nindz ‘bashfulness, customary submissive attitude [of the 
bride]’ || + *uz-) Oss. D. eznemun/zzn&(m)t ‘to move back [of animals]’ 

*MISC: (+ *ni-) Огт. піт-/піпт ek ‘to descend’ 

*SANSKRIT: nam ‘to bend (oneself), bow’ (RV+) = EWAia II: 14 

«PIE *nem- ‘to bend, bow’ = LIV: 453 f. | Pok.: 764 


*nar 281 


*IE COGNATES: Toch. näm- ‘to bow’ 
*REFERENCES: TFL I: 402a Ё; Abaev, Slovar’ I: 228; MacKenzie 1966: 103; Abaev, Slovar’ II: 204 f.; 
DKS: 173a, 210a; Werba 1997: 201 ff.; Cheung 2002: 13, 210
```


## [2026-09-07T19:40:45.502Z] AGENT

Now I'll write the verification file.


## [2026-09-07T19:48:16.624Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\nWIKT_NEM = W + \"Reconstruction:Proto-Indo-European/nem-\"\nWIKT_NAMAZ = W + \"%D9%86%D9%85%D8%A7%D8%B2\"\nWIKT_NAMAD = W + \"%D9%86%D9%85%D8%AF\"\nWIKT_NAMUS = W + \"%D9%86%D8%A7%D9%85%D9%88%D8%B3\"\nWIKT_NOMRE = W + \"%D9%86%D9%85%D8%B1%D9%87\"\nWIKT_NIMRA = W + \"%D9%86%D9%85%D8%B1%D8%A9\"\nWIKT_NUMERUS = W + \"numerus\"\nWIKT_NOMOS = W + \"%CE%BD%CF%8C%CE%BC%CE%BF%CF%82\"\nEO_NUMBER = \"https://www.etymonline.com/word/number\"\nEO_NOMAD = \"https://www.etymonline.com/word/nomad\"\nEO_NUMB = \"https://www.etymonline.com/word/numb\"\n\ndoc = {\n \"pdf_page\": 359,\n \"book_page\": 329,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": []\n}\n\n# ---------------- ENTRY 0 : Nem 1 ----------------\ne0 = {\n \"entry\": 0,\n \"root\": \"Nem 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *nem- 'to assign, allot; to take' (Pokorny 763-764 'nem-1'; Watkins/AHD 'nem-')\",\n \"note\": \"The root, its language label and its gloss are all right, and the whole chart is visibly built out of two articles: Pokorny 763-764 (nem-1) and Klein s.v. 'nimble'. Pokorny's material list for nem-1 opens with 'Avestan nəmah- n. \\\"loan\\\"', continues 'gr. νέμω \\\"divide\\\" ... νομός \\\"distribution; meadowland\\\", νόμος \\\"alignment, order\\\"', 'Latin numerus \\\"number\\\" (*nomes-o-), nummus \\\"currency, coin\\\"' and 'Gothic, Old Saxon, Old English niman, Old High German neman, Old Icelandic nema \\\"take\\\"' - i.e. nodes #1, #4, #8 and (through numb) #15 in Nourai's order. Klein's 'nimble' entry lists the same set in one sentence ('fr. I.-E. base *nem-, \\\"to divide, distribute, allot\\\", whence also Avestic nəmah-, \\\"loan\\\", Gk. νέμειν ... νομός ... νόμος ... L. numerus'), which is why Nourai's KLN page hangs on node #1. Two cross-cutting problems: (a) the Pahlavi-Persian branch (#2-#3) does not belong under this root at all - every modern authority, Bartholomae included, takes namāč / namāz from the homonymous nəmah- 'worship' of root Nem 2 (see node #2); (b) node #3's citation is printed 'BQT:1070' in the book, which is a Borhān page in vol. 2 (letter ج/ح) and cannot be the namāz entry; it is Nourai's own slip, repeated from 'BRT:1070' in the box to its left, for BQT:2167 as cited in entry 1. Wiktionary now derives its Etymology 2 *nem- 'to bend' from this Etymology 1 by the shift 'to distribute' > 'to worship, sacrifice' > 'to bend', so Nourai's Nem 1 / Nem 2 split, while it follows Pokorny, may in the end be one root.\",\n \"note_fa\": \"ریشهٔ «Nem 1» و برچسب زبانی و معنای آن («واگذاردن، گرفتن») درست است: پوکورنی در ص ۷۶۳–۷۶۴ ریشهٔ *nem- را با معنی «گرفتن، سامان دادن، شمردن» می‌آورد و واتکینز نیز «nem-. واگذاردن، بخش کردن؛ همچنین گرفتن». نکتهٔ چشمگیر آن است که همهٔ شاخه‌های این نمودار — اوستایی nəmah- «قرض»، یونانی nomos، لاتینی numerus و ژرمنی niman — در همان مقالهٔ پوکورنی و در مادهٔ nimble فرهنگ کلاین با همین ترتیب آمده‌اند؛ پس نورایی مستقیماً از این دو برداشته است. دو ایراد فراگیر: نخست آنکه شاخهٔ «نماچ/نماز» به این ریشه تعلق ندارد و پژوهش امروزی — و خودِ بارتولمه — آن را از هم‌آوای nəmah- «نیایش، کرنش» زیر ریشهٔ Nem 2 می‌گیرد (بنگرید به گرهٔ ۲)؛ دوم آنکه ارجاع گرهٔ ۳ در کتاب «BQT:1070» چاپ شده که صفحه‌ای از جلد دوم برهان قاطع (حرف ج/ح) است و نمی‌تواند مادهٔ «نماز» باشد — خطای چاپی خودِ نورایی به تأثیر «BRT:1070» جعبهٔ کنارش، و درست آن BQT:2167 است. ویکی‌واژه امروز ریشهٔ *nem- «خم شدن» را نیز از همین *nem- «بخش کردن» می‌داند (با تحول معنایی «بخش کردن» ← «نیایش کردن» ← «خم شدن»)، پس تفکیک Nem 1 / Nem 2 نورایی که از پوکورنی گرفته شده، سرانجام ممکن است یک ریشه باشد.\",\n \"sources\": [WIKT_NEM, EO_NUMBER],\n \"ref_check\": [\n   {\"ref\": \"POK:763\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt line 62524 ff.: 'Root / lemma: nem-1 ... Meaning: to take; to put in order, count, curse, bad name ... Material: Avestan nəmah- n. \\\"loan\\\" ... References: WP. II 330 f., WH. II 158 f. ... Page(s): 763-764'. The German original is POK_02.txt line 6706 'Av. nəmah- n. \\\"Darlehen\\\";'. Nourai's page number is exactly right.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 330-331, '1. nem- \\\"zuteilen, nehmen\\\"'\", \"stance\": \"supports\",\n    \"note\": \"incoming/WLD/WLD_Bd2_pages.txt line 21849: '1. nem- „zuteilen, nehmen'' (aus „sich zuteilen'' oder von der gemeinsamen ...)'; line 21915 adds 'Ursprüngliche Gleichheit von nem- „zuteilen'' (etwa als „beibiegen''?) mit nem- „biegen'' ist nicht wahrscheinlich zu machen' - Walde-Pokorny explicitly keep the two roots apart, which is the position Nourai follows.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. ~751 (AHD_watkins1985.txt line 780) s.v. nem-\", \"stance\": \"supports\",\n    \"note\": \"'nem-. To assign, allot; also to take. 1. Germanic *nem- in: a. Old English niman, to take, seize: NIM, NUMB ... 2. Greek nemein, to allot: NEMESIS. 3. O-grade form *nom- in: a. Greek nomos, portion, usage, custom, law, division, district: NOME, -NOMY; ... (ASTRONOMY) ... c. Greek nomas, wandering in search of pasture: NOMAD ... 4. Perhaps suffixed o-grade form *nom-eso- in Latin numerus, number, division: NUMBER ... [Pok. 1. nem- 763.]' - Nourai's bare 'AHD' refs on nodes #4, #7, #8, #12, #13, #14, #15 all come from this one paragraph.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. 'nomos (1)' and 'nemos (1)' (IEC.txt lines 11836, 11629)\", \"stance\": \"supports\",\n    \"note\": \"'nomos (1) \\\"part, share, division, decision\\\". Cf. nem- (2) Vedic námah \\\"pasture\\\"; ... Gk. nomós, nomé, m.f. \\\"pasture; abode; district\\\"; nómos, m. \\\"law, custom\\\": Lat. cf. numerus, 1, m. \\\"number\\\"; Li. namai, mpl. \\\"house\\\" ... WP II, 330'; and 'nemos (1) \\\"holding, taking, share\\\". WP II, 330 ... Go. niman, sv. 4 (and com. Gmc. \\\"take\\\")'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. 'nimble' (KLN_1966.txt line 25439, leaf 561 = printed p. ~1095)\", \"stance\": \"supports\",\n    \"note\": \"'... fr. I.-E. base *nem-, \\\"to divide, distribute, allot\\\", whence also Avestic nəmah-, \\\"loan\\\", Gk. νέμειν, \\\"to deal out, distribute, allot\\\", νέμεσις ..., νομός, \\\"land allotted, pasture; district, province\\\", νόμος, \\\"anything allotted or assigned; usage, custom; law\\\", L. numerus, \\\"number\\\", Lith. nuoma ... \\\"rent, interest\\\" ... See numb, and cp. nim. Cp. also Nemesis, noma, nomad, nome, ... -nomy, number, numeral, numeric, numismatic ...'\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"nemah 1 : loan, what is given back, a prayer\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Avestan nəmah- n. 'loan' is genuine, but the box conflates it with its homonym. The 'loan' word is a neuter *-es-/-os- stem built on *nem- 'to assign, allot' (lit. 'that which is allotted', Bartholomae: \\\"Eig. 'Zuwendung'?\\\"), morphologically the exact counterpart of Greek nomos and of Latin numerus < *nom-es-o-; Bartholomae compares Gk. νόμος and Lith. nuomas 'interest' in the same line. It is attested only in Vendidad 4.1, the chapter on debts: '... nāit nəmō paitištaraiti, tāyuš nəmahe bavaiti, hazaŋha nəmō.baraŋhe' = \\\"whoever does not give the loan back to a lender becomes a thief of the loan and a robber of the lender\\\" (Bartholomae's rendering, AiW col. 1070), with the derivatives nəmanhant- 'lending' and nəmō.bara- 'one who gives a loan' beside it. Pokorny 763 and Klein s.v. 'nimble' both list precisely this word for the root, so the arrow root -> nəmah- 'loan' is confirmed. What is not confirmed is the third gloss 'a prayer': that belongs to the OTHER nəmah- n., 'Verehrung, Ehrerbietung, Huldigung' (Bartholomae cols. 1069-1070), a separate lemma which Bartholomae marks 'Zum V. nam-' - the verb 'to bend' of Nourai's own root Nem 2 - and for which he cites 'ai. námas- n. \\\"Huldigung\\\"; vgl. mp. namāt, np. namāz \\\"Gebet\\\"'. Hence the node is only plausible: two homonyms have been merged so that the Pahlavi-Persian branch below can hang from this root.\",\n \"derivation_fa\": \"واژهٔ اوستایی nəmah- «قرض، وام» راستین است، ولی این جعبه آن را با هم‌آوایش درآمیخته است. صورتِ «وام» یک ستاک خنثای *-es-/-os- بر پایهٔ ریشهٔ *nem- «واگذاردن، بخش کردن» است (تحت‌اللفظ «آنچه واگذارده می‌شود»؛ بارتولمه: «معنای اصلی Zuwendung؟») و از نظر ساخت درست همتای nomos یونانی و numerus لاتینی (< *nom-es-o-) است؛ بارتولمه در همان سطر آن را با νόμος یونانی و nuomas لیتوانیایی «بهره» می‌سنجد. تنها گواه آن وندیداد ۴٫۱ است، در باب وام‌ها: «... کسی که وام را به وام‌دهنده باز نگرداند، دزدِ وام و راهزنِ وام‌دهنده می‌شود» (فرهنگ ایرانی باستان، ستون ۱۰۷۰)، در کنار مشتق‌های nəmanhant- «وام‌دهنده» و nəmō.bara-. پوکورنی (۷۶۳) و کلاین (مادهٔ nimble) هر دو همین واژه را برای این ریشه می‌آورند، پس پیکانِ ریشه ← nəmah- درست است. اما معنای سومی که نورایی افزوده — «نیایش» — از آنِ nəmah- دیگری است، «ستایش، کرنش، نیایش» (فرهنگ بارتولمه، ستون‌های ۱۰۶۹–۱۰۷۰)، که بارتولمه آن را «از ستاک nam-» می‌داند، همان فعل «خم شدن» ریشهٔ Nem 2، و ذیل آن می‌نویسد: «سنسکریت námas- «کرنش»؛ قی: فارسی میانه namāt، فارسی نو namāz «نماز»». پس این گره تنها با احتیاط پذیرفتنی است: دو هم‌آوا یکی گرفته شده‌اند تا شاخهٔ پهلوی–فارسی از این ریشه آویخته شود.\",\n \"sources\": [WIKT_NEM],\n \"ref_check\": [\n   {\"ref\": \"POK:763\", \"status\": \"supports\",\n    \"note\": \"POK_02.txt line 6706 (German original of p.763): 'Av. nəmah- n. „Darlehen'';' - the very first item of Pokorny's material for nem-1.\"},\n   {\"ref\": \"KLN:1048\", \"status\": \"supports\",\n    \"note\": \"Klein's 'nimble' (KLN_1966.txt line 25439) has 'Avestic nəmah-, \\\"loan\\\"' among the *nem- descendants - exactly the claim. Caveat on the page number: in the 1966 two-volume set this entry falls on leaf 561, i.e. printed p. ~1095, and 'namda' (Nourai's KLN:1026 on entry 2) on leaf 549 = p. ~1071; the 22-page gap between Nourai's two citations matches, so his KLN numbers for the letter N run some 45 pages low - probably taken from the 1971 one-volume printing. Content is right, the page number cannot be reproduced in the 1966 edition.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW col. 1070, s.v. 'j. nəmah- n. \\\"Darlehen\\\"' (BRT.txt line 18975)\", \"stance\": \"supports\",\n    \"note\": \"'j. nəmah- n. \\\"Darlehen\\\": ... \\\"wer einem Darleiher das Darlehen nicht wiedergibt, wird zu einem Dieb des Darlehens, zu einem Räuber am Darlehnsgeber\\\" V.4.1. ... Eig. „Zuwendung''?; s. gr. νόμος, lit. nūmas \\\"Zins\\\".' - the word and the sense are Bartholomae's; note he gives NO Persian descendant here.\"},\n   {\"src\": \"BRT\", \"where\": \"AiW cols. 1069-1070, s.v. 'j., g. nəmah- n. \\\"Verehrung, Ehrerbietung, Huldigung\\\"'\", \"stance\": \"contradicts\",\n    \"note\": \"Same leaf: '... Zum V. nam-: — ai. námas- n. \\\"Huldigung\\\"; vgl. mp. namāt, np. namāz \\\"Gebet\\\"' - the 'prayer' sense and the Persian word belong to this second lemma, i.e. to root Nem 2, not to nəmah- 'loan'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 330 f., '1. nem-'\", \"stance\": \"supports\",\n    \"note\": \"The article Pokorny reprints as nem-1 (WP. II 330 f. is his own reference); WLD_Bd2_pages.txt line 21849 ff. carries the same members, and line 21915 insists that identity with nem- 'biegen' 'ist nicht wahrscheinlich zu machen'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nem- (line 780)\", \"stance\": \"silent\",\n    \"note\": \"Watkins gives the root and its Greek/Latin/Germanic branches but lists no Iranian member at all, so the Avestan word is not corroborated from this side.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"namač : prayer\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Middle Persian namāč / namāz (Book Pahlavi <nmʾc>, with the Aramaic ideogram <OSGDE> = sgdh 'prostration'; MacKenzie CPD p. 57 'namāz ... reverence, prostration, prayer', Nyberg II 135 'namāč'; Manichaean MP and Parthian nmc) is a real word and is indeed the ancestor of NP namāz, but modern scholarship unanimously derives it from the OTHER Avestan nəmah-, 'Verehrung, Huldigung' - the verbal abstract of nam- 'to bend, bow' (Nourai's Nem 2) - not from nəmah- 'loan'. The form is an Iranian *namā-č/-z abstract on that stem (Pāzand namāž), the sense being 'the bowing (before a god)' > 'act of worship' > 'the prescribed prayer'. Nourai's own reference refutes him: Bartholomae's col. 1070 contains BOTH lemmas, and the sentence 'vgl. mp. namāt, np. namāz \\\"Gebet\\\"' stands under 'nəmah- Verehrung ... Zum V. nam-', while the 'Darlehen' lemma has no Persian descendant. Nyberg p. 135 spells it out ('namāč ... - Av. (1069) nəmah-', i.e. Bartholomae's column 1069 = the 'Verehrung' word), as do Horn no. 1040 ('aw. vergl. nemah- \\\"Gebet\\\"; ai. namas-; phl. namāč'), Buck p. 544, Mo'in's footnote in Borhān-e Qāteʿ p. 2167 ('پهلوی namāč، از ایرانی باستان *nam- «خم شدن، تعظیم کردن»') and Wiktionary (Proto-Iranian *námah < PII *námas < PIE *némos, from *nem- 'to bend'). The chart's own NOTE, which reports BQT:2167, POK:764 and SYN:544 as the dissenting view, in fact reports the standard view; the arrow drawn here is the minority - indeed unsupported - one.\",\n \"derivation_fa\": \"فارسی میانهٔ namāč / namāz (در پهلوی کتابی ⟨nmʾc⟩ با هزوارش آرامی ⟨sgdh⟩ «سجده»؛ مکنزی، فرهنگ کوچک پهلوی ص ۵۷: «namāz، کرنش، سجده، نماز»؛ نیبرگ ج۲ ص ۱۳۵ «namāč»؛ فارسی میانهٔ مانوی و پارتی nmc) واژه‌ای راستین و نیای «نماز» فارسی است، اما پژوهش امروزی یکدست آن را از nəmah- دیگرِ اوستایی، یعنی «ستایش، کرنش»، مشتقِ ستاک nam- «خم شدن» (همان ریشهٔ Nem 2 نورایی) می‌گیرد، نه از nəmah- «وام». ساخت آن اسم‌مصدرِ ایرانیِ *namā-č/-z بر همان ستاک است (پازند namāž) و تحول معنایی «کرنش در برابر خدا» ← «پرستش» ← «نمازِ واجب» است. مرجع خودِ نورایی او را رد می‌کند: ستون ۱۰۷۰ بارتولمه هر دو مادّه را دارد و جملهٔ «قی: فارسی میانه namāt، فارسی نو namāz «نماز»» ذیل «nəmah- ستایش ... از ستاک nam-» آمده است، در حالی که مادهٔ «وام» هیچ بازماندهٔ فارسی ندارد. نیبرگ (ص ۱۳۵: «namāč ... اوستایی (۱۰۶۹) nəmah-»)، هرن (شمارهٔ ۱۰۴۰)، باک (ص ۵۴۴)، حاشیهٔ معین در برهان قاطع (ص ۲۱۶۷: «پهلوی namāč، از ایرانی باستان nam- (خم شدن، تعظیم کردن)») و ویکی‌واژه همه همین را می‌گویند. یادداشتِ خودِ نمودار که این دیدگاه را «نظرِ دیگران» می‌نماید، در واقع نظرِ رایج است و پیکانِ کشیده‌شده در اینجا بی‌پشتوانه است. داوری: پژوهش امروزی این پیکان را رد می‌کند.\",\n \"sources\": [WIKT_NAMAZ],\n \"ref_check\": [\n   {\"ref\": \"BRT:1070\", \"status\": \"contradicts\",\n    \"note\": \"BRT.txt leaf containing cols. 1069-1072: under 'j., g. nəmah- n. \\\"Verehrung, Ehrerbietung, Huldigung, Ehrfurcht(sbezeigung)\\\"' Bartholomae closes 'Zum V. nam-: — ai. námas- n. \\\"Huldigung\\\"; vgl. mp. namāt, np. namāz \\\"Gebet\\\"'; the separate lemma 'j. nəmah- n. \\\"Darlehen\\\"' on col. 1070a ends 'Eig. \\\"Zuwendung\\\"?; s. gr. νόμος, lit. nūmas \\\"Zins\\\"' with no Persian word. So the cited column supports the Nem 2 derivation and contradicts this arrow.\"}\n ],\n \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, p. 135 (leaf 150 of NYB_vol2_glossary.txt) s.v. namāč\", \"stance\": \"contradicts\",\n    \"note\": \"'... — Av. (1069) namah-; MPrthPrs nmc; FrP 19 *SGDH = nm'c, but Cod. 8, XVII, 7 nm'š with NP gl. namāj; Paz. namāž; NP namaz.' Nyberg points to Bartholomae's column 1069, the 'Verehrung' word, not 1070's 'Darlehen'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 57 (PHD.txt line 494)\", \"stance\": \"partial\",\n    \"note\": \"'namāz [OSGDE < A sgdh; nm'c | = M, N ~] reverence, prostration, prayer. ~ burdan: pay homage.' MacKenzie confirms the word and its Aramaic ideogram (sgdh 'prostration') but gives no etymology; note he reads the Book Pahlavi <c> as /z/, i.e. namāz, beside Nyberg's namāč.\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss p. 233 no. 1040 (HRN.txt leaf 254)\", \"stance\": \"contradicts\",\n    \"note\": \"'1040. nemāz \\\"Gebet\\\" ... aw. vergl. nemah- \\\"Gebet\\\"; ai. namas-; phl. v. namāč (pāz. namāš). ... Da alle neuiranischen Formen auf die mittelpersische charakteristische Neubildung namāč zurückgehen, so halte ich dieselben sämmtlich für Lehnwörter.'\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāteʿ (Moʿin) p. 2167, footnote 4 on نماز (incoming/BQT/BQT_v4_pages.txt, pdf page 250)\", \"stance\": \"contradicts\",\n    \"note\": \"'۴ - پهلوی namāč، از ایرانی باستان nam- (خم شدن، تعظیم کردن) «بارتولمه ...؛ نیبرگ ص ۱۳۵»؛ ورک: هوبشمان ۱۰۴۰؛ قی: اوستایی nəmah- (دعا)، هندی باستان namas-، پازند namāž ... کردی nimēž، گیلکی namāz - مجازاً عبادت مخصوص مسلمانان.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 9.14 'BEND', p. 544 (SYN.txt leaf 595)\", \"stance\": \"partial\",\n    \"note\": \"'Skt. namati mostly intr., Av. namaiti intr., caus. Skt. nāmayati, Av. nāmayeiti trans., Skt. namas-, Av. nəmah- \\\"bending, homage\\\", Toch. nām- \\\"incline, bow\\\" ... Walde-P. 2.331 f.' Buck files nəmah- 'homage' under 'bend'; he says nothing about the Pahlavi word, so on the Pahlavi step he is only indirect.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"namâz «نماز» : prayer\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The arrow itself - Pahlavi namāč/namāz -> New Persian namāz - is textbook: Book Pahlavi <nmʾc> already stands for /namāz/ (the Pahlavi letter <c> regularly writes /z/, cf. <rwc> = rōz 'day'), Pāzand namāž, and NP نماز continues it unchanged, with the Islamic specialisation 'the five prescribed ṣalāt' beside the older 'obeisance, homage' still alive in the Shāhnāme idiom namāz burdan 'to make obeisance' - which is exactly what the Ferdowsī couplet in the box illustrates ('چو نزدیک رستم فراز آمدند / پیاده به رسم نماز آمدند'), quoted by Nūshīn in the Shāhnāme glossary s.v. نماز (بردن). From Persian the word was carried into Turkic (Ottoman/Turkish namaz), Indo-Aryan (Urdu, Bengali), Georgian, Armenian, Russian and even Thai ละหมาด. Only the placement is wrong: this box hangs from a root ('assign, take') that does not own it, and it is duplicated - correctly - as node #3 of entry 1. Note also the citation: the printed page really says 'BQT:1070', which is a page in Borhān vol. 2 (letters ج/ح) and cannot be the نماز article; the correct page, cited by Nourai himself in entry 1, is BQT:2167. The extraction is faithful; the slip is the book's, evidently caught from 'BRT:1070' in the box to its left.\",\n \"derivation_fa\": \"خودِ این پیکان — فارسی میانهٔ namāč/namāz ← «نماز» فارسی نو — از نمونه‌های درسی است: املای پهلوی کتابی ⟨nmʾc⟩ همان /namāz/ را می‌نویسد (حرف ⟨c⟩ در پهلوی به‌قاعده /z/ را می‌نمایاند، مانند ⟨rwc⟩ = rōz «روز»)، در پازند namāž، و «نماز» فارسی نو بی‌دگرگونی ادامهٔ آن است؛ با این تخصیص معنایی که در دورهٔ اسلامی «صلاتِ پنج‌گانه» شد، در حالی که معنای کهن‌ترِ «کرنش، تعظیم» در ترکیب «نماز بردن» شاهنامه زنده مانده است — و همان بیتِ درون جعبه («چو نزدیک رستم فراز آمدند / پیاده به رسم نماز آمدند») گواه همین معناست، که نوشین در واژه‌نامک ذیل «نماز (بردن)» آورده است. از فارسی به ترکی عثمانی، اردو، بنگالی، گرجی، ارمنی، روسی و حتی تایلندی رفته است. تنها ایراد، جای‌گذاری است: این جعبه از ریشه‌ای آویخته که از آنِ آن نیست و همین گره در ورودیِ Nem 2 (گرهٔ ۳) به‌درستی تکرار شده است. دیگر آنکه ارجاعِ چاپ‌شده «BQT:1070» است که صفحه‌ای از جلد دوم برهان (حرف ج/ح) است و نمی‌تواند مادهٔ «نماز» باشد؛ درستش BQT:2167 است که خودِ نورایی در ورودی بعد آورده. خطای خوانش اسکن نیست، خطای چاپی کتاب است و پیداست از «BRT:1070» جعبهٔ کنارش سرایت کرده.\",\n \"sources\": [WIKT_NAMAZ],\n \"error_in\": \"book\",\n \"book_prints\": \"BQT:1070\",\n \"correct_form\": \"BQT:2167\",\n \"ref_check\": [\n   {\"ref\": \"BQT:1070\", \"status\": \"not_found\",\n    \"note\": \"Not a namāz page. Nourai's BQT numbering is the continuous pagination of the Amir Kabir set, in which p. 1070 falls in vol. 2 (ث/ج-...), while نماز is on p. 2167 - verified: in incoming/BQT/BQT_v4_pages.txt the نماز article is on pdf page 250, نمد on 252 and ناموس on 189, and 2167-250 = 2169-252 = 2106-189 = 1917, so the offset is uniform and Nourai's other three BQT numbers on this page are all exact. The printed page 329 of the book itself shows 'BQT:1070' (see the PNG copied to data/verification/sources/refs/ocr/BOOK/359.png), so this is the author's misprint, not an extraction error.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāteʿ p. 2167 s.v. نماز (pdf page 250 of vol. 4)\", \"stance\": \"supports\",\n    \"note\": \"Headword: 'نماز - بفتح اول و ثانی بالف کشیده و بزای نقطه‌دار، بمعنی بندگی و اطاعت و ادای طاعت و سجود و پرستش و خدمتگاری و فرمان‌برداری باشد'; Moʿin's footnote 1 adds 'در اصطلاح، عبادت مخصوص و واجب مسلمانان که پنج بار در شبانه‌روز ادا کنند و آن را بعربی صلاة گویند', with Sanāʾī's line 'در طریقت کجا روا باشد / دل به بتخانه رفته، تن به نماز'.\"},\n   {\"src\": \"FSF\", \"where\": \"Nūshīn, Vāzhe-nāmak, printed p. 331 (leaf 444 of FSF_pages.txt) s.v. نماز (بردن)\", \"stance\": \"supports\",\n    \"note\": \"The page carries the very couplet of the chart - 'چو نزدیک رستم فراز آمدند / [پیاده به رسم نماز آمدند]' - among the Shāhnāme instances of نماز بردن 'to make obeisance'. The scan's printed page is 330-331, not Nourai's 328; the offset of this printing (printed = leaf - 113) differs, so only the page number is doubtful, not the content.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien no. 1040, p. ~103 (HUB.txt line 3601 ff.)\", \"stance\": \"partial\",\n    \"note\": \"'1040. Die iranischen Dialektformen sind schwerlich entlehnt, also iran. *namad- [read *namāz-/namāč-] anzusetzen.' Hübschmann contradicts Horn's claim that the Kurdish/Balochi/Pashto forms are loans from Middle Persian, positing an inherited Old Iranian formation instead - a refinement of the same Nem 2 etymology.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Greek\", \"words\": \"nomos : law\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Ancient Greek νόμος 'usage, custom, law' is the o-grade action noun of νέμω 'to deal out, distribute, allot' (νόμος < *nom-o-s), the same formation as νομός 'pasture, allotted land, district' differing only in accent; the semantic path is 'what is apportioned' > 'established usage' > 'statute, law' (Herodotus, the Attic orators). Pokorny 763 lists 'gr. νέμω ... νομή \\\"distribution; meadowland\\\", νόμος \\\"alignment, order\\\", νομίζω, νόμισμα \\\"custom, usage, gebräuchliche Geldwährung\\\"' under nem-1; Watkins files it as 'O-grade form *nom- in: a. Greek nomos, portion, usage, custom, law, division, district'. Nourai's language label and gloss are right; the only thing his 'law' gloss leaves out is that the same word underlies the Arabic branch precisely in the sense 'divine law' (node #5).\",\n \"derivation_fa\": \"νόμος یونانی باستان «رسم، عرف، قانون» اسم‌مصدر با واکهٔ o از νέμω «بخش کردن، واگذاردن» است (νόμος < *nom-o-s)، همان ساختی که νομός «چراگاه، زمینِ واگذارشده، ناحیه» دارد و تنها در جای تکیه با آن فرق می‌کند؛ تحول معنایی «آنچه بخش‌شده» ← «رسمِ جاافتاده» ← «قانون» است (هرودوت و خطیبان آتنی). پوکورنی در ص ۷۶۳ ذیل nem-1 «νέμω ... νομή، νόμος «سامان، نظم»، νομίζω، νόμισμα» را می‌آورد و واتکینز آن را «صورت واکهٔ o یعنی *nom-: یونانی nomos، بهره، رسم، عرف، قانون، بخش، ناحیه» می‌داند. برچسب زبانی و معنای نورایی درست است؛ ادعای او در اینجا پذیرفتنی است.\",\n \"sources\": [WIKT_NOMOS, EO_NOMAD],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 780 s.v. nem-: '3. O-grade form *nom- in: a. Greek nomos, portion, usage, custom, law, division, district: NOME, -NOMY; ...' - exactly the node.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 763 (POK_full.txt line 62533 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'gr. νέμω divide from ... νομή \\\"distribution; meadowland\\\", νόμος \\\"alignment, order\\\", νομίζω \\\"see, observe as geltend an\\\", νόμισμα \\\"custom, custom, Einrichtung, gebräuchliche Geldwährung\\\"'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. nome, nomad (KLN_1966.txt lines 25545, 25541)\", \"stance\": \"supports\",\n    \"note\": \"'nome ... Gk. νομός, \\\"land allotted, pasture; district, province\\\". See nomad'; 'nomad ... fr. νομός, \\\"land allotted, pasture; district, province\\\", which is rel. to νέμειν, \\\"to deal out, distribute, allot\\\", fr. I.-E. base *nem-'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Nomad (SKT.txt line 12413)\", \"stance\": \"supports\",\n    \"note\": \"'Nomad, wandering. (Gk.) Gk. νομάδ-, stem of νομάς, roaming in search of pasture. — Gk. νομός, a pasture, allotted abode. — Gk. νέμειν, to assign. (√NAM.)'\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Arabic\", \"words\": \"nâmŭs : law, rules\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Arabic نَامُوس nāmūs 'divine law, revealed law; the angel who brings it (Gabriel); confidant of secrets' is indeed the Greek νόμος, but it did not come straight from Greek: the standard account (Wiktionary with citations; Tobia al-ʿUnaysī; Fraenkel's school on Aramaic transmission) is Greek νόμος -> Classical Syriac ܢܡܘܣܐ nāmōsā -> Arabic nāmūs, the long -ū- and the -s of the Arabic form reflecting the Syriac status absolutus/emphaticus rather than a direct Greek borrowing. It entered Arabic before Islam through Christian-Aramaic religious vocabulary (nāmōsā is the standard Peshitta word for the Mosaic Law), which is why the earliest Arabic senses are 'divine law' and, in the sīra, the epithet of Gabriel (Waraqa b. Nawfal's 'this is the nāmūs who came to Moses'). The chart's Greek -> Arabic arrow is therefore right in substance but skips the Syriac step; hence plausible rather than confirmed. Nourai's own gloss 'law, rules' matches Moʿin's bracketed 'عادت، شریعت' and the Borhān footnote.\",\n \"derivation_fa\": \"«ناموس» عربی به معنی «شریعت، قانون الهی؛ فرشتهٔ وحی (جبرئیل)؛ صاحبِ راز» همان νόμος یونانی است، اما یک‌راست از یونانی نیامده: روایت پذیرفته‌شده (ویکی‌واژه با ارجاع، طوبیا العنیسی، و سنت فرنکل در باب وام‌واژه‌های آرامی) چنین است: یونانی νόμος ← سریانی ܢܡܘܣܐ nāmōsā ← عربی nāmūs؛ کشیدگی ‎-ū-‎ و ‎-s‎ پایانی صورتِ عربی بازتاب صورتِ سریانی است، نه وام‌گیری مستقیم از یونانی. این واژه پیش از اسلام از راه واژگان دینی مسیحی–آرامی به عربی رسید (nāmōsā در ترجمهٔ پشیطا برابرِ شریعت موسی است) و همین است که کهن‌ترین معناهای عربی آن «شریعت» و در سیره لقبِ جبرئیل است («هذا الناموس الذی جاء موسی»، گفتهٔ ورقة بن نوفل). پس پیکانِ یونانی ← عربی در گوهر درست است ولی حلقهٔ سریانی را نادیده گرفته؛ از این رو «با احتیاط پذیرفتنی».\",\n \"sources\": [WIKT_NAMUS, WIKT_NOMOS],\n \"ref_check\": [\n   {\"ref\": \"BQT:2106\", \"status\": \"supports\",\n    \"note\": \"Borhān-e Qāteʿ p. 2106 = pdf page 189 of vol. 4 (incoming/BQT/BQT_v4_pages.txt line 7553), Moʿin's footnote 5 on ناموس: '[ناموس]، از یونانی nomos بمعنی عادت و شریعت ... در عربی «ناموس» صاحب راز آگاه بر نهانی ... و نام جبرئیل علیه‌السلام ... و شریعت «اقرب‌الموارد» و نیز ... بمعنی قانون و حکم آید.' Greek origin and the 'law, rules' gloss are exactly as drawn.\"},\n   {\"ref\": \"MON:4629\", \"status\": \"partial\",\n    \"note\": \"The six-volume Moʿin is not online and page numbers cannot be mapped; the entry text in the 2-vol Adena condensation (MON_part2.txt line 73100) reads 'ناموس: [یو.] (عادت، شریعت) (ا.) شریعت، احکام الهی. قانون، قاعده. وحی. فرشته، ملک. (اخ.) جبرئیل ... آبرو، عزت، احترام ... عفت، عصمت، پاکدامنی. زنان یک خانواده وابسته به یک مرد ... ج. نوامیس.' - Moʿin's Greek tag and both glosses of nodes #5 and #6 confirmed; only the page is unverifiable (4629 < 4815 for نمره is at least alphabetically consistent).\"}\n ],\n \"consulted\": [\n   {\"src\": \"TAD\", \"where\": \"Tobia al-ʿUnaysī, Tafsīr al-alfāẓ al-dākhila, s.v. ناموس (TAD_pages.txt line 2740)\", \"stance\": \"supports\",\n    \"note\": \"'ناموس - يوناني νόμος معناه عادة وشريعة وسنة' - 'nāmūs: Greek nomos, its meaning is custom, law and practice.'\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qurʾān (FVQ_pages.txt / FVQ.txt)\", \"stance\": \"silent\",\n    \"note\": \"grep for 'namus', 'nāmūs' and 'νόμος' returns nothing - nāmūs is not Qurʾanic, so Jeffery has no entry; a negative but expected result.\"},\n   {\"src\": \"AFM\", \"where\": \"Addī Shīr, al-Alfāẓ al-fārisiyya al-muʿarraba (AFM_pages.txt line 3944)\", \"stance\": \"partial\",\n    \"note\": \"The only hit for ناموس is a badly OCR'd line pairing a Syriac form ܢܡܩܐ with 'اليوناني ... اي الناموس', i.e. Addī Shīr too knows the word through Syriac/Greek, not Persian; the line is too corrupt to quote as evidence.\"},\n   {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen\", \"stance\": \"silent\",\n    \"note\": \"grep for 'namus'/'nomos'/'νόμος' in AFA.txt finds nothing; the word is not in Fraenkel's list, so the Aramaic route rests on the Syriac lexica and Wiktionary's citations.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 6, \"lang\": \"Persian\", \"words\": \"nâmŭs «ناموس» : rules, dignity, family\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian ناموس nāmūs is an Arabic loan (Wiktionary: 'borrowed from Arabic نَامُوس'), inherited with the whole Arabic sense-range and then developed further in Persian: from 'divine law, statute' (still the first gloss in Borhān and Moʿin) through 'reputation, renown' to the dominant modern senses 'honour, moral reputation; chastity' and, by metonymy, 'the womenfolk of a family' - the three glosses Nourai gives ('rules, dignity, family'). Borhān-e Qāteʿ p. 2106 lists them in that order ('بمعنی ... بانگ و آوازه ... و بمعنی عصمت و عفت هم هست ... و ملائکه ... و احکام الهی'), and Moʿin's footnote 7 remarks 'باین معنی امروزه بیشتر متداول است' of the 'chastity' sense. From Persian it spread through Ottoman Turkish to Turkish namus, Urdu nāmūs, Georgian ნამუსი, Armenian նամուս and Ossetic/Russian намыс. The empty refs= on this node is not a problem: the box inherits BQT:2106 / MON:4629 from its parent, and both cover the Persian word.\",\n \"derivation_fa\": \"«ناموس» فارسی وام‌واژه‌ای عربی است (ویکی‌واژه: «وام‌گرفته از عربی نَاموس») که همهٔ گسترهٔ معنایی عربی را با خود آورده و سپس در فارسی پیش رفته است: از «شریعت، حکم الهی» (که هنوز نخستین معنای برهان و معین است) به «آوازه، شهرت» و از آن به معناهای غالبِ امروزی «عِرض و آبرو؛ عصمت و پاکدامنی» و به مجاز «زنانِ خانواده» — همان سه معنایی که نورایی آورده. برهان قاطع در ص ۲۱۰۶ همین‌ها را به ترتیب می‌آورد و معین در پانویس ۷ دربارهٔ معنای «عفت» می‌نویسد «باین معنی امروزه بیشتر متداول است». از فارسی به ترکی عثمانی و از آنجا به ترکی namus، اردو، گرجی، ارمنی و روسی/آسی намыс رفته است. خالی بودن ارجاعِ این جعبه ایرادی نیست، چون BQT:2106 و MON:4629 جعبهٔ مادر هر دو واژهٔ فارسی را هم پوشش می‌دهند. ادعای نورایی درست است.\",\n \"sources\": [WIKT_NAMUS],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The node carries no refs of its own; the parent's BQT:2106 (checked: it is the Persian dictionary article on ناموس itself, so it covers this node too) and MON:4629 are the effective references.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāteʿ p. 2106 s.v. ناموس (pdf page 189, lines 7539-7580)\", \"stance\": \"supports\",\n    \"note\": \"'ناموس - بر وزن قاموس، بمعنی ... بانگ و آوازه، و صاحب سرّ و خانه و منزل باشد، و بمعنی عصمت و عفت هم هست، و جنگ و جدال را هم گفته‌اند، و ملائکه، و احکام الهی را نیز گویند'; sub-entries 'ناموس اکبر' and 'ناموس‌گاه' follow.\"},\n   {\"src\": \"MON\", \"where\": \"Moʿin (2-vol Adena condensation) s.v. ناموس (MON_part2.txt line 73100)\", \"stance\": \"supports\",\n    \"note\": \"'ناموس: [یو.] (عادت، شریعت) ... قانون، قاعده ... آبرو، عزت، احترام ... عفت، عصمت، پاکدامنی. زنان یک خانواده وابسته به یک مرد ... ج. نوامیس' - Nourai's 'rules, dignity, family' in Moʿin's own order.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 7, \"lang\": \"English\", \"words\": \"-nomy, economy, astronomy\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All three items go back to Greek νόμος / νέμειν. The combining form -nomy is Greek -νομία 'management, ordering' (via Latin -nomia and French -nomie), whence anomie, antinomy, autonomy, Deuteronomy, metronome. Astronomy is Greek ἀστρονομία 'star-ordering' (ἄστρον + -νομία), through Latin astronomia and Old French astronomie, in English from c. 1200. Economy is Greek οἰκονομία 'household management' (οἶκος 'house' + the νέμειν element, via οἰκονόμος 'steward'), Latin oeconomia, French économie, English 1530s; note that Watkins indexes ECONOMY under the root of οἶκος (weik-1) rather than under nem-, so the second element only is from this root - a bookkeeping detail, not a disagreement. Nourai's arrow (Greek nomos -> these English words) is therefore right, though these are learned borrowings through Latin and French, not direct Greek-to-English descent.\",\n \"derivation_fa\": \"هر سه واژه به νόμος / νέμειν یونانی بازمی‌گردند. جزءِ ترکیبیِ ‎-nomy‎ همان ‎-νομία‎ یونانی «تدبیر، سامان‌دهی» است (از راه لاتینی ‎-nomia‎ و فرانسویِ ‎-nomie‎) که در anomie، antinomy، autonomy و Deuteronomy دیده می‌شود. astronomy از ἀστρονομία یونانی «سامانِ ستارگان» (ἄστρον + ‎-νομία‎) از راه لاتینی astronomia و فرانسوی کهن astronomie، در انگلیسی از حدود ۱۲۰۰ م. economy از οἰκονομία «تدبیر خانه» (οἶκος «خانه» + همان جزءِ νέμειν، از οἰκονόμος «کارپرداز»)، لاتینی oeconomia، فرانسوی économie، در انگلیسی از دههٔ ۱۵۳۰. یادآوری: واتکینز economy را زیر ریشهٔ οἶκος (یعنی weik-1) فهرست کرده، نه زیر nem-، پس فقط جزء دومِ آن از این ریشه است — نکته‌ای فهرست‌نگارانه، نه مخالفت. پیکانِ نورایی درست است، هرچند این‌ها وام‌واژه‌های کتابی از راه لاتینی و فرانسوی‌اند نه بازماندهٔ مستقیم یونانی در انگلیسی.\",\n \"sources\": [EO_NOMAD, WIKT_NOMOS],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"AHD_watkins1985.txt line 780 lists under nem- '3.a. Greek nomos ...: NOME, -NOMY; ANOMIE, ANTINOMIAN, ANTINOMY, (ASTRONOMER), (ASTRONOMY), AUTONOMOUS, BINOMIAL, DEUTERONOMY, METRONOME ...' - '-NOMY' and '(ASTRONOMY)' are there verbatim, but ECONOMY is not: the index (line 1441) files 'ECONOMY weik-1', i.e. under 'house'. Partial for that one word only.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. nomad / nome and words there referred to (KLN_1966.txt lines 25541-25545)\", \"stance\": \"supports\",\n    \"note\": \"Klein's 'nimble' cross-reference list ends '... Nomeus, Nomic, nomistic, nomo-, -nomy, number, numeral, numeric, numismatic ...', putting -nomy under *nem-.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Nomad (SKT.txt line 12413)\", \"stance\": \"supports\",\n    \"note\": \"Skeat traces νομός to νέμειν 'to assign' under the same root marker (√NAM), the base of the -nomy compounds.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 8, \"lang\": \"Latin\", \"words\": \"numerus : a portion, a number\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin numerus 'a part of a whole assigned to its rank; category, count, number' goes back to *nom-es-o- > Proto-Italic *nomezos, with regular intervocalic rhotacism (-s- > -r-) and the weakening -e- > -e/u- of the medial syllable, from the o-grade of *nem- 'to allot' - i.e. it is the Latin twin of Greek νόμος and of Avestan nəmah-. Pokorny 763 states it flatly ('Latin numerus \\\"number\\\" (*nomes-o-)'), de Vaan (via Wiktionary) reconstructs *nomezos, and the semantics ('esse in numero' = 'to be in the category of', 'numerum obtinere' = 'to hold a rank') still show the original 'apportioned share', which is exactly Nourai's gloss 'a portion, a number'. Two authorities hedge: Watkins writes 'Perhaps suffixed o-grade form *nom-eso- in Latin numerus', and Ernout-Meillet, after 'On rapproche gr. νέμω \\\"je distribue, je partage\\\"', add 'Le tout peu clair'. The connection is nevertheless the received one and I take the node as confirmed, with that caveat noted.\",\n \"derivation_fa\": \"numerus لاتینی «بخشی از یک کل که در جای خود رتبه‌بندی شده؛ رده، شمار، عدد» از *nom-es-o- ← ایتالیکِ آغازین *nomezos می‌آید، با ابدالِ قاعده‌مندِ ‎-s-‎ میان‌واکه‌ای به ‎-r-‎ (rhotacism) و تحلیلِ واکهٔ هجای میانی، از صورتِ واکهٔ o ریشهٔ *nem- «واگذاردن» — یعنی همزادِ لاتینیِ νόμος یونانی و nəmah- اوستایی. پوکورنی در ص ۷۶۳ آن را بی‌درنگ می‌آورد («لاتینی numerus «عدد» (*nomes-o-)») و دِ فان صورت *nomezos را بازمی‌سازد؛ معنای کهن نیز در تعبیرهایی چون esse in numero «در ردهٔ ... بودن» و numerum obtinere «رتبه‌ای داشتن» پیداست، که درست همان معنای «بهره، بخش» است که نورایی آورده. دو مرجع احتیاط می‌کنند: واتکینز می‌نویسد «شاید صورتِ پسوندی *nom-eso-» و ارنو–مِیه پس از «آن را با νέμω یونانی می‌سنجند» می‌افزایند «همهٔ اینها روشن نیست». با این همه، این ریشه‌شناسی پذیرفتهٔ همگانی است و گره را درست می‌شمارم.\",\n \"sources\": [WIKT_NUMERUS, EO_NUMBER],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 780: '4. Perhaps suffixed o-grade form *nom-eso- in Latin numerus, number, division: NUMBER; ENUMERATE, SUPERNUMERARY. [Pok. 1. nem- 763.]' - the arrow as drawn, with Watkins' own 'perhaps'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 763 (POK_full.txt line 62544)\", \"stance\": \"supports\",\n    \"note\": \"'Latin numerus \\\"number\\\" (*nomes-o-), nummus \\\"currency, coin\\\" (from gr. νόμιμος \\\"allowed, legitimate, lawful, ordinary\\\")'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. numerus (LAT.txt lines 42379-42418)\", \"stance\": \"partial\",\n    \"note\": \"'numerus, -ī m.: partie de l'ensemble classée à son rang, catégorie, compte et \\\"nombre\\\" ... Esse in numero ne veut pas dire exactement \\\"être au nombre de\\\", mais \\\"être dans la catégorie de\\\" ... Panroman sauf esp. et port. (de même numero). M.L.5994.' and at the end: 'On rapproche gr. νέμω \\\"je distribue, je partage\\\"; et, pour le traitement phonétique, on rappelle umerus. Le tout peu clair.'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 330 f., '1. nem-'\", \"stance\": \"supports\",\n    \"note\": \"The Latin word stands among the members of WP's nem- 'zuteilen' (WP. II 330 f. = the article Pokorny reprints, where 'lat. numerus' is listed with nummus).\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. nomos (1) (IEC.txt line 11836)\", \"stance\": \"supports\",\n    \"note\": \"'... Gk. nomós, nomé ... nómos, m. \\\"law, custom\\\": Lat. cf. numerus, 1, m. \\\"number\\\" ... WP II, 330'.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 9, \"lang\": \"Italian\", \"words\": \"numero\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Italian numero is the regular Tuscan continuation of Latin numerus - a semi-learned form which kept the proparoxytone stress and the unsyncopated -e- (nùmero, not the popular *nombro that French shows), attested from the 13th century (Dante, Convivio). Ernout-Meillet note that numerus is 'panroman sauf esp. et port.', with numero the shape of the Italian reflex (REW/M.L. 5994). The box has no refs of its own, but the step Latin > Italian is uncontroversial; its function in the chart is to be the source of the Arabic and hence Persian نمره of nodes #10-#11, and it is Italian - not French or Latin - that Wiktionary names as the source of Arabic نمرة, so Nourai's choice of Italian here is deliberate and correct.\",\n \"derivation_fa\": \"numero ایتالیایی ادامهٔ قاعده‌مندِ توسکانیِ numerus لاتینی است — صورتی نیم‌کتابی که تکیهٔ سه‌هجایی و ‎-e-‎ نیفتاده را نگه داشته (nùmero، نه صورتِ مردمیِ *nombro که فرانسوی نشان می‌دهد) و از سدهٔ سیزدهم گواه دارد (دانته، Convivio). ارنو–مِیه یادآور می‌شوند که numerus «در همهٔ زبان‌های رمانس جز اسپانیایی و پرتغالی» بازمانده دارد و صورتِ ایتالیایی همان numero است (REW ۵۹۹۴). این جعبه ارجاعِ خود ندارد، اما گامِ لاتینی ← ایتالیایی بی‌گفت‌وگو است؛ کارکردش در نمودار آن است که سرچشمهٔ «نمرة» عربی و «نمره» فارسی (گره‌های ۱۰ و ۱۱) باشد، و ویکی‌واژه هم درست ایتالیایی — نه فرانسوی و نه لاتینی — را منبعِ «نمرة» عربی می‌داند؛ پس گزینشِ ایتالیایی در اینجا آگاهانه و درست است.\",\n \"sources\": [WIKT_NUMERUS, WIKT_NIMRA],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"No reference is given on this box; the parent's 'AHD' covers Latin numerus, and the Latin > Italian step is checked here against Ernout-Meillet and Wiktionary instead.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. numerus (LAT.txt line 42394)\", \"stance\": \"supports\",\n    \"note\": \"'Ancien (Liv., Andr.), usuel, class. Panroman sauf esp. et port. (de même numero). M.L.5994.' - the Romance survival, Italian included.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. numero (cross-referenced from 'number', KLN_1966.txt line 25752 ff.)\", \"stance\": \"supports\",\n    \"note\": \"Klein's 'number' entry ends 'See nimble and cp. numeral, numeric, numero, numerous', i.e. he treats It./Sp. numero as a member of the same Latin family.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 10, \"lang\": \"Arabic\", \"words\": \"nomreh\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Arabic نِمْرة / نُمْرة nimra/numra 'number' is a modern Mediterranean borrowing of Italian numero, taken over with the feminine ending -a (tāʾ marbūṭa) that Arabic regularly gives to Italian nouns in -o/-a and reshaped to the native fiʿla pattern, whence the sound plural نمرات. Wiktionary records it for Egyptian Arabic (nimra), Moroccan Arabic (namra) and South Levantine Arabic (numra) and derives the Levantine form explicitly 'borrowed from Italian numero'; the route is the 18th-19th c. Italian commercial and maritime lingua franca of Alexandria, Tunis and the Levant, the same channel that gave Arabic فاتورة fātūra 'invoice' and بوليصة būliṣa 'policy'. Nourai's Italian -> Arabic arrow is thus exactly the modern account. It is not Classical Arabic (Lane and the classical lexica have only نمرة 'a spot, a leopard-mark' from نمر), which is why no classical dictionary is cited here.\",\n \"derivation_fa\": \"«نِمْرة/نُمْرة» عربی به معنی «شماره» وام‌واژه‌ای نوی مدیترانه‌ای از numero ایتالیایی است که با پایانهٔ مؤنثِ ‎-a‎ (تاء مربوطه) — همان پایانه‌ای که عربی به‌قاعده به اسم‌های ایتالیاییِ مختوم به ‎-o/-a‎ می‌دهد — گرفته و بر وزنِ «فِعْلة» ریخته شده، و از همین‌جا جمعِ سالمِ «نمرات». ویکی‌واژه آن را در عربی مصری (nimra)، مغربی (namra) و شامی جنوبی (numra) ثبت کرده و صورتِ شامی را صریحاً «وام‌گرفته از ایتالیایی numero» می‌داند؛ راهِ ورود، زبانِ میانجیِ بازرگانی و دریانوردیِ ایتالیایی در اسکندریه و تونس و شام در سده‌های ۱۸–۱۹ است، همان مسیری که «فاتورة» و «بولیصة» را هم به عربی آورد. پس پیکانِ ایتالیایی ← عربی نورایی درست همان روایتِ امروزی است. این واژه عربیِ کلاسیک نیست (در لسان و لغت‌نامه‌های کهن «نُمْرة» تنها «خالِ پلنگ» از ریشهٔ نمر است) و از این‌رو هیچ فرهنگ کلاسیکی در اینجا ارجاع نشده.\",\n \"sources\": [WIKT_NIMRA, WIKT_NOMRE],\n \"ref_check\": [\n   {\"ref\": \"MON:4815\", \"status\": \"partial\",\n    \"note\": \"Moʿin's own page cannot be checked (the 6-vol edition is not online); his entry, in the Adena condensation (incoming/MON/MON_2vol_Adena_v2_djvu.txt line 79416), tags نمره '[معر.]' = muʿarrab, an Arabicised word, which is precisely the Arabic mediation this node asserts, but Moʿin names no European source.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Moʿin s.v. نمره (MON_2vol_Adena_v2_djvu.txt line 79416)\", \"stance\": \"supports\",\n    \"note\": \"'نمره: [معر. عدد، رقم] (ا.) شماره، عدد ... ج. نمرات. نمرة ترتیب: شماره مسلسل، شمارة ترتیب.' The muʿarrab tag and the Arabic-type plural نمرات are the evidence for an Arabic intermediary.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs\", \"stance\": \"silent\",\n    \"note\": \"grep for 'namus', 'nomos' and 'numero' in LKT.txt returns nothing - as expected, since Lokotsch collects oriental words in European languages, i.e. the opposite direction of this loan.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 11, \"lang\": \"Persian\", \"words\": \"nomreh «نمره» : number  [+ نمرات]\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Persian نمره nomre 'number; mark, school grade' is certainly the same Mediterranean word, and the Arabic-mediated route Nourai draws is the one Wiktionary gives - 'ultimately from Italian numero, possibly transmitted through Arabic نُمْرة (numra)' - the decisive evidence being the broken/sound plural نمرات nomarāt printed in Nourai's own box (and in Moʿin, 'ج. نمرات'): a plural in -āt is only formed on words felt to be Arabic feminines in -a, so the word must have reached Persian in its Arabic dress rather than straight from French. Moʿin accordingly tags it '[معر.]' (muʿarrab). The reason for a 'plausible' rather than 'confirmed' verdict is that Wiktionary's own wording is 'possibly', and a direct borrowing from French numéro (or Russian номер) in the Qajar period is the rival account often met with in Persian handbooks; the -e < -a of nomre and the plural nomarāt favour the Arabic route but do not exclude a French form re-shaped on the Arabic pattern. Semantically Persian added the schoolroom sense 'mark, grade' (Moʿin: 'عددی که معرف معلومات شاگرد و مدرسه است و آن را معلم پس از سوال و امتحان تعیین ... می‌کند'), unknown to Arabic and Italian.\",\n \"derivation_fa\": \"«نمره» فارسی به معنی «شماره» و «نمرهٔ درس» بی‌گمان همان واژهٔ مدیترانه‌ای است و مسیری که نورایی می‌کشد همان است که ویکی‌واژه می‌آورد: «سرانجام از numero ایتالیایی، احتمالاً از راه نمرةِ عربی». گواهِ کارساز، جمعِ «نمرات» است که در همان جعبهٔ نورایی و در معین («ج. نمرات») آمده: جمعِ ‎-ات‎ تنها بر واژه‌هایی بسته می‌شود که مؤنثِ عربیِ مختوم به ‎-ة‎ احساس شوند؛ پس واژه در جامهٔ عربی به فارسی رسیده، نه یک‌راست از فرانسوی. معین نیز آن را «[معر.]» (معرّب) برچسب زده است. دلیلِ «با احتیاط پذیرفتنی» بودن آن است که خودِ ویکی‌واژه «احتمالاً» می‌گوید و روایتِ رقیب — وام‌گیریِ مستقیم از numéro فرانسوی (یا номер روسی) در دورهٔ قاجار — در دستنامه‌های فارسی فراوان دیده می‌شود؛ ‎-ه‎ پایانی و جمعِ «نمرات» مسیرِ عربی را نیرو می‌دهد ولی صورتِ فرانسویِ بازریخته بر الگوی عربی را نفی نمی‌کند. از نظر معنایی، فارسی معنای آموزشگاهیِ «نمره» را افزوده که در عربی و ایتالیایی نیست.\",\n \"sources\": [WIKT_NOMRE, WIKT_NIMRA],\n \"ref_check\": [\n   {\"ref\": \"MON:4815\", \"status\": \"supports\",\n    \"note\": \"Content verified in the Adena condensation of Moʿin (incoming/MON/MON_2vol_Adena_v2_djvu.txt line 79416): 'نمره: [معر. ...] (ا.) شماره، عدد. مجموع شماره‌هایی که از یک نشر به (روزنامه، مجله) در هر دفعه چاپ و منتشر می‌شود ... عددی که معرف معلومات شاگرد و مدرسه است ... ج. نمرات.' Both the muʿarrab tag Nourai relies on for the Arabic step and the plural نمرات printed in his box come from this entry; only the page number of the 6-vol edition is unverifiable.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Moʿin s.v. نمره and نمره‌گیر (MON_2vol_Adena_v2_djvu.txt lines 79416, 79427)\", \"stance\": \"supports\",\n    \"note\": \"The neighbouring entry 'نمره گیر: [معر. ف. و ...] (ص‌فا. امر.) آلتی که در تلفون تعبیه شده، شامل نمره‌ها و با چرخاندن آن نمرة مطلوب را بدست آرند' shows Moʿin analysing the word as muʿarrab + Persian, i.e. a foreign word naturalised through Arabic.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-hā-ye Hend-o-Orupāyi (incoming/ARY)\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur's dictionary treats inherited Indo-European vocabulary of Persian; نمره, a modern European loan, is not among his headwords, so nothing can be taken from him here.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 12, \"lang\": \"French\", \"words\": \"nombre\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"French nombre continues Latin numerus by the popular route: syncope of the medial vowel (*nùm'rus), then the epenthetic -b- that regularly develops in Gallo-Romance between m and r (cf. camera > chambre, cumulare > combler), giving Old French nombre, first attested in the 11th-12th c. and passing into Anglo-Norman noumbre. Watkins' 'NUMBER' under nem- and Klein's 'number, n. — ME. nombre, noumbre, fr. OF. (= F.) nombre, fr. L. numerus (for *nomeros)' both describe exactly this step, and Skeat has 'Number. (F.—L.) F. nombre. — L. numerum, acc. of numerus'.\",\n \"derivation_fa\": \"nombre فرانسوی ادامهٔ مردمیِ numerus لاتینی است: نخست افتادنِ واکهٔ هجای میانی (*nùm'rus) و سپس رویشِ ‎-b-‎ میانجی که در گالو–رمانس به‌قاعده میان m و r پدید می‌آید (مانند camera ← chambre، cumulare ← combler)، و حاصل، nombre فرانسوی کهن است که از سدهٔ یازدهم–دوازدهم گواه دارد و به noumbre انگلو–نورمن رسیده. واتکینز که NUMBER را زیر nem- می‌آورد، کلاین («number — از انگلیسی میانهٔ nombre، از فرانسوی کهن nombre، از لاتینی numerus») و اسکیت («Number. فرانسوی nombre — لاتینی numerum») همه همین گام را وصف می‌کنند. ادعای نورایی درست است.\",\n \"sources\": [EO_NUMBER, WIKT_NUMERUS],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 780 gives 'Latin numerus, number, division: NUMBER; ENUMERATE, SUPERNUMERARY', the English word being by definition the Old French one; the index line 1945 confirms 'NUMBER nem-'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. number (KLN_1966.txt line 25752)\", \"stance\": \"supports\",\n    \"note\": \"'number, n. — ME. nombre, noumbre, fr. OF. (= F.) nombre, fr. L. numerus (for *nomeros) \\\"number\\\", fr. I.-E. base *nem-, \\\"to divide, distribute, allot\\\". See nimble and cp. numeral, numeric, numero, numerous.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Number (SKT.txt line 12505)\", \"stance\": \"supports\",\n    \"note\": \"'Number. (F.—L.) F. nombre. — L. numerum, acc. of numerus, a number. Allied to Nomad. (√NAM.) Der. out-number.'\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. numerus\", \"stance\": \"supports\",\n    \"note\": \"'Panroman sauf esp. et port. ... M.L.5994' - the French reflex among the Romance continuations.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 13, \"lang\": \"English\", \"words\": \"number, numerous\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Number is Middle English nombre/noumbre (c. 1300, 'sum, aggregate of a collection'), from Old French/Anglo-French nombre < Latin numerus; the verb followed from OF nombrer. Numerous, however, did not come through French: it is a 15th-16th c. learned borrowing straight from Latin numerōsus 'consisting of many; rhythmical' (Ernout-Meillet: 'numerosus: 1° conforme a la mesure; rythmique ... 2° abondant, nombreux'), so the box's two words reach English by two different routes - a small imprecision in an otherwise correct arrow, since both ultimately rest on numerus. Klein makes the split explicit: 'number, n. — ME. nombre ... fr. OF. nombre' but 'numerous, adj. — L. numerosus ... fr. numerus'. Verdict confirmed for the node, with that note.\",\n \"derivation_fa\": \"number از انگلیسی میانهٔ nombre/noumbre (حدود ۱۳۰۰ م. به معنی «جمع، مجموع») و آن از nombre فرانسوی کهن/انگلو–فرانسوی و از numerus لاتینی است؛ فعلِ آن نیز از nombrer فرانسوی کهن آمده. اما numerous از راه فرانسوی نیامده: وام‌واژه‌ای کتابی از سدهٔ ۱۵–۱۶ م. یک‌راست از numerōsus لاتینی «پرشمار؛ موزون» است (ارنو–مِیه: «numerosus: ۱- موافقِ وزن، موزون؛ ۲- فراوان، پرشمار»). پس دو واژهٔ این جعبه از دو راهِ جداگانه به انگلیسی رسیده‌اند — بی‌دقتیِ کوچکی در پیکانی که در کل درست است، چون هر دو سرانجام بر numerus استوارند. کلاین این جدایی را صریح می‌گوید. داوری: ادعای نورایی درست است، با همین یادآوری.\",\n \"sources\": [EO_NUMBER],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt index line 1945: 'NUMB nem- NUMBER nem- ... NUMISMATICS nem-'; the nem- article itself lists 'NUMBER; ENUMERATE, SUPERNUMERARY' under Latin numerus. NUMEROUS is not separately indexed but is a derivative of the same numerus.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. number and numerous (KLN_1966.txt lines 25752, 25765)\", \"stance\": \"supports\",\n    \"note\": \"'number, n. — ME. nombre, noumbre, fr. OF. (= F.) nombre, fr. L. numerus ...'; 'numerous, adj. — L. numerosus, \\\"numerous\\\", fr. numerus. See number, n., and -ous.' - the two routes.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Number (SKT.txt line 12505)\", \"stance\": \"supports\",\n    \"note\": \"'Number. (F.—L.) F. nombre. — L. numerum ... Allied to Nomad. (√NAM.)'\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 14, \"lang\": \"Different Languages\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"An empty collector box: Nourai uses 'Different Languages' whenever a set of English words descends from the root through branches he does not want to draw individually. Here it stands for the two remaining branches of Watkins' nem- article that feed node #15: Germanic (*nem- > Old English niman 'to take, seize' > ME nome/nomen > numb) and Greek (νομάς 'roaming in search of pasture' > Latin Nomas > French nomade > nomad). Both are listed in the same AHD paragraph Nourai cites, so the pass-through is accurate as far as it goes; it is a drafting device, not an etymological claim, and cannot be wrong except by omission.\",\n \"derivation_fa\": \"جعبه‌ای تهی و «گردآورنده»: نورایی هرگاه گروهی از واژه‌های انگلیسی از راهِ شاخه‌هایی به ریشه برسند که نمی‌خواهد یک‌یک بکشد، برچسبِ «زبان‌های مختلف» را می‌گذارد. در اینجا این جعبه نمایندهٔ دو شاخهٔ باقی‌ماندهٔ مقالهٔ nem- واتکینز است که به گرهٔ ۱۵ می‌رسند: ژرمنی (*nem- ← انگلیسی کهن niman «گرفتن» ← انگلیسی میانه nome/nomen ← numb) و یونانی (νομάς «چرنده، سرگردان در پیِ چراگاه» ← Nomas لاتینی ← nomade فرانسوی ← nomad). هر دو در همان بندِ AHD که نورایی ارجاع داده آمده‌اند، پس این گرهِ گذری تا همین اندازه درست است؛ شیوهٔ نمودارکشی است، نه ادعای ریشه‌شناختی، و جز به قصورِ حذف نمی‌تواند خطا باشد.\",\n \"sources\": [EO_NOMAD, EO_NUMB],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"The two branches the box stands for are both in AHD_watkins1985.txt line 780: '1. Germanic *nem- in: a. Old English niman, to take, seize: NIM, NUMB; (BENUMB)' and '3.c. Greek nomas, wandering in search of pasture: NOMAD'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 763 (POK_full.txt line 62549)\", \"stance\": \"supports\",\n    \"note\": \"'Gothic Old Saxon Old English niman, Old High German neman, Old Icelandic nema \\\"take\\\"' - the Germanic branch of the collector box.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. nimble (KLN_1966.txt line 25439)\", \"stance\": \"supports\",\n    \"note\": \"Klein's cross-references from *nem- include both 'nomad' and 'numb', the two words of node #15.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 15, \"lang\": \"English\", \"words\": \"numb, nomad\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Numb: Middle English nome, noumen (c. 1400) 'seized, taken, overpowered (with cold or palsy)', the past participle of nimen < Old English niman 'to take, seize' (Gothic niman, ON nema, OHG neman, G. nehmen) < Germanic *neman < PIE *nem- 'to take'; the sense is literally 'taken (with cold)', figurative from the 1560s, and the -b is unetymological, added in the 17th c. on the model of comb, limb (Klein: 'The b in numb is excrescent'). Nomad: 1550s, from French nomade < Latin Nomas, gen. Nomadis < Greek νομάς, gen. νομάδος 'roaming for pasture', a derivative of νομός 'allotted land, pasture' from νέμειν - so numb reaches the root through Germanic and nomad through Greek and Latin, which is exactly why the parent box is labelled 'Different Languages'. Both words are indexed under nem- by Watkins.\",\n \"derivation_fa\": \"numb: از انگلیسی میانهٔ nome/noumen (حدود ۱۴۰۰ م.) «گرفته‌شده، از کار افتاده (از سرما یا فلج)»، اسم مفعولِ nimen از انگلیسی کهن niman «گرفتن» (گوتیک niman، نورس کهن nema، آلمانی علیای کهن neman، آلمانی nehmen) از ژرمنیِ *neman و آن از *nem- هندواروپایی «گرفتن»؛ معنا تحت‌اللفظ «گرفته‌شدهٔ سرما» است و کاربردِ مجازی از دههٔ ۱۵۶۰ م.؛ حرف ‎-b‎ ریشه‌شناختی نیست و در سدهٔ هفدهم به قیاسِ comb و limb افزوده شده (کلاین: «b در numb زائد است»). nomad: از دههٔ ۱۵۵۰ م.، از nomade فرانسوی، از Nomas لاتینی (اضافیِ Nomadis) و آن از νομάς یونانی (اضافیِ νομάδος) «چرنده، در پیِ چراگاه رونده»، مشتقِ νομός «زمینِ واگذارشده، چراگاه» از νέμειν. پس numb از راه ژرمنی و nomad از راه یونانی و لاتینی به ریشه می‌رسند و همین است دلیلِ برچسبِ «زبان‌های مختلف» در جعبهٔ مادر. واتکینز هر دو را زیر nem- فهرست کرده. ادعای نورایی درست است.\",\n \"sources\": [EO_NUMB, EO_NOMAD],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 780: '1.a. Old English niman, to take, seize: NIM, NUMB; (BENUMB)' and '3.c. Greek nomas, wandering in search of pasture: NOMAD'; index lines 1930 and 1945: 'NOMAD nem-', 'NUMB nem-'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. numb and nomad (KLN_1966.txt lines 25752, 25541)\", \"stance\": \"supports\",\n    \"note\": \"'numb, adj. — ME. nome, lit. \\\"taken, seized\\\", pp. of nimen (fr. OE. niman), \\\"to take\\\". See nim and nimble. The b in numb is excrescent. Cp. benumb.'; 'nomad ... L. nomas, gen. -adis ... fr. Gk. νομάς ... fr. νομός ... rel. to νέμειν ... fr. I.-E. base *nem-, \\\"to divide, distribute, allot\\\".'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. numb / Numb (SKT.txt lines 12304, 12504)\", \"stance\": \"supports\",\n    \"note\": \"'numb. (E.) M. E. nome, nomen, pp. seized, taken, caught with, overpowered, deprived of sensation. Pp. of M. E. nimen (A. S. niman), to take; see Nimble. + Icel. numinn, bereft, pp. of nema, to take.'; 'Numb; see Nimble.'\"},\n   {\"src\": \"POK\", \"where\": \"IEW 763 (POK_full.txt line 62549 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'Gothic Old Saxon Old English niman ... \\\"take\\\"; lengthened grade Gothic anda-nem n. \\\"reception\\\", Old High German nama \\\"forcible receiving, robbery\\\" ...'\"}\n ]\n})\n\ndoc[\"entries\"].append(e0)\nprint(json.dumps(doc, ensure_ascii=False)[:200])\nwith open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/e0.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\nprint(\"ok\", len(e0[\"nodes\"]))\nPYEOF"
}
```


### [2026-09-07T19:48:18.608Z] TOOL RESULT

```
{"pdf_page": 359, "book_page": 329, "verified_by": "claude-opus-5", "verified_on": "2026-09-07", "entries": [{"entry": 0, "root": "Nem 1", "verdict": "confirmed", "modern_form": "PIE *nem- 'to assign,
ok 15
```


## [2026-09-07T19:48:25.779Z] TOOL CALL #71: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg359.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/359.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-07T19:48:25.855Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-07T19:53:24.013Z] TOOL CALL #72: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nSC='/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/e0.json'\ndoc=json.load(open(SC,encoding='utf-8'))\n\nW = \"https://en.wiktionary.org/wiki/\"\nWIKT_NEM = W + \"Reconstruction:Proto-Indo-European/nem-\"\nWIKT_NAMAZ = W + \"%D9%86%D9%85%D8%A7%D8%B2\"\nWIKT_NAMAD = W + \"%D9%86%D9%85%D8%AF\"\n\n# ---------------- ENTRY 1 : Nem 2 ----------------\ne1 = {\n \"entry\": 1,\n \"root\": \"Nem 2\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *nem- 'to bend, bow' (Pokorny 764 'nem-2 biegen'; Walde-Pokorny II 331-332; LIV 453 f.)\",\n \"note\": \"The root is genuine and Nourai's page is exact: Pokorny's second article, 'Root/lemma: nem-2, Meaning: to bend ... Page(s): 764', and Cheung (2007) 280 f. sets up Proto-Iranian *nam 'to bend, bow' with '«PIE *nem- \\\"to bend, bow\\\" = LIV: 453 f. | Pok.: 764'. The gloss is right in both halves: 'to bend, bow in respect' is the verb nam- and its abstract nəmah- 'homage', and 'also brush wood and twigs' is the derived noun Av. nəmata- 'Reisig' (Bartholomae AiW 1068, WP II 332 '*\\\"biegsam, sich herunterbeugend\\\"'), joined in Pokorny by Gk. νέμος / Lat. nemus 'grove, pasture' - the one item that is disputed, since Walde-Pokorny say of νέμος, nemus, Gaul. νεμητον and OIr. nemed that 'sie alle eher zu nem- \\\"zuteilen\\\"' belong, in spite of their formal comparability with Av. nəmata-. Two further points bear on the whole page: (a) the Pahlavi-Persian branch drawn here (#2-#3) is the one modern scholarship accepts, so entry 1 is right and entry 0's duplicate of it is wrong; (b) Wiktionary derives this 'bend' root from the 'assign' root of Nem 1 by the shift 'distribute' > 'worship, sacrifice' > 'bend', which would collapse Nourai's two roots into one - a live question, but Pokorny and Walde-Pokorny, whom he follows, keep them apart ('Ursprüngliche Gleichheit ... ist nicht wahrscheinlich zu machen', WP II 331).\",\n \"note_fa\": \"این ریشه راستین است و شمارهٔ صفحهٔ نورایی دقیق: مقالهٔ دومِ پوکورنی، «nem-2، معنی: خم شدن ... صفحهٔ ۷۶۴»، و چونگ (۲۰۰۷، ص ۲۸۰–۲۸۱) ریشهٔ ایرانی آغازینِ *nam «خم شدن، کرنش کردن» را با ارجاع «هندواروپایی آغازین *nem- = LIV: 453 f. | Pok.: 764» می‌آورد. هر دو نیمهٔ معنایی که نورایی داده درست است: «خم شدن، کرنش کردن» همان ستاک nam- و اسم‌مصدرِ nəmah- «ستایش» است، و «چوب‌خرده و شاخه‌های نازک» همان اسمِ مشتقِ اوستایی nəmata- «Reisig» است (بارتولمه، ستون ۱۰۶۸؛ والده–پوکورنی ج۲ ص۳۳۲: «*خم‌شو، فروخمنده»)، که پوکورنی νέμος یونانی و nemus لاتینی «بیشه، چراگاه» را نیز بدان می‌پیوندد — و همین یکی مورد اختلاف است، زیرا والده–پوکورنی می‌گویند که νέμος و nemus و νεμητον گالی و nemed ایرلندی کهن «همه بهتر است به nem- «بخش کردن» بازبسته شوند»، هرچند صورتاً با nəmata- اوستایی سنجیدنی‌اند. دو نکتهٔ دیگر بر کلِ این صفحه اثر دارد: نخست آنکه شاخهٔ پهلوی–فارسی که در اینجا کشیده شده همان است که پژوهش امروزی می‌پذیرد، پس این ورودی درست و تکرارِ آن در ورودیِ Nem 1 نادرست است؛ دوم آنکه ویکی‌واژه این ریشهٔ «خم شدن» را از ریشهٔ «واگذاردن» Nem 1 مشتق می‌داند و این دو را یکی می‌کند — پرسشی زنده، اما پوکورنی و والده–پوکورنی که نورایی از آنها پیروی کرده، آنها را جدا نگه می‌دارند.\",\n \"sources\": [WIKT_NEM, WIKT_NAMAZ],\n \"ref_check\": [\n   {\"ref\": \"POK:764\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt line 62575 ff.: 'Root / lemma: nem-2 ... Meaning: to bend ... Material: Old Indic namas- n. = Avestan nəmah- n. \\\"bowing, bending = worship, veneration, grace\\\". Old Indic namati \\\"bows, leans, bends\\\" (Kaus. namayati), Avestan namaiti \\\"bends\\\" ... with apa-, fra- \\\"escape, flee\\\" ... References: WP. II 331 f. ... Page(s): 764'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 331-332, '2. nem- „biegen''' (incoming/WLD/WLD_Bd2_pages.txt line 21935 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'2. nem- „biegen''. Ai. námas- n. = av. nəmah- n. „Verbeugung = Verehrung, Huldigung'', ai. namati „beugt sich, neigt sich, beugt, biegt'' (kaus. nāmayati), av. namaiti „beugt sich (weg)'' (nāmaiti, kaus. nāmayeiti), mit apa-, fra- „entfliehen''; Ptc. ai. natá- „gebogen''; av. nəmata- m. (auch nimata-) „Reisig'' (*„biegsam, sich herunterbeugend'', s. Bartholomae Airan. Wb. 1068).' Every single word of node #1 is here.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Etymological Dictionary of the Iranian Verb, pp. 280-281 s.v. *nam\", \"stance\": \"supports\",\n    \"note\": \"CHEUNG.txt line 18489 ff.: '*nam \\\"to bend, bow\\\" *AVESTAN: Y Av. nəm- (nam-) \\\"to bend\\\" || (+ *apa-) \\\"to yield, cede, depart, leave\\\" || (+ *fra-) \\\"to flee from\\\", caus. \\\"to bend down\\\" ... «PIE *nem- \\\"to bend, bow\\\" = LIV: 453 f. | Pok.: 764'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt)\", \"stance\": \"silent\",\n    \"note\": \"Watkins' appendix has only one nem- entry, the 'assign, allot' one; there is no root box for 'to bend', so the American Heritage list neither supports nor contradicts this root.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. 'nemo' and 'nomos, is (2)' (IEC.txt lines 11628, 11837)\", \"stance\": \"supports\",\n    \"note\": \"'nemo \\\"turn, bend, bow\\\"; nemos \\\"curve, arch, heaven\\\" Skt. námāmi, v. id.: Av. nam-, v. intr. id.; Tokh. AB nām-, B nem-, tr. id.; ... Skt. námas, n. \\\"bend, bow\\\"'; 'nomos, is (2) \\\"turn, bend\\\". Cf. nemo and nemos (1) Skt. cf. namráh \\\"crooked\\\"; Gk. nomeis, pl. \\\"ribs of ship\\\"'.\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan / Old Persian\",\n \"words\": \"nam : to bend, bow ; nemah 2 : bowing in respect ; namaiti : bends ; fra-namaiti, apa-namaiti ; nemata 1 : twigs\",\n \"verdict\": \"plausible\",\n \"derivation\": \"All five items are genuine and are drawn, in this order, from one paragraph of Walde-Pokorny II 331-332. (1) The verb: Younger Avestan nam-/nəm- 'to bend', middle only outside the causative (Cheung's Liste no. 40). (2) nəmah- n., the -as- stem abstract 'Verbeugung = Verehrung, Huldigung, Ehrfurchtsbezeigung' (Bartholomae cols. 1069-1070, with the specialised sense 'Gebet' in Y. 58.1 etc.), exactly matching Sanskrit námas-. (3) namaiti 'bends' (3sg. present; the long-vowel stem nāmaiti and the causative nāmayeiti beside it). (4) The prefixed forms are real attestations, not Nourai's inventions: Cheung cites INJ. 3sg. YAv. apanəmata (Yt 19.35 f.) '(+ *apa-) to yield, cede, depart' and 3pl. YAv. franəmante (Y 57.18), IMPV. fra(-ca) nəmaŋʷha (V 2.10, 2.18) '(+ *fra-) to flee from', and WP glosses 'mit apa-, fra- \\\"entfliehen\\\"'. (5) nəmata- m. 'Reisig, brushwood, dry twigs' (Bartholomae AiW 1068, V. 9.46, V. 5.35, V. 5.38), also 'Geflecht aus Reisig, Hürde', which Bartholomae derives 'Zum V. nam- \\\"(sich) herabbeugen\\\"' - so the twig sense sits under this root correctly. The verdict is only plausible because of the language label: none of the five is attested in Old Persian. Kent's Old Persian lexicon has no verb nam- and no nāma- of this shape, so 'Avestan / Old Persian' should read simply 'Avestan' (the same slip lies behind the chart's note in entry 0, which calls nam- 'Old Persian').\",\n \"derivation_fa\": \"هر پنج قلمِ این جعبه راستین است و به همین ترتیب از یک بندِ والده–پوکورنی (ج۲، ص۳۳۱–۳۳۲) برداشته شده است. ۱) ستاکِ فعلی: اوستایی نوِ nam-/nəm- «خم شدن»، که جز در صورتِ سببی همیشه در وجهِ میانه می‌آید (چونگ، شمارهٔ ۴۰). ۲) nəmah- خنثی، اسم‌مصدرِ ستاکِ ‎-as-‎ به معنی «کرنش = ستایش، نیایش، اظهارِ فروتنی» (بارتولمه، ستون‌های ۱۰۶۹–۱۰۷۰، با معنای تخصیصیِ «دعا» در یسنا ۵۸٫۱ و جاهای دیگر)، درست برابرِ námas- سنسکریت. ۳) namaiti «خم می‌شود» (سومِ شخصِ مفردِ حال؛ در کنار ستاکِ کشیدهٔ nāmaiti و سببیِ nāmayeiti). ۴) صورت‌های پیشوندی گواهِ متنی دارند و ساختهٔ نورایی نیستند: چونگ apanəmata (یشت ۱۹٫۳۵) را با معنی «واگذاشتن، رفتن» و franəmante (یسنا ۵۷٫۱۸) و fra(-ca) nəmaŋʷha (وندیداد ۲٫۱۰ و ۲٫۱۸) را با معنی «گریختن از» می‌آورد، و والده–پوکورنی نیز «با apa- و fra- «گریختن»» دارد. ۵) nəmata- مذکر «چوب‌خرده، شاخه‌های خشک» (بارتولمه ۱۰۶۸؛ وندیداد ۹٫۴۶، ۵٫۳۵، ۵٫۳۸) و نیز «بافتهٔ چوب‌خرده، پرچین»، که بارتولمه آن را «از ستاکِ nam- «فروخمیدن»» می‌داند — پس معنای «شاخه» به‌درستی زیر همین ریشه نشسته است. تنها دلیلِ «با احتیاط پذیرفتنی» بودن، برچسبِ زبانی است: هیچ‌یک از این پنج صورت در پارسی باستان گواه ندارد؛ در واژه‌نامهٔ کِنت نه ستاکِ nam- هست و نه چنین صورتی، پس «اوستایی / پارسی باستان» باید تنها «اوستایی» باشد — همین لغزش در یادداشتِ ورودیِ نخست هم هست که nam- را «پارسی باستان» می‌خواند.\",\n \"sources\": [WIKT_NEM, WIKT_NAMAZ],\n \"ref_check\": [\n   {\"ref\": \"POK:764\", \"status\": \"supports\",\n    \"note\": \"IEW 764 (POK_full.txt line 62577 ff.) has four of the five: 'Avestan nəmah- n. \\\"bowing, bending = worship, veneration, grace\\\" ... Avestan namaiti \\\"bends\\\" (nāmaiti, Kaus. nāmayeiti), with apa-, fra- \\\"escape, flee\\\"'. Only nəmata- is missing from Pokorny's abridged article (it is in his source, WP II 332).\"},\n   {\"ref\": \"WLD2:234\", \"status\": \"not_found\",\n    \"note\": \"Wrong page. Walde-Pokorny Bd. II p. 234 is the article range 'mand- — mari' (incoming/WLD/WLD_Bd2_pages.txt line 15282 '\\\\f234    mand- — mari'); the nem- 'biegen' article, which contains all five of Nourai's words verbatim, is on pp. 331-332 (line 21935 ff.). Nourai's number is almost certainly a slip for 334 or 331; the reference is right in substance, wrong in page.\"},\n   {\"ref\": \"SYN:544\", \"status\": \"supports\",\n    \"note\": \"Buck p. 544 (SYN.txt leaf 595, ch. 9.14 BEND): 'Skt. namati mostly intr., Av. namaiti intr., caus. Skt. nāmayati, Av. nāmayeiti trans., Skt. namas-, Av. nəmah- \\\"bending, homage\\\", Toch. nām- \\\"incline, bow\\\" (SSS 446), further connection, Walde-P. 2.331 f.' - namaiti and nəmah- 'bowing in respect' exactly as in the box, with WP II 331 f. as Buck's own reference (a further sign that Nourai's 'WLD2:234' should be 331/334).\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW cols. 1068-1071 (BRT.txt, leaf with cols. 1067-1072)\", \"stance\": \"supports\",\n    \"note\": \"col. 1068: 'j. nəmata- m. 1) \\\"Reisig\\\" ... 2) \\\"Geflecht aus Reisig, Hürde\\\" ... Zum V. nam- \\\"(sich) herabbeugen\\\", vgl. nhd. Reis und ags. hrissan \\\"zittern\\\" ... np. namad \\\"grober Teppich; Filz\\\"'; cols. 1069-1070: 'j., g. nəmah- n. \\\"Verehrung, Ehrerbietung, Huldigung, Ehrfurcht(sbezeigung)\\\" ... Zum V. nam-: — ai. námas- n. \\\"Huldigung\\\"; vgl. mp. namāt, np. namāz \\\"Gebet\\\"'; col. 1071: 'g. nəmōi Inf. \\\"um auszuweichen, zu entfliehen\\\"' and 'j. nəmasyā- den. Praes. \\\"(einer Gottheit) Ehrfurcht bezeugen, huldigen\\\"'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"pp. 280-281 s.v. *nam 'to bend, bow'\", \"stance\": \"supports\",\n    \"note\": \"'*AVESTAN: Y Av. nəm- (nam-) \\\"to bend\\\" || (+ *apa-) \\\"to yield, cede, depart, leave\\\" || (+ *fra-) \\\"to flee from\\\", caus. \\\"to bend down\\\" || (+ *ui-) \\\"to put, spread apart\\\" = Liste: 40 ... INJ. 3sg. YAv. apanəmata (Yt 19.35 f.), SUBJ. 1sg. YAv. fra.nmāne (Yt 9.4, Yt 17.25), IMPV. 2sg. YAv. fra(-ca) nəmaŋʷha (V 2.10, V 2.18)' - Nourai's fra-namaiti and apa-namaiti are real Avestan forms.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian: Grammar, Texts, Lexicon, lexicon\", \"stance\": \"contradicts\",\n    \"note\": \"grep of KNT.txt for a headword nam-/nāma- of this meaning finds nothing (only nāman- 'name' and unrelated hits); Old Persian has no attested verb nam- 'to bend', so the 'Old Persian' half of the box's language label is unsupported.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. 'nemo' (IEC.txt line 11628)\", \"stance\": \"supports\",\n    \"note\": \"'nemo \\\"turn, bend, bow\\\" ... Skt. námāmi, v. id.: Av. nam-, v. intr. id.; Tokh. AB nām-, B nem-, tr. id.; ... Skt. námas, n. \\\"bend, bow\\\"'.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"namâč : bowing, prayer\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"This is the correct home of the word. Middle Persian namāč / namāz, Book Pahlavi <nmʾc> written with the Aramaic ideogram <OSGDE> = sgdh 'prostration' (MacKenzie CPD p. 57), Manichaean MP and Parthian nmc, Pāzand namāž, is an Old Iranian abstract on the stem nam- 'to bend, bow' - Nyberg indexes it under 'nəmata-/nəmah-' and writes 'namāč ... - Av. (1069) nəmah-', i.e. the 'Verehrung' word of Bartholomae's column 1069, and Moʿin's footnote in Borhān-e Qāteʿ p. 2167 says 'پهلوی namāč، از ایرانی باستان nam- (خم شدن، تعظیم کردن)'. The semantic sequence is 'a bending' > 'obeisance, homage (to a god)' > 'act of worship' > 'the prescribed prayer', which is why MacKenzie glosses it 'reverence, prostration, prayer' and the idiom namāz burdan means 'to pay homage'. The chart's NOTE, that 'BRT:1070 derives it from Avestan nemah: what one owes', misreports Bartholomae: column 1070 carries both homonyms, and it is under the 'Verehrung' lemma - not the 'Darlehen' one - that Bartholomae himself writes 'vgl. mp. namāt, np. namāz \\\"Gebet\\\"'. Modern scholarship therefore stands wholly on this side of the dispute the chart records.\",\n \"derivation_fa\": \"جای درستِ این واژه همین‌جاست. فارسی میانهٔ namāč/namāz، در پهلوی کتابی ⟨nmʾc⟩ با هزوارشِ آرامیِ ⟨sgdh⟩ «سجده» (مکنزی، ص ۵۷)، در فارسی میانهٔ مانوی و پارتی nmc، در پازند namāž، اسم‌مصدری ایرانی باستان بر ستاکِ nam- «خم شدن، کرنش کردن» است — نیبرگ آن را ذیل «اوستایی (۱۰۶۹) nəmah-» می‌آورد، یعنی همان مادهٔ «ستایش» ستون ۱۰۶۹ بارتولمه، و حاشیهٔ معین در برهان قاطع ص ۲۱۶۷ می‌نویسد: «پهلوی namāč، از ایرانی باستان nam- (خم شدن، تعظیم کردن)». زنجیرهٔ معنایی چنین است: «خمیدن» ← «کرنش و نیایش (در برابر خدا)» ← «پرستش» ← «نمازِ واجب»؛ از این‌رو مکنزی آن را «کرنش، سجده، نماز» معنی می‌کند و ترکیبِ namāz burdan «تعظیم کردن» است. یادداشتِ نمودار که می‌گوید «بارتولمه ۱۰۷۰ آن را از nəmah- اوستایی «آنچه وام است» می‌گیرد»، بارتولمه را نادرست گزارش کرده: ستون ۱۰۷۰ هر دو هم‌آوا را دارد و آن جمله («قی: فارسی میانه namāt، فارسی نو namāz «نماز»») ذیل مادهٔ «ستایش» است، نه مادهٔ «وام». پس پژوهش امروزی تماماً در همین سوی اختلافی است که نمودار ثبت کرده. ادعای نورایی در این ورودی درست است.\",\n \"sources\": [WIKT_NAMAZ],\n \"ref_check\": [\n   {\"ref\": \"BQT:2167\", \"status\": \"supports\",\n    \"note\": \"Borhān-e Qāteʿ p. 2167 = pdf page 250 of vol. 4 (incoming/BQT/BQT_v4_pages.txt line 9987 ff.), Moʿin's footnote 4 on نماز: 'پهلوی namāč، از ایرانی باستان nam- (خم شدن، تعظیم کردن) «بارتولمه ...، نیبرگ ص ۱۳۵»؛ ورک: هوبشمان ۱۰۴۰؛ قی: اوستایی nəmah- (دعا)، هندی باستان namas-، پازند namāž، افغانی nmanž، بلوچی namāz ... کردی nimēž، زازا nemaž، اورامانی nmāž، گیلکی namāz - مجازاً عبادت مخصوص مسلمانان.' The page number is exact and the content is precisely the arrow drawn.\"}\n ],\n \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p. 135 s.v. namāč (NYB_vol2_glossary.txt leaf 150)\", \"stance\": \"supports\",\n    \"note\": \"'... — Av. (1069) namah-; MPrthPrs nmc; FrP 19 *SGDH = nm'c, but Cod. 8, XVII, 7 nm'š with NP gl. namāj; Paz. namāž; NP namaz.'\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 57 (PHD.txt line 494)\", \"stance\": \"supports\",\n    \"note\": \"'namāz [OSGDE < A sgdh; nm'c | = M, N ~] reverence, prostration, prayer. ~ burdan: pay homage.' - the ideogram sgdh 'prostration' is itself evidence for the 'bowing' etymology.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss p. 233 no. 1040\", \"stance\": \"supports\",\n    \"note\": \"'aw. vergl. nemah- \\\"Gebet\\\"; ai. namas-; phl. v. namāč (pāz. namāš)' - Horn puts the Pahlavi word under Av. nəmah- 'prayer/homage', not under 'loan'.\"},\n   {\"src\": \"BRT\", \"where\": \"AiW cols. 1069-1070 s.v. nəmah- 'Verehrung'\", \"stance\": \"supports\",\n    \"note\": \"'Zum V. nam-: — ai. námas- n. \\\"Huldigung\\\"; vgl. mp. namāt, np. namāz \\\"Gebet\\\"' - Bartholomae, the very reference the chart's note invokes against this arrow, in fact supports it.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"namâz «نماز» : prayer\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian نماز namāz is the direct continuation of MP namāz (Book Pahlavi <nmʾc>, whose <c> writes /z/ exactly as in <rwc> = rōz 'day'; Pāzand namāž), so the change is one of spelling rather than of sound. Semantically Persian kept both layers: the pre-Islamic 'obeisance, homage', alive in the Shāhnāme formula namāz burdan - the couplet in the box, 'چو نزدیک رستم فراز آمدند / پیاده به رسم نماز آمدند', is one of Nūshīn's examples of exactly that idiom - and the Islamic 'the five prescribed ṣalāt', which Moʿin's Borhān footnote marks as the figurative extension ('مجازاً عبادت مخصوص مسلمانان'). Horn (no. 1040) observed that every New Iranian form - Kurdish nimēž, Zaza nemaž, Hawrami nmāž, Gilaki namāz, Balochi namāz/nawāz, Pashto nmūnj - presupposes the specifically Middle Persian formation namāč and concluded that they are all loans from Persian; Hübschmann (PSt no. 1040) objected that the dialect forms are hardly borrowed and posited an inherited Old Iranian stem instead. From Persian the word travelled with Islam into Turkic, Indo-Aryan, Georgian, Armenian, Russian and Thai. The arrow, the script and the gloss are all correct.\",\n \"derivation_fa\": \"«نماز» فارسی نو ادامهٔ بی‌واسطهٔ namāz فارسی میانه است (پهلوی کتابی ⟨nmʾc⟩ که ⟨c⟩ آن درست مانند ⟨rwc⟩ = rōz «روز» صدای /z/ را می‌نویسد؛ پازند namāž)، پس دگرگونی در اینجا املایی است نه آوایی. از نظر معنایی فارسی هر دو لایه را نگه داشته: معنای پیش از اسلامِ «کرنش، تعظیم» که در ترکیبِ «نماز بردن» شاهنامه زنده است — و بیتِ درون جعبه، «چو نزدیک رستم فراز آمدند / پیاده به رسم نماز آمدند»، یکی از شواهدِ نوشین برای همین ترکیب است — و معنای اسلامیِ «صلاتِ پنج‌گانه» که معین در حاشیهٔ برهان آن را گسترشِ مجازی می‌داند («مجازاً عبادت مخصوص مسلمانان»). هرن (شمارهٔ ۱۰۴۰) دیده بود که همهٔ صورت‌های ایرانیِ نو — کردی nimēž، زازا nemaž، اورامی nmāž، گیلکی namāz، بلوچی namāz/nawāz، پشتو nmūnj — بر ساختِ ویژهٔ فارسی میانهٔ namāč استوارند و از این‌رو همه را وام‌واژه از فارسی شمرد؛ هوبشمان (مطالعات فارسی، شمارهٔ ۱۰۴۰) خرده گرفت که «صورت‌های گویشی ایرانی به‌دشواری وام‌گرفته‌اند» و ستاکی موروثی از ایرانی باستان فرض کرد. از فارسی همراهِ اسلام به زبان‌های ترکی، هندوآریایی، گرجی، ارمنی، روسی و تایلندی رفته است. پیکان و املا و معنا هر سه درست است.\",\n \"sources\": [WIKT_NAMAZ],\n \"ref_check\": [\n   {\"ref\": \"BQT:2167\", \"status\": \"supports\",\n    \"note\": \"The same Borhān page (pdf 250 of vol. 4) is the article on نماز itself: 'نماز - بفتح اول و ثانی بالف کشیده و بزای نقطه‌دار، بمعنی بندگی و اطاعت و ادای طاعت و سجود و پرستش و خدمتگاری و فرمان‌برداری باشد', footnote 1: 'در اصطلاح، عبادت مخصوص و واجب مسلمانان که پنج بار در شبانه‌روز ادا کنند و آن را بعربی صلاة گویند'.\"},\n   {\"ref\": \"FSF:328\", \"status\": \"partial\",\n    \"note\": \"Right book and right entry, page slightly off in the copy on disk: Nūshīn's Vāzhe-nāmak has the headword 'نماز (بردن)' with the chart's Ferdowsī couplet on printed p. 330-331 (FSF_pages.txt leaf 444, whose running head reads 'نمایش  ۳۳۱'); Nourai cites 328. Since this scan's printing runs printed = leaf - 113 and its edition was not identified, the 2-3 page discrepancy is most likely a different printing rather than a wrong citation.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no. 1040 (HUB.txt line 3599)\", \"stance\": \"partial\",\n    \"note\": \"'1040. Die iranischen Dialektformen sind schwerlich entlehnt, also iran. *namad- [OCR; read *namāz-/*namāč-] anzusetzen.' - Hübschmann accepts the etymology but contradicts Horn on whether the New Iranian forms are loans from Persian.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss p. 233 no. 1040\", \"stance\": \"supports\",\n    \"note\": \"'1040. nemāz \\\"Gebet\\\" ... LW. kurd. nimēž, nimz \\\"Gebet\\\"; afgh. nmūnj; bel. namāz, nawāz. Da alle neuiranischen Formen auf die mittelpersische charakteristische Neubildung namāč zurückgehen, so halte ich dieselben sämmtlich für Lehnwörter. Fr. Müller (WZKM. 5, 67) nimmt als Grundform ap. *namasčiy an; aber ap. sč konnte im Neupersischen doch nicht zu ž werden.'\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 57\", \"stance\": \"supports\",\n    \"note\": \"'namāz ... | = M, N ~]' - MacKenzie's '= N ~' notation states that the New Persian form is identical with the Middle Persian one, i.e. the arrow as drawn.\"}\n ]\n})\n\ndoc[\"entries\"].append(e1)\n\n# ---------------- ENTRY 2 : Nemata 2 ----------------\ne2 = {\n \"entry\": 2,\n \"root\": \"Nemata 2, Nimatâ\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Avestan nəmata- (variant nimata-) m. 'brushwood, dry twigs; wickerwork of twigs' - Bartholomae, AiW col. 1068; Walde-Pokorny II 332\",\n \"note\": \"The Avestan word and its two shapes are real: Walde-Pokorny II 332 has 'av. nəmata- m. (auch nimata-) \\\"Reisig\\\"' and Bartholomae AiW 1068 documents it from V. 9.46 ('the corpse-demon vanishes ... like dry brushwood after a year'), V. 5.35 and V. 5.38 ('the enjoyment of wood, brushwood and iron implements'), with the second sense 'Geflecht aus Reisig, Hürde' in compounds (*nəmatō.aiwi.varana- 'shelter of wattle', *nəmaθkā- 'brushwood as fuel'). Two reservations make this only plausible. (a) The gloss: 'straw, grass' is not Bartholomae's ('Reisig' = brushwood/dry twigs) but comes verbatim from Horn's Grundriss p. 233 no. 1041, 'aw. nemata-, nimata- \\\"Stroh, Gras\\\"; phlv. namat \\\"Stroh, Gras\\\"; grober Teppich\\\"' - which is also where the doublet 'Nemata 2, Nimatâ' in the root box comes from, not from Nyberg. (b) The status: this is not an independent root but the same word Nourai has already listed as 'nemata 1: twigs' inside entry 1, since Bartholomae derives it explicitly 'Zum V. nam- \\\"(sich) herabbeugen\\\"' and WP explain it as '*\\\"biegsam, sich herunterbeugend\\\"' - i.e. 'the bendable stuff'. Nourai has therefore split one Avestan word into a member of Nem 2 and a root of its own, and put a Persian etymology in the wrong place: نمد belongs under Nem 2 too. Hübschmann (PSt no. 1041) adds a real caution - 'Zd. nimata- ist dunkel' - while accepting Ossetic nimät 'felt, felt coat' as a cognate and Sanskrit namata- 'felt' as a loan from Iranian.\",\n \"note_fa\": \"واژهٔ اوستایی و دو صورتِ آن راستین است: والده–پوکورنی (ج۲، ص۳۳۲) «اوستایی nəmata- مذکر (و نیز nimata-) «چوب‌خرده»» دارد و بارتولمه (ستون ۱۰۶۸) آن را از وندیداد ۹٫۴۶ («نسو ناپدید می‌شود ... چون چوب‌خردهٔ خشکِ سالِ گذشته»)، ۵٫۳۵ و ۵٫۳۸ («بهره‌مندی از چوب و چوب‌خرده و ابزارِ آهنی») گواه می‌آورد و معنای دومِ «بافتهٔ چوب‌خرده، پرچین» را در ترکیب‌ها. دو نکته این ریشه را تنها «با احتیاط پذیرفتنی» می‌کند. الف) معنا: «کاه و گیاه» از بارتولمه نیست (او «Reisig» یعنی چوب‌خردهٔ خشک دارد) بلکه واژه‌به‌واژه از هرن، ص ۲۳۳، شمارهٔ ۱۰۴۱ آمده: «اوستایی nemata-، nimata- «کاه، گیاه»؛ پهلوی namat «کاه، گیاه»؛ فرشِ درشت» — و دوگانهٔ «Nemata 2, Nimatâ» هم از همان‌جاست، نه از نیبرگ. ب) جایگاه: این ریشهٔ مستقلی نیست، بلکه همان واژه‌ای است که نورایی پیش‌تر با عنوان «nemata 1: شاخه» در ورودیِ Nem 2 آورده است، زیرا بارتولمه صریحاً آن را «از ستاکِ nam- «فروخمیدن»» می‌داند و والده–پوکورنی معنای اصلی‌اش را «*خم‌شو، فروخمنده» می‌گیرند، یعنی «چیزِ خم‌شدنی». پس نورایی یک واژهٔ اوستایی را دو نیم کرده و ریشه‌شناسیِ «نمد» را در جای نادرست نشانده؛ «نمد» نیز به Nem 2 تعلق دارد. هوبشمان (شمارهٔ ۱۰۴۱) احتیاطِ درستی می‌افزاید: «صورتِ اوستاییِ nimata- تاریک است»، هرچند nimät آسی «نمد، بالاپوشِ نمدی» را هم‌ریشه و namata- سنسکریت را وام‌واژه از ایرانی می‌داند.\",\n \"sources\": [WIKT_NAMAD],\n \"ref_check\": [\n   {\"ref\": \"NYB:135\", \"status\": \"partial\",\n    \"note\": \"Nyberg, Manual of Pahlavi II p. 135 (NYB_vol2_glossary.txt leaf 150) reads 'namat [nmt'] felt 3117. — Av. (1068) nəmata-, regarding which v. Benveniste, BSL 32, 1931, 82sq.; NP namad; borrowed in Aram and Arab (namaṭ-)', and his index has 'nəmata-: namat'. So Nyberg does give the Avestan form and Bartholomae's column, which is what the root box needs - but he glosses the Pahlavi as 'felt', gives no 'straw, grass' anywhere, and treats nəmata- as an Avestan lexeme (under the verb nam-), not as a root in its own right. The gloss printed in the root box is Horn's, not Nyberg's.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW col. 1068 s.v. 'j. nəmata- m.' (BRT.txt, leaf with cols. 1067-1070)\", \"stance\": \"partial\",\n    \"note\": \"'j. nəmata- m. 1) \\\"Reisig\\\": nasuš ... nāit ... nəmatə tarō yāre \\\"die Nasu verschwindet .. wie übers Jahr das (dürre) Reisig\\\" V.9.46; ... vīspaca avi tiγra nəmata \\\".. und auf lauter spitzes (dorniges) Reisig\\\" V.5.35; ... āsnasca nəmatahecā ayaŋhecā \\\"die Nutzniessung von Holz und Reisig und Eisengerät\\\" V.5.38. 2) \\\"Geflecht aus Reisig, Hürde\\\" (nur Komp.) ... Zum V. nam- \\\"(sich) herabbeugen\\\" ... np. namad \\\"grober Teppich; Filz\\\". — Pü.: namat ... NA. schwankt zwischen nəmat- und nim-. Vgl. auch das ai. LW. namata-, das ein mp. nam- voraussetzt.' Supports the form, the Pahlavi and the Persian, but glosses 'brushwood', not 'straw, grass', and files it under the verb nam-.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss p. 233 no. 1041 (HRN.txt leaf 254)\", \"stance\": \"supports\",\n    \"note\": \"'1041. nemed \\\"grober Teppich, Filz\\\", ar. LW. namat. aw. nemata-, nimata- \\\"Stroh, Gras\\\"; phlv. namat \\\"Stroh, Gras\\\"; grober Teppich\\\" (Šāy. nāšāy. II, 101).' This is the source of Nourai's root name, its double form and its gloss.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 332 (incoming/WLD/WLD_Bd2_pages.txt line 21960 f.)\", \"stance\": \"supports\",\n    \"note\": \"'av. nəmata- m. (auch nimata-) „Reisig'' (*„biegsam, sich herunterbeugend'', s. Bartholomae Airan. Wb. 1068)'; and the following lines refuse to attach Gk. νέμος / Lat. nemus to it ('sie alle eher zu nem- „zuteilen''').\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no. 1041 (HUB.txt line 3601)\", \"stance\": \"partial\",\n    \"note\": \"'1041. Zd. nimata- ist dunkel, vgl. Darmesteter, Zend-Avesta II, p. 45, Anm. — Dazu osset. nimät, nmät \\\"Filz, Filzmantel\\\" ... Skr. namata- \\\"Filz\\\" ist LW.' - Hübschmann calls the Avestan form obscure while accepting the Ossetic cognate and the Sanskrit loan.\"}\n ],\n \"nodes\": []\n}\n\ne2[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"namat : felt rug or cloth\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian namat, Book Pahlavi <nmt'>, is well attested (Nyberg's reference '3117' is to the Pahlavi text he glosses; MacKenzie CPD p. 57 'namad [nmt' | N ~] felt') and is the regular continuation of Av. nəmata-: an Old Iranian *namata- with no change but the loss of the final vowel, the intervocalic -t- still written and pronounced -t in Middle Persian and voiced to -d only in New Persian. The semantic step is the interesting one and it is exactly the step Bartholomae's second Avestan sense predicts: 'brushwood' > 'wattle, matted stuff' > 'matted wool, felt' (Bartholomae's own note explains 'die dünn gewordenen Reiser der Bäume werden von den Frühjahrsstürmen abgerissen und verwebt', i.e. naturally matted twigs), and Horn p. 233 records the Pahlavi word still with both senses, '\\\"Stroh, Gras\\\"; grober Teppich', citing the Šāyast nē šāyast glossary II 101. From Middle Persian it was borrowed into Aramaic and Arabic (namaṭ) and into Sanskrit (namata-, a loan per Hübschmann and Bartholomae). Both of Nourai's references are exact.\",\n \"derivation_fa\": \"namat فارسی میانه، در پهلوی کتابی ⟨nmt'⟩، گواهِ استوار دارد (نیبرگ با ارجاع «۳۱۱۷» به متنِ پهلوی؛ مکنزی، ص ۵۷: «namad [nmt'] نمد») و ادامهٔ قاعده‌مندِ nəmata- اوستایی است: از ایرانی باستانِ *namata- بی هیچ دگرگونی جز افتادنِ واکهٔ پایانی، و ‎-t-‎ میان‌واکه‌ای در فارسی میانه هنوز ‎-t‎ نوشته و تلفظ می‌شد و تنها در فارسی نو به ‎-d‎ نرم شده است. گامِ معنایی نکتهٔ دلکشِ آن است و درست همان گامی است که معنای دومِ اوستاییِ بارتولمه پیش‌بینی می‌کند: «چوب‌خرده» ← «بافته، به‌هم‌مالیده» ← «پشمِ به‌هم‌مالیده، نمد»؛ خودِ بارتولمه در پانویس توضیح می‌دهد که «شاخه‌های نازک‌شدهٔ درختان را توفان‌های بهاری می‌کَنند و به هم می‌بافند». هرن نیز در ص ۲۳۳ واژهٔ پهلوی را همچنان با هر دو معنا ثبت کرده: «کاه، گیاه؛ فرشِ درشت»، به گواهِ واژه‌نامهٔ شایست نه‌شایست ج۲ ص۱۰۱. از فارسی میانه به آرامی و عربی (نمط) و به سنسکریت (namata-) وام رفته است. هر دو ارجاعِ نورایی دقیق است.\",\n \"sources\": [WIKT_NAMAD],\n \"ref_check\": [\n   {\"ref\": \"NYB:135\", \"status\": \"supports\",\n    \"note\": \"Nyberg II p. 135 (leaf 150): 'namat [nmt'] felt 3117. — Av. (1068) nəmata-, regarding which v. Benveniste, BSL 32, 1931, 82sq.; NP namad; borrowed in Aram and Arab (namaṭ-).' Page, form, gloss and the Avestan source all exactly as the node draws them.\"},\n   {\"ref\": \"HRN:233\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss p. 233 no. 1041 (HRN.txt leaf 254 = printed 233, offset leaf = printed + 21): '... aw. nemata-, nimata- \\\"Stroh, Gras\\\"; phlv. namat \\\"Stroh, Gras\\\"; grober Teppich\\\" (Šāy. nāšāy. II, 101).' The page is exact, and it is Horn's Pahlavi gloss that Nourai renders 'felt rug or cloth'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 57 (PHD.txt line 494)\", \"stance\": \"supports\",\n    \"note\": \"'namad [nmt' | N <)] felt.' MacKenzie normalises the Book Pahlavi <nmt'> as namad and glosses it 'felt', identical with the New Persian word.\"},\n   {\"src\": \"BRT\", \"where\": \"AiW col. 1068 s.v. nəmata-\", \"stance\": \"supports\",\n    \"note\": \"'— Pü.: namat; (zu V.3): apar-namat, unklar' - Bartholomae's own Pahlavi equivalent of Av. nəmata- is namat, exactly this node.\"},\n   {\"src\": \"SNS\", \"where\": \"Tavoosi, glossary of Šāyast nē šāyast (SNS.txt) - the text Horn cites (Šāy. nāšāy. II 101) for Pahlavi namat\", \"stance\": \"silent\",\n    \"note\": \"The word could not be located in the OCR of this glossary; Horn's citation stands unconfirmed from the local copy, though Nyberg's independent attestation ('felt 3117') covers the Pahlavi word.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"namad «نمد» : a thick felt cloth\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian نمد namad 'felt, thick felt cloth' is the direct continuation of MP namat, with the regular New Persian voicing of intervocalic/final -t to -d after a vowel (cf. MP wāt > NP bād, MP zamīnīt-type finals), so *namata- > namat > namad. Moʿin's footnote in Borhān-e Qāteʿ p. 2169 gives the chain and the cognates: 'نمد ... پهلوی namat «تاوادیا ص ۱۹۳» ... در سانسکریت namata- (نمد) مستعار است «هوبشمان ۱۰۴۱» ... کردی nemed (فرش نمد)؛ لری nmd', with the definition 'پشم‌های روی هم گذاشته و مالیده که از آن فرش و کلاه و چاقه کنند' - wool laid one layer on another and pressed, from which rugs, caps and coats are made - i.e. Nourai's 'a thick felt cloth' precisely. The word travelled far: Arabic/Aramaic namaṭ, Sanskrit namata-, Ossetic nimät, Hungarian nemez, Uyghur nemet, Uzbek namat, and through Hindi namda into Anglo-Indian numdah/numnah 'a felt rug, a saddlecloth' - which is why Klein has an entry for it at all.\",\n \"derivation_fa\": \"«نمد» فارسی ادامهٔ بی‌واسطهٔ namat فارسی میانه است، با نرم‌شدنِ قاعده‌مندِ ‎-t‎ پایانی/میان‌واکه‌ای به ‎-d‎ در فارسی نو (مانند wāt فارسی میانه ← «باد»)، یعنی *namata- ← namat ← namad. حاشیهٔ معین در برهان قاطع ص ۲۱۶۹ همین زنجیره و هم‌ریشه‌ها را می‌آورد: «نمد ... پهلوی namat «تاوادیا ص ۱۹۳» ... در سانسکریت namata- (نمد) مستعار است «هوبشمان ۱۰۴۱» ... کردی nemed (فرش نمد)، لری nmd»، و تعریفِ متن: «پشم‌های روی هم گذاشته و مالیده که از آن فرش و کلاه و چاقه کنند» — درست همان «پارچهٔ ضخیمِ نمدی» نورایی. این واژه راهِ درازی رفته: عربی و آرامی نمط، سنسکریت namata-، آسی nimät، مجاری nemez، اویغوری nemet، ازبکی namat، و از راهِ هندی namda به انگلیسیِ هند numdah/numnah «فرشِ نمدی، زیرزینی» — و همین است دلیلِ آنکه کلاین برای آن مادّه‌ای دارد. ادعای نورایی درست است.\",\n \"sources\": [WIKT_NAMAD],\n \"ref_check\": [\n   {\"ref\": \"BQT:2169\", \"status\": \"supports\",\n    \"note\": \"Borhān-e Qāteʿ p. 2169 = pdf page 252 of vol. 4 (incoming/BQT/BQT_v4_pages.txt line 10075): 'نمد - بفتح اول و دوم، پهلوی namat «تاوادیا ص ۱۹۳» ... در سانسکریت namata- (نمد) مستعار است «هوبشمان ۱۰۴۱» و رک: ...؛ کردی nemed (فرش نمد)؛ قی: لری nmd (نمد) «ژابا ص ۴۲۳»؛ پشم‌های روی هم گذاشته و مالیده که از آن فرش و کلاه و چاقه کنند. مارا هم ازین نمد کلاهی است (مثل).' The page is exact (offset verified against ناموس 2106 and نماز 2167 on the same volume).\"},\n   {\"ref\": \"KLN:1026\", \"status\": \"supports\",\n    \"note\": \"Klein s.v. 'namda' (KLN_1966.txt line 24924, leaf 549 = printed p. ~1071 in the 1966 two-volume set): 'namda, numda, n., a felt rug, a saddlecloth (India) — Hind. namda, fr. Pers. namad, \\\"felt\\\"'; the cross-reference 'numda, numdah, n. — See namda' is at line 25756. Content exactly supports the node; as with KLN:1048 on entry 0, Nourai's page number runs about 45 pages below the 1966 pagination (the gap of 22 pages between his 1026 and 1048 does match the 24 leaves between the two entries), so he is presumably citing the 1971 one-volume printing.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss p. 233 no. 1041\", \"stance\": \"supports\",\n    \"note\": \"'1041. nemed \\\"grober Teppich, Filz\\\", ar. LW. namat.' - the New Persian headword itself, with the Arabic loan noted.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien nos. 1040-1041 (HUB.txt lines 3599-3606)\", \"stance\": \"supports\",\n    \"note\": \"'1040. Die iranischen Dialektformen sind schwerlich entlehnt, also iran. *namad- anzusetzen.' (his numbering here concerns the felt word) and '1041 ... Dazu osset. nimät, nmät \\\"Filz, Filzmantel\\\" ... Skr. namata- \\\"Filz\\\" ist LW.' - an inherited Old Iranian *namad-/namata- with Ossetic cognate and Sanskrit loan.\"},\n   {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Fārsi s.v. نمد (2-vol Adena condensation)\", \"stance\": \"supports\",\n    \"note\": \"The lexicon entry gives نمد as an inherited Persian word for felt with the compounds نمدمال, نمدزین etc.; no foreign tag ([ع.], [فر.]) is attached, i.e. Moʿin treats it as native Iranian, consistent with this node.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāteʿ p. 2169, main text s.v. نمد and نمد در آب داشتن\", \"stance\": \"supports\",\n    \"note\": \"'نمد در آب داشتن - کنایه از مکر کردن و در فکر حیله و دغا بودن باشد'; 'نمدزین - دی باشد که بر پشت اسب نهند و زین را بر بالای آن گذارند' - the word's Persian idioms, confirming it as a fully naturalised Persian noun.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Sogdian\", \"words\": \"nmt : felt\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sogdian nmt (Buddhist Sogdian) /namat/ 'felt' is the Sogdian cognate - not descendant - of the Pahlavi word, both continuing Old Iranian *namata-; Gharib's dictionary gives it as entry 6002, 'nmt B, namat, < Av. nəmata-, Khot. namata, felt', citing the Buddhist text TSP 3.229 and the discussions of Benveniste (BSL 32 p. 71) and Bailey (BSOAS 19.53 f.), with the Manichaean form nmθk and the derivative nmt'kr'k (entry 6003, 'felt-maker'). The word is thus attested in three Middle Iranian languages (Sogdian, Khotanese, Middle Persian), which is what makes the Old Iranian reconstruction secure and confirms Nourai's arrow root -> Sogdian. Note that the Sogdian form belongs, like the Pahlavi one, under root Nem 2 rather than under a separate 'Nemata' root.\",\n \"derivation_fa\": \"nmt سغدی (سغدیِ بودایی) /namat/ «نمد» هم‌ریشهٔ واژهٔ پهلوی است، نه بازماندهٔ آن؛ هر دو ادامهٔ ایرانی باستانِ *namata- اند. فرهنگ قریب آن را با شمارهٔ ۶۰۰۲ می‌آورد: «nmt، سغدی بودایی، namat، از اوستایی nəmata-، ختنی namata، نمد»، با ارجاع به متنِ بودایی TSP 3.229 و بحث‌های بنونیست (BSL 32 ص ۷۱) و بیلی (BSOAS 19.53 f.)، و صورتِ مانویِ nmθk و مشتقِ nmt'kr'k (شمارهٔ ۶۰۰۳، «نمدمال»). پس این واژه در سه زبانِ ایرانیِ میانه (سغدی، ختنی، فارسی میانه) گواه دارد و همین بازسازیِ ایرانی باستان را استوار می‌کند و پیکانِ نورایی (ریشه ← سغدی) را تأیید می‌کند. یادآوری آنکه صورتِ سغدی نیز، مانندِ صورتِ پهلوی، به ریشهٔ Nem 2 تعلق دارد نه به ریشهٔ جداگانهٔ «Nemata».\",\n \"sources\": [WIKT_NAMAD],\n \"ref_check\": [\n   {\"ref\": \"SOD:240\", \"status\": \"supports\",\n    \"note\": \"Gharib, Sogdian Dictionary, entry 6002 on printed p. ~240 (SOD_pages.txt leaf 306; printed ≈ leaf - 66): '6002 nmt B — namat © < Av. nəmata-, Khot. namata © ob. -y — felt — TSP 3.229; Benv. BSL 32 p71; Bailey. BSOAS 19.53 f; MDiii, nmθk'; entry 6003 'nmt'kr'k B' follows. Both the page and the content are exactly as cited.\"}\n ],\n \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p. 135 s.v. namat\", \"stance\": \"supports\",\n    \"note\": \"'Av. (1068) nəmata-, regarding which v. Benveniste, BSL 32, 1931, 82sq.' - Nyberg points to the same Benveniste article that Gharib cites for the Sogdian form, i.e. the two Middle Iranian words are treated as one Old Iranian lexeme.\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Khotanese dictionary/Indo-Scythian Studies\", \"stance\": \"supports\",\n    \"note\": \"Gharib's entry cites 'Bailey. BSOAS 19.53 f' for the Khotanese cognate namata 'felt', the third Middle Iranian witness; the Khotanese form is what makes the Old Iranian *namata- reconstruction independent of Persian.\"}\n ]\n})\n\ndoc[\"entries\"].append(e2)\n\nout='/home/sfmqrb/git/rishe/data/verification/page-359.json'\nwith open(out,'w',encoding='utf-8') as f:\n    json.dump(doc,f,ensure_ascii=False,indent=1)\nprint('written', out)\nprint('entries', [(e['entry'], len(e['nodes'])) for e in doc['entries']])\nPYEOF"
}
```


### [2026-09-07T19:53:25.768Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-359.json
entries [(0, 15), (1, 3), (2, 3)]
```


## [2026-09-07T19:53:29.134Z] TOOL CALL #73: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-359.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 359"
}
```


### [2026-09-07T19:53:30.456Z] TOOL RESULT

```
JSON OK
nodes verified: 21/21
node verdicts: {'plausible': 4, 'disputed': 1, 'confirmed': 16}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 19, 'contradicts': 1, 'not_found': 2, 'partial': 4, 'not_checked': 2}
books consulted: {'supports': 46, 'contradicts': 5, 'silent': 6, 'partial': 6} | by book: {'KLN': 7, 'BRT': 5, 'SKT': 5, 'PHD': 4, 'HRN': 4, 'BQT': 4, 'POK': 4, 'MON': 4, 'NYB': 3, 'HUB': 3, 'LAT': 3, 'WLD': 2, 'IEC': 2, 'AHD': 1, 'SYN': 1, 'FSF': 1, 'TAD': 1, 'FVQ': 1, 'AFM': 1, 'AFA': 1, 'LKT': 1, 'ARY': 1, 'CHEUNG': 1, 'KNT': 1, 'SNS': 1, 'ISS_alt_DKS': 1}
```


## [2026-09-07T19:53:59.061Z] AGENT

`verify_check.py 359` reports **0 PROBLEM lines**, 21/21 nodes verified.

## Page 359 (book p. 329) — Nem 1 / Nem 2 / Nemata 2

**Verdicts:** roots — 2 confirmed, 1 plausible. Nodes — 16 confirmed, 4 plausible, 1 disputed.
**Ref checks:** 19 supports, 4 partial, 1 contradicts, 2 not_found, 2 not_checked. 63 `consulted` entries across 26 books.

**disputed**
- *Nem 1* #2 Pahlavi `namâč` "prayer" — every modern authority derives MP namāč/namāz from the *other* Avestan nəmah- "worship" (< nam- "to bend" = Nem 2), not from nəmah- "loan". Nourai's own reference refutes him: Bartholomae's col. 1070 holds both homonyms and the sentence "vgl. mp. namāt, np. namāz 'Gebet'" stands under the *Verehrung* lemma marked "Zum V. nam-". Nyberg 135, Horn 1040, Buck 544, Moʿin (BQT 2167) and Wiktionary all agree. The chart's own NOTE reports the standard view as the dissent.

**plausible (with reasons)**
- *Nem 1* #1 Avestan `nemah 1` — the "loan" word is genuine (Vd. 4.1), but the added gloss "a prayer" belongs to the homonym; two lemmas merged so the Persian branch can hang here.
- *Nem 2* #1 "Avestan / Old Persian" — all five forms (nam-, nəmah-, namaiti, fra-/apa-namaiti, nəmata-) are real and come verbatim from Walde-Pokorny II 331-332, and Cheung 280 f. attests apanəmata / franəmante; but **no Old Persian nam- exists** (Kent's lexicon has none), so the language label is half wrong.
- *Nem 1* #11 Persian `نمره` — Wiktionary says "possibly through Arabic نمرة"; the plural نمرات and Moʿin's [معر.] tag favour Nourai's Italian→Arabic→Persian route over direct French numéro.
- ROOT *Nemata 2, Nimatâ* — the word is real (WP II 332 "av. nəmata- (auch nimata-) 'Reisig'"), but the gloss "straw, grass" and the doublet come verbatim from **Horn p. 233 no. 1041**, not from Nyberg (who glosses "felt"); and it is not a separate root — Bartholomae AiW 1068 derives it "Zum V. nam-", i.e. it is the same word Nourai already lists as "nemata 1: twigs" under Nem 2. Hübschmann 1041: "Zd. nimata- ist dunkel".
- Also #5 Arabic `nâmŭs` is plausible only because the chart skips the Syriac step (Gk. νόμος → Syr. nāmōsā → Ar. nāmūs; TAD, Wiktionary).

**Reference errors in the book (extraction is faithful — verified on the page image, copied to `data/verification/sources/refs/ocr/BOOK/359.png`)**
- *Nem 1* #3 prints **`BQT:1070`** — a page in Borhān vol. 2 (letter ج/ح). Correct is BQT:2167, which Nourai himself cites in entry 1. Evidently caught from "BRT:1070" in the adjacent box. (`error_in: book` recorded on the node.)
- *Nem 2* #1 prints **`WLD2:234`** — that page is "mand- — mari"; the article is WP II **331-332**. Substance right, page wrong.
- KLN:1048 / KLN:1026 content is exact (Klein s.v. *nimble*, s.v. *namda*) but the pages run ~45 low against the 1966 two-volume pagination — Nourai is probably citing the 1971 one-volume printing.
- FSF:328 is 2-3 pages off in the scan on disk (نماز (بردن) with the same Ferdowsī couplet is on p. 330-331) — likely a different printing.

**No extraction errors found** — the JSON matches the printed page throughout (including the empty "Different Languages" box and the `نمرات` extra).

BQT page offsets were cross-checked and are uniform: ناموس 2106, نماز 2167, نمد 2169 = pdf pages 189/250/252 of vol. 4 (+1917), all three exact. 11 web pages archived via `fetch_source.py`.
