# Verification process log — verify-page-340


## [2026-09-07T17:36:04.799Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 340 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-340.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-340.json. Write /home/sfmqrb/git/rishe/data/verification/page-340.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 340` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T17:36:06.517Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T17:36:07.226Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T17:36:07.242Z] TOOL RESULT

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


## [2026-09-07T17:36:07.328Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-340.txt"
}
```


### [2026-09-07T17:36:07.354Z] TOOL RESULT

```
1	=== PDF page 340 (book page 310) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Miždho : reward  (refs POK:746)
4	#1 (parent #0) [Avestan] refs=POK:746; KLN:957 | mîžda : reward ; mîžda-vare : wage earner ☞Bher 1
5	  #2 (parent #1) [Persian] refs=BQT:2000; HRN:219 | moždeh «مژده» : reward, worthy news ; mozd «مزد» : wage, pay, salary ; mozdůr «مزدور» : wage earner, mercenary | extra: مژدگانی
6	  #3 (parent #1) [Sogdian] refs=SOD:227 | myzd : reward, salary
7	#4 (parent #0) [Germanic] refs=AHD | medo : reward
8	  #5 (parent #4) [English] refs=None | meed : reward
9	--- entry 1 ---
10	ROOT [Semitic] M.l.h : salt  (refs KLN:928; FVA:384)
11	#1 (parent #0) [Arabic] refs=KLN:928 | m.l.h, milh : salt
12	  #2 (parent #1) [Persian] refs=FVA:384 | melh «مِلح» : salt | extra: املاح
13	مَلاحت ، ملیح ، ملیحه
14	#3 (parent #0) [Hebrew] refs=KLN:928 | melah : salt ; mallŭh : mallow plant
15	  #4 (parent #3) [Latin] refs=KLN:928 | malva : mallow
16	    #5 (parent #4) [English] refs=KLN:928 | mallow, mauve
17	  #6 (parent #3) [Greek] refs=None | malaxe : mallow
18	    #7 (parent #6) [English] refs=AHD:1527 | malachite : a dark green mineral, copper carbonate
19	#8 (parent #0) [Semitic] refs=KLN:926 | malha : salt. Name of a Phoenician colony given to a Spanish port.
20	  #9 (parent #8) [Spanish] refs=KLN:926 | Malaga : a Spanish port
21	    #10 (parent #9) [French] refs=None | Malaga
22	      #11 (parent #10) [Persian] refs=MON6:1883 | mâlâgâ «مالاگا» : a Spanish port
23	    #12 (parent #9) [English] refs=KLN:926 | Malaga : a Spanish port and its famous wine
24	--- entry 2 ---
25	ROOT Moin -> redirect to Mei 3
26	--- entry 3 ---
27	ROOT [Indo-European] Moiso : sheep  (refs POK:747)
28	#1 (parent #0) [Avestan] refs=POK:747; SYN:158 | mâěša : ram ; mâěšî : sheep
29	  #2 (parent #1) [Persian] refs=BQT:2078; HRN:226 | mîš «میش» : ram ; gâvmîš «گاومیش» : buffalo ☞Gwou
30	
```


## [2026-09-07T17:36:11.364Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-340.json",
 "description": "Read source JSON page 340"
}
```


### [2026-09-07T17:36:11.403Z] TOOL RESULT

```
{
  "pdf_page": 340,
  "book_page": 310,
  "entries": [
    {
      "root": {
        "name": "Miždho",
        "lang": "Indo-European",
        "refs": "POK:746",
        "gloss": "reward"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:746; KLN:957",
          "words": [
            {"translit": "mîžda", "gloss": "reward", "script": null},
            {"translit": "mîžda-vare", "gloss": "wage earner", "script": null, "see": ["Bher 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2000; HRN:219",
          "words": [
            {"translit": "moždeh", "gloss": "reward, worthy news", "script": "مژده"},
            {"translit": "mozd", "gloss": "wage, pay, salary", "script": "مزد"},
            {"translit": "mozdůr", "gloss": "wage earner, mercenary", "script": "مزدور"}
          ],
          "script_extra": "مژدگانی",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:227",
          "words": [
            {"translit": "myzd", "gloss": "reward, salary", "script": null}
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
            {"translit": "medo", "gloss": "reward", "script": null}
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
            {"translit": "meed", "gloss": "reward", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "M.l.h",
        "lang": "Semitic",
        "refs": "KLN:928; FVA:384",
        "gloss": "salt"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:928",
          "words": [
            {"translit": "m.l.h, milh", "gloss": "salt", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:384",
          "words": [
            {"translit": "melh", "gloss": "salt", "script": "مِلح"}
          ],
          "script_extra": "املاح\nمَلاحت ، ملیح ، ملیحه",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:928",
          "words": [
            {"translit": "melah", "gloss": "salt", "script": null},
            {"translit": "mallŭh", "gloss": "mallow plant", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Latin",
          "refs": "KLN:928",
          "words": [
            {"translit": "malva", "gloss": "mallow", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:928",
          "words": [
            {"translit": "mallow, mauve", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "Greek",
          "refs": null,
          "words": [
            {"translit": "malaxe", "gloss": "mallow", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD:1527",
          "words": [
            {"translit": "malachite", "gloss": "a dark green mineral, copper carbonate", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Semitic",
          "refs": "KLN:926",
          "words": [
            {"translit": "malha", "gloss": "salt. Name of a Phoenician colony given to a Spanish port.", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Spanish",
          "refs": "KLN:926",
          "words": [
            {"translit": "Malaga", "gloss": "a Spanish port", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "Malaga", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON6:1883",
          "words": [
            {"translit": "mâlâgâ", "gloss": "a Spanish port", "script": "مالاگا"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 9,
          "lang": "English",
          "refs": "KLN:926",
          "words": [
            {"translit": "Malaga", "gloss": "a Spanish port and its famous wine", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Moin",
        "redirect": "Mei 3"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Moiso",
        "lang": "Indo-European",
        "refs": "POK:747",
        "gloss": "sheep"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:747; SYN:158",
          "words": [
            {"translit": "mâěša", "gloss": "ram", "script": null},
            {"translit": "mâěšî", "gloss": "sheep", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2078; HRN:226",
          "words": [
            {"translit": "mîš", "gloss": "ram", "script": "میش"},
            {"translit": "gâvmîš", "gloss": "buffalo", "script": "گاومیش", "see": ["Gwou"]}
          ],
          "note": null,
          "quote": {"text": "یکی تخت زرین نهادند پیش - همه پایه ها چون سر گاومیش", "poet": "Ferdowsî"}
        }
      ]
    }
  ]
}
```


## [2026-09-07T17:36:11.463Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T17:36:11.503Z] TOOL RESULT

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


## [2026-09-07T17:36:33.415Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','FVA','AFA','SOD','AHD','BQT','HRN','MON','SYN','BRT','PHD','LKT','WLD','IEC','SKT','ARY','HUB']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600])\n    print()\n\""
}
```


## [2026-09-07T17:36:33.545Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && ls tools/"
}
```


### [2026-09-07T17:36:34.674Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N

AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
```


### [2026-09-07T17:36:34.719Z] TOOL RESULT

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
----
build_site.py
fetch_source.py
ganjoor.py
jscheck.js
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
```


## [2026-09-07T17:36:39.574Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-07T17:36:39.618Z] TOOL RESULT

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


## [2026-09-07T17:36:41.373Z] TOOL CALL #8: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SOD','BQT','MON','KLN','AHD']:\n    print(k, json.dumps(d[k].get('page_offset'),ensure_ascii=False))\n    print('  hint:', json.dumps(d[k].get('lookup_hint'),ensure_ascii=False)[:800])\n    print('  scans:', json.dumps(d[k].get('scans'),ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-07T17:36:42.642Z] TOOL RESULT

```
POK "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  hint: "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"
  scans: null
SOD "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)"
  hint: "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}"
  scans: null
BQT "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...')."
  hint: "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. |
  scans: [{"volume": "3", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "first_printed": 1208, "last_printed": 1925, "pdf_offset": -1205, "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json", "lang": "fas", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "oc
MON null
  hint: "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks)."
  scans: null
KLN "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  hint: "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."
  scans: null
AHD "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page."
  hint: "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.)."
  scans: null
```


## [2026-09-07T17:36:47.384Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: mizd\\|lemma: moiso\\|lemma: mizdho\\|mizdho\" POK_full.txt | head -20; echo ===; grep -n \"Root / lemma: m\" POK_full.txt | sed -n '1,200p' | grep -i \"miz\\|mois\\|mais\""
}
```


### [2026-09-07T17:36:47.441Z] TOOL RESULT

```
61204:Root / lemma: moiso-s or maiso-s 
(eval):1: == not found
```


## [2026-09-07T17:36:48.280Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"mizdhó\\|mizdho\\|mīždha\\|mīžda\" POK_02.txt POK_03.txt POK_01.txt | head -20"
}
```


### [2026-09-07T17:36:48.335Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T17:36:50.961Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '61195,61230p' POK_full.txt; echo ====; grep -n \"mizd\" POK_full.txt | head -20"
}
```


### [2026-09-07T17:36:51.016Z] TOOL RESULT

```
Exit code 1


Material: Old Icelandic madra^ Our Lady's Bedstraw, Yellow Bedstraw, Maid's Hair, Petty 
Mugget, Cheese Renning ', isl. hvTt-, kross-madra eic. 'Galium boreale, smooth green red 
', Old High German matara^ madder, type of plant ', Old English maedere, maeddrei. ds.. 
Middle Low German mede. Old Frisian m/de6s.; S\ay\c*modrb (e.g. Czech modrf} 'blue'. 
References: WP. II 305. 
Page(s): 747 

Root / lemma: moiso-s or maiso-s 

Meaning: sheep; hide, leatherwork 

Material: Old Indie mesa-m. 'aries, ram', mesh' fleece ', Avestan maesa-^anes, ram, 

sheep'; 

Old Icelandic me/ssm. 'basket'. Old High German me/sfsja' baggage ', Middle Low 
German /77e5e 'barrel'. 

Old Bulgarian mechb^hose', russ. mechleW, fur, hose; sack, bag' (etc.); Lithuanian 
maisas, /r75/se'Heunetz ', Latvian maiss, ma/kss'sack, bag'. Old Prussian moasis 
'bellows'; 

References: WP. II 303, Trautmann 165, Specht Indo Germanic Dekl. 52 f. 
Page(s): 747 

Root / lemma: moRs, Aryan *moRsu 

Meaning: soon 

Material: Old Indie Adv. /77a/rsJ'rash, hasty, bald, early, matutinal', maksumaksu^ right 

away '; Instr. PI. maksubhih, Superl. maksutama-, with nasal: Old Indie marjksu^ soon'; 

Avestan mosu^ immediately, right away'; common Old Indie gh- > ks- 
(eval):1: === not found
```


## [2026-09-07T17:36:51.315Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Lohn\" POK_02.txt | sed -n '1,40p'"
}
```


### [2026-09-07T17:36:51.362Z] TOOL RESULT

```
1374:Got.  fra-gildan  »vergelten,  erstatten*,  us-gildan  »vergelten*,  aisl.  gjalda »bezahlen,  entrichten,  vergelten,  wert  sein',  ags.  gieldan,  ahd.  geltan  ,be, zahlen,  vergelten,  dienen,  opfern'  (urgerm.  *seZ^ö),  aschwed.  gjalla  ^g. (*5eZ/)ö);  got.  gild  n.  ,Steuer,  Zins',  aisl.  gjald  »Bezahlung,  Lohn,  Strafe'' ags.  gield  , Bezahlung,  Abgabe»  Opfer,  Bruderschaft',  aisl.  gildi  ,Mitglied! schaff,  ags.  gilde  n.  ds.,  güda  m.  , Gildenbruder'  (daraus  mir.  ^17^^^ ,Knappe'),  mnd.  gilde,  daraus  nhd.  Gilde;  ahd.  gelt  , Bezahlung,  Vergeltung Opfer  usw.',  nhd.  Geld;  got.  gilstr  n.  ,Steuer*,  ahd.  gelstar  {^geld-tra-) »Opfer,  Steuer';  aus  ndd.  gellen  =  gelten  stammt  lit.  geliüoti  ,gelten';
5005:air.  log,  lüag,  lüach  ,Lohn,  Preis^  (mit  g-  oder  ^Ä-Formans), /oZac2  (foluth) ^Substanz'  =  cymr.  golud  ,Reichtum',  acorn.  wuludoc  ,dives'  (*upo-lau-to-m)  ; cymr.  llaioen  ^fröhlich^  (,*genießendQ ;  auch  cymr.  llawer  jY'iqYj  air.  lour ^genug'  als  ursprüngliches  Subst.  ,Zahl,  große  Menge^  aus  Hdueros  =  gr. laqög ;
5006:got.  laun  Ti,,  ahd.  lön  (n._,  m.)  ,Lohn,  Vergeltung^,  anord.  laun  n.  PI., ags.  lean  ds. ;
5163:gr.  XccTQOv  n.  ,Lohn,  Sold',  Xargevg,  Xdrgig  , Lohnarbeiter',  Xargsvw  , diene um.  Sold* ;  lat.  latrö  ist  gr.  Lw. ;
6364:fraglich  ist  Zugehörigkeit  von  lat.  merx  ,Ware',  merces,  -edis  , Preis, Lohn.  Sold',  mercärl  .handeln',  osk.  amiricadut  .handelsmäßig',  amirikum .commercium'.
6463:mizdhö-  ,Lohn,  Sold^
6464:Ai.  midhd-  n.  , Kampfpreis,  Wettkampf^,  av.  Trvt^da-  n.,  osset.  mizd,  myzd ,Lohn',  np.  muzd  ,Lohn^;  gr.  (xta&ög  ,Sold^;  got.  mizdö  ,Lohn^,  ags.  meord ds.  und  ags.  med,  as.  meda,  ahd.  meta,  miata  ds.,  nhd.  Miete]  aksl.  mbzda, rmzda  ,Lohn^
```


## [2026-09-07T17:36:57.660Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find line index of 'mizdhö-' \nfor i,l in enumerate(lines):\n    if 'mizdh' in l or 'moiso' in l or 'maiso' in l or 'maesa' in l or 'maesa' in l:\n        print(i+1,'|',l[:150])\nEOF"
}
```


### [2026-09-07T17:36:59.065Z] TOOL RESULT

```
6463 | mizdhö-  ,Lohn,  Sold^
6477 | moiso-s  oder   maiso-s  ,Schaf;   Fell,   daraus  gefertiote    Schläuche,   Säcke'.
6478 | Ai.  mesd-   m.    , Widder',   mesl-  ,Schaffell',   av.   maesa-   ,Widder,   Schaf;
```


## [2026-09-07T17:36:59.321Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npos=t.find('mizdh')\nleaf=t.count('\\f',0,pos)\nprint('mizdh leaf',leaf,'-> printed page',leaf+344)\nprint(repr(t[pos-1500:pos+900]))\nEOF"
}
```


### [2026-09-07T17:37:00.744Z] TOOL RESULT

```
mizdh leaf 407 -> printed page 751
"f.,  129.\nmeuk-  ,kratzen,  ritzen'.\nGr.  dfxvKdlaL'  al  d'HLÖeg  rwv  ßslwvj  Tcaqd  rö  d^vaasiv  Hes.,  d(.iva(7(ü,  att. df.LVTi;(jD  ,ritze,  zerkratze',  d^vxrj  ,Riß,  Schramme',  usw. ;  lat.  mucrö  ,scharfe Spitze,  Speer,  Schwert';  vielleicht  zu  ags.  ge-myscan  ,plagen,  entstellen' (^muhskjan)  und  lit.  müsti  , schlagen';  vielleicht  auch  ai.  musti  f.,  av. musti-  ,Faust'?\nWP.  II  255,  WH.  II  117  f.\nmeu-s-  ,stehlen'  s.  S.  753.\nI.  mezg-  ,unter tauchen'.\nAi.  mdjjati  ,taucht  unter,  sinkt  unter'  (Part.  Perf.  Pass.  magna-  aus *mazgnd-),  Kaus.  majjayati  ,versenkt';  lat.  mergö,  -ere  ,tauche  ein,  ver- senke, verberge',  davon  mergus  m.  ,Taucher  (Wasservogel);  Rebsenker'; halt.  Iterativ  *mazgäiö  ,tauche  mehrfach  ein,  wasche'  in  lit.  mazgöti,  lett.\n746\nmazgät  ^waschen^  Vgl.  estn.  mdskmaj  mordw.  muskdms,  samojed.  ma$u Ungar,  mosni  , waschen^;  usw.]  unsicher,  ob  hierher  gr.  ulayo)  ^mische^  aus *mi-mzgö]  anders  oben  S.  714.\nWP.  II  100 f.,    WH.  II  76 f.,    Trautmann  173,   H.  Güntert  Kaljpso  51.\n2.  mezg-  ^stricken,  knüpfen^;  mozgo-  ,Knoten^\nAhd.  as.  mäscaj  ags.  max,  rnÖBsci'  ^Masche',  aisl.  mgshvi  ds.; lit.  mezgü,  mBgsti  , knüpfen,  stricken^,  mäzgas,  lett.  mazgs  , Knoten^,  Üt. mazgyti  Iter.  ,stricken*^,  makstyti  ,flechten^,  lett.  mezget,  mi^get  ^verrenken' mezgit  , ranken^  (russ.  mdzgarh  , Spinne^?  s.  Berneker  II  28). WP.  II  301,  Trautmann  172.\nmizdhö-  ,Lohn,  Sold^\nAi.  midhd-  n.  , Kampfpreis,  Wettkampf^,  av.  Trvt^da-  n.,  osset.  mizd,  myzd ,Lohn',  np.  muzd  ,Lohn^;  gr.  (xta&ög  ,Sold^;  got.  mizdö  ,Lohn^,  ags.  meord ds.  und  ags.  med,  as.  meda,  ahd.  meta,  miata  ds.,  nhd.  Miete]  aksl.  mbzda, rmzda  ,Lohn^\nWP.\x0c  II  301,  Trautmann  188.\nznö-,  mo-lo-  ,sich  mühend\nGr.  fxojXog  ^Anstrengung,  Mühe^,  f.LwXiw,  kiet.  y.u)Viu}  ,prozessiere',  pSAvg , ermattet^,  vielleicht  nöXiq  ,kaum^  (o  für  w  nach  iioyig)]  Ic-fxoTog  ,uner- müdlich%-  lat.  möles  f.  ,Last,  Masse',  Denom.  mölior,  -tri  ,mit  Anstrengung wegschaff en%  molestus  ,verdrießlich,  lästig,  beschwerlich'  (Analogie  zu modestus) ;  got.  af-mauips  ,ermüdet',  ahd.  muoan,  mhd.  müen,  müejen ,beunruhigen,  beschweren',  ndl.  moeijen  ,belästigen,  bemühen';  ahd.  muodij as.  mödi  ,müde',  ags.  mede  ,müde,  betrübt"
```


## [2026-09-07T17:37:14.856Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 mizdh ===\"; grep -n \"mizdh\\|moiso\\|maiso\" incoming/WLD/WLD_Bd2_pages.txt | head; echo \"=== WLD Bd3 ===\"; grep -n \"mizdh\\|moiso-\\|maiso\" WLD_band3.txt | head; echo \"=== AHD mizdho ===\"; grep -n -i \"mizdh\\|^meed\\|MEED\" AHD_watkins1985.txt | head -20; echo \"=== AHD moiso ===\"; grep -n -i \"moiso\\|maiso\" AHD_watkins1985.txt | head"
}
```


### [2026-09-07T17:37:14.930Z] TOOL RESULT

```
=== WLD Bd2 mizdh ===
16320:als „*Bespringer“,                  s.   "^moisos oder ^maisos „Schaf' ),                      Uhlenbeck      Ai.   Wb.
19891:mizdho- „LohD,                  Sold^^    feegen den Ansatz         '^'mid^dho-    s.    Brugmann      626
20003:                                  moiso-s Oder maiso-s          — moks, nioksu                         303
20020:moiso-s Oder maiso-s „Schaf;                         PlieB,      Pell,   daraus gefertigte, Schlauche,
=== WLD Bd3 ===
=== AHD mizdho ===
761:mizdho-
762:mizdho-. Reward. West Germanic *médé- in Old English méd, reward, compensation, meed: MEED. [Pok. mizdho- 746. m6-. To exert oneself. Suffixed form *mé-I- in: a. Latin molés, heavy bulk, mass, massive structure: MOLE%, MOLECULE; DEMOLISH; b. Latin molestus (irregularly from mdélés), labored, difficult, troublesome: MOLEST. [Pok. m6- 746.] m6d-. To meet, assemble. 1. Germanic *mdtjan in Old English métan, to meet: MEET!. 2. Germanic *méta- in Old English mot, gemét (ge-, together; see kom), meet- ing, moot, assembly, council: MOOT; FOLKMOTE, GEMOT, WITENAGEMOT. 3. Perhaps suffixed zero-grade form *mod-tlo- in Germanic *mathla- in Old Norse mdl, speech, agreement (> Norwegian mdi, speech): MAIL; (BLACKMAIL), RIKSMAL. [Pok. mdd- 746.] modhro-. A color. Germanic *madraz in Old English meedere, madder: MADDER!. [Pok. modhro- 747.] molko-. Skin bag. Germanic *malhé- in Old High Ger- man malha, pouch, bag, akin to the Germanic source of Old French male, bag: Matti. [Pok. molko- 747.] mone. Neck, nape of the neck. 1. Germanic *man6 in Old English manu, mane: MANE. 2. Latin monile, necklace: MONILIFORM. [Pok. mono- 747.] mori-. Body of water; lake (?), sea (?). 1. Germanic *mari- in: a. Old English mere (> Middle English mere), sea, lake, pond: MERE?; (MERMAID); b. Old Norse marr, sea, akin to the Scandinavian source of MARRAM; C. Old High German mari (> German Meer), sea: MEER- SCHAUM. 2. Germanic *mariska-, water-logged land, in: a. Old English mersc, merisc, marsh: MARSH; b. Old French marasc, maresc, marsh: MORASS. 3. Latin mare (> French mer), sea: MARE?, (MARINARA), MARINE, MARI- TIME; BECHE-DE-MER, MARICOLOUS, MARICULTURE, OR- MER, ULTRAMARINE. [Pok. mori 748.] mormor-. Also murmur-. Murmur. Imitative root. Latin murmur, a murmur: MURMUR. [Pok. mormor- 748.] moro-. Blackberry, mulberry. 1. Greek moron, mulberry, in sukomoros, an African fig tree: SYCAMORE. 2. Latin morum, mulberry (probably from Greek): MORULA, MUR- REY; MULBERRY. [Pok. moro- 749.] morwi-. Ant. 1. Germanic variant form *meur- in Danish myre, ant, akin to the Scandinavian source of Middle English mire, ant: PISMIRE. 2. Variant form *morm- in: a. Greek murméx, ant: MYRMECO-; b. (with dissimila- tion) Latin formica, ant: FORMIC, FORMICARY; FORMICI- vorous. [Pok. morui- 749.] m6(u)lo-. Name of a plant. Greek mélu, moly: MOLY. [Pok. mé(u)-lo- 750.] m6(u)ro-. Foolish. Greek méros, foolish: MORON; OXYMO- RON. [Pok. mé(u)ro- 750.] mozgo-. Marrow. Germanic *mazg6- in Old English mezrg, mzerh, marrow: MARROW. [Pok. moz-g-o- 750.] mregh-m(n)o-. Brain. 1. Germanic *brag-na- in Old English bregen, brain: BRAIN. 2. Greek bregma, the front part of the head: BREGMA. [Pok. mregh-m(n)o- 750.] mregh-u-. Short. I. Suffixed form *mregh-w-i- in Latin brevis, short (> briima, the shortest day, winter): BRIEF, BRUMAL; ABBREVIATE, (ABRIDGE). II. Zero-grade form *“mrghu-. 1.Germanic *murgja-, short, also pleasant, joyful, in: a. Old English myrge, mirige, pleasant: MERRY; b. Germanic *murgithd, pleasantness, in Old English myrgth, pleasure, joy: MIRTH. 2. Greek brakhus, short: BRACHY-; AMPHIBRACH, TRIBRACH. 3. Greek com- parative brakhion, shorter, hence also “upper arm” (as opposed to the longer forearm): BRACE, BRACERO, BRA- CHIUM, BRASSARD, BRASSIERE, PRETZEL; EMBRACE. [Pok. mreghu- 750.] mu'-. Imitative of inarticulate sounds. 1. Reduplicated form in Germanic *mum- in: a. Middle Low German mummen, to be silent, akin to Middle English mum, silent: MUM}; b. Icelandic mumpa, to eat greedily, akin to the probable Scandinavian source of dialectal English mump, to mumble, grimace: MUMPs; c. Low German
1841:MEATUS mei-1 MECHANIC magh-1 MECHANISM magh-! MECHANO- magh-! MECONIUM mak-1 MECOPTERAN miak-, pet- MEDDLE meik- MEDIAL medhyo- MEDIAN medhyo- MEDIASTINUM medhyo- MEDIATE medhyo- MEDICAL med- MEDICATE med- MEDICINE med- MEDICO med- MEDIEVAL alw-, medhyo- MEDIOCRE medhyo- MEDITATE med- MEDITERRANEAN medhyo-, ters- MEDIUM medhyo- MEDLEY meik- MEDULLA (s)mer-3 MEED mizdho-
=== AHD moiso ===
```


## [2026-09-07T17:37:16.537Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN meed ===\"; grep -n \"^meed\" KLN_1966.txt | head; echo \"=== KLN mallow/malva/malachite/Malaga ===\"; grep -n \"^mallow\\|^malachite\\|^Malaga\\|^mauve\\|^malva\" KLN_1966.txt | head -20"
}
```


### [2026-09-07T17:37:16.609Z] TOOL RESULT

```
=== KLN meed ===
=== KLN mallow/malva/malachite/Malaga ===
22633:Malaga,  n.,  white  wine  exported  from  Malaga, port  in  Spain.  —  The  name  of  Malaga,  orig.  a Phoenician  colony,  comes  fr.  Phoen.  malha, ‘salt’,  which  is  rel.  to  Heb.  melah.  See  mallow. Malagasy,  adj.,  pertaining  to  Madagascar,  its people  or  its  language;  n.,  1)  a  native  of  Mada¬ gascar;  2)  the  language  of  the  Malagasy.  — Related  to  Madagas-  in  Madagas-car.  For  the interchangeability  of  -l-  and  -d-  cp.  L.  lingua, ‘tongue’,  fr.  OL.  dingua  (see  lingual  and  cp. words  there  referred  to).
23185:mauve,  n.  and  adj.,  purple  dye.  —  F.,  fr.  L.  mal- va,  ‘mallow’.  See  mallow, maverick,  n.,  unbranded  cattle.  —  Named  after Samuel  A.  Maverick  (died  in  1870),  a  civil  en¬ gineer  in  Texas,  in  allusion  to  his  unbranded cattle.
```


## [2026-09-07T17:37:25.116Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== mallow ===\"; grep -n \"mallow,\" KLN_1966.txt | head -10; echo \"=== malachite ===\"; grep -n -i \"malachite\" KLN_1966.txt | head -5; echo \"=== meed ===\"; grep -n \"meed,\" KLN_1966.txt | head -5"
}
```


### [2026-09-07T17:37:25.199Z] TOOL RESULT

```
=== mallow ===
22623:malaceous,  adj.  —  See  prec.  word  and  -aceous. Malachi,  1)  masc.  PN. ;  2)  in  the  Bible,  the  last in  the  order  of  the  Twelve  Prophets.  —  Heb. Mal'akht,  lit.  ‘my  messenger’,  fr.  mal'akh, ‘messenger’,  fr.  base  l-’-k ,  ‘to  send  ,  which  is  rel. to  Arab,  la’ aka,  al’aka,  ‘he  sent’, malachite,  n.  —  F.,  formed  with  subst.  suff.  -ite fr.  Gk.  |xaXdr/T),  ‘mallow’.  See  mallow, malacia,  n.,  pathological  softening  of  a  tissue (med)  —  Medical  L.,  fr.  Gk.  paXaxta,  ‘soft¬ ness’,  fr.  paXaxoc,  ‘soft’.  See  malaco-  and  1st  -ia. -malacia,  combining  form  denoting  pathological softening  (med.)  —  See  prec.  word, malaco-,  before  a  vowel  malac-,  combining  form meaning‘soft’. — Gk.u.ocXaxo-,  paXax-,  fr.  p.aXa- y.oq,  ‘soft’,  which  stands  for  * ml le-qos,  and  is  rel. to  Gk.  pXa£,  gen.  pXaxoc,  ‘lazy,  inactive,  slug¬ gish’,  fr.  I.-E.  base  •melaq-,  ‘to  soften’,  whence also  Ir.  malcaim,  ‘I  rot’,  MIr.  blen,  the  groins  . Base  *  melaq-  is  enlarged  fr.  base  *(s)mel-,  ‘to rub,  grind’,  whence  Gk.  p.oXr],  later  (zuXoq, ‘mill’,  L.  molere,  ‘to  grind’,  molina,  ‘mill’.  See meal,  ‘edible  grain’,  and  cp.  words  there  referred to.
22686:Derivative:  malle-al,  adj. mallow,  n.,  name  of  a  plant.  —  ME.  malwe,  fr. OE.  mealwe,  fr.  L.  malva,  which,  together  with Gk.  paXay//;,  of  s.m.,  is  borrowed  fr.  Heb.  mal- luah,  ‘mallow’  (Job  30:4),  a  derivative  of  melah, ‘salt’ ;  cp.  Aram,  milha,  Syr.  melha,  Arab,  mill), Akkad,  milu,  ‘salt’.  (See  H.  Lewy,  Die  semiti- schen  Fremdworter  im  Griechischen,  3 1  f.,  and Immanuel  Low,  Flora  der  Juden,  I  227  ff.  and 242  ff.)  Cp.  malachite,  malvacious,  mauve.  Cp. also  Malaga.
23185:mauve,  n.  and  adj.,  purple  dye.  —  F.,  fr.  L.  mal- va,  ‘mallow’.  See  mallow, maverick,  n.,  unbranded  cattle.  —  Named  after Samuel  A.  Maverick  (died  in  1870),  a  civil  en¬ gineer  in  Texas,  in  allusion  to  his  unbranded cattle.
=== malachite ===
22623:malaceous,  adj.  —  See  prec.  word  and  -aceous. Malachi,  1)  masc.  PN. ;  2)  in  the  Bible,  the  last in  the  order  of  the  Twelve  Prophets.  —  Heb. Mal'akht,  lit.  ‘my  messenger’,  fr.  mal'akh, ‘messenger’,  fr.  base  l-’-k ,  ‘to  send  ,  which  is  rel. to  Arab,  la’ aka,  al’aka,  ‘he  sent’, malachite,  n.  —  F.,  formed  with  subst.  suff.  -ite fr.  Gk.  |xaXdr/T),  ‘mallow’.  See  mallow, malacia,  n.,  pathological  softening  of  a  tissue (med)  —  Medical  L.,  fr.  Gk.  paXaxta,  ‘soft¬ ness’,  fr.  paXaxoc,  ‘soft’.  See  malaco-  and  1st  -ia. -malacia,  combining  form  denoting  pathological softening  (med.)  —  See  prec.  word, malaco-,  before  a  vowel  malac-,  combining  form meaning‘soft’. — Gk.u.ocXaxo-,  paXax-,  fr.  p.aXa- y.oq,  ‘soft’,  which  stands  for  * ml le-qos,  and  is  rel. to  Gk.  pXa£,  gen.  pXaxoc,  ‘lazy,  inactive,  slug¬ gish’,  fr.  I.-E.  base  •melaq-,  ‘to  soften’,  whence also  Ir.  malcaim,  ‘I  rot’,  MIr.  blen,  the  groins  . Base  *  melaq-  is  enlarged  fr.  base  *(s)mel-,  ‘to rub,  grind’,  whence  Gk.  p.oXr],  later  (zuXoq, ‘mill’,  L.  molere,  ‘to  grind’,  molina,  ‘mill’.  See meal,  ‘edible  grain’,  and  cp.  words  there  referred to.
22686:Derivative:  malle-al,  adj. mallow,  n.,  name  of  a  plant.  —  ME.  malwe,  fr. OE.  mealwe,  fr.  L.  malva,  which,  together  with Gk.  paXay//;,  of  s.m.,  is  borrowed  fr.  Heb.  mal- luah,  ‘mallow’  (Job  30:4),  a  derivative  of  melah, ‘salt’ ;  cp.  Aram,  milha,  Syr.  melha,  Arab,  mill), Akkad,  milu,  ‘salt’.  (See  H.  Lewy,  Die  semiti- schen  Fremdworter  im  Griechischen,  3 1  f.,  and Immanuel  Low,  Flora  der  Juden,  I  227  ff.  and 242  ff.)  Cp.  malachite,  malvacious,  mauve.  Cp. also  Malaga.
22711:Malus,  n.,  name  of  a  southern  constellation  (as- tron.)  —  Lit.  ‘mast’,  fr.  L.  malus,  fr.  *mados, *mazdos;  cogn.  with  OE.  truest,  ‘mast’.  See mast,  ‘pole’.  For  the  change  of  I.-E.  d  to  /  in Latin  cp.  lachrymal  and  words  there  referred  to. Malva,  n.,  a  genus  of  plants,  the  mallow  (bot.)  — L.,  ‘mallow’.  See  mallow  and  cp.  malachite, mauve.
=== meed ===
23322:Derivatives:  medus-al,  medus-an,  adjs. medusoid,  1)  adj.,  like  a  medusa;  2)  a  medusalike gonophore  of  a  hydrozoan  (zool.)  —  Com¬ pounded  of  medusa  and  Gk.  -octS r\t;,  ‘like’,  fr. e!8o?,  ‘shape,  form’.  See  -oid. meed,  n.,  reward  (poet.)  —  ME.  mede,  fr.  OE. med,  meord,  ‘reward,  requital’,  rel.  to  OS.  meda, OHG.  meta,  miata,  mieta,  MHG.,  G.  miete, Goth,  mizdd,  ‘reward’,  and  cogn.  with  OI.  mi- dham  (for  *mizdha-),  ‘prize,  reward,  contest, booty’,  midhvah,  ‘giving  in  abundance’,  Avestic mizda,  ‘reward’,  Gk.  piaD8i;  (for  •mizdhos), ‘wages,  pay’,  OSlav.  mizda,  ‘salary’, meek,  adj.  —  ME.  mek,  fr.  earlier  rneoc,  fr. ON.  mjukr,  ‘mild,  soft,  gentle’,  which  is  rel.  to Goth,  muka-modei,  ‘humility’,  and  prob.  cogn. with  OIr.  mocht  (for  *mukto-),  ‘mild,  gentle’, L.  mucus,  ‘mucus  of  the  nose’.  See  mucus  and cp.  words  there  referred  to.
```


## [2026-09-07T17:37:32.081Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor pat in ['meed,  n.,  reward','mallow,  n.,  name  of  a  plant','Malaga,  n.,  white  wine','malachite,  n.','mauve,  n.  and  adj']:\n    pos=t.find(pat)\n    leaf=t.count('\\f',0,pos)\n    print(pat[:20],'leaf',leaf,'approx printed pages', 2*(leaf-12), 2*(leaf-12)+1)\nEOF"
}
```


### [2026-09-07T17:37:33.618Z] TOOL RESULT

```
meed,  n.,  reward leaf 513 approx printed pages 1002 1003
mallow,  n.,  name   leaf 499 approx printed pages 974 975
Malaga,  n.,  white  leaf 498 approx printed pages 972 973
malachite,  n. leaf 497 approx printed pages 970 971
mauve,  n.  and  adj leaf 510 approx printed pages 996 997
```


## [2026-09-07T17:37:34.202Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (479,480,481,482,483,484,485,486):\n    pass\n# print running numbers around the meed leaf to calibrate\nimport re\npos=t.find('meed,  n.,  reward'); leaf=t.count('\\f',0,pos)\nfor i in range(leaf-1,leaf+2):\n    print('--- leaf',i,'---')\n    print(leaves[i][:200].replace('\\n',' '))\n    print('...tail:',leaves[i][-200:].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T17:37:35.512Z] TOOL RESULT

```
--- leaf 512 ---
i-,  ‘to  change;  to  change  one’s  place;  to  go’. See  mean,  ‘of  low  rank’,  and  cp.  irremeable,  per¬ meate.  Cp.  also  conge. Mecca,  n.,  city  in  Arabia,  birthplace  of  Moham¬ med  a
...tail: o  heal,  cure’,  fr.  medicus.  See  medical and  verbal  suff.  -ate. Derivatives:  medication  (q.v.),  medicat-ive,  adj., medicator  (q.v.),  medicat-ory,  adj. medication,  n.  —  L.  medicatio,
--- leaf 513 ---
  gen.  -onis, ‘healing,  cure’,  fr.  medicatus,  pp.  of  medicare, medicdri.  See  prec.  word  and  -ion. medicator,  n.  —  Late  L.  medicator,  ‘physician’, fr.  L.  medicatus,  pp.  of  medica
...tail: ‘to  measure’.  See  mete, ‘to  measure’. Derivatives:  meet-ly,  adv.,  meet-ness,  n. Meg,  fem.  PN.  —  Dimin.  of  Margaret, mega-,  before  a  vowel  meg-,  combining  form meaning  'large,  gre
--- leaf 514 ---
at’  (in  physics  it  is  used  in  the meaning  of  ‘a  million  times’,  e.g.  megavolt  —  a million  volts).  —  Fr.  Gk.  pEyap,  fem.  psyiXv], neut.  peyx,  ‘great,  large,  mighty’,  which  i
...tail: he  second  element  is  rel.  to  Heb. tzadaq,  ‘he  was  eighteous’,  tzaddlq,  ‘just,  right¬ eous'.  See  tzaddik. meld,  tr.  and  intr.  v.,  in  pinochle,  to  announce for  a  score.  —  G.  m
```


## [2026-09-07T17:37:50.207Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(495,516):\n    nums=re.findall(r'(?<![\\d.])(9\\d\\d|1\\d\\d\\d)(?![\\d.])', leaves[i])\n    head=leaves[i][:60].replace('\\n',' ')\n    print(i, nums[:8], '|', head)\nEOF"
}
```


### [2026-09-07T17:37:51.475Z] TOOL RESULT

```
495 ['921', '1900', '1866', '922'] | d,  adj. maculate,  adj.  —  L.  maculatus,  spotted  ,  pp.
496 ['923', '1638', '1715', '1775', '1816', '924'] |  1215. _ ML.,  ‘great  charter’.  See  magnum  and chart. ma
497 ['925', '926'] |   .  Cp. also  Mac-. Derivatives :  maiden,  adj.,  maiden-h
498 ['927', '1658', '1741', '1868', '1945', '928'] | v.,  maladroit-ness, n. malady,  n.,  sickness,  disease.  —
499 ['1514', '929', '1628', '1766', '1834', '1250', '1517', '1811'] | aught. malleolus,  n.,  one  of  the  two  rounded  projecti
500 ['930', '931', '1886'] |  Yakut  mamma ,  ‘earth’  (the mammoth  was  believed  to  r
501 ['932', '1723', '933', '934'] | a. See  pandora. mandolin,  n.  —  F.  mandoline,  fr.  It. 
502 ['1654', '1722', '1598', '1666', '935', '936'] | late,  tr.  v.  —  Back  formation  fr.  manipul¬ ation. Der
503 ['1311', '937', '1500', '1571', '1936', '938', '939'] | anx  cat. many,  adj.  and  n.  —  ME.  mani,  moni,  meni, 
504 ['1678', '1874', '1786', '1889', '1569', '1625'] | =  F.)  marche,  fr. marcher.  See  prec.  word  and  cp.  d
505 ['940', '941', '1280', '1062'] | —  L.  maritalis,  ‘of  mar¬ riage',  fr.  maritus,  ‘a  mar
506 ['1658', '1730', '942', '943', '1850', '1914', '1699', '1768'] |  See  marital  and  marriage. Derivatives:  marri-ed,  adj.,
507 ['1823', '1911', '1836', '1735', '946', '947'] | —  Prob.  fr. F.  massue,  ‘club’,  fr.  VL.  *mattiuca,  fr
508 [] | nis, ‘chewing,  mastication’,  fr.  masticatus,  pp.  of mas
509 ['948', '949', '1879', '1930'] | o  measure’.  See  meter,  ‘poetical  rhythm’, and  cp.  wor
510 ['950', '1870', '1853', '1927', '1748', '1832', '1831'] | ark,  stain’;  see  mole, ‘spot’.  For  the  second  element
511 ['953'] | acc.), ON.  mer,  OHG.,  MHG.,  G.  mir,  Goth,  mis, ‘me’  
512 ['1605'] | i-,  ‘to  change;  to  change  one’s  place;  to  go’. See  
513 ['957'] |   gen.  -onis, ‘healing,  cure’,  fr.  medicatus,  pp.  of  
514 ['958', '1750', '1817', '1807'] | at’  (in  physics  it  is  used  in  the meaning  of  ‘a  mi
515 ['1748', '1832', '1819'] | elden,  ‘to  announce’,  fr. MHG.  melden,  ‘to  betray,  re
```


## [2026-09-07T17:38:08.888Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (497,498,499):\n    L=leaves[i]\n    print('=== leaf',i,'len',len(L))\n    import re\n    for m in re.finditer(r'(?<![\\d.])(9[0-9]\\d)(?![\\d.])',L):\n        print('  num',m.group(1),'at',m.start())\n    for pat in ['Malaga','mallow,  n.','malachite','malva','Malva']:\n        p=L.find(pat)\n        if p>=0: print('  ',pat,'at',p)\nEOF"
}
```


### [2026-09-07T17:38:10.208Z] TOOL RESULT

```
=== leaf 497 len 11535
  num 925 at 1753
  num 926 at 10928
   malachite at 9886
=== leaf 498 len 11316
  num 927 at 2317
  num 928 at 11182
   Malaga at 486
=== leaf 499 len 11425
  num 929 at 2916
   Malaga at 1518
   mallow,  n. at 1018
   malachite at 1475
   malva at 1096
   Malva at 2582
```


## [2026-09-07T17:38:57.251Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN muzd ===\"; grep -n \"muzd\\|mužd\\|mužda\" HRN.txt | head -20; echo \"=== HRN mēš/mīš ===\"; grep -n \"mêš\\|mîš\\|mēš\\|Schaf\" HRN.txt | head -20"
}
```


### [2026-09-07T17:38:57.336Z] TOOL RESULT

```
=== HRN muzd ===
5087:mizda- und zu dem Abfall der Endung np. Hor]muzd
8507:978. muzd, muzd 'Lohn, Preis', muzde {mizde) 'frohe Bot-
=== HRN mēš/mīš ===
2358:arm. LW. bun 'Stamm (eines Baumes), Schaft*.
4623:(302) ; sar. ydtid *Hut, hohe Mütze aus Schaffell'.
6310:Rind', ya/n. «li^wr 'Schaf, Vieh überhaupt' (Tomaschok,
```


## [2026-09-07T17:38:58.874Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT mizda ===\"; grep -n \"mīžda\\|mizda\\|mîžda\" BRT.txt | head -10; echo \"=== BRT maesa ===\"; grep -n \"maēša\\|maesa\\|maēšī\" BRT.txt | head -10; echo \"=== PHD ===\"; grep -n \"^muzd\\|muzd\\b\\|^mēš\\|mēš \" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-07T17:38:58.960Z] TOOL RESULT

```
=== BRT mizda ===
6189:Gen.  subj.  und  obj.:  alsm  *d>nidyäi{iA.) .  .  rayS  'st/  ". .  jrXoiiTOU  fioi'pai"  Y.  4J.  i ; —  abifra  (sd.) . .  ya  vaahsus  'sis  mananha Y._3i5.i3;  —  aiahya  yasa  {%A:)  'slm  y am iiyam  Y.  54.1;  —  °M/a  ^ae^ananqm viäu/(sd.)  ahurakya  mazdS  ".  .  des  AhM. Belohnungen  fiir  die  Taten  . ."  Y.2<V,4; — ■  nöit  kl  "M  *^ao^nanqm  vimysit  N. 16  ij);  —  zard>!ustrahe  .  .  asatinS  'itmia fravaiimca  yazamatde  Vr.  16. 2 ;  2,  Yt  13. 95;  —  tti  ahmt  nmane  Jamyarps  yh  asao- nqm  xshätas/a  'sayasca  . .  paitisatitayasla Y.  60. 2.  a)  mit  vanAav-  Adj.  und  aka^ Adj.  näher  bestimmt:  vatfkttyascä  °Ssi/ .. yS  ns  ara^ä  (sd.)  irmavaia^a  asanhäxs ^■5^-3't  —  syao^ana  mizdavqn  (sd.)  .. akfm  akai  vamthlm  'stm  vanhaavi  Y. 43. 5 ;  —  tSm  vatmklm  yasä  (sd.)  °sim  Y. 5;. ai;  —  maifyn  siaya  ahm  vaaAuya 'st  gaui  (sd)  Y.5/.  10«;  —  xmBth  afn- n>ntu  ahmya  nmsne  vawtklm  °/lm  i^a- parqm  Yt.  /J. i  S 7 ;  —  vaauAlsca  aöa  vaau- klsca  'sayS  Y.53.3;  —  yhca  tsi  gmh *aiura.mazda  ..  iSä  . .  vanukim  iihl/  'lim . .  ihm  .  .  *panndlm  yazamaidi  Y.^S. if  b)  Du.  'die  beiden,  beiderlei  Lose', d.  i.  (das)  gute  und  (das)  böse:  tmnanha (sd.) y5  dä%alibyd  priLratüm  xsayqs  'äfä*"^ üista  ". .,  der  über  beiderlei  Lose  gebietend den  Klugen  den  wahren  Ratav  versprochen hat"  Y.57.5.  A)  als  Gottheit,  die  die Lose,  insbesondere  die  guten  verteilt,  im jAw.  als  Göttin  des  durch  Frömmigkeit  ver- dienten Wohlstands*';  I)  im  gAw,:  Siraosö 'sfi  mqza.raya  (sd.)  Aacimnif  ya  vT  altl *ran3ibya  savlfi(sd.)  vldayäi  \ .  4j.  1 2 ; -^ sraosS  .  .  yU  *'li^  haiaiti  *mqxaraya  V. 27.6,  Vr. /2.1;  —  ya  vldayaf  'sts' (HS.) räshqm  (sd.)  Y.j^.  la;  —  ys  fta  'sSis aojaifha  var>dayaita  yqm  ,  .  gai^qm  .  . Y.  so.  3.  a)  Du,  in  Verbindung  mit armaiay-  Du.  ^A.  und  Arm.':  yads  ahm zivlm  (sd.)  .  ,  mazdasca  .  .  'sicil  armaitl Y.31.^.  II)  im  jAw.:  yö  'lim  yazäite ..k5  mihnm  yazaiieY\..i-j.2;  —  -/j  (VS.) srlre  'si  banumaili  .  .  °li  dä'ire  vehäm i^arifiilYt.sy.^;  6of.*;  —  hm  hacSl  'Hl pourvsj^ä'iira'Yt  /j?.54;  — /rä  mqm  aiwt.- urvalsayatfuha  marsdik?m  'al  (als  VS.) hnzaiti  Yl  77. 1 5 ;  —  'lim  . .  darr/S.- variiman3m..bartntltn  vispä  baSlazsY.S'i. 2;  —  sraohmla  'lim  nairXmca  sauh>m IVyt.40;   —  fravalays   .  .    'Isil  balsaza
6412:•  j.  asö.mizda-  Adj.  (fem.  °dä^  'den Lohn  der  Gerechtigkeit  eintragend':  ta (näml,  gai:ä)  nS  buyan  humizda  (sd.)  .  . 'da  Y.  5J.  3.
10442:fravartis  agarbäyatä  "Fr.  wurde  gefangen  i genommen"  Bh.  2. 13.  E  3)  'etwas  weg- 1 nehmen  von— (Abi.)':  g}urvaya  Äipälai'e. sävar»  Y.  r).  28.  4)  'einen  Anteil  be- ! kommen  von  — '  (Gen.):  tnä  hl  mairyö'. giurvayöit  "nicht  soll  davon  was  be- kommen , ."  Yt.  8. 59;  —  yezi  se  mairys gfurvay.V  Yt.Äöo;  —  mizdahe  .  .  g>r)W- 1 ytiti  yS  girswyaUe  VyL  JO  (?).  5)  'i^-
20563:•  j.,  g.  mizda-''  n.  i)  TLohn'  als  das  ver- abredete oder  zugesicherte  oder  gebührende Äquivalent  einer  Leistung  (usw.) :  kaiä  . . tal  'dim  Aan^nl{sd.)  äasä  aspa  arinavattjs (sd.)  ..hyat  m5i ..  aj/hai/r {sd.)  \.44-i&;
20570:•  g.  mizda'vant-  Adj.  'mit  dem  (gebühren- den) Lohn  (in  beiderlei  Sinn,  Lohn  tind Strafe)  versehen':  hyat  da  syaokana  'von (APn.)  yäiä  uxiä  akSm  akäi  vanuAlm asim  vanhaov?  "wie  du  den  Taten  ihren Lohn  bestimmtest''  und  den  Worten,  das böse  Los  dem  Bösen,  das  gute  dem  Guten"
30412:humizda-
30445:•  j.  hu-mizda-  Adj.  (fem.  'da-)  'schönen, guten  Lohn  bringend ,  eintragend' :  tä (nämL^aSi)  nS  buyan  °da  aijniidä  a^.-
=== BRT maesa ===
5378:Komp.:  'me  (LS.)-)-3*arf.,  S  368.  48,  —  Vgl. armaesad-.
=== PHD ===
PHD.txt:380:gawazn [gw’sn' | N ~] deer. gawdar [0011 | N ~] calf. ģāw-dumb [g'bdwmb | N —dum] horn, trumpet. ģāw-mēš [TWR Amyš | N gā(w)mēš] buffalo. £áy-, v. ģādan. Gayómart [g”ywkmlt! = Av. gayó marata | (M gyhmwrd), N ~] the First Man. gaz [gc | N ~] tamarisk. gaz-, —išn, v. gazidan. gazag [gc’k'] biting. ģāzar [g'cl | N gázur] fuller, washerman. £azdum [gcdwm | N každum!] scorpion; astr. Scorpio. £azidag [ezytk! | N gazid] poll-tax. gazidan, gaz- [gc-, gz-ytn! | N ~] bite, sting. ~išn: biting. gëg [gdk' | M gyyg] thief. gēhān [gy)?>n! | = M, N gihān, jahān] world. ~ig [-yk'] worldly, mortal. -ģēn [-k(y)n! | M -gyn, N -gin] suffix forming adjectives of quality. gês [гуз | (M gyswg, N gēsū)] curls, locks. £étig [gytyk, gytydy | M gytyg, N géti] 1. the material world; 2. worldly. ~ig [-yk'] worldly. gil [ТУМА < A tym; gl | N ~] clay. gilag [g(y)lk! | N gila] complaint, lamentation. —-Obàr [wp] swallowing complaint, suffering in silence. ģilēn [T YN Ayn! | N gilin] (made of) clay. gilistag [g/ystk!] home, dwelling of demons. gir-, ~iSnig, v. griftan. gird [git! | M gyrd, N ~] round, circular; gathered. (9) — āmadan: gather, collect (intr.). — kardan: gather, collect (tr.). ~ih: roundness. girdag [gitk' | N ~a] disk, round. gisnag [gink' | P gyfng] short, small. ģišnīz [ginyc | N —] coriander. giyā(h) [gy^h, gy^h | (M gy'w), N ~] grass. ~izag [-yck'] a straw, blade of grass. gizistag [gcystk' | J w/Bzsth] accursed, hateful. gogird [оо | M gwgyrd, N ~] sulphur. ~ӧтапа [-’wmnd] sulphurous. gohr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage. goóhrag [gwhlk'] = göhr. ~-danag [-d^m k!] physicist. 1g6hrig [gwhlyk'] natural, essential. *ģūhrīg [gw(’)hlyk'] equivalent, substitute, indemnity,
PHD.txt:487:mēšaģ [myšk!] urine.
PHD.txt:488:mēš-sār [туї | N ~] having a sheep’s head (ornament).
PHD.txt:491:méx [myh | P myx, N ~] peg, nail. ~ ī gàh: astr. Polaris, pole star. 1-3méz-, v. mézidan, mëzišn, mistan. mēzd [my()zd | № тёз] offering, meal. „bān [-p’n' | N ~] host. mézidan, 'méz- [myc-ytn!] suck. *mézisn [myckn'] blinking, twinkling. mih [mt!] false, contrary, opposite. mihēxt [mytwht!] falsehood. imihr [mtr! | M myhr, N —] Mithra; sun; cal. 7th month; 16th day. tmihr [mtr!, etc.] contract, bond. šmihr [mtr!, etc.] love, friendship. mihrbān [mtr'p?n! | Р myhrb’n, N ~] friendly, kind. mihr-dróz [mtr'dhwc] = mihródruj. mihródruj [mtr?w-, mtrwk-diwe = Av. mitlyo.drujim] contract-breaker. ~th: breaking faith. mihr-zan [mtr'zn'] = mihródruj. mij(ag) [myc(k') | N muz(a)] eyelid; eyelash. mijüg (myc-, myšwk! | IN mizü] lentil. mir-, v. murdan. mistan, 3mëz- [mstn', myc- | N mézidan] urinate. -i$n(ih): urination. mizag [m(y)ck! | N maza] taste. ~darih [-d’lyh] (sense of) taste. ~ӧтапа [отпа] tasty. mizd [m(y)zd | N muzd] reward, hire, pay. ~war [-wbl | N -àr] hireling. *mizné [m(y)znydy] mist, dew. mög [mwk!] shoe. 5 *moy-mard [mgw-mit', -gGBRA | N muy) magus. mör [mwl | N <) ant. mórd [mwlt! | N ~] myrtle. morwārīd [mwlw'lyt! | M mwrwryd, N ~] pearl. *mowbed [mgwpt' | N móbad] Mazdean priest. móy [mwd | N ~] hair. móya$ [mwdk' | N méya] lamentation. móyen [mwdyn'] (made of) hair. moz [mwe | N ~] banana. mózag [mzvck! | N тоха] shoe. *mūdag [mwtk'} spoilt, destroyed. muy [DKRA < А dgP | N mux] date-palm. muhr [muwdl | M mwhr, N ~] seal. Сар [mwhlk! | P mwhrg, N ~a] bead, vertebra, piece (in backgammon, etc.). *muhrišn [*mwtl$n!] excrement. mulān [mwi?n'] belly (daevic).
PHD.txt:518:6 [OL < А Ч; ?w | M ’w] to, at; v. also 6h. ~ gird ámadan: gather, collect (intr.). — ham kardan: gather (tr.). ~ ham madan: gather (¿ntr.); come to an end. *óbad-, v. bastan, *óftadan. Obārdan, bär- Dwf?l-tn! | M ?wb’rd] swallow, devour. Obastan, *dbad- [NPLWN-stn! < A У npl; ^wpstn!, ^wpt- (if not Oft-, q.v.) | M ?wbyst, J ^wfst-] fall. *oftadan, Oft- Pwpt- | M *wpt'd, N uft~] fall. Gear Pwk’l] ebb. ogardan, ógàr- Pwk’l-tn'] remove, expel. *брга ['wgPy] declination, dip. Sh [KN < A kn | Mwh] so, thus; (with verbs, giving a sense of uncertainty) may, perhaps. Ohrmazd Pwhrmgd | M ^whrm(y)zd, N Hórmuzd] Ahura Mazda; astr. Jupiter; cal. 1st day of the month. -om [-wm | = M, N ~] suffix forming ordinal numbers from panjom onwards. -mand [-’wmnd | M -wmnd, N -mand] suffix forming adjectives of quality. *óréb(ih) [wlyp(yh)] disappointment. Dron ['cwlwn! | Mwrwn] hither. ад... ~: since. osán- Pws*n- | = M] throw down. óspurdan, ӧѕраг- [”zospl-tn!] tread, trample. 051°, v. awest^. Ost [220511] firm, reliable. ostigàn Pwstyk’n! | M Iwstyg^n, N ustuwàn?] firm, strong, sure, reliable. ~ih: reliability. lēš [wf | = M, N Ads] consciousness, intelligence. mih: = 68. 268 [wf | = M] death.
PHD.txt:659:хак [APLA < А ‘pr’; Pk! | N <] earth, dust. хат [/?m | N ~] crude, raw. xāmīz [h’myc | N ~] pickled meat. xāmēš [/4mwš | N ~] silent. ixān [/?z! | P æn, N ~] house. ~ ud man: house and home, dwelling.
PHD.txt:4688:frahixtan frahixtag frayádisnig fravādišn frāy frādahišnīh frahist farroxīh farrox lxwah-I xwastant frārāst frārūnīh frārēn frāmēš frūmēš- frāmuštan frahist parrag frch pardāxtan frehbūdīh frehbūd pardāz-
PHD_mackenzie.txt:3578:mizd [m(y)zd IN muzd] reward, hire, pay.
PHD_mackenzie.txt:3846:Ohrmazd [)whrm:;:d I M )whrm(y)zd, N H6rmuzd] Ahura Mazda: astr.
```


## [2026-09-07T17:39:10.195Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npos=t.find(\"muzd, muzd 'Lohn\")\nif pos<0:\n    pos=t.find(\"978. muzd\")\nleaf=t.count('\\f',0,pos)\nprint('muzd leaf',leaf,'printed page',leaf-21)\nprint(t[pos-300:pos+900])\nEOF"
}
```


## [2026-09-07T17:39:10.347Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"mêš\\|mSš\\|mîš\\|1017\\|Widder\" HRN.txt | head -20"
}
```


### [2026-09-07T17:39:11.453Z] TOOL RESULT

```
muzd leaf 240 printed page 219
arißh 'Tod';
arm. vergl. waÄ, warA 'Tod' (H. No. 185).
kurd. merk 'Tod'; bei. mark; oss. d. t. marg *Gift'
(178 e).
Der Bedeutungswechsel im Ossetischen könnte als
ein Analogen vielleicht auch die Ableitung von np. mar
Schlange' aus l^mar^ sterben* bezw. deren Causativs
*tödten' rechtfertigen.
978. muzd, muzd 'Lohn, Preis', muzde {mizde) 'frohe Bot-
schaft'.
aw. mUda- 'Lohn'; phlv. m(i)zd (paz. mozd), mtizd
(AV.); ai. midhd- 'Kampf, Wettkampf; got. mizdö
'Lohn'.
oss. d. mizd, t. m^izd 'Bezahlung, Vergeltung, Lohn,
•Belohnung' (188).
Das u im Neupersischen ist auffällig.
979. me^^yiden saugen, schmecken', meze 'Wohlgeschmack',
meklden.
g. meöcLdmün\ Käs. Q. hdmij, K. bemüj, 7j, oermez;
Q. mitSn, K. vermSt {*mi/ten),
phlv. micUan (Bund.), midak 'Wohlgeschmack (Men.);
kurd, mltin^imlßim 'saugen'; bei. micagj n. misay 'saugen'
(235).
Von einer l^meq/c- 'saugen*.
980. miSe, muze 'Augenwimper, HJD (Jer. 9, 18).
g. müjeng; Käs. mejd, mujd^ mezL— 220 —
kurd. miMnk, mizl, mujüal (H.-Sch.) ^Augenwimpern';
bei. micäc, n. misäs ^Augenwimpern*, daneben LW.
mizayän (236).
ai. nimis' 'Blinzeln, Zwinkern des Auges*, skr. nMsa-,
das Bartholomae ZDMG. 44, 553 vergleicht, stimmt
lautlich nicht zu np
```


### [2026-09-07T17:39:11.495Z] TOOL RESULT

```
2232:ai. ürana- *Widder, Lamm'; phlv. varak', arm. gam
8021:aw. varsni- männlich (Widder)'; phlv. gtisan, vergl.
8022:N. pr. Gusnasp; ai. vfsni^ 'Widder*.
8176:942. göspendj gösfend 'Kleinvieh, Schaaf, Widder, Ziege'.
8772:1008. meS 'Schaaf, Widder.
8837:1017. näi^uk 'zierlich, lieblich, zart', näz 'Freude, Ver-
13104:f(^«'*/^ 1017.
13117:>iä^! 1017.
13121:näziden 1017.
13122:näzuln 1017.
13123:iiäzuk 1017.
16457:»aci'k 1017.
18624:K. nac 1017.
18627:K. rtakh- 1017.
18979:1017.
19455:näzik 1017.
19914:näzak 1017.
19915:ng;(2;aA;a 1017.
20597:n. näzttk 1017
20598:j «äsTMrÄ: 1017.
```


## [2026-09-07T17:39:19.420Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npos=t.find(\"1008. meS 'Schaaf\")\nleaf=t.count('\\f',0,pos)\nprint('leaf',leaf,'printed page',leaf-21)\nprint(t[pos-200:pos+700])\nEOF"
}
```


## [2026-09-07T17:39:19.766Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD myzd ===\"; grep -n \"myzd\" SOD_pages.txt | head -20"
}
```


### [2026-09-07T17:39:20.667Z] TOOL RESULT

```
leaf 247 printed page 226
, auch
kimtz, kumlz *Urin', ginnzlden harnen' (aw. gaomaeza-y
phlv. gcmez, arm. LW. gomez-)) sind sämmtlich
unbelegt.
1007. meyezd *Gelage\
aw. myazda- ^Opfermahl'; phlv. myazd, myäzil;
ai. miyidha-.
1008. meS 'Schaaf, Widder.
aw. maesct' *Schaaf, Schaafbock'; phlv. mes; ai.
mesd',
kurd. mt^ miya; af/. m^y 'Mutterschaaf, LW. mes
'Büffel'; bei. mes (240); wa;t'- w^*> sar. mdo^ mdul,
siyn. may, mdyij.
1009. mey *Wolke .
aw. maf.ya- *Wolke'; phlv. mey ^ vd. 15 (18); ai.
meghä-; arm. m^g 'Nebel* (H. No. 197).
oss. d. meyä, t. 7nty *Nebel, Wolke' (185).
Dass mey mit l^meig^h- 'harnen' (1006) zusammen
gehört, scheint sicher zu sein, vergl. zuletzt Bechtel,
Hauptprobleme S. 373.
') Das l Hesse sich allerdings als Ablaut erklären.
') Seifenkraut; Ochsenurin.— 227 —
1010. vfieig 'Heuschrecke, ^''^D (Is. 33, 4).
aw. madaxa- 'Heuschrecke' (D armestet er, Et. ir.
n, 197); phlv. waig (kaum madag),
b
```


### [2026-09-07T17:39:20.711Z] TOOL RESULT

```
=== SOD myzd ===
10880:     Pam-Pay- ©Parth. Wmyzd                                      load
19979: 5675 myzd S                       *                             big,
```


## [2026-09-07T17:39:28.060Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor i,l in enumerate(lines):\n    if 'myzd' in l:\n        print('LINE',i+1)\n        print('\\n'.join(lines[max(0,i-6):i+8]))\n        # leaf\n        pos=sum(len(x)+1 for x in lines[:i])\n        leaf=t.count('\\f',0,pos)\n        print('>>> leaf',leaf,'printed page ~',leaf-66)\n        print('---')\nEOF"
}
```


### [2026-09-07T17:39:29.333Z] TOOL RESULT

```
LINE 10880
                                                                 (to)tremble
                                                                 VJ 1001; GMS 576
2456 p>m>y ^ p>m>k
                                                            2469 pV B, S                                            j,
2457 p^Pyyy      M   jUm^ j/ ^Ji) J jJt jU^ oU^jj ^Ua-
                                                                 par ©Yaghn. vor
     Pam-Pay- ©Parth. Wmyzd                                      load
     Great Builder, Builderforte of the Manichaean               SCE 341;MDii;MSP bl05

       god)W-Lii                                            2470 p>r2 B                                     -j'j-o'j-
     BBB;
                                                                 par (L*p»r) ^P^k
                                                                                                                                 98

>>> leaf 162 printed page ~ 96
---
LINE 19979
 5674 myz>y S, B                                      V
      meze ©Av. maez\ MP /mz                                5684 mz'yx   B =* mz'yYOO
      urine                                                5685 mz'yxch S                              ^cJ'jj
                                                                mazexc/k (mz'yxk) ©f. -ch\ m. -k; adj.
      Hen. BSOAS 1946, 718, TSP 2.299, myn>y ; S W,               ^mz^YCh)
        BSOAS 1991, 490
 5675 myzd S                       *                             big,
                                                                 Anc. old
                                                                       Lett. 2.40, 2.53; GMS 396, 976
      mizd ? ©Av. mizda
      salary, reward                                       5686 mz'yxk =** mz'yxch
                                                           5687 mz'yxy'k S                                      J ,y
      Anc. Lett. 248, 49; Bailey. Prolexis. 280
                                                                 mazexyak ^mzyxy*
>>> leaf 293 printed page ~ 227
---
```


## [2026-09-07T17:39:37.080Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && head -3 BQT_v4_pages.txt; echo ...; python3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\nprint('nblocks',len(blocks))\nfor i,b in enumerate(blocks[:3]):\n    print(i, b[:120].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T17:39:38.382Z] TOOL RESULT

```
[pdf page 1]
[pdf page 2]
ه
...
nblocks 553
0 [pdf page 1] 
1 [pdf page 2] ه و سم ۰ و الب اس ی 9 ۱ عه ر جر ن‌خلف بربری لیر رها ّف‌بال ۱۰۶۲ #کک . ناس مد ی «چا لد ولوح ا! ۰ ً ّ ۰ ,7 اس
2 [pdf page 3] اداره کل نکا زشن" ساره ۰۱/۹/) ‎٩۰9‏ ی ثاریم موم : ار ۴ رِ وزارت میت د انشمند محتر ‏ آقای د کتوحمد معین‌استا
```


## [2026-09-07T17:39:41.720Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\nfor target in (83,84,82,161,162,160):\n    b=blocks[target-1] if target-1 < len(blocks) else ''\n    print('=== pdf',target,'printed',target+1917,'len',len(b))\n    print(b[:1500])\n    print()\nEOF"
}
```


### [2026-09-07T17:39:43.085Z] TOOL RESULT

```
=== pdf 83 printed 2000 len 2265
[pdf page 83]
مزاح کوهران هم
میگویند ۱ بدام نیفتد بمد از آن همه خلاس شوند و حالت
مزاج ۲ گوهران <کنایه‌ازمناسر | اولدست دهد. واین بازی‌را عربان تدمیح با دال
اریمه است که خاك وآب وهوا وآتش باشد ۴ ؛ | بی نقطه بر وزن تفتیح خوانند - و هم دراعربی
و با زای فارسی هم بنظرآمده است . بمعنی زباده کردن قیمت چیزی باشد مثلآنکه
مزاج وی دکنایه ازخوشامدگوی قیمت آن چیز بده دیثار رسیده باشد دیگری
با ۴ بدوازده دیثار پرساند و همچنین 8 .
از بازی باشد و آن چنان است که دو کس در ابید » اجرت کار کردن باشد ام از لیا
براپربکدیگرخم شده بایستند وسرپرسر هم نهند | 2 و پا .
واسر رسماای بردست گیرند وابیکس دیگرآن مزدبر اس اول وسکون ثامی‌ودال
ربسمان را شخصی بر دست گیرد و بردور و پیش | بی نقطه و افتح بای ابجد و سکون رای قرشت.
ابغان میگردد و لمیگذار دک ه کسی برایشان‌سوار | بمعنی مزدور باشد وآنرا هزذبره و هزده-
شود وبرپشت‌ایشان نشیند. وشخصیر !که محافظت | ار نیز گوبند .
یشان میکند خربندهء گوبند . چون آن شخص مزد دندات - بنم اول, بممنی دندان
پا خود را برهريك از حربفان بزند اورا بیاورد | مزد است وآن زری باشد که چون فقرا و مردم
ویجای آن دوکی بازدارد. و همچنین محافظت | نامراد را بمهمانی آورند مبلغی بقدر آنچه خرچ
آن ي كکس میکند تا دیگری پا خورد و آمده | طعام و شراب ایشان شده باشد بند از خوردن
سربرسر شخص اول نهد و اگر احیاناً شخصی از | اطمام بایشان‌قسمت کنند. واین رسم‌درقدیم‌متمارف
حربفها برآها سوار شود فرود نمیاید تادیگری | بوده .
۱ - ر4 : اقرب الموارد » هنتهی الارب . ۴ - (عر ) بکر اول همزوج شدن
«آمیختن -کیفیتی در بدن که از آمیزش عناصر و اجزای اسیله پیدا میشود « فرهنگه نظام >.
۴ -ظ . بمعنی اختلاط و امتزاج عناصراست . نظامی

=== pdf 84 printed 2001 len 2382
[pdf page 84]
سر مزکت
مزدقان - با قاف بر وزن یهلوان » نام | کننده که از کندم و گاوری وجومازند و بعربی
شهربست در قغستان ؛ و با زای فارسی هم هست. | انبین خوانند .
واسح‌آن است ۱ .* مزرعة خاك - کنابه آززمین است
مزدود ؟ - بر وزن پرزور » بمعمی - وکالید و جد ادان و حیوانات دیگر را هم
شاکرد باشد - ومزدیر را نیز کوبند بمنی‌شخسی | گفته‌اند - وقبروگوررا نیز گویند که محل دفن
که‌کار بکند واجرت بگیرد ۳ . گردن انان باشد .
مزدور دیو- رمزدوردیوان- مزرعه دانه سوز -کنایه از دیا
شخصی را کوبند که‌کارهای لایعنی کند که در آن وعالم است . ۱
نه فایده دنیا و ته نفع آخرت بجعت او باشد مزده - بروزن اکره . بممنی‌چراغدان
و اینچنین شخصیر! هیزم کش دوزخ دی زکویند باشد؛ وباین ممنی‌بتقدیم رای بی‌نقطه هم گفته‌اند
وعاملان و متصدبان دبوانیرا هم گفته‌اند . که بروزن هرزه باشد ‎٩‏ .
مزده بر ۴ « با بای ابجد پروزن مهره مزگ « بفتح اول وسکون ثانی وکاف
کی » بممنی مزدور باشد وعربان اجیرگویند.* | فارمی, درخت بادام تلخ است و معرب آن مزج
زد * - بنتح اول وسکون ثانی*ورای | باشد ۷ .
قرشت » بوزه را کوبند و آن چیزیت مت هز کت ۸ - بنتح اول وکسکاف فارسی

۱- « مزدقان ( بفتح اول و سوم ) شه رکیست ازلواحی ری و معروقت و آن بین ری
و ساوه است - و مزدقان شهری است كوچك از شهرهای قپستان . » * ممجم البلدان » - و نام
رودخانه ات که از ساوه کذرد . « نزهةالقلوب . مقالةٌ الئه طبع بریل ۱۳۳۱ ص ۹۲ . رل :
مژدقان . ۴ - از: مزد۳-ور ( پوند اتصاف ودارندکی) < بر ( بردن ) [ قی: کنجور,
رنجور ] ۳ مزدیر («.م.). پپلوی832200087 « یونکرص۱۱۷ > کردیع 3۵20-۷67 « ژابا
س ۳۹۷ ۰ 7712011 ( متخدم )« ژابا س ۳۹۷ . رك : دارمتتر . تتبعات ج ۱ ۲۹۲ -

۴ - ر4 : مزدبر . ۴ - رل : مزدی

=== pdf 82 printed 1999 len 2086
[pdf page 82]
-۱۹۹۹- هز
و در عربی پا تشدید ثانی ۰ ارکی را کویند که | مریح ذلب‌فعل زحل سیما هم میگویند.
گذرگاه آب و نان است ۱ - و بضم اول:آنکه مریخ زحل‌خو اد -کنابه ازآش
نوبت خود را در شراب خوردن بدبگری ایثار | انگشت وزغال‌است‌بمنی‌زغالی که اخگرشده باشد
کند - و در عربی با تشدید انالی » آبکامه را | نه چوب وهیزم ‏
گوبند و آن خورشی است مشهور خصوصاً در مریخ سلب - بفتح سین بی‌نقطه ولام
سفاهان ۴ . و سکون بای ابجد , کنایه از لبلی سرخ است-

مریافلن ۴ « جنم اول وسکون نانی | وسرخ پوش: را نیز کوبند .
و تحتانی بال فکشیده وکسر فا ولام مضموم بنون مریخ و کیوان دیدن «کنابه از
زد » لفتی است بونانی و ممنی آن‌بمربی ذوالف | انگشت و زغال نیم سوخته در منقل دیدن باشد.
ورقه باشد » ون پیخکیاهیست که از شام وبیت مری ز بافات - بنم اودونانی بتحتانی
المقدسآورند وآنرا حز ببل‌نیز کویند. کزن کی رسیده وقتح زای تقطه‌دار وپای ابجد پالف کفید.
مار وعقرب را نافع است . و نون مفتوح بکاف زده . نام دوائی است که
مرخ -بکر اول . نام کوکبی است تخم آن رابار تنگه خوانند و خوب کلان همان
ازجملة سبعةٌ سیاره ودرآسمان پنعم میباشد۴ - | است ‎٩‏ .
و کنایه از انگشت و زغال افروخته است ‎٩‏ - مر یشم - بنتح اول و نانی به نحتانی
.وباسطلاح اهل صنمت که کیمیاکران باشندآهن | مجهول کشيده وشین نقطه‌دار مضموم بمیم زده »
وفولاد - خسته بندرا کویند وآن چیزی‌باشد که برجراحت
هریخ آفقاب علم - کنابه از آش بندند ۷ .
شمله‌ناك است ۰ مریم و2 - باعین بی نقطه و ولو
مریح "ذنب فعل < کنابه از حلقة | ورای قرغت .کنایه از شاخ درخت انگور است
زنجیر است که بر پای, ستوران گذارند وآن را | در ایام خزان و برکك ریزان .
بیان دوازدهم
درمیم با زای نقطه‌دار مشتمل بربست وشش لف

=== pdf 161 printed 2078 len 2277
[pdf page 161]
می. نقطه . بلفت سربانی نام درختی است بز رکه | واشین قطه‌دار بالف کیفء , نام کیاهی است که
که نس و میوة آترا آنرا بعریی (۱) حی‌العالم کوبند و آن لوعی از
پیودنی لوطوی‌خوانند. ار ۹6| رباحین است و هیده سبز می‌باشد . اکن باییه
و ب ی کوبند لوطوی 0/7 4هر۷8۵ | کهنه قدری از آن بکوبند و بر خنازین ضماد
بام‌هماندرخت است ‎۰٩‏ لا ی کنند تحلیل دهد وآن را میشا یی ب ز کوبند
میستی ۲ - پجها ۹ | که بروزن زیبایی(۷) باشد ‏
با ثابی مجهول بروزن ۳ ر ۸ میش بهار * - نم کلی استکه‌آنرا
یستی » بمعنی پیستی 3 کل گاز چشم میگوبند و در فضل بهار ظاهرشود
باشد وآآنیملتی‌است که وم ومسهل بلغم وسودا باشد وسنگهکوده راپریزاند؟
پزبان عریی برس کویند ؛ و بط ی کویند پیستی | وبسنی کوبند نوعی‌ازرباحین است وآدرا حی‌المالم
بمعنی‌جذامیست پمنی‌شخص ی که علت جذام داشته | خوانند - و بممنی ابرهم‌هست که عربان سحاب
باشد . کوبند . :
هی‌سوسن ؟* - بکسر نانی ‏ شربت ميشته ۱ - بکسراول وفتح تای قرشت,
سوسن راکوبند 8۰ مملم جهودان راگوبند ۰
هیشا ؟ - با اول .بتانی مجهول رسیده می شعری‌فش» کنایه از شراب
(۷) چش : - جربی . (۷) چش : میشالی ... زیببالی +
۱- رك : لوطوی . ۲ -ظ . مصحف « پیستی » « رشیدی > ( رك : پیست ) پا
مسحف 3 پسه» (هم.) ۴ - معرب‌آن « میسوسن » ( بفتح اول وضم سوم وافتح پنجم).
رك : دزی ج ۲ ص ۲:۹۲۹ . این کلمه فارسی است: می ۳ شراب» وسوسن ۳ 19[ ۰ وآن شربتی
است مرکب که نغيةٌ آن مشکل وتوسط ابن‌جزله ( منهاج : شراب السوسن ) بتفسیل شرح‌داده
شده است. ر4: عقار ۲4۷ ف - ۴ - رشیدی کوید : « ظاهراً مخفف همیغا باشد. , چه او
را همیشه بهار نی زگوبند » » ی : میش بهار . 8 -اظ . مخفف « همیشه بهار »۰ معرب
آن « میشبهار» < 5680061۲۷1۷۱۵0 این‌کلمه 

=== pdf 162 printed 2079 len 2208
[pdf page 162]
سا خ میا میکد
انگوری لملی باشد . میگزد * - با اول بتحتای رسیده
میش مرغ- بیکمراول وسکون ثانی وکان فارسی مفتوح بزای تقطله‌دار و دال مرا
ثاله ۰ پرسایست آبی و کبود رنکهکه آنرا زده» بمعنی‌میزد باشد(۱) که مجلس وبزم شراب
0 نیمه 7 | وهی و عفرتگاه ومپمانی باشد - و مهمانغاندٌ
خرچال کوبند ۱ #۰ آکابر وسلاطین را نیز کوبند ؛ و بغتح اول وکا
میغ ۴ - با تانی مجهول پروزن تیغ ۰ | فارسی هم کفته‌اند -
بغاربرا گوبند قیره و ملاسق زمین - و بمعنی | هیگمسار ۱ « ینمی شراب خوار ۷ چه
ابر.هم‌آمده است که عربان سحاب خوانند ۴ ۰ | کارون بمعتی خوردن شراب باشد لایر .
میگ ۴ - بفتح اول و اسکون:ننانی میک ۸ - بنتم اول و کان قارسی
و کاف فارسی » ملخ را کویند که بعریی جراد | وسکون نانی وکاف تازی » بمعنی‌میگه باش د که
خوانند . ملخ است - وتصغیر میگه‌هم هت پمنی ملخك.
(۷) چش : است .
۱ -ر4 : خرچال . ۴ - اوستا -3386802 (ابر) » پپلوی 136810 » هندی
باستان -1336810۸8 » آرمنی 3368 (مه) . استی ۳۸82 ۰ ۳1810 (مه » ابر ). اینکه «میغ»
با ره 128180 ( ادرارکردن ) همریشه باشد , قطعی بنظن میرسد « اسشق ۱۳*۹ .
۴ - « میغ » ابربود » فردوسی ( طوسی ) کفت :
همانا که پاران نبارد ز میغ فزون زانکه پارید پرسرش تیخ.»
« لفت فرسی ۰۲۸۴
۴ - ۳288 ميکك (ءم.) . اکنون در سواحل خلیج فارس نوعی از علخ را «میگو»
کوبند , وآن متعلق بزبان پارمی‌اخص - یمنی‌لهجهٌ جنوب غربی. است ودراصل ۰0733202۳2
2ازط ده بوده است . رك : ص هیجده ازمقدمهٌ کتاب حاض . هوبشمان کوید : میگه فارسی
*پارسی باستان -62ا5724 ( ۳ اوستا 0۳201182 ) فی: ۰0218 کلم ارمنی 7۳82۳876
مستعاراست. ولفت اشکانی- پارسی»1382 13324 متعلق است متقیماً بكلمةٌ اوستایی 222412252
«هوبشمان ۱۶۱۰ ۰ پپلری 33

=== pdf 160 printed 2077 len 2305
[pdf page 160]
پات اسم
و مهما ی کند ۱ - و هیز بانی ۲ خدمت | هیچ چیز شواند خوردن و مٍل هیچ چیزسداشته
مهمان کردن ومهمانداری نمودن ومهمانی باشد. | باشد ‎٩‏ .
هیز د - بفتح اول و انی وسکون نا میزد * - بنتح اول بر وزن قیصر ء
و دال ابجد . بمعنی مجلس شراب و بزم عشرت دستار و مندیلی راکوبن د که برس بندند -
و مهمانی باغد ۴ ؛ ویکسر اول وفتح زای هوز میز لك - با نالی مجهول بروزن نیز ۰
یزاین معنی است که بزم شراب باشد - ویکر | بول وشاش راکویند - و مصفر بول و اشاشی هم
اول و ثانی مجپول » پعتی بشاشد و بول کند | هت ۸ .
چه میز بمعنی شاش و میزیدن بمعنی شاشیدن هیژه * بر وزن ربزه » میان زین اسب
باعد ۴ . را کوبند که خانهٌ زین باشد . ۰
هیزده ‎٩‏ - بنتح اول و ناك + غراب میزیدن ‎٩‏ - باتانی مجپول بر وزن
زده راکویند وآن شخصی اس ت که ببب بیار پچیدن » بمعنی بول کردن وشاشیدن باغد *9.
خوردن شراب بد حال ومی‌مزه باشد بمرتبه‌ا ی که میس ۱۱ بفتح اول وسکون ثانی وسین
۱- او میهمان من بد ومن میزبان او مهمان نت و خوان ببر میزبان تهاد
رسمی‌است خوان وکاسه نهادن ز میزبان آن روزخوان وکاسه همی میهمان‌نهاد.
معزی نیشایوری ص ۱۸۵ ۰۴

۴ - از : میزبان ۳ ی ( حاصل مصدر , اسم معنی ) ۳ میزوانی. رك: تذکرة الاولیاه
چاپ آروپا ج ۱ ص ۹۰ ی ۱۳ وس ۳۲۸ ۱4 وارك : قهرست ولف .

۴ - اوستا - 83322042 (طمام فدیه وقربانی) » پهلوی 23824 ۰ 129220 . هندی
باستان - 2161102 « اسشق ۱۳۰۷ > و رك : هوبشمان ۱۶*۷ . در اوستا « میزده » عبلرت از
نذر و تقدیمی غیر مایع و فدیه , چیزی خوردنی در مقابل نذر مایم وآشامیدیی ( که این وا در
اوستایی 22018072 و در پهلوی 2012۳ و در فارسی « ژور » ( بفتح اول ) کوبند ۶۰ خرده اوستا
۲۲۸ ح > ورك : بشتها اص ۳۳۹ سنا ۲۸ ۰ ۱۳۱۱۱۲۵ :

ای
```


## [2026-09-07T17:40:00.645Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\nimport re\nfor w in ['مژده','مژدگانی','گاومیش','مژد']:\n    print('===',w)\n    for i,b in enumerate(blocks):\n        if w in b:\n            print('  pdf',i,'printed',i+1917 if i>0 else '?', '| count',b.count(w))\nEOF"
}
```


### [2026-09-07T17:40:02.254Z] TOOL RESULT

```
=== مژده
  pdf 65 printed 1982 | count 1
  pdf 87 printed 2004 | count 5
  pdf 266 printed 2183 | count 1
  pdf 276 printed 2193 | count 1
  pdf 285 printed 2202 | count 1
=== مژدگانی
  pdf 87 printed 2004 | count 1
  pdf 163 printed 2080 | count 1
=== گاومیش
=== مژد
  pdf 65 printed 1982 | count 1
  pdf 82 printed 1999 | count 1
  pdf 83 printed 2000 | count 1
  pdf 85 printed 2002 | count 1
  pdf 87 printed 2004 | count 10
  pdf 163 printed 2080 | count 1
  pdf 261 printed 2178 | count 2
  pdf 266 printed 2183 | count 1
  pdf 268 printed 2185 | count 1
  pdf 276 printed 2193 | count 2
  pdf 284 printed 2201 | count 2
  pdf 285 printed 2202 | count 1
  pdf 291 printed 2208 | count 1
```


## [2026-09-07T17:40:17.186Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\nprint('=== block87 (pdf88, printed 2005) ===')\nprint(blocks[87])\nEOF"
}
```


### [2026-09-07T17:40:18.597Z] TOOL RESULT

```
=== block87 (pdf88, printed 2005) ===
[pdf page 88]
- وم مزو

تمامی بود اورا نیز این مذهب خوش‌آمده متابع | کهموی پلك چشم باشد یمنی مژه‌هاء ومفرد هم

او شد و بدوگروید و این مذهب را رواج داد | استعمال میکنند و جم اول آمده است.
ن انوشیروان شاه شد اورا باهشتاد هزار

اس 0 پا د هزارکی مزهژ » بکر هردو میم وسکون:هردو
تابع او بودند بقتل آورد ؛ و در مویدالفضلا | بر . باشد که چون بر گوشت نشب

پم اول وسکون زای هوز هم آمده‌است . .| زای فارسی,مگی باشد که چون بر گوشت شیند
و داز ۱ 1 | کوشت را بد بوی و کنده سازد و کرم در آن
مژد الی * - با کاف فارسی بروزت | .. پ.

کته دا ۹ ۰ افتد ‎٩‏ - و خرمگی را دز مرمرژ میگوین دکه
دالی » بمعنی لوید و بشارت و مژده باشد مگ بزرکه باء

که خبرخوش است - و چیزی را نیز کوین د که بزر که باشد .

بآورندة مژده دهند ۴ . مژزنگ. بروزن پلنکه, بمعثی ناخوشی
مژده * < بنم اول وفتح ثالت. بعارت | و زشتی باشد ۷ - وحیز ومخنت را لیز کوبند.

و خبرخوش و نوید باشد۴ - وشادی وخوشحالی ها « بکر اول وثانی بواو کشیده .

را نی ز کویند ؛ و بکس اول هم آمده است. علفی راکوبند که حمامیان سوزند وعربان شری
هژگان « بکر اول وتح نانی وکاف | خوانند - و مرجمك را نیز کفته اند که عدس

فارسی‌بالف کشیده وبنون زده » جمع مژء‌است 8 | باشد ۸ -

۱- دارستر ( جبعات ج اص ۲۷۲ ح ۱) مژدکانی را ماش زندگانی ( مرکب از:
مژدگان جمع مژده + ی اسم معنی ( حاصل مصدر ) دانسته است . فقس : کردی 10128810
( خبن خوش ؛ انعام که پآورندع خبر خوش دهند ) « ژابا ضس ۰۳۹۷

۴ - مژدگانی بده ای خلوتی‌نافه گشای1 که زسحرای ختن آهوی مشکین‌آمد.

« حافظ شیرازی صس ۱۱۹ *.

۴ - هرن « اسفق ۹۷۸ > مژده و مد ( جنم میم ) را همرشه مزد ( چتم میم ) داند-
رك : مزد ؛ اورامانی 330212018 « 4 . اورامان ۱۷۶ *. ۴ - « فی‌الجمله بانواع عقوبت
گرفتار آمدم تا این هفته که مژدة سلامت حجاج برسید از بند گرام خلاس کرد ( ملك ) >
«کگلتان س ۳۸ . - ر3 : مژه .کردی ۳01828 ( جمع 82[ [ مژه ] )
« ژابااس ۳۹۷ :
تا دیدم ثیر مژکاش . نداست م که هت تبغ عشق و تیرهجرش در دل وجان کارگر.

« معزی لیشاپوری ص ۰۳۲۷

‎٩‏ - بتر کی کونکاون گویند « جهانگیری » . ۷ - در جهالگیری و رشیدی این
بیت فرخی را شاهد آورده‌اند :
همه آراستةٌ جنگه و فزایندة کین روز گاری(روزی خود) بخوشی‌خورده وناخورده مژنگه.
ولی در دیوان چاپ ,عبدالرسولی (ص ۲۰۷ ) « ناخورده شرنگه >آمده است .

‏۸ «<مرجو * مرجمك * مرجومك . در مقدمة الادب زمخشری (ص ۱4) « عدص .
برسنگه. مژو >.
```


## [2026-09-07T17:40:27.665Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\nfor i in (159,160,161):\n    b=blocks[i]\n    print('=== block',i,'pdf',i+1,'printed',i+1918,'===')\n    for ln in b.split('\\n'):\n        if 'میش' in ln or 'مش' in ln:\n            print('   ',ln[:200])\nEOF"
}
```


### [2026-09-07T17:40:28.854Z] TOOL RESULT

```
=== block 159 pdf 160 printed 2077 ===
    هر که صبوحی کند بادل‌خرم بود بادولبمشکیوی» بادو رخ‌خورعین.
=== block 160 pdf 161 printed 2078 ===
    بام‌هماندرخت است ‎۰٩‏ لا ی کنند تحلیل دهد وآن را میشا یی ب ز کوبند
    با ثابی مجهول بروزن ۳ ر ۸ میش بهار * - نم کلی استکه‌آنرا
    (۷) چش : - جربی . (۷) چش : میشالی ... زیببالی +
    است مرکب که نغيةٌ آن مشکل وتوسط ابن‌جزله ( منهاج : شراب السوسن ) بتفسیل شرح‌داده
    را همیشه بهار نی زگوبند » » ی : میش بهار . 8 -اظ . مخفف « همیشه بهار »۰ معرب
    آن « میشبهار» < 5680061۲۷1۷۱۵0 این‌کلمه صورنهای مختلف درخ ابن‌البیطار و پاین‌اسمیت
    2 میشنه , معلم جپودان باشد . عماره (مروزی) کوید :
    چوئین بتی که صفت کردم سرمست پیش میشنه بنشته.»
    میش - بکسر اول ( تلفظ کنونی ) و در تلفظ قدیم 322650 » اوستایی -132868123
    (گاو میش) » بلوچی 93 , وخی 41 . سربکلی 40. ۳ ۹ ان
    تفه ( میش ) « زابااس ۸*۹ ۰۶ نیز کردی « میش > « ژابا میش
=== block 161 pdf 162 printed 2079 ===
    میش مرغ- بیکمراول وسکون ثانی وکان فارسی مفتوح بزای تقطله‌دار و دال مرا
    0 میشنه - رك : هيشته (۱)
    ودرلفت فرس چاپ‌هرن « میشته» آمده » وییت مزبور دررشیدی بدون ذکر نام شاعرچنینآمده +
    دیدم بت ماه روی رعنايك را سرمت به پیش میشته آبنشته.
    ظ . این نام مصحف « مشنا > ( بکس اول ) است که کنابی است بهودان را» وآن در عربی‌دخیل
```


## [2026-09-07T17:40:44.158Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN sheep 3.25 ===\"; grep -n \"3\\.25 *SHEEP\\|3\\.25  SHEEP\\|SHEEP\" SYN.txt | head -10; echo \"=== IEC mizdh/moiso ===\"; grep -n \"mizdh\\|moiso\\|maiso\" IEC.txt | head -10; echo \"=== HUB mizd/mes ===\"; grep -n \"muzd\\|mizd\\|mēš\\|mêš\" HUB.txt | head -10; echo \"=== NYB mizd ===\"; grep -n \"mizd\\|mēš\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-07T17:40:44.258Z] TOOL RESULT

```
=== SYN sheep 3.25 ===
4176:SHEEP RAM Grk. ols, mpéBarov xptés NG mpoparo kptapt Lat. ovis aries It. pecora montone Fr, mouton bélter Sp. carnero, oveja morueco Rum. oave berbec Tr. cdera, 61, cit reithe NIr.  caora : reithe W. dafad hwrdd, maharen Br. darivad maout-laro, -tourc’h Goth. lamb ges ON saudr, fer, smali hritr, vedr (coll.)
=== IEC mizdh/moiso ===
=== HUB mizd/mes ===
2427:Zrvan) die Zeit als Urwesen, dessen S5hne Ormizd
4296:mizd = arm. Ormizd, alter 2J:m,Aramazd --= ai^,A(h)uramazda ;
4345:uneigentliches Eompositum wie Hormizd = A(h)uramazda).lOr
4471:sassanid. Hormizd, arm. Ormizd^ ap. A(h)uramazdd; miyan
4809:micdc; muzd, muzd *Lohn', paz. mazd Min. Gl. 136, phi.
4810:m(i)zd und muzd Gl. and Ind. 213 und 217, afgh. LW. mazd
4811:oder muzd Vages, hire' = zd. mizda-^ ap. ^mizda-, gr.
5210:Anm. 5, ^kr. «;rsa^a^i?a- ; Atr-ormizd (EliSe, Laz. Pharp.)
5857:(Tab. 3, 6), phi. Daraydv, ap. Darayava(h)tis -, Nehormizd
6012:phi. dastuvar; muzdur, afgh. LW. mazdUr =
=== NYB mizd ===
398:āmēcišn [’mycän'] mixture; the elements that constitute the human body (Arab. mizdj): 4 ~ 12019. — MPrs ’myzysn (A-H I, Sogd. 164°-17), from MPrthPrs 'myaln ?(?)myxs- ‘to mix’: Verbum 178, Ghilain 81. Cf guméxtan, gumécisn.
493:cf BdA, p. 712-81, and the second (1. 5) the prep. ‘with’; — adv. back, again: ka Zartuxst hāmēš ~ būt when Z. became
639:armēšt ['Imyšt'] cripple, helpless 51%, pl. cas. obl. ~-dn 854. — Borrowed from Av. (197) armaē-štā-; Paz. armēšt, Skr. v. paūgu (Mx).
1532:trimoš [plmwš, plmwš] forgotten: ~ kartan to forget 875.99; ~ būtan to be forgotten, neglected 6816, — MPrs fr’mws (S); Paz. frāmēš, farmoš; NP faramoš, farmös. Cf Verbum 185, where the com- mon derivation from Skr mrsyate ‘he neglects’ is douted.
1854:hāmēš [h*mwš] silent; ~ bütan to become silent, to cease speaking 3473. ~ NP aümos.
2299:kirpak [krpk'] virtue, pious duty (duties) imposed on the faithful by the Zoroastrian religion, or regarded as religiously meri- torious in general: 6419. 6714, 6921, 7924, 8313; opp. vinds 6313-14 etc.; opp. bazak 80°; enumeration of the principal virtues 8319-855; — kür w ~ exercise of virtue 6416 etc. passim; of pious institutions 13°; varz i ~ practicing virtue 66°; pātdāšn 4 ~ reward of virtue 8019, ~ mizd id. 8018; — ~ u ahlāyēh 066197209; m u vēhēh u rästeh 78. — MPrthPrs kyrbg
2539:spannäk ~ 659, spenäk (-nāt) ~ 10215-17, 10312, 106% = Av. Spanta-Mainyu-; 3 ~ 654; ~ i véh a good spirit, opp. ~ % vattar an evil spirit 651; pl. the celestial gods, pl. cas. obl. ~-dn 40%. 578, 5924, 7218, 7416, 8917.25, with the app. yazdan 7413-18; opp. gétikan, v. getik, 34". 2. the heavenly world, the beyond, opp. geteh, getah 3612, 629.1", 6819-20, 723; har 4 m opp. hir i getäh 6814, 798-11-12, 8023.25; šahr t ~ the realm of Heaven 667; mizd i ~ the reward of Heaven 62°. 658. — Av. (1136) mainyaoya-, adj. of mainyu- (v. s. v. dušmen); Paz. mainyč, minč etc.; NP minč ‘heaven’. The spelling mdnwd of FrP 1 (glossed by mynwy) is constant throughout the whole of BP, and must not be emended to mynwg or mynwk. An adj. mēnēk < *mainyava-ka- is so far only attested in MPrs: mynwg $h ‘the Heavenly King‘ (List 85), and the abstr. mynwgyh ‘the quality of possessing an animal spirit (menög)’, of the body, as opposed to gy’n and rw’n ‘the soul’, a purely Manichean terminology quite for- eign to Zoroastrianism. The Zoroastrians have always understood mönöi as an adj., rendering it in Skr by paralokiya, paralokacara, Sünyacärin (‘existing in the air-space', e.g. 7712. 8514-18), adrsya ‘in- visible’ (SGV), only in the sense of B 2 by a subst.: pat mēnči 723 Skr. v. paraloke. The construction of this adj.: optional addition of the ending -č and position before its head w., is taken over from the NW area, and known from Bal., where the adj. is regularly placed before its headw. and may, or may not, take the ending -e (thus Gilbertson) or -e, -en (thus Longworth Dames; traces of this ending in BP v.s. v. harvistén harvén, névakén). When this construction was borrowed by the SW language the ending -€ was mistaken for the izäfat; hence the translations of the Dasturs: paralokīyā yà buddhih for menöye xrat, ete.
2544:mēš-sār [myás?l] *'of the sheep category” = of sheep-leather: kamar % ~ 6’. — Av. (1109) mačša-, NP meš + sar < Av. (1566 sg.) !saraöa- ‘species’.
2581:mizd [mzd; myzd 812°] reward 62°. 658. 8013; ~ pātdāšn dätan to give a remuner- ation as recompense 103%; wages 812°. — Av. (1187) mižda-; Ps. mzdy; MPrs mzd (BBB); Paz. mazd; NP mizd, muzd.
2860:-p, -pi [-py] (Prth) emphasizing part.: LHw-p = hē-p to him HajA:14; "MT- S-p = kaš-ip, v. "kaš; apar-p-im ravišn I must climb up 40%; (ZK-p =) an-ip tē armēšt daxšak-ip früc venend 5113-14 (v.s. v. an and tē); ZK-py 51: as -p(?) is purely Prth we have to assume the Prth. equivalent of ZK: et-- p? (Henning,
```


## [2026-09-07T17:40:45.727Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY مزد/میش ===\"; grep -n \"مزد\\b\\|مژده\\|میش \" incoming/ARY/ARY_pages.txt | head -20; echo \"=== ARY latin index ===\"; grep -n -i \"MOZD\\|MISH\\|MIZD\" incoming/ARY/ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-07T17:40:45.782Z] TOOL RESULT

```
=== ARY مزد/میش ===
1214:در مقدهه‌ی فرهنگك نوین پیوسته فارسی -انگلیسی و انگلیسی -فارسی. انتشارات مزداء لوس آنجلس»
2279:معنی این واژه در زبان‌های بالتیک(لیتوانی و لتونی و پروسی کهن): دستمزد.
2620:۱- 8۸881۸87 و 813۸7 این واژه را شتق از واجریشه‌ی هند و اروپایی -8۸/811* (به معلی "دمزدن")
2834:اهورا هرمز اهورامزدا / ۹۹
4388:چم اين واژه در زبان سانسکریت: پاداش؛ مزد.
8747:۲- هلت دگرگرنی چم این واژه در زبان‌های ایرانی این است که پس از ظهور زرتشت و آئین او "آهورامزدا" مورد
10367:۱ واژه‌های ژرمنی وابسته به "دمزدن" نیز از این واجریشه‌اند: آلمانی کهن:۳۸۷813۸۷؛ ایسلندی کهن:7۸78۸.
10368:: همچنین واژه‌های یونانی ۳۸۷181 (به چم "دمزدن") و ۸۷8181۸ (به چم "دمزدنی یا تنفس") نیز از همین
13981:مزدا /] ۴۷۱
13997:واژه‌ی آمژده" نیز به احتمال قوی از همین واجريشه است.
14493:میش ۲۸۹
=== ARY latin index ===
1426:RAMDITI RAMISHN, RAM, RAMENITAN
1631:AZMISHT AZIMA AVESTAN) glong\
1983:BARNHART: (MIX) 668 MISHRAS, LITHUANIAN) gg
8119:OLD HIGH GERMAN) of gilt DAM, DAMISHN — (PAHLAVI) 15 he
13563:was y py Mish oF 9? (M¥s \)MUS, MUKN
13709:(SANSKRIT) ey Suile MIZD, MOZD PAHLAVI) 6 shay
13710:MIDHA, MIDHAMA MIZD, MYZD HOSSETIC) gus s\
13715:MZDA (CZECH) Soy MIZDO GOTHIC) S35
13727:Tees sebGouy| - MUZDA, MIzDA
13747:ever Misha delice MENDEN
13763:‘REFERENCES Wena MICAC, MISHASH, MIZHAGHAN |
13764:POKORNY, —SSS~S~«STABTAB NIMISHA (SANSKRIT) ey Sst. |
14030:OLD CHURCH why) AT EME! MISHK KURDISH) 2,5 q
14035:MISH © (SERBIAN) «9 pe MUKN, MOUG, — (ARMENIAN) . <4)!
```


## [2026-09-07T17:40:58.399Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npos=t.find('SHEEP RAM Grk')\nleaf=t.count('\\f',0,pos)\nprint('SHEEP table leaf',leaf,'printed',leaf-24)\nprint(t[pos:pos+2500])\nEOF"
}
```


### [2026-09-07T17:40:59.665Z] TOOL RESULT

```
SHEEP table leaf 188 printed 164
SHEEP RAM Grk. ols, mpéBarov xptés NG mpoparo kptapt Lat. ovis aries It. pecora montone Fr, mouton bélter Sp. carnero, oveja morueco Rum. oave berbec Tr. cdera, 61, cit reithe NIr.  caora : reithe W. dafad hwrdd, maharen Br. darivad maout-laro, -tourc’h Goth. lamb ges ON saudr, fer, smali hritr, vedr (coll.)
Dan. faar vaedder Sw. far bagge, viédur, gumse OE sctap ramm, weder ME _ schepe ram, wether NE sheep ram Du. _—schaap ram OHG | scaf ram(mo), widar MHG schaf - wider, ram NHG ss schaf widder, schafbock Lith. avis tekis, avinas Lett. atta, avs auns, tekulis Chsl.  ovica ovinit SCr. ovca ovan Boh. _ ovce beran Pol. owca baran Russ. ovea baran Skt. avi- mesa-, urana-
Ay. anumaya- maeSa-
3.25. Generic words for ‘sheep’, sev- eral of them also or only ‘ewe’.
1. IE *owi-, nom. sg. *owis. Walde- P. 1.167. Ernout-M. 717 f.
Grk. dfs (Arg. acc. pl. dfs), dis (Hom.), ols, the reg. word in Homer and most dialects, but replaced in Att. by mpoBarov; Lat. ovis (> OFr. oue, Rum. oaie), late dim. ovicula (> Sp. oveja ‘ewe’ but also generic) ; Ir. oi generic and ‘ewe’, Ir. disc, NIr. foisc (f by sentence Phonetics) ‘ewe’, (W. ewig ‘hind’); (Goth. awési ‘herd of sheep’, awistr ‘sheepfold’, but lamb ‘sheep’, cf. Jn. 10.15, 16), ON er, OF eowu, ME, NE
SELECTED INDO-EUROPEAN SYNONYMS
3.27 3.28 3.29 WETHER EWE LAMB roplas ols auvos, dpny pouvouxtopLevo ampoBariva apvl, dpvaxe Kptapte vervex ovis agnus castrone pecora agnello mouton brebis agneau carnero llano oveja cordero berbec castrat oaie micl molt (lon) 61, cdira; uan, dinu disc molt foisc uan molli, gwedder _ dafad, oen mamog maout danvadez oan Sti aters lamb, wiprus geldingr @r lamb bede jaar lam galigumse tacke lamm weder eowu lamb wether ewe lamb wether ewe lamb hamel oot lam widar (hamal) ou (ouwt) lamp hamel ouwe lamp hammel, schéps mutterschaf lamm avinas avis éras, avinélis auns avs gers cane ovtca agne, agnict skopac ovan ouca jagnje skopec, beran ovce, bahnice jehné, beranek skop, baran owca jagnig, baranek baran ovca jagnenok petva- avi-, mesi-, urd- maéesi-
ewe, Du. oot, OHG ou, ouwi, MHG ouwe (NHG dial. awe), all ‘ewe’; Lith. avis, Lett. avs, ‘sheep’ or ‘ewe’, derivs. Lith. avinas, Lett. awns ‘male sheep’ (‘ram or ‘wether’), Lith. avinélis ‘lamb’, Lett. aita, aitin’a ‘sheep’; ChSl. ovtca, SCr. ovea, etc., all the Slavic words for ‘sheep’ or ‘ewe’, deriv. ChSI. ovini, SCr. ovan ‘ram’; Skt. avi- ‘sheep’, ‘ewe’.
2. Att., NG mpéBarov, specialized fr. ‘cattle, small cattle’ (3.15).
3. It. pecora, fr. Lat. pecor
```


## [2026-09-07T17:41:07.835Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor m in re.finditer(r'ma[eé][SsŠš]a|mesa-|meṣ', t):\n    leaf=t.count('\\f',0,m.start())\n    print(leaf, leaf-24, t[max(0,m.start()-120):m.start()+160].replace('\\n',' ')[:280])\n    print()\nEOF"
}
```


### [2026-09-07T17:41:09.278Z] TOOL RESULT

```
188 164 atta, avs auns, tekulis Chsl.  ovica ovinit SCr. ovca ovan Boh. _ ovce beran Pol. owca baran Russ. ovea baran Skt. avi- mesa-, urana- Ay. anumaya- maeSa- 3.25. Generic words for ‘sheep’, sev- eral of them also or only ‘ewe’. 1. IE *owi-, nom. sg. *owis. Walde- P. 1.167. Ernout-M.

188 164 l.  ovica ovinit SCr. ovca ovan Boh. _ ovce beran Pol. owca baran Russ. ovea baran Skt. avi- mesa-, urana- Ay. anumaya- maeSa- 3.25. Generic words for ‘sheep’, sev- eral of them also or only ‘ewe’. 1. IE *owi-, nom. sg. *owis. Walde- P. 1.167. Ernout-M. 717 f. Grk. dfs (Arg. acc.

191 167 . Bapi- xot dpves, Baptov’ mpoBarov (Hesych.), Alb. berr ‘wether, livestock’, ultimate source dub. Berneker 43. 6. Skt. mesa-, Av. maéSa- (alone or with varsni- ‘male’) ‘ram’, Skt. mesi-, Av. maési- ‘ewe’, NPers. mis ‘sheep’ : ChSl. mécht ‘bag made of skin’, etc., orig. ‘sheepski

191 167  dpves, Baptov’ mpoBarov (Hesych.), Alb. berr ‘wether, livestock’, ultimate source dub. Berneker 43. 6. Skt. mesa-, Av. maéSa- (alone or with varsni- ‘male’) ‘ram’, Skt. mesi-, Av. maési- ‘ewe’, NPers. mis ‘sheep’ : ChSl. mécht ‘bag made of skin’, etc., orig. ‘sheepskin’ or ‘skin

453 429 ChSl. méchit ‘leather bottle’, Russ. mech (pl. mechi) ‘bellows’, Boh. méch, Pol. miech ‘sack’, Lett. maiss ‘sack’, Skt. mesa- ‘ram, fleece’ perh. orig. ‘sheepskin’. Walde-P. 2.303. Berneker 2.46. Pol. futro (also ‘lining’), 16th cent. borrowing fr. NHG futter ‘lining’ (: Goth. fo
```


## [2026-09-07T17:41:17.712Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(185,196):\n    nums=re.findall(r'(?<![\\d.])(1[0-9]\\d)(?![\\d.])', leaves[i])\n    print(i, nums[:6],'|', leaves[i][:70].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T17:41:18.988Z] TOOL RESULT

```
185 ['153'] | . Pedersen 2.26, 51, 93. Grk. Bots ‘ox, cow’, pl. Bées ‘cattle’, dim. 
186 ['152', '154', '153'] |  lat. 209. 3. ON naut, naut-fé (Dan. néd, Sw. not), OF néat, ME nete (
187 ['152', '153', '155'] | been discussed above (pp. 152, 153), The others are: 1, Ir. dam, NIy. 
188 ['156'] | �� (Lat. tollere, etc.), like Goth. barn ‘child’ fr. *bher- ‘carry’. W
189 ['128', '157', '136'] | n) 61, cdira; uan, dinu disc molt foisc uan molli, gwedder _ dafad, oe
190 [] | ithout con- necting the two groups). G. §. Lane, Language 7.281 ff. It
191 ['158'] |  Collection, Haridwar eee Digitized by Arya Samaj Foundation Chennai a
192 ['159'] | �� (or ber- bec bane with pple. of bdte ‘beat’, here ‘castrate’), but 
193 ['160'] | aving wool on’ used for ‘male sheep’ (érepor kal dpynades ‘male sheep 
194 ['161', '100'] | e words listed under the other headings. Swine were domesticated in Eu
195 ['162'] | ig. dub. NED s.v. hog. Bjorkman, IF 30.262. In NE both hog and pig (3.
```


## [2026-09-07T17:41:27.505Z] TOOL CALL #39: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py"
}
```


### [2026-09-07T17:41:27.552Z] TOOL RESULT

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
```


## [2026-09-07T17:41:38.636Z] TOOL CALL #40: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/misd%CA%B0%C3%B3s\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D8%B2%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%DA%98%D8%AF%D9%87\" \\\n \"https://en.wiktionary.org/wiki/meed\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%DB%8C%D8%B4\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D8%A7%D9%88%D9%85%DB%8C%D8%B4\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 340 verification\" ; done"
}
```


## [2026-09-07T17:41:41.260Z] TOOL CALL #41: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%CE%BC%CE%B1%CE%BB%CE%AC%CF%87%CE%B7\" \\\n \"https://en.wiktionary.org/wiki/malva#Latin\" \\\n \"https://www.etymonline.com/word/mallow\" \\\n \"https://www.etymonline.com/word/malachite\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D9%84%D8%AD\" \\\n \"https://en.wiktionary.org/wiki/%D7%9E%D7%9C%D7%97\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 340 verification\" ; done"
}
```


### [2026-09-07T17:41:45.957Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/da3d9d01e946a1f3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/157af0fbeed72623.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c20cc9398e7fb1c2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c37fa6157bddcac4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dd752b053bd2fef6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/88261092913e176d.txt
```


### [2026-09-07T17:41:51.027Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1b6e542fafe6c6ce.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cb467bd59092ce8b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/aee7e4d7dc0a8e85.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3a12481b1d4132d8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3718e00cdd15ee70.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b934ffbacd9a708e.txt
```


## [2026-09-07T17:41:54.014Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in da3d9d01e946a1f3 157af0fbeed72623 c20cc9398e7fb1c2 c37fa6157bddcac4; do echo \"########## $f\"; head -c 200 $f.txt; echo; grep -n -A12 -i \"Etymology\" $f.txt | head -60; done"
}
```


### [2026-09-07T17:41:55.322Z] TOOL RESULT

```
########## da3d9d01e946a1f3
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/misd%CA%B0%C3%B3s
FETCHED: 2026-09-07T17:41:40Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/misdʰós - Wiktionary, the
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Declension 
69-
70- 1.2.2 
71- Derived terms 
72-
73- 1.2.3 
74- Descendants 
--
137: Etymology
138- [ edit ] 
139-
140- From *mey-s- ( “ to exchange ” ) + *dʰeh₁- ( “ to put, place ” ) . The first element appears to be an s-stem noun.
141-
142- Noun
143- [ edit ] 
144-
145- *misdʰós 
146-
147- reward , prize 
148-
149- wage , payment 
########## 157af0fbeed72623
URL: https://en.wiktionary.org/wiki/%D9%85%D8%B2%D8%AF
FETCHED: 2026-09-07T17:41:41Z
STATUS: 200
TITLE: مزد - Wiktionary, the free dictionary

مزد - Wiktionary, the free dictionary 

 Jump to co
70: Etymology 
71-
72- 2.2 
73- Pronunciation 
74-
75- 2.3 
76- Noun 
77-
78- 2.3.1 
79- Derived terms 
80-
81- 2.4 
82- References 
--
164: Etymology
165- [ edit ] 
166-
167- From Middle Persian [script needed] ( mzd, myzd /⁠mizd⁠/ ) , [ 1 ] from Old Persian , from Proto-Iranian *miždám , from Proto-Indo-Iranian *miždʰám , from Proto-Indo-European *misdʰós . [ 2 ] Cognate with Northern Kurdish mijde , Talysh مژد ( məžd ) , Ossetian мызд ( myzd ) , Avestan 𐬨𐬍𐬲𐬛𐬀 ( mīžda ) , and further with Ancient Greek μισθός ( misthós ) , German Miete . Related to مُژْدَه ( mužda ) .
168-
169- Pronunciation
170- [ edit ] 
171-
172- ( Classical Persian ) IPA ( key ) : /ˈmuzd/ 
173-
174- ( Dari, formal ) IPA ( key ) : [mʊzd̪] 
175-
176- ( Dari, formal ) IPA ( key ) : [mʊzd̪] 
########## c20cc9398e7fb1c2
URL: https://en.wiktionary.org/wiki/%D9%85%DA%98%D8%AF%D9%87
FETCHED: 2026-09-07T17:41:42Z
STATUS: 200
TITLE: مژده - Wiktionary, the free dictionary

مژده - Wiktionary, the free dictionary 

 
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Derived terms 
69-
70- 1.2.2 
71- Descendants 
72-
73- 1.3 
74- Further reading 
--
82: Etymology 
83-
84- 2.2 
85- Pronunciation 
86-
87- 2.3 
88- Noun 
89-
90- 2.3.1 
91- Derived terms 
92-
93- 2.4 
94- Proper noun 
--
166: Etymology
167- [ edit ] 
168-
169- Borrowed from Classical Persian مُژْدَه ( mužda , “ good news ” ) .
170-
171- Noun
172- [ edit ] 
173-
174- مژده • ( müjde ) ( definite accusative مژده‌یی ( müjdeyi ) , plural مژده‌لر ( müjdeler ) ) 
175-
176- good news , glad tidings , something or someone pleasant , fortunate , or otherwise positive 
177- Synonym: تباشیر ( tebâşir ) 
178-
--
238: Etymology
239- [ edit ] 
240-
241- Borrowed from Parthian 𐫖𐫇𐫋𐫅𐫃 ( mwjdg /⁠muždag⁠/ , “ (good) news, message ” ) , from Proto-Iranian *miždám , from Proto-Indo-Iranian *miždʰám , from Proto-Indo-European *misdʰós . Related to مُزْد ( muzd ) .
242-
243- Pronunciation
244- [ edit ] 
245-
246- ( Classical Persian ) IPA ( key ) : /muʒ.ˈda/ 
247-
248- ( Dari, formal ) IPA ( key ) : [mʊʒ.d̪ä] 
249-
250- ( Dari, formal ) IPA ( key ) : [mʊʒ.d̪ä] 
########## c37fa6157bddcac4
URL: https://en.wiktionary.org/wiki/meed
FETCHED: 2026-09-07T17:41:42Z
STATUS: 200
TITLE: meed - Wiktionary, the free dictionary

meed - Wiktionary, the free dictionary 

 Jump to content 

 Main menu
65: Etymology 1 
66-
67- 1.2.1 
68- Noun 
69-
70- 1.2.1.1 
71- Quotations 
72-
73- 1.2.1.2 
74- Derived terms 
75-
76- 1.3 
77: Etymology 2 
78-
79- 1.3.1 
80- Verb 
81-
82- 1.4 
83- See also 
84-
85- 1.5 
86- Anagrams 
87-
88- 2 
89- Central Franconian 
--
124: Etymology 1 
125-
126- 5.1.1 
127- Noun 
128-
129- 5.2 
130: Etymology 2 
131-
132- 5.2.1 
133- Noun 
134-
135- 5.3 
136: Etymology 3 
137-
138- 5.3.1 
139- Noun 
140-
141- 6 
142- Plautdietsch 
143-
144- Toggle Plautdietsch subsection 
145-
146- 6.1 
147: Etymology 
148-
149- 6.2 
150- Adjective 
151-
152- 6.2.1 
153- Antonyms 
154-
155- 6.2.2 
156- Derived terms 
157-
```


## [2026-09-07T17:42:01.729Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '160,230p' c37fa6157bddcac4.txt"
}
```


### [2026-09-07T17:42:01.770Z] TOOL RESULT

```
 6.4 
 Further reading 

 Toggle the table of contents 

 meed 

 21 languages 

 Deutsch 
 Eesti 
 Suomi 
 Français 
 Magyar 
 Հայերեն 
 Bahasa Indonesia 
 Ido 
 Malagasy 
 മലയാളം 
 မြန်မာဘာသာ 
 Nederlands 
 Polski 
 Русский 
 Kiswahili 
 தமிழ் 
 తెలుగు 
 ไทย 
 اردو 
 Tiếng Việt 
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
```


## [2026-09-07T17:42:03.320Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in dd752b053bd2fef6 88261092913e176d; do echo \"##### $f\"; grep -n -A8 \"^ Etymology$\" $f.txt | head -60; done"
}
```


### [2026-09-07T17:42:04.510Z] TOOL RESULT

```
##### dd752b053bd2fef6
212: Etymology
213- [ edit ] 
214-
215- From Proto-Iranian *mayšáh , from Proto-Indo-Iranian *mayšás , from Proto-Indo-European *moysós ( “ sheep, skin of sheep ” ) . Cognate with Sanskrit मेष ( meṣá ) , Avestan 𐬨𐬀𐬉𐬱𐬀 ( maēša ) and Persian میش ( miš ) .
216-
217- Noun
218- [ edit ] 
219-
220- میش • ( meš ) 
--
251: Etymology
252- [ edit ] 
253-
254- Etymology tree
255-
256- Proto-Indo-European *mon- 
257- Proto-Indo-European *mon-us-i-yōs 
258- Proto-Indo-Iranian *manušíyas 
259- Sanskrit म॒नु॒ष्य॑ ( manuṣyà ) 
--
288: Etymology
289- [ edit ] 
290-
291- From Middle Persian 𐭬𐭩𐭱 ( mēš ) , from Old Persian *maišah , from Proto-Iranian *mayšáh , from Proto-Indo-Iranian *mayšás , from Proto-Indo-European *moysós ( “ sheep, skin of sheep ” ) . Cognate with Sanskrit मेष ( meṣá ) and Avestan 𐬨𐬀𐬉𐬱𐬀 ( maēša ) .
292-
293- Pronunciation
294- [ edit ] 
295-
296- ( Classical Persian ) IPA ( key ) : /ˈmeːʃ/ 
--
355: Etymology
356- [ edit ] 
357-
358- Borrowed from Sanskrit मेष ( meṣá ) . Influenced by Classical Persian میش ( mēš ) .
359-
360- Pronunciation
361- [ edit ] 
362-
363- ( Standard Urdu ) IPA ( key ) : /meːʃ/ 
##### 88261092913e176d
161: Etymology
162- [ edit ] 
163-
164- From Middle Persian [script needed] ( TWRAmyš /⁠gāw-mēš⁠/ , literally “ cow-sheep ” ) ; compare Persian گاو ( gâv , “ cow ” ) and میش ( miš , “ ewe ” ) for the constituents. Old Armenian գոմէշ ( gomēš ) , Classical Syriac ܓܡܘܫܐ ( gāmōšā ) and Old Georgian კამბეჩი ( ḳambeči ) are borrowed from Middle Iranian languages.
165-
166- Pronunciation
167- [ edit ] 
168-
169- ( Classical Persian ) IPA ( key ) : /ɡaːw.ˈmeːʃ/
```


## [2026-09-07T17:42:10.758Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"Proto-West Germanic\\|mizdo\\|Proto-Germanic \\*mizd\\|Old English mēd\\|mēd\" c37fa6157bddcac4.txt | head -20"
}
```


### [2026-09-07T17:42:10.799Z] TOOL RESULT

```
263: From Middle English meede , mede , from Old English mēd , meord , meard , meorþ ( “ meed, reward, pay, price, compensation, bribe ” ) , from Proto-West Germanic *miʀdu , from Proto-Germanic *mizdō ( “ meed ” ) , from Proto-Indo-European *misdʰéh₂ , from Proto-Indo-European *mey- ( “ to exchange ” ) .
315: From Middle English meden , from Old English *mēdian ( “ to reward, bribe ” ) , from Proto-West Germanic *miʀdōn , from Proto-Germanic *mizdōną ( “ to reward ” ) , from Proto-Indo-European *misdʰ- ( “ to pay ” ) . Cognate with German Low German meden ( “ to hire, lease, rent ” ) , German mieten ( “ to rent ” ) .
417: From Middle Low German möde , from Old Saxon mōthi , from Proto-West Germanic *mōþī .
471: English terms inherited from Proto-West Germanic 
472: English terms derived from Proto-West Germanic 
499: Plautdietsch terms inherited from Proto-West Germanic 
500: Plautdietsch terms derived from Proto-West Germanic
```


## [2026-09-07T17:42:12.238Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"##### malache\"; grep -n -B2 -A10 \"^ Etymology\" 1b6e542fafe6c6ce.txt | sed -n '1,80p'"
}
```


### [2026-09-07T17:42:12.301Z] TOOL RESULT

```
##### malache
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
74- Declension 
75-
--
159- μάλβακα ( málbaka ) ( acc.sg. ) 
160-
161: Etymology
162- [ edit ] 
163-
164- Uncertain. Likely related to or the sources of Latin malva , Middle Armenian բաղբակ ( baġbak ) and Georgian ბალბა ( balba ) . Suggested to be from a Semitic source; compare Hebrew מַלּוּחַ ( mallū́aḥ , “ saltbush ” ) , Aramaic מַלוּחָא / ܡܲܠܘܼܚܵܐ ( mallūḥā , “ saltbush ” ) , Arabic مُلَّاح ( mullāḥ , “ seepweed ” ) , however these are of the Amaranthaceae family instead of the Malvaceae and have been pointed towards without acquaintance with the Armenian and Georgian.
165-
166- Pronunciation
167- [ edit ] 
168-
169- IPA ( key ) : /ma.lá.kʰɛː/ → /maˈla.çi/ → /maˈla.çi/ 
170-
171- ( 5 th BCE Attic ) IPA ( key ) : /ma.lá.kʰɛː/
```


## [2026-09-07T17:42:20.579Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### malva\"; grep -n -A6 \"^ Etymology\" cb467bd59092ce8b.txt | sed -n '1,60p'; echo; echo \"#### etymonline mallow\"; sed -n '1,60p' aee7e4d7dc0a8e85.txt | tail -40"
}
```


### [2026-09-07T17:42:20.647Z] TOOL RESULT

```
#### malva
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
82: Etymology 
83-
84- 2.2 
85- Pronunciation 
86-
87- 2.3 
88- Noun 
--
119: Etymology 
120-
121- 4.2 
122- Pronunciation 
123-
124- 4.3 
125- Noun 
--
145: Etymology 1 
146-
147- 5.1.1 
148- Pronunciation 
149-
150- 5.1.2 
151- Noun 
--
157: Etymology 2 
158-
159- 5.2.1 
160- Verb 
161-
162- 6 
163- Italian 
--
168: Etymology 
169-
170- 6.2 
171- Pronunciation 
172-
173- 6.3 
174- Noun 
--
191: Etymology 
192-
193- 7.2 
194- Pronunciation 
195-
196- 7.3 
197- Noun 
--
220: Etymology 
221-
222- 8.2 
223- Pronunciation 

#### etymonline mallow
 Origin and history of mallow 

 mallow (n.) 

 late 14c., spelling alteration of late Old English malwe and directly from Latin malva "mallows" (source also of Modern French mauve , Spanish and Italian malva ), a word from a Mediterranean substrate language. The same lost word apparently yielded Greek malakhe "mallow."
 also from late 14c. 

 Entries linking to mallow 

 malachite (n.) 

 common green ore of copper, a basic carbonate of copper having a beautiful green color, late 14c., from French malachite , ultimately from Greek malachitis (lithos) "mallow (stone)," from malakhe "mallow" (see mallow (n.)); the mineral traditionally so called from the resemblance of its color to that of the leaves of the mallow plant.

 malvaceous (adj.) 

 "of or pertaining to the mallow," 1690s, from Late Latin malvaceus , from Latin malva (see mallow ).

 marshmallow 
 mauve 
 See All Related Words (4) 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 marshmallow 

 Old English mersc-mealwe "kind of mallow plant (Althea officinalis) which grows near salt marshes;" from marsh + mallow. The confection (so called from 1877) originally was made from paste from the mucilaginous roots of this plant. The Greek word for the shrub, althaea, is from a

 bush 

 "many-stemmed woody plant," from Old English bysc (found in place names), from West Germanic *busk "bush, thicket" (source also of Old Saxon and Old High German busc, Dutch bosch, bos, German Busch). Influenced by or combined with Old French (busche "firewood") and Medieval Latin

 cheese 

 "curd of milk coagulated, separated from the whey, pressed, and used as food," Old English cyse (West Saxon), cese (Anglian) "cheese," from West Germanic *kasjus (source also of Old Saxon kasi, Old High German chasi, German Käse, Middle Dutch case, Dutch kaas), from Latin caseus 

 brush 

 "instrument consisting of flexible material (bristles, hair, etc.) attached to a handle or stock," late 14c., "dust-sweeper, a brush for sweeping," from Old French broisse, broce "a brush" (13c., Modern French brosse), perhaps from Vulgar Latin *bruscia "a bunch of new shoots" (u
```


## [2026-09-07T17:42:32.896Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### ملح\"; grep -n -A6 \"^ Etymology\" 3718e00cdd15ee70.txt | grep -A6 \"edit\" | head -40; echo; echo \"#### מלח\"; grep -n -A6 \"^ Etymology\" b934ffbacd9a708e.txt | grep -A6 \"edit\" | head -40"
}
```


### [2026-09-07T17:42:32.963Z] TOOL RESULT

```
#### ملح
240- [ edit ] 
241-
242- Root 
243-
244- م ل ح ( m l ḥ ) 
245-
--
--
972- [ edit ] 
973-
974- From Arabic مِلْح ( milḥ , “ salt ” ) .
975-
976- Pronunciation
977- [ edit ] 
--
991: Etymology
992- [ edit ] 
993-
994- From Arabic مِلْح ( milḥ , “ salt ” ) .
995-
996- Pronunciation
997- [ edit ] 
--
1011: Etymology
1012- [ edit ] 
1013-
1014- Borrowed from Arabic مِلْح ( milḥ , “ salt ” ) .
1015-
1016- Noun
1017- [ edit ] 
--
1067: Etymology
1068- [ edit ] 
1069-
1070- From Arabic مِلْح ( milḥ , “ salt ” ) .
1071-
1072- Pronunciation
1073- [ edit ] 

#### מלח
212- [ edit ] 
213-
214- מֶלַח 
215-
216- Root 
217-
--
--
359- [ edit ] 
360-
361- מַלָּחִים 
362-
363- Root 
364-
```


## [2026-09-07T17:42:35.744Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '225,270p' 3718e00cdd15ee70.txt; echo \"-----PERSIAN section?\"; grep -n \"Persian\" 3718e00cdd15ee70.txt | head -20"
}
```


### [2026-09-07T17:42:35.794Z] TOOL RESULT

```
 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 See also: ملخ 

 Arabic
 [ edit ] 

 Etymology
 [ edit ] 

 Root 

 م ل ح ( m l ḥ ) 

 8 terms 

 Inherited from Proto-West Semitic *milḥ- .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /milħ/ 

 Noun
 [ edit ] 

 مِلْح • ( milḥ )  m ( plural أَمْلَاح ( ʔamlāḥ ) or مِلَاح ( milāḥ ) or مِلَح ( milaḥ ) or مِلْحَة ( milḥa ) ) 

 salt 

 salt water 

 wit , intellect 

 knowledge 

 scholar 

 beauty , loveliness , grace 
-----PERSIAN section?
```


## [2026-09-07T17:42:36.304Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '195,240p' b934ffbacd9a708e.txt"
}
```


### [2026-09-07T17:42:36.340Z] TOOL RESULT

```
 מַלַח or מְלַח • ( mālaḥ or mlaḥ ) 

 to salt 

 to steer , to guide , to sail 

 Noun
 [ edit ] 

 מֶלַח or מְלַח • ( melaḥ or məlaḥ )  m 

 absolute state of מִלְחָא ( milḥā , “ salt ” ) 

 Hebrew
 [ edit ] 

 Etymology 1
 [ edit ] 

 מֶלַח 

 Root 

 מ־ל־ח ( m-l-kh ) 

 3 terms 

 From Proto-West Semitic *milḥ- . Compare Aramaic מִלְחָא ( milḥā ) , Classical Syriac ܡܠܚܐ ( milḥā ) , Arabic مِلْح ( milḥ ) , Maltese melħ .

 Pronunciation
 [ edit ] 

 ( reconstructed Biblical ) IPA ( key ) : /mɛlħ/ 

 ( Samaritan ) IPA ( key ) : /ˈmeːla/ 

 ( Tiberian ) IPA ( key ) : /ˈmɛ.laħ/ [ˈmɛː.laħ] 

 ( Yemenite ) IPA ( key ) : /ˈma.laħ/ [ˈmæː.læħ] 

 ( Sephardi ) IPA ( key ) : /ˈme.laħ/ , /ˈme.laχ/ 

 ( Ashkenazi ) IPA ( key ) : /ˈmɛ.laχ/ 

 ( Modern Israeli ) IPA ( key ) : /ˈme.laχ/ 
 Audio : ( file )
```


## [2026-09-07T17:42:46.116Z] TOOL CALL #51: Bash

```json
{
 "command": "for u in \\\n \"https://en.wikipedia.org/wiki/M%C3%A1laga\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/moys%C3%B3s\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D8%B2%D8%AF%D9%88%D8%B1\" ; do python3 tools/fetch_source.py \"$u\" --note \"page 340 verification\"; done"
}
```


### [2026-09-07T17:42:51.300Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/84a781e765a97e5a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/18326219a8c118a4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/218861abb9efaa17.txt
```


## [2026-09-07T17:42:54.192Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### Malaga wiki\"; grep -n -i -B2 -A8 \"Phoenician\\|etymolog\" 84a781e765a97e5a.txt | head -60"
}
```


### [2026-09-07T17:42:54.241Z] TOOL RESULT

```
#### Malaga wiki
374- "Málaga City" redirects here. For the Spanish football club under that name, see FC Málaga City .
375-
376: [[María Eugenia Aubet|Aubet, María Eugenia]]. [https://books.google.com/books?id=B7SLWT2vpNcC&dq=Phoenician%20Malaka&pg=PA305 ''The Phoenicians and the West: politics, colonies and trade''. Cambridge University Press.] {{webarchive |url=https://web.archive.org/web/20160623213252/https://books.google.com/books?id=B7SLWT2vpNcC&lpg=PA310&ots=wVS21ior7W&dq=Phoenician%20Malaka&pg=PA305 |date=23 June 2016 }}</ref>\n<!-- Politics ----------------->"},"government_footnotes":{"wt":""},"government_type":{"wt":"[[Ayuntamiento (Spain)|Ayuntamiento]]"},"governing_body":{"wt":"City Council of Málaga"},"leader_party":{"wt":"[[People's Party (Spain)|PP]]"},"leader_title":{"wt":"[[Alcalde|Mayor]]"},"leader_name":{"wt":"[[Francisco de la Torre (politician)|Francisco de la Torre Prados]]"},"area_total_km2":{"wt":"398"},"area_urban_km2":{"wt":"827"},"elevation_m":{"wt":"11"},"elevation_max_m":{"wt":"1031"},"elevation_min_m":{"wt":"0"},"elevation_min_point":{"wt":"[[Mediterranean Sea]]"},"elevation_max_point":{"wt":"Pico Reina"},"population_as_of":{"wt":"2025"},"population_footnotes":{"wt":"<ref name=\"u970\">{{cite web | title=City Population: Check for Humans | website=City Population | url=https://www.citypopulation.de/checkhuman.html?url=%2Fen%2Fspain%2Fandalucia%2Fm%25C3%25A1laga%2F29067__m%25C3%25A1laga%2F | access-date=2026-07-20}}</ref>"},"population_total":{"wt":"597,173"},"population_density_km2":{"wt":"auto"},"population_urban":{"wt":"855,609"},"population_urban_footnotes":{"wt":"<ref name=\"m951\">{{cite web | title=City Population: Check for Humans | website=City Population | url=https://www.citypopulation.de/checkhuman.html?url=%2Fen%2Fspain%2Furbanareas%2Fandaluc%25C3%25ADa%2F115676__m%25C3%25A1laga%2F | access-date=2026-07-20}}</ref>"},"population_density_urban_km2":{"wt":"auto"},"population_metro":{"wt":"1,100,000"},"population_metro_footnotes":{"wt":"<ref name=\"k839\">{{cite web | title=Datos Basicos Ciudad | website=Málaga Open for Business | url=https://openforbusiness.malaga.eu/es/Datos-Basicos-Ciudad/?utm_source | access-date=2026-07-20}}</ref>"},"population_rank":{"wt":"6th in Spain"},"population_blank1_title":{"wt":"Seat/Locality<ref name=\"e528\">{{cite web | title=City Population: Check for Humans | website=City Population | url=https://www.citypopulation.de/checkhuman.html?url=%2Fen%2Fspain%2Flocalities%2Fmalaga%2Fm%25C3%25A1laga%2F29067000502__m%25C3%25A1laga%2F | access-date=2026-07-20}}</ref>"},"population_blank1":{"wt":"551,480"},"demographics_type2":{"wt":"GDP"},"demographics2_footnotes":{"wt":"<ref>{{Cite web|url=https://ec.europa.eu/eurostat/databrowser/view/met_10r_3gdp/default/table?lang=en|title=Gross domestic product (GDP) at current market prices by metropolitan regions|last=|first=|date=|website=ec.europa.eu|archive-url=|archive-date=|access-date=}}</ref>"},"demographics2_title1":{"wt":"Metro"},"demographics2_info1":{"wt":"€28.244 billion (2020)"},"postal_code_type":{"wt":"Postcode"},"postal_code":{"wt":"29001-29018"},"area_code":{"wt":"+34 (Spain) 95 (Málaga)"},"area_code_type":{"wt":"Calling code"},"website":{"wt":"{{URL|www.malaga.eu}}"},"timezone":{"wt":"[[Central European Time|CET]]"},"utc_offset":{"wt":"+1"},"timezone_DST":{"wt":"[[Central European Summer Time|CEST]]"},"utc_offset_DST":{"wt":"+2"},"official_name":{"wt":""},"module":{"wt":""},"footnotes":{"wt":""}},"i":0}}]}'>Municipality in Andalusia, Spain
377- Málaga
378-
379- Municipality 
380-
381- View from Gibralfaro
382-
383- Cathedral of the Incarnation 
384-
--
448- Málaga ( / ˈ m æ l ə ɡ ə / ⓘ ; Spanish: [ ˈmalaɣa ] ⓘ ) is a municipality of Spain and the capital of the province of Málaga , in the autonomous community of Andalusia . With a population of 592,346 in 2024, it is the 2nd-largest city in Andalusia and the 6th-largest in the country . [ 7 ] It lies in Southern Iberia on the Costa del Sol ( ' Coast of the Sun ' ) of the Mediterranean , primarily on the left bank of the Guadalhorce . The urban core originally developed in the space between the Gibralfaro Hill and the Guadalmedina .
449-
450: Málaga's history spans about 2,800 years, making it one of the oldest continuously inhabited cities in Western Europe . According to most scholars, it was founded about 770   BC by the Phoenicians from Tyre as Malaka . [ 8 ] From the 6th century   BC the city was under the hegemony of Ancient Carthage , and from 218   BC, it was under Roman rule, economically prospering owing to garum production. [ 9 ] In the 8th century, after a period of Visigothic and Byzantine rule, it was placed under Islamic rule. In 1487, the Crown of Castile gained control in the midst of the Granada War . In the 19th century, the city underwent a period of industrialisation followed by a decay in all socioeconomic parameters in the last third of the century. [ 10 ] 
451-
452- The most important business sectors in Málaga are tourism, construction and technology services, but other sectors such as transportation and logistics are beginning to expand. Málaga has consolidated as a tech hub, with companies mainly concentrated in the Málaga TechPark (Technology Park of Andalusia). [ 11 ] It hosts the headquarters of the region's largest bank, Unicaja , and it is the fourth-ranking city in Spain in terms of economic activity . [ 12 ] Regarding transportation, Málaga is served by the Málaga–Costa del Sol Airport and the Port of Málaga , and the city was connected to the high-speed railway network in 2007.
453-
454- History
455- [ edit ] 
456-
457- Main article: History of Málaga 
458-
--
460-
461- Clay amphora from the Cerro del Villar site, near the mouth of the Guadalhorce (6th century BC). 
462: Phoenicians from Tyre founded a colony named Malake [ 13 ] about 770   BC ( Punic : 𐤌𐤋𐤊𐤀 , mlkʾ ). [ 13 ] The town controlled access to the Guadalmedina and served as a waypoint on trade routes between Phoenicia and the Strait of Gibraltar . Like other Phoenician colonies, it fell under Carthaginian rule during the 6th or 5th century   BC. The Phoenician and Later Roman urban core developed around an area running from the Gibralfaro Hill to the mouth of the Malaca flumen ( Guadalmedina ). [ 14 ] 
463-
464: After the Punic Wars , the Roman Republic took control of the town known to them as Malaca . By the 1st century BC, Strabo alluded to its Phoenician profile, in contrast to the hellenised characteristics of the neighbouring settlement of Mainake . [ 15 ] 
465-
466- Transformed into a confederated city, it was under a special law, the Lex Flavia Malacitana . A Roman theatre was built at this time. [ 16 ] After the fall of the Western Roman Empire , it was ruled first by the Visigoths . The city was taken c.   552 by the Byzantine Empire ; [ 17 ] either Malaca or Carthago Nova possibly then becoming the capital of the province of Spania . [ 18 ] The Byzantines restored and expanded the docks, thus consolidating the fishing and trading tradition the city already enjoyed. [ 18 ] The city was retaken by the Visigoth King Sisebut in 615. [ 19 ] The Islamic conquest of Málaga (rendered as مالقة — Mālaqah —in Arab sources) by Arab and Berber forces took place in 711 or perhaps 713. [ 20 ] Following a period of diminished importance during the early stages of the emiral period already in force since before the conquest, Málaga was fully Islamised by the end of the aforementioned period in the wake of Muhammad I 's attributed intervention in the urban configuration as a medina . [ 21 ] 
467-
468- A 19th-century reconstruction of Islamic Malaqah 
469- The consolidation of the city's importance after 930 (under the Caliphate of Córdoba ) ran parallel to the diminishing fortune of Archidona , the latter of which Málaga replaced as the capital of the corresponding kura of Rayya. [ 22 ] [ 23 ] The early 10th-century chronicle of Aḥmad al-Rāzī mentions the vineyards of Málaga, extolling the unparalleled quality of its raisins . [ 24 ] In the 11th century, following the unravelling of Umayyad authority across the caliphate, Málaga became a centre of power of the Hammudids , who established a petty kingdom (nominally also a caliphate) in the city, the taifa of Málaga , complemented by the also Hammudid sister dominion in Ceuta across the Strait of Gibraltar. [ 25 ] The city was seized away from the Hammudids by the Granadan Zirids in 1056 or 1057, and also underwent an ephemeral spell under the Sevillian Abbadids by 1066 before returning to the former. [ 26 ] By the late 11th century, the Zirids lost the city to the North African Almoravids . [ 26 ] 
470-
471- See also: Taifa of Málaga 
472-
--
953- The old historic centre of Málaga reaches the harbour to the south. In the north it is surrounded by mountains, the Montes de Málaga (part of the Baetic Cordillera ) lying in the southern base of the Axarquía hills, and two rivers, the Guadalmedina – the historic center is located on its left bank – and the Guadalhorce , which flows west of the city into the Mediterranean, in the Churriana district.
954-
955: The oldest architectural remains in the city are the walls of the Phoenician city, which are visible in the cellar of the Museo Picasso Málaga .
956-
957- The Roman theatre of Málaga, which dates from the 1st century BC, was rediscovered in 1951. [ 80 ] 
958-
959- The Moors left posterity the dominating presence of the Castle of Gibralfaro , which is connected to the Alcazaba , the lower fortress and royal residence. Both were built during the Taifa period (11th century) and extended during the Nasrid period (13th and 14th centuries). The Alcazaba stands on a hill within the city. Originally, it defended the city from the incursions of pirates. Later, in the 11th century, it was completely rebuilt by the Hammudid dynasty . [ 81 ] Occupying the eastern hillside that rises from the sea and overlooks the city, the Alcazaba was surrounded by palms and pine trees.
960-
961- Like many of the military fortifications that were constructed in Islamic Spain, the Alcazaba of Málaga featured a quadrangular plan. It was protected by an outer and inner wall, both supported by rectangular towers, between which a covered walkway led up the slope to the Gibralfaro (this was the only exchange between the two sites). Due to its rough and awkward hillside topography, corridors throughout the site provided a means of communications for administrative and defensive operations, also affording privacy to the palatial residential quarters.
962-
963- The entrance of the complex featured a grand tower that led into a sophisticated double bent entrance. After passing through several gates, open yards with gardens of pine and eucalyptus trees, and the inner wall through the Puerta de Granada, one finds the 11th- and 14th-century Governor's palace. It was organised around a central rectangular courtyard with a triple-arched gateway and some of the rooms have been preserved to this day. An open 11th-century mirador (belvedere) to the south of this area affords views of the gardens and sea below. Measuring 2.5 square metres (27 square feet) , this small structure highlighted scalloped, five-lobed arches. To the north of this area were a waterwheel and a Cyclopean well (penetrating forty metres or 130 feet below ground), a hammam, workshops and the monumental Puerta de la Torre del Homenaje , the northernmost point of the inner walls. Directly beyond was the passage to the Gibralfaro above.
--
971- Other sights include: [ 84 ] 
972-
973: Walls. Phoenician, Roman, Byzantine, Arab and Spanish remains of the defensive compounds of the city.
974-
975- Church of the Sacred Heart .
976-
977- San Felipe Neri Church .
978-
979- Church of the Holy Martyrs .
980-
```


## [2026-09-07T17:42:55.351Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### moysos\"; grep -n -A10 \"^ Etymology$\" 18326219a8c118a4.txt | head -30; echo \"#### mozdur\"; grep -n -A6 \"^ Etymology$\" 218861abb9efaa17.txt | head -30"
}
```


### [2026-09-07T17:42:56.727Z] TOOL RESULT

```
#### moysos
#### mozdur
181: Etymology
182- [ edit ] 
183-
184- Inherited from Middle Persian [script needed] ( myzdwbl /⁠mizdwar⁠/ , “ hireling, hired laborer ” ) . [ 1 ] Equivalent to مزد ( muzd  / mozd , “ wage ” ) +‎ ـور ( -war  / -var ) .
185-
186- Pronunciation
187- [ edit ] 
--
274: Etymology
275- [ edit ] 
276-
277- Borrowed from Classical Persian مزدور ( muzdūr , “ mercenary ; labourer ” ) , which in turn inherited from Middle Persian [script needed] ( myzdwbl /⁠mizdwar⁠/ , “ hireling, hired laborer ” ) . [ 1 ] 
278-
279- Pronunciation
280- [ edit ]
```


## [2026-09-07T17:43:09.170Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"salt\\|Toponym\\|name.*derive\" 84a781e765a97e5a.txt | head -20; echo ====; head -5 18326219a8c118a4.txt"
}
```


### [2026-09-07T17:43:09.221Z] TOOL RESULT

```
Exit code 1
(eval):1: === not found
```


## [2026-09-07T17:43:11.727Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"salt\" 84a781e765a97e5a.txt | head -10; echo \"-----\"; head -6 18326219a8c118a4.txt"
}
```


### [2026-09-07T17:43:11.780Z] TOOL RESULT

```
-----
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/moys%C3%B3s
FETCHED: 2026-09-07T17:42:49Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/moysós - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/moysós - Wiktionary, the free dictionary
```


## [2026-09-07T17:43:13.898Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '120,200p' 18326219a8c118a4.txt"
}
```


### [2026-09-07T17:43:13.947Z] TOOL RESULT

```
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Noun
 [ edit ] 

 *moysós [ 1 ] [ 2 ] 

 ram , sheep (= *h₂ówis )

 sheepskin , fleece , wool 

 Inflection
 [ edit ] 

 Thematic

 singular

 nominative

 *moysós 

 genitive

 *moysósyo 

 singular

 dual

 plural

 nominative

 *moysós 

 *moysóh₁ 

 *moysóes 

 vocative

 *moysé 

 *moysóh₁ 

 *moysóes 

 accusative

 *moysóm 

 *moysóh₁ 

 *moysóms 

 genitive

 *moysósyo 

 *? 

 *moysóHom 

 ablative
```


## [2026-09-07T17:43:23.798Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT meed/mallow/mauve ===\"; grep -n \"Meed\\|MEED\\|Mallow\\|Mauve\\|Malachite\" SKT.txt | head -10; echo \"=== LKT Malaga/malve ===\"; grep -n -i \"malaga\\|malve\\|milh\" LKT.txt | head -10; echo \"=== FSD meed ===\"; grep -n -i \"meed, n\" FSD_vol3.txt | head -5"
}
```


### [2026-09-07T17:43:23.869Z] TOOL RESULT

```
=== SKT meed/mallow/mauve ===
11265:MaU70,  the  name  of  a  colour ;  see Mallow.
11347:Meed.  (E.)    ME.  mtdt,  mittL m^d.  older  form  m^rd  (with  r  for +  G.    mieth4,   hire;  Goth,   miida, mzda,  Gk.  fua96s,  pay.
=== LKT Malaga/malve ===
695:'Eine  Gemüsepflanze,  Hibiscus  esculen>- tis,  griechisches  Korn',  tk.  ebenso ;  hier- aus rum.  bamie,  bamä,  bambä  'Okra (unreife  Malvenf rucht) ,  GumbokapseP [nach  Ghijä  Pop,  Rumänisch-deutsches Wörterbuch  S.  44].
2112:'Malve';  hieraus  mit  ar.  Art.  und  Imäla alboheza  'dass.'.  —  DE  71.
=== FSD meed ===
```


## [2026-09-07T17:43:24.865Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM milh ===\"; grep -n \"ملح\" AFM_pages.txt | head -5; echo \"=== FVQ milh ===\"; grep -n -i \"milh\\|salt\" FVQ.txt | head -8; echo \"=== AFA milh ===\"; grep -n -i \"milh\\|Salz\" AFA.txt | head -8"
}
```


### [2026-09-07T17:43:24.936Z] TOOL RESULT

```
=== AFM milh ===
785:1 ± ܡ والملح تعريب 3 الشراب المصنوع من الارز ودقيق الدرة
937:يتكون مثل اليد في بعض الينابيع اكات 1:06 ملح الصناعة وهو مركب
1527:ܗ وعشرين او ثلاث ليالٍ :3 وقيل هى ليالى الملحاق ١‏ حيط الحيط ) .
2614:00 بالملح والماء ٠»‏ قات ٠‏ ܐܠ ܝܗ الها ܐܡ ܘܚ § ܐܰܥ او ܚܳܐܝܳܢ الفارسيّة التي
2856:( الطرخون ) نبات ُيَكْبّس في ܐܘ والملح واللبن واصل عروقه العاقر قرعا معرب
=== FVQ milh ===
2855:elusive personalities Umayya b. Abfs-Salt, Musailama, and the 
8147:a Prophet to whom was given the Zabur j j> j (Psalter). 
9417:The Psalter. 
9441:as a corruption of some Jewish or Christian word for the Psalter, 
9474:came to be used by a popular derivation for the Psalter. 6 
12986:and Umayya b. Abi-s-Salt, 6 but it is hardly possible to decide whether 
13879:opposed to the salt water of the sea, and in the two latter passages the 
15411:Mada'in found stores of camphor there and took it for salt, would 
=== AFA milh ===
1821:hat, entlehnt aus ninV nach ^Arüch: kleine eingesalzene
```


## [2026-09-07T17:43:35.818Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nfor pat in ['Meed.  (E.)','MaU70,  the  name']:\n    pos=t.find(pat); leaf=t.count('\\f',0,pos)\n    print(pat[:12],'leaf',leaf,'printed',leaf-20)\n    print(t[pos-200:pos+400].replace('\\n',' '))\n    print()\nEOF"
}
```


## [2026-09-07T17:43:36.930Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON ملح ===\"; grep -n \"ملح\" MON_part2.txt MON_part1.txt | head -6; echo \"=== MON میش ===\"; grep -n \"میش \\|گاومیش\" MON_part2.txt | head -6"
}
```


### [2026-09-07T17:43:37.008Z] TOOL RESULT

```
Meed.  (E.) leaf 302 printed 282
the  Crec-i meipifum.  —  GV.  fUowiXw,  a  medlar. Medley ;  see  MiaoeUaneoua, Medullar,  belooging  to  the  marrow.  (L L,   mrdti/Zaris,  adj.  — L.  meduOa^ Prob.  allied  to  mtd-ius^  middle. Meed.  (E.)    ME.  mtdt,  mittL m^d.  older  form  m^rd  (with  r  for +  G.    mieth4,   hire;  Goth,   miida, mzda,  Gk.  fua96s,  pay. Meek.    (Scand.)      M.  E,    mtki, spelt  meoc,  Ormulum,  667.  — lod. soft,  agile,  meek,  mild  ;  Swed.  mjuM,DmJ myg^  soft;    Du.    muik\  Goth,   mitir*.  v comp.  muka-modii,  gentleseas. Meeraohaum ;  sec  Mere  (1). Meet  (1),  fitting ;  see  

MaU70,  the  leaf 299 printed 279
 :  see  Mandate. Mausoloumf  a  magnificent  tomb.  (L, «Gk.)  L.  mausaUum,  a  splendid  tomb, orig.  the  tomb  of  Mau^olus.-*Gk.  Mavoai- \uov\  from  Viavaai\off  Mausolus,  a  king  of Caria. MaU70,  the  name  of  a  colour ;  see Mallow. MaviB,  the  song-tbnisb.  (F.-C.)  M.E mavis.  »  F.  mauvis,  a  throstle ;  cf.  Span. maJvis,  a  thrush.— Bret,  milfid^  milvui,  a mavis,  also  m\kk<mid  (at  vanncs).  Cf. Com.  mtikuis^  O.  Com.  melhtut,  a  lark. Maw,  stomach.  (E.)  M.E.  imiiM.  A.S. maga.'^  Du.  nuxag,  Icel.  magi,  Swed.  magt, Dan.  mave,  G.  magtn.  ^Perhaps  f
```


### [2026-09-07T17:43:37.074Z] TOOL RESULT

```
=== MON ملح ===
MON_part1.txt:3079:(پ.) بصورت پسوند به آخر اسم ملحق 
MON_part1.txt:3129:اتتتانت: ‏ ۱ (.) (شیم.) ملحی که از 
MON_part1.txt:4208:شباهت به آخر کلمات ملحق شود: انگشتال 
MON_part1.txt:5120:خر دمندانه . گاه به آخره اسم و صفت ملحق 
MON_part1.txt:5888:ایق: | (ص‌نسب.) ملحدی که همه چیز را مباح 
MON_part1.txt:6657:ملحق گردد و چون کلمه‌ای به هاء 
=== MON میش ===
423:غ میش گد ان سستن. ۱-0 
1312:غرم ۲ (.) میش کوهی» کوسفند مادة 
10856:قامیش , گذاشتن: 7-0 [تر. ف. 
10857:غامیش گذاشتن | (مصل.) (عم.) مزاحم 
14876:فلمیش امدن: 7.0 (مسص ل.) 
14880:قمیش می آیی؛ دیگر قمیش نیا (فرعا.)
```


## [2026-09-07T17:43:52.854Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"mizda\\.\" BRT.txt | head -20; echo ====; grep -n \"mizdavan\\|mizda-van\\|mizdvan\\|mižda\" BRT.txt | head"
}
```


### [2026-09-07T17:43:52.911Z] TOOL RESULT

```
Exit code 1
(eval):1: === not found
```


## [2026-09-07T17:43:55.036Z] TOOL CALL #62: Bash

```json
{
 "command": "ls site/pages/340.jpg 2>/dev/null || pdftoppm -f 340 -l 340 -r 150 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg340 && echo done"
}
```


### [2026-09-07T17:43:56.691Z] TOOL RESULT

```
site/pages/340.jpg
done
```


## [2026-09-07T17:43:59.021Z] TOOL CALL #63: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/340.jpg"
}
```


### [2026-09-07T17:43:59.050Z] TOOL RESULT

```

```


## [2026-09-07T17:44:21.326Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 340 -l 340 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg340hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg340hi.png'); print(im.size)\nw,h=im.size\n# Persian box entry0 approx x 540-850/1100, y 200-300/1400 in the 1100x1400 render\nbox=(int(w*0.47),int(h*0.145),int(w*0.80),int(h*0.225))\nim.crop(box).resize((int((box[2]-box[0])*1.6),int((box[3]-box[1])*1.6))).save('crop_pers0.png')\n\""
}
```


### [2026-09-07T17:44:24.415Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-07T17:44:28.141Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop_pers0.png"
}
```


### [2026-09-07T17:44:28.171Z] TOOL RESULT

```

```


## [2026-09-07T17:44:37.255Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg340hi.png'); w,h=im.size\nbox=(int(w*0.22),int(h*0.405),int(w*0.42),int(h*0.45))\nim.crop(box).resize((int((box[2]-box[0])*2.2),int((box[3]-box[1])*2.2))).save('crop_heb.png')\nbox2=(int(w*0.22),int(h*0.715),int(w*0.45),int(h*0.765))\nim.crop(box2).resize((int((box2[2]-box2[0])*2.2),int((box2[3]-box2[1])*2.2))).save('crop_av3.png')\n\""
}
```


### [2026-09-07T17:44:38.870Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T17:44:41.778Z] TOOL CALL #67: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop_heb.png"
}
```


### [2026-09-07T17:44:41.798Z] TOOL RESULT

```

```


## [2026-09-07T17:44:46.494Z] TOOL CALL #68: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop_av3.png"
}
```


### [2026-09-07T17:44:46.514Z] TOOL RESULT

```

```


## [2026-09-07T17:44:57.577Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i,L in enumerate(leaves):\n    if 1090 <= 0: pass\nfor i in range(560,610):\n    L=leaves[i]\n    if re.search(r'ma[eé][sš]', L) or 'Widder' in L or 'Schaf' in L:\n        nums=re.findall(r'(?<![\\d.])(1[01]\\d\\d)(?![\\d.])', L)\n        print('leaf',i,nums[:6])\n        m=re.search(r'ma[eé][sš]\\w*', L)\n        if m: print('   ', L[max(0,m.start()-200):m.start()+300].replace('\\n',' '))\n        for mm in re.finditer(r'Widder|Schaf', L):\n            print('   *', L[max(0,mm.start()-150):mm.start()+150].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T17:44:58.838Z] TOOL RESULT

```
leaf 604 ['1086']
   *  hai  ialär.  —  VgL  lu  näiälay-. •  j.  ni'vaStakö.srvä-  Adj.  (mask.  'va-) 'mit  eingebogenen,  nach  innen  zurückge- krümmten Hörnern',  vom  Schafbock:  maf- sähe  kihrpa  .  .  "vaht  Yt  14.  33. *mvaila>ka-  Adj.,  Ableit  aus  'ni-vaila-  Adj-, PPfP.;  VgL  mp.  vaJian,  np.  gajtan  'd
```


## [2026-09-07T17:45:11.447Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npos=t.find(\"mizda-''\")\nif pos<0:\n    m=re.search(r\"j\\., g\\.\\s+mizda\", t); pos=m.start() if m else -1\nleaf=t.count('\\f',0,pos)\nprint('mizda leaf',leaf)\nprint(t[pos-400:pos+800].replace('\\n',' '))\nleaves=t.split('\\f')\nprint('nums in leaf:', re.findall(r'(?<![\\d.])(11\\d\\d)(?![\\d.])', leaves[leaf])[:8])\nprint()\nfor i in range(612,620):\n    L=leaves[i]\n    print('--- leaf',i, re.findall(r'(?<![\\d.])(11\\d\\d|10\\d\\d)(?![\\d.])', L)[:6], L[:80].replace('\\n',' '))\n    m=re.search(r'ma[eéf][sšl]a', L)\n    if m: print('    HIT:', L[max(0,m.start()-200):m.start()+400].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T17:45:12.878Z] TOOL RESULT

```
mizda leaf 657
miteinander':  yat  mht>h>m raoxsne  tapayäti  'li  urvaranqm  zairigaa- nanam  .  .  stmäia  *uzuxlyeiiiti  YL  7. 4.       i IS.  au*  *müta}'-  f.  'Mischung'  >l,  lam  V.  myas-, —  VgL  lat.  fHisüi,  misiim.  —  Vü,:  mliaki\ Npü-:  Äamiia,  Sü. :  sadahm, —  ')  Mit  i  Yt.  5- —  »)  Falsch  Roth  ZDMG.  34-  703,  Pischel VSL  7.  S7.  —  J)  Wohl  Aamflai  zu  lesen  ;   s. •  j.,  g.  mizda-''  n.  i)  TLohn'  als  das  ver- abredete oder  zugesicherte  oder  gebührende Äquivalent  einer  Leistung  (usw.) :  kaiä  . . tal  'dim  Aan^nl{sd.)  äasä  aspa  arinavattjs (sd.)  ..hyat  m5i ..  aj/hai/r {sd.)  \.44-i&; —  ahmai  'dim  hanmtl  parShüm  (sd.) mariJ.vistäis  Ißd)  mal  vJspät!  gäva  a«r  Y.  | 46.1g;  —  yas/ai  'dim  Aan?ntl{sA.)  nöit däitl\.44.i')\  —  hanalla  ta  tum  tat  'd?m  ^ yat  zaota  kanayamnd  ätsha  Y.55.30;  F.  11; —  'dake  a/r^raUi  (ad.)  Vyt.jo.  a)  bes.  I von  dem  Lohn,  der  den  Gläubigen  ver- 1 sprechen  ist:  haurvata  ammtäia  ySi  stü °d)m  asaonam  pard.asti  jas^nlam  "H.  und  , A.,  die  den  Lohn  der  Gerechten  bilden,  1 —  mndräya-  1188 '  wenn  sie  ins  künftige  Leben  kommen" Ylj.  25;  V.p.44;  —  cvat  aßimäi  nai
nums in leaf: ['1188']

--- leaf 612 []  p>nnine  (sd.)  .  .  \a^a%a mävayaHt  .  .  vjspe  tfnsmiu  (sd.)  Yt. '¥-38; 
--- leaf 613 [] i.:  hauv  ''uvajam  hami^^iyam akunauS mana  Bh.4>3.  bi)  im  gAw.; zu  a  3):
--- leaf 614 [] xta  akurB  V. 2.  31;  —  Aa  ml  bara  aßmaca  . .  N.  lO^; —  yän^m  . .  (i
--- leaf 615 [] n/ö]  ahutS  maxdi*nämqm  (/«^veranlasst fiie  ist  wertlos. PPA,  einer  Basis 
--- leaf 616 ['1108'] 13-  3i  im Gegens.  lu  laslhaiufy.  SSVa^/a  freilich /o/rw- fararn  Aimilah. 
--- leaf 617 [] .  Ä  11; F.^g. *)  Insbesondere  gilt  das  vom  Rindshara  (a. ^armofta-)!);  
--- leaf 618 [] zdayasna  aiäAa  z?md  %rii (sd.)  'yjm  ava.kanay>n  dva  'fa  frasnä^aym malsm
--- leaf 619 [] h  V.  //.  7. j.  maj'na-  Adj.   (fem.  *«J-)   i)  "nackt, °Ha{ND.)  anaiv/i.
```


## [2026-09-07T17:45:19.538Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (617,618):\n    L=leaves[i]\n    for m in re.finditer(r'ma[éefl]s\\w*|mafs\\w*|Schafbock|Widder|Schaf', L):\n        print(i, '|', L[max(0,m.start()-250):m.start()+350].replace('\\n',' '))\n        print()\nEOF"
}
```


### [2026-09-07T17:45:20.863Z] TOOL RESULT

```
617 | sT.  ZA.  3.  266,  Schka- DEK  RealL  103 1. Zam  V.  'nnÄ-,  J  V^  '-4-  —  ^ß'-  "laämait: —  K.:gümä.  {in  V.  Ä  13) :  rnÜai'),  (lU  F.): m««  (in  Aw.-Bach5t.>  —  »  VgL  V.  *.  12  t  — ')  Oder  tIL  mHaJt  aas  ar.  'maqiAa-  ? ■  j.  maesman-  n.  'Harn',  als  Rcimgungs- und  Heilmittel'':  Ävam  tanüm  pairi.- yaozdat^Ua  gius'mana  apäca  paiti  avd^a —  aitä  vasträ  JrasMaoi^fn  •managfui'V. 7. 13;  14,  74,  16. 12;  —  gSus'mana  OtryS.- paiüiristtm  (sd.)  V.J.  51. KompA.  —  Zam  V.  "marä-,  —  Pü. :  gimh.  — I)  Vgl  in  moimia: •  j.  *maesinaAima-''  n.  'Schluck

617 | pairi.- yaozdat^Ua  gius'mana  apäca  paiti  avd^a —  aitä  vasträ  JrasMaoi^fn  •managfui'V. 7. 13;  14,  74,  16. 12;  —  gSus'mana  OtryS.- paiüiristtm  (sd.)  V.J.  51. KompA.  —  Zam  V.  "marä-,  —  Pü. :  gimh.  — I)  Vgl  in  moimia: •  j.  *maesinaAima-''  n.  'Schluck  Harn': "  rJ  .  .  ^'mqn  '>  aiamai  (sd.)  P.  g. Zum  V.  iam:    —    Vgl.  sama-.  —  K.:  apisa- maki')  (miisma  ist  nicht  übersetzt). —  <)  Hds. (nach   DsT.)    maisma   iamait;   aber   BLOcaST Lei.  156  hat  iitmqit.  —  »)  Das  wäre  etwa  ir. 'ufail-samaJi'. j.  'tnaez-  V.  'harnen'.   Fraes.  3  ma

617 | fralsttm  maf- isnli  pasvasca  staoräca  V.J.  6;  —  -ia«- hqm  na  gäisanqm  .  .  aratujriit  ya *maizS*^  vä  *frä  va  saimns{sA.)  srSva- yeiti  N.J7.  a)  mit  Inhaltsakk.:  par(^t dvaHbya  yOi  aahtn  i^altvada&asca  a^ai- tvadai^Ts^a  aae  malsma  malsayanta  (Opt) yaiibyS  .  .  Jroinyante  V.  8. 1 3. mxfrä  'nach  vorne  pissen  vor  — ,  hinans- pissen  über-' (Akk.)  ;^ai  nä  faurva  Jrabda (sd.)  frahdöJräjO  framauaiii  V.  18.  40. ai.  mlkaii,  np,  metaä.  —  Pü.:  mitiOH  (GltPh. /.  301,  Sp.  VendPü.  so«,  3..1etzte(  Wort)  — ■)  Hds.  yoftff,  aber  Pti.:  mnä». g.  

617 |   maf- isnli  pasvasca  staoräca  V.J.  6;  —  -ia«- hqm  na  gäisanqm  .  .  aratujriit  ya *maizS*^  vä  *frä  va  saimns{sA.)  srSva- yeiti  N.J7.  a)  mit  Inhaltsakk.:  par(^t dvaHbya  yOi  aahtn  i^altvada&asca  a^ai- tvadai^Ts^a  aae  malsma  malsayanta  (Opt) yaiibyS  .  .  Jroinyante  V.  8. 1 3. mxfrä  'nach  vorne  pissen  vor  — ,  hinans- pissen  über-' (Akk.)  ;^ai  nä  faurva  Jrabda (sd.)  frahdöJräjO  framauaiii  V.  18.  40. ai.  mlkaii,  np,  metaä.  —  Pü.:  mitiOH  (GltPh. /.  301,  Sp.  VendPü.  so«,  3..1etzte(  Wort)  — ■)  Hds.  yoftff,  aber  Pti.:  mnä». g.  »maez-  

617 | ia  ntiid,  Sa.  i  frasädcfu.  —  0  Wört- lichi  "nicht  faber)  hegen  sie  es,   um  .  .",  — —  1)  JusTls  Obeisetiung  PrJ.<Kf.247  verstehe ich  nicht •  j.  *maezant-  Adj.,  PPA.:  s.  '/waa-  (mit No.  i). •  j.  maeäa-  m.;  mae^-  f.  'Schaf;  Schaf- mutter': 'iahe  kihrpa  aurunahe  Yt.i4.z3; —  'hhe  . .  yat  varsnSi!  tatsMarahe  (sd.) "eiaesSchafbocks.."YU7.56; — hazanntn 'ianain  N.  ^2;  —  °/(  vihrkavaiti  (sd.)  V. ig.  33;  —  °iinqm  damunqm  '(Schafmutter') paiti.puiiranqm  A.J.  7. KompE.;   Ableit.    —    ai.  mtfä-  m.,    m^f/.  f.; mp.  (Pü.),  np.  »ifL •  j. 

617 | d,  Sa.  i  frasädcfu.  —  0  Wört- lichi  "nicht  faber)  hegen  sie  es,   um  .  .",  — —  1)  JusTls  Obeisetiung  PrJ.<Kf.247  verstehe ich  nicht •  j.  *maezant-  Adj.,  PPA.:  s.  '/waa-  (mit No.  i). •  j.  maeäa-  m.;  mae^-  f.  'Schaf;  Schaf- mutter': 'iahe  kihrpa  aurunahe  Yt.i4.z3; —  'hhe  . .  yat  varsnSi!  tatsMarahe  (sd.) "eiaesSchafbocks.."YU7.56; — hazanntn 'ianain  N.  ^2;  —  °/(  vihrkavaiti  (sd.)  V. ig.  33;  —  °iinqm  damunqm  '(Schafmutter') paiti.puiiranqm  A.J.  7. KompE.;   Ableit.    —    ai.  mtfä-  m.,    m^f/.  f.; mp.  (Pü.),  np.  »ifL •  j.  maeäina

617 |   Obeisetiung  PrJ.<Kf.247  verstehe ich  nicht •  j.  *maezant-  Adj.,  PPA.:  s.  '/waa-  (mit No.  i). •  j.  maeäa-  m.;  mae^-  f.  'Schaf;  Schaf- mutter': 'iahe  kihrpa  aurunahe  Yt.i4.z3; —  'hhe  . .  yat  varsnSi!  tatsMarahe  (sd.) "eiaesSchafbocks.."YU7.56; — hazanntn 'ianain  N.  ^2;  —  °/(  vihrkavaiti  (sd.)  V. ig.  33;  —  °iinqm  damunqm  '(Schafmutter') paiti.puiiranqm  A.J.  7. KompE.;   Ableit.    —    ai.  mtfä-  m.,    m^f/.  f.; mp.  (Pü.),  np.  »ifL •  j.  maeäina- Adj.  "vom  Schaf  herrührend, daiiir  bestimmt,  ovillus':  'Hmm  yavaah?nt Aog.  82; ÄbleiL  aus  ni

617 | maeäa-  m.;  mae^-  f.  'Schaf;  Schaf- mutter': 'iahe  kihrpa  aurunahe  Yt.i4.z3; —  'hhe  . .  yat  varsnSi!  tatsMarahe  (sd.) "eiaesSchafbocks.."YU7.56; — hazanntn 'ianain  N.  ^2;  —  °/(  vihrkavaiti  (sd.)  V. ig.  33;  —  °iinqm  damunqm  '(Schafmutter') paiti.puiiranqm  A.J.  7. KompE.;   Ableit.    —    ai.  mtfä-  m.,    m^f/.  f.; mp.  (Pü.),  np.  »ifL •  j.  maeäina- Adj.  "vom  Schaf  herrührend, daiiir  bestimmt,  ovillus':  'Hmm  yavaah?nt Aog.  82; ÄbleiL  aus  nia^io:  —  Pü. :  meiii,  mätak  i  mii •  j.  maoSanö.kara-  Adj.  (fem.  °kairl-) 'Lust,  Wollust  bereitend':  

617 | .."YU7.56; — hazanntn 'ianain  N.  ^2;  —  °/(  vihrkavaiti  (sd.)  V. ig.  33;  —  °iinqm  damunqm  '(Schafmutter') paiti.puiiranqm  A.J.  7. KompE.;   Ableit.    —    ai.  mtfä-  m.,    m^f/.  f.; mp.  (Pü.),  np.  »ifL •  j.  maeäina- Adj.  "vom  Schaf  herrührend, daiiir  bestimmt,  ovillus':  'Hmm  yavaah?nt Aog.  82; ÄbleiL  aus  nia^io:  —  Pü. :  meiii,  mätak  i  mii •  j.  maoSanö.kara-  Adj.  (fem.  °kairl-) 'Lust,  Wollust  bereitend':  jahikayii  .  . •kairyäi  Y,p.3a, Vgl.  ahiinuita:  —  ai.  moiiana-  n.;  vgt,  moda- m.  'Lust'.    —   Pü.!    mülai   (Stt.:   mandatvam) tartä

618 | zdayasna  aiäAa  z?md  %rii (sd.)  'yjm  ava.kanay>n  dva  'fa  frasnä^aym malsmana  giul  *Bim  äp3  "die  Mazday. sollen  in  der  Erde  drei  Löcher  graben, zwei  Löcher  —  da  sollen  sie  mit  Rindsurin waschen  — ,  eins  —  mit  Wasser  — "  V.  76'.  1 2 ; Ä37; — paoirtm  upa  'fim  nt^w^>söis . . iitim  Ufa  . .  xltUm  upa  . .  "hrayS  anya  'ya ni^TVinssis  "ein  erstes  Loch  sollst  du  aus- stechen, ein  

618 |  Rinder- bam  enthaltend.  Der  Raum  ist  zunächst  in iwei  wieder  mit  je  drei  Furchstrichen  umzogene Abteilungen  getchiedeo,  eine  kleinere  mit  den Wasser-  und  eine  grössere  mit  den  Hamlöchern. In  der  letitem  Abteilung  ist  abermals  durch drei  Furcbstiiche  an  der  den  Wasserlöchern abgekehrten  Seite  eine  Unterabteilung  mit  drei Löchern  geschaffen.  Die  Furch  st  riebe  werden  zu je  dreien  gezogen  der  Reibe  nach  l)um  die  Unter' abteilung,  3)  um  die  grössere  Abteilung,  3]  um beide  Abteilungen,  4}  um  die  kleinere  Abteilung ; Tgl.  zu  antar
```


## [2026-09-07T17:45:36.723Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"mizda[a-zA-Z.'’-]*\" BRT.txt | sort | uniq -c | sort -rn | head -20; echo ===; grep -o \"mizdö[a-zA-Z.'-]*\\|mizd\\.[a-z]*\" BRT.txt | sort | uniq -c | head"
}
```


### [2026-09-07T17:45:36.785Z] TOOL RESULT

```
Exit code 1
      3 mizda-
      1 mizdavqn
      1 mizda'vant-
      1 mizdahe
      1 mizda-''
      1 mizda
(eval):1: == not found
```


## [2026-09-07T17:45:47.789Z] TOOL CALL #73: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%D9%85%D9%84%D8%AD/\" \"https://fa.wikipedia.org/wiki/%D9%85%D8%A7%D9%84%D8%A7%DA%AF%D8%A7\"; do python3 tools/fetch_source.py \"$u\" --note \"page 340 verification: Persian melh / Malaga\"; done"
}
```


### [2026-09-07T17:45:51.068Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b7ed0b0fcbfae85c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8779405432c09a32.txt
```


## [2026-09-07T17:45:54.950Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### abadis ملح\"; grep -n \"معین\\|\\[ع\\|نمک\" b7ed0b0fcbfae85c.txt | head -15; echo; echo \"#### fa.wiki مالاگا\"; grep -n \"مالاگا\" 8779405432c09a32.txt | head -5"
}
```


### [2026-09-07T17:45:55.014Z] TOOL RESULT

```
#### abadis ملح
13: مترادف ملح : نمک، ملاحت
20: ملح. [ م ِ ] ( ع اِ ) نمک. ( منتهی الارب ) ( آنندراج ). نمک طعام و مذکر و مؤنث هر دو می آید ولی بیشترمؤنث می باشد. ج ، مِلاح. املاح. ملحة [ م ِ ل َ ح َ / م ِح َ ]. مِلَح. ( ناظم الاطباء ). نمک طعام. تصغیر آن مُلَیحة است. ج ، مِلاح. ( از اقرب الموارد ) : 
29: || هر نمکی. ( ناظم الاطباء ). نام عامی است گونه ای از عقاقیر ارباب صناعت کیمیا را که قسمی از آن را ملح عذب ( شیرین ) و قسمی را ملح مرّ ( تلخ ) خوانند و قسمی موسوم به ملح اندرانی است و قسمی احمر ( سرخ ) باشد که از آن باطیه و سینی کنند و قسمی را ملح نفط گویند که بوی نفط کند و قسمی مسمی به ملح بیضی است که از وی بوی تخم مرغ آب پز آید و قسمی را ملح هندی نامند که به رنگ سیاه باشد و قسمی ملح طبرزد است و ملح بول را از بول گیرند و ملح قلی را از قلی استخراج کنند. ( از مفاتیح العلوم خوارزمی از یادداشت به خط مرحوم دهخدا ). معدنی و مائی می باشد و معدنی بدون آب متکون می گردد و آن جبلی و بری می باشد و مائی او آبهایی است که منجمد گردد و معدنی او اقسام است و هریک را نامی مخصوص است... و بهترین او ملح اندرانی معدنی است پس ملح مائی و بعد از آن نمک طعام و قسمی هندی مائی کمیاب است و زبون ترین آن ملح معدنی است و اقسام تنگار و قلی و بوره و نوشادر را املاح نامند و املاح مصنوعه نیز می باشد و او را از خاکستر بعضی نباتات که آب او را صاف نموده به آتش و یا به آفتاب منعقد می سازند و به دستور از بول حیوانات و انسان نمک به طبخ و عقد می گیرند و بهترین او محرق محلول معقود صاف است و مراد از مطلق ملح نمک طعام است. ( از تحفه حکیم مؤمن ) : ملح از بسیار جنس است و همه اجناسش گرم است. ( الابنیه چ دانشگاه ص 314 ). و رجوع به املاح و نمک ( اصطلاح شیمی ) شود.
34: نمک، ملاح و املاح جمع
38: فرهنگ معین
41: (مِ ) [ ع . ] (اِ. ) نمک . ج . املاح و ملاح . 
46:نمک. 
55:. مُلُوحَة ومّلاحَة به معنی شوری است و مِلْح به معنی شور و نمک است یعنی: این شراب گوارا و این شور و تلخ است ایضا . این لفظ فقط دوبار در کلام الله آمده است. wikialkb: مِلْح 
59: نمک 
63: مِلْحٌ: به معنی وجود نمک در آب است که باعث سختی آب در نوشیدن می شود، ( وَهُوَ الَّذِی مَرَجَ الْبَحْرَیْنِ هَٰذَا عَذْبٌ فُرَاتٌ وَهَٰذَا مِلْحٌ أُجَاجٌ ) 
66: مِلْحٌ: به معنی وجود نمک در آب است که باعث سختی آب در نوشیدن می شود، ( وَهُوَ الَّذِی مَرَجَ الْبَحْرَیْنِ هَٰذَا عَذْبٌ فُرَاتٌ وَهَٰذَا مِلْحٌ أُجَاجٌ ) آب دریا که شوری آن گرفته نشده، قابل شرب نیست. مراد از املاح، ناخالصی ها است.
70: نمک، ملاحت
72: جراد به معنی ملخ است که از حشرات میباشد و اینجا صحبت از ملح به معنی نمک است
74: کلمه ای عربی ست: نمک
82: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 

#### fa.wiki مالاگا
4:TITLE: مالاگا - ویکی‌پدیا، دانشنامهٔ آزاد
6:مالاگا - ویکی‌پدیا، دانشنامهٔ آزاد 
69: مالاگا 
258: برای دیگر کاربردها، مالاگا (ابهام‌زدایی) را ببینید.
261: مالاگا
```


## [2026-09-07T17:46:10.624Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\nfor want in ['mizdho-','moiso-s Oder maiso-s „Schaf']:\n    for i,l in enumerate(lines):\n        if want in l:\n            # find nearest preceding [pdf page N]\n            pg=None\n            for j in range(i,-1,-1):\n                m=re.match(r'\\[pdf page (\\d+)\\]',lines[j].strip())\n                if m: pg=m.group(1); break\n            print('---',want,'line',i+1,'pdf page',pg)\n            print('\\n'.join(lines[i:i+8])[:900])\n            print()\n            break\nEOF"
}
```


## [2026-09-07T17:46:11.422Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"misdh\\|mizdo\\|meed\\|MEED\" IEC.txt | head -8; echo \"=== IEC moiso ===\"; grep -n \"moisos\\|meisos\\|maisos\" IEC.txt | head -8"
}
```


### [2026-09-07T17:46:11.922Z] TOOL RESULT

```
--- mizdho- line 19891 pdf page None
mizdho- „LohD,                  Sold^^    feegen den Ansatz         '^'mid^dho-    s.    Brugmann      626
        Anm 1).
   Ai. nfidhd- n. „Kampfpreis, \YettkampP, av. mtzda- n. „Lohn^, np.
7mizd „Lohn“: gr. taodog „Sold^^; got.          „Lohn“, ags. meoi’d ds. und
ags. med^ as. mcda, ahd. mtta^ miata ds., nhd.           abg, nihzda „Lohn“.
Curtius 260 usw. lat. mTles ist nicht „Soldner^’ (s. Yf. LEAYb.^ s. v.). Piir
                            ;


--- moiso-s Oder maiso-s „Schaf line 20020 pdf page None
moiso-s Oder maiso-s „Schaf;                         PlieB,      Pell,   daraus gefertigte, Schlauche,
        Sacke“.
      Ai. mesa- m. „Widder, Schafbock; Felk‘, av. -maeya- „Widder, Schaf‘; abg.
mech'h „Schlauch“,     russ.       „Fell, Pelz; Schlauch, Balg; Sack‘d (usw.,
s.    Berneker II 46 f. mdisms, mdisza „Heunetz u. dgl.“, lett. mdiss, mdihss
                              ;
                                  lit.
```


### [2026-09-07T17:46:11.978Z] TOOL RESULT

```
10830:misdhos, à, om 'pay, reward'. (Composed of the elements: mit- and -dhos). WP II, 301 Skt. midhám, n. “prize, award’; Av. mizdom ‘wage’; Per. mazd, id.; Oss. mízd, Digor, mizd, id. cf. also muzdur (sic) 'hireling'; Hiero- Hitt. cf. midas ‘servant’; Phryg. (?) Midas (pro- per name); Isaurian Mi00as, id.; Gk. misthós, m. ‘pay, reward; MIr. mad Ir. miadh, m. (respect, honour’. Phonol. of type uisolos, à, q.v.); OBr. muoed ‘pride’; Cor. cf. ar-feth, pl. fedhow ‘wages’; Go. mizdo, f. ‘reward’; OE meord, f. “reward, pay’; (Celtic LW in) OHG miata, MHG miete, OE med, f. id. be- side OE méde 'agreeable; agreement' in view of synthetized consonantism; OCS (and com. SI.) mízda “pay”. (N. B. Windischmann, in the Jena Literary Gazette, 1834, analysed the word as mis- and -dà)
=== IEC moiso ===
```


## [2026-09-07T17:46:21.425Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npos=t.find(\"misdhos, à, om\")\nleaf=t.count('\\f',0,pos)\nprint('IEC leaf',leaf,'approx printed pages',2*(leaf-15),2*(leaf-15)+1)\nEOF\nhead -3 incoming/WLD/WLD_Bd2_pages.txt; grep -c \"pdf page\" incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-07T17:46:22.665Z] TOOL RESULT

```
IEC leaf 433 approx printed pages 836 837
                ALOIS WALDE


0
```


## [2026-09-07T17:48:08.969Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD MALACHITE ===\"; grep -n \"MALACHITE\" AHD_watkins1985.txt | head -3; echo \"=== LEW malva ===\"; grep -n \"malva\" LEW_1910.txt | head -5; echo \"=== LAT malva ===\"; grep -n -i \"malva\" LAT.txt | head -5"
}
```


### [2026-09-07T17:48:09.054Z] TOOL RESULT

```
=== AHD MALACHITE ===
721:[malakhé. Mallow. Greek noun, akin to Latin malva, mallow, both probably borrowed from a pre-Indo-Euro- pean Mediterranean language. 1. Greek malakhé, molo- khé, mallow: MALACHITE. 2. Latin malva, mallow: MALLOW, MAUVE.]
1803:MAL- mel-5 MALACHITE malakhé MALACOLOGY mel-1 MALADY mel-5 MALARIA wer-2
=== LEW malva ===
1066:marya-h II 41, 46, 799 maryaka-h II 41 maryada II 38, 78 -marésana- II 120 mila-h, mdla-, malind- ITI 122 malva- I 508 masam kar- II 43 mdsta- II 109 mastaka-h, mdsta- ka- II 73 masti- IT 56 mastu- IT 7 mah-, mahdad-, ma- hat- II 11 maha-h ,,Fest** II 5 mahant- I 700 mdhas-  ,,Macht*‘ TOE Til, Eh55 mahdayati IL 5 mahi II 13 mahiyaté II 5 mahyam, mahya IT 84 ma ,,Mutter’‘ II 21
=== LAT malva ===
```


## [2026-09-07T17:48:12.307Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor fn,pats,off in [('HUB.txt',[\"micdc; muzd, muzd *Lohn'\",\"muzdur, afgh\"],10),\n                    ('PHD.txt',[\"mizd [m(y)zd | N muzd] reward\",\"ģāw-mēš [TWR Amyš\"],21),\n                    ('NYB_vol2_glossary.txt',[\"mizd [mzd; myzd 812\",\"mēš-sār [myás?l]\"],0)]:\n    t=open(fn,encoding='utf-8',errors='replace').read()\n    for p in pats:\n        pos=t.find(p)\n        if pos<0: print(fn,p[:20],'NOT FOUND'); continue\n        leaf=t.count('\\f',0,pos)\n        print(fn, p[:22],'leaf',leaf,'printed',leaf-off if off else '?')\nEOF"
}
```


### [2026-09-07T17:48:13.560Z] TOOL RESULT

```
HUB.txt micdc; muzd, muzd *Loh leaf 147 printed 137
HUB.txt muzdur, afgh leaf 180 printed 170
PHD.txt mizd [m(y)zd | N muzd] leaf 80 printed 59
PHD.txt ģāw-mēš [TWR Amyš leaf 59 printed 38
NYB_vol2_glossary.txt mizd [mzd; myzd 812 leaf 148 printed ?
NYB_vol2_glossary.txt mēš-sār [myás?l] leaf 146 printed ?
```


## [2026-09-07T17:48:25.162Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\nfor p in ['[malakhé. Mallow.','mizdho-. Reward.']:\n    pos=t.find(p); leaf=t.count('\\f',0,pos)\n    print(p[:18],'leaf',leaf,'printed',leaf-29)\nEOF\necho \"=== PHD mēš ===\"; grep -n \"mēš \\[\" PHD.txt | head -3; grep -o \"mēš \\[[^]]*\\][^.]*\\.\" PHD.txt | head -3"
}
```


### [2026-09-07T17:48:28.257Z] TOOL RESULT

```
[malakhé. Mallow. leaf 68 printed 39
mizdho-. Reward. leaf 72 printed 43
=== PHD mēš ===
380:gawazn [gw’sn' | N ~] deer. gawdar [0011 | N ~] calf. ģāw-dumb [g'bdwmb | N —dum] horn, trumpet. ģāw-mēš [TWR Amyš | N gā(w)mēš] buffalo. £áy-, v. ģādan. Gayómart [g”ywkmlt! = Av. gayó marata | (M gyhmwrd), N ~] the First Man. gaz [gc | N ~] tamarisk. gaz-, —išn, v. gazidan. gazag [gc’k'] biting. ģāzar [g'cl | N gázur] fuller, washerman. £azdum [gcdwm | N každum!] scorpion; astr. Scorpio. £azidag [ezytk! | N gazid] poll-tax. gazidan, gaz- [gc-, gz-ytn! | N ~] bite, sting. ~išn: biting. gëg [gdk' | M gyyg] thief. gēhān [gy)?>n! | = M, N gihān, jahān] world. ~ig [-yk'] worldly, mortal. -ģēn [-k(y)n! | M -gyn, N -gin] suffix forming adjectives of quality. gês [гуз | (M gyswg, N gēsū)] curls, locks. £étig [gytyk, gytydy | M gytyg, N géti] 1. the material world; 2. worldly. ~ig [-yk'] worldly. gil [ТУМА < A tym; gl | N ~] clay. gilag [g(y)lk! | N gila] complaint, lamentation. —-Obàr [wp] swallowing complaint, suffering in silence. ģilēn [T YN Ayn! | N gilin] (made of) clay. gilistag [g/ystk!] home, dwelling of demons. gir-, ~iSnig, v. griftan. gird [git! | M gyrd, N ~] round, circular; gathered. (9) — āmadan: gather, collect (intr.). — kardan: gather, collect (tr.). ~ih: roundness. girdag [gitk' | N ~a] disk, round. gisnag [gink' | P gyfng] short, small. ģišnīz [ginyc | N —] coriander. giyā(h) [gy^h, gy^h | (M gy'w), N ~] grass. ~izag [-yck'] a straw, blade of grass. gizistag [gcystk' | J w/Bzsth] accursed, hateful. gogird [оо | M gwgyrd, N ~] sulphur. ~ӧтапа [-’wmnd] sulphurous. gohr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage. goóhrag [gwhlk'] = göhr. ~-danag [-d^m k!] physicist. 1g6hrig [gwhlyk'] natural, essential. *ģūhrīg [gw(’)hlyk'] equivalent, substitute, indemnity,
659:хак [APLA < А ‘pr’; Pk! | N <] earth, dust. хат [/?m | N ~] crude, raw. xāmīz [h’myc | N ~] pickled meat. xāmēš [/4mwš | N ~] silent. ixān [/?z! | P æn, N ~] house. ~ ud man: house and home, dwelling.
mēš [TWR Amyš | N gā(w)mēš] buffalo.
mēš [/4mwš | N ~] silent.
```


## [2026-09-07T17:48:35.770Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Malve\\|malva f\" LEW_1910.txt | head -8"
}
```


### [2026-09-07T17:48:35.815Z] TOOL RESULT

```
12048:(schweiz.) I 760 Inumpen TI 803 LTiinse IT 812 machen II 3 Miéhre II 79 Majoran II 85 Malve II 17 Mam (frith) IT 21 Mama IT 21 Mamme (alem.)
```


## [2026-09-07T17:48:42.297Z] AGENT

Now I'll write the verification file.


## [2026-09-07T17:57:05.888Z] TOOL CALL #82: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk340.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 340,\n \"book_page\": 310,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Miždho\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *misdʰós (Pokorny *mizdhó-) 'reward, wage, hire'\",\n   \"note\": \"Pokorny 746 has exactly 'mizdhó- ‚Lohn, Sold‘' with av. mīžda-, np. muzd, gr. misthós, Got. mizdō; Watkins/AHD prints the same root as 'mizdho-. Reward. [Pok. mizdho- 746]'. Modern Wiktionary writes it *misdʰós and analyses it as *mey-s- 'exchange' + *dʰeh₁- 'put' (i.e. 'what is put in exchange'), so the root, the language label 'Indo-European' and the gloss 'reward' are all right; only the notation differs (Nourai keeps Pokorny's -zdh-). The one weak point on the page is the Avestan node's second word mīžda-vare, which is not an attested Avestan compound (see node 1).\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *misdʰós (در نگارش پوکورنی *mizdhó-) به معنی «پاداش، مزد، اجرت»؛ پوکورنی (ص ۷۴۶) همین ریشه را با اوستایی mīžda-، فارسی نو muzd، یونانی misthós و گوتی mizdō آورده است. تحلیل امروزی آن را *mey-s- «مبادله کردن» + *dʰeh₁- «نهادن» می‌داند، یعنی «آنچه در برابر کار نهاده می‌شود». عنوان ریشه، برچسب زبانی و معنای آن در نمودار نورایی درست است و تنها شیوهٔ آوانگاری او کهنه (بر پایهٔ پوکورنی) است.\",\n   \"sources\": [\n     W + \"Reconstruction:Proto-Indo-European/misd%CA%B0%C3%B3s\"\n   ],\n   \"ref_check\": [\n     {\"ref\": \"POK:746\", \"status\": \"supports\", \"note\": \"POK_02.txt, \\\\f-leaf 407 (= printed p. 746; the running numeral '746' stands on the same leaf): 'mizdhö-  ,Lohn,  Sold' / Ai. midhá- n., av. mīžda- n., osset. mizd, myzd, np. muzd ,Lohn'; gr. misthós; got. mizdō ... WP. II 301'. Word-for-word Nourai's root box.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. II 301 (incoming/WLD/WLD_Bd2_pages.txt line 19891)\", \"stance\": \"supports\", \"note\": \"'mizdho- ‚Lohn, Sold‘ ... Ai. mīdhá- n., av. mīzda- n. ‚Lohn‘, np. mizd ‚Lohn‘; gr. misthós; got. mizdō, ags. meord ... nhd. Miete, abg. mĭzda' — the source Pokorny himself cites.\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 43 (AHD_watkins1985.txt leaf 72)\", \"stance\": \"supports\", \"note\": \"'mizdho-. Reward. West Germanic *mēdē- in Old English mēd, reward, compensation, meed: MEED. [Pok. mizdho- 746.]'\"},\n     {\"src\": \"IEC\", \"where\": \"Mann col./p. ~836 (IEC.txt leaf 433)\", \"stance\": \"supports\", \"note\": \"'misdhos, ā, om ‘pay, reward’. (Composed of the elements: mit- and -dhos). WP II, 301  Skt. mīdhám ... Av. mizdəm ‘wage’; Per. mazd ... Gk. misthós ... Go. mizdo'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"mîžda; mîžda-vare\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Av. mīžda- n. 'reward, wage' is the direct Iranian continuation of PIE *misdʰós: the PIE cluster *-zdʰ- gives Avestan -žd- and the vowel is lengthened before it (Y.44.18 tat mīždəm hanānī, Y.46.19, Y.55.3). Bartholomae, Altiran. Wb. col. 1187 s.v. mizda- glosses it 'Lohn als das verabredete oder zugesicherte oder gebührende Äquivalent einer Leistung', i.e. exactly 'reward, wage' — confirmed. The second word, mîžda-vare 'wage earner', is NOT an attested Avestan compound: the only Avestan derivative in -va(nt)- is mīžda-vant- 'provided with (the deserved) reward' (BRT col. 1188), and a grep of the whole of Bartholomae yields only mižda-, mižda-vant-/mizdavan̰t- and the case forms mizdahe/mizdavqn. Nourai's -vare is retro-projected from the well attested Middle Persian mizd-war 'hireling' (MacKenzie 1971:59 'mizd ... ~war [-wbl | N -ār] hireling'), whose second element does go back to *bara- 'bearing' (PIE *bʰer-), so his cross-reference ☞Bher 1 is right in substance but the form should be starred as Old Iranian *mīžda-bara-, not printed as Avestan.\",\n     \"derivation_fa\": \"اوستایی mīžda- (خنثی) «پاداش، مزد» بازماندهٔ مستقیم *misdʰós هندواروپایی است؛ خوشهٔ *-zdʰ- در ایرانی باستان به -žd- بدل شده و واکهٔ پیش از آن کشیده شده است (یسنا ۴۴/۱۸، ۴۶/۱۹). بارتولومه (ستون ۱۱۸۷) آن را «مزد، اجرتِ قرارگذاشته‌شده» معنی کرده است؛ پس واژهٔ نخست پذیرفتنی است. اما mîžda-vare در اوستا گواهی نشده است: در فرهنگ بارتولومه تنها mīžda-vant- «دارندهٔ مزد» آمده است. صورت mîžda-vare بازسازیِ نورایی از پهلوی mizd-war «مزدور» (مکنزی، ص ۵۹) است که جزء دوم آن از *bara- «برنده، حمل‌کننده» (ریشهٔ *bʰer-) است؛ بنابراین ارجاع او به ریشهٔ Bher درست است ولی صورت را باید ایرانی باستانِ بازسازی‌شده *mīžda-bara- نوشت، نه اوستایی.\",\n     \"sources\": [W + \"Reconstruction:Proto-Indo-European/misd%CA%B0%C3%B3s\", W + \"%D9%85%D8%B2%D8%AF\"],\n     \"ref_check\": [\n       {\"ref\": \"POK:746\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 407 (p. 746) lists 'av. mīžda- n.' under the root — the Avestan word, though not the compound.\"},\n       {\"ref\": \"KLN:957\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 513, whose running numeral is 957, s.v. 'meed': '... cogn. with OI. mīdham (for *mizdha-) ‘prize, reward’ ..., Avestic mizda, ‘reward’, Gk. misthós (for *mizdhos), ‘wages, pay’'. Klein has mizda but no mīžda-vare.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"col. 1187-1188 (BRT.txt \\\\f-leaf 657, running numeral 1188 on the leaf)\", \"stance\": \"partial\", \"note\": \"'• j., g. mizda- n. 1) ‘Lohn’ als das verabredete oder zugesicherte oder gebührende Äquivalent einer Leistung' and, immediately after, 'g. mizda-vant- Adj. ‘mit dem (gebührenden) Lohn ... versehen’'. Supports mīžda-, but has no *mīžda-vara-/-bara-: `grep -o \\\"mizda[a-zA-Z.'-]*\\\" BRT.txt` returns only mizda-, mizdavqn, mizda'vant-, mizdahe.\"},\n       {\"src\": \"NYB\", \"where\": \"vol. II Glossary s.v. mizd (NYB_vol2_glossary.txt line 2581)\", \"stance\": \"supports\", \"note\": \"'mizd [mzd; myzd 812°] reward ...; wages. — Av. (1187) mižda-; Ps. mzdy; MPrs mzd (BBB); Paz. mazd; NP mizd, muzd' — Nyberg's own reference to Bartholomae col. 1187 for the Avestan form.\"},\n       {\"src\": \"IEC\", \"where\": \"Mann p. ~836 s.v. misdhos\", \"stance\": \"supports\", \"note\": \"'Av. mizdəm ‘wage’' listed with 'cf. also muzdur (sic) ‘hireling’' — Mann too knows the -war derivative only from Persian, not from Avestan.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"moždeh; mozd; mozdŭr\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All three are one family. NP مزد mozd < MP mizd [m(y)zd] 'reward, hire, pay' (MacKenzie 1971:59; Nyberg II s.v. mizd) < Old Iranian *miždam = Av. mīžda-; the Avestan/OIr. cluster -žd- was de-palatalised to -zd- in the SW (Persian) line. مزدور mozdur is inherited from MP mizd-war 'hireling' (MacKenzie 1971:59; Junker's muzdwar quoted in Mo'in's footnote to Borhan p. 2001) = mizd + -war < *bara- 'bearing' (PIE *bʰer-), with the regular MP -war > NP -ūr/-vār. مژده mužde 'good news' keeps the ž because it comes not from the SW form but from a NW/Parthian one: Parthian mwjdg /muždag/ '(good) news, message' > NP mužda, plus the Persian nominal -a; Horn (Grundriss no. 978, p. 219) already treated 'muzd, mužd ‘Lohn, Preis’, mužde (mizde) ‘frohe Botschaft’' as one entry and remarked 'Das u im Neupersischen ist auffällig' (i.e. *mizd would be expected; the u is by labialisation before the cluster). The semantic step is 'reward' > 'the reward paid to the bringer of good news' > 'good news' — still visible in مژدگانی moždegāni (mužde + -gān + -ī) 'the present given for good tidings' (Borhan p. 2005 n. 1, comparing Kurdish mizdgānī). Nourai's chart is right on every count.\",\n     \"derivation_fa\": \"این سه واژه یک خانواده‌اند. «مزد» از فارسی میانهٔ mizd «پاداش، اجرت» (مکنزی ص ۵۹؛ نیبرگ) و آن از ایرانی باستان *miždam، همان mīžda- اوستایی؛ خوشهٔ -žd- در شاخهٔ جنوب‌غربی به -zd- بدل شده است. «مزدور» بازماندهٔ mizd-war پهلوی است: مزد + وَر (از *bara- «برنده»، ریشهٔ *bʰer-) که در فارسی نو به -ور/-ور > ـور بدل شده؛ حاشیهٔ معین بر برهان قاطع (ص ۲۰۰۱) نیز آن را «از: مزد + ور» و پهلوی muzdwar می‌داند. «مژده» ژ خود را نگه داشته چون از صورت شمال‌غربی (پارتی) mwjdg /muždag/ «پیام، خبر خوش» آمده است، نه از صورت جنوب‌غربی. هرن (اسشق ۹۷۸، ص ۲۱۹) هر سه را زیر یک ماده آورده و یادآور شده که «u فارسی نو شگفت است». تحول معنایی: «مزد» > «پاداشی که به آورندهٔ خبر خوش می‌دهند» > «خبر خوش»؛ همین معنا در «مژدگانی» (مژده + گان + ی) مانده است (حاشیهٔ برهان، ص ۲۰۰۵، پانویس ۱). ادعای نورایی درست است.\",\n     \"sources\": [W + \"%D9%85%D8%B2%D8%AF\", W + \"%D9%85%DA%98%D8%AF%D9%87\", W + \"%D9%85%D8%B2%D8%AF%D9%88%D8%B1\"],\n     \"ref_check\": [\n       {\"ref\": \"BQT:2000\", \"status\": \"supports\", \"note\": \"Borhan-e Qateʿ ed. Moʿin vol. 4 (incoming/BQT/BQT_v4_pages.txt): printed p. 2000 = pdf 83 carries the مزد block ('مزدبر ... بمعنی مزدور باشد', 'مزد دندان'), and p. 2001 = pdf 84 has مزدور with Moʿin's etymological footnote 'از: مزد + ور (پیوند اتصاف و دارندگی) ... پهلوی muzdwar «یونکر ص ۱۱۷»، کردی mizdwer «ژابا ص ۳۹۷»'. مژده itself is five pages on, at p. 2005 = pdf 88, whose footnote 3 reads 'هرن «اسشق ۹۷۸» مژده و مژد (به ضم میم) را همریشهٔ مزد داند - رك: مزد' — precisely Nourai's arrow.\"},\n       {\"ref\": \"HRN:219\", \"status\": \"supports\", \"note\": \"HRN.txt \\\\f-leaf 240 = printed p. 219 (offset leaf = p+21): '978. muzd, mužd ‘Lohn, Preis’, mužde (mizde) ‘frohe Botschaft’. aw. mīžda- ‘Lohn’; phlv. m(i)zd (paz. mozd), mūzd (AV.); ai. mīdhá-; got. mizdō ‘Lohn’. ... Das u im Neupersischen ist auffällig.'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"PHD\", \"where\": \"MacKenzie p. 59 (PHD.txt leaf 80, offset leaf = p+21)\", \"stance\": \"supports\", \"note\": \"'mizd [m(y)zd | N muzd] reward, hire, pay. ~war [-wbl | N -ār] hireling.' — both mozd and mozdur come straight out of this MP entry.\"},\n       {\"src\": \"HUB\", \"where\": \"Persische Studien pp. 137 and 170 (HUB.txt leaves 147, 180; offset leaf = p+10)\", \"stance\": \"supports\", \"note\": \"p. 137: 'muzd, mužd ‘Lohn’, paz. mazd Min. Gl. 136, phl. m(i)zd und muzd ..., afgh. LW. mazd oder muzd ‘wages, hire’ = zd. mižda-, ap. *mizda-, gr. ...'; p. 170: 'muzdur, afgh. LW. mazdūr'.\"},\n       {\"src\": \"NYB\", \"where\": \"vol. II Glossary s.v. mizd\", \"stance\": \"supports\", \"note\": \"'... Paz. mazd; NP mizd, muzd'.\"},\n       {\"src\": \"BQT\", \"where\": \"vol. 4 pp. 2001, 2005 (Moʿin's footnotes)\", \"stance\": \"supports\", \"note\": \"quoted in ref_check above; also 'مژدگانی' footnote citing Darmesteter, Études iraniennes I 272 n.1 and Kurdish mizdgānī.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Sogdian\",\n     \"words\": \"myzd\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Sogdian myzd /mizd/ 'wage, reward', written in the Sogdian (S) script, continues Old Iranian *miždam like MP mizd: Sogdian keeps the cluster as -zd- and shows the same i-vocalism, so it is a sister form of the Middle Persian word rather than a Persian loan. It is attested in the Ancient Letters (2.48-49, i.e. the early-4th-c. Sogdian merchant letters from Dunhuang) and discussed by Bailey, Prolexis 280. Gharib's Sogdian Dictionary no. 5675, p. 227, gives 'myzd S | mizd ? ©Av. mizda | salary, reward' — with the same comparison to Avestan mīžda- that Nourai draws.\",\n     \"derivation_fa\": \"سغدی myzd /mizd/ «مزد، پاداش» (به خط سغدی) مانند mizd فارسی میانه بازماندهٔ *miždam ایرانی باستان است؛ سغدی نیز خوشه را -zd- و واکه را i نگه داشته، پس این صورت خواهرِ صورت پهلوی است و وام‌واژهٔ فارسی نیست. گواهِ آن «نامه‌های باستانی» سغدی دون‌هوانگ (سدهٔ چهارم میلادی، ۲/۴۸-۴۹) است و بیلی در Prolexis ص ۲۸۰ به آن پرداخته است. قریب در فرهنگ سغدی (شمارهٔ ۵۶۷۵، ص ۲۲۷) آورده: «myzd ... mizd ؟ ©اوستایی mizda ... مزد، پاداش» — همان مقایسه‌ای که نورایی کرده است. ادعای نورایی درست است.\",\n     \"sources\": [W + \"%D9%85%D8%B2%D8%AF\"],\n     \"ref_check\": [\n       {\"ref\": \"SOD:227\", \"status\": \"supports\", \"note\": \"SOD_pages.txt \\\\f-leaf 293 (printed page ≈ leaf − 66 = 227), entry '5675 myzd S | mizd ? ©Av. mizda | salary, reward | Anc. Lett. 248, 49; Bailey, Prolexis, 280'. Nourai's SOD:227 is therefore a page number, and the page is the right one.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"SOD\", \"where\": \"Gharib no. 5675, p. 227\", \"stance\": \"supports\", \"note\": \"quoted above; the neighbouring entries 5674 myz'y 'urine' and 5684-5687 mz'yx- confirm the alphabetical position, i.e. the page identification.\"},\n       {\"src\": \"POK\", \"where\": \"IEW p. 746 s.v. mizdhó-\", \"stance\": \"silent\", \"note\": \"Pokorny lists Avestan, Ossetic and New Persian but no Sogdian form (his Iranian material is pre-Sogdian-dictionary).\"},\n       {\"src\": \"HENNING\", \"where\": \"HENNING_selected_papers.txt\", \"stance\": \"silent\", \"note\": \"grep for 'myzd' in the Selected Papers returns nothing usable; no independent Sogdian discussion found there.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Germanic\",\n     \"words\": \"medo\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The Germanic node is right in substance but the form is a conflation. Proto-Germanic had *mizdō (f.) 'reward', preserved unchanged in Gothic mizdō (Klein p. 957; Pokorny 746). In West Germanic the *z was rhotacised and then lost before *d with compensatory lengthening (*mizdō > Proto-West-Germanic *miʀdu > *mēdu), giving Old English mēd beside the archaic non-syncopated meord/meard, Old Saxon mēda, Old High German mēta/miata, German Miete 'rent'. Watkins/AHD accordingly writes 'West Germanic *mēdē-'. Nourai's 'medo' is that West Germanic *mēdō/*mēdē- spelled without the length mark, and so skips the Gothic-type *mizdō stage; as a label for the branch immediately above English meed it is acceptable, but 'Germanic *mizdō' would be the correct reconstruction at this level.\",\n     \"derivation_fa\": \"این گره در اصل درست است ولی صورت آن آمیزه‌ای است. ژرمنی آغازین *mizdō «پاداش» داشته که در گوتی بی‌دگرگونی mizdō مانده است (کلاین ص ۹۵۷؛ پوکورنی ص ۷۴۶). در ژرمنی غربی z به r بدل و سپس پیش از d افتاده و واکه در جبران آن کشیده شده است (*mizdō > *miʀdu > *mēdu)؛ از این‌رو انگلیسی کهن mēd (و صورت کهن‌تر meord)، ساکسون کهن mēda، آلمانی علیای کهن mēta/miata و آلمانی Miete پدید آمده‌اند. واتکینز در ضمیمهٔ AHD همین را «ژرمنی غربی *mēdē-» می‌نویسد. صورت «medo» نورایی همان *mēdō ژرمنی غربی بدون نشانهٔ کشش است و مرحلهٔ *mizdō را نادیده می‌گیرد؛ با احتیاط پذیرفتنی است.\",\n     \"sources\": [W + \"meed\", W + \"Reconstruction:Proto-Indo-European/misd%CA%B0%C3%B3s\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt p. 43 (leaf 72): 'mizdho-. Reward. West Germanic *mēdē- in Old English mēd, reward, compensation, meed: MEED. [Pok. mizdho- 746.]' — the reference Nourai cites gives *mēdē-, i.e. his 'medo', but at the West Germanic (not Proto-Germanic) level.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"p. 957 s.v. meed (KLN_1966.txt leaf 513)\", \"stance\": \"partial\", \"note\": \"'OE. mēd, meord, ‘reward, requital’, rel. to OS. meda, OHG. meta, miata, mieta, MHG., G. miete, Goth. mizdō, ‘reward’' — Klein gives the Gothic *mizdō form, not *medo.\"},\n       {\"src\": \"POK\", \"where\": \"IEW p. 746\", \"stance\": \"partial\", \"note\": \"'got. mizdō ‘Lohn’, ags. meord ds. und ags. mēd, as. meda, ahd. meta, miata ds., nhd. Miete' — again *mizdō for Germanic.\"},\n       {\"src\": \"IEC\", \"where\": \"Mann p. ~836 s.v. misdhos\", \"stance\": \"partial\", \"note\": \"'Go. mizdo, f. ‘reward’; OE meord, f. ‘reward, pay’; (Celtic LW in) OHG miata, MHG miete, OE med, f. id.'\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"English\",\n     \"words\": \"meed\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English meed 'reward, recompense' (now only poetic/archaic) is inherited, not borrowed: Old English mēd (West Saxon; beside meord, meard, meorþ) > Middle English mede, meede > meed, with the regular ME ē > ModE /iː/ and the <ee> spelling. It is the direct English reflex of West Germanic *mēdu < Proto-Germanic *mizdō < PIE *misdʰós, hence a cognate of German Miete 'rent' and of Persian mozd. Klein and Skeat both give the chain, and Watkins's index lists 'MEED mizdho-'.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی meed «پاداش» (امروز تنها شعری و کهن‌گرایانه) وام‌واژه نیست بلکه میراثی است: انگلیسی کهن mēd (در کنار صورت کهن‌تر meord) > انگلیسی میانه mede/meede > meed، با تحول منظمِ ēِ انگلیسی میانه به /iː/ و املای ee. این واژه بازماندهٔ راستِ *mēdu ژرمنی غربی < *mizdō ژرمنی آغازین < *misdʰós هندواروپایی است؛ پس هم‌ریشهٔ Miete آلمانی و «مزد» فارسی است. کلاین و اسکیت هر دو همین زنجیره را می‌آورند و فهرست واتکینز نیز MEED را زیر mizdho- آورده است. ادعای نورایی درست است.\",\n     \"sources\": [W + \"meed\"],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; the parent node's KLN:957 and the root's AHD in fact cover it (both quoted below).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"p. 957 s.v. meed (KLN_1966.txt leaf 513)\", \"stance\": \"supports\", \"note\": \"'meed, n., reward (poet.) — ME. mede, fr. OE. mēd, meord, ‘reward, requital’ ...'\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat p. 282 (SKT.txt leaf 302, offset leaf = p+20)\", \"stance\": \"supports\", \"note\": \"'Meed. (E.) ME. mede, ... mēd, older form meord (with r for [z]) ... G. miethe, hire; Goth. mizda, [OSlav.] mzda, Gk. misthós, pay.'\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985, English index (AHD_watkins1985.txt line 1841)\", \"stance\": \"supports\", \"note\": \"'MEED  mizdho-'.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"M.l.h\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Proto-West-Semitic *milḥ- 'salt'; triconsonantal root m-l-ḥ\",\n   \"note\": \"The Semitic root and its gloss are right: Arabic مِلْح milḥ, Hebrew מֶלַח melaḥ, Aramaic מִלְחָא milḥā, Syriac melḥā and Maltese melħ all go back to Proto-West-Semitic *milḥ- 'salt' (Klein p. 928 s.v. mallow gives the same set, adding 'Akkad. milu' — the Akkadian everyday word is in fact ṭābtu, milʾu being 'saltpetre'). What is NOT right on this chart is the Indo-European half of it: Nourai (following Klein, who follows H. Lewy 1895) makes Latin malva and Greek malachē direct borrowings from Hebrew mallūaḥ. Modern scholarship rejects this: Watkins/AHD — Nourai's own reference for the malachite node — says 'Greek malakhḗ ... akin to Latin malva, both probably borrowed from a pre-Indo-European Mediterranean language', and Etymonline and Wiktionary say the same, noting in addition that the Semitic mallūaḥ plants are Amaranthaceae (saltbush) and not Malvaceae. Nodes 4 and 6 are therefore marked disputed. The Málaga branch (nodes 8-12) is an independent and older hypothesis that remains possible but is not proven (see node 8).\",\n   \"note_fa\": \"ریشهٔ سه‌حرفی سامی م‌ل‌ح و معنای «نمک» درست است: عربی مِلْح، عبری melaḥ، آرامی milḥā، سریانی melḥā و مالتی melħ همه از *milḥ- سامیِ غربی آغازین‌اند (کلاین ص ۹۲۸ همین‌ها را آورده است). آنچه درست نیست نیمهٔ هندواروپایی نمودار است: نورایی به پیروی از کلاین (و او به پیروی از ه. لِوی ۱۸۹۵) malva لاتین و malachē یونانی را وام‌واژهٔ بی‌واسطهٔ عبری mallūaḥ می‌داند. پژوهش امروزی این را رد می‌کند؛ واتکینز در ضمیمهٔ AHD — همان مرجعی که خودِ نورایی برای «malachite» به آن ارجاع داده — می‌گوید یونانی malakhḗ و لاتین malva «هر دو احتمالاً از زبانی مدیترانه‌ای پیش‌هندواروپایی وام گرفته شده‌اند»؛ اتیمونلاین و ویکی‌واژه نیز همین را می‌گویند و می‌افزایند که گیاهانِ سامیِ mallūaḥ از تیرهٔ اسفناجیان‌اند نه پنیرکیان. پس گره‌های ۴ و ۶ «رد‌شده» نشان زده‌اند. شاخهٔ مالاگا (گره‌های ۸ تا ۱۲) فرضیه‌ای کهن و ممکن ولی اثبات‌ناشده است.\",\n   \"sources\": [W + \"%D9%85%D9%84%D8%AD\", W + \"%D7%9E%D7%9C%D7%97\", \"https://www.etymonline.com/word/mallow\"],\n   \"ref_check\": [\n     {\"ref\": \"KLN:928\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 499, whose running numeral 929 stands after the entry (so the entry is on p. 928), s.v. mallow: 'ME. malwe, fr. OE. mealwe, fr. L. malva, which, together with Gk. malachē, of s.m., is borrowed fr. Heb. mallūaḥ, ‘mallow’ (Job 30:4), a derivative of melaḥ, ‘salt’; cp. Aram. milḥa, Syr. melḥa, Arab. milḥ, Akkad. milu, ‘salt’. (See H. Lewy, Die semitischen Fremdwörter im Griechischen, 31 f. ...)'. This is Nourai's whole entry, root and all.\"},\n     {\"ref\": \"FVA:384\", \"status\": \"not_checked\", \"note\": \"FVA = S. M. Nahvi, Farhang-e Vāžehā-ye ʿArabi dar Fārsi (dakhil), 1368/1989. data/verification/sources/refs_online.json records it as 'catalog' only: no digital copy on archive.org, ketabnak, noorlib or the open web (re-searched 2026-09), so p. 384 cannot be inspected.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"KLN\", \"where\": \"p. 928 s.v. mallow; p. 926 s.v. Malaga\", \"stance\": \"supports\", \"note\": \"quoted above and under node 8.\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 39 (AHD_watkins1985.txt leaf 68)\", \"stance\": \"contradicts\", \"note\": \"'[malakhḗ. Mallow. Greek noun, akin to Latin malva, mallow, both probably borrowed from a pre-Indo-European Mediterranean language. 1. Greek malakhḗ, molokhḗ, mallow: MALACHITE. 2. Latin malva, mallow: MALLOW, MAUVE.]' — the square brackets mark it as a non-IE word, and no Semitic source is admitted.\"},\n     {\"src\": \"FVQ\", \"where\": \"FVQ.txt, grep 'milh'/'salt'\", \"stance\": \"silent\", \"note\": \"Jeffery's Foreign Vocabulary of the Qurʾān has no entry for مِلْح — as expected, since it is native Semitic and not a loan word.\"},\n     {\"src\": \"AFA\", \"where\": \"AFA.txt, grep 'milh'/'Salz'\", \"stance\": \"silent\", \"note\": \"Fraenkel's Aramäische Fremdwörter treats no Arabic milḥ (again, native, not Aramaic-borrowed).\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Arabic\",\n     \"words\": \"m.l.h, milh\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic مِلْح milḥ (m., pl. أَمْلَاح ʔamlāḥ / مِلَاح milāḥ) 'salt' belongs to the root م ل ح (m-l-ḥ) and is inherited from Proto-West-Semitic *milḥ- — not derived from any other Semitic language, i.e. the arrow 'Semitic root → Arabic' is simply the normal relation of a root to its qatl-pattern noun (*miCC- > milḥ). It is Qurʾānic (25:53 hāḏā ʿaḏbun furātun wa-hāḏā milḥun ʔujāj 'this one sweet and fresh, that one salty and bitter'). The same root gives مَلَحَ malaḥa 'to salt', مَالِح/مَلِيح 'salty', and the transferred senses 'wit, grace, beauty' that Persian later borrowed (see node 2).\",\n     \"derivation_fa\": \"عربی مِلْح (مذکر، جمع: أَملاح/مِلاح) «نمک» از ریشهٔ م‌ل‌ح است و میراثِ *milḥ- سامیِ غربی آغازین؛ یعنی پیکانِ «ریشهٔ سامی ← عربی» چیزی جز رابطهٔ معمولِ ریشه با اسمِ بر وزنِ فِعْل نیست. این واژه قرآنی است (فرقان ۵۳: «هَذَا عَذْبٌ فُرَاتٌ وَهَذَا مِلْحٌ أُجَاجٌ»). از همین ریشه مَلَحَ «نمک زدن»، مالِح/ملیح «شور» و معناهای مجازی «نمکینی، زیبایی» ساخته شده که فارسی بعدها وام گرفت. ادعای نورایی درست است.\",\n     \"sources\": [W + \"%D9%85%D9%84%D8%AD\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:928\", \"status\": \"supports\", \"note\": \"Klein p. 928 s.v. mallow explicitly lists 'Arab. milḥ, ‘salt’' among the cognates of Heb. melaḥ.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"p. 928 s.v. mallow\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n       {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. ملح (Arabic)\", \"stance\": \"supports\", \"note\": \"'Root م ل ح (m l ḥ) ... Inherited from Proto-West Semitic *milḥ-. Noun مِلْح (milḥ) m (plural أَمْلَاح (ʔamlāḥ) or مِلَاح (milāḥ) ...): salt; salt water; wit, intellect; ... beauty, loveliness, grace.'\"},\n       {\"src\": \"FVQ\", \"where\": \"FVQ.txt\", \"stance\": \"silent\", \"note\": \"not treated by Jeffery (native Arabic word).\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"melh\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian مِلح melh 'salt' is a straightforward Arabic loan (an Arabism of the learned, medical and alchemical registers); the inherited Persian word is نمک namak < MP namak, and melh never displaced it in ordinary speech. Moʿin's Farhang marks it '[ع.] (اِ.) نمک. ج. املاح و ملاح' — Arabic, noun, 'salt', plural amlāḥ/milāḥ — and Dehkhoda quotes Muntahā al-arab and the medical literature (ملح اندرانی, ملح طبرزد, ملح بول …). The forms Nourai adds in the margin are the same Arabic stem borrowed with its own morphology: أملاح amlāḥ (broken plural, in Persian 'salts' as a chemical term), مَلاحت malāḥat (maṣdar of the ii-form, 'saltiness' > 'gracefulness, comeliness'), ملیح/ملیحه malīḥ/malīḥa (faʿīl adjective, 'salty' > 'comely, pretty') — the same 'salt → wit/beauty' shift that Arabic itself made.\",\n     \"derivation_fa\": \"«مِلح» در فارسی وام‌واژهٔ عربی است و در لایهٔ ادبی، طبی و کیمیایی به کار می‌رفته؛ واژهٔ میراثی فارسی «نمک» (از namak پهلوی) است و «ملح» هرگز جای آن را در زبان روزمره نگرفت. فرهنگ معین آن را «(مِ) [ع.] (اِ.) نمک. ج. املاح و ملاح» ثبت کرده و دهخدا از منتهی‌الارب و متون طبی شاهد آورده است (ملح اندرانی، ملح طبرزد، ملح بول…). صورت‌های حاشیه‌ای نمودار همه از همان ستاک عربی‌اند: «املاح» جمع مکسر (در فارسی اصطلاح شیمی)، «ملاحت» مصدرِ بابِ دوم به معنی «شوری» و سپس «نمکینی و زیبایی»، «ملیح/ملیحه» صفت بر وزن فعیل به معنی «شور» و سپس «نمکین، زیبا» — همان تحول معناییِ «نمک ← نمکینی/زیبایی» که در خودِ عربی رخ داده است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://abadis.ir/fatofa/%D9%85%D9%84%D8%AD/\", W + \"%D9%85%D9%84%D8%AD\"],\n     \"ref_check\": [\n       {\"ref\": \"FVA:384\", \"status\": \"not_checked\", \"note\": \"Nahvi 1368, Farhang-e Vāžehā-ye ʿArabi dar Fārsi: no digital copy exists on any permitted platform (refs_online.json, re-searched 2026-09), so p. 384 could not be read.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin s.v. ملح, via abadis.ir/fatofa/ملح\", \"stance\": \"supports\", \"note\": \"'(مِ ) [ ع . ] (اِ. ) نمک . ج . املاح و ملاح .' — Moʿin tags the word Arabic and gives both plurals, one of which (املاح) is Nourai's marginal form.\"},\n       {\"src\": \"ARY\", \"where\": \"Dehkhoda text on the same abadis page (Loghatnāme)\", \"stance\": \"supports\", \"note\": \"'ملح. [ م ِ ] ( ع اِ ) نمک. ( منتهی الارب ) ( آنندراج ) ... ج ، مِلاح. املاح ... تصغیر آن مُلَیحة است' — an independent Persian lexicographical confirmation of the loan and of the derivatives.\"},\n       {\"src\": \"AFM\", \"where\": \"AFM_pages.txt, grep 'ملح'\", \"stance\": \"silent\", \"note\": \"Addi Shir's list of Persian words arabised has nothing on ملح, as expected: the traffic here runs the other way (Arabic → Persian).\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Hebrew\",\n     \"words\": \"melah; mallŭh\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Hebrew מֶלַח melaḥ 'salt' (absolute state; construct מְלַח) is inherited from Proto-West-Semitic *milḥ-, exactly parallel to Arabic milḥ — confirmed. מַלּוּחַ mallūaḥ, a maqqūl-type derivative of the same root ('the salty one'), occurs once in the Hebrew Bible, Job 30:4, and its formation from melaḥ is not in doubt. The gloss is what is loose: mallūaḥ is the saltbush / orach Atriplex halimus, a halophyte of the Amaranthaceae (Aramaic mallūḥā, Arabic مُلَّاح mullāḥ 'seepweed' are the same plant); 'mallows' is the King James rendering of Job 30:4 which Klein, and after him Nourai, carried over. The true mallow (Malva) is a Malvaceae and a different plant, which is one of the reasons the borrowing claimed in nodes 4 and 6 is now rejected.\",\n     \"derivation_fa\": \"عبری מֶלַח melaḥ «نمک» میراثِ *milḥ- سامیِ غربی آغازین است و درست با مِلْح عربی برابر می‌ایستد؛ این بخش پذیرفتنی است. מַלּוּחַ mallūaḥ نیز مشتقی از همین ریشه («شوره‌ای») است و یک بار در کتاب ایوب (۳۰:۴) آمده؛ ساخته شدنش از melaḥ تردیدی ندارد. آنچه دقیق نیست معنای آن است: mallūaḥ همان «سلمهٔ شوره‌زار» (Atriplex halimus) از تیرهٔ اسفناجیان است (آرامی mallūḥā و عربی مُلّاح همان گیاه)، و برگردانِ «پنیرک» از ترجمهٔ انگلیسی شاه جیمز به کلاین و از او به نورایی رسیده است. پنیرکِ راستین (Malva) از تیرهٔ پنیرکیان و گیاهی دیگر است؛ همین ناهمخوانی گیاه‌شناختی یکی از دلیل‌های ردِ وام‌گیریِ ادعاشده در گره‌های ۴ و ۶ است.\",\n     \"sources\": [W + \"%D7%9E%D7%9C%D7%97\", W + \"%CE%BC%CE%B1%CE%BB%CE%AC%CF%87%CE%B7\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:928\", \"status\": \"supports\", \"note\": \"Klein p. 928 s.v. mallow: 'Heb. mallūaḥ, ‘mallow’ (Job 30:4), a derivative of melaḥ, ‘salt’' — word for word Nourai's node, gloss included.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. מלח (Hebrew, Etymology 1)\", \"stance\": \"supports\", \"note\": \"'From Proto-West Semitic *milḥ-. Compare Aramaic מִלְחָא (milḥā), Classical Syriac ܡܠܚܐ (milḥā), Arabic مِلْح (milḥ), Maltese melħ.'\"},\n       {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. μαλάχη (Etymology)\", \"stance\": \"partial\", \"note\": \"'compare Hebrew מַלּוּחַ (mallū́aḥ, “saltbush”), Aramaic מַלוּחָא (mallūḥā, “saltbush”), Arabic مُلَّاح (mullāḥ, “seepweed”), however these are of the Amaranthaceae family instead of the Malvaceae' — confirms the word and its root, corrects the gloss.\"},\n       {\"src\": \"KLN\", \"where\": \"p. 928\", \"stance\": \"supports\", \"note\": \"also 'cp. Aram. milḥa, Syr. melḥa' for melaḥ.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Latin\",\n     \"words\": \"malva\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Latin malva 'mallow' is real and is the ancestor of the Romance and English words, but the arrow drawn here — straight from Hebrew mallūaḥ — is not the modern view, on two counts. (i) Source: Watkins/AHD (p. 39 of the 1985 edition, the same appendix Nourai cites as AHD:1527 for malachite) brackets malakhḗ as non-Indo-European and says Greek malakhḗ and Latin malva are 'both probably borrowed from a pre-Indo-European Mediterranean language'; Etymonline says of malva 'a word from a Mediterranean substrate language. The same lost word apparently yielded Greek malakhe'; Beekes and Chantraine treat μαλάχη as Pre-Greek (the α/ο and χ/κ alternations malákhē / molókhē are a Pre-Greek signature). The Semitic explanation goes back to H. Lewy, Die semitischen Fremdwörter im Griechischen (1895), 31 f., which is precisely what Klein p. 928 is quoting, and Wiktionary adds that the Semitic plants are Amaranthaceae, not Malvaceae. (ii) Route: even on the Semitic hypothesis Latin would have taken the word through Greek, as with most Mediterranean plant names, not directly from Hebrew. Verdict: disputed — the modern account is 'Mediterranean substrate word, shared by Greek and Latin'.\",\n     \"derivation_fa\": \"لاتین malva «پنیرک» واژه‌ای واقعی و نیای واژه‌های رومانس و انگلیسی است، اما پیکانی که اینجا کشیده شده — یک‌راست از عبری mallūaḥ — دیدگاه امروزی نیست، از دو جهت: یک) سرچشمه: واتکینز در ضمیمهٔ AHD (چاپ ۱۹۸۵، ص ۳۹؛ همان ضمیمه‌ای که نورایی برای malachite به آن ارجاع می‌دهد) malakhḗ را با قلاب به نشانِ غیرهندواروپایی بودن آورده و می‌گوید یونانی malakhḗ و لاتین malva «هر دو احتمالاً از زبانی مدیترانه‌ای پیش‌هندواروپایی وام گرفته شده‌اند»؛ اتیمونلاین نیز malva را «واژه‌ای از زبانِ زیرلایهٔ مدیترانه‌ای» می‌داند و بیکس و شانترن μαλάχη را پیش‌یونانی می‌شمارند (جابه‌جایی α/ο و χ/κ در malákhē/molókhē نشانهٔ پیش‌یونانی است). فرضیهٔ سامی از ه. لِوی (۱۸۹۵، ص ۳۱ به بعد) است و کلاین (ص ۹۲۸) همان را نقل می‌کند. دو) مسیر: حتی با پذیرشِ فرضیهٔ سامی، لاتین این واژه را — مانند بیشترِ نام‌های گیاهیِ مدیترانه‌ای — از راه یونانی می‌گرفت نه بی‌واسطه از عبری. داوری: پژوهش امروزی این پیکان را رد می‌کند و به جای آن «واژهٔ زیرلایهٔ مدیترانه‌ای، مشترک میان یونانی و لاتین» می‌گوید.\",\n     \"sources\": [\"https://www.etymonline.com/word/mallow\", W + \"%CE%BC%CE%B1%CE%BB%CE%AC%CF%87%CE%B7\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:928\", \"status\": \"supports\", \"note\": \"Klein p. 928 does say what Nourai's arrow says — 'L. malva, which, together with Gk. malachē, of s.m., is borrowed fr. Heb. mallūaḥ' — but he is reporting H. Lewy 1895, and the claim has not survived. The reference supports the chart; the chart does not survive the other references.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 39 s.v. [malakhḗ]\", \"stance\": \"contradicts\", \"note\": \"'Greek noun, akin to Latin malva, mallow, both probably borrowed from a pre-Indo-European Mediterranean language ... 2. Latin malva, mallow: MALLOW, MAUVE.'\"},\n       {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/mallow\", \"stance\": \"contradicts\", \"note\": \"'directly from Latin malva “mallows” ..., a word from a Mediterranean substrate language. The same lost word apparently yielded Greek malakhe “mallow”.'\"},\n       {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. μαλάχη\", \"stance\": \"contradicts\", \"note\": \"'Uncertain. Likely related to or the sources of Latin malva ... Suggested to be from a Semitic source; ... however these are of the Amaranthaceae family instead of the Malvaceae and have been pointed towards without acquaintance with the Armenian and Georgian [բաղբակ baġbak, ბალბა balba].'\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"English\",\n     \"words\": \"mallow, mauve\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Both English words come from Latin malva, but by two different routes and 800 years apart. mallow: Latin malva was borrowed into Old English as mealwe/malwe (it is in the OE herbals), giving Middle English malwe and, by a late-14th-century respelling of final -we as -ow, mallow. mauve: a modern loan from French mauve 'mallow' (< Latin malva), taken into English in 1856-59 as the name of the first aniline dye, W. H. Perkin's 'mauveine', so called from the mallow-flower colour; hence the colour term. Klein treats them in one family ('Cp. malachite, malvacious, mauve'), and Skeat's entry is simply 'Mauve, the name of a colour; see Mallow'. The Latin→English edge is not in doubt; only the Semitic origin further up (node 4) is.\",\n     \"derivation_fa\": \"هر دو واژهٔ انگلیسی از malva لاتین‌اند، اما از دو راه و با هشتصد سال فاصله. mallow: malva لاتین در دورهٔ انگلیسی کهن به صورت mealwe/malwe وام گرفته شد (در گیاه‌نامه‌های انگلیسی کهن هست)، سپس انگلیسی میانه malwe و در پایانِ سدهٔ چهاردهم با تبدیل املای -we به -ow، mallow. mauve: وامی نو از فرانسوی mauve «پنیرک» (< malva لاتین) که در سال‌های ۱۸۵۶-۱۸۵۹ نامِ نخستین رنگِ آنیلینی (mauveine ساختهٔ پرکین) شد، از آن رو که رنگش به گلِ پنیرک می‌مانست؛ و از آنجا نامِ رنگ. کلاین هر دو را یک خانواده می‌داند و اسکیت می‌نویسد «Mauve، نام یک رنگ؛ نگاه کنید به Mallow». پیکانِ لاتین ← انگلیسی تردیدی ندارد؛ آنچه محل تردید است سرچشمهٔ سامیِ بالای زنجیره (گرهٔ ۴) است.\",\n     \"sources\": [\"https://www.etymonline.com/word/mallow\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:928\", \"status\": \"supports\", \"note\": \"Klein p. 928 s.v. mallow: 'ME. malwe, fr. OE. mealwe, fr. L. malva ... Cp. malachite, malvacious, mauve'; the mauve entry itself is on p. 950 (KLN_1966.txt leaf 510): 'mauve, n. and adj., purple dye. — F., fr. L. malva, ‘mallow’. See mallow.'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"SKT\", \"where\": \"Skeat p. 279 (SKT.txt leaf 299)\", \"stance\": \"supports\", \"note\": \"'Mauve, the name of a colour; see Mallow.'\"},\n       {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/mallow\", \"stance\": \"supports\", \"note\": \"'late 14c., spelling alteration of late Old English malwe and directly from Latin malva “mallows” (source also of Modern French mauve, Spanish and Italian malva)'.\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 39\", \"stance\": \"supports\", \"note\": \"'2. Latin malva, mallow: MALLOW, MAUVE.' — both English words assigned to Latin malva.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Greek\",\n     \"words\": \"malaxe\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The word is real: Ancient Greek μαλάχη malákhē (Attic/Ionic also μολόχη molókhē) 'mallow', attested from Hesiod and the Hippocratic corpus; Nourai's 'malaxe' is his transliteration with x for χ. What is disputed is the parentage. The α/ο alternation malákhē ~ molókhē together with the χ/κ variation (cf. μάλβακα in Hesychius) is a classic Pre-Greek signature, and that is how Beekes's Etymological Dictionary of Greek and Chantraine class the word; Watkins/AHD calls it 'probably borrowed from a pre-Indo-European Mediterranean language'; Wiktionary calls the etymology 'Uncertain', mentions the Semitic proposal (Hebrew mallūaḥ) and objects both that the Semitic plants are Amaranthaceae rather than Malvaceae and that the proposal ignores Middle Armenian բաղբակ and Georgian ბალბა, which point to a non-Semitic Mediterranean/Caucasian source. So the Hebrew → Greek arrow reflects H. Lewy 1895 via Klein and is not today's view.\",\n     \"derivation_fa\": \"خودِ واژه واقعی است: یونانی باستان μαλάχη malákhē (در آتیک و ایونی نیز μολόχη molókhē) «پنیرک»، از هزیود و مجموعهٔ بقراطی به بعد گواهی شده؛ «malaxe» آوانگاریِ نورایی با x در برابر χ است. آنچه محل اختلاف است تبارِ آن است. جابه‌جاییِ α/ο در malákhē ~ molókhē همراه با تناوبِ χ/κ (سنجیده شود با μάλβακα در هزوخیوس) نشانهٔ کلاسیکِ واژه‌های پیش‌یونانی است و بیکس و شانترن آن را همین‌گونه دسته‌بندی می‌کنند؛ واتکینز آن را «احتمالاً وام از زبانی مدیترانه‌ای پیش‌هندواروپایی» می‌داند؛ ویکی‌واژه ریشه را «نامعلوم» می‌خواند، پیشنهادِ سامی (عبری mallūaḥ) را می‌آورد و دو ایراد می‌گیرد: ناهمخوانیِ تیرهٔ گیاهی، و نادیده گرفتنِ բաղբակ ارمنیِ میانه و ბალბა گرجی که به سرچشمه‌ای مدیترانه‌ای/قفقازی و نه سامی اشاره دارند. پس پیکانِ عبری ← یونانی بازتابِ نظر لِوی (۱۸۹۵) از راه کلاین است و پژوهش امروزی آن را نمی‌پذیرد.\",\n     \"sources\": [W + \"%CE%BC%CE%B1%CE%BB%CE%AC%CF%87%CE%B7\", \"https://www.etymonline.com/word/mallow\"],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives this node no reference of its own; the parent's KLN:928 covers it and does say 'L. malva, which, together with Gk. malachē, of s.m., is borrowed fr. Heb. mallūaḥ' — so the claim is Klein's (after H. Lewy 1895), not Nourai's invention.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. μαλάχη\", \"stance\": \"contradicts\", \"note\": \"'Uncertain. Likely related to or the sources of Latin malva, Middle Armenian բաղբակ (baġbak) and Georgian ბალბა (balba). Suggested to be from a Semitic source ... however these are of the Amaranthaceae family instead of the Malvaceae and have been pointed towards without acquaintance with the Armenian and Georgian.' The page also records the Hesychian by-form μάλβακα.\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 39 s.v. [malakhḗ]\", \"stance\": \"contradicts\", \"note\": \"'Greek noun, akin to Latin malva ... both probably borrowed from a pre-Indo-European Mediterranean language.'\"},\n       {\"src\": \"KLN\", \"where\": \"p. 926 s.v. malachite and p. 928 s.v. mallow\", \"stance\": \"supports\", \"note\": \"Klein backs Nourai: 'malachite, n. — F., formed with subst. suff. -ite fr. Gk. μαλάχη, ‘mallow’. See mallow' and the mallow entry's Hebrew derivation.\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"English\",\n     \"words\": \"malachite\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The edge Greek → English is right, with the usual Romance staging. Greek μαλαχῖτις (λίθος) malakhîtis (líthos) 'mallow(-green) stone', a -ῖτις adjective from μαλάχη 'mallow', named for the resemblance of the mineral's green to mallow leaves, gave Latin molochitis (Pliny, NH 37.114) and then French malachite, whence English malachite in the late 14th century. Nourai's gloss is chemically right in substance: malachite is a basic copper carbonate, Cu2CO3(OH)2. Note that his own reference here — the AHD Indo-European appendix — makes the Greek word a pre-Indo-European Mediterranean loan, so the appendix supports this node while contradicting the Hebrew origin drawn at node 6.\",\n     \"derivation_fa\": \"پیکانِ یونانی ← انگلیسی درست است، با میانجی‌های معمولِ رومانس. یونانی μαλαχῖτις (λίθος) «سنگِ پنیرک‌رنگ»، صفتی بر وزنِ -ῖτις از μαλάχη «پنیرک»، به سببِ همانندیِ سبزیِ کانی با برگِ پنیرک؛ از آن لاتین molochitis (پلینی، تاریخ طبیعی ۳۷/۱۱۴) و سپس فرانسوی malachite و در پایانِ سدهٔ چهاردهم انگلیسی malachite. معنایی که نورایی داده از نظر شیمی درست است: مالاکیت کربناتِ بازیِ مس، Cu₂CO₃(OH)₂. نکته آنکه خودِ مرجعِ او — ضمیمهٔ ریشه‌های هندواروپاییِ AHD — واژهٔ یونانی را وامی مدیترانه‌ایِ پیش‌هندواروپایی می‌داند؛ یعنی همان ضمیمه این گره را تأیید و سرچشمهٔ عبریِ گرهٔ ۶ را رد می‌کند.\",\n     \"sources\": [\"https://www.etymonline.com/word/malachite\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD:1527\", \"status\": \"partial\", \"note\": \"The 1976 AHD appendix (pp. 1505-1550) is not open online; the same entry stands in the 1985 standalone Watkins edition at p. 39 (AHD_watkins1985.txt leaf 68): '[malakhḗ. Mallow. ... 1. Greek malakhḗ, molokhḗ, mallow: MALACHITE.]'. It supports Greek malakhḗ > MALACHITE (Nourai's arrow) but square-brackets the Greek word as non-Indo-European and offers no Semitic source.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/malachite\", \"stance\": \"supports\", \"note\": \"'late 14c., from French malachite, ultimately from Greek malachitis (lithos) “mallow (stone),” from malakhe “mallow” ...; the mineral traditionally so called from the resemblance of its color to that of the leaves of the mallow plant.'\"},\n       {\"src\": \"KLN\", \"where\": \"p. 926 s.v. malachite (KLN_1966.txt leaf 497)\", \"stance\": \"supports\", \"note\": \"'malachite, n. — F., formed with subst. suff. -ite fr. Gk. μαλάχη, ‘mallow’. See mallow.'\"}\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"Semitic\",\n     \"words\": \"malha\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The historical facts are solid: a Phoenician colony was founded on the site of modern Málaga by Tyrians about 770 BC, appears on its own coinage as Punic 𐤌𐤋𐤊𐤀 mlkʾ, and is Malaka/Malaca in Greek and Latin authors; Roman Malaca lived on fish-salting and garum. The etymology from the Semitic word for 'salt' — Klein p. 926: 'The name of Malaga, orig. a Phoenician colony, comes fr. Phoen. malha, ‘salt’, which is rel. to Heb. melah' — fits that industry and is the most frequently repeated explanation, but it is not proven: the Punic legend is written with kaph (mlkʾ), not with ḥeth, which is why other scholars connect the name instead with Semitic m-l-k 'king, royal' or take it as pre-Phoenician. Also 'malha' is Klein's citation form of the common noun, not an attested spelling of the toponym. Hence plausible, not confirmed; the node's language label 'Semitic' would be better as 'Phoenician/Punic'.\",\n     \"derivation_fa\": \"داده‌های تاریخی استوارند: مستعمره‌ای فینیقی در جای مالاگای امروز، به دست مردم صور، نزدیک ۷۷۰ پیش از میلاد بنیاد شد، بر سکه‌های خودش به پونیکی 𐤌𐤋𐤊𐤀 mlkʾ نوشته شده و در نویسندگان یونانی و لاتین Malaka/Malaca است؛ مالاکای رومی از نمک‌سود کردن ماهی و ساختِ گاروم می‌زیست. ریشه‌شناسی از واژهٔ سامیِ «نمک» — کلاین ص ۹۲۶: «نام مالاگا، که در آغاز مستعمره‌ای فینیقی بود، از فینیقی malha «نمک» می‌آید که با melaḥ عبری خویشاوند است» — با همین صنعت سازگار است و پرتکرارترین توضیح است، اما اثبات‌شده نیست: نوشتهٔ سکه با کاف است (mlkʾ) نه با حا؛ از این‌رو گروهی دیگر نام را به ریشهٔ m-l-k «شاه، شاهی» می‌بندند یا آن را پیش‌فینیقی می‌شمارند. همچنین «malha» صورتِ استنادیِ کلاین برای اسمِ عام است، نه املای گواهی‌شدهٔ نام‌جای. پس با احتیاط پذیرفتنی است؛ و برچسب «سامی» بهتر بود «فینیقی/پونیکی» باشد.\",\n     \"sources\": [\"https://en.wikipedia.org/wiki/M%C3%A1laga\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:926\", \"status\": \"supports\", \"note\": \"KLN_1966.txt: the entry 'Malaga, n., white wine exported from Malaga, port in Spain. — The name of Malaga, orig. a Phoenician colony, comes fr. Phoen. malha, ‘salt’, which is rel. to Heb. melah. See mallow.' sits at the head of leaf 498, before that leaf's running numeral 927, i.e. on printed p. 926 — Nourai's page is exact.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"Wikipedia\", \"where\": \"en.wikipedia.org/wiki/Málaga, 'History'\", \"stance\": \"partial\", \"note\": \"'Phoenicians from Tyre founded a colony named Malake about 770 BC (Punic: 𐤌𐤋𐤊𐤀, mlkʾ)' and 'the Roman Republic took control of the town known to them as Malaca'. Confirms the Phoenician colony and the name, but the consonantal skeleton mlkʾ does not show the ḥ of m-l-ḥ.\"},\n       {\"src\": \"LKT\", \"where\": \"LKT.txt, grep 'Malaga'\", \"stance\": \"silent\", \"note\": \"Lokotsch's dictionary of European words of oriental origin has no Malaga entry (his 'Malve' material at no. 2112 concerns Arabic-mediated plant names only).\"},\n       {\"src\": \"KLN\", \"where\": \"p. 928 s.v. mallow\", \"stance\": \"supports\", \"note\": \"cross-refers: 'Cp. also Malaga.'\"}\n     ]\n    },\n    {\n     \"id\": 9,\n     \"lang\": \"Spanish\",\n     \"words\": \"Malaga\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Spanish Málaga is the unbroken continuation of the Phoenician name of the same place: Punic mlkʾ / Greek Malaka > Latin Malaca (a confederated city under the Lex Flavia Malacitana, hence the adjective malacitano still used today) > Andalusi Arabic مالقة Mālaqa after the conquest of 711 > Castilian Málaga after the Castilian capture of the city in 1487. The stress on the first syllable and the -g- for Latin -c- are the normal Ibero-Romance treatment of the intervocalic voiceless stop in a name transmitted through Arabic. So the edge 'Phoenician toponym → Spanish' is right; only the further derivation of that toponym from 'salt' (node 8) is uncertain.\",\n     \"derivation_fa\": \"«Málaga»ی اسپانیایی ادامهٔ بی‌گسستِ نامِ فینیقیِ همان جاست: پونیکی mlkʾ / یونانی Malaka > لاتین Malaca (شهری هم‌پیمان زیر «قانون فلاویِ مالاکا»، که صفتِ malacitano تا امروز از آن مانده) > عربیِ اندلسی مالقة Mālaqa پس از فتح ۷۱۱ > کاستیلیِ Málaga پس از بازپس‌گیریِ ۱۴۸۷. تکیه بر هجای نخست و g در برابر c لاتین همان رفتارِ معمولِ ایبرورومانس با انسدادیِ بی‌واکِ میان‌واکه‌ای در نامی است که از راه عربی رسیده باشد. پس پیکانِ «نام‌جای فینیقی ← اسپانیایی» درست است؛ تنها ریشهٔ آن نام از «نمک» (گرهٔ ۸) نامسلم است.\",\n     \"sources\": [\"https://en.wikipedia.org/wiki/M%C3%A1laga\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:926\", \"status\": \"supports\", \"note\": \"Klein p. 926: 'Malaga ... port in Spain. — The name of Malaga, orig. a Phoenician colony ...' — the Spanish place name is exactly what Klein is explaining.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"Wikipedia\", \"where\": \"en.wikipedia.org/wiki/Málaga, 'History'\", \"stance\": \"supports\", \"note\": \"gives the whole chain: Phoenician Malake (Punic mlkʾ) → Roman Malaca (Lex Flavia Malacitana) → Islamic 'مالقة — Mālaqah — in Arab sources' → Castilian control in 1487.\"},\n       {\"src\": \"KLN\", \"where\": \"p. 926\", \"stance\": \"supports\", \"note\": \"as quoted.\"}\n     ]\n    },\n    {\n     \"id\": 10,\n     \"lang\": \"French\",\n     \"words\": \"Malaga\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"A pass-through node with no reference in the book, and correct as far as it goes: French writes the Spanish city Malaga (without the Spanish accent) and uses the bare name as a common noun for its sweet fortified wine and its raisins (vin de Malaga, raisins de Malaga, attested in French from the 17th century). The word is simply borrowed from Spanish Málaga, with French stress on the final syllable. Its only role on the chart is to carry the name onwards to Persian (node 11).\",\n     \"derivation_fa\": \"گرهی گذرا و بی‌مرجع در کتاب، و تا همین اندازه درست: فرانسوی نامِ شهر اسپانیایی را Malaga (بدون تکیه‌نمای اسپانیایی) می‌نویسد و همین نام را برای شرابِ شیرینِ آن دیار و کشمشش نیز به کار می‌برد (vin de Malaga، raisins de Malaga، از سدهٔ هفدهم در فرانسوی گواهی شده). این واژه سرراست از اسپانیاییِ Málaga وام گرفته شده و تنها با تکیهٔ پایانیِ فرانسوی. کارکردِ آن در نمودار تنها رساندنِ نام به فارسی است (گرهٔ ۱۱).\",\n     \"sources\": [\"https://en.wikipedia.org/wiki/M%C3%A1laga\"],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference given in the book for this node; the parent node's KLN:926 covers the name itself.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"PHN\", \"where\": \"PHN.txt (Pihan, mots français dérivés de l'arabe/persan/turc)\", \"stance\": \"silent\", \"note\": \"no Malaga entry — expected, since the French word came from Spanish, not from Arabic.\"},\n       {\"src\": \"DEV\", \"where\": \"DEV.txt (Devic, mots français d'origine orientale)\", \"stance\": \"silent\", \"note\": \"no entry either; French Malaga is treated as a plain Spanish place name.\"}\n     ]\n    },\n    {\n     \"id\": 11,\n     \"lang\": \"Persian\",\n     \"words\": \"mâlâgâ\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Persian مالاگا mālāgā for the Spanish port is a modern European loan, and the spelling itself shows which door it came through: the گ (g) can only render a European g, whereas the older Islamic-period Persian and Arabic form of the same city is مالقة Mālaqa with qāf (as in the Arabic geographers and in Persian works depending on them). A g-form therefore entered Persian in the 19th-20th century from French or English, which makes Nourai's route French → Persian plausible; but nothing in the form distinguishes French from English mediation, and Moʿin's Farhang vol. 6 (the aʿlām volumes), where he cites the entry, is not digitised, so the specific claim could not be checked against its own source.\",\n     \"derivation_fa\": \"«مالاگا» در فارسی وام‌واژه‌ای نو و اروپایی است و خودِ املا نشان می‌دهد از کدام در آمده است: «گ» تنها می‌تواند برگردانِ g اروپایی باشد، در حالی که صورتِ کهن‌ترِ همان شهر در فارسی و عربیِ دورهٔ اسلامی «مالقة» با قاف است (چنان‌که در جغرافی‌نویسانِ عرب و متونِ فارسیِ برگرفته از آنان). پس صورتِ g‌دار در سدهٔ نوزدهم-بیستم از فرانسوی یا انگلیسی به فارسی رسیده است و مسیرِ «فرانسوی ← فارسی» نورایی با احتیاط پذیرفتنی است؛ ولی هیچ نشانهٔ آوایی میانجیِ فرانسوی را از انگلیسی جدا نمی‌کند، و جلد ششم فرهنگ معین (اعلام) که نورایی به آن ارجاع داده دیجیتالی نشده است، پس ادعای مسیر با مرجعِ خودش سنجیده نشد.\",\n     \"sources\": [\"https://fa.wikipedia.org/wiki/%D9%85%D8%A7%D9%84%D8%A7%DA%AF%D8%A7\"],\n     \"ref_check\": [\n       {\"ref\": \"MON6:1883\", \"status\": \"not_checked\", \"note\": \"Moʿin's Farhang-e Fārsi vols. 5-6 are the aʿlām (proper-name) volumes; refs_online.json records that only a 2-volume abridgement of the lexicon volumes (MON_part1/MON_part2, no page breaks) is on archive.org and that 'Page numbers cannot be mapped online', so vol. 6 p. 1883 is not inspectable. grep of MON_part1/part2 for مالاگا returns nothing (they cover the lexicon only).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"Wikipedia (fa)\", \"where\": \"fa.wikipedia.org/wiki/مالاگا\", \"stance\": \"supports\", \"note\": \"the Persian article is headed مالاگا, confirming that this is the current Persian form of the Spanish port's name (with گ, not ق).\"},\n       {\"src\": \"MON\", \"where\": \"MON_part1.txt / MON_part2.txt, grep 'مالاگا'\", \"stance\": \"silent\", \"note\": \"the digitised 2-volume abridgement contains no such entry; the aʿlām volumes Nourai cites are not among the scans.\"}\n     ]\n    },\n    {\n     \"id\": 12,\n     \"lang\": \"English\",\n     \"words\": \"Malaga\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English Malaga is the Spanish place name taken over unchanged except for the loss of the accent and the anglicised stress (/ˈmæləɡə/). As in French, the bare name became a commodity term: 'Malaga' has denoted the sweet fortified wine of the region since the 17th century and, in American usage, the Málaga grape and its raisins. Klein's headword is framed exactly this way — he defines Malaga as the wine and then explains the town's name — which is precisely Nourai's gloss 'a Spanish port and its famous wine'.\",\n     \"derivation_fa\": \"«Malaga»ی انگلیسی همان نام‌جایِ اسپانیایی است که بی‌دگرگونی گرفته شده، جز افتادنِ تکیه‌نما و انگلیسی‌شدنِ جای تکیه (/ˈmæləɡə/). مانند فرانسوی، همین نامِ خالی به نامِ کالا هم بدل شد: Malaga از سدهٔ هفدهم بر شرابِ شیرینِ آن ناحیه و در کاربردِ آمریکایی بر انگورِ مالاگا و کشمشِ آن دلالت می‌کند. مادهٔ کلاین نیز همین‌گونه چیده شده — نخست شراب را تعریف می‌کند و سپس نامِ شهر را توضیح می‌دهد — و این درست همان معنایی است که نورایی نوشته: «بندری اسپانیایی و شرابِ نامدارش». ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wikipedia.org/wiki/M%C3%A1laga\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:926\", \"status\": \"supports\", \"note\": \"Klein p. 926: 'Malaga, n., white wine exported from Malaga, port in Spain. — The name of Malaga, orig. a Phoenician colony, comes fr. Phoen. malha, ‘salt’ ...' — both halves of Nourai's gloss.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"p. 926 s.v. Malaga\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n       {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt (Webster's New Twentieth Century)\", \"stance\": \"silent\", \"note\": \"grep for a Malaga headword in the available volume returns nothing usable (the volume held locally does not reach the M-range proper names).\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 3,\n   \"root\": \"Moiso\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *moysós 'ram, sheep; sheepskin, fleece'\",\n   \"note\": \"Pokorny 747 has the root as 'moiso-s oder maiso-s ‚Schaf; Fließ, Fell, daraus gefertigte Schläuche, Säcke‘' — so the root name, the label 'Indo-European' and the gloss 'sheep' are all right; Nourai merely drops the second half of the meaning. That half matters, because it is what ties Sanskrit meṣá- 'ram, fleece' and Avestan maēša- to Old Church Slavonic měxŭ 'skin bag, bellows', Russian mekh 'fur', Lithuanian maĩšas 'net, sack' and Old Prussian moasis 'bellows' — the semantic bridge being the sheepskin. Wiktionary reconstructs it as *moysós and glosses it 'ram, sheep' and 'sheepskin, fleece, wool'.\",\n   \"note_fa\": \"پوکورنی (ص ۷۴۷) این ریشه را «moiso-s یا maiso-s: گوسفند؛ پشم، پوست، و مشک و کیسه‌ای که از آن می‌سازند» آورده است؛ پس نامِ ریشه، برچسبِ «هندواروپایی» و معنای «گوسفند» در نمودار درست است و نورایی تنها نیمهٔ دومِ معنا را نیاورده. آن نیمه اهمیت دارد، زیرا همان است که سنسکریت meṣá- «قوچ، پشم» و اوستایی maēša- را به اسلاوی کلیسایی کهن měxŭ «مشک، دم آهنگری»، روسی mekh «پوستین»، لیتوانیایی maĩšas «کیسه» و پروسی کهن moasis «دم» می‌پیوندد؛ پلِ معنایی همان «پوستِ گوسفند» است. ویکی‌واژه این ریشه را *moysós بازسازی می‌کند با معناهای «قوچ، گوسفند» و «پوستِ گوسفند، پشم».\",\n   \"sources\": [W + \"Reconstruction:Proto-Indo-European/moys%C3%B3s\"],\n   \"ref_check\": [\n     {\"ref\": \"POK:747\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 407, line 6477: 'moiso-s oder maiso-s ‚Schaf; Fließ, Fell, daraus gefertigte Schläuche, Säcke‘. Ai. mešá- m. ‚Widder‘, mešī- ‚Schaffell‘, av. maēša- ‚Widder, Schaf‘ ...'; the database dump POK_full.txt confirms 'Root / lemma: moiso-s or maiso-s ... Page(s): 747'.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. II 303 (incoming/WLD/WLD_Bd2_pages.txt line 20020)\", \"stance\": \"supports\", \"note\": \"'moiso-s oder maiso-s ‚Schaf; Fließ, Fell, daraus gefertigte Schläuche, Säcke‘. Ai. meṣa- m. ‚Widder, Schafbock; Fell‘, av. maēša- ‚Widder, Schaf‘; abg. měchŭ ‚Schlauch‘ ... lit. maĩšas ...' — the source of Pokorny's own 'WP. II 303'.\"},\n     {\"src\": \"SYN\", \"where\": \"Buck §3.26 (RAM), printed p. 158 (SYN.txt leaf 191, whose running numeral is 158)\", \"stance\": \"supports\", \"note\": \"'6. Skt. meṣá-, Av. maēša- (alone or with varšni- ‘male’) ‘ram’, Skt. meṣī-, Av. maēšī- ‘ewe’, NPers. mīš ‘sheep’ : ChSl. měchŭ ‘bag made of skin’, etc., orig. ‘sheepskin’ or ‘skin’. Walde-P. 2.303.'\"},\n     {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt, grep 'moiso'/'maiso'\", \"stance\": \"silent\", \"note\": \"Watkins has no *moiso- root entry (the root left no English derivative), so the AHD appendix simply does not cover this root; it jumps from modhro- 747 to molko- 747.\"},\n     {\"src\": \"IEC\", \"where\": \"IEC.txt, grep 'moisos'/'maisos'\", \"stance\": \"silent\", \"note\": \"no entry found in Mann for this root.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"mâěša; mâěšî\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The forms are right and so is the descent, but the two glosses are swapped in emphasis. Avestan maēša- is a masculine noun 'sheep, ram' and maēšī- its feminine 'ewe' — Bartholomae, Altiran. Wb. col. 1109: 'j. maēša- m.; maēšī- f. ‘Schaf; Schafmutter‘', with Yt. 14.33 maēšahe kəhrpa aurunahe 'in the shape of a wild ram' and A. 3.7 maēšīnąm ... paiti.puθranąm 'ewes with young'; Buck p. 158 likewise 'Av. maēša- ‘ram’ ..., Av. maēšī- ‘ewe’'. Nourai's 'mâěšî : sheep' should therefore be 'ewe'. Phonologically maēša- is the regular Iranian outcome of PIE *moysós: *oy > Avestan aē, *s after the diphthong becomes š (ruki), Sanskrit meṣá- shows the same. The transliteration mâěša/mâěšî is Nourai's own convention (â for a, ě for e) and is printed that way in the book, so it is not a scanning error.\",\n     \"derivation_fa\": \"صورت‌ها و مسیرِ گشتِ آنها درست است، ولی جای دو معنا کمی جابه‌جا شده. اوستایی maēša- اسمِ مذکر «گوسفند، قوچ» است و maēšī- مؤنثِ آن «میشِ ماده» — بارتولومه (ستون ۱۱۰۹): «maēša- مذکر؛ maēšī- مؤنث: گوسفند؛ میشِ مادر»، با گواهِ یشت ۱۴/۳۳ maēšahe kəhrpa aurunahe «به پیکرِ قوچِ وحشی» و آفرینگان ۳/۷ maēšīnąm... paiti.puθranąm «میش‌های آبستن»؛ باک (ص ۱۵۸) نیز maēša- را «قوچ» و maēšī- را «میشِ ماده» می‌آورد. پس «mâěšî: sheep» در نمودار باید «میشِ ماده» می‌بود. از نظر آوایی maēša- برآمدِ منظمِ *moysós است: *oy در اوستایی aē می‌شود و s پس از دوواکه بر پایهٔ قاعدهٔ ruki به š بدل می‌گردد؛ سنسکریت meṣá- همین را نشان می‌دهد. آوانگاریِ mâěša/mâěšî شیوهٔ خودِ نورایی است (â برای a و ě برای e) و همان‌گونه در کتاب چاپ شده، پس خطای خوانشِ اسکن نیست.\",\n     \"sources\": [W + \"%D9%85%DB%8C%D8%B4\", W + \"Reconstruction:Proto-Indo-European/moys%C3%B3s\"],\n     \"ref_check\": [\n       {\"ref\": \"POK:747\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 407: 'av. maēša- ‚Widder, Schaf‘' under moiso-s/maiso-s, p. 747.\"},\n       {\"ref\": \"SYN:158\", \"status\": \"supports\", \"note\": \"SYN.txt leaf 191, running numeral 158 (Buck §3.26 RAM): 'Skt. meṣá-, Av. maēša- ... ‘ram’, Skt. meṣī-, Av. maēšī- ‘ewe’, NPers. mīš ‘sheep’'. Nourai's page number is exact (the offset drifts: leaf 191 = p. 158, not leaf−24).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"col. 1109 (BRT.txt \\\\f-leaf 617; the preceding leaf 616 carries the numeral 1108)\", \"stance\": \"partial\", \"note\": \"'• j. maēša- m.; maēšī- f. ‘Schaf; Schafmutter‘: ʻšahe kəhrpa aurunahe Yt. 14.33; ... ʻšīnąm damunąm (‘Schafmutter’) paiti.puθranąm A. 3.7. — ai. meṣá- m., meṣī- f.; mp. (Pü.), np. mēš.' Supports the pair but glosses maēšī- as 'ewe', not 'sheep'.\"},\n       {\"src\": \"NYB\", \"where\": \"vol. II Glossary s.v. mēš-sār (NYB_vol2_glossary.txt line 2544)\", \"stance\": \"supports\", \"note\": \"'mēš-sār ‚‘of the sheep category’ = of sheep-leather ... — Av. (1109) maēša-, NP mēš + sar' — an independent pointer to Bartholomae col. 1109 and to the Avestan-to-NP line.\"},\n       {\"src\": \"HRN\", \"where\": \"Horn no. 1008, printed p. 226 (HRN.txt leaf 247)\", \"stance\": \"supports\", \"note\": \"'1008. mēš ‘Schaaf, Widder’. aw. maēsa- ‘Schaaf, Schaafbock’; phlv. mēš; ai. mešá-.'\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"mîš; gâvmîš\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP میش mīš continues Middle Persian mēš (Book Pahlavi myš, e.g. in the compound mēš-sār 'of sheep-leather', MacKenzie 1971 and Nyberg II s.v.), from Old Iranian *maiša- = Avestan maēša-; the MP majhūl ē regularly becomes ī in New Persian spelling and in the modern standard pronunciation, which is exactly what Moʿin notes in his footnote on میش in Borhan: 'بکسر اول (تلفظ کنونی) و در تلفظ قدیم mēš، اوستایی maēša-' followed by the Baluchi, Wakhi and Sarikoli cognates. In current Persian میش is specifically the ewe (the ram being قوچ), so Nourai's 'ram' is a shade off; Horn's no. 1008 gives both senses ('Schaaf, Widder'). گاومیش gāvmīš 'water buffalo' is inherited as a whole from the Middle Persian compound gāw-mēš (PHD p. 38 'gāw-mēš [TWR Amyš | N gā(w)mēš] buffalo'), literally 'cow-sheep', a descriptive name for the animal introduced from India; the compound was borrowed out of Middle Iranian into Old Armenian գոմէշ gomēš, Syriac ܓܡܘܫܐ gāmōšā, Old Georgian ḳambeči and Arabic جاموس jāmūs. Ferdowsi's line quoted in the book (همه پایه‌ها چون سر گاومیش) shows the word in place by the 10th century.\",\n     \"derivation_fa\": \"«میش» بازماندهٔ mēš فارسی میانه است (در پهلوی کتابی myš، مثلاً در ترکیبِ mēš-sār «از چرمِ گوسفند»، مکنزی و نیبرگ)، و آن از ایرانی باستان *maiša- = maēša- اوستایی؛ ēِ مجهولِ فارسی میانه در فارسی نو به ی بدل شده است — و معین در حاشیهٔ «میش» در برهان قاطع همین را می‌گوید: «بکسر اول (تلفظ کنونی) و در تلفظ قدیم mēš، اوستایی maēša-» و سپس هم‌ریشه‌های بلوچی، وخی و سریکلی را می‌آورد. در فارسیِ امروز «میش» ویژهٔ گوسفندِ ماده است (نرِ آن «قوچ»)، پس «ram» در نمودار کمی نادقیق است؛ هرن (شمارهٔ ۱۰۰۸) هر دو معنا را آورده. «گاومیش» یکپارچه از ترکیبِ gāw-mēš فارسی میانه به میراث رسیده است (مکنزی، ص ۳۸)، تحتِ‌اللفظ «گاو-میش»، نامی توصیفی برای جانوری که از هند آمده بود؛ همین ترکیب از ایرانیِ میانه به ارمنیِ کهن գոմէշ gomēš، سریانی gāmōšā، گرجیِ کهن ḳambeči و عربی «جاموس» وام داده شده است. بیتِ فردوسی که در کتاب آمده («همه پایه‌ها چون سر گاومیش») نشان می‌دهد واژه در سدهٔ چهارم هجری جا افتاده بوده است. ادعای نورایی درست است.\",\n     \"sources\": [W + \"%D9%85%DB%8C%D8%B4\", W + \"%DA%AF%D8%A7%D9%88%D9%85%DB%8C%D8%B4\"],\n     \"ref_check\": [\n       {\"ref\": \"BQT:2078\", \"status\": \"supports\", \"note\": \"Borhan-e Qateʿ ed. Moʿin vol. 4, printed p. 2078 = pdf 161 (incoming/BQT/BQT_v4_pages.txt block 160): 'میش - بکسر اول ( تلفظ کنونی ) و در تلفظ قدیم mēš ، اوستایی maēša- ... (گاو میش) ، بلوچی ... وخی ... سریکلی ...' — both of Nourai's words and the Avestan source, on exactly the cited page.\"},\n       {\"ref\": \"HRN:226\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 247 = printed p. 226 (leaf = p+21): '1008. mēš ‘Schaaf, Widder’. aw. maēsa- ‘Schaaf, Schaafbock’; phlv. mēš; ai. mešá-; kurd. mī, miya; afgh. mēy ‘Mutterschaaf’, LW. mēš ‘Büffel’; bel. mēš.'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"PHD\", \"where\": \"MacKenzie p. 38 (PHD.txt leaf 59)\", \"stance\": \"supports\", \"note\": \"'ģāw-mēš [TWR Amyš | N gā(w)mēš] buffalo' — the Middle Persian compound behind گاومیش, with the Aramaic-script spelling TWR ('ox') + Amyš.\"},\n       {\"src\": \"NYB\", \"where\": \"vol. II Glossary s.v. mēš-sār\", \"stance\": \"supports\", \"note\": \"'Av. (1109) maēša-, NP mēš' — confirms the MP mēš stage and the NP outcome.\"},\n       {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. میش (Persian) and گاومیش\", \"stance\": \"supports\", \"note\": \"میش: 'From Middle Persian 𐭬𐭩𐭱 (mēš), from Old Persian *maišah, from Proto-Iranian *mayšáh, from Proto-Indo-European *moysós (“sheep, skin of sheep”)'; گاومیش: 'From Middle Persian (gāw-mēš, literally “cow-sheep”) ... Old Armenian գոմէշ (gomēš), Classical Syriac ܓܡܘܫܐ (gāmōšā) and Old Georgian კამბეჩი (ḳambeči) are borrowed from Middle Iranian languages.'\"},\n       {\"src\": \"SYN\", \"where\": \"Buck p. 158\", \"stance\": \"supports\", \"note\": \"'NPers. mīš ‘sheep’' in the maēša- group.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-340.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk340.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-340.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-07T17:57:07.560Z] TOOL RESULT

```
written
JSON OK
```


## [2026-09-07T17:57:11.457Z] TOOL CALL #83: Bash

```json
{
 "command": "python3 tools/verify_check.py 340"
}
```


### [2026-09-07T17:57:12.935Z] TOOL RESULT

```
nodes verified: 19/19
node verdicts: {'plausible': 6, 'confirmed': 11, 'disputed': 2}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 17, 'not_checked': 5, 'partial': 1}
books consulted: {'partial': 7, 'supports': 33, 'silent': 9, 'contradicts': 5} | by book: {'KLN': 9, 'Wiktionary': 6, 'NYB': 4, 'AHD': 4, 'Etymonline': 3, 'BRT': 2, 'IEC': 2, 'PHD': 2, 'POK': 2, 'SKT': 2, 'MON': 2, 'Wikipedia': 2, 'HUB': 1, 'BQT': 1, 'SOD': 1, 'HENNING': 1, 'FVQ': 1, 'ARY': 1, 'AFM': 1, 'LKT': 1, 'PHN': 1, 'DEV': 1, 'Wikipedia (fa)': 1, 'WEB': 1, 'HRN': 1, 'SYN': 1}
```


## [2026-09-07T17:57:20.834Z] TOOL CALL #84: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nv=json.load(open('data/verification/page-340.json'))\nurls=set()\ndef walk(o):\n    if isinstance(o,dict):\n        for k,val in o.items():\n            if k=='sources': urls.update(val)\n            else: walk(val)\n    elif isinstance(o,list):\n        for i in o: walk(i)\nwalk(v)\nidx=set()\nfor line in open('data/verification/sources/web/index.jsonl'):\n    try: idx.add(json.loads(line)['url'])\n    except: pass\nfor u in sorted(urls):\n    print('OK ' if u in idx else 'MISSING ', u)\nEOF"
}
```


### [2026-09-07T17:57:22.215Z] TOOL RESULT

```
OK  https://abadis.ir/fatofa/%D9%85%D9%84%D8%AD/
OK  https://en.wikipedia.org/wiki/M%C3%A1laga
OK  https://en.wiktionary.org/wiki/%CE%BC%CE%B1%CE%BB%CE%AC%CF%87%CE%B7
OK  https://en.wiktionary.org/wiki/%D7%9E%D7%9C%D7%97
OK  https://en.wiktionary.org/wiki/%D9%85%D8%B2%D8%AF
OK  https://en.wiktionary.org/wiki/%D9%85%D8%B2%D8%AF%D9%88%D8%B1
OK  https://en.wiktionary.org/wiki/%D9%85%D9%84%D8%AD
OK  https://en.wiktionary.org/wiki/%D9%85%DA%98%D8%AF%D9%87
OK  https://en.wiktionary.org/wiki/%D9%85%DB%8C%D8%B4
OK  https://en.wiktionary.org/wiki/%DA%AF%D8%A7%D9%88%D9%85%DB%8C%D8%B4
OK  https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/misd%CA%B0%C3%B3s
OK  https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/moys%C3%B3s
OK  https://en.wiktionary.org/wiki/meed
OK  https://fa.wikipedia.org/wiki/%D9%85%D8%A7%D9%84%D8%A7%DA%AF%D8%A7
OK  https://www.etymonline.com/word/malachite
OK  https://www.etymonline.com/word/mallow
```


## [2026-09-07T17:57:45.119Z] AGENT

Page 340 done — `data/verification/page-340.json` written, `verify_check.py 340` reports 19/19 nodes, 0 PROBLEM lines.

**Counts** — roots: 3 confirmed. Nodes: 11 confirmed, 6 plausible, 2 disputed. Ref checks: 17 supports, 1 partial, 5 not_checked. 54 `consulted` entries across 26 books (33 supports, 7 partial, 9 silent, 5 contradicts).

**Disputed**
- *M.l.h* #4 Latin `malva` — modern view (Watkins/AHD p. 39, Etymonline, Wiktionary) makes malva and Greek malakhḗ both loans from a pre-IE Mediterranean substrate, not from Hebrew *mallūaḥ*; and even on the Semitic hypothesis Latin would have gone via Greek. Klein p. 928 does say what Nourai says, but he is quoting H. Lewy 1895.
- *M.l.h* #6 Greek `malaxe` — μαλάχη/μολόχη with χ/κ variation is a Pre-Greek signature (Beekes, Chantraine); Wiktionary calls the etymology uncertain and objects that the Semitic *mallūaḥ* plants are Amaranthaceae, not Malvaceae, and that the proposal ignores Arm. բաղբակ / Georg. ბალბა.

**Notable `plausible` calls**
- *Miždho* #1: Av. `mîžda-vare` is unattested — Bartholomae has only mižda- and mižda-vant-; the form is retro-projected from MP *mizd-war* (PHD 59).
- *Miždho* #4: "medo" is West Germanic *mēdē- (as AHD prints); Proto-Germanic was *mizdō (Goth. mizdō).
- *M.l.h* #3: Heb. `mallŭh` is saltbush (Atriplex halimus), not mallow — the gloss is the KJV rendering of Job 30:4 that Klein passed on.
- *M.l.h* #8/#11: Málaga < 'salt' is the common but unproven theory (the Punic coin legend is mlkʾ with kaph); Persian مالاگا route via French unverifiable — Moʿin vol. 6 (aʿlām) is not digitised.
- *Moiso* #1: maēšī- is 'ewe' (Bartholomae col. 1109 "Schafmutter", Buck p. 158), not generic 'sheep'.

**Reference pages all confirmed exact**: POK 746/747, KLN 926/928/957, HRN 219/226, SOD 227 (page, not entry no.), SYN 158 (Buck §3.26 — note the SYN leaf offset drifts, leaf 191 = p. 158, not leaf−24), BQT vol. 4 p. 2000/2001 (مزد، مزدور; مژده with Moʿin's citation of Horn 978 is at p. 2005) and p. 2078 (میش/گاومیش). Not checkable: FVA:384 (Nahvi 1368 — no digital copy anywhere), MON6:1883 (Moʿin aʿlām volumes not scanned), AHD:1527 (1976 appendix not open; same entry located in the 1985 Watkins ed. p. 39).

**Extraction error for the owner (minor)**: node #2 of entry 0 has `"translit": "mozdůr"` (U+016F, u-with-ring); the printed page 340 clearly shows **mozdŭr** with a breve (U+016D), the same glyph the extraction rendered correctly as `mallŭh` in entry 1. Everything else on the page — including `mâěša`/`mâěšî`, `mîžda-vare`, the Persian script and the `FVA:384` refs — matches the printed page exactly.
