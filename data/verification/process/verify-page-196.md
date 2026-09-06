# Verification process log — verify-page-196


## [2026-09-06T02:14:38.175Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 196 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-196.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-196.json. Write /home/sfmqrb/git/rishe/data/verification/page-196.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 196` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T02:14:39.881Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T02:14:40.610Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T02:14:40.630Z] TOOL RESULT

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


## [2026-09-06T02:14:40.862Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-196.txt"
}
```


### [2026-09-06T02:14:40.873Z] TOOL RESULT

```
1	=== PDF page 196 (book page 166) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ghuel : crooked, bent  (refs POK:489)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:489 | zŭrah : lie, cheat
5	  #2 (parent #1) [Pahlavi] refs=None | zŭr
6	    #3 (parent #2) [Persian] refs=HRN:147; ETM:67; POK:489 | zŭr 2 «زور» : lie
7	    #4 (parent #2) [Arabic] refs=ETM:67; VDQ:240 | zŭr : lie (against God) ; tazvîr : pretence ; mozavver : liar
8	      #5 (parent #4) [Persian] refs=ETM:67 | tazvîr «تزویر» : pretence ; mozavver «مزوّر» : liar
9	#6 (parent #0) [Greek] refs=POK:489 | phalos : lie
10	#7 (parent #0) [Latin] refs=POK:489 | fallô-ere : to falsify ; falsus : lie
11	  #8 (parent #7) [English] refs=AHD:470,473 | false ; fail ; failure
12	--- entry 1 ---
13	ROOT Ghŭgh -> redirect to Gheugh
14	--- entry 2 ---
15	ROOT [Indo-European] Ghŭk, Ghŭkos : hoot, whoop  (refs IEC:347)
16	#1 (parent #0) [Persian] refs=IEC:347; MON:2454 | ğŭk «غوک» : frog | extra: غوق
17	#2 (parent #0) [Sanskrit] refs=IEC:347 | ghŭkah : owl
18	#3 (parent #0) [Middle German] refs=IEC:347 | gucken : a kind of bird
19	--- entry 3 ---
20	ROOT Ghŭkos -> redirect to Ghŭk
21	--- entry 4 ---
22	ROOT Ǧhumbo -> redirect to Gwa
23	--- entry 5 ---
24	ROOT Ghu-to -> redirect to Ghu 1
25	--- entry 6 ---
26	ROOT Gî -> redirect to Gěi
27	--- entry 7 ---
28	ROOT Gieu -> redirect to Geu 3
29	
```


## [2026-09-06T02:14:43.899Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-196.json",
 "description": "Read source JSON page 196"
}
```


### [2026-09-06T02:14:43.954Z] TOOL RESULT

```
{
  "pdf_page": 196,
  "book_page": 166,
  "entries": [
    {
      "root": {
        "name": "Ghuel",
        "lang": "Indo-European",
        "refs": "POK:489",
        "gloss": "crooked, bent"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:489",
          "words": [
            {"translit": "zŭrah", "gloss": "lie, cheat", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": null,
          "words": [
            {"translit": "zŭr", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "HRN:147; ETM:67; POK:489",
          "words": [
            {"translit": "zŭr 2", "gloss": "lie", "script": "زور"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Arabic",
          "refs": "ETM:67; VDQ:240",
          "words": [
            {"translit": "zŭr", "gloss": "lie (against God)", "script": null},
            {"translit": "tazvîr", "gloss": "pretence", "script": null},
            {"translit": "mozavver", "gloss": "liar", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "ETM:67",
          "words": [
            {"translit": "tazvîr", "gloss": "pretence", "script": "تزویر"},
            {"translit": "mozavver", "gloss": "liar", "script": "مزوّر"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:489",
          "words": [
            {"translit": "phalos", "gloss": "lie", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:489",
          "words": [
            {"translit": "fallô-ere", "gloss": "to falsify", "script": null},
            {"translit": "falsus", "gloss": "lie", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": "AHD:470,473",
          "words": [
            {"translit": "false", "gloss": null, "script": null},
            {"translit": "fail", "gloss": null, "script": null},
            {"translit": "failure", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ghŭgh",
        "redirect": "Gheugh"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ghŭk, Ghŭkos",
        "lang": "Indo-European",
        "refs": "IEC:347",
        "gloss": "hoot, whoop"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:347; MON:2454",
          "words": [
            {"translit": "ğŭk", "gloss": "frog", "script": "غوک"}
          ],
          "script_extra": "غوق",
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:347",
          "words": [
            {"translit": "ghŭkah", "gloss": "owl", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Middle German",
          "refs": "IEC:347",
          "words": [
            {"translit": "gucken", "gloss": "a kind of bird", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ghŭkos",
        "redirect": "Ghŭk"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ǧhumbo",
        "redirect": "Gwa"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ghu-to",
        "redirect": "Ghu 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Gî",
        "redirect": "Gěi"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Gieu",
        "redirect": "Geu 3"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-06T02:14:44.440Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T02:14:44.478Z] TOOL RESULT

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


## [2026-09-06T02:15:02.720Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ghu̯el\\|ghu̯er\\|ghwel\" POK_full.txt | head -40; echo \"---PAGE489---\"; grep -n \"^489\\|489$\" POK_full.txt | head",
 "description": "Grep Pokorny for ghwel"
}
```


## [2026-09-06T02:15:04.241Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','ETM','VDQ','HRN','IEC','MON','AHD']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:900])\n    print()\n\"",
 "description": "Check refs_online for keys"
}
```


### [2026-09-06T02:15:04.262Z] TOOL RESULT

```
36298:The enxtended root {*ghwel-)-nta, -na, -/aformants follow the model of lllyrian - Anatolian 
---PAGE489---
```


### [2026-09-06T02:15:05.901Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry

ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}

VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Not on archive.org. Also on ghaemiyeh (ghbook.ir) as an app/EPUB per news reports.", "cites": "page number of the Persian translation of Jeffery's Foreign Vocabulary of the Qurʾān"}

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": "", "cites": "column/page number of Mann, An Indo-Europea

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
```


## [2026-09-06T02:15:11.389Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=497 && NR<=499' POK_01.txt | head -120",
 "description": "Print Pokorny page 489 area"
}
```


### [2026-09-06T02:15:12.910Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T02:15:15.320Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"$f: $(wc -c < $f) bytes, $(tr -cd '\\f' < $f | wc -c) FF\"; done",
 "description": "Check POK file sizes and form feeds"
}
```


### [2026-09-06T02:15:16.836Z] TOOL RESULT

```
POK_01.txt: 981836 bytes, 363 FF
POK_02.txt: 1137861 bytes, 433 FF
POK_03.txt: 1170809 bytes, 429 FF
POK_full.txt: 3971883 bytes, 0 FF
```


## [2026-09-06T02:15:19.762Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=145 && NR<=147' POK_02.txt",
 "description": "Print POK_02 leaves 144-146"
}
```


### [2026-09-06T02:15:21.448Z] TOOL RESULT

```
 mit  den  Zähnen'  (daneben  durch  Entgleisung aus  ßQv^o),  eßgv^a :  ßgiTio))  ,beiße',  ßQvydrjv  ,beißend',  ßQV'y(,iög  , Zähne- knirschen', ßgvxsTÖQ  ,kaltes  Fieber'  (,Zähneklappern').
486
b)  air.  hrön  ^Kummer^  cjmr.  brtoyn  ^stechender  Schmerz'  (urkelt. *brügnos);
lit.  grduziu,  grduHi  ,nagen^  sugrüzinü  ^vernichten';
aksl.  gryzq,  grysti  ,nagen'  (in  andern  slav.  Sprachen  auch  von  nagendem Kummer;  hierher  wohl  auch  sloven.  grüze  PI.  f.  ^Krätze^.
Zu  gryzg  wahrscheinlich  russ.  grusth  ^Kummer',  sloven.  grüst  ,EkeP.
WP.  I  697  f.,  Trautmann  100.
j
Ohvi  und  Q^h.
^bctei{o-)  , hinschwinden,  z'ngrunde  gehen^,  auch  trans.  ^vernichten' ; gVidi-ti-s,  g^bdoi-o-  ,Untergang^
Ai.  ksindti,  ksinöti  ( :  gr.  *q)d-LvJ^-(o)j  ksdyati  ,vernichtet,  läßt  vergehen', partiz.  ksitd-h  , erschöpft'  (=  gr.  q)d'LTÖg ;  srdva-h  dksitam  =  gr.  y,Xeog  Ucfd-i- xov  ^unverwüstlicher  Ruhm^),  kslnd-h  ds.,  ksiydte  , schwindet  hin,  nimmt ein  Ende',  ksayd-h  , Abnahme,  Untergang'  (:  gr.  q)'d'örj  f.),  kHti-h  , Ver- drehen, Untergang'  (=  gr.  q)d-L(TLg  und  -?-  lat.  sitisj  vgl.  -tuSt  lat.  sittts)]
prakr.  ajjhitah-  (=  äq)d-LTog)y  jklna-  (=  ai.  kslna-)]
av.  ay^önvamndm  ,sich  nicht  mindernd'  (Kuiper  Nasalpräs.  65^);
gr.  ep.  (pMvoiy  att.  q)d-tvu)  (^cpS-ivfWy  s.  oben)  , vernichte',  meist  intr. ,schwinde  hin,  gehe  zugrunde',  cp^ivv-d-o)  , schwinde  hin,  mache  verschwin- den', Fut.  q)d'hao)  (att.  di7to(pd-taw)j  Aor.  eifdsiaa  (att.  SLTtecpd-Xaa),  icpd-t(.iriv^ qi&ffxsvog  ,vernichten',  Pass.  , zugrunde  gehen',  Partiz.  Perf.  Pass.  q}&LTÖg, (pd-ÖT}  , Schwindsucht',  (pd-laig  ds.  (s.  oben  ) ;  über  vielleicht  alte  Doppel- formen, wie  ipiv€G&aLj  xpiva^siv  , Blüten  oder  Früchte  abfallen  lassen,  ver- lieren', xpLGig'  dnwXeia  Hes.,  u.  dgl.  s.  Schwyzer  Gr.  Gr.  I  326.
Aus  dem  Lat.  wahrscheinlich  situs,  -üs  ,der  modrige  Schmutz  und Schimmel,  körperliche  Unreinlichkeit  und  alles  körperliche  und  geistige  Ver- rosten' und  suis  ,Durst'  (wenn  eigentlich  ,*Hinschwinden,  Verschmachten').
WP.  I  505 f.,  Schwyzer  Gr.  Gr.  I  326,  Benveniste  BSL.  38,  139 ff.
g^hffer-   (oder  besser  g^ider-??)  , 
rinnen,   fließen;   zerrinnen,  verschwinden',
im  ar.  Kaus.  und   im  gr.  zo-Verbum   trans.  , rinnen  lassen,  zerrinnen
lassen',  daher  gr.  , verschwinden  lassen,  vernichten'.
Ai.    k^drati   , fließt,   strömt,   zerrinnt,   verschwindet',    ksara-m   ,Wasser',
ksärayati  ,läßt  fließen',  ksälayati  , wäscht  ab'  (vgl.  Wackernagel  Ai.  Gr.  I
241);  av.  y^araiti  , strömt,  wallt  auf,  yzärayeiti  ,läßt  fließen',  mit  vi-  ,läßt
überfließen';  Weiterbildung  in  a-yzrädayeiti  ,läßt  aufwallen',  vi-yzrädayeiti
;läßt  auseinander,   überwallen' ;    umgestellt  zyar-  in  avi  fra-zyaraiti  ,fließt
herzu
zu-
wahrscheinlich arm.  jur,  Gen.  jroy  ,Wasser'  {^g^hdöro-)] gr;  att.  cpd-slQix)  {*q)d'SQia}',  lesb.  q)&8QQü},  ark.  (pd^iqqoj)),  schwachstufig  dor. (pd-aiQü)   (*q)&aQicü)   ,richte   zugrunde';    dazu    auch   g)d-6iQ  ,Laus'    (ipeigsc (pd-eiQSi  Hes.  ist  Folge  der  spätem  spirantischen  Aussprache  des  ^),  (pd'OQ&
488  f
^Verderben,  Vernichtung'  und  (als  Rest  der  älteren  Bedeut.)  ,Yerniischt oder  Verreibung    der    Farben',    ebenso    av^igj^sigo)    außer    ,zugleich   od« gänzlich   zugrunde    richten'    auch    ,lasse  Farben   ineinanderfließen',   da^ auch    ^verschmelzen,    vermischen    überhaupt',   avi.icpd-siQeadai   ;Zusaminei2 strömen'.
WP.  I  700,  Schwyzer  Gr.  Gr.  I  326,  714,    Benveniste  BSL.  38,  139  £
g^hedh-  , bitten,  begehren'.
Av.  jaiöyemi,  apers.  Jadiyämiy  ,ich  bitte';
gr.  Aor.  d-saaaad'ai  {*gVihedk-s-)  ,anflehen',  Partiz.  -d^satög  in  dnö^eavog ,verwünscht,  verschmäht',  Ttolv-d'sarog  ,sehr  ersehnt',  Pers.-N.  Oeö-S-earog böot.  0LÖ-q)SLarog]  ftö&og  m.,  tto&i^  f.  ,Sehnsucht,  Verlangen',  nod-m  ,er. sehne,  vermisse  schmerzlich,  verlange';
air.  guidiiL  ,bitte'  (=  nod-io}),  Perf.  1.  Sg.  ro-gäd,  s-Konj.  1.  PI.  gessam (usw.);  geiss  f., Verwünschung, Tabu'  {*gViedh-ti-s)]  guide,G ehet^ {*g^hodhia)'^ foigde  ,BetteW  (^uo-gediä) -,  cjmr.  gweddi  , Gebet'  (*uo-godlma) ;
lit.  geddu-ju,  -ti  ,sich  sehnen,  sehnsüchtig  suchen,  verlangen,  wollen', gedü  (und  gedziü),  gedeti  ,sich  sehnen ;  traurig  sein,  trauern' ;  Nasalpräsens pasigendü,  -gedaü,  -gesti  ,sich  sehnen;  etwas  vermissen',  ablaut.  Kausat. gadmti  ,verderben,  stören',  daher  sekundär  der  ö -Vokalismus  (statt  uo) von  gödas  ,Gier,  Habsucht;  Klette',  godits  , ha
bgierig,  geizig',  godziüoi^ godetis  ,begehren,  wonach  dürsten,  wünschen,  begierig  sein';
im  Slav.  mit  durchgeführter  Nasalierung :  aksl.  z^zdq^  ^^dati,  acech.  Mdatil ,begehren,  wonach  dürsten',  z^zdg,  zedeti  ,cupere',  z^^da  , Durst',  poln/ zqdza  ,Begehren,  Gier,  Sehnsucht,  Wunsch';
unsicher  wegen  des  Anlautes  anord.  ged  n.  (*gadia-)   ,Sinn,  Charakter," Verlangen,   Lust',   gedlauss   , charakterlos'   vielleicht  =  ahd.  getilös,  mhd.  | getlös  ,zügellos,  mutwillig';
man  beachte  die  übereinstimmende  Gruppierung  d^eaaaad^ai  ;  Ttod^sw  = ir.  gess-am  (*guhedh-s-o-mos)  :  guidiu  (*g'^liodh-eiö).
WP.  I  673,  Trautmann  84£.,  Endzelin  Lett.  Gr.  577.
(*^Mi2ei-0  g'^hgi-,  g^bgi-d- :  g^hid-  ,hell,  leuchtend';  g^hoi-d-ro-s  ds.
Gr.  (patÖQÖg  ,klar,  hellglänzend,  leuchtend;  heiter,  vergnügt'  (=  lit. giedras),  woneben  cpaidi-  im  cpaidL(j,og  ,glänzend,  stattlich';  q)aLÖg  ,schum- merig,  dämmerig,  bräunlich,  grau'  (Gdf.  *(p(xL-J^ög  oder  -oög)'^  cparAÖg' XafiTtQÖg  Hes. ;
lit.    giedrasj    gaidrüs    ,heiter,    klar'    (davon    giedrä,    gaidrä   f.    ,schönes Wetter'),  lett.  dziedrs  ,azurblau',  ablautend  dzidrums  ,Klarheit';  lit.  gaisas  ■- i^g^hdid-so-s),  gaisa  , Lichtschein  am  Himmel',  lett.  gäiss  m.  ,Luft,  Wetter', gaiss  (*gaisus)   ,klar',   gäisma   f.  ,Licht',   lit.   gaXsras   m.   ,Lichtschein   am
489
Uimmel,    Feuersbrunst;    Zorn^,    gaXzdras    m.    , Lichtschein    am    Himmel'; ■tvohl  auch  apr.  gaylis  ,weiß*. WP.  I  665,  Trautmann  75.
g^beio-  :  g^hl-  , Ader,  Sehne,  Band' ;  gHbi-slo-  ds. Cymr.  gi-au  PL  ,Nerven,  Sehnen';
lit.  gijä  , Faden  im  Aufzug  eines  Gewebes',  lett.  dzija  , Faden,  PL Garn';
aksL  H-ca  , Sehne',  russ.  diaL  Mca  ,Kammgarn',  skr.  zica  ,Faden,  Draht, Schnur,  Saite';  die  bsl7-Formen  könnten  auch  zu  gVin9-  gehören.
g'ihislO'',
Arm.  jil  , Sehne,  Schnur';
lat.  fllum  , Faden';
lit.  gysla  ,Ader,  Sehne,  Blattrippe',  lett.  dztsla^  dztksla  ,Ader'  (die Nasalierung  in  zemait.  ginsla  ist  sekundär),  apr.  pettegislo  , Rückenader' ; aber  aksl.  züa^  russ.  i2?a,  skr.  zila  usw.  ,Ader,  Sehne'  sind  Neubildun- gen zu  zi-ca,  s.  oben.
WP.  I  670,  694,  WH.  I  497  f.,  Trautmann  87,  90.
g^bel-
```


## [2026-09-06T02:15:26.326Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==148' POK_02.txt | head -60",
 "description": "Print POK_02 leaf 147"
}
```


### [2026-09-06T02:15:28.048Z] TOOL RESULT

```
  ,wollen'.
Gr.  d-slü)j  i-&€lo)  (zum  Präfix  s.  W-,  ö-Part.)  ,will,  wünsche',  ablautend (pakiC^ei '  d'eXei  Hes. ;  ijiL^dg)sXog  ,heftig' ;
anord.  gildra  f. ;  gildri  n.  , Falle',  gilja  ,verlocken',  aschwed.  gicel- skaper  , Unzucht';
aksL  zeleti,  ^elatij  iter.  russ.-ksl.  zalati  ,wünschen',  aksl.  zelja  , Wunsch, Sehnsucht'  (auch  ,trauern'  und  ,Trauer'  durch  Anlehnung  an  ^aU  , Schmerz' von  *^"eZ-  ,stechen').
WP.  I  692.
gbuel-  ,sich  krümmen,  von  der  geraden  Richtung  abbiegen  (auch  geistig und  sittlich)  u.  dgl.';  ghuelo-s  ,gekrümmt'.
Ai.  hvdrate  ,biegt  von  der  geraden  Richtung  ab,  macht  krumme  Wege', hvdlati  ,gerät  auf  Abwege,  strauchelt,  irrt',  juhuränd-h  , mißglückend', vihriUa-h  , schadhaft,  krank',  hrunäti  ,geht  irre',  Partiz.  hrutd-y  geneuert hvftd-',  hürchati  ,geht  schief,  gleitet,  schwankt,  fällt';  hvdras-  n.  ,Krüm- mung',  hvard-  m.  , Schlange',  vihrüt-  f.  ,Art  Schlange  oder  Wurm' ;
av.  zbardmna-  ,krumm  gehend',  zharad-a-  n.  ,Fuß  daevischer  Wesen', zharah-  n.  ,Hügel',   zürah-  n.  ,Unrecht,  Trug',   npers.  zur  , falsch;  Lüge';
gr.  q)aXl7tT€L'  uwqaivei  Hes.,  (paXög  , stammelnd,  töricht'  Hes.  und  wahr- scheinlich (pdXoQ  m.  ,hornartiger  Vorsprung  am  Helm',  vermutlich  g)oAxdg, Beiwort  des  Thersites  B.  217,  etwa  , krummbeinig' ;   vielleicht  auch  dTto-
L
490  •
(fcblLog   ,trügerisch'    (ö-stufig),    q)fjlog    ^betrügerisch^,    q)rjXi^T7jg    ;Betrüger',  v? cprjXötJ  (dor.  cpaXöcü)  betrüge';  ^^';
lat.  fallö,  -ere  ^täuschen,  betrügen;  unwirksam  machen;  sich  entziehen-  ^'-^ unbemerkt  bleiben'  (,*krumme  Wege  machen;   ausbiegen';    *ghujnö,  vgl.  - ai.  hrunäti)'j  '4-  -
lit.  nuozvelnüs  ,abschüssig'j  zvalüs  ^geschickt;  flink,  behend'  (,*sich leicht  biegend');  ablaut.  i^vünas  ,schräg,  schief  {*g'hul-),  pa^il-ti,  -au ,sich  neigen',  ir^/^wo^t  , schaukeln,  schwanken';  prazulnas  (*ghul-)  ,schräge, schief,  paMnus  ds. ;  atiülas,  -us  ,schroff,  hart,  unhöflich,  unbarmherzig' u.  dgl. ;
lett.  zveVu,  zveVu,  zvelt  ,wälzen,  fortbewegen,  umwerfen ;  schlagen',  refl. ,sich  schwerfällig  fortbewegen,  sich  wälzen,  umfallen',  zvalstities  ,wanken, schwanken',  zvatns  ,sch wankend';
aksl.  z^l^  ,böse,  schlimm',  skr.  zäo  (f.  zlä)^  russ.  zoi  (f.  zia)  ds. ;
vielleicht  *ghu-el-  aus  einem  gheu-  ,schief'  erweitert;  vgl.  ^ghu-er-  in lit,  ziirU  ,eine  Rankenpflanze'  (*g^ur-lo-),  gv.  ^egfiog  m.  ,Feigenbohne^ (*guher-mo-).
WP.  I  643 f.,  WH.  I  448,   Trautmann  372  f.
•'^^ ' ghuelg-  ,anblicken'?  ^-^'<
Gr.  d-sXyo}   ,bezaubere,   umschmeichle'   (unwahrscheinlich   oben  S.  247);
lit.  ^velgiüj  zvelgti  ^anblicken',  Iterat.  zvalgaUj  zvalgyti  und  zvilgis  m. , Blick',  ^vUgiu,  ^vilgUi  ,kurz  hinblicken'.
WP.  I  644,  Trautmann  374,  Schwyzer  Gr.  Gr.  I  302.  .v4.^-
^hemh-  , lustig  springen,  hüpfen'??  "^
Gr.  äd-sixßovaa '  äy.oXaaraivovaa  (,ausgelassen')  Hes. ;
mhd.  gampen,  gumpen  , springen',  gampel,  gumpel  , lustiges  mutwilliges Springen,  PossenspieF,  gümpelj  nhd.  Gimpel]  mit  oberdeutscher  Lautver- schiebung mhd.  gampf  m.
```


## [2026-09-06T02:15:54.398Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT zura ===\"; grep -n -i \"zūra\\|zura-\\|zurah\\|zūrah\" KNT.txt | head -20; echo \"=== BRT zurah ===\"; grep -n \"zūrah\\|zurah\\|zbar\" BRT.txt | head -20; echo \"=== PHD zur ===\"; grep -n -i \"^zūr\\|zūr \\|zwl\" PHD.txt PHD_mackenzie.txt | head -20",
 "description": "Grep Kent, Bartholomae, MacKenzie"
}
```


### [2026-09-06T02:15:54.498Z] TOOL RESULT

```
=== KNT zura ===
1331:q*e. On züra-kara ‘evil-doer’ from *zurah-kara-,
=== BRT zurah ===
2658:denn',  mit  folg.  Konj.:  "va  ts  eäi-ar» aojaica  framrava  .  .  fravannqm  "so  WÜI ich  dir  denn  erzählen  von  . ."  Yt.  y. I.  a)  hinter  dem  ersten  Wort  des Satzes,  zur  Hervorhebung;  unübersetzbar: ^ra  (sd.,  auch  fdSt.)  °va  V.j.40,  usw.;  — - rüit  'Vä  aku  (sd.)  vistö  nagdä,.  Y.29.6; —  fracaraiö  (sd.)  °va  ..  N.  /oy.
3436:j,  ai%ra  P.  26:  lies  i%ra, *  g-i  j'  ^t  P^-  'dai  dann,  darauf;  aber; denn;  und';  oft  unübersetzbar.  A)  an
3440:fryai  "inoavqs  (sd.)  saßyll  maj-ailJ  at  nJ a},i  ..  dazdyli  hakurmi  {%A^  Y.44.1; 161  3^-7iS4-^^  (benutzt /7. 9),  2)  ein- leitend, unübersetzbar:  aj  niä  yavä  blndxS pafri .  .  Y.491;  '•  5<  3<*-3,  3'-^.  33"' 9,1^,34-4,  4ß-A,t4,  4tV.3,  7,  12,  5«.  10, 57.10.  a)  insbes.  beim  a)  Futur:  al  tJ
3455:atcit  . .  "wenn  auch  .  .,  so  doch  . ."  Yt s)  einen  selbständigen  Satz  ein- leitend, vor  Konj.,  unübersetzbar:  a/cTt aAmäi  .  .  ankaiti  Y.50.3.  3)  einen Satzteil  anschliessend;  a)  'und  zwar" :  panca- ahmi  .  .  ajcij  ahmäl  ya^a  .  .  av/ia^ niväitisisd.)^.  10.16.  b)  'aber':  agustJ (sd.)  . .  aäbyl  ySi  . .  atlu  a^bya  vakiltä  Y. 31.1.
4482:•  j,  a-inizbaratay-  f.  'das  Nichtweg-, forttragen':   nizhnla  (sd.)   nSit   Ua  (LS.)
4828:mit  frS^''^  i)  'hervorgehen,  -Ireten': aiiihe  haxayB  fräyente  astva(.»r>take  Yt. ■'5-9SJ  — yü'ia  .,  hvanxsaet^m  tarasca harqtn..fraca  iii/i  aiwica  vazaite  ava^a  . . Yt  /0.118.  2)  'vorwärts,  weiter  gehen': fräyantö  tarö  pilüm  ..yim  cinvats  Vyt. 42.  a)  &oiysX  mA  ß-a^a: /rain /raysiii^ irUtim  uzbaröti  äpö  V.6.2T,  — /ra/a  fra- yaniu  n  maoö  (sA)  Y. /O.  14,  ig;  19;  — /rasa  /raya  (aSIA.)!'  vahisDm  a  ahüm binjayanti  (sd.)  ie  ..  V,  7.52;  —  vgl.  Inf. Jrayäi.  3)  'einhergehen'  iyio? paiti  mit Akk.):  yat  ÖS  paiii  ml  asava  frayaf^  .  . aismssastö  .  .  V.J.  i ;  —  äat  liama  yh paiti  frayat^^  tä paiii, .Yi.  lOjiJ).  4)  'be- gehen', mit  Akk.,  a)  einen  Weg:  kaf  tä pa>ä  (sd.)  Jrayqn^  pasvqm  vil  staorqm va  narqm  vä  Y.S.iy,  ii^23,  3.  15;  — likrava  paoirlm  aHa  pa%ä/rayanlu{s\.3Xl Sing.)  V.  Ä19.  b)  eine  Tat:  (aili  tä ^ao^aa  varsta  , .  fralta^''^  apati(a{&i.) anuzvars/a  . .  V.i^.i.
6944:•  j.,  g.  ahmät  Adv.  I)  'inde';  i)  räumlich; nHt  käu  as  vaote  (sd.)  .  .  nBit  a'  vaiata ". ,  oon  inde  procedit"  P.  4^.  2)  zeit- lich, a)  'von  nun  an,  nunmehr':  ys . .  kayä (sd.)  a°  . .  7'ästryä  Y._jy.6;  — yä  a°  staota yasnya  irävayeni  "indem  ich  nunmehr  die StY.  aufsage"  Ny.4-S-  b)  mit  folgen-' dem  ya^a  und  fiiL  Konj.  'doncc,  bis  dass': aU'it  a'  yaha  ap?mgm  maniva  an  Aat mz'Ji/is  (sd.)  Y. 10.16.  U)  beim  Kompar., wörtL  'als  das',  was  i)  vorausgeht  oder 1)  folgt;  meist  unübersetzbar,  i)  zurück- weisend auf  zuvor  Genanntes  oder  Ge- sagtes: imaj  vS  jatöyemi  .  .  yalca  a°  asH miirya  ".  .  quodque  hoc  est  maius"  Y. 'jj.  14;  14'i  —  saisisca  .  .  oAqxitäiscä *ß-äyjblscal(sA.)ca  a-  Vr.  Ä  i.  a)  in Verbindung  mit  eil :  ayaaAaUtäis  kan- täis  paiti  azdibis  avaJitriäiyilt  {%^)  masyd vü  'mii-'i/V. 4. 50;  51,52.  2)  voraus- weisend auf  einen  Nebensatz  mit  &)yd:ia: yifnö  zqm  visävayat  afvit  irii'va  a'  mas- yefäm  ydia  fara  ahmai  Y.  2. 1 1 ;  —  nüit il  a-  *drajyS  *yätltn  framraemi  (sd.)  .  . äfrOIm  .  .  ya>a  .  .  V.33;  Yt.  I3. 64^;  — xraesyöJaraia  (sd.)  ri5  a'  ya>a  vikrkS raiÄfsd.)  Ißi/eV.  IJ.8;  —  näirivai/e.  .  «• pÖurum  '>  frantraomi  . .  ya%a  mayavö  (sd.) /ratäxsffit'V.4.^T,  47J.  h)  yäha  yat: itsit  vaakö  a'  fyao>amm  v»r^yeiti  ya'^a yai..karMt^.4S;^.iS.\o.  c)  yattsit: nSit  vanhs  a'  syao%tum   vtnsyeiti  yaüöil
7036:aahat  ästais  . .  ä°  yezi  aahaj  anäsiütS  . . V.^.40;  5.28-35",  7.13,  IS,  75',  ■^'■37, 99,  106;  —  yeüca  hz  anya  aya  fyao%na fravarita  .  .  ä'  yezi  //  .  .  rigij  fravarila Y.3.21;  Vd.2  aSt  ß)  yezi  .  .  aiwi.- srunvaili  .  .  yezi  J-  nsit  aiwi.surunvaiH N.  26;  60,  _jtV,  3Q,  iV(V,  g6,  100,  101, 104, 105,  54*>,  26  aSt.*',  (J5'>,  97S>; — yu  nBit öim  .  .  vääm  *aiwy<Is  . .  yezi  S°  öyum.pe väcim  *aiwyas  anaiwisH  (sd.)  .  .  N.  74; IQ.  4)  zur  Anknüpfung  eines  begrün- denden oder  erläuternden  Satzes  'denn; nämlich';  minyö  yö  parö.dari  .  ,  ä°  hS msrrfS  väcim  baraiti  Y.iS.i^;  —  sasta he  .  .  /rasnsoay^n  ä°  yat  he  zasta  mit framata  äat  (s.  7)  ,.  V.  1^.40;  —  mä  äi barg  (sd.)  agvS  yat  irisUm  ä°  yezi  sS  barai aivö ..  V.5.14.  5)  in  Säuen,  die  eine Aufforderung  oder  Wülensäusserung  ent- halten, 'so  .  .  denn',  oder  unübersetzbar: a°  mS  ahe  .  .  paräca  vaepaya  Y.  /o.  12; ra,  Yt5,77;  —  ä°  tum  ,.  nava  rnaya ni^wjnsöis  Y.iO.iS;  22.2,  9;  —  3°  vS kascil  .  .  isalta  Yt/5.53;  —  ä°  tbaHä taurvayeni  Yt. /4-4;  —  a° .  .yasami  Yt^. '3o>  131;  —  ä°  dis  avaioayamahi  Y. 4.aff.,  24.Z,  5.  55-^^  Yt.ii.i6,  ai;  ^.5, 11.31.  a)  hinter  dem  ersten  Wort  des Satzes:  imqm  ä'  sqm  .  .  yazamaidiY.^H. 1 ;  gg.  1 ,  a ;  —  alahya  a°  sairl  .  .  ädä (sd.)  Y.  JJ.8;  —  aZsmanqmat  3°  .  .  /ra- näsayata  A.  j,  s^  b)  in  anderer  Stellung: paoirlm  upa  may>m  haktrit  äpö  ä° kvqm  tanüm  pairtyaozdai'^Tia  V.p.31; 31.  6)  hinter  dem  Pron.  interrog.  wie
7038:satz'so,  dann;  da.' -.yezi ('wenn') aAipaurva.- naem3l  3'  mqm  avi.rimilnaya  (sd.)  Yt.16. 2;  a.  3-3,  Y.2.43,  ^'.36,  103,  /ö'.ii,Nik. 3,  Vd.  13';  —  yat  ('wenn')  yave  dayat ä'  datva  y^ism  (sd.)  V.J. 32;  321,  H.  2". 13,  N.  IJ2;  —  3at  (s.  8)  yat  apö  uzbargnte .  .  a°  fraiasinti  . .  fravasayö  Yt.  13.65; V.  Ä40,  i7.4;  —  yat  ("als')  mqm  tura pazdayatita  .  .  3'  az3m  tanüm  aguze  .  . \3at  (s.  3)  mqm  fraguzayanta  ..Yt  i7.  55^'; — yas}  tat  nmäfum  äk^rstmn  .  .  «7°  mqm tnairyö  akasat  dai  (s.  2)  .  .  fräksrmaot V.  22.  i£;  —  3at  (s.  8)  yat  miirtm  .  . /radaöqm   .  .   a°  dim  danqm  ,  .  Yt.  10.  i ;
7042:—  jfff  ('wer'  sva,  'wenn  einer')  i/irar/i  zn aiwi.v?r)zyHti  .  .  ä"  aoxta  Tm  za  nara V.^j.aö.  8)  Ohne  Beziehung  nach  vom oder  zurück,  einfach  satzeinleitend: aoxta  saraiiuärö  "es  sprach  Z"  Y./0.17, Vt.1.5,  3.2,  A2.I,  'Vyt24;  Y.21.3,  Aog. 57,  A'/D,  Vd./2,  20,  Yt.  ij.  54;  —  3° /ra/ssat  anävl . .  aal  (s.  2)  aoxta  ar»dvl Yt.5.  88;  7;  —  äat  aokU  haxa  haia  "es spricht  der  Freund  zum  Freund"  V.  18. 26; 18,  FrW./o.4i.  a)  bes.  vor  ya-,  yat, yezi:  ä°  ya/tmäi  xlnüts  bavatti  (sd.)  .  . ahmai  .  .  äat  (s.  3)  yahmäi  tbistö  bavaiti mihrB  ahmai  .  .  Yt./o.S?;  —  ä'  yg  na his  frayasaite  .  .  ahmai  .  .  "qui  vir  eas adorat  . .,  ei  . ."  Yt.y5.s1;  18,  P.57;  — ä'  yat . .  ipa  vä  . .  iriiiyät  iu'^a  . .  "wenn . .  ein  Hund  .  .  stirbt,  wie  .  ."  V.  .V.  1 ;  Yt. 6'.if.->,  7.4,  14.63;  —  ä'  yasp  %wapa'^qm (sd.)  Jasaiti  vahwassö  yezih  . .  a^a  .  . Yt/?.2o;  —  ä'  yat  apo  uzbarpnte .  .  äai (s.  7)  . .  Yt.  13.6si10.AZ,  ss;  —  ,r  yäl mi>rpm  .  .  /radaöam  .  .  äat  (s.  7)  .  .  "als ich  den  M.  schuf  . .,  da  . ."  Yt  to. ä°  yezi  anhat  äfs  . .  äat  (s.  3)  yezi  anhat urvara  V. 8. 1Ö4-6 ;  Vd.  2  i.,3.St  a)  ein- geschoben :  ye^he  hätam  ä'  yesng  (sd.)  . . vai%ä  .  .  yänhamca  ..  Y.2j.i$;  H.2.14
7263:Aufforderung  oder  Willensäusserung  ent- halten, 'so  .  .  denn',  oder  unübersetzbar: ä'    ml  ahe  .  .  paräca   vaipaya  Y.  /o.  12;
11081:Ordnung:  manahicä  vacakicä  syaoiansi Y.30.3.  Bj  zur  Anknüpfung  eines  neuen selbständigen  Satzes  'und'  oder  imüber- setzbar;  m  folgt  dessen  erstem  Wort  b)  im Aw.:  duwar>snat>hs  da/snyä  (sd.)  hsnts xaAyJcä  .  .  xraospTitqm  (sd.)  Ufa  .  .  tratä is  dra/sS{&d.)  ..  momc3(s±)  asta  Y.5J.8; —  atySs, .  akäl  (sd)  mananh3  st3  äirym drBjtucS  pairi.matsiscä  (Sp.564  m.)  syao- tnqm  ..  Y-32-  3;  —  aj  f3  mainyB  ..vaAyi aitmcä  (sd.)  äsca  hudarthS  prj/  vTsyatä "^i-SO-y,  7  (aimaua),  32. 1  {aüyacä),  45.  7, 4-.S  i'äc'a),  49T>  1°  {''^l^^)y  49-  S  {täim, S3-3  C^*"^^);  —  a^äca  "kiwä  Smavantaslä (Sp.  567  a)  buyamä  rapsUca  tä  HS  dan- gStncS  ustäca  (ßp.  568  m.)  Y.4i-4',  —  *i)mS janhtntu  yahmat  haca  ..snatiat,.  'hriiatca (sd.)  &ia  .  .  gStd  apajasat  .  .  aß  paurva 7'aMaKyai(sd.)  ..  aidaca (sd.)  ila  ..  sadayät V.2.22— 24;  —  hö  vTsp>m  ahüm  ..va?nai .  .  darfsta  ddiat  * amir^x^äntim  vispqm ..galiqm  Yt /p.94;  —  (Vnam  ..  sqm' .  . yazamaUe  yä  ni  baraitl  yäslä  tsi  gmi  . . tä  yasamaide  Y.  38. 1 ;  —  kyatca  mSt  tnraos ..at..\. 43.12;—  prssa^a  na  ..  Y.  43- 10;  —  avavaitya  ..ya^a  im  sk  astica  im xä  avaiti..Y.i9.T,  —  *vJsqs  *tac'a'^>  i'taä Mäm^lf  . .  vJsmte  "und  diese  zwanzig Namen  .."  Yt. /.  19;  —  dasa  ..  msrfhö sayana  dva  hamina  talla  fanii  sarata  .  . V.  J.3;  2.41;' JÄ65  (/ijÄi),  YL/5.  51 ifaifa),    Y.  19.  10  f.  {fltiaica),  8.  4,    ig.  6
11371:—  *anl?m}m{5d..)^ii  sat^h^m  F.3  e.  d)  im Nachsatz  hinter  yaUit:  yatät  vTmahim ssA.)  aiAhä  z?me  tsmäi  mihrö  hangrif- {itnnB  . ,  Yt.  10. 104  f  3)  einfach  her- vorhebend, meist  unübersetzbar"';  a)  im Ap.,    beim  Pron.  dem.:    Ayi^  duvaistam
13835:duh-arstimca  V.J.  20;  42,  Y.  77.  8,  7,  Yt /0. 106'';  —  hüxtahe  ahmt  'tahe  iiHi ahmt  Y.  /o.  16;  7/.  7;  —  nizbarimnB  .  . °l(ua  H.J.  7;  Fr\V._y.  I,  2;  —  aibigaityä äaßil  vJspä  . .  hüxta'ä  ,.pairirifyä  dai%t vlspH  . .  °tälä  Y.ii.iT,  —  yai  fraoirilaiti fairi  ..  -taiifyasc'a  H.  i.  ij;— paili//,U^ .  .  'tanqmca  Vr.  20.  2.
14133:•  j.  drajä-  f.  Name  eines  Flusses*':  'jya (IS.)  paiti  zbarahi  nmänakt  pourusoipahe "an  der  Z>r.,  auf  dem  Hügel  des  Hauses ^.s"  V.  /p-  4 ;  —  '}ya  paiti  zbarahe  "auf dem  Hügel  an  der  Dr."  V.if).  ii.
14860:AbleLt.  aus  "patan  Adv.  'im  Fing',  lum  V. pal-;  vgl.  BtHL.  BB.  /5.I9.  — Pü.i  väyantiai, —  1)  ZJtaHiAwverbindung  (lU  BB.  lO.  267); fasu  siaura  bilden  zusammen  das  i.  Glied, j.  patantam  Ab5oI,'>  'beim  Gehen'  (in ^ÄÄ/ischer  Art) :  ahmi..yim  sästa  datAhSus paf    va   zbar3tti3m    vä  .  .  "wenn    ein
15531:der  <i-DekI.  gebildet.  !  bal'azya  uzbarsm  paoirJs..  Syum  gaohrs-
16845:N.48;  —  uzbarayat  N.  2S.  >äiys  paraiaratH   dasa  (sd.)    V.  13.  10;
16896:mit  Abi.):  tä  ..  druj»m  nizbarät  asahe  haca gaihabys  Yt  ig.  93;  —  hyät  drva  gais hamistU  niSbfrtlö  haca  spirttahe  main- ySuidamabyS'^.8. 6.  4)'(ZJflÄ'isches)3'') abtun,  sich  losmachen  von  — '  (Akk.); Med.:  frastavans  humalaca  . .  niiba- r>mnff  duhnataca  ..  H. /.  7.
16914:mit  US  'hervorstlömen'  -.yat  äpB  uzbarmte ..  trt^anAai  hala  vourukasSt  ¥1^.65.
=== PHD zur ===
PHD.txt:125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
PHD.txt:217:arzómand [le wmnd | (N arjumand)] valuable, worthy. ~ih: value, worth. Arzür []zwl] a demon; a mountain at the mouth of hell. a-sag [?s?*k! | M *s?g] innumerable, countless. азап Pon! | N ~] at rest, easy, peaceful. “АП: rest, ease, peace. a-sar Dell endless. āsāy-, ~išn, v. āsūdan. a-sazāģ ["sc? k!] unfitting, unsuitable. a-sazisn|ig Dscfn-yk'] imperishable, permanent. ~ih: imperishability, permanence. a-sēj [Psyc] free from danger.
PHD.txt:424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
PHD.txt:661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
PHD.txt:680:žzēn [zyn! | N zin] saddle. zēn-abzār [zyn'pe!l | N zinafzár] horse-armour. zēnāwand [zy>zond] alert, vigilant. zēndān [zynd?n! | = M, N zindān] prison. «bān [-p?*x! | N -ban] jailer. ~ig [-yk! | N -i] prisoner. zënënidan, zënën- [zynyn-ytn!] look after, preserve. zēnhār [zyn)?] | N zinhàr] protection. zénig [zynyk!] armed. *zibāl [zb | N zībāl] swift (horse, etc.). zih [zyh | N zih] bow-string. zindag [zy(w)ndk! | M zyndg, N zinda] alive, living. ~th: life. zindakkar [zywndkkl | M zyndkr] vivifier, reviver. zinénidan, zinén- [zynyn-ytn'] damage, harm. zirak [zylk' | M zyr, N ~] wise, clever. zistan, v. ziwistan. zišt [zyst! | = P, N ~] hateful, ugly. ziwénidan, ziwén- [zywyn-ytn! | M zywyn-] vivify, revive. zi(wi)stan, zi(w)- [zyz-stn! | M zywystn, zyw-, N zistan] live. zi(w)išn [zywšn! | M zyysn] life; livelihood. ~ih: life, living. --6mand [-”xmnd] living, alive. ziyānaģ [zyd?nk'] young woman. zīyišn, v. zī(w)išn. zofāy [zwp'd | M zwp’y] deep; depth. *~ih: depth. ` zofr [zwpl | M zwwpr, J zwrf, (N žarf)) deep. —šy [2d] depth. ~-payag [-p'dyk'] deep. zóhr [zwhl | M zwhr] libation, offering. zor [z())wl | M zwr, N ~] power, strength. Bay ge J ~ig, ~dmand [-yk!, -wmnd | M -mnd, N —mand] powerful, strong. d z^ 201 [zwt! = Av. zaotar-] first officiating priest. ~ih: office of 201. Zraw-, v. zruftan. !zréh [zlyh | P zryh] sea, lake. *zréh [ziyh | N zirih] armour. zruftan, zraw- [zlwp-tn'] = azruftan. zūd [zwt! | M zwd, N ~] quick(ly). ^h : speed. zür [zwl | M z*wr] false, deceitful.
PHD.txt:682:zūr-ģuģāy [zw/gwk”dy | M zwrgwg'y] false witness. ~th: false testimony.
PHD.txt:683:zurwan [zwlw’n'] time; the god Time, Zurvan.
PHD.txt:5078:zūr, zūr zoromand zūrgugāy zūrgugāyīh zorig Zurwün zofāy zofāyīh zofr zofrāy zofr-pāyag zanjīr zanišn zētīh, zūdīh zot, zūd wahīgt ant
PHD_mackenzie.txt:558:add    hiig [HZWLYA < A ~zyr'; hwk' 1M hwg, N xugj pig.
PHD_mackenzie.txt:1204:Arzur ['Izwl] a demon; a mountain at the mouth of hell.
PHD_mackenzie.txt:3184:kann-zor [kmzwll N --] weak.
PHD_mackenzie.txt:5580:xiig [HZWL Y A < A lJ,zyr); hwk l IN . . . . ] pig.
PHD_mackenzie.txt:5861:ziir [zwll M ZC wr] false, deceitful.
PHD_mackenzie.txt:5864:zQ.r-gu~ay [zwlgwk)dy I M zwrgwg)y] false witness.
PHD_mackenzie.txt:5866:zurwan [zwlw)n l ] time; the god Time, Zurvan.
```


## [2026-09-06T02:16:00.797Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT ctx ===\"; sed -n '1320,1345p' KNT.txt; echo \"=== KNT zura lexicon ===\"; grep -n \"zūra\\|zura\" KNT.txt | head -20",
 "description": "Kent context on zura-kara"
}
```


### [2026-09-06T02:16:00.870Z] TOOL RESULT

```
=== KNT ctx ===
tigra- ‘pointed’, also in tigrarauda-; Tigra-, a fortress in Armenia; Tigrd- ‘Tigris’, borrowed from Semitic,
-gmata- ‘gone’, to root gam-, in pardgmaté hagmata Hagmatüna-.
Bagábigna- a man's name, see Lex. s.v.
Sugda- a Persian province, also Suguda with anaptyxis (8128).
But pIE -gh-to-, becoming -gdho-, plr. -gda-, was in OP replaced by -kt- (analogical to -gt- becoming -kt-): duruxiam ‘false’, pte. to pres. stem durujiya-, cf. drauga- ‘the Lie’ (palataliza- tion only in the present stem, where there is the suffix -jo-).
M04. PAR. б became & in Av. and OP (graphic ~Siy- in. OP, §25): pIE *g*iélo-, OP Sydta- ‘happy’, GAv. šyäta-
‘joyous’, Lt. quietus. pIE *q*icti-, ОР &уан- ‘happiness’, cf. Lt. quiés,
gen. quiél-is.
pIE *qieu-, OP a&iyava ‘he set forth’, Skt. deyavat, Gk. (Hom.) aor. éoveve ‘he put into motion’. 5105. Tas Crusren -s-é- appears in OP with
reduction to s in раза ‘after’, from pIE *po-sq*é:
cf. Av. paséa, Skt. pased. The evidence of Sasa- nian Pahlavi shows that this value alone is pho- netic in OP (Bv. Gr. §114), and that the -&- which is seen in some sandhi combinations, be- longs rather to Median: OP kaSevy ‘anyone’ from pIE *q*0s-q*id; manaš-clä] DNb 32 from *menos-
q*e. On züra-kara ‘evil-doer’ from *zurah-kara-,
see §119,
The sandhi product of -d c- has a similar varia- tion: OP s (not attested) and remade c (§130), Med. $c; there are the following examples: pIE *ed-q*id, ОР aciy ‘then’, Av. а/с. plE *7od-q*id, ОР yaciy ‘when’, Av. yatčit. pIE *g#d-gtid, OP cišciy ‘anything’, with Med.
38 OLD PERSIAN
šc; so also OP avasciy from earlier *avad-cid, OP aniyasciy from earlier *angad-cid. $106. PIE у remained unchanged in most IE languages, down into the recorded forms of the languages; exceptional combinations in which it suffered change in OP, are mentioned below. pIE *réto- ‘directed’, OP rästa- ‘straight’, Av. rasta- ‘upright’, Lt. тёсіо-. pIE *pro, ОР fra- (in cpds.), Av. fra, Skt. pra, Gk. тро. |
pIE "enter ‘inside’, ОР ачаг, Av. antara, Skt. атт, Lt. inter.
pIE *su-prek-to-, OP ufrašta- ‘well punished’, cf.
Skt. prechümz ‘I ask’, Lt. precor ‘I ask’. pIE *proterom, OP frataram, Skt. pratardm, Gk.
TpóTEpov. pIE root *dhreugh- in OP drauga- ‘the Lie’, Skt.
drihyait ‘he deceives’, Gm. iriigen ‘to deceive’. pIE *тотідо-, OP en ‘man’, Skt. mdrtya-,
ef. Lt. mortalis. pIE *ерлегопі ‘they bore’, OP abara”, Skt. dbha- ran, cf. Lt. feró.
OP т may come also from pIE у 7 (566, $68, cf. 6530-35), and from pIE ! | 1 (8107, 566, $68); but there are many ambiguities, since pIE r and pIE { can be distinguished only if we have a cognate outside the Aryan branch of IE. It is also difficult in many instances, to distinguish the original vocalie r and 1 from the original consonantal r and І (830-35).
For OP developments of pAr. ir, see §§78-9; of pAr. sr, see 5118.1. In borrowed names of persons and places, r is of frequent occurrence; e.g. Абита ‘Assyria’, Атафауа ‘Arabia’, Ufratu-
"Euphrates", Armina ‘Armenia’, Karka ‘Carians’,
in which the forms in other languages assure the т ав original at the time of borrowing.
=== KNT zura lexicon ===
1331:q*e. On züra-kara ‘evil-doer’ from *zurah-kara-,
```


## [2026-09-06T02:16:02.379Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"zür\\|zúr\\|zûr\" BRT.txt | head -20; echo \"=== search Unrecht Trug ===\"; grep -n \"Unrecht.*Trug\\|Trug.*Unrecht\" BRT.txt | head -10",
 "description": "Grep Bartholomae for zurah"
}
```


### [2026-09-06T02:16:02.478Z] TOOL RESULT

```
4628:Zu  angra-,  %  aj^.  3.   —   Pü.:   kt  züräk  (erl.r laiär)  hhtd. j.  anusvi  aiita  N.  707:  lies  anusavan/a.
5147:•  j.  ava'sdastö-fravaSay-  Adj.  etwa  'der die  Fr.  erzürnt  hat,  dem  die  Fr.  zUmea': ahwuuTjanam  anaiaottqm  .  .  'Hnqm  Yt /J.106.
5367:•  p,  arika-''  Adj.  'feindlich  gesinnt,  feind- sehg':  yaiia  naiy  °ka''  aham  naiy  drau- jana" . .  naiy  züra''kara''  Bh.  4. 1 3  i  —  ^/a*
5614:"T^*^  yüA"'^*-;  -.1  R  ■  .  -■  J'  i-  arazüra-  m.  Name  eines  Daei'a"^; ki>mp.i.:  »Ableit. —  Zur  idg.  Baals 'nr^T. 'nch-       ■"    oc-         ■.     i  n/-      c        1
9152:—  afrin>in  ifmiavät  Az,  2;  Vyt.  J  (wo k^rjnofilAi);  —  va!s  paoirlm  miirsm k^rmaoiti  V.J.3;  —  iian  (sd.)  hä  iiisläta iiryatii>  Yt.  10.  109;  —  ^fö  0ng  /rS.ga pa^mSng  hucistöis  (sd.)  *carat  (Konj.)9> ; \.4li.a,\  —  k(ii:a..  zarjm  (sd.)  (ar,l»r'>' kaca  xsmal  Y.  44. 1 7.  a)  mit  Adv,  statt Akk.:  II  ya^äsäm  hacärnJ"  d^ahyJ'  ara^^J *aJh/riavaya"li '^  Bh.  j.  S;  —  <iai  yimd ara'ia  k^rjfiaat ya'>a..'V.-J.$2.  h)  mit Inf.  als  Obj.:  yaf  kirsnaot..  c^airyqn  (sd.) 3far?i>m  ajyamnum  Y.'y.4; 75,16  {k}rma-\ rJni).  S- S.  2a)  mit  sksfuiem  'etwas' (Akk.)  zerbrechen,  zerstören';  shnd?m  (sd.) sl  mauö  k^nnüi'A  Y.  i/.  28.  b)  ;  mit züre^  'Jemandem  (Akk.)  Unrecht  tun': naiy  "sakurim  .  .  zür,^  (sd.)  akunavam Bh,4. 13.  c)  mit  ntazdam  Med.  'sich etwas  (Akk.)  ins  Gedächtnis  rufen,  recor- dari':  inasdqmcä  büirüä  (s.  bei  5)  ktrshul ,  .  xrapaitl  (sd.)  hyat  ahmat  aibi  Y. 40.  1 .  3a)  'Jemanden,  etwas  (Akk)  iiin- schaffea  zu  -,  verbringen,  versetzen  in  -'; a)  mit  Lok.  des  Ziels:  II  pasäva^dis a''ura^mazd<l  maiiä  dastayi  (sd.)  akunaus Bh,  4. 4,  1-)  mit  Lok.  eines  Nom.  act. zur  Umschreibung  des  Verbs:  vispqm  .  . taiiüm  ayao^dsta  (sd.)  k)rJiiaoiti  V.<V,4o;
11844:J^.  7  2 ;  —  nsit  kau  *'mS  yö  nsit  asa  *°mS P.  47  '* ;  —  'mumca  nmänö.paitlm  Yt  5. 8  7 10. 112,  /7.1z;  —  hsuca  'manam  tanci'tö P.25;  ~  hlu  (näml.  kaine)  ..'"ma  (NSf.) V./5,  30;  —  °mS'ä:raaaonB\t.^.(i\,  14-40, ig.  91;  87,  J.  105,  117,  /J.  99,  Vyt26';  Vt. 5.11,  Az.3;  Yt7jj.  28;5.  53,  58,  19,  42; ^■9^»  I03i  ■<'6'  •'^1  '37-  ^)amjsimam ippntanqm  ..  "manqm  Y.  26".  3;  —  vaini 'manqm  taxm5.t»m3m  Vt.  75.  57;  —  vätS "BiJ  V.j^i.  13,  Yt  J5.46,  Vyt.24;  Yt/0. 127, Y.7.  26,  S.2.30,  Y./.  IS,  2.  15,  7/.Z3;  Yt. JO.65,  140';  Y. 57.  II,  33',  j.  20,4-23.  V. J&I4,S./.  17;  —  vays 'ma  (VSm.)  Yt. 75.  57;  —  fravasls..  'mä  (AFS.)  . .  tana/ta Yt7j.  7s;  32,33;  —  aj  %7VS  mSnghai 'miniüä  spmltm  mazdä  "für  einen  starken und  heiligen  will  ich  dich  halten,  o  M." Y.  43-  4-  b)  von  Tieren;  vamsahe  .  . 'mähe  Yt.  74. 15;  —  -mähe  ttunyahe  Yt. 74.  36'. KompA,  E.;  Ableit.  —  Vgl.  tqsyai-,  lanHsla-. —  np.  lahm  'stark';  mp.  VgL  lak,  laklk;  ahd. vgl  digan  'Held'.  — Pii.:  taklk  (im  PPG I.  mit nhv  erklärt),  Npii.:  zürSvar.  —  ')  So  nach Pü. ;  lü  an  lakik  kl  nl  pa  akräkih  laklk.
15728:väiam  (sd.j  vazaUi  YL  ü.  33;  —  mmsu  (sd.) *°f^fl">(ADm.)a:"ak/?V./p.42.  2)9)  der Reihenfolge  (und  dem  Rang)  nach,  'der erslere':  ttaola  (sd.)  yanya  .  ,  'va/^^  vä naemat  aparät  vä  N._37;  —  yai  ki  avßi •rum'>  ubjyäite  (sA.)  V.j-sa  PQZ.;  —  cva^ haca  'rvaiibya*^  (läxcA.  majaHfya)?  ya%a %rig3im  V.p.  9;  Ä  39; —  aiwUa  apanm (sd.)  apäla  'voHbyai'i  V.iß.^S; — 'rvä^^ äätä  dämqn  aiaonXsY.iÖ.^;  —  upa  vä mq%r?m  sp^niitn  maraSa..  'rutiüa'^  naime asne  apanmca  ".  ,  die  erste  Hälfte  und die  zweite"  V.4.4S;  45;  —  'ruin*>  vä na^m^m  ^yän  apanm  väü.44; — mitAbl.: näirivaite..afimäi  •rum''>  {SSx\.)/ramraomi ya%a  May avB^sd.)^. 4.47.  A)iSTLpcururva als  Adv.  'zuerst';  'rva  hl  tamS  baraiti •n>a  oTannä  Yt/4^36.  3)9)  der  Zeit nach  'der  frühere,  erstere':  Xtyaiy  'ruvä xsäyähiyä  Eh.  4. 9;  —  anuzvarstä^  (sd.) paiü  'rvät^  V.4.  ao;  —  yafärS  *rvS^ uifhistaiti  "qui  prior  surgit"  V.iS.a6;  26, Yt  14.  44');  —  yatära  (sÄ)  vä  als  °rva'> (^Pm.) /räyatmU  Yt.rj.47;  lO.g  (NSf.); —  yahmal  hala  'rvS'ä  snao%S  (sd.)  .  . inalzät  V.2.  32;  —  'rvai'>  (NPol)  täyüm . .  bU^ySima&e  mä  Ä/  'rv5^''  büSiyaifa  nS Y.  p.  2 1 ;  a  I  \  F.  1 3»;  —  iaiärif  'rvö  (NPm.)J* amayäntei^)  V.7.36;37j  —  ava.jasnm (sd.)  -rvqm^  äpB  JaÜiyöt^  .  .  pasiaSa aiwyS  zaohrä  frabarOis  Y.  6^5. 1  o.  a)  Das Praesens  hat  dabei  den  Sinn  der  Ver- gangenheit"); j'?«  Toa^'f  (NPm.)  mihrwt druiinti  "die  zuvor  den  M.  belogen  haben" Yt  10. 45;  —  atibyS  .  .  ysi  vB  vanuhls  . . nHiJ  °rva^  (ASf.)")  äzärayente  "denen, die  euch,  ihr  guten, . .  nicht  zuvor  erzürnt haben"  YLy.30; — tä  sravä  ..yä'rva'^ al^rapalays  dnnjayan  (Sp.  773  o.)  V. 4.45;  —  ä  äim  aoxta..'rv3'*  asavapara.- iri^yB  (PPA.)  ". .  ein  früher  gestorbener Gläubiger"  H.  2.  16.  —  Aber:  ä  dim aoxta  .  .  'rv5''>  drvö  ava.mtrm  (PPfP.) ". .  ein   früher   gestorbener  Ungläubiger"
21203:—  aitatahqm  urvaranqm  y  IUn.H^ranqm Y.  Ä  7  5 ;  —  aSaesqm  y  daxmanqm  V.  7. 51;  Yt_5.  9, 13; —  aäanhqm  y  myazda- nqm  N.  ^2.  Anhang.  Auftallig  ist  die Wortfolge  (zu  c):  daiiikanqmcli  aidyünam hyat  urunayazamaidfY.3g,3*'>.  2)oluie erkennbare  Bedeutung;  A)imgAw.;a)vor clt  in  ya-  hyalclt  'quicunque'  (Sp.  593  u., 1230  u.):  yä  mazdd^a  (sd.)  hyatüt}^  vt- du!iY.30.\.  b)  vor  cä:  däröi  ahvä astvatascä  hyaicä^l  mananhS  ayapta(sd.) "vitarum  et  (vitae)  corporeae  et  (vitae) animi  fclicitatcs"  Y.  2Ä3;  —  varp^aitl  .. ratui  syaoianS  razistä  (sd.)  drigvataüä hyaicä^'^  *asaom  yehyaca  hsm>myasaill (sd.)  . .  Y.33. 1.  c)  zur  Einleitung  einer Aufforderung:  hy^  höi  hudsmSm  (sd.)  dyäi vax)lrahya  Y.2g.B.  b)  im  jA^p.;  zur Einleitung  der  Antwort:  kva paoirJm  aiiihä zsniB  asailtimi  ..  y^  arpzürahe  grivaya V.J.  7;  —  zur  Einleitung  des  Refrains: paiti  /ahikayai . .  kthrpjm  näämnäi  asaone . .  vadar»  jatäi  y'^^  hl  k»hrppm  . .  vadar> jaiii  Y.5.  33;—  sonst:  bval  vispB  ankul astvä  *azar>s5 ..  daryypm  _y'"  yave  vispai F._3  h;  —  daiiihSul  dairihupaUlm  bisatyai vähm  .  .  anjB  y'i'>  paoirlm  nmana/ie nmänäpaitlm  näirikqm  bHasyät  ka'hioa daSnu  arsjB  V.  7.  41  f.;  —  vTtasti.dra/s y'fi huSkanqm  (sd.)  .  .  aiiihS  s»mB  mdat^yqn V.  7.  29;  29f.3,  33  f.*;  —  das?mB  y  ahmi spanB  alvandasö  spanaauha  .  ,  lutvadasa y    ahmi   data   visqstPmB   ahmi  y    ahmi
26832:Ableil.  —  lEt,  s.  sfinia-.  —  Vgl,  spJnaA-.— Vä.:  aiBzürtiiTA i  s.  zu  sfinta-,
27777:•  j.,  g.  zar-  V.  'erzürnen',  Praea.  10  b sarariu-^\  11  b  zaran-",  13  zaranya-^'', 30  (Iter.)  zäraya-;  Perf.  i  zazar-'K  — PPfP.  tar^ia-,
27778:1)  Akt  'erzürnen':  anäisvä  nöii  ahurä inazda  asimcä yän3ii zaratialntäi^  manascä kyal  vahistim  "um  dieser  Gunstbeweise willen    möchten    wir  euch,    o  AhM,  und
27780:A.  und  VM.,  nicht  erzürnen"  Y.  2Ä9;  — drva    zaritS   YtiJ.  5.  2)    Med.   'sich
27781:erzürnen,  zornig,  ergrimmt  werden':  drvi zantS  zaranumanö*'*  zazarSnB'''  Yt II.  5;  —  mihrym  yim  ..  zaranimmm p3r3%ujafai3hs  vazmti  avi  kamayh  "M., den,  wenn  er  zUmt,  die  breithufigen  (Rosse) fahren  gegen  .  ."  Yt.  10. 47.
28216:•  p.  zürah-,  j.  zürah-  n.  'Unrecht,  Trug': naiy  "sakaurim  naiy  »^"kuvatam  °ra* akunavam  "weder  einem.. noch  einem.. Ut  ich  Unrecht"  Bh.^.  13''.
28219:•  p.  züra''-kara-  Adj.  ^Unrecht  tuend': naiy  'kan^  äham  £h.  4.13.
28220:•  j.  zürö.jata-  Adj.  'unrechtmässig,  ver- räterisch getötet*;  syävariami  (sd-,  Dat statt  Gen.)  -take  narake  Ytp,  18;  —  yat aae  ya  sfS.jata{^:)ca  .  .  'iala  V.  7.  3.
28364:•  p.  naiy   "Sakaurim    naiy   ^^"huvalam züra''  (sd.)  akunavaiu  Bh.  4. 1 3.
28365:Vgl.  zu  zürah:  Jn.  JAOS.  24.  92  versichert, es  stehe  tatsächlich  iH'ui^ill:)m''  auf  dem Stein.
29986:•  j.  ha,m.bBr«9'a-  n.  'Versammlung':  cim ''ha  (AP.)  hqmMrayama  (sd.)  ..arszürahe paiti  kam3r3%3m  V, /p.  44;45.
30072:irüt  . .  u  züräk  ntfnüi  *«'  oiärTA  i  i*«  u eiitiUan  i  drvan  ape  dil  starl  iäl.
=== search Unrecht Trug ===
28216:•  p.  zürah-,  j.  zürah-  n.  'Unrecht,  Trug': naiy  "sakaurim  naiy  »^"kuvatam  °ra* akunavam  "weder  einem.. noch  einem.. Ut  ich  Unrecht"  Bh.^.  13''.
```


## [2026-09-06T02:16:09.757Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 168 (p.147) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==169' HRN.txt | head -60",
 "description": "Horn page 147"
}
```


## [2026-09-06T02:16:10.885Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ghuk ===\"; grep -n -i \"ghūk\\|ghuk\\|ghukos\\|gucken\" IEC.txt | head -20",
 "description": "Grep Mann IEC for ghuk"
}
```


### [2026-09-06T02:16:11.418Z] TOOL RESULT

```
=== HRN leaf 168 (p.147) ===
— 147 —
LW. kurd. zirt, zir/ * Panzer ; af;'. zira; bei. zirili
(306); arm. zrah.
Urverwandt mit afy. zyara * Kettenpanzer', oss. zyär
Tanzer (132) ?
%l, liieryiin gelbfarbig.
aw. zairi.gaona- gelbfarbig'; phlv. vergl. zarlnqün
(vd. 2 (67)).
Vergl. np. öün aus *cigün (No. 450) und aöenjiin,
G62. »ist 'schlecht, schimpflich*, zistür.
Kää. Z. jist (auch s. v. bed).
aw. jlstayamna- (y. 8, 3) Verachtend, vorspottend'
(Geldner, 3 Yasht, 128ji); phlv. zist 'hässlich' (Men.).
af/. LW. zl/t; sar. ir^ Verdorben, schlecht, hässlich'.
663. zefer, zefr *Mund' (8ähn. I, 195, 1189).
aw. zafar- 'Rachen ; phlv. znfar,
Muss dialektisch sein, da die reguläre Form np.
dehan (No. 589) ist.
664. i^elTi, zalü 'Blutegel', zerü (AM. 180 Zeile 2 v. u.).
skr. LW. (?) Jalüka-, jaluka-, Jalikä- 'Blutegel*
(Bütticher, Arica 67).
kurd. zdü, zuliil, zalüg, zürT; af/. LW. zallü 'Blut-
egel', echt zavara\ bei. zaray (417).
Gegen Curtius' Zusammenstellung mit lat. hirüdö,
air. gil vergl. Hübsch mann, ZDMG. 38, 424.
665. zelle^ ziUe 'Grille, Heimchen'.
skr. jhillikCL', jhillU Grille, Heimchen' (Hübsch-
mann, ZDMG. 38, 424).
666. xeni 'Kälte', zemistan 'Winter.
aw. zyao- 'Winter', Gen. ziniö; phlv. zam 'Winter'
(vd. 2 (20)), zam(i)stan; ai. himä- 'Winter ; arm. vergl.
jiun 'Schnee', jmern 'Winter', jmerem 'überwintern
(H. No. 178).
oss. d. zumägy t. zimag 'Winter' (135); af/. zimai;
wa;^. zam, zamin (Adj.), sar. zainän, zamämn (Adj.),
si/n. zimjy zinj 'Schnee'.
) vt. 19, 42 ]int die neuo AuRfj^abe harözuiiem.
10*
```


### [2026-09-06T02:16:11.475Z] TOOL RESULT

```
=== IEC ghuk ===
5051:ghükos (ghuk-) ‘hoot, whoop’ Skt. ghükah ‘owl; Per. yük ‘frog; R gik ‘whoop’; gikať, v. id.; Cz. (*-u-) hek ‘groan’ beside hykat ‘bray’; cf. R variant zyk (‘dim fr.
5061:*&hük-); Cz. heslo (^slogan', fr. *ghukslo-?); MHG gucken, v. (‘cuckoo’ fr. *ghug-). Extn. in Li. gükCioti ‘sob’
19547:-ukos, dim. extn. Cf. Skt. laghukah ‘trivial, light’; lambukah, m. “an astral yoga’; píthukah, m. ‘scalded rice; youngster’; Arm. man-uk, s. ‘child’; Gk. plat- ukós, adj. ‘broad’; OCS Iíg-ükü, adj. “light; list-ükü, m. ‘leaflet’; Li. dant-ükas little tooth"; Latv. te]-uks, m. “runt, undersized calf
```


## [2026-09-06T02:16:19.443Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN zur ===\"; grep -n \"zür\\|zur '\\|zür-\\|Lüge\" HRN.txt | head -30",
 "description": "Grep Horn for zur / Lüge"
}
```


### [2026-09-06T02:16:19.521Z] TOOL RESULT

```
=== HRN zur ===
640:ahmend, azver {äzür),
648:äzartan etc.; ai. [/har- 'zürnen.
3992:sieden; aufbrausen, zürnen' (181).
5015:557. iliiröy, deröy 'Lüge; unwahr.
5016:ap. drauga- *Lüge*; i\\^\ draoya'\ phlv. dröy, dröy,
5870:kurd. zdü, zuliil, zalüg, zürT; af/. LW. zallü 'Blut-
5945:674. zur 'falsch; Lüge*.
5947:zür]zat, zür]ynhäsih, arm. LW. zur\ ai. hvaras-.
5983:kurd. zahr, zäir, zur 'Gift' ; af/. bei. (297) LW. zahr,
8597:8än; kauk.-bergjüd. zürnai sonst sürnm u. v. a. m. Umgekehrt steht
17301:zürgukästh 674.
17303:zürzat 674.
19374:/azür 486.
```


## [2026-09-06T02:16:20.419Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5040,5065p' IEC.txt; echo \"=== leaf of line 5051 ===\"; awk 'NR<=5051{n+=gsub(/\\f/,\"\")} END{print \"form feeds before:\",n}' IEC.txt",
 "description": "IEC context and leaf number"
}
```


### [2026-09-06T02:16:22.182Z] TOOL RESULT

```
ghrt- ‘thrus? (?), ‘coerce’ (?). (Variant *ghrst-?) Arm. gahem (strike, thrust’, phon. of mah ‘death’, fr. *mrt-); Lat. (?) hortor, ari (urge on”, beside a variant (?) hostio, ire ‘strike’ of type *ehrst-, cf. hostorium *strickle'; hostia “vic- tim’; Srb. (?) cf. grčem, grtati ‘scrape together”. Obscure; possibly two roots, and for Srb. cf. Lat. co-hors, -hortis
ghub- “peak, pile'. Variant of ghubh- (1), q. v. Oss. (ambig.) cf. gubank, Dig. gobat *mound, hillock’; MHG gupf, e wm., guphe, f. “peak, top, tip'; G Gupf, id.; cf. MHG goffe, guffe, f. ‘buttocks’; Li. (ambig.) gubà ‘shock of shea- ves?
ghubho, ið (1) “bend, hollow?. Cf. ghoubh-, ghubhos (1) & (2) Oss. cf. gubín, gubun ‘stomach’; Lyc. gupo (or gubo), gupu ‘tomb’; Arm. cf. gub, gs gbo ‘pit’; Gk. küptoó, pf. kékupha ‘bend’; kûphos ‘bend; vessel, container’; cf. küphós ‘bent, hunch- backed’; OCS cf. sü-gübü “arm? beside sù-
347
gybü (*-ü-) joint’; OCz. o-hnúti, aor. 3s o- heb ‘bend’; Cz. cf. zá-heb, gs -hbu, m. id.; Pol. cf. giac, inf. id.; Li. cf. dvi-gubas, tri-gubas *two-, three-fold’. Extended forms in Tokh. kupar ‘deep’, and Gk. küphaléos ‘bent’. Nasa- lized in Li. gumbu, inf. gübti ‘bend’
ghübhó, ið (2) ‘move’. Same as (1)? Sw. cf. lyckt-gubbe *will-o-the-wisp; OCS gybljo, gybati *move', & com. SI.
ghübhos, à (1) ‘hump, lump’. (Same as next? Cf. dholos for semantics) Oss. cf. gubank, gobat ‘mound’; Gk. küphos, n. (2) ‘hump, tumour’; OE guba ‘buttock, flank’; Norw. cf. gubbe old man’; Li. gubà, Latv. guba ‘pile, stook’; Cz. cf. o-heb, o-hyb ‘hump; bend’
ghübhos (2) “bent; bend’. Same as (1)? Also “hollow?. Cf. ghubh-, ghoubh- Oss. gubín, gubun “stomach, belly”; Arm. gub, gs gbo ‘pit, ditch’; Lyc. gupo (or gubo), gupu ‘tomb’; Gk. (*-ü-) küphós ‘bent, hunched' be- side küphos, n. “bend; hollow vessel’; OCS sü-gübü ‘arm’, beside (*-ü-) sü-gybü ‘joint’, and (*-ou-) sá-gubü “double”; cf. also gybükü ‘flexible’. Cf. WP I, 357 & 567
ghüdos (ghudsos) (?) ‘rascal’. MLG güte *demon, goblin'; Du. guit, Fris. gut ‘scamp’; Norw. gutt ‘boy’; Li. güdas 'scalliwag; outsider; White Russian'. The extended form occurs in Alb. goc ‘boy’, gocë ‘girl’; in Sw. gosse, wm ‘boy’ and in Fr. gosse, mf. ‘boy; girl', but the route taken by this wd. is un- certain (Moeso-gothic?). Cf. also Li. gudà *bo- gey'
ghugh- see Supt. and ghugh-. Slovak hegnüt ‘shake, jolt’ has an unusual phonology: -g- for expected -h-)
ghügh- hideous; monster’. Cf. gügh- Skt. cf. guhah ‘name of a god’; EMDu. guig ‘grimace’, ON gygr, pl. gygjar ‘hag’; Cz. cf. hyzd, o-hyzda ‘ugliness’; Li. güZë ‘goddess of travel'. (The semantics of the last, and of Srb. gizda ‘charm’ are obscure). (Lusat. hida ‘hate’, hidżźić, v. id. suggests a variant *ghüdh-)
ghükos (ghuk-) ‘hoot, whoop’ Skt. ghükah ‘owl; Per. yük ‘frog; R gik ‘whoop’; gikať, v. id.; Cz. (*-u-) hek ‘groan’ beside hykat ‘bray’; cf. R variant zyk (‘dim fr.
ghübhó, ið — ghundhos (ghundholos), à
20
25
30
35
40
45
 
348
*&hük-); Cz. heslo (^slogan', fr. *ghukslo-?); MHG gucken, v. (‘cuckoo’ fr. *ghug-). Extn. in Li. gükCioti ‘sob’
ghül- (1) “stir, swell Skt. ghürnami ‘sway’; W gil “ferment (i-st.); Icel. gúll ‘puffed cheeks’; OCz. po-hyliti, v. ‘engulf; R at (bombast’, for sense cf. G Wort-schwall). Short vowel in ON gul, gol, Mod. gola ‘breeze’
ghül- (2) ‘stunted; stump’ (?). Cf. gül- Arm. gul, gs gli, i-st. ‘blunt’; MHG gül ‘mon- ster; beast; boar; nag’; Du. guil ‘nag’
ghuldos (ghuldius) ‘male animal, castrated animal” Skt. huduh ‘ram’; G Golz ‘castrated sow’; E gilt ‘young sow’; ON gyltr, m., gylta ‘young sow, piglet’; Sw. gylta, f. ‘young sow’; Norw. cf. gold (for *golt, via Danish?) ‘barren’
ghulgh- “lump, clump’. (?ghlugh-) Per. gurz “club, mace’; Arm. guydz, guydzn ‘clod’. (Isophonic is Oss. gurdz embryo?)
=== leaf of line 5051 ===
form feeds before: 203
```


## [2026-09-06T02:16:28.668Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5935,5960p' HRN.txt; echo \"=== leaf ===\"; awk 'NR<=5945{n+=gsub(/\\f/,\"\")} END{print \"ff before:\",n}' HRN.txt",
 "description": "Horn entry 674 zur context"
}
```


### [2026-09-06T02:16:30.368Z] TOOL RESULT

```
hierher 0. Vergl. Hörn, KZ. 32, 583 No. 13 2).
672. xinüden, zunüden *heulen , Praes. ziuec-em, ztmöylden.
ai. [/'nav-j naiiti, ndmite *brüllen (von Tieren)', mit
accha 'zurufen' (mit ud kommt es nicht vor).
Vergl. np. nöyiden etc. (No. 1054).
673. xüd 'schnell'.
aw. \/jav- 'eilen*, Java, javarö (?, Geldner, BB.
XIV, 21, 22, aber auch KZ. 30, 533); phlv. zät (päz.
zöt); ai. i^jav-, jdvate *eilen*.
kurd. zu; bei. züt^ zU, n. zid^ (430).
674. zur 'falsch; Lüge*.
ap. zurah- {znrah-) ; aw. zurö.Jata- ; phlv. zur,
zür]zat, zür]ynhäsih, arm. LW. zur\ ai. hvaras-.
Bartholomae, zuletzt ZDM6. 46, 296, Ilübsch-
mann, gleichzeitig ib. 329.
674*»^'* {\)»ör 'Kraft, Gewalt' (reimt auf hör, Sahn. I, 202
Vers 1311).
aw. zävar- 'Macht, Kraft*; phlv. zör, zörlh, arm.
LW. zatir^ zaurcwor, zauruüun,
LW. kurd. afy. bei. (312) zör.
675. {^i)zör 'Weihwasser (pärsisch).
aw. zaotirä' 'Weihwasser*; phlv. zölir, zur, arm.
*) Im Ossctisclicn bezeichnet das L W. zjndon *Höllc* (v o n
Stack elberg, Baltische Monatsschrift, XXKVIII, lieft 8, 674).
*J Herr Prof. Nöldeke vermag zindän mit plene geschriebenem
i bezw. e im Pehlevl zu belogen, was für die Richtigkeit der obigen
=== leaf ===
ff before: 170
```


## [2026-09-06T02:16:38.252Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==171' HRN.txt | head -5; echo \"--- leaf 169 head ---\"; awk 'BEGIN{RS=\"\\f\"} NR==170' HRN.txt | head -3",
 "description": "Check Horn leaf page headers"
}
```


### [2026-09-06T02:16:39.820Z] TOOL RESULT

```
149
Der Bedüutungsunterschied macht diese Zusammen-
stellung bedenklich.
671. niindän 'Gefängniss'.
aw. *2:aewa.d(2wa- (y) ; ^\\\\, z(i)ndan (PPöl.); arm.
--- leaf 169 head ---
— 148 —
Daneben auch allgemein entlehnt, kurd. afy. zamistän,
bei. zamisiän, :^imisfän, zavistän (414), sar. zümistän,
```


## [2026-09-06T02:16:48.791Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB zur ===\"; grep -n \"zūr\\|zur '\\|zurah\\|hvaras\" HUB.txt | head -20; echo; echo \"=== FVQ zur ===\"; grep -n -i \"zūr\\b\\|al-zūr\\|zur\\b\" FVQ.txt | head -20; echo; echo \"=== PLA zur ===\"; grep -n -i \"zūr\\|zur\\b\\|tazwīr\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20",
 "description": "Grep Hubschmann, Jeffery, Asbaghi"
}
```


### [2026-09-06T02:16:48.903Z] TOOL RESULT

```
=== HUB zur ===
7868:np. paz. phi. zur *falsch, Ltige', arm. zur, ap. zurah-
7869:'Unrecht', zurakara- *der Unrecht thut\ zd. zurah- in zuro-
7916:im Armenischen: zoh *Opfer, zur 'ungerecht', zaur 'Heer',

=== FVQ zur ===
246:Ein Beitrag zur Frage uber die Fremdworter im Koran. Mimchen, 1884. 
296:Abhandlungen zur arabischen Philologie. Leiden, 1896. 
319:Beitrdge zur Erkldrung des Koran. Leipzig, 1886. 
394:Leszynsky, R. Die Juden in Arabien zur Zeit Mohammeds. Berlin, 1910. 
414:' ? Zur EntzifFerung der thamudeniseheii Inschriften," MVAO. Berlin, 1904. 
428:Mordtmann, J. H. Beitrage zur mindischen Epigraphik. Weimar, 1897. 
448:Neue Beitrage zur semitischen Sprachwissenschaft. Strassburg, 1910. 
452:Geschichte der Perser und Araber zur Zeit der Sasaniden. Leiden, 1879. 
483:Rhodakanakis, N. " Zur semitischen Spraohwissenschaft," in WZKM, xxv. 
551:Vollers, K. " Beitrage zur Kenntniss der lebenden arabischen Sprache," in ZDMG, 
6204:8 Zur Urgeschichte der Armenier, 1854, p. 813, and Armenische Studien, 1877, 
8271:tion of ttf*n and D"n. " Zur Radix ^^ ist naohzutragen, dass in ihr VEF^\ und 
9247:5 " ^JJ ^ * ine Wtymulogio : zur Bcdeutung ist hier nur daran zu orirmorn, 
9853:(Zur). 
9894:Phlv. both simply as JyS zur, a lie, falsehood, fiction, 2 ' and in com- 
9896:pounds as ^OO^^Vr zur-yukawh = false evidence, perjury? 
11872:Proper Names, p. 91, and Uaudissin, Studien zur semitischen Religionsgeschichte, i, 
17718:3 On this form of the name sec Marquart, Untermchungen zur Geschichte von Eran, 
17722:gigkeit, 67, 75 ; Fr. Miiller, in WZKM, viii, 278. Marquart, Untersitchungen zur 
21147:zur 156 

=== PLA zur ===
780:lassen sich auf die großen Veränderungen zurückführen, die diese Wörter 
830:zu welchen mittel- bzw. altiranischen Sprachen das Wort zurückgeführt 
1980:arzur fa. FAR arzür "ein Dämon, ein Berg in der Hölle" vor ”, 
2052:„)-  azur: Pl. v._„ zur q. V. 
3253:5 zur - - 
3950:"bis zur Türschwelle begleiten od. empfangen". 
4150:por-zur "stark" mp. dio purr "voll" + ),s zür "Stärke, Kraft" 5, 
4472:„4-?r - buzurß-mihr "Anuschirwans Großwesir" aus dem pers. 0. buzurg- 
5297:aß - udarömihr = buzurfmihr s. buzurämihr . 
6704:les - Zurßäni: Nisba v. Olss Zur&an s. Zur%än . 
6705:on»lo,s - Zur&äniyya: ein Dorf in Choresm. aus dem pers. „nl gurgäanag 7, 
6958:>» - $uzur: Pl. v. Bazr s. $azr. 
10975:>2,- zurüd: Pl. v.2„, zarad q. v. 
11072:Zur) - zanburk: "ein Teil der Uhr" aus dem pers. ER zamburak 8, 
11328:+» - zur: "Lüge" <T pers. „, zur 7 mp. Is zur er. zürah "Übeltäter". 
11331:zn» - Zur: "Kraft" aus pers. zur 8 mp. Is zor, zawar aw. zavar 
11790:—lw- saräb = Zuräb a. v. 
11827:L sarädar zurück. *. 
13828:"Urkunde, Vertrag" zurück 3, 
14432:zur - tarz: "Form" pers. ); tarz 9,
```


## [2026-09-06T02:16:56.518Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9845,9905p' FVQ.txt",
 "description": "Read Jeffery FVQ entry on zur"
}
```


### [2026-09-06T02:16:56.572Z] TOOL RESULT

```
built therefrom. It was from this Syr. that we get the Eth. }\Gh*l 
(Noldeke, Neue Bcitrdge, 44) and the Arm. ^j/^g, 4 and it was 
probably from the same source that it passed into Arabic. One might 
expect that it would be an early borrowing, and as a matter of fact 
it occurs in the early poetry. 5 

^ > 

(Zur). 



xxii, 131 ; xxv, 5, 72 ; Iviii, 2. 
Falsehood. 

It is linked with idolatry in xxii, 31, but in the other passages 
is quite colourless. 

1 Fnienkel, op. cit, 100 ; Vollera, ZDMfl, 1, 6J ; li, L>98 ; Ptfm, 1094. 

8 Cf. Lat. htngerc and tho Av. ^LjJJJ ( Bartholoiuao, AIW, 1228; Iteichelt, 

Elemcntarbuch, 477). 

3 Sco Meinhold's Yorna (1913), p. 29 ; Krauss, (Jricchische Lchmvorter, ii, 240-242. 

4 HubHohmaim, Arm. Gramm, i, 302 ; ZDMG, xlvi, 235. 
fi Cf. 'Antara, xxi, 31, in Ahlwardt's Divans, p. 46. 



156 FOREIGN VOCABULARY OF THE QUR*AN 

The usual theory of the philologers is that it is derived from 

though this is clearly a denominative, and that the aiithorities felt 
some difficulty with the word is clear from LA, v, 426. 

Fraenkel, Frewdiv, 273, suggested that it was from "IT. 1 There is 
a Heb. word KIT loathsome thing from TIT to be loathsome, but it 
seems hardly possible to derive the Arabic from this. It would seem 



rather to be of Iranian origin. Pers. jj j is lie, falsehood, which 

Vullers, Lex, ii, 158, gives, it is true, as a loan-word from Arabic. He 
is certainly wrong, however, for not only does the word occur in 

Phlv. both simply as JyS zur, a lie, falsehood, fiction, 2 ' and in com- 

pounds as ^OO^^Vr zur-yukawh = false evidence, perjury? 
and in the Fazcnd znr, a Zt>, 4 but also in the O.Pers. of the Bchistun 
inscription (where we read (iv, 63-4) naiy draufana aham, naiy 
zurakara dJiam, " I was no liar, nor was I an evil doer/ 1 and further 
(iv, 65) naiy . . . zura akunavam Vk I did no wrong"), 5 and in the 
Av. u^utg^J'K zurdfaa* From Middle Persian the word 

was borrowed into Arm., where wo find qjn-p false, wow/, 7 which 
enters into several compounds, e.g. i^/m/pu/k calumimtor, ^/i^u*V/^ 
injustice, etc., so that it was probably directly from Middle Persian
```


## [2026-09-06T02:17:29.497Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD watkins ghwel ===\"; grep -n \"ghwel\\|gʷhel\\|ghwel-\\|false.*fail\\|fallere\" AHD_watkins1985.txt | head -20; echo; echo \"=== KLN false ===\"; grep -n \"fallere\\|fallō\\|falsus\" KLN_1966.txt | head -20",
 "description": "Grep AHD and Klein"
}
```


### [2026-09-06T02:17:29.568Z] TOOL RESULT

```
=== AHD watkins ghwel ===

=== KLN false ===
14304:faience,  n.,  a  fine  kind  of  painted  and  glazed porcelain.  —  F.  faience,  shortened  fr.  original vaisselle  de  Faience  (‘vessel  of  Faenza’),  fr. Faenza,  name  of  a  town  in  Italy, fail,  n.,  failure.  —  ME.  faille,  faile,  fr.  OF. faille,  faile,  fr.  faillir.  See  fail,  v. fail,  intr.  and  tr.  v.  —  ME.  faillen,  faile n,  fr.  OF. (=  F.)  faillir,  fr.  VL.  *fallire,  corresponding  to L .fallere,  ‘to  deceive’.  See  false  and  cp.  faucet, fault.
14330:fall,  n.  —  Fr.  fall,  v.  In  the  sense  of  ‘autumn’, fall  is  short  for  ‘the  season  of  the  falling  leaves’, fallacious,  adj.  —  L.  falldcidsus,  ‘deceitful,  de¬ ceptive,  fallacious’,  fr.  falldx,  gen.  fallacis, ‘deceitful’;  fr.  fallere,  pp.  falsus,  ‘to  deceive’. See  false  and  -acious.
14331:Derivatives :  fallacious-ly,  adv.  ,fallacious-ness,  n. fallacy,  n.  —  L.  fallacia,  ‘deceit,  artifice,  strat¬ agem’,  fr.  falldx,  gen.  fallacis.  See  prec.  word and  -y  (representing  L.  -ia). fallal,  n’.,  a  bit  of  finery.  —  An  invented  word, fallalery,  n.,  valueless  finery.  —  Formed  from prec.  word  with  suff.  -ery. fallen,  pp.  of  fall.  —  ME.  fallen,  fr.  OE.  feallen, ‘fallen’,  fr.  feallan,  ‘to  fall’.  See  fall,  v. fallible,  adj.  —  Late  L.  fallibilis,  fr.  L.  fallere, ‘to  deceive’.  See  false  and  -ible.
14336:(F.  faux,  fem  .fausse),  fr.  E.  falsus,  pp.  of  fallere, ‘to  deceive’,  which  is  of  uncertain  etymology.
14338:Derivatives:  false,  adv.,  false-hood,  n.,  false-ly, adv.,  false-ness,  n.,  falsify  (q.v.),  fals-ity,  n. falsetto  n.,  an  artificial  voice  (mus.)  —  It., dimin.  of  falso,  ‘false’,  fr.  L.  falsus.  See  prec. word.
14342:falsity,  n.  —  OF.  falsete  (F.  faussete),  fr.  Late L .falsitatem,  acc.  of falsitas,  ‘falsity,  falsehood’, fr.  L.  falsus.  See  false  and  -ity. falter,  intr.  v.,  to  waver.  —  ME.  falteren,  of  un¬ certain  origin.
14453:faucet,  n.,  a  tap  for  drawing  liquid.  —  F .  fausset, 'vent  plug",  fr.fausser,  ‘to  make  false,  to  falsify", fr.  Late  L.  falsdre,  fr.  L.  falsus.  See  false  and  -et. faucitis,  n.,  inflammation  of  the  fauces  (med.)  — A  Medical  L.  hybrid  coined  fr.  fauces  and  -itis, a  suff.  of  Greek  origin.
14456:silicate  (mineral.)  —  Named  after  the  French geologist  Barthelemy  Faujas  de  Saint-Fond (1741-1819).  For  the  ending  see  subst.  suff.  -ite. fault,  n.  —  ME.  faute,  fr.  OF.  (=  F.)  fame,  fr. VL.  *fallita,  fern.  pp.  of  fallere,  ‘to  deceive,  dis¬ appoint;  to  fail’;  see  fail,  v.,  and  cp.  default. The  l  in  fault  is  intrusive  and  was  originally mute  in  pronunciation;  its  insertion  into  the word  is  due  to  the  influence  of  L.  fallere.  For the  insertion  of  the  /  cp.  vault.
```


## [2026-09-06T02:17:31.641Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK ghuk? ===\"; grep -n -i \"ghūk\\|ghuk-\\|gucken\" POK_full.txt | head -20; echo; echo \"=== WLD ghuk ===\"; grep -n -i \"ghūk\\|ghuk\" WLD_band3.txt incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt 2>/dev/null | head -10",
 "description": "Grep Pokorny/Walde for ghuk"
}
```


### [2026-09-06T02:17:31.758Z] TOOL RESULT

```
=== POK ghuk? ===

=== WLD ghuk ===
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:35678:Ai. gilhati , guhdti ,.versteckt“ (Aor. aghukkd), guild ,.Versteck, Hohle",
```


## [2026-09-06T02:17:42.969Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD 'false' ===\"; grep -n \"false, from Latin falsus\\|fallere\\|To be false\\|ghwel\" AHD_watkins1985.txt | head -20; echo \"=== AHD gwhel-ish headwords ===\"; grep -n \"^ghwel\\|ghwel\" AHD_watkins1985.txt | head; echo \"=== search 'gh w el' ===\"; grep -n -i \"krumm\\|crooked\" AHD_watkins1985.txt | head -20",
 "description": "Search Watkins AHD for the root"
}
```


### [2026-09-06T02:17:43.070Z] TOOL RESULT

```
=== AHD 'false' ===
=== AHD gwhel-ish headwords ===
=== search 'gh w el' ===
284:tives: a. ekhinos, hedgehog (< “‘snake-eater”): ECHINO-, ECHINUS; b. ekhidna, snake, viper: ECHIDNA. [Pok. ang#(hji- 43.] ank-. Also ang-. To bend. I. Germanic *ank- in Old Norse *ankula and Middle English ancle, ankle: ANKLE. Il. Suffixed form *ank-ulo-. 1.Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE!; b. prob- ably Latin Angli, the Angles: ANGLE. 2. Greek ankulos, crooked, bent: ANKYLOSIS; ANCYLOSTOMIASIS. ITI. Greek ankura, anchor: ANCHOR. IV. Greek ankdn, elbow: AN- CON. V. Sanskrit anka, hook, avicati, he bends: PALAN- QUIN. VI. Suffixed variant form *onk-o- in Latin uncus, hooked, bent: UNCINARIA, UNCINATE, UNCINUS, UNCUS; UNCIFORM. VII. Suffixed form *ang-olo- in Latin angu- lus, angle, corner: ANGLE*, [Pok. 2. ank-, ang- 45.] ano-. Ring. 1. Latin dnus, ring, anus: ANUS; ANILINGUS. 2. Latin diminutive annulus, ring, signet ring: ANNULAR, ANNULET, ANNULUS. [Pok. dno- 47.] ans-. Loop, handle. Latin dnsa, handle: ANSATE. [Pok. ansa 48.] ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse dss, god: AEsIR. 2. Suffixed reduced form *nsu-ro- in Avestan ahura, spirit: AHURA Mazpa, Ormazp. [Pok. ansu- 48.] ant-. Front, forehead. I. Inflected form (locative singular) *anti, “against,” with derivatives meaning in front of, before; also end. 1. Germanic *andi- in Old English and-, indicating opposition: UN-?; ALONG. 2. Germanic *andja- in Old English ende, end: END. 3. Latin ante, before, in front of, against: ANCIENT!, ANTE, ANTE-, ANTERIOR; ADVANCE. 4. Greek anti, against, in enantios, opposite: ANTI-; ENANTIOMER, ENANTIOMORPH. 5. Compound form *anti-oko-, “appearing before, having prior aspect” (*akw-, appearance; see okW-), in Latin antiquus, former, antique: ANTIC, ANTIQUE. 6. Reduced form *nti- in Ger- manic *und- in Old Norse und (> Middle English un-), until, unto: UNTIL. 7. Variant form “anto- in Sanskrit antah, end, in Vedantah, essence of the Veda: VEDANTA. II. Probable inflected form (locative plural) *antbhi, “on ter sides of,” whence *ambhi. See ambhi. [Pok. ant-s 48. ap-'. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE; (INEPT). 2. Latin apisci, to attain: ADEPT. 3. Latin apex, top, summit (< “something reached”): APEX. 4, Prefixed form *co-ap- (co-, together; see kom) in Latin cdpula, bond, tie, link: copuLa, COPULATE, COUPLE. 5. Perhaps Latin ammentum, dmen- tum (< *ap-mentum, “something tied”), thong, strap: AMENT!, [Pok. 1. ap- 50.] ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.] apero-. Shore. Perhaps a derivative of ap-?. Suffixed form *dper-yo- in Greek épeiros, land, mainland, conti- nent: EPEIROGENY. [Pok. dpero- 53.] apo-. Also ap-. Off, away. 1. Germanic *af in: a. Old English of, zf (> Middle English of, of-), off: oF, OFF, OFFAL; b. Old English ebba, low tide: EBB; c. Old High German aba, off, away from: ABLAUT; d. Germanic *aftan- in Old English zftan, behind: ABAFT. 2. Latin ab, ab-, away from: AB-!. 3. Greek apo, away from, from: apo-. 4, Suffixed (comparative) form “*ap(o)-tero- in Germanic *aftar- in Old English zfter, after, behind: AFTER. 5. Suffixed form *ap-t-is- in Germanic *aftiz in Old English eft, again: EFTsoons. 6. Suffixed form *apu-ko- in Germanic afug- in Old Norse dfugr, turned backward: AWKWARD. 7. Possible root *po(s), on, in: a. Russian po, at, by, next to: PoGROM; b. Latin post, behind, back, afterward: POST-, POSTERIOR; POST- MORTEM, PREPOSTEROUS, PUISNE, (PUNY); C. Latin pd- nere, to put, place, from *po-sinere (sinere, to leave, let; of obscure origin): APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITION), (COMPOUND), DEPONE, DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST, POSTS,
492:TION), GENERIC, GENEROUS, GENRE, GENUS; CONGENER, (CONGENIAL), DEGENERATE, (ENGENDER), MISCEGENA- TION; b. Greek genos and genea, race, family: GENEAL- OGY, GENOCIDE, GENOTYPE, HETEROGENEOUS; c. Greek suffix -genés, ‘‘-born’”: -GEN, -GENY. 4. Suffixed full-grade form *gen-yo- in: a. Latin genius, procreative divinity, inborn tutelary spirit, innate quality: GENIAL!, GENIUS; b. Latin ingenium (in-, in; see en), inborn character: ENGINE, INGENIOUS. 5. Suffixed full-grade form *gen-d- in Latin indigena (indu-, within; see en), born in (a place), indigenous: INDIGEN, (INDIGENOUS). 6. Suffixed full-grade form *gena-wo- in Latin ingenuus (in-, in; see en), born in (a place), native, natural, freeborn: INGENUOUS. 7. Suffixed full-grade form *gen- men- dissimilated in Latin germen, shoot, bud, embryo, germ: GERM, GERMAN?, (GERMANE), GERMINAL, GERMI- NATE. 8. Suffixed full-grade form *gena-ti- in Greek genesis, birth, beginning: GENESIS, -GENESIS. 9. Redupli- cated form *gi-gn- in: a. Latin gignere (past participle genitus), to beget: GENITAL, GENITIVE, GENITOR, GENT!, (GINGERLY); CONGENITAL, PRIMOGENITURE, PROGENI- TOR, (PROGENY); b. Greek gignesthai, to be born: EPI- GENE. 10. Suffixed zero-grade form *-gn-o- in Latin benignus (bene, well; see deu-?), good-natured, kindly, and malignus (male, ill; see mel-5), evil-natured, malevo- lent: BENIGN, MALIGN. 11. Zero-grade form *gna- becom- ing *gnda- in Latin praegnds (prae-, before; see per’), pregnant: PREGNANT!. 12. Suffixed zero-grade form *gna-sko- becoming *gnd-sko- in Latin gndsci, ndsci (present participle ndscéns, past participle gndtus, nd- tus), to be born: NAIVE, NASCENT, NATAL, NATION, NA- TIVE, NATURE, NEE, NOEL; (ADNATE), AGNATE, COGNATE, CONNATE, ENATE, INNATE, NEONATE, PUISNE, (PUNY), RENAISSANCE. 13. Suffixed o-grade form *gon-o- in Greek gonos (combining form -gonos), child, procre- ation, seed: GONAD, GONO-; ARCHEGONIUM, EPIGONE. 14. Zero-grade form *gn- in Sanskrit ja- in krmi-ja-, “produced by worms” (see k*rmi-). [Pok. 1. gen- 373.] genu-'. Knee; also angle. 1. Variant form *gneu- in: a. Germanic *knewam in Old English cnéo, knee: KNEE; b. Germanic *knewljan in Old English cnéowlian, to kneel: KNEEL. 2. Basic form *genu- in Latin genii, knee: GENICULATE, GENUFLECT. 3. Suffixed variant form *gon-ya- in Greek gdnia, angle, corner: -GON, GONION; AMBLYGONITE, DIAGONAL, GONIOMETER, GONIOMETRY, ORTHOGONAL. [Pok. 1. genu- 380.] genu-2. Jawbone, chin. 1. Form *genw- in Germanic *kinnuz in Old English cin(n), chin: CHIN. 2. Basic form *genu- in Greek genus, chin: GENIAL. 3. Suffixed variant form *gna-dho- in Greek gnathos, jaw: GNATHIC, -GNATHOUS; CHAETOGNATH 4, Variant form “g(h)enu- in Sanskrit hanu, jaw: HANUMAN. [Pok. 2. genu- 381.] gep(h)-. Also gebh-. Jaw, mouth. 1. Probably Germanic *kaf-, to gnaw, chew, in Old English ceaf, husks, chaff: CHAFF!, 2. Germanic *kabraz, “gnawer,” in Old English ceafor, ceafer, beetle: CHAFER; (COCKCHAFER). 3. Ger- manic *kéfalaz in Old English céafl, jaw, cheek: JOWL!. [Pok. geph-, gebh- 382.] ger-'. To gather. 1. Extended form *grem- in Germanic *kram- in Old English crammian, to stuff, cram: CRAM. 2. Reduplicated form *gre-g- in Latin grex (stem greg-), herd, flock: GREGARIOUS; AGGREGATE, CONGREGATE, EGREGIOUS, SEGREGATE. 3. Earliest forms “ager-, *ggor-d-, in Greek ageirein, to assemble, and aguris, agora, marketplace (> agoreuein, to speak): AGORA}; (AGORAPHOBIA), ALLEGORY, CATEGORY, PANEGYRIC. [Pok. 1. ger- 382.] ger-2. Curving, crooked; hypothetical Indo-European base for a variety of Germanic words with initial kr-. I. Words meaning to bend, curl; bent, crooked, hooked; something bent or hooked. 1. Germanic *krdpp6n-, a hook, especially one used in harvesting grapes, in: a. Old High German krapfo, a hook: AGRAFFE; b. Old French graper, to harvest grapes, hence (back-formation) grape,
494:vine, grape: GRAPE; c. Old French grapon, grapnel: GRAPNEL; d. Old French grape, a hook: GRAPPLE; e. Ital- ian dialectal grappa, vine stem, brandy: GRAPPA. 2. Old English crump, crumb, crooked, bent, stooping: CRUM- MIE, CRUMPET, (CRUMPLE). 3. Low German krimpen, to wrinkle: CRIMP!. 4. Middle Dutch crampe, hook, and Frankish *kramp, hook: cramMpP?. 5.Old High German krampfo, a cramp, akin to the Germanic source of Old French crampe, cramp: CRAMP!. 6. Old English crypel, a cripple: CRIPPLE. 7. Germanic *kreupan in Old English créopan, to creep: CREEP. 8. Middle Low German krink, a ring: CRINGLE. 9. Germanic *krengan in Old English cringan, to yield: CRINGE. 10. Middle Dutch crinkelen, akin to Middle English crinkelen, to make kinks in: CRINKLE. 11. Old Norse kriki, a bend, nook: CREEK. 12. Old Norse krékr, a hook: cRooOK. 13. Frankish *krok- (> Old French croc), a hook: CROCHET, (CROCKET), (CROQUET), (CROUCH); ENCROACH. 14. Old English crycc, (bent) staff, crutch: CRUTCH. 15. Old French crosse, crook: CROSIER, LACROSSE. 16. Middle Dutch crulle, curly: CRULLER, CURL. 17. Old English cranc-(stzf), a weaving implement: CRANK}. 18. Norwegian krake, a sickly beast, akin to the source of Middle English crok, an old ewe: cRocK3, 19. Old Norse karpa, to boast: CaRP!, 20. Middle Dutch kroes, curled, akin to the source of Old French grosele, gooseberry: GROSSULARITE. II. Words meaning ‘“‘a rounded mass, collection; a round object, vessel, container.” 1. Old English cruma, a frag- ment: CRUMB. 2. Frankish *kruppa, rump, akin to the Germanic source of Old French croup, rump: CROUP?, (CROUPIER), CRUPPER. 3. Old English cropp, cluster, bunch, ear of corn: crop. 4. Italian gruppo, an assem- blage: Group. 5. Old English crocc, pot: CROCK}. 6, Mid- dle Dutch cruyse, pot: CRUSE. 7. Old English cribb, manger: CRIB. 8. Old English cradel, cradle: CRADLE. 9. Frankish *kripja, cradle, akin to the Germanic source of Old French cre(s)che, crib: CRECHE. 10. Old English creet and Old Norse kartr, wagon: CART. 11. Old English croft, small enclosed field: crort. [Pok. 3. ger- 385.] gerbh-. To scratch. 1. Germanic *kerban in Old English ceorfan, to cut: CARVE. 2. Zero-grade Germanic form *kurbiz in Old English cyrf, a cutting (off): KERF. 3. Variant form *grebh- in: a. Germanic *krab(b)- in Old English crabba, a crab: CRAB}; b. Germanic *krabiz- in Old French crevise, crayfish: CRAYFISH; C. perhaps Ger- manic *krab- in Old Norse krafla, to crawl: CRAWL. 4. Zero-grade form *grbh- in Greek graphein, to scratch, draw, write, and gramma (< *grbh-mn), a picture, writ- ten letter, piece of writing, and grammé, a line: GRAF- FITO, GRAM!, -GRAM, GRAMMAR, GRAPH, -GRAPH, -GRAPHER, GRAPHIC, -GRAPHY; AGRAPHA, AGRAPHIA, DIAGRAM, EPIGRAM, (EPIGRAPH), GRAPHITE, ICONOGRA- PHY, PARAGRAPH, PROGRAM, PSEUDEPIGRAPHA, TETRA- GRAMMATON, TOPOGRAPHY. [Pok. gerebh- 392.] [gerere. To carry, carry on, act, do. Latin verb of un- known origin. Oldest form ges-, past participle gestus. GERENT, GERUND, (GEST), GESTATION, (GESTICULATE), GESTURE, JEST; ARMIGER, BELLIGERENT, (CONGERIES), CONGEST, DIGEST, EGEST, INGEST, REGISTER, SUGGEST, VELIGER.] gere-'. To grow old. 1. Suffixed lengthened-grade form *géro-s- in Greek géras, old age: AGERATUM, CALOYER, GERIATRICS. 2. Suffixed form “gera-ont- in Greek geron (stem geront-), old man: GERONTO-. [Pok. ger- 390.] gere-2. To cry hoarsely; also the name of the crane. I, Words meaning “‘to cry hoarsely”; also words denoting the crow. 1, Germanic *kré- in: a. Old English crawe, a crow: CROW}; b. Old English crdwan, to crow: CROW?; c. Old English cracian, to resound: CRACK; d. Middle Dutch krdken, to crack: CRACKNEL; @. Old Norse kraka, a crow: CRAKE. f. Middle Dutch krdnen, to groan, la- ment: CROON. 2. Possibly (but more likely imitative) Germanic *kur(r)- in Old Norse kurra, to growl, akin to Middle English curre, cur: cur. II. Words denoting a
934:*sua-yo-, contracted to *si-yo- in Greek huein, to rain, and huetos, rain: ISOHYET. II. Possible extended zero-grade form *sib-. 1.Germanic *sip- in: a. Old English sipan, sipian, to drink, sip: suP!; b. Old French soup(e), soup: SOUP, (SUP2). 2. Germanic “supp- in: a. Old English sopp, bread dipped in liquid: sop; b. possibly Low German sippen, to sip, probably akin to the source of Middle English sippen, to sip: stp. III. Possible ex- tended zero-grade form “sig-. 1. Germanic *sik- in Old English sican, to suck: sucK. 2. Germanic shortened form *sukdn in Old English socian, to steep: SOAK. 3. Latin siigere, to suck: SUCTION, SUCTORIAL. 4, Variant form *sik- in Latin siicus, succus, juice: SUCCULENT. [Pok. 1. seu- 912.] seut-. To seethe, boil. 1. Germanic *seuthan in Old English séothan, to boil: SEETHE, (SODDEN). 2. Germanic *suth- in: a. Middle Dutch sudde, sudse, marsh, swamp: sups; b. suffixed form *suth-l- in Middle High German sudelen, to soil, do sloppy work, akin to Middle Dutch soetler, sutler: SUTLER. [Pok. 4. seu- 914.] si-lo-. Silent. Suffixed (stative) form *si/-é- in Latin silére, to be silent: SILENT. [In Pok. 2. sé(i)- 889.] skabh-. To prop up, support. Suffixed form *skabh-no- in Latin scamnum, a bench (> Old English sceamel, table, stool): SHAMBLES. [Pok. skabh- 916.] skai-. Also kai-. Bright, shining. 1. Extended form *kaid- in Germanic *haiduz, “bright appearance,” manner, quality, in Old English -hdd, quality, condition: -Hoop. 2. Suffixed form *ki-t-ro- in Sanskrit citra-, variegated, many-colored: CHEETAH, CHINTZ. [Pok. (s)kdi- 916.] [skalkaz. Servant, slave. Germanic noun of unknown origin. 1. Old High German compound marahscalc, “horse-servant” (see marko-). 2. Germanic compound *sini-skalkaz, “old servant” (see sen-'). [In Pok. (s)kel- 929.]] skamb-. Also kamb-. To curve, bend. Suffixed form *kamb-o- in Celtic *kambo-, crooked, and denominative verb *k(a)mb-yo-, to turn, exchange, whence Gallo-Latin cambidre, to exchange: CAMBIST, CAMBIUM, CHANGE. [Pok. (s)kamb- 918.] skand-. Also skend-. To leap, climb. 1. Latin scandere, to climb: SCAN, SCANDENT, SCANSION, SCANSORIAL; AS- CEND, (CONDESCEND), DESCEND, TRANSCEND. 2. Suffixed form *skand-alo- in Greek skandalon, a snare, trap, stumbling block: SCANDAL. 3. Suffixed form *skand-sld- in Latin scdlae, steps, ladder: ECHELON, ESCALADE, SCALE?. sked-. To split, scatter. Extension of sek-. 1. O-grade form *skod- in Germanic *skaé- in Old English *sc(e)ater- ian, to scatter: SHATTER. 2. Variant nasalized form *ska-n-d- in Latin scandula, a shingle for roofing (< “split piece”): SHINGLE}. [Pok. (s)k(hjed- 918.] skeei-. To gleam. 1. Suffixed form “ske(ji-no- in Ger- manic *skinan, to gleam, shine, in: a. Old English scinan, to shine: SHINE; b. Old High German scinan, to shine: GEGENSCHEIN. 2. Germanic extended form *ski-m- in Old English scimerian, scymrian, to shine brightly: SHIM- MER. 3. Possibly suffixed form *ski-nto-, shining, in Latin scintilla, a spark: SCINTILLA, SCINTILLATE, STEN- CIL, (TINSEL). 4. Suffixed zero-grade form *skia-G-, *skiy-d- in Greek skia, shadow: SKIAGRAM, SKIASCOPE, SQUIRREL. [Pok. skai- 917.] skei-. To cut, split. Extension of sek-. 1. Germanic suffixed form *ski-nd- in: a. Old English scinu, shin, shinbone (< “piece cut off’): SHIN!-; b. Old French eschine, backbone, piece of meat with part of the back- bone: CHINE, 2, Latin scire, to know (< “to separate one thing from another,” “discern”): SCIENCE, SCILICET, SCIOLISM, SCIRE FACIAS; ADSCITITIOUS, CONSCIENCE, CONSCIOUS, NESCIENCE, (NICE), OMNISCIENT, PLEBI- SCITE, PRESCIENT. 3. Suffixed zero-grade form *skiy-end in Old Irish scian, knife: SKEAN. 4. Extended root *skeid- in: a. Germanic *skitan, to separate, defecate, in Old English *scitan, to defecate: SHIT; b. suffixed zero-grade
936:form *sk(hjid-yo- in Greek skhizein, to split: SCHISM, SCHIST, SCHIZO-; C. nasalized zero-grade form *ski-n-d- in Latin scindere, to split: SCISSION; EXSCIND, PRESCIND, RESCIND. 5. Extended root *skeit- in: a. Germanic *skaith-, *skaidan in (i) Old English scéadan, to sepa- rate: SHED! (ii) perhaps Old English scéath, sheath (< “split stick”): SHEATH; b. Germanic *skidam in Old Norse skidh, log, stick, snowshoe: SKI; C. o-grade form *skoit- in Latin scittum, shield (< “board”): ECU, ES- CUDO, ESCUTCHEON, ESQUIRE, SCUDO, SCUTUM, (SQUIRE). 6. Extended root *skeip- in Germanic *skif- in: a. Middle English sheve, pulley (< “piece of wood with grooves”): SHEAVE?; b. Old Norse skifa, to slice, split, akin to the Scandinavian source of SKIVE; c. Middle Low German schever, splinter, akin to the possible Low German source of Middle English schivere, scivre, splinter: SHIVER?. [Pok. skei- 919.] skel-'. Also kel-. To cut. 1. Germanic *skalj6, piece cut off, shell, scale, in: a. Old English scell, sciel, shell: SHELL; b. Italian scaglia, chip: SCAGLIOLA. 2. Germanic *skalé in: a. Old English sc(e)alu, husk, shell: SHALE; b. Old French escale, husk, shell: scALE!. 3. Germanic *skal- in: a. Old Norse skalli, bald head (< “closely shaved skull”): SCALL; b. Old Norse skalpr, sheath, shell, akin to the source of Middle English scalp, scalp: SCALP. 4. Germanic *skél6é in Old Norse skal, bowl, drinking vessel (made from a shell): SCALE’, SKOAL. 5. Germanic *skelduz in Old English scield, shield (< “board’’): SHIELD. 6. Germanic *skeli- in: a. Old Norse skil, reason, discernment, knowledge (< “‘incisiveness”): SKILL; b. Middle Dutch schillen, to diversify, with past partici- ple schillede, separated, variegated, akin to the Low German source of Middle English scheld, variegated: SHELDRAKE. 7. Germanic skulé, a division, in Middle Low German schdle, troop: SCHOOL?, SHOAL’. 8. Suffixed variant form *kel-tro- in Latin culter, knife: COLTER, CULTRATE, CUTLASS. 9. Suffixed zero-grade form “skl-yo- in Greek skaillein, to stir up, hoe (> skalenos, uneven): SCALENE. 10. Extended root *skelp- in: a. Germanic *skelf- in Middle Low German schelf, shelf (< “split piece of wood”): SHELF; b. possibly Germanic *halbaz (< variant root *kelp-), divided, in Old English healf, half: HALF; C. perhaps variant *skalp- in Latin scalpere, to cut, scrape, with derivative sculpere (originally as the combining form of scalpere), to carve: SCALPEL, SCULP- TURE. [Pok. 1. (s)kel- 923.] skel-2. To be under an obligation. O-grade (perfect) form *skol- in Germanic *skal-, I owe, hence I ought, in Old English sceal (used with the first and third person singular pronouns), shall: SHALL. [Pok. 2. (s)kel- 927.] skel-3. Also kel-. Crooked. With derivatives referring to a bent or curved part of the body, such as a leg, heel, knee, or hip. 1. Suffixed form *skel-ko- in Germanic *skelha- in Old High German scilihen, to wink, blink (> German Schiller, iridescence): SCHILLER. 2. Suffixed form *skel-es- in Greek skelos, leg: ISOSCELES, TRISKELION. 3. Suffixed o-grade form “skol-yo- in Greek skolios, crooked: sco.iosis. 4. Lengthened o-grade form *skol- in Greek skéléx, earthworm, grub (< “that which twists and turns”): SCOLEX. 5. Suffixed lengthened-grade form *k6l-o- in Greek kélon, limb, member: COLON}. 6. Attrib- uted (quite doubtfully) by some to this root is Greek kulindein, to roll: CALENDER, CYLINDER. [Pok. 4. skel- 928.] skele-. To parch, wither. Variant *sk/é-, contracted from *skleo-. 1. Greek skellesthai, to dry, whence skeletos (< suffixed form *skeb-to-), dried up (body), mummy: SKELETON. 2. Suffixed variant form *sk/é-ro- in Greek skléros, hard: SCLERA, SCLERO-, SCLEROMA, (SCLEROSIS), (SCLEROTIC), SCLEROTIUM, SCLEROUS; SCLEROTIZATION. [Pok. 3. (s)kel- 927.] skeng-. Crooked. Germanic *skank6n-, “that which bends,” leg, in Old English sc(e)anca, shinbone: SHANK. [Pok. (s)keng- 930.]
942:leaves): CRAMBO. 4. Perhaps Celtic *krumb-i- in Welsh crwn, crooked, arched: CROMLECH. [Pok. (s)kerb(h)- 948.] skét(e)-. To injure. Suffixed zero-grade form *skoat-on- in Germanic *skathén- in: a. Old Norse skadha, to harm: SCATHE; b. Old High German scado (> German Scha- den), harm, injury, damage: SCHADENFREUDE. [Pok. skéth- 950.]
1146:TRORSE, SUBVERT, TERGIVERSATE, TRANSVERSE, UNI- VERSE. 5. Balto-Slavic *wirstd-, a turn, bend, in Russian versta, line: VERST. II. Root *wreit-, to turn. Germanic *writh-, *wraith- in: a. Old English writha, band (< “that which is wound around”): WREATH; b. Old English writhan, to twist, torture: WRITHE; Cc. Old English wrath, angry (< “tormented, twisted”): WRATH, WROTH. III. Root *wergh-, to turn. 1. Germanic *wurgjan in Old English wyrgan, to strangle: WORRY. 2. Nasalized vari- ant *wrengh- in: a. Germanic *wreng- in Old English wringan, to twist: WRING; b. Germanic *wrang- in (i) Old Norse *vrangr, rangr, curved, crooked, wrong, akin to the Scandinavian source of Middle English wrong, wrong: WRONG (ii) Low German wrangeln, to wrestle, akin to the Low German source of Middle English wranglen, to wrangle: WRANGLE. IV. Root *werg-, to turn. 1. Nasalized variant form *wreng- in Germanic *wrankjan in: a. Old English wrencan, to twist: WRENCH; b. Old English gewrinclian, to wind (ge-, col- lective prefix; see kom): WRINKLE. 2. Latin vergere, to turn, tend toward: VERGE?; CONVERGE, DIVERGE. V. Root *wreik-, to turn. 1. Germanic *wrig- in: a. Old English wrigian, to turn, bend, go: wRy; b. Middle Low German wriggeln, to wriggle: WRIGGLE. 2. Germanic *wrthst- whence *wristiz in Old English wrist, wrist: wRIsT. 3. Secondary Germanic derivative *wraistjan in Old English wréstan, to twist, with its frequentative *wréstlian, to wrestle: WREST, WRESTLE. 4. Possibly o-grade form *wroik- in Gaulish *briiko, heather (> French bruyére, heath): BRIAR}. VI. Germanic root *wrib- in Old French riber, to be wanton: RIBALD. VII. Root *werb-, also *werbh-, to turn, bend. 1. Ger- manic *werp-, *warp-, “to fling by turning the arm,” in Old English weorpan, to throw away: WARP. 2. Latin verber, whip, rod: REVERBERATE. 3. Latin verbéna, sacred foliage: VERBENA, (VERVAIN). 4, Zero-grade form *wrb- in Greek rhabdos, rod: RHABDOMANCY, RHABDOVI- Rus. 5. Nasalized variant form *wrembh- in Greek rhom- bos, magic wheel, rhombus: RHOMBUS. VIII. Root *werp-, to turn, wind. 1. Metathesized form *wrep- in Germanic *wrap- in Danish dialectal vraule, to wind, akin to the source of Middle English wrappen, to wrap: wraP. 2. Zero-grade form *wrp- in Greek rhaptein, to sew (> rhaphé, suture): RAPHE, RAPHIDE; RHAPSODY, STAPHYLORRHAPHY, TENORRHAPHY. IX. Root *wrmi-, worm; rhyme word to k*rmi-. 1. Germanic *wurmiz in Old English wyrm, worm: worm. 2. Latin vermis, worm: VERMEIL, VERMI-, VERMICELLI, VERMICULAR, VERMIN. [Pok. 3. ver- 1152.]
```


## [2026-09-06T02:17:44.706Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW fallo ===\"; grep -n \"fallo\\|fallō\" LEW_1910.txt | head -10; echo; echo \"=== LAT fallo ===\"; grep -n \"^fallo\\|fallo,\" LAT.txt | head -10; echo; echo \"=== SKT false/fail ===\"; grep -n \"^False\\|^Fail\\|fallere\" SKT.txt | head -10",
 "description": "Grep Walde LEW, Ernout-Meillet, Skeat"
}
```


### [2026-09-06T02:17:44.813Z] TOOL RESULT

```
=== LEW fallo ===

=== LAT fallo ===
20360:fallo, -is, fefelli, falsum, fallere; seul yerbe a perfectum a
20372:me fallo, nisi fallor, haud falsa sum (Pl.T^r.). Fal lo peut Stre ac-
20375:id ego si fallo, les deux sens de "tromper" et de "echapper a" remon-
22894:suppose sous fallo, on pourrait envisager que la forne flec- suppo-
46370:etc. (cf. le cas de -cello, uello, fallo, et v. aussi pendo). L'ombrien

=== SKT false/fail ===
6261:Fail :  see  FalUble.
6302:False,  Falter ;  see  Fallibla.
```


## [2026-09-06T02:17:50.569Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD FALSE caps ===\"; grep -c \"FALSE\" AHD_watkins1985.txt; grep -o \"FAIL[A-Z]*\" AHD_watkins1985.txt | head; echo \"=== LAT fallo entry ===\"; sed -n '20355,20400p' LAT.txt",
 "description": "Check AHD and Ernout-Meillet fallo"
}
```


### [2026-09-06T02:17:50.655Z] TOOL RESULT

```
=== AHD FALSE caps ===
0
=== LAT fallo entry ===
Mot etrusque, comme le dit Festus (v. Bottiglioni, St.Etr.3, p.330),
falco, - 5 nis m.: faucon. V.falx. Peut-etre calque semantique de
capys ? Cf. le double sens de gr.ocpTrq "faucille" et "faucon".
faliscum, -I (fall-) n.: v./orco. Sorte de couteau, sans doute
ainsi nomme du pays ou il etait fabrique?
fallo, -is, fefelli, falsum, fallere; seul yerbe a perfectum a
redoublement en f (cf. cependant facio)} du reste fefelli est refait
sur le present: si la forne £tait ancienne, on attendrait *febuli
comme pepuli de pello. Formes accessoires attestees en b.latin: fal 15 ,
-3 s (d^nominatif de fa l la, -ae? ), cf. Non.109,16: fallam pro fallaciam.
Eouius Decuma (13): is me non uocabit: ob eam rem hanc feci fallam ;
et CGL Y 641,35) fallator m.(gl.); falleo,-es et fallio,-Is, d'ofc
*fallia M.I.3168, et en britt. : corn. fall, fyllel} un pcp '. fefellitus
dans P 4 tr. 6 i (et sans doute *fallitus sur lequel a ete bati fallita,
cf.fr. faute, etc. M.l.3169): i° tromper; 3° ^chapper a (= gr. Xa.v 9 a.va>) ,
souvent impersonnel: non me fallit, suivi ou non d'une proposition
completive. De ce sens d^rive l'emploi pronominal ou ai£dio-passif:
me fallo, nisi fallor, haud falsa sum (Pl.T^r.). Fal lo peut Stre ac-
compagne d'un complanent de personne: fallere aliquem, ou de chose:
fallere spem, ancien accusatif "de l'objet interne", cf. Pl., Am.933,
id ego si fallo, les deux sens de "tromper" et de "echapper a" remon-
tent probablement k un sens unique de "cacher, etre cach^" {fefellit,
latuit Gloss.), sens du reste atteste k 1 '^poque imperiale, cf.Ov., F.
3,33, sua diuina furta fefellit ope} Hor.Ep.1,16,54 sit spes fallendi
(= latendi): miscebis sacra profanis-, ibid.1,17,10 qui natus moriensque
fefellit (= eXoc 9 e). - Ancien, usuel. Panroman (sauf roumain). M.L.3167.
Formes nominales: falsus: i° faux, trompeur; a' qui se trompe. M.L.
3171; irl./alZsa, britt. ffals} germ.; m.h.a. valsch. Substantif n.
falsum: le faux, oppose A uerum, et dont derivent falsarius} falsitas,
mot de la 1 . de 1 'figlise cr^e d'apres ueritas} falsimonium, Plaute,
d'aprfes testimonium} falso,- 3 s (b.lat.). M.L.3170 avec les derives
ordinaires. Falsus sert en outre de premier terme k des adj. composes;
falsidicus, falsiloquus (= v|/eu8oXc>yoc), etc .} fallax (g 4 n .pl. fal lacum
Catul.30,4): trompeur. De 1 k: fallacia f.: usit 4 surtout au pl .falla¬
ciae-, fallaciSsus (Geli., Apul.); fallacitas (cf.mendacitas, Tert.),
falldciloquela, fallaciloquentia (= v|/6u8oXc>y£«), dans Accius, cite
par Cic.Fin.4,68.
Composes: refellG: repousser le mensonge, refuter. Cf. arguo et re-- 381 -
fama
darguo. - *Falsico est supposd par -r.h.&.falscon "falschen".
On voit par falsus que fallo doit reposer sur faldo (toutefois
on peut songer aussi a *faln5). Le rapport qu'on croit apercevoir au
premier abord avec v.h.a./allan "tomber" et par suite avec lit. pulu
"je toabe", ara. p' lania "je «'dcroule", et sans doute gr. crqxxXXto "je
fais toaber" se heurte au fait que .c'est un p latin qui, dans spuma
et pumex, repond k un ph sanskrit. Mais on n'ose rien affiraer parce
```


## [2026-09-06T02:17:53.283Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20400,20420p' LAT.txt",
 "description": "Ernout-Meillet fallo continued"
}
```


### [2026-09-06T02:17:53.354Z] TOOL RESULT

```
et pumex, repond k un ph sanskrit. Mais on n'ose rien affiraer parce
que les sourdes aspirdes alternent souvent avec des sourdes siaples;
le rapprocheaent indique est trop seduisant pour qu'on n'essaie pas
de s'y tenir. - La diphtongue en a a aussi un caractere "populaire".
Les rapprochements avec gr.cpqXoC, cprjXoC "troapeur", ou avec got.dwals
"jwopoc", ou avec skr .hvarati "il va de travers", v.sl.z&Iu "avehant",
sont vagues. En sanie, etyaologie eabarrassante.
faluppa?: quisquilias paleas minutissimas uel surculi minuti quas
faluppas uocant (Gl.). - Mot sans doute non latin, M.L.3173.
falx, -cis f.; "faux" et "serpe". - Ancien, usuel. Panroaan. M.L.
31 75 • *
Derivas: falcula {.facula, flac la), M.L. 3159 et *alcicula, M.L.3IS 6 :
faucille, et "ongle, griffe"; falcito,-ds (tardif) "faucher", frd-
qnentatif de *falcd,-as , atteste par les 1 . roaanes, M.L.3153, cf.
*defalcb, 3516; falco,-onis a.: -nes dicuntur quorum digiti pollices
in Pedibus intro sunt curuati, a similitudine falcis, P.F.78,17,
peut-etre a rapprocher de falco,-onis "faucon" que les gloses ex-
pliquent par quod incuruis digitis sit, cf.Isid., Or.13,7, 57 , CGL
IY 341,3, Serv. Ae.10,145; toutefois le noa du faucon, /aico,n'app-
parait que tardiveaent (ital., Polea.Silu.), et il est possible que
le rapprocheaent avec falx soit une etyaologie populaire; mais le
```


## [2026-09-06T02:18:04.918Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON ghuk ===\"; grep -n \"غوک\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10; echo; echo \"=== BQT ghuk ===\"; grep -n \"غوک\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null | head -10",
 "description": "Grep Moin and Borhan for غوک"
}
```


### [2026-09-06T02:18:04.996Z] TOOL RESULT

```
=== MON ghuk ===
incoming/MON/MON_2vol_Adena_v2_djvu.txt:904:غر: ۲ (اصت.) آواز غوکث» صدای وزغ. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:3420:غوک: - ۷ | - گوک ( ) زمین کنده و 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:3423:غوک: ۶ غوق| (۱) (جاد.) غوکان ج. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:3424:غوکک. (جاد.) قورباغگان. ( (جان.) گاهی 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:3427:غوک چوب: 0« (امر.) دو چوب باشد 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:15552:سساند کدی او رو ضص_فدع» غوکل؛ ج. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:15555:و می‌شوند) غوکان؛ 
MON_part2.txt:904:غر: ۲ (اصت.) آواز غوکث» صدای وزغ. 
MON_part2.txt:3420:غوک: - ۷ | - گوک ( ) زمین کنده و 
MON_part2.txt:3423:غوک: ۶ غوق| (۱) (جاد.) غوکان ج. 

=== BQT ghuk ===
incoming/BQT/BQT_v4_pages.txt:4405:گفتا که ينجبايك و غوکه ومکل بکوب درخایه هل توچنگه خشتار بامداد.>
```


## [2026-09-06T02:18:06.925Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index zur/ghuk ===\"; grep -n -i \"ZUR\\|GHUK\\|GUK\" incoming/ARY/ARY_latin_index_pages.txt | head -20; echo; echo \"=== ARY persian ===\"; grep -n \"غوک\\|زور\" incoming/ARY/ARY_pages.txt | head -10",
 "description": "Grep Aryanpur"
}
```


### [2026-09-06T02:18:07.002Z] TOOL RESULT

```
=== ARY latin index zur/ghuk ===
3651:VAAGE DANISH) Sails ‘WUZURG, BAZURG (PAHLAVI) (5 4,
3655:VZRUK, VZURK — (ARMENIAN) 5,1
8036:APY 9 APO g AO i oo dby ZUR- (OLD HIGH GERMAN) pS gilt
8769:ALKISTA, ALKISTAN :(HITTITE) ca RAZURA HAVESTAN) gel
9170:444 140 bide, ZURETI, ZIRETI
9582:FALSE ENGLISH) gudSsl ZURAH, AVESTAN) gle 9|
9584:FALSK (SWEDISH) (S38 yo ZUR (PAHLAVI) 5 slag
9984:ytd | Guke
12944:ZHERU CZECH) So GUKARITAN, PAHLAVI) «5 3h

=== ARY persian ===
4401:سنا زورون مس سس
5064:چم‌های این واژه در زبان‌های این فهرست: جست و خیز» شادی» ورجه ورجه؛ غوکك» وزغ» تند.
5388:۳۸۸1-۸1727۸7 (به چم "قوت" و "زور") می‌داند (برهان قاطع : ۴۳۹) یی
6572:۲ چم اين واژه در زبان‌های ژرمنی کهن "گرفتن" برده ولی در زبان‌های ژرمی نوین چم آن اپا زور بلند کردن*
9732:۱ واژه‌ی زور" به چم "آب مقدس که در مراسم زرتشتی پاشیده می‌شود" نیز از همین واجریشه است
9754:زور (به چم "نادرست و دروغ") / ۳۳۱
13366:31۸5۵ اسلواکی (51.07420)+ زورید )۱
14394:سغدی (/800/0140): 01 سوئدی (57520/57): زور 1
```


## [2026-09-06T02:18:12.778Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=9700 && NR<=9790' incoming/ARY/ARY_pages.txt; echo \"=== page tag ===\"; awk 'NR<=9754 && /\\[pdf page/{p=$0} END{print p}' incoming/ARY/ARY_pages.txt",
 "description": "Read Aryanpur zur entry"
}
```


### [2026-09-06T02:18:14.552Z] TOOL RESULT

```
ایركدی کهن (#فل#/ 012): ۰ 810 ,8850 256 تلا
ولزی (84 )+ نان 1 (01100) :0/05
برتونی (/87870): 13۸ 2 (01100) 357
گالیکه (0۸81]70): ند 3 (۸778) ۸400
برهان قاطع : 1.۸۳
بادداشت:
۱- چم این واژه در زبان آلمانی نوین؛ سرزنده.
چم این واژه در زبان هلندی: جیره.
۲- یکی از چم‌های واژه‌ی انگلیسی 011101 زنده.
۳ بازگلت به: زیستن.
2۸07۸ ,207
اوستایی (47887۵/۷): فریزی کهن ((۲۷۹1۵ 010): 17۸
خ2۸07118 بال2۸07۸ آلمانی کهن (/(08704۸ 2۷/0 ۵ا۵):
1 پهلوی (1شالتم۳۸): 7207 ۸ ,61022۸
هو «سانسکر یت (8۸/51077): آلمانی (0874۸۷): ود ند ان
20306 ,103011 انگلیسی کهن (2۸0/1 012): ۰ 0807۸05 ۱
ارمنی (۸//8142): 7 ب,08[ انگلیسی (8لا600): 0
یونانی 078850): 60 ,01852۸ دانمارکی (0۸۷/80): 0052
لانین (7/0): ۰ ۲۲۵۲۶۵ ,57۸00 سوئدی (91752154): 207۸
گرتیکد (ع00771): 01137۸ نروژی (/087801۸): 207۸
ایسلندی کهن (/504(/210۸71۸۸ 00): هلندی (0ل07): 0 ,0007
۸ ,978ت0۲ 60107۸ لیتوانی (۸(/1۸/۷تا777):
[pdf page 329]
ُ
ا
۰ زود ۱
6۸1 ,۷۸85 پسگشت‌ها ده اد اد ی
لتونی (لتی) ((477۸ل): ات 48 200200
9 (07) 2 ۸ :22( ها
کک هام ۹ جهمی روم 1
۱ لغت‌نامه دهخدا: ۱۳۲ ا
یادداشت: ی
۱ واژه‌ی زور" به چم "آب مقدس که در مراسم زرتشتی پاشیده می‌شود" نیز از همین واجریشه است
(اوستابی:2۸0711۸؛ پهلری: 2:013). ۱
۲ چم این واژه در زبان‌های ژرملی و زبان لاتین: جاری شدن؛ آبگونه شدن. ۱
۳ چم این واژه در زبان ارمنی: آبکند» دره, :
۳ ا
اوستایی (47887/400): ۸ ,701 ایسلندی کهن (/54(/0/0141 0ا۲)0شاید)
پارسی پاستان (۳8۴۹1۵۸۷ صا0): 717۸ ده
پهثری (1لاماتا۸ه). 0 ,701
کردی (00/5(7): 71711 ,211 ,275 رنآ2 پسگشت‌ها از ادن ۲
بلرچی (//4۲0): ۰ 21773 ,217 ,207 9 ۸0800
اففانی (پشتو) (۸۳017۸(۷1): 2 9 (01166) :2ل52 ۸لز
سانسکریت (84۸/5507): 2.1317771 ب۳۸لآل برهان قاطع : ۱۰۳۳
یادداشت: ۰
شاید این واژه‌ها هم از همین واجريشه باشند: گرتیکه: 8 آلمانی کهن: 98۸7؛ انگلیسی کهن:9021۸ انگلیسی:
نان :
:
اوستایی (4587۸4): 3 5۸۷۸8 ,ا3۵7[ ,تشاد
پهلری ([اللم۸ه): 6 208 ارمنی (4748401): 3
کردی (07(01374): اد زد زا بونانی (0220): (شاید) 05
سانسکریت (84(507): ایسلندی کهن (524701۸4۷۵(۷ صا۲)0(شاید)
۱۲
[pdf page 330]
زور (به چم "نادرست و دروغ") / ۳۳۱
3 پسگشت‌ها 055
گالی (ل8لاتا0): (شاید) دید 99 20802900
8 (878006) ام ارم
برهان قاطع + ۱.۳۳
| م‌اگلیس سوازای ارس سا ۱88۵8
اوستایی (/۸587/4): ,218۸5 انگلیسی ([8۸01./5): اد ۱۸|
728۸73810۸ رقلف78۸3 دانمارکی (ل0۸2//3): ۳۸
پهلوی (۸1اب۸): 3 سرئدی (57750150): ۸
سانسکریت (54//5817): نروژی (/(فا07۷/50/): 7۸
8 ا7شل 17۷ ملدی (00760: ۷۸5
بونانی (07670): 05 اسلاوی کهن (10/شا5 ۲707677 012):
لاتین (4710: 200 ۱
۸5 ,تنل۴۸ ,قتاقل۴۸ روسی (55]4(۷): 20
فرانسه (17ح۳8۸7): ۸1 لیتوانی (777170/]۸۷/):
اسپانیایی (52۸(۷]87): 7۹0 ۷0213/825 ,2177۸515
ایتالیایی (7(لا74): ۳80 لنونی (لتی) (4774/4): 2۸7۸18 ,تال278
رومانی (۵۷ا۸1۸(۷): 7۸8
پرتغالی (۳071017835): ۳0 پسگشت‌ها اسرد اد
ایسلندی کهن 364/0100440 صات): 89 2006904
۲۸۵۸ 7 (8۳ت۲۸) 7
+ و » فریزی کهن (540۷ل7 0/0 05 8ل۲۸ 3 (85ل۲۸) اد دی هم
۱ ۹ آلمانی مان (0م/0570 0 از ةا04/00: 4 (85ت۲۸) :002/5
ْ لا ۷۸3 8 (8فت۴۸) :5 ۰
ُ آلمانی (4۸(۷ل087): 7۸ لغت‌نامه دهخدا: ۱۳۰۹
۱ انگلیسی میانه (2۸0./374 0/7008(از فرانسه) فرهنگ معین : ۱۶۰
: نع
۱ بادداشت:
۱ این واژه عربی نیست و شکل عربی آن از فارسی گرفته شده است.
سم
[pdf page 331]
۲ ا/ زه (به چم "چله‌ی کمان")
اوستایی (48707): ونر لیتوانی (۸(4ا(۸لا 14 7/.): 601۸8 وی
پهلری (4/1ماتله۳): 271
کردی (7ل400/5): 21 پسگشت‌ها َ اش دید
بلوچی (ابقه‌تالمه: 1101 81 ۶0/6990
آفقانی (پشتو) (۸۳0[۸(۷1): ت2۸ ملکمانم ۸2
=== page tag ===
[pdf page 330]
```


## [2026-09-06T02:18:29.584Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3415,3432p' incoming/MON/MON_2vol_Adena_v2_djvu.txt; echo \"=== BQT ghuk variants ===\"; grep -n \"غوك\\|غوک\\|غوق\" incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt BQT_v2_pages.txt 2>/dev/null | head -20",
 "description": "Moin ghuk entry and Borhan grep"
}
```


### [2026-09-06T02:18:29.709Z] TOOL RESULT

```
انگیختن. هنگامه کرردن. 
غوغو: :۱:8 - ک وکو (اصت. ( 
کوکو. (جاذ.) کبوتر. 
غوغولوغوغو: ۱:05۱0:07- غوغولوغو| 
(اصت.) بانگ خر وس .۰ ی 
غوک: - ۷ | - گوک ( ) زمین کنده و 
عمیق؛ گودال. 

غوک: ۶ غوق| (۱) (جاد.) غوکان ج. 
غوکک. (جاد.) قورباغگان. ( (جان.) گاهی 
مرادف با دوحباتین‌ها بکار رود. غ وک سبز: 
(جاد.) نوعی غو کن سبز. چوب دودله. 
غوک چوب: 0« (امر.) دو چوب باشد 
که کودکان بدان بازی الک‌دولک کنند. 
0 


.) فاخته 
=== BQT ghuk variants ===
incoming/BQT/BQT_v4_pages.txt:899:ماشر !۱ < بارای بی‌نقطه پروزن‌ناسزاء | میاغوب هم هست پٍمنیآزرده مشو و شور وغوقا
incoming/BQT/BQT_v4_pages.txt:4405:گفتا که ينجبايك و غوکه ومکل بکوب درخایه هل توچنگه خشتار بامداد.>
incoming/BQT/BQT_v4_pages.txt:4438:- و در مقام شك وکمان استعمال میکنند ی | بمعنی وزق و غوك باشد - و بکسر نانی » زلورا
incoming/BQT/BQT_v4_pages.txt:5433:ملگ * - بنم اولبروزن غوك » مطلق | وسامان راکویند ۲۴- ودرهندی بیخ نباتات ومابه
incoming/BQT/BQT_v4_pages.txt:11507:که از کوء و عمارت عالی وحمام وچاء وغیره باز فوقه ۴ - بر وزن کوقه » شور از غوقا
incoming/BQT/BQT_v4_pages.txt:13453:وغوك را نیز گفته اند ‎٩‏ ؛ و بعتی گوبند صدای واك؟ - بسکون کان » پرند‌است
incoming/BQT/BQT_v4_pages.txt:14611:(رك : وزق) قورباغه » غوك » ضفدع +
incoming/BQT/BQT_v4_pages.txt:14616:معروف امت و اورا غوك خوانند وبمربی شفدغ | آخر فضل زمتان راکویند چه وزهه باده بادی
incoming/BQT/BQT_v4_pages.txt:14631:۱- موّلف سراج نوشته : « وزغ » بفتحتین غوك » وبقاف که شهرت کرفته لِجعراقیان
incoming/BQT/BQT_v4_pages.txt:22337:جیم ومیم مضموم بروزن مفلوك » وزق وغوك را | ربایند۸ - وبعربی دهان را کوبند .
incoming/BQT/BQT_v3_pages.txt:15458:غنجمرش است که وزق وغوك باشد .
incoming/BQT/BQT_v3_pages.txt:15998:۱ « از صحیفات ‎Let‏ صاحب بزهان آنت که غوك چوب را ‎gas‏ ده دله که‌پیوفا
incoming/BQT/BQT_v3_pages.txt:22410:‏قاس بر وزن طاس . غوكه را کوبند
incoming/BQT/BQT_v3_pages.txt:34046:- و غوك و وزق را نز گویند ۸ .
incoming/BQT/BQT_v3_pages.txt:34816:- ودر مژیدالفضلا بمعنی غوكآمده است که‌وزق
BQT_v2_pages.txt:390:     ‫‪1‬‬    ‫ورك‬   ‫جاغوك‬   ‫‪۳‬‬   ‫رك‬    ‫‪۹‬‬        ‫ظاهراً همین « جاج مثو » است کهقصبه ایست ازقنوج‪.‬‬
BQT_v2_pages.txt:723:                          ‫ومانند! تراکونند‪#.‬‬     ‫جامةغوك ‪ -‬چیزی باد سبز شه‬
BQT_v2_pages.txt:2295:                                                             ‫جام غوك است» وآن چیزی باشد سبزرنگ که‬
BQT_v2_pages.txt:4613:‫چغوك(‪ )۳‬است که گنشکه باشده وبعر بیعسقور ‪.‬‬
BQT_v2_pages.txt:5900:  ‫‪1‬‬    ‫رضم اول وزق وغوك را گوش‬     ‫گفته اند ‪-‬‬
```


## [2026-09-06T02:18:37.674Z] TOOL CALL #32: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T02:18:37.683Z] TOOL RESULT

```


```


## [2026-09-06T02:18:41.613Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D9%88%D8%B1",
 "prompt": "Give the full Persian and Arabic sections: etymology of Persian زور (zur/zūr) in both the \"strength\" and the \"lie/falsehood\" senses, and the etymology of Arabic زور (zūr) \"falsehood\" and related تزوير / مزوّر. Quote the etymologies verbatim."
}
```


## [2026-09-06T02:18:43.158Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%BA%D9%88%DA%A9",
 "prompt": "Give the full Persian entry for غوک: etymology, pronunciation, meaning, cognates, and any cited sources (Hasandust, Cheung, etc.). Quote verbatim."
}
```


### [2026-09-06T02:18:48.882Z] TOOL RESULT

```
# Persian Entry for غوک

**Etymology:** The word was "Borrowed from Sogdian (ğwk)" and is "cognate with Ormuri and Parachi" according to the Dehkhoda Dictionary.

**Pronunciation:** The entry provides multiple pronunciations across Persian dialects:
- Classical Persian: /ˈɣuːk/
- Dari (formal, Kabuli): [ɣuːk]
- Hazaragi: [ɣuk]
- Iranian Persian: [quːkʰʲ]
- Tajik: [ʁuk]

**Meaning:** The noun has two definitions:
1. Frog
2. Toad

**Cognates:** Related forms appear in Ormuri and Parachi languages, derived from the same Sogdian source.

**Cited Source:** Ali-Akbar Dehkhoda's *Dehkhoda Dictionary* (1931–), published by the University of Tehran Press.
```


### [2026-09-06T02:18:50.823Z] TOOL RESULT

```
# Etymology of زور (zur/zūr) - Persian and Arabic

## Persian Etymology

**"Strength" sense (Etymology 1):**
"Inherited from Middle Persian [script needed] (zwl /⁠zōr⁠/), which Pokorny derives from Proto-Indo-European *gew- ("to hasten")"

**"Falsehood" sense (Etymology 3):**
"From Middle Persian [script needed] (zʿwr /⁠zūr⁠/). Compare also Old Armenian զուր (zur), from Parthian."

## Arabic Etymology

**زُور (zūr) "lie/falsehood":**
"Borrowed from Middle Persian 𐭦𐭥𐭫 (zwl /⁠zūr⁠/), and denominal verb."

**Related forms (تَزْوِير/مُزَوَّر):**
The verb زَوَّرَ (zawwara, Form II) derives from the same root and means "to forge, counterfeit, falsify" or "to fake, simulate." The participles مُزَوِّر (muzawwir, "one who forges") and مُزَوَّر (muzawwar, "forged/counterfeited") are passive and active participles respectively.
```


## [2026-09-06T02:18:58.324Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD ghwk frog ===\"; grep -n -i \"γwk\\|gwk\\|frog\" SOD.txt | head -20",
 "description": "Grep Gharib Sogdian for frog"
}
```


### [2026-09-06T02:18:58.377Z] TOOL RESULT

```
=== SOD ghwk frog ===
5224:77-95;  "Sogdian  on  a  Frog  Plain,"  M flanges  Benvenlste, 
28535:frog,  toad 
28549:frog's  eggs 
89814:frog     3185 
89815:frog's  eggs     3187
```


## [2026-09-06T02:19:00.840Z] TOOL CALL #36: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B2%D9%88%D8%B1' --note 'page 196, root Ghuel: Persian/Arabic زور — MP zūr, Arabic borrowed from MP' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%BA%D9%88%DA%A9' --note 'page 196, root Ghuk: Persian غوک frog, Wiktionary says borrowed from Sogdian ğwk' 2>&1 | tail -3",
 "description": "Archive the two Wiktionary pages"
}
```


### [2026-09-06T02:19:39.136Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/162b84a90f3c113a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f5145ebc83b1b976.txt
```


## [2026-09-06T02:19:41.291Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28525,28555p' SOD.txt; echo \"=== entry 3185 ===\"; grep -n \"^3185\\|3185\\b\" SOD.txt | head -5",
 "description": "Gharib frog entry"
}
```


### [2026-09-06T02:19:41.374Z] TOOL RESULT

```
3184  cywty   B  (^<a*i;jL^.>)ju^ 
cayut 

owl 

SCE  148;  Hen.  LW  96 

3185  cyz-   B  (>^  .-J^^^y 
cayz  ©Yaghn.  caYz  ©ace.  -w;  abl.  -> 

frog,  toad 

TSP  3.250;  SCE  178;  Hen.  L  W  96 

3186  cyz  r'yh   S  («Ljy"cJ.j)Jv 
cayz-  ray   ^r'y 

marsh  land 

Gersh.  Melanges  Benv.  196ff;  MDii  B16,  8 

3187  cyzr'w'k   B    <»j'jj^)^T^aj^<^jj  ji^jy-iw 

cayz-  rawe 
frog's  eggs 
Hen.  Texts.  727;  TSP  3.134;  Benv.  cYnrWk? 

3188  ck»t   B  (jK^)j\^i4» 
cakat  (ck}t)  ®<*cakata%  Pahl.  cakad 

peak, forehead 
=== entry 3185 ===
28532:3185  cyz-   B  (>^  .-J^^^y 
89814:frog     3185 
94658:toa^l  3185
```


## [2026-09-06T02:19:45.768Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^[0-9]*  ywk\\|ywk \\|yuk\\|ġwk\\|γwk\" SOD.txt | head -20",
 "description": "Grep Gharib for ywk/yuk"
}
```


### [2026-09-06T02:19:45.829Z] TOOL RESULT

```
9957:ay/ikun   (»yyqwn)  ©<*ay«-/:a-/xa;  OP  *ayuka; 
11362:596  'pz'ywk  S 
19930:1875  »wywk  B  ojU^cuo 
27685:Pozayukst   ©elat.   ^'pyz'ywksth 
46834:nawan  ?  ©Yaghn.  now  ©pi  riwnnt   =*n'ywk 
46961:5842  n'ywk   M 
46962:nayuk  (n'ywq)  ©Av.  ndvaya%  OP  naviya 
46970:5843  n'ywq  =»  n*ywk 
46973:nayukawe  ^n'ywk 
46978:nayuk 
50427:nayukst   (*nywq)  ©elat.  adj.  ^n*ywk 
59422:patyukik  ? 
72331:9522  t>ywk   S(AL)  =¥  t)yw1k 
74913:9903  w'ywk   M,  S  Jj£^^j£± 
74914:wayuk   (w*ywq)  ©MP  wayug 
74921:9904  w*ywq  =»  w'ywk 
82946:ywk 
82964:11051  ywk   B,  M      {oy  y^>  j*)^^  i*€  i*j>  i*x5&  i*A*z 
82979:11052  ywq    C  =>  ywk 
82981:11053  ywk'Ps'k   S  =>  ywk  fs>k
```


## [2026-09-06T02:19:47.642Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '82940,82985p' SOD.txt",
 "description": "Gharib ywk entry"
}
```


### [2026-09-06T02:19:47.721Z] TOOL RESULT

```
yuhann 

John 
C2,  53R3 


ywk 


450 


JU»JLj  i^Jy^S 


(>)j. 


JJJ 


(^^r>>  <U-  <  jl£* 


11051  ywk   B,  M      {oy  y^>  j*)^^  i*€  i*j>  i*x5&  i*A*z 
yok   (ywq)   ©<*yauka 

teaching,  view,  doctrine 

GMS  1635;  TSP  p278;  BSTBL  pl45;  STii  3.60; 

C2  p236;  ywk\  ywleh,  SCE  59;  VJ  28b  n  p92; 

Padm.  29; Vim.  89,  171;  Frag.  Len.  91.2,  6; 

Sund.  AoFviii  1981,  21R  5  pl79;  ob.  ywqyy 

C2,  52V11,  68V15 

11052  ywq    C  =>  ywk 

11053  ywk'Ps'k   S  =>  ywk  fs>k 

11054  ywk  fs'k   M 
yok-fsak   (ywk'fJs'k) 
teachings
```


## [2026-09-06T02:19:57.706Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN ghuk ===\"; grep -n -i \"Frosch\" HRN.txt | head -10; echo \"=== HUB ghuk ===\"; grep -n -i \"Frosch\\|gūk\\|guk\" HUB.txt | head -10; echo \"=== PHD frog ===\"; grep -n -i \"frog\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -10",
 "description": "Grep Horn/Hubschmann/MacKenzie for frog"
}
```


### [2026-09-06T02:19:57.802Z] TOOL RESULT

```
=== HRN ghuk ===
9367:1082. vei^ey Frosch', arab. LW. vazayat 'Eidechsenart'.
9368:aw. vazayä' 'Frosch'; phlv. vazay, vazag.
9369:kurd. LW. vizdq 'Frosch' (H.-Sch.).
=== HUB ghuk ===
1263:bei 6reg. Magistros: Jemand fand einen Frosch
3350:dauen' = phi. gukar-Uan zu skr. vi-kar umwandeln .
5500:'wachsen*, skr. vi + Wzl. vardh; guvdh 'Zeuge* = phi. gukas,
5671:'Erlangung ?; 8) gukas 'Zeuge' --= np. guvah, skr. "^vikaga-":^
5695:gukds und in gumartan, dessen Entstehung aus "^vimartan
5750:Zeugniss' = phi. gukasth Shk. 247, Min. Gl. 95, np. guvah,
5752:= phi. gukarak 'digesting Shk. 246, np. guvara, da gu^
5776:stellung Ton gukas mit skr. vi'kag, Yon gukdrdk mit skr. vi'kar (oben
7508:202, skr. kuQ); guvah 'Zeuge' = phi. guka&^) Gl. and Ind.
8578:= phi. gukos und guvaridan Verdauen' = phi. gukarttan
=== PHD frog ===
PHD_mackenzie.txt:2400:frog [plwk I N juror] brilliance, brightness.
PHD_mackenzie.txt:2402:frogihistan, frogih- [plwkyh-stn ] shine.
PHD_mackenzie.txt:5153:wak [wk' I N bak] frog.
PHD_mackenzie.txt:5294:wazay [wzyl N -, bazay] frog.
PHD_mackenzie.txt:6088:both Joma; of - worlds do-axwanig.        brazisn, frog, payrog, spig.
PHD_mackenzie.txt:6634:forget fdmustan, az daxsag histan.           frog wak, wazay.
PHD_mackenzie.txt:7551:senseless abeboy, aboy, abeos.            shine brlizidan, drafsidan, frogih-
PHD_mackenzie.txt:8682:frogih-                    - AU;~ C2>    frezbanih             .-u~V~Q.)
PHD_mackenzie.txt:8683:frogihistan         \\~~~V               frezhanig            \~"""fZ..)de,)
PHD_mackenzie.txt:8684:frog
```


## [2026-09-06T02:20:05.324Z] TOOL CALL #41: WebSearch

```json
{
 "query": "ریشه‌شناسی واژه «غوک» حسن‌دوست فرهنگ ریشه‌شناختی زبان فارسی وزغ"
}
```


### [2026-09-06T02:20:15.854Z] TOOL RESULT

```
Web search results for query: "ریشه‌شناسی واژه «غوک» حسن‌دوست فرهنگ ریشه‌شناختی زبان فارسی وزغ"

Links: [{"title":"فرهنگ ریشه‌شناختی فارسی، محمد حسن‌دوست، 1393 تهران، فرهنگستان زبان و ادب فارسی، دورۀ پنج جلدی","url":"https://lsi-linguistics.ihcs.ac.ir/article_1976.html"},{"title":"فرهنگ ریشه‌شناختی زبان فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C_%D8%B2%D8%A8%D8%A7%D9%86_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"فرهنگ ریشه‌شناختی زبان فارسی | راهک","url":"https://raahak.com/?p=942"},{"title":"مقاله فرهنگ ریشه شناختی فارسی، محمد حسن دوست، ۱۳۹۳ تهران، فرهنگستان زبان و ادب فارسی، دوره پنج جلدی","url":"https://civilica.com/doc/1581142/"},{"title":"کتاب فرهنگ ریشه شناختی زبان فارسی(5جلدی) اثر محمد حسن دوست | ایران کتاب","url":"https://www.iranketab.ir/book/40213-farsi-language"},{"title":"کتاب فرهنگ ریشه‌شناختی زبان فارسی (جلد 5)","url":"https://fanuus.org/library/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AC%D9%84%D8%AF-5/"}]

بر اساس نتایج جستجو، اطلاعات مرتبط با فرهنگ ریشه‌شناختی زبان فارسی نوشتهٔ محمد حسن‌دوست پیدا شد:

فرهنگ ریشه‌شناختی زبان فارسی یک فرهنگ لغت اختصاصی برای ریشه‌شناسی زبان فارسی تألیف محمد حسن‌دوست است که در سال ۱۳۹۳ در پنج جلد و از سوی انتشارات فرهنگستان زبان و ادب فارسی چاپ و منتشر شده است. این کتاب در سی‌وسومین دورهٔ جایزهٔ کتاب سال جمهوری اسلامی ایران، در گروه «زبان‌های باستانی»، به‌عنوان اثر برگزیده شناخته شد.

پیشتر، در سال ۱۳۸۳، جلد نخست فرهنگی با همین نام، تألیف حسن‌دوست، شامل حروف «آ - ت»، از سوی فرهنگستان زبان و ادب فارسی منتشر شده بود. متن اصلی فرهنگ ریشه‌شناختی زبان فارسی (آ - ی) در جلدهای اول تا چهارم قرار دارد و مشتمل بر ۲۹۵۷ صفحه و حاوی ۵۵۱۴ مدخل است.

با این حال، نتایج جستجو شامل اطلاعات تفصیلی درباره ریشه‌شناسی خاص واژهٔ «غوک» یا رابطهٔ آن با واژهٔ «وزغ» نیست. برای کسب اطلاعات دقیق‌تر درباره این موضوع، ممکن است لازم باشد به خود کتاب مراجعه کنید یا جستجویی بیشتر انجام دهید.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T02:20:23.318Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/false",
 "prompt": "Quote the full etymology of \"false\" and, if present on the page, of \"fail\" and \"failure\" — including the Latin fallere and any PIE root given."
}
```


## [2026-09-06T02:20:24.970Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0el-",
 "prompt": "Does this reconstruction page exist? If so give the root, gloss and descendants. If it is a redirect or missing, say so."
}
```


### [2026-09-06T02:20:27.184Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T02:20:29.928Z] TOOL RESULT

```
# Etymology of "False," "Fail," and Related Terms

## False (adjective)
"late Old English, 'intentionally untrue, lying,' from Old French _fals_, _faus_ ... from Latin _falsus_ 'deceptive, feigned, deceitful, pretend,' ... past participle of _fallere_ 'deceive, disappoint,' which is of uncertain origin"

## Fail (verb)
"c. 1200, _failen_, 'be unsuccessful in accomplishing a purpose' ... from Old French _falir_ ... This is from Vulgar Latin _*fallire_, from Latin _fallere_ 'to trip, cause to fall;' figuratively 'to deceive, trick, dupe, cheat, elude; fail, be lacking or defective.'"

The page traces this to "a PIE root meaning 'to stumble' (source also of Sanskrit _skhalate_ 'to stumble, fail;' ... Greek _sphallein_ 'to bring or throw down,' _sphallomai_ 'to fall;' ... )" The Latin sense represents "a metaphorical shift from 'stumble' to 'deceive.'"

**Note:** The page does not contain a separate entry for "failure," only for "false" and "fail."
```


## [2026-09-06T02:20:56.283Z] TOOL CALL #44: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://www.etymonline.com/word/false' --note 'page 196, root Ghuel: Latin falsus/fallere \"of uncertain origin\"; fail entry links fallere to PIE *(s)ghwel- \"stumble\" (Gk sphallein), not Pokorny 489' 2>&1 | tail -2",
 "description": "Archive etymonline false"
}
```


## [2026-09-06T02:20:57.665Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%98%E0%A5%82%E0%A4%95",
 "prompt": "Give the Sanskrit entry for घूक (ghūka): meaning, etymology (is it called onomatopoeic/imitative?), and any cited source."
}
```


### [2026-09-06T02:20:58.769Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/eaa99f3631618ddd.txt
```


### [2026-09-06T02:21:05.527Z] TOOL RESULT

```
# Sanskrit Entry: घूक (ghūka)

**Meaning:** Owl

**Etymology:** The word is borrowed from Dravidian languages. The entry notes: "Originally onomatopoeic" in origin. Related forms include Tamil *kūkai*, Telugu *gūba*, and Kannada *gūbe*.

**Cited Sources:**
- Monier Williams (1899), *A Sanskrit–English Dictionary*, Oxford: Clarendon Press, page 378
- Mayrhofer, Manfred (2001), *Etymologisches Wörterbuch des Altindoarischen* [Etymological Dictionary of Old Indo-Aryan], volume III, Heidelberg: Carl Winter Universitätsverlag, page 171
- Turner, Ralph Lilley (1969–1985), *A Comparative Dictionary of the Indo-Aryan Languages*, London: Oxford University Press, page 243
```


## [2026-09-06T02:21:24.655Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 ghuel ===\"; grep -n \"hvárate\\|hvarate\\|zbarəmna\\|zürah\\|zurah\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo; echo \"=== NYB zur ===\"; grep -n \"zūr\\b\\|zwl\\|zūr \" NYB_vol2_glossary.txt | head -10; echo; echo \"=== AFM zur ===\"; grep -n \"زور\\|تزوير\" AFM.txt | head -10; echo; echo \"=== KLN gucken ===\"; grep -n -i \"gucken\\|Gauch\\|cuckoo\" KLN_1966.txt SKT.txt | head -10",
 "description": "Final batch of reference greps"
}
```


### [2026-09-06T02:21:24.748Z] TOOL RESULT

```
=== WLD Bd1 ghuel ===

=== NYB zur ===
880:az-var [’cwl] avaricious, covetous 704, — V. dz. Paz. äzür, NP äzvar, āzūr.
4531:zwly, Gr. v. Sbvauıs or orparela; Arm. lw. zaur < *zauur; Av. (1689 sq.) zävar-.
4562:zor [zwl, Ps. zwly; erroneously zwhl] strength, power, vigour 14. 158.15. 897, 10678; zwhl (v. zöhr) for zor 9415; as to 128’, v.s. v. täyitan. - MPrs zwr, the SW form corresponding to NW zavar (q. v.); NP zör, which in later pronunciation coincided with zur ‘lie’, OP zürah- ‘deceit’, züra-kara- ‘evil-doer’. — The orthographical confusion of zör with zöhr is very frequent.
4563:zörik [zwlyk] powerful 52*3.
4572:Zurvin [zwlw’n'] the god Time: ~ i akanärak Eternity 7734-11, — Av. (1684) zaurvan- ‘old age, decrepitude’; MPrth Prs zrw’n; Paz. zurug. Cf zarmān

=== AFM zur ===
708:( ܐܫ ) حرقة ܢܝܟ لحار زور زب ܢܡܝ 
902:السر ياني ܐ ܒܙܪ »ܐ بمنى بباع البزور. واما !6( بمنى حامل البازي فعرب عن 
1298:والزورّق ( ابو ععرو) + ول أدَ في العاجم 8 يدي شرق ادر و5 عدن القالن 
1438:سطوح ٠‏ زهره لازوردي الاون ورقة طويل ساقة واوراقة مرة ويقال له بالتركية قويون 
3230:الارائى ` ܙܪܢܦܐ ܨ زورنه والفرني 9111 والايطاليالي 50 ٠ويقال‏ 4 
3236:* (الزرفين) تعريب زورفين وهو حلقة للباب 
3400:00700 ܨ القوة ܐܪܪ 64 زور ( سُفاء الغليل ) ومنه ® والكردي 
3897:وقال في التاج في ترجمة السنبوق وهي لغة في السلبوك :«زورق سفر يعمل في سواحل 
5731:(اللازورد) 3 0 
7488:زور لهم 

=== KLN gucken ===
SKT.txt:3627:Cock  (0.  a  male  bird.  (^E.)  M.  E A.S.  cocc;  fiom  the  birds  ay.  'Ciy anon  rt»A/  coh!'  Ch.  C.  T.  Nun's  Pries Tale,  456.  CC  Gk.  mUxv,  the  cry  of  t cnckoo ;  W.  cog,  a  cuckoo.
SKT.txt:3644:lieiwern  A  cuckoo  and  a
SKT.txt:3647:»  L.)     F.    fpMC0u.  M  L. ntd^lMS,  a  cuckoo;  from •  Gk.  mt'fMwv^,    a   cuckoo  ; Sku  jMiVj,  a  cnckoo.    Cf. Aad  tee  Coo. a  p{t£  of  hay.  (ScJtnH.)     Dan. 1;  kc3.A«iitr, lamp. ball;  Swcd. "earth. 10  stick  «p  abruptly.    (CO as  la  «r  A  bkeirmJ,  cock -xArMM^A,  cock-fiosetl.
SKT.txt:4462:Cuckold.  Cuckoo  :  see  Oook  (i).
KLN_1966.txt:2805:anhydride,  anhydrid,  n.,  an  oxide  which  is  capable of  forming  an  acid,  if  added  to  water  (chem.)  — Formed  with  suff.  -ide  resp.  -id,  fr.  Gk.  cNoSpo;, ‘waterless’.  See  anhydrous, anhydrite,  n. ,  anhydrous  calcium  sulfate  (mineral.) —  Formed  with  subst.  suff.  -ite  fr.  Gk.  avuSpop, ‘waterless’.  See  next  word  and  cp.  prec.  word, anhydrous,  adj.,  containing  no  water  (chem!)  — Gk.  avuSpop,  ‘waterless’,  fr.  av-  (see  priv.  pref. an-)  and  u§o>p,  ‘water’.  See  hydro-.  For  E. -ous,  as  equivalent  to  Gk.  -op,  see  suff.  -ous. ani,  n.,  any  of  certain  black  birds  of  the  cuckoo family.  —  Sp.  ani.  Port,  ani,  fr.  Tupi  ani. anicut,  annicut,  n.,  a  dam  (Anglo-lnd.)  —  Tamil anai  kattu,  ‘dam  building’, anigh,  adv.,  new  (pseudo-archaic).  —  Formed on  analogy  of  afar,  etc.,  fr.  a-,  ‘on’,  and nigh.
KLN_1966.txt:3429:Arisaema,  n.,  a  genus  of  plants  of  the  arum  family (bot.).  —  ModL.,  lit.  ‘blood  of  arum’,  fr.  Gk. <xp[p,  ‘a  kind  of  arum’,  which  is  rel.  to  Spov, ‘cuckoopint’,  and  aTpioc,  ‘blood’  (see  Arum  and hemal);  so  called  from  the  red-spotted  leaves  of some  species.
KLN_1966.txt:3558:Arum,  n.,  a  genus  of  plants;  (not  cap.)  any  plant of  this  genus  (hot.)  —  L.,  fr.  Gk.  Spov,  ‘the cuckoopint’,  a  word  of  Egyptian  origin.  See Plinius,  Historia  Naturalis,  19,  96,  and  cp. Araceae.
KLN_1966.txt:5288:bola,  also  bolas,  n.,  an  implement  used  by  the Gauchos.  —  PI.  of  Sp.  bola,  ‘ball’,  fr.  L.  bulla, ‘boss,  knob’.  See  bill,  ‘document’.
KLN_1966.txt:6189:californium,  n.,  a  radioactive  element  ( chem .)  — ModL.,  named  after  the  University  of  Califor¬ nia.  For  the  ending  see  chem.  suff.  -ium. caliga,  n.,  a  heavy  military  shoe  ( Roman  antiq.) —  L.,  rel.  to  calx ,  gen.  calcis,  ‘heel’,  calcar, ‘spur’,  calceus,  ‘shoe’.  See  Calceolaria, caliginous,  adj.,  dim,  dark.  - —  L.  caliginosus,  fr. caligo,  gen.  caliginis ,  ‘darkness’,  fr.  I.-E.  base *qdl-,  ‘black,  spotted’,  whence  also  Gk.  y.rf.ic. Dor.  xaXf;,  ‘stain,  spot,  blemish’,  v.rfi'  (in Hesychius),  ‘cloud  wanting  water’,  OSlav.  kalu, ‘mud,  dirt’,  OIr.  caile,  ‘spot’,  but  OI.  kdlah, ‘black;  cuckoo’,  kali  (fern.),  ‘black  color,  night’, are  not  derived  from  this  base  (see  Albert Thumb,  Handbuch  des  Sanskrit,  II,  p.202).  Cp. the  related  base  *qel-,  ‘black,  spotted’,  whence Gk.  xsXaivo;,  ‘black’.  See  Celaeno  and  cp. Columba,  columbine.  For  the  ending  sec  suff.  -ous. Derivatives:  caliginous-ly,  adv.,  caliginous- ness,  n.
KLN_1966.txt:6299:See  prec.  word  and  adj.  suff.  -ate,  resp.  -ous. Campephagidae,  n.,  a  family  of  birds,  the  cuckoo shrike  (ornithol.)  —  ModL.,  lit.  ‘caterpillar eaters’,  formed  with  suff.  -idae  fr.  Gk.  xiu.Trr|, ‘caterpillar’,  and  the  stem  of  9ayefv,  ‘to  eat’.  For the  first  element  see  hippocampus,  for  the  second see  -phagous.
```


## [2026-09-06T02:21:36.167Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ghuel\\|ghyel\\|ghuel-\\|hvarate\\|hvárate\\|zürah\\|hrunati\\|hrunáti\" incoming/WLD/WLD_Bd1_pages.txt | head -10; echo \"---try fallo---\"; grep -n \"fallo\\|fallō\" incoming/WLD/WLD_Bd1_pages.txt | head -10",
 "description": "Grep Walde-Pokorny Bd1"
}
```


### [2026-09-06T02:21:36.249Z] TOOL RESULT

```
18207:Auffassungen von nnotpcbhog verzeichnet Boisacq 71, 1097 s. auch u. ghuel-                         ;
60934:                                            guer,- guere                    ghuel-                                         643
60972:ghuel- „sich kriimmen, von der geraden Richtung abbiegen (auch geistig
60977:irrt“, juhumnd-h     „miBgluckend“, vihruta-h „schadhaft. krank“, hrunati
61051:Ehrlich aaO. an: deXyco ..bezaubere" (sei ghuel-gu, doch siehe u. clhelgh-
61053:Yersuche u. dhelgh „schlagen‘), got. wilpeis ..wild" (angeblich ghueltijo
---try fallo---
61037:Bezz. BB. 5, 318,                  Schrader KZ. 30, 466, Yf. LEWb. 2                                       u. fallo          m. Lit. Boi-
61044:Tganeig Hes.) „betriige“; lat. fallo, -ere „tauschen, betriigen; unwirksam
61046:ausbiegen“' Gdf. {jlmJ.no, vgl. ai. hmndti ; fallo nicht nach Reichelt KZ. 46,
78999:LEWb. 2 u. fallo. — Eber got. dulps „Fest“, s. u. *dhdl- „bliihen‘                                       .       — Ai.
79006:                                                         s. v.).    Lat. fallo                     —
80985:anders Luft KZ. 36, 148 (: ai. dhvr- „betrfigen“, got. dwals, lat. fallo) und
80986:Ehrlich Z. idg. Sprgesch. 29 (: ai. hvrnati „tauscht“, fallo, cpyXoco, s. u. ghueV),
```


## [2026-09-06T02:21:38.717Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '60970,61000p;61035,61050p' incoming/WLD/WLD_Bd1_pages.txt",
 "description": "Read Walde-Pokorny ghuel entry"
}
```


### [2026-09-06T02:21:38.791Z] TOOL RESULT

```
324 f.) und ahd. Jcolo usw. (s. geu- „gliihen“) aus.

ghuel- „sich kriimmen, von der geraden Richtung abbiegen (auch geistig
          und sittlich) u. dgl.‘-
      Ai. hvdrate       von der geraden Richtung ab, geht schief macht
                             ..biegt
krumme Wege“, hvalati ..geht schief,    gerat auf Abwege, strauchelt, fallt,
irrt“, juhumnd-h     „miBgluckend“, vihruta-h „schadhaft. krank“, hrunati
..geht irre", Ptc. hruta-h und geneuert hvrtd-h, hiirchaii „geht schief, gleitet.
schwankt, fallt"; hvdras- n. ,,Krummung-\ hvara-h ,,Schlange‘         vihnU- f.                       £
                                                                                                          .



„Art Schlange oder Wurm“.
   Av. zbarsmtum ,,den krummgehenden", zbarafta- n. „FuB daevischer
Wesen“, sbarali- n. „Hugel ‘, surah- n. „Unrecht, Trug", np. r Hr ..falsch:
Liige“ (s. Bthl. Wb. 1697 m. Lit.                            i.



      Lit.      nuozvelnus ,.abschiissig“; zvaliis „geschickt:                       flink.       behend" („*sich
                                                                        1
leicht biegend")              ;   izvilnas „ schrag, schief- , puzcil-ti, -an „sich neigen", 5tm/-
Juoti „schaukeln, schw avken
                                           11
                                                :   prnhdnas „schrage, schief", pazitlnus ,,schrage,
absch iissig", athilas. -us „schroff, grob, hart, unhoflich, unbarmherzig" u. dgl.
      lett. zvel'u , zvel'u, srelt ,.wiilzen,                     fortbewegen. umwerfen; schlagen", red
„sich schwerfallig fortbewegen. sich walzen. umfallen ", sva'lsiities ..wanken.
schwanken". svnlns „schwankend“


Bezz. BB. 5, 318,                  Schrader KZ. 30, 466, Yf. LEWb. 2                                       u. fallo          m. Lit. Boi-
sacq    u. cpyXog),           ano-cpcoXiog              „triigerisch“             (r-stufig)       (fiir    andere Deutungs-
versuche s. u. labh- „beriihren“) cprjXog oder cpqXog „betrugerisch, tiiuschend“,
(pr]Xt]T>jg oder q-yXyryg ,,Betriiger“, cpyXoco (dor. cpaXoco cpaXmQdg' ziaoa-                               :



Tganeig Hes.) „betriige“; lat. fallo, -ere „tauschen, betriigen; unwirksam
machen; sich entziehen; unbemerkt bleiben" („*krumme Wege machen;
ausbiegen“' Gdf. {jlmJ.no, vgl. ai. hmndti ; fallo nicht nach Reichelt KZ. 46,
                 ;


344 zu slav. hlaznb, s. auch u. *bliel- ,.aufblasen“).       Mit Unrecht reiht
```


## [2026-09-06T02:21:48.957Z] TOOL CALL #49: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T02:21:49.004Z] TOOL RESULT

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


## [2026-09-06T02:21:55.676Z] TOOL CALL #50: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E0%A4%98%E0%A5%82%E0%A4%95' --note 'page 196, root Ghuk: Sanskrit ghūka- \"owl\" — Wiktionary/Mayrhofer EWAia III 171: Dravidian loan, originally onomatopoeic' 2>&1 | tail -2",
 "description": "Archive Sanskrit ghuka page"
}
```


### [2026-09-06T02:21:57.695Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3e4b97fa2b90d41d.txt
```


## [2026-09-06T02:25:19.680Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/gucken",
 "prompt": "Give the German entry for gucken: etymology (Middle High German form, origin, any imitative/onomatopoeic note), and meaning. Also say whether it is connected to Kuckuck/cuckoo."
}
```


## [2026-09-06T02:25:21.270Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"تزویر\\|تزوير\\|مزوّر\\|مزور\" incoming/MON/MON_2vol_Adena_v1_djvu.txt MON_part1.txt 2>/dev/null | head -10",
 "description": "Grep Moin for tazvir"
}
```


### [2026-09-06T02:25:21.329Z] TOOL RESULT

```
incoming/MON/MON_2vol_Adena_v1_djvu.txt:13458:تقلب» تزویر. اشکك سحات: باران. شک 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:13520:تزویر» مکر. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:30777:(ص‌مر.) پرحیله» پرتزویر. پرفسون» 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:30781:پرحیله» پرتزویر. سخت زیر ک» بسیار 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:40027:محال. (ا.) تزویر» مکرء حیله 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:54634:مکر؛ فریب» تزویر. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:54800:(عم.) شخص مزور و مردم آزار. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:61970:کند؛ مزور» حیله گر. کسی که چیزی را برای 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:70991:دورنگی» دورویی» نفاق» تزویر» ریاکاری. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:81287:سوسه: (ع)معتاه (.) (عم.) حقه» تزویر.
```


### [2026-09-06T02:25:25.481Z] TOOL RESULT

```
# German Entry: gucken

**Etymology:**
The word derives from Middle High German *gücken* and *guggen*, meaning "to look inquisitively, peek, peer." Its ultimate origin is uncertain. However, it may stem from a specialized use of Middle High German forms meaning "to cuckoo, call or cry like a cuckoo," traceable to Old High German *guckōn/gukkōn*.

**Connection to Cuckoo:**
Yes, there is a potential connection. The entry notes: "Perhaps from a specialised use of Middle High German _gücken_, _gucken_ ('to cuckoo, call or cry like a cuckoo')." The k-pronunciation is often attributed to Low German influence rather than direct cuckoo etymology, though this remains speculative.

**Meaning:**
In modern German, *gucken* is a colloquial verb meaning:
1. To look or direct one's gaze at something
2. To watch something for a duration
3. To have a certain facial expression (as a copulative verb)

The word is common in northern and central Germany but considered informal for standard written German.
```


## [2026-09-06T02:25:38.277Z] TOOL CALL #53: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/gucken' --note 'page 196, root Ghuk: German gucken — MHG gücken/gucken \"peek\", origin uncertain, perhaps from MHG \"to call like a cuckoo\"' 2>&1 | tail -2; ls site/pages/196.jpg 2>/dev/null || pdftoppm -f 196 -l 196 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg196 && echo done",
 "description": "Archive gucken page and render PDF page 196"
}
```


### [2026-09-06T02:25:40.260Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d921b237e5cbd98a.txt
site/pages/196.jpg
done
```


## [2026-09-06T02:25:41.772Z] TOOL CALL #54: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/196.jpg"
}
```


### [2026-09-06T02:25:41.811Z] TOOL RESULT

```

```


## [2026-09-06T02:25:54.066Z] AGENT

Now I'll write the verification file.


## [2026-09-06T02:32:33.663Z] TOOL CALL #55: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /home/sfmqrb/git/rishe/data/verification/page-196.json <<'JSONEOF'\n{\n  \"pdf_page\": 196,\n  \"book_page\": 166,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ghuel\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ǵʰwel- 'to bend, to turn aside from the straight line (also morally)'; adj. *ǵʰwelo- 'crooked'\",\n      \"note\": \"Pokorny IEW 489-490 heads the entry 'ghu̯el- „sich krümmen, von der geraden Richtung abbiegen (auch geistig und sittlich) u. dgl.‘; ghuelo-s „gekrümmt‘' — Nourai's gloss 'crooked, bent' and the label 'Indo-European' are exactly right, and his citation POK:489 is the right page. Walde-Pokorny I 643 f. has the identical entry. The palatal quality of the initial (*ǵʰ, not plain *gʰ) is guaranteed by Skt. hvárate, Av./OP z-, Lith. žvalùs, OCS zŭlŭ. Two reservations, both about the western branches and not about the root itself: Watkins/AHD does not list this root at all, and modern Latin etymology (Ernout-Meillet, Klein, de Vaan, Etymonline) detaches Latin fallō from it (see node #7). The Iranian branch — which is what the whole Persian/Arabic part of the chart hangs on — is solid.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ǵʰwel- به معنی «خمیدن، از راه راست منحرف شدن (چه در معنای مادی و چه در معنای اخلاقی)» است؛ پوکورنی در صفحهٔ ۴۸۹ فرهنگ ریشه‌شناختی هندواروپایی و والده-پوکورنی در جلد یکم صفحهٔ ۶۴۳ همین معنا را می‌آورند، پس ارجاع نورایی (POK:489) و برگردان او «کج، خمیده» درست است. کامی‌بودن همخوان آغازین (*ǵʰ نه *gʰ) از روی سنسکریت hvárate، اوستایی و پارسی باستان با z آغازین، و لیتوانیایی žvalùs و اسلاوی کهن zŭlŭ مسلّم است. دو نکتهٔ احتیاطی: واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage اصلاً چنین ریشه‌ای ندارد، و ریشه‌شناسان امروزی لاتین fallō را از این ریشه جدا می‌کنند (نگاه کنید به گرهٔ ۷). ولی شاخهٔ ایرانی — که تمام بخش فارسی و عربی نمودار بر آن استوار است — استوار و پذیرفته است.\",\n      \"sources\": [],\n      \"ref_check\": [\n        {\"ref\": \"POK:489\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 147 (= printed pp. 489-490, the printed folio numbers 489 and 490 appear inline in the OCR): 'ghuel- „sich krümmen, von der geraden Richtung abbiegen (auch geistig und sittlich) u. dgl.‘; ghuelo-s „gekrümmt‘' — and within the same entry 'av. ... zūrah- n. „Unrecht, Trug‘, npers. zur „falsch; Lüge‘ ... gr. φαλός ... φηλός „betrügerisch‘ ... lat. fallö, -ere „täuschen, betrügen‘'. Every branch Nourai draws is on that page.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I pp. 643-644 (WLD_Bd1_pages.txt lines 60972-61046)\", \"stance\": \"supports\", \"note\": \"'ghuel- „sich kriimmen, von der geraden Richtung abbiegen (auch geistig und sittlich) u. dgl.‘ ... Av. ... surah- [= zūrah-] n. „Unrecht, Trug‘, np. zūr „falsch: Lüge‘ (s. Bthl. Wb. 1697 m. Lit.) ... φηλός oder φαλός „betrügerisch, täuschend‘ ... lat. fallo, -ere'. Walde-Pokorny is Pokorny's own source ('WP. I 643 f.') and says the same.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins, AHD Indo-European Roots (1985), whole file\", \"stance\": \"silent\", \"note\": \"grep for 'ghwel', 'FALSE', 'FAIL', 'fallere' in AHD_watkins1985.txt returns nothing: Watkins has no *ghwel-/*ǵʰwel- root and does not assign false/fail to any PIE root.\"},\n        {\"src\": \"ARY\", \"where\": \"p. 331 (ARY_pages.txt, [pdf page 331], header 'زور (به چم \\\"نادرست و دروغ\\\") / ۳۳۱')\", \"stance\": \"supports\", \"note\": \"Aryanpur's word-family page for زور 'false, lie' gathers exactly Nourai's set: Avestan ZŪRAH, Pahlavi ZŪR, Sanskrit HVAR-, Greek, Latin FALLERE/FALSUS, French FAUX, English FALSE, Danish FALSK, Swedish FALSK, OCS/Russian, Lithuanian; cross-refs برهان قاطع, لغت‌نامه دهخدا ۱۳۰۹, فرهنگ معین ۱۶۰.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"zŭrah\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both languages have the neuter s-stem *ǵʰwel-os- > Indo-Iranian *ĵʰwaras- > Old Iranian zūrah- 'wrong, deceit' (the palatal *ǵʰ gives Indo-Iranian ĵʰ, Skt. h, Iranian z; the *-w- is absorbed with compensatory lengthening of the vowel, exactly as in Skt. hváras- n. 'crookedness', the same formation). Old Persian zūrah- is attested at Behistun IV 63-65: 'naiy draujana āham, naiy zūrakara āham ... naiy ... zūra akunavam' = 'I was not a liar, nor a wrongdoer ... I did no wrong'; the compound zūra-kara- 'evil-doer' presupposes *zurah-kara- with the s-stem. Younger Avestan has the same noun and the compound zūrō.jata- 'unlawfully/treacherously slain' (Yt 9.18, V 7.3), beside the unreduced sibling zbar- 'to walk crookedly' (zbarəmna-), which preserves the labial as zb-. So Nourai's twin label 'Avestan / Old Persian' is literally correct — Bartholomae marks the entry 'p. zūrah-, j. zūrah-'. The gloss 'lie, cheat' is a shade narrower than the 'wrong, deceit' of the dictionaries but not wrong.\",\n          \"derivation_fa\": \"واژهٔ zūrah- در هر دو زبان اوستایی متأخر و پارسی باستان به معنی «نادرستی، بیداد، فریب» به کار رفته و ستاکی است از نوع ساکن به -ah (پایانهٔ خنثای *-os هندواروپایی) از ریشهٔ *ǵʰwel-. همخوان کامی *ǵʰ در هندوایرانی به ĵʰ و سپس در ایرانی به z بدل شده (در سنسکریت به h، چنان‌که hváras- «کجی» دقیقاً همین ساخت است) و -w- در میان حذف شده و مصوّت را کشیده کرده است. در کتیبهٔ بیستون (ستون چهارم، بندهای ۶۳ تا ۶۵) داریم: naiy draujana āham, naiy zūrakara āham «نه دروغ‌زن بودم، نه بیدادگر»، و naiy zūra akunavam «بیداد نکردم». در اوستای متأخر نیز zūrō.jata- «به ناحق کشته‌شده» آمده است. برچسب «اوستایی/پارسی باستان» نورایی درست است؛ بارتولومه هم مدخل را با نشان «پارسی باستان و اوستایی جوان» می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:489\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 147 (printed p. 489): 'av. zbardmna- „krumm gehend‘, zbaraθa- n. ..., zbarah- n. „Hügel‘, zūrah- n. „Unrecht, Trug‘, npers. zur „falsch; Lüge‘'. Pokorny does not separately name Old Persian, but Bartholomae and Kent do (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. ~1697 (BRT.txt line 28216; cross-refs at lines 28219, 28220, 28364)\", \"stance\": \"supports\", \"note\": \"'p. zūrah-, j. zūrah- n. „Unrecht, Trug‘: naiy ṧakaurim naiy ... zūra akunavam „weder einem.. noch einem.. tat ich Unrecht‘ Bh.4.13'; also 'p. zūra-kara- Adj. „Unrecht tuend‘' and 'j. zūrō.jata- Adj. „unrechtmässig, verräterisch getötet‘'. The 'p.' (altpersisch) + 'j.' (jungawestisch) marking is precisely Nourai's double language label. Walde-Pokorny cites this as 'Bthl. Wb. 1697'.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, §105 (KNT.txt line 1331) and §119\", \"stance\": \"supports\", \"note\": \"'On zūra-kara „evil-doer‘ from *zurah-kara-, see §119' — Kent reconstructs the OP compound from the s-stem *zurah-, i.e. exactly the form Nourai puts in the box.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 643 (WLD_Bd1_pages.txt line ~60984)\", \"stance\": \"supports\", \"note\": \"'Av. zbarsmtum ..., zbaraθa- n. ..., zbarah- n. „Hügel‘, surah- [OCR for zūrah-] n. „Unrecht, Trug‘, np. zūr „falsch: Lüge‘ (s. Bthl. Wb. 1697 m. Lit.)'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"zŭr\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian zūr [Book Pahlavi zwl, Manichaean z'wr] 'false, deceitful' continues Old Iranian zūrah- with the ordinary Middle Persian loss of the old neuter s-stem ending (-ah > Ø, as in Av. manah- > MP menīšn's base man-, Av. raocah- > MP rōšn's base rōc). The compound zūr-gugāy 'false witness', zūr-gugāyīh 'false testimony' is a Zoroastrian legal term of the Sasanian books and is the exact Middle Persian ancestor of NP زورگواهی. Nourai supplies no reference for this box, but MacKenzie, Nyberg and Horn all give the form. Nyberg adds an important caution that justifies Nourai's numbering of the Persian reflex as 'zŭr 2': Book Pahlavi writes both zūr 'lie' and zōr 'strength' as zwl, and the two only became homophonous later in New Persian.\",\n          \"derivation_fa\": \"فارسی میانه (پهلوی) zūr، به خط پهلوی کتابی zwl و در مانوی z'wr، به معنی «دروغ، ناراست» دنبالهٔ همان zūrah- ایرانی باستان است؛ پایانهٔ ستاک خنثای -ah در فارسی میانه به‌کلّی افتاده است. ترکیب zūr-gugāy «گواه دروغ» و zūr-gugāyīh «گواهی دروغ» اصطلاحی حقوقی در متون زردشتی ساسانی است و نیای مستقیم «زورگواهی» فارسی نو است. نورایی برای این خانه ارجاعی نداده، ولی مکنزی، نیبرگ و هرن هر سه این صورت را می‌آورند. نیبرگ نکتهٔ مهمی می‌افزاید که شمارهٔ «زور ۲» نورایی را توجیه می‌کند: در پهلوی کتابی هم zūr «دروغ» و هم zōr «نیرو» را zwl می‌نویسند و این دو تنها در فارسی نو هم‌آوا شده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"Nourai gives refs=None for this box. Checked independently in MacKenzie (PHD), Nyberg (NYB) and Horn (HRN) — see consulted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p. 99 s.v. (PHD.txt lines 680-682; PHD_mackenzie.txt lines 5861, 5864)\", \"stance\": \"supports\", \"note\": \"'zūr [zwl | M zʿwr] false, deceitful.' and 'zūr-gugāy [zwlgwkʿdy | M zwrgwgʿy] false witness. ~īh: false testimony.'\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. zōr (NYB_vol2_glossary.txt line 4562)\", \"stance\": \"supports\", \"note\": \"'zōr [zwl ...] strength, power ... NP zōr, which in later pronunciation coincided with zur „lie‘, OP zūrah- „deceit‘, zūra-kara- „evil-doer‘.' Nyberg thus confirms the MP form and warns of the zōr/zūr homonymy — which is why Nourai numbers the New Persian word 'zūr 2'.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 674, p. 149 (HRN.txt lines 5945-5947)\", \"stance\": \"supports\", \"note\": \"'674. zur „falsch; Lüge‘. ap. zurah- (zūrah-); aw. zurō.jata-; phlv. zur, zūr|zat, zūr|guḵāsih, arm. LW. zur; ai. hvaras-.' — Horn puts the Pahlavi stage between Old Iranian and New Persian exactly as the chart does.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"zŭr 2 «زور»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian زور zur 'lie, falsehood' is the regular continuation of MP zūr, unchanged in form. It is a homonym, not a sense, of زور zōr 'strength, force' (< MP zōr < Av. zāvar- 'power'), and Nourai's '2' correctly separates them; the same care is taken by Horn (no. 674 zur 'falsch, Lüge' vs. no. 674b zōr 'Kraft, Gewalt'), Hübschmann and Nyberg. Surviving mainly in the compounds زورگو / زورگواهی 'false witness' and in the legal-religious vocabulary (شهادت زور), the word was largely displaced in everyday New Persian by دروغ (< OP drauga-). Armenian zur 'false, vain' is an independent Parthian/Middle Persian loan of the same word, which shows the form was already zūr in Middle Iranian. Nourai's reference HRN:147 is two pages off: Horn's entry is on p. 149.\",\n          \"derivation_fa\": \"«زور» به معنی «دروغ، ناراستی» دنبالهٔ بی‌تغییر zūr فارسی میانه است. این واژه هم‌آواست — و نه هم‌معنا — با «زور» به معنی «نیرو» که از zōr فارسی میانه و آن از zāvar- اوستایی می‌آید؛ شمارهٔ ۲ که نورایی به کار برده همین تفکیک را نشان می‌دهد و هرن (شمارهٔ ۶۷۴ در برابر ۶۷۴ب)، هوبشمان و نیبرگ نیز همین تفکیک را می‌کنند. این واژه بیشتر در ترکیب‌هایی چون «زورگو» و «شهادت زور» مانده و در کاربرد روزمره جای خود را به «دروغ» (از drauga- پارسی باستان) داده است. «زور» ارمنی نیز وام‌واژه‌ای مستقل از پارتی/فارسی میانه است و نشان می‌دهد صورت zūr در ایرانی میانه پیش از این وجود داشته. ادعای نورایی درست است؛ تنها ارجاع HRN:147 دو صفحه خطاست و مدخل هرن در صفحهٔ ۱۴۹ است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B2%D9%88%D8%B1\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:147\", \"status\": \"partial\", \"note\": \"Horn's entry is no. 674 on printed p. 149, not p. 147 (HRN.txt: line 5945 falls in leaf 170 = printed 149; leaf 168 = printed p.147 carries entries 661-666, zairi-gaona/zist/zafar/zalu/zelle/zem). Content fully supports: '674. zur „falsch; Lüge‘. ap. zurah- (zūrah-); aw. zurō.jata-; phlv. zur ...'.\"},\n            {\"ref\": \"ETM:67\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Riše-šenāsi (Etimoloji), Qoqnus 1374 — refs_online.json records no digital copy on any permitted platform (catalogue/purchase entries only).\"},\n            {\"ref\": \"POK:489\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 147: 'npers. zur „falsch; Lüge‘' stands in the ghuel- entry immediately after the Avestan forms.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt lines 7868-7869)\", \"stance\": \"supports\", \"note\": \"'np. paz. phl. zur „falsch, Lüge‘, arm. zur, ap. zurah- „Unrecht‘, zurakara- „der Unrecht thut‘, zd. zurah- in zurō-...' — the full chain NP ← Pahlavi ← OP/Avestan, with the Armenian loan.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Riše-hā p. 331\", \"stance\": \"supports\", \"note\": \"Headword 'زور (به چم “نادرست و دروغ”)' with Avestan ZŪRAH, Pahlavi ZŪR, and the European cognates; cross-refs to Borhan-e Qate', Dehkhoda 1309 and Mo'in 160.\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt line 4562\", \"stance\": \"supports\", \"note\": \"'NP zōr, which in later pronunciation coincided with zur „lie‘' — confirms both the NP form and the homonymy Nourai's '2' guards against.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Arabic\",\n          \"words\": \"zŭr; tazvîr; mozavver\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic زُور zūr 'falsehood, perjury' (Qur'an 22:30 qawl al-zūr, 25:4 and 25:72, 58:2) is a loan from Middle Persian zūr, taken over in the pre-Islamic or earliest Islamic period, most plausibly through the Sasanian-Arab contact zone of al-Ḥīra. Once in Arabic the consonant skeleton z-w-r was reanalysed as a native triliteral root and merged with the genuine Arabic z-w-r 'to incline, swerve; to visit' (zawira 'be crooked', azwar, zāra), which is why the Arab lexicographers derive zūr from zāra — a derivation Jeffery calls 'clearly a denominative' and rejects. On the reanalysed root Arabic then built the productive Form II زَوَّرَ zawwara 'to falsify, forge', with verbal noun تَزْوِير tazwīr 'falsification, forgery, pretence' and participles مُزَوِّر muzawwir 'forger, falsifier' (agent) and مُزَوَّر muzawwar 'falsified, counterfeit' (patient). Nourai's gloss 'mozavver : liar' is therefore loose: the shape he writes is the passive participle 'falsified'; the 'liar/forger' sense belongs to muzawwir, though Persian usage of مزوّر does mean 'deceitful person'. Note also that the arrow is drawn from Pahlavi, not from New Persian — which is exactly what Jeffery concludes ('probably directly from Middle Persian').\",\n          \"derivation_fa\": \"«زُور» عربی به معنی «دروغ، شهادت دروغ» (قرآن: ۲۲/۳۰ «قول الزور»، ۲۵/۴ و ۷۲، ۵۸/۲) وام‌واژه‌ای است از zūr فارسی میانه که احتمالاً پیش از اسلام و از راه حیره وارد عربی شده است. پس از وام‌گیری، سه همخوان ز-و-ر در عربی همچون ریشه‌ای بومی بازتحلیل شد و با ریشهٔ اصیل عربی ز-و-ر به معنی «کج شدن، منحرف شدن؛ دیدار کردن» درآمیخت؛ به همین سبب لغویان عرب «زور» را از «زارَ» گرفته‌اند، ولی جفری این را «آشکارا اشتقاق برساخته» می‌داند و رد می‌کند. بر همین ریشهٔ بازتحلیل‌شده باب تفعیل ساخته شد: زَوَّرَ «جعل کردن»، مصدر تَزْویر، و اسم فاعل مُزَوِّر و اسم مفعول مُزَوَّر. برگردان نورایی از «مزوّر» به «دروغ‌گو» اندکی نادقیق است؛ مُزَوَّر یعنی «جعل‌شده» و «جعل‌کننده» مُزَوِّر است، هرچند «مزوّر» در فارسی به معنی «مردِ دورو و فریبکار» به کار می‌رود. نکتهٔ درست دیگر نمودار این است که پیکان از پهلوی کشیده شده نه از فارسی نو — و این همان نتیجه‌ای است که جفری می‌گیرد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B2%D9%88%D8%B1\"],\n          \"ref_check\": [\n            {\"ref\": \"ETM:67\", \"status\": \"not_checked\", \"note\": \"Abolghasemi's Riše-šenāsi has no digital copy (refs_online.json: 'RE-SEARCH 2026-09: no digital copy on any permitted platform').\"},\n            {\"ref\": \"VDQ:240\", \"status\": \"supports\", \"note\": \"VDQ is Badre'i's Persian translation of Jeffery's Foreign Vocabulary of the Qur'ān; the noorlib viewer is JavaScript-only and cannot be fetched, so per refs_online.json's own instruction the substance was checked in the English original at the corresponding entry, FVQ pp. 155-156 s.v. (Zūr): 'It would seem rather to be of Iranian origin. Pers. زور is lie, falsehood ... not only does the word occur in Phlv. both simply as zur, a lie, falsehood, fiction, and in compounds as zur-gukawāh = false evidence, perjury ... but also in the O.Pers. of the Behistun inscription ... so that it was probably directly from Middle Persian [that it was borrowed].'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'ān pp. 155-156 s.v. زور (FVQ.txt lines 9853-9905)\", \"stance\": \"supports\", \"note\": \"'The usual theory of the philologers is that it is derived from [زار] though this is clearly a denominative ... Fraenkel, Fremdw. 273, suggested that it was from [Heb.] ... it seems hardly possible to derive the Arabic from this. It would seem rather to be of Iranian origin ... Vullers, Lex. ii, 158, gives [Pers. زور] as a loan-word from Arabic. He is certainly wrong, however ...'\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen s.v. زور (PLA_asbaghi_1988_ia_djvu.txt line 11328)\", \"stance\": \"supports\", \"note\": \"'زور - zur: „Lüge‘ < pers. زور zur, mp. zur, aw. zūrah-' — Asbaghi lists it among the Persian loanwords in Arabic, with exactly Nourai's chain. (The neighbouring line 11331 keeps the other زور 'Kraft' < pers. zor, mp. zor/zawar, Av. zavar- separate, confirming the two-homonym analysis.)\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur p. 331, یادداشت (note)\", \"stance\": \"supports\", \"note\": \"'این واژه عربی نیست و شکل عربی آن از فارسی گرفته شده است' = 'this word is not Arabic; its Arabic form is taken from Persian'.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-Fārisiyya al-Muʿarraba (AFM.txt, grep زور)\", \"stance\": \"silent\", \"note\": \"Addi Shir has no headword for زور 'falsehood' (only incidental occurrences and unrelated entries such as الزورق, الزرفين); he does not include it in his list of Persian arabicisms.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"tazvîr «تزویر»; mozavver «مزوّر»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A textbook Persian → Arabic → Persian round trip. The Iranian etymon (MP zūr) went into Arabic as zūr (node #4), was fitted there with Arabic Form-II morphology, and came back into New Persian after the conquest as two ordinary Arabic loanwords: تزویر tazvir 'forgery, dissimulation, hypocrisy' (Ar. verbal noun tafʿīl of zawwara) and مزوّر mozavvar 'deceitful, hypocritical; forged' (Ar. participle). Neither could have been formed inside Persian: the internal vowel pattern (ta-C₁C₂īC₃, mu-C₁aC₂C₂aC₃) is purely Arabic templatic morphology, which is what makes the return trip visible. Mo'in accordingly tags them [ع.] (Arabic) while using them throughout as normal Persian words for 'trickery, deceit'. So the words are Persian in use, Arabic in shape, and Iranian in root — exactly the three-step Nourai draws.\",\n          \"derivation_fa\": \"این خانه نمونهٔ کلاسیک «رفت‌وبرگشت» است: واژهٔ ایرانی zūr به عربی رفت، آنجا در قالب باب تفعیل ریخته شد، و پس از اسلام همچون دو وام‌واژهٔ عربی به فارسی بازگشت: «تزویر» (مصدر باب تفعیل از زَوَّرَ) به معنی «جعل، دورویی، فریب» و «مزوّر» (اسم مفعول) به معنی «جعلی؛ دورو و فریبکار». هیچ‌یک از این دو نمی‌توانست در درون فارسی ساخته شود، زیرا وزن‌های تَفْعیل و مُفَعَّل یکسره صرفِ قالبیِ عربی است؛ همین نشانهٔ آشکار وام‌گیری دوباره است. معین نیز این دو را با نشان [ع.] می‌آورد و در سراسر فرهنگ خود آنها را همچون واژه‌های عادی فارسی به معنی «مکر و حیله» به کار می‌برد. پس واژه در کاربرد فارسی است، در ساخت عربی، و در ریشه ایرانی — دقیقاً همان سه گام که نورایی رسم کرده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B2%D9%88%D8%B1\"],\n          \"ref_check\": [\n            {\"ref\": \"ETM:67\", \"status\": \"not_checked\", \"note\": \"No digital copy of Abolghasemi's Riše-šenāsi exists on any permitted platform (refs_online.json).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi (2-vol Adena abridgement, vol. 1: MON_2vol_Adena_v1_djvu.txt lines 13458, 13520, 40027, 54634, 54800, 70991)\", \"stance\": \"supports\", \"note\": \"تزویر is used throughout as a Persian gloss for 'تقلب', 'مکر', 'فریب', 'دورویی، نفاق، ریاکاری', and مزوّر in 'شخص مزور و مردم آزار' — confirming both the Persian currency of the words and Nourai's senses 'pretence' and (in Persian usage) 'deceitful person'.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi s.v. زور (PLA line 11328)\", \"stance\": \"supports\", \"note\": \"Asbaghi's entry establishes the Arabic stem as a Persian loan, which is the premise of the round trip; the Form-II derivatives are Arabic formations on that borrowed stem.\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery pp. 155-156\", \"stance\": \"supports\", \"note\": \"Jeffery notes the Arabic word's Middle Persian origin and explicitly corrects Vullers, who had (wrongly) taken Persian زور itself to be an Arabic loan — the mirror-image error to the one this node avoids.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Greek\",\n          \"words\": \"phalos\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek φηλός (Doric φαλός) 'deceitful, cheating', with the verb φηλόω (Doric φαλόω) 'I deceive' and the agent noun φηλητής 'deceiver'; Hesychius also glosses φαλός 'stammering, foolish' and φαλιπτει·μωραίνει. Initial φ- is the regular dialectal outcome of *ǵʰw-, on the model of Aeolic/Doric φήρ beside Attic θήρ 'wild beast' < *ǵʰwēr- (whose palatal is guaranteed by Lith. žvėrìs, OCS zvěrь, just as the palatal of *ǵʰwel- is guaranteed by Lith. žvalùs, OCS zŭlŭ). Both Pokorny and Walde-Pokorny place these Greek words in this root without qualification. Nourai's gloss 'lie' is loose — φαλός/φηλός is the adjective 'deceitful' and φαλόω the verb 'to deceive', not the noun 'a lie' — and it should be noted that the Greek forms are lexicographers' words (Hesychius, glossaries) rather than words of the living literary language, which is why some Hellenists leave them unexplained.\",\n          \"derivation_fa\": \"واژهٔ یونانی φηλός (در گویش دوری φαλός) «فریبکار، دغل» با فعل φηλόω / φαλόω «فریب می‌دهم» و اسم فاعل φηλητής «فریبکار» به همین ریشه بازمی‌گردد. آوای آغازین φ دگرگونی گویشی منظمِ *ǵʰw- است، درست همان‌گونه که φήρ در آیولی/دوری در برابر θήρ آتیکی «جانور وحشی» از *ǵʰwēr- پدید آمده؛ کامی‌بودن این همخوان از روی لیتوانیایی žvėrìs و اسلاوی کهن zvěrь ثابت است، همچنان که در ریشهٔ ما از روی žvalùs و zŭlŭ. هم پوکورنی و هم والده-پوکورنی این واژه‌ها را بی‌هیچ تردیدی زیر همین ریشه می‌آورند. تنها ایراد، برگردان نورایی است: φαλός صفت است به معنی «فریبکار» نه اسم «دروغ». ادعای نورایی با این ملاحظهٔ کوچک پذیرفتنی است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:489\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 147 (printed pp. 489-490): 'gr. φαλιπτει· μωραίνει Hes., φαλός „stammelnd, töricht‘ Hes. ... vielleicht auch ἀπο-φώλιος „trügerisch‘ (ō-stufig), φηλός „betrügerisch‘, φηλητής „Betrüger‘, φηλόω (dor. φαλόω) „betrüge‘'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 644 (WLD_Bd1_pages.txt lines 61037-61044)\", \"stance\": \"supports\", \"note\": \"'ἀπο-φώλιος „trügerisch‘ (ō-stufig) ... φηλός oder φαλός „betrügerisch, täuschend‘, φηλητής oder φαλητής „Betrüger‘, φηλόω (dor. φαλόω ... Hes.) „betrüge‘'. Note WLD's spelling φαλός is precisely Nourai's 'phalos'.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, Dict. étym. de la langue latine, s.v. fallo (LAT.txt lines 20404-20406)\", \"stance\": \"partial\", \"note\": \"'Les rapprochements avec gr. φαλός, φηλός „trompeur‘, ou avec got. dwals, ou avec skr. hvarati „il va de travers‘, v.sl. zŭlŭ, sont vagues.' Ernout-Meillet know the Greek words with Nourai's exact glosses but consider the comparison of the whole set loose; their doubt bears above all on the Latin member (node #7).\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, whole file\", \"stance\": \"silent\", \"note\": \"No entry for this root and no Greek φηλός/φαλός.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Latin\",\n          \"words\": \"fallô-ere; falsus\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Latin facts are not in doubt: fallō, fefellī, falsum, fallere 'to deceive, disappoint; to escape notice, be hidden', with the past participle falsus turned adjective 'false, feigned, deceptive' (whence falsitās, fallāx, fallācia, and Vulgar Latin *fallīre, *fallita). What is disputed is the attachment to *ǵʰwel-. Pokorny 489 f. and Walde-Pokorny I 644 derive fallō from *ǵʰwl̥-nō- 'to make crooked paths, to swerve', comparing Skt. hrunāti 'goes astray' — which is exactly what Nourai's arrow draws. But modern Latin etymology does not follow them: Ernout-Meillet conclude 'Les rapprochements avec gr. φαλός, φηλός ... ou avec skr. hvarati ... sont vagues. En somme, étymologie embarrassante'; Klein says falsus is from fallere 'which is of uncertain etymology'; Watkins/AHD assigns false and fail to no PIE root at all; and the currently preferred account (de Vaan, followed by Etymonline) puts fallō under a root meaning 'to stumble, trip' — Greek σφάλλω 'to trip, throw down', Sanskrit skhálate 'stumbles' — with a metaphorical shift 'trip somebody up' → 'deceive'. Ernout-Meillet add a formal argument of their own: falsus shows that fallō must rest on *fald-ō or *faln-ō, which is not what *ǵʰwl̥-nō- predicts. A second, smaller point: Nourai's gloss 'falsus : lie' is wrong — falsus is an adjective 'false, feigned', never the noun 'a lie'.\",\n          \"derivation_fa\": \"دربارهٔ خودِ داده‌های لاتین تردیدی نیست: fallō, fefellī, falsum, fallere «فریفتن، ناکام گذاشتن؛ پنهان ماندن» و اسم مفعول falsus که به صفت «دروغین، ساختگی» بدل شده است. آنچه مورد اختلاف است، پیوند این فعل با ریشهٔ *ǵʰwel- است. پوکورنی (صفحهٔ ۴۸۹) و والده-پوکورنی (جلد یکم صفحهٔ ۶۴۴) fallō را از *ǵʰwl̥-nō- «کج رفتن» می‌گیرند و با سنسکریت hrunāti «به بیراهه می‌رود» می‌سنجند — و پیکان نورایی دقیقاً همین است. اما ریشه‌شناسی امروزی لاتین این را نمی‌پذیرد: ارنو و مه‌یه می‌نویسند «این سنجش‌ها مبهم‌اند؛ خلاصه، ریشه‌شناسی‌ای دردسرساز»؛ کلاین می‌گوید ریشهٔ fallere «نامعلوم» است؛ واتکینز اصلاً برای false و fail ریشهٔ هندواروپایی قائل نیست؛ و رأی رایج امروز (دِ وان و به پیروی او Etymonline) fallō را با یونانی σφάλλω «به زمین زدن، لغزاندن» و سنسکریت skhálate «می‌لغزد» می‌پیوندد و تحول معنایی «پای کسی را گرفتن» ← «فریفتن» را در نظر می‌گیرد. ارنو و مه‌یه دلیل صوری هم می‌آورند: صورت falsus نشان می‌دهد که fallō باید بر *fald-ō یا *faln-ō استوار باشد. افزون بر این، برگردان نورایی از falsus به «دروغ» نادرست است؛ falsus صفت است. پژوهش امروزی این پیکان را رد می‌کند.\",\n          \"sources\": [\"https://www.etymonline.com/word/false\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:489\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 147 (printed p. 490): 'lat. fallö, -ere „täuschen, betrügen; unwirksam machen; sich entziehen; unbemerkt bleiben‘ („*krumme Wege machen; ausbiegen‘; *ghu͞l̥nō, vgl. ai. hrunāti)'. Pokorny does say what Nourai's arrow says; the problem is that Pokorny is no longer the current view here.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. fallo (LAT.txt lines 20360, 20395-20406)\", \"stance\": \"contradicts\", \"note\": \"'On voit par falsus que fallo doit reposer sur *faldo (toutefois on peut songer aussi à *falnō) ... Les rapprochements avec gr. φαλός, φηλός „trompeur‘, ou avec got. dwals ..., ou avec skr. hvarati „il va de travers‘, v.sl. zŭlŭ ..., sont vagues. En somme, étymologie embarrassante.'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein, Comprehensive Etym. Dict. s.v. false (KLN_1966.txt line 14336)\", \"stance\": \"partial\", \"note\": \"'... fr. L. falsus, pp. of fallere, „to deceive‘, which is of uncertain etymology.' Klein records the Latin chain but refuses the PIE root.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 644 (WLD_Bd1_pages.txt line 61044-61046)\", \"stance\": \"supports\", \"note\": \"'lat. fallo, -ere „täuschen, betrügen; unwirksam machen; sich entziehen; unbemerkt bleiben‘ („*krumme Wege machen; ausbiegen‘ Gdf. *ghu͞lnō, vgl. ai. hrunāti; fallo nicht nach Reichelt KZ. 46, 344 zu slav. blaznŭ ...)'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, whole file\", \"stance\": \"silent\", \"note\": \"grep for 'fallere', 'FALSE', 'ghwel' returns nothing: Watkins does not derive Latin fallō from any Indo-European root.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"false; fail; failure\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three descend from Latin fallere/falsus, so the arrow Latin → English is right; only the link from Latin up to the root is doubtful (node #7). (a) false: Latin falsus was borrowed into Old English very early as fals 'fraud, falsehood' (a Christian-Latin loan), then re-supplied in the 13th c. by Old French fals, faus (mod. faux) → Middle English fals → false; the sense 'intentionally untrue, lying' is the late Old English one. (b) fail: Latin fallere was reshaped in Vulgar Latin as a fourth-conjugation *fallīre 'to be lacking, come short', giving Old French falir/faillir → Middle English failen (c. 1200); the noun fail is from Old French faille. (c) failure: not a Latin word at all but an English refashioning — Anglo-French failer, the infinitive used as a noun (Middle English failer 'default', c. 1400), respelt -ure from the 1660s on the model of pleasure, seizure. The same verb also gave English fault (< OF faute < VL *fallita), default, fallacy, fallible and (via Italian) falsetto. Nourai's AHD:470,473 are the main-dictionary pages of the 1975 New College edition (fail, false), which is not the volume held locally.\",\n          \"derivation_fa\": \"هر سه واژه از fallere / falsus لاتین می‌آیند، پس پیکان «لاتین ← انگلیسی» درست است؛ تنها پیوند لاتین به ریشهٔ هندواروپایی مورد تردید است (گرهٔ ۷). «false»: falsus لاتین بسیار زود، در دورهٔ انگلیسی باستان، همچون fals «فریب» وام گرفته شد و سپس در سدهٔ سیزدهم از راه فرانسهٔ باستان fals/faus دوباره تقویت شد و به fals انگلیسی میانه و false امروزی رسید. «fail»: fallere لاتین در لاتین عامیانه به باب چهارم بدل شد (*fallīre «کم آمدن، از کار ماندن») و از آن falir/faillir فرانسهٔ باستان و failen انگلیسی میانه (حدود ۱۲۰۰ میلادی) پدید آمد. «failure» اصلاً واژه‌ای لاتین نیست، بلکه ساختی انگلیسی است: مصدر انگلونورمن failer که همچون اسم به کار می‌رفت (failer انگلیسی میانه، حدود ۱۴۰۰)، و از دههٔ ۱۶۶۰ به قیاس pleasure و seizure با پسوند -ure نوشته شد. از همین فعل، fault و default و fallacy و fallible نیز در انگلیسی هست. ادعای نورایی در این خانه درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/false\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:470,473\", \"status\": \"not_checked\", \"note\": \"Nourai's AHD numbers are pages of the main dictionary of the American Heritage Dictionary, New College Edition 1975 (p. 470 ~ fail, p. 473 ~ false), which is a lending-only scan; the copy on disk is only Watkins's Indo-European Roots appendix (AHD_watkins1985.txt), and that has no *ghwel- root and no fail/false entries, so the cited pages could not be inspected. Content verified instead in Klein, Skeat and Etymonline (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.vv. fail, false, fault (KLN_1966.txt lines 14304, 14336, 14456)\", \"stance\": \"supports\", \"note\": \"'fail, intr. and tr. v. — ME. faillen, failen, fr. OF. (= F.) faillir, fr. VL. *fallire, corresponding to L. fallere, „to deceive‘'; 'fail, n., failure. — ME. faille, faile, fr. OF. faille'; false '... fr. OF. fals, faus ... fr. L. falsus, pp. of fallere'; 'fault, n. — ME. faute, fr. OF. faute, fr. VL. *fallita'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. (SKT.txt lines 6261, 6302)\", \"stance\": \"supports\", \"note\": \"'Fail: see Fallible.' and 'False, Falter; see Fallible.' — Skeat groups fail and false under Latin fallere, as the chart does.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\", \"note\": \"No Indo-European root is assigned to false/fail in the appendix Nourai's AHD citation series usually points to.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Ghŭk, Ghŭkos\",\n      \"verdict\": \"disputed\",\n      \"modern_form\": \"not a reconstructible Indo-European root; Mann's *ghūkos (ghuk-) 'hoot, whoop' is a private grouping of independent onomatopoeic words\",\n      \"note\": \"Nourai copies Mann faithfully: IEC cols. 347-348 has 'ghūkos (ghuk-) „hoot, whoop‘: Skt. ghūkaḥ „owl‘; Per. γūk „frog‘; R gik „whoop‘; gikatʹ, v. id.; Cz. hek „groan‘ beside hykat „bray‘ ... MHG gucken, v. („cuckoo‘ fr. *ghug-). Extn. in Li. gūkčioti „sob‘' — so the citation IEC:347 is exact and the gloss 'hoot, whoop' is Mann's own. But the root has no standing outside Mann: Pokorny has no such entry (grep of POK_full.txt for 'ghūk/ghuk-/gucken' returns nothing), Walde-Pokorny has none, and Watkins/AHD has none. Mann's dictionary is notorious for assembling onomatopoeic look-alikes into 'roots'; here each member has its own, quite different explanation (Skt. ghūka- a Dravidian loan, Persian غوک an Iranian frog-word, German gucken a native expressive verb). What the set really shares is imitative sound-symbolism, which by its nature recurs independently and cannot establish common descent. Verdict: disputed at the root level, and consequently for every branch.\",\n      \"note_fa\": \"نورایی این نمودار را بی‌کم‌وکاست از مان گرفته است: در فرهنگ تطبیقی هندواروپایی مان، ستون‌های ۳۴۷ و ۳۴۸، آمده است «ghūkos (ghuk-) „هوهو کردن، هیاهو‘: سنسکریت ghūkaḥ „جغد‘؛ فارسی γūk „غوک‘؛ روسی gik „فریاد‘؛ چکی hek „ناله‘؛ آلمانی میانه gucken (فعل، „فاخته‘ از *ghug-)». پس ارجاع IEC:347 درست است و برگردان «هوهو، هیاهو» نیز از خود مان است. ولی چنین ریشه‌ای بیرون از کتاب مان اعتباری ندارد: نه پوکورنی چنین مدخلی دارد، نه والده-پوکورنی، نه واتکینز. فرهنگ مان به گردآوردن واژه‌های آوایی همانند زیر عنوان «ریشه» شهره است، حال آنکه هر یک از اعضای این دسته توضیح جداگانه‌ای دارد: ghūka- سنسکریت وام‌واژه‌ای دراویدی است، «غوک» فارسی واژه‌ای ایرانی برای قورباغه، و gucken آلمانی فعلی بومی و تقلیدی. آنچه این واژه‌ها را به هم می‌پیوندد ریشه‌شناسی عامیانهٔ آوایی است نه خویشاوندی تاریخی؛ نام‌آوایی به‌طبع در زبان‌های بی‌ربط هم پدید می‌آید. پژوهش امروزی این ریشه را نمی‌پذیرد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%E0%A4%98%E0%A5%82%E0%A4%95\",\n        \"https://en.wiktionary.org/wiki/%D8%BA%D9%88%DA%A9\",\n        \"https://en.wiktionary.org/wiki/gucken\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"IEC:347\", \"status\": \"supports\", \"note\": \"IEC.txt lines 5051 and 5061, with the printed column numbers 347 and 348 visible inline in the OCR: 'ghūkos (ghuk-) „hoot, whoop‘ Skt. ghūkah „owl‘; Per. γūk „frog‘; R gik „whoop‘ ... MHG gucken, v. („cuckoo‘ fr. *ghug-).' Mann's entry begins in col. 347 and finishes in col. 348, so Nourai's page number is right.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"POK_full.txt (whole database dump), grep 'ghūk', 'ghuk-', 'gucken'\", \"stance\": \"silent\", \"note\": \"No hits: Pokorny's IEW has no root of this shape and does not treat Skt. ghūka- or Pers. γūk anywhere.\"},\n        {\"src\": \"WLD\", \"where\": \"WLD_Bd1 and WLD_band3, grep 'ghūk', 'ghuk'\", \"stance\": \"silent\", \"note\": \"The only hit is an unrelated Sanskrit aorist form (aghukkā to guh- 'hide'). Walde-Pokorny has no *ghuk- root.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\", \"note\": \"No such root in the Indo-European Roots appendix.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"ğŭk «غوک» (variant غوق)\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Persian word is real and the gloss is right: غوک ġuk 'frog, toad', with the by-form غوق noted in brackets on the chart and in Mo'in (whose entry reads 'غوک | غوق ... قورباغه'), so the extraction's script_extra matches the book. What is wrong is the derivation. No Iranian authority derives غوک from an Indo-European root: the inherited Iranian word for 'frog' is *wazaga- — Av. vazaġa-, MP wazay/wazag, NP وزغ vazaγ (Horn no. 1082) — and MacKenzie gives a second Middle Persian frog-word wak [wkʼ]. Wiktionary, citing Dehkhoda, calls غوک a borrowing from Sogdian ġwk with cognates in Ormuri and Parachi; but Gharib's Sogdian dictionary, the standard lexicon, has only cyz- (cayz) 'frog, toad' (no. 3185) and no ġwk, so that route is not corroborated either. The most that can be said is that ġuk is an expressive/imitative Iranian formation of Middle- or New-Iranian date, perhaps remodelled on or contaminated with wak; its resemblance to Sanskrit ghūka- 'owl' and German gucken is coincidence of sound-imitation, not shared inheritance.\",\n          \"derivation_fa\": \"خودِ واژه و معنایش درست است: «غوک» به معنی قورباغه، با گونهٔ «غوق» که هم در کتاب نورایی داخل قلاب آمده و هم در فرهنگ معین («غوک | غوق ... قورباغه») ثبت است؛ پس خوانش اسکن با کتاب می‌خواند. آنچه نادرست است ریشه‌شناسی آن است. هیچ ایران‌شناسی «غوک» را از ریشه‌ای هندواروپایی نمی‌گیرد: واژهٔ موروثیِ ایرانی برای قورباغه *wazaga- است — اوستایی vazaġa-، فارسی میانه wazay/wazag، فارسی نو «وزغ» (هرن، شمارهٔ ۱۰۸۲) — و مکنزی واژهٔ دومی هم در فارسی میانه دارد: wak. ویکی‌واژه به نقل از دهخدا «غوک» را وام‌واژه‌ای از سغدی ġwk می‌داند، ولی در فرهنگ سغدی قریب که مرجع استاندارد است تنها cyz- «قورباغه» (شمارهٔ ۳۱۸۵) آمده و از ġwk نشانی نیست. بیشترین چیزی که می‌توان گفت این است که «غوک» ساختی نام‌آوا و متأخر در ایرانی است، شاید زیر تأثیر wak. شباهت آن به ghūka- سنسکریت و gucken آلمانی تصادفِ تقلید آواست، نه هم‌ریشگی. پژوهش امروزی پیکان نورایی را نمی‌پذیرد.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%BA%D9%88%DA%A9\"],\n          \"ref_check\": [\n            {\"ref\": \"IEC:347\", \"status\": \"supports\", \"note\": \"Mann col. 347 does list 'Per. γūk „frog‘' under ghūkos, exactly as Nourai draws it — but Mann gives no Iranian intermediate forms and cites no Iranist.\"},\n            {\"ref\": \"MON:2454\", \"status\": \"partial\", \"note\": \"Mo'in's page numbers cannot be mapped online and the 6-vol print is not on disk; the 2-vol Adena abridgement (MON_2vol_Adena_v2_djvu.txt lines 3423-3427) has 'غوک: غوق | (جاذ.) غوکان ج. غوکک ... قورباغگان ... (جان.) گاهی مرادف با دوزیستان بکار رود ... غوک سبز ... غوک چوب'. The headword, the sense and the variant غوق are Mo'in's; but Mo'in offers no etymology there, so the citation supports the word, not the derivation.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD_mackenzie.txt lines 5153, 5294, 6634)\", \"stance\": \"contradicts\", \"note\": \"'wak [wkʼ | N bak] frog' and 'wazay [wzy | N -, bazay] frog'; the English-Pahlavi index reads 'frog wak, wazaȳ'. Middle Persian has no *ġūk, so the New Persian word cannot be an inherited continuation through Middle Persian.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 1082 (HRN.txt lines 9367-9369)\", \"stance\": \"partial\", \"note\": \"'1082. vazaġ „Frosch‘, arab. LW. vazaġat „Eidechsenart‘. aw. vazaġa- „Frosch‘; phlv. vazaġ, vazag.' Horn's Persian etymological grundriss treats only وزغ and is silent on غوک — i.e. he saw no Old Iranian etymology for it.\"},\n            {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary no. 3185 (SOD.txt line 28532) and the English index (line 89814)\", \"stance\": \"contradicts\", \"note\": \"'3185 cyz- B / cayz ... frog, toad' is Gharib's only word for 'frog'; there is no ġwk headword (SOD line 82964 'ywk' is yok 'teaching, doctrine' < *yauka). The Sogdian-loan story repeated from Dehkhoda is not supported by the standard Sogdian lexicon.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', vol. 4 s.v. وزغ (BQT_v4_pages.txt lines 14611, 14616, 14631) and vol. 3 line 15458\", \"stance\": \"partial\", \"note\": \"Borhan uses غوك throughout as the plain Persian gloss of وزق/ضفدع: '(رك: وزق) قورباغه، غوك، ضفدع' and 'معروف است و او را غوك خوانند و بعربی ضفدع'. The word and sense are confirmed for the 17th century; Mo'in's etymological footnotes give it no Old Iranian ancestor.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"ghŭkah\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Sanskrit घूक ghūka- m. 'owl' is a real word with the right meaning (Monier-Williams 1899, p. 378), so Nourai has copied Mann correctly. But it is not an inherited Indo-European word: Mayrhofer, Etymologisches Wörterbuch des Altindoarischen III 171, treats it as a borrowing from Dravidian — compare Tamil kūkai, Telugu gūba, Kannada gūbe 'owl' — the Dravidian word itself being onomatopoeic, from the owl's hooting 'ghū-ghū'; Turner's CDIAL 243 registers only the Indo-Aryan continuations. It is also late: ghūka- belongs to the classical, not the Vedic, lexicon, which is what one expects of a loan. So the resemblance to Persian غوک and German gucken is the ordinary convergence of hoot-words, and there is no descent from a common Indo-European ancestor to draw.\",\n          \"derivation_fa\": \"واژهٔ سنسکریت घूक (ghūka-) به معنی «جغد» واقعی است و معنایی که نورایی داده درست است (مونیه-ویلیامز، صفحهٔ ۳۷۸)؛ پس نورایی مان را درست نقل کرده است. اما این واژه میراث هندواروپایی نیست: مایرهوفر در فرهنگ ریشه‌شناختی هندوآریایی باستان (جلد سوم، صفحهٔ ۱۷۱) آن را وام‌واژه‌ای از زبان‌های دراویدی می‌داند — سنجیده با تامیلی kūkai، تلوگویی gūba و کانادایی gūbe «جغد» — و خودِ واژهٔ دراویدی نام‌آواست و از بانگ «غوغو»ی جغد گرفته شده است. افزون بر این، ghūka- واژه‌ای متأخر و کلاسیک است نه ودایی، و همین دیرآیندی با وام‌بودن آن سازگار است. پس شباهت آن به «غوک» فارسی و gucken آلمانی همان همگرایی همیشگیِ واژه‌های نام‌آواست. پژوهش امروزی این پیکان را رد می‌کند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%98%E0%A5%82%E0%A4%95\"],\n          \"ref_check\": [\n            {\"ref\": \"IEC:347\", \"status\": \"supports\", \"note\": \"Mann col. 347: 'ghūkos (ghuk-) „hoot, whoop‘ Skt. ghūkah „owl‘' — the Sanskrit form and gloss are Mann's, and he makes it the head member of the group (the root is named after it).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"POK_full.txt, grep 'ghūk'/'ghuk'\", \"stance\": \"silent\", \"note\": \"Pokorny nowhere cites Skt. ghūka-; there is no root under which he could place it.\"},\n            {\"src\": \"WLD\", \"where\": \"WLD_Bd1_1930 / WLD_band3, grep 'ghūk'/'ghuk'\", \"stance\": \"silent\", \"note\": \"Only the unrelated aorist aghūkkā (root guh- 'to hide') is found; Walde-Pokorny does not know an IE etymology for ghūka-.\"},\n            {\"src\": \"web:Mayrhofer/Monier-Williams via Wiktionary\", \"where\": \"en.wiktionary.org/wiki/घूक (citing Mayrhofer EWAia III 171; Monier-Williams 1899 p.378; Turner CDIAL 243)\", \"stance\": \"contradicts\", \"note\": \"The entry glosses ghūka- 'owl', states it was borrowed from Dravidian (Tamil kūkai, Telugu gūba, Kannada gūbe) and that the word is 'originally onomatopoeic' — i.e. not inherited from any Indo-European root.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Middle German\",\n          \"words\": \"gucken\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Nourai's own source does not say what his box says. Mann (col. 348) writes 'MHG gucken, v. („cuckoo‘ fr. *ghug-)' — gucken is marked as a verb, its sense is the cuckoo's call, and Mann derives it not from *ghuk- but from a variant *ghug-. The box 'gucken : a kind of bird' therefore misreports Mann twice: it turns a verb into a bird name, and it hangs it directly on the head root. In German philology gucken (MHG gücken, guggen 'to peep, peer, look inquisitively', OHG guckōn/gukkōn) is of uncertain origin; the guess that it is a specialised use of a verb 'to call like a cuckoo' is offered as a possibility, not a fact, and the k-spelling is usually put down to Low German influence. The German cuckoo-noun is a separate word, MHG gouch 'cuckoo; fool' (< Proto-Germanic *gaukaz) beside the reduplicated Kuckuck, neither of which shows a form *ghuk-. Verdict: disputed — the gloss is wrong and the derivation is not even Mann's.\",\n          \"derivation_fa\": \"خانهٔ نمودار با مأخذ خودِ نورایی نمی‌خواند. مان در ستون ۳۴۸ می‌نویسد: «آلمانی میانه gucken، فعل („فاخته‘، از *ghug-)»؛ یعنی gucken را فعل می‌داند، معنایش را بانگ فاخته می‌گیرد، و آن را نه از *ghuk- بلکه از گونهٔ *ghug- می‌آورد. پس نوشتهٔ «gucken: نوعی پرنده» دو خطا دارد: فعل را به نام پرنده بدل کرده و آن را یک‌راست به ریشهٔ اصلی بسته است. در ریشه‌شناسی آلمانی، gucken (آلمانی میانه gücken، guggen «سرک کشیدن، نگریستن»، آلمانی باستان guckōn) خاستگاه نامعلومی دارد؛ این حدس که کاربردی ویژه از فعلی به معنی «چون فاخته بانگ زدن» باشد تنها یک احتمال است، و تلفظ با k را معمولاً به تأثیر آلمانی سفلی نسبت می‌دهند. نام فاخته در آلمانی واژه‌ای جداست: gouch آلمانی میانه (از ژرمنی آغازین *gaukaz) و Kuckuck مکرّر. خطای این خانه از آنِ کتاب است، نه خوانش اسکن.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/gucken\"],\n          \"ref_check\": [\n            {\"ref\": \"IEC:347\", \"status\": \"partial\", \"note\": \"The entry runs over into col. 348, where IEC.txt line 5061 reads 'MHG gucken, v. („cuckoo‘ fr. *ghug-)'. Mann has the word, but as a verb and from a variant root — not as 'a kind of bird' descending from *ghūk-, which is what the chart states.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein, Comprehensive Etym. Dict. (KLN_1966.txt, grep 'gucken', 'Gauch')\", \"stance\": \"silent\", \"note\": \"No entry for gucken or Gauch; Klein's 'cuckoo' material (s.v. cuckoo, cuckoopint) is unconnected to any *ghuk- root.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. (SKT.txt lines 3627, 3647, 4462)\", \"stance\": \"silent\", \"note\": \"Skeat derives cuckoo from OF coucou / L. cuculus / Gk. κόκκυξ / Skt. kokila, all imitative reduplications with -k-k-, and knows no *ghuk- family; he has no gucken.\"},\n            {\"src\": \"web:Wiktionary (German)\", \"where\": \"en.wiktionary.org/wiki/gucken\", \"stance\": \"partial\", \"note\": \"'From Middle High German gücken, guggen („to look inquisitively, peek, peer‘) ... ultimate origin uncertain. Perhaps from a specialised use of Middle High German gücken, gucken („to cuckoo, call or cry like a cuckoo‘), from Old High German guckōn, gukkōn.' The cuckoo link is entertained as a possibility, but the word is a verb meaning 'to peek', never a bird name.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-196.json > /dev/null && echo \"JSON OK\"",
 "description": "Write and validate page-196.json"
}
```


### [2026-09-06T02:32:38.120Z] TOOL RESULT

```
JSON OK
```


## [2026-09-06T02:32:41.682Z] TOOL CALL #56: Bash

```json
{
 "command": "python3 tools/verify_check.py 196",
 "description": "Run verify_check for page 196"
}
```


### [2026-09-06T02:32:43.430Z] TOOL RESULT

```
nodes verified: 11/11
node verdicts: {'confirmed': 7, 'disputed': 4}
root verdicts: {'confirmed': 1, 'disputed': 1}
ref checks: {'supports': 7, 'not_checked': 5, 'partial': 3}
books consulted: {'supports': 19, 'silent': 8, 'partial': 5, 'contradicts': 4} | by book: {'WLD': 4, 'AHD': 3, 'KLN': 3, 'PHD': 2, 'NYB': 2, 'HRN': 2, 'ARY': 2, 'FVQ': 2, 'PLA': 2, 'LAT': 2, 'SKT': 2, 'BRT': 1, 'KNT': 1, 'HUB': 1, 'AFM': 1, 'MON': 1, 'SOD': 1, 'BQT': 1, 'POK': 1, 'web:Mayrhofer/Monier-Williams via Wiktionary': 1, 'web:Wiktionary (German)': 1}
```


## [2026-09-06T02:33:03.700Z] AGENT

Page 196 (book p. 166) verified — `data/verification/page-196.json`, `verify_check.py 196` shows 0 PROBLEM lines.

**Counts** — 2 non-redirect entries, 11 nodes. Roots: 1 confirmed, 1 disputed. Nodes: 7 confirmed, 4 disputed. Ref checks: 7 supports, 3 partial, 5 not_checked. 21 `consulted` books (19 supports / 5 partial / 4 contradicts / 8 silent).

**Disputed items**
- **Ghŭk, Ghŭkos (ROOT)** — Mann's *ghūkos "hoot, whoop" (IEC 347‑348) is quoted exactly, but the root exists only in Mann: Pokorny, Walde‑Pokorny and Watkins/AHD have nothing. The three members are independent onomatopoeic words.
- **Ghŭk #1, Persian ğŭk «غوک» "frog"** — word and gloss right (Mo'in has غوک/غوق, matching the chart's bracketed variant), derivation wrong: the inherited Iranian frog‑word is *wazaga‑ (Horn 1082; MacKenzie *wazay*, *wak*). Wiktionary/Dehkhoda's "from Sogdian ġwk" isn't corroborated either — Gharib has only *cyz-* "frog" (no. 3185).
- **Ghŭk #2, Sanskrit ghŭkah "owl"** — real word, but Mayrhofer (EWAia III 171) makes it a Dravidian loan (Tamil *kūkai*, Telugu *gūba*), originally onomatopoeic, not IE.
- **Ghŭk #3, Middle German gucken "a kind of bird"** — Nourai misreads his own source: Mann writes "MHG gucken, **v.** ('cuckoo' fr. \*ghug-)" — a verb, from a *variant* root. gucken is MHG *gücken/guggen* "to peek", origin uncertain.
- **Ghuel #7, Latin fallô-ere / falsus** — Pokorny 489 f. does say what the arrow says, but modern Latin etymology detaches it: Ernout‑Meillet "étymologie embarrassante… les rapprochements… sont vagues"; Klein "of uncertain etymology"; Watkins/AHD has no such root; de Vaan/Etymonline prefer *sgʷʰh₂l‑ "stumble" (Gk. σφάλλω, Skt. *skhálate*). Also `falsus : lie` is a wrong gloss (adjective, not noun).

**Best confirmations** — the whole Iranian/Semitic spine of *Ghuel* is solid: Bartholomae has "p. zūrah-, j. zūrah- n. 'Unrecht, Trug'" (so Nourai's double label Avestan/Old Persian is literally right); Kent §105 on OP *zūra-kara-* < \*zurah-kara-; MacKenzie *zūr* "false, deceitful", *zūr-gugāy*; Jeffery FVQ 155‑156 and Asbaghi PLA both make Arabic زور a loan **from Middle Persian**, exactly as drawn; Aryanpur p. 331 notes «این واژه عربی نیست و شکل عربی آن از فارسی گرفته شده است».

**No extraction errors** (page image checked). Two data notes for the owner, both minor: (1) the printed Persian box reads «زور ۳» with a superscript ۳ that the JSON's `script` field drops (translit keeps "zŭr 2"); (2) `HRN:147` is Nourai's own slip — Horn's entry 674 *zur* 'falsch; Lüge' is on p. **149**.
