# Verification process log — verify-page-130


## [2026-09-05T20:02:40.732Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 130 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-130.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-130.json. Write /home/sfmqrb/git/rishe/data/verification/page-130.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 130` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:02:42.512Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:02:43.289Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


## [2026-09-05T20:02:43.315Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-130.txt"
}
```


### [2026-09-05T20:02:43.394Z] TOOL RESULT

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


### [2026-09-05T20:02:43.404Z] TOOL RESULT

```
1	=== PDF page 130 (book page 100) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dheu 2, Dhu, Dhu-bh : smoke, mist, dizziness, dull color  (refs POK:262)
4	#1 (parent #0) [Avestan] refs=POK:262 | dvaidi 1 : smoke
5	  #2 (parent #1) [Pahlavi] refs=HRN:129; POK:262; BQT:894 | dŭd : smoke ; dŭtak-mân : smoke house, also family members sitting around fire in their house ☞Dem
6	    #3 (parent #2) [Persian] refs=BQT:894; HRN:129 | dŭd «دود» : smoke ; dŭdeh «دوده» : soot ; dŭdmân «دودمان» : family
7	#4 (parent #0) [Avestan] refs=POK:262; BRT:688 | dav 1 : press ; dvaidi 2 : we both press | NOTE: Neither POK nor BRT are certain about this derivation
8	  #5 (parent #4) [Avestan] refs=BQT:172 | han-davathe : pressed together, depressed. ☞Sem 1
9	    #6 (parent #5) [Persian] refs=BQT:172 | andŭh «اندوه» : sorrow ; andŭhgîn «اندوهگین» : sorry
10	#7 (parent #0) [Greek] refs=AHD; KLN:1670 | tuphein : to make smoke ; tuphos : smoke ; tuphun : typhoon
11	  #8 (parent #7) [Latin] refs=None | 
12	    #9 (parent #8) [French] refs=None | 
13	      #10 (parent #9) [Persian] refs=MON:1181 | tîfŭs «تیفوس» : typhus ; tîfoîd «تیفوئید» : typhoid
14	    #11 (parent #8) [English] refs=AHD | typhus, typhoid
15	  #12 (parent #7) [Arabic] refs=KLN:1670; SKT:581 | tŭfân : hurricane, typhoon
16	    #13 (parent #12) [Persian] refs=MON:2240 | tŭfân «طوفان» : typhoon, rain
17	    #14 (parent #12) [English] refs=SKT:581 | typhoon | NOTE: KLN:1670 derives it from a Chinese root but indicates that it is influenced by the Arabic word "tŭfân".
18	#15 (parent #0) [Latin] refs=AHD | fŭmus : smoke
19	  #16 (parent #15) [English] refs=None | fume, perfume
20	#17 (parent #0) [Germanic] refs=AHD | 
21	  #18 (parent #17) [English] refs=None | dizzy, deaf, dumb, dull, deer, dust, dove
22	
```


## [2026-09-05T20:02:46.652Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-130.json && echo \"=== MATRIX ===\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source JSON and source matrix"
}
```


### [2026-09-05T20:02:46.715Z] TOOL RESULT

```
{
  "pdf_page": 130,
  "book_page": 100,
  "entries": [
    {
      "root": {
        "name": "Dheu 2, Dhu, Dhu-bh",
        "lang": "Indo-European",
        "refs": "POK:262",
        "gloss": "smoke, mist, dizziness, dull color"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:262",
          "words": [
            {"translit": "dvaidi 1", "gloss": "smoke", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:129; POK:262; BQT:894",
          "words": [
            {"translit": "dŭd", "gloss": "smoke", "script": null},
            {"translit": "dŭtak-mân", "gloss": "smoke house, also family members sitting around fire in their house", "script": null, "see": ["Dem"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:894; HRN:129",
          "words": [
            {"translit": "dŭd", "gloss": "smoke", "script": "دود"},
            {"translit": "dŭdeh", "gloss": "soot", "script": "دوده"},
            {"translit": "dŭdmân", "gloss": "family", "script": "دودمان"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "بدو گفت رو پیش دستان بگوی - کزاین دودهٔ سام شد رنگ و بوی",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:262; BRT:688",
          "words": [
            {"translit": "dav 1", "gloss": "press", "script": null},
            {"translit": "dvaidi 2", "gloss": "we both press", "script": null}
          ],
          "script_extra": null,
          "note": "Neither POK nor BRT are certain about this derivation",
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Avestan",
          "refs": "BQT:172",
          "words": [
            {"translit": "han-davathe", "gloss": "pressed together, depressed.", "script": null, "see": ["Sem 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT:172",
          "words": [
            {"translit": "andŭh", "gloss": "sorrow", "script": "اندوه"},
            {"translit": "andŭhgîn", "gloss": "sorry", "script": "اندوهگین"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD; KLN:1670",
          "words": [
            {"translit": "tuphein", "gloss": "to make smoke", "script": null},
            {"translit": "tuphos", "gloss": "smoke", "script": null},
            {"translit": "tuphun", "gloss": "typhoon", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "MON:1181",
          "words": [
            {"translit": "tîfŭs", "gloss": "typhus", "script": "تیفوس"},
            {"translit": "tîfoîd", "gloss": "typhoid", "script": "تیفوئید"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 8,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "typhus, typhoid", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 7,
          "lang": "Arabic",
          "refs": "KLN:1670; SKT:581",
          "words": [
            {"translit": "tŭfân", "gloss": "hurricane, typhoon", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "MON:2240",
          "words": [
            {"translit": "tŭfân", "gloss": "typhoon, rain", "script": "طوفان"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "حافظ از دست مده دولت این کشتی نوح - ورنه طوفان حوادث ببرد بنیادت",
            "poet": "Hâfez"
          }
        },
        {
          "id": 14,
          "parent": 12,
          "lang": "English",
          "refs": "SKT:581",
          "words": [
            {"translit": "typhoon", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": "KLN:1670 derives it from a Chinese root but indicates that it is influenced by the Arabic word \"tŭfân\".",
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "fŭmus", "gloss": "smoke", "script": null}
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
            {"translit": "fume, perfume", "gloss": null, "script": null}
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
          "words": [],
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
            {"translit": "dizzy, deaf, dumb, dull, deer, dust, dove", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
=== MATRIX ===
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


## [2026-09-05T20:03:14.869Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','MON','HRN','BRT','AHD','KLN','SKT','PHD','NYB','HUB','FVQ','CHEUNG','ARY','LKT','WLD','IEC','SYN','LEW','LAT','AFM','PLA','TAD','ARB']:\n    v=d.get(k)\n    print('==',k,json.dumps(v,ensure_ascii=False)[:700])\n\""
}
```


### [2026-09-05T20:03:16.584Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 
== CHEUNG null
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pag
== ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt", "/home/sfmqrb/git
```


## [2026-09-05T20:03:20.455Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 269 270 271 272; do echo \"########## leaf $n (printed ~$((n-8)))\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' POK_01.txt | head -80; done"
}
```


### [2026-09-05T20:03:22.432Z] TOOL RESULT

```
########## leaf 269 (printed ~261)
  (dherobh-?)  ,arbeiten'.
Arm.  derbuk  ,rough,  stiff,  rüde';
ags.  deorfan  st.  V.  ,arbeiten;  umkommen',  gedeorf  n.  ,  Arbeit,  Mühsal', afries.  for-derva,  mnd.  vor-derven,  mhd.  verderben  ,umkommen',  auch  Kaus. ^verderben';
lit.  dirbu,  dirbti  , arbeiten',  ddrbas  , Arbeit',  darbüs  ,arbeitsam'.
WP.  I  863,  II  631,  Klügelt  101,  649,
dherebh'  , gerinnen,  gerinnen  machen,  ballen,  dickflüssig'.
Ai.  drapsd-h  m.  ,Tropfen'??;
gr.  TQeqisad-ai,  Tstqocpevai  ,gerinnen,  fest  sein',  XQecpu),  dor.  rgdcpco  , mache gerinnen  (ydXa]  tvqöv),  nähre  (*mache  dick,  feist),  erziehe'  (^QeipWy  ed-gstpa), tQocpög  ,nährend',  f.  ,Amme',  d-qe^if-ia  ,das  Genährte,  Pflegling,  Kind, Zuchtvieh',  TQOcpig  ,feist,  stark,  groß',  TQOcpallg^  -Idog  , frischer  Käse,  ge- ronnene Milch',  Taocpvg  , dicht',  rdgcpea  PI.  n.  , Dickicht',  TQacpeqr]  (yfj) ;festes  Land';
nasaliert  und  mit  idg.  b  (idg.  Artikulationsschwankung  in  nasaler  Um- gebung) d-QOi-ißoq  ,geronnene  Masse  (von  Milch,  Blut  usw.)',  ^go^ßdof-iai jgerinne',  d-QOfißeTov  ,Klümpchen';
17
268
as.  derli   (*dartia)  ^kräftig;   böse^^   afries.   mnd.   derve  ^derb,   gerades (verschieden  von  ahd.  derh  ^ungesäuert'  =  anord.  pjctrfr),  ablaut.  anor^ djarfr  , mutig,  kühn'  (die  ältere  Bed.  noch  in  norw.  dial.  dirna  aus  *c?iVa3I ^zunehmen;,  wieder  zu  Kräften  kommen');  anord.  dirfa  , ermutigen';
nasaliert  wohl  anord.  dramh  , Übermut'  (*dick  sein),  nisl.  dramhr  ,Knoteni im  Holz';  anord.  drumhr  , Klotz';  mnd.  drummel  ^gedrungene  Person'.
WP.  I  876.
dheregh-  mit  Formans  -(e)s-  und  -no-  in  Namen  beerentragender  strau- chiger Pflanzen,  bes.  auch  von  solchen  Dornsträuchern,  woraus  z.  t1 ,Dorn'?    Zweifelhafte  Gleichung.
Ai.  dräksä  ,Weintraube';
gallorom.  *dragenos  ,Dorn*,  air.  draigen  m.  , Schlehdorn*,  cymr.  drae^ m.,  nbret.  di^ean  , Dornstrauch'  (kelt.  "^drageno-  aus  *dhr^gli-)'^
vielleicht  auch  ahd.  tirn-pauma  ,cornea  silva*,  tyrn,  dirnhaum  ,cornus*^^ nhd.  dial.  di(e)rle,  dirnlein  ,Kornelkirsche',  Schweiz,  tierlij  falls  nicht! aus  dem  Slav.  in  sehr  alter  Zeit  entlehnt;
lit.  dngnes  PL,  lett.  drigenes  ,schwarzes  Bilsenkraut'  (vgl.  Mühlenbach-1 Endzelin  I  498),    falls  nicht  aus  dem  Slav.  entlehnt;
russ.  dereuj  deren  , Hartriegel,  Kornelkirsche',  skr.  drijen,  öech.  drin  ds. poln.  (alt)  drzon  jBerberitze',  kaschub.  drbn  , Dornen',  polab.  dren  ,Dorn'.
Germ.-sl.  Grundf.    kann   "^dherghno-   sein    und    stünde    dem   freilich   in seiner   Bed.    , Schößling,    Zweig',    PL  ,junges    Gebüsch'    erheblich    anders- gefärbten gr.  TQ€xyog  (Hes.,  anthoL),  tsqxvoq  (Maximus),  kypr.  t«  zsQxvija  ^  • sehr  nahe.
WP.  I  862  f.,  Pedersen  KG.  I  97,  M.-L.  2762.
dheregh-  {dhrgh-nä-)  , drehen,  winden,  wenden'  (auch  , spinnen,  nähen*).
Npers.  darz,  darza  ,Naht*,  darzmän,  darznän  , Faden*,  darzan  ,NadelV pehl.  darzik  , Schneider';
arm.  dafnam  (*darjnam),  Aor.  darjay  ,sich  wenden,  sich 
########## leaf 270 (printed ~262)
 drehen,  sich kehren;  zurückkehren*,  dafn  , bitter,  herbe*  (vgl.  oivog  zgerrsTac  u.  dgl.), darj  jWendung,  Umkehr,  Rückkehr*,  Kaus.  darjucanem  ,verto,  averto, converto,  reddo*;
alb.  dreth  (St.  *dredh-),  Aor.  drodha  ,umdrehen,  zusammendrehen, zwirnen,  spinnen*,  alb.-skutar.  nnrize  ,Windel*  (n-dred-ze)-  nach  Pedersen Hitt.  123,  125,  Toch.  Spracbg.  20  hierher  hitt.  tar-na-ah-hi  ,ich  stecke ein,  lasse  hinein*,  toch.  A  tärnä-,  tärk-,  Prät.  A  cärk,  B  carka  , lassen, entlassen'  (?).
WP.  I  863,  Liden  Arm.  St.  101  ff.,  Meillet  Esquisse^  111,  Kuiper  Nasal- präs. 151.  '^^
259
dbers'  , wagen,  kühn  sein',  älter  ,angreifen,  losgehen*  (auch  mit  -i-,  -u- erweitert).
Ai.  dhrs-nö-ti,  dhdrs-ati  ,ist  dreist,  mutig,  wagt',  ährsü-  (Gramm.),  dhrsat Jierzhaft'  (=  av.  dard^at),  dhrsnii-  ,kühn,  tapfer,  mutig,  dreist,  frech', dhfstd-  ,keck,  frech',  dhfsüa-  ,kühn,  mutig',  dädhrsi-  ,beherzt,  kühn',  mit Objekt  dharsayati  ,wagt  sich  an,  vergreift  sich,  bewältigt',  dharsana-  n. , Angriff,  Mißhandlung',  dharsaka-  ,angreifend,  über  etwas  herfallend';  av. darsam  Adv.  ,heftig,  sehr',  darsi-,  darsyu-,  darsita-  ,kühn',  apers.  adar^- nau§  ,er  wagte',  dädarsi-  EN;
gr.  lesb.  -d-sgaog  n.  ,Mut,  Kühnheit'  (hom.  QsgalTrjg  ,Frechling'),  mit aus  dem  Adj.  verschleppter  Tief  stufe  ion.  altatt.  d^ccQOog  (att.  ^agoog)  ds., att.  d-gdaog  n.  ,Mut,  Kühnheit;  Verwegenheit,  Frechheit',  d-aqüeu),  d^aggeo) ,bin  mutig',  S-agavg  (rhod.  QaQGvßiog,  ther.  Qhagvfxaqhog),  d-gaavg  ,kühn, mutig;  verwegen,  frech'  (=  ai.  dlifsu-),  lesb.  Adv.  -S^goaecjg,  Mgavvog mutig,  getrost,  vertrauend'  (*-9-ag(To-avvog)]
lat.  infestus  , feindlich*,  infestäre  , feindlich  behandeln,  angreifen'  und manifestus   , handgreiflich,   auf  der  Tat  ertappt;    offenkundig'   (*dhers-to-)]
got.  ga-dars  ( :  ai.  Ferf .  dadhdrsa  ,hat  sich  erkühnt'),  Inf.  gadaürsan,  ,ich wage',  as.  gidurran,  ags.  dear^  durran,  ahd.  {gi)tar,  (gi)turran  ,wagen',  ahd. giturst,  ags.  gedyrst  f.  , Kühnheit,  Verwegenheit'  (=  ai.  drsti-h  ,Kühnheit');
lit.  nasaliert  lit.  dresü  ,wage*  (*dhrensö),  dristü,  dristi  {dhrns-)  , wagen', drqsä  (*dkrons-)  , Dreistigkeit',  di-qsüs  =  lett.  drüoss  ,mutig'  (*dhrons-j alit.  noch  drisüs  und  draiisniaus)]  ohne  Nasalierung  apr.  dirstlan  , stattlich* und  dyrsos  ,tüchtig'  (*dirsu-);
hierher  vielleicht  toch.  A  ^sär  ,rauh',  tsrasi  , stark',  B  tsirauüe  , Stärke*.
WP.  I  864,  WH.  I  698  f.,  Trautmann  60,  Van  Windekens  Lexique  147.
dbes-,  dhos-  in  religiösen  Begriffen.
Arm.  di'Jt  , Götter*  (PI.  *dheses)',  lat./eWae  (alat. /esiae)  ,Tage,  an  denen kei
########## leaf 271 (printed ~263)
ne  Geschäfte  vorgenommen  wurden,  Feiertage*,  festus  ,f estlich,  feier- lich, ursprüngl.  von  den  der  religiösen  Feier  gewidmeten  Tagen',  osk. fiisnam  Akk.  ,templum',  umbr.  fesnaf-e  ,in  fanum'*,  tiefstufig  lat.  fänum {*fas-no-m)  , heiliger,  den  Göttern  geweihter  Ort'  und  ai.  dhisnya-  , an- dächtig, fromm,  heilig'  (unsicherer  dhisanyant-  u.  dgl.,  s.  unter  dheid- , sehen');  über  gr.  d-eog  ,Gott'  s.  unter  dheues-,  über  lat.  fäs,  fästus  oben S.  105f.
WP.  I  867,  WH.  I  453,  3 f.;  EjVP  333,  347 f.
X.  dbeu-  ,laufen,  rinnen*.
Ai.  dhdvate  , rennt,  rinnt',  dehnstufig  dhdvati  ds.,  dhäuti-h  f.  , Quelle, Bach*;  mpers.  davfidan  ,laufen,  eilen*,  päm.  dav-  ,laufen,  rennen';
17*
260
gi\   ^€w,   ep.   auch   x^siu),  Fut.   d^£vaoy,ai  , laufen*;   lak.    af]'  rqixe   Hes; ^oög  , schnell',  ßorj-^öog  ,auf  einen  Anruf  schnell  zur  Hand,  helfend*,  daznl ßotjd-iü)   (statt   *ßorjdo€Cü)  , helfe',    ^oaCu)   ,versetze  in  schnelle  Bewegun, bewege  mich  schnell';
gr.-illjr.  dvdv'  ytgrjvrjv  Hes.;
anord.  dgggy  Gen.  dggguar  {*dawwo),  ags.  deatü,  as.  dau^  ahd.  to\i^  n} Tau  (*dawioa-)',
unsicher  mir.  döe  ,Meer'  (*dheuiä)  als  ,das  heftig  Bewegte';
hierher  wohl  *dhu-rO'  im  thrak.  FIN  ^A-d^vqag  (^n-dhu-r-)  und  in reichen  ven.-illyr.  FIN,  so  illyr.  Duria  (Ungarn),  nhd.  Tyra,  Thur,  äh Dura   (Elsaß,  Schweiz),    oberital.  Dora,  Doria,    frz.   Dore,    Doire,   Don iber.  Durius,    Turia  usw.   (Fokorny  Urill.  2,  10,  79,  105,  113,  127,  145^ 160,  165,  169  f.);
nach  Rozwadowski  (Rev.  Slav.  6,  58  ff.)  hierher  der  FIN  Düna,  wes slav.  Dvina  (*dhueinä),  als  finn.  väinä  ,breiter  Fluß*,  estn.  väin(a)  ,Sund* syrj.  'dyn  »Mündung*  entlehnt. .   WP.  I  834.
2,  dbeu-,  dbu-ei-  , hinschwinden,  bewußtlos  werden,  sterben*.
Got.  diwans  (*dheu-ono-) , sterblich*,  ablaut.  ahd.  touiven,  as.  döian  , sterben*, anord.  deyja,  dö  (*döw),  däinn  ,sterben';  got.  daups  ,tot*,  auch  af-dauipt ,geplagt',  ahd.  töt^  ags.  dead,  anord.  daudr  ,tot*,  got.  dau^us  ,Tod',  ahd. töd,  ags.  deaj)^  anord.  daud-r,  -ar  und  daude  ,Tod*;
air.  duine  (*dliu-n-io-),  PI.  döini  (*dheuen-{o-),  cymr.  dyn,  corn.  bret. den  , Mensch*  (.Sterblicher*,  Brugmann  ZfceltPh.  3,  595 ff.);  s.  auch  unter ghdem-]
vielleicht  lat. /wnws  (fönus?)  n.  , Leichenbegängnis,  Bestattung',  fallsaus *dheu{e)-nos  ,auf  den  Tod  bezügliche  Erweisung';  formell  jedoch  genau =  air.  n.  5-Stamm  dün  , Festung',  wohl  ursprüngl.  ,Burghügel'  (s.  unter 4.  dheu-  S.  263);
nach  Marstrander  Pres,  a  nasale  inf.  15^  hierher  air.  -deda  , seh  windet dahin'  aus  *dhe-dhu-ä-t]  vgl.  auch  oben  unter  3.  dhe-]
im  Germ,  auch  die  Bed.  , fühllos,  ohnmächtig  werden*,  awnord.  da {*dawa)  , Bewußtlosigkeit,  Ohnmacht*,  Prät.  dö  auch  , wurde  gefühllos' (von  Gliedern),  aschwed.  däna  ,in  Ohnmacht  fallen*,  norw.  daana  , steif, lahm  werden  (von  Gliedern),  in  Ohnmacht  fallen'  (Ableit.  vom  Partiz. dainn), 
########## leaf 272 (printed ~264)
 isl.  dodl  , Gefühllosigkeit*,  dodna  ,gefühllos  werden*,  got.  usdaupt ,im-piger,  eifrig',  ahd.  tawalön  ,hinschwinden,  hinsterben*,  ndl.  dauwel jträges  Weib*;  ferner  anord.  cZä  auch  »Entzückung  der  Seele*  (,*Betäu bung'),  da  (*dawen)  , bewundern';  anord.  dan  f.  ,Tod'.
3'
261
Erweiterung-  dhu-ei-  :  dhu-i-  in:
arm.  di^  Gen.  dioy  , Leiche,  Leichnam',  air.  dlth  {*dhuUu-)  ,Ende, Tod';  ag-s.  dwlnan  (st.  V.)  ,abnehmen;  schwinden',  neben  dem  7iöM-Verb anord.  duma  und  duena  ds.;  ags.  dwcescan  , auslöschen'  (*dwaiskjan),  lit. (/i?i5<i  ,erlöschen'  (Büga  bei  Endzelin  KZ.  52,  123).
WP.  I  835,  WH.  I  451,  568.
dbeu-  , blank,  glänzen'.
Ai.  dhavald-  ,glänzend  weiß',  dJiävatl  ,macht  blank,  reinigt,  spült',  av. fraöavata  ,rieb  sich  (reinigend)  ab';
gr.  ^oög' . . .  Xa^TtQÖg^  d^owaau  •  . . .  XaiinQvvai  Hes.,  ddoVreg  X«t;xci:  -^iovreg Ps.-Hsd.,  S^alsiov  xad-agöv.   xal  d-coUov  Hes.  (Kontr.  aus  *^oJ^aUog).
WP.  I  835,  Schulze  KZ.  29,  260  f.  =  Kl.  Sehr.  369.
4.  dheu-,  dheuO'  (vermutlich:  dhue-,  vgl.  dio  Erw.  dhue-k-,  dhä-s-)  ,stieben, wirbeln,  bes.  von  Staub,  Rauch,  Dampf;  wehen,  blasen,  Hauch,  Atem; daher  dampfen,  ausdünsten,  riechen,  stinken;  stürmen,  in  heftiger, wallender  Bewegung  sein,  auch  seelisch;  in  heftige,  wirbelnde  Bewe- gung versetzen,  schütteln';  Nominalbildungen:  dhü-li-,  dhü-mo-.
Mit  lü-Formantien:
Ai.  dhUmd-h  m.  ,Rauch,  Dampf,  dhümäyati  , raucht,  dampft'  =  lat. fümäre,  formell  auch  =  ahd.  tümön  ,sich  im  Kreise  drehen*;
gr.  d^vixog  ,  Gemüts  Wallung,  Leidenschaft,  Mut*  (dvi^iao)  noch  rein  sinn- lich , rauche,  räuchere';  ■d-Vf.idX-ajip  , Kohlenmeiler',  d-^i.av.ög  , leidenschaftlich*, d^v^aivo)  , zürne*  usw.);
lat.  fümus  , Rauch,  Dampf,  Qualm,  Brodem'  (fümäre  s.  oben);
lit.  dnmai  PI.  , Rauch',  lett.  dumi  PL,  apr.  dumis  ds.;
aksl.  dyrm  , Rauch*;
mit  ü:  mir.  duynacha  PL  ,Nebel'  (nir.  dumhach  aus  *dhumuko-  , neblig, dunkel');  gr.  d-^^og,  -ov  , Thymian'  (starkriechende  Pflanze  wie  auch O^vußgay  d-vi^ßgov  ,Satureja  thymbra  L.'  s.  Boisacq  m.  Lit.;  nach  Nieder- mann Gl.  19,  14  zu  russ.  dubrdvka,  dubrövka  ,Potentilla  Tormentilla', das  nach   Berneker  215  zu    aksl.  dgmh^  , Eiche'  [s.  unten  S.  264]  gehört).
Lat.  ßmus  ,Mist,  Dünger'  (als  *dhu-i-mos  auf  Grund  von  suffio^  -Ire erwachsen);
mit   idg.  ou:    ahd.    toum    , Dampf,    Dunst,  Duft',   as.   dömian   , dampfen'.
Dazu  Farbenadjektive  der  Bed.  ,rauchfarben,  nebelgrau,  düster*:  ai. dhümrd-  ,rauchfarben,  grau,  braunrot,  trüb  (auch  vom  Verstand)',  dhümala- .rauchfarben,  braunrot';
lit.  dumhlas  , Schlamm,  Moor  auf  dem  Grund  eines  Teiches',  lett.  duhl'i , Schlamm,    Kot'    (vermutlich  =  ai.  dhümra-]    vgl.  aber  unten  S.  268  und
262
Mühlenbach-Endzelin  I  509),  lett.  dümal'§  , dun
```


## [2026-09-05T20:03:31.707Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 273 274; do echo \"########## leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' POK_01.txt; done"
}
```


### [2026-09-05T20:03:33.384Z] TOOL RESULT

```
########## leaf 273
kelfarbig,  braun',  düma% ,rauchfarben',  dumjs,  fem.  dumja  , dunkelbraun,  fabl,  trüb  (von  den  Auge^! dumm*,  dumühsnis   , Sumpf,  dumhra  zeme   ,schwarzes  Moorland',   duThhr^ duffibrs  , Quelle,  Moor,  Morast'  (vgl.  Mühlenbach-Endzelin  I  514;  ausfübrlic}^ über  solche  Moorbezeichnungen  nach  der  Farbe  Schulze  Kl.  Sehr.  X\^,
vgl.  mit   dem   Farbnamensuffix  -no-:   lett.    duni,   dünas  PL    , Schlamm''
mit  'ko-,  bzw.  von  der  Wurzelerw.  mit  -k-:  lett.  düksne,  dükste  , Sumpf Pfuhl,  MovsisV  :  dükans  , Schweißfuchs,  dunkelfarbig';
mit  -g-:  lett.  duga  , zäher  Schleim,  der  auf  dem  Wasser  schwimmt' dugains  üdens  , unreines  Wasser',  d.  uguns  , dunkle,  getrübte  Flamme* dungans  , Schweißfuchs'  (wenn  letzteres  nicht  aus  *dumgans,  vgl.  balgar^ , weißlich',  salgans  , süßlich');
mit  -t-  toch.  B  tute  ,gelb'?
Mit  i-Formantien:
Ai.  dhüli-,  dhüll  f.  , Staub,  staubiger  Erdboden,  Blütenstaub',  dhülika ,Nebel',  alb.  delenje  , Wacholder'  (als  ,Räucherholz',  aus  *dhülimo-),  lat, fühgo  ,Ruß',  mir.  düil  , Wunsch,  Begehr'  (*Gemütswallung,  wie  ^v^ög), lit.  dulis  m.  ,Räucherwerk  zum  Forttreiben  der  Bienen',  dülke  ,Stäubchen', lett.  düläjs,  dülejs  ,mehr  rauchende  als  brennende  Fackel  zum  Honigaus- nehmen'; lit.  didsvas  ,rauchfarben,  mausgrau';  ablautend  russ.  dülo  ,Mün- dung  (eines  Gewehrs,  einer  Kanone'),  dühce  , Mundstück  eines  Blasinstru- ments'  (usw.,  s.  Berneker  237;   erst   slav.  Ableitungen  von  duti  , blasen').
Verba  und  einzelsprachliche  Nominalbildungen:
ai.  dhünöti  {dhunöti,  dhuvdti)  ^schüttelt,  bewegt  hin  und  her,  facht  an', Fut.  dhavisyatij  Perf.  dudhäva,  Pass.  dhüydte,  Partiz.  dhutd-h,  dhütd-h  " ,geschüttelt^,  mpers.  dlt  , Rauch';  ai.  dhunäti  ,bewegt  sich  hin  und  her, schüttelt',  Partiz.  dhünäna-,  dhüni-  f.  ,das  Schütteln',  dhünayati  ^bewegt hin  und  her,  schüttelt^,  dhavitram  n.  ,Fächer,  Wedel',  dhavitavyä-  ,anzu- fächeln';  av.  dvaidi  ,wir  beide  bedrängen'?  {*du-vaidl)'^  Kuiper  Nasalpräs. 53  stellt  hierher  ai.  dhvajati  (Dhp.  7,  44),  av.  dvazaiti  , flattert^  (dazu  ai. dhvajd-h  ,Fahne')  aus  *dhu-eg- (?)',
arm.  de-dev-im  , schwanke,  schaukle'  (vgl.  das  ebenfalls  redupl.  Intensiv dhvajd-h  ai.  dö-dhavUi);
gr.  d-icü  (ßdvaa),  lesb.  d^vio) , stürme  einher,  brause,  tobe,  rauche'  {*dhu-iö, V  aus    d^awj   edvaa,   wie   auch   ü   im   ai.  Pass.  dhüydte   und   anord.  dyja    g ,schütteln'   Neubildung   ist;    in   der   Bed.   ,rase'   vielleicht   aus  *dhusiö,  s.  /^ dheues-),  ^vduj,  dvd^w  ds.,  MeXka  ,Sturm'  (s.  S.  269  unter  dheues-),  ep.  divot  j% ,fahre  einher,  stürme  daher^  {^d-vvJ^w),  d^Vvew  ds.  {^-^viifu)),  ^vvog'  ndh- fiOQy    ÖQ^irj,    ÖQÖLiog   Hes.    Mit   der   Bed.    , rauchen    (Rauchopfer),   riechen': -d^Vü)    (^ö-w),    Ts&vyta    ,opfere',    -d-vaia  , Opfer',    ^
########## leaf 274
i(j,cc    ,Opfertier^,  ^vog  n. , Raucher  werk  (daher  lat.  tüs),  Opfergabe,   Opfer'  (davon  ^veia  ,Mörser'?
263
s.  Boisacq  m.  Lit.),  &vÖ£Lg,  d-vrjSiq  ,von  Opferdarapf  oder  Räucherwerk duftend';  S-vov  ^ein  Baum,  dessen  Holz  wegen  seines  Wohlgeruches  ver- brannt wurde',  dv'ia,  &va  ^Thuja',  ^vrilrj  , Opfergabe'  (:ion.  d-valrj^iara -. att.  ^Irj^ccra,  ^^fa-i'^^v-,  s.  Bechtel  Lex.  168  f.,  Boisacq  s.  v.),  dvy,ih] Opferstätte,  Altar'.
Auf  Grund  der  Bed.  , (zusammen) wirbeln'  d-tg,  ^ivög  , Sandhaufen,  bes. Düne,  Gestade,  Sandbank,  Haufen  überhaupt',  aus  ^d-f-iv,  gebildet  wie a-A-ttv-,  yliotiv-,  ösXcptv-,  chötv-,  vgl.  gr.  ^iXa  ,Haufen'  (Hes.),  zur  Bed. unten  nhd.  Düne;  kaum  mit  Schwyzer  Gr.  Gr.  I  570 ^  zu  ai.  dhisnya-  ,auf einen  Erdaufwurf  aufgesetzt';
alb.  geg.  dej,  tosk.  denj  ,berausche',  Med.  ,schwinde  dahin,  schmelze' (*deuniö,  vgl.  got.  dauns  , Dunst'),  dejet  ,fließt,  schmilzt';
lat.  siif-fiö,  -flre  , räuchern'  {sufflmentum  ,Räucherwerk';  über  fimus s.  oben)  aus  *-dhu-nö,  wie  fio  ,werde'  aus  ^hhu-iiö,  foeteo,  -ere  ,übel  riechen, stinken'  auf  Grund  eines  Partiz.  *dJm-oi-to-s  (wie  püteö  von  *pütos)]
hierher  (als  *Aufgeschüttetes)  gall.,  urir.  Jovvov,  latin.  dünum,  air.  n. «-St.  dün  (:lat.  fünus,  s.  S.  260)  ,Burg'  (*Hügel),  acjmr.  din  (ncymr. dinas)  ds.;  air.  dü[a)e,  arch.  doe  ,Wall'  (*dhöuio-);  air.  dumae  m.  , Hügel', gall.  GN  Dumiatis]  auch  air.  de  f.  Gen.  d'lad  , Rauch',  mir.  dethach  ds. (^*dhuiiat-) ;
ags.  dün  m.  f.  ,Höhe,  Berg',  engl,  down  , Sandhügel,  Düne',  mnl.  düne, mnd.  düne,  daraus  nhd.  Düne]  vgl.  zur  Bedeutung  klr.  vy-dma  ,Düne'  zu slav.  d^mq  , blase';  hingegen  ist  germ.  *tü-na-  ,Zaun,  eingehegter  Platz' (aisl.  ags.  tun  ds.,  , Stadt',  nhd.  Zaun)  wohl  kelt.  Lw.;
anord.  dyja  ,schütteln'  s.  oben;
got.  dauns  f.  , Geruch,  Dunst'  (*dhou-ni),  anord.  daunn  m.  , Gestank' (vgl.  alb.  dej]  über  ahd.  nhd.  dunst  s.  unter  der  Wurzelform  *dheues-); anord.  dünn  m.  , Daune  (daraus  mnd.  düne^  wovon  wieder  nhd.  Daune] vgl.  mndl.  donst  ,Daunen,  Staubmehl'  =  dt.  Dunst]  s.  Falk-Torp  u.  dum,)] as.  dununga  ,deliramentum'  (u  oder  «?);  aisl.  düni  ,Feuer';
lit.  dujä  f.  ,Stäubchen',  duje  ,Daune';  dvylas  , schwarz,  schwarzköpfig, vom  Rinde',  ablaut.  dülas  , fahlgrau';
slav.  *dujg,  *duti  (z.  B.  russ.  düju,  duth)  ,blasen,  wehen',  ablautend *dyjg  in  sloven.  dijem,  diti  , wehen,  duften,  leise  atmen' ;  aksl.  düng  dungti {*dhoiin-)  , blasen'  (ablautend  mit  ai.  dhfü-nöti,  -näti,  gr.  dtvw)]
toch.  A  twe,  B  tioeye  , Staub'.
Vgl.  noch  das  vielleicht  ursprungsgleiche  *dheu-  ,laufen,
```


## [2026-09-05T20:03:53.566Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD dheu ===\" && grep -n -E \"^ *dheu|dheu-1|dheubh|dheu-4|dhue|dhu-mo\" AHD_watkins1985.txt | head -60"
}
```


### [2026-09-05T20:03:53.628Z] TOOL RESULT

```
=== AHD dheu ===
382:blind: TYPHUS; TYPHLOSOLE. 11. Extended form *dheubh., “beclouded in the senses,” in suffixed o-grade form *dhoubh-o- in: a. Germanic *daubaz in Old English déaf, deaf: DEAF; b. nasalized form *dhu-m-bho- in Germanic *dumbaz in Old English dumb, dumb: pumps; c. Germanic *diibén- in Old English *dife, dove (< “dark-colored bird”): DOVE!. 12. Extended zero-grade form *dhwel- in: a. Germanic *dwelan, to go or lead astray, in Old English dwellan, to deceive (but influenced in sense by cognate Old Norse dvelja, to tarry): DWELL; b. Germanic *dulaz in (i) Old English dol, dull: DoL- DRUMS (ii) Middle Low German dul, dull: (DOLT), DULL. 13. Extended zero-grade form *dhwes- in Greek suffixed form *th(wjes-es-, smoke, whence Greek *th(w)es-es-yon, becoming theion, brimstone, sulfur: THIO-, THION-. 14. Perhaps Old English docce, dock (< “dark-colored plant”): Dock‘. 15. Perhaps Irish did, pipe: DUDEEN. [Pok. 4. dheu- 261.] dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English déaw, dew: DEW; b. compound *melith-dauwaz, “honeydew” (see melit-). [Pok. 1. dheu- 259.] dheu-’. To become exhausted, die. 1. Suffixed o-grade form *dhou-to- in Germanic *daudaz in Old English déad, dead: DEAD. 2. Suffixed o-grade form *dhou-tu- in Germanic *dauthuz in Old English déath, death: DEATH. 3. Suffixed o-grade form *dhow-yo- in Old Norse deyja, to die: DIE}. 4. Suffixed extended zero-grade form *dhwi-no- in Germanic *dwinan in Old English dwinan, to diminish, languish: DWINDLE. [Pok. 2. dheu- 260.] dheub-. Deep, hollow. 1. Germanic *deupaz in Old Eng- lish déop, deep: DEEP, DEPTH. 2. Germanic expressive denominative *duppjan in Old English dyppan, to im- merse, dip: pip. 3. Parallel root form *dheubh- in Ger- manic *deub-, *dub- in verb *diibjan in Old English dyfan, to dip, and difan, to sink, dive: pivE. [Pok. dheu-b- 267.] dheubh-. Wedge, peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek teukhos (< *theukhos), gear, anything produced, tool: HEPTATEUCH, HEXATEUCH, PENTA- TEUCH. [Pok. dheugh- 271.] dhghem-. Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, “earthling,” in Germanic *gumén- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth: CHTHONIC; AUTOCH- THON. 3. Zero-grade form *dhghm- in Greek khamai, on the ground: CHAMAEPHYTE, CHAMELEON, CHAMOMILE, GERMANDER. 4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth: HUMBLE, (HUMILIATE), (HUMILITY), HUMUS; EXHUME, INHUME, TRANSHUMANCE. 5. Suffixed o-grade form *(dh)ghom-on-, “earthling,” in: a. Latin homé, human being, man: HOMAGE, HOMBRE!, HOMINID, HOMO!, HOMUNCULUS, OMBRE; BONHOMIE, HOMICIDE; b. (in part) Latin himdnus, human, kind, humane: HUMAN, (HUMANE). 6. Suffixed form *(dh)ghem-ya in Russian zemlya, land, earth: SIEROZEM, ZEMSTVO. 7. Full-grade form *(dh)ghem- in Persian zamin, earth, land: ZAMINDAR. [Pok. ghdhem- 414.] dhghut-. Fish. Greek ikhthus, fish: 1cHTHYO-. [Pok. ghdha- 416,] dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic “ges-ter- in Old English geo- stran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.] dhgvhei-. To perish, die away. Zero-grade form *dhgvhi- in Greek phthinein, to die away: PHTHISIS. [Pok. gthdhei(a)- 487.)
394:dhwen-. To make noise. Germanic *duniz in Old English dyne, noise: DIN. [Pok. dhuen- 277.]
1432:DOGE deuk- pocMa dek-1 pDoGMaTIC  dek-! DOIT twei- DOLABRIFORM del-3 DOLCE dik-u- DOLDRUMS_ dheu-t DOLE! dail- DOLE? del-3 DOLERITE del-2 DOLICHOCEPHALIC del-1 DOLICHOCRANIAL  del-1 DOLOR del-3 DOLPHIN gWelbh- Dott dheu-1 Dom deme-1, dhé-1 DOMAIN deme-! DOME deme-1 DOMESTIC deme-1 DOMICILE deme-! DOMINATE deme-1 DOMINICAL deme-1 DOMINIE deme-1 DOMINION deme-' DOMINO! deme-1 DOMINO2 deme-1 DONATION d6- DONATIVE d6- DONOR do- poom dhé-1 pooR dhwer- DOPE dub- DORMANT drem- DORMER drem- DORMITORY drem- DORSAL dorsum poRrsO- dorsum pory? aurum DOSE dé-
1434:DOTE dud- DOUBLE dwo- DOUBLET dwo- DOUBLOON dwo- DOUBLURE dwo- DOUBT dwo- DOUCEUR dik-u- DOUCHE deuk- poucH dheigh- DOUGHTY dheugh- DOUR deru. DOVE! dheu-1 DOWAGER dé- DOWEL dheubh- DOWER do- Down! dhino- pDowN2 dheu-! pown’ dhiino- Dowry do- DOXOLOGY dek-1 DOYEN deki DOZE dheu- DOZEN dekm, dwo- DRAB! der-2 DRAB? dher-! DRABBLE dher-! DRACHMA dergh- DRAFT dhragh- DRAG dhragh- DRAGON derk- DRAGOON derk- DRAIN dreug- DRAKE? derk- DRAMA dera- DRAMATURGE werg- DRAPE der-2 DRASTIC dere- DRAW dhragh- DRAY dhragh- DREAM dhreugh- DREARY dhreu- DRECK sker-4 DREGS dher-1 DRENCH dhreg- DRIFT dhreibh- DRILL! tere-1 DRINK dhreg- DRIP dhreu- DRIVE dhreibh- DRIVEL dher-! DRIZZLE dhreu- -DROME der-1 DROMEDARY der-1 DROMOND der-1 -DROMOUS der-1
1435:DRONE! dher-3 DRooP dhreu- DROP dhreu- DROPsY wed-1 DROSHKY dhragh- DRoss_ dher-1 DROUGHT dreug- DROVE? dhrelbh- DROWN dhreg- DROWSE dhreu- DRUID deru DRUPE deru, pekw- DRY dreug- DRYAD deru DUAD dwo- DUAL dwo- DuB! dheubh- DUB? dheubh- DUBIOUS dwo- DUCAL deuk- DucaT deuk- DUCHESS deuk- DUCHY deuk- Duct deuk- DUCTILE deuk- DUDEEN dheu-1 DUE ghabh- DUEL duellum DUENNA deme-1 DUET dwo- DUKE deuk- DukHoBoR_ bher-2, dheu-! DULCET dik-u- DULCIFY dik-u- DULL dheu-! Duma dhé-1 DUMB dheu-1 DUMP dub- pDuN2 dheu-? DUNDERHEAD (s)tene- DUNE dhino- DUNGEON deme-1 DUNK teng- DUO- dwo- DUODECIMAL dekm, dwo- DUOPSONY wes-1 DUPLE dwo- DUPLEX dwo- DUPLICATE dwo- DUPLICITY dwo- DURABLE deue- DURA MATER deru DURAMEN deru DURANCE deue- DURATION deue- DURBAR dhwer- DURESS deru DURING deue- DURST dhers- DURUM deru Dusk dheu-! Dust dheu-' DutTcH teuta- DUTY ghabh- DUUMVIR wi-ro- DUVETYN dheu-! DWELL dheu-! DWINDLE dheu-3 DYAD dwo- DYNAMIC deu-2 DYNAMITE deu-2 DYNAST deu-2 DYNASTY deu-2 Dys- dus- DYSENTERY en DYSLEXIA leg-1 DYSMENORRHEA mé-2 DYSPEPSIA pekw- DYSPLASIA pele-2 DYSPNEA pneu- DYSPROSIUM ei-1
1463:ENTER en ENTERIC en ENTERO- en ENTERON en ENTERPRISE ghend- ENTERTAIN ten- ENTHUSIASM dhés- ENTHYMEME dheu-1 ENTIRE tag- ENTITY es-
1544:FROLIC fik-, preu- FROM per? FRONTISPIECE spek- FROST preus- FROTTAGE bhréi- FROWARD per! FRUCTIFY bhrig- FRUGAL bhriig- FRUGIVOROUS bhrig- FRUIT bhriig- FRUITION bhriig- FRUMENTACEOUS _ bhrig- FRUMENTY bhriig- FRUSTULE bhreus-2 FRUSTUM bhreus-2 FRY! bher-4 FUGACIOUS bheug-1 -FUGE bheug-! FUGITIVE bheug-1 FUGLEMAN man-1, pleu- FUGUE bheug-! FUHRER per-2 FULCRUM bhelg- FULGENT bhel-1 FULGURATE bhel-1 FULIGINOUS dheu-1 FULL! pele-1 FULMAR pu-2 FULMINATE bhel-1 FUMARIC ACID dheu-1 FUMAROLE dheu-1 FUMATORIUM dheu-! FUMATORY dheu-1 FUME dheu-! FUMIGATE ag-, dheu-! FUMITORY dheu-1, ters- FUNAMBULIST al-2 FUNCTION bheug-2 FUND bhudh- FUNDAMENT bhudh- FUNDUS_ bhudh- FUNGIBLE bheug-2 FUNNEL gheu-
1952:OBEY au-5 OBFUSCATE dheu-1 OBITUARY el-1 OBJECT! yé- OBJURGATE ag-, yewes- OBLAST epi, wal- OBLATE! tele- OBLIGE leig-1 OBLITERATE deph- OBLIVION lel- OBLONG del-1 OBLOQUY tolkw- OBNOXIOUS nek-1 OBOE busk- OBSCURE (s)keu- OBSEQUIOUS sekw-1 OBSERVE ser-! oBsEss sed-1 OBSTACLE sta- OBSTETRIC sta- OBSTINATE sta- OBSTREPEROUS §strep- OBSTRUCT ster-2 OBTAIN ten- OBTECT (s)teg- OBTEST trei- OBTRUDE treud- OBTUND (s)teu- OBVERT wer-3 oBvious wegh- OBVOLUTE wel-3 OCARINA awi- OCCASION kad- occipuT kaput OCCLUDE kleu-3 occuLT kel-2 occupy kap- occur kers-2 OCELLUS okWw- OCHLOCRACY wegh- OCHLOPHOBIA wegh- OCTAD okto(u) OctTans okt6(u) OCTANT oktd(u) OCTAVE okt6d(u) OcTAvO okt6(u) OCTENNIAL at-
2079:PER- pert PERCEIVE kap- PERCENT dekm PERCH? perk-1 PERCOLATE kagh- PERCURRENT kers-2 PERCUSS kwét- PERDITION d6- PERDURABLE deue- PEREGRINE agro- PEREMPTORY em- PERENNIAL at- PERFECT dhé-1 PERFIDY bheidh- PERFORATE bher-2 PERFUME dheu-1 PERFUNCTORY bheug-2 PERFUSE gheu- PERGOLA perg- PERI- per! PERICARDIUM kerd-1 PERICLINE Klei- PERIGEE gé PERIHELION sawel- PERIL per-4 PERIMYSIUM mis- PERINEPHRIUM negWh-ro- PERIOD sed-2 PERIONYCHIUM nogh- PERIOSTEM ost- PERIPATETIC pent- PERIPETEIA pet- PERIPHERY bher-1 PERIPHRASIS gWhren- PERIPHYTON bheue- PERIPTERAL pet- PERISARC  twerk- PERISH ei-1 PERISSODACTYL per! PERISTALSIS | stel- PERISTYLE sta- PERITHECIUM dhé-1 PERITONEUM ten- PERITRICH _ thrix PERIWINKLE! weng- PERJURE yewes- PERMANENT men-3 PERMEATE mei-1 PERMIT (s)meit(a)- PERMUTE mei-1 PERNICIOUS nek-1 PERONEAL per-2 PERORAL 6s- PERORATE 6r- PERPEND (S)pen- PERPENDICULAR (S)pen- PERPETRATE peter- PERPETUAL pet- PERPLEX plek-
2178:REIGN reg-! REIMBURSE bursa REINDEER dheu-1, ker-1 REINFORCE bhergh-2 REITERATE i- REJECT yé- REJOICE gau- REJUVENATE yeu- RELAPSE leb-! RELATE tele- RELAX slég- RELAY slég- RELEGATE leg-1 RELENT lento- RELIEVE leg¥h- RELINQUISH leikw- RELUCENT leuk- RELUCT leug-! RELY leig-1 REMAIN men-3 REMAND man-2 REMARK merg- REMEDY med- REMEMBER (s)mer-! REMEX ere-! REMINISCENT men-! REMIT (s)meit(a)- REMORA mere- REMORSE mer-2 REMOTE meue- REMOVE meue- REMUDA mei-1 REMUNERATE mei-! RENAISSANCE gene- REND rendh- RENDER do- _ RENDEZVOUS wOS RENEGADE ne RENEGE ne RENITENT kneigh- RENOUNCE neu-! RENOVATE newo- RENOWN no-men- RENT! do- REPAIR! pere-1 REPAND pete- REPARTEE pere-2 REPAST pa- REPEAT pet- REPEL pel-6 REPENT2 rép-1 REPERTORY pere-! REPINE kWei-1 REPLENISH pele-! REPLETE pele-1 REPLEVIN plegan REPLICATE plek- REPORT per-2 REPOSE! paus- REPOSIT apo- REPREHEND ghend- REPRESENT e@S- REPRESS per-5 REPRIMAND per-5 REPRISAL ghend- REPRISE ghend- REPROACH pert REPROVE per? REPTILE rép-1 REPUBLIC ré- REPUDIATE (s)peud- REPUGN peuk- REPUTE peu-
2381:THIO- dheu-t THION- dheu-1 THIRD trel-
2389:THYME dheu-! -THYMIA dheu-1 THYROID dhwer- TICK? deigh- TICK3 dhé-1 TICKET steig- TIDE! da- TIDE2 da- TIDINGS da- TIE deuk- TIERCE trei- TIFFANY bha-1 TIGER steig- TIGHT tenk-2 TILE (s)teg- TILLER? teks- TILLERS del-3 TILT? del-3 TIMBER deme-1 TIME da- TIMOCRACY kWeig-1 TINCT teng- TINGE teng- TINSEL skeei- TINT teng-
```


## [2026-09-05T20:03:57.320Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '380,383p' AHD_watkins1985.txt | fold -w 200 | head -60"
}
```


### [2026-09-05T20:03:57.371Z] TOOL RESULT

```
14
dhg“hei-
blind: TYPHUS; TYPHLOSOLE. 11. Extended form *dheubh., “beclouded in the senses,” in suffixed o-grade form *dhoubh-o- in: a. Germanic *daubaz in Old English déaf, deaf: DEAF; b. nasalized form *d
hu-m-bho- in Germanic *dumbaz in Old English dumb, dumb: pumps; c. Germanic *diibén- in Old English *dife, dove (< “dark-colored bird”): DOVE!. 12. Extended zero-grade form *dhwel- in: a. Germani
c *dwelan, to go or lead astray, in Old English dwellan, to deceive (but influenced in sense by cognate Old Norse dvelja, to tarry): DWELL; b. Germanic *dulaz in (i) Old English dol, dull: DoL- DRUMS 
(ii) Middle Low German dul, dull: (DOLT), DULL. 13. Extended zero-grade form *dhwes- in Greek suffixed form *th(wjes-es-, smoke, whence Greek *th(w)es-es-yon, becoming theion, brimstone, sulfur: THIO-
, THION-. 14. Perhaps Old English docce, dock (< “dark-colored plant”): Dock‘. 15. Perhaps Irish did, pipe: DUDEEN. [Pok. 4. dheu- 261.] dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old Englis
h déaw, dew: DEW; b. compound *melith-dauwaz, “honeydew” (see melit-). [Pok. 1. dheu- 259.] dheu-’. To become exhausted, die. 1. Suffixed o-grade form *dhou-to- in Germanic *daudaz in Old Engl
ish déad, dead: DEAD. 2. Suffixed o-grade form *dhou-tu- in Germanic *dauthuz in Old English déath, death: DEATH. 3. Suffixed o-grade form *dhow-yo- in Old Norse deyja, to die: DIE}. 4. Suffixed ext
ended zero-grade form *dhwi-no- in Germanic *dwinan in Old English dwinan, to diminish, languish: DWINDLE. [Pok. 2. dheu- 260.] dheub-. Deep, hollow. 1. Germanic *deupaz in Old Eng- lish déop, deep: 
DEEP, DEPTH. 2. Germanic expressive denominative *duppjan in Old English dyppan, to im- merse, dip: pip. 3. Parallel root form *dheubh- in Ger- manic *deub-, *dub- in verb *diibjan in Old English dyfa
n, to dip, and difan, to sink, dive: pivE. [Pok. dheu-b- 267.] dheubh-. Wedge, peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: 
puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, 
dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek teukhos (< *theukhos), gear, anything produced, tool: HEPTATEUCH, HEXATEUCH, PENTA- TEUCH. [Pok. dheugh- 271.] dhghem-.
 Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, “earthling,” in Germanic *gumén- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth: CHTHONIC; AUTOCH- THON. 3
. Zero-grade form *dhghm- in Greek khamai, on the ground: CHAMAEPHYTE, CHAMELEON, CHAMOMILE, GERMANDER. 4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth: HUMBLE, (HUMILIATE), (HUMILITY), HU
MUS; EXHUME, INHUME, TRANSHUMANCE. 5. Suffixed o-grade form *(dh)ghom-on-, “earthling,” in: a. Latin homé, human being, man: HOMAGE, HOMBRE!, HOMINID, HOMO!, HOMUNCULUS, OMBRE; BONHOMIE, HOMICIDE
; b. (in part) Latin himdnus, human, kind, humane: HUMAN, (HUMANE). 6. Suffixed form *(dh)ghem-ya in Russian zemlya, land, earth: SIEROZEM, ZEMSTVO. 7. Full-grade form *(dh)ghem- in Persian zamin, ear
th, land: ZAMINDAR. [Pok. ghdhem- 414.] dhghut-. Fish. Greek ikhthus, fish: 1cHTHYO-. [Pok. ghdha- 416,] dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic “ges-ter- in Old
 English geo- stran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.] dhgvhei-. To perish, die away. Zero-grade form *dhgvhi- in Greek phthinein, to die away: PHTHISIS. [Pok. gthdhei
(a)- 487.)
dhg“her-
```


## [2026-09-05T20:04:01.246Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '374,380p' AHD_watkins1985.txt | fold -w 200 | tail -40"
}
```


### [2026-09-05T20:04:01.304Z] TOOL RESULT

```
ININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo
- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade 
form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- i
n Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé
-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dh
yd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he medita
tes (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compoun
d Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High Germ
an teic, dough: TEIGLACH. 4. Suffixed zero-grade form *dhigh-ird, in Latin figira, form, shape (< “result of kneading”): FIGURE; CONFIGURATION, DISFIGURE, PRE- FIGURE, TRANSFIGURE. 5. Nasalized ze
ro-grade form *dhi-n-gh- in Latin fingere, to shape: (FAINT), FEIGN, (FEINT), FICTILE, FICTION, FIGMENT; EFFIGY. 6. Nasal- ized zero-grade form *dhi-n-g(h)- in Greek thinganein, to touch: THIGMOTAXIS,
 THIXOTROPY. 7. Suffixed o-grade form *dhoigh-o- in Avestan daéza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English del
l, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de
/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248
.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek 
thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-
egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic 
*drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRAB
BLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended
dher-2
zero-grade form *dhra-gh- in: a. Greek tarassein (Attic tarattein), to confuse, disturb: ATARACTIC; b. Greek trakhus, rough: TRACHEA, TRACHOMA, TRACHYTE. [Pok. 1. dher- 251.] dher-2, To hold firmly, s
upport. 1. Suffixed form *dher-mo- in Latin firmus, firm, strong: FARM, FERMATA, FIRM, FIRMAMENT; AFFIRM, CONFIRM, INFIRM, (INFIR- MARY). 2. Extended form *dhergh- possibly in Latin fortis, strong (bu
t this is also possibly from bhergh-?). 3. Suffixed zero-grade form *dhr-ono- in Greek thronos, seat, throne (< “support”): THRONE. 4. Suffixed form *dher-mn in Sanskrit dharma, statute, law (< �
�that which is established firmly”): DHARMA. 5. Old Persian dar-, to hold (whence Persian -ddr, ‘“-holder’’): SIRDAR, TAHSILDAR, ZAMINDAR. [Pok. 2. dher- 252.] dher-3, To drone, murmur, buzz
. Extended zero-grade form *dhrén- in: a. Germanic *drén- in Old English dran, drén, male honeybee: DRONE}; b. Greek thrénos, dirge, lament: THRENODY. [Pok. 3. dher- 255.] dhers-. To venture, be b
old. 1. O-grade form *dhors- and zero-grade form *dhrs- respectively in Germanic *ders- and *durs- in Old English dearr and durst, first and third person singular present and past indicative of durran
, to venture: DARE, (DURST). 2. Possibly Latin -festus in: a. infestus, hostile (? < “directed against”; in-, into, against; see en): INFEST; b. manifestus, palpable, evident (< “caught red-hand
ed, grasped by the hand”; manus, hand; see man-2): MANIFEST. [Pok. dhers- 259.] dhés-. Root of words in religious concepts. Possibly an extension of dhé-'. 1. Suffixed form *dhés-yd in Latin fér
iae (Old Latin fésiae), holidays: FAIR?, FERIA. 2. Suf- fixed form *dhés-to- in Latin féstus, festive (> German Fest, festival): FEAST, (-FEST), (FESTAL), FESTIVAL, FES- TIVE, FESTOON, (FETE), FIES
TA; (GABFEST), OKTOBER- FEST. 3. Suffixed zero-grade form *dhas-no- in Latin fanum, temple: FANATIC; PROFANE. 4. Possibly suffixed zero-grade form *dhas-o- becoming *dhes-o- in Greek theos (< *thes-os
), god: THEO-; APOTHEOSIS, ATHEISM, ENTHUSIASM, PANTHEON, POLYTHEISM. [Pok. dhés- 259.] dheu-'. Also dheue-. The base of a wide variety of derivatives meaning “to rise in a cloud,” as dust, vapor
, or smoke, and related to semantic notions of breath, various color adjectives, and forms denoting defective perception or wits. 1. Suffixed extended zero-grade form *dhii-mo- (<*dhua-mo-), smoke, in
: a. Latin fimus, smoke: FUMAROLE, FUMATORIUM, FUMATORY, FUME; FUMARIC ACID, FUMIGATE, FUMITORY, PERFUME; b. Greek thumos, soul, spirit: -THYMIA; ENTHYMEME; c. Greek thumon, thumos, thyme (< “plant 
having a strong smell”): THYME. 2. Suffixed lengthened zero-grade form *dhi-li- in Latin filigd, soot: FULIGINOUS. 3. Ex- tended form *dheus- possibly in Germanic *dus- in: a. Old English dysig, foo
lish (< “stupefied,” “confused”): pD1zzy; b. Danish dase, to make drowsy, akin to the probable Scandinavian source of DOZE. 4. Suffixed ex- tended form *dheus-o- in Germanic *deuzam, breathing
 creature, animal, in: a. Old English déor, animal: DEER; b. Old Norse dyr, animal, deer: REINDEER. 5. Suffixed o-grade form *dhous-o in Slavic *dukh- in Russian dukh, breath, spirit: DUKHOBoR. 6. Va
riant extended form *dhwes- in nasalized form *dhwens- in Germanic *duns-, dust, meal, in: a. Germanic suffixed form *duns-to- in Old English dist, dust: pustT; b. Old Norse diinn, bird’s down (< �
�fine like dust”): DOWN?, DUVETYN; (EIDER- Down). 7. Extended zero-grade form *dhus- in Greek thuos, burnt sacrifice, incense (> Latin thus, incense), and ¢huia, cedar: THUJA, THURIBLE; (THURIFER).
 8. Suf- fixed extended zero-grade form *dhus-ko- in: a. Ger- manic duskaz in Old English dox, twilight: Dusk; b. Latin fuscus, dark, dusky: OBFUSCATE. 9. Suffixed extended zero-grade form *dhus-no- i
n Welsh dwn, dull brown color, whence Old English dun(n), dark-brown: DUN2, 10. Zero-grade extended form *dhubh- in Greek tuphein (< *thuphein), to make smoke, and tuphios,
14
```


## [2026-09-05T20:04:12.332Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN typhoon ===\" && grep -n -i \"typhoon\" KLN_1966.txt KLN_1971.txt | head -20 && echo \"=== KLN typhus ===\" && grep -n -i \"typhus\" KLN_1966.txt KLN_1971.txt | head -20 && echo \"=== SKT typhoon ===\" && grep -n -i \"typhoon\" SKT.txt | head"
}
```


### [2026-09-05T20:04:12.439Z] TOOL RESULT

```
=== KLN typhoon ===
KLN_1966.txt:40609:Derivative:  typhoid-al,  adj. typhomania,  n.,  delirium  characteristic  of  typhus (med.)  —  Medical  L.,  compounded  of  typho- and  Gk.  jxavla,  ‘madness,  frenzy’.  See  mania, typhonic,  adj.,  pertaining  to,  or  resembling,  a  ty¬ phoon.  —  Gk.  TU9ttmx6?,  fr.  -rupoiv,  which  is rel.  to  TU90?,  ‘smoke,  mist’.  See  typhus  and  -ic. typhoon,  n.,  a  cyclone  in  the  western  Pacific.  — Chin,  tai  fung,  lit.  ‘great  wind’;  influenced  in form  by  Arab,  tufan  (whence  also  Port,  tufao), fr.  Gk.  TO9COV,  ‘whirlwind’  (see  typhus). typhous,  adj.,  pertaining  to  typhus.  —  Formed with  suff.  -ous  fr.  Gk.  TU90G  See  typhus.
KLN_1971.txt:256187:typhoon, n., a cyclone in the western Pacific. — - 
=== KLN typhus ===
KLN_1971.txt:173784:typhus, but usually milder; n., a paratyphoid 
KLN_1971.txt:232370:L .fumus, ‘smoke’. See typhus and cp. stove. Cp. 
KLN_1971.txt:246647:thyine, thyme, thysano-, tumble, typhlo-, typhus, 
KLN_1971.txt:256168:Ti^eiv, ‘to smoke’. See typhus, 
KLN_1971.txt:256171:typhus (med.) — Gk. TU90-, TU9-, fr. tu9<j<;. 
KLN_1971.txt:256172:See typhus. 
KLN_1971.txt:256181:typhomania, n., delirium characteristic of typhus 
KLN_1971.txt:256186:rel. to tu 9Q£, ‘smoke, mist’. See typhus and -ic. 
KLN_1971.txt:256190:fr. Gk. TU9WV, ‘whirlwind’ (see typhus). 
KLN_1971.txt:256191:typhous, adj., pertaining to typhus. — Formed 
KLN_1971.txt:256192:with suff. -ous fr. Gk. TucpOQ. See typhus. 
KLN_1971.txt:256198:typhus, n. — Medical L., fr. Gk. TU9oq, ‘smoke, 
KLN_1966.txt:27364:Derivative:  paratroop-er,  n. paratyphoid,  adj.,  pertaining  to  a  fever  resembling typhus,  but  usually  milder;  n.,  a  paratyphoid fever  {med)  —  Coined  fr.  para-,  ‘beside’,  and typhoid.
KLN_1966.txt:36774:stew,  tr.  and  intr.  v.,  to  cook  slowly.  — -  ME. stuert,  stuwen,  to  bathe’,  fr.  OF.  estucer,  ‘to bathe  in  warm  water’  (whence  F.  etuver,  ‘to heat,  stove,  stew'),  fr.  VL.  *extufare  (whence also  It.  stufare ),  fr.  1st  ex-  and  *tufare,  ‘to  heat’, which  is  cogn.  with  Gk.  xutpoi;,  ‘mist,  vapor’, L .fumus,  ‘smoke’.  See  typhus  and  cp.  stove.  Cp. also  next  word.
KLN_1966.txt:39044:thio-,  before  a  vowel  thi-,  combining  form  used in  the  sense  of ‘containing  sulfur’  ( chem .)  —  Gk. Delo-,  Dei-,  fr.  Oetov,  Homeric  Gk.  9£eiov, ‘brimstone’,  for  *9.F£C[-(e)lov,  lit.  ‘that  which smokes’,  from  I.-E.  base  *dhewes-,  *dhwes-,  ‘to breathe,  smoke'.  Base  *dhewes-,  *dhwes-,  is  an enlargement  of  base  *dheu-,  ‘to  fly  about  like dust,  to  smoke,  whirl,  shake,  be  scattered,  van¬ ish',  whence  OI.  dhunbti,  dhuvati,  ‘shakes, moves',  Gk.  Ooei-v,  ‘to  sacrifice’,  prop,  ‘to  cause to  smoke’,  9up.ee,  ‘sacrifice’,  Oupov,  also  9upo?, ‘thyme’,  9upi£v,  ‘to  burn  so  as  to  produce smoke’,  UOptapa,  ‘incense’,  9uo<;,  ‘burned  sac¬ rifice’  (whence  L.  thus,  gen.  thuris,  ‘frankin¬ cense’),  9up6 p,  ‘spirit,  breath,  life,  mind,  soul, desire,  courage,  anger',  OOstv,  Ouia^Eiv,  ‘to rage’.  Cp.  thanato-,  Thuja,  thurible,  Thyiad, thyine,  thyme,  thysano-,  tumble,  typhlo-,  typhus, the  first  element  in  Thymelaeceae  and  the  second element  in  athymia,  barythymia.  Cp.  also  deaf and  words  there  referred  to,  and  dull,  and  words there  referred  to.  Cp.  also  deer,  dizzy,  down, ‘soft  plumage',  down,  ‘hill’,  dust,  feral,  ‘funereal’, fume,  fury,  hag,  ‘a  witch’,  and  the  first  element in  Dukhobors.
KLN_1966.txt:40605:typhlo-,  before  a  vowel  typhl-,  combining  form meaning  ‘blind’.  —  Gk.  TJ9X0-.  rut?/.-,  fr. TJ9/.0:  (dissimilated  fr.  *f>u9Xoc),  ‘blind, closed,  blunt',  which  is  rel.  to  TJ90?,  ‘smoke’, Tucpsiv,  ‘to  smoke'.  See  typhus, typho-,  before  a  vowel  typh-,  combining  form meaning  ‘smoke,  vapor',  used  in  the  sense  of typhus  (med.)  —  Gk.  TO90-,  TU<p-,  fr.  xuepo?. See  typhus.
KLN_1966.txt:40609:Derivative:  typhoid-al,  adj. typhomania,  n.,  delirium  characteristic  of  typhus (med.)  —  Medical  L.,  compounded  of  typho- and  Gk.  jxavla,  ‘madness,  frenzy’.  See  mania, typhonic,  adj.,  pertaining  to,  or  resembling,  a  ty¬ phoon.  —  Gk.  TU9ttmx6?,  fr.  -rupoiv,  which  is rel.  to  TU90?,  ‘smoke,  mist’.  See  typhus  and  -ic. typhoon,  n.,  a  cyclone  in  the  western  Pacific.  — Chin,  tai  fung,  lit.  ‘great  wind’;  influenced  in form  by  Arab,  tufan  (whence  also  Port,  tufao), fr.  Gk.  TO9COV,  ‘whirlwind’  (see  typhus). typhous,  adj.,  pertaining  to  typhus.  —  Formed with  suff.  -ous  fr.  Gk.  TU90G  See  typhus.
KLN_1966.txt:40610:Typhula,  n.,  a  genus  of  fungi  (hot.)  —  A  ModL. hybrid  coined  fr.  Gk.  ruipoe,  ‘vapor’  (see  next word),  and  L.  dimin.  suff.  -ula.  The  correct  form would  be  Typhidium  (fr.  Gk.  TU90?  and  suff. -idium,  fr.  Gk.  dimin.  suff.  -iStov). typhus,  n.  —  Medical  L.,  fr.  Gk.  TU90?,  ‘smoke, mist,  cloud,  fever  accompanied  by  stupor’, which  is  rel.  to  T09EIV,  ‘to  smoke',  TU9X09, ‘blind’,  TU9WV,  ‘whirlwind’.  These  words  are  of uncertain  origin.  They  are  perh.  cogn.  with Goth,  daufs,  OE.  deaf,  ‘deaf’,  Goth,  dumbs,  OE. dumb,  ‘dumb’,  OE.  dufe-  (in compounds),  ‘dove’, lit.  ‘the  dark-colored  (bird)’,  OIr.  dub  (for  *dhu- bu-),  ‘black’.  All  these  words  possibly  derive  fr. I.-E.  base  *dheu-bh-,  *dhu-bh-,  ‘to  fill  with smoke,  to  cloud,  darken;  to  be  dull,  dumb  or deaf’.  See  deaf  and  cp.  typhlo-. typic,  adj.  —  F.  typiqtte,  fr.  Late  L.  typicus.  See next  word.
=== SKT typhoon ===
20365:TYPHOON,
20378:worH  ;  it  is  a  Chinese  word a  great  wind/  —  Chined  ta, f^vinLantun/«M^''>,  wind,  whence >  gale,  a  typhoon  (VVitliAinsK rould  be  better ;  tythyon  '\%  due I  with  the  old  wont  typhon  (not in  old  authors),  from  Gk.  tm/'Wi', r,  a  whirlwind.  The  close  acd- idcncL-  of  these  words  In  sense  and
23717:Ckineu'.  china,  Chinese,  nankeen,  tea, typhoon.
```


## [2026-09-05T20:04:21.374Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT leaf for typhoon ===\" && python3 -c \"\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\ni=t.find('TYPHOON')\nprint('leaf(0based)=',t[:i].count('\\f'))\nprint(t[i-200:i+1400])\n\""
}
```


### [2026-09-05T20:04:23.202Z] TOOL RESULT

```
=== SKT leaf for typhoon ===
leaf(0based)= 557
  cf.  L.  duhim, doLiblful,  from  duo,  two.+f'-  ::wieliiht,  O. L>u.  hveeluhf\  umilarly  compounded.
twill.  (Low  G."i  Low  Q.twillen,  to naJfc  double  j  dL  tv/ili^  a  (otkcd  bcaoch.  ^
TYPHOON,
Allied  to  Swell.  Dan,  tviUimg,  a  twta. The  word  has  reference  to  a  pecnl:** method  of  doubling  the  warp-threadt.  ac taking  two  of  ihem  logt-tlicr ;  thi^  pvtt an  appearance  of  dia^nal  lines  ii'  textile fabric**.     From  A.  S  /ii'/*,  double  (abort).
twin.  (E.)  A.  S.  gt'tutnfte,  twins.4- Icel.  iviunr^  in  paii« ;  Lithuan.  tiwuiit twins;  cf.  L.  bint,  two  at  a  lime.  Froa the  A.  S.  twi;  double;  the  -if  gives  ad* lributi%'e  force,  as  in  L.  bi-n-i,  two  at  i  titne.
twine,  vb.  (£.1  M.  E.  tn'tiren,  lo twist  together.  From  A.  S.  twiM,  sb ,  s twisted  or  Joublcii  thread.  —  A.  S.  ^>l'/-, double ;  see  twioft  (above).  -4*  Du.  tvy^, sb.,  a  twist,  twine.  Icel.  tvinni^  twinr Swed.  tvinntrdd,  twine-thread.
twist,  vb.    (E.)       M,  E.  twiiten,  n\y formed   from  A.  S.  tufitf.   sb.,  a  rwpe  or twisted  cord.-*  A.  S.  tiv/-,  double:  w'-l" sufhx  -sf,  as  is  b/a-st  ^m  biaw.    Tbe  !>■• tiifist,    Dan.  Swed.  tvist.  G.    twin,  »« '  discord,'  which  is  afiolber  sense  of  ()■ same  word ;   so  also  M ,  E,  fwiti,  a.  twig  m fork  of  a  branch ;  Icel.  tvistr,  the  deuu,  i8 card  playing. Tympanum ;  see  Type. Type.    (K.-U-Gk-)      F.  t^  (Sbef wood).  — L.    tj^/mm,   ace.    of  i^/iu. —Gt Tinroj,   a    blow,   mark    of  a    blnw    rrsrrp, impr
```


## [2026-09-05T20:04:31.433Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor m in re.finditer('[Tt]yphoon',t):\n    print('---leaf',t[:m.start()].count('\\f'), 'printed~', t[:m.start()].count('\\f')-20)\n    print(t[m.start()-600:m.start()+700].replace(chr(10),' ')[:1300])\n    print()\n\""
}
```


### [2026-09-05T20:04:33.309Z] TOOL RESULT

```
---leaf 557 printed~ 537
l.  (F.  -  L.  -  Gk.)  Dima M.  E.  timbre,  a  small  lambonruie.«-0.  F< timbre,  ty /fibre,  a  timbrcLoL*.  tymf^dmaoK a  drum ;  see  below. tympanum,   the  hollow  pttt  «/ ear.  &c.    (L.  -  Gk.)       L.  tjmfmnm drum,  tympanum.  —  Gk-.  rv^mFBV.  a roller ;  the  same  as  nnmrcpf.  a  Arum  ^^ TWIT*,  b.iie  of  Ti)«-r*ii',  to  ■  i my.  Gk.  rv^nayiai.  a  d  i  < cUy  is  tightly  stretched.  a>.  %     rv.:: Typlioon,  a  violent  wiuilwaui.  ^ChianJ c TYPHUS. worH  ;  it  is  a  Chinese  word a  great  wind/  —  Chined  ta, f^vinLantun/«M^''>,  wind,  whence >  gale,  a  typhoon  (VVitliAinsK rould  be  better ;  tythyon  '\%  due I  with  the  old  wont  typhon  (not in  old  authors),  from  Gk.  tm/'Wi', r,  a  whirlwind.  The  close  acd- idcncL-  of  these  words  In  sense  and rvniarkable,  as  Whitney  notes. a  kind  of  fever.  ( L.  —  Gk.)     L. Gk.  Tv^or,  unok-e^    mitt ;   also UMBILICAL. 53 1 stupor,  esp.  if  an&ing  from  fever;  tyf^hta yrtvr  =  slUi>or-fevcr.  —  Gk.  rin/mv.  to  smoke. Cr.  Skt.  iihtip,  to  fumigate.  (^I^IIU.) Der.  iypho  ul^  i.  e.  typhu»-llkc,  from  eiSofl, re:«rmb]aijce. Tyrant.  (F.-L.-Gk)  The  /  is  added. O.  F.  tiroH,  lUo  tyfant.—  'L.  tyrauHutn, ace.  of  tyranitus,  a  tyrant— Gk.  fuparKor, 

---leaf 641 printed~ 621
gle,  cowry,  sham Idy. Italian  from  Turkish  from Hindustani:  tulip,  turban \piaco-namu\  calico, cashmere. PM  Ltm  Latin  from  Hindi  x Bongaii:  bungalow. pice. St:  areca. Hetefrom  Malayalim :  betel. \Hm'-  teak. Maumaraa,    ctHiiit,   waxy  (»), Malay :  bamboo  [perhaps  Canarese]^ caddy,  cassowary,  cockatoo,  crease  \2'\  or creese,  dugong,  gong,  gntla-perclia,  lory (luiy),  mango,  mudc  (amuck),  orang- outang, proa  ( prow },  rattan,  sago, apas. French  from  Malay:  ratafia. French  from  Arabic  from  Malay:  cam- phor. Ckineu'.  china,  Chinese,  nankeen,  tea, typhoon. Portugtuse  from  Chinese:  junk  (i). Latin  from  Greek  from  Ckinese:  silk. French  from  Latin  from  Grtik  frMiv Chines*  X  sctge. Japaneit  \  ^aMn,  10^ . Portuguese  /r»m  Jaf€Lnt\t :  \j«cv-ifc. 613 VI.    DISTRIBUTION   OF  WORDS,  ETC. Java :  bantam. Annamtst:  gamboge. Kussianfrvm  Tatar :  cossack,  nuunmoth. Persian  from  Tatar:  klinii,  larior  (3). AIoHgoiiaa :  mogul. Thibetan:  lama  (0, Australian :  kangaroo, bat. TahUioH'.  Utioo  (a). Polymsian:  Uboo. ao.  Words  derired  from  variotia  AFRICAN  languages. Hebrew  from  Egyptian  :  ephah. Latin  from  Greek  from  Hebrew  from Egyptian :  sack  (1). French  from  Latin  from  Grttk  from Htbrrtv from
```


## [2026-09-05T20:04:46.835Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT dvaidi ===\" && grep -n -i \"dvaidi\\|dvaidī\\|dvaêdi\" BRT.txt | head -20 && echo \"=== BRT hand.va ===\" && grep -n -i \"handvai\\|han-dva\\|hqndav\\|handav\" BRT.txt | head -20"
}
```


### [2026-09-05T20:04:46.904Z] TOOL RESULT

```
=== BRT dvaidi ===
12816:atyä  (sd.)  Ayat  maiäqm  dvaidi  (iDftM.)"
=== BRT hand.va ===
29376:•j.han-dvar3na-i)Adj.'comes,  Genosse', von  dafinsx^KO.  Wesen :  kva  datvanqm  'n) . .  hqm.patanB  V.  7.  53;  54.  3)  n.  'co-
```


## [2026-09-05T20:04:49.684Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\ni=t.find('dvaidi')\nprint('leaf',t[:i].count('\\f'))\nprint(t[i-2500:i+900])\n\""
}
```


### [2026-09-05T20:04:51.496Z] TOOL RESULT

```
leaf 397
chen,  sagen,  reden'; i)  mit  Aklc  des  Gesagten:  dalva  drvants .,    ayqm    äaci%rfm    däunta'^    V, /(j.  45;
—  uspatat  Jranroie  .  .  ayqm  daoihrim daomns'*  Yt. 75,57;  —  aHs  daksk5  .  . saxsä^nm  daomnö*'' \t.ig.\T.  3)  das Gesagte  folgt  in  direkter  Rede:  adavtita (Augm.)  avrS  mainyuf:  mä  .  .  H.  2.  35; Yt^.  14;  —  ktnsanJm  ..yS  davata:  nsit «?  .  .  Y.  5.  34;  —  advännta  adäunta (Augm.)  dafva  V.  ig.  45;  45,  47.  a)  mit uiti:  uiti  davata  Äi  y}  .  .  ai?rö  mainyus; drvxf  upa.dvilra  V.  ig.  i ;  44,  Yt.  77.  1 9, Vyt^;  —  büiyqsta  .  .  uiti  aoj?mna  uiti daomna:  yfafsata  .  .  FrW.  10.  43.
mit  paiti  'antworten',  mit  Dat.  der  Fers.
*dav-  688
und  folg.  dir.  Rede:  paHi  a&mai  adavata (Augm.)  .  .  aarB  mainyui:  mä  ml .  .  V. ig.6;  —  druxi  hl  paiti jd<tvata:skiäara .. v.ig.y,  JA  31.
mit  /r3  nnd  vi  'hin  und  her  reden': fradavata  vtdavata  fi-amof^fota  vlmaigiata ar»HJ  mainyu/  "es  redete  hin,  es  redete her,  es  überlegte  hin,  es  Überlegte  her AM.''  V.jp.43.
mit  vT:  s.  bei  JrS.
mp.  (Pü.)  dm/istan  i),  PDi.  war-^aam  "ich  rede an»  dem  Schlafp).  —  ')  Im  Gegens.  zu  mrav und  vai-,  t,  H.  2.  \^,  35  twd  V.  ig.  6,  7.  — •)  Statt  davi',  %  36S.  22,  33,  3^.  —  S>  Hos.1 NpEt.  17  a.
•  j.  *dav-  V.  'entfernen'.  Praes.  3  dava-, 4  dva-.
'forttreiben,  for^agen':  *apala  vh  samar? ana  dttyc**^  (iSPM.)  "fort  ja^e  ich  euch damit  (zurück)  in  die  Erde"  Yti.  39.
mit  avi  und  frä  Med.  'mit  sich  fort- führen, fortreissen',  vom  Wasser:  yäha masyaya  äß  kasyanhqm  apqm  *avi./rä- '  iavaite'^  "wie  ein  grösseres  Wasser  kleinere Wasser  mit  sich  fortreisst"  V,  5.  34.
Vgl.  «i.  doj'i/äm,  dmiasänaioA  (usw.),  gr.  Jm- !  luu  (usw.);  IF.  13.  137.  —  S.  noch  dita-, düta-,  äittiaalam,  daibitä.  —  Pü.  (zu  Yt.):  fa lamii  daMil,  (zu  V.) :  apar  fräl  boret.  —  ')  So nach  J  10,  F  1  nsw.;  s.  BXHU  IF.  It.  136.  — *)  Jpl,  Mfa;  NA.  -ti.
•  j.  Jdav-  V.,  nur  mit  /ra  'reinigend  ab- reiben'.    Praes.  i  dava-.
Med.  'sich  abreiben  mit  — '  (Gen.): aOaesamca  t>mS  p3riiu.ß'avaii{si.)  /rata- vata  {3S,)  V.ß.  29.
ai.  dhävalt ;  np.  aiutüdan,  tidüdan  (HOKK  GliPh. /  b.  130).  —  PiL ;  fräe  e  tanSiid,  erL ;  xäfi  afie i  ianäiid.
•  g.  <dav-  V.  '(sich)  diHngen'.     Praes.
I  daV'  :  du:
i)  'drangen,  bedrängen':  mS  urva gSuscä
atyä  (sd.)  Ayat  maiäqm  dvaidi  (iDftM.)"
*f7rasibyS  nöit  .  .  ".  .  indem  wir  den  Äf.
mit  Bitten  bedrängen:   'nicht  .  .'"  Y.  2p.
5.         2)  'sich  drängen  (nach—)':  mit..
avästryi     davqsanä''     hum^r^isii^    (sd.)
baxitä  Y.31.J0;  VgL  "davSsa.
ai.  TgL  d/iÜnMi  'er  EChnttell'(?).  —  Vgl  Hödü- und  Gdn.  KZ.  27.  233,  Bn.  Stud.  /,  351.  — Pu.  (zu  \.2g):  shrmaad  an  i pa  Timänlt  (Sn.; sanidtAiyam)  hampurimd;  (zaY.^/j:  transskr. (davaslkä ,  in  Aw.-Buchst. ;  man  sah  später dav^  für  einen  EN.  an,  s.  DST.  ZA.  /.  330, JUSTl  NB.   82),  Sü.:  aimegak.   —    ■)  D.  i.  du.
vaidi,  s.  No.  2.  —  ■)  Könnte  auch  für  duv^ stehen,  S  26S.  12.
dby  Google
689
dava
•  j-  y<^01  «i«  dava  ^itsii  uxriltif  P. 54:  -  ?  -.
•  j.  ", .  yitn  davata  aüi  . ."  FtD.  7. ■  g.  'davant-  Adj.,  PPA.:  s.  ^dav-,
»  j.  'davant-  Adj.  (fem.  'vainil-),  PP
```


## [2026-09-05T20:05:07.507Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 150 (p.129) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==151' HRN.txt | head -60"
}
```


### [2026-09-05T20:05:09.221Z] TOOL RESULT

```
=== HRN leaf 150 (p.129) ===
- 129 -
af/. dvalas; oss. d. duades, t. duädäs.
Die neupersische Form (eine Analogiebildung) ist
entlehnt in kurd. duänzdih (hier findet sich noch
ausserdem das n von np. sänzdeh), hol. duäzdeh,
oll. (\)dö%ten *anheften, durchbohren, nähen', Praes.
döz-em, döz, dözene, kun\döz grosse Nadel' (AM. 52
ZeUe 6, 116 Zeile 2 v. u.).
maz. düj, düjene,
phlv. döc *Speer (Dat. d. 21, 8), phlv. pjiz. dö/tav,
dözEm (PPGl.)
oss. än-düzün, d. än-dozun ^befestigen (von
Stackeiberg, ZDMG. 43, 671); bei. dööag , n.
dösay *nähen (91).
578. (2)döy(ten 'melken', Praes. dös^em, dösTden, döy saure
Milch' (AM. 216 Zeile 5) ').
ai. [/"döh-, dogdhi 'melken', dögha^; phlv. dö/fan
(Bund.), dösUan (Bund., PPGL).
kurd. dötifiy düsim, di-dösim melken'; afy. Ivasal;
oss. d. docufiy t. dücifi (111); bei. dösay (94); wa;^.
dtc-am^ dögnam, sar. dauz-am.
579. dFfd 'Rauch', diidmän 'Familie.
phlv. dfit 'Rauch', dütahnan (AV.), vorgl. dütal'
'Familie' Bahmyst (Spiegel, Trad. Lit. S. 4()G); ai.
vergl. dhümä' 'Rauch'; lat. //7mMs, lit. diima-s, ksl.
dymü,
kurd, du; af/. lü; bei. düt, dlt (90); wa;^. dit, sijn.
öud, sar. düt.
580. dür 'fern'.
ap. dura- 'fern'; aw. dura''; phlv. dür\ ai. dum-,
kurd. dür; af/. liri; bei. d/lr, dJr (89); wa;^. JJr,
yidg. lüro,
581. dö»eyi 'Hölle*.
aw. (anMtis) daozaMahe, vergl. duzah" 'Hölle';
phlv. dömx (päz. diiza/, dorn/), dö^a/ (PPGl.) —
dusähü darf man das Pchlevivvort nicht losen; denn
*J Wa/. dayOWj sar. diiyoic *Molke*.
Hör II, Qrundriss d. neup. Etymologie. 9
```


## [2026-09-05T20:05:18.335Z] TOOL CALL #16: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-05T20:05:20.288Z] TOOL RESULT

```
{
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
```


## [2026-09-05T20:05:25.228Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v2 leaf 354 (p.894) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==355' BQT_v2_pages.txt | head -70"
}
```


### [2026-09-05T20:05:26.776Z] TOOL RESULT

```
=== BQT v2 leaf 354 (p.894) ===
 ‫‪4‬‬                                                                                                                            ‫حودمان‬

‫دود = بضم اول بر وزن مور ؛ معروف‬                                   ‫دودمان‪ = ۱‬با میم بورزن دوستان »‬
‫است که تقیض ترديك باشد ‪ - ۱‬وبفتح اول ‪۷‬‬                             ‫خاندان وخانواده‪ ۴‬وقبیلهرا کوبند‪ -‬ونام موضعی‬
‫خواندن درسهای گذشته بود ‪ -‬و یالة شراب را‬                                                                ‫است نزديك بشیراز ‪.‬‬
‫واسوسانی که اخبارامراواعیان‬
                          ‫نیز کویند ‪ - ۸‬ج‬                          ‫دوده ‪ = ۴‬یسم اول بر وزن بوده ›‬
‫راتحقیق نمودهبلاطین وپادشاهان نویسند‪ -‬وبمعنی‬                        ‫دودمان و خانواده راکویند ‪ -‬و دود چراغ که‬
                       ‫‪.‬‬    ‫ابام وعهد وزمان هم هت‬                 ‫بجهت‌ساختن رمکب و سياهی گیرند‪ -‬ودود کش‬
‫دور آسران = با سین بی‌نقطه بر‬                                       ‫ر‬
                                                                    ‫پ‪-‬و‬‫وطبخ و بخاربرا گیفزته اند‬ ‫حمام م‬
‫وزن زآوورران‪ ,‬نام پادشاه جادو گران‌باشد واورا‬                     ‫بزرکتی و مهتر باشد ‪ -‬وبفتح اول بمعنی دائره‬
                           ‫دوران سرون هم میگوبند ‪.‬‬                                                                                ‫است‬

                                                                   ‫بر وزن زود رج »‬                    ‫دو دهنح؟ =‬
‫دوراع = بلاقغنطه‌داربروژن سوراخ»‬
                                                                    ‫سفالی که بآن‌دوده بجهت سیاهی ومر کب‌ساختن‬
‫دوغ وماستی رکاوبند که شیردران(‪ )۲‬دوشیده‬
                                                                   ‫گیرند ‪ -‬ودردکش حمام و مطبخ وبخاربرا نیز‬
 ‫باشند » واصل این لفت دوغ راغ است مت‬
                                                                                                   ‫کونند ‪.‬‬
‫مامت دامن کوه » اشاره بايشکه شبان در دامن‬
                                                                   ‫دوهنگ ‪ - °‬بان فارسی » بروزن‬
                                                                                             ‫د‬
‫گیورسفند بماست دوشیده است چه راغ‬
                               ‫کوه ش‬                               ‫و ممتی دودهنج است که سفال و(‪ )۱‬دود‬
                  ‫‪7‬‬    ‫دامن کوه نیزآعده است‬             ‫بمعنی‬
                                                                   ‫چراغ کرفتن ‪ -‬ودود کش حمام ومطبخ و بخاری‬
‫دروان سرون ‪ - ۲‬بممنی‌دوراسران‬                                                                                                   ‫باشد ‪-‬‬


                                                             ‫‏)‪ (e‬چك‪ :‬براان ‪.‬‬                  ‫و ‪.‬‬    ‫‪- :‬‬   ‫چك‬       ‫(‪)۱‬‬


      ‫از‪ :‬دود ‪ 4+‬مان (یسو ند مان بم‌عنی‌خانه) *قاب‪ ۱‬ص‪ ۳۷‬ح* لغة بمعنی جای‌دود‬
         ‫› بهلوی ‪00‬‬                   ‫دوده‬     ‫دود خانه ‪۳‬‬         ‫) بمناسیت احاق خانواده چنانکه ‪reyof‬‏ (فر)‬

  ‫ناکهی بای وجودش بگل رقت و دود فراق ازدودمانش برآهد‪€, .‬‬                                   ‫‪۱‬‬                 ‫> ‪.‬‬              ‫«اسشق‬
  ‫«کلتان ‪. ۸۸۱۰‬‬
      ‫‪ ۰‬بهلوی ‪katûd‬‏‬        ‫دودخانه‬        ‫ِ‬   ‫دودمان‬    ‫ت‬    ‫واتصاف)‬   ‫‪( ۰‬یوند نست‬            ‫از؛ دود ا‬         ‫ك‬    ‫‪۳‬‬

  ‫‪2‬‬    ‫آهتگد»‪‎‬‬   ‫دود‬       ‫مخفف‬        ‫‪o‬‬           ‫مخفف « دود آهنج» ‪۴‬‬             ‫‪۴‬‬        ‫‪۰‬‬     ‫‪6‬‬          ‫ی استق وهویشمان‬

      ‫‪ - ۱‬بهلوی ‪۲0d‬‏ (بعید) «اسشق ‪« ۸۵‬منای ‪ > ۲ : ۲۷۲‬از ابرانی باستان ‪2۳84 -‬‬
  ‫« بارتولمه ‪ »۰۵۷‬دیبرکه ‪ » ۶‬پارسی باستان و اوستا‪ .3۲00-‬هندی باستان _ ‪arûd‬‏ ‪ .‬کردی‬
  ‫‪۲‬ففانی ‪ 1۳11۰‬بلوجی ‪ ۲04‬و ‪ ۲11۰‬وخی ‪ . ۲1‬بودغا ‪« 0701‬اسدق ابا »‪ .‬کیلکی ‪. ۲110‬‬
                                                                            ‫ا‬
      ‫‪ .‬سنگری‬         ‫* سمنانی ‪rid‬‏ و ‪۲1‬‬                ‫ص‪۳۹‬‬
                                                          ‫» نطنز ی ‪rûd‬‏ ‪ °‬ك ‪۲ ۱ .‬‬                     ‫فریزندی و برلی ‪۲0‬‬
                                ‫› ‪.‬‬    ‫« ك‪ .‬ص‪۳۰۱‬‬              ‫وشهمیرزادی ‪ . ۳1‬سرخه‌بی ‪ . ۲114‬لاسگردی ‪۲‬‬
                       ‫‪( - ۷‬مر) بسن گردیدن* منتهی الارب * کردکتن « غیات اللغات» ‪.‬‬
      ‫بدست رسانیدن پیاله های شراب در مهمانی « نام الاطا > مأخوذاز(عر)‪.‬‬                                 ‫‪ - ۸‬از دست‬

  ‫"‪« .‬دو؟ بمعنی دوغ‬                            ‫رك‪ :‬دودان سرون ‪.‬‬         ‫‪۶‬‬             ‫مأخوذ از (عر)‪. ‎‬‬                    ‫‪٩‬‬
      ‫که درنسخ‌مروج‬        ‫ات‬   ‫دور اسروب» ‪bêrsarûD‬‏‬              ‫ابن نامم صحف(‬       ‫ظ›‬         ‫‪۳۱‬‬                  ‫(ه‪.‬م ) آهده‪۰ ‎‬‬
      ‫النهب « دورشرین؟ و«دوسر؟ ودرتاریخ طبری «خوراسرو؟آمده واو سر منوش چیپر (منوچهپریادشاه‪‎‬‬
      ‫بشدادی) وجد سیزدهمین زرتشت است طبق‌سنت (رك‪ :‬مزدینا جدول برایر ص ‪ )۸1‬نه دشمن‌او‪.‬‬
          ‫( برهان فاطع ‪) ۷۱۱‬‬
```


## [2026-09-05T20:05:39.257Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"اندوه\" BQT_v1_pages.txt | head -20"
}
```


### [2026-09-05T20:05:39.320Z] TOOL RESULT

```
7617:و نرمی ومردمی وآدمت. 4- غم واندوه وتشگی
13788:و بای فارسی بر وزن اندوهمند . بمعتی ملكث
14298:| زد و۸ چم ثالث » مخفف اندوه است
16511:غم و اندوه و کناه بسیار باشد همچو: با رگیری
20329:اسوه و دلگیری - و اندوهکن و دلتنگ وفرو
23346:واندوه ‏ و فشردن کلو باشد » دباین حعنی بجای
24173:عر جسته 0 غمکین واندوهتاله را گوبند" ۰
25488:واندوهگن باشد ۵ , وباینمعئی بفتح اول وضم
25496:3 اندوهگین و بی رونق باشد - و بمعنی روی
25501:کهغمناك واندوهگین وافرده گردیده و بی‌رواق
27932:وغرور خود در اندوه است.
28333:تاسه - بر وزن کاسه ۰ بمعنی اندوه
28337:کلو بمب سیری با ملال و اندوه دیگر ٩‏ -
28404:و غ‌واندوه - و مکدر شده نیز آمده است ۴ -
28475:بی قراری و بی آرامی و اشطراب واندوه ۷ -
28539:وهحنت وهشهت و اندوه
29853:رووه- با واو مجپول بروزن اندوه »
30269:کلف خوانند - و بممتی اندوه و بی قراری دل
30668:واندوه باشده - و بضم اول وثانی . غلاف کارد
31184:درختی است که خار های بسپار یز دارد و کل | وصاحب اندوه باشد .
```


## [2026-09-05T20:05:43.056Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 388 390 392; do echo \"###### leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | head -45; done"
}
```


### [2026-09-05T20:05:44.627Z] TOOL RESULT

```
###### leaf 388
اندر خور
ا ندز خو در - بنمخای نفطه‌داروسکون
واو ممدو له و رای می‌نقعله 4 ممحنی اج وسزاوار
وزیبا باشد .
بمشی اندرخور است که لابق و مزاوار و زیبا
باشد .
آثدر خو دك هه بنکون داز ابید .
بمعنی اندرخور است که لابق و سزاوار و زیبا
باخد - و بختح رای دوبم بسمنی یبد است بعنی
می‌زید .
| نذر حور ند - بسکون نون و دال
ابجد » بمعتی انترخورد است که لابق و سزاوار
وزیبا باشد .
) فلرد ۱ - بلزای حوز بروز نکمعرش,
بمعنی پند وصیحت - وحکایت و وصیت باشد -
و بمعنی کتاب ونوششه هم بنظرآعده باشد .
اندررا بروزن صندل اه کاو زهر را
گوبند . وآن حنگی است که درمیان زهرء کاو
با شیردان او متکون حبشود ۰ و آنرا عربی
حجرالبق رکویند . ۱
انفد وا با واه بروزن اندرزاابمعنی
سر گشته‌وحیران‌باشد - وبمعنیآرزوو حاجتمندی
هم هست - و سرنگون آریخته و واژ گونرا نیز
کوش .
3 شش :- واحتیاج ۰
و۷ -
| ندر و از - با زای فارسی بر وزن
چنبر باز , بمعنی آندرواست که سر کشته وحیران
و آرزو و حلجتمندی - و سرنگون آویشته
باشد .
اند واه ۲ ع بروزن لشگ ی گاء»‌بمعنی
اندرواژ اس تکه س رکشته رحیران - واحتیاج -
وسرنگون آوبخته باشد . .
| ندد و ای" بروزن‌سندل‌سای,یمعنی
اندرواه است که صر گشته وحیران و احتیاج (۱)
وسرتگون آویخثه باشد .
| نددوالی " - بروزنک پروایی: بمحنی
ب کشتگی وحیرانی - و آرزو و حلجتمندی -
وسر‌دگونی باشف .
ندر وب س بفتح اول وضم ثالث‌پروزن
کند کرب . نام نوعی از جوشش باشد که پوست
بعربی قوبا کوبند .
اندروخون ه بن خای شله دار
رسممی سطیر ار تال باشد .
| ندروسص - بر وزن سندروی ؛ تلم
###### leaf 390
انسجان
که کرفتگی دل ودلگیری باشد .
اندهان بروزن مردمان ؛ جمم انده
باشد چنانکه جانور را جانوران ومردمرا عردمان
کویند . واین جمم بخلاف‌قیای است چه‌بنیراز
جاتور را بالف ونون جمع وان کرد .
نده‌قو و » بت دوقاف و سکون دو
واو ؛ دوایی‌است که آنرا حندقوفی‌خوانشد * کلف
را نافع است ,
انفی ‏ بر وزن لندی » بمعنی خاسه
باشد که درعقابل خرجی‌است - وبمعنی‌امیدواری
هم آمده است - وبجای لفظ بودکه.و باشد که
هم استعمال میکنند - وبمعنی‌آن لحظه هم‌هت
" وبمعنی تیزهم آمد» است که بعربی‌ایضا خوانند .
اند یدن عه بر وزن خندیدن . سمحنی
تعجب کردن باشد - و سخنی را ليز گونند که
از رویه خك وزرب تک کته شود .
اند یشه - بر وژن هم پیشه » بممنی
فکروخیال باشد - و بمعنی فری ویم هم آمده
است .
) ند باث بروزن نزديك , لفظی است
از کلمات تمنی که در غربی لیت و لعل وعسی
۱ -رك : اندوب واندوج .
بقیه ازصفحةٌ ۱۷۱
(9
کویند بعنی باشدکه و بود که و بابد که -
وبمعنی زبرا, که و از برای آن واز ابنجهت‌هم
گفته‌اند .
) نفد و ه با ذال قطه دار و رای‌بی شطه
پروژن لبلبو » پا زهر باشد و انرا فاد زهر نیز
کوبند , وبجای زال نقطه دار زای هوزهم آمده
اشنت: ۵
افر » بفتح اول وانی‌وسکونرای‌فرشت»
هرچیززشت وید را کوشد .
اثر وب بر وزن منکوب » جوششی
است با خارش که بمربی فوبا خوانند و بعضی
گونند جوهدی است که آنرا شارسی گر
و بتازی جرب خوانند , و با زای نتطه دار حم
کنته اند ۱ .
انز دو - شم اول و زای هوز و رای
فرشت بواو رسیده » سحنی بازهر است وفاد زهر
نی گونشه .
افز دوت »بر وزن و معنی عنزروت
است» وآن صمفی باشد نلخ که بیشتر درمرهمها
بکاربرند؟ وعتزروت معرب آنست » و در مود
###### leaf 392
اگارده است که افسانه و سر گذشت باشد .
انگاده ۱ ه بروزن عموارء ."هر چیز
"که افانه وس گذشت داشد - وباد گذشتها کردن
رانیز کوبند - و ازسر گرفتن سر گذشت وافانه
را عم گفته اند بطریق کنابه چنانکه ا گر کسی
بسیارومکرراز گذشته بگوید گویشدهانگاره‌میکند»
یعنی باز از سر هیگیرد - و پس پی خزنده از
شرم و حیا را نیز کوبند - وبمعتي دفتر وحساب
و نامه اعمال هم نوشتهاند .
انگادیدن ۱ » بر وزن ترسانیدن »
بمعنی هو رکردن وینداشتن ‏ و گمان بودن‌باشد .
اناد » با زای‌هوزبروزن پرواز .افزار
آن اووات است .
انگاشتی ۱ -بر وزن برداشتن. بمعنی
صور کردن و نداشتن و کمان بردن باشه. .-
انگام ۴ » بروزن و معنی‌هتگام است
که موسم و وفت باشد .
انگاهه ۲ - بر وزن و معنی هنک‌امه
۱ راد : انگاردن ۰
۳ ت ازمادهٌ اذیدمن» رژد انجمن.
ات
است که مجمع و انجمن بازیگران و قصهخوانان
ا لگیین ۴ - با بای‌ابجد بروزن‌عنبرین,
سل و شهد را گوبند .
انگیینه - بروزن شنبلیله , نام حلوامی
است و ان قلن باشد که نيك بقوام آورده‌باشند
و برطبقی ریزند تا سخت‌شود و دندان کیر گردد .
انگدان ه بنم نالك ودال بالف کشیده
بروزن مردمان , شنای را گوبند یمنی دمومردم؛
و آن جانوری باشد وحشی شبیه بادمی ؛ و در
جاوتری میگوبند واه اعلم - و نام درختی حم
نقطهدار هم آمذه است - و نام قربه‌است‌ازفرای
کاشان که بانگوان اشتهار دارد.
انگرده ۳ بشم ثالث بروزن‌افرده. دانةً
انگور که از خوشه جدا شده باشد . ۱
افگر یز - بکون‌نالت بروزن‌دنگریز,
رستنی باشد و گل‌آن مانندگل خسك زرد.متود
و اطراف آن خار دارد و انرا بعربی قرطم بری
خوانند » و بیونانی طریفان کویند - و نوعی از
شه ازصفحهٌ ۱۷۳
يب ۲۳۵ ۰ رك : انگزد .
« نیب گی۰۹٩‏ >.
```


## [2026-09-05T20:05:53.839Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==390' BQT_v1_pages.txt"
}
```


### [2026-09-05T20:05:55.584Z] TOOL RESULT

```
اف
او رفتی . بکشب بای شد و آتش را بکشت
راندروی درمیان دربا کم کردید ..
سین می‌نقطه , نام یکی از حکمای بونان است
گوند درطبابت اعجاز مکاربردی ۴
نلم مکی از مبلوزان تورانیی است ۳
دوازده د بردست گر کین ملاد کشنه شد" شلد ,
| ند ۴ بسکون کاف , تسضر اند
است , واند عددی باشد مجهول میان سه و نه
و انرا بعربی بضم خوانند - وهرچیز کم را نیز
نس ,۰
ند گان بروزن بند گان ۰ نلم‌شهری
۳ است مایین سمرقند و چین ء معرب آن
اند دی نم‌اول وثالثولام ۳
نانی وسین م‌نقطه » نام شهرست درحدود حغرب
- ونام جزیره‌ای هم هست‌در بالای کوهی ؛ وبهر
دوممنی فتح اول و ثالث ورابع هم امده است
! ند مه ‌ بروزن صردهه: » باد آوردن
غمپای گذخنه باشد .
که درمقایل بیرون است
ی
خبون وبرادر اراس
«مناس۹ ۲۷ .راد: ۳
اند
کرداند . آنرا بعربی قوباکویشد .
افو ج -بروزن محلوج» بمعنی‌اندوب
است وآن جوششی است با خارش که عرب قوبا
شف
] ند و خقی* - بروزن‌افروختن» بمعنی
جمم کردن وفراهم آوردن باشد - بمعئی قرض
و ایس دادن ‌‌ زد ابیت
اند‌و.- وزن مقصود ۰ کاهمگل
) ندودن۱ - بروزن‌فرمودن . کاهگل
و کلابه مالیدن باشد - ومطلا وملمع کردن دا
نیز کوید .
ا فك و ۷ - بروزن سردوز؛ بمعنی‌فراهم
آورده وجمم کرده شده باشد - وامر باین حمنی
همست عنی جمع کن وفراه آور .
اندول بروزن ممقول ۰ کلیمی باشد
کهآنرا برچهارچوب بامیخها سکم کنندوبجهت
استراحت برآن نشینند . و این در ملك زنگبار
مصمول است »
| ندو ف » بنتح رابع وسکون نون‌ودال
ابجد » از انباع است بمعنی تار وعار که زبروزس
شده رازهم باشدم باشد .
آف‌وه٩‏ - بروزن انبوه , گرشکی ول
ودلگیربرا اگوبند ف
| زد و۸ چم ثالث » مخفف اندوه است
» و اوزن ۳6000۲ ومادر ۸5۷۵۵
۴ - نیز اندیرما, در اوستا
۴ پهلوی 12702۷ (کم »کمی)
فعه در صفحة ۱۷
```


## [2026-09-05T20:06:05.507Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==391' BQT_v1_pages.txt | tail -30"
}
```


### [2026-09-05T20:06:07.274Z] TOOL RESULT

```
) ند باث بروزن نزديك , لفظی است
از کلمات تمنی که در غربی لیت و لعل وعسی
۱ -رك : اندوب واندوج .
بقیه ازصفحةٌ ۱۷۱
(9
کویند بعنی باشدکه و بود که و بابد که -
وبمعنی زبرا, که و از برای آن واز ابنجهت‌هم
گفته‌اند .
) نفد و ه با ذال قطه دار و رای‌بی شطه
پروژن لبلبو » پا زهر باشد و انرا فاد زهر نیز
کوبند , وبجای زال نقطه دار زای هوزهم آمده
اشنت: ۵
افر » بفتح اول وانی‌وسکونرای‌فرشت»
هرچیززشت وید را کوشد .
اثر وب بر وزن منکوب » جوششی
است با خارش که بمربی فوبا خوانند و بعضی
گونند جوهدی است که آنرا شارسی گر
و بتازی جرب خوانند , و با زای نتطه دار حم
کنته اند ۱ .
انز دو - شم اول و زای هوز و رای
فرشت بواو رسیده » سحنی بازهر است وفاد زهر
نی گونشه .
افز دوت »بر وزن و معنی عنزروت
است» وآن صمفی باشد نلخ که بیشتر درمرهمها
بکاربرند؟ وعتزروت معرب آنست » و در مود
الغضلا باین ععتی با ذال نقطه‌دار و بای آیجد ‌‌
آمده است که انذروب باشد .
۷ ره : اندوختن.
. درونی؛ داخلی . باطنی‎ > ٩
* بارتولمه ۹۸۸ * تیب ک۱۰۰۵ که
```


## [2026-09-05T20:06:21.478Z] TOOL CALL #22: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/ 2>/dev/null | head -30; echo \"---\"; timeout 300 python3 tools/ref_page.py BQT:171 --image 2>&1 | tail -30"
}
```


### [2026-09-05T20:06:23.292Z] TOOL RESULT

```
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
---
no scan of BQT covers printed page 171 (see 'scans' in refs_online.json)
```


## [2026-09-05T20:06:30.893Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG dau ===\" && grep -n -i \"andōh\\|andoh\\|handōh\\|handoh\" CHEUNG.txt HUB.txt HRN.txt PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt 2>/dev/null | head -30"
}
```


### [2026-09-05T20:06:30.947Z] TOOL RESULT

```
=== CHEUNG dau ===
PHD.txt:3741:Sorrow andag, andoh, bēš, pim, témar, zarīg. sorrowful andag(g)én, andēhgēn,
HUB.txt:4995:= koh 'Berg'; anduh = andoh *Kummer : htiS = hds 'Ver-
PHD_mackenzie.txt:1094:andOh ['ndwh I M 'ndwx-, N.....,] sorrow.
PHD_mackenzie.txt:7513:sad andiig(g)en, andohgen, zarig-          seam darz.
PHD_mackenzie.txt:7633: sorrow andag, andoh, bes, pim,         spoil wimustan, winahidan.
PHD_mackenzie.txt:7635: sorrowful andag(g)en, andohgen,           winastag.
PHD_mackenzie.txt:12060:anagran, awcran              \~t'"           andohgcn                    ,\~ t-~
NYB_vol2_glossary.txt:1894:handóhakan [hndwhkn'] anxious 4?. — Also handöhaken, J.-Prs ’ndwhgyn Isa 1:2. Arm. lw. andohakan ‘disquieting, dreadful’.
NYB_vol2_glossary.txt:7504:Armenian andohakan: handöhakan apa: ap
CHEUNG.txt:26033:*NWIR: NP tuxSidan ‘to strive’, taxsa ‘diligent’ || (+ *ham-) NP andoh ‘anxious’ 
CHEUNG.txt:26037:*MISC: (+ *ham-) Arm. (LW) andohakan ‘dreadful’ 
CHEUNG.txt:34895:"ndwh /andoh/, 400 
CHEUNG.txt:40704:andoh, 400 
CHEUNG.txt:52273:andohakan, 400
```


## [2026-09-05T20:06:35.311Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25990,26045p' CHEUNG.txt"
}
```


### [2026-09-05T20:06:35.357Z] TOOL RESULT

```
(Aeol.) съркес̧ (pl.) ‘(pieces of) meat’, ? Olrish turc (m.) ‘boar’, are semantically 
possible, but not very informative with regard to morphology and derivation. 

«PIE? > LIV: 656 | Pok.: 1102 


*QuaxS (tux&) ‘to be busy, working on’ 

*AVESTAN: Av. Ofaxs- ‘to take care of’, OAv. @BaxSah- (n.) ‘effort, work’ (Y 33.3, Y 
46.12) > Liste: 26 

Pres. them.: IND. 3pl. med. YAv. 0Baxsonte (Yt 10.14), INJ. 25р. OAv. 0Baxšo (Y 29.2); Partic.: pres. 
med. Y Av. 0Baxsomna- (Yt 5.65) 

*OLD PERSIAN: (+ *ham-) ha™taxs- ‘to work with, effect’. © Cf. Kent, Le: 
"contamination of *tas- ‘to cut, form’, Skt. taks- ‘form by cutting’ ... and pAr. 
*tuaks-, Av. Owaxs- (mid.) be busy’ ...". = Kent: 185b f. 

MED.; Pres. them.: IND. 3sg. ha"taxsataiy <h-t-x-3-t-i-y > (DNb 16), impf. lsg. hamataxSata 
<h-m-t-x-3-t-a> (DB 4.65), «h-m-a-[t]-x-&-t-a > (DB 4.92), 3du. hamataxsa" tà «h-m-t-x-&-t-a» (DB 4.82) 
*MIDDLE PERSIAN: MMP twxs- ‘to strive, be busy with, diligent’, BMP twhs- /tuxs-/ 
‘to strive, struggle with’, (sec. caus.) MMP twxsyn- ‘to make diligent, industrious’ || 
(+ *ham-) BMP ’ndwh /andöh/ ‘sorrow’, MMP ’ndwxyn ‘sad, sorrowful’ 
c DMMPP: 33 1b, 47a 

Pres.: IND. 3sg. BMP twhsyt /tuxsed/, 3р1. MMP twxsynd, MMP twxsynd, IMPV. 2sg. BMP twhs /tuxs/; 
Partic.: pres. MMP twxs’g, (pl. MMP twxš’g’n ‘striving’, perf. pass. BMP twhsyt /tuxsid/; Inf.: BMP 
twhsytn /tuxsidan/, caus. MMP twxsynydn 

*PARTHIAN: twxS- ‘to strive, be busy with’ = Ghilain: 48 | DMMPP: 331b 

Pres.: IND. 3sg. "twxsyd, 3р1. "twxsynd 

*SOGDIAN: (+ *ham-) BSogd. ’nt(’)wxs, CSogd. ’ntwxs, MSogd. ’ndwxs ‘to strive, 
endeavour’ 

Pres.: IND. 3sg. BSogd. ’nt’wxst, 3р1. (subj. ?) BSogd. ’nt’wxs’nt, SUBJ. 15р. BSogd. ’nt’wxs’n, OPT. 
lsg. CSogd. "ntwxsym ’zw (Weber 1970: 152), 3sg. MSogd. "ndwxsyy, IMPV. 2р1. BSogd. ’ntwxst’, 
MSogd. ’ndwxsö’, Partic.: pres. BSogd. ’nt’wxs’k, BSogd. "ntwxs'k, MSogd. *’ndwxsy (BBB: 39); Inf.: 
BSogd. ’ntwxs’y, BSogd. ’ntwxs’k, pret. BSogd. ’nt’wxs’t 

*CHORESMIAN: (+ *ham-) ’ndyx (m.), ‘пах (m.) ‘sorrow, sadness’ 

*NWIR: NP tuxSidan ‘to strive’, taxsa ‘diligent’ || (+ *ham-) NP andoh ‘anxious’ 
*NEIR: Oss. I. tyxsyn/tyxst, D. tuxsun/tuxst ‘to be restless, confused, concerned; to 
be burdened; to be in a difficult situation; to succeed in’ 

*MISC: (+ *ham-) Arm. (LW) andohakan ‘dreadful’ 

*SANSKRIT: tvaks ‘to be working, active, strong’ (RV) = EWAia I: 683 f. 


*yab/fl 401 


9 This Ш. root has no certain IE correspondences. It is interpreted as a desiderative
```


## [2026-09-05T20:06:49.693Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"davaθ\\|davath\\|davaOe\\|davat\" BRT.txt | head -20; echo \"--- thwaxsh ---\"; grep -n \"Owax\\|θβaxš\\|Þwax\\|0Bax\\|Owaxs\" BRT.txt | head -10"
}
```


### [2026-09-05T20:06:49.772Z] TOOL RESULT

```
2464:yat  baväma  aiwi.vanyn  dänavö  . .  ahmi gal'ie  piianähu  Yt.5.73;  —  ahmäi  J/ri- n?nti .  ./ravalayö  buyiil  ahmi  nmäne  giusia va^wa  ..  ". .  dem  . . ;  in  dessen  Hause  . ." V't.  jj-sif.;  Y..;j.6  (s.  2  2  aa);  —  auch bei  Beziehung  auf  das  Subjekt  des  Satzes: (ya^a)nar>m ..  asavamm*jas?nSfm  ahmya nmjne  .  .  paiti  taröpi^wim  dai'i^yät  "als ob  er  einen  Gläubigen,  der  in  sein  (zu ihm  ins)  Haus  kommt  .  ."  V.y.aa;  — naSca  ,  .  *hö  nl  ahmat  haca  gätaot  isaetci fraiütöip  nöit  apaiiitöit(%A.)'B.23.  b)  sub- stantivisch: adä  (sd.)  ta^a  guti  p>r9- sat  as>m  .  .  ahmäi  asä  (als  Subj.)  ,  ■  paitl.- mravat  Y.ag.ii.;  30.t,  46.8,  13;  —  uz- valoayat  zara^ustrS  annm  mainyUm  .  . paiti  ahmäi  adavata  .  .  aarS  mainyus  .  .
5014:•  ').  a-vadö.urvatay-  Adj.  'der  einen  Ver- trag durch  das  (blosse)  Wort  abzuschliessen nicht  quaÜfizirt  ist' "';  myazdava  ratus amyaxdavatum  ratunafm  'vaitlm  aaste antarf  masdayasnäii  ".  .  macht  (erklärt) der  Ä. . .  den  . .  Laien  für  unfähig,  durch das  (blosse)  Wort  einen  Vertrag  abzu- schliessen" A.J.8.
8209:Verben  des  Sprechens  und  Denkens;  a)  auf die  folgende  direkte  Rede  verweisend:  °A' aojanö  (uifyae/anS,  °ti  vacsbts  aojanS)  Yt. /0.53  usw.";  —  °tX  mravat  Y.^j.a;  — aiiasca  °ti  V.  4-Ali  N. J7;  —  °ii  fravasata Yt /4-54t '7'i8,  ai;  —  'li  davata  \.sg.i, 44,  Yt/7.19;  *i9.47",  FrW.io.41;  —  Ui maiikäns  YL/iJ.47.  b)  iD  die  direkte Rede  eingeschoben:  ulla  ahinai  .  .  —  'ti tiiraof  ahurS  mazdü  —  ..yahinäi..'^X.io.\yi; 79.53,  V./A'.i,  VyL //(?),  43.  2)  'so',
10687:\vlvar?zdavatB  yalä  Y.p.30;    —    spaoaA^
12480:•  j.  'daeva-  Adj.  (fem.  'dapvj-)  'den Dapva  zugehörig,  von  ihnen  herrührend (usw.),  rfa?iisch':  kB  asti  'vö  ks  da^aySzB "wer  gehört  zu  den  Z>.,  wer  ist  ein  Z>.- Anbeter?"  V.Ä31;  32';  —  kva  asti  'vB kva  datvaydzB  Y.y.sz'y  54'.  yt77.6;  — yat  nürsm  vyämbura  (sd.)  'va  maSyäka da^vayäsB  vohuntm  vä  täc^änti  YL  7^.  54; — -  ga%Bittsca  'vJsüa  *handramana  (sd.) N.  5j;  Yt.  77, 6.  et)  sonst  von  drug-: aiXm  dahaktm  ..  'vTm  *dru/im  V.5. 8;  — Hat  ki  ha,  paiti.davata  ya.  'vi  druxl  V. 18.  $1;  —  nase  °vJ  druxs  SrB.j;  — sraosim  ..yd  janta  °vaya  drujB  Y.57. 15.
12799:—  uspatat  Jranroie  .  .  ayqm  daoihrim daomns'*  Yt. 75,57;  —  aHs  daksk5  .  . saxsä^nm  daomnö*'' \t.ig.\T.  3)  das Gesagte  folgt  in  direkter  Rede:  adavtita (Augm.)  avrS  mainyuf:  mä  .  .  H.  2.  35; Yt^.  14;  —  ktnsanJm  ..yS  davata:  nsit «?  .  .  Y.  5.  34;  —  advännta  adäunta (Augm.)  dafva  V.  ig.  45;  45,  47.  a)  mit uiti:  uiti  davata  Äi  y}  .  .  ai?rö  mainyus; drvxf  upa.dvilra  V.  ig.  i ;  44,  Yt.  77.  1 9, Vyt^;  —  büiyqsta  .  .  uiti  aoj?mna  uiti daomna:  yfafsata  .  .  FrW.  10.  43.
12802:und  folg.  dir.  Rede:  paHi  a&mai  adavata (Augm.)  .  .  aarB  mainyui:  mä  ml .  .  V. ig.6;  —  druxi  hl  paiti jd<tvata:skiäara .. v.ig.y,  JA  31.
12803:mit  /r3  nnd  vi  'hin  und  her  reden': fradavata  vtdavata  fi-amof^fota  vlmaigiata ar»HJ  mainyu/  "es  redete  hin,  es  redete her,  es  überlegte  hin,  es  Überlegte  her AM.''  V.jp.43.
12828:•  j.  ", .  yitn  davata  aüi  . ."  FtD.  7. ■  g.  'davant-  Adj.,  PPA.:  s.  ^dav-,
13417:adavata  .  .  atJrS  mainyui:  mä  t, mirmcavuha  .  .  kahe  vaca  vanji  . .  mann 'ma  atirS.mainyus  V.  ig.  5—8;  —  nalcis xsayät  .  .  arrrö  mainyus  .  ,  ^aliu  'mohu YrVil.4.2.        \y.ig.iy.  lies  dämi4ät3m\
14186:htn  . .  yö  äxstisca  . .  'u/s  (sd.)  spasys  (sd.) sffniäaAeYtit.14.  e)  von  einerspeziellen Gegnerin  des  Sraola :  sraosrm  . .  yS  JarUa daiciaya  'ujS  as.aojar>hs  *aAü.ittirynce  Y. 57.  15;  —  sraosS  .  .  'upm  jaynisto  Yt II.  y,  —  sraosS  ..'ußm  apansat  apayüxtai paiti  vatrat  'uxs  (als  Vok.)  ai^ä^re  .  ..- tum  .  .  aiva  .  .  anaiwyostis  AunaAi?  dat .  .  paiti.davata  ya  dagvi  'uxf  .  .  V.  j8. 3of.*'.  0   sonst:    *«»/  *tai  paiti  -uxs
19737:mit  /r3  und  vi  'hin  und  her  überlegen': fradm/tüa  vXdavata  (sd.)  framatefata  vf- manyata  atarB  mainyui  Y.  ig.  43.
19991:—  msnnlaiie  (3SPM.)  vlspqm  daiiihaom tnairys  .  .  Yt  io.  2 ;  V.  21.1;  —  ata  datva vlspä  *m»rancfnta^>  yä  .  .  Yt  6^.  3;  — druxi  upajtoära  imrfncaauha  assum  sara- %usira  (statt  Akk.)«'  V.  75.  I;  —  paiti ahmäi  adavata  . .  anrS  mainyul:  mS  mi dqma  mirmiar3uha..tara%u^traN.ig.f>'°'>;
22409:*  j.  va<)a')^n-  m.  EN.  eines  glaubensfeind- lichen  Fürsten:  adavata  ..  aarS  mainyui: ,  ,  tard^uilra  .  .  apastavartuha  .  .  dabtqm mätdayasnJm  vindäi  ystum  ya^a  vindai °nS  (NS.)  ■'  daiähupaitis  ". .  Zar. !  schwör der  maid.  Religion  ab,  um  die  Gunst  zn erlangen,  wie  sie  der  Landesherr  V.  er- langte" V.J5.6;  —  •7a(NS.)  Y.8'\
23085:Vgl.  n-ar,I«a..  -  ai.  z^rna.  m.  EN.  -  ■)  Es ist  das  die  anter  'var/ina-  No.  erwähnte Formel.  In  der  Münchener  Hds.  lautet  sie: i-ar/inait  ^jvqrn  aifhi  aruittSU  JqmäsfaHoMe pa%rahe  faAritn  i^Uifni  amä  yim  davata (fol.  5)  dßf  afa%alö  failim  ä/vm  dtfnia  nvyq- itdi'i  hväiilS  HöU  i3naiti  nMt  ami  h-ttti  x'äiJ Sitte  yaza,  aä%3  änmi  tSyeile  yavaica  yavatläi- lai/a  aUm  vehu.  Die  Hds.  enthält  noch  einige andere  Formeln  von  gleichem  Kaliber.
23261:paiti  ahmai  adavata  .  .  anrö  mainyttl .  .
24898:'jammern,  heulen',  im  gAw.  nur  vom  Rind gebraucht,  dagegen  imjAw,  nur  von  dafvi- schen  Wesen^';  a)  im  gAw.:  aica  gSus urv3  raostä  "und  ein  Jammern  erhob  da die  Seele  des  Stiers"  Y.  2g.  9.  a)  Kaus. 'jammern  machen':  yälä  kavä  *qnmSnT urüdsyatä  "und  wie  der  K.  es  (das Rind)  unaufhörlich  jammern  macht"  Y. 44.  »o^>.  b)  im  jAw.:  yai  pi/irif(sd.) dayäj  aal  daeva  uru^sn  y.J.^i;  —  uru- %?ftta  adäunta  dalua  drvarüB  V.  79. 45; —  k^nsänXm  .  .  yS  raosta  xsdkrS.kämya yS  davata  "den  K. . .,  der  jammerte  in  der Sorge  um  seine  Herrschaft,  der  sagte . ."  Y. g.24;  —  uruhajF.g.  S.  noch  "aparB.
27815:die  Erzählung  von  Zar.%  Versuchung: ,  .fradvarat  a*tr5  mainyus. .  uiti  davata .  ,.■ druxs  upa.dvära  nurmcanuha  aläum  'ra (statt  Akk.)-  druxl  hi  pairi.dvarat  .  .  'rS akumin  vairlm  frasrävayat . .  drux/  ht . . apa.dvarat . .  paitüdavata:  . .  ar»ra  mainys ndit  hl  aosS  pairi.vainämi  spilamai  'räi; pouru.ii'annatihd  alava  'rö.  'rS . .  pairir vamäi:  dafva  ml  ..  aohm  hqmpirfst^e. usihUtat  'r5  fra^üsat  'rS  asants  , .  asänS zasta  drazimnö . .  vindimnS  da%u!s  ahurai mazdäi . .  uzva^ayat  'rS  anrim  mainyam: .  .  janärii  dqma  daSvU.d(tt}m  .  .  yahmai *mxayäiti  saofyqs , .  paiii  akmäi  adavata . . anrS  mainyul:  mä  midqma  mtntUaituha asäum  'ra  tum  ahi  pouruiaspahe  puhrB bart^ryät  haca  zaz'W{sd.)  apa.siavamika  .. damqm  mnzdayasnXm  vindai  yjntm  ya%a vindat  va)iayan3  .  .  paiti  ahmäi  ava^ata yö  spttSmS  'r5:  ndil  .  .  apa.staväne  .  . daiiiqm  matdayasnJm  "..machte  sich^^^. heran  . .  so  sprach  er  . . :  ^Drug,  geh  hin, töte  den  heiligen  Zar'  Die  Dn^  ging um  ihn  herum  , .  Zar.  sagte  den  AhV. auf. .  ,  Die  Drug  wich  . .  vor  ihm  zurück  . . sie  antwortete:  ', ,  AM.,  ich  kann  des  Ver- derbens für  (ihn,  für)  den  Spit.Zar.  nicht gewahr    werden;     der    heilige    Zar.    ist
--- thwaxsh ---
```


## [2026-09-05T20:06:59.729Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && for L in 389 390; do curl -sL -o bqt_n$L.jpg \"https://archive.org/download/borhan-ghate-v1/page/n$L.jpg?fit=bounds&w=1600\" ; echo \"n$L: $(file bqt_n$L.jpg)\"; done"
}
```


### [2026-09-05T20:07:08.209Z] TOOL RESULT

```
n389: bqt_n389.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
n390: bqt_n390.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
```


## [2026-09-05T20:07:12.690Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && which convert magick pdftoppm; for L in 389 390; do convert bqt_n$L.jpg -crop 2479x900+0+2500 +repage -resize 1400x bqt_bot$L.png 2>/dev/null || magick bqt_n$L.jpg -crop 2479x900+0+2500 +repage -resize 1400x bqt_bot$L.png; done; ls -la bqt_bot*.png"
}
```


### [2026-09-05T20:07:14.966Z] TOOL RESULT

```
/usr/bin/convert
magick not found
/usr/bin/pdftoppm
-rw-rw-r-- 1 sfmqrb sfmqrb 154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb 168738 Sep  5 16:07 bqt_bot390.png
```


## [2026-09-05T20:07:17.177Z] TOOL CALL #28: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt_bot389.png"
}
```


### [2026-09-05T20:07:17.213Z] TOOL RESULT

```

```


## [2026-09-05T20:07:21.786Z] TOOL CALL #29: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt_bot390.png"
}
```


### [2026-09-05T20:07:21.803Z] TOOL RESULT

```

```


## [2026-09-05T20:07:42.521Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ tufan ===\" && grep -n -i \"Tufan\\|tūfān\\|Ṭūfān\" FVQ_pages.txt | head -10; echo \"=== AFM/TAD/ARB tufan ===\"; grep -n \"طوفان\" AFM.txt TAD.txt ARB_mo3rb.txt LKT.txt 2>/dev/null | head -10; echo \"=== LKT taifun ===\"; grep -n -i \"taifun\\|tufan\\|typhon\" LKT.txt | head -10"
}
```


### [2026-09-05T20:07:42.601Z] TOOL RESULT

```
=== FVQ tufan ===
=== AFM/TAD/ARB tufan ===
ARB_mo3rb.txt:10205:بناها » فعربت فقيل ” حران ©' ٠‏ وذ قوم أنها أول مديتة بنيت على الأرض بعد الطوفان » 5 
ARB_mo3rb.txt:24619:() « الموس » الطوفان باللبل والطلب ججرأة » وأطوس أيضا : شدة الأكل» ركلاها يصلح 
=== LKT taifun ===
4487:1990.  Chin.  t'ai-fnng: Zusammensetzung  aus  chin.  Tai,  Ab- kürzung für  Tai-wan,  Namen  der  Insel Formosa,  und  fung  'Wind',  also  eigent- lich 'Formosawind' ;  hieraus  zur  Bezeich- nung eines  Zyklons  in  den  südchinesischen Gewässern  engl,  typhoon,  dtsch.  Taifun, Teifun;  frz.  typhon.  Erst  über  ar.  füfän 'heftiger  Sturm'  entstand  pg.  tufäo,  to- fano.  —  Auch  die  Ableitung  aus  tai 'groß'  und  fung  'Wind',  also  'großer, d.  h.  starker  Wind',  hat  aus  semantischen Gründen  manches  für  sich.  [Hirth ChinFW  210/212.  Hobson-Jobson  947 bis  950  [mit  Anführung  anderer  z.  T. lächerlicher  Etymologien].  Lammens Rem  242/243.
```


## [2026-09-05T20:07:50.387Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"ufan\\|awpan\\|taufan\\|Tftfan\\|deluge\" FVQ_pages.txt | head -20; echo \"=== AFA ===\"; grep -n -i \"ufan\\|awpan\" AFA.txt | head"
}
```


### [2026-09-05T20:07:50.448Z] TOOL RESULT

```
108:Qur'iin citations is throughout that of FRigel's edition, not the Kufan
2707:Some held that it has no derivation, being A^ - : the Kufans in
2746:final A takes the place of an initial u. The Kufans took it as a con-
5806:inscription (where we read (iv, 63-4) naiy draufana aham, naiy
7516:The Deluge.
7526:Mandaean meaning deluge in general (Noldeke, Mand. Gramm., 22,
=== AFA ===
```


## [2026-09-05T20:07:53.399Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7505,7545p' FVQ_pages.txt; echo \"--- leaf/page ---\"; python3 -c \"\nt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('The Deluge.')\nprint('leaf',t[:i].count('\\f'),'printed',t[:i].count('\\f')-17)\""
}
```


### [2026-09-05T20:07:55.314Z] TOOL RESULT

```
4 See Kunstlinger, " Tur und Gabal im Kuran," in Rocznik Orjentalistyczny, v
(1927), pp. 58-67.FOREIGN VOCABULARY OF *THE QUR^AN 207
as we learn from as-Suyutl, Ilq, 322, thought that it was a Nabataean
word.
Heb. HISS TTtrpa, from meaning a single rock or boulder, conies
to have the sense of cliff, and Aram. NT)B is a mountain. So in the
Targums TO"! JO1B is Mt. Sinai, 1 but the t llx^ j? of the
Qur'an is obviously the Syr. ^i^CD io which occurs beside li
> 1 > m% 2
(Tufdn).
vii, 130 ; xxix, 13.
The Deluge.
The Commentators did not know what to make of it. Tab. tells
us that some took it to mean water, others death, others a torrent of
rain, others a great storm, 3 and so on, and from Zam. we learn that yet
others thought it meant smallpox, or the rinderpest or a plague of
boils.
Fraenkel, Vocab, 22, recognized that it was the Rabbinic K391CD
which is used, e.g., by Onkelos in Gen. vii, and which occurs in the
Talmud in connection with Noah's story (Sank. 96 a ). FraenkePs
theory has been generally accepted, 4 but we find X'WBIC) in
Mandaean meaning deluge in general (Noldeke, Mand. Gramm., 22,
136, 309), 5 and Syr. Uao is used of Noah's flood in Gen. vi, 17,
and translates KaTaKXva/JLO^ in the N.T., so that Mingana,
Syriac Influence, 86, would derive the Arabic word from a Christian
source.
The flood story was known before Muhammad's time, and we find
the word jli^L* used in connection therewith in verses of al-A'sha
and Umayya b. Abi-s-Salt, 6 but it is hardly possible to decide whether
it came into Arabic from a Jewish or a Christian source.
1 Vide Onkelos on Ex. xix, 18.
2 Fraenkel, Vocab, 21 ; Mingana, Syriac Influence, 88 ; and see Horovitz, JPN,
170 ; KU, 123 if. ; Guidi, Delia Sede, 571.
3 It can hardly be connected, however, with the Gk. rv<f>u>v.
4 Hirschfeld, Beitrage, 45 ; Horovitz, KU, 23 ; Massignon, Lexique, 52 ; Well-
hausen, ZDMQ, Ixvii, 633.
5 Also on the incantation bowls, cf. Montgomery, Aramaic Incantation Texts,
Glossary, p. 290.
6 Al-A'sha in Geyer, Zwei Gedichte, i, 145 = Diwan, xiii, 59 ; Umayya, xxvi, 1 ;
xxx, 10 (ed. Schulthess).208 FOREIGN VOCABULARY OF THE QUR'AN
iii, 43 ; v, 110 ; vi, 2 ; vii, 11 ; xvii, 63 ; xxiii, 12 ; xxviii. 38 ;
--- leaf/page ---
leaf 224 printed 207
```


## [2026-09-05T20:08:05.441Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON تیفوس ===\" && grep -n \"تیفوس\\|تیفوئید\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10; echo \"=== MON طوفان ===\"; grep -n \"طوفان\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10"
}
```


### [2026-09-05T20:08:05.526Z] TOOL RESULT

```
=== MON تیفوس ===
incoming/MON/MON_2vol_Adena_v2_djvu.txt:16066:بیماری‌های عفونی (ذات‌الریه» تیفوئید) 
MON_part2.txt:16066:بیماری‌های عفونی (ذات‌الریه» تیفوئید) 
MON_part1.txt:45662:تیفوس: :۱65 (.) (پز.) مرضی عفونی که 
MON_part1.txt:45664:ظاهری آن شبیه به تیفوئید (حصبه) است 
MON_part1.txt:45666:جلدی است آن را تیفوس پتشیال یا تیفوس 
MON_part1.txt:75288:امراض عفونی و حاد مانند تیفوئید و برخی 
MON_part1.txt:84199:و تیفوس و غیره می‌باشد. شپش انکل انسان 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:45662:تیفوس: :۱65 (.) (پز.) مرضی عفونی که 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:45664:ظاهری آن شبیه به تیفوئید (حصبه) است 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:45666:جلدی است آن را تیفوس پتشیال یا تیفوس 
=== MON طوفان ===
MON_part1.txt:770:جوشان و خروشان. اشاره به طوفان نوح. 
MON_part1.txt:45042:فارسی «طوفان» و به معنی شورش دریا 
MON_part1.txt:47232:توسط چنین سحری می‌توانند طوفان‌های 
MON_part1.txt:63023:و سرماء طوفان و باد. 
MON_part1.txt:93275:طوفان: «9: (.) باران سخت. آب سیار 
MON_part1.txt:93281:سیار که همه را فرا گیرد مانند طوفان آتش» 
MON_part2.txt:19884:نبا زکك» برف» طوفان» دنب السرحان» فلق» 
MON_part2.txt:23473:که در مواقم طوفان آب دریا که به کشتی 
MON_part2.txt:53769:ق ک3: مر ع طوفان: (جان.) برنده‌ای است 
MON_part2.txt:53775:اشت‌فاده کنتك: مرغ طوفان در سراسر
```


## [2026-09-05T20:08:08.918Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '45655,45672p' MON_part1.txt; echo \"-----طوفان-----\"; sed -n '93270,93290p' MON_part1.txt; echo \"---- 45035,45050 ----\"; sed -n '45035,45050p' MON_part1.txt"
}
```


### [2026-09-05T20:08:09.020Z] TOOL RESULT

```
و دارای لبه تبز بود. ساقه شمش کارد و 
غیر ۵. (ناء) دبوار یک لایی نازک به قطر 
یک آجر. بلندی کوه قله تیغ. 

تیف: ۱16 (.) خس و خار و خلاشه. 

تیفو ید: ۱1]074 (.) (پز.) حصبه. 
تیفوس: :۱65 (.) (پز.) مرضی عفونی که 
به وسیلةً شپش سرایت کند و چون علایم 
ظاهری آن شبیه به تیفوئید (حصبه) است 
بدین نام خوانده شده و چون دارای بئور 
جلدی است آن را تیفوس پتشیال یا تیفوس 
اکزانتماتیکک نامند. میکرب به وسیله نیش 
زدن شیش و ریختن مدفوع‌اش در محل 
گزیدگی يا خاراندن خود شخص وارد خون 
می‌شود و شخص سالم را مبتلا می‌کند و در 
صورتی که در معالجهٌ آن اهمال شود 
خطر ناک است) محر قه. 
-----طوفان-----
اطاعت. به طوع و رغبت: (ق.) به میل و 
ارادهٌ خو یش. 
طو ذ ف: (ند. ها ع. ۰] (مص‌ل.) دور 
چیزی گشتن» گرداگرد گردیدن. (امص.) 
طواف» گشت. 
طوفان: «9: (.) باران سخت. آب سیار 
که همه را بپوشد و غرق کند. (زه.) باد 
شدید و ناگهانی که موجب خسارت و 
خرایی ابنیه و ساختمان‌ها شود و سب 
تشکیل امواج سهمگین و مسخرب گردد و 
خطر عظیمی جهت کشتی‌ها دارد. هر چیز 
سیار که همه را فرا گیرد مانند طوفان آتش» 
طو فان باد. 
طوق: (ند. 0۷۷« [ع.] (.) زیوری که 
گرد گردن برآرند؛ گردن‌بند. آنچه که گرد 
چیزی را فرا گیرد. خطی چون حلقه بررگرد 
گُردن کبوتر و مانند آن. طوق بهار: (کد.) 
قوس قزح» رنگین کمان. طوق عنبر: (کن.) 
نودمیدگی خط خوبان. طوق فرمان: (اض. 
تشبیهی) فرمانی که در حکم گردن‌بند بر 
گردن خدمتگزاران است. طوق ماه: هاله 
---- 45035,45050 ----


کاهگل و گچ مالند. 

توفان: ۱62 (ص‌فا. توفیدن) شور و غوغا 
کننده» فریاد کننده» غران. (.) (زم.) (فره.) 
طو فان. ضح.- در بعض فر هنگ ها «توفان» را 
فارسی «طوفان» و به معنی شورش دریا 
گرفته‌اند ولی اين دو کلمه با هم ربطی ندارد. 
توفی: 2۷2 [ع. ۰ (مسص‌ل.) درگذشتن» 
مردن. (مصم.) میرانیدن. 

توفیدن: ۱-0 (مص‌ل.) فرباد کردن» 
آواز و شور و غوغا, برآوردن. غربدن» 
عربده کردن. جنبش کردن» هزاهز. 
توفیر: (-.2۷۷]1۳)10۷) [ع.] ( مسصم.) زیاد
```


## [2026-09-05T20:08:19.233Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 130 -l 130 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg130 && ls -la pg130.png && convert pg130.png -crop 100%x50%+0+0 +repage -resize 1500x pg130_top.png && convert pg130.png -crop 100%x55%+0+900 +repage -resize 1500x pg130_bot.png && ls"
}
```


### [2026-09-05T20:08:22.109Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 74748 Sep  5 16:08 pg130.png
bqt_bot389.png
bqt_bot390.png
bqt_n389.jpg
bqt_n390.jpg
pg130_bot.png
pg130.png
pg130_top.png
pg136_300.png
pg136.png
```


## [2026-09-05T20:08:24.374Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg130_top.png"
}
```


### [2026-09-05T20:08:24.396Z] TOOL RESULT

```

```


## [2026-09-05T20:08:34.440Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg130_bot.png"
}
```


### [2026-09-05T20:08:34.456Z] TOOL RESULT

```

```


## [2026-09-05T20:08:43.806Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD dud ===\" && grep -n \"dūd\\|dud \\[\\|dwd\\|dūdag\\|dwtk\" PHD_mackenzie.txt | head -10; echo \"=== NYB dut ===\"; grep -n \"dūt\\|dut \\[\\|dwt\\b\\|dūtak\" NYB_vol2_glossary.txt | head -10; echo \"=== HUB dud ===\"; grep -n \"579\\.\" HUB.txt | head -5"
}
```


### [2026-09-05T20:08:43.893Z] TOOL RESULT

```
=== PHD dud ===
2100:diid [dwt' I M dwd, N .....] smoke.
2101:diidal1 [dwtk I N .....a] family.
2103:dudil1ar [dtykll M dwdygr, N digar] second.
5285:wayOdagan [wydwtk)n I M ·wywdg)n, N ba)'ogan(i)] nuptials, marriage
=== NYB dut ===
1411:dit [dwt'] smoke 2029-24, — MPrth dwd (MHC); NP dud.
1650:gäviyöt [g'wydwt'] pasture 402°. — Bor- rowed from Av. (484) gaoyaoti-.
=== HUB dud ===
2234:579. Dazu auch np. d4ida ^Pamilie' Pird. I, 453, v. 334.
```


## [2026-09-05T20:08:51.802Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 dheu- ===\" && grep -n \"dh(e)u-\\|dheu-\\|dhū-mo\\|dhūmo\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -15; echo \"=== IEC dhumos ===\"; grep -n -i \"dhūmos\\|dhumos\\|dhū-mo\" IEC.txt | head -10; echo \"=== SYN smoke fumus ===\"; grep -n \"fumus\" SYN.txt | head -6; echo \"=== LEW fumus ===\"; grep -n \"fumus\" LEW_1910.txt | head -5"
}
```


### [2026-09-05T20:08:51.917Z] TOOL RESULT

```
=== WLD Bd1 dheu- ===
34852:Bed. Verh. wie gr. dvuog, fiviialrm: ai .dhunoti usw. (s. dheu- „stieben“) 
41836:bunden (s. *dhuen- unter dheu- „sterben“). 
44398:u. *dheu-dh- „stieben)“. Eine auch auBerhalb der idg. Sprachen verbreitete 
50215:dung von ai. dravati mit av. dvaraiti ,.geht ‘ s. unter *dheu-, *dheuer- „stieben‘\ 
52261:„sterblich"? (s. dheu- „hinschwinden“, wo auch iiber air. dtth, arm. di). Die 
52448:als „betaubt werden“ an anord. da „BewuBtlosigkeit“ usw. (s. idg. *dheu- 
52539:dheu- 
52566:1. dheu- „laufen, rinnen“. 
52588:Urspriingliche Gleichheit mit dheu- „stieben, heftige Bewegung" (z. B. 
52591:137), s. dheu- „blank“. 
52598:dheu dheu-, dheua x - 
52604:2. dheu- „hinschwinden, bewuBtlos werden, sterben“ (uber die kaum mit 
52605:Recht vermutete Yerwandtschaft mit dheu-, dhu-en- „stieben“ s. d.; 
52613:iiber andere Deutungen s. S. 841 *dheu-, dhu-en- ,.stieben ! ); kaum aber lat. 
52637:3. dheu- blank, glanzen". 
=== IEC dhumos ===
=== SYN smoke fumus ===
2102:THE PHYSICAL WORLD IN ITS LARGER ASPECTS 73 1.83 SMOKE (sb.) 5 Goth Lith. ditmat (pl.) Grk. alts ON reykr Lett. dimi (pl.) Ney eer Dan. 799 ChSI. dymé Lat.  fumus Sw. rok SCr. dim It. fi as OE réc, smoca Boh. dim Ti lp Medien ME __ reke, smoke Pol. dym ae Lah : NE smoke a am OD Ress Du. rook t. aima- Ir, CN OHG rouh Av. = Nir. mwg MHG rouch we moged NHG rauch
=== LEW fumus ===
```


## [2026-09-05T20:10:05.827Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"fumus\\|fümus\\|f umus\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo \"--- context of dheu stieben ---\"; grep -n \"stieben\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | sed -n '1,25p'"
}
```


### [2026-09-05T20:10:05.898Z] TOOL RESULT

```
54717:m vor i (gegeniiber fumus ) als mitbedingender TJmstand in Rechnung zu 
--- context of dheu stieben ---
21999:Hes., bom. y.ty.anpiy'na, Bezz. BB. 5, 313, Bechtel aaO., s. u. qevxp- „stieben“). 
23885:qeuep- (:quep-, quop-, qftp-), woneben vereinzeltes qcn(e)p-, q(e)uep- ..stieben, 
23948:lit. kupuoti „schwer atmen", lett. kupet „rauchen, dampfen, stieben", kupi- 
34852:Bed. Verh. wie gr. dvuog, fiviialrm: ai .dhunoti usw. (s. dheu- „stieben“) 
44398:u. *dheu-dh- „stieben)“. Eine auch auBerhalb der idg. Sprachen verbreitete 
48345:; .stieben“) nicht als ..dorniger, ritzender, reiBender Strauch“ benannt zu 
50215:dung von ai. dravati mit av. dvaraiti ,.geht ‘ s. unter *dheu-, *dheuer- „stieben‘\ 
51535:„stieben“) : dsog n. 
52195:beuegy • fie fiat a [oe/ur>], in welcher Bed. zu *dhem- „stieben“] evara&rjg lies, 
52588:Urspriingliche Gleichheit mit dheu- „stieben, heftige Bewegung" (z. B. 
52605:Recht vermutete Yerwandtschaft mit dheu-, dhu-en- „stieben“ s. d.; 
52613:iiber andere Deutungen s. S. 841 *dheu-, dhu-en- ,.stieben ! ); kaum aber lat. 
52648:„stieben, wirbeln, bes. von Staub, Rauch, Dampf; wehen, blasen, Hauch, 
52683:sondern nach van Wijk IF. 24, 34 als *staubma- zu ahd. stioban „stieben", 
52940:3. bh- Er\r. dlteubh- „stieben, raucben; nebelig, verdunkelt, auch vom 
53011:w-Erw. dhuen(&)- „stieben, heftig bewegt sein; wirbelnder Rauch, Nebel, 
53042:falls eine alte Sonderanwendung von dlieu- „zerstieben, wirbeln“ darstelle 
53093:„stieben, wirbeln" zu deuten, s. unter dheues-). — Als Gutturalerw. be- 
53149:dheues-, dhues-, dheus-, dhus- „stieben, stiiuben, wirbeln (nebeln, regnen, 
53154:dieses nicht in verschiedenen Wzln. („spirare, stieben usw.; furere“) 
53176:krause Spitzen ££ kaum als *dhvensrici „zerstiebendes“ hierher (s. Yf. LEWb. 2 
53284:ostfries. dose „Moosschicht auf den Torfmooren" („zerstiebend, verwirrt"?? 
53318:Mit der Bed. „stieben, Staubregen u. dgl." : norw. duskregn „Staubregen“, 
53402:„wohin reichen", auch u. *dhu~, *dhu-k- „stieben“. 
53416:„stieben“). Got. diups, aisl. diupr, ags. deop, as. diop, ahd. tiof „tief“;
```


## [2026-09-05T20:10:09.169Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '52645,52680p;52940,52975p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-05T20:10:09.219Z] TOOL RESULT

```
deog „Gott“ ist unsicher, s. *dhes- „religios“. 

dheu-, dhena- x (vermutlich *dheue-, vgl. die Erw. *dheue-h-, *dheue-s-) 
„stieben, wirbeln, bes. von Staub, Rauch, Dampf; wehen, blasen, Hauch, 
Atem; daher dampfen, ausdiinsten, riechen, stinken; stiirmen, in hef- 
tiger, wallender Bewegung sein, auch seelisch; in heftige, wirbelnde 
Bewegung versetzen, schiitteln". 

Mit m-Formantien : 

Ai. dhuma- m. „Rauch, Dampf", dhumayati „raucht, dampft" = lat. fil- 
mare, formell auch = ahd. tumon „sich im Kreise drehen"), gr. dvyog „Ge- 
miitswallung, Leidenschaft,Mut" (dvyiao) nocli rein sinnlich „rauche, riiuchere"; 
’&vjudXcoy’ „Kohlenmeiler", s. Aly Gl. 5, 60 f. ; fivy.iy.6g „leidenschaftlich“, 
Wald e , Etymologisches Worterbuch. I. 54 



836 


dheu- 


7?t jaaivco „ziirne“ usw.), lat. fiimus „Rauch, Dampf, Qualm, Brodem" ( fu - 
mare s. o.), lit. dumai pi. „Rauch“, lett. dumi pi., apr. dumis ds., aksl. dyim 
„Rauch“; mit u mir. dumacha „Nebel !i (nir. dumhach „nebelig, dunkel"; 
Stokes KZ. 41, 384); gr. 'dvg.og, -ov „Thymian“ (starkriechende Pflanze wie 
auch dv/ujUgov „Satureja thymbra L." Boisacq m. Lit.), vielleicht 

= lat. fimus ,,Mist, D linger" (wenn i iiber ii aus u infolge der beider- 
seitigen labialen Umgebung; nicht als *dhu-i-mos von einer nicht ander- 
weit beglaubigten Wzf. *dhu-ei- naeh Persson Wzerw. 114 Anm. 6, auch 
kaum erst auf Grund von suffio, -ire erwachsen, nach Yf. LEWb. 2 s. v., 
wobei l zu erwarten ware, vgl. sufflmentum-, doch kann deren i die Laut- 
entwicklung yon *fiimus zu fimos unterstiitzt haben nach Osthoff MU. 4, 
3. bh- Er\r. dlteubh- „stieben, raucben; nebelig, verdunkelt, auch vom 
Geist und den Sinnen". 

Gr. x l 'cpco (dvipai, Tvgpfjvai) „Rauch, Dampf, Qualm machen; langsam ver- 
brennen, sengen; pass, rauchen, qualmen, glimmen", r vcpog n. „Rauch, 
Dampf, Qualm; Benebelung, Torheit, dummer Stolz", vvcpoio „mache Rauch 
oder Dampf; benebele die Sinne, mache tbricht, aufgeblasen", xervgp&adai 
„toricht, aufgeblasen, lioffartig sein", ivcfcbs, -d> oder -mvo? „Wirbelwind, 
Ungewitter", zvcpe.dcov, -ovos „verheerender Brand", TVfpsdavog, zvcpoyegcov 
„geistesschwacher Alter"; tv go log „blind, dunkel, blode", zvcploco „blende“, 
Tvgplcbyj „blind“, xvcplcbooo o „werde blind": 

Air. dub (*dhubu-) „schwarz", acymr. dub { *dheab- ), ncymr. du, acorn, duw , 
mcorn. du, bret. da „schwarz“, gall. Dubis „Le Doubs", d. i. „Schwarzwasser“, 
wohl nach Schulze SBprAk. 1910, 797 auch mir. dobur „Wasser“, cymr .dwfr, 
corn, dour (d. i. dowr ), bret. dour (d. i. dur) ds., gall. Uertio-dubrum FluB- 
name f„Erlenwasser“) nach derselben Anschauung benannt sind (nicht besser 
zu aksl. dt>bn „Tal“, lit. duburfys „Grube, Loch", Wz. *dheub- „tief", Lit. bei 
Berneker 242 f. Der dort erwahnfce poln. FluBname Dbra, lieute Brda = 

, Brahe" ist wohl zu den kelt. Worten fur Wasser zu stellen). 

Got. dnufs (- b -) „taub, verstockt", anord. daufr „taub, trage", ags. deaf 
„taub“, ahd. toup (- b -) „taub, stumpfsinnig, unsinnig" (anord. deyfa, mhd. 
touben „betauben, kraftlos machen", ablautend nd. duff „schwiil (Luft), 
matt (Farbe 1 , gedampft (Laut)", ndl. dof , mhd. top „unsinnig, toricht, yer- 
riickt", as. dovon „wahnsinnig sein", ags. dofian „rasen“, ahd. toben, -on, 
nhd. toben, sowie (als Ptc. eines st. Y.) anord. dofinn „stumpf, schlaff, halb- 
tot", wozu dofna „schlaff, schal werden" (ygl. auch norw. mdartl. dova, dan. 
dfimcelde, dt. Taub-nessel); anord. dupt n. „Staub“, norw. duff, dyft f. ds.. 
mhd. tuft, duft „Dunst, Yebel, Tau, Reif", abd. tuft „Frost“, nhd. Duft 
„feiner Geruch" (oder zur Wzf. dheup-, s. u.); 

got. ( hranva-)dubo , anord. dufa, ags. dufe, ahd. tuba „Taube“ (nach der 
dunkeln Farbe, Parallelen z. B. bei Boisacq 994; andere Deutungen er- 
wahnt Falk-Torp u. due). Nasaliert got. dumbs , anord. dumbr, ags. dumb
```


## [2026-09-05T20:10:18.435Z] TOOL CALL #42: Bash

```json
{
 "command": "head -40 tools/fetch_source.py"
}
```


### [2026-09-05T20:10:18.486Z] TOOL RESULT

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


## [2026-09-05T20:10:24.821Z] TOOL CALL #43: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D9%88%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D8%B7%D9%88%D9%81%D8%A7%D9%86\" \\\n \"https://www.etymonline.com/word/typhoon\" \\\n \"https://www.etymonline.com/word/typhus\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0uh%E2%82%82m%C3%B3s\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 130, root Dheu 2 / Dhu-bh: dud, andoh, tufan, typhoon, typhus, fumus\" ; done"
}
```


### [2026-09-05T20:10:29.663Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/822073e4c0d7b52a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1e3eb396112c7ab3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8b9f00c69e8818ea.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d3da6fc08a71b840.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1880294b29336cff.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fa2aa8f0abd2cb0f.txt
```


## [2026-09-05T20:10:32.435Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 822073e4c0d7b52a 1e3eb396112c7ab3 8b9f00c69e8818ea; do echo \"##### $f\"; grep -n -i -A12 \"Etymology\" $f.txt | head -60; done"
}
```


### [2026-09-05T20:10:34.275Z] TOOL RESULT

```
##### 822073e4c0d7b52a
73: Etymology 
74-
75- 2.2 
76- Noun 
77-
78- 3 
79- Brokskat 
80-
81- Toggle Brokskat subsection 
82-
83- 3.1 
84- Noun 
85-
--
95: Etymology 1 
96-
97- 4.2.1 
98- Noun 
99-
100- 4.3 
101: Etymology 2 
102-
103- 4.3.1 
104- Noun 
105-
106- 4.4 
107- References 
108-
109- 5 
110- Hijazi Arabic 
111-
112- Toggle Hijazi Arabic subsection 
113-
--
115: Etymology 
116-
117- 5.2 
118- Pronunciation 
119-
120- 5.3 
121- Noun 
122-
123- 6 
124- Kashmiri 
125-
126- Toggle Kashmiri subsection 
127-
--
129: Etymology 
130-
131- 6.2 
132- Pronunciation 
133-
134- 6.3 
135- Noun 
136-
137- 7 
138- Pashto 
139-
140- Toggle Pashto subsection 
##### 1e3eb396112c7ab3
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Derived terms 
72-
73- 1.3.2 
74- Descendants 
--
146: Etymology
147- [ edit ] 
148-
149- Inherited from Middle Persian [script needed] ( ’ndwh /⁠andōh⁠/ , “ sorrow ” ) . Noun form of the verb اندوهیدن . 
150-
151- Pronunciation
152- [ edit ] 
153-
154- ( Classical Persian ) IPA ( key ) : /ʔan.ˈdoːh/ 
155-
156- ( Dari, formal ) IPA ( key ) : [ʔän̪.d̪oːʱ] 
157-
158- ( Dari, formal ) IPA ( key ) : [ʔän̪.d̪oːʱ] 
##### 8b9f00c69e8818ea
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Declension 
72-
73- 1.3.2 
74- Descendants 
--
96: Etymology 
97-
98- 3.3 
99- Pronunciation 
100-
101- 3.4 
102- Noun 
103-
104- 3.4.1 
105- Descendants 
106-
107- 3.4.2 
108- See also 
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
128- Declension 
129-
130- 5 
131- Urdu 
--
139: Etymology 
140-
141- 5.3 
142- Pronunciation 
143-
144- 5.4 
145- Noun 
146-
147- 5.4.1 
148- Declension 
149-
150- Toggle the table of contents 
151-
--
236: Etymology
237- [ edit ] 
238-
239- Through Aramaic ܛܘܦܢܐ / טוֹפָנָא ( ṭōpānā ) ( Classical Syriac ܛܲܘܦܵܢܵܐ ( ṭawpānā ) ), probably from a Sinitic language, though it has also been suggested that the term could be natively Semitic: see typhoon for more. Compare Cantonese 大風  / 大风 ( daai 6 fung 1 , “ big wind ” ) and Ancient Greek τυφῶν ( tuphôn ) .
```


## [2026-09-05T20:10:41.671Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '/^ *Persian *$/,+60p' 822073e4c0d7b52a.txt | grep -n -i -B2 -A8 \"Middle Persian\\|Proto-Iranian\" | head -40; echo \"===TYPHOON etymonline===\"; sed -n '1,80p' d3da6fc08a71b840.txt | grep -n -i -A6 \"typhoon\" | head -40"
}
```


### [2026-09-05T20:10:43.551Z] TOOL RESULT

```
76- [ edit ] 
77-
78: From Proto-Iranian *duHmáh , from Proto-Indo-Iranian *dʰuHmás , from Proto-Indo-European *dʰuh₂mós . Compare Northern Kurdish dû and Lurish دی ( di , “ smoke ” ) . (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium . Particularly: “Did Proto-Iranian *Hm become /d/? And if not, where does the /d/ come from?”) 
79-
80- Pronunciation
81- [ edit ] 
82-
83- ( Classical Persian ) IPA ( key ) : /ˈduːd/ 
84-
85- ( Dari, formal ) IPA ( key ) : [d̪uːd̪] 
86-
===TYPHOON etymonline===
1:URL: https://www.etymonline.com/word/typhoon
2-FETCHED: 2026-09-05T20:10:28Z
3-STATUS: 200
4:TITLE: Typhoon - Etymology, Origin & Meaning
5-
6:Typhoon - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
--
21: Origin and history of typhoon 
22-
23: typhoon (n.) 
24-
25- Tiphon "violent storm, whirlwind, tornado," 1550s, from Greek typh ō n "whirlwind," personified as a giant, father of the winds, a name probably [Beekes] from or related to typhein "to smoke" (see typhus ). According to Watkins from PIE *dheub- "deep, hollow," via notion of "monster from the depths." The god-name is in Middle English in Wycliffe's wynd Tiffonyk (c. 1384, via Latin typhonicus ).
26-
27- The meaning "cyclone, violent hurricane of India or the China Seas" is attested by 1588 in Thomas Hickock's translation of an account in Italian of a voyage to the East Indies by Caesar Frederick, a merchant of Venice:
28-
29- concerning which Touffon ye are to vnderstand, that in the East Indies often times, there are not stormes as in other countreys; but euery 10. or 12. yeeres there are such tempests and stormes, that it is a thing incredible, but to those that haue seene it, neither do they know certainly what yeere they wil come. ["The voyage and trauell of M. Caesar Fredericke, Marchant of Venice, into the East India, and beyond the Indies"] 
--
38: Entries linking to typhoon 
39-
40- typhus (n.) 
41-
42- acute infectious fever, usually accompanied by severe prostration, delirium, and small reddish spots, 1785, from medical Latin, from Greek typhos "stupor caused by fever," literally "smoke," from typhein "to smoke," related to typhos "blind," typhon "whirlwind." Beekes rejects the derivation suggested in Watkins that these are from a PIE root *dheu- (1) "dust, vapor, smoke."
43-
44- The Greek term [typhos] 
--
52: giant in Greek mythology, Latin Typhon , from Greek Typhōs (see typhoon ), Father of the Winds. The word was sometimes used in 16c. English for "a whirlwind."
53-
54- *dheu- (1) 
55-
56- Proto-Indo-European root meaning "dust, vapor, smoke." 
57-
58: It might form all or part of: enthymeme ; fewmet ; fume ; fumigation ; funk ; perfume ; sfumato ; typhoid ; typhoon ; typhus .
59-
60- It might also be the source of: Sanskrit dhuma- "smoke, fume;" Greek thymos "spirit, courage, anger," thymiao "fumigate," thymin "incense;" Latin fumus "smoke, steam, fume;" Lithuanian dūmai "smoke" (plural); Old Prussian dumis "smoke;" Old Church Slavonic dymu "smoke;" Middle Irish dumacha "fog;" perhaps Old High German toum "steam, vapor."
```


## [2026-09-05T20:10:47.834Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '28,40p' d3da6fc08a71b840.txt"
}
```


### [2026-09-05T20:10:47.877Z] TOOL RESULT

```
 concerning which Touffon ye are to vnderstand, that in the East Indies often times, there are not stormes as in other countreys; but euery 10. or 12. yeeres there are such tempests and stormes, that it is a thing incredible, but to those that haue seene it, neither do they know certainly what yeere they wil come. ["The voyage and trauell of M. Caesar Fredericke, Marchant of Venice, into the East India, and beyond the Indies"] 

 This sense of the word, in reference to titanic storms in the East Indies, is found in Europe first in Portuguese in the mid-16th century. It apparently is from tufan , a word in Arabic, Persian, and Hindi meaning "big cyclonic storm." Yule ["Hobson-Jobson," London, 1903] writes that "the probability is that Vasco [da Gama] and his followers got the tufao ... direct from the Arab pilots."

 The Arabic word sometimes is said to be from Greek typhon , but other sources consider it purely Semitic, though the Greek word might have influenced the form of the word in English. Al-tufan occurs several times in the Koran for "a flood or storm" and also for Noah's Flood. Chinese (Cantonese) tai fung "a great wind" also might have influenced the form or sense of the word in English, and that term and the Indian one may have had some mutual influence; toofan still means "big storm" in India.

 From the thighs downward he was nothing but coiled serpents, and his arms which, when he spread them out, reached a hundred leagues in either direction, had countless serpents' heads instead of hands. His brutish ass-head touched the stars, his vast wings darkened the sun, fire flashed from his eyes, and flaming rocks hurtled from his mouth. [Robert Graves, "Typhon," in "The Greek Myths"] 
 also from 1550s 

 Entries linking to typhoon 

 typhus (n.)
```


## [2026-09-05T20:11:00.439Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HJB typhoon ===\" && grep -n -i \"TYPHOON\" HJB.txt | head -5 && python3 -c \"\nt=open('HJB.txt',encoding='utf-8',errors='replace').read()\ni=t.upper().find('TYPHOON, S.')\nif i<0: i=t.upper().find('TYPHOON')\nprint(t[i:i+1500])\n\" ; echo \"=== KLN page marker near typhus ===\" && python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find('typhus,  n.  —  Medical  L.')\nprint('leaf',t[:i].count('\\f'))\nimport re\nseg=t[max(0,i-6000):i+2000]\nprint([m for m in re.findall(r'\\n\\s*(1[0-9]{3})\\s*\\n',seg)])\n\""
}
```


### [2026-09-05T20:11:02.542Z] TOOL RESULT

```
=== HJB typhoon ===
132:Of  words  that  seem  to  have  been  admitted  to  full  franchise,  we  may  give examples  in  curry^  toddy^  veranda,  cheroot,  loot,  nahob,  teapoy,  sepoy,  cowry ;  and of  others  familiar  enough  to  the  English  ear,  though  hardly  yet  received into  citizenship,  compound,  batta,  pucka,  chowry,  baboo,  mahout,  aya,  nauU^,* first-chop,  competition-toa/^,  griffin,  &c.  But  beyond  these  two  classes  of words,  received  within  the  last  century  or  so,  and  gradually,  into  half  or whole  recognition,  there  are  a  good  many  others,  long  since  fully  assimilated, which  really  originated  in  the  adoption  of  an  Indian  word,  or  the  modifica- tion of  an  Indian  proper  name.  Such  words  are  the  three  quoted  at  the beginning  of  these  remarks,  chintz,  calico,  gingham,  also  shawl,  bamboo,  pagoda^ typhoon,  m/msoon,  mandarin,  palanquin,f  &c.,  and  I  may  mention  among further  examples  which  may  perhaps  surprise  my  readers,  the  names  of  three of  the  boats  of  a  man-of-war,  viz.  the  cutter,  the  jolly-boat,  and  the  dijigy,  as all  (probably)  of  Indian  origin.!  Even  phrases  of  a  different  character — slang  indeed,  but  slang  generally  supposed  to  be  vernacular  as  well  as  vulgar — e.g,  'that  is  the  cheese* ;%  or  supposed  to  be  vernacular  and  profane — e,g, *I  don't  care  a  dam^X — are  in  reality,  however  vulgar  they  may  be,  neither vernacular  nor  profane,  but  phrases  turning  upon  innocent  Hindustani vocables.
162:onr  Anglo-Indian  coUoquiaUsmS)  even  if  eventually  traceable  to  native sources  (and  especially  to  Mahratti,  or  Dravidian  originals)  have  come  to us  throngb  a  Portuguese  medium,  and  often  bear  traces  of  having  passed through  that  alembic.  Not  a  few  of  these  are  familiar  all  over  India,  but the  number  current  in  the  South  is  larger  still.  Some  other  Portuguese woids  also,  though  they  can  hardly  be  said  to  be  recognized  elements  in  the Anglo-Indian  colloquial,  have  been  introduced  either  into  Hindustani generally,  or  into  that  shade  of  it  which  is  in  use  among  natives  in  habitual contact  with  Europeans.  Of  words  which  are  essentially  Portuguese,  among Anglo-Indian  colloquialisms,  persistent  or  obsolete,  we  may  quote  goglet, framy  plantain,  muster^  caste,  peon,  padre,  midry  or  maistry,  almyra,  aya,  cohray masqutlo,  pom/ret,  cartuez,  palmyra,  still  in  general  use ;  picoUa,  rolong,  pial, fogass,  margosa,  preserved  in  the  South  ;  hotel,  brab,  foras,  oart,  veUard  in Bombay  ;  joss,  compradore,  linguist  in  the  ports  of  China  ;  and  among  more or  less  obsolete  terms,  Moor,  for  a  Mahommedan,  still  surviving  under  the modified  form  Moorman,  in  Madras  and  Ceylon  ;  Gentoo,  still  partially  kept up,  I  believe,  at  Madras  in  application  to  the  Telugu  language,  mustees,  castees, bandeja  (*  a  tray '),  Kittysol  (*  an  umbrella,*  and  this  survived  ten  years  ago  in the  Calcutta  customs  tariff),  cuspadore  (^  a  spittoon '),  and  covid  ('  a  cubit  or ell*).  Words  of  native  origin  which  bear  the  mark  of  having  come  to  us through  the  Portuguese  may  be  illustrated  by  such  as  palanquin,  mandarin, nangelin  (a  small  weight  for  pearls,  &c.)  m^onsoon,  typhoon,  mango,  mangosteen^ jack-fruit,  batta,  curry,  chop,  congee,  coir,  cutch,  catamaran,  cassanar,  nabobs avadavat,  betel,  areca,  benzoin,  corge,  copra.*  A  few  examples  of  Hindustani words  borrowed  from  the  Portuguese  are  chdbl  (*a  key'),  bdola  (*a  port- manteau'),  6aft«  (*  a  bucket'),  martol  (*a  hammer*),  tauliya  (*a  towel,' Port. toalha),  sdbun  (*soap'),  bdsan  (* plate'  from  Port,  bctcia),  llldm  and  nlldm  (*an auction'),  besides  a  number  of  terms  used  by  Lascars  on  board  ship.
176:other  products  which  have  been  imported,  such  as  loquotf  leechee,  choto-chow^ cumquat^  gtrueng,  &c.  and  (recently)  jinncfaAaw.  For  it  must  be  noted  that a  considerable  proportion  of  words  much  used  in  Chinese  ports,  and  often ascribed  to  a  Chinese  origin,  such  as  mandarinj  junky  chop,  pagoda,  and  (as  I believe)  typhoon  (though  this  is  a  word  much  debated)  are  not  Chinese  at  all, but  words  of  Indian  languages,  or  of  Malay,  which  have  been  precipitated  in Chinese  waters  during  the  flux  and  reflux  of  foreign  trade.
8619:DEVIL,  s.  A  petty  whirlwind,  or circular  storm,  is  often  so  called.  (See PI8ACHEE,  8HAITAN»  TYPHOON.)
15714:NOB'-WESTEB,  s.  A  sudden  and violent  Btorm,  such  as  often  occurs  in the  hot  weatiier,  bringing  probably  a '  dust-storm '  at  first,  and  culminating in  hail  or  torrents  of  rain.  (See TYPHOON.)
typhoon,  m/msoon,  mandarin,  palanquin,f  &c.,  and  I  may  mention  among further  examples  which  may  perhaps  surprise  my  readers,  the  names  of  three of  the  boats  of  a  man-of-war,  viz.  the  cutter,  the  jolly-boat,  and  the  dijigy,  as all  (probably)  of  Indian  origin.!  Even  phrases  of  a  different  character — slang  indeed,  but  slang  generally  supposed  to  be  vernacular  as  well  as  vulgar — e.g,  'that  is  the  cheese* ;%  or  supposed  to  be  vernacular  and  profane — e,g, *I  don't  care  a  dam^X — are  in  reality,  however  vulgar  they  may  be,  neither vernacular  nor  profane,  but  phrases  turning  upon  innocent  Hindustani vocables.
We  proposed  also,  in  our  Glossary,  to  deal  with  a  selection  of  those administrative  terms,  which  are  in  such  familiar  and  quotidian  use  as  to form  part  of  the  common  Anglo-Indian  stock,  and  to  trace  all  (so  far  as XX)6sible)  to  their  true  origin — a  matter  on  which,  in  regard  to  many  of  the words,  those  who  hourly  use  them  are  profoundly  ignorant— and  to  follow them  down  by  quotation  from  their  earliest  occurrence  in  literature.
A  particular  class  of  words  are  those  indigenous  terms  which  have  been adopted  in  scientific  nomenclature,  botanical  and  zoological.  On  these  Mr. Bumell  remarks : —
"The  first  Indian  botanical  names  were  chiefly  introduced  by  Garcia de  Orta  {CoUoguios,  printed  at  G
=== KLN page marker near typhus ===
leaf 885
[]
```


## [2026-09-05T20:11:47.106Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"tufan\\|tufao\\|Touffon\\|tay-fung\\|ta-fung\" HJB.txt | head -8"
}
```


### [2026-09-05T20:11:47.159Z] TOOL RESULT

```
22653:TYPHOON,  s.  A  tornado  or cyclone- wind  ;  a  sudden  storm,  a  *  nor- Wester*  (qv.).  Sir  John  Barrow  (see Autobiog.  57)  ridicules  "learned  anti- quarians "  for  fancying  that  the  Chinese took  typhoon  from  the  Egyptian  Tyyhon, the  word  being,  according  to  him, simply  the  Chinese  syllables,  ta-fung, •Great  Wind.'  His  ridicule  is  mis- placed. With  a  monosyllabic  lan- guage like  the  Chinese  (as  w^e  have remarked  elsewhere)  you  may  construct a  plausible  etymology,  to  meet  the requirements  of  the  sound  alone,  from anything  and  for  anything.  And  as there  is  no  evidence  that  tne  word  is in  Chinese  use  at  all,  it  would  ])erhaps be  as  fair  a  suggestion  to  derive  it  from the  English  'Hough  'un,*'  Mr.  Giles, who  seems  to  think  that  the  balance  of evidence  is  in  favour  of  this  (Barrow's) etymology,  admits  a  serious  objection to  be  that  the  Chinese  have  special names  for  the  typhoon,  and  rarely,  if ever,*  speak  of  it  vaguely  as  a  *  great wind.*  The  fact  is  that  very  few  words of  the  class  used  by  seafaring  and trading  people,  even  when  they  refer to  Chinese  objects,  are  directly  taken from  the  Chinese  language.  E.g.  Man- darin,  pagoda,  chop,  cooly,  tviena^ue; — none  of  these  are  Chinese.  And  the probability  is  that  Vasco  and  his loUowers  jgot  the  txifao,  which  our sailors  made  into  touff&n  and  then  into
22656:Dr.  F.  Hirth,  again  (Journ.  R.  Oeog. Soc.  i.  260),  advocates  the  quasi-Chinese origin  of  the  word.  Dr.  Hirth  has found  the  word  Tai  (and  also  with  the addition  of  fiing,  '  wind ')  to  be  really applied  to  a  certain  class  of  cyclonic winds,  in  a  Chinese  work  on  Formosa, which  is  a  re-issue  of  a  book  originally published  in  1694.  Dr.  Hirth  thinks fai  as  here  used  (which  is  not  the Chinese  word  ta  or  tai,  'great,'  and  is expressed  by  a  different  character)  to be  a  local  Formosan  term  ;  and  is  of opinion  that  the  combination  Vai-fung is  *'  a  sound  so  near  that  of  typhoon  as almost  to  exclude  all  other  conjectures, if  we  consider  that  the  writers  using the  term  in  European  languages  were travellers  distinctly  applying  it  to storms  encountered  in  tnat  part  of  the China  Sea."  Dr.  Hirth  also  refers  to F.  Mendes  Pinto  and  the  passages (quoted  below)  in  which  he  says  tufao is  the  Chinese  name  for  such  storms. Dr.  Hirth's  paper  is  certainly  worthy of    much    more   attention    than   the
22666:"The  question  of  the  origin  of  Tufan appears  to  be  somewhat  tangled.
22669:**  But  again,  the  sense  of  wkirlweind  is  Dot recognised  in  classical  Arabic.  Even  Doaj in  his  dictionary  of  later  Arabic  only  cites  a modem  French- Arabic  dictionary  (Boctbor's) for  the  sense,  Tottrbillon,  trombe.  Bist^i  in the  Mohii  d  MohU  does  not  giye  this  sense, though  he  is  pretty  full  in  giving  modem  as well  as  old  words  and  senses.  In  Arabic  the root  ^tff  means  '  to  go  round,'  and  a  combina- tion of  this  idea  with  the  sense  of  sadden disaster  might  conceivably  hare  given  the new  meaning  to  the  word.  On  the  other hand  it  seems  simpler  to  regard  this  sense as  a  late  loan  from  some  modem  form  of Tvtpiinfy  typhOf  or  t^oiu.  But  in  order  finally to  settle  the  matter  one  wants  examples  ot this  sense  of  tUfAn,"
22679:1567. — *^I  went  aboorde  a  shippe  of  Ben- gala,  at  which  time  it  was  the  yeere  of Touffon,  concerning  which  Tonifon  ye  are to  vnderstand  that  in  the  East  Indies  often times,  there  are  not  stormes  as  in  other countrevs  ;  but  every  10  or  12  yeeres  there are  such  tempests  and  stormes  that  it  is  a thinfi;  incredible . . .  neither  do  they  know  cer- tainly what  yeere  they  will  come." — Master Caemr  tVederike,  in  Hakl.  ii.  370  [369].
22680:1575. — "  But  when  we  approach'd  unto  it (Cyprus),  a  Hurricane  arose  suddenly,  and blew  so  fiercely  upon  us,  that  it  wound  our great  Sail  roimd  about  our  main  Most.  .  .  . These  Winds  arise  from  a  Wind  that  is called  by  the  Greeks  Typhon ;  and  Pliny calleth  it  Vertex  and'  Vortex  ;  but  as  danger- ous as  they  are,  as  they  arise  suddenly,  so quickly  are  they  laid  again  also." — Rauwolff's Traveh,  in  Ray't  CoUeclion,  ed.  1705,  p.  320. Here  the  traveller  seems  to  intimate  (though we  are  not  certain)  that  Typhxtn  was  then applied  in  the  Levant  to  such  winds  ;  in  any case  it  was  exactly  the  tufan  of  India.
```


## [2026-09-05T20:11:58.101Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index DUD ===\" && grep -n -E \"^ *DUD|DUD |dhumo|DHEU\" incoming/ARY/ARY_latin_index_pages.txt | head -10; echo \"=== ARY pages دود ===\"; grep -n \"دودمان\\|دوده\" incoming/ARY/ARY_pages.txt | head -6; echo \"=== IEC dhumo ===\"; grep -n -i \"dhūmos\\|dhumo-\\|dhūmo\" IEC.txt | head -6; echo \"=== IEC dheubh ===\"; grep -n -i \"dheubh\\|dhubh\" IEC.txt | head -6"
}
```


### [2026-09-05T20:11:58.220Z] TOOL RESULT

```
=== ARY latin index DUD ===
8380:MALLORY & ADAMS: DHEU TOU .
=== ARY pages دود ===
=== IEC dhumo ===
=== IEC dheubh ===
3201:dhrsus, os, is — dhubhlos
3212:dhubh- (1) ‘strike’ (variant: dhubhs-). Cf. deps- OE dubbian; Sw. dubba, id.; MHG cf. tüf- teln, id.; OCz. (variant) debs ‘din’; debšu, debsati ‘make a din’. (OE & Sw. also = ‘to dub’)
3213:dhubh- (2) ‘weak, flat, silly, soft, mad, limp, insipid; weakness’, etc. Gk. túphos ‘stupefac- tion’; tetúphomai ‘dote’; MHG top, gs tobes ‘stupid, mad’; G toben ‘to rage’; Du. dof ‘dull, matt: OFris. dof ‘weak’; OE dobian, dofian, v. ‘dote’; dofung ‘stupidity’; ON dofi ‘numbness’; dofinn ‘numb’; Norw. doven ‘lazy’; Sw. duven “flat, insipid’; dufna ‘grow insipid'. Cf. G tüfteln, LG difteln ‘fuss’
3214:dhubh- (?) (3) (dhubha-?) ‘heed’. Cf. tubhālo- (tubhá-) Hom. a-súphelos ('contemptuous' is ambig.); OE dybbian ‘pay heed'; Cz. dbát, Pol. dbać, id. (but OCz. tbáti points to tubhå-, q.v.)
3217:dhubhlos, is (dhubhol-) “depression, hollow’. Cf. dhubo, dhübhó
3220:dhubhlos (2) & dhubhros ‘dark, deep, dirty, stagnant'. Cf. dhubros, dhübh- Gk. tuphlós ‘blind’; Ir. (variant) dobhair “dark, foul’; Icel. cf. dufl ((2) ‘frivolity; gambling;
```


## [2026-09-05T20:12:03.942Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"dhūmos\\|dhumos\\|dhūmo\\|dhumo\" IEC.txt | head -8; grep -n \"‘smoke’\" IEC.txt | grep -i \"fumus\\|dhum\" | head -5"
}
```


### [2026-09-05T20:12:04.011Z] TOOL RESULT

```
3295:dhumo ‘breathe, smoke”, etc. see dham- (1) and cf. dhümos and derivs. For a type *-dhum- no-, cf. Sequanian duman ‘overcast’. Cf. dhunmn-
```


## [2026-09-05T20:12:42.798Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dhümos\\|dhūmos\" IEC.txt | head -5; sed -n '3296,3310p' IEC.txt"
}
```


### [2026-09-05T20:12:42.871Z] TOOL RESULT

```
3273:dhūmāið, eið (ið) ‘steam, smoke, breathe, blow’. WP I, 835. See dhümos Skt. dhüumáyami, tr. ‘cloud over; Gk. cf. thumiáo Cemoulder", ambig. cf. dhusmo-); Lat. fümo, are ‘smoke, foam’; OHG *a-tumon (spelt àdhmon: “blow, breathe. See FK: atmen); OCz. dýmu, ati (and dymaju), v. “blow, sigh, swell’; Cz. dymám “smoke”, intr.; OCS dymiti se, intr. id. (: Skt. dhümye, mp. id.; Li. dümiju, yti, id.)
3287:dhümoka 'smoke, billow, cloud, puff. Cf. dhümos, etc.
3291:dun’. Cf. dhümos, etc.
3295:dhumo ‘breathe, smoke”, etc. see dham- (1) and cf. dhümos and derivs. For a type *-dhum- no-, cf. Sequanian duman ‘overcast’. Cf. dhunmn-
3296:dhümos “smoke, vapour, fog, spirit, breath. WP I, 835. Cf. dhusmos Skt. dhümáh also npl. dhümáàh: ‘smoke, vapour; Gk. (ambig.) thümós (/vapour, breath, spirit”, cf. dhusmos); Lat. fümus; OCS dymü; Li. dúmas & (pl.) dümai. See next
dhümos “smoke, vapour, fog, spirit, breath. WP I, 835. Cf. dhusmos Skt. dhümáh also npl. dhümáàh: ‘smoke, vapour; Gk. (ambig.) thümós (/vapour, breath, spirit”, cf. dhusmos); Lat. fümus; OCS dymü; Li. dúmas & (pl.) dümai. See next
dhumsos, om, à (dhusmos) ‘swell, vapour, enthusiasm, animus'. Cf. dhunmn-, dhüs-. (Some of the evidence is ambig.). See dhü- mos above Arm. dum, gs dmo “cold, catarrh, influenza”; Gk. cf. thüma ‘incense; sacrifice’ (ambig. also thumós ‘vapour, breath"); Ir. cf. dámas (fr. *dhümestis) ‘pretence’; Du. dons, EMDu. dons, EMDu. donst "down (uff: OHG cf. dunist ‘vapour’; G (fr. LG) Dunst, id.; Pol. dasy, pl. ‘sulks’; Latv. cf. dusmas, pl. “anger”; G (fr. LG) cf. dunsen, v. *puff up'
dhumtos '(biown-up, vaporized'", etc. See dhüm-, dham- Oss. dunt, pp. ‘blown’; Pol. det id.; Cz. dut, id.; Li. dümtas, id. Cf. Ir. donn “pregnant?
dhundó, ið “bang, beat, thud’. Cf. dhundho Arm. cf. dndéem (‘bang’, fr. *dhundhitio); OE dynt ‘blow’; EME dint, id. & cf. to dunt “crack, of earthenware, when in firing-oven'; ON dyttr ‘diw’ beside dyntr ‘crash’; R cf. dut (2) ‘trash’; (for Li. dundeéti, Latv. dun-
221
det, see next)
dhundhó, ið “force, stir, move’. (There is some confusion w. dhundo, q.v.) Arm. cf. dndéem Chang" Cf. the two mnes. of E ‘bang (1) “hit”, 2) *explode'); Alb. dynd “force, expel, move, stir, shake, uproot’, fr. *dhundheio; ON dunn, s. ‘troop, drove, mass’; Li. dündu, éti ‘roar, rumble, shake, rattle, throb’; Latv. dundēt, inf. ‘rumble, hum’. (The Baltic forms are ambig. cf. dhund-). (Isophonic is Skt. dhundhukam, n. ‘defect in wood’; Hind. dundh, m. ‘dimness’; G Tunte ‘waverer; tuntig ‘wavering’; Icel. dunda ‘to dally’) |)
dhundhulos (dhundhilos) “sway, swing; pen- dulum’. Cf. dhundho Arm. dndey 'sway, rock, swing" (fr. *dhun- dhilo-); It. (fr. Gmc.) dóndolo ‘pendulum, bob, jest; G tunteln, tünteln ‘dally’; ON dyndill ‘bob, pendulum, tail, penis’. Radical in Icel. dund ‘dalliance’, dunda “to dally’; OCS doda "nod (Isophonic: Li. dundulis ‘rumble, roar’. See next)
dhundhur- (dhundhro-) ‘rumble, roar, hum, din’. Skt. dhundhurih (a musical instrument); Arm. drndem ‘stamp; toll’; dřndiwn ‘din’; Gk. tonthorúzo ‘rumble’; tonthrùs ‘din’; W dwndwr ‘din’; dwndro ‘rumble’; Sw. Norw. Dan. dunder, id.; dundra, dundre, v. id.; Li. dundurys “horsefly'; Latv. dundurs, id.; Li. dunduriuoti, v. ‘rumble, roar, buzz’; Latv. dundurot, id. :
dhung- ‘bulge, projection’ Gk. cf. stór-thugx, gs -thuggos “point of spear; headland”; Alb. dungë ‘bulge; pistol" beside i dunguem ‘bulging’; ON (?) dokka *wind- lass; Norw. dunk ‘can, jar, keg’; OCz. duha ‘bruise’; Pol. dega ‘callouse’
dhungo ‘bang, bump” Norw. Sw. dunke, dunka, id.; ON cf. dynkr, m. id.; Li. cf. duñgzti (sg dunzgu) beside dunksiü, éti, id.
dhunmn-, dhunno- (smoke-coloured, murky, dun, dim'. Cf. dhusmos. WP I, 846. (Some of the evidence is ambig.) Av. cf. dunman “cloud, vapour’; Gk. cf. thün- nos, thünné 'tunny'; Sequanian duman *over-
dhundho, io — dhures, is, uis, ó(n)
10
20
```


## [2026-09-05T20:12:47.418Z] TOOL CALL #52: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-05T20:12:47.469Z] TOOL RESULT

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


## [2026-09-05T20:15:06.584Z] TOOL CALL #53: Bash

```json
{
 "command": "head -5 /home/sfmqrb/git/rishe/data/verification/sources/web/fa2aa8f0abd2cb0f.txt; echo ---; head -5 /home/sfmqrb/git/rishe/data/verification/sources/web/1880294b29336cff.txt"
}
```


### [2026-09-05T20:15:06.632Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0uh%E2%82%82m%C3%B3s
FETCHED: 2026-09-05T20:10:29Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/dʰuh₂mós - Wiktionary, the free dictionary

---
URL: https://www.etymonline.com/word/typhus
FETCHED: 2026-09-05T20:10:29Z
STATUS: 200
TITLE: Typhus - Etymology, Origin & Meaning
```


## [2026-09-05T20:15:12.756Z] TOOL CALL #54: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.etymonline.com/word/fume\" --note \"page 130, node 16 fume/perfume < Lat fumus\" && python3 tools/fetch_source.py \"https://www.etymonline.com/word/*dheu-\" --note \"page 130, root Dheu 2: PIE *dheu- (1) dust, vapor, smoke\" && grep -c . data/verification/sources/web/*.txt >/dev/null; head -5 data/verification/sources/web/$(python3 -c \"\nimport hashlib;print(hashlib.sha1('https://www.etymonline.com/word/*dheu-'.encode()).hexdigest()[:16])\").txt"
}
```


### [2026-09-05T20:15:15.478Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5d70eca59bcaedd5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d35f76f237745bbe.txt
URL: https://www.etymonline.com/word/*dheu-
FETCHED: 2026-09-05T20:15:15Z
STATUS: 200
TITLE: *dheu- - Etymology and Meaning of the Root
```


## [2026-09-05T20:15:34.996Z] TOOL CALL #55: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK data/verification/sources/refs/ocr/BQT && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg130.png data/verification/sources/refs/ocr/BOOK/130.png && cat > data/verification/sources/refs/ocr/BQT/172.vision.txt <<'EOF'\n# Borhan-e Qate' (ed. Mo'in), printed p. 172 = archive.org borhan-ghate-v1 leaf n390.\n# Read from the page image (bottom footnote block); OCR of BQT_v1_pages.txt was unusable here.\n# Footnotes 6-9 of p. 172 (continuation of the footnotes begun on p. 171, \"بقیه در صفحهٔ ۱۷۲\"):\n\n۶ - پهلوی handûtan ، تاوادیا ۱۶۰ : ۲ ، اونوالا ۲۱۵ ، مرکب از: han-du اوستایی ،\nجزو اول هن (هم) و جزو دوم du ( مالیدن ، پاک کردن ) ، بارتولمه ۶۸۸ .\n۷ - رک: اندوختن.\n۸ - پهلوی handôh ، نیبرگ ۱۰۰. رک: اندوهگین.\nاندرون - بفتح اول و سوم ، پهلوی andarôn ، معین ۲۶۶ ، درون، داخل، باطن.\nاندرونی - بفتح اول و سوم ؛ منسوب باندرون . پهلوی andarônîk ، معین ۲۶۶ ، درونی؛ داخلی، باطنی .\nاندوهگین - بفتح اول ، پهلوی handôh(a)kên (غمناک، با اندوه، باغصه)، ارمنی andohakan\nمرکب از: an(a) پسوند + hadôhak ؛ handôh ( اندوه ) مرکب از han-davatha\nمشتق از dav ( فشار دادن ) . • بارتولمه ۶۸۸ ، نیبرگ ۱۰۰ .\n\n# Key point: the Avestan-looking form \"han-davatha\" that Nourai prints (as \"han-davathe\")\n# is Mo'in's own reconstruction in this footnote, not an attested Avestan word;\n# Mo'in refers it to Bartholomae col. 688 (dav- 'sich drängen') and Nyberg p. 100 (handōh).\nEOF\necho OK; ls -la data/verification/sources/refs/ocr/BOOK/130.png"
}
```


### [2026-09-05T20:15:36.624Z] TOOL RESULT

```
OK
-rw-rw-r-- 1 sfmqrb sfmqrb 74748 Sep  5 16:15 data/verification/sources/refs/ocr/BOOK/130.png
```


## [2026-09-05T20:22:57.754Z] TOOL CALL #56: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nS = {\n \"dud\": W+\"دود\",\n \"andoh\": W+\"اندوه\",\n \"tufan\": W+\"طوفان\",\n \"typhoon\": \"https://www.etymonline.com/word/typhoon\",\n \"typhus\": \"https://www.etymonline.com/word/typhus\",\n \"fume\": \"https://www.etymonline.com/word/fume\",\n \"dheu\": \"https://www.etymonline.com/word/*dheu-\",\n \"dhumos\": W+\"Reconstruction:Proto-Indo-European/dʰuh₂mós\",\n}\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"dvaidi 1\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The form dvaidī is genuine Avestan, but it is a finite verb, not a noun for 'smoke'. Bartholomae, AiW col. 688, lists it exactly once, as the 1st person dual middle of 5.dav- 'sich drängen, bedrängen' (Y 29.5 … dvaidī 'while we two press [Ahura] with entreaties'). Pokorny p. 262 quotes that same form — \\\"av. dvaidi 'wir beide bedrängen'? (*du-vaidī)\\\" — and immediately before it gives the Iranian word for 'smoke' as Middle Persian: \\\"mpers. dūt 'Rauch'\\\". Nourai has split the single Avestan form into two homonyms (his 'dvaidi 1' and 'dvaidi 2' in the box below) and hung the sense 'smoke' on one of them; no Avestan word dvaidi 'smoke' is attested anywhere, and the Iranian 'smoke' word is first recorded only in Middle Persian dūd/dūt < Old Iranian *dūta- (beside the parallel *dʰuh₂-mo- of Skt. dhūmá-, Lat. fūmus). The printed page (book p. 100) really does read 'dvaidi 1 : smoke', so the JSON extraction is faithful and the error is Nourai's own; the arrow root → Pahlavi dūd would be correct if this intermediate Avestan box were simply removed.\",\n \"derivation_fa\": \"صورت dvaidī در اوستا واقعاً هست، اما فعل است نه اسم: بارتولمه (ستون ۶۸۸) آن را تنها یک بار، همچون اولْ‌شخصِ مثنایِ میانهٔ ستاک dav- «فشار آوردن، در تنگنا نهادن» (یسنا ۲۹٫۵) ثبت کرده است. پوکورنی نیز در همان صفحهٔ ۲۶۲ همین صورت را با پرسش‌نشان می‌آورد و واژهٔ ایرانیِ «دود» را نه اوستایی، بلکه فارسی میانه (dūt «Rauch») می‌داند. بنابراین «دودِ» اوستایی وجود ندارد؛ نورایی یک صورت واحد را به دو هم‌آوا بخش کرده و معنیِ «دود» را بر یکی از آن دو نهاده است. کهن‌ترین گواهِ این واژه در ایرانی، فارسی میانهٔ dūd/dūt از ایرانی باستان ‎*dūta-‎ است. صفحهٔ چاپی (ص ۱۰۰ کتاب) همین «dvaidi 1 : smoke» را دارد، پس خطا از خوانشِ اسکن نیست، از خودِ کتاب است؛ پژوهش امروزی این حلقه را رد می‌کند.\",\n \"sources\": [S[\"dud\"], S[\"dheu\"]],\n \"ref_check\": [\n   {\"ref\": \"POK:262\", \"status\": \"contradicts\", \"note\": \"Pokorny IEW p. 262 (POK_01 leaf 273) reads: \\\"… Partiz. dhutá-, dhūtá- 'geschüttelt', mpers. dūt 'Rauch'; … av. dvaidi 'wir beide bedrängen'? (*du-vaidī)\\\". The gloss 'smoke' belongs to the Middle Persian word; the Avestan form is glossed 'we two press' and is queried.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 688 s.v. 5.dav-\", \"stance\": \"contradicts\", \"note\": \"grep 'dvaidi' in BRT.txt gives one hit only, under \\\"5.dav- V. '(sich) drängen'. Praes. 1 dav- : du: 1) 'drängen, bedrängen': … dvaidi (1DuM.)\\\" — a verb form, glossed 'press', never 'smoke'.\"},\n   {\"src\": \"AHD\", \"where\": \"dheu-1 (Watkins 1985)\", \"stance\": \"silent\", \"note\": \"Watkins' dheu-1 lists Skt., Greek, Latin, Germanic, Slavic and Welsh material but no Avestan word at all.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 835 ff. 'dheu-, dheuə- stieben, wirbeln'\", \"stance\": \"silent\", \"note\": \"Walde-Pokorny's list of m-formations (ai. dhūmá-, lat. fūmus, lit. dūmai, aksl. dymŭ) contains no Avestan noun.\"}\n ]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"dŭd; dŭtak-mân\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian dūd, written ⟨dwt'⟩ in Book Pahlavi and ⟨dwd⟩ in Manichaean script, 'smoke' (MacKenzie, CPD, 'dūd [dwt' | M dwd, N دود] smoke'; Nyberg, Manual II, 'dūt [dwt'] smoke … MPrth dwd; NP dūd'). It continues Old Iranian *dūta- < PIE zero grade *dʰuh₂-to-/*dʰuh₂- of the root, the ⟨t⟩ of the Pahlavi spelling being the usual historical writing for /d/. Beside it stands the collective dūdag ⟨dwtk⟩ 'family' and the compound dūtak-mān 'smoke-house', i.e. those who sit round one hearth: Horn, Grundriss no. 579 (p. 129), cites 'phlv. dūt \\\"Rauch\\\", dūtakmān (AV.)' from the Ardā Wīrāz-nāmag and 'dūtak \\\"Familie\\\"' from the Bahman Yašt (after Spiegel, Trad. Lit. 406). The semantic figure hearth-smoke → household is the same as Latin focus 'hearth' → 'family'.\",\n \"derivation_fa\": \"فارسی میانهٔ dūd (در پهلویِ کتابی ⟨dwt'⟩ و در مانوی ⟨dwd⟩) «دود»، از ایرانی باستان ‎*dūta-‎ که خود از پایهٔ هندواروپاییِ ‎*dʰuh₂-‎ است؛ «ت» در املای پهلوی نگارشِ تاریخیِ همان /d/ است. در کنارِ آن dūdag ⟨dwtk⟩ «خاندان» و ترکیبِ dūtak-mān «خانهٔ دود» یعنی کسانی که گرد یک اجاق می‌نشینند. هرن (شمارهٔ ۵۷۹، ص ۱۲۹) همین صورت‌ها را از ارداویراف‌نامه و بهمن‌یشت گواه آورده و مکنزی و نیبرگ نیز آن‌ها را تأیید می‌کنند. تحول معنایی «دودِ اجاق ← خانواده» همانندِ لاتینِ focus «اجاق ← خانواده» است. ادعای نورایی در این حلقه درست است.\",\n \"sources\": [S[\"dud\"], S[\"dhumos\"]],\n \"ref_check\": [\n   {\"ref\": \"HRN:129\", \"status\": \"supports\", \"note\": \"Horn, Grundriss (HRN.txt leaf 150 = printed p. 129), entry 579: \\\"dūd 'Rauch', dūdmān 'Familie'. phlv. dūt 'Rauch', dūtakmān (AV.), vergl. dūtak 'Familie' Bahman Yašt (Spiegel, Trad. Lit. S. 406); ai. vergl. dhūmá- 'Rauch'; lat. fūmus, lit. dūma-s, ksl. dymŭ.\\\" — Nourai's Pahlavi box is a direct transcript of this.\"},\n   {\"ref\": \"POK:262\", \"status\": \"supports\", \"note\": \"POK_01 leaf 273 (printed p. 262): \\\"mpers. dūt 'Rauch'\\\" stands in Pokorny's list of verbal/nominal formations of dheu-4.\"},\n   {\"ref\": \"BQT:894\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ p. 894 (BQT_v2_pages.txt leaf 354), Moʿin's footnotes: «از: دود + مان (پسوند مان به‌معنی خانه) … لغةً به‌معنی جای دود» and «… بهلوی dūtak» for دوده; the footnote on دود cites the Old Iranian antecedent and Bartholomae.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 28\", \"stance\": \"supports\", \"note\": \"PHD_mackenzie.txt l. 2100-2101: \\\"dūd [dwt' | M dwd, N دود] smoke\\\" and \\\"dūdag [dwtk | N دوده] family\\\".\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary\", \"stance\": \"supports\", \"note\": \"NYB_vol2_glossary.txt l. 1411: \\\"dūt [dwt'] smoke 202°-24. — MPrth dwd (MHC); NP dūd.\\\"\"}\n ]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"dŭd «دود»; dŭdeh «دوده»; dŭdmân «دودمان»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian دود dūd continues Middle Persian dūd unchanged. دوده dūda is dūd plus the nominal suffix -a (< MP -ag; MacKenzie's dūdag), and carries both of the chart's senses: Borhān-e Qāṭeʿ p. 894 defines دوده as «دودمان و خانواده … و دود چراغ که بجهت ساختن مرکب و سیاهی گیرند», i.e. 'family' and 'lamp-black, soot' — the latter being literally the deposit of smoke, whence its use for making ink. Ferdowsī's line quoted in the box («کزاین دودهٔ سام شد رنگ و بوی») uses the 'lineage' sense, and Hübschmann, Pers. Studien no. 579, notes 'np. dūda \\\"Familie\\\" Firdausī I, 453 v. 334'. دودمان dūdmān is dūd + -mān 'dwelling' (MP mān 'house'), literally 'smoke-house' > 'family, dynasty'; Borhān p. 894: «دودمان … خاندان و خانواده و قبیله را گویند», with Moʿin's footnote «از: دود + مان (پسوند مان به‌معنی خانه)». (Wiktionary's Proto-Iranian *duHmáh for دود is the *dʰuh₂-mós formation and leaves the final -d unexplained; the *dūta- of Moʿin/Horn accounts for it better.)\",\n \"derivation_fa\": \"«دود» در فارسی نو دنبالهٔ بی‌تغییرِ dūd فارسی میانه است. «دوده» = دود + پسوندِ ـه (از ‎-ag‎ فارسی میانه، همان dūdag مکنزی) و در برهان قاطع (ص ۸۹۴) هر دو معنیِ چارت را دارد: «دودمان و خانواده … و دود چراغ که بجهت ساختن مرکب و سیاهی گیرند» — یعنی هم «خاندان» و هم «دوده/سیاهیِ چراغ». بیتِ فردوسی در همین جعبه («کزاین دودهٔ سام شد رنگ و بوی») معنیِ «تبار» را می‌رساند و هوبشمان نیز (شمارهٔ ۵۷۹) همین کاربرد را از شاهنامه گواه آورده است. «دودمان» = دود + پسوندِ ـمان «خانه» (از mān فارسی میانه)، تحت‌اللفظ «خانهٔ دود». حاشیهٔ معین بر برهان همین را می‌گوید. ادعای نورایی درست است.\",\n \"sources\": [S[\"dud\"]],\n \"ref_check\": [\n   {\"ref\": \"BQT:894\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 354 (printed p. 894) carries the headwords دود («معروف است»), دوده and دودمان with exactly the chart's glosses, plus Moʿin's footnote «از: دود + مان (پسوند مان به‌معنی خانه) … بهلوی dūtak».\"},\n   {\"ref\": \"HRN:129\", \"status\": \"supports\", \"note\": \"Horn no. 579 heads the entry \\\"dūd 'Rauch', dūdmān 'Familie'\\\" — the two New Persian words of the box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Persische Studien, on Horn no. 579\", \"stance\": \"supports\", \"note\": \"HUB.txt l. 2234: \\\"579. Dazu auch np. dūda 'Familie' Firdausī I, 453, v. 334.\\\" — the Šāh-nāma use that the chart's Ferdowsī quotation illustrates.\"},\n   {\"src\": \"PHD\", \"where\": \"CPD p. 28\", \"stance\": \"supports\", \"note\": \"'dūdag [dwtk | N دوده] family' — MacKenzie explicitly equates MP dūdag with NP دوده.\"},\n   {\"src\": \"BQT\", \"where\": \"p. 894\", \"stance\": \"supports\", \"note\": \"«دوده … و دود چراغ که بجهت ساختن مرکب و سیاهی گیرند» = soot / lamp-black.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Avestan\", \"words\": \"dav 1; dvaidi 2\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Bartholomae's AiW col. 688 has \\\"5.dav- V. '(sich) drängen'. Praes. 1 dav- : du: 1) 'drängen, bedrängen' … dvaidi (1DuM.)\\\" (Y 29.5) and the participle davąsanā (Y 31.10); his only etymological remark is \\\"Vgl. ai. dhūnoti 'er schüttelt'(?)\\\" — with a question mark. Pokorny p. 262 prints the same form and the same doubt: \\\"av. dvaidi 'wir beide bedrängen'? (*du-vaidī)\\\". So the arrow root → Avestan dav- is precisely what both of Nourai's cited authorities say, and both flag it as uncertain, which is what the chart's own NOTE reports. Semantically the bridge would be PIE 'shake, whirl up, set in violent motion' → Iranian 'press hard on, importune'; that is possible but nowhere established, and Cheung's Etymological Dictionary of the Iranian Verb sets up no Iranian root *dau- 'to press' at all. Verdict: plausible, and the NOTE is accurate.\",\n \"derivation_fa\": \"بارتولمه در ستون ۶۸۸ ستاکِ ‎5.dav-‎ «فشار آوردن، در تنگنا نهادن» را با صورتِ مثنّای میانهٔ dvaidī (یسنا ۲۹٫۵) ثبت کرده و تنها یادداشتِ ریشه‌شناختی‌اش این است: «قس. سنسکریت dhūnoti ‹می‌جنباند›(؟)» — با علامتِ پرسش. پوکورنی (ص ۲۶۲) نیز همان صورت و همان تردید را دارد. پس پیوندِ ریشه ← dav- دقیقاً همان چیزی است که هر دو مرجعِ خودِ نورایی می‌گویند و هر دو آن را قطعی نمی‌دانند؛ یادداشتِ خودِ چارت («نه پوکورنی و نه بارتولمه در این اشتقاق مطمئن نیستند») درست است. گذارِ معنایی «جنباندن/به‌گردباد درآوردن ← فشار آوردن» ممکن است اما اثبات‌نشده، و چونگ اصلاً ریشهٔ ایرانیِ ‎*dau-‎ «فشردن» نمی‌شناسد. با احتیاط پذیرفتنی است.\",\n \"sources\": [S[\"dheu\"]],\n \"ref_check\": [\n   {\"ref\": \"POK:262\", \"status\": \"supports\", \"note\": \"POK_01 leaf 273 (p. 262): \\\"av. dvaidi 'wir beide bedrängen'? (*du-vaidī)\\\" — Pokorny does place the form under dheu-4, with a question mark, exactly as the chart's NOTE says.\"},\n   {\"ref\": \"BRT:688\", \"status\": \"supports\", \"note\": \"BRT.txt around l. 12816 carries the running head '*dav- 688'; the entry reads \\\"5.dav- V. '(sich) drängen'. Praes. 1 dav-: du: 1) 'drängen, bedrängen': mē urvā gəuščā … dvaidi (1DuM.) … Y.29.5\\\", with the note \\\"Vgl. ai. dhūnoti 'er schüttelt'(?)\\\".\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"Etym. Dict. of the Iranian Verb\", \"stance\": \"silent\", \"note\": \"no Iranian verbal root *dau- 'to press' is set up; the only *dau- entries concern 'to run/flow' and 'to speak/deceive'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 835 ff.\", \"stance\": \"silent\", \"note\": \"Walde-Pokorny's 'dheu-, dheuə- stieben, wirbeln' lists the verbal formations (ai. dhūnóti, gr. θύω, anord. dyja) without any Avestan member.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Avestan\", \"words\": \"han-davathe\",\n \"verdict\": \"disputed\",\n \"derivation\": \"There is no Avestan word han-davaθa-: Bartholomae's AiW has no han-dav- compound (grep of BRT.txt for handav-/han-dva- returns only han-dvarəna- 'companion', an unrelated formation). The form comes from Moʿin's footnote in Borhān-e Qāṭeʿ p. 172 s.v. اندوهگین, which I read from the page image: «handôh (اندوه) مرکب از han-davatha مشتق از dav (فشار دادن) • بارتولمه ۶۸۸ ، نیبرگ ۱۰۰» — a reconstruction (*ham-davaθa-), not an attested lemma, and Nourai copies it as an Avestan headword with the ending changed to -the. The etymology itself is rejected by current Iranian scholarship: Cheung, Etym. Dict. of the Iranian Verb p. 400, assigns MP/NP andōh to *ham- + *θuaxš- 'to be busy, to strive' (Av. θβaxš-, OP haṃtaxš-), citing Manichaean MP ʾndwxyn 'sorrowful', Sogdian ʾnt(ʾ)wxs- 'to strive, endeavour' and Chorasmian ʾndyx 'sorrow' — the -xš- of those cognates cannot be got out of *dav-.\",\n \"derivation_fa\": \"واژهٔ اوستاییِ ‎han-davaθa-‎ وجود ندارد؛ در فرهنگِ بارتولمه هیچ ترکیبِ ‎han-dav-‎ نیست. این صورت از حاشیهٔ معین بر برهان قاطع (ص ۱۷۲، ذیل «اندوهگین») گرفته شده است که از روی تصویرِ صفحه خواندم: «handôh (اندوه) مرکب از han-davatha مشتق از dav (فشار دادن) • بارتولمه ۶۸۸، نیبرگ ۱۰۰» — یعنی صورتی بازسازی‌شده (‎*ham-davaθa-‎)، نه واژه‌ای گواهی‌شده؛ نورایی همان را با پایانهٔ ‎-the‎ همچون سرواژهٔ اوستایی آورده است. ریشه‌شناسیِ امروزی این را رد می‌کند: چونگ (۲۰۰۷، ص ۴۰۰) اندوه را از ‎*ham-‎ + ‎*θuaxš-‎ «کوشیدن، سرگرمِ کاری بودن» می‌داند (اوستایی θβaxš-، پارسی باستان ham-taxš-) و گواهانِ فارسی میانهٔ مانوی ʾndwxyn، سغدیِ ʾntwxs- و خوارزمیِ ʾndyx را می‌آورد؛ خوشهٔ ‎-xš-‎ این هم‌ریشه‌ها را نمی‌توان از dav- بیرون آورد.\",\n \"sources\": [S[\"andoh\"]],\n \"ref_check\": [\n   {\"ref\": \"BQT:172\", \"status\": \"partial\", \"note\": \"Borhān-e Qāṭeʿ p. 172 (archive.org borhan-ghate-v1 leaf n390; text saved to data/verification/sources/refs/ocr/BQT/172.vision.txt) does print «handôh (اندوه) مرکب از han-davatha مشتق از dav (فشار دادن)» with the references «بارتولمه ۶۸۸، نیبرگ ۱۰۰». So Nourai reports his source faithfully — but Moʿin gives it as a reconstruction, not as an attested Avestan word, and the reference he leans on (Bartholomae col. 688) has no such compound.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 688 and the han- entries\", \"stance\": \"contradicts\", \"note\": \"grep of BRT.txt for 'handav|han-dva|hqndav' returns only \\\"han-dvarəna- Adj. 'Genosse'\\\"; there is no han-davaθa-, so Moʿin's citation of Bartholomae 688 covers only the simplex dav-.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p. 400 s.v. *θuaxš (tuxš) 'to be busy, working on'\", \"stance\": \"contradicts\", \"note\": \"\\\"*MIDDLE PERSIAN: MMP twxs- 'to strive' … || (+ *ham-) BMP ʾndwh /andōh/ 'sorrow', MMP ʾndwxyn 'sad, sorrowful'\\\"; *SOGDIAN \\\"(+ *ham-) BSogd. ʾnt(ʾ)wxs … 'to strive'\\\"; *NWIR \\\"(+ *ham-) NP andōh 'anxious'\\\".\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary p. 100\", \"stance\": \"partial\", \"note\": \"NYB_vol2_glossary.txt l. 1894: \\\"handōhakan [hndwhkn'] anxious … Arm. lw. andohakan 'disquieting, dreadful'\\\" — the page Moʿin cites; Nyberg gives the Middle Persian form but no Avestan antecedent.\"}\n ]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Persian\", \"words\": \"andŭh «اندوه»; andŭhgîn «اندوهگین»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The words are real and the Middle Persian ancestry is right, but the route through Avestan dav- 'to press' is not. NP اندوه continues MP handōh ⟨ʾndwh⟩ 'sorrow' (MacKenzie, CPD 10: \\\"andōh [ʾndwh | M ʾndwx-, N اندوه] sorrow\\\"), and اندوهگین continues MP andōhgēn / handōh(a)gēn 'sorrowful' (MacKenzie 'andōhgēn'; Nyberg II 100 handōhakan, whence the Armenian loan andohakan 'dreadful'); the suffix is MP -gēn > NP -گین. The decisive evidence is MacKenzie's and Cheung's Manichaean citation ʾndwx-: with -xš- in the Sogdian ʾntwxs- 'to strive' and Chorasmian ʾndyx 'sorrow', the word belongs to *ham- + *θuaxš- 'to be busy, be burdened with' (Av. θβaxš-, OP haṃtaxš- 'to work at'), the semantic path being 'preoccupation, being taken up with something' → 'care, sorrow' (Cheung 400). Wiktionary likewise gives only 'inherited from Middle Persian ʾndwh, noun form of the verb اندوهیدن'. The Borhān/Moʿin derivation that Nourai follows is a pre-Cheung guess.\",\n \"derivation_fa\": \"خودِ واژه‌ها و پیشینهٔ فارسی‌میانه‌شان درست است، اما راهِ اشتقاق نادرست. «اندوه» دنبالهٔ handōh ⟨ʾndwh⟩ فارسی میانه است (مکنزی: «andōh [ʾndwh | مانوی ʾndwx-] sorrow») و «اندوهگین» دنبالهٔ handōh(a)gēn با پسوندِ ‎-gēn‎ > ـگین؛ وامواژهٔ ارمنیِ andohakan نیز همین صورتِ میانه را نشان می‌دهد. گواهِ قاطع، صورتِ مانویِ ʾndwx- در کنارِ سغدیِ ʾntwxs- «کوشیدن» و خوارزمیِ ʾndyx «اندوه» است: این خوشهٔ ‎-xš-‎ نشان می‌دهد واژه از ‎*ham-‎ + ‎*θuaxš-‎ «سرگرمِ کاری بودن، کوشیدن» است (اوستایی θβaxš-، پارسی باستان ham-taxš-) و تحول معنایی‌اش «گرفتاریِ خاطر ← غم» بوده است (چونگ ۲۰۰۷، ص ۴۰۰). ویکی‌واژه نیز تنها فارسی میانه را می‌آورد. اشتقاقِ برهان/معین که نورایی از آن پیروی کرده، حدسی پیش از پژوهشِ چونگ است؛ پژوهش امروزی آن را رد می‌کند.\",\n \"sources\": [S[\"andoh\"]],\n \"ref_check\": [\n   {\"ref\": \"BQT:172\", \"status\": \"partial\", \"note\": \"Moʿin's footnote on p. 172 («اندوهگین … پهلوی handôh(a)kên … ارمنی andohakan … handôh مرکب از han-davatha مشتق از dav») supplies the Middle Persian and Armenian forms correctly but the Old Iranian derivation is his own and is now superseded.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 10\", \"stance\": \"supports\", \"note\": \"PHD_mackenzie.txt l. 1094: \\\"andōh [ʾndwh | M ʾndwx-, N اندوه] sorrow\\\"; l. 7513/7635 'andōhgēn' for 'sad/sorrowful' — the Middle Persian antecedents of both Persian words.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p. 400\", \"stance\": \"contradicts\", \"note\": \"\\\"*NWIR: NP tuxšidan 'to strive', taxša 'diligent' || (+ *ham-) NP andōh 'anxious'\\\" under the root *θuaxš — a different origin from Nourai's.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual II glossary, handōhakan\", \"stance\": \"partial\", \"note\": \"gives handōhakan and the Armenian loan, with no Avestan source.\"}\n ]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Greek\", \"words\": \"tuphein; tuphos; tuphun\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Greek τύφω / inf. τύφειν 'to raise smoke, make smoulder', τῦφος 'smoke, vapour; (metaphorically) stupor, delusion, conceit', τυφλός 'blind' and τυφώς / gen. τυφῶνος 'whirlwind, hurricane' (personified as the monster Typhon). Nourai's 'tuphun' is his transliteration of the oblique stem τυφῶν-, not a separate word. Walde-Pokorny I put all of these under the bh-extension of the root: \\\"3. bh-Erw. dheubh- 'stieben, rauchen; nebelig, verdunkelt, auch vom Geist und den Sinnen': Gr. τύφω … τῦφος … τυφώς 'Wirbelwind, Ungewitter' … τυφλός 'blind'\\\", beside OIr. dub 'black', Goth. daufs, dumbs, dūbō; Watkins/AHD dheu-1 §10 does the same (\\\"Zero-grade extended form *dhubh- in Greek tuphein … and tuphlos, blind: TYPHUS\\\"). That is exactly the chart's 'Dhu-bh'. The caution: Klein himself, on the very page Nourai cites, says these Greek words \\\"are of uncertain origin\\\" and only 'possibly' derive from *dheu-bh-, and Beekes (reported by Etymonline s.v. typhus) rejects the IE derivation and treats τῦφος as Pre-Greek; Mann's IEC also files τύφος under a separate dhubh- (2) 'weak, flat, silly'. Hence plausible rather than confirmed.\",\n \"derivation_fa\": \"یونانیِ τύφω / τύφειν «دود کردن، دود برانگیختن»، τῦφος «دود، بخار» و به‌مجاز «گیجی، خودپسندی»، τυφλός «کور» و τυφώς / τυφῶνος «گردباد» (که همان تیفونِ اساطیری است). صورتِ «tuphun» در چارت آوانگاریِ ستاکِ ‎τυφῶν-‎ است، نه واژه‌ای جدا. والده-پوکورنی همهٔ این‌ها را ذیلِ گسترشِ ‎-bh-‎ ریشه («dheubh- ‹برخاستنِ گرد، دود کردن؛ مه‌آلود، تیره، حتی در ذهن و حواس›») می‌آورد و واتکینز/AHD نیز همین کار را می‌کند؛ این همان «Dhu-bh» عنوانِ چارت است. اما احتیاط لازم است: کلاین در همان صفحه‌ای که نورایی ارجاع می‌دهد این واژه‌های یونانی را «با خاستگاهِ نامعلوم» می‌خواند و بیکس آن‌ها را پیش‌یونانی می‌داند؛ مان هم τύφος را ذیلِ ریشهٔ جداگانه‌ای می‌گذارد. پس با احتیاط پذیرفتنی است.\",\n \"sources\": [S[\"typhus\"], S[\"typhoon\"]],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985, dheu-1 §10: \\\"Zero-grade extended form *dhubh- in Greek tuphein (< *thuphein), to make smoke, and tuphlos, blind: TYPHUS; TYPHLOSOLE.\\\"\"},\n   {\"ref\": \"KLN:1670\", \"status\": \"partial\", \"note\": \"KLN_1966.txt leaf 885 (printed ~1670), s.v. typhus: \\\"Medical L., fr. Gk. τῦφος, 'smoke, mist, cloud, fever accompanied by stupor', which is rel. to τύφειν 'to smoke', τυφλός 'blind', τυφῶν 'whirlwind'. These words are of uncertain origin. They are perh. cogn. with Goth. daufs … All these words possibly derive fr. I.-E. base *dheu-bh-, *dhu-bh-.\\\" — the root link is offered only as a possibility.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I, '3. bh-Erw. dheubh-'\", \"stance\": \"supports\", \"note\": \"\\\"Gr. τύφω (θύψαι, τυφῆναι) 'Rauch, Dampf, Qualm machen …', τῦφος n. 'Rauch, Dampf, Qualm; Benebelung, Torheit, dummer Stolz', … τυφώς, -ῶ oder -ῶνος 'Wirbelwind, Ungewitter'; τυφλός 'blind, dunkel, blöde'.\\\"\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, dhubh- (2) and dhubhlos (2)\", \"stance\": \"partial\", \"note\": \"IEC.txt l. 3213 'dhubh- (2) \\\"weak, flat, silly, soft, mad…\\\" Gk. túphos \\\"stupefaction\\\"' and l. 3220 'dhubhlos (2) & dhubhros \\\"dark, deep, dirty\\\" … Gk. tuphlós \\\"blind\\\"' — Mann keeps these apart from his dhūmos 'smoke'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. thio-\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt l. 39044 lists 'typhlo-, typhus' among the offspring of \\\"base *dheu-, 'to fly about like dust, to smoke, whirl…'\\\", along with deaf, dull, deer, dizzy, down, dust, fume.\"}\n ]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Latin\", \"words\": \"\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Empty pass-through box: it stands for the Modern (Medical) Latin typhus, the disease name coined by François Boissier de Sauvages in his Nosologia methodica (1759) directly from Greek τῦφος 'stupor', because the patient falls into a smoky torpor. Klein s.v. typhus: \\\"Medical L., fr. Gk. τῦφος\\\"; Etymonline: \\\"1785, from medical Latin\\\". Classical Latin had borrowed only typhōn 'whirlwind' and the adjective typhōnicus (Vulgate, Acts 27:14 ventus typhonicus), not typhus in this sense — so the box is right only if 'Latin' is read as New Latin, which is Nourai's usual practice for scientific vocabulary.\",\n \"derivation_fa\": \"این جعبهٔ خالی حلقهٔ واسطه است و مرادِ نورایی «لاتینِ نو (لاتینِ پزشکی)» است: نامِ بیماری typhus را بواسیه دو سُواژ در «نوزولوژیا متودیکا» (۱۷۵۹ م) مستقیماً از τῦφος یونانی به‌معنی «کرختی و گیجیِ تب‌آلود» ساخت. کلاین می‌نویسد «لاتینِ پزشکی، از τῦφος یونانی» و اتیمآنلاین نیز آغازِ کاربردِ انگلیسی را ۱۷۸۵ م از همان لاتینِ پزشکی می‌داند. لاتینِ کلاسیک تنها typhōn «گردباد» و صفتِ typhōnicus را وام گرفته بود، نه typhus را به این معنی. پس اگر «لاتین» را لاتینِ نو بخوانیم، حلقه درست است.\",\n \"sources\": [S[\"typhus\"]],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the book.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. typhus (KLN_1966 leaf 885)\", \"stance\": \"supports\", \"note\": \"\\\"typhus, n. — Medical L., fr. Gk. τῦφος …\\\" — i.e. New Latin, not classical Latin.\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.v. typhus (web archive)\", \"stance\": \"supports\", \"note\": \"\\\"1785, from medical Latin, from Greek typhos 'stupor caused by fever', literally 'smoke'.\\\"\"}\n ]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Empty pass-through box for French typhus (attested from 1806, taken over unchanged from the medical Latin) and typhoïde, from Greek τυφώδης 'typhus-like'; fièvre typhoïde was established as the name of the distinct disease by Pierre-Charles-Alexandre Louis in Paris in 1829. French is the right intermediary for the two Persian forms in the next box, because Persian medical and scientific vocabulary of the Qajar and early Pahlavi period came through the Dar al-Funun and French-language medicine, and the Persian shapes تیفوس / تیفوئید reproduce French [tifys] / [tifɔid] rather than English pronunciations.\",\n \"derivation_fa\": \"این جعبهٔ خالی نمایندهٔ فرانسویِ typhus (از ۱۸۰۶ م، بی‌تغییر از لاتینِ پزشکی) و typhoïde (از یونانیِ τυφώδης «تیفوس‌مانند») است؛ نامِ fièvre typhoïde را پیر لویی در ۱۸۲۹ م در پاریس برای بیماریِ جداگانه به کار برد. واسطه‌بودنِ فرانسه برای دو واژهٔ فارسیِ جعبهٔ بعد درست است، زیرا واژگانِ پزشکیِ فارسی در دورهٔ قاجار و پهلویِ نخست از راهِ دارالفنون و پزشکیِ فرانسوی‌زبان آمده و صورتِ «تیفوس/تیفوئید» تلفظِ فرانسوی را بازمی‌تاباند، نه انگلیسی را.\",\n \"sources\": [S[\"typhus\"]],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the book.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.vv. تیفوس، تیفوئید\", \"stance\": \"supports\", \"note\": \"MON_part1.txt ll. 45661-45672 print each headword followed by the European source form in Latin script (badly damaged in the OCR) and the tag (پز.) 'medical' — Moʿin treats both as modern European loans, not as inherited words.\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.v. typhus\", \"stance\": \"supports\", \"note\": \"gives the medical-Latin > modern-European route that the French box represents.\"}\n ]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Persian\", \"words\": \"tîfŭs «تیفوس»; tîfoîd «تیفوئید»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both are twentieth-century medical loanwords, taken from French: تیفوس from typhus (the ـوس ending renders French -us; an English source would have given *تایفوس, with the diphthong) and تیفوئید from typhoïde, the hamza-carrier ئـ reproducing the French diaeresis in -oïde. Moʿin's Farhang defines تیفوس as «مرضی عفونی که به وسیلهٔ شپش سرایت کند و چون علایم ظاهری آن شبیه به تیفوئید (حصبه) است بدین نام خوانده شده … آن را تیفوس پتشیال یا تیفوس اکزانتماتیک نامند» and تیفوئید simply as «حصبه», both flagged (پز.) 'medical'. The whole chain Greek τῦφος → New Latin typhus → French → Persian is thus exactly as the chart draws it.\",\n \"derivation_fa\": \"هر دو وام‌واژهٔ پزشکیِ سدهٔ بیستم و از راهِ فرانسه‌اند: «تیفوس» از typhus فرانسوی (پایانهٔ ـوس همان ‎-us‎ فرانسوی است؛ اگر از انگلیسی می‌آمد «تایفوس» می‌شد) و «تیفوئید» از typhoïde که همزهٔ «ئـ» بازتابِ همان دو نقطهٔ فرانسویِ ‎-oïde‎ است. معین در فرهنگ فارسی تیفوس را «مرضی عفونی که به وسیلهٔ شپش سرایت کند … تیفوس پتشیال یا تیفوس اکزانتماتیک» و تیفوئید را «حصبه» تعریف می‌کند و هر دو را با نشانِ (پز.) می‌آورد. زنجیرهٔ یونانی ← لاتینِ نو ← فرانسه ← فارسی همان است که چارت کشیده. ادعای نورایی درست است.\",\n \"sources\": [S[\"typhus\"]],\n \"ref_check\": [\n   {\"ref\": \"MON:1181\", \"status\": \"supports\", \"note\": \"MON_part1.txt ll. 45660-45672 (grep 'تیفوس') give «تیفوئید … (پز.) حصبه» and «تیفوس … (پز.) مرضی عفونی که به وسیلهٔ شپش سرایت کند …», each preceded by the Latin-script European source form; the printed page cannot be checked against the OCR file, but the entries are present and say what Nourai reports.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.vv. تیفوس، تیفوئید\", \"stance\": \"supports\", \"note\": \"both are given as European medical loans, defined exactly as in the chart ('typhus', 'typhoid = حصبه').\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.v. typhus\", \"stance\": \"supports\", \"note\": \"confirms the medical-Latin coinage of 1759/1785 that the French and Persian forms continue.\"}\n ]\n})\n\nnodes.append({\n \"id\": 11, \"lang\": \"English\", \"words\": \"typhus, typhoid\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English typhus is first recorded in 1785, straight from the medical Latin of Boissier de Sauvages; typhoid is first an adjective, 'resembling typhus' (1800), from Greek τυφώδης, and becomes a noun (typhoid fever) after Louis' 1829 separation of the two diseases. Watkins/AHD lists TYPHUS under dheu-1 §10, i.e. under the same root as the chart, and Klein s.v. typho- notes it is 'used in the sense of typhus (med.)'. The chart's arrow Latin → English is therefore right, though the modern-Latin term also reached English partly through French.\",\n \"derivation_fa\": \"واژهٔ انگلیسیِ typhus نخستین بار در ۱۷۸۵ م، یکسره از لاتینِ پزشکیِ بواسیه دو سُواژ، ثبت شده است؛ typhoid نخست صفت بوده به‌معنی «تیفوس‌مانند» (۱۸۰۰ م) از یونانیِ τυφώδης و پس از جدا کردنِ دو بیماری به دستِ لویی (۱۸۲۹ م) اسم شده است. واتکینز در پیوستِ ریشه‌های هندواروپاییِ AHD همین TYPHUS را ذیلِ ‎dheu-1‎ می‌آورد، یعنی همان ریشهٔ چارت. پس پیکانِ لاتین ← انگلیسی درست است، هرچند بخشی از راه از فرانسه هم گذشته است.\",\n \"sources\": [S[\"typhus\"]],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 dheu-1 §10 ends '…and tuphlos, blind: TYPHUS; TYPHLOSOLE', and the index (AHD_watkins1985.txt l. 2389) has 'THYME dheu-1' etc.; TYPHUS is credited to this root.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.vv. typhus, typhoid, typho- (leaf 885)\", \"stance\": \"supports\", \"note\": \"\\\"typho-, … used in the sense of typhus (med.) — Gk. τυφο-, τυφ-, fr. τῦφος. See typhus.\\\" and 'Derivative: typhoid-al, adj.'\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.v. typhus\", \"stance\": \"supports\", \"note\": \"\\\"1785, from medical Latin, from Greek typhos 'stupor caused by fever' …\\\"\"}\n ]\n})\n\nnodes.append({\n \"id\": 12, \"lang\": \"Arabic\", \"words\": \"tŭfân\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Arabic طوفان ṭūfān is Qurʾānic (7:133 and 29:14) and means primarily 'the Deluge, the Flood'. Jeffery, The Foreign Vocabulary of the Qurʾān, pp. 207-208, follows Fraenkel in deriving it from the Aramaic/Rabbinic טופנא ṭawpānā (Onkelos on Gen. 7), Syriac ܛܘܦܢܐ ṭawpānā (Peshitta Gen. 6:17, rendering κατακλυσμός) and Mandaic ṭaupana; he says the theory 'has been generally accepted' and adds, in the footnote on the same page, that the word 'can hardly be connected, however, with the Gk. τυφῶν'. Wiktionary likewise routes the Arabic word 'through Aramaic ṭōpānā (Classical Syriac ṭawpānā)'. Yule (Hobson-Jobson s.v. TYPHOON) leaves the Semitic root ṭ-w-f 'to go round' as a possible native source and suggests only that the post-classical sense 'whirlwind' — which is not in classical Arabic — may be a late loan from a modern reflex of τυφῶν. So Klein's derivation of the Arabic noun straight from Greek τυφῶν, which Nourai adopts, is a minority position; at most Greek touched the later meteorological sense, not the word.\",\n \"derivation_fa\": \"«طوفان» عربیِ قرآنی است (اعراف ۱۳۳ و عنکبوت ۱۴) و معنی نخستینش «سیلِ بزرگ، طوفانِ نوح» است. جفری در «واژگانِ دخیل در قرآن» (ص ۲۰۷–۲۰۸) به پیروی از فرنکل آن را وام‌واژه‌ای آرامی می‌داند: טופנא ṭawpānā (ترجومِ اونقلوس بر سِفر پیدایش ۷) و سریانیِ ṭawpānā و مندائیِ ṭaupana؛ و در پانوشتِ همان صفحه صریحاً می‌نویسد که «به‌سختی می‌توان آن را با τυφῶν یونانی پیوند داد». ویکی‌واژه نیز همین راهِ آرامی را می‌آورد. یول در «هابسن-جابسن» ریشهٔ سامیِ ط-و-ف «گِرد چیزی گشتن» را ممکن می‌شمرد و تنها معنیِ متأخّرِ «گردباد» را شاید وام از صورت‌های نوِ τυφῶν می‌داند. پس اشتقاقِ کلاین (یونانی ← عربی) که نورایی پذیرفته، نظری اقلیّتی است؛ پژوهش امروزی خاستگاهِ آرامی/سامی را ترجیح می‌دهد.\",\n \"sources\": [S[\"tufan\"], S[\"typhoon\"]],\n \"ref_check\": [\n   {\"ref\": \"KLN:1670\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 885, s.v. typhoon: \\\"Chin. tai fung, lit. 'great wind'; influenced in form by Arab. tufan (whence also Port. tufão), fr. Gk. τυφῶν, 'whirlwind' (see typhus).\\\" Klein does derive the Arabic word from Greek — but only in passing, and the same entry makes Chinese the source of the English word.\"},\n   {\"ref\": \"SKT:581\", \"status\": \"contradicts\", \"note\": \"Skeat, Concise Etym. Dict. (SKT.txt leaf 557), s.v. Typhoon: \\\"a violent whirlwind. (Chinese) … it is a Chinese word … ta 'great', fung 'wind' … the spelling typhoon is due to confusion with the old word typhon … from Gk. τυφῶν, a whirlwind.\\\" Skeat mentions no Arabic word at all, so this citation cannot support a Greek → Arabic arrow. (Note: the entry sits at printed p. ~537 of the 1911 Concise edition, not 581; Nourai may be citing another printing.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"FVQ\", \"where\": \"Jeffery pp. 207-208 s.v. ṭūfān (FVQ_pages.txt leaf 224)\", \"stance\": \"contradicts\", \"note\": \"\\\"Fraenkel, Vocab, 22, recognized that it was the Rabbinic ṭwpnʾ which is used, e.g., by Onkelos in Gen. vii … Fraenkel's theory has been generally accepted\\\", with n. 3: \\\"It can hardly be connected, however, with the Gk. τυφῶν.\\\"\"},\n   {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. TYPHOON, pp. 947-950\", \"stance\": \"partial\", \"note\": \"\\\"In Arabic the root ṭ-w-f means 'to go round', and a combination of this idea with the sense of sudden disaster might conceivably have given the new meaning to the word. On the other hand it seems simpler to regard this sense as a late loan from some modern form of τυφῶν, typho, or tifone.\\\"\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1990\", \"stance\": \"partial\", \"note\": \"\\\"Erst über ar. ṭūfān 'heftiger Sturm' entstand pg. tufão, tofano\\\" — Lokotsch uses the Arabic word only as the mediator of the Portuguese form, and offers no Greek etymology for it.\"}\n ]\n})\n\nnodes.append({\n \"id\": 13, \"lang\": \"Persian\", \"words\": \"tŭfân «طوفان»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian طوفان is a straightforward Arabic loan, kept with the Arabic ṭāʾ, and it carries the Arabic sense first: Moʿin's Farhang defines it «باران سخت، آب بسیار که همه را بپوشد و غرق کند» ('violent rain; a flood that covers and drowns everything') and only then the modern meteorological «باد شدید و ناگهانی که موجب خسارت … شود». Ḥāfeẓ's couplet quoted in the box («حافظ از دست مده دولت این کشتی نوح / ورنه طوفان حوادث ببرد بنیادت») uses the Deluge sense, with Noah's ark alongside. One caveat worth adding to the chart: Moʿin warns under the separate entry توفان (the present participle of توفیدن 'to roar, rage') that «در بعض فرهنگ‌ها «توفان» را فارسی [و] «طوفان» را … گرفته‌اند ولی این دو کلمه با هم ربطی ندارد» — the native Persian توفان and the Arabic loan طوفان are unrelated homophones. The arrow Arabic → Persian is right; only the Greek origin of the Arabic word behind it (node 12) is doubtful.\",\n \"derivation_fa\": \"«طوفان» در فارسی وام‌واژه‌ای عربی است که با «ط» نوشته می‌شود و نخست همان معنیِ عربی را دارد: معین در فرهنگ فارسی آن را «باران سخت، آب بسیار که همه را بپوشد و غرق کند» می‌آورد و تنها پس از آن معنیِ هواشناختیِ «باد شدید و ناگهانی» را. بیتِ حافظ در همین جعبه («حافظ از دست مده دولت این کشتی نوح / ورنه طوفان حوادث ببرد بنیادت») به همان طوفانِ نوح اشاره دارد. نکتهٔ سودمند این‌که معین ذیلِ «توفان» (اسمِ فاعلِ توفیدن) هشدار می‌دهد: «در بعض فرهنگ‌ها ‹توفان› را فارسی [و] ‹طوفان› را … گرفته‌اند ولی این دو کلمه با هم ربطی ندارد» — یعنی «توفانِ» فارسی و «طوفانِ» عربی هم‌آوا و بی‌خویشاوندند. پیکانِ عربی ← فارسی درست است؛ تنها خاستگاهِ یونانیِ واژهٔ عربی (گرهِ ۱۲) محلِ تردید است.\",\n \"sources\": [S[\"tufan\"]],\n \"ref_check\": [\n   {\"ref\": \"MON:2240\", \"status\": \"supports\", \"note\": \"MON_part1.txt l. 93275 ff. (grep 'طوفان'): «طوفان: … (اِ.) باران سخت. آب بسیار که همه را بپوشد و غرق کند. (زه.) باد شدید و ناگهانی که موجب خسارت و خرابی ابنیه و ساختمان‌ها شود …» — the two senses the chart gives ('typhoon, rain').\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. توفان (MON_part1.txt l. 45038 ff.)\", \"stance\": \"partial\", \"note\": \"«توفان: (صفت فاعلی از توفیدن) شور و غوغا کننده، فریاد کننده، غران … ضح.- در بعض فرهنگ‌ها ‹توفان› را فارسی، ‹طوفان› را … گرفته‌اند ولی این دو کلمه با هم ربطی ندارد.» — Moʿin keeps the native Persian participle apart from the Arabic loan.\"},\n   {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. TYPHOON\", \"stance\": \"supports\", \"note\": \"Yule treats tūfān as an Arabic/Persian/Urdu word for a great storm, current all over the Indian Ocean world — the sense the Persian word has.\"}\n ]\n})\n\nnodes.append({\n \"id\": 14, \"lang\": \"English\", \"words\": \"typhoon\",\n \"verdict\": \"plausible\",\n \"derivation\": \"English typhoon is a convergence of two, arguably three, words, and Nourai's arrow captures only one strand — but a real one. (a) The sense 'great cyclonic storm of the Indian Ocean and the China Sea' entered European languages through Portuguese tufão in the mid-16th century, from Arabic/Persian/Urdu ṭūfān; Yule (Hobson-Jobson s.v. TYPHOON) says 'the probability is that Vasco [da Gama] and his followers got the tufão … direct from the Arab pilots', and the first English attestations are Touffon/Tuffon (1588, Hickock's translation of Caesar Frederick). (b) Greek τυφῶν entered English separately in the 1550s as Tiphon 'whirlwind'. (c) Cantonese 大風 tai fung 'great wind' is what Klein, Skeat and Lokotsch make the source of the modern form. Etymonline's summary — Arabic/Persian tufān for the meaning, Greek typhon and Chinese tai fung for the shape — vindicates Nourai's arrow for the sense while showing it is not the whole story. Nourai's own NOTE reports Klein's Chinese derivation accurately.\",\n \"derivation_fa\": \"واژهٔ انگلیسیِ typhoon برآیندِ هم‌نشینیِ دو (بلکه سه) واژه است و پیکانِ نورایی تنها یک رشتهٔ آن را می‌گیرد — رشته‌ای واقعی اما نه تمامِ داستان. نخست، معنیِ «تندبادِ سهمگینِ اقیانوس هند و دریای چین» در میانهٔ سدهٔ شانزدهم از راهِ پرتغالیِ tufão و آن از عربی/فارسی/اردوِ «طوفان» به زبان‌های اروپایی رسید؛ یول در هابسن-جابسن می‌نویسد که به احتمالِ زیاد واسکو دا گاما و همراهانش این واژه را یکسر از ناخدایانِ عرب گرفتند و نخستین گواهانِ انگلیسی Touffon (۱۵۸۸ م) است. دوم، τυφῶν یونانی جداگانه در دههٔ ۱۵۵۰ م به‌صورتِ Tiphon «گردباد» وارد انگلیسی شد. سوم، چینیِ کانتونیِ tai fung «بادِ بزرگ» که کلاین و اسکیت و لوکوچ آن را خاستگاهِ صورتِ امروزی می‌دانند. پس ادعای نورایی برای «معنی» پذیرفتنی است اما برای «صورت» ناقص؛ یادداشتِ خودِ او دربارهٔ نظرِ کلاین درست نقل شده است.\",\n \"sources\": [S[\"typhoon\"]],\n \"ref_check\": [\n   {\"ref\": \"SKT:581\", \"status\": \"contradicts\", \"note\": \"SKT.txt leaf 557, s.v. Typhoon: \\\"a violent whirlwind. (Chinese) … it is a Chinese word … ta 'great', fung 'wind' … the spelling typhoon is due to confusion with the old word typhon (not uncommon in old authors), from Gk. τυφῶν, a whirlwind.\\\" Skeat derives the English word from Chinese and says nothing of Arabic, so he does not support the arrow as drawn. (The entry stands at printed p. ~537 of the 1911 Concise edition; Nourai's page 581 must belong to another printing.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. typhoon (leaf 885 ≈ p. 1670)\", \"stance\": \"partial\", \"note\": \"\\\"Chin. tai fung, lit. 'great wind'; influenced in form by Arab. tufan (whence also Port. tufão), fr. Gk. τυφῶν\\\" — Arabic is admitted only as an influence, exactly as the chart's NOTE reports.\"},\n   {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. TYPHOON (pp. 947-950) and Introduction\", \"stance\": \"supports\", \"note\": \"Yule ridicules the Chinese derivation ('there is no evidence that the word is in Chinese use at all') and concludes 'the probability is that Vasco and his followers got the tufão, which our sailors made into touffon and then into [typhoon]'; the Introduction lists typhoon among words 'ascribed to a Chinese origin … [that] are not Chinese at all'.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1990\", \"stance\": \"partial\", \"note\": \"\\\"Chin. t'ai-fung … hieraus … engl. typhoon, dtsch. Taifun, Teifun; frz. typhon. Erst über ar. ṭūfān 'heftiger Sturm' entstand pg. tufão, tofano.\\\" — Chinese for English, Arabic for Portuguese.\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.v. typhoon (web archive)\", \"stance\": \"supports\", \"note\": \"\\\"It apparently is from tufan, a word in Arabic, Persian, and Hindi meaning 'big cyclonic storm' … 'the probability is that Vasco and his followers got the tufao … direct from the Arab pilots' … Chinese (Cantonese) tai fung 'a great wind' also might have influenced the form or sense.\\\"\"}\n ]\n})\n\nnodes.append({\n \"id\": 15, \"lang\": \"Latin\", \"words\": \"fŭmus\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin fūmus 'smoke, steam, fume' < PIE *dʰuh₂-mos, the m-formation of the root: word-initial PIE *dʰ- gives Latin f-, and the laryngeal-coloured *-uh₂- gives ū. The equation is one of the oldest and safest in Indo-European: Skt. dhūmá- 'smoke' (= Lat. fūmus exactly, and the denominative dhūmāyati = Lat. fūmāre), Lith. dūmai (pl.), Old Prussian dumis, OCS dymŭ, Gk. θυμός 'spirit, passion' (semantically 'the smoke that rises in one'). Pokorny p. 262 and Walde-Pokorny I 835 print the whole set; Watkins/AHD dheu-1 §1a: 'Suffixed extended zero-grade form *dhū-mo- … smoke, in a. Latin fumus'.\",\n \"derivation_fa\": \"لاتینِ fūmus «دود، بخار» از ‎*dʰuh₂-mos‎ هندواروپایی است، یعنی ساختِ ‎-mo-‎ همین ریشه: ‎*dʰ-‎ آغازین در لاتین f می‌شود و ‎*-uh₂-‎ به ū بدل می‌گردد. این برابری از کهن‌ترین و مطمئن‌ترین برابری‌های هندواروپایی است: سنسکریتِ dhūmá- «دود» (دقیقاً برابرِ fūmus، و فعلِ dhūmāyati برابرِ fūmāre)، لیتوانیاییِ dūmai، پروسیِ باستان dumis، اسلاویِ کهنِ کلیسایی dymŭ و یونانیِ θυμός «جان، خشم» (از «دودی که در آدمی برمی‌خیزد»). پوکورنی (ص ۲۶۲)، والده-پوکورنی (ج ۱ ص ۸۳۵) و واتکینز همگی همین را می‌آورند. ادعای نورایی درست است.\",\n \"sources\": [S[\"dhumos\"], S[\"fume\"]],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985, dheu-1 §1: \\\"Suffixed extended zero-grade form *dhū-mo- (<*dhuə-mo-), smoke, in: a. Latin fumus, smoke: FUMAROLE, FUMATORIUM, FUMATORY, FUME; FUMARIC ACID, FUMIGATE, FUMITORY, PERFUME.\\\"\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p. 262 (POK_01 leaf 273)\", \"stance\": \"supports\", \"note\": \"\\\"Ai. dhūmá-ḥ m. 'Rauch, Dampf', dhūmāyati 'raucht, dampft' = lat. fūmāre … lat. fūmus 'Rauch, Dampf, Qualm, Brodem' … lit. dūmai Pl. 'Rauch' … aksl. dymъ 'Rauch'.\\\"\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 835 f.\", \"stance\": \"supports\", \"note\": \"the same equation, headed 'Mit m-Formantien: Ai. dhūma- m. \\\"Rauch, Dampf\\\" … lat. fūmus \\\"Rauch, Dampf, Qualm, Brodem\\\"'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, dhūmos (IEC.txt l. 3296, p. ~221)\", \"stance\": \"supports\", \"note\": \"\\\"dhūmos 'smoke, vapour, fog, spirit, breath'. WP I, 835 … Skt. dhūmáḥ … Gk. thūmós … Lat. fūmus; OCS dymŭ; Li. dúmas & (pl.) dūmai.\\\"\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 1.83 SMOKE, p. 73\", \"stance\": \"supports\", \"note\": \"the SMOKE table lists Lat. fumus beside Lith. dūmai, Lett. dūmi, ChSl. dymŭ, SCr. dim, Pol. dym, Skt. dhūma-.\"}\n ]\n})\n\nnodes.append({\n \"id\": 16, \"lang\": \"English\", \"words\": \"fume, perfume\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle English fume (late 14th c.) is borrowed from Old French fum 'smoke' and the verb fumer, from Latin fūmus / fūmāre; the sense 'angry excitement' ('in a fume') is a metaphor of the same kind as Greek θυμός. Perfume comes into English in the 1530s from Middle French parfum / parfumer, itself from Old Provençal or Italian perfumare 'to fill with smoke' (per 'through' + fumare 'to smoke'): the word originally denoted the smoke of burning incense used to fumigate a room, and only then the pleasant smell itself and the liquid that carries it. Watkins/AHD lists both FUME and PERFUME under dheu-1 §1a, and the index confirms 'PERFUME dheu-1'.\",\n \"derivation_fa\": \"واژهٔ انگلیسیِ fume در اواخر سدهٔ چهاردهم از فرانسهٔ کهن (fum «دود» و فعلِ fumer) وام گرفته شده و آن از لاتینِ fūmus / fūmāre است؛ معنیِ «برآشفتگی» («in a fume») همان استعاره‌ای است که در θυμός یونانی دیده می‌شود. perfume در دههٔ ۱۵۳۰ م از فرانسهٔ میانه parfum/parfumer آمده و آن از ایتالیاییِ perfumare «پر از دود کردن» (per «سرتاسر» + fumare «دود کردن») است: نخست به دودِ عودی می‌گفتند که اتاق را با آن بخور می‌دادند و سپس به خودِ بویِ خوش و مایعِ آن. واتکینز هر دو را ذیلِ ‎dheu-1‎ می‌آورد. ادعای نورایی درست است.\",\n \"sources\": [S[\"fume\"], S[\"dheu\"]],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the book; its parent Latin box cites AHD.\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 dheu-1 §1a and the index (l. 2079 'PERFUME dheu-1', l. 1544 'FUME dheu-1')\", \"stance\": \"supports\", \"note\": \"both English words are credited to the Latin fumus branch of this root.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. stew / fume\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt l. 36774 refers *tufare 'to heat' to Gk. τῦφος and 'L. fumus, \\\"smoke\\\". See typhus' — Klein keeps fumus and typhus in one family.\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.v. fume (web archive)\", \"stance\": \"supports\", \"note\": \"gives the Old French fum < Latin fumus route and the *dheu- (1) root.\"}\n ]\n})\n\nnodes.append({\n \"id\": 17, \"lang\": \"Germanic\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Empty pass-through box standing for the Proto-Germanic continuations of the root that Watkins/AHD collects under dheu-1: *dus- (whence OE dysig 'foolish'), *deuzam 'breathing creature' (OE dēor), *duns-to- 'dust, meal' (OE dūst), and, from the bh- and w-extensions, *daubaz 'deaf' (OE dēaf), *dumbaz (OE dumb), *dūbōn 'dark-coloured bird' (OE *dūfe) and *dulaz (OE dol). Walde-Pokorny I, under '3. bh-Erw. dheubh-', prints the same Germanic set: 'Got. daufs (-b-) \\\"taub, verstockt\\\" … got. (hraiwa-)dūbō, anord. dúfa, ags. dūfe, ahd. tūba \\\"Taube\\\" (nach der dunkeln Farbe) … Nasaliert got. dumbs, anord. dumbr, ags. dumb'. Nourai's 'Germanic' box therefore has real content even though it is printed empty.\",\n \"derivation_fa\": \"این جعبهٔ خالی نمایندهٔ دنباله‌های ژرمنیِ آغازینِ همین ریشه است که واتکینز ذیلِ ‎dheu-1‎ گرد آورده: ‎*dus-‎ (انگلیسیِ کهن dysig «نادان»)، ‎*deuzam‎ «جاندارِ نفس‌کش» (dēor)، ‎*duns-to-‎ «گرد و غبار» (dūst) و از گسترش‌های ‎-bh-‎ و ‎-w-‎: ‎*daubaz‎ «کر» (dēaf)، ‎*dumbaz‎ (dumb)، ‎*dūbōn‎ «پرندهٔ تیره‌رنگ» (*dūfe) و ‎*dulaz‎ (dol). والده-پوکورنی نیز ذیلِ «گسترشِ ‎bh-‎: dheubh-» همین مجموعهٔ ژرمنی را می‌آورد. پس جعبهٔ خالیِ «ژرمنی» در واقع محتوایی روشن دارد و ادعای نورایی درست است.\",\n \"sources\": [S[\"dheu\"]],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 dheu-1 §§3, 4, 6, 11, 12 set up exactly these Germanic forms (*dus-, *deuzam, *duns-to-, *daubaz, *dumbaz, *dūbōn, *dulaz).\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I, '3. bh-Erw. dheubh-'\", \"stance\": \"supports\", \"note\": \"\\\"Got. daufs (-b-) 'taub, verstockt', anord. daufr, ags. dēaf … got. (hraiwa-)dūbō, anord. dúfa, ags. dūfe, ahd. tūba 'Taube' (nach der dunkeln Farbe) … Nasaliert got. dumbs, anord. dumbr, ags. dumb.\\\"\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. thio- (KLN_1966.txt l. 39044)\", \"stance\": \"supports\", \"note\": \"Klein refers 'deaf and words there referred to, and dull … deer, dizzy, down … dust … fume' all to base *dheu-.\"}\n ]\n})\n\nnodes.append({\n \"id\": 18, \"lang\": \"English\", \"words\": \"dizzy, deaf, dumb, dull, deer, dust, dove\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Each of the seven is credited to this root by Watkins/AHD dheu-1: dizzy < OE dysig 'foolish' (Gmc *dus- < extended *dheus-, 'stupefied, confused'); deer < OE dēor 'animal' (Gmc *deuzam < *dheus-o- 'breathing creature'); dust < OE dūst (Gmc *duns-to- < nasalized *dhwens-); deaf < OE dēaf (Gmc *daubaz < *dhoubh-o- 'beclouded in the senses'); dumb < OE dumb (Gmc *dumbaz < nasalized *dhu-m-bho-); dove < OE *dūfe (Gmc *dūbōn, 'dark-coloured bird'); dull < OE dol / MLG dul (Gmc *dulaz < *dhwel-). The unifying idea — 'rise in a cloud, becloud, hence dull of colour, sense or wit' — is Pokorny's and Walde-Pokorny's as well, and the chart's own root gloss ('smoke, mist, dizziness, dull color') states it exactly. The one thing to keep in mind is that the group is held together by a semantic principle rather than by a single formation, and that individual members (dove, deer) have been explained otherwise by other scholars.\",\n \"derivation_fa\": \"هر هفت واژه را واتکینز در پیوستِ AHD ذیلِ ‎dheu-1‎ می‌آورد: dizzy از انگلیسیِ کهن dysig «نادان» (ژرمنی ‎*dus-‎ از گسترشِ ‎*dheus-‎)؛ deer از dēor «جانور» (‎*deuzam‎ از ‎*dheus-o-‎ «جانِ دم‌زننده»)؛ dust از dūst (‎*duns-to-‎ از صورتِ خیشومی‌شدهٔ ‎*dhwens-‎)؛ deaf از dēaf (‎*daubaz‎ از ‎*dhoubh-o-‎ «تیره‌شده در حواس»)؛ dumb از dumb (‎*dumbaz‎ از ‎*dhu-m-bho-‎)؛ dove از ‎*dūfe‎ (‎*dūbōn‎ «پرندهٔ تیره‌رنگ»)؛ و dull از dol (‎*dulaz‎ از ‎*dhwel-‎). اندیشهٔ پیوند‌دهنده — «برخاستنِ گرد و دود، تیره شدن، و از آن‌جا کندیِ رنگ و حس و هوش» — همان است که پوکورنی و والده-پوکورنی دارند و در معنیِ ریشه در خودِ چارت («دود، مه، گیجی، رنگِ کدر») بازتاب یافته است. تنها باید به یاد داشت که این خوشه را اصلی معنایی به‌هم بسته است نه یک ساختِ واحد، و برخی اعضا (dove، deer) اشتقاق‌های دیگری هم یافته‌اند.\",\n \"sources\": [S[\"dheu\"]],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the book; its parent Germanic box cites AHD, which covers every word listed.\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 dheu-1 §§3a (DIZZY), 4a (DEER), 6a (DUST), 11a (DEAF), 11b (DUMB), 11c (DOVE), 12b (DULL)\", \"stance\": \"supports\", \"note\": \"\\\"a. Old English dysig, foolish (< 'stupefied,' 'confused'): DIZZY … *deuzam, breathing creature, animal, in a. Old English dēor, animal: DEER … *duns-to- in Old English dūst, dust: DUST … *dhoubh-o- … Old English dēaf, deaf: DEAF; b. nasalized form *dhu-m-bho- … dumb; c. Germanic *dūbōn in Old English *dūfe, dove (< 'dark-colored bird'): DOVE … *dulaz in Old English dol, dull.\\\" The AHD index likewise gives 'DULL dheu-1', 'DUMB dheu-1', 'DUST dheu-1', 'DOVE1 dheu-1'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I, dheubh- section\", \"stance\": \"supports\", \"note\": \"same Germanic list (daufs, dūbō, dumbs) under the bh-extension; the colour adjectives ('rauchfarben, nebelgrau, düster') stand under the main root.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. thio-\", \"stance\": \"supports\", \"note\": \"\\\"Cp. also deaf and words there referred to, and dull, and words there referred to. Cp. also deer, dizzy, down, 'soft plumage', down, 'hill', dust …\\\" — Klein groups the same English words under *dheu-.\"}\n ]\n})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Dheu 2, Dhu, Dhu-bh\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *dʰeu- / *dʰeuh₂- 'to rise in a cloud (dust, smoke, vapour); to blow, breathe', with the bh-extension *dʰeubʰ- 'to becloud, darken (also of the senses)' and the noun *dʰuh₂-mos 'smoke'\",\n \"note\": \"Pokorny's '4. dheu-, dheuə- \\\"stieben, wirbeln, bes. von Staub, Rauch, Dampf; wehen, blasen, Hauch, Atem; daher dampfen, ausdünsten, riechen, stinken; … Nominalbildungen: dhū-li-, dhū-mo-\\\"' runs IEW pp. 261-267, so Nourai's POK:262 is a page inside the entry, and it is the right page: it carries the m-formations (Skt. dhūmá-, Lat. fūmus), the colour adjectives ('rauchfarben, nebelgrau, düster' — the chart's 'dull color'), the Middle Persian dūt 'Rauch' and the Avestan dvaidi. The three-part heading 'Dheu 2, Dhu, Dhu-bh' matches Walde-Pokorny's arrangement (full grade, zero grade, and the bh-extension dheubh-) and Watkins' dheu-1, whose gloss — 'the base of a wide variety of derivatives meaning \\\"to rise in a cloud\\\", as dust, vapor, or smoke, and related to semantic notions of breath, various color adjectives, and forms denoting defective perception or wits' — is virtually a paraphrase of the chart's 'smoke, mist, dizziness, dull color'. Root, language label and gloss are all correct. Two of the chart's arrows fail, both on the Iranian side: the Avestan box 'dvaidi 1 : smoke' (node 1), which turns Pokorny's Middle Persian dūt into a non-existent Avestan noun, and the andūh branch (nodes 5-6), which follows Moʿin's footnote in Borhān-e Qāṭeʿ p. 172 in deriving اندوه from *han-davaθa- 'pressed together' when Cheung 400 shows it to be *ham-θuaxš- 'to be preoccupied'. On the Semitic side the Greek origin of Arabic ṭūfān (node 12) is a minority view that Jeffery expressly rejects.\",\n \"note_fa\": \"ریشهٔ هندواروپاییِ ‎*dʰeu-/*dʰeuh₂-‎ «چون ابر برخاستن (گرد، دود، بخار)؛ وزیدن، دمیدن» با گسترشِ ‎*dʰeubʰ-‎ «تیره و مه‌آلود کردن (حتی در حواس)» و نامِ ‎*dʰuh₂-mos‎ «دود». مدخلِ «۴. dheu-» در فرهنگِ پوکورنی از ص ۲۶۱ تا ۲۶۷ کشیده است، پس ارجاعِ نورایی به ص ۲۶۲ درونِ همان مدخل و درست است: در همان صفحه ساخت‌های ‎-m-‎ (سنسکریتِ dhūmá-، لاتینِ fūmus)، صفت‌های رنگ («دودی‌رنگ، خاکستریِ مه‌آلود، تیره» = همان «رنگِ کدرِ» چارت)، فارسی میانهٔ dūt «دود» و صورتِ اوستاییِ dvaidi آمده‌اند. سه‌بخشیِ عنوان («Dheu 2, Dhu, Dhu-bh») با آرایشِ والده-پوکورنی (درجهٔ کامل، درجهٔ صفر، و گسترشِ dheubh-) و با ‎dheu-1‎ واتکینز می‌خواند و معنیِ آن‌ها تقریباً همان «دود، مه، گیجی، رنگِ کدر» است. ریشه، برچسبِ زبان و معنی هر سه درست‌اند. اما دو پیکان لغزیده است، هر دو در بخشِ ایرانی: جعبهٔ اوستاییِ «dvaidi 1 : دود» (گرهِ ۱) که واژهٔ فارسی‌میانهٔ dūt را به اوستایی برده، و شاخهٔ «اندوه» (گره‌های ۵ و ۶) که به پیروی از حاشیهٔ معین بر برهان قاطع (ص ۱۷۲) آن را از ‎*han-davaθa-‎ «فشرده» می‌گیرد، حال آن‌که چونگ (ص ۴۰۰) نشان داده از ‎*ham-θuaxš-‎ «گرفتارِ کار/خاطر بودن» است. در بخشِ سامی نیز یونانی‌دانستنِ خاستگاهِ «طوفانِ» عربی (گرهِ ۱۲) نظری اقلیّتی است که جفری صریحاً ردش می‌کند.\",\n \"sources\": [S[\"dheu\"], S[\"dhumos\"], S[\"typhus\"], S[\"typhoon\"]],\n \"ref_check\": [\n   {\"ref\": \"POK:262\", \"status\": \"supports\", \"note\": \"POK_01.txt leaves 272-274 (printed pp. 261-263) carry '4. dheu-, dheuə- (vermutlich: dhue-, vgl. die Erw. dhue-k-, dhā-s-) \\\"stieben, wirbeln, bes. von Staub, Rauch, Dampf; wehen, blasen, Hauch, Atem; daher dampfen, ausdünsten, riechen, stinken; stürmen …\\\"; Nominalbildungen: dhū-li-, dhū-mo-'. Page 262 itself has 'lat. fūmus', 'Farbenadjektive der Bed. \\\"rauchfarben, nebelgrau, düster\\\"', 'mpers. dūt \\\"Rauch\\\"' and 'av. dvaidi'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 835 ff. (dheu-, dheuə-) and the section '3. bh-Erw. dheubh-'\", \"stance\": \"supports\", \"note\": \"the same root with the same gloss, and the bh-extension explicitly glossed 'stieben, rauchen; nebelig, verdunkelt, auch vom Geist und den Sinnen' — Nourai's 'Dhu-bh'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, dheu-1 [Pok. 4. dheu- 261]\", \"stance\": \"supports\", \"note\": \"\\\"dheu-1. Also dheuə-. The base of a wide variety of derivatives meaning 'to rise in a cloud,' as dust, vapor, or smoke, and related to semantic notions of breath, various color adjectives, and forms denoting defective perception or wits.\\\"\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, dhūmos (p. ~221) and dhubh- (2)\", \"stance\": \"partial\", \"note\": \"Mann has the 'smoke' root (dhūmos, citing WP I 835) but files the Greek τύφος/τυφλός words under separate dhubh- entries rather than as an extension of it.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 1.83 SMOKE (p. 73)\", \"stance\": \"supports\", \"note\": \"the SMOKE table gathers Lat. fumus, Lith. dūmai, ChSl. dymŭ, Skt. dhūma- — the *dʰuh₂-mos family — under one heading.\"}\n ],\n \"nodes\": nodes,\n}\n\nout = {\n \"pdf_page\": 130,\n \"book_page\": 100,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [entry],\n}\n\np = \"data/verification/page-130.json\"\nwith io.open(p, \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"wrote\", p, len(nodes), \"nodes\")\nPYEOF\npython3 -m json.tool data/verification/page-130.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 130"
}
```


### [2026-09-05T20:24:10.066Z] TOOL RESULT

```
wrote data/verification/page-130.json 18 nodes
JSON OK
nodes verified: 18/18
node verdicts: {'disputed': 4, 'confirmed': 9, 'plausible': 5}
root verdicts: {'confirmed': 1}
ref checks: {'contradicts': 3, 'supports': 14, 'partial': 3, 'not_checked': 4}
books consulted: {'contradicts': 5, 'silent': 4, 'supports': 31, 'partial': 8} | by book: {'KLN': 7, 'WLD': 6, 'WEB': 6, 'AHD': 3, 'PHD': 3, 'NYB': 3, 'CHEUNG': 3, 'MON': 3, 'HJB': 3, 'BRT': 2, 'IEC': 2, 'LKT': 2, 'HUB': 1, 'BQT': 1, 'FVQ': 1, 'POK': 1, 'SYN': 1}
```


## [2026-09-05T20:24:19.702Z] TOOL CALL #57: Bash

```json
{
 "command": "python3 - <<'PY'\nimport json,io\np=\"data/verification/page-130.json\"\nd=json.load(open(p))\nn=0\ndef fix(lst):\n    global n\n    for c in lst or []:\n        if c.get(\"src\")==\"WEB\":\n            c[\"src\"]=\"ETYMONLINE\"; n+=1\ne=d[\"entries\"][0]\nfix(e.get(\"consulted\"))\nfor nd in e[\"nodes\"]: fix(nd.get(\"consulted\"))\nwith io.open(p,\"w\",encoding=\"utf-8\") as f:\n    json.dump(d,f,ensure_ascii=False,indent=2); f.write(\"\\n\")\nprint(\"renamed\",n)\nPY\npython3 tools/verify_check.py 130 | head -8"
}
```


### [2026-09-05T20:25:30.100Z] TOOL RESULT

```
renamed 6
nodes verified: 18/18
node verdicts: {'disputed': 4, 'confirmed': 9, 'plausible': 5}
root verdicts: {'confirmed': 1}
ref checks: {'contradicts': 3, 'supports': 14, 'partial': 3, 'not_checked': 4}
books consulted: {'contradicts': 5, 'silent': 4, 'supports': 31, 'partial': 8} | by book: {'KLN': 7, 'WLD': 6, 'ETYMONLINE': 6, 'AHD': 3, 'PHD': 3, 'NYB': 3, 'CHEUNG': 3, 'MON': 3, 'HJB': 3, 'BRT': 2, 'IEC': 2, 'LKT': 2, 'HUB': 1, 'BQT': 1, 'FVQ': 1, 'POK': 1, 'SYN': 1}
```


## [2026-09-05T20:25:49.840Z] AGENT

Page 130 (book p. 100), one entry, root **Dheu 2, Dhu, Dhu-bh** — verified, `verify_check.py 130` shows 0 PROBLEM lines.

**Counts:** root `confirmed`; nodes 18/18 — 9 confirmed, 5 plausible, 4 disputed. Ref checks: 14 supports / 3 partial / 3 contradicts / 4 not_checked (empty boxes).

**Disputed / problem arrows**
- **#1 Avestan "dvaidi 1 : smoke"** — no such Avestan noun. Pokorny 262 gives the "smoke" word as *Middle Persian dūt*, and `av. dvaidi` there is glossed "wir beide bedrängen?"; Bartholomae 688 has it only as 1du.mid. of `dav-` "press". Nourai split one form into two homonyms. The arrow root → Pahlavi dūd would be right with this box deleted.
- **#5 Avestan "han-davathe"** — unattested; it is Moʿin's *reconstruction* in the Borhān-e Qāṭeʿ footnote on p. 172 (read from the page image, saved to `sources/refs/ocr/BQT/172.vision.txt`), not a lemma. Bartholomae has no `han-dav-` compound.
- **#6 Persian اندوه / اندوهگین** — word and MP handōh are right, route is not: Cheung 2007 p. 400 puts it under *ham- + *θuaxš- "to be busy/burdened" (MMP ʾndwx-, Sogd. ʾntwxs-, Chor. ʾndyx), which the -xš- makes decisive.
- **#12 Arabic ṭūfān ← Greek τυφῶν** — Jeffery, *Foreign Vocabulary of the Qurʾān* 207-208: from Aramaic/Syriac ṭawpānā, and in his footnote "It can hardly be connected, however, with the Gk. τυφῶν." Klein does say what Nourai reports, but it is a minority view.

**Also worth noting:** #14 English *typhoon* is `plausible`, not wrong — Yule/Etymonline support the Arabic route for the sense (Port. tufão, 1588 "Touffon") while Klein/Skeat/Lokotsch make the form Chinese; Nourai's own NOTE reports Klein correctly. Nourai's `SKT:581` contradicts the arrow (Skeat says Chinese, no Arabic) and the entry sits at printed p. ~537 in the 1911 Concise edition, so his page number belongs to another printing.

**Extraction errors:** none. I rendered PDF p. 130 (copied to `sources/refs/ocr/BOOK/130.png`) and the JSON matches the printed chart everywhere, including the odd "dvaidi 1 : smoke" — that is Nourai's own mistake, not a misread.

Eight web pages archived via `fetch_source.py` (Wiktionary دود/اندوه/طوفان/*dʰuh₂mós, Etymonline typhoon/typhus/fume/*dheu-).
