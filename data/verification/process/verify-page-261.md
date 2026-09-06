# Verification process log — verify-page-261


## [2026-09-06T20:32:45.334Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 261 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-261.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-261.json. Write /home/sfmqrb/git/rishe/data/verification/page-261.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 261` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T20:32:46.980Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T20:32:47.706Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T20:32:47.733Z] TOOL RESULT

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


## [2026-09-06T20:32:47.889Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-261.txt"
}
```


### [2026-09-06T20:32:47.921Z] TOOL RESULT

```
1	=== PDF page 261 (book page 231) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kes 1, Kas 1 : to cut  (refs POK:586)
4	#1 (parent #0) [Latin] refs=AHD | castrum, castellum : an "isolated" fortified place, camp, castle ; castrare : to cut
5	  #2 (parent #1) [Arabic] refs=KLN:45 | al-qasr : castle
6	    #3 (parent #2) [Persian] refs=MON:2682 | qasr «قصر» : castle
7	  #4 (parent #1) [French] refs=AHD | chateau
8	    #5 (parent #4) [English] refs=None | chateau, castle
9	  #6 (parent #1) [English] refs=AHD | castrate, chastity
10	--- entry 1 ---
11	ROOT [Indo-European] Kes 2, Qseu : to scratch  (refs POK:585; WLD1:449)
12	#1 (parent #0) [Avestan] refs=POK:585; KNT:175 | hu-xšnuta, hu-šnŭta : well polished, pleasant, happy ☞Su 1 ; xšnâvaya : to satisfy
13	  #2 (parent #1) [Persian] refs=HRN:113; BQT:755; FFD:52 | xošnŭd «خشنود» : happy | extra: خوشیدن ، خوش
14	  #3 (parent #1) [Sogdian] refs=SOD:83 | `xšn`w : to satisfy
15	#4 (parent #0) [Greek] refs=POK:587; IEC:572 | ksniô : to scratch, comb ; kseô : rake
16	  #5 (parent #4) [Pahlavi] refs=HRN:170 | šânak : comb
17	    #6 (parent #5) [Persian] refs=BQT:1230 | šâneh «شانه ۱» : comb
18	  #7 (parent #4) [English] refs=KLN:1758 | xyster : bone scraper
19	#8 (parent #0) [Persian] refs=POK:585; BQT:1307 | šŭr «شور (شوره)» : with sharp taste, salty ; shŭr-bâ «شوربا» : a salty soup ☞Pekw
20	#9 (parent #0) [Persian] refs=IEC:572 | xasîdan «خسیدن ؟» : to chew | NOTE: This word was not found in MON.
21	
```


## [2026-09-06T20:32:51.379Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-261.json && echo \"=== MATRIX ===\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source JSON and source matrix"
}
```


### [2026-09-06T20:32:51.439Z] TOOL RESULT

```
{
  "pdf_page": 261,
  "book_page": 231,
  "entries": [
    {
      "root": {
        "name": "Kes 1, Kas 1",
        "lang": "Indo-European",
        "refs": "POK:586",
        "gloss": "to cut"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "castrum, castellum", "gloss": "an \"isolated\" fortified place, camp, castle", "script": null},
            {"translit": "castrare", "gloss": "to cut", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "KLN:45",
          "words": [
            {"translit": "al-qasr", "gloss": "castle", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:2682",
          "words": [
            {"translit": "qasr", "gloss": "castle", "script": "قصر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {"translit": "chateau", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "chateau, castle", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 1,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "castrate, chastity", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kes 2, Qseu",
        "lang": "Indo-European",
        "refs": "POK:585; WLD1:449",
        "gloss": "to scratch"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:585; KNT:175",
          "words": [
            {"translit": "hu-xšnuta, hu-šnŭta", "gloss": "well polished, pleasant, happy", "script": null, "see": ["Su 1"]},
            {"translit": "xšnâvaya", "gloss": "to satisfy", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:113; BQT:755; FFD:52",
          "words": [
            {"translit": "xošnŭd", "gloss": "happy", "script": "خشنود"}
          ],
          "script_extra": "خوشیدن ، خوش",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:83",
          "words": [
            {"translit": "`xšn`w", "gloss": "to satisfy", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:587; IEC:572",
          "words": [
            {"translit": "ksniô", "gloss": "to scratch, comb", "script": null},
            {"translit": "kseô", "gloss": "rake", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Pahlavi",
          "refs": "HRN:170",
          "words": [
            {"translit": "šânak", "gloss": "comb", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT:1230",
          "words": [
            {"translit": "šâneh", "gloss": "comb", "script": "شانه ۱"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:1758",
          "words": [
            {"translit": "xyster", "gloss": "bone scraper", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Persian",
          "refs": "POK:585; BQT:1307",
          "words": [
            {"translit": "šŭr", "gloss": "with sharp taste, salty", "script": "شور (شوره)"},
            {"translit": "shŭr-bâ", "gloss": "a salty soup", "script": "شوربا", "see": ["Pekw"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "گر برای شوربایی بر در اینها روی - اوّلت سِکبا دهند از چهره آنگه شوربا", "poet": "Khâqânî"}
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:572",
          "words": [
            {"translit": "xasîdan", "gloss": "to chew", "script": "خسیدن ؟"}
          ],
          "script_extra": null,
          "note": "This word was not found in MON.",
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


## [2026-09-06T20:33:33.798Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','AHD','KLN','HRN','BQT','SOD','IEC','KNT','MON','FFD','PHD','BRT','ARY','SKT','LEW','LAT','SYN','HUB','NYB','FVQ','AFM','PLA','LKT','CHEUNG','RCH']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print('==',k, json.dumps({kk:v[kk] for kk in v if kk in ('kind','url','lookup_hint','local_file','page_offset','scans','note','title')}, ensure_ascii=False)[:700])\n\""
}
```


### [2026-09-06T20:33:35.916Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful fo
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf", "/
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 4
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers sho
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/ref
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictiona
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_h
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags."}
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal."}
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Latin headword in bold at line start fol
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. 
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number."}
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "lookup_hint": "HathiTrust search-only; Google 
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number."}
CHEUNG MISSING
== RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 = p.242, leaf 587 = p.494); weakly detected, verify by grepping the page number. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are Persian/Arabic in script (poorly OCRed) followed by transliteration and English glo
```


## [2026-09-06T20:33:41.728Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_full.txt; do echo \"### $f: $(grep -c '' $f) lines, $(grep -c $'\\f' $f) ff\"; done\necho \"--- grep kes- headwords\"\ngrep -n -E '^\\s*[0-9]?\\.?\\s?(kes|kseu|kes-|keu-s)' POK_full.txt | head -40"
}
```


### [2026-09-06T20:33:43.694Z] TOOL RESULT

```
### POK_01.txt: 5152 lines, 352 ff
### POK_02.txt: 6716 lines, 420 ff
### POK_full.txt: 93771 lines, 0 ff
--- grep kes- headwords
34175:kese^ molar tooth ', Middle Low German kuse, mnl. kuze, changing through ablaut mnl. 
44451:kes-). 
46721:keu-s-\r\ russ. dial, cuchatb 'percewe, hear', sloven, cuha-m, -//"feel, foresee, predict ',
```


## [2026-09-06T20:33:48.091Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 241 242 243 244; do echo \"=========== POK_02 leaf $n (printed p.$((n+344)))\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((n+1))\"'' POK_02.txt | head -80; done"
}
```


### [2026-09-06T20:33:49.817Z] TOOL RESULT

```
=========== POK_02 leaf 241 (printed p.585)
e,  verbinde,  gleiche  aus',  jünger  y^iqv&o)^  xegdw,  yiegaloj^ att.  TisQdvvv^iL,  Fut.  yisgaaco,  att.  yiSQw,  Aor.  iy.eQao(G)a,  ion.  iTTL^iQTJaaLj  Perf. xsTtgä^at,  ä-xQarog  ( :  ai.  slrtd-)  ,ungemischt,  rein ;  sich  in  ungehemmter Kraft  äußernd,  unbändig'  {*k,rd-tös)'j  Kgaaig  f.  ,MischuDg',  y-gazi^Q  , Misch- krug'; hom.  äy,r]Qarog  in  der  Bed.  ,rein  (Wasser)',  metr.  Dehnung  für *dy£Qarog(?)  i  ^•
anord.  hrära,  ags.  hreran,  ahd.  {h)ruoren  ,in  Bewegung  setzen,  rücken," rühren^,  as.  hröra  ,Bewegung,  Aufruhr',  ahd.  ruora  ,Bewegung  (auch  im Leibe:  nhd.  Ruhr)',  ags.  as.  hrör  ,rührig,  stark',  ags.  krer  (engl,  rear)  ,halb gekocht'.
WP.  I  419  f.,  Schwyzer  Gr.  Gr.  I  695,  697,  Risch  Wortbildung  227.
kerm-  , ermüden,  rasten,  schlafen'?
Ahd.  mhd.  hirmen,  mndl.  hermen   , ruhen,  rasten';  lit.  kirmy-jü,  Jcirmyti, hirmUi  ,anfaulen,  faul  werden'  (beeinflußt  von  hirmis  ,Wurm'?). WP.  I  426.
kerno-  , Kinnbacken' ;  nur  kelt.  und  slav. ;  vgl.  2.  her-.
Cymr.  cern  , Kinnbacken^,  bret.  kern  , Mühltrichter,  Scheitel,  Tonsur', mir.  cern  ,Ecke,  Winkel'  (es  liegt  die  Vorstellung  des  Knicks  am  Kinn- backen vor);
slav.  *cerm  in:  abg.  crenovhnaja  ^^ivlai^  r.-ksl.  crSnovtm  {zuh^),  crenovithct ,^vXr]^  ,dens  molaris',  slovak.  ^ren  , Kinnbacken'  usw.
Nach  Büga  RFV.  67,  234  zu  lett.  c^rwo-Ä;(s)Zzs  ^Backenzahn',  ai.  carvati ,kauen'.
WP.  I  427,  Trautmann  129,  Specht  Idg.  Dekl.  141,  169.
ke-ro-  Farbbezeichnung?
Ai.  särd-  ,bunt,  scheckig',  dessen  -ra-  als  formantisch  erwiesen  wird durch  die  av.  Kompositionsform  *iä-(i)i-  in  säi-mu^ay-  EN  ,der  ungleich- mäßig gefärbte  Eselinnen  hat';
gr.  nrjQvlog  ,der  blaue  ^Eisvogel'  (Deminutivformans  -vXog).
"^ke-ro-  vielleicht  als  *ke[i']-ro-  zu  2.  Icei-  in  , Farbbezeichnungen' ?
WP.  I  420,  WH.  I  133.
583
kers-    und    wohl   auch   bloßes   ker-    in  Worten   für   Farben,    bes.    dunkle, schmutzige;  krs-no-  ^schwarz^;  vgl.  auch  4.  kel-  und  6.  ker-,
Ai.  kj-piä-  , schwarz*  =  apr.  kirsnan  ds.,  FIN  Kirsnappe  =  abg.  Sr^n^, russ.  cerem,  skr.  crn  usw.  , schwarz'  (*chrxm,  *chrsm) ;  ohne  -wo-Formans lit.  kersas  , schwarz  und  weiß  gefleckt',  kerse  , bunte  Kuh',  kerHs  ,schwarz- bunter  Ochse',  kersulis  , Ringeltaube' ;  karsis  
=========== POK_02 leaf 242 (printed p.586)
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
=========== POK_02 leaf 243 (printed p.587)
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
=========== POK_02 leaf 244 (printed p.588)
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


## [2026-09-06T20:34:05.761Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==245' POK_02.txt | tail -30\necho \"==== leaf 246 (p.588-ish)\"\nawk 'BEGIN{RS=\"\\f\"} NR==246' POK_02.txt | head -40"
}
```


### [2026-09-06T20:34:07.735Z] TOOL RESULT

```
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
==== leaf 246 (p.588-ish)
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
```


## [2026-09-06T20:34:28.959Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== IEC ksn\"\ngrep -n -E '^ks(n|e)' IEC.txt | head -30\necho \"===== IEC leaf for p.572 (leaf ~ 572/2+15 = 301)\"\nfor n in 300 301 302; do echo \"--- leaf $n\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((n+1))\"'' IEC.txt | head -5; done"
}
```


### [2026-09-06T20:34:31.111Z] TOOL RESULT

```
===== IEC ksn
8154:kseió ‘tie, bind". Cf. ksetos Skt. khayami ((1) ‘fix’. For (2) ‘strike’, see quseio); Hitt. sxiya(mi), sxai 'tie; gather; pledge’; cf. sxaminan, acc. "cord": OCS šija, ‘neck’; Cz. šíje ‘nape’
8155:kseloksos, kseluqusos, à ‘shell, busk, bark, peeľ. Variant: skel-. Cf. WP II, 591. (Basic formula uncertain) Arm. xayax, o-st. “hide, skin’; Lat. siliqua “shell; pod, husk’; Ir. cf. scilice ‘husking of corn’; R Seluxà ‘peel, husk’; Séluxi, Soluxi, pl. ‘scab, mange’. (Lat. silex ‘flint and Ofr. scelec ‘rock’, Ir. sceilg ‘reef, cliff suggest a parallel phonology, but IE ks- is normally = Ir. c-, cf. ksengið). (Cz. šešule ‘shell, pod, husk’ suggests metathesis)
8156:kseluos ‘bent, crooked, lame’. Cf. skoluos Skt. kharvah, id.; Arm. xey, id.; Per. šal *para- lytic’; Tokh. cf. śālyi, B $walyai “left-handed; Br. (?) welš (for *chwelš? “lame, hemiplegic’; OHG scelah, gs scelawes 'crosseyed'; OE
8160:ksengió (skeng-, skng-) limp, pace, amble’. Cf. WP I, 588 & II, 564 Skt. kháfijami ((limp', fr. *ksen$-); Per. cf. xing ‘white horse’; xinga, adj. ‘able-bodied’; (zero-gde in) xazidan, inf. ‘crawľ (*ksn&-); and in Gk. (variant: *sk-) skázo ‘limp’; MIr. cin- gim ‘go, walk’; 3sg. pf. cechaing; Sw. skinka, inf. ‘limp’; R Sag, m. ‘pace’; Sagàt, Sagnüt, inf. id. Gaul. cf. -cengo-, cing-, Sequanian: -cingos ('gait, path” or sim.)
8163:kserom (?) “fluid? Skt. ksaram (water; Lat. (ambig.) serum ‘whey’ (equates equally with Skt. sáras, n. “fluid, water”. See seros, om)
8165:kseros (2) (quseros ?) “sharp, harsh'. (Same as (1)? The alternative initial is suggested by Gk. psorós (rough?) Skt. khárah, kharuh 'rough, harsh'; Oss. cf. áxsálí ‘Juniper’; Tokh. A tsår, B Scire trough, hard’; R cf. Sero-xovatyj ‘rough, rugged’; Ukr. Sory, pl. ‘barbs’. Long-gde in R o-šaràšiť ‘dumbfound’
8166:kserp- (?) ‘roughness, rough surface’ Lat. cf. (?) sirpus, scirpus ‘rush, mat, fish-
8167:ksengið (skeng-, skng-) — kseubh-
8177:ksesió ‘grind, crush, pound, scrape’. Cf. ksestós. WP I, 450 Per. xasam, -idan ‘chew’; Oss. cf. Kaxín, pp. kaxt (dig. Consonantism?) beside xäst “held; bitten; bite; fight" (variants: *ks-? *qus-?); Gk. kséo, adj. ksestós ‘scrape, rake, polish’; Alb. shesh, pér-shesh, v. ‘crumble; raze; break; level; Cz. cf. šášeň 'shipworm, teredo’. The existence of a doublet in Gk. pséo beside psáo ‘rub down, crumble’ suggests hybridism. Cf. the Ossetic forms above)
8178:ksestós (1) ‘scraped, razed', etc. Cf. ksesió Gk. ksestós; Alb. i sheshét “level, razed'; Srb. cf. po-3Sast, f. ‘epidemic’; R cf. Sàstat' ‘husk (oats); traipse'. (Li. Zemaité šēkštis, m. "wood. en rake’ may represent a variant *kse'stio-)
8179:ksestos (2) “pole, stick’. Cf. kestis & Kestrom and WP IL, 523 Per. (?) šast «archer's thumbstall'; Lat. (?) cf. sestertium ‘pickaxe’; R šest “pole, perch’; Latv. cf. škesta, škestra ‘rod, switch’
8181:ksetros, à, om ‘protection; protector, hold- er’. Cf. WP I, 504 Skt. ksatrám ‘dominion, power’; Av. xSaðro ‘ruler’; -à, f. ‘kingdom’; -om “rule; -is, f. *mis- tress of the house’; OPer. xsaśa- ‘kingdom, kingship’; Oss. äxsar ‘strength’ (LW in Oss. saxár ‘town’, fr. Per.); Per. šahr ‘city’; Hitt. cf. sxassaras ‘mistress of the house’; Olr. cf. cathir, f. (/city', fr. *ksotri-); W (R-gde as Ir.) cadr 'strong'; cader, f. *hill fortress'; cadar, pl. cedyr, f. ‘defence, shield’; OCz. cf. šetřiti ‘watch’; Cz. ‘regard, care for, save’; Slovak šetriť “notice; spare’; Pol. szatrzyc się ‘take care’. The Gk. LW satrápēs represents an Av. form xSaðra-pavan- (Boisacq)
8182:kseubh- “move, sway, stir. Variant of type ksübh-, q. v. Cf. skeubh-, skubh-, qusibh-. (The initial is ambig. in Indo-Iran. & Slav.). WP I, 502 `
8185:kseul- (kseuel-) ‘sway, swerve, totter’. (Ini- tial ambig. in Per. & Latv., W) Per. šūlam, -īdan ‘dote, wander in mind’; šul, adj. ‘silly’; W (ambig.) cuall (‘foolhardy’, fr. *kseyoli-); R cf. ševeliť, inf. intr. ‘stir, move’; Latv. Sauls ‘silly’; Saulis, m. (fooľ: W cuall, pl. cueill ‘madmar’)
8186:kseuos, ios ‘queer, odd, deranged’. Cf. skai- uos, skauios, aseuios, seuios, quseuios. WP II, 537. (Some of the evidence is ambig.) Arm. xev “mad, silly’; Du. cf. schouw *de- praved, wild’; OCS šuj, adj. ‘left-hand’; var- iants in Per. šūx ‘wanton, shameless’; MHG schiech, gs schiehes ‘askew’; cf. adv. schipfes, id.
8191:kseul- (kseuel-) — ksnt-
8205:ksneuo (ksneumi) ‘pierce, stab, be sharp, be keen'. Cf. sneu- Skt. kspaumi ‘sharpen’; Gk. cf. ikshneümon (?) (Cichneumondly,, if for ix, gs ikós ‘grub’ + *ksneu- ‘pierce’); Lat. cf. nov-acula ‘razor’; OE sneowan ‘hasten’; cf. sneome: OS sniumo “quickly”; pp. in Skt. ksnutáh, Av. hu-xinuta-; o-gde in MHG snoede ‘contemptuous’; ON snauór ‘bare; impoverished’
8206:ksn-, variant of ksən-, see ksənio, ksnt- Oss. àxsinin, Dig. äxsinun ‘gnaw; card wool
8207:ksnt- (1) ‘wander, sway, totter’. Cf. Ks- (px.) and nt- Oss. cf. xátin, xätun ‘roan? (fr. *Ksnt-?); OCS Setajo, ati ‘rave, wander in mind, dally’; Big. šètam ‘roam’; Srb. Secem se, šetati se ‘walk’; R šatàťsa, inf. ‘sway’; OCz. Sétiti së “become silly’; R cf. Satkri ‘shaky’; OCS Setavú "Tool. hardy’; Cz. po-šetilý “silly”
8208:ksnt- (2) ‘prickly; prickle, thorn’. Cf. ksonio, ksost-, ksot- Oss. cf. åxsid ‘carded, combed’; Gk. ksánsis, f. ‘carded wool, carding of wool’, beside ksás- ma, n. id.; Lat. sentis, m. ‘briar’; sentus, adj. ‘overgrown, tattered’
===== IEC leaf for p.572 (leaf ~ 572/2+15 = 301)
--- leaf 300
. küokas ‘cudgel’, küoka, id.
koks- (koksos, à; koksios, koKsios) 'flank, side, shank; latera. WP I, 456 Skt. káksah, kaksa “armpit; side, flank’; kač- Chah, à, am, mfn. (“bank, shore’; adj. type); cf. also (variant) ka$yam ‘flank, haunch’; Av. ka$o “shoulder; shore”; Lat. coxa, cossa ‘thigh, hip’; cf. coxim, adv. ‘squatting’; LLat. coxius ‘with a hip disease’; MIr. coss (ffoot, fr. *koKs-, cf. eas, eis fr. *eKs); Ir. cos, pl. cosa “foot, leg, treetrunk'; W coes, f. “leg, shank, beside cesail ‘armpit’; OHG hahsa, G Hachse, Hechse *bend of knee; hamstring'; Sw. has, m. pl. -ar "bock
koksó (1) ‘squeeze, constrain’. Skt. cf. káksyam ‘girdle’ beside (variant) kačā- mi 'bind'; Av. kaš- ‘bind’; Arm. koxem ‘squeeze, mangle, tread’; kox, koxan, s. ‘tread’; Ir. coscaim, coiscim ‘restrain’; cosc (restraint. Consonantism as in Ír. nasc *bond': Lat. nexus)
kokso (2) (kaks- ?) ‘fondle, love” Alb. cf. mé n-gáshet (impers: ‘I fancy"); Pol. kochać ‘love’; Cz. kochat ‘fondle’; cf. roz-ko8, f. ‘delight’ i
kokstis, os, ios “hard, old, withereď’. Cf. (variant) Koktos, kăkstios Skt. kastah ‘harmful’; Arm. košt, Let ((1; ‘hard, coarse’, via *kokitis by induction): Gaul. cotto-; Cor. coth, Br. koz, compar. kosoch, adj. Cold Ambig. cf. Koktos); Du. (ambig.) hecht (/solid, firm’, but cf. VW: EWNT: becht prob. fr. Gmc. *hafti-); OCS ko&tí "lean, slim?
--- leaf 301
n *reach, get, fetch")
327
(kolĝ-, o-gde form of kelĝ-, q. v. in Go. halks “empty, vain, penniless’. For Sw. halka 'stum- ble’; halka, halke ‘slippery track’; Icel. hálka, id. see Supt. K: klg-. Isophonic: OE healc, healoc ‘bend; cavity’: Sw. hálk, s. ‘ring’; hålka ‘hollow out’)
kolKos ‘awn, barb, ear of corn’. Variant: kolsos, q.v. WP I, 434, 435 and II, 592 Mir colc, colg ‘sting, bristle, blade, awn’; Ir. colg, m., cailg, f. id.; cf. cuilc, f. ‘reed’ and (e-gde) cealg ‘sting’; OW cf. colginn, Mod. W colyn, f. ‘sting, pivot’; Cor. colgh, m. ‘point, awn’; OCS (ambig. and com. SI.) klasü ‘barb, awn, ear’; R cf. kolosija “ears of corn’. EMAIb. kall, pl. kallëz ear of corn” represents a type kolsos, q.v.
kolnos, is, us ‘hill’
--- leaf 302
kt. kamala ‘wealth’; MHG hamel ‘boulder’; Li. cf. kamuolys “lump; Latv. kamols ‘ball of
329
thread"
komoros (?) (a plant). Cf. WP I, 390 Skt. kamalah ‘lotus’; Gk. kómaros ‘arbutus’. (Isophone: Latv. kamara “crust, rind’)
komos, us Jump, hump’. Cf. kombos, komo- los. WP I, 388 & 460 Icel. hom, gs hamar “ham, haunch'; R kom Jump’; Srb. kom ‘mash, lees’; Slovene kom “hill, peak’; Latv. kams “lump”, kama ‘clod, pease-pudding’
```


## [2026-09-06T20:34:41.215Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nimport re\ni=t.find(\"ksesió ‘grind\")\nleaf=t.count('\\f',0,i)\nprint(\"leaf(0based)\",leaf)\n# print page numbers near\nseg=t.split('\\f')\nfor n in (leaf-1,leaf,leaf+1):\n    s=seg[n]\n    print(\"---\",n, re.findall(r'^\\s*(\\d{3})\\s*$', s, re.M)[:5])\nprint(seg[leaf][:1500])\nEOF"
}
```


### [2026-09-06T20:34:43.325Z] TOOL RESULT

```
leaf(0based) 325
--- 324 ['570', '511']
--- 325 ['572', '573']
--- 326 ['574']
ng-, Sequanian: -cingos ('gait, path” or sim.)
ksërið (1) ‘dry, parch, wither; turn dry, etc. Cf. kseros (1). WP I, 503 Skt. ksáràmi (2) ‘perish’; Arm. cf. xarem (‘sear, brand”, fr. *ksor-2); Per. cf. xirman “barn, threshing-floor'; Gk. cf. kseraino ‘dry’; Lat. seresco, Gre “dry in the sun; get dry’; Li. Seri- uos, -uotis (^wither', intrans.); Latv. seru, sert *dry (grain) in kiln?
ksérió (2) *ill-use, abuse". Cf. kseros (2) Skt. cf. ksaritah (2) 'abused'; Alb. shorr *squeeze'; Pol. szarzac, inf. “abuse, bully, tor- ment
kserom (?) “fluid? Skt. ksaram (water; Lat. (ambig.) serum ‘whey’ (equates equally with Skt. sáras, n. “fluid, water”. See seros, om)
kséros (1) ‘parched, scorched, arid". WP I, 503. Cf. kserió (1) & next Skt. ksarab ‘caustic’ beside Hindi khar, f. ‘grass’; Per. cf. xirman ‘barn, threshing-floor'; Arm. cf. xar, i-st. (hay, fr. *ksor-?); xaran, i, av ‘burn, cautery, stigma’; Gk. kserón “dry land”; kserós ‘dry’; Lat. cf. seresco ‘get dry’, beside serenus ‘dry, of weather’; Li. cf. Saras, m. ‘dry fodder’ beside šērà, id.; Latv. sers “dried corn’; cf. also sere, seris ‘sandbank’
kseros (2) (quseros ?) “sharp, harsh'. (Same as (1)? The alternative initial is suggested by Gk. psorós (rough?) Skt. khárah, kharuh 'rough, harsh'; Oss. cf. áxsálí ‘Juniper’; Tokh. A tsår, B Scire trough, hard’; R cf. Sero-xovatyj ‘rough, rugged’; Ukr. Sory, pl. ‘barbs’. Long-gde in R o-šaràšiť ‘dumbfound’
kserp- (?) ‘roughness, rough surface’ Lat. cf. (?) sirpus, scirpus ‘rush, mat, fis
```


## [2026-09-06T20:34:50.907Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nseg=t.split('\\f')\nimport re\nfor n in (325,326):\n    for line in seg[n].split('\\n'):\n        if line.strip().startswith(('ksn','ksən','ksneu','kson')):\n            print(n,'|',line[:400])\nEOF"
}
```


### [2026-09-06T20:34:52.616Z] TOOL RESULT

```
326 | ksənő, ið ‘scratch, scrape, dig’. Cf. ksnt-. WP I, 450 Skt. khánami, pp: khatáb ‘dig’; khaníh, f. *dig- ging; mine’; Oss. åxsinin ‘comb’; Gk. ksaíno, fut. ksanó ‘lacerate; card wool’; ksánion ^wool- comb’; long-gde in ksenós “cutting, canal; cf. Lat. sentus ‘overgrown, tattered; nasty”; OCz. (?) chanéti, inf. ‘flatter’. (A variant oc- curs in Skt. kham, n. (1) ‘hole’; Oss. xwm, xwmä ‘plowed field"
326 | ksneuo (ksneumi) ‘pierce, stab, be sharp, be keen'. Cf. sneu- Skt. kspaumi ‘sharpen’; Gk. cf. ikshneümon (?) (Cichneumondly,, if for ix, gs ikós ‘grub’ + *ksneu- ‘pierce’); Lat. cf. nov-acula ‘razor’; OE sneowan ‘hasten’; cf. sneome: OS sniumo “quickly”; pp. in Skt. ksnutáh, Av. hu-xinuta-; o-gde in MHG snoede ‘contemptuous’; ON snauór ‘bare; impoverished’
326 | ksn-, variant of ksən-, see ksənio, ksnt- Oss. àxsinin, Dig. äxsinun ‘gnaw; card wool
326 | ksnt- (1) ‘wander, sway, totter’. Cf. Ks- (px.) and nt- Oss. cf. xátin, xätun ‘roan? (fr. *Ksnt-?); OCS Setajo, ati ‘rave, wander in mind, dally’; Big. šètam ‘roam’; Srb. Secem se, šetati se ‘walk’; R šatàťsa, inf. ‘sway’; OCz. Sétiti së “become silly’; R cf. Satkri ‘shaky’;
```


## [2026-09-06T20:35:00.866Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 191 (p.170)\"; awk 'BEGIN{RS=\"\\f\"} NR==192' HRN.txt\necho \"=== HRN leaf 134 (p.113)\"; awk 'BEGIN{RS=\"\\f\"} NR==135' HRN.txt"
}
```


### [2026-09-06T20:35:02.532Z] TOOL RESULT

```
=== HRN leaf 191 (p.170)
— 170 -
Die Ableitung von np. Mm aus aw. ysäfniya-
(üarniesteter, Et. ir. I, 82, II, 161) ist sehr an-
sprechend, wennschon mir eine Grundform ^/sampHya-
nicht wahrscheinlich ist. Bei einer so starken Con-
traction konnte auch schliesslich der auslautende Nasal
noch in Mitleidenschaft gezogen werden, vergl. np.
Behräm gegenüber Varahrän; g. cum bei Beresine,
II, 24, VIII, 1 ist gewiss erst sekundär wie cübän
statt sübän (No. 776).
769. San 'ihr (Enclit.).
ap. sam (Enclit.) ; phlv. -^dn,
770. sdnzdeh sechzehn'.
aw. /svasjlasa 'sechzehnter ; phlv. säncdahiim ^).
af/. späras ; kurd. LW. säfizdeh,
np. sänzdeh ist durch das ihm vorhergehende pämdeh
beeinflusst.
771. smie 'Kamm'.
Käs. K. yö\sen (?).
phlv. sänak 'Kamm' (AV.); gr. xrf4', icrivinv (Hesych),
indog. he-n (Hübschmann, ZDMG. 44, 560).
bei. sak *Kamm' (445), dagegen LW. sänug 'Pferde-
strieger (866).
772. sah 'König, Herrscher, sähäne, sälü, sähin 'Falke'-).
ap. /ßäyadiya- 'Herrscher; päz. sah (PPGL), ^syäv
aaa, Ksoiiavöad (Agathias 261, 5, 264, 1).
Allgemein entlehnt (meist mit der speciellen Be-
deutung 'Perserkönig), wie auch säht (z. B. oss. d. sai
'Fünfkopekenstück', bei. säht 'Zweiannastück' (256);
dagegen in der Bedeutung *Landstrasse' in skr. säht,
Weber, Monatsber. BAW. 1879, 812).
778. sähensfih 'König der Könige'.
ap. yßäyad iyänäm ysäyadiya *der Könige König',
Vergl. Seite 128 Note 6.
^) * Sähen ^ vorgl. arm. LW. .^aJien.
=== HRN leaf 134 (p.113)
— 113 —
508. x^^> /ß^i ^^'^^ {^' i- X<^s, jüd.-pers.), (Sahn, /^^es^ daneben
äähn.O, AM.: ;kös) gut, schön, fröhlich* etc.").
Käs. x^Sj /öS.
phlv. /^as hezw, yüs (paz. ;^^as); kurd. /ös, v^; af/.
yöi; bei. vas (407); öij'n. ;Kdi^', sar. yS^.
Nöldeke (mündliche Mitteilung) nimmt als Grund-
form *huakSi- an. Dieselbe Anknüpfung des Wortes
bei Fr. Müller, WZKM. 5, 352.
509. yiiisnüdj x^snü zufrieden, fröhlich*.
aw. *huxsnüta' vergl. hu/rnüiti- 'Befriedigung'; phlv.
/iisnüt, /usnütik (AV.).
510. x^"'*^) 'Schwein, :i)5 (Qiss. Dan. S. 388).
aw. hü kehrpa in Ebergestalt'; phlv. /ük (Bund.),
yßköak hezw, /übadak (Payprus, Ilorn ZDMG. 43, 51);
skr. siikard- 'Eber, Schwein*.
kurd. /ü (H.-Sch.); B>fy.xilg; oss. d. t. yiä (310);
bei. hlk, n. hJy (157) ; wa;r. /äg, sar. y^ug,
511. //rn 'Blut', yümn.
aw. vohuni' *Blut'; phlv. yün, yUnömaud,
kurd. ;^("n (ll.-Sch.); af}'. vTne (f. pl.); bei. LW. hün,
hon (162); wa/. vu/c^n, Uyn. vlyTn, sar. va/ln, sangl.
vain,
512. xöl Helm', yöd.
ap. yauda- *Helm*; aw. ayö],yaoda'.
arab. LW. yu^at 'Helm'; Sify.yöl; oss. d. yodäy t. yüd
(302) ; sar. ydtid *Hut, hohe Mütze aus Schaffell'.
513. yi^'ei 'Schweiss .
aw. yya^öa- 'Schweiss' (ZPGl.), vergl. aw. y'^'Tsctt,
ynseu] phlv. yj^ai bezw. y^'ede, vergl. ynst (y. 9 (37),
») Z. B. xöst (I, 117 Vers 962).
*) Np. ves, das ich Mitteilungen, Heft IV, S. 25 No. 6 fälschlich
neben phlv. reh gesetzt habe, lässt sich nicht zu np. '/us stellen, da die
Vertretung von altem sv durch v wohl kurdisch und belucisch aber nicht
neupersisch ist. Nöldeke (mündliche Mitteilung) sieht r^s als Doppel -
form zu ges an, dessen Aussprache durch jüd.-per8. "»;^;j (Is. 10, 12) voll-
stündig sicher gestellt ist.
') Der bei diesem Worte auch Gberlie forte Majliril vokal if^t falsch.
II o !• n , Grundriss d. noiip. Ktymolojrio. S
```


## [2026-09-06T20:35:15.506Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN alcazar / qasr\"\ngrep -n -i 'alcazar' KLN_1966.txt | head\necho \"=== KLN xyster\"\ngrep -n -i 'xyster' KLN_1966.txt | head\necho \"=== KLN castle/castrum\"\ngrep -n -i \"^castle\\|Arab. al-qasr\\|qasr\" KLN_1966.txt | head -20"
}
```


### [2026-09-06T20:35:15.609Z] TOOL RESULT

```
=== KLN alcazar / qasr
2126:alcazar,  n.,  a  castle,  a  palace.  —  Sp.,  fr.  Arab. al-qasr,  ‘the  castle’,  fr.  al-,  ‘the’,  and  L.  castrum, ‘fortified  place,  fort,  castle’.  See  castrameta- tion  and  cp,  castle.
6706:castle,  n.  —  ME.  castel,  fr.  ONF.  castel,  corre¬ sponding  to  OF.  chaste!  (F.  chateau),  fr.  L.  cas¬ tellum,  ‘citadel,  fortress,  stronghold’,  dimin.  of castrum,  ‘fortified  place,  fort,  castle’,  castra (pi.),  ‘camp’.  See  castrametation  and  cp.  alcazar, castellan,  Castilian,  chateau.
6712:castrametation,  n..  the  laying  out  of  a  camp (mil.)  —  F.  castrametation,  fr.  ML.  castrameta- tidnem,  acc.  of  castrametatio,  fr.  L.  eastrametd- tus,  pp.  of  castrametari,  ‘to  pitch  a  camp’,  which is  compounded  of  castra,  'camp',  and  metdri, ‘to  measure,  mete’.  Castra  is  the  plural  of  cas¬ trum,  ‘a  fortified  place,  fort,  castle’,  orig.  ‘that which  has  been  cut  out’,  fr.  *kastrom,  ‘a  cut¬ ting  tool’.  See  next  word  and  cp.  alcazar.  L. metdri  is  rel.  to  metiri,  ‘to  measure’ ;  see  mete, castrate,  tr.  v.,  to  remove  the  testicles  of.  —  L. caslrdtus,  pp.  of  castrare ,  ‘to  cut,  geld’,  fr.  *kas- trom.  ‘a  cutting  tool’;  prob.  cogn.  with  OI. sasati,  sdsti,  ‘cuts’,  sastram,  ‘knife’,  Gk.  xedtsetv, ‘to  split’,  and  perh.  also  with  OSlav.  kosa, ‘sickle’.  L.  castrum,  ‘a  fortified  place’  (in  the  pi. 'camp'),  carere,  ‘to  be  without,  be  wanting,  be free  from,  abstain  from',  castus,  ‘pure,  chaste’, are  prob.  related  to  castrare.  See  chaste  and  cp. caret.  Cp.  also  castle  and  the  first  element  in castrametation.  For  the  ending  see  verbal  suff. -ate.
=== KLN xyster
25687:nova,  n.,  a  new  star  that  appears  suddenly  and then  grows  fainter  gradually  ( astron .) —  ModL., short  for  L.  nova  Stella,  ‘a  new  star’;  fern,  of novus,  ‘new’.  See  new  and  cp.  novel,  adj. novaculite,  n.,  a  hard  slate  used  for  whetstones {mineral.)  —  Formed  with  subst.  suff.  -ite  fr.  L. novacula,  ‘a  sharp  knife,  a  razor’,  a  noun  formed with  instrumental  suff.  -cula,  from  the  verb *novdre,  ‘to  whet’,  which  prob.  derives  fr. *qsnewa-,  from  I.-E.  *qsneu-,  enlargement  of base  *qseu-,  whence  also  OI.  kfnotram,  ‘whet¬ stone’,  kfnauti,  ‘grinds,  whets’  (pp.  kynutah), ON.  snoggr,  ‘short-haired’,  snaudr,  ’bald,  bare, poor’,  Norw.  snau ,  dial.  Swed.  snauder,  ‘bald, short’,  MDu.  snode,  Du.  snood,  ‘base,  heinous, wicked’,  MHG.  snoede,  ‘contemptible’  (whence G.  schnode,  ‘base,  disdainful'),  orig.  meaning ‘shorn’.  For  derivatives  of  the  primitive  base *qseu-,  see  xyster.
=== KLN castle/castrum
2126:alcazar,  n.,  a  castle,  a  palace.  —  Sp.,  fr.  Arab. al-qasr,  ‘the  castle’,  fr.  al-,  ‘the’,  and  L.  castrum, ‘fortified  place,  fort,  castle’.  See  castrameta- tion  and  cp,  castle.
6706:castle,  n.  —  ME.  castel,  fr.  ONF.  castel,  corre¬ sponding  to  OF.  chaste!  (F.  chateau),  fr.  L.  cas¬ tellum,  ‘citadel,  fortress,  stronghold’,  dimin.  of castrum,  ‘fortified  place,  fort,  castle’,  castra (pi.),  ‘camp’.  See  castrametation  and  cp.  alcazar, castellan,  Castilian,  chateau.
```


## [2026-09-06T20:35:22.405Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nseg=t.split('\\f')\nimport re\ndef leafof(sub):\n    i=t.find(sub); return t.count('\\f',0,i)\nfor s in [\"alcazar,  n.,  a  castle\",\"castle,  n.  —  ME.  castel\",\"chastity\",\"xyster\"]:\n    l=leafof(s); print(s[:20],\"leaf\",l)\n# xyster entry\ni=t.find(\"xyster\")\nprint(t[i-200:i+900] if i>0 else \"NOT FOUND\")\nEOF"
}
```


### [2026-09-06T20:35:23.947Z] TOOL RESULT

```
alcazar,  n.,  a  ca leaf 35
castle,  n.  —  ME.  leaf 140
chastity leaf 153
xyster leaf 566
  Du.  snood,  ‘base,  heinous, wicked’,  MHG.  snoede,  ‘contemptible’  (whence G.  schnode,  ‘base,  disdainful'),  orig.  meaning ‘shorn’.  For  derivatives  of  the  primitive  base *qseu-,  see  xyster.
novation,  n.,  the  replacement  of  an  old  obligation by  a  new  one  {law).  —  Late  L.  novatio,  gen. -onis,  ‘a  making  new,  renewal',  fr.  L.  novatus, pp.  of  novare,  ‘to  make  new’,  fr.  novus,  ‘new’. See  new,  adj.,  and  -ation  and  cp.  next  word, novel,  adj.,  new;  strange;  unusual.  —  ME.,  fr. OF.  novel,  nouvel  [F.  nouveau  (fern,  nouvelle)], fr.  L.  novellas,  dimin.  of  novus,  ‘new’.  See  new and  cp.  nova,  novation,  novice,  innovate,  reno¬ vate.
novel,  n.,  a  fictitious  prose  narrative  of  consider¬ able  length,  representing  human  life.  —  MF.  no- velle  (F.  nouvelle),  ‘short  story’,  fr.  It.  novella, fr.  L.  novella,  ‘new  things',  neut.  pi.  of  novellas, ‘new’,  used  as  a  fem.  sing.  noun.  See  novel,  adj. novelette,  n.,  a  short  novel.  —  Formed  fr.  novel, n.,  with  dimin.  suff.  -ette. novel
```


## [2026-09-06T20:35:31.665Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor fn in ['KLN_1966.txt','KLN_1971.txt']:\n    t=open(fn,encoding='utf-8',errors='replace').read()\n    print(\"#####\",fn, \"leaves\",t.count('\\f'))\n    for m in re.finditer(r'xyst', t):\n        i=m.start(); leaf=t.count('\\f',0,i)\n        print(\"leaf\",leaf,\"|\",t[i-100:i+400].replace('\\n',' '))\n        print('---')\nEOF"
}
```


### [2026-09-06T20:35:33.354Z] TOOL RESULT

```
##### KLN_1966.txt leaves 902
leaf 566 | ,  disdainful'),  orig.  meaning ‘shorn’.  For  derivatives  of  the  primitive  base *qseu-,  see  xyster. novation,  n.,  the  replacement  of  an  old  obligation by  a  new  one  {law).  —  Late  L.  novatio,  gen. -onis,  ‘a  making  new,  renewal',  fr.  L.  novatus, pp.  of  novare,  ‘to  make  new’,  fr.  novus,  ‘new’. See  new,  adj.,  and  -ation  and  cp.  next  word, novel,  adj.,  new;  strange;  unusual.  —  ME.,  fr. OF.  novel,  nouvel  [F.  nouveau  (fern,  nouvelle)], fr.  L. 
---
leaf 589 | eophagous,  adj.,  feeding  on  oysters.  —  Com¬ pounded  of  ostreo-  and  Gk.  -<pdy o;,  fr.  cpxystv, ‘to  eat’.  See  -phagous. ostrich,  n.  —  ME.  ostrice,  oystriche,  fr.  OF. ostruce,  fr.  earlier  OF.  ostrusce  (F.  autruche ),  fr. VL.  avis  struthid,  lit.,  ‘the  bird  ostrich’,  fr.  L.  avis, ‘bird’,  and  Gk.  axpooIKcov,  ‘ostrich’;  see  aviary and  Struthio.  A  similar  contraction  of  L.  avis occurs  in  E.  bustard,  which  derives  ult.  fr.  L.  avis turda. Ostrog
---
##### KLN_1971.txt leaves 0
leaf 0 | node, ‘base, disdainful’), orig. meaning  ‘shorn’. For derivatives of the primitive base  *qseu see xyster.   novation, n., the replacement of an old obligation  by a new one (law). — Late L. novdtio, gen.  -dnis, ‘a making new, renewal", fr. L. nova t us,  pp. of novare, ‘to make new', fr. novus, ‘new’.  See new, adj., and -ation and cp. next word,  novel, adj., new; strange; unusual. — ME., fr.  OF. novel , nouvel [F. nouveau (fem. nouvelle)],  fr. L. novellas, dimin. of novus, ‘new*. See new 
---
leaf 0 | rved of wood’,  from the stem of £etv ‘to scrape, scratch, pol-  ish’, which is rel. to of s.m. See xyster.  X rays, n. pi., Roentgen rays. — They were called  by their discoverer Wilhelm Konrad von  Roentgen (1845-1923) (in 1 896) X Strahlen (=  X-rays ), to suggest that the exact nature of  radiation was unknown. For such use of the  letter x see X, x.   xyl-, form of xylo- before a vowel,  xylem, n., woody tissue in higher plants, the op-  posite of phloem {bot.) — G. Xylem, coined by  the bo
---
leaf 0 | iv, ‘to scrape, scratch, polish’ (see  next word) ; so called in allusion to the 2-edged  leaves.   xyster, n., an instrument for scraping bones  (surg.) — Gk. £u<rnr)p, ‘graving tool’, fr. £uav,  ‘to scrape, scratch, polish’, whence also £up6v,  ‘razor’, Soot !<;, ‘robe with a sweeping train’,     £u<ru6v, ‘polished shaft of a spear’ (short for  Sopu £uaT6v), ‘polished shaft of a spear’, neut.  of ‘polished’ (see next word), and cogn.   with k?urah, ‘razor’; fr. I.-E. base *qseu~. Cp.  Xyris, x
---
leaf 0 |  Cp.  Xyris, xoanon. For derivatives of *qsneu- f art  enlargement of base *qseu-, see novaculite.  xystus, n., a long and open portico for athletic  exercises {Greek and Roman antiq .) — L.,  fr. Gk. £u<tt6s, ‘a covered portico or gallery  where the athletes exercised in winter^, short for  £uot 6<; 8p6p,o<;, ‘polished course or race’;  ^uoto? is verbal adj. of £ueiv, ‘to scrape,  scratch, polish’ (see prec. word) ; so called in al-  lusion to the polished floor of the portico.      y-, perfect
---
```


## [2026-09-06T20:35:40.617Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null\necho \"=== search خشنود in v2\"\ngrep -n 'خشنود' BQT_v2_pages.txt | head -20"
}
```


### [2026-09-06T20:35:40.699Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4339896 Sep  4 14:06 BQT_v2_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2499427 Sep  4 14:06 incoming/BQT/BQT_v3_pages.txt
=== search خشنود in v2
12538: ‫مخفف خشنود است که راضی وخوشحال باشد ‪۰‬‬
14889:                                                    ‫خشنود‬    ‫اول و واو معدو له ‪.‬رك‪:‬‬   ‫‪ -‬سم‬        ‫نوود‬
40236:                                                ‫ر‪-‬‬‫‪۱‬‬          ‫( راضی » خشنود ) «گربرسن ‪۹‬‬                ‫‪۲‬‬
```


## [2026-09-06T20:35:44.682Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n '\\[pdf page' BQT_v2_pages.txt | head -3\necho \"---\"\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(\"npages\",len(pages))\nfor i,p in enumerate(pages):\n    if 'خشنود' in p:\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        print(\"idx\",i,\"tag\",m.group(1) if m else None)\nEOF"
}
```


### [2026-09-06T20:35:46.452Z] TOOL RESULT

```
---
npages 684
idx 213 tag None
idx 253 tag None
idx 667 tag None
```


## [2026-09-06T20:35:49.835Z] TOOL CALL #17: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-06T20:35:49.883Z] TOOL RESULT

```
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
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
```


## [2026-09-06T20:35:52.284Z] TOOL CALL #18: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:755 2>&1 | head -60"
}
```


### [2026-09-06T20:35:54.453Z] TOOL RESULT

```
no scan of BQT covers printed page 755 (see 'scans' in refs_online.json)
```


## [2026-09-06T20:36:00.904Z] TOOL CALL #19: Bash

```json
{
 "command": "grep -o '\"where\": \"[^\"]*BQT[^\"]*\"' data/verification/page-25*.json | head; echo \"---\"; python3 -c \"\nimport json,glob\nfor f in sorted(glob.glob('data/verification/page-25*.json'))[:3]:\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e['nodes']:\n            for c in n.get('ref_check',[]):\n                if c['ref'].startswith('BQT'): print(f, c['ref'], c['status'], c['note'][:300]); \n\" | head -20"
}
```


### [2026-09-06T20:36:02.962Z] TOOL RESULT

```
data/verification/page-251.json:"where": "p. 1688 footnote 5 (BQT_v3_picofile.pdf p. 481)"
data/verification/page-253.json:"where": "Borhan-e Qate' p.1214 with Mo'in's footnote (BQT_v2_pages.txt leaf 674)"
data/verification/page-253.json:"where": "grep 'شمیز' in BQT_v1/v2/v3 pages files"
data/verification/page-252.json:"where": "Borhan-e Qateʿ s.v. چرمه (BQT_v2_pages.txt line 5336; also quoted verbatim by Dehkhoda)"
data/verification/page-258.json:"where": "Moʿin's footnote in BQT p.1619"
---
data/verification/page-250.json BQT:149 partial BQT_v1_pages.txt leaf 365 (printed ≈ p.150-155 with the volume's drifting leaf offset, so within a few pages of Nourai's 149) carries the افسردن entry: 'افسردن، بر وزن افشردن، بمعنی سرد شدن و یخ بستن و منجمد گردیدن باشد - و از چیزی و کسی دل سرد شدن هم هست' — both of Nourai's senses, but the Borhān e
data/verification/page-250.json BQT:7 partial BQT_v1_pages.txt leaf 215 (≈ printed p.5-7) has the entry 'آب سالان - بالام بر وزن آب پاشان، بمعنی باغ باشد و بعربی حدیقه گویند' with a Moʿin footnote referring the reader to بهاران; the Persian word is there, but the page carries nothing on Old Persian upa-sard.
data/verification/page-250.json BQT:7 partial BQT_v1_pages.txt leaf 215: 'آب سالان - بالام بر وزن آب پاشان، بمعنی باغ باشد و بعربی حدیقه گویند ۴' — the word is on the page Nourai cites, but Borhān glosses it 'garden', not 'spring'; Moʿin's footnote there is a cross-reference (قس: بهاران).
data/verification/page-250.json BQT:1671,1673 partial Borhān-e Qāṭeʿ ed. Moʿin p.1671 (کلاه) with footnote 10: 'وجه اشتقاقی آن درست معلوم نیست. قس: کردی kulāw، پهلوی kulāf «هوبشمان ۸۹۳»' — the Pahlavi form yes, the Indo-European root no. p.1673 (کلبه) footnote 5: '* کربه. از پهلوی kurpak > ارمنی kʿrpak … معرّب آن کربق، قربق … و نیز کربج، کلبة' — Pahlav
data/verification/page-251.json BQT:1688 supports not cited by Nourai for this node but by the same editor: footnote 5, p. 1688, 'در پهلوی kilîsyâk گاه در مورد معبد ساری بکار رفته' (read from the page image; saved to data/verification/sources/refs/ocr/BQT/1688.vision.txt).
data/verification/page-251.json BQT:1688 supports Headword «کلیسا ۵»: 'مخفف کلیسیا است که جای پرستش و معبد ترسایان باشد' + footnote 5 'از یونانی ékklēsía' (page image read by vision, saved as data/verification/sources/refs/ocr/BQT/1688.vision.txt).
data/verification/page-251.json BQT:1709 supports footnote 6, p. 1709: 'در رسم‌الخط پهلوی kanashyâ (مجمع) «بلوشه. دستور پهلوی ص ۲۵»' (read from the page image, saved to data/verification/sources/refs/ocr/BQT/1709.vision.txt).
data/verification/page-251.json BQT:1709 supports Headword 'کنشت — بفتح اول و ثانی و سکون سین بی‌نقطه و فوقانی، آتشکده و آتشخانه را گویند ... و مخفف کنشت هم هست که آتشکده و معبد یهودان باشد' with footnote 6 (Pahlavi kanashyâ, Hebrew keneseth, Aramaic کنوشتا).
```


## [2026-09-06T20:36:09.984Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[213]\nimport re\nfor ln in p.split('\\n'):\n    if 'خشنود' in ln or 'خشن' in ln or 'خوش' in ln:\n        print(repr(ln))\nprint(\"=== full leaf 213 (first 3000 chars) ===\")\nprint(p[:3000])\nEOF"
}
```


### [2026-09-06T20:36:11.730Z] TOOL RESULT

```
'                                                   \u202bباشد \u202a.\u202c\u202c         \u202bخشنان \u202a -\u202cب باضمول بر وزن برهان \u202a۰\u202c\u202c'
' \u202bمخفف خشنود است که راضی وخوشحال باشد \u202a۰\u202c\u202c'
'  \u202b\u202a«- ۴\u202cخدن\u200cبروزن كتف سعتی\u202c               \u202bورك\u202a :\u202cخشن\u202a,\u202cخشنار\u202a.\u202c\u202c                  \u202bحشن سید نود“ «لفت\u200cقرس \u202a۶\u202c\u202c          \u202b\u202a ۱\u202cکے\u202c'
'  \u202bزیر کد\u202a .\u202cوخشن خالها رخوردن\u200cطعامپا | وشراب ها که حرارت طبیمی راازترا کیب مردم رفع\u202c'
'  \u202bاز \u202a :\u202cخشن\u202c      \u202b\u202a۴\u202c\u202c               \u202b\u202a,\u202c\u202c   \u202bخش \u200cخاله\u202c   \u202b\u202a:\u202c\u202c   \u202bرك\u202c                 \u202b\u202a« €\u202cجامع الحکمتن\u202c          \u202b\u202a...\u202cدقع همی کنند \u202a.\u202c\u202c'
'         \u202bعقاب تیز برباید (ارباید\u202a .\u202cدهخدا) خشنار\u202a».\u202c\u202c                             \u202bاز آن کردار مکرودم رباید\u202c'
'             \u202b\u202a .\u202cزن مادر بود \u202a .\u202cفرخی (سستالی) گوید\u202a: \u200e\u202c\u202c                     \u202bرك \u202a :\u202cخرو وخوش \u202a«:\u202cخخو\u202c               \u202bو\u202c        \u202b\u202a۶ “°\u202c\u202c   \u202b\u202aAA\u202c\u202c'
=== full leaf 213 (first 3000 chars) ===
                                                                                                                ‫‪۷۲‬‬


 ‫بزر کهتیرء رن میانسرسفید باشد و ترکان‬                            ‫خشی ه بنتح اول بروزن چمن گ‪.‬یاهی‬
‫قثقلداق میگوبند ‪ ۰‬وبضم اول نیز درست است "‬                         ‫باشد کهاز آن جامه بافند و فقیران ودروشان‬
‫و بشاین نقطه دار همآمده است چه در فارسی‬                           ‫پوشند ‪ -‬وبکر اول مخفف خشین است» ‪ ۰‬آن‬
 ‫سین وشین هردو بهم تبدیل می‌بابند ؛ و بجای‬                         ‫بازبی باشد نه‌سقید وله سباء ‪ -‬ودرعربی هرچیز‬
 ‫لون بای حطی هکمفته اند کهبر وزن بدیدار‬                                                             ‫درشت را گوشد ‪۳‬‬
                                                   ‫باشد ‪.‬‬         ‫خشنان ‪ -‬ب باضمول بر وزن برهان ‪۰‬‬
‫‪ -‬بر وزن بلنگ ‪ ,‬زاغ سر‬                    ‫حشنگ‬                                       ‫فرخنده وخجسته ومبارك راگوبند ‪.‬‬
‫وسر کجل و کجلی را کوبند ‪ -‬و مردم کچل را‬                           ‫ک=نابه ازمنافق‌بودن‬            ‫دن‬
                                                                                                  ‫شیلو‬
                                                                                                     ‫ش‬ ‫خ‬
                                           ‫تگبفزته‌اند‪.‬‬                                             ‫وطاق کردن باشد ‪.‬‬
         ‫‪۱‬‬       ‫‪۲‬‬     ‫معیم ‪. _ ۵‬‬
 ‫حشنو = بامول والك بروزن‌پر کو‪.‬‬                                   ‫خشی خاله = بروزن‌طر بخانه‪ .‬خانه‌ای‬
 ‫مخفف خشنود است که راضی وخوشحال باشد ‪۰‬‬
                                                                  ‫‪۰‬ویند که ازتی بوربا سازند ‪ -‬و خانه‌ای رانيز‬
                                                                                                            ‫گ‬
                    ‫ویفتح اول هم درست است ‪۴#.‬‬                      ‫گته‌اند که بر در ورنجرءآن خار شتری ندند‬
  ‫حشنی ‪ -‬بضم اول و کر الك بورزن‬                                    ‫و آب بر آن پاشند تاهوا و نیم سرد درون‬
                    ‫‪.‬‬        ‫ند‬
                              ‫وهبرا‬
                                  ‫گحش‬
                                    ‫معطی » زن فا‬                                                                         ‫ی‬
‫واو ‪۰‬‬    ‫بصم اول ونانی وسکون‬          ‫=‬   ‫حشو‬                     ‫= بقتح اول باسن بینقطه‬            ‫ر‪۶‬‬
 ‫مادر زن ومادر شوهر باشد ‪٩‬‏ ‪ -‬ویقتح اول در‬                        ‫بمعتی خشتنشار است که مرعابی‬            ‫بروزن طلبکار »‬



  ‫‪«- ۴‬خدن‌بروزن كتف سعتی‬               ‫ورك‪ :‬خشن‪,‬خشنار‪.‬‬                  ‫حشن سید نود“ «لفت‌قرس ‪۶‬‬          ‫‪ ۱‬کے‬

  ‫را شتافتن بخاتهاء‬      ‫بینم که مردمان مر گرمای‌سخت‬                  ‫‪#‬اهم‬       ‫‪۴‬‬    ‫ت‪۱‬شرح‌قاموی*‪.‬‬
                                                                                                  ‫ت»‬‫سس‬
                                                                                                     ‫شت ازهر چىز ا‬

  ‫زیر کد‪
```


## [2026-09-06T20:36:20.396Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i 'xsnu\\|xšnu\\|hu-x\\|khshnu\\|husnut' BQT_v*_pages.txt incoming/BQT/BQT_v*_pages.txt 2>/dev/null | head -20\necho \"=== leaf 214 head\"\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[214][:1200])\nEOF"
}
```


### [2026-09-06T20:36:24.032Z] TOOL RESULT

```
=== leaf 214 head
  ‫”‪^“ Ye‬‬                                                                                                           ‫خشوانه‬

‫تر‬    ‫را گونند که در مقایل‬    ‫خعك‬    ‫و در عرای‬         ‫عربی‌خرمای زیون وضایم‪ -‬وزبون شدن خرمارا‬
                                      ‫است ‪. ۴‬‬                                                                  ‫گویند ‪.‬‬
 ‫جشیج ه بفتح اول وکر انی وسکون‬                         ‫حشوا ل‪ ۵‬بنم اول وسکون ثانی وواو‬
 ‫تحتانی و جیم ‪ ۰‬بمعنی تقیض و ضد باشد © ‪-‬‬
                                                        ‫موبها ازه آویخته باشد ماتند خرسك وکبه‬
                                      ‫اشد © ‪.‬‬                                      ‫وامثال آن ‪.‬‬
                                                                                         ‫‪۳‬‬     ‫‪۰‬‬               ‫‪۰‬‬



 ‫با جیم بر وزن رفیقان »‬      ‫خشیحان‬                     ‫وخاش = بفتح اول وخای‬                               ‫حش‬
 ‫نقضان‬
     ‫ضدان و‬          ‫جمم خشیج است ‪.‬که بمعتی‬            ‫بروزن لش ولاش » ان لفت‬                        ‫ده‬
                                                                                                      ‫یالف‬
```


## [2026-09-06T20:36:30.067Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor fn in ['BQT_v2_pages.txt','incoming/BQT/BQT_v3_pages.txt']:\n    t=open(fn,encoding='utf-8',errors='replace').read().split('\\f')\n    print(\"####\",fn,len(t))\n    for w in ['شانه','شور']:\n        idxs=[i for i,p in enumerate(t) if w in p]\n        print(w, idxs[:25])\nEOF"
}
```


### [2026-09-06T20:36:31.876Z] TOOL RESULT

```
#### BQT_v2_pages.txt 684
شانه [3, 8, 17, 70, 74, 82, 94, 145, 190, 234, 275, 322, 329, 344, 358, 364, 458, 538, 585, 607, 673]
شور [12, 13, 16, 18, 23, 25, 34, 39, 42, 47, 57, 62, 74, 75, 99, 100, 105, 106, 112, 113, 140, 141, 152, 156, 171]
#### incoming/BQT/BQT_v3_pages.txt 721
شانه [11, 20, 21, 66, 68, 111, 358, 406, 415, 438, 451, 504, 528, 529, 581, 623, 652, 663]
شور [4, 15, 40, 51, 73, 97, 98, 101, 102, 106, 115, 131, 140, 148, 162, 172, 177, 190, 199, 200, 201, 207, 209, 210, 220]
```


## [2026-09-06T20:36:39.502Z] TOOL CALL #23: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nprint(json.dumps(d.get('scans'),ensure_ascii=False,indent=1))\nprint(d.get('page_offset'))\n\""
}
```


### [2026-09-06T20:36:41.641Z] TOOL RESULT

```
[
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
]
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
```


## [2026-09-06T20:36:49.886Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re,json\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\npm=json.load(open('BQT_v3_pagemap.json'))['map']\nfor pr in ['1230','1307','1306','1308']:\n    print(pr,'-> pdf',pm.get(pr))\ndef show(pdfpage):\n    for seg in t:\n        m=re.search(r'\\[pdf page (\\d+)\\]',seg)\n        if m and int(m.group(1))==pdfpage:\n            return seg\n    return None\nfor pr in ['1230','1307']:\n    pg=pm.get(pr)\n    s=show(int(pg)) if pg else None\n    print(\"=========== printed\",pr,\"pdf\",pg)\n    print(s[:2500] if s else \"no tagged page\")\nEOF"
}
```


### [2026-09-06T20:36:52.098Z] TOOL RESULT

```
1230 -> pdf 21
1307 -> pdf 98
1306 -> pdf 97
1308 -> pdf 99
=========== printed 1230 pdf 21
[pdf page 21]
شاد ۲۳۰ ات

شا له ۱ = بروزن ‎le‏ معروفت‌وآن

چیزی باشد که از چوب
و غیره سازاد و بدان‌رش سس
رزلف و کیو راپردازدهند ‎ABBE‏
‏سوافزاریاست جولاعگایرا
که تارهای‌رسمان رااز ‎OT‏ شانه(سه‌فم)
‎asta‏ بمنواییکه در وقت بافتن دونار ییکجا
و پپلوی هم واقع نشود -
و بمعتی شان ‎Jee‏ و ‎BS‏
‎yy‏ هپهست ۷ - ‎cary‏
‎pty‏ اسب رالیز کویند -
واستخوان کتفراهم‌میگوند.
‎als‏ سره ‎anus‏ شانه سر
راگویند» وآن پرنده ایست معروف ۸ .

ایثان هم هست که ضمیر جمح غایب باشد ۷ -
ودر عربی ۴ بمعنی قدر ومرتبه وش وکت‌وعظمت
- وحال وفکر والدیشه و کاروبار باشد - و بیم
داه شتن از چیزی را هم گویند - و کاهی بجای
‎bid‏ حق عم گنته میشود چنانکه میگوبند « این
‎aT‏ در ‎ols‏ او ‎Jul‏ شده است» یمنی در حق او
آمده است

‎BL‏ ۴ - بر وزن ‎ails‏ » یعئی زلت
وکا کل را شاه کند .

‏شاندن ‎pe‏ وزن ماندن . بمعنی شاله
کردن باشد ۴ - ومشفف ‎Quiles‏ و شالیدن هم
هت 6 .#

‎Hi‏ ه بر وزن اوك ۰ سنکه دان
‎ory‏ دان مرغارا کوشد .

‏- پهلوی حم 0 - پارسی‌باستان ‎sham‏ «اسشق ۰.۷۹۹ درفارسی «شان»م رکب

‏است از وه .+ ون جمع‌آن 0 ‎als)‏ : مان ‎von‏ «هوبشمان ۰۷۰۹ . رله: ‎Sedge‏

‎je bela‏ . - (عر) «شأن ‎cal‏ « کاروحال . ‎Os?‏ جمع ... وجست وجوی

‏وجستن ودربافتن وکین - وکردن ‎TUES‏ موجب خوبی‌ورونق حال وکارباشد وخبردادن»

‏«منتبی الارب» . درفارسی بجای شأن . ‎shan‏ تلفظ کنند. خاقانی‌شروانی درفصيدة شینبه پس از
میت مذ کور درح ۰ ‎ate‏ قبل گوید «دیوان خاقانی ۰۲۱۸ :

‏و گرچه‌تحل وقتی‌نوش بارد ‎mts‏ دارد . توآن منک رکه اوحی ربك آمد وحی درشاش.

‏۴ - رك : شالدن.
‎ole - ۴‏ بآب‌وفاروی عدل میشوید فك بدست ظفی جمد مك میشاند .
الوری اییوردی . «فرهنگه ‎Glin‏ .
© - بدسگال تو راجه دارد ‎Ole‏ شانده در دل ز غم ‎Me‏ از تو

‏سوزی‌سمرفندی. «فرهنك ‎Hellas‏

‎Shak yey. 65-2 ‏اروپابی)‎ yas) ‏حند وژرمانی‎ « (ate) 50202 ‏پهلوی‎ - ۱

‏بلوجی ع ‎shandg‏ (قتوی اسب) « ‎geet‏ ۰۷۷۱ , اورامانی ‎SHADE‏ ( دوششیب کوه ) «قد.

‏اورامان ‎Ley‏ = ۷ مد ان( م.) : ۷ - پرنده‌ای از نوع کنجشك دارای منقار
پاربگ و دراز باندام سارسیاه ودارای بکدسته 2 (بشکل ‎(ct‏ پرسر .

‎os fs #‏ - بفتح دال » اوستا ‎xshvash . dasa‏ ,پهلوی ‎shdacdah‏ کردی ع

‎, 9202021 ‏پازد‎ cvye geet? ‏پدبدآمده‎ Gogh? ‏(ن) در شانزده بقیای‎ . shanzdeh

‏بلوچی ع یز 510402212« هوبشمان ۳۷۰ کیلکی ‎shonzdie‏ ؛ ؛عددی‌دوبر ابر هشتده‌بملاواخش.

‏) برهان اطع ۱۵۹ ]

=========== printed 1307 pdf 98
[pdf page 98]
‎Vey‏ شورش

‏و شتن وپاکیزه ساختن ‎Ob‏ باشد - وشوریدن
و شورش مصدر ‎cas‏ - و بفتح اول وئالی‌بزبان
زلد و پازند (۲) بمعنی سیر است که در برابر
کرسنه باشد .۷

‎Wise‏ ینم اول و بای فارسی بالف
کشیده , چاروایی راگوبند از اصب واستر وخر
الاغ که دروقت راء رفتن سرهای یاهای ار ازهم
دورباشد وقاب ‎Lak‏ بهم رسد وساییده ‎singe‏
‏کرد چاروابی که زانوهایش بهنگام رفتن بهم
پساید .

‏شور باج* » با جیم ساکن + معرب
شوربا است که آب گوشت پشته باشد .

‏شود سلح ”!= ‎phe yee‏ شور است
که ورزیدن سلاح ‎ath Ke‏ بکار فرمودن ۰
نی بچگوله بکار پاید فرمود - و کی را نیز
کفنه‌اند که مستمد قتال و جدال ‎ath‏ ومقدمة
الجیش را یز گوبند یمنی جمعی که جنگه را
بهم رسانند و بت ر کی شرباشاران خوانشد.

‏شو رش ۰۱۱ بکسالت,بممنی‌شوریدن
است ممنی شور وغوغا کردن - و درهم آمیختن
- و برهم زدن - وبرهم خوردن +

‏شو خیدان ۱ - بروزن‌پرشیدن ‎wee‏
‎oS oe‏ شدن باشد.

‎ae‏ اول و سکون ثالی و دال
‎aml‏ )1( یمنی شد ورفت و گذشت ۴سومورچةً
کوچك را یز کوبند - و بکسر اول وتالی‌شبت
راکویند ۴ , وآن رستنیی ‎ath‏ معرو ف که در
‎col‏ کنند ودر ک و کو وطمام لیز .

‏شودانیق ۷ ه بضم اول و دال بالف
کشیده و نون بتحتالی رسیده و بقاف زده.ععرب
سودالیات‌است» وآن مرغی باشدکه درخت را با
منقار سوراخ کند .

‏شو‌دن * »بر وزن بودن ‎Orr gear‏
باشد .

‏شور دم اول و ثالی مجهول بر وزن
مور . طعمی و لذتی باشد ممروف ‎٩‏ - وآشوب
ر ‎lege‏ و فرداد را کویند ۷ - و شوم و لحس
واعبارك را نیز گفته‌اند - و بمعنی سعی و کوشش
هم‌هست - و :ای رومی را 55 کوبند که نقیر
باد ‎leery‏ ورزش وکاری را خوب ورزیدن‌هم
هت - و برهم خوردن - وبرهم زدن - و بهم
آمیخته را یز ‎ca”‏ الدوبعربی مالج خوانند۸ -

‏(۱) چك : - ابجه . ‎(x)‏ چك : ژند ویاژند .
۱ - از : شوخ («م.)-یدن ‎(Spree ty)‏ . ۴ رگ : شدن .
۴ ره : شبت . ۴ - رك : سودالیات . 6 ‎Cpe) we‏

‏۱ - چیزی که درآن ‎te‏ دك بیش از اعتدال باشد » پردمك :

‏کس له بیند که تشنگان حجاز ‏ بلب آب شور کرد آیند . * کلتان ۳۷ ۰.

‏۷ - تا ‎alg‏ زلفك شوریده را بخط ‎past‏ فتاد گرد همه شهر شور وشر .
ءمار؟ مزوری «لفت فری ۰.۰۱4۳ ۸ -(عر)مالح (بکسرسوم) » بمعنی شور(لمکین)وآب‌شوره
و مالج (بفتح‌سوم) ممرب ماله (گلکاران) است .

‎sd ٩‏ شوربا ‎dy -۶* Ae)‏ سلحشور . ‎oN‏ از: شور ۳* ش(اسم‌مصدر).

‏* فورالدی وفورالیدن - ‎ee‏ اول وفتح دال , از: ‎satya) Gash gull base‏
مصدری متمدی) [ُرك : خوریدن] بهیجان آوردن | تحريك کردن 6 ابچاد آشو بکردن.

‏شور با - از : شور ‎LA eb)‏ (آش) , ممرب ‎OT‏ شوریاج (ه.م.) وشوربه «لفس» .
رك: شورباج ورك: الطبیخ ص۲۸ .
```


## [2026-09-06T20:37:08.255Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD sanag/comb\"\ngrep -n -i \"^šānag\\|^šānak\\|comb\" PHD.txt | head -20\necho \"=== PHD xusnud\"\ngrep -n -i \"xušnūd\\|xšnūd\\|xwašnūd\\|xušnūt\" PHD.txt PHD_mackenzie.txt | head\necho \"=== PHD sor salty\"\ngrep -n -i \"salty\\|^šōr\" PHD.txt | head"
}
```


### [2026-09-06T20:37:08.330Z] TOOL RESULT

```
=== PHD sanag/comb
31:'The script of the Pahlavi books derives ultimately from that of the official Aramaic of the Achaemenian empire. In the course of time, however, a high degree of ambiguity has developed in the script. Table I shows the development of the letters from Imperial Aramaic (with the transliteration and names of letters commonly used by Semitists), through the distinct forms used in the Parthian and Persian inscriptions of the third century A.D., and the archaic manuscript forms of the Psalter fragment (about seventh century),! to those of the Zoroastrian books. In addition to the multiple values of the letters listed, some of them may represent combinations of letters in certain contexts, e.g. - or 35 for 3+».
392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
430:kē(x)šīdan, kū(x)š- [kz(4)$-ytn! | M htos-ydn, N kēšīdan) strive, struggle, endeavour. ~iSn: strife, combat. ~iSnig : energetic. Кбу [kwd | N ~] street, lane. ki [AYK < A’yk | M kw, N kū, hi] where; that; than, ~ Буар [N лија] where. ~ tā: so that. kūč(ak) [Awe(k!) | N kūčak] small. kak [kwk'] small, short. kulāčag [kwľck' | N kulīča] small, round bun. kulāf [kwl”5 | N kuláh] cap, bonnet. ~ak [-k!] | N ~hak] little cap; calyx. kulang [Ring | N ~] crane. kullag [kwlk'] locust. kumig [Awmyk'] stomach. kun-, -išn, v. kardan, kunišn. кар [STE < A *st-h; kwn! | N ~] rump, buttocks, anus. kundāģ [knd^k! | M qnd’-, N kunda] magician, soothsayer. ~ih: magic, astrology. kundur [kwndl | N ~] frankincense. kunišn [kwnsn' | M kwnyšn] action, deed. ~gar LA | M -gr] doer, performer. kunjid [ŠM% < А пг; kwnc(y)t! | N ~] sesame. kün-marz [Rzonmlc] sodomite; sodomy. kurkum [kwlkwm] saffron. kurrag [kwlk' | N ~a] foal, colt. 1kust [Ruwst!] side, direction; district. kust [kwst' | Ar. qust] costus. kustag [kwstk! | M Rwstg] = !kust. ~bed [-pt'] district-commander. kustig [kwstyk! | N ~i] sacred girdle. kuštan, kuš- [NK SWN-tn! < А V nks; kwi-tn! | M kwšt, kws-, N ~] kill.
566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [spl | M ‘spr, N sipar] shield. spar-, v. spurdan. spas [sp’s | M ?s-, “р>, N sipas] service, gratitude, thanks.
583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
1279:comb šanag.
1280:combat | hamnibardih, kē(x)šišn; v. fight.
1281:combustion sog, sēzišn.
1929:fight (n.) Jang, nibard, pahikafišn; v. battle, combat.
=== PHD xusnud
=== PHD sor salty
566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [spl | M ‘spr, N sipar] shield. spar-, v. spurdan. spas [sp’s | M ?s-, “р>, N sipas] service, gratitude, thanks.
3506:salty sor.
```


## [2026-09-06T20:37:17.109Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD hu-\"; grep -n -o \"hušnūd[^]]*\\|hunsand[^]]*\" PHD.txt | head\necho \"=== BRT xšnu\"; grep -n -o \"hu-x[sš]nu[a-zāūē-]*\\|x[sš]nāvaya[a-z]*\\|x[sš]nu-\\|hux[sš]nuta[a-z]*\" BRT.txt | head -30\necho \"=== BRT count xšnav\"; grep -c 'xšnav\\|ysnav\\|xsnav' BRT.txt"
}
```


### [2026-09-06T20:37:17.220Z] TOOL RESULT

```
=== PHD hu-
189:hunsand [Phwnsnd
400:hunsand [hwnsnd | = P, (N xursand)
1372:hunsand, hu- šnūd, widwar.
1373:hunsandih, hušnūdīh, Énómag, šnēhr, wīdwarīh.
1649:hunsandih.
1650:hunsand.
2200:hušnūdih, šādih, šnāyēn- išn, urwāzišn, xwa(h)rih.
2206:hunsand,
=== BRT xšnu
5655:huxsnutaya
10906:xsnu-
30188:hu-xsnuta-
=== BRT count xšnav
6
```


## [2026-09-06T20:37:20.528Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor pat in ['hu-xsnuta-','xsnu-','huxsnutaya']:\n    for m in re.finditer(re.escape(pat),t):\n        i=m.start(); leaf=t.count('\\f',0,i)\n        print(\"###\",pat,\"leaf\",leaf)\n        print(t[max(0,i-600):i+800].replace('\\n',' '))\n        print()\n        break\nEOF"
}
```


### [2026-09-06T20:37:22.556Z] TOOL RESULT

```
### hu-xsnuta- leaf 993
  Aupaitisläiu'* "des  Kamel(hengst)s,  der  weisslichen Schaum  auf  seinen  Kopf  zurückwirft, auf  seine  guten  Knie  und  Beine"-  Yt 14.  iZ'^. *xsniu>%ra-  n.  'Knie'  kann  ich  nur  als  Um- bildung von  *i!nav-  n.  'Knie'  (vgl.  äsinav- und  inav-)  nach  Wörtern  wie  dvar&ra-  n, 'Bein',  ai.  cariira-  n.  'Fuss',  iharilra-  n.  'Arm' begreifen.  —  Npü.;  bisyär  xuscihr. —  i)Vgl.Bd. 34.  4,  wo  das  Kamel  hulnük  genannt  wird.  — )>  Dualrerbindung,  lu  BB.  lO,  ifiT.  —  3)  S. iSt.  Dst.  ZA.  3.  S65,  Jn.  Reader  109. dby  Google l83I huxänuta- 'hutay- iSsa •  j.  hu-xsnuta-  Adj.  (fem.  •«•)  'gutge- schärft, scharfgespitzt':  aritayasat  , ,  'ia YtJO.  39;   —  ar^tSis  -taya  Yl. /O.  24. ai.  iinuld-  Adj.,  PPtP.  iura  V.  kin^li.  —  Vgl li£i.inüla-. •  j.  hu'xsnütay-  f.  'gute  Befriedigung': tbiltahecii  ax^nuHake  müra  manu  räma- yeiti    'üittm  paiti    mihrahe    ".  .  bei  (Sp. 825  u.)  guter  Befriedigung  des  M."''> Yt.io.  log. 1)  Sva.  wenn  M.  wohl  befiieili£t  ist;  vgl.  Yt. 10,  111. •  j.  hu-ci3ra-  Adj.  (fem.  'rä-)  i)  'von guter  Abstammung,  Herkunft':  nfm!  *nm .  .  yeAhl  n/maahs  ciinm  Aumahmcä AoxDmcä  hvarsUmcä  Y.^S.i.  t)  'des Anblick  gut  ist,  schön*:  äuiäia  aki  'ra (NSf.)  Yt. /-.  15. Vgl.  hu!a.tä.  EN. ■    hön'.  ^  Pü. :  > •  j.  hu'diSrä-  £  EN.  eines  gläubigen Mädchens:  'rayi  

### xsnu- leaf 329
Müilil  Bium  va  asaond 'mm  H. /-s'*. Pü.:  inäyltärih.  —  ■)  Vgl.  DST.  ZA.  2.  649 und  Yl  /.  O. •  j.  xSnaodräi  Inf.  'zufrieden  zu  stellen': s.  unter  'xsnaoira-. Zum  V.  xinav: •  j.  xänaoma-  m.  'Zufriedenstellung, Wohltat':  ks  paoirim  itnam  sam  mazista 'ma  xsnüvayäti  V.J.12. Zum  V,  xsnav:  —  Vgl.  xinümaine  mil  JScHMIDT Krit.  103.  —  rap.  inöm;  %.  dizu  Hbm.  AGr.  /. 214.  —  Pü,:  inäyünlh,  erl-i  .,  rämUnlar  iarl •  g.  xSnaoäamoa-  Adj.,  PPA.:  ^.'xihav: •  ).,  g.  'xänav-  V.  'Genüge  haben  an  — , leisten  in  — '.  Praes.  i  xs'nu-,  5  kuxsnu-, 16  (Des.)  cixsfiusa-,  17  (Fut.)  xsnaolya-, 30  (Iter.)  xinävaya-;  J-Aor.  i  xsnaos-, 2  x/tovis:  —  PPfP.  xskuta-'^;  PFP.  xsnao- %wa';  Inf  x/nümaine,  xsnao^räi.  S. noch  ax/nus/a  und  kuxsnBsa. i)  'sich  etwas  genügen  lassen,  zufrieden sein  mit  — ';  a)  mit  Akk. :  surunuyä  nB yas- futn . .  xsnuyä  nS yastatn  Y.  68. 9.  b)  mit Gen.:  surunuyä  nS . . yasnaAe  x/nuySm.. yasnahe  Yt. /o.ji.  2)  'Jemandem  Ge- nüge tun,  ihm  zuweisen,  was  ihm  recht und  billig  ist,  gebührt,  es  ihm  recht  machen, ihn  zufruden  stellen,  seine  Pflicht  ernillen gegen  — ',  mit  Akk. :  ks  paoirim  imam  iqm masista  xsnaoma  x'nävayäliV.3.iz;g.^2^; —  äai  tum  nishti>ail..ttar»m^a  asavamm kuxsnvqnS  H.2.13,  Vyt55(wo  ^kjt/h- vänB)-,  —  yS  neu  narsm  aiava

### huxsnutaya leaf 145
  ■)  Im  Gegens.  lu   häitisi-,\      nicht  besonders  übersetzt. B.  Y.  5j.  S.  —  >>  Them,  —  J)  VgL  lU  uxiaii-,  I      .  .,        .  .-    ,r  ,-  1      \   .     r      ■   l -..«r«4 '"«""".V-.  rffl.v/-Ti- und  den  Gebrauch    •  ]■  <"-^"'-  Adj.   (fem.  '!.,■)_  l)  'aufgencb- :t'.  2)  'gerade,  aufrichtig'. Kom[.E.;  Ableit.  (s.  arl/j/-)').  —  Aus  ir.  '/■J''''- dby  Google ■arätay- •  i-,  p,   'arätay-  f;  m."  'Speer,  Lanze': yaäam  zayanqm   raitöiiti  paoiryS  °iis  V. 14.^;    —    'tayasiä    karitayasca    '^.fj —  •//'/  ki-aiwyästa  Yt  13.  7 ; •tSis  huxsnutaya  Yt  10.  24;  —  'tayasat Anx/mi/a  YtiO.  39;  —  'lintrm  brSi'irS.- ta^nam  YtJO.  39;  —  väfff  laut  'Um AaraUi  jram..\'t.lo.2i;'P.2r,  —  WfiärsaAyä ..^düraiy  't'ts  parügmati  D.O.  4. KoiDp.\.,  E.;  Ableit.  (ärltya-,  'Srstaya-).  —  ü. Tfläy-  f.,  np.  xiil;  arm.  LW.  aiteay.  Vgl.  dam Hbx.  KZ. 36. 166  und  No. a.  —  lü.  fiu  V.  14): aril';    erl.;  tiäai,  (lu  V,  //  und  V.):    alin'i. —  ■)  Sicher  nur  Yl  10.  39.  —  J)  Wohl  aus a}t  veiderbi,  s.  aim.  LW.  Anders  GlcFb. y  b.  67. •  j.  *arStay-  f.,  anderer  Name  für  arftat- (sd.);  ufaratilUm  .  .  yqmca  sraosahe  ,  , yqmca  'tdif  yazata^e  y.^y.^^. Eig.  'Sichautrichten,  Geradesein' ;  lEt.  s.  arsla-. —  Pö. :  wie  iüt  arUSt-. •  j.  arätat-  f.  Name  derGöttin  {Yazala-)
```


## [2026-09-06T20:37:38.157Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG xšnaw\"; grep -n -i 'xšnau\\|xšnaw\\|xsnau\\|xšnu' CHEUNG.txt | head -20"
}
```


### [2026-09-06T20:37:38.227Z] TOOL RESULT

```
=== CHEUNG xšnaw
29483:Pres. athem.: IND. Isg. äx$nümiy <a-x-8-nu-u-mi-i-y> (ХР1 26), med. "axsnauvaiy <a-x-8-n-u-[v]-i-y> 
29509:*xSnau2 ? 457 
29536:*AVESTAN: xšnu- ‘to entertain, welcome, take care of (a guest)’, OAv. xSanmanai 
29542:ОРТ. 2sg. med. YAv. "kuxsnuuisa (FrW 7.2); Aor. s-: 3sg. INJ. OAv. xšnauš (Y 46.13, Y 51.12), med. 
29545:31.3, Y 51.9, Y 60.2); Caus.: pres. IND. 3sg. YAv. xsnauuaiieiti; Desid.: pres. IND. 15р. OAv. cixsnusa 
29589:*xšnauš ‘to sneeze’ 
57805:*ti(n)f , *xšnau! 
57937:*xsnaus
```


## [2026-09-06T20:37:40.518Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '29470,29600p' CHEUNG.txt"
}
```


### [2026-09-06T20:37:40.567Z] TOOL RESULT

```
*NEIR: Oss. І. exsyzgon, D. axsizge “pleasant; urgently needed’ 

© Considering the limited distribution, *xsij may be a regional borrowing. 
*PIE LIV: - | Pok.: 


*хф паш ‘to hear (< ‘to sharpen (the ears)’)’ 
*AVESTAN: ? Y Av. hu-xsnuta- (+ *hu- ‘well’) ‘well-sharpened’ (Yt 10.24, Yt 10.39). 
9 On Av. xsnu- see also Kellens — Pirart 1990: 233f. 


*OLD PERSIAN: (+ *4-) 4-xSn(a)u- ‘to hear’ (cf. Benveniste 1946: 47 ff.) = Kent: 182 
Pres. athem.: IND. Isg. äx$nümiy <a-x-8-nu-u-mi-i-y> (ХР1 26), med. "axsnauvaiy <a-x-8-n-u-[v]-i-y> 
(\DNb 24 |, Hinz 1965: 229), SUBJ. 25р. axsnavahy <a-x-S-n-v-a-h-y> (DNb 29), IMPV. 2sg. äxsnudiy 
<a-x-8-nu-u-di-i-y> (DNb 54). © On axšnümiy see Hinz 1969: 46. It is no doubt a late formation, on 
which see Mayrhofer 1991: 201. 


*MIDDLE PERSIAN: (+ *а-) MMP ’Snw-, ВМР ’Snw- /ä-Snü-/ ‘to hear, understand’ 
c DMMPP: 57b 


Pres.: IND. 3pl. MMP ’šnwynd (M49 II R,13, M382 II A,6(1769)), SUBJ. Zeg. MMP пуу (M219 II 
R,9), ІМРУ. Zeg. MMP ‘пуу (M219 II R,14); Partic.: perf. pass. MMP ’snwd (M176 I V,14) 
*PARTHIAN: ‘Snw- ‘to hear, hearken’? = DMMPP: 93b f. 

Pres.: IND. 35р. ‘Snwyd, ‘Snwyyd, 3pl. ‘Snwynd (SS 53), SUBJ. 15р. ‘Snw’n, 3sg. ‘Snw’h, 1р1. ‘Snw’’m, 
IMPV. 2sg. ‘Snw-, 2р1. ‘Snwyd, ‘snwyyd; Partic.: pres. *‘Snw’g (|SS 7 |), perf. pass. '$nwd; Inf.: ’snwdn 
(M4572 II Ri,9(1024)), “šnwdn 

*NWIR: (simplex or with *a-) NP sinudan, Sunudan, Sanidan/Sanav- ‘to listen, hear’, 
Kurd. (Sina) Zinaftin/Zinaw-, Awrom. aZn(aw)iäy/-Znaw- ‘to hear’, Fariz. bäsno 
‘hear !’, Abz. asnida/ó-Snónov-, Anar. -aSnofte/asnov-, Bakht. asnidan, Gil. (Rsht.) 
isnaveesteen/isnav-, Ham. esnoftan/esnov-, Jow. ma-fnoft/a-fno- ‘to hear, listen’, 
Gur. (Kand.) Sinäft-/-Snäw-, Meim. bem-efnofi/a-fno?-, Khuns. esnev-/esnift, 
esneva, Nn. asnufle/asnov-, Natan. -$novä/sänäv-, Qohr. asnófta/asnóv- ‘to hear’, 


*xSnau2 ? 457 


Semn. -snüá, Sang. -osnünd-/osnovaen-, Shamerz. -äšní-/šänám-, Siv. esn-/esni, Soi 
bá-šn-, Sorkh. b-ceSnu-/cesnu-, Lasg. b-ásnav- ‘to hear || (+ *a-) Zaz. 
asnawitiS/asnawen- ‘to hear’. Ф It is almost impossible to distinguish between ап 
initial prothetic vowel and the old preverb *a-, which can disappear or be 
assimilated after a tense marker. 

*NEIR: ? Wa. К$ыу-/К$әп- ‘to hear’, (caus.) К$ыу(ы)у-/К$оуоуа ‘to rebuke’ (rather 
*Hax$ ?) Ф The Wa. forms are "phonetically difficult to explain", Steblin- 
Kamenskij, ibid. 

*SANSKRIT: ksnav ‘to whet, sharpen’ (RV+) = EWAia I: 441 


«PIE *ksneu- ‘to sharpen’ = LIV: 373 | Pok.: 585 

*REFERENCES: Horn 1893: 177; Zhukovskij I: 20, 156; КРЕТ: 81a f., 140a f., 207b, 247a; Ivanow 1926: 
422; KPF II: 205; Christensen, Contributions I: 69, 167, 261; Christensen, Contributions II: 59, 116, 160; 
Abrahamian 1936: 113; Lambton 1938: 42b, 78a; MacKenzie 1966: 89; Nyberg II: 34b; WIM I: 68; WIM 
Ш: 104; Vahman — Asatrian 1991: 77; Werba 1997: 174; Paul 1998: 291; Steblin-Kamenskij 1999: 212; 
Lecoq 2002: 120, 122, 131, 133 (passim) 


*xÉnau^ ? ‘to exchange gifts (between host and guest) (whence: ‘to entertain, 
welcome (a guest), to thank, praise, etc.’)’ 
*AVESTAN: xšnu- ‘to entertain, welcome, take care of (a guest)’, OAv. xSanmanai 


"instead" (Y 29.9) = Liste: 17 

Pres. {1} athem.: OPT. 2sg. YAv. xsnuiiá (Y 68.9), med. OAv. xsnouuisà (Y 28.1); Pres. {2} athem. red.: 
ОРТ. 2sg. med. YAv. "kuxsnuuisa (FrW 7.2); Aor. s-: 3sg. INJ. OAv. xšnauš (Y 46.13, Y 51.12), med. 
3sg. YAv. xsnaosta (P 49), SUBJ. 15р. med. OAv. xSnaosai (Y 46.1), 3р1. OAv. xšnaošən (Y 30.5); 
Partic.: pres. (2) kuxsnuuana- (Yt 8.49, H 2.13), aor. OAv. xsnaosomna- (Y 46.18), perf. pass. xSnüta- (Y 
31.3, Y 51.9, Y 60.2); Caus.: pres. IND. 3sg. YAv. xsnauuaiieiti; Desid.: pres. IND. 15р. OAv. cixsnusa 
(49.1) 

*OLD PERSIAN: хёпи- ‘to be satisfied, glad’ > Kent: 182 

Partic.: perf. pass. xSnuta- <x-S-nu-u-t> (DNb 26) 

*MIDDLE PERSIAN: MMP ‘snwm- (denomin.) “о propitiate’ || BMP sn’dyn- /snayen-/ 
(sec. caus.) ‘to praise, propitiate’, BMP hwsnwtk /hosnud/ /husnüd/, BMP hwsnwtk 
/hosnudag/ /husnudag/ ? ‘satisfied, content > DMMPP: 94 

Pres.: IND. 3sg. MMP ‘snwmyd {hapax} || Caus.: pres. IND. 3sg. BMP sn'dynyt /Snayénéd/; Inf.: caus. 
BMP Ssn’dynytn /Snayénidan/; Partic.: perf. pass. BMP sn’dynyt /Snayénid/ 

*SOGDIAN: SSogd. ’xSnyBnt ‘hospitable, dienerfreundlich’ 

*CHORESMIAN: m/XNwry- (denomin.) ‘to thank’, bxnwr’wc (+ neg.) ‘ingratitude’ 
c» Samadi: 138 

*NWIR: NP xusnüd ‘content, pleased, happy’ 

*NEIR: Oss. æxsæn (postp.) ‘in the middle of, between’, axszeny ‘public, general’, 
æxsæny lag ‘mediator, go-between’ (with archaic meaning ?) 

9 On the etymology see Schwartz, Fs H.P. Schmidt: 213 f.; Schwartz 1990: 203. 
This root and its IE provenance postulated by Schwartz, l.c. is problematic, as one 


458 *x&naus 


needs to make several assumptions about their semantic development: it 1s a rather 
tall order to reconcile notably the meanings of Av. and Oss. through an unproven 
series of semantic shifts. 

«PIE *ksenu- ‘to exchange gifts (between guest and host)’ ? = LIV: — | Pok.: 

*IE COGNATES: Gr. &évoc, (Ion.) &etvog 'strange(r); guest, host’, Olrish son ‘in 


exchange' 
*REFERENCES: Abaev, Slovar’ IV: 227 


*xšnauš ‘to sneeze’ 

*MIDDLE PERSIAN: BMP snwsk /snösag/ ‘sneeze’ 

*CHORESMIAN: xnwy- ‘to sneeze’ — Samadi: 238 

*NWIR: Kurd. (Kurm.) heniZin/heniZ- ‘to sneeze, yawn; to snooze’, Siv. esnis, Sang. 
asnis ‘to sneeze’, NP sundsah, isndsah, Khuns. esniZä, išnīžä, Tr. hosnija ‘sneeze’ 
*NEIR: Pash. nZol, Yzgh. SonixtsnixW-, Yghn. xünúš-/xünúšta ‘to sneeze’, Pash. nZai 
‘sneeze’, M. yanigo ‘sneezing’, Sh. Sini(y)zgak, Sunizgak, Rosh. Sinivzak ‘cold in 
the head, phlegm’, ? Oss. I. axsnyrsyn/&xsnyrst, D. aexsnirsun/aexsnirst ‘to sneeze’. 
© As for the Oss. forms, they are hardly connected to Engl. sneer, snore, snarl, NHG
```


## [2026-09-06T20:38:05.285Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD xsn\"; grep -n \"xšn\\|x&n\\|'xšn\\|xsn\" SOD.txt | head -20\necho \"=== SOD_pages xsn\"; grep -n \"xšn\\|xsn\" SOD_pages.txt | head -20\necho \"=== KNT xsnu\"; grep -n -i \"xšnu\\|xsnu\\|axšnu\" KNT.txt | head -20"
}
```


### [2026-09-06T20:38:05.372Z] TOOL RESULT

```
=== SOD xsn
11871:Oxsn'qc)   ©*fra-san 
12224:axsnam   ©Av.  xsnaoma-   ^'xsn'm 
12234:=^xsnk-,  xsnq- 
12241:(o)xsankawe   ^xsnkWk 
12247:(o)xsankawe/-wya  ?   Oxsnq'wyh) 
12267:(o)xsnirk  ?   Oysnyrkh)  =^xsnyrk(>1 
15933:(o)pxans   =>pxsn-,  py'ns-,  'py'rs- 
21453:2086  'xsn'qc  =>  'fsn'qc 
21455:2087  'xsn'm   M  y^tjJj^x* 
21464:oxsnam   ®*xsnduman   =»}Ysn}m,  xsn'm 
21470:2088  'xsn'w-   M  o^y^- 
21471:oxsnaw   (DAv.  xsnavaya-   =^xswndyy 
21476:2089  >xsnk-    M  Xii  <.j£iL  «L>  j 
21477:ox(a)sang   (xsnk)   ©pi.  -0  =»}Ysnk- 
21480:GMS  157,  511,  981,  1204;  f.adj.  >xsnk\  KG;  MSP 
21482:2090  'xsnkNv'k   S  J^ojfc 
21483:oxsankawe   Oxsnq'wyh)   -^ysnkWk 
21488:2091  'xsnq'wyh    M  **  ,xsnk)w,k 
21490:2092  >xsnyrk(,)   M  c-ou«Ai; 
21491:oxsnirk   -^ysnyrk^,  xsnyrq 
=== SOD_pages xsn
5656:           =»»5>kw                                                    Oxsn'qc) ©*fra-san
5816:                                                                  axsnam ©Av. xsnaoma- ^'xsn'm
5824:    (o)xsawanc =»xsywny(y), }xswny                                  =^xsnk-, xsnq-
5831:                                                                  (o)xsankawe ^xsnkWk
5837:723 ^s'y- B                 d>/c-*£~ ^J'^.M...                    (o)xsankawe/-wya ? Oxsnq'wyh)
5852:       (o)xsnirk ? Oysnyrkh) =^xsnyrk(>1                           VJ 6a, 1029; BBB plOl; Tales. 486.22; GMS 243
7394:       (o)pxans =>pxsn-, py'ns-, 'py'rs-
9815:                                                                    2086 'xsn'qc => 'fsn'qc
9817:     BSTi 175; Gersh. JRAS 1946,182                                 2087 'xsn'm     M                                       y^tjJj^x*
9823:        oxsnam ®*xsnduman      =»}Ysn}m, xsn'm                 2099 'xswndyy M                                          >y**-
9824:        forgiveness                                                 (s)xsunde ©<*xsnutaka
9827: 2088 'xsn'w- M                        o^y^-
9828:      oxsnaw (DAv. xsnavaya- =^xswndyy                         2100 'xswny M                                               j&
9832: 2089 >xsnk- M                       Xii <.j£iL «L> j                king, ruler
9835:      ox(a)sang (xsnk) ©pi. -0 =»}Ysnk-
9837:        GMS     157, 511, 981, 1204; f.adj. >xsnk\ KG; MSP     2102 >xsypt-    S => >xs>y|3t-
9838: 2090 'xsnkNv'k S                                J^ojfc        2103 »xsyc   M                   jjulT ^cjT ^qjulT ^<L^j < ^y*
9839:      oxsankawe Oxsnq'wyh) -^ysnkWk                                 axsic   ^'ksyc
9843: 2091 'xsnq'wyh       M ** ,xsnk)w,k                          2104 »xsy5 M                                  jiJL^l<^l<r,>U>
9844: 2092 >xsnyrk(,) M                         c-ou«Ai;                o/axse5
=== KNT xsnu
4128:TEXTS WITH NOTES AND TRANSLATION 139 26 išaiy : xSnuta : °° amiy : uta : màm : vas
4150:54 сіу : ° üxSnudiy : tya : partamtaty : asti
5338:z5nula- past pte. pass. ($71, 3242.1), cf. uzšnav-: zSnuta nsm. ‘satisfied’ DNb 26. |xsnutam) nsn. ‘heard’ DNb 53.
```


## [2026-09-06T20:38:16.638Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"2088 'xsn'w-\")\nprint(\"SOD leaf\",t.count('\\f',0,i), \"-> printed ~\", t.count('\\f',0,i)-66)\nseg=t.split('\\f')[t.count('\\f',0,i)]\nprint(seg[:300])\nk=open('KNT.txt',encoding='utf-8',errors='replace').read()\nj=k.find(\"z5nula- past pte\")\nleaf=k.count('\\f',0,j)\nprint(\"KNT leaf\",leaf,\"-> printed ~\",leaf-15)\nprint(k.split('\\f')[leaf][:400])\nEOF"
}
```


### [2026-09-06T20:38:18.378Z] TOOL RESULT

```
SOD leaf 148 -> printed ~ 82
                                                                                                                       'xty'k


  83
                                                                     happy
        oxsnam ®*xsnduman      =»}Ysn}m, xsn'm                 2099 'xswndyy M              
KNT leaf 205 -> printed ~ 190
 sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 5110, $122) DB 1.52.
azinav- vb. ‘hear, satisfy’ ($96): cf. Av. zšnav- ‘Genüge haben an’, adj. zínav- ‘Genüge leistend’, ріс. zšnůta-, sb. zínütay- ‘Zufriedenstellung’ (Bthl. AiW 557-60); apparently an extension of root zinà- ‘learn’ (cf. pIE *40- and *doy- ‘give’), with semantic development ‘learn, hear of, hear’, and ‘hear, hearken to,
```


## [2026-09-06T20:38:27.517Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nk=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in (203,204,205,206):\n    s=k[n]\n    nums=re.findall(r'\\b(1[6-9]\\d)\\b',s[:300])\n    print(\"leaf\",n,\"head:\",s[:120].replace('\\n',' '),\"| nums\",nums[:4])\nprint(\"=== leaf 205 full-ish\")\nprint(k[205][:1800])\nEOF"
}
```


### [2026-09-06T20:38:29.073Z] TOOL RESULT

```
leaf 203 head: ted by the OP writing. регу. of Iran. root *kas- (89.V, §87, $126, §146.II), = Skt. kaś- ‘be visible, appear, shine’ (so | nums []
leaf 204 head: , 66, 70f, 78f, 80, 91, 92; 3.1, 9, 11, 20, 21, 181 28, 29, 40f, 49f, 53, 54, 64, 69, 75, 76f, 83, 83f; 4.1, 3, 5, 11, 1 | nums ['181']
leaf 205 head:  sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 5110, $122) DB 1.52. azinav- vb. ‘hear, satisfy’ ($96): cf. | nums []
leaf 206 head: n, fall down’: [avagmat]a nsf. past pte. ($244) DSe 46f (conj. of Kent, cf. JAOS 54.46). рата + gam- ‘go forth’: paragma | nums []
=== leaf 205 full-ish
 sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 5110, $122) DB 1.52.
azinav- vb. ‘hear, satisfy’ ($96): cf. Av. zšnav- ‘Genüge haben an’, adj. zínav- ‘Genüge leistend’, ріс. zšnůta-, sb. zínütay- ‘Zufriedenstellung’ (Bthl. AiW 557-60); apparently an extension of root zinà- ‘learn’ (cf. pIE *40- and *doy- ‘give’), with semantic development ‘learn, hear of, hear’, and ‘hear, hearken to, satisfy’ (Lg. 15.171; ef. also Bv. TPS 1945.47-50). Hz. ApI 238-40 gives an impossible equation with Skt. éru- ‘hear’ (pIE
OLD PERSIAN
*flu-); Sen 247, 251, has wrong meanings. Р}.
sani, Acme 1.319-20, gives another etymology, -
See also uzsnav-.
z5nula- past pte. pass. ($71, 3242.1), cf. uzšnav-: zSnuta nsm. ‘satisfied’ DNb 26. |xsnutam) nsn. ‘heard’ DNb 53.
à + zínav-: dxSnautiy (§71, $122, $208) ‘satisfy’ DNb 24. āzšnavāhy 2d sg. subj. (§227.1) ‘satisfy’ DNb 29f. äzšnudiy 2d sg. ішу. ($208, §237.1) ‘hear’ DNb 54.
gaifa- sb. ‘(living) personal property, cattle’: Av. gaébü- ‘individual living being, pl. world; household, property’, РЫ. géhdn ‘world’ (from gen, pl.), to root pIE *g*ei- seen in OP jiv- (869, $101, $151). For varying interpretations, see Tm. Lex, 85, with lit. — ga26àm-cà (S89) asf. DB 1.65.
gaud- vb. ‘conceal’: Av. gaoz-, Skt. githati (§88). apa- + gaud- ‘conceal, hide away’: apagau- dayahy 2d sg. subj. (§227.1) DB 4.55, 51. apagaudaya 2d sg. inj. (5215, §224, §227.II, $237) DB 4.54. gaub- vb. ‘say’, mid. ‘call one’s self’ (§213): Sas. РЫ. gowét ‘he says’, NPers. goydd, inf. guftán: perhaps a -bh- extension of pIE root *gheu- seen with -s- extension in gauga- (q.v.; Ву. BSLP 31.2.70). gaubataiy mid. (42851) DB 2,21, 31, 51; 3.15, 59. agaubaté imt. mid. DB 1.84, 93; 2.66f; 3.35, 55 (written agauratà, 454.11), 89f; 4.82. agauba^ià 3d pl. imf. mid. ($28617) DB 293
```


## [2026-09-06T20:38:36.339Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nk=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in (189,190,191):\n    print(\"### leaf\",n); print(k[n][:600].replace('\\n',' ')); print()\nEOF"
}
```


### [2026-09-06T20:38:38.123Z] TOOL RESULT

```
### leaf 189
n., asn.); AÁuramazdü, АМ; ava (nsn.); avdkaram, avükaramca-; ucdram; uld, uta-; tya (nsn., asn.); dahydus; duvarayd; nat-; pati-; pasdva; уава; haw, hau-: Asl 12; DB 1.25 bis, 55, 87, 94; 2.24, 34, 40, 45, 54, 60, 68, 75, 79, 86, 90, 96; 3.6, 11, 17, 37, 441, 61, G6f, 87; 4.39, 46, 60, 64; DPd 28°; DPh 8, 10; DNa 50 (m° omitted, $52.VI), 52#, 544; DNb 13, 28, 28f, 31, 32f, 33, 48, 51, 52; DSe 51°, 52°; DSE 10, 19°, 20°, 58; Ds} 4°, 6°; DSk 5; DSI 4f; DSm 3°; D8s 7°; DSt 9°; DH 6, 8; Хра 15, 18f, 191; XPb 24, 29, 30; XPe 13 bis; ХРа 18f, 19; ХР 32, 38, 41, 45f, 47; XPg 14; XPh 32, 45, 58, 167 

### leaf 190
. Skt. apa, Gk. and, Lt. ab, Gt. af, Gm. ab, NEng. оў, off, pIE *apo. Used with vb. gaud- and in sbb. apaddna-, apa- niydka-; with suffix in apalara-, apara-. apataram adv. ‘farther off, far off’; nsn. of apatara-, which is apa- + comp. -fara- ($82, 5190.111), ef. Gk. adv. ётотіро. DNa 18; DSe 16f; XPb 25; XPh 16. apaddna- sb. ‘palace’: from apa- + déna- ($147.I) to root *dà-, cf. Skt. apadhá- ‘conceal- ment’, Gk. атоблк ‘storehouse’. For development in later Iranian, with ара- by secondary length- ening (but not OP appa-, cf. $130), see Henning, Trans. Philol. Soc. 1944.110n. apadünam asm. D*

### leaf 191
 formed like Gk. &exero to root *segh-, ёттєтө to root *pet- (JAOS 62.269; 855.IT, §103.I1). amala adv. ‘thence’: demonst. stem ama-, found (though rarely) in Skt., + adv. -tos, as in Skt. tátas ‘thence’, Gk. ёктоѕ ‘outside’, Lt. caelitus ‘from the sky’: Buck, Lg. 3.4-5; Jn. quoted by Gray, JRAS 1927.101: ef. Kent, JAOS 51.231. Hardly, with Gray, JRAS 1927.99-100, and Hz. ApI 65-6, the same as Skt. abl. asmat remade to *asmatas, with -tos ending. DPh 6, 7; DH 5, 6. отида, see maub-. ay- vb. ‘go’: Av. ay- (pres. aiti), Skt. i- (pres. éti), Gk. «о, Lt. it: conj., §208. Cf. also youviyd-. айу ($6
```


## [2026-09-06T20:38:52.926Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nk=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n,s in enumerate(k):\n    if 'LEXICON' in s[:300].upper(): print(\"leaf\",n,\"|\",s[:200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T20:38:54.597Z] TOOL RESULT

```
leaf 2 | � i тег. E EAD Мут OLD PERSIAN GRAMMAR TEXTS LEXICON BY ROLAND G. KENT Professor Emeritus of Indo-European Linguistics University of Pennsyloania AMERICAN ORIENTAL SOCIETY NEW EAV
leaf 4 | y whose courtesy tt appears here FOREWORD This volume has been prepared to meet the need for a comprehensive treatment of the Old Persian inscriptions; neither the latest collec- tions of texts, nor t
leaf 20 | gs and uses; fuller discussion will be found in the phonology and in the Lexicon, s.vv.: I. Place-Names: Asagarla ‘Sagartia’, a district of Media, with s in asa- from Ё if it means ‘stone’. Sikayawati
leaf 34 | ch problems must be settled by etymological comparison or by comparison with borrowings in other languages; but these are only problems relating to individual words or forms, not affecting the general
leaf 193 | t’). - LEXICON ч. Атах$аса- sb. ‘Artaxerxes’ (Т, son of Xerxes; П, son of Darius II; III, son of Artaxerxes II): Elam. ir-tak-Sa-a8-Sa, Akk; ar-tak-Sat-su, Gk. ’Aprakeptns (§29.n2, 530). From arta- ‘j
leaf 227 | ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1); see OP mar-, and cf. Hz. АрІ 249-51. тапа пзш. XPh 48, 55. marlahyá gsm. РВ 5.20, 36. EU: ET TORR ON | INS SEE cals l
```


## [2026-09-06T20:39:01.361Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in MON_part1.txt MON_part2.txt; do echo \"### $f $(grep -c '' $f) lines\"; grep -n 'قصر' $f | head -5; done"
}
```


### [2026-09-06T20:39:03.076Z] TOOL RESULT

```
### MON_part1.txt 99339 lines
6952:نماز مسافر» خلاف قصر است. 
10210:ارگبد: رئیس ارگ» رئیس قصرء کوتوال» 
11068:کاخ» کوشک» قصر 
11874:افزون» خواستن» طلب افزونی کردن. مقصر 
19435:ندارد و مشرف به حیاط است. قصرء کاش. 
### MON_part2.txt 94500 lines
12941:کردن بازداشتن. نماز قصر. نماز تا 
12942:قصر: نمازی کوتاه که در سفر خوانند یعنی 
12953:«مقصور» نامند. قصر ممکن است به وسئلة 
12955:فقط» تنها که آنها را ادات قصر گو بندء 
12956:صورت گیرد. قصر را به تقسیمات ذیل
```


## [2026-09-06T20:39:06.007Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '12900,12975p' MON_part2.txt"
}
```


### [2026-09-06T20:39:06.058Z] TOOL RESULT

```
فرد و مسطح که در قسمت خلفی تحتانی 
دبوارة بینی قرار دارد و تنها استخوان فرد 
صورت محسوب می‌شود. به شکل تيغة 
چهار گوشی است که دارای دو سطح و 
چهار کنار است. این استخوان جدار داخلی 
فوقانی‌سوراخ‌های بینی را بوجود 
می‌اورد؛ استخوان تیغه یی؛ ج. . قصات. 
قصباٌ کبری: (پز.) استخوانی است طویل و 
در بدن زوج است و در قسمت داخلی ساق 
پاقرار دارد و با استخوان نازکك نی 
استخوان‌بندی ساق پا را بوجود می آورد. اين 
استخوان سار درشت است و دارای بکك 
تنه و دو انتها است. تنه‌اش منشوری و سه 
سطح داخلی و خارجی و خلفی دارد و نیز 
دارای سه خط الر أس است که خط الر آس 
قدامی آن بسیار تیز و نمایان است و به شکل 
حرف 5است و آن را ستیغ درشت نی نامند. 
سطح فوقانی انتهای فوقانی این استخوان را 
طبق درشت نامند که با لقمه‌های استخوان 
ران مفصل می‌شو د. سطح تحتانی انتهای 


قصب‌انجیر فرهنگ فارسی معین ۱۱ 


(قاب) مفصل می‌شود و سطح داخی انتهای 
تحتانی برآمدگیی دارد بنام قوزک داخلی؛ 
درشت نی. 

فصد: ۵ (ع.] (مصل.) راه میانه رفتن. 
آهنگ چیزی کردن. ((مص.) مبانه‌روی. 
عزبمت. (.) اهنگك» ثیت. مقصود. فه قصد: 
قصدا و عمدا. به قصد آنکه: به منظور 
آنکه. قصد سوء: قصد بد. قصد ضروری: 
(فد.) هرگاه مبداً اول فعل تخیل به انضمام 
طبیعت يا مزاج باشد قصد ضروری می‌نامند 
مانند تنفس برای انسان که با آن منشأً آن 
قصد می‌باشد مع‌دلک عمل ضروری است. 
(فر لغا. سج. ۰ ۲۴.) 

رنف )6 کو ۶ ردنمع 
کردن بازداشتن. نماز قصر. نماز تا 
قصر: نمازی کوتاه که در سفر خوانند یعنی 
دو رکعت در صبح؛ دو رکعت در ظهر» دو 
رکعت عصرء سه رکعت در مغرت؛ دو 
رکعت در عشا. (عر.) انداختن نون آخر 
«مفاعیلن» و ساکن گردانیدن لام» جزوی را 
که این زحاف در آن واقع شده باشد مقصور 
گویند. (معا.) یا «حصرء اثبات حکم يا صفت 
است برای کسی يا چیزی به نحو انحصار و 
نفی حکم از غیر آن. کسی يا چیزی را که 
حصر برای آن صورت گرفته «مقصور فیه؛ 
و فعل با حالتی را که بدان اختصاص بافته 
«مقصور» نامند. قصر ممکن است به وسئلة 
یکی از ادات مانند: جزء الا غیر از» مگر 
فقط» تنها که آنها را ادات قصر گو بندء 
صورت گیرد. قصر را به تقسیمات ذیل 
قسمت کنند: قصر حقیقی: (معا.) آن است 
که اختصاص چیزی به چیز دیگر از روی 
حققت حقیقت باشد نه به ادعای متکلم. قصر 
اضافی: (معا) آن است که در وی اختصاص 
نسبت به قسمتی از اشیا معین است نه همة 
آنها. قصر صفت بر موصوف: (معا.) انحصار 


۱۳ فر هنک فارسی معین فصر 


سسکا سس سس 


حالتی و صفتی است بر کسی یا چیزی با 
بعکس؛ چنانکه در شواهد فوق آمده. ضح.- 
در انجا مراد از صفت و موصوف معنی 
دوع آن دو نست» بلکه مقصود از 
موصوف دات و مراد از صفت حالتی است
```


## [2026-09-06T20:39:11.583Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '12976,13040p' MON_part2.txt"
}
```


### [2026-09-06T20:39:11.630Z] TOOL RESULT

```
از حالات آن. بنابراین فعل و فاعل و 
مسندالیه و مسند در این مورد موصوف و 
صفتند. قصر افراد: (معا.) نست دادن بت 
صفت تنها است بر موصوف. قصر قلب: 
(معا.) آن است که صفتی را خلاف نظر 
مخاطب به موصوف سبت دهند. قصر 
تعسین: (معا.) آن است که مخاطب در 
انحصار چند صفت برای یک موصوف 
متردد باشد و گوینده با حصر یکك صفت 
بدان موصوف او را از تردید بیرون آورد. 
(دکتر صفا. آیین سخن. چا. چهارم ۲۱ - 
۳۸( 

قصر: 7 [ع.] ((.) کوشکک» کاخ شاهی؛ 
ج. . قصور. قصر سما: (اض. تشییهی) کوشکك 
آسمان. قصر دوازده دری: که شمان 
هشتم» فلکك البروج (به مناست دوازده 
برج). 

تصر: 2۳۲ [ع.] (مصل.) کو تاه بودن. 
(امص.) کو تاهی؛ مق. طول» درازی. 
قصری: آ-۸۰۳:(ص‌نسب.) ظرفی فلزی یا 
لعابی که در آن بشاب کنند. 

قصعه: (0-)2 ۲۸5 [ع. قصعه | (۱.) کاسه» 
بشقاب بز رگ ج. قصعات. قصع» قصاع. 
قصود. 50 [ع.] (امص.) (تص 1 صحت 
(همحو بری» تار یخ ۳ 7 ۲ ). 
قصور: تتادهر [ع.] (مص‌ل.) درمانده شدن؛ 
سست گشتن. باز ایستادن (در کار). (امص.) 
درماندگیء سستی. کوتاهی. خطاء کگناه. 
ضح.- بعضی بین «قصور» و «تقصیر» فرق 
گذاشته‌اند «قصوره به خطایی که از روی 


سهو سر ز ند اطلاق شود «تقصیر » به خطای 
هو ای : 

قسصهه: (ه)«عه [ع. قصه] (.) حکایت» 
داستان» سر‌گذشت. خبر. سخن. (حق. قد) 
مرافعه» دعوی. (قزوینی. یادداشتها 
۹ ) ج. . قصص. قصه برداشتن: «قصه 
رفع کر دن» به معنی دادخواهی و مرافعه نزد 
شاطای با اه ناف زین ات وطاهرا در 
قدیم عر ض‌حال را به اختصار می‌نوشتند و 
بالای چوبی نصب می‌کردند و در بیرون 
قصر بر منظر یادشاه با امیر می‌داشتند (از 
این ر و تعسر مزبور بش آمده است.) قصة 
کوتاه!ا: در وقتی گویند که خواهند مطلب را 
اجمالاً بیان کنند و سخن را به پایان رسانند؛ 
القصه. الحاصل. 

قصه خوان: «ق [ع. ف. قصه خواآننده] 
(ص‌فا.) کسی که قصه‌ها را از روی کتاب 
برای دیگران خواند. قصه بر داز» داستانسرا. 
قصه دراز کر دن: ۵(۲22-2) ۲-0۵ [ع. 
ف.| (مصل.) بسیار گفتن» سخن بی‌ایده 
هه (تی-.« (ع. ف. < 
قصه گو بنده] (ص. فا.) آنکه داستان گوید؛ 
ناقل. 

قشصی: (۲)] ۲۸5 [ع.] (ض.) دور شونده. 
دور؛ ج. اقصا(ء). 

قصید: ۵آدهر (ع.] (.) نيزة ش _
```


## [2026-09-06T20:39:23.817Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins kes-\"; grep -n -A12 '^kes-' AHD_watkins1985.txt | head -40\necho \"=== AHD kes 2\"; grep -n 'castrate\\|chaste\\|castellum' AHD_watkins1985.txt | head -10"
}
```


### [2026-09-06T20:39:23.881Z] TOOL RESULT

```
=== AHD watkins kes-
=== AHD kes 2
334:bher-2. To cut, pierce, bore. 1. Germanic *bordn in Old English borian, to bore: BORE}. 2. Germanic *baru-ga-, castrated pig, in Old English bearg, barg, castrated pig: BARROW’. 3. Germanic *bor-, perhaps in French burin, burin: BURIN. 4. O-grade form *bhor-d- in Latin fordre, to pierce, bore: FORAMEN; BIFORATE, PERFORATE. 5. Per- haps Greek pharunx, throat (< “a cutting, cleft, pas- sage”): PHARYNX. 6. Slavic *bor- in Russian borot’, to overcome: DUKHOBOR. See extension bhreu-'. [Pok. 3. bher- 133.]
512:CICHLID. 3. Greek khelidw6n, khelidén, the swallow: CELANDINE. [Pok. ghel- 428.] ghel-2. To shine; with derivatives referring to colors, bright materials (probably “yellow metal”), and bile or gall. I. Words denoting colors. 1. Suffixed form *ghel-wo- in Germanic *gelwaz in Old English gealu, yellow: YELLOW. 2. Suffixed variant form *ghlé-ro- in Greek khioros, green, greenish yellow: CHLORO-; CHLORITE!. 3. Suffixed variant form *ghlo-wo- in Greek khloos (< *khlo-wo-s), green color: CHLOASMA. 4, O-grade form *ghol- in Russian zola, ashes (from their color): PODZOL. II. Words denoting gold. 1. Suffixed zero-grade form *ghl-to- in Germanic *gultham, gold, in: a. Old English gold, gold: GOLD; b. denominative verb *gulthjan in Old English gyldan, to gild: GILD!; c. Middle Dutch gulden, golden: GUILDER, GULDEN; d. Old Norse gulinn, golden, akin to the possible source of Middle English gollan, yellow flower: GOWAN. 2. Suffixed o-grade form *ghol-to- in Polish zloto, gold: zLoTy. 3. Suffixed full-grade form *ghel-i- in the unknown Iranian source of Syriac zarnikd, orpiment: ARSENIC. III. Words denoting bile. 1. Suffixed o-grade form “ghol-no- in Germanic *gallon-, bile, in Old English gealla, gall: GALL!. 2. Suffixed o-grade form *ghol-& in Greek kholé, bile: CHOLE-, CHOLER, (CHOL- ERA); ACHOLIA, MELANCHOLY. 3. Suffixed full-grade form *ghel-n- in Latin fel, bile: FELON?. IV. A range of Germanic words (where no preforms are given, the words are late creations). 1. Germanic *glaimiz in Old English glém, bright light, gleam: GLEAM. 2. Middle High Ger- man glimsen, to gleam, akin to the source of Middle English glimsen, to glimpse: GLIMPSE. 3. Swedish dialec- tal glinta, to shine, akin to the source of Middle English glent, a glint: GLINT. 4. Swedish glimra, akin to the source of Middle English glimeren, to glimmer: GLIM- MER. 5. Old Norse glitra, to shine: GLITTER. 6. Old English glisnian, to shine: GLISTEN. 7. Middle Dutch glisteren, to shine: GLISTER. 8. Germanic *glasam, glass, in Old English gles, glass: GLASS, GLAZE. 9. Germanic *glaz- in Middle Low German glaren, to glisten, akin to the source of Middle English glaren, to glitter, stare: GLARE!. 10. Icelandic glossi, a spark, perhaps akin to the source of GLoss!. 11. Old High German glanz, bright: GLANCE2. 12. Old Norse gléggr, clear-sighted: GLEG. 13. Germanic *gladaz in Old English gled, shining, joyful: GLAD. 14. Germanic *gleujam in Old English gléo, sport, merriment: GLEE. 15. Old English gléd, ember: GLEED. 16. Germanic *gié- in: a. Old English gléwan, to glow: GLow; b. Norwegian dialectal glora, to gleam, stare, akin to the probable source of Middle English gloren, to gleam, stare: GLOWER; C. Old Norse glotta, to smile (scornfully), perhaps akin to the source of GLOAT. 17. Germanic *glé-m- in Old English glém, twilight: GLOAMING. 18. Possibly distantly related is Germanic *glidan, to glide, in: a. Old English glidan, to slip, glide: GLIDE; b. Old French glier, to glide: GLISSADE; c. Old High German glitan, to glide: GLITCH; d. derivative Germanic “glidén- in Old English glida, kite (< “gliding, hovering bird”): GLEDE. 19. Middle Low German glibbe- rich, slippery, possibly akin to the source of GLrB. [Pok. 1. &hel- 429.] ghel-. To cut. 1. Germanic “galdjan, to castrate, in Old Norse gelda, to castrate, and geldingr, a castrated ani- mal: GELD!, (GELDING). 2. Germanic *gulti- in Old Norse gyltr, a sow (< “castrated pig”): GiLT?. [Pok. 2. ghel- 434.] gheldh-. To pay. Only in Germanic and Slavic. 1. Ger- manic *geldam, payment, in: a. Old English geld, gield, payment, service: GELD?; DANEGELD, WERGELD; b. Old High German gelt, payment, reward: GELT!. 2. Germanic *geldan, to pay, in Old English gieldan, to pay, yield: YIELD. 3. Germanic *geldjam, payment, contribution, hence an association founded on contributions, a crafts- men’s guild, in Old Norse gildi, guild: GuILD. [Pok. ghel-t6 436.] ghelegh-. A metal. Possible root of Greek khalkos,
623:(SCARCE). 3. Greek karpos, fruit: -cARP, CARPEL, CARPO-, -CARPOUS. [In Pok. 4. sker- 938.] kers-'. Dark, dirty. 1. Suffixed form *ker(s)-no- in Rus- sian chérnyi (feminine chérnaya), black: CHERNOZEM. 2. Suffixed zero-grade form *krs-no- in Sanskrit krsna-), black, dark: KrisHNa. [Pok. kers- 583.] kers-2. To run. Zero-grade form *krs-. 1. Latin currere (past participle cursus), to run: CORRIDOR, (CORSAIR), COURANTE, COURIER, COURSE, CURRENT, CURSIVE, CUR- SOR, CURULE; CONCOURSE, CONCUR, DECURRENT, DIS- COURSE, EXCURSION, HUSSAR, INCUR, INTERCOURSE, OCCUR, PERCURRENT, PRECURSOR, RECOURSE, RECUR, succor. 2. Suffixed form *krs-o- in Gaulish carros, a wagon, cart, in: a. Latin carrus, a two-wheeled wagon: CAR, CAREER, CARGO, CARICATURE, CARIOLE, CAROCHE, (CARRY), CHARGE, CHARIOT; b. Latin carpentum, a two- wheeled carriage: CARPENTER. [Pok. 2. fers- 583.] kert-. To turn, entwine. I. Zero-grade form *krt-. 1. Suf- fixed form *krt-i- in Germanic *hurdiz, wickerwork frame, hurdle, in: a. Old English hyrdel, hurdle, frame: HURDLE; b. Old French hourd, fence, hurdle, scaffold: HOARDING. 2. Suffixed form “*krt-sti- in Germanic *hur- sti- in Old High German hurst, thicket: Horst. II. Per- haps suffixed variant form *krot-i- in Latin crdatis, wickerwork hurdle: CRATE, GRATE?, (GRID), GRIDDLE; (GRIDIRON). [Pok. kert- 584.] kes-'. To scratch. 1. Germanic *hezd6 in Old English heordan, coarse parts of flax: HARDS. 2. Extended form *kseu- in Greek xuein, to scrape: XYSTER. 3. Nasalized form *ks-n-eu- in: a. Germanic *snaww- in Old Norse snéggr, “close-cropped,” perhaps akin to the source of snuG!: b. Latin novdcula, razor: NOVACULITE. [Pok. kes- 585.] kes-2. To cut. Variant kas-. 1. Suffixed form *kas-tro- in: a. Latin castrare, to castrate: CASTRATE; b. Latin cas- trum, fortified place, camp (perhaps “separated place”): CASTLE. 2. Suffixed form *kas-to- in Latin castus, chaste, pure (< “cut off from, free of, faults”): CASTE, CHASTE; CASTIGATE, INCEST. 3. Suffixed (stative) form *kas-é- in Latin carére, “to be cut off from,” lack: CARET. 4. Ex- tended geminated form *kasso- in Latin cassus, empty, void: (CASHIER), QUASH. [Pok. hes- 586.] kes-°. To order. Suffixed 0-grade form *kos-mo- in Greek kosmos, order: COSMOS; MACROCOSM, MICROCOSM. keu-' Also ekeu-. To perceive, see, hear. O-grade form *akou-. 1. Extended form *kous- in: a. Germanic *haus- Jan in (i) Old English hieran, to hear: HEAR (ii) Old English he(o)rcnian, to harken: HEARKEN; b. suffixed form *9-kous-yo- in Greek akouein, to hear: ACOUSTIC. 2. Variant *skou- in: a. Germanic *skauwon in (i) Old English scéawian, to look at: SHOW (ii) Flemish scauwen, to look at: SCAVENGER; b. Germanic *skaunjaz in Mid- dle Dutch schoon, beautiful, bright (< “conspicuous, attractive”): SCONE; Cc. Germanic *skauniz in Old Eng- lish sciene, bright, sheen: SHEEN. [Pok. 1. keu- 587.] keu-?. Base of various loosely related derivatives with assumed basic meaning “to bend,” whence “a round or hollow object.” I. Extended forms *keub-, *keup-. 1. Ger- manic *haup- in: a. Old English héap, heap: HEAP; b. Dutch hoop, heap, troop: FORLORN HOPE. 2. Germanic *hupp-, to leap (by first bending the legs), in Old English hoppian, to hop: HoP!. 3. Germanic *Aupiz in Old Eng- lish hype, hip: H1P!. 4. Zero-grade form *kup-, vessel, in: a. suffixed form *kup-s- in Greek kupselé, chest, hollow vessel: CYPSELA; b. long-vowel form *kip- in (i) Ger- manic *Aifi- in Old English hyf, hive: HIVE (ii) suffixed form *kip-a in Latin cupa, tub, vat: CUPOLA, CUPULE; c. expressive form *kupp- in Late Latin cuppa, drinking vessel: cup. 5. Zero-grade form *kub- in: a. Greek kubos, cube: CUBE; b. suffixed form *kub-@- in (i) Latin cubdre, to lie down on (< “to bend down, prostrate”): COUVADE, COVEY, CUBICLE; CONCUBINE, INCUBATE, SUCCUBUS (ii) Latin cubitum, elbow: CUBIT; Cc. nasalized form *ku-m-b- in (i) Latin -cumbere, to lie down, recline: ACCUMBENT,
938:skep-. Also kep-. Base of words with various technical meanings such as “to cut,” “to scrape,” “to hack.” 1. Germanic *skap- in: a. Old English gesceap (ge-, collective prefix; see kom), form, creation (< “cutting”): SHAPE; b. Old English -scipe, state, condition (collective suffix): -sHIP; c. Dutch -schap, “-ship,” condition (collec- tive suffix): LANDSCAPE. 2. Germanic ablaut variant *skOpo-, “thing cut out,” container, in Middle Dutch and Middle Low German schdépe, bucket for bailing water: scoop. 3. Germanic *skaftaz in Old English sceaft, rod of a spear: SHAFT! 4, Germanic expressive form *skabb- in: a. Old English sceabb, a scab, scratch: sHaBBy; b. Old Norse skabb, a scab: scaB. 5. Variant form *skabh- in: a. Germanic *skaban in (i) Old English sceafan, to scrape, pare away: SHAVE (ii) Old High German skaban, to scrape: SAPSAGO; b. Latin scabere, to scrape: SCABIES; c. suffixed form *skabh-ro- in Latin scaber, rough (< “scratched”’): SCABROUS; d. Greek skaphé, boat (< “thing cut out”): SCAPHOID; BATHYSCAPH. 6. Variant form *skap- in Latin scapula, shoulder blade (used as a tool for scraping): SCAPULA. 7. Variant form *kap- in: a. Latin capd, castrated cock: CAPON; b. Late Latin capuldre, to cut: SCABBLE. 8. O-grade form *kop- in: a. suffixed form *kop-yd- in Germanic *hapjo, a cutting tool, ax, sickle, in (i) Old High German hdppa, happa, sickle, akin to the Germanic source of Old Provencal apcha, small ax: PIOLET (ii) Medieval Latin hapia, ax, and Old French hache, small ax: HASH!, HATCHET; NUT- HATCH, QUEBRACHO; b. suffixed form *kop-yo- in Greek koptein, to strike, cut: COMMA; APOCOPE, SARCOPTIC MANGE, SYNCOPE; C. Russian kopat’, to hack, with de- rivative kop’e, lance, in kopeika, kopeck: KOPECK. 9. Pos- sibly zero-grade variant form *skup(h)- in Greek skuphos, a cup (but more likely of obscure origin): SCYPHISTOMA, SCYPHOZOAN. [Pok. 2. (s)kep- 931.] sker-!, Also ker-. To cut. I. Basic forms *sker-, *ker-. 1. Germanic *skeran in Old English scieran, sceran, to cut: SHEAR. 2. Germanic *skeraz in: a. Old English scéar, plowshare: SHARE?; b. Old English scearu, scaru, portion, division (but recorded only in the senses of “fork of the body,” “tonsure”): SHARE!. 3. Germanic *skér- in: a. *skér-6- and *sker-ez- in Old English scéar, scissors: SHEARS; b. compound *skér-berg-, “sword protector,” scabbard (see bhergh-') in Old High German scarberc, scabbard, akin to the possible Germanic source of Anglo- Norman escaubers, scabbard: SCABBARD. 4. Germanic *skur- in Old Norse skor, notch, tally, twenty: SCORE. 5. Germanic suffixed form *skar-jam in Old Norse sker, low reef (< “something cut off’’): scaR?. 6. Suffixed o-grade extended form *skord-o- in Germanic *skardaz in Old English sceard, a cut, notch: SHARD. 7. Extended form *skerd- in suffixed zero-grade form *skrd-o- in Germanic *skurtaz in: a. Old English scort, sceort, “cut,” short: SHORT; b. Old English scyrte, undergarment (< “cut piece”): SHIRT; c. Old Norse skyrta, shirt: SKIRT. 8. Germanic extended form *skerm- in: a. Old High German skirmen, to protect, akin to the source of Old French eskermir, to fight with a sword, fence: SKIRMISH; b. Middle Dutch scherm, shield: SCREEN. 9. Variant form *kar- in Latin caré (stem carn-), flesh: CARNAGE, CARNAL, CARNASSIAL, CARNATION, CARNIVAL, CARRION, CARUNCLE, CHARNEL, CRONE; CARNIVOROUS, INCAR- NATE. 10. Suffixed o-grade form *kor-yo- in Latin co- rium, leather (originally “piece of hide”): CORIACEOUS, CORIUM, CUIRASS, CURRIER; EXCORIATE. 11. Suffixed zero-grade form *kr-to- in Latin curtus, short: CURT, CURTAL, KIRTLE. 12. Suffixed o-grade form *kor-mo- in Greek kormos, a trimmed tree trunk: cor. 13. Suffixed o-grade form *kor-i- in Greek koris, bedbug (< “cutter”): corREopsis. II. Extended roots *skert-, *kert-. 1. Zero-grade form *krt- or o-grade form *kort- in Latin cortex, bark (< “that which can be cut off”): CORTEX; DECORTICATE. 2. Suffixed form *kert-snd- in Latin céna, meal (< “portion of food”): CENACLE. III. Extended root
```


## [2026-09-06T20:39:39.671Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB 771 / sane\"; grep -n -E '^\\s*77[01]\\.|šāne|sane .Kamm|Kamm' HUB.txt | head -10\necho \"=== HUB 509\"; grep -n -E '^\\s*50[89]\\.' HUB.txt | head\necho \"=== NYB husnud/sanak\"; grep -n -i 'husnut\\|hušnūd\\|šānak\\|šōr\\b' NYB_vol2_glossary.txt | head\necho \"=== LKT alcazar/kasr\"; grep -n -i 'kasr\\|alcazar\\|alcázar' LKT.txt | head\necho \"=== DEV alcazar\"; grep -n -i 'alcazar\\|kaçr\\|qasr' DEV.txt PHN.txt | head"
}
```


### [2026-09-06T20:39:39.795Z] TOOL RESULT

```
=== HUB 771 / sane
2783:770. Dazu paz. Sdnzdah Min. 61. 186, bal. LW. sanzdah,
5795:vasama velum' (Vis u Kamm 856, 1 nach v. Stackelberg)
8419:zd. xsvaSf idg. svek^s ; s^wa *Kamm* = gr. xra^ ; ^'^^
=== HUB 509
1992:508. Np. x^aS gut, schon, angenehm' = zd. "^hvasi- (skr.
2005:509. Das Wort wird gewohnlich so geschrieben, als ob die
2187:508. Die Etymologie von dastilr 'Vorschrift', paz. dastur
=== NYB husnud/sanak
=== LKT alcazar/kasr
2634:1117.  Ar.  kasr:
9966:alcazar  1117
=== DEV alcazar
DEV.txt:2122:'  Dans  les  lan[jues  hispaniques,  souvent  i'adjonclion  de  la  voyelle  ne  dé- place  pas  Taccenl;  ainsi  ^«xiJI  al-qasr,  cliâleaii  lorl,  devient  «/cazor,  *jir lamr,  dalle,  devient  Umaras,  etc.
PHN.txt:1113:ALCAÇAR et ALCAZAR, n. pr. (a.)
PHN.txt:10196:Alcaçar et Alcazar, n. pr. (a.) 17
```


## [2026-09-06T20:39:43.737Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT 1117\"; sed -n '2630,2645p' LKT.txt\necho \"=== PHN alcazar\"; sed -n '1108,1125p' PHN.txt\necho \"=== HUB 508-509 context\"; sed -n '1985,2015p' HUB.txt\necho \"=== HUB 8419 context\"; sed -n '8410,8425p' HUB.txt"
}
```


### [2026-09-06T20:39:43.818Z] TOOL RESULT

```
=== LKT 1117
1115.  Tk.  kaskawal:
'Eine  Art  Käse'  [Kelekian  Kämüs  928b; wohl  aus  it.  caccio  cavallo];  hieraus  rum. ca§caval  'Quarkkäse'.
1116.  Sskr.  käsmiras:
Kasmir  ist  eine  Stadt  und  ein  größeres Gebiet  im  nordwestlichen  Indien,  wo Schals  in  vorzüghcher  Qualität  her- gestellt wurden.  Hieraus  engl,  cashmere, ndl.  cachemir,  dtsch.  Kaschmir  (früher Kasimir);  it.  casimiro,  sp.  casimiro,  pg. Casimir a,  frz.  cachemire;  russ.  kazmir, kasemir,  poln.  kazmirek,  cech.  kazimir. [Bern  SlEtWb  496.
1117.  Ar.  kasr:
'Schloß,  Burg'  [aus  lat.  Castrum,  gr. Kdaxpov  ZDMG  LI,  316];  hieraus  mit ar.  Art.  sp.  pg.  alcäznr  'dass.,  Kastell'; pg.  cagarete  'Teil  des  Zugnetzes  mit Sack'(?);  it.  cdssero  'kleines  Schloß',  siz. cässaru  'Hauptstraße'.  [In  Palermo  und in  anderen  Städten  nennt  das  Volk  den Hauptkorso  so].  [DE  90.  Eguilaz  135. ML  6895.  ZfromPh  XXV,  503.  GrS VociSic  232.
1118.  Ar.  kassäb :
'Metzger'  [vom  Vb.  kasaba  'schneiden', s.  hier  Nr.  1108],  ebenso  tk.;  hieraus rum.  casap  'dass.',  casapie  'Metzgerei', bulg.  kasap,  kasapiii,  kasab  'Metzger', serb.  kasap,  kasapin  'dass.',  bulg.  serb. kasapnica  'Schlachtbank'.  [Bern  SlEt Wb  492.
1119.  Mal.  kasuwäri:
[Pijn  143:  soewa7-i]  'Ein  großer  strauß- ähnlicher VogeP,    Casuarius  galeatus,
Tk.  kasyk.]
90
der  auf  den  Inseln  Ozeaniens  heimisch ist.  Das  Wort  ist  in  alle  europäischen Sprachen  übergegangen:  engl. cassowari/, schwed.  dän.  kasiiar,  ndl.  casnaris,  ka- suaris,  dtsch.  Kasuar  (früher  Kossebares) ; sp.  casoar,  casiiel,  pg.  casicar,  it.  casua- rio,  frz.  casoar;  russ.  kazuaru.  —  Wegen der  Ähnlichkeit  seiner  Blätter  mit  den Federn  des  Kasuars  heifst  ein  im  ma- layischen  Archipel  wachsender  Baum schon  mal.  pöhon  kasuwärl  'Kasuar- baum', ebenso  lat.  Casuarina  L.,  engl. casuarina.  frz.  casuarine.  [Devic  DEt 88.    MMM  14.    JAOS  XVII,  125/128.
1120.  Tk.  kasyk:
'LöfleP  [vom  Stamme  kas  'reiben,  schar- ren, graben'  Vämbery  TktEtWb  S.  20, Nr.  22 II];  hieraus  serb.  kasika  'dass., Holzlöffel'.
1121.  Tk.  kat:
=== PHN alcazar
il a quarante-quatre kilomètres de tour. Près de ce lac, en
181 a, le général français Suchel remporta une victoire qui
lui valut le titre de duc d'Albuféra. — On trouve encore en
espagnol albuhera, et en portugais albufeira, avec le sens de
lac ou lagune, ce qui confirme l'origine arabe de ces mots.
ALCAÇAR et ALCAZAR, n. pr. (a.)
jjaJk}\ [alqas'r] le château, dénomination commune à divers
châteaux forts ou palais élevés par les Maures, et par suite
à quelques villes. L'une d'elles , appelée Alcaçar Saghir ou le
Petit Château, est située en Afrique, dans le royaume de Fez;
elle fut bâtie , vers la fin du xii* siècle , par Yakoub almoudjahed
almansour, dans l'endroit le plus serré de la côte du détroit
de Gibraltar, entre Ceuta et Tanger, vis-à-vis de Tarif, h
quatre lieues de la côte d'Espagne. L'autre, nommée Alcaçar
KUnr ou le Grand Château, se trouve également dans le royaume
de Fez, un peu à l'est d'Elarich (^jJ^^jJI), dont on a fait
Laroche par corruption.
ALCADE, s. m. (a.)
=== HUB 508-509 context
in Stiicke*. Das zugehdrige np. xurda *klein, kleines
Stiick' kann mit lat. curitis (— gr. ^agxig geschoren'
nach Brugmann, Grdr. I, 238, zu ksl. hrattiku nach
Fick, Wb.'* I, p. 385), dem ein np. *A:»rrf oder *Aarrf
entsprechen wiirde, nicht vermittelt werden. Horn's
Bemerkungen tiber das anl. x aus k sind verfehlt.
Vgl. Fr. Mtiller, WZKM. 7, 373.
508. Np. x^aS gut, schon, angenehm' = zd. "^hvasi- (skr.
sval^Or-) sch5naugig? Moglich, aber nicht sicher.
Vgl. bal. vas 'siiss, angenehm, gut, glucklich, fr5hlich*.— 58 —
Zur Aussprache bemerkt Triimpp (Ueber den Accent
etc. p. 240), dass jetzt in Nordpersien x6s, im Siiden
xus gesprochen wird, stets mit kurzem Vokal. Wo
es bei Firdusi lang erscheint, ist nicht xiJIs (Sal.
Shuk. p. 12) zu lesen sondern x'^a^ N old eke).
Die entsprechenden afgh. Worter sind nach Geiger
(Etym. und Lautl. des Afgh. p. 31) wohl alle entlehnt:
xd$ *suss', xus, x^Q^ 'erfreut, ergotzt, angenehm, lieb-
lich\ Doch konnte x^ *su8s' (davon x^a^Sdql 'siiss
werden* etc.) auch echt sein.
509. Das Wort wird gewohnlich so geschrieben, als ob die
altere Aussprache x^asnud =^ paz. x^asnud (Min. Gl.
169) ware. Lag neben ^huxsnUta- *wohl befriedigt',
ein ^x^axsnuta- selbstzufrieden ?
511. Die Worter fur *Blut* gehoren wohl zusammen, wie
aber sind sie lautgesetzlich mit einander zu vereinigen?
Gerade np. ocun ist am schwersten mit zd. vohuni-
wegen des Anlauts zusammenzubringen ; die afgh. und
pamir Formen lauten wenigstens wie das Zendwort
mit V an. Si vend, ftn *Blut* wird aus xun (vgl. fask
'trocken* = np. xusk) oder vun (vgl. fisagl *Hunger =
=== HUB 8419 context
das Verhaltniss von zd. fstdna- zu np. pistan 'Brust', siehe
oben p. 41.
§ 128. Idg. pk^ —^ zd. fs -^- arm. np. s im Anlaut:
subcLn 'Hirt' = zd. "^fsupCLna-, arm. spet *Hirt' = zd.
*fsupaiti' von zd. fsu- 'Vieh' in Kompos. (= idg. ph^u-) ^=
selbstandigem pasu- (idg. pek^u-).
M Vgl. tran»oxanisch ixseS bei N o 1 d e k e , mand. Gram. Einl. p.l3.— 236 —
§ 129. Idg. kh = iran. ap. s = np. s:
kas 'AchselhQhle' = zd. kasa-, skr. kaksa-: sas *sechs'
zd. xsvaSf idg. svek^s ; s^wa *Kamm* = gr. xra^ ; ^'^^
*Beir = zd. ^cisa-, arm. tasem 'behaue'; tast 'Becken' = zd.
tasta- ; neS 'Spitze, Stachel', nestar *Lanzette*, skr. neksana- ;
casm 'Auge* = zd. dasman-, skr. caksus ; arm. LW. sahapet
'Schutzgeist* (5. Jhd.) = zd. soid-rapaiti- ; sen *Dorf * =
zd. -say ana, Wrzl. k^si wohnen'.
Dazu auch as 'Bruhe' H. 29, Osam *Trank' H. 30,
```


## [2026-09-06T20:40:00.089Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ qasr\"; grep -n -i 'qasr\\|Qaṣr\\|castrum' FVQ.txt | head\necho \"=== AFA/AKD qasr\"; grep -n -i 'kasr\\|qasr\\|castrum' AFA.txt AKD.txt | head\necho \"=== MON خسیدن\"; grep -n 'خسیدن' MON_part1.txt MON_part2.txt | head\necho \"=== MON شانه comb\"; grep -n 'شانه:' MON_part1.txt MON_part2.txt | head -5\necho \"=== MON شور\"; grep -n 'شور:' MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-06T20:40:00.228Z] TOOL RESULT

```
=== FVQ qasr
15001:(Qasr). 
15009:correct in deriving it from Lat. castrum 9 through Gk. Kacrrpw and 
=== AFA/AKD qasr
AFA.txt:8224:Anm. 3 zu jüd. KHlf p = xa^rpov castrum , deren genauere
=== MON خسیدن
MON_part1.txt:21384:بخسیدن: 25-1420 [- بسخیدن] 
MON_part1.txt:29565:یخسیدن: ۵225-127 (مصل.) چین چین 
MON_part1.txt:73157:خواهد رفید» زفیده) تر شدن» خسیدن» 
=== MON شانه comb
MON_part2.txt:4586:فال شانه: قالی است که از شانه برگیرند. فال 
MON_part2.txt:9776:قاب شانه: جای شانه» شانه‌دان. قاب 
MON_part2.txt:18520:کاشانه: ()۱:22 (- کاشان - معر. 
MON_part2.txt:36518:گوشانه: (قد. 0()826-)۱5112۸ان آقس. گوشه) 
MON_part2.txt:62281:تصل شانه: (ش) من اشت که ات آن 
=== MON شور
MON_part2.txt:9796:قاب ‌شور: 7-50۲ [- قاب شوی | (ص‌فا) 
MON_part2.txt:23688:کشور: ۲۵۵۷۲ ۱- کشخور] (.) هر بخش از 
MON_part2.txt:23690:زدن کشور: زیر و زبر کردن آن. 
MON_part2.txt:49630:محشور: ۱۹1 [ع. ۰] (امف.) ) گرد آمده با 
MON_part2.txt:53057:مرده‌شور: 01۰-۲ [- مر ده‌شوی ] مر ده‌شور
```


## [2026-09-06T20:40:08.927Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON شانه headword\"; grep -n 'شانه' MON_part2.txt | grep -n 'په\\.\\|پهل' | head -5\ngrep -n '^شانه\\|شانه: ' MON_part1.txt MON_part2.txt | head -5\necho \"=== search شانه with کاکل/گیسو\"; grep -n 'شانه.*گیسو\\|گیسو.*شانه' MON_part1.txt MON_part2.txt | head -5\necho \"=== RCH خسیدن\"; grep -n 'khasīdan\\|khasidan\\|to chew' RCH.txt | head -10"
}
```


### [2026-09-06T20:40:09.065Z] TOOL RESULT

```
=== MON شانه headword
MON_part2.txt:4586:فال شانه: قالی است که از شانه برگیرند. فال 
MON_part2.txt:9776:قاب شانه: جای شانه» شانه‌دان. قاب 
MON_part2.txt:18520:کاشانه: ()۱:22 (- کاشان - معر. 
MON_part2.txt:27411:شانهٌ گوسفندی بدست گیرد و بر در خانه‌ها 
MON_part2.txt:27413:شانه مالد تا از آن صدای غرغری یدید آید 
=== search شانه with کاکل/گیسو
=== RCH خسیدن
```


## [2026-09-06T20:40:17.003Z] TOOL CALL #43: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T20:40:17.010Z] TOOL RESULT

```


```


## [2026-09-06T20:40:20.253Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D8%B5%D8%B1",
 "prompt": "Give the Arabic etymology of قَصْر (qaṣr) \"castle, palace\" — is it from Latin castrum / Greek kastron via Aramaic? Also give the Persian section for قصر."
}
```


## [2026-09-06T20:40:21.686Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/castle",
 "prompt": "Give the full etymology of castle, and any mention of castellum, chateau, castrum, and the PIE root."
}
```


## [2026-09-06T20:40:23.084Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%B4%D9%86%D9%88%D8%AF",
 "prompt": "Give the Persian etymology of خشنود (xošnud) — Middle Persian and Avestan forms and the root."
}
```


## [2026-09-06T20:40:24.556Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%86%D9%87",
 "prompt": "Give the Persian etymology of شانه (šâne) \"comb\" — Middle Persian form, Proto-Iranian, PIE root."
}
```


## [2026-09-06T20:40:25.736Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D9%88%D8%B1",
 "prompt": "Give the Persian etymology of شور (šur) \"salty\" — Middle Persian form, Proto-Iranian and PIE root. Also anything on شوربا."
}
```


### [2026-09-06T20:40:27.457Z] TOOL RESULT

```
# Etymology of قَصْر (qasr) - Castle/Palace

Yes, the word traces back to Latin through intermediary languages. According to the Wiktionary entry:

**Etymology path:** The noun comes "From Aramaic _קַצְרָא_ (qaṣrā), from Latin _castrum_." It's cognate with Classical Syriac, Hebrew, and Byzantine Greek forms of the same root.

The entry shows this word spawned numerous descendants across Romance languages (Spanish _alcázar_, Portuguese _alcácer_), Mediterranean languages (Italian _cassero_), and beyond, demonstrating its widespread adoption from the original Latin military term.

---

## Persian Section

Unfortunately, the provided content does not include a dedicated Persian language section for قصر. The document shows Persian listed among the 14 languages with entries for this word, but the actual Persian content is not present in the excerpt provided. The text cuts off after the extensive Arabic and Hijazi Arabic conjugation tables.
```


### [2026-09-06T20:40:29.974Z] TOOL RESULT

```
# Etymology of Castle

**Origin Path:**
The word "castle" traces back through Old North French *castel* to Latin *castellum*, meaning "a castle, fort, citadel, stronghold; fortified village." This Latin term was "a diminutive of *castrum* 'fort,'" which derives from Proto-Italic *\*kastro-* meaning "part, share."

**Key Terms:**

- **Castellum**: The Latin foundation referring to fortified structures and military strongholds
- **Castrum**: The parent Latin term for "fort," used in military contexts; its plural *castra* meant "military encampment, military post"
- **Chateau**: The Modern French descendant of the same Latin root
- **PIE Root**: The chain ultimately connects to the Proto-Indo-European root *\*kes-*, meaning "to cut," likely relating to the notion of something "cut off" or fortified

**Historical Development:**
In late Old English, *castel* initially meant "village" (from biblical Vulgar Latin usage), later evolving to signify "large building or series of connected buildings fortified for defense." The Latin *castrum* entered Old English as *ceaster*, forming the *-caster* and *-chester* place name endings still visible in English geography today.
```


### [2026-09-06T20:40:30.479Z] TOOL RESULT

```
# Persian Etymology of خشنود

Based on the Wiktionary entry, here's the etymological background:

**Middle Persian Origin:**
The Persian adjective خشنود (xošnud) is "inherited from Middle Persian" with the form shown as (hwšnwt' /⁠hušnūd⁠/, "contented, happy").

**Meaning:**
The word means "content" or "satisfied" in modern Persian, maintaining its sense of emotional contentment from its Middle Persian ancestor.

**Note on Avestan:**
The provided content does not include information about an Avestan form or root. The etymological chain documented here only traces back to Middle Persian, without reference to earlier Indo-European linguistic ancestors like Avestan.
```


### [2026-09-06T20:40:30.597Z] TOOL RESULT

```
# Etymology of شانه (šâne) "Comb"

**Middle Persian form:** šʾnk' (šānag) — meaning "comb" or "pitchfork"

**Proto-Iranian:** *fšā- — meaning "to comb"

**Proto-Indo-European root:** *peḱ- — meaning "to pluck (wool, hair)"

The word traces back through these linguistic layers, with the Middle Persian form "šānag" deriving from the Proto-Iranian verbal root for combing, which ultimately connects to the ancient PIE root referring to the action of plucking fibers.
```


### [2026-09-06T20:40:34.834Z] TOOL RESULT

```
# Persian Etymology of شور (šur) "salty"

## Middle Persian Form
The Middle Persian equivalent is **swr** (pronounced šōr), representing a direct ancestor of the modern Persian term.

## Proto-Iranian and PIE Roots
According to the etymology section, this term derives from **Proto-Iranian *sauraH** ("salty"), which ultimately traces back to the **Proto-Indo-European root *súHros** ("sour, acidic, salty").

The word was borrowed into Persian from Parthian **šwr** /šōr/, which itself descended from these ancient roots.

## Cognates
Related forms appear across Indo-Iranian languages, including Northern Kurdish şor/sûr, Central Kurdish swêr, Baluchi šōr, and Pashto x̌arǝ́na.

## شوربا (šōrbā/šurbâ)
This derived term combines شور (šōr, "salty") with Persian با (bā), literally meaning "salty [dish]." It refers to a savory broth or soup, representing a common Persian culinary preparation.
```


## [2026-09-06T20:40:54.747Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/castrate",
 "prompt": "Give the etymology of castrate, and of chaste/chastity if mentioned, including PIE root *kes- \"to cut\"."
}
```


## [2026-09-06T20:40:55.740Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/chateau",
 "prompt": "Give the etymology of chateau, and of chastity if present on the page."
}
```


## [2026-09-06T20:40:57.508Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BE%CF%8D%CF%89",
 "prompt": "Give the Ancient Greek etymology of ξύω (xuō) \"to scrape\", the PIE root, and any derived terms like ξυστήρ (xystēr)."
}
```


## [2026-09-06T20:40:59.041Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BE%CE%B1%CE%AF%CE%BD%CF%89",
 "prompt": "Give the Ancient Greek etymology of ξαίνω (xainō) \"to card, comb wool\" — the reconstructed preform and PIE root."
}
```


### [2026-09-06T20:41:00.288Z] TOOL RESULT

```
# Etymology of Castrate and Related Words

**Castrate (verb, 1610s):**
Derived from "castration" or Latin *castratus* (past participle of *castrare*). The Latin verb supposedly stems from a noun *castrum* meaning "knife, instrument that cuts." The figurative sense of "destroy the strength or vitality of" appears earlier, in the 1550s.

**Chaste/Chastity:**
These words are linked to the same Proto-Indo-European root as castrate.

**PIE Root *kes- ("to cut"):**
This ancient root "might form all or part of" numerous English words including castrate, castle, castigate, and chaste. The root appears across multiple language families: Sanskrit *sastra-* (knife), Greek *keazein* (to split), Latin *carere* (to be cut off from), and Old Church Slavonic *kosa* (scythe).

All these terms ultimately trace back to the fundamental concept of cutting or severing, whether literally or metaphorically.
```


## [2026-09-06T20:41:00.630Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/s%C3%A1uraH",
 "prompt": "Give the reconstruction, meaning, descendants (especially Middle Persian/Parthian šōr and Persian شور) and the PIE source."
}
```


### [2026-09-06T20:41:01.456Z] TOOL RESULT

```
# Etymology of Chateau and Chastity

## Chateau
The word "chateau" comes from French *château*, which derives from Old French *chastel* (12th century). It traces back to Latin *castellum* meaning "castle." The term has been used in English since around 1739 to describe "large stately residence in the country, manor-house."

## Chastity
According to the page, chastity's etymology connects to the Proto-Indo-European root *\*kes-* meaning "to cut." The word is listed among entries linked to this root, suggesting it shares linguistic ancestry with castle and related terms, though the page does not provide explicit etymology details for chastity itself beyond this root connection.
```


### [2026-09-06T20:41:03.694Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T20:41:04.907Z] TOOL RESULT

```
# Ancient Greek ξύω (xuō) Etymology

**Etymology Chain:**
The word ξύω derives from Proto-Hellenic *ksuyō, which comes from Proto-Indo-European *ksuyéti, ultimately from the PIE root *ksew- meaning "to scrape, shave, scratch."

**PIE Root:**
"*ksew-* ("to scrape, shave, scratch")" provides the fundamental semantic foundation for this verb family.

**Cognates:**
Related terms appear in Latin, including *novācula* and *saucius*, demonstrating the root's Indo-European distribution.

**Derived Terms:**
- ξόανον (xóănon) - wooden image
- ξύλον (xŭ́lon) - wood
- ξυστός (xŭstós) - scraped/polished
- ξύστρα (xŭ́strā) - scraper

**Related Terms:**
- ξαίνω (xaínō)
- ξέω (xéō)

The semantic development traces from the basic action of scraping through specialized applications like planing, polishing, and engraving, with derived terms extending into materials (wood) and tools (scrapers).
```


### [2026-09-06T20:41:07.128Z] TOOL RESULT

```
# Ancient Greek Etymology of ξαίνω

**Reconstructed Preform:** Proto-Hellenic *\*ksəňňō*

**PIE Root:** Proto-Indo-European *\*ksn̥-ye⁄o-* meaning "to scratch; to comb, card"

According to the Wiktionary entry, the verb traces back through Proto-Hellenic to a Proto-Indo-European root related to combing and scratching actions. The PIE root *\*kes-* also connects to related forms like *\*késr̥* ("comb"), which shares cognates across various Indo-European languages including Latin *sentis* ("thorn") and Irish *cíor* ("comb").
```


## [2026-09-06T20:41:14.379Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/s%C3%A1uras",
 "prompt": "Proto-Iranian reconstruction for \"salty/sour\" — give the form, meaning, PIE source and descendants (Persian شور, Parthian, Baluchi, Kurdish)."
}
```


## [2026-09-06T20:41:14.680Z] TOOL CALL #55: WebSearch

```json
{
 "query": "Persian شور šōr \"salty\" etymology Proto-Iranian *sūra- Parthian Hasandust"
}
```


### [2026-09-06T20:41:16.407Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T20:41:23.662Z] TOOL RESULT

```
Web search results for query: "Persian شور šōr "salty" etymology Proto-Iranian *sūra- Parthian Hasandust"

Links: [{"title":"شور - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B4%D9%88%D8%B1"},{"title":"شوره - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B4%D9%88%D8%B1%D9%87"},{"title":"Parthian - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/Parthian"},{"title":"Persian Etymology Research Papers - Academia.edu","url":"https://www.academia.edu/Documents/in/Persian_Etymology"},{"title":"Persia - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/Persia"},{"title":"Category:Parthian terms derived from Proto-Iranian - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Parthian_terms_derived_from_Proto-Iranian"},{"title":"Parthian language","url":"https://en.wikipedia.org/wiki/Parthian_language"},{"title":"Suristan","url":"https://en.wikipedia.org/wiki/Suristan"},{"title":"Proto-Iranian language","url":"https://en.wikipedia.org/wiki/Proto-Iranian_language"}]

Based on the search results, I found relevant information about the etymology of Persian شور (šōr, "salty"):

Persian شور was borrowed from Parthian šōr, possibly from Proto-Iranian *sauraH ("salty"), from Proto-Indo-European *súHros ("sour, acidic, salty"). 

The word is cognate with Northern Kurdish şor, sûr, Central Kurdish سوێر (swêr), Baluchi شور (šōr, šowr), Baluchi سور (sowr), Harzani سور (sür) and Pashto ښرنه (x̌arǝ́na, "saline").

However, the search results did not contain specific information about "Hasandust" that was mentioned in your original query. The results do confirm the etymological chain from Proto-Iranian through Parthian into Persian for this word related to "salty."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T20:41:29.000Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D9%88%D8%B1%D9%87",
 "prompt": "Give the Persian etymology of شوره (šure) \"saltpetre, salty ground\" — its relation to شور and the Middle Persian/Proto-Iranian forms."
}
```


## [2026-09-06T20:41:30.414Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/f%C5%A1%C4%81nah",
 "prompt": "Proto-Iranian reconstruction for \"comb\" — form, meaning, PIE source, descendants (Middle Persian šānag, Persian شانه)."
}
```


## [2026-09-06T20:41:31.079Z] TOOL CALL #58: WebSearch

```json
{
 "query": "Middle Persian šānag \"comb\" Persian شانه etymology Proto-Iranian *fšāna- PIE *peḱ-"
}
```


### [2026-09-06T20:41:33.091Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T20:41:33.730Z] TOOL RESULT

```
# Etymology of شوره (šure)

**شوره** derives from Parthian *šōrag*, which is cognate to Middle Persian sōrag ("salty land"). The word was borrowed into Persian from these earlier Iranian languages.

By surface analysis, the term breaks down as: **شور** (šur, meaning "salty") + **ـه** (-e, a suffix), creating a transparent morphological structure in Persian.

The Arabic شورج (šawraj) represents a related Iranian borrowing into that language, demonstrating the term's broader Indo-Iranian heritage across regional languages and historical periods.
```


### [2026-09-06T20:41:38.139Z] TOOL RESULT

```
Web search results for query: "Middle Persian šānag "comb" Persian شانه etymology Proto-Iranian *fšāna- PIE *peḱ-"

Links: [{"title":"شانه - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%86%D9%87"},{"title":"(PDF) The Origins of Middle Persian Zamān and Related Words: A Controversial Etymological History","url":"https://www.academia.edu/35233437/The_Origins_of_Middle_Persian_Zam%C4%81n_and_Related_Words_A_Controversial_Etymological_History"},{"title":"A concise review of the Iranian calendar","url":"https://arxiv.org/pdf/astro-ph/0409620"},{"title":"Persian Online – Grammar & Resources » Middle Persian","url":"https://sites.la.utexas.edu/persian_online_resources/history-of-the-language/middle-persian/"},{"title":"Middle Persian literature","url":"https://en.wikipedia.org/wiki/Middle_Persian_literature"},{"title":"Middle Persian language | Britannica","url":"https://www.britannica.com/topic/Middle-Persian-language"},{"title":"Middle Persian","url":"https://en.wikipedia.org/wiki/Middle_Persian"},{"title":"Iran (word)","url":"https://en.wikipedia.org/wiki/Iran_(word)"}]

Based on the search results, I found relevant information about the etymology you're asking about:

The Persian word شانه (šānah, "comb") comes from Middle Persian šānag ("comb; pitchfork"), which derives from Proto-Iranian *fšā- ("to comb"), ultimately from Proto-Indo-European *peḱ- ("to pluck (wool, hair)"). 

This etymological chain shows how the word evolved from its Proto-Indo-European root through Proto-Iranian to its modern Persian form.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T20:41:44.357Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/FFD/FFD_pages.txt',encoding='utf-8',errors='replace').read()\nsegs=t.split('\\f')\nprint(\"segs\",len(segs))\nfor i,s in enumerate(segs):\n    if 'خوشید' in s or 'خشنود' in s:\n        m=re.search(r'\\[pdf page (\\d+)\\]',s)\n        print(\"seg\",i,\"tag\",m.group(1) if m else None)\n        print(s[:900]); print('-----')\nEOF"
}
```


### [2026-09-06T20:41:46.056Z] TOOL RESULT

```
segs 115
seg 56 tag 57
[pdf page 57]
فعلهای فارسی دری
خوردن
خورد + فارسی میانه ۷۵7۵4 + ایرانی باستان ۷۷۵۲-1۵*. برای 2 آراست.
: خور + فارسی میانه 5۷۵7 < ایرانی باستان ۴*3۵۲-۵. برای 8 -> آرای.
و 3۷/8۲ به معنی (خوردن» و «نوشیدن» هر دو به کار رفته‌اند.
خوشیدن
«خوشید» مادةٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
خوش « فارسی میانه 355 < ایرانی باستان 8۸۵05-8*. برای ۵ -> آرای. ريشةٌ 1205 به
معنی «خشک شدن» است.
واژةٌ «خشک» از ريشهٌ ۳203 گرفته شده است. صورت فارسی ميانةٌ آن 1031 است. از
ایرانی باستان 8۵5-2*. 1805 صورت ضعیف ريشه و 1۵ پسوند است.
دادن
داد < فارسی میانه 434 < ایرانی باستان 43-12*. برای "18 > آراست. ريشهٌ 45
به‌معنی «دادن» است. در ایرانی باستان دو ريشةٌ 48 وجود داشته است: ۱-به معنی
«دادن»» ۲- به معنی «نهادن». «نهادن» از 13 به معنی «نهادن)» آمده است. >
نهادن.
ده < فارسی میانه 42 < ایرانی باستان ۵4۵۵5". 4202 ماد مضاعف است از 43.
داشتن
داشت + فارسی میانه 4381. به جای 4381 باید 417۵ می آمد از 4۲-12* ایرانی
-----
```


## [2026-09-06T20:42:03.797Z] TOOL CALL #60: Bash

```json
{
 "command": "ls site/pages/261.jpg 2>/dev/null; pdftoppm -f 261 -l 261 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg261 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T20:42:05.982Z] TOOL RESULT

```
site/pages/261.jpg
total 4396
drwx------ 2 sfmqrb sfmqrb    4096 Sep  6 16:42 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     132 Sep  6 16:34 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   96095 Sep  6 16:39 av_box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  113038 Sep  6 16:40 av_box3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  103258 Sep  6 16:39 av_box.png
-rw-rw-r-- 1 sfmqrb sfmqrb   95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22433 Sep  6 16:39 ffd61_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73736 Sep  6 16:39 ffd61.png
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb  105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb  346511 Sep  6 16:39 root262.png
-rw-rw-r-- 1 sfmqrb sfmqrb 2985742 Sep  6 16:39 skt1882.txt
```


## [2026-09-06T20:42:09.017Z] TOOL CALL #61: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg261.png"
}
```


### [2026-09-06T20:42:09.359Z] TOOL RESULT

```

```


## [2026-09-06T20:42:09.357Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T20:42:21.048Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\nsegs=t.split('\\f')\nprint(\"segs\",len(segs))\nfor w in ['شانه','خشنود','شور ','قصر']:\n    hits=[]\n    for i,s in enumerate(segs):\n        if w in s:\n            m=re.search(r'\\[pdf page (\\d+)\\]',s); hits.append((i,m.group(1) if m else None))\n    print(w,hits[:12])\nEOF"
}
```


### [2026-09-06T20:42:22.770Z] TOOL RESULT

```
segs 545
شانه [(12, '13'), (21, '22'), (45, '46'), (104, '105'), (169, '170'), (176, '177'), (181, '182'), (358, '359'), (371, '372'), (403, '404')]
خشنود []
شور  [(5, '6'), (10, '11'), (24, '25'), (28, '29'), (31, '32'), (270, '271'), (383, '384')]
قصر [(470, '471')]
```


## [2026-09-06T20:42:25.960Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (358,371,383,270):\n    s=t[i]\n    for ln in s.split('\\n'):\n        if 'شانه' in ln or 'شور' in ln:\n            print(i,'|',ln.strip()[:250])\n    print('----')\nEOF"
}
```


### [2026-09-06T20:42:27.503Z] TOOL RESULT

```
358 | چم این واژه در هلندی: شانه‌ی اسب.
----
371 | شانه (به چم "استخوان کلف" و "کثیف) / ۳۷۳
371 | و اروپایی نشان (شاید) آورده شده است. ضناً این احتمال هم وجرد دارد که "شانه" از هند و اروپایی ۸1807۰
----
383 | شور / ۳۸۵
----
270 | پا شور 9
----
```


## [2026-09-06T20:42:30.537Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(\"=== ARY seg 371 (printed 372/373)\"); print(t[371][:2500])\nprint(\"=== ARY seg 383\"); print(t[383][:1800])\nEOF"
}
```


### [2026-09-06T20:42:32.201Z] TOOL RESULT

```
=== ARY seg 371 (printed 372/373)
[pdf page 372]
اج وو وود دما
شانه (به چم "استخوان کلف" و "کثیف) / ۳۷۳
پسگشت‌ها آش‌ هرد ند 3 (813188) :5028 ۱۷۸
1 ۹ 8002 بق 2520 ۸00
3 (817885) رامیت نا برهان قاطع + ۱۳۳۰
پهلری (/۲اتنم۳): 5۳20۷۸ ,517201۸6 انگلیسی (7ل8(/05): 0710
بلوچی (اتلعتانلم8): ۰ 81120060 ,817۸4 دانمارکی (0۸2۷/34): 3 دراه ادن
افغانی (پشتر) (/4۳0/4۸4): 05۸ سوئدی (817820/374): 50008۸ ا
برنانی 02870): کلتشا5 ,اتمه نروژی (/۸/0775014): 3 را 8 هن
لانین (/47): شهاناقف؟٩‏ ,قاتا هلندی (7ل07): 3 دای اش
فرانسه (7ح/۳52): ۵۳۸5
اسپانیایی (8۳۸(/]5): 3۸ پسگشت‌ها اراد گرا ادا
ایتالیایی (97 ۳4 5۶۸3۸ 5 ۸0090
پرتغالی (ظ۳087001052: ۰ 3188۸21۸ 0 (5130110538) ۰ . مهد
گونیک (0077712): 315 9 (ا۲ن2۸۲) بالط
ایسلندی کهن (507210410 2ا0): یه ها
۱ 8۸ات50 2 (5هفآ58-5 نمی
فریزی کهن (انفاکلق7 0ا۵): 90712588 53 (88011253) 002/5
آلمانی کهن (05204۸ 0[4اط صا0): 8 (8130171053) :7
: 500178۸ بفااکنانا50 برهان قاطع + ۳۳۰
ِ آلمانی (/(05294): ادا اش فرهنگ معین +" ۳
و انگیشیگهن (نتولزه‌زرع صله): 500120 لفت‌نامه دهخدا: ۱۳۰۷
بادداشت: 1 ۲
۱- رابطه‌ی میان: واژه‌های ایرانی و دیگر واژه‌های این فهرست احتمالی است و بهمین دلیل در جلر واجریشه‌ی هند
و اروپایی نشان (شاید) آورده شده است. ضناً این احتمال هم وجرد دارد که "شانه" از هند و اروپایی ۸1807۰
(سانسکریت:-۱517۳11 اوستایی: -15118۳۳1 آلبانی: 7ن81) باشد. (624:۳0720۸390)
۲- 07/1088 ریشه‌ی واژه‌های ژرمی اب فهرست را "ناشناخته" می‌داند.
۳ چم این واژه در یونانی: کج بیل» بیل باغبانی. :
چم این واژه در زبان لاتین؛ چاقر,
۰ ۰
ار ۰

=== ARY seg 383
[pdf page 384]
شور / ۳۸۵
0605۵ ۷362۴ ,0(23800) روسی (7ل8951): زد باب لا
فرانسه (۳88۸67): ۲0۲۲۸۵ چکه (2807): 2
اسپانیایی (/8۳۸۸//5): ا ا زان اه اسلوا کی (8-01420): 7۳ (۲0)
ایتالپایی (/(ال7): لا اد اشنا ندرا لیتوانی (۸ا هلاب 7لل):
رومانی (2/4۸م(/): ان ان اه 71 ,۳۸۰213157
پرتغالی (۳087701-282: ۰ ۳0۲۲0۴8 تونی (لتی) (/77/142هل): 727
گرتبکد (0077412): ۸ ایرلندی کهن (57ل5/ 01):
1 ایسلندی کهن (/5240/0/0۸/14 0۵): 7 ,6۸37 ,۰031۸۸4
۸ ۲۸۸۸ آلبانی (/۸2المقلم: 077
آلمانی کهن (/(6572۸1۸ 0(4لز صا0):
آف32 ,0۷73۷8 پسگشت‌ها 5
آلمانی (087804۸00): رنه 6 ۶005900
انگلیسی گهن (800180 صا0): و56 0۷ اتمه
۷7 ,۲۸2۷/۸۵ 7 (۲0۲۲۸17۴۵) +:05۸(15
انگلیسی (8(/0/5): 0 :025 ۸4۸
دانمارکی (۷184ل0۸): 0 9 (۴8۲۵۵۲2۴) ,ا12 (4(0۷)
سوئدی (9820154): ۳۸ 10 ملظ
نروژی (0/08۷501۸۸: دزن دک 8 (۲0۲) َ :01008
دی (01770): لدنوندها 5 (۵۷() وراد نج
اسلاوی کهن (4۲70ا5 #6نابل 2ل0): 6 (85600(128) ۸04/۸۸0
1 برهان قاطع + ۱۳۹۸
مّ
لهستانی (۳0/7534): 2۸
یادداشت: َ
واژه‌ی انگلیسی 2۸8 (انگلیسی کهن:01(881۸۸۲) نیز از همین واجریشه است. بازگشت به: دانتن ۰
اش 1
| مانکایس مروازای ارس ملگ
پهلری (1الل۳۸): ۸6 ,8508 لیتوانی راب7 560871 ,ت86
کردی (68/0154): ,81178 لنونی (لتی) ((7714): ۰ 53607 ,8761771
سانسکریت (5۸۸5807): رانا ۰
یونانی (6524ق07): ۸ ,2۷0
یی
```


## [2026-09-06T20:42:48.130Z] TOOL CALL #65: WebSearch

```json
{
 "query": "Persian \"خسیدن\" meaning dictionary Dehkhoda خاییدن chew"
}
```


## [2026-09-06T20:42:50.199Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/kes-",
 "prompt": "Give the PIE root *kes- reconstruction(s): meaning(s), whether there is a \"to cut\" root and a \"to scratch/comb\" root, and their descendants (Latin castrare/castrum/castus, Greek ξαίνω, etc.)."
}
```


### [2026-09-06T20:42:54.976Z] TOOL RESULT

```
Web search results for query: "Persian "خسیدن" meaning dictionary Dehkhoda خاییدن chew"

Links: [{"title":"https://dehkhoda.ut.ac.ir/en/dictionary","url":"https://dehkhoda.ut.ac.ir/en/dictionary"},{"title":"Dehkhoda Dictionary","url":"https://en.wikipedia.org/wiki/Dehkhoda_Dictionary"},{"title":"Dehkhoda Dictionary Institute","url":"https://en.wikipedia.org/wiki/Dehkhoda_Dictionary_Institute"},{"title":"معنی خاییدن | لغت‌نامه دهخدا","url":"https://www.vajehyab.com/dehkhoda/خاییدن"},{"title":"Dehkhoda Persian Dictionary - App Store - Apple","url":"https://apps.apple.com/us/app/dehkhoda-persian-dictionary/id1257192673"},{"title":"Dehkhoda Persian Learners Dictionary - Dehkhoda Lexicon Institute and International Center for Persian Studies","url":"https://dehkhoda.ut.ac.ir/en/book/18/dehkhoda-persian-learners-dictionary"},{"title":"The Great Persian Dictionary - Dehkhoda Lexicon Institute and International Center for Persian Studies","url":"https://dehkhoda.ut.ac.ir/en/book/29/the-great-persian-dictionary"},{"title":"Ali-Akbar Dehkhoda","url":"https://en.wikipedia.org/wiki/Ali-Akbar_Dehkhoda"},{"title":"Dehkhoda Lexicon Institute and International Center for Persian Studies","url":"https://dehkhoda.ut.ac.ir/en"},{"title":"لغت‌نامهٔ دهخدا The Encyclopedic Dictionary of the Persian Language (Dehkhoda Dictionary)","url":"https://www.iranbooks.net/product/11614/%D9%84%D8%BA%D8%AA%D9%86%D8%A7%D9%85%D9%87-%D8%AF%D9%87%D8%AE%D8%AF%D8%A7-The-Encyclopedic-Dictionary-of-the-Persian-Language-Dehkhoda-Dictionary"}]

Based on the search results, I found information about the Persian word خاییدن (khāyidan) in the Dehkhoda Dictionary:

خاییدن (khāyidan) means "to soften with teeth" or "to chew". It can also be translated as "mastication" (مضغ) and "chewing" (جویدن).

The search results show the entry from Vahehyab, which provides definitions based on the Dehkhoda Dictionary, including classical Persian literary examples from poets like Roudaki and Ferdowsi that illustrate the word's usage.

However, I should note that the search results did not return specific information about the word خسیدن (khesidan) that you also mentioned in your query. If you'd like information about that particular word or its relationship to خاییدن, please let me know and I can conduct an additional search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-06T20:42:56.964Z] TOOL RESULT

```
# PIE Root *kes- Reconstruction

## Primary Meaning
The root *kes- carries a single core meaning: **"to scrape, comb"** according to Wiktionary's reconstruction.

## Single Root, Not Multiple
The evidence presented does not support distinct "to cut" versus "to scratch/comb" roots. The documented *kes- encompasses scraping and combing activities, with extensions producing terms related to hair, fibers, and grooming implements.

## Key Descendants

**Germanic extensions:**
- Proto-Germanic *hazdaz ("hair") and *hezdǭ ("flax fibers")

**Balto-Slavic:**
- Lithuanian kàsti; Proto-Slavic *česàti ("to scratch, comb")
- Proto-Slavic *kosà ("hair, braided hair")

**Greek:**
- Ancient Greek ξέω (xéō, "to shave, carve, smooth, polish")

**Celtic:**
- Old Irish cír ("comb")

**Albanian:**
- kezë ("woman's head-dress, bonnet, hair-net")

## Regarding Latin Terms
The webpage does not discuss Latin castrare, castrum, or castus in connection with *kes-. These etymologies would require consultation of additional sources beyond this reconstruction entry.
```


## [2026-09-06T20:43:04.126Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/castrum",
 "prompt": "Give the Latin etymology of castrum (and castellum, castrare, castus if mentioned) — the reconstructed PIE/Proto-Italic source and what de Vaan says."
}
```


## [2026-09-06T20:43:05.889Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://www.vajehyab.com/?q=%D8%AE%D8%B3%DB%8C%D8%AF%D9%86",
 "prompt": "Does the Persian word خسیدن exist in any of these dictionaries (Dehkhoda, Moein, Amid)? What does it mean?"
}
```


### [2026-09-06T20:43:09.931Z] TOOL RESULT

```
Yes, خسیدن exists in the Dehkhoda dictionary. According to the entry, it means "خاییدن" (to soften by chewing under the teeth). The dictionary notes indicate this is a colloquial term from Shushtar with etymological references to classical Persian texts like the Sharafnama-ye Maniri.
```


### [2026-09-06T20:43:10.037Z] TOOL RESULT

```
# Latin Etymology of Castrum

**Proto-Italic and PIE Sources:**

The word derives from Proto-Italic *\*kastrom*, which comes from Proto-Indo-European *\*ḱes-* ("to cut, cut off, separate") plus the suffix *\*-trom*.

**De Vaan's Analysis:**

According to Michiel de Vaan's *Etymological Dictionary of Latin and the other Italic Languages* (2008), the root combines a cutting/separating concept with an instrumental suffix, producing a term for a fortified position—essentially "a place cut off or separated."

The word is cognate with Sanskrit शस्त्र (śastrá, "cutting tool, sword"), reflecting the shared Indo-European origin.

**Related Terms:**

While *castellum* is mentioned as a derived term from *castrum*, the page does not provide separate etymologies for *castrare* or *castus*.
```


## [2026-09-06T20:43:20.509Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%A7%DB%8C%DB%8C%D8%AF%D9%86",
 "prompt": "Give the Persian etymology of خاییدن (xāyidan) \"to chew\" — Middle Persian, Proto-Iranian, PIE root."
}
```


### [2026-09-06T20:43:26.329Z] TOOL RESULT

```
# Etymology of خاییدن (xāyidan)

Based on the Wiktionary entry, here's the etymological path:

**Proto-Indo-European Origin:** The word derives from PIE "*k(ʷ)end-" or "*k(ʷ)enHd(ʰ)-"

**Proto-Indo-Iranian Stage:** It evolved into "*kʰād-" according to Derksen's analysis.

**Persian Development:** This proto-form ultimately yielded the modern Persian verb خاییدن (xāyidan), meaning "to gnaw; to chew."

The entry notes cognates supporting this lineage: Sanskrit खाद्/खादति (khād/khādati, "to chew, to bite"), Ancient Greek κνώδων (knṓdōn, "sword spikes"), and Khotanese khays- ("to drink"), all reflecting the shared Indo-European root concerned with consuming or biting actions.
```


## [2026-09-06T20:43:41.169Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D9%82%D8%B5%D8%B1|page 261 Kes 1, Arabic/Persian qasr < Aramaic qasra < Latin castrum\" \\\n \"https://www.etymonline.com/word/castle|page 261 Kes 1, castle < castellum < castrum < PIE *kes- to cut\" \\\n \"https://www.etymonline.com/word/castrate|page 261 Kes 1, castrate/chaste under PIE *kes- to cut\" \\\n \"https://www.etymonline.com/word/chateau|page 261 Kes 1, chateau < OF chastel < L castellum\" \\\n \"https://en.wiktionary.org/wiki/castrum|page 261 Kes 1, Latin castrum < Proto-Italic *kastrom < PIE *kes- (de Vaan)\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D8%B4%D9%86%D9%88%D8%AF|page 261 Kes 2, Persian xosnud < MP husnud\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%86%D9%87|page 261 Kes 2, Persian sane comb < MP sanag < PIr *fsa- < PIE *pek-\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D9%88%D8%B1|page 261 Kes 2, Persian sur salty < Parthian sor < PIr *sauraH < PIE *suHros (sour)\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D9%88%D8%B1%D9%87|page 261 Kes 2, Persian sure < Parthian sorag\" \\\n \"https://en.wiktionary.org/wiki/%CE%BE%CF%8D%CF%89|page 261 Kes 2, Greek xuo scrape < PIE *ksew-, derivative xyster\" \\\n \"https://en.wiktionary.org/wiki/%CE%BE%CE%B1%CE%AF%CE%BD%CF%89|page 261 Kes 2, Greek xaino < *ksn-ye/o- (Nourai's ksnio)\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/kes-|page 261 Kes 2 root, PIE *kes- to scrape, comb\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D8%A7%DB%8C%DB%8C%D8%AF%D9%86|page 261 Kes 2, Persian xayidan to chew < PIIr *khad-, not *kes-\" \\\n ; do\n  url=\"${u%%|*}\"; note=\"${u#*|}\"\n  python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -1\ndone"
}
```


### [2026-09-06T20:43:45.295Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/851e1e414670f737.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4e508691eb1b48e7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/035f5273ea38749f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/99cb55999679275a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0acd8b16355a1556.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/df4e52e22771427c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f85d98d11e954350.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a86edaf21e6e0921.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cd8d90149b656804.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/49dd90084a93381f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b615fc72008632ed.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/604973b4b663f8e1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ccbdf43b60a5d316.txt
```


## [2026-09-06T20:43:49.847Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.vajehyab.com/?q=%D8%AE%D8%B3%DB%8C%D8%AF%D9%86\" --note \"page 261 Kes 2, Dehkhoda s.v. خسیدن = خاییدن (Shushtar dialect)\" 2>&1 | tail -2; sed -n '1,40p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T20:43:52.468Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3c23652f52469e15.txt
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
```


## [2026-09-06T20:44:04.202Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 pages file\"; ls incoming/WLD/\npython3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nsegs=t.split('\\f')\nprint(\"segs\",len(segs))\nfor i,s in enumerate(segs):\n    if re.search(r'castr[oa]|kastrom|castrare',s) and re.search(r'\\bkes|ḱes|kes-',s):\n        m=re.search(r'\\[pdf page (\\d+)\\]',s); print(\"seg\",i,m.group(1) if m else None)\nEOF"
}
```


### [2026-09-06T20:44:06.005Z] TOOL RESULT

```
=== WLD Bd1 pages file
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
segs 895
seg 456 None
```


## [2026-09-06T20:44:08.547Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\ns=t[456]\nprint(s[:3500])\nEOF"
}
```


### [2026-09-06T20:44:10.264Z] TOOL RESULT

```
     Nicht iiberzeugend vergleicht Siitterlin IF. 25, 62 unter Annahme von
idg. *kel(e.i)p- auch aisl. hllfa „beschirmen" (s. lieip-).


kes- „schneiden“.
     Ai. qusati           ,  f asti „schneidet, metzgt, metzelt", casta- „niedergemetzelt",
gasfra-       n.          „schneidendes Werkzeug, Messer, Dolch", casd- m. „Schlacht-
messer".
     Gr. (Fiekl 3 54, I 4 424)                               neat, to     „spalte“,             evy.smos „leicht            zu   spalten",
y.eagvov , Axt, Schusterahle"
              ;
                               (Formans wie bei oyJnagvov oder nach diesem,
s. *sqer-ep- „schneiden“), y.etcov Ptc. Praes. (wohl nach Schulze Qu. ep. 434

in    y.ewv    — *xe<xcov zu bessern                              ;   y.ea-   = ai. casi- in casi-iyati Fut., Bechtel
Lexil. 144; es liegt dann im Gr. nur die set-Basis vor, denn xeoxqov, xeozgog,
xeozog gehoren                          zu xevzeco   ,
                                                             s.   kent- "stechen",                und gegen die Deutung von
ay.eoyai          als             *n-x£oofiai „chirurgisch                        einsehneiden",               s.   iak- „heilen“).   Mir.
cm .Speer" *kestd Fickll 85; wohl gesichert, trotz Thurneysen beiBoisacq
       ,
                              (          ,
                                                         4

425 Anm. 1). Sehr unsicher ags .loss, „Zweig. SchoBling" (Zupitza Gutt. 184;
mnd. liar „Werkzeug zum Scharfen der Sense", liarcn ,,scharf sein, scharfen"
s. dagegen unter koi- „scharfen, wetzen“); desgleichen anord. lies f. „Wirbel-

zapfen in einem Spannriemen", norw. Iirsjc ,,aufrechtstehendes Gitterwerk
zu Trocknen von Heu oder Korn" (Fick III 4 86, Falk-Torp u. hesje)\
 ebenso       aksl. ko-a „Sichel, Sense"                               (/.-   aus k- nach Meillet Et. 178, Msl. 9, 374
 durcli    Diss. gegen das ausl. -.s-? bezweifelt                          von Berneker 581, der darum
 Bezzenbergers BB.                           12, 239          und Wiedemanns BB. 28, 15 mich nicht iiber-
 zeugende Yerbindung mit *qoksa, lat. coxa offen                                                      lafit.    — Aksl. socha „Kniip-
 pel", oso'iti „abscindero" gelidrt zu scq- „schneiden“).
      Sicberer e-Yokalismus                         in       der gr. Sippe (denn die Deutung von xeIojv als
 *y.E}Ho, zu dt. h                      awn   ,
                                                   Sommer Gr. Ltst. 79 nach
                                                  aksl. kovati ..schmieden",
 Persson Wzenv. 134, De orig. gerundii 52, verdient wegen der Bed. nicht
 den Yorzug; auch die von Boisacq vermutete Entstehung aus *xaaQco,
 *y.daovor nach Parallelen wie xztavov xzdofiat steht auf schwachen FtiBen).      :



 Das a der flgdn. ital. Worte, wenn sie uberhaupt verwandt sind, ist daher
 Reduktionsvokal e zu bestinimen (s. zuletzt Brugmann IF. 28,369, Giintert
 Abl. 50    * la strom, ..Schneidewerkzeug"
                  :                           ai. cast rein  die Gleichung ist            :                         / ;


 aber bei der Fruchtbarkeit des ai. Formans -tra- und ital. -is(tro)- nicht
 zwingend!' vorausgesetzt von lat .castro, -are „abschneiden, verschneiden,
 kastrieren" iFroehde KZ. 23, 310      cuprum ,, Lager" (d. i. „abgeschnittener
                                                                         ;


 Raum“ oder locus ad segregandum instructus" Thes.).
```


## [2026-09-06T20:44:18.810Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (455,456,457,458):\n    s=t[i]\n    nums=re.findall(r'^\\s*(4[45]\\d)\\b',s,re.M)\n    print(\"### seg\",i,\"nums\",nums[:5])\n    print(s[:250].replace('\\n',' '))\nprint(\"==== seg 457 body\")\nprint(t[457][:2500])\nEOF"
}
```


### [2026-09-06T20:44:20.503Z] TOOL RESULT

```
### seg 455 nums []
                                  q e la°o-, qelejo   —    kelb-, kelp-                                447  qeldno-, q e leuo- „kahl“.    Ai. ati-kurva-, -Mica- „ganz kahl“, av. kaurva -, npers. kal haarlos, kahl"         ,   (Yanieek LEWb. 2 312, Ge
### seg 456 nums []
     Nicht iiberzeugend vergleicht Siitterlin IF. 25, 62 unter Annahme von idg. *kel(e.i)p- auch aisl. hllfa „beschirmen" (s. lieip-).   kes- „schneiden“.      Ai. qusati           ,  f asti „schneidet, metzgt, metzelt", casta- „niedergemetzelt", gas
### seg 457 nums []
                                                                       ‘                    i                 ,                                                          qes-                                               449  osk. kasit ,.oportet“ ode
### seg 458 nums ['450', '443']
450                                             qes-   dagegen cas „gelockt, kraus, gedreht" (Pick II 4 57 zw.) stimmt weder in der Bed. noch im Yokal sonderlich (freilich auch nicht zu (fiasio „Flechtwerk‘'); auch mir. cotut „Sehleifstein" ist kaum 
==== seg 457 body
                                                                       ‘                    i                 ,




                                                     qes-                                               449

osk. kasit ,.oportet“ oder „decet“ Cvgl. deco, bio am „entbehre“; bet „oportet“i
als   mediopassives *kase- „wovon abgeschnitten sein“ auf den Begriff
„schneiden“ zuriickgehn nach Thurneysen Thes., Yf. LEWb. 2 s. v.
   Nicht iiberzeugend ist die Analyse von gr. £l<pos ,,Schwert, Messer                                    1

                                                                                                              ,


£i(pat„ Hobeleisen“ (Ilea.) als £-i<pog, wie egicpog, origipog, (Kretschmer KZ. 3                        1


414 zw. Brugmann 1 2 867; s. Boisacq s. v.).


qes- „kratzen, kammen".
  Aksl. cesq, cesnti             „kammen;     streifen,         abstreifen   (z.      B. Beeren“), bulg.
(usw.)       ,,Kamm“, cech. pa-ces, poln. pa-czes „Hede, Werg“, russ. pa-
           cesel
cesy PI. m., paeesy PI. f. „Abfall beim zweiten Hecheln“, ccska ,.Hede,
Werg“, cesuja „Schuppe“, cesotka ,,Kratze“; ksl. kosa „Haar“, russ. (usw.)
kosa „Flechte, Zopf   ksl. kostm ,,Haar“ (dazu aber trotz Fick I 4 390 nicht
                            -
                                ‘,


gr.    xoprj);                          anriihren“, kasati S£ ,,beriihren“
                     aksl. kosnati „beriihren,                                aus
„zupfen“ oder „sich an jemandem abscheuern“; vgl. serb. dirat „beruhren;
reizen“; Zubaty AfslPh. 16,396, Berneker 58 If. unter Yerweis auch auf
                                                 -
serb. kosim, -iti „lacerare, vellere ', das wohl Iterativ zu resat i; kosnati,
kasati nicht wahrscheinlicher nach G. Meyer Alb. Wb. 220, Pedersen KZ.
36, 328, 338 zu alb. k'as „nahere, bringe nahe, nehme auf"', ngas „beriihre,
treibe an“      cech. (usw.) kochati „ergotzen, liebkosen, lieben“ (zu kosnnji
                 ;


als „liebkosend, zartlich beriihren“, vielleicht geradezu ,,krauen“ nach
Bruckner KZ. 43, 3 LI; nicht als *koks- zu lekte „Hure“, z. B. Ehrlich
KZ. 41, 287); vgl. zu den slav. Worten noch Berneker 152, 491, 538, 580ff.
   Lit. kasa „Haarflechte, Zopf" (brauclit nicht si. Lw. zu sein), kasaii,- yti
„fortgesetzt gelinde kratzen“, kasit kasti „umgraben‘,
                                                                              -
```


## [2026-09-06T20:44:28.552Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW castrum\"; grep -n -o 'castrum[^.]\\{0,300\\}' LEW_1910.txt | head -3\necho \"=== LAT castrum\"; grep -n -o 'castrum[^.]\\{0,300\\}' LAT.txt | head -3\necho \"=== SKT castle\"; grep -n -A3 '^CASTLE\\|^CASTRATE\\|^CHASTE' SKT.txt | head -20"
}
```


### [2026-09-06T20:44:30.261Z] TOOL RESULT

```
=== LEW castrum
=== LAT castrum
2700:castrum: meme sens; alicarius: de iaeunier, ou de brasseur;
10243:castrum
10277:castrum avait pris le sens de "retranchement, emplacement fortifie",
=== SKT castle
```


## [2026-09-06T20:44:32.785Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10235,10300p' LAT.txt\necho \"=== SKT\"; grep -n -i 'Castle, a fort\\|Castrate\\|Chaste,' SKT.txt | head"
}
```


### [2026-09-06T20:44:32.861Z] TOOL RESULT

```
casso, -as, -are: = labare. Mot plautinien (3 ex.Mi,851,856). Cf.
cassabundus, a cadendo. Apud Maeuium (fr.C0m.130 R 3 ); risi egomet me-
cum cassabundum ire ebrium, Varr.L.L.7,53. A basse epoque apparait un
fr 4 quentatif cossito (3 ex.de Paul dans le Digeste, e.g. ubi cassitare
coepisset stillicidium, 8,3,30,3). Cf.M.L.1739 *casicare.
Fr 4 quentatif de cadd.
cassus, -a, -um: vide (de), vain. Ancien et usuel, mais rare
dans la prose classique; fr 4 quent > dans la locution adverbiale in cassum
"en vain". Conserv 4 en v.ital., prov., M.L. 1741.castrum
- 185 -
Derivas: casse, casso adv. (tardifs); casso,-as (4 e s.ap.J.-C.) rendre
vain, priver (de), detruire, d'ou cassatus "effectu prluatus", cassd-
tim; cassesco (cassisco) "exinanire" (Sol.Amm.), d'ou cassita.
Voir ca reo, castus, et peut-etre necesse.- 11 ne 3'agirait pas d'un
participe en *-to~, mais d'un adjectif a gemination expressive. On peut
penser egalement a rapprocher cado,caedo, comme lassus de laedo.
castanea, -ae f. (quelques formes de castania, castanun, castana):
chS-taigne. Ancien adjectif substantive nux castanea, emprunt^ au grec
xapua Hotcrxctveia ou naoravaia; Isid., Or.17,7,34, castaneam Latini a
graeco appellant uocabulo. Hanc enim xoaravov uocant eo quod fructus
gemini in nodum testiculorum infra folliculum reconditi sunt, qui, dum
eiciuntur, quasi castrantur. Cf. aranea. Atteste depuis Virgile. Pan-
roman. M.L.174«,1743. Passe en germanique: v.h.a .chestinna, etc. (de
*castinia) , et en celt.: iri. castan, britt. cesten. De IA castanetum.
Le vocalisme avec a interieur maintenu montre que 1'emprunt ne re-
monte pas a la periode la plus ancienne. Sur un doublet *cas tinea, v.
Meillet, Hsquisse d’une hist. de la l. lat., p.90; H.L.Einf. 3 ,p.153.
castigo, -as: cf .castus.
castor, -oris m.: castor. Emprunt au gr.xaaTwp expliqu 4 par l'e-
tymologie populaire a castrando, cf.Serv.G.1,58; le mot latin est fiber.
De la castoreum-, castorinus,-a,-um. M.L. 1747,1748.
Sur Koccrrwp, v. Boisacq, Rev.de 1 ' Instr .pubi, en Belgique,t .53 (1910),
p.101 et suiv., Pline HN.8,109 et la note d'Ernout ad 1 .
castro, -as, -aul, -atum, -are: couper, emoider; et "chatrer",
d^u "amputer" (sens phys. et moral); castratus: e unuque.
Derives et composes: castratio,-tor,-torius,-tura, exeastro (Varr.,
Ital.). Ancien, usuel. M.L.1749 et 4344 *incastrare.
Ce n'est que tardivetoent que s 1 etablit un rapport entre castus et
castro, e.g. Isid., Or.10,33, castus primum a castratione nuncupatus;
postea placuit ueteribus etiam eos sic nomindre qui perpetuam libidinis
abstinentiam pollicebantur, Thes.III 547,4isqq, Castro est le d^nomi-
natif de *kas-tro-m "ce qui sert a couper", disparu en latin parce que
castrum avait pris le sens de "retranchement, emplacement fortifie",
mais dont le derive a survecu.
Au vocalisme prfes, castrum est a rapprocher de skr .castrdm "instru-
ment tranchant", a cote de gdsati "il coupe" et, sans doute, de hom.
xeucov "fendant", gr.xea^co "je fends".
castrum, -1 n.: retranchement, lieu fortifi^. Le sg. n 1 est gubre
employ^ que dans les noms de lieux Castrum nouum, Laurens Castrum,
Castrum mutilum, etc. Il semble avoir designe d 1 abord une propriete
gardee ou retranchee, cf.Corn.Nep., Alc.9,3, ... ei dederat Grynium in
Phrygia castrum, ex quo quinquagena talenta uectigalis capiebat, ce qui
correapond, semble-t-il, au sens de 1 1 osq. castrous, ombr.kastruvu,
kastruvuf, castruo. Le sens ancien est peut-etre "separation, ce qui
sert a separer", et il y aurait parente avec castro,-are. Employ^ sur-
tout dans la langue militaire au pluriel:
castra,-orum n. (d^ja castra,-ae dans Accius, fem. qui reparait a
basse epoque): camp, campement (souvent oppos 4 a urbs, et plus tard A
pagus, d'ou pagensis form^ sur castrensis) . Il y a prise de possession
quand le general etablit son camp sur un terrain, cf.Varr.fgm. dans
Serv.auct., Ae.9,52, duces ... hastam in ... agrum mittebant, ut castriscastus
186
locun caperent. M.L.1750. V. angi. ceaster (Chester-); ga.ll. caer.
Derivas: castrensis (cf .forensis) d'ou castrensidnus,-arius, et,
tardifs, castrianus,.castricianus (de castricius). Noter le juxtapose
castra netor : netari castra, quod netis deriguntur, P.F.110,18 (usit6
=== SKT
3675:coddle,  to  pamper,  render  effeminate. (£.)  Grig,  to  castrate;  but  confusetl  with caJtitr,  '  to  cocker,*  Col.    Sec  p.  578.
6026:Eunuch,  one  who  is  castrated.  (H« Gk.)  L.  eunuchut.  •-  Gk.  tvv  <M\ot,  a diajbbcrlain ;  one  who  had  charge  of ilceping  apartments.  — Gk.  fVK^,  a  couch; ix^iv,  to  keep,  have  in  charge.
10666:castrate,  mod.  Du.   ttMtm, lupti,  to  peel.
10667:lib.  to  castrate.  (Du.)  Da.  /mMm above.  Der.  g-lib,  verb,  the  aaroe  (o| letc) ;  cf.  O.  Du-iT/u/v,  'gelt,'  Hexhul Iioqu&clotis.  ullcative.  (L.)  Col from  L.  lequaci',  crude  form  of  lo^i talkative.  *  L.  locui,  to  speak.  +  K rtthe,  10  speak  ;  Skt.  lap  (for  lak\  to  t^ (VRAK.)
11765:modeet,  moderate,  chaste,  decent  (F.
12115:1//1///,    W.   «m///,   a    wether   she Diet  cites  Pror.  mcuf,  Como  mat, mutt,   castrated,  and  derives  all  j mntilus,  maimed-
17089:(Scaod.)    Orig.   a    thtn  slip  of pat  under  a.  wheel.  — Swed.  ji*V, shoe  or  sole;  Icel.  sJkfIS,  a  billet see  aboTe.    See  also  Shoddy, (a),  a  hut;  see  Shade. Sheen,  fairness.  (E.)     Sec  Show. Sheep.  (E.)    A.  S.  ued/,  scip;   pi.  the mc.  +  Du.  sihaap,  G.  uhaf.     Cf  Polish a    wether,    from    Charch   Slaronic *J*tli,  to  castrate.
17659:oflT'  the  end  of  a  thing;  cf.  led.  mtthMtr, siivibbcd,  Dipped,  wiUi  Ihc  tip  cut  ofT; sHupra,  to  snub.  p.  Allied  to  obs.  £. iR^d/,  to  pinch,  nip.  answering  to  Icel. smypa^  to  castrate,  also  to  di&^ace,  snub; Swcd.  smpay  to  castrate,  mutkt,  to  clip olT.  Allied  to  Bnap,  and  Snip.  Per. snttb'noitd,  t.  e.  with  a  short  or  stumpy QOiC,  as  if  with  the  end  cut  off.
21343:Wether,  a  castrated  ram.  (E.)  K.  S. Bv5*r+0.Sax.  wtthfir,witkar,  Icel.  ivCr, Dan.  vadcr,  Swed.  vadur,  G,  widdtr,  Goth. wiMrm,  a  lamb.  LiL  '  a  yeaxUng  ;  *  allied to  Veal.
```


## [2026-09-06T20:45:09.284Z] TOOL CALL #77: Bash

```json
{
 "command": "tail -14 data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d.get('url'))\n\""
}
```


### [2026-09-06T20:45:11.031Z] TOOL RESULT

```
https://abadis.ir/fatofa/%D9%86%DA%A9%D9%88%D9%87%DB%8C%D8%AF%D9%86/
https://en.wiktionary.org/wiki/سنبه
https://abadis.ir/fatofa/%D8%AF%D9%87%DA%A9%D8%AF%D9%87/
https://en.wiktionary.org/wiki/%DA%A9%D8%AF%D8%AE%D8%AF%D8%A7
https://www.ahdictionary.com/word/search.html?q=cipher
https://www.etymonline.com/word/castrate
https://en.wiktionary.org/wiki/%D8%B4%D9%88%D8%B1%D9%87
https://en.wiktionary.org/wiki/%CE%BE%CF%8D%CF%89
https://en.wiktionary.org/wiki/%CE%BE%CE%B1%CE%AF%CE%BD%CF%89
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/kes-
https://en.wiktionary.org/wiki/%D8%B3%D9%88%DA%AF
https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D9%88%D8%B3
https://www.vajehyab.com/?q=%D8%AE%D8%B3%DB%8C%D8%AF%D9%86
https://en.wiktionary.org/wiki/%DA%A9%D9%88%D9%86
```


## [2026-09-06T20:53:55.623Z] TOOL CALL #78: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build261.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 261,\n \"book_page\": 231,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Kes 1, Kas 1\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *kes- 'to cut' (variant *kas-), with instrument noun *kas-tro-m 'cutting tool'\",\n   \"note\": \"Pokorny p.586-587 has a root kes- 'schneiden'; kes-tro-m 'Schneidewerkzeug, Messer', quite separate from the ḱes- 'kratzen, kämmen' of p.585-586 that Nourai calls Kes 2. Watkins/AHD prints exactly Nourai's headword shape: 'kes-2. To cut. Variant kas-' [Pok. kes- 586]. So both the root, the 'Indo-European' label and the gloss 'to cut' are right, and Nourai's split of Kes 1 / Kes 2 reproduces the standard handbooks. The only reservation modern Latinists add (Ernout-Meillet, de Vaan) is that the connection of castus/careō with castrāre is 'probable' rather than demonstrated.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *kes- «بریدن» (با گونهٔ *kas-) و اسم ابزارِ *kas-tro-m «ابزار بریدن». پوکورنی در صفحهٔ ۵۸۶ ریشهٔ kes- «بریدن» را جدا از ḱes- «خاراندن، شانه کردن» (ص ۵۸۵) آورده و واتکینز نیز در پیوست فرهنگ American Heritage همین دو ریشه را با شمارهٔ ۱ و ۲ از هم جدا کرده است؛ بنابراین نام ریشه، برچسب زبانی و معنای «بریدن» در نمودار نورایی درست است. تنها نکتهٔ احتیاطی آن است که پیوند castus و careō با castrāre نزد ارنو-میه و دِ ڤان «محتمل» شمرده می‌شود نه قطعی. ادعای نورایی درست است.\",\n   \"sources\": [W+\"castrum\", \"https://www.etymonline.com/word/castle\", \"https://www.etymonline.com/word/castrate\"],\n   \"ref_check\": [\n    {\"ref\": \"POK:586\", \"status\": \"supports\",\n     \"note\": \"POK_02.txt leaf 246 (printed pp.586-587): 'kes- .schneiden'; keS-tro-m ,Schneidewerkzeug, Messer'. ... *kastrom .Schneidewerkzeug' (: ai. Sastrdm) wird vorausgesetzt von lat. castrō, -āre .abschneiden, verschneiden, kastrieren', castrum .Lager' als .abgeschnittenes Stück Land''. The entry begins on the last quarter of p.586, exactly where Nourai points.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 appendix s.v. kes-2\", \"stance\": \"supports\",\n     \"note\": \"'kes-2. To cut. Variant kas-. 1. Suffixed form *kas-tro- in: a. Latin castrare, to castrate: CASTRATE; b. Latin castrum, fortified place, camp (perhaps “separated place”): CASTLE. 2. Suffixed form *kas-to- in Latin castus, chaste, pure (< “cut off from, free of, faults”): CASTE, CHASTE; CASTIGATE, INCEST. ... [Pok. kes- 586.]' (grep 'kes-2' AHD_watkins1985.txt) — Nourai's 'Kes 1, Kas 1: to cut' is a transcript of this entry.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 448 (WLD_Bd1_pages.txt seg 456)\", \"stance\": \"supports\",\n     \"note\": \"'kes- „schneiden“. Ai. śāsati, śāsti „schneidet, metzgt“, śāstra- n. „schneidendes Werkzeug, Messer, Dolch“ ... *kastrom „Schneidewerkzeug“ ... vorausgesetzt von lat. castro, -are „abschneiden, verschneiden, kastrieren“; castrum „Lager“'.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet pp. 185-186 s.vv. castro / castrum\", \"stance\": \"supports\",\n     \"note\": \"'castro est le dénominatif de *kas-tro-m \\\"ce qui sert à couper\\\", disparu en latin parce que castrum avait pris le sens de \\\"retranchement, emplacement fortifié\\\" ... castrum est à rapprocher de skr. śastrám \\\"instrument tranchant\\\", à côté de śásati \\\"il coupe\\\"'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Latin\", \"words\": \"castrum, castellum; castrare\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin castrāre 'to cut, geld' is a denominative of a lost noun *kas-tro-m 'cutting tool' (PIE *kas-tro-, exactly matched by Sanskrit śastrá- 'knife, dagger' beside śásati 'he cuts'). The same *kas-tro-m survives as castrum, whose oldest sense is territorial: Oscan gen. sg. castrous 'fundi', Umbrian kastruvuf 'fundos' show 'a piece of land marked off', whence Latin castrum 'a place cut off, entrenchment, fort' and the plural castra 'camp'. castellum is the regular diminutive in -ellum ('little fort, citadel'), first military (Caesar), later the Vulgate word for a fortified village. So Nourai's gloss 'an \\\"isolated\\\" fortified place' renders precisely the etymological sense that Ernout-Meillet give ('séparation, ce qui sert à séparer'). Nourai's Latin box is a faithful copy of AHD's kes-2 entry.\",\n     \"derivation_fa\": \"castrāre لاتینی «بریدن، اخته کردن» فعلی است ساخته از نامِ ازمیان‌رفتهٔ *kas-tro-m «ابزار بریدن»؛ همین صورت در سنسکریت śastrá- «کارد، خنجر» (در کنار śásati «می‌بُرَد») بازمانده است. همان *kas-tro-m در castrum ماند، اما با تحول معنایی «پارهٔ زمینِ جدا شده» ← «حصار، اردوگاه»؛ صورت‌های اُسکی castrous «مِلک» و اومبریایی kastruvuf «املاک» گواه معنای کهن‌اند. castellum مصغّرِ منظم آن با پسوند ‎-ellum‎ است («دژِ کوچک»). بنابراین معنای «جایگاه استحکامیِ جدا افتاده» که نورایی می‌آورد همان معنای ریشه‌شناختی است که ارنو-میه به دست می‌دهند. ادعای نورایی درست است.\",\n     \"sources\": [W+\"castrum\", \"https://www.etymonline.com/word/castle\", \"https://www.etymonline.com/word/castrate\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. kes-2: 'Suffixed form *kas-tro- in: a. Latin castrare, to castrate: CASTRATE; b. Latin castrum, fortified place, camp (perhaps “separated place”): CASTLE.' Nourai's node is this line.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet p.185 s.v. castro, p.186 s.v. castrum\", \"stance\": \"supports\",\n       \"note\": \"'Castro est le dénominatif de *kas-tro-m \\\"ce qui sert à couper\\\" ... Le sens ancien est peut-être \\\"séparation, ce qui sert à séparer\\\", et il y aurait parenté avec castro,-are' — the 'isolated place' gloss is Ernout-Meillet's.\"},\n      {\"src\": \"KLN\", \"where\": \"leaf 140 s.v. castrametation / castrate (printed ≈ p.256)\", \"stance\": \"supports\",\n       \"note\": \"'Castra is the plural of castrum, “a fortified place, fort, castle”, orig. “that which has been cut out”, fr. *kastrom, “a cutting tool” ... castrate ... fr. L. castratus, pp. of castrare, “to cut, geld”, fr. *kastrom ... prob. cogn. with OI. sasati, sasti, “cuts”, sastram, “knife”, Gk. κεάζειν, “to split”'.\"},\n      {\"src\": \"POK\", \"where\": \"p.586-587 s.v. kes- 'schneiden'\", \"stance\": \"supports\",\n       \"note\": \"'*kastrom .Schneidewerkzeug' ... vorausgesetzt von lat. castrō, -āre ..., castrum .Lager' als .abgeschnittenes Stück Land', osk. Gen. Sg. castrous .fundi', umbr. castruo, kastruvuf .fundos''.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Arabic\", \"words\": \"al-qasr\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic قَصْر qaṣr 'castle, palace' (with the article al-qaṣr) is one of the oldest Latin loans in Arabic: Latin castrum / castra passed into Byzantine Greek as κάστρον and into Aramaic as קַצְרָא qaṣrā, and Arabic took it from Aramaic in pre-Islamic times (it is already Qur'ānic, Q 25:10, 77:32 — hence Jeffery's entry). The route explains the shape: Latin -st- is rendered by emphatic ṣ, the neuter -um is dropped, and the word is re-analysed on the Arabic pattern faʿl, which then attracted it to the unrelated Arabic root q-ṣ-r 'to be short, to shorten'. Nourai's arrow Latin → Arabic is correct in substance; the chart simply omits the Aramaic/Greek relay.\",\n     \"derivation_fa\": \"«قَصْر» عربی از کهن‌ترین وام‌واژه‌های لاتینی در عربی است: castrum لاتینی از راه یونانی بیزانسی κάστρον و آرامی קַצְרָא (qaṣrā) به عربی رسیده و پیش از اسلام در آن جا افتاده است (در قرآن نیز آمده، از این رو جفری آن را در واژه‌های دخیل قرآن آورده). صورت واژه همین راه را نشان می‌دهد: ‎-st-‎ لاتینی به «ص» مفخّم بدل شده، پایانهٔ خنثای ‎-um‎ افتاده و واژه بر وزن «فَعْل» بازتحلیل شده و سپس با ریشه‌شناسی عامیانه به ریشهٔ بی‌ربطِ «ق‌ص‌ر» (کوتاه شدن) پیوند خورده است. جهت وام‌گیری در نمودار نورایی درست است، فقط واسطهٔ آرامی/یونانی را نیاورده است.\",\n     \"sources\": [W+\"%D9%82%D8%B5%D8%B1\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:45\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 35 (≈ printed p.45-46), s.v. alcazar: 'Sp., fr. Arab. al-qasr, “the castle”, fr. al-, “the”, and L. castrum, “fortified place, fort, castle”. See castrametation and cp. castle.' — exactly Nourai's arrow, including the al- of his 'al-qasr'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"no. 1117 (Ar. kasr), printed p.90\", \"stance\": \"supports\",\n       \"note\": \"'1117. Ar. kasr: „Schloß, Burg“ [aus lat. castrum, gr. Κάστρον ZDMG LI, 316]; hieraus mit ar. Art. sp. pg. alcázar „dass., Kastell“; it. càssero „kleines Schloß“' — Lokotsch adds the Greek relay.\"},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery s.v. (Qasr), FVQ.txt line 15001 ff.\", \"stance\": \"supports\",\n       \"note\": \"Jeffery has the entry '(Qasr)' and judges earlier scholars 'correct in deriving it from Lat. castrum through Gk. Κάστρον and ...' (the Aramaic form follows).\"},\n      {\"src\": \"PHN\", \"where\": \"Pihan s.v. ALCAÇAR et ALCAZAR\", \"stance\": \"partial\",\n       \"note\": \"'القصر [alqas'r] le château, dénomination commune à divers châteaux forts ou palais élevés par les Maures' — confirms the Arabic word and its spread west, silent on the Latin source.\"},\n      {\"src\": \"AFA\", \"where\": \"Fraenkel, AFA.txt line 8224\", \"stance\": \"supports\",\n       \"note\": \"Fraenkel cites 'jüd. קצרא = κάστρον castrum' — the Jewish-Aramaic intermediary that stands between Latin and Arabic.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"qasr «قصر»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian قصر qaṣr 'palace' is a straight Arabic loan of the ʿAbbāsid period, taken with the Arabic script and the emphatic ṣād (pronounced [s] in Persian); Moʿin tags it simply [ع.] 'Arabic' and glosses it with the native words کوشک and کاخ. Because the Arabic word is itself Latin castrum, قصر is a Latin word that reached Persian by the western route (Latin → Aramaic/Greek → Arabic → Persian) rather than by inheritance — a genuine loan round-about, not a cognate of Persian کوشک. Nourai's chain is correct.\",\n     \"derivation_fa\": \"«قصر» در فارسی نو وام‌واژه‌ای عربی از دورهٔ عباسی است که با همان خط و همان صادِ عربی (که در فارسی [س] تلفظ می‌شود) گرفته شده است؛ معین آن را با نشانهٔ [ع.] می‌آورد و با واژه‌های بومیِ «کوشک» و «کاخ» معنی می‌کند. چون خودِ واژهٔ عربی از castrum لاتینی است، «قصر» واژه‌ای لاتینی است که از راه غرب (لاتینی ← آرامی/یونانی ← عربی ← فارسی) به فارسی رسیده، نه از راه میراث ایرانی؛ پس با «کوشک» هم‌ریشه نیست. زنجیرهٔ نورایی درست است.\",\n     \"sources\": [W+\"%D9%82%D8%B5%D8%B1\"],\n     \"ref_check\": [\n      {\"ref\": \"MON:2682\", \"status\": \"supports\",\n       \"note\": \"Moʿin, Farhang-e Fārsi (MON_part2.txt line ~12988), s.v. قصر: 'قصر: [ع.] (اِ.) کوشک، کاخ شاهی؛ ج. قصور.' The running heads of the OCRed leaf are the قصب- / قصر pages of vol. 3, i.e. Nourai's p.2682. Moʿin marks the word Arabic; he gives no further (Latin) etymology, so the reference supports the Arabic→Persian step only.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"vol. 3 s.v. قصر\", \"stance\": \"supports\",\n       \"note\": \"'[ع.] (اِ.) کوشک، کاخ شاهی' — tagged Arabic, glossed with the inherited Persian synonyms.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt seg 470 (printed ≈ p.471)\", \"stance\": \"silent\",\n       \"note\": \"Aryanpur's Indo-European root dictionary mentions قصر only in passing and gives it no Indo-European root of its own — consistent with its being a loan, not an inherited word.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"French\", \"words\": \"chateau\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"French château continues Latin castellum through Old French chastel (12th c.): Vulgar Latin ca- before a > Old French cha- [tʃa-] (the regular northern-Gallo-Romance palatalisation, cf. campus > champ), intervocalic -ll- simplifies, and the pre-consonantal s of chastel was lost about 1200-1300, its loss marked by the circumflex of modern château (as in castellum > chastel > châtel/château). The plural châteaux and the toponymic Château- are the same word. Nourai's Latin → French arrow is the textbook chain.\",\n     \"derivation_fa\": \"château فرانسوی دنبالهٔ castellum لاتینی است از راه چاستل کهن (chastel در فرانسویِ کهنِ سدهٔ ۱۲): ca- لاتینی پیش از a در گویش‌های شمالی گالو-رومی به cha- کام‌شده بدل می‌شود (همچون campus > champ)، ‎-ll-‎ میان‌واکه‌ای ساده می‌شود و «س»ِ پیش از همخوان در حدود سدهٔ ۱۳ می‌افتد؛ نشانهٔ این افتادگی همان کلاهکِ (accent circonflexe) â در château امروزی است. پیکان لاتینی ← فرانسوی در نمودار نورایی همان زنجیرهٔ کتاب‌های درسی است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/chateau\", \"https://www.etymonline.com/word/castle\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. kes-2 routes castellum to CASTLE; the AHD main entry for chateau gives 'French château, from Old French chastel, from Latin castellum', which is the arrow drawn here.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"leaf 140 s.v. castle (printed ≈ p.256)\", \"stance\": \"supports\",\n       \"note\": \"'ONF. castel, corresponding to OF. chastel (F. chateau), fr. L. castellum, “citadel, fortress, stronghold”, dimin. of castrum'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet p.186 s.v. castrum (M.L. 1750)\", \"stance\": \"supports\",\n       \"note\": \"Ernout-Meillet cite the Romance continuations of castrum/castellum via Meyer-Lübke no. 1750 and note the English borrowing 'V. angl. ceaster (Chester-)'.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"chateau, castle\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Both English words go back to Latin castellum through French, but by two different French routes, and the chart's single arrow blurs them. castle is the older: Old Northern (Norman) French castel, which kept the un-palatalised ca-, was taken into late Old English as castel (already in the Anglo-Saxon Chronicle 1048, first meaning 'village' after the Vulgate's castellum, then 'fortified building' after the Norman keeps) — Middle English castel > castle. chateau is a modern learned borrowing (first English use c. 1739) of Central French château in the sense 'stately country house', and later of the wine-label sense. So 'English ← French' is right for both words, but castle does not come from château; it comes from its Norman doublet castel — the two are a doublet pair in English.\",\n     \"derivation_fa\": \"هر دو واژهٔ انگلیسی سرانجام به castellum لاتینی می‌رسند، اما از دو راهِ فرانسویِ جدا؛ نمودار این دو را در یک پیکان درهم آمیخته است. castle کهن‌تر است: صورت نورمانی/شمالیِ castel که ca- کام‌نشدهٔ خود را نگه داشته بود، در اواخر انگلیسی باستان به‌صورت castel وام گرفته شد (نخست به معنی «دهکده» به پیروی از ترجمهٔ لاتینی انجیل، سپس «دژ» پس از فتح نورمان‌ها) و از آن‌جا castle. اما chateau وامی متأخر و کتابی از فرانسویِ مرکزی است (نخستین کاربرد انگلیسی حدود ۱۷۳۹ م.) به معنی «کوشکِ ییلاقی». پس «انگلیسی از فرانسوی» برای هر دو درست است، ولی castle از château نیامده بلکه از دوگانهٔ نورمانیِ آن castel آمده است؛ این دو در انگلیسی «دوگانه» (doublet) اند. با احتیاط پذیرفتنی است.\",\n     \"sources\": [\"https://www.etymonline.com/word/castle\", \"https://www.etymonline.com/word/chateau\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"The node carries no reference in the book (the English box on the printed page has no reference icon — checked on the page image).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"leaf 140 s.v. castle (printed ≈ p.256)\", \"stance\": \"partial\",\n       \"note\": \"'castle, n. — ME. castel, fr. ONF. castel, corresponding to OF. chastel (F. chateau), fr. L. castellum' — Klein derives castle from the Old NORTHERN French form, not from château, and lists chateau only as a cognate to compare ('cp. ... chateau').\"},\n      {\"src\": \"SKT\", \"where\": \"grep 'castle'/'chateau' in SKT.txt\", \"stance\": \"silent\",\n       \"note\": \"Skeat's concise edition on disk is too poorly OCRed at this alphabetic range to read the CASTLE entry; no usable text found.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"castrate, chastity\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"castrate (1610s) is Latin castrātus, past participle of castrāre, taken directly into English from the Latin, alongside the earlier noun castration (15th c. via French). chastity comes by the other suffixed branch of the root: PIE *kas-to- > Latin castus 'cut off from (fault), pure' > castitās, acc. castitātem > Old French chastete > Middle English chastite > chastity; the adjective chaste followed the same path. Watkins lists castrate, caste, chaste, castigate and incest together under kes-2, so both of Nourai's English words are on the reference he cites.\",\n     \"derivation_fa\": \"castrate (سدهٔ ۱۷ م.) همان castrātus لاتینی است، اسم مفعولِ castrāre، که یک‌راست از لاتینی به انگلیسی رفته است. chastity از شاخهٔ دیگر همین ریشه می‌آید: هندواروپاییِ *kas-to- > لاتینی castus «بریده از عیب، پاک» > castitās (رایی castitātem) > فرانسویِ کهن chastete > انگلیسی میانه chastite > chastity؛ صفتِ chaste نیز همین راه را پیموده است. واتکینز در پیوستِ AHD واژه‌های castrate، caste، chaste، castigate و incest را زیر همین ریشهٔ kes-2 گرد آورده، پس هر دو واژهٔ انگلیسیِ نورایی در همان مرجعی هست که او یاد کرده است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/castrate\", \"https://www.etymonline.com/word/chateau\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. kes-2: '1a. Latin castrare, to castrate: CASTRATE ... 2. Suffixed form *kas-to- in Latin castus, chaste, pure (< “cut off from, free of, faults”): CASTE, CHASTE; CASTIGATE, INCEST.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"leaf 140 s.v. castrate; leaf 153 s.v. chastity (printed ≈ pp.256, 282)\", \"stance\": \"supports\",\n       \"note\": \"'castrate, tr. v. ... — L. castratus, pp. of castrare, “to cut, geld”, fr. *kastrom, “a cutting tool” ... L. castrum ... carere ..., castus, “pure, chaste”, are prob. related to castrare. See chaste'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet p.186 s.v. castrum / castus\", \"stance\": \"partial\",\n       \"note\": \"Ernout-Meillet warn that the link of castus to castro is late and possibly secondary: 'Ce n'est que tardivement que s'établit un rapport entre castus et castro, e.g. Isid., Or.10,33, castus primum a castratione nuncupatus' — so 'chastity' under this root is probable rather than proven.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Kes 2, Qseu\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ḱes- 'to scratch, comb', with the enlargements *ks-en-, *ks-eu- and *ks-n-eu-\",\n   \"note\": \"Pokorny p.585-586 has 'ḱes- „kratzen, kämmen“; ksu-ro- „Schermesser“' with exactly the three Wurzelerweiterungen Nourai's headword implies: ks-en- (Gk. ξαίνω), ks-es- (Gk. ξέω), ks-eu- (Skt. kṣurá-, Gk. ξύω) and ks-n-eu- (Skt. kṣṇāuti, Av. hu-xšnuta-). 'Qseu' is Nourai's spelling of Klein's *qseu- = *kseu-. Walde-Pokorny I 449, which he also cites, is the parallel entry. Root, language label and gloss are right; what is not right is that Nourai hangs on this one root three Persian words (خشنود, شانه, شور) that modern Iranian etymology assigns elsewhere.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ḱes- «خاراندن، شانه کردن» با گسترش‌های *ks-en-، *ks-eu- و *ks-n-eu-. پوکورنی در صفحهٔ ۵۸۵–۵۸۶ همین ریشه را با نامِ ḱes- «kratzen, kämmen» و اسم ابزارِ ksu-ro- «تیغِ سلمانی» آورده و همان سه گسترشی را برمی‌شمارد که سرنویسِ نورایی به آن‌ها اشاره دارد: ks-en- (یونانی ξαίνω)، ks-es- (یونانی ξέω)، ks-eu- (سنسکریت kṣurá-، یونانی ξύω) و ks-n-eu- (سنسکریت kṣṇāuti، اوستایی hu-xšnuta-). «Qseu» صورت نوشتاری نورایی از *qseu- کلاین (= *kseu-) است و ارجاع WLD1:449 نیز دقیقاً همان مدخل والده-پوکورنی است. نام ریشه، برچسب زبانی و معنا درست است؛ آنچه درست نیست این است که نورایی سه واژهٔ فارسیِ «خشنود»، «شانه» و «شور» را زیر همین ریشه می‌آورد، حال آن‌که ریشه‌شناسی ایرانیِ امروز هر سه را به جای دیگری می‌برد.\",\n   \"sources\": [W+\"Reconstruction:Proto-Indo-European/kes-\", W+\"%CE%BE%CE%B1%CE%AF%CE%BD%CF%89\", W+\"%CE%BE%CF%8D%CF%89\"],\n   \"ref_check\": [\n    {\"ref\": \"POK:585\", \"status\": \"supports\",\n     \"note\": \"POK_02.txt leaf 244-245 (printed pp.585-586): 'ḱes- ,kratzen, kämmen'; ksu-ro- ,Schermesser'' followed by 'Wurzelerweiterungen: ks-en- in gr. ξαίνω (*ksn̥i̯o) ,kratze, kämme' ... ks-n-eu- in: ai. kṣnāuti ,schleift, wetzt, reibt' ... av. hu-xšnuta- ,gut geschärft' ... ks-es- in: gr. ξέω ... ks-eu- in: ai. kṣurá- m. .Schermesser'; npers. šōr .salzig', kurd. šūr'. The whole of Nourai's chart 2 is drawn from these two pages.\"},\n    {\"ref\": \"WLD1:449\", \"status\": \"supports\",\n     \"note\": \"WLD_Bd1_pages.txt seg 457, printed p.449: 'ḱes- „kratzen, kämmen“. Aksl. česǫ, česati „kämmen; streifen“ ... Lit. kasà „Haarflechte, Zopf“, kasaú,-yti „fortgesetzt gelinde kratzen“'. The page number Nourai gives is the first page of the entry.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kes-1\", \"stance\": \"supports\",\n     \"note\": \"'kes-1. To scratch. 1. Germanic *hezdō in Old English heordan, coarse parts of flax: HARDS. 2. Extended form *kseu- in Greek xuein, to scrape: XYSTER. 3. Nasalized form *ks-n-eu- in: a. Germanic *snaww- ...; b. Latin novacula, razor: NOVACULITE. [Pok. kes- 585.]' — Nourai's 'Kes 2, Qseu: to scratch' is this entry, and his Greek and English nodes are its items 2-3.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann pp.572-574 (IEC.txt leaves 325-326)\", \"stance\": \"supports\",\n     \"note\": \"Mann has the family under several headwords: 'ksənō, -ió ‘scratch, scrape, dig’ ... Gk. ksaíno ... ‘lacerate; card wool’' (p.574), 'ksesió ‘grind, crush, pound, scrape’ ... Gk. kséo, adj. ksestós ‘scrape, rake, polish’. WP I, 450' (p.572), 'ksneuo ... pp. in Skt. ksnutáh, Av. hu-xšnuta-' (p.574).\"},\n    {\"src\": \"SYN\", \"where\": \"Buck, concept 'comb'\", \"stance\": \"silent\",\n     \"note\": \"Buck's synonym dictionary has no separate section for 'comb'; grep of SYN.txt returned nothing usable for this root.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"hu-xšnuta, hu-šnŭta; xšnâvaya\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Two different Avestan words are conflated here. (a) Young Avestan hu-xšnuta- is real and does belong to this root: Bartholomae, AiW col. 1831, 'hu-xšnuta- Adj. \\\"gutgeschärft, scharfgespitzt\\\"', used only of arštay- 'spear' (Yt 10.24, 10.39), = Skt. kṣṇutá-, past participle of kṣṇāuti 'whets' — this is Pokorny's ks-n-eu-. Its meaning is 'well-sharpened', NOT 'well polished, pleasant, happy'. (b) The 'pleasant, happy' word is hu-xšnūta- (long ū) beside hu-xšnūti- f. 'gute Befriedigung' (AiW 1831, Yt 10.108), and xšnāvaya- is the iterative-causative stem of the verb xšnav- 'to satisfy, to do one's duty by' (AiW 557-60, Praes. 30 xšnāvaya-). Cheung, Etymological Dictionary of the Iranian Verb (2007), separates these as two roots: *xšnau¹ 'to hear (< to sharpen the ears)' = PIE *ksneu-, to which hu-xšnuta- 'well-sharpened' belongs, and *xšnau² 'to exchange gifts / to entertain, thank, satisfy' = PIE *ksenu- (cf. Gk. ξένος), to which Av. xšnu-/xšnāvaya- and NP xušnūd belong; Kent, meanwhile, calls āxšnav- 'apparently an extension of root xšnā- \\\"learn\\\"'. So the arrow root → 'to satisfy' is what modern scholarship rejects. Note also that 'hu-šnŭta' is not an Avestan form but the Pahlavi/Pāzand shape (hušnūt), so the box mixes two language stages.\",\n     \"derivation_fa\": \"در این خانه دو واژهٔ اوستایی جداگانه در هم آمیخته‌اند. نخست، hu-xšnuta- اوستایی نو واقعاً به همین ریشه می‌رسد: بارتولومه در ستون ۱۸۳۱ فرهنگ ایرانی باستان آن را «gutgeschärft، خوب تیزکرده» معنی می‌کند و تنها با arštay- «نیزه» به کار رفته (یشت ۱۰، بندهای ۲۴ و ۳۹)؛ برابر سنسکریت kṣṇutá-، اسم مفعولِ kṣṇāuti «تیز می‌کند». پس معنای آن «خوب تیزشده» است، نه «خوش‌صیقل، خوشایند، شاد». دوم، واژهٔ «خرسند» hu-xšnūta- (با وویِ کشیده) در کنار hu-xšnūti- «خرسندیِ نیک» است و xšnāvaya- ستاکِ سببیِ فعلِ xšnav- «خشنود کردن» (بارتولومه ۵۵۷–۵۶۰). چونگ در فرهنگ ریشه‌شناختی فعل ایرانی (۲۰۰۷) این دو را دو ریشهٔ جدا می‌داند: *xšnau¹ «شنیدن (از «تیز کردنِ گوش»)» از هندواروپایی *ksneu- که hu-xšnuta- «خوب تیزشده» از آن است، و *xšnau² «پیشکش‌ ردّ و بدل کردن ← پذیرایی کردن، سپاس گفتن، خشنود کردن» از *ksenu- (هم‌ریشه با ξένος یونانی) که xšnu-/xšnāvaya- اوستایی و «خشنود» فارسی از آن‌اند. کِنت نیز āxšnav- پارسی باستان را گسترشی از ریشهٔ xšnā- «دانستن» می‌شمارد. بنابراین پیوند «خشنود کردن» با ریشهٔ «خاراندن» را پژوهش امروزی رد می‌کند. افزون بر این، صورت hu-šnŭta اوستایی نیست بلکه شکل پهلوی/پازند (hušnūt) است و دو مرحلهٔ زبانی در یک خانه آمده‌اند.\",\n     \"sources\": [W+\"%D8%AE%D8%B4%D9%86%D9%88%D8%AF\", W+\"Reconstruction:Proto-Indo-European/kes-\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:585\", \"status\": \"supports\",\n       \"note\": \"POK_02.txt leaf 244, printed p.586, under 'ks-n-eu-': 'ai. kṣnāuti ,schleift, wetzt, reibt', kṣnōtra- n. ,Schleifstein', Partiz. kṣnutá- av. hu-xšnuta- ,gut geschärft''. Pokorny does put Av. hu-xšnuta- here — but with the gloss 'well sharpened', not 'pleasant, happy'.\"},\n      {\"ref\": \"KNT:175\", \"status\": \"partial\",\n       \"note\": \"Kent's Lexicon begins on leaf 193 = printed p.164, so leaf 204-205 = printed pp.175-176, where the entry stands: 'āxšnav- vb. ‘hear, satisfy’ (§96): cf. Av. xšnav- “Genüge haben an”, adj. xšnav- “Genüge leistend”, ptc. xšnuta-, sb. xšnūtay- “Zufriedenstellung” (Bthl. AiW 557-60); apparently an extension of root xšnā- “learn” ... with semantic development “learn, hear of, hear”, and “hear, hearken to, satisfy”.' Kent has the words but explicitly derives them from xšnā- 'learn', not from *kes-/*kseu-.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 1831 (BRT.txt leaf 993) and col. 557-560 (leaf 329)\", \"stance\": \"partial\",\n       \"note\": \"col. 1831: 'j. hu-xšnuta- Adj. (fem. -ā-) „gutgeschärft, scharfgespitzt“: arštayasca ... Yt.10.39 ... ai. kṣnutá- Adj., PPtP. ... V. kṣnāu-' — and immediately after it a SEPARATE lemma 'j. hu-xšnūtay- f. „gute Befriedigung“'. col. 557 ff.: 'j., g. xšnav- V. „Genüge haben an —, leisten in —“. Praes. 1 xšnu-, 5 huxšnu-, ... 30 (Iter.) xšnāvaya-' — so xšnāvaya- is a real Avestan stem, but of the 'satisfy' verb, not of the 'sharpen' word.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"Etym. Dict. of the Iranian Verb pp. 456-458, s.vv. *xšnau1 / *xšnau2\", \"stance\": \"contradicts\",\n       \"note\": \"'*xšnau1 “to hear (< ‘to sharpen (the ears)’)”. AVESTAN: ? YAv. hu-xšnuta- (+ *hu- ‘well’) “well-sharpened” (Yt 10.24, Yt 10.39) ... «PIE *ksneu- “to sharpen” = LIV: 373 | Pok.: 585' versus '*xšnau2 ? “to exchange gifts ... whence: to entertain, welcome (a guest), to thank, praise”. AVESTAN: xšnu- ... Caus.: pres. IND. 3sg. YAv. xšnauuaiieiti ... MIDDLE PERSIAN: BMP hwsnwtk /hošnūd/ ... NWIR: NP xušnūd “content, pleased, happy” ... «PIE *ksenu- “to exchange gifts”'. Cheung thus splits the node's two words between two roots.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann p.574 s.v. ksneuo\", \"stance\": \"supports\",\n       \"note\": \"'ksneuo (ksneumi) ‘pierce, stab, be sharp, be keen’ ... pp. in Skt. ksnutáh, Av. hu-xšnuta-' — Mann agrees with Pokorny that hu-xšnuta- is the 'sharp' word.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"xošnŭd «خشنود» (with خوشیدن ، خوش)\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"For خشنود itself the chain in the chart is the standard one: Avestan *hu-xšnūta- 'well satisfied' (built on xšnav- like huxšnūti- 'good satisfaction') > Book Pahlavi hwšnwt' /hušnūd/ 'contented, happy' (Ardā Wīrāz-nāmag) > New Persian xušnūd/xošnud, with the regular Middle Persian voicing of final -t after a long vowel to -d and the loss of initial h- of hu- into the x of xš- (Horn no. 509 gives exactly aw. *huxšnūta- > phlv. xušnūt > np. xušnūd). Cheung confirms the Iranian route (MP hušnūd, NP xušnūd) while assigning it to his root *xšnau², not to *kes-. The two extra Persian words in the same box are wrong: خوش goes back to MP xwaš (Horn 508; the older shape xwaš is why xušnūd is often written as if it began with خوش — Hübschmann 509 already noted this folk-etymological respelling), and خوشیدن is 'to dry up', whose own ancestor Abolghāsemī gives on the very page Nourai cites as *hauš-/huš- 'to become dry' (the root of خشک), not xšnav-.\",\n     \"derivation_fa\": \"برای خودِ «خشنود» زنجیرهٔ نمودار همان زنجیرهٔ پذیرفته‌شده است: اوستایی *hu-xšnūta- «نیک‌خشنود» (ساخته بر ستاکِ xšnav-، همچون huxšnūti- «خشنودیِ نیک») > فارسی میانه (پهلوی کتابی) hušnūd «خرسند، شاد» (در ارداویراف‌نامه) > فارسی نو «خشنود»؛ ‎-t‎ پایانی پس از واکهٔ کشیده در فارسی میانه به ‎-d‎ نرم شده و «ه»ِ پیشوندِ hu- در خوشهٔ xš- ادغام شده است. هرن در مدخل ۵۰۹ دقیقاً همین را می‌آورد. چونگ نیز راهِ ایرانیِ آن را تأیید می‌کند، اما آن را به ریشهٔ *xšnau² می‌برد نه به ریشهٔ «خاراندن». اما دو واژهٔ افزودهٔ همین خانه نادرست‌اند: «خوش» از فارسی میانهٔ xwaš است (هرن ۵۰۸) — و هوبشمان در همان شمارهٔ ۵۰۹ یادآور می‌شود که املای «خوشنود» ریشه‌شناسی عامیانه است — و «خوشیدن» به معنی «خشک شدن» است که ابوالقاسمی در همان صفحه‌ای که نورایی ارجاع داده آن را از ریشهٔ *huš «خشک شدن» (ریشهٔ «خشک») می‌گیرد. پس تنها بخشِ نخستِ این خانه پذیرفتنی است.\",\n     \"sources\": [W+\"%D8%AE%D8%B4%D9%86%D9%88%D8%AF\"],\n     \"ref_check\": [\n      {\"ref\": \"HRN:113\", \"status\": \"supports\",\n       \"note\": \"Horn, Grundriss p.113 (HRN.txt leaf 134), no. 509: 'xūšnūd, xūšnū ‚zufrieden, fröhlich'. aw. *huxšnūta- vergl. huxšnūiti- ‚Befriedigung'; phlv. xūšnūt, xūšnūtik (AV.).' — exactly Nourai's arrow, including the reconstructed Avestan form.\"},\n      {\"ref\": \"BQT:755\", \"status\": \"partial\",\n       \"note\": \"BQT_v2_pages.txt leaf 213 (printed ≈ p.756 on the running-head offset printed ≈ leaf+543) has the neighbourhood of Nourai's page with the headword 'خشنو ... مخفف خشنود است که راضی وخوشحال باشد' — the Borhān has the word and glosses it 'content, cheerful', but the Latin-script part of Moʿin's footnote is not legible in this OCR, so the Avestan claim cannot be read off the page.\"},\n      {\"ref\": \"FFD:52\", \"status\": \"contradicts\",\n       \"note\": \"FFD_pages.txt [pdf page 57] = printed p.52 (Abolghāsemī, Feʿl-hā-ye Fārsi-ye Dari), s.v. خوشیدن: '«خوشید» مادهٔ ماضی جعلی است ... خوش < فارسی میانه hušk < ایرانی باستان *huš-ka-. ریشهٔ huš به معنی «خشک شدن» است. واژهٔ «خشک» از ریشهٔ huš گرفته شده است.' The reference Nourai cites for خوشیدن puts it under 'to become dry', not under xšnav-.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no. 509 (HUB.txt line 2005)\", \"stance\": \"partial\",\n       \"note\": \"'Das Wort wird gewöhnlich so geschrieben, als ob die ältere Aussprache xʷašnūd = pāz. xʷašnūd wäre. Lag neben *huxšnūta- ‚wohl befriedigt', ein *xʷa-xšnuta- ‚selbstzufrieden'?' — Hübschmann accepts *huxšnūta- but warns that the خوش- spelling is secondary.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *xšnau2, Middle Persian and NWIR sections\", \"stance\": \"partial\",\n       \"note\": \"'BMP hwsnwtk /hošnūd/ /hušnūd/ … ‘satisfied, content’ … NWIR: NP xušnūd ‘content, pleased, happy’' — same Iranian chain as Nourai, different PIE root.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, English index (PHD.txt lines 1372-1373)\", \"stance\": \"supports\",\n       \"note\": \"MacKenzie's English-Pahlavi index gives 'hunsand, hu-šnūd, widwar' for 'content(ed)' and 'hunsandih, hušnūdih, šnōmag ...' for 'contentment' — the Middle Persian stage of the word is secure.\"},\n      {\"src\": \"ARY\", \"where\": \"grep خشنود in ARY_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"Aryanpur's Indo-European root dictionary has no entry for خشنود (grep returns nothing).\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Sogdian\", \"words\": \"`xšn`w\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Sogdian ʾxšnʾw- 'to satisfy' is real: Gharib's Sogdian Dictionary entry 2088, on the printed page 83 that Nourai cites, gives 'ʾxšnʾw- (Manichaean) ... Av. xšnāvaya-' and cross-refers to entry 2099 ʾxšwndyy 'forgiveness' < *xšnutaka-. The Sogdian verb is the eastern Iranian continuation of the same Old Iranian stem *xšnau-, with the prothetic ʾ- normal before an initial cluster in Sogdian (cf. ʾxšywnʾk 'king' beside xšaywan-). Two reservations: Gharib's Avestan reference marks a cognate, not a source — Sogdian descends from Old Iranian, not from Avestan, so the arrow Avestan → Sogdian is a sister relation drawn as descent; and the ultimate root is Cheung's *xšnau² 'to satisfy', not the 'scratch' root of the chart.\",\n     \"derivation_fa\": \"ʾxšnʾw- سغدی «خشنود کردن» واژه‌ای واقعی است: قریب در فرهنگ سغدی، مدخل ۲۰۸۸ در همان صفحهٔ ۸۳ که نورایی ارجاع داده، آن را با ارجاع به xšnāvaya- اوستایی آورده و به مدخل ۲۰۹۹ (ʾxšwndyy «آمرزش» از *xšnutaka-) ارجاع می‌دهد. فعل سغدی دنبالهٔ ایرانیِ شرقیِ همان ستاکِ ایرانی باستان *xšnau- است و همزهٔ آغازی آن، الفِ میانجیِ معمول سغدی پیش از خوشهٔ آغازین است (قس ʾxšywnʾk «شاه» در برابر xšaywan-). دو نکته: نخست آن‌که ارجاع قریب به اوستایی نشانهٔ هم‌ریشگی است نه سرچشمه — سغدی از ایرانی باستان می‌آید نه از اوستایی — و پیکانِ «اوستایی ← سغدی» در واقع رابطهٔ خواهری را چون رابطهٔ فرزندی نشان داده است؛ دوم آن‌که ریشهٔ نهایی به گفتهٔ چونگ *xšnau² «خشنود کردن» است نه ریشهٔ «خاراندن». با احتیاط پذیرفتنی است.\",\n     \"sources\": [W+\"%D8%AE%D8%B4%D9%86%D9%88%D8%AF\"],\n     \"ref_check\": [\n      {\"ref\": \"SOD:83\", \"status\": \"supports\",\n       \"note\": \"SOD_pages.txt leaf 148, which carries the printed page number '83' in the running head, entry '2088 ʾaxšnʾaw- M ... ○xšnaw ① Av. xšnāvaya- ⇒ ʾaxšwndyy'. Gharib's page and entry are exactly where Nourai points, and he refers the verb to Avestan xšnāvaya- — the node's parent.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SOD\", \"where\": \"Gharib entry 2099 ʾaxšwndyy, same page\", \"stance\": \"supports\",\n       \"note\": \"'2099 ʾaxšwndyy M ... (s)xšunde © <*xšnutaka- … forgiveness' — the same stem with the *-ta- participle, confirming the Sogdian family.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *xšnau2, Sogdian section\", \"stance\": \"partial\",\n       \"note\": \"'SOGDIAN: SSogd. ʾaxšnyβnt ‘hospitable, dienerfreundlich’' — Cheung records the Sogdian branch of the 'satisfy' root but assigns it to *ksenu-, not to *kes- 'scratch'.\"},\n      {\"src\": \"BRT\", \"where\": \"AiW col. 557-560 s.v. xšnav-\", \"stance\": \"supports\",\n       \"note\": \"Bartholomae's Iter. stem 'xšnāvaya-' is the form Gharib cites as the Sogdian verb's Avestan counterpart.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Greek\", \"words\": \"ksniô; kseô\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Both entries belong to the root, but one of them is a reconstruction printed as if it were a Greek word. 'ksniô' is Pokorny's *ksn̥i̯ō, the preform he sets up for the attested Greek ξαίνω 'I card (wool), comb, scratch' (aor. ἔξηνα, noun ξάνιον 'wool-comb'); Wiktionary reconstructs the same thing as PIE *ksn̥-ye/o- > Proto-Hellenic *ksəňňō > ξαίνω. Nobody writes a Greek verb ksniô, so the chart's 'Greek' box for this word is really a PIE-extension box. 'kseô' is genuine: ξέω 'to scrape, plane, polish' (< *ks-es-o), whose sense Mann gives as 'scrape, rake, polish' — so Nourai's one-word gloss 'rake' comes from Mann and is thin but not wrong. The chart's Greek node also has to carry the ξύω/ξυστήρ material that the English node below hangs on, but ξύω belongs to the *kseu- extension, which Wiktionary treats as its own root *ksew-.\",\n     \"derivation_fa\": \"هر دو مدخل به این ریشه می‌رسند، اما یکی از آن‌ها بازسازی است که چون واژهٔ یونانی چاپ شده. «ksniô» همان *ksn̥i̯ō پوکورنی است، یعنی صورتِ بازسازی‌شده‌ای که او برای ξαίνω یونانیِ گواهی‌شده («پشم حلّاجی کردن، شانه کردن، خراشیدن»؛ اسمِ ξάνιον «شانهٔ پشم») می‌گذارد؛ ویکی‌واژه نیز همان را *ksn̥-ye/o- هندواروپایی > *ksəňňō هلنی آغازین > ξαίνω بازسازی می‌کند. هیچ فعلی به شکل ksniô در یونانی نوشته نمی‌شود، پس خانهٔ «یونانی» برای این واژه در حقیقت خانهٔ گسترشِ هندواروپایی است. اما «kseô» واقعی است: ξέω «تراشیدن، صیقل دادن» (از *ks-es-o) که مان معنی آن را «scrape, rake, polish» می‌دهد؛ پس معنیِ تک‌واژه‌ایِ «rake» نزد نورایی از مان گرفته شده و ناقص است ولی نادرست نیست. با احتیاط پذیرفتنی است.\",\n     \"sources\": [W+\"%CE%BE%CE%B1%CE%AF%CE%BD%CF%89\", W+\"%CE%BE%CF%8D%CF%89\", W+\"Reconstruction:Proto-Indo-European/kes-\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:587\", \"status\": \"partial\",\n       \"note\": \"The Greek material is on pp.586-587 of Pokorny, but the two words Nourai lists are on p.586, not 587: 'ks-en- in gr. ξαίνω (*ksn̥i̯o) ,kratze, kämme; walke, prügle', ξάνιον ,Kamm zum Wollekrempeln'' and 'ks-es- in: gr. ξέω (*ks-es-o), Aor. ἔξεσσα ,schaben, glätten''. Page 587 carries the continuation (ξύω, ξυρόν, ξόανον), which is what the English node needs. Note that Pokorny writes *ksn̥i̯o with the syllabic-n mark that Nourai has dropped, which is how a reconstruction became a 'Greek' word.\"},\n      {\"ref\": \"IEC:572\", \"status\": \"supports\",\n       \"note\": \"IEC.txt leaf 325, whose two printed page numbers are 572 and 573, s.v. 'ksesió ‘grind, crush, pound, scrape’. Cf. ksestós. WP I, 450 Per. xasam, -idan ‘chew’; ... Gk. kséo, adj. ksestós ‘scrape, rake, polish’'. Nourai's 'kseô: rake' and his node 9 (xasîdan) both come from this single Mann entry.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"pp.585-587 s.v. ḱes-\", \"stance\": \"supports\",\n       \"note\": \"The four extensions ks-en-, ks-n-eu-, ks-es-, ks-eu- are laid out in this order; ξαίνω and ξέω are the Greek members of the first and third.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann p.574 s.v. ksənō, ió\", \"stance\": \"supports\",\n       \"note\": \"'ksənō, ió ‘scratch, scrape, dig’. Cf. ksnt-. WP I, 450 Skt. khánami ... Gk. ksaíno, fut. ksanó ‘lacerate; card wool’; ksánion ‘wool-comb’' — Mann's headword ksən(i)ō is Nourai's 'ksniô'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kes-1\", \"stance\": \"partial\",\n       \"note\": \"Watkins keeps only the *kseu- branch for Greek ('Extended form *kseu- in Greek xuein, to scrape: XYSTER') and does not list ξαίνω or ξέω.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Pahlavi\", \"words\": \"šânak\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The Middle Persian word is beyond doubt: MacKenzie, Concise Pahlavi Dictionary, 'šānag [šʾnk' | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade', and the English index 'comb šānag'. What is wrong is the arrow. Pahlavi is not descended from Greek; at best šānag would be a cognate of ξαίνω, which is how Horn and Hübschmann present it (Horn no. 771: 'šāne \\\"Kamm\\\". phlv. šānak \\\"Kamm\\\" (AV.); gr. ξαίνω, κτείς (Hesych), indog. kes-n (Hübschmann, ZDMG. 44, 560)'). And the modern account takes it out of this root altogether: MP šānag continues Proto-Iranian *fšāna- from PIE *peḱ- 'to pluck (wool, hair)', the root of Avestan fšu-/pasu- and of Greek πέκω, κτείς — the same source Hübschmann's comparison with κτείς really points to, since Iranian *fš- regularly gives Persian š- (cf. šubān 'shepherd' < *fšu-pāna-). So the node is doubly disputed: wrong parent language and, on the current view, wrong root.\",\n     \"derivation_fa\": \"خودِ واژهٔ فارسی میانه بی‌گمان است: مکنزی در فرهنگ کوچک پهلوی می‌آورد «šānag [šʾnk'] ۱. شانه ۲. چنگک ۳. استخوان کتف» و در نمایهٔ انگلیسی «comb šānag». آنچه نادرست است پیکان است. پهلوی از یونانی نمی‌آید؛ در بهترین حالت šānag هم‌ریشهٔ ξαίνω است، چنان‌که هرن و هوبشمان نشان می‌دهند (هرن، شمارهٔ ۷۷۱: «شانه «Kamm». پهلوی šānak «Kamm» (ارداویراف)؛ یونانی ξαίνω، κτείς؛ هندواروپایی kes-n»). افزون بر این، ریشه‌شناسی امروزی آن را یکسره از این ریشه بیرون می‌برد: šānag پهلوی دنبالهٔ ایرانی آغازینِ *fšāna- از هندواروپایی *peḱ- «کندن (پشم و مو)» است، همان ریشهٔ fšu-/pasu- اوستایی و πέκω و κτείς یونانی — و همین است آنچه مقایسهٔ هوبشمان با κτείς در واقع به آن اشاره دارد، زیرا *fš- ایرانی به‌طور منظم در فارسی «ش» می‌شود (قس «شبان» از *fšu-pāna-). پس این خانه از دو سو رد می‌شود: هم زبانِ مادرِ نادرست و هم — بنا بر دیدگاه امروزی — ریشهٔ نادرست.\",\n     \"sources\": [W+\"%D8%B4%D8%A7%D9%86%D9%87\"],\n     \"ref_check\": [\n      {\"ref\": \"HRN:170\", \"status\": \"partial\",\n       \"note\": \"Horn, Grundriss p.170 (HRN.txt leaf 191), no. 771: 'šāne ‚Kamm'. phlv. šānak ‚Kamm' (AV.); gr. ξαίνω, κτείς (Hesych), indog. kes-n (Hübschmann, ZDMG. 44, 560). bel. šāk ‚Kamm''. Horn does have the Pahlavi word and does compare Greek and an IE *kes-n — but as a cognate set, not as a borrowing from Greek.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p.79 s.v. šānag; English index 'comb'\", \"stance\": \"supports\",\n       \"note\": \"'šānag [šʾankʹ | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade' and 'comb šanag' — the Middle Persian form and meaning are certain.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien §129 (HUB.txt line 8419)\", \"stance\": \"partial\",\n       \"note\": \"§129 'Idg. kḱ = iran. ap. š = np. š: ... šāna ‚Kamm' = gr. κτείς' — Hübschmann equates šāna with Gk. κτείς (which is from *pḱten-), not with ξαίνω; and §128 on the same page gives the parallel šubān < *fšupāna-, the very sound law that yields *fšāna- > šānag.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt [pdf page 372] = printed p.373, s.v. شانه\", \"stance\": \"partial\",\n       \"note\": \"Aryanpur's شانه page gives Pahlavi šānag/šānak with Germanic and Latin comparanda and adds the caution 'رابطهٔ میان واژه‌های ایرانی و دیگر واژه‌های این فهرست احتمالی است' ('the relation between the Iranian words and the rest of this list is only probable').\"},\n      {\"src\": \"NYB\", \"where\": \"grep šānak in NYB_vol2_glossary.txt\", \"stance\": \"silent\",\n       \"note\": \"Nyberg's glossary does not contain the word (grep returns nothing).\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Persian\", \"words\": \"šâneh «شانه ۱»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The step drawn here — Pahlavi šānak > Persian شانه — is certain and regular: Middle Persian šānag loses its final -g after the unstressed vowel (like bandag > banda 'servant', xānag > xāna 'house'), giving New Persian šāna/šāne 'comb'. The Borhān-e Qāṭeʿ page Nourai cites has the entry and Moʿin's footnote gives the Pahlavi source. The other senses of MP šānag ('pitchfork', 'shoulder-blade') survive as the homonymous Persian شانه too, which is why Nourai numbers his headword «شانه ۱». Only the ultimate root above this node is contested (see node 5).\",\n     \"derivation_fa\": \"گامی که در این خانه کشیده شده — پهلوی šānak > فارسی «شانه» — قطعی و منظم است: ‎-g‎ پایانیِ فارسی میانه پس از واکهٔ بی‌تکیه می‌افتد (همچون bandag > بنده، xānag > خانه) و šāna/šāne «شانه» به دست می‌آید. برگی از برهان قاطع که نورایی ارجاع داده همین مدخل و حاشیهٔ معین با صورت پهلوی را دارد. معناهای دیگرِ šānag پهلوی («چنگک»، «استخوان کتف») نیز در فارسی به‌صورت «شانه»های هم‌آوا مانده‌اند و از همین رو نورایی سرواژه را «شانهٔ ۱» شماره زده است. تنها ریشهٔ نهایی بالای این خانه مورد اختلاف است (نگاه کنید به خانهٔ پیشین). این گام درست است.\",\n     \"sources\": [W+\"%D8%B4%D8%A7%D9%86%D9%87\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1230\", \"status\": \"supports\",\n       \"note\": \"Borhān-e Qāṭeʿ, printed p.1230 (BQT_v3 pdf page 21 per BQT_v3_pagemap.json), headword 'شانه ۱ — معروف و آن چیزی باشد که از چوب و غیره سازند و بدان ... زلف و گیسو را پردازند' with the further senses 'shoulder-blade' and the weaver's reed, and Moʿin's footnote 1 beginning 'پهلوی shānak ...' with an Indo-European comparison. Exactly Nourai's page and word.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. šānag\", \"stance\": \"supports\",\n       \"note\": \"'šānag [šʾankʹ | N ~a] 1. comb ...' — MacKenzie's '| N ~a' notation states the New Persian outcome شانه directly.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss p.170 no. 771\", \"stance\": \"supports\",\n       \"note\": \"'šāne ‚Kamm'. ... phlv. šānak ‚Kamm' (AV.)' — Horn's entry is headed by the New Persian word and derives it from the Pahlavi.\"},\n      {\"src\": \"BQT\", \"where\": \"Moʿin's footnote, p.1230\", \"stance\": \"supports\",\n       \"note\": \"Footnote to شانه ۱ gives 'پهلوی shānak' plus Baluchi shānag and Awromānī forms.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"xyster\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English xyster (surgery, 'an instrument for scraping bones') is a straight learned borrowing of Greek ξυστήρ 'scraper, graving tool', an agent noun in -τήρ from ξύω 'to scrape, polish', which is Pokorny's ks-eu- extension of ḱes- (Skt. kṣurá- 'razor', Gk. ξυρόν 'razor'). Klein's entry is exactly Nourai's node, and Watkins routes XYSTER to kes-1 through '*kseu- in Greek xuein'. The only refinement is that ξύω belongs to the *kseu- branch, so English xyster does not descend from Nourai's Greek box (ξαίνω/ξέω) but from its sister ξύω on the next page of Pokorny.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی xyster («ابزار تراشیدن استخوان» در جرّاحی) وامی کتابی و مستقیم از ξυστήρ یونانی است، اسم فاعلی با پسوند ‎-τήρ‎ از ξύω «تراشیدن، صیقل دادن»، که همان گسترشِ ks-eu- از ریشهٔ ḱes- نزد پوکورنی است (سنسکریت kṣurá- «تیغ»، یونانی ξυρόν «تیغ»). مدخل کلاین دقیقاً همین خانهٔ نورایی است و واتکینز نیز XYSTER را از راه «*kseu- در xuein یونانی» به ریشهٔ kes-1 می‌برد. تنها نکتهٔ دقیق‌تر آن است که ξύω به شاخهٔ *kseu- تعلق دارد، پس xyster از خانهٔ یونانیِ نمودار (ξαίνω/ξέω) نمی‌آید بلکه از خواهرِ آن ξύω در صفحهٔ بعدِ پوکورنی. ادعای نورایی درست است.\",\n     \"sources\": [W+\"%CE%BE%CF%8D%CF%89\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1758\", \"status\": \"supports\",\n       \"note\": \"Klein, vol. II (KLN_1971.txt, x- section, printed ≈ p.1758) s.v. xyster: 'xyster, n., an instrument for scraping bones (surg.) — Gk. ξυστήρ, “graving tool”, fr. ξύειν, “to scrape, scratch, polish”, whence also ξυρόν, “razor” ... and cogn. with [Skt.] kṣuráh, “razor”; fr. I.-E. base *qseu-. Cp. Xyris, xoanon. For derivatives of *qsneu-, an enlargement of base *qseu-, see novaculite.' Klein's *qseu- is Nourai's root name 'Qseu'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kes-1, item 2\", \"stance\": \"supports\",\n       \"note\": \"'Extended form *kseu- in Greek xuein, to scrape: XYSTER.'\"},\n      {\"src\": \"POK\", \"where\": \"pp.586-587, ks-eu-\", \"stance\": \"supports\",\n       \"note\": \"'ks-eu- in: ai. kṣurá- m. .Schermesser, Dornpflanze' ... gr. ξύω .schabe, reibe, glätte', Partiz. ξυστός ... ξυστήρ .Schabeisen''. ξυστήρ is named on p.586-587.\"},\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 566 s.v. novaculite\", \"stance\": \"supports\",\n       \"note\": \"'from I.-E. *qsneu-, enlargement of base *qseu-, whence also OI. kṣnōtram, “whetstone”, kṣnāuti, “grinds, whets” (pp. kṣnutāh) ... For derivatives of the primitive base *qseu-, see xyster.'\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"Persian\", \"words\": \"šŭr «شور (شوره)»; shŭr-bâ «شوربا»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Nourai is faithfully copying Pokorny, who does print 'npers. šōr \\\"salzig\\\", kurd. šūr' among the ks-eu- forms on p.586, next to Sanskrit kṣurá- 'razor' — the semantic bridge being 'sharp' → 'sharp-tasting, salty', which is why Nourai glosses it 'with sharp taste, salty'. Modern Iranian etymology rejects this. Persian شور continues Middle Persian šōr 'salty' (MacKenzie: 'šōr [šwl] salty; ~ag salt (land)'), but as a Parthian/north-western form: the inherited stem is Proto-Iranian *sauraH- 'salty, sour' < PIE *súHros (whence English sour, German sauer, Russian syroj), whose Persian-proper reflex would begin with s-; the š- betrays borrowing from Parthian, exactly like šahr, šāh-rāh. Aryanpur's root dictionary sets شور beside English sour, Old English sūr, German sauer and Russian syroj, and says so explicitly. شوربا is a transparent Persian compound šōr 'salty' + bā 'broth, stew' (Borhān-e Qāṭeʿ's own footnote: «شوربا - از: شور + با (آش)، معرّب آن شورباج») and gave Arabic شورباج / شوربة and Turkish çorba; Nourai's cross-reference ☞Pekw for bā (< *pakwa- 'cooked', PIE *pekʷ-) is right. So the compound is right and the root is wrong.\",\n     \"derivation_fa\": \"نورایی در این‌جا وفادارانه از پوکورنی نقل می‌کند: پوکورنی در صفحهٔ ۵۸۶ در میان صورت‌های ks-eu-، در کنار kṣurá- سنسکریت («تیغ»)، عبارتِ «npers. šōr «شور»، kurd. šūr» را چاپ کرده است؛ پلِ معنایی همان «تیز» ← «تیزمزه، شور» است و از این‌رو نورایی آن را «با مزهٔ تند، شور» معنی کرده. اما ریشه‌شناسی ایرانیِ امروز این را نمی‌پذیرد. «شور» فارسی دنبالهٔ šōr فارسی میانه است (مکنزی: «šōr شور؛ šōrag شوره‌زار»)، اما به‌صورت وام‌واژه‌ای پارتی/شمال‌غربی: ستاکِ موروثی ایرانی آغازین *sauraH- «شور، ترش» از هندواروپایی *súHros است (که sour انگلیسی، sauer آلمانی و syroj روسی از آن‌اند) و بازتاب فارسیِ سره‌اش می‌بایست با «س» آغاز شود؛ «ش» نشانهٔ وام‌گیری از پارتی است، درست همچون «شهر» و «شاهراه». آریان‌پور نیز در فرهنگ ریشه‌های هندواروپایی، «شور» را در کنار sour و sūr انگلیسی کهن و sauer آلمانی و syroj روسی می‌نشاند. «شوربا» ترکیبی شفاف است از «شور» + «با (آش)» — چنان‌که حاشیهٔ خودِ برهان قاطع می‌گوید — و معرّب آن «شورباج/شوربة» و ترکی çorba از همین است؛ ارجاع نورایی به ریشهٔ Pekw برای جزء «با» (از *pakwa- «پخته») درست است. پس ترکیب درست است و ریشه نادرست: پژوهش امروزی این را رد می‌کند.\",\n     \"sources\": [W+\"%D8%B4%D9%88%D8%B1\", W+\"%D8%B4%D9%88%D8%B1%D9%87\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:585\", \"status\": \"supports\",\n       \"note\": \"POK_02.txt leaf 244-245, at the very foot of printed p.586 under 'ks-eu-': 'ai. kṣurá- m. .Schermesser, Dornpflanze'; npers. šor .salzig', kurd. šūr ds.' — Pokorny really does derive Persian شور from this root, so Nourai's citation is accurate (the line is on p.586, one page past the 585 he gives).\"},\n      {\"ref\": \"BQT:1307\", \"status\": \"supports\",\n       \"note\": \"Borhān-e Qāṭeʿ p.1307 (BQT_v3 pdf page 98), headword 'شور — بضم اول و ثانی مجهول بر وزن مور. طعمی و لذتی باشد معروف ... و آشوب و غوغا و فریاد را گویند', with 'شور باج - با جیم ساکن، معرب شوربا است که آب گوشت پخته باشد' on the same page and the footnote 'شوربا - از: شور (شامل) + با (آش)، معرب آن شورباج ... و شوربه'. Both of Nourai's words and his Khāqānī line's vocabulary (شوربا) are on the cited page.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. šōr; English index 'salty šōr'\", \"stance\": \"partial\",\n       \"note\": \"'šōr [šwl] salty. ~ag [-kʹ] salt (land)' and 'salty šor' — confirms the Middle Persian stage but says nothing about the Indo-European root.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt [pdf page 384] = printed p.385, s.v. شور\", \"stance\": \"contradicts\",\n       \"note\": \"Aryanpur's شور page lists Pahlavi šōr, Kurdish, Sanskrit, Greek, Old Church Slavonic and Germanic cognates and notes 'واژهٔ انگلیسی SOUR (انگلیسی کهن: SŪR) نیز از همین واجریشه است' — i.e. شور belongs with English sour (PIE *sūro-), not with *kes-/*kseu-.\"},\n      {\"src\": \"BQT\", \"where\": \"Moʿin's footnote to شوربا, p.1307\", \"stance\": \"supports\",\n       \"note\": \"'شوربا - از: شور + با (آش)، معرب آن شورباج (ه.م.) و شوربه' — supports the compound analysis and the Arabic borrowing back out of Persian.\"},\n      {\"src\": \"IEC\", \"where\": \"grep 'salty' near ks-eu- in IEC.txt\", \"stance\": \"silent\",\n       \"note\": \"Mann has no entry connecting a Persian 'salty' word with the ks-eu- family; his ks-family entries (ksənō, ksesió, ksneuo) list only 'scratch/chew' Persian forms.\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"Persian\", \"words\": \"xasîdan «خسیدن ؟»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The word exists, and Nourai's own question mark shows he doubted it. Dehkhoda has خسیدن s.v. as a synonym of خاییدن 'to chew, to soften under the teeth', marked as a Shushtar usage and supported from the Šarafnāma-ye Manyarī; Moʿin indeed does not carry it, which is what the chart's NOTE says (I checked: MON has only بخسیدن '= بسخیدن' and یخسیدن, no خسیدن). Mann, the reference Nourai gives, puts 'Per. xasam, -idan \\\"chew\\\"' under his root ksesió 'grind, crush, pound, scrape' (WP I 450) beside Greek kséo — that is the sole authority for the derivation. But if خسیدن is simply a dialect variant of خاییدن, its ancestry is elsewhere: خاییدن goes back to Proto-Indo-Iranian *kʰād- 'to chew' (Skt. khādati), PIE *k(ʷ)end-, with no connection to *kes- 'to scratch'. Since the semantic bridge 'scrape' → 'chew' is Mann's alone and no Iranist repeats it, the node has to count as disputed.\",\n     \"derivation_fa\": \"واژه هست، و علامت پرسشِ خودِ نورایی نشان می‌دهد که او نیز در آن تردید داشته است. دهخدا «خسیدن» را به معنی «خاییدن» (نرم کردن زیر دندان) آورده و آن را کاربردی شوشتری با شاهدی از شرف‌نامهٔ مَنیَری می‌داند؛ معین آن را ندارد و همین است آنچه یادداشت نمودار می‌گوید (بررسی شد: در معین تنها «بخسیدن» و «یخسیدن» هست، نه «خسیدن»). مان — همان مرجعی که نورایی یاد کرده — «Per. xasam, -idan «جویدن»» را زیر ریشهٔ ksesió «ساییدن، خرد کردن، تراشیدن» در کنار kséo یونانی می‌آورد و این تنها سندِ این ریشه‌شناسی است. اما اگر «خسیدن» تنها گونه‌ای گویشی از «خاییدن» باشد، تبار آن جای دیگری است: «خاییدن» به هندوایرانی آغازینِ *kʰād- «جویدن» (سنسکریت khādati) و هندواروپایی *k(ʷ)end- می‌رسد و هیچ پیوندی با *kes- «خاراندن» ندارد. چون پلِ معناییِ «تراشیدن ← جویدن» تنها از آنِ مان است و هیچ ایران‌شناسی آن را تکرار نکرده، این خانه را باید ردشده شمرد.\",\n     \"sources\": [\"https://www.vajehyab.com/?q=%D8%AE%D8%B3%DB%8C%D8%AF%D9%86\", W+\"%D8%AE%D8%A7%DB%8C%DB%8C%D8%AF%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"IEC:572\", \"status\": \"supports\",\n       \"note\": \"IEC.txt leaf 325 (printed pp.572-573), s.v. 'ksesió ‘grind, crush, pound, scrape’. Cf. ksestós. WP I, 450 Per. xasam, -idan ‘chew’; Oss. cf. kæxín ... Gk. kséo, adj. ksestós ‘scrape, rake, polish’ ...' — Mann's page is exactly Nourai's citation and carries exactly his form and gloss.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"grep خسیدن in MON_part1/part2\", \"stance\": \"silent\",\n       \"note\": \"Confirms the chart's own NOTE: Moʿin has بخسیدن ('[- بسخیدن]') and یخسیدن but no headword خسیدن.\"},\n      {\"src\": \"BQT\", \"where\": \"grep خسیدن in BQT_v1/v2/v3 pages files\", \"stance\": \"silent\",\n       \"note\": \"The Borhān-e Qāṭeʿ OCR files return no خسیدن headword either.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"grep xšan-/xas- 'chew' in CHEUNG.txt\", \"stance\": \"silent\",\n       \"note\": \"Cheung's Iranian verb dictionary has no root yielding a Persian xasīdan 'to chew'; the verb 'to chew' is treated under *xād-.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-261.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=2)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build261.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-261.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 261"
}
```


### [2026-09-06T20:53:57.926Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 15/15
node verdicts: {'confirmed': 7, 'plausible': 4, 'disputed': 4}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 14, 'not_checked': 1, 'partial': 4, 'contradicts': 1}
books consulted: {'supports': 24, 'partial': 11, 'silent': 8, 'contradicts': 2} | by book: {'KLN': 5, 'ARY': 4, 'CHEUNG': 4, 'PHD': 4, 'LAT': 3, 'POK': 3, 'IEC': 3, 'BQT': 3, 'MON': 2, 'BRT': 2, 'HUB': 2, 'AHD': 2, 'LKT': 1, 'FVQ': 1, 'PHN': 1, 'AFA': 1, 'SKT': 1, 'SOD': 1, 'NYB': 1, 'HRN': 1}
```


## [2026-09-06T20:54:20.152Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-261.json` written; `verify_check.py 261` reports 15/15 nodes, 0 PROBLEM lines.

**Page 261 (book p. 231) — verdicts**
- Roots: 2 confirmed. Nodes: 7 confirmed, 4 plausible, 4 disputed.
- Ref checks: 14 supports, 4 partial, 1 contradicts, 1 not_checked. Books consulted: 24 supports, 11 partial, 8 silent, 2 contradicts.

**Disputed**
- Kes 2 / node 1 (Avestan `hu-xšnuta`, `xšnâvaya`): Bartholomae 1831 glosses hu-xšnuta- "well-sharpened" (of spears) only; Cheung 2007 splits *xšnau¹ "hear/sharpen" (PIE *ksneu-) from *xšnau² "satisfy" (PIE *ksenu-, cf. Gk ξένος), and Kent:175 derives āxšnav- from xšnā- "learn". "hu-šnŭta" is a Pahlavi/Pāzand form, not Avestan.
- Kes 2 / node 5 (Pahlavi `šânak` under Greek): Pahlavi cannot descend from Greek (Horn 170 presents it as a cognate); modern view takes MP šānag < PIr *fšāna- < PIE *peḱ-, not *kes-.
- Kes 2 / node 8 (Persian `šŭr`, `shŭr-bâ`): Pokorny 586 really does list "npers. šōr salzig" under ks-eu-, so Nourai's ref supports him — but Wiktionary and Aryanpur p.385 derive شور from Parthian šōr < PIr *sauraH < PIE *súHros (= English *sour*). The compound شور+با and the ☞Pekw cross-ref are correct.
- Kes 2 / node 9 (Persian `xasîdan`): word is real (Dehkhoda: = خاییدن, Shushtar), and Mann IEC:572 does put it under ksesió — but خاییدن goes back to PIIr *kʰād-; no Iranist repeats Mann's "scrape → chew" bridge.

**Plausible**: Kes 1 node 5 (English *castle* comes from Norman *castel*, not from *château* — doublets); Kes 2 node 2 (خشنود chain is standard, but the extra خوش / خوشیدن are wrong — FFD:52, the page Nourai cites, derives خوشیدن from *huš- "to dry"); Kes 2 node 3 (Sogdian is a sister of Avestan, not a descendant); Kes 2 node 4 ("ksniô" is Pokorny's reconstruction *ksn̥i̯ō printed as a Greek word; the attested form is ξαίνω).

**Transcription flags / extraction errors: none.** Checked the rendered page image — the JSON matches the printed chart exactly, including the "؟" after خسیدن, the extra Persian words خوشیدن ، خوش in the xošnŭd box, and the reference-less English box (node 5).

Notable ref finding: FFD:52 *contradicts* the node it is cited for. Also useful page mappings confirmed for reuse: KNT lexicon leaf = printed + 29 (leaf 193 = p.164); SOD:83 = SOD_pages leaf 148 (printed number visible on the leaf). 14 web sources archived via `fetch_source.py`.
