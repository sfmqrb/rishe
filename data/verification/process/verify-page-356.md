# Verification process log — verify-page-356


## [2026-09-07T18:18:00.583Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 356 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-356.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-356.json. Write /home/sfmqrb/git/rishe/data/verification/page-356.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 356` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T18:18:02.525Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-07T18:18:03.274Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T18:18:03.287Z] TOOL RESULT

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


## [2026-09-07T18:18:04.141Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-356.txt"
}
```


### [2026-09-07T18:18:04.185Z] TOOL RESULT

```
1	=== PDF page 356 (book page 326) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Nei 1, Ni 2 : to shine, to be excited  (refs POK:760)  PART 2
4	#1 (parent #0) [Sanskrit] refs=POK:760; UNV:51 | nili, nilah : dark blue ; nîlotpala : blue lotus
5	  #2 (parent #1) [Persian] refs=BQT:2231 | nîl «نیل ، نیلوفر ، نیلپَر ، نیلفَر ، نیله» : indigo ; lîlak «لیلک» : lilac
6	    #3 (parent #2) [Arabic] refs=None | laylak
7	      #4 (parent #3) [Spanish] refs=None | 
8	        #5 (parent #4) [French] refs=None | 
9	          #6 (parent #5) [English] refs=AHD:757 | lilac
10	    #7 (parent #2) [Arabic] refs=AHD:52 | al-nil : the indigo
11	      #8 (parent #7) [Portuguese] refs=None | 
12	        #9 (parent #8) [English] refs=AHD:52 | anil, aniline
13	        #10 (parent #8) [French] refs=AHD:52 | aniline
14	          #11 (parent #10) [Persian] refs=MON:98 | ânâlîn «آنیلین»
15	--- entry 1 ---
16	ROOT [Indo-European] Nei 2, Neia, Nî 3 : to lead, guide  (refs POK:760)
17	#1 (parent #0) [Avestan / Old Persian] refs=KLN:1026; HRN:265; SYN:712; POK:760; KNT:193 | nî 2, nay : to guide ; nayeiti : leads ; fra-nay : leads forward ☞Per 1
18	  #2 (parent #1) [Pahlavi] refs=HRN:265 | nîtan : to lead ; ânîtan : to bring
19	    #3 (parent #2) [None] refs=None | 
20	--- entry 2 ---
21	ROOT Nei 3 -> redirect to Ne 1
22	--- entry 3 ---
23	ROOT Neia -> redirect to Nei 2
24	
```


## [2026-09-07T18:18:08.231Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-356.json",
 "description": "Read source JSON page 356"
}
```


### [2026-09-07T18:18:08.275Z] TOOL RESULT

```
{
  "pdf_page": 356,
  "book_page": 326,
  "entries": [
    {
      "root": {
        "name": "Nei 1, Ni 2",
        "lang": "Indo-European",
        "refs": "POK:760",
        "gloss": "to shine, to be excited"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:760; UNV:51",
          "words": [
            {"translit": "nili, nilah", "gloss": "dark blue", "script": null},
            {"translit": "nîlotpala", "gloss": "blue lotus", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2231",
          "words": [
            {"translit": "nîl", "gloss": "indigo", "script": "نیل ، نیلوفر ، نیلپَر ، نیلفَر ، نیله"},
            {"translit": "lîlak", "gloss": "lilac", "script": "لیلک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "برآمد نیلگون ابری ز روی نیلگون دریا - چو رای عاشقان گردان چو طبع بیدلان شیدا",
            "poet": "Farrokhî Sîstânî"
          }
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": null,
          "words": [
            {"translit": "laylak", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Spanish",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD:757",
          "words": [
            {"translit": "lilac", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 2,
          "lang": "Arabic",
          "refs": "AHD:52",
          "words": [
            {"translit": "al-nil", "gloss": "the indigo", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Portuguese",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": "AHD:52",
          "words": [
            {"translit": "anil, aniline", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
          "lang": "French",
          "refs": "AHD:52",
          "words": [
            {"translit": "aniline", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON:98",
          "words": [
            {"translit": "ânâlîn", "gloss": null, "script": "آنیلین"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Nei 2, Neia, Nî 3",
        "lang": "Indo-European",
        "refs": "POK:760",
        "gloss": "to lead, guide"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "KLN:1026; HRN:265; SYN:712; POK:760; KNT:193",
          "words": [
            {"translit": "nî 2, nay", "gloss": "to guide", "script": null},
            {"translit": "nayeiti", "gloss": "leads", "script": null},
            {"translit": "fra-nay", "gloss": "leads forward", "script": null, "see": ["Per 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:265",
          "words": [
            {"translit": "nîtan", "gloss": "to lead", "script": null},
            {"translit": "ânîtan", "gloss": "to bring", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Nei 3",
        "redirect": "Ne 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Neia",
        "redirect": "Nei 2"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-07T18:18:08.609Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T18:18:08.659Z] TOOL RESULT

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


## [2026-09-07T18:18:30.006Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','UNV','BQT','AHD','MON','KLN','HRN','SYN','KNT','PHD','NYB','BRT','LKT','SKT','ARY','HUB','CHEUNG','PLA','AFM','FVQ','DEV','PHN','LAM','WLD','IEC','WEB','FSD','TAD']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print(k, v.get('kind'), v.get('page_offset'), v.get('local_file'), '|', (v.get('lookup_hint') or '')[:160])\n\""
}
```


## [2026-09-07T18:18:30.608Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -30 && echo --- && ls site/pages/356.jpg 2>/dev/null; ls data/verification/sources/refs/ocr/ | head"
}
```


### [2026-09-07T18:18:31.347Z] TOOL RESULT

```
POK archive_djvu POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD
UNV archive_djvu leaf = printed + 2 (e.g. leaf 9 = p.7); only 48 leaves. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe/data/verification/sources/refs/UNV.txt | Pagination of the 1963 edition differs; use the glossary (Pahlavi words in transliteration) to verify substance.
BQT archive_djvu+local_scan_ocr vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (ret
AHD archive_djvu+website+archive_restricted 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via '
MON website+archive_djvu None ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) b
KLN archive_djvu KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:
HRN archive_djvu leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai
SYN archive_djvu leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept headin
KNT archive_djvu leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt | Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$1
PHD archive_djvu leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsi
NYB archive_djvu Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates 
BRT archive_djvu Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is 
LKT archive_djvu leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt | Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in translit
SKT archive_djvu leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
ARY local_scan_ocr printed page = pdf page + 1 ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan
HUB archive_djvu leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Pers
CHEUNG MISSING
PLA archive_djvu 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] | HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use:
AFM archive_djvu 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt'] | Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as 
FVQ archive_djvu printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] | Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
DEV archive_djvu leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt | French headword in caps at line start.
PHN archive_djvu leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt | French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.
LAM archive_djvu leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt | French headword in caps at line start with running heads like '2 ABRI'.
WLD archive_djvu Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP v
IEC archive_djvu TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
WEB archive_djvu not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt | Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1
FSD archive_djvu vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
TAD archive_djvu 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image ['/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt'] | Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
```


### [2026-09-07T18:18:31.393Z] TOOL RESULT

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
---
site/pages/356.jpg
AFM
ARY
BOOK
BQT
FFD
HRN
IRN
PLA
SNS
SOD
```


## [2026-09-07T18:18:35.148Z] TOOL CALL #7: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/356.jpg"
}
```


### [2026-09-07T18:18:35.175Z] TOOL RESULT

```

```


## [2026-09-07T18:18:46.585Z] TOOL CALL #8: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob,os\nfor f in sorted(glob.glob('data/verification/page-3*.json'))[-8:]:\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e.get('nodes',[]):\n            if not n.get('words'):\n                print(f, e.get('root'), json.dumps(n,ensure_ascii=False)[:900]); print('---')\nEOF"
}
```


## [2026-09-07T18:18:46.856Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nei-\" POK_full.txt | head -40"
}
```


### [2026-09-07T18:18:48.563Z] TOOL RESULT

```
data/verification/page-347.json Nabatu {"id": 6, "lang": "French", "words": "", "verdict": "plausible", "derivation": "The empty pass-through node stands for French naphte (m.) 'naphtha', the form from which the chemical derivative naphtaline was coined in Paris in 1821 and which is what node #7 needs. Standard French lexicography takes naphte from Latin naphtha (attested in French from the 16th c. as a learned borrowing, with the Greek-Latin -phth- simplified in pronunciation), which makes the Greek → French arrow of the chart correct as an ultimate route but not a direct one. Nourai's own reference disagrees on the immediate donor: Pihan p. 283 s.v. NAPHTE marks it '(A.)' = Arabic, from نفط nafṭ, and argues that the spelling naphthe found in some dictionaries is 'calqué sur le grec νάφθα; mais ce dernier mot n'est lui-même qu'une transcription de l'arabe naft'.", "derivation_fa": "این گرهِ تهی نمایندهٔ فرانسویِ naphte «نفت»
---
data/verification/page-35.json Âdhâmah {"id": 3, "lang": "Latin", "words": "", "verdict": "disputed", "derivation": "An empty pass-through box: Latin Adam, the indeclinable biblical name. The word itself is real — it is the form of the Vulgate (Gen. 2-5, Rom. 5:14) — but the arrow drawn into it is wrong. Latin got the name from the Greek Ἀδάμ of the Septuagint (3rd-2nd c. BCE) and of the New Testament, which transliterated Hebrew אָדָם directly; the Vetus Latina and then Jerome (c. 400 CE) simply kept the Greek spelling. Arabic آدَم, Nourai's drawn parent, is first attested in the Safaitic/pre-Islamic period and became a written language word only in the 7th c. CE, i.e. centuries after Latin Adam was in use, and no modern authority routes any European form of the name through Arabic. The correct chain is Hebrew (#1) → Greek Ἀδάμ → Latin Adam → English.", "derivation_fa": "جعبه‌ای گذری و تهی برای Adam لاتینی، نام کتاب‌مقدسیِ ص
---
data/verification/page-36.json Agaru {"id": 1, "lang": "Syriac", "words": "", "verdict": "confirmed", "derivation": "Empty pass-through node standing for the Aramaic/Syriac stage. Akkadian agāru 'to hire' was taken over into Imperial Aramaic as ʾgr (ʾăgar 'he hired'), Syriac ܐܓܪ ʾegar 'to hire', with the nouns ܐܓܝܪܐ ʾăgīrā 'hireling, hired labourer' and ܐܓܪܐ ʾagrā 'wage, reward'. The Aramaic forms keep the Akkadian consonant skeleton unchanged (ʾ-g-r); the word is far commoner in Syriac than in Jewish Aramaic, which is why Jeffery makes Syriac specifically the donor to Arabic. Placing Syriac between Akkadian and both Arabic and Greek is therefore right for the Arabic branch and at least defensible for the Greek one.", "derivation_fa": "گرهی گذری و تهی که جای مرحلهٔ آرامی/سریانی را نگاه داشته است. اکدی agāru «اجیر گرفتن» در آرامی هخامنشی به صورت ʾgr و در سریانی ʾegar «اجیر گرفتن» وام گرفته شده است، با اسم‌های ʾăgīrā «مزدور» 
---
data/verification/page-36.json Agaruh {"id": 7, "lang": "Greek", "words": "", "verdict": "plausible", "derivation": "The unlabelled Greek node stands for ἀλόη 'aloe', first in Dioscorides (Materia Medica iii.3, 1st c. CE) and in John 19:39 (σμύρνης καὶ ἀλόης); the word is absent from Hippocrates and Theophrastus, so it enters Greek only with the Roman-period trade in the drug. Everyone agrees it is an Oriental loan; the disagreement is over the immediate donor. Klein (and Nourai following him at the top of this entry) says 'prob. borrowed fr. Heb. ahalim, ahaloth'; the current treatment (Beekes; Wiktionary) has it enter Greek through Aramaic in the 1st c. CE — cf. Syriac and Christian Palestinian Aramaic cognates — with the ultimate source Old Tamil akil. Either way the node's position between the Semitic word and Latin is right; only 'Hebrew' vs 'Aramaic' as the exact donor is open. Greek -η renders the Semitic feminine plu
---
data/verification/page-36.json Agaruh {"id": 8, "lang": "Latin", "words": "", "verdict": "confirmed", "derivation": "Unlabelled node = Latin aloē, -ēs, a straight learned borrowing of Greek ἀλόη retaining the Greek first-declension inflection; it is the form Pliny uses ('The best Aloe is brought out of India', Nat. Hist. xxvii) and the form of the Vulgate at John 19:39, whence it passed into every medieval European pharmacopoeia. Latin also formed the compound lignum aloēs 'aloes-wood', the source of English lign-aloes.", "derivation_fa": "گرهٔ بی‌برچسب همان aloē لاتینی است، وامی عالمانه و مستقیم از ἀλόη یونانی که صرف نخستِ یونانی را نیز نگاه داشته است؛ همان صورتی که پلینیوس به کار برده («بهترین aloe را از هند می‌آورند») و همان صورت وولگات در یوحنا ۱۹:۳۹، که از آنجا به همهٔ داروسازی‌های اروپای سده‌های میانه رفته است. لاتینی ترکیب lignum aloēs «چوب عود» را نیز ساخته که سرچشمهٔ lign-aloes انگلیسی است؛ ادعای نورایی در این گره د
---
```


### [2026-09-07T18:18:48.603Z] TOOL RESULT

```
32957:/■extensions ghnei-, ghneid(h)-: 
45357:A /-basis in kneig"h-, knei-b- " incline '? (see there). 
45563:kenei-s-: Lithuanian knisue\.c., see below. 
45575:k(e)nei-d-. 
47677:Root / lemma: knei-g^h-, knei-b- 
47699:Besides Indo Germanic knei-b-\v\ Old Icelandic hmpa {*hnTpen, -on) " allow the head to 
59535:Note: extended mehneh-. mnah-ar\6 mneh-, irienei-. mehi- 
59545:reason; devotion, prayer' {*menei-: irienT-); Old Indie manute^ thinks '; manati^ mentions ' 
59643:{muna/Pirom *menei-eti= Old Indie manay-ati, compare mene-\v\:) Old High German 
62151:See also: probably to nei- S. 312 f. 
62239:Root / lemma: nei-1, neie-. nT-{*hoin^ 
62249:Gen. Sg. Proto Irish netas. Old Irish math {*nei-t-os, s. also nei-2)\ Hittite /75/- "steer, guide, 
62257:Root / lemma: nei-2, neie- : m- {*hoin-) 
62263:(back)l gleam; smile back (at) ' (with present formation -d(h)-)\ *nei-b^o-\x\ Middle Irish 
62473:/7e/"not' {nei-p' nor; and not| not| neither '); Gothic nei{ajT. Asy.) "not'. Old Icelandic nfno'. 
63018:Root/ lemma: ne-tr-, ne-tr-: snake, derived from Root/ lemma: (s)ne-3x\(^ (s)nei-\ to sew 
63045:Root / lemma: /?/-, nei- i*he- nei-) 
79227:Root /lemma: (s)ne-ax\6 (s)nei- 
79231:Note: (maybe from the present sne-Jd\ or backwards s/7e-from snei-l); compare the 
79264:5-loose: natns "leinen, zwirnen', nat(e)ne = snat(e)ne\ *nT- as zero grade to *nei- (see
```


## [2026-09-07T18:18:54.379Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '62235,62300p' POK_full.txt"
}
```


### [2026-09-07T18:18:54.428Z] TOOL RESULT

```
References: WP. II 321, Trautmann 195 f.; J. Loth RC. 40, 352 f.; 41, 193 ff. 

Page(s): 761 

Root / lemma: nei-1, neie-. nT-{*hoin^ 

Meaning: to lead 

Material: Old Indie /7ay5// (participle mta-), Avestan /75ye/// "leads'. Middle Persian mtan 

"guide, lead, drive, push'. Old Indie mthai. " direction, way', mtho, /7e/a "guide, leader', 

netar-, netar-m. 6s., netra-n. " direction, eye'; Middle Irish ne, /7/a "warrior, hero ' {*neit-s). 

Gen. Sg. Proto Irish netas. Old Irish math {*nei-t-os, s. also nei-2)\ Hittite /75/- "steer, guide, 

lead'. 

References: WP. II 321, Pedersen Hittite p. 77 f., 81, Frisk Suffixales -th- 5 f. 

Page(s): 760 

Root / lemma: nei-2, neie- : m- {*hoin-) 
Meaning: to move vividly, be excited; to shine 

Material: Latin nited, -ere^ shine| glitter| look bright; be sleek/in good condition; bloom| 
thrive ', nitidus^ shining! bright ', nitor^ press/lean upon; struggle; ADVance; depend on 
(with abl.); strive] labor, radiance ' (from a participle *ni-t6-); perhaps re-mdeo^ shine 
(back)l gleam; smile back (at) ' (with present formation -d(h)-)\ *nei-b^o-\x\ Middle Irish 
mab^ vitality ', cymr. nwyf6s.\ noi-b^o-\v\ Old pers. naiba-, npers. /7eM/ "beautiful, good', 
Old Irish /7c»Z&"holy'; *ne/-ma\n Middle Irish n/am 'radiance, beauty'; *ne/-ko-\n Middle 
Irish nlacbm. " hero ', n/achusm. " braveness'; *ne/-to-\n cymr. /7tvyo'"ferventness, passion', 
hispan. war god Neto; Old Irish PN Ma// {Gen. Ne///) from *ne/t-s-/o-s, placed perhaps also 
in Old Irish /7/a" hero ' (see ne/-1)\ Germanic *n/Pa-\n Gothic ne/f^n. " envy ', Old English 
nTdm. "fight, struggle, hate, enmity'. Old Saxon Old Frisian /7/?/7" eagerness, hate, envy ', 
Old Icelandic nfd' derision, ridicule, disgrace, shame'; could also belong to Old Irish mtbn. 
(Indo Germanic *n/lu-) "fight, struggle'; dubious Old Indie /7/7a- "bluish black', nayana-n. f. 
"eye', netra-n. ds. 

References: WP. II 321, 336, WH. II 168, 171, Vendryes RC. 46, 265 ff. 
Page(s): 760 

Root / lemma: ne/-3, ni- {*houn-) 



See also: see above S. 312 f. {en-). 
Page(s): 760 



Root / lemma: neR- {*hounR-) 

Meaning: death, dying; dead person 

Material: Old Indie nasyati, nasati^ gets lost, disappears, passes away ', nasayat/" makes 

disappear, ruin' (lengthened grade compared with Latin noceo^ harm'), Avestan nasye/t/' 

disappears ', participle Old Indie nasta-' lost ', Avestan nasta- ds. (= Latin e-nectus), 

nasista- " most perishable ', nas- f. 'need, misfortune' (= Latin nex, gr. vsK-rap, veke^; Old 

Indie -nasM].), nasu- 'corpse, carrion ' (= gr. v£ku(;, Latin nequ-alia; compare *nRu-\v\ Old 

Irish ecetc), lengthened grade Old Indie nasa-m. ' das Zuniehtewerden '; gr. v£K£(; vcKpoi
```


## [2026-09-07T18:19:26.793Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_02 leaf 416 (p.760) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==416' POK_02.txt | head -60"
}
```


### [2026-09-07T18:19:28.048Z] TOOL RESULT

```
=== POK_02 leaf 416 (p.760) ===
uchtsau');  aisl.  mostr  , große  Menge'  (*muh-stra-)]  einzige  Hoch- stufenform in  ags.  meagol  ,(*klumpig,  massig'  =)  ,fest,  stark'.
WP.  II  311;  nach  Hubschmid  ZnPh.  66,  33  f.  nichtidg.
inüs  jMaus'  auch  ,Muskel'  (älter  *müs,  musös  aus  *meus,  musös). Ai.  mü§-  m.  ,Maus,  Ratte',  np.  mü§  ,Maus';
arm.  mu-kn  ,Maus,  Muskel' ;  gr.  (j,vg  (^vdg,  ^vv  nach  ^g,  ''vög,  ^v)  ,Maus', auch  jMuskel';  alb.  ml  ,Maus',  lat.  müs  m.  ,Maus'  (mürlnus  :  mhd.  miusln
753
von  Mäusen*) ;  ahd.  mhd.  as.  mnd.  aisl.  ags.  müs  ,Maus,  Muskel'  (Kons. -St.) ib<^.  ""^y^^  ^'  »Maus'.
Vielfach  auf  Körperteile  angewendet:  arm.  muJcn  , Muskel',  gr.  (xvg Muskel',  [xv(bv  ,muskelreiche  Gegend  des  Leibes'  (woraus  auch  , wollüstiges \Veib'  in  gr.  ^vwv/a),  jwua^,  -aycog  m.  ,MiesDauschel,  Löffel'  :  lat.  mürex Purpurschnecke';  lat.  musculus  ds.,  ,Muskel',  ahd.  usw.  müs  ,Muskel,  bes. des  Oberarms',  mnd.  müs  bes.  ,der  Fleischballen  des  Daumens',  nhd.  Maus^ Mäuschen,  abg.  myhca  ,/9^orxtW';  andrerseits  ai.  muskd-  m.  ,Hode,  weibliche Scham',  npers.  musk  ^Bibergeil'  (aus  dem  Pers.  stammt  gr.  (xöayog,  nhd. Moschus)]  gr.  ixvGxov  , Geschlechtsorgan' ;
wohl  zu  ai.  musnäti  , stiehlt,  raubt'  usw.,  s.  unter  2.  meu-  , fortschieben'.
WP.  II  312  f.,  WH.  II  132  f.,    Trautmann  191,   Specht   Idg.  Dekl.  40f.
rnat-o-s  ,gestutzt'?
Lat.  mutilus,  mtitidus  ,verstümmelt',  *muticus  ,gestutzt',  mütöj  muttö Penis',  GN  Mutunus,  rom.  mutt-  ,abgestumpft' ;  ir.  mut,  gael.  mutach ,kurz'  (mit  expressivem  tt)\  vielleicht  auch  ir.  moth  ,penis'  als  , Stummel'.
WP.  II  312,  WH.  II  136 f.;  nach  E.  Lewy  eher  zu  lat.  mütus  S.  751, vgl.  , stumm' ;  ,verstümmeln'.
48
1.  nä-  jhelfen,  nützen*.
Ai.  nä-tha-  n.  , Hilfe*,  m.  ,Schützer'7  nä-tha-te  ,fleht*;  gr.  d-vl-vTi-ui -vä-fiev  ,nütze*,  Fut.  d-vrj-oojj  Med.  d-vi-vä-f.iat,  Aor.  <hn^fir]v  ,habe  Nutzen* oveiaq  n.,  richtiger  })vr]aQj  -arog  ,Nutzen*  (*o-7iä-wf),  usw.     '  |
WP.  II315.
2.  nä-  ,sich  fürchten,  schämen*,  Verbalnomen  auf  -sor-,  -sr-.
Air.  nä»'  ,bescheiden*  {*nä-sro-\  nd{i)re  , Scham*  (*7iä-smä);  hitt.  naÄ(Ä)- , fürchten,  sich  fürchten*,  nahSariia-  ,sich  fürchten*. H.  Pedersen  Hittitisch  187.
näg^h-  ,nüchtern*?  Nur  arm.  und  griech.
Arm.  naut'^i  ,nüchtern*;  gr.  viqcpw,  dor.  vdq)(a  ,bin  nüchtern*. WP.  II  317.
nak-  ,Fell*.
Gr.  vd%og  n.,  ya^rj  f.  , wolliges  Fell,  Vlies*,  äQvay.lg  f.  (für  *dQvo-vaxig) , Schaffell*,  vayiv(6)QL0v'  öig^a  Hes. ;  ags.
```


## [2026-09-07T18:19:28.358Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN lilac/anil/aniline/nice ===\"; grep -n \"^lilac\\|^anil\\|^aniline\\|^indigo\" KLN_1966.txt KLN_1971.txt | head -20\necho \"=== KLN leaf for p.1026 ===\"; grep -n \"1026\" KLN_1966.txt | head -5"
}
```


### [2026-09-07T18:19:28.436Z] TOOL RESULT

```
=== KLN lilac/anil/aniline/nice ===
KLN_1966.txt:2807:anile,  adj.,  like  an  old  woman.  —  L.  anilis,  ‘per¬ taining  to  an  old  woman’,  fr.  anus,  gen.  anus, ‘old  woman',  from  the  I.-E.  imitative  base  *an-, whence  also  Hitt,  annash,  ’mother’,  hannash, ‘grandmother’,  Gk.  avvip,  ‘grandmother’, Lith.  ahyta,  ‘mother-in-law’,  OPruss.  ane,  ‘old mother’,  OHG.  ano,  MHG.  ane,  an,  ‘grand¬ father,  great  grandfather’,  OHG.  ana,  ‘grand¬ mother,  great  grandmother’,  G.  Ahnen,  ‘ances¬ tors’,  OHG.  eninchili  (whence  MHG.  eninkel, enenkel,  G.  Enkel),  ‘grandson’,  prop,  dimin. of  OHG.  ano,  ‘great  grandfather'.  Cp.  the  first element  in  Olaf.
KLN_1966.txt:19189:indigotic,  adj.,  pertaining  to,  or  resembling,  in¬ digo.  — •  Irregularly  formed  fr.  indigo  with suff.  -ic.
KLN_1966.txt:19198:indigo) ;  so  called  by  them  in  allusion  to  its  color in  the  spectrum.
KLN_1966.txt:21685:lilac
KLN_1966.txt:21740:lilac,  n.  —  MF.,  fr.  Sp.  lilac,  fr.  Arab,  ldylak,  lilak, fr.  Pers.  lilak,  var.  of  nilak,  ‘bluish’,  fr.  nil,  ‘blue, indigo’,  fr.  OI.  nilah,  ‘dark  blue’,  which  is  of  un¬ certain  etymology.  It  possibly  derives  fr.  I.-E.
KLN_1971.txt:15352:anil, n., 1) a West Indian shrub, from which in- 
KLN_1971.txt:15360:anile, adj., like an old woman. — L. anllis, ‘per- 
KLN_1971.txt:15375:aniline, also anilin, n., an oily, poisonous liquid, 
KLN_1971.txt:15379:anility, n., quality of being anile. — L. anllitas, 
KLN_1971.txt:15381:anile and -ity. 
KLN_1971.txt:122578:indigo, n., a blue dye. — F., fr. Du. indigo, bor- 
KLN_1971.txt:122584:indigotic, adj., pertaining to, or resembling, in- 
KLN_1971.txt:122649:indigo) ; so called by them in allusion to its color 
KLN_1971.txt:122911:aniline , etc.); 2) names of elements (as bromine, 
KLN_1971.txt:137801:lilac, n. — MF., fr. Sp. lilac, fr. Arab. Idylak, lilak, 
KLN_1971.txt:137803:indigo’, fr. OI. nflah , ‘dark blue’, which is of un- 
KLN_1971.txt:271347:anile, for ‘Lith. ahyta' read ‘Lith. anyta ' . 
=== KLN leaf for p.1026 ===
```


## [2026-09-07T18:19:35.490Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_02 leaf 423 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==423' POK_02.txt | head -30\necho; echo \"=== find nei- in POK_02 ===\"; grep -n \"nei-\" POK_02.txt | head -20"
}
```


## [2026-09-07T18:19:37.128Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN_1971 anil block ===\"; sed -n '15350,15395p' KLN_1971.txt\necho; echo \"=== KLN_1971 lilac block ===\"; sed -n '137798,137812p' KLN_1971.txt\necho; echo \"=== KLN_1966 lilac ===\"; sed -n '21740,21744p' KLN_1966.txt\necho; echo \"=== KLN_1971 indigo ===\"; sed -n '122578,122590p' KLN_1971.txt"
}
```


### [2026-09-07T18:19:37.824Z] TOOL RESULT

```
=== POK_02 leaf 423 ===
nä-  r\.  f.  ,Auge', netra-  n.  ds.
WP.  II  321,  336,  WH.  II  168,  171,  Vendryes  RC.  46,  265  ff.
3.  nei-,  ni-  s.  oben  S.  312  f.
I.  neid-  ,heruntermachen,  schmähen'.
Ai.  nindati,  Pass.  nidyd-te  , schmähen,  tadeln,  verachten',  dnedya-  ,nicht zu  schmähen',  nid-,  nidä,  nidä,  nindä  , Schmähung,  Tadel,  Verachtung'; av.  naed-  (näisml)  ,schmähen';  arm.  anicanem,  Aor.  3.  Sg.  anec  ,fluche' (*oneid-s-et) ;
gr.  ^vsLÖog  , Vorwurf,  Schmach',  dvsiöi^a)  , schmähe'  (o-Präfix  ,be-schimpfe', wie  auch  arm.  anicanem) ;  got.  ga-naitjan  , schmähen',  naiteins  , Lästerung', ■  ahd.  neizzen  , quälen,  plagen',  ags.  ncetan  ds.;  lit.  niedeti,  lett.  nist  ,ver- achten',  naids,  naidus  ,Haß,  Feindschaft'.
WP.  II  322  f.,  Kuiper  Nasalpräs.  130,  Trautmann  193;  wohl  zu  nei- S.  312f.
r
761
ueid-  '  n^d-  ^fließen,  strömen',  FIN  Neidä,  Nidä.
^i.    nedati  ,  flließt,    strömt';    gall.    FIN   Nida   ,Nidda'    und   ,Nied',    brit. pi^  Nida,  cymr.  Nedd  ,Neatli' ;  vollstufig  poln.  FIN  Nida,  lit.  FIN  Niedä, apr.  FIN  Nyda  ,Neide'. J.  Löwenthal  ZONF.  6,  81,  Krähe  BzNF.   1,  248ff.
aeig^-  ^waschen';  Pass.  Partiz.  nig'A-to-.
Ai.  nBnekti  , wäscht,  reinigt',  Aor.  anäiksU,  Pass.  nijyate,  Partiz.  niktd-, ninikta  Imper.  , waschet',  Kaus.  nejdyati-,  Aor.  naBnizaiti  Intens.  , wäscht ab,  spült  weg';  gr.  vit,o}  (*nig'^iö  =  ir.  nigim)  ,wasche',  Fut.  vlipw,  Aor. l^/ii//«,  viTtTQOv  ,Waschwasser',  x^Q-^'^yj  ds.,  ä-viTizog  ,ungewaschen'  (=  ai. niUd-,  ir.  necht)]  gr.  äviyqög  .^äy-ad-aq-coc,^^  ]  lat.  noegeum  (^noigV:-io-)  ,Schweiß- tuch^;
air.  nigid  , wäscht'  {'^nig^ieti,  Verlust  der  Labialisierung  vor  x),  Fut. -ninus  =  ai.  (Gramm.)  niniksati-,  necht  ,rein';  mcymr.  enneint  ,Bad' (*an-nig-antio-]  das  g  aus  dem  Präs.  übertragen);
germ.  *nikwe8^  -us-  in  aisl.  nykr  (Gen.  nyks)  , Wassergeist,  Flußpferd', ags.  nicor  ,Wasseruntier,  Krokodil',  ahd.  nihhus,  nichus  , Flußuntier, I  Wassergeist',  nhd.  Nix,  ahd.  nichussa  , weiblicher  Wassergeist,  Nixe', mndl.  nicker,  mnd.  necker  , Wassergeist'.
WP.  II  322,  Thurneysen  Gr.  115;  anders  Vendryes  RC.  47,  442  ff.
neik-  , Getreide  schwingen'.
Gr.  XiTiLidü)  jhandhabe  die  Getreideschwinge',  Xiy.fxr)rrJQ  ,der  das  Getreide schwingt',  Xi^iög,  XUvov  , Getreideschwinge',  diss.  aus  *viyLu6q,  *vUvov, vgl.  veTaXov,  vUXov,  vL'/,a '  XiTifj,^  Hes.,  wie  auch  tx^«y  •  Xixfiav  Hes.  (oder Haplologie  hinter  ava :  dvLy.^cbi.ied'a) ;  mir.  cruth-necht , roter  Weizen',  cymi-. nithio,  bret.  niza  , worfeln'  (auch  wohl  cymr.  gwenith,  bret.  gioiniz,  corn. gwaneth  ,  Weizen') ;  lit.  niek�

=== find nei- in POK_02 ===
1391:i-Erweiterungen  ghnei-,  ghneid{h)-:
3095:Weitere  Verbindung  mit  lat.  sclpio,  gr.  O'kIttwv  und  Wurzel  skmp-  ,schnei- den*  ist  wahrscheinlich.
3334:Eine  i-Basis  in  kneigVi-,  knei-b-  ,neigen'?  (s.  dort).
3376:lit.  kniebiüj  kniebti  ,leise  kneifen';  lett.  knäb-ju,  -u,  -t  ,picken,  zupfen', Iter.  knäbat]  lit.  knab-üj  Mi  ,schälen  (Kartoffeln  u.  dgl.)',  knabüs  ,lang- fingerig,  diebisch,  geschickt',  knabenti,  knebenti  .(auf)  picken',  knimbuy -aUj  krvtbti  ,zupfen,  klauben',  lett.  knibet^  knibindt  Iter.  ,klauben'  {-ni- kann  Tiefstufe  zu  -ne-  sein);  ob  die  folgenden  Worte  erst  aus  knib-  ge- folgerten Ablaut  nach  der  i-Reihe  haben  oder  z.  T.  alte  Reste  der  i -Variante kenei-bh-  sind,  ist  nicht  sicher;  lit.  knyburiuoti  ,mit  irgendeiner  Hand- oder Fingerarbeit  beschäftigt  sein',  lett.  knieb-ju,  -u,  -t  ,zwicken',  Iter. knaibit.
3380:got.  hnasqus  ,weich.  fein'  (von  Kleidern;  ursprüngl.  entweder  ,durch Reiben  oder  Knistern  weich  gemacht'  oder  ,weich  wie  gekratzte  Wolle'), ags.  hnesce  ,zart,  weich,  schwach',  ahd.  [Kjnascön  ,naschen  (*abknipsen), Leckerbissen  genießen';  lett.  knüosti,  knuost  ,mit  dem  Schnabel  im Gefieder  rupfend   Vgl.  von  der  i-Basis  kenei-s-:   lit.  knisü  usw.,  s.  unten.
3383:2.  Dentalerweiterungen: k(e)nei-d-:
4186:knei-g^h-,  knei-b-  ,neig-en,  sich  biegen'.
4189:Daneben  idg.  knei-b-  in  aisl.  hnlpa  (*hmpen,  -ön)  ,den  Kopf  hängen lassen,  mißmutig  sein',  hntpinn  ,  miß  mutig',  gnlpa  f.  (*ga-hnlpön')  ,über- hängender  Felsen',  ags.  hnipian  ,den  Kopf  hängen  lassen,  mißmutig  sein'; got.  *ga(h)nipnan  ,traurig  sein';  lit.  knimhü,  kmhti  , zusammenknicken'.
5445:Ai.  lunäti,  lunöti  , schneidet,  schneidet  ab',  lünd-  ,abgeschnitten,  ge- schnitten' ( :  mir.  Ion),  lavitra-  n.  ,Sichel',  lavi-  f.  ds.  ( :  gr.  Xatov,  aisl.  U ds.),  lava-  m.  ,das  Schneiden,  Schur,  Wolle,  Haar,  Abschnitt',  läva-  , schnei- dend', lävaka-  m.  , Abschneider,  Mäher';
5692:2.  d-Er Weiterung:  got.  maitan  ^hauen,  schneiden^  aisl.  meita,  ahd.  meizan ^schneiden^,  aisl.  meitill  tu.,  ahd.  meizil  , Meißel^;  ahd.  stein-meizo  , Stein- metz^; dazu  ags.  mite,  ahd.  mlza  ^Milbe^  (wohl  zu  gr.  [xldag  ^Made^),  viel- leicht auch  ags.  se-mette,  engl,  ant,  emmet,  ahd.  ä-meiza  , Ameise^  (^Abschnei- der^);  ob  auch  abg.  medh  ;Erz^,  russ.  mädh  , Kupfer^?
6177:nienei-  :  nieni-]  Nominalbildungen:  men-raen-  n.,  znenos-  n.,  men-ti-^ men-tu-,  nioni-,  znn-ti-,  mn-to-  ,Sinn,  Gedanke',  men-ter-  , Denker'. Ai.  mdnyate  , denkt',  av.  mainyeite  ds.,  ap.  mainyähay  (idg.  *men-i-0', =  gr.  {.laivofxai  ,rase',  air.  -muiniur,  slav.  mhnjq  , meine,'  s.  unten),  ai.  Perf. ma-mne,  mene^  manäy-ati  ,ist  eifrig',  manä-yu-  , eifrig,  fromm',  manl-sä ,Weisheit,  Verstand ;  Andacht,  Gebet'  (*m^nei-  :  m^ni-) ;  ai.  mannte  , denkt'; mdnati  , erwähnt'  (=  lit.  menü,  poln.  -mione,  öech.  -menu);  0.1.  mandyati  ,ehrt , ( :  lit.  is-monis  , Verstand'),  av.  manaydn  ,man  könnte  glauben' ;  Supin.  ai.
6189:got.  *man,  munum  (Inf.  munan,  Prät.  mundo)  , meinen,  glauben'  (Prät* Präs.  wie  ^efxova^  memim,  j.is(j,vr]uaL),  ga-munan  ,sich  einer  Sache  erinnern*^ aisl.  muna  , gedenken,  sich  erinnern',  munu,  mono  , beabsichtigen,  werden**^ ags.  mon,  man  ,(ge) denke',  3.5.  far-munan  (Fvsit.  -munsta)  »nicht  gedenken  ■■■ verleugnen';  got.  schw.  V.  munan  (3.  Sg.  munaip,  Prät.  munaida)  »gedenken (zu  tun),  (xsXXsLv^  (munaip  aus  ^m^nei-eti  =  ai.  manay-ati,  vgl.  m^ne-  [xiA ahd.  ßrmonen  , verachten'  (und  slav.  monäti,  lit.  minUi,  sowie  —  wenn  all —  gr.  ij,av7jvai) ;  o-stuf.  ahd.  as.  manön,  ags.  manian  , mahnen'  (ahd.  maiun 3.  Sg.  =  lit.  mäno  ,versteht',  vgl.  reduktionsstufig  arm.  i-manam  »verstehe' aus  *m^nämi)\  got.  muns  m.  , Gedanke,  Meinung',  aisl.  munr  ,Sinn,  Ver- langen, Lust',  ags.  myne  , Erinnerung,  Verlangen,  Liebe',  as.  muni-lik , lieblich'  (=  ai.  müni');  got.  ana-minds  , Verdacht'  (=  ai.  manti-),  ga-minU n.  , Andenken',  aisl.  minne  , Erinnerung',  ahd.  as.  minn{e)a  , Liebe,  Minne* (*minpjä,  *mindjä)]  got.  ga-munds,  Si^s.  ge-mynd,  ahd.  gi-munt  , Andenken Gedächtnis'  (=  ai.  mati-  usw.);
6615:I.  xze,  ne,  nei  Satznegation  der  reinen  Verneinung  (ne  einzelsprachlich  auch   * Wortnegation   geworden);   n-  Wortnegation;  ne-k"o-s  , nicht  einer', nei-k^o-s  ds. ;  ne-k^e  ,und  nicht*,  ne-ue  ,oder  nicht*. ne:  ai.  nd  ,nicht',   ned   (iidid)   ds.,   av.  ap.  na-  ,nicht',   av.  nöit  (=  ai. ned),  ai.  nd-vä  =  av.  na-va  ,oder  nicht'  (vgl.  lat.  ne-ve,   und  genauer  air.  nö s.  unten) ;  ai.  naca  ,und  nicht'  (=  lat.  neque  usw.) ;
6627:12 ei  betontes  ,nicht':  av.  nae-cis  ,keiner',  adv.  ^laecis  verstärkte  Negation; lat.  7ü,  altlat.  nei  Adv.  und  Konj.  1.  älter  ,nicht,  daß  nicht',  2.  ,si  non', quid-nl-,  osk.  nei  ,nicht'  (nei-p  ,neque');  got.  nei  {&TC.ley.)  ,nicht^  aisl.  nl ,nein',  ahd.  nl  emphatisches  ,nicht';  lit.  nie-kas  ,niemand',  ne%  ,auch  nicht, nicht  einmal' ;  aksl.  ni  ,neque',  ni-Uto  ,niemand' ;  die  germ.  Formen  viel- leicht aber  =  ai.  ned  ,durchaus  nicht,  damit  nicht',  av.  nöit,  ap.  nay  aus idg.  *ne  id  ,das  nicht';  vielleicht  ist  idg.  nei  aus  *ne-\-l  (vgl.  ovtoa-l)  zu deuten.
6660:1.  nei-,  neio-ini-  , führen'.
6661:Ai.  ndyati  (Partiz.  nltd-),  av.  nayeiti  , führt',  mpers.  nltan  , führen treiben',  ai.  nlthä  f.  , Führung,  Weg',  nltho,  netä^  ,Führer',  nitar-,  netdr- m.  ds.,  netrd-  n.  , Führung,  Auge';  mir.  ns,  nla  ,Krieger,  Held'  {*neit-i\ Gen.  Sg.  urir.  netas,  air.  niatJi  {*nei-t-os\  s.  auch  2.  nei-)]  hitt.  näi-,  lenken führen'.
6663:2.  nei-,  neis-  :  ni-  , lebhaft   bewegt   sein,    erregt   sein,   glänzen';    noi-bho-^
6664:,gut,  heilig';  kelto-germ.  nei-to-,  ni-tu-  , Leidenschaft'.
6665:Lat.  niteö,  -ere  ,glänze,  strahle',  nitidus  , glänzend',  nitor  ,  Glanz'  (von einem  Partiz.  *ni-tö-) ;  vielleicht  re-nldeö  , erglänzen'  (mit  präsensbildendem -d(hy)]  *nei-bhO'  in  mir.  nlab  , Lebenskraft',  cymr.  nwyf  ds. ;  noi-bho- in  apers.  naiba-,  npers.  new  , schön,  gut',  air.  nolh  , heilig';  *nei-mä  in mir.  nlam  , Glanz,  Schönheit';  *nei-Jco-  in  mir.  mach  m.  ,Held',  nlachus m., Tapferkeit';  *nei-to-  in  cjmr.  nwyd  , Leidenschaft',  hispan.  Kriegs- gott Netö]  air.  PN  Nlall  (Gen.  NeiU)  aus  *neit-s-lo-s]  steckt  vielleicht auch  in  air.  ma  ,Held'  (s.  1.  nei-)]  germ.  ^nipa-  in  got.  neip  n.  ,Neid', ags.  m(J  m.  , Kampf,  Haß,  Feindschaft',  as.  afries.  nith  , Eifer,  Haß,  Neid\ aisl.  nid  ,Hohn,  Schmach';  könnten  auch  zu  air.  nlth.  n.  (idg.  *i2ifu-) ,Kampf  gehören;  zweifelhaft  ai.  nila-  , schwarzblau',  nayanä-  r\.  f.  ,Auge', netra-  n.  ds.
6667:3.  nei-,  ni-  s.  oben  S.  312  f.
```


### [2026-09-07T18:19:37.967Z] TOOL RESULT

```
=== KLN_1971 anil block ===
anights, adv. (archaic) — Formed fr. OE. on 
nihte; see a-, ‘on’, night, and the adv. suff. -s. 
anil, n., 1) a West Indian shrub, from which in- 
digo is made; 2) indigo. — Port, anil, fr. Arab. 
an-ntl, assimilated fr. al-ntl, fr. a/-, ‘the’, and 
nil, ‘indigo’, fr. Pers. nila, ult. fr. OI. mil, ‘indi- 
go’, fr. nflah, ‘dark blue’. Cp. lilac. 
Derivatives: anil-ic, adj., anil-ide, n., aniline 
(q.v.) 

anile, adj., like an old woman. — L. anllis, ‘per- 
taining to an old woman’, fr. anus, gen. anus, 
‘old woman’, from the I.-E. imitative base *an-, 
whence also Hitt, annash , ‘mother’, hannash , 
‘grandmother’, Gk. avv(?, ‘grandmother’, 
Lith. adyta, ‘mother-in-law’, OPruss. ane, ‘old 
mother’, OHG. ano , MHG. ane , an, ‘grand- 
father, great grandfather’, OHG. ana , ‘grand- 
mother, great grandmother’, G. Ahnen , ‘ances- 
tors’, OHG. eninchill (whence MHG. eninkel , 
enenkel, G. Enkel), ‘grandson’, prop, dimin. 
of OHG. ano , ‘great grandfather’. Cp. the first 
element in Olaf. 

Derivative: anile-ness , n. 
aniline, also anilin, n., an oily, poisonous liquid, 
C 6 H 5 NA 2 (chem.) — Coined by C. J.Fritzsche 
in 1841 fr. anil and chem. suff. -ine, resp. -in. 
Derivative: aniline, anilin , adj. 
anility, n., quality of being anile. — L. anllitas, 
‘the old age of a woman, anility’, fr. anllis. See 
anile and -ity. 

animadversion, n., criticism; blame. — L. ani- 
madversio, gen. -dnis, ‘perception, observation, 
attention’, fr. animadversus, pp. of animadver- 
tere. See animadvert and -ion. 

Derivative: animadversion-al , adj. 




37 



=== KLN_1971 lilac block ===
and subst. suff. -ing. 

Lila, fern. PN. — See Leila, 
lilac, n. — MF., fr. Sp. lilac, fr. Arab. Idylak, lilak, 
fr. Pers. lilak , var. of nilak, ‘bluish’, fr. nil, ‘blue, 
indigo’, fr. OI. nflah , ‘dark blue’, which is of un- 
certain etymology. It possibly derives fr. I.-E. 
base *«?-, ‘to shine’. See neat, adj., and cp. anil 
and the first element in nilgai and in nainsook. 
Derivative: lilac, adj. 

Liliaceae, n. pi., the lily family {bot.) — ModL., 
formed fr. Lilium with suff. -aceae. 
liliaceous, adj. — See prec. word and -aceous. 
Lilith, n., a female evil spirit. — Heb. Lilith , fr. 

=== KLN_1966 lilac ===
lilac,  n.  —  MF.,  fr.  Sp.  lilac,  fr.  Arab,  ldylak,  lilak, fr.  Pers.  lilak,  var.  of  nilak,  ‘bluish’,  fr.  nil,  ‘blue, indigo’,  fr.  OI.  nilah,  ‘dark  blue’,  which  is  of  un¬ certain  etymology.  It  possibly  derives  fr.  I.-E.
Liliaceae
base  *ni-,  ‘to  shine’.  See  neat,  adj.,  and  cp.  anil and  the  first  element  in  nilgai  and  in  nainsook. Derivative:  lilac ,  adj.
Liliaceae,  n.  pi.,  the  lily  family  ( bot .)  —  ModL., formed  fr.  Li  limn  with  suff.  -aceae. liliaceous,  adj.  —  See  prec.  word  and  -aceous. Lilith,  n.,  a  female  evil  spirit.  —  Heb.  Lilith ,  fr. Akkad.  Lilitu  (whence  also  Syr.  Lelitha),  not  re¬ lated  to,  but  folk-etymologically  connected  with, Heb.  ldylah,  ‘night’,  and  explained  accordingly as  ‘night  demon’.
Lilium,  n.,  a  genus  of  plants,  the  lily  (bot.)  —  L. lllium.  See  lily.

=== KLN_1971 indigo ===
indigo, n., a blue dye. — F., fr. Du. indigo, bor- 
rowed fr. Sp. indico , Indigo, fr. L. indicum , ‘in- 
digo’, fr. Gk. Iv8ix6v, ‘indigo’, (short for ’IvSixiv 
(pocpp.axov, lit. ‘Indian dye’), neut. of Tv$ix6<;, 
‘Indian’. See Indie. 

indigotic, adj., pertaining to, or resembling, in- 
digo. — Irregularly formed fr. indigo with 
suff. -ic. 

indirect, adj. — Late L. indirectus (prob. through 
the medium of F. indirect ), fr. in-, ‘not’, and L. 
directus . See direct, adj. and v.
```


## [2026-09-07T18:20:03.646Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN neat ===\"; grep -n \"^neat\" KLN_1971.txt | head; \necho \"=== KLN_1971 leaf containing 'neat, adj' ===\"; grep -n \"to shine\" KLN_1971.txt | sed -n '1,40p' | grep -i \"n[iï]\" | head\necho \"=== AHD watkins nei ===\"; grep -n \"^nei-\\|^nei\\b\\|nei-\\.\" AHD_watkins1985.txt | head -20\necho \"=== UNV nil ===\"; grep -n -i \"nil\" UNV.txt | head -20"
}
```


### [2026-09-07T18:20:03.752Z] TOOL RESULT

```
=== KLN neat ===
118393:neath the cuticle of arthropods (zool.) — 
123277:neath, infernal’. See infernal, 
158620:neath’, v^pTspo?, £-v£pxepo?, ‘nether, infernal’, 
159430:neat, n., an animal of the ox family; cattle. — 
159446:neat, adj., pure, undiluted; cleanly, tidy; elegant. 
159462:neath. 
=== KLN_1971 leaf containing 'neat, adj' ===
30289:fulgere , ‘to shine’, fulgur, ‘lightning’, fulmen (fr. 
=== AHD watkins nei ===
776:sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contracted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old English wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixed form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
=== UNV nil ===
444:aivsart  niliand  awsart  pa  pust  us  dahand
695:AA’örterbnchern  mit  'Laute’  und  mit  'Harfe’  bestimmt;  s.  PahlT.  113.  8.  17  (wozu Bthl.  IF.  57.  88).  —  ^  vin  'Laute’:  s.  arniLAA'.  vin.  Hbm.  AGr.  247.  —  ^  vin-liannär: nach  CSachs  Langhalslaute  mit  Straußeneikorpus:  s.  aram.  X^22.  —  “  mustaJ::  oh sva.  np.  'Faust’?  ]\Ian  kann  auf  der  Fau.st  (oder  vielmehr  den  beiden  Händen)
735:No.  10.  —  zen:  bedeutet  sonst  ‘IVaffe’  und  —  wie  das  np.  —  'Sattel’;  s. No,  10.  —  zang  'Glöckchen’,  s.  np.  arniLW,  zangak.  —  zil:  zu  türk.-kurd.
```


## [2026-09-07T18:20:04.625Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 286 (p.265) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==286' HRN.txt | head -50"
}
```


### [2026-09-07T18:20:05.851Z] TOOL RESULT

```
=== HRN leaf 286 (p.265) ===
- 264 —
4. afsTultan Vernichten; abnehmen', awsiuitan, afstn-
(i)sn.
Scheint ein Causativuni mit der gewöhnlichen phlv.
Endung -imtan (np. dagegen -ämdeN) zu sein. Bar-
tholomae denkt dagegen nach briefl. Mitteilung an
Zusammenhang mit aw. hisidyät etc. (vergl. oben
No. 922).
5. agräl, agre Vortrefflich' (AW.-Komm., Bund.).
aw. ayrya' Vorzüglich ; ai. agriyd",
6. ahöklnltan Verunreinigen, beschmutzen', ähökinttär
(aw. ähitl', vd. 20, 14), ahökm{i)sn (aw. ähiti-) ^).
Nur ähö (Reim: Vis und Rämin, S. 48, Vers 2),
phlv. äliök, ist im Neupersischen erhalten.
7. ahlav *fromm, gottesfürchtig (Nöldeke, ZDMü. 31,
557).
ap. arta- (in Comp.); aw. areta, asa-; ai. ^td-,
8. ahü 1) *Herr'.
aw. ahü- 'Herr ; lat. erus (Brugmann).
Das Wort scheint nur als Transcription von aw.
ahü' im PehlevT zu existiren.
2) *Welt\
aw. adhu' 'Welt*.
9. akdin ungläubig, aköman.
aw. ahi' *böse* (im Pehlevi aufgegeben), "^akadaeua-
(vergl. ayadaena-)^ akem manö.
10. a'inäva/nd 'stark, mächtig' (Pehlv.-Yasna, Men. etc.).
aw. amavant- stark'; ai. dmavant-,
11. amültär unverletzbar'.
Das mit aw. amnyamna- (vergl. Geldner, KZ.
25, 557 Note 49 und dazu Bartholoraae, Studien
II, 179) von Justi, Bund., zusammengebrachte Wort
muss aus dem Wortschatze des PehlevT gestrichen
werden (West, Sacred Books of the East, Vol. V,
p. 5 Note 2).
^) Fr. Müllers Lesung aiwakinltann in Eins zusammenbringen,
vereinigen, mischen* und dann 'verunreinigen* (WZKM. 5, 64) halte ich
nicht für richtig.
```


## [2026-09-07T18:20:21.028Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 287 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==287' HRN.txt | head -60\necho \"=== HRN nitan/anitan ===\"; grep -n \"nltan\\|nītan\\|nitan\" HRN.txt | head -20"
}
```


### [2026-09-07T18:20:22.393Z] TOOL RESULT

```
=== HRN leaf 287 ===
- 265 -
12. anaiv nicht arisch; boshaft, feindlich*, anainh (Men.).
aw. miairya-,
np. ener schlechter Charakter ist unbelegt (die laut-
gesetzliche Form müsste nEr lauten), die Riväyets
haben arier als ^ungehorsam'.
13. anäklh 'Unheil etc.'
Das sehr häufige Wort ist aufgegeben; das seltene
anäk (AV.) hat sich dagegen im np. näk erhalten
(s. oben No. 1020*»»»).
14. andarvnl Atmosphäre, Luftraum .
aw. *aütarevat/u-; ai. *antarc(lyU',
Im Neupersischen soll endervä {endenväl 'Bedürfniss*
vergl. unter bayisten, oben No. 179) 1) aufgehängt,
hangend; nieder (den Kopf nach unten)' bedeuten.
FJ citiert hierfür als angebliche Belege die beiden
folgenden Verse (Kamal):
^i kl ez her ser-). mö-yl tu etil endercäst (sie)
yeJc sPr-l mö-yt türCL her dö jäidn nem-l bdhdst
Kemäl Ismail.
ger bemihr-i tu myerdäned ztmüne ^) rayträi
göyM ez yem röz-ü seb jCLy-l vey endervüyi vdi
Hekim Qaträn.
2) erstaunt, bestürzt* (mit Vers aus Enverr).
15. angöSttak *Art und Weise' (Men., Bund., ZPGl.).
Die Lesung ist unsicher; West liest neuerdings
(mir völlig unwahrscheinlich) 'angiim-altak und über-
setzt counterpart, similitude* (Bund.). Jedenfalls kann
auch West' 8 erste Erklärung aus angösUan ^umarmen'
nicht beibehalten werden ; np. engösTden existirt nicht.
16. änUan 'herzubringen*.
aw. *Ä + V^iiay-; ai. cL -i [/^yiay- 'herbeigeleiten,
-führen, -bringen, -holen\ Vergl. phlv. nitan.
17. antarmäh 'Neumond'.
aw. aütaremaofiha" 'Neumond'.
') Corrigirt aus zi zemätie^ aber die beiden Zeilen sind wohl nicht
ganz in Ordnung.
=== HRN nitan/anitan ===
1236:vergl. öfttnltan, äwäZ'öft(i)smh (vd. 16 (64) Gl.),
2620:vimär, vlmärlh (Men.), virnärinltan (y. 30, 6 nach
3039:*) So lese ich statt nvedlnltan.
3169:pütaky püslnitan, püs(i)sn^ arm. LW. put (aaß^pog, v6&og) ;
3458:tacänitan (Bund.), täc(i)sn (Bahmy§t), viel häufiger mit
3617:stehlen; phlv. tarftlnltan durch List wegnehmen*
7108:farjam 'Ende', frajämtnltany vergl. fraj(a)ftan (AV.,
7257:phlv. kahltan, kähet, kälünltan, käh{i)sn (Men. s. v.
8872:berühmt*, nämlnltan (PPGrl.); ai. wamaw- ; arm. anim
9130:n(i)vedinltan gelesen werden zu müssen (vergl. No. 314).
10035:6. ahöklnltan Verunreinigen, beschmutzen', ähökinttär
10060:^) Fr. Müllers Lesung aiwakinltann in Eins zusammenbringen,
10094:-führen, -bringen, -holen\ Vergl. phlv. nitan.
10185:37. iiiväklh 'Hilfe, Beistand' (AV.), vergl. awäklnitan
10290:54. candTnltan 'erregen (AV.).
10720:130. maranclnltan 'tödten, vernichten', häufig.
10736:182. ftiaslnitan (aw. [/^maet- , mi^naitl entsprechend ;
10749:135. menitan meinen, glauben \ sehr häutig.
10817:149. n{i)v{i)hlnltan 'kund tun, vd. 17 (26) u. ö. (nach
11051:191. Hiiflfßnltan zufriedenstellen', snäfjm(i)sn, snäyTnitärlli,
```


## [2026-09-07T18:20:23.320Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== UNV nilufar ===\"; grep -n -i \"lufar\\|lofar\\|nllufar\\|nilup\\|nylwp\" UNV.txt | head -20\necho \"=== UNV leaf count ===\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' UNV.txt\necho \"=== PHD nay ===\"; grep -n \"^nay\\|^ny\\|nītan\\|^nī\" PHD.txt | head -20\necho \"=== PHD_mackenzie nay ===\"; grep -n \"^nay\" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-07T18:20:24.583Z] TOOL RESULT

```
=== UNV nilufar ===
=== UNV leaf count ===
47
=== PHD nay ===
508:nay [KN YA < A gny’; та | N ~] reed, cane. nay-, v. nidan.
509:nay [nd | M my, N ~] tube, flute, clarion; pole, perch (10 ft.).
5038:nay! kundāgīh kundāg nayestān! kandan kanīg kanīzag xwan-! xwandan! -gen
=== PHD_mackenzie nay ===
3682:nay [KNY A < A '1ny); n)d IN --] reed, cane.
3683:nay-, v. nidan.
3684:nay [n)d 1M n»', N --] tube, flute, clarion; pole, perch (10 ft.).
3688:nayestan [KNYAst)n ' 1N --] reed-bed, cane-brake.
3689:nayiza~ [n)ycl~'    I N --a] small reed, straw.
3690:nay-sray [n)dsPd] flautist.
9635:nayt
9648:naycstiinI            \l"~,~                   kiswiin
10404:nay, nay, 1-2way, way               ...... ,       udI
```


## [2026-09-07T18:20:34.416Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD nidan ===\"; grep -n \"nīdan\\|nidan\" PHD.txt | head\necho \"=== KNT leaf 208 (p.193) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==208' KNT.txt | head -40\necho \"=== KNT nay ===\"; grep -n \"^nay\\|nay-\" KNT.txt | head -15"
}
```


## [2026-09-07T18:20:35.038Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN leaf 736 (p.712) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==736' SYN.txt | head -40"
}
```


### [2026-09-07T18:20:35.942Z] TOOL RESULT

```
=== PHD nidan ===
128:delete mezidan ... suck. for ?mēzišn ... read ! meziin ... for mistan, *mēz- read... *mēz-.. mihoxt [mytwht' = Av. midaoxta-| falsehood. *mihr .. add ~ druxtan : break faith. add mizīdan, miz- [myc-ytn' | N mazidan] suck. for *moy-mard ... read mowmard ... mēy ... add M mwy. read nüxun [n^hwn' | P nxwn, N nàxun] (finger) nail. delete nāyīzag ... (read wezag). nek, ~th ... add benefit. nibastan ... delete SKBHWN-tn' < A Vškb; nibastan ... read M nb’st, P nb’y-. nibeg ... add M nbyg. nibištan ... |YKTYBWN-tn'... (not -stn'). nidan, nay- |DB(Y)LWN-tn' < A Ydbr |... nigün, ~sar |-s 1 | (P ngws’r)| downwards. add *nihēb |nyhyp | N ~] fear, terror. for nīšān read nišān...
161:a- P- | M ?-] privative prefix, un-, Jess, а D] then (generally with a suffixed pronoun, e.g. 8-š). ab [M YA < А my';?p | M >b, N ~] water. B Soy 277 abad рр? | M Ра, N ~] populous, thriving, prosperous. ~ih: prosperity. ābādān [f*?t?*n' | N ~] thriving, prosperous, cultivated. ~ih: prosperity, cultivation. abādixšā(y) 'P?th? (d), v. pādixšā(y)] without authority, powerless. ~ih: powerlessness; anarchy. abādyāwand Pf?tyd”wnd | J ?b’dywn<d>] powerless, weak. ~ih: powerlessness, weakness. арар [LW TE < A lwt-h | M?Pg, N (a)bā] with. ~ih Dë kuk) company, assistance. abāgēnīdan, abāģēn- [^P'kyn-ytn!] accompany. a-bahr РРА] portionless, deprived. abām Pf?m | P ?bmyh, N (a)wàm] loan, debt. Abàn PPn! | M'0x, N ~] cal. 8th month; roth day. aband (nd, v. рапа | M ?bnd] erring. “АҺ: error. 'abar [ODM < А дат; bl | M "be, N bar] up; on, over. ~ āmadan: rise (sun). ~ āxistan: rise up. ~ āxrāmīdan: step up. — burdan : undertake. ~ madan: cope with, comprehend. ~ nigeridan: consider. ~ nihumbidan: conceal. ~ niSastan: sit, be enthroned. ~ nišāstan: seat, install. ~ rasidan: come to, upon. ~ rasidan б: attain. tabar Dél higher, superior. ~ag [-g | MP brg] superior. ~agan(ag) [-k’n(k)'] superior. --dar [-t, Zenit | M ?brdr] higher. ~dom [-twm | M ?brdwm] highest. —domih [-twmyh] superiority. abargar [5/21 god, divinity. abarig(àn) ['Bblyk( ny] = abarag. abarig DPryk! | M ?Pryg, J ?Pry] other.
166:~ih: wonder. àb-dàn [^5d?n!] water-holder. abdast ['5dst!] hand-guard. abdom Pfdwm | М ?bdwm] last, final(ly). ~ih: finality, end. abd-sahist [pdshst'] wonderful. abē- [5»(y)- | M ?by-, N bé] without, Jess. ~-bar [-5/] fruitless. ---bé$ [-bys] unharmed. ~-bim [-bym] fearless. ~-bimih: fearlessness. e--boy [-bwd] senseless. ---bēyih : senselessness. —-büd(ih) [-bwt', -bwtyh] deficiency. «=čim [-cym] without reason, cause. abēdān рругп!] of use, wanted. abé-|-guman [-gwmn!] without doubt, certain. —-$umiünih : certainty. ~-mizag [-m(y)ck!] tasteless. ~e must [-mwst'] uncomplaining, content. ~-niyaz [-пуа?с] free from want. ~=-68 [ws] M *by?wš, N béhóf] senseless, unconscious. -~-6Sih : senselessness, unconsciousness. abér [yl] very, much. abē-rāh Payis] e erring. abesar [fysl | M ?bysr, N afsar] crown. abesīhēnīdan, abesihén- [Ashyn-ytn', v. abesihidan] destroy. išn(īh): destruction. abesihidan, abesih- Pžs(y)%-ytn! | M? bysyh-] perish, be destroyed. —išn(ih): destruction, ruin. abespardan Pžļsp?/tn!) = abespurdan. abespurdan, abespār- [’fspwltn', ?psp'l- | M ?byspwrd, ?byspr-, N sipurdan, sipàr-] commit, entrust, consign. ubestag [5(y)s? k!] Avesta, the Mazdean scriptures, abestām [ēst m] = abestān. abestàn [°25/°п!] refuge, support, trust. ābestan Dóystn! | P ?bystn, N abtstan] = ābustan, abé-süd [yý swt'] profitless. “Аһ: profitlessness. a-bëš Буў] harmless; unharmed, invulnerable. ~ih: harmlessness; invulnerability. abē-|-wināh [-cwz?^s | M?bywr? 1] innocent. ~-wizend [-wznd] harmless, invulnerable, safe. abézag Pfyck! | M ?bycg, (N *oëza)] pure, holy. ~th: purity, holiness, abēzār Pye’, ?Буе?1 | N bézdr] free.
175:-üg [> | M Ze, N -a] suffix forming agent nouns from present stems. a-gàh [?g's] without rank. āgāh [?k’s | M ?g(h), N <] aware, knowing. ~ih: knowledge. ügahénidan, абваһёп- [A?^syn-ytn!] inform. ügandan, Agan- [’kn-dn' | P ?gnd, N ~] fill, stuff. a-ganj [Аис !] penniless. agar (HT, for А hn | Mgr, N ~] if. agar DEI | М °g°r-] inactive, powerless, имко ~ih : inactivity, impotence. agarénidan, agarén- [?/?/уп-уїп!] render powerless. agarihistan, agarih- [?*4?/y%-stn! | M ?g’ryyh-] become powerless. ag-dén [k-, ?gdyn!] of evil religion, infidel. ~th: heterodoxy, non-Mazdean religion. абепёп [’k(y)nyn' | M (*)*g(y)nyn] together.
186:~ih: heresy. āhēg Phwk' | M >ле, N ahd] fault, blemish. ahógénidan, áhógén- ["nokyn-ytn!] defile. a-homānāģ [’hwm’r’k'] unlike. ahēš [nof] deathless, immortal.
196:~ih: disbelief. an-āštīh [?n’styh] discord, enmity; disquiet, unrest. ānay-, v. ānīdan. an-ayād [?7’byd’t'] forgotten. an-āzarm [cim] without respect, dishonoured.
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
220:aswür 13 āwēnidan
221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āškārāg (34 1Q)k! | M sq?rg, N āškārā] obvious, evident. ~ih: revelation, confession. aškaragënidan [$k*Pkyn-ytn!] reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N šunawā] hearing. —ih: (sense of) hearing. āšnūdan, āšnaw- [OSMEN-tn! < А « ўт; топі | M? fnwdn, ?fnw-, N funüdan, funaw-] hear, understand. ~išn: hearing. або [šwk! = Av. ašawa] righteous. āšūb [>р | P swb, N ~] disturbance, turmoil. Aštād [s?t! | Md, N ~] the goddess Rectitude; cal. 26th day. aštag [štk'] messenger. ~th: mission. aštar РД whip. āštīh Pštyh | M 7st, N āštī] peace. Ašwahišt Piwhst'] = Ardwahišt. āšyān(ag) ['syd?n(k) | (M ?hy*ng), N ašyana] nest, lair. ātaxš Pths = Av. ātarš | N ātaš] fire. āwādaģ Pwb'tk! | J ?zo?d] generation. āwahan [wb’hn'] fortified place, stronghold. амат ['wbm | M ?w^m] time, season. -āwand [ла | M 2w(y)nd] suffix forming adjectives of quality. awar [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v. āwurdan. a-wardàg ['wit?k&!] undeviating. a-wardisnig [?wltsnyk'] immutable. Аһ: immutability. āwarišn [zoblfn! | M *wryšn) abode, home. a-warzid [Pwicyt'] untilled. *Aiwas-, v. tāwištan. ама [Pc | N ~] voice, sound. a-wazisnig ['wcfnyk!] immobile. āwēnīdan, āwēn- ['wyn-ytn! | (P ?bzoyn-)] admonish, blame. ~i$n: blame, reproach.
=== KNT leaf 208 (p.193) ===
3f, 57; XPa 20; XPc 14; XPf 48, alva}m-c* ($521) DB 5.9. Ка&-сїу nsm. DB 149, 53; DSe 37. @& ciy asn. DB 1.58. paruvam-ciy DB 1.63, 67, 69. yaciy (q.v.) DNb 35, 36, 57. haw-cty DPe 23f. hakaram-ciy DNb 34f. [haca-cily DSf 23: vakna-|cily XPg 7f, less likely than vaknalptly, see under apiy. |
Citcizri- sb. ‘Cincikhri’, father of Martiya (§163.V): Elam. st-in-sa-ak-ri-1§, Akk. #-in-Sa- ah-ri-i& Cicizrais gsm. (§179.1V) DB 2.9.
сій adv. ‘so long’, correlative with уйій ‘un- til’: from ci- + suffix seen in Gk. ёте-та ‘then’ (8191.11; wrongly König, RuID 72, and Sen 40). DB 248, 63.
cica- sb. ‘seed, lineage’: Av. &6ra-, NPers. &hr ‘origin’ ($78, $148.IIT). In Ariyaciqa-, Ciça- іахта-.
Ciga"lazma- sb. ‘Cicantakhma’, а Sagartian
OLD PERSIAN
rebel: Elam. şi-iš-ša-an-tak-ma, Akk. -it-ra-an. — | lah-ma, Gk. Tpravraixuns. From ciga-(§9.n1) + | lazma- ‘brave’ ($9.11): ‘Brave-by-Lineage’ (§160,- Ie); the -zm- is Median ($163.II; Jacobsohn, KZ 54.261; Bv. BSLP 31.2.79). For the nasal end-
ing the prior element, see $159.n1. Cicatazma
пет. DB 2.79; 4.20; DBg 1f. Ciçatarmam asm, DB 2.871. Cicalaxmà ism. DB 2.86.
сіла] emphasizing adv. after neg., ‘at all’: , :
Av. cină ‘also, likewise’; perhaps isn. of ci-, cf.. 4 JAOS 58.116-7, 324, and Harl, KZ 63.2 (not ! eità], with Sen 134). DSe 36.
ciyăkara- (§53) adj. ‘how great’; nt. аз sb., ‘how great a thing’: *ciya(n)t-, cf. Skt. kiyat nsn. ‘how much, how many’, + kara- to root kar- ‘make’ ($160.19; Bthl. AiW 597; hardly to kara- ‘time’, cf. hakaram, as taken by MB Gr $293, Hz. ApI 101-3). ciyakaram nsn. (§259) DNa 39; ciyükaram DNb 50; ciyakaram-ca-maiy (written — : -"m*m*eur; $41, $51, $132, $138.I; Lg. 15.178, — | against Hz. ApI 240) DNb 51, 51f. 1
CiSpi- (so Schaeder, SbPAW 1931.641.n4; i Catišpi- acc. to Justi, INB 152, on the evidence of certain spellings in Greek) sb. "Teispes', King of Elam about 610 в.с., ancestor of Cyrus and Darius: Elam. $1-13-рї-1$, АКК. $-4f-pi-i$, Gk. Téergs (S117, 8124.3, §164.V). Стр nsm. (824, §179.IV) DB 1.5°; DBa 8. Cišpãiš gsm. (824, 8179.IV) DB 1.5f; Cišpaiš ($24, S170.IV) AmH 3; DBa 8.
ja*tar- sb. ‘smiter, slayer’: Av. Jantar-, Skt. hantdr-; pIE *g*hen-tor-, agent noun to OP root jan- ($154.11). Jat пзш. ($186.1) DB 4.58, 78.
jad- vb. ‘pray, ask’, with acc. of person and асс. of thing: Av. Jad- (gad-, Bthl. AIW 487), pres. faiya- (§214), Gk. aor. inf. mid. Өёосасдо:, pIE *g*hedh-. — jadiyümiy lst sg. ($226.1) DPd 21; DNa 54; XPh 59; XSc 4.
jan- vb. ‘strike; smite, defeat (enemy ш. battle); mould (brick)’: Av. Jan- (gan-, Bthl. AW
490), Skt. han-, Gk. бере ‘strikes’, dóvos ‘murder’, - |
Lt. dé-fendit ‘wards off’, pIE *g*hen- ($101, $110, 6208); see also jatar-.
јачу (Skt. hánii; 3208, $228.1) DSe 36, 40. ajanam Ist sg. imf. ($110, $122, $208) DB 1.89, 95; 2.69; 4.61; 5.25; XPh 34. аја" imf. (8101, $208) DB 2.26, 36, 41, 46, 55, 61, 87, 98°; 3.7, 18, 39,46,63, 68;.88; 6011) 05634. | ajaniya imf. pass.
LEXICON
(8220) DSf 29, jadiy (Skt. jaht; $101, $122, 8208, 6237.1) 2d sg. шу. DB 2331, 51; 3.15. ја 2d pl. imv. ($208, 5231) DB 2.21, 84; 3.58, 86.
ava- + jan- and ava- + à + jan- ‘smite down, slay’ (apparently ava- in avajata, ара-й- in avàjan- iyà, others ambiguous; cf. §206c, JAOS 62.274): avàjanam 1st sg. imf. ($226.IT) DB 1.57, 59, 73, 83; 2.5; 481; 5.13, 27°. арфа" imf, ($228.IT) DB 1.31 bis; 3.75.  avàjana" За pl. imf. ($208, $232. П) DB 2.13. avájantyü opt. (§206c, $2281, §228.1I) DB 1.51, 52 (858, JAOS 62.274; hardly with Foy, KZ 35.34). avajata nsm. past pte. pass. (8122, §242.1) DB 1.32 (error for avdjata, ace. to Gray AJP 21.13, Bthl. AW 491).
pali- + jan- ‘fight against’: patzyajatà imf. mid. ($140.П1, $208, $235.II) РМа 47.
fra- + jan- ‘cut off’: frájanam lst sg. imf. (§226.11) DB 2.74, 89.
vi- + jan- ‘shatter’: vijaná"tiy 3d pl. subj. ($208, $222.111, §232.1) A’Sa 5°, A?Ha 7° (conj. Kent).
Jav- vb. ‘press forward’:
=== KNT nay ===
5600:nay- vb. ‘lead’: Av. nayeitt, Skt. náyati. Conj., §213. anaya imf. DB 2.88; 3.88°; 5.12. [ajnaya" 3d pl. imf. ($232.11) DB 5.28. anayatá imf. mid. as pass. ($235.П) DB 1.82, 2.73; 5.26". Some or all of these are possibly ànay-, from à + nay-. | fra- + nay- ‘lead forth, provide’: fránayam Ist sg. imf. ($226.11) DB 1.87.
5693:fra- prefix ‘before, forth’ (as prep., not found in OP): Av. fra, Skt. pra, Gk. тро, Lt. prü-fessus, Gt. fra-, pIE *pro ($33, $01, $75.II, $106, $132.3). Found with verbs а1$-, jan-, nay-, var-, má-, sá-, haj-; in nouns framdtar-, framānä-, Fravarti-; in phrasal adv. fraharavam; with suffixes and exten- sions, in fratama-, fratara-, fratara-, fravata, fraxa-.
```


### [2026-09-07T18:20:37.213Z] TOOL RESULT

```
=== SYN leaf 736 (p.712) ===
r *twal-) : rbAn, THAos ‘swelling, hump, knob’, fr. extension of *teu- in words for ‘swell’, Walde-P. 1.709. Boisacq 850. : 2, Tat, quatere, quassare : Ir. caithim a Walde-P. 1.511. Ernout-M. ee Hence fr. epds. It. scuotere (fr. -culere), Fy. secouer, OF r. secourre, Sp. Ss pee , Rum. scutura (fr. dre, fr. ex-
S000, 8413 r. ex-culere). REW 2998, 3. , ih Ds crothim, NIr. crothaim, prob. :
« hresti, kratyti ‘shake’ 5), ON lytt ‘s ake’, etc. (below, 1 UN hreda ‘f hten’ Stok nighten’. Walde-P. 1.484. 899. Falk.
WV - ~ a -Torp 928.
: siglo, etym 2
t. heja, hejal
hacker, this a MBr. hegaff, fr. Fr. emry 159, ne Du. hotsen ‘shake’. 264, 'W 4208. Franck-v. W.
Digitized by Arya Samaj Foundation Chennai and eGangotri
N, TRANSPORTATION, NAVIGATION 675
10.26 SHAKE (vb. trans.)
add”, Goth. -hrisjan, gawigan, Lith. kralyli, purlyli elo yhoo wagjan Lett. purindat, kratit qo ON _hrista, skaka ChSl.  tresti its gt sre Dan. ryste SCr.  trestt quatere quas Sw.  skaka Boh. trdsti scualere (e30) hrysian, sceacan Pol. irzqsé secouer ME schake, rese Russ.  trjast’ sacudtr NE __ shake Skt. dha sculura Du. schudden Ay. crothim OHG - scut(t)an, sculilon crothatm MHG__ schiilen, schiiteln siglo NHG _ schiitteln a hej F cy 1, Gol gew, with sb. cevouds fr. 4, Goth. af-hrisjan (‘arorwaocey’), : - ‘he aroused’, tvesa- us-hrisjan (“xrwaocew’) OE hrysian,
ME rese, ON hrista (dental pres.), Dan. ryste : Skt. krid- ‘play, frolic’ (*kriz-d-), IE *(s)krei-s-, extension of *(s)ker- ‘turn, bend’, ef. Lith. kreipti (10.12). Walde- P. 2.572. Falk-Torp 904, 928. Feist 7.
Goth. gawigan, wagjan (render ca- hebw), OE wecgan, wegan, see under ‘move,’ 10.11.
ON, Sw. skaka, Norw. skage, OE scea- can, scacan, ME schake, NE shake : Skt. khaj- ‘stir about’, IE *(s)keg- beside *(s)kek-, in ChSl. skokt ‘a leap, bound’,
W. ysgogi ‘move’ (10.11), Br. diskogella —
‘secouer pour arracher’. Walde-P. 2.557. Falk-Torp 979.
Du. schudden, OHG scut(/)an, MHG schiit(t)en (NHG schiitten), with iter. forms OHG scutilon, MUG schiit(t)eln, NHG._ schiitteln (also NHG schiittern ‘tremble, shiver’ and schaudern ‘shud- der’, NE shudder) : Lith. kutéti ‘rouse’, Lett. kutet ‘tickle’, ON hossa ‘toss’ (a child on the knees). Walde-P. 2.601 f. Weigand-H. 2.806. Franck-v. W. 602 f.
5. Lith. kresti, Lett. krest, with the more common iter. kratyti, krattt, see above, 3.
Lith. purtyti, Lett. purét, purinat : Lith. dial. 7-purti, Russ. pyrit’ ‘ruffle (feathers) up’, perh. also Boh. pureli, pouriti se ‘blow oneself up’, SCr. puritz ‘blow’, etc., these as orig. ‘kindle’ : Boh.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Di
```


## [2026-09-07T18:20:46.040Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nfor f,pat in [('KNT.txt','nay- vb'),('SYN.txt','nayati')]:\n    txt=open(f,encoding='utf-8',errors='replace').read()\n    pages=txt.split('\\f')\n    for i,p in enumerate(pages):\n        if pat in p:\n            print(f,'leaf(0based)',i,'| head:',p[:120].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T18:20:47.345Z] TOOL RESULT

```
KNT.txt leaf(0based) 216 | head: e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) DB 1.15, DPe 14, DSe 28°; drayahiyà ($27
SYN.txt leaf(0based) 775 | head: SI. vest, etc. (the Balto-Slavic group), above, 1. 7. Skt. ni- ni- (nayati, nita-), Av., OPers. ni- (Av. 3sg. pres. naye
```


## [2026-09-07T18:20:47.544Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN LEAD ===\"; grep -n \"10\\.64\\|LEAD (vb\" SYN.txt | head\necho \"=== BRT nay ===\"; grep -n \"nay-\\|nayeiti\\|1036\\|1037\" BRT.txt | grep -i \"nay\" | head -20"
}
```


### [2026-09-07T18:20:47.649Z] TOOL RESULT

```
=== SYN LEAD ===
16624:M wb.) 10.54 OverTAKE oll pen Gb.) 10.55 Arrive, REACH 10.12 ae AROUND 10.56 APPRoAcH (vb.) 40.18 Wino, WRAP (vb.) 10.57 ENTER 10.14 Ron (7b.) 10.61 Carry (BEaR) 10,15 rairb.) 10.62 Brine re Russe, LIFT 10.63 SEND 10. vb.) 10.64 Leap (vb.) Ce se Tigui 10.65 D 1024 Dror (sb., of Liquid) : RIVE (vb. trans.) 1025 THROW (vb.) 10.66 Rive (vb.) 1098 SHAKE (vb. trans.) 10.67 Pusu, Sov (vb.) 1031 Bor (vb. intr.) 10.71 Roan 10.33 Smvx (vb.) 10.73 Street 10.34 Fuoat (vb.) 10.74 Brmwce 10.35 Sw (vb.) 10.75 Carrtace, Wacon, Cart 1036 Satz (vb.) 10.76 WHEEL 1037 Fuy (vb.) 10.77 AXLE 10.38 Brow (vb. intr.) 10.78 Yoxs 1041 Creer, CRAWL 10.81 Sup 1042 Ste, Sur (vb.) 10.82 Sartor 1043 Jump, Leap (vb.) 1044 Dancz (vb.) ee meee 1045 Watx (vb.) i 10.46 Run (vb.) 10.85 Oar 1047 Go 10.852 Row (vb.) 1048 Come 10.86 RuppER 1049 Go Away, Depart 10.87 Masr a Tze 10.88 Sar (sb.) 10.53 peso 10.89 AncHoR
16893:Boh. zvednouti epd. of root ved- in vésit ‘lead, guide’ (10.64).
17830:Lat. portare (> It. portare, Fr. porter, Rum. purta) : Skt. pr- ‘lead across, rescue’, para- ‘beyond, far’, Grk. zelpw ‘pierce’, repdw ‘pass across’, Goth., OHG, OE faran ‘go, travel’ (10.47), OE ferian ‘carry’ (Dan. fre, Sw. fora ‘carry’ and ‘lead’, 10.64), IE *per-. Walde-P. 2.39. Ernout-M. 793 f.
17834:Rum. duce, fr. Lat. dicere ‘lead? (10.64).
17866:ON fera (Dan. fére, Sw. fora ‘carry’ and ‘lead’, NHG fihren ‘lead’, 10.64), caus. to ON fara, Goth. faran ‘go, travel’ (10.47).
17901:» tye 0 a _ Ee. 9.504 f. Bric hi Aah ! ; this sense dub. RY 4 am in presyati and caus. 1. . 10.64 LEAD (vb.) Goth. tiuhan Lith. — vestz rk. 1m trreouat ON. leida Lett. vest yo &nd Dan. __lede, fére ChSl.  vesti_ Int, _dilcere an Sw. _ leda, fora SCr.  voditi yt, menaré, © 4 OE ladan Boh.  vésti Bau ME _lede Pol. prowadzié
17956:hicle, NE always uses drive (so Grk. &habvw, e.g. Hom. Il. 23.334, and Lat. agere), but the majority of other modern languages use rather a verb for ‘lead’ (10.64) or ‘guide’, e.g. NG dényd, St. guidare, condurre, Fr. conduire, Sp. gutar, conducir, NHG lenken (but vieh treiben), Russ. pravit’ (‘rule, direct’, etc. : pravy) Tight’).
17977:Rum. mina ‘drive’ (animals), fr. late Lat. mindre id., see Fr. mener ‘lead’, etc., 10.64.
24936:prob. fr. pieza ‘piece’ (= iéce, etc.), perh. through k open’, ef. It. spezzare 1 REW 6450. 3. Ir. doinscanna 3sg. (*to-ind-scann-), andinlinscanna 38g. (*ind-to-ind-scann-), ef, frarscannat ( fo-scann-) ‘they toss it’, NIr. foscnaim ‘toss, Winnow, purge, deanse’, etym. dub. Walde-P. 2.564. Pedersen 2.618. Ir. sb. tossach, NIr. tosach, fr. the shorter form Ir. tuws, NIr. tus, lit. ‘a leading forth’ : W. tywys ‘lead’ (10.64). Hence NIr. tosnuighim (also tosuigim, ete.), Pedersen 1.308. W. dechreu, Br. deraoui, with sbs. W. dechreuad, Br. derou, etym. dub. Peder- sen 1.484 (as perh. orig. ‘draw blood’ = ‘begin battle’ : Lat. cruor, etc.). 4. Goth. duginnan; OE onginnan, winnan, rarely beginnan, ME aginne, ie (and with dropping of prefix ga ea begin, with sbs. OE a i a : peemuarainge, ~ynge, NE nen > Dan Be poe SND Ui ths, bepynd ; egynde, Sw. begynna, with Man, ingin “ se, begynnelse), OHG bigin- ths, Dy ae MHG, NHG beginnen, MaG = : G begin, OHG anagin, tig, rit etym. dub.  Walde-P. Goth, ae 58. Feist 128. Mastodeing ¢ ee dustodjan, with sb. USE to : rd S. of -stodjan (ON steda tlandan ( eo: establish’), caus. of 44, ‘Pret. st05) ‘stand’, etc. Feist
30308:Grk. #yéouar, orig. and in Hom. only ‘lead, conduct’ (10.64), henc2 also ‘hold, consider, think’ (cf. Lat. dicere ‘lead’ and ‘reckon, consider’).
=== BRT nay ===
3186:Pii. :  anapasmiin'\  [itx  Y.  g):  ana/VKäyistii); erl,;  ka  »."att  mal  "wenn  gegessen,  ials  wieder da";  Sü.:  atiavasääah.  —  ')  NA.  'jay'  mit rt4!  s.  aber  K  s  und  Yt.  75.  16.  —  >)  Vgl. lu  satil-.  —  Sl  Vgl.  ai.  apahänay-  f.
3308:6i  adukanay-
3315:•  p.  adu-kanay-  f.,  G.  mit  mäk-  m.  Name eines  Monats*':  °naism3hyil{,?A^  Bh.2.i2.
5007:•  j.  ava-kanay-  m.  'Graben,  fossa*:  ys aitfm  ai'aAan^m  avakatäa  yeiihä  v5  aisS 'nis  anhat  V.  75.39  ■>.
5819:•  j,  astö.vi'Sätav-  :  °\5tu-  m.  Name  eines Dafva'h  fräksrssts  "hstus  "zirijä  (sd.) ajiairi.ayö  Aog.57;  —  °oütu^  dim  handa- yeiti  vayS  dim  bastsm  nayeiti  V.ß.S;  — 'oUlus  p?sanatti  V.4.^^.
5883:•  j.  aspö-stäna-  m.,  'stänay-  m.  T/erde-
8820:•  j.  uströ.stlna-  m.,  °stinay-  m.  'Kamel- sialV:  yiziia  ag^a  gaowa  "naisva  frajasiit V.  /j5, 23  i  —yö  aitim  °n.im  uzdasta ''  yetihii vö  ag\i>  °ni.r  auhat  "wer  diesen  Kamel- stalt  gebaut  hat,  welcher  (fem.)  von  euch" dieser  Kamelstall  gehört"  V. /5.24.
9105:.J7-  S53.  3^-  259.  wo  weliere  IJtL a  j.  uätrö.stäna-  m.,  'stänay-  m.  'Kaniel- stall':  yesi'a  aSia  ga'uva  'naSii'a  /rajasäl V-  '5-^3i — yö  iiitjm  °n.>m  uzdasta'^ yi-i'jhii v5  a?\i>  'nis  auhat  "wer  diesen  Kamel- stall  gebaut  hat,  wciclier  (fem.)  von  euch" dieser  Kamelstall  gehört"  V.  75.24.
9487:•  p.  kapiäakänay-f,'i  Name  einer  Festung  er  mit  der  Strafe,."  V,7.38.         3)  para in  Arachosien'l ;  'nis  nUmä"  didä  Bh-S-g.  aisqm     irisintqm     raisS    cikatn'^    daaZs.-
9555:A^^-  ?■  ^w  ^  T'  ^'  ^°i, '"/"'"'  ""■  J'"^^"''' '  •  J-  kui^sänay-  m.  EN.  eines  von  Haoma
9581:Et.?    \^.  i>r»5nay--l    -    PÜ.    (lu   Yt.  //):    vff^geri  :   altlyS k' yaifgam  karapH  usixsca
9583:*iarsyüiiAä.  —    S.  lU  kirisänay-.    —    ')  J  10  ,       Vgl.  ai.  kam    Praen.    (mit    vorausgeh.    Dat.),
9869:•  j-^gac'^-Stäna-m.,  -stanay-  m.,  'Rin- derstall': yaua  ai^a  galwa  -naisva /ra- jasiit  V.  ;5.  29; — yö  altim  -tarn  uzdasta yerihh  v3  alsS  °nis  anhai  V.  /j.  30  ".
11265:•  j.  cäxsnay-')  m.  EN.  eines  Gläubigen: °nöt^''>  asaonS  Yt.  13. 114"*.
11511:KompE.  —  Superl.  lum  Praes.  5  des  V.  xan-. —  ai,  TgL  jdgAnay-  und  hänijlha-  Adj.  — Pü. :  ialärhim,  iaiär.
11556:KompE. ■  j.  Janay-,  g.  J^nay-  'Weib,  Frau':  t^ä i  hati^yä  (sd.)  «ürj  a>S  JjtiayJ  (VF.)  Y. 53-  6 ;  —  da^va . .  vasnfmram  *apa.kariay.>n
11559:ai.  jänay-  t,  np.  iow.  —  VgU  Jqnay-.  —  mp. in«,  (in  A):JiA;  s.  noch  No.  i.  —  0  Pt4 usw. ;  NA.  janyaos  (woiu  Bthl.  AF.  3.  64). Das^  erklärt  sich  wie  in  al.  säkhyau.  Pu.: /fl  io»im,  — ')  S.  Vir.  NA./ancfl,  ohne  Epen- these 1
11627:•  g.  JSnay-  f.:  s.  unter  Janay-.
11644:•  j.  Janay-  f  'Weib'  in  verächtlichem Sinn'':  %risum  aSaZsqm  axtinqm  'nayd dnnjaili  V.  7.  59  Gl.  (?).
11645:got.  qens.  —  Vgl.  janay-,  —  Pü. :  srisülak  ösän cnikih  }eh  {i.  janay-  a)  dranjenit.  —  >)  So  Dach pa.     Ganz  unRichcc.
```


## [2026-09-07T18:21:01.117Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT leaf 216 (find page numerals) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==216' KNT.txt | grep -o \"1[0-9][0-9]\" | head -20\necho \"--- first 300 chars\"; awk 'BEGIN{RS=\"\\f\"} NR==216' KNT.txt | head -c 300\necho; echo \"=== KNT leaves 210-220 headwords ===\"; python3 - <<'EOF'\ntxt=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(205,222):\n    import re\n    nums=re.findall(r'\\b(1[5-9][0-9]|2[0-1][0-9])\\b', txt[i][:400])\n    print(i, nums[:5], txt[i][:80].replace('\\n',' '))\nEOF"
}
```


## [2026-09-07T18:21:02.401Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT nay- headword ===\"; grep -n \"nay-\" BRT.txt | grep -i \"führ\\|leiten\\|1036\\|nayeiti\" | head -20\necho \"=== BRT search 'j. nay' ===\"; grep -n \"j\\.  *nay\\|j\\. nay\" BRT.txt | head"
}
```


### [2026-09-07T18:21:02.514Z] TOOL RESULT

```
=== KNT leaf 216 (find page numerals) ===
191
111
136
135
191
111
101
103
113
128
132
103
122
128
132
122
128
150
156
190
--- first 300 chars
rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far and wide’ (GAv. düiré, LAv. duire, Skt. d'ré; $65, 6191.111) DNa 44. duraty apiy DSe 11, DZe 6, DE 18, XPa 9, XPb 18, XPe 8, XPd 13, XPf 13, XPh 10, XE 18, XV 14, A'Pa 14f°, A’He 17. düraiapiyy DNa 12, dürayapiy DNa 46 ($18, $13
=== KNT leaves 210-220 headwords ===
205 []  sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 5110, $122) DB 1.52
206 [] n, fall down’: [avagmat]a nsf. past pte. ($244) DSe 46f (conj. of Kent, cf. JAOS
207 ['163'] 3f, 57; XPa 20; XPc 14; XPf 48, alva}m-c* ($521) DB 5.9. Ка&-сїу nsm. DB 149, 53
208 ['152', '215']  Skt. jū- ‘press for- ward, impel quickly, excite, promote’, pres. jdvate ‘haste
209 ['153'] it (§76.V, 5148.1). Cf. Gray, AJP 58.67; Hz. Klio 8.51, AMI 2.77; Hinz, ZDMG 95.
210 [] 1) XPh 23. tyam asi. DB 4.70f; DPd 7. tya as asf. (856.V) AmH 5; AsH 13°. tyà np
211 ['155', '188']  word of uncertain meaning, Sb 3. Sanuvaniya- sb. ‘bowman’: deriv. ($144.IV) of 
212 ['209', '218'] fnu, Lt. јеси ‘made’, NEng. do, deed, pIE *dhe-. See also wadd-, data-,ddna-. ай
213 ['162'] 5-6). Dérayava'u- sb. ‘Darius’ (I, son of Hystaspes, king 522-486 ».c.; IT, son 
214 ['153', '166'] Hz. Ap! 136-8) nsn. as sb. ‘handiwork’, DSe 42. Daha- adj. ‘Dahian’; pl., a prov
215 [] rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far and wide’ (GAv. düiré
216 ['207', '191'] e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) 
217 [] n üv-nara- (§142). nàv- sb. ‘ship’: Skt. ndus, Gk. vais, Lt. nav-is, pIE *ndv- (
218 ['166'] with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing’ + "wüdá- ‘abode’ (
219 ['167', '178'] ‘I pierce (as with a spit)’, Gt. faran ‘to travel’. рамо[т- іаїу| nsn. past pte.
220 [] tem (530, $148.I, 6154.1), ef. Av. posana- ‘battle’, Skt. pfiana- ‘battle, army’
221 ['154', '186', '186', '166'] r-, Gk. rarnp, Lt. pater, Gt. fadar, pIE *poler- (863.11, 875.1, 576.1, $154.II)
```


### [2026-09-07T18:21:02.572Z] TOOL RESULT

```
=== BRT nay- headword ===
=== BRT search 'j. nay' ===
```


## [2026-09-07T18:21:32.506Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('total leaves',len(txt))\nfor i in (216,217):\n    print('=== leaf',i)\n    print(txt[i][:1500])\nEOF"
}
```


### [2026-09-07T18:21:33.825Z] TOOL RESULT

```
total leaves 232
=== leaf 216
e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) DB 1.15, DPe 14, DSe 28°; drayahiyà ($27) XPh 23.
naiy adv. ‘not’: Av. 207, РЫ. në, Skt. ned; :
from pIE *ne, Skt. na, Lt. ne-scio ‘I don't know’, -+ Эа, asn. of pron. i-, Lt. id, OP id-am, ete. (869, 884, $191.1, $291.11, §292a). DB 1.32, 48, 49 ter, 52, 53, 71, 91°; 221, 24, 31, 51, 84; 3.15, 86; 4.44, 47 bis, 51, 55, 58, 63 bis, 63f, 64°, 65 bis; 5.16°, 31; DPd 11; DNb 7f, 12, 13, 21, 23, 36, 40; DSe 36, 40 bis, 43°; DS} 3; XV 22. nai-maiy (836) DB 4.64. nai-ma DNb 8, 10, 19. nai- pati-mà (8133) ОМ 20. nai-&im DB 4.49. naty- diš ($136) DB 4.73, 78.
naiba- adj. ‘beautiful, (religiously) good’, re- .
placing GAv. vahu- ‘good’, and opposite of duš- karta- (Hz. AMI 8.68, ApI 266-7): NPers. nē ‘brave, good’ ($11, §75.V, $148.11). пафа nsf. DPd 8. naibam nsn. XPa 13, 16; XPg 4; XV 20. naibam asn. DSe 32°; DSi 4^; DSp 2f°; XPh 43.
naucaina- adj. ‘of cedar’: NPers. nóZ, пдѓап ‘pine cone’; therefore naucaina- ‘pine-cone-shaped’ ($147.11), appropriate to the cedar (König, Burg- bau 53-4; Hz. AMI 3.58). naucaina nsm. DSf 30f. |
nab- vb. ‘perish’, causative (8123.2, $215) "in- jure; destroy’: Aw. )nas-) ӨЮ. naé-, Gk. vexus
7 ыйсы аЙ eet NUI ШЕЛ, АМАА а аз an ШО. Дені. Zr é
DD де 5... anes
LEXICON
‘corpse’, Lt. acc. nec-em ‘destruction’, nocet ‘harms’, pIE *nek- (887).
vi- + nab- caus. ‘injure, harm’: vindPayatiy (8215) DNb 17f. viyanatlaya imf. (§122, $1232, $215) DB 4.66. vinátayá"tiy За pl. subj. (8222.1
=== leaf 217
n üv-nara- (§142).
nàv- sb. ‘ship’: Skt. ndus, Gk. vais, Lt. nav-is, pIE *ndv- ($142). See also ndviyd-. [naval прі. (8183.1V) DZe 11 (supplied by Tm. Lex. 52).
navama- adj. ‘ninth’: Ау. паота-, Skt. navamá-, pAr. navama- remade from pIE neyeno- after pAr. dasama- ‘tenth’ ($14911, $204IV), ef. Lt. nénus.  navama пзш. DB 1.10; DBa 10f.
naviyd- fem. adj. as sb., ‘navigability’, i.e. ‘impossibility of fording the river on foot’: Av. nàvaya- ‘navigable’, Skt. navyd-, adj. to nàv- ‘ship’ (§144.V). Hardly collective, ‘collection of ships, flotilla’, and certainly not lsf. to nav-, ‘on ship- board’; ef. König, RulD 70-1, and esp. Kent, JAOS 62.269-71 (with lit.), 63.67. ^ nàviyà nsf. DB 1.86.
nàh- sb. ‘nose’: Av. nàh-, Skt. nds-, Lt. narés, NEng. nose, pIE *nds- (5110, $142).  náham asm. (81181, §185.1V) DB 2.74, 88f.
ni- prep. and verbal prefix ‘down’: Ау. ni, Skt. ni-, pIE *ni; in adv. nipadiy, and with verbs ar-, kan-, cay-, pa10-, yam-, std-, had-.
nij- verbal prefix ‘away’: sandhi form of pIE *nis- before voiced stops, generalized, cf. Av. niš-, Skt. niş- ($120); with verb ay- ‘go’.
nipadiy phrasal adv. and prep., ‘on the track of, close after’: prep. ni- + loc. padiy, to pad- ‘foot’ ($76.11, $136, $140, $191.1V). тарайту adv. DB 2.73; prep. with acc. DB 3.73.
nipisti- sb. ‘impression’: deriv. of ni- + paid- ($152.11).  [niplisftiya] Isf DB. 4.90 (conj. of Kent, JAOS 62.268).
194 OLD PERSIAN
niydka- sb. ‘grandfather’: Av. nyáka- ($146.- HI); ef. apaniyüka-. {nilyaka nom. DSI 13
```


## [2026-09-07T18:21:42.210Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT nayeiti ===\"; grep -n \"nayeiti\" BRT.txt | head -10\necho \"=== BRT 'füliren\\|führen' with nay ===\"; grep -n \"1036\\|1037\\|1038\" BRT.txt | head -8"
}
```


### [2026-09-07T18:21:42.266Z] TOOL RESULT

```
=== BRT nayeiti ===
5819:•  j,  astö.vi'Sätav-  :  °\5tu-  m.  Name  eines Dafva'h  fräksrssts  "hstus  "zirijä  (sd.) ajiairi.ayö  Aog.57;  —  °oütu^  dim  handa- yeiti  vayS  dim  bastsm  nayeiti  V.ß.S;  — 'oUlus  p?sanatti  V.4.^^.
18599:*astB.vj%Stus  dim  bandayäti  vayö  dim batUm  nayeiti  V.  5. 8 ;  —  sp3n>m  *naisyuti FrB.(?).  a)  mit  Angabe  des  wohin? durch  Akk. :  tsm  *vä  ahum  dngvantB  syao- %anaU  c^äii  dama  nalsat  (Konj.)^'  "zu solchem  Leben  (aber)  wird  euch,  ihr  Drug- genossen,  ob  eurer  Taten  das  eigne  Ich führen"  Y.j/.  20.
25752:PPA.,  tu  'urvinya-,  Praes.  13  a'l  einer  Basis ifrai'i  vgl.  ai.  vlinäli.  —  S.  auch  uniaid:  — ')  So  nach  Fi,  Jio  usw.;  NA.  hat  uruinaiBi, mit  geringwertigen  Hds.  —  >)  Fehlt  S  134- ai.  vHnaS  j  j.  'unnayeiti  —  lat.  'cHnat,  ai. AUnöt :  gr.  «Xi'ko)  (Bgm.  Grdr.  /.  981).
=== BRT 'füliren\|führen' with nay ===
18483:1036
18496:1037
18499:1038
```


## [2026-09-07T18:21:43.770Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB nitan ===\"; grep -n \"nītan\\|nitan\\|nay-\" NYB_vol2_glossary.txt | head -15\necho \"=== CHEUNG nay ===\"; grep -n \"^\\*nay\\|\\*nay-\\|NAY\" CHEUNG.txt | head -15"
}
```


### [2026-09-07T18:21:43.827Z] TOOL RESULT

```
=== NYB nitan ===
262:aeürénitan [>c*lynytn'] to make ineffec- tive: bé acdrénét (sc. your work) with the explanation akartārēh-ic 6 šmāh dahét he will create ineffectiveness for you, he will make your work inefficacious 45?. — Den. of a-cär, v. car. V.s.v. axtäyisneh.
311:*ähöyenitan, pt. = pret. pass. *ahdyénit ['hwkynyt'!] "to insist on (pat) 383. — Meaning approximately clear; reading hypothetical. I take it as the caus. *ayöden- of OP yaud- ‘to be in commo- tion’, Av. (1231 sq.) yaoz-, v.s.v. āyēz. This *äyöden- having developed into *ayoyén- io SW, the first -y- was dropped and -h- inserted to fill the hiatus, ac- cording to the cominon rule; -k- is only graphic, as often after a w to assure its reading as -0- — if -k- is not simply (by no means uncommon) the defective form of the old letter d (cf the Ps.): *hwdyn-. — Commonly the spelling *hwkynytn' stands
313:for ähökenitan ‘to defile, to soil, to stain’, den. of ähök, Paz. ähö, NP ahi ‘fault, defect, stain’, v. Zsprm ch. III, heading, Av. s.v. (345) ahita- and (346) ahiti-.
343:akahčh [’k’syh] information, message 32. 72. 4613. 594; — religious doctrine(s) and tradition(s) commonly accepted by the community (in contradistinetion to pat- tākēh, g. v.) 1095-28, 1117-15; ~ governing an inf.: the accepted doctrine (tradition) is that 111!!.2223. — Paz. NP ägähi; FrO VIII: vaččim [Av. (1321) vaédaya-]: ākāhēh. — V. kār-ākāhēh, visp-äkäheh. äkähönitan [~-ynytn'] to inform a p. of (hac) 1373-24, 4727,
349:akārēnītan [~-ynytn'] to incapacitate, to destroy 42%, — Paz. ägärined, Skr. v. vināšayati (SGV XII, 43).
497:apākēh [’p’kyh] 1. company; pat ~ together 5712, — 2. backward movement: pat ~ back 418; v. pat-apākēnītan. — 3. help, assistance 5919-20, 729-26 (opp. ha- mēstārēh). — V. lapāk and ?apäk. Paz. āvāgī. V. also apar-apākēh.
498:apäkenitan [—-ynytn'] to make a p., or a th., one's helper, or companion, or help: hakar vēnākēh apakéné [-yd] (if thou wilt make Clear Vision thy helper
500:Vision 595, with the gl. ku-t dančikeh bavet ‘that is: (if) knowledge is to be thine’. — Cf also pat-apäkenitan.
529:apa-sihčnišn [pshynsn'] destruction 8818-19, — Paz. substitutes awasīnašn < *apasindisn, v. below. — V. n. of apa-/apé-/sihénitan [’p/’py/shynytn'], to destroy, to annihilate: aš hamäk dam i tē bē apasihčnit hah [HWH'-’h] (cond.) 3121-321; .; ... nē apésthénitan (it is not for thee to =) thou shalt not be able to destroy 46° (MS ’pys-, v. below s. v. apasistan). — Paz. awasihinidan (Mx), Milr caus. of apa-sih- < *apa-sid-, v. ‘apasistan. Its pass. is apa-sihistan, pres. be nē  apasihiyet Ppshydyt', written so as to look like »pshhyt ] will not be consumed, emptied 9710, — The Milr pass. suff. pres. -ih(et, -ēnd, ete.) being always written -yhyt', -yhynd (etc.) in BP, the reading ’pshhyt' = *apasihihet must be rejected and the second h taken as the ligature of -yd- which occurs frequently (cf the spell- ing of miyän and niyäk). Thus the correct reading is apasihiyet. The original form of the pass. suff. was actually -2y(é, -end ete.), which developed into -2h(é etc.), -y- having been dropped and -h- inserted in the hiatus. The preservation of -iyé in apasihiyét is without doubt due to the distaste for having two suc- cessive syllables beginning with Z. — The
534:apa-sistan ['psstn'] apčsistan [’pysstn'] apa-sih- ['psh-, *psyh-] or apésih- ['py- syh-], to be destroyed, annihilated: bē apasihet will be annihilated, of Ahriman 644, of the wicked 103! (in both passages ’pshyt' in the printed editions); — bē apäyet apesihät (subju. 3d p. sg.) vis ? Pourusäsp the manor of P. (must be =) is evidently going to be destroyed 441°; nē be apesistan <i> vis 1 Pourušāsp rād not in order that the manor of P. might be destroyed 4421. My spellings apasihät, apasistan in Dk are to be corrected; the scribe of the Dk MS (now available in re- production) constantly writes all forms of this vb. and its derivatives ’pys-, keeping the two letters y and s distinct with a care not very common in Phl. writing (in 441° he wrote by a slight slip of pen ’p’s- instead of ’pys-). The form apēsīhāt 441° is directly confirmed by MPrs ’bysyh’d (S). — < apa- + Av. (1547) saéd-, pres. pass. "apa-sidyati > Milr *apa-siy-é > apa-sihet or apa-styy-ēt > apa-siyét > apasthét; Paz. awasihed, awasthend; M Prth ?bsyst ‘dried’, Ghilain 83. The form with -ē-: apésihét etc. goes back to *apa- hisidyatt with pres. reduplication (cf Av. ava-hisióyat which is, however, perf. opt.). The active pres. ‘to destroy’ was *apa- sind- > apa-sinn- (always spelt ’psyn-): apa-sinnčt, apa-sinnisn (Paz. awa-sinasn) ; from this are formed the secondary infini- tives apa-sinnitan (BdJ 15%, apésinni- tan (Mx 2771), apasinnistan (KnA 79). Bal sinday ‘to break’, Skr chid- (< Id.- = europ. aci pres. chinad-, chind- (Lat.
535:scindo). This act. is generally supplanted by the secondary caus. apasihčnitan from apa-sih-. — Note: — There is a synonymous vb. of uncertain origin which may have been influenced by the apa-sih- vbs.: Paz. awasdinidan SGV XI" = Phl *apa-sāyēnītan; "ps'dín! = apa-sāyišn Mx 15% (wanting in Cod. K); *pys’synytn' = apēsāhēnītan (the second -s- inverse spelling of h) DkM 175°. 351! (in the MS 13419. 27015), *pys'hšnyh = apesahiš- neh ibd. 180° (= MS 13816); to be de- rived from *apa-sü- *apa-säy- ‘to rub away’, cf s. v. apa-sütak ?
629:harm 5611.13, — V, rešenitan.
671:aržānīkēnītan [~-ynytn'] to consider a p. worthy, governing a subordinated clause without an introducing particle, 5318 in a very complicated passage 5317-21, which only seems possible to understand on the following suppositions: a) kū-t bahr hac man bé burt l. 19 is not a gloss, as I have marked it, but is governed by anak tč bavat l. 17 ‘it shall be unhappy for thee that thou hast bereft ...'; b) the clause kē ... aržānīkēnīt hom 1.17-19 is loosely attached to tē l.17; c) for MNW-t L<y> (MS very clearly MNWtl) read MNW kw) LY» = kē tē man, to man being the exact counterpart of LK ^NH = tč an (v. žan) 1. 19 and both signifying ‘thou and I’; d) YBLWN-m l. 18 and 20, and HWH'-m 1. 19, are the Ist. p. pl. coinciding with the Ist p. sg.; e) there is a wordplay between *š = dé ‘food’ l. 18 and ’$ = as (demonic) eye’ 1. 20 (as burtan 'to have a vision', v. 'aš; bahr ‘ministry’, v. this w.). Text: anàk tč bavat, marak, ke t(0» man fratom hac ax" i astomand andar Rdg u Notar hac bahr barišneh āš barom frac aržānīkēnīt hom, kū-t bakr hac man bē burt. niin-ip tē an pat apar-barišneh aš barom u et bavēt kū-t dušcašmiha al zänak nikēram i-t nest ‘unhappy shall it be for thee, little scoundrel, (that thou) — as thou and I first of all men in the material world between Räg and Notar have been found worthy of earning food by perfor- mance of ministry — that thou hast bereft me of the ministry. Now thou and I shall be enraptured in an ecstatic vision, and then it will happen that I shall see thee evil-minded in another house that is not thine’. The passage is the immediate continuation of the incident related in 537-15, Zsprm XII, 7 epitomizes 5316-21 as follows: dwlyslwb BR’ L zltwšt gwpt' "VK cygwnt pltwm HWH'-m b’hl wlweyk BR’ ’pknd HWH'-m ZK tw "NH KR?
715:āstēnītan [’stynytn'] to set up, to erect 398, 10912, Caus. of östätan (g.v.), both < *aipi-sta; the alternation ē- : ā- is pos- sibly due to shifting accent: *aivi-sté- > *ayyi-stā- > "ai-sta- > Estä-, but áivi-stá- > *dv-std- > *āstā- (divergent explana- tion Verbum 224). Cf MPrth pt. ’wystn’d ‘to put, to place’ (S), Ghilain 78 sq.
726:taš ['š] eye, of demonic beings 3118; ~ burtan to carry one’s eye (sight) far away = to have a vision of distant and hidden things 51-53, of the. pre-Zoro- astrian seers, v. also apar-barišneh and ef s. v. aržānīkēnītan.
=== CHEUNG nay ===
18279:*KHOTANESE: *nay- ‘to sound’, nayai ‘sound’ || (+ *pati-) LKh. panay- ‘to make a 
36997:*nay-, 276
```


## [2026-09-07T18:21:52.172Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG *NAY ===\"; grep -n \"NAY\\b\\|\\*nay- ‘to lead\\|nay- ‘to lead\" CHEUNG.txt | head\necho \"---\"; grep -n -i \"nītan\\|nidan\" CHEUNG.txt | head"
}
```


### [2026-09-07T18:21:52.221Z] TOOL RESULT

```
=== CHEUNG *NAY ===
18380:*OLD PERSIAN: nay- ‘to lead’ || (+ *fra-) ‘to lead forth, provide’ = Kent: 193 
---
2579:caus. BMP byszynytn /besazenidan 
3397:pasture’, NP Caränidan/Carän-, Meim. bem-tfernä/a-tfern-, Qohr. cerna/ cern-, Tr. 
3889:wyd’p’n’nytn /wiyabanidan/; Inch./Pass.: pres. IND. 35р. wypsyd, SUBJ. 3р1. MMP *wyps’nd 
7379:/pazzamand/; Inf.: caus. BMP pz’ptn, sec. caus. BMP pz’mynytn /pazzamenidan/ || (+ *fra-) Pret.: IND. 
8087:girià (+ va) ‘to return’, NP gardänidan/gardän- (sec. caus.), Jow. bam-gerna/a-gern-, 
9507:Partic.: perf. pass. BMP hwnyt /hunid/; Inf.: BMP hwnytn /hunidan/ || (+ *ni-) Caus.: pres. IND. 3sg. 
9729:ВМР ’wsm’lt /osmard/; Inf.: BMP ’wsm’lynytn /6smarénidan/ || (+ *а-) Pres.: IND. 3р1. BMP /amarend/ 
13396:r’yn-; Inf.: caus. BMP I’dynytn /rayénidan/; Pass.: pres. IND. 3pl. MMP r’yyhynd || (+ *api- ?) Partic.: 
13397:perf. pass. BMP pdl’stk /payrastag/, MMP “pyr’st; Inf.: caus. ВМР pyl’dynytn /payrayenidan/ || (+ *abi-) 
15541:*NWIR: (+ *4-) NP agandan/agin- ‘to fill, stuff’, (caus.) NP aganidan/agan- ‘to stuff,
```


## [2026-09-07T18:21:54.631Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD nidan main ===\"; grep -n \"nīdan\\|DB(Y)LWN\" PHD.txt | head\necho \"=== PHD leaf with nidan ===\"; python3 - <<'EOF'\ntxt=open('PHD.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(txt):\n    if 'nay-, v. nidan' in p or 'nīdan' in p:\n        print('leaf',i, p[:200].replace('\\n',' '))\nEOF\necho \"=== NYB nitan ===\"; grep -n \"nītan\\b\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-07T18:21:55.920Z] TOOL RESULT

```
=== PHD nidan main ===
128:delete mezidan ... suck. for ?mēzišn ... read ! meziin ... for mistan, *mēz- read... *mēz-.. mihoxt [mytwht' = Av. midaoxta-| falsehood. *mihr .. add ~ druxtan : break faith. add mizīdan, miz- [myc-ytn' | N mazidan] suck. for *moy-mard ... read mowmard ... mēy ... add M mwy. read nüxun [n^hwn' | P nxwn, N nàxun] (finger) nail. delete nāyīzag ... (read wezag). nek, ~th ... add benefit. nibastan ... delete SKBHWN-tn' < A Vškb; nibastan ... read M nb’st, P nb’y-. nibeg ... add M nbyg. nibištan ... |YKTYBWN-tn'... (not -stn'). nidan, nay- |DB(Y)LWN-tn' < A Ydbr |... nigün, ~sar |-s 1 | (P ngws’r)| downwards. add *nihēb |nyhyp | N ~] fear, terror. for nīšān read nišān...
161:a- P- | M ?-] privative prefix, un-, Jess, а D] then (generally with a suffixed pronoun, e.g. 8-š). ab [M YA < А my';?p | M >b, N ~] water. B Soy 277 abad рр? | M Ра, N ~] populous, thriving, prosperous. ~ih: prosperity. ābādān [f*?t?*n' | N ~] thriving, prosperous, cultivated. ~ih: prosperity, cultivation. abādixšā(y) 'P?th? (d), v. pādixšā(y)] without authority, powerless. ~ih: powerlessness; anarchy. abādyāwand Pf?tyd”wnd | J ?b’dywn<d>] powerless, weak. ~ih: powerlessness, weakness. арар [LW TE < A lwt-h | M?Pg, N (a)bā] with. ~ih Dë kuk) company, assistance. abāgēnīdan, abāģēn- [^P'kyn-ytn!] accompany. a-bahr РРА] portionless, deprived. abām Pf?m | P ?bmyh, N (a)wàm] loan, debt. Abàn PPn! | M'0x, N ~] cal. 8th month; roth day. aband (nd, v. рапа | M ?bnd] erring. “АҺ: error. 'abar [ODM < А дат; bl | M "be, N bar] up; on, over. ~ āmadan: rise (sun). ~ āxistan: rise up. ~ āxrāmīdan: step up. — burdan : undertake. ~ madan: cope with, comprehend. ~ nigeridan: consider. ~ nihumbidan: conceal. ~ niSastan: sit, be enthroned. ~ nišāstan: seat, install. ~ rasidan: come to, upon. ~ rasidan б: attain. tabar Dél higher, superior. ~ag [-g | MP brg] superior. ~agan(ag) [-k’n(k)'] superior. --dar [-t, Zenit | M ?brdr] higher. ~dom [-twm | M ?brdwm] highest. —domih [-twmyh] superiority. abargar [5/21 god, divinity. abarig(àn) ['Bblyk( ny] = abarag. abarig DPryk! | M ?Pryg, J ?Pry] other.
166:~ih: wonder. àb-dàn [^5d?n!] water-holder. abdast ['5dst!] hand-guard. abdom Pfdwm | М ?bdwm] last, final(ly). ~ih: finality, end. abd-sahist [pdshst'] wonderful. abē- [5»(y)- | M ?by-, N bé] without, Jess. ~-bar [-5/] fruitless. ---bé$ [-bys] unharmed. ~-bim [-bym] fearless. ~-bimih: fearlessness. e--boy [-bwd] senseless. ---bēyih : senselessness. —-büd(ih) [-bwt', -bwtyh] deficiency. «=čim [-cym] without reason, cause. abēdān рругп!] of use, wanted. abé-|-guman [-gwmn!] without doubt, certain. —-$umiünih : certainty. ~-mizag [-m(y)ck!] tasteless. ~e must [-mwst'] uncomplaining, content. ~-niyaz [-пуа?с] free from want. ~=-68 [ws] M *by?wš, N béhóf] senseless, unconscious. -~-6Sih : senselessness, unconsciousness. abér [yl] very, much. abē-rāh Payis] e erring. abesar [fysl | M ?bysr, N afsar] crown. abesīhēnīdan, abesihén- [Ashyn-ytn', v. abesihidan] destroy. išn(īh): destruction. abesihidan, abesih- Pžs(y)%-ytn! | M? bysyh-] perish, be destroyed. —išn(ih): destruction, ruin. abespardan Pžļsp?/tn!) = abespurdan. abespurdan, abespār- [’fspwltn', ?psp'l- | M ?byspwrd, ?byspr-, N sipurdan, sipàr-] commit, entrust, consign. ubestag [5(y)s? k!] Avesta, the Mazdean scriptures, abestām [ēst m] = abestān. abestàn [°25/°п!] refuge, support, trust. ābestan Dóystn! | P ?bystn, N abtstan] = ābustan, abé-süd [yý swt'] profitless. “Аһ: profitlessness. a-bëš Буў] harmless; unharmed, invulnerable. ~ih: harmlessness; invulnerability. abē-|-wināh [-cwz?^s | M?bywr? 1] innocent. ~-wizend [-wznd] harmless, invulnerable, safe. abézag Pfyck! | M ?bycg, (N *oëza)] pure, holy. ~th: purity, holiness, abēzār Pye’, ?Буе?1 | N bézdr] free.
196:~ih: disbelief. an-āštīh [?n’styh] discord, enmity; disquiet, unrest. ānay-, v. ānīdan. an-ayād [?7’byd’t'] forgotten. an-āzarm [cim] without respect, dishonoured.
219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āškārāg (34 1Q)k! | M sq?rg, N āškārā] obvious, evident. ~ih: revelation, confession. aškaragënidan [$k*Pkyn-ytn!] reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N šunawā] hearing. —ih: (sense of) hearing. āšnūdan, āšnaw- [OSMEN-tn! < А « ўт; топі | M? fnwdn, ?fnw-, N funüdan, funaw-] hear, understand. ~išn: hearing. або [šwk! = Av. ašawa] righteous. āšūb [>р | P swb, N ~] disturbance, turmoil. Aštād [s?t! | Md, N ~] the goddess Rectitude; cal. 26th day. aštag [štk'] messenger. ~th: mission. aštar РД whip. āštīh Pštyh | M 7st, N āštī] peace. Ašwahišt Piwhst'] = Ardwahišt. āšyān(ag) ['syd?n(k) | (M ?hy*ng), N ašyana] nest, lair. ātaxš Pths = Av. ātarš | N ātaš] fire. āwādaģ Pwb'tk! | J ?zo?d] generation. āwahan [wb’hn'] fortified place, stronghold. амат ['wbm | M ?w^m] time, season. -āwand [ла | M 2w(y)nd] suffix forming adjectives of quality. awar [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v. āwurdan. a-wardàg ['wit?k&!] undeviating. a-wardisnig [?wltsnyk'] immutable. Аһ: immutability. āwarišn [zoblfn! | M *wryšn) abode, home. a-warzid [Pwicyt'] untilled. *Aiwas-, v. tāwištan. ама [Pc | N ~] voice, sound. a-wazisnig ['wcfnyk!] immobile. āwēnīdan, āwēn- ['wyn-ytn! | (P ?bzoyn-)] admonish, blame. ~i$n: blame, reproach.
225:ayābāģ Dy'p()£!] acquisitive, receptive. ~ih: comprehension. ayād Pbyd?t' | M? yd, N yad] memory. ~ kardan; remember. ~gar LEI | N —gàr] memoir. āyaft Pdypt' | M ?ypt, N āyift] boon, favour, gift. ayāftan, ayüb- [5?5-tn! | M *3pt,*?b-, N yāftan, yab-] obtain, acquire, attain. ayār [kdybl | M hy’r, N yar] helper, friend. ~th: help, friendship. ayārdēnīdan, ayārdēn- ['4?/tyn-ytn!] boil, agitate. ~i&n: agitation. ayārdīdan, ayārd- Py’lt-ytn! | M ?y^rd-] be agitated, seethe. ayārīdan, ayür- [hdyb'l-ytn! | N yār-īdan] 1. help, assist; 2. be able, dare. ayürómand [hdyb’Pwmnd | N yarmand] helpful, friendly. ~ih: helpfulness, friendliness. ayāsīdan, ayās- [’byq’s-yin' | M ?y^s-] remember, be mindful of. „išn(īh): memory. ayāstan [by@’sin' | M *)*st] = ayāsīdan. āyišm [dšm] moon. aydxšust [ywhhhwst! = Av. ayóxfusta- | M ”ywxšyst 1] metal. ~€n [-yn'] metallic. āydoxtan, āyēz- ['ywhtn!, ?ywc-] join, yoke. ~išn: union, alliance. 14ydzidan Pyweytn'] = āyēūxtan. tāyozīdan, āyoz- Pywe-ytn' | Р уші, ?ywz-] trouble, disturb; strive, struggle. ^-i$n(ih): endeavour, strife. laz [MN < A mn; hc | Mc, ?z, N ~] from, than. žaz Dell dragon. *az [ANE < A?nh | P >z] I. āz Pc | M ?z, N ~] greed, lust. Ba, z- azabar [hcpl | M?c?br, № zabar] above. 7 āzād Pot! | M ?zd, N ~] r. noble; 2. free. āzādīh Petyh] т. freedom; 2. gratitude, thanks. ~ ģuftan, ~ hangardan, ~ kardan, pad ~ dāštan: thank, give thanks. атат [?с?[ | N ~] torment. āzardan сіп! | M ”zyrdn] = azardan. āzārdan, āzār- Pc/-tn! | № ~] torment, injure. ~išn: torment, injury. lāzarm [clm | M ??zrm, N ~] honour, respect. *'ázarm [?clm | M ?zrm-] harm, injury. a-zarmān Pz/mn!] ageless, unaging. āzarmīģ [clmyk'] honoured, respected. ~th: honour, respect.
270:bēyēnīdan, bóyén- [bwdyn-ytn'] scent, perfume.
343:~ih: plenty, prosperity. e frāxēnīdan, früxén- [pP hwyn-ytn!] enlarge, make prosper.
352:frazāmēnīdan, frazāmēn- [plc*myn-ytn!] = frazāftan.
=== PHD leaf with nidan ===
leaf 22 delete xüg ... (read hüg). delete xükar(ag) ... (read hükar(ag)). for for xwaday ... read N xuday. xwarg ... add live coal. yazd ... read yazad ... N izad, yazd. yazdan ... read yazadan .. Amend Engli
leaf 24 cessity. ~išnīg : necessary, fitting, seemly. abāz [L AWHL < A lI2(w)hr;?Pc | М Рс, N baz, wa] back, again, re-. ~ айдап б: attribute, ascribe to. 7 appoint t= ~ dāštan: withhold, restrain, prevent. ~
leaf 31 conut. an-arzünig [?77/c”nyk!] undeserving, unworthy. an-ast [^n 4 Y T'] non-existent. ~ih : non-existence. ānāst [?n’st'] spoilt, destroyed. ~ih: destruction. ānāstag [Mrstā!] = ānāst. an-āstawān [”1
leaf 34 , ~išn, v. āsūdan. a-sazāģ ["sc? k!] unfitting, unsuitable. a-sazisn|ig Dscfn-yk'] imperishable, permanent. ~ih: imperishability, permanence. a-sēj [Psyc] free from danger. asém Deum | = M, N sim] sil
leaf 35 ] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āš
leaf 37 appiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan. ayabag 15 azarmigih ayābāģ Dy'p()£!] acquisitive, receptive. ~ih: co
leaf 41  sorrowful. béwar [Буш | M bywr, N ~] myriad, ten thousand. P bid [руй | P byd] again. bidaxš [byths] viceroy. *bifagàn [bch'n!] medicinal. bim [bym | = M, N ~] fear, terror. ~gén [-kn'] fearful, terr
leaf 56 ansient. ~ih : transience. frasp [plsp | N farasp] roof-tree, beam, mast. *fra& [5/5] spear. fraš(a)ģird [piškrt! | M prš(y)gyrd] the Restoration (at the end of time). ~ig [-yk!] of Eternity (after th
leaf 67 . *hawan [/?zn! = Av. háwani-] the morning gdh. hāwand [/?wnd | M ÞPw(y)nd] like, similar. ^h: likeness, similarity. hāwišt [h’wst'] disciple, pupil. ~ih: disciplehood. haxt [h()At'] thigh, haunch, hi
leaf 69 ng (daevic). hunušakēnīdan [hwnskynytn'] bear daevic offspring. hu-pādixšā(y) [hwp?thš”(d)) good ruler. ~th: good rule. hu-passandagih [hwpsndkyh] satisfaction. hur [ŠKL < A fkr; hwl] an alcoholic dri
leaf 72 , lady of the house. ~ig [-yk'] domestic; servant. ~-xwaday [-hwty | P gdyxwd?y, N kadxudā] householder, master of the house. kadām [ktm | M kd?m, N кийат) which, what. c--iz-é(w) [-c-H D] whichever. 
leaf 82 burdan: pay homage. nām-burdār [л?т bwlt?l | N ~] heir, preserving the father's name. nāmčišt [?жт-, ŠMcst'], (pad) ~: in particular, especially. ~ig [-yk'] famous, well known. nāmīģ 58 namig [n’myk' 
leaf 99 an. sanwar [snwl = Av. 0anwar-] bow. sar [LOYŠE < A r'šh; sl | M sr, N ~] head; top, summit; end, begin- ning. | sarāsar [s?s] | N ~] from end to end. sard [s/t! | M srd, N ~] cold. ^Àh: coldness. sar
leaf 106 ient. ~ih: patience. Skeft [škypt! | P “#kyft, N šigift] hard; extraordinary, astonishing; very. ~ih: hardness; hardship, distress; astonishment. šken(n)-, ~išn, v. škastan. ških- [fkyh- | N šikth-] b
leaf 108 suffix forming comparative adjectives. tar [2] | M гу] darkness. tarāzēnīdan, tarāzēn- [tcyn-ytn!] weigh. tarázüg [tPcwk! | (P tPzwg), N tarazü] balance, scales; astr. Libra. targ [tlg | N ~] helmet. 
leaf 111 t?n! = Av. uštāna-] soul, ghost. ~th : vitality. ~отапа [-'wmnd] living, animate. uštar [GMRA < А gmD ;^wstl | N uštur] camel. 7—-$üw-palang Puštlg”plng | № ~) giraffe. uzdehig [we-, ^wzdhyk! | M ?wzd
leaf 112  ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] 
leaf 123 üfrün 96 yal xwarūfrān [hwl(’)wpl’n' | M xwrwpr'n) sunset, west. xwarrah [GDE < A gdh | (M prh, N farr)] fortune, glory, splendour. ~6mand [-’wmnd] fortunate, glorious. xwarséd, v. xwarxséd. xwartar [
leaf 124 hr] holy, pure. ~th: holiness, purity. yojdahrgar [ywsd’slkl] purifier. ~ih: purification, sanctification. убх [ywc | N ~] cheetah, hunting leopard. Z zádag [2’tk' | М side, N zāda] born; child. тайап
leaf 126 [zlwp-tn'] = azruftan. zūd [zwt! | M zwd, N ~] quick(ly). ^h : speed. zür [zwl | M z*wr] false, deceitful. Zür-gugày тоо zyānūmand zūr-ģuģāy [zw/gwk”dy | M zwrgwg'y] false witness. ~th: false testimon
leaf 127 g-go(w). affability huēwāzīh. affable nuēwāz. affair kar, kard, tis. affection grāmīgīh. afraid, be ~ tarsidan. after fraz az, pas az, pay i. afterwards pas. again abaz, did, P bid. against padirag. k
leaf 128  zardalüg. Aquarius Dol. aquatic ābīg. Arab 'Tazig. arch-demon māzandar. archer kamāndār. architect ráz-kirrog. archives déwàn. ardent garmog, taftig. Aries Warrag. ark kēwūd. arm baza. armed zenig. a
leaf 129 , skin ~ hambān, mask. baggage bunag. batt čīnag. bake poxtan. balance tarāzūg. ball gēy. banana mēz. banish pad débahr адап. bank, river — bār. banker gāhbed. banner drafš, nīšān. banguet sūr, xwaran
leaf 130 nišn, érang(ih), nikoh- išn. blame (v.) āwēnīdan,  éraxtan, nikēhīdan. blameless anērang. blameworthy āwēnišnīg, nikēhišnīg. blaze waxšīdan. blazing waxšendag. blemish āhēg. bless āfrīdan. blessed far
leaf 133 ng garzišnīg, must6mand. complaint garzišn, gilag, must. complete (a.) bowandag, hangirdig, (u)spurrig. complete (v. ) frazaftan, hangirdén- idan, hanjaftan. completeness hangirdigih, spurrigih. compl
leaf 134 ool down afsardan. cooling afsarišn. cope with abar madan. copper roy; (a.) rūyēn; v. coin. copulate gadan, marzidan. copulation māyišn, marzišn(īh). copy pa(č)čēn. coral wassad, xróhak. coralline was
leaf 136 àmagómand. desist from abaz éstádan az. desolate awérag, awērān. desolation drošag. despatring anummed. despatch (n.) wisé; (v.), v. send. desperate gyan-abespar. despise tar kardan / menidan. destiny
leaf 141 rce must, stabrih; vital ~ axw. forehead anig, pēšānīg. foreign anódagig, uzdehig. foremost pāhlom, pēšēnīg; ~ seat pëšgah. forest razür; v. wood. forget frámustan, az daxšag Шап. forgive abaxSayidan,
leaf 146 tive agar, armēšt. inactivity agàrih. incantation afsón, nérang. incapable anabzàr, anādūg. incline grayidan. incorrigible kordil. incorruptible apēhišn. increase (n.) abzón, abzāyišn, fra- dahišnih, 
leaf 148 b. lead (v.) anidan, franāftan, haxtan, nidan, rāyēnīdan, zaménidan, adēn-; ~ up ahrāftan. leaden arzīzēn, srubēn. leader parwānag, sālār. leadership parwānagīh, pēšēbāyīh. leaf wal/rg. lean grāyīdan.
leaf 151 . morocco leather saxtag. mortal anēšxwar, géhanig, marg- ómand, 686mand, sazišnīg, mortar hawan; (lime) агар. mosque mazgit. mosquito paxsag. most frahist. mother mad(ar). motion jumbāgīh, Jumbisn, r
leaf 152 wül(i$n), parwarišn. now nian; had. noxious creature xrafstar. number mar(ag), sag. nuptials wayddagan. nurse, (wet-) dayag. nursing, nurture dayaganih. oath sógand, war. 125 obedience ēkānagīh. obedi
leaf 154 drustabed. physicist gēhrag-dānag. physics čihr-šnāsīh. physique tanbahr. pickled meat xámiz. picture pahikar, nigārag. piece  pürag; (backgammon, muhrag. pierce suftan. pig xüg. pigeon kabēd, kabótar
leaf 155 stūdan, (stāyīdan), šnāyīdan, praiseworthy burzišnīg, stāyišnīg. prayer namāz, niyāyišn; ahunawār, āfrīnagān, hūmāst. precisely gókànig. prefer wizidan. pregnancy ābusīh. pregnant abestan, abus(tan), 
leaf 157 š; v. repentance. regretful abaxSawand. reign šahryārīh; v. sovereignty. reject anaftan, spóxtan. rejection spūzišn. rejoice urwazistan. rejoicing urwāzišn. relationship brādarēdih. relation, relative
leaf 158 . richness tuwāngarīh; v. wealth. rider aswār. ridge griwag, téx. riding aswārīh. right drust. даап, griftan, righteous аһа, ahlaw, ardā, ašē, frārēn. righteousness  ahlawīh,  ahlāyīh, ardayih, frārēn
leaf 160 he. sheep mēš, pah. sheepfold, -pen pahast. sheet čādur. shell post, shelter war. shepherd pānāg, šubān. shield magind, spar. shine brāzīdan, drafšīdan, frēgīh- istan, tāftan, (tābīdan). shining brāzi
leaf 169 tan. surroundings parwār. suspend āgustan. sustenance rozig. swallow (n.) paristog/k. swallow (v.) obárdan. swear (oath) sogand xwardan. sweat (n.) xwēy. sweat (v.) xwistan. sweep muštan, rob-. sweet 
leaf 177 victory. triumph (v.) čērīhistan. triumphant abarwéz, Cer. troop gund. trouble (n.) duš(x)warih, widang. trouble (v.) āyēzīdan, ranjénidan. troubled ranjag, ranjwar. trousers Salwar. true rast, wabari
leaf 182 l ~ frazām-pērēzīh. victuals pih. vigilant gubrag, zēnāwand. vile wadag, zéfan. vileness wadagih. village deh, wis. vina (lute) win. vindictive kénwar. vindictiveness kēnwarih, vine raz. vinegar sik. 
leaf 188 wither hēšīdan ; cause to ~ hūšēnīdan. withhold abāz dāštan. within andarón. without abé-, bē az. witness gugāy; false — zūr-gugāy. woe wāy. wolf gurg. woman nārīg, тап; married ~ šūy- mand; young ~ z
leaf 194 0 1,000 C 6684 PAHLAVI KEY [134] 5 — EM 2142411312127 99 tazidan tazišnīh not taškanag tašt tadan tadar Numerals [183] 146 tarságáh tarsāg tarsīdan tarsagāh tarsagāhīh tarist sel tom tambür ünóh! tab 
leaf 195 rar ute» rar tagīg tag takēk tagarg -tar tar, tarr tarazén- tarāzēnīdan tarāzūg piht targ tars dat targumān tarwēn- tarwēnīdan trufš truftag truš talag, tarrag talagčīn tarmānīh tarmenišnīh tarmenišn 
leaf 200 šnāyišn šnāyīdan šnāz šnāz- šnāzīdan šaw- šawāg Soy, Suy šanēn šūymand -išn šan šnēhr šūnīg šūn šnūg šnūman šnūmag šnūšag drūdī šusīr salt sálagih! 173] jaw! Jawēnī šēwan frēst-Ī frēstādan? hil-t hili
leaf 202 U ISU ves e ©, Pee 1-2čīnag čīnišn čegāmag čegām-iz Cer čēlāngar čēlān Celangar čērīh čērīh- čērīhistan čim čim-gūwāgīh čimīg 1%īdan čand, čang Cand- éandih éandal Čang-srāy čandišn L?griw! éandidan c
leaf 204 5451170 13100 ureas 100 19 $2.2) 1020 №2170 Ale DE ре Soro -V03 PO 100 31 H 1117 o» 3 105 read т 15? vo - vro AS POUR Po HOUND Po -—— Po ASD ^6 120› 14) 6 Ро \^© We pattānūmand pattān padēxīh padēxēn-
leaf 206 VU» 0) VU» оу - ve YO OCO TAD a guo Aso ~ 114320 We 13.409 0 14590359 0 \3 22 оу We as \Stes O - Saas ees PAHLAVI KEY 156 [162] framēšīdan Wes 2 o framustan WE D Ф framüdan we e o frasawand 214 tu» o 
leaf 209 rārēn frāmēš frūmēš- frāmuštan frahist parrag frch pardāxtan frehbūdīh frehbūd pardāz- pardaxtan, parrēxtan PAHLAVI KEY [153] eod o 15160090 Air KUŠA VO уез оу ad 9 ^o PAS оу we32 0) DÉI cf 1rd es —1 
leaf 211  pa(č)čībāgīh frazand pēr, purr pēlāwadēn [155] ThE no TY 51 110 PRIE мо IOS uo = 39110 Wes) nuo VAS 4599 110) VA nes 15v" 0) New g GNU O 3° ос uo ~Pie Sve w Podio 160 [154] 1-2pešag 1 V. pēšpārag S e
leaf 212 O” tay poxtan ure 125 nem! 519 PAHLAVI KEY pērēzgarīh pīlbān pēm, pīm pēmēn- pēmēnīdan pimgen pës- pésidan pēsišn pestan pēč- pēčīdan pēš pēšānīg pēšūbāy pēšūbāyīh PE pēšār pēšārwār pēšgāh pēšēnīg pēš
leaf 213 ir Sr pādixšā(y) (Ou v» оу pidixtayth — “UCU у о pādixšīr Nas rey о pādyāb ` UU еу о) padyabib, ALI 00 t€» о) pādāšn VA My o padirán- ` - My yey a pādīrānēn- -p ry yey a pādīrānēnīdan W3 y ry We pādīr
leaf 214  MS $t о) 16ү” 0) Vts оу «Oras 0 dw 03579 \- су 0 ”\оу о) nery 19 ru о> © ГАУ” о» 1 $^ Y^ о) Str о) padyawandih “> (ry ve» o stardsmur starwan stardih stard stabr stabrih stabrag staft pah, pay pahnāy
leaf 216 Q335 spīzišn 1^0 2301 spiš ^U" Q335 spitāmān 16” 10 035 spēd-dār `o тез as» gáy- gādanī wattart wattarīh! srawēn- srawēnīdan srūwēn ` sarw, sraw, srü srūwar sarw bar-! burdan! srub srubén Srūš srūšīg 
leaf 217 sraxtag wad! sargén srišwadag srešk [143] 1355 ee - da z I 5 166 sahmgen sahmgenih sāstār sāstārīh rawen-! rawenidan! rawiánt raftan! saxtag sabz šast” sī haštād* sagēn nawad* sēn sēnag sen murw sezd 
leaf 220 urw wy Ww $6 murwnīš we NV 5G murnjén- 51136 murnjēnīdan 131936 mērd, murd Ne murdan Ae mustomand 1-3must mustgar Se F” ^ ale mozag ^ de 96 "пик mustan oe müdag muhrign mizdwar fro(x)s-t fróxtan! must
leaf 224 g ranjēn-, rūzēn- ranjēnīdan, rozēnīdan lawzēnag rūzīg rozwürag rozan ranjwar rozward rozgar ranjag, rozag rozbinag roz-Saban rosnih rēšn rūšnag rūšngar rodbar rodigan rodig 12го rüdan abàg! rūstūg ra
leaf 226 �mišnīg _ ~ rámián A» rāspīg we rāstīh 14 nu» rast ç е! гая \ 4» rāvīg PA) rāzkirrēg So labag PS lābakkar AS ee lābakkarīh rādīh [125] kadag man-t mānistanī māndanī man’, wiest? net rah- rah- rah, (23
leaf 227 c(w) . kahas kadagxwadāy kadagbünüg kadagig CM Pos Sims 4308 1535 5 25 176 kardagān 1%kardāg kam kamāndār kamān kamāl kamālīg kamistīh ‘kamist kamzor kamzorih kamar kamarband maygt arz! kastār kastärī
leaf 231 ān kārāgāh kārāgāhīh kārdāg kārīgīh kārīg kārēzār kārawānīg kārawān kārnāmag kahrubāy kalbodómand kālbod kārframān kārd kām kūm- ard! kūmistan kāmzīwišn kamagómand kāmaghanjām [115] 180 zardčūbug zam 
leaf 233  No aes EOS uv ins Wd» «S 5:6 "ovS ^O HU HH vo PS «MS AP’ ox S 182 PAHLAVI KEY [по] zahag 19S zahrag Kä: zāmyād YU g S zāmēn- - e$ zāmēnīdan Wes PAS zadan US zādag \зтеҳЅ zibāl NS S 1-1, zay- -aS zih 
leaf 240 šn 1745.29 41 nang Au wind- - 23 windādan Wed 11 niwéy- — 4911 niwéy- e 41) niwēyēn- -P niwčyēnīdan “тёз v 4911 niwē, wandag 155 141 wanigarih «D As" niwēyišnīh Be r^ 4311 niwévisn VU 4) VI windišnīgs
leaf 244 �īg v waxšgar м ну а wixšayišnīh wixšayišnīg wisšayišn T?waxsidan waxSendag waxšwar [91] 192 PAHLAVI KEY " [90] naxód MP v — Sach nal-, wal-, war- wārānīg 445 aA V waran ' У» ` narig ` A wālīdan, wari
leaf 245 9] LIU ITU Me U ier ro’) VISUS NËT ac) Td „дузу EL el — rz) — c tA (Wes vtt Vts” v5 VWres t” (el AZ ved a set 6r'\ зе +”\ WC ус vt єт” men t^ Wo t^, Y^ t^ PAHLAVI KEY [88] xO \ nihal, wahār, waxr eat)
leaf 247 HLAVI KEY [36] 7 rv reer мге” -dey Werder wor Seo o -0 1" оз \r6 30 we 116 Jas we 6 re 1.5t1€357 05 tee 1505 - (de es oru ко” 1510* sēr veo хоп! daménag zamigig zamig ^39 varā 1 45 set Viet zamigpaymü
leaf 252 n gumārdag jumb- dumbēmand jumbāgīh jumbīh- PAHLAVI KEY gon gonag dowom drustih drust gowizar gozénag gugay gugay gugayih gugayih gugan- gokanig gokan doganag gugar- gugārīdan gugārdan dēk gēūgirdūman
leaf 254 nert Узе» ү 25” ve ур KR — Aen Ap Wey Ae ECHT м уу Ir Ne SCH ^U79 ур 202 dagrand PAHLAVI KEY [70] ope dagrand-xwadāy t pay KÉ dagr-zīwišn gilagobàr gilag dagr-pattày dast!, xwarrah! xwarrahómand! dast
=== NYB nitan ===
349:akārēnītan [~-ynytn'] to incapacitate, to destroy 42%, — Paz. ägärined, Skr. v. vināšayati (SGV XII, 43).
497:apākēh [’p’kyh] 1. company; pat ~ together 5712, — 2. backward movement: pat ~ back 418; v. pat-apākēnītan. — 3. help, assistance 5919-20, 729-26 (opp. ha- mēstārēh). — V. lapāk and ?apäk. Paz. āvāgī. V. also apar-apākēh.
535:scindo). This act. is generally supplanted by the secondary caus. apasihčnitan from apa-sih-. — Note: — There is a synonymous vb. of uncertain origin which may have been influenced by the apa-sih- vbs.: Paz. awasdinidan SGV XI" = Phl *apa-sāyēnītan; "ps'dín! = apa-sāyišn Mx 15% (wanting in Cod. K); *pys’synytn' = apēsāhēnītan (the second -s- inverse spelling of h) DkM 175°. 351! (in the MS 13419. 27015), *pys'hšnyh = apesahiš- neh ibd. 180° (= MS 13816); to be de- rived from *apa-sü- *apa-säy- ‘to rub away’, cf s. v. apa-sütak ?
671:aržānīkēnītan [~-ynytn'] to consider a p. worthy, governing a subordinated clause without an introducing particle, 5318 in a very complicated passage 5317-21, which only seems possible to understand on the following suppositions: a) kū-t bahr hac man bé burt l. 19 is not a gloss, as I have marked it, but is governed by anak tč bavat l. 17 ‘it shall be unhappy for thee that thou hast bereft ...'; b) the clause kē ... aržānīkēnīt hom 1.17-19 is loosely attached to tē l.17; c) for MNW-t L<y> (MS very clearly MNWtl) read MNW kw) LY» = kē tē man, to man being the exact counterpart of LK ^NH = tč an (v. žan) 1. 19 and both signifying ‘thou and I’; d) YBLWN-m l. 18 and 20, and HWH'-m 1. 19, are the Ist. p. pl. coinciding with the Ist p. sg.; e) there is a wordplay between *š = dé ‘food’ l. 18 and ’$ = as (demonic) eye’ 1. 20 (as burtan 'to have a vision', v. 'aš; bahr ‘ministry’, v. this w.). Text: anàk tč bavat, marak, ke t(0» man fratom hac ax" i astomand andar Rdg u Notar hac bahr barišneh āš barom frac aržānīkēnīt hom, kū-t bakr hac man bē burt. niin-ip tē an pat apar-barišneh aš barom u et bavēt kū-t dušcašmiha al zänak nikēram i-t nest ‘unhappy shall it be for thee, little scoundrel, (that thou) — as thou and I first of all men in the material world between Räg and Notar have been found worthy of earning food by perfor- mance of ministry — that thou hast bereft me of the ministry. Now thou and I shall be enraptured in an ecstatic vision, and then it will happen that I shall see thee evil-minded in another house that is not thine’. The passage is the immediate continuation of the incident related in 537-15, Zsprm XII, 7 epitomizes 5316-21 as follows: dwlyslwb BR’ L zltwšt gwpt' "VK cygwnt pltwm HWH'-m b’hl wlweyk BR’ ’pknd HWH'-m ZK tw "NH KR?
715:āstēnītan [’stynytn'] to set up, to erect 398, 10912, Caus. of östätan (g.v.), both < *aipi-sta; the alternation ē- : ā- is pos- sibly due to shifting accent: *aivi-sté- > *ayyi-stā- > "ai-sta- > Estä-, but áivi-stá- > *dv-std- > *āstā- (divergent explana- tion Verbum 224). Cf MPrth pt. ’wystn’d ‘to put, to place’ (S), Ghilain 78 sq.
726:taš ['š] eye, of demonic beings 3118; ~ burtan to carry one’s eye (sight) far away = to have a vision of distant and hidden things 51-53, of the. pre-Zoro- astrian seers, v. also apar-barišneh and ef s. v. aržānīkēnītan.
729:v.s. v. aržānīkēnītan. — NP ä$ ‘meat, soup, broth'; cannot be identified with
848:Pywe't'] cikāmcihē Pourusäsp ku yazišn kunät whenever P. intends to perform a sacrifice 5313-14, — Av. (1231) yaoz- ‘to be agitated’; MPrth rzmy(y)wz ‘eager for battle’ (A-H III); Arm. lw. yoiz 'commo- tion, trouble’, but also ‘research, investi- gation’ (den. vb. yuz-em ‘to agitate; to scrutinize’); — ä-yaoz- ‘to agitate, to MPrth ”ywštn, ?ywz- (’y-) (A-H III), ”*ywštg ‘tossing’ (sea), ’ywz ‘violent; disturbance’ (MHC). Borrowed in MPrs in the same sense (Verbum 183) and also in BP: razmik adydzisn ["ywešn'] ‘the act of fighting in battle-array', NSt § 3; äyöz renders Av. yaozante Y. 654. In SW, where Z changed to z, āyēz- coincided with āyēž- and adopted its inf. āyuxtan, ef DkM 695 pres. äyöz-, but 6815 äyux- tārēh in the sense ‘strive for’. The genuine SW form of yaoz-: OP yaud-, v. yöd-; possibly represented by *āhēyēnītan (q.
1117:cê [MH; cyh 12111] 1. interrog. pron. what? 59. 726. 89? ete.; how? 1513, 51?!; with prep. 6 cé, pat cé, hac cē; cé rād? why? 351! ete.; combined with a subst.: ce zaman? 715, cē gah? 722; pat ce āivēnak? how? 76%; cé vinäs? 121, cē vat? 7322, etc. ; apar cē ātvēnak margēnītan i Zartuxst pursit how to kill Z. 4912-25-26, 4813-14 (apar governs the whole clause). — 2. rel. pron. what: či ndmakY ce ... nipištv estet, ce Šahpuhr" . . . framätY nipigstany P 2:3-4; kart" ... ce ... sahät P2:8-9; har ce 61.3218, 86%. 9618; ēt ce ... apāc āvurt 11214715; 361; pat hàn cim rād ce 121". — 3. conj. a) subordinating: because 105); ce ka id. 991. — b) coordination: for 2$. 619.22. etc., passim. — MH 305 wrong ideogr. for encl. -c(%). — < cahya, gen. sg. of Av. OP (422 sq.) ka-.
1248:dāyakānēnītan to tend, to nurse 50!9, daž- [dc-] pres., 3d p. sg. dazét 2418, to burn, to blind by cauterization. — Av. (675) dag-: ef NP dižan ‘acid, pungent’, Arm. lw. dazan ‘bitter, cruel’.
```


## [2026-09-07T18:22:08.432Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG around 18360 ===\"; sed -n '18355,18400p' CHEUNG.txt"
}
```


### [2026-09-07T18:22:08.499Z] TOOL RESULT

```
=== CHEUNG around 18360 ===


© Although the evidence for an Ir. root *naid is sparse, it can be established quite 
firmly, being attested in an East and a West Ir. language. No verbal forms other than 
in Пг., are attested, whence the Ur. root may actually be denominative. 

«PIE *neido- ‘flowing’ => LIV: 449 | Pok.: 761 


*IE COGNATES: Gall. Nida river name, Lith. Nieda river name 
*REFERENCES: DKS: 79; Werba 1997: 430; Shahbakhsh: s.v. nid- 


*naiH! ‘to lead’ 

*AVESTAN: naii- (паё-) ‘to lead’ || (+ *aua-) ‘to take, lead, bring down; to flow 
rapidly [of water]’ || (+ *upa-) ‘to lead on, upon’ || (+ *para-(a-)) ‘to lead, carry 
forth’ || (+ *fra-) ? ‘to bring to’ (cf. Waag 1941: 81). © On the translation of ҮАУ. 
natieinte (Yt 10.42), Y Av. franaiiata (N 70), together with possible OP parallels, see 
Hoffmann, Aufs.: 314, fn 2. = Liste: 41 

Pres. them.: IND. 35р. YAv. naiieiti (V 5.8 Е), med. 3sg. ? YAv. "naiiete (? P 59), med.(-pass.) 3р1. ҮАУ. 
naiieinte (Yt 10.42), INJ. med.(-pass.) 3sg. ? YAv. fränaiiata (N 70), SUBJ. 15р. YAv. upanaiieni (Yt 
9.18); Aor. s-: SUBJ. 3sg. OAv. naëšat (Y 31.20); Fut.: 3sg. YAv. naéSiieiti (Vn 6, rep.) 

*OLD PERSIAN: nay- ‘to lead’ || (+ *fra-) ‘to lead forth, provide’ = Kent: 193 

Pres. them.: impf. IND. 15р. franayam <f-r-a-n-y-m> (DB 1.87), 35р. anaya <a-n-y> (DB 2.88, DB 5.12), 
3р1. “anaya” <a-n-y> (DB 5.28), med.(/pass.) 3sg. anayata <a-n-y-t-a> (DB 1.82, DB 2.73) 

*MIDDLE PERSIAN: MMP n’y- (BMP DB(Y)LWN-) ‘to lead’ || (+ *a-) MMP ’’ny- 
(ВМР HYTYWN-) ‘to bring, lead’ = DMMPP: 239a, 49b f. 

Pres.: IND. 3sg. MMP n‘yd, SUBJ. 3pl. MMP nyy’nd; Partic.: perf. pass. MMP n‘yd, MMP nyd, nyyd; 
Inf.: MMP nyydn || (+ *a-) Pres.: IND. 15р. MMP "om, 2sg. MMP "on, 2pl. MMP ’nyd, SUBJ. 2sg. 
MMP ’n’yh, IMPV. 2pl. MMP ’nyd; Partic.: perf. pass. MMP ’’nyd 

*KHOTANESE: (+ *4-) ānāñä (gdv.) ‘to be brought’ = SGS: — 

*SOGDIAN: SSogd. n’y- ‘to lead’ || (+ *ati-) BSogd. tyny-, CSogd. tny- ‘to bring in, 
lead in, introduce’ || (+ *a-) BSogd. "och, CSogd. "ny, MSogd. ’’ny ‘to lead, fetch, 
bring’ || (+ *para-à-) SSogd. pr’ny, BSogd. pr’n’y, CSogd. pr’ny ‘to lead, bring’ || (+ 
*niZ-) SSogd. nyzn’y ‘to lead from’ 

Pres.: SUBJ. 3sg. SSogd. n’y’ty || (+ *ati-) Pres.: SUBJ. 3sg. CSogd. tny't, 3р1. CSogd. tny’nt, Impf.: 
IND. 3sg. BSogd. tyny, 3р1. CSogd. “tynynt, Pret.: tr. IND. 2sg. CSogd. tny’d’ry; Inf.: pret. BSogd.
```


## [2026-09-07T18:22:09.488Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v4 pdf page 314 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==314' incoming/BQT/BQT_v4_pages.txt | head -60"
}
```


### [2026-09-07T18:22:10.740Z] TOOL RESULT

```
=== BQT v4 pdf page 314 ===
[pdf page 314]
۲۳۱۳ - بیلگون پردها
جامه وامثال‌آن رنگه کنند ‎٩‏ - و سیند سوخته فیلفر * - بافا . بروزن و ممنی تیلیر
را نیز کنته‌اند که بجهت چشم زخم بر بناگوش | است که‌مشفف لیلوفرباشد وآن کلی است‌معروف
و پیشانی اطفالکشند ۲ . و هشهور .

فیلهر ؟ - بفتح بای فارسی بر وزن بی ثیل قللک - بسنی یل خم‌آسمان‌است
هنر , بمعنی لیلوفراست وآن‌گلی است‌معروف, | که کنایه ازدموست فلك باشد - وسپاهیآسمان
و بسنی کل کبودیرا کویند که بیارة‌آن بر درخت ! را نیز گویند -
پیچیده بالا رود » وآن‌نوعی ازلیلوقر باشدوبمریی فيلت - بروزن كيلك. مسر یل‌است-
قاتل‌النحل کویند بسکون حای بی‌نقطه. وگرفتن اعضا واندام را نیز کوبند بسن دو نان

فیلج ۴ - بر وزن ابرج . معرب نیله | انگنت دست چنانکه بدردآید ‎٩‏ +
است که به نبل مشهور است و بدان چیزهارنگه نیلگری کردن - کنایه از سبزه
کنند . ‌ روبانیدن باشد ۰

نیل‌خم آسمان - کنایه از نسوست نیلگون پردها «کنایه از آساها
آسمانی است. امت .

‎٩‏ یله (هم.) . از ساسکریت 8118 , معربآن از فارسی «لیلج» ( بکسراول, وفتح

‏سوم ) و « لیلج » ( بفتح اول وسوم ) (۸.م.) ( رك : لوفر۳۷۰ ). این کلمه را به 104180 (قر)
اطلاق کرده‌اند » ولی باید دادت که عرب همواره 028161 (فر) « 110610718 188118 را با
مونلد: ( 00610 12018016۲۵ ) خلط کرده است « عقار ۲۶۹ ف » ورك :

‏.5 .0 مق ن17۸2- 8100 ,واه

‏* نیلج , حوالذدی تميه‌المامة الئیل ... ویسمی ایا الطین‌الاخضر والمین‌الخضراء » «عقار ۲۸۹ ۰
یل کیاهی است از تیرة پروانه واران ( 1.681101861865 ) که ازآن رنگه آبی لیلی بدست
میآآید ودرلقاط گرم‌میروید « کل کلاب ۲۲۳*. ۲ - در دخهٌ میرزا (ابراهیم)اسیندسوخته
که بربناگوش طفلان مالند بجهت دفع چشم زخم «رشیدی» - رودئیل: 8 (فر) ع8711(انگه).
باقوت در معجم‌البلدان کوید : «هوتم‌بب لیلوی من‌الرومية » رودی بز رکه بافی‌بقای شرقی »
وآن ازشمبةٌ اسلی که از درباچة 878828 - ۷1010718 خارج شود » و ازناحیتی بانلاقی عبور
کند وسپس بنام بحرالجبل موسوم کردد . وآنگاه بحرالغزال" درآن ریزد و پسی بنام بحرالاییش
درآید . ازديك خرطوم . ازسمت راست بحرالازرق- کة ازحبشه میآید- درآن میر‌یزد. دِل‌ازلوبه
ومصر عبور کند ومصر را بوسیلهٌ طغبانهای متناویش مشروب سازد وبفاهره رسد و درآنجا مصب‌وی
آغاز گردد و دوشاخةٌ اصلی آن در بحرالروم ریزد. مجرای بل را ۹۵*۰ کیلومترداسته‌اند.

‏۴ < یلفر < پیلوقر(ه.م.) ۴ - معرب «یله» (ه.م.) و « بیل» ر4 : ح" ور4:

‏دزی ج ۲ ص۹۳۲ .۰ 9 یلیر اه یلوفر(ه.م.) ‎٩‏ - ر4 : جهانگیری.

‏2 لیلگون - بکسر اول ؛ از : نبل (ه.م.) + کون ( * کون ) ؛ برنگه یل »

‏آبی -اسبز : ۱

‏برآمد لیلگون ابری ز روی نیلگون دربا ‏ چو رای عاشقان کردان چو طبع یبدلان شیدا .

‏َ « فرخی سیستالی . دیوان ص۲ >.
بجای «بیلگون» اول » دربستی نخ : فپ کون.- نیز نومی اسپ استِ . و4 : نوروژنامه ميس

‏۳ وتعلیقات‌آن مس ۰.۱۳۰
```


## [2026-09-07T18:22:26.858Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON آنیلین ===\"; grep -n \"آنیلین\\|انیلین\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head\necho \"=== MON نیلوفر / نیل ===\"; grep -c \"نیلوفر\" MON_part1.txt MON_part2.txt 2>/dev/null"
}
```


### [2026-09-07T18:22:26.932Z] TOOL RESULT

```
=== MON آنیلین ===
incoming/MON/MON_2vol_Adena_v2_djvu.txt:84034:همه وانیلین است. (شیم.) وانیلین. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:84036:وانیلین: (.) (شیم.) مادهٌ معطری 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:84054:و دارای طعم سوزاننده است» وانیلین علاوه 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:84061:ضح. -وانیلین را غالا در بازار و تداول عامه 
MON_part2.txt:84034:همه وانیلین است. (شیم.) وانیلین. 
MON_part2.txt:84036:وانیلین: (.) (شیم.) مادهٌ معطری 
MON_part2.txt:84054:و دارای طعم سوزاننده است» وانیلین علاوه 
MON_part2.txt:84061:ضح. -وانیلین را غالا در بازار و تداول عامه 
=== MON نیلوفر / نیل ===
MON_part1.txt:7
MON_part2.txt:25
```


## [2026-09-07T18:22:28.386Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY نیل ===\"; grep -n \"نیل\" incoming/ARY/ARY_pages.txt | head -20\necho \"=== LKT nil/anil/lilac ===\"; grep -n -i \"^[0-9]*\\. *nil\\|anil\\|lilak\\|lila\\b\\|indigo\" LKT.txt | head -20"
}
```


### [2026-09-07T18:22:28.458Z] TOOL RESULT

```
=== ARY نیل ===
=== LKT nil/anil/lilac ===
707:216.  Ar.  bannä' : 'Baumeister';  hieraus  mit  Imäla/ä>e >  ü/  sp.  albani,  alba0l,  albanir  'Polier', pg.  alvanel  'Maurer',  Vb.  sp.  albanilear, Adj.  sp.  albanilesco.    [DE  65.
1140:Auch  ciwit  gesprochen:  'Indigopflanze, Indigofera  tinctoria,  indigofarben' ;  hier- aus rum.  civit  'indigoblau'.
2188:N.  pr.,  Halbinsel  in  Südasien  [ursprüng- lich ind.  sindh,  hieraus  pers.  hind  mit lautgesetzlichem  Übergange  von  s  zw  h und  schließlich  gr.  'Ivbia,  Adj.  'IvbiKÖ?, lat.  India,  indicus].  Bereits  gr.  ivbiKÖv bezeichnete  einen  Farbstoff,  den  die Spanier  später  aus  Ostindien  nach  Europa einführten:  ein  tiefes  Blau,  das  aus Pflanzenstoffen  hergestellt  wird,  und zwar  aus  einer  Papilionacee  Indigofera. Aus  lat.  tndicum  wurde  dann  sp.  endico, indigo,  pg.  indigo,  it.  indaco,  afrz.  iiide, prov.  inde,  frz.  indigo,  dtsch.  Endich, Indiek,  Indigo  'indischblau'.  —  Nach
2286:[Aus  tk.  jeni,  s.  hier  Nr.  953,  und  ceri 'Heer,  Truppe'  vom  Stamme  der,  ter 'eng  zusammenziehen,  vereinigen'  Väm- bery TktEtWb  S.  170,  Nr.  182  II],  Name des  stehenden  tk.  Heeres  von  1330  bis 1826,  in  welchem  Jahre  Sultan  MAH- MÜD  II.  die  Truppe  auflöste  [vgl.  Th. Menzel,  Das  Korps  der  Janitscharen.  In Beiträge  zur  Kenntnis  des  Orients.  I. (1902/03)  und  in  der  Beilage  zur  All- gem.  Zeitung  1903,  Nr.  284/286].  Hier- aus [und  aus  der  älteren  tk.  Form  ja- nycary]  bulg.  janil^arni,  serb.  janicar^ klruss.  janycar ,  jancar,  necar,  russ. janicar,  poln.  janiczar,  cech.  janicar ; dtsch.  Janitschar,  ndl.  jaiiitsaar,  engl. janizary;iLgiannizzero,  ivz.jannissaire, sp.  jemzaro,  pg.janizaro,  rum.  ianicer, ienicer.  [Devic  DEt  143.  ML  4583. Gorjajew  436.    Bern  SlEtWb  445.
3017:'Storch'  [onomatopoetische  Bildung  nach dem  Klappern  des  Schnabels,  ebenso  wie ass.  lakalaka  Del  HWB  885  a],  ebenso tk.  leklek,  vulg.  lejlek  [mit  Erweichung des  Gutturals  wie  in  Beg  >  bej,  s.  hier Nr.  282]  'Storch,  Kranich';  hieraus  rum. liliac  'Fledermaus';  serb.  lelek,  lilak, Cech.  lelek,  klruss.  lelek,  russ.  leklek 'Storch'.    [Gorjajew  184.
3070:1319.  Ar.  lilak:
3071:Auch  lailak  [aus  pers.  llläg,  niläg,  s.  hier Nr.  1568]  'Syringa  vulgaris,  spanischer Flieder',  dessen  lilafarbene  Blütensträuße zwar  keinen  Farbstoff  liefern,  aber  einem bestimmten  Blau  seinen  Namen  gegeben haben ;  daher  hieraus  rum.  liliac  'P'lieder', Uliachiü  'lila',  lulachiu  'Indigo',  it.  sp. lilac,  frz.  lilas;  hu\g.  Iii' ak,lulak'^Fl\edev\ Cech.  poln.  lilak  'dass.';  dtsch.  lila  'bläu- lich', engl,  lilac  'Flieder'.  [Ngr.  XouXctKi 'bläuliche  Farbe  oder  Tinte'.]  [DE  297. Eguilaz  439.    Mikl  SlEtWb  169  b.
3603:'Schwarz',  [aus  der  Zusammenstellung 'schwarz  wie  die  Nacht'  wurde  'schwärz- lich' und  schließlich]  'bläulich'  [titlas  <^ *nihlas  *nihras,  also  dasselbe  Wort wie  lat.  nigtr  <^  *niher  <^  *nihrus], ebenso  Tpers. mlä  'Indigo',  ar.  nila  'dass.'; hieraus  mit  ar.  Art.,  der  dem  folgenden n  assimiliert  wird,  sp.  anil,  anir,  kat. antßl,  pg.  anil,  frz.  anil;  ndl.  anijl,  engl. anile,  neel  'Indigo';  dtsch.  Anilin,  ein Farbstoff,  der  i.  J.  182i6  bei  der  Destil- lation von  Indigo  entdeckt  und  i.  J.  1884 aus  dem  Steinkohlenteer  hergestellt %vurde.  —  Vgl.  noch  angloind.  neelwalla 'Indigopflanzor',  neel-kothee  'Indigo- pflanzung'. [DE  196.  Eguilaz  269.  ML 5923,    Hobson-Jobson  31.
3763:N.pr.,  Name  einer  Stadt  in  Unterägypten, offenbar  äg.  Ursprungs  [p  wahrschein- lich der  bestimmte  Art.] ;  hier  wurden die  mit  Indigo  blau  gefärbten  Kittel  her- gestellt, welche  schon  die  Kreuzfahrer über  ihre  Rüstungen  zogen,  daher  mlat. pelusia  'pelusisches  Gewand';  hieraus frz.  blouse;  engl,  hlouze,  dtsch.  Bluse. Vgl.  BRUGSCH  in  der  Voss.  Zeitung 25.  1.  1891.  Sonntagsbeilage.
4274:Ebenso  malayälam  churutfu  'eine  Rolle (Tabak)';  hieraus  angloind.  engl,  che- root  'Zigarre',  bes.  eine  solche,  die  an beiden  Enden  abgestumpft  ist,  wie  es die  indischen  und  die  Manilazigarren früher  waren.   [Hobson-Jobson  188/189.
5266:gr«'ö"  626 gdbal  <ö'il gahara  631 gabbän  628 gabbär  629 gäbija  630 ^a/>?'  631 gädämasi  633 ^'a(/(i  634 ß'adt  635 <7«/f«  637 gaffäfa  637 ^'a/'»  638 gahäz  640 ^'aiö  641 ^ötrfrt  642 <|rt/<rt  643 galiiba  648 galada  649 gäliba  646 gälija  647 ^■ffZ/ä/j  648 </rt«(?ri  649 ganiä'a  651 gunial  653 gämi'  655 g<itut  656 ganill  658 ganiisa  749 ganam  666 ^rt>i&  661 ganhija  662 gandür  663 ganib  664 gamma  665 ganna  99 ^är  667.  1685 </öra  669.  1496 garaba  674 gurad  670 garafa  689 garäma  671 ^aras  672 garb(t)  674 garbäl  673 ^arf  676
5709:St.  75 Amalgam  1378 arnalgamieren  1378 Atnber  78 Amen  68 .4»iocA:  71 Amulett  866 Anakonda  74 Anatolien  76 angeschickert  j.  1787  b Anilin  1568 Antimon  918 Aprikose  247 Araber  89  c Arabeske  89  d v4r/rfftf  St.  1719 .4r?V>-  112 ^riojoTi  St.  1719 ^rnujii«?  104 ^rrai;  92 Arschitie  108 ^rsewa^  495 Artischocke  833 Asangue  St.  392 Äschere  St.  1915 Aschkenasi  120 A  schlauch  119 Assegai  2181 I  ^toir  St.  1574
8250:indigo  909
9796:arfor  501 adraja  485 aduana  526 aduar  502 adufa  538 adufe  537 agengibre  1930 oguajaque  2168 aguanafa  1535 ahorrar  886 ajarafe  1840 «;e&e  1735 ajedrea  1872 ajedrez(atama)  1871 ajimenez  1815 ajimiz  1816 ajonjoU  744 ajorca  1951 ajovar  1959 ajuar  1959 alabarda  823 alabega  761 alacena  871 alacran  4:1 alafia  24 alahilca  904 alamar  67 alambar  78 alambique  79 alambre  78 alameda  1364 alamud  72 alancel  1428 alaqueca  45 alarbe  89 alarde  94 aZaWf^o  59  d.  100 I  alarife  99 alatar  134 alazan(o)  870 albacea  2158 albaheca  761 «Zöate  226 albanilear  216 albanal  204 nlbanar  204 albani(r)  216 albanil(esco)  216 alhaqida  188 albaran  226 albarazo  224 ffife«r(/a  228 albardän  241 a/fcarrfi  dial.  242 albardin  242 albaricoque  247 albarrada  249 albarrän  251 albarrana  251 albarraz  762 albayaldar  6 albayalde  6
```


## [2026-09-07T18:22:50.039Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY latin index NIL ===\"; grep -n -i \"NIL\\|NILUFAR\" incoming/ARY/ARY_latin_index_pages.txt | head -20\necho \"=== AFM nil ===\"; grep -n \"النيل\\|نيلج\\|نيل )\" AFM_pages.txt | head -20"
}
```


### [2026-09-07T18:22:50.098Z] TOOL RESULT

```
=== ARY latin index NIL ===
364:‘sey Set ey ENRICO CAMPANILE Sts coeaal
1632:UD-+MATI SANSKRIT) 4 Sonile HOLD PERSIAN) Stoel go jh,
2347:ASWINAN «(OLD PRUSSIAN) eS 13% Asvas, ASVAH (SANSKRIT) cs Sunil
2850:BADHAM (SANSKRIT) sey Senile 3,"
3718:BHAGA,, (SANSKRIT) xz nile
5843:TANAKTI, TANC :(SANSKRIT) cy Sunil TANG (PAHLAVI) (5 ghey
5870:(SANSKRIT) 4 Sunil
6026:TISTEL NORWEGIAN) $535 SANSKRIT) <y Sunile
6302:(PASTURE, GRAZE) 146-147 (SANSKRIT) oy Sunil
7338:SUGGA, SVIN (NORWEGIAN) «5595 (SANSKRIT) ny Snile
7510:‘REFERENCES behey (SANSKRIT) ey Sunil
7721:MACKENZIE: . (SANSKRIT) toy Sunil
7740:DRZWI (POLISH) tng! DVARAS SANSKRIT) ep Sunil
7834:‘REFERENCES beth DHRUVAS (SANSKRIT) ny Senile
7960:NUODARAS ALETTIC) (3) sd) (SANSKRIT) cy Sunil
8640:RUMPR re \cnil
9199:GENU HITTITE) <a JANU. (SANSKRIT) 4 Sunil
11054:AGANSRRIT) oy Sunil SHKAFTAN, SHKAF. :(PAHLAV]) «5.314
11305:LET, LED BRETON) 35» SANSKRIT) ay Snilee
11540:‘REFERENCES thay (SANSKRIT) Sy Sanile
=== AFM nil ===
3378:ورق النيل
3963:7 ما عليه من الزرقة و يرك الماء فيرسب النيلج اسفله كالطين ܐ (4&¬0
3972:الحنا حين ( حيط المحبظ ) ٠‏ وقال صاحب البيغان القاطع :« النيلوفر ورد معروف يظلهر
```


## [2026-09-07T18:22:50.481Z] TOOL CALL #35: Bash

```json
{
 "command": "sed -n 1,40p tools/fetch_source.py"
}
```


### [2026-09-07T18:22:50.541Z] TOOL RESULT

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


## [2026-09-07T18:22:55.100Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(txt):\n    if 'النيلج' in p or 'النيلوفر' in p:\n        print('=== leaf',i); print(p[:2500])\nEOF"
}
```


### [2026-09-07T18:22:56.396Z] TOOL RESULT

```
=== leaf 156
ܚܝܚ © ܘ | كك
11 ‫ 0[ )3 معرب وده
(3) الكتات الذي 4 فيه تعريب ثامه وبنوا.منة فملا وقالوا غقّ
3 6 الاراعى ` ܢܡܩܐ و شربه اليونالي 94 اي الناموس
جد ( العا 096 ܦ £ حجم الخردل .0 (08(8421¶÷ 0 2 93
106 ) تعريب 3( اللبز. والمب المذكور سني به لاه
ܝܣ
(التوردجة ) الضميمة وما أف من كل شىء ء 5 لورده
(التَاوق ) الطنشمة المنقؤرة التى يري فيها الماء في الدواليب 3 تاوه
00 ال لتيل اشىء مث عرس نذلاة ونان 99890
3 .
( | ܢܗ ) 6 تنشبه السحر ولست محقيقته وو( ܣ ܢ . ٠و‏ 1
الخر” راسكف ده ود 2 اأزجل اختلف اقالا ܐ وكذا في ܨܚ ܩ
النميمة والمثي بها 0 ذلك راجع الى معنى اككلمة الفارسية ܡ ܢܐܚ ومعناها 15
والمكر والسحر 6000 للدم 397 مر ةيه 1 لو رولك انل اللرن الال اذ الم
الحديدة ܨ يذ 112 8 با لسا نسكر ܚ ٠ومئها‏ 383 بالعبرائة 51
التَيِرّح ) بعنى القوي او القوة اذ يقال ريح نيرج اي عاصف فعرب عن ܕ ومعناها
القوة ٠و(‏ التَيْرج» بمنى ܘ ܐܝܐ ܐܚ فالظاهر اله مأخوذ من الارائي مش" وهو
القدوم ( راجع اضيا ل ا
79 نبات العظلم 'يصّغ به ازرق فارسلتةُ نيل وهو مشتق من نيلى و ©
بالسنسكر 3 اي ازرق ولعصيره يقال نيه بالفارسية ومنة انيلع ` ?: دخان
الغ حم يمَالج به 9 الوم وهو 2 ܨ د من ܠ ܫܝ بالماء
7 ما عليه من الزرقة و يرك الماء فيرسب النيلج اسفله كالطين ܐ (4&¬0
ويدف
܇ ‏ + من الزياحين تت في !1 الزاكدة 2 أصل
كامزر وساق أملس يعاول بجسب عق الماء فاذا ساوى سطاحة أَوْرّق وأزْهر واذا بلغ
يسقط عن رأسه ع داخله ܥ اسود ٠‏ 2 9 ܫܡ مركت دن نيل وهو الذي
ܐ
ܐ ܐ
=== leaf 157
ܢܐ }ܘ ܐ ܝܝ
:3 تر
يصبغ به ومن ܨ وهو اسم »ܓ 21 فل ܗ بنيل لان الورقة | مضموغة
الحنا حين ( حيط المحبظ ) ٠‏ وقال صاحب البيغان القاطع :« النيلوفر ورد معروف يظلهر
في طلوع الشمس فوق الماء ويزهر وفي غرويها يع في 2( وقيل اله عند وقوعه
في الاء يلقي طائر ويسقظ مكانة ويقم 2 مسترياً الى ان يظهر النيساوفر فيطير
ܫܠ ܝ € ٠‏ ومئه الفرسي 7 و شر به المونالي )ܐ
(النم» ' ̈ܡ ;© لبن وورق صغار وله £
حامض > 0 وحلا وهو يؤكل ( اقرب الموارد ) فارسَّهُ نم وفشر بشجر
مع | = ار اند صغير وكير زهره نظير عنقود كأنة حسمن كنن من البنفشة
وسطه اضفر لذيذ 3 وبعي - 9[ ' الفرو القصيد الى الصدر
ܪ 5-5 وهو مر كل م :ديه اي نصف ومن هاء التتخصيص وهو م 1106
(النئبرشت) الذي شوئ لصف ܝܨ ا ܝ 2 اي نصف ومن رسن
اي نثوى
التاى ) ܐܨ مخض وهو المزفار
م جب 7
0
# (المنّق) اتتكثير اعدمق ٠‏ وفيا القاموس الأحمى الضعيف والاشي بالدبيسة
ܘܗܒ 1 4 4091 المنافق السفيه ܨܭ 33 لغتان شه
8 (المازق) ܡ الغليان .‫ نبا 4:0 البق 5 15
لغات ܦ
: فقال فيه الشاعر الفارسى‎ )١(
` بكذرى شى بساغى 22 كش نياوفر‎ 1
ܐܐܟ ,ܝ ܳܐ برارد شدارد رق مث افا ست
```


## [2026-09-07T18:23:08.319Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://www.etymonline.com/word/lilac\" \"https://www.etymonline.com/word/anil\" \"https://www.etymonline.com/word/aniline\" \"https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A5%80%E0%A4%B2\" \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D9%84\" \"https://en.wiktionary.org/wiki/lilac\"; do\npython3 tools/fetch_source.py \"$u\" --note \"page 356, roots Nei 1/Nei 2: nil/lilac/anil/aniline chain\" ; done"
}
```


### [2026-09-07T18:23:15.359Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/03cf3bb106223877.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/540600d7aec313e2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e5550cb32b6fb627.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/51a65af935f67c44.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6478fc53893adca2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9e4f37b84688318e.txt
```


## [2026-09-07T18:23:18.437Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 03cf3bb106223877 540600d7aec313e2 e5550cb32b6fb627; do echo \"=== $f\"; grep -i -A12 \"^lilac\\|^anil\\|^aniline\" $f.txt | head -40; done"
}
```


### [2026-09-07T18:23:19.760Z] TOOL RESULT

```
=== 03cf3bb106223877
Lilac - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
=== 540600d7aec313e2
Anil - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
=== e5550cb32b6fb627
Aniline - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads
```


## [2026-09-07T18:23:22.788Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 03cf3bb106223877 540600d7aec313e2 e5550cb32b6fb627; do echo \"=== $f\"; grep -i -B2 -A8 \"Persian\\|Sanskrit\" $f.txt | head -50; done"
}
```


### [2026-09-07T18:23:24.072Z] TOOL RESULT

```
=== 03cf3bb106223877
=== 540600d7aec313e2
 anil (n.) 

 West Indian shrub from which indigo is made, 1580s, from French or Portuguese anil "the indigo shrub," from Arabic an-nil "the indigo," assimilated from al-nil , from Persian nila , ultimately from Sanskrit nili "indigo," from nilah "dark blue."
 also from 1580s 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 indigo 

=== e5550cb32b6fb627
 aniline (n.) 

 chemical base used in making colorful dyes, 1843, coined 1841 by German chemist Carl Julius Fritzsche and adopted by Hofmann, ultimately from Portuguese anil "the indigo shrub," from Arabic an-nil "the indigo," assimilated from al-nil (with Arabic definite article al- ), from Persian nila , ultimately from Sanskrit nili "indigo," from nilah "dark blue."

 With suffix -ine indicating "derived substance" (see -ine (1); also see -ine (2) for the later, more precise, use of the suffix in chemistry). Discovered in 1826 in indigo and at first called crystallin ; it became commercially important in 1856 when mauve dye was made from it. As an adjective from 1860.
 also from 1843 

 Entries linking to aniline 

 indigo (n.)
```


## [2026-09-07T18:23:29.706Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== etymonline lilac\"; grep -i -A10 \"lilac (n\" 03cf3bb106223877.txt | head -30\necho; echo \"=== wiktionary lilac (Persian mention)\"; grep -n -B3 -A6 \"Persian\" 9e4f37b84688318e.txt | head -40"
}
```


### [2026-09-07T18:23:29.768Z] TOOL RESULT

```
=== etymonline lilac
 lilac (n.) 

 1590s, shrub of genus Syringa with mauve flowers, with French lilac , Spanish lilac from Turkish leylak (the tree reached Western Europe via Istanbul), perhaps from a native Balkan name. Attested from 1791 as a color name; as a scent, from 1895. As an adjective, "pale pinkish-purple," from 1801. Related: Lilaceous .
 also from 1590s 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 lavender 


=== wiktionary lilac (Persian mention)
212-
213- Proto-Indo-European *neyH- der. ? 
214- Sanskrit नील॑ ( nī́la ) der. 
215: Middle Persian 𐭭𐭩𐭫 ( nīl ) 
216: Classical Persian نِیل ( nīl ) 
217-
218: Middle Persian 𐭪 ( k /⁠-ak⁠/ ) 
219: Classical Persian ـَک ( -ak ) 
220-
221: Classical Persian لِیلَک ( līlak ) bor. 
222- Arabic لِيلَك ( līlak ) bor. 
223- French lilac bor. 
224- English lilac 
225-
226- From obsolete French lilac (now lilas ), from Arabic لِيلَك ( līlak ) .
227-
--
332- Bokmål: syrin   m 
333- Nynorsk: syrin   m 
334-
335: Persian: یاس شیروانی ( yâs-e širvâni ) 
336-
337- Plautdietsch: Fleedabosch   m 
338-
339- Polish: lilak   (pl)   m , bez   (pl)   m 
340-
341- Portuguese: lilás   (pt)   m 
--
429-
430- Northern Sotho: perese 
431-
432: Persian: یاس شیروانی ( yâs-e širvâni ) 
433-
434- Polish: lilak   (pl)   m , bez   (pl)   m 
435-
436- Portuguese: lilás   (pt)   m 
437-
438- Romanian: liliac   (ro)   m 
--
586-
```


## [2026-09-07T18:23:40.516Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== wikt नील\"; grep -n -A6 \"Etymology\" 51a65af935f67c44.txt | head -60\necho; echo \"=== wikt نیل Persian\"; grep -n -B2 -A10 \"Sanskrit\\|Middle Persian\" 6478fc53893adca2.txt | head -60"
}
```


### [2026-09-07T18:23:40.573Z] TOOL RESULT

```
=== wikt नील
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 2 
68- Hindi 
--
76: Etymology 1 
77-
78- 2.2.1 
79- Adjective 
80-
81- 2.2.2 
82- Noun 
--
100: Etymology 2 
101-
102- 2.3.1 
103- Proper noun 
104-
105- 2.3.1.1 
106- Declension 
--
151: Etymology 
152-
153- 5.3 
154- Pronunciation 
155-
156- 5.4 
157- Adjective 
--
251: Etymology
252- [ edit ] 
253-
254- From Sanskrit नील ( nīla ) .
255-
256- Noun
257- [ edit ] 
--
271: Etymology 1
272- [ edit ] 
273-
274- Hindi Wikipedia has an article on: नील (रामायण) 
275-
276- Wikipedia hi 
277-
--
382: Etymology 2
383- [ edit ] 
384-
385- Borrowed from Classical Persian نیل ( nīl ) , from Arabic النِيل ( an-nīl ) , from Ancient Greek Νεῖλος ( Neîlos ) .
386-
387- Proper noun
388- [ edit ] 
--
571: Etymology
572- [ edit ] 
573-
574- Possibly from Proto-Indo-European *neyH- ( “ to be excited, shine ” ) , i.e. "the shining color"; see also Welsh nwyfiant ( “ splendor, gleam ” ) , Old Irish níab ( “ strength ” ) , noíb ( “ holy ” ) , Middle Irish níam ( “ splendor, gleam ” ) , níamda ( “ shining ” ) , Proto-Germanic *nīþą ( “ envy ” ) , Latin niteō ( “ to shine ” ) . [ 1 ] [ 2 ] 

=== wikt نیل Persian
262- [ edit ] 
263-
264: Borrowed from Persian نیل ( nil , “ indigo ” ) , from Middle Persian 𐭭𐭩𐭫 ( nīl ) , ultimately from Sanskrit नील ( nīla , “ dark blue ” ) .
265-
266- Noun
267- [ edit ] 
268-
269- نیل • ( nil ) ( definite accusative نیلی ( nili ) , plural نیللر ( niller ) ) 
270-
271- indigo , a purplish-blue dye obtained from certain plants , such as the indigo plant or woad 
272- Synonyms: بویا چیویتی ( boya çiviti ) , چیویت ( çivit ) 
273-
274- indigo , any leguminous plant of the genus Indigofera , but especially Indigofera tinctoria 
--
363- [ edit ] 
364-
365: Semi-learned borrowing from Sanskrit [Term?] .
366-
367- Pronunciation
368- [ edit ] 
369-
370- IPA ( key ) : /ˈniː.lə̆/ 
371-
372- Numeral
373- [ edit ] 
374-
375- نِیل ( nīl ) 
--
387- [ edit ] 
388-
389: From Middle Persian 𐭭𐭩𐭫 ( nīl ) , from Sanskrit नील ( nīla ) .
390-
391- Pronunciation
392- [ edit ] 
393-
394- ( Classical Persian ) IPA ( key ) : /ˈniːl/ 
395-
396- ( Dari, formal ) IPA ( key ) : [niːl] 
397-
398- ( Dari, formal ) IPA ( key ) : [niːl] 
399- ( Kabuli ) IPA ( key ) : [niːl] 
--
513-
514- Proto-Indo-European *neyH- der. ? 
515: Sanskrit नील॑ ( nī́la ) der. 
516: Middle Persian 𐭭𐭩𐭫 ( nīl ) bor. 
517- Arabic نَيْل ( nayl ) bor. 
518- Persian نیل 
519-
520- Borrowed from Arabic نَيْل ( nayl ) .
521-
522- Pronunciation
523- [ edit ] 
524-
525- ( Classical Persian ) IPA ( key ) : /ˈnajl/ 
526-
--
587- [ edit ] 
588-
589: Semi-learned borrowing from Sanskrit [Term?] . (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .)
```


## [2026-09-07T18:23:53.397Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ney-\" \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D9%84%D9%88%D9%81%D8%B1\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/neyH-\"; do python3 tools/fetch_source.py \"$u\" --note \"page 356: PIE *ney- 'to lead', Persian nilufar, PIE *neyH- 'shine'\"; done"
}
```


### [2026-09-07T18:23:57.248Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f0189b55a3454b41.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ff128b656df61678.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c318dd96a311a965.txt
```


## [2026-09-07T18:24:00.465Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== PIE ney- ===\"; head -60 f0189b55a3454b41.txt\necho; echo \"=== PIE neyH- ===\"; head -40 c318dd96a311a965.txt"
}
```


### [2026-09-07T18:24:00.505Z] TOOL RESULT

```
=== PIE ney- ===
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ney-
FETCHED: 2026-09-07T18:23:55Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
=== PIE neyH- ===
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/neyH-
FETCHED: 2026-09-07T18:23:57Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/neyH- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/neyH- - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in
```


## [2026-09-07T18:24:04.093Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -A30 \"Proto-Indo-European \\*neyH-\\|^ Root\\|Etymology\" c318dd96a311a965.txt | sed -n '1,80p'\necho \"=== nilufar ===\"; grep -n -B2 -A8 \"Sanskrit\\|Etymology\" ff128b656df61678.txt | head -50"
}
```


### [2026-09-07T18:24:04.189Z] TOOL RESULT

```
62: Etymology 
63-
64- 1.2 
65: Root 
66-
67- 1.2.1 
68- Derived terms 
69-
70- 1.3 
71- References 
72-
73- Toggle the table of contents 
74-
75- Reconstruction:Proto-Indo-European/ neyH- 
76-
77- Add languages 
78-
79- Reconstruction 
80-
81- Discussion 
82-
83- English 
84-
85- Read 
86-
87- Edit 
88-
89- View history 
90-
91- Tools 
92-
93- Tools
94-
95- move to sidebar 
--
134: Etymology
135- [ edit ] 
136-
137- Neo-root from a reanalysis of *(s)neh₁- ( “ to turn ” ) +‎ *-éyti , with the root laryngeal metathesized to after the *-y- suffix. [ 1 ] 
138-
139: Root
140- [ edit ] 
141-
142- *neyH- [ 2 ] [ 3 ] [ 4 ] 
143-
144- to lead 
145-
146- to churn (dairy products)
147-
148- Derived terms
149- [ edit ] 
150-
151- Terms derived from the Proto-Indo-European root *neyH- (12 c, 0 e) 
152-
153- *néyH-e-ti ( thematic present ) 
154- Hittite: [Term?] ( /⁠nēanzi⁠/ , 3pl ) [ 2 ] 
155-
156- Proto-Indo-Iranian: *náyHati ( see there for further descendants )
157-
158- *niH-tó-s 
159- Proto-Indo-Iranian: *niHtás 
160- Proto-Indo-Aryan: *niHtás 
161- Sanskrit: नीत ( nītá ) ( see there for further descendants )
162-
163- Proto-Iranian: *niHtáh 
164- Manichaean Middle Persian: [Term?] ( /⁠n'yd⁠/ ) [ 4 ] 
165-
166- Unsorted formations 
167-
168- Proto-Slavic: *něti [ 5 ] ( see there for further descendants )
169-
=== nilufar ===
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
157- Wikipedia fa 
158-
159: Etymology
160- [ edit ] 
161-
162: From Middle Persian nylw(k)pl ( nīlōpal , “ lotus, water-lily ” ) , ultimately from Sanskrit नीलोत्पल ( nīlotpala , “ blue lotus ” ) .
163-
164- Pronunciation
165- [ edit ] 
166-
167- ( Classical Persian ) IPA ( key ) : /niː.luː.ˈfar/ 
168-
169- ( Dari, formal ) IPA ( key ) : [niː.luː.fäɾ] 
170-
--
270-
271- Categories : Persian terms derived from Middle Persian 
272: Persian terms derived from Sanskrit 
273- Persian terms with IPA pronunciation 
274- Rhymes:Persian/ar 
275- Rhymes:Persian/ar/3 syllables 
276- Persian lemmas 
277- Persian nouns 
278- Persian terms with quotations 
279- Persian proper nouns 
280- Persian given names
```


## [2026-09-07T18:24:19.852Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%A2%D9%86%DB%8C%D9%84%DB%8C%D9%86/\" --note \"page 356 node 11: Persian آنیلین aniline, Mo'in entry\" 2>&1 | tail -2\npython3 tools/fetch_source.py \"https://www.vajehyab.com/moein/%D8%A2%D9%86%DB%8C%D9%84%DB%8C%D9%86\" --note \"page 356 node 11: Mo'in آنیلین\" 2>&1 | tail -2"
}
```


### [2026-09-07T18:24:24.034Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b372c26b3f6e1d2a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/689625fb07c0ed53.txt
```


## [2026-09-07T18:24:28.109Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== abadis\"; grep -n \"آنیلین\" b372c26b3f6e1d2a.txt | head -20\necho; sed -n '1,10p' b372c26b3f6e1d2a.txt\necho \"=== vajehyab\"; sed -n '1,10p' 689625fb07c0ed53.txt; grep -n \"آنیلین\" 689625fb07c0ed53.txt | head"
}
```


### [2026-09-07T18:24:28.179Z] TOOL RESULT

```
=== abadis
13: برابر پارسی : ( آنیلین ) رَنگ زا
20: ( آنیلین ) آنیلین. ( فرانسوی ، اِ ) ماده رنگی که از زغال سنگ گیرند. 
24: ( آنیلین ) ( اسم ) مایعی است بیرنگ و با بوی نامطبوع که در هوا کدر میشود و در آب کم محلول است و آن یکی از ترکیبات بنزین است اگر مخلوط نیتر و بنزین و براد. آهن و اسید استیک را تقطیر کنیم آنیلین بدست میاید . (اسم ) انیلین تازه مایعی است بیرنگ ولی با اکسید کنندها رنگهای مختلف میدهد مثلا با کلروردوشو رنگ بنفش میدهد . و آن ماد. اولی. عد. بیشماری از رنگهای آبی است و از احیائ نیتروبنزن بتوسط ئیدرژن بدست میاید . 
28: ( آنیلین ) [ فر. ] (اِ . ) مایعی است بی رنگ و با بوی نامطبوع که در هوا کدر می شود و درآب کم محلول است و آن یکی از ترکیبات بنزین است و نشانة آن در شیمی ۲ NH ۵ H ۶ C است . 
32: ( آنیلین ) مایعی روغنی، بی رنگ، مرکب از کربن، هیدروژن و اکسیژن که از نیتروبنزن به دست می آید و در رنگ سازی، داروسازی، و تهیۀ آفت کش کاربرد دارد.
37: آنیلین. آنیلین ( به انگلیسی: Aniline ) با فرمول شیمیایی C6H5NH2 یک ترکیب شیمیایی با جرم مولی آن 93. 13 g/mol می باشد. شکل ظاهری این ترکیب روغن مانند، مایع بی رنگ است. برای تولید این ماده ابتدا بنزن به نیتروبنزن تبدیل می شود، سپس نیتروبنزن هیدروژنه می شود. 
38:آنیلین پیش ماده ای پرمصرف در ساخت مواد شیمیایی لاستیکی، پلی یورتان، آفت کش ها، رنگ ها، مواد منفجره و مواد دارویی است. 
39: wiki: آنیلین 
45: آنیلین. آنیلین (aniline)
46:(یا: فنیل آمین) C۶H۵NH۲، یکی از ساده ترین مواد شیمیایی آروماتیک۱. با بنزن، که پیوند اتم های کربن آن حلقوی است، مرتبط است. در حالت خالص، مایعِ روغنیِ بی رنگ و دارای بویی مخصوص است. وقتی در معرض هوا قرار گیرد قهوه ای می شود. در قطران زغال سنگ۲ یافت می شود و در صنایع لاستیک سازی، داروسازی، و رنگینه ها به کار می رود. این ماده بسیار سمی است. در ۱۸۲۶ کشف شد و در آغاز از تقطیر۳ خشک نیل (ایندیگو۴) به دست می آمد. وجه تسمیه آن نیز همین است. wikijoo: آنیلین 

URL: https://abadis.ir/fatofa/%D8%A2%D9%86%DB%8C%D9%84%DB%8C%D9%86/
FETCHED: 2026-09-07T18:24:23Z
STATUS: 200
TITLE: انیلین - معنی در دیکشنری آبادیس

انیلین - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 انیلین
=== vajehyab
URL: https://www.vajehyab.com/moein/%D8%A2%D9%86%DB%8C%D9%84%DB%8C%D9%86
FETCHED: 2026-09-07T18:24:23Z
STATUS: 200
TITLE: معنی آنیلین | فرهنگ انتشارات معین | واژه یاب

'
 />

 معنی آنیلین | فرهنگ انتشارات معین | واژه یاب 

4:TITLE: معنی آنیلین | فرهنگ انتشارات معین | واژه یاب
9: معنی آنیلین | فرهنگ انتشارات معین | واژه یاب 
17: آنیلین
```


## [2026-09-07T18:24:51.556Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd2 p.321 (leaf 326) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==326' incoming/WLD/WLD_Bd2_pages.txt | head -30\necho \"=== WLD Bd2 p.336 (leaf 341) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==341' incoming/WLD/WLD_Bd2_pages.txt | head -20"
}
```


### [2026-09-07T18:24:52.757Z] TOOL RESULT

```
=== WLD Bd2 p.321 (leaf 326) ===
                                                   nei- (neia^^-)   — neik-                                               321


gen, amaxam) = lesb. a^u/ne, dor. d/ne (daraus                               fj/ueag,    f]/uag,    rj/iisig;   Poss. lesb.
ajuiLiog,    dor. djiiog        = av. ahma-, jon. att. i^jus-Tegog) usw.

1.     nei- „fuhren“ (neia^-).
       Ai. ndyati (Ptc. nitd-),                  av. nayeiti „fuhrt‘',         mp. nitan „fuhren, treiben'%
ai.     nttar-,        nUctr-     m.     ^Piihrer', neird-            n.   ,,Pubrung,      Auge“       ;
                                                                                                           ein ^nei-t-{s)
„Puhrer,        Heerfuhrer^^ vermutet Pokorny ZfcPh. 10, 405                                        wohl        ricbtig   als
Grundlage von mir. ne, nae^ gen. ogom nHas,                                       air.    math       (archaisch       nHK)
„Held“.
  Gr. dvivy]fii (Hirt IF.                  12,    219 f.)   &,   vielmehr u. na- „helfen'\


2. nei“ ,,gianzen'\
    Lat. niteo, -rre ,,glanzen“, yiitidiis „glanzend, fettglanzend, fett; von wohl-
gepflegtem Aussehen^', nitor „Glanz, Glatte“ {niteo auf Grund eines Ptc.
‘"'ni-to-, wie fateor           remdeo, -ere „erglanzen*^ (eig. ,,herniederglanzen“)
rait praesensbildendem -dih)-:, dazu '^nei-ma in mir. niam „Glanz, glanzen-
der Schmuck“, cymr. mvyf „Lebhaftigkeit'', mir. niamde „glanzend“, cymr.
mvyfiant „Glanz, Ge\valt“ nivyfo „lebendig werden^' (ansfiibrlich Osthoff
IF. 5, 299) mit Formans -hho- (vgl. z. B. doyv-q)og, lit. ral-has „gesprenkelt“)
                   ;


*noi-hho- in ap. naiba-, np. new „schon, gut“, air. noib „heilig“ (Liden
Stud. 59 m.Lit.).
    Hochst fraglich ist hingegen Zugehorigkeit von got. nidva f. „Rosk’
=== WLD Bd2 p.336 (leaf 341) ===
336                                                 nit    no-



niJiol„pronus“ aus "^niwol, mnd. nigel „niedrig^‘ (wegen i nichfc nach Fick
III* 297 zu abg.         hieher wohl auch lett nlwdf^ „verachtlich behandeln,
schinahen, niederdriickea'' (auch got. naiw          Marc. VI 19? Fick III*
297 zw.).
  Ygl. idg.            '^ni-’Zdos                unter sed- „sitzen“.      Als „heruTiterinachen‘‘
(wie      nhvdt) beruhen wohl auch
         lett.                                            7ieiq~ (s. d.), neid- ,jOV€idog^\ nit- „be-

feinden“ auf unserem nei-, ni-,
   Vgl. Fick BB. 1, 336, Wb. I* 95, 500, Schulze KZ. 27, 603 f., Qu. ep.
467 f., Osthoff MU. 4, 222 f., Brugmann IF. 1 1, 274, Grdr. II ^ 2, 861 f. Fick
und Brugmann vermitteln ne-i- mit ne-r- „unten“ und ndhos^ ndheri „unter“,
letzterer auch (recht fraglich) mit gr. jiQo-vco7iijg „nach unten geneigf‘,
v£vd>7irjTai TETajislvcoTat, xaraTtiTtXTqxxai Hes.
                  *
```


## [2026-09-07T18:24:53.674Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC nei ===\"; grep -n \"^nei-\\|^neia\\|^nei\\b\\|^nilo\\|^ni-\" IEC.txt | head -15\necho \"=== SYN leaf of 10.64 ===\"; python3 -c \"\ntxt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(txt):\n    if '10.64 LEAD' in p: print('leaf',i)\n\"\necho \"=== SYN leaf 775 head ===\"; awk 'BEGIN{RS=\"\\f\"} NR==776' SYN.txt | grep -o \"7[0-9][0-9]\" | head"
}
```


### [2026-09-07T18:24:55.008Z] TOOL RESULT

```
=== IEC nei ===
11580:nei “neither, nor'. WP II, 320. Cf. ne, ei Boeot. Arc. nei “indeed, yes? (a formal equi- valent, but semantics obscure, cf. Mod. Gk. nai yes); Cypr. ni. .. .ni... ‘neither. . .nor'; N. Alb. ne, ne, ., id.; OLat. nei, Lat. ni ‘f not, unless, that. . .not'; Osc. & Umb. nei ‘no’; Go. nei ‘not’; OHG ni, ON ní ‘no’; OCS and com. Slav. ni “neither; nor; Li. Latv. nel. . .nel. . ., id.
11581:nei- "down Cf. ni-, neiu- Gk. neí-atos ‘lowest’; neíara, adv. "lower; nei-óthen ‘from below’; nei-óthi “down below’; formant in OCS niže (‘below’, and com. Sl.); nici ‘face downward’; and in Slo- vene ni-Cati, inf. ‘crouch’; ni-hati, inf. ‘dangle’; z-gde in Skt. Av. ni- ‘down’; Oss. ní, ni, id.
11596:nei-quis, -quid “nobody, nothing; trifle, tri- vial person, scamp'. Var: -quos. Cf. quis, quid, quos, quod & ne-, nei-, ne-quis, etc. Oss. cf. (for the formation) níkw “never; no- where’; OCS nikyj ‘no, none’ ničí ‘nothing’; Li. niðkas ‘nobody; bad, wretched; scamp’; niekis, gs: -io, m. ‘trifle’; Latv. nieks ‘nothing; scamp’
11599:neið (1) “lead, send’. Gk. ambig. Skt. náyami “lead”; naye, mp. ‘go’; Av. nayc- (imi) "lead": Hitt. neyami, v. (1) “lead, send’; Gk. cf. ko-néo, egko-néo “hurry, wait upon, urge
11773:ni-teros, -tomos 'further down, nether; at the bottom, below, lowest". Cf. ni WP II, 325 Skt. cf. nitarám, adv. *below, lower'; Av. nito- ma- (lowest; OE nióer(e), neoóan, niðan, adv. ‘below, lowest? beside nip, n. ‘abyss’; MHG oder, niden ‘below’
=== SYN leaf of 10.64 ===
leaf 773
=== SYN leaf 775 head ===
```


## [2026-09-07T18:25:09.847Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN leaf 773-775 relevant ===\"; awk 'BEGIN{RS=\"\\f\"} NR==774' SYN.txt | head -20\necho \"---775---\"; awk 'BEGIN{RS=\"\\f\"} NR==776' SYN.txt | grep -o \"Skt. ni-.\\{0,400\\}\" | head -3"
}
```


### [2026-09-07T18:25:11.034Z] TOOL RESULT

```
=== SYN leaf 773-775 relevant ===
m’ to ‘send (a message)’ and ‘send’ in general, Pedersen 1.359, 2.525.
NIt. cutrim ‘put, place’ (12.12; ef. Ir, fo-ceird ‘throws’ 10.25), also ‘send’,
W. anfon (and danfon, with dy- ‘to’), perh. fr. *ndhi-mon-: Lat. monére ‘warn’, caus. of the root *men- in Lat. memini ‘remember’, Skt. man- ‘think’. Pedersen 2.301.
Br. kas (also ‘lead’), fr. Norm. Fr. casser = Fr. chasser ‘hunt, drive away’. Henry 56.
4. Goth. sandjan, OE sendan, OHG sentan, etc., general Gmc., caus. of the root seen in OHG-sinnan ‘travel, go’; OE sid, OHG sint ‘journey, course, way’, etc., hence orig. ‘cause to g0’. From the same root prob. also Lith. siysti, Lett. sitit. Walde-P. 2.496. Feist 410 f.
NHG schicken, earlier meaning ‘pre- pare, suit, adapt’, so MHG schicken = ON skikka ‘arrange’ : OHG sehen, NHG geschehen ‘happen’, etc. Weigand- H. 2.702. Kluge-G. 516.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
see under
re commonly Di te., genera ali. (iter ae Bice, ON
ric, Peres * Slavic, It ver; sell’,
Kner 499.
Igitized by Arya Samaj Foundation Chennai and eGangotri
N, TRANSPORTATION, NAVIGATION 711
presayati (so also OPers. fraigayam ‘I sent’; but Av. fraésya- ‘impel’ and ‘promise’, not quotable as ‘send’), cpd. of pra- ‘forth’ and 7s- ‘impel, hurl’ = Av. is- ‘set in rapid motion’ : ON eisa ‘start violently’, Lat. tra ‘anger’, etc., IE *eis-. Walde-P. 1.106 f.
Av. maé6- ‘mittere’, Barth. 1105, but
» tye 0 a _ Ee. 9.504 f. Bric hi Aah ! ; this sense dub. RY 4 am in presyati and caus. 1. . 10.64 LEAD (vb.) Goth. tiuhan Lith. — vestz rk. 1m trreouat ON. leida Lett. vest yo &nd Dan. __lede, fére ChSl.  vesti_ Int, _dilcere an Sw. _ leda, fora SCr.  voditi yt, menaré, © 4 OE ladan Boh.  vésti Bau ME _lede Pol. prowadzié
g' : 5 Fr, mener, conduire, gut- NE lead
Apart from an inherited group in which ‘lead’ seems to be the primary sense, words for ‘lead’ are cognate with others for ‘draw’, ‘seek’, ‘road’, ‘carry’, ‘0 (as ‘cause to go’), and ‘drive’. Strictly, one ‘leads’ from in front and ‘drives’ from behind, but in situations where both have in common the notion ee difference may be lost
) With resulting interchange.
1, TE *wedh-. Walde- deen 2.518 alde-P. 1.255. Pe-
---775---
Skt. ni- ni- (nayati, nita-), Av., OPers. ni- (Av. 3sg. pres. nayeiti, OPers, 3sg. imperf. anaya, etc.); cf. Skt. netar- ‘guide’, perh. : Ir. néath (Ogam gen. netas) ‘hero’. Walde-P. 2.321.
```


## [2026-09-07T18:25:11.926Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN nil ===\"; grep -n \"nll\\b\\|nil '\\|nll 'Indigo\\|Indigo\" HRN.txt | head -15\necho \"=== HUB nil ===\"; grep -n -i \"indigo\\|nllufar\\|nilufar\" HUB.txt | head -10\necho \"=== PLA nil ===\"; grep -n \"نیل\\|nīl\\b\" incoming/PLA/PLA_pages.txt | head -15"
}
```


### [2026-09-07T18:25:12.004Z] TOOL RESULT

```
=== HRN nil ===
=== HUB nil ===
=== PLA nil ===
```


## [2026-09-07T18:25:23.778Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN lufar/nil ===\"; grep -n -i \"lufar\\|nllofar\\|nilofar\" HRN.txt | head\necho \"=== HUB lufar ===\"; grep -n -i \"lufar\" HUB.txt | head\necho \"=== PLA arabic نيل ===\"; grep -n \"نيل\" incoming/PLA/PLA_pages.txt | head\necho \"=== PLA latin nil ===\"; grep -n -i \"nīl\\|nil(a)\\|nīla\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head"
}
```


### [2026-09-07T18:25:23.853Z] TOOL RESULT

```
=== HRN lufar/nil ===
=== HUB lufar ===
=== PLA arabic نيل ===
=== PLA latin nil ===
```


## [2026-09-07T18:25:24.661Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT nay all ===\"; grep -n \"nay-\" BRT.txt | head -30"
}
```


### [2026-09-07T18:25:24.712Z] TOOL RESULT

```
=== BRT nay all ===
3186:Pii. :  anapasmiin'\  [itx  Y.  g):  ana/VKäyistii); erl,;  ka  »."att  mal  "wenn  gegessen,  ials  wieder da";  Sü.:  atiavasääah.  —  ')  NA.  'jay'  mit rt4!  s.  aber  K  s  und  Yt.  75.  16.  —  >)  Vgl. lu  satil-.  —  Sl  Vgl.  ai.  apahänay-  f.
3308:6i  adukanay-
3315:•  p.  adu-kanay-  f.,  G.  mit  mäk-  m.  Name eines  Monats*':  °naism3hyil{,?A^  Bh.2.i2.
5007:•  j.  ava-kanay-  m.  'Graben,  fossa*:  ys aitfm  ai'aAan^m  avakatäa  yeiihä  v5  aisS 'nis  anhat  V.  75.39  ■>.
5883:•  j.  aspö-stäna-  m.,  'stänay-  m.  T/erde-
8820:•  j.  uströ.stlna-  m.,  °stinay-  m.  'Kamel- sialV:  yiziia  ag^a  gaowa  "naisva  frajasiit V.  /j5, 23  i  —yö  aitim  °n.im  uzdasta ''  yetihii vö  ag\i>  °ni.r  auhat  "wer  diesen  Kamel- stalt  gebaut  hat,  welcher  (fem.)  von  euch" dieser  Kamelstall  gehört"  V. /5.24.
9105:.J7-  S53.  3^-  259.  wo  weliere  IJtL a  j.  uätrö.stäna-  m.,  'stänay-  m.  'Kaniel- stall':  yesi'a  aSia  ga'uva  'naSii'a  /rajasäl V-  '5-^3i — yö  iiitjm  °n.>m  uzdasta'^ yi-i'jhii v5  a?\i>  'nis  auhat  "wer  diesen  Kamel- stall  gebaut  hat,  wciclier  (fem.)  von  euch" dieser  Kamelstall  gehört"  V.  75.24.
9487:•  p.  kapiäakänay-f,'i  Name  einer  Festung  er  mit  der  Strafe,."  V,7.38.         3)  para in  Arachosien'l ;  'nis  nUmä"  didä  Bh-S-g.  aisqm     irisintqm     raisS    cikatn'^    daaZs.-
9555:A^^-  ?■  ^w  ^  T'  ^'  ^°i, '"/"'"'  ""■  J'"^^"''' '  •  J-  kui^sänay-  m.  EN.  eines  von  Haoma
9581:Et.?    \^.  i>r»5nay--l    -    PÜ.    (lu   Yt.  //):    vff^geri  :   altlyS k' yaifgam  karapH  usixsca
9583:*iarsyüiiAä.  —    S.  lU  kirisänay-.    —    ')  J  10  ,       Vgl.  ai.  kam    Praen.    (mit    vorausgeh.    Dat.),
9869:•  j-^gac'^-Stäna-m.,  -stanay-  m.,  'Rin- derstall': yaua  ai^a  galwa  -naisva /ra- jasiit  V.  ;5.  29; — yö  altim  -tarn  uzdasta yerihh  v3  alsS  °nis  anhai  V.  /j.  30  ".
11265:•  j.  cäxsnay-')  m.  EN.  eines  Gläubigen: °nöt^''>  asaonS  Yt.  13. 114"*.
11511:KompE.  —  Superl.  lum  Praes.  5  des  V.  xan-. —  ai,  TgL  jdgAnay-  und  hänijlha-  Adj.  — Pü. :  ialärhim,  iaiär.
11556:KompE. ■  j.  Janay-,  g.  J^nay-  'Weib,  Frau':  t^ä i  hati^yä  (sd.)  «ürj  a>S  JjtiayJ  (VF.)  Y. 53-  6 ;  —  da^va . .  vasnfmram  *apa.kariay.>n
11559:ai.  jänay-  t,  np.  iow.  —  VgU  Jqnay-.  —  mp. in«,  (in  A):JiA;  s.  noch  No.  i.  —  0  Pt4 usw. ;  NA.  janyaos  (woiu  Bthl.  AF.  3.  64). Das^  erklärt  sich  wie  in  al.  säkhyau.  Pu.: /fl  io»im,  — ')  S.  Vir.  NA./ancfl,  ohne  Epen- these 1
11627:•  g.  JSnay-  f.:  s.  unter  Janay-.
11644:•  j.  Janay-  f  'Weib'  in  verächtlichem Sinn'':  %risum  aSaZsqm  axtinqm  'nayd dnnjaili  V.  7.  59  Gl.  (?).
11645:got.  qens.  —  Vgl.  janay-,  —  Pü. :  srisülak  ösän cnikih  }eh  {i.  janay-  a)  dranjenit.  —  >)  So  Dach pa.     Ganz  unRichcc.
12111:KompE.  —  Zum  Praei.  20  {*taurva-;  ai.  tur- vali)  des  V.  'lar-.  —  S.  noch  vispajaurvairl: —  ai.  vgl.  lurvine  Inf.,  lumänay-  Adj,
12367:•  j.  *tuänay-">  Adj.  'stillschweigend':  -«//'> F./*
12431:%ultray-.  Y.S.  7,  72,9,  60.  2,  Yl5.S9,  y. 99,  V.  2. 1,  2  (Sp.  346  m.).  7)  mäzda- yasnay-,  uzw.:  °nä  'yasni/ W.j.Jii,  43,  5. 21,  Yt  II.  i,  y.  94,  VytJ5;  —  'rtam 'yasnlm  Y.g.  26,  12.  9,  25.  6,  Yt  2.  14, g.  26,  V.  2. 42,  3. 31»,  40',  ig.  2,  6,  7,  16, Vd.  <?;  —  'nayä  ('nayäsca)  'yasnöil  Y, i2.9,  y.3'.  8,  15- 1,  22-25.  J5-I.  Vt;o. 117,  136,  J'9.69,Vr.j.  5,9.7,  ro.3,  72.3, G.  2.  7,  V.J.  30,  g.  2,  47,  52,  P.  i4,  FrB^ Nik.  j,  2;  —  'nayät  'yasnBii  ^.  41';  — •ne  'yasne  (s.  a).  S)  vanhav-  und  mäsda- yasnay-%  vaauAi  'na  °yasnif  Y. 3,42,  Yt. '3-  94;  ~~  vaauhJm  °nqm  'yasnlm  Y. g.  26,  V.19. 16;  —  'nayä  vanAuyä  'yas' nBif  Y.  22. 3.  S.  femer  zu  7  und  0 unter  a.  a)  als  Gottheit",  immer  mit mäzdayasnay- fiäy.  ya%a . .  äs  saoiS  mana yat  ahuraAe  mazdä  'nayäsca  •yasnsii  Yt. ig.Zz;  —  m(hr»m  .  .  yeAAe  °na  'yasnil lfm  (sd.)  pdhs  rähaiti  Vt  10.  68;  —  pUa /?(näml.  asöii)  yS  ahurS..brata..sraolS.. :^at3ha  'na  'yasnis  Yt  ij,  16;  Yyt $2;  — usia  ml  aAura  mazäa  . .  usta  'ne  (VS.) 'yesne  Yt.  Ä  29;  23,  Y.  S.  3;  —  'na  'yasne Yt/Ä8(?);  —  v:>n%ra^n3m  ya^  °nay& 'yasnsis  Vyt  42;  10,  34,  J7.  a)  sonst
13388:Ableit  aus  'dänay-  m.  EN".  —  ■>  Denkbar wäre  auch,  dass  dänayana- za 'dSnav- gehöit; vgl.  lu  märgaya..
13427:•  g.  'dämay-,  g.  d^nay-  Adj.  (auch fem.)  'schaffend,  Schöpfer',  a)  absolut  oder b)  mit  t)  Gen.  obj.,  ß)  Akk.;  von  (lUttem, uzw.  i)  von  Mazdäh:  b  a)  at  ^wä  minghl
13488:Zum  V.  nay-;  «i.  vgL  stnä-rä^,  NSm.  — 'däsnian-  n-,  s.  dasvar:  —  Pü, ;  dnisHA,  Sü. : laundatyam.  —  >)  Nach  den  abgeleiteten  r- Slämmen.
13496:KompA.  —  PPfP.  einer  aj.  Basis  dai-;  S  TOg. 7  No.  II.  —  np.  däit');  vgl.  mp.  däi'l;  ksl. daiä  'finden',  vgl.  an.  taia,  got.  leian ;  s.  noch zu  daia-.  —  Pü.:  iart\t.  —  0  Da»  als  PPfP. zum  Praes.  därad  dient.  Vgl.  j.  däilayänay- Und  vindat . .  yäiam,  p.  däraytrvi^us  und  ai. jödädvasuh ;  s.  nach  No.  a.  —  ')  Vr.  ig.  2, S.  Pü.  zu  'dä%ra:  mp.jiän  das  ist  etwa  sva.  mit,/ vindUn;  vgl.  däslayänay-.  —  J)  Vermutlich verkehrte  Umsetzung  des  Ideogramms  fatgn/i.
13497:•  j.  dä^'yänay-  m.  EN.  eines  Ungläu* bigen,  dessen  Söhne  Kimäspa  erschlägt' " : k3nsSsp>tn  . .  yS  janat . .  huttavoica  •nsis Yt.  75.41.
13498:Ejg.  'der  Gunslbeweise  (der  Götter)  erhallen hat';  *yänixy-  f.  sva.  j'öjia.«).  —  ')  Nach  JusTi NB.  8Ö  vielmehr  patton.  Adj.,  Ableit.  aus *°yäna- ;  s.  No.  a.  —  »)  Vgl.  ai,  jyänay-  f. neben  ^^ÖHo-  n.,  j.  VAi«a)-- m,  neben  "j/äna  n.
13603:•  g.  d^nay-  Adj.:  s.  unter  'äämay.
13818:•  j.  dui£-anay-  Adj.  'der  einen  üblen  Atem, d.  i.  Geruch  hat' :  macirinam  artukanam  . . 'aininqm  V.  14.  5-
```


## [2026-09-07T18:25:34.854Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"V\\.  *nay-\\|des V. nay\\|zum V. nay\" BRT.txt | head\necho \"---- search 'führen' near n headwords ----\"\ngrep -n \"^\\s*•\\s*[jgp]\\.\\s*\\(nay\\|näy\\|nai\\)\" BRT.txt | head\necho \"---- col 1049-1052 ----\"\ngrep -n \"^1049$\\|^1050$\\|^1051$\\|^1052$\" BRT.txt | head"
}
```


### [2026-09-07T18:25:36.140Z] TOOL RESULT

```
13488:Zum  V.  nay-;  «i.  vgL  stnä-rä^,  NSm.  — 'däsnian-  n-,  s.  dasvar:  —  Pü, ;  dnisHA,  Sü. : laundatyam.  —  >)  Nach  den  abgeleiteten  r- Slämmen.
---- search 'führen' near n headwords ----
18451:•  p.  naiy  neg.  Part:  s.  unter  nfft/.
18452:•  j.  nai°,  nur  in  (alten)  Verbindungen mit  enkl.  Part  und  Pron.,  neg.  Part  'nicht'.
18716:•  j.  naircmanah-  Adj,  'mannhaften  Sinns' : °ni  ktnsäsps  Y.  g.  11,  Yt.  j.  37,  1$.  aj, ip-3^,  44*-
18729:•  j.  nairya-  Adj.  (fem.  'ryä-)  'virilis'; i)  'männlichen  Geschlechts';  a)  von  Men- schen; dva  nara  us.eayeirtie  mHwana (sd.)  strica  'ryasca  V.  2.  41 ;  —  yezi  °ryS afihat  ..yezi  strJ  atshat  V.S.  $S;  —  däya ml  .  .  'ryqm  3snqm  */razaintlm  \.6S.$;
18732:•  j.  nairyö.näman-Adj.  '(mit  männlichem
18734:•  j.  nairy5,saoha-'>  m.  Name  einer  Gott- heit {Yazata),  die  des  Götterbotenamts waltet;  *'hs'^  ..  astö  mazdä  ahurahe  "J^., der  Bote  des  AhM^  V.  ;p.  34;  34;  — nairyS.sarjAs  (statt  Dat )  aocayata  yS  dmva ahurS  masdh:  nairya  sartha  '*  vyHxana  . . imal  saiihsil  airyamanai  V.  22.  7;  13;  — sraosasca  ,  .  °hasca  yd  mayu^{sA.)  Yt  10. 5a;  —  apqm  naptärsm  . .  nairim  sanfum  '> Y.  77.  23;  —  sraohm  ..  nairimca  saa/ifin'^ huraohm  Y.  57.  3,  Vyt^o;  Vr.  7.  i;  — sraolake  ,  .  nairyeheca  sat?haAe'^  Vr.  is. 16;  — yqmca  (räml.  Jrava/lm)  srao/aAe ..yqmca  nairyeAe  saaAaAe'^  Yty.Sj;  — Xfa%r»n.nafolrfm  "Atm  yazattm  Y.  77. 1 1 ;
18753:•  j.  nairyf^niJii^.vänti'vant-  Adj.  'der ' mannhafte  Tapferkeit  besitzt*;  tir7zSJa-\ man^m  Tantum  taxtnpm  Yt.  ig.  42.
19112:•  j.  nainöjtäa*ra-  Adj,  -  ?  -,  unter  den  "i«  gf-  ">'f  "  ">"';  »gl-  B=*»-  GrCr.i  177 Namen  AhM.%:    'rö  nama    aAmi   namd.- 1     "^^  "-'^'**-
28364:•  p.  naiy   "Sakaurim    naiy   ^^"huvalam züra''  (sd.)  akunavaiu  Bh.  4. 1 3.
30480:•  p.  naiy  "saiaurim  naty  •»  "huvatam'' züra*  (sd.)  akunavam  Bh.  4.13.
---- col 1049-1052 ----
18678:1049
18681:1050
```


## [2026-09-07T18:25:41.061Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '18575,18615p' BRT.txt"
}
```


### [2026-09-07T18:25:41.108Z] TOOL RESULT

```
j.  m>/>ir- :  I.  unter  nafä/..
dby  Google
I04I  naohuämant-  -
g.  ttafhi-lä :  s,  anter  nafit-.
•  j.  naehui'mant-  m,  Name  eines  Bergs
oderGehiTgs:  aAmaj  Aa/a  ffaraysß-aäx^an .  .  säirivas^a  "masca  Y(.  ig.  4,
Eig.  Bed,?  ~    'TiaaAm-  (=—  ar.  *nasul-  oder
•  ].,  g.  Dana  Adv.  i)  'an  einem  besondem Ort,  abgesondert';  yJ  dät  ntanS  vahyS mazda  asyascä  .  .  %waAinl  xratä  apsmim °nä  aahat  "wer  sein  Denken  (jetzt)  besser macht  und  (jetzt)  schlechter  ,  .,  der  wird nach  deinem  Ratschluss  zuletzt  abgesondert sein"  Y,  48. 4''.  z)  'an  mehreren  ver- schiedenen Orten',  attrib.  sva,  'verschiedene, mehrere';  nabänazdists  aat  kavatqm  'na yahmi  "parftili  ". .,  aber  von  mehreren einander  gleichstehenden  der,  bei  dem  er den  Einwand  erhebt"  N.  79;  —  naba- nazdistfm  ,  .  äat  *havatqm  *°na''>  aihra- paittm  ", .,  aber  von  mehreren  einander gleichstehenden  den  Lehrer"  N.5J'.
KompA.  —  ai.  nänä  Adv.;  s.  daiu  BtHU IF.  10.  10,  12.  116.  —  Pa.  (in  N.)r  ^«/(?,  IF. 12.  1 1 7),  (m  V.) :  vtart  u  ian  «.  —  i)  Zuletzt  zSt. IF./2.  117.— ')  Hd».  aba,  s,  aber  Pü.  —  3)  IF. 12.  115.  —  *)  Weil  man  das  Wort  mit  Harim narlm  V.  JO.  Z  in  BeziehuDg  brachte.
•  j.  nana'rlstay-  m.  EN.  eines  Gläubigen: Uois  paisatat3h5  ai'aonS  Yt  13. 115,
Eig.  'da  und  dort  Sorge  tr^end';  "tastay-  f., .™  V.  rld-  (S  51  II),  ..  in  räl... j.  natalima  N,  86:  lies  tii  nUima.
•  j.,  g.namV,'sich(weg)beugen'.  Praes.3 tuma-,  3  °nma-,  4  näma-,  30  (Kaus.)  »3- maya-.  —  PPfP.  *'nala-;  Inf.  nsinSi.
parö  a^rlf  baoh^  dürSt  tumaiii  Vyt 5/(?).         S.  noch  Inf.
mit  apa  'entfliehen,  weichen  von  —  weg' (Abi.  mit  ha^ä):  paoirXm  i^annS  apani- mata  .  .  yimat  kaca  Yt  J^.  35.
mit^a  i)  'fliehen',  absolut:  /ränämailt . .  artrS  mainyul  Yt/p.gö.  a)  'fliehen vor  -'  (.pars  mit  Abi.,  Lok.):  hö  nöit taritS  *franämaite^^  .  ,  parS  dafvatibyö Y.57. 18;  — frä  akmat  parB  vlspe  daiva tarita  tumanle^.sy.i&,'^t.f).n{wQn3m/irite); — yä^a  assm  mit tarÜS  fra.nmäne .. pat daSvalibyS  Yt.5.4;  —  a?iu pars fränämaiU alsmö'VLit).')^.  3)  Kaus. 'niederbeugen, eindiiicken':  frS  *parst)m  nSmayänti  .  . ßättayänti  (sd.)  Yt.  14. 56.  Undeutlich ; yat  */ranata'^  bun  N.Ö5.
mit  VI  'sich  auseinander  tun,  -ziehen, -dehnen':  ärmaite  fraca  üia  vlla  mmataka
nay-  1043
harShre  pasvqmla  . .  "Arm.,  geh  vorwärts und  tu  dich  auseinander,  um  tragen  zu können  .  ."  V.  2. 10.  a)  Kaus.  'aus- einander treiben,  sprengen':  fravasayS  .  . yi  rasmanS  .  .  vf  ma&iyqmtn   namayeinti
Yty.39-
ai.  nämate,  nämaya'i;  naiah,  ni-näme;  mp. fra-nämilan  (usw.;  s.  Pü-V  -  Pö.  (lu  V.  57)- änäniT/an,  (la  V.  i):  awnämilanS.  ~  1)  Pt4; s.  daj  folg.  mmanle.  —  ')  So  T,  Ausg.  'Hl/a. Pä.:  fehlt  —  3)  Das  .i  darin  ist  Dach  /"J:.- Manier  mit  ^  dargestellt.
•  *iiainra-vak-"  Adj.  'ehrerbietige  Worte sprechend':  'växs  F.je,
Adj.;  np,  nanu  'sintl,  weich'.  —  Pü.:  ä/^i grwiln,  —  I)  Hds.  namnra'.
•  i->  K-.  P-  oay-  V.  'leiten'.  Praes.  2 naya-,  3  nya- '',  1 7  (FuL)  naSiya-;  j-Aor.  i
i)  'Jemanden  leiten,  führen':  darisa  nä pairyaQxtaca  . .  ^nyete  usianavaitli'  vTspä /rasutfiain/ (sd.)  P.jÄ  a)  ["hinführen, hinbringen  zu  —'  (abiy  mit  Akk.):  Äauv {ih''d'laxinam  agarbäye^  anayi^  abiy  mSm Bh.2. 14;  5.1;  —  fravartis  .  .  anayatä (in  pass,  Sbn)  abiy  mim  Bh.2.  13;  — hatev ,.  baitJ*  *anayaiä  (pass.)''  abiy  mäm Bh,  1. 17.  3)  'wegführen,  wegbringen':
*astB.vj%Stus  dim  bandayäti  vayö  dim batUm  nayeiti  V.  5. 8 ;  —  sp3n>m  *naisyuti FrB.(?).  a)  mit  Angabe  des  wohin? durch  Akk. :  tsm  *vä  ahum  dngvantB  syao- %anaU  c^äii  dama  nalsat  (Konj.)^'  "zu solchem  Leben  (aber)  wird  euch,  ihr  Drug- genossen,  ob  eurer  Taten  das  eigne  Ich führen"  Y.j/.  20.
mit  ava  i)  'Jemanden  herabfUhren, ■holen  von  —  her,  aus  — '  {haca  mitlnstr.): avanayeni  spmt>m  mainyBm  kaca  . .  *garö nmäna  Yt  75.44.  2)  absolut  'reissen', \omVi 3SStT :  rat)hqm  *avajtayHntTm''^"dit reissende  R."  P.J"^.
mit  upa  'Jemand  herzufuhren':  ya%a  .. batidaymi  .  .  franrasyatam  . .  Uta  bashm upanayeni  Yt.i?.  18.
I  mit/i7i'j/(?}  und  3 'herzuführen, -bringen (lassen)': öwica/yJ  aspaisd^ patiyanayami^ Bh.7.  18.
mit  para  '(als  Beute?)  fortfllhren':  ime nS . .  aspa  para  *mihra  *ioa  nayenU  "die da  führen,  o  M.,  unsre  Rosse  hier  (als Beute?)  fort"  Yt70.42.
ai.  näyaH,  ni}at\  mp.  nUan.  —  PiL  (lu  Y.,  V.) :
ob,Google
»043
•nava-
■aos,  (ta  V-S^:  (eblt;  t.  «m^  >'<>.  4.  — '}  D.  L  iBya-,  $  36S.  II.  —  »)  Ansg.  hit äi«a>-<ia.  —  j)  V.  5,  öa.  wo  die  Stelle  tci- wendet  Lit,  steht  dafür  mjfriiayäl.  —  4)  Hds. tna  njfm^/im  (u>  nach  Blcm3iet  Lei.  95). Pä.:  /a  afe  *iia}J>iii.  —  i)  Do  Stein  lässl aar  noch  äßiajrum  erkemicn,  daTor  eine  Lacke. Vll.  besser  äHyäit'  »lau  patiyä'  in  lesen.
•  j.  'nava  Psut  'durchaus  nicht,  überhaupt nicht,  sicher  nicht,  keineswegs':  kä  filasti Li>af  ..tf  he  asii  ä^a  tf  ke  asti  äp^ntii iiC-it  kl  asti  yaotdairym  "Vas  ist  die  Sühne dafür?  .  .  Es  gibt  dafür  überhaupt  keine Sühne  .  ."  V.  j,  39;  —  yS  mqm  . .  dära- yeiä  yaia  täybm  pfssaärtm  n'  ahmt p>sS.- sUrö  ".  .  wie  einen  todsündigen  Dieb;  und ich  bin  doch  sicher  kein  Todsünder"  Y. //.  3;  —  tum  afi-a  ..  anaiivySstis  kunahi .  .  «•  as3m  .  .  anaiwyäsfil  kunämi  "ge- bierst du  denn  . .  ohne  Begattung?  . . Ich  getäie  keineswegs  ohne  Begattung" V.  /<V.  31;  —  yaf  . .  yu:rtanqm  . .  /ratjm?m '^anjayeni  (sd.)  .  .  *«'  */rä~i:w>nsäma  ** razunm  (sd.)  Yt.  5.  50;  l^.  ti  "'.  nava.- ci!  sbes.
KompA.  —  Komp. :  *nii'  +  ^vä  j  ar,  •nag^f , $  pa.  I.  —  ai.  »gL  nä  väi').  —  Pö,;  «.  - ■}  NA.  tua!a./rSk-,vfrisäm\  i.  aber  F  1  und S  296.  4.  —  1)  In  der  Bedeotnnc  'überhaupt nicht'  RV.  3.  33,  10,  to.  95.  15.
•  j.  'nava  Part  'oder  nicht';  u^»r»ptat paiti  draonät  (sd.)  «•  tagfnptäl  V.  5. 26;  a6'.
Ableit  —  Komp.:  •«a'  +  Ji»«;  ar.  'nauä, ip2.  t,  Bthi-  BB.  ij.  58'),  —  aL  Hfl  vä.'— Pu,:  ne.  —  >)  VgL  übrigens  daia  'ntna.
•  j.  ^nava  indekL''  Zw.  'neun':  ya^  Ai  'va (als  Nom.)  xsafna  lacantt  Y.g.  35,  ig.  23; i/i.  10,  1 1 ;  —  'va  (als  Akk.)  ptrüwS . . i^rmuFa  V.2.  ^o;  5.  $1,  ().ii,  ii.jaPüZ., 10.18,  14-14,  17-6',  /^.aiPüZ.,  22.ao', P.g,  Yt4-ö(?>,  /9.41;  —  °^'a  «/«  may^m'^ V.5,  54;  —  -zraÄ  yatkj  navaitisca  °vaca sata  'va^a  hatattra  navasSsea  (sd.)  batvqn y.22.3;  YL/j.  59;  —  'va^a  navaÜTm^a "99"  Yt5. 8a;  —  'va  sala  upäzananqm V.  ^,  15;  15;  —  'va  (als  Instr.)  satäts harta.cnanqni  V,  4.  9;  —  *°va  *sat-lts^^ hazannmla  Ytj.  120;  —  'va  (als  Dat) druJaiH  xsa^raaiyd  V.4.10  PuZ.(?);  —  1 'vaijqm  (Gen.)  aspatiqm  ar/ham  V.  22. , 30;  —  *m?nääidyäi  (sd.) . .  'va  dasmi  Y.
•11J114«.  \3lO. —  ')  Man  Tcilangte  den  Plnr. des  Sabst..«,  Tgl.  irJi-No.  3.  —  j>  N.\,  «iira.- jn/*.  —  4)  Dp.  u,  mp.  d  aas  ir.  a^c',  k  Tom ZaUvoct  für  10  iiiiA.
•  j.  *iiava  Adr.:  s.  nara-.
```


## [2026-09-07T18:25:57.036Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON نیل with sanskrit tag ===\"; grep -n \"سنس\" MON_part2.txt | grep \"نیل\" | head -5\necho \"=== MON نیلوفر ===\"; grep -n \"نیلوفر\" MON_part2.txt | head -5\necho \"=== SKT lilac/anil ===\"; grep -n \"^LILAC\\|^ANIL\\|^INDIGO\" SKT.txt | head\necho \"=== DEV lilas/anil ===\"; grep -n \"^LILAS\\|^ANIL\\|^INDIGO\" DEV.txt | head\necho \"=== PHN lilas/anil ===\"; grep -n \"^LILAS\\|^ANIL\\|^INDIGO\" PHN.txt | head\necho \"=== HJB neel ===\"; grep -n \"^NEEL\\|NEEL,\" HJB.txt | head"
}
```


### [2026-09-07T18:25:57.152Z] TOOL RESULT

```
=== MON نیل with sanskrit tag ===
=== MON نیلوفر ===
22847:گردن: برج عقرب. کژدم نیلوفری: برج 
33195:گل آب: (گیا.) یکی از گونه‌های نیلوفر آبی 
38723:صحرایی. (گیا.) لبلاب مصری. ( گیا.) نیلوفر 
38726:زیرا مراد از کلمة لبلاب انواع نیلوفر 
38727:صحرایی و نیلوفر باغی است که جزو تیرد 
=== SKT lilac/anil ===
=== DEV lilas/anil ===
=== PHN lilas/anil ===
=== HJB neel ===
15520:NEELQYE,  NILGHAU.
15529:NEELAM,  Ti'R'RTiAm,  s.  Hind. nUdTTif  from  Port,  leildo.  An  auction •or  public  outcry,  as  it  used  to  be -called  in  India  (corresponding  to •Scotch  roup;  comp.  Qerm.  rufenj  and 'Otitroop  of  Linschoten's  translator below).  The  word  is,  however,  Ori- •ental  in  origin,  for  Mr.  C.  P.  Brown <(MS.  notes)  points  out  that  the  Portu- gese word  IS  from  Ar.  i^ldm  (al'€ldm^
15538:NEELGTE,  NILGHAIJ,  &c.,  s. Hind,  nilgdu,  nilgdi,  lilgdl,  i.e.  *blue cow ' ;  the  popuhir  name  of  the  great antelope,  called  by  PaUas  Antilope tragocamelus  {Portax  pidus,  of  Jerdon, [Boselaphus  tvamcamelus  of  Blanford, MamTMdia,  517J),  given  from  the  slaty blue  which  is  its  predominant  colour. The  proper  Hind,  name  of  the  animal is  ra;A  (Skt  riiya^  or  rishyd),
```


## [2026-09-07T18:26:10.733Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== UNV ufar/ofar ===\"; grep -n -i \"ufar\\|ofar\\|nll\\|nil\" UNV.txt | head -12\necho \"=== WEB lilac/anil ===\"; grep -n \"^lilac\\|^anil\\b\\|^aniline\\|^anil \" WEB_vol1.txt | head\necho \"=== FSD anil ===\"; grep -n \"^anil\\b\\|^aniline\\|^lilac\" FSD_vol1.txt FSD_vol3.txt 2>/dev/null | head"
}
```


### [2026-09-07T18:26:10.844Z] TOOL RESULT

```
=== UNV ufar/ofar ===
442:evenlliä  cäsnth  u  röömand  ümis  i  str
444:aivsart  niliand  awsart  pa  pust  us  dahand
695:AA’örterbnchern  mit  'Laute’  und  mit  'Harfe’  bestimmt;  s.  PahlT.  113.  8.  17  (wozu Bthl.  IF.  57.  88).  —  ^  vin  'Laute’:  s.  arniLAA'.  vin.  Hbm.  AGr.  247.  —  ^  vin-liannär: nach  CSachs  Langhalslaute  mit  Straußeneikorpus:  s.  aram.  X^22.  —  “  mustaJ::  oh sva.  np.  'Faust’?  ]\Ian  kann  auf  der  Fau.st  (oder  vielmehr  den  beiden  Händen)
735:No.  10.  —  zen:  bedeutet  sonst  ‘IVaffe’  und  —  wie  das  np.  —  'Sattel’;  s. No,  10.  —  zang  'Glöckchen’,  s.  np.  arniLW,  zangak.  —  zil:  zu  türk.-kurd.
903:[z]  höd  ciyön  etö)i  höd  -  nllöpar  85.
931:85.  ^  Entlehnt  aus  ai.  nllotpala-:  np.  bei  Kosen  S.  27  'Wasserlilie*.
=== WEB lilac/anil ===
=== FSD anil ===
FSD_vol3.txt:50355:anil their conti'iits. when Identhiil in MiH.*cles - iliuii'o-
FSD_vol3.txt:50648:anil starM wnrn Ciods ClenweiH iuauhoe that ilmy were the
FSD_vol3.txt:72144:anil effereTii, motor and sensory, etc
FSD_vol3.txt:98049:anil Opieonsiria (Aug 'i.**) Ops Con-si'vaT.
FSD_vol3.txt:146177:lilac, crimson, or white nowers. ,
FSD_vol3.txt:149199:anil thn likn C W Hotbon Baamningo of CioUioa^
FSD_vol3.txt:153128:anil of ItH bed may be cultivated pl>nag't*
FSD_vol3.txt:162773:anil fruit, nuturullml In
FSD_vol3.txt:178001:anil a funiicl-shais'd oxpuiisloii (the wings) at the en-
FSD_vol3.txt:200576:anil 11 Htiiirt, cli>sel\ eiirled tiill fn’i|ucnll\ keiit us a |)et
```


## [2026-09-07T18:26:19.271Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('UNV.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(txt):\n    if 'nllöpar' in p or 'nllotpala' in p or 'nīlōpar' in p or 'nllöpar' in p or 'llotpala' in p or 'lopar' in p.lower():\n        print('=== leaf',i,'(printed ~',i-2,')')\n        for line in p.split('\\n'):\n            if 'lopar' in line.lower() or 'lotpala' in line.lower(): print('   >',line.strip()[:300])\nEOF"
}
```


### [2026-09-07T18:26:20.546Z] TOOL RESULT

```
=== leaf 37 (printed ~ 35 )
=== leaf 38 (printed ~ 36 )
   > 85.  ^  Entlehnt  aus  ai.  nllotpala-:  np.  bei  Kosen  S.  27  'Wasserlilie*.
```


## [2026-09-07T18:26:29.006Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('UNV.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=txt[37]\ni=p.lower().find('lopar')\nprint(p[max(0,i-600):i+300])\nEOF\nls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK | head"
}
```


### [2026-09-07T18:26:30.429Z] TOOL RESULT

```
wie  der  Duft  der  Mäd¬ chen.
76.  ^  s.  GrBd.  118.  7,  np.  entlehnt  aus  ai.  Icarpura-.  —  ^  Fehlt  in  den
Hss.;  s.  §  73,  No.  2.
77.  ^  JJ.  Name  einer  Pllanze  mit  weißen  und  ^^elben  (s.  §  78)  Blüten;  s. np.  ‘Jasmin,  weiße  Hagerose,  überh.  weiße  Rose’  (Zenkek).
7
100.png
101.png
102.png
103.png
104.png
105.png
106.png
108.png
109.png
110.png
```


## [2026-09-07T18:27:36.865Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^nainsook\" KLN_1971.txt KLN_1966.txt | head\npython3 - <<'EOF'\nfor f in ('KLN_1966.txt','KLN_1971.txt'):\n    txt=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    for i,p in enumerate(txt):\n        if 'nainsook' in p:\n            print(f,'leaf',i)\n            j=p.find('nainsook'); print(p[max(0,j-200):j+700].replace('\\n',' '))\n            break\nEOF"
}
```


### [2026-09-07T18:27:38.443Z] TOOL RESULT

```
KLN_1971.txt:158352:nainsook, n., a fine cotton fabric. — Hind, nain- 
KLN_1966.txt leaf 478
blue’,  which  is  of  un¬ certain  etymology.  It  possibly  derives  fr.  I.-E. Liliaceae base  *ni-,  ‘to  shine’.  See  neat,  adj.,  and  cp.  anil and  the  first  element  in  nilgai  and  in  nainsook. Derivative:  lilac ,  adj. Liliaceae,  n.  pi.,  the  lily  family  ( bot .)  —  ModL., formed  fr.  Li  limn  with  suff.  -aceae. liliaceous,  adj.  —  See  prec.  word  and  -aceous. Lilith,  n.,  a  female  evil  spirit.  —  Heb.  Lilith ,  fr. Akkad.  Lilitu  (whence  also  Syr.  Lelitha),  not  re¬ lated  to,  but  folk-etymologically  connected  with, Heb.  ldylah,  ‘night’,  and  explained  accordingly as  ‘night  demon’. Lilium,  n.,  a  genus  of  plants,  the  lily  (bot.)  —  L. lllium.  See  lily. Lilliputian,  adj.,  diminutive,  tiny.  —  Prop,  ‘per¬ taining  to  Lilliput’,  a  fabulous  island  with  inhab¬ itants  6  inches  high.  The  name  was  coined  by Swift
KLN_1971.txt leaf 0
,  indigo’, fr. OI. nflah , ‘dark blue’, which is of un-  certain etymology. It possibly derives fr. I.-E.  base *«?-, ‘to shine’. See neat, adj., and cp. anil  and the first element in nilgai and in nainsook.  Derivative: lilac, adj.   Liliaceae, n. pi., the lily family {bot.) — ModL.,  formed fr. Lilium with suff. -aceae.  liliaceous, adj. — See prec. word and -aceous.  Lilith, n., a female evil spirit. — Heb. Lilith , fr.  Akkad. Lilitu (whence also Syr. Lelitha), not re-  lated to, but folk-etymologically connected with,  Heb. ldyla h , ‘night’, and explained accordingly  as ‘night demon’.   Lilium, n., a genus of plants, the lily {bot.) — L.  lilium. See lily.   Lilliputian, adj., diminutive, tiny. — Prop, ‘per-  taining to Lillipuf, a fabulous island with inhab-  itants 6 inches high. The name was coined by  Swift in Gulliver's Travels (1726). For the ending  see suff. -ian.   Deri
```


## [2026-09-07T18:27:42.429Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '158350,158362p' KLN_1971.txt\necho \"=== leaf of nainsook in KLN_1966 ===\"\npython3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(txt):\n    if 'nainsook' in p and 'Hind' in p:\n        print('leaf',i); j=p.find('nainsook'); print(p[max(0,j-300):j+500].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T18:27:43.972Z] TOOL RESULT

```
Derivatives: nail-er , n., nail-ery, n., nail-ing, adj. 
nainsook, n., a fine cotton fabric. — Hind, nain- 
sukh , compounded of nain , ‘eye’, and sukh, 
‘pleasure’. The first element derives fr. OI. 
nayanam , ‘eye’, which is prob. a derivative of 
I.-E.bas e*ni-, ‘to shine’, whence possibly alsoOI. 
nflah, ‘blue, dark blue’; see lilac. The second 
element comes fr. OL sukhdfy, ‘ease, comfort, 
pleasure, enjoyment’. 

naive, naive, adj., natural, ingenuous, innocent, 
artless. — F. naive, fern, of naif \ fr. L. nativus, 
=== leaf of nainsook in KLN_1966 ===
leaf 549
  to  fasten  with  a  nail  or  nails.  —  ME. nailen,  fr.  OE.  nseglian,  fr.  nsegel,  ‘nail’;  rel.  to OS.  neglian,  ON.  negla ,  OHG.  negilen,  MHG. negelen,  nagelen,  G.  ndgeln,  Goth,  ganagljan,  ‘to nail’.  See  nail,  n. Derivatives:  nail-er,  n.,  nail-ery,  n.,  nail-ing,  adj. nainsook,  n.,  a  fine  cotton  fabric.  —  Hind,  nain- sukh,  compounded  of  nain,  ‘eye’,  and  sukh, ‘pleasure’.  The  first  element  derives  fr.  OI. nayanam,  ‘eye’,  which  is  prob.  a  derivative  of I.-E.base*n/-,  ‘to  shine’,  whence  possibly  alsoOI. nflab,  ‘blue,  dark  blue’;  see  lilac.  The  second element  comes  fr.  OI.  sukhah,  ‘ease,  comfort, pleasure,  enjoyment’. naive,  naive,  adj.,  natural,  ingenuous,  innocent, artless.  —  F.  naive,  fern,  of  naif  fr.
```


## [2026-09-07T18:27:50.750Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (524,525,526):\n    print('=== leaf',i,'~ pp.',2*(i-12),2*(i-12)+1)\n    print(txt[i][:600].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T18:27:52.153Z] TOOL RESULT

```
=== leaf 524 ~ pp. 1024 1025
,  ‘small’  (see  micro-),  and  E. -fy  (fr.  L.  -fiedre). micro-,  micr-,  combining  form  meaning  1)  small ; 2)  microscopic ;  3)  one  millionth  part  of  a  given unit  (as  e.g.  microgram  denotes  the  millionth part  of  a  gram).  —  Gk.  plxpo-,  plxp-,  fr. plxpo?,  ‘small’,  which  is  cogn.  with  L.  mica, ‘crumb’.  See  mica. microanalysis,  n.,  the  chemical  analysis  of  very small  quantities.  —  ModL.,  compounded  of micro-  and  analysis. microbarograph,  n.,  a  barograph  for  recording very  small  changes.  —  Compounded  of  micro- and  barograph. microbe,  
=== leaf 525 ~ pp. 1026 1027
ere  referred  to. midst,  n.  —  ME.  middest,  midest,  formed  with intensive  suff.  -t  fr.  middes,  mides,  adverbial  gen. of  mid.  See  mid,  adj.,  and  cp.  amid,  amidst. Cp.  also  against  and  words  there  referred to. Derivative:  midst,  prep. midsummer,  n.  —  ME.  midsumer,  midsomer,  fr. OE.  midsumor.  See  mid,  adj.,  and  summer, midwife,  n.  —  ME.  midwif,  fr.  OE.  mid,  with , and  wif,  ‘wife,  woman’.  The  first  element  is  rel. to  Goth,  mip,  ON.  med,  ‘with’,  and  cogn.  with Gk.  pcxi,  ‘between,  among,  with,  after’;  see meta-.  For  the  secon
=== leaf 526 ~ pp. 1028 1029
ilesian,  ‘Irish’, milk,  n.  —  ME.  melk,  milke,  fr.  OE.  meoluc, meolc,  mile,  rel.  to  OS.  miluk,  ON.  mjolk ,  Swed. and  Norw.  mjolk,  OFris.  melok ,  Dan.,  Du.  melk, OHG.  miluh,  MHG.,  G.  milch,  Goth,  miluks, ‘milk’,  OE.  melcan,  ON.  molka,  mjolka,  OFris. melka,  Du.  melken,  OHG.  melchan,  MHG.,  G. melken,  ‘to  milk’,  fr.  I.-E.  base  *melg-,  ‘to  press out,  to  wipe  off  milk’,  whence  also  Gk.  <&piX- ysiv,  ‘to  milk’.  Alb.  mjel',  miel',  ‘I  milk’,  L.  mul- gere,  ‘to  milk’,  OSlav.  mluzq,  mldsti,  Lith.  melzu, milzti,  ‘to  milk’,  Mir.  bli
```


## [2026-09-07T18:28:03.714Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"nayati\\|nayeiti\\|‘to lead’, whence\\|nItan\" KLN_1966.txt KLN_1971.txt | head -20"
}
```


### [2026-09-07T18:28:03.771Z] TOOL RESULT

```
KLN_1966.txt:24912:naik,  naique,  n.,  1)  a  title  of  honor;  2)  a  native non-commissioned  officer  in  the  British  India army.  —  Hind,  nayak,  fr.  OI.  ndyakah ,  ‘leader, chief,  general’,  fr.  ndyati ,  ‘leads',  which  is  rel.  to Avestic  nayeiti,  ‘leads’,  and  cogn.  with  Hitt. nai-,  ne-,  ‘to  guide,  lead’,  Mir.  ne,  nia,  ‘hero, warrior’.
KLN_1966.txt:25133:need,  tr.  v,,  to  want,  be  in  need  of;  intr.  v.,  to  be necessary.  —  ME.  neden,  needen,  fr.  OE.  neo- dian ,  ‘to  be  necessary’,  fr.  neod.  See  need,  n. needle,  n.  —  ME.  nedle ,  fr.  OE.  nSdl,  rel.  to  OS. nathla,  ON.  nal,  Swed.  nal,  Dan.  naal,  OFris. nedle,  OHG.  nadala,  nbdla,  MHG.  nadele,  na- del,  G.  Nadel ,  Goth,  nepla ,  and,  with  metathe¬ sis,  OFris.  nelde,  MLG.  nalde,  MDu.  nallde,  Du. naald,  ‘needle’  (Finn,  neula  and  nallo,  ‘needle’, are  Teut.  loan  words),  lit.  ‘a  tool  for  sewing’, formed  with  I.-E.  instrumental  suff.  *-tld  fr. l.-E.  base  *(s)ne-,  ‘to  spin,  to  sew  with  a  needle’, whence  MLG.  neien,  MDu.  naeyen,  Du.  naaien, OHG.  najan,  MHG.  mejen,  G.  nahen,  ‘to  sew’, OI.  snayati,  ‘wraps  up’,  snayuh,  ‘sinew’,  Gk. vsoj,  veiv,  ‘to  spin’,  v5jp.x,  ‘that  which  is  spun, thread’,  v7)-rpov,  ‘distaff’,  L.  ned,  nere,  ‘to  spin’, OSlav.  niti,  nista,  ‘thread’,  snujq,  snovati,  ‘to twist',  Lett,  sndte,  ‘a  linen  cover’,  OIr.  snathe , ‘thread’,  sndthat ,  ‘needle’,  W.  nyddu,  Co.  nethe, ‘to  sew",  OW.,  OBret.  notuid,  W.  nodwydd, ‘needle’.  Cp.  -nema,  nemato-,  nerve.  Cp.  also snood.
KLN_1966.txt:41187:with  OI.  vasndfi,  ‘purchase  money’,  vasndm, ‘reward’,  vasnayati,  ‘he  bargains,  haggles  ,  Arm. gin  (for  *wesnom),  ‘purchase  money’,  Gk.  uvr), &v op,  ‘price  paid  (for  a  thing),  purchase  ^Les¬ bian  8wa  (for  *wosna),  ‘purchase’,  Gk.  cbvEt- cr9-oa,  ‘to  buy’,  Hitt,  ushshaniya-,  ‘to  sell',  and —without  the  suff.  -no — wash-,  ‘to  buy’.  Cp. vend,  vendee,  vent,  ‘market’,  venta,  and  the  sec¬ ond  element  in  opsonin.
KLN_1971.txt:153977:cogn. with OI. manayati , ‘he considers, honors’, 
KLN_1971.txt:158315:Avestic nayeiti , ‘leads’, and cogn. with Hitt. 
KLN_1971.txt:159815:OI. snayati, ‘wraps up’, snayuh, ‘sinew’, Gk. 
KLN_1971.txt:259998:‘reward’, vasnayati, ‘he bargains, haggles’, Arm.
```


## [2026-09-07T18:28:18.824Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '158280,158420p' KLN_1971.txt | grep -n \"^[0-9]\\{3,4\\} *$\" \necho \"---\"; awk 'NR>=158200 && NR<=158500 && /^ *[0-9]{3,4} *$/ {print NR\": \"$0}' KLN_1971.txt"
}
```


### [2026-09-07T18:28:20.384Z] TOOL RESULT

```
---
158436: 487
```


## [2026-09-07T18:28:30.412Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(518,556):\n    nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$', txt[i])\n    hw=txt[i][:40].replace('\\n',' ')\n    print(i, nums, '|', hw)\nEOF"
}
```


### [2026-09-07T18:28:31.869Z] TOOL RESULT

```
518 ['966', '967'] |   subst. suff.  -ise. Derivative:  merch
519 ['968'] | ��  Gk.  pepo-,  pep-,  fr. pspos,  ‘par
520 ['970', '971'] | Xaox6g,  ‘bud,  sprout,  shoot’.  Meaorc
521 ['972'] |   metallurg-ist,  n. metamere,  n.,  one
522 ['974'] | n  entering the  earth’s  atmosphere.  —
523 ['976'] | pounded  of  metro-, ‘measure',  and  Gk
524 ['977', '978'] | ,  ‘small’  (see  micro-),  and  E. -fy 
525 ['979', '980'] | ere  referred  to. midst,  n.  —  ME.  m
526 [] | ilesian,  ‘Irish’, milk,  n.  —  ME.  me
527 [] | ter,  Swed.  mjelte,  ‘spleen’, Norw.  m
528 [] | OSlav.  mgknqti,  ‘to  be¬ come  soft’, 
529 ['986', '987'] |   and  cp.  the  first  element  in  mus
530 ['988', '989'] | able’,  which  is  of  uncertain  etymol
531 ['990', '991'] | — with  -/-forma¬ tive  element — OSlav.
532 ['992', '993'] | t  for  mob- cap. mobcap,  n.,  a  woman
533 ['994'] | edietatem, acc.  of  medietas,  ‘the  mi
534 [] | e  and  -ment  and  cp. movement.  For  
535 ['998', '999'] | ��  ME.  munec,  fr.  OE.  munuc  (whenc
536 ['1000'] | nd  L. nomen,  ‘name’ ;  see  mono-  and
537 ['1002', '1003'] |  named  after  Antoine-Fran- qois-Ernest
538 ['1004', '1005'] | rt,  of  mordre,  ‘to  bite’,  fr.  VL. 
539 ['1006', '1007'] | he  family  Nymphalidae  ( entomol .)  —
540 ['1008', '1009'] | odHeb.  mdshdbhah,  a  fem.  noun formed
541 ['1010'] | adj.  —  See  moldy. moulin,  n.,  a  ne
542 ['1011', '1012'] | ing  mucin  (biochem.)  —  Coined  fr.  
543 [] | ng  see  suff.  -ity. mull,  tr.  v.,  1
544 ['1015', '1016', '1017'] |  like  a  mummy,  to  dry  up,  shrivel.
545 [] | urrain’,  which  also  derive  fr. VL.  
546 ['1021'] | appoint,  something;  to  have  room; to
547 ['1022'] |   ;  see  man.  Peas¬ ants  were  called
548 [] | d  fr  prec.  word  with  suff.  -aceae.
549 [] | l  cured  of  leprosy  by  Elisha.  —  H
550 ['1028'] |  B  hem,  Hitt,  laman  (formed  with  d
551 [] |   of  coconut  shells, narial,  adj.,  p
552 ['1033'] | us,  ‘birth,  des¬ cent,  origin,  race,
553 ['1035'] | d  of  navis,  ‘ship’,  and agere,  ‘to 
554 ['1036'] | n.,  that  part  of  the  body  which  j
555 ['1039'] |  MF.  (=  F.)  negatif  (fern. negative)
```


## [2026-09-07T18:28:39.850Z] TOOL CALL #65: Bash

```json
{
 "command": "sed -n 1,120p /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-07T18:28:39.885Z] TOOL RESULT

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


## [2026-09-07T18:29:35.152Z] TOOL CALL #66: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/BOOK/356.png 2>/dev/null || (pdftoppm -f 356 -l 356 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf data/verification/sources/refs/ocr/BOOK/356 && ls -la data/verification/sources/refs/ocr/BOOK/356.png)"
}
```


### [2026-09-07T18:29:36.639Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 43469 Sep  7 14:29 data/verification/sources/refs/ocr/BOOK/356.png
```


## [2026-09-07T18:35:36.477Z] TOOL CALL #67: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-356.json",
 "content": "{\n  \"pdf_page\": 356,\n  \"book_page\": 326,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Nei 1, Ni 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *nei- / *neiə- : *nī- 'to be vividly moved, to be excited, to shine' (Pokorny 2. nei- , IEW 760)\",\n      \"note\": \"Pokorny p.760 carries exactly the two roots of this page, but numbered the other way round: '1. nei-, neiə-, nī- \\\"führen\\\"' and '2. nei-, neiə- : nī- \\\"lebhaft bewegt sein, erregt sein, glänzen\\\"'. Nourai's 'Nei 1, Ni 2 : to shine, to be excited' is Pokorny's nei-2 (his 'Nei 2 ... to lead' is Pokorny's nei-1), so the language label, the gloss and the page reference are all right and only the numbering is Nourai's own. Watkins/AHD carries the same root and, remarkably, the whole of this chart in one line: 'nei-. To be excited, shine. ... 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.]'. The solid material of the root is Latin niteō 'to shine', nitidus, Middle Irish níab, níam, Welsh nwyf, Old Persian naiba- / NP nēw 'beautiful, good', Old Irish noíb 'holy', Germanic *nīþa- 'envy, strife'; the Indic colour word nīla- on which this whole page hangs is attached to it only tentatively (see node #1), which is why every derivative below is 'possibly', not 'certainly', of Indo-European stock.\",\n      \"note_fa\": \"ریشهٔ هندواروپاییِ *nei- / *nī- «به‌جنبش‌درآمدن، برانگیخته‌شدن، درخشیدن» در پوکورنی (IEW) صفحهٔ ۷۶۰ آمده است، اما پوکورنی آن را «nei- شمارهٔ ۲» می‌نامد و «nei- شمارهٔ ۱» را به معنی «رهبری‌کردن» می‌گیرد؛ یعنی شماره‌گذاری نورایی وارونهٔ پوکورنی است، ولی برچسب زبان، معنی و شمارهٔ صفحه درست است. گواه‌های استوار این ریشه عبارت‌اند از لاتینی niteō «درخشیدن»، ایرلندی میانه níam «درخشش»، پارسی باستان naiba- و فارسی نو نیو/نَو «نیک، زیبا» و ژرمنی *nīþa-. اما «نیلِ» سنسکریت که تمام این نمودار بر آن استوار است، به گواهی خودِ پوکورنی «مشکوک» است. نتیجه: ادعای نورایی درباره خودِ ریشه درست است، ولی با احتیاطی که واتکینز نیز رعایت کرده («احتمالاً فارسی nil»).\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A5%80%E0%A4%B2\",\n        \"https://en.wiktionary.org/wiki/lilac\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:760\", \"status\": \"supports\", \"note\": \"Pokorny IEW p.760 (POK_02.txt \\\\f-leaf 422/423, German original): '2. nei-, neis- : ni- \\\"lebhaft bewegt sein, erregt sein, glänzen\\\"; noi-bho- \\\"gut, heilig\\\"; kelto-germ. nei-to-, ni-tu- \\\"Leidenschaft\\\". Lat. niteō, -ere \\\"glänze, strahle\\\" ... noi-bho- in apers. naiba-, npers. new \\\"schön, gut\\\" ... zweifelhaft ai. nila- \\\"schwarzblau\\\"'. Exactly Nourai's root, gloss and page.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II p.321 (WLD_Bd2_pages.txt leaf 326)\", \"stance\": \"partial\", \"note\": \"'2. nei- \\\"glänzen\\\". Lat. niteo, -ere \\\"glänzen\\\", nitidus ... *noi-bho- in ap. naiba-, np. new \\\"schön, gut\\\", air. noib \\\"heilig\\\"' — the root as such is confirmed, but Walde-Pokorny lists no Indic nīla- under it at all; the doubtful Sanskrit attachment is Pokorny's later addition.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. nei-\", \"stance\": \"supports\", \"note\": \"'nei-. To be excited, shine. 1. Suffixed form *nei-to- in Germanic *nitha- ... 2. Suffixed zero-grade form *ni-to- in Latin nitere, to shine: NEAT, (NET). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.]'\"},\n        {\"src\": \"KLN\", \"where\": \"vol. II p.1026 s.v. nainsook (KLN_1966.txt leaf 549)\", \"stance\": \"supports\", \"note\": \"'OI. nayanam, \\\"eye\\\", which is prob. a derivative of I.-E. base *nī-, \\\"to shine\\\", whence possibly also OI. nīlah, \\\"blue, dark blue\\\"; see lilac.' Klein's *nī- 'to shine' is Nourai's root, with the same 'possibly' about the colour word.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.v. nei- (IEC.txt lines 11580-11599)\", \"stance\": \"silent\", \"note\": \"Mann lists nei- 'neither, nor', nei- 'down' and neið (1) 'lead, send', but has no entry for a root nei- 'shine/be excited' — the 'shine' root is not part of his inventory.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"nili, nilah; nîlotpala\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The words are all real: Sanskrit नील nīla- (nom. sg. nīlaḥ) 'dark blue, blue-black' (already Vedic, AV, as a colour adjective), fem. नीली nīlī 'the indigo plant, indigo dye' (Nourai's 'nili'), and the compound नीलोत्पल nīlotpala- 'blue lotus' = nīla- + utpala- 'lotus, water-lily'. What is not certain is the arrow from the root: Pokorny puts nīla- into 2. nei- only with an explicit warning — 'zweifelhaft ai. nila- \\\"schwarzblau\\\", nayanā- \\\"Auge\\\", netra- ds.' (IEW 760) — and Walde-Pokorny II 321 does not have it under the root at all. Klein calls nīlaḥ 'of uncertain etymology. It possibly derives fr. I.-E. base *nī-, \\\"to shine\\\"', Watkins writes 'Possibly Persian nil', and Wiktionary 'Possibly from Proto-Indo-European *neyH- (\\\"to be excited, shine\\\"), i.e. \\\"the shining colour\\\"'. Lokotsch (no. 1568) takes the word quite differently, from *nihlas 'black as night' and hence the same word as Latin niger. So: real words, correct glosses, but a derivation that the sources accept only as a possibility — 'plausible', not 'confirmed'.\",\n          \"derivation_fa\": \"هر سه واژه واقعی‌اند: سنسکریت नील (nīla-) «آبی تیره، لاجوردی» (از دورهٔ وِدایی)، مؤنث नीली (nīlī) «گیاه و رنگِ نیل» (همان «nili» نورایی) و ترکیبِ नीलोत्पल (nīlotpala-) «نیلوفر آبی» از nīla- + utpala- «لوتوس». اما پیوندِ این واژه‌ها با ریشهٔ هندواروپایی *nei- «درخشیدن» قطعی نیست: خودِ پوکورنی آن را «مشکوک» (zweifelhaft) خوانده، والده‌پوکورنی (ج۲ ص۳۲۱) اصلاً آن را زیر این ریشه نیاورده، کلاین می‌نویسد «ریشه‌شناسی‌اش نامعلوم است؛ شاید از ریشهٔ *nī- «درخشیدن»»، و ویکی‌واژه هم «احتمالاً از *neyH- به معنی درخشیدن، یعنی رنگِ درخشان». در برابر، لوکوچ آن را از *nihlas «سیاه چون شب» و هم‌ریشهٔ niger لاتینی می‌داند. پس ادعای نورایی «با احتیاط پذیرفتنی است».\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A5%80%E0%A4%B2\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:760\", \"status\": \"partial\", \"note\": \"Pokorny p.760 does name the word, but with a caveat: 'zweifelhaft ai. nila- \\\"schwarzblau\\\", nayanā- n. f. \\\"Auge\\\", netra- n. ds.' (POK_02.txt, end of leaf 422). It supports the arrow only as a doubtful possibility, and it says nothing about nīlotpala-.\"},\n            {\"ref\": \"UNV:51\", \"status\": \"supports\", \"note\": \"Unvala, King Husrav and his Boy: the glossary/commentary note to §85 (UNV.txt \\\\f-leaf 37-38 of the local copy) reads 'nīlōpar 85. ... Entlehnt aus ai. nīlotpala-: np. bei Rosen S. 27 \\\"Wasserlilie\\\"' — i.e. exactly Nourai's Sanskrit nīlotpala 'blue lotus' with its Middle Persian borrowing. The passage sits on p.~35-36 of the copy on disk, not p.51; refs_online.json warns that the pagination of the 1963 edition differs from the one Nourai used, so the substance, not the page, is what checks out.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II p.321 (leaf 326)\", \"stance\": \"silent\", \"note\": \"Under '2. nei- \\\"glänzen\\\"' Walde-Pokorny list only Latin, Celtic, Iranian and Germanic material; ai. nīla- is absent — grep of the leaf for 'nila' finds nothing.\"},\n            {\"src\": \"KLN\", \"where\": \"vol. I p.895 s.v. lilac / vol. II p.1026 s.v. nainsook\", \"stance\": \"partial\", \"note\": \"'fr. OI. nīlah, \\\"dark blue\\\", which is of uncertain etymology. It possibly derives fr. I.-E. base *nī-, \\\"to shine\\\"' (lilac); 'whence possibly also OI. nīlah' (nainsook).\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nei-\", \"stance\": \"partial\", \"note\": \"'3. Possibly Persian nil, indigo: ANIL, LILAC' — Watkins does not even commit to the Sanskrit stage, only to the Persian word.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1568 (LKT.txt line 3603)\", \"stance\": \"contradicts\", \"note\": \"Lokotsch derives the Indic word from a 'black as the night' notion: 'nīlas < *nihlas *nihras, also dasselbe Wort wie lat. niger < *niher', i.e. from the 'black' root, not from *nei- 'shine'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"nîl «نیل ، نیلوفر ، نیلپَر ، نیلفَر ، نیله»; lîlak «لیلک»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian نیل nīl 'indigo (dye and plant)' comes from Middle Persian nīl (Pahlavi 𐭭𐭩𐭫), itself borrowed from Sanskrit nīla- 'dark blue' with the Indian long ī kept unchanged and the final -a lost as in every MP borrowing of an Indic a-stem; the variant نیله nīla keeps that final vowel, and Mo'in's footnote in Borhan-e Qāṭeʿ p.2231 states it flatly: 'نیله ... از سانسکریت nīla، معرّبِ آن از فارسی «لیلج»'. نیلوفر nīlūfar 'water-lily, lotus' is Sanskrit नीलोत्पल nīlotpala- 'blue lotus' via Middle Persian nīlōpal/nīlōpar (Unvala's King Husrav §85 nīlōpar), with the Middle-Iranian dissimilation of the second l to r and the ordinary NP lenition p > f; نیلفر nīlfar is its syncopated doublet and نیلپَر nīl-par a Persian folk reshaping as 'blue petal/wing' (Borhan p.2231 note 4: 'نیلفر < نیلوفر'). لیلک līlak is نیل + the adjectival-diminutive suffix -ak, i.e. *nīlak 'bluish', with the initial n dissimilated to l before the second l — Klein states this in so many words ('fr. Pers. lilak, var. of nilak, \\\"bluish\\\", fr. nil, \\\"blue, indigo\\\"'), Wiktionary's tree gives 'Classical Persian نیل + ـَک > لِیلَک (līlak)', and the same n/l wobble is visible in Hind. nīlgāu ~ lilgāī (Hobson-Jobson s.v. NEELGYE). The Farrokhī Sīstānī verse in the box ('برآمد نیلگون ابری ز روی نیلگون دریا') is quoted from that very page of Borhan.\",\n          \"derivation_fa\": \"«نیل» فارسی نو از فارسی میانهٔ nīl و آن وام‌واژه‌ای است از سنسکریت nīla- «آبی تیره»؛ ایِ کشیدهٔ هندی دست‌نخورده مانده و ‑a پایانی، چنان‌که در همهٔ وام‌واژه‌های هندیِ فارسی میانه، افتاده است؛ گونهٔ «نیله» همان مصوت پایانی را نگاه داشته و معین در حاشیهٔ برهان قاطع (ص ۲۲۳۱) صریح می‌نویسد: «نیله ... از سانسکریت nīla، معرّبِ آن از فارسی لیلج». «نیلوفر» از سنسکریت nīlotpala «نیلوفر آبی» است که از راه فارسی میانهٔ nīlōpal/nīlōpar آمده (اونوالا، خسرو و ریدک، بند ۸۵: nīlōpar)، با ناهمگونیِ ل دوم به ر و نرم‌شدن p به f؛ «نیلفر» گونهٔ کوتاه‌شدهٔ آن و «نیلپَر» ریشه‌شناسی عامیانه («پرِ نیلی») است. «لیلک» همان نیل + پسوند ‑َک (*نیلک «نیلی‌رنگ») است که در آن ن آغازین به سبب ل بعدی به ل بدل شده (ابدال/ناهمگونی)؛ کلاین و ویکی‌واژه هر دو همین را می‌گویند و همین نوسانِ ن/ل در nīlgāu ~ lilgāī هندی هم دیده می‌شود. بیت فرخی سیستانی نیز از همان صفحهٔ برهان نقل شده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D9%84\",\n            \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D9%84%D9%88%D9%81%D8%B1\",\n            \"https://en.wiktionary.org/wiki/lilac\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2231\", \"status\": \"supports\", \"note\": \"Borhan-e Qāṭeʿ p.2231 = BQT_v4_pages.txt pdf page 314 (printed = pdf + 1917). The page has the headwords نیلفر، نیلج، نیل‌خم آسمان، نیلگون and, in Mo'in's footnotes: 'نیله (هم.). از سانسکریت nīla، معرّب آن از فارسی «لیلج» ... (رك: لوفر)'; '۴ - نیلفر < نیلوفر (ه.م.)'; 'نیلج - معرب نیله است که به نیل مشهور است'; 'نیلگون - بکسر اول؛ از: نیل (ه.م.) + گون؛ برنگ نیل، آبی' followed by the same Farrokhī verse Nourai prints, 'برآمد نیلگون ابری ز روی نیلگون دریا / چو رای عاشقان گردان چو طبع بیدلان شیدا. «فرخی سیستانی. دیوان ص ۲»'. The cited page is exactly where Nourai's Persian box comes from.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, s.v. (النيل) — AFM_pages.txt leaf 156\", \"stance\": \"supports\", \"note\": \"'(النيل) نبات العظلم يصبغ به أزرق، فارسيته نيل وهو مشتق من نيلى ... بالسنسكريت أي أزرق، ولعصيره يقال نيله بالفارسية ومنه أنيلج' — Persian nīl from Sanskrit, and the Persian derivative نیله; the following entry adds 'ومنه الفارسي نیلوفر'.\"},\n            {\"src\": \"KLN\", \"where\": \"vol. I p.895 s.v. lilac\", \"stance\": \"supports\", \"note\": \"'fr. Pers. lilak, var. of nilak, \\\"bluish\\\", fr. nil, \\\"blue, indigo\\\", fr. OI. nilah, \\\"dark blue\\\"' — the nīl > nīlak > līlak step exactly as drawn.\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. NEELGYE, NILGHAU\", \"stance\": \"supports\", \"note\": \"'Hind. nilgau, nilgai, lilgai, i.e. \\\"blue cow\\\"' — an independent witness that Indo-Persian nīl- readily dissimilates to līl-, the change assumed for nīlak > līlak.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1568\", \"stance\": \"supports\", \"note\": \"'ebenso pers. nīlā \\\"Indigo\\\", ar. nīla \\\"dass.\\\"' — Lokotsch has the same Persian word (though a different ultimate origin for the Indic form).\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"laylak\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic لِيلَك līlak, also لَيْلَك laylak 'lilac, Syringa vulgaris', is a borrowing of Persian لیلک līlak; the Persian long ī is rendered in Arabic both as ī and, in the commoner popular form, as the diphthong ay (whence Ottoman/Turkish leylâk), which is why Nourai prints laylak and Klein gives both: 'Arab. lāylak, lilak, fr. Pers. lilak'. Lokotsch's entry no. 1319 is headed 'Ar. lilak: auch lailak [aus pers. līlāg, nīlāg]'. Semantically the word travelled with the shrub, which is native to the Balkans/Anatolia but whose Persian name (the 'bluish' one) followed the flower's pale violet colour; from Arabic-speaking (and then Ottoman) intermediaries it reached the Iberian peninsula and, in the 1560s, western Europe.\",\n          \"derivation_fa\": \"عربی «لِیلَك / لَیْلَك» به معنی یاس بنفش (Syringa vulgaris) وام‌واژه‌ای است از «لیلکِ» فارسی؛ ایِ کشیدهٔ فارسی در عربی هم ī و هم ـ در صورت عامیانه‌تر ـ مصوت مرکب ay بازنمایی می‌شود (از همین‌جا leylâk ترکی)، و از این‌رو نورایی صورت laylak را آورده و کلاین هر دو را: «عربی lāylak، lilak از فارسی lilak». لوکوچ نیز در شمارهٔ ۱۳۱۹ می‌نویسد «عربی lilak، همچنین lailak، از فارسی līlāg، nīlāg». این گره درست است؛ تنها یادآوری آنکه این گره در کتاب هیچ ارجاعی ندارد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/lilac\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"the book gives no refs= for this node; the claim is checked against Klein, Lokotsch and Wiktionary under 'consulted'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"vol. I p.895 s.v. lilac\", \"stance\": \"supports\", \"note\": \"'MF., fr. Sp. lilac, fr. Arab. lāylak, lilak, fr. Pers. lilak' — both Arabic vocalisations, and the Persian donor.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1319 (LKT.txt line 3070)\", \"stance\": \"supports\", \"note\": \"'Ar. lilak: Auch lailak [aus pers. līlāg, nīlāg, s. hier Nr. 1568] \\\"Syringa vulgaris, spanischer Flieder\\\" ... daher hieraus rum. liliac \\\"Flieder\\\" ... it. sp. lilac, frz. lilas ... engl. lilac.'\"},\n            {\"src\": \"WEB/Etymonline\", \"where\": \"etymonline.com/word/lilac\", \"stance\": \"contradicts\", \"note\": \"Etymonline is the dissenter: 'with French lilac, Spanish lilac from Turkish leylak (the tree reached Western Europe via Istanbul), perhaps from a native Balkan name' — i.e. Turkish, not Arabic, as the immediate donor, and no certainty about the Persian origin. The majority (Klein, Lokotsch, AHD, Wiktionary) keeps the Arabic-from-Persian route.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Spanish\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Empty pass-through box = Spanish lilac (modern lila) 'lilac', the Iberian form of the Arabic word and the one from which the plant name spread into the other Romance languages. Klein routes English lilac through it explicitly ('MF., fr. Sp. lilac, fr. Arab. lāylak'), and Lokotsch lists 'it. sp. lilac' beside 'frz. lilas' among the descendants of Arabic lilak. Wiktionary's tree omits the Spanish stage and takes obsolete French lilac straight from Arabic; nothing in the chart is wrong either way, since the Spanish and French forms are identical in shape.\",\n          \"derivation_fa\": \"این جعبهٔ تهی نمایندهٔ lilac اسپانیایی (امروز lila) است، صورتِ ایبریایی واژهٔ عربی و همان صورتی که نام این گیاه از آن به دیگر زبان‌های رومی رفته است. کلاین راهِ انگلیسی را صریحاً از همین‌جا می‌برد («از فرانسویِ میانه، از اسپانیایی lilac، از عربی lāylak») و لوکوچ نیز در فهرست بازماندگانِ lilak عربی «it. sp. lilac» را در کنار «frz. lilas» آورده است. ویکی‌واژه مرحلهٔ اسپانیایی را حذف می‌کند و lilac فرانسویِ کهن را یک‌سره از عربی می‌گیرد؛ چون شکلِ اسپانیایی و فرانسوی یکی است، هیچ‌یک از دو نمودار نادرست نمی‌شود.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/lilac\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"no refs= on this node in the book.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"vol. I p.895 s.v. lilac\", \"stance\": \"supports\", \"note\": \"'MF., fr. Sp. lilac, fr. Arab. lāylak, lilak'.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1319\", \"stance\": \"supports\", \"note\": \"'it. sp. lilac, frz. lilas' listed among the European reflexes of Arabic lilak.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Empty pass-through box = French lilac, the now obsolete 16th-17th c. form of modern lilas. The shrub itself reached western Europe from Istanbul about 1560 (with Busbecq's plant consignments), and the name came with it in the Ibero-Romance shape lilac; the French final -c was later replaced by -s (lilas), a change of the ordinary sort in French plant names. This is the form English borrowed in the 1590s, and it is what both Klein ('MF.') and Wiktionary ('From obsolete French lilac (now lilas)') give.\",\n          \"derivation_fa\": \"جعبهٔ تهیِ گذری همان lilac فرانسوی است، صورتِ متروکِ سده‌های ۱۶ و ۱۷ که امروز lilas شده است. خودِ درختچه در حدود ۱۵۶۰ از استانبول به اروپای باختری رسید و نامش نیز در همان قالبِ ایبریایی‌رومیِ lilac همراه آن آمد؛ سپس ‑c پایانی در فرانسوی به ‑s بدل شد (lilas). انگلیسی در دههٔ ۱۵۹۰ همین صورت را وام گرفت؛ کلاین («فرانسویِ میانه») و ویکی‌واژه («از فرانسویِ متروک lilac، امروز lilas») هر دو همین را می‌گویند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/lilac\",\n            \"https://www.etymonline.com/word/lilac\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"no refs= on this node in the book.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"vol. I p.895 s.v. lilac\", \"stance\": \"supports\", \"note\": \"English lilac 'MF., fr. Sp. lilac' — Middle French is the immediate donor, as drawn.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1319\", \"stance\": \"supports\", \"note\": \"'frz. lilas' among the reflexes; 'dtsch. lila \\\"bläulich\\\", engl. lilac \\\"Flieder\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"lilac\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English lilac, first recorded in the 1590s as the name of the shrub (colour sense 1791, adjective 'pale pinkish-purple' 1801), from French lilac. The Oriental origin of the word is the standard view: Klein takes it back through Spanish and Arabic to Persian lilak/nilak 'bluish' from nil 'indigo', and Watkins puts LILAC (with ANIL) under the IE root nei- 'to be excited, shine' precisely via 'Persian nil'. Etymonline is the one dissenting voice, making Turkish leylak the donor of the Romance forms and suspecting 'a native Balkan name' behind it — a doubt about the pre-Turkish stage, not about the Persian word's existence.\",\n          \"derivation_fa\": \"«lilac» انگلیسی نخست در دههٔ ۱۵۹۰ به نامِ درختچه ثبت شده (معنی رنگ در ۱۷۹۱ و صفتِ «بنفشِ کم‌رنگ» در ۱۸۰۱) و از فرانسوی گرفته شده است. خاستگاه شرقی واژه دیدگاه رایج است: کلاین آن را از اسپانیایی و عربی به فارسیِ lilak/nilak «نیلی‌رنگ» از نیل می‌رساند و واتکینز نیز LILAC را (همراه ANIL) درست از راه «فارسی nil» زیر ریشهٔ nei- «درخشیدن» آورده است. تنها اتیمانلاین است که ترکیِ leylak را وام‌دِه صورت‌های رومی می‌داند و پشتِ آن به نامی بومی در بالکان گمان می‌برد؛ این تردید دربارهٔ حلقهٔ پیش از ترکی است، نه دربارهٔ وجودِ واژهٔ فارسی. ادعای نورایی پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/lilac\",\n            \"https://en.wiktionary.org/wiki/lilac\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:757\", \"status\": \"partial\", \"note\": \"AHD:757 is a page of the 1975/76 New College edition's main dictionary (s.v. lilac), which is not readable online; the same dictionary's Indo-European appendix, available on disk as Watkins 1985, states the identical claim: 'nei-. To be excited, shine ... 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.]'. So the reference is right in substance, but the exact page could not be inspected.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"vol. I p.895 s.v. lilac\", \"stance\": \"supports\", \"note\": \"full chain 'MF. < Sp. lilac < Arab. lāylak, lilak < Pers. lilak, var. of nilak \\\"bluish\\\" < nil'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"silent\", \"note\": \"grep -n '^LILAC' SKT.txt returns nothing; the concise Skeat has no lilac entry.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/lilac\", \"stance\": \"contradicts\", \"note\": \"'1590s ... with French lilac, Spanish lilac from Turkish leylak (the tree reached Western Europe via Istanbul), perhaps from a native Balkan name.'\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Arabic\",\n          \"words\": \"al-nil\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic النيل al-nīl 'the indigo' (with the variants نيلة nīla and نيلج nīlaj) is the Persian word نیل with the Arabic definite article; in pronunciation the article's l assimilates to the following n, giving an-nīl, and it is this sandhi form that the Portuguese and Spanish traders heard and took over whole (anil). Addi Shir is explicit that the direction is Persian > Arabic and that the ultimate source is Indian: '(النيل) نبات العظلم يصبغ به أزرق، فارسيته نيل وهو مشتق من نيلى ... بالسنسكريت أي أزرق'; Mo'in adds from the Persian side that نیلج is the muʿarrab of Persian نیله (Borhan p.2231). Nourai's gloss 'the indigo' correctly renders the article.\",\n          \"derivation_fa\": \"عربی «النیل» (با گونه‌های «نیلة» و «نیلج») همان «نیلِ» فارسی است با حرف تعریف عربی؛ در تلفظ، لامِ حرف تعریف به نونِ پس از خود همگون می‌شود و an-nīl می‌دهد و بازرگانان پرتغالی و اسپانیایی همین صورتِ سرِهم را وام گرفتند (anil). ادّی شیر صریح می‌گوید سمتِ وام‌گیری از فارسی به عربی است و سرچشمهٔ نهایی هندی: «(النیل) ... فارسیته نیل وهو مشتق من نیلی ... بالسنسکریت أی أزرق»؛ معین نیز از سوی فارسی می‌افزاید که «نیلج» معرّبِ «نیلهٔ» فارسی است (برهان قاطع ص ۲۲۳۱). برگردانِ نورایی («the indigo») هم حرف تعریف را درست بازتاب داده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/anil\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:52\", \"status\": \"partial\", \"note\": \"AHD:52 is the main-dictionary page of the 1975/76 edition (s.v. anil / aniline), not accessible online; the same dictionary's root appendix (Watkins 1985, s.v. nei-) carries the claim: 'Possibly Persian nil, indigo: ANIL, LILAC'. Substance confirmed, page not inspectable.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AFM\", \"where\": \"Addi Shir s.v. (النيل), AFM_pages.txt leaf 156\", \"stance\": \"supports\", \"note\": \"'فارسيته نيل وهو مشتق من نيلى ... بالسنسكريت أي أزرق ولعصيره يقال نيله بالفارسية ومنه أنيلج'.\"},\n            {\"src\": \"KLN\", \"where\": \"vol. I p.37 s.v. anil\", \"stance\": \"supports\", \"note\": \"'Port. anil, fr. Arab. an-nīl, assimilated fr. al-nīl, fr. al-, \\\"the\\\", and nil, \\\"indigo\\\", fr. Pers. nila, ult. fr. OI. nīlī, \\\"indigo\\\", fr. nīlah, \\\"dark blue\\\"' — the assimilation al- > an- spelled out.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1568\", \"stance\": \"supports\", \"note\": \"'ar. nīla \\\"dass.\\\"; hieraus mit ar. Art., der dem folgenden n assimiliert wird, sp. anil, anir, kat. anyil, pg. anil, frz. anil'.\"},\n            {\"src\": \"BQT\", \"where\": \"p.2231, Mo'in's note\", \"stance\": \"supports\", \"note\": \"'نیلج - معرب نیله است که به نیل مشهور است' — the Arabic form is derived from the Persian, not vice versa.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Portuguese\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Empty pass-through box = Portuguese anil 'the indigo shrub, indigo dye', taken over from Arabic an-nīl with the assimilated article treated as part of the word (the same treatment as in Spanish anil, Catalan anyil). Portuguese is the pivot because the 16th-century Portuguese carried the dye from Gujarat and the Persian Gulf to Europe; Klein makes it the direct donor of English anil ('Port. anil, fr. Arab. an-nīl'), Etymonline 'from French or Portuguese anil', and Lokotsch lists 'pg. anil' beside sp. anil.\",\n          \"derivation_fa\": \"این جعبهٔ تهی نمایندهٔ anil پرتغالی «بوتهٔ نیل، رنگِ نیل» است که از عربی an-nīl وام گرفته شده و حرف تعریفِ همگون‌شده را بخشی از خودِ واژه پنداشته‌اند (همان‌گونه که در anil اسپانیایی و anyil کاتالانی). پرتغالی حلقهٔ کلیدی است، زیرا در سدهٔ ۱۶ پرتغالی‌ها این رنگ را از گجرات و خلیج فارس به اروپا می‌بردند؛ کلاین آن را وام‌دِه مستقیم anil انگلیسی می‌داند و اتیمانلاین «از فرانسوی یا پرتغالیِ anil».\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/anil\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"no refs= on this node in the book.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"vol. I p.37 s.v. anil\", \"stance\": \"supports\", \"note\": \"'Port. anil, fr. Arab. an-nīl'.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1568\", \"stance\": \"supports\", \"note\": \"'sp. anil, anir, kat. anyil, pg. anil, frz. anil'.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"anil, aniline\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Two words of different kinds. English anil 'the West Indian indigo shrub; indigo' (1580s) is a straight borrowing of Portuguese/French anil and the arrow drawn here is correct — Klein: 'anil ... Port. anil, fr. Arab. an-nīl'. English aniline, however, is not a borrowed word at all: it is the chemical name coined in 1841 by the German chemist Carl Julius Fritzsche on anil + -ine and taken up by A. W. Hofmann, entering English in 1843 (the substance itself had been obtained from indigo in 1826 and was first called crystallin). So its Persian-Arabic pedigree is real but indirect, running through the learned name rather than through Portuguese; the chart's Portuguese → English arrow is right for anil and a shortcut for aniline, hence 'plausible' for the node as a whole.\",\n          \"derivation_fa\": \"در این گره دو واژه از دو جنسِ متفاوت کنار هم نشسته‌اند. «anil» انگلیسی (۱۵۸۰ م) وامی مستقیم از anil پرتغالی/فرانسوی است و پیکانِ نمودار درست است. اما «aniline» به‌هیچ‌روی وام‌واژه نیست: نامی است شیمیایی که کارل یولیوس فریتسشهٔ آلمانی در ۱۸۴۱ از anil + پسوند ‑ine ساخت، هوفمان آن را رایج کرد و در ۱۸۴۳ به انگلیسی رسید (خودِ این ماده را در ۱۸۲۶ از تقطیر نیل گرفته و نخست crystallin نامیده بودند). پس تبارِ فارسی‑عربیِ آن واقعی است، ولی غیرمستقیم و از راهِ اصطلاح‌سازی علمی، نه از راه پرتغالی. پیکانِ «پرتغالی ← انگلیسی» برای anil درست و برای aniline میان‌بر است؛ از این‌رو گره «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/anil\",\n            \"https://www.etymonline.com/word/aniline\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:52\", \"status\": \"partial\", \"note\": \"the 1975/76 AHD page could not be read online; the appendix of the same dictionary (Watkins 1985 s.v. nei-) lists 'ANIL, LILAC' under the root, which is the claim the chart makes. The AHD appendix does not list ANILINE separately.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"vol. I p.37 s.v. anil, aniline\", \"stance\": \"partial\", \"note\": \"'anil ... Port. anil, fr. Arab. an-nīl' (supports), but 'aniline, also anilin ... Coined by C. J. Fritzsche in 1841 fr. anil and chem. suff. -ine' — i.e. a coinage, not a borrowing from Portuguese.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/aniline\", \"stance\": \"partial\", \"note\": \"'1843, coined 1841 by German chemist Carl Julius Fritzsche and adopted by Hofmann, ultimately from Portuguese anil ... from Arabic an-nil ... from Persian nila, ultimately from Sanskrit nili'.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1568\", \"stance\": \"supports\", \"note\": \"'ndl. anijl, engl. anile, neel \\\"Indigo\\\"; dtsch. Anilin, ein Farbstoff, der i. J. 1826 bei der Destillation von Indigo entdeckt ... wurde.'\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"French\",\n          \"words\": \"aniline\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"French aniline is the same 1841 chemical coinage, formed on French anil (itself from Portuguese/Arabic an-nīl) with the suffix -ine of chemical nomenclature, and current in French from the early 1840s; it is the form through which the word reached most other languages, Persian included (node #11). The chart's arrow Portuguese → French is therefore right about the word-history of anil and, for aniline, records the fact that the French chemical term rests on that borrowed base; strictly, the name was minted by a German chemist and merely naturalised in French, which is why the node is 'plausible' rather than 'confirmed'.\",\n          \"derivation_fa\": \"«aniline» فرانسوی همان برساختهٔ شیمیایی سال ۱۸۴۱ است که بر پایهٔ anil فرانسوی (خود از پرتغالی و عربی an-nīl) با پسوندِ ‑ine اصطلاحاتِ شیمی ساخته شد و از آغاز دههٔ ۱۸۴۰ در فرانسوی رواج داشت؛ همین صورت است که واژه را به بیشتر زبان‌ها، از جمله فارسی (گرهٔ ۱۱)، رساند. پیکانِ «پرتغالی ← فرانسوی» دربارهٔ تاریخِ واژهٔ anil درست است و دربارهٔ aniline نشان می‌دهد که اصطلاح فرانسوی بر همان پایهٔ وام‌گرفته ساخته شده؛ با این حال نام‌گذار شیمی‌دانی آلمانی بود و فرانسوی آن را بومی کرد، پس این گره «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/aniline\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:52\", \"status\": \"partial\", \"note\": \"same page as node #9: the 1975/76 AHD dictionary page is not online; the Watkins appendix of the same work supports the underlying anil < an-nīl < Persian nīl chain.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"vol. I p.37 s.v. aniline\", \"stance\": \"partial\", \"note\": \"'Coined by C. J. Fritzsche in 1841 fr. anil and chem. suff. -ine, resp. -in' — a coinage on the borrowed base, not a Romance inheritance.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1568\", \"stance\": \"supports\", \"note\": \"Lokotsch traces 'frz. anil' and 'dtsch. Anilin' to the same Arabic-Persian source, and dates the substance's discovery in indigo to 1826.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Persian\",\n          \"words\": \"ânâlîn «آنیلین»\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The word and the arrow are right, the transliteration is not. The Persian script in the box, آنیلین, reads ānīlīn — the ordinary modern Persian name of aniline, borrowed from French aniline, with the French nasal-free -ine rendered as ‑ین and the initial a- lengthened to آ- as in most French loans of the Qajar/Pahlavi period (cf. آمونیاک، آسپیرین). Mo'in's dictionary tags it exactly so: 'آنیلین [فر.] (اِ.) مایعی است بی‌رنگ و با بوی نامطبوع ... و نشانهٔ آن در شیمی C6H5NH2 است'; Dehkhoda likewise 'آنیلین. (فرانسوی، اِ) مادهٔ رنگی که از زغال سنگ گیرند'. But the Latin transliteration printed beside it is 'ânâlîn', with â where the script has ی: an impossible reading of آنیلین. The printed page (site/pages/356.jpg, copy at data/verification/sources/refs/ocr/BOOK/356.png) shows 'ânâlîn' in the book itself, so the JSON is faithful and the slip is Nourai's own misprint for ânîlîn.\",\n          \"derivation_fa\": \"واژه و پیکان درست است، آوانگاری نه. صورتِ فارسیِ درونِ جعبه، «آنیلین»، ānīlīn خوانده می‌شود؛ همان نامِ رایجِ امروزیِ این مادّه که وام‌واژه‌ای است از aniline فرانسوی، با بازنماییِ ‑ine فرانسوی به «‑ین» و کشیده‌شدنِ a آغازی به «آ»، چنان‌که در بیشترِ وام‌واژه‌های فرانسویِ دورهٔ قاجار و پهلوی (مانند آمونیاک و آسپیرین). معین همین را می‌گوید: «آنیلین [فر.] (اِ.) مایعی است بی‌رنگ و با بوی نامطبوع ... و نشانهٔ آن در شیمی C6H5NH2 است»، و دهخدا نیز «آنیلین. (فرانسوی، اِ) مادهٔ رنگی که از زغال سنگ گیرند». اما آوانگاریِ لاتینِ کنارِ آن «ânâlîn» است، با â به‌جای «ی»: خوانشی ناممکن از «آنیلین». تصویرِ صفحهٔ چاپی نشان می‌دهد که خودِ کتاب «ânâlîn» چاپ کرده است؛ پس خطای خوانشِ اسکن نیست، خطای چاپیِ کتاب است و صورت درست ânîlîn است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"ânâlîn «آنیلین»\",\n          \"correct_form\": \"ânîlîn «آنیلین»\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%A2%D9%86%DB%8C%D9%84%DB%8C%D9%86/\",\n            \"https://www.etymonline.com/word/aniline\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:98\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Farsi s.v. آنیلین, read through abadis.ir (the site reprints the lexicon entries): 'آنیلین [فر.] (اِ.) مایعی است بی رنگ و با بوی نامطبوع که در هوا کدر می شود و درآب کم محلول است ... و نشانة آن در شیمی C6H5NH2 است' — the tag [فر.] = French is precisely the arrow the chart draws. The volume/page (vol. 1 p.98) could not be checked against a scan, but the entry and its origin tag are Mo'in's.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"abadis.ir s.v. آنیلین (Mo'in entry)\", \"stance\": \"supports\", \"note\": \"origin tag '[فر.]' (French).\"},\n            {\"src\": \"DKH\", \"where\": \"abadis.ir s.v. آنیلین (Dehkhoda entry)\", \"stance\": \"supports\", \"note\": \"'آنیلین. (فرانسوی، اِ) مادهٔ رنگی که از زغال سنگ گیرند' — Dehkhoda also marks it a French loan.\"},\n            {\"src\": \"BOOK\", \"where\": \"printed page 326 = pdf 356 (data/verification/sources/refs/ocr/BOOK/356.png)\", \"stance\": \"supports\", \"note\": \"the printed box reads 'ânâlîn' next to آنیلین, so the extraction is faithful and the odd form is the book's own misprint.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Nei 2, Neia, Nî 3\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *neyH- 'to lead' (Pokorny 1. nei-, neiə-, nī-, IEW 760; LIV² *neiH-)\",\n      \"note\": \"Pokorny p.760: '1. nei-, neiə-, nī- \\\"führen\\\". Ai. nayati (Partiz. nītá-), av. nayeiti \\\"führt\\\", mpers. nītan \\\"führen, treiben\\\", ai. nīthā f. \\\"Führung, Weg\\\", netā, nitar-, netar- \\\"Führer\\\", netra- n. \\\"Führung, Auge\\\"; mir. né, nia \\\"Krieger, Held\\\"; hitt. nāi- \\\"lenken, führen\\\"'. Watkins has the same root as 'neiə-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.]', and Walde-Pokorny II 321 the same again. Nourai's three variants 'Nei 2, Neia, Nî 3' are exactly Pokorny's three ablaut shapes nei-/neiə-/nī-, and his 'Neia -> Nei 2' and 'Nei 3 -> Ne 1' redirects mirror Pokorny's own arrangement (Pokorny's 3. nei-, nī- is cross-referred to en-, p.312). Modern reconstruction keeps this root (Wiktionary/LIV *neyH- 'to lead', analysed as a neo-root from *(s)neh₁- + *-éyti), so this is the better-founded of the two roots on the page.\",\n      \"note_fa\": \"پوکورنی در صفحهٔ ۷۶۰: «1. nei-, neiə-, nī- «رهبری‌کردن، بردن». سنسکریت nayati (اسم مفعول nītá-)، اوستایی nayeiti «می‌برد»، فارسی میانه nītan «بردن، راندن»، سنسکریت nīthā «راه»، netar- «رهبر»، netra- «چشم»؛ ایرلندی میانه né/nia «دلاور»؛ هیتی nāi- «راندن، بردن»». واتکینز همین ریشه را با نامِ neiə- «to lead» آورده و والده‌پوکورنی (ج۲ ص۳۲۱) نیز همان. سه گونهٔ «Nei 2, Neia, Nî 3» در کتاب نورایی همان سه درجهٔ ابلاوتِ پوکورنی است، و ارجاعِ «Nei 3 ← Ne 1» هم بازتابِ همان ارجاعِ پوکورنی به ریشهٔ en- (ص ۳۱۲) است. بازسازیِ امروزی (LIV و ویکی‌واژه) این ریشه را با صورت *neyH- «بردن» نگه داشته است؛ پس این ریشه از ریشهٔ نخستِ همین صفحه استوارتر است. ادعای نورایی درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/neyH-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:760\", \"status\": \"supports\", \"note\": \"POK_02.txt \\\\f-leaf 422 (printed p.760): '1. nei-, neiə-, nī- \\\"führen\\\". Ai. náyati (Partiz. nītá-), av. nayeiti \\\"führt\\\", mpers. nītan \\\"führen, treiben\\\" ... hitt. nāi- \\\"lenken, führen\\\"'. Root, gloss and page all as cited.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. neiə-\", \"stance\": \"supports\", \"note\": \"'neiə-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.]'\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II p.321 (leaf 326)\", \"stance\": \"supports\", \"note\": \"'1. nei- \\\"führen\\\" (neiə-). Ai. náyati (Ptc. nītá-), av. nayeiti \\\"führt\\\", mp. nītan \\\"führen, treiben\\\", ai. nītar-, netar- m. \\\"Führer\\\", netra- n. \\\"Führung, Auge\\\"'.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.v. neið (1) (IEC.txt line 11599)\", \"stance\": \"supports\", \"note\": \"'neið (1) \\\"lead, send\\\". Skt. náyami \\\"lead\\\"; Av. naye-(imi) \\\"lead\\\"; Hitt. neyami, v. \\\"lead, send\\\"'.\"},\n        {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/neyH-\", \"stance\": \"supports\", \"note\": \"'*neyH- : to lead ... Neo-root from a reanalysis of *(s)neh₁- (\\\"to turn\\\") + *-éyti', with Proto-Indo-Iranian *náyHati and Proto-Iranian *niHtáh > Manichaean MP n'yd.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"nî 2, nay : to guide; nayeiti : leads; fra-nay : leads forward\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Bartholomae's AiW col. 1043 has the verb as a single Avestan-Old Persian lemma: '• j., g., p. nay- V. \\\"leiten\\\". Praes. 2 naya-, 3 nya-, 17 (Fut.) naēšya-', with the Younger Avestan 3 sg. nayeiti quoted from Vd 5.8 ('astō.vīδōtuš dim bandayāiti vayō dim bastəm nayeiti'), the prefixed forms ava-nayeni, upa-nayeni, para-nayeṇti, and the cross-reference 'ai. nāyati, niyat; mp. nītan'. On the Old Persian side Kent p.193 has 'nay- vb. \\\"lead\\\": Av. nayeiti, Skt. náyati ... anaya imf. DB 2.88; 3.88; 5.12 ... fra- + nay- \\\"lead forth, provide\\\": frānayam 1st sg. imf. DB 1.87', i.e. Nourai's fra-nay is the attested Behistun form frānayam. 'nî 2' is Nourai's own numbering of the Indo-Iranian root nī- (Avestan present stem naya-, zero grade nī- in the participle nīta-); the thematic present *náy-e-ti gives Av. nayeiti and OP nay-, with regular Iranian *ay > ay before a vowel. Everything in the box is right, including the joint 'Avestan / Old Persian' label, since both languages have the verb in the same shape.\",\n          \"derivation_fa\": \"بارتولومه در «فرهنگ ایرانی باستان» ستون ۱۰۴۳ این فعل را یک سرواژهٔ مشترکِ اوستایی و پارسی باستان آورده است: «nay- «بردن، رهبری‌کردن»، ستاکِ حال naya-، gونهٔ nya-، آیندهٔ naēšya-»، با صیغهٔ سومِ مفردِ اوستایی nayeiti از وندیداد ۵٫۸ و صورت‌های پیشوندی ava-nayeni و upa-nayeni، و ارجاعِ «سنسکریت nāyati؛ فارسی میانه nītan». از سوی پارسی باستان، کنت در صفحهٔ ۱۹۳ می‌نویسد: «nay- فعل «بردن»: اوستایی nayeiti، سنسکریت náyati ... anaya ماضی استمراری در بیستون ۲٫۸۸ ... fra- + nay- «پیش بردن، فراهم آوردن»: frānayam بیستون ۱٫۸۷» — یعنی «fra-nay» نورایی همان صورتِ گواه‌دارِ کتیبهٔ بیستون است. «nî 2» شماره‌گذاریِ خودِ نورایی برای ریشهٔ هندوایرانیِ nī- است (ستاکِ حالِ اوستایی naya-، درجهٔ صفرِ nī- در اسم مفعولِ nīta-). ادعای نورایی، از جمله برچسبِ دوگانهٔ «اوستایی/پارسی باستان»، درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/neyH-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1026\", \"status\": \"supports\", \"note\": \"Klein vol. II p.1026 (KLN_1966.txt \\\\f-leaf 549; the surrounding leaves carry the printed numerals 1022 and 1028) s.v. naik, naique: 'Hind. nayak, fr. OI. nāyakah, \\\"leader, chief, general\\\", fr. nāyati, \\\"leads\\\", which is rel. to Avestic nayeiti, \\\"leads\\\", and cogn. with Hitt. nai-, ne-, \\\"to guide, lead\\\", Mir. né, nia, \\\"hero, warrior\\\"' — Avestan nayeiti 'leads' on exactly the cited page.\"},\n            {\"ref\": \"HRN:265\", \"status\": \"supports\", \"note\": \"Horn, Grundriss der neupersischen Etymologie p.265 (HRN.txt \\\\f-leaf 287, headed '- 265 -'), no. 16: 'ānītan \\\"herzubringen\\\"; aw. *ā + √nay-; ai. ā-i √nī \\\"herbeigeleiten, -führen, -bringen, -holen\\\". Vergl. phlv. nītan.' Horn's Avestan root √nay- is the one drawn here.\"},\n            {\"ref\": \"SYN:712\", \"status\": \"supports\", \"note\": \"Buck, Dictionary of Selected Synonyms, §10.64 LEAD (vb.), which begins on the printed p.711/712 (SYN.txt \\\\f-leaf 773; leaf 774 carries the running head '711'): the discussion paragraph reads 'Skt. nī- (nayati, nītá-), Av., OPers. ni- (Av. 3sg. pres. nayeiti, OPers. 3sg. imperf. anaya, etc.); cf. Skt. netar- \\\"guide\\\" ... Walde-P. 2.321.'\"},\n            {\"ref\": \"POK:760\", \"status\": \"supports\", \"note\": \"IEW 760 '1. nei- ... av. nayeiti \\\"führt\\\"' (see the entry-level ref_check).\"},\n            {\"ref\": \"KNT:193\", \"status\": \"supports\", \"note\": \"Kent, Old Persian, Lexicon p.193 (KNT.txt \\\\f-leaf 216; the next leaf carries the running head '194 OLD PERSIAN'): 'nay- vb. \\\"lead\\\": Av. nayeiti, Skt. náyati. Conj., §213. anaya imf. DB 2.88; 3.88; 5.12 ... fra- + nay- \\\"lead forth, provide\\\": frānayam 1st sg. imf. DB 1.87.' Cheung's verb dictionary independently cites the same place ('*OLD PERSIAN: nay- \\\"to lead\\\" || (+ *fra-) \\\"to lead forth, provide\\\" = Kent: 193').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 1043 (BRT.txt line ~18600)\", \"stance\": \"supports\", \"note\": \"'• j., g., p. nay- V. \\\"leiten\\\". Praes. 2 naya-, 3 nya-, 17 (Fut.) naēšya- ... 1) \\\"jemanden leiten, führen\\\" ... ai. nāyati, niyat; mp. nītan.'\"},\n            {\"src\": \"CHEUNG\", \"where\": \"Etymological Dictionary of the Iranian Verb, *naiH¹ 'to lead' (p.~276)\", \"stance\": \"supports\", \"note\": \"'*naiH¹ \\\"to lead\\\". *AVESTAN: naii- (naē-) \\\"to lead\\\" ... Pres. them.: IND. 3sg. YAv. naiieiti (V 5.8 f.) ... *OLD PERSIAN: nay- \\\"to lead\\\" || (+ *fra-) \\\"to lead forth, provide\\\" = Kent: 193 ... impf. 1sg. franayam <f-r-a-n-y-m> (DB 1.87)'.\"},\n            {\"src\": \"KNT\", \"where\": \"p.193 s.v. nay-\", \"stance\": \"supports\", \"note\": \"as quoted in ref_check; also 'fra- prefix ... Found with verbs ... nay-'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"nîtan : to lead; ânîtan : to bring\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian has both verbs, from the same root with and without the preverb *ā-: nīdan / nay- 'to lead' (Book Pahlavi DB(Y)LWN-tn', an Aramaic ideogram from √dbr 'to lead', Manichaean n'y-) and ānīdan / ānay- 'to bring, lead (hither)' (Book Pahlavi HYTYWN-tn' < Aramaic hyty, Manichaean ''ny-) — MacKenzie's Concise Pahlavi Dictionary has 'nīdan, nay- [DB(Y)LWN-tn' < A √dbr]', 'ānīdan, ānay- [HYTYWN-tn' < A hyty; ʾnytn']  bring, lead' and, in his English index, 'lead (v.) ānīdan, franāftan, haxtan, nīdan, rāyēnīdan'. The forms rest on the participial stem *niH-tá- (Av. nīta-, Skt. nītá-) plus the MP infinitive ending, and on the present stem *naya- for nay-/ānay-. Nourai's spellings nītan / ānītan with -tan are Horn's 1893 transcription, which is what he cites; MacKenzie writes -dan because Book Pahlavi -tn' after a long vowel is read /d/. Not an error, just an older convention.\",\n          \"derivation_fa\": \"فارسی میانه هر دو فعل را دارد، از یک ریشه، یکی بی‌پیشوند و یکی با پیشوندِ *ā-: nīdan / nay- «بردن» (در پهلویِ کتابی با هزوارشِ آرامیِ DB(Y)LWN-tn' از ریشهٔ dbr، در مانوی n'y-) و ānīdan / ānay- «آوردن» (هزوارشِ HYTYWN-tn' از آرامیِ hyty، مانوی ''ny-). مکنزی در «فرهنگ کوچک پهلوی» هر دو را آورده و در نمایهٔ انگلیسیِ خود زیر «lead» می‌نویسد: «ānīdan, franāftan, haxtan, nīdan, rāyēnīdan». این صورت‌ها بر ستاکِ اسم مفعولیِ *niH-tá- (اوستایی nīta-، سنسکریت nītá-) و ستاکِ حالِ *naya- استوارند. نگارشِ «nîtan / ânîtan» با ‑tan آوانگاریِ هُرن (۱۸۹۳) است ـ همان مرجعی که نورایی به آن ارجاع داده ـ در حالی که مکنزی ‑dan می‌نویسد، زیرا ‑tn' پس از مصوت کشیده /d/ خوانده می‌شود. پس خطا نیست، تنها اختلاف قرارداد است؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/neyH-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:265\", \"status\": \"supports\", \"note\": \"Horn p.265 (HRN.txt leaf 287), no. 16 of the Pahlavi appendix: 'ānītan \\\"herzubringen\\\"; aw. *ā + √nay-; ai. ā-i √nī \\\"herbeigeleiten, -führen, -bringen, -holen\\\". Vergl. phlv. nītan.' Both of Nourai's Pahlavi words, with both glosses, on the cited page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. nīdan / ānīdan, and English index s.v. lead\", \"stance\": \"supports\", \"note\": \"'nay-, v. nīdan'; 'nīdan, nay- [DB(Y)LWN-tn' < A √dbr]'; 'ānīdan, ānay- [HYTYWN-tn' < A hyty, ʾnytn'] bring, lead'; index: 'lead (v.) ānīdan, franāftan, haxtan, nīdan, rāyēnīdan, zamēnīdan'.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\", \"note\": \"grep of NYB_vol2_glossary.txt for 'nītan' finds only the causative -ēnītan formations (akārēnītan, āstēnītan …); the glossary is limited to the texts Nyberg edits and has no entry for nīdan/ānīdan.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *naiH¹, Middle Persian section\", \"stance\": \"supports\", \"note\": \"'*MIDDLE PERSIAN: MMP n'y- (BMP DB(Y)LWN-) \\\"to lead\\\" || (+ *a-) MMP ''ny- (BMP HYTYWN-) \\\"to bring, lead\\\" = DMMPP: 239a, 49b f. ... Inf.: MMP nyydn'.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW col. 1043 s.v. nay-\", \"stance\": \"supports\", \"note\": \"closes the entry with 'mp. nītan' — Bartholomae himself uses Nourai's -tan spelling.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": null,\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"A genuinely blank box: the printed page (pdf 356, copy at data/verification/sources/refs/ocr/BOOK/356.png) shows an empty rounded frame to the right of the Pahlavi box, with no language label, no word and no reference, so the extraction is faithful and there is no claim to test. Judging from the layout it is the slot for the New Persian continuation, and it is empty for a good reason: neither Middle Persian verb survived into New Persian. MacKenzie's entries for nīdan and ānīdan carry no 'N ~' New Persian equivalent (contrast e.g. 'nibištan ... N nawištan'), and New Persian replaced them with بردن and آوردن; only derivatives such as نیو and رهنمود-type compounds continue the root indirectly. Marked 'unverified' because there is literally nothing in the box to confirm or dispute.\",\n          \"derivation_fa\": \"این جعبه در چاپِ کتاب واقعاً تهی است: در تصویرِ صفحه (pdf ۳۵۶) قابی گرد و خالی در سمت راستِ جعبهٔ پهلوی دیده می‌شود، بی‌برچسبِ زبان، بی‌واژه و بی‌ارجاع؛ پس خوانشِ اسکن درست است و ادعایی برای سنجیدن وجود ندارد. از آرایشِ نمودار برمی‌آید که جای «فارسی نو» بوده و بی‌دلیل هم تهی نمانده است: هیچ‌یک از دو فعلِ فارسی میانه به فارسی نو نرسیده است. مکنزی در برابر nīdan و ānīdan هیچ معادلِ «N» (فارسی نو) نمی‌آورد، و فارسی نو به‌جای آن‌ها «بردن» و «آوردن» را به کار می‌برد. از این‌رو داوری «تأییدنشده» است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"the box carries no language, no word and no refs= in the book.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. nīdan, ānīdan\", \"stance\": \"silent\", \"note\": \"no New Persian equivalent is given for either verb, unlike the great majority of MacKenzie's entries, which name the NP reflex after 'N'.\"},\n            {\"src\": \"BOOK\", \"where\": \"printed page 326 = pdf 356 (data/verification/sources/refs/ocr/BOOK/356.png)\", \"stance\": \"supports\", \"note\": \"the box on the page is empty; the JSON's empty node is a faithful rendering, not a dropped word.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-07T18:35:36.515Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-356.json (file state is current in your context — no need to Read it back)
```


## [2026-09-07T18:35:39.747Z] TOOL CALL #68: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-356.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 356"
}
```


### [2026-09-07T18:35:41.255Z] TOOL RESULT

```
JSON OK
nodes verified: 14/14
node verdicts: {'plausible': 3, 'confirmed': 9, 'transcription_suspect': 1, 'unverified': 1}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 5, 'supports': 9, 'not_checked': 5}
books consulted: {'silent': 4, 'partial': 5, 'contradicts': 3, 'supports': 29} | by book: {'KLN': 10, 'LKT': 9, 'AFM': 2, 'Etymonline': 2, 'BOOK': 2, 'BRT': 2, 'CHEUNG': 2, 'PHD': 2, 'WLD': 1, 'AHD': 1, 'HJB': 1, 'WEB/Etymonline': 1, 'SKT': 1, 'BQT': 1, 'MON': 1, 'DKH': 1, 'KNT': 1, 'NYB': 1}
```


## [2026-09-07T18:35:46.753Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport io\np='data/verification/page-356.json'\ns=io.open(p,encoding='utf-8').read()\ns=s.replace('\"src\": \"WEB/Etymonline\"','\"src\": \"Etymonline\"')\nio.open(p,'w',encoding='utf-8').write(s)\nEOF\npython3 -m json.tool data/verification/page-356.json >/dev/null && python3 tools/verify_check.py 356 | tail -5"
}
```


### [2026-09-07T18:35:48.193Z] TOOL RESULT

```
nodes verified: 14/14
node verdicts: {'plausible': 3, 'confirmed': 9, 'transcription_suspect': 1, 'unverified': 1}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 5, 'supports': 9, 'not_checked': 5}
books consulted: {'silent': 4, 'partial': 5, 'contradicts': 3, 'supports': 29} | by book: {'KLN': 10, 'LKT': 9, 'Etymonline': 3, 'AFM': 2, 'BOOK': 2, 'BRT': 2, 'CHEUNG': 2, 'PHD': 2, 'WLD': 1, 'AHD': 1, 'HJB': 1, 'SKT': 1, 'BQT': 1, 'MON': 1, 'DKH': 1, 'KNT': 1, 'NYB': 1}
```


## [2026-09-07T18:36:05.690Z] AGENT

Done — `data/verification/page-356.json` written, valid JSON, `verify_check.py 356` reports 14/14 nodes and 0 PROBLEM lines.

**Page 356 (book p. 326) — verdicts**
- Roots: 2 confirmed (Nei 1 "to shine/be excited" = Pokorny 2. nei- IEW 760; Nei 2/Neia/Nî 3 "to lead" = Pokorny 1. nei- IEW 760 — Nourai's numbering is the inverse of Pokorny's, page and glosses correct)
- Nodes: 9 confirmed, 3 plausible, 1 transcription_suspect, 1 unverified
- Ref checks: 9 supports, 5 partial, 5 not_checked (nodes with no `refs=`)

**Flagged items**
- #11 Persian `ânâlîn «آنیلین»` — transcription_suspect, `error_in: "book"`: the script reads ānīlīn, the printed transliteration says "ânâlîn" (â where the script has ی). Page image confirms the book itself prints "ânâlîn", so the extraction is faithful; correct form ânîlîn. The derivation (French *aniline* → Persian) is confirmed by Mo'in [فر.] and Dehkhoda.
- #1 Sanskrit nili/nilah/nîlotpala — plausible: Pokorny attaches nīla- to the root only as "zweifelhaft", Walde-Pokorny omits it, Klein/Watkins/Wiktionary say "possibly"; Lokotsch (no. 1568) derives it instead from *nihlas, cognate with Latin niger.
- #9, #10 English/French aniline — plausible: *anil* is a genuine borrowing, but *aniline* is an 1841 chemical coinage by C. J. Fritzsche on *anil*, not a word passed from Portuguese.
- #3 (entry 1) — unverified: the printed box is genuinely blank (no language, word or ref). MacKenzie gives no New Persian reflex for nīdan/ānīdan, which explains the empty slot.

**No extraction errors found** — the JSON matches the printed page throughout (including the empty Spanish/French/Portuguese pass-through boxes and the blank box in entry 1).

Notable verified references: BQT:2231 = Borhan vol. 4, pdf p. 314 — carries Mo'in's «نیله … از سانسکریت nīla» footnote and the exact Farrokhī Sīstānī verse; KNT:193, KLN:1026 (s.v. *naik*), HRN:265 (s.v. ānītan), SYN:712 (Buck §10.64 LEAD) all check out verbatim. UNV:51 checks out in substance (nīlōpar < Skt. nīlotpala) but sits on p. ~35 of the copy on disk — the 1963 edition's pagination differs. AHD:757/AHD:52 are 1976 main-dictionary pages (not online), marked partial; the same dictionary's root appendix states the claim. 11 web sources archived via `fetch_source.py`.
