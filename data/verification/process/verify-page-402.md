# Verification process log — verify-page-402


## [2026-09-14T00:52:58.228Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 402 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-402.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-402.json. Write /home/sfmqrb/git/rishe/data/verification/page-402.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 402` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:52:59.333Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T00:53:00.236Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:53:00.254Z] TOOL RESULT

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


## [2026-09-14T00:53:00.738Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-402.txt"
}
```


### [2026-09-14T00:53:00.758Z] TOOL RESULT

```
1	=== PDF page 402 (book page 372) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Peuk, Pug : to prick  (refs POK:828)
4	#1 (parent #0) [Avestan] refs=SNS:175; HUB:73 | spôz : to pull out, remove, also hesitate
5	  #2 (parent #1) [Pahlavi] refs=HRN:156 | spož, spôxtan : to pierce, pull out | NOTE: HRN is not certain about the link with Latin word "pungere"
6	    #3 (parent #2) [Persian] refs=BQT:1091; FSF:221 | sepŭxtan «سپوختن ۱ ( اسپوختن ۱ ، سپوزیدن )» : to pierce, throw in, pull out
7	  #4 (parent #1) [Pahlavi] refs=SNS:175 | spôzed : hesitate
8	    #5 (parent #4) [Persian] refs=BQT:1091; FSF:221 | sepŭxtan «سپوختن ۲ ( اسپوختن ۲ )» : to hesitate, delay ; sepŭz-gâr «سپوزگار» : one who hesitates ☞Kwer
9	#6 (parent #0) [Latin] refs=AHD | pungere : to prick
10	  #7 (parent #6) [English] refs=AHD | puncture ; pivot, point, punctuate
11	    #8 (parent #7) [Persian] refs=MON:822 | pančar «پنچر» : punctured, flat (tire)
12	--- entry 1 ---
13	ROOT Pî -> redirect to Pô 2
14	--- entry 2 ---
15	ROOT Pikho -> redirect to Piko
16	--- entry 3 ---
17	ROOT [Indo-European] Piko, Pikho : lump, knot  (refs POK:830; WLD2:70)
18	#1 (parent #0) [Avestan] refs=POK:830; WLD2:70 | pixa : knot, ball ; nava-pixem : a stick with nine knots used in Zoroastrian ceremonies.
19	  #2 (parent #1) [Pahlavi] refs=SNS:143 | pĕxak : a stick with none knots
20	    #3 (parent #2) [Persian] refs=MON:880 | pîxtan «پیختن» : to wrap up in a bundle
21	  #4 (parent #1) [Sogdian] refs=SOD:335 | pyx : knot
22	
```


## [2026-09-14T00:53:03.730Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-402.json",
 "description": "Read source JSON for page 402"
}
```


### [2026-09-14T00:53:03.777Z] TOOL RESULT

```
{
  "pdf_page": 402,
  "book_page": 372,
  "entries": [
    {
      "root": {
        "name": "Peuk, Pug",
        "lang": "Indo-European",
        "refs": "POK:828",
        "gloss": "to prick"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "SNS:175; HUB:73",
          "words": [
            {"translit": "spôz", "gloss": "to pull out, remove, also hesitate", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:156",
          "words": [
            {"translit": "spož, spôxtan", "gloss": "to pierce, pull out", "script": null}
          ],
          "note": "HRN is not certain about the link with Latin word \"pungere\"",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1091; FSF:221",
          "words": [
            {"translit": "sepŭxtan", "gloss": "to pierce, throw in, pull out", "script": "سپوختن ۱ ( اسپوختن ۱ ، سپوزیدن )"}
          ],
          "note": null,
          "quote": {"text": "ولی را گاه نِه بر گاه بنشان - عدو را چاه کن در چاه بسپوز", "poet": "Sŭzanî"}
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:175",
          "words": [
            {"translit": "spôzed", "gloss": "hesitate", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:1091; FSF:221",
          "words": [
            {"translit": "sepŭxtan", "gloss": "to hesitate, delay", "script": "سپوختن ۲ ( اسپوختن ۲ )"},
            {"translit": "sepŭz-gâr", "gloss": "one who hesitates", "script": "سپوزگار", "see": ["Kwer"]}
          ],
          "note": null,
          "quote": {"text": "نه مرگ از تن خویش بتوان سپوخت - نه چشم جهان کس به سوزن بدوخت", "poet": "Ferdowsî"}
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "pungere", "gloss": "to prick", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "puncture", "gloss": null, "script": null},
            {"translit": "pivot, point, punctuate", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON:822",
          "words": [
            {"translit": "pančar", "gloss": "punctured, flat (tire)", "script": "پنچر"}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Pî",
        "redirect": "Pô 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Pikho",
        "redirect": "Piko"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Piko, Pikho",
        "lang": "Indo-European",
        "refs": "POK:830; WLD2:70",
        "gloss": "lump, knot"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:830; WLD2:70",
          "words": [
            {"translit": "pixa", "gloss": "knot, ball", "script": null},
            {"translit": "nava-pixem", "gloss": "a stick with nine knots used in Zoroastrian ceremonies.", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:143",
          "words": [
            {"translit": "pĕxak", "gloss": "a stick with none knots", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:880",
          "words": [
            {"translit": "pîxtan", "gloss": "to wrap up in a bundle", "script": "پیختن"}
          ],
          "note": null,
          "quote": {"text": "زبالا برایشان درم ریختند - زمشک و زعنبر همی پیختند", "poet": "Ferdowsî"}
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:335",
          "words": [
            {"translit": "pyx", "gloss": "knot", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T00:53:05.893Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','AHD','HUB','HRN','SNS','BQT','FSF','MON','SOD','PHD','NYB','KLN','ARY','BRT']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n\"",
 "description": "Check refs_online entries"
}
```


### [2026-09-14T00:53:07.058Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
```


## [2026-09-14T00:53:13.355Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -100",
 "description": "List local reference files"
}
```


### [2026-09-14T00:53:13.393Z] TOOL RESULT

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
SKT_dli_revised.txt
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
```


## [2026-09-14T00:53:14.187Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T00:53:14.249Z] TOOL RESULT

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


## [2026-09-14T00:53:19.254Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['POK']['page_offset'])\nprint(d['POK']['lookup_hint'])\nprint(d['SNS'].get('page_offset'))\nprint(d['SNS'].get('lookup_hint'))\nprint(d['FSF'].get('page_offset'))\nprint(d['SOD'].get('page_offset'))\nprint(d['HUB'].get('lookup_hint'))\nEOF"
}
```


## [2026-09-14T00:53:20.118Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"peuk\" POK_full.txt | head -30; echo ---; grep -n \"pungere\" POK_full.txt | head -20"
}
```


### [2026-09-14T00:53:20.292Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking
printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
```


### [2026-09-14T00:53:20.499Z] TOOL RESULT

```
69242:Root / lemma: puk-1, peuk- 
69248:fuhslox' etc.; Lithuanian paustis " animal hair '; russ.-poln. puch ( *peukso-, poukso-) 
69255:Alb. suggests that Root/ lemma: puk-1, peuk-: (thick-haired, *fox) is a reduced root of 
---
```


## [2026-09-14T00:53:24.389Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 82[6-9]\" POK_full.txt | head; echo ---; grep -n \"Page(s): 83[0-2]\" POK_full.txt | head"
}
```


### [2026-09-14T00:53:24.467Z] TOOL RESULT

```
67460:Page(s): 828 
67481:Page(s): 827 
67511:Page(s): 827 
67518:Page(s): 827 
67524:Page(s): 828 
67575:Page(s): 828 
67603:Page(s): 829 
67840:Page(s): 827 
67878:Page(s): 829 
---
67933:Page(s): 830 
67947:Page(s): 830 
67967:Page(s): 830 
67985:Page(s): 830 
68011:Page(s): 830 
68027:Page(s): 831 
68061:Page(s): 831 
68129:Page(s): 831-832 
68162:Page(s): 832-833
```


## [2026-09-14T00:53:25.178Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==828+8' POK_01.txt | head -80"
}
```


### [2026-09-14T00:53:26.215Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:53:28.362Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '67520,67610p' POK_full.txt"
}
```


### [2026-09-14T00:53:28.440Z] TOOL RESULT

```
Root / lemma: peua- 
See also: s. pu-2. 
Page(s): 828 



Root/ lemma: peuor, pur, Gen. pu-n-es, Lok. puuen/{Nom. -r-, Gen. -n- inanimate 

formant) 

Meaning: fire 

Note: with multiple equalization of the r-and /74orms and of vocalism 

Material: Armenian hur{Gen. hroy} "fire' {*pur-), hn-oc'oven' {*pun-)\ gr. nup, nup6(; "fire", 

wherefore nupa 'Feuerstatte, stove, hearth, pyre, stake', nupsTOc; m. "fever", nupa6(; m. 

"Brandfacker, korinth. flupFoq 'Pferdename' (*" feueirot '), nuppoq, poet, nupaoq " 

feuerrot ' fnupoFoc;); 

Maybe lllyrian TN Pirustae (Pipustae) 

Umbrian p/rl\re' ( *pu/), Akk. purom-e^\ns fire' ( *pur-), Oscan aasaf purasiaf^ in 

f . . . , 
araigniana ; 

Old Icelandic furrvn. "fire' {*pur-) and fyrr, fyr'r. Old High German Old Saxon Old Frisian 
fiur{*peurJ)\ Old High German older /^^//'(disyllabic, compare Musp. vugii). Old English fyr 
(from Lok. *puueri)\ 

Gothic /5/7"fire' {*pudn). Gen. Dat. funins, /Z//7//7 (latter from * puneni, a hybridization from 
*puueni: *pun-es). Old Icelandic funim. "fire'; Old High German funko. Middle English 
/b/7/re "spark'; with ablaut ( *puon-) Middle Low German Ka/7/re "spark'; 

Maybe lllyrian TN Perestae (Penestae) 

Old Prussian pannolke', panu-stac/an TeuerstrahV {*puon-u), loanword Finnish panu 
"fire'; 

Slavic *pur/a-m. 'glowing ash' in Czech pyrm. and pyr/n. 6s.; in addition Old Czech 
pynna' favilla ', Czech pyre f/" g\o\N' , serb. ^p/>7//"anfachen' etc.; 



Hittite pahhur, pahhuwar, Dat. pahhu(e)ni^\\x€\ Tocharian A por, B puwar, pwards. 

Note: Hittite used reduplicated -Z?/?- for voiced laryngeals!! 

References: WP. II 14 f., WH. II 391, Trautmann 206, 232, Benveniste Origines 1,10; 
Pedersen Hittite 187f. 
Page(s): 828 

Root / lemma: pezd- 

Meaning: to break wind 

Note: (compare 'joe/'o'- 'loudly fart ') 

Material: Gr. p5£U) "leise einen streichen lassen' from *pz5£U) (reconverted with metathesis 

from *pezdd}, wherefore p56-Ao(; " fetidness ' with new formationer ograde, and *p5£-Au-(; 

"pedens, scornful, ridiculing' in BSeAu-kAewv 'Cleontloppedens', as well as as base from 

(35£Aup6(; "disgusting", ^bzK\}aao\xa\ "verabscheue, empfinde disgust, repulsion, loathing ', 

(35uAAiJL) 'verabscheue, dread', but also "p5£U)'; Latin pedo, -ere ' fart ' ( *pezdd), podex'Vne 

Hintere' {*pozd-ek-s), ped/'s louse' (because of Demin. ped/cu/us o\der *pede^] 

kir. pezd/ty and zero grade (proto Slavic *bbzd-) bzdfty, russ. bzdetb 'leise einen 
streichen lassen', sloven, pezdeti, Lithuanian bezdu, bezdeti, Latvian bezdetleise einen 
streichen lassen', Lithuanian b /zdas ^ podex' , b /zdz/us ' Stanker'; Baltic *bezdet/based on 
auf 'yozo'e// besides *pezdetr, perhaps handelt es sich also um contamination with the root 
bhes-'blow', above S. 146. 

References: WP. II 68 f., WH. II 272 ff., Trautmann 221 ; 
See also: compare above pes-1. 
Page(s): 829 

Root / lemma: ped-1, pod- 
Meaning: container, vessel 

Material: Old Indie perhaps pa/Za-m. 'Kornbehalter', pa///" grain measure' (whether -//-from 
-dl-)\ Old High German fazzon. Middle High German vazzen^\v\ ein vessel tun, catch, 
riJsten, sich bekleiden'. Old High German fezzil. Middle High German i/ezze/'band, strap,
```


## [2026-09-14T00:53:28.964Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '67925,68030p' POK_full.txt"
}
```


### [2026-09-14T00:53:29.013Z] TOOL RESULT

```
Nom. PI. /ic/a/>7 "throes of childbirth, pain'; die Middle Irish inflection goes auf Old Irish a- 

inflection back, as e.g. Middle Irish pe/'s^ "person' auf Old Irish persan, the Old Irish Nom. 

Sg. muft consequently *idan{*pidun^ gelautet have. 

References: WP. II 70; compare Feist 155 f. 

Page(s): 830 



Root / lemma: pik(h)o- 

Meaning: lump, knot 

Material: Avestan yO/A'5- "knot' in nava-pixem "neunknotigen'; Latvian piks, pika^E.x6- and 

Lehmklumpen', sniega-pika "Schneeballen'. 

References: WP. II 70. 

Page(s): 830 

Root / lemma: pi-lo- 

Meaning: hair, felt 

Note: 

Root / lemma: pi-lo- : hair, felt, : Root / lemma: pu-lo- : "hair, felt ' derived from Root / 

lemma: pel-2a, pela- : pla- : to cause to move, drive, felt. 

Material: Latin pilus m. "hair', whereof as collective "Haarknauel' also pilai. " ball, bale, 

Strohpuppe'; auf an 5-stem based on 'yO/T-s-os "verfilzf, in gr. mkoc, m. " felt ', ttTAsoj "filze', 

Latin pilleus, -ei//77 "Filzkappe, FilzmiJtze' ( *pilseio-)\ Old Church Slavic pl-bstb " felt '. 

References: WP. II 71, WH. II 302 f., 304 f. 

Page(s): 830 



Root / lemma: pi-n- 

Meaning: a piece of wood 

Material: Old Indie /0/>75/r5-/77 'staff, stick, club, mace, joint'; gr. iTiva^, -qkoc; 'Sparre, balk, 

beam, board, Schreibtafel, Gemalde'; Old High German witu-f?na\.. Middle Low German 

K/>7e"Holzhaufen'; Old Church Slavic ptnt m., serb. panjeic. "tree truck, -strunk'. 

References: WP. II 71; Vasmer2, 335; 

See also: probably to spei- "sharp, pointed bit of wood'. 

Page(s): 830 

Root / lemma: pTp(p)- 

Meaning: to squeak 

Note: also unredupl. pA-with variant derivatives, onomatopoeic word 

Material: Old Indie pippaka "ein certain bird', pippTka- "ein bird'? gr. nTno(; f. or ninTTO(; m. 

"young bird', nlncb, nirrpa f. "a kind of Baumhacker', nin(n)i^u) "piepe'; Latin pTpilo, -are, 

pTpio, -Tre, pTpo, -^/'e"piepen', pip(p)itare^oi Naturlaut the Mause', pTpulum^ ^qs Wimmern', 

Oscan yC>//75//c» "clamor plorantis'. Modern High German (Low German) piepen {\n\Vc\ 

verhinderter consonant shift); Lithuanian yOyyO//"whistle' (loanword?); Czech pipteti 

"piepsen', sloven, pfpa^ chicken; duct, tube, pipe', serb. pipa, eine disease, malady of the 

chicken ' (Modern High German Pips) etc.; 

Czech yC>//ra//"piepen', ; Bulgarian pile, Serbo-Croatian /7//e"Kuchlein' ; similarly alb. bibe 
"young water bird ', Armenian i6'/Z?e/77"pigolare', gr. nicpiy^, ni(paAAi(; "a bird'. 

References: WP. II 70, WH. II 309; Vasmer2, 363 f. 
Page(s): 830 

Root / lemma: pTzda- 

Meaning: vulva 

Grammatical information: f. 

Material: Alb. pith {pidiii) m. "vulva'; cak. pizda, russ. pizda, poln. pizda^s., out of it 

borrowed (?) Lithuanian pyzda, Latvian pTzdai. ds., and Old Prussian peisda ' Arsch' . 

References: WP. II 69, Trautmann 21 1 ; 

See also: compare also pezd-S. 829. 

Page(s): 831 

Root / lemma: p/ab- 
Meaning: to babble, etc..
```


## [2026-09-14T00:53:35.943Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: peuk\\|lemma: peug\\|lemma: peuk-\\|peukjoi\\|Meaning: to prick\" POK_full.txt | head -20"
}
```


### [2026-09-14T00:53:35.993Z] TOOL RESULT

```
11196:Meaning: to prick, pierce 
16741:Meaning: to prick; tick 
29932:Meaning: to prick, bite 
53131:Meaning: to prick; to drill, sharpen
```


## [2026-09-14T00:53:36.594Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '67440,67520p' POK_full.txt"
}
```


### [2026-09-14T00:53:36.644Z] TOOL RESULT

```
Meaning: to stick; to punch 

Material: 1. peuR- gr. *n£UKOc; n. "cusp, peak, sting, prick' in gr. nspi-nsuKsc;, hom. ex£- 

n£UK£(; "with a cusp, peak versehen'; n£UK£5av6(; " pricking, wounding', later "bitter', 

n£UKaAi|jO(; "sharp, eindringend'; 

here as "die stechende' das root nouns peuR-. puR-i\r, spruce' in gr. TT£UKr| f. ds., thrak. 
PN n£UKr|, lllyrian VN Peucetii, Middle Irish ochtachi. {*puRtaka) "fir, spruce, spear, 
javelin'; Old High German fiuhta, asachs. fiuhtia ( *fiuhtjdn) "fir, spruce'. Old Prussian peuse 
f. "pine tree' (Baltic *piause), zero grade Lithuanian pus/si., Gen. PI. pusi], East Lithuanian 
Nom. PI. p^ses (conservative stem). 

2. peug-. gr. ttu^ Adv. "with the fist', nuypn f. "fist, Faustkampf, nuyfjaTo(; "eine Faust 
high, dwarf', nuycbv, -6vo(; m. "ulna, ell', nuy-paxo(;, nuKTr|<; "Faustkampfer'; Latin pugil 
ds., pugnusvn. "fist', pugno, -a/ie "fight', pungo, -ere, pupugl punctum^ prick ', pugioxn. 
"dagger'. 

References: WP. II 15, WH. II 383 f., Trautmann 232, Specht Indog. Dekl. 57 f. 
Page(s): 828 

Root / lemma: peu-1, peuQ- : pu- 
Meaning: to clean, sift 



Material: Old Indie Trans, punati, Med. yoai/a/e "purifies, cleans, lautert (sich)', pavitum; 
pavltar-, p6tar-rc\. "Reiniger, Lauterer', yC>5i//?/'5/r7"Lauterungsmittel, Seihe, sieve '; pavana- 
"reinigend', pavaka-(d\so pavaka-) ' pure, candid ' = Middle Persian pavag, np. pak^ 
candid, pure'; Old Indie pJ/a- "pure", puti-i. " cleaning, purification '; Avestan puitika-^-Lux 
Lauterung dienend'; 

Latin purus'pure' (formation as cla-ru-s), purgo, o\der pur/go, -are^c\ear\'; putus^pure', 
nepus'non purus' {*neput-s)\ putare'c\ear\, clean'; Middle Irish J/-"new, fresh, noble', 
cymr. /A'fresh, green'; Old High German fowen. Middle High German voewen^ sieve, corn, 
grain clean' {*fawjan= Old Indie /Oai/5ya//"purifies, cleans, lautert'); 

doubtful gr. nruov, ttteov " throw shovel ' (: Old High German fowerR). 

References: WP. II 13, WH. II 390 f. 
Page(s): 827 

Root / lemma: peu-2 

Meaning: to research, to understand 

Material: Gr. vn-niO(; (*vr|-nF-iO(;) and vr|-nu-TiO(; ' injudicious, kindisch', nivuT6(; 'smart', 

nivupisvnv auv£Tr|v Hes. (due to eines present *ni-vO-[ji from *nu-vO|ji); Latin puto -are 

{putare) "to cleanse, clear; of trees, to lop. Transf. to clear up, settle, esp. of accounts; 

hence, to weigh up, ponder, reckon, estimate; to consider, believe, think'; Old Church 

Slavic is-py-th "perscrutatio', pytajg, -a//'scrutari, quaerere'. 

maybe alb. {*peus) pyes'ask questions', pye^e 'question' : gr. iruaTK;, nsOoK^f. "question'. 

Proto-Slavic form: pytati: Old Church Slavic: py/a// examine, scrutinize' [verb], Russian: 
yoy/^/'' torture, torment, try for' [verb], Slovak: pytat'^asV! [verb], Polish: pytac^asV! [verb], 
Serbo-Croatian: pftati^diSV! [verb], Slovene: pftati^asV! [verb]. Other cognates: Latin putare 
"cut off branches, estimate, consider, think' [verb]. 

Note: 

From Root/ lemma: b'^eudh-, nasal. b'^u-n-6'^-\ "to be awake, aware' derived Root/ 
lemma: peu-1, peua-. pu-\ "to clean, sift' , Root/ lemma: peu-2\ "to research, to 
understand' (see above). 

References: WP. II 13 f.; different Schwyzer Gr. Gr. 1, 6962. 
Page(s): 827 



Root / lemma: peu-3 
Meaning: " foam ' 
See also: see below pu-1, S. 847. 
Page(s): 827
```


## [2026-09-14T00:53:43.034Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '67425,67445p' POK_full.txt"
}
```


### [2026-09-14T00:53:43.103Z] TOOL RESULT

```
' {*petra)\ Old High German fettah. Middle High German vittich. Middle Low German 
vit(te)k. Modern High German Fittich; 

Hittite pattaru.. Gen. PI. paddanas^ muo^'. 

*ptei-, pti-i^r. irTaiw "stofte an etwas (intr.), strauchle, irre, have whereas misfortune' 
(nraiaw, Enraiapai, sniaiaGriv), rare tr. "bump, poke, umstijrzen', nraTaija "damage, loss, 
misfortune, beating ', iGunfiwv "geradaus fliegend' (probably actually "geradaus treffend = 
pushing, thrusting, aufschlagend'), nriAov " feather, Flaumfeder'. 

References: WP. 1119 ff., WH. II 282 f., 297 f. 
Page(s): 825-826 

Root / lemma: peuR- and peug- 

Meaning: to stick; to punch 

Material: 1. peuR- gr. *n£UKOc; n. "cusp, peak, sting, prick' in gr. nspi-nsuKsc;, hom. ex£- 

n£UK£(; "with a cusp, peak versehen'; n£UK£5av6(; " pricking, wounding', later "bitter',
```


## [2026-09-14T00:53:44.523Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"spaz\\|spuz\\|spōz\\|spōxtan\\|spoxtan\\|sipōxtan\\|sipuxtan\" CHEUNG.txt | head -40"
}
```


### [2026-09-14T00:53:44.564Z] TOOL RESULT

```
23178:/spöxtag/, MMP 'spwxt; Inf.: BMP spwhtn /spoxtan/ 
52422:spuz-el, 354
```


## [2026-09-14T00:53:47.169Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23120,23230p' CHEUNG.txt"
}
```


### [2026-09-14T00:53:47.222Z] TOOL RESULT

```
Y Av. auui.spasta- (Yt 13.69). 0 For YAv. hisposant- cf. Kellens 1974: 115f. 


*MIDDLE PERSIAN: MMP ons ‘to serve’, MMP ‘sp’s, ВМР sp’s /späs/ ‘service, 


gratitude, thanks’ (LW) = DMMPP: 86 

Pres.: IND. 3sg. ‘spsyd 

*PARTHIAN: ‘sps- ‘to serve’, ’sp’s, sp’s ‘service’ || (+ *pati-) ? pdysp’s- ‘to pay 
attention’ — Ghilain: 51 f., 69 | DMMPP: 86 

Pres.: IND. 3р]. ‘spsynd; Partic.: perf. pass. ‘spyst 

*KHOTANESE: späs(S)- (sas-, s(p)as-) ‘to see; appear = SGS: 135 

*SOGDIAN: BSogd. ’sp’ys, BSogd. ’spys, CSogd. spys/spxs, MSogd. ’spys ‘to serve, 
honour, pay respect’, BSogd. ’sp’s, sp’s ‘service, honour’ || (+ *ham-) MSogd. 
"nspstqy, MSogd. ’spstky’, SSogd. ’nsp’st’ky’kh, SSogd. ’nspst’kyh ‘zeal, 


354 *spauc ? 


willingness to serve’. 9 The pret. stem (’)spxst- has given rise to a secondary pres. 
stem (CSogd.) sp(’)xs- (GMS: par. 599). 

Well attested Pres.: IND. 3sg. BSogd. 'sp'ysty,'spysty, 3р1. dur. SSogd. ’spys’nt ’skwn, SUBJ. 35р. 
BSogd. ’spys’t, etc. 

*BACTRIAN: OTIO-, MOTLO-, CATO- ‘to serve, worship’, «слтосо, OTAGO ‘service’ 
c» S-W, Bact.: 224b 

*NWIR: NP sipas ‘kindness, favour, thanksgiving’, NP sipasidan/sipas- (denomin.) 
*to praise (God) for benefits received; to implore assistance, grace, favour? 

*MISC: Arm. (LW) spasem ‘to serve’ (« WIr.), Toch. (LW) spaktam ‘service’, A 
spaktanik, B spaktanike ‘servant’ (< Bactr., cf. Schwartz 1974: 411). 

*SANSKRIT: spas ‘to observe, watch, spy’ (RV) || ("s-less" var.) pas ‘to see’ (RV+) 
= EWAia II: 107 

«PIE *speK- ‘to look around, take notice’ = LIV: 575 f. | Pok.: 984 

*IE COGNATES: Gr. скёлторол ‘I look around, look at’, Lat. speciö ‘to see’, OHG 
spehon, NHG spähen ‘to spy’ 

*REFERENCES: DKS: 436b f.; Werba 1997: 430 f., 233 


*spaué ? ‘to thrust; verstoßen’ 

*MIDDLE PERSIAN: MMP ‘spwx- (pret. stem), ВМР spwc- /spöz-/ ‘to reject, thrust, 
throw out’; to overstep (the boundaries); to disobey, evade (a command)’ 
c DMMPP: 87b 

Pres.: IND. 3sg. BMP spwoyt /spozed/, SUBJ. 3sg. BMP ѕрис t /spozad/; Partic.: perf. pass. BMP spwhtk 
/spöxtag/, MMP 'spwxt; Inf.: BMP spwhtn /spoxtan/ 

*KHOTANESE: (+ *fra-) OKh. haspäs- ‘to strive’, Khot. haspij- (caus.) ‘to urge’. © 
See also *spaié. = SGS: 151 

*NWIR: NP sipöxtan/sipöz- ‘to prick, pierce, transfix, thrust, poke; to draw forth one 
thing from another’ 

*MISC: Arm. (LW) spuZ-el ‘to postpone, delay, procrastinate’ 

© Further (DIr. cognates are unknown. An IE origin cannot be ascertained. 


*srai ‘to lean’ 

*AVESTAN: YAv. sri- ‘to lean’ || (+ *apa-) ‘to turn away from, averse from’ || (+ 
*upa-) ‘to lean upon [intr.]’ || (+ *ni-) ‘to bring to, assign’ — Liste: 66 

Pres. {1} nu-: IND. 15р. YAv. nisrinaomi (V 18.51), 3sg. YAv. nisrinaoiti (Yt 10.27), INJ./IMPV. 2pl. 
YAv. nisrinaota (Yt 13.34), SUBJ. 2sg. them. YAv. nisirinauuähi (Yt 5.87), OPT. 3sg. YAv. nisirinuiiat 
(V 3.20, ViD 2); Pres. {2} them.: INJ. med. 35р. YAv. ира... sraiiata (Yt 17.21), IMPV. 25р. ҮАУ. upa... 
sraiian'ha (Yt 17.21); Fut.: IND. 3sg. YAv. sraesiieiti (V 8.34); Aor. athem.: INJ. med. 3sg. YAv. nisrita 
(Y 65.11); Perf.: IND. 35р. ? YAv. sisraiia (Vyt 51); Partic.: pres. {2} med. YAv. apa.sraiiamna- (Yt 
13.26), fut. ҮАУ. sra@Siiant- (У 8.34), aor. med. Y Av. sraiiana- (V 3.29, Vyt 36), perf. pass. YAv. srita- 
(Е 531), YAv. apa.srita- (N 78), Y Av. nisrita- (N 10); Caus.: SUBJ. 2sg. YAv. nisraraiia (V 18.51) 


*srais 355 


*OLD PERSIAN: (+ ni-) niyagär- ‘to restore’ — Kent: 188b 

Caus.: impf. IND. 1sg. niyacarayam <n-i-¢-a-r-y-m> (DB 1.64) 

*MIDDLE PERSIAN: (+ *ni-) BMP ns’y /nisay/ ‘conveying, dispatch’ 

*KHOTANESE: Q LKh. ssaidä, assigned by Bailey (DKS: 412a f.) to *srai, has a 
different etymology, on which see *srai8. 

*CHORESMIAN: (+ *apa-) bs’ry- ‘to reject, decline’ = Samadi: 25 

*NWIR: Gz. särt, Siv. sid ‘staircase, ladder’ (< "OP" *¢(a)ita- < Ir. *sr(a)ita-) 

*NEIR: Pash. sal (m.) ‘stair (built of stone or earth)’, Yzgh. Хаа ‘ladder [pieced 
together]’ || (+ *us- ?) Pash. sayal/Sayam ‘to reject, repudiate’, ? Sh. soxis- ‘to slip’ 
(formally difficult), ? Sh. Хоу, Rosh. xüy, Bart. Xüy ‘moraine of large boulders’ || (+ 
*ui-) ? Pash. waxedal ‘to slip (from the hand)’, Sh. (Baj.) wixi(y)-/wixid, Rosh. 
wiXay-/wixid, Bart. wixi-/wixid, Yzgh. x"ay-/x'ad ‘to open, unlock’, Wa. 
WBIS(b1)y-/Wbis(o)n- ‘to untie, loose, release’. Ф As for Wa. wbis(bi)y-/wbris(o)n- cf. 
Steblin-Kamenskij 1999: 403: "We note that Wa. ъы$(ы)у- can go back 
phonetically impeccably to Old Ir. *ui-, *aua-srai(a)-". 

*SANSKRIT: sray ‘to lean against’ (RV+) = EWAia II: 665
```


## [2026-09-14T00:53:59.959Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 177 (p.156) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==178' HRN.txt | head -60"
}
```


## [2026-09-14T00:54:00.848Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB leaf 84 (p.73) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==84' HUB.txt | head -60"
}
```


### [2026-09-14T00:54:00.982Z] TOOL RESULT

```
=== HRN leaf 177 (p.156) ===
— 156 —
aw. spereza- 'Milz' (ZPGl.) ; pblv. spärz; ai. pWidn-
*Milz\
703. siperl Vollendet', isperl .(Sahn. II, 820 Vers 866).
aw. "^usjjerena-, tis- 4- {/'par- ; LW. chald. N^löDN,
arm. spar.
de Lagarde, Semitica 45. Unsicher, vergl. np.
supürden (No. 697).
704. 8ipe7iJ 'RuhepVdtz, Gasthaus' (8ähn. I, 229 Vers 1791).
plilv. «5paw/ 'Ruheplatz, Asyl' (Men. ; AV.), spun-
jänaklh, arm. LW. aspnjakan Gast', cliald. syr. LW.
rr^'N, prSK^N 'Gasthof, Gasthofbesitzer (de Lagarde,
Semitica 51).
Dazu gehören auch die Lehnworte türk. ispenje
'Steuern von Kriegsgefangenen , Sklavengeld', serb.
spendza *Aufwand', rumaen. spendze 'Steuer, bulg.
ispenö 'Sklaventaxe' bei Miklosich, Denkschr.
WAW. Band 37, 48 und 38, 130 (dort falsch erklärt).
de Lagarde, Armen. Stud. No. 207 sieht in dem
Worte eine Zusammensetzung mit np. esp *Pferd'.
705. siijJuS, uspus 'Laus', siqms (etc.).
miiz. isftj (H.-Sch.).
aw. spis 'Laus'; phlv. spis (vd. 17 (8)), sjjus (AV.).
kurd. sipi^ aspe 'Laus' ; afy. spa$a ; oss. sis^ (239) ;
wa/. sisy sar. spal.
706. sipöyten^ supö/ten 'einheften {der- Sa'di, Bostän
S. 261 Vers 304); heraustreiben (Sahn. III, 1797
Vers 231; Is. 16, 3, 4)' 0.
phlv. spöj (päz. spöz) 'Aufschub' (Salemann, Mel.
asiat. IX, 247, 248 Note 85), spö/tan^ spöjet 'ent-
fernen, heraustreiben (Men., AV.), spö/tUan; arm. LW.
spidem Verschieben'.
Wenn 'einheften' die Grundbedeutung ist, so Hesse
sich lat. pungö (V^ptig-) vergleichen; doch ist dies
durchaus unsicher.
707. sipiJir 'Himmel'.
ap. JSnid^ofMrag^ 2l!7itd()tddT?jg; phlv. Huspitr (Gemme,
*) Die Belegstellen stammen von Herrn Prof. Nöldeke.
```


### [2026-09-14T00:54:02.100Z] TOOL RESULT

```
=== HUB leaf 84 (p.73) ===
— 73 —
skr. gasana- Torschriff (ZDMG. 47, 702) ist auch nicht
sicher. — Zu dem hier angefuhrten setigso (Shuk.
p. 147 s. V. aunbada) vgl. np. sang i sal 'Schleifstein'
(Rosen, Np. Sprachf. p. 50). Das in der Anmerkung
erwahnte np. sa Tribut = phi. sak (Matikan i 5atrang,
phi. Text p. 1, 12) ist = arm. LW. sak 'Tribut' (Elise
35, 6). Zu np. sav vgl. afgh. LW. sav a taxe, a tribute*.
697. Im Phi. ist apspurtan zu lesen, vgl. arm. ap-spar-em
'iibergebe, iiberlasse, vertraue an . Als iranische Wurzel
ist spar anzusetzen. Der Infinitiv sipdrdan (vgl. kas.
espdrtdn u. s. w.) ist vom Praesens neu gebildet;
ursprunglich steht nur der Infinitiv supurdan neben
dem Praesens sipdram (und siparam Sal. Shuk.
Gram. § 41, c). Fiir phi. spurtltan ist spurtan zu setzen,
vgl. Gl. and. Ind. 156.
698. Unsicher der Bedeutung wegen.
700. Die Bedeutung von zd. spOrdddsta- ist unsicher.
702. Zu den kas. Dialectformen mit l- stimmt jud. tat.
siipul *Milz* (Miller p. 80).
703. Dazu paz. spur perfect*, spur[ = phi. spurtk complete*
Shk. 268, phi. spur perfect' Gl. and Ind. 161, an-aspurlk
'imperfect* West, PT. 4, 40, spurikih 'completeness'
4, 328, an-avispurtk unvollendet* BB. 17, 261, arm. spar
*Ende' (/ spar 'bis ans Ende', anspar *endlos'). Np.
sipari = phi. *spartk; phi. spur = ap. *spma-; arm*
spar = ap. sparna-?
704. Arm. aspnjakan *Wirt*, aspnjaJcanufiun *Gastfreund-
schaft*. Die arm. Form setzt ein *aspinj voraus, das
zu den syrischen und mandaischen Formen stimmt.
706. Dazu paz. spuxtan to sed aside*, spuxtdr *remover ,
spoid putting aside, Shk. 267—268, arm. spuzel auf-
schieben', spuiumn 'Aufschub' (aus spoii- =■ ipsLZ.spdz-),
Phi. y^spoxtxtan'^ ist eine XJnform.
707. Np. sipihr 'Himmel' ist nach NSldeke direkt =
skr. gvitrd" Veisslich, wei3s', dazu nach Geiger afgh.
sper^ grau*.
```


## [2026-09-14T00:54:17.158Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"spuz\\|spaz-\\|spōz\\|spoz\" BRT.txt | head -30; echo \"=== AiW columns near spa ===\"; grep -n \"^spas\\|spasyeiti\" BRT.txt | head"
}
```


### [2026-09-14T00:54:17.211Z] TOOL RESULT

```
=== AiW columns near spa ===
7025:frasüsat  ar?dvT  . .  J"  aoxta  ar)dvi  Yt5. 8;  V.  :ji.\2  2St;  —  äat  (s.  8)  ml paoiryäi risväi  xsafne  atars  .  .  nmSnS.paitim yHsaiti  .  .  iV  ml  bityiii  . ,  v<lstrlm  /suyan- t>m  yasaiti  .  .  ä'  tnl  ^rityäi  . .  sraosfm yäsaiti  V.JtV.iS— 22;  —  itir&  mt^rahe frayana  (sd.)  ,  .  ä°  hva  pasu  vfra  vasö.- xsa^rö  fracaraitt  (sd.)  Yt/0.  112;  — miiir^m  .  .ynihe..frada%at  ahurö  mazJit balvari  döthiariqm  .  .  ii°  nbyö  döiiräbyö ..spasyeiti ..  ä'  '..\Llo.Zz;  28,101  (vor j-a/), /J.68,  H.2.10,  i4iSt,P.jiS'2St(vor
26862:spasitay-^
```


## [2026-09-14T00:54:18.346Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"spwc\\|spoz\\|spōz\\|spwhtn\\|spuxt\\|spōxt\" SNS.txt SNS_pages.txt | head -30"
}
```


### [2026-09-14T00:54:18.464Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:54:24.124Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l SNS.txt SNS_pages.txt; echo ---; grep -c $'\\f' SNS.txt; echo ---; awk 'BEGIN{RS=\"\\f\"} NR==100' SNS.txt | head -40"
}
```


### [2026-09-14T00:54:25.176Z] TOOL RESULT

```
  34173 SNS.txt
  16583 SNS_pages.txt
  50756 total
---
0
---
```


## [2026-09-14T00:54:25.316Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pixa\\|pixem\\|nava.pix\\|navapix\" BRT.txt POK_01.txt POK_02.txt POK_03.txt WLD_band3.txt 2>/dev/null | head -20"
}
```


### [2026-09-14T00:54:25.371Z] TOOL RESULT

```
POK_03.txt:797:Av.  pixa-  ,Knoten'  in  nava-pixdm  ,neunknotigen' ;   lett.  piks,  pika  ,Erd- und  Lehmklumpen',  sniega-pika  , Schneeballen'. WP.  II  70.
BRT.txt:10504:•  j.  grava-"  m.  'Rohrstock,  Stock':  graom jytis^ii. .  nava.pixim  (sd.)  adrinjayHl  aom
BRT.txt:18637:•  j.  nava.pixa-  Adj.  'mit  neun  Knoten': graom  ayasois  .  ,  °x>m  "sollst  du  einen Rohrstock   mit   neun   Knoten   holen"  V.
BRT.txt:21276:mit  a  i)  'herbeibringen,  holen':  graom ayasBÜ. .  nava.pixim  (sd.)  V.p.i  4.  a)  Med. "sich  etwas  holen,  verschaffen':  parpnrm ayasaisa  Yt./4.35;  ^5-SSj  —  ayasattha Vyt_9(?).  a)  "hinzubringen  zu  — ,  sam- meln in  — '  (Akk):  gaomalzim  ayasdii  .. 6ix»lnm  (ad.)  V.ig.21.  3)  II  Med.  'an sich  nehmen,  accipere';  a)  '(Truppen)  an ach  ziehen':  Aauv  Jtara*  (sd.)  parärasJ^ abiy  vUtäspam  pasävJ*  vistäspt^  ^äyasatä^ avam  käram  Bh.j.  ij  —  vaAya^dätt^  .  . amuki^  (s.Ntr.)  aityavi^  *pisiy^uväääm hacä  avaäasa*  isram  */lyasata^  "F.  zog .  .  nach  J'.,  von  da  aus  zog  er  Truppen an  sich"  Bh.j,  7,  b)  '(Länder)  an  sich reissen'-./twsz'a*  gauma/a* . .  aditi^  kt^bsji- yam  ut3p3rsam..ut3  aniyS^ äaAySvaf' hauv *äyasats^'>  ^teuaipa/iyam  (sd.)  aiuta  Bh.  /. 12.  II  4)  Med,  'etwas  (Akk.)  heischen, verlangen':  yS  vä  kasSu^ amatahö  (sd.)  ma- ziiiqm  ayamaite  *büjim  Y.j/.  13.  a)  zu- gleich mit  Akk.  der  Person:  vfIJßir3m{sd.) ditn  ayasata  äyapta  (sd.)  .  .  V.  zo.  3.
```


## [2026-09-14T00:54:33.784Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=797{if(/\\f/)n++}END{print \"ff before:\",n}' POK_03.txt; python3 -c \"\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\ni=t.find('nava-pixdm')\nprint('block idx',t[:i].count(chr(12)))\n\""
}
```


## [2026-09-14T00:54:34.685Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" SNS_pages.txt | head -5; echo ---; grep -n \"spo\\|spö\" SNS_pages.txt | head -20"
}
```


### [2026-09-14T00:54:35.289Z] TOOL RESULT

```
ff before: 62
block idx 64
```


### [2026-09-14T00:54:35.355Z] TOOL RESULT

```
---
5655:                                                                                                                                                        framan spoxtan                    ^UflJ&^U
```


## [2026-09-14T00:54:39.110Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==65' POK_03.txt | head -20"
}
```


## [2026-09-14T00:54:39.790Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5620,5700p' SNS_pages.txt"
}
```


### [2026-09-14T00:54:40.276Z] TOOL RESULT

```
gä  ,Vaterland*,  Ttaigig,  -ISog  f.  ds.,  lat. patria  ds.,  patrönus  , Schutzherr*,  patrö,  -äre  ,vollbringe,  vollziehe* ;  proprius ,eigen,  eigentümlich,  beständig*  aus  *prop  (a)  trios  ,von  den  TtgoTtdrogsg, den  Altvorderen  als  ererbter  Besitz  überkommen*  (?),  s.  WH.  II  374  f. ; mcymr.  edryd  ,Wohnstätte^  könnte  ursprünglich  als  ^väterlicher  Besitz* mit  mir.  aithre  identisch  sein;  aisl.  fedgar  PL  , Vater  und  Sohn*  (vgl.  gr. TiaTQLxög  ,väterlich*) ;  fedgin  PI.  ,Eltern*  {*fedr-gin).
WP.  II  4,  WH.  II  263  ff. ;  vom  Lall  wort  pä-  ausgegangen?  Kretschmer WZKM.  51,  315 f;  oder  zu  pö(i>  schützen?
830  ^
pid'  ,gebären*??  ursprüngl.  ,stark  ziehen^?  nur  germ.  und  kelt.
Got.  fitan  ,gebärenS  vielleicht  zu  ags.  fitt  ,Streit',  engl  fit  ,Anfall  eiaei, Krankheit^  nwf ries.  ^<s  ,bissig';  mir.  idu,  Gen.  idan,  Nom.  PL  idain  ,GqJ burtswehen,  Schmerz';  die  mir.  Flexion  geht  auf  air.  ä-Flexion  zurück, wie  z.  B.  mir.  persu  ,Person^  auf  air.  persan]  der  air.  Nom.  Sg.  muß somit  Hdan  {*piduna)  gelautet  haben. WP.  II  70;  vgl.  Feist  155  f.
pik(h)o-  jklumpiges,  Knoten'?
Av.  pixa-  ,Knoten'  in  nava-pixdm  ,neunknotigen' ;   lett.  piks,  pika  ,Erd- und  Lehmklumpen',  sniega-pika  , Schneeballen'. WP.  II  70.
pi-lo-  jHaar*,  s-Stamm  piles-.
Lat.  pilus  m.  ,Haar',    wovon   als   Kollektiv   ,Haarknäuel'   auch  pila  t  ij>- ,Ball,  Ballen,  Strohpuppe';   auf   einem  s-Stamm   beruht  *pil-s-os  ,verfilzt,   I^. in  gr.  TtlXog  m.  ,Filz',  TtlXeco  ,filze',  lat.  pilleus,  -eum  , Filzkappe,  Filzmütze* (*pilseio-)]  aksl.  phsh  ,Filz'.
WP.  II  71,  WH.  II  302  f.,  304  f.
pi-n-  jHolzstück'.
Ai.  pinakä-m   ,Stab,    Stock,   Keule';   gr.  Ttiva^y   -ay-og   ,Sparre,   Balken> Brett,  Schreibtafel,  Gemälde';  ahd.  witu-fina  f.,  mnd.  vine  ,Holzhaufen^' * aksl.  phUb  m.,  serb.  pänj  usw.  ,Baumstamm,  -Strunk'.
WP.  II  71;  Vasmer  2,  335;  wohl  zu  spei-  , spitz,  spitzes  Holzstück'.
pip(p)-  >piepen',  auch  unredupl.  pi-  mit  verschiedenen  Ableitungen. Schallwort.
Ai.  pippakä  ,ein  bestimmter  Vogel',  pippika-  ,ein  Vogel'?  gr»  TtTnog  f. oder  TTiTtTCOQ  m.  ,junger  Vogel',  rtlrcü),  niTtqa  f.  ,eine  Art  Baumhacker',. 7tLfc{7t)i^(o  ,piepe*;  lat.  plpilö,  -äre,  pipiö,  -Ire,  pipö,  -äre  ,piepen',  pip(p)itäre ,vom  Naturlaut  der  Mäuse',  plpulum  ,das  Wimmern',  osk.  pipatio  ,clamor plorantis',  nhd.  (nd.)  piepen  (mit  verhinderter  Lautverschiebung);  lit.  pyptiy. pfeifen*  (Lw.?);  Öech.  pipteti  ,piepsen',  sloven.  pipa  ,Huhn;  Röhre',  serb. pipa,  eine  Krankheit  der  Hühner'  (nhd.  Pips)  usw.;
öech.  pikati  ,piepen',  u.  dgl;  bulg.  pile,  skr.  plle
```


### [2026-09-14T00:54:40.315Z] TOOL RESULT

```
t«                                                                                                                                                                                     E
                                                                                      litest,   SBff.   V. V. p. 284.                                                             :    j             To
                                                                       rci^u
               ^W-»>^«0^:pa r ^3akan/palCl3akan:
      :parakan: <&»**»»          (        SnS   W *) parakla     :    ^
                                                        ,U;u--*l£4,b*^                                                                                                              U; cu-rfbfc.Uajlj
\r\                                                                                                                                                                                                                               If.




                                 \fArS         .Ai»oj>i-J *oirfU>:                             f ramSyend : jVUt                                         (Baitey.Oper. p. 23
                                                                                                                                                                     •TT-U/T^
                                                                                                                                                                                               :& .^L :
                                                                                                                                                                                             Viiv.Uan.
                                                                                                                                                                                                                 ^
                                                                                                                                                                                                                II,
                                                                                                                                                                                                                        .j^
                                                                                                                                                                                                                      6 4.
                .gjUo^'O*                          1*^'^                             :framayisn:                \yj>-^ J t>
                                                                                                                                                                                                                              )




                .
                 >A/W^ (Wir.Wan.                                                 II,       66)prm-? ysn :^t                                  +J*J+ * , -i USJ uA                     ^^        U oU> : f rara5n
                                                                                                                                                                                                 ,




                                               (yU<5l*o'j '•&) "*>•> :framud: fvv*


                                                                                                                                                        framan spoxtan                    ^UflJ&^U
                                                                                                                                                    :
                                                                                                                                                                                     :                      "
                                                                                                                                                                                                                 .V^J^
                                                                                               f nam0dan :         MVlW     11
                        .
                            a-* 1 -4   O u>    '
                                                       ft**
                                                              1   J*- "* **«*
                                                                         '
                                                                                           :



                                                                                                               To/IT'i                                      **•*   west.         Stfff.     p. 239,     2   :«f> )«Bl.Uai



fJUjj ^.Ij^>.^ Jh.                                 cjj •          ^i> 'atf «J*«*                :   f ravahr :    V^u                    *TV/r^..Ai/Trf,       W    /1;-i5       (Kotwal. p. 96. N. 1 **»

                                                                                                                                     |

                                                                                                                                                        •TA-TY/r^
                                                                                                                                                                                     »/>*»* -T-i/n -5
                                                                                                                                                                                                                wm       .
                                                                                                                                                                                                                             YA
      IJSjij^V^ WiVb. 992)..                                                 ,       f ravahr/ fravSi: b-                                                                (
                                                                                                                                                                             .us,    oUji^^raman-e:^^

 Zoroastrian ProfcZems in The Ll'Centurij*                                                                                                                                               -j*l«jja-di^U>:frainan:             ^^ej
                                                        .<t/\x3              U-1)/**                  P-       98-101.
                                                                                                                                 I                                           'fife's      >{M*. Man. II, 66.)
                        o-4    / Ji o- *^ Cu"» O-4/ *) f ranamisn:
                                           *   4                    «
                                                                                 1     :                          t^JJTl

Leave off, to pass over=franaraIdan                                                                        :    o*;-4-*                                                -j'-»>iU>           :fraraan     burdar Xgi)^o
                                                                                                                                 |
        it>*jPfojt        >o*£^ :f^av-:t- {Tavadia. 5nS. 161)
                                                                                                                                             A/1Y ^* *=***' 'i*jkj#*L>
                    •   TY/W^ Mi*. 990) plavayati:^^^                                                                            I
                                                                                                                                         '                                   :   framan burdarIh:^-»£9«X>


                                                                        .^Aj          U*ftlj:parvanag:                9 V                                                 .*L> :fram5yed: £w^o
                            U/XT ^                 (tfir.tfan.                    Hf 65)prw'ng                    :   jjk        I
```


## [2026-09-14T00:54:51.538Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -20 SNS_pages.txt; echo \"=== grep spo variants ===\"; grep -n \"spoz\\|spöz\\|sp5z\\|spuz\\|spOz\\|spoxt\\|sp5xt\" SNS_pages.txt | head -20; echo \"=== SNS.txt ===\"; grep -n \"spoz\\|spoxt\\|spuz\" SNS.txt | head -20"
}
```


### [2026-09-14T00:54:51.603Z] TOOL RESULT

```
    A
>l»>'i




 O^t'

        /
« *>&
                              Shiraz University Publication




     A GLOSSARY OF
SAYIST NE SAYIST
 A pahlavi persian Glossary
             -

=== grep spo variants ===
5655:                                                                                                                                                        framan spoxtan                    ^UflJ&^U
=== SNS.txt ===
8729:: framan spoxtan : ^UflJ&^U " .V^J^
```


## [2026-09-14T00:54:58.104Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nprint('ff count',t.count(chr(12)))\nt2=open('SNS.txt',encoding='utf-8',errors='replace').read()\nprint('ff2',t2.count(chr(12)))\ni=t.find('framan spoxtan')\nprint('block',t[:i].count(chr(12)))\n\""
}
```


## [2026-09-14T00:54:59.165Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pexak\\|pixak\\|pexk\\|pyxk\\|pêxak\" SNS.txt SNS_pages.txt | head"
}
```


### [2026-09-14T00:54:59.252Z] TOOL RESULT

```
ff count 242
ff2 0
block 81
```


### [2026-09-14T00:54:59.295Z] TOOL RESULT

```
SNS.txt:31502:pexak 143/6 
SNS_pages.txt:15891:pexak 143/6                puxtag 137/4                      raftar 225/12          rfistaglh 234/16
```


## [2026-09-14T00:55:03.030Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15880,15900p' SNS_pages.txt; echo \"=== index lines with 175 ===\"; grep -n \" 175/\" SNS.txt | head -20"
}
```


### [2026-09-14T00:55:03.090Z] TOOL RESULT

```
                                                         srCsOcarnaio 185/4                sQdag 190/19
 sar 182/10-230/18        siganag 10/9-172/5
                                                         srubSn 183/7-184/6                sOdaglh 191/15
 sar 3 sar 231/3          siya(h)   172/6
                                                         srtld    134/17                   sfldan 191/7
 sar brldan 230/20         si yak-S 10/10
31                                             ,bft.L a yy   i$A* $***& c-^j
 _ >*
pestar 232/22              pusarlh 109/17                    rad 226/2              reraanth 235/13
pes ud pas 143/2           pusih 138/19                      radSn 226/4            r€s 234/12
petrSt 142/14              pust 139/5-10                     radlh 226/5            rSsag 234/18
pexak 143/6                puxtag 137/4                      raftar 225/12          rfistaglh 234/16
pSxak snas 143/18                                            raraag 228/4           rSxtan 233/1
pid 11/12                                                    rapitvin 225/16        rfized 233/14
pidar 11/16                r5d 221/12                        ras 300/15             rSzfind 233/16
pihan/pihn 123/18          radlh 222/3                       rasad 300/19           rSzIhfid 233/10
pSlapd&n 139/16            radtar 222/2                      rasan 227/3            rfizisn 233/12
pSryOtkes 140/1            rah 222/9                         rasSd 234/3            riftagC?)    226/19
pCryStkSsan 140/7          ram 223/7                         rasSnd 300/18          rist 226/15-234/2
p5ry5tk§slh 140/10         ramisn 223/14                     rasldan 234/8-300/17   rObah 229/9
pOst 138/20                ramisnlgtar 223/19                rasisnlh 234/9         rOd 229/12
=== index lines with 175 ===
28390:spas 175/4 
29052:spanta- 175/18 
29735:x v astan5m 175/7 
30511:'•sprhm^n 175/16 
31421:spanCnaag 175/17 
31423:spannag ra§nSg 175/19 
31425:sparm 175/15 
31427:spSs 175/3 
31438:spSzSd 175/21
```


## [2026-09-14T00:55:13.470Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\nimport re\nfor i,b in enumerate(blocks):\n    if re.search(r'sp[aoO05][szZ]', b) and i<220:\n        print('---block',i,'---')\n        for ln in b.split('\\n'):\n            if re.search(r'sp[aoO05]', ln): print(repr(ln[:200]))\nEOF"
}
```


### [2026-09-14T00:55:14.601Z] TOOL RESULT

```
---block 74 ---
"     p^b'n t^^Ui^fc.           1614)     spasSnO,         ,/spas       : .jl   tuF^           I       ^'^c^'^C **'.)^ :p3dixsa:"
---block 77 ---
'               f   (** ^                i^it/iOtflsH spazamisn:'
---block 103 ---
'                                                         .j-V-       :spas:o"e>JJ            "-JjIj^a^-jVJU^jI^^j.i^^i^Ujj^"                                             .jL   :sar:\\<o»'
'                  (AiJ/fc.    1614) spas i&SiS**             /spas-          :&-'
'                                                        sparm            .'
'                                 .^jj-.titf- . U#- :span(n)ag:'
'                                             U*W>. 1619) spanta-:t-                                                            (   YVA **r 1 tr*^)               HJ^ J>- tf^ jj'
'                          i^.^L- :spann5g raenog:                     jits^a^o^                                            V»a^            (Mir. Man.           I, 43)shmyn:^Zi'
'spanjed       I, «j1, JH **»- j*'
---block 205 ---
' p                            vispatay- 273/18'
'                                                                   spas 175/4'
```


## [2026-09-14T00:55:23.095Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\nb=blocks[103]\nprint(b[:6000])\nEOF"
}
```


### [2026-09-14T00:55:24.187Z] TOOL RESULT

```
                                                         '       :


                                       tu^tn-L.jlj                                                                                 c-^Lul-^L^U^Ij                                                       \Vt
YA


                                                      .(Kotwai.       P- 169)                                                                  (Jlb.jfi^-,       :sast5r:        1a*»«*xx_w
                   .Y-p-6-T-l/" ** -6/T^
                                             *                                              !.P$           •(/Kk'fc.       1573)sastar-                   :   i^tf-**    sastar-:*5"
                                                                                                                      U/1fl^           (Mir. Man.             Ill, 61)-;s*st*r                      :




                                                         .j-V-       :spas:o"e>JJ            "-JjIj^a^-jVJU^jI^^j.i^^i^Ujj^"                                             .jL   :sar:\<o»
                  (AiJ/fc.    1614) spas i&SiS**             /spas-          :&-


                                                                                                                                                              .JL.aJL :salag: l9J-*<_v

^^.T^V^^^                 ***<* :x v ast ? :                            ,*mvW
 T4j^ffj.A.T
                               v
             w«*m*>o nsjlwO * x astanam :         1                          ^W           (Mir. s'rtjsU (AiWb.                   1567)         saracfa-: L.              [4V0"* •'*&)
                   V splitcorn -
                                  falhhanast                                         \>
                                                                                                                      »Y—) /A <5 .*/?<* -A/Y«£                    #sn.        III.
Corn separated                                                                   :                                                                                                           61).

=x
     v ast:l
             j0T
                     ^t^^^U^^fc^^^from kusks.                                                 •   T/ir-^ .JLijjii^            rpanzdah salag:                       i5^-o» -*oCef«J                           lo
                                         .«u-l*AJ»y-     trashed straw

>ahlavi VendidZd V. 35.
                                                                             :             _jj jjjJL^ki. "U-ilk-,1 .«iyL<4jfflU ,                             &JL :saligSn: vpS&HM
?ahl. V. GIoq  Kapadia, p. 488.                                                  :    )                          •6/1 Y 1&4        ->^ *!>! ^ o-' j* -5 ^V 3 iljil ^tf
5n3.      Tavadia, p. 71.                                                        :
                                                                                      *

                                                                                                       (          Y*_>» :^&) ^»jSjL .*jL .jfcjL :s3rlgar: J3jJ-m_jj


                                                                                 ^JOiJ
                                                                                           V-          1    •     >    +   sar     :         *V>» j'^'j*- vSj- t-»&tljaJ JOtf            l          |




                                                        sparm            .
                                                                                          {Tavadia.             SnS.
                                    O i*o J* fdrj pjr
                                         «    •
                                                                                                                             -«&) ,^/jl-          :fww> «/(gar: ^5 + Jui                                      u
                                                      c                                                .o«l^>il> T^T^)l, jJfts
                    ,-y/1»*       (.Mir. Man. II, 15) sprhm^n: j-tt                                                                               Ji^jii:Vj3/jL
                                                                                                                                               4 .|
                                                                                                                                                                 p   32.  |      .




                                 .^jj-.titf- . U#- :span(n)ag:
                                                                             4xmoa»                                                    •
                                                                                                                                           o****- : sahmgen/ sahmgon                         W .#->->
                                             U*W>. 1619) spanta-:t-                                                            (   YVA **r 1 tr*^)               HJ^ J>- tf^ jj
                          i^.^L- :spann5g raenog:                     jits^a^o^                                            V»a^            (Mir. Man.           I, 43)shmyn:^Zi
     -,J j-i <o-Jl*tf>j** <>*f« t*ii


                                            vw<iito»»
  .JUL: postpone, neglect. (<JW) spSzed:                                                                                                                          .^.L:s5yag: *-*-*OJ                         To


spanjed       I, «j1, JH **»- j*
                      :
                                 /Spoz:fc-.^ 3 ~l"                                        s'yg     :   jtkiAiWb.            208)ch5y5                 :   ^^^m a-saya-               :        fc.
```


## [2026-09-14T00:55:40.062Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v2 سپوختن ===\"; grep -n \"سپوختن\\|اسپوختن\\|سپوزیدن\" BQT_v2_pages.txt BQT_v2.txt | head -20"
}
```


### [2026-09-14T00:55:40.131Z] TOOL RESULT

```
=== BQT v2 سپوختن ===
BQT_v2.txt:28568:امرازسپوختن باشدا که بعنف دراندرون کردن 
BQT_v2.txt:28597:۱ - امر از ۶ در سیوختن » رك : سپوختن ۰ 
BQT_v2.txt:54059:ماضی سپوختن است کا فروبردن بزور باشدبعنی 
BQT_v2.txt:54110:۱ - اسم مفعول از «سپوختن» . 
BQT_v2.txt:54133:رك : سپوختن . 
BQT_v2_pages.txt:17426:                                                                     ‫امرازسپوختن باشدا که بعنف دراندرون کردن‬
BQT_v2_pages.txt:17436:                                                        ‫سپوختن‬              ‫امر از ‪ ۶‬در سیوختن »‬
BQT_v2_pages.txt:33002:                                                                                                      ‫رک‬‫ماضی سپوختن افست‬
BQT_v2_pages.txt:33036:    ‫‪ - ۸‬سوم شخص‬                           ‫‪.‬‬   ‫رك‪ :‬حیوختن‬                          ‫‪-‬سم مفعول از «سپوختن» ‪.‬‬
BQT_v2_pages.txt:33047:                                                                                                               ‫‪.‬‬    ‫رك ‪ :‬سپوختن‬
```


## [2026-09-14T00:55:41.235Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSF ===\"; grep -n \"سپوختن\\|سپوز\\|بسپوز\" FSF_pages.txt | head -20; echo \"=== SOD pyx ===\"; grep -n \"pyx\" SOD_pages.txt | head -20"
}
```


### [2026-09-14T00:55:41.330Z] TOOL RESULT

```
=== FSF ===
14711:‫بسپوختند‬    ‫همه درد‬    ‫به دارو‬                       ‫زمان و زمین از تو دارم سپنج‬
=== SOD pyx ===
```


## [2026-09-14T00:55:46.071Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" BQT_v2_pages.txt | head -3; python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\nprint('blocks',len(blocks))\nfor i,b in enumerate(blocks):\n    if 'سپوختن' in b or 'سپوز' in b:\n        print(i, b[:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T00:55:47.218Z] TOOL RESULT

```
blocks 684
296                                                                                 
553  ‫سپوز کار‬
```


## [2026-09-14T00:55:50.640Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nb=t.split('\\f')[553]\nprint(b)\nEOF"
}
```


### [2026-09-14T00:55:51.758Z] TOOL RESULT

```
 ‫سپوز کار‬                                                                                                              ‫‪۱ ۰۹۱-‬‬
 ‫بعنف وتمدی و زور فرو بردن ‪ - ۴‬و بر آوردن‬                               ‫سیندان ‪ = ۱‬بفتح اول بروزن لوندان‪,‬‬
 ‫است ؛ و بقتح اول‬               ‫اد‬
                                 ‫داز‬
                                   ‫ضغت‬
                                     ‫ان ل‬
                                        ‫باشد ‪ ۵8‬؛ ای‬                    ‫خردل فارسی باشد ‪ .‬و آن تخمی است دوابی‬

                                                                                  ‫خوانند ؛ وبکر اول هم بنظرآمده است‪.‬‬
 ‫سيو حته ‪: = 1‬کر اول و واو مجهول‬
                                                                         ‫سیید و ر = بکر اول بروزن سپردوز‪.‬‬
 ‫بر وزن فروخته ‪ ۰‬بمعنی بزور فرو برده‌وخللانیده‬
                                                                        ‫تادرسه و کماج خر مه را گوند ‪ ۰‬و آن نخته‌ای‬
        ‫ویر آورده باشد ‪ 1‬وشتح اول همآمده اس‬
                                                                       ‫که بر سر ستون خیمه‬                           ‫راناخ‬
                                                                                                                        ‫سشدومي‬
                                                                                                                             ‫با‬
 ‫سیوز ‪ ۰ ۲‬بکر اول و واو محهول ›‬                                                                                            ‫گذراند ‪.‬‬
 ‫بمعنی ‪-‬یوخت است که از فروبردن ‪ -‬وبرآوزدن‬
                                                                        ‫سیند یں ‪ = ۴‬بر وزن درم‌چین ‪ ۰‬بمعتی‬
 ‫بعنف و زور باشد چیزی را دچریزی ‪ -‬وامی‬
 ‫و شلان‬      ‫بر‬    ‫فرو‬        ‫است می‬      ‫هم أ مده‬   ‫تاين مەی‬
                                                                        ‫مپندان است که خردل فارسی ‪ -‬و تنم تره‌تیزل‬
                                                                                                                             ‫باشد ‪۰‬‬

                                                   ‫‏‪ET‬‬
 ‫‪ ۰‬دی‬        ‫فروزد‬       ‫وزن‬     ‫بر‬   ‫»‬   ‫^‬   ‫سیور‪۵‬‬
                                                                        ‫بزور باشدبعنی‬            ‫وابردن‬
                                                                                                      ‫رک‬‫ماضی سپوختن افست‬
 ‫فروبرد و «خلاند و در اندرون کند ‪ -‬و برآورد‪-‬‬                            ‫چیزیرا در چبزی بعنف وتعدی و زور فرو برد‬
‫اندازد‪ .‬هم‬        ‫تاخیر کند و کارها را ماز سس‬           ‫ود دمعتي‬
                                                                         ‫‪ -‬وبمعنی برآ ورد هم هست که از بورد!ن‌باشد؛‬
                                                     ‫گفته‌اند ‪.‬‬         ‫و شتح‬       ‫اس‬      ‫اضداد‬   ‫‪ 1۱‬باین اعتمار این لفت از‬


 ‫سیو ر گار * ه باکاف فارسی بالف‬                                                                                    ‫اول هما مده ام‬


‫کشیده وبرای بی نقطهٌ زده » کسی را کونند که‬                              ‫سیو ختن ‪ - ۴‬بکراول و واو مجهول‬
      ‫درکارها تاخیرکند وباز پس اندازر ‪۰٩‬‏ ‪۰#‬‬
                                                                        ‫بر وزن فروختن » بم‌عنی چیزی را در چیزی‬

                          ‫‪.‬‬     ‫دان‬
                                  ‫ینن»‬
                                     ‫سندا‬
                                        ‫اصی‬
                                          ‫رك ‪:‬‬                     ‫‪۴‬‬          ‫‪.‬‬    ‫سیندین‬    ‫‪.‬‬   ‫اسیتدان‬   ‫‪:‬‬   ‫رك‬      ‫‪۱‬‬



    ‫‪ - ۴‬ا سپوخ ‪(-‬ی‪۳‬وز) ‪ +‬نن ( پوند مصدری ) ‪=-‬پوزیدن ؛پهلوی ‪8۵6۲6۳5‬‬
    ‫( از ‪ " ۵6۳5[ :‬پازند ‪ ( )2۵۳5‬نأخیر ‪ ,‬مهلت ) ‪ ۰‬پازند ‪ ۰ ۳800۱05‬ارمنی ‪1622‬ع؟‬
                                               ‫‪.‬‬      ‫تبرکه ‪۹‬‬          ‫ورك‪:‬‬       ‫هو شمان ‪۹‬‬         ‫‪۳‬‬   ‫(بتعویقاداختن)«اسشق‬


                  ‫عدو را چاه کن درچاه بسپوز ‪.‬‬                                 ‫‪ - ۴‬ولی را گاه له ب رکاه نشان‬

   ‫سوزلی سمرقندی ‪.‬‬
                  ‫بر سپوزد سر از گریباش ‪.‬‬                                     ‫‪-‬ن دمدباد شهوتی جاش‬
                                                                                                ‫چو‬‫*‬
   ‫انوری ایوردی ‪« .‬فرهنگك نظام“ ‪.‬‬

    ‫‪ - ۸‬سوم شخص‬                           ‫‪.‬‬   ‫رك‪ :‬حیوختن‬                          ‫‪-‬سم مفعول از «سپوختن» ‪.‬‬
                                                                                                        ‫‪ ۱‬ا‬
                                                                                  ‫مفرد مضارع از «سیوختن» و«سیوزیدن؟‪.‬‬

                  ‫نوش با کام او بچودون زهر ‪.‬‬                             ‫سپوز کار بدهر‬                  ‫د‬
                                                                                                        ‫شکه‬
                                                                                                          ‫باهر‬
                                                                                                             ‫‏*‬
   ‫ابوشکور بلخی ‪« .‬فرهنگه ظام؛ ‪.‬‬
   ‫= بکراول وفتح ششم ‪٠‬‏ از ‪ :‬سپور (ه‪.‬م‪ + ).‬دن ( يولد مصدری)؛‬                                            ‫‪ #‬دیوریدن‬

                                                                                                               ‫‪.‬‬    ‫رك ‪ :‬سپوختن‬


                                               ‫‪ #‬سیه ¬ بكر اول وفتح دوم ‪ ۰‬مخفف سپاه («‪.‬م‪. )۰‬‬
```


## [2026-09-14T00:56:07.573Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\nprint('blocks',len(blocks))\nfor i,b in enumerate(blocks):\n    if 'سپوخ' in b or 'سپوز' in b:\n        print('=== block',i,'===')\n        print(b[:2500])\nEOF"
}
```


### [2026-09-14T00:56:08.913Z] TOOL RESULT

```
blocks 485
=== block 296 ===
‫سپیجاب‬                                        ‫‪۳۹۳‬‬


                 ‫ند‬
                  ‫تفرو‬‫خهش‬
                        ‫وزگا‬
                           ‫دن در‬
                               ‫هما‬                                ‫ج‬
                                                                  ‫نمو‬
                                                                    ‫گابو‬
                                                                       ‫مر‬      ‫امشکهد‬
                                                                                    ‫بواه‬
                                                                                       ‫نخ‬
‫بسپوختند‬    ‫همه درد‬    ‫به دارو‬                       ‫زمان و زمین از تو دارم سپنج‬
‫)‪(1۵011-۳4-1‬‬                                         ‫‪۳۱۱۰-۲4۵‬‬
                                     ‫سپهتاز‬
‫از سپه ‪ +‬تاز [اسم فاعل مرخم از تاختن =‬                           ‫چندروزه عاریتی» موقتی‪:‬‬
                      ‫تازنده ]‪:‬تازنده سپاه‪:‬‬                 ‫ببخش و بخور هرچ آید فراز‬
               ‫ورازاد بدنام آن پسهلوان‬              ‫بدین تاج و تخت سپنجی مناز‬
‫دلیر و سپه تاز و روشن روان‬                           ‫(‪)۷-۰۴-۱۲۶‬‬

 ‫(‪)۳-۴۷۱-۱۰۶۶۲‬‬                                      ‫فخر گرگانی «سپنجی» را در این بیت به‬
                        ‫سپه کش (بازبر کاف)‬           ‫معنی مهمان‪ ,‬راهگذر بکار می‌برد‬
 ‫اسزپه ‪+‬کش [اسم فاعل مرخم اکزشیدن‬                                            ‫)‪(۸4۴-4‬‬
                        ‫رش‪:‬‬
                          ‫شهک]‪:‬‬
                              ‫لند‬
                                ‫کش‬                     ‫[جهان] به چه ماند؟ به‌حان کاروانگاه‬
       ‫سپه کش چو قارن مبارز چو سام‬                  ‫همیشه کاروانی رابرو راه‬
‫سپه برکشیده حسام از نیام‬                               ‫ز هر گونه سپنجی در وی آیند‬
‫(‪)۱-۹۱۱-۵۷8۶‬‬                                         ‫ولیکن دیرگه در وی نپایند‬
                   ‫=سپیجاب س=بیجاب‬
                                 ‫سییجاب ا‬                                   ‫سیوختن (با زیر اول)‬

‫این نام را در فرهنگ‌ها و در بسیاری از‬                ‫این واژه از اضداد است‪ .‬هم به معنی‬
 ‫نسخه‌های قدیمی شاهنامه نادرست‬                      ‫چیزی را در چیزی خلانیدن و فرو کردن‬
 ‫«سپنجاب» نوشته‌اند‪ .‬درست آن سپیجاب‬                  ‫و هم به معنی برآوردن بیرون کشیدن»‬
‫و اسپیجاب است‪ .‬در نسخه خطی ترجمة‬                                                ‫بیرون راندن‪:‬‬

‫تفسیر طبری که در کتابخانهة سلطنتی ایران‬
```


## [2026-09-14T00:56:21.697Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\nfor i in (124,125,295,297):\n    print('=== block',i,'===')\n    print(blocks[i][:300])\nEOF"
}
```


## [2026-09-14T00:56:22.830Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\nb=blocks[296]\ni=b.find('سیوختن')\nprint(b[i-200:i+2500])\nEOF"
}
```


### [2026-09-14T00:56:23.260Z] TOOL RESULT

```
=== block 124 ===
‫بیران‬                                           ‫‪۳‬‬


  ‫دل هر دو بیداد ‪ :‬سلم و تور] از آنسان بسوز‬                    ‫و درم ریختند‬      ‫زسعیفران‬
                                                                                        ‫ب‬
 ‫رمگز نبینند جز تیره روز‬
                       ‫ک
=== block 125 ===
                                                 ‫‪Y۲‬‬                                           ‫پیراه‬



                                      ‫بیستگانی‬        ‫(ص یز) آن را‬      ‫بهار در («مقدمه مصحح»‬


 ‫ماهیانه کهبه سپاهیان و نوکران دهند‬                   ‫یاداور می‌شود‪ .‬در لغت شهنامة ع
=== block 295 ===
                                            ‫‪۳۹۲‬‬                                     ‫سپرده درون‬

            ‫سر مرد جنگی خرد نسپرد‬                                 ‫بپرسیدم از هر کسی بی‌شمار‬
                                                   ‫بترسیدم ازگردش روزگار‬
‫)‪(۲-1۴-۸0‬‬              
=== block 297 ===
                                                   ‫‪۳۹۴‬‬
                     ‫ستیر (با زیر اول و زبر دوم)‬                      ‫‪ ۸۴-۴‬ب س ‪.)۴۱‬‬
                                                                                  ‫‪۲‬ص‬‫خوانند» (‬
                                         ‫ا‬
```


### [2026-09-14T00:56:24.642Z] TOOL RESULT

```
‫(‪)۱-۹۱۱-۵۷8۶‬‬                                         ‫ولیکن دیرگه در وی نپایند‬
                   ‫=سپیجاب س=بیجاب‬
                                 ‫سییجاب ا‬                                   ‫سیوختن (با زیر اول)‬

‫این نام را در فرهنگ‌ها و در بسیاری از‬                ‫این واژه از اضداد است‪ .‬هم به معنی‬
 ‫نسخه‌های قدیمی شاهنامه نادرست‬                      ‫چیزی را در چیزی خلانیدن و فرو کردن‬
 ‫«سپنجاب» نوشته‌اند‪ .‬درست آن سپیجاب‬                  ‫و هم به معنی برآوردن بیرون کشیدن»‬
‫و اسپیجاب است‪ .‬در نسخه خطی ترجمة‬                                                ‫بیرون راندن‪:‬‬

‫تفسیر طبری که در کتابخانهة سلطنتی ایران‬                 ‫در بیت‌های زیر به معنی بیرون راندن‪:‬‬
‫است و عکس صفحه اول آن را حبیب‬                           ‫نه مرگ از تن خویش بتوان سپوخت‬
‫یغمایی در جلد اول این کتاب چاپ کرده‬                  ‫نه‌چشم جهان کس به سوزن بدوخت‬
 ‫است این نام«سبیجاب» است‪ .‬همچنین‬                     ‫(‪)۲-۲۸-۱۴۱‬‬
 ‫است در «حدودالعالم» نسخه خطى‬                               ‫کسی گوید آتش زبانش نسوخت‬
‫تومانسکی (چساپ فسرهنگستان علوم‬                       ‫به‌چاره بد از تن بباید سوخت‬
 ‫شوروی ‪« )۰۳۹۱‬اسبیجاب‪ ...‬بر سر حد‬                    ‫(‪)۶۵۹۳-۲۵۲‬‬
 ‫وندر وی شهرهاو‬
              ‫تسرکستانست‪ ...‬ا‬                   ‫رستم در زهدان مادر چنان بزرگ بود که‬
‫ناحیت‌ها و روستاها بسیار است و قصبهً‬                ‫پهلوی رودابه را شکافتند تاکودک را‬
 ‫این ناحیت شهریست که اسبیجاب‬                                           ‫بیرون بکشند» سپس‪:‬‬
```


## [2026-09-14T00:56:51.131Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON پنچر ===\"; grep -n \"پنچر\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -10; echo \"=== MON پیختن ===\"; grep -n \"پیختن\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -10"
}
```


### [2026-09-14T00:56:51.220Z] TOOL RESULT

```
=== MON پنچر ===
=== MON پیختن ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:13223:اشس‌پوختن: 30 [- اشسپیختن < 
MON_part1.txt:13223:اشس‌پوختن: 30 [- اشسپیختن <
```


## [2026-09-14T00:56:51.955Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD knot ===\"; grep -n \"'knot'\\|knot\" SOD_pages.txt | head -20"
}
```


### [2026-09-14T00:56:52.009Z] TOOL RESULT

```
=== SOD knot ===
15656:        gr'mg                                                              knot, bond, joining
33315:      topknot                                                         usya ©<*usi ^sy*
38667: Jerusalem      1945                    keeping     3417                        knot 4187
39708:    topknot     10231                               transgression        2133                 Tukhar      5329
```


## [2026-09-14T00:56:56.418Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13200,13240p' MON_part1.txt"
}
```


### [2026-09-14T00:56:56.493Z] TOOL RESULT

```
ا )از عد ارس آمش‌مایوت لسان: 
اشاعت؛: اد (ع. اشاعة] (مسصم.) 
آشکار کردن» فاش کردن (خبر و جز آن). 
باشیدن» پراکندن» گستردن. رحق.) اجتماع 
حقوق مالکان متعدد در مال واحد» بدون 
قصد همکاری در انتفاع از آن مال» مانند 
ترکة میت که بطور اشاعه بین وارثان مشتر ک 
است. اشاعت خر: فاش کردن خر. 
اشباح: طقاکه [غ. ۰] (.) ج. . شسبح. تنها» 
کالبدها. سایه‌ها. سیاهی‌ها که از دور دیده 
می‌شو د. 


اشباع: عاقه [ع. .] (مص‌م.) سیر گردانیدن» 
سیر کردن. رنگ سیر کردن (.) پر و بسیار» 
پر و فراوان. (قا.) حرکت دخیل. (شیم.) 
اندازه‌ای از ماده که در ترکیب بیشتر از آن 
محتاج نباشد. (پز.) اندازة تحمل بدن دوا را. 
اشباه: [ع.] (مصل.) مانند کسی 
شدن,» مانند شدن به چیزی» با چیزی مانیدن. 
اشسه: (ع.] (ص تفض..) شبیه تر» 
ماننده‌تر ماناتر. 

اشس‌پوختن: 30 [- اشسپیختن < 
اشپوختن - اشبیختن] (مسصم.) پاشیدن» 
پرا کندن» پراکنده کردن» افشاندن. گل نم 
ردن. ترشح کردن. 

اشپون: اجه (.) (چاپ.) سرب باریکی که 
میان هر دو سطر نهند تا فاصلهً مطلوب پیدا 
شو د. (چاد.) و احد طول سطر. 

اشتاد: 024 (.) (اخ.) نام فرشته‌ای است. 
روز بیست و ششم‌از هرماه‌شمسی که فرشتة 
مذکورمو کل‌بر اواست. 

اششاک: 1 [ع.] (مصم.) بهم در 
شدن» بهم پبوستن» در آمیختن» شکه ّ 
شدن. 

اشستاه: حجصاهاکه [ع.] (مصل.) بوشیده
```


## [2026-09-14T00:56:57.526Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"4187\" SOD_pages.txt | head -10; echo ---; grep -n \"^ *4187\\|4187 \" SOD.txt | head"
}
```


### [2026-09-14T00:56:57.598Z] TOOL RESULT

```
15653:                                                                      4187 yr'ns B
37765:   11386, 11387,11421                    biting      11528                       bond     2651, 4187
38667: Jerusalem      1945                    keeping     3417                        knot 4187
38680:joining 52, 4187                          11601                                  7615, 8105, 8106, 8107, 8108,
---
35270:4187  yr'ns   B 
87860:bond    2651,  4187 
90970:joining     52, 4187 
91069:knot    4187
```


## [2026-09-14T00:57:05.746Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pyx\\|pyX\\|pyk\\|p'yx\" SOD_pages.txt | head -20; echo \"=== block 401 ===\"; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nb=t.split('\\f')\nprint(len(b))\nprint(b[401][:1500])\nEOF"
}
```


### [2026-09-14T00:57:06.816Z] TOOL RESULT

```
4400:     BSTBL, Dhy. 207                                                    226 Mpyk        M
4402: 213 »pkyny(y)      M => »pkyn>k                                             apik       =*}pyk                              L?^1    \ji'
7818:1401 'pyk      M
7821:      apik =>»pyk
9859:2094 >xspyk M                                   ^Li^Ui             (o)xsewan(a)kya ?
11158:         etc.; C2 gloss. ->; -w, Hen. Tales. 480.8;             2572 pyk'nc M           (Jt^r^j^olf^^^JL-^uAaU
11164:       bridegroom                                               2573 pyk'nyc    S                      JU ^J* „U ijf^A
12249:       ywt}w, p>yc                                           2986 pyk B, M, S                     ^ Jj*. , jj^ <£>
12253:2973pyc>n>k B                                                       2367; MDii; C2, 3R3; abl. pyk\ VJ 132, 146,
12268:                                                                                     3000 pykp'r'yck1    B, M                    yij^^jt
12274:                                                                                     3001 pykp>rcyk B                            ^^^>
12275:      2989 pyk> B                                            ^T^U
12284:      2990 pykVh  B, S                             Ij^«oj^m£>-
12285:           Pek =»Pyk                                                                 3003 pykp'ryck =» Pykp>r>yck>
12290:      2991 pyk'prm         B =* Pykprm(w)                                                 SCE 28; BSTBL, Vim. 47, 51; Dhu. 162
12291:      2992 pyk}s}r     B =» pyks»r                                 Ojj^i             3005 PyksMr   B, M, S      (0>>>^ jj)>-<jj^<£>-
12292:      2993 byqb'r      C                                                                  Peksar   (pyk^r, Pyks'r) ©Yaghn. veske =>bys\
12296:      2994 pykcyk       M, S                         ls^-J1^ 'ijjj*
12298:                                                                                     3006 byqsJr ** bs\ pyks'r
12300:           external                                                                  3007 pyks}r -» Pyks»r
=== block 401 ===
645
                                                                                                                            334
 pxwst-

         =»pxwst-, pyw'sty, pwx>y-, pwxst-, pyw'y-,                        C2, 3V2,pI. -mVyf, C2, 3R11
         'pyv^y-                                                     8305 py'mnyy        M                    jL^Ui ^ji^U^
       (to)cut off
       BBB 505.8 a7; GMS 616; STi 3.2; Sund. AoFi                         healer, healing
          1974, 3R 2; impf. p>xw>y, MSP b 184                             GMS  892
                                                                           pyamne
 8294 pxwst- C                               o>f(±*                 8306 pytat- M                     j»tjjl»jj < jj/o^j*
      (a)pxw/ust, paxust- ©pt. St. ^pxw'y-, 'pyw'y-,                     pyamt ©pt. st. ^py'nVty, pyms-
        'pywst-, pwxst-                                                  (/0)heal, (to)bc healed
      0c>)cut off                                                        GMS 888
      STii 6, 6; BSTii 867.26; C2 gloss.
                                                                    8307 py,mtw(6,r)- M                 &£**&* 'd* J' CMj*
8295 pxwsty         C                           oju^ i*j^A£
                                                                         pyamtu (8ar-) ©pp. perf. st. f. py>mt* ^pyto-
      paxuste       ©pi. -f =^pYw*sty                                    (ro)heal, (to)bt healed
      cut off
```


## [2026-09-14T00:57:11.249Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nb=t.split('\\f')\nprint(b[402][:4000])\nEOF"
}
```


### [2026-09-14T00:57:12.384Z] TOOL RESULT

```
335

      BSTBL, Dhy. 91, 256, Vim. 86, Frag. Len. 100 c8;
        GMS lllln 1                                                     pyksyu KG 2056
                                                                 8333 pyksw =* pyks>k(w)
8317 py»tyh =» pyV                                               8334 pym'kh B                                             <j£
8318 py'tyy M =* py}tk                                                pemak, fimak ? ©*paimaka^ Oss. fink
                                                                      foam, froth                                                pyr
8319 pych ? B =» prc(h)
                                                                      SCE 323; BSTBL, Dhy. 345                              >fb
8320 py6      B ■* py5h
                                                                 8335 pyms-     C                          jzsllii' ( jj&jU^
8321 py8»r       B =* py5>r                                                                                          o*.
8322 pyS}n(h) ywtNv B                                 d%>T *&         pyams ^py'm-, py'mt-
                                                                      (to)be healed
     pi5an xutaw/u
                                                                      C2, 66V11 p52:BSTii 875.11
     king of elephants
     VJ                                                          8336 pyn-     B, C

8323 pyS'r B, M, S        (j^ yj^> >>)Uj <>U>-4, iiS\^
                                                                      (to)open
     pi5ar (py6*r, py5S>r, pyd>r) ©<*pati-radi                        TSP 13.15; STi 39.5, 69.7; BSTii 888.8; Benv. JA
       ©postp. +Crt
                                                                        1955, 308; C2 pl31, 2pl. impv. pynth C2, 60R8;
     for, because of
     EG9H 165; GMS 1613; Hen. BSOAS 12, 46 n %                           pen pyndyr-y BSTi; Gersh. JRAS 1946, 179
                                                                        perf.
       S W, CLI 1989, 181                                        8337 pynmcyq C                              ^^iJJ
                                                                      pinamcik, penamcik ©<pyrnmcyk ©adj. pi, -f;
8324 pycPr       C ^ py5>r                                              ob. pi. -ty =»pyrnmcyk, pnmcyq
8325 py8)rnqy> C                                    Ui«*JU.           former, previous
     py5arnakya ? ^pcPrnqy*                                           GMS 356; C2 gloss, pynmcyq, C2, 31V7; pnmcyq,
     healing
      STii 3.20                                                         C2, 57V27
                                                                 8338 pynms* C              (0jtjLri Oj^^ >^) ^        < JAi*
8326 py55,r      M =* py8>r                                           pinamsa, penamsa      ©adv. & postp.
8327 py5h B                   (jy> >^ ^) JJ « J-                      before, in the presence of
     pi5 ©Parth. MP pyh Khwar. pyz ©ob. -yh\ pi.                      C2 gloss, pynms\ 55V27; pnms\ 77R17
        -/A; ob. pi. -tyh\ gen. pi. ->n                          8339 pynmstr C                       ^                    i^J
      elephant
      VJ; TSP 2.979, 3.136, 6.8, 9.44, 84, 13.16; SCE 364,            pinamstar, penamstar    =>pyrnmslr
                                                                      first, formerly
        379; BSTBL, Vim. 83, Dhy. 10; pydtu Vim. 64
                                                                      BSTii 851.5; C2, 11R28, 12V5, pnmstr                 Uf
8328 py8p>k B                                           jijj
                                                                 8340 pyntp't B
     pi6pe (py6p}y)                                                     ©<Skt. pindapata
     elephant keeper
                                                                      beggar
      VJ 48b, 61b, 203, 195; GMS 1137
8329 pySp'y «* py8p>k
```


## [2026-09-14T00:57:19.691Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nb=t.split('\\f')\nimport re\nfor i in (403,404):\n    print('==== page',i-67,'block',i,'====')\n    print(b[i][:3500])\nEOF"
}
```


### [2026-09-14T00:57:20.844Z] TOOL RESULT

```
==== page 336 block 403 ====
                                                                                                                           336




  pyr
        moving ?                                                        6.19
         MDii p94 R2 n p98; Gersh. Advice. 86                   8355 pyrnmcyq       M, C =» pyrnmcyk

8344 pyr- B, C, S                     ^sil^Lipl ifrj'jjl        8356 pyrnms* C
     pi/er (DKhot. pir                                               pirnamsa ©adv. =>pynms>
     0<?)believe, (to)trust                                          previously, before, forward
     SCE 214, 455; TSP 6.41, 53, 63; BSTBL, Dhu. 80,                 STi 6.13, 10.12; Sund. AoFiii 1975, 241, 3, 14
          8.7; Frag. Len. 68.9, 114.3; BSTii 886, 10, 17:       8357 pyrnms*r             (j>> >^   j->) jl J** <>r < JJ < jjz^
          C2, 51R10, 14, 51V17 p96; GMS 200n 1; MSP                                                                    u~$*
                                                                      pirnamsar (pyrms}r)
          c7; Bailey. Prolexis. 194                                   previously, before, forward
                                                                      VJ 281, 785, 840, 1295; TSP; BSTBL, Dhy.; Frag.
8345 pyr'k B                                           ? ^>
                                                                        Len.; BBB el3; KG 2327; STi 34.3, 86.6; STii
     pire, pere?
     believer                                                           1.28, 2.4, 324; BSTi 82 etc,, -w, BSTBL, Dhy.
        TSP 16.45; S W, BSOAS 1983, 44                                 356
                                                                8358 pyrnmstr                 (uy^ y^? jj)*AJ tj^
8346 pyr}mstr =» pyrnmstr
                                                                     pirnamstar (pyr*mstr) =^pynmstr
8347 pyr't- B                                        j*kj£           before, formerly
     perat, pirat ©pt. st. =»pyr-                                     GMS 1288, 1290, 1682; BSTBL, Vim. 154, Dhy.
        OcObelieve                                                      135, 281; TSP; STii 10.21; BSTi 199; MDii;
        TSP 6.67; S W, BSOAS 1983, 44, per
                                                                        Frag. Len. 91.5; MSP bl73, >yw. . . "soonn, VJ
8348 pyrSn M, S                                     (jVL^j              60b 383 n p92; TSP 2.80
     per8an ©<* pari-dana                                       8359 pyrnyq        C                                 ^<j*>
     saddle
                                                                      pernik, perpazan =»pyrn}k, pyr-
        GMS 122; JRAS 1944, 140n 1; Frag. Len. 37.15,                 faithful
          19                                                          STi 44.4; GMS 997; Sund. AoFiii 65.5
8349 pyrm'str      B =* pyrnmstr                                8360 pyrp}zn       B                                  ,y>J^
8350 pyrms'r     B => pyrnms'r
                                                                      pir-pazan
                                                                      faithful at heart
8351 pyrn'k B                                      j&^^y
                                                                      TSP 2.1171
     pirne, perne ©pi. pyrrCyt       ^pyryn'k
     believer                                                   8361 pyryq     C
        TSP 2.704, 1166; pi. 
==== page 337 block 404 ====
337
                                                                                                                   pz»tyk
                                                              8379 pystrw     B, C, S                  (jy> ^—^ jj)j*ji{J^
8367 pys»pr     S -> ps>Pr, ps'Pr
                                                                   pistaru ©adv. & postp. =^pystrw, pstrw
8368 pys>k    M                                        ^p
                                                                   later, afterwards
      pise ? (pysyy, pys(>)y) ©pi. pys())yt, pyysyyt               GMS 373
      organ, limb
      W-Lii 574; BBB 603; KG 372; GMS 1635, 1658;             8380 pystrw'yck        B =» pystr,yck>
        }stkpyPy, SCE 368                                     8381 pystrycyk* B                                      *j-uJ<^jou
8369 pys(>)y =* pys>k                                              pistarecik
                                                                   future, later
8370 pysm B                                   ^L^jJL*
                                                                   SCE 485; GMS 373
     pism ? pesm ? ©<pasca-ima ^pysm
     according to                                            8382 pystw8}r      S =* pyst-1, pyz-
     SCE 532; TSP 15.31; STii 8.7; GMS 373, 1472             8383 pysty     B =» pc-
8371 pysmwr8(w)                                  S j> jl ^   8384 pystycyk => 'pystr^ck*
     pis-mur5                                                8385 pys-wz'y C                           ^Lj^^i^\^iS j\a
     after death
      TSP 8.52, 8 bis 6 n p216; Frag. 6.5; GMS 1143                pis-waze
                                                                     ivlzayaOd©Parth. wzyh- "to abandon"; Av.
                                                                   heirloom
8372 pysll'm'k S                           {Ll^ikj? ijlj*
     pis-name                                                      BSTii 885-21; C2, 51R21 n p96, -*wz>y "to
     surname
      MDii p21.3n p27
                                                             8386 pysyy M =» pys}k
8373 pysn'myk S                               ? o^.U <*k~j   8387 pytc C                                             LU;<oJUuf
     pis-namlk                                                                "
                                                                  pete le?ave©<*pyty; Parth. apedag        ©f. pytc
                                                                  lost, stray ?
     copy, above-named ?
     MDii pl39.6 n pl40; MDiii 70.16                               C2,6V16n5p59
8374 pyspSw S                     ^ j* < JU>* <xu <JT jl ^
                                                             8388 pyts'r S(AL) =* pts>r'
     pis-pa8u ©<*pasca-padam\ OP nipadiy                     8389 pytsr5 B                           ojl>> ijMoa <jJ*
     behind, after (wards X subsequently
                                                                  accordingly
                                                                  patsar5/9 ©postp. -=»ptsr6, pts}r5
     KG 406

8375 pyst                       (jy> ^* >>).**, ^ <Uf              SCE; TSP 2.482, 518, 531, 6.141, 9.91; Frag. Len.
     pi/est ©<*pasit\ A v. pascaeta =»pystrw, pstrw                  100 c3; VJ 912; SCE ptsh+iO p68; STii 10.23
     but, then, later
      EGSii 204; GMS 373, 434; BBB; pyst\ TSP 6.71;          8390 pyz-     B, M, C        (Oy> ^ •
```


## [2026-09-14T00:57:32.549Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\" SOD.txt; grep -n \"pyx\" SOD.txt | head; echo \"=== entry 335 ===\"; grep -n \"^ *335 \\| 335 \" SOD.txt | head -5; echo \"=== page 338 ===\"; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nb=t.split('\\f')\nprint(b[405][:2500])\nEOF"
}
```


### [2026-09-14T00:57:34.036Z] TOOL RESULT

```
111423
=== entry 335 ===
9660:335  Vskr'ky'kh  i^i^jS^r 
12465:^Ytmzyn  "all  armoured";  GMS  335  n  1 
14300:GMS  335  n  1 
63911:335 
73648:GMS  525;  VJ  1374;  TSP  3204;  BSTBL,  Dhy.  335 
=== page 338 ===
                                                                                                                         338
  p?yyr-
 8393 pzyyr-       B                          jj jIju? tpj^f^lj          ill, sick
       pazyer (pzyyr-) ©impf. p>zYyr-            =»zyyr-,                SCE 425; BSTBL, Dhy. 226; GMS 1060, 1078
                                                                   8404 r>pty> S                                   cJLf t^U,
       (to)pc llr-out, (/o)shout
            cayy                                                        raftya, rapdya
       TSP 13ii 11; C2, 51R23, 57R30; BSTii 890.51,                      sickness
         851.10
                                                                         MDii pl75.1
 8394 pzyyr-       C => pzyyr-                                     8405 r}py
                                                                        raf(e) M(S)                                     ^L*
 8395 pzyyrt- C                                      ojlJl£*ij
      pazyert ©pt. st.                                                   illness
      (/o)shout, (to)cry out                                             Hen. Tales. 481.53
      inf. C2, 3R14, 12V10, 22V18                                  8406 r'Py'kh     B                                   ^j^
 8396 pznw     C =$ pdn(y)
                                                                         rafyak     =»pw r'py'kh
8397 pzrn      M                                        ojju[<r*
                                                                         illness
      pazarn =>ptzrn, 'pz'rn                                             TSP 6.164; r'fitf "illness" MDii pl25.1
      sorrow
                                                                   8407 r}cpr B =» r>cprt
      GMS 579.957
                                                                   8408 r}cprt B                      (JXs* •& (ty>jyrh
8398 pzt B                                                   ^          rajP/wart (r'cpwrt) ©rajawarta; <Skt.
     pazd ©<Av. pazdaya; Yaghn. Pazd\ Oss.
                                                                           rdjyavardhana
                                                                         Rajwart(flame     =*r>zprt
                                                                                       of the  king of elephants)
        fdzddg      ©nom. ace. -y- inst. ->
      smoke
```


## [2026-09-14T00:57:54.009Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in \"پیختن\" \"پيختن\" \"بیختن\" \"پنچر\" \"ینچر\"; do echo \"=== $p ===\"; grep -ln \"$p\" MON_part1.txt MON_part2.txt BQT_v1_pages.txt BQT_v2_pages.txt FSF_pages.txt incoming/ARY/ARY_pages.txt 2>/dev/null; done"
}
```


### [2026-09-14T00:57:55.084Z] TOOL RESULT

```
=== پیختن ===
MON_part1.txt
=== پيختن ===
=== بیختن ===
MON_part2.txt
FSF_pages.txt
MON_part1.txt
BQT_v1_pages.txt
BQT_v2_pages.txt
incoming/ARY/ARY_pages.txt
=== پنچر ===
=== ینچر ===
BQT_v2_pages.txt
MON_part1.txt
```


## [2026-09-14T00:57:57.726Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"پیختن\" MON_part1.txt | head; echo \"=== context ===\"; grep -n \"پیختن\" MON_part1.txt | head -3 | cut -d: -f1 | while read l; do sed -n \"$((l-8)),$((l+8))p\" MON_part1.txt; echo \"-----\"; done"
}
```


### [2026-09-14T00:57:58.791Z] TOOL RESULT

```
13223:اشس‌پوختن: 30 [- اشسپیختن < 
=== context ===
پر و فراوان. (قا.) حرکت دخیل. (شیم.) 
اندازه‌ای از ماده که در ترکیب بیشتر از آن 
محتاج نباشد. (پز.) اندازة تحمل بدن دوا را. 
اشباه: [ع.] (مصل.) مانند کسی 
شدن,» مانند شدن به چیزی» با چیزی مانیدن. 
اشسه: (ع.] (ص تفض..) شبیه تر» 
ماننده‌تر ماناتر. 

اشس‌پوختن: 30 [- اشسپیختن < 
اشپوختن - اشبیختن] (مسصم.) پاشیدن» 
پرا کندن» پراکنده کردن» افشاندن. گل نم 
ردن. ترشح کردن. 

اشپون: اجه (.) (چاپ.) سرب باریکی که 
میان هر دو سطر نهند تا فاصلهً مطلوب پیدا 
شو د. (چاد.) و احد طول سطر. 

-----
```


## [2026-09-14T00:57:59.018Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ینچر\" MON_part1.txt | head; echo \"=== ctx ===\"; grep -n \"ینچر\" MON_part1.txt | head -3 | cut -d: -f1 | while read l; do sed -n \"$((l-6)),$((l+6))p\" MON_part1.txt; echo \"-----\"; done"
}
```


### [2026-09-14T00:58:00.015Z] TOOL RESULT

```
32828:ینچر ؛ 027627 (.) سوراح شدن لاستکك 
=== ctx ===
برای جبران در آخر هر سال پنج روز دیگر 
(بنام بنجه دزدیده) می‌افرودند تا سال 


شمسی درست سیصد و شصت و پنج روز 
باشد» خمسه مسترقه» بهی زکك» بنجکك. 
ینچر ؛ 027627 (.) سوراح شدن لاستکك 
پسنچه: (ه)ما«هم [- پنجه - بنجه] (.) 
بیشانی» ناصیه. 

پ‌ند: 0274 (.) اندرز» صلاحگویی» 
نصیحت» موعظه» وعظ ذ کر تذکیر. عهده 
و 
-----
```


## [2026-09-14T00:58:12.113Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nprint('ff',t.count(chr(12)))\nlines=t.split('\\n')\nprint(len(lines))\ni=32828\n# find nearest page markers\nimport re\nfor j in range(i-1,max(0,i-400),-1):\n    if re.search(r'^\\s*[۰-۹\\d]{2,4}\\s*$', lines[j]):\n        print('marker before at',j,repr(lines[j])); break\nfor j in range(i,min(len(lines),i+400)):\n    if re.search(r'^\\s*[۰-۹\\d]{2,4}\\s*$', lines[j]):\n        print('marker after at',j,repr(lines[j])); break\nEOF"
}
```


### [2026-09-14T00:58:13.348Z] TOOL RESULT

```
ff 0
99340
marker before at 32787 '۳۹۹ '
marker after at 33053 '۳۷ '
```


## [2026-09-14T00:58:18.514Z] TOOL CALL #53: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T00:58:18.521Z] TOOL RESULT

```


```


## [2026-09-14T00:58:22.222Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/پیختن/",
 "prompt": "What do the dictionaries (فرهنگ معین، لغتنامه دهخدا، فرهنگ عمید) say for the entry پیختن? Give the glosses and any etymology tags verbatim, and any verses cited."
}
```


## [2026-09-14T00:58:23.764Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/سپوختن",
 "prompt": "Give the full Persian entry for سپوختن: etymology (Middle Persian form, Proto-Iranian root), meanings, and any cited sources (Cheung, Hasandust, MacKenzie)."
}
```


### [2026-09-14T00:58:27.194Z] TOOL RESULT

```
# Persian Dictionary Entries for پیختن

**لغتنامه دهخدا:**
Defines the term as "پیچیدن" (twisting), "برتافتن" (throwing), and "پیچاندن" (winding). Includes classical verses from Rudaki, Ferdowsi, and other poets illustrating usage.

**فرهنگ معین:**
Lists two meanings: "۱ - پیچیدن . ۲ - پخش کردن ، افشاندن" (twisting and scattering/dispersing).

**فرهنگ عمید:**
Provides the gloss "در هم پیچیدن، پیچیدن" (intertwining, twisting) with a citation: "همه طومارها به هم درپیخت / داد تا پیک پیش خسرو ریخت" (Nizami).
```


### [2026-09-14T00:58:30.558Z] TOOL RESULT

```
# Persian Entry: سپوختن (sepūxtán)

## Etymology
From Middle Persian *spwhtn'* (spōxtan, spōz-), meaning "to thrust; to overstep, disobey; to delay, reject." The entry notes: "Compare Old Armenian _սպուժեմ_ (spužem), an Iranian borrowing."

## Meanings (Archaic)

1. **To thrust, poke, press, penetrate** — exemplified in 8th-century poetry by Abu'l-Abbas Marwazi
2. **To sodomize** — illustrated through 1920s verse by Iraj Mirza
3. **To drive away, fend off, ward off, repel** — from 10th-century Shahnameh by Ferdowsi
4. **To delay, prolong** — also from Ferdowsi's Shahnameh

## Cited Sources

- **Cheung, Johnny (2007)**: _Etymological Dictionary of the Iranian Verb_, Brill, page 357
- **MacKenzie, D. N. (1971)**: _A Concise Pahlavi Dictionary_, Oxford University Press, page 76
- **Dehkhoda Dictionary Institute**: Dehkhoda Dictionary entry
- **Hasan Amid (1985)**: _Farhang-e Fārsī-e ʿAmīd_ dictionary
```


## [2026-09-14T00:58:53.828Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD spoxtan/pexak ===\"; grep -n \"spwhtn\\|spōxtan\\|spoxtan\\|spwc\\|spōz\" PHD.txt PHD_mackenzie.txt 2>/dev/null | head -10; echo \"=== PHD pexak ===\"; grep -n \"pēxak\\|pexak\\|pyhk\\|pēx \" PHD.txt PHD_mackenzie.txt 2>/dev/null | head -10"
}
```


### [2026-09-14T00:58:53.901Z] TOOL RESULT

```
=== PHD spoxtan/pexak ===
PHD.txt:568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
PHD_mackenzie.txt:4621:spoxtan, spoz· [spwhtn', spwc- I M <spwxt, N sip",] thrust; overstep,
PHD_mackenzie.txt:4624:spoz [spwc I N sipoz] disobedience; delay.
PHD_mackenzie.txt:6373:delay (v.) spoxtan.                        determined brin.
PHD_mackenzie.txt:6430:disobey spoxtan.                        dragon az, Azdahag; (astr.) Gozihr.
PHD_mackenzie.txt:7222:overstep spoxtan.                      peacock fras(a)murw.
PHD_mackenzie.txt:7416:reject anaftan, spoxtan.                 rest (n.) asanih, asayisn, haspin.
PHD_mackenzie.txt:7779:testament handarz.                        thrust spoxtan.
=== PHD pexak ===
```


## [2026-09-14T00:58:55.879Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB ===\"; grep -n \"spōxtan\\|spoxtan\\|spōz\\|spwhtn\" NYB_vol2_glossary.txt | head -10; echo \"=== NYB pexak ===\"; grep -n \"pēxak\\|pexak\" NYB_vol2_glossary.txt | head -5; echo \"=== FSF عنبر بیختند ===\"; grep -n \"بیختند\\|عنبر همی\" FSF_pages.txt | head -10"
}
```


### [2026-09-14T00:58:55.950Z] TOOL RESULT

```
=== NYB ===
1520:framän [plm'n'] order, command 12). 11310 ete.; ~ būt hac... + inf. it was ordained, decreed by ... that 3611-13; ~ dätan to issue orders, to order 191 ete. passim; ~ patigraftan to comply with an order 38!; — be spoxtan to disregard, disobey an order 3? (cf 12"); v. also
3498:spöxtan [spwhtn'] spož- [spwe-] to throw, to drive 2974-%; bg ~ to defy, to dis- regard 3? (cf spož-kar); to drive out 66". — Prth: Arm. lw. spuž-em ‘to postpone, to delay, to procrastinate’; MPrs (lw.) *spwxt (A-H I); Paz. pres. spož-; NP sipoatan svpoz-.
5856:‘sprhm: spram ‘spwr: spurr ‘spwryg: spurrik ‘spwxt: spoxtan ‘spyd-: spét ‘spyd-pr: parr
6807:spih(a)r, spahir: spihr sp6z-: spoxtan
7403:sipoxtan: spoxtan
=== NYB pexak ===
=== FSF عنبر بیختند ===
5938:                       ‫که ه‬                          ‫ز بر مشک و عنبر همی بیختند‬
9187: ‫ز بر مشک و عنبر همی بیختنا‬                  ‫(‪)۳-۸۴-۱۱۷‬‬
13808:‫زبر مشک و عنبر همی بیختند‬                          ‫(‪)۲-۹۲۱-۹۹۹۱‬‬
```


## [2026-09-14T00:59:12.950Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nb=t.split('\\f')\nimport re\nfor i in (71,):\n    print('=== block',i,'page?',i+72,'===')\n    print(b[i][:4000])\nEOF"
}
```


## [2026-09-14T00:59:13.921Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD peuk ===\"; grep -n -i \"peuk\\|peug\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T00:59:14.132Z] TOOL RESULT

```
=== block 71 page? 143 ===
 in                                          ,U-   —„L
                                                   .
                                                         *.L*3l 3
                                                                                                                                                                  U;^li«.U»jl,                                                                          n«

                                                                         •   >* * :bOy:
                                                                                  •
                                                                                                                    »|J
                                                                                                                                (4rm.    bunr^j' (A iWb. 9 69 ) budhnZ z l***** bona-                                                               :*"
UtVfc.       918)         bSdha -    : ,j*Sj** baod/bao<fa                                          :       t-              |
                                                                                                                                        (tfir.   Wan.   II. 48)        bwn^*                     Gram.                           123)
            •f J  >>W        bOi:^ (Mir. Nan. II, 48) bwy                                           :    >!»                J

                                                                                                                                                                           .bun: lsjAf bin: j^*/ ' a*» 7

       •   1Y/H^ 'u^iS*'^^: bOy I pak;                                           ^* -                   -*-»                i
                                                                                                                                 jlrgAjfgijAjijI     :bun abaz kardan:                               >iv»»^j*i               \«^«j
*Ai*jl^^l A».Li>j1                  L^I    =J   j*So-l^>^. n jl^ -tf*:bOy:                                        ^|                      lf/1Y<^    >J^oAl<^V :bur* kardag: \a>J»3ii»
                          •   H-T/IT^        -fi/lY^      (trV> «j>^ Jj J ) '^'   '



                                                                                                                                                                             /                   *                  Sj
                                                                                                                                                                       •c£*jp JijUT j±f<                    ,            ;   bunis                  :   -*omj
                        v
              .Oi-j>*.:x astan: B'yHWN, stn                                      >*:        hyowivMi
                                                                             :
                                                                                                                                                    (raya^ia.      79)       o UT '£3^:bun!h                                         :        fcjfcfc

                                                                                                                                                                                                        •       lY/r^ .iv/Y^                                    l«
xw'stn             xjsli      (GNPB.       110) svadati,                */svad-                 jl           L              |

     1—r/)\J .(^y^j xvastan iL(Mir.Man.                                               II,       48)                                                                                  (*U-       .J.IT           :bavandag:
                                                                                                                                                                                 •
```


### [2026-09-14T00:59:14.201Z] TOOL RESULT

```
=== AHD peuk ===
846:ré, feather, in Old English fether, feather: FEATHER. 2. Latin petere, to go toward, seek: -PETAL, PETITION, PETULANT; APPETITE, COMPETE, IMPETUS, PERPETUAL, REPEAT. 3. Suffixed form *pet-nd in Latin penna, pinna, feather, wing: PANACHE, PEN!, PENNA, PENNATE, PEN- NON, PINNA, PINNACLE, PINNATE, PINNATI-, PINNULE. 4. Suffixed form *pet-ro- (see 6ku-). 5. Suffixed form *pet-yo- in Latin propitius, favorable, gracious, originally a religious term meaning “falling or rushing forward,” hence “eager,” “well-disposed” (said of the gods; pro-, forward; see per'): PROPITIOUS. 6. Suffixed zero-grade form *pt-ero- in Greek pteron, feather, wing, and pterux, wing: -PTER; ACANTHOPTERYGIAN, APTERYX, ARCHAEOP- TERYX, COLEOPTERA, MECOPTERAN, PERIPTERAL, PLE- COPTERAN, PTERIDOLOGY, PTEROCERCOID, PTERYGOID. 7. Suffixed zero-grade form “pt-ilo- in Greek ptilon, soft feathers, down, plume: COLEOPTILE. 8. Suffixed variant form *pté-no- in Greek pténos, winged, flying: STEAROP- TENE. 9. Reduplicated form *pi-pt- in Greek piptein, to fall: PTOMAINE, PTOSIS; PERIPETEIA, PROPTOSIS, SYMP- TOM. 10. O-grade form “pof- in Greek potamos (-amo-, Greek suffix), “rushing water,” river: HIPPOPOTAMUS. [Pok. 2. pet- 826.] pete-. To spread. 1. Suffixed o-grade form “pota)-mo- in Germanic *fathmaz, “length of two arms stretched out,” in Old English fethm, fathom: FATHOM. 2. Suffixed (stative) variant zero-grade form *pat-é- in Latin patére, to be open: PATENT, PATULOUS. 3. Variant zero-grade form in nasalized form *pat-no- probably in Latin pan- dere (past participle passus < *pat-to-), to spread out: PACE!, (PAS), (PASS), PASSIM; EXPAND, REPAND. 4. Suf- fixed form *pet-alo- in Greek petalon, leaf: PETAL. 5. Suf- fixed form *pet-ano- in Greek patané (? < *petand), platter, “thing spread out”: (PAELLA), PAN!, PATEN, (PATINA!), (PATINA2). [Pok. 1. pet- 824.] [petra. Cliff. Greek noun. Collective formation from petros, rock, stone (of unknown origin). PETRO-, PET- ROUS; PARSLEY, PETRIFY, SALTPETER.] peu-. To cut, strike, stamp. 1. Suffixed (participial) zero-grade form *pu-to-, cut, struck, in: a. Latin putdre, to prune, clean, settle an account, think over, reflect, consider: PUTAMEN, PUTATIVE; (ACCOUNT), AMPUTATE, COMPUTE, COUNT!, DEPUTE, DISPUTE, IMPUTE, REPUTE; b. possibly Latin puteus, well (> Old English pyét): Prt’. 2. Variant form *pau- in: a. suffixed form *pau-yo- in Latin pavire, to beat: PAVE, (PAVE); b. suffixed (stative) form *paw-é- in Latin pavére, to fear (< “to be struck”): PAVID; C. perhaps Greek paiein, to beat: ANAPEST. [Pok. 3. péu- 827.] peue-. To purify, cleanse. Suffixed zero-grade form *pii-ro- (< *pua-ro-) in Latin purus, pure, and purgdre, to purify (< “piir-igdre; second element agere, to drive; see ag-): PURE, PURGE, PURITAN; COMPURGATION, DEPU- RATE, EXPURGATE, (SPURGE). [Pok. 1. peu- 827.] peuk-. Also peug-. To prick. Zero-grade form “pug-. 1. Suffixed form *pug-no- in Latin pugil, pugilist, and pugnus, fist, with denominative pugndare, to fight with the fist: PONIARD, PUGILISM, PUGIL STICK, PUGNACIOUS; IMPUGN, OPPUGN, REPUGN. 2. Nasalized zero-grade form *pu-n-g- in Latin pungere, to prick: BUNG, POIGNANT, POINT, POINTILLISM, PONTIL, (POUNCE!), (POUNCE?), PUNCHEON!, PUNCTUATE, PUNCTURE, PUNGENT; COM- PUNCTION, EXPUNGE, SPONTOON, TRAPUNTO. 3. Greek pugmé, fist: (PYGMAEAN), PYGMY. [Pok. peuk- 828.] pezd-. To fart. 1. Suffixed form *pezd-i- in Germanic *fistiz, a fart, in Middle English fisten, to fart: FEIST, FIZZLE. 2. Latin pédere, to fart: PETARD. 3. Possibly Latin pédis, louse (? < “foul-smelling insect”): PEDICU- LAR. See also perd-. [Pok. pezd- 829, 2. peis- 796.] peter-. Father. 1. Germanic *fadar in Old English feder (> Middle English fader), father: FATHER; FOREFATHER. 2. Latin pater, father (> patrare, to bring about): PADRE, PATER, PATERNAL, PATRI-, PATRICIAN, PATRIMONY, PA- TRON; EXPATRIATE, IMPETRATE, PERPETRATE. 3. Greek
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1387:COMMODITY med- COMMON mei-! COMMOTION meue- COMMUNE mei-1 COMMUNICATE mei-1 COMMUNISM mei-1 COMMUTE mei-1 COMPACT! pag- COMPANION pa- COMPANY pa- COMPARE pera-2 COMPART pere-2 COMPASSION pé(i)- COMPEL pel-6 COMPELLATION pel-6 COMPENDIUM (s)pen- COMPENSATE (s)pen- COMPETE pet- COMPLACENT plak-! COMPLAIN plak-2 COMPLECT plek- COMPLETE pele-1 COMPLEX plek- COMPLICATE plek- COMPLICE plek- COMPLIMENT pele-1 COMPLY pele-1 COMPONENT apo- COMPORT per-2 COMPOSE apo-, paus-, COMPOSITE apo- COMPOSITION apo- COMPOUND apo- COMPRADOR pere-1 COMPREHEND ghend- COMPRESS per-5 COMPRISE ghend- COMPROMISE (s)meit(9)- COMPUNCTION peuk- COMPURGATION peue- COMPUTE peu- COMRADE kamer- con! kom
1487:EXPOSTULATE prek- EXPOUND apo- EXPRESS per-5 EXPUNGE peuk- EXPURGATE peue- EXQUISITE quaerere EXSCIND skei- EXSECT sek- EXSICCATE seikw- EXTANT sta- EXTEND ten- EXTENUATE ten- EXTERIOR eghs EXTERMINATE ter- EXTERNAL eghs EXTINGUISH  steig-
1673:ILLATION tele- ILLITERATE deph- ILLUMINATE leuk- ILLUSION leid- ILLUSTRATE leuk- IMBECILE bak- IMBIBE p6(i)- IMBRICATE ombh-ro- IMBRUE_bhreu-2 IMBUE ombh-ro- IMMACULATE macula IMMANENT men-3 IMMATURE ma-1 IMMENSE mé6-2 IMMERSE mezg-! IMMINENT men-2 IMMIX meik- IMMODERATE med- IMMODEST med- IMMOLATE mele- IMMORTAL mer-2 IMMUNE mei-1 IMMURE mei-3 IMP bheue- IMPAIR ped-1 IMPALE pag- IMPARITY pere-2 IMPART pere-2 IMPEACH ped-1 IMPECCABLE ped-1 IMPECUNIOUS peku- IMPEDE ped-! IMPEL pel-6 IMPEND (s)pen- IMPERATIVE pere-1 IMPERIAL pere-1 IMPETRATE peter- IMPETUS _pet- IMPINGE pag- IMPIOUS pius IMPLEMENT pele-1 IMPLICATE plek- IMPONE apo- IMPORT per-2 IMPORTANT per-2 IMPORTUNE per-2 IMPOSE apo- IMPOTENT poti- IMPOUND bend- IMPRECATE prek- IMPRESS! per-5 IMPRIMIS_ per! IMPRINT per-5 IMPROBITY pert IMPROMPTU em- IMPROVE es-, pert IMPUDENT (s)peud- IMPUGN peuk- IMPUNITY kweij-1 IMPUTE peu- IN-l ne
1988:OPINION op-* OPISTHOBRANCH epi OPISTHOGNATHOUS epi OPIUM s(w)ok"o- OPPORTUNE per-2 OPPOSE apo- OPPRESS per-5 OPPROBRIUM bher-1 OPPUGN peuk- OPSIN OkW-
2111:POETIC kWej-2 POGROM apo-, ghrem- -POIESIS kwej-2 -POIETIC kwej-2 POIGNANT peuk- POIKILOTHERM peig-1 POILU pilo-
2112:POINT peuk- POINT-DEVICE weidh- POINTILLISM peuk- POISE! (s)pen- POISON pO(i)- POKE’ beu-1 PoLack pele-2 POLE! kwel-1
2114:POLICE pele-3 POLICLINIC pela-3 POLICY! pele-3 POLICY? deik- POLIOMYELITIS pel-2 POLIS pele-3 POLISH pel-6 POLITIC pele-3 POLITY pele-3 POLKA pele-2 POLLEN pel-1 POLLEX pol- POLLUTE leu-2 POLTERGEIST bhel-4, gheis- POLTROON pau- POLY- pele-1 POLYGALA melg- POLYGLOT glégh- POLYGYNY gWen- POLYHISTOR weid- POLYMATH mendh-! POLYNYA pele-2 POLYP ped-1 POLYPNEA pneu- POLYPOD ped-1 POLYTECHNIC teks- POLYTENE ten- POLYTHEISM dhés- POLYTOCOUS tek- POLYTROPHIC threph- POMACE pomum POMADE pomum POME pomum POND bend- PONDER (S)pen- PONDEROUS (S)pen- PONIARD peuk- PONS pent- PONTIFEX dhé-!, pent: PONTIFF pent- PONTIL peuk- PONTINE pent- PONTOON pent- PONY pau-
2125:POST- apo- POSTBELLUM duellum POSTERIOR apo- POSTICHE apo- POSTMERIDIAN deiw- POST-MORTEM apo-, mer-2 POSTPARTUM _pere-1 POSTSCRIPT skribh- POSTULATE prek- POSTURE apo- POTABLE p0(i)- POTATION pd(i)- POTATORY pd(i)- POTENT poti- POTION po(i)- POTPOURRI pu-2 POUCH beu-! POULARD pau- POULTICE pel-1 POUNCE! peuk- POUNCE? (s)poi-mo- POUNCE3 peuk- POUND! (s)pen- POUNDS bend- POUSETTE pel-6 POUT beu-! POVERTY pau- POWDER pel-1 POWER poti- PRAAM per! PRACTICAL prak- PRACTICE prak- PRAEDIAL wadh-1 PRAEMUNIRE mei-3 PRAENOMEN no-men- PRAETOR ei-1 PRAGMATIC prak- PRAISE per-6 PRANDIAL ed- PRATINCOLE kwel-1 PRAXIS prak-
2140:Puc’ ped-1 PUGILISM peuk- PUGIL STICK peuk- PUGNACIOUS peuk- PUISNE apo-, gene- PUKKA pekw- PULICIDE plou- PULLET pau- PULLEY kwel-1 PULMONARY pleu- PULSATE pel-6 PULSE! pel-6 PULSE? pel-1 PULVERIZE pel-1 PUMICE (s)poi-mo- PUMPKIN pekw- PUNCH? penk¥e PUNCHEON! peuk- PUNCTUATE peuk- PUNCTURE peuk- PUNGENT peuk- PUNISH kWej-1 PUNITORY kvei-1 PUNKA peg- PUNT! pent-
2144:PUSH pel-6 PUSILLANIMOUS an@-, pau- PUSTULE pu-1 PUTAMEN peu- PUTATIVE peu- _ PUTREFY dhé-1, pu-2 PUTRESCENT pu-@ PUTRID pu-2 PYCNIDIUM puk-! PYCNOMTER puk-! PYELITIS pleu- PYGMAEAN peuk- PYGMY peuk- PYKNIC puk-! PYLON pulé PYLORUS pulé PYO- pu-2 PYRACANTHA = ak- PYRARGYRITE arg- PYRE pir- PYRENE piiro- PYRETIC  pir- PYRITES pir- PYRO- pur- PYROPE okw- PYROSIS pir- PYROXENE xenos PYRRHOTITE pir- PYRUVIC ACID 6g-
2178:REIGN reg-! REIMBURSE bursa REINDEER dheu-1, ker-1 REINFORCE bhergh-2 REITERATE i- REJECT yé- REJOICE gau- REJUVENATE yeu- RELAPSE leb-! RELATE tele- RELAX slég- RELAY slég- RELEGATE leg-1 RELENT lento- RELIEVE leg¥h- RELINQUISH leikw- RELUCENT leuk- RELUCT leug-! RELY leig-1 REMAIN men-3 REMAND man-2 REMARK merg- REMEDY med- REMEMBER (s)mer-! REMEX ere-! REMINISCENT men-! REMIT (s)meit(a)- REMORA mere- REMORSE mer-2 REMOTE meue- REMOVE meue- REMUDA mei-1 REMUNERATE mei-! RENAISSANCE gene- REND rendh- RENDER do- _ RENDEZVOUS wOS RENEGADE ne RENEGE ne RENITENT kneigh- RENOUNCE neu-! RENOVATE newo- RENOWN no-men- RENT! do- REPAIR! pere-1 REPAND pete- REPARTEE pere-2 REPAST pa- REPEAT pet- REPEL pel-6 REPENT2 rép-1 REPERTORY pere-! REPINE kWei-1 REPLENISH pele-! REPLETE pele-1 REPLEVIN plegan REPLICATE plek- REPORT per-2 REPOSE! paus- REPOSIT apo- REPREHEND ghend- REPRESENT e@S- REPRESS per-5 REPRIMAND per-5 REPRISAL ghend- REPRISE ghend- REPROACH pert REPROVE per? REPTILE rép-1 REPUBLIC ré- REPUDIATE (s)peud- REPUGN peuk- REPUTE peu-
2279:SPECIOUS spek- SPECTACLE spek- SPECTRUM spek- SPECULATE spek- SPECULUM spek- SPEECH spreg- SPEED spé-1 SPELL! spel-3 SPELL? spel-3 SPELT! spel-! SPERM! sper-4 SPEW spyeu- SPHENE spé-2 SPHENO- spé-2 SPICA spei- SPICA_ spei- SPICULUM spei- SPIDER (s)pen- SPIKE! spei- SPIKE? spei- SPILE spei- SPILL! spel-1 SPILL? spei- SPIN (s)pen- SPINDLE (s)pen- SPINE spei- SPINEL spei- SPINIFEX dhé-1 SPINNEY spei- SPIRACLE spirare SPIRE! spei- SPIRE? sper-2 SPIRIT spirare SPIT! spyeu- SPIT? spei- SPITTLE spyeu- SPITZ spel- SPLANCHNIC spelgh- SPLEEN spelgh- SPLENDID spel-2 SPLICE splei- SPLINT splei- SPLINTER splei- SPLIT splei- SPOIL spel-1 SPOKE! spei- SPONDEE spend- SPONSOR spend- SPONTANEOUS (s)pen- SPONTOON peuk- SPOON spé-2 SPOOR spere- SPORADIC sper-4 SPORE sper-4 SPORO- sper-4 SPORRAN bursa SPORT per-2 SPOUSE spend- SPOUT spyeu- SPRAG (s)preg- SPRAWL sper-4 SPREAD sper-4 SPREE ghend- SPRING spergh-
2406:TRAPUNTO peuk- TRAUMA tera-1 TRAVAIL pag- TRAVE treb- TRAVEL pag- TRAVESTY wes-4 TRAY deru TREACLE ghwer- TREAD der-1 TREADLE der-1 TREASON d6- TREAT tragh- TREBUCHET beu-1 TRECENTO dekm, trei- TREE deru TREFOIL bhel-3 TREMATODE tere-! TREMENDOUS trem- TREMOR trem- TREMULOUS trem- TRENCH tera-2 TREPAN! tere-1 TREPHINE trei- TREPID trep-1
```


## [2026-09-14T00:59:47.221Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 tools/ref_page.py SNS:143 --image 2>&1 | head -40"
}
```


### [2026-09-14T00:59:48.548Z] TOOL RESULT

```
no scan of SNS covers printed page 143 (see 'scans' in refs_online.json)
```


## [2026-09-14T00:59:50.713Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nb=t.split('\\f')\nimport re\nfor i,x in enumerate(b):\n    if re.search(r'p[eE5S]xak|pexk|pyxk|p.xak', x) and i<200:\n        print(i, x[:200])\n# find blocks containing 'petrOt' or 'pes ud pas'\nfor i,x in enumerate(b):\n    if 'petr' in x or 'pes ud' in x:\n        print('P',i, [l.strip()[:80] for l in x.split('\\n') if 'petr' in l or 'pes ud' in l])\nEOF"
}
```


### [2026-09-14T00:59:51.834Z] TOOL RESULT

```
P 87 ['•   ****** **      0-* ***< tJa-** Jttf :petret:                   yW>**w']
P 226 ['pes ud pas 143/2           pusih 138/19                      radSn 226/4        ', 'petrSt 142/14              pust 139/5-10                     radlh 226/5        ']
```


## [2026-09-14T00:59:56.263Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nb=t.split('\\f')\nfor i in (87,88):\n    print('==== block',i,'====')\n    print(b[i][:3500])\nEOF"
}
```


### [2026-09-14T00:59:57.374Z] TOOL RESULT

```
==== block 87 ====
                              Li tebtjlj                                                                                       Laj   cu^L *.L<-I,
                                                                                                                                                                                 ITT


                                                              VW J                                    TMVl.tf                   3$w>;X           .^ :frazand: J*io
                                                                      -^«
     .   .       v   ^.J.: pfiiudpas:                      Jut*   -




                                                                                                  l*iiL      ,   C



                 »«*'   80 >P lstra    S
                                           J
                                            l,h        "    (i-*^
.TW*J*/1*«
                                                                                                                         .jKiT.lj^ :payd5g/p€dag:
                                                                                                                                                                     1uh»U
                                                                                       'pratuafca- pratyafic- .
                                                                                       («-. *«„. „, „., pyd ,
                                                                                                                **                    ^      *
                                                                                                                                                 p . tytta - :      ^,**,,
                                                                                                                                                                             ,

                                                                                                                                     g       s
                                                                                                                                                  ^ WEm
                                                                                        ./***.;       *«** .44Vfc-^-P*ty'k                                 :
                                                                                                                                                               ^^^
                                                                                       •A/IT   J .^jKiT.^l^,^^^. P aydagIhgd:Y«^^^o
                                                                          *'
    ,_,.,., i,   % *u. *- <«•"* * 5§ak: ^'J'**
                                                                                        -_i
                                                                                                                     ^o^ '*£,>*• Payd3genId: ** *£-****>
                                                                                                                                         :

                                                                                       •c-U«4,»m        :   paydagenld ested: ^v*'*» yaVAu^y


                         ./, =nava-pixa                „ pixa-: *.
  M m.
                                                   ,
         10451
           
==== block 88 ====
                                                                                                    U; ^__L o-L ^l,                             Iff




                                                                 pelotan      I    ram §rbad: Y&b***J(F* twt^xjjw               :   •A.T,_,bSjJ




                                                                                                                        •j5j«   :pSrCz: C^Jf
                                                                 :   jzk(AiWb.      862)   aojah-       :j'       pairi. aojastara-:^-
                                                                     PYLwzy   :    j V^ tfj-ky (Mir. Man.              II,   64) pyrwz




                                                                         Xo/tt^         f^tf^V'^)        'ifeiW        :p§r6zgar:         >J(2P-»«J



                                                                        T/TT^ lT-f/H^           >j?/j£jN          :pSrOzgartar: Vjj^'O


                                                                                  \^/U«^      -CMpAxW rperOzgartum: -6»)°^ 3 k                       j *->




                                                                                  M/\o<£   m ^ /V       Wif/fc.        817)pa§man-         :   fc-


                                                                                   .YA/i««^     -j^j^         :   P Sm * 92»w: -*»w» « ^«J
                                                                                                        *

                                         /-tap-:*-,'
                      , ^
                            tapayeiti,
     t 4Pt i,   Aap- *.—       p
                                     83) ta£6an    , ..



                            ; c gnpe

\°


                                                   taXt!   ^""
                       \T/T^     (   VV*«)*»   8
```


## [2026-09-14T01:00:07.601Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nb=t.split('\\f')[87]\ni=b.find('nava-pixa')\nprint(repr(b[i-1500:i+1200]))\nEOF"
}
```


### [2026-09-14T01:00:08.708Z] TOOL RESULT

```
'                                                                    ,\n\n                                                                                                                                     g       s\n                                                                                                                                                  ^ WEm\n                                                                                        ./***.;       *«** .44Vfc-^-P*ty\'k                                 :\n                                                                                                                                                               ^^^\n                                                                                       •A/IT   J .^jKiT.^l^,^^^. P aydagIhgd:Y«^^^o\n                                                                          *\'\n    ,_,.,., i,   % *u. *- <«•"* * 5§ak: ^\'J\'**\n                                                                                        -_i\n                                                                                                                     ^o^ \'*£,>*• Payd3genId: ** *£-****>\n                                                                                                                                         :\n\n                                                                                       •c-U«4,»m        :   paydagenld ested: ^v*\'*» yaVAu^y\n\n\n                         ./, =nava-pixa                „ pixa-: *.\n  M m.\n                                                   ,\n         10451\n                                                                                                  •   ****** **      0-* ***< tJa-** Jttf :petret:                   yW>**w\n*^\'v**a.*k****** snas:                             **""^                                       -H-f-M/T*                 MiW. 834) P aiti.rae0wa ,4.\n                                                                          .\n                                                                      T       .\n                                                                                                                                                                                       )6\n\n                                                                                      [P«iS                 ^^paitiS :fc. .J^^\n                                                                                      i*tr.\n                                                                                                  :\n\n\n\n                                                                                                  py5:'
```


## [2026-09-14T01:00:18.810Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in \"سپوختن\" \"سپوز\" \"پیختن\" \"پیچیدن\"; do echo \"=== $p ===\"; grep -n \"$p\" incoming/ARY/ARY_pages.txt | head -5; done"
}
```


### [2026-09-14T01:00:19.725Z] TOOL RESULT

```
=== سپوختن ===
=== سپوز ===
=== پیختن ===
=== پیچیدن ===
5459:فارسی (//۳85۸54): تابیدن, تافتن, تاب (به چم اگرداندن" و "پیچیدن)
5905:فارسی (28/814): تنجیدن, تنج (به چم "بخود پیچیدن" و درهم فشرده شدن۳)
```


## [2026-09-14T01:00:20.518Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN pivot ===\"; grep -n \"^pivot\\|pivot, n\\.\" KLN_1966.txt KLN_1971.txt | head -5; echo \"=== KLN puncture ===\"; grep -n \"puncture,\" KLN_1966.txt | head -3; echo \"=== SKT pivot ===\"; grep -n -i \"pivot\" SKT.txt | head -5"
}
```


### [2026-09-14T01:00:20.593Z] TOOL RESULT

```
=== KLN pivot ===
KLN_1971.txt:39674:pivot; that on which something turns’, which is 
KLN_1971.txt:183525:pivot, n., a point or pin, etc., on which something 
KLN_1971.txt:183528:pivot-er, n. 
KLN_1971.txt:183530:pivot, intr. v., to turn about on a pivot; tr. v., to 
KLN_1966.txt:28972:pivot,  n.,  a  point  or  pin,  etc.,  on  which  something turns.  —  F.  pivot,  of  uncertain  origin. Derivatives:  pirot-al,  adj.,  pivot-al-ly,  adv., pivot-er,  n.
=== KLN puncture ===
72:aspirin,  n.  ( pharm .)  —  A  hybrid  coined  by  H.  Dreser  in  Pfliiger's  Archiv  in  1 899.  The  acetylo-salicylic acid  occurs  in  the  flowers  of  the  plant  Spiraea  ulmaria.  In  order  to  distinguish  from  this  natural  pro¬ duct  the  same  substance  gained  chemically,  the  word  aspirin  was  formed  by  Dreser  from  priv.  pref. a-,  the  above  mentioned  plant  Spiraea,  and  chem.  suff.  -in.  Hence  aspirin  prop,  means  ‘acetylo-sali¬ cylic  acid  which  is  gained  not  from  the  Spiraea  ulmaria  (but  in  a  chemical  way)’, astigmatism,  n.,  defect  of  the  eye  that  prevents  the  rays  of  light  from  converging  to  a  point  on  the  retina (med.  and  optics ).  —  Coined  by  the  English  mathematician  and  philosopher  William  Whewell  ( 1 794- 1866)  in  1819  fr.  priv.  pref.  a-  and  Gk.  a-uypa,  gen.  crTlyiiaTog,  ‘a  prick,  puncture,  mark’.  See  stig- matic  and  -ism.
1556:acupressure,  n.,  the  checking  of  bleeding  by  the pressure  of  a  needle  on  the  bleeding  vessel (surg.)  —  Compounded  of  L.  acus,  ‘needle’  and pressura  ‘pressure’.  See  acus  and  pressure, acupuncture,  n.,  puncture  of  the  ailing  part  with a  needle  to  relieve  pain.  —  Compounded  of  L. acus,  ‘needle’,  and  punctura,  ‘a  pricking’.  See acus  and  puncture.
3742:asthmatic,  adj.  —  L.  asthmaticus,  fr.  Gk.  aaffpia- xixoc,  fr.  dahlia.  See  asthma  and  -atic. Derivative:  asthmatic-al-ly,  adv. astigmatic,  adj.,  pertaining  to,  or  suffering  from, astigmatism  (med.  and  optics).  —  See  next  word, astigmatism,  n.,  defect  of  the  eye  that  prevents the  rays  of  light  from  converging  to  a  point  on the  retina  (med.  and  optics).  —  Coined  by  the English  mathematician  and  philosopher  Wil¬ liam  Whewell  (1794-1866)  in  1819  fr.  priv.  pref. a-  and  Gk.  axiypa,  gen.  oxtypaxo?,  ‘a  prick, puncture,  mark’.  See  stigmatic  and  -ism. Astilbe,  n,,  a  genus  of  plants  of  the  saxifrage family  (bot.)  —  ModL.,  lit.  ‘not  shining’,  fr. priv.  pref.  a-  and  axiX()eiv,  ‘to  shine’.  See  stilbite. astir,  adv.  —  Formed  fr.  a-,  ‘on’,  and  stir, astomatous,  adj.,  having  no  mouth.  —  Formed fr.  priv.  pref.  a-  and  -stomatous. astonish,  tr.  v.  —  Obsol.  astony,  fr.  ME.  astonien , astonen,  which  is  formed  with  change  of  pref. fr.  e st oner  (whence  F.  etonner),  fr.  VL.  *exto- nare,  lit.  ‘to  strike  with  thunder’,  fr.  1st  ex- and  L.  tondre,  ‘to  thunder’.  See  thunder  and  cp. astound.  The  verb  astonish  was  influenced  in form  by  English  verbs  ending  in  -ish,  in  which this  suff.  is  the  equivalent  of  OF.  and  F.  -iss.
=== SKT pivot ===
14068:pivot,  a  pin  on  which  a  wheel,  &c. ttiros.  (F.  -  Ital.  -  Low  L.)  F.  pivot. Formed,  with  dimin.  sQfBx  •<>/,  from  Ital. a  piptr,  weakened  form  of  pipa^  a pipe.  The  Ital./iz-a  meant  (i)  a  i»pe,  ^j) a  tube  with  Fine  bore,  (3)  a  solid  peg.— Low  L  pipa,  a  pipe ;  allied  to  1*  jf>ipart,
23475:French  from  Italian  from  Lew  Latin : basement,  bassoon,  pivot.
```


## [2026-09-14T01:00:26.685Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"PIVOT [a-z()ā-]*\" AHD_watkins1985.txt | head; echo \"--- PUNCTUATE/POINT ---\"; grep -n -o \"PUNCTURE [a-z-]*\\|POINT [a-z-]*\\|PUNCTUATE [a-z-]*\" AHD_watkins1985.txt | head"
}
```


### [2026-09-14T01:00:26.781Z] TOOL RESULT

```
--- PUNCTUATE/POINT ---
2140:PUNCTUATE peuk-
2140:PUNCTURE peuk-
```


## [2026-09-14T01:00:27.446Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/pivot",
 "prompt": "What is the etymology given for \"pivot\"? Quote it."
}
```


### [2026-09-14T01:00:31.369Z] TOOL RESULT

```
# Etymology of "Pivot"

According to the Online Etymology Dictionary, the noun "pivot" originates from French. Here's the etymology:

"pin on which a wheel or other object turns," 1610s, from French *pivot*, from Old French *pivot* "hinge pin, pivot" (12c.), also "penis," a word of uncertain origin."

The word's figurative sense meaning "turning point" or "that which something hinges upon" emerged later, being recorded from 1813. The verb form developed by 1841, derived from the French *pivoter* and the noun form.
```


## [2026-09-14T01:00:41.151Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/پنچر/",
 "prompt": "What do فرهنگ معین، لغتنامه دهخدا، فرهنگ عمید say for پنچر? Quote the etymology tag / foreign origin marker verbatim (e.g. [فر.] [انگ.] and the Latin-script word)."
}
```


## [2026-09-14T01:00:42.217Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/puncture",
 "prompt": "Etymology of \"puncture\" and of \"point\" and \"punctuate\" — quote the Latin chain (pungere, punctus, punctura) and dates."
}
```


### [2026-09-14T01:00:46.917Z] TOOL RESULT

```
# Persian Dictionary Definitions of "پنچر"

**Farhang-e Moein:**
"(پَ چَ ) [ فر . ] (اِ. ) ۱ - سوراخ شدن لاستیک چرخ . ۲ - (عا. ) خسته ، زهوار دررفته"

The etymology markers indicate foreign origin: [فر.] (French) and [اِ.] (English).

**Farhang-e Amid:**
This source provides a definition focusing on the characteristic of a punctured tire that has lost its air, but does not include explicit etymology markers in the excerpt provided.

**Loghatnaameh-ye Dehkhoda:**
This dictionary is mentioned in the site's feature list but no specific entry excerpt is quoted on this page.
```


### [2026-09-14T01:00:48.393Z] TOOL RESULT

```
# Etymology of "Puncture," "Point," and "Punctuate"

## Latin Chain: *pungere* → *punctus* → *punctura*

**Puncture (noun):** Late 14c., from Late Latin *punctura* "a pricking," derived from Latin *punctus* (past participle of *pungere* "to prick, pierce"). The verb form emerged later in the 1690s.

**Point & Punctuate:** These words share the same Latin root *pungere* through the PIE base *\*peuk-* meaning "to prick." The etymological entry notes that this root forms "all or part of" numerous related words including point, punctuate, and punctuation.

## Key Dates

- **Late 14c.:** *Puncture* (noun) first recorded
- **Mid-15c.:** The sense of "act of perforating" documented
- **1690s:** *Puncture* (verb) emerges
- **Punctuate/Punctuation:** Also derived from the same *pungere* root, though specific dates for these terms aren't provided in the source material

The interconnected semantic thread across all three words traces back to the fundamental concept of making a hole or mark with a sharp point.
```


## [2026-09-14T01:01:02.506Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pewǵ-",
 "prompt": "What does this page say: root, meaning, derived terms (Latin pungō, Greek pugmē), and is any Indo-Iranian/Avestan descendant listed?"
}
```


## [2026-09-14T01:01:04.159Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%AE%D8%AA%D9%86",
 "prompt": "Is there a Persian entry for پیختن? Give its etymology and meanings if present."
}
```


### [2026-09-14T01:01:07.159Z] TOOL RESULT

```
# Summary of *pewǵ- Root Page

**Root and Meaning:**
The Proto-Indo-European root "*pewǵ-" has two primary meanings: "to punch, fist-fight" and "to prick, poke, stab."

**Notable Derived Terms:**
The page lists several important descendants, including:
- Latin *pungō* ("to prick, sting")
- Ancient Greek *pugmḗ* ("fist, fist-fight")
- Latin *pugil* ("boxer, fist-fighter")
- Latin *pugnus* ("fist")

**Indo-Iranian/Avestan:**
No Indo-Iranian or Avestan descendants are listed on this page. The documented descendants are confined to Italic, Hellenic, Celtic, Germanic, and Balto-Slavic language families.

The page notes this root is "probably not related" to *pewḱ- ("pine"), distinguishing it from a similar-sounding root.
```


### [2026-09-14T01:01:08.133Z] TOOL RESULT

```
# Persian Entry for پیختن

Yes, there is a Persian entry for **پیختن** (pixtan) on Wiktionary.

## Meaning

The word is listed as an **obsolete verb** with the following definition: "to twist; wrap"

## Etymology

The entry does not provide explicit etymological information about the word's origin or historical development.

## Additional Details

- **Present stem:** پیچ (pič)
- **Pronunciation:** [pʰiːxˈtʰæn] (IPA)
- **Derived terms:** پیچیدن (pičidan) and پیچاندن (pičândan)

The entry notes this is an archaic or obsolete form no longer in common use in modern Persian.
```


## [2026-09-14T01:01:18.180Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pic ‘to\\|\\*paič\\|pēčīdan\\|picidan\\|pixtan\\|pīxtan\" CHEUNG.txt | head -20; echo ---; grep -n \"to twist\" CHEUNG.txt | head -20"
}
```


### [2026-09-14T01:01:18.244Z] TOOL RESULT

```
13324:and Lith. rupéti (rupiü) “о worry’, Pol. rupic ‘to torment, irritate, tease’, Russ. rupit’ 
19103:290 *paič ? 
---
1675:iveendun/ivest ‘to twist the yarn before piling up to the loom’ || (+ *ham-) Yi. 
3098:3inz ‘needle’, etc. Persian *pec, BMP pyc-, NP pec-/pecidan ‘to twist, distort, bend, 
7219:*KHOTANESE: ? gai’h- ‘to twist, spin’ (in hapax gai’he ‘he twists, spins [transl. BSkt. 
7228:ziyiv-/ziyfvd- ‘to twist’, ? Yi. zoyü( v)-/zayuvd- ‘to walk about, fly’ || (+ *ui- ?) Sh. 
8073:66) for LKh. pa-jisth- (< *pa-jar@ia-), MMP gys-/gyst-, Pash. yaral ‘to twist, spin’ is 
8092:*NEIR: Pash. yaxt-/yar- ‘to twist, spin, turn’, Yghn. yil-/yilta ‘to roll; to flow 
8807:yaral ‘to twist, spin’ (EVP: 27) may not belong here: s.v. *gart. 
15395:*NWIR: (?) NP camidan ‘to twist, bend’, NP caftah ‘curved, bent, a vaulted roof” 
16271:*kart? ‘to twist, turn’ 
16278:*ham-kart - ‘to twist, braid together’. > Samadi: 102 f., 128 f. 
24615:*tanó ‘to twist (together), become narrow, dense, constrict’ 
24631:*NWIR: NP tanjidan/tanj- ‘to squeeze; to twist, roll together; to draw tight; to be 
24643:*PIE *tenk- (*temk- ?) ‘to twist together, pull oneself together, condense’ = LIV: 
25332:*tap ‘to twist, wind’ 
25337:*CHORESMIAN: (+ *upa-) bd’by- ‘to twist’ || (+ *us-) ? m/(w)stnb- ‘to throw up, 
25342:tovna/tov-, Varz. towna/town- ‘to twist’ 
27520:fold, cease; to twist; to stroll’ 
28138:*ujeH;. ‘to braid, wind’ (Lat. viére ‘to bind, to plait’; Lith. vun ‘to twist’; OCS 
28238:*AVESTAN: YAv. uruuaés- ‘to twist, turn’ || (+ *abi-) ‘to turn to’ || (+ *aua-) ‘to turn 
58184:to twist
```


## [2026-09-14T01:01:21.838Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19095,19140p' CHEUNG.txt; echo \"=== line 3090-3110 ===\"; sed -n '3090,3110p' CHEUNG.txt"
}
```


### [2026-09-14T01:01:21.899Z] TOOL RESULT

```
*SANSKRIT: ра ‘to drink’ (RV+) = EWAia П: 113 

*PIE *peHs(-i)- ‘to drink’ = LIV: 462 f. | Pok.: 839 f. 

*IE COGNATES: Hitt. /päs-/ ‘to take a sip’, Gr. rivo ‘I drink’, Lat. bibere, OCS piti, 
Arm. ompel, Alb. pi- ‘to drink’, etc. 


290 *paič ? 
*REFERENCES: Horn 1893: 230; IFL II: 409b; Steblin-Kamenskij 1999: 272; Asatrian — Livshits: 83 


*pait ? ‘to pinch ?' 

*AVESTAN: OAv. pic- ‘to pinch ?° = Liste: 35 

Pres. ja-: IND. 3р1. OAv. pisiieinti (Y 44.20); Partic.: pres. OAv. pisiiant- (Y 50.2) 

*SANSKRIT: ? pec ‘to arch, to contract” = EWAia II: 166 

© On the interpretation of the Avestan forms see De Vaan 2000: 71 ff. Further cor- 
respondences are unknown. 

*PIE— = LIV: — | Pok.: 


*REFERENCES: Werba 1997: 206 


*paiH ‘to lactate, (breast-)feed' 

*AVESTAN: Y Av. pi- ‘to lactate, (breast-)feed', YAv. paiiah- (n.) ‘milk’ || (+ *fra-) 
‘to flow forth to’ — Liste: 34 

Pres. nu-: IND. 3sg. YAv. frapinaoiti (V 3.31), INJ. med. 3sg. ? YAv. frapinuuata (Yt 19.51); Partic.: 
perf. YAv. pipiius- (V 15.8) 

“MIDDLE PERSIAN: BMP pym /pém/ ‘milk’ 

*KHOTANESE: ? pyau ‘swelling, overflowing’ 

*NWIR: NP pinu ‘cream-cheese; butter-milk? 

*NEIR: Sh. pai, Sangl. poy, Yi. poya, M. poya 'sour milk" (LW ?), Pash. poy (f. 
sg./pl.) *milk (esp. in or from the breast or udder)' 

=== line 3090-3110 ===
*SANSKRIT: ? cira- ‘strip, tatter, rag’ (TA+), cela- (n.) ‘clothes, garment’ (Gaut.+) 
c EWAia I: 545 

© For semantic (and formal) reasons it is unlikely that the above-mentioned Iranian 
forms contain the root Sëai ‘to heap up, gather’. It must be admitted though that an 
IE provenance for *čaiH! ‘to sew’ is doubtful. The root itself is perhaps exclusively 
Ilr. (cf. Skt. cira-, cela-) and may be related to the second part of the (presumably) 
compounded formation Skt. sü-ci- ‘needle’, YAv. sü-kä- (f.), Oss. I. su-zin, D. so- 
3inz ‘needle’, etc. Persian *pec, BMP pyc-, NP pec-/pecidan ‘to twist, distort, bend, 
wreathe, coil, wind in a serpentine form' (borrowed into modern dialects) is 
probably unrelated, it derives from adverb *patica ‘back’ + ¿dan ‘to collect’, 
Nyberg II: 160a f. 


*PIE — > LIV: — | Pok.: 

*REFERENCES: KPF II: 189; Abrahamian 1936: 119; Lambton 1938: 41a, 77a; IIFL II: 279a; Andreev — 
PeSéereva: 327b Ё; MacKenzie 1966: 92, 104; WIM I: 71;WIM II/1: 81; DKS: 1, 16; WIM III: 307; 
МЕУР: 9.
```


## [2026-09-14T01:01:35.468Z] TOOL CALL #74: Bash

```json
{
 "command": "pdftoppm -f 402 -l 402 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"$SCRATCH/pg402\" 2>/dev/null || pdftoppm -f 402 -l 402 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg402; ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-14T01:01:37.152Z] TOOL RESULT

```
total 3968
drwx------ 2 sfmqrb sfmqrb   4096 Sep 13 21:01 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep 13 20:49 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    592 Sep 13 20:53 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  95654 Sep 13 20:53 bqt390_436_foot.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  34040 Sep 13 20:54 bqt390_436_top.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 124665 Sep 13 20:53 bqt390_662_foot.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  93636 Sep 13 20:53 bqt390_662_top.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 537986 Sep 13 20:53 bqt390_n436.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 527696 Sep 13 20:53 bqt390_n662.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   2291 Sep 13 20:56 c404-empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77003 Sep 13 21:01 c404-greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4255 Sep 13 20:56 c404-patil.png
-rw-rw-r-- 1 sfmqrb sfmqrb  34837 Sep 13 20:57 c404-pest.png
-rw-rw-r-- 1 sfmqrb sfmqrb  46825 Sep 13 20:57 c404-symp2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  34820 Sep 13 20:56 c404-symp.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3627 Sep 13 20:54 crop14-394.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4873 Sep 13 20:54 crop18-394.png
-rw-rw-r-- 1 sfmqrb sfmqrb  20203 Sep 13 20:57 edit_about.py
-rw-rw-r-- 1 sfmqrb sfmqrb 120893 Sep 13 20:58 pg390b.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  39607 Sep 13 20:58 pg390b.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55136 Sep 13 20:50 pg390.png
-rw-rw-r-- 1 sfmqrb sfmqrb 113843 Sep 13 20:57 pg391big.png
-rw-rw-r-- 1 sfmqrb sfmqrb  18836 Sep 13 20:57 pg391crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  81140 Sep 13 20:57 pg391.png
-rw-rw-r-- 1 sfmqrb sfmqrb  34659 Sep 13 20:58 pg391root.png
-rw-rw-r-- 1 sfmqrb sfmqrb  21174 Sep 13 20:58 pg391sog.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75438 Sep 13 20:56 pg392.png
-rw-rw-r-- 1 sfmqrb sfmqrb 101976 Sep 13 20:57 pg393.png
-rw-rw-r-- 1 sfmqrb sfmqrb 145431 Sep 13 20:54 pg394hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  96039 Sep 13 20:53 pg394.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72433 Sep 13 20:54 pg397.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77067 Sep 13 20:55 pg398.png
-rw-rw-r-- 1 sfmqrb sfmqrb  85891 Sep 13 21:00 pg399-crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb  45417 Sep 13 21:00 pg399-greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb  64776 Sep 13 20:54 pg399.png
-rw-rw-r-- 1 sfmqrb sfmqrb  43498 Sep 13 21:00 pg399-sog.png
-rw-rw-r-- 1 sfmqrb sfmqrb 167174 Sep 13 20:58 pg400big.png
-rw-rw-r-- 1 sfmqrb sfmqrb  24547 Sep 13 20:58 pg400_fa_heli.png
-rw-rw-r-- 1 sfmqrb sfmqrb  23086 Sep 13 20:58 pg400_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  14689 Sep 13 20:58 pg400_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb  32600 Sep 13 20:58 pg400_kasak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  35662 Sep 13 20:58 pg400_kasak3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  22852 Sep 13 20:58 pg400_kasak.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79028 Sep 13 20:57 pg400.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70671 Sep 13 21:01 pg402.png
-rw-rw-r-- 1 sfmqrb sfmqrb 136264 Sep 13 20:56 pg404hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71542 Sep 13 20:56 pg404.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63962 Sep 13 20:58 pg405.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63610 Sep 13 20:57 pg406.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79866 Sep 13 20:59 pg407.png
-rw-rw-r-- 1 sfmqrb sfmqrb  21327 Sep 13 20:55 pg408-ampus.png
-rw-rw-r-- 1 sfmqrb sfmqrb  33681 Sep 13 20:55 pg408-germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78365 Sep 13 20:54 pg408.png
-rw-rw-r-- 1 sfmqrb sfmqrb     40 Sep 13 20:53 queue.txt
```


## [2026-09-14T01:01:41.485Z] TOOL CALL #75: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg402.png"
}
```


### [2026-09-14T01:01:41.840Z] TOOL RESULT

```

```


## [2026-09-14T01:01:41.838Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T01:02:00.205Z] TOOL CALL #76: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py"
}
```


### [2026-09-14T01:02:00.257Z] TOOL RESULT

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


## [2026-09-14T01:02:10.434Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 p70 pik ===\"; grep -n \"pik(h)o\\|piks, pika\\|nava-pix\\|pixa\" incoming/WLD/WLD_Bd2_pages.txt | head -10; echo \"=== WLD Bd2 peuk/pug ===\"; grep -n \"peuk̂\\|peuk-\\|peug-\\|pungo\\|pugnus\" incoming/WLD/WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-14T01:02:10.513Z] TOOL RESULT

```
=== WLD Bd2 p70 pik ===
4686:  Av. pioca- „Knoten“ in nava-pixdm „neunknotigen“ yerbindet Liden IP.
=== WLD Bd2 peuk/pug ===
945:                                                peak- uud peug-                                          5
970:peuk- und peug- (wohl            „stechen“. die Form auf Media lat. (teil-
973:     ^peuk-: gi\ ^jiEVHog n. ,,Spitze, StacheP* in ex^-TievxEgj TZEQi-nevxEg
996:      2.   "^peug-:      „mit der Faust’‘, adv. erstarrter n. sg. m. f., vgl.
1004:,,Faustkampf, Kampf*‘, pugiUus „Handvolk‘          pungo^ -ere, piipngl, pUnctnm
40689:  Got. stiks „Stich,           Punkt“ (wie            lat.       punctum pungo), abd. stih
```


## [2026-09-14T01:02:11.755Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC peug/pug ===\"; grep -n \"^peug\\|^pug\\|^peuk\\|^pik\" IEC.txt | head -20; echo \"=== SYN pungere ===\"; grep -n \"pungere\" SYN.txt | head -5"
}
```


### [2026-09-14T01:02:11.856Z] TOOL RESULT

```
=== IEC peug/pug ===
12818:peug- (or peug-) “bot, bellyworm' W cf. eu-od, -on, pl. *bellyworms'; G Fiek, m. id.
12819:peuk- (peuKt-, püK-) ‘fir-tree’. WP II, 15 Gk. peüke, f. id.; Alb. pishé, f. id. Ir. cf. ocht-ach, f. id; OS fiuhtia, f. id.: MHG viehte, s & wf., id. (G Fichte); Li. pušis, gs: -i&s, f. id.
12867:pik-, pik- radical form of following entries, cf. pikolos, pikos, etc. Alb. pik, v. ‘drip; stab; embitter; pickle’; Li. pykà ‘anger’; pykstü, pýkti, v. ‘be angry; LW in Ir. pioc, pioch, m. ‘droplet; jot; pore & in Alb. pikë ‘point, dot, source of Fr. pique, fr. a Lat. type *picca. A type pīkāið arises in Alb. pikoj, v. ‘drip’; OCz. pikati, inf. ‘urinate’ and in OCS pikanina, pikotyna, f. “urine?
12868:pikolos, à, is (pikl-) ‘tip, point. Cf. pik-, pikos, a and WP II, 17
12878:pikis, ios, io “pitch, raging fire’. Extn. piknis, os. WP II, 75 Gk. píssa, pitta, f. ‘pitch; hell; Lat. pix, gs: picis, f. “pitch” beside picula ‘scrap of pitch’; OHG.OS cf. fehon, v. ‘consume, destroy’; OCS cf. píklü, nol m. *pitch" beside piklinú, adj. infernal; Blg. cf. pákál, m. ‘pitch, hell; Srb. cf. paklina “tar, pitch’, pakao, m. "bell": Li. pikis, gs: io, m. ‘pitch’; Latv. pikis “pitch, hell. (DW in Alb. pis, m. ‘pitch’). For the extn. *piknos, cf. Lat. pinus, gs: -üs & <i, f. ‘pine’; Arm. cf. eye-vin, gs. -vno, o-st. id. (for eye- see elntà); OS cf. fini-star, n. ost & fini-stri, f. i-st. (*darkness'. Cf. ster-); MHG vin-ster, OS fini-stri, adj. “dark?
12879:pikos "a bird’. WP II, 681 Skt. pikah, m. ‘cuckoo’; Alb. cf. (dim. type) pikth, m., piké, f. (^woodpecker. Sense in- fluenced by Lat. picus, pica, see poiKos, à). (Isophone: Latv. piks, m., pika, f. “lump, clot ; Alb. cf. pikset, 3s. *coagulates'")
12880:pikos, à “point, prick, stab, sting'. Cf. piko- los EMAIb Alb. pikë, f. “point, dot: të pik&-t, n. ‘stab’; Lat. pica, f. ‘oestrus in pregnant women’; MIr. íoc, m. ‘suffering’; íocaim, v. ‘suffer; Slovene pik ‘sting — of insects; R pik, m. ( ‘peak’, geog.); Ukr. pyka, f. ‘snout. (Isophonic are It. picca ‘pike, spear’; picco, adj. and m. ‘stung; pungency; mountain peak’ from a variant of type *pik-)
12881:pikros, us ‘sharp, bitter, acrid’. Cf. pik-, pik-, etc. Variant piklo- Gk. pikrós, id.; Alb. cf. pikllim, m. "butter, ness, sadness' beside i píkun, T i píkur, adj. “bitter, embittered, mortified, aghast; Li. pikrüs, adj. ‘nasty’. (The origin of Norm. Fr. paicre, adj. “bitter, harsh? is unknown)
12882:piks- ‘strike’. Variant of type pik-, see pikos, etc. OCS pi3o, píxati, v. id.; (long-gde in) Cz. píchat, inf. ‘stab, sting; Li. pykSiu & pyšku, inf: pyk3eti, v. ‘knock; bang, fire aP. A simi- lar consonantism arises in Av. pax$-, pp: pax- sta (sic) 'stab, prick'. (Isophonic short-gde
12885:piktos “sad, sorry, angry; sadness, anger”. Cf. pikros, pik-, etc. Alb. i pikët “bitter, harsh, acrid’; MIr. cf. ío- caim, v. “suffer”; íoc, m. ‘suffering’, (mod. *re- quital, revenge’); Ir. pp. iochtha ‘avenged’; Li. piktas, adj. *evil, nasty' beside pyktis, gs: pykčio, m. ‘anger’; Latv. pikts, adj. “evil, vio- lent, angry”
12886:pikið “mark, paint, adorn’. Cf. peik-, poiK-, piKtós. WP II, 9 Av. pis- ‘adorn’; Ober, ni-piš- “write down’; Per. na-vištan, inf. id.; OCS (and com. Sl.) pí39, pisati, v. ‘write, engrave’; isophonic: Li. pyštù, pišti, v. ‘get rusty’; pisüs, adj. ‘rusty
12887:piktos (pikitos) “marked, lined, painted, de- corated”. Cf. piKio, peiK-, poiK-. Skt. pistáh, pisitáh, id.; OPer. pista-, id. beside -pisti- ‘impression’; Lat. pictus, id.; MIr. cf. cicht (w. assimilated conss. *decorator) (but cf. Ir. ar-ecraim, v. ‘adorn’, fr. *pr-piKro ?); OCS cf. pístrü, OCz. pstry, adj. 'variegated"; (e-gde in) Li. piestas, adj. “drawn, written’
12893:piktos — pipël-
13725:pug- (pung-) “jab, jolt, stab'. Cf. pung- asa separate entry Gk. cf. püx, adv. “with the fist; pugón, gs: -onos, f. ‘elbow’; pugmé, f. ‘fist’; Lat. cf. pügio, -onis, f. ‘dagger’; pugna, f. ‘fight’; pugnus, gs: -1, m. ‘fist, punch’ beside pungo, Gre, v. ‘prick’: Li. pungu, pugti, v. ‘erupt in pimples’; LG fuck, m. “tap, jab, jolt’; fucken, v. id.; Latv. cf. puksts, s. “single heartbeat'. (Isophones: SWG Fucke, f. ‘pullet’: Du. vokken, v. ‘breed’; Icel. fok, n. “drift; spray”; fokka, f.: Sw. fock, -a, mf. *foresail")
13770:puggs, OFris. OE, LG pung, m., Mod. Gk. pouggi ‘purse’; (? LW in) OCS pọgy, gs: pọ- güve, f. (bunch, cluster’, but perh. of inde- pendent origin); Li. cf. pungulys, gs. -io, m. ‘bale, bundle’; Latv. cf. pogaļa, f. “seed-cap- sule’; R püga, f. ('cudgel': Pol. pega, id., also in R ‘rump of bird, pincushion of lacework- ers"); Latv. poga, f. “button, stud”, cf. R püg- ovica, id.
=== SYN pungere ===
6168:(cf. Lat. pugnus ‘fist’ : pungere ‘sting’, orig.
21913:It., Sp. punta, Fr. pointe (> ME, NE point) fr. MLat. puncta, new formation beside Lat. piinctum ‘puncture, point’ as small spot (> It., Sp. punto, Fr. point > ME, NE point in this sense), fr. pungere ‘prick, puncture’. Ernout-M. 824. REW 6847.
```


## [2026-09-14T01:02:23.566Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4670,4700p' incoming/WLD/WLD_Bd2_pages.txt; echo \"==== page marker search ====\"; awk 'NR>=4600 && NR<=4700' incoming/WLD/WLD_Bd2_pages.txt | grep -n \"pdf page\" ; grep -n \"pdf page\" incoming/WLD/WLD_Bd2_pages.txt | head -3"
}
```


### [2026-09-14T01:02:24.716Z] TOOL RESULT

```
      Nicht zu ahd. clialawa ^Schauder*', lat. gelu nach Fick BB          8,    330, Wb.    P 405.
70                                 piq{h)o-   — pip-
„sulineii“(aus „geruhrt machen, versohnen''?), osk. piikiui              nach
Bucheler j,lustrifico“, u. pihatu „piato“ (Johannson PBrB. 15, 228); ags. fMe
„treu, freundlich“, mnd. velich^ veilich ^sicher, sorglos'^? (Fick III^ 224 sehr zw.)
     Recht fraglich; plus wird auch       als ^pu-lios   mit purus usw. verbunden
(Lit, bei Vf.   LEWb.^ s, v.), allerdings kaum wahrscheinlicher. — tJber gr,
fjmog (Rozwadowski Rocznik slaw. 2, 102, ^fiedermann lA. 29,35                Wood
Cl. PhU, 5, 303 ff.) 8 epi- „Gefahrte“.
                       .




piq(h)o- „kluinpiges, Kiioteii“.
  Av. pioca- „Knoten“ in nava-pixdm „neunknotigen“ yerbindet Liden IP.
19, 325 f. ansprechend mit lett. piTzs, pika „Erd- und Lehmklumpen^, sne-
gapika „Schneeballen“; wenn -q(h)o- formantiscb ist (oder etwa zum For-
mans nmempfnnden wurde), konnte allenfalls auch lett. -pate „KloB, Klum-
pen“ und (??) lit. pitas „rund“ verwandt sein; lat. pila „Balh' aber zu
pilus „Haar‘'.


pid- „gebaren“??
     Got. fitan „gebaren“, air. idu^ gen. idan, n. pi. idain j,Geburtswehen,
Schmerz^'.     Feist PBrB. 15, 547, Uhlenbeck PBrB. 27, 119, Fick IP 46.
Die Ablantreihe des got. Terbums ist nicht festzustellen, ebenso nicht,
ob gerade „Geburtsschmerz“ die alteste Bed. des air. Wortes ist.                  —
fitan nicht nach Lewy IF. 32, 163 zu apr. pidai „tragt, bringt" (s. auch
u. ped- „fassen“).
==== page marker search ====
```


## [2026-09-14T01:02:33.662Z] TOOL CALL #80: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/سپوختن\" \\\n \"https://en.wiktionary.org/wiki/پیختن\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pewǵ-\" \\\n \"https://www.etymonline.com/word/puncture\" \\\n \"https://www.etymonline.com/word/pivot\" \\\n \"https://abadis.ir/fatofa/پیختن/\" \\\n \"https://abadis.ir/fatofa/پنچر/\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 402, roots Peuk/Pug and Piko: verifying sepuxtan, pixtan, pancar, pungere/pivot\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T01:02:38.929Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4d4184329375d79d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eb21d3898e0ad02c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c3c7fc7e53d56a33.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eeba5dc2bfe0106c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/87120d51f9e4e843.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e31b584e0007e71b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/422783f97d670d2c.txt
```


## [2026-09-14T01:02:57.426Z] TOOL CALL #81: WebSearch

```json
{
 "query": "Sogdian \"pyx\" knot Gharib Sogdian dictionary pixa Avestan knot"
}
```


### [2026-09-14T01:03:04.117Z] TOOL RESULT

```
Web search results for query: "Sogdian "pyx" knot Gharib Sogdian dictionary pixa Avestan knot"

Links: [{"title":"Sogdian Dictionary, Sogdian Persian English by Gharib, Badrozaman | Leather bound | 1995 | Farhangan Publications | 9789645558060 | Biblio","url":"https://www.biblio.com/book/sogdian-dictionary-sogdian-persian-english-gharib/d/1196715091"},{"title":"Sogdian Dictionary: Sogdian - Persian - English by B. Gharib: New Hardcover (1995) 1st Edition. | Anis Press","url":"https://www.abebooks.com/first-edition/Sogdian-Dictionary-Persian-English-B-Gharib/30040190515/bd"},{"title":"Full text of \"Ù Ø±Ù‡Ù†Ú¯ Ø³ØºØ¯ÛŒ sogdian dictionary\"","url":"https://archive.org/stream/SogdianDictionary/GharibSogdianDictionnary_djvu.txt"},{"title":"A Compendious Sogdian Dictionary I Raham Asha","url":"https://parsianjoman.org/wp-content/uploads/2024/03/Pages-from-Sogdian-Dictionary.pdf"},{"title":"Sogdian Dictionary: Sogdian - Persian - English - B. Gharib: 9789645558060 - AbeBooks","url":"https://www.abebooks.com/9789645558060/Sogdian-Dictionary-Persian-English-Gharib-9645558069/plp"},{"title":"B. Gharib, \"Sogdian dictionary\" (Book Review) - ProQuest","url":"https://www.proquest.com/scholarly-journals/b-gharib-sogdian-dictionary-book-review/docview/1304102820/se-2"},{"title":"Sogdian dictionary : Sogdian, Persian, English / B. Gharib ; [editorial supervisor, A. Mansouri ; editor, S. Fotouhi.] | Book | Badr al-Zamān Qarīb 1929 or 1930- (Mansouri, Ahmad | Mansouri, Ahmad;Fotouhi, Sharzad | The National Library of Israel","url":"https://www.nli.org.il/en/books/NNL_ALEPH990018188540205171/NLI"},{"title":"SOGDIAN LANGUAGE i. Description - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/sogdian-language-01/"},{"title":"Sogdian alphabet","url":"https://en.wikipedia.org/wiki/Sogdian_alphabet"}]

I've completed the web search for your query about Sogdian "pyx," knot, Gharib Sogdian dictionary, pixa, and Avestan knot. The search results provide some relevant information:

The search found references to Badrozaman Gharib's Sogdian Dictionary: Sogdian-Persian-English published in Tehran in 1995. However, the search results don't contain specific information about the terms "pyx," "pixa," or their relationship to knots in Sogdian or Avestan languages.

The results do confirm that Sogdiana was first mentioned in the Avesta, establishing a connection between these linguistic and cultural areas, but they don't provide the specific etymological or linguistic details you're seeking about these particular terms.

To find more detailed information about these specific terms and their meanings in the Gharib dictionary, you may need to consult the dictionary directly or search for specialized academic articles on Sogdian linguistics or Avestan-Sogdian linguistic connections.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T01:04:03.436Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW pungo ===\"; grep -n \"pungo\" LEW_1910.txt | head -4; echo \"=== LAT pungo ===\"; grep -n \"pungo,\" LAT.txt | head -4; echo \"=== KLN puncture entry ===\"; grep -n \"^puncture\\|puncture,  n\\.\" KLN_1966.txt | head -4"
}
```


### [2026-09-14T01:04:03.527Z] TOOL RESULT

```
=== LEW pungo ===
=== LAT pungo ===
50844:pug- que dans pungo, pupugi, avec suffixe -no- comme dana somnus .
=== KLN puncture entry ===
1556:acupressure,  n.,  the  checking  of  bleeding  by  the pressure  of  a  needle  on  the  bleeding  vessel (surg.)  —  Compounded  of  L.  acus,  ‘needle’  and pressura  ‘pressure’.  See  acus  and  pressure, acupuncture,  n.,  puncture  of  the  ailing  part  with a  needle  to  relieve  pain.  —  Compounded  of  L. acus,  ‘needle’,  and  punctura,  ‘a  pricking’.  See acus  and  puncture.
31013:punctum,  n.,  a  point  ( anat .,  zool.,  bot.)  L. punctum,  prop.  neut.  pp.  of  pungere,  ‘to  pierce’, used  as  a  noun.  See  pungent  and  cp.  point,  n. puncture,  n.,  the  act  of  pricking,  perforation.  — L.  piinctura,  ‘a  pricking’,  fr.  punctus,  pp.  of  pun¬ gere.  See  pungent  and  -ure  and  cp.  acupuncture. Derivatives:  puncture,  tr.  and  intr.  v.,  punctur- ation,  n.,  punctur-ed,  adj.,  punctur-er,  n. pundit,  n.,  a  learned  man.  —  Hind,  pandit,  fr.  Ol. panditab,  ‘learned,  wise;  learned  man’,  which  is of  uncertain  origin.  Cp.  pandit,  Pandy. Derivatives:  pundit-ic,  adj., pundit-ic-al-ly,  adv., pundit-ry,  n.
```


## [2026-09-14T01:04:05.867Z] TOOL CALL #83: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg402.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/402.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head"
}
```


### [2026-09-14T01:04:05.956Z] TOOL RESULT

```
total 18908
drwxrwxr-x  2 sfmqrb sfmqrb  12288 Sep 13 21:04 .
drwxrwxr-x 13 sfmqrb sfmqrb   4096 Sep  7 13:51 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-14T01:04:10.535Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '50835,50850p' LAT.txt"
}
```


### [2026-09-14T01:04:10.619Z] TOOL RESULT

```
puga, -ae f. : fesse. Emprunt de la langue ^rotique au gr.uuyn
(Novius, Hor., cf.Non.39,30). Cf. pugesiaca ( pigi - codd.) sacra, Petr. ,
Sat.140; depugis (Hor.) = aTwyoS.
pugil; pugillus: v. pugnus .
pQgio: y.pungS.
pugna; pugnS: v. le suivant.
pugnus, -I m.: poing; pugnus a punctione, i.e. percussu dicitur,
P.F.243, 1 , "poignee" (par ex. Cat., Agr. 82). - Ancien, usuel. Panroman
M.L.6814 pUgnus . Iri. cuan-ene, punann. Peut-Stre meme racine *peug~/
pug- que dans pungo, pupugi, avec suffixe -no- comme dana somnus .
Le poing est "ce qui sert A frapper"; la racine qui dana pungo a
le sena sp(?cial de "piquer" exprimerait d'une maniore generale 1'idAe
de "choc". Cf. pugil,-lis n.(non .pugilis dans Varr.; u dans Prudence;
m£me formation que uigil ): athlbte qui pratique le pugilat, boxeur;
d'ou pugilor, -aris ( -lo ); pug i latus,-iis; pugilatio (Cic.), -tor (Am.).
De pugnus "poing" d^rive le d 4 nominatif pugn 5 ,-as, proprement
```


## [2026-09-14T01:11:04.477Z] TOOL CALL #85: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/write-402.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\ndata = {\n \"pdf_page\": 402,\n \"book_page\": 372,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Peuk, Pug\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *pewḱ- / *pewǵ- 'to prick, stab, punch' (Pokorny peuk̑- und peug̑-, IEW 828)\",\n   \"note\": \"Root box, language label and gloss are all right: Pokorny IEW p.828 heads the entry 'peuk̑- und peug̑-' with the meaning 'stechen, stoßen' (English IED dump: 'to stick; to punch'), and Watkins/AHD reproduces it verbatim as 'peuk-. Also peug-. To prick. Zero-grade form *pug-. … [Pok. peuk- 828]'. Walde-Pokorny II 15 has the same entry. The one cross-cutting problem on this chart is the Iranian branch: NEITHER Pokorny, NOR Walde-Pokorny, NOR Watkins, NOR Wiktionary's *pewǵ- page lists ANY Indo-Iranian reflex of this root — the material is exclusively Greek, Latin, Celtic, Germanic and Baltic. Nourai's whole left-hand branch (Avestan spôz → Pahlavi spôxtan → Persian سپوختن) therefore hangs on Horn's own explicitly hedged guess, which the chart itself records in its NOTE and which Cheung 2007 rejects. The Latin/English branch (pungere → puncture, point, punctuate) is standard; 'pivot' is the exception (see node #7).\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *pewḱ-/*pewǵ- «سوراخ کردن، خلیدن، مشت زدن» در فرهنگ پوکورنی (ص ۸۲۸) با همین صورت دوگانه و همین معنا آمده است و واتکینز (پیوست AHD) نیز عیناً «peuk-، همچنین peug-: to prick» می‌آورد؛ پس خودِ ریشه، برچسب زبانی و معنای آن در نمودار نورایی درست است. اما نکتهٔ مهم این است که نه پوکورنی، نه والده‑پوکورنی و نه واتکینز هیچ بازماندهٔ هندوایرانی برای این ریشه ذکر نکرده‌اند؛ مادهٔ این ریشه تنها یونانی، لاتینی، سلتی، ژرمنی و بالتیک است. بنابراین شاخهٔ ایرانیِ این نمودار (اوستایی spôz ← پهلوی spôxtan ← فارسی سپوختن) تنها بر حدسِ محتاطانهٔ هرن استوار است — همان تردیدی که خودِ نمودار در یادداشتش آورده — و چونگ (۲۰۰۷) آن را نمی‌پذیرد.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pewǵ-\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:828\", \"status\": \"supports\", \"note\": \"POK_full.txt l.67435-67443 (= POK_03.txt leaf for printed p.828): 'Root / lemma: peuk̑- and peug̑- | Meaning: to stick; to punch | Material: 1. peuk̑- gr. *πεῦκος n. \\\"cusp, peak, sting, prick\\\" … 2. peug̑-: gr. πύξ … Latin pugil …, pugnus \\\"fist\\\", pugno, -āre \\\"fight\\\", pungo, -ere, pupugī punctum \\\"prick\\\", pugio \\\"dagger\\\". References: WP. II 15 … Page(s): 828'. Exactly Nourai's root, label and gloss — but with no Iranian material at all.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II p.15 (incoming/WLD/WLD_Bd2_pages.txt l.945-1004)\", \"stance\": \"supports\", \"note\": \"running head 'peuk- und peug-' p.15; '*peuk-: gr. πεῦκος n. \\\"Spitze, Stachel\\\" …', '2. *peug-: … pugnus … pungo, -ere, pupugi, punctum'. This is the WP II 15 that Pokorny cites; again no Iranian reflex.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. peuk- (AHD_watkins1985.txt l.846)\", \"stance\": \"supports\", \"note\": \"'peuk-. Also peug-. To prick. Zero-grade form *pug-. 1. Suffixed form *pug-no- in Latin pugil …, pugnus, fist … 2. Nasalized zero-grade form *pu-n-g- in Latin pungere, to prick: BUNG, POIGNANT, POINT, POINTILLISM, PONTIL, (POUNCE1), (POUNCE2), PUNCHEON1, PUNCTUATE, PUNCTURE, PUNGENT; … 3. Greek pugmē, fist … [Pok. peuk- 828.]' — Nourai's 'AHD' citation is the modern standard for this root.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. pug- (pung-) (IEC.txt l.13725)\", \"stance\": \"supports\", \"note\": \"'pug- (pung-) \\\"jab, jolt, stab\\\". … Gk. pūx … pugmē, f. \\\"fist\\\"; Lat. … pugnus … beside pungo, -ere, v. \\\"prick\\\"' — same root, no Iranian.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/pewǵ-\", \"stance\": \"partial\", \"note\": \"gives *pewǵ- 'to punch, fist-fight; to prick, poke, stab' with Latin pungō, pugil, pugnus, Gk. pugmḗ; descendants confined to Italic, Hellenic, Celtic, Germanic, Balto-Slavic — NO Indo-Iranian; and notes it is 'probably not related' to *pewḱ- 'pine', i.e. modern reconstruction splits what Pokorny (and Nourai) join.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"spôz\", \"verdict\": \"disputed\",\n     \"derivation\": \"No Avestan verb spōz-/spaz-/spauz- exists. Bartholomae's Altiranisches Wörterbuch has no such root (grep of BRT.txt for spaz-/spuz-/spōz finds nothing; the neighbouring columns 1613-1620 hold spas- 'to look' and spənta-). Both of Nourai's own citations are about MIDDLE Persian, not Avestan: SNS p.175 is the Šāyast nē-šāyast glossary entry spōzēd (Pahlavi 3sg., 'postpone, neglect'), and Hübschmann, Persische Studien p.73 is his note on Horn no.706, which cites only Pāzand spuxtan / spōxt and the Armenian loan spuže-l. The real reconstruction is Cheung 2007: 354 *spauč? 'to thrust; verstoßen', attested only in MP spōz-/spōxtan (plus Khot. haspās- and the Armenian loan), with the explicit verdict 'Further (other) Ir. cognates are unknown. An IE origin cannot be ascertained.' So this node should read [Middle Persian] spōz-, and the arrow from PIE *peuk̂-/peug̑- is not supported: the -z- of spōz- would have to come from a palatal *-č-/*-ǰ-, not from the *-g̑-/*-k̂- of peug̑-, and no Iranian language shows a *pug-/*pauk- 'prick' verb.\",\n     \"derivation_fa\": \"هیچ فعل اوستایی به صورت spōz-/spaz- وجود ندارد؛ در «فرهنگ ایرانی باستان» بارتولومه چنین ریشه‌ای نیامده است (ستون‌های ۱۶۱۳ تا ۱۶۲۰ تنها spas- «نگریستن» و spənta- را دارند). هر دو ارجاع خودِ نورایی هم دربارهٔ فارسی میانه است نه اوستایی: SNS ص ۱۷۵ مدخل پهلویِ spōzēd «به تأخیر انداختن» است و هوبشمان ص ۷۳ حاشیه‌ای بر شمارهٔ ۷۰۶ هرن است که تنها صورت‌های پازند spuxtan/spōxt و وام‌واژهٔ ارمنی spužel را می‌آورد. بازسازی امروزی از آنِ چونگ (۲۰۰۷، ص ۳۵۴) است: ایرانی *spauč؟ «راندن، فروبردن»، که تنها در فارسی میانه (و ختنی haspās-) گواهی دارد و چونگ صریحاً می‌گوید «خویشاوند ایرانی دیگری شناخته نیست و خاستگاه هندواروپایی آن را نمی‌توان اثبات کرد». پس این گره باید «فارسی میانه» برچسب می‌خورد و پیوند آن با ریشهٔ *peug̑- را پژوهش امروزی رد می‌کند؛ افزون بر آن ز در spōz- باید از *č/*ǰ ایرانی بازمانده باشد نه از *g̑ هندواروپایی.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/سپوختن\"],\n     \"ref_check\": [\n      {\"ref\": \"SNS:175\", \"status\": \"partial\", \"note\": \"Tavoosi, Šāyast nē-šāyast glossary: the back index (SNS.txt l.31438) reads 'spōzēd 175/21', and the page itself (SNS_pages.txt \\\\f-block 87+16=103, which carries spās 175/3-4, sparm 175/15, spənta- 175/18, spannāg mēnōg 175/19) shows ': spōzēd:' glossed 'postpone, neglect' with the present stem '/spōz'. The page number is right, but the form is Pahlavi, not Avestan — the glossary flags its Avestan comparanda with '(AiWb. nnnn)', and spōzēd carries none.\"},\n      {\"ref\": \"HUB:73\", \"status\": \"contradicts\", \"note\": \"Hübschmann, Persische Studien p.73 (HUB.txt leaf 84), note to Horn 706: 'Dazu pāz. spuxtan \\\"to set aside\\\", spuxtār \\\"remover\\\", spōxt \\\"putting aside\\\", Shk. 267-268, arm. spuzel \\\"aufschieben\\\", spuzumn \\\"Aufschub\\\" (aus spōž- = pāz. spōž-). Phl. \\\"spōxtxtan\\\" ist eine Unform.' Pāzand and Armenian only; no Avestan, and no PIE comparison.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, s-section (cols. ~1600-1630)\", \"stance\": \"silent\", \"note\": \"grep of BRT.txt for 'spaz-', 'spuz', 'spōz', 'spoz' returns nothing; Bartholomae knows no Avestan root of this shape.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p.354 s.v. *spauč ?\", \"stance\": \"contradicts\", \"note\": \"'*spauč ? \\\"to thrust; verstoßen\\\". MIDDLE PERSIAN: MMP ʾspwx- (pret. stem), BMP spwc- /spōz-/ … KHOTANESE: (+*fra-) OKh. haspās- … NWIR: NP sipōxtan/sipōz- … MISC: Arm. (LW) spuž-el … ◊ Further (O)Ir. cognates are unknown. An IE origin cannot be ascertained.' No Avestan entry at all, and the PIE link is explicitly refused.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p.76 s.v. spōxtan\", \"stance\": \"partial\", \"note\": \"'spōxtan, spōz- [spwhtn', spwc- | M ʾspwxt, N sip~] thrust; overstep, disobey; delay, reject.' MacKenzie cites Avestan cognates elsewhere on the same page ('spas [sp = Av. θβāsa-]', 'spenāg [= Av. spənta-]') but gives none here.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/سپوختن\", \"stance\": \"partial\", \"note\": \"'From Middle Persian spwhtn' (spōxtan, spōz-) … Compare Old Armenian սպուժեմ (spužem), an Iranian borrowing.' Cites Cheung 2007 and MacKenzie 1971; the chain stops at Middle Persian, with no Avestan and no PIE.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"spož, spôxtan\", \"verdict\": \"plausible\",\n     \"derivation\": \"The Middle Persian word itself is beyond doubt: Book Pahlavi spwhtn' /spōxtan/, present spwc- /spōz-/ 'thrust; overstep, disobey; delay, reject' (MacKenzie, CPD p.76), Manichaean MP ʾspwxt; Nyberg II s.v. spōxtan 'to throw, to drive … bē ~ to defy, to disregard … to drive out', with the Armenian loan spuž-em 'to postpone' and Pāzand present spōž-. Horn no.706 (p.156), the reference cited, gives 'phlv. spōj (pāz. spōz) \\\"Aufschub\\\", spōxtan, spōjet \\\"entfernen, heraustreiben\\\" (Mēnōg ī Xrad, Ardā Wīrāz)'. What is only 'plausible' is the ARROW: the parent node is a phantom Avestan form (see #1), so this box is in effect the Middle Persian word drawn twice, and its ultimate ancestry is Proto-Iranian *spauč? (Cheung 354), not PIE *peug̑-. The chart's own NOTE is accurate and worth keeping: Horn writes 'Wenn \\\"einheften\\\" die Grundbedeutung ist, so ließe sich lat. pungō (√pug-) vergleichen; doch ist dies durchaus unsicher' — modern scholarship (Cheung) has come down on the 'unsicher' side.\",\n     \"derivation_fa\": \"خودِ واژهٔ فارسی میانه جای تردید ندارد: پهلوی کتابی spwhtn'‏ /spōxtan/ با ستاک حال spwc- /spōz-/ به معنی «فروبردن، راندن، سرپیچی کردن، به تأخیر انداختن» (مکنزی، فرهنگ کوچک پهلوی، ص ۷۶)، فارسی میانهٔ مانوی ʾspwxt، و نیبرگ (جلد دوم، واژه‌نامه) همین صورت‌ها را با وام‌واژهٔ ارمنی spužem «به تأخیر انداختن» و ستاک پازند spōž- می‌آورد. هرن نیز در شمارهٔ ۷۰۶ (ص ۱۵۶) دقیقاً همین را دارد. آنچه تنها «با احتیاط پذیرفتنی» است خودِ پیکان است: گرهِ پدر (اوستایی spôz) وجود خارجی ندارد، پس این جعبه در عمل تکرار همان واژهٔ فارسی میانه است و نیای واقعی‌اش ایرانی *spauč (چونگ ۳۵۴) است نه *peug̑- هندواروپایی. یادداشت خودِ نمودار درست است: هرن می‌نویسد اگر معنای اصلی «فروکردن» باشد شاید بتوان با pungō لاتینی سنجید، «ولی این به‌کلی نامطمئن است» — و پژوهش امروزی همان سوی «نامطمئن» را گرفته است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/سپوختن\"],\n     \"ref_check\": [\n      {\"ref\": \"HRN:156\", \"status\": \"supports\", \"note\": \"Horn, Grundriss der neupersischen Etymologie p.156 (HRN.txt leaf 178), no.706: 'sipōxten, supōxten \\\"einheften (Saʿdī, Bōstān); heraustreiben (Šāhn. III 1797)\\\". phlv. spōj (pāz. spōz) \\\"Aufschub\\\" (Salemann, Mél. asiat. IX 247), spōxtan, spōjet \\\"entfernen, heraustreiben\\\" (Mēn., AV.), spōxtītan; arm. LW. spužem \\\"verschieben\\\". Wenn \\\"einheften\\\" die Grundbedeutung ist, so ließe sich lat. pungō (√pug-) vergleichen; doch ist dies durchaus unsicher.' Supports the Pahlavi forms AND the chart's NOTE about Horn's uncertainty.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.76 (PHD.txt l.568)\", \"stance\": \"supports\", \"note\": \"'spōxtan, spōz- [spwhtn', spwc- | M ʾspwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. spōz [spwc | N sipōz] disobedience; delay. ~gar [… | N ~] disobedient; dilatory.' — one lemma covering both of Nourai's Pahlavi boxes.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary), s.v. spōxtan (NYB.txt l.3498)\", \"stance\": \"supports\", \"note\": \"'spōxtan [spwhtn'] spōž- [spwc-] to throw, to drive 29:74-75; bē ~ to defy, to disregard 3:7 (cf spōž-kar); to drive out 66:11. — Prth; Arm. lw. spuž-em \\\"to postpone, to delay, to procrastinate\\\"; MPrs (lw.) ʾspwxt; Pāz. pres. spōž-; NP sipōxtan/sipōz-.'\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p.354 s.v. *spauč ?\", \"stance\": \"supports\", \"note\": \"for the MP forms: 'BMP spwc- /spōz-/ \\\"to reject, thrust, throw out; to overstep (the boundaries); to disobey, evade (a command)\\\" … Partic.: perf. pass. BMP spwhtk /spōxtag/ … Inf.: BMP spwhtn /spōxtan/'.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p.73 (note to Horn 706)\", \"stance\": \"supports\", \"note\": \"'pāz. spuxtan \\\"to set aside\\\", spuxtār \\\"remover\\\", spōxt \\\"putting aside\\\", Shk. 267-268 … Phl. \\\"spōxtxtan\\\" ist eine Unform.'\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"sepŭxtan «سپوختن ۱ ( اسپوختن ۱ ، سپوزیدن )»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"NP سپوختن sipōxtan (also اسپوختن with prothetic alef, and the secondary present-stem infinitive سپوزیدن) continues Middle Persian spōxtan/spōz- directly: Book Pahlavi spwhtn' → early NP sipōxtan, the initial sp- cluster being resolved by the anaptyctic i- of New Persian (spōz > sipōz) and receiving a prothetic alef in the اسپوختن variant, exactly as اسپید/سپید beside MP spēd. The past stem spōxt- (< *spauxta-) keeps the -xt- of the MP participle spōxtag; the present stem سپوز sipōz- generates the younger regular infinitive سپوزیدن. Borhān-e Qāṭeʿ p.1091 defines سپوختن as «چیزی را در چیزی بعنف و تعدی و زور فرو بردن ـ و برآوردن» ('to drive one thing into another by force — and to bring out'), i.e. exactly Nourai's 'to pierce, throw in, pull out', and notes the word is از اضداد (a contronym). The Sozanī Samarqandī couplet quoted on the chart is printed on that very page of Borhān.\",\n     \"derivation_fa\": \"«سپوختن» (و گونهٔ «اسپوختن» با الف آغازین، و مصدرِ جوان‌ترِ «سپوزیدن» که از ستاک حال ساخته شده) دنبالهٔ مستقیم فارسی میانهٔ spōxtan / spōz- است: خوشهٔ آغازین sp- در فارسی نو با واکهٔ میانجی شکسته می‌شود (spōz ← سِپوز) و در گونهٔ «اسپوختن» الف پیشین می‌گیرد، درست مانند «اسپید/سپید» در برابر spēd پهلوی. ستاک گذشتهٔ spōxt- (از *spauxta-) همان ـخت صفت مفعولی پهلوی spōxtag را نگاه داشته است. برهان قاطع (ص ۱۰۹۱) می‌نویسد: «چیزی را در چیزی بعنف و تعدی و زور فرو بردن ـ و برآوردن»، و می‌افزاید که این واژه «از اضداد» است — یعنی همان سه معنایی که نورایی آورده. ادعای نورایی در این گره درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/سپوختن\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1091\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ p.1091 (BQT_v2_pages.txt \\\\f-block 553, printed header ۱۰۹۱): «سپوختن ۴ ـ بکسر اول و واو مجهول بر وزن فروختن، بمعنی چیزی را در چیزی بعنف و تعدی و زور فرو بردن ـ و برآوردن … و بمعنی برآورد هم هست … باین اعتبار این لفظ از اضداد است». Mo'in's footnote 4 on the same page: «اسپوخ (ـوز) + تن (پسوند مصدری) = سپوزیدن؛ پهلوی spōxtan (از spōz-؛ پازند spōž) … پازند spuxtan، ارمنی spužel (بتعویق انداختن)، ورک: هوبشمان». The Sozanī verse «ولی را گاه نه بر گاه نشان ـ عدو را چاه کن در چاه بسپوز» is printed there too.\"},\n      {\"ref\": \"FSF:221\", \"status\": \"not_found\", \"note\": \"Noushin, Vāže-nāmak (Donyā 1363 scan, FSF_pages.txt): the entry «سپوختن (با زیر اول)» — «این واژه از اضداد است. هم به معنی چیزی را در چیزی خلانیدن و فرو کردن و هم به معنی برآوردن، بیرون کشیدن، بیرون راندن» — stands on printed page 393 (\\\\f-block 296, whose running head reads ۳۹۳), not p.221; block 124 (= p.221) is in the پ section (پیران etc.). The book supports the gloss, but not at the page Nourai cites — possibly a different printing.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p.76\", \"stance\": \"supports\", \"note\": \"'spōxtan, spōz- … | N sip~' — MacKenzie himself equates the MP verb with NP sipōxtan.\"},\n      {\"src\": \"HRN\", \"where\": \"no.706, p.156\", \"stance\": \"supports\", \"note\": \"'sipōxten, supōxten \\\"einheften (der- Saʿdī, Bōstān S.261 V.304); heraustreiben (Šāhn. III 1797 V.231)\\\"' — the two senses Nourai gives.\"},\n      {\"src\": \"FSF\", \"where\": \"Vāže-nāmak p.393 s.v. سپوختن\", \"stance\": \"supports\", \"note\": \"«هم به معنی چیزی را در چیزی خلانیدن و فرو کردن و هم به معنی برآوردن بیرون کشیدن، بیرون راندن» — the contronymic pair.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/سپوختن\", \"stance\": \"supports\", \"note\": \"senses 1 'to thrust, poke, press, penetrate' (Abu'l-ʿAbbās Marwazī, 8th c.) and 3 'to drive away, fend off, repel' (Ferdowsī), from MP spōxtan, spōz-.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Pahlavi\", \"words\": \"spôzed\", \"verdict\": \"plausible\",\n     \"derivation\": \"spōzēd is real, but it is not a separate lexeme: it is the 3sg present indicative (BMP spwcyt) of the very verb in node #2, spōxtan/spōz-. The Šāyast nē-šāyast glossary (SNS p.175) lists it precisely so, glossing it 'postpone, neglect' with the stem '/spōz'; MacKenzie CPD p.76 collects 'thrust; overstep, disobey; delay, reject' under one headword, and the derived noun spōz 'disobedience; delay' with spōz-gar 'disobedient; dilatory'. The semantic bridge is 'to push away' → 'to push (a matter) back' → 'to postpone' — the same shift that produced Armenian spuž-el 'to postpone, procrastinate', borrowed from Parthian/Middle Persian (Nyberg II s.v.). So Nourai's split of one Middle Persian verb into two Pahlavi boxes hanging from a phantom Avestan parent is an artefact of his layout, not a real bifurcation, though the form and gloss of this box are correct.\",\n     \"derivation_fa\": \"spōzēd واژه‌ای جداگانه نیست، بلکه سوم‌شخص مفرد مضارع (پهلوی کتابی spwcyt) از همان فعل گرهٔ پیشین، یعنی spōxtan / spōz-، است. واژه‌نامهٔ «شایست نه‌شایست» (ص ۱۷۵) آن را با معنی «به تعویق انداختن، فروگذاشتن» و ستاک /spōz آورده، و مکنزی (ص ۷۶) همهٔ معناها — «فروبردن، سرپیچی کردن، به تأخیر انداختن» — را زیر یک مدخل گرد می‌آورد و اسم spōz «سرپیچی، تأخیر» و spōz-gar «سهل‌انگار، تأخیرکننده» را نیز می‌افزاید. پلِ معنایی روشن است: «پس‌راندن» ← «کاری را پس انداختن» ← «به تأخیر افکندن»؛ همین تحول در وام‌واژهٔ ارمنی spužel هم دیده می‌شود. پس دوپاره کردن یک فعلِ واحدِ فارسی میانه به دو جعبهٔ پهلوی، کارِ صفحه‌آراییِ نورایی است نه واقعیتِ زبانی — هرچند صورت و معنای خودِ این جعبه درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/سپوختن\"],\n     \"ref_check\": [\n      {\"ref\": \"SNS:175\", \"status\": \"supports\", \"note\": \"Tavoosi, Šāyast nē-šāyast glossary: back index 'spōzēd 175/21' (SNS.txt l.31438); the page itself (SNS_pages.txt block 103 = printed pp.174-175) reads ': spōzēd:' with the English gloss 'postpone, neglect' and the present stem '/spōz'. Page number and gloss both check out.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p.76\", \"stance\": \"partial\", \"note\": \"'spōxtan, spōz- … thrust; overstep, disobey; delay, reject' — one lemma, so 'hesitate/delay' is a sense of the same verb, not a separate word; also 'spōz [spwc | N sipōz] disobedience; delay. ~gar … disobedient; dilatory.'\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg II glossary s.v. framān and s.v. spōxtan\", \"stance\": \"supports\", \"note\": \"'framān … bē spōxtan to disregard, disobey an order' (l.1520) and 'spōxtan … bē ~ to defy, to disregard … Arm. lw. spuž-em \\\"to postpone, to delay, to procrastinate\\\"' (l.3498) — the delay sense sits inside the same verb.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p.354 s.v. *spauč ?\", \"stance\": \"supports\", \"note\": \"'Pres.: IND. 3sg. BMP spwcyt /spōzēd/, SUBJ. 3sg. BMP spwct /spōzād/' — spōzēd cited explicitly as the 3sg present of spōxtan.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Persian\", \"words\": \"sepŭxtan «سپوختن ۲ ( اسپوختن ۲ )»; sepŭz-gâr «سپوزگار»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Both words are genuine and both continue MP spōz-. (a) سپوختن ۲ 'to hesitate, delay': Borhān-e Qāṭeʿ p.1091 s.v. سپوز ۲ «بمعنی تأخیر کند و کارها را بازپس اندازد», and Wiktionary lists 'to delay, prolong' (Ferdowsī) as a distinct sense of سپوختن beside 'to drive away'. The phonology is that of node #3 (MP spōxtan → NP sipōxtan). (b) سپوزگار sipōz-gār 'one who delays' is the straightforward NP continuation of Pahlavi spōz-gar, which MacKenzie CPD p.76 glosses 'disobedient; dilatory' and explicitly equates with the New Persian word; Borhān p.1091 s.v. سپوزگار: «کسی را گویند که در کارها تأخیر کند و بازپس اندازد» — Nourai's 'one who hesitates' exactly, with the suffix -gār/-gar of agent nouns (cf. آموزگار). One caveat on the illustration: the Ferdowsī line «نه مرگ از تن خویش بتوان سپوخت / نه چشم جهان کس به سوزن بدوخت» is classed by Noushin (Vāže-nāmak p.393) under the sense بیرون راندن 'to drive out, repel', not under 'delay' — though 'one cannot stave death off' reads naturally either way.\",\n     \"derivation_fa\": \"هر دو واژه اصیل‌اند و هر دو دنبالهٔ spōz- فارسی میانه‌اند. (الف) «سپوختن ۲» به معنی درنگ و تأخیر: برهان قاطع (ص ۱۰۹۱) ذیل «سپوز ۲» می‌نویسد «بمعنی تأخیر کند و کارها را بازپس اندازد»، و ویکی‌واژه نیز «به تأخیر انداختن، طول دادن» را معنای جداگانه‌ای از سپوختن (با شاهد فردوسی) می‌آورد؛ تحول آوایی همان است که در گرهٔ پیشین گفته شد. (ب) «سپوزگار» دنبالهٔ مستقیم spōz-gar پهلوی است که مکنزی (ص ۷۶) «سرکش؛ سهل‌انگار، تأخیرکننده» معنا می‌کند و خود آن را با واژهٔ فارسی نو برابر می‌نهد؛ برهان قاطع نیز می‌نویسد «کسی را گویند که در کارها تأخیر کند و بازپس اندازد». پسوند ـگار همان پسوند فاعلیِ «آموزگار» است. تنها نکته آنکه نوشین در «واژه‌نامک» (ص ۳۹۳) بیت فردوسی را ذیل معنی «بیرون راندن» آورده نه «تأخیر»؛ هرچند «مرگ را از تن نتوان پس راند» هر دو خوانش را برمی‌تابد. روی‌هم‌رفته ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/سپوختن\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1091\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ p.1091 (BQT_v2_pages.txt block 553): «سپوز ۲ … و بمعنی تأخیر کند و کارها را بازپس اندازد» and «سپوزگار ـ با کاف فارسی، بالف کشیده و رای بی‌نقطه زده، کسی را گویند که در کارها تأخیر کند و بازپس اندازد» — both of Nourai's words and glosses.\"},\n      {\"ref\": \"FSF:221\", \"status\": \"partial\", \"note\": \"Noushin, Vāže-nāmak: the Ferdowsī verse «نه مرگ از تن خویش بتوان سپوخت / نه چشم جهان کس به سوزن بدوخت» is quoted on printed p.393 (block 296), under the sense «بیرون راندن», not «تأخیر» — and not on p.221, which is in the پ section of this printing.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p.76\", \"stance\": \"supports\", \"note\": \"'spōz [spwc | N sipōz] disobedience; delay. ~gar [… | N ~] disobedient; dilatory.' — the Pahlavi etymon of سپوزگار, equated by MacKenzie with the NP word.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg II glossary s.v. spōxtan\", \"stance\": \"supports\", \"note\": \"'bē ~ to defy, to disregard 3:7 (cf spōž-kar)' — the agent noun attested in the Pahlavi texts; 'NP sipōxtan/sipōz-'.\"},\n      {\"src\": \"FSF\", \"where\": \"Vāže-nāmak p.393\", \"stance\": \"partial\", \"note\": \"«این واژه از اضداد است … در بیت‌های زیر به معنی بیرون راندن: نه مرگ از تن خویش بتوان سپوخت …» — same verse, different sense-label.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/سپوختن\", \"stance\": \"supports\", \"note\": \"sense 4 'to delay, prolong', with a Šāhnāme citation, alongside sense 3 'to drive away, fend off, ward off, repel'.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Latin\", \"words\": \"pungere\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin pungō, pungere, pupugī, punctum 'to prick, pierce' is the nasal-infix present of the zero grade *pug- of the root: PIE *pu-n-g- > Lat. pungō, with the infix dropped outside the present system (perfect pupugī with reduplication, supine punctum). Pokorny p.828 lists it under peuk̑-/peug̑- ('Latin … pungo, -ere, pupugī punctum \\\"prick\\\"'), and Watkins/AHD gives it exactly as Nourai does: '2. Nasalized zero-grade form *pu-n-g- in Latin pungere, to prick.' Ernout-Meillet (s.v. pugnus) treat pugnus and pungō as the same root *peug-/pug-, the verb specialising to 'piquer'.\",\n     \"derivation_fa\": \"فعل لاتینی pungō / pungere با ماضی pupugī و صفت مفعولی punctum به معنی «سوراخ کردن، خلیدن» ساختِ «میان‌وند بینی» (nasal infix) بر درجهٔ صفرِ ریشه است: هندواروپایی *pu-n-g- ← لاتینی pungō، که این میان‌وند بیرون از نظام مضارع می‌افتد (از این‌رو pupugī و punctum بدون n). پوکورنی (ص ۸۲۸) و واتکینز هر دو همین را می‌گویند؛ واتکینز عیناً می‌نویسد «صورت بینی‌شدهٔ درجهٔ صفر *pu-n-g- در pungere لاتینی». ارنو و مِیه نیز pugnus «مشت» و pungō را از یک ریشه می‌دانند. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/puncture\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. peuk-: '2. Nasalized zero-grade form *pu-n-g- in Latin pungere, to prick: BUNG, POIGNANT, POINT, POINTILLISM, PONTIL, (POUNCE1), (POUNCE2), PUNCHEON1, PUNCTUATE, PUNCTURE, PUNGENT; COMPUNCTION, EXPUNGE, SPONTOON, TRAPUNTO.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW p.828 s.v. peuk̑-/peug̑-\", \"stance\": \"supports\", \"note\": \"'Latin pugil ds., pugnus m. \\\"fist\\\", pugno, -āre \\\"fight\\\", pungo, -ere, pupugī punctum \\\"prick\\\", pugio m. \\\"dagger\\\".'\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.15\", \"stance\": \"supports\", \"note\": \"under '2. *peug-': '… pugnus … pungo, -ere, pupugi, punctum'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. pugnus (LAT.txt l.50844)\", \"stance\": \"supports\", \"note\": \"'Peut-être même racine *peug-/pug- que dans pungō, pupugī, avec suffixe -no- comme dans somnus … la racine qui dans pungo a le sens spécial de \\\"piquer\\\".'\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. punctum/puncture (KLN_1966.txt l.31013)\", \"stance\": \"supports\", \"note\": \"'punctum … prop. neut. pp. of pungere, \\\"to pierce\\\"'; 'puncture, n. … L. punctura, \\\"a pricking\\\", fr. punctus, pp. of pungere.'\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"puncture; pivot, point, punctuate\", \"verdict\": \"disputed\",\n     \"derivation\": \"Three of the four are textbook, one is not. PUNCTURE: Late Latin punctūra 'a pricking' (from punctus, pp. of pungere) → Old French/Anglo-French → English, first attested late 14c. as a noun, verb from the 1690s (Klein; Etymonline). POINT: Latin punctum / Medieval Latin puncta → Old French point/pointe → Middle English point (Buck, Dict. of Selected Synonyms: 'It., Sp. punta, Fr. pointe (> ME, NE point) fr. MLat. puncta, new formation beside Lat. punctum \\\"puncture, point\\\" … fr. pungere'). PUNCTUATE: Medieval Latin punctuāre, punctuātus, from punctum. All three are listed under peuk- in Watkins' index. PIVOT is the odd one out: it is NOT in Watkins' index at all, and both Klein ('F. pivot, of uncertain origin') and Etymonline ('Old French pivot \\\"hinge pin, pivot\\\" (12c.), also \\\"penis\\\", a word of uncertain origin') refuse an etymology; Skeat derives it instead from Italian piva 'pipe' via a diminutive *pivo. Nourai's placing of pivot under pungere is therefore unsupported — hence the node verdict follows the weakest word.\",\n     \"derivation_fa\": \"از چهار واژهٔ این جعبه سه‌تا بی‌چون‌وچرا درست‌اند و یکی نه. puncture از لاتینی متأخر punctūra «خلش» (از punctus، صفت مفعولی pungere) از راه فرانسهٔ کهن به انگلیسی رسیده و نخستین کاربردش در اواخر سدهٔ چهاردهم میلادی است. point از punctum لاتینی / puncta لاتینی میانه از راه point/pointe فرانسهٔ کهن آمده است (باک، فرهنگ مترادف‌های هندواروپایی). punctuate از punctuāre لاتینی میانه است. هر سه در نمایهٔ واتکینز ذیل peuk- آمده‌اند. اما pivot اصلاً در نمایهٔ واتکینز نیست و کلاین («فرانسوی pivot، خاستگاه نامعلوم») و اتیمانلاین («pivot فرانسهٔ کهن، سدهٔ دوازدهم، خاستگاه نامعلوم») هر دو از ریشه‌یابی آن سر باز می‌زنند؛ اسکیت آن را از piva ایتالیایی «نی، لوله» می‌گیرد. پس گنجاندن pivot زیر pungere را پژوهش امروزی نمی‌پذیرد و حکم این گره را همان ضعیف‌ترین واژه تعیین می‌کند.\",\n     \"sources\": [\"https://www.etymonline.com/word/puncture\", \"https://www.etymonline.com/word/pivot\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 index lists 'PUNCTURE peuk-', 'PUNCTUATE peuk-' (l.2140) and 'POINT peuk-' (l.2112), plus POIGNANT, PONTIL, PUNGENT, COMPUNCTION, EXPUNGE — but there is NO entry 'PIVOT' anywhere in the index (grep 'PIVOT' over AHD_watkins1985.txt returns nothing). So AHD supports three of Nourai's four words and is silent on the fourth.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. puncture and s.v. pivot (KLN_1966.txt l.31013, l.28972)\", \"stance\": \"partial\", \"note\": \"'puncture, n. … L. punctura, \\\"a pricking\\\", fr. punctus, pp. of pungere' — supports; but 'pivot, n., a point or pin, etc., on which something turns. — F. pivot, of uncertain origin.' — contradicts the peuk- assignment.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. pivot (SKT.txt l.14068)\", \"stance\": \"contradicts\", \"note\": \"'pivot, a pin on which a wheel, &c. turns. (F. - Ital. - Low L.) F. pivot. Formed, with dimin. suffix -ot, from Ital. *pivo, weakened form of piva, a pipe … - Low L. pipa, a pipe.' — an entirely different origin.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck §12.34 / l.21913\", \"stance\": \"supports\", \"note\": \"'It., Sp. punta, Fr. pointe (> ME, NE point) fr. MLat. puncta, new formation beside Lat. punctum \\\"puncture, point\\\" …, fr. pungere \\\"prick, puncture\\\".'\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/puncture and /word/pivot\", \"stance\": \"partial\", \"note\": \"puncture: 'late 14c., from Late Latin punctura \\\"a pricking\\\", from Latin punctus, pp. of pungere \\\"to prick, pierce\\\"'; pivot: 'from Old French pivot \\\"hinge pin, pivot\\\" (12c.) … a word of uncertain origin.'\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"Persian\", \"words\": \"pančar «پنچر»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"پنچر pančar 'punctured, (of a tyre) flat' is a 20th-century European loan into Persian, taken with the arrival of the motor car; the donor is English 'puncture' /ˈpʌŋk.tʃə/, whose -ct- /k-tʃ/ cluster Persian simplifies to -nč- and whose final unstressed syllable it renders -ar, giving pančar (compare Urdu/Hindi पंक्चर pankchar, the same motoring loan on the same route through British India). Mo'in, Farhang-e Fārsi, records it as an unassimilated European loan — «پنچر (پَ چَ) [فر.] (اِ.) ۱ - سوراخ شدن لاستیک چرخ. ۲ - (عا.) خسته، زهوار دررفته» — printing the Latin-script etymon 'puncture' beside the headword; his tag [فر.] 'French' is best taken as a slip, since French has no such motoring word (a flat tyre is crevaison), while the English form matches the Persian shape exactly. The chart's arrow English puncture → Persian pančar is thus right; only the ultimate PIE link runs through Latin pungere (node #6).\",\n     \"derivation_fa\": \"«پنچر» وام‌واژه‌ای اروپایی است که در سدهٔ بیستم و همراه با آمدن اتومبیل وارد فارسی شد. صورت وام‌دهنده انگلیسی puncture است: خوشهٔ ـct‑ آن (k+č) در فارسی به ـنچ ساده شده و هجای پایانیِ بی‌تکیه ـar بازتاب یافته است؛ همین وام با همین مسیر (از انگلیسیِ هند بریتانیایی) در اردو و هندی نیز به صورت पंक्चर دیده می‌شود. معین در «فرهنگ فارسی» آن را وام‌واژه‌ای اروپایی ثبت کرده است: «پنچر (پَ چَ) [فر.] (اِ.) ۱ ـ سوراخ شدن لاستیک چرخ. ۲ ـ (عا.) خسته، زهوار دررفته»، و صورت لاتین puncture را کنار سرواژه چاپ کرده است؛ برچسب [فر.] یعنی فرانسوی به احتمال زیاد لغزش است، چون فرانسوی چنین واژه‌ای در معنای پنچری ندارد (فرانسوی crevaison می‌گوید) حال آنکه صورت انگلیسی دقیقاً با ساخت فارسی می‌خواند. پس پیکان «انگلیسی puncture ← فارسی پنچر» درست است.\",\n     \"sources\": [\"https://abadis.ir/fatofa/پنچر/\", \"https://www.etymonline.com/word/puncture\"],\n     \"ref_check\": [\n      {\"ref\": \"MON:822\", \"status\": \"partial\", \"note\": \"Mo'in's entry is confirmed but not at a page number I can check: the only local OCR of Mo'in is the 2-volume Adena reprint (MON_part1.txt l.32828), whose entry reads «پنچر ؛ puncture (اِ.) سوراخ شدن لاستیک» on a page numbered ۳۹۹ in that reprint — different pagination from the 6-volume Amir Kabir edition Nourai cites. The vajehyab/abadis text of Farhang-e Mo'in gives «پنچر (پَ چَ) [ فر . ] (اِ. ) ۱ - سوراخ شدن لاستیک چرخ . ۲ - (عا. ) خسته ، زهوار دررفته» — so Mo'in has the word and marks it a European loan, but labels it French rather than English.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in via abadis.ir/fatofa/پنچر/\", \"stance\": \"partial\", \"note\": \"«پنچر (پَ چَ) [ فر . ] (اِ. ) ۱ - سوراخ شدن لاستیک چرخ» — confirms the European loan and the gloss, but tags it [فر.] (French) where Nourai (and the phonetics) say English.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ (v1/v2 OCR)\", \"stance\": \"silent\", \"note\": \"grep for «پنچر» across BQT_v1_pages.txt / BQT_v2_pages.txt finds nothing — expected: Borhān is a 17th-century dictionary and cannot contain a motoring loan.\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/puncture\", \"stance\": \"supports\", \"note\": \"for the English donor: 'puncture (n.), late 14c., from Late Latin punctura \\\"a pricking\\\" … verb 1690s' — the English word from which the Persian motoring term is taken.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 3,\n   \"root\": \"Piko, Pikho\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *pik(h)o- 'lumpy thing, knot' (Pokorny piq(h)o-, IEW 830; WP II 70)\",\n   \"note\": \"Root, language label, gloss and BOTH cited pages are exactly right. Pokorny IEW p.830 heads the entry 'piq(h)o- \\\"klumpiges, Knoten\\\"' (the IED English dump renders it 'pik(h)o-. Meaning: lump, knot' — verbatim Nourai's 'Piko, Pikho : lump, knot'), and refers to WP. II 70, where Walde-Pokorny p.70 has the same entry with the same two witnesses. It should be said that this is one of the thinnest roots in Pokorny: it rests on exactly two items, the Avestan compound nava-pixəm and Latvian piks/pika 'clod of earth or clay, sniega-pika \\\"snowball\\\"', joined by Lidén (IF 19, 325f.) — no verb, no third branch, and the -q(h)o- is admitted to be possibly a mere suffix. The chart's Iranian descent is sound as far as Pahlavi pēxak; the New Persian box (#3) does not belong here, and the Sogdian box (#4) could not be verified.\",\n   \"note_fa\": \"ریشه، برچسب زبانی، معنا و هر دو ارجاع این نمودار درست است: پوکورنی در «فرهنگ ریشه‌شناختی هندواروپایی» (ص ۸۳۰) مدخل را با همین صورت piq(h)o- و معنی «کلوخه‌مانند، گره» آورده و به والده‑پوکورنی جلد دوم ص ۷۰ ارجاع می‌دهد، و آنجا نیز همین مدخل با همان دو گواه هست. باید افزود که این یکی از سست‌ترین ریشه‌های پوکورنی است: تنها بر دو داده استوار است، ترکیب اوستایی nava-pixəm و لتونیایی piks/pika «کلوخ گِل» و sniega-pika «گلولهٔ برف»، که لیدِن (IF ۱۹، ۳۲۵ به بعد) به هم پیوند داده است؛ نه فعلی در کار است، نه شاخهٔ سومی، و خودِ پوکورنی می‌پذیرد که ‑q(h)o- شاید تنها پسوند باشد. تبار ایرانیِ نمودار تا «پهلوی pēxak» درست است؛ اما گرهٔ فارسی نو (پیختن) به اینجا تعلق ندارد و گرهٔ سغدی را نتوانستم تأیید کنم.\",\n   \"sources\": [],\n   \"ref_check\": [\n    {\"ref\": \"POK:830\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 65 (German original, with the printed page number 830 standing a few lines above): 'piq(h)o- \\\"klumpiges, Knoten\\\". Av. pixa- \\\"Knoten\\\" in nava-pixəm \\\"neunknotigen\\\"; lett. piks, pika \\\"Erd- und Lehmklumpen\\\", sniega-pika \\\"Schneeballen\\\". WP. II 70.' Also POK_full.txt l.67940: 'Root / lemma: pik(h)o- | Meaning: lump, knot … Page(s): 830'.\"},\n    {\"ref\": \"WLD2:70\", \"status\": \"supports\", \"note\": \"Walde-Pokorny Bd. II p.70 (incoming/WLD/WLD_Bd2_pages.txt l.4680-4690, running head '70  piq(h)o- — pip-'): 'piq(h)o- \\\"klumpiges, Knoten\\\". Av. pixa- \\\"Knoten\\\" in nava-pixəm \\\"neunknotigen\\\" verbindet Lidén IF. 19, 325 f. ansprechend mit lett. piks, pika \\\"Erd- und Lehmklumpen\\\", snegapika \\\"Schneeballen\\\"; wenn -q(h)o- formantisch ist …, könnte allenfalls auch lett. -pate \\\"Kloß, Klumpen\\\" und (??) lit. pilas \\\"rund\\\" verwandt sein; lat. pila \\\"Ball\\\" aber zu pilus \\\"Haar\\\".'\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW p.830\", \"stance\": \"supports\", \"note\": \"see ref_check; entry sits between pid- 'gebären??' and pi-lo- 'Haar'.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p.70\", \"stance\": \"supports\", \"note\": \"see ref_check; note that WP explicitly flags lat. pila 'Ball' as NOT belonging here, so Nourai's added gloss 'ball' has no Western support.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, Indo-European roots appendix\", \"stance\": \"silent\", \"note\": \"grep of AHD_watkins1985.txt finds no root 'pik(h)o-' or 'piko-' — Watkins drops this root entirely (unsurprisingly, since it has no English reflex).\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. pikos 'a bird' (IEC.txt l.12879)\", \"stance\": \"partial\", \"note\": \"Mann has no root 'lump, knot'; he mentions the Latvian material only as an aside: '(Isophone: Latv. piks, m., pika, f. \\\"lump, clot\\\"; Alb. cf. pikset, 3s. \\\"coagulates\\\")' — i.e. he does not set up Pokorny's root.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"pixa; nava-pixem\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Younger Avestan nava.pixa- is a bahuvrīhi 'having nine knots', from nava- 'nine' (PIE *newn̥) + pixa- 'knot'; the accusative singular nava.pixəm is the attested form. Bartholomae, AiW, lists it: 'j. nava.pixa- Adj. \\\"mit neun Knoten\\\": graom ayasōiš .. °əm \\\"sollst du einen Rohrstock mit neun Knoten holen\\\" V[idēvdāt] 14', and repeats the phrase under grava- m. 'Rohrstock, Stock' — so the referent really is a ritual cane with nine knots, prescribed in the Vendīdād's purification passages, exactly Nourai's gloss. The simplex pixa- 'knot' is not independently attested: Pokorny and Walde-Pokorny extract it from the compound (Lidén IF 19, 325f.) and compare Latvian piks/pika 'clod'. Nourai's extra gloss 'ball' is his own extension from the Latvian 'snowball' and should be treated as a gloss on the Latvian, not on the Avestan word.\",\n     \"derivation_fa\": \"ترکیب اوستایی متأخر nava.pixa- یک صفت «بهوریهی» به معنی «دارای نُه گره» است، از nava- «نُه» و pixa- «گره»؛ صورت گواهی‌شده رایی مفرد nava.pixəm است. بارتولومه در «فرهنگ ایرانی باستان» آن را چنین می‌آورد: «nava.pixa- صفت، \\\"با نُه گره\\\": graom ayasōiš .. °əm یعنی باید چوب‌دستی‌ای با نُه گره بیاوری، وندیداد ۱۴»، و همین عبارت را ذیل grava- «چوب‌دستی» نیز تکرار می‌کند؛ پس مرجع آن به‌راستی عصایی آیینی با نُه گره است که در بخش‌های پاک‌سازیِ وندیداد تجویز شده — درست همان چیزی که نورایی گفته است. صورت سادهٔ pixa- «گره» به‌تنهایی گواهی ندارد و پوکورنی و والده‑پوکورنی (به پیروی از لیدِن) آن را از همین ترکیب بیرون کشیده‌اند. معنای افزودهٔ «گوی/توپ» در نمودار از روی لتونیایی sniega-pika «گلولهٔ برف» است نه از اوستایی.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"POK:830\", \"status\": \"supports\", \"note\": \"IEW p.830: 'Av. pixa- \\\"Knoten\\\" in nava-pixəm \\\"neunknotigen\\\"' — the Avestan node verbatim.\"},\n      {\"ref\": \"WLD2:70\", \"status\": \"supports\", \"note\": \"WP II 70: 'Av. pixa- \\\"Knoten\\\" in nava-pixəm \\\"neunknotigen\\\" verbindet Lidén IF. 19, 325 f. ansprechend mit lett. piks, pika \\\"Erd- und Lehmklumpen\\\"'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.v. nava.pixa- (BRT.txt l.18637) and s.v. grava- (l.10504)\", \"stance\": \"supports\", \"note\": \"'j. nava.pixa- Adj. \\\"mit neun Knoten\\\": graom ayasōiš .. °əm \\\"sollst du einen Rohrstock mit neun Knoten holen\\\" V. [Vidēvdāt] 14'; and s.v. grava- 'Rohrstock, Stock': 'graom ayasōiš .. nava.pixəm'. Confirms form, meaning and ritual context; Bartholomae lemmatises only the compound, not a simplex pixa-.\"},\n      {\"src\": \"POK\", \"where\": \"IEW p.830\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.70\", \"stance\": \"supports\", \"note\": \"see ref_check; WP notes the simplex is inferred and that the -q(h)o- may be a suffix.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"pĕxak\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Pahlavi pēxak is the Middle Persian continuation of Avestan pixa- with the productive diminutive/appurtenance suffix -ak (< OIr. *-aka-), i.e. *pixa-ka- > pēxak, the short i of an open syllable being lengthened/raised to ē in Middle Persian as regularly (cf. Av. diz- : MP dēz). The Šāyast nē-šāyast glossary (Tavoosi) has it on p.143 line 6, together with the compound pēxak-šnās at line 18, and the entry itself sets it beside '= nava-pixa- … pixa-' with a Bartholomae AiWb column reference — i.e. the same identification Nourai draws. Semantically it is not 'knot' but the ritual object, the nine-knotted cane of Vd. 14 (the barsom-like implement), which is why the Pahlavi Vidēvdād gloss carries it. NOTE on the wording: the printed page (p.372 of the book, PDF 402) really does read 'a stick with none knots'; 'none' is Nourai's own misprint for 'nine' — the extraction is faithful.\",\n     \"derivation_fa\": \"«pēxak» پهلوی دنبالهٔ pixa- اوستایی است با پسوند زایای ـak (از ایرانی باستان *-aka-)، یعنی *pixa-ka- ← pēxak؛ واکهٔ کوتاه i در هجای باز در فارسی میانه به ē کشیده شده است، درست مانند diz- اوستایی ← dēz پهلوی. واژه‌نامهٔ «شایست نه‌شایست» (توسی) آن را در ص ۱۴۳ سطر ۶ آورده و در سطر ۱۸ همان صفحه ترکیب pēxak-šnās را، و در خودِ مدخل با ارجاع به «فرهنگ ایرانی باستان» بارتولومه صورت‌های «nava-pixa-» و «pixa-» را کنار آن نهاده است — یعنی همان این‌همانی‌ای که نورایی کشیده است. از نظر معنایی pēxak نه «گره» بلکه همان ابزار آیینی، عصای نُه‌گرهِ وندیداد ۱۴، است. یک نکتهٔ فنی: در صفحهٔ چاپی کتاب (ص ۳۷۲) به‌راستی «a stick with none knots» چاپ شده؛ «none» غلط چاپی خودِ نورایی به‌جای «nine» است و استخراج داده‌ها درست عمل کرده است.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"pĕxak : a stick with none knots\",\n     \"correct_form\": \"pēxak : a stick with nine knots\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"SNS:143\", \"status\": \"supports\", \"note\": \"Tavoosi, Šāyast nē-šāyast glossary: the back index (SNS.txt l.31502) reads 'pexak 143/6' and 'pēxak šnās 143/18'; the corresponding page block (SNS_pages.txt \\\\f-block 87, which also carries pēš ud pas 143/2 and pētrōt 142/14) shows the entry with '…ak:' followed by '= nava-pixa , pixa-:' and an '(AiWb. 1045…)' column reference. Page number and content both check out.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD\", \"stance\": \"silent\", \"note\": \"grep of PHD.txt / PHD_mackenzie.txt for 'pēxak', 'pexak', 'pyhk' finds nothing — MacKenzie's concise dictionary omits this rare Vidēvdād-gloss word.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\", \"note\": \"grep of NYB_vol2_glossary.txt for 'pexak/pēxak' finds nothing; Nyberg's glossary covers only the texts of Part I.\"},\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.v. nava.pixa-\", \"stance\": \"supports\", \"note\": \"confirms the Avestan base the SNS glossary points to: 'nava.pixa- Adj. \\\"mit neun Knoten\\\" … \\\"sollst du einen Rohrstock mit neun Knoten holen\\\"' — hence 'nine', not 'none'.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"pîxtan «پیختن»\", \"verdict\": \"disputed\",\n     \"derivation\": \"پیختن is a real (archaic) Persian verb, but it does not come from pēxak. It is the past-stem infinitive of the verb whose present stem is پیچ pēč- : MP pēč- , past pēxt (*pati-čaxta-) → NP پیختن beside پیچیدن and پیچاندن, exactly as ریختن : ریز-, آمیختن : آمیز-, گریختن : گریز-. Wiktionary gives پیختن (pixtan) 'to twist; wrap', obsolete, present stem پیچ (pič), derived terms پیچیدن, پیچاندن; Mo'in glosses it «۱ - پیچیدن. ۲ - پخش کردن، افشاندن» and Dehkhoda «پیچیدن، برتافتن، پیچاندن». Cheung 2007 (s.v. *čaiH, p.36) states the etymology of the family explicitly: 'Persian *pēč, BMP pyc-, NP pēc-/pēcīdan \\\"to twist, distort, bend, wreathe, coil\\\" … it derives from adverb *pati-ča \\\"back\\\" + čay- \\\"to collect\\\", Nyberg II: 160a f.' — nothing to do with a knotted stick. Morphologically too, a noun pēxak 'nine-knotted cane' cannot yield a transitive verb 'to wrap'. Finally the illustration is itself doubtful: the Šāhnāme line is standardly read «ز بالا بر ایشان درم ریختند / ز بر مشک و عنبر همی بیختند» with بیختن 'to sift' (so Noushin, Vāže-nāmak, three times), not پیختند. Modern scholarship therefore puts پیختن with پیچیدن (< *pati-čay-), and Nourai's arrow from Pahlavi pēxak is rejected.\",\n     \"derivation_fa\": \"«پیختن» فعلی کهنِ راستین در فارسی است، اما از pēxak نمی‌آید. این مصدرِ ساخته‌شده از ستاک گذشتهٔ همان فعلی است که ستاک حالش «پیچ» است: فارسی میانه pēč-، گذشته pēxt (از *pati-čaxta-) ← «پیختن» در کنار «پیچیدن» و «پیچاندن»؛ درست مانند ریختن/ریز-، آمیختن/آمیز-، گریختن/گریز-. ویکی‌واژه «پیختن» را با ستاک حالِ «پیچ» و واژه‌های هم‌خانوادهٔ «پیچیدن» و «پیچاندن» ثبت کرده، معین آن را «۱ ـ پیچیدن ۲ ـ پخش کردن، افشاندن» و دهخدا «پیچیدن، برتافتن، پیچاندن» معنا کرده‌اند. چونگ (۲۰۰۷، ذیل *čaiH) صریح می‌گوید: «فارسی *pēč، پهلوی کتابی pyc-، فارسی نو pēc-/pēcīdan … از قید *pati-ča \\\"باز، پس\\\" به‌علاوهٔ فعل čay- \\\"گرد آوردن\\\" است؛ نیبرگ، جلد دوم، ۱۶۰ الف». افزون بر این، از نظر ساختواژی هم اسمِ pēxak «عصای نُه‌گره» نمی‌تواند فعل متعدیِ «پیچیدن» بسازد. سرانجام، شاهدِ نمودار نیز مشکوک است: بیتِ شاهنامه در خوانش رایج «ز بالا بر ایشان درم ریختند / ز بر مشک و عنبر همی بیختند» است با «بیختن» (الک کردن)، نه «پیختند» (نوشین در «واژه‌نامک» سه بار همین صورت را دارد). پس ریشه‌شناسی امروزی «پیختن» را با «پیچیدن» می‌گذارد و پیکان نورایی از pēxak پذیرفته نیست.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/پیختن\", \"https://abadis.ir/fatofa/پیختن/\"],\n     \"ref_check\": [\n      {\"ref\": \"MON:880\", \"status\": \"partial\", \"note\": \"Mo'in does have پیختن — the vajehyab/abadis text of Farhang-e Mo'in gives «پیختن: ۱ - پیچیدن . ۲ - پخش کردن ، افشاندن» — but he offers no derivation from pēxak (Mo'in's bracketed origin tag is absent here), and the page number cannot be checked against the only local Mo'in OCR, which is the 2-volume Adena reprint with different pagination (grep of MON_part1.txt for «پیختن» returns only the unrelated اشپوختن/اشپیختن entry).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/پیختن\", \"stance\": \"contradicts\", \"note\": \"'پیختن (pixtan), obsolete verb, \\\"to twist; wrap\\\"; present stem پیچ (pič); derived terms پیچیدن (pičidan), پیچاندن (pičândan)' — i.e. it belongs to the pēč- family, not to pēxak.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p.36, discussion s.v. *čaiH1 'to sew' (CHEUNG.txt l.3098)\", \"stance\": \"contradicts\", \"note\": \"'Persian *pēc, BMP pyc-, NP pēc-/pēcīdan \\\"to twist, distort, bend, wreathe, coil, wind in a serpentine form\\\" (borrowed into modern dialects) is probably unrelated [sc. to *čaiH], it derives from adverb *patiča \\\"back\\\" + čay- \\\"to collect\\\", Nyberg II: 160a f.'\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in via abadis.ir/fatofa/پیختن/\", \"stance\": \"partial\", \"note\": \"«۱ - پیچیدن . ۲ - پخش کردن ، افشاندن»; Dehkhoda on the same page: «پیچیدن، برتافتن، پیچاندن»; ʿAmid cites Neẓāmi «همه طومارها به هم درپیخت» — all in the 'twist/wrap' family, none in the 'knot' family.\"},\n      {\"src\": \"FSF\", \"where\": \"Noushin, Vāže-nāmak (FSF_pages.txt l.5938, 9187, 13808)\", \"stance\": \"contradicts\", \"note\": \"the Šāhnāme hemistich Nourai quotes is printed three times in Noushin's glossary as «ز بر مشک و عنبر همی بیختند» (root بیختن 'to sift'), never as پیختند.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Sogdian\", \"words\": \"pyx\", \"verdict\": \"unverified\",\n     \"derivation\": \"I could not confirm a Sogdian word pyx 'knot' anywhere. Gharib's Sogdian Dictionary p.335 (SOD_pages.txt \\\\f-block 402, which carries the printed page number 335 and entries 8317-8340) runs pyʾtyh, pyʾtyy, pyč(h), pyδ-, pyδʾr, pyδh 'elephant', pyδpʾk, pyksʾk(w), pymʾkh, pyms-, pyn-, pynmcyq … — there is no pyx entry there, nor on the facing pages 334/336/337, where the sequence goes straight from pyt- (8387-8389) to pyz- (8390). A grep for 'pyx' across the whole of SOD.txt/SOD_pages.txt returns nothing (the OCR preserves x elsewhere, e.g. pxwst-, spxs-), and Gharib's English index gives 'knot' only at entry 4187 = γrʾns 'knot, bond, joining'. Neither Pokorny nor Walde-Pokorny cites any Sogdian for this root — their only Iranian witness is the Avestan compound. If a Sogdian pyx exists it is not in the standard dictionary at the page Nourai cites; a web search turned up nothing either. Formally such a word would be unobjectionable (Sogd. pyx < *pixa-), which is why I mark this unverified rather than disputed.\",\n     \"derivation_fa\": \"نتوانستم واژهٔ سغدی pyx «گره» را در هیچ منبعی تأیید کنم. «فرهنگ سغدی» بدرالزمان قریب در ص ۳۳۵ (که شمارهٔ صفحه روی همان برگ چاپ شده و مدخل‌های ۸۳۱۷ تا ۸۳۴۰ را دارد) این مدخل‌ها را می‌آورد: pyʾtyh، pyč(h)، pyδ-، pyδh «فیل»، pyδpʾk، pyksʾk(w)، pymʾkh، pyms-، pyn-، pynmcyq … و هیچ مدخل pyx در آن نیست؛ در صفحه‌های روبه‌رو (۳۳۴، ۳۳۶، ۳۳۷) هم رشتهٔ مدخل‌ها یکسره از pyt- به pyz- می‌رود. جست‌وجوی «pyx» در کل متن فرهنگ قریب هیچ نتیجه‌ای ندارد (حال آنکه OCR حرف x را در جاهای دیگر مانند pxwst- و spxs- نگاه داشته است)، و نمایهٔ انگلیسی قریب برای «knot» تنها مدخل ۴۱۸۷ یعنی γrʾns را می‌دهد. پوکورنی و والده‑پوکورنی نیز هیچ گواه سغدی برای این ریشه نیاورده‌اند. از نظر آوایی چنین صورتی ناممکن نیست (سغدی pyx از *pixa-)، و به همین سبب حکم را «تأییدنشده» گذاشتم نه «ردشده».\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"SOD:335\", \"status\": \"not_found\", \"note\": \"Gharib, Sogdian Dictionary, printed p.335 = SOD_pages.txt \\\\f-block 402 (the block opens with the printed number '335'); it contains entries 8317-8340 (pyʾtyh … pyntpʾt), with no pyx. Neighbouring pages 334 (block 401) and 336-338 (blocks 403-405) likewise have none; grep 'pyx' over SOD.txt and SOD_pages.txt returns zero hits. Gharib's English index (SOD.txt l.91069) has 'knot 4187' only, = entry 4187 γrʾns 'knot, bond, joining'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary pp.334-338 and the English index\", \"stance\": \"silent\", \"note\": \"see ref_check: the dictionary has no pyx; its word for 'knot' is γrʾns / γrʾmk (entry 4187, 'knot, bond, joining').\"},\n      {\"src\": \"POK\", \"where\": \"IEW p.830 s.v. piq(h)o-\", \"stance\": \"silent\", \"note\": \"the entry's only Iranian witness is 'Av. pixa- \\\"Knoten\\\" in nava-pixəm'; no Sogdian is cited.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.70\", \"stance\": \"silent\", \"note\": \"likewise only Avestan and Latvian; no Sogdian.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-402.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/write-402.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-402.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 402"
}
```


### [2026-09-14T01:11:06.459Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 12/12
node verdicts: {'disputed': 3, 'plausible': 2, 'confirmed': 6, 'unverified': 1}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 5, 'contradicts': 1, 'supports': 8, 'not_found': 2}
books consulted: {'silent': 7, 'contradicts': 5, 'partial': 8, 'supports': 23} | by book: {'PHD': 6, 'CHEUNG': 4, 'Wiktionary': 4, 'NYB': 4, 'BRT': 3, 'FSF': 3, 'POK': 3, 'WLD': 3, 'KLN': 2, 'Etymonline': 2, 'MON': 2, 'HUB': 1, 'HRN': 1, 'LAT': 1, 'SKT': 1, 'SYN': 1, 'BQT': 1, 'SOD': 1}
```


## [2026-09-14T01:11:28.141Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-402.json` written; `verify_check.py 402` reports **0 PROBLEM lines** (12/12 nodes, 2 roots).

**Page 402 (book p. 372) — verdicts**
- Roots: 2 confirmed (Peuk/Pug = POK 828 / Watkins "peuk-, also peug-, to prick"; Piko/Pikho = POK 830 / WP II 70 "piq(h)o- klumpiges, Knoten")
- Nodes: 6 confirmed, 2 plausible, 3 disputed, 1 unverified
- Ref checks: 8 supports, 5 partial, 1 contradicts, 2 not_found. 18 books consulted.

**Disputed / unverified**
- *Peuk, Pug* #1 **Avestan spôz** — no such Avestan verb exists; Bartholomae has no root spaz-/spōz-. Both cited refs are Middle Persian (SNS 175 = Pahlavi spōzēd; Hübschmann 73 = Pāzand/Armenian). Cheung 2007:354 sets up Ir. *spauč? attested only in MP/NP and says flatly "an IE origin cannot be ascertained". Node should read [Middle Persian].
- *Peuk, Pug* #7 **English pivot** — not in Watkins' index at all; Klein and Etymonline both say "of uncertain origin", Skeat derives it from Ital. *piva* 'pipe'. (puncture, point, punctuate are all fine.)
- *Piko* #3 **Persian پیختن** — it is the past-stem infinitive of پیچ‌/پیچیدن (Wiktionary: present stem پیچ; Cheung: NP pēč- < *pati-ča + čay-, Nyberg II 160a), not a derivative of pēxak 'nine-knotted cane'. The Šāhnāme line quoted is standardly «…همی بیختند» (بیختن 'to sift'), so printed by Noushin three times.
- *Piko* #4 **Sogdian pyx 'knot'** — unverified: not on Gharib p. 335 (entries 8317–8340) nor anywhere in the dictionary; his only 'knot' word is γrʾns (entry 4187). POK/WP cite no Sogdian for this root.

**Book misprint (extraction is faithful — no data fix needed)**
- Pahlavi node *pĕxak* is printed on p. 372 as "a stick with **none** knots"; Nourai's typo for "nine" (Bartholomae: nava.pixa- 'mit neun Knoten', Vd 14). Recorded with `error_in: "book"`; page image copied to `data/verification/sources/refs/ocr/BOOK/402.png`.

**Citation page-number problems (Nourai's, not the data's)**
- `FSF:221` (both Persian سپوختن nodes): the entry is on p. **393** of the Donyā 1363 scan; p. 221 is in the پ section.
- `MON:822` / `MON:880`: unverifiable against the local 2-vol Adena reprint (different pagination); content confirmed via Mo'in on abadis.
- `BQT:1091`, `HRN:156`, `HUB:73`, `SNS:143`, `SNS:175`, `POK:828`, `POK:830`, `WLD2:70`, `AHD` all check out exactly, including Horn's own hedge about *pungere* that the chart's NOTE records.
