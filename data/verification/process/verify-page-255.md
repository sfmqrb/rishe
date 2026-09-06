# Verification process log — verify-page-255


## [2026-09-06T16:09:39.743Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 255 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-255.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-255.json. Write /home/sfmqrb/git/rishe/data/verification/page-255.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 255` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T16:09:42.161Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T16:09:42.855Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T16:09:42.870Z] TOOL RESULT

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


## [2026-09-06T16:09:43.229Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-255.txt"
}
```


### [2026-09-06T16:09:43.244Z] TOOL RESULT

```
1	=== PDF page 255 (book page 225) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kens : to speak solemnly, proclaim  (refs POK:566; WLD1:403)
4	#1 (parent #0) [Old Persian] refs=POK:566; KNT:188 | thah : to say, declare ; thâtiy : says
5	  #2 (parent #1) [Persian] refs=TZF:19 | soxan «سخن» : speech | NOTE: See "Kâs 2" for another possible root of "soxan"
6	#3 (parent #0) [Avestan] refs=POK:566; KNT:188 | sah 2 : to say, declare
7	  #4 (parent #3) [Persian] refs=IEC:608 | afsâneh «افسانه» : fable | extra: فسانه
8	#5 (parent #0) [Latin] refs=POK:566; AHD:1522 | cĕns-ĕre : to judge, estimate, tax
9	  #6 (parent #5) [French] refs=None | censur : censor
10	    #7 (parent #6) [Persian] refs=VOP:210 | sânsor «سانسور» : censor
11	  #8 (parent #5) [English] refs=AHD:1522 | censor, census
12	#9 (parent #0) [Greek] refs=AHD:301,1522 | kos-mein : to arrange in order ; kos-mĕtikos : skilled in beautifying ; kos-mos : arrangement, world | NOTE: A possible derivation from Indo-European "Kens".
13	  #10 (parent #9) [French] refs=AHD:301 | cosmetique : cosmetic
14	    #11 (parent #10) [Persian] refs=VOP:321 | mâtîk «ماتیک» : lipstick
15	    #12 (parent #10) [English] refs=AHD:301 | cosmetic
16	  #13 (parent #9) [English] refs=AHD | cosmos, cosmic
17	
```


## [2026-09-06T16:09:44.925Z] AGENT

I'll read the source JSON and reference index.


## [2026-09-06T16:09:46.345Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-255.json",
 "description": "Read page 255 source JSON"
}
```


### [2026-09-06T16:09:46.379Z] TOOL RESULT

```
{
  "pdf_page": 255,
  "book_page": 225,
  "entries": [
    {
      "root": {
        "name": "Kens",
        "lang": "Indo-European",
        "refs": "POK:566; WLD1:403",
        "gloss": "to speak solemnly, proclaim"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:566; KNT:188",
          "words": [
            {"translit": "thah", "gloss": "to say, declare", "script": null},
            {"translit": "thâtiy", "gloss": "says", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "TZF:19",
          "words": [
            {"translit": "soxan", "gloss": "speech", "script": "سخن"}
          ],
          "script_extra": null,
          "note": "See \"Kâs 2\" for another possible root of \"soxan\"",
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:566; KNT:188",
          "words": [
            {"translit": "sah 2", "gloss": "to say, declare", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "IEC:608",
          "words": [
            {"translit": "afsâneh", "gloss": "fable", "script": "افسانه"}
          ],
          "script_extra": "فسانه",
          "note": null,
          "quote": {
            "text": "ره زین شب تاریک نبردند برون - گفتند فسانه ای و در خواب شدند",
            "poet": "Khayyâm"
          }
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:566; AHD:1522",
          "words": [
            {"translit": "cĕns-ĕre", "gloss": "to judge, estimate, tax", "script": null}
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
          "words": [
            {"translit": "censur", "gloss": "censor", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "VOP:210",
          "words": [
            {"translit": "sânsor", "gloss": "censor", "script": "سانسور"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 5,
          "lang": "English",
          "refs": "AHD:1522",
          "words": [
            {"translit": "censor, census", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:301,1522",
          "words": [
            {"translit": "kos-mein", "gloss": "to arrange in order", "script": null},
            {"translit": "kos-mĕtikos", "gloss": "skilled in beautifying", "script": null},
            {"translit": "kos-mos", "gloss": "arrangement, world", "script": null}
          ],
          "script_extra": null,
          "note": "A possible derivation from Indo-European \"Kens\".",
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "French",
          "refs": "AHD:301",
          "words": [
            {"translit": "cosmetique", "gloss": "cosmetic", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "VOP:321",
          "words": [
            {"translit": "mâtîk", "gloss": "lipstick", "script": "ماتیک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 10,
          "lang": "English",
          "refs": "AHD:301",
          "words": [
            {"translit": "cosmetic", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 9,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "cosmos, cosmic", "gloss": null, "script": null}
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


## [2026-09-06T16:09:48.262Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','KNT','TZF','IEC','AHD','VOP','BRT','HRN','HUB','PHD','NYB','MON','BQT','ARY','KLN','SKT','CHEUNG','SYN','WEB','FSD']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-06T16:09:50.054Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فار
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09:
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
CHEUNG MISSING
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
```


## [2026-09-06T16:09:56.202Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','KNT','IEC','AHD','BRT','HRN','HUB','PHD','NYB','ARY','KLN','SKT','SYN','MON','BQT','FSD','WEB','TZF','VOP']:\n    v=d.get(k) or {}\n    print('==',k, '| local:', v.get('local_file'), '| offset:', v.get('page_offset'), '| hint:', (v.get('lookup_hint') or '')[:250])\n\"; ls data/verification/sources/refs/ | head -60"
}
```


### [2026-09-06T16:09:58.281Z] TOOL RESULT

```
== POK | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' .
== WLD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 1
== KNT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt | offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
== IEC | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== AHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are
== BRT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers 
== HRN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== HUB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== PHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== NYB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== ARY | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | offset: printed page = pdf page + 1 | hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built
== KLN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== SKT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== SYN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== MON | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | offset: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: show
== BQT | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode
== FSD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
== WEB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt | offset: not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.
== TZF | local: None | offset: None | hint: Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).
== VOP | local: None | offset: None | hint: Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).
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
```


## [2026-09-06T16:10:03.749Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\n# POK p.566 -> POK_01 leaf = p+8 = 574 (POK_01 covers pp 1-?), check\nawk 'BEGIN{RS=\"\\f\"} NR==575 || NR==574 || NR==576' POK_01.txt | head -80"
}
```


## [2026-09-06T16:10:04.672Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"k̂ens-\\|kens-\\|ḱens\" POK_full.txt | head -20"
}
```


### [2026-09-06T16:10:05.706Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-06T16:10:05.750Z] TOOL RESULT

```
9334:Root / lemma: ken-2, kens-, keni-, kenu-\ "to rub, scrape off; ashes' must have come from
```


## [2026-09-06T16:10:09.074Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"feierlich sprechen\\|k̂ens\\|kʷens\\|censere\" POK_full.txt | head -20; echo ---; ls POK*; wc -l POK_full.txt"
}
```


### [2026-09-06T16:10:09.131Z] TOOL RESULT

```
---
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
93771 POK_full.txt
```


## [2026-09-06T16:10:12.795Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in POK_01.txt POK_02.txt POK_03.txt; do echo \"$f: $(tr -cd '\\f' < $f | wc -c) leaves, $(wc -c <$f) bytes\"; done"
}
```


### [2026-09-06T16:10:14.727Z] TOOL RESULT

```
POK_01.txt: 363 leaves, 981836 bytes
POK_02.txt: 433 leaves, 1137861 bytes
POK_03.txt: 429 leaves, 1170809 bytes
```


## [2026-09-06T16:10:17.547Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=222 && NR<=224 {print \"=== leaf \" NR \" ===\"; print}' POK_02.txt | head -120"
}
```


### [2026-09-06T16:10:19.556Z] TOOL RESULT

```
=== leaf 222 ===
in  , drücken'  (germ.  -p[p]-,  vgl.:)  aisl.  Jinippa  , stoßen, stecken',  hnippask  , zanken',  mengl.  nippen  ,kneifen,  klemmen',  engl,  nip^ nd.  ndl.  nippen  , nippen',  nhd.  bair.  nipfen,  nipfeln  , nippen' ;  nd.  nibbeiert , abbeißen';  vielleicht  lit.  knimbü  u.  dgl.  (s.  o.  unter  kene-bh-),  wenn  mit altem  i-Yokalismus.
4.  s-Er Weiterung:  lit.  knisü,  kmsti  ,wühlen,  graben',  lett.  knidiy. knislis  , kleine  Mücke'.
IV.  u-Basis  kenu-j  kneu-:
1.  Gr.  xyd(/)og,  Tivovg  ,das  knarrende  Reiben  des  Rades  in  der  Rad- ächse;  Lärm  der  Füße  beim  Marschieren',  xvio)  ,kratze  leicht',  xvv^a ,däs  Kratzen,  leichte  Anpochen',  'Avvog  n.   , Krätze',   xvv'  IX&xigtov  Hes.;
aisl.  Jineggva,  hnqgg  (und  schwach  hnyggjd)  , stoßen'  (ursprüngl.  , reiben^ kratzen')  =  ahd.  hniuwan,  mhd.  niuwen  ,zerstoßen,  zerquetschen*  (ags. hnygelan,  Plur.  , Abschnitzel'  aus  *hnuvilan'?)',  ferner  mit  der  Bed.  ,karg* (vgl.  schäbig  :  schaben)  aisl.  hneggr  ,knapp,  karg,  sparsam',  ags.  hneavr ,karg,  knauserig',  mnd.  nouwe  ,eng,  schmal,  knapp,  gering,  genau*,  mhd- nouynouwe  ,eng,  genau,  sorgfältig',  nhd.  genau]
lett.  knüdu  und  knüsiu,  Inf.  knüt  und  knüst,  Prät.  knüdu  ,jucken'  (d(hy und  s^Präs.,  vgl.  mit  wurzelhaft  behandeltem  -c^-  Siuch  knudet  ds.);  poln- knowac    ,zerstückeln,    ästein',    knowie    ,Strohsplitter'  ?    (s.   auch  Brückner
-m  .t
563
}CZ.  45,  313  wegen  slav.  *k^n^  , Stamm',  *kzniga  ,Buch*,  worüber  anders Berneker  663,  664).
2.  Dentalerweiterungen: Mit  d:  gr.   xvv^a,   y,vvoa  , Krätze',  ytw^ovfiaL  ,kratze  mich';   über  -/.ovv^a
s.  unten ;  ags.  hnot  ,abgeschabt,  kahl,  kurzgeschoren'.
Mit  dh:  gr.  i^vvd'Oq'  ä-^avd-a  (.UTigä  Hes.,  y,vvd-öv'  oi.LLy.Q6v  Hes.  ;
aisl.  hnjöda,  hnaud  , stoßen,  schlagen,  nieten',  ahd.  pi-hneotan  ,befestigen', inhd.  niet  m.  f.  ,breit  geschlagener  Nagel,  Niet',  nieten  ,nieten';  aisl. hnydia  ,Werkzeug  zum  Schlagen  oder  Klopfen';
norw.  dial.  nuddast  , abgestumpft  werden'  (mit  s-  schwed.  mdartl.  snudda , sanft  berühren',  Falk-Torp  u.  nudd)]  ahd.  hnotön  , schütteln',  mhd.  no^^en ,sich  hin  und  her  bewegen',  mengl.  nodden,  engl,  nod  , nicken';  aisl.  hnoss f.  , Kleinod'  (,gehämmert'),  ags.  hnossian  ,klopfen'.  Über  lett.  knudet  usw. s.  oben  1.
Mit  t:  vermutlich  got.  hnupö,  hnutö  ^amloxp^  aisl.  hnüdr  , Stange,  Pfahl', lett.  knute,  knutele  , dünne  Stange'  (oder  Lw.  aus  nhd.  Knüttel'?).
3.  ^-Erweiterungen:  gr.  yiovvta^  OY.öwta,  Y.vv^a  , starkriechende  Pflanze, Erigeron  vis
=== leaf 223 ===
cosum  L.'  (wenn  -f-  aus  -yt-;  auch  -di-  ist  gleich  möglich; zur  Geruchsbed.  vgl.  oben  vLvXaa,  nidor)]  aisl.  hnykr  (*hnuki-)  , Gestank' (daneben  fnykr,  snykr,  knykr,  nykr  ds.,  wohl  späte  Anlautswechselformen).
4.  Labialerweiterungen: Mit  idg.  b:  got.  dis-hniupan  ,zerreißen',   dishnupnan  , zerrissen  werden',
aschwed.  niupa  , kneifen',  ags.  a-hneopan  ,abpflücken';  mit  intensiver Kons.-Doppelung  norw.  mdartl.  nuppa  ,pflücken,  rupfen',  ags.  hnoppian ipflücken',  dän.  mnd.  noppe  , Wollflocke,   Zotte,  Hechelhede';
mit  idg.  bh :  aisl.  hnyfill  , kurzes,  abgestumpftes  Hörn,  Lamm  mit  solchen Hörnern',  ndd.  nohhe,  nubbe  ,Wollflocke',  mhd.  noppe,  nop  , Tuchflocke' (eher  Lw.  aus  mnd.  noppe).
5.  s-Erweiterung:  lett.  knaüsis  ,kleine  Mücke'  (wie  knisis,  ^nislis  von der  i-Basis).
WP.  I  392  ff.,  WH.  I  217  f.,  II  166  f.
5.  ken-  , frisch  hervorkommen  (vielleicht  eigentlich:  sprießen),  entspringen,
anfangen;  auch  von  Tierjungen  und  Kindern'.
Ai.   kanina-   ,jung',    Komp.    Sup.    kdnlyas-,  kdnistha-,  kanisthd-]    kanyä,
Gen.   PI.   kaninäm  (alter  w-St.)   ,Mädchen*,   av.  kaine,   kaim-,  kainln-  ds. ;
gr.  Tcaivög  ,neu,  unerhört' ;
lat.   recens   , frisch,   jung,   neu',    eigentlich    , gerade   vom   Ll^rsprung,    der
Geburt  her';
36*
564  •
mir.  cinim  , entspringe*,  ciniud  , Geschlecht,  Stamm';  air.  cenel , Geschlecht*, acymr.  cenetl,  ncymr.  , Geschlecht,  Nation';  vielleicht  auch  acymr.  mcymr. cein,  ncymr.  cain,  mbret.  quen,  air.  —  aus  dem  Brit.  —  cain  ,schön'  (:  gr. naivög  ,schön'  =  ,jung'?);  echt  ir.  ist  cain  (*hni-)  ds.;
mir.  cano,  cana  ,  Wolfs  junges',  cjmr.  cenau  ,junger  Hund  oder  Wolf (*kenduö  :  ken-) ;
galL  Cintus,  Cintugnätos  (,Primigenitus'),  air.  cetne,  cet-  ,erster',  cymr. usw.  cyn(t)  ,erst,  vor,  eher',  cyntaf  ,der  erste';
burgund.  hendinos  ,König' ;  strittig  got.  hindumists  »äußerster,  hinterster', ahd.  hintana,  hintar  ,hinter',  ags.  hindema  ,der  letzte'  (,novissimus');
aksl.  m-,  na-chuq,  -6^ti  »anfangen',  za<^§ti  ,ds. ;  empfangen  (vom  Weibe)', kom  ,Anfang',  komch  ,Ende',  aksl.  c^do  ,Kind'  (wenn  nicht  Lw.  aus  nhd. Kind-  s.  Berneker  154);  mit  beweglichem  s-  osorb.  sceho  ,das  letztgeborene Kind*,  russ.  §cen6k  ,3unger  Hund*,  aksl.  sten^  ,catulus*.
WP.  I  397  f.,  Wackernage
=== leaf 224 ===
l-Debrunner  III  112  f.
4.  ken-  ,sich  mühen,  eifrig  streben,  sich  sputen*.
Gr.  xomy*  kTteiyead'aij  ivsQysTvj  y,6vsL'  OTcevöe,  Tqi%Sy  ycovaQWTeQOV  öqu- (Tz Ly(,ü)r SQOv  Hes.,  yiovrjral'  -^egaTtowsg,  dyxövovg'  diay.6vovgy  öovXovg  Hes., did^covog,  ion.  ÖLrjycovog  , Diener,  Aufwärter*,  iyxovico  ,eile,  verlege  mich  auf etwas*,  iy-%ovig  , Dienerin*;
lat.  cönor,  -ärl  ,sich  körperlich  anstrengen,  den  Versuch  machen* ;
urkelt.  *kän-  (idg.  *kön-)  , vollbringen*  in  mcymr.  digoni  , machen*, dichawn,  digawn,  cymr.  dichon,  digon  ,kann*,  digon  ,genug*,  acymr. MN  Guoccawn,  mcymr.  gochawn^  gogawn  »ausgezeichnet*,  abr.  MN  Uuocon.
WP.  I  398  f.,  WH.  I  262.
ken-  jleer,  nichtig*;  nur  griech.  und  armen.
Arm.   sin   ,leer,   eitel',    gr.   hom.  v£v6[J^]6gj   kypr.    yLEvavfögj   ion.   y,eiv6g. (*x6v/os)  =  att.  TLsvdg  ,leer,  eitel' WP.  I  390.
keUQkö-  ,honiggelb,  goldgelb*  (mit  unklaren  Ablautverhältnissen).
Ai.  käncana-  , golden*,  m.  ,Name  einer  Pflanze',  käficana-  n.  ,Gold';
gr.  Tivrjyiög,  dor.  xyäx(5s  ,gelblich,  saflorfarben',  ycvfjycog  ,Saflor';
lat.  canicae  ,Kleie*;
aisl.  hunang,  aschwed.  hunagh  n.,  ags.  hunig,  as.  honig^  ahd.  honag, honang  , Honig'  (nach  der  Farbe  benannt;  Grundf.  wohl  germ.  *hunaga-, woraus  finn.  hunaja]  das  teilweise  vor  g  auftretende  n  beruht  auf  Nasa- lierung des  Vokals  durch  das  vorhergehende  n  und  unterstützendem  Ein- flüsse des  germ.  Suffixes  -ung-,  -ing-) ;
i
565
apr.  cucan  ,braun*  (l.  cücan,  d.  i.  cuncan-^  u  ist  balt.  Entw.  aus  reduz. Vokal  in  zweisilbigen  Basen)  5
über  ai.  kdnaka-  n.  ,Gold'  s.  Kuiper,  Proto-Munda  30 f.;
gall.  caneco-sedlon  kaum  als  , goldener  Sessel*  hierher,  auch  nicht  zu  mir. canach  , Sumpfgras*  (:  cymr.  ^aw  ds.),
WP.  I  400,  Vendryes  RC  47,  200  f.,  H.  Lewis  Et.  Celt.  1,  320  f.
keng-,  kenk-  s.  oben  unter  keg-.
j.  kenk-  , gürten,  jimbinden,  anbinden*.
Ai.  kdncate  (Dhätup.)  ,bindet',  kaücuka-  m.  , Panzer,  Wams,  Mieder*, käfici  f.  , Gürtel';
gr.  myyiXlg  , Gitter*  (zum  l  aus  e  s.  Solmsen  Beitr.  I  214  f.),  xdy,aXa  n.  PL ,Mauern*  (*knk-),  7todo-xd}i(7,)rj  ,Holz  zum  Festlegen  der  Füße* ;
lat.  cingö,  -ere  ,gürten,  gürtelartig  umgeben',  umbr.  sihitu  ,cinctos*, vielleicht  auch  gihgefa  ,cancellos*  (*kinkedä-)]  lat.  -g  für  c  Entgleisung auf  Grund  der  doppeldeutigen  cinxi,  cinctum  nsich.  Präsentien  wie  clingö, mingö]  WH.  I  217  stellt  hierher  kelt.  cing-  , schreiten*  (anders  oben  S.  439), falls  ursprüngl.  ,*sich  im  Kreise  wenden* ;  die  Variation  des  Auslauts wäre  allerdings  leichter  verständlich,  als  die  S.  439  angenommene  Anlauts- variation ;  noch  anders  über  kelt.  cing-  Kuiper  Nasalpräs.  168  f. ;
lit.  kinkaü,  -yti  , Pferde  anschirren*.
Eine  unnasalierte  Wurzelf.  *ke
```


## [2026-09-06T16:10:23.633Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=225 && NR<=226 {print \"=== leaf \" NR \" ===\"; print}' POK_02.txt"
}
```


### [2026-09-06T16:10:25.305Z] TOOL RESULT

```
=== leaf 225 ===
k-  sucht  man  in  ai.  kaca-  m.  , Haupthaar (»♦Zusammengebundenes*  ?) ;  Narbe,  Band*  und  lat,  cicätrix  ,Narbe, Schramme*  (auf  Grund  eines  "^cicäre  aus  *cecäre  ,zusammenbinden,  ver- narben') ?
WP.  I  400  f.,  WH.  I  211,  216  f.
2,  kenk-  , brennen  (dörren),  weh  tun;  auch  bes.  von  brennendem  Durst  und Hunger'.
Ai.  käTdksati  , begehrt*  (, brennend  verlangen*),  kdkate  (Dhätup.)  , dürstet*;
gr.  xsyyiSL'  nsiva  (nach  Aor.  ^'/.a^elv  entstand  ein  neues  Präs.  *x«yxa>, vgl.:)  yiayy,ofj.€vr]g'  ^rjgäg  reo  (pößo)  Hes.,  hom.  ftoXvyiayurjg  (diipa)  ,sehr brennend*,  %ayY.avog  ,dürr'  v.ayy.aivei'  -d^dXTtSL,  ^r]QaivsL  Hes.,  ytay-KaXia' y.ata'Ksyiavf.iiva  Hes. ;  y.a/.id'rjg '  i(XQog)og  üuTtsXog ;  xaxi^fg  *  Xifxrjgeg ;  xßxt^^a  * XLfxr]Qd  Hes.  (in  der  Endung  vermutete  Schulze  Kl.  Sehr.  329  *aidh' , brennen*);
got.  hührus,  mit  gramm.  Wechsel  anord.  hungr,  ags.  hungor,  ahd.  hun- gar  (*k'Q,kru-)  ,Hunger*  (=  gr.  xax-) ;  ablaut.  anord.  hä  , plagen,  quälen' {*hanhön') ;
lit.  kankä  , Schmerz,  Qual',  kankinti  ,peinigen',  kefikti  , schaden'.
WP.  I  401,  Trautmann  126^  Wissmann  Nom.  postverb.  42.
566  f
j.  kenk-  etwa  , Kniekehle  oder  Ferse'..
Ai.  kajdkäla-  m.  n.  , Knochen.   Gerippe' 5
anord.  hä  (*hanha-)  in  hä-möt  m.  »Sprunggelenk,  Fersengelenk',  hä-sin  f. .  ', Kniesehne  des  Hinterbeins  bei  Tieren,  Fersensehne  beim  Menschen',  a^s Jiöh-sinu  f.,  afries.  hö-sene  , Fersensehne',  ags.  höh  , Ferse'  {*hanha-),  anord. hcell  jFerse*  (*hanh{la-),  ags.  heia  m.  , Ferse';
lit.  Jcenkle   , Kniekehle',  kmka  ,ds.,  Hachse',  lett.   cinksla   , Sehne  in  der Kniebeuge'. WP.  I  401.
kenk-,  konk-   , schwanken',   ursprüngl.  »hangen,   geistig   in   Schwebe   sein'. Ai.    sdTdkate    , schwankt,    zweifelt,    fürchtet',    saidkä   , Besorgnis,   Furcht Zweifel',  sai^kita-  , besorgt';
lat.    cunctor    ,zögere,    bin   unschlüssig'   aus    *concitor    Frequentätiv   zu '    *concö,  bzw.  Ableit.  vom  Partiz.  *concitos  =  ai.  saidkita-'^
aisl.  hseita  ,w3Lgen^  (*hanhatjan-),  hstta  f.  , Gefahr,  Wagnis',  häski  m. ds.  (*hanhaskan-) ;  got.  st.  V.  hähan  (Prät.  haihäh)  »hängen,  in  der Schwebe  lassen',  aisl.  hanga  (Prät.  hekk),  ags.  hön  (Prät.  h&ng),  ahd.  hähan
■  (Prät.  Mang)  , hängen*  (trans.);  got.  schw.  V.  hähan  (Prät.  hähaida)  , hangen', aisl,  hanga,  ags.  hongian,  ahd.  hangen  , hangen'  (intrans.);  Kausativ  aisl. hengja,  ahd.  hengen  , hängen' ;  ahd.  rahd.  henken  , aufhängen'  aus  *hengjan, davon  nhd.  Henkel,  Schweiz,  henkel  »Tragriemen',  vgl.  mhd.  hengel  , Eisen- haken,   Henkel';    
=== leaf 226 ===
dazu   wohl   ahd.    hähila,  -ala   f.,    mnd.  hale   n.    ,Kessel-
■  haken'  (*hanhilö)]
hitt.  ga-an-ki  (kanki)  ,hängt'.
WP.  I  382  f.,  WH.  I  307;   vgl  oben  kUk-  und  %-.
kens-  ,feierlich  sprechen»  verkündigen';  kens-tor-  , Sprecher',  kens-to- »verkündef.
Ai.  samsdyati  »läßt  aufsagen»  kündet  an'  (=  lat.  censeö),  sdmsati  »rezi- "  tiert,  lobt'»  sdmsa-  m.  »Lob,  Preisgebet'»  sasti-  f.  »Lob'  (*kns-),  sdsä  f.  »Lob- lied';
av.  sah-  »pronuntiare',  Optat.  sahyät,  sasti-  »Wort,  Vorschrift' ;  s^nghaite, apers.  d-ätiy  »spricht»  verkündet'  {*d-a{n)hati)]
alb.  thom  »ich  sage'  (^kensmi),  2.  Sg.  thua,  thue,  ablaut.  Partiz.  than »gesagt'  (*thonsno-) ;
lat.  censeö,  -ere  »begutachten,  schätzen',  osk.  censamur  ,censetor'^  cen- saum  »censere'»  keenzstur,  kenzsur  (==  censor :  sii.  saihstar-  »der  da  rezitiert")» an-censto  f.  =  in-censa  »non  censa'»  lat.  census  (:  ai.  sastd-h  »gesprochen, gepriesen'),  censtom-en  ,in  censum',  Kenssurineis  Gen.  (=  Censörinus)  ]
abg.  s^H  »inquif  (alter  Wurzelaarist?  Vgl.  Meillet»  Slave  commun^  209).
WP.  I  403»  WH.  I  198ff.»  EM3  201.
567
^enth{6)-  , Lumpen,  Lappen';  auch  ket{h)-'^
Ai.  kanthä  jg-eflicktes  Kleid';  arm,  k'ot'anak  , Kleid,  Decke';
gT.  ycivTQCDv  ,Rock  aus  Lumpen,  Flickpoem'  ist  Bedeutungslehnw.  aus dem  Lat. ;
lat.  centö  ,aus  Lappen  zusammengenähtes  Kleid  oder  Decke,  Flickwerk' ;
ohne  Nasal  ahd.  hadara  f.  , Lappen,  Lumpen'  (^haprö,  idg.  *koträ),  nhd. Hadern]  dazu  mit  Z- Ableitung  mhd.  Hadel,  ablaut.  nhd.  dial.  Hudel,  davon hudeln  ,schmieren'.
WP.  I  402  f.,  WH.I  200.
kent-  , stechen'.
Gr.  xsvTso)  (seit  dem  5.  Jhd. ;  älter:)  *yc€vTa),  Aor.  yisvaai  , stechen', ycsWQOv  , Stachel'  (Formans -ro-)  , stechend',  -ksvtcjq  ,Anstachler'  (zu  y.£VTQOv gebildet  nach  sonstigen  -tcjq  neben  -tqo-),  -Ksarög  ,gestickt'  (*y,svT-r6g), 'AeafQOv  , spitzes  Eisen',  yiiarQog  , Pfeil',  v.earQä  f.  , Spitzhammer',  Y.ovr6g , Stange,  Schifferstange'  (daraus  lat.  contus  ds.,  wovon  percontärl  eigentlich ,mit  der  Schifferstange  sondieren',  daher  , untersuchen,  forschen');
air.  cinteir  (lat.  Lw.)  ,calcar',  cymr.  cethr  ,Nagel',  corn.  kenter  ds.,  bret. kentr  , Sporn'  (Entlehnung  aller  aus  lat.  centrum  ,y.£VTQOv\  Pedersen  KG.  I 198,  ist  kaum  erweislich,  aber  wahrscheinlich;  Vendryes  Mel.  Saussure 319  läßt  nur  das  ir.  Wort  aus  dem  Brit.  stammen);
ahd.  Äaw^a^, spitz';
```


## [2026-09-06T16:10:35.197Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"kens-\" AHD_watkins1985.txt | head; echo \"--- kosm\"; grep -n -i \"kosmos\\|cosmetic\\|cosmos\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T16:10:35.261Z] TOOL RESULT

```
615:kenk-’. Heel, bend of the knee. 1. Germanic *hanhaz in Old English héh, heel: HocK!. 2. Germanic *hanhilén- in Old English héla, heel: HEEL!. [Pok. 3. kenk- 566.] kens-. To proclaim, speak solemnly. Form *kens-é- in Latin cénsére, to judge, assess, estimate, tax: CENSOR, CENSUS; RECENSION. [Pok. kens- 566.]
1340:CELLA kel-2 CELLAR kel-2 CELLARER kel-2 CEMBALO keu-2, kleu-3 CEMENT kae-id- CEMETERY kei-1 CENACLE sker-1 -CENE_ ken-3 CENOBITE gWei-, kom CENOGENESIS ken-3 CENOTAPH dhembh-, ken-4 Cenozoic ken-3 CENSOR kens- CENSUS kens- CENT dekm CENTAL dekm CENTAVO dekm CENTENARIAN dekm CENTENARY dekm CENTENNIAL dekm CENTER kent- CENTESIMAL dekm CENTESIS kent- CENTI- dekm CENTIGRADE ghredh- CENTIME dekm CENTNER dekm CENTO kentho- CENTRIFUGAL bheug-'
2174:REBUT bhau- RECALESCENCE kele-! RECANT kan- RECAPITULATE kaput RECEDE ked- RECEIVE kap- RECENSION kens- RECENT ken-3 RECIDIVISM kad- RECIPROCAL pert RECISION kae-id- RECK reg-1 RECKLESS reg-! RECKON reg-1 RECLAIM kele-2 RECLINE klei- RECLUSE kleu-3 RECOGNIZE gnd- RECOIL (s)keu- RECOMMEND man-2 RECONDITE dhé-1 RECORD kerd-1 RECOURSE kers-2 RECOVER kap- RECREANT kerd-1 RECREMENT krei- RECRIMINATE  krei- RECRUDESCE kreud-! RECRUIT ker-3 RECTANGLE reg-1 RECTIFY dhé-1, reg-1 RECTILINEAR reg-1 RECTITUDE reg-!
--- kosm
623:(SCARCE). 3. Greek karpos, fruit: -cARP, CARPEL, CARPO-, -CARPOUS. [In Pok. 4. sker- 938.] kers-'. Dark, dirty. 1. Suffixed form *ker(s)-no- in Rus- sian chérnyi (feminine chérnaya), black: CHERNOZEM. 2. Suffixed zero-grade form *krs-no- in Sanskrit krsna-), black, dark: KrisHNa. [Pok. kers- 583.] kers-2. To run. Zero-grade form *krs-. 1. Latin currere (past participle cursus), to run: CORRIDOR, (CORSAIR), COURANTE, COURIER, COURSE, CURRENT, CURSIVE, CUR- SOR, CURULE; CONCOURSE, CONCUR, DECURRENT, DIS- COURSE, EXCURSION, HUSSAR, INCUR, INTERCOURSE, OCCUR, PERCURRENT, PRECURSOR, RECOURSE, RECUR, succor. 2. Suffixed form *krs-o- in Gaulish carros, a wagon, cart, in: a. Latin carrus, a two-wheeled wagon: CAR, CAREER, CARGO, CARICATURE, CARIOLE, CAROCHE, (CARRY), CHARGE, CHARIOT; b. Latin carpentum, a two- wheeled carriage: CARPENTER. [Pok. 2. fers- 583.] kert-. To turn, entwine. I. Zero-grade form *krt-. 1. Suf- fixed form *krt-i- in Germanic *hurdiz, wickerwork frame, hurdle, in: a. Old English hyrdel, hurdle, frame: HURDLE; b. Old French hourd, fence, hurdle, scaffold: HOARDING. 2. Suffixed form “*krt-sti- in Germanic *hur- sti- in Old High German hurst, thicket: Horst. II. Per- haps suffixed variant form *krot-i- in Latin crdatis, wickerwork hurdle: CRATE, GRATE?, (GRID), GRIDDLE; (GRIDIRON). [Pok. kert- 584.] kes-'. To scratch. 1. Germanic *hezd6 in Old English heordan, coarse parts of flax: HARDS. 2. Extended form *kseu- in Greek xuein, to scrape: XYSTER. 3. Nasalized form *ks-n-eu- in: a. Germanic *snaww- in Old Norse snéggr, “close-cropped,” perhaps akin to the source of snuG!: b. Latin novdcula, razor: NOVACULITE. [Pok. kes- 585.] kes-2. To cut. Variant kas-. 1. Suffixed form *kas-tro- in: a. Latin castrare, to castrate: CASTRATE; b. Latin cas- trum, fortified place, camp (perhaps “separated place”): CASTLE. 2. Suffixed form *kas-to- in Latin castus, chaste, pure (< “cut off from, free of, faults”): CASTE, CHASTE; CASTIGATE, INCEST. 3. Suffixed (stative) form *kas-é- in Latin carére, “to be cut off from,” lack: CARET. 4. Ex- tended geminated form *kasso- in Latin cassus, empty, void: (CASHIER), QUASH. [Pok. hes- 586.] kes-°. To order. Suffixed 0-grade form *kos-mo- in Greek kosmos, order: COSMOS; MACROCOSM, MICROCOSM. keu-' Also ekeu-. To perceive, see, hear. O-grade form *akou-. 1. Extended form *kous- in: a. Germanic *haus- Jan in (i) Old English hieran, to hear: HEAR (ii) Old English he(o)rcnian, to harken: HEARKEN; b. suffixed form *9-kous-yo- in Greek akouein, to hear: ACOUSTIC. 2. Variant *skou- in: a. Germanic *skauwon in (i) Old English scéawian, to look at: SHOW (ii) Flemish scauwen, to look at: SCAVENGER; b. Germanic *skaunjaz in Mid- dle Dutch schoon, beautiful, bright (< “conspicuous, attractive”): SCONE; Cc. Germanic *skauniz in Old Eng- lish sciene, bright, sheen: SHEEN. [Pok. 1. keu- 587.] keu-?. Base of various loosely related derivatives with assumed basic meaning “to bend,” whence “a round or hollow object.” I. Extended forms *keub-, *keup-. 1. Ger- manic *haup- in: a. Old English héap, heap: HEAP; b. Dutch hoop, heap, troop: FORLORN HOPE. 2. Germanic *hupp-, to leap (by first bending the legs), in Old English hoppian, to hop: HoP!. 3. Germanic *Aupiz in Old Eng- lish hype, hip: H1P!. 4. Zero-grade form *kup-, vessel, in: a. suffixed form *kup-s- in Greek kupselé, chest, hollow vessel: CYPSELA; b. long-vowel form *kip- in (i) Ger- manic *Aifi- in Old English hyf, hive: HIVE (ii) suffixed form *kip-a in Latin cupa, tub, vat: CUPOLA, CUPULE; c. expressive form *kupp- in Late Latin cuppa, drinking vessel: cup. 5. Zero-grade form *kub- in: a. Greek kubos, cube: CUBE; b. suffixed form *kub-@- in (i) Latin cubdre, to lie down on (< “to bend down, prostrate”): COUVADE, COVEY, CUBICLE; CONCUBINE, INCUBATE, SUCCUBUS (ii) Latin cubitum, elbow: CUBIT; Cc. nasalized form *ku-m-b- in (i) Latin -cumbere, to lie down, recline: ACCUMBENT,
763:mops, fool, also pug dog (> German Mops, pug dog): ROLLMoPsS; d. Old French momer, to act (in dumb show): MuM2, 2, Germanic *mut- in Old Norse mudhla, akin to the source of Middle English muteren, muttren, to mut- ter: MUTTER. 3. Latin muttire, to mutter: MOT, MOTTO. 4. Lengthened-grade form *mi- in Latin miius, silent, dumb: MuTE. 5. Greek muein, to close the eyes (< “to close the lips”): MIOSIS, MYOPIA, MYSTERY!, (MYSTIC). [Pok. 1. mii- 751.] mu-2, Gnat, fly. Imitative root. 1. Germanic *mukjé- in Old English mycg, midge: MIDGE. 2. Suffixed form *mus-ka in Latin musca, a fly: Mosquito, Musca, MUSCARINE, MUSH?, MUSKET. 3. Suffixed form *mus-ya in Greek muia, mua, a fly: mytasis. [Pok. 2. mi- 752.] mik-. A heap. Germanic *miigén-, *mihon- in: a. Old English miga, miiha, miiwa, heap of grain: Mow}; b. Old Norse migi, heap, akin to the probable Scandinavian source of MOGUL}. [Pok. mitk- 752.] [mundus. Women’s cosmetics, also world (probably by a calque on Greek kosmos, order, feminine adornment, world-order, universe). Latin noun of unknown origin; possibly from Etruscan. MUNDANE; ULTRAMUNDANE.] miis-. A mouse; also a muscle (from the resemblance of a flexing muscle to the movements of a mouse). 1. Ger- manic *mis- (plural *misiz) in Old English mis (plural
1394:CONVOLVE wel-3 CONVULSE wel-4 cook pekw- cOoKY kak-2 cooL gel-3 COOPER ku- COOPERATE op-1 CO-OPT op-2 COORDINATION ar- COPE! kel-1 COPEPOD kap- COPIOUS op-1 COPRO- kekw- COPULA ap-! COPULATE ap-1 COPY op-1 CORACIIFORM ker-2, merph- CORACOID ker-2 CORBEL ker-2 CORBINA ker-2 CORD ghere- CORDATE kerd-1 CORDIAL kerd-1 CORDIFORM kerd-1 CORDON ghere- COREOPSIS sker-! CORGI kwon- CORIACEOUS sker-1 CORIUM §sker-1 cOoRM sker-! CORMORANT ker-2 CORN! gre-no- CORN2 ker-1 CORNEA ker-1 CORNEL ker-6 CORNEOUS ker-1 CORNER ker-1 CORNET ker-1 CORNICULATE ker-1 CORNIFICATION ker-1 CORNU_ ker-1 CORNUCOPIA op-! CORONA sker-3 CORONOID  sker-3 CORPORAL! kWrep- CORPORAL’ kWrep- CORPORATE kWrep- CORPOREAL kWrep- CORPOSANT kWrep-, sak- CORPS kWrep- CORPSE kWrep- CORPULENCE kWrep- CORPUS krep- CORPUSCLE kWrep- CORRADE réd- CORRECT reg-! CORRIDOR kers-2 CORRIE kWer-2 CORROBORATE reudh-! CORRODE réd- CORRUGATE ruk-2 CORRUPT reup- CORSAGE kWrep- CORSAIR kers-2 CORSE kWrep- CORSET kWrep- CORTEGE gher-1 CORTEX sker-1 CORUSCATE sker-2 CORVEE reg-! CORVINE ker-2 Corvus ker-2 CORYDALIS_ ker-1 CORYMB_ ker-1 CORYNEBACTERIUM bak-, ker-1 CORYPHAEUS_ ker-1 COSMONAUT nau-2 COSMOPOLITE pele-3 cosmos kes-3 cost sta-
```


## [2026-09-06T16:10:36.000Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=201 && NR<=205 {print \"=== leaf \" NR \" ===\"; print}' KNT.txt | head -100"
}
```


### [2026-09-06T16:10:37.579Z] TOOL RESULT

```
=== leaf 201 ===
B Gr. $144, §286, $298 (Bv. takes uvd- as instr. and not vriddhied), and by H. H. Schacder, Nachrich- ten d. Ak. d. Wiss. in Gottingen, phil.-hist. Kl. 19046-7.24-30. wdmarsiyus nsm. DB 143.
Uvárazmi- sb. ‘Chorasmia’, a province of the Persian Empire: Elam. ma-ra-18-mi-18, Akk. þu- ma-ri-iz-ma-’, Gk. Xwpaspin, Av. asf. z'airizom. From u- ‘good’ + vāra- ‘0° (8126, 5148.111), + ami- (§95, $120, 5152.) to zam- ‘land’. See also Uvürazmiya-. Uvirazmiy nsf. (SI79.1; Lg. 19.223) DB 1.16, DPe 16f; Uvārazmiš DNa 231, DSe 22°, DSm 9°, XPh 21f. Uvārazmiyā арзї. DSf 39f.
Uvürazmiya- adj. ‘Chorasmian’: deriv. to pre- ceding ($144.11). (Uvarajzm*ya (822) nsm. APP 8. |
war Stika- sb. ‘good spearman’: u- ‘good’ + drStika- ‘spearman’ (8126). шаг Ка пат. DNb 44.
wasabdra- sb. ‘good horseman’: u- ‘good’ + asabāra- ‘horseman’, with vriddhi ($126). uvāsa- bara nsm. DNb 42.
waspa- adj. ‘having good horses’: u- ‘good’ ($118.1V, $140.1V) + aspa- ‘horse’ ($9.11). waspä nsf. AmH 6; DPd 8. uvaspam asn. DSf 11; DSp 3°; рле 4^; for asf. AsH 10 (§52.[11). waspd apn. as sb. ‘good horses’ DSs 5°.
Uvja- Unjiya-, see Uja- Ujiya-: cf. Wb. МОЕ 7.43, Schaeder ShHPAW 1931.636.n3.
twnara- sb. ‘skill, accomplishment’: ad}. form- ation to pAr. *su- ‘good’ + *nar- ‘man’ (§142, 5148.1, V), = ‘having the good quality of a man’, Av. hunara- ‘ability, skill’, Skt. sümára- ‘glad, joyous, merry’, with vriddhi of the first vowel in OP and Skt. to show the derivative nature (523.11, $126: Lg. 15.173, JNES 4.51-2: cf. Hz. RHRel. 113.30, ApI 200-6, who aecepts this meaning but seeks another etymology, as does also Pisani, Riv. Stud. Or. 19.93-4). düvnarü npn. DNb 45, 51. üwnaraibis ipn. DNb 48.
ustaSand- (usta$na- Bv. Ст. $294) sb. 'stair-
178
case’: us- (see ud-, $84, $85) + tašanā- (§102), deriv. (5147 1) to root taš- ‘cut, fashion’ (see under tax’-), pIE *ud-tekbend-. ustaSandm asf. А?Ра 22 (as nom., §56.V).  [usta]canám (§49b) Ае 5f.
ušabāri- adj. ‘camel-borne’: usa- ‘camel’ ($79, $130), Av. ustra- (MB Gr. $109; cf. Justi, GGA 1882.488), + bāri- ‘borne by’ (8122, $126, $51521, 6160.1е), to root bar- ‘bear’. Cf. Jn. Indo-Iranian Studies Sanjana 18-20. ušabārim DB 1.86f.
uši- sb. dual ‘two ears, hearing, understand- ing’ (cf. JNES 4232; Hz. RHRel. 113.30, ApI 342-4): LAv. dual «&, cf. Gk. ois, Lt. auris, Gt. ausó. иу ndn. ($189) DNb 28, [р-а adn. ($136) DNb 32. ušībiyā idn. ($189) DNb 37; udiyd idn. (with sg. ending, $189; Lg. 19.224—5) DNb 35.
uška- adj. ‘dry’; nt. as sb., ‘land, mainland’: Av. hu&ka- ‘dry’, NPers. zusk, Skt. $ügka-, Sisyatt ‘dries’, Lith. saüsa-s ‘dry’, NEng. sere, sear ($146.1). uškahyā gsn. DPe 13.
ushamaranakara- sb. ‘good warrior’: u- ‘good’ + hamaranakara- ‘warrior’ (§140.VI). ushamara- nakara nsm. DNb 34.
uzma- adj. as sb. ‘that which is up from the earth, stake’: from ud- ‘up’ + zma- to zam- ‘earth’ ($84, $95, $120, $130, §142, 5148.11, VI): other- wise Wackernagel, KZ 61.208; Lommel, OLZ 37.180.n2; König, RuID 72. uzmayā-patiy lsn. DB 2.76, 91; 3.52, 92.
ka- interrog.-indef. pron. ‘who’: Av. Skt. ka-, Gk. то-, Lt. quo-, NEng. wha-t, pIE *q*o- ($201). See also Ка, -katy, ci- (§132.2). With encl. -ciy, ‘any’: kaš-ciy (89. VI, $09, $105) nsm. DB 1.49, 53; DSe 37.
kā, generalizing particle after 2d pers. pron.: probably isn. of ka- ($191.11; Kern ap. Caland, 1. Syntax der Pron. im Av. 47; Kieckers, Etymol. Miszellen 1934.135; otherwise Gray, JAOS 23.60). DB 4.37, 41, 67°, 70, 87°; DSt 10°; XPh 46.
-katy, emphatic encl. particle, m ada-katy (q.v.): probably lsn. to ka- ($191.11), ef. Gk. то ‘somewhither’ (Bv. Gr. $336 takes as *ka*<4, cf. naiy from *na-19).
kaufa- sb. ‘mountain’: Av. kaofa-, Phl. kof,
NPers. köh ($75.IT, $106). See also Akaufactya-. kaufa nsm. DB 1.37; 3.44; DSf 31.
OLD PERSIAN
ka"ta- pte. as sb. (8276. TII) ‘excavation’: pAr, « 7 с *knta-, to 'kan-, with restored n ($242.11) agin с Samar-kand, wherein -kand has been transferred from the ditch 
=== leaf 202 ===
to the wall alongside it (König, - Burgbau 32n; Hz. AMI 3.54-5, Ар! 224). katam nsn. DSf 25.
Katpatuka- sb. ‘Cappadocia’, a province of the Persian Empire; also, as adj., ‘Cappadocian’: Elam. ga-at-ba-du-qa, Akk. ka-at-pa-tuk-ka, Gk. Каттодокіа. ($93.11).
(1) ‘Cappadocia’: Katpatuka nsm. РВ 1.15f; DPe 12; DNa 28; DSe 27°; D8m 8^; XPh 26. (2) ‘Cappadocian’: Katpatuka пэш. A?P 21.
ikan- vb. ‘dig’: Av. kan-, Skt. khan- ($100), . See also Adukanaiía-, kata-. ka*tanaiy ($238; NPers. kándón) inf. DZe 9; XV 21. akaniya imf, pass. ($113, $220) DSf 24, 28 (25, 29 read avaniya: see under van-); DZe 10°.
ni- + kan- ‘destroy, obliterate’: пач imv. (§208, $237.IT) DB 4.80.
vi- + kan- ‘dig apart, destroy’: viyakanam 1st sg. imf. XPh 38. viyaka" imf. ($208, §228.11) DB 1.64. vikanàhy 2d sg. subj. (327) DB 4.71, 78; vikandh"-di& (S27, 454.11, $136) DB 4.77.
*kan- vb. of uncertain connections, probably ‘throw, place’: cf. NPers. dwgdnddn ‘heap up’ from ava-kan- (Dv. Gr. $184; Morgenstierne, Acta Or. 1.249; Hz. ApI 225).
ava- + kan- ‘put down on, place on’: avakanam Ist sg. imf. (8213, 5226.1) DB 1.86.
Ka™pa"da- (8111) sb. ‘Kampanda’, a district in Media (cf. Kónig, RuID 71): Elam. qa-um-pan- taš, Akk. ha-am-ba-mu. Kapada пет. DB 2.27.
kapautaka- adj. ‘blue’, in kdsaka hya kapau- |
taka ‘lapis lazuli’: deriv. ($146.11) of stem in РЫ. — | kapót, NPers. kabod ‘gray-blue’, Skt. kapóta- ‘pigeon, pigeon-color, gray’ (Scheil 21.29; Bv. BSLP 30.1.61; Konig, Burgbau 62; Bleichsteiner, WZKM 37.94-101; Wb. AfOF 7.42, cf. PW 10.1887 s.v. Караша; Hz. AMI 3.64-5). kapau- taka nsm. DSf 37.
Käpišakāni- sb. ‘Kapishakani’, a fortress in Arachosia ($117, $126): Elam. qa-ap-pi-i3-fa-qa- nui, Каракат ns. DB 3.608.
Ka"büjiya- sb. ‘Cambyses’, (1) father of Cyrus the Great; (2) son of. Cyrus the Great, king of Persia before-Dartus: Elam. kan-bu-si-ia, АКК.
LEXICON
kam-bu-ai-ia, Gk. KayBvons (8111, $144.IV): ety- mology disputed (cf. Bthl. AiW 437; Charpentier, ZII 2.140-52). Kabūjiya nsm. DB 1.28, 30f, 31, 32, 33, 43. Kabijiyam asm. DB 1.45, 46. Kabüyyahyà gsm. CMb 1f; DB 1.29, 30, 39. Kabūjiyāä absm. DB 1.40.
kam- vb. ‘like’, see amazamata, if for (h)- amaxmatd. See also kama-, and possibly canah-.
káma- sb. ‘wish, desire’: Av. Skt. kdma- (§126, $148.I, V, VI). See also kam-. For syntax of de- pendent acc., $249.T, JAOS 66.44-9. kama nsm. DB 4.35f; 5.17°, 29, 33°; DNa 38; DNb 8, 10, 12, 19, 20, 27; DSf 16; DZe 12°. ХРЇ 22, 30.
kamna- ad}. ‘small, few’: Av. kamna-, NPers. käm ($147.11). kamnam nsn. (as pred. sb. $259) DB 2.19. kamnatbis ipm. DB 1.56; 2.2, 71; 3.41, "Af.
kar- vb. ‘do, make, build’: Av. kar-, pres.
karonaoitt, Skt. kr-, pres. krndti karóti (809, $122, $132.2, 5182.3). See also akarta-, ucára-, kara-, dastakarta-, duskarta-, hakarta-.
kunautiy (866.1, $70, $99, $2101) DNb 24f; DSs 2°, 3f, 4, 6°. |
akunavam ($66.1) 184 sg. imf. DB 1.62, 63, 68, 12, 87; 2.20, 76, 83, 91; 3.31f, 52, 85; 4.3f, 6, 86°, 40, 41, 45, 59, 60, 65, 89; 5.2, 8f, 17, 29, 33; DNa 491, 51; DNb 48f; DSa 4, 5; 284 3°; DSe 32, 34, 45, 49; DSf 21, 22 bis; D8g 3^; DSi 4^; ре] 2°, 3, 3f°, 4; D8o 2°, 4; XPa 13, 14; XPb 27; XPd 17; ХРЇ 37f, 41; XPg 11f; XPh 43, 43f, 44f, 46; ХР]; A'Pa 21f; D'Sb 4. — akunavüm (853, $55.I) A’Sdb 3; akuvanasaSa (455.1) A'Sde 3.  [akun]aàm (855.I) XSe 3; A’Ha 5; [akunàm] A’Sa 4, 5; akund (555.1) A’Ha 7.
akunauš imf. (884, $218.I, $228.1IT) AsH 8; DB 2.23, 85, 90; 3.5, 16, 57; 4.10, 12, 15, 18, 20, 23, 26, 28, 31, 34, 35; 5.10; DPa 6; РМа 56, 34; DSe 5; DSf 4, 10, 15, 17, 20°, 30; DSi 3^; DSm 5°; DSt 6°; рле 3; DE 8; XPa 4, 15; XPb 8; ХРе 4, 11; XPd 6; XPf 6, 24, 27, 32, 42; XPg 4f; XPh 5; XSaa 2 (-nauu& in ab, $53); XE 9; XV 7, 20, 23; A'Pa 6°; D'Sa 2; D'Sb 3; А?НЬ; A*He 5; A?Pa 6. akunaš (S55.I) ЬЬ 3; A?Sa 3f.
akunava^ 3d pl. imf. DB 2.34, 39, 45, 54, 59; 3.37, 44, 61, 66; DNa 20f, 37; DSe 19°; XPh 18. akunavaía (5282.10) DSf 50°, 51, 53.
акитӣ lst pl. aor. ($218.IT, $230.1T) DB 1.90, 94, 96; 2.68, 70; XPa 17; ХРЇ 43.
akunava"tà 3d pl. imf. mid. (§210.1, $236.IT) DB
179
3.12; 5.6; DSf 48 (Hz. ApI 229-30 takes as fr
=== leaf 203 ===
om ã + kart- ‘cut’; but see Kent, Lg. 18.81-2).
акша aor. mid. ($66.1, §218.11, §235.11) CMb 4; DB 1.47.
akunavayalà imf. pass. (§220, $235.IT) DB 1.20, 24.
akariya imf. pass. (585.1, §99, $220) DSf 37; XPh 42.
akarzya^tà За pl. imf. pass. (§35.1, $66.IT, $220, 8236.11) DB. 3.92. !
[c]àzr[;yatà]| or cazr{iyatd] perf. pass. ($219, $220) DB 4.90 (Kent, JAOS 62.267-8, for KT's „ада... after König, Klotho 446).
kunavahy 2d sg. sub). (8222. TIT) DB 4.75, 79.
kunavánazy lst sg. subj. mid. (§66.1, $222. III, $233.IV) DSI 4 (Bv. BSLP 30.1.65; not act. -nty, with Wb. AfOF 7.39).
kunavdtaiy subj. mid. (5222.11) DNb 56.
caxriya perf. opt. ($99, $1081, $122, $219, 6228.1, $228.II) DB 1.50.
kariyaiš opt. pass. (585.1, $220, $223.IT, $228.- Ш) DNb 9, 11 (not desiderative future, as taken by Hz. Apl 228).
kunautuy imv. (§210.1, 5237.П) DB 4.76.
kušuvā 2d sg. aor. imv. mid. (5218.1, $237.11) DNb 50.
eartanaiy inf. (581, $99, $122, 5238) DB 1.94; 2.33, 381, 44, 53, 58, 67; 3.36, 431, 60, 651; DSf 20°; DSn 1°.
karta nsm. past pte. pass. (Av. karata-, NPers. hard, Skt. kid-; $30, 506, 8122, 242.1) DPe; ЮР; DSf 38, 40, 43; XPi*; AM,
kartā nsf. A?Pa 28. kartā npf. ($119) DSi 46.
kartam nsn. DB 1.27; 2.27, 37, 42, 47, 57, 62, 02, 08; 3.8f, 10, 19, 21, 40, 47, 53, 64, 69, 76; 4.2, 42, 46f, 49, 511, 52, 54; "Ма 48f; DNb 29, 48, 56°; DSe 44; DS} 5f°; DSn 2; DSs 7; XPa 14, 15f, 19, 20; XPb 23f, 25, 30; ХРе 13, 14; XPd 19; XPf 38, 461, 47; XSc 5°; XV 27°; XH; A'Pa 24°. kartā (for nsn., $56:V) А?Ра 26. kartam asn. DNa 51; XPf 40; XPg 10; XPh 46; A’Sd 4.
kara- sb. ‘doer, maker’, as 2d element of cpd.: deriv. of kar- ($82, §143.1); found in avükara-, ciyükara-, düraniyakara-, zürakara-,  hakara-, hamaranakara-, and with passive meaning, 'thing made’, in patikara- (cf. Bv. Gr. $289).
küra- sb. ‘people, army’: Lith. káras ‘war’, dialectal ‘army’, Gt. harjis ‘army’, NGm. Heer (8143. III); ef. König, КИР 66. See also ukdra-.
180
Ката nsm. DB 1.33, 40, 79, 85; 2.16, 18, 25, 27, 301, 35, 40, 46, 50, 55, 60, 751, 87, 90, 94; 3.3, 17, 26, 32, 38, 45, 59, 62, 67, 81; 4.92; DPe 22; DSi 29,32. Ката-йт DB 1.50. káram asm. DB 1.51, 52, 66, 78, 86, 88, 95; 2.19, 20f, 25, 35, 41, 46, 55, 61, 68, 72, 81, 83f, 87, 97; 3.1f, 4, 7, 15, 17, 29, 38, 42, 46, 55, 58, 62, 67, 84, 85; 4.34; 5.7; DPe 21. kárahyà gsm. DB 1.31f, 38, 64, 75; 2.10, 15, 80; 3.24, 70, 80; 4.54, 55, 58. kárá ism. DB 1.93; 2.22, 67, 85, 95; 3.15f, 33, 36, 73, 861; 5.9, 21, 24; DPe 8f. |
Karka- adj. ‘Carian’; pl., also a province of the Persian Empire: Elam. kur-qa-ap, Akk. kar-sa, Gk. Kapes, Карко{ (§31, §106); cf. Eilers, OLZ 38.201-13, with lit. Karka пет. А?Р 30. Karka npm. DNa 30; DSe 30°; DSf 33; XPh 28.
karnuvaka- sb. ‘stonemason’: from root kart- ‘cut’, Av. pres. karanv-, Skt. kyi-, pIE *gert-, + suffix -aka- (§30, $146.D), ef. JAOS 51.210. There are also forms of this root without -i- (JAOS 53.20), such as Gk. керө (cf. Boisaca, Dict. étym. de la langue greeque, s.v.). See also Bv. BSLP 30.1.06; Hz. AMI 3.78; Kónig, Burgbau 69-70; Wb. AfOF 7.48. — karnuvakà npm. DSf 47.
Karmüna- sb. ‘Carmania’, a district of South- ern Iran ($166.I): NPers. Kirmān, Gk. Kapyavia. Karmánà absm. DSf 35.
karSa- sb. ‘weight, (unit by) weight’ (like Lt. pondo, Lg. 19.227-9), = 83.33 gr. or slightly less than 3 oz. avoirdupois (Gray, JAOS 20.55; Sehmidt, Treasury of Persepolis 62): Skt. karga- ‘pull, unit by weight’ (§29.n2, $80, $1431, VI). The OP kar$a- was one-sixth of the Babylonian mana ‘mina’ (weight; not unit of value). Elam. transcribes kur-Sa-wm, = kršam, which may mark the word as netter, since Elam. transcriptions commonly represent the nom. sg. of the foreign word; but the other evidence is rather for the masc. karšā ism. (§252D; Lg. 19.227-9; not ndm.) Wal. karíayá lsm. (§251C; Lg. 19.227-9; not npm.) We 1; Wd 1.
kasaka- sb. ‘semi-precious stone’; Elam. ga- st-ga causes König and Wb. to write kás'ka, but this is not warran
=== leaf 204 ===
ted by the OP writing. регу. of Iran. root *kas- (89.V, §87, $126, §146.II), = Skt. kaś- ‘be visible, appear, shine’ (so König, Burgbau 61; not to Skt. Ёйс@- ‘crystal, quartz’, despite Bv. BSLP 30.1.61); for meaning, cf. NEng.
OLD PERSIAN
brilliant. Cf. also Scheil 21.29; Wb. МОЕ 7.49. Hz. AMI 3.65, ApI 230-3; Bv. Gr. $273. See algo :
kasakaina-. Казака пзш. DSf 37, 39.
kasakaina- adj. ‘of semi-precious stone’, | | namely, of lapis lazuli: adj. to preceding ($147. ;
III).  kásakaina nsm. DPi; XPi.
Kuganakü- sb. ‘Kuganaka’, a town in |
Persia: Elam. ku-ug-gan-na-qa-an, Akk. ku-gu-ne- ak-ka. — Kuganaká nsf. DB 2.9.
Ku'duru- sb. ‘Kunduru’, а town in Media: Elam. ku-un-tar-ru-i$, АКК. ku-un-du-ur. Кид“. ти$ (§22) nsm. DB 2.65.
Küru- sb. ‘Cyrus’, founder of the Persian Empire: Elam. ku-rag, АКК. ku-ra-a$, Gk. Коро; (§164.V). Küru$ пэт. CMa 1; CMb 1; CMe.
Kürau$ gsm. DB 1.28, 39, 53; 3.25; 4.9, 27f; DBb
5f; DBh 6f.
Kūša- sb. ‘Ethiopia’, a province of the Per- sian Empire: Elam. ku-ša-a-ia, АКК. ku-ú-šu, Heb. kik. See also KüSiya-. Kā- absm. DPh 6; DSf 48; DH 5.
Kūšiya- adj. ‘Ethiopian’; pl., a province of the Persian Empire: adj. to preceding (5144.11). Kūšāya (sic!) пзш. A?P 28. Kasydé npm. DNa 30; DSe 30°; XPh 28 (written Kūšiya, $51; ef. Lg. 13.298).
zaudü- sb. ‘hat, cap’ ($100, $143.IV): Av. таоба-, Oss. хойй, NPers. тоб, Arm. (borrowed) zoir ‘headband’ (cf. Duchesne-Guillemin, BSOS 9.865, for further connections). See also tigra- zauda-. [zaudāäļm asf. DB 5.22.
Xarsadasya (or Xarsaisya), word of doubtful Meaning, Se; apparently gsm. of owner’s name. Justi, INB 173, reads lines 1-3-2, and gets Xišyāršā, approximately the АКК. form of the name of Xerxes ($163. VII); against this, see Wb. KIA 181.
tradu- sb. ‘wisdom’, meaning given by АКК. equivalent {ётё bissatum ‘word or message of wisdom’: Av. zralav- zrabw- ‘geistiges Wollen und Können’ (Bthl. AiW 535), Skt. krdtu- ‘power’, Gk. kparüs ‘strong’ (§33, 581, 5108.1, §153.III, §179.- n2); cf. Hz. RHRel. 113.27-9, Ар! 285-7. xradum asm. DNb 3.
X Sabrita- sb, ‘Khshathrita’, name assumed by the Median rebel Phraortes ($9.11, 578): Elam.
-
```


## [2026-09-06T16:10:44.504Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"θātiy\\|ātiy vb\\|^θah\\|thah\\|Oātiy\\|8atiy\\|Odtiy\" KNT.txt | head -20; echo \"---grep says\"; grep -n \"vb. ‘say\" KNT.txt | head"
}
```


### [2026-09-06T16:10:44.570Z] TOOL RESULT

```
3477:20 : afahya : xSapava :raucapativà : ava : akunavayatà —— :8atiy : Dárayava
---grep says
5341:gaud- vb. ‘conceal’: Av. gaoz-, Skt. githati (§88). apa- + gaud- ‘conceal, hide away’: apagau- dayahy 2d sg. subj. (§227.1) DB 4.55, 51. apagaudaya 2d sg. inj. (5215, §224, §227.II, $237) DB 4.54. gaub- vb. ‘say’, mid. ‘call one’s self’ (§213): Sas. РЫ. gowét ‘he says’, NPers. goydd, inf. guftán: perhaps a -bh- extension of pIE root *gheu- seen with -s- extension in gauga- (q.v.; Ву. BSLP 31.2.70). gaubataiy mid. (42851) DB 2,21, 31, 51; 3.15, 59. agaubaté imt. mid. DB 1.84, 93; 2.66f; 3.35, 55 (written agauratà, 454.11), 89f; 4.82. agauba^ià 3d pl. imf. mid. ($28617) DB 293. gaubdtaty subj. mid. (5285.1) DB 2.84; 3.86.
```


## [2026-09-06T16:10:50.846Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=210 && NR<=213 {print \"=== leaf \" NR \" ===\"; print}' KNT.txt | grep -n \"18[5-9]\\|19[0-2]\\|proclaim\\|say\\|Oah\\|θah\" | head -40"
}
```


### [2026-09-06T16:10:52.431Z] TOOL RESULT

```
16:tunwa"l- adj. ‘powerful’: pte. (8240) to *tu- | nautiy, pres. to lav- (8122; JAOS 15.170; otherwise — : Hz. ApI 329-32). Decl., $190.1, $210. tunwa | папа. (§210.1) DNb 10. tunuva"lam. (589) DB 4.65. tunuva*tahya gsm. DNb 9.
17:{шат pron. ‘thou’: GÀv. эт, LAv. tim, Skt. tuvám, pIE *tuyom; ef. Skt. dm, Gk. Dor. r$, Lt. tà, Gt. pit (576.1, $187). Decl., $194. turam nsm. DB 4.37, 41, 67, 70, 87; twa (§52.V; not йш = pIE *ti, as taken by Hz. ApI 329) XPh 46. Quam asm. (Skt. wam; S81, $114, $1323) DB 4.48, 58, 55, 74; DSt Of. ату gsm. (Skt. te, ОК. adv. to.) DNb 58 ($183). -taiy encl. gsm. in the following: Auramazdà-tay (852.11) DB 4.58; Aura- mazda-luiy DB 4.78; ada-taiy DNa 43, 45; ava-tary DB 4.76, 79; ша-іату DB 4.56, 58, 73f, 75, 716, 79; tya-laiy DNb 53; partalm-taiy| DNb 54; má-taiy DNb 52, 55 (cf. mà : tary 58); haw-tary DNa 57.
23:281°; DSf 47f, 49, 51°, 52, 54°, DH 4; XPh 24. tyat-saiy (6186) DB 1.57; 2.77; 3.48, 51, 74, 90, 91. tya as npm. ($52
39:187
53:188
57:баћ- vb. ‘declare, say’: Ау. sqh-, pres. sanha-, Skt. édsati, Lt. censet, рТЕ *kens- (§87); perhaps lacking the nasal in the OP present ($108.n1; MB Gr. $134, ef. Wackernagel, IF 45.321-7; dubious theories on the pronunciation, Hz. AMI 3.83-6). 6atiy (8131, $213, 5228.1; JAOS 35.332-4) AmH 4, 9; AsH 5; CMb 3; DB 1.3, 6, 8f, 11, 121, 17, 20, 24, 26f, 35, 43, 48, 61, 71, 72, 81, 83, 90; 2.1, 5°, 8, 11, 13, 18, 29, 37, 42, 49, 57, 64, 70, 78, 91, 92; 3.1, 9, 10, 19, 21, 28f, 40, 49, 521, 54, 64, 69, 75, 76, 83; 4.1, 2, 31, 33, 36, 40, 43, 45, 50, 52f, 57, 59, 61, 67, 69, 72, 76, 80, 86, 88; 5.1, 14, 18, 20, 30, 33f; DBa 4, 9, 13f; DPd 5, 12; DPe 5, 18; DPh 3; DNa 15, 30, 47; DNb 5, 22; DSa 3; рва 2f°; DSe 14, 30°, 41, 49°; DSf 8, 55; DSg 2f; DSi 2f; DS} 2, 4°; DSk 3; DSI 1; DSm 3; DSo 2°; DSt 6f; DZc 7; DH 3; XPa 11, 17; XPb 21; ХРе 9; XPd
88:dauStar- sb. ‘friend’: NPers. dost, Skt. jostdr- ‘loving’; agent-noun ($154.IT) to root daus-, Av. zaos- ‘enjoy’, Skt. jus-, Lt. gustat ‘tastes’, NEng. choose, pIE *ĝeus- (S88). daustà nsm. (§124.5, 6186.1) DB 4.56, 69, 74; DNb 7,8, 12; DS} 4.
98:189
```


## [2026-09-06T16:11:39.098Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC leaf for p.608: leaf ~ 608/2+15 = 319\"; awk 'BEGIN{RS=\"\\f\"} NR>=317 && NR<=321 {print \"=== leaf \" NR \" ===\"; print substr($0,1,3000)}' IEC.txt | grep -n \"60[5-9]\\|61[0-2]\\|sanh\\|kens\\|k̂ens\\|sah\" | head -30"
}
```


## [2026-09-06T16:11:40.101Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### KLN censor\"; grep -n \"^censor,\\|^census,\\|^censure,\\|^cosmetic,\\|^cosmos,\\|^cosmic,\" KLN_1966.txt | head"
}
```


### [2026-09-06T16:11:40.859Z] TOOL RESULT

```
=== IEC leaf for p.608: leaf ~ 608/2+15 = 319
```


### [2026-09-06T16:11:40.903Z] TOOL RESULT

```
### KLN censor
6959:censure,  n.  —  F.  censure,  fr.  L.  censura,  ‘judg¬ ment,  criticism’,  fr.  census,  pp.  of  censere.  See
6961:censure,  tr.  and  intr.  v.  —  F.  censurer,  fr.  censure. See  censure,  n.
```


## [2026-09-06T16:11:45.384Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '6945,6975p' KLN_1966.txt; echo \"=== cosmetic/cosmos ===\"; grep -n \"cosmetic\\|cosmos,\\|cosmic,\" KLN_1966.txt | head -12"
}
```


### [2026-09-06T16:11:45.454Z] TOOL RESULT

```
Derivatives:  cement,  tr.  v.,  cement-ation,  n.,  ce¬ ment -er,  n.
cemetery,  n.  —  Late  L.  coemeterium,  fr.  Gk. y.oiur,-nr,ptov,  ‘sleeping  room,  burial  place’,  fr. xoiuxv,  ‘to  put  to  sleep’,  which  is  rel.  to  xoi-ri), ‘place  to  lie  down  in,  bed’,  xot-ro;,  ‘place  to  lie down  in,  bed;  sleeping,  sleep’,  xoitcov,  ‘bed¬ chamber’,  xei(jl<xi,  ‘I  lie  down,  lie  asleep’,  xcoptr), ‘village’,  fr.  I.-E.  base  *kei~,  ‘to  lie,  rest’,  whence also  Goth,  halms,  ‘village’,  OE.  ham,  ‘home, house,  dwelling’.  See  home  and  cp.  city,  civil. Cp.  also  the  second  element  in  neossine. cenacle,  n.,  a  dining  room.  —  F.  cenacle ,  fr.  L. cenuculum,  'dining  room’,  fr.  cena,  ‘dinner’, which  stands  for  *qert-sna  (cp.  Oscan  kersnu, of  s.m.),  lit.  ‘portion’,  fr.  I.-E.  base  *qert-,  ‘to cut’,  whence  also  OI.  kpntdti,  ’cuts’,  Lith.  kertu, kirsti,  ‘to  hew’.  Arm.  k'ert'em,  ‘I  skin,  flay’,  and prob.  Hitt,  karsh-,  ‘to  cut  off’.  Base  *qert-  is an  enlargement  of  base  *qer~,  ‘to  cut’,  for  which see  carnal.
Cenchrus,  n.,  a  genus  of  grasses,  ‘the  sandbur, the  burgrass’  (bot.)  —  ModL.,  fr.  Gk.  y.b(/pac, ‘millet’.  See  Cachrys.
-cene,  combining  form  denoting  certain  periods in  geology,  as  in  Eocene.  —  Introduced  by  the British  geologist  Sir  Charles  Lyell  (1797-1875) fr.  Gk.  xatvoe,  ‘new’,  which  is  cogn.  with  L. recens,  gen.  -ends,  ‘new’.  See  recent  and  kainite. cenobite,  coenobite,  n.,  a  member  of  a  religious order  living  in  a  community.  —  Eccles.  L.  coe- nobita,  ‘a  cloister  brother’,  fr.  coenobium,  ‘a  con¬ vent’,  fr.  Gk.  xoivopiov,  ‘life  in  community, monastery’,  fr.  xoivo?,  ‘common’,  and  plop, ‘life’.  For  the  first  element  see  coeno-,  for  the second  see  bio-.
Derivatives:  cenobit-ic,  cenobit-ic-al,  adjs.,  ceno- bit-ic-al-ly,  adv.,  cenobit-ism,  n. cenoby,  n.  —  See  coenobium.
-cenosis,  combining  form  meaning  ‘discharge’ {med.)  —  Medical  L.,  fr.  Gk.  yivcomc,  ‘an  emp¬ tying’,  fr.  xsvop,  ‘empty’.  See  cenotaph, cenosite,  n.,  a  hydrous  silicate  and  carbonate  of calcium,  yttrium,  etc.  {mineral)  —  Formed  with subst.  suff.  -ite  fr.  Gk.  xaiv&q,  ‘new,  novel,  un¬ usual’  (see  -cene);  so  called  in  allusion  to  its composition.
cenotaph,  n.,  an  empty  tomb  in  honor  of  a  dead person  who  is  buried  elsewhere.  —  F.  ceno- taphe,  fr.  L.  cenotaphium,  fr.  Gk.  XEVordqxov, ‘an  empty  tomb’,  compounded  of  xsvfip,  ‘emp¬ ty’,  and  Tacptov,  neut.  of  TX9109,  ‘pertaining  to a  grave’,  fr.  Tob-poq,  ‘burial,  grave,  tomb’.  The first  element  is  cogn.  with  Arm.  sin,  ‘empty’ ;  cp. keno-,  kenosis.  The  second  element  is  rel.  to  Gk. Dootteiv,  ‘to  bury’,  titppoq,  ‘ditch’,  and  cogn. with  Arm.  damban,  dambaran,  ‘grave,  tomb’. Cp.  Taphrina  and  the  second  element  in  epitaph, tritaph.
Cenozoic,  adj.,  designating  the  geological  period extending  from  the  beginning  of  the  Tertiary  to the  present.  —  Compounded  of  Gk.  xoav6?, ‘new,  recent’,  ciot,,  ‘life’,  and  suff.  -ic.  See  -cene and  zoo-.
cense,  tr.  and  intr.  v.  —  Aphetic  for  incense, censer,  n.  —  Aphetic  for  incenser,  fr.  OF.  en- censier  (F.  encensoir),  fr.  Eccles.  L.  incensarium, fr.  incensum,  ‘incense’,  lit.  ‘that  which  is  burnt  , neut.  pp.  of  L.  incendere,  ‘to  set  fire  to,  burn  . See  incense,  ‘smoke  of  burning  spices’, censor,  n.  —  L.  censor,  fr.  censere,  ‘to  reckon,  as¬ sess,  estimate,  value,  deem,  judge’,  cogn.  with OF  samsati,  ‘recites,  praises’,  sariisayati,  ‘an¬ nounces’,  sasa,  ‘song  of  praise’,  Toch.  B  can- may  a,  ‘he  has  been  proclaimed’.  Cp.  census, excise,  ‘duty’,  recension.
Derivatives:  censor,  tr.  v.,  censor-ial,  adj.,  cen¬ sorious  (q.v.)
censorious,  adj.,  inclined  to  censure;  critical.
L.  censorius,  ‘pertaining  to  a  censor’,  fr.  censor. See  prec.  word  and  -orious.
Derivatives:  censorious-ly,  adv.,  ccnsonoits- ness,  n.
censure
censure,  n.  —  F.  censure,  fr.  L.  censura,  ‘judg¬ ment,  criticism’,  fr.  census,  pp.  of  censere.  See
censor  and  -ure.
censure,  tr.  and  intr.  v.  —  F.  censurer,  fr.  censure. See  censure,  n.
Derivatives :  censur-abte,  adj.,  censur-er,  n. census,  n.  —  L.  census,  ‘rating  of  property,  re¬ gistration  of  citizens  and  their  property’,  fr.  cen¬ sus,  pp.  of  censere.  See  censor.
Derivative:  census,  tr.  v. cent,  n.,  a  hundred  (used  in  certain  phrases  only). —  F.,  ‘a  hundred’,  fr.  L.  centum,  ‘a  hundred’. See  hundred  and  cp.  next  word,  centenarian, centner,  century,  percentage, cent,  n.,  the  hundredth  part  of  a  dollar.  —  Ab¬ breviation  of  L.  centesima  (scil.  pars),  ‘the  hun¬ dredth  part’,  fem.  of  centesimus,  ‘thehundredth’, fr.  centum,  ‘a  hundred’.  See  prec.  word  and  cp. mill.
cental,  n.,  a  unit  of  weight,  hundredweight.  — Formed  fr.  L.  centum,  ‘a  hundred’,  with  adj. suflf.  -al,  on  analogy  of  quintal. centaur,  n.,  i)  one  of  a  mythical  race  in  ancient Thessaly,  conceived  as  monsters,  half  man,  half horse  ( Greek  mythol.);  2)  (cap.)  =  Centaurus ( astron .)  —  L.  Centaurus,  fr.  Gk.  Kevxaupoc, which  is  of  uncertain  origin,
Centaurea,  n.,  a  genus  of  plants  of  the  thistle family  ( bot .)  —  ModL.,  fr.  L.  centaureum  or centaurium.  See  centaury.
Centaurium,  n.,  a  genus  of  plants  of  the  gentian family  (bot.)  —  ModL.,  fr.  L.  centaureum  or centaurium.  See  centaury  and  -ium.
Centaurus,  n.,  a  southern  constellation  between Hydra  and  Cross  (astron.)  —  L.,  ‘centaur’. See  centaur.
centaury,  n.,  any  of  a  group  of  plants  of  the gentian  family.  —  ME.,  fr.  ML.  centauria,  fr. L.  centaureum,  centaurium,  fr.  Gk.  xsvxaupeiov, xevxaupiov,  lit.  ‘Centaur’s  plant’,  fr.  K(vxaupoi;, ‘centaur’.  According  to  Pliny  (see  Nat.  Hist.  25, 66)  the  Centaur  Chiron,  wounded  by  an  arrow shot  by  Heracles,  heals  his  wound  with  this  plant, whence  its  name  xcvxaupeiav  or  xevxaupiov, ‘Centaur's  plant’  (see  centaur).  In  Latin,  folk etymology  altered  the  foreign  word  into  the compound  of  the  Latin  words  centum,  ‘hundred’, and  aurum,  ‘gold’.  As  a  loan  translation  of  L. centaureum  in  this  mistaken  sense,  arose  G. Tausendgiildenkraut,  ‘centaury’,  lit.  ‘thousand- golden-herb’.
centenarian,  adj.,  pertaining  to  a  period  of  a hundred  years;  n.,  a  person  one  hundred  years old.  —  L.  centendrius,  ‘relating  to  a  hundred’,  fr. centeni,  ‘a  hundred  each’,  fr.  centum,  ‘a  hun¬ dred’.  See  cent,  ‘a  hundred’,  and  -arian  and  cp. centner,  kantar.
centenary,  1)  adj.,  pertaining  to  a  century;  per¬ taining  to  a  period  of  a  hundred  years;  2)  n., a  century;  a  period  of  a  hundred  years.  —  L. centendrius,  ‘relating  to  a  hundred’.  See  prec. word  and  adj.  suff.  -ary.
258
centennial,  adj.,  of  a  hundred  years;  happening once  in  a  hundred  years ;  one  hundred  years  old ; n.,  the  hundredth  anniversary;  the  celebration of  the  hundredth  anniversary.  — -  Formed,  on the  analogy  of  bi-ennial,  fr.  L.  centum,  ‘a  hun¬ dred’,  and  annus,  ’year’.  See  annual,  biennial. Derivative:  centennial-ly,  adv. center,  centre,  n.  —  F.  centre,  fr.  L.  centrum,  fr. Gk.  xcvTpo'j,  ‘point,  prickle,  spike,  ox  goad, point  round  which  a  circle  is  described’,  from  the stem  of  xevxsiv,  ‘to  prick,  goad’,  whence  also xsvxcop,  ‘a  goader,  driver’,  xs <s-t6c,  (for  *xevx- x6p),  ‘embroidered’,  x£axpa,  ‘pickax’,  xovx6t;, ‘pole’,  fr.  I.-E.  base  *kent-,  ‘to  prick’,  whence also  Bret,  kentr,  OIr.  cinteir,  ‘a  spur’,  OHG. hantag,  ‘sharp,  pointed’,  Lett,  sits,  ‘hunter’s spear’,  situ,  sist,  ‘to  strike’,  W.  cethr,  ‘nail’.  Cp. centrifugal,  centripetal,  concentrate,  eccentric, Dicentra,  paracentesis.  Cp.  also  cestrum,  cestus, ‘girdle’,  kent,  ‘a  pole’,  quant,  ‘a  pole’. Derivatives:  center,  centre,  intr.  and  tr.  v.,  cen¬ tering,  centr-ing,  centre-ing,  n. centesimal,  adj.,  counting  by  hundredths.  — Formed  with  adj.  suff.  -al  fr.  L.  centesima(pars), ‘a  hundredth  (part)’,  fr.  centum,  ‘a  hundred’. See  cent  (in  both  senses), centi-,  combining  form  meaning  ‘one  hundred’, or  ‘a  hundredth  part’.  —  L.  centi-,  fr.  centum, ‘a  hundred’,  See  cent,  ‘a  hundred', centigrade,  adj.  —  Compounded  of  centi-  and gradus,  ‘degree’.  See  -grade, centigram,  centigramme,  n.  —  F.  centigramme, compounded  of  centi-  and  gramme,  fr.  Gk. Ypau.p.ct,  ‘that  which  is  written’.  See  centi-  and -gram.
centiliter,  centilitre,  n.  —  F.  centilitre,  compound¬ ed  of  centi-  and  litre.  See  centi-  and  liter, centillion,  n.  —  Formed  fr.  centi-  on  the  analogy of  million  (q.v.)  See  also  billion, centime,  n.  —  F.,  formed  fr.  cent,  ‘a  hundred’,  on the  analogy  of  decime,  ‘one  tenth  (of  a  franc)’, fr.  L.  decima  (pars),  ‘tenth  (part)’,  fr.  decern, ‘ten’.  See  cent,  ‘a  hundred’,  and  decimal, centimeter,  centimetre,  n.  —  F.  centimetre,  com¬ pounded  of  centi-  and  metre.  See  centi-  and -meter.
centipede,  n.  —  F.  centipede,  fr.  L.  centipeda, ‘centipede,  many-footed  insect’,  compounded of  centum,  ‘a  hundred’,  and  pes,  gen.  pedis, ‘foot’.  See  centi-  and  pedal, centner,  n.,  commercial  hundredweight.  —  G., fr.  L.  centendrius,  ‘relating  to  a  hundred’.  See centenarian  and  cp.  kantar. cento,  n.,  a  composition  made  up  of  selections from  different  works.  —  L.  cento,  ‘patchwork’, cogn.  with  OI.  kantha,  ‘patched  garment’,  OHG. hadara,  MHG.,  G.  hader,  ‘rag’  [cp.,  with  -/- formative  element,  MHG.  hadel  (whence  F. haillon),  ’rag’].  Gk.  xevxpwv,  ‘piece  of  patch- work’,  is  a  loan  word  fr.  L.  cento,  and  was  in¬ fluenced  in  form  by  xtvxptov,  ‘one  that  deserves the  goad  (=  xivxpov)’.  Cp  Centunculus.
259
=== cosmetic/cosmos ===
4710:Derivative:  bell,  n.,  a  bellow  (as  the  cry  of  the stag  in  the  rutting  season);  a  roar, belladonna,  n.,  1)  a  poisonous  plant ;  2)  a  drug  ex¬ tracted  from  this  plant.  —  It.  (whence  F.  bella- done),  lit.  ‘a  beautiful  woman’,  from  bella,  fern, of  bello  (fr.  L.  bellus),  ‘beautiful’,  and  donna, ‘woman,  lady’  (fr.  L.  domina)  (see  beauty  and dame  and  cp.  beldame);  so  called  in  allusion  to the  cosmetic  once  made  from  it.
9336:cosher,  tr.  v.,  to  pamper.  —  Of  uncertain  origin, cosher,  adj.  —  A  var.  spelling  of  kosher, cosignatory,  adj.,  signing  jointly  with  another or  others.  —  Formed  fr.  co-  and  signatory, cosine,  n.,  the  sine  of  the  complement  of  an  angle (trigon.)  —  Fr.  co.  sinus,  abbreviation  of  ModL. complement i  sinus,  ‘the  sine  of  the  complement’. This  name  and  its  abbreviation  into  co.  sinus were  first  used  by  Edmund  Gunter,  a  mathe¬ matician  of  the  early  17th  cent.  See  complement and  sine  and  cp.  cotangent,  cosecant. cosmetic,  adj.,  serving  to  beautify.  —  Gk.  xoa- [tijtixo?,  ‘skilled  in  arranging’,  fr.  xoapojTi?, ‘well-ordered’,  verbal  adj.  of  xooptav,  ‘to  order, arrange,  adorn’,  fr.  xoapoc,  ‘order,  ornament, decoration,  set  form;  world,  universe’.  See  cos¬ mos  and  -ic.
9337:Derivatives:  cosmetic,  n.,  a  preparation  for beautifying  the  skin,  cosmetic-al-ly,  adv.,  cos- metic-ian,  n.,  one  who  makes  or  applies  cos¬ metics.
9338:cosmetology,  n.,  the  study  of  cosmetics.  —  Com¬ pounded  of  Gk.  xooprjToc,  ‘well-ordered’  (see prec.  word),  and  -Xoyla,  fr.  -Xoyo ?,  ‘one  who speaks  (in  a  certain  manner);  one  who  deals (with  a  certain  topic)’.  See  -logy, cosmic,  adj.,  pertaining  to  the  cosmos;  vast.  — Gk.  xoapuxA?,  ‘of,  or  connected  with,  the  world’, fr.  xo ctjxoc,  ‘world’.  See  cosmos  and  -ic. Derivatives:  cosmic-al,  adj.,  cosmic-al-ity,  n., cosmic-al-ly,  adv.
9339:cosmo-,  combining  word  denoting  the  world.  — Gk.  xoct|j.o-,  fr.  xoapiop,  ‘world’.  See  cosmos, cosmogony,  n.,  the  origination  of  the  universe.  — Gk.  xoafzoyovtx  (whence  also  F.  cosmogonic ), compounded  of  xoafio?,  ‘world’,  and  -yovla,  fr. yovo?,  ‘race,  offspring’.  See  cosmos  and  -gony. Derivatives:  cosmogon-ic,  cosmogon-ic-al,  adjs., cosmogon-ist,  n.
9351:cosmorama,  n.,  an  exhibition  of  views  of  different parts  of  the  world.  —  Compounded  of  Gk. xoap.0?,  ‘world’,  and  opap-a,  ‘that  which  is  seen, view,  sight’,  fr.  opav,  ‘to  see’.  For  the  first  ele¬ ment  see  cosmos.  The  second  element  is  cogn. with  L.  vereri,  ‘to  observe  with  awe,  revere,  re¬ spect,  fear’,  OE.  wxr,  ‘cautious,  aware’.  See ware,  ‘alert’,  and  cp.  the  second  element  in  dio¬ rama,  myriorama,  panorama.  Cp.  also  -rama. Derivative:  cosmoram-ic,  adj. cosmos,  n.,  the  world  conceived  as  an  ordered whole.  —  Gk.  xoapto?,  ‘order,  ornament,  de¬ coration,  set  form;  world,  universe’,  whence xoauiv,  To  order,  arrange,  adorn’,  xoapi7)x6? (verbal  adj.),  ‘well-ordered,  regular’;  of  uncer¬ tain  origin.  Cp.  cosmetic,  the  first  element  in cosmetology  and  the  second  element  in  macro¬ cosm,  microcosm.
23036:mascagnite,  n.,  ammonium  sulfate  (mineral.)  — Named  after  its  discoverer,  the  Italian  anat¬ omist  and  physiologist  Paolo  Mascagni  (1752- 1815).  For  the  ending  see  subst.  suff.  -ite. mascara,  n.,  a  cosmetic  preparation  for  coloring the  eyelashes.  —  Sp.  mascara,  ‘a  mask’,  fr. Arab,  mdskharct,  ‘mockery ;  buffoon'.  See  mask, mascle,  n.,  1)  a  steel  plate;  2)  a  lozenge  voided (her.)  —  OF.  mascle  (F.  made),  fr.  L.  macula, ‘spot’.  See  mackle,  made, mascot,  n.,  talisman,  charm.  —  F.  mascotte,  pop¬ ularized  by  Audran’s  operette  La  Mascotte (1880).  F.  mascotte  is  a  loan  word  fr.  Proven?. mascoto,  ‘sorcery,  charm’,  fr.  masco,  ‘sorceress, witch’,  which  is  of  uncertain  origin, masculine,  adj.  —  ME.  masculin,  fr.  OF.  (=  F.) masculin  (fem.  masculine),  ‘of  the  male  sex’,  fr. masculus,  ‘male’,  fr.  mas,  ‘male’,  which  is  of uncertain  origin.  Cp.  emasculate.
```


## [2026-09-06T16:11:47.313Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"sen-, sn-\\|^sen-\\|sanh\\|s'ansati\\|kens\" IEC.txt | head -20; echo \"=== find printed page 608 marker\"; awk 'BEGIN{RS=\"\\f\"} /(^| )60[78]( |$)/ {print NR}' IEC.txt | head -20"
}
```


### [2026-09-06T16:11:49.141Z] TOOL RESULT

```
46:The present Dictionary was begun tentatively in January 1925 before the appearance of Walde's and Pokorny's Indogermanisches Worterbuch (1927-32), but was set aside for a number of years because certain information was lacking to give it complete authenticity. The most acutely felt deficiencies were the absence of a full Albanian dictionary, made good by the author between 1939 and 1948; a full dictionary of Old Irish; the absence of a Welsh etymological dictionary; inadequate dictionaries of Lithuanian and Latvian; and a confused & inadequate understanding of, and exploitation of, the vocabulary of old and modern Armenian. Hittite, deciphered by the Czech Bedfich Hrozny in 1915, was unavail- able, as were the documents of Mycenaean in Linear B deciphered by M. Ventris, and ad- ded to by Bennett, Blegen and Mabel Lang. Tokharian became more fully available only with the publication of Van Windekens's Tokharian Etymological Dictionary of 1941, with additions in “Orbis” in 1968-70. Ossetic, believed to be the only surviving relic of ancient Scythian, became available with the publication of Vsevolod Müller's three-volume dictionary of 1927-34.
6958:keló, ið (1) “lift, bear, bring’. Cf. WP I, 434 & II, 600 and keleso above Oss. cf. car, cará (ceiling': Li. kelis, io ‘rise’); Tokh. A kal B kal- (carry; bear; tolerate’ (Van Windekens); Gk. cf. keléontes ‘upright beams of loom’; MAib. and It. Alb. qell, aor. qella ‘bring’; Gk. cf. kélōn ‘swipe of well- bucket’; Lat. cf. ex-cello beside celsus, adj. “tall; beetle-browed'; lo onis "one w. large forehead"; OWel. celi (/heavens', fr. *keleso); OE cf. heolor ‘scale, balance (?); OCS cf. čelo (“forehead”, a former -es-stem, cf. čele- sínü, adj. Semantics of lat. frons, see bhr&hnt- above); Li. keliü, kélti (3) “carry” (pf: keliau); Late celu,t “lift; rouse; choose?
7009:kent- (2) f'endmost; before, after’. (Super- lative: kentomo-) Olr. cét-, cpds. ‘chief; Ir. céad "first, cf. céadamh *May day, the first of May': W cyn- taf ‘first’: Go. hinduma, OE hindema *'hind- most, last’; Gaul. cintu-, cpds. ‘first: MW E W cynt ('earlier'; adj. “first'); Br. kent "before": Cor. kens, kyns, kenj (kendZ) ‘former’; Bur- gundian (in Lat. context) cf. hindemos ‘chief: Go. hinduma, OE hindema *last', but W cyn- taf, Ir. céadamh (see above); MHG cf. hinder *back, behind' beside G hinten, id. (fr. *ken- tomo-)
7401:klk- (2) “lump” Cf. klk, id.; Latv. cf. kilkens ‘dumpling’
9272:Kuibh- (2) ‘gadfly; squeak, buzz Gk. síphon (2) ‘gadfly’; Oss. cf. c'uvvàá bindzà, id.; Ir. cíob ‘pip in chickens"
13954:quendh- (quenmn-, quens-) (1) “head, end, tip, point, headland'. Cf. WP I, 398 Oss. cánd, Dig. cándà “pile, mass, cairn’; Hes. cf. ténthinoi, mpl. ‘cobble stones, flat stones’ (phonol. ambig.); MIr. cend, cenn, Ir. ceann, m. pl: cinn & ceanna ‘head, end’; Gaul. pen- nos, m. ‘head’; Br. penn, pl. -u, m. ‘head, top’; cf. pens, f. (“arse”, fr. *quent-?); W pen, -nnau, m. “head, end’; Cor. pen, pl. pennow, m. ‘head, chief, chapter; E whin "hard rock, doleritic quartz-basalt; furze’; Li. cf. kensas, kesas, m. ‘hillock’; cf. (z-gde or r-gde) Cz. énét, čnít, inf. jut out?
15000:saneu-mi, sanu- ‘get, reach, seize’. Cf. WP II, 493. Cf. asnu- Skt. sanmi, v. ‘acquire’; cf. sanih, m. ‘gain’; Hitt. sanhh(mi), pret: sānahhun, v. ‘approach, attack; try, seek’; Arm. hanum, aor: hani, v. (extract, draw, derive’? Cf. sanio, but not in sense of ‘wipe, delete’); Gk. Hom. aínumai, v. ‘seize, get; enjoy” (fr. *sanju-? Bois. Hof. un-
15194:sen-, -sen “self Ir. -sean, -san (3s. m & 3 pl. mf.), id.; OCS (and com. Sl.) se; Osc. cf. siom, id.
15195:sen- (sena, iom, io, us) ‘figure, image, phe- nomenon' Skt. sanuh, mn. /^wiseacre; epithet of sun; high wind'; Hitt. senas “image, clay or wax figure’; OHG cf. sélt-sàni, n., -sani, f. marvel beside un-sani, n. ‘monster’; Ir. sion, f. ‘weather’; W hin, f. id.
16605:sngh-nu- ‘reach’. Cf. se&h- and WP II, 482 Skt. (ambig. vocalism) saghnómi, v. "be a match for’; Hitt. sanhami, v. “approach; test; attack'; imperative: sah!; OCS (and com. Sl.) segno, -noti, v. ‘reach’; OCz. sahu, 2s: sěžeš, inf. síci, v. id.
16606:snguhó, ið ‘singe, scorch’. (Cf. WP II, 495) Hitt. sanhwami, sanhumi, v. ‘roast: Gk. hápto, v. (2) ‘kindle’; haphé, f. ‘ignition’; cf. áphthai, fpl. “mouth ulcers'; n-áphtha “crude oi (?); MHG cf. (o-gde) senge, f. ‘dryness’; sengen, v. ‘singe, burn’; OE sengan, wv. id.; cf. also G sangeln, v. ‘singe; tingle’; MHG sun- gen ‘be singed’
20462:ulobhos (?) *top, head, hill Gk. lóphos, m. ‘neck, mane, tuft, crest, peak'; lophía, f. id.; Maced, cf. otto-lobus ('eight- hill, a place-name); cf. also Gk. ko-lophón, m. (top, peak, if fr. *Kor-ulobhon, cf. Kor-, Kor-) (hardly Tokh. A lap “head? as V. Windekens)
=== find printed page 608 marker
175
720
724
725
726
730
733
```


## [2026-09-06T16:11:58.500Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '6990,7015p' IEC.txt | cut -c1-400"
}
```


### [2026-09-06T16:11:58.554Z] TOOL RESULT

```
meri ‘poison’; Srb. čemer ‘bitterness’; Big. čemer, as OCS; Cz. čemer ‘rash, pain, nausea’
beside čemeřice, Cemerka “sneezewort'; R
čemerica ‘hellebore’; Srb. Cemerika, id.; Li.
kemeras, keméras ‘hemp agrimony’; Latv.
kemers (id?) but Camarags 'sneezewort (kems-, variant of type kem-, q. v. Cf. km-, kmst-, kmt-
Li. cf. kemšu, inf. kimšti ‘stuff, cram’; Latv.
kelo, ið — kents-
20
25
30
35
40
45
488
kemsu, kimst ‘plug’)
keng- 'seize, grip, hold; hold, hook, grapple, hobble'. Cf. knk- Av. cf. Caro ‘claw, cleft hoof; Per. Gäng ‘claws, fingers”, cf. also čängāl, čängul ‘claws, hook’; Lat. cingo, Gre “tie; gird” beside cingulum, cingula (LW in Ir. ceangal ‘tying, binding, ceanglaim, v.id., and in W cengl, f. “band; girth; hank’; cenglu “bind'); ON hinkr, n. (delay', fr. *kengro-); Sw. hink
(kenk- *quake', see next)
kenkolos, kenklos ‘unsteady, hobbling, limp- ing’; radical: kenk- Oss. cànkul ‘crippled; cripple’; Skt. Caficalah ‘wagging, unsteady’, cf. čañkāmi limp, tremble, flicker’; Gk. kégklos ‘wagtail’ beside kígklos, id. and kigklízo “be restless’; MHG hingeln ‘limp, hesitate’; Li. kenklë ‘hollow of the knee’, cf. kinka (‘wobbling of the knees; hock, fetlock’, f
kent- (1) 'suffer, make suffer. WP I, 513. (Variants: kont-, knt-, kents-) Olr. céssaim ‘suffer’; Ir. céasaim ‘torment’ (both < *kents-); OE cf. hinder ‘sad, sinister’ beside hypan, v. (sack', fr. *kntjo); Cz. cf. z-kusit (experience, suffer”, fr. *kontseio); Li. kenčiu, inf. kęsti, id. beside kantrüs ('suffer- ing")
kent- (2) f'endmost; before, after’. (Super- lative: kentomo-) Olr. cét-, cpds. ‘chief; Ir. céad "first, cf. céadamh *May day, the first of May': W cyn- taf ‘first’: Go. hinduma, OE hindema *'hind- most, last’; Gaul. cintu-, cpds. ‘first: MW E W cynt ('earlier'; adj. “first'); Br. kent "before": Cor. kens, kyns, kenj (kendZ) ‘former’; Bur- gundian (in Lat. context) cf. hindemo
kents-, see kent- (1) Ir. cf. céasna ‘trouble, want’; Li. kesmas "hard.
489
ship”
kepó, ið (1) ‘tap, peck, prick, strike’ Av. čap- ‘destroy’; Oss. cäf, s. ‘blow, wound’; càvin ‘strike’; Alb. qep (1) ‘tap’; Li. cf. kēpš- Cioti ‘tap, rap’ *
kepo, io (2) “join, attach, adhere'. Cf. WP I, 344 Alb. qep, aor. qepa (2) ‘sew’; Ukr. cf. pry-, u-Cepyty ‘attach’; Li. kempü, képti (2), aor. képau ‘stick, adhere’; Latv. Ken, kept, id., aor. ķepu; cf. ķepa ‘paw’
(kepəl, see quepəl- ‘shake, sway’, etc.)
```


## [2026-09-06T16:12:06.014Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"afsāna\\|afsana\\|afsāne\\|fsāna\\|afsun\\|afsūn\" IEC.txt | head; echo \"=== page 608 ===\"; grep -n \"^608$\\|^607$\\|^609$\" IEC.txt | head"
}
```


### [2026-09-06T16:12:07.999Z] TOOL RESULT

```
14412:rapsió (rapotio) 'shout, bluster, bully’. (Vari- ant rasp-) OHG refsen, MHG refsen & respen, v. ‘bully’; OE repsan, v. ‘blame’; ON refsa, v. (“punish?. NB: ON has both -fs- and -ps- as reflexes of IE *-ps-, cf. the parallel raftr & raptr 'rafter'); Srb. cf. ropcem, roptati, v. ‘brawl’; Blg. ropščà, roptàja, id.; OHG cf. rafsunga, s. ‘blame’ and Sw. räfst, m. ‘reproof
=== page 608 ===
8626:607
8643:608
```


## [2026-09-06T16:12:10.241Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '8626,8665p' IEC.txt | cut -c1-500"
}
```


### [2026-09-06T16:12:10.333Z] TOOL RESULT

```
607
‘motley’; Ir. cíar ‘dark’; ON (ambig.) hárr Cgrey', but cf. Kaisros. Scots har, haar “low mist” is perh. fr. Norse)
Keita (Keit-) ‘rest, lair, abode, room’. Cf.
Kei-, Ki-, etc. Skt. Sáyita ‘rest, abode’; Go. hépyo ‘room’. Long-grade radical also in Skt. śāyah, adj. “sleeping, resting’; short-gde in śayah, id. and m. ‘sleep, rest, sofa". Cf. WP I, 358 & 376
Kekos, om, à ‘fodder, greenstuff. WP I, 381 (Kéquos?)
Skt. Sakam *potherb'; ON (ambig.) há (“after- math’, but cf. kau-); Li. Sëkas “green fodder’; Latv. séks, id.
Kekuros, ios *mild, tame, pleasant, docile' (*Kequros? for Arm. sovor “used to . . 2 Skt. Sakurah, id.; Lat. cicur, id.; OE heore, id.; MHG ge-hiure, id. beside hiuren, v. ‘greet’; ON hyrr, id. beside hyrast ‘get brighter, cheer up’. (The alleged Sabine form cipru- ‘good’ is inconclusive as a cognate, cf. WH:LEW: er and hircus for speculations on -p-/-qu- in Sabine)
kél- (1) “hide, cover, shelter. WP I, 433 Short vowel in Mir celim, Ir. ceilim ‘hide’; ceal, m. *cover; death'; W cel, pl. -ydd 'shel- ter, corpse'; adj. “hidden; Cor. kel, pl. kelow, m. & adj. “hide, hiding; hidden'; W celu, v. ‘hide’; OHG, OE hélan, id.; Du. helen, v. id.; extns. in Gk. kel-ainós ((dark': W celain *corpse); OE heol-stor, adj. ‘dark’; Gaul. (?) cel-icnon ‘tower; MHG ge-hilwe “haze, cloud”; Skt. saranáh ‘protective’; -am, n. and sarman, n. ‘shel
kěl- (2), kél-àqua “dart, arrowhead, quill’ Skt. cf. salam ‘quill’ beside $alaka ‘rod, arrow- head’; Arm. slak, gs A abl. -av “dart, arrow’; Gk. kélon ‘arrow, arrow-shaft
Kelmn- (Kelmó(n)) (1) “cover, shelter’. Cf. Kél- (1)
Keiota (Keit-) — Kensos, à, us
20
25
30
35
40
45
608
Skt. Sarman ‘shelter’; Go. hilms ‘helmet’; OHG hélm, id.; OE helm, m. ‘helmet; crown of tree; protection; lord’; ON hjálmr (1) *hel- met; Li. Selmuó, gs -eñs (1) ‘cover, lid; Gmc. LW in SI. Slémü “helmet?
Kelmn- (Kelmo(n)) (2) ‘beam, tie-beam, roof- tree'. (Variant? Ki-elm-, cf. Ki- and el- (2)). Cf. Klm- in Supt:K Ober cf. 0armis ‘timber’; Oss. (?) sámàn (axle'. 1/r are sometimes lost in Oss.); ON hjálmr, m. (2) ‘hayrick’; OCS slémé, n. ‘beam’; Li. Selmuoó, eps (2) *roof-ridge, gable’; Latv. selmenis, id. Variants include Arm. seyan, o-st. ‘table’; Gk. keléontes 'loom-beams'; Ger. z-grade Holm, m. “horizontal bar, tie-beam, truss’. For a possible variant of type *K
kemnd- (Kemndh-) ‘young deer, female deer’. WP I, 385 Gk. kemás, gs -ádos ‘young stag’ (f); OHG hinta, MHG hinte, hinde, Du. hinde, OE hind, f. ‘hind’; Sw. hind, pl. -or, f. id. (Oss. säg ‘goat’ is an uncertain cognate. For vocal- ism cf. sädä ‘100°)
KenKelos, variant of kenkolos, q. v.
Skt. cf. sansalah ‘moving’
Kenos ‘empty, vain, silent’. WP I, 390 Skt. sanah “quiet, soft; Arm. sin ‘empty, vain, futile; Gk. kenós, id. beside Ion. keinós, Hom. kenéos, id.
Kens- (Kensmi) (variant of Kēs-mi, q.v.) *utter, pronounce'. WP I, 403 Skt. Sámsami ‘recite, tell, promise’ beside (var- iant) $asami ‘discipline’; Av. sásmi ‘teach’ be- side sasmi ��speak, order’; Ober, cf. 0àtiy, 3s ‘says’; a-0aham ‘I said’; Arm. asem, osem (‘say, speak, tel. Phonology obscure); Tokh. A känts- ‘vow, admit’; Alb. thom, them, 3s. thotë ‘say’; Lat. censeo, Gre ‘consider, think’; OFris. (?) henzia “approve, ratify’; OCS (defec- ti
Kensos, à, us 'utterance, opinion, state- ment. Cf. Kens- (and Kés-). WP I, 403 Skt. $ámsab ‘pronouncement, cal? beside $asah “order”; Per. cf. fa-sana ‘fable’; Lat. cén- sus, gs -us 'polltax, census’; LW in Gk. kén- sos, id.; Osc. cf. censaum, inf. ‘to vote, ad-
609 judge’; Alb. cf. e thânë, f, (“saying”, fr. a type *Kons-)
Kent- ‘prick, point, spike’. WP I, 402. Cf. Kentrom Oss. síndz, Dig. sindzä ‘thorn, splinter beside síngin, Dig. singin, adj. ‘prickly’; Gk. cf. ken- táð, kentéð, v. ‘prick’; Alb. thind ‘beak’; Br. cf. kentel, pl. -téliu, f. ‘point, time, hour, les- son’; MHG cf. hint-ber ‘raspberry’; G Him- beer, id.; OE hind-berge, EME hind-berry, id. (Isophones: Gaul. cintu- “first; OW cynt, W cyn ‘before’; Ir. céad- cpds. “first-?; céadamh “of the first of May’
Kentrom, à (Kütr-) ‘point, spike, spur’. Cf. Kent-. WP I, 402 Arm. santr, gs santer (‘comb’, fr. Kütrə, but gs vocalism obscure); Gk. kéntron ‘spur, prickle, goad, sting’; LW in LLat. centria ‘sting’; Alb. thundër, f. (hoof, heel, talon, thorny plant’, fr. *Kntrá); Gaul. centron (part of a mountain- name); Br. kentr, pl. -u, f. ‘spur’; Cor. kentr, pl. ow, f. ‘spike’; Olr. centir, cintir ‘spur’; Du. (?) hinder, m. ‘annoyance’; Fris. ‘obstacle, catch’; 
Keng (Kop-) ? ‘obtrude, bristle’. (The Alb. forms are ambig. cf. Kap- & Koip-) Alb thep ‘sharpen’; cf. o-gde gë-thapë ‘claw’; Li. Septi, pres. Sempu, pf. šepau ‘bristle’; cf. o-gde šãpas ‘bristle, awn’. Only the Lith. forms are explicit
Kephelos (Kepolos) "a fish". (IE?) Sk. $apharah ‘cyprinus sophore'; Scyth. (?) cf. sapérdes (groundling' (err. for *sepár-?); Gk. képhalos *mullet; Li. Sápalas ‘roach’; Latv. sapals ‘Danubian carp’
Kequros, see Kekuros
Ker- (1) (Kerā, ios, iə. Cf. Kerið, and Kerus as a separate entry). WP I, 408, 410, 427, 454, and II, 576 Skt. sáryah ‘arrow’; Sáryà ‘cane, shaft, arrow’; EMAIb. therrë, therë, f. ‘briar; MHG hir, smfn. ‘pang; violence’; Li. Serys, m. ‘bristle’
Ker- (2) (e-grade form of type Kr-, Kor-
Kent- — Kerdhos, à
15
20
25
30
35
```


## [2026-09-06T16:12:26.659Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### PHD\"; grep -n \"^saxwan\\|^sax(w)an\\|saxwan\" PHD.txt | head; echo \"### NYB\"; grep -n \"saxwan\\|sax'an\\|sxwn\" NYB_vol2_glossary.txt | head; echo \"### HRN soxan/afsana\"; grep -n -i \"suxan\\|sujan\\|sacan\\|afsāna\\|afsana\\|fasāna\\|fasana\" HRN.txt | head -20; echo \"### HUB\"; grep -n -i \"suxan\\|afsana\\|afsāna\\|fasāna\" HUB.txt | head -20"
}
```


### [2026-09-06T16:12:26.751Z] TOOL RESULT

```
### PHD
312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
564:sang [KYPA < A kyp’; CCA (in error); sng | (P?sng), N ~] stone, rock. -~sar [-s?1] stony place. sanj-, v. saxtan. sanwar [snwl = Av. 0anwar-] bow. sar [LOYŠE < A r'šh; sl | M sr, N ~] head; top, summit; end, begin- ning. | sarāsar [s?s] | N ~] from end to end. sard [s/t! | M srd, N ~] cold. ^Àh: coldness. sardag [sltk' = Av. sarada- | (M s’rg), J srdg] sort, kind. sardsér [s/tsyl | N ~] cold region, uplands. sārēnīdan, sárén- [s’/yn-ytn'] provoke. sargen [slgyn' | N sargin] dung, manure. sarmāģ [s/m?k! | N затта] coldness. sarw [slw(b)' | M srw, N ~] cypress. sas [ss | N ~] bug. sāstār [s”st”7 | P s?s?r] commander; tyrant. ~ih: tyranny. Sawah [sw’h = Av. sawahi-] the western continent of the earth. saxt [sQ)At! | N ~] strong, hard, severe(ly); very. “Аһ: strength, severity. saxtag [shtk! | (N saxtiyán)] morocco leather. saxtan, ѕапј- [s’htn', snc- | N ~] weigh. sāxtan, sáz- [s*htm!, ?c- | (P s?*c-), N ~] make, prepare; tolerate. sāxtārīh [Pht yh] toleration, forbearance. saxwan [МРУА < А mly’; shwn' | М sxwn, N suxan] word, speech. say-, v. südan. sayag [sg dk! | M ғур, N sáya] shade, shadow. lsaz- [sc- | M sz-, N ~] be fitting, proper, worthy. --i$n(ih): fitness, worthiness. 26а2-, —išn, v. sazistan, saz-, v, sáxtan. sazāģ [sk | N sazá] fitting, worthy. ~th: fitness, worthiness. ~ ~war [-w/ | N sazāwār] = затар. sazistan, *saz- [sc-stn'] pass. ~išn: passing, transience. ~iSnig : transient, perishable, mortal. sé [3; TLTA < А tl? | M sh, N si] three. sëb [syf | N ~] apple. sēj [sye = Av. 'Gyejah- | N ~) danger, trouble. --ómand [-”zvmnd | N —mand] dangerous. sel [si | N —] spear, javelin. sém [sym | N —] — asém. !sén(ag) [syn(k)! | N sina] breast, chest. *sén murw [synmzlw | (N simury)] a fabulous bird.
1509:deceitful dēsaxwan, zūr.
3766:speech dranjišn, gēwišn, guftārīh, saxwan, waz; v. good, evil.
4106:two-tongued dó-saxwan. Lyrannous sézd(én), statt, tyranny sāstārīh, sēzd, tyrant sāstār,
4343:word ēwāz, mārīg, saxwan, sraw, waz; holy ~ máàns?r(spand).
4816:saxwan sahóg
4871:1 az! muhrag mang, moy saxwanī moyén tis’, cis! tis-izt moyag muhr osmar-t бёгпагї$пї O$murdan! ket murdar mog
5433:gumēzagīh gumczag gumēzišn ёп! röz-šabän! dósaxwan dūsēn: stiin-t stadant dusrawih dusraw
### NYB
6127:soxtan swend: sčkand swd: süt swyg: a-sčhišn sxt: saxt sxwn: saxUan sygyn: *sak syh: ?sih szyd: sac-
### HRN soxan/afsana
### HUB
4400:= phi. fairaxv; suxtin ^= suxan *Wort', paz. saxun aus
7466:ap. &uxra'; suxun^ suxan *Wort* aus iran. "^saxvan- = ap.
7771:suxan 'Wort', alter sax^an 'speech' JRAS. 1894, p. 4692aus
```


## [2026-09-06T16:12:31.380Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '7460,7475p' HUB.txt; echo \"-----\"; sed -n '7765,7780p' HUB.txt"
}
```


### [2026-09-06T16:12:31.435Z] TOOL RESULT

```
vasna-^ asnaiy *nahe' = zd. asne, Vgl. zd. frasna^ = skr.
pragna-] asm, gen. von asan-,
§ 99. Ap. d im Anlaut vor Vokalen = iran. s =
idg. A;', k% ist im Np. nicht durch h sondern durch .s ver-
treten :
sal Mahr = zd. sareda-; surx Voth* = zd. suxra-,
ap. &uxra'; suxun^ suxan *Wort* aus iran. "^saxvan- = ap.
*&a(h)uvan' von &ah *sprechen, skr. gq^, zd. satlh; sang
*Stein, ap. a&angaina- *steinern ; sard 'kalt' = zd. sareta-;
saya *Schatten' = skr. chdya- (mit ch aus idg. k%) u. s. w.
Vgl. Horn 688 — 765. Ebenso in Zusammensetzungen :
afsan *Wetzstein , afsar 'Krone', pdsux *Antwort\ pasand
'angenehm' (oben p. 41), dsiidan ruhen*, duvSst *zweihundert'
=-• zd. duy^ saite; farsang = phi. frasang naQaaiyyric,
u. s. w.
Im Arm., Phi. und Paz. erscheint hier gleichfalls
-----
QUQ = zd. x^a&ra- (KZ. 33, 217), wahrend die Keilinschriften
auch hier wieder h nicht schreiben und nur uvd geben:
uvcLrazmis, harauvatis. Auch hier weicht also das Mittel-
und Neupersische vom Dialekt der Keilinschriften wieder ab !
b) im Inlaut: dozax 'Holle = phi. inschr. dQsdxm
d. i. dozaxv, zd. daoSanuha-, arm. dzoxK (oben p. 64); suxun,
suxan 'Wort', alter sax^an 'speech' JRAS. 1894, p. 4692aus
phi. sax^an, arm. Rast-sohun (Mos. Chor. 150); pdstix
'Antwort* — phi. *pasaxv neben pasaxv (oben p. 36); farrux
glucklich' = phi. farraxv = ap. *farna{h)uva7i' (oben p. 83),
arm. xorox in Xorox-azat (Sebeos 107) = p. FarruxzdS ^=
Xorazad (Tab. 395) u. s. w. ; arab. Arruxaj aus *Arax^ad
= gr. XoQoxodd bei Isidor von Charax, alter \4pax(jDoia^
ap. harauvatis (Tab. 157).
§ 109. Idg. 8 vor und nach Konsonanten.
a) Idg. sy = ap.J% = np. h: dih *Dorf', arm. deh =
```


## [2026-09-06T16:12:47.930Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Wort'\\s*=\\|saxvan\\|sax\\^an\\|suxan\" HRN.txt | head -10; echo \"=== search Horn 765 region ===\"; grep -n \"^ *76[0-9]\\. \\|^ *688\\. \" HRN.txt | head -20"
}
```


### [2026-09-06T16:12:47.993Z] TOOL RESULT

```
=== search Horn 765 region ===
6056:688. süyfeii 'machen, ausführen', Praes. säz-em, säz 'Gerät*.
6621:760. st 'dreissig'.
6624:761. siyah *scliwarz', sit/dhi.
6634:762. sex (i'^i^iit auf be/^), Sa di, Gul. 46 Zeile 5 v. u., Spr.)
6640:763. si^deh 'dreizehn*.
6645:764. s~ui% 'Kummet'*).
6661:765. sl/inury 'Greif, Adler; N. pr.', vergl. STn\duxt,
6666:766. Süx 'Zweig, Ast; Hörn (des Stieres), Greweih'.
6673:767. Häd 'fröhlich, heiter , sadt,
6677:768. Hiiiu 'Abendmahlzeit, Nachtessen*.
6698:769. San 'ihr (Enclit.).
```


## [2026-09-06T16:12:53.063Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Wort'\" HRN.txt | head -20; echo \"=== afsana/fasana in HRN ===\"; grep -n -i \"fable\\|Fabel\\|Märchen\\|Marchen\" HRN.txt | head -20"
}
```


### [2026-09-06T16:12:53.128Z] TOOL RESULT

```
11030:185. Hvav *Wort', nur im AW.-Komm.
11031:aw. sravah' 'Wort'; ai. grävas- 'Ruhm'; ksl. sloro
11032:'Wort'.
=== afsana/fasana in HRN ===
```


## [2026-09-06T16:12:57.303Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"uxan\\|ux^an\\|saxvan\" HRN.txt | head -20; echo \"=== afs ===\"; grep -n \"^ *[0-9]*\\. afs\\|afsäna\\|afsana\\|fasäna\" HRN.txt | head -20"
}
```


### [2026-09-06T16:12:57.414Z] TOOL RESULT

```
=== afs ===
10026:4. afsTultan Vernichten; abnehmen', awsiuitan, afstn-
```


## [2026-09-06T16:13:02.726Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; grep -n \"سخن\\|افسانه\" ARY_pages.txt | head -20"
}
```


### [2026-09-06T16:13:02.779Z] TOOL RESULT

```
386:مردم جهان به زبان عبری سخن می‌گفتند ولی از آن پس زبانهای مختلف (که در واقع نوعی تنیه ‏
634:نظر شمار سخنگویان (بیش از یک میلیارد نفر) بزرگترین خانواده‌ی زبان‌های هند و اروپایی
731:سخنگویان به این زبان‌ها پیش از ۱۳۰ میلیون نفر است.
749:آثار فلسفی و تاریخ ی گوناگون. زبان یونانیکلاسیکه به ندریج تبدیل به یونانی نوین شد. سخنگویان
765:مرکزی و بخشی از امریکای شمالی بردند. امروزه شمار سخنگویان این زبان‌ها به حدود ۹۰۰ میلیون
783:۰ میلیون نفر به آن سخن می‌گویند و زبان رسمی چندین کشور دیگر و زبان بین‌المللی جهان
840:صربی» کرواتی» مقدونی). جمع سخنگویان به این زبان‌ها حدود ۴۵۰ میلیون نفر است.
863:شش میلیون نفر به این دو زبان سخن می‌گویند.
871:زبان سخن می‌گویند.
1108:خط نویسی» افسانه‌ها و تاریخ مردم خود را در حافظه‌ی خود جا داده و در بزم‌ها یا مراسم رسمی با
1334:۵ توضیحات افسانه مانند درباره‌ی ریشه‌ی واژه‌ها را باید با شک و تردید فراوان مورد
1873:فرهنگ بزرگ سخن: ۱7۱
10449:۱ واژه‌ی فارسی "پاسخ" از واجربشه‌های "پاد" و "سخن" تشکیل شده است» (پهلری آن: ۳۸880 ,(۳80
11619:۳ چم این واژه در زبان‌های رومانس و ژرمنی: سخن» واژه گفتار,
14045:چم این واژه در زبان یونانی: سخن؛ حرف
16172:فرهنگ بزرگ‌سخن به سزپزتی دکتز نخس انوری. نهران: انتشاران سخن» ۱۳۸۱
```


## [2026-09-06T16:13:03.170Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Zauber\\|Erzählung\\|Erzahlung\" HRN.txt | head -20"
}
```


### [2026-09-06T16:13:03.220Z] TOOL RESULT

```
3856:410. JädU 'Zauberer, Jadül.
3857:aw. j/ätu- 'Zauberer'; i^hlw. jatuk, jatükih, arm. LW.
5117:schichte, Erzählung .
5589:^) von Staokelberg, Fünf ossetische Erzählungen, 83 ver-
10715:Tomaschek stellt wa;^. mutr 'Zauberspruch' dazu;
```


## [2026-09-06T16:13:06.297Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '5110,5125p' HRN.txt; echo \"=== ARY line 10449 context ===\"; sed -n '10440,10460p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-06T16:13:06.355Z] TOOL RESULT

```
Vorschrift'.
') (^Iml.l. LW. pppi, arm. LW. (htsfnk.- 127 -
ap. "^dastabara-; phlv. dastwar, dastbar.
Nicht zu dest *Hand\ sondern zu der in aw. dqsfva-
etc. steckenden Wurzel dmts- (Darmestetor, Et. ir.
I, 115 Note)'). Zu derselben Wurzel stellt Nöldeke
(mündliche Mitteilung) auch np. dästan-), destan *Go-
schichte, Erzählung .
5()9. duH^^är, duSvär 'schwierig*, dus/'ün, dusvan,
aw. vergl. duzadra- (Geldner, KZ. 25, 478, Studien
I, 17 folgg.); phlv. dus/J'är, dmx'arlh.
Die neup. phlv. Formen sind Neubildungen aus
dus+x"^'^ (No. 49G).
570. destän 'menstruirende Frau'.
aw. da/stavaitl-; phlv. dastän (arm. LW. dasfan;
chald. LW. ]P\'^'^)j dastan(i)stan^ vorgl. dayßak,
=== ARY line 10449 context ===
انگلیسی (5ل870): هی 397 ین
دانمارکی (0۸0/184): 508 1 (8۸) ی مین اس
سوئدی (31720/50): ۵6۸ 9 (0188) ما۸5
ملدی (ثن۵07: 2860680 ,8860801 4 (8۳8503) ات دی هم
اسلاری کهن (۲10با5 )نان 0ا0): ناش تلا
1 هن 2 (8۸9) :0/05
لهستانی (۳03): ه6ا050 6 (8۸9) 37
روسی (551۸1): هد برهان قاطع : 11:۶
یادداشت: :
۱ واژه‌ی فارسی "پاسخ" از واجربشه‌های "پاد" و "سخن" تشکیل شده است» (پهلری آن: ۳۸880 ,(۳80
کردی: 315881۷ ارمنی:۳۸7۸87۸۷1).
۲- چم این واژه در لانین: به ترتیب گفتن.
۳- 03110188 معتقد است که واژه‌های این فهرست با واژه‌های ایرانی - هندی این فهرست رابطه‌ای ندارد. سایر
۱ پسگشت‌ها هم واژه‌های ایرانی - هندی این فهرست را مورد بررسی قرار نداده‌اند» لذا جلو واجریشه‌ی هند و اروپایی
(شاید) آورده‌ام.
دا ۹ 8
اوستایی (۸887/04): -لف 5۸ بلورچی (/للاءل8۸): 3
پهلری (1/شاللم): 3 افغانی (پشتو) (/470[2): 3
اوستی (0598712): 3 سانسکر یت (7ل54(/۶8۶): 21313۸8 ,518۸۹
کردی (00820/37): 82806 ب587 بال8۸ ارمنی (0/8011۸7): 3
[pdf page 353]
```


## [2026-09-06T16:13:10.860Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; sed -n '10400,10450p' ARY_pages.txt"
}
```


### [2026-09-06T16:13:10.899Z] TOOL RESULT

```
۲ چم این واژه در زبان لاتین؛ قلم حکاکی,
[pdf page 351]
۲ سخت_
| بمانکلیس سرواژی تال سر را ۵80
اوستایی (/488742): 7 انگلیسی (874الا8/0): 1 ست۲ ات
پهلوی (1/اتلمط): ۰ 5.7 دانمارکی (0۸7/8[7): ۱۱4
بلرچی (الللاملم8): 7 و85۸6 سرئدی (81/50197): 11۸6۸
تخاری 4 (۸ ۷مل701۸7): ۰ 2881۸87 ایرلندی کهن (لل5لا صا0): 7
تخاری 8 (8 /(4ل700۸7): ۰ 1۸۱/۸۲
سانسکریت (8۸4(/38807): پسگشت‌ها 5
۸ 8۸007 2 م۶0
ایسلندی کهن (0104714/(ی3 ضا0): 8 (11۸101) امین ان
۱ 3 7 (۸30]) :102/22
آلمانی سیانه (//0580 بز0ا قاططا/م: 0 (اکتهتم :005
11۸6 3 (۸701ت) +57
آلمانی (052/0/۸(۷): نود کر ۱ برهان قاطع + ۱۱:۰۶ .
انگلیسی کهن 8070/5/0 ۰:00 11۸6۸91
یادداشت:
۱- ۳01۳030۷9 واژه‌های ژرمنی ان فهرست را با دیگر واژه‌های این فهرست همريشه می‌داند ولی 0717088 و
7 و 87612۸1 ریشه‌ی واژه‌های ژرمنی را ناشناخته می‌دانند.
۲ چم این واژه در زبان‌های ژرمنی: روی تخم خوابیدن؛ به وجرد آوردن,
چم این واژه در زبان سانسکریت: توانستن» قدرت داشتن,. ا
۳ واژه‌ی انگلیسی 11۸30 (انگلیسی کهن: 38۸52 آلمانی: 11۸/87 از ریشه‌ی هند و اروپابی 1۳۸1*) آمده‌اند
00531 0
آوستایی (1ل48874): 5۸ هت
پارسی باستان (/۲8۸51۸ 010): -507 ,+8۸36 ارمنی (/(4۷48714): 4 بلاق
پهلری (1اماتنهم): 8070۸81 ,5۸3۷۷۸8۷ بونانی (072274): اد ون دون دا
سانسکریت. (5(/38/7): لاتین (/710ل): اد اراد نا
۳۳۳
[pdf page 352]
تمه
ا . ست
ایسلندی کهن (۵ 901۸۷۷ صا0): لینوانی (4] هنال 7/):
. لد نم تآهلد5 ,ت52 ,5۸۳1
ساکسونی کهن (540/0 010): 88001۸01 ایرلندی کهن (8/30/ ص01): 13
فریزی کهن (/۶7/540 صا0): ه502 گالی (4ل3/الام0): دا
آلمانی کهن ((087۸44 05 (ا0): ولزی (4اکا): 8 58 ,88
ردان آلبانی (الفاامفقتم: 70
آلمانی (44/۷ل052): 5
انگلیسی کهن (4ل5لق2:0 ص۰0 8800۸1 پسگشت‌ها اسرد
انگلیسی (5ل870): هی 397 ین
دانمارکی (0۸0/184): 508 1 (8۸) ی مین اس
سوئدی (31720/50): ۵6۸ 9 (0188) ما۸5
ملدی (ثن۵07: 2860680 ,8860801 4 (8۳8503) ات دی هم
اسلاری کهن (۲10با5 )نان 0ا0): ناش تلا
1 هن 2 (8۸9) :0/05
لهستانی (۳03): ه6ا050 6 (8۸9) 37
روسی (551۸1): هد برهان قاطع : 11:۶
یادداشت: :
۱ واژه‌ی فارسی "پاسخ" از واجربشه‌های "پاد" و "سخن" تشکیل شده است» (پهلری آن: ۳۸880 ,(۳80
کردی: 315881۷ ارمنی:۳۸7۸87۸۷1).
```


## [2026-09-06T16:13:25.094Z] TOOL CALL #32: Bash

```json
{
 "command": "ls site/pages/255.jpg 2>/dev/null; pdftoppm -f 255 -l 255 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg255 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T16:13:27.337Z] TOOL RESULT

```
site/pages/255.jpg
total 10644
drwx------ 7 sfmqrb sfmqrb    4096 Sep  6 12:13 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    1166 Sep  6 12:13 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  180887 Sep  6 11:56 bqt1637_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50592 Sep  6 11:56 bqt1637_kaz.png
-rw-rw-r-- 1 sfmqrb sfmqrb  181961 Sep  6 12:11 bqt1688_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  340758 Sep  6 12:11 bqt1709_fn2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  280452 Sep  6 12:11 bqt1709_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67391 Sep  6 11:49 build225.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71757 Sep  6 11:47 build232.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49952 Sep  6 11:57 build234b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   32265 Sep  6 11:51 build234.py
-rw-rw-r-- 1 sfmqrb sfmqrb   24770 Sep  6 12:01 build243.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  6 11:28 c224_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3203 Sep  6 11:28 c224_n7.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:27 c229_bibua.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5308 Sep  6 11:27 c229_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5313 Sep  6 11:27 c229_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9059 Sep  6 11:50 c237_n18.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2389 Sep  6 11:50 c237_n3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4987 Sep  6 11:52 c239_kandid2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4734 Sep  6 11:52 c239_kandid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12852 Sep  6 11:52 c239_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4087 Sep  6 11:52 c239_sandarus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   15240 Sep  6 11:54 c246_caiique.png
-rw-rw-r-- 1 sfmqrb sfmqrb   36354 Sep  6 12:02 c246_casaque.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84366 Sep  6 11:54 c246_n2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51690 Sep  6 11:54 c246_n6.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13719 Sep  6 12:02 c248_p3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   30759 Sep  6 12:02 c248_p4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2750 Sep  6 12:02 c248_persian2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3046 Sep  6 12:02 c248_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12347 Sep  6 11:20 c_hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12691 Sep  6 11:20 c_ieuo.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2071 Sep  6 11:26 c_ijlak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14654 Sep  6 11:20 c_ijlak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12239 Sep  6 11:20 c_latis.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169482 Sep  6 11:58 crop_1648b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45260 Sep  6 11:57 crop_1648.png
-rw-rw-r-- 1 sfmqrb sfmqrb  305924 Sep  6 11:57 crop_1731.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb  111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb     724 Sep  6 12:11 drive.py
-rw-rw-r-- 1 sfmqrb sfmqrb   83691 Sep  6 11:19 gen215.py
-rw-rw-r-- 1 sfmqrb sfmqrb    2303 Sep  6 11:25 j.json
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb   77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67513 Sep  6 11:27 mk217.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74459 Sep  6 11:33 mk218b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17605 Sep  6 11:25 mk218.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50138 Sep  6 11:24 mk222.py
-rw-rw-r-- 1 sfmqrb sfmqrb   78297 Sep  6 11:32 mk223.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47928 Sep  6 11:38 mk224.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53093 Sep  6 11:40 mk226.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51303 Sep  6 11:39 mk228.py
-rw-rw-r-- 1 sfmqrb sfmqrb   29152 Sep  6 11:37 mk229.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47535 Sep  6 11:47 mk230.py
-rw-rw-r-- 1 sfmqrb sfmqrb   64267 Sep  6 11:59 mk235.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73422 Sep  6 12:02 mk237.py
-rw-rw-r-- 1 sfmqrb sfmqrb   81037 Sep  6 12:03 mk240.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80347 Sep  6 12:08 mk242.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58802 Sep  6 12:07 mk244.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:52 p233
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 p245
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 p249
-rw-rw-r-- 1 sfmqrb sfmqrb   33321 Sep  6 11:51 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   30335 Sep  6 12:07 part2.py
-rw-rw-r-- 1 sfmqrb sfmqrb   38036 Sep  6 12:11 part3.py
-rw-rw-r-- 1 sfmqrb sfmqrb   54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb  141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb  194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb  147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71937 Sep  6 11:19 pg219.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb  118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb   90848 Sep  6 11:22 pg224hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55412 Sep  6 11:15 pg224.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80963 Sep  6 11:32 pg225.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161218 Sep  6 11:26 pg226hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74322 Sep  6 11:19 pg226.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54381 Sep  6 11:31 pg227.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52519 Sep  6 11:25 pg228.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78760 Sep  6 11:27 pg229hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42112 Sep  6 11:26 pg229.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65310 Sep  6 11:32 pg230.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69894 Sep  6 11:34 pg231.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67111 Sep  6 11:35 pg233.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82071 Sep  6 11:44 pg234.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47149 Sep  6 11:44 pg236.png
-rw-rw-r-- 1 sfmqrb sfmqrb  125593 Sep  6 11:50 pg237hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67972 Sep  6 11:50 pg237.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168221 Sep  6 11:52 pg239hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81026 Sep  6 12:03 pg239.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83594 Sep  6 12:03 pg239_small.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81131 Sep  6 11:51 pg240.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97613 Sep  6 11:49 pg242.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80947 Sep  6 11:59 pg244.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80632 Sep  6 11:55 pg245.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79253 Sep  6 11:54 pg246.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64208 Sep  6 12:04 pg247.png
-rw-rw-r-- 1 sfmqrb sfmqrb  142780 Sep  6 12:02 pg248hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49887 Sep  6 12:02 pg248.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82530 Sep  6 12:05 pg249.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89076 Sep  6 12:13 pg250.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75263 Sep  6 12:04 pg251.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74772 Sep  6 12:13 pg252.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55906 Sep  6 12:13 pg255.png
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 __pycache__
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   53545 Sep  6 12:03 w241.py
```


## [2026-09-06T16:13:30.246Z] TOOL CALL #33: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg255.png"
}
```


### [2026-09-06T16:13:30.594Z] TOOL RESULT

```

```


## [2026-09-06T16:13:30.588Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T16:13:43.400Z] TOOL CALL #34: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg255.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/255.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/255.png"
}
```


### [2026-09-06T16:13:43.457Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 55906 Sep  6 12:13 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/255.png
```


## [2026-09-06T16:13:43.870Z] TOOL CALL #35: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T16:13:43.877Z] TOOL RESULT

```


```


## [2026-09-06T16:13:47.149Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%AE%D9%86",
 "prompt": "Give the full Persian etymology section for سخن (soxan): Middle Persian form, Proto-Iranian reconstruction, Avestan/Old Persian cognates, and any cited authorities."
}
```


## [2026-09-06T16:13:49.295Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D8%A7%D9%86%D9%87",
 "prompt": "Give the full Persian etymology of افسانه (afsāne) 'fable, tale': Middle Persian form, root, prefix, cognates, and cited authorities."
}
```


### [2026-09-06T16:13:53.642Z] TOOL RESULT

```
# Persian Etymology for سخن (soxan)

Based on the Wiktionary entry, here is the available etymological information:

**Proto-Iranian Source:**
The word ultimately derives from Proto-Iranian *cánhati, according to the etymology section.

**Cognates:**
The entry identifies several related words across Indo-European languages:
- Sanskrit शंसति (śáṃsati, "to declare")
- Latin cēnseō
- Ancient Greek κῶμος (kômos)

**Note on Middle Persian:**
The entry does not provide a specific Middle Persian form or intermediate stage in the etymological development. There is no mention of Avestan or Old Persian cognates in the available content.

The Persian section carries a cleanup notice, with an editor noting: "ultimately from X, but see there for more," suggesting the etymology section may be incomplete or require refinement regarding the specific historical progression from Proto-Iranian to Modern Persian.
```


### [2026-09-06T16:13:56.448Z] TOOL RESULT

```
# Persian Etymology of افسانه (afsāne)

**Middle Persian Form:**
Inherited from Middle Persian [Inscriptional Pahlavi needed] (ʾfsʾnk /⁠afsānag⁠/, "fable").

**Root and Prefix:**
The etymology is incomplete according to the source, but scholars propose it may be "a prefixed derivative of Proto-Indo-European *ḱens- ('to proclaim'). Or maybe *ḱen- ('empty'), as found in Ancient Greek κενός (kenós, 'empty')."

**Cognates:**
The word shares connections with Ancient Greek κενός (kenós), meaning "empty," suggesting a possible semantic development from "emptiness" to "tale spun from emptiness."

**Cited Authority:**
Durkin-Meisterernst, Desmond (2004) provides a dictionary entry for the Middle Persian form in *A Dictionary of Manichaean Middle Persian and Parthian*.

The source notes the etymology requires further development and invites additional contributions.
```


## [2026-09-06T16:14:01.443Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cosmos",
 "prompt": "Give the full etymology of cosmos, and any statement about the origin of Greek kosmos (whether it is of unknown/uncertain origin)."
}
```


## [2026-09-06T16:14:02.153Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/censor",
 "prompt": "Give the full etymology of censor and census: Latin censere, PIE root, and any related forms (Sanskrit, Avestan, Old Persian)."
}
```


### [2026-09-06T16:14:07.886Z] TOOL RESULT

```
# Etymology of Cosmos

## Full Etymology

The word **cosmos** entered English around 1200 from the Latinized form of Greek *kosmos*, meaning "order, good order, orderly arrangement." The term gained popular usage in 1848 when translating Humboldt's *Kosmos* from German.

The Greek root *kosmos* derived from the verb *kosmein*, which meant "to dispose, prepare," with specialized senses including "to order and arrange (troops for battle)" and "to deck, adorn, equip, dress." This gave *kosmos* a secondary meaning of "ornaments of a woman's dress, decoration," alongside its primary sense of "the universe."

Pythagoras reportedly first applied this word to the universe, possibly originally referring to "the starry firmament," which was later extended to encompass the entire physical world. The word "often suggested especially 'the universe as an embodiment of order and harmony.'"

## Origin of Greek Kosmos

The document provides **no information about the ultimate origin or etymology of the Greek word *kosmos* itself**. It traces the word's meanings and uses but does not indicate whether Greek *kosmos* is of known, uncertain, or unknown origin.
```


### [2026-09-06T16:14:09.813Z] TOOL RESULT

```
# Etymology of Censor and Census

**Censor (noun, 1530s):**
From French and Latin *censor*, derived from Latin *censere* meaning "to appraise, value, judge." The word originally referred to "Roman magistrate of 5c. B.C.E. who took censuses and oversaw public manners and morals." By the 1640s, it acquired the meaning of "official empowered to examine books, plays (later films, etc.)."

**Census (noun, 1610s):**
From Latin *census*, "the enrollment of the names and property assessments of all Roman citizens," originally the past participle of *censere*.

**Proto-Indo-European Root:**
Both terms trace to the PIE root *\*kens-* meaning "speak solemnly, proclaim."

**Related Indo-European Forms:**
The etymology notes Sanskrit cognates: *amsati* ("recites, praises") and *asa* ("song of praise"), demonstrating the root's connection to formal utterance and judgment across ancient languages.

**Related English Forms:**
*Censorious*, *censorship*, *censure*, and *censorable* all derive from this etymological family.
```


## [2026-09-06T16:14:15.252Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%CF%8C%CF%83%CE%BC%CE%BF%CF%82",
 "prompt": "Give the Ancient Greek etymology section for κόσμος: what origin is given, is it called unknown/uncertain, is Beekes or Chantraine cited, and is any connection to PIE *ḱens- mentioned?"
}
```


## [2026-09-06T16:14:16.818Z] TOOL CALL #41: WebSearch

```json
{
 "query": "ریشه واژه ماتیک فارسی فرانسه cosmétique"
}
```


### [2026-09-06T16:14:20.435Z] TOOL RESULT

```
# Ancient Greek Etymology of κόσμος

**Origin:** The word derives from Proto-Hellenic *kónsmos, which came from Proto-Indo-European *ḱónsmos, ultimately from *ḱens- ("to announce, put in order").

**Certainty:** The origin is **not** marked as unknown or uncertain. It presents a clear etymological path.

**Scholarly citations:** **Beekes is cited.** Robert S. P. Beekes' *Etymological Dictionary of Greek* (2010) is referenced in the References section as the source for this etymology.

**PIE connection:** Yes, the connection to PIE *ḱens- is explicitly mentioned. The entry states the word comes "from Proto-Indo-European *ḱónsmos, from *ḱens-" and notes related cognates in Latin (cēnseō) and Sanskrit (śaṃsati).
```


### [2026-09-06T16:14:28.636Z] TOOL RESULT

```
Web search results for query: "ریشه واژه ماتیک فارسی فرانسه cosmétique"

Links: [{"title":"فهرست وام‌واژه‌های فرانسوی در فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D9%88%D8%A7%D9%85%E2%80%8C%D9%88%D8%A7%DA%98%D9%87%E2%80%8C%D9%87%D8%A7%DB%8C_%D9%81%D8%B1%D8%A7%D9%86%D8%B3%D9%88%DB%8C_%D8%AF%D8%B1_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"پیوست:فهرست وام‌واژه‌های فرانسوی در فارسی - ویکی‌واژه","url":"https://fa.wiktionary.org/wiki/%D9%BE%DB%8C%D9%88%D8%B3%D8%AA:%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D9%88%D8%A7%D9%85%E2%80%8C%D9%88%D8%A7%DA%98%D9%87%E2%80%8C%D9%87%D8%A7%DB%8C_%D9%81%D8%B1%D8%A7%D9%86%D8%B3%D9%88%DB%8C_%D8%AF%D8%B1_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"معنی ماتیک در فرهنگ معین | جدول یاب","url":"https://www.jadvalyab.ir/moein/%D9%85%D8%A7%D8%AA%DB%8C%DA%A9"},{"title":"1000 لغت مشترک فرانسوی در زبان فارسی - آکادمی روان","url":"https://www.ravaan.co/%D9%91french-words-in-persian/"},{"title":"کلمات فرانسوی در فارسی: چند کلمه فرانسوی در زبان فارسی وجود دارد؟ - مجله زبان فریدلینگو","url":"https://faridlingo.ir/french-words-in-persian/"},{"title":"واژه های مشترک بین زبان فرانسه و فارسی","url":"https://www.parsine.com/fa/news/259204/%D9%88%D8%A7%DA%98%D9%87-%D9%87%D8%A7%DB%8C-%D9%85%D8%B4%D8%AA%D8%B1%DA%A9-%D8%A8%DB%8C%D9%86-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%B1%D8%A7%D9%86%D8%B3%D9%87-%D9%88-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"واژه های مشترک بین زبان فرانسه و فارسی - Elmineh.ir - علمینه","url":"https://elmineh.ir/%D9%88%D8%A7%DA%98%D9%87-%D9%87%D8%A7%DB%8C-%D9%85%D8%B4%D8%AA%D8%B1%DA%A9-%D8%A8%DB%8C%D9%86-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%B1%D8%A7%D9%86%D8%B3%D9%87-%D9%88-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C/"}]

بر اساس نتایج جستجو، معلومات مربوط به ریشه واژه "ماتیک" به شرح زیر است:

واژه "ماتیک" از فرانسوی گرفته شده است و مخفف از کلمه "کسمتیک" (Cosmétique) فرانسوی است. کلمه کُسمِتیک فرانسوی که از کُسمِتیکُوس یونانی گرفته شده است، به داروهایی اطلاق می‌گردد که برای طراوت و زیبایی و محافظت پوست بدن و صورت و گیسوان به کار برده می‌شود.

در زبان فارسی، ماتیک به معنی ماده‌ی سرخ که زنان به لب می‌مالند می‌باشد.

پس خلاصه‌ای از ریشه‌شناسی این واژه به این صورت است:
- **کلمه یونانی**: کُسمِتیکُوس
- **کلمه فرانسوی**: Cosmétique
- **کلمه فارسی**: ماتیک (مختصر و عامی از Cosmétique)


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T16:14:36.469Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1ens-",
 "prompt": "Give the full content: the root's meaning, its derived terms and descendants by branch (Indo-Iranian, Italic, Albanian, Greek, Tocharian), and whether Greek kosmos is listed."
}
```


## [2026-09-06T16:14:38.050Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.jadvalyab.ir/moein/%D9%85%D8%A7%D8%AA%DB%8C%DA%A9",
 "prompt": "What does Mo'in's dictionary say for ماتیک — the origin tag and the definition?"
}
```


### [2026-09-06T16:14:44.834Z] TOOL RESULT

```
# Proto-Indo-European Root *ḱens-

## Root Meaning
The root *ḱens- has two primary meanings: 1) "to announce, to proclaim" and 2) "to put in order."

## Derived Terms by Branch

**Indo-Iranian:**
- Proto-Indo-Aryan: *śánsati → Sanskrit śáṃsati (शंसति)
- Proto-Iranian: *cánhati (with further descendants listed)

**Italic:**
- Latin: cēnseō, derived from *ḱn̥s-éh₁-ye-ti

**Greek:**
- Ancient Greek: κόσμος (kósmos, meaning "order/world"), derived from *ḱóns-mo-
- Ancient Greek: κῶμος (kômos), possibly from *ḱómso-

**Albanian:**
- them, with uncertain derivation (possibly from this root or from *ḱeh₁s-)

**Germanic:**
- Proto-Germanic: *hazjaną

## Descendants by Branch

The entry lists Sanskrit śaṃs under descendants. The Greek word kosmos (κόσμος) is definitively listed as deriving from the *ḱóns-mo- formation of this root.
```


### [2026-09-06T16:14:46.058Z] TOOL RESULT

```
# Mo'in's Dictionary Entry for ماتیک

**Origin tag:** "[فر.]" (French)

**Definition:** "از انواع لوازم آرایش که با آن لب ها را رنگ کنند، روژ لب" — a category of cosmetic products used to color lips, specifically lip rouge.
```


## [2026-09-06T16:14:53.388Z] TOOL CALL #44: WebSearch

```json
{
 "query": "Beekes Etymological Dictionary of Greek κόσμος \"no etymology\" kosmos origin unknown"
}
```


## [2026-09-06T16:14:55.878Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D8%A7%D8%AA%DB%8C%DA%A9/",
 "prompt": "What do the Persian dictionaries (Dehkhoda, Mo'in, Farhang-e Emrooz, فرهنگ فارسی عمید) say about ماتیک — especially its origin/etymology (from which French word)?"
}
```


### [2026-09-06T16:15:00.059Z] TOOL RESULT

```
Web search results for query: "Beekes Etymological Dictionary of Greek κόσμος "no etymology" kosmos origin unknown"

Links: [{"title":"Beekes Etymological Dictionary Greek","url":"https://www.scribd.com/document/698401131/Beekes-Etymological-Dictionary-Greek"},{"title":"κόσμος - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%CE%BA%CF%8C%CF%83%CE%BC%CE%BF%CF%82"},{"title":"Beekes - Etymological Dictionary of Greek | PDF","url":"https://www.scribd.com/document/371380654/Beekes-Etymological-Dictionary-of-Greek"},{"title":"Robert S. P. Beekes","url":"https://en.wikipedia.org/wiki/Robert_S._P._Beekes"},{"title":"Etymological Dictionary of Greek - Beekes, Robert.pdf","url":"https://isidore.co/CalibreLibrary/Beekes,%20Robert/Etymological%20Dictionary%20of%20Greek%20(5821)/Etymological%20Dictionary%20of%20Greek%20-%20Beekes,%20Robert.pdf"},{"title":"Beekes' Etymological Dictionary of Greek - Learning Greek - Textkit Greek and Latin","url":"https://www.textkit.com/t/beekes-etymological-dictionary-of-greek/15376"},{"title":"Beekes’ (2010) Etymological Dictionary of Greek","url":"https://koine-greek.com/2017/04/23/beekes-2010-etymological-dictionary-of-greek/"},{"title":"κόσμος | Definition of κόσμος at Definify","url":"https://www.definify.com/word/%CE%BA%CF%8C%CF%83%CE%BC%CE%BF%CF%82"}]

Based on the search results, I found references to Beekes' Etymological Dictionary of Greek, though the search results don't directly show the specific entry for κόσμος (kosmos) stating "no etymology" or "origin unknown." 

The search results confirm that Beekes' Etymological Dictionary of Greek was published in 2010 by Brill with the assistance of Lucien van Beek, and the Wiktionary entry cites Beekes pages 759-760 for the κόσμος entry.

However, the search results show some conflicting information about the etymology: one source suggests a connection to Proto-Indo-European roots, while the overall approach of Beekes' dictionary involves identifying words of Pre-Greek origin to illustrate the flaws in the traditional approach that practically every word has an Indo-European etymology.

To get the exact wording from Beekes regarding κόσμος, you would need to consult the dictionary directly at pages 759-760, as the search results don't contain the full text of that specific entry.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-06T16:15:02.413Z] TOOL RESULT

```
# Etymology of ماتیک According to Persian Dictionaries

Based on the Abadis dictionary content, here's what the Persian lexicographic sources state:

**Dehkhoda Dictionary** provides the most detailed etymological information, stating that ماتیک is "from French, abbreviated from French cosmétique," and traces it further back to the Greek κοσμητικός (kosmetikos), which refers to substances used for beauty and skin care.

**Mo'in Dictionary** offers a simpler characterization: "from French, a type of cosmetic product used to color lips; lip rouge."

**Farhang-e Emrooz** similarly describes it as "from French," classifying it among cosmetic tools for lip coloring.

**Farhang-e Emrooz (Amid)** presents it as a colored substance made from chemicals for lip coloring, without explicitly discussing its French origin in the excerpt provided.

All dictionaries agree on the word's French source and its function as a lip cosmetic, though Dehkhoda uniquely traces the etymological chain back to Greek origins through the French intermediary.
```


## [2026-09-06T16:15:14.567Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/indoeurop.html#kens-",
 "prompt": "Find the entries for the roots kens- and kes-3 (kes3). Quote them exactly: what English words are derived from each, and under which root is Greek kosmos placed?"
}
```


## [2026-09-06T16:15:16.003Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D8%A7%D9%86%D8%B3%D9%88%D8%B1/",
 "prompt": "What do Dehkhoda / Mo'in / Amid say about سانسور — its origin (which French word) and meaning?"
}
```


### [2026-09-06T16:15:20.122Z] TOOL RESULT

```
I cannot locate the entries for **kens-** or **kes-3** in the provided text. The content appears to be truncated mid-document, ending in the middle of the **bheuə-** entry. The document indicates "[Content truncated due to length...]" at the conclusion.

To answer your question about these roots and the placement of Greek *kosmos*, I would need access to the complete appendix sections covering the K entries, which are not fully included in the provided excerpt.
```


### [2026-09-06T16:15:22.081Z] TOOL RESULT

```
# سانسور: Etymology and Definitions

**Origin:** The word سانسور derives from French (censure/censorship).

**Dehkhoda Dictionary** defines it as: "ممیزی و تفتیش مطبوعات و مکاتیب و نمایشها" (inspection and examination of publications, correspondence, and performances).

**Mo'in Dictionary** characterizes it as: "کنترل و بازرسی حاکمیت بر فعالیت سیاسی، اجتماعی و... خاصه فرهنگی" (governmental control and inspection of political, social, and especially cultural activities).

**Amid Dictionary** describes it as state supervision over films, plays, newspapers, and publications, involving deletion of certain content before publication according to official discretion.

All three sources consistently identify سانسور as a form of governmental oversight involving examination and removal of content deemed inappropriate.
```


## [2026-09-06T16:15:27.362Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} NR==412 || NR==413' WLD_Bd1_pages.txt | head -60"
}
```


### [2026-09-06T16:15:29.067Z] TOOL RESULT

```
                                                                   kens-   — ker-                                         403

  Uber arm. kotor „Bruchstiick“ (Bugge KZ. 32, 49) s. vielmehr Pedersen
KZ. 39, 380.
                    2
                                —
                 Da arm. kotor auch „Streit“ bedeutet, dachte Zupitza
Gutt. 103 unter                     Annahme                eines Bedeutungsverbaltnisses wie zwischen gr.
Ijaxog       „Lumpen“,             /Igaxog
                                           (j-Q-)’ ifianov Jiokviekeg ai. vrkna- „abgehauen,  :


                                              u
gespalten“              :   as, wroht „Streit , unwahrscheinlich an Yerwandtschaft auch
rait aksl.kotora „Streit, Kampf“, mhd. hader „Zank, Streit, Hader**, wozu
(trotz Fick III 4 69) ahd. hadti-, ags heafro-, anord. hqd- „Kampf“, gall.
Cutu-riges air. cath „Kampf** (s. kat- „Kampf“), fur die aber eine Gd.-
                    ,


Bed. „spalten, rei6en“ ganzlich unerweislich ist.                                       — Auch mit kent- „stechen“
;Prellwitz 216) nicht zu vereinigen.


kens- „feierlich sprechen, autoritativ verkiindigen“.
   Ai. gamsayati „IaBt aufsagen, kiindet an“ (= lat. rmseo), cawsati „rezi-
tiert, sagt auf, lobt“, gasti- „Lob“, gasman- n. „Lob,       Preis“, av. sqh-
(sawhaUi usw., s. Bartholomae Airan. Wb. 1 5 7 S f.) „pronuntiare“, sasti-
„Wort, Yorschrift", ap. ftathj oder danh atiy „spricht, verkiindigt“ ; lat. cen-
seo -ere „begutachten, schatzen**, osk. censamur „censetor“, censaum „cen-
      ,


sere“, keenzstur lat. censor (: ai. gainstar- „der da rezitiert“), an-censto
                                    :



„non censa“:lat. census (ai. gastd- „gesprochen, gepriesen“); alb. from „ich
sage“ (*k ensmi G. Meyer Alb. Wb. 91, Pedersen KZ. 36, 332, Jokl IF.
                                ;


37, 101); abg. sgtz „inquit“                                    (Brugmann IF. 1, 177).
      In der Bed. kaum vereinbar ist gr. xoajuog „Ordnung, ordentliche Ein-
richtung, Anstand; Schmuck, Zier“ (ware *xoro-/uog), Froehde KZ. 33, 311,
Zupitza Gutt. 109, Brugmann Distrib. 19; letzterer versucht IF. 28, 358 f.
Anknupfung vielmehr an q'irep -, q*er- „machen, corpus * (ai. kalp- „ordnen“?)                        1




unter q'ior^^smo-, was mich nicht iiberzeugt (allenfalls eher als *xop.jiop6g
zu xopipog, lit. svankns , s. kuenq    „hiibsch“, ibd. 360 Anm 2; oder zu
apr. kanxtin s. u.?)        ,
                                            —
                           Nir. caint „Rede, Sprache * (Fick II 4 69; Loth
                                                                                                  1
```


## [2026-09-06T16:15:47.814Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.m.wiktionary.org/wiki/%CE%BA%CF%8C%CF%83%CE%BC%CE%BF%CF%82",
 "prompt": "Quote VERBATIM the Ancient Greek \"Etymology\" paragraph of this page, word for word, including any hedging words like \"possibly\", \"uncertain\", \"unknown\", and any footnote/reference text."
}
```


## [2026-09-06T16:15:49.104Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"1578\\|1579\\|pronuntiare\" BRT.txt | head -20"
}
```


### [2026-09-06T16:15:49.153Z] TOOL RESULT

```
26280:1578
26296:•  j.,  g.  sah'*,  p.  ö-ah-*'  V.  'pronuntiare'. Praes,  i  saA-^'^  :  sai-*\  3  sSngAa-,  sar»ha-, ^aka-  (=  Sj-)»,  7  iqsah-^\  27  (Pass.) %ahya-T>.  —  PPfP.  'sas'ta-;  Inf.  %aslanaiy, °sastayai-ca;  Absol.  'saahim.
26306:1579
28980:Sp.  928  o.)  ist  weggelassen:  danys.Hli (sd.)  ile  vTse  afrJnämi  yahmat  h°  imti zaoira  y.SS.i^;  \t.  S.  4'.  '  b)  bei NomiDa";  o)  bei  verbalen  Substantiven: raiis  i&i.;  'decessum')  rm  A^  ariha  ztmat vaähs  k^nnaoili  Vt.  17.  20;  —  spmtat  h" mainyaot  aisam  ahr^m  ('origo')  FrW. 70,40;  —  yä  h"  daSnayUt  .  ,  apastüilis ('abdicatio'j  ^.4J-  ß)  bei  Raumwörtera: dsräl  Cprocul')  A'  ahmiil  nmänät  .  .  ays i^yejä . .*yeyenH yeAhe ..  Y.57,  14;  14';  — nSii . .  *dräjyS  ('longius')  *'iyeillm  framraomi (sd.)  . .  ä/rllim  yUnat  -4'  .  .  P.  7j;  — nazdyS  ('propius')  ahmi  . .  yaia  änha  k' *gaosaHöya  P.  2  V;  28;  —  airime  gätüm hs nUhthaüta  . .  *psr3ntanm  (sd.;  'seorsum') h'  anyanbyS  mazdayasna^byS  V.g.  33;  29; —  aiai  dräjö  ('quantam  longitudinem')  h* i!^ral\.  3. 16;  16^;  — yS  hn%rS.masar»h3m iS/wamm  ('viam  miUe  passuum')  h'  vizibys paräiti  V.  JJ.  18;  —  äiat  ('quantum*)  h' mtiya^bya  Y.i).  10;  8f.';  —  avavat  ('tan- tum')  h'  paourt-aiibya  yäha  %rigilim  V. 1M39;  II,  76;  — yd  *yujyastxm  (sd.)  h' gat^abyS  parätti  'v.  7^.  17;  N.  8,  <??(?), V,_j.  17*,  J(5'.4*,  17. 4«,  b)  im  gÄw. a)  bei  Verben  (bei  solchen  der  Bewegung nicht  bezeugt):  frg  ma  sl/iJ  (Sp.  1575  o.) "iiwahmut  *vaoca^hl  *mainy}us  h'  'üwä Siaiihn  "..  pronuntiare  ex  tuo  , tuum  os"  Y.  28. 11;  —  ysi  gSus  h'  iyävtl (sd.)  "qui  a  bove  (habitant  sva.)  stant' Y.  J7.  a";  —  ka^ü  . .  zarjm  (sd.)  laränl h'  xsmap''  ",  .  impetrem  a  vobis  (sva. per  vos)"  Y.  44-17;  —  a^byS  mazdh  .  . xsäi^rät  A'  paifi.mraot  ". .  per  Regnum (deum)  respondit"  Y.ya.  2;  —  sonst mit  'asa-  A  (als  Gottheit)  im  Sinn  von 'peri^nim,  As'o  juvante  (u.  dgl.)':  aiät  h'
```


### [2026-09-06T16:15:49.829Z] TOOL RESULT

```
REDIRECT DETECTED: The URL redirects to a location that was not fetched automatically.

Original URL: https://en.m.wiktionary.org/wiki/%CE%BA%CF%8C%CF%83%CE%BC%CE%BF%CF%82
Redirect URL (from the server's Location header — server-supplied, not verified): https://en.wiktionary.org/wiki/%CE%BA%CF%8C%CF%83%CE%BC%CE%BF%CF%82
Status: 301 Moved Permanently

To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
- url: "https://en.wiktionary.org/wiki/%CE%BA%CF%8C%CF%83%CE%BC%CE%BF%CF%82"
- prompt: "Quote VERBATIM the Ancient Greek "Etymology" paragraph of this page, word for word, including any hedging words like "possibly", "uncertain", "unknown", and any footnote/reference text."
```


## [2026-09-06T16:15:56.633Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"saxvan\\|sax'van\\|saxx'an\\|sax^an\" BRT.txt | head -10; echo \"=== around 26280 ===\"; sed -n '26276,26300p' BRT.txt | cut -c1-600"
}
```


### [2026-09-06T16:15:56.693Z] TOOL RESULT

```
=== around 26280 ===
dby  Google
1577
sötStS-
8^-  i
1578
*'taÄi^^  Y.jö'.i;  —  ahurai  masdäi ..°t3m (statt  DS.)  vfnkrayne  fi-üdat^a^äi  Vr. i7. 1 ;  —  ttm  (näml.  mihtvm)  amixüanhm yazat)m  sBrim  damshu  °t>m  YtJO.  6;  13; —  sara  mihra..'ta  Yt  70.  31;  F./2; — tiÜrlm  ..yakmäi  ..fradä^at..lffs'firalsva °täi  YtÄ45;  43,  47;  — fravaslS . . spinta ..  spifüsth  ..  sürä  ..  'tu  Yt7j.75;  147, 31,  34;  —  vartuhi  °U  (VSf.)  andvl  süre ans/Ute  Yl.  5.  18,  130,  Ny.  /.  19;  Yt g,  4.  b)  sonst:  frataan  äps  */i  Yt. 13.  78.
KompE.  —  Superl.  zu  isüra-;  vgl.  Yt  r.  15, ro.  6,  31,  13.  75,  147.  —  ai-  iävif/ha-  Adj.  - Vgl,  säsfi/üta:  -Fi.:  sät  j^astSr»),  tri  (lu Yt.  /.  8] ;  dSmSa  räi  süt  J'Shtm ;  (lU  V.  33) : sültnänä,  erL:  sät  kunänd.  —  ')  NA,  sivtit'; s.  Var.  —  3)  Diese  Übersetzung  -  Sü. :  lä- bhepsuh,  läbkUihilifan  -  lässt  erkennen,  dass ntln  in  üf  nicht  das  Superlativsuffix,  sondern ein  Nomen  sah.  Der  Anlass  daiu  wird  Y, 55.  l :  *irvisiahc  . .  yt  rtä  iil5  gewesen  sein  : süf  J^ätl  ir  .  ,  ke  amäi  j^ästär
•  ).  sÖidii-  n.  'Waffe'  zum  Angriff:  (aj 'ois  tat  v?rf^rfm  dndimaidl  kyat  tumS huci^rsm  "das  machen  wir  zur  Waffe,  das zum  Angriff,  das  Gebet  . ."  Y.jÄ  i.
Ob  zum  V.  sa7d-  (BuKG  KZ.  3g.  363)?  Oder zu  lat.  eatd5>-)l  —  PQ.:  süt  (weil  man  saoiiil las;  s.  K4).  —  1)  Dessen  Zugehöriglteit  zu scindi  wegen  der  Bedeutung  doch  sehr  Icag-
•  j.  söinman-  n.  'Spalte':  yS  bar>sma *iao/ayeiii  (sd.)  dracs{sd.)  vä  paiti  'ma.. N.  100.
Zum  V.  jflÄ/.;  Bthl.IF.A2S3').  — Pü.:*ji;j^J* 'Loch'.  —  ")  Ich  nehme  jetzt  an,  <3ass  ir.  dm im  jAw.  «llgemein  m  nm  geworden  ist  (vgl, %  302.  2)  und  zwar  nach  der  Witkungsfrist des  Gesetzes  J  ^93-  !'»■  s.  sanman-.  ■*daii- mahi  läs^l  sich  als  Neubildung  nach  daiqaii usw.  fassen;  für  maimya-  kommt  der Einlluss von  ntaiitna-  in  Anschlag.  [Np.  Alma  ist jedenfalls  nicht  nach  GIrPh.  /  b.  92  ent- standen.]
•  j.  *saQha-''  m.  'Zahl'"':  '»ia  7.12. Zum  V.  säA:  —  ai.  Säsa-  m.  'Gebot'.  —  Pü. : matai.  —  i)  Hds.  vi',  aber  unter  den  Wör- tern für  s-,    —    =)    Bedeutung  nach  Pü.,   un-
•  j.  slnhaoha*  m.  EN,  eines  Gläubigen: bh>kahe  'nhahe  asaonö  "des  B.,  Sohns des  S.  ..'■  Yt./J,  124.
Eig.  'Gebieter',  Ableit.  aus  *iii»haA-  n.,   zum
V.  sah-,  vgl.  idsuf.  n.  'Befehl'.
j.  vTspayi  sqcalca  Y.  4.  a;  lies  vtspayisi  !t^C!i.
g.  s(is,  sifstä :  s.  'tand~
'}.  sqsaahqm:  s.  sqh-  mit  No.  S.
•  g.  s%3tr3i  Inf.  (absol.)  'es  zu  vollenden, die  Vollendung  (im  eschatologischen  Sinn) herbeizuführen*:  maiiys  ^ws  s°  v>r>fiE (Sp.  1361  m.)  ahurä  "dass  du  es  zu meinen  Gunsten  vollendeii  werdest,  darauf vertraue  ich,  o  Ah"  Y.46.3''.
Zum  V.  ^sand:  —  Vgl.  anu.s<iilräi.  —  Pü. : man  e  i  13  ämöxtisn  döstrn  bkrmazd.  —  ')  Vgl. zu  taxdyäi.
•  j.,  g.  sah'*,  p.  ö-ah-*'  V.  'pronuntiare'. Praes,  i  saA-^'^  :  sai-*\  3  sSngAa-,  sar»ha-, ^aka-  (=  Sj-)»,  7  iqsah-^\  27  (Pass.) %ahya-T>.  —  PPfP.  'sas'ta-;  Inf.  %aslanaiy, °sastayai-ca;  Absol.  'saahim.
Akt  I)  'verkünden,  kundtun,  bekannt geben';  i)  H  ohne  Obj.;  es  folgt  direkte Rede:  %3tiy  däray^vJ'u^  xfäyahiyt^: ima^  tyaf"  manä  kartam  babirami  Bh.^.  i ;
2  ff ,  7. 2  ff.,  2. 1  ff.,  3. 1  ff.,  5. 1  ff:,  D.  „^  2,
3,  5.2,  3,  ij,  77.3;  —  %ätiy  xsayariä xsäyd^iya/':    mäm  J'ur^mazdä  pätuo  X.
!-r,  3.  2.  3,  3.  3,  4-3,  7-  3;   —  ^^'y
```


## [2026-09-06T16:16:07.548Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### CHEUNG sanh\"; grep -n \"\\*sanH\\|sanh-\\|\\*canh\" CHEUNG.txt | head -10; echo \"### SKT censor/cosmos\"; grep -n \"^CENSURE\\|^CENSOR\\|^COSMOS\\|^COSMETIC\\|^CENSUS\" SKT.txt | head; echo \"### SYN word/speak\"; grep -n \"18.21 SPEAK\\|18.22 SAY\\|18.27 WORD\" SYN.txt | head"
}
```


### [2026-09-06T16:16:07.652Z] TOOL RESULT

```
### CHEUNG sanh
9158:*IE COGNATES: Hitt. /sanh-/ ‘to mean, to want, to search’, Gr. dvbo, буо, буор ‘I 
33716:songh-, sanh-, 334 
52179:/sanh-/, 128 
### SKT censor/cosmos
### SYN word/speak
31429:SING A Spout, CRY OuT 18.14 VaRrrous CRIES 18,21 SPEAK, TALK 18.22 Say 18,23 Be SILENT 18.24 LANGUAGE 18.25 DIALECT 18,26 WorD 18.27 DicTIONARY 18.28 NAME 18.31 Asx! (Question, Inquire) 18.32 ANSWER (vb.) 18.33 ApMiT, CONFESS 18.34 Deny 18.35 Asx?, REQUEST 18.36 Promise (vb.) 18.37 RerusE 18.38 Forbip
31563:vyocAL UTTERANCE, SPEECH; READING AND WRITING 1253 18.21 SPEAK, TALK Grk. deve (aor. enor, fut. Goth. rddjan, mapljan Lith. kalbéti ; toa, etc.), ayopebw, ON mala, reéa, tala Lett. rundat Nard Dan. tale, snakke ChSl. glagolati, vétali
31633:18.22 SAY
```


## [2026-09-06T16:16:10.790Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '31633,31660p' SYN.txt | cut -c1-1400; echo \"=== 18.26 WORD ===\"; awk 'NR>=31680 && NR<=31760' SYN.txt | grep -n -i \"suxan\\|18.26\\|18,26\" | head"
}
```


### [2026-09-06T16:16:12.666Z] TOOL RESULT

```
18.22 SAY
Grk. — Aéyw, dul, aor. elo, Goth. gisan
Lith.  sakytt, tart
fut. ta ON segja, kueda Lett. tetkt, sactt
NG equ, aor. elxa Dan. sige ChSl.  reStz, povédéte
Lat. — dicere Sw. sdga SCr. kazati, rect : sie iaee OE — cwepan, secgan Boh. fei, praviti, povédélt Fr. dire ME  saye, quethe Pol. —rzec, powiedziec
Sp. decir NE say Russ. skazat'
Rum. zice Du. —_zeggen Skt.  vac-, bri--, etc.
Ir. asbiur OHG quedan, sagen Ay. vak-, mril-, a0}- Nir. (a)deirim MHG sagen, queden OPers. dah-
W. dywedyd NHG sagen Br. lavarout
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
gu- -
Digitized by Arya Samaj Foundation Chennai and eGangotri
yocaAL UTTERANCE, SPEECH; READING AND WRITING 1257
For yerbs for ‘speak’ and ‘say’ in gen- 9], and those that cover both senses, erat)
18.21.  esides the usual verbs for ‘say’,
here ate often more isolated forms which are common in the parenthetical Pe before or after direct quotations, like Lat. inquit. These are not included in the list, but several are noticed in the discussion, where this use is conveniently shown by the rendering ‘inquit’ (some are restricted to the third person, others not). Cf. also such use of verbs for ‘do, make’ or ‘put’ (through ‘make a re- sponse’, etc.) as forms of It. fare, Fr. faire, NG xévw, Boh. diti, ete. Buck, op. cit. 134. Spitzer, “Romanisch facit ‘er sagt?”’, Stilstudien 1.223. Berneker 192. Here also Hitt. tezzi ‘says’, fr. dat-, le- ‘put’ (IE *dhé-, 12.12). Goetze-Pe- dersen, Murgilis Sprachlahmung 68. Cf. Toch. A plac wawim ‘might speak (lit. lead) a word’.
1. IE *sek”- in words for ‘say, tell’, prob. orig. ‘point out’ (as in Ch§&l. socitt) and ultimately the same as *sekv- in words for ‘follow’ (10.52) and ‘see’ (15.51), though the semantic relations may be variously interpreted. Walde-P. 2.477 ff. Ernout-M. 489. Falk-Torp 963. Buck, op. cit. 128 f.
Grk. vere; Lat. inseque, insece ‘re- late, tell’, Umbr. pru-sikurent ‘pronun- tlaverint?, Lat. inquam (-quis, -quit) say’; OW hepp, W. eb ‘inquit’; ON ae OE secgan, OHG sagen, general
me. (except Goth.) for ‘say’ (but con- hection rejected by Collitz, Praet. 78 ff.); Lith, sakyti, Lett. sacit; Arm. ogem ‘say’. - ; a déyw, aor. elroy, fut. épa, etc.,
‘ Grk, Gnpl ‘say, affirm’: Lat. fart
zeigon, Grk. detxvipr, Skt. dic- ‘point out, show’ (15.55). A late parallel de- velopment of Skt. dic- as ‘say’ is attested in Buddhistic Hybrid Sanskrit and in Apabhranca, as Professor F. Edgerton informs me. Walde-P. 1.766. Ernout- M. 265 ff. Walde-H. 1.348.
Lat. aid (ais, ait, etc., infin. rare), early ‘say yes, affirm’, whence weakened ‘say’, fr. *agyd, cf. ad-agid ‘proverb’, prodigium ‘portent’: Grk. 7 ‘spoke’, av-wya (perf.) ‘command’, Arm. asem ‘say’. Walde-P. 1.114. Ernout-M. 29f. Walde-H. 1.24 f.
4. Ir. asbiur, lit. ‘bring forth’, cpd. of as-, pretonic for ess- = Lat. ex, and berim ‘carry’. Hence NIr. adeirim (usually spoken deirim), fr. forms with infixed pronoun, Ir. at-beir ‘he says it’. Pedersen 2.466, 1.469.
Ir. ol, NIr. ar ‘inquit’, orig. an adv. of pronominal origin. Pedersen 1.273, 2.141. Havers, KZ 44.26 ff.
W. dywedyd, beside OW guetid ‘says’ prob. fr. the same root as W. gwadu ‘deny’, Lat. vetdre ‘forbid’. Stokes 268. Loth, RC 42.362 f., 367 f.
Br. lavarout : Ir. labrur ‘speak’ (18.21).
W. medd, Br. eme ‘inquit’, see under Br. komz ‘speak’ (18.21).
=== 18.26 WORD ===
79:18.26 WORD Grk.  pfjua, dékts, eros Goth. waurd Lith. Zodis NG ékis ON ord Lett. vards Lat. verbum, vox Dan. ord ChSl. glagolii, slovo It, parola Sw. ord SCr. rajeé Yr, mot, parole OE word Boh. _ slovo Sp. palabra ME word Pol.  slowo Rum. cuvint NE ‘word Russ. _ slovo Ir, briathar, focal Du. woord Skt.  gabda-, pada-, vacas-, Nir. focal, briathar OHG wort etc. W. gair MHG wort Av. vat-, vatah-, urxéa-, Br. ger, komz NHG ~ wort sravah-, ma§ra-
```


## [2026-09-06T16:16:21.263Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### SKT\"; grep -n -i \"censure\\|censor\" SKT.txt | head -5; echo \"### SKT cosmos\"; grep -n -i \"cosmic\\|cosmos\" SKT.txt | head -5; echo \"### FSD censor\"; grep -n \"^censor\\b\\|^censure\\|^census\" FSD_vol1.txt | head -5"
}
```


### [2026-09-06T16:16:21.340Z] TOOL RESULT

```
### SKT
1743:cIo<e.  A.S.  bt',  preBx  (see  Be-);  and ■O'rri^n,  to  accuse.  Cf.  Icel.  mr^a  (for ITJ;^7<>).  to  Klaoder.  Swed,  riya^  to  discover; O.  Iries.  iiwrogiat  to  accuse;  Golh. u/rifA- JtiH,  to  accase ;  G.  rv^a,  to  censure.  B. These  are  ciusal  verl«,  from  the  $b,  seen  in Goth,  wrchs,  accusation,  led.  rJ^, a  slander. Boy,  a  governor.  (Turk.)  Turk,  big  (i>ron. nearly  as  bay),  a  lord,  prince. Beyond.  (E-)  Sec  Yon. Besel,  the  part  of  a  ring  in  which  the stone  is  set.  (?.)  Also  spell  basil:  it  also means  a  sloping  edge.  — O.  F.  t>iiri.  mod.  F. bUeaH,  a  bezel,  basil,  slant,  sloped  edpe. Cf.  Span,  bixel,  the  slanting  edge  of  a  look- ing-glass; Low  L.  bisaiur,  'lapis  cni  duo sunt  anguli ; '  Ducange.  (Perhaps  from  L. bis,  double ;  and  a/a,  a  wing?) Beaomr,  a  stone.  (F.  -  i*ort.  -  Pers.) O.  F.  bitaar,  F.  b^xaard.  —  Port,  besaar (Brachct).  —  Per*.  fnid-%ahr^  bezoar;  lit *  poisoD-expcHcr.*  from  its  supposcfi  virtue, —  Per^./zi*/,  expelling;  and  «Mr,  poison. Bi-,  prefix.  (L.)  In  bi-as,  the  prefix  is F.,  but  of  L,  origin.  — L.  bi-,  put  for  dui'^ twice.  — I...  duo,  two.  So  also  Gk.  2i-,  Skt dvi.    See  Two.
3226:Censor.  (L.)    L.  censor,  % assessor,  critic. —L.  ctnstrt^  to nion,  appraise.
3227:censure.  (L.)  L.  ctnsufo^ nion.  — L.  etnsert  (above).
19037:Syndlo.  (F.-L.-Gk.)  F.  tymJU,  't 8}Tidick,  censor,  controller  of  maADcn:* Cot.  —  L.  syndutis.  —  Gk.  ovrStjrM,  ad), helping  in  a  court  of  justice ;  as  sb,  s srndic.  —  Gk.  avv,  together;  Str7,  jusbot Allied  to  Dlotlon.     (V  DIK.)
19931:retort,  a  censure  returned ;  tube distilling.  (F.  — L.)  F,  rttorti,  a  retort; lit.  a  thmg  twisted  back.  — F.  rttorti,  fem of  retort,  pp.  of  retordre,  to  twist  back.— L,  re-torquere,  to  twist  back.
### SKT cosmos
4158:Cosmic,  relating  to  the  world.  (Gk.) Gk.  KOfffntfis,  aU] ,  from  n6aiu>\,  order,  also the  world,  univci^c.
### FSD censor
```


## [2026-09-06T16:16:21.971Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=cosmos",
 "prompt": "What Indo-European root does the AHD give for cosmos in the word entry / roots link? Quote the etymology line."
}
```


### [2026-09-06T16:16:25.897Z] TOOL RESULT

```
Based on the content provided, the etymology line for "cosmos" states:

"[Middle English, from Greek _kosmos_, order.]"

However, the page does not specify which Indo-European root the AHD links to for this word. While the page mentions that etymologies can be traced back to reconstructed proto-languages with references to Indo-European Roots appendices, the specific Indo-European root for "cosmos" is not detailed in this particular entry excerpt.
```


## [2026-09-06T16:16:36.345Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cosmetic",
 "prompt": "Give the full etymology of cosmetic: French cosmétique, Greek kosmetikos, kosmein, kosmos, and dates."
}
```


## [2026-09-06T16:16:37.052Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.cnrtl.fr/etymologie/censure",
 "prompt": "Give the etymology and first attestation dates of French \"censure\" and \"censeur\" (from Latin censura / censor)."
}
```


### [2026-09-06T16:16:41.556Z] TOOL RESULT

```
# Etymology of Cosmetic

**Noun (c. 1600):** From the Latinized Greek _kosmetike (tekhnē)_, meaning "the art of dress and ornament." The root is _kosmetikos_, derived from _kosmein_ ("to arrange, adorn") and _kosmos_ ("order; ornament").

**Adjective (1640s):** From French _cosmétique_ (16c.), tracing back through the same Greek roots. The figurative sense meaning "superficial, affecting appearance only" emerged in 1955.

**Key Etymology Chain:**
- Greek _kosmos_ (order, ornament) → Greek _kosmetikos_ (skilled in adornment) → Greek _kosmein_ (to arrange, adorn) → French _cosmétique_ → English _cosmetic_

The word family ultimately connects concepts of order, arrangement, and decoration across Greek and Romance languages spanning from antiquity through the modern era.
```


### [2026-09-06T16:16:42.874Z] TOOL RESULT

```
I apologize, but I cannot provide the etymology and first attestation dates you've requested. The webpage content provided only shows "Portail lexical" (Lexical Portal), which is a header or title without substantive etymological information about "censure" or "censeur."

To answer your question accurately, I would need access to the actual content of a lexical resource or etymology dictionary that contains detailed information about these French words, their Latin origins (censura/censor), and their documented first appearances in texts. The current source material is insufficient for this task.

I'd recommend consulting resources like the TLFi (Trésor de la Langue Française informatisé) or Littré for authoritative French etymological data.
```


## [2026-09-06T16:16:51.955Z] TOOL CALL #58: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D8%B3%D8%AE%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D8%A7%D9%86%D9%87' \\\n 'https://en.wiktionary.org/wiki/%CE%BA%CF%8C%CF%83%CE%BC%CE%BF%CF%82' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1ens-' \\\n 'https://www.etymonline.com/word/cosmos' \\\n 'https://www.etymonline.com/word/censor' \\\n 'https://www.etymonline.com/word/cosmetic' \\\n 'https://abadis.ir/fatofa/%D9%85%D8%A7%D8%AA%DB%8C%DA%A9/' \\\n 'https://abadis.ir/fatofa/%D8%B3%D8%A7%D9%86%D8%B3%D9%88%D8%B1/' \\\n 'https://www.jadvalyab.ir/moein/%D9%85%D8%A7%D8%AA%DB%8C%DA%A9' \\\n 'https://www.ahdictionary.com/word/search.html?q=cosmos' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 255, root Kens: soxan/afsaneh/censor/cosmos/matik/sansor verification' 2>&1 | tail -2; done"
}
```


### [2026-09-06T16:17:02.734Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/42784e83f7dc7fbf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cee37e2d722427e5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f91ac4dc46a68f38.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/03414707790dcf74.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c8ec838d59453ab4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/215ea5c4a4e854aa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3933dd3952ebe762.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/764a885f5c794b7a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9f33009f1ad1eb28.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b7110f8751d3b632.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/17d024d875aab834.txt
```


## [2026-09-06T16:17:05.560Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -A6 -i \"Etymology\" f91ac4dc46a68f38.txt | head -40"
}
```


### [2026-09-06T16:17:05.606Z] TOOL RESULT

```
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
91: Etymology 
92-
93- 2.2 
94- Pronunciation 
95-
96- 2.3 
97- Noun 
--
199: Etymology
200- [ edit ] 
201-
202- From Proto-Hellenic *kónsmos , from Proto-Indo-European *ḱónsmos , from *ḱens- ( “ to announce, put in order ” ) . Related to Latin cēnseō ( “ to estimate ” ) and Sanskrit शंसति ( śaṃsati , “ to commend, praise ” ) . [ 1 ] 
203-
204- Pronunciation
205- [ edit ] 
--
403: Etymology
404- [ edit ] 
405-
406- From Ancient Greek κόσμος ( kósmos ) . Cognate with Mariupol Greek ко́смос ( kósmos ) .
407-
408- Pronunciation
409- [ edit ]
```


## [2026-09-06T16:17:09.443Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -i \"beekes\\|References\" f91ac4dc46a68f38.txt | head -10; sed -n '380,400p' f91ac4dc46a68f38.txt"
}
```


### [2026-09-06T16:17:09.498Z] TOOL RESULT

```
80: References 
340: References
343: ^ Beekes, Robert S. P. ( 2010 ), “ κόσμος ”, in Etymological Dictionary of Greek (Leiden Indo-European Etymological Dictionary Series; 10 ), with the assistance of Lucien van Beek, Leiden, Boston: Brill, →ISBN , pages 759-760 
 honour idem, page 404.
 insignia idem, page 444.
 millinery idem, page 529.
 nature idem, page 552.
 order idem, page 578.
 ornament idem, page 580.
 polity idem, page 625.
 raiment idem, page 669.
 regime idem, page 687.
 robe idem, page 719.
 system idem, page 851.
 tinsel idem, page 877.
 trappings idem, page 890.
 trimming idem, page 895.
 trinket idem, page 895.
 universe idem, page 923.
 world idem, page 989.

 κόσμος , in  ΛΟΓΕΙΟΝ [ Logeion ] Dictionaries for Ancient Greek and Latin (in English, French, Spanish, German, Dutch and Chinese), University of Chicago , since 2011

 Greek
```


## [2026-09-06T16:17:20.591Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -l '\"Kâs' data/extracted/batch/*.json | head; echo \"---\"; python3 - <<'EOF'\nimport json,glob,os\nfor f in sorted(glob.glob('data/extracted/batch/*.json')):\n    d=json.load(open(f))\n    for e in d.get('entries',[]):\n        r=e.get('root') or {}\n        n=r.get('name') or ''\n        if n.startswith('Kâs') or n.startswith('Kas'):\n            print(os.path.basename(f), n, '|', r.get('lang'), '|', r.get('gloss'), '| refs', r.get('refs'))\nEOF"
}
```


### [2026-09-06T16:17:22.230Z] TOOL RESULT

```
data/extracted/batch/page-244.json
data/extracted/batch/page-255.json
data/extracted/batch/page-396.json
data/extracted/batch/page-532.json
---
page-244.json Kas 1 | None | None | refs None
page-244.json Kâs 2 | Indo-European | to direct, command | refs POK:533; WLD1:358
page-244.json Kasyapa | Avestan | tortoise | refs MON:2987; SOD:204; BQT:1651
```


## [2026-09-06T16:17:24.554Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb; sed -n '1,80p' data/verification/agent/charts/page-244.txt | grep -n -A20 \"Kâs 2\""
}
```


### [2026-09-06T16:17:26.113Z] TOOL RESULT

```
sed: can't read data/verification/agent/charts/page-244.txt: No such file or directory
```


## [2026-09-06T16:17:29.489Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 - <<'EOF'\nimport json\nd=json.load(open('data/extracted/batch/page-244.json'))\nfor e in d['entries']:\n    r=e.get('root') or {}\n    if (r.get('name') or '')=='Kâs 2':\n        print(json.dumps(e,ensure_ascii=False,indent=1)[:2500])\nEOF"
}
```


### [2026-09-06T16:17:31.977Z] TOOL RESULT

```
{
 "root": {
  "name": "Kâs 2",
  "lang": "Indo-European",
  "refs": "POK:533; WLD1:358",
  "gloss": "to direct, command"
 },
 "nodes": [
  {
   "id": 1,
   "parent": 0,
   "lang": "Avestan / Old Persian",
   "refs": "POK:533; BRT:1574; SYN:1338; BQT:354",
   "words": [
    {
     "translit": "sâs 1, sâh 1",
     "gloss": "command",
     "script": null
    },
    {
     "translit": "sâsta, sâstar",
     "gloss": "ruler, oppressor",
     "script": null
    },
    {
     "translit": "sâxvan, sâsnâ",
     "gloss": "instructions, teachings",
     "script": null
    },
    {
     "translit": "paiti-sahva",
     "gloss": "return of speech, answer",
     "script": null,
     "see": [
      "Per 3"
     ]
    }
   ],
   "note": null,
   "quote": null
  },
  {
   "id": 2,
   "parent": 1,
   "lang": "Pahlavi",
   "refs": "BQT:354,1573; MON:1843",
   "words": [
    {
     "translit": "sâstâr",
     "gloss": "ruler, oppressor",
     "script": null
    },
    {
     "translit": "sâstâreh",
     "gloss": "bad domination",
     "script": null
    },
    {
     "translit": "soxvan",
     "gloss": "instructions, speech",
     "script": null
    },
    {
     "translit": "passaxv, pasux",
     "gloss": "answer",
     "script": null
    }
   ],
   "note": null,
   "quote": null
  },
  {
   "id": 3,
   "parent": 2,
   "lang": "Persian",
   "refs": "BQT:354,1072,1107; HRN:160; MON:1796; FSF:99",
   "words": [
    {
     "translit": "sâstâ",
     "gloss": "oppressor, demon",
     "script": "ساستا"
    },
    {
     "translit": "soxan",
     "gloss": "speech",
     "script": "سخن"
    },
    {
     "translit": "pâsox",
     "gloss": "answer",
     "script": "پاسخ"
    }
   ],
   "script_extra": "ساستار",
   "note": "See \"Kens\" for another possible root of \"soxan\". See \"Wegwh\" for another possible root of \"pâsox\"",
   "quote": null
  }
 ]
}
```


## [2026-09-06T16:17:45.884Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"sax'^van\\|saxvan\\|sax\\^van\\|sax\\\\\\\\'an\\|saxi'an\\|sazvan\" BRT.txt | head -10; echo \"== try loose ==\"; grep -n \"'Wort'\\s*:\\|n\\. 'Wort\" BRT.txt | head -10"
}
```


### [2026-09-06T16:17:45.963Z] TOOL RESULT

```
== try loose ==
20451:•  j.,  g.  'm^Sra-  m.  'Wort,  Ausspruch, Spruch';  1)  im  gAw.  'Wort':  tnä  äs  at vi  drigvatS  'rqs^ä  gBsta  säsnäs(sti.ya  Y. Ji.  18.  a)  sonst  nur  vom  göttlichen Wort:  malfäi/vfs/äis'yäi  tsi  'rA  (als AP.) marynti  Y.  .#J.  14;  —  ni  Aim  mfrqzdyäi (sd.)  ^waAya  'raü  sit^hakyä  Y.44.14; —  ySi  im  v!  noil  thä  Tfm  varpsmtl  (sd.) Y.  45-  3;  —  •''»'  y'"t  AaurvatStS  alahyä am»ntäias{ai[.)Sl  Y.31.6;  —  tlm  asBUii (sd.)  akurö  'rfm  tasat  .  .  gavBi  Y.  2g. 7.  a)  bes.  'Verheissungswort,  -spruch': av3  °ra  yS  rii&pmff  (sd.)  affir/  Aa^  Y. 44. 17;  —  ans  'rS  mazi/tfm  väurSimatdi (sd.)  xra/stra  Y.28.$.  2)  im  jAw.; 'Spruch,  Ausspruch':  f^i^  (Stverz.)  'rym Y.55,33;  usw.;  —  sva. 'Urteil':  vispanqm anu  (ad.)  'nm  Yt5. 93;  —  sva.  'Befehl*''>:
```


## [2026-09-06T16:17:57.286Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -B3 -A12 \"Etymology\" 42784e83f7dc7fbf.txt | sed -n '1,80p'"
}
```


### [2026-09-06T16:17:57.335Z] TOOL RESULT

```
59- Toggle Arabic subsection 
60-
61- 1.1 
62: Etymology 1.1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Verb 
69-
70- 1.1.2.1 
71- Conjugation 
72-
73- 1.2 
74: Etymology 1.2 
75-
76- 1.2.1 
77- Verb 
78-
79- 1.2.1.1 
80- Conjugation 
81-
82- 1.3 
83: Etymology 1.3 
84-
85- 1.3.1 
86- Adjective 
87-
88- 1.3.1.1 
89- Declension 
90-
91- 1.4 
92- References 
93-
94- 2 
95- Persian 
--
97- Toggle Persian subsection 
98-
99- 2.1 
100: Etymology 
101-
102- 2.2 
103- Pronunciation 
104-
105- 2.3 
106- Noun 
107-
108- 2.3.1 
109- Derived terms 
110-
111- 2.3.2 
112- Descendants 
--
117- Toggle South Levantine Arabic subsection 
118-
119- 3.1 
120: Etymology 1 
121-
122- 3.1.1 
123- Pronunciation 
124-
125- 3.1.2 
126- Verb 
127-
128- 3.1.2.1 
129- Conjugation 
130-
131- 3.1.2.2 
132- See also 
133-
134- 3.2 
135: Etymology 2 
136-
137- 3.2.1 
138- Pronunciation 
139-
140- 3.2.2 
141- Verb
```


## [2026-09-06T16:17:59.814Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; awk '/^ Persian$/,0' 42784e83f7dc7fbf.txt | grep -n -A10 \"Etymology\" | head -30"
}
```


### [2026-09-06T16:18:02.307Z] TOOL RESULT

```
4: Etymology
5- [ edit ] 
6-
7- A user suggests that this Persian entry be cleaned up, giving the reason: “"ultimately from X, but see there for more"?” .
8-
9- Please see the discussion on Requests for cleanup ( + ) for more information and remove this template after the problem has been dealt with.
10-
11- Ultimately from Proto-Iranian *cánhati ; see there for more.
12-Cognate with Sanskrit शंसति ( śáṃsati , “ to declare ” ) , Latin cēnseō and perhaps Ancient Greek κῶμος ( kômos ) .
13-
14- Pronunciation
--
84: Etymology 1
85- [ edit ] 
86-
87- Inherited from Arabic سَخَنَ ( saḵana ) .
88-
89- Pronunciation
90- [ edit ] 
91-
92- IPA ( key ) : /sa.xan/ , [ˈsa.xan] 
93-
94- Audio ( al-Lidd ) : ( file ) 
--
263: Etymology 2
264- [ edit ] 
265-
266- Inherited from Arabic سَخَّنَ ( saḵḵana ) .
267-
268- Pronunciation
```


## [2026-09-06T16:18:47.116Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npy() { python3 -c \"\nimport sys\nf=sys.argv[1]; ln=int(sys.argv[2])\ndata=open(f,encoding='utf-8',errors='replace').read().split('\\n')\ntxt='\\n'.join(data[:ln])\nprint(f, 'line',ln,'-> leaf(0based)=', txt.count('\\f'))\n\" \"$1\" \"$2\"; }\npy HUB.txt 7466; py HUB.txt 7771; py PHD.txt 564; py KLN_1966.txt 6959; py KLN_1966.txt 9351; py SKT.txt 3226; py SKT.txt 4158; py NYB_vol2_glossary.txt 6127; py SYN.txt 31633"
}
```


### [2026-09-06T16:18:50.891Z] TOOL RESULT

```
HUB.txt line 7466 -> leaf(0based)= 220
HUB.txt line 7771 -> leaf(0based)= 228
PHD.txt line 564 -> leaf(0based)= 100
KLN_1966.txt line 6959 -> leaf(0based)= 146
KLN_1966.txt line 9351 -> leaf(0based)= 199
SKT.txt line 3226 -> leaf(0based)= 97
SKT.txt line 4158 -> leaf(0based)= 117
NYB_vol2_glossary.txt line 6127 -> leaf(0based)= 284
SYN.txt line 31633 -> leaf(0based)= 1349
```


## [2026-09-06T16:19:06.627Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9352,9362p' KLN_1966.txt | grep -o \"^[0-9]\\{3,4\\}$\" | head; awk 'NR>=9330 && NR<=9370' KLN_1966.txt | grep -oE \"\\b3[0-9]{2}\\b\" | head -5; echo \"--- PHD page marker near leaf 100\"; awk 'BEGIN{RS=\"\\f\"} NR==101' PHD.txt | tail -3"
}
```


### [2026-09-06T16:19:08.948Z] TOOL RESULT

```
360
361
--- PHD page marker near leaf 100
mand [-”zvmnd | N —mand] dangerous. sel [si | N —] spear, javelin. sém [sym | N —] — asém. !sén(ag) [syn(k)! | N sina] breast, chest. *sén murw [synmzlw | (N simury)] a fabulous bird.
se-pay 75 spas
se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarma
```


## [2026-09-06T16:19:19.087Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==101' PHD.txt | head -4 | cut -c1-300; echo \"=== KLN cosmos page head ===\"; awk 'BEGIN{RS=\"\\f\"} NR==200' KLN_1966.txt | grep -oE \"^[0-9]{3}$|[0-9]{3}\" | head -5"
}
```


### [2026-09-06T16:19:20.672Z] TOOL RESULT

```
mand [-”zvmnd | N —mand] dangerous. sel [si | N —] spear, javelin. sém [sym | N —] — asém. !sén(ag) [syn(k)! | N sina] breast, chest. *sén murw [synmzlw | (N simury)] a fabulous bird.
se-pay 75 spas
se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty,
=== KLN cosmos page head ===
710
770
360
361
```


## [2026-09-06T16:19:26.520Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"afsān\\|afsan\\|ʾfsʾn\" PHD.txt | head -3 | cut -c1-400; echo \"=== NYB ===\"; grep -n \"afsān\\|ʾpsʾn\\|afsan\" NYB_vol2_glossary.txt | head -3 | cut -c1-300; echo \"=== FSD census ===\"; grep -n \"^census\\b\" FSD_vol1.txt | head -2 | cut -c1-400"
}
```


### [2026-09-06T16:19:26.603Z] TOOL RESULT

```
172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'
1864:Jable afsān.
3831:story afsān.
=== NYB ===
=== FSD census ===
```


## [2026-09-06T16:19:32.681Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"fs?n\\|afs[āa]n\" PHD.txt | head -5 | cut -c1-200; echo \"---\"; grep -no \"afsān[^ ]* \\[[^]]*\\][^.]*\\.\" PHD.txt | head -5"
}
```


### [2026-09-06T16:19:32.759Z] TOOL RESULT

```
172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! 
1864:Jable afsān.
3831:story afsān.
---
```


## [2026-09-06T16:19:40.730Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 255 -l 255 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg255hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg255hi.png'); print(im.size)\nw,h=im.size\nim.crop((int(0.20*w),int(0.245*h),int(0.55*w),int(0.28*h))).save('c255_latin.png')\nim.crop((int(0.40*w),int(0.235*h),int(0.72*w),int(0.28*h))).save('c255_french.png')\n\""
}
```


### [2026-09-06T16:19:44.942Z] TOOL RESULT

```
(5100, 6600)
```


## [2026-09-06T16:19:47.157Z] TOOL CALL #73: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c255_latin.png"
}
```


### [2026-09-06T16:19:47.173Z] TOOL RESULT

```

```


## [2026-09-06T16:19:50.965Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg255hi.png'); w,h=im.size\nim.crop((int(0.21*w),int(0.262*h),int(0.56*w),int(0.283*h))).resize((int(0.35*w*1.3),int(0.021*h*1.3))).save('c255_latin2.png')\nim.crop((int(0.42*w),int(0.262*h),int(0.60*w),int(0.283*h))).resize((int(0.18*w*2),int(0.021*h*2))).save('c255_french2.png')\n\""
}
```


### [2026-09-06T16:19:53.154Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:19:55.304Z] TOOL CALL #75: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c255_latin2.png"
}
```


### [2026-09-06T16:19:55.358Z] TOOL RESULT

```

```


## [2026-09-06T16:19:55.357Z] INPUT

[Image: original 2320x180, displayed at 2000x155. Multiply coordinates by 1.16 to map to original image.]


## [2026-09-06T16:19:58.525Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg255hi.png'); w,h=im.size\nc=im.crop((int(0.21*w),int(0.283*h),int(0.62*w),int(0.303*h)))\nc=c.resize((c.width*2,c.height*2))\nc.save('c255_latin3.png'); print(c.size)\n\""
}
```


### [2026-09-06T16:20:00.770Z] TOOL RESULT

```
(4182, 264)
```


## [2026-09-06T16:20:03.224Z] TOOL CALL #77: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c255_latin3.png"
}
```


### [2026-09-06T16:20:03.296Z] TOOL RESULT

```

```


## [2026-09-06T16:20:03.293Z] INPUT

[Image: original 4182x264, displayed at 2000x126. Multiply coordinates by 2.09 to map to original image.]


## [2026-09-06T16:20:14.396Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T16:20:14.435Z] TOOL RESULT

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


## [2026-09-06T16:25:58.342Z] TOOL CALL #79: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-255.json <<'JSONEOF'\n{\n  \"pdf_page\": 255,\n  \"book_page\": 225,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Kens\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ḱens- 'to proclaim, speak solemnly, announce authoritatively' (Pokorny 566; Walde-Pokorny I 403)\",\n      \"note\": \"Root, language label and gloss are all exactly right. Pokorny IEW 566 (POK_02.txt leaf 226) heads the entry \\\"kens- ‚feierlich sprechen, verkündigen‘; kens-tor- ‚Sprecher‘, kens-to- ‚verkündet‘\\\" and gathers under it Skt. śaṃsáyati / śáṃsati, Av. sah- 'pronuntiare', OP θ-ātiy, Alb. thom, Lat. cēnseō / cēnsor / cēnsus, OCS sętъ. Walde-Pokorny I 403 (WLD_Bd1_pages.txt leaf 412) has the same root with the gloss \\\"feierlich sprechen, autoritativ verkündigen\\\" — which is almost word-for-word Nourai's \\\"to speak solemnly, proclaim\\\". Mann IEC 608 gives \\\"Ḱens- (Ḱensmi) … 'utter, pronounce'. WP I, 403\\\" and a separate noun \\\"Ḱensos, ā, us 'utterance, opinion, statement'\\\". One cross-cutting caveat: WP I 403 explicitly REJECTS attaching Greek κόσμος to this root (\\\"In der Bed. kaum vereinbar ist gr. κόσμος\\\"), and Pokorny 566 omits it altogether — see node #9, where Nourai himself hedges. Nothing on the printed page differs from the JSON: the extraction of this chart is faithful throughout.\",\n      \"note_fa\": \"ریشهٔ بازسازی‌شدهٔ *ḱens- در هندواروپایی آغازین به معنای «رسماً گفتن، اعلام کردن، آشکارا بیان کردن» است و پوکورنی (صفحهٔ ۵۶۶) و والده-پوکورنی (جلد ۱، صفحهٔ ۴۰۳) هر دو دقیقاً همین معنا را می‌آورند؛ پس برچسب زبانی و معنای ریشه در نمودار نورایی درست است. بازماندگان این ریشه در سنسکریت śáṃsati «می‌ستاید، بازمی‌گوید»، در اوستایی sah- «اعلام کردن»، در پارسی باستان θātiy «می‌گوید» و در لاتین cēnseō «سنجیدن، داوری کردن» دیده می‌شود. تنها نکتهٔ محل بحث پیوند دادن کُسموس یونانی به این ریشه است که والده-پوکورنی آن را از نظر معنایی «به‌سختی سازگار» می‌داند و پوکورنی اصلاً نمی‌آورد؛ خود نورایی نیز آن را «احتمالی» خوانده است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1ens-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:566\", \"status\": \"supports\", \"note\": \"Pokorny IEW p.566 (local POK_02.txt, awk RS=\\\\f NR==226): \\\"kens- ‚feierlich sprechen, verkündigen‘; kens-tor- ‚Sprecher‘, kens-to- ‚verkündet‘ … av. sah- ‚pronuntiare‘ … apers. θ-ātiy ‚spricht, verkündet‘ (*θa(n)hati) … lat. censeō, -ēre ‚begutachten, schätzen‘ … WP. I 403\\\". Exactly Nourai's root and gloss.\"},\n        {\"ref\": \"WLD1:403\", \"status\": \"supports\", \"note\": \"Walde-Pokorny Bd. I p.403 (local incoming/WLD/WLD_Bd1_pages.txt, leaf 412, running head 'kens- — ker- 403'): \\\"kens- ‚feierlich sprechen, autoritativ verkündigen‘. Ai. çamsayati … av. sŋh- … ap. θatiy oder θanhatiy ‚spricht, verkündigt‘; lat. censeo -ere …\\\". Nourai's page reference is exact.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"IEW p.566 (POK_02.txt leaf 226)\", \"stance\": \"supports\", \"note\": \"\\\"kens- ‚feierlich sprechen, verkündigen‘ … WP. I 403, WH. I 198ff., EM3 201\\\"\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. I p.403 (leaf 412)\", \"stance\": \"partial\", \"note\": \"supports the root but adds \\\"In der Bed. kaum vereinbar ist gr. κόσμος ‚Ordnung, ordentliche Einrichtung, Anstand; Schmuck, Zier‘\\\" — i.e. Walde-Pokorny reject the Greek branch Nourai draws in node #9\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kens- (AHD_watkins1985.txt line 615)\", \"stance\": \"supports\", \"note\": \"\\\"kens-. To proclaim, speak solemnly. Form *kens-ē- in Latin cēnsēre, to judge, assess, estimate, tax: CENSOR, CENSUS; RECENSION. [Pok. kens- 566.]\\\"\"},\n        {\"src\": \"IEC\", \"where\": \"Mann p.608\", \"stance\": \"supports\", \"note\": \"\\\"Ḱens- (Ḱensmi) (variant of Ḱēs-mi, q.v.) 'utter, pronounce'. WP I, 403\\\" plus the noun \\\"Ḱensos, ā, us 'utterance, opinion, statement'\\\"\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Old Persian\",\n          \"words\": \"thah; thâtiy\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"OP θah- (Nourai transliterates the theta as 'th') is the Old Persian continuant of PIE *ḱens-: PIE palatal *ḱ > Proto-Indo-Iranian *ć > Iranian *s, but in the Persid dialect of the Achaemenid inscriptions the cluster *ns/*nh before a vowel yields θ, giving 3sg. θātiy < *θa(n)hati (Pokorny 566 writes exactly \\\"apers. θ-ātiy ‚spricht, verkündet‘ (*θa(n)hati)\\\"). θātiy is the single most frequent verb form in the corpus, the formula θātiy Dārayavauš xšāyaθiya 'says Darius the king' that opens nearly every paragraph of Bīsotūn (DB 1.3, 1.6, 1.8f …) and of DNa/DNb/XPh. Kent's Lexicon p.188 lemmatises the root as θah- and glosses it 'declare, say', equating it with Av. saŋh-, Skt. śāsati and Lat. censet, from pIE *kens-. Both the words and the language label are correct.\",\n          \"derivation_fa\": \"فعل پارسی باستان θah- (که نورایی آن را به شکل ساده‌شدهٔ thah نوشته است) بازماندهٔ مستقیم ریشهٔ *ḱens- است: کام‌گان هندواروپایی *ḱ در هندوایرانی به *ć و سپس در ایرانی به s بدل شد، ولی در گویش پارسیِ سنگ‌نبشته‌های هخامنشی خوشهٔ *nh پیش از واکه به θ گرایید و صورت سوم‌شخص θātiy از *θa(n)hati پدید آمد. این صورت پربسامدترین فعل کتیبه‌هاست و در آغاز تقریباً هر بند بیستون می‌آید: «θātiy Dārayavauš xšāyaθiya» یعنی «داریوش شاه می‌گوید». کنت در واژه‌نامهٔ خود (صفحهٔ ۱۸۸) همین ریشه را θah- «اعلام کردن، گفتن» می‌آورد و آن را با saŋh- اوستایی و censeō لاتین یکی می‌داند؛ بنابراین ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1ens-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:566\", \"status\": \"supports\", \"note\": \"IEW 566: \\\"av. sah- ‚pronuntiare‘, Optat. sahyāt, sasti- ‚Wort, Vorschrift‘; sŋghaite, apers. θ-ātiy ‚spricht, verkündet‘ (*θa(n)hati)\\\"\"},\n            {\"ref\": \"KNT:188\", \"status\": \"supports\", \"note\": \"Kent, Old Persian, Lexicon p.188 (KNT.txt, leaf block carrying the printed numerals 187/188): \\\"θah- vb. 'declare, say': Av. sŋh-, pres. saŋha-, Skt. śāsati, Lt. censet, pIE *kens- (§87) … θātiy (§131, §213) AmH 4, 9; AsH 5; CMb 3; DB 1.3, 6, 8f, 11 …\\\". Nourai's page number is exact.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Bartholomae AiW col. 1578\", \"stance\": \"supports\", \"note\": \"\\\"j., g. sah-, p. θ-ah- V. 'pronuntiare'. Praes. saŋha-, saŋha- … PPfP. sasta-; Inf. sastanaiy\\\" with the Bīsotūn citation \\\"θātiy Dārayavauš xšāyaθiya\\\" — Bartholomae treats Av. sah- and OP θah- as one verb\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 18.22 SAY, p.1257\", \"stance\": \"supports\", \"note\": \"the comparative table for 'say' lists \\\"OPers. θah-\\\" beside Av. vak-, mrū-, aθ- and Skt. vac-\"},\n            {\"src\": \"IEC\", \"where\": \"Mann p.608 s.v. Ḱens-\", \"stance\": \"supports\", \"note\": \"\\\"Ober. cf. θātiy, 3s 'says'; a-θaham 'I said'\\\" listed among the reflexes of Ḱens-\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"soxan «سخن»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The root attribution is right, the immediate parent is not. NP سخن soxan continues MP saxwan (MacKenzie: \\\"saxwan [MPYA < A mly'; shwn' | M sxwn, N suxan] word, speech\\\"), from Old Iranian *sax(u)an- 'utterance', a -van-/-uan- noun to the verb sah- of nodes #1/#3 — Wiktionary derives the Persian word from Proto-Iranian *cánhati and gives Skt. śáṃsati and Lat. cēnseō as cognates, i.e. exactly PIE *ḱens-. But Hübschmann, Persische Studien §99 (p.210) states the rule and the consequence explicitly: \\\"Ap. θ im Anlaut vor Vokalen = iran. s = idg. ḱ ist im Np. nicht durch h sondern durch s vertreten … suxun, suxan 'Wort' aus iran. *saxvan- = ap. *θa(h)uvan- von θah 'sprechen', skr. śaṃs-, zd. saŋh-\\\", and again at §108 (p.218) \\\"suxun, suxan 'Wort', älter saxwan … aus phl. saxwan\\\". In other words the New Persian word cannot descend from the θ-dialect form θah- drawn as its parent; it comes through a Middle Persian *saxwan whose s- points to a non-Persid (Median-type) Old Iranian form of the same root. The chart's own NOTE offers \\\"Kâs 2\\\" (Nourai's PIE *ḱās- 'to direct, command', p.244) as an alternative parent; modern scholarship keeps soxan with *ḱens- (Hübschmann, Wiktionary), while Av. sāsnā- 'teaching' and sāstar- 'ruler' belong to the other root — the two are frequently confused in Iranian, which is why Nourai hedged.\",\n          \"derivation_fa\": \"ریشه درست است، ولی پدرِ بی‌واسطه در نمودار درست انتخاب نشده است. «سخن» فارسی نو دنبالهٔ saxwan فارسی میانه است (مکنزی: «saxwan … word, speech، فارسی نو suxan») و آن نیز از ایرانی باستان *sax(u)an- «گفتار» می‌آید، یعنی اسمی با پسوند ‎-uan-‎ از همان ستاک sah-. هوبشمان در «مطالعات فارسی» بند ۹۹ به‌روشنی می‌نویسد که θ آغازیِ پارسی باستان در فارسی نو نه به h بلکه به س بدل می‌شود و suxan «واژه» از ایرانیِ *saxvan- است که برابر پارسی باستانِ *θa(h)uvan- از θah «گفتن» می‌باشد؛ پس «سخن» نمی‌تواند مستقیماً از گونهٔ θ-دار کتیبه‌ها گرفته شده باشد و از گویشی غیرپارسی (مادی‌گونه) به فارسی میانه رسیده است. یادداشت خود نمودار «کاس ۲» (ریشهٔ *ḱās- «فرمان دادن») را هم پیشنهاد می‌کند؛ ریشه‌شناسی امروزی «سخن» را زیر *ḱens- می‌گذارد و sāsnā- و sāstar- اوستایی را زیر آن ریشهٔ دیگر، هرچند این دو ریشه در ایرانی بارها با هم آمیخته‌اند. حکم: ادعای نورایی دربارهٔ ریشه پذیرفتنی است، اما پیوند «پارسی باستان ← سخن» با احتیاط.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%D8%AE%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"TZF:19\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Tārix-e Moxtasar-e Zabān-e Fārsi p.19 — refs_online.json gives kind 'website' with no open copy (ketabnak requires login); no accessible text to verify\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien §99 (p.210) and §108 (p.218)\", \"stance\": \"partial\", \"note\": \"\\\"suxun, suxan 'Wort' aus iran. *saxvan- = ap. *θa(h)uvan- von θah 'sprechen', skr. śaṃs-, zd. saŋh-\\\" — same root as Nourai, but explicitly NOT via the Old Persian θ-dialect: \\\"Ap. θ im Anlaut vor Vokalen … ist im Np. nicht durch h sondern durch s vertreten\\\"\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.74 s.v. saxwan\", \"stance\": \"supports\", \"note\": \"\\\"saxwan [MPYA < A mly'; shwn' | M sxwn, N suxan] word, speech\\\" — establishes the Middle Persian step the chart omits\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, Pahlavi-script index s.v. sxwn\", \"stance\": \"supports\", \"note\": \"index line \\\"sxwn: saxwan\\\", confirming the Pahlavi spelling shwn' = saxwan\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Riše-hā-ye Hend-o-Orupāyi, pdf pp.352-353\", \"stance\": \"supports\", \"note\": \"the entry lists اوستایی SAH, پارسی باستان *θAH / *θANH, پهلوی SAXWAN alongside Latin censeō, and notes «واژهٔ فارسی پاسخ از پاد و سخن ساخته شده است (پهلوی PASSXW)» — same root chain (OCR noisy)\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Avestan\",\n          \"words\": \"sah 2\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Av. sah- (present saŋha-/saŋhaite, opt. sahyāt, ppp. sasta-, inf. sastanaiy) 'to declare, pronounce' is the regular Avestan reflex of *ḱens-: PIE *ḱ > Iranian s, and the nasal of the root appears in the present stem saŋh- (< *ḱens-). Bartholomae AiW col.1578 heads it \\\"j., g. sah-, p. θ-ah- V. 'pronuntiare'\\\", i.e. he treats the Avestan and the Old Persian verb of node #1 as one lemma; Pokorny 566 gives \\\"av. sah- ‚pronuntiare‘, Optat. sahyāt, sasti- ‚Wort, Vorschrift‘; saŋhaite\\\". Nourai's '2' is his own homonym number, distinguishing this sah- from the sāh-/sās- 'to command, teach' of his root \\\"Kâs 2\\\" (PIE *ḱās-, p.244) — a distinction Bartholomae also makes, and a sensible one.\",\n          \"derivation_fa\": \"ستاک اوستایی sah- (بن حال saŋha-/saŋhaite، وجه تمنایی sahyāt، اسم مفعول sasta-) به معنای «اعلام کردن، گفتن» بازتاب قاعده‌مند *ḱens- در اوستایی است: کام‌گان *ḱ در ایرانی به s بدل شد و خیشومی ریشه در بن حال به شکل saŋh- بازمانده است. بارتولومه در «فرهنگ ایرانی باستان» ستون ۱۵۷۸ همین ماده را «sah- اوستایی، θah- پارسی باستان، فعل: pronuntiare» می‌آورد، یعنی ماده اوستایی و پارسی باستان را یکی می‌داند، و پوکورنی نیز در صفحهٔ ۵۶۶ همین صورت‌ها را زیر ریشه می‌آورد. عدد ۲ در «sah 2» شمارهٔ هم‌آواییِ خود نورایی است و این ستاک را از sāh-/sās- «فرمان دادن، آموزاندن» (ریشهٔ «کاس ۲» او) جدا می‌کند؛ این تفکیک درست و مطابق بارتولومه است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1ens-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:566\", \"status\": \"supports\", \"note\": \"IEW 566: \\\"av. sah- ‚pronuntiare‘, Optat. sahyāt, sasti- ‚Wort, Vorschrift‘; sŋghaite\\\"\"},\n            {\"ref\": \"KNT:188\", \"status\": \"supports\", \"note\": \"Kent p.188 s.v. θah-: \\\"Av. sŋh-, pres. saŋha-, Skt. śāsati, Lt. censet, pIE *kens-\\\" — the Avestan verb is cited on exactly the page Nourai gives\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW col. 1578\", \"stance\": \"supports\", \"note\": \"\\\"j., g. sah-, p. θ-ah- V. 'pronuntiare'. Praes. 1 sah- : sas-, 3 saŋha-, saŋha- … PPfP. sasta-; Inf. sastanaiy\\\"; the neighbouring lemma \\\"saŋha- m. 'Zahl' … zum V. sah-\\\" shows the same stem\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.403\", \"stance\": \"supports\", \"note\": \"\\\"av. sŋh- (saŋhaiti usw., s. Bartholomae Airan. Wb. 1578 f.) ‚pronuntiare‘, sasti- ‚Wort, Vorschrift‘\\\"\"},\n            {\"src\": \"IEC\", \"where\": \"Mann p.608 s.v. Ḱens-\", \"stance\": \"supports\", \"note\": \"\\\"Av. sāsmi 'teach' beside sasmi 'speak, order'\\\" grouped with Skt. śáṃsami and Lat. censeō\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"afsâneh «افسانه» (also فسانه)\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP افسانه afsāne / فسانه fasāne 'tale, fable' goes back to MP afsānag (Manichaean MP ʾfsʾnk /afsānag/ 'fable'; MacKenzie's English index has \\\"fable afsān\\\" and \\\"story afsān\\\"), and the standard analysis takes it as a prefixed nominal derivative of exactly this root: Mann, IEC 608, s.v. \\\"Ḱensos, ā, us 'utterance, opinion, statement'. Cf. Ḱens- (and Ḱēs-). WP I, 403\\\" lists among the reflexes \\\"Per. cf. fa-sāna 'fable'\\\" beside Skt. śáṃsaḥ, Lat. cēnsus and Osc. censaum — i.e. Nourai's cited page says precisely what his arrow says. The prefix element (a)f- is best explained from Old Iranian *upa- or *abi- (cf. افسون afsun, افسوس afsus with the same af-), so *upa-sanH-na-ka- > MP afsānag > NP afsāna, with the usual MP -ag > NP -a(h) and the doublet فسانه produced by loss of the unstressed initial vowel, as in Khayyām's line quoted on the chart. The verdict is 'plausible' rather than 'confirmed' only because the prefix is not securely established and Wiktionary records a competing suggestion — \\\"a prefixed derivative of Proto-Indo-European *ḱens-, or maybe *ḱen- 'empty' (cf. Ancient Greek κενός)\\\" — so the *ḱens- route is the leading but not the sole account.\",\n          \"derivation_fa\": \"«افسانه» (گونهٔ کوتاه‌شدهٔ «فسانه») از afsānag فارسی میانه می‌آید (در فارسی میانهٔ مانوی ʾfsʾnk، و مکنزی در نمایهٔ انگلیسی‌اش afsān را برابر fable و story می‌آورد). تحلیل رایج آن را مشتقی پیشوندی از همین ریشه می‌داند: مان در «فرهنگ تطبیقی هندواروپایی» صفحهٔ ۶۰۸، ذیل *Ḱensos «گفته، سخن»، خودِ صورت فارسی fa-sāna «افسانه» را در کنار śáṃsaḥ سنسکریت و cēnsus لاتین می‌آورد؛ یعنی همان ارجاعی که نورایی داده است دقیقاً ادعای او را تأیید می‌کند. پیشوند «اَف-» را بهتر است از *upa-/*abi- ایرانی باستان بدانیم (مانند «افسون» و «افسوس»)، پس *upa-sanH-na-ka- ← afsānag ← افسانه، با تبدیل معمول ‎-ag‎ فارسی میانه به ‎-ه‎ فارسی نو، و «فسانه» از افتادن واکهٔ آغازینِ بی‌تکیه پدید آمده است (چنان‌که در بیت خیام روی همین صفحه). حکم «با احتیاط پذیرفتنی» است، زیرا پیشوند به‌طور قطعی اثبات نشده و ویکی‌واژه گمانِ رقیبی هم یاد می‌کند: پیوند با ریشهٔ *ḱen- «تهی» (یونانی kenós).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D8%A7%D9%86%D9%87\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:608\", \"status\": \"supports\", \"note\": \"Mann, IEC p.608: \\\"Ḱensos, ā, us 'utterance, opinion, statement'. Cf. Ḱens- (and Ḱēs-). WP I, 403 — Skt. śáṃsaḥ 'pronouncement' … Per. cf. fa-sāna 'fable'; Lat. cēnsus, gs -us 'polltax, census'\\\". Nourai's page is exact and the Persian word is named there.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, English–Pahlavi index s.vv. 'fable' and 'story'\", \"stance\": \"supports\", \"note\": \"\\\"fable afsān.\\\" and \\\"story afsān.\\\" — the Middle Persian antecedent of افسانه\"},\n            {\"src\": \"POK\", \"where\": \"IEW p.566 s.v. kens-\", \"stance\": \"silent\", \"note\": \"Pokorny lists no Iranian nominal derivative for this root beyond Av. sasti-; افسانه is not mentioned\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.403\", \"stance\": \"silent\", \"note\": \"the Iranian material is limited to Av. sŋh-/sasti- and OP θatiy; no New Persian derivative\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie\", \"stance\": \"silent\", \"note\": \"grep of HRN.txt for 'afsana', 'fasāna', 'Fabel', 'Märchen' returns nothing — Horn has no entry for افسانه\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"cĕns-ĕre\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin cēnsēre 'to assess, appraise, judge, reckon; to take a census' is the classic Italic reflex of *ḱens-, formed with the stative suffix *-ē- (Watkins: \\\"Form *kens-ē- in Latin cēnsēre\\\"; from *ḱn̥s-eh₁-ye-ti per Wiktionary). Pokorny 566 sets it beside Oscan censamur 'censetor', censaum 'censere', keenzstur/kenzsur = cēnsor (matching Skt. śaṃstar- 'he who recites'), an-censto = incensa, and the participial noun cēnsus (= Skt. śastá- 'spoken, praised'), the source of the Roman institution of the census and the magistracy of the censor (5th c. BCE). Semantically the root's 'proclaim solemnly' narrowed in Italic to the formal declaration of a citizen's property before the magistrate, hence 'assess, value, judge'. Nourai's gloss 'to judge, estimate, tax' is right. One typographic note: the book prints the vowels with breves, cĕns-ĕre, whereas the Latin verb has two long ē (cēnsēre); the extraction is faithful to the page, and this is only Nourai's habitual disregard of Latin quantities, not a factual error.\",\n          \"derivation_fa\": \"فعل لاتین cēnsēre «سنجیدن، ارزیابی کردن، داوری کردن، سرشماری کردن» بازتاب ایتالیکِ ریشهٔ *ḱens- است که با پسوند حالت‌نمای *-ē- ساخته شده (واتکینز: «صورت *kens-ē- در cēnsēre لاتین»). پوکورنی در صفحهٔ ۵۶۶ آن را در کنار صورت‌های اسکی censamur و keenzstur (= cēnsor) و اسم مفعولی cēnsus می‌گذارد که با śastá- سنسکریت «گفته‌شده، ستوده‌شده» برابر است. از نظر معنایی، مفهوم «رسماً اعلام کردن» در ایتالیک به «اعلام رسمی دارایی نزد مأمور دولت» و از آنجا به «برآورد کردن، مالیات بستن» تخصیص یافته است؛ پس معنایی که نورایی می‌دهد درست است. تنها نکتهٔ نگارشی این است که کتاب هر دو واکه را کوتاه (cĕns-ĕre) نشان داده، حال آنکه در لاتین هر دو کشیده است (cēnsēre)؛ این بی‌دقتی خود کتاب است و خوانش اسکن درست انجام شده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/censor\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1ens-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:566\", \"status\": \"supports\", \"note\": \"IEW 566: \\\"lat. censeō, -ēre ‚begutachten, schätzen‘, osk. censamur ‚censetor‘, censaum ‚censere‘, keenzstur, kenzsur (= censor : ai. śaṃstar- ‚der da rezitiert‘) … lat. census (: ai. śastá-h ‚gesprochen, gepriesen‘)\\\"\"},\n            {\"ref\": \"AHD:1522\", \"status\": \"supports\", \"note\": \"the corresponding entry in Watkins 1985 (the 1976 appendix pp.1505-1550 is not open online, but the root list is the same): \\\"kens-. To proclaim, speak solemnly. Form *kens-ē- in Latin cénsére, to judge, assess, estimate, tax: CENSOR, CENSUS; RECENSION. [Pok. kens- 566.]\\\"\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966, pp. 257-258 s.v. censor\", \"stance\": \"supports\", \"note\": \"\\\"censor, n. — L. censor, fr. censere, 'to reckon, assess, estimate, value, deem, judge', cogn. with OI śaṃsati, 'recites, praises', śaṃsayati, 'announces', śāsā, 'song of praise', Toch. B cansmaya, 'he has been proclaimed'\\\"\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., p.77 s.v. Censor\", \"stance\": \"supports\", \"note\": \"\\\"Censor. (L.) L. censor, an assessor, critic. — L. censere, to estimate, appraise.\\\" and \\\"censure. (L.) L. censura … — L. censere (above).\\\"\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.403\", \"stance\": \"supports\", \"note\": \"\\\"lat. censeo -ere ‚begutachten, schätzen‘, osk. censamur ‚censetor‘ … lat. census\\\"\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"French\",\n          \"words\": \"censur\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"There is no French word *censur. French has censure f. 'censorship, censure' (< Lat. cēnsūra, itself from cēnsus, pp. of cēnsēre) and censeur m. 'censor' (< Lat. cēnsōrem). The box carries the gloss 'censor', which belongs to censeur, but the word that actually gave the Persian سانسور of node #7 — and that Klein describes — is censure: \\\"censure, n. — F. censure, fr. L. censura, 'judgment, criticism', fr. census, pp. of censere. See censor and -ure\\\" (Klein 1966 p.258). I rendered the printed page at 600 dpi and read the box: it prints exactly \\\"censur : censor\\\", so the extraction is faithful and the missing final -e is Nourai's own misprint (the box also carries no reference of its own, refs=None, which is consistent with it being a hurried intermediate link). The chain Latin cēnsēre > cēnsūra > OFr./Fr. censure (attested from the 14th c.) > Persian sānsor is otherwise sound.\",\n          \"derivation_fa\": \"در فرانسه واژه‌ای به شکل *censur وجود ندارد؛ آنچه هست censure (مؤنث) به معنای «سانسور، بازرسی و حذف» از cēnsūra لاتین، و censeur (مذکر) به معنای «سانسورچی» از cēnsōrem لاتین است. معنایی که کتاب داده («censor») به censeur می‌خورد، اما واژه‌ای که «سانسور» فارسی از آن گرفته شده censure است؛ کلاین (صفحهٔ ۲۵۸) می‌نویسد: «censure از فرانسهٔ censure، از لاتین censūra ‹داوری، نقد›، از census». صفحهٔ چاپی را با تفکیک ۶۰۰ نقطه بر اینچ بازخوانی کردم: در خانه دقیقاً «censur : censor» چاپ شده است؛ پس خطای خوانش اسکن نیست، بلکه خطای چاپی خود کتاب است و «ه» پایانی افتاده است. زنجیرهٔ لاتین cēnsēre ← cēnsūra ← فرانسهٔ censure ← فارسی «سانسور» در کل درست است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"censur : censor\",\n          \"correct_form\": \"censure (F., 'censorship'); F. censeur = 'censor'\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/censor\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference of its own in the book (refs=None); nothing of Nourai's to check\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.258 s.vv. censure, censor\", \"stance\": \"partial\", \"note\": \"\\\"censure, n. — F. censure, fr. L. censura, 'judgment, criticism', fr. census, pp. of censere\\\" — has the derivation but the French form is censure, not *censur\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat p.77 s.v. censure\", \"stance\": \"partial\", \"note\": \"\\\"censure. (L.) L. censura … — L. censere\\\"; Skeat takes English censure straight from Latin, and knows no form *censur\"},\n            {\"src\": \"BOOK\", \"where\": \"printed page 225 (pdf 255), Latin→French box, rendered at 600 dpi (copy at data/verification/sources/refs/ocr/BOOK/255.png)\", \"stance\": \"supports\", \"note\": \"the page itself reads \\\"censur : censor\\\" — the JSON matches the book exactly, so the defect is the author's\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"sânsor «سانسور»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian سانسور sānsor is a 20th-century loan from French censure [sɑ̃syːʁ], taken over with the French nasal vowel resolved into ān and the French -ure rendered -or/-ur: censure > sān-sur/sān-sor. It entered Persian with the whole vocabulary of the press and of state administration in the Constitutional and early Pahlavi periods, when French was the language of Iranian officialdom, alongside ژورنال, رپرتاژ, بولتن. Dehkhoda glosses it 'ممیزی و تفتیش مطبوعات و مکاتیب و نمایشها' and Mo'in 'کنترل و بازرسی حاکمیت بر فعالیت سیاسی، اجتماعی و … خاصهٔ فرهنگی', both tagging it as French. Thus the route Latin cēnsēre > Fr. censure > Pers. sānsor is correct; only the French form printed in node #6 is defective.\",\n          \"derivation_fa\": \"«سانسور» وام‌واژه‌ای است از فرانسهٔ censure که در سدهٔ چهاردهم خورشیدی وارد فارسی شده است. واکهٔ خیشومیِ فرانسوی ‎[ɑ̃]‎ در فارسی به «ان» تجزیه شده و پایانهٔ ‎-ure‎ به ‎-ور‎ بدل گشته است: censure ← سانسور. این واژه همراه با انبوه اصطلاحات مطبوعاتی و اداریِ فرانسوی‌تبار (ژورنال، رپرتاژ، بولتن) در دورهٔ مشروطه و پهلوی اول به فارسی راه یافت، در روزگاری که فرانسه زبان دیوان و مطبوعات ایران بود. دهخدا آن را «ممیزی و تفتیش مطبوعات و مکاتیب و نمایش‌ها» و معین «کنترل و بازرسی حاکمیت بر فعالیت سیاسی، اجتماعی و… خاصهٔ فرهنگی» معنی می‌کند و هر دو آن را «فر.» (فرانسوی) نشان می‌گذارند. پس ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%B3%D8%A7%D9%86%D8%B3%D9%88%D8%B1/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"VOP:210\", \"status\": \"not_checked\", \"note\": \"Moshiri, Farhang-e Vāžehā-ye Orupāyi dar Fārsi (1371) — refs_online.json records kind 'none': not on archive.org, ketabnak or noorlib, no copy accessible\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in via abadis.ir/fatofa/سانسور (فرهنگ فارسی معین)\", \"stance\": \"supports\", \"note\": \"tagged French; 'کنترل و بازرسی حاکمیت بر فعالیت سیاسی، اجتماعی و… خاصهٔ فرهنگی'\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Riše-hā-ye Hend-o-Orupāyi\", \"stance\": \"silent\", \"note\": \"grep of ARY_pages.txt finds no entry for سانسور — the book covers inherited Indo-European vocabulary, not modern European loans\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.258 s.v. censure\", \"stance\": \"supports\", \"note\": \"confirms the French etymon censure < L. censura that the Persian word reflects\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"censor, census\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English censor (1530s) is Latin cēnsor, the title of the Roman magistrate of the 5th c. BCE who took the census and supervised public morals; the modern sense 'official who examines books, plays, films' is first recorded in the 1640s. Census (1610s) is Latin cēnsus, 'the enrolment of the names and property assessments of all Roman citizens', the past participle of cēnsēre used as a noun. Both are learned borrowings straight from Latin (censor partly through French censeur), not inherited, so no Germanic sound changes are involved. Watkins lists precisely CENSOR, CENSUS (and RECENSION) as the English outcomes of *kens- via cēnsēre, and Etymonline gives the same PIE root *kens- 'speak solemnly, proclaim'.\",\n          \"derivation_fa\": \"واژه‌های انگلیسی censor (از دههٔ ۱۵۳۰) و census (از دههٔ ۱۶۱۰) وام‌واژه‌های کتابی و مستقیم از لاتین‌اند، نه میراث ژرمنی؛ از این رو هیچ دگرگونی آوایی ژرمنی در آن‌ها دیده نمی‌شود. censor همان cēnsor لاتین است، عنوان مأمور رومی سدهٔ پنجم پیش از میلاد که سرشماری می‌کرد و بر اخلاق همگانی نظارت داشت، و معنای امروزی آن («بازرس کتاب و نمایش و فیلم») از دههٔ ۱۶۴۰ پدید آمده است. census نیز اسم‌شدهٔ اسم مفعول cēnsus «ثبت نام و دارایی شهروندان رومی» است. واتکینز در پیوست ریشه‌های هندواروپاییِ فرهنگ آمریکن هریتیج همین دو واژه را (به‌همراه recension) برآمده از *kens- از راه cēnsēre می‌داند؛ پس ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/censor\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1522\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. kens- (AHD_watkins1985.txt line 615) ends \\\"…to judge, assess, estimate, tax: CENSOR, CENSUS; RECENSION\\\"; the index confirms \\\"CENSOR kens- CENSUS kens-\\\"\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 pp. 257-258 s.vv. censor, census\", \"stance\": \"supports\", \"note\": \"\\\"census, n. — L. census, 'rating of property, registration of citizens and their property', fr. census, pp. of censere. See censor.\\\"\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat p.77 s.v. Censor\", \"stance\": \"supports\", \"note\": \"\\\"Censor. (L.) L. censor, an assessor, critic. — L. censere, to estimate, appraise.\\\"\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, index p.1340\", \"stance\": \"supports\", \"note\": \"\\\"CENSOR kens- CENSUS kens-\\\"\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Greek\",\n          \"words\": \"kos-mein; kos-mĕtikos; kos-mos\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Greek words themselves are impeccable: κόσμος 'order, orderly arrangement; ornament, adornment; world-order, universe' (Pythagoras is said to have first applied it to the universe), the denominative verb κοσμέω/κοσμεῖν 'to arrange, order, adorn, equip', and the verbal adjective κοσμητικός 'skilled in arranging/adorning' (from κοσμητός 'well-ordered'). What is at issue is only the arrow from *ḱens-, and Nourai's own NOTE ('A possible derivation') is the right posture. Against it: Walde-Pokorny I 403, on the very page Nourai cites for the root, says outright \\\"In der Bed. kaum vereinbar ist gr. κόσμος ‚Ordnung … Schmuck, Zier‘ (wäre *ḱons-mos)\\\" and prefers Brugmann's alternative; Pokorny 566 drops the Greek word from the entry entirely; Klein (1966 p.361) ends his κόσμος entry \\\"of uncertain origin\\\"; Watkins 1985 puts it under a wholly separate root \\\"kes-³. To order. Suffixed o-grade form *kos-mo- in Greek kosmos, order: COSMOS; MACROCOSM, MICROCOSM\\\" — so Nourai's citation AHD:1522 (= the kens- page) does not cover kosmos; and today's online AHD gives only \\\"[Middle English, from Greek kosmos, order.]\\\" with no root at all. For it: Wiktionary, citing Beekes, EDG (2010) 759-760, derives κόσμος from Proto-Hellenic *kónsmos < PIE *ḱóns-mo- < *ḱens- 'to announce, put in order', which is the same *ḱons-mos that Walde-Pokorny had considered and rejected. So the derivation is accepted by some scholars and not by others — hence 'plausible', with the semantic bridge ('authoritative pronouncement' → 'ordering, arrangement') the weak point.\",\n          \"derivation_fa\": \"خودِ واژه‌های یونانی بی‌اشکال‌اند: κόσμος «نظم، سامان؛ زیور، آرایه؛ نظمِ جهان، گیتی» (گفته‌اند نخستین‌بار فیثاغورس آن را بر جهان اطلاق کرد)، فعل مشتق κοσμεῖν «سامان دادن، آراستن» و صفت فعلی κοσμητικός «کاردان در آراستن». آنچه محل بحث است تنها پیوند این خانواده با ریشهٔ *ḱens- است و خودِ نورایی هم آن را «احتمالی» خوانده که موضع درستی است. در برابر این پیوند: والده-پوکورنی در همان صفحهٔ ۴۰۳ که نورایی برای ریشه ارجاع می‌دهد صریحاً می‌نویسد «κόσμος یونانی از نظر معنایی به‌سختی با این ریشه سازگار است»؛ پوکورنی در صفحهٔ ۵۶۶ اصلاً آن را نمی‌آورد؛ کلاین آن را «with نامعلوم‌الاصل» می‌داند؛ و واتکینز در پیوست آمریکن هریتیج آن را زیر ریشهٔ جداگانهٔ kes-³ «سامان دادن» می‌گذارد، پس ارجاع AHD:1522 که نورایی داده اصلاً به کُسموس مربوط نیست. در تأیید آن: ویکی‌واژه به استناد بیکس (فرهنگ ریشه‌شناختی یونانی، ۲۰۱۰، صفحات ۷۵۹–۷۶۰) κόσμος را از *ḱóns-mo- و آن را از *ḱens- می‌گیرد. بنابراین این اشتقاق را برخی پذیرفته‌اند و برخی نه؛ حکم «با احتیاط پذیرفتنی» است و ضعف اصلی در پل معنایی («اعلام رسمی» ← «نظم و سامان») نهفته است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%BA%CF%8C%CF%83%CE%BC%CE%BF%CF%82\",\n            \"https://www.etymonline.com/word/cosmos\",\n            \"https://www.ahdictionary.com/word/search.html?q=cosmos\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1522\", \"status\": \"contradicts\", \"note\": \"p.1522 of the 1976 appendix is the kens- page; but Watkins assigns kosmos to a different root: \\\"kes-³. To order. Suffixed o-grade form *kos-mo- in Greek kosmos, order: COSMOS; MACROCOSM, MICROCOSM\\\" (AHD_watkins1985.txt line 623), and the index reads \\\"cosmos kes-3\\\". AHD therefore does not support Greek kosmos < kens-.\"},\n            {\"ref\": \"AHD:301\", \"status\": \"partial\", \"note\": \"p.301 of the 1976 AHD is the dictionary page carrying 'cosmetic'; the current online AHD gives only \\\"[Middle English, from Greek kosmos, order.]\\\" with no Indo-European root link at all\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.403 s.v. kens-\", \"stance\": \"contradicts\", \"note\": \"\\\"In der Bed. kaum vereinbar ist gr. κόσμος ‚Ordnung, ordentliche Einrichtung, Anstand; Schmuck, Zier‘ (wäre *ḱons-mos), Froehde KZ. 33, 311, Zupitza Gutt. 109, Brugmann Distrib. 19; letzterer versucht IF. 28, 358 f. Anknüpfung vielmehr an kʷerep-, kʷer- ‚machen‘\\\"\"},\n            {\"src\": \"POK\", \"where\": \"IEW p.566 s.v. kens-\", \"stance\": \"silent\", \"note\": \"the entry lists Skt., Av., OP, Alb., Lat., Osc. and OCS reflexes and no Greek word — Pokorny silently dropped the κόσμος question from WP I 403\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 pp. 360-361 s.v. cosmos\", \"stance\": \"contradicts\", \"note\": \"\\\"cosmos, n. … — Gk. κόσμος, 'order, ornament, decoration, set form; world, universe', whence κοσμεῖν, 'to order, arrange, adorn', κοσμητός (verbal adj.), 'well-ordered, regular'; of uncertain origin.\\\"\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kes-³ and index\", \"stance\": \"contradicts\", \"note\": \"\\\"cosmos kes-3\\\" — a separate root from kens-\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat p.97 s.v. Cosmic\", \"stance\": \"silent\", \"note\": \"\\\"Cosmic, relating to the world. (Gk.) Gk. κοσμικός, adj., from κόσμος, order, also the world, universe\\\" — no Indo-European etymology offered\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"French\",\n          \"words\": \"cosmetique\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"French cosmétique (16th c.) is a learned borrowing of Greek κοσμητικός, feminine κοσμητική (τέχνη) 'the art of dress and ornament', through the Latinised cosmetica; the Greek adjective is built on κοσμητός 'well-ordered', verbal adjective of κοσμεῖν 'to arrange, adorn'. Etymonline gives the chain \\\"Greek kosmos (order, ornament) > kosmetikos (skilled in adornment) > French cosmétique > English cosmetic\\\", the English adjective being taken from the French in the 1640s (the noun a little earlier, c.1600, directly from the Greek). The book prints the French word without its accent, 'cosmetique'; that is Nourai's usual practice with French forms and not an error of substance.\",\n          \"derivation_fa\": \"واژهٔ فرانسوی cosmétique (سدهٔ شانزدهم میلادی) وام‌گیریِ دانشورانه‌ای است از κοσμητικός یونانی (مؤنث κοσμητική τέχνη «هنر آرایش و پیرایش») از راه صورت لاتینی‌شدهٔ cosmetica؛ صفت یونانی خود از κοσμητός «آراسته، سامان‌یافته»، صفت فعلی κοσμεῖν «آراستن، سامان دادن»، ساخته شده است. اتیمانلاین همین زنجیره را می‌آورد: kosmos ← kosmetikos ← cosmétique فرانسوی ← cosmetic انگلیسی. کتاب واژهٔ فرانسوی را بدون علامت تشدیدِ واکه («cosmetique») چاپ کرده است که شیوهٔ همیشگی نورایی در نوشتن واژه‌های فرانسوی است و خطای محتوایی به شمار نمی‌رود؛ در مجموع ادعای این گره درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/cosmetic\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:301\", \"status\": \"partial\", \"note\": \"p.301 of the 1976 AHD is the dictionary page with 'cosmetic'; the modern AHD entry for cosmetic gives \\\"[French cosmétique, from Greek kosmētikos, skilled in adornment, from kosmein, to arrange, adorn, from kosmos, order]\\\" — the French step Nourai draws is confirmed, but AHD offers no Indo-European root for it\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.360 s.v. cosmetic\", \"stance\": \"supports\", \"note\": \"\\\"cosmetic, adj., serving to beautify. — Gk. κοσμητικός, 'skilled in arranging', fr. κοσμητός, 'well-ordered', verbal adj. of κοσμεῖν, 'to order, arrange, adorn', fr. κόσμος\\\"\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat p.97 s.v. Cosmic\", \"stance\": \"partial\", \"note\": \"Skeat gives κόσμος but has no separate entry for cosmetic/cosmétique\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Persian\",\n          \"words\": \"mâtîk «ماتیک»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian ماتیک mātik 'lipstick' is a clipping of French cosmétique: Dehkhoda's entry states it outright — ماتیک is 'از فرانسه، مخفف cosmétique فرانسوی', tracing it further back to Greek κοσμητικός and defining cosmétique as the preparations used for the freshness and beauty of skin and hair. The Persian form keeps only the last two syllables of [kɔs.me.tik], with the loss of the initial syllable (a common fate of long European loans in colloquial Persian) and the regular lengthening of the stressed vowel to ā: cos-mé-tique > mā-tik. Mo'in tags it [فر.] 'French' and defines it 'از انواع لوازم آرایش که با آن لب‌ها را رنگ کنند، روژ لب', i.e. the meaning narrowed from 'cosmetic in general' to 'lip colour' specifically. Nourai's arrow French cosmétique → Persian mâtîk is therefore exactly what the Persian lexicographers say.\",\n          \"derivation_fa\": \"«ماتیک» کوتاه‌شدهٔ واژهٔ فرانسوی cosmétique است. دهخدا صریحاً می‌نویسد که ماتیک «از فرانسه، مخفف cosmétique فرانسوی» است و آن را تا κοσμητικός یونانی پی می‌گیرد و «کسمتیک» را داروهایی می‌داند که برای طراوت و زیبایی پوست و گیسو به کار می‌رود. در فارسی تنها دو هجای پایانی ‎[me.tik]‎ نگاه داشته شده و هجای آغازین افتاده است — سرنوشتی که بسیاری از وام‌واژه‌های بلندِ اروپایی در گفتار فارسی یافته‌اند — و واکهٔ تکیه‌بر به «ا» کشیده بدل شده است: cos-mé-tique ← ماتیک. معین آن را با نشان «فر.» می‌آورد و چنین معنی می‌کند: «از انواع لوازم آرایش که با آن لب‌ها را رنگ کنند، روژ لب»؛ یعنی معنا از «فرآوردهٔ آرایشی» به‌طور کلی، به «سرخابِ لب» تخصیص یافته است. پس پیکان نورایی از cosmétique فرانسوی به «ماتیک» فارسی درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D9%85%D8%A7%D8%AA%DB%8C%DA%A9/\",\n            \"https://www.jadvalyab.ir/moein/%D9%85%D8%A7%D8%AA%DB%8C%DA%A9\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"VOP:321\", \"status\": \"not_checked\", \"note\": \"Moshiri, Farhang-e Vāžehā-ye Orupāyi dar Fārsi — refs_online.json records kind 'none': no copy found on archive.org, ketabnak or noorlib\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in via jadvalyab.ir/moein/ماتیک and abadis.ir\", \"stance\": \"supports\", \"note\": \"origin tag [فر.]; 'از انواع لوازم آرایش که با آن لب‌ها را رنگ کنند، روژ لب'\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate'\", \"stance\": \"silent\", \"note\": \"a 17th-century dictionary of classical Persian; it can contain no 20th-century French loan such as ماتیک\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Riše-hā-ye Hend-o-Orupāyi\", \"stance\": \"silent\", \"note\": \"grep of ARY_pages.txt finds no ماتیک entry — the book treats inherited Indo-European vocabulary only\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"cosmetic\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English cosmetic as a noun appears c.1600 from Latinised Greek kosmetike (tekhne) 'the art of dress and ornament'; as an adjective it is taken in the 1640s from French cosmétique (16th c.), which is Nourai's route. The figurative sense 'superficial, affecting appearance only' is first recorded in 1955. The word is a learned Renaissance borrowing, so it shows no native English sound development, only the substitution of -ic for French -ique. Klein confirms the same chain via κοσμητικός < κοσμητός < κοσμεῖν < κόσμος.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی cosmetic در جایگاه اسم حدود سال ۱۶۰۰ از صورت لاتینی‌شدهٔ یونانی kosmetike (technē) «هنر آرایش و پیرایش» گرفته شده و در جایگاه صفت در دههٔ ۱۶۴۰ از cosmétique فرانسوی وارد شده است — یعنی همان راهی که نورایی رسم کرده است. معنای مجازی «سطحی، ظاهری» نخستین‌بار در سال ۱۹۵۵ ثبت شده است. این واژه وام‌واژه‌ای دانشورانه از دورهٔ رنسانس است و هیچ تحول آوایی بومیِ انگلیسی در آن دیده نمی‌شود؛ تنها پایانهٔ فرانسوی ‎-ique‎ به ‎-ic‎ انگلیسی بدل شده است. کلاین نیز همین زنجیره را از κόσμος تا κοσμεῖν و κοσμητικός تأیید می‌کند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/cosmetic\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:301\", \"status\": \"supports\", \"note\": \"p.301 of the 1976 AHD is the dictionary page for cosmetic; the AHD entry gives \\\"[French cosmétique, from Greek kosmētikos …]\\\", exactly the French→English step drawn here\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.360 s.v. cosmetic\", \"stance\": \"supports\", \"note\": \"\\\"cosmetic, adj., serving to beautify. — Gk. κοσμητικός, 'skilled in arranging', fr. κοσμητός … fr. κόσμος. See cosmos and -ic.\\\"\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"silent\", \"note\": \"grep for 'cosmetic' in SKT.txt returns no headword; Skeat has only Cosmic\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"English\",\n          \"words\": \"cosmos, cosmic\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English cosmos is the Latinised Greek κόσμος 'order, good order, orderly arrangement', known in English from c.1200 but popularised in 1848 as the title of the English translation of Humboldt's Kosmos; cosmic is Greek κοσμικός 'of or connected with the world', through Latin cosmicus. As direct learned borrowings they involve no sound change beyond Latin orthography and the English -ic suffix. The English step drawn here is uncontroversial; the doubtful link in this branch is the one above it (node #9, Greek ← Indo-European), not this one. Nourai's bare 'AHD' reference is the appendix in general.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی cosmos همان κόσμος یونانی است به صورت لاتینی‌شده، به معنای «نظم، سامان، آرایشِ سنجیده»؛ از حدود سال ۱۲۰۰ در انگلیسی شناخته بوده اما رواج امروزی‌اش از سال ۱۸۴۸ و از عنوان ترجمهٔ انگلیسی کتاب «کُسموس» اثر هومبولت است. cosmic نیز از κοσμικός «مربوط به جهان» از راه cosmicus لاتین آمده است. چون هر دو وام‌واژهٔ کتابی و مستقیم‌اند، هیچ دگرگونی آوایی بومی در آن‌ها رخ نداده و تنها املای لاتینی و پسوند انگلیسیِ ‎-ic‎ افزوده شده است. این حلقه از زنجیره بی‌چون‌وچرا درست است؛ حلقهٔ مشکوک، حلقهٔ بالاتر است (گرهٔ ۹: یونانی ← هندواروپایی).\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/cosmos\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 does give COSMOS (with MACROCOSM, MICROCOSM) — but under the root kes-³ 'to order', not under kens-; the index reads \\\"cosmos kes-3\\\". The English words are covered by AHD; the root assignment Nourai draws is not.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 pp. 360-361 s.vv. cosmos, cosmic\", \"stance\": \"supports\", \"note\": \"\\\"cosmic, adj., pertaining to the cosmos; vast. — Gk. κοσμικός, 'of, or connected with, the world', fr. κόσμος, 'world'\\\"; the cosmos entry adds 'of uncertain origin' for the Greek word itself\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat p.97 s.v. Cosmic\", \"stance\": \"supports\", \"note\": \"\\\"Cosmic, relating to the world. (Gk.) Gk. κοσμικός, adj., from κόσμος, order, also the world, universe\\\"\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 index p.1394\", \"stance\": \"partial\", \"note\": \"\\\"cosmos kes-3\\\" — the English word is in the appendix, but under a different root\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-255.json > /dev/null && echo \"JSON OK\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 255"
}
```


### [2026-09-06T16:26:02.046Z] TOOL RESULT

```
JSON OK
nodes verified: 13/13
node verdicts: {'confirmed': 9, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 9, 'not_checked': 4, 'contradicts': 1, 'partial': 3}
books consulted: {'supports': 24, 'partial': 5, 'silent': 9, 'contradicts': 3} | by book: {'KLN': 8, 'SKT': 7, 'WLD': 4, 'ARY': 3, 'AHD': 3, 'BRT': 2, 'IEC': 2, 'PHD': 2, 'POK': 2, 'MON': 2, 'SYN': 1, 'HUB': 1, 'NYB': 1, 'HRN': 1, 'BOOK': 1, 'BQT': 1}
```


## [2026-09-06T16:26:09.503Z] TOOL CALL #80: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-255.json'\ns=open(p,encoding='utf-8').read()\nold='کلاین آن را «with نامعلوم‌الاصل» می‌داند'\nnew='کلاین آن را «نامعلوم‌الاصل» می‌خواند'\nassert old in s\nopen(p,'w',encoding='utf-8').write(s.replace(old,new))\njson.load(open(p,encoding='utf-8'))\nprint('ok')\nEOF\npython3 tools/verify_check.py 255"
}
```


### [2026-09-06T16:26:12.425Z] TOOL RESULT

```
ok
nodes verified: 13/13
node verdicts: {'confirmed': 9, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 9, 'not_checked': 4, 'contradicts': 1, 'partial': 3}
books consulted: {'supports': 24, 'partial': 5, 'silent': 9, 'contradicts': 3} | by book: {'KLN': 8, 'SKT': 7, 'WLD': 4, 'ARY': 3, 'AHD': 3, 'BRT': 2, 'IEC': 2, 'PHD': 2, 'POK': 2, 'MON': 2, 'SYN': 1, 'HUB': 1, 'NYB': 1, 'HRN': 1, 'BOOK': 1, 'BQT': 1}
```


## [2026-09-06T16:26:31.132Z] AGENT

Page 255 (book p. 225), single entry, root **Kens** — written to `/home/sfmqrb/git/rishe/data/verification/page-255.json`; `verify_check.py 255` reports 13/13 nodes, 0 PROBLEM lines.

**Verdicts:** root confirmed; nodes 9 confirmed, 3 plausible, 1 transcription_suspect.

**Root:** POK:566 and WLD1:403 both check out verbatim (`kens- „feierlich sprechen, verkündigen"` / `„…autoritativ verkündigen"`) — gloss and label exact.

**Flagged items**
- `#6 [French] censur` — **transcription_suspect, error_in: book**. No such French word; it is `censure` (< L. *censura*), or `censeur` for the gloss 'censor'. Rendered pdf p.255 at 600 dpi: the page itself prints "censur : censor", so the extraction is faithful. Page PNG copied to `data/verification/sources/refs/ocr/BOOK/255.png`.
- `#2 [Persian] soxan` — **plausible**. Root right, parent wrong: Hübschmann §99/§108 says NP *suxan* is from Iranian \*saxvan- (= OP \*θa(h)uvan-), i.e. it cannot descend from the θ-dialect `thah` drawn as its parent; MP *saxwan* (MacKenzie p.74) is the missing step. The chart's own NOTE ("see Kâs 2") is answered: modern work keeps *soxan* with \*ḱens-.
- `#4 [Persian] afsâneh` — **plausible**. IEC:608 supports it outright ("Ḱensos … Per. cf. fa-sāna 'fable'"), MP *afsānag*; downgraded only because the prefix is unexplained and Wiktionary records an alternative (\*ḱen- 'empty').
- `#9 [Greek] kos-mos etc.` — **plausible**, and Nourai's own hedge is warranted. WLD I 403 (the very page he cites for the root) explicitly rejects it: "In der Bed. kaum vereinbar ist gr. κόσμος"; Pokorny 566 omits it; Klein "of uncertain origin"; **Watkins/AHD puts *kosmos* under a separate root `kes-³`, so his ref AHD:1522 contradicts** (marked as such). Only Wiktionary (citing Beekes 2010) supports \*ḱóns-mo-.

**Refs not checkable:** TZF:19 (Abolghasemi — no open copy), VOP:210 and VOP:321 (Moshiri — `kind: none` in refs_online.json). Node #11 *mâtîk* was instead confirmed from Dehkhoda, which states it is "از فرانسه، مخفف cosmétique فرانسوی".

**No extraction errors** on this page — the JSON matches the printed chart everywhere, including "censur" and the Latin `cĕns-ĕre` (the book prints both breves; Latin has *cēnsēre*, noted in the derivation as the author's habit, not a data fault). 11 web pages archived via `fetch_source.py`.
