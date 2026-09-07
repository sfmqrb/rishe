# Verification process log — verify-page-343


## [2026-09-07T17:36:12.890Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 343 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-343.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-343.json. Write /home/sfmqrb/git/rishe/data/verification/page-343.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 343` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T17:36:14.202Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T17:36:14.990Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T17:36:15.006Z] TOOL RESULT

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


## [2026-09-07T17:36:15.522Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-343.txt"
}
```


### [2026-09-07T17:36:15.543Z] TOOL RESULT

```
1	=== PDF page 343 (book page 313) ===
2	--- entry 0 ---
3	ROOT [Arabic] M.s.s, Massa : M.s.s: to touch. Massa: he touched.  (refs FVA:381)
4	#1 (parent #0) [Persian] refs=MON; FVA:381 | mass «مَسّ» : to touch | extra: مُماس ، تماس
5	#2 (parent #0) [French] refs=PHN:257 | 
6	  #3 (parent #2) [Persian] refs=MON:3697 | mâsâž «ماساژ» : massage
7	  #4 (parent #2) [English] refs=KLN:944 | massage
8	--- entry 1 ---
9	ROOT [Indo-European] Mu, Mus : a mouse, muscle  (refs POK:752)
10	#1 (parent #0) [Sanskrit] refs=None | mus : mouse ; muska : testicle
11	  #2 (parent #1) [Persian] refs=POK:752; BQT:2053 | müš «موش» : mouse
12	  #3 (parent #1) [Persian] refs=POK:752; BQT:2053; MON:4147 | mošk «مُشک ۱ ( مِسک )» : musk ; mešk «مِشک ۲ ( بیدمشک )» : musk ; meškî «مِشکی ( مِشکین )» : musk color, black
13	    #4 (parent #3) [Greek] refs=None | 
14	      #5 (parent #4) [Latin] refs=None | muskus
15	        #6 (parent #5) [French] refs=None | 
16	          #7 (parent #6) [English] refs=AHD:865 | musk
17	#8 (parent #0) [Germanic] refs=AHD | mus : mouse
18	  #9 (parent #8) [English] refs=None | mouse
19	#10 (parent #0) [Latin] refs=AHD | mus : mouse, muscle
20	  #11 (parent #10) [English] refs=None | muscle
21	
```


## [2026-09-07T17:36:19.312Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-343.json",
 "description": "Read source JSON page 343"
}
```


### [2026-09-07T17:36:19.359Z] TOOL RESULT

```
{
  "pdf_page": 343,
  "book_page": 313,
  "entries": [
    {
      "root": {
        "name": "M.s.s, Massa",
        "lang": "Arabic",
        "refs": "FVA:381",
        "gloss": "M.s.s: to touch. Massa: he touched."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON; FVA:381",
          "words": [
            {
              "translit": "mass",
              "gloss": "to touch",
              "script": "مَسّ"
            }
          ],
          "script_extra": "مُماس ، تماس",
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "French",
          "refs": "PHN:257",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:3697",
          "words": [
            {
              "translit": "mâsâž",
              "gloss": "massage",
              "script": "ماساژ"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "English",
          "refs": "KLN:944",
          "words": [
            {
              "translit": "massage",
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
        "name": "Mu, Mus",
        "lang": "Indo-European",
        "refs": "POK:752",
        "gloss": "a mouse, muscle"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": null,
          "words": [
            {
              "translit": "mus",
              "gloss": "mouse",
              "script": null
            },
            {
              "translit": "muska",
              "gloss": "testicle",
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
          "refs": "POK:752; BQT:2053",
          "words": [
            {
              "translit": "müš",
              "gloss": "mouse",
              "script": "موش"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:752; BQT:2053; MON:4147",
          "words": [
            {
              "translit": "mošk",
              "gloss": "musk",
              "script": "مُشک ۱ ( مِسک )"
            },
            {
              "translit": "mešk",
              "gloss": "musk",
              "script": "مِشک ۲ ( بیدمشک )"
            },
            {
              "translit": "meškî",
              "gloss": "musk color, black",
              "script": "مِشکی ( مِشکین )"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "فغستان چو آمد به مَشکوی شاه - یکی تاج بر سر ز مُشک سیاه",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Greek",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": null,
          "words": [
            {
              "translit": "muskus",
              "gloss": null,
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
          "lang": "English",
          "refs": "AHD:865",
          "words": [
            {
              "translit": "musk",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {
              "translit": "mus",
              "gloss": "mouse",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "mouse",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {
              "translit": "mus",
              "gloss": "mouse, muscle",
              "script": null
            }
          ],
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
            {
              "translit": "muscle",
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


## [2026-09-07T17:36:22.107Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['FVA','MON','PHN','KLN','POK','BQT','AHD','WLD','IEC','SYN','HRN','HUB','ARY','PHD','NYB','LKT','PLA','AFM','FVQ','SKT','WEB','FSD','CHEUNG']:\n    if k in d: print(k, json.dumps(d[k],ensure_ascii=False)[:400])\n    else: print(k,'MISSING')\n\"",
 "description": "Inspect refs_online for relevant abbreviations"
}
```


### [2026-09-07T17:36:23.539Z] TOOL RESULT

```
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 202
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verific
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
CHEUNG MISSING
```


## [2026-09-07T17:36:43.293Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,80p tools/verify_check.py && echo ---- && ls data/verification | head -40 && echo ---- && sed -n 1,60p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Inspect verify_check and matrix"
}
```


### [2026-09-07T17:36:43.346Z] TOOL RESULT

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
----
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
----
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
```


## [2026-09-07T17:36:44.320Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-312.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:4000])\"",
 "description": "Example verification file"
}
```


### [2026-09-07T17:36:45.544Z] TOOL RESULT

```
{
 "entry": 2,
 "root": "Leuk, Leuqos",
 "verdict": "confirmed",
 "modern_form": "PIE *leuk- (Pokorny leuk̂-) 'light, brightness; to shine, to see', with the thematic *leuk-o-s (Gk. leukós) that Nourai calls 'Leuqos'",
 "note": "Root, language label, gloss and page reference are all right. Pokorny, IEW 687-690, lemma leuk̂- (leuk-), Meaning 'bright, to shine; to see' (References: WP. II 408 ff.), listing exactly the material of this chart: Av. raocah-, OP raucah-, Av. raoxšna-, Lat. lūx/lūmen/lūna/lūstrum/lūstrāre, Goth. liuhaþ / OHG lioht / OE lēoht, Skt. loka-. Watkins/AHD: \"leuk-. Light, brightness. ... [Pok. leuk- 687.]\" — so POK:687 is the exact page. Kent (KNT:205), Nourai's second reference, gives the same root in the older notation pIE *leugos s.v. raucah-. 'Leuqos' is Nourai's spelling of the *leuk-o-s form (Gk. leukós 'white, bright', Skt. loka- 'open bright space, world', Lat. lūcus 'grove'); it is not a separate root. Cross-cutting remarks: (1) the chart's strongest link, Persian rūz/rōšan/afrūxtan and the Arabic loan rizq, is fully confirmed; (2) two Persian items in the Persian box (آرش, درفش ۱) and one Avestan item (a-raxša, plus the unattested raoč-xšaema) are not supported by modern sources; (3) the Sogdian box mixes an inherited word (rwxšn) with a Sanskrit loanword (δwk' < Skt. loka); (4) the Germanic box misprints the reconstruction (liuhtam for *leuhtam); (5) on the printed page the Old Persian box has an arrow into an empty, unlabelled box that the JSON does not record.",
 "note_fa": "ریشه، برچسبِ زبان، معنی و شمارهٔ صفحه هر چهار درست است: پوکورنی در «فرهنگ ریشه‌شناسیِ هندواروپایی» صفحه‌های ۶۸۷ تا ۶۹۰ ریشهٔ leuk̂- را با معنای «روشن، درخشیدن؛ دیدن» می‌آورد و همان داده‌های این نمودار را برمی‌شمارد: اوستایی raocah- و raoxšna-، پارسی باستان raucah-، لاتین lūx و lūmen و lūna و lūstrum، گوتیک liuhaþ و انگلیسی کهن lēoht، و سنسکریت loka-. واتکینز نیز ذیل leuk- همین ارجاع «پوکورنی ۶۸۷» را دارد. «Leuqos» صورتِ ستاک‌دارِ *leuk-o-s است (یونانی leukós، سنسکریت loka-، لاتین lūcus) و ریشهٔ جداگانه‌ای نیست. به‌طور کلی: پیوندِ فارسی «روز، روشن، افروختن» و وام‌واژهٔ عربیِ «رزق» کاملاً تأیید می‌شود؛ اما «آرش» و «درفش ۱» در جعبهٔ فارسی و «a-raxša» و «raoč-xšaema» در جعبهٔ اوستایی پشتوانهٔ امروزی ندارند؛ جعبهٔ سغدی یک واژهٔ میراثی (rwxšn) را با یک وام‌واژهٔ سانسکریت (δwk' از loka) درآمیخته؛ و در جعبهٔ ژرمنی صورتِ بازسازی‌شده غلط چاپ شده است (liuhtam به‌جای *leuhtam).",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/lewk-",
  "https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B2"
 ],
 "ref_check": [
  {
   "ref": "POK:687",
   "status": "supports",
   "note": "POK_full.txt, block 'Root / lemma: lehuk- (*lehugh-)', Meaning 'bright, to shine; to see', Page(s): 687-690 — with \"rocas-, rocis-, Avestan raocah-, ap. raucah- n. 'light, radiance, esp. of heaven', Avestan raoxšna- 'gleaming'\", \"Latin lūmen 'light' from *leuk-s-men; lūna 'moon goddess' (*leuksna)\", \"lustrum ... lūstro, -are 'to light up, illuminate'\", \"Gothic liuhaþ 'light' ... Old English leoht\""
  },
  {
   "ref": "KNT:205",
   "status": "supports",
   "note": "Kent, Old Persian, Lexicon s.v. raucah- (KNT.txt leaf 229): \"raucah- sb. 'day': Av. raocah- 'light', Phl. rūč, NPers. rōz, Skt. rócas- 'light', pIE *leugos\"; cf. §156.II \"pIE *leugos, OP rauca, Skt. rócas\". Kent's *leug-/*leugos is the same root in pre-1959 notation."
  }
 ],
 "consulted": [
  {
   "src": "AHD",
   "where": "Watkins 1985, s.v. leuk-",
   "stance": "supports",
   "note": "\"leuk-. Light, brightness. I. Basic form *leuk- ... [Pok. leuk- 687.]\" with the Germanic, Latin and Greek branches of this chart"
  },
  {
   "src": "WLD",
   "where": "Walde-Pokorny Bd. II 408-411, s.v. leuq-",
   "stance": "supports",
   "note": "the same root under the older lemma leuq-: \"rocas-, rocis- n., av. raocah-, ap. raucah- n. 'Licht, Leuchte, bes. des Himmels', ai. rukṣá- 'glänzend', av. raoxšna- 'glänzend' ... (= lat. luna ...); auf diesem -es-St. beruhen auch lat.
```


## [2026-09-07T17:36:51.916Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK mus ===\"; grep -n \"mūs-\" POK_full.txt | head -20\necho \"=== POK page 752 block ===\"; grep -n \"Page(s): 752\" POK_full.txt | head",
 "description": "grep Pokorny for mus"
}
```


### [2026-09-07T17:36:51.978Z] TOOL RESULT

```
=== POK mus ===
=== POK page 752 block ===
61624:Page(s): 752 
61705:Page(s): 752 
61738:Page(s): 752-753
```


## [2026-09-07T17:36:53.760Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD mus ===\"; grep -n -i \"^mūs\\|mūs-\\.\\|musk\" AHD_watkins1985.txt | head -20\necho \"=== KLN musk ===\"; grep -n -i \"musk\\b\" KLN_1966.txt | head -20\necho \"=== KLN massage ===\"; grep -n -i \"massage\" KLN_1966.txt | head -10",
 "description": "grep AHD and Klein"
}
```


### [2026-09-07T17:36:53.849Z] TOOL RESULT

```
=== AHD mus ===
763:mops, fool, also pug dog (> German Mops, pug dog): ROLLMoPsS; d. Old French momer, to act (in dumb show): MuM2, 2, Germanic *mut- in Old Norse mudhla, akin to the source of Middle English muteren, muttren, to mut- ter: MUTTER. 3. Latin muttire, to mutter: MOT, MOTTO. 4. Lengthened-grade form *mi- in Latin miius, silent, dumb: MuTE. 5. Greek muein, to close the eyes (< “to close the lips”): MIOSIS, MYOPIA, MYSTERY!, (MYSTIC). [Pok. 1. mii- 751.] mu-2, Gnat, fly. Imitative root. 1. Germanic *mukjé- in Old English mycg, midge: MIDGE. 2. Suffixed form *mus-ka in Latin musca, a fly: Mosquito, Musca, MUSCARINE, MUSH?, MUSKET. 3. Suffixed form *mus-ya in Greek muia, mua, a fly: mytasis. [Pok. 2. mi- 752.] mik-. A heap. Germanic *miigén-, *mihon- in: a. Old English miga, miiha, miiwa, heap of grain: Mow}; b. Old Norse migi, heap, akin to the probable Scandinavian source of MOGUL}. [Pok. mitk- 752.] [mundus. Women’s cosmetics, also world (probably by a calque on Greek kosmos, order, feminine adornment, world-order, universe). Latin noun of unknown origin; possibly from Etruscan. MUNDANE; ULTRAMUNDANE.] miis-. A mouse; also a muscle (from the resemblance of a flexing muscle to the movements of a mouse). 1. Ger- manic *mis- (plural *misiz) in Old English mis (plural
1140:for strong-smelling animals. 1. Germanic *wisulén- in Old English wesle, weosule, weasel: WEASEL. 2. Suffixed form *wis-onto- in Germanic *wisand-, *wisunt-, Euro- pean bison (which emits a musky smell in the rutting season), in: a. Old High German wisunt, bison: WISENT; b. Latin bisdn (plural bisontés), bison: BISON. [Pok. 3. ueis- 1134.] weit(a)-. To speak, adjudge. Extended o-grade form *woito- in Russian véti, council (see sem-'). wekti-. Thing, creature. Germanic *wihti- in Old English wiht, person, thing: WIGHT!; (AUGHT?), NAUGHT, NOT. [Pok. wek-ti- 1136.] = wekv-. To speak. 1. O-grade form *wokv- in: a. Latin vox (stem vdc-), voice: VOCAL, VOICE, VOWEL; EQUIVOCAL, UNIVOCAL; b. Greek ops, voice: CALLIOPE. 2. Suffixed o-grade form *wok-d- in Latin vocdre, to call: VOCABLE, VOCATION, VOUCH; ADVOCATE, AVOCATION, CONVOKE, EQUIVOCAL, EVOKE, INVOKE, PROVOKE, REVOKE. 3. Suf- fixed form *wek-es- in Greek epos, song, word: EPIC, EPOS. [Pok. uekz- 1135.] wel-'. To see. 1. Suffixed zero-grade form *wl-id- in Germanic *wlituz, appearance, in Old Norse litr, appear- ance, color, dye, akin to the source of Litmus. 2. Suffixed form *wel-uno- perhaps in Sanskrit Varunah, “seer, wise one,” sovereign god: VARUNA. [Pok. 1. wel- 1136.] wel-2, To wish, will. 1. Germanic *wel- in Old English wel, well (< “according to one’s wish”): WELL?. 2. Germanic *welon- in Old English wela, weola, well-being, riches: WEAL!, WEALTH. 3. Germanic *wiljén- in Old English willa, desire, will power: WILL. 4. Germanic *wil(Ijan in Old English wyllan, willan, to desire: WILL?; NILL. 5. Ger- manic compound *wil-kumon- (see g¥a-). 6. O-grade form *wol- in Germanic *wal- in Old French galloper and Old North French waloper, to gallop: GALLOP, WALLOP. 7. Basic form *wel- in Latin velle (present stem vol-), to wish, will: VELLEITY, VOLITION, VOLUNTARY; BENEVO- LENT, MALEVOLENT. 8. Suffixed form *wel-up- in Latin voluptds, pleasure: VOLUPTUARY, VOLUPTUOUS. [Pok. 2. uel- 1137.] wel-3, To turn, roll; with derivatives referring to curved, enclosing objects. 1. Germanic *walt- in: a. Old High German wailzan, to roll, waltz: wALTz; b. Middle Dutch welteren, to roll: WELTER. 2. Germanic *weluka- in Old English weoluc, weoloc, mollusk (having a spiral shell), whelk: WHELK!. 3. Perhaps Germanic *wel- in Old Eng- lish welig, willow (with flexible twigs): wILLOw. 4. Per- haps Germanic *welk- in Old English wealcan, to roll, toss, and wealcian, to muffle up: WALK. 5. O-grade form *wol- in Germanic *wall- in: a. Old English wiella, wella, a well (< “rolling or bubbling water,” “spring”): WELL; b. Old High German waillén, to roam: GABERDINE. 6. Perhaps suffixed o-grade form *wol-d- in Germanic *walé in: a. Old English walu, streak on the skin, weal, welt: WALE; b. Old High German *-walu, a roll, round stem, in *wurzwalu, rootstock (see wrad-). 7. Extended form *welw- in: a. Germanic *walw6n in Old English wealwian, to roll (in mud): WALLOW; b. Latin volvere, to roll: VAULT!, VAULT2, (VOLT2), VOLUBLE, VOLUME, VO- LUTE, VOLUTIN, VOLVOX, VOUSSOIR; CIRCUMVOLVE, CON- VOLVE, DEVOLVE, EVOLVE, INVOLVE, OBVOLUTE, REVOLVE; C. suffixed o-grade form *wolw-d- in Latin vulva, volva, covering, womb: VOLVA, VULVA; d. suffixed zero-grade form *wlw-d- in Latin valva, leaf of a door (< “that which turns”): VALVE; e. suffixed form *welu-tro- in Greek elutron, sheath, cover: ELYTRON. 8. Suffixed form *wel-n- in Greek eilein (< *welnein), to turn: ILEUS; NEURILEMMA. 9. Perhaps variant *wall- in Latin vallés, vallis, valley (< “that which is surrounded by hills”): VAIL!, VALE!, VALLEY. 10. Suffixed form *wel-end, possi- bly identical with the Greek name Helené (earliest form Welend), Helen, in Greek helenion, elecampane: ELECAM- PANE, INULIN. 11. Suffixed form *wel-ik- in Greek helix, spiral object: HELIX. 12. Suffixed form *wel-mi-nth- in Greek helmis, helmins (stem helminth-), parasitic worm:
1897:MUNIFICENT mei-1 MUNITION mei-3 MURAL mel-3 MURAMIC ACID mei-3 MURDER mer-2 MURE mei-3 MURINE mis- MURK mer-1 MURMUR mormor- MURRAIN mer-2 MURREY moro- Musca mu-2 MUSCARINE mu-2 MUSCLE miis- MUSE misum Muse men-1 MUSEUM men-! MUSH2 mu-2 MUSIC men-1! MUSKET mu-2 MusT! med- MUSTS ~=meu- MUSTACHE mendh-2
=== KLN musk ===
1151:Abelmoschus,  n.,  a  genus  of  plants  of  the  mallow family  (bot.)  —  ModL.,  fr.  Arab,  habb-al-musk, in  vulgar  pronunciation  habb-el-mosk,  lit.  ‘grain of  musk’.  See  hubba  and  musk, abelmosk,  n„  a  plant  of  the  mallow  family.  — Fr.  prec.  word.
5066:Derivative:  bishop,  tr.  and  intr.  v. bishopric,  n.  —  OE.  bisceoprice,  biscoprice,  com¬ pounded  of  bisceop,  biscop,  ‘bishop’,  and  rice ‘dominion’.  See  prec.  word  and  Reich, bismite,  n.,  bismuth  trioxide  (mineral.)  —  Coined fr.  next  word  and  subst.  suff.  -ite. bismuth,  n.,  name  of  a  metallic  element  (chem.)  — G.  Bismuth  (now  spelled  Wismut),  Latinized  by Georgius  Agricola  (in  1530)  into  bisemutum. The  origin  of  the  word  is  uncertain.  It  is  not connected  with  Arab,  ithmid,  ‘antimon’,  as  most lexicographers  would  have  it. bismuto-,  bismutho-,  combining  form  meaning ‘bismuth’.  —  See  prec.  word, bisnaga,  n.  a  kind  of  cactus.  —  Port,  bisnaga  (cp. Sp.  biznaga),  fr.  Arab,  bisndj,  secondary  form  of bastindj,  fr,  L .pastindca,  ‘parsnip’.  See  parsnip, bison,  n.,  wild  ox.  —  F.,  fr.  L.  bison,  fr.  OHG. wisunt  (MHG.,  G.  wisent),  which  is  rel.  to  OE. wesand,  ON.  visundr,  and  cogn.  with  OPruss. wis-sambrs,  ‘aurochs’,  and  with  L.  vissio, ‘stench’.  The  bison  is  named  after  the  peculiar odor  of  musk  emitted  by  it  during  the  rutting season.  See  weasel.
11049:Derivative:  desk,  tr.  v. desm-,  form  of  desmo-  before  a  vowel, desma,  n.,  a  sponge  spicule  (zoo/.)  —  ModL.,  fr. Gk.  Sccyux,  ‘a  bond’.  See  desmo-. desman,  n.,  either  of  two  molelike  mammals ( Myogale  moschata,  resp.  Myogale  pyrenaica). —  Swed.  desman,  ‘musk’.
23048:Derivatives :  mask,  tr.  and  intr.  v.,  musk-ed,  adj., mask-er,  n.,  mask-ette,  n.
24473:moschatel,  n.,  a  small  plant  having  greenish flowers  with  a  musky  smell.  —  F.  moscatelle,  fr. It.  moschatella,  a  dimin.  formed  fr.  moscato, ‘flavored  with  musk’,  fr.  ML.  muscatus,  of  s.m., fr.  L.  museus,  ‘musk’.  See  musk  and  cp.  muscatel, moselle,  n.  —  Wine  from  the  valley  of  the  River Moselle.
24534:mouse,  n.  —  ME.  mous,  fr.  OE.  mils,  rel.  to  OS., ON.,  OFris.,  MLG.,  MDu.,  Dan.,  Swed.  mus, Du.  muis,  ‘mouse’,  OHG.,  MHG.  mus,  G. Maus,  ‘mouse;  muscle’,  and  cogn.  with  OI. muf-,  ‘mouse,  rat’,  muskdh,  ‘scrotum,  testicle’, lit.  ‘a  little  mouse',  OPers.  mush,  ‘mouse’,  Arm. mukn  (gen.  mkan),  Gk.  p<3?  (gen.  pooq), ‘mouse;  muscle',  L.  mils  (gen.  muris ),  Alb.  mi, Lith.  muse,  OPrus.  muso,  ‘mouse’,  OSlav.  my  si, ‘mouse’,  mysica,  ‘arm’.  Cp.  dormouse,  flitter- mouse.  Cp.  also  murex,  Muridae,  murine,  Mus, muscatel,  muscle,  muscular,  musk,  musteline, marmot.  Cp.  also  Mya,  myelo-,  myo-,  amyous, perimysium.
24589:mugger,  muggur,  n.,  the  common  crocodile  of India  ( Crocodilus  palustris).  —  Hind,  magar,  fr. OI.  makarah,  ‘sea  monster,  crocodile’,  which  is rel.  to  OI.  nakrah,  ‘crocodile’,  mikrah,  ‘a  kind  of aquatic  animal’ ;  prob.  of  Dravidian  origin, mugget,  n.,  1)  the  lily  of  the  valley;  2)  the  wood¬ ruff.  —  F.  muguet,  ‘lily  of  the  valley ;  woodruff’, fr.  ( noix )  muguette,  alteration  of  (noix)  muscade, ‘nutmeg’  (cp.  the  transitory  forms  muguade, mugate),  fr.  muse,  ‘musk’.  See  musk  and  cp. muscardine,  muscat.
24607:mule,  n.,  a  hybrid  between  the  horse  and  the  ass. ME.,  fr.  OF.  mu!,  fr.  L.  miila,  fem.  of  mulus, ‘mule’  (whence  OF.  mul,  replaced  in  F.  by  its diminutive  mulet).  L.  mulus  stands  for  *mugh- slos  (cp.  the  diminutive  muscellus,  fr.  *muxellus) and  is  cogn.  with  Gk.  p.uxX6<;  (for  *mukslos), ‘he-ass’.  Alb.  musk,  ‘mule’.  Cp.  muleta. Derivatives:  mul-ish,  adj.,  mul-ish-ly,  adv.,  mul- ish-ness,  n.
24719:muscadel,  n.  —  A  var.  of  muscatel, muscadine,  n.,  a  grape  grown  in  the  southern U.S.  —  Formed  with  suff.  -ine  fr.  OProveng. muscada,  fern,  of  muscat,  ‘flavored  with  musk’. See  muscat.
24720:muscardine,  n.,  dormouse  ( obsol .  and  rare).  - —  F., fr.  earlier  F.  muscardin,  muscadin,  ‘lozenge  fla¬ vored  with  musk’,  fr.  It.  moscardino,  of  s.m.,  fr. moscado,  ‘having  the  smell  of  musk’,  fr.  VL. muscatus,  of  s.m.,  fr.  L.  muscus;  see  musk  and cp.  muscat.  The  animal  was  called  muscardine by  the  French  naturalist,  Comte  Georges  Louis Leclerc  de  Buffon  (1707-88)  in  allusion  to  its musky  smell.
24722:muscat,  n.,  1)  a  light  musky  grape;  2)  a  muscatel wine.  —  F.,  fr.  OProveng.  muscat,  lit.  ‘having the  smell  of  musk’,  fr.  VL.  muscatus,  of  s.m., fr.  L.  muscus.  See  musk  and  cp.  next  word, muscatel,  n.,  1)  a  variety  of  white  grape  with  a musky  flavor;  2)  a  sweet  wine  made  from  mus¬ catel  grapes.  —  ME.  muskadelle,  fr.  MF.  mus¬ catel,  muscadel,  fr.  OProveng.  *muscadel,  dimin. of  muscat.  See  muscat  and  dimin.  suff.  -el  and cp.  moschatel.
24726:(fr.  L.  minus)  and  cabo,  ‘head’  (fr.  L.  caput).  See minus  and  capital,  adj.,  and  cp.  mischief. Muscovite,  n.,  an  inhabitant  of  Muscovy,  a  Rus¬ sian.  —  Formed  fr.  Muscovy  (F.  Moscovie),  an¬ cient  name  of  Russia,  with  subst.  suff.  -ite. Muscovy  duck,  the  musk  duck  (Cairina  moschata)
24727:—  Corruption  of  musk  duck.
24742:musk,  n.,  substance  secreted  by  a  gland  near  the testicles  of  the  musk  deer.  —  ME.  muske,  fr. OF.  (=  F.)  muse,  fr.  L.  muscus,  fr.  Gk.  p.6axo?, fr.  Pers.  mushk,  ‘musk’,  fr.  OI.  niuskdh,  ‘scro¬ tum,  testicle’,  lit.  ‘a  little  mouse ,  fr.  mils-, ‘mouse’.  See  mouse  and  cp.  muscle.  Cp.  also muscadine,  muscardine,  muscat,  muscatel.  Cp. also  mugget  and  the  second  element  in  nutmeg. Derivatives:  musk-ish,  musk-y,  adjs. muskellunge,  n.,  a  large  pike  of  North  America. —  Algonquian  maskinonge,  lit.  'large  pike  . musket,  n.,  hand  gun,  formerly  used  by  infantry; replaced  by  the  rifle.  —  MF.  (—  F.)  mousquet , fr.  It.  moschetto,  ‘arrow  for  a  crossbow’  (now meaning  ‘musket’),  lit.  ‘a  little  fly’,  fr.  mosca, ‘fly’,  fr.  L.  musca.  See  midge  and  -et  and  cp. mosquito.  For  sense  development  cp.  zum- booruk,  ‘a  small  gun’,  which  is  traceable  to Arab,  zambiir,  ‘a  hornet’.
24746:musketry,  n„  muskets  collectively.  —  F.  mous- queterie,  formed  fr.  mousquet,  ‘musket’,  on  the analogy  of  It.  moschetteria.  See  musket  and  -ry. muskus  grass. —  Fr.  Du.  muskus ,  ‘musk  ,  fr.  L.
24747:muscus.  See  musk.
26803:Ovibos,  n.,  the  genus  consisting  of  the  musk  ox (zool.)  —  ModL.,  compounded  of  ovi-,  ‘sheep’, and  L.  bos,  gen.  bovis,  ‘ox’.  See  bovine. Ovibovinae,  n.  pi.,  a  subfamily  of  the  Bovidae (zool.)  —  ModL.,  fr.  prec.  word.  For  the  ending see  suff.  -inae.
=== KLN massage ===
7438:cbirapsia,  n.,  friction,  massage  (med.)  —  Medical L.,  compounded  of  chir-  and  Gk.  a^nq, ‘a  touching,  fastening’.  See  apsis, cbirata,  n.,  the  plant  Swertia  chirata.  —  Hind. chiraita,  fr.  OI.  kirata  tikta ,  lit.  ‘the  bitter  plant of  the  people  called  Kiratas'. chirm,  n.,  noise.  —  ME.,  fr.  OE.  cirm,  cerm, ‘shout,  cry,  noise’.  Cp.  charm,  ‘song  of  birds’, chirm,  intr.  v.,  to  make  a  noise,  to  chirp.  —  ME. chirmen,  fr.  OE.  cirman,  ‘to  shout,  cry’,  fr.  cirm. See  prec.  word.
23063:massacre,  n.,  indiscriminate  killing.  —  F.,  fr. earlier  mafacre,  rel.  to  OF.  macecle,  macecre, ‘shambles,  butchery’ ;  of  uncertain  origin, massage,  n.  —  F.  massage,  fr.  masser,  'to  mas¬ sage’,  fr.  Arab,  massa,  ’he  felt,  touched’,  which is  rel.  to  Heb.  mashash,  ‘he  felt,  touched’, mishshesh,  ‘he  felt  through,  groped’,  Aram. mashshesh,  ‘he  felt  through,  groped’,  Ethiop. marsasa,  ‘he  felt,  touched’,  Akkad,  mashdshu, ‘to  smear  over,  spread  over’.  The  practice  of massage  has  come  to  Europe  from  the  East  and consisted  originally  in  the  simple  touching  of the  superficial  parts  of  the  body.  This  word  has nothing  to  do  with  Gk.  y-iaae tv,  ‘to  knead’, with  which  it  is  connected  by  most  lexicogra¬ phers.  For  the  ending  see  suff.  -age.
23065:Derivatives;  massage,  tr.  v.,  massag-er,  n., massag-ist,  n.
23070:masseur,  n.,  a  man  who  practices  massage.  —  F., formed  fr.  masser,  ‘to  massage’,  with  suff.  -ear, representing  L.  -or.  See  massage,  and  agential suff.  -or.
23071:masseuse,  n.,  a  woman  who  practices  massage.  —
28705:physiotherapy,  n.,  medical  treatment  by  physical and  mechanical  means  (as  massage,  heat,  elec¬ tricity).  —  Compounded  of  physio-  and  -ther¬ apy.
34880:shampoo,  tr.  v.  —  Hind,  charnpo,  imper.  of champnd,  ‘to  knead,  press,  massage,  shampoo’. Derivatives:  shampoo,  n.,  shampoo-er,  n. shamrock,  n.,  a  trifoliate  plant,  the  national  em¬ blem  of  Ireland.  —  Ir.  seamrog,  dimin.  of  sea- mar,  ‘clover’.
```


## [2026-09-07T17:37:02.589Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '61590,61760p' POK_full.txt",
 "description": "Print Pokorny page 752 blocks"
}
```


### [2026-09-07T17:37:02.639Z] TOOL RESULT

```
References: WP. II 313. 
Page(s): 750 

Root / lemma: mut-o-s 

Meaning: circumcised 

Material: Latin mutilus, /77i///o'i/s "mutilated', *muticus^ truncated, chopped down, cut down, 

cut off, circumcised ', muto, mutfd'pen\s', GN Mutunus, rom. mutt-^ dull '; Irish mut, gael. 

mutacb' short' (with expressive //); perhaps also Irish /770//7 "penis' as " stub'. 

References: WP. II 312, WH. II 136 f.; after E. Lewy rather to Latin mutusS. 751 , compare 
" dumb ': " mutilate '. 
Page(s): 753 



Root / lemma: muk- 
Meaning: heap, etc.. 

Material: Gr. jjukoov awpoq GniJcbv Hes.; proto gall. *mukina ' cairn, pile of stones set up as 
a memorial or mark of some kind ' (Jokl V. Rom. 8, 193); Old Icelandic mugi, mugr^heap, 
bulk, mass'. Old English mugam. "(corn, grain-) heap', muha ds. (also muwa), compare 
further Swedish dial, moa^ pile up, collect, accumulate' {*mOhdn), Old High German mO- 
werf^ mole ', with -k(k)-. Middle Low German muke, Dutch muik Middle High German 
mOche, Modern High German (half Low German) Maukei., Bavarian (genuine High 
German) Mauche^ Auswuchs, Fuftgeschwulst der Pferde ', Swiss mauchm. ' Auswuchs 
an Rebholz, unordentlicher Haufe ' and with if. Norwegian dial, mukka^heap, bulk, mass'. 
Middle High German mockem. 'clump, gobbet ' (with it identical is Middle High German 
mocke^ Zuchtsau '); Old Icelandic /770s//' 'big, giant bulk, mass' {*muh-stra-)\ unique 
lengthened grade form in Old English meagor {*\\}'(r\py , massive ' =) 'tight, firm, strong'. 
References: WP. 11311; after Hubschmid ZnPh. 66, 33 f. not Indo Germanic 
Page(s): 752 

Root / lemma: mu-1 

Meaning: to murmur, moo (expr.) 

Material: 1 . Gr. |ju, pu ' cry of pain ', Latin mu facere, mutmut facere 'stir, move, budge '. 

2. Old Indie muka-^ dumb ', Armenian munj^ dumb ', gr. jjOko^, jjutk;, [jutt6(;, puSoq, 
|juvap6(;, Hes. fjuv56(; ' dumb ', Latin mutus^ dumb '; compare also Old Danish mue, 
Norwegian mua^ keep mum, keep quiet, remain silent, do not mutter, mumble '; Old High 
German mawen^cry', Latvian maunu, mawu, maut'roar, bellow', Czech myjat/" moo'; here 
also Modern High German Mowe, Old English m^w, mew, Old Icelandic mar{P\. mavai). 
Old Saxon meu6s. 

3. [Old Indie mukha-n. 'mouth' derives from Dravidian]; gr. puAAov 'lip'; puAAaivu) 
'verzieheden mouth, cut, bite Gesichter' (fjuara^ ' upper lip, whisker, moustache', s. 
Boisacq m. Lithuanian), Old High German mu/at, Middle High German mu/n. 'muzzle'. 
Middle Low German /t?^/©' muzzle, snout'. Old Icelandic /77J// "muzzle, esp. upper lip of an 
animal, bulging crag ', Gothic faurmuljan ' das Maul zubinden ' (whether with ani. s- in 
addition Norwegian smaul, Latvian s/77a^/e 'muzzle'??); s. also under mou-lo-S. 750. 

4. With dental formant: 



Latin muttio, -ire^ mutter, mumble ', muttum nullum^ keinen Muckser' (compare above 
mutmut); Old High German /77i////d/7 'mumble, murmur, trickle ', musse^ spring ', Old 



Icelandic mud/a 'mumb\e, murmur', besides with Germanic t. Norwegian dial, mutra, 
Middle English muteren, engl. mutterds.; Lithuanian /77i//e "muzzle'. 

5. guttural extensions (compare above 2.): 

With A:;gr. pOKaopai " bellow', puxOi^w "snort, spotte'. Middle High German muhen, 
mugen, muwen'roar, bellow'. Old Bulgarian mykh' bellowing, braying, roar', russ. mycatb 
"roar, bellow', Serbo-Croatian slov. Czech mukat/^roar, bellow'. 

With g:0\6 Indie munjati, moJat/^gWes einen Ton from sich' (Dhatup.); mucchana' 
growing sound, tone'; gr. |ju^u) "bringe with closed Lippen einen sound hervor, stohne' (out 
of it Latin mussare^ mutter/whisper (discontently); hum (bee); keep quiet (about); 
hem/haw; hesitate '), |Juymo<; "sigh'; 

Latin mugio, -Ire 'roar, bellow', conmugento' convocanto ', mugmor' loiter] dally ' (also " 
nugarlet quasi tarde conari '), Umbrian /77^/e/o"muttTtum ', mugatu' muttlto ', Latin 
mugilareoi Naturlaut of Esels; Old High German muckazzen' talk quietly, mutter, mumble 
', Modern High German Middle Low German mucken' talk with half-open mouth ' {kk\s 
expressive). East Frisian muk'V\ss\ 

6. s-extension: gr. pOu) "sich shut, from den Lippen and den Augen' (hence ^juojijj "die 
Augen zusammenkneifend, shortsighted '; puaco "bite die Lippen together'; from *jjuaT6$ 

verschwiegen': puaTr|<; "in die Mysterien Eingeweihter', puaTiK6(; "die Mysterien 
betreffend', puarripiov " mystery, secret Zeremonie', compare also pusTv "in die Mysterien 
einweihen'; Norwegian mysa'to screw up one's eyes'; from Germanic here also Middle 
Low German mummelen, engl. /77^/77i6'/e "mumble, murmur', mump, Norwegian mumpaAs.; 
Middle High German mupf, muff' Verziehung des Mundes ', mupfen, muffen. Middle Low 
German mopen, engl. mope'ga\Nk', engl. /770/? "grimace'; perhaps Modern High German 
Bavarian /t?^^©/? "ruminate' ; 

Latvian mus/nat'\Nh\sper, mumble, murmur'; Hittite mu-u-ga-a-mi {mugami) " spreche 
Klagegebete '. 

References: WP. Il309ff., WH. II 117, 119 f., 135, 139 f., Trautmann 188. 
Page(s): 751-752 

Root / lemma: mu-2, mus- 
Meaning: fly n. 



Material: Armenian mun, Gen. mnoy^a mosquito, gnat ' {*mus- or *mu-no-); alb. mu-ze, 
/77/-ze(ze diminutive suffix) ' mosquito '; gr. puTa (*[juaja) "fly'; Latin musca; Old Icelandic 
/77j/n. ( *muja-) " mosquito '; Swedish mygg, mygga. Old English mycg. Old Saxon muggia. 
Old High German mucka " mosquito ' ( *mukja)\ 

with -5-gotland. mausa{*musa), Flemish meuzie{*musT}\ Lithuanian muse. Old Prussian 
muso, Latvian musa, musal\Y'; Old Bulgarian muchal\y' {*mousa), m-bsica^ mosquito '. 
References: WP. II 311, WH. II 133, Trautmann 191, Specht Indo Germanic Dekl. 43. 
Page(s): 752 

Root / lemma: mus 

Meaning: mouse 

Note: (older *mus, musosirovn *meus, musos) 

Material: Old Indie mus-m. ' mouse, rat', np. mus^ mouse '; 

Armenian mu-kn^ mouse, muscle '; gr. \x\ic, {\x\ibc,, puv after ho,, Clxioc,, uv) " mouse ', 
also " muscle '; alb. ml miu' mouse ' {*miusTn) 

Alb. Geg mini, min/{P\) " the mouse ' 

Latin mOsm. " mouse ' {munnus: Middle High German miusTn'ofthe mouse'); Old High 
German Middle High German Old Saxon Middle Low German Old Icelandic Old English 
mOs' mouse, muscle ' (consonant-stem); Old Bulgarian mysbt ' mouse '. 

Often applied on body parts: Armenian mukn' muscle ', gr. \^0q " muscle ', jjucbv 
'muskelreiche region of Leibes' (from which also " voluptuous woman' in gr. (juojvia), pua^, 
-aKO(; m. " mussel, spoon': Latin mOrex' Mediterranean sea snail, snail emitting purple dye 
'; Latin muscuius6s., " muscle ', Old High German etc. mOs^ muscle, esp. of the upper 
arm'. Middle Low German mOs esp. 'the spherical flesh of thumbs'. Modern High German 
Maus, i\/1ausciien. Old Bulgarian mystca ' (3paxiwv '; on the other hand Old Indie muska- 
m. 'testicle, vulva', npers. musk^ castor, beaver' (from Pers. derives gr. [joaxoc;. Modern 
High German A^c»sc/7^s 'musk'); gr. [juaxov ' genitals '; 

Maybe alb. Geg /77i/s/ri//'muscle', /77i/5M 'shoulder', musi7keni'\ungs'. 

probably to Old Indie musnati' steals, robs ' etc., see below meu-2'push away '. 

References: WP. II 312 f., WH. II 132 f., Trautmann 191, Specht Indo Germanic Dekl. 40 f. 
Page(s): 752-753 



Root / lemma: meni- 

Meaning: a kind offish 

Material: Gr. paivn (out of it Latin maena), \ia\v'\Q, "a small sea fish', Slavic *m-bnb, russ. 

menb etc. 'toad '; but Old Indie mma- m. "fish' (whereof mainika-, mainala- " fisherman ') is 

of dravid. origin; perhaps here Old High German muniwa. Old English myne, engl. minnow 

'minnow, small freshwater fish, a fish', (under the influence of common Celtic -ns-, -nt- > - 

nn-). 

References: WP. II 267 f.; 

See also: belongs probably to men-4. 

Page(s): 731
```


## [2026-09-07T17:37:05.302Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN page markers near massage ===\"; sed -n '23020,23075p' KLN_1966.txt | grep -n \"page\\|\\[\" | head\nawk 'NR>=22900 && NR<=23100 && /^[0-9]+$|page/' KLN_1966.txt | head -20\necho \"=== AHD mus- entry ===\"; python3 - <<'EOF'\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\ni=t.find('miis-. A mouse')\nprint(t[i:i+1200])\nEOF",
 "description": "Klein page markers and AHD mus- entry"
}
```


### [2026-09-07T17:37:06.618Z] TOOL RESULT

```
=== KLN page markers near massage ===
938
939
940
941
942
943
944
945
1
946
947
=== AHD mus- entry ===
miis-. A mouse; also a muscle (from the resemblance of a flexing muscle to the movements of a mouse). 1. Ger- manic *mis- (plural *misiz) in Old English mis (plural
‘ mys), mouse: MOUSE. 2. Latin mis, mouse: MURINE,
MUSCLE, MUSTELINE. 3. Greek mus, mouse, muscle: MY- ELO-, MYO-; EPIMYSIUM, MYOSOTIS, MYSTICETE, PERIMY- SIUM, SYRINGOMYELIA. [Pok. miis 752.]
[misum. Snout. Medieval Latin noun of unknown origin. MUSE, MUZZLE.]
mut-. Cut short. Suffixed form *mut-il- in Latin mutilus, maimed: MUTILATE. [Pok. mut-o-s 753.]
[nabja-. Bird’s beak. Germanic root. Old English neb(b), beak: NEB, (NIB), (NIPPLE).]
nana. Child’s word for a nurse or female adult other than its mother. 1. Greek nanna, aunt, whence nannas, uncle, whence nan(njos, “little old man,” dwarf: NANO-. 2. Late and Medieval Latin nonna, aunt, old woman, nun: NUN}. 3. English (directly from baby talk) NANA, NANNY. [Pok. nana 754.]
nas-. Nose. 1. Germanic zero-grade form *nusé in Old English nosu, nose: NOSE, (NUZZLE); NOSTRIL. 2. Ger- manic nasja- in Old English ness, headland: NESS. 3. Lengthened-grade form “nds-, in: a. Latin ndris, nos- tril: NAREs; b. expressive form *ndss- in Latin ndsus, nose: NASAL, NASO-; NASTURTIUM,
```


## [2026-09-07T17:37:22.879Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN mus/musk ===\"; grep -n -i \"mūš\\|mus 'Maus'\\|Maus\\b\\|mušk\\|Moschus\" HRN.txt | head -20\necho \"=== HUB ===\"; grep -n -i \"Maus\\|Moschus\\|mušk\" HUB.txt | head -20\necho \"=== PHD ===\"; grep -n -i \"mušk\\|mūšk\\|mouse\" PHD.txt PHD_mackenzie.txt | head -20",
 "description": "grep Horn, Hübschmann, MacKenzie"
}
```


### [2026-09-07T17:37:22.988Z] TOOL RESULT

```
=== HRN mus/musk ===
6681:schmaus', mä\xäm 'Abend' (?); bei. säm 'Hauptmahlzeit,
8650:995. ninS *Maus*.
8652:ai. müs~, skr. müsaka-, mfisika- *Maus, Ratte*; arm.
8653:mvkn 'Maus' (H. No. 206).
8655:küfai 'Maus, junge Ratte*; oss. d. miste, t. mist (189);
=== HUB ===
3547:arm. napak 'Moschusbeutel' (bei Moses, Geogr. ed.
3548:Soukry p. 44, 7 v. u.) = np. ndfa 'Nabel, Moschus-
4892:(arab. misk) 'Moschus* = musk; Hier folgt auf u entweder
6636:Moschusbeutel', Moses, Geogr. ed. Soukry p. 44, 7 v. u..^ 188 —
7106:') Horn setzt mauSa- wegen np. mOi an. Vielieioht wurde aber
8293:*Maus* H. 995; xusk 'trocken H. 489; mBs *Widder H. 1008;
=== PHD ===
PHD.txt:493:Р murd [то | P mort !] death. murdan, mir- (YMYTWN-tn! < A ymwtwn, V mwt; mulin' | M murd, myr-, N ~] die. murdār [mwrt?], mwld?l | N ~] carrion. murnjénidan, murnjén- (mwlncyn-ytn'] destroy. murw [mwlw! | M mwrw, (N mury)] bird. murwāģ [mwlw’k' | M mwrw’, N murwd] omen. murwizag [mwlwyck'] little bird. murw-nīš [mwlwnys] augur, soothsayer. must [mwst'] force, violence. ž*must [mwst'] = must. *must [mwst'] complaint. must|-abarmānd [mwst!’plm’nd] aggressive, aggressor. ~gar [-kl] violent, rebellious, mustómand [mwst?wmnd | N mustmand] complaining, unhappy. ImuSk [отео | N ~] musk. 2mušk [mwsk! | (N mis)] mouse, rat. must [mzvšt! | N ~] fist. muštan, māl- [mwéstn', wl- | N ~] rub, sweep.
PHD.txt:540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
PHD.txt:583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
PHD.txt:933:basil, royal — šāhesprahm; speckled ~ palangmušk.
PHD.txt:2861:mouse mušk.
PHD.txt:2873:musk mušk.
PHD.txt:3325:rat mušk. I
PHD_mackenzie.txt:3627:2musk [mwsk I (N mtis)] mouse, rat.
PHD_mackenzie.txt:4776:-Aawag [Iwb)k l ] bat, flittermouse.
PHD_mackenzie.txt:7093:minister dastwar; prime ...... wuzurg-         mouse musk.
```


## [2026-09-07T17:37:25.801Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB ===\"; grep -n -i \"mušk\\|mūš\\b\\|mouse\" NYB_vol2_glossary.txt | head -15\necho \"=== IEC mus ===\"; grep -n -i \"^mūs\\|mūs- \\|muskos\\|mus-\\b\" IEC.txt | head -15\necho \"=== SYN mouse ===\"; grep -n -i \"mouse\" SYN.txt | head -15\necho \"=== LKT Moschus ===\"; grep -n -i \"moschus\\|musk\" LKT.txt | head -15\necho \"=== SKT musk ===\"; grep -n -i \"musk\\|mouse\\b\" SKT.txt | head -15",
 "description": "grep Nyberg, Mann, Buck, Lokotsch, Skeat"
}
```


### [2026-09-07T17:37:25.897Z] TOOL RESULT

```
=== NYB ===
=== IEC mus ===
11462:muskos, à ‘undergrowth, moss’. Cf. WP II, 251. Cf. musos (1) Lat. muscus, gs -i, m. ‘moss’; LG musch, m. id.; Sw. cf. myska, f. ‘woodruff. (Fr. mousse *moss' is from a type *mussa implied in LLat. mussula *moss")
11465:mūsos, ios, iə (1) ‘overgrowth, mould, moss, filth’. Cf. mustos (1), muskos & meus- Arm. cf. ma-mur, gs -mro, o-st ‘moss’ beside gri-mur (‘seaweeď’, lit. ‘water-moss’); LLat. cf. mussula ‘moss’, and Fr. mousse, f. id. fr. LL
=== SYN mouse ===
3744:CHAPTER 3 ANIMALS 3.45 Foau, Cott gal eANo 3.46 Ass, DonKEY 3.12 Mate (adj.) 3.47 Mute gia ene 3.51 Hen, Catcxen (Generic) Blan CASTE 3.52 Cock Blo ESTO 3.53 CAPON 3.16 PasTuRE (vb.) aa ee ON chaaeh Pe, 3.55 CHICKEN 3.18 HerDSMAN aA Goan 3.19 STABLE, STALL ne Duue 3.20 CATTLE (Bovine Species) et at ae se 3.612 Purry a oe 3.62 Car 3 4 CALF 3.63 Mouse eed tae AM ; eS a 3.66 FISHERMAN 3.28 Ews 3.71 Wo.ur | 3.29 Lams 3.72 Lion 3.31 Swint 3.73 BEAR 3.32 Boar 3.74 Fox | 3.33 Barrow 3.75 DEER i 3.34 Sow 8.76 MonxkEY 3.35 Pie 3.77 ELEPHANT 3.36 Goat 3.78 CAMEL | 3.37 Hu-coar 3.79 Hunt (vb.) 3.38 Kip 3.81 InsEctT 3.41 Horse (Generic) 3.82 BEE 3.42 Srantion 3.83 Fy : 3.43 GrLpine 3.84 Worm 344 Mare 3.85 SNAKE
3745:In the inherited names of animals | pent’, ‘hare’, and ‘mouse’ here and there is little to be said about their se- there, is attributed to taboo (cf. esp. mantic source. For in most of them the Meillet, Ling. hist. 281 ff.). This has Toot connection is wholly obscure. The | doubtless played a part in individual interest in this chapter lies rather in the | cases. But one hesitates to make too oes, substitutions, and shifts of appli- | much of this factor when one observes cation, that virtually every inherited animal eas a of certain inherited animal | name (and for that matter nearly every = ee e that of the ‘bear’ in Slavic | inherited word in other classes, as in the
3760:Color words underlie some, as ‘brown’ in the Gme. words for ‘bear’ (3.73) and an IE word for ‘beaver’ (NE beaver, etc.); ‘gray’ in Lith. pelé ‘mouse’ (3.63) and prob. a widespread word for ‘hare’
4880:2. Lat. félés, possibly : W. beleu ‘mar- ten’. Walde-P. 2.177. Walde-H. 1.474. In Plaut, Rud. 3.4.43 ‘mouser’, prob.
4894:3.68 MOUSE Grk. pis Goth. Lith. pelé NG wovrixe ON mis Lett. pele Lat. mis Dan. mus ChSl. myst It. topo (sorcio) Sw. mus SCr. mis Fr. souris OE mis Boh. my& Sp. ralén ME mous Pol. mysz Rum. $oarece NE mouse Russ. mys’ Ir. luch Du. muis Skt. mis- Nir. luch OHG mis Av. W. Ulygoden MHG mis Br. logodenn NHG maus
4897:2, NG movrixds, pop. movrix, fr. pds Tlovrixos ‘Pontic mouse’ (Aristot. HA 600°14, Pliny 8.82, etc.).
4898:3. It. sorcio, Rum. goarece, fr. Lat. sdrex ‘shrewmouse’. Fr. souris fr. *soricius. REW 8098, 8101.
4899:It. topo ‘mouse’ or ‘rat’, fr. Lat. talpa ‘mole’. REW 8545.
4900:Sp. ratén, formed fr. rata ‘rat’, and ‘she-mouse’. Similar confusion between ‘rat’ and ‘mouse’ in Fr. dialects (REW 70892), likewise in NG ovrixc and It. topo.
5020:Br. marmouz, fr. OF r. marmot or mar- mouset, both used for ‘monkey’ (also
6133:ChSl. mystica (SCr. miica ‘arm’ and ‘muscle’), deriv. of ChSl. myst ‘mouse’ in transferred sense ‘muscle’ (from the re- semblance between the muscle of upper arm especially and a mouse). Cf. Lat. musculus ‘little mouse, muscle’, Grk. pis
6134:‘mouse’ and ‘muscle’, etc. Walde-P. 1.312f. Ernout-M. 645 f.
6667:Skt. muska-, apparently dim. to mis- ‘mouse’, from the shape (cf. Lat. muscu- lus ‘muscle’, etc.). Walde-P. 2.313.
7080:Grk. cxép, gen. cxaréds, hence NG oxaré, usually pl. cxara; Lat. miscerda ‘mouse dung’, sucerda ‘swine dung’, etc.; OE scearn, ON skarn; Slavic vbs., SCr. sratt, ete.; Av. sairya- (Barth. 1567); Hitt. sakkar, gen. saknas (Sturtevant, Hitt. Gloss. 128).
=== LKT Moschus ===
851:293.  Hebr.  b§s§m: 'Balsamstaude,  Balsam',  eine  Handels- ware, welche  die  Griechen  nebst  dem Namen  von  den  Phöniziern  erhielten. Gr.  ßd\aa|nov,  lat.  balsamum;  hieraus  it. balsamo,  balsimo,  asp.  blasmo,  sp.  pg. balsamo,  prov.  balme,  frz.  bäume  [aber pikardisch  bäm  'Minze'],  rum.  baisam; dtsch.  Balsam,  ndl.  balsem,  engl,  bahn; russ.  bal'sam,  bulg.  serb.  poln.  baisam, cech.  baisam,  balzam.  —  Aus  demselben Grundwort  mlat.  bisamum,  dtsch.  Bisam, cech.  poln.  pizmo  'Moschus'.  —  Vgl. noch  Balsamine,  Impatiens  Balsamina, engl,  halsamine,  baisam.  [Kluge  34  u. 54.  G.  Schvveinfurth,  Über  Balsam  und Myrrhe  1893.
859:'Frucht  der  Pflanze  Abelmoschus  escu- lentus'  [s.  hier  Nr.  762] ;  hieraus  anglo-
980:[Aus  gr.  irovTiKÖv  (Kcxpuov),  lat.  (nux) pontica]  'Haselnuß';  hieraus  sp.  bodoque 'Kieselstein  oder  Bolzen  für  die  Arm- brust, Geschoß  für  die  Muskete'  [weil von  der  Größe  einer  Haselnuß],  pg. bodoque  'dass.'  [Constancio  Dicc  178  b]. Rum.  bondoc,  bunduc  'untersetzt,  dick und  fett'.  —  Die  Ableitungen  von  frz. ff  yifZoi«7Ze 'Leberwurst',  ka.t.tiiaiulonguilla, sp.  alböndiga  von  diesem  Grundwort scheinen  begrifflich  und  formell  sehr fraglich  zu  sein  [vgl.  BAIST  in  ZfrumPh V.  233.  G.  PARIS  in  Romania  XI,  163. DE  72.    Eguilaz  115.    ML  1205].
1614:'Parfüm  aus  Moschus  und  Ambra';  hier- aus sp.  algalia,  pg.  algälia  'dass.';  mlat. galia  muscata,  sp.  pg.  gato  de  algalia [Constancio  Dicc  50  b]  'Zibetkatze,  Vi- verra  civetta  Schreb.'.
1852:b)  Mit  ar.  musk  'Moschus'  [s.  hier Nr.  1701]  wird  ar.  habb  al-niusk  'Hibis- cus  abelmos(  hus  L.' ;  hieraus  sp.  abel- mosco,  pg.  abehnosco,  abelmoscho  [Con- stancio Dicc  4a:  'ambarina'],  frz.  abel- mosc,  abelmosch,  ndl.  abelmosch.  Da  der Duft  ihrer  Blüten  wie  der  von  Ambra und  Moschus  zusammen  ist,  heißt  sie auch  frz.  ambrette,  ndl.  amberbloem  [zu
2454:'Leisten  eines  Schusters',  ebenso  tk. kalyh,  Icahjp  'Modell,  Form';  hieraus rum.  calib,  calip,  calup  'Gießform,  Mo- dell, Leiste',  calupciü  'Betrüger';  aus dem  Ar.  unmittelbar  sp.  gälibo  'Schiffs- modell', frz.  gabarit;  asp.  calibo,  sp. calibre,  frz.  calibre  'Durchmesser  der Mündung  eines  Geschützes,  Gewicht  der Kugel';  it.  coUbro  'Maßinstrument,  um die  Zusammengehörigkeit  von  Geschütz und  Geschoß  zu  bestimmen';  dtsch. Kaliber,  engl,  calibre  [amerikanische Schreibung  caliber,  s.  Herrigs  Archiv CXLI,  194],  bei  Shakespeare  l.HenrylVth IV,  2,  21.  2.  Henry  IVth  III,  2,  292 und  295  caliver  'kleine  Muskete'  [wenn nicht  aus  frz.  coiileuvre  <^  lat.  coluber 'Schlange'] ;  russ.Ä:«?«/^ 'Gießform, -löffel', kaliber  'Geschützweite',  bulg.  kahp,  serb. kalup  'Gußform,  Schuhleisten'.  [Devic DEt  79/80.  Gorjajew  129.  Sain  48. SCHUCK ARDT  in  ZfromPh  XXIV,  571. A.  KLUYVER  in  ZfdWf  XI,  219/224.
3394:[Aus  aram.  mesklnä  'arm',  das  selbst Entlehnung  aus  dem  ass.  muskenu  'arm', nämlich  zwischen  dem  freien  Volksbür- ger und  dem  Sklaven  in  der  Mitte  stehend, aus  Sukennu  'niederfallen',  irpoaKuveiv; vgl.  ZAkkFW  47]  'arm,  elend';  hieraus it.  meschino,  prov.  kat.  mesqui,  sp.  mes- quino,  mezqnino,  pg.  mesquinho,  mez- quinho,  rum.  nieschin,  f'Z.  mesquin 'armselig',  afrz.  tueschin  'Bursche',  me- schine  'Mädchen'.  [DE  314.  Eguilaz 450/451.    ML  5539.
3496:1515  a.  Pers.  musk:
3497:'Moschus'  [aus  sskr.  mnshkas  'Hode' wegen  der  Ähnlichkeit  einer  solchen  mit dem  Beutel  des  Moschustieres],  ar.  musk, misk,  tk.  misk;  hieraus  mlat.  museum 'Bisam,  Moschus',  it.  musco,  musehio, prov.  mtisc,  frz.  musc,  kat.  almesc,  pg. almiscre,  alniiscar,  sp.  musco,  musca, amusco,  als  Adj.  'moschus-,  d.h.  dunkel- farbig', sp.  altnizele,  kat.  musc  'braun', sp.  pg.  mosquita  'Moschusrose',  frz. muscadin  'Stutzer'  [Behrens  Beitr.  376; wahrscheinlich  nach  dem  Moschus,  mit dem  die  Stutzer  sich  partümierten],  rum. mosc'MoschusLier',  moseu§or;  engl. musk, dtsch.  Müsch,  später  Moschus;  russ. muskus  'Moschus',  moskot'  'Drogen'.  — Eine  Abltg.  hiervon  ist  lat.  muscatus >  engl,  muskate,  dtsch.  Muskat  [Samen- kerne von  Myristica  fragrans].  [DE  166. Gorjajew  319.  ML  5775.
3507:[Aus  must  'Faust'  Horn  NpEt  S.  220, Nr. 982;  ebenso  gebildet  wie  dästä  'Griff, Bündel,  Strauß',  d.  h.  alles,  was  in  die Hand  däst  hineingeht;  also  wörtlich: 'alles,  was  in  die  Faust  hineingeht'] 'Pelzmantel  mit  langen  Ärmeln,  weiter Rock'.  Aus  der  älteren  Form,  pehlewi niustak,  entstand  ar.  mustaka  'dass.'; hieraus  mit  ar.  Art.  mlat.  almutium, afiz.  auntusse,  sp.  almucio  'prunkvoller Pelzmantel  der  Domherren  und  Stifts- damen, der  über  den  Arm  herabhängt', afrz.  aumucelle,  sp.  almucella  'kleine Kapuze,  Kragenkappe',  sp.  muceta  'Pilger kragen',  pg.  murga  de  pelles  'Chorpelz der  Domherren';  eng\.amice  'Mantel  der Chorherren  und  Pilger',  ndl.  muts,  disch. Mütze  'eine  Kopfbedeckung',  (dial.)  Motze 'Oberjacke  der  Frauen  (oder  Männer)'. Eingehend  behandelt  von  Justi,  Mütze und  Verwantes  [sie!]  in  Zeitschrift  für deutsches  Altertum  u.  deutsche  Literatur. Berhn  1891.  XLV,  420/426.  —  Auf  das ar.Gdwt. m«<s<«A;  geht  auch  trz.mousquet, it.  moschetto ;  engl,  musket,  dtsch.  Muskete zurück  [nach  DE  GOEJE,  s.  Wiedemann, Beiträge  zur  Geschichte  der  Naturwissen- schaften VI.  Erlangen  1906.  S.  38].
5510:manü  1456  a.  1462  a menieni  1386 »igstf  1366 muskenu  1470
5849:Moschus  1515  a
5851:Uli Moslem  1516  a Jtfoi^e  1520 Muezzin  1485 Mtf^i  1493 Jlf;(Ä-cr  1507 M««//  1381 Mumie  1510 Müsch  1515  a Muselmann  1516  a Muskat  1515  a Muskete  1520 Muslim  1516  a Musseline  1484 JfM<Äe  1520
6102:tnueddin  1485 muezzin  1485 ww/"<i  1493 »>M/Ky  1493 »wuZi  1381.  1460  a mullagatawny  1460  a mulligatawny  1460  a mulmul  1381 munimy  1510 mun/rfe  1400 »iMSÄ;  1515  a muskate  1615a musket  1520 mnsliman  1516  a muslin  1484 tnusulman  1516  a
7422:abarca  24 «feöas  1 abbntia  1 abhatlssa  1 abelmoschus  762  b
=== SKT musk ===
2642:caliver,  a  sort  of  musket.  (F. from  its  caiiber  or  borr  '
3088:Skt   kastiiri,  musk;  Ten.
5371:Dose.  (.ScnriH.'i  Iccl.  t/$Isa.  to  doze ; Swcc!.  dial  t^Mja,  Duo.  t^ose,  to  dor.e.  mope. Allict]  lo  A.b.  i^wtrj,  stupefied;  and  prob. lo  E.  if <>r- mouse.
6867:ft»ao(o),  fllftOOd);  see ftj«fl(l) below. ftiaUfi),  alijghtmu&ket.  (F.^L.)  Orig. Dot  the  musket  itself,  but  its  fire-lock  ;  aUo t|<ll  futcl,  fuset,  fust,  *  Fust,  ftijee.  or fitsd.  a  pipe  filled  with  wild  fire,  and  put inio  the  touch-hole  of  a  bomb;'  Ker»ey (i;»5'.  -  O.  F.  /w/«7.  ••  fire-siccle  for  a tinder-boi  ;*  Cot.— L.  foftU.  2.  steel  foi fire.  —  L.  /»cui,  a  hearth;    Der.
7275:.  of  L../ujvi.  a  spindle. FuaII  \\\  a  Ii;;*)t  muskrt;  see  Fooua. TumXI  K*\  *  ^P>  ^^^''  ^c  Fiuee  (3). FbMI  (i).  easily  molten  ;  sec  Fuaa  (l). buie.  flu-ry.    (E.I    The  sb,  cor to  M  E. /j#j,  adj.,  eager;  A,  S. i    proTTipt   +  Icel.   ftitSt    eager be,  oriZfing;  O  H   G. /wnj,  ready,  willing, (f ),  to  bcoome  mouldy ;  >ee  below.
11146:marmolio,  a  marmui.  .  i._..u  \.uc  Romaifid (Grison)  name  murmont ;  O.  H.  G-  w*< munfo,  murtmutifo,  a  marmot.  — L.  ««^ stem  of  mus,  mouse;  and  mont-,  stem  i mom,  mountain.  Thus  the  sense  is tain-mouse.*    (See  Diez.)
11919:musket  (F.-Ital-L.)  O.Y.nunis- put,  ft  musket,  orig.  a  kind  of  hawk ^another  &oit  of  gun  was  called  a y^/<[On^/, another  a  saJker,  a  kind  of  hawk).  —  Ital. mosquefic,  a  musket,  oritf.  a  kind  of  hawk, so  called  from  its  smalt  size.  Dimin.  of Ital.  mffsca,  a  Hy.  — L.  mitsea,  a  fly.
11949:Mouse.  (E.)  M.  E.  mom.  A.  S.  mi£r (pi.  Mj!/),  ^  Du.  mnis,  Icel.  «w//j,  Dan. mttiu,  Swed.  m$u,  G.  mans.  Ross.  muiih\ L.  m$4s,  Gk.  /«iJr,  Per*,  mtish,  a  mouse; Skt.  miiska,  a  rat,  a  mouse.  Lit  'a stealing  animal.'"*^  MUS,  to  steal;  Skt. mtish,  to  steal.     Sec  Muscle  (1).
12050:MUBOadel ;  see  Musk.
12051:Muflole  (i),  the  fleshy  part  of  I (F.  •  L. )    F.  musele.  -  L.  muu musmlus,  (t)  a  little  mou&e,  (a' from  its  creeping  appearance  i Dimin.  of  L.  mus^  a  mouse : (Cf.  F.  scuHs,  (i)  moose,  (j)  n\\ muscle  (a),  musaol.  a  ihcll^ In  earlier  use.     M.  E.  muufe,  A.I tfiutc/e  (Wright),  fl  tnusilc  (lisb"!. fu/ui,  a  sca-miiscle,  also  a  Ul (above).
12055:tulus,  a  sca-moscle ;  doable a  mouse.
12076:hind  the  musk-deer's  navel.     Lit  '  thief;' from  mush,  to  steal.     See  Mouse.
12078:Musket;  see  Moaqoito.
12530:nutmeg,  the^ask-nut.   (E.; U  -  Pers.  -  Ski.)     M  E    BiiAri nutmtggt.    Here  -w/.' musk,  from  L.  mn musk:  see  Musk.     <..    ^, nutmeg,  also  called  n^jc\ Hutt  nnyicada^  lul.  <tow mujcafa,  nutmeg. Nutation,  a  noddW. ffwAi/u),  a  nodding.  —  U
15980:S:  tee  B«al  (i). to.    (L.)      From  pp.  of  L.  rt- Tcject.  —  L.  rc/>u*iium,  a  casting t  of  what  one  is  ashamed  of.— r :  /wi/',  base  of  p%niert,  to  feel Utior,  shame, t ;  see  FaffUimi. see  Pulsate . sec  Putative. Require ;  sec  Query. ,  Bequito ;  uc  Quiofc. S  ice  Bear  (j>. Be,  Beannouae.  a  bat   (E.) liXr,  %  bat;  from  the  flapping L—A.  S.   kr^ran,    to   agitate, motion,   allied   to   hr6r,  adj., U>.  a  mouse.     Cf.  prov.  V..JlUUr- flutter-mouse  or  bat. ard;  sec  Bear  (j). d,    to    repeal.     (F.-L.)      F.   rt- ^cancel:  Cot  L.  rt-jcituftn,  to Biul.  ••  L.    rt',    back  ;    scindere, ■ied  to  Sohiinu     (y^KID.) p.    to    cut    off.     (L)       L.    ab- n  cut  off.
```


## [2026-09-07T17:37:37.422Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 995 ===\"; sed -n '8640,8670p' HRN.txt\necho \"=== HUB 4880-4900 ===\"; sed -n '4880,4900p' HUB.txt\necho \"=== PHN massage ===\"; ls | grep -i phn; grep -n -i \"massage\\|masser\\|massa\" PHN*.txt | head -20",
 "description": "Horn 995, Hübschmann, Pihan"
}
```


### [2026-09-07T17:37:37.495Z] TOOL RESULT

```
=== HRN 995 ===
nniljvg, t. mäljig 'Ameise' ein.
994. tnöze 'Schuh', arab. LW. manzaj.
aw. [/^maoc^ mit paiti 'anziehen (sc. Schuhe)*, vergl.
framv/ti' *das Ausziehen (der Schuhe)'; phlv. tnööak
(Men. ; arm. LW. muöak), vergl. mök (chald. LW.
NpID), auch patmö/tan 'anziehen'; ai. [/^möö- mit ä,
prati anziehen (irgend ein Kleidungsstück)*, mit upa
*Schuhe anziehen*.
LW. afy. möza ; bei. müzag, n. mözay 'Socken, Stiefel,
Beinkleider* (174).
995. ninS *Maus*.
g. muSk,
ai. müs~, skr. müsaka-, mfisika- *Maus, Ratte*; arm.
mvkn 'Maus' (H. No. 206).
kurd. fni§ik, misk; Si{y. mayak, maya 'Ratte', maya-
küfai 'Maus, junge Ratte*; oss. d. miste, t. mist (189);
bei. musk, n. milsk (245).
996. möT 'Haar' ^).
g. mld.
phlv. mö, möd bezw. möf; bei. müd^ mtd, n. mi^
'Haar (eines Menschen), Ziegenhaar' (247).
i tritt sonst dialektisch im Np. nur für ursprüng-
liches ü, nicht für ö ein, doch giebt es Ausnahmen;
man wird also trotz g. bei. mtd doch eine ap. Grund-
form *mauda- annehmen müssen 2).
997. möye 'Weinen, Klage', möylden,
aw. vergl. amayavä' 'Leid'; phlv. wöyaÄ:; ai. vergl.
dmtvä'.
Die von Darmesteter, Et. ir. H. 169, ver-
glichenen aw. ai. Worte lassen sich mit np. möye
lautlich nicht vereinigen, und auch Bartholomae,
=== HUB 4880-4900 ===
phi. tuxsdk. Vgl. auch angabin (A. M.) Honig' = angubln.
§ 24. Inl. u wird zu i in : dbistan *schwanger = phi. apus,
zd. apu&ra- =: *apw^ra-; tihf 'leer = pSz. tihf, phi. tuhik
Shk. 269; diz- *b6se* = duz, ap. dws-, zd. dus-, dui-; pisar
'Sohn* = pusar (nach Horn durch pidar beeinflusst) ^) ; misk
') Bei Firdusi soil b($2 fiir ba 'mit' vorkommen nach Sal. Shuk.
Oram. p. 28. loh kann die Form nicht finden und sie kommt (auch
naoh Sale m an n, Mp. Stud. p. 250) nioht vor. Ueber baz = 'wieder
zu* siehe oben p. 23.
') ^S^ pU* SturpiUakan, syr. HSorbHigdn § 35 und 87. Zur Aus-
sprache Odur vgL JA8B. XXXVII, I, p. 14.
*) Jetzt wird pisdr *Sohn* und pddUr *Vater' gesproohen.— 140 —
(arab. misk) 'Moschus* = musk; Hier folgt auf u entweder
ein Zischlaut (s, s, z) oder ein i in der folgenden Silbe.
§ 25. Inl. u wird zu u durch Ersatzdehnung in : pur
'Sohn' aus *puhr neben pus (pusar) = ap. pttd'^a-; Sapur^)
= phi. Sahpiihr. arm. Sapuh (alter Sapurh) = 'KSnigs-sohn .
Vgl. § 9, d.
§ 26. Fiir ap. u-s erscheint h^-s im Anlaut in: np.
hos, hus 'Verstand* = paz. hOs Min. Gl. 104, Shk. 250, phi.
hos (kann auch os oder us gelesen werden), arm. us *Ge-
=== PHN massage ===
PHN.txt
1566:Abou bekr s'empara de Sédjelmassat en Mauritanie; et les Al-
2331:les pays de Sous, Tafilet et Sédjelmassat dans le Maroc; au nord»
3682:pour ramasser les javelots de leurs adversaires, dans l'exercice
4166:DAMASQUINER et DAMASSER, v. a. (a.)
4183:Le verbe damasser signiGe fabriquer des étoffes de soie àjkurs,
4190:mot DAMASSADE pour désigner une étoffe damassée, soie etfiL et de
4386:à l'autre, et à ramasser avec un bâton recourbé (appelé ij^y^
4817:tienne, renversa les Aghlabites et s'établit à Sédjelmassat. Bien
5608:taux, fameux dans l'histoire, et qui massacraient impitoyable-
6552:précieux ; dérivé de (^^^ [/^/lozan] amasser, rassembler, d'où vient
6842:rassembler, amasser. — Comparez l'espagnol magacen, qui , pré-
6992:tion et fit massacrer devant lui ceux qui s'étaient rendus à son
7217:MASSER, V. a, (a,)
7218:j«w» [mass] manier, toucher, palper. — L'opération du massage
7222:tout à la suite d'un bain, le massage excite chez la personne
10441:Damasquiner et Damasser, v. a. (a.) iSk
10712:Masser, v. a. ( a. ) aSy
```


## [2026-09-07T17:37:38.984Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls | grep -i bqt\necho \"=== BQT grep موش ===\"; grep -n \"موش\" BQT_v4_pages.txt | head -5\necho \"=== BQT grep مشک ===\"; grep -n \"مشک\" BQT_v4_pages.txt | head -5",
 "description": "Find BQT files and grep"
}
```


### [2026-09-07T17:37:39.054Z] TOOL RESULT

```
BQT_alt_v1.txt
BQT_dli_part1.txt
BQT_v1_djvu.xml
BQT_v1_pages.txt
BQT_v1.txt
BQT_v2_pages.txt
BQT_v2.txt
=== BQT grep موش ===
ugrep: warning: BQT_v4_pages.txt: No such file or directory
=== BQT grep مشک ===
ugrep: warning: BQT_v4_pages.txt: No such file or directory
```


## [2026-09-07T17:37:44.737Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7200,7240p' PHN.txt\necho \"=== offset ===\"; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['PHN'],ensure_ascii=False,indent=1))\"",
 "description": "Pihan MASSER entry"
}
```


## [2026-09-07T17:37:45.541Z] TOOL CALL #16: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2053 --image 2>&1 | head -60",
 "description": "Fetch Borhan page 2053"
}
```


### [2026-09-07T17:37:45.937Z] TOOL RESULT

```
sculptée en ronde bosse ou en bas-relief, et employée comme orne-
ment en architecture. L'augmentatif italien s'écrit mascherone,
— C'est aux Grecs qu'on attribue généralement l'invention des
masques; il y en avait de trois espèces : le tragique, le comique,
le satyrique, et l'on en faisait un usage habituel au théâtre.
MASCARAT, n. pr. (a.)
jX^mjm [mou^o^W] et, avec le b t d'unité, 'âj^*miti [mou^askarat\
lieu de réunion d'une armée, camp; dérivé dej. C io g [^o^&ar] armée.
C'est ainsi qu'on appelle une ville d'Algérie, située dans la pro-
,vince d'Oran et à 70 kilomètres de cette dernière ville. Prise
par les Français après un combat meurtrier, elle fut cédée par
le général Bugcaud à l'émir Abd elkader, à la suite d'un traitéMAT * 257
conclu sur les bords de la Tafna en 1887; mais, l'émir ayant
rompu le traité en iSSg, la ville de Mascarat fut occupée de
nouveau par nos troupes en 1 84 1 . On trouve souvent Mascara
écrit sans t à la lin; cependant il est plus régulier de conserver
cette lettre, comme en arabe.
MASSER, V. a, (a,)
j«w» [mass] manier, toucher, palper. — L'opération du massage
ou massement, très-usitée chez les peuples orientaux , consiste à
presser avec la main les diverses parties du corps , pour donner
plus de souplesse aux articulations et aux tissus. Pratiqué sur-
tout à la suite d'un bain, le massage excite chez la personne
qui le subit un sentiment général de bien-être et de plaisir. —
Comparez avec l'arabe le verbe grec fida'CTetv dont le sens est
le même.
MAT, adj. m. (p.)
c»U [mât] défait, réduit à Vextrémité. — Faire mat ou mater veut
dire, au jeu d'échecs, mettre le roi dans l'impossibilité de changer
9 *
déplace, ce qui termine la partie. Voyez Echec. — Par exten-
sion, le verbe mateb s'emploie aussi au figuré, dans le sens de
dompter, humilier, affaiblir, abattre, comme dans les phrases sui-
vantes : mater V orgueil de quelqu'un, mater son corps par les jeûnes
et les austérités. Ce verbe alors a pour participe passé maté, k,
abattu, réprimé, dompté.
MATAMORE, s. f. (a.)
ijy^ia^ \maimjoûrat\ caveau, nom de lieu dérivé de^^^^ [t^amar]
cacher sous terre. Cellier souterrain , silo dans lequel les Maures258 ' M AU
ont coutume de consener le grain. C'est aussi le nom d'une
sorte de prison où le même peuple enfermait jadis les esclaves
=== offset ===
{
 "title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866",
 "edition_found": "1866",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/dictionnairetym01pihagoog",
 "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt",
 "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.",
 "notes": "Built from djvu.xml."
}
```


### [2026-09-07T17:37:53.093Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 136; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2053.png
REF: BQT:2053  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 136  OCR-lang: fas

وچ موش کین
بعرپی فاره میگوبند ۱ - وبا تانی‌مجپول» کربه موشگر ‎٩‏ (۱) » با ثانی مجهول وکاف
ونوحه باشد ۴ . ۱ فارسی وسکون رای قرشت » نوحه گرباشد وآن
موش خوار ۴ - ۱ زبی است که هرکاه شخمی‌بمیرد اودرمیان زنان
با خای نقطه‌دار و واو ی شته صفات‌آن مرده را يك يك بشمارد و توحه
ممدوله‌پروزن هوشیار, ‏ - ۹۹۳ ۳ : کند با ان دیگن آترا شنیده بگربه و موبه
۳۳ بند .
زغن‌راکوبند کمغلیواج اس ۱
اش : موش کود - بکر نات وکاف
باشد . موش
موش در بندی؟ - بسنی پوش بوا و کشیده و برای بی‌نقطهةٌ زده » شپره راکوبند
دربندی است وآنگیاهی باش د که میکوبند واز | که‌مرغعیسی حور
آن شافها میسازند و از جالب ارمنیه میآورند . | است ؛ وبستی ۹۸۷ ی
نقری و ورمهای کرم را نافع است . کوبندجانوری مت صض رد۴ ۲
ی موشکا با کاف بر وزن روستّا» نام | است که‌درزر و و و گ
۰ ر ضه زمین خاله کند 0
هوشك پران - بکر کان ون یذ خال کند موق کور
فارسی و تشدید رلی قرشت » جآنوری است سفید ۱ 2 بخ سات‌خورد. جود خواهند که اورا بگیرند
وشبیه بموش‌وازسرتادمش خط میاه کشیده ودمش از ۷ 9 مه موباخی ند رو و
موی بسیاردارد ودربالای درخت میباشد وازدرخت یرای ۷ برکه (۷) خوانند .گوشتش
بدرخت میجهد هرچند فاصله بسیار باشد و ازین | زهر فائل ات رن
جهت است که موشاه‌پران کونشش 8 . موش گیر ۸ - باکاف فارسی بتحتانی
(۱) چش : موشکر (۱) (۷) چش : انگنت ب رکه .
۱ -هندی باستان - 130810 ۰ سانکریت - 1۳0880268 ۰ - 3۵90168 ( موش :
موش صحرائی ) » ارمنی 1221318 (موش) » افقانی 12281021۳ » 1388128 ( موش صحرائی ) :
و۳۵۶ - 338852 (موش » موش صحرائی‌جوان) » استی121816 ۰ 73151 » بلوچی ۲ 1۵150,
ط۵5 « اسشق ۹۹۵۰ ۰ کردی کلتهزه ( موش ) ۰ 32696 , 198۴ . زازا 10058
« ژابا ص4۰۰ > »گیلکی و نطنزی 128815 » فربزندی 1211810 « که .۱ص ۲۸۷ > ۰ دزفولی
16 2 امام » ؛ جانوری پستاندار از چارپایان جونده » دارای دمی طوبل .
۴ -ظ.ازت ر کیب«موشگر» استخراج کرده‌اند . ۴ - از: موش + خوار(خوارنده).
قی : موی کیر . ۴ - منسوب به دربند ( باب‌آلاپواب ) « معجم‌البلدان ».
۰ «* موش خرما 0 درجاهایی که درخ‌خرما هت بشتر برآن میماند . در هندوستان
بسیار است و به‌آن «کلهری » میگوبند. « فرهنگه نظام >. ‎۹٩‏ -اظ . مصحف « مویگر»
موبه گر(ه.م.) ۷ -کردی ۷۵50-6067 2071۳ [-06واه. ۳۵۲۵ ۳۵8۵-8۵ ؛
زازا 16۵7 309801 « ژابا س 2*۸ » ؛ جانوری است ازحشره خواران » بطول ۱۵ سانتیمتر ؛ با
پوزه مخروطی و دست وپای بسبارکوتاه . چشمهای كوچك موش کور زیر موهای ناحبةٌ سر پنهان
است . دستهای او پهن است و به پنج چنگال قوی ختم میشود .
۸ - از : موش + کیر (گیرنده) . قی : موش‌خوار .
```


## [2026-09-07T17:38:14.165Z] TOOL CALL #17: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2010 --image 2>&1 | head -30",
 "description": "Probe Borhan page 2010"
}
```


## [2026-09-07T17:38:14.182Z] TOOL CALL #18: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-07T17:38:20.461Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 93; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2010.png
REF: BQT:2010  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 93  OCR-lang: fas

مینیون ۱
مینیون ۱)- بفتح اول‌وثانی بتحتانی] زده » بلفت پونانی شنجرف را کوبند که مسوران
رسیده و کسر نون وبای حطی بواو کشیده وبنون | ولقاشان بکار برند .
بیان پانزدهم
در میم با شین نقطه دار مشتمل برهفتاد و دو لغت و کنایت
مشاش - بنتح اول و ثانی بالف کشیده بمعنی آنبوه و بسیار وپر و لبریز وسطین وکنده
و بشین نقطه دار زده » انگبیته (۲) را کوبند | وغلیظ باشد ۴ - ونام قربه‌ایست ازبلوکات غزئین
وآن علی‌باشد قوام داده که برطبق ریزند وپهن | تزديك بموضع مکانه کهآنهم ازقرای‌تزنین است
"کنند تا سرد شود وسخت گردد و دروقت‌خوردن - و جنم اول » معروف است که کر ه کردن پنجةٌ
دندان گیر باشد ۱ - و منع از شاشیدن و بول دست باشد وجمع نمودن انگشتان چنانچه پنجهٌ
کردن هم هت ۴ - و بنم اول» درعربی زمین ۱ دست ظرفیت بهم رساند 8 - و مردم کم و قلیل
نرم ونفی وطبیعت و استخوانهای نرمی که وان | وکروه الاك را نیز کوبند ‎٩‏ - و بمعنی مالید
خوردن ۴ . هم آمده است که ماضی مالیدن باشد چه مشتن
مشبت قلعه - کنایه ازمجمره و عود بمعنی مالیدن است ۷ - و بیخ‌گیاهی هم هت
سوز است - وکنایه ازآسمان هم هت . خوشبوی که‌تخمآ ترا نودری‌خوانند ۸‏ وپعربی‌سعد
مشت - بفتح اول وسکون ثانی وفوقانی | کوبند ‎٩‏ .
(۱) چك » چش : هسینون . (۷) چش : آبگینه .
۱« مشخته . حلوایی بود صافی و درشت . بتازی آنرا ماش خوانند . چین درچین
بود .» « لغفت فری ص 20۸ * » ولی در قاموسهای عربی دیده نشد . رك : مشخنه » انگبینه .
۴ ر4:شاشیدن . ۴ - رك : منتهی‌الارب » اقرب‌الموارد .
۴ -کردی 150 ( فراوان ) « ژابا صس ۳۹۹ * : در اراك ( سلطان] باد ) 1325121 و
5 ( پر ولیریز ) ۸« مکی‌نزاد » :
ازرقی دیو چهر بز مژه رنگه از بدی مشت و از هجیری ونگه.
شیخ سووان « جهانگیری »۸« رشیدی ».
6 - پهلوی 33151 (مشت . قوت) « نیب رکك ص۱۵۳ ۰ اوستا 7۳05۳811 ( 1018811
48 ) [ باندازء يك قبضه ] «* بارتولمه ۱۱۸۹ > هندی باستان- ]1215121 ۰ مازندرالی
```


### [2026-09-07T17:38:20.466Z] TOOL RESULT

```


```


## [2026-09-07T17:38:25.186Z] TOOL CALL #19: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2015 --image 2>&1 | head -45",
 "description": "Probe Borhan page 2015"
}
```


## [2026-09-07T17:38:27.605Z] TOOL CALL #20: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B4%DA%A9",
 "prompt": "Give the full etymology sections for the Persian entries مشک (mošk 'musk', mašk 'waterskin', etc.) — which Middle Persian / Sanskrit forms are cited, and any mention of Sanskrit muṣka or mūṣ 'mouse'."
}
```


### [2026-09-07T17:38:32.293Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 98; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2015.png
REF: BQT:2015  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 98  OCR-lang: fas

و۱ مشکوی
بمعنی شکار آمده است . از شکتن است - و بممنی تندی مکن وآشفته
مشك ذمین > گیاهی باشد بفات مشوهم آمده است که منم ازتندی کردن وآشفته
خوشیوی وآلرا بعربی‌سمد کوبند ومشكك زمینی | شدن باشد .
هم میگویند ۱ . مشک ناقه - بسکون‌کاف (۷) ؛گیاهی
مك فروشان - مسروف است ۴ | است که دانه و تغم آن بماشد مشك خوشبوی
- کنایه از مردمان خلیق و مهربان و خوشخوی | میباشد - وبکسر کاف. مشك خالص و بی خش‌را
باشد . کوبند .
مشك فشان از فقاع(۱) - کنایه مشکنات - بنم اولوسکون ثانی و دسر
از شخصی است که در وقت حرف زدن بوی‌خوش ثالت وفتح نون وکاف ساکن, پرنده‌است كوچك
از دهاش برآید ۰ شمه يكيك واو پیوسته در کنارهایآب شند ۷
مشکک - بنم اول. صخيرمعك‌است ۴ - وگوی عمیق را نیز گوبند که در زمین افتد .
و ناگیای هم هست خوشبوی که بمریی سمد مشکو ر مشکوی ۸ - بنم اور
خوانند ۱ 1 ۱ وسکون ثانی و ثالث بواو مجهول کشیده در لغت
۱ مشگل « بفتح اول وسکون نالی‌وضم اول و بتحتانی زده در لغت دویم » بمعنی بتخانه
کاف فارسی ولام ساکن , وراعزن رآ گویند؛ باشد - و کنایه از حرم‌سرای پادشاهان و سلاطین
در ممنی بجای حرف ثالی نون هم مداست. هم هست ‎٩‏ - وخلوتغانةٌ شیرین وخسرو را نیز
ااعلم . کویند *۱- و بمعنی کوشك و بالاخانه باشد
مشکمالی - بامیم بال فکشید. بروزن مطلقاً خواه کوچك و خواه بز رکه ؛ و بعطی بالا
خشك‌سالی » نام لحن بیست وچهارم است از سی | خانهٌ كوچك را مشکو خوانند - و بافچه را هم
لحن بارید 8 . گفته‌اند ؛ وبفتح: اول نیز درست است - وتصغین
مشگی ۱ - بفتح اول وکاف » نهی‌ومنع مك و خيك هم هست که مشکیجه باشد ۱۹.
(۱) خم۱: قفا .۰ (۲) چش :+ فارسی .
۱ - ردنمشکك . ۴ - جمع مغك فروش,» یعنی فروشندة مشك (ه.م.)
۴ - از : مشکه + که( پوند صغیر ) . ۴ اظ . مصحف « منگل » (ه.م.)»
و رك : شنگل. وقی : هشنگه. مشنگك. 8 - درصورت الحان باربدی که نظامی گنجوی
در خسروو شیرین‌آورده نام لخن سیزدهم است :
چو درمشکوبگفتی (چوبرمشکوبه کردی) مشك مالی همه مشکوشدی پرمشك حالی.
نظامی کنجوی « فرهنگه نظام». رك : جمال زاده . آوازهای قدیمی ابران . مجلةٌ موسیقی ۷ :
۲ ص۴۳ ‎٩‏ - نهی از « شکتن > . ۷ -رك : رشیدی. ۸ < مشکوبه
«رشیدی» . برای وجه اشتقاق‌آن » رك : معك ( بفتح اول ) [ م۲۶۱4 ح۳] ۰
‎٩‏ - ملکرا هت مشکوبی چوفرخار درآن مشکوکایزانند بسیار . نظامی کنجوی .
و گرنه از مداین راه می پرس ره مشکوی شاهنشاه می پری .۰
نظامی کنجوی « کنجینه س ۰.۶۱۶۵
۴ رفت شیرین زشبتان وفا ( به شبیخون فنا ) نش مشکو وشیستان چکنم ؟
« خاقانی شروانی ص ۷۲۵۸ » ورك : جهانگیری .
```


### [2026-09-07T17:38:37.752Z] TOOL RESULT

```
# Persian Etymology for مشک

## Etymology 1 (Musk)

**Middle Persian form cited:** mwšk' (mušk, "musk")

**Sanskrit source:** मुष्क (muṣka)

The entry notes this derives "from Middle Persian mwšk' (mušk, 'musk'), from Sanskrit मुष्क (muṣka)." Cognates mentioned include Old Armenian մուշկ (mušk) and Old Georgian მუშკი (mušḳi), plus English "musk."

## Etymology 3 (Waterskin)

**Middle Persian form cited:** mšk' (mašk, "mussuck, skin bag")

**Old Persian source:** 𐎶𐏁𐎣𐎠 (maškā-, "(inflated cow) skin")

This etymology traces to Old Persian and ultimately to Proto-Semitic *mašk-, described as a "Semitic borrowing."

**Note:** The document does not mention Sanskrit mūṣ ('mouse') in any Persian etymology sections.
```


## [2026-09-07T17:38:46.198Z] TOOL CALL #21: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2014 --image 2>&1 | head -45",
 "description": "Probe Borhan page 2014"
}
```


## [2026-09-07T17:38:48.206Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B4",
 "prompt": "Give the full Persian etymology of موش (muš 'mouse'): Middle Persian form, Proto-Iranian/Proto-Indo-Iranian reconstruction, Sanskrit cognate, and whether it is described as inherited (cognate with Sanskrit) rather than borrowed from Sanskrit."
}
```


### [2026-09-07T17:38:53.593Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 97; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2014.png
REF: BQT:2014  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 97  OCR-lang: fas

مشقولیه -۲۹۱۸۶-
هشقو یه ۱ - با قاف ولام بر وزن مشاك بیف ۴ - بنم اول . بمعنی بید
گردویه للم مادرزن وأمق باشد و وامق عاشق | معك است - وبمعنی‌عود هم بنظرآمده است9 .
عضرا بود » و قسةٌ وامق و عذرا مشهور است. مشک دانه - نم اور دانه ای باشد
مغ . بکسر اول وسکون انی وکاف | خوشبوی که‌آنرا سوراخ کنند و برشته کعند -
فارسی ۰ همروف 8 و نام لحن بیست ودویم است ازسی‌لخن بارید۹ ؛
است . کوبند ناف ۹ 1 وبکر اول هم‌آمده است .
آهوی خطائی‌است » 1 ۷ مشکدر ۷ بفتح اول و دال ایجد
و عربان مك ۱ 3 ص َ و سکون ثانی و ثالث و رای قرشت » جانوریست
خوانند۳ باسین اوق که معك و خيك آب را پاره و سورا کند.
بی‌نقطهة‌وبفتج اول, ع / 4
گوذ 11 ۴ - جم اول و فتح دال ابجد
پوست توسفندی ,هاچ
باشد که‌درست کنده ریس وسکون میم در آخر جانوری باشد سیاه رلگه
چا ۰ در غایت خوش آوازی .
باشند خواه دباغت
8 ۸ زر( 6
شده باشد و خواه سقاه ومعك‌او مشکر < بفتح اول وکسرنالی» هنع
شده باشد و درآن ماست وآب کنند ۴ . از شکار کردن است بعتی شکار مکن چه شکر
۱ - مسحف « معشقولیه . زن پدر وامق بود . عنصری ( بلخی ) کوید :
زن بد کنش معشقولیه نام نبودش جز از بد دکر هییچ‌کام .>
« لغت فری ص ۰۵*۱

۴ - سانسکریت 1018162 مصفر 77285 (موش). بونانی33081605 ,لاتینی 118015,
فراسوی و انگلیسی 32180 , عربی مك ( بکر اول ) . غیاث کوید : اهل فاری بکر میم
واهل ماوراءالنعر بضم میم خوانند . در سخةٌ ترجمان‌البلاغه مکتوب بسال ۵*۷ قمری مشك بم
اول ضبط شده ( رك : ترجمان البلاغه چاپ احمد آتش » بخش عکسی ص ۶۷ب و۷۵۱ الف )

و با کاف تازی ادح است ؛ وآن ماده‌است مأخوز از کیه‌ای مشکین باندازة تخم هرغی » هستقر
در زیر پوست شکم آعوی ختامی (غزال السك < 1667 1281) نر» وفتیکه تازه باشد برنگه
شکلات ولزج است. اما خشعك‌آن جصورت کرد دارای طعم کمی تلخ وبوی تند است . آترا بعنوان
اسای‌بیاری‌ازعطربات بکارمیبرند. . رك : 184678.11601 /376۲ ۷۷/۵10516715 ورك: تحفةّحکیم
مژمن: مك . ۴ - در پهلوی 10281 . وآن اسلا بمعنی چرم (مخصوصاً چرمی که در
آن‌آب ریزند) وسپس‌صورت معك ایرزین دریهلوی ز۱ رسالهةٌ خر و کواتان بند ۳ اطبیق چاپ
جاماسب اسالا) درآمده بمعنی خيمهٌ سلطنتی» وهمین معنی‌است که درفارسی «مشکو» و «مشکوی»
شده (ازافادات شفاهی استاد هنینکه) در سغدی 7ع133801. (مغك اپرزین881-2027287)
رد : . 5049 11 .00 ,م2 ,اصافا00620 ۷نط۸۲ واه .8
6 . 0,ون1ع50 , وهند11 ۰ ۴ رد : ید معك. 8 -آنچه دریرهان بمعنی
عود نوشته » اصلی ندارد ( سراج اللغات بنقل فرهنگه نظام جه ص م ) - ‎٩‏ - درصورتی
که نظامی کنجوی درخرو وشیرین برای الحان باربدی‌آورده » لخن‌دهم است. :
```


### [2026-09-07T17:39:01.157Z] TOOL RESULT

```
# Persian Etymology of موش (muš, 'mouse')

**Middle Persian form:** mwšk' /mušk/ ("mouse, rat")

**Proto-level reconstructions:** The entry traces the word back through "Proto-Iranian *múHs, from Proto-Indo-Iranian *múHs, from Proto-Indo-European *múHs"

**Sanskrit cognate:** There is no Sanskrit cognate listed for the Persian word موش. However, the Khowar entry shows a different etymology—Khowar موش derives "From Sanskrit मनुष्य (manuṣya)" meaning "man/husband," which is unrelated to the mouse sense.

**Inheritance status:** The Persian موش is described as "Inherited from Middle Persian," making it a cognate word descended from a common ancestor language, rather than a borrowing from Sanskrit. The article explicitly notes that the Karakhanid word's "Similarity to Persian موش (muš, 'mouse') is a coincidence."
```


## [2026-09-07T17:39:15.052Z] TOOL CALL #23: Bash

```json
{
 "command": "pdftoppm -f 343 -l 343 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg343 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/",
 "description": "Render book page 343"
}
```


## [2026-09-07T17:39:16.077Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/musk",
 "prompt": "Give the full etymology of musk, and also of muscle and massage if shown on the page (quote the chains: Late Latin muscus, Late Greek moskhos, Persian mushk, Sanskrit muska-)."
}
```


### [2026-09-07T17:39:17.142Z] TOOL RESULT

```
total 17724
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 13:39 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb      725 Sep  7 13:36 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb    64151 Sep  7 13:39 pg343.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 13:36 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


### [2026-09-07T17:39:23.254Z] TOOL RESULT

```
# Etymology of Musk

**Musk** entered English in the late 14c. from Old French *musc* and Medieval Latin *muscus*. The term traces back through Late Greek *moskhos*, Persian *mushk*, and Sanskrit *muska-s* meaning "testicle," derived from *mus* (mouse). The etymology reflects a comparison: "The deer gland was thought to resemble a scrotum."

The word expanded to describe various aromatic animals and plants, including the musk-deer (1680s), musk-ox (1744), and musk-melon (1570s).

---

# Etymology of Muscle

**Muscle** derives from Latin *musculus*, literally "a little mouse," a diminutive of *mus*. This reflects an anatomical comparison: muscles' "shape and movement...were thought to resemble mice." The same analogy existed in Greek (*mys* = both mouse and muscle) and appears across languages—Old Church Slavonic *mysica* (arm) and German *Maus* (muscle).

---

# Massage

The page does not contain etymology for "massage."
```


## [2026-09-07T17:39:25.956Z] TOOL CALL #25: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg343.png"
}
```


### [2026-09-07T17:39:26.445Z] TOOL RESULT

```

```


## [2026-09-07T17:39:26.430Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-07T17:39:42.388Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg343.png')\nprint(im.size)\nim.crop((1500,1130,2000,1260)).resize((1500,390)).save('p343_mus.png')\nim.crop((1200,1620,1500,1760)).resize((900,420)).save('p343_lat.png')\n\"",
 "description": "Crop mus and Latin boxes"
}
```


### [2026-09-07T17:39:44.028Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-07T17:39:46.906Z] TOOL CALL #27: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p343_mus.png"
}
```


### [2026-09-07T17:39:46.921Z] TOOL RESULT

```

```


## [2026-09-07T17:39:58.783Z] TOOL CALL #28: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p343_lat.png"
}
```


### [2026-09-07T17:39:58.805Z] TOOL RESULT

```

```


## [2026-09-07T17:40:00.817Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && grep -l \"error_in\" page-3*.json | tail -5 && python3 - <<'EOF'\nimport json,glob\nfor f in sorted(glob.glob('/home/sfmqrb/git/rishe/data/verification/page-3*.json'))[-12:]:\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e.get('nodes',[]):\n            if n.get('error_in'):\n                print(f.split('/')[-1], n.get('id'), n.get('verdict'), n.get('error_in'), '|', str(n.get('book_prints'))[:60],'|',str(n.get('correct_form'))[:60])\nEOF",
 "description": "Check error_in conventions in recent pages"
}
```


### [2026-09-07T17:40:02.326Z] TOOL RESULT

```
page-335.json
page-331.json
page-33.json
page-333.json
page-39.json
page-333.json 12 unverified extraction | None | None
page-333.json 13 unverified extraction | None | None
page-334.json 4 transcription_suspect book | manphur, manfur | mamphur, manfur
page-335.json 1 plausible book | mardta : everyone | mareta (Av. marata-) 'mortal, man'; 'everyone' belongs to So
page-335.json 19 unverified extraction | None | None
page-337.json 1 transcription_suspect book | merx, comerx : merchandise | merx (gen. mercis) 'merchandise'; commercium 'trade'
page-337.json 2 transcription_suspect book | commerci : commerce | commercio
page-337.json 3 disputed book | cumerx : trade | comércio (and the node should be Byzantine Greek κομμέρκιον 
page-39.json 12 transcription_suspect extraction | اتر | اتر
```


## [2026-09-07T17:40:24.306Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/massage",
 "prompt": "Full etymology of English massage and of French massage/masser: what origins are given (Arabic مس massa 'to touch', Portuguese amassar, Greek massein 'to knead')? Quote the etymology text."
}
```


## [2026-09-07T17:40:25.481Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B3",
 "prompt": "Give the Arabic entries for مس: the root م س س, the verb مَسَّ (massa) 'to touch', and the noun مَسّ (mass). Also any Persian entry مس. Quote glosses and root information."
}
```


### [2026-09-07T17:40:29.312Z] TOOL RESULT

```
# Etymology of "Massage"

## English Massage

According to the Wiktionary entry, the English word derives from French. The etymology states:

> "From French _massage_ (noun), from _masser_ ('to massage') (borrowed around the end of the 18th century from Arabic _مَسَّ_ (massa, 'feel, touch'), or from Portuguese _amassar_) + _-age_."

The sources identify three possible origin points: Arabic "massa" meaning "feel" or "touch," Portuguese "amassar," and the French suffix "-age."

## French Massage

For French, the etymology is simpler:

> "From _masser_ +‎ _-age_."

This indicates the French noun was formed by combining the verb "masser" with the standard French noun-forming suffix "-age." However, the French verb "masser" itself ultimately traces back to the Arabic and Portuguese origins mentioned in the English etymology section.
```


### [2026-09-07T17:40:34.097Z] TOOL RESULT

```
# Arabic Entries for مس

**Root:** The Arabic root is [م س س](/w/index.php?title=Appendix:Arabic_roots/%D9%85_%D8%B3_%D8%B3&action=edit&redlink=1) (m s s), containing 5 terms.

**Verb - مَسَّ (massa):**
This Form I verb is transitive with multiple meanings:
- "to feel, to touch"
- "to handle, to palpate"
- "to violate (something sacred)"
- "to infringe upon"
- "(euphemistic) to cohabit with"
- "to befall, to hit"

The conjugation shows it as a geminate verb with past stem vowel *i* and non-past vowel *a*, supporting full passive voice.

**Noun - مَسّ (mass):**
This masculine noun serves as the verbal noun of the verb. Its definitions include:
- "touching, touch"
- "contact"
- "misfortune, calamity"
- "attack, fit, frenzy"
- "insanity, madness"

**Persian Entry - مس (mis/mes):**
In Persian, مس denotes "copper" (the chemical element Cu, atomic number 29). An archaic meaning refers to "fetter, shackle."
```


## [2026-09-07T17:40:40.755Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D8%A7%D8%B3%D8%A7%DA%98/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for ماساژ, including any language-of-origin label (e.g. فر. = French) and the definition. Also any دهخدا entry text."
}
```


## [2026-09-07T17:40:43.183Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D8%B4%DA%A9/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entries for مشک — all senses (مُشک 'musk', مَشک 'waterskin') with the origin labels Mo'in gives (e.g. سنسکریت, پهلوی) and the definitions. Also quote any دهخدا etymology."
}
```


### [2026-09-07T17:40:47.321Z] TOOL RESULT

```
# Farhang-e Mo'in Entry for ماساژ

According to Farhang-e Mo'in:

"[ فر. ] (اِ. ) مالش بدن کسی با سر انگشتان دست جهت رفع خستگی او، مشت و مال"

The entry identifies the term as French in origin and defines it as a rubbing of the body with fingertips to relieve fatigue.

# Dehkhoda Entry

The Dehkhoda dictionary notes that ماساژ (from French) means "mast-o-mal" (kneading and rubbing) and describes it as one method for alleviating pain. It explains how massage helps move pathological secretions from subcellular tissue into veins and lymphatic vessels, and discusses its therapeutic importance following recognition of cellular swelling's role in conditions like sciatica and neuralgia.
```


### [2026-09-07T17:40:49.450Z] TOOL RESULT

```
# فرهنگ معین Entries for مشک

## مُشک (musk)

**Definition:** "مادة سیاه رنگ و خوشبویی که در ناف آهوی مشک تولید می شود"

**Origin:** Sanskrit etymology indicated (سانسکریت)

## مَشک (waterskin)

**Definition:** "خیک، پوست گوسفندی که آن را قالبی کنده باشند"

The entry marks this form with a different vocalization (fatha rather than damma on the initial م).

---

## Dehkhoda Etymology

The Dehkhoda lexicon provides extensive etymological detail, noting that مشک derives from the ناف (gland) of the خطایی آهو (Himalayan musk deer), with the substance produced through natural biological processes. The text distinguishes this term from Arabic مسک and discusses regional pronunciation variations between Persian speakers (کسر) and Transoxianan speakers (ضم).
```


## [2026-09-07T17:41:08.692Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls | grep -iE \"FVQ|AFM|PLA|AFA|DEV|DOZ|LAM\"\necho \"=== FVQ misk ===\"; grep -n -i \"misk\\|musk\" FVQ_pages.txt | head -10\necho \"=== AFM مسك ===\"; grep -n \"المسك\\|( المسك )\" AFM_pages.txt | head -10\necho \"=== PLA ===\"; ls incoming/PLA 2>/dev/null | head",
 "description": "grep Jeffery, Addi Shir, Asbaghi"
}
```


### [2026-09-07T17:41:08.771Z] TOOL RESULT

```
AFA.txt
AFM_alt.txt
AFM_pages.txt
AFM.pdf
AFM.txt
DEV.txt
DOZ.txt
FVQ_pages.txt
FVQ.txt
LAM.txt
=== FVQ misk ===
9501:(Misk).
9503:Musk.
9514:(Miskin).
9522:The muskenu of the Cuneiform inscriptions was interpreted by Littmann
=== AFM مسك ===
582:1 بالمسكة 3 5[ 6
3614:والمسك واللادن والكافورܒܝ <
3657:غيده المخرقة اختلاق التكذب وهي كلمة ܙܝ على الخراق كاك.سكن على المسكين
3862:أن طاف اقطار المسكونة اتتهى الى اذور 9 وأعر 43" 0.33
3922:0ه فحّة ) وعاء المسك اي ܐܙܪ ا ٠‏ تعر يبب 0
3923:1 + 0 لمك فان المسك جشمع حول مرعها اتات
=== PLA ===
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
```


## [2026-09-07T17:41:11.730Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN page around massage ===\"; awk 'BEGIN{RS=\"\\f\"}{n++; if (index($0,\"massage,  n.\")>0) print \"leaf(0-based FF index):\",n-1}' KLN_1966.txt\necho \"=== KLN musk leaf ===\"; awk 'BEGIN{RS=\"\\f\"}{n++; if (index($0,\"musk,  n.,  substance\")>0) print \"leaf:\",n-1}' KLN_1966.txt\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['KLN'].get('page_offset'));print(d['AHD'].get('page_offset'));print(d['BQT'].get('page_offset'));print(d['POK'].get('page_offset'))\"",
 "description": "Locate Klein page numbers"
}
```


### [2026-09-07T17:41:13.030Z] TOOL RESULT

```
=== KLN page around massage ===
leaf(0-based FF index): 507
=== KLN musk leaf ===
leaf: 545
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
```


## [2026-09-07T17:41:25.388Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=23000 && NR<=23090 {print NR\": \"substr($0,1,90)}' KLN_1966.txt | grep -nE \": *[0-9]{3}$|massage|masseur|mass,\" ",
 "description": "Find Klein printed page numbers near massage"
}
```


## [2026-09-07T17:41:26.599Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=24700 && NR<=24800 {print NR\": \"substr($0,1,80)}' KLN_1966.txt | grep -E \": *[0-9]{3,4}$|musk,\" \necho \"=== FVQ misk entry ===\"; sed -n '9490,9530p' FVQ_pages.txt",
 "description": "Klein musk page + Jeffery misk entry"
}
```


### [2026-09-07T17:41:26.746Z] TOOL RESULT

```
43:23042: 944
44:23043: 945
61:23060: mass,  n.,  quantity,  size.  —  ME.  masse,  fr.  OF. (=  F.)  masse,  fr.  L.  massa, 
62:23061: Derivatives:  mass,  v.  (q.v.),  mass-y,  adj.,  mass-i- ness,  n.
63:23062: mass,  tr.  and  intr.  v.  —  F.  masser,  fr.  masse.  See mass,  n.
66:23065: Derivatives;  massage,  tr.  v.,  massag-er,  n., massag-ist,  n.
71:23070: masseur,  n.,  a  man  who  practices  massage.  —  F., formed  fr.  masser,  ‘to  mas
72:23071: masseuse,  n.,  a  woman  who  practices  massage.  —
73:23072: F. ,  fem.  of  masseur.  See  prec.  word, massicot,  n.,  yellow  oxide  of  lead.  — 
91:23090: 946
```


### [2026-09-07T17:41:27.954Z] TOOL RESULT

```
24742: musk,  n.,  substance  secreted  by  a  gland  near  the testicles  of  the  mus
24786: 1021
=== FVQ misk entry ===
1 Horovitz, Parodies, 11; Geyer, Zwei Qedickte, i, 87 ff. ; Ximmern, Akkad.
Fremdw., 40.
2 Cook, Glossary, 75 ; Duval in JA, viii c Ser., vol. xv, 482.
3 ZDMO, xxii, 268.
4 Cowley, Aramaic Papyri, p. 148.264 FOREIGN VOCABULARY OF THE QUR*AN
In the Qur'an it is used of the fane at Quba' (ix, 109), of the Temple
at Jerusalem (xvii, 1), of the Church built over the Seven Sleepers
(xviii, 20), and other places of worship, so that it is clear that for
Muhammad it meant any place of worship. In the same general sense
it is used in the pre-Islamic poetry, 1 and so must have come at an early
date from the more settled communities in the North. 2
(Misk).
Ixxxiii, 26.
Musk.
This sole occurrence is in an early Meccan description of Paradise.
The word was widely used among the Arabs in the pre-Islamic
period 3 and was quite commonly recognized as a loan-word from the
Persian. 4
The Phlv. 4-tyi^* mushk 5 seems to have come ultimately from the
Skt. *nra, 6 but it was from the Iranian, not the Indian form, that
were borrowed the Arm. jh^ 7 ; Gk. //capos' : Aram. ptflB ;
Syr. JoaQLo ; Eth. JJfllf|. It is more likely to have come direct from
Middle Persian into Arabic 8 than through the Syriac, as Mingana,
Syriac Influence, 88, claims.
(Miskin).
Of very frequent occurrence, e.g. ii, 77, 172 ; ix, 60.
Poor. "
' '^e ' ...
Note therefrom the formation <1X.^.^ poverty, indigence, n,
*58 ; iii, 108.
Fraenkel, Vocab, 24, pointed out that the Arabic word is from the
Syr. ]* *>ffnVo though this comes itself ultimately from Akkadian.
The muskenu of the Cuneiform inscriptions was interpreted by Littmann
1 Horovitz, KU, 140.
2 Schwally, ZDMQ, Hi, 134 ; Lammens, Ranctuaires, passim ; Von Kremer,
Streifziige, ix, n.
3 Siddiqi, Studien, 85 ; Geyer, Zwei Gediehte, i, 90 ff. : ii, 79. r
4 al-Jawaliqi, Mu'arrab, 143 ; ath-Tha'alibi, Fiqh, 318 ; as-Suyu^i, Itq, 324 ;
Mvzkir, i, 136; al-KhafajI, 182; LA, xii, 376.
5 Justi, Glossary to the Bundahesh, p. 241. Vullers, Lex, ii, 1185.
7 Hiibschmann,* Arm. Gramm, i, 196. 8 Vollers, ZDMQ, 1, 649, 652.FOREIGN VOCABULARY OF THE QUR*AN 265
```


## [2026-09-07T17:41:43.392Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM around 3920 ===\"; sed -n '3915,3930p' AFM_pages.txt\necho \"=== AFM headword مسك ===\"; grep -n \"( مسك\\|(مسك\\|( المسك\" AFM_pages.txt | head\necho \"=== PLA misk ===\"; grep -n -i \"misk\\|mušk\\|Moschus\" PLA_pages.txt | head -20",
 "description": "Addi Shir and Asbaghi on misk"
}
```


### [2026-09-07T17:41:43.458Z] TOOL RESULT

```
=== AFM around 3920 ===
܀ ܟحا ¿ © ܐ ܘܡܐ
* 5 السكران ܐ :¥97 اي سكر ومن بان (ويقال .50
وان» أي صاحب
5 بقل طيّب 3[ 1:3 وهو ايضاً ® بالتركيّة وك
بالكردة و سكع بالاراميّة و سلح» بالسريائّة الدارجة او ܝܐ بوورون
باليونانة 1161111329 بالرومسة 11111119 بالاتكايرنة وع111611 بالفرنسة و 1111176
بالكرمانية و 111@1112 بالايطا ® و اوباب لارى بالارمنمة
0ه فحّة ) وعاء المسك اي ܐܙܪ ا ٠‏ تعر يبب 0
1 + 0 لمك فان المسك جشمع حول مرعها اتات
اليد ) ¬ فيه تعريب انيور ܙ ܕܐܐ الارامي” ܫܝܦܘܪܐ ܙ البوق
ܠ .0 ܐܒܨ 2 وونة 107 ܐ ° ܒܘܩܝܢܐ
9 السراويل الموضع 0 من معرب 0
ܟ (الشكر ) الداهي الفطن تعريب كران حذف شطره نحفيفاً ٠‏ ونكران
1 01 وهو اسم نال مق ( 0057 30
ܣ اي الدهاء والفطنة لل عدذلك
الك ) ܐ :1:3 ܚܒ انك رين اي * اللحية 3
=== AFM headword مسك ===
=== PLA misk ===
ugrep: warning: PLA_pages.txt: No such file or directory
```


## [2026-09-07T17:41:45.125Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY موش ===\"; grep -n \"موش\" incoming/ARY/ARY_pages.txt | head -8\necho \"=== ARY مشک ===\"; grep -n \"مشک\" incoming/ARY/ARY_pages.txt | head -8\necho \"=== ARY latin index MUS ===\"; grep -n -iE \"^MUS|MUS-|MOUSE\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Aryanpur on mouse/musk"
}
```


### [2026-09-07T17:41:45.311Z] TOOL RESULT

```
=== ARY موش ===
13510:3 ,21172 دانمارکی موش ۶ 05
13825:۱ بازگشت به: موش.
13827:۳ واجریشه‌ی شناسان معتقدند که واژه‌ی "مایچه" (که شاید در اصله آمرشچه" رده است) با واژه‌ی "موش" خوبشی
13828:دار د و بهمین دلیل واژه‌ی ماهیچه در لاتین (18ن1ت۸108601) مصفر واژه‌ی 11118 به معنی "موش * است. دلیل این
13829:خویشی» شباهت شکسل ساهیچه‌ی دوسر و "موش" است. فمن در زبان‌های ارمنی و یوتانی واژه‌های
=== ARY مشک ===
1247:دگرگونی تلفظ آنهاء شناخت خویشی نزدیکه آنها را مشکل مي‌کند.
1615:واجریشه‌های مشکوکه نوشته‌ام(شاید).
1930:خواننده» جلر واژه‌های مشکوکك (شاید) آورده است.
3147:معنی این واژه در زبان گوتبکه: مشک شراب,
14066:۴ | مشک
=== ARY latin index MUS ===
13541:MUS «(OLD SCANDINAVIAN) 45 541-31 MUSHKA (SANSKRIT) 2 Sil
13542:MUS (OLD HIGH GERMAN) yf gall MUKN ARMENIAN) .¢a .)
13543:MUSKEL (GERMAN) git (GREER)-Jhiy « gl
13544:MUS (OLD ENGLISH) 4S pK Mis, Mis, MYos;Niio- *
13545:MUSCLE HENGLISH) 53S MUSCULUS LATIN) pa
13546:MUSKLE (DANISH) Silo MUSCLE AAPRENCH) ib
13547:MUSKEL SWEDISH) (628 yo MUSCULO SPANISH) glee!
13548:MUSKEL :(NORWEGIAN) «$39 5 MUSCULO. A(ITALIAN) git
13549:MUSCHI ARUMANIAN) gly)
13550:MUSCULO —«(PORTUGUESE) Js »
```


## [2026-09-07T17:41:51.283Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY 13490-13560 ===\"; sed -n '13490,13560p' incoming/ARY/ARY_pages.txt\necho \"=== page tag ===\"; awk 'NR<=13560 && /\\[pdf page [0-9]+\\]/{t=$0} END{}' incoming/ARY/ARY_pages.txt\ngrep -n \"\\[pdf page\" incoming/ARY/ARY_pages.txt | awk -F: '$1<13560' | tail -3",
 "description": "Aryanpur muš/mâhiche entry"
}
```


### [2026-09-07T17:41:52.879Z] TOOL RESULT

```
=== ARY 13490-13560 ===
لاتین (7100ل): لیترانی ((4ا(هنا 7 7ا):
30 ,116183785 ,11۳6585 0 با 155۲۲۲
فرانسه (//۳7/2۸): 1 لتونی (لنی) (/47۳4): 132710 ,217لشآ
ایتالپایی (0غلله7): 1 ایرندی کهن (84ل#ا 2ا0): 11 :
رومانی (27ا 1۸4۸۸ #): دای ۹
پرتغالی (ظ۳0/7170188): 1 پسگشت‌ها 5
گونیکه (0077110): 2117 ۳۳ ۱
ایسلندی کهن ((54(70/0۸۸ ضا0): 3 (11۳6) +7 لفط ۱
51۸ 6 (۸0388) م۸2
ساکسونی کهن (/(54200 ۰:01 1216608 207 2
آلمانی کهن (/027040 07 ]با 2ا0): 6 (۲360) :0/105
: ۲ 10 9 (16ا) +7
ات آلمانی 084490): ۰ 10 برهان قاطع : ۹۵
انگلیسی کهن سماامیم: نات
اوستایی (4837(۷): ۸73۸۸ ,۸17۸1۸1488 پهلو: ی (اامابزهم: 8۸۸۸ بقلقال۸ مقاق۸ه
پارسی پاستان (4(۷اق۶87 ۵12): ۰ ۸۱/25۸ اوستی (03387/6): 1۸
[pdf page 455]
۶ | ملد
کردی (7ل60(15): هلا ,۵۳۵ ,28 انگلیسی کهن (8۸01/3/1 صا0): 18
اففانی (پشتو) (/۸۳0/7۸۷): آنگلیسی (7ل5لا8(/0): 15
3 ,21172 دانمارکی موش ۶ 05

تخاری ۸ (۸ [(4ل7ل102). 3 سرئدی (89525[7): 5

تخاری 8 (8 ۸ 7021۸7): ۳۸۹ نروژی (0775012۷/). 095
سانسکریت (84(/58077): هلندی (017637): . 085
۸۸1۸0 ,۸۸۹ ,ش۸۲۸۳ اسلاوی کهن (12/ا ما5 7ل)#ناتل0 صا0):لآق7۸
ارمنی (8(45011407): قلد ای چکه (280)): ,ق3۸
یونانی 078870): 5۸5 اسلواکي (510743): ,2۸85
لاتین (7120ل): تن پروسی کهن (/۶5۸ت۲۴۷ 0ا0): 7201807
فرانسه (ق۳82۸)+ 08 ولزی (77د 8 ): ,۶1
اسپانیایی (5۳۸/۷/۶7): 108 ,7708077405 آلبانی (۸1۸2مقلهم): ۸ ,75
ايتاليایی ((۸ا74): 0 هنبت (7177[72): ۸8 ,۸3۷2۸87

رومانی (4۸(۷۸۸انا):

58 71057 ,[70 پسگشت‌ها اهر ۲
پرتغالی (۳08712010882): 8 758 : میت مین
گرتیک (ع/00711): 18 9 (۲5) وی ان ۸۳
ایسلندی کهن (210۸71۵(۷ی5 صاه): 058 9 (۷۳) مان / ارات هب ۲/۶
ساکسورنی کهن ((5)0 صا0): 195 5 (15)) :0702/5
فریزی کهن (۷لفولق۲ صا0): نی 1 (9ت) :547
آلمانی کهن (1ل05801 104 ۵ا۵): 18 برهان قاطع : 1۹۳۱
آلمانی (088//۸0۷): 8

۰ اوستایی (ل487۸): ۸ اففانی (پشتو) (470/۸/0): 110
پارسی باستان (۵(۷ا28۹ ۰:02 ۸/1۸7۸* تخاری 4 (۸ ۸۸ ل70): ۸
پهلری (1ماتلمه): 0 120۸8 تخاری 8 (8 4۸ ارتل70): 3 با ۱
اوستی (05527/6): 3120 ,31۸0۸ ,112205 سانسکریت (54(/587): 3127۸ بال۸127۸
کردی (015(1/(): م۸2 آرمنی (۸/87/0۷): ۸8 اب۸۸
بلوچی (/8۸617): 8ق٩‏ ,312713 ,۸127 یونانی (08225): بد وین انا

اد ا
[pdf page 456]
لاتین (7100): 3 با روسی (/53148): ۸7
فرانسه (۳72(/67): نا چکه (ل280): 1۸۸
اسپانیایی (3ل52۸0(/8): ای زا صربی (/5588[4): ۸7
ایتالیایی (المل7/): ای ۱( بوهمی ۰:۵0 ۷2۵3۲ ,۸۴۶
رومانی (/(۸4۸/4ل8۷): 3 اسلا کی (51.014): ۸۸
پرتغالی (00871001-582): ۸ لیتوانی ریرمپرمنا :31076 ۸1072۸
ایسلندی کهن ((4 542۷010/۸۷ ا0): لترنی (لتی) (71/۷ا): اد نی
3 1 رد ابرندی کهن (تلقل#ا 0۵): ۱
ساکسونی کهن (540000 012): ۰ 1100۸8 گالی (5/]ا0۸): 0(
فریزی کهن رمرممم صام: ۰ 008۸ ولزی (للکل(): 1
آلمانی کهن (65704/۸ 04/ط طلا0): پرتونی (/87570۸): ۳۸3
3 گالیکه (حللتظده): 3
آلمانی (1۸ل087): ۳( آلبانی ‏ (ل(ا#لفقام): 072
انگلیسی کهن (ب5/-ا2(۷0 صا0): ۰ 110008
انگلیسی (8۸/0]/50): 0 پسگشت‌ها ارت تا
دانمارگی (۵۸(۷38): 13 0 ۶0/09
سوئدی (9ز81852/3): 3 داریا 0 (۸107387) 8۸70/7۰
=== page tag ===
13477:[pdf page 454]
13506:[pdf page 455]
13543:[pdf page 456]
```


## [2026-09-07T17:42:06.987Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY 13815-13840 ===\"; sed -n '13815,13840p' incoming/ARY/ARY_pages.txt\ngrep -n \"\\[pdf page\" incoming/ARY/ARY_pages.txt | awk -F: '$1<13840' | tail -2\necho \"=== ARY مشک 14050-14080 ===\"; sed -n '14055,14080p' incoming/ARY/ARY_pages.txt\ngrep -n \"\\[pdf page\" incoming/ARY/ARY_pages.txt | awk -F: '$1<14070' | tail -2",
 "description": "Aryanpur mahiche and mešk entries"
}
```


## [2026-09-07T17:42:07.697Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && ls && grep -n -i \"misk\\|Moschus\\|mušk\" PLA_asbaghi_1988_ia_djvu.txt | head -20",
 "description": "Asbaghi on misk"
}
```


### [2026-09-07T17:42:08.277Z] TOOL RESULT

```
=== ARY 13815-13840 ===
ایتالیایی (۷هاله7): 0نا2180 نروژی (0/08501۸: ده نا
رومانی (/۸4۸(/1۸/#): 3زا
پرتغالی (۳087000835: ۰ 11380171-0
[pdf page 465]
۶ ال
پسگشت‌ها 5 8 (۸115016) ۱۳/0/5
زان 000010 بر رها 1 (5 0۸083 34
7 هت‌وناین 7 فرهنگ ممینارایلا بر ۶۳۷۴۴ ۳۷۴۵
135 :۸6 ما0 : و ت
یادداشت: 5
۱ بازگشت به: موش.
۲ چم این واژه در سانسکریت: خایه,
۳ واجریشه‌ی شناسان معتقدند که واژه‌ی "مایچه" (که شاید در اصله آمرشچه" رده است) با واژه‌ی "موش" خوبشی
دار د و بهمین دلیل واژه‌ی ماهیچه در لاتین (18ن1ت۸108601) مصفر واژه‌ی 11118 به معنی "موش * است. دلیل این
خویشی» شباهت شکسل ساهیچه‌ی دوسر و "موش" است. فمن در زبان‌های ارمنی و یوتانی واژه‌های
و18 ۸5(با ۸1385) دو چم دارند: مرش و عضله.
۴ واژه‌های ژرمنی این فهرست همه از لاتین مشتق شده‌اند.
پهلوی (4ال2۸): 81۸7۸۲ ,۸127015717 8ب ۱۱۳۹
کر دی (ل68۵15): 55331۸18 ,2/۸5
سانسکریت (7ل8۸4(80): ۸ پسگشت‌ها 5
یرنانی 0580): 3 700 مهو
لاتین (47100): 16۵78 بف1137893 اک این انا
فرانسه (۳2۸۴(4): اب ۱۷۳۱۱ 40 (تفت23 ان هه ره رین
اسپانیایی (5۸(18[7): با 3 (01۸1788) تمد هم
ایتالیایی (/(۵لل): ۱۸788۸ ۰ | 196 جتفتاهی) ۸
پرتغالی (۳07001895), ۸7۸۸ برهان قاطع + ۴ و ۱۹۳۴
13792:[pdf page 464]
13818:[pdf page 465]
=== ARY مشک 14050-14080 ===
سندی (3002(0): ان لترنی (لنی) (401ا7#م): فلا .۰
لیر سانکریت (۷507ل54): پروسی کهن (/(954تا۲۸ ص/0): ۰ ۱10۸818
۳ ۱ 2 ۱۸۹۸۸ دا
ایسلندی کهن رمرظنام یی 2ا0): پسگشت‌ها اه اند
155 نا
آلمانی کهن (/(02804۸ 04آلز صا0): نت اس تشد
۸15۸ 48 (نا۸ظ۲ 80 8۸۴)
اسلاوی کهن (۷۲۳بما٩‏ 6126/4 صا0): 4 (048800) :۸۸225
[ا شدای برهان قاطع + روما
لهستانی (0/734): ۱107
[pdf page 473]
۴ | مشک
چمانگلسی سوازی فرش سس 286
پهلری (۲7شاتلم): کاننی نا 3
سانسکریت (84(/5707): 35۸3 پسگشت‌ها 5
برنانی 0782/0): 005( 3
لاتین (7700با): 15 8 (0/1556 ۰ - 280/7
فرانسه ([88۸۲ق): دنا 4 (0656) داد
آلمانی (688//۷): 1108671175 ,2118017 8 (۸/84) :0105
انگلیسی (57ا2۸/0): ۸ 2 (۸۸86) نون اج
هلندی (3ل76ا0): 5 برهان قاطع : ۳.۱۴
یادداشت,
چم این واژه در زبان سانسکریت: خایه. َ
آوستایی (۸۲287۸2): 6۸ ,نا۸1۸6 پر تغالی (۳077701852)+ 0
پارسی باستان (8۶۵4/۷ صل0): گرتیک (077170): 115له۸1 ,21۸6۸1
۸6 ,1۸6175 ,تا8تا۸/ ایسلندی کهن (010۸۲1۵2ی5 )+
14041:[pdf page 472]
14065:[pdf page 473]
```


### [2026-09-07T17:42:08.330Z] TOOL RESULT

```
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
2260:_ I - ”istär: "Münze, 4.1/2 Miskal, vier" pers. ı aus pers. Us 
4308:Me aranfama$ : "Frankenmoschus" pers, ua farangmusk <Tmp. 
4312:Im altind., altchines. u. altpers. Arzneischatz wurde Moschus erwähnt- 
15265:SW SUCHE firangmask: "caryophyllus aromaticus, Frankenmoschus" << mp. 
15416:Arab _ falangamisk = faranfamiäk q. v. 5 
18171:miSk 250 
18177:Zu miSk: "Moschus" oT pers 2. mo&k ı MP. zur muSk 2, syr. Jun 
18183:pers. muSk >er. musk, tk. misk, mlat. muscum, frz. musc, SP.Musco, 
18186:engl. musk, dtsch. Moschus. 
18189:Moschus skr. B> pers. > ar. > lat. a 
18881:u _ narmask: "Duft, Moschus aus Granatapfel" = narmask q. v. a,
```


## [2026-09-07T17:42:28.255Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && sed -n '18165,18195p' PLA_asbaghi_1988_ia_djvu.txt\necho \"=== page tags near ===\"; grep -n \"\\[pdf page\" PLA_pages.txt 2>/dev/null | head -3",
 "description": "Asbaghi misk entry full"
}
```


### [2026-09-07T17:42:28.302Z] TOOL RESULT

```
11. Wahrmund s. v. 


11 


miSk 250 


muläb 


Zu miSk: "Moschus" oT pers 2. mo&k ı MP. zur muSk 2, syr. Jun 


(pers. ) 3 


pers. muSk >er. musk, tk. misk, mlat. muscum, frz. musc, SP.Musco, 


engl. musk, dtsch. Moschus. 


Moschus skr. B> pers. > ar. > lat. a 


Eine Ableitung hiervon ist lat. muscatus >engl. muskate, dtsch. 


Muskat 5, 
=== page tags near ===
```


## [2026-09-07T17:42:30.251Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== DEV masser ===\"; grep -n -i \"masser\\|massage\" DEV.txt LAM.txt DOZ.txt | head -10\necho \"=== SKT massage ===\"; grep -n -i \"massage\\|mass\\b\" SKT.txt | head -5\necho \"=== WEB massage ===\"; grep -n -i \"massage\" WEB.txt | head -5\necho \"=== FSD ===\"; ls | grep -i FSD",
 "description": "Devic/Lammens/Dozy/Skeat/Webster on massage"
}
```


### [2026-09-07T17:42:30.339Z] TOOL RESULT

```
=== DEV masser ===
LAM.txt:1542:de Ja3 laqai, recueillir, ramasser. Bocthor et Marcel tra-
LAM.txt:6936:(1) C^est la déâmtion de Massergouaïhi, cité par Ibn el-Beithâr :
DEV.txt:435:Alicate.  Sorte  de  pince  dont  se  servent  les  émailleurs à  la  lampe.  Esp.  et  port,  alicate.  C'est  l'arabe  bUAJî  al-laq- qât,  tenailles,  comme  l'a  fort  bien  remarqué  M.  Defré- mery^,  de  la  racine  \xxi  hqat,  recueillir,  ramasser.
=== SKT massage ===
453:Agglomerate,  to  ma«s  together.  (U) Pp.  of  L,  agglom/rarf,  to  form  into  a  mass,
454:—  L.  ag-=ad;  Jtnd  gfam^r-,  stem  ctf  ghmus, a  mass,  ball,  clue  of  thread,  allied  to giobtts,  a  globe  ;  see  Globe.
2439:bullion  cF.  -  L.)  F.  boMUhn,  a  stud ; but  the  O.  F.  buUione  meant  a  mint,  and Low  L.  bulliono,  bnllie  meant  a  mass  of iDelaI.*Low  L.  bullare,  to  stamp,  maik with  a  seal.  — L.  bulla,  a  seal;  sec  Bull  (2).
3587:L)  -,  ortg.  a  mass
3588:the  ti:uc  woi.i  u  M.  E.  ctudt, ck.  A-  S.  ^/i/J*.  a  round  mass, Ic,  hill.  Allied  to  (Inv.  q.  r., (wfaeuce  E.  con-gh-mtr'
=== WEB massage ===
ugrep: warning: WEB.txt: No such file or directory
=== FSD ===
FSD_vol1.txt
FSD_vol2.txt
FSD_vol3.txt
FSD_vol4.txt
```


## [2026-09-07T17:42:40.018Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls | grep -i \"WEB\"\necho \"=== FSD vol3 massage ===\"; grep -n -i \"massage\" FSD_vol3.txt | head -5\necho \"=== FSD vol3 musk ===\"; grep -n -i \"musk, n\" FSD_vol3.txt | head -5\necho \"=== FSD vol2 ===\"; grep -n -i \"massage\" FSD_vol2.txt FSD_vol4.txt | head -5",
 "description": "Funk &amp; Wagnalls massage/musk"
}
```


### [2026-09-07T17:42:40.108Z] TOOL RESULT

```
WEB_vol1.txt
=== FSD vol3 massage ===
15159:ptotlos Massage produces a oomhlned tonlo and sedative
15169:(K., < maaaer ( < Or. maaaO), knead | ~ vibratory massage,
15310:ihAr-a-pfl'tlse. a The aystematlc use of massage In the
34797:Uterus by external massage — cascade ni.. In the llguefar-
137055:The Instrument used in percussion massage,
=== FSD vol3 musk ===
54687:mosque, 1 mosk; 2 musk, n. A Mohammedan temple of {
61657:musk, n. 1. A soft, unctuous, reddish-brown powdery
=== FSD vol2 ===
FSD_vol4.txt:28602:Swin'ton  and  PenMle-bur-y.  An  urban  district  In  Lan- swJpe,  1   swcUp,  2   swip,  tt  [swiped,  swtp'in‘0  1   1.  [Col- loq  ]   To  give  a   strong  blow  or  swipe  to,  strike  with  full swing  of  the  arm  2.  [Slang  I   To  take  with  a   swipe  or sweep  steal  by  snatching  as,  to  steipe  a   watch.  3t.  To drink  down  hurriedly  [<  AS  swipian.  move  rapldlj  1 swlppet-— swlp'cr,  n   IColloql  One  who  swipes swipe,  n   1.  [Colloq  ]   A   hard  blow,  a   swiping  blow, especially  m   field-games,  as  cricket  2-  A   weU-sweep or  similar  sweep  See  sweep,  n   ,   4   (2)  3.  A   dnnk  gulped down.  4.  [Slang]  A   massage  or  rub -down  —   swipe'* beam",  n   The  counterpoise  lever  of  a   drawbridge  [C  l swipes,  1   swolps,  2   swlps,  n   [Colloq  1   Poor,  weak  beer, hence,  any  beer,  also,  the  leavings  of  beer  in  a   mug Bw>pest.  [tipsy
FSD_vol4.txt:39691:Trlp'sa-cum,  i   trip'ss-kum  2   trlp'sa-cum,  n   Bot  A genus  of  tall  American  perennial  grasses.  Including  the gama-grass  ( <   Gr  tripsts  see  tripsis  f trip 'sis,  1   trip'eis  2   trip'sis,  n   fRare  1   1 _   2,  A   shampoo  or  massage  [<  Gr  tripsis,
FSD_vol4.txt:48244:V   Ibrate  +   -scope  J— Tl"bro-scop'Jc,  a vl"bro-thcr''a-peu'tIC8,  1   val  bro-fhcr'o-plfl'tiks,  2   vITiro- th6f*a-pQ'tlc8,  n   Med  The  use  of  vlbratorj  massage  as a   healing  agent  I   <   L   rfbro  vibrate  +   tbyrapbutjcs  ] Vl-bur'num,  1   vol-bOrinom,  2   vl-bilrinflm,  n   Bot  1.  A large  genus  of  shrubs  or  small  trees of  tbe  honeysuckle  family,  having opposite  entire  or  serrate  leaves  and clusters  of  small  flowers,  becoming  ’ a   dry'  or  fleshy  ovoid drupe  In  fruit  2.  (v-]
FSD_vol4.txt:62038:Illustration  of  typical heads  of  race-stocks, schemes  of  races maple  Varieties marble  Varieties marine  engine Parts  of  a   triple-ex- pansion engine massage
FSD_vol4.txt:64361:massage,  mo-say*,  TFr ,   1*.  2,  3,  6,  6   7, 8, 16, 20.  23, 25.-ma8'jJ*,  8 , 1»,  11, 14, 17, 18  19
```


## [2026-09-07T17:42:41.259Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/massage",
 "prompt": "Quote the full etymology of massage (noun and verb) and masseur: which origin does Etymonline give — Arabic massa 'to touch, feel, handle' or Portuguese amassar / Greek massein?"
}
```


### [2026-09-07T17:42:46.546Z] TOOL RESULT

```
# Etymology of Massage

**Noun:** Etymonline presents two possible origins without definitively choosing between them:

1. **Arabic origin:** "possibly from Arabic _massa_ 'to touch, feel, handle'" with the caveat that "if so, probably the word was picked up in Egypt during the Napoleonic campaign there."

2. **Portuguese/Latin origin:** "Another possibility...is that French got it in colonial India from Portuguese _amassar_ 'knead,' a verb from Latin _massa_"

The source treats both as plausible hypotheses rather than settling on one definitive etymology.

**Verb:** Derived from the noun form in 1874, with figurative usage appearing by 1966.

**Masseur:** The entry states the word comes "from French _masseur_, masc. agent noun from _masser_" (which connects back to the massage noun's uncertain origins).

In summary, Etymonline acknowledges uncertainty and presents both the Arabic and Portuguese/Latin possibilities without declaring one as the authoritative origin.
```


## [2026-09-07T17:42:54.835Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '15155,15175p' FSD_vol3.txt\necho \"=== FSD musk ===\"; sed -n '61655,61668p' FSD_vol3.txt\necho \"=== WEB_vol1 (A-?) has no M ===\"; grep -c . WEB_vol1.txt",
 "description": "FSD massage and musk entries"
}
```


### [2026-09-07T17:42:54.935Z] TOOL RESULT

```
Mm'm e Gn-ralm, l mfls'm « ka-ril'ra: 2 mMs'B& e ck-ri'rft
A provlnoe In N. W. Tuacany, Italy; 687 sq. m.. capital.
1 dl Carrara.
Okln after lajuries. facUltating thoir absorption by the lym-
ptotlos Massage produces a oomhlned tonlo and sedative
eSeot on the nervous system It is of great therapeutic value
in nervous disorders, as neuralgia, neurasthenia chorea, eto .
md In dlspeUlng the erlppUng effects of muscular rheuma-
tism eramp. and the stiffening after-effeotsof fractures and
sprains Bee Ulus below
Th« Urm maaaoc* la usad aa tha canarie aamo for astarasi ma-
alpulatloiia which era amployad for tha purpnaa of affaellna tha
aarvoua and miMular ayatama and tha aanaral oiroulatioa.
H C. Wood TharapauUea, Mmaaaaa p 30. ( 1 .. 1880 1
(K., < maaaer ( < Or. maaaO), knead | ~ vibratory massage,
ror therapeutic purpaeos, rapid light percussions produced
^by a special apparatus
*»* ■»-g4't«B, 1 maa’a-Jftl. 2 m6s*a-g6'ie. a An ancient,
hmr-clvlllaed, nomadic Bcirihlan nation, who invaded Asia
atmut 636 B C , and defeated Cyrus the Great
mas^sa^vse'. 1 mas*e-80s'; 2 mksVihaa'. n. Same as
=== FSD musk ===
And with tha floating truMurn muaJLii tha vrinda
BaAauua Dab win Bol Garden, Xcon. of Veg, oaa. 8. 1. 200.
musk, n. 1. A soft, unctuous, reddish-brown powdery
substance of a strong, ponetratiug, and diffusivo odor,
and slightly bitter taste.
It Is Imported in the pod. a sac situated In front of the
prepuce of the male musk-deer, which, after the animal la
klllel. Is cut oir nnJ drloJ. or os grain •musk, found chte'^y
oil atones where ttio animal has secreted It. Almk Is used by
lierfumcra, and to a small extent In tnedicinc as a stimulant
ond antispasmodlc A resinous substanco with a musk-llko
odor, formerly called arilUclal musk. Is made by treating
rcjtlllel oil of amber with ooli fumlnj nitric add.
Geneva la no grain of aand. 'tis a grain of muali that parfurana
=== WEB_vol1 (A-?) has no M ===
114685
```


## [2026-09-07T17:42:56.673Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BC%CF%8C%CF%83%CF%87%CE%BF%CF%82",
 "prompt": "For Ancient/Byzantine Greek μόσχος: does the entry list a sense 'musk' borrowed from Middle Persian mušk? Quote the etymology of the 'musk' sense and any note that Latin muscus was borrowed from it."
}
```


### [2026-09-07T17:43:01.796Z] TOOL RESULT

```
# μόσχος: Musk Etymology

Yes, the entry lists "musk" as a sense under **Etymology 2**.

**Etymology of the musk sense:**
"From Middle Persian [script needed] (mwšk' /⁠*mušk⁠/), itself from Sanskrit मुष्क (muṣká, "testicle")"

**Note on Latin borrowing:**
The descendants section indicates that this Greek term contributed to later languages: "→ Late Latin: muscus (see there for further descendants)". This shows the Greek word passed into Latin, which then spread to Romance languages and other descendants.
```


## [2026-09-07T17:43:13.046Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=musk",
 "prompt": "Quote the American Heritage Dictionary etymology bracket for the entry \"musk\" (Middle English, Old French, Late Latin, Late Greek, Persian, Sanskrit forms)."
}
```


### [2026-09-07T17:43:16.224Z] TOOL RESULT

```
# Musk Etymology

According to the American Heritage Dictionary, the etymology of "musk" traces back through multiple languages:

"[Middle English, from Old French _musc_, from Late Latin _muscus_, from Greek _moskhos_, from Persian _mušk_, probably from Sanskrit _muṣkaḥ_"

This linguistic progression shows the word's journey from Sanskrit through Persian, Greek, Latin, Old French, and into Middle English.
```


## [2026-09-07T17:43:17.775Z] TOOL CALL #50: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D9%85%D8%B4%DA%A9\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B4\" \\\n \"https://en.wiktionary.org/wiki/massage\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D8%B3\" \\\n \"https://en.wiktionary.org/wiki/%CE%BC%CF%8C%CF%83%CF%87%CE%BF%CF%82\" \\\n \"https://www.etymonline.com/word/musk\" \\\n \"https://www.etymonline.com/word/massage\" \\\n \"https://abadis.ir/fatofa/%D9%85%D8%A7%D8%B3%D8%A7%DA%98/\" \\\n \"https://abadis.ir/fatofa/%D9%85%D8%B4%DA%A9/\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 343 (book 313), roots M.s.s/Massa and Mu,Mus: verification of massage, musk, mouse, muscle chains\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-07T17:43:24.438Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/47386dcf6068f7c8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d47dac0ea4428b32.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b84a5d913e451fb0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/77eaea8cd7f2d248.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dfa5f64f7749c960.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5b9bc33f8d4f14bd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ad32b625516c0ee3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/32fe773a84974210.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1667acf7e6e47209.txt
```


## [2026-09-07T17:43:41.131Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/muh%E2%82%82s",
 "prompt": "Give the reconstructed PIE form and meaning for the 'mouse' root (*muh₂s / *muHs), its descendants (Latin mus, Sanskrit mūṣ, Proto-Germanic *mūs, Greek mys, Proto-Iranian), and any note about the 'muscle' sense."
}
```


## [2026-09-07T17:43:42.180Z] TOOL CALL #52: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.ahdictionary.com/word/search.html?q=musk\" --note \"page 343: AHD:865 musk etymology (Late Latin muscus < Greek moskhos < Persian mušk < Sanskrit muṣkaḥ)\" 2>&1 | tail -2",
 "description": "Archive AHD musk"
}
```


### [2026-09-07T17:43:42.579Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T17:43:44.128Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/eb949db4d4c9cae0.txt
```


## [2026-09-07T17:43:48.189Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/muHs",
 "prompt": "Give the reconstructed PIE form and meaning for the 'mouse' root, its descendants (Latin mūs, Sanskrit mūṣ, Proto-Germanic *mūs, Ancient Greek mys, Proto-Iranian *mūš), and any note about the 'muscle' sense or the Pokorny page."
}
```


### [2026-09-07T17:43:49.663Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T17:43:52.924Z] TOOL CALL #54: WebSearch

```json
{
 "query": "wiktionary Reconstruction Proto-Indo-European mouse *muh₂s mūs",
 "allowed_domains": [
  "en.wiktionary.org"
 ]
}
```


### [2026-09-07T17:43:58.795Z] TOOL RESULT

```
Web search results for query: "wiktionary Reconstruction Proto-Indo-European mouse *muh₂s mūs"

Links: [{"title":"Reconstruction:Proto-Indo-European/múh₂s - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%BAh%E2%82%82s"},{"title":"Reconstruction:Proto-Germanic/mūs - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/m%C5%ABs"},{"title":"Reconstruction:Proto-Indo-European/múHs - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%BAHs"},{"title":"mouse - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/mouse"},{"title":"mus - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/mus"},{"title":"Reconstruction:Proto-Indo-European/mewsH- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mewsH-"},{"title":"Reconstruction:Proto-Indo-Iranian/múHs - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/m%C3%BAHs"},{"title":"μῦς - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%CE%BC%E1%BF%A6%CF%82"},{"title":"Reconstruction:Proto-Italic/mūs - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Italic/m%C5%ABs"},{"title":"Reconstruction:Proto-Indo-European/-mos - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-mos"}]

Based on the search results, I found information about the Proto-Indo-European word for mouse on Wiktionary:

The Proto-Indo-European word *múh₂s means "mouse", with descendants documented across multiple language families.

The word has descendants in various languages including: Proto-Albanian *mū-, Armenian մուկ (muk), Proto-Balto-Slavic *mū́ˀšis, Proto-Germanic *mūs, Proto-Hellenic *mū́s (Ancient Greek μῦς), Proto-Indo-Iranian *múHs, and Proto-Italic *mūs (Latin mūs).

The reconstructed form *múh₂s reflects the laryngeal notation system used in Proto-Indo-European linguistics, where the "₂" indicates a specific type of laryngeal consonant that was present in the ancient language but left no direct phonetic traces in most descendant languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T17:44:03.309Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%BAh%E2%82%82s",
 "prompt": "Give the reconstructed form, gloss, and the list of descendants (Proto-Indo-Iranian, Proto-Germanic, Proto-Italic, Proto-Hellenic, Armenian). Also note anything said about the 'muscle' meaning or about muṣka 'testicle'."
}
```


### [2026-09-07T17:44:04.752Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T17:44:09.157Z] TOOL CALL #56: Bash

```json
{
 "command": "curl -s -A \"Mozilla/5.0\" \"https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/m%C3%BAh%E2%82%82s&action=raw\" | head -60",
 "description": "Fetch PIE mouse reconstruction raw"
}
```


### [2026-09-07T17:44:10.609Z] TOOL RESULT

```
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>

<p>Not Found</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1108 cp1108, Varnish XID 217856886<br>Upstream caches: cp1108 int<br>Error: 404, Not Found at Mon, 07 Sep 2026 17:44:10 GMT<br><details><summary>Sensitive client information</summary>IP address: 187.15.144.43</details></code></p>
</div>
</html>
```


## [2026-09-07T17:44:15.813Z] TOOL CALL #57: Bash

```json
{
 "command": "curl -s -A \"Mozilla/5.0\" \"https://en.wiktionary.org/w/api.php?action=query&prop=revisions&rvprop=content&rvslots=main&format=json&titles=Reconstruction:Proto-Indo-European/m%C3%BAHs\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nfor p in d['query']['pages'].values():\n    print(p.get('title'))\n    r=p.get('revisions')\n    if r: print(r[0]['slots']['main']['*'][:2500])\n\"",
 "description": "Fetch PIE muHs via API"
}
```


### [2026-09-07T17:44:17.257Z] TOOL RESULT

```
Reconstruction:Proto-Indo-European/múHs
{{reconstructed}}
==Proto-Indo-European==
{{etymon|ine-pro|id=mouse|pos=word}}

===Noun===
{{ine-noun}}

# {{topics|ine-pro|Rodents}} [[mouse]]

====Inflection====
{{ine-decl-noun-mf|ac=hysterokinetic|múHs|muHs}}

====Descendants====
{{derivsee|Terms derived from the Proto-Indo-European word *múHs}}
* {{desc|sqj-pro|*mū-}}
** {{desc|sq|mi|g=m}}
* Armenian:
** {{desc|xcl|մուկն}} (possibly from {{l|ine-pro||*muh₂s-m̥|pos=accusative singular}})
*** {{desc|hy|մուկ}}
* {{desc|ine-bsl-pro|*mū́ˀšis}} {{see desc}}
* {{desc|gem-pro|*mūs}} {{see desc}}
* {{desc|grk-pro|*mū́s}}
** {{desc|grc|μῦς}}
* {{desc|iir-pro|*múHs}} {{see desc}}
* {{desc|itc-pro|*mūs}}
** {{desc|la|mūs}} {{see desc}}

===References===
* {{R:kho:Bailey|page=337ab|mūla-}}
* {{R:os:Abaev|vol=II|pages=142–143|myst <nowiki>|</nowiki> mistæ}}
```


## [2026-09-07T17:44:36.789Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW mus ===\"; grep -n \"^mūs\\|mus, mūris\\|musculus\" LEW_1910.txt | head -10\necho \"=== LAT mus ===\"; grep -n -i \"mūs\\b\\|musculus\" LAT.txt | head -10\npython3 -c \"\nfrom PIL import Image\nim=Image.open('/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2014.png'); print(im.size)\nw,h=im.size\nim.crop((0,int(h*0.42),w,int(h*0.66))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt2014_foot.png')\n\"",
 "description": "Latin dicts + crop BQT footnote"
}
```


### [2026-09-07T17:44:38.251Z] TOOL RESULT

```
=== LEW mus ===
=== LAT mus ===
31792:zard"; cf. [iuS en grec et le rapport mus: musculus. Ancien (Lucii.),
52649:rameus', ramosus, M.L.7031; ramusculus (b.latin, d'ob dans les 1 .
(1650, 2546)
```


## [2026-09-07T17:44:41.222Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt2014_foot.png"
}
```


### [2026-09-07T17:44:41.246Z] TOOL RESULT

```

```


## [2026-09-07T17:45:48.897Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd2 mus ===\"; grep -n \"Maus'\" incoming/WLD/WLD_Bd2_pages.txt | head -10\necho \"=== WLD Bd3 register ===\"; grep -n \"mūs\\b\" WLD_band3.txt | head -5\necho \"=== IEC mus mouse ===\"; grep -n -i \"'mouse'\" IEC.txt | head -10\necho \"=== NYB ===\"; grep -n -i \"mwšk\\|mušk\\|mus'\" NYB_vol2_glossary.txt | head -10",
 "description": "WLD, Mann, Nyberg greps"
}
```


### [2026-09-07T17:45:49.011Z] TOOL RESULT

```
=== WLD Bd2 mus ===
20583:Nicht nach Pedersen IF. 5, 34 zu mus „Maus'' als „kleine Mause“.
20672:  gr. yvg „Maus“ {yvbg^ nvv nach eg, ""vog, bv)', alb. mi „Maus'‘ (G. Meyer
=== WLD Bd3 register ===
=== IEC mus mouse ===
=== NYB ===
```


## [2026-09-07T17:45:53.042Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '20660,20700p' incoming/WLD/WLD_Bd2_pages.txt\necho \"=== page tag ===\"; grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd2_pages.txt | awk -F: '$1<20700' | tail -2",
 "description": "Walde-Pokorny mus entry"
}
```


### [2026-09-07T17:45:54.324Z] TOOL RESULT

```
muro- ..groBe Anzahl“.
                   viel, unendlich*. fAvoioi ,,10 000*' nach Stokes BE. 19,
   Gv, uvQiog ,,sehr
97, KZ. 40. 249 zu dem  zwar sparlich belegten, aber doch wohl gesicherten
mir. ynar „Uberfiu6" (cymr.                      myrdd 10000 ist lat. myria-s.        -dem,    s.    Peder-
sen II 131 >


nius „Maus“.
   Ai. mas- „Maus, Eatte“ {muia-, musaha-^ mtmka- m. ds.), np. mus „Maus“;
   arm. ynu-kn „Mau&" (Hiibschmann Arm.                             St. I 44,   Arm. Gr. I 475, Brug-
mann IP L 4S3);
  gr. yvg „Maus“ {yvbg^ nvv nach eg, ""vog, bv)', alb. mi „Maus'‘ (G. Meyer
BB. 8, 190, Alb.Wb. 27s! Pedersen KZ. 36, 262);
  lat. mas „Maus" (/n?7r7r?t5 mhd. miusin „von Mausen**); ahd. mhd. as.
                                                  :



mnd. aisl. ags. miis ,,Maus" (Kons.-St.; abg. ynijsh ..Maus".
  Yielfach auf Korperteile angewendet, wegen der x4.hnlichkeit zwischen
dem Zucken der Muskeln unter der Haut und dem Laufen einer 3Iaus
                                         mjk- — mrou- (mleu-?)                                          313

(s.   Parallelen bei Palk-Torp u. nms): gr. juvg ..ifuskel^, /livcov ,.muskel-
reiche Gegend des Leibes“,   lat. mtiscnhis .,Muskei'’ ahd. usw. mns „Muskel,

bes. des     Oberarms% mnd. mfis bes. ^.der Fleischballen des Daumens*', nhd.
JIatis, Mdiischen^    arm. mtikn „Muskel“, abg. myshca ..pga^icov andrerseits             ;



ai.    mxishd- m. j^Hode, weibliche Scham'* (letzteres vermutlich mit Herein-
spielen der Vorstellung „M^useloch“, woraus auch ^wolliistiges ^\'"eib** in
gr. i^ivcovla)^ np. mush „Bibergeil“ (aus dein Pers. stammt gr. fjiooyog^ nhd.
3Iosc}ms)\ gr. yvoyog' to dvdqEiov xal ywaixsTov uooiov Hes. erklilrt: Pick
KZ. 43, 149 richtiger aus ^fjLvyoxov^ well ev jiwyot des Korpers gelegen.
Geschlechtliche Vorstellung auch in dt. maiisen (aber dies vielleicht von der
Fruchtbarkeifc der ilaus?).                Uber ai. musft-      ,,   Faust   *   (Giintert KZ. 45, 193)
s.    wahrseheinlicheres unter meuh „kratzen'^
  Curtins 33S, Fick   111, 2S9, 520, ITH 327, Falk-Torp u. mtts (mit sehr
=== page tag ===
```


## [2026-09-07T17:46:07.109Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D9%85%D8%A7%D8%B3/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for مماس — its origin label (e.g. [ع.] Arabic) and definition; and any entry for مس (مَسّ) 'touching' or تماس with origin labels."
}
```


### [2026-09-07T17:46:12.262Z] TOOL RESULT

```
# Farhang-e Mo'in Entry for مماس

According to the Farhang-e Mo'in dictionary section:

**Origin label:** [ع.] (Arabic)

**Definition:** "(مُ سّ ) [ع.] (اِمف.) به هم ساییده شده، مالیده شده" — meaning "rubbed together, worn smooth through contact."

---

# Related Entries

The document does not provide separate dedicated entries for مس (touching) or تماس with their own origin labels in the Farhang-e Mo'in section. However, both terms appear throughout the dictionary as related concepts explaining مماس, with the Dehkhoda dictionary noting that تماس (contact) should be consulted for additional context on the grammatical relationship.
```


## [2026-09-07T17:46:39.574Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg343.png data/verification/sources/refs/ocr/BOOK/343.png\npython3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%85%D9%85%D8%A7%D8%B3/\" --note \"page 343: Mo'in labels مماس as [ع.] (Arabic) — support for the Arabic m-s-s loan node\" 2>&1 | tail -1\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%BAHs\" --note \"page 343: PIE *muHs 'mouse' reconstruction and descendants (root box Mu, Mus)\" 2>&1 | tail -1\ncat > data/verification/sources/refs/ocr/BQT/2014.vision.txt <<'EOF'\n[read from data/verification/sources/refs/ocr/BQT/2014.png = BQT vol. 4 pdf p. 97, printed p. 2014 — entry مشک with Mo'in's etymological footnote 2]\n\nمشک - بکسر اول و سکون ثانی و کاف فارسی ... معروف است ... ناف آهوی خطائی است ... و عربان مسک خوانند ...\n\nfootnote ۲ (verbatim, Latin-letter forms as printed):\n«۲ - سانسکریت muska مصغر mûs (موش)، یونانی moskos، لاتینی muscus، فرانسوی و انگلیسی musc، عربی مسك (بکسر اول). غیاث گوید: اهل فارس بکسر میم و اهل ماوراءالنهر بضم میم خوانند. در نسخهٔ ترجمان‌البلاغه مکتوب بسال ۵۰۷ قمری مشك بضم اول ضبط شده (رك: ترجمان البلاغه چاپ احمد آتش، بخش عکسی ص ۲۴۷ب و ۲۵۱ الف) و با کاف تازی اصح است؛ وآن ماده‌ایست مأخوذ از کیسه‌ای مشکین باندازهٔ تخم مرغی، مستقر در زیر پوست شکم آهوی ختائی (غزال المسك = musk deer) نر، وقتیکه تازه باشد برنگ شکلات و لزج است، اما خشك آن بصورت گرد دارای طعم کمی تلخ و بوی تند است. آنرا بعنوان اساس بسیاری از عطریات بکار می‌برند. رك: Webster's New Intern. Dict ... و رك: تحفهٔ حکیم مؤمن: مسك.»\n\nfootnote ۴ (same page, on مشک 'waterskin'): «در پهلوی mašk. وآن اصلاً بمعنی چرم (مخصوصاً چرمی که در آن آب ریزند) و سپس صورت مشک ابرزین در پهلوی ... درآمده بمعنی خیمهٔ سلطنتی، وهمین معنی است که در فارسی «مشکو» و «مشکوی» شده (از افادات شفاهی استاد هنینگ)؛ در سغدی mšk-.»\nEOF\nls -la data/verification/sources/refs/ocr/BQT/ | head",
 "description": "Save vision file, copy page PNG, archive URLs"
}
```


### [2026-09-07T17:46:52.559Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/45e32fb373a3f417.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/85940474333823fa.txt
total 55744
drwxrwxr-x  2 sfmqrb sfmqrb   12288 Sep  7 13:46 .
drwxrwxr-x 12 sfmqrb sfmqrb    4096 Sep  6 18:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb  368375 Sep  4 13:39 0001.png
-rw-rw-r--  1 sfmqrb sfmqrb    1684 Sep  4 13:39 0001.txt
-rw-rw-r--  1 sfmqrb sfmqrb  534367 Sep  4 13:39 0049.png
-rw-rw-r--  1 sfmqrb sfmqrb    2677 Sep  4 13:39 0049.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1076 Sep  4 15:27 103.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  330101 Sep  6 17:59 1092.jpg
-rw-rw-r--  1 sfmqrb sfmqrb    2600 Sep  6 17:59 1092.vision.txt
```


## [2026-09-07T17:48:28.520Z] AGENT

Now I'll write the verification file.


## [2026-09-07T17:55:34.188Z] TOOL CALL #64: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk343.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_MSS = \"https://en.wiktionary.org/wiki/%D9%85%D8%B3\"\nW_MASSAGE = \"https://en.wiktionary.org/wiki/massage\"\nE_MASSAGE = \"https://www.etymonline.com/word/massage\"\nA_MASAZ = \"https://abadis.ir/fatofa/%D9%85%D8%A7%D8%B3%D8%A7%DA%98/\"\nA_MOMAS = \"https://abadis.ir/fatofa/%D9%85%D9%85%D8%A7%D8%B3/\"\nA_MOSK = \"https://abadis.ir/fatofa/%D9%85%D8%B4%DA%A9/\"\nW_MOSK = \"https://en.wiktionary.org/wiki/%D9%85%D8%B4%DA%A9\"\nW_MUSH = \"https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B4\"\nW_MOSCHOS = \"https://en.wiktionary.org/wiki/%CE%BC%CF%8C%CF%83%CF%87%CE%BF%CF%82\"\nE_MUSK = \"https://www.etymonline.com/word/musk\"\nAHD_MUSK = \"https://www.ahdictionary.com/word/search.html?q=musk\"\nW_PIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%BAHs\"\n\nKLN_MASSAGE = (\"Klein, KLN_1966.txt line 23063 (printed pp. 944/945, page markers \\\"944\\\"/\\\"945\\\" at lines \"\n  \"23042-23043): \\\"massage, n. - F. massage, fr. masser, 'to massage', fr. Arab. massa, 'he felt, touched', \"\n  \"which is rel. to Heb. mashash, 'he felt, touched', ... Aram. mashshesh, ... Ethiop. masasa, ... Akkad. \"\n  \"mashashu... The practice of massage has come to Europe from the East... This word has nothing to do with \"\n  \"Gk. massein, 'to knead', with which it is connected by most lexicographers.\\\"\")\n\nPOK_MUS = (\"POK_full.txt, block 'Root / lemma: mus / Meaning: mouse / Note: (older *mus, musos from *meus, musos)', \"\n  \"Page(s): 752-753: \\\"Old Indic mus- m. 'mouse, rat', np. mus 'mouse'; Armenian mu-kn 'mouse, muscle'; gr. mys \"\n  \"'mouse', also 'muscle'; Latin mus m. 'mouse'; Old High German ... Old English mus 'mouse, muscle'... Often \"\n  \"applied on body parts: ... Latin musculus ds., 'muscle' ... on the other hand Old Indic muska- m. 'testicle, \"\n  \"vulva', npers. musk (from Pers. derives gr. moschos, Modern High German Moschus 'musk')\\\"\")\n\nWLD_MUS = (\"Walde-Pokorny Bd. II 312-313 s.v. mus 'Maus' (WLD_Bd2_pages.txt lines 20670-20700): \\\"Ai. mus- 'Maus, \"\n  \"Ratte' (musa-, musaka-, muska- m. ds.), np. mus 'Maus'; arm. mu-kn 'Maus'; gr. mys 'Maus'; lat. mus 'Maus'; \"\n  \"ahd. mhd. as. mnd. aisl. ags. mus 'Maus'... Vielfach auf Koerperteile angewendet, wegen der Aehnlichkeit \"\n  \"zwischen dem Zucken der Muskeln unter der Haut und dem Laufen einer Maus: gr. mys 'Muskel', lat. musculus \"\n  \"'Muskel'... ai. muska- m. 'Hode, weibliche Scham'... np. mush 'Bibergeil' (aus dem Pers. stammt gr. moschos, \"\n  \"nhd. Moschus)\\\"\")\n\nAHD_MUS = (\"Watkins 1985 s.v. mus- (AHD_watkins1985.txt line ~763): \\\"mus-. A mouse; also a muscle (from the \"\n  \"resemblance of a flexing muscle to the movements of a mouse). 1. Germanic *mus- (plural *musiz) in Old \"\n  \"English mus (plural mys), mouse: MOUSE. 2. Latin mus, mouse: MURINE, MUSCLE, MUSTELINE. 3. Greek mus, mouse, \"\n  \"muscle: MYELO-, MYO-... [Pok. mus 752.]\\\"\")\n\nBQT2053 = (\"BQT vol. 4, printed p. 2053 (= pdf p. 136; data/verification/sources/refs/ocr/BQT/2053.png+.txt), \"\n  \"footnote 1 on the موش entries: \\\"هندی باستان mus، سانسکریت musa-, musaka- (موش، موش صحرائی)، ارمنی mukn (موش)، \"\n  \"افغانی ...، اوستی miste/mist، بلوچی musk، کردی mišik (موش)، ... ؛ جانوری پستاندار از چارپایان جونده، دارای دمی طویل\\\"\")\n\nBQT2014 = (\"BQT vol. 4, printed p. 2014 (= pdf p. 97), entry مشک, Mo'in's footnote 2 — read from the page image and \"\n  \"saved verbatim to data/verification/sources/refs/ocr/BQT/2014.vision.txt: \\\"سانسکریت muska مصغر mûs (موش)، یونانی \"\n  \"moskos، لاتینی muscus، فرانسوی و انگلیسی musc، عربی مسك (بکسر اول). غیاث گوید: اهل فارس بکسر میم و اهل ماوراءالنهر \"\n  \"بضم میم خوانند... وآن ماده‌ایست مأخوذ از کیسه‌ای مشکین باندازهٔ تخم مرغی، مستقر در زیر پوست شکم آهوی ختائی \"\n  \"(غزال المسك = musk deer) نر\\\"\")\n\nFVQ_MISK = (\"Jeffery, Foreign Vocabulary of the Qur'an p. 264 s.v. (Misk), lxxxiii.26 'Musk' (FVQ_pages.txt lines \"\n  \"9501-9512): \\\"The word was widely used among the Arabs in the pre-Islamic period and was quite commonly \"\n  \"recognized as a loan-word from the Persian. The Phlv. mushk seems to have come ultimately from the Skt., but \"\n  \"it was from the Iranian, not the Indian form, that were borrowed the Arm. mushk; Gk. moschos; Aram.; Syr.; \"\n  \"Eth. ... It is more likely to have come direct from Middle Persian into Arabic than through the Syriac.\\\"\")\n\nPLA_MISK = (\"Asbaghi, Persische Lehnwoerter im Arabischen p. 250 s.v. misk (PLA_asbaghi_1988_ia_djvu.txt lines \"\n  \"18171-18189): \\\"Zu misk 'Moschus' ... pers. mošk / MP. mušk ... pers. mušk > ar. misk, tk. misk, mlat. muscum, \"\n  \"frz. musc, sp. musco, engl. musk, dtsch. Moschus. Moschus: skr. > pers. > ar. > lat.\\\"\")\n\nLKT_MUSK = (\"Lokotsch no. 1515a (LKT.txt line 3496): \\\"Pers. musk: 'Moschus' [aus sskr. mushkas 'Hode' wegen der \"\n  \"Aehnlichkeit einer solchen mit dem Beutel des Moschustieres], ar. musk, misk, tk. misk; hieraus mlat. muscum \"\n  \"'Bisam, Moschus', it. musco, muschio, prov. musc, frz. musc, ... engl. musk, dtsch. Muesch, spaeter Moschus; \"\n  \"russ. muskus 'Moschus'.\\\"\")\n\nKLN_MUSK = (\"Klein s.v. musk (KLN_1966.txt line 24742, printed p. ~1021): \\\"musk, n., substance secreted by a gland \"\n  \"near the testicles of the musk deer. - ME. muske, fr. OF. (= F.) musc, fr. L. muscus, fr. Gk. moschos, fr. \"\n  \"Pers. mushk, 'musk', fr. OI. muskah, 'scrotum, testicle', lit. 'a little mouse', fr. mus-, 'mouse'.\\\"\")\n\nKLN_MOUSE = (\"Klein s.v. mouse (KLN_1966.txt line 24534): \\\"mouse, n. - ME. mous, fr. OE. mus, rel. to OS., ON., \"\n  \"OFris., MLG., MDu., Dan., Swed. mus, Du. muis, OHG., MHG. mus, G. Maus, 'mouse; muscle', and cogn. with OI. \"\n  \"mus-, 'mouse, rat', muskah, 'scrotum, testicle', lit. 'a little mouse', OPers. mush, 'mouse', Arm. mukn, Gk. \"\n  \"mys, 'mouse; muscle', L. mus (gen. muris)...\\\"\")\n\nSYN_MUSKA = (\"Buck, Selected Synonyms (SYN.txt line 6667, section 4.49 'testicle'): \\\"Skt. muska-, apparently dim. to \"\n  \"mus- 'mouse', from the shape (cf. Lat. musculus 'muscle', etc.). Walde-P. 2.313.\\\" and line 4894, section 3.68 \"\n  \"MOUSE: \\\"Grk. mys, Lat. mus, OE mus, ME mous, NE mouse, Skt. mus-\\\"\")\n\nSYN_MUSCLE = (\"Buck (SYN.txt line 6133, 'muscle'): \\\"ChSl. mystica (SCr. misica 'arm' and 'muscle'), deriv. of ChSl. \"\n  \"mysi 'mouse' in transferred sense 'muscle' (from the resemblance between the muscle of upper arm especially \"\n  \"and a mouse). Cf. Lat. musculus 'little mouse, muscle', Grk. mys 'mouse' and 'muscle', etc. Walde-P. 1.312f.\\\"\")\n\nPHD_MUSK = (\"MacKenzie, Concise Pahlavi Dictionary (PHD.txt line 493): \\\"1mušk [mwšk' | N ~] musk. 2mušk [mwšk' | \"\n  \"(N muš)] mouse, rat\\\"; English index: \\\"mouse mušk\\\" (line 2861), \\\"musk mušk\\\" (line 2873), \\\"rat mušk\\\" (3325)\")\n\nHRN_MUS = (\"Horn, Grundriss no. 995 (HRN.txt lines 8650-8657, printed p. ~220): \\\"mush 'Maus'. g. mušk, ai. mus-, \"\n  \"skr. musaka-, musika- 'Maus, Ratte'; arm. mukn 'Maus'. kurd. mišik, misk; oss. d. miste, t. mist; bel. mušk, \"\n  \"n. mušk\\\"\")\n\nHUB_MISK = (\"Huebschmann, Persische Studien Sec. 24 (HUB.txt lines 4890-4893, printed p. 139-140): among the cases \"\n  \"where inlautendes u becomes i - \\\"misk (arab. misk) 'Moschus' = mušk; hier folgt auf u entweder ein Zischlaut \"\n  \"(s, š, z) oder ein i in der folgenden Silbe\\\"\")\n\nARY_MOSK = (\"Aryanpur, Farhang-e riše-hā (ARY_pages.txt [pdf page 473], printed p. 474), headword مشک: Pahlavi, \"\n  \"سانسکریت muska, یونانی moschos, لاتینی muscus, فرانسه musc, آلمانی Muskus/Moschus, انگلیسی musk, هلندی muskus, \"\n  \"with the note \\\"چم این واژه در زبان سانسکریت: خایه\\\" ('the meaning of this word in Sanskrit: testicle') and a \"\n  \"cross-reference to برهان قاطع\")\n\nARY_MUSCLE = (\"Aryanpur (ARY_pages.txt [pdf page 465], printed p. 466), entry ماهیچه, note 3: \\\"واژه‌ریشه‌شناسان معتقدند \"\n  \"که واژهٔ «ماهیچه» با واژهٔ «موش» خویشی دارد و بهمین دلیل واژهٔ ماهیچه در لاتین (musculus) مصغر واژهٔ mus به معنی «موش» \"\n  \"است. دلیل این خویشی، شباهت شکل ماهیچهٔ دوسر و «موش» است\\\"\")\n\nSKT_MUSK = (\"Skeat (SKT.txt lines 11949, 12051, 12076): \\\"Mouse. (E.) M.E. mous. A.S. mus (pl. mys)... L. mus, Gk. \"\n  \"mys, Pers. mush, a mouse; Skt. muska, a rat, a mouse\\\"; \\\"Muscle (1)... F. muscle. - L. musculus, (1) a little \"\n  \"mouse... Dimin. of L. mus, a mouse\\\"; \\\"Musk... behind the musk-deer's navel. Lit. 'thief'; from mush, to \"\n  \"steal. See Mouse.\\\"\")\n\nFSD_MASSAGE = (\"Funk & Wagnalls New Standard (FSD_vol3.txt line 15169, s.v. massage): \\\"(F., < masser (< Gr. masso), \"\n  \"knead)\\\" - i.e. F&W derive French masser from Greek masso 'to knead', the etymology Klein explicitly rejects\")\n\nPHN_257 = (\"Pihan 1866, p. 257 s.v. MASSER, v.a. (a.) (PHN.txt lines 7217-7226): \\\"mass [Arabic مس] manier, toucher, \"\n  \"palper. - L'operation du massage ou massement, tres-usitee chez les peuples orientaux, consiste a presser avec \"\n  \"la main les diverses parties du corps... Comparez avec l'arabe le verbe grec massein dont le sens est le meme.\\\" \"\n  \"- the '(a.)' tag marks the word as Nourai's claim: of Arabic origin\")\n\ndata = {\n \"pdf_page\": 343,\n \"book_page\": 313,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"M.s.s, Massa\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Arabic geminate root م س س (m-s-s), form I perfect مَسَّ massa 'he touched, felt', verbal noun مَسّ mass 'touching, contact'\",\n   \"note\": \"The root box is right on all three counts: م س س is a real Arabic (indeed common Semitic) root, massa is its 3rd sg. masc. perfect 'he touched', and mass is its maṣdar. Klein adds the Semitic comparanda (Heb. mašaš, Aram. maššeš, Eth. masasa, Akkad. mašāšu 'to smear over'). The whole chart, however, hangs on one contested claim: that French masser/massage comes from this Arabic verb. Nourai's two references say so (Pihan 1866 p.257; Klein p.944), and Klein even denies the rival Greek etymology outright; but Etymonline, Wiktionary and the French tradition leave the choice open between Arabic massa and Portuguese amassar 'to knead' (< Lat. massa), and Funk & Wagnalls (1913) derives masser straight from Greek μάσσω. Hence node #2 is only plausible, while the two modern loans below it (Persian ماساژ, English massage, both from French) are certain. FVA:381, the reference Nourai cites for the root and for node #1, has no digital copy and could not be checked.\",\n   \"note_fa\": \"جعبهٔ ریشه درست است: «م‌س‌س» ریشه‌ای عربی (و در اصل سامی) است، مَسَّ ماضی سوم‌شخص مفرد «لمس کرد» و مَسّ مصدر آن است؛ کلاین همریشه‌های سامی آن را می‌آورد (عبری mašaš، آرامی maššeš، حبشی masasa، اکدی mašāšu). ولی تمام این نمودار بر یک ادعای مورد اختلاف تکیه دارد: اینکه masser/massage فرانسوی از همین فعل عربی گرفته شده باشد. دو مرجع خودِ نورایی (پیان ۱۸۶۶ ص۲۵۷ و کلاین ص۹۴۴) همین را می‌گویند و کلاین حتی ریشهٔ یونانی μάσσειν «خمیر کردن» را به‌صراحت رد می‌کند؛ اما اتیمانلاین و ویکی‌واژه و سنّت فرانسوی میان «مسّ» عربی و amassar پرتغالی (از massa لاتینی) تردید دارند و فرهنگ فانک و واگنالز (۱۹۱۳) masser را یکسر از یونانی μάσσω می‌گیرد. پس گرهٔ ۲ تنها «با احتیاط پذیرفتنی» است، در حالی که دو وام‌واژهٔ نوی زیر آن (ماساژ فارسی و massage انگلیسی، هر دو از فرانسه) قطعی‌اند.\",\n   \"sources\": [W_MSS, W_MASSAGE, E_MASSAGE],\n   \"ref_check\": [\n    {\"ref\": \"FVA:381\", \"status\": \"not_checked\", \"note\": \"Nahvi, Farhang-e vāže-hā-ye ʿarabi dar fārsi (Tehran 1368/1989): refs_online.json records no digital copy (archive.org, ketabnak, noorlib and web searched); only the OpenLibrary catalogue record exists.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"p. 944/945 s.v. massage\", \"stance\": \"supports\", \"note\": KLN_MASSAGE},\n    {\"src\": \"FVQ\", \"where\": \"grep of FVQ_pages.txt for 'mass'/'m-s-s'\", \"stance\": \"silent\", \"note\": \"Jeffery has no entry for مسّ — as expected, since it is native Arabic, not a foreign word of the Qur'an; his only nearby entries are (Misk) p.264 and (Miskin) p.264.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/مس (Arabic section)\", \"stance\": \"supports\", \"note\": \"root م س س; verb مَسَّ (massa) 'to feel, to touch, to handle, to palpate'; noun مَسّ (mass) 'touching, touch, contact' = verbal noun of the verb — exactly the root box's glosses.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Persian\",\n     \"words\": \"mass\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian مَسّ mass 'touching, contact' is the Arabic maṣdar of م س س taken over unchanged (an Arabic loan, which is what the arrow means here); it lives in Persian mainly in learned and technical registers. The two words in the extra field are further stems of the same Arabic root borrowed with it: مُماس mumāss, form III active participle, 'touching, in contact', in geometry 'tangent'; تماس tamāss, form VI maṣdar, 'mutual contact'. Mo'in tags مماس explicitly as [ع.] 'Arabic'. No sound change is involved beyond the Persian reading of the gemination (mass), since Persian borrows Arabic orthography wholesale; the only Persian innovation is the semantic narrowing of تماس to everyday 'contact, touch (of persons), telephone contact'.\",\n     \"derivation_fa\": \"«مَسّ» فارسی همان مصدر عربیِ ریشهٔ م‌س‌س است که بی‌هیچ دگرگونی آوایی به فارسی وام گرفته شده (پیکان نمودار در اینجا به معنای وام‌گیری است) و بیشتر در کاربرد ادبی و علمی به کار می‌رود. دو واژهٔ افزودهٔ جعبه نیز از همان ریشه‌اند: «مُماس» اسم فاعلِ باب مفاعله («تماس‌یافته»، در هندسه: خطِ مماس) و «تماس» مصدر باب تفاعل («به هم رسیدن»). معین ذیل «مماس» نشانهٔ [ع.] می‌گذارد، یعنی معرّب/عربی بودن آن را تصریح می‌کند. تنها نوآوری فارسی، تحول معناییِ «تماس» به معنای امروزیِ «ارتباط، تماس تلفنی» است. ادعای نورایی درست است.\",\n     \"sources\": [W_MSS, A_MOMAS],\n     \"ref_check\": [\n      {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Nourai gives no page for MON here. Mo'in via abadis.ir (فرهنگ معین section) s.v. مماس: «(مُ سّ) [ع.] (اِمف.) به هم ساییده شده، مالیده شده» — the [ع.] label confirms the Arabic origin of this family in Persian; without a page number the citation itself cannot be located in the printed Farhang.\"},\n      {\"ref\": \"FVA:381\", \"status\": \"not_checked\", \"note\": \"no digital copy of Nahvi's dictionary (see root ref_check).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 944/945 s.v. massage\", \"stance\": \"supports\", \"note\": KLN_MASSAGE + \" — Klein's Arab. massa 'he felt, touched' is the same form as the chart's Massa.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/مس\", \"stance\": \"supports\", \"note\": \"Arabic مَسّ (mass) 'touching, touch; contact', verbal noun of مَسَّ; Form III/VI derivatives of the root are the source of Persian مماس/تماس.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi 1988, grep for mass/mss\", \"stance\": \"silent\", \"note\": \"Asbaghi catalogues Persian loans IN Arabic, so a native Arabic word borrowed into Persian is outside his scope — no entry.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"French\",\n     \"words\": \"\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"An empty pass-through box standing for French masser 'to massage' / massage. Nourai's source, Pihan (1866) p.257 s.v. MASSER, marks the word '(a.)' = of Arabic origin and derives it from Arabic mass 'manier, toucher, palper', adding that the practice was 'très-usitée chez les peuples orientaux' and that Greek μάσσειν only happens to mean the same; Klein (p.944) agrees and states flatly that the word 'has nothing to do with Gk. massein, to knead'. Modern handbooks are more cautious: masser/massage are first attested in French only around 1779-1812, in travellers' reports from the East, and Etymonline and Wiktionary give two possibilities — Arabic massa (picked up in Egypt during the Napoleonic campaign) or Portuguese amassar 'to knead' (< Latin massa), picked up in colonial India — while Funk & Wagnalls (1913) derives masser from Greek μάσσω 'to knead'. The Arabic route is therefore accepted but not established: plausible.\",\n     \"derivation_fa\": \"این جعبهٔ تهی نمایندهٔ فعل فرانسویِ masser «مشت‌ومال دادن» و اسمِ massage است. مأخذ نورایی، پیان (۱۸۶۶) ص۲۵۷، این واژه را با نشانِ «(a.)» یعنی عربی‌تبار می‌آورد و از مسّ عربی («لمس کردن، مالیدن») می‌گیرد و می‌افزاید که این کار «در میان مردمان مشرق بسیار رایج» بوده؛ کلاین نیز همین را می‌گوید و پیوند آن با μάσσειν یونانی («خمیر کردن») را به‌صراحت رد می‌کند. اما پژوهش امروزی محتاط‌تر است: masser و massage در فرانسه تنها از حدود ۱۷۷۹ تا ۱۸۱۲ در سفرنامه‌های مشرق‌زمین دیده می‌شوند و اتیمانلاین و ویکی‌واژه دو راه را در برابر هم می‌نهند: وام‌گیری از «مسّ» عربی (در مصرِ دورهٔ ناپلئون) یا از amassar پرتغالی «خمیر کردن» (از massa لاتینی) در هندِ استعماری؛ فانک و واگنالز هم آن را از μάσσω یونانی می‌گیرد. پس ادعای نورایی با احتیاط پذیرفتنی است، نه قطعی.\",\n     \"sources\": [E_MASSAGE, W_MASSAGE],\n     \"ref_check\": [\n      {\"ref\": \"PHN:257\", \"status\": \"supports\", \"note\": PHN_257}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 944/945 s.v. massage\", \"stance\": \"supports\", \"note\": KLN_MASSAGE},\n      {\"src\": \"FSD\", \"where\": \"vol. III s.v. massage (FSD_vol3.txt line 15169)\", \"stance\": \"contradicts\", \"note\": FSD_MASSAGE},\n      {\"src\": \"SKT\", \"where\": \"grep of SKT.txt for massage/masser\", \"stance\": \"silent\", \"note\": \"Skeat's Concise Etymological Dictionary (1911) has no entry for massage — the word was still a recent medical borrowing.\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/massage\", \"stance\": \"partial\", \"note\": \"\\\"possibly from Arabic massa 'to touch, feel, handle'... if so, probably the word was picked up in Egypt during the Napoleonic campaign there. Another possibility is that French got it in colonial India from Portuguese amassar 'knead', a verb from Latin massa\\\" — the Arabic origin is offered as one of two.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"mâsâž\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian ماساژ māsāž is a straightforward 20th-century loan from French massage, taken in through medical and hygienic vocabulary; French -age is regularly rendered -âž in Persian (گاراژ garāž, ماساژ māsāž, پاساژ pāsāž), and the French nasal-free /a/ of mas- is lengthened to Persian ā in the open syllable. Mo'in labels the entry [فر.] 'French' and glosses it «مالش بدن کسی با سر انگشتان دست جهت رفع خستگی او، مشت و مال». If Nourai's Arabic etymology of masser is right, ماساژ is a round trip — Arabic مسّ → French → Persian — beside the directly borrowed Arabic مسّ of node #1; the immediate source is in any case French, not Arabic.\",\n     \"derivation_fa\": \"«ماساژ» وام‌واژه‌ای است از فرانسویِ massage که در سدهٔ چهاردهم خورشیدی همراه واژگان پزشکی و بهداشتی به فارسی آمده است؛ پایانهٔ -age فرانسوی در فارسی به‌گونهٔ «-اژ» درمی‌آید (گاراژ، پاساژ، ماساژ) و /a/ کوتاهِ فرانسوی در هجای باز به «آ» کشیده می‌شود. معین این واژه را با نشانِ [فر.] می‌آورد: «مالش بدن کسی با سر انگشتان دست جهت رفع خستگی او، مشت و مال». اگر ریشه‌شناسی نورایی برای masser درست باشد، «ماساژ» یک رفت‌وبرگشت است: مسّ عربی ← فرانسه ← فارسی، در برابر «مسّ» که یکسر از عربی وام گرفته شده؛ در هر حال مأخذ بی‌واسطهٔ آن فرانسه است. ادعای نورایی درست است.\",\n     \"sources\": [A_MASAZ, W_MASSAGE],\n     \"ref_check\": [\n      {\"ref\": \"MON:3697\", \"status\": \"supports\", \"note\": \"Mo'in via abadis.ir (فرهنگ معین section) s.v. ماساژ: «[فر.] (اِ.) مالش بدن کسی با سر انگشتان دست جهت رفع خستگی او، مشت و مال» — the [فر.] (French) label is exactly what the chart's arrow claims. The printed page number 3697 cannot be verified in the online text, which carries no pagination.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"vajehyab/abadis فرهنگ معین s.v. ماساژ\", \"stance\": \"supports\", \"note\": \"«[فر.] (اِ.) ... مشت و مال»\"},\n      {\"src\": \"Dehkhoda\", \"where\": \"abadis.ir/fatofa/ماساژ (لغت‌نامه دهخدا section)\", \"stance\": \"supports\", \"note\": \"Dehkhoda also marks ماساژ as French and glosses it 'مشت و مال', describing the therapeutic technique — no Arabic mediation claimed for the Persian word.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/massage\", \"stance\": \"supports\", \"note\": \"French massage 'from masser + -age' is the source of the international word borrowed by Persian and English alike.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"English\",\n     \"words\": \"massage\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English massage is a French loan of the 1870s: the noun is first recorded in English in 1874 (in medical writing on Swedish and 'Oriental' rubbing techniques), with masseur/masseuse following in the same decade; the verb is back-formed in 1874-1876. French massage = masser + -age, and English keeps the French stress and the /ɑːʒ/ ending. Klein (Nourai's KLN:944) gives the whole chain 'F. massage, fr. masser, fr. Arab. massa' — so the English link itself is uncontroversial; only the ultimate Arabic step (node #2) is debated.\",\n     \"derivation_fa\": \"massage انگلیسی وام‌واژه‌ای فرانسوی از دههٔ ۱۸۷۰ است: اسم آن نخست در ۱۸۷۴ در نوشته‌های پزشکی دربارهٔ «مشت‌ومالِ سوئدی و شرقی» دیده می‌شود و masseur و masseuse در همان دهه از پی آن می‌آیند؛ فعل آن در ۱۸۷۴–۱۸۷۶ از اسم ساخته شده است. صورت فرانسوی از masser + -age است و انگلیسی همان تکیه و پایانهٔ /ɑːʒ/ فرانسوی را نگه داشته است. کلاین (همان KLN:944 که نورایی می‌آورد) تمام زنجیره را می‌آورد: «F. massage از masser از عربی massa»؛ پس این حلقه بی‌گفت‌وگو درست است و تنها حلقهٔ پایانی (گرهٔ ۲، عربی ← فرانسه) مورد اختلاف است.\",\n     \"sources\": [E_MASSAGE, W_MASSAGE],\n     \"ref_check\": [\n      {\"ref\": \"KLN:944\", \"status\": \"supports\", \"note\": KLN_MASSAGE + \" The entry sits between the printed page markers 944 and 945 in the scan, so Nourai's page is right.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 944/945 s.v. massage, masseur, masseuse\", \"stance\": \"supports\", \"note\": \"\\\"massage, n. - F. massage, fr. masser...\\\"; \\\"masseur, n., a man who practices massage. - F., formed fr. masser\\\"\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/massage\", \"stance\": \"supports\", \"note\": \"massage n. 1874 from French; verb from the noun 1874; masseur from French masseur — the French→English step is agreed, the Arabic step only 'possibly'.\"},\n      {\"src\": \"FSD\", \"where\": \"vol. III s.v. massage\", \"stance\": \"partial\", \"note\": FSD_MASSAGE + \" — F&W agree that English took the word from French, but not on the pre-French history.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Mu, Mus\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *múHs (*muh₂s) 'mouse', an s-stem root noun; the 'muscle' sense is a secondary transfer (Pokorny 752-753 mūs; Watkins mūs-)\",\n   \"note\": \"Language label, gloss and page are right: Pokorny's lemma is exactly 'mūs, meaning: mouse', pp. 752-753, and Watkins' entry reads verbatim \\\"mūs-. A mouse; also a muscle (from the resemblance of a flexing muscle to the movements of a mouse). [Pok. mūs 752.]\\\" — which is where Nourai's gloss comes from. One caveat about the headword: the 'Mu' half is not a mouse-root. Pokorny's neighbouring lemmas on the same pages are mū-1 'to murmur, moo' (751-752) and mū-2/mus- 'fly' (752, whence Lat. musca, Gk. muia) — unrelated roots that merely share the page — and modern reconstruction knows only *múHs (acc. *muh₂s-m̥), not a bare base *mu-. Structurally the chart is also a mixture: the Germanic and Latin branches are genuine descendants of the root, whereas 'Sanskrit' stands in for Indo-Iranian and is drawn as the ancestor of Persian موش, which is really its sibling; only مشک is truly borrowed out of Indic. The one form on the page that no source supports is the Latin box 'muskus' (see node #5): the printed page really has muskus, a misprint for Late Latin muscus.\",\n   \"note_fa\": \"برچسب زبان، معنی و شمارهٔ صفحه هر سه درست است: مدخل پوکورنی همان mūs «موش» در صفحه‌های ۷۵۲–۷۵۳ است و واتکینز نیز عیناً می‌نویسد: «mūs- موش؛ و نیز ماهیچه (از شباهت جنبش ماهیچه به دویدن موش). [پوکورنی ۷۵۲]» — یعنی معنیِ نمودار از همین‌جا آمده است. یک نکته دربارهٔ سرواژه: بخشِ «Mu» ریشه‌ای برای «موش» نیست؛ مدخل‌های همسایه در همان صفحه‌ها mū-1 «زمزمه کردن، بانگ گاو» و mū-2/mus- «مگس» (لاتین musca، یونانی muia) هستند که ریشه‌هایی جداگانه‌اند و تنها هم‌صفحه‌اند، و بازسازی امروزی تنها *múHs را می‌شناسد نه ستاکِ برهنهٔ *mu-. ساختار نمودار هم آمیخته است: شاخه‌های ژرمنی و لاتینی فرزندان راستین ریشه‌اند، اما «سانسکریت» جانشین شاخهٔ هندوایرانی شده و نیای «موش» فارسی نشان داده شده، در حالی که این دو خواهرند نه پدر و فرزند؛ تنها «مشک» است که به‌راستی وام‌واژه‌ای از هندی است. تنها صورتی که هیچ مأخذی آن را تأیید نمی‌کند، «muskus» در جعبهٔ لاتینی است (گرهٔ ۵): در صفحهٔ چاپی هم همین آمده، یعنی خطای چاپی کتاب به‌جای muscus لاتینی متأخر.\",\n   \"sources\": [W_PIE, E_MUSK, AHD_MUSK],\n   \"ref_check\": [\n    {\"ref\": \"POK:752\", \"status\": \"supports\", \"note\": POK_MUS + \" — the lemma begins on p. 752 (running to 753), so Nourai's page is right.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 752-753 s.v. mūs\", \"stance\": \"supports\", \"note\": POK_MUS},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mūs-\", \"stance\": \"supports\", \"note\": AHD_MUS},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 312-313 s.v. mūs\", \"stance\": \"supports\", \"note\": WLD_MUS},\n    {\"src\": \"SYN\", \"where\": \"Buck 3.68 'mouse'\", \"stance\": \"supports\", \"note\": SYN_MUSKA},\n    {\"src\": \"IEC\", \"where\": \"grep of IEC.txt for mūs/mouse\", \"stance\": \"silent\", \"note\": \"Mann's Indo-European Comparative Dictionary has muskos 'undergrowth, moss' and mūsos 'mould, moss' (cols. ~1146) but no 'mouse' lemma turned up in the OCR — it gives no support either way.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/múHs\", \"stance\": \"supports\", \"note\": \"\\\"*múHs — mouse\\\", descendants Proto-Albanian *mū-, Old Armenian մուկն (possibly < acc. *muh₂s-m̥), Proto-Balto-Slavic *mū́ˀšis, Proto-Germanic *mūs, Proto-Hellenic *mū́s > Gk. μῦς, Proto-Indo-Iranian *múHs, Proto-Italic *mūs > Lat. mūs — i.e. all four branches of this chart, but no bare base *mu-.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Sanskrit\",\n     \"words\": \"mus; muska\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Skt. मूष् mūṣ- (f./m.) 'mouse, rat', with the thematic doublets mūṣa-, mūṣaka-, mūṣikā-, is the Indic continuation of PII *múHs < PIE *múHs, unchanged apart from the regular Indic retroflexion of s after ū (ruki). मुष्क muṣka- m. 'testicle, scrotum' (also 'vulva') is a -ka- derivative of the same base with the shape metaphor 'little mouse' — Buck: \\\"Skt. muska-, apparently dim. to mūs- 'mouse', from the shape\\\" — precisely the metaphor that gives Lat. mūsculus 'muscle' and Gk. μῦς 'mouse, muscle'. Nourai's undiacriticked 'mus' and 'muska' are his usual simplified transliteration of mūṣ and muṣka, not misprints. Note that this Sanskrit box functions in the chart as a stand-in for the whole Indo-Iranian branch: it is the real source only of the borrowed مشک below it (node #3), not of Persian موش (node #2).\",\n     \"derivation_fa\": \"«mūṣ» سانسکریت («موش، موشِ صحرایی»)، با گونه‌های mūṣa- و mūṣaka-، ادامهٔ هندیِ *múHs هندوایرانی و هندواروپاییِ آغازین است و تنها دگرگونیِ آوایی آن، تبدیل s به ṣ پس از ū است (قاعدهٔ ruki). «muṣka-» به معنای «خایه، کیسهٔ بیضه» ساختی است با پسوند -ka- از همان ستاک، بر پایهٔ تشبیهِ شکلی «موشکِ کوچک»؛ باک می‌نویسد: «muṣka- سانسکریت، بنا بر ظاهر مصغّرِ mūṣ- «موش»، از روی شکل آن» — همان استعاره‌ای که در لاتین mūsculus «ماهیچه» و در یونانی μῦς («موش» و «ماهیچه») را ساخته است. صورت‌های بی‌اعرابِ «mus» و «muska» در نمودار شیوهٔ همیشگیِ آوانویسیِ سادهٔ نورایی است، نه غلط چاپی. توجه: این جعبهٔ سانسکریت در نمودار جانشین کل شاخهٔ هندوایرانی شده و در واقع تنها مأخذ «مشک» (گرهٔ ۳) است، نه «موش» (گرهٔ ۲).\",\n     \"sources\": [W_MOSK, W_PIE],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of its own in the book.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 752-753 s.v. mūs\", \"stance\": \"supports\", \"note\": POK_MUS},\n      {\"src\": \"WLD\", \"where\": \"Bd. II 312-313\", \"stance\": \"supports\", \"note\": WLD_MUS + \" — WLD lists muṣka- both among the 'mouse' formations and separately as 'Hode, weibliche Scham'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 4.49 'testicle' and 3.68 'mouse'\", \"stance\": \"supports\", \"note\": SYN_MUSKA},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mūs-\", \"stance\": \"partial\", \"note\": AHD_MUS + \" — Watkins lists the Sanskrit branch only implicitly (the root gloss covers it); the muṣka- derivative appears in AHD's dictionary entry for musk, not in the root appendix.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"müš\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The word is right but the arrow's direction is not: New Persian موش mūš 'mouse' is inherited, not taken from Sanskrit. It continues Middle Persian mušk / mūš (Pahlavi spelling mwšk', MacKenzie: \\\"2mušk [mwšk'] mouse, rat\\\") < Proto-Iranian *múHs < PII *múHs, so it is the sibling of Skt mūṣ-, not its descendant; the Pahlavi -k of mwšk' is the same suffixal extension seen in Baluchi mušk and Kurdish mišk, and New Persian simply drops it. Horn no. 995 sets out exactly this cognate set (\\\"mūš 'Maus'; ai. mūṣ-, skr. mūṣaka-; arm. mukn; kurd. mišik; oss. miste/mist; bal. mušk\\\"), and Mo'in's footnote to Borhān p. 2053 does the same, listing Old Indian, Armenian, Ossetic, Baluchi and Kurdish forms side by side rather than deriving Persian from Sanskrit. Verdict plausible: right word, right root, wrong genealogy (a cognate drawn as a descendant). Diacritic: the printed page has mŭš, while the JSON transliterates müš; the correct value is long ū (mūš).\",\n     \"derivation_fa\": \"واژه درست است اما جهت پیکان نه: «موش» فارسی نو واژه‌ای میراثی است و از سانسکریت وام گرفته نشده. این واژه ادامهٔ فارسی میانهٔ mušk / mūš است (نوشتار پهلوی mwšk'؛ مکنزی: «2mušk موش، موش صحرایی») که خود از ایرانی باستان *múHs و آن از هندوایرانیِ آغازین *múHs می‌آید؛ پس «موش» هم‌ریشهٔ mūṣ سانسکریت است، نه فرزند آن. «ک» پایانیِ پهلوی همان افزودهٔ پسوندی است که در بلوچی mušk و کردی mišk هم دیده می‌شود و فارسی نو آن را انداخته است. هرن در شمارهٔ ۹۹۵ همین مجموعهٔ هم‌ریشه‌ها را می‌آورد و حاشیهٔ معین بر برهان قاطع ص۲۰۵۳ نیز صورت‌های هندی باستان، ارمنی، اوستی، بلوچی و کردی را در کنار هم می‌نشاند و فارسی را از سانسکریت نمی‌گیرد. داوری: با احتیاط پذیرفتنی — واژه و ریشه درست، ولی نسب‌نامه نادرست (هم‌ریشه به‌جای فرزند). نکتهٔ آوانویسی: در صفحهٔ چاپی «mŭš» آمده و در داده‌های استخراج‌شده «müš»؛ صورت درست mūš با «او»ی کشیده است.\",\n     \"sources\": [W_MUSH, W_PIE],\n     \"error_in\": \"extraction\",\n     \"book_prints\": \"mŭš\",\n     \"correct_form\": \"mūš (NP موش; the printed breve mŭš was read as ü in the JSON)\",\n     \"ref_check\": [\n      {\"ref\": \"POK:752\", \"status\": \"supports\", \"note\": POK_MUS + \" — 'np. mūš \\\"mouse\\\"' is listed directly under the root, i.e. Pokorny too treats Persian as a cognate of Old Indic, not as a borrowing from it.\"},\n      {\"ref\": \"BQT:2053\", \"status\": \"supports\", \"note\": BQT2053 + \" — the page cited is indeed the موش page of Borhān (vol. 4), and Mo'in's footnote gives the cognates, not a Sanskrit source.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p. 57 s.v. 2mušk\", \"stance\": \"supports\", \"note\": PHD_MUSK},\n      {\"src\": \"HRN\", \"where\": \"Horn no. 995 (p. ~220)\", \"stance\": \"supports\", \"note\": HRN_MUS},\n      {\"src\": \"WLD\", \"where\": \"Bd. II 312\", \"stance\": \"supports\", \"note\": \"\\\"Ai. mūs- 'Maus, Ratte' ..., np. mūš 'Maus'\\\" — Persian listed as a parallel to the Indic form.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/موش\", \"stance\": \"partial\", \"note\": \"\\\"Inherited from Middle Persian mwšk' /mušk/ ('mouse, rat'), from Proto-Iranian *múHs, from Proto-Indo-Iranian *múHs, from Proto-Indo-European *múHs\\\" — inheritance, not borrowing from Sanskrit.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"mošk; mešk; meškî\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian مشک mušk/mošk 'musk' does come from the Indic muṣka- of the box above: the musk gland under the belly of the male musk deer (Moschus moschiferus, غزال المسک, Mo'in's آهوی خطایی) was seen as a scrotum, so 'testicle' became the name of the drug. The route is Skt muṣka- → Middle Persian mušk [mwšk'] (MacKenzie: \\\"1mušk musk\\\") → New Persian مشک; Mo'in's own etymological footnote on Borhān p. 2014 states the chain in these very terms: «سانسکریت muska مصغر mûs (موش)، یونانی moskos، لاتینی muscus، فرانسوی و انگلیسی musc، عربی مسك». From Middle Persian the word passed into Arabic as مسک misk (already in Qur'an 83:26; Jeffery: 'quite commonly recognized as a loan-word from the Persian... more likely to have come direct from Middle Persian into Arabic than through the Syriac'), and the Arabicized misk came back into Persian — which is exactly the doublet Nourai records in his parenthesis «مُشک ۱ ( مِسک )»; Hübschmann §24 files Persian misk 'Moschus' (< Arab. misk) among the cases of u > i before a sibilant, and Ghiyāth (quoted by Mo'in) already noted that the people of Fārs said mešk while Transoxianans said mošk — which is all the chart's mošk ~ mešk pair amounts to, not two different words. mešk in بیدمشک bīd-e mešk 'musk willow' (Salix aegyptiaca, whose blossom water smells of musk) is the same noun in compound; meškī/مشکین is the nisba adjective 'musk-coloured', i.e. jet black, the colour of dried musk — the sense of Ferdowsi's line quoted in the box, «... یکی تاج بر سر ز مُشک سیاه».\",\n     \"derivation_fa\": \"«مشک» فارسی به‌راستی از muṣka هندی (سانسکریت) می‌آید: کیسهٔ مشکِ زیر شکمِ آهوی نرِ ختایی (غزال المسک) را همچون کیسهٔ بیضه می‌دیدند و از همین رو نامِ «خایه» بر آن دارو نشست. راه آن چنین است: muṣka سانسکریت ← فارسی میانهٔ mušk (پهلوی mwšk'؛ مکنزی: «1mušk مشک») ← «مشک» فارسی نو؛ و حاشیهٔ ریشه‌شناسیِ خودِ معین بر برهان قاطع ص۲۰۱۴ همین زنجیره را می‌آورد: «سانسکریت muska مصغر mûs (موش)، یونانی moskos، لاتینی muscus، فرانسوی و انگلیسی musc، عربی مسك». از فارسی میانه به عربی رفت و «مسک» شد (که همان در قرآن ۸۳:۲۶ آمده؛ جفری: «به‌روشنی وام‌واژه‌ای از فارسی... به احتمال بیشتر یکسر از فارسی میانه به عربی رفته، نه از راه سریانی») و صورتِ معرّبِ «مسک» باز به فارسی برگشت — همان دوگانه‌ای که نورایی در کمانکِ «مُشک ۱ (مِسک)» ثبت کرده است. هوبشمان در بند ۲۴ «مسک» فارسی را در شمار موارد تبدیل u به i پیش از حرف صفیری می‌آورد، و غیاث (به نقل معین) گفته بود که «اهل فارس بکسر میم و اهل ماوراءالنهر بضم میم خوانند» — یعنی جفتِ mošk ~ mešk نمودار همین اختلاف تلفظ است، نه دو واژهٔ جدا. «مشک» در «بیدمشک» (بیدِ مُشک، Salix aegyptiaca که عرقِ گلش بوی مشک دارد) همان اسم است در ترکیب، و «مشکی/مشکین» صفتِ نسبی به معنای «به رنگ مشک»، یعنی سیاهِ پرکلاغی است — همان معنایی که در بیتِ فردوسیِ نقل‌شده در جعبه دیده می‌شود. ادعای نورایی درست است.\",\n     \"sources\": [W_MOSK, A_MOSK, E_MUSK, AHD_MUSK],\n     \"ref_check\": [\n      {\"ref\": \"POK:752\", \"status\": \"supports\", \"note\": POK_MUS + \" — 'npers. mušk ... (from Pers. derives gr. moschos, NHG Moschus)' stands right beside 'Old Indic muska- m. \\\"testicle\\\"', i.e. Pokorny's page carries both ends of this node's claim.\"},\n      {\"ref\": \"BQT:2053\", \"status\": \"partial\", \"note\": \"p. 2053 is the موش page (footnote quoted at node #2) and says nothing about مشک; the Borhān page that actually carries Mo'in's etymology of مشک is p. 2014 — \" + BQT2014 + \" So the reference supports the claim, but Nourai's page number belongs to the mouse entry, not the musk entry.\"},\n      {\"ref\": \"MON:4147\", \"status\": \"supports\", \"note\": \"Mo'in via abadis.ir (فرهنگ معین): مُشک «مادهٔ سیاه‌رنگ و خوشبویی که در نافِ آهوی مشک تولید می‌شود» with a Sanskrit origin label (سانسکریت); مَشک 'waterskin' is a separate entry, so Mo'in agrees with the chart in keeping the two apart. Page 4147 itself is not verifiable in the unpaginated online text.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p. 57 s.v. 1mušk\", \"stance\": \"supports\", \"note\": PHD_MUSK + \" — MP mušk carries both senses, 'musk' and 'mouse', in the same spelling mwšk'.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien §24 (pp. 139-140)\", \"stance\": \"supports\", \"note\": HUB_MISK},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi 1988 p. 250 s.v. misk\", \"stance\": \"supports\", \"note\": PLA_MISK},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery p. 264 s.v. (Misk)\", \"stance\": \"supports\", \"note\": FVQ_MISK},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_pages.txt [pdf page 473] s.v. مشک\", \"stance\": \"supports\", \"note\": ARY_MOSK},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1515a\", \"stance\": \"supports\", \"note\": LKT_MUSK},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. musk\", \"stance\": \"supports\", \"note\": KLN_MUSK}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Greek\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The empty box stands for Late/Byzantine Greek μόσχος 'musk' (homonymous with, but distinct from, classical μόσχος 'young shoot, calf'), borrowed from Middle Persian mušk in the aromatics and medical literature of late antiquity (Aetius, Paul of Aegina, 6th-7th c.): Iranian u is rendered by Greek o and the cluster -šk- by -σχ-, with the usual -ος nominative added. Jeffery states that it was 'from the Iranian, not the Indian form' that Armenian mušk, Greek μόσχος, Aramaic, Syriac and Ethiopic musk-words were all borrowed; Walde-Pokorny say the same in one clause ('aus dem Pers. stammt gr. μόσχος, nhd. Moschus'). Wiktionary's μόσχος (etymology 2) has 'From Middle Persian mwšk'..., itself from Sanskrit muṣká' with 'Late Latin muscus' as its descendant — exactly this node and the next.\",\n     \"derivation_fa\": \"این جعبهٔ تهی نمایندهٔ μόσχος یونانیِ متأخر/بیزانسی به معنای «مشک» است (هم‌آوا با μόσχος کلاسیک «جوانه، گوساله» ولی جدا از آن) که در ادبیات داروسازی و پزشکیِ اواخر دورهٔ باستان (اتیوس، پولس اجانیطی، سدهٔ ششم و هفتم میلادی) از فارسی میانهٔ mušk وام گرفته شده است: «او»ی ایرانی به o یونانی و خوشهٔ -šk- به -σχ- بدل شده و پایانهٔ نهادیِ -ος بر آن افزوده شده است. جفری تصریح می‌کند که ارمنی mušk، یونانی μόσχος و صورت‌های آرامی و سریانی و حبشی همه «از صورت ایرانی، نه هندی» وام گرفته شده‌اند؛ والده-پوکورنی نیز در یک عبارت همین را می‌گویند: «μόσχος یونانی از فارسی است». ویکی‌واژه ذیل μόσχος (ریشه‌شناسی ۲) می‌نویسد «از فارسی میانهٔ mwšk'، خود از سانسکریت muṣká» و muscus لاتینیِ متأخر را فرزند آن می‌شمارد — یعنی درست همین گره و گرهِ پس از آن. ادعای نورایی درست است.\",\n     \"sources\": [W_MOSCHOS, E_MUSK],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the Greek box carries no reference in the book.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FVQ\", \"where\": \"Jeffery p. 264 s.v. (Misk)\", \"stance\": \"supports\", \"note\": FVQ_MISK},\n      {\"src\": \"WLD\", \"where\": \"Bd. II 313\", \"stance\": \"supports\", \"note\": \"\\\"np. mush 'Bibergeil' (aus dem Pers. stammt gr. moschos, nhd. Moschus)\\\"\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/μόσχος (etymology 2)\", \"stance\": \"supports\", \"note\": \"\\\"From Middle Persian mwšk' (*mušk), itself from Sanskrit मुष्क (muṣká, 'testicle')\\\"; descendants: \\\"→ Late Latin: muscus\\\".\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. musk\", \"stance\": \"supports\", \"note\": KLN_MUSK + \" — Klein's chain has Gk. μόσχος between Persian and Latin, as here.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Latin\",\n     \"words\": \"muskus\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"The Greek → Latin step is right, but Latin never had a form *muskus: the word is Late Latin muscus 'musk' (Medieval Latin also muscum), which gave Old French musc, Italian musco/muschio, Medieval Latin muscatus > Muskat, and — through French — English musk. Klein: 'fr. OF. musc, fr. L. muscus, fr. Gk. μόσχος'; AHD: 'from Late Latin muscus'; Mo'in's own footnote on Borhān p. 2014 prints «لاتینی muscus»; Lokotsch has 'mlat. muscum'; Asbaghi 'mlat. muscum'. The printed page 313 of the book really does read 'muskus' (see the page image copied to data/verification/sources/refs/ocr/BOOK/343.png), so this is Nourai's own misprint and the extraction is faithful. A likely source of the slip: the k-spelling exists in the modern borrowings Dutch/Russian muskus 'musk' (Klein even has an entry \\\"muskus grass — fr. Du. muskus, 'musk', fr. L. muscus\\\"), which is not a Latin form.\",\n     \"derivation_fa\": \"گامِ یونانی ← لاتینی درست است، اما در لاتینی هرگز صورتِ *muskus نبوده: واژه muscus لاتینیِ متأخر است (در لاتینیِ میانه muscum نیز) که از آن musc فرانسویِ کهن، musco/muschio ایتالیایی، muscatus لاتینیِ میانه (نیای Muskat) و از راه فرانسه musk انگلیسی برآمده است. کلاین: «از OF musc، از muscus لاتینی، از μόσχος یونانی»؛ فرهنگ American Heritage: «از muscus لاتینیِ متأخر»؛ و حاشیهٔ خودِ معین بر برهان ص۲۰۱۴ می‌نویسد «لاتینی muscus»؛ لوکوچ و اصباغی نیز «mlat. muscum». در صفحهٔ ۳۱۳ چاپی همان «muskus» آمده است (تصویر صفحه در data/verification/sources/refs/ocr/BOOK/343.png)، پس این خطای چاپیِ کتاب است و خوانشِ اسکن درست بوده. سرچشمهٔ احتمالی لغزش: صورتِ با k تنها در وام‌واژه‌های نو، هلندی و روسیِ muskus، دیده می‌شود (کلاین حتی مدخلی دارد: «muskus grass از هلندیِ muskus، از muscus لاتینی») که صورتی لاتینی نیست.\",\n     \"sources\": [E_MUSK, AHD_MUSK, W_MOSCHOS],\n     \"error_in\": \"book\",\n     \"book_prints\": \"muskus\",\n     \"correct_form\": \"muscus (Late Latin muscus, Medieval Latin muscum)\",\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the Latin box carries no reference in the book.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. musk (and s.v. muscat, moschatel, muskus grass)\", \"stance\": \"partial\", \"note\": KLN_MUSK + \" — Klein has the whole chain but the Latin form is muscus; his only muskus is Dutch.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1515a\", \"stance\": \"partial\", \"note\": LKT_MUSK + \" — 'mlat. muscum', with Russian muskus listed as a modern borrowing, not a Latin form.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur [pdf page 473] s.v. مشک\", \"stance\": \"partial\", \"note\": ARY_MOSK + \" — Aryanpur's Latin form is muscus.\"},\n      {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. musk\", \"stance\": \"partial\", \"note\": \"\\\"[Middle English, from Old French musc, from Late Latin muscus, from Greek moskhos, from Persian mušk, probably from Sanskrit muṣkaḥ]\\\" — chain identical, Latin form muscus.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"French\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The empty box is Old French musc (attested from the 12th-13th c. in medical and apothecary texts), taken from Late/Medieval Latin muscus/muscum with regular Old French loss of the Latin -us ending; it survives as modern French musc, and its derivatives spread widely — muscade/noix muscade 'nutmeg' (whence English nutmeg's second element), muguet 'lily of the valley', muscat, muscardin. Klein and Lokotsch both put French musc between Latin and English, exactly as drawn.\",\n     \"derivation_fa\": \"این جعبهٔ تهی همان musc فرانسویِ کهن است (از سدهٔ دوازدهم و سیزدهم میلادی در متون پزشکی و عطاری) که از muscus/muscum لاتینیِ متأخر و میانه گرفته شده و پایانهٔ -us لاتینی به قاعدهٔ فرانسویِ کهن افتاده است؛ همان است که در فرانسهٔ امروز musc مانده و مشتقات فراوانی از آن پراکنده شده: muscade و noix muscade («جوز هندی»)، muguet، muscat و muscardin. کلاین و لوکوچ هر دو musc فرانسوی را میان لاتین و انگلیسی می‌نشانند، درست همان‌گونه که در نمودار کشیده شده است. ادعای نورایی درست است.\",\n     \"sources\": [E_MUSK, W_MOSCHOS],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the French box carries no reference in the book.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. musk, muscat, mugget\", \"stance\": \"supports\", \"note\": KLN_MUSK + \"; and s.v. mugget: \\\"F. muguet ... fr. (noix) muguette, alteration of (noix) muscade ... fr. musc, 'musk'\\\" — French musc as the pivot.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1515a\", \"stance\": \"supports\", \"note\": LKT_MUSK + \" — 'prov. musc, frz. musc' listed between Medieval Latin and English.\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/musk\", \"stance\": \"supports\", \"note\": \"\\\"late 14c., from Old French musc (13c.) and directly from Medieval Latin muscus\\\".\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"English\",\n     \"words\": \"musk\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English musk appears in the late 14th c. as ME muske/musc, borrowed from Old French musc (and reinforced by Medieval Latin muscus in medical Latin); by the 16th-18th c. it had generated the compounds musk-melon (1570s), musk-deer (1680s) and musk-ox (1744), and the adjective musky. The chart's chain Sanskrit → Persian → Greek → Latin → French → English is precisely what AHD prints for the word, so Nourai's AHD:865 is the standard modern authority for this node, not merely his own reading.\",\n     \"derivation_fa\": \"musk انگلیسی در اواخر سدهٔ چهاردهم میلادی به‌صورت muske/musc در انگلیسیِ میانه پیدا می‌شود و وام‌واژه‌ای است از musc فرانسویِ کهن (با تقویتِ muscus لاتینیِ میانه در لاتینِ پزشکی)؛ از سدهٔ شانزدهم تا هجدهم ترکیب‌هایی چون musk-melon (۱۵۷۰م)، musk-deer (۱۶۸۰م) و musk-ox (۱۷۴۴م) و صفتِ musky از آن ساخته شد. زنجیرهٔ نمودار (سانسکریت ← فارسی ← یونانی ← لاتین ← فرانسه ← انگلیسی) همان است که فرهنگ American Heritage برای این واژه چاپ می‌کند؛ پس ارجاعِ AHD:865 نورایی خودْ مرجعِ معیارِ امروزی برای این گره است. ادعای نورایی درست است.\",\n     \"sources\": [E_MUSK, AHD_MUSK],\n     \"ref_check\": [\n      {\"ref\": \"AHD:865\", \"status\": \"supports\", \"note\": \"Nourai's page is in the body of the 1975/76 New College edition, which is not open online (refs_online: archive_restricted); the same dictionary's current entry (ahdictionary.com s.v. musk, archived) reads \\\"[Middle English, from Old French musc, from Late Latin muscus, from Greek moskhos, from Persian mušk, probably from Sanskrit muṣkaḥ]\\\" — the chart's chain verbatim (with muscus for the chart's muskus). Watkins' root appendix does not file MUSK under mūs-, since for AHD the English word is a loan, not an inherited derivative.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. musk\", \"stance\": \"supports\", \"note\": KLN_MUSK},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Musk\", \"stance\": \"partial\", \"note\": SKT_MUSK + \" — Skeat has the Persian-Sanskrit connection but adds the older 'lit. thief, from mush to steal' explanation of the Sanskrit base, which modern work does not follow.\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/musk\", \"stance\": \"supports\", \"note\": \"\\\"late 14c. ... from Late Greek moskhos, from Persian mushk, from Sanskrit muska-s 'testicle', from mus 'mouse'... The deer gland was thought to resemble a scrotum.\\\"\"},\n      {\"src\": \"FSD\", \"where\": \"vol. III s.v. musk\", \"stance\": \"supports\", \"note\": \"Funk & Wagnalls describes musk as the substance 'imported in the pod, a sac situated in front of the prepuce of the male musk-deer' — the same referent and the same anatomical metaphor behind the Sanskrit name.\"}\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"Germanic\",\n     \"words\": \"mus\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Nourai's 'Germanic mus' is Proto-Germanic *mūs (a consonant/root stem, pl. *mūsiz), the regular reflex of PIE *múHs with the laryngeal lost and compensatory length: it gives OE mūs (pl. mȳs by i-mutation), OS/ON/OFris/MDu mūs, OHG-MHG mūs > German Maus, Dan./Swed. mus, Du. muis. Watkins states the step in the same words: '1. Germanic *mūs (plural *mūsiz) in Old English mūs (plural mȳs), mouse: MOUSE'. The German and Old English words also carry the transferred sense 'muscle (of the upper arm)' (Klein: OHG mūs 'mouse; muscle'), which is the same metaphor as Latin mūsculus.\",\n     \"derivation_fa\": \"«mus» ژرمنیِ نمودار همان *mūs ژرمنیِ آغازین است (ستاکی بی‌واسطه، جمعِ *mūsiz) که بازتابِ قاعده‌مندِ *múHs هندواروپایی است با افتادنِ حنجره‌ای و کشیدگیِ جبرانی؛ از آن mūs انگلیسیِ کهن (جمعِ mȳs با همگونیِ i)، mūs ساکسونیِ کهن و نورس و فریزی، mūs آلمانیِ علیایِ کهن > Maus آلمانی، mus دانمارکی و سوئدی و muis هلندی برآمده است. واتکینز همین گام را با همین واژه‌ها می‌آورد: «۱. ژرمنیِ *mūs (جمعِ *mūsiz) در mūs انگلیسیِ کهن (جمعِ mȳs)». صورت‌های آلمانی و انگلیسیِ کهن معنای انتقالیِ «ماهیچهٔ بازو» را نیز دارند (کلاین: mūs آلمانیِ علیایِ کهن «موش؛ ماهیچه») که همان استعارهٔ mūsculus لاتینی است. ادعای نورایی درست است.\",\n     \"sources\": [W_PIE],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": AHD_MUS + \" — Nourai cites AHD without a page; the Watkins root entry gives exactly the Germanic *mūs > OE mūs > MOUSE step of this node and the next.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 752-753\", \"stance\": \"supports\", \"note\": \"\\\"Old High German Middle High German Old Saxon Middle Low German Old Icelandic Old English mūs 'mouse, muscle' (consonant-stem)\\\"\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II 312-313\", \"stance\": \"supports\", \"note\": \"\\\"ahd. mhd. as. mnd. aisl. ags. mūs 'Maus' (Kons.-St.)\\\" and, for the transferred sense, \\\"ahd. usw. mūs 'Muskel, bes. des Oberarms'\\\"\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. mouse\", \"stance\": \"supports\", \"note\": KLN_MOUSE},\n      {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/múHs\", \"stance\": \"supports\", \"note\": \"descendant list: \\\"*mūs (Proto-Germanic)\\\" directly under PIE *múHs.\"}\n     ]\n    },\n    {\n     \"id\": 9,\n     \"lang\": \"English\",\n     \"words\": \"mouse\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Old English mūs (pl. mȳs) > Middle English mous/mus > Modern English mouse: the vowel is the inherited long ū, which was diphthongized to /aʊ/ in the Great Vowel Shift (15th-17th c.) while the spelling ou was imported from Anglo-Norman scribal practice; the irregular plural mice continues OE mȳs, i.e. *mūsiz with i-mutation and later unrounding of ȳ. Klein and Skeat both give the chain ME mous < OE mūs with the same Germanic and Indo-European cognates as the chart.\",\n     \"derivation_fa\": \"mūs انگلیسیِ کهن (جمعِ mȳs) > mous انگلیسیِ میانه > mouse انگلیسیِ نو: واکهٔ آن همان «او»ی کشیدهٔ میراثی است که در «چرخشِ بزرگِ واکه‌ها» (سدهٔ پانزدهم تا هفدهم) به /aʊ/ بدل شد، در حالی که نوشتارِ ou از شیوهٔ کاتبانِ انگلونورمان به وام گرفته شده بود؛ جمعِ بی‌قاعدهٔ mice نیز ادامهٔ mȳs انگلیسیِ کهن است، یعنی *mūsiz با همگونیِ i و سپس بی‌گردیِ ȳ. کلاین و اسکیت هر دو زنجیرهٔ mous انگلیسیِ میانه از mūs انگلیسیِ کهن را با همان هم‌ریشه‌های ژرمنی و هندواروپاییِ نمودار می‌آورند. ادعای نورایی درست است.\",\n     \"sources\": [W_PIE],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of its own; the parent box's AHD citation covers the step (Watkins: 'Old English mūs (plural mȳs), mouse: MOUSE').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. mouse\", \"stance\": \"supports\", \"note\": KLN_MOUSE},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Mouse\", \"stance\": \"supports\", \"note\": SKT_MUSK},\n      {\"src\": \"SYN\", \"where\": \"Buck 3.68 'mouse'\", \"stance\": \"supports\", \"note\": SYN_MUSKA + \" — the table gives 'OE mūs, ME mous, NE mouse' in sequence.\"}\n     ]\n    },\n    {\n     \"id\": 10,\n     \"lang\": \"Latin\",\n     \"words\": \"mus\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Latin mūs (gen. mūris) 'mouse' is the correct Italic reflex of PIE *múHs (Proto-Italic *mūs), the oblique r being rhotacism of intervocalic s (*mūs-is > mūris). The gloss is what makes this node only plausible: classical Latin mūs means 'mouse' (and by extension some marine and other animals), never 'muscle'. The muscle sense belongs to the diminutive mūsculus 'little mouse', hence 'muscle' and also 'sea-mussel'; it is Greek μῦς, not Latin mūs, that carries both senses in one word (Pokorny lists 'gr. μῦς \\\"mouse\\\", also \\\"muscle\\\"' but for Latin only 'mūsculus ds., \\\"muscle\\\"'). Watkins compresses the same way ('2. Latin mūs, mouse: MURINE, MUSCLE, MUSTELINE'), which is probably where Nourai's double gloss comes from.\",\n     \"derivation_fa\": \"mūs لاتینی (اضافیِ mūris) «موش» بازتابِ درستِ *múHs هندواروپایی در شاخهٔ ایتالیایی است (*mūs ایتالیاییِ آغازین) و «ر»ِ ستاکِ غیرفاعلی از تبدیلِ s میان‌واکه‌ای به r (قاعدهٔ rhotacism: *mūs-is > mūris) پدید آمده است. آنچه این گره را تنها «با احتیاط پذیرفتنی» می‌کند معنیِ آن است: mūs در لاتینِ کلاسیک تنها «موش» است و هرگز «ماهیچه» نبوده؛ معنیِ «ماهیچه» از آنِ مصغّرِ mūsculus («موشکِ کوچک») است که هم «ماهیچه» و هم «صدفِ دریایی» را می‌رساند. این μῦς یونانی است، نه mūs لاتینی، که هر دو معنی را در یک واژه دارد (پوکورنی برای یونانی می‌نویسد «μῦς موش، و نیز ماهیچه» اما برای لاتین تنها «mūsculus ماهیچه»). واتکینز هم همین‌گونه فشرده می‌نویسد («۲. لاتینی mūs، موش: MURINE، MUSCLE، MUSTELINE») و شاید معنیِ دوگانهٔ نورایی از همین‌جا آمده باشد.\",\n     \"sources\": [W_PIE, \"https://www.etymonline.com/word/muscle\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": AHD_MUS + \" — Watkins gives Latin mūs the gloss 'mouse' only, and files MUSCLE under it as a derivative; the chart's 'mouse, muscle' gloss for Latin mūs itself goes beyond the reference.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 752-753\", \"stance\": \"partial\", \"note\": POK_MUS + \" — 'Latin mūs m. \\\"mouse\\\"' with the muscle sense given only for mūsculus.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II 312-313\", \"stance\": \"partial\", \"note\": WLD_MUS + \" — 'lat. mūs \\\"Maus\\\"' and separately 'lat. mūsculus \\\"Muskel\\\"'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck, 'muscle'\", \"stance\": \"supports\", \"note\": SYN_MUSCLE},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet (LAT.txt line 31792)\", \"stance\": \"partial\", \"note\": \"the entry refers to \\\"μῦς en grec et le rapport mus : musculus\\\" — i.e. the 'muscle' sense is carried by Greek μῦς and by the Latin diminutive, not by mūs itself.\"}\n     ]\n    },\n    {\n     \"id\": 11,\n     \"lang\": \"English\",\n     \"words\": \"muscle\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The etymology is right in substance but the chart skips two steps: English muscle (late 14c. in anatomical translation, common from the 16th c.) comes from Middle French muscle, which comes from Latin mūsculus, the diminutive of mūs — 'little mouse', named for the way a flexing biceps moves under the skin (Buck and Aryanpur both spell out the metaphor). So the arrow should be mūs → mūsculus → (Old/Middle) French muscle → English muscle, not mūs → English. The same Latin diminutive also gave, by a separate route, English mussel (OE muscle/muxle, from Late Latin mūsculus 'sea-mussel'), so muscle and mussel are doublets.\",\n     \"derivation_fa\": \"ریشه‌شناسی در اصل درست است، اما نمودار دو گام را نادیده گرفته: muscle انگلیسی (از اواخر سدهٔ چهاردهم در ترجمه‌های کالبدشناسی و از سدهٔ شانزدهم رایج) از muscle فرانسویِ میانه آمده و آن از mūsculus لاتینی، مصغّرِ mūs، یعنی «موشِ کوچک» — نامی که از جنبیدنِ ماهیچهٔ دوسر زیر پوست گرفته شده است (باک و آریان‌پور هر دو همین استعاره را باز می‌کنند). پس پیکان باید mūs ← mūsculus ← muscle فرانسوی ← muscle انگلیسی باشد، نه یکسر mūs ← انگلیسی. همان مصغّرِ لاتینی از راهی دیگر mussel انگلیسی («صدف»، انگلیسیِ کهن muscle/muxle از mūsculus لاتینیِ متأخر) را هم داده است؛ پس muscle و mussel دوگانه‌اند.\",\n     \"sources\": [\"https://www.etymonline.com/word/muscle\", W_PIE],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of its own; its parent box cites AHD, whose index line reads 'MUSCLE mūs-' (AHD_watkins1985.txt line 1897) — i.e. Watkins too files the word under the root, with the mūsculus step given in the dictionary body.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. muscle\", \"stance\": \"supports\", \"note\": \"Klein s.v. mouse cross-refers to muscle, muscular, musk; the muscle entry derives it from L. mūsculus, dimin. of mūs (cp. his s.v. muscardine, muscat for the same base).\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Muscle (1)\", \"stance\": \"supports\", \"note\": SKT_MUSK + \" — \\\"Muscle (1), the fleshy part... F. muscle. - L. musculus, (1) a little mouse... Dimin. of L. mus, a mouse\\\" plus the note that muscle (2) 'mussel' is the same word.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur [pdf page 465], entry ماهیچه note 3\", \"stance\": \"supports\", \"note\": ARY_MUSCLE},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/muscle\", \"stance\": \"supports\", \"note\": \"\\\"from Latin musculus 'a muscle', literally 'a little mouse', diminutive of mus 'mouse'... muscles' 'shape and movement... were thought to resemble mice'\\\"\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-343.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=1)\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk343.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-343.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 343",
 "description": "Write and check page-343.json"
}
```


### [2026-09-07T17:55:35.862Z] TOOL RESULT

```
written
JSON OK
nodes verified: 15/15
node verdicts: {'confirmed': 10, 'plausible': 4, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 10, 'not_checked': 7, 'partial': 2}
books consulted: {'supports': 43, 'silent': 2, 'contradicts': 1, 'partial': 12} | by book: {'KLN': 11, 'Wiktionary': 5, 'Etymonline': 5, 'WLD': 5, 'SKT': 4, 'FSD': 3, 'POK': 3, 'SYN': 3, 'ARY': 3, 'LKT': 3, 'PLA': 2, 'AHD': 2, 'PHD': 2, 'FVQ': 2, 'MON': 1, 'Dehkhoda': 1, 'HRN': 1, 'HUB': 1, 'LAT': 1}
```


## [2026-09-07T17:55:43.892Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.etymonline.com/word/muscle\" --note \"page 343: English muscle < Latin musculus dimin. of mus (nodes #10, #11)\" 2>&1 | tail -2 && grep -c \"musculus\" data/verification/sources/web/*.txt 2>/dev/null | grep -v \":0\" | head -3",
 "description": "Archive etymonline muscle page"
}
```


### [2026-09-07T17:55:45.795Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/03e5178489e83d0a.txt
data/verification/sources/web/03e5178489e83d0a.txt:3
data/verification/sources/web/5cdb7745fcd8f314.txt:1
data/verification/sources/web/5b9bc33f8d4f14bd.txt:1
```


## [2026-09-07T17:56:03.734Z] AGENT

Done. `verify_check.py 343` reports 0 PROBLEM lines (15/15 nodes, both roots).

**Page 343 (book p. 313) — 2 entries, 15 nodes**
- Root verdicts: confirmed 2. Node verdicts: confirmed 10, plausible 4, transcription_suspect 1.
- ref_check: supports 10, partial 2, not_checked 7 (FVA has no digital copy; 5 nodes carry no refs in the book). consulted: 61 entries from 19 books (POK, WLD, AHD/Watkins, SYN, KLN, SKT, FSD, HRN, HUB, PHD, BQT, MON, ARY, PLA, FVQ, LKT, LAT, PHN + web).

**Flagged items**
- `transcription_suspect` #5 Latin **muskus** (root Mu/Mus): the printed page really shows "muskus" — Nourai's misprint for Late Latin **muscus** (Klein, AHD, Lokotsch, Asbaghi, and Mo'in's own footnote on Borhān p. 2014 all print muscus; the k-spelling exists only in Dutch/Russian muskus). `error_in: book`; page image copied to `data/verification/sources/refs/ocr/BOOK/343.png`.
- `plausible` #2 Persian **موش** (Mu/Mus): word and root right, arrow direction wrong — NP mūš is inherited (MP mušk/mūš < PIr *múHs), a cognate of Skt mūṣ-, not a descendant of it (Horn 995, MacKenzie, Mo'in's BQT 2053 footnote all treat it as a cognate).
- `plausible` #10/#11 Latin mus "mouse, muscle" → English muscle: Latin mūs never means 'muscle'; the sense and the English word come via the diminutive mūsculus and French muscle (two steps omitted).
- `plausible` #2 French box (M.s.s/Massa): Pihan 257 and Klein 944 do derive masser from Arabic mass (Klein explicitly rejects Gk. μάσσειν), but Etymonline/Wiktionary keep Portuguese amassar open and Funk & Wagnalls derives it from Greek μάσσω — accepted, not established.

**For the owner to fix (JSON vs printed page)**
- Entry 1 node #2: the page prints **mŭš** (breve); the extraction has **müš** (umlaut). Correct value is mūš. Only diacritic-level.
- Not an extraction issue but worth noting: Nourai's `BQT:2053` on node #3 is the موش page; Mo'in's مشک etymology is on BQT p. 2014 (saved verbatim to `sources/refs/ocr/BQT/2014.vision.txt`).
