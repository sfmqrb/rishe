# Verification process log — verify-page-110


## [2026-09-05T17:27:24.883Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 110 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-110.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-110.json. Write /home/sfmqrb/git/rishe/data/verification/page-110.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 110` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T17:27:26.009Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T17:27:26.674Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T17:27:26.689Z] TOOL RESULT

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


## [2026-09-05T17:27:27.072Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-110.txt"
}
```


### [2026-09-05T17:27:27.098Z] TOOL RESULT

```
1	=== PDF page 110 (book page 80) ===
2	--- entry 0 ---
3	ROOT [Semitic] D.b.r, Dibbĕr, Dâbhar : to buzz; he spoke; word  (refs KLN:406)
4	#1 (parent #0) [Arabic] refs=KLN:406 | dabbŭr, zunbŭr : bee ; z.b.n : bee
5	  #2 (parent #1) [Persian] refs=FVA:180 | zanbŭr «زنبور» : bee
6	#3 (parent #0) [Hebrew] refs=KLN:406 | Debhôrâh, Davôrâ : bee, name of a prophetess in Bible
7	  #4 (parent #3) [English] refs=AHD:340 | Deborah, Debbie
8	--- entry 1 ---
9	ROOT [Indo-European] Dě 1 : to bind, tie  (refs POK:183)
10	#1 (parent #0) [Sanskrit] refs=POK:183 | dâman : bind, trap
11	  #2 (parent #1) [Persian] refs=BQT:817 | dâm «دام ۲» : trap
12	#3 (parent #0) [Greek] refs=POK:183 | dein : to bind ; dia-dein, dia-děma : a headband tied on two sides ☞Dwo
13	  #4 (parent #3) [Persian] refs=BQT:921; MON:1603 | dayhîm «دیهیم» : crown
14	  #5 (parent #3) [Latin] refs=AHD:363 | diadema : crown
15	    #6 (parent #5) [English] refs=KLN:440 | diadem : crown, royal headband
16	--- entry 2 ---
17	ROOT [Indo-European] De 2, Do 1 : demonstrative stem  (refs POK:181)
18	#1 (parent #0) [Avestan] refs=POK:182 | ka-da, ka-tha : when ☞Kwo
19	  #2 (parent #1) [Persian] refs=BQT:1748; HRN:96 | kay 1 «کی ۱» : when
20	#3 (parent #0) [Avestan] refs=POK:183; KLN:1622 | yeth : at present ; yathât : from where ; dim : him, her, he, she ; dit : it ; -da 5 : toward, to
21	#4 (parent #0) [Germanic] refs=AHD | tô : to
22	  #5 (parent #4) [English] refs=None | to, too
23	
```


## [2026-09-05T17:27:30.106Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-110.json",
 "description": "Read source JSON for page 110"
}
```


### [2026-09-05T17:27:30.145Z] TOOL RESULT

```
{
  "pdf_page": 110,
  "book_page": 80,
  "entries": [
    {
      "root": {
        "name": "D.b.r, Dibbĕr, Dâbhar",
        "lang": "Semitic",
        "refs": "KLN:406",
        "gloss": "to buzz; he spoke; word"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:406",
          "words": [
            {
              "translit": "dabbŭr, zunbŭr",
              "gloss": "bee",
              "script": null
            },
            {
              "translit": "z.b.n",
              "gloss": "bee",
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
          "refs": "FVA:180",
          "words": [
            {
              "translit": "zanbŭr",
              "gloss": "bee",
              "script": "زنبور"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:406",
          "words": [
            {
              "translit": "Debhôrâh, Davôrâ",
              "gloss": "bee, name of a prophetess in Bible",
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
          "refs": "AHD:340",
          "words": [
            {
              "translit": "Deborah, Debbie",
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
        "name": "Dě 1",
        "lang": "Indo-European",
        "refs": "POK:183",
        "gloss": "to bind, tie"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:183",
          "words": [
            {
              "translit": "dâman",
              "gloss": "bind, trap",
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
          "refs": "BQT:817",
          "words": [
            {
              "translit": "dâm",
              "gloss": "trap",
              "script": "دام ۲"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:183",
          "words": [
            {
              "translit": "dein",
              "gloss": "to bind",
              "script": null
            },
            {
              "translit": "dia-dein, dia-děma",
              "gloss": "a headband tied on two sides",
              "script": null,
              "see": ["Dwo"]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:921; MON:1603",
          "words": [
            {
              "translit": "dayhîm",
              "gloss": "crown",
              "script": "دیهیم"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "Latin",
          "refs": "AHD:363",
          "words": [
            {
              "translit": "diadema",
              "gloss": "crown",
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
          "refs": "KLN:440",
          "words": [
            {
              "translit": "diadem",
              "gloss": "crown, royal headband",
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
        "name": "De 2, Do 1",
        "lang": "Indo-European",
        "refs": "POK:181",
        "gloss": "demonstrative stem"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:182",
          "words": [
            {
              "translit": "ka-da, ka-tha",
              "gloss": "when",
              "script": null,
              "see": ["Kwo"]
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
          "refs": "BQT:1748; HRN:96",
          "words": [
            {
              "translit": "kay 1",
              "gloss": "when",
              "script": "کی ۱"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:183; KLN:1622",
          "words": [
            {
              "translit": "yeth",
              "gloss": "at present",
              "script": null
            },
            {
              "translit": "yathât",
              "gloss": "from where",
              "script": null
            },
            {
              "translit": "dim",
              "gloss": "him, her, he, she",
              "script": null
            },
            {
              "translit": "dit",
              "gloss": "it",
              "script": null
            },
            {
              "translit": "-da 5",
              "gloss": "toward, to",
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
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {
              "translit": "tô",
              "gloss": "to",
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
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "to, too",
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


## [2026-09-05T17:27:30.607Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T17:27:30.642Z] TOOL RESULT

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


## [2026-09-05T17:27:36.096Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','POK','AHD','BQT','MON','HRN','FVA','FVQ','WLD','IEC','SYN','BRT','SKT','LEW','LAT','PHD','NYB','HUB','ARY','AFM','PLA','LKT','FSD','WEB','RCH']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-05T17:27:37.929Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.history.resource.17812; 1852 Johnson dictionarypersia00johnuoft)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 =
```


## [2026-09-05T17:27:42.140Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Deborah\" KLN_1966.txt | head -20; echo \"=== 1971 ===\"; grep -n \"Deborah\" KLN_1971.txt | head -20"
}
```


### [2026-09-05T17:27:42.351Z] TOOL RESULT

```
10442:Deborah,  fern.  PN. ;  in  the  Bible,  a  prophetess and  judge  in  Israel.  —  Heb.  Dlbhdrdh,  lit.  ‘bee’, rel.  to  Syr.  debbori,  ‘wasp’,  debborithd,  ‘bee’, Aram,  dibborithd,  Arab,  zunbdr,  dabbur,  ‘bee’, from  the  Sem.  base  d-b-r-,  meaning  ‘to  hum, buzz',  whence  also  dibber,  ‘he  spoke’,  dabh&r, ‘word,  thing’.
=== 1971 ===
64982:Deborah, fern. PN.; in the Bible , a prophetess
```


## [2026-09-05T17:27:42.696Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n '1,60p' tools/verify_check.py; echo ---; ls data/verification/ | head -40"
}
```


### [2026-09-05T17:27:42.745Z] TOOL RESULT

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
---
agent
page-100.json
page-101.json
page-102.json
page-103.json
page-106.json
page-107.json
page-126.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
page-36.json
page-37.json
page-38.json
page-39.json
page-40.json
page-41.json
page-42.json
page-43.json
page-44.json
page-45.json
page-46.json
page-47.json
page-48.json
page-49.json
page-50.json
page-51.json
page-52.json
page-53.json
page-54.json
page-55.json
page-56.json
page-57.json
page-58.json
page-59.json
page-60.json
```


## [2026-09-05T17:27:49.101Z] TOOL CALL #8: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','POK','AHD','BQT','MON']:\n    print(k, json.dumps(d[k].get('page_offset'),ensure_ascii=False)); print(' hint:', json.dumps(d[k].get('lookup_hint'),ensure_ascii=False)[:500]); print(' local:', d[k].get('local_file')); print()\n\""
}
```


### [2026-09-05T17:27:50.891Z] TOOL RESULT

```
KLN "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
 hint: "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt

POK "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
 hint: "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?ba
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt

AHD "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page."
 hint: "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New Colle
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt

BQT "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...')."
 hint: "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf i
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']

MON null
 hint: "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Ade
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
```


## [2026-09-05T17:27:57.703Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef leafof(path, pat, maxn=6):\n    data=open(path,encoding='utf-8',errors='replace').read()\n    leaves=data.split('\\f')\n    out=[]\n    for i,l in enumerate(leaves):\n        if re.search(pat,l):\n            out.append(i)\n    return out[:maxn]\nprint(\"KLN Deborah leaves\", leafof('KLN_1966.txt', r'Deborah,\\s+fern'))\nprint(\"KLN diadem leaves\", leafof('KLN_1966.txt', r'^diadem,'))\nEOF"
}
```


## [2026-09-05T17:27:58.715Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^diadem\" KLN_1966.txt | head; echo \"=== POK full lemma dē ===\"; grep -n \"lemma: d[eēě]-\" POK_full.txt | head -20"
}
```


### [2026-09-05T17:27:59.518Z] TOOL RESULT

```
KLN Deborah leaves [224]
KLN diadem leaves []
```


### [2026-09-05T17:27:59.575Z] TOOL RESULT

```
=== POK full lemma dē ===
19507:Root / lemma: de- do- 
19645:Root /lemma: de-\ «/a-and del-, di- 
19653:Root / lemma: de-. <ya-and dei-, di-\ "to bind' derived from dual , duel-, stems of Root/
```


## [2026-09-05T17:28:07.992Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in (214,215,216,223,224,225):\n    t=leaves[i].strip().split('\\n')\n    print('--- leaf',i,'first3:', t[:3])\n    print('    last2:', t[-2:])\nEOF"
}
```


### [2026-09-05T17:28:09.524Z] TOOL RESULT

```
--- leaf 214 first3: [",  excursion,  ex¬ cursus,  incur,  intercourse,  kraal,  occur,  occur¬ ence,  precursor,  recourse,  recur,  succor,  suc- cursal.  Cp.  also  car  and  words  there  referred  to. ON.  hross,  OE.  hr  os,  hors,  ‘horse’,  are  prob.  not cogn.  with  L.  currere,  but  derivatives  of  I.-E. base  *(s)qerd-,  a  -{/-enlargement  of  *(s)qer-,  ‘to leap,  jump'  (see  horse).  Derivatives :  current,  n. (q.v.),  current-ly,  adv.,  current-ness,  n. current,  n.  —  ME.  corant,  fr.  OF.  corant,  curant (F.  courant ),  pres.  part,  of  curre,  ‘to  run’,  used as  a  noun.  See  current,  adj. curricle,  n.,  a  light  two-wheeled  carriage.  —  L. curriculum,  ‘a  running,  a  course;  a  chariot  for racing’,  fr.  currere,  ‘to  run’.  See  current,  adj., and  -cle  and  cp.  curriculum.", 'Derivative:  curricle,  intr.  v. curricular,  adj.,  1)  pertaining  to  carriages;  2)  per¬ taining  to  the  curriculum.  —  Formed  with  suff. -ar  fr.  L.  curriculum.  See  next  word, curriculum,  n.,  course  of  study.  —  L.,  ‘a  course’. See  curricle.', 'currier,  n.,  1)  one  who  dresses  leather;  2)  one  who curries  horses.  —  ME.  corier,  fr.  OF.  corier,  fr. L.  coriarius,  ‘tanner,  currier’,  fr.  corium,  ‘leath¬ er;  see  corium.  E.  currier  was  influenced  in  form by  next  word.']
    last2: ['custodian,  n.  —  Formed  with  suff,  -an  fr.  L.  cus¬ todia.  See  next  word.', "custody,  n.  —  L.  custodia,  ‘watching,  guard,  care, protection’,  fr.  custos,  gen.  custodis,  ‘watch, guard,  preserver,  keeper,  overseer,  protector’, fr.  I.-E.  base  *(s)qeudh-,  ‘to  cover’,  whence  also L.  cudo ,  ‘helmet  made  of  skin’,  OI.  kuharam, ‘cave’,  kuhufr,  ‘new  moon’,  lit.  ‘that  which  is hidden’,  Gk.  xeijfleiv,  ‘to  cover,  hide,  conceal', W.  cudd,  ‘a  hiding’,  cuddio,  ‘to  hide’,  Mir.  codal, ‘skin’.  Cp.  custos.  For  derivatives  of  the  related base  *(s)qeut-  see  hide,  ‘skin’.  The  bases *(s)qeu-dh-  and  *(s)qeu-t-  are  dental  enlarge ments  of  base  *(s)qeu-,  ‘to  cover,  hide’.  See  sky and  cp.  words  there  referred  to. custom,  n.  —  ME.  custume,  custome,  fr.  OF.  cos¬ tume,  custume  (F.  coutume),  fr.  L.  consuetu- dinem,  acc.  of  consuetudo,  ‘custom,  habit,  use, usage’,  fr.  cdnsuetus,  pp.  of  consuescere,  ‘to  ac¬ custom’,  fr.  con-  and  suescere,  ‘to  become used  or  accustomed’,  fr.  I.-E.  base  *swedh-, whence  also  Gk.  eS>oc;,  Jj-fto?,  ‘custom,  usage’, £9vo?,"]
--- leaf 215 first3: ['‘race’.  Base  *swedh-  is  compounded  of *swe-,  ‘his,  her,  its,  one’s  own’,  and  *dhe-,  ‘to put,  place;  to  do,  make’,  hence  lit.  means  ‘to make  one’s  own’.  See  sui-  and  the  verb  do  and cp.  consuetude,  costume,  which  are  doublets  of custom.  Cp.  also  assuetude,  de  suetude,  man- suete,  mastiff,  sodality.  Cp.  also  ethical,  ethnic, hetaira.', 'customable,  adj.  —  OF.  costumable,  fr.  costume, ‘custom’.  See  prec.  word  and  -able, customary,  adj.  —  OF.  costumier  (F.  coutumier), fr.  costume,  ‘custom’.  See  custom  and  adj.  suff.', '-ary.']
    last2: ['Cyclopean,  adj.,  pertaining  to,  or  resembling,  the Cyclopes.  — -  Formed  with  suff.  -an  fr.  L. Cycldpeus,  fr.  Gk.  KuxXcotceiop,  fr.  KuxXox^.  See Cyclops.', 'cyclopedia,  cyclopaedia,  n.  —  ModL.,  abbrevia¬ tion  of  e']
--- leaf 216 first3: ['ncyclopedia  (q.v.)', 'Derivatives:  cyclop(a)ed-ic,  adj.,  cyclop(a)ed- ist,  n.', 'Cyclops,  n.,  one  of  a  race  of  one-eyed  giants  in Greek  mythology.  —  L.,  fr.  Gk.  KuxXojij/,  gen. KiSxXtamx;,  lit.  ‘round-eyed’,  fr.  xuxXo?,  ‘circle’, and  ojtj/,  gen.  dim)?,  ‘eye’,  fr.  I.-E.  base  *6kw-,  a collateral  form  of  base  *okw-,  ‘eye’.  See  cyclo- and  -opia.']
    last2: ['the  quite  incidental  fact  that  the  first  element  in the  name  Kuv6aapye?  comes  fr.  xumv,  gen. xu v6p,  ‘dog’  (see  cyno-).', 'Derivatives:  cynic,  cynic-al,  adjs.,  cynic-al-ly , adv.,  cynic-ism,  n.,  cynic-ist,  n. cyno-,  before  a  vowel  cyn-,  combining  form meaning  ‘dog-’.  —  Gk.  xuvo-,  xuv-,  fr.  xumv, gen.  xuv6<;,  ‘dog’,  which  is  cogn.  with  L.  canis, Goth,  hands,  OE.  hand,  ‘dog’.  See  hound  and cp.  canine.  Cp.  also  cynanche,  Cynias,  cyno']
--- leaf 223 first3: ['et,  daviot (whence  F.  davier,  with  change  of  suff.),  dimin. of  the  PN.  David;  so  called  in  allusion  to  the slaying  of  Goliath.  See  David  and  cp.  -et. davy,  n.,  safety  lamp.  —  Shortened  fr.  Davy  lamp; named  after  its  inventor,  the  English  chemist Sir  Humphrey  Davy  (1778-1829). davy,  n.  (slang).  —  Short  for  affidavit.', 'Davy  lamp.  —  See  davy,  ‘safety  lamp’, daw,  n„  a  kind  of  crow,  a  jackdaw.  —  ME.  dawe, rel.  to  OHG.  tdha,  MHG.  tdhe,  also  tahele, tale,  idle  (diminutives  of  tdhe),  G.  Dohle;  cp. OPruss.  doacke,  ‘starling’,  ML.  tacula.  It.  tac- cola,  ‘jackdaw’,  which  are  German  loan  words, dawdle,  intr.  and  tr.  v.,  to  waste  (time).  —  Perhaps a  var.  of  dial.  E.  doddle,  ‘to  walk  unsteadily’.', '404']
    last2: ['debate,  n.  —  ME.  debat,  fr.  MF.  (=  F.)  debat, ‘dispute,  strife,  debate’,  fr.  debattre.  See  debate,  v.', 'debauch,  tr.  v.,  to  lead  astray,  corrupt.  —  OF.  de- baucher,  ‘to  leave  work,  be  idle’  (whence  F.  de- baucher,  ‘to  turn  somebody  away  from  his  work ; to  entice  away,  lead  astray’).  The  orig.  meaning of  OF.  debaucher  was  ‘to  rough  down  timber’. It  is  a  hybrid  coined  fr.  de-,  a  pref.  of  Latin origin  (see  de-),  and  OF.  bale,  bauch,  bau  (F. bait),  ‘beam’,  fr.  Frankish  *balk,  which  is  rel. to  OHG.  balko,  OE.  balca,  ‘ridge  between  fur¬ rows’;  see  balk  and  cp.  ebauchoir.  The  sense  of OF.  debaucher  underwent  the  following  p']
--- leaf 224 first3: ['hases  of development;  ‘to  rough  down  timber;  to  split, cleave;  to  separate;  to  turn  somebody  away from  his  work  or  from  his  duty;  to  entice  away; to  lead  astray’.', 'Derivatives:  debauch ,  n.,  debauch-ed,  adj.,  de- bauch-ed-ly,  adv.,  debaitch-ed-ness,  n.,  debauchee (q.v.),  debauch-er,  n.,  debauch-ery,  n.,  debouch¬ ment,  n.', 'debauchee,  n.,  a  debauched  person.  —  F.  de- bauche,  pp.  of  debaucher,  ‘to  entice  away,  to lead  astray’.  See  debauch  and  -ee.']
    last2: ['Derivatives:  decarboniz-ation,  n.,  decarboniz¬ er ,  n.', 'decarch,  n.,  a  commander  of  ten  men;  a  decurion. —  Gk.  Sexapyr']
--- leaf 225 first3: ["]?,  compounded  of  8£xa,  ‘ten’, and  -ap/t]?,  ft-  apx'k,  ‘leader,  chief,  ruler’.  See", 'deca-  and  -arch.', 'decarchy,  n.,  a  government  of  ten.  —  Gk.  Sexap- Xia,  fr.  Sexdcpxr)?.  See  prec.  word  and  -archy. decastich,  n.,  a  poem  of  ten  lines.  —  Gk.  8exi- <mxo?,  ‘containing  ten  lines’,  fr.  Sexa,  ‘ten’,  and <jt ixoq,  ‘row,  line,  rank’.  See  deca-  and  sticbic. decastyle,  n.,  a  portico  with  ten  columns  ( arch .) — Compounded  of  deca- and  Gk.oxuXo?, ‘pillar’. See  style,  ‘gnomon’.']
    last2: ['decrement', 'decimalize,']
```


## [2026-09-05T17:28:15.580Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"diadem\" KLN_1966.txt | head -10"
}
```


### [2026-09-05T17:28:15.627Z] TOOL RESULT

```
2616:‘to  push  back’,  fr.  dvd,  ‘back’  (see  ana-),  and xpouciv  (for  *xpouast.v),  ‘to  knock,  strike, push’,  which  is  rel.  to  Homeric  xpoalvstv  (prob. for  *xpouadv-teiv),  ‘to  stamp,  strike  with  the hoof’,  and  cogn.  with  OSlav.  su-krusg,  su-kru - Siti,  Russ.  krusit\  Lith.  krusu,  kruSti,  ‘to  smash, shatter’,  OSlav.  kruchu,  ‘piece,  bit  of  food’, anadem,  n.,  a  wreath,  garland.  —  L.  anadema,  fr. Gk.  dvd8/)pa,  ‘band,  headband’,  fr.  dvaSetv, ‘to  bind  up’,  fr.  dvd  (see  ana-)  and  8eTv,  ‘to bind’.  See  diadem.
3790:Derivative:  asyndetic-al-ly,  adv. asyndeton,  n.,  omission  of  conjunctions  ( rhet .)  — Gk.  aouvSsTov,  neut.  of  dauvSexo?,  ‘uncon¬ nected’,  fr.  a-  (see  priv.  pref.  a-)  and  aovSexo?, ‘connected’,  verbal  adj.  of  ouvSetv,  ‘to  bind together,  connect’,  fr.  otiv,  ‘with’  (see  syn-),  and 8eiv,  ‘to  bind’.  See  diadem  and  cp.  polysyn¬ deton.
9237:Derivative:  coronal-ly,  adv. coronal,  n.,  circlet,  diadem.  —  L.  coronalis,  ‘per¬ taining  to  a  crown'.  See  coronal,  adj. coronary,  adj.,  1)  pertaining  to  a  crown;  2)  en¬ circling;  3)  pertaining  to  either  of  the  two  ar¬ teries  supplying  the  heart  tissues.  —  L.  coro- narius,  ‘pertaining  to  a  crown’,  fr.  corona.  See corona  and  adj.  suff.  -ary. coronate,  tr.  v.,  to  crown.  —  L.  coronatus,  pp.  of coronare,  ‘to  crown’,  fr.  corona.  See  corona  and verbal  suff.  -ate.
11050:Desmanthus,  n.,  a  genus  of  plants  of  the  mimosa family  (bot.)  —  ModL.,  compounded  of  Gk. 8£a(i7),  ‘bundle’,  and  dcvffoi ;,  ‘flower’.  See  desmo- and  anther  and  cp.  the  first  element  in  Desmo- dium  and  the  second  element  in  Teleodesmacea. desmid,  n.,  an  alga  of  the  family  Desmidiaceae (bot.)  —  ModL.  Desmidium  (name  of  the  genus) as  if  fr.  Gk.  *8sap.l8tov,  dimin.  of  Seap.6;, ‘band,  bond,  chain’  (see  desmo-);  so  called because  it  sometimes  occurs  in  chains. Desmidiaceae,  n.  pi.,  a  family  of  algae  (bot.)  — ModL.,  formed  with  suff.  -aceae  fr.  ModL. Desmidium.  See  prec.  word, desmo-,  before  a  vowel  desm-,  combining  form meaning  ‘bond’.  —  Gk.  Sea^o-,  Seap.-,  fr. Scapo;,  ‘band,  bond’,  rel.  to  Slapa,  of  s.m., SeapT),  ‘bundle’,  Sean;,  ‘a  binding',  fr.  Seeiv,  ‘to bind',  whence  also  Set f),  ‘torch’,  lit.  ‘sticks, bound  together’  (prop.  fern,  verbal  adj.  of  Slew, ‘to  bind’),  the  second  element  in  xpfj-8e-pvov, ‘headdress’,  Sia-8r,pa,‘band  or  fillet’,  (nro-Srjpa, ‘a  sandal’  (lit.  ‘that  which  is  bound  under’),  fr. l.-E.  base  *de(i)-,  *d*-,  ‘to  bind.  See  diadem  and cp.  words  there  referred  to.  Cp.  also  desma, desmid,  syndesmo-.
11220:Diadelphia,  n.,  a  class  of  plants  in  the  Linnaean system  ( bot .)  —  ModL.,  prop,  ‘plants,  the stamens  of  which  are  united  into  two  bundles’, lit.  ‘like  two  brothers’,  fr.  di-,  ‘two’,  and  Gk. aSeXcpo;,  ‘brother’.  See  adelpho-  and  -ia. diadelphous,  adj.,  1)  having  filaments  united  by two  bundles;  2)  pertaining  to  the  class  Dia¬ delphia.  —  Formed  fr.  di-,  ‘two’,  Gk.  dSeXcpo;, ‘brother’,  and  suff.  -ous.  See  prec.  word, diadem,  n.,  crown;  fillet.  —  OF.  diademe  (F.  dia- deme),  fr.  L.  diadema,  fr.  Gk.  SidSrjpa,  ‘band, fillet,  royal  headband’,  fr.  SiaSciv,  ‘to  bind on  either  side’,  fr.  Sid  (see  dia-)  and  Seiv,  ‘to bind’,  fr.  I.-E.  base  *de(i)-,  *d1-,  ‘to  bind’, whence  also  OI.  dy-dti,  ‘binds’,  di-man,  'band, bond’.  Alb.  del ,  ‘sinew,  tendon’,  duai,  ‘sheaf’. See  desmo-  and  -ma  and  cp.  anadem.  Cp.  also Aditi,  Aditya.
11221:Derivatives:  diadem,  tr.  v.,  diadem-ed,  adj. diadoche,  n.,  succession.  —  Gk.  SiaSox?),  ‘succes¬ sion’,  rel.  to  81x80/0;,  ‘succeeding,  successor’, in  gradational  relationship  to  SiaSE/ea&ai,  ‘to succeed’,  lit.  ‘to  receive  one  from  another’,  fr. Sid  (see  dia-)  and  Sbyeabou,  ‘to  take,  accept, receive’,  fr.  I.-E.  base  *dek-,  *dok-,  ‘to  take,  re¬ ceive,  accept ;  acceptable,  becoming,  good’, whence  also  L.  decere,  ‘to  be  seemly  or  fitting’. See  decent  and  cp.  words  there  referred  to. Diadochi,  n.pl.,  the  successors  of  Alexander  the Great;  hence  also  successors  (in  general).  — ModL.  Diadochi,  fr.  Gk.  SidSo/oi,  pi.  of  8id- 80x0;,  successor’.  See  prec.  word, diadochokinesia,  diadochokinesis,  n.,  the  normal
36730:stephane,  n.,  a  kind  of  hairdress  ( Greek  antiq.)  — ModL.,  fr.  Gk.  axs<pccv7],  ‘that  which  encircles; diadem’,  fr.  ax^tpciv,  ‘to  encircle,  crown, wreathe’.  See  stemma  and  cp.  stephano-  and words  there  referred  to.
36731:stephanion,  n.,  the  point  where  the  sutura  coro- nalis  crosses  the  temporal  ridge  ( craniol .)  — ModL.,  fr.  Gk.  crxcq) xvtov,  dimin.  of  ax£( potvoc;, ‘crown’,  ‘that  which  encircles,  crown,  wreath’, which  is  rel.  to  oxEtpavv),  ‘that  which  encircles; diadem’,  used  also  as  a  medical  term  to  denote the  sutura  coronalis.  For  this  use  of  crxeipavifj see  Aretaeus  Medicus,  ed,  K.  Hude,  Corpus Medicorum  Graecorum,  II,  Xpovicov  voocov HEparceimxov,  I,  2.  See  prec.  word, stephanite,  n.,  a  black  mineral.  —  G.  Stephanit, named  after  Archduke  Stephan,  mining  director of  Austria  (died  in  1867).  The  ending  -it  goes back  to  Gk.  -  txr;? ;  see  subst.  suff.  -ite. stephano-,  before  a  vowel  stephan-,  combining form  denoting  crown.  —  Gk.  0x890010-,  fr. atitpaMoq,  ‘that  which  encircles ;  crown ;  wreath’, fr.  crxEcpEtv,  ‘to  encircle;  to  crown;  to  wreathe’, See  stemma  and  cp.  Stephana,  stephane,  ste¬ phanion,  Stephanos,  Stephanotis,  Stephen  and  the second  element  in  Dasystephana.
37870:Seap.6;,  ‘band’,  which  is  cogn.  with  &ia-§7)pia, ‘a  headband,  fillet’.  See  diadem, syndesmosis,  n.,  articulation  of  parts  of  bones  by means  of  ligaments  (anat.)  —  Formed  with  suff. -osis  fr.  Gk.  auvScauoc,  ‘that  which  binds  to¬ gether’.  See  prec.  word.
```


## [2026-09-05T17:28:15.962Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19500,19560p' POK_full.txt; echo \"=====2====\"; sed -n '19640,19720p' POK_full.txt"
}
```


### [2026-09-05T17:28:16.019Z] TOOL RESULT

```
after Van Windekens Lexique 138 here Tocharian A tap- ' allow to sound, announce ' 
{*tup-) in Infin. tpassi, participle Pass, cacpunder 

References: WP. I 781 f., Endzelin KZ. 44, 58, MiJhlenbach-Endzelin I 518, Schwyzer Gr. 
Gr. 17183. 
Page(s): 221-222 

Root / lemma: de- do- 

Meaning: a demonstrative stem 

Material: Avestan vaesman-da ' up there to the house '; 



gr. -5s in 6-5£, r|-5£, t6-5£ ' that here, this ' (I - deixis), £v0a-5£, £v9£v-5£, t£T-5£, hinter 
Akk. the direction, e.g. 56fJov-5£, oIkov 5£, oIk6v5£, 'A9r|va^£ (*A9avava-5£), as Avestan 
vaesmen-da (Arcadian 0up5a £^u) Hes., reshuffling of -5£ after double forms as np6a9£ : 
npooGa), also in 5£-upo (5£upo emulated PI.) 'here', Latin quan-de, quam-de^ as like ' = 
Oscan pan, Umbrian pane 'as', also Oscan pun, Umbrian pon{n)e 'as well as' {*quom-de), 
Latin in-de^ thence, from there ' {*im-de), un-de^ whence, from where '; gr. 5£ 'but'; gr. 5r| 
' just, now, just, certainly ', n-5r| 'already', £n£i-5r| ' since, whereas, because '; 5ai after 
interrogative words '(what) then?'; 

Indo Germanic la'eput also in Old Irish article in-d{*sind-os, Indo Germanic *sem-de); 

Italian -*dam\v\ Latin quT-dam, quon-dam, Umbrian ne-rsa' as long as' (probably 
solidified Akk. f. *ne-dam ' not at the same time '; besides m. or n. in:); 

Latin dum{*dom) 'still', as Konj. 'while, during the time that; so long as, provided that; 
until', originally demonstratives 'then', compare etiam-dum, interdum, nondum, agedum{: 
gr. aY£ 5n), manedum, quidum^as so?' , then in relative-conjunctional meaning, as also in 
dummodo, dumne, dumtaxat, Oscan fsfdum ' the same as' however, is to be 
disassembled in fs-fd-um, as also in. Latin Tdem, quidem, tandem, tantusdem, totidem\s 
not to be recognized with dum Irom *domt\r\e changing by ablaut -denr. Id-em kom * id-em 
= Old Indie /d-am ' just this ', compare Oscan fs-fd-um, as quid-emiroxw *quid-om = Oscan 
pfd-um, and as a result of the syllable separation f-dem\Nou\6 be sensed as -dem an 
identity particle and would grow further); 

but the primary meaning of dum is ' a short while ', wherefore u perhaps is old (compare 
dudum) and dum belongs to root deua- (EM2 288 f.). 

Indo Germanic '(t/o originally 'here, over here' in Latin o'd-/7/-c^/77 (archaically), donee 
{*dd-ne-que), for Lukrez also donique^ so long as, till that, to, finally ', but also 'then' {do- 
equal meaning with ad-, ar- in Umbrian ar-ni-po ' as far as ' from * ad-ne-q^om) and in 
quandd^\N\r\en' = Umbrian panupei^ whenever, as often as; indef. at some time or other '; 
Old Irisho'lo, du, acymr. o'/(= dJ), corn, de'to' from *o'J(in gall, o^iz-c/'and'), Thurneysen 
Grammar 506; Old English to. Old Saxon to{te, ti). Old High German zuo{za, ze, zf, the 
abbreviated forms are in spite of Solmsen KZ. 35, 471 not to understand as previously 
proto Indo Germanic ablaut variants). Modern High German /o (Gothic du'to' with Dat. and 
proverb, e.g. in du-g fnnan ^beg\n' , seems proclitic development from *td{7), is marked from 
Brugmann l|2, 812 as unresolved); Old Lithuanian o'o preposition and prefix 'to'; Old 
Church Slavic da^ so, and, but; that ' (meaning-development '*in addition' - 'still, and', 
from which then the subordinating link); different Pedersen Tocharian 5. 



Besides Indo Germanic *dd\x\ Old Cliurch Slavic o'o "until, to'. 

Lithuanian da-, perfektivierendes verbal prefix, and Latvian o'a "until - to', also verbal 
prefix e.g. in o''5-/e/"hinzugehen', derive from dem Slavischen. 
=====2====

tango'to touch'), Pedersen Tocharian 2071. 

Page(s): 1 83 

Root /lemma: de-\ «/a-and del-, di- 

Meaning: to bind 

Note: 



Root / lemma: de-. <ya-and dei-, di-\ "to bind' derived from dual , duel-, stems of Root/ 

lemma: dud(u)\ "two' meaning "bind in two' 

Material: Old Indie oy-a//(with a-, ni-, sam-) "binds' {dy- zero grade of *dei-, from 3. PI. 

dyanti, compare Avestan nT-dya-t^m2>. Sg. Med. in pass, meaning " it has made soil 

holdback ', -a-extension from the zero grade di-, Bartholomae Airan. Wb. 761), Old Indie 

participle dita- " bound ' (= gr. 5£t6(;), daman-u. "band, strap' (= gr. -5r|MC(), ni-datar- 

'binder'; 

gr. (hom. Attic) Ssw (*5£ju)) "bind', 5£t6i; " bound ', 5£Tr| " shavings tied together as a 
torch, faggot, torch, fetter, sheaf ' (5s- for Indo Germanic *d9-as Qzioc, : TiGriM'). 
apaAAoSsTrip " sheaf binder ', btaxo, "the fastening, binding', 5£ap6(; "band, strap', Kpri5£- 
pvov "head fascia', Sspvia PI. " bedstead '; hom. present 5i5r|Mi bind' is to 5nau) after 
TiGniJi: 6nau) "neologism'; un6-5r||Ja (compare Old Indie daman-) "sandal', 5ia5r|Ma " a 
band or fillet, turban, diadem '; 

alb. duai^ fascicle, sheaf (about *o'd/7-from Indo Germanic *de-n-), o'e'/"(*band, strap), 
sinew, tendon, vein' (Indo Germanic *o'd-/c»-). 

References: WP. I 771 f., Schwyzer Gr. Gr. I 340 f., 676, 688. 
Page(s): 1 83 

Root / lemma: degh-mo-s 

Meaning: slant 

Material: Old \n6\cj/hma-h^ slantwise, slant, skew' (Proto Aryan *z/z/7/77^-assimil. from 

*dizhma-), gr. 56xMioq, 5oxm6c; "slant, skew' (assimil. from *5ax|j6c;). 

References: Pedersen KZ. 36, 78, WP. I 769. 

See also: Other possibilities see below gei-^ium, bend'. 

Page(s): 222 

Root / lemma: d^ab^-^ 

Meaning: proper, * fitting, dainty 

Material: Armenian darbin^ smith ' {Vi'"db^r-ino-)\ 

Latin faber, /^it*/"/"" craftsman, artist'. Adj. "ingenious, skilful'. Adv. fabre^sVMxjX, affabre^ 
skillfully ', contrast infabre, fabrica^ dexterity, workshop ' (Paelignian faber\s Latin 
loanword); perhaps here Latin (Plaut.) effafilatus' exposed ', Denom. from *fafilla, 
"*acquiescence' (/dial.?); 

Note: 



common Latin d- > f-\ 

alb. Tosc thembere^\\ee\, hoof (where a smith would attach a horseshoe)' [common alb. f- 
>th-. 

Gothic ga-daban^ occur, arrive, reach, happen, be suitable ', Perf. gadob^ to be clearly 
seen, to be conspicuous ', Adj. gadofis^ it is suitable, proper, fitting' = Old English gedefe 
" fitting, mild' {*ga-ddbja), gedafen^ proper', gedafn/an' be fitting, suitable' = Old Norse 
o'a/^a "proficient, proper, become strong, prosper, thrive'. Old English gedaefte^ fitting, 
mild', gedaeftan^ sori, order, arrange'; 

Old Church Slavic dobrt 'good, beautiful, beauteous, fair ' (= Armenian darbin, Latin
```


## [2026-09-05T17:28:31.478Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19560,19645p' POK_full.txt"
}
```


### [2026-09-05T17:28:31.523Z] TOOL RESULT

```
prefix e.g. in o''5-/e/"hinzugehen', derive from dem Slavischen. 

en-do. Old Latin endo, indu^\v\\ Latin only more as composition part, e.g. indi-gena, ind- 
oles, other formations in hom. to £v-5-Tva (right £v5Tva) "intestines, entrails ', Middle Irish 
inne^As." ( *en-d-io-)\ (common Celtic -ns-, -nt- > -nn-), against it wird Old Irish ind 
preposition and prefix "in' von Thurneysen Grammar 521 as after in- umgefarbte 
Entsprechung von gall. a/7o'e contemplates and further von Pedersen KG. I 450 with 
Gothic s/7o'"untir. Old Indie ^o'/?/ connected; and gr. £v5o-9i " indoors, in, within ', £v5o-9£v 
" from inside ' are reshaped as Lesbian Doric £v5oi after oiko-0i, -9£v, -i from £v-5ov, s. 
*dem-\.o build'; Hittite an-da^\n' to *en-do{or*n-dd?), Pedersen Hittite 166. Whereas it is 
the adverbial- and predicate character of nouns Old Irish /n{d), abret. in, mcymr. yn 
probably instrumental of article; s. further Thurneysen Grammar 239. 

de{as o'd probably an Instr. extension) in Latin o'e"prep. with abl. in space, down from, 
away from. Transf., coming from an origin; taken from a class or stock, made from a 
material, changed from a previous state; of information, from a source, in time, following 
from, after; in the course of, during, about a subject; on account of a cause; according to a 
standard', Faliscan ofe (besides Oscan dat^de' (for *dad, with t afier post, pert etc; Oscan- 
Umbrian *dad\s probably replacement for *o'e after ehtradetc, respectively after the 
ablative transformed in Instr. -e{d), d{d)\ad); as proverb in dafdajd' give away, give up, 
surrender, deliver, consign, yield, abandon, render', dadfl<atted^ dedicate, consecrate, set 
apart ', Umbrian daetom^ a fault, crime '; in addition compounds Latin deterior^ lower, 
inferior, poorer, worse ', Sup. detemmus, demum (Old Latin also demus) " of time, at 
length, at last; in enumerations, finally, in short; 'id demum', that and that alone ' ("*to 
lowest ' - "lastly, finally'), denique^ at last, finally; in enumerations, again, further or finally; 
in short, in fine '; 

Old Irish o'/"(besides o'efrom Indo Germanic de, wherewith perhaps gall. ppaTou-5£ " 
from a judicial sentence ' is to be equated), acymr. di, ncymr. y, i, corn, tiie, bret. o'/" from - 
down, from - away ', also as privative particle (e.g. acymr. di-auc^ slow, tardy, slack, 
dilatory, lingering, sluggish, inactive, lazy ', as Latin debiiis, intensifying Old Irish dT-mor^ 
very large ' as Latin o'e/77a^/s "furthermore, very much') 

The meaning " from - down, from - away ' these with gr. 5n, 5£ formally the same 
particle probably is only a common innovation of Celtic and Italic; also German? 



(Holthausen KZ. 47, 308: Old High German zao'a/" poverty, need' from *de-tlom, of *de^ 
from - away ', as wadar^oor, needy' : Latin i/e "enclitic, or, or perhaps'?). 

The ending of the following adverbial groups also belongs to this root: Old Indie tada 
"then', Avestan /aJa"then', Lithuanian /5o'a"then'; Old Indie /rao'a "when?', Avestan kada, 
jav. /raJa "when?', Lithuanian /rao'a"when'; Old Indie yao'a "when, as', Avestan yada,\ay. 
j/aJa"when', Old Chureh Slavic yeo'a "when' (compare also Old Indie yao'/" if. Old pers. 
yadiy, Avestan yedi, yeidi^as soon as' and Avestan y5Ja/"whenee'); Old Indie /da'now, 
yet'; also the Slavic formations as russ. /r^o(3 "whereto, where'; 

Maybe alb. ku-do{*kud^^ everywhere, anywhere', nasal nga-do{k^d^ "everywhere' 

Old Chureh Slavic k^du, /r^o'e "whence', n/kbda-ze ^ r\ever' , poln. o'o/r^o' "whereto, where'. 
Old Church Slavic f^de' from there ', sqdu^ from here ' , but it could contain also Indo 
Germanic d^^. 

A cognate stem Wperhaps in enclitic Iran. Akk. Avestan Old pers. dim^ her, she ', 
Avestan d/t'es', d/sP\. m. f., drP\. n., and Old Prussian Akk. Sg. d/n, d/en^\\r\r\, sie' (etc); 
compare but Meillet MSL 19, 53 f. 

References: WP. I 769 ff., WH. I 325 f., 339 f., 370 f., 694, 859, Schwyzer Gr. Gr. I 624 f. 
Page(s): 181-183 

Root / lemma: deg- 

Meaning: to grab? 

Material: Gothic tekan 'touch'; 

Maybe alb. takonj "touch' 

Additional cognates: [PN taka= WFris. take, EFris. taken, MDu. /a/re/7 grasp, seize, catch, 

rel. by ablaut to Goth, tekan] 

with ablaut Old Norse taka, (engl. take) "take'; Tocharian B tek-, tak- "touch', B teteka" as 

soon as '. 

Maybe alb. /a/rc»A7y"touch' : Gothic tekan "touch'; 

References: WP. I 786, WH. I 351, Van Windekens Lexique 138, 139 (compares also Latin 

tango'to touch'), Pedersen Tocharian 2071. 

Page(s): 1 83 

Root /lemma: de-\ «/a-and del-, di-
```


## [2026-09-05T17:28:53.001Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'diadem,  n.,  crown' in l:\n        print('diadem leaf',i)\n        # find page numbers printed\n        print([m for m in re.findall(r'^\\s*(\\d{3})\\s*$', l, re.M)])\n    if 'yeidi' in l or 'yaSat' in l:\n        pass\n# nearby leaf page markers\nfor i in range(238,246):\n    print(i, re.findall(r'^\\s*(\\d{3,4})\\s*$', leaves[i], re.M))\nEOF"
}
```


## [2026-09-05T17:28:53.783Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD de- ===\"; grep -n \"^d[eē]-\" AHD_watkins1985.txt | head -20; echo \"=== AHD dō / de- do ===\"; grep -n \"diadem\" AHD_watkins1985.txt | head"
}
```


### [2026-09-05T17:28:54.882Z] TOOL RESULT

```
diadem leaf 242
[]
238 ['434', '435']
239 ['436', '437']
240 ['438', '439']
241 ['440', '441']
242 []
243 []
244 ['444', '445', '446']
245 ['447', '448']
```


### [2026-09-05T17:28:54.944Z] TOOL RESULT

```
=== AHD de- ===
=== AHD dō / de- do ===
```


## [2026-09-05T17:29:03.730Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in (241,242):\n    ls=[x for x in leaves[i].split('\\n') if x.strip()]\n    print('--leaf',i,'FIRST:',ls[0][:150]); print('   LAST:',ls[-1][:150])\nEOF\necho \"=== AHD sample ===\"; sed -n '1,10p' AHD_watkins1985.txt; echo ...; grep -n \"diadema\" AHD_watkins1985.txt | head; echo \"=== dhē / de ===\"; grep -n \"^de-\" AHD_watkins1985.txt | head"
}
```


### [2026-09-05T17:29:05.711Z] TOOL RESULT

```
--leaf 241 FIRST:  deity.
   LAST: diaconate,  n.,  the  office  of  a  deacon.  —  Eccles. L.  diaconatus,  fr.  Late 
--leaf 242 FIRST:  L.  diaconus.  See  deacon and  subst.  suff.  -ate.
   LAST: Diana,  n.,  the  goddess  of  the  moon  and  of  hunt¬ ing  in  Roman  mythology;  identified  with  the Greek  Artemis.  —  L.,  earlier  Dividna. 
=== AHD sample ===
American Heritage — Dictionary
of
Indo-European Roots
Revised and edited by Calvert Watkins
JUN 01 1985
American Heritage , Dictionary Indo-European Roots
American
Heritage
Dictionary do-European
Root
...
=== dhē / de ===
```


## [2026-09-05T17:29:13.516Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"DIADEM\" AHD_watkins1985.txt | head; echo \"=== de- bind ===\"; grep -n -i \"dē-\\. To bind\\|To bind\" AHD_watkins1985.txt | head -20; echo \"=== search de1 ===\"; grep -n -iE \"^ *d[eē][-–]?[0-9]?\\.\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T17:29:13.590Z] TOOL RESULT

```
360:[dan-. Low ground. Germanic root. Suffixed form *dan- Jam in: a. Old English denn, lair of a wild beast: DEN; b. possibly Old English Dene (genitive plural Dena), the Danes, and Old Norse Danr, Dane: DANE, DANISH; DANELAW. [In Pok. 2. dhen- 249.]] dap-. To apportion (in exchange). Suffixed form *dap-no- in Latin damnum, damage entailing liability (for repara- tion), harm: DAMAGE, DAMN; CONDEMN, DAMNIFY, IN- DEMNIFY, (INDEMNITY). [In Pok. dd- 175.] de-. Demonstrative stem, base of prepositions and ad- verbs. 1. Germanic *t6 in Old English #6, to: TO, TOO. 2. Perhaps Latin dé, dé-, from: DE-. 3. Latin déterior, worse: DETERIORATE. 4, Latin débilis, weak (see bel-). [Pok. de-, do- 181.] dé-. To bind. Contracted from *deo-. Greek dein, to bind: DESMID; ANADEM, ASYNDETON, DIADEM, PLASMODESMA, (SYNDESMOSIS), SYNDETIC. [Pok. dé- 183.] deigh-. Insect. Possibly in Germanic *tik-6, tikk-6 in Middle English teke, tick: TIck?. [Pok. deigh- 187.] deik-. To show, pronounce solemnly; also in derivatives referring to the directing of words or objects. I. Variant *deig-. 1. O-grade form doig- in: a. Germanic *taikjan, to show, in Old English t&can, to show, instruct: TEACH; b. Germanic *taiknam in (i) Old English tacen, tacn, sign, mark: TOKEN (ii) Old English tdcnian, to signify: BETO- KEN (iti) Gothic taikns, sign: TETCHY (iv) Old French tache, teche, mark, stain: TACHISM. 2. Latin digitus, finger (< “pointer,” “indicator”): picitT. II. Basic form *deik-. 1. O-grade form *doik- possibly in Germanic *taihw6 in Old English ta, tahe, toe: TOE. 2. Basic form *deik- in Latin dicere, to say, tell: DICTATE, DICTION, DICTUM, DITTO, DITTY; ADDICT, BENEDICTION, CONDI- TION, CONTRADICT, EDICT, FATIDIC, (INDICT), INDITE, INTERDICT, JURIDICAL, JURISDICTION, MALEDICT, PRE- DICT, VALEDICTION, VERDICT, VERIDICAL. 3. Zero-grade form *dik-d- in Latin dicdre, to proclaim: ABDICATE, DEDICATE, PREACH, PREDICATE. 4. Agential suffix *-dik- in: a. Latin index, indicator, forefinger (in-, toward; see en): INDEX, INDICATE; b. Latin jiidex (< *yewes-dik-), judge, “one who shows or pronounces the law” (jis, law; see yewes-): JUDGE, JUDICIAL; PREJUDICE; Cc. Latin vindex (first element obscure), claimant, avenger: (VEN- DETTA), VINDICATE; (AVENGE), REVENGE. 5. Greek deik- nunai, to show: DEICTIC; APODICTIC, PARADIGM, POLICY?. 6. Zero-grade form *dik- in Greek dikein, to throw (< “to direct an object”): DIsK. 7. Form *dikd in Greek diké, justice, right, court case: DICAST; EURYDICE, SYNDIC, THEODICY. [Pok. deik- 188.] deiw-. To shine (and in many derivatives, “sky, heaven, god”). I. Noun *deiwos, god. 1. Germanic *Tiwaz in: a. Old English Tiw (genitive Tiwes), god of war and sky: Tiu, (TuEspay); b. Old Norse Tyr, sky god: Tyr. 2. Latin deus, god: DEISM, DEITY, JOSS; ADIEU, DEICIDE, DEIFIC. 3. Latin divus, divine, god: DIVA, DIVINE!, (DI- VINE?). 4. Latin dives, rich (< “fortunate, blessed, di- vine”): Dives. 5. Suffixed zero-grade form *diw-yo-, heavenly, in Latin Didna, moon goddess: DIANA. 6. San- skrit devah, god, and deva-, divine: DEVI; DEODAR, DEVANAGARI. II. Variant *dyeu-, Jove, the name of the god of the bright sky, head of the Indo-European pan- theon. 1. Latin Jovis, Jupiter (> Italian Giove): JovE, JOVIAL. 2. Derivative *jou-il- in Latin Jiilius, “descended from Jupiter” (name of a Roman gens): JULY. 3. Voca- tive compound *dyeu-poter- (*pater-, father; see peater-), “O father Jove,” in Latin Juppiter, Jiipiter, head of the Roman pantheon: JuprTerR. 4. Greek Zeus, Zeus: ZEUS; (Dioscuri). III. Variant *dyé- (< *dyea-) in Latin diés, day (> Late Latin diurnum, day): DIAL, DIARY, DIET?, DISMAL, DIURNAL; ADJOURN, CIRCADIAN, (JOURNAL), (JOURNEY), MERIDIAN, QUOTIDIAN, (POSTMERIDIAN), SOJOURN. IV. Variant *deis- in Greek délos (< *deyalos), clear: PSYCHEDELIC. [Pok. 1. dei- 183.] dek-'. To take, accept. 1. Suffixed (stative) form *dek-é- in Latin decére, to be fitting (< “to be acceptable”):
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
=== de- bind ===
330:3. O-grade form *bhol- in Germanic *ball- in: a. Old English beallucas, testicles: BOLLIX; b. Old Norse bdllr, ball: BALL; c. Danish bolle, round roll, akin to the probable Scandinavian source of BILBERRY; d. Middle High German baile (> Italian balla, palla), ball: BAL- LOON, BALLOT; PALL-MALL; e. French baile, ball: BAL- LOTTEMENT; f. Old French baie, rolled-up bundle: BALE!. 4. Suffixed o-grade form *bhol-to- possibly in Germanic *balthaz, bold, in: a. Old English bald, beald, bold: BOLD; b. Old High German bald, bold: BAWD. 5. Suffixed o-grade form *bhol-n- in Latin follis, bellows, inflated ball: FOLLICLE, FOOL!; (FOLLICULITIS). 6. Possibly Greek phalaina, whale: BALEEN. 7. Conceivably (but more likely unrelated) Greek phellos, cork, cork oak: PHEL- LEM; PHELLODERM, PHELLOGEN. (The following deriva- tives of this root are entered separately: bhel-?, bhelgh-, bhlei-, bhleu-.) [Pok. 3. bhel- 120.} bhel-3, To thrive, bloom. Possibly from bhel-?. I. Suffixed o-grade form *bhol-yo-, leaf. 1. Latin folium, leaf: ForL?, FOLIAGE, FOLIO, FOLIUM; CINQUEFOIL, DEFOLIATE, EX- FOLIATE, FEUILLETON, FOLICOLOUS, MILFOIL, PORTFO- LIO, TREFOIL. 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN. II. Extended form *bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m6n- in (i) Old Norse blém, blémi, flower, blossom: BLOOM! (ii) Old English bléma, a hammered ingot of iron (semantic development obscure): BLOOM?; c. Germanic suffixed form *bl6-s- in Old English bléstm, bléstma, flower, blossom: BLOssoM; d. Latin flés (stem flor-), flower: FERRET?, (FLORA), FLORA, (FLORAL), FLOR- IATED, FLORID, FLORIN, FLORIST, -FLOROUS, FLOSCULUS, FLOUR, FLOURISH, FLOWER; CAULIFLOWER, DEFLOWER, EFFLORESCE, ENFLEURAGE, FLORIGEN. 2. Germanic suf- fixed form *blé-do- in Medieval Latin bladium, produce of the land: EMBLEMENTS. 3. Suffixed zero-grade form *bhib-to- in Germanic *bladaz in Old English bled, leaf, blade: BLADE. [Pok. 4. bhel- 122.] bhel-4. To cry out, yell. Germanic *bell- in: a. Old English bellan, to bellow, bark, roar: BELL?; b. Old English belle, a bell: BELL!; c, Old English belgan, bylgan, to become enraged: BELLOW; d. perhaps Old English bealcan, *b(iJelcan, to utter, belch forth: BELCH; e. Middle High German buldern, boldern, to make noise: POLTERGEIST; f. Icelandic baula, to low, akin to the Scandinavian source of Middle English baulen, to howl: BAWL. [Pok. 6. bhel- 123.] bheld-. To knock, strike. Zero-grade form *bhid- in Germanic *bult-, missile, in Old English bolt, heavy arrow, bolt: BouT!. [Pok. bheld- 124.] bhelg-. Also bhelk-. A plank, beam. 1. Germanic *balku- in Old English balc(a), ridge: BALK. 2. Germanic *balk6n- in: a. Old French bauch, beam: DEBAUCH; b. Old Italian balcone, scaffold: BALCONY. 3. Suffixed zero-grade form *bhik-yo- in Latin fulcire, to prop up, support: FULCRUM. 4. Possibly Greek phalanx, beam, finger bone, line of battle: PHALANGE, PHALANX. [Pok. 5. bhel- 123.] bhelgh-. To swell. Extension of bhel-2. 1. Germanic *balgiz in Old English bel(ijg, belig, purse, bellows: BELLOWS, BELLY. 2. Germanic *bulgjan in Old Norse bylgja, a wave: BILLOW. 3. Germanic *bolgstraz in Old English bolster, cushion: BOLSTER. 4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE. [Pok. bhelgh- 125.) bhelu-. To harm. Germanic *balwaz in Old English bealo, b(e)alu, harm, ruin, bale: BALE?. [Pok. bheleu- 125.] bhendh-. To bind. 1. Germanic *bindan in Old English bindan, to bind: BIND; WOODBINE. 2. O-grade form *bhondh- in Germanic *band- in: a. Old English bend, band, ribbon, akin to the Germanic source of Old French bende, band: BEND?; b. Old English bendan, to bend: BEND!; c. Old Norse band, band, fetter: BAND!, BOND; d. Old French bande, bond, tie, link: BAND!. 3. Zero-
360:[dan-. Low ground. Germanic root. Suffixed form *dan- Jam in: a. Old English denn, lair of a wild beast: DEN; b. possibly Old English Dene (genitive plural Dena), the Danes, and Old Norse Danr, Dane: DANE, DANISH; DANELAW. [In Pok. 2. dhen- 249.]] dap-. To apportion (in exchange). Suffixed form *dap-no- in Latin damnum, damage entailing liability (for repara- tion), harm: DAMAGE, DAMN; CONDEMN, DAMNIFY, IN- DEMNIFY, (INDEMNITY). [In Pok. dd- 175.] de-. Demonstrative stem, base of prepositions and ad- verbs. 1. Germanic *t6 in Old English #6, to: TO, TOO. 2. Perhaps Latin dé, dé-, from: DE-. 3. Latin déterior, worse: DETERIORATE. 4, Latin débilis, weak (see bel-). [Pok. de-, do- 181.] dé-. To bind. Contracted from *deo-. Greek dein, to bind: DESMID; ANADEM, ASYNDETON, DIADEM, PLASMODESMA, (SYNDESMOSIS), SYNDETIC. [Pok. dé- 183.] deigh-. Insect. Possibly in Germanic *tik-6, tikk-6 in Middle English teke, tick: TIck?. [Pok. deigh- 187.] deik-. To show, pronounce solemnly; also in derivatives referring to the directing of words or objects. I. Variant *deig-. 1. O-grade form doig- in: a. Germanic *taikjan, to show, in Old English t&can, to show, instruct: TEACH; b. Germanic *taiknam in (i) Old English tacen, tacn, sign, mark: TOKEN (ii) Old English tdcnian, to signify: BETO- KEN (iti) Gothic taikns, sign: TETCHY (iv) Old French tache, teche, mark, stain: TACHISM. 2. Latin digitus, finger (< “pointer,” “indicator”): picitT. II. Basic form *deik-. 1. O-grade form *doik- possibly in Germanic *taihw6 in Old English ta, tahe, toe: TOE. 2. Basic form *deik- in Latin dicere, to say, tell: DICTATE, DICTION, DICTUM, DITTO, DITTY; ADDICT, BENEDICTION, CONDI- TION, CONTRADICT, EDICT, FATIDIC, (INDICT), INDITE, INTERDICT, JURIDICAL, JURISDICTION, MALEDICT, PRE- DICT, VALEDICTION, VERDICT, VERIDICAL. 3. Zero-grade form *dik-d- in Latin dicdre, to proclaim: ABDICATE, DEDICATE, PREACH, PREDICATE. 4. Agential suffix *-dik- in: a. Latin index, indicator, forefinger (in-, toward; see en): INDEX, INDICATE; b. Latin jiidex (< *yewes-dik-), judge, “one who shows or pronounces the law” (jis, law; see yewes-): JUDGE, JUDICIAL; PREJUDICE; Cc. Latin vindex (first element obscure), claimant, avenger: (VEN- DETTA), VINDICATE; (AVENGE), REVENGE. 5. Greek deik- nunai, to show: DEICTIC; APODICTIC, PARADIGM, POLICY?. 6. Zero-grade form *dik- in Greek dikein, to throw (< “to direct an object”): DIsK. 7. Form *dikd in Greek diké, justice, right, court case: DICAST; EURYDICE, SYNDIC, THEODICY. [Pok. deik- 188.] deiw-. To shine (and in many derivatives, “sky, heaven, god”). I. Noun *deiwos, god. 1. Germanic *Tiwaz in: a. Old English Tiw (genitive Tiwes), god of war and sky: Tiu, (TuEspay); b. Old Norse Tyr, sky god: Tyr. 2. Latin deus, god: DEISM, DEITY, JOSS; ADIEU, DEICIDE, DEIFIC. 3. Latin divus, divine, god: DIVA, DIVINE!, (DI- VINE?). 4. Latin dives, rich (< “fortunate, blessed, di- vine”): Dives. 5. Suffixed zero-grade form *diw-yo-, heavenly, in Latin Didna, moon goddess: DIANA. 6. San- skrit devah, god, and deva-, divine: DEVI; DEODAR, DEVANAGARI. II. Variant *dyeu-, Jove, the name of the god of the bright sky, head of the Indo-European pan- theon. 1. Latin Jovis, Jupiter (> Italian Giove): JovE, JOVIAL. 2. Derivative *jou-il- in Latin Jiilius, “descended from Jupiter” (name of a Roman gens): JULY. 3. Voca- tive compound *dyeu-poter- (*pater-, father; see peater-), “O father Jove,” in Latin Juppiter, Jiipiter, head of the Roman pantheon: JuprTerR. 4. Greek Zeus, Zeus: ZEUS; (Dioscuri). III. Variant *dyé- (< *dyea-) in Latin diés, day (> Late Latin diurnum, day): DIAL, DIARY, DIET?, DISMAL, DIURNAL; ADJOURN, CIRCADIAN, (JOURNAL), (JOURNEY), MERIDIAN, QUOTIDIAN, (POSTMERIDIAN), SOJOURN. IV. Variant *deis- in Greek délos (< *deyalos), clear: PSYCHEDELIC. [Pok. 1. dei- 183.] dek-'. To take, accept. 1. Suffixed (stative) form *dek-é- in Latin decére, to be fitting (< “to be acceptable”):
372:deuk-. To lead. 1. Germanic *teuhan in Old English téon (> Middle English tuggen), to pull, draw, lead: TUG; WANTON. 2. Suffixed zero-grade form *duk-d- in Ger- manic *tugdn in Old English togian, to draw, drag: TOW}. 3. Suffixed o-grade form *douk-eyo- in Old English *tiegan, tigan, to bind: TIE. 4. Suffixed o-grade form *douk-mo- in Germanic *tau(h)maz in Old English téam, descendant, family, race, brood: TEAM. 5. Germanic denominative *tau(h)mjan in Old English téman, tieman, to beget: TEEM!. 6. Basic form *deuk- in Latin diicere, to lead: DOCK!, DOGE, DOUCHE, (DUCAL), (DUCAT), (DUCH- ESS), (DUCHY), DUCT, DUCTILE, DUKE; (ABDUCENS), AB- DUCT, ADDUCE, CIRCUMDUCTION, CON3, (CONDOTTIERE), CONDUCE, CONDUCT, DEDUCE, (DEDUCT), EDUCE, (EN- DUE), INDUCE, INTRODUCE, PRODUCE, REDOUBT, RE- DUCE, SEDUCE, SUBDUCTION, SUBDUE, TRADUCE, TRANSDUCER. 7. Suffixed zero-grade form *duk-d- in Latin éducdre, to lead out, bring up (é- < ex-, out; see eghs): EDUCATE. [Pok. deuk- 220.]
671:extensions in: a. Old English slim, slime: sLIME; b. Old English slipor, slippery: SLIPPERY; Cc. Old English *slice, smooth (> Middle English slike, smooth): sLick; d. Old English lim, cement, birdlime: LIME; e. Old English lam, loam: LOAM; f. Old Norse s/éttr, smooth, sleek, akin to the probable Scandinavian source of Middle English slight, slender: SLIGHT; g. Middle Dutch and Middle Low German slippen, to slip, slip away, akin to the probable source of Middle English slippen, to slip: sL1P!; h. Middle Low German slépen, to drag: SCHLEP. 2. Suffixed form *lei-mo- in Latin limus, slime: LIMACINE, LIMICOLINE. 3. Suffixed form */ei-w- in Latin oblivisci (ob-, away; see epi), to forget (< “to wipe, let slip from the mind”): OBLIVION, OUBLIETTE. 4. Extended form *(sjleia- in: a. nasalized zero-grade form */i-n-a- in Latin linere, to anoint: LINIMENT; b. Suffixed zero-grade form *li- (< *lig-) in Greek litos, plain, simple: LiToTEs. [Pok. 3. lei- 662.] léi-. Also lei-. To flow. 1. Extended form “/eib- in Latin libdre, to pour out, taste: LIBATION; PRELIBATION. 2. Possibly suffixed extended form */eit-os- in Latin litus, shore: LITTORAL. [Pok. 4. lei- 664.] leid-. To play, jest. Suffixed o-grade form *loid-o- in Latin lidus, game, play, with its derivative lidere, to play (but both words may possibly be from Etruscan): LUDICROUS; ALLUDE, COLLUDE, DELUDE, ELUDE, ILLU- SION, INTERLUDE, PRELUDE, PROLUSION. [Pok. leid- 666.] leie-. To waste away. Zero-grade form “li- (< *lia-) in Greek limos, hunger, famine: BULIMIA. [In Pok. 2. lei- 661.] leig-'. To bind. 1. Germanic */ik- in Middle Low German lik, leech line: LEECH?. 2. Zero-grade form */ig-d- in Latin ligare, to bind: LEAGUE!, LEGATO, LIABLE, LIEN, LIGASE, LIGATE; ALLOY, (ALLY), COLLIGATE, COLLIGATIVE, FURL, OBLIGE, (RALLY), RELY. [Pok. 4. leig- 668.] leig-?. Poor. Perhaps Greek oligos, few, little: OLIGO-. [Pok. 1. leig- 667.] leig-5. To leap, tremble. O-grade form */oig- in Germanic *laik- in: a. Old English -lac, suffix denoting activity: WEDLOCK; b. Old Norse leika, to play: LARK?. [Pok. 3. leig- 667.] leigh-. To lick. 1. Greek leikhein, to lick: ELECTUARY. 2. Zero-grade form *lig- in Germanic *likk6n in: a. Old English liccian, to lick: Lick; b. Old French lechier, to live in debauchery: LECHER. 3. Nasalized zero-grade form *ling- in Latin lingere, to lick: ANILINGUS, CUNNI- LinGus. [Pok. leigh- 668.] leikw-, To leave. 1. Basic form *leikv- in Greek leipein, to leave: ECLIPSE, ELLIPSIS. 2. O-grade form *loikv- in: a. Germanic */aihwnjan in Old English lénan, to lend, give (< “to leave to”): LEND; b. suffixed form *loikv-nes- in Germanic */aihwniz in Old Norse Jan, loan: LOAN. 3. Zero-grade form *likv- in Germanic *-lif-, left, in: a. Germanic *ain-lif-, “one (beyond ten),” in Old English endleofan, eleven (see oi-no-); b. Germanic *twa-lif-, “two left (beyond ten),” in Old English twelf, twelve (see dwo-). 4. Nasalized zero-grade form *li-n-kv- in Latin linquere, to leave: DELINQUENT, DERELICT, RELINQUISH. [Pok. leike- 669.] leip-. To stick, adhere; fat. 1. Germanic *libam in Old English Jif, life (< “continuance”): LIFE, LIVELY. 2. Ger- manic “libén in Old English lifian, libban, to live: LIVE}. 3. Germanic */aibjan in Old English léfan, to leave, have remaining: LEAVE!. 4. Germanic “libro in Old English lifer, liver (formerly believed to be the blood-producing organ): LIVER}. 5. Zero-grade form *lip- in Greek lipos, fat: L1po-. 6. Variant form *aleibh- in Greek aleiphein, to anoint with oil (> aleiphar, unguent): ALIPHATIC; SYNA- LEPHA. [Pok. eip- 670.] leis-'. Track, furrow. 1. O-grade form *lois- in: a. Ger- manic */aist- in Old English Jast, lést, sole, footprint: Last’; b. Germanic */laistjan, “to follow a track,” in Old English /éstan, to continue: LAST?; c. suffixed form *lois-G in Germanic */aiz6 in Old English Jar, learning:
776:sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contracted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old English wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixed form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
895:ryfe, abundant: RIFE. 3. Suffixed form *reip-d- in Latin ripa, bank (< “that which is cut out by a river”): RIPARIAN, RIVAGE, RIVER; ARRIVE. IV. Extended form *reib- in Germanic *rip-. 1. Germanic *ripja- in Old English ripe, ripe, ready for reaping: RIPE. 2. Germanic *ripan in Old English ripan, to reap: REAP. 3. Middle Low German repelen, to remove seeds, akin to the source of Middle English ripelen, to remove seeds: RIPPLE? [Pok. 1. rei- 857.] rei-2. Striped in various colors, flecked. Suffixed o-grade form *roi-ko- in Germanic *raihaz in Old English rd, raha, deer: ROE*. [Pok. 2. rei- 859.] rei-3, To flow, run. 1. Suffixed zero-grade form *7i-nu- in: a. Germanic *ri-nw-an, whence *rinnan, to run, in Old English rinnan, to run, and Old Norse rinna, to run: RUN, RUNNEL; b. secondary Germanic derivative *runiz in Old English ryne, a running: EMBER DAY. 2. Suffixed zero-grade form *ri-l- in Germanic *ril- in Dutch ril and Low German rille, running stream: RILL. 3. Suffixed form *rei-wo- in Latin rivus, stream: RIVAL, RIVULET; DERIVE. [Pok. 3. er- 326.] reidh-. To ride. I. Basic form *reidh-. 1. Germanic *ridan in: a. Old English ridan, to ride: RIDE; b. Middle Dutch riden, to ride (> ridder, rider, knight): RITTER. 2. Celtic *vo-réd- in Latin verédus, post horse (*vo-, under; see upo): PALFREY. II. O-grade form *roidh-. 1. Germanic *raid- in: a. Old English rdd, a riding, road: RAID, ROAD; b. possibly Middle High German reidel, rod between upright stakes (< “wooden horse”): RADDLE!. 2. Prob- ably Germanic *raid-ja- in Old English réde, geréde, ready (< “prepared for a journey’): READY. 3. Germanic *raidjan in Vulgar Latin *arrédare, to arrange: ARRAY. [Pok. reidh- 861.] reig-'. To bind. 1. Germanic *rigg- (the -gg- is anoma- lous) in Norwegian rigga, to bind, akin to the Scandina- vian source of Middle English riggen, to rig: RIG. 2. Zero-grade form *rig- in Latin corrigia (probably borrowed from Gaulish), thong, shoelace (cor-, from com-, together; see kom): SCOURGE. [Pok. reig- 861.] reig-2. To reach, stretch out. 1. O-grade form “roig- in Germanic *raikjan in Old English récan, to stretch out, reach: REACH. 2. Possibly suffixed (stative) zero-grade form “rig-é- in Latin rigére, to be stiff (? < “be stretched out”): RIGID, RIGOR. [Pok. (reig-) 862.] rendh-. To tear up. 1. Germanic *randjan in Old English rendan, to tear: REND. 2. Germanic *rind- in Old English rinde), rind (< “thing torn off”): RIND. [Pok. rendh- 865.] rep-. To snatch. Suffixed zero-grade form *rap-yo- in Latin rapere, to seize: RAPACIOUS, RAPE!, RAPID, RAPT, RAVEN?, RAVIN, RAVISH; EREPSIN, SURREPTITIOUS. [Pok. rep- 865.] rép-'. To creep, slink. Latin répere, to creep: REPENT?, REPTILE; SUBREPTION. [Pok. 1. rép- 865.] rép-2, Stake, beam. Suffixed variant form *rap-tro- in Germanic *raf-tra- in: a. Old English refter, rafter: RAFTER; b. Old Norse raptr, beam: RAFT!. [Pok. 2. rép- 866.] ret-. To run, roll. 1. Prefixed form *to-vo-ret-, “a running up to” (to-, to; vo, under, up, up from under; see upo), in Old Irish toir, pursuit: Tory. 2. Suffixed o-grade form *rot-d- in Latin rota, wheel: RODEO, ROLL, ROTA, RO- TARY, ROTATE, ROTUND, (ROTUNDA), ROULETTE, ROUND!, ROWEL; BAROUCHE, CONTROL, PRUNE?, ROTIFORM, ROTO- GRAVURE. [Pok. ret(h)- 866.] rét-. Post. O-grade form *rdt- in Germanic *réd- in Old English réd, rod, cross: ROOD. [Pok. rét+ 866.] reu-'. To bellow. 1. Extended form *reud- in Germanic *rauton in Old Norse rauta, to roar (akin to the Scandi- navian source of ROTE?): ROUT’. 2. Suffixed extended form *reum-os- in Latin riimor, rumor, “common talk”: RUMOR. 3. Extended form *reug- in Latin rigire, to roar: RIOT, RUT’. 4. Variant *rau-ko- in Latin raucus, hoarse: RAUCOUS. [Pok. 1. reu- 867.]
909:sé-4, To bind, tie. Contracted from *sea-. Variant *sesi-, zero-grade form *si-. Suffixed form *si-nw- in Germanic *sinwo- in Old English sinu, seonu, tendon: SINEW. [Pok. 3. sé(i)- 891.]
981:ably from the splitting of its husk at threshing), akin to the Germanic source of Late Latin spelta, spelt: SPELT!. 2. Extended form ‘*spelt- in Germanic *spilthjan in Old English spillan, to spill, destroy: sPILLt. 3. Suffixed o-grade form *spol-yo- perhaps in Latin spolium, hide torn from an animal, armor stripped from an enemy, booty: SPOIL; DESPOIL. [Pok. 1. (s)p(h)el- 985.] spel-2. To shine, glow. Extended form *splend- in Latin splendére, to shine: SPLENDID; RESPLENDENT. [Pok. 2. (s)p(h)el- 987.] spel-3. To say aloud, recite. Suffixed form *spel-no-. 1. Germanic *spellam in: a. Old English spell, discourse, story: SPELL?; b. Old English spel, news: GOSPEL. 2. Ger- manic denominative *spellén in Old French espeller, espelir, to read out: SPELL!. [Pok. (s)pel- 985.] spelgh-. Spleen, milt. 1. Deformation *(pjlihén in Latin lién, milt, spleen: LIENAL. 2. Uncertain preform in: a. Greek splén, spleen: SPLEEN; b. Greek splankhna, inward parts: SPLANCHNIC. [Pok. sp(h)elgh(en) 987.] (s)pen-. To draw, stretch, spin. I. Basic form *spen-. 1. Suffixed form *spen-wo- in Germanic *spinnan, to spin, in: a. Old English spinnan, to spin, with derivative *spin-thron-, “the spinner,” contracted to spithra, spi- der: SPIN, SPIDER; b. Germanic derivative *spin-ilén in Old English spinel, spindle: SPINDLE. 2. Extended form *pend- in Latin pendére, to hang (intransitive), and pendere, to cause to hang, weigh, with its frequentative pensdre, to weigh: PAINTER2, (PANSY), PENCHANT, PEN- DANT, PENDENTIVE, PENDULOUS, PENSILE, PENSION}, PENSIVE, PESO, POISE!; ANTEPENDIUM, APPEND, (APPEN- DIX), COMPENDIUM, COMPENSATE, DEPEND, DISPENSE, EXPEND, IMPEND, PENTHOUSE, PERPEND, PERPENDICU- LAR, PREPENSE, PROPEND, SUSPEND, VILIPEND. 3. Per- haps suffixed form *pen-ya- in Greek penia, lack, poverty (< “a strain, exhaustion”): -PENIA. II. O-grade forms *spon-, *pon-. 1. Germanic “spannan in: a. Middle Dutch spannen, to bind: SPAN; b. Old High German spannan (> German spannen), to stretch: SPANNER. 2. Germanic *spanno- in Old English span(n), distance: SPAN], 3. Perhaps Germanic *spangé in Middle Dutch spange, clasp: SPANGLE. 4. Suffixed and extended form *pond-o- in Latin pondé, by weight: PoUND!. 5. Suffixed and extended form *pond-es- in Latin pondus (stem ponder-), weight, and its denominative ponderdre, to weigh: PONDER, PONDEROUS; EQUIPONDERATE, PREPON- DERATE. 6. Perhaps suffixed form *spon-t- in Latin sponte, of one’s own accord, spontaneously: SPONTANE- ous. 7. Greek penesthai, to toil, with o-grade derivatives ponos, toil, and ponein, to toil: GEOPoNic. [Pok. (s)pen-(d)- 988.] spend-. To make an offering, perform a rite, hence to engage oneself by a ritual act. O-grade form *spond-. 1. Suffixed form *spond-eyo- in Latin spondére, to make a solemn promise, pledge, betroth: SPONSOR, SPOUSE; DESPOND, ESPOUSE, RESPOND. 2. Suffixed form *spond-a in Greek spondé, libation, offering: SPONDEE. [Pok. spend- 989.]} sper-'. Spear, pole. 1. Germanic *speru- in: a. Old Eng- lish spere, spear: SPEAR; b. Middle Low German spér, spit: SPARERIBS. 2. Germanic *sparjén- in Old Norse sperra, rafter, beam: SPAR}. [Pok. 1. (s)per- 990.] sper-2. To turn, twist. 1. Suffixed form *sper-ya- in Greek speira, a winding, coil, spire: SPIRE?. 2. Suffixed zero-grade form *spr-to- in Greek sparton, rope, cable: ESPARTO. [Pok. 3. sper- 991.] . sper-3. Bird’s name, sparrow. Suffixed o-grade form *spor-wo- in Germanic *sparwan- in Old English spearwa, spearwe, sparrow: SPARROW. [Pok. sper-(g)- 997.] sper-4. To strew. I. Zero-grade form *spr-. 1. Germanic *spr- in Old English spréawlian, to sprawl: SPRAWL. 2. Extended form *spreut- in Germanic *sprit- in: a. Old English spriitan, to sprout: SPROUT; b. Old English spryttan, to sprout, come forth: sPpuRT; c. Old English
1059:syi-. To bind, sew. I. Basic form *syi- in Germanic
=== search de1 ===
```


## [2026-09-05T17:29:34.156Z] TOOL CALL #19: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 110 -l 110 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg110 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-05T17:29:35.033Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==118' HRN.txt | head -60"
}
```


### [2026-09-05T17:29:36.404Z] TOOL RESULT

```
total 33096
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 13:29 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5971 Sep  5 02:13 baga.html
-rw-rw-r-- 1 sfmqrb sfmqrb   189420 Sep  5 02:15 bqt440_bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   513902 Sep  5 02:15 bqt440.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   502834 Sep  5 02:02 bqt538_big.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    72705 Sep  5 02:02 bqt538_fn6.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24595 Sep  5 02:02 bqt538_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22593 Sep  5 02:02 bqt538_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   207980 Sep  5 02:01 bqt538.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5214 Sep  5 02:23 build82a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    53401 Sep  5 02:29 build82b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    19831 Sep  5 02:31 build82c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48417 Sep  5 10:19 build93.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59425 Sep  5 10:54 build98.py
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2950 Sep  5 10:15 c_anth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2661 Sep  5 10:15 c_armonica.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9603 Sep  5 10:50 c_byz2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11328 Sep  5 10:49 c_byz_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3138 Sep  5 10:50 c_heb1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4953 Sep  5 10:50 c_heb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb      914 Sep  5 11:04 chicane.html
-rw-rw-r-- 1 sfmqrb sfmqrb     4845 Sep  5 10:50 c_root3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1795 Sep  5 10:50 c_scyth2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2953 Sep  5 10:50 c_scyth3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4885 Sep  5 10:49 c_scyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3019 Sep  5 10:15 c_sus.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33345 Sep  5 10:55 e0.102.json
-rw-rw-r-- 1 sfmqrb sfmqrb    38686 Sep  5 10:34 e0.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    26175 Sep  5 10:38 e1.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb      456 Sep  5 10:56 g.py
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    49033 Sep  5 10:53 mk100.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17464 Sep  5 10:55 mk102b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25511 Sep  5 10:58 mk102c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    21655 Sep  5 10:53 mk102.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62559 Sep  5 11:04 mk103.py
-rw-rw-r-- 1 sfmqrb sfmqrb    31652 Sep  5 13:24 mk105.py
-rw-rw-r-- 1 sfmqrb sfmqrb    40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb    78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79383 Sep  5 02:19 mk78.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52793 Sep  5 02:18 mk79.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57729 Sep  5 02:31 mk81.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58379 Sep  5 02:39 mk83.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76819 Sep  5 02:39 mk84.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25181 Sep  5 02:44 mk86.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67712 Sep  5 10:03 mk87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66054 Sep  5 10:10 mk89.py
-rw-rw-r-- 1 sfmqrb sfmqrb    70790 Sep  5 10:04 mk90.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48553 Sep  5 10:03 mk91.py
-rw-rw-r-- 1 sfmqrb sfmqrb    27206 Sep  5 10:38 mk95b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    39501 Sep  5 10:34 mk95.py
-rw-rw-r-- 1 sfmqrb sfmqrb    49433 Sep  5 10:35 mk96.py
-rw-rw-r-- 1 sfmqrb sfmqrb    54149 Sep  5 10:47 mk97.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61159 Sep  5 10:50 mk99.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
-rw-rw-r-- 1 sfmqrb sfmqrb    32690 Sep  5 13:24 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71589 Sep  5 10:41 pg100.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68145 Sep  5 10:44 pg102.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114170 Sep  5 10:49 pg103_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79623 Sep  5 10:49 pg103.png
-rw-rw-r-- 1 sfmqrb sfmqrb   169766 Sep  5 10:57 pg104_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22122 Sep  5 10:58 pg104_charlatan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78826 Sep  5 10:57 pg104.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31584 Sep  5 11:00 pg104_tea.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82500 Sep  5 10:57 pg105.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55270 Sep  5 11:01 pg106.png
-rw-rw-r-- 1 sfmqrb sfmqrb    48976 Sep  5 11:01 pg107.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68501 Sep  5 13:26 pg108.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67502 Sep  5 13:29 pg110.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb   155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63822 Sep  5 01:59 pg78.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59439 Sep  5 02:09 pg79.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58953 Sep  5 02:08 pg80.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99904 Sep  5 02:15 pg81.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29321 Sep  5 02:20 pg82_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74477 Sep  5 02:20 pg82.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56108 Sep  5 02:20 pg82_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   154129 Sep  5 02:25 pg83_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7123 Sep  5 02:26 pg83_apac.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4363 Sep  5 02:26 pg83_bohyah.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67094 Sep  5 02:25 pg83.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82358 Sep  5 02:23 pg84.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63329 Sep  5 02:25 pg85.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31530 Sep  5 02:35 pg86.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79874 Sep  5 09:47 pg87.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134852 Sep  5 09:54 pg88_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11747 Sep  5 09:54 pg88_e0spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31391 Sep  5 09:55 pg88_join.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98452 Sep  5 09:54 pg88.png
-rw-rw-r-- 1 sfmqrb sfmqrb    26700 Sep  5 09:54 pg88_spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb   171528 Sep  5 02:45 pg89_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4628 Sep  5 02:45 pg89_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4924 Sep  5 02:45 pg89_berijan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80984 Sep  5 09:49 pg89.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77182 Sep  5 09:48 pg90.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63799 Sep  5 09:55 pg91.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157177 Sep  5 10:09 pg92_500.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8494 Sep  5 10:09 pg92_avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3476 Sep  5 10:09 pg92_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90918 Sep  5 10:07 pg92.png
-rw-rw-r-- 1 sfmqrb sfmqrb    93420 Sep  5 10:15 pg94.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44047 Sep  5 10:16 pg94_sogd.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49714 Sep  5 10:16 pg94_urvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78178 Sep  5 10:11 pg95.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163439 Sep  5 10:15 pg96_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72929 Sep  5 10:15 pg96.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101597 Sep  5 10:41 pg99_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8738 Sep  5 10:41 pg99_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65608 Sep  5 10:40 pg99.png
```


### [2026-09-05T17:29:37.887Z] TOOL RESULT

```
— 96 —
428. jev (AM.), jo *6erste*, jevm.
Käs. ye, ya,
SiW.yava- *6etreide'; phlv. jav bezw. yav; ai. yäva-.
knrd, je, jau, yö (H.-Sch.); oss. yau, yäu, yeu *Hirse'
(147); bei. /ö, jav, n. jau 'Gei-ste' (179); si/n. yavoj,
sar. yaugjy yögj, 'MehY (aus ^yavaka^).
429. Jevän, juvän 'Jüngling .
niäz. javän.
aw. ytivan- {yvan-) 'Jüngling; phlv. yuvän (päz.
falsch jüdän)^), arm. LW. yavanak, yovanak 'Junges
eines Vierfüsslers'; ai. yüvan-,
LW. kurd. juvän; afy. javän; bei. javan (111).
430. jösTden *koehen, sieden, jös{pere), jösäk, jösänldtn,
Ka§. vöyösnaä, böyösad (Qohrüd).
ai. yüs-, yüsdn- 'Brühe*.
LW.(?) kurd, jüSverdin, jüsdnin; hei, jösenag 'kochen,
sieden; aufbrausen, zürnen' (181).
431. jöf, jö *Kanar.
ap. yauviyä'^); phlv. jöi bezw. yöl; ai. yavyd'.
LW. kurd. /i?; Sity,jova; bei. /ö * Wasserlauf, Kanal*
(117).
jehan, jihän 'Welt* s. gehän (No. 951).
C.
432. {\)cäre 'Hilfsmittel, Ausweg*.
aw. darana- in ätare^carana-, sraosö^öay^ana-; phlv.
carak; ai. ödrana- 'das Vollführen, Thätigkeit*.
arm. LW. öar 'Heilmittel*.
Geldner, Studien I, 50, will auch np. cär 'Ofen* von
ütare.^öarana- ableiten.
{2)cäre 'Spinnrad* siehe s. v. cerx (No. 437).
*) V und a sind, wie auch sonst bisweilen, verbunden.
2) Bartholomae, Bß. 13, 70.
```


## [2026-09-05T17:29:46.031Z] TOOL CALL #21: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(d['HRN']['lookup_hint']);print();print(d['HRN'].get('notes',''))\"\necho \"=== grep kai/key in HRN ===\"; cd data/verification/sources/refs && grep -n \"'wann'\\|wann\\b\" HRN.txt | head -20"
}
```


### [2026-09-05T17:29:47.606Z] TOOL RESULT

```
Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.

OCR of German Fraktur-free text is decent; Persian script is not OCRed.
=== grep kai/key in HRN ===
7643:878. {\)kei 'wann? wie?', jüd.-pers. '»>!!.
7644:aw. kada *wann'; ai. kadd *wann?\
7646:wann?' (182).
```


## [2026-09-05T17:29:51.384Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(d):\n    if '878. ' in p:\n        print('leaf',i,'-> printed page',i-21)\n        print(p[:1500])\nEOF"
}
```


### [2026-09-05T17:29:53.258Z] TOOL RESULT

```
leaf 217 -> printed page 196
— 196 -
'wer?' siyn. käi^ sar. ka *was für ein?' wa;^. kü, ki, sar.
ko *dass .
Np. ki setzt ein ap. ^kaya- voraus, vergl. ai. kaya-,
877. (2)kih ^klein; kihm (Sahn. I, 70 Vers 171).
g. kasük, kastar (Comp.); Käs. V. kessär, kesserUr,
K. Z. ias.
aw. kasyäo ^kleiner ; phlv. kih(i)st, kas,
2&y, kasr 'kleiner, jünger ; oss. Msfär (156) jünger,
jüngst'; bei. kasän, kassän 'klein, gering, wenig' (439;
Dames: kisän, kisäin, kisänak).
Zu np. kih vergl. unter bih (No. 241); phlv. kas,
g. kasük etc. stammen vom Positiv aw. kasu- 'klein,
gering.
878. {\)kei 'wann? wie?', jüd.-pers. '»>!!.
aw. kada *wann'; ai. kadd *wann?\
afy. kala ; oss. d. t. ßäd wenn, ob* (158) ; bei. kad'i
wann?' (182).
879. (2)kei 'Herrscher (wie /iisrev 'Herrscher ursprünglich
N. pr.).
aw. kavi-; phlv. ke, vergl. Kerat (Gemme, Hörn,
ZDMG. 44, 675 No. 139); ai. kavi- weise.
Dazu got. us'skava 'vorsichtig, nüchtern*, ahd. scou-
wön 'schauen', Brugmann, Grundriss I, § 528.
880. kes 'Religion .
Siw. tka^Sa- 'Bekenntniss, Gelöbniss (so — nicht
mehr als 'ketzerisches Bekenntniss, Irrglaube' aus
*atika^sa'j wie KZ. 28, 2 — fasst auch Bartholomae
jetzt nach brieflicher Mitteilung das Wort auf ') ; phlv.
kes, vergl. pö^yötkes (nur umschreibend), arm. LW. ßes.
881. ktn 'Feindschaft, Hass, Zorn', Mne.
aw. ka^nä' 'Strafe, Rache'; phlv. ken (paz. ;^fM),
kemtan, arm. LW. ken, jünger Mnavor,
kurd. LW. km; bei. kenay 'Feindschaft, Hass,
Rache (201).
*) f hat keinen etymologischen Wert wie in mehreren anderen
Wörtern, vergl. Indog
```


## [2026-09-05T17:30:05.911Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(d))\nfor i in range(270,280):\n    txt=d[i]\n    print('--- leaf',i,'approx p',i+543)\n    print(txt[:300].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-05T17:30:07.645Z] TOOL RESULT

```
leaves 684
--- leaf 270 approx p 813
   ‫وت‬                                                                                                         ‫دارا‬ | ‫داادرار کردن" » با دال ابجد ‪,‬‬                                 ‫است در هندوستان ‪ -‬و داامروبی که آنرا‬ | ‫کنابه ازدیر باسدن وشات داشتن‪ -‬ومدارا کردن‪-‬‬                    ‫‪ -‬و
--- leaf 271 approx p 814
 ‫دار شش‌دو‬                                                                                      ‫سس‬   ‫‪۱۱‬‬ |  |  | ‫دارخال = با خای نقطه دار بر وزن‬                       ‫دار با‪ » ۱‬بابای ابجد بالف کشیده ‪۲‬‬ | ‫پارسال ‪ ,‬درختی که آنرا پوند نکرده باشند ‪-‬‬                       ‫مابحتاج وضروری ودرب
--- leaf 272 approx p 815
                                                                                 ‫داز شمان‬ |  |  |  |  |                         ‫‪-‬‬     ‫دار کوب‬             ‫دارشعان ‪ = ۱‬باشن‌شطهدار وعین‬ |                        ‫بز وزن خاکروب ‪,‬‬            ‫بی‌نقطه بورزن آبریز گان » درختی باشد سطبر‬ |                  
--- leaf 273 approx p 816
 ‫دای‬                                                                                              ‫سور‬ | ‫چوب بندند کتباوتران ودمگر پرندکان برآن‬                 ‫دار و برد بادال ابجد درآخربروزن‬ |             ‫‪.‬‬      ‫بنشینند ‪ -‬وترجمة لفظ هم‌هست‬       ‫ساز وبرگك » بمعنی طاق وترتب گویرودارو کر‬
--- leaf 274 approx p 817
      ‫ا‪6‬س‬ |  |                ‫داستخاله است که مذ کور شد ‪.‬‬              ‫است مانند دای ودسته دزازی هم دارد و حرية "‬ |                                                          ‫و استخوان ماهی را لیز‬           ‫‪۱‬‬       ‫مردم کیلان ات‬ | ‫دستحاله ‪ = ۷‬بخاای نقطه‌دار بروزن‬ |                         
--- leaf 275 approx p 818
 ‫داغ سو‬                                                                                                            ‫س‬ |                                                                                                                    ‫ری ‪۱‬‬ |                                                        
--- leaf 276 approx p 819
 ‫”‪“AI‬‬                                                                                                          ‫داغ شدن‬ |  | ‫دالیز و‪٩‬‏ تست س بای اد و فتح زای‬                                       ‫داع شدن ‪ -‬بنایتآزرده شدن باشد‪.‬‬ | ‫هوز‪ ,‬مرغی است کوچك وجهنده که عرب صموه‬                     
--- leaf 277 approx p 820
 ‫دامن بدندا نکرفتن‬                                                                           ‫‪ ۷۱‬رس‬ |  |                                         ‫گفته‌اند ‪. ۴‬‬     ‫دام = بروزن رام» نقیض ددباشد که‌آن‬ |                                                          ‫وحشی غیر درنده است عموماً و آهوو غزال 
--- leaf 278 approx p 821
  ‫بح‬        ‫یز‬ |  |  ‫سله وسبدی باشد بز رکه که دوچوب بدروطرف‬                        ‫دامن بارفشاندن ک»نابه از سفر‬ |     ‫ومد لد وبدان سر کنو وامثار آن کشند ‪.‬‬ |                                          ‫ن‬               ‫آ‬     ‫کردن و کرچ لمودن ‪ -‬وترك دادن ‪ -‬و اعراض‬ |  ‫داموع = بروزن آروغ » فربا
--- leaf 279 approx p 822
 ‫داشور‬ |  | ‫دا نژه گ بازای فارسی» بروزن وهعتی‬                           ‫و واو وضم رای قرشت (‪ )۱‬و سکون جيم اول‬ |                  ‫دالجه است که عدی اند ‪.#‬‬                    ‫وبای ابجد (‪ )۲‬وجیم آخرء حبی است که آنرا‬ |  | ‫داش ® ‪ -‬بروزن بال » بىمنىعلم‬                                ‫که از‬
```


## [2026-09-05T17:30:16.574Z] TOOL CALL #24: Bash

```json
{
 "command": "sed -n '1,50p' tools/ref_page.py"
}
```


### [2026-09-05T17:30:16.613Z] TOOL RESULT

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
```


## [2026-09-05T17:30:19.180Z] TOOL CALL #25: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\""
}
```


### [2026-09-05T17:30:21.381Z] TOOL RESULT

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
```


## [2026-09-05T17:30:27.666Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(d):\n    if 'دیهیم' in p or 'دبهیم' in p:\n        print('leaf',i,'approx p',i+543)\nEOF"
}
```


## [2026-09-05T17:30:28.546Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(d[277][:3000])\nEOF"
}
```


### [2026-09-05T17:30:29.406Z] TOOL RESULT

```
leaf 282 approx p 825
leaf 381 approx p 924
leaf 463 approx p 1006
```


### [2026-09-05T17:30:31.197Z] TOOL RESULT

```
 ‫دامن بدندا نکرفتن‬                                                                           ‫‪ ۷۱‬رس‬

                                        ‫گفته‌اند ‪. ۴‬‬     ‫دام = بروزن رام» نقیض ددباشد که‌آن‬
                                                         ‫وحشی غیر درنده است عموماً و آهوو غزال و‬
                                                         ‫لیر را(‪)۱‬گویند خصوصا ‪ - ۱‬وحشرات‌الارش‬
                                                         ‫وپرنده را هم میگوبند ‪ -‬و هرچیز که جانوران‬
‫دامگاه ستول = بمعنی دامگاه دیو‬
                                                         ‫در آن بفریب گرفتار شوند ‪ - ۴‬و نزد محققین‬
                     ‫است که عالم سفلی است ‪.‬‬
 ‫‪e‬‏ تیدام اور‬         ‫گرگ‬            ‫دامگاه‬                                             ‫بمعنی زخارف‬

        ‫است کهجهان فانی وعالم سفلی باشد ‪.‬‬                                              ‫دلیوی و آنچه‬
‫دام آشتن > کابه از بازی دادن ودام‬                                                   ‫باعثبازماندکیاز‬
                                                            ‫مبداء باشد‪ . # .‬نوعی‌دام (تور) ماهیگیری‬
          ‫‪ -‬وخلاصی از دام باشد ‪9 .‬‬           ‫سردن‬

‫دامن باغی گرفتن‪ -‬کنابهازخلوت‬
                                                         ‫دامفول‪ -‬با غين نقطه‌دار وواوه‌جهول‬
                ‫زیدن گووشه نشینی باشد ‪.‬‬                  ‫بروزن زاغنول‪ ,‬دانهاو گرهها باشد مانند گردکان‬
‫دامن بد ندان گردن = کنایه از‬                             ‫که ازاعنا کولوی مردم برمیآید ودردنمبکند‬
‫نمودن باشد د و کنایه از‬        ‫فروتنی کردن و عجز‬         ‫نورآاسلعه میکوبند‪ -‬وغول‌بیابانی رائیز گفته‌اند‬
                  ‫گرشختن هما مدهاست (‪. )۲‬‬                                         ‫واونوعی ازجن است ‪.‬‬
‫دامن بنددان گر تز بمعنی‌دامن‬                             ‫داهلث » بفتحثالث بر وزن کالك '‬
‫بدندان کردن است کنهابه از عجز و فروتنی‬                   ‫جانوران وحتی کوچك راگویند همچوخ رگوش‬
                                    ‫وگربختن باشد ‪.‬‬      ‫ورویاه وامثالآن ‪ -‬و مقنمه وسرانداز زنانرا هم‬

                                ‫‪.‬‬    ‫(‪ )۲‬چك‪ .‬چش ‪ :‬هم هت‬               ‫(‪ )۱‬چك ‪ :‬نخحیر را ‪.‬‬

  ‫» رام شدن) » بونانی ‪( 5618002‬کاو نر) ‪.‬‬               ‫رمدن‬
                                                          ‫‪ - ۱‬حندی باستان ‪( 0۳31 -‬کرا‬
   ‫)؛ در پپلوی ‪0۳84‬‬           ‫رمدن‬
                                 ‫لانبنی ‪ ( 6720۳10‬کاو نر‪ .‬ورزاو ) فس ‪ :‬استی ‪( 000۳0‬کرا‬
                     ‫(مخلوق) (اوستا ‪« )020180-‬اسشق ‪ ۰۳۵‬و ص ‪۲۷۲٩‬‏ ورك ‪ :‬مناس ‪. ۰۷۲:۲‬‬
  ‫‪ - ۴‬هندی باستان‪( 02008 -‬بند‪ .‬ریمان ‪ ,‬زنجیر) » افقانی ‪ , 0101‬ارمنی ع (‪)8‬‬
  ‫‪( 602‬تور) «امذق‪ .۱۳۰‬پهلوی ‪« 018‬مناس ‪۱۷۲‬؛ نیز تورماهیگیری ‪« :‬ماهی از دام جدا‬
  ‫شد ‪,‬روباه پیشتررفت وماهی خوردن گرفت» «سندبادنامه‪ .‬ظهیری‪ .‬طبع احمدآش ص ‪ ۸4‬طبری‬
               ‫رك ‪ :‬دامنی ‪.‬‬          ‫‪ ۰‬مازندرانی کنونی ‪ « 20062‬واژه نامه ‪. ۲۱4۰‬‬
                                       ‫‪۴‬‬
```


## [2026-09-05T17:30:53.009Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(d[381][:3500])\nEOF"
}
```


### [2026-09-05T17:30:54.952Z] TOOL RESULT

```
  ‫دهیم‬                                                                                            ‫‪۲۱‬‬
                ‫هت که بعربی سنای گوبند ‪.‬‬                  ‫دیو کلو چ ‪ = ۱‬بضم کاف ولام بواو‬
 ‫دو مشنگ‪ -‬بفتح میم وشین‌قطه‌دار‬
                              ‫ډ‬                            ‫کشیده وبجیم فارسی زده» طفل مصروع و کودگ‬
 ‫وسکون نون وکاف فارسی» بمعنی کاومشنگه(‪)۱‬‬                                          ‫نفته راگویند ‪.‬‬
                                                                                               ‫گر‬‫ج‬
 ‫است » وآن نوعی ازحبوب باشد که چون پوست‬                   ‫ديو کلوخ ‪ ۴‬کدلوخهای بزرکهرا‬
                ‫آلرا بکنند بعدس مقشر ماند ‪.‬‬                ‫گویند که در وقت شیار کردن از زمین بر خیزد‬
‫ديو فك ‪ -‬بر وزن ربوند ‪ ,‬هام داروبی‬                                                         ‫وبر اطراف ریزد‪.‬‬
                                     ‫است دوایي ‪.‬‬           ‫دگینودم" د بر وزن دیو مردم »‬
                                                           ‫نوعی از گندم است که هر دو دانه دريك علاف‬
‫وزن موه ‪ ۰‬کرم پبلة‬         ‫‪-‬ر‬
                            ‫دوه * ب‬
                                  ‫ب‬
                                 ‫گاوشد ‪.‬‬
                                       ‫ابرشم ر‬             ‫ند ‪.‬‬
                                                              ‫ونهیرا‬
                                                                   ‫گ‌دا‬
                                                                      ‫میباشد ؛ وبعضی خوش بزر که بی‬
 ‫‪-‬نابه ازاقالیم سبعه‬
                   ‫دیو هفت در ک‬                           ‫دلو گیر ‪ -‬باانی مجهول بروزن شیر‬
                                                           ‫کیره کسی را گوبند که او را گجرنفته باشد ‪-‬‬
 ‫درو هفت سر کنابه از شب است‬                                ‫‌یکه دبورا بگیرد ‪ -‬و نام شهری است در‬
                                                                                              ‫پکا‬
                                                           ‫ملك دکن " و درین زمان بدولت آباد شهرت‬

‫هم میشود ‪ -‬کور زمین را فگیفزته اند باعتبار‬                                                               ‫دارد ‪.‬‬
                       ‫هفت اقلیم وهفت طبقه ‪3.‬‬            ‫‪-‬رعی از قماش باشدکه‬
                                                                           ‫دیو گیری ن‬
                                                                 ‫در دب وگر میبافند که آن دوك آباد امت‬
 ‫دھو ل ‪ -‬بارال بثانی مجپول رسیده‬
                               ‫ی‬
‫وهای بواو کشده وبلام زده ‪ ۰‬بمعدی آخرداهول‬                  ‫دیو لاخ ‪ » ۴‬بالام بالفکشیده وبخای‬
                                                          ‫نقطه دار زده » جا ومقام دیو راگویند چه لاخ‬
‫ديهيم ‪- ۱‬بکس هابزوزن تعظیم »‬                              ‫بمعنی مان است همچو سنگه لاخ و رود لاخ‬
                       ‫هخصوص بادشاهان‬
                                    ‫اجى ک م‬                ‫وکلمةٌ لاخ بغیرازین سه موضم جای دبگرنيامده‬
                          ‫تخت‬     ‫ممعنی‬   ‫و‬   ‫‪77‬‬   ‫است‬
                                                          ‫و صبحرا وخارستالی‌را نگدوزبند که از‬             ‫است؟ ‏‬
                        ‫از‬                                 ‫آبادانی دور باشد ‪ -‬وجایگاه خراب و خرابه ‏‬
                                                          ‫وچراگاه دور را نیز گفته‌الد ‪ -‬وسردسیر را هم‬
         ‫دهم‬           ‫وبعضی کوبند دبهیم افسری‬
‫تیمن وتبر ك بربالای‬    ‫بوده که آ را درقد‪.‬یم سهت‬
```


## [2026-09-05T17:31:00.656Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(d[381][3500:7000])\nprint('=========NEXT LEAF 382=========')\nprint(d[382][:2500])\nEOF"
}
```


### [2026-09-05T17:31:02.346Z] TOOL RESULT

```
                                            ‫میگونشد‪..‬‬
‫سرپادشاهان مویباخته‌اند کولاه مرصع را فيز‬                   ‫جن‬     ‫دڼو مر د" ‪ -.‬دراصطلاح مى‬
                                              ‫گوشد ‪.‬‬       ‫ومردم مفد ومفتن باشد ‪ -‬و لومی ازحیوان هم‬
                                                         ‫مشتگه)‪.‬‬    ‫کاو مغك س‬             ‫چش‪:‬‬   ‫((‬


  ‫از ‪ :‬دیو ‪ +‬لاخ ( يسولف‬                                 ‫رك ‪:‬‬                         ‫‪:‬‬    ‫رك‬    ‫‪8‬‬

          ‫اهرمن لاخ‪.‬‬    ‫لاخ ‪۰‬‬    ‫لام »کوج ‪ ۰ ۷‬حندولاج ‪3‬‬                    ‫نسر‬   ‫‪۴‬ك‬             ‫مکان ) ‪.‬‬
   ‫ءنبت وتصفیر) = دبوك د=بوچه‪ ,‬دراوراق مانوی بپارنی ‪8۷/4‬‬
                                                       ‫‪ :‬دیو‪( +‬‬                       ‫از‬         ‫‏‪e‬‬




                                ‫(کرم)‪ .‬درپهلوی ‪ 12۷6‬که خرفتری محوب شده (شابد ‪ :‬زالو) ‪.‬‬
         ‫‪Henning, A list of Middle‬‬                       ‫‪Persian...,‬‬   ‫‪BSOS , IX , 1,p.82, 90.‬‬
   ‫‪ ( 2۲۵1‬افر ) بادشاه ابران بسته میشد ف«رهنك‬                    ‫رکه‬
                                                                 ‫د‬    ‫اسلو لوار ا رشته "مخصوصاً بنو‬
                                                                   ‫کاری‬
                                                                   ‫نیگ‪-‬لیی ‪ .‬لبدل واسکات › ‪.‬‬
                                                                                           ‫اات‬
                                                                                             ‫پو‬
                                                     ‫* ده ‪ -‬بکرارل ‪.‬رك ‪ :‬ده (بکراول) ‪.‬‬

=========NEXT LEAF 382=========
                                                     ‫ن|حام‬

        ‫در حرف ذال نقطه دار‪.‬با حروف تپحی مشتمل بر سزده لغت‬
‫بل د بکراول وسکون بای ابجد ‪۴‬‬                                 ‫* ذاقنو بداس ‪ ۱‬سبکرفان ونون‬
‫ولام" بوست لاك بشت‌هندی باشد؛ وبعضی گویند‬                    ‫مواو رسیده و کت بای اند ودال بنوقعاه بالف‬
‫آن با‬   ‫است؟ ‪.‬خاکنتر‬         ‫دكربیشتابی‬
                                      ‫بوست لا‬                ‫کیت ورین مه زود امسانتبای‬
                                                             ‫وویند نوعی‬
                                                                      ‫بعنی مانند غار »آون داروبی‌است گ‬
 ‫‪ ۰ °‬بر وزن و معنی درخش‬                                            ‫از مازربون است وبرکث آن یهن مبباشد‪.‬‬
                                  ‫ذر خش‬
          ‫است که برق وتابندن وروشنی باشد ‪.‬‬                   ‫ذاقی ‪ = ۴‬بروزن سافی؛ بیونالی درخت‬

 ‫ذرع = بروزن‌سرع ک‪.‬نارو گوشة کشت‬                                                         ‫غار را گونند ‪٤‬‏‬
‫بمعنی کز باشد؛‬    ‫و درعری‬    ‫‪-‬‬   ‫وزراعت راگورند؟‬                                         ‫وآن درختیاست‬

   ‫وآن چوبی است که چیزها بدان پیمایند ‪. ۷‬‬                                                ‫که برکش از‬
                                                                                         ‫گبهر‌بید درازتر‬
  ‫ذر یس ‪ -‬ببایس‌ینقطه (‪ )۱‬بورزن‬
                                                                                          ‫واز برگے مورد‬
                                                                                          ‫برزکتر ولرمتر‬
                                            ‫ات ‪. ۸‬‬                                        ‫وسقیدتر میباشد‬
                                                                                         ‫و موه آن از‬
 ‫ذقکر ‪ -‬باکاف بروزن کفتر‪ ۰ .‬تخم‬
 ‫کرفس کوهی است وآترابیونانی فطراسالون ‪٩‬‏‬
                                                                                             ‫فندق کوچکتر‬
                                                                                         ‫واز نخودبزر کتر‬
                                            ‫خوانند ‪.‬‬
                                                                                         ‫است‪.‬اسهال خولی‬
 ‫کر ‪١‬‏ بفتح اول وکاف وسکون رای‬                                                       ‫را نافع بود ویکنوع‬
                                            ‫ذ‬
‫قرشت » بلفت زند ویازند (‪ )۲‬بمعنی نرباشد که‬
```


## [2026-09-05T17:31:16.617Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt; do echo \"== $f\"; grep -c \"دیهیم\" $f 2>/dev/null; done"
}
```


## [2026-09-05T17:31:17.712Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"دیهیم\\|دهیم\" incoming/ARY/ARY_pages.txt | head -20; echo \"=== ARY دام ===\"; grep -n \"^.*دام \" incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-05T17:31:18.155Z] TOOL RESULT

```
== MON_part1.txt
5
== MON_part2.txt
4
== incoming/MON/MON_2vol_Adena_v1_djvu.txt
5
== incoming/MON/MON_2vol_Adena_v2_djvu.txt
4
```


### [2026-09-05T17:31:18.206Z] TOOL RESULT

```
=== ARY دام ===
659:پاسداری مرزهای امپراتوری روم در شمال انگلستان؛ به استخدام رومیان درآمدند
1371:دارد ولی هیچکدام از پسگشت‌های در دسترس من اشاره‌ای همریشه‌های ایرانی و سانسکریت این
1538:آشکار است). لازم به ترضیح است که در هیچ کدام از مراجع اشاره‌ای به رابطه‌ی "آرواره" با این واچریشه‌ی هند و
1744:۱- رابطه‌ی واژه‌ی "آستر"(پهلوی )) با دیگر واژه‌های این فهرست در هیچ کدام از پسگشت‌ها(مراجع) من
1892:سانسکریت. (8۸4(/5577): ادا 0 3 (۸۸۴) یدام ده ها
```


## [2026-09-05T17:31:20.248Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -A3 -B3 \"دیهیم\" MON_part1.txt | head -60"
}
```


### [2026-09-05T17:31:20.307Z] TOOL RESULT

```
15042-افسد: 0۱ [ع.] (ص تسفضد.) تسباه‌تر) 
15043-فاسد تر» تبه کار تر. 
15044-
15045:افسر: ۲م (.) تأج» دیهیم» کلاه بادشاهی. 
15046-افسر: ۲ (.) (نط.) کسی که در نظام 
15047-دارای درجه باشد؛ صاحیمنصب. ضمح. 
15048-فرهنگستان این کلمه را به معنی فوق از انگٌ. 
--
15878-و متعارف انجام دادن. 
15879-
15880-اکلیل: (ع.] (ا.) تاج» افسر دسهيم. 
15881:سر بند؛ ج . اکالیل. ۰ (گیا.) دیهیم. (نق.) گردی 
15882-است ِ ره رنگ‌های طلابی» نقر ه‌ای» 
15883-سبز و غیره. 
15884-
--
36428-آذینش گرزن است. میوه‌اش سته می‌باشد؛ 
36429-انگور روباه» عنب‌العلب. 
36430-تاج‌گذاری: آ2022۲-1-.۱ [معر. ف.] 
36431:9 آیین | نهادن دیهیم بر سر بادشاهی 
36432-نوء جشن تاج گذاردن پادشاهان؛ تتویج» 
36433-تاجور: ۱-57 (ص‌مر.) دارای تاج با افسر. 
36434-بادشاه» سلطان. 
--
64919-ی است:و کازها: تقریاً در یکك سطح 
64920-قرار گر فته‌اند. 
64921-
64922:دیهیم‌ جو(ی ): ٩.-10(‏ [یو. ف. - دیهیم 
64923:جو بنده] (ص‌فا.) آنک دیهیم جو ید» کسی 
64924-که درصدد بدست آوردن تاج بادشاهی 
64925-
64926-
```


## [2026-09-05T17:31:23.845Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '64890,64930p' MON_part1.txt"
}
```


### [2026-09-05T17:31:23.895Z] TOOL RESULT

```
دیوگرفته] (ص‌مف.) کسی که او را جن گرفته 
باشد؟ مصر و ع. 

دیولاخ: 5-.0 (امر.) ام دیوه مکان 
دیوان. صحرایی که از آبادی دور باشد. 
جایگاه خرات» خرانه. چراگاه دوردست. 
سر دسیر. 

دیومر د. 0 (ص‌مر.) مرد بد درون» 
مرد پلید» شیطان‌منش. مرد بیابانی» وحشی. 
غول» نسناس. 

دیوه: (0-)2-*0 (امر.) دیوکک» زالو. کرم 
ابریشم. 

دیویریود: 11202 (۰) (نسط.) واحدی 
نظامی؛ لشکر. ۱ 
دیه: )رنه [ع. دی ] (.) بولی که قاتل با 
اقوام او برای جبران قتلی که واقع شده 
پردازد؛ خونبها. 

دیهول: (قد. ٩[۳51605--‏ [- داهول] (ا.) تاج 
مر صع. 

۳ مج .32۳1۳00 (۰) نواری 
مخصوص که گرد تاج پادشاه ایران بسته 
می‌شد. زره بادشاهی کلاه مرا صع: . (گیا.) 
نوعی گل آذین که شیه گل آذین خوشه‌یی 
است» منتهی رشد و نمو دم گل‌های بایینی 
ی است:و کازها: تقریاً در یکك سطح 
قرار گر فته‌اند. 

دیهیم‌ جو(ی ): ٩.-10(‏ [یو. ف. - دیهیم 
جو بنده] (ص‌فا.) آنک دیهیم جو ید» کسی 
که درصدد بدست آوردن تاج بادشاهی 


۷" 


3: 2 (حر.) یکی از حروف صامت فارسی و
```


## [2026-09-05T17:31:32.878Z] TOOL CALL #34: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/ 2>/dev/null; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ 2>/dev/null"
}
```


### [2026-09-05T17:31:32.913Z] TOOL RESULT

```
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
```


## [2026-09-05T17:31:39.337Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint('n',len(pages))\n# find tags\nfor p in pages:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m and int(m.group(1)) in (538,539,540,541,542,543):\n        print('=== ',m.group(1))\n        print(p[:1200])\nEOF"
}
```


### [2026-09-05T17:31:41.233Z] TOOL RESULT

```
n 721
===  538
[pdf page 538]
‎Wet‏ کرهن
که ها بائد لیکن بطریق خفا بیان باید کرد | میکوند ۱ - و بستی نهیب و حبله هم آمده
چنانکه مسمای ها بقملآید ویبکون‌ميم. کیاهی 5
است که آن در زمین شیار کرده میباشد و بیخ کوصهة آب ۵ » بینی جت و خیز
‎olen»‏ به نی میماند ۱ . آب است ده موجه بزرکه باشد .
کوه محروق »یمن ی کوه سوخته , کوه ] سمان = ‎pine‏ بلندی ‎OAT‏
‎say : 31.‏ است ‏ و پیمتی اوج هم آمده است .
وآن‌کوهی است سیاه در حدود ارمن . : |
کوهنگ ‏ بروزن ‎sp‏ ۱ کوهه گرفقه - جن کرفتهرا کون
مه ی | پیز بیس کار ‎Wea Sop‏
‎gee ۳‏ شخصی کهاو را جن گرفته باشد
خی زگرد و ‎wea‏ گو هی ‎oY‏ با تاك بتحتانی رسیده ,
کوهه © با ثانی مجهول وفتح‌ثالث» | آلوی کوهیرا کویند و بعربی زعرور خوانند -
زین اسب را کوبند عموماً و بلندی پیش و پس | ومردمی را یز گوبند که در کوهستان میباشند.
زین اسب را خموصاً چه پیش را پر کوهه‌وعفب کوهیج ‎lt Ga‏ و سکون
را پس کومه خرانشد - و هر چیز بلند دا ی | ‎gies‏ وجیم . بمعنی کوهج است کهآلوی کوهی
کفته‌اند ۴ - و برآمدگی پشت کاو و یشت‌شتر

‏باشد و بعریی زعرور خوالند .
را هم ‎es‏ - و مطلق ‎Vath‏ نیز گویند کو شین = بائالیمجهول بروزن زوبین»
- و بمعنی موجه آب‌هم هست ۵ - وجن رالیز

‏کیاهی است که بیج آن به بخ نی میماند و در
‎oS‏ اند چه جن گرفته را کومه_کرفته هم | زمین شیر کرده سبار است ۱۴
‎٩‏ رگ :کوهین ۴ - رگ : رشیدی ۰
===  539
[pdf page 539]
کوعه

کوی ۱ بر وزن جوی » راه فرأخ
‎lS,‏ را گوبند که شاه راه‌باشد - وبمعت یگنر
ومحله ‎ote‏ است .

‎MOS‏ © بروزن‌مورچه.سی رکوی
است که راء کوچك وننگه باشد ۰

‏کویر- بکر اول و ‎gis‏ مجهول
بر وزن دلیر » زمین بی ‎OT‏ و شوره زار باشد
‎LT,‏ :م‌بی‌فراح کوبند ۴ - ویمعنی سراب حم
آمده است و آن زمیتی باشد شور که از دور
‎TE‏ ماند - وزمینیرا نی نکفته‌اند که باران‌بر آن
پاربده باشد ومردم وحیوانات دیگر بربالای ‎OT‏
‏آمد وشد بیارکرده باشند وآن زمین‌بمربه‌ای
خشك وناهموار شده باشدکه تردد و آهد و شد
‎Oly‏ دشوار بود - و بمعنی شیر ژبان هم آمده
است که شیر خشمناله وقهررآلود باشد *

‎pT‏ با ثالك مجهول بر وزن مویزه
کنج ‎LS,‏ خانه راگویند ۴ ۰

‎» ‏بر وزن تمیز‎ eh ‏با زای‎ 2S
‏بمعن ی کیل بائد وآن پیمانه است که چیز ها‎
‏پدان پیمایند وبعربی‌ففیز خوانند- وبعض یگویند‎
‏کویژ بمعن ی کیل بفتح کف بت بلکه بکس‎
‏کاف‌است رآن‌میوه‌ای باشد صحرائی شبیه بسیب‎
BFS ator ‏وآلرا در خراسان علف شیران و‎
+ ‏خوانند. ائهاعل6‎

‎۷۷۲

‏کو یت" - بنم اول وسکون سی‌بی.
نقطه بروزن گربشت, ‎saw‏ کوفتگی و آزارباشد*

‏کویستی ’- بنم‌اول‌بروزن بگریختن»
بمعتی کوفتن ‎ald‏ وغیر ‎OF‏ باشد ؛ ‎Kay‏ اول
وفتح اول هم آمده است ۰

‏کو ‎Sse 4 ead‏ بروزن ‎ww‏
‏له کوقنه شده راگویند - و دو طرف سرین
وشتکا‌رایز گفته‌اند وظاه رآ که ‎CRS‏
‏نون صحیف خ
===  540
[pdf page 540]
عباوت کوی ‎ak‏

کنابه از ‎Ws‏ ورو زکار است ۰
‎SLES‏ ۱ > بانستای بالف کنیده
‎ling‏ وفوفالی زده » طفلی راکوبندکه برس راء

انداخته باشند -

دست افزاری است روغنگرانرا ‎US ase‏ ترازو
که از ب رکه خرما بافند ۰

PIS ‏منم اول و فتح نات‎ OST
- ‏شیری نکه مردان خورند‎ ate

کوی هفتاه داه- بکر ‎salt‏

Pgs ‏بیست و‎ oly

درکاف تازی با ها مشتمل برچهل و پنج لغت و کنایت

که - بفتح اول وسکون و ظهور انی »
مخفف ‎AS‏ انت که اسبان و ختران ‎AM,‏ و
خران خورند ۴ - ویضم اول 6 مخفف کوه است
که عربان جبل کوبند ۴ - و بضم اول وقتح
ثانی؟ ‎Gite‏ کوحه اس تکه پیش و پی زین

اسب - ‎dey‏ آب ۵ - وبلندی پشت شتر وکاو
‎Wark‏ - وبکسراول وظهور الی . بمعنی کوچك
باشد ۷ - ویک اول وخفای ‎GE‏ » افاد#معنی
علت ودلیل کند چنانکه کوبند «بسپب آش‌زدم
که ‎jl‏ لمیکرد ‎hee‏

(۱) چش : دویم .

‎٩‏ - یمنی : یافته در کوی (وبرزن).

‏۴ راك : که :

‏شنو اکنون صورت افاله را ليك هن از که جداکن دانه را .

‏«مولوی , مثنوی چاپ علاءالدوله صس ‎RAVER‏

‏۴ - رك: کوه .

‏۴ - درین صورت ‎AS?‏ بابد لوشت . در سیستان جابی بنام «قوحه» ( معرب «کهه ©
ودکوعه» ) بوده است «تاریخ سیستان ص ۳۳۵ ح ۳ . ۵ قی ‎kohak'> ju):‏

‏( کوه, موج.) «هوبشمان ‎AVE‏ 3 = کوهان (ه.م.) ۷ - اوستا18512 (کوچك
‎ ۷10)1(5) ۰ kas ode‏ افتانی ‎eS) kashr‏ » شاکرد ) ؛ استی ۷55/8۲ ( شاگر
===  541
[pdf page 541]
کپا ۱ - ۵۵ ۱۷-

گها هب وزن ‎the‏ پممنی. خیل | کیهان هم هست که آن ‎at‏ بسعنی جعان
ومنقعل وترمنده باشد ‎٩‏ ۰ است ۴ - و بکر اول , جمع که است ؟ که
‎ST‏ ابر وزن شهاب , کیاء ها | بسمنی کوجکان وخردان باشد -
ودواهای _ جوثانیده باشد که گرما رم بر عضو آگهیپ ‎ph‏ اول وکسر ثانی وسکون
ورم کرده ‎ole TS‏ بر آمده بندند تا درد ساکن بای ‎al‏ , نی ننگه ‎tate ae‏ و ‎TS‏
‏شوو ۰ ‎Syl‏ یز ‎as‏ آمده است
کهان ‏ بنتخ اول » بر وزن و ‎wm‏ کهید ۱ ضم اول وئالث وسکون
جهان است که ‎dle‏ ودنیا وروز کار باشدومخفف | ثالی ودال ‎«dom!‏ مخفف کوه بود (۱) ‎sical‏
‏(۱) چش : کوه بوده .
‎٩‏ - بدست خود که کندباخود این که من کردم
کهای توبه ام آخر ز احمقی تاکی ؟
نزاری فهتانی ۶ رشیدی * .
- رشیدی گوید: «کپاب و کهتاب ‎eal‏ » کاه دود که برای پیماری ‎lel‏ کنند .
قطران گوید :
‎(ly‏ چون او باشند مهتران نه بفتل بود برنگه بیکی‌دود داغ ودود کهاب.»
«کهاب و کهتاب ۰ اهار راگوبند که جوشالیده گرما کرم بر عضوی که دردی با ورمی
داشته باشد » با برآمده باشدیبندند تا درد ‎OT‏ تخمیف یابد .» وهمین بیت قطران را شاهدآورده.
ولی ثهاب درین ‎Cy‏ باحتمال فوی تصحیف « کباب» است (رك : فرهنگک نظام) . این‌بیت‌دردبوان
قطران باهتمام نخجوانی لبامده ورك : کهتاب ‎ .‏ ۴ - صحیم «گهان» مخذف «کیهان» است .
۴.- چنانکه کویند: ‎YT gale‏ رك: که. ‏ ۵ - ر: جهانگی
===  542
[pdf page 542]
‎Le ۱ ۱۷ 0-‏
کوه بودنده که عبارت از زاهد و عابد و .هرتاض کهبله ‎eae?‏ اول بر وزن بتکده ,
و کوشه شین ودهقان ‎ath‏ - وبمعنی تحصیل‌داد | ‎ag pines‏ است که بیمقل وابله واحمق باشد ؛
وخزانه دار ۱ و صراف هم هست و عربان افد ویفتح اول هم آمده است ۰
خوانشد بکر قاف - وبمعنی‌سسار نیز گفته‌انده که پیک © مخقفکوه پیکر اس ت که
‎lan,‏ آخ رکه خزینه دار وصراف وتحصیل‌دار فیل وا قوی ‎Je‏ باشد .
وسمار است بفتح اول و کر اول هم آمده‌است ‎ek‏ ۱
که بر وزن سرمد و اممت باشد و معرب آن بط س بر وزن مهتاب » بمعنی
جهید است کاه‌دود ‎Lgaly tk‏ جوشانیده را نیز ‎SF ais gS‏
‎nine ۴ 1‏ اول پروزن ‎Ue ey‏ کرماکرم بجهت تضفیف وجم ودرد برعضو ورم
کهبر بفتح اول بروزن دهبی » 6 کرده واز جای برآمده پندند؟ .
لاشست در هندوستان + ۳
‎ar) ? ۰‏ اون و رای 5 گهتر ۲ » بکراولبروزن مهتر ؛بمعنی
‎re‏ بفتح اول و رای قرشت
ناخ رکه 8 اجك وخر دباشد-
پروزن احمدكك » بادنجان راگوبند و ‎OV‏ چیزی کوچکتر باند چه که ‎Che iS ines‏ وخردباخد
است معروف که قلیه کنند نوخورند ۰ کهر- بتح اول و ثانی بر وزن ‎ste‏ ©
‎en = ee‏ اول بروزن مهمل؛بمعنی کی اش ‎sre‏ اسب واستر ‎eels‏
‏بشد .

‏بی عقل و احمق ‎ably‏ بائد ۴ ‎Jl cist‏
وش ‎elt‏ هم آمده است ۰ کهر بات ‎Gi‏ ربا است ۸

‏۱ - تباید عمی‌کین درم خورده شد رد ومو بد و گهیدآزرده شد.
. «فردوسی طوسی.٩‏
‎Laka‏ ب
===  543
[pdf page 543]
کپربا دنگ
ه رکه با خود دارد از علت برقان ایمن باشد ۰

کهر با و لاه ‎gine‏ لون و ‎Sy‏
‏زرد است - و چیزی را ‎Ga‏ کویندکه خاصیت
کامربا داشته‌باشد - و کنایه ‎oddly it‏ ویردارند
وسبك دست هم هست +

کهرم۱ - ‎pe‏ اول بروزن رستم » نام
مبارزی بوده تورانی که بردست یکی ازپهلوانان
ایرانی در جنکه دوازده رخ کشته شد ۰

‎che ۲ ۵‏ اول بر وزن بهره »

‎. )۱( ‏شیر هست را گویند‎ UE

‎DH‏ بر وزن ‎Je‏ خردل‌بوستالی
‎Fast‏ کویندا کر آبآترایگیرند ودرپای‌درخت
‎il‏ فرش بربزند انار آن درخت شیرین گردد ؛
و بسنی کوبند تره تيزك است که بزبان عربی
‎po >‏ خوانند .

‎» ‏پفتح اول بروزن مهزل‎ « Se
‏رستنی وداروبی باشد که در دواها لیز بکار برد‎
‏وبعربی جرجیرکوشد - ادرلر آوید وملین‌وسخن‎
+ ‏و مقوی باه باشد‎

‎ie AS, ‏کهصاد* » بروزن‎

‎. ‏گویند‎ ... oT ‏خم۱:‎ )٩(

‏‌۱ع۱۷-

‏کوهار است یمنی زمين وجایی که درآنجاکوه
بیار باشد .

‏کههتان ۲ » بروزن ‎ON‏ مخنف
کوهتان است - و نام ولابتی است از خراسان
ومعرب آن‌فهستان‌است والحال بتعریب‌اشتهاردارد.

‏کهسته نم اول بر وزن کته »
کوز؛ پر آب را کونند ۷

‏کهله ‎A‏
‏واحمق باشد .

‏شته ‎٩‏ » باشن نقطه دار , بروزن

‎* ‏کپته است که کوزة پررآب باشد‎ gary

‏کهکان ‎ee‏ اول وکاف بروزن‌بهتان»
‎eae‏ کوهکن باتد *۱ و گهکانی_بنمتی
کوهکنی ۱۱ .

‏کهکشان "۱ = بروزن‌مهوشان متفف
کاهکتان است و آن
```


## [2026-09-05T17:31:51.844Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor p in d:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if not m: continue\n    n=int(m.group(1))\n    if 544<=n<=552:\n        print('===',n, 'printed ~',n+1207)\n        print(p[:900])\nEOF"
}
```


### [2026-09-05T17:31:53.651Z] TOOL RESULT

```
=== 544 printed ~ 1751
[pdf page 544]
۱۷۷
‎Syl‏ کنابه از اسب وشتر ‎ash‏ - فرهاد را
‎ps‏ گونن که عاشق شیرین بود» ۰

کهلم ‎ch‏ اول ولام بروزن‌شلفم +
پمعنی بادنجان است =

‎AG”‏ - بنتم اول بروزن بهله ۰ ریزها
وکاورسهای زر وسیم را گویشد- و زر سفید (۱)
را نیز کفته‌اند ویترکی آقجه خوانند ‎He‏

‏کهنیاد. بفتح اول و بای ابجد بروزن
قلم‌کار. مخفف ‎Ll OW‏ است که انبار کام باشد -
ویضم‌اول بمعنی خانه‌است که بعربی بیت‌خوانند
و بارگاه را نیز گویند و زردشت گفته است که
رو زکار کهن بارها کرده است وبهرباری گونه ای
آفریده است چون آسان و زمن وکیاء ۳
جالوران؛ ‎Valery‏ بامردم بسالیآفریده وهر يك
ازین کهن بارها پن‌روز است ونامشان‌هم کهن‌بار
است ‎Jol GEL‏ ودوم همچوکهن باراولو کین
بار دویم و کپن‌بار سیم وفارسیان بهرکهن باری
جشنی سازند وعید کنند چنانکه درکاهنبار,تفصیل
‎ae‏ کور شد ۷ .
کهن خرابات - کنابه از دای
قانی‌است .
کهی ذذ © - بازای‌هوزبروزن‌مبتس,

‏نام قلمه‌است قدیم از فلاع بدخثان وممرب‌آن
قندز؟ است » والحال نیز بقندز اشتهار دارد *

‎P
=== 545 printed ~ 1752
[pdf page 545]
کهیز سلنده
نام قلعه‌ای باشد از ‎EY,‏ میستان ‎٩‏ - وبسنی درختی است ت 5 ‎els,‏ مانند شیطرج ‎BAYT,‏
‏گوند کهیج معرب کهی باشد . دواها بکار پرند .
گهیر ۲ - با الك مجهول بروزن‌صفیر» کهین - ‎«oS NS‏
سیب صحراثیراکونند ‎LT,‏ در خرانان علی | بمعنی کوچکترین_باشد چه که بمعنی کوچك
‎aa‏ است ۵ . -وسیب صحراگیرا نیز گونند که‌بعربی
شیران وبعربی زعرور خوانند . مب من جر >

زعرور وذوئللة حباب خوانند پسیبآنکه ‎Bits‏
‏کهیلا = بالامبروزن ‎sicker» Col‏ ] آن سه پپلو ‎Mattes‏ .
بود ایرای ۴ +

کهیثه ۲ بکراود بر وزن‌نگینه,
گهچله ۴ > بر وزن ‎dee‏ پوست. | بمعنی کهین است که کوچکترین باشد .

بیان بیست وسیم

در ‎GE‏ تازی با ‎GL‏ حطی مشتمل بر یکسد و پنج لفت و کنایت

کی « بفتح اول و سکون ثالی » بمعنی : این لفظ راکویند ۸ -و یمعتی پادشاه پادشاحان
کدام و چه وقت باشد ۸ - ودر وقت انکار نیز | است یعنی پادشاهی که در عصر خود از همة
۱ - جهانگیری کوید : در اين ایام به کهی مشهور است :
‎ts‏ کارام گیرند هیچ سپاهان ما با 
=== 546 printed ~ 1753
[pdf page 546]
uw -۱۷-

پادشاهان بزرکتر باشد و بعربی ملك الملوك | وترجمةٌسلطان هم هست ‎٩‏ - وبعضی کوینداین
خوانند ۱ - و پادشاه فهار و جبار ‎ath‏ مرتبه دا | تلم را زال پدر رستم بقباد گذاشت وکیقباد
لي زکویند ۱ , واين تام را در بلندی وقدر از | ‎Vals‏ - و در عربی بتشدید ثانی . بمعنی‌داغ
‎whe Sol”‏ ؟ چد اوبلندترین کواکبسباره | باشد که بردست ‎by‏ واعنای دیگر نهند - ولکه
است » وبعضی کوبند معنی لفوی کی پادشاه قباد ] ونان را هم کنته‌اید ۷.
است ودر قدیم اين چپار پادشاء را که کیکاوی کیا «پکر اول و ثانی بالف کشیده .
وکیضرو وکیقباد وکی لهراسب باشد «کی» .

بمعتی کی است که یادشاء بز رکف جبارباشد -
میگفته‌اند ۴ وسنی پنج میگوبند و کیومرترا | * ی
داخل میدانند ۴ - وهريك از عناصر ‎aw)‏ را و مرزبالرا یز کوبند که زمین دار باشد یعنی
نیز کمته‌اند ۵ - وبسمنی پا کیزه واطیف‌هم آمده | پادشاء كوچك - وپپلواندا ‎we‏ سویمعئی
است ۷ - واصیل وتجیب را نیز میگویند صاحب وخداوند نیز آمده است . ‎٩‏ - ویمعنی

۱ - در اوستا 12۷1 
=== 547 printed ~ 1754
[pdf page 547]
کیابلد
وعقال هم هست - و طبایع را نیز کوبند که
پرودت وحرارت ورطوبت وببوست باشد٩‏ سوهر
يك از عناصر اریمه را نیز ۴ - وبمعنی پاکیزه
ولطیف هم کنته‌اند ۴ - وبلت سربانی مسطکی
‎aS,‏ وآنرا بعربی علك رومی خوانندوبسنی
کوبند ‎tlle‏ رومی تومی از مسطکی است ۴ -
ویمعتی دهان هم بنظر آمده است که بعربی قم
گویند .

‎ULF‏ - بادال ‎sen!‏ بروزن‌خرابات,
‎gine‏ جبروت است همچنانکه روان کرد پممنی
ملکوت باشد -

‏کیاچود = ‎pe‏ اول بروزن بلادور ؛
عاقل وفاضل ‎bby,‏ راکویند ‎٩‏ +

‏کیاخره ۲ - بکر اول و شم خای
‎babs‏ وقتح رای ‎abi‏ توربراکویند که‌از
‎Slate‏ بیادشاهان‌فایش(۱) کردد چه کیا ‎eet‏
‏پلدشاه وخره نوری باشد از ‎ile‏ خدای تعالی
فایض(۱) بربند کان‌خود که بسبب آن‌رباست کنشد؛
وباواو معدوله هم آمده است که کیاخورهباشد.

‏پوت

‏" کیاخن - بر وزن فلاخن » بسنی
‎Kaaba pal‏ واستواری ورمی‌وهمواری
کاری کردن ‎Auth‏ - وسخن چرب وشیرین راهم
کفته‌انه ؛ وباکاف فارسی هم آمده است.

‏کیاخوده ‎٩‏ - با واوسسدوله‌بروزن
ومعت
=== 548 printed ~ 1755
[pdf page 548]
۱۷۵۱

بخوردنی ‎ath‏ واین حال بیشتر زان آبستن را
چم رت ۱ ۰

کیادش- بفتع اول و دابع بر وزت
جفاکشی .نام یکی از چهار پسر کیتباد
است؟ ۰

کیا دهین © ‎eek‏ پروزن فروردین»
ام یکی ازچهار پس رکیقیاد است (۱) ۰

‎LST‏ » با کاف فارسی در آخر
پروزن‌دماوند. رنگه‌پا کیژه ولطیف رااگویند؟ -
ویسعنی سفید جم آمده است ۰

‎HILT‏ - بکاول ‎py‏ زای‌شلمدار
وسکون نون ودال ‎vine latin‏ پادشاء‌بز رکه
وعظیم باشد چه کیا پادشاه و زند بز رکه ‎fan)‏
‏را گویند .

‏(۱) چش : -کی‌ارمین ... کیقباد است ۰

‎ws
‎. ‏اول بر وزن چراغ‎ Ge rel”

‏بمعت یگیاءه است که علف باشد ۰

‎LF‏ - بائاف درم ظرسی بر وزت
مساکن» بمعتی مخالف باشدودرشت وتاهموار
را یز گوبند 6 *

‏کیان - ‎ca‏ اول جم عکی باشد بستی
پادشاهان ‎she‏ بز رکه ۷ - وپادشاهان ‎SAMS‏
‏کفته‌الد که کیقباد و کیضرو وکیکاری و کی
لهرامب باشد ۲ - و یشم اول ‎tse‏ کردیوا
کون دکه بيكستون بریای‌باشد و آتراکنبدی حم
میگوبند , و بس یکوند ‎bas‏ کردان ( ۷)
وعربان صحرا شین باشد ۸ » ویک 
=== 549 printed ~ 1756
[pdf page 549]
کیان خره
باشد که حرارت وبرودت ورطوبت ‎mel pty‏
وعناصراربمه را یز کوبند - واصل وبنای‌هرچیز
‎wld‏ - و مرزبالرا هم میکوند که زمين
دار ‎oa ath‏
گیان‌خره ۴ بن خای شطه دار
وقتح رای بی‌قطه بممنی کیاخرء است و آن‌نوری

باشد از جااب ‎a‏ بسوی یادشاهان. چه کیان

پادشاهان وخره لوری و پرتوی را کویند که از
جالب‌خدای‌تعالی به‌بند کان فایض(۱)شود که‌بدان
سبب بعضی پادشاهی ورباست کنند وبسنی‌ستمت
وحرفت آموزند +

کیان‌خوده ۳ - با واو مسوله,
‎ae‏ کیان خره است که نوری باشد از جالب
اه فاییض(۱) بیادشاهان ورژسا -

کیپا ۴ = بفتح ‎Shy Jol‏ فارسی بروزن
شیدا » بلفت زند وپازند نقره را کگوند و بعریی

فنه خوانند .

کی بشین* ‎bo‏ بای فارسی و شن

۱۷۵۲

قطه دار بروزن درگزین » نام .یکی ازچهارپس
کیقباد است ؛ وبجای بای فارسی نون مکسورهم
پنظ آمده است +

کیبو - بکسراول وم بای ابجدیروزن
تیهوه مرغی‌است بزر کهآ نرا دبنارهم‌میگوبند؛
وبسنی گوبند مرغکی است کوچك و رنگهای
مختلف دارد و آشبانی سازد که کوبی از رسمان
پامته‌ان
=== 550 printed ~ 1757
[pdf page 550]
—\ver—

صلب‌واز درخت لوعی از بلوط بهم میرسدوبعربی
صمة ‎oan SEAM‏ وبحذف تحتانی بعد از فا
‎ean jt‏ است؛ وب ی گوبند سریالی است

‎Ts‏ با ‎we at‏ 9 وزن سرا
وریم نقره رااگویند ویعربی خبت الفضه خوانشد.

‎Sear‏ اول و سکون ثانی وجیم
‎aml‏ خرالاغ دم بربده رااگوبند٩‏ -وچاروایپرا
تیز گفته‌اند ‎pS‏ کلو وزیر دهاش ورم ‎GETS‏
‏کرده ‎ath‏ +

‎OF‏ » بکر اول ‎Os‏ ثانی و جیم
فارسی » بمعنی_پراگنده و پررشان باشد ۴ -
وجنی از ‎Lele‏ ابریشمی هم هست- ونام ولایتی
است ترديك بیستان ۴ - و بمعنی کم واندك
‎al, cle Sy‏ هم آمده است ۴

‏کی کیچ * < بروزذییج ‎nes‏

‏کوچك کوچك وخرد خرد ‎sols Saal Sally‏

‏آعته باشد ,

‎MT Sine pals ‏داش‎ -

‏ص۱۱۲

‏۴ - رك: کیچ کیچ .

‏کیچه ۱ ‎Ge‏ اول وئتح الك ۰
کوچه است که راء تنگه ‎sath‏

‎a‏ ۷ = بکراول وسکون‌انی‌وخای
‎abe‏ دار . ‎SSW Se‏ درکرشهای چشم
بهم رسد » وچ رک ی که برردست وپا نشیند ۰

‏کیخرس . بنتح اول و سکون ثالی
وضم خای نقطه دار وسکون را وسین بی ‎“us‏
‏غله‌است که آنر
=== 551 printed ~ 1758
[pdf page 551]
وچیزی دا یز کویند که بدان طلا ‎Sealy oy‏
‎UT‏ بپم ‎as, Ses‏ وآلرابسریی لحم خواند۱ -
و پزبان ‎er‏ پممنی مکر و حیله - و جنگه
وجدال - وحایض شدن زن باشد ۴ ۰

. ‏با بای فارسی بروزن اژدها‎ - YAS
weg ‏بردع بوده واو را‎ ak ‏تلم زلی است که‎
. ۴ ‏میگنته وممرب آن قیدافه است‎

کیرخ - با اود ‎gh‏ رسیده و رای
بی‌هطةٌ مقتوح ‎Gln‏ تقطمدار زده » دوتختمیان
پیوسته ‎ath‏ وقرآن و کتاب.برآن پندوصربی
رحل خوانند ؛ ‎orks‏ معنی باکاف فرسی‌هم آمده
است واسح آن است * ۰

kin ge 1 ay ‏بر وزن‎ 2 IS
‏ونگاهداختن وحصول چیزهایی باشد که پیش از‎
+ ‏در ذهن پوشیده بودم‎ yl

گیریان ۱ ‎shh‏ حطی بر وزن
میهمان » ییمتی فد وقربان باشد وآن‌پدلی‌است
که خود را با دنگری را ‎oly‏ ازبلا برهاشد.

کیره با ول ‎gt‏ کشیده وبزای نتطهرار
زده ۰ بسعنی تمد باشد ۷ رآنرا از پشم مالند
و جریی لید (۱) کویند .

)و9

‎oe”‏ - بکس اول وسکون تانی‌وسین
‎tty‏ » چن و شکنج راگویند ۸ - و بعربی
توبره وخر ‎aly‏ را خوانند ‎٩‏ .

‏کیسر گو نه ۲۰ - بنتع 
=== 552 printed ~ 1759
[pdf page 552]
—\vee~

شدن باشد ‎ute‏ چیزی صورت اسلی خود رارها

کند وصورت دیگر بهتر از آن بگیرد .
کیش با ‎gt‏ مجهول بروزن رش»
بممنی تر کش باشد وآن ‎gle‏ است که‌تیرد رآن
کنند وبر کمر بندند ‎٩‏ - ویمعنی دین ومذحب
‎chy‏ هم آمده ‎col‏ ۴ ۰- وپرمرغالرا گویند
مطلفاً ‎Lye‏ پری که برتیر اصب کنند ‎phe‏
‏شپری است در جزیره‌ای از دربا و ‎Ol‏ بهرموز
اثتهار دارد ؛ و وجه این آن است که چون بر
بلندیهای اطراف‌هرموز ‎aisle ae Teg‏ کیش که
ت رکش باشد پنظ درمیآبد ۴ - ونوعی ازجامه

بو که از کتان بافند 6 - ‎(by‏ جانوری‌است که"

از پوستآن پوستین کنند ۱ - ودرخت شمشادرا

۱ - رك : قی رکش » ت رکش :
آسمان. کر ‎OE‏ بر بندد

"را یز گفته اند ۷ - ولنظی است که ‎Ke‏
‎ee‏ بازی در محل خودکویند4 و ‎OT‏ چنان
است که مهره‌ای ازمهره‌های شطرنج را درجابی
کذارند که در یکی از ‎Steerer Tighe‏
دارد شاء حریف الاح ازآن ‎ale‏ بر خیزد با
‎aS oT oe‏ - ورادن ودور تمودن مر غ‌راییر

"باین لفظ کنند » واين لفظ امراست بردور ‎ed‏

ورفتن ‎em,‏ دور ش
```


## [2026-09-05T17:32:07.007Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor p in d:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m and int(m.group(1))==545:\n        print(p)\nEOF"
}
```


### [2026-09-05T17:32:08.839Z] TOOL RESULT

```
[pdf page 545]
کهیز سلنده
نام قلعه‌ای باشد از ‎EY,‏ میستان ‎٩‏ - وبسنی درختی است ت 5 ‎els,‏ مانند شیطرج ‎BAYT,‏
‏گوند کهیج معرب کهی باشد . دواها بکار پرند .
گهیر ۲ - با الك مجهول بروزن‌صفیر» کهین - ‎«oS NS‏
سیب صحراثیراکونند ‎LT,‏ در خرانان علی | بمعنی کوچکترین_باشد چه که بمعنی کوچك
‎aa‏ است ۵ . -وسیب صحراگیرا نیز گونند که‌بعربی
شیران وبعربی زعرور خوانند . مب من جر >

زعرور وذوئللة حباب خوانند پسیبآنکه ‎Bits‏
‏کهیلا = بالامبروزن ‎sicker» Col‏ ] آن سه پپلو ‎Mattes‏ .
بود ایرای ۴ +

کهیثه ۲ بکراود بر وزن‌نگینه,
گهچله ۴ > بر وزن ‎dee‏ پوست. | بمعنی کهین است که کوچکترین باشد .

بیان بیست وسیم

در ‎GE‏ تازی با ‎GL‏ حطی مشتمل بر یکسد و پنج لفت و کنایت

کی « بفتح اول و سکون ثالی » بمعنی : این لفظ راکویند ۸ -و یمعتی پادشاه پادشاحان
کدام و چه وقت باشد ۸ - ودر وقت انکار نیز | است یعنی پادشاهی که در عصر خود از همة
۱ - جهانگیری کوید : در اين ایام به کهی مشهور است :
‎ts‏ کارام گیرند هیچ سپاهان ما با سپاء کهيچ.
فردوسی طوسی «جهانگیری» -
درتاریخ صیستان ‎(HAST EATON)‏ چنین نامی نيامده. نام قلمه‌ای درسیستانه کوهژ»
آمده که در تاریخ بیهقی چاپ قدیم طهران آنرا « کوحتیز» ودر چاپ کلکنه« کوهشیر» (قلمتی‌از
فلاع غزئین) دوشنه‌الد «تاریخ سیستان‌ص ۲۰۷ ح 4 ) ۰ ولیز نام جایی در سیستان «قوهه»(معرب
کوهه . کهه) آمده (تاریخ سیستان ۳۳۵ ح ۳ ). احتمال میرو که «کهیج» ‏ کوهیج -
کوفیج = کوفج , همان طابفهةٌ معروف ساکن بلوچستان و کرمان باشد ‎Ay)‏ : کوچ . کوفج) ولقة
‎Lam‏ این استاء پسمتي (کوهی, کوهتانی) است . - «کهیر وکهین اسم فارسی زعرور
است» « محیط اعظم‌بنقل فرهنگ نظام» < فهر-ت مخزن‌لادوبه » ۰ رك : کهین .
۴ - رثك : فهرست ولف - و همتی دیگر آن = کهیله ‎(pe)‏
‏۴ - «کهیلا و کهیله اسم هندی سلیخه است ت» «فپرست مخزن الادوبه» .
۵ - از :که (کوچك) ین (دبت) . ‎٩‏ - رگ :کهیر . ۷ - از :که
(کوچك) + ‎(en) a,‏
‎A‏ در اوستا 2008 ( چه وقت ۶ ). حندی باستان 6808 (چه وقت؟؛ ) » اففالی
‎kala‏ , اسی ۷80 ( حرگاه . اگرءآیا) , پلوچی ۷201 (چه وقت؛) «اسشق ۰۰۸۷۸ ‎Pll‏
‏باستان 8018 (چه وقت؟) «بارتولمه ۲۱۱۷ « نیب ر ‎oF‏ ص۱۱۷ کردی ‎Ki‏ ( که ؛کدام ؛ )

۳۵۲ oe UL?
```


## [2026-09-05T17:32:19.235Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== kada ==\"; grep -n \"kaδa\\|kada\" BRT.txt | head -10; echo \"== yeδi ==\"; grep -n \"yeδi\\|yeidi\\|yezi\" BRT.txt | head -10; echo \"== yaδat ==\"; grep -n \"yaδāt\\|yaδat\" BRT.txt | head -5; echo \"== dim ==\"; grep -n \"^dim\\b\\|dim, \" BRT.txt | head -10"
}
```


### [2026-09-05T17:32:19.321Z] TOOL RESULT

```
== kada ==
4218:Sprechenden  nahe  liegt,  adjektivisch,  auch sva,  'dieser  mein,  unser':  °na  bansmana imqm  zao^ram  äyese  yaH'^.2.1;  —  vlspa tarsuca  xhiärata  *vanaiti(?)  °na  masanaca i'atihanaca  .  .  ".  .  "durch  diese  (meine) Grösse  und  .,"  P,42";  —  \iimä  dakyai«^ tyil  adam  adarsty  kada  (sd.)  °«J  pärsä iärJ  D.j.z.  n)  in  schwachdeikti- schem  Sinn  'dieser,  der,  er';  l)  auf  Vor- hergenanntes, -gesagtes  (Wort  oder  Satz) zurückweisend;  i)  auf  ein  Wort,  a)  ad- jektivisch: iwt  hafat  vir^rmt  .  .  aal  °na v>r3>!ra  hacimnS  . .  YL  ig.  54;  54;  — parttum  ayasalsa  .  .  °na  parma  tanüm aizuiji/gisYl.i4.^$;  35,  /7.61';  —  mana zaya  asti  vahistjm{%A.)  ,.*na'  vaca  vanSni ..  'na  saya'V.if).<).  b)  substantivisch: yat  .  .  aoxte  alsa  .  .  kacanuha  ml  *''na^^ apirmäyüka  .  .  a%a  *hä  *xsayäe  *°na*'' Aaxisit  (sd.)  ciiva/  *'na^'>  .  .  faraakacaiti (sd.)  ". .  'geh  mit  ihm,  mein  Kind!' . ." N.;?;  —  aitatca..  uxnanam  luchs-isnum.. astica  -na  avavat  uxoala  (sd.) . .  Y.  ig,  10;
5986:kada  mazda  yöi  uxsand  "snam  . .  /rärmtg
10658:Vgl.  xrü:  ~  I'ü.:  fixrinii'),  erl.:  lin-aiidU, Su.:  kadarthaaarvam.  —  i)  S.  lu  jrrnw-.
10730:ntanauhl  '%r3J  hcUü  paitt.mraot  asä  kuL- haxa  Y.32.  2;  —  mazdä  , .  vokü  uxfya (sd.)  manavAä  °hr3  aiälä  ustä  tanüm Y._jj.  10;  —  yahmi  spfntJ  %wä  mainyU urvafse  jass  mafsds  "ärä  ahmt{s,A.)  voha mananha  Y.43.6;  —  aAmäicä  «ärJ  (als Sah].)  ^^ /asaj  (sA.)  mananha  voha  asaüä Y.3Q.  7;  —  ahmsi  dqn  (sd.)  .  .  mazdä •^rJ  armaitf  ahurS  Y.  47.  i;  —  kj  binx- 'iqm  täil  ''hrJ  mal  ärmaitim  ^..44.1;  — kada  masda  ala  mal  ärmai/i/ /imaj  (sd.) •^ra  Y.48.11;  — yqm  Asi  °'^ra  voAuäi cdiit  (sA)  tnananhi  Y.^o.y,  —  mazdi dadät . .  haurvat3  aminlätasca  . .  asahyica ..  •UraAyä  sarS  (sd.)  Y.^jj.ai.  a)  im YHapt,  mit  va^hav-K^y.as>m..vahist>m ..vohuia  maiid ..  vokucä  '"hrsm  \.3~.i,i.\ —  asäatcä  hacä  varahsuseä  mananhs  vatf- ksusca  'hrai  Y. J5. 10.  a)  im  jAw.,  mit va i rya- Adj. :  '^rtm  vairTm  amihm  sptn- hm  yazamaide  S. 2.  4 ;  Vr.  20.  i;  —  ahurS mazdä  . .  vohu  manö . .  ahm  vahist»m  .  . ''i:r>m  VairTm  .  ,  spmta  ärmaitis  .  .  Y. 57.  24;  1.1  f.,  /tf.  3,  Yt/.  25,  4.  i;  —  ahu- rake  maxdä  .  .  vanh^us  mananhB aiahe ..'"hrahe  vairyeke..  Y.70.2;  —  aku- rai  masdäi  . .  aläi  . .  °^rai  vairyät  armatSe V,  iff.  iii  G.J.  s;  —  vaAu  manauha  haH- mnS  aläca  .  .  '^r3ca  ya  vairya  FrW.  /, I ;  —  viscihnm  dim  ayasata  Syapta  (sd.) ■ira  vairyaY.2Q-^(J\  k)  xlaiirahe  vair- yeht  a)  (nämlich  mS)  heisst  der  6.  Monat im  Jahr:  pancaca  haptaitttn  *pailisJiahyehe (sd.)  '"hrahe  vairyehe  anayranqm  A.  3. 9.  ß>    (nämlich    ayani)    heisst    der  4.
18675:elliptisch  sva,  'ein  Mann  und  ein  Weib,  ein Menschenpaar"**:  dvaübya  haca  n)r>bya dva  nara  us^ayein/e (sd.)  t//i^wa/ia  s/ri^a nairyas^a  V.2.41.  2) '•  praegn. 'wehr- hafter Mann,  Kriegsmann;  kriegerischer Held':  narSi  ßrasaoifträi  Y.  28.  8;  — katna  (sd.)  syävarsänai  zurSjatahe  na- rahe''*  Yt*j.  18;  — pqsnus  narJ  (NS.)'^ HryS  taxmS  Aog.  84;  — y^i  narS  taxma ptntmU  Yt./J  27;  —  t! nard paiti.sanmti ySkva  v3r3%ra.l'aohl!  {sd.)  YtJ_j.  46;  — yat  mS  slärS  .  .  AacÜnte  (sd.)  n?r>byS ä^annff  *bax/3nia  Yt- 8.  1 ;  5.11,  77.6,7; das/a  narqm  *pouru.tät?m  stäkyanqm.. vanatqm  avammnanqm  Ny. J.  10;  —  hva- iai  naire  barumnäi  Y.  65.  4;  — yä  na- qm  vjg3r>pla{sd.yit . .  baoxtär^m  dahäi/i Vr.7,3;  Yt  10.12;  —  ya^a  hazannm Oim  narftn  adar.taySi^  Yt.  8.  $$; I.  19*;  —  a%ra  narqtn  mihrS.drujqtn apq/{sd.)  gavB  dar>tayeiti  Yt70. 48;  — narqm  asätanqm  frasS.car^'hrqm  saosyan- tqm  Y.  24.  5,  Yt.  13. 17.  a)  als  Bezeich- nung für  den  zweiten  Stand  (s.  'piflra-) 'Krieger,  Ritter***:  kada  .  .  mquarfi/ (sd.) rS  vis3nliY.48.  10;  — daidx atturai (AP.)  ,  .  asaunS  .  .  aidyüi  väsliyJng  ,  . ahmaibyä  ahma.rafonarahs  {^d^  Y.40.3; %wqm  ttarakl  ysi  taxma  Jathyintt äsu.aspim  .  .  %wqm  a^ravanS  .  .  mastim Yt5.  86.  3)''  ohne  Betonung  des  Ge- schlechts sva.  Mensch;  Person';  1)  im Gegensatz  zum  Tier;  uzw.  zu  a)  pasav-: ahe  nmanaßie pasvqmca  narqntla  Y.^-S; pasBm  .  .  nanm  ra?syät  V,  13.  32 b)  'span-.  . .  ahe  nmanake  spä  vä na  va  irihyat  V.5, 39;  8. 1,  4;  —  yat ahmi  spänasca  narasca  para.irüinti  V. 6.1; — y!i  pa^a  uebarmte  (^)  spänasca irista  iiarawca  (NF.)"  irisia  V.  Ä  14; 3.  32;  —  yat  ,  .  sairi  riiianie  spänasca irista  naraila  (AP.)'*  irista  V.  3.  8; 36.  c)   ^av-:  janyäi  *n>rSuI^'*  para
19586:Haomai  vTipe  zi  anyg  *°SawAj  aaftwa fiaSnte  .  .  äat  hs  ys  kaomahe  '%6  aiä AacaiU . .  rmjaiü  (sd.)  hasmake  °%3  "denn alle  andern  Rauschtrinke  sind  von  . .  A. begleitet,  aber  er,  der  Rauschtrank  des H.  . ."  Y.  10.  8;  Yt  17.5'.  b)  sonst: dahms  hurqm  (sd.)  ifaraiti  'S?  ^asfya.- paya/ahü  N.  jo;  —  kada  ajSn  mB%r>m ahya  *°äahyä''>  yä  . .  "wann  wirst  du  den Unflat  dieses  Rauschtranks  treffen,  mit dem.."  Y-^i".!©!).  [N.jo:  lies  mi^Ue statt  mähB  ^araiti;  s.  Pü.]
20478:•  g.  m^iaray- 1  'Verkündigung,  Botschaft" des  Propheten:  kada  tnazda  "röÜ  narS vjs^ntl  "wann,  o  M.,  werden  die  Ritter die  Botschaft  verstehen  lernen?"  M.48. 10.
20847:I  et  (eum)  qui  (est)  faciendi  et  dicendi" I  Y.  33. 14;  —  *grSkms . .  atikSus  maraxtärB I  (sd.)  ahya  \yai(a  ^'Grlhmas  . .  et  (ii)  qui (sunt) ..  destructores"  Y.J2. 13; —  ku%ra töi  andrS  (sd.)  .  .  yöi  .  ,  caxrays  "num tibi  (sunt)  fidi  (ü)  qui  . ,"  Y.^4.7;  — kada  .  .  yOi  uxiäiiS  ainqm  .  .  frärmtl "quando  . .  (ii)  qui  (sunt)  tauri  .  ."  Y.  4G. 3;  —  naldä  dahySus  \ydi  iastSrS  drjsvatas "neque  (ii)  qui  (sunt)  . .  imperatores"  Y. 4O.  I ;  —  tat  ..  uitanai  data  . .  ySi  sl gSus  v^nzinl  (sd.)  azyi  ".  .  vitae  (eorum) qui  .  ."  Y.  34.  14;  —  tim  at  yasna- nqm  paurvataia  yazamaidl  ySi  ..  iyeintJ ".  .  imprecationum  .  .  (eorum)  qui  .  ." ^•37-  2;  —  yi  varpsaiil  (sd.)  kyat vasnä  firasöJ^mim  "qui  . .  fecerit  . .  (id) quod  (est)  .  ."  "^.46.  19;  —  hyatcS dar>gSm  dr)gvll.d»byS  rasB  savai'a  alavabyö "et  (id)  quod  (est)  . .  damnum  et  lucra  . ." Y._jo.  11;  —  Aaihyavanitqm  {%A.)  hyat vasna  f?rasS.t}m}m  "verificationem  (eius) quod.."  Y. 50.11;  —  ai  zt  töi  vaxsya .. hyai  aksyä  (NSf.;  sd.)  dngvaiii  wörtlich ",.  von  dem,  was  die  Androhung  ist,,"  Y, 51.  8;  —  hyat  "qsasutä  (sd.)  yä  (NPn.) daiiiiana  (sd.)  fraoxta  "..  (ea)  quae  (sunt) . .  enuntiata"  Y.  48.  1 ;  —  das  Relativ  kon- gruirt  mit  dem  Praedikat:  vldvä  yalclt güzra  (sd.)  singhanhS  (wörtlich)  "kennend auch  (das),  was  die  geheimen  Lehren  (sind)" Y.4<V,3;  —  anais  a  vT.nSnasa  ya  (NSt) iarapsjis{ad.}cä  kjvltäscä  Y._J2.  15;  — *m>ndäiäyai  (sd.)  ya  (NSf)  toi  adisHi Y.44.8;  5,^.13;  —  nipatihw . .  tumas^a ya  armaitiH&d.)  Tiilcä  Y.4g.  10;  —  yS va  mSi  \yh  (NPf)  gasha  dasdi  (Sp. 7 1 S  u.)  *asnatihe  wörtlich  ". .  (das),  was meine  Besitztümer  (sind)  .  ."  Y,  46. 8;  — vtayUta  yä  (NPn.)  mrqi  sädra  drtgvats (wörtlich)  "immer  (wird  sein)  was  die Qualen  (sind)  .  ."   Y.45.  7;  43-5,  49-6;
22631:•  j.  vanar-  n.  —  ?  — :  'nar»  F.  8. Pu.:  nddakada.
22890:—  unsinnlich:  kada  .  .  frannil  V)rsz- ääis  s^nghlil  saosyantam  xratavB  (sd.) Y.4tf.3.
== yeδi ==
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
2477:y^  . .  möi  gas'^iä  dazdl  *amaiiklmit  akyä  \  myazdS  . .  äisy.ll  kl  anhe  ava{  mlid^m  A. maä%rilfrö^StY.46.Z\'—yatäröpaurvö^3.(il.;  — yastal  mihdgm  haiuftt? nöit däitX äire  . .  paitiJiaraiti  ahmäi  atars  ä/rJnat  .  .  kä  tsm  ahyä  *maeHis(sA.)  ar»hatY.44. V.1S.26;  YLIJ.51; — y ahmäi  xlnstö  ba-\  i^.  b)  .\Sn.,  f.  mit  Äaca  sva. 'dadurch': vaili  mi^rä  ahmäi  Jasaiti  avaiäke  YLIO.  yezi  mit  spä  ..  maeyevä  . .  pai'jyäite  ahmat 84;  87,  Y.GS.w*;  — yöi  nsil  ahm  main-  haca  irisyät  "sonst  konnte  der  Hund  in  . . yantä  aiibyö  dair?  (sd)  voka  as  manö  Y.  \  geraten,  dadurch  könnte  er  Schaden  neh- 34-&]  9.  2&  10,  45-ii  — yaisqm  ..  mazdä  \iata"  V,/_j.37;  —  ahmat  haca  /«>nj  (sd) ..  vatghö  vai'ja  alsqm  ..  Yt.i6.%; — ^J  sayiJ/A' Nik.  7;  *2; — yesi  tat  paiti  irisjati syao^anä  yä  vacatihä  yä  yasnJ  .  .  ae^qm  '  aiähal  hala  iyae>n!i7ar3za  (sd.)  .  ,  V./_?. töi..}hmä  pourutimäil  äasl?(sd.}Y.j4-^,''  38-  2)  vorausweisend;  i)  adjektivisch ■ —  yöi  *aite  . .  *gä'kä  nSit  *srävayänti  . .  I  auf  direkte  Rede  oder  Zitat:  vahiütsm  . . assqm  fyaohamm\ia'\  .  .  N, 25;  —  ySt  ..'igänii  ..  vir^zyat  öyä  (ISf.)  «>/f  (sd.):  hvö avatahabdgnti  (sd..)  /ramar?nl>m  (sd.)  ag-  *pt3  asahyä  mazdlY.4y.2;~aya  antar?.- £qm  nöit  aita^qm  ratufris  ..  N.52;  ^j\  uxti  (sd.) :  nöit  nS  mana  (usw.,  Y..^5.z) —  yahmät  kakmäicit  nalmaruim  vätS  ä'^rö  Y.ig.i$.  —  a)  mit  ergänzendem  Relativ: baoiolm  vibaraiti  (sd.)  ahmll  kahmäiHt  aya  aibigara  (LS.  als  Instr.)  aya  aibijary- nalmanqm..\.8.&o.  a)  Die  Beziehung  ta{d.^.)  yä  amfsanqm  sp^ntanqm..:  gave ist  ungenau:  ^yJ  räakaytn  (sd.)  sravaahä  rto5j/(usw.,Y._j5.4)  Vr.J2.i.  a)  substan- vahistät  iyadkanäl  mantärü  aeibyö  mazäi  tivisch  und  adjektivisch  auf  eine  erläuternde akä  (sd)  mraot  "qua  alienant  doc-  oder  ergänzende  nominale  Beifügung:  «7.5- trina  . .,  üs  .  ."  (statt  qui  ..  iis  ,  .)  Y.32.  yacä  i^agtuL  yäsat  ahyi  Virßzin3m..ahyä .. 1 2'*^  Anhang  zu  II  I  1,  2.     a)  An   ahurahya  uruasimai^A.)  mazda  Y.j2.i ;  2S.
2481:asmöjfanvä  namaYt.1.30; — yezi  ts ai^Aelylm  axlöyöi  (sA)  dat^hB  Y.jö.i;   -~  da- avä.ursrao(ia    yat   yasnahela    vaAmaAeca   ^rls  ahmui  .  .  c^arinö  yö  hlf  ,  .  zbayeiti Yt. /J.  24;4i;  —  u^tä  {%d.}  aAmäi  yahmät
2560:drw^  .  .  'tat  nasul"''  pinnäne  yä  .  .  V.  Gen.'*:  °(.a  ..  aitihä  z^mä  V.j.18,  6.7, 10. 1;  —  -tat  bansma  yat  paiti  apim  .  .jiV.S,  16.12.  2)  'dann,  so'  a)  hmier  ytzi: S.joi?).  b)  substantivisch:  'tattlvayö\yezi  anhat  upaStm  va  ..  'ua  ..  altä ..  yat  K  asti  ,  .  Y.2j,5;  — D  "/«*  ty<^^vasträ  fraca  ktrantaytn  .  .  V.7.12;  N. iariam    ava*    risam    ..    D.  (J-S;    —    äat  26.  b)  hinter  _yfl/:  Hat  yat  hr! frä  vayS
2708:•  j.  aevö.däta-  Adj.  (fem.  °t,7-)  'einzig-,  "der  ich.,  (sie),  solang  als  ich  kann  und allcingeschaffen',  vom  Urrind*':  matikahe  vermag,  lehienwill.."V,2(V.4; — atvislaota gaoci^irahe  giuscct  'taya  giuüa  poum.sar)-  ]  aojai  (sd.)  . .  arthaca  yavai  (sd.)  . ,  taväca ouy.i  Yt7.o;  —  gaem  'iaAe  ..  pouru.-'Uitica  V-jO.  11;  4S- 9;  —  ..*smvayöil yezi sarp'-.ahe  tirunö  S.  2.  I2(?).  \iste  {yai)  n5it*i$ieO{%%^hl.)ttSit  asavamm
2735:yö  vaoce  *n)ma<,ka  nqma  Yx.14-  55-  balsaz3m  (sd,)  ..  upöisaym  ..yezi  is»mnö
2766:mit  upa  i)  'etwas  suchen,  wonach suchen',  mit  Akk.:  hat  aitaSsqm  ..  käHt ufaitätl  yavat  (sd.)  ha&r>m  "auf  welche  , Entfernung  .  .  soU  ei  von  ihnen  welche  ] suchen?  .  ."  N.  log;  —  antar»  käisnmcitx *iiat  artya  (sd.J  upaisöit  N. /0(j;  — yö\ aäagiqm  *öim  käcit  *upöisät"^  .  .  N. , lo^f?);  a)  ohne  Objekt:  yezi  nöit  updi- laiii"''.,  "wenn  er  nicht  (danach)  sucht,.."] N.  ;09;  —  yö  *updisöit"^  nt)it  *vinatti  \ "wer  (danach)  sucht,  aber  nicht(s)  findet"  | N.  10g.  2)  'etwas  ausfindig  zu  machen  | suchen  für  — '  (Dat):  ava'ha  hg  baisazam  \ (sd.)  upöisaypn"^  ya'^a  dahmätcst  V. /j. , 35-  3)  'etwas  wünschen':  yöi  ..  aoäilye.-  \ draonaahasca  *k>ntS  däitim  gius  draonS upa.il i mnö  (stall NP.) [avä\  avankabditUi
2769:mit  pairi  1)  'ringsum  absuchen,  auf- lesen': mazdayasna  aitihh  zimß  pairisa- yanta  (Opt.)  . .  varfsqmca  (als  Obj.)  ..yezi nsit  pairiianie  . .  astqmca  7-arpsqm:a  .  . V.  ö.  7f. 's\  z)  'herumsuchen  nach  — , aussuchen,  auslesen':  asstnanqm  xraoldva- nqm  .  .pairlstanqmY.i4.4'i'>;  A.3.5'^; —  uxtiitn  srlr>m  pairisttm  F.^^f'*'; V.J. 42  PüZ,;  —  pairi  daxma  aSlayqn  vi daxma    calsayqn   Y.S.z.  a)    mit    Dat
2877:anrufen';  aoxtö  rattis  aoxtö  sraoiävarjzö ci'iqm  frä^wfrisaiti  (sd.)  "der  (zu  dem Zweck)  angerufene  R.  .."  V.  7.  7 1 ;  5.  26'; —  yezi  .  .  apsrmSyukö  .  .  aoxtö  vä  Ae aoxte  '^wat  pairi.^auAa  "wenn  .  .  das Kind  .,  oder  angerufen  zu  ihm  sagt:  Ich will  dich  begleiten'"  N.  7;  7(?).  *aojaite V.  Ä'.8oPüZ.(?).  .
3143:•  j.  a-x§nüta-  Adj.  'nicht  zufrieden  ge- stellt': yezi  aesö  nn  yö  yaozdai:ryö ..tbistö "tö  paräili  V.  9. 40.
== yaδat ==
== dim ==
5244:dim  v  V.5.1.
22985:PFP.  zum  V.  »J'ar-.  —  M.  varya-  Adj.;  vgl. varya-  Adj.  —  Pü.:  kämak,  fa  iämai,  (zu  2a -  ausier  Y.  J/  -  und  zu  A):  tiansskr.  — I)  NämL  miidim,  s.  Y.  34.  I3.
27553:dim    disyata  (sd.)   yh    apasca    urvaräsca
```


## [2026-09-05T17:32:27.432Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg110.png"
}
```


### [2026-09-05T17:32:27.911Z] TOOL RESULT

```

```


## [2026-09-05T17:32:27.909Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T17:32:36.418Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg110.png')\nprint(im.size)\nim.crop((580,560,1000,690)).resize((1680,520)).save('pg110_zbn.png')\nim.crop((580,1940,1100,2160)).resize((1560,660)).save('pg110_yeth.png')\n\""
}
```


### [2026-09-05T17:32:38.433Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-05T17:32:40.694Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg110_zbn.png"
}
```


### [2026-09-05T17:32:40.714Z] TOOL RESULT

```

```


## [2026-09-05T17:32:51.422Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg110_yeth.png"
}
```


### [2026-09-05T17:32:51.445Z] TOOL RESULT

```

```


## [2026-09-05T17:33:01.156Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(820,828):\n    ls=[x for x in d[i].split('\\n') if x.strip()]\n    nums=re.findall(r'^\\s*(1\\d{3})\\s*$', d[i], re.M)\n    print('leaf',i,'pagenums',nums,'FIRST:',ls[0][:80],'|| LAST:',ls[-1][:80])\nEOF"
}
```


### [2026-09-05T17:33:03.030Z] TOOL RESULT

```
leaf 820 pagenums ['1340'] FIRST: plier,  ‘to  beseech,  en¬ treat’  (fr.  L.  supplicdre;  see  supplicate). Deri || LAST: Derivatives:  surli-Iy,  adv.,  surli-ness ,  n. surmise,  tr.  and
leaf 821 pagenums ['1548', '1549'] FIRST:   intr.  v.  —  ME.  surmisen,  fr.  MF. surmis,  surmise,  masc.  and  fem.  pp || LAST: sustain,  tr.  v.  - —  ME.  susteinen,  fr.  AF.  sustein-, stem  of  OF.  sust
leaf 822 pagenums ['1510', '1551'] FIRST: r, sustenance,  n.  —  ME.,  fr.  OF.  sustenance,  souste- nance  (F.  soutenan || LAST: swart,  adj.,  swarthy  (poetic).  —  ME.  swerte, swarte,  fr.  OE.  sweart,  ‘
leaf 823 pagenums ['1552', '1553'] FIRST: , orig.  ‘of  the  color  of  dirt',  fr.  I.-E.  base  *  sword-, ‘dirty,  dark || LAST: swindler,  n.,  cheat,  sharper.  —  G.  Schwindler, ‘giddy  person;  dreamer,  
leaf 824 pagenums ['1554', '1555'] FIRST:   waste  away,  lan¬ guish,  disappear’,  whicn  is  rel.  to  OE.  swindan, ‘to || LAST: syllable,  n.  —  ME.  sillable,  fr.  MF.  sillabe  (F. syllabe),  fr.  OF.,  f
leaf 825 pagenums ['1556'] FIRST: s  there  referred to.  Cp.  also  monosyllable,  dissyllable,  trisyllable, tet || LAST: Symplocarpus,  n.,  a  
leaf 826 pagenums [] FIRST: genus  of  plants,  the  skunk cabbage  (bot.) —  ModL.,  shortened  from  *Sym- || LAST: syndic,  n.,  the  accredited  agent  or  manager  of  a corporation,  esp.  of 
leaf 827 pagenums [] FIRST: cogn.  with  L.  dicere,  ‘to  show,  tell’.  See diction  and  words  there  re || LAST: syphilous,  adj.,  syphilitic.
```


## [2026-09-05T17:33:09.373Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(855,864):\n    ls=[x for x in d[i].split('\\n') if x.strip()]\n    nums=re.findall(r'^\\s*(1\\d{3})\\s*$', d[i], re.M)\n    print('leaf',i,nums,'FIRST:',ls[0][:60],'|| LAST:',ls[-1][:60])\nEOF\necho \"=== to, prep ===\"; grep -n \"^to,  prep\\|^to,  adv\\|to,  prep\" KLN_1966.txt | head"
}
```


### [2026-09-05T17:33:11.560Z] TOOL RESULT

```
leaf 855 [] FIRST: ,  ‘deceiver’,  fr. OI.  sthagah,  of  s.m.,  fr.  sthagati, || LAST: thysano-,  before  a  vowel  thysan-,  combining  form meani
leaf 856 [] FIRST: and cp.  words  there  referred  to. || LAST: Derivative:  tiff,  intr.  v.,  to  be  angry, tiffany,  n.,
leaf 857 [] FIRST: ze.  —  Obsol.  F.  tiphanie, fr.  Late  L.  theophania,  ‘m || LAST: timbre,  n.,  the  characteristic  quality  of  a  sound, qu
leaf 858 [] FIRST: hrough  the  intermediary || LAST: Tiphia,  n.,  a  genus  of  insects,  the  wasp  ( entomol¬ 
leaf 859 [] FIRST: t,  n.,  a  scarf.  —  ME.  tipet,  dimin.  of  tip,  ‘a poi || LAST: titrate,  tr.  v.,  to  determine  the  strength  of  a chem
leaf 860 [] FIRST: rmine  the strength  of’,  fr.  titre,  ‘title;  right;  fin || LAST: togated,  adj.,  togaed;  dignified.  —  Formed  with 1st  s
leaf 861 [] FIRST: wearing  the  toga’,  fr. toga.  See  toga. || LAST: L.  tomus,  fr.  Gk.  xopo?,  ‘a  
leaf 862 ['1626'] FIRST: cut,  a  piece  cut  off, section,  part  of  a  book,  volu || LAST: toot,  intr.  v.,  
leaf 863 ['1629'] FIRST: to  blow  a  horn.  —  Of  imitative  ori¬ gin;  cp.  Du.  t || LAST: toreutic,  adj.,  pertaining  to  chased  work.  —  Gk. xope
=== to, prep ===
19731:intitule,  tr.  v.,  to  give  a  title  to.  —  OF.  entituler, intituler  (F.  intituler),  fr.  Late  L.  intitulare,  ‘to give  a  name  to’,  fr.  in-,  ‘in’,  and  titulare,  ‘to  give a  title  to,  entitle’,  fr.  L.  titulus,  ‘title’.  See  title and  cp.  entitle,  which  is  a  doublet  of  intitule. into,  prep.  —  ME.,  fr.  OE.  into,  which  is  com¬ pounded  of  in,  ‘in’,  and  to,  ‘to’.  See  in,  prep, and  to.
26318:onslaught,  n.,  onset,  assault.  —  Formed  on  the analogy  of  Du.  aanslag,  ‘an  attempt’  (see  on  and slay  and  cp.  G.  Anschlag,  ‘stroke ;  plot,  design’); influenced  in  form  by  slaughter, onto,  prep.  —  Formed  on  analogy  of  into  fr.  on and  to  (qq.v.)  Cp.  unto.
39384:T.N.T.,  trinitrotoluene.  —  Abbreviation  of  the initials  of  the  elements  of  trinitrotoluene, to,  prep.  —  ME.,  fr.  OE.  to,  rel.  to  OS.,  OFris.  to, Du.  toe,  OHG.  zuo,  zua,  zo,  MHG.  zuo,  G.  zu, ‘to’,  from  the  I.-E.  pronominal  base  *do-,  ‘to, toward,  upwards’,  whence  also  L.  do-  in  donee, ‘as  long  as,  while’,  and  -do  in  quandd,  ‘when’. Cp.  I.-E.  *do  in  OSlav.  do,  ‘as  far  as,  to',  and  in OL.  -do,  -du  (in  endo,  endu,  ‘in').  Cp.  also  I.-E. *de  in  Avestic  -da  (as  in  vaesmen-da,  ‘to  the house’),  Gk.  -Sc  [as  in  olxxSc.  oixrWSc,  ‘to one’s  home,  homeward’,  and  in  ’AtHjvai^s  (for *’AffSvavz8c ),  ‘to  or  toward  Athens’],  and  in L.  -de  (as  in  inde,  ‘thence,  from  there’,  unde, ‘whence,  from  where’).  Cp.  too,  which  is  a doublet  of  to,  and  tattoo,  ‘drumbeat'.  Cp.  also de-,  endo-,  indigene.
39499:tomorrow,  adv.  and  n.  ME.  to  morgen ,  to morwen,  fr.  OE.  to  morgenne  (fr.  to,  ‘to’,  and morgenne,  dat.  of  morgen,  ‘morning,  morrow  ), also  (unflected)  to  morgen.  See  to,  prep.,  and morrow,  morn,  and  cp.  today,  tonight, tompion,  n.  —  A  var.  of  tampion,  tampon. Tompion,  n.,  a  watch  made  by,  or  resembling, that  made  by  Thomas  Tompion  (1639-1713). tomtit,  n.,  the  titmouse.  —  Compounded  of  tom and  tit,  ‘a  small  bird’.  Cp.  titmouse, tom-tom,  n.  —  A  var.  of  tam-tam.
39543:too,  adv.  —  ME.  to,  too,  fr.  OE.  to,  adv.,  iden¬ tical  with  to,  prep.  See  to  and  cp.  G.  zu,  which also  unites  the  meanings  to  and  too.
40827:until,  prep,  and  conj.  —  ME.,  prob.  fr.  unto  (with the  substitution  of  til,  ’till’,  for  to).  Cp.  Dan. indtil  and  Swed.  intill  and  see  unto  and  till, unto,  prep.  —  ME.,  contraction  of  *und  to.  The first  word  means  ‘up  to,  until’,  and  is  rel.  to  OE. dp,  OS.,  ON.,  OFris.,  Goth,  und,  OHG.  unzi, ‘up  to,  until’,  and  to  OE.  end,  ‘end’;  see  end.  For the  etymology  of  the  second  word  see  to.  Cp. prec.  word.
```


## [2026-09-05T17:33:20.526Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(d):\n    if 'to,  prep.  —  ME.,  fr.  OE.  to,  rel.  to  OS.' in p:\n        print('leaf',i)\nEOF"
}
```


### [2026-09-05T17:33:22.458Z] TOOL RESULT

```
leaf 860
```


## [2026-09-05T17:33:42.290Z] TOOL CALL #46: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py"
}
```


### [2026-09-05T17:33:42.324Z] TOOL RESULT

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


## [2026-09-05T17:33:53.324Z] TOOL CALL #47: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D9%86%D8%A8%D9%88%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D7%93%D7%91%D7%95%D7%A8%D7%94\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deh%E2%82%81-\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D9%87%DB%8C%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%CE%B4%CE%B9%CE%AC%CE%B4%CE%B7%CE%BC%CE%B1\" \\\n \"https://www.etymonline.com/word/diadem\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%DB%8C\" \\\n \"https://www.etymonline.com/word/to\" \\\n ; do python3 tools/fetch_source.py \"$u\" --note \"page 110 verification (D.b.r / De 1 / De 2)\"; done"
}
```


### [2026-09-05T17:33:58.821Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d9acf167e2a97dd9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c41ec9c4ce5ac1df.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4ee49e29ff4d36cd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5bfe55a5ce8921a9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/22664546d4c2399f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3c0c859d79aff9b2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9f1c56c359bf99e7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d6937d5cb7398b19.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/77d36874687f4822.txt
```


## [2026-09-05T17:34:01.397Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"########## ZANBUR\"; grep -n -A12 -i \"^Persian\\|^Arabic\\|Etymology\" d9acf167e2a97dd9.txt | head -80"
}
```


### [2026-09-05T17:34:01.452Z] TOOL RESULT

```
########## ZANBUR
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
76- 1.4.2 
77- Derived terms 
--
94: Etymology 
95-
96- 2.3 
97- Noun 
98-
99- 2.3.1 
100- Derived terms 
101-
102- 2.3.2 
103- Descendants 
104-
105- 2.4 
106- Further reading 
--
114: Etymology 
115-
116- 3.2 
117- Pronunciation 
118-
119- 3.3 
120- Noun 
121-
122- 3.3.1 
123- Derived terms 
124-
125- 3.3.2 
126- Descendants 
--
213: Etymology
214- [ edit ] 
215-
216- From Aramaic זבּור ( zibbūr , “ hornet ” ) , doublet of دَبُّور ( dabbūr ) ; cognates with Classical Syriac ܕܒܘܪܐ ( debbōrā ) and Hebrew דְּבוֹרָה ( dvorá ) .
217-
218- Pronunciation
219- [ edit ] 
220-
221- IPA ( key ) : /zun.buːr/ , ( colloquial ) /zan.buːr/ 
222-
223- Noun
224- [ edit ] 
225-
--
430: Etymology
431- [ edit ] 
432-
433- Borrowed from Arabic زُنْبُور ( zunbūr , “ hornet, bee ” ) , from Aramaic זבּור ( zibbūr , “ hornet ” ) .
434-
435- Noun
436- [ edit ] 
437-
438- زنبور • ( zenbur ) ( definite accusative زنبوری ( zenburu ) , plural زنابیر ( zenâbir ) ) 
439-
440- bee , hornet , wasp , any winged insect of the order Hymenoptera except ants 
441- Near-synonyms: آری ( arı ) , اشك آریسی ( eşek arısı ) , یابان آریسی ( yaban arısı ) 
442-
--
475: Etymology
476- [ edit ] 
477-
478- Borrowed from Arabic زَنْبُور ( zanbūr ) . An alternative pronunciation of Modern Standard Arabic زُنْبُور ( zunbūr ) .
479-
480- Pronunciation
481- [ edit ] 
482-
483- ( Classical Persian ) IPA ( key ) : /zan.ˈbuːr/ 
484-
```


## [2026-09-05T17:34:09.327Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"##### DVORA\"; sed -n '150,320p' c41ec9c4ce5ac1df.txt"
}
```


### [2026-09-05T17:34:09.367Z] TOOL RESULT

```
##### DVORA
 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Hebrew
 [ edit ] 

 Root 

 ד־ב־ר ( d-b-r ) 

 12 terms 

 דבורה 
 Etymology
 [ edit ] 

 From Proto-Semitic *dVbr- ( “ bee ” ) . Cognate with Classical Syriac ܕܒܘܪܐ ( debbōrā ) , Amharic ዲቧራ ( dibʷara ) , Arabic دَبُّور ( dabbūr ) , زُنْبُور ( zunbūr ) , Classical Mandaic ࡆࡉࡌࡁࡅࡓࡀ ( zimbura ) , Aramaic דְּבוֹרְתָא , זִיבּוֹרָא .

 Pronunciation
 [ edit ] 

 ( Tiberian ) IPA ( key ) : /dvoːˈrɔː/ [da.voːˈʀɔː] 

 ( Yemenite ) IPA ( key ) : /də.vøˈrɔ/ [dæ.vøːˈrɔː] , [dæ.veːˈrɔː] 

 ( Modern Israeli ) IPA ( key ) : /dvoˈra/ 
 Audio : ( file ) 

 Noun
 [ edit ] 

 דְּבוֹרָה • ( dvorá )  f ( plural indefinite דְּבוֹרִים , singular construct דְּבוֹרַת־ , plural construct דְּבוֹרֵי־ ) [pattern: קְטוֹלָה ] 

 bee 

 Declension
 [ edit ] 

 Declension of דְּבוֹרָה 

 isolated forms

 with possessive pronouns

 Number: 

 State: 
 form

 Person: 
 singular 
 plural

 m 

 f 

 m 

 f 

 singular 
 indefinite

 דְּבוֹרָה 

 first

 דְּבוֹרָתִי 
 דְּבוֹרָתֵנוּ 

 definite

 הַדְּבוֹרָה 

 second

 דְּבוֹרָתְךָ 
 דְּבוֹרָתֵךְ 
 דְּבוֹרַתְכֶם 
 דְּבוֹרַתְכֶן 

 construct

 דְּבוֹרַת־ 

 third

 דְּבוֹרָתוֹ 
 דְּבוֹרָתָהּ 
 דְּבוֹרָתָם 
 דְּבוֹרָתָן 

 plural 
 indefinite

 דְּבוֹרִים 

 first

 דבוריי / דְּבוֹרַי 
 דְּבוֹרֵינוּ 

 definite

 הַדְּבוֹרִים 

 second

 דְּבוֹרֶיךָ 
 דבורייך / דְּבוֹרַיִךְ 
 דְּבוֹרֵיכֶם 
 דְּבוֹרֵיכֶן 

 construct

 דְּבוֹרֵי־ 

 third

 דְּבוֹרָיו 
 דְּבוֹרֶיהָ 
 דְּבוֹרֵיהֶם 
 דְּבוֹרֵיהֶן 

 Derived terms
 [ edit ] 

 דְּבוֹרָנִית ( dvoranít ) 

 Proper noun
 [ edit ] 

 דְּבוֹרָה • ( dvorá )  f 

 a female given name , Dvora , Debora , and Deborah 

 ( biblical ) Deborah ( a judge of Israel ) 

 References
 [ edit ] 

 H1683 in Strong, James ( 1979 ), Strong’s Exhaustive Concordance to the Bible 

 Klein, Ernest ( 1987 ), “ דְּבוֹרָה ”, in A Comprehensive Etymological Dictionary of the Hebrew Language for Readers of English ‎ [1] , Jerusalem: Carta, →ISBN , page 113a 

 Jastrow, Marcus ( 1903 ), A Dictionary of the Targumim, the Talmud Babli and Yerushalmi, and the Midrashic Literature ‎ [2] , London, New York: Luzac & Co., G.P. Putnam's Sons, page 276b 

 “ דבורה ” in the Hebrew Terms Database of the Academy of Hebrew Language

 Further reading
 [ edit ] 

 דבורה on the Hebrew Wikipedia. Wikipedia he 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=דבורה&oldid=89860647 "

 Categories : Hebrew terms belonging to the root ד־ב־ר 
 Hebrew terms inherited from Proto-Semitic 
 Hebrew terms derived from Proto-Semitic 
 Hebrew terms with IPA pronunciation
```


## [2026-09-05T17:34:32.310Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"##### PIE deh1-\"; grep -n -i \"bind\\|Descendants\\|Proto-Ira\\|Sanskrit\\|Ancient Greek\" 4ee49e29ff4d36cd.txt | head -40; echo; echo \"##### dam\"; grep -n -B3 -A10 \"Persian\" 5bfe55a5ce8921a9.txt | sed -n '1,80p'"
}
```


### [2026-09-05T17:34:32.372Z] TOOL RESULT

```
##### PIE deh1-
142: to bind 
157: ⇒ Ancient Greek: ῠ̓πόδημᾰ ( ŭpódēmă ) 
161: Sanskrit: दामन् ( dā́man ) 
163: Proto-Iranian: *dáHma 
172: Ancient Greek: δετός ( detós ) 
176: Sanskrit: दित ( ditá ) 
205: Mallory, J. P. , Adams, D. Q. , editors ( 1997 ), “Bind”, in Encyclopedia of Indo-European Culture , London, Chicago: Fitzroy Dearborn Publishers, page 64 
217: Sanskrit terms with non-redundant manual transliterations 

##### dam
117- Further reading 
118-
119- 4 
120: Persian 
121-
122: Toggle Persian subsection 
123-
124- 4.1 
125- Pronunciation 
126-
127- 4.2 
128- Etymology 1 
129-
130- 4.2.1 
131- Noun 
132-
--
847- Etymology 1
848- [ edit ] 
849-
850: From Persian دام ( dâm , “ snare, trap ” ) .
851-
852- Noun
853- [ edit ] 
854-
855- دام • ( dam ) 
856-
857- net , trap , snare , for catching game 
858- Synonyms: ( net ) آغ ( ağ ) , شبكه ( şebeke ) 
859-
860- ( figuratively ) trap laid for a person 
--
870- Etymology 2
871- [ edit ] 
872-
873: From Persian دام ( dâm , “ livestock, domesticated animals ” ) .
874-
875- Noun
876- [ edit ] 
877-
878- دام • ( dam ) 
879-
880- any wild animal that does not attack or prey on others
881-
882- Etymology 3
883- [ edit ] 
--
900-
901- Redhouse, James W. ( 1890 ), “ دام ”, in A Turkish and English Lexicon ‎ [4] , Constantinople: A. H. Boyajian, page 883 
902-
903: Persian
904- [ edit ] 
905-
906- Dari
907-
908- دام 
909-
910: Iranian Persian
911-
912- Tajik
913-
914- дом 
915-
916- Pronunciation
917- [ edit ] 
918-
919: ( Classical Persian ) IPA ( key ) : /ˈdaːm/ 
920-
921- ( Dari, formal ) IPA ( key ) : [d̪ɑːm] 
922-
923- ( Dari, formal ) IPA ( key ) : [d̪ɑːm] 
924- ( Kabuli ) IPA ( key ) : [d̪ɑːm] 
925-
926- ( Hazaragi ) IPA ( key ) : [d̪ɔːm] 
927-
928- ( Iran, formal ) IPA ( key ) : [d̪ɒːm] 
929-
--
967- Etymology 2
968- [ edit ]
```


## [2026-09-05T17:34:36.378Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '930,1010p' 5bfe55a5ce8921a9.txt; echo \"=== PIE deh1 context ===\"; sed -n '135,185p' 4ee49e29ff4d36cd.txt"
}
```


### [2026-09-05T17:34:36.429Z] TOOL RESULT

```
 ( Tajik, formal ) IPA ( key ) : [d̪ɔm] 

 Rhymes: -aːm 

 Readings

 Classical reading ? 

 dām

 Dari reading ? 

 dām

 Iranian reading ? 

 dâm

 Tajik reading ? 

 dom

 Etymology 1
 [ edit ] 

 From Proto-Indo-Iranian *dáHma (compare Sanskrit दामन् ( dā́man , “ string, cord, rope, fetter ” ) ), from Proto-Indo-European *déh₁-mn̥ , from Proto-Indo-European *deh₁- ( “ to bind ” ) .

 Noun
 [ edit ] 

 دام • ( dâm ) 

 snare , trap 
 Synonym: تله ( tale ) 
 به دام افتادن ― be dâm oftâdan ― to get trapped (literally, “ to fall in a trap ”) 
 به دام انداختن ― be dâm andâxtan ― to trap, ensnare (literally, “ to throw into a trap ”) 

 Etymology 2
 [ edit ] 

 From Middle Persian [script needed] ( dʾm /⁠dām⁠/ , “ tame animal ” ) , ultimately from Proto-Indo-European *demh₂- ( “ to tame, dominate ” ) . Cognates include Albanian dem ( “ bull ” ) , Old Irish dam ( “ ox ” ) and Ancient Greek δάμαλος ( dámalos , “ calf ” ) .

 Noun
 [ edit ] 

 دام • ( dâm ) 

 livestock 

 any domesticated animals and livestock such as sheep, cows, goats, dogs, cats, etc
 Antonym: دَد ( dad , “ wild animals ” ) 

 Derived terms
 [ edit ] 

 دامدار ( dâmdar , “ cowhand, pastoralist ” ) 
 دامداری ( dâmdari , “ pastoralism ” ) 

 References
 [ edit ] 

 MacKenzie, D. N. ( 1971 ), “²dām”, in A concise Pahlavi dictionary , London, New York, Toronto: Oxford University Press, page 24 

 Rastorgujeva, V. S. ; Edelʹman, D. I. ( 2003 ), Etimologičeskij slovarʹ iranskix jazykov [ Etymological Dictionary of Iranian Languages ] (in Russian), volume 2, Moscow: Vostochnaya Literatura, page 322 

 Etymology 3
 [ edit ] 

 Borrowed from French dames .

 Noun
 [ edit ] 

 دام • ( dâm ) 

 draughts , checkers 

 References
 [ edit ] 

 Dehkhoda, Ali-Akbar ( 1931– ), “ دام ”, in Dehkhoda Dictionary Institute , editors, Dehkhoda Dictionary (in Persian), Tehran: University of Tehran Press . 
=== PIE deh1 context ===
 [ edit ] 

 Root
 [ edit ] 

 *deh₁- [ 1 ] [ 2 ] [ 3 ] 

 to bind 
 Synonyms: *bʰendʰ- , *dʰerǵʰ- 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *deh₁- (8 c, 0 e) 

 *d(h₁)-yé-ti ( ye-present ) 

 *déh₁-mn̥ ~ *dh₁-mén-s 
 Proto-Albanian: *dēma [ 4 ] 
 Albanian: duo , dua , dúaj 

 Proto-Hellenic: *dḗmə 
 ⇒ Ancient Greek: ῠ̓πόδημᾰ ( ŭpódēmă ) 

 Proto-Indo-Iranian: *dáHma 
 Proto-Indo-Aryan: *dáHma 
 Sanskrit: दामन् ( dā́man ) 

 Proto-Iranian: *dáHma 
 Persian: دام ( dâm ) 

 *doh₁-lo-s 
 > ? Proto-Albanian: *dōla [ 5 ] 
 Albanian: dell ( see a different proposal of the etymology at the entry ) 

 *dh₁-tó-s 
 Proto-Hellenic: *detós 
 Ancient Greek: δετός ( detós ) 

 Proto-Indo-Iranian: *dHtás 
 Proto-Indo-Aryan: *dHtás 
 Sanskrit: दित ( ditá ) 

 See also
 [ edit ] 

 *dʰeh₁- ( “ to do, put, place ” ) 
 *dʰeh₁(y)- ( “ to suckle, nurse ” ) 
 *h₂enǵʰ- 
 *h₂ep- 
 *stembʰ-
```


## [2026-09-05T17:34:43.523Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### DEYHIM\"; grep -n -i -B4 -A14 \"Etymology\" 22664546d4c2399f.txt | sed -n '1,80p'"
}
```


### [2026-09-05T17:34:43.573Z] TOOL RESULT

```
#### DEYHIM
58-
59- Toggle Persian subsection 
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
71- Related terms 
72-
73- 1.3.2 
74- References 
75-
76- Toggle the table of contents 
--
136-
137- Persian
138- [ edit ] 
139-
140: Etymology
141- [ edit ] 
142-
143- From Middle Persian 𐭣𐭩𐭣𐭩𐭬𐭩 ( dīyēm, dīdēm , “ diadem ” ) from Parthian 𐭃𐭉𐭃𐭉𐭌 ( dīδēm, dīdēm , “ half-crown, flower-crown ” ) . Ultimately from Ancient Greek διάδημα ( diádēma ) .
144-
145- Pronunciation
146- [ edit ] 
147-
148- ( Classical Persian ) IPA ( key ) : /daj.ˈhiːm/ 
149-
150- ( Dari, formal ) IPA ( key ) : [d̪äj.hiːm] 
151-
152- ( Dari, formal ) IPA ( key ) : [d̪äj.hiːm] 
153- ( Kabuli ) IPA ( key ) : [d̪ä.jiːm] 
154-
```


## [2026-09-05T17:34:48.139Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### diadema GK\"; grep -n -A8 \"Etymology\" 3c0c859d79aff9b2.txt | head -30; echo; echo \"#### etymonline diadem\"; grep -n -i \"diadem\" 9f1c56c359bf99e7.txt | head -20"
}
```


### [2026-09-05T17:34:48.195Z] TOOL RESULT

```
#### diadema GK
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
153: Etymology
154- [ edit ] 
155-
156- From διαδέω ( diadéō , “ to bind round ” ) +‎ -μα ( -ma , result noun suffix ) .
157-
158- Pronunciation
159- [ edit ] 
160-
161- IPA ( key ) : /di.á.dɛː.ma/ → /ðiˈa.ði.ma/ → /ðiˈa.ði.ma/ 

#### etymonline diadem
1:URL: https://www.etymonline.com/word/diadem
4:TITLE: Diadem - Etymology, Origin & Meaning
6:Diadem - Etymology, Origin & Meaning 
21: Origin and history of diadem 
23: diadem (n.) 
25: c. 1300, diademe , "aureole of a martyr or confessor;" mid-14c., "a crown, anything worn on the head as a mark of royalty," from Old French diademe and directly from Latin diadema "cloth band worn around the head as a sign of royalty," from Greek diad ē ma "the headband worn by Persian kings and adopted by Alexander the Great and his successors," from diadein "to bind across," from dia "across" or "through" (see dia- ) + dein "to bind," which is related to desmos "band," from PIE root *dē- "to bind." Related: Diademed .
28: Entries linking to diadem 
44: Persian taj is literally "crown, diadem, ornamental headdress," but here denoting an object of distinguished excellence....
78: Share diadem 
82: https://www.etymonline.com/word/diadem Copy 
85: <a href="https://www.etymonline.com/word/diadem">Etymology of diadem by etymonline</a> Copy 
88: Harper, D. (n.d.). Etymology of diadem. Online Etymology Dictionary. Retrieved September 5, 2026, from https://www.etymonline.com/word/diadem Copy 
91: Harper Douglas, "Etymology of diadem," Online Etymology Dictionary, accessed September 5, 2026, https://www.etymonline.com/word/diadem. Copy 
94: Harper, Douglas. "Etymology of diadem." Online Etymology Dictionary, https://www.etymonline.com/word/diadem. Accessed 5 September, 2026. Copy 
97: D. Harper. "Etymology of diadem." Online Etymology Dictionary. https://www.etymonline.com/word/diadem (accessed September 5, 2026). Copy 
104: Dictionary entries near diadem 
110: diadem
```


## [2026-09-05T17:34:54.762Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### key\"; grep -n -A10 \"^ Etymology\" d6937d5cb7398b19.txt | head -60; echo; echo \"#### etymonline to\"; sed -n '20,40p' 77d36874687f4822.txt"
}
```


### [2026-09-05T17:34:54.823Z] TOOL RESULT

```
#### key
62: Etymology 1 
63-
64- 1.1.1 
65- Noun 
66-
67- 1.1.1.1 
68- Further reading 
69-
70- 1.2 
71: Etymology 2 
72-
73- 1.2.1 
74- Adverb 
75-
76- 1.3 
77: Etymology 3 
78-
79- 1.3.1 
80- Noun 
81-
82- 1.3.2 
83- Further reading 
84-
85- 1.4 
86: Etymology 4 
87-
88- 1.4.1 
89- Contraction 
90-
91- 1.4.2 
92- Further reading 
93-
94- 2 
95- Middle Mongol 
96-
--
100: Etymology 
101-
102- 2.2 
103- Noun 
104-
105- 2.3 
106- References 
107-
108- 3 
109- Pahari-Potwari 
110-
--
125: Etymology 1 
126-
127- 4.1.1 
128- Pronunciation 
129-
130- 4.1.2 
131- Adverb 
132-
133- 4.2 
134: Etymology 2 
135-
136- 4.2.1 

#### etymonline to
 Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.

 About
 Who Did This 
 Sources 
 Introduction 
 Links 

 Support
 Premium 
 Patreon 
 Donate with PayPal 
 Merch 

 Apps

Get Chrome Extension 

Get iOS App 

Get Android App
```


## [2026-09-05T17:34:58.147Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### key Persian section\"; awk '/^ Persian$/,0' d6937d5cb7398b19.txt | head -80; echo \"==========\"; echo \"#### etymonline to entry\"; grep -n -i \"to (prep\\|Old English to\\|PIE root \\*de-\\|do-\" 77d36874687f4822.txt | head -10"
}
```


### [2026-09-05T17:34:59.808Z] TOOL RESULT

```
#### key Persian section
 Persian
 [ edit ] 

 Etymology 1
 [ edit ] 

 From Middle Persian [Book Pahlavi needed] ( AYMT /⁠kay⁠/ ) 𐫐𐫏𐫏 ( kyy /⁠kay⁠/ ) , 𐫐𐫏 ( ky /⁠kay⁠/ ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈkaj/ 

 ( Dari, formal ) IPA ( key ) : [kʰäj] 

 ( Dari, formal ) IPA ( key ) : [kʰäj] 
 ( Kabuli ) IPA ( key ) : [kʰäj] 

 ( Hazaragi ) IPA ( key ) : [kʰäj] 

 ( Iran, formal ) IPA ( key ) : [kʰʲej] 

 ( Tajik, formal ) IPA ( key ) : [kʰäj] 

 Rhymes: -aj 

 Readings

 Classical reading ? 

 kay

 Dari reading ? 

 kay

 Iranian reading ? 

 key

 Tajik reading ? 

 kay

 Adverb
 [ edit ] 

 Dari

 کی 

 Iranian Persian

 Tajik

 кай 

 کی • ( kay  / key ) 

 ( interrogative ) when ?
 کَی خَو می‌رِی؟ ― kay xaw mē-rī? ― when are you going to sleep? ( Dari , informal ) 

 Etymology 2
 [ edit ] 

 From Middle Persian 𐫐𐫏 ( ky /⁠kē⁠/ ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈkiː/ 

 ( Dari, formal ) IPA ( key ) : [kʰíː] 

 ( Dari, formal ) IPA ( key ) : [kʰíː] 
 ( Kabuli ) IPA ( key ) : [kʰíː] 

 ( Hazaragi ) IPA ( key ) : [kʰí] 

 ( Iran, formal ) IPA ( key ) : [kʰʲíː] 
==========
#### etymonline to entry
56: to (prep.) 
58: Old English to , ta , te , "in the direction of, as far as (a place, state, goal)," opposite of from ; also "for the purpose of, furthermore;" from West Germanic *to (source also of Old Saxon and Old Frisian to , Dutch toe , Old High German zuo , German zu "to"). Not found in Scandinavian, where the equivalent of till (prep.) is used.
60: This is reconstructed to be from PIE pronominal base *do- "to, toward, upward" (source also of Latin donec "as long as," Old Church Slavonic do "as far as, to," Greek suffix -d ē "to, toward," Old Irish do , Lithuanian da- ), from demonstrative *de-. Also see too .
114: Old English into "into, to, against, in," originally in to. It emerged in late Old English to do the work of the dative case inflections, then fading, that formerly distinguished, for instance, the notion of "in the house" from that of "into the house." Compare onto, unto. To be 
118: 1680s, "signal calling soldiers or sailors to quarters at night," earlier tap-to (1640s), from Dutch taptoe, from tap "faucet of a cask" (see tap (n.1)) + toe "shut, to" (from Proto-Germanic *to; see to (prep.)). "So called because police formerly visited taverns in the evening t
122: Old English todæge, to dæge "on (this) day," from to "at, on" (see to) + dæge, dative of dæg "day" (see day). Meaning "in modern times" is from c. 1300. As a noun from 1530s. Generally written as two words until 16c., after which it usually was written to-day until early 20c. Sim
```


## [2026-09-05T17:35:12.376Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFA (Fraenkel) zunbur/dabbur ===\"; grep -n -i \"zunbûr\\|zunbur\\|dabbûr\\|dabbur\\|Biene\" AFA.txt | head -10\necho; echo \"=== AFM Addi Shir زنبور ===\"; grep -n \"زنبور\" AFM.txt | head -5\necho; echo \"=== PLA Asbaghi zanbur ===\"; grep -n -i \"zunbur\\|zanbur\\|زنبور\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -5\necho; echo \"=== FVQ Jeffery ===\"; grep -n -i \"zunbur\\|dabbur\" FVQ.txt | head -5\necho; echo \"=== LKT ===\"; grep -n -i \"zunbur\\|dabbur\\|diadem\" LKT.txt | head -5"
}
```


### [2026-09-05T17:35:12.485Z] TOOL RESULT

```
=== AFA (Fraenkel) zunbur/dabbur ===
4633:Hier füge ich noch den Namen des Bienenstockes ein,
4640:nicht gerade besonders viel Bienenzucht getrieben worden
4645:Aramäischen gekommen zu sein. ^^ »Bienenkorb** scheint

=== AFM Addi Shir زنبور ===

=== PLA Asbaghi zanbur ===
11027:zufäna 146 zanburak 
11072:Zur) - zanburk: "ein Teil der Uhr" aus dem pers. ER zamburak 8, 
11164:—»,) -— zanburak = zamburak q. v. 

=== FVQ Jeffery ===

=== LKT ===
```


## [2026-09-05T17:35:14.506Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4625,4665p' AFA.txt"
}
```


### [2026-09-05T17:35:14.546Z] TOOL RESULT

```
würdiger Weise keinen Beleg , Tgl. aber Gen. 24 , 25 ; Exod.
5,7 u. a. m.
Sehr fraglich ist mir auch die Echtheit Ton oJ; »Stroh'*
hauptsachlich deshalb , weil die Araber über die Schreibung
und Ableitung des Wortes selbst nicht im Klaren sind.
Daneben &i% äi^ u. a. Dergleichen pflegt am Ehesten bei125
Woltern fremden Ursprungs vorzukommen. Aber mit nS^
kann ich es nicht zusammenbringen.
Hier füge ich noch den Namen des Bienenstockes ein,
g 1^, woneben H^IIT Torkommi Es kann keinem Zweifel
unterliegen, dass dies Wort erst aus aram. HHIO syr. l^äd
PSm. 1713 und Sindban ed. Baethgen, p. 9,7 a. f. (auch
li^&s) übernommen ist. Die Entlehnung ersieht man aus
dem Mangel einer Ableitung und der yerschiedenen Yoca-
lisationsmoglichkeit. Auch kann im eigentlichen Arabien
nicht gerade besonders viel Bienenzucht getrieben worden
sein. Aber auch die aramäischen Worter sind fremden Ur-
sprungs. Sie sind entlehnt aus pers. JjT %t^>Korb*', Vul-
lers II. 90, 3, daneben auch s^f %5^ u- &• Schreibungen. In das
Arabische scheint das Wort erst durch Yermittelung des
Aramäischen gekommen zu sein. ^^ »Bienenkorb** scheint
eine spatere arabisierende an die Wurzel To »drehen*' an-
gelehnte Umbildung zu sein.
ACKERBAU UND PFLANZENREICH.
Es ist eine eigen thümliche Thatsache , dass zwei der äl-
testen und verbreitesten arabischen Eigennamen s^Xi^ und
j^ den Pflüger und Ackerbauer bedeuten; der erste zu
s^yu^ der andere zur Wurzel ^^^ »das Land bebauen, cul-
tiyieren" gehörig. So müssen also auch die Araber in
einer Urperiode im weiten Strecken am Wüstenrande
Ackerbau getrieben haben. In der Zeit aber, wo sie als
Araber in der Geschichte auftreten, sind sie nur noch No-
maden und kennen den Ackerbau fast gar nicht. Ammia-
nus sagt XIY ,4,3 Ton ihnen : nee qnisquam stiram ap-126
prehendit vel arborem colit, sed erraut semper per <>patia.
Für eincQ grossen Tbeil von Arabien war ja allerdings die
Boilencuitur unmüglicli , aber auch wo mau Ackerbau trei-
ben konnte , lag der Boden brach : sü ttxtx Vi myx^"'' ''P*-
iriix; TÜv Aaän d^iiperipuv evTuv Agatharciiidea (Müller)
135. Denn der Araber hielt den Ackerbau für eine eines
freien Mannes nicht würdige Arbeit '). Man Tgl. die cha-
```


## [2026-09-05T17:35:20.568Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON zanbur ===\"; grep -n -m4 \"زنبور\" MON_part1.txt | head -6; echo \"---\"; grep -n -B2 -A4 \"^زنبور\" MON_part1.txt | head -30"
}
```


### [2026-09-05T17:35:20.643Z] TOOL RESULT

```
=== MON zanbur ===
3606:از مرغ. سنگگ» موش زنبور» مار و غیره؛ 
3611:مرع؛» سگٌ» موش» زنبور» مار و غبره؛ 
15672:خبیص خشک که زنبور عسل آرد و آن نه 
18300:انگ: وه (.) زنبور» زنبور عسل. 
---
55178-
55179-خان: 20 (.) خانه» سرا. کاروانسرا. لانة 
55180:زنبور» کندو. شیار داخل لولةً تفنگ. 
55181-خان؛ 0 زتر.] (ا.) عنوانی که به شاه با 
55182-امپری در ترکستان و سپس در نواحی دیگر 
55183-دادند. عنوانرجال و فتر کات: احمدخان» 
55184-محمد‌خان. ضح.- در فرون اخیر از اهمست 
--
63214-دند نه: (ه-)مممفحمل [ع. . دندنه ] (مص‌ل.) با 
63215-خود سخن نرم گفتن. (.) صدای مکس و 
63216:زنبور. سخن آهسته و زير لبی که فهمیده 
63217-
63218-
63219-‌ ۰ 
63220-
--
71668-دیوئی» قرمساقی» قوادی. 
71669-
71670:زنبور: 220057 [ع.] (.) (جان.) حشره‌ای 
71671-بال نازک است و قطعات دهانیش بیشتر 
71672-لسنده است. تغیبر شکل این حشره کامل 
71673-تشکیلات منظم می‌زیند و در سوراخ‌ها و 
71674-است. زنبور دارای سوزن زهرالودی است 
--
71680-درشت‌تر می‌باشند. از لحاظ زندکی و طرز 
71681-تغذیه هر دو نوع یکسانند ولی از کلمة 
71682:زنبور بیشتر مراد رنسور زرد رنگگ است)؟ 
71683-
71684-
71685-۷
```


## [2026-09-05T17:35:25.667Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD dām ===\"; grep -n \"dām\\b\\|dʾm\" PHD.txt | head -12; echo; echo \"=== PHD didem ===\"; grep -n -i \"didem\\|dydym\\|dīdēm\" PHD.txt | head -6; echo; echo \"=== PHD kay ===\"; grep -n \"^kay\\|kay '\" PHD.txt | head -8"
}
```


### [2026-09-05T17:35:25.743Z] TOOL RESULT

```
=== PHD dām ===
308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
396:hannàm [%7m | = M] = handām. Harborz [Albwic | N Alburz] the mountain range surrounding the world. harg [hlg | cf. M bie, Аг. xarj, xaraj] duty, tribute; work, effort. *harrób- [hlwp- | M hrwb-] collect, gather. —išn(ih): collection, gathering. har(w) [KRA < A АР; hl | M been, N har] all, each, every. harwin [%/wyx! | M hrwyn] pl. al. harwisp [Ahlwsp! | M hrwsp] all. ~in [-yn'] pl. all. harzag [hick! | N harza] loose, free. has®r [Ps] = Av. háóra-] a measure of time (unequal hour, ze of day- light); a measure of length (— frasang, or 1 frasang, 1 mile). haspin [hspyn! | = M] rest, repose. hast, ~ih [AY T!, -yh] = tast, ~ih. hašāģird [kP klt! | M APgyrd, N šāgtrd] disciple, pupil. hast [h#! | = M, N ~] eight. ~ad [80 | N ~] eighty. ~dah [лаһ | N ~, higdah] eighteen. lhàwan [h?wn! | N +] a mortar. *hawan [/?zn! = Av. háwani-] the morning gdh. hāwand [/?wnd | M ÞPw(y)nd] like, similar. ^h: likeness, similarity. hāwišt [h’wst'] disciple, pupil. ~ih: disciplehood. haxt [h()At'] thigh, haunch, hip. hāxtan, hàz- [/7htn', h'e-] lead, guide, persuade, convert. ~išn: persuasion, conversion. hazār [1,000, hel | M h?r, N ~] thousand. ~ag LEI | N ~a] millennium. hazzān [?/h2’n'] tomb, ossuary. hên [Ayn! | M hyyn] army. ~ih: attack, aggression. hérbed [%y/pt! | N hérbud] teacher-priest. ~ih: priestly office. hērbedestān [hylptst’n'] priestly school. ~ih: priestly studies. hérig [hylyk' | N h/xéri] iris, wallflower. hézag [Ayck! | (M hyjg), N лег] pail. hil-, —išn, v. histan. hindüg [Andwk! | M hyndwg, N hindi] Indian. ~ап [-°п!] India. hištan, hil-, (P hirz-) [S BKWN-tn! < A У #9; (hlc-) | M hyštn, hyl-, (P Ayrz-), N —] let, leave, abandon, pardon, set, appoint. ~išn: pardon, loosing. hixr [hyhl] excrement. hixtan, hanj- [Ayhtn', hne- | P hxt] draw (water).
422:kabk [АрА! | N ~] partridge. ~-anjir [acyl | N ~] a kind of francolin. kabód [kpwt! | N ~] grey-blue; pigeon. kabótar [kpwil | M kbwtr, N ~] pigeon. kāč [с | N kāš(ki)], ~ ka: would that, if only. кадар [01А] game, joke. кадар [ktk' | M kdg, N kada] house. ~-banig [-b'mwk! | N Radbanü] mistress, lady of the house. ~ig [-yk'] domestic; servant. ~-xwaday [-hwty | P gdyxwd?y, N kadxudā] householder, master of the house. kadām [ktm | M kd?m, N кийат) which, what. c--iz-é(w) [-c-H D] whichever. kadar [kt] who, which. 7-iz-é(w) [-c-H D] whoever. kaf [kp | N —] foam, slime. kaf-, v. kaftan. kafč [kpc | N ~] ladle, skimmer. ~ag [-А! | N ~a] spoon. kafš, ~ag [kps, -k! | N Аар] shoe. ~gar [-k/ | N ~] shoemaker. kaftan, kaf- [kp-in' | P kft, kf-] fall. kah [TBNA < A tbr | N ~] chaff, straw. kān-, ~i§n, v, kāstan. _ kahas [kts | М khs] channel, sewer. kāhēnīdan, káhén- [R'hyn-ytn!] decrease, lessen (tr.). kühidan [P hytn! | N ~] = kastan. kahist [ksst'] least. kah-rubāy [Ара | N —rubá] amber. kahwan [khwbn' | M qhwn, N kukan] old. kākom [RP Rkwm | N ~] stoat. ~ i spéd: ermine. kālbod [Аро | (M k*/byd), N ~] body, shape, form. ~ӧтапа [-wmnd] corporeal. kam [km | M kmb, N ~] little, small, few; v. kem. kam [Em | = M, N ~j will, desire, purpose. kàm-, v. kāmistan. 1катаб [k?mk! | N kama] kinds of gruel, or soup. ?kümag [k?*mk! | N kama] = kam. «-hanjām [-hnc’m] gaining one’s end, successful. -~-hanjamih: success. „ūmand [-wmnd] willing(ly), desirous. ~-widar [-wt?l | N kām-gučār] successful, independent. ~-xwaday [-Awt^y] independent, absolute. kamal [kml | (M km?7)] head (daevic). ~ig [-yR!] chief (daevic).
603:wābar [w’Al | M wbr, (N bāwar)] truth; belief. wābarīģān [w?/yk?n' | M wbryg’n) true, trustworthy. “Аһ: trustworthiness. wabz [wpc, wpz] wasp. wačast [wcst! = Av. vwacas-tasti-] strophe (of the Gathas). watéag [wck!, (bck!) | N bacca] child, baby, cub. wad [SL Y.ÀA < A sry’; wt! | M wd, N bad] bad, evil. ^ Áh : badness, evil. маа [w?t! | M wd, N bad] wind, breath, spirit; cal. 22nd day. wadag [wtk'] evil, vile, wicked. ~ih: evil, vileness. wādām [w’t?m | N bádám] almond. wādbān [w°tp’n' | N bādbān] sail.
770:almond wādām; — sweetmeat lawz- énag.
2634:limb handām, (hannām), pēšag.
2776:member handām, (hannām), pēšag.
4306:which čē, kadam, kadār, ke. whichever kadām-iz-ē(w). whip aštar, tāzānag. whirlwind wād-girdag. white spēd, arus; (n.) spēdag. who kē, kadār.
5550:dāmādīh
5551:dāmād

=== PHD didem ===

=== PHD kay ===
```


## [2026-09-05T17:35:33.609Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \"kay [^]]*\\][^.]*\\.\" PHD.txt | head -8; echo \"---- NYB\"; grep -n -o \"kaδ[^ ]*\\|kad ['\\\"]*when\\|kay[^a-z][^.]\\{0,60\\}\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-05T17:35:35.550Z] TOOL RESULT

```
426:kay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian.
---- NYB
1149:kay- ‘to choose, to select’; cf Skr cinoti 1
1727:kay; MPrth wyg’h, abstr
1731:kay-em
2157:kay < kad; NP kai
2161:kayān [kd’n'] 2727, zuarrah i —-ān, ~-dn xLarrah, v
4131:kay-; MPrth wjyd (pt
4345:kayän u äturän šah 12%; kayān ~ u han 4 herpat — 554; yazdan ~ i
5222:kay-: citan kohrp-: karp keresaspa-: Krišāsp kū (kuda): kū kutak
```


## [2026-09-05T17:35:43.510Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,io\np='incoming/WLD/WLD_Bd1_pages.txt'\nd=open(p,encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(d))\nfor i,pg in enumerate(d):\n    if re.search(r'δ[ηι]μα|διάδημα|diadema', pg) or ('dāman' in pg and 'binden' in pg):\n        print('hit leaf',i)\nEOF"
}
```


### [2026-09-05T17:35:45.097Z] TOOL RESULT

```
leaves 895
```


## [2026-09-05T17:35:49.370Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\n# find leaf whose text contains printed page marker 771\nfor i,pg in enumerate(d):\n    m=re.search(r'\\[pdf page (\\d+)\\]',pg)\n    tag=m.group(1) if m else '?'\n    if re.search(r'\\b77[01]\\b', pg[:200]) or 'binden' in pg and 'daman' in pg.lower():\n        print(i,tag,pg[:200].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-05T17:35:51.305Z] TOOL RESULT

```
778 ? 770                                                                   de-,         do- |  |  | bildung von -ds nach Doppelformen wie jiqooOe Jigooda), auch in de-vgo                                         
779 ?                                                    de-   :   da- (dei-)                            771 |  | dat „de" entw. Abl. f. *dad alsUmbildung eines Instr. *da, oder aus einem |                       
840 ? 532                                                          dhau-   — dheig- |  | -daman-         2. Zsglied „Absieht“; daeman- n. „Auge, Augapfel; Blick“, |                           als | doidra- n     „Au
```


## [2026-09-05T17:35:53.876Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(d[779][:2600])\nEOF"
}
```


### [2026-09-05T17:35:55.603Z] TOOL RESULT

```
                                                   de-   :   da- (dei-)                            771

dat „de" entw. Abl. f. *dad alsUmbildung eines Instr. *da, oder aus einem
                                              lat. per, als Praefix in dad id
solchen weitergebildetes *dcl-ti vgl. osk. per-t
                                               ,


„dediderit", dadikated „dedicavit", umbr. daetom „demptum", s. iiber diese
und die friiher genannten o.-u.-Formen bes. v. Planta II 465 ff. m. Lit.);
dazu Komp. lat. deterior „minder gut, schlechter", Sup. deterrinius daman                      ,

(altlat. aueh dennis) „eben, nun, erst („*zu unterst“  „zuletzt, endlich“,
                                                                 ‘
                                                                                   —
                                                                                   -




Lit. bei Yf.LEWb. 2 s. y.), denique „und nun gar, und dann, endlich";

     air.       dJ (daneben de aus idg. de, womit vielleicht gall. fiyarov-de „e judicio"
gleichzusetzen ist, siehe Thurneysen Hdb. 190, 459), acymr. di, ncymr. y,
corn. bret. di„von              —
                       herab, von                        —
                                     \v eg", auch als Privativpartikel (z. B.

acymr. di-auc „segnem", wie lat. clebilis steigernd air. dT-mor „sehr groB"
                                                                     ;


wie lat. demagis).
   Die Bed. „von           —
                     herab, von                —
                                   weg" dieser mit gr. dy, de formell gleichen
Partikel  ist wohl erst eine gemeinsame Neuerung der Kelten und Italiker;

auch der Germanen? (Holthausen KZ. 47, 308 ahd. sadal „Armut, Not,         ;



Mangel" von *de „von                  —
                             "’eg", wie ivadal ,,arm“ lat. re?).     Got. imtc ;           —
„bis, weil" ist *und pe (oder te zu to"! Trautmann GGA. 191 1, 251 m. Lit.).

   Zu unserem Stamme gehort auch der Ausgang folgender Adverbial-
gruppen: ai. tada „dann“, av. tada „dann", lit. tada „dann", ai. kada „wann?“,
av. kada, jav. kada „wann?‘‘, lit. kada „wann“, ar. yada ,,wann, als", av.
yada jav. yada „wann", aksl. jeda ,,wann“ (vgl. auch ai. yadi „wenn‘‘, ap.
        ,


yadiy av. yedi, yeidi „zur Zeit als" und av. yabat, ,.woher"), ai. id a ,,jetzt",
            ,


und die slav. Bildungen wie russ. kuda „wohin", aksl. kqdn, kqdc „woher“,
nikida-ze „nunquam“, poln. dokqd ,,wohin“, aksl. tade „von dort", sqdu
.,von hier" u. dgl. (s. Berneker
```


## [2026-09-05T17:36:07.826Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nt=d[780]\nprint(t[:2800])\nEOF"
}
```


### [2026-09-05T17:36:09.666Z] TOOL RESULT

```
            ;                             :                                ;          ;                 ;




772                                               dei-, deia-



  Altere Lit. bei Curtius 5 234.               — Lat. reditnio „umbinde, umwinde, be-
kranze, umgebe", redimiculum                  „Stirnband“            ist       nicbt mit xgy-deyvov auf
eine erw. \Yzf. *dem- zu beziehen (Froehde BB. 17, 306 f.), sondern zu                                ai.

ydmati (s. Wz. *-iem-) „halt, halt zusammen" zu stellen (Niedermann IA.
19, 34 m. Lit.).


dei-, deia-       (:   deid -, di- uud dia -) „hell glanzen, schimmern, scheinen".
   Ai. dt-de-ti „scheint, leuchtet", 3. pi. duly at i, impf. 3. sg. adidet , imper.
2. sg. didlhi , su-di-ti-h „schonen Glanz habend", kaus. dipayati „entziindet,
erhellt", dfpyate „flammt,  strahlt, scheint", didi- „scheinend“ (auf Grand
von dt-de-ti); ahnliches *doi-d-o (gebroehene Redupl.) in anord. teitr „heiter,
                             <;
froh“, ags. tartan „liebkosen , tat- (in                        Namen) „froh“, ahd. zeiz ,,zart, an-
mutig“     (vgl. heiter       sowohl „klar“ als ,,froh“; Uhlenbeck Ai. Wb. 126); viel-
leicht hierher         auch    lit.   didis ,.gro£i“ als „ansehnlich“
   gr. hom. Seazo „videbatur“, ded/irjv ibo'AimQov , ed6£a£ov Hes., arkad.
                                                               '




Konj. deazoi (s. Schulze KZ. 27, 422 Anm., Brugmann II 2 3, 151, 540),
hom. dor. Soaooazo „erschien“, Konj. doaooezai (wegen der o-Stufe nach
Brugmann Grdr. II 1 902, Brugmann-Thumb GrGr. 4 324 denominativen Ur-
sprungs)
   hom. deeAob „sichtbar“ (*<5£t£L>s; mit metr. Dehnung evdelelog), drjlog
ds. (aus ^dialog, woraus auch Hesychs dialog; s. zuletzt Bechtel Lexil. 98),
hom. agi^ylog „sehr deutlich, klar“ (wohl aus *dialog, s. Prellwitz 2 52
Bechtel Lex. 61 nimmt *dirj-log an <Se(t)£-Ao? = zgy-zog zege-zgov); eine
                                                       :                                   :




schwachste Ablautform *di-lo-s sucht Charpentier KZ. 47, 183 (aber auch
nicht iiberzeugend) in Sev-dilla> ,.blicke hiu und her, werfe die Augen
wohin“ (s. Boisacq 176, 1106; devdillco nicht zu mhd. zwinzen „zwinkern",
Pick BB. 12, 162, da dieses als *zwinlczen, *twinlcatjan zu mhd. zivinken);
*do(lo- vermutlich in ags. sweo-tol (aus *tal) „offenbar, deutlich, klar“ (Holt-
hausen IP. 20, 321; andere Deutungen, so die Yerh. mit sueid- ,. glanzen"
verzeichnet Falk-Torp u. svide ) und in ir. doel „Kafer“ („glanzend schwarzes
Insekt")        sowie im      ir.   FluBnamen Daol  (*doila) als „die glanzende" (Po-
korny KZ. 47, 167 f.).              Hierher wohl auch lit. dailiis usw. Ygl. ohen S. 764.
   Ion. diCrjjut „suche, strebe" bleibt fern (s. Boisacq s. v. und u. grjzsco
m.
```


## [2026-09-05T17:36:20.152Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(d[779][2600:6000])\nEOF"
}
```


### [2026-09-05T17:36:21.986Z] TOOL RESULT

```
 674 f., 431, v. d. Osten-Sacken IF. 33, 249).

     Ein verwandter             St.   *di in       den       enklit. iran. Akk. av. ap. dim „ihn, sie",
av. dit „es",          dis pi. m. f., (Bartliolomae 684) und apr. Akk. sg.
                                          dl pi. n.
din, dien .,ihn, sie" (usw.,    Trautmann Apr. 321).
                                          s.

     Vgl. Curtius 5 233, Johansson BB. 15,312, Persson IF. 2, 218 f.. Brug-
mann II 2 2, 81          1 f.




de-    ;    da- (dei-) „binden".
                         sam -) „bindet‘ {dy- Tiefstufe von *dei-, vgl. av.
     Ai. dy-dti (mit a-, ni-,
ni-dyd-tqm 3. sg. med. in pass. Bed. „es soli Einhalt getan werden", -a-
Erweiterung von der Tiefstufe di-, Bartholomae Airan. \Vb. 761), ai. ptc.
dit a-„gebunden" (= gr. derog), daman- n. „Band“ (= gr. -dypa), ni-datar-
,   Binder";gr. deco (*d&-io) „binde“, derog ,,gebunden“, dery „zusammen-
gebundene Spane als „Fackel“ {de- fur idg. *dd- wie derog tidy pi), apaX-              :




X,o-deryg „Garbenbinder“, dsoig „das Binden, Bindung", deapog „Band“,
y.gy-de-pvov „Kopfbinde“; aol. Praes. didyui „binde“ ist nach Solmsen
IvZ. 39, 211 f. zu dyaco nach xii)r\pi dyaco „neugebildet“; vn o-dypa (= ai.
                                                             :




daman-) „Sandale", diadypa „umgeschlungenes Band, Turban, Diadem"
(y.Qy-depvov ist trotz -dypa nicht aus *dypv-ov durch Langdiphthongkurzung
herzuleiten)
     alb.        duai „Garbe“ (iiber *clon- aus idg. de-n-, G. Meyer Alb. Wb. 76),
del „(*Band;,           Sehne, Flechse, Ader" (idg. do-lo-, Jokl SBYlenerAk. 16S.
I.   13).
      Waldc, Etymologisches Wotterl'Uch. I.
```


## [2026-09-05T17:36:31.674Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC dēmn/daman ==\"; grep -n \"dēmn\\|dēmen\\|daman- \\|dāman\" IEC.txt | head -8; echo; echo \"== SYN bind ==\"; grep -n \"διάδημα\\|δέω\\|dāman\" SYN.txt | head -6; echo \"== LEW diadema ==\"; grep -n -i \"diadema\" LEW_1910.txt LAT.txt | head -6; echo \"== SKT diadem ==\"; grep -n -i \"diadem\" SKT.txt | head -5"
}
```


### [2026-09-05T17:36:31.759Z] TOOL RESULT

```
== IEC dēmn/daman ==
2784:dhémn- “setting, fixture, form, shape, sub- stance’. WP I, 828. Cf. dheio (2) *dhemen-, *dhemn- in Gk. thé- ma, cf. also thémis: Myc. temi- “Justice? and Hes. thémeros “firm, stationary'; Lat. femen, gs -inis & femur, gs femoris & feminoris (*thigh': Cz. dymé, gs demene ‘groin’, beside Lat. femin-àlia *drawers"); Ir. damhna 'substan- ce; cause’; W defn ‘substance, material’ beside defnydd, pl. iau (elemen? fr. *dhemniio-); MHG tinne (‘forehead’; pl. ‘temples’); Swiss Tenn ‘main room in hut’; G Tenne ‘threshing- floor’; *dhemn-, *dhēmō(n) in Skt. dhàman ‘fixed abode, reaim, place, common-law, rule, pleasure’; Av. dama, obl. daman- ‘creature’; Gk. théma ‘tomb’, themón ‘heap’; Li. démé “mark, note’; demuó, eps “item, theme, com- ponent, datum’. Cf. further dhomn-. (Av. dax- məm ‘repository for bones’ seems to represent a type *dhesmom. Cf. dhesno-. For Ir. deimh- in ‘certainty’ see above: dhémen-)

== SYN bind ==
== LEW diadema ==
LAT.txt:25301:rete, diadema, coronas aureas, ruscea f facile f, arsinea, galbeos,
== SKT diadem ==
```


## [2026-09-05T17:36:37.908Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC dei bind ==\"; grep -n \"‘to bind’\\|'to bind'\\|“to bind”\\|to bind’\" IEC.txt | head -12; echo; echo \"== SYN BIND ==\"; grep -n \"9\\.16 *BIND\\|BIND$\\|^BIND\" SYN.txt | head -5"
}
```


### [2026-09-05T17:36:39.546Z] TOOL RESULT

```
== IEC dei bind ==

== SYN BIND ==
13764:{SCELLANEOUS PHYSICAL ACTS, ETC. 545 M - (perf) stigybate Pol. fatdowaé, deriv. of fatda ‘a fold’, al sina ep. of root in | loanword fr. MHG valde (NHG falte) ‘a ip hyban, : ’. Berneker 278 oh. 24 fold’. Berneke : (one ‘pend’ OL perc 7. Skt. verb for ‘fold’? The root puf- We. savilt, opd. of skladyoat’, cpds. (beside puta- ‘fold, pocket’, cf. above, 4) ob. skladalt, Bie together’, and | is not quotable in this sense. The adj. jg. = Ch a ane klast’ ‘put, | dvi-guna- ‘twofold’ occurs with vdsas- Bob Hasti ‘ley , ‘clothing’ in sense of ‘folded’. 3 (12.12): place’ ( 9.16 BIND (vb. trans.) Goth. (ga)bindan Lith. ribli . bw ON binda Lett. —siet, rist cs jw Piste Dan. _ binde ChSl. sivezati, povrésti Tat, _vineire, ligdre, ne Sw.  binda SCr.  (s)vezati it, —_‘legaré OE _bindan, tigan Boh. vazati lier ME ___ binde, tye Pol.  wiazaé gp. _ligar, atar NE bind, tie Russ. sujazat! Rum, lego Snictin Du. binden Skt. bandh-, sa-, nah-, da- In le : OHG bale Av. _ band-, ha(y)-, daraz- : ‘sci MHG _binden NEG inden Br. eren, slaga
```


## [2026-09-05T17:36:42.704Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13765,13775p' SYN.txt | head -20"
}
```


### [2026-09-05T17:36:42.749Z] TOOL RESULT

```
A great variety of roots show the no- tion ‘bind’ either in verbs or in nouns for ‘bond, chain, rope, knot’, ete. But only one of these is common to the most usual yerbs for ‘bind’ in more than one of the main branches, namely, to those of Gmc. and Indo-Iranian.
1, IE *bhendh-. Feist 93,
Goth., OE bindan, etce., with Goth. bandi, ete, ‘bond’, both vb. and sb. gen- eral Gme.; Skt. bandh-, Av. band- with o Skt. bandha-, bandhana-, Av. banda-; : : same toot in Grk. retoua (*mevOona) eet Lat. offendizx, offendimen- only a rf and’ (of the priest’s cap, ae, al term), Ir. buinne ‘band’,
2: 1 hats tes? ut Bou), NG Str, with dyati, sil ‘Skt. da-, di- bind (8sg. ‘bond, aa oy Samdana-, daman- Pim, TE *deQ)-, *do-. Walde- 3, Lat, vines: (> It. vincolo ee With aaa ‘bond’? rob. nasal-
Walde-P. 2.152.
oS) oF vinculo),
ized form of IE *wezk-, *weig-, in Sw. vika ‘fold’, etc. (9.15), extension of *we7- in Lat. vzére ‘plait’, Lith. vytz ‘wind’, etc. Walde-P. 1.233 ff.
Lat. ligdre (> It. legare, Fr. lier, Sp. ligar, Rum. lega) with derivs. ligamen (> It. legame), ligdtitira (> Rum. legd- turd), ete. : Alb. lidh ‘bind’, ON Ik, Du. [ijk ‘leech-line’, etc. Walde-P. 2.400. Ernout-M. 549 f. Walde-H. 1.800.
Lat. nectere, perh., reformed after plectere, fr. IE *ned- or *nedh- in Skt. nah-, Ir. nascim ‘bind’, Lat. nodus ‘knot’, etc. (below, 4). Walde-P. 2.328. Ernout-M. 662 f.
Sp. atar, fr. Lat. aptdare ‘fit, adapt, ap- ply’ (hence in Sp. ‘tie to, fasten, bind’), deriv. of aptus ‘fitted, adapted’, pple. of the rare apere ‘bind’ (cf. apisci ‘seize, at- tain’) : Skt. dp- ‘reach, attain’. Walde- P. 1.46. Ernout-M. 60f. Walde-H. 1.57.
4. Ir. con-rigim, W. rhwymo, Br. eren (*en-rig-), with sbs. Ir. cuimrech, W. rhwym, Br. ere ‘bond’: Lat. corrigia
```


## [2026-09-05T17:36:56.384Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kaSa\\|ka5a\\|kaba\\b\" BRT.txt | head -6; echo \"--- yeSi/yebi ---\"; grep -n \"ye5i\\|yeSi\\|yebi\\|yeidi\" BRT.txt | head -6; echo \"--- 684 ---\"; python3 - <<'EOF'\nd=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(d))\nfor i in range(348,362):\n    print(i, d[i][:120].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-05T17:36:58.146Z] TOOL RESULT

```
9249:vouru.kaSaya  "an  den  wogenden  Ufern . ,"  ttuyjl  vayqm  'sam  V.J.  20.
19630:—  insbcs.  des  Leibes,  Taille':  ha  ht  'iim nyasata  Yt.  5.  137;  —  paitis  he  -oyäi bajyamns  Vd.  iS;  12  {'yehe).  A)  Adv,; a)  AS.  'tim  'in  derMitte  von  —  ",  mitten  in— ' (Gen.)*':  garBit y5  hUtaite  °\im  trayatths vouru.kaSahe  Yt6'.3a;  J2.17,  *Y.42,4'\ Yt5. 42.  b)  DS.  'lyai  'um  die  Mitte von-' (Gen.)*':  "lyäl  amqmea  xlafnam^a avattkabdaita  (sd.)    V.  4.  45.  c)  LS.
28800:•  j.  'haosravah-  m.  Name  einer  Bucht des  VourukaSa*^:  aSa  hau  apayzärS  bvai srayanhö  vouru.kafahe  vairis'yS  'vä  nqma Yt.  15.  56;  —  vairim  'varthsm  S.a.  9;  — vardis  'vanhahe'^  Ny.5.  5.
--- yeSi/yebi ---
25616:•  ].,  g.  urvad-a-  Adj.  'amicus,  befreundet; Freund':  ntpaydis  mallm  '"him yavamiti .. aurva^äj  parö  du^malnyaot  mi  t?m  'htm fräyavaydis  sna%ai  .  .  Yt./.  34;  —  ÄvS. alava  zara>:uitrJ  •'inm  %rätärfm  isöit  1 (Sp.  28f,)  alavamm  te  aiaonat  afyeSiyai\ (sd.)  mraomi  '%>m  ''^■3^  Y.  77.  13;  — /r-ä\ n  vTsai  '"hB  staota  •'iigm  staotärim  van-  ■ AarfApfn(Sp.  1405*1.)  ..aax/a  aAurS  mazda^ ya\a  ..  V.10.9;  —  *dr3gubyS  vastär>m\ änasli  ya^a  'htm  spitamäi  \.  ig.  14; ¥.g; —  '%S  *brätä  *pt3  vü  Y.45.11;  — kvS  il  .  .  ahäm.bis  (sd)  '%5  Y.  44.  2 ; 30.6.  a)  mit  Dat.":  ki  "äff  spitamäi zard^uitrai  nä  matdä  "welcher  Mann ist  Freund  dem  SpZ.,  o  M.T  Y.jr.  11; 4ß.  14;  —  maida  dadäi  ahurS  . .  yS  A^i mainyri  iyao'ianäisca  'i^ö  ".  .  dem  . .,  der im  Geist  und  in  Werken  ihm  Freund  ist"  Y. 31. 2 1  '>.  b)  mit  Gen, :  »ä  J  bavahi  yasata- nqm  ydha  .,Az.4;—a.  noch  Y._J7. 3 1 ,  bei  a.
--- 684 ---
leaves 1041
348 —  /,läl  msi  sqs  tvSm  .  ,  Y.46.1^;  — täiit  ..ya  nSil  vä  anhat  (Sp.  271  u.)  .  . Y.j/.  5;  —  tsmUit  uzt
349  2.  3)  sva. | 'nicht  einmal,  ne  —  quidem' ;  a)  die  Negation folgt:  yat  nil  kasvikqmcina  yaahuyanqm (sd.)  ava
350 e  Richterbrücke,  bei  der  die  Scheidung der  Guten  and  Bösen  erfolgt.  Sie  echt  nach mp.  Büchern  vom  Nocdfus
351 Herrscher  sollen (über  uns)  herrschen  —  nicht  sollen schlechte  Herrscher  über  uns  herrschen  - | dby  Google | 599
352 ',  S'*^;  —  'vat  antan "vantö  *<iae  qsavö  auhin  N.  loS;   *iurius  .  .  frSsnaaiti  V,  5.  27,  zu   b) : | itif
353 (doch | vgL  voNBEAnicE  ZDMG.  vo.  355).   —    ')  So | Fl;  NA.  •frülS. | •  j.  Jaxävah-  Adj.  -?-:  °va  F.  15. | Ansch
354     Et.?  —    »>  Das  «rsle  «  ist  mit  dem  Zeichen i      Xu.  33  der  Schrifllafet   in  GlrPh.  i.  i6i  ge- I 
355   Wort  beeinllusst  ist.  —  0  An  den entsprechenden  Stellen  des  Mi,  steht  freilich beidemale  intüi,  2.  125, 
356 n'':  %risum  aSaZsqm  axtinqm  'nayd dnnjaili  V.  7.  59  Gl.  (?). | got.  qens.  —  Vgl.  janay-,  —  Pü. :  srisülak 
357 m  V.  'gay-,  —  VgL  garva- nay:  —  ai.  Jirä-  Adj.  'rasch,  lebhaft',  afy. £i>  'lebhaft',   np.  lö-aJk  'schlau
358 diä  (sd.)  yH  masyä  oHstä  dants 'axhntl  daivB^tustä    Y.  32.  4.  b)   im | jAw.'*:  i)  'darum,  deshalb':  nSil  
359 �i  jassit..  Y.46.8;  —  vaMstH sravsscä  fyao%aftacä  vao^ä,  tä  (APn.)  tu  . . Y.J4-1S;  —  a%a  hat  voAa,  tat  S
360 ahmäi  ..  ya;%a  ta aishaihim  .  .;  ta  (APn.)  Aa'hra  /ra/rä-'(]S.)upauha(at\t.i5.^t; — iviqm  iainitiS vaySmi;  ti
361 .'':  Aat  tat  dqma  .  ..-  vlsp^m  patti uiärtAftn  .  .  Aasavra/a  patti.jasaiti  "was ist  das  flir  ein  Geschöp
```


## [2026-09-05T17:37:05.383Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AVG dim ==\"; grep -n \"dim\\b\" AVG.txt | head -8; echo \"== AVG kada ==\"; grep -n \"kada\\|ka\\^da\" AVG.txt | head -6"
}
```


### [2026-09-05T17:37:05.441Z] TOOL RESULT

```
== AVG dim ==
235:bdidistam  dim
531:'all' ;  Av.  mildtm  and  mildim  'reward'.— A v.  dura-  written  for  dura-  'far' ; Av.  drujo  and  drujo  'of  the  Druj' ;   Av.  yutyta-  and  yu^ta-  'yoked'.
537:Note.  Likewise  i  arising  from  reduction  of  ya,  §  63  is  lengthened ; but  the  u,  arising  from  reduction  of  va,  appears  mostly  short  before  m: — Av.  ma'dim  'middle'  (ace.)  =  Skt.  mddhyam ;  but  often  Av.  pri$um  beside Prijum  (from  *pri$-va-m)  'third'.
732:Orig.  dya,  dva  =  Av.  di,  du  —  before  m,  n. Av.  dasa.gdim  'space  of  ten  steps'  =  Skt.  °gdyam; Av.  avdin  'they  came  down'  =  Skt.  avdyan;  Av.  nasdum 'corpse'  (i.  e.  nasdvam).
762:rd'tt  'with  offering'  =  Skt.  raff;  GAv.  a'&t  (YAv.  a*wi) 'unto,  to'  =  Skt.  abhi;  YAv.  maldim  'middle*  (ace.  sg.) =  Skt.  mddhyam;  —  Av.  ba^rye^te  'they  are  brought'  = Skt.  bhriyante;  Av.  nivoiryeite  'is  confined'  (yvar-); Av.  niurwdydt  'should  How'  (y~rud-}.  —  Av.  a'ryo 'Aryan'  =  Skt.  aryds;  Av.  n&ryqm  'manly'  (ace.  fern.) =  Skt.  ndrydm;  Av.  ma'nyus  'Spirit'  =  Skt.  manyus.  — With  vanishing  of  the  y  which  caused  the  epenthesis, gen.  sg.  fern,  of  aem  'this'  =  Skt.  dsyds.
1168:§   183.     Av.  &/  =  Skt.  ^//,  or  </.     See  Brugmann,   Grundriss  §  591. Av.  mildim  I|ito8dv'  =  Skt.  unchain;  Av.  mtr'^diktm  'mercy'  (if from  y/«<zr/-,  cf.  §  179)  =  Skt.  mfilikam.    Here  again  GAv.  asriildum Ys.  32.3  (§  1 79)=  Skt.  asrd<}hvam.
2243:i— H.  MASC.  NEUT.  Sg.  Nom.  afro;  Ace.  oyum  (§  63  Note  2), or  (abbreviated  spelling)  dim,  aoim;  Insir.aeva;  Gen.  alvahe ;  Loc. afvakmi  (§  443). — Hi.  FEM.  Sg.  Nom.  alva;  Ace.  afvqm;  Gen. atvavha  (§§  443,  134).
2379:Sg.  Ace.  dim  m.  f. ;  dif  n.  —  PL  Ace.  dil  m.  f . ;  di  n.  Ys.  65.8.
== AVG kada ==
4226:Suffix  GYAv.  -<U,  -<&  =  Skt.  -da,  -dha,  -dha,  Av.  yadtt,  yada 'when'  =  Skt  yadd;  Av.  kada,  kada  'when?'  =  SkL  kada.  So  Av. ada  'then'  =  Skt.  ddha,  adha.
```


## [2026-09-05T17:37:22.060Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON dām ==\"; grep -n -m6 \"^دام:\" MON_part1.txt; grep -n -A4 \"^دام:\" MON_part1.txt | head -20; echo; echo \"== BQT v2 زنبور ==\"; python3 - <<'EOF'\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(d):\n    if 'زنبور' in p:\n        print('leaf',i,'~p',i+543)\nEOF"
}
```


### [2026-09-05T17:37:24.361Z] TOOL RESULT

```
== MON dām ==
59261:دام: 130 (مخلوق) ( ۰ جانور وحشی غیر 
59272:دام: 00 (هند.] (ا.) سکه‌ای مسین در 
59261:دام: 130 (مخلوق) ( ۰ جانور وحشی غیر 
59262-درنده؛ عموماً و آهو و گوزن خصوصا مق. 
59263-دد. جانور اهلی؛ مانند: گاو» گوسفند» اسب 
59264-استر» شتر. 
59265-
--
59272:دام: 00 (هند.] (ا.) سکه‌ای مسین در 
59273-هندوستان که نخستین بار در زمان شیر شاه و 
59274-جانشینانش از سلسلةٌ سوری ضرب شد. بنابه 
59275-قول ابوالفضل بن مبارکك ۲۹۰ دام یکث 
59276-مهر و ۴۰ دام یکث روپیه بود. 

== BQT v2 زنبور ==
leaf 181 ~p 724
leaf 211 ~p 754
leaf 293 ~p 836
leaf 344 ~p 887
leaf 346 ~p 889
leaf 356 ~p 899
leaf 496 ~p 1039
```


## [2026-09-05T17:37:27.517Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '59266,59272p' MON_part1.txt; echo \"----- MON dām trap? search دام (تله)\"; grep -n \"دام\" MON_part1.txt | sed -n '1,3p'; grep -n -B1 -A6 \"دام:\" MON_part1.txt | sed -n '1,40p'"
}
```


### [2026-09-05T17:37:27.628Z] TOOL RESULT

```
دام سل (ا.) آلتی که جانوران را به فرب 
گر فتار سازد؛ بند» تله. آلتی که بدان ماهبان 
را صبد کننده تور ماهیگیری» شست. (تص.) 
زخارف دنیوی و آنچه که سبب بازماندگی 
از مدآ باشد. 

دام: 00 (هند.] (ا.) سکه‌ای مسین در 
----- MON dām trap? search دام (تله)
861:رسیدن» سهو ده نهر اقدام چاه بل آب از 
899:[ دوس دامن میت بو ون اس 
947:می‌شو د که هو ده به کاری اقدام کند و زیان 
1031-برند و به فشار آب در آن کنند؛ آب‌دزدکک. 
1032:آب‌اندام: 2.0 (ص‌مر. آمر.) آنکه 
1033-دارای پبیکری زیبا است. خوش شکل؛ 
1034-خوش قد و قامت. 
1035-
1036-ابانگان: 2027-00 (امر.) جشنی در ایران 
1037-باستان که در روز آبان (دهم) از ماه آبان بر پا 
1038-می‌داشتند. 
--
9767-(نج.) از پس یکدیگر بر آمدن ستارگان. 
9768:اردام: او [ع.] (مص‌ل.) هميشه بودن» 
9769-ساکن و پا بر جا بودن. (مص عم.) رام ساختن» 
9770-خا کر یزی کردن. 
9771-
9772-اردب: (270۸«)0 [معر.] پیمانه‌ای است برایر 
9773-بیست و چهار «صاع, و آن شصت و چهار 
9774-من باشد. 
--
11566-استخبارات. 
11567:استخدام: صقل »اوه [ع. 8 (سص م.) به 
11568-خد مت پذیرفتن؛ به چاکری گرفتن» به 
11569-خدمت گماشتن؛ کسی را برای خدمت 
11570-خواستن. (امص.) به خدمت گماشتگی؛ ج. 
11571:اسستخداسات. ادارة استخدام: ادارة 
11572-کارگزینی. ادارهٌ عمومی: به خدمت گماشتن 
11573-بطور رسمی و دایم و ثابت در یکی از امور 
11574-عمومی دایمی دولتی. 
11575-استخر: 6 ([ - - استرخ + استلخ - ستخر ] 
11576-(.) آبگیری بزرگ که آب بسیار در آن 
11577-آیده آنگین تالاب. استخر شنا: (ور.) 
--
14422-کسی يا چیزی نسبت دهد. 
14423:اعدام: 2420 [ع.] ( ج. عدم؟ نست‌ها؛ 
14424-نستی‌هاء نابودی‌ها» نابودها. 
14425:اعدام: 0 ([ع.] (سصم.) درو ش 
14426-کردن» تهیدست کردن. (امص.) بسی چیزی» 
14427-تهیدستی. (مص‌م.) نیست گردانیدن» نیست 
14428-کردن» کشتن. 
14429-اعدل: ا26 [ع.] ص تسفض.) دادگر تر) 
14430-شایسته‌تر برای شهادت دادن. راست‌تر»
```


## [2026-09-05T17:37:39.619Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nt=d[496]\ni=t.find('زنبور')\nprint(t[:200])\nprint('...')\nprint(t[max(0,i-800):i+900])\nEOF"
}
```


### [2026-09-05T17:37:41.380Z] TOOL RESULT

```
      ‫و‬                                                                                                       ‫زلبری‬

 ‫صنبر زنبوراست‪ -‬وتوپ‬           ‫ز بورگ‬
‫کوچك را گیوزبند ‪ -‬و نوعی از اسلح
...
      ‫و‬                                                                                                       ‫زلبری‬

 ‫صنبر زنبوراست‪ -‬وتوپ‬           ‫ز بورگ‬
‫کوچك را گیوزبند ‪ -‬و نوعی از اسلحه باشد‬                     ‫طوعام کنند ولخدوربعربی‌البرباریس خواند ‪۱‬‬
                          ‫سرآن بفابت تبز ® ‪.‬‬              ‫‪-‬نابه ازدبوث‬
                                                                     ‫و نام یکی ازآلات‌جنکه است ک‬
‫ر نبو ره = بروزن طنبوره ل‪.‬وعی ازساز‬                      ‫ور عردمی باشد که در محافل و مجالس قابل دقع‬

‫باشد که بتر اهل هند نوازند » و آن چوبی‬                    ‫کردن باشند ‪ -‬و شاهد بازار را نگیوزیند وم‬
‫بود که برد وسرآن دو کدو نصب کرده باشند و‬                 ‫رایر باد‬       ‫خود‬   ‫دهان‬   ‫باشد که کسی‬   ‫آن‬       ‫الت‬   ‫اول و‬



 ‫دو تار بر آن بته نوازند و آنرا کنگری یز‬                 ‫کند و دیگری بنوعی دست (‪ )۱‬بر آن زلدکه‬
‫کوبند یکسر کاف ‪ -‬وزنبور سیاه بز رکک راهم‬
‫میگوبند‪ -‬و نوعی از پیکان تیر واسلحة جنگه‬                   ‫ثریری = بابای اب
```


## [2026-09-05T17:37:48.595Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WEB Deborah ==\"; grep -n -o \"Deborah[^.]\\{0,160\\}\" WEB_vol1.txt | head -4; echo \"== FSD Deborah ==\"; grep -n -o \"Deborah[^.]\\{0,160\\}\" FSD_vol1.txt | head -4; echo \"== FSD diadem ==\"; grep -n -o \"diadem, n[^.]\\{0,200\\}\" FSD_vol1.txt | head -3; echo \"== RCH zanbur ==\"; grep -n -o \"zanbúr[^.]\\{0,100\\}\\|zunbúr[^.]\\{0,100\\}\" RCH.txt | head -5"
}
```


### [2026-09-05T17:37:50.430Z] TOOL RESULT

```
== WEB Deborah ==
== FSD Deborah ==
87392:Deborah
== FSD diadem ==
== RCH zanbur ==
```


## [2026-09-05T17:37:53.932Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '87388,87398p' FSD_vol1.txt; echo \"=== SKT/KLN diadem 1971 ===\"; grep -n -o \"diadem[^.]\\{0,200\\}\" KLN_1971.txt | head -3; echo \"=== WEB diadem ===\"; grep -n -o \"di.adem[^.]\\{0,200\\}\" WEB_vol1.txt | head -3"
}
```


### [2026-09-05T17:37:55.710Z] TOOL RESULT

```
scope  and  Pannmlnt  mountains, de-au'rate,  1   dl-e'ret;  2   d6-a'rat,  a.  1.  Entom.  Of  the color  of  gold.  2f.  Gilded;  golden.  [<LL .   deauratus,  _ pp.  of  deauro,  gild,  <   L.  de,  down,  aurum,  gold.]  —   de-bauched%  / 1   di-betfht';  2   de-b(\cht',  pa.  1.  Corrupted; de-an'ratet,  n.  To  gild.—  de"au-ra't!ont,  n.  de-baucht*,  /despoiled  of  virtue  or  purity.  2.  Per-
deave,  1   dlv;  2   d£v,  v.  [Scot.  &   Prov.  Eng.]  1. 1.  To  deafen  taining  to  or  characterized  by  debauchery  or  excess;  as or  bewilder  with  noise.  II.  i.  To  become  deal.  debauched  habits.—  dc-bauch'ed-Jy,  adv.—  de-baueh'ed-
dcave'Iy,  l   dlv'li;  2   dev'ly,  a.  [Prov.  Eng.l  Solitary;  lonely,  ness,  n.
dc"a-war'rent.  vt.  To  break  up  (a  warren).  deb"au-chee',  1   deb’o-^hi';  2   d&b'o-fhe',  n.  One  ha*
Deb.,  n   Diminutive  of  Deborah.  *   bitually  profligate,  drunken,  or  lewd;  a   dissipated  per
deb.,  abbr.  Debenture.  _   _   son;  libertine.
dc-bac'Ic,  1   dl-bak'l  or  dl-ba'kl;  2   de-bilc'l  or  de-bii'cl,  Debauchees,  dissolute,  heartless,  fickle,  cowardly,  havo  been **  1.  The  breaking  up  of  ico  m   a   river  by  a   flood.  2.  over  Hinco  the  world  began.
Thackeray  Four  Georoes,  George  IY.  p.  109.  [e.  a   l.  1891.1 [<  F.  dibauchi,  pp.of  dibaucher ;   see  debauch,  r.]
One  who
Death’s-head  Moth.
Geol.  A   violent  flood  of  waters  that  carries  off  great
=== SKT/KLN diadem 1971 ===
14043:diadem
21802:diadem and cp
57146:diadem
=== WEB diadem ===
```


## [2026-09-05T17:38:06.636Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg110.png')\nim.crop((1330,1890,1970,2140)).resize((1920,750)).save('pg110_empty.png')\n\""
}
```


### [2026-09-05T17:38:08.500Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T17:38:10.925Z] TOOL CALL #77: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg110_empty.png"
}
```


### [2026-09-05T17:38:10.943Z] TOOL RESULT

```

```


## [2026-09-05T17:39:10.194Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && tail -9 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d['url'])\""
}
```


### [2026-09-05T17:39:11.771Z] TOOL RESULT

```
https://www.etymonline.com/word/discuss
https://abadis.ir/fatofa/%D8%AF%DB%8C%DA%A9%D8%AA%D9%87/
https://abadis.ir/fatofa/%D8%AF%DB%8C%D8%B3%DA%A9/
https://abadis.ir/fatofa/%D8%AF%DB%8C%DA%A9%D8%AA%D8%A7%D8%AA%D9%88%D8%B1/
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dyew-
https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A8%D8%A7
https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D9%88
https://www.etymonline.com/word/journal
https://abadis.ir/fatofa/%DA%98%D9%88%D8%B1%D9%86%D8%A7%D9%84/
```


## [2026-09-05T17:39:14.571Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -c . index.jsonl; python3 -c \"\nimport json\nfor l in open('index.jsonl'):\n    d=json.loads(l)\n    if 'page 110' in d.get('note',''): print(d['url'])\""
}
```


### [2026-09-05T17:39:16.156Z] TOOL RESULT

```
1115
https://en.wiktionary.org/wiki/%D8%B2%D9%86%D8%A8%D9%88%D8%B1
https://en.wiktionary.org/wiki/%D7%93%D7%91%D7%95%D7%A8%D7%94
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deh%E2%82%81-
https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D9%85
https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D9%87%DB%8C%D9%85
https://en.wiktionary.org/wiki/%CE%B4%CE%B9%CE%AC%CE%B4%CE%B7%CE%BC%CE%B1
https://www.etymonline.com/word/diadem
https://en.wiktionary.org/wiki/%DA%A9%DB%8C
https://www.etymonline.com/word/to
```


## [2026-09-05T17:39:21.254Z] TOOL CALL #80: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg110.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/110.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head"
}
```


### [2026-09-05T17:39:21.318Z] TOOL RESULT

```
total 3256
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 13:39 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r-- 1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r-- 1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-05T17:46:36.899Z] TOOL CALL #81: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk110.py",
 "content": "# -*- coding: utf-8 -*-\nimport json, io\n\nW_ZANBUR = \"https://en.wiktionary.org/wiki/%D8%B2%D9%86%D8%A8%D9%88%D8%B1\"\nW_DVORA  = \"https://en.wiktionary.org/wiki/%D7%93%D7%91%D7%95%D7%A8%D7%94\"\nW_DEH1   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deh%E2%82%81-\"\nW_DAM    = \"https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D9%85\"\nW_DEYHIM = \"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D9%87%DB%8C%D9%85\"\nW_DIADEM = \"https://en.wiktionary.org/wiki/%CE%B4%CE%B9%CE%AC%CE%B4%CE%B7%CE%BC%CE%B1\"\nE_DIADEM = \"https://www.etymonline.com/word/diadem\"\nW_KAY    = \"https://en.wiktionary.org/wiki/%DA%A9%DB%8C\"\nE_TO     = \"https://www.etymonline.com/word/to\"\n\ndoc = {\n \"pdf_page\": 110,\n \"book_page\": 80,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n\n # ================= ENTRY 0 =================\n {\n  \"entry\": 0,\n  \"root\": \"D.b.r, Dibbĕr, Dâbhar\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"Proto-Semitic *dVbr- 'bee' (Hebrew דְּבוֹרָה dəḇōrā); separately Semitic √d-b-r 'to speak' (Heb. dibbēr 'he spoke', dāḇār 'word, thing')\",\n  \"note\": \"The three glosses of the root box ('to buzz', 'he spoke', 'word') are exactly Klein's own statement on p.406 s.v. Deborah: 'from the Sem. base d-b-r-, meaning “to hum, buzz”, whence also dibber, “he spoke”, dabhar, “word, thing”'. So Nourai reproduces his source faithfully. Modern Semitic lexicography is more cautious: Wiktionary (following the Semitic Etymological Dictionary tradition) reconstructs a noun *dVbr- 'bee' for Heb. dəḇōrā / Syr. debbōrā / Arab. dabbūr, zunbūr and does NOT derive it from the verb 'to speak'; the reflexes also show an irregular d/z correspondence (Heb. d- but Aram. zibbūrā, Arab. zunbūr beside dabbūr), which points to an old culture word spread across the Semitic area rather than to a regular derivation from a verbal root. Hence 'plausible': the bee-words form one family (confirmed), but the further link 'buzz' > 'speak' > 'word' is the traditional Gesenius/Klein explanation, not today's consensus. Layout note: on the printed page there is one completely EMPTY box in entry 2 (to the right of the second Avestan node); it carries no language label and no words and is a typesetting artefact of the book, not something the extraction lost.\",\n  \"note_fa\": \"ریشهٔ سامی D.b.r با سه معنای «وزوز کردن؛ گفت؛ واژه» دقیقاً همان چیزی است که کلاین در ص ۴۰۶ ذیل Deborah می‌نویسد، پس نقل نورایی از منبعش درست است. اما ریشه‌شناسی سامی امروزی محتاط‌تر است: برای «زنبور» یک اسم سامی آغازین *dVbr- بازسازی می‌کنند (عبری dəḇōrā، سریانی debbōrā، عربی dabbūr و zunbūr) و آن را از فعل d-b-r «سخن گفتن» نمی‌گیرند؛ افزون بر این، تناوب نامنظم د/ز (عبری با «د» ولی آرامی zibbūrā و عربی zunbūr) نشان می‌دهد که با یک واژهٔ فرهنگی کهنِ سرگردان در حوزهٔ سامی روبه‌روییم نه با اشتقاق قاعده‌مند از یک ستاک فعلی. بنابراین: خانوادهٔ واژه‌های «زنبور» درست است، ولی پیوند «وزوز > سخن گفتن > واژه» با احتیاط پذیرفتنی است.\",\n  \"sources\": [W_ZANBUR, W_DVORA],\n  \"ref_check\": [\n   {\"ref\": \"KLN:406\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 224 (= printed pp. 405-406; leaf 223 carries the printed numeral '404'), s.v. 'Deborah, fem. PN.; in the Bible, a prophetess and judge in Israel. — Heb. Dĕbhōrāh, lit. “bee”, rel. to Syr. debbōrā, “wasp”, debbōrīthā, “bee”, Aram. dibbōrīthā, Arab. zunbūr, dabbūr, “bee”, from the Sem. base d-b-r-, meaning “to hum, buzz”, whence also dibber, “he spoke”, dabhār, “word, thing”.' — the root box word for word (grep -n 'Deborah' KLN_1966.txt).\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p.405/406, leaf 224 s.v. Deborah\", \"stance\": \"supports\",\n    \"note\": \"'from the Sem. base d-b-r-, meaning “to hum, buzz”, whence also dibber, “he spoke”, dabhār, “word, thing”' — this IS Nourai's root box.\"},\n   {\"src\": \"AFA\", \"where\": \"Fraenkel, Aram. Fremdwörter, p.125 f. (AFA.txt l.4633 ff.)\", \"stance\": \"silent\",\n    \"note\": \"Fraenkel treats only the beehive word (kuwwāra 'Bienenkorb', from Aramaic, ult. Persian) — 'Es kann keinem Zweifel unterliegen, dass dies Wort erst aus aram. … übernommen ist'; he says nothing about dabbūr/zunbūr or about d-b-r 'buzz/speak' (grep -i 'Biene|zunbur|dabbur' AFA.txt).\"},\n   {\"src\": \"LKT\", \"where\": \"whole text\", \"stance\": \"silent\",\n    \"note\": \"grep -i 'zunbur|dabbur' LKT.txt returns nothing; Lokotsch has no European word from this root.\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1, \"lang\": \"Arabic\", \"words\": \"dabbŭr, zunbŭr; z.b.n\",\n    \"verdict\": \"transcription_suspect\",\n    \"error_in\": \"book\",\n    \"book_prints\": \"z.b.n\",\n    \"correct_form\": \"z.n.b.r\",\n    \"derivation\": \"Arabic دَبُّور dabbūr and زُنْبُور zunbūr both mean 'hornet, large bee' and are doublets: dabbūr keeps the Semitic d of the Hebrew/Syriac forms, while zunbūr entered Arabic through Aramaic זבּור zibbūr / Syriac zibbōrā, whose z- reflects the irregular sibilant variant of the same culture word (Wiktionary s.v. زنبور: 'From Aramaic זבּור (zibbūr, “hornet”), doublet of دَبُّور (dabbūr); cognates with Classical Syriac ܕܒܘܪܐ (debbōrā) and Hebrew דְּבוֹרָה (dvorá)'). The n of zunbūr is a nasal infix/expansion of the same base (cf. Mandaic zimbura). The THIRD word in the box is the problem: the printed page (checked at 300 dpi, data/verification/sources/refs/ocr/BOOK/110.png) really reads 'z.b.n : bee'. There is no Arabic root z-b-n meaning 'bee' — زبن zabana means 'to push, thrust away'. Nourai's own convention here is to give the consonantal root of the preceding word, and that root is z-n-b-r (or the base z-b-r); 'z.b.n' is a metathesis/misprint of the book. The JSON reproduces the page faithfully, so the error is the author's, not the extraction's.\",\n    \"derivation_fa\": \"عربی «دَبّور» و «زُنبور» هر دو به معنی زنبور درشت‌اند و دوگانه (doublet) به شمار می‌آیند: «دبّور» همان دالِ سامی را نگه داشته و «زنبور» از راه آرامی zibbūr / سریانی zibbōrā وارد عربی شده که «ز» آن گونهٔ نامنظمِ همان واژهٔ کهن است؛ «ن» نیز افزودهٔ خیشومی همان ستاک است (سنجید با مندایی zimbura). اما واژهٔ سوم جعبه اشکال دارد: در صفحهٔ چاپی به‌روشنی «z.b.n» آمده، حال آنکه در عربی ریشهٔ «ز ب ن» به معنی زنبور نیست (زَبَنَ یعنی «راندن، پس زدن»)؛ ریشهٔ درستِ «زنبور» ز ن ب ر است. پس این خطای چاپی کتاب است، نه خطای خوانش اسکن.\",\n    \"sources\": [W_ZANBUR],\n    \"ref_check\": [\n     {\"ref\": \"KLN:406\", \"status\": \"partial\",\n      \"note\": \"Klein p.406 s.v. Deborah does list 'Arab. zunbūr, dabbūr, “bee”' — so the two real words are covered; Klein has nothing resembling a root 'z.b.n', which confirms that form is Nourai's own misprint.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"KLN\", \"where\": \"1966 ed. p.406, leaf 224\", \"stance\": \"supports\",\n      \"note\": \"'Arab. zunbūr, dabbūr, “bee”, from the Sem. base d-b-r-'.\"},\n     {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen (PLA_asbaghi_1988_ia_djvu.txt ll.11027, 11072)\", \"stance\": \"silent\",\n      \"note\": \"Asbaghi lists only زنبورک zanburak 'ein Teil der Uhr, aus dem pers. zamburak' — i.e. a Persian loan built ON Arabic zunbūr; he does not treat zunbūr itself, which is consistent with zunbūr not being Persian.\"},\n     {\"src\": \"AFA\", \"where\": \"Fraenkel, whole text\", \"stance\": \"silent\",\n      \"note\": \"no entry for dabbūr/zunbūr (grep -i 'zunbur|dabbur' AFA.txt: no hits).\"}\n    ]\n   },\n   {\n    \"id\": 2, \"lang\": \"Persian\", \"words\": \"zanbŭr\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"New Persian زنبور zanbūr 'bee, wasp, hornet' is an Arabic loan, taken over after the Islamic conquest from Arabic زُنْبُور zunbūr (Classical Persian /zan.ˈbuːr/, with the Arabic variant vocalisation zanbūr rather than the Modern Standard Arabic zunbūr — Wiktionary: 'Borrowed from Arabic زَنْبُور (zanbūr). An alternative pronunciation of Modern Standard Arabic زُنْبُور (zunbūr)'). Mo'in's Farhang-e Farsi marks the headword زنبور with the tag [ع.] = Arabic. The word is therefore the end point of the chain Semitic *dVbr- > Aramaic zibbūr > Arabic zunbūr > Persian zanbūr, exactly as the chart draws it; the native Persian word for the insect was مگس/انگبین-related, and Persian keeps zanbūr only as a loan (whence the diminutive zanburak, which Arabic later re-borrowed).\",\n    \"derivation_fa\": \"«زنبور» در فارسی نو وام‌واژه‌ای عربی است که پس از اسلام از عربی زُنبور گرفته شده؛ تلفظ کلاسیک فارسی zanbūr است که با گونهٔ عربی zanbūr می‌خواند نه با zunbūrِ عربی معیار امروز. معین در «فرهنگ فارسی» سرواژهٔ «زنبور» را با نشانهٔ [ع.] (عربی) آورده است. پس زنجیرهٔ سامی آغازین *dVbr- ← آرامی zibbūr ← عربی زُنبور ← فارسی زنبور همان است که نمودار نورایی می‌کشد و ادعای او درست است؛ خودِ فارسی بعدها «زنبورک» را از آن ساخت که دوباره به عربی وام رفت.\",\n    \"sources\": [W_ZANBUR],\n    \"ref_check\": [\n     {\"ref\": \"FVA:180\", \"status\": \"not_checked\",\n      \"note\": \"FVA = S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368/1989). refs_online.json records: 'Searched archive.org, ketabnak, noorlib, web: no digital copy found … RE-SEARCH 2026-09: still no digital copy on any permitted platform.' Nothing to check.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"MON\", \"where\": \"MON_part1.txt l.71670 s.v. زنبور\", \"stance\": \"supports\",\n      \"note\": \"'زنبور: [ع.] (ا.) (جان.) حشره‌ای بال نازک است…' — Mo'in's bracketed origin tag [ع.] marks the word as Arabic.\"},\n     {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol 2, leaf 496 ≈ printed p.1039 (زنبور / زنبوره)\", \"stance\": \"partial\",\n      \"note\": \"Borhan has the headwords زنبور/زنبوره ('صنبر زنبور است… و زنبور سیاه بزرگ را هم می‌گویند'), i.e. the word is old and well attested in Persian, but the scan gives no etymological footnote here — no statement for or against the Arabic origin.\"},\n     {\"src\": \"PLA\", \"where\": \"PLA_pages / djvu, ll.11027, 11072\", \"stance\": \"supports\",\n      \"note\": \"Asbaghi registers only the Persian-formed diminutive zanburak as a Persian loan INTO Arabic; the base zunbūr is not in his list of Persian loanwords, i.e. he treats it as Arabic — consistent with the direction Arabic > Persian.\"}\n    ]\n   },\n   {\n    \"id\": 3, \"lang\": \"Hebrew\", \"words\": \"Debhôrâh, Davôrâ\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Biblical Hebrew דְּבוֹרָה dəḇōrā (Tiberian /dvoːˈrɔː/, Modern Israeli dvorá) is the ordinary noun 'bee' used as a woman's name; it is the name of the prophetess and judge of Israel in Judges 4-5, whose 'Song of Deborah' is one of the oldest Hebrew poems. Wiktionary derives it 'From Proto-Semitic *dVbr- (“bee”). Cognate with Classical Syriac ܕܒܘܪܐ (debbōrā), Amharic ዲቧራ (dibʷara), Arabic دَبُّور (dabbūr), زُنْبُور (zunbūr), Classical Mandaic ࡆࡉࡌࡁࡅࡓࡀ (zimbura), Aramaic דְּבוֹרְתָא, זִיבּוֹרָא', citing Klein's Hebrew dictionary p.113a and Jastrow p.276b. Nourai's two transliterations are simply the Tiberian reading (Debhôrâh, with spirantised bh) and the Modern Israeli one (Davôrâ). The one point where the chart goes beyond the sources is the link to dibbēr 'he spoke': Wiktionary files דבורה under the Hebrew root ד־ב־ר but takes the etymology back to a noun for 'bee', not to the verb.\",\n    \"derivation_fa\": \"«دِبورا» (دْبورا) در عبری کتاب مقدس اسم عام «زنبور عسل» است که نام زن هم شده؛ دبورهٔ نبیّه و داور بنی‌اسرائیل در سِفر داوران باب‌های ۴ و ۵ و سرایندهٔ «سرود دبوره» است. ویکی‌واژه آن را از سامی آغازین *dVbr- «زنبور» می‌گیرد و هم‌ریشه‌های سریانی debbōrā، امهری dibʷara، عربی dabbūr و zunbūr و مندایی zimbura را برمی‌شمرد (به استناد فرهنگ عبریِ کلاین ص ۱۱۳ و یاسترو ص ۲۷۶). دو آوانگاریِ نورایی همان خوانش طبریِ Debhôrâh و خوانش عبری امروزی Davôrâ است. تنها نکتهٔ فراتر از منابع، پیوند دادن آن به فعل dibbēr «گفت» است که ویکی‌واژه آن را نمی‌آورد.\",\n    \"sources\": [W_DVORA],\n    \"ref_check\": [\n     {\"ref\": \"KLN:406\", \"status\": \"supports\",\n      \"note\": \"Klein p.406: 'Deborah, fem. PN.; in the Bible, a prophetess and judge in Israel. — Heb. Dĕbhōrāh, lit. “bee”, rel. to Syr. debbōrā …' — the node's form, language and gloss (including 'name of a prophetess in Bible') are Klein's own wording.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"KLN\", \"where\": \"1966 ed. p.406, leaf 224\", \"stance\": \"supports\",\n      \"note\": \"'Heb. Dĕbhōrāh, lit. “bee”'.\"},\n     {\"src\": \"AFA\", \"where\": \"Fraenkel, whole text\", \"stance\": \"silent\",\n      \"note\": \"Fraenkel's subject is Aramaic loans in Arabic; no entry on Hebrew dəḇōrā (grep -i 'debora|dbwrh|Biene' AFA.txt gives only the beehive discussion at p.125).\"}\n    ]\n   },\n   {\n    \"id\": 4, \"lang\": \"English\", \"words\": \"Deborah, Debbie\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"English Deborah is the Hebrew name taken over unchanged through the Vulgate/Septuagint spelling Debbora and, decisively, through the English Bible; it became a common baptismal name among Puritans in the 16th-17th c. and was carried to New England, which is why it is far commoner in American than in British usage. Debbie (also Deb, Debby) is the ordinary English hypocoristic, first syllable + the -ie/-y diminutive suffix; Funk & Wagnalls (FSD) still lists it lexically: 'Deb., n. Diminutive of Deborah.' No sound change is involved beyond the anglicised stress (ˈdebərə) and the loss of the Hebrew final -āh.\",\n    \"derivation_fa\": \"«Deborah» در انگلیسی همان نام عبری است که از راه ترجمه‌های یونانی و لاتینی کتاب مقدس (Debbora) و سپس انجیل انگلیسی بی‌دگرگونی وارد شده و در سدهٔ ۱۶ و ۱۷ در میان پیوریتن‌ها نام تعمیدی رایجی شد و با مهاجران به نیوانگلند رفت؛ از همین رو در انگلیسی آمریکایی رایج‌تر است. «Debbie» تصغیر عادی انگلیسی است: هجای نخست + پسوند تصغیر ‎-ie/-y؛ فرهنگ فانک و واگنالز هنوز مدخل «Deb., n. Diminutive of Deborah» را دارد. جز جابه‌جایی تکیه به ˈdebərə و افتادن «-اه» پایانی عبری، دگرگونی آوایی دیگری در کار نیست.\",\n    \"sources\": [W_DVORA],\n    \"ref_check\": [\n     {\"ref\": \"AHD:340\", \"status\": \"not_checked\",\n      \"note\": \"Nourai's AHD numbers are pages of the 1975/76 American Heritage Dictionary, New College Edition, whose main A-Z text is not open online (refs_online.json: the 1970s AHD scans on IA are lending-only, djvu.txt returns 401); the local AHD file is Watkins 1985, which contains only the Indo-European appendix and has no entry for a Hebrew name. Page 340 of the New College Edition falls in the deb-/dec- range, which is consistent with a 'Deborah' entry, but I could not read it.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"KLN\", \"where\": \"1966 ed. p.406, leaf 224 s.v. Deborah\", \"stance\": \"supports\",\n      \"note\": \"Klein enters Deborah as an English female personal name of Hebrew origin — 'Deborah, fem. PN.; in the Bible, a prophetess and judge in Israel'.\"},\n     {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. I (FSD_vol1.txt l.87392)\", \"stance\": \"supports\",\n      \"note\": \"'Deb., n. Diminutive of Deborah.' — the short form the chart calls Debbie is lexicalised.\"}\n    ]\n   }\n  ]\n },\n\n # ================= ENTRY 1 =================\n {\n  \"entry\": 1,\n  \"root\": \"Dě 1\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *deh₁- 'to bind' (Pokorny dē-, də- and dei-, dī- 'binden', IEW 183; Watkins dē-)\",\n  \"note\": \"Root, language label and gloss are all correct. Pokorny's headword (POK_full.txt: 'Root/lemma: dē-, də- and dei-, dī-; Meaning: to bind; … References: WP. I 771 f.; Page(s): 183') is Nourai's Dě 1 with his citation POK:183. In today's laryngeal notation the root is *deh₁- (Wiktionary), the -ə- of Pokorny being the reflex of h₁. Buck §9.16 BIND lists it as 'IE *de(i)-, *dō-. Walde-P. 1.771'. Note that Pokorny adds the (not universally accepted) idea that the root is a derivative of the numeral *dwo- 'two', 'bind in two' — this is the ☞Dwo cross-reference in the Greek node; Watkins and Wiktionary do not follow it, and the semantics of dia-deō ('bind across') are enough to explain the compound without it.\",\n  \"note_fa\": \"ریشه، برچسب زبانی و معنا هر سه درست است. سرواژهٔ پوکورنی «dē-، də- و dei-، dī- «بستن»» در ص ۱۸۳ ایونتسه‌وُرت‌بوخ همان Dě 1 نورایی است و ارجاع POK:183 دقیق است. در نویسهٔ حنجری امروزی این ریشه *deh₁- نوشته می‌شود و ə پوکورنی بازتاب همان h₁ است. باک در بند ۹٫۱۶ («بستن») نیز آن را «هندواروپایی *de(i)-، *dō-» می‌آورد. تنها نکتهٔ محل بحث، حدسِ پوکورنی است که این ریشه را برگرفته از عدد *dwo- «دو» («به دو بستن») می‌داند — همان ارجاع ☞Dwo در جعبهٔ یونانی؛ واتکینز و ویکی‌واژه آن را نمی‌پذیرند و معنای dia-deō «از دو سو بستن» بی‌نیاز از این فرض توضیح می‌دهد.\",\n  \"sources\": [W_DEH1],\n  \"ref_check\": [\n   {\"ref\": \"POK:183\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt l.19653: 'Root/lemma: dē-, də- and dei-, dī-. Meaning: to bind … Material: Old Indic dyati … dāman- n. “band, strap” (= gr. -δημα) … gr. δέω “bind” … ὑπό-δημα … διάδημα “a band or fillet, turban, diadem”. References: WP. I 771 f. Page(s): 183.' Exactly the root box and its two branches.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I p.771 (WLD_Bd1_pages.txt leaf 779)\", \"stance\": \"supports\",\n    \"note\": \"'dē- : də- (dei-) “binden”. Ai. dy-áti … ai. ptc. dita- “gebunden” (= gr. δετός), dāman- n. “Band” (= gr. -δημα) … gr. δέω “binde” … ὑπό-δημα (= ai. dāman-) “Sandale”, διάδημα “umgeschlungenes Band, Turban, Diadem”.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt l.360)\", \"stance\": \"supports\",\n    \"note\": \"'dē-. To bind. Contracted from *deə-. Greek dein, to bind: DESMID; ANADEM, ASYNDETON, DIADEM, PLASMODESMA, (SYNDESMOSIS), SYNDETIC. [Pok. dē- 183.]' — same root, same page reference as Nourai.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §9.16 BIND, no. 2 (SYN.txt l.13765)\", \"stance\": \"supports\",\n    \"note\": \"'Skt. dā-, di- “bind” (3sg. dyati), Grk. δέω, with Skt. dāman-, sandāna- “bond”, Grk. δεσμός. IE *de(i)-, *dō-. Walde-P. 1.771.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt\", \"stance\": \"silent\",\n    \"note\": \"grep for 'dāman'/'dēmn' in IEC.txt returns only the unrelated dhēmn- 'setting, fixture' entry (l.2784); Mann has no usable entry for this root under the spellings tried.\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1, \"lang\": \"Sanskrit\", \"words\": \"dâman\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Vedic/Sanskrit दामन् dā́man- n. is the regular *-mn̥ action/instrument noun of the root: PIE *déh₁-mn̥ > Proto-Indo-Iranian *dáHma > Skt dā́man- 'string, cord, rope, fetter, band' (the laryngeal lengthens the root vowel to ā and is lost, and *-mn̥ becomes -man). Its exact Greek match is -δημα in ὑπόδημα 'sandal' (Walde-Pokorny I 771 writes 'dāman- n. “Band” (= gr. -δημα)', and Pokorny 183 the same). The verb belonging to it is dyáti 'binds' (zero grade *dh₁-yé-ti). One caveat on the gloss: dā́man- means 'band, rope, tether, fetter' — 'trap' is not a Sanskrit sense but has been carried back into the box from the Persian derivative in the next node.\",\n    \"derivation_fa\": \"«دامَن» (dā́man-) در سنسکریت وداییْ اسمِ ابزار/کنشِ منظمِ ساخته‌شده با پسوند ‎*-mn̥‎ از همین ریشه است: هندواروپایی آغازین *déh₁-mn̥ ← هندوایرانی آغازین *dáHma ← سنسکریت dā́man- «ریسمان، بند، طناب، زنجیر»؛ حنجریِ h₁ واکهٔ ریشه را کشیده کرده و خود از میان رفته و ‎*-mn̥‎ به ‎-man‎ بدل شده است. همتای دقیق یونانی‌اش ‎-δημα‎ در ὑπόδημα «کفش» است (والده‑پوکورنی جلد ۱ ص ۷۷۱: «dāman- n. Band (= gr. ‎-δημα‎)»). فعلِ هم‌خانوادهٔ آن dyáti «می‌بندد» است. یک نکتهٔ معنایی: dā́man- یعنی «بند و ریسمان»؛ معنای «تله» سنسکریت نیست و از واژهٔ فارسیِ جعبهٔ بعد به این جعبه سرایت کرده است.\",\n    \"sources\": [W_DEH1],\n    \"ref_check\": [\n     {\"ref\": \"POK:183\", \"status\": \"supports\",\n      \"note\": \"POK_full.txt l.19653 (page 183): 'Old Indic dy-áti … “binds” … Old Indic participle dita- “bound” (= gr. δετός), dāman- n. “band, strap” (= gr. -δημα), ni-dātar- “binder”.'\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. I p.771 (leaf 779)\", \"stance\": \"supports\",\n      \"note\": \"'ai. ptc. dita- “gebunden” (= gr. δετός), dāman- n. “Band” (= gr. -δημα), ni-dātar- “Binder”'.\"},\n     {\"src\": \"SYN\", \"where\": \"Buck §9.16 BIND no. 2\", \"stance\": \"supports\",\n      \"note\": \"'with Skt. dāman-, sandāna- “bond”' — Buck too glosses it 'bond', not 'trap'.\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dē-\", \"stance\": \"partial\",\n      \"note\": \"Watkins gives only the Greek branch of the root (dein) because his appendix lists English derivatives; the Sanskrit noun is not mentioned. Silent, not contradicting.\"}\n    ]\n   },\n   {\n    \"id\": 2, \"lang\": \"Persian\", \"words\": \"dâm\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"New Persian دام dām 'snare, trap, net' is real and old, but it is a COUSIN of Sanskrit dāman-, not a descendant of it: Wiktionary derives it 'From Proto-Indo-Iranian *dáHma (compare Sanskrit दामन् (dā́man, “string, cord, rope, fetter”)), from Proto-Indo-European *déh₁-mn̥, from *deh₁- (“to bind”)', i.e. Proto-Iranian *dáHma > Middle Persian dām 'net, snare, trap' (MacKenzie, Concise Pahlavi Dictionary p.24: 'dām [dʾm | P dʾmg, N ~] net, snare, trap') > NP dām, with the Old Iranian -man stem simply losing its final syllable in Middle Persian as usual. The semantic step 'band, rope' > 'net' > 'snare, trap' is already Middle Iranian. Mo'in, in his footnote to the Borhan-e Qate' entry, gives exactly this comparative material. Nourai's arrow Sanskrit → Persian is therefore the right root and the right *word*, but the wrong direction of transmission (Persian did not borrow from Sanskrit); hence 'plausible'. Note also that the homograph dām 'livestock, tame animal' (Borhan's first sense, 'نقیض دد') is a different word, from MP dām < PIE *demh₂- 'to tame'; the chart's «دام ۲» correctly picks the second, 'trap' entry.\",\n    \"derivation_fa\": \"«دام» به معنی «تله، تور» در فارسی نو واژه‌ای کهن و اصیل است، اما هم‌ریشهٔ dāman- سنسکریت است نه برگرفته از آن: هندواروپایی آغازین *déh₁-mn̥ ← هندوایرانی آغازین *dáHma ← ایرانی آغازین *dāma- ← فارسی میانه (پهلوی) dām «تور، دام» (مکنزی، ص ۲۴: «dām [dʾm] net, snare, trap») ← فارسی نو «دام»؛ ستاکِ ‎-man‎ِ ایرانی باستان در فارسی میانه هجای پایانی را از دست داده است. تحول معنایی «بند/ریسمان» ← «تور» ← «تله» در همان دورهٔ ایرانی میانه رخ داده است. معین در حاشیهٔ «برهان قاطع» دقیقاً همین شواهد را می‌آورد. بنابراین ریشه و واژه درست است ولی جهت انتقالی که نورایی می‌کشد (سنسکریت ← فارسی) نادرست است و باید «هم‌ریشه» خواند؛ از این رو با احتیاط پذیرفتنی است. همچنین «دام» به معنی «چارپای اهلی» (معنی نخست برهان: «نقیض دد») واژه‌ای جداست از ریشهٔ *demh₂- «رام کردن»، و «دام ۲»ِ نمودار درست همان «تله» را برگزیده است.\",\n    \"sources\": [W_DAM, W_DEH1],\n    \"ref_check\": [\n     {\"ref\": \"BQT:817\", \"status\": \"supports\",\n      \"note\": \"Borhan-e Qate' vol. 2, leaf 277 of BQT_v2_pages.txt (printed page ≈ leaf+543, i.e. 817-820; the headword block دام runs from Nourai's cited page). The entry's sense 4 is 'هرچیز که جانوران در آن بفریب گرفتار شوند' = snare, and Mo'in's footnote 4 at the bottom of the page reads: 'هندی باستان dāman- (بند، ریسمان، زنجیر)، … ارمنی dam (تور) «امذق ۱۳۰»، پهلوی dām «مناس ۱۷۲»؛ نیز تور ماهیگیری' — Old Indic dāman- 'band, rope, chain', Armenian dam 'net', Pahlavi dām. That is Nourai's arrow, with the same Sanskrit comparandum.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.24 (PHD.txt l.308)\", \"stance\": \"supports\",\n      \"note\": \"'dām [dʾm | P dʾmg, N ~] net, snare, trap' — the Middle Persian link Nourai's chart skips; also 'dām [dʾm | = M, N ~] tame animal' and 'dām [dʾm | = M] creature, creation', i.e. three homographs.\"},\n     {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. دام (MON_part1.txt l.59266)\", \"stance\": \"supports\",\n      \"note\": \"'دام (ا.) آلتی که جانوران را به فریب گرفتار سازد؛ بند، تله. آلتی که بدان ماهیان را صید کنند، تور ماهیگیری' — the trap sense, and carrying no [ع.]/foreign tag, i.e. treated as inherited Persian.\"},\n     {\"src\": \"BQT\", \"where\": \"vol. 2 leaf 277, Mo'in's footnote\", \"stance\": \"supports\",\n      \"note\": \"quoted above; note that Mo'in cites Hübschmann-style comparanda but sets Sanskrit and Persian side by side as cognates, not as source and borrower.\"}\n    ]\n   },\n   {\n    \"id\": 3, \"lang\": \"Greek\", \"words\": \"dein; dia-dein, dia-děma\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Greek δέω (Homeric/Attic, from *deh₁-yō) 'I bind', verbal adjective δετός 'bound' (= Skt dita-), noun δεσμός 'band'; with the preverb διά 'across, through' it gives διαδέω 'to bind across, bind round on both sides', whence the result-noun διάδημα (διαδέω + -μα, Wiktionary) 'the band tied round the head'. The -δημα of the compound is the exact cognate of Skt dāman- (Walde-Pokorny I 771 makes the equation explicitly for ὑπό-δημα). The chart's gloss 'a headband tied on two sides' renders the διά- literally and is right; the ☞Dwo cross-reference reflects Pokorny's speculation that the root itself contains *dwo- 'two', which is not needed and not generally accepted — διά alone accounts for it. Historically διάδημα was the white headband of the Achaemenid Great King; Alexander adopted it, and it became the Hellenistic royal insignia (Etymonline: 'the headband worn by Persian kings and adopted by Alexander the Great and his successors').\",\n    \"derivation_fa\": \"یونانی δέω (از ‎*deh₁-yō‎) «می‌بندم»، صفت مفعولی δετός «بسته» (برابر با dita- سنسکریت) و اسم δεσμός «بند»؛ با پیشوند διά «از میان، از دو سو» فعل διαδέω «از دو سو بستن» و از آن اسمِ حاصلِ διάδημα (διαδέω + پسوند ‎-μα‎) «نواری که گرد سر می‌بندند» ساخته شده است. جزء ‎-δημα‎ همان هم‌ریشهٔ دقیقِ dāman- سنسکریت است (والده‑پوکورنی جلد ۱ ص ۷۷۱ این برابری را برای ὑπό-δημα صریح می‌آورد). ترجمهٔ نورایی «نواری که از دو سو بسته می‌شود» درست است؛ ارجاع ☞Dwo بازتاب حدس پوکورنی است که خود ریشه را حاوی *dwo- «دو» می‌داند و پذیرفتهٔ همگان نیست، چون διά به تنهایی بس است. از نظر تاریخی، διάδημα همان نوار سپیدِ شاهان هخامنشی بود که اسکندر آن را پذیرفت و نشان شاهی دولت‌های هلنی شد.\",\n    \"sources\": [W_DIADEM, E_DIADEM, W_DEH1],\n    \"ref_check\": [\n     {\"ref\": \"POK:183\", \"status\": \"supports\",\n      \"note\": \"POK_full.txt l.19653 (p.183): 'gr. (hom. Attic) δέω (*δέjω) “bind”, δετός “bound” … ὑπό-δημα (compare Old Indic dāman-) “sandal”, διάδημα “a band or fillet, turban, diadem”.'\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. I p.771 (leaf 779)\", \"stance\": \"supports\",\n      \"note\": \"'gr. δέω (*δέ-jω) “binde”, δετός “gebunden” … διάδημα “umgeschlungenes Band, Turban, Diadem”.'\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dē-\", \"stance\": \"supports\",\n      \"note\": \"'Greek dein, to bind: DESMID; ANADEM, ASYNDETON, DIADEM …'\"},\n     {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. diadem, leaf 242 (pp.442-443)\", \"stance\": \"supports\",\n      \"note\": \"'Gk. διάδημα, “band, fillet, royal headband”, fr. διαδεῖν, “to bind on either side”, fr. διά (see dia-) and δεῖν, “to bind”, fr. I.-E. base *de(i)-, *dī-, “to bind”, whence also OI. dy-áti, “binds”, dā-man, “band, bond”.' — 'bind on either side' is precisely Nourai's gloss.\"}\n    ]\n   },\n   {\n    \"id\": 4, \"lang\": \"Persian\", \"words\": \"dayhîm\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"New Persian دیهیم dayhīm 'royal diadem, crown' is a Greek word that came back to Iran: Ancient Greek διάδημα was taken into Parthian as 𐭃𐭉𐭃𐭉𐭌 dīδēm / dīdēm 'half-crown, flower-crown', thence Middle Persian dīdēm / dīyēm 'diadem', thence NP dayhīm (Wiktionary s.v. دیهیم: 'From Middle Persian dīyēm, dīdēm “diadem” from Parthian dīδēm, dīdēm “half-crown, flower-crown”. Ultimately from Ancient Greek διάδημα'). Phonetically: Greek -ᾰ- of the first syllable is lost in the Iranian shape dī-, Greek -δη- gives Parthian -δē-, and the intervocalic Middle Iranian δ is weakened to h/y in New Persian, giving dai-h-īm; the final -a of διάδημα drops as usual. Since the Greek word itself denotes the Achaemenid king's headband, the word is a genuine round trip: Persian object > Greek name > Parthian/Middle Persian loan > New Persian dayhīm. Mo'in's Farhang-e Farsi confirms the origin with the tag [یو.] (Greek) on the compound دیهیم‌جو(ی).\",\n    \"derivation_fa\": \"«دیهیم» در فارسی نو وام‌واژه‌ای یونانی است که به ایران بازگشته است: یونانی διάδημα به پارتی 𐭃𐭉𐭃𐭉𐭌 dīδēm «نیم‌تاج، تاج گل» راه یافت، از آنجا به فارسی میانه dīdēm/dīyēm و سپس به فارسی نو «دیهیم». از نظر آوایی: «ا»ی هجای نخستِ διά در صورت ایرانی می‌افتد و dī- می‌ماند، ‎-δη-‎ یونانی در پارتی ‎-δē-‎ می‌شود، و ذالِ ایرانی میانه در میان دو واکه در فارسی نو به «ه/ی» نرم می‌شود؛ چنین است که dīdēm به dayhīm می‌رسد و «ـه»ی پایانی یونانی نیز می‌افتد. چون خودِ واژهٔ یونانی نام نوار سر شاهان هخامنشی است، اینجا با یک رفت‌وبرگشت تمام‌عیار روبه‌روییم: نشانِ ایرانی ← نامِ یونانی ← وام پارتی و پهلوی ← «دیهیم» فارسی. معین نیز در «فرهنگ فارسی» ذیل «دیهیم‌جو(ی)» نشانهٔ [یو.] (یونانی) را می‌گذارد. ادعای نورایی درست است.\",\n    \"sources\": [W_DEYHIM, E_DIADEM],\n    \"ref_check\": [\n     {\"ref\": \"BQT:921\", \"status\": \"supports\",\n      \"note\": \"Borhan-e Qate' vol. 2, BQT_v2_pages.txt leaf 381 (printed ≈ leaf+543 = 921-924, the last page of the د section, next leaf starting ذ): 'دیهیم ۱ ـ بکسر ها بروزن تعظیم، تاجی که مخصوص پادشاهان است … و بمعنی تخت'; the footnote at the foot of the leaf glosses it as the band 'که بر (افسر) پادشاه ایران بسته می‌شد'. The entry is where Nourai says it is and gives the meaning 'crown' he prints; the scan's footnote is too damaged to read the Greek etymon, which MON supplies.\"},\n     {\"ref\": \"MON:1603\", \"status\": \"supports\",\n      \"note\": \"Mo'in, Farhang-e Farsi, s.v. دیهیم (MON_part1.txt l.64922 area): the headword is glossed 'نواری مخصوص که گرد تاج پادشاه ایران بسته می‌شد؛ زر پادشاهی، کلاه مرصع' with a Latin-script etymon (OCR-garbled, = diadēma), and the immediately following compound is tagged '[یو. ف. ـ دیهیم جوینده]', where یو. = یونانی (Greek). Mo'in therefore marks دیهیم as Greek, as Nourai's arrow requires.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"MON\", \"where\": \"MON_part1.txt ll.64922-64924 (دیهیم، دیهیم‌جو)\", \"stance\": \"supports\",\n      \"note\": \"'[یو. ف.]' tag = Greek + Persian.\"},\n     {\"src\": \"BQT\", \"where\": \"vol. 2 leaf 381 ≈ p.921-924\", \"stance\": \"supports\",\n      \"note\": \"'دیهیم … تاجی که مخصوص پادشاهان است'; also the byform 'دیهول [ـ داهول] تاج مرصع'.\"},\n     {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary\", \"stance\": \"silent\",\n      \"note\": \"grep -i 'didem|dydym' PHD.txt: no hits — MacKenzie's concise glossary does not carry the word, so the Middle Persian form is taken from the Manichaean/Parthian material cited by Wiktionary.\"}\n    ]\n   },\n   {\n    \"id\": 5, \"lang\": \"Latin\", \"words\": \"diadema\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Latin diadēma, -atis n. is a straight Hellenistic borrowing of Greek διάδημα, taken over with the Greek -μα/-ματος stem (hence the neuter and the Greek-type genitive) at the time when Rome met the Hellenistic monarchies (2nd-1st c. BCE); it means 'the cloth band worn round the head as a sign of royalty' (Etymonline). It supplied the word to the Romance languages and, through Old French diademe, to English. Nothing in the form changes: Greek δ/ι/ά/δ/η/μ/α is transliterated letter for letter, Greek η giving Latin ē.\",\n    \"derivation_fa\": \"لاتین diadēma وام‌گیریِ مستقیمِ یونانی διάδημα است که در دورهٔ رویارویی روم با پادشاهی‌های هلنی (سدهٔ دوم و یکم پیش از میلاد) با همان ستاک ‎-μα/-ματος‎ به لاتین رفته و از این رو خنثی است و صرفِ یونانی‌وار دارد؛ معنایش «نوار پارچه‌ای که به نشانِ شاهی گرد سر می‌بندند» است. همین واژه به زبان‌های رومی و از راه فرانسهٔ باستان diademe به انگلیسی رسیده است. هیچ دگرگونی آوایی در کار نیست: حرف‌به‌حرف آوانویسی شده و «η» یونانی در لاتین ē شده است.\",\n    \"sources\": [E_DIADEM, W_DIADEM],\n    \"ref_check\": [\n     {\"ref\": \"AHD:363\", \"status\": \"not_checked\",\n      \"note\": \"AHD:363 is a page of the 1975/76 American Heritage Dictionary New College Edition (main A-Z text), which is not open online (lending-only on archive.org; djvu.txt 401). Page 363 falls in the di- range, consistent with a 'diadem' entry. The local AHD file (Watkins 1985, the IE appendix) covers the same claim from the root side: 'dē-. To bind … Greek dein, to bind: … DIADEM' (AHD_watkins1985.txt l.360), and the appendix index line 'DIADEM dé-' (l.1424).\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"KLN\", \"where\": \"1966 ed. leaf 242 (pp.442-443) s.v. diadem\", \"stance\": \"supports\",\n      \"note\": \"'diadem, n., crown; fillet. — OF. diademe (F. diadème), fr. L. diadema, fr. Gk. διάδημα …' — the Greek > Latin step is explicit.\"},\n     {\"src\": \"LAT\", \"where\": \"Ernout-Meillet (LAT.txt l.25301)\", \"stance\": \"silent\",\n      \"note\": \"'diadema' occurs only inside a quoted Latin word-list (rete, diadema, coronas aureas …), not as a headword; Ernout-Meillet do not treat this obvious Greek loan.\"},\n     {\"src\": \"LEW\", \"where\": \"Walde 1910 (LEW_1910.txt)\", \"stance\": \"silent\",\n      \"note\": \"grep -i 'diadema' LEW_1910.txt: no hits; the 1910 Walde omits transparent Greek loanwords.\"}\n    ]\n   },\n   {\n    \"id\": 6, \"lang\": \"English\", \"words\": \"diadem\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"English diadem is first recorded c.1300 as diademe 'aureole of a martyr or confessor', and from the mid-14th c. in the royal sense 'a crown, anything worn on the head as a mark of royalty' (Etymonline). It comes from Old French diademe and directly from Latin diadēma, itself from Greek διάδημα; the Middle English trisyllable diademe lost its final -e in the 15th-16th c. as unstressed final -e fell throughout English, giving modern diadem. Klein gives the same chain and takes it back to the same base: 'fr. I.-E. base *de(i)-, *dī-, “to bind”, whence also OI. dy-áti, “binds”, dā-man, “band, bond”'.\",\n    \"derivation_fa\": \"واژهٔ انگلیسی diadem نخستین بار حدود سال ۱۳۰۰ به صورت diademe به معنی «هالهٔ شهیدان» و از میانهٔ سدهٔ چهاردهم به معنی شاهانهٔ «تاج، هر آنچه به نشان شاهی بر سر نهند» ثبت شده است. از فرانسهٔ باستان diademe و مستقیماً از لاتین diadēma آمده و آن از یونانی διάδημα. صورت سه‌هجایی انگلیسی میانه diademe در سده‌های پانزدهم و شانزدهم با افتادن «ـه»ی بی‌تکیهٔ پایانی در سراسر انگلیسی به diadem بدل شد. کلاین همین زنجیره را می‌آورد و آن را به همان ریشهٔ هندواروپایی «بستن» می‌رساند و سنسکریت dāman- را هم‌ریشه می‌شمارد. ادعای نورایی درست است.\",\n    \"sources\": [E_DIADEM],\n    \"ref_check\": [\n     {\"ref\": \"KLN:440\", \"status\": \"supports\",\n      \"note\": \"Klein does have exactly this entry, but on pp.442-443 of the 1966 two-volume edition, not 440: KLN_1966.txt leaf 242 runs from 'diaconus' to 'Diana', while leaf 241 (which carries the printed numerals 440 and 441) runs 'deity … diaconate'. So Nourai's page number is two off; the content — 'diadem, n., crown; fillet. — OF. diademe (F. diadème), fr. L. diadema, fr. Gk. διάδημα, “band, fillet, royal headband”, fr. διαδεῖν, “to bind on either side”' — supports the arrow completely.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"KLN\", \"where\": \"1966 ed. leaf 242 s.v. diadem\", \"stance\": \"supports\",\n      \"note\": \"quoted above; Klein also cross-refers anadem, asyndeton, desmo-, all from the same base.\"},\n     {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary\", \"stance\": \"silent\",\n      \"note\": \"grep -i 'diadem' SKT.txt: no hits — the Concise Skeat has no entry for this word.\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 index (AHD_watkins1985.txt l.1424)\", \"stance\": \"supports\",\n      \"note\": \"'DIADEM dé-' in the English-to-root index, i.e. Watkins refers English diadem to the root dē- 'to bind'.\"}\n    ]\n   }\n  ]\n },\n\n # ================= ENTRY 2 =================\n {\n  \"entry\": 2,\n  \"root\": \"De 2, Do 1\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *de-/*do-, demonstrative/deictic pronominal stem and particle (Pokorny 'de-, do-, a demonstrative stem', IEW 181-183; Watkins de-)\",\n  \"note\": \"Root, language label and gloss are correct, and the page number is right: Pokorny's entry 'de- do-, Meaning: a demonstrative stem' is printed on pp.181-183 (POK_full.txt gives 'Page(s): 181-183'), so POK:181 for the root, POK:182 and POK:183 for material inside it are all consistent. Walde-Pokorny I 769-771 is the same entry in the earlier edition. Everything on this chart is enclitic/adverbial material of the stem, which is exactly how the modern handbooks treat it (Watkins: 'de-. Demonstrative stem, base of prepositions and adverbs … [Pok. de-, do- 181.]'). Note that Nourai separates this stem (De 2, Do 1) from the homophonous root of entry 1 (Dě 1 'to bind') — correctly, since Pokorny too has them as two consecutive but distinct lemmas on p.183.\",\n  \"note_fa\": \"ریشه، برچسب زبانی و معنا درست است و شمارهٔ صفحه نیز دقیق: مدخل پوکورنی «de- do-، ستاک اشاره» در صفحه‌های ۱۸۱ تا ۱۸۳ چاپ شده، پس POK:181 برای ریشه و POK:182 و POK:183 برای مواد درون آن با هم می‌خوانند؛ والده‑پوکورنی جلد ۱ ص ۷۶۹–۷۷۱ همان مدخل در ویراست پیشین است. هرچه در این نمودار آمده مادهٔ پی‌بستی و قیدیِ همین ستاک است و کتاب‌های امروزی هم آن را چنین می‌بینند (واتکینز: «de-، ستاک اشاره، پایهٔ حروف اضافه و قیدها»). نورایی این ستاک را از ریشهٔ هم‌آوای مدخل پیشین (Dě 1 «بستن») جدا کرده و این جداسازی درست است، چون پوکورنی نیز آن دو را دو مدخل پیاپی ولی جداگانه در ص ۱۸۳ آورده است.\",\n  \"sources\": [E_TO],\n  \"ref_check\": [\n   {\"ref\": \"POK:181\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt l.19507: 'Root / lemma: de- do-. Meaning: a demonstrative stem. Material: Avestan vaēsman-da “up there to the house”; gr. -δε in ὅ-δε, ἥ-δε, τό-δε … Latin in-de, un-de … References: WP. I 769 ff., WH. I 325 f. … Page(s): 181-183.'\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I pp.769-771 (WLD_Bd1_pages.txt leaves 778-779)\", \"stance\": \"supports\",\n    \"note\": \"running head 'de-, do-' on p.770 and 'de- : də- (dei-)' on p.771; the entry contains the whole adverbial series 'ai. tadā “dann”, av. taδa … ai. kadā “wann?”, av. kada, jav. kaδa “wann?” … ai. yadi “wenn”, ap. yadiy, av. yeδi, yeidi “zur Zeit als” und av. yaθāt “woher”'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt l.360)\", \"stance\": \"supports\",\n    \"note\": \"'de-. Demonstrative stem, base of prepositions and adverbs. 1. Germanic *tō in Old English tō, to: TO, TOO. 2. Perhaps Latin dē, dē-, from: DE-. … [Pok. de-, do- 181.]'\"},\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p.1622 (leaf 860) s.v. to, prep.\", \"stance\": \"supports\",\n    \"note\": \"'from the I.-E. pronominal base *do-, “to, toward, upwards” … Cp. also I.-E. *de in Avestic -da (as in vaesmen-da, “to the house”), Gk. -δε … and in L. -de (as in inde, “thence”, unde, “whence”).'\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1, \"lang\": \"Avestan\", \"words\": \"ka-da, ka-tha\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Avestan kada (Gathic) and kaδa (Younger Avestan) 'when?' — Nourai's two spellings, his 'th' standing for the fricative δ — are the interrogative stem *kʷo-/ka- (whence the ☞Kwo cross-reference) plus the adverbial ending -da/-δa of the demonstrative stem *de-/*do-. Jackson's Avesta Grammar §4226 states the equation directly: 'Suffix G/YAv. -da, -δa = Skt. -da, -dha, -dhā; Av. yaδa, yaδā “when” = Skt. yadā; Av. kaδa, kada “when?” = Skt. kadā. So Av. aδa “then” = Skt. adha, adhā.' The alternation d ~ δ is purely positional: intervocalic Old Iranian d became the voiced fricative δ in Younger Avestan, while the Gathic spelling keeps d. So the arrow root → Avestan is exactly right: it is the ENDING, not the whole word, that comes from *de-/*do-.\",\n    \"derivation_fa\": \"اوستایی kada (گاهانی) و kaδa (اوستایی نو) «کِی؟» — دو نویسشی که نورایی می‌آورد و «th» او همان ذال (δ) است — از ستاک پرسشی ‎*kʷo-/ka-‎ (همان ارجاع ☞Kwo) به‌علاوهٔ پایانهٔ قیدیِ ‎-da/-δa‎ از ستاک اشارهٔ *de-/*do- ساخته شده است. جکسن در «دستور اوستا» بند ۴۲۲۶ همین برابری را می‌آورد: «پسوند ‎-da، -δa‎ = سنسکریت ‎-da، -dha، -dhā‎؛ اوستایی kaδa، kada «کِی؟» = سنسکریت kadā». تناوب د ~ ذ کاملاً جایگاهی است: دالِ ایرانی باستان در میان دو واکه در اوستایی نو به ذال سایشی بدل شده، ولی املای گاهانی «د» را نگه داشته است. پس پیکان ریشه ← اوستایی درست است، با این توضیح که آنچه از *de-/*do- می‌آید پایانهٔ واژه است نه همهٔ آن.\",\n    \"sources\": [E_TO],\n    \"ref_check\": [\n     {\"ref\": \"POK:182\", \"status\": \"supports\",\n      \"note\": \"Inside the de-/do- entry (pp.181-183; POK_full.txt l.19507 ff.) stands: 'The ending of the following adverbial groups also belongs to this root: Old Indic tadā “then”, Avestan taδa “then”, Lithuanian tadà; Old Indic kadā “when?”, Avestan kada, jav. kaδa “when?”, Lithuanian kadà.' The adverb list sits in the middle of the three-page entry, so a citation to p.182 is right.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. I p.771 (leaf 779)\", \"stance\": \"supports\",\n      \"note\": \"'ai. kada “wann?”, av. kada, jav. kaδa “wann?”, lit. kada “wann”'.\"},\n     {\"src\": \"AVG\", \"where\": \"Jackson, Avesta Grammar §4226-area (AVG.txt l.4226)\", \"stance\": \"supports\",\n      \"note\": \"'Suffix G/YAv. -da, -δa = Skt. -da, -dha, -dhā, Av. yaδa, yaδā “when” = Skt. yadā; Av. kaδa, kada “when?” = Skt. kadā. So Av. aδa “then” = Skt. adha, adhā.'\"},\n     {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch (BRT.txt)\", \"stance\": \"partial\",\n      \"note\": \"the local OCR of Bartholomae is badly degraded (columns interleaved, δ rendered as S/5/b); 'kada' occurs in many quoted Gatha passages (e.g. l.5986 'kada mazdā yōi uxšānō …', l.20478 'kadā mazdā nərəš vīsəṇtī “wann, o M., werden die Ritter die Botschaft verstehen lernen?”'), which confirms the word and its meaning, but the headword entry itself could not be isolated in this scan.\"}\n    ]\n   },\n   {\n    \"id\": 2, \"lang\": \"Persian\", \"words\": \"kay 1\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"New Persian کِی kay 'when?' continues Old Iranian *kadā (= Av. kada/kaδa) through Middle Persian kay: intervocalic Old Iranian -d- became the fricative δ in Middle Persian and then dropped, the resulting *ka-a contracting and the final vowel yielding the diphthong -ay, exactly as Nyberg formulates it (Manual of Pahlavi II, glossary: 'kay < kad; NP kai'). MacKenzie's Concise Pahlavi Dictionary confirms the Middle Persian form and meaning: 'kay [AYMT | N ~] when?'. Horn no. 878 gives the same chain for New Persian, and Mo'in's footnote in the Borhan-e Qate' spells out the comparative dossier. The homograph kay 'king, Kayanid' (Borhan's second sense, Av. kavi-) is a different word, which is why the chart writes «کی ۱».\",\n    \"derivation_fa\": \"«کِی» فارسی نو دنبالهٔ ایرانی باستان ‎*kadā‎ (اوستایی kada/kaδa) از راه فارسی میانهٔ kay است: دالِ میان دو واکهٔ ایرانی باستان در فارسی میانه نخست به ذال سایشی بدل شده و سپس افتاده است و آنچه مانده به دوواکهٔ ‎-ay‎ انجامیده — چنان‌که نیبرگ در واژه‌نامهٔ «راهنمای پهلوی» می‌نویسد: «kay < kad؛ فارسی نو kai». مکنزی نیز صورت و معنای پهلوی را دارد: «kay … when?». هرن در شمارهٔ ۸۷۸ همین زنجیره را می‌آورد و معین در حاشیهٔ «برهان قاطع» پروندهٔ تطبیقی آن را می‌گشاید. «کیِ» دیگر به معنی «شاه، کیانی» (از اوستایی kavi-) واژه‌ای جداست و از همین رو نمودار «کی ۱» نوشته است. ادعای نورایی درست است.\",\n    \"sources\": [W_KAY],\n    \"ref_check\": [\n     {\"ref\": \"BQT:1748\", \"status\": \"supports\",\n      \"note\": \"Verified precisely: Borhan-e Qate' vol. 3 scan, pdf page 545 = printed 1748 (calibrated on the running-head numerals ۱۷۵۱ at pdf 548 and ۱۷۵۲ at pdf 549). That page opens the ک+ی section with 'کی، بفتح اول و سکون ثانی، بمعنی کدام و چه وقت باشد ۸', and Mo'in's footnote ۸ at the bottom reads: 'در اوستا kaδa (چه وقت؟)، هندی باستان kadā (چه وقت؟)، افغانی kala، آسی ked (هرگاه، اگر، آیا)، بلوچی kadi (چه وقت؟)، ایرانی باستان *kadā (چه وقت؟) «بارتولمه»، «نیبرگ … ص ۱۱۷»، کردی kî'. That is Nourai's arrow, with Bartholomae and Nyberg cited.\"},\n     {\"ref\": \"HRN:96\", \"status\": \"not_found\",\n      \"note\": \"Horn p.96 (HRN.txt leaf 118, header '— 96 —') contains nos. 428-432, jev … čāre; there is nothing about kay. The entry Nourai needs is Horn no. 878 on p.196 (leaf 217): '878. (1) kei “wann? wie?” … aw. kada “wann”; ai. kadā “wann?”; afγ. kala; oss. d. t. ked “wenn, ob” (158); bel. kadi “wann?” (182).' The content fully supports the arrow, so '96' looks like a misprint for '196'.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 878, p.196 (HRN.txt leaf 217)\", \"stance\": \"supports\",\n      \"note\": \"'878. (1) kei “wann? wie?” … aw. kada “wann”; ai. kadā “wann?”'.\"},\n     {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD.txt l.426)\", \"stance\": \"supports\",\n      \"note\": \"'kay [AYMT < A ʾymty | N ~] when?' — Middle Persian kay, New Persian the same; a second entry '²kay [kd | N ~] title of the dynasty of Wištāsp … Kayanian' shows the homograph the chart avoids.\"},\n     {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary (NYB_vol2_glossary.txt l.2157)\", \"stance\": \"supports\",\n      \"note\": \"'kay < kad; NP kai' — Nyberg states the very sound history (loss of the intervocalic dental) that the chart's arrow implies.\"}\n    ]\n   },\n   {\n    \"id\": 3, \"lang\": \"Avestan\", \"words\": \"yeth; yathât; dim; dit; -da 5\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"All five items are genuine Avestan and all five really belong to this stem, but one gloss is wrong. (a) 'yeth' = Av. yeδi / yeidi (Nourai's 'th' = δ), the conditional 'if, at the time when' beside Skt yadi, Old Persian yadiy; Walde-Pokorny I 771 glosses it 'zur Zeit als' — literally 'at the time when' — and Nourai's 'at present' is a mistranslation of that German phrase; the word never means 'at present'. (b) 'yathât' = Av. yaθāt 'from where, whence' (WLD I 771 'av. yaθāt “woher”'), correctly glossed. (c) and (d) dim and dit are the enclitic accusative pronouns of the related stem *di-: Jackson, Avesta Grammar, gives the paradigm 'Sg. Acc. dim m. f.; dit n. — Pl. Acc. diš m. f.; dī n. (Ys. 65.8)', i.e. dim 'him/her', dit 'it' — exactly the chart's glosses; Walde-Pokorny I 771 files them here: 'Ein verwandter St. *di in den enklit. iran. Akk. av. ap. dim “ihn, sie”, av. dit “es”, diš pl. m. f., dī pl. n. (Bartholomae 684)'. (e) '-da 5' is the directional enclitic -da of vaēsman-da 'to the house' (Pokorny's very first example under the lemma; Klein p.1622 s.v. to cites 'Avestic -da (as in vaesmen-da, “to the house”)'), Greek -δε, Latin -de. So: four items confirmed, one gloss ('at present') wrong — hence 'plausible' for the node.\",\n    \"derivation_fa\": \"هر پنج صورت اوستایی اصیل‌اند و هر پنج به همین ستاک می‌رسند، اما یک معنا نادرست است. الف) «yeth» همان yeδi/yeidi اوستایی است («th»ی نورایی = ذال)، حرف شرط «اگر، هنگامی که»، هم‌ارز yadi سنسکریت و yadiy پارسی باستان؛ والده‑پوکورنی جلد ۱ ص ۷۷۱ آن را «zur Zeit als» یعنی «هنگامی که» معنی می‌کند و «at present»ِ نورایی ترجمهٔ نادرست همین عبارت آلمانی است؛ این واژه هرگز «اکنون» معنی نمی‌دهد. ب) «yathât» همان yaθāt «از کجا» است و معنایش درست آمده. ج و د) dim و dit ضمیرهای پی‌بستِ رایی از ستاک خویشاوند *di- هستند؛ جکسن صرف آن را می‌آورد: «مفرد رایی dim مذکر و مؤنث؛ dit خنثی — جمع رایی diš؛ dī خنثی»، و والده‑پوکورنی همین‌جا جایشان می‌دهد و به بارتولمه ستون ۶۸۴ ارجاع می‌دهد. ه) «‎-da‎» همان پی‌بستِ سویشی در vaēsman-da «به‌سوی خانه» است که پوکورنی نخستین شاهد مدخل قرارش داده و کلاین در ص ۱۶۲۲ ذیل to نقلش می‌کند؛ برابرِ ‎-δε‎ یونانی و ‎-de‎ لاتین. پس چهار مورد تأیید می‌شود و یک معنا («at present») نادرست است؛ از این رو جعبه با احتیاط پذیرفتنی است.\",\n    \"sources\": [E_TO],\n    \"ref_check\": [\n     {\"ref\": \"POK:183\", \"status\": \"supports\",\n      \"note\": \"The de-/do- entry (pp.181-183) contains both groups: 'compare also Old Indic yadi “if”, Old pers. yadiy, Avestan yeδi, yeidi “as soon as” and Avestan yaδāt “whence”' and 'A cognate stem *di- perhaps in enclitic Iran. Acc. Avestan, Old pers. dim “her, she”, Avestan dit “it”, diš pl. m. f., dī pl. n.' (POK_full.txt, l.19507 ff.). A citation to the last page of the entry, 183, is right. Note Pokorny/WP gloss yeδi 'zur Zeit als / as soon as', NOT 'at present'.\"},\n     {\"ref\": \"KLN:1622\", \"status\": \"supports\",\n      \"note\": \"KLN_1966.txt leaf 860 (= pp.1622-1623; leaf 862 carries the printed numeral 1626), s.v. 'to, prep.': '… from the I.-E. pronominal base *do-, “to, toward, upwards” … Cp. also I.-E. *de in Avestic -da (as in vaesmen-da, “to the house”), Gk. -δε …, and in L. -de (as in inde …, unde …)'. This is precisely the '-da 5 : toward, to' item; Klein says nothing about yeδi, yaθāt, dim, dit.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. I p.771 (leaf 779)\", \"stance\": \"partial\",\n      \"note\": \"supports the forms but corrects the gloss: '(vgl. auch ai. yadi “wenn”, ap. yadiy, av. yeδi, yeidi “zur Zeit als” und av. yaθāt “woher”)'; and 'Ein verwandter St. *di in den enklit. iran. Akk. av. ap. dim “ihn, sie”, av. dit “es”, diš pl. m. f., dī pl. n. (Bartholomae 684)'.\"},\n     {\"src\": \"AVG\", \"where\": \"Jackson, An Avesta Grammar, pronominal paradigm (AVG.txt l.2379)\", \"stance\": \"supports\",\n      \"note\": \"'Sg. Acc. dim m. f.; dit n. — Pl. Acc. diš m. f.; dī n. Ys. 65.8.' — dim 'him, her' and dit 'it' exactly as the chart glosses them.\"},\n     {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch col. 684 (cited by Walde-Pokorny I 771)\", \"stance\": \"partial\",\n      \"note\": \"the local BRT.txt OCR is too degraded to isolate the headword columns (dim appears only in index/citation lines such as l.5244 'dim v V.5.1.'); the reference is therefore taken at second hand from Walde-Pokorny, who cite 'Bartholomae 684' for exactly this set dim / dit / diš / dī.\"}\n    ]\n   },\n   {\n    \"id\": 4, \"lang\": \"Germanic\", \"words\": \"tô\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Proto-Germanic (West Germanic) *tō 'to' continues the o-grade *dō/*do- of this pronominal stem, PIE *d- giving Germanic *t- by Grimm's Law. Watkins states it in one line: 'de-. Demonstrative stem, base of prepositions and adverbs. 1. Germanic *tō in Old English tō, to: TO, TOO. … [Pok. de-, do- 181.]'. Pokorny's own material lists the whole set: 'Old English tō, Old Saxon tō (te, ti), Old High German zuo (za, ze, zi) … Modern High German zu (Gothic du “to” …)', beside Latin do- in dōnec and -dō in quandō and Old Church Slavonic do. The label 'Germanic' on the box is thus right, though strictly the form *tō is West Germanic (Gothic has du, which Brugmann already flagged as unexplained).\",\n    \"derivation_fa\": \"ژرمنی آغازین (به‌دقت: ژرمنی غربی) ‎*tō‎ «به، به‌سوی» دنبالهٔ گونهٔ ‎*dō/*do-‎ همین ستاک اشاره است و «د»ی هندواروپایی بر پایهٔ قانون گریم در ژرمنی به «ت» بدل شده است. واتکینز در یک سطر می‌گوید: «de-، ستاک اشاره … ۱. ژرمنی ‎*tō‎ در انگلیسی باستان tō: TO، TOO». پوکورنی همهٔ خانواده را برمی‌شمارد: انگلیسی باستان tō، ساکسونی باستان tō، آلمانی علیای باستان zuo و آلمانی امروزی zu (گوتیک du)، در کنار ‎do-‎ لاتین در dōnec و ‎-dō‎ در quandō و do در اسلاوی کلیسایی. پس برچسب «ژرمنی» درست است، هرچند به‌دقت این صورت ژرمنی غربی است.\",\n    \"sources\": [E_TO],\n    \"ref_check\": [\n     {\"ref\": \"AHD\", \"status\": \"supports\",\n      \"note\": \"Nourai cites AHD without a page (the IE appendix). AHD_watkins1985.txt l.360: 'de-. Demonstrative stem, base of prepositions and adverbs. 1. Germanic *tō in Old English tō, to: TO, TOO. … [Pok. de-, do- 181.]' — the node and its English child in one sentence.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"POK\", \"where\": \"IEW pp.181-183, s.v. de- do-\", \"stance\": \"supports\",\n      \"note\": \"'Old English to, Old Saxon to (te, ti), Old High German zuo (za, ze, zi …) … Modern High German zu (Gothic du “to” with Dat. …, seems proclitic development from *tō)'.\"},\n     {\"src\": \"KLN\", \"where\": \"1966 ed. p.1622 (leaf 860) s.v. to, prep.\", \"stance\": \"supports\",\n      \"note\": \"'ME., fr. OE. to, rel. to OS., OFris. to, Du. toe, OHG. zuo, zua, zo, MHG. zuo, G. zu, “to”, from the I.-E. pronominal base *do-, “to, toward, upwards”.'\"}\n    ]\n   },\n   {\n    \"id\": 5, \"lang\": \"English\", \"words\": \"to, too\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Old English tō 'in the direction of, as far as' (Etymonline: 'from West Germanic *tō, source also of Old Saxon and Old Frisian to, Dutch toe, Old High German zuo, German zu … reconstructed to be from PIE pronominal base *do- “to, toward, upward” … from demonstrative *de-'). English to and too are one and the same word split in spelling and function: too is the stressed adverbial use of OE tō, and the spelling with -oo, fixed only in the 16th c., marks that stress; Klein: 'too, adv. — ME. to, too, fr. OE. to, adv., identical with to, prep. See to and cp. G. zu, which also unites the meanings to and too.' Hence the chart's single box 'to, too'.\",\n    \"derivation_fa\": \"انگلیسی باستان tō «به‌سوی، تا» از ژرمنی غربی ‎*tō‎ و آن از ستاک ضمیریِ هندواروپایی ‎*do-‎ «به، به‌سوی، رو به بالا» که خود از ستاک اشارهٔ *de- است. «to» و «too» در انگلیسی یک واژه‌اند که در املا و نقش از هم جدا شده‌اند: «too» کاربرد قیدیِ تکیه‌دارِ همان tōی انگلیسی باستان است و املای دوواوی آن تنها در سدهٔ شانزدهم تثبیت شد و همان تکیه را نشان می‌دهد؛ کلاین می‌نویسد: «too قید — انگلیسی میانه to، too، از انگلیسی باستان to قید، همان to حرف اضافه؛ سنجید با zu آلمانی که هر دو معنی را یک‌جا دارد». از این رو نورایی هر دو را در یک جعبه آورده و درست است.\",\n    \"sources\": [E_TO],\n    \"ref_check\": [\n     {\"ref\": \"None\", \"status\": \"not_checked\",\n      \"note\": \"The node carries no reference in the book (refs=None); its parent Germanic node cites AHD, whose entry 'de- … Germanic *tō in Old English tō, to: TO, TOO' covers this child directly.\"}\n    ],\n    \"consulted\": [\n     {\"src\": \"KLN\", \"where\": \"1966 ed. pp.1622-1623 (leaf 860), s.vv. to, prep. and too, adv.\", \"stance\": \"supports\",\n      \"note\": \"'to, prep. — ME., fr. OE. to … from the I.-E. pronominal base *do-'; 'too, adv. — ME. to, too, fr. OE. to, adv., identical with to, prep. … Cp. G. zu, which also unites the meanings to and too.'\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. de-\", \"stance\": \"supports\",\n      \"note\": \"'1. Germanic *tō in Old English tō, to: TO, TOO.' — both English words listed as derivatives of this root.\"},\n     {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary\", \"stance\": \"silent\",\n      \"note\": \"not consulted usefully: the Concise Skeat's entries for such function words give only the Germanic cognates, nothing that bears on the Avestan/Indo-European side.\"}\n    ]\n   }\n  ]\n }\n ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-110.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(doc,f,ensure_ascii=False,indent=1)\n    f.write(\"\\n\")\nprint(\"ok\")\n"
}
```


### [2026-09-05T17:46:36.930Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk110.py (file state is current in your context — no need to Read it back)
```


## [2026-09-05T17:46:44.389Z] TOOL CALL #82: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk110.py && python3 -m json.tool data/verification/page-110.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 110"
}
```


### [2026-09-05T17:46:49.434Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 15/15
node verdicts: {'transcription_suspect': 1, 'confirmed': 12, 'plausible': 2}
root verdicts: {'plausible': 1, 'confirmed': 2}
ref checks: {'partial': 1, 'not_checked': 4, 'supports': 12, 'not_found': 1}
books consulted: {'supports': 29, 'silent': 8, 'partial': 5} | by book: {'KLN': 8, 'WLD': 4, 'AHD': 4, 'MON': 3, 'BQT': 3, 'PHD': 3, 'PLA': 2, 'AFA': 2, 'SKT': 2, 'AVG': 2, 'BRT': 2, 'FSD': 1, 'SYN': 1, 'LAT': 1, 'LEW': 1, 'HRN': 1, 'NYB': 1, 'POK': 1}
```


## [2026-09-05T17:47:09.595Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-110.json` written; `verify_check.py 110` reports 15/15 nodes, 0 PROBLEM lines.

**Page 110 (book p. 80) — 3 entries, 15 nodes**
- Node verdicts: confirmed 12, plausible 2, transcription_suspect 1. Root verdicts: confirmed 2, plausible 1.
- Ref checks: supports 12, partial 1, not_found 1, not_checked 4. Books consulted: 42 lookups across 18 titles.

**Flagged items**
- `transcription_suspect` — D.b.r, Arabic node, third word **`z.b.n : bee`**: the printed page (verified at 300 dpi, copied to `data/verification/sources/refs/ocr/BOOK/110.png`) really reads `z.b.n`, so `error_in: "book"`. There is no Arabic root z-b-n 'bee' (زبن = 'to push away'); the root of زنبور is z-n-b-r. Author's misprint, extraction faithful.
- `plausible` root — **D.b.r "to buzz; he spoke; word"**: this is Klein p.406 verbatim, but modern Semitic lexicography reconstructs Proto-Semitic *dVbr- 'bee' and does not derive it from the verb 'to speak'; the d/z correspondences are irregular (Heb. dəḇōrā vs Aram. zibbūrā, Arab. zunbūr).
- `plausible` node — **Persian dām ← Sanskrit dāman**: right root, wrong direction. dām descends via Proto-Iranian *dáHma > MP dām (MacKenzie p.24), a cognate of Skt dāman-, not a borrowing from it.
- `plausible` node — **Avestan "yeth : at present"**: form is real (Av. yeδi/yeidi), but the gloss mistranslates Walde-Pokorny's German "zur Zeit als" ('at the time when'); it never means 'at present'. Other four items in the box (yaθāt, dim, dit, -da) confirmed.

**Reference-number slips in the book (not extraction errors)**
- `HRN:96` → the kay entry is Horn no. 878, **p. 196**; p. 96 has nos. 428-432 (jev … čāre). Likely a misprint for 196.
- `KLN:440` → Klein's *diadem* is on **pp. 442-443** (1966 two-vol. ed., leaf 242); leaf 241 carries the printed 440/441.
- `BQT:1748` verified exactly (vol. 3 scan pdf p. 545 = printed 1748, calibrated on running heads ۱۷۵۱/۱۷۵۲); Mo'in's footnote 8 there gives Av. kaδa, OIr. *kadā, citing Bartholomae and Nyberg.

**No extraction errors found** — the JSON matches the printed page everywhere I checked. One layout note for the owner: entry 2 has a large **completely empty box** on the printed page (right of the second Avestan node) with no label or text; it is a typesetting artefact of the book, correctly omitted from the JSON.

9 web sources archived via `fetch_source.py` (Wiktionary زنبور / דבורה / *deh₁- / دام / دیهیم / διάδημα / کی, Etymonline diadem + to).
