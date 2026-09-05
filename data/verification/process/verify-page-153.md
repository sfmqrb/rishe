# Verification process log — verify-page-153


## [2026-09-05T20:26:19.644Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 153 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-153.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-153.json. Write /home/sfmqrb/git/rishe/data/verification/page-153.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 153` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:26:20.911Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:26:21.743Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:26:21.758Z] TOOL RESULT

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


## [2026-09-05T20:26:22.284Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-153.txt"
}
```


### [2026-09-05T20:26:22.304Z] TOOL RESULT

```
1	=== PDF page 153 (book page 123) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Embhi : honey, honey bee  (refs POK:311; WLD1:125)
4	#1 (parent #0) [Avestan] refs=SOD:42 | ang, angu : honey ; angu-paěna : sweet sap ☞Peî
5	  #2 (parent #1) [Pahlavi] refs=WLD1:125 | ang, angubin : honey
6	    #3 (parent #2) [Persian] refs=BQT:174; HRN:254 | ang «انگ ۲» : honey | extra: انگبین ، سکنجبین ، گزانگبین ، انغوزه
7	#4 (parent #0) [Sogdian] refs=SOD:42 | `nkwpyn : honey
8	#5 (parent #0) [Sanskrit] refs=POK:311 | hingu : resin
9	  #6 (parent #5) [Sogdian] refs=SOD:87 | inku, `ynkw : resin
10	#7 (parent #0) [Latin] refs=WLD1:125 | apis : bee
11	  #8 (parent #7) [English] refs=KLN:89 | apiary, apiology
12	#9 (parent #0) [Greek] refs=POK:311 | ampis : honey
13	--- entry 1 ---
14	ROOT [Indo-European] Ěmos : a suffix meaning most or last  (refs IEC:257)
15	#1 (parent #0) [Avestan] refs=IEC:257 | -emô : most or extreme
16	  #2 (parent #1) [Persian] refs=IEC:257 | -om «-ُم» : a suffix indicating the order of a number | extra: دوّم ، چهارم ، پنجم
17	#3 (parent #0) [Latin] refs=IEC:257 | -imus ; inf-imus : lowest ; post-omus : lowest ; max-imus : maximum ; min-imus : minimum
18	  #4 (parent #3) [English] refs=AHD | maximum ; minimum
19	
```


## [2026-09-05T20:26:25.383Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-153.json",
 "description": "Read source JSON page 153"
}
```


### [2026-09-05T20:26:25.421Z] TOOL RESULT

```
{
  "pdf_page": 153,
  "book_page": 123,
  "entries": [
    {
      "root": {
        "name": "Embhi",
        "lang": "Indo-European",
        "refs": "POK:311; WLD1:125",
        "gloss": "honey, honey bee"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "SOD:42",
          "words": [
            {"translit": "ang, angu", "gloss": "honey", "script": null},
            {"translit": "angu-paěna", "gloss": "sweet sap", "script": null, "see": ["Peî"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "WLD1:125",
          "words": [
            {"translit": "ang, angubin", "gloss": "honey", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:174; HRN:254",
          "words": [
            {"translit": "ang", "gloss": "honey", "script": "انگ ۲"}
          ],
          "script_extra": "انگبین ، سکنجبین ، گزانگبین ، انغوزه",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:42",
          "words": [
            {"translit": "`nkwpyn", "gloss": "honey", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:311",
          "words": [
            {"translit": "hingu", "gloss": "resin", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Sogdian",
          "refs": "SOD:87",
          "words": [
            {"translit": "inku, `ynkw", "gloss": "resin", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "WLD1:125",
          "words": [
            {"translit": "apis", "gloss": "bee", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": "KLN:89",
          "words": [
            {"translit": "apiary, apiology", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:311",
          "words": [
            {"translit": "ampis", "gloss": "honey", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ěmos",
        "lang": "Indo-European",
        "refs": "IEC:257",
        "gloss": "a suffix meaning most or last"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "IEC:257",
          "words": [
            {"translit": "-emô", "gloss": "most or extreme", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "IEC:257",
          "words": [
            {"translit": "-om", "gloss": "a suffix indicating the order of a number", "script": "-ُم"}
          ],
          "script_extra": "دوّم ، چهارم ، پنجم",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "IEC:257",
          "words": [
            {"translit": "-imus", "gloss": null, "script": null},
            {"translit": "inf-imus", "gloss": "lowest", "script": null},
            {"translit": "post-omus", "gloss": "lowest", "script": null},
            {"translit": "max-imus", "gloss": "maximum", "script": null},
            {"translit": "min-imus", "gloss": "minimum", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "maximum", "gloss": null, "script": null},
            {"translit": "minimum", "gloss": null, "script": null}
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


## [2026-09-05T20:26:26.146Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:26:26.221Z] TOOL RESULT

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


## [2026-09-05T20:26:36.049Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && python3 -c \"\nimport json;d=json.load(open('data/verification/page-152.json')) if __import__('os').path.exists('data/verification/page-152.json') else None\nprint(bool(d))\""
}
```


## [2026-09-05T20:26:37.300Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','SOD','BQT','HRN','IEC','KLN','AHD','MON','ARY','PHD','BRT']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600]); print()\n\""
}
```


### [2026-09-05T20:26:37.765Z] TOOL RESULT

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
page-129.json
page-130.json
page-131.json
page-133.json
page-135.json
page-137.json
page-138.json
page-146.json
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
----
False
```


### [2026-09-05T20:26:39.546Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
```


## [2026-09-05T20:26:43.544Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==319||NR==320' POK_01.txt | head -80"
}
```


## [2026-09-05T20:26:44.889Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"embh\" POK_full.txt | head -30; echo ====; grep -n \"hiṅgu\\|hingu\" POK_full.txt POK_01.txt | head -20"
}
```


### [2026-09-05T20:26:45.509Z] TOOL RESULT

```
.  elteur)  »feuchte Niederung'.  Dazu  altnord.  Uldna  ,schimmeln',  ahd.  oltar  »Schmutzkrume*, wohl  auch  anord.  ylda  »Moderduft*.
zn-Formantien  finden  sich  in:
norw.  dial.  ulma  .schimmeln'»  ndd.  ostfries.  olm,  ulm  »Fäulnis,  bes.  im Holz*,  mnd.  ulmich  ,von  Fäulnis  angefressen',  mhd.  ulmic  ds.;  lit.  elmes, almens  »die  aus  der  Leiche  fließende  Flüssigkeit*.
^^-Erweiterung  liegt  in  arm.  alb  »Dreck'  vor.
WP.  I  152  f.,  WH.  I  28  f.»  Petersson  Heterokl.  165  f.
20
306  s
f     .  ■     i
4.  el-,  ol'  Schallwurzel.  •
Arm.  almuk  ,Lärm,  Aufruhr  usw.*  (*lmo-),  alavC-lh  ,Flehen*,  olb  »Klao-^t  I ololh  , inständige  Bitte';  *  .    f
gr.  ololvg  , Heuler,  weibischer  Mensch',  öXolvyr}  , Klagegeschrei*,  ölom^^      \ v6g  »jammernd',  dlocpvQo^ai  ,jammere';  vielleicht  auch  k'lsyog  n.  , Klagelied« elsog  m.,  später  n.  , Mitleid';
asl.  jahnr^  ,Lärm',  jalma    ,strepere,    Stridore,    crepare',   norw.    mdartl jalm^  jelm  , Schall',  schwed.  mdartl.  jalm  , Schrei,  Mißlaut*;  norw.  mdartl alka  , Händel  anfangen*,  ostfries.  ulken  »Unwesen  treiben,  schreien,  spottea    •''•• höhnen'  (nhd.  ulken),  schwed.  dial.  alken  ,zu  knurren  anfangen';  /•■^r
lit.  nualdeti  »erschallen',  algöti  , zusammenrufen,  nennen';
vielleicht  gehören  auch  die  Namen  für  Wasservögel  von  einer  Wz.  el hierher  (doch  s.  S.  304);  etwas  verschieden  ist  der  Gefühlswert  von  uU,
WP.  I  153  f.,  Pisani  Armen.  8  f.
5.  el-,  Ol-  , vernichten»  verderben'??
Arm.  eiern,  Gen.  eiefan  »Unglück*;  olorm  , unglücklich*;
gr.  b'llvuL  , verderbe'  (*ol-vv-(i.L),  Fut.  dXeao),  Perf.  dX(bXsY.a  (älter  intrans] ^lü)Xa)  usw.,  nach  Schwjzer  Gr.  Gr.  I  747  dl-  statt  *il~  nach  dem  Kausat*^ *dX6w',  öle/.iü  , vernichte*,  iJXs&gog  m.  , Verderben*;
nach  Loth  (RC  40,  371)  hierher  mbret.  el-hoet , Hunger'  (zu  hoet  ,Nahrung').  "^j bret.  (Vannes)  ol-huid  , Nahrungsmaugel',  ol-argant  , Geldmangel'  usw.^'^ vielleicht  auch  air.  el-tes  ,lauwarm'  {tes  , Hitze');
über  lat.  aboleö  s.  WH.  I  4 f.;  ob  el-  den  Wurzeln  elg-,  elk-  zugrunde' liegt?
eventuell  hitt.  hu-ul-la-a-i  »er  besiegt,  vernichtet*,  Couvreur  g  134 L/ anders  Hendriksen,  Laryngaltheorie  27»  47.  :\
WP.I159f.»  Schwyzer  Gr.  Gr.  1361,  363,696,  747,  Petersson  Heterokl.  159.
6.  el-,  elQ-ilä-]  el-eu-(dh')  , treiben,  in  B
ewegung  setzen;    sich  bewegen,
gehen'.
Arm.  eianim  ,ich  werde',  Aor.  1.  Sg.  eU  (*ehi),  2.  Sg.  ehr,  3.  Sg.  eieu-, elanem  ,ich  steige  hinauf,  komme  heraus',  3.  Sg.  Aor.  el;  dazu  eluzi  ,j'ai fait  monter'  (*el-ou-ghe-),  danach  eluzanem  ,je  fais  sortir';
gr.  ila-  im  Imper.  koisch  iXdrw,  Fut.  iXävTc  {*£XaovTt)y  Aor.  iXdaavrsg und  poet.  iXdco  , treibe';  suppletiv  zu  &/o)  (s.  unten  kelt.  el-),  Fut.  att.  iXßf Aor.  IrjXaaa;  meist  äXavvio  ,treibe,  fahre'  (von  einem  Nomen  *^Xa-vv-ogy Brugmann  Grundriß  H,  1,  321);
mit  dh-Erweiterung  , kommen' :  Aor.  '^Xdov  (aus  ^Xvd'Ov)^  daraus  dor.  ustv. 'ijv&ov]  Perf.  hom.  elXrjXov&a,  att.  iXrjXv&cc]  Fut.  ion.  iXsucrof^ai]  über  Perf. iXrjXvf.isv  (*elu-),  Adjekt.  Ttgoa-i^XvTog  »einer,  der  kommt',  e'ftrjXvg,  -vöog  ds.^ s.  Schwyzer  Gr.  Gr.  I  704 2,  769^;
307
man  stellt  noch  hierher  iallu)  ,schicke,  werfe'  (*i-J-iö),  Aor.  hom.  ^Xa, dor.  t'ß^«  (Schwyzer  Gr.  Gr.  I  648,  717);  aber  ai.  lyarti  ,er  erregt'  gehört eher  zu  1.  er--^
air.  lu^d  ,ging'  (*hidh-e),  3.  PI.  lotar  {Hudh-ont-r)]  wie  im  Gr.  wird i,n  Kelt.  ag-  , treiben'  durch  el-  suppliert,  womit  aber  zum  Teil  auch  die ^Vurzel  'pel-  ,pellö'  (s.  dort)  zusammengefallen  ist,  so  gewiß  im  air.  Fut. thlaid  ,wird  treiben'  (aus  *pi-plä-s.e-ti),  Fut.  sek.  di-eblad  , würde  entreißen'; gl-  erscheint  im  Brit.  nur  im  Konjunktiv:  Fräs.  l.  Sg.  mcymr.  el{h)wyf, 3.  Sg.  el,  Corn.  1.  Sg.  yllyf,  3.  Sg.  ello,  mbr.  3.  Sg.  me  a  y-el  ,ich  werde crehen*  (das  y  ist  hiatustilgend ;  Ih  und  II  gehen  auf  ^4-intervok.  s  zurück); vielleicht  hierher  die  gall.  FIN  Elaver  >  Elaris  >  frz.  Allier  {*eb-uer-  : *eld-iten-,  s.  oben  ilavvw)  und  Elantia  >  nhd.  Elz]
vielleicht  dazu  als  no-Partizip  (??)  ags.  lane,  -u  f.  , Gasse,  Weg',  anord. l^n  , Häuserreihe',  usw.  Über  anord.  elta  , drücken,  verfolgen,  forttreiben' i*alatjan?)  s.  Falk-Torp  m.  Nachtr.
\VP.  I  155  f.,  Meillet  BSL.  26,  6  f.,  Schwyzer  Gr.  Gr.  I  213,  507,  521  ^ G81f.
p  eh  elQ-,  mit  -ic-Er Weiterung  elk-,  elak-  , hungrig,  schlecht'  (?).
Air.  elc  ,böse'  (aber  olc  ds.,  Gen.  uilc  setzt  *ulko-  voraus!);  über lat.  ulciscor  s.  unter  elkos-]
vielleicht  anord.  illr  ,böse'  (*elhila-)-
lit.  dlkti,  lett.  alkt  (daneben  s-alkt)  , hungern'  (*ohk-),  apr.  alklns,  lit. dlkanas  ,nüchtern';
aksl.  lacg  und  ahcg,  lakati  und  ahkati,  sloven.  Idkati  , hungern',  cech. lakati  ,verlangen',  wo  der  Stamm  slav.  *ölka  aus  dem  Präter.  stammt; dazu  die  Adjektiva  aksl.  lahm,  ahchm,  cech.  lacny  , hungrig'  und  aksl. lakorm  , hungrig',   cech.  lakomy  , gierig',  usw.
WP.  I  159  f.,  Trautmann  6  f.
I.  el;  elei-y  lei-  , biegen';  olinä  , Ellenbogen*.
A.  Hierher  stellen  sich  zunäch
```


### [2026-09-05T20:26:45.564Z] TOOL RESULT

```
Exit code 1
(eval):1: === not found
```


## [2026-09-05T20:26:51.783Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"embh\" POK_full.txt | head -30; echo \"====\"; grep -n \"hi.gu\" POK_full.txt | head -20"
}
```


### [2026-09-05T20:26:51.844Z] TOOL RESULT

```
====
```


## [2026-09-05T20:26:52.752Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls; echo \"====\"; wc -l POK_full.txt 2>/dev/null"
}
```


### [2026-09-05T20:26:52.855Z] TOOL RESULT

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
====
93771 POK_full.txt
```


## [2026-09-05T20:26:56.212Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^.\\{0,80\\}311\" POK_full.txt | head -20; echo \"==== head\"; head -40 POK_full.txt"
}
```


### [2026-09-05T20:26:58.242Z] TOOL RESULT

```
1545:References: WP. I 177, Feist 1 b f., 579 a., W. Schuize KZ. 52, 311 = Kl. Schr. 398. 
1572:References: WP. I 177, Feist 1 b f., 579 a., W. Schuize KZ. 52, 311 = Kl. Schr. 398. 
5146:Pedersen KZ.38, 311; 39, 402, Vondrak SI. Gr. I 184, Adontz Mel. Boisacq I 10, as well as 
26199:Page(s):311 
26251:Page(s): 310-311 
26858:Page(s): 311-314 
32129:References: WP. I 555 ff., WH. I 112 f., 311, 629, 852, Trautmann 80, 100 f. 
52186:References: WP. I 471, Trautmann 311, W. Schuize Kl. Schr. 366. 
61623:References: WP. 11311; after Hubschmid ZnPh. 66, 33 f. not Indo Germanic 
61704:References: WP. II 311, WH. II 133, Trautmann 191, Specht Indo Germanic Dekl. 43. 
65448:References: WP. II 73 ff., WH. 211 f., 306, 308, 311, 312, Trautmann 207 f., 210, 217. 
92416:gawizneigs' s\c\\ mitfreuend'. Old English tvesa/? 'to feast' (only Beowulf 3115, Hs. 
92616:References: WP. I 311, WH. II 770 f., 814 f., Trautmann 348, Vasmer 1, 196, Frisk 575; 
92824:References: WP. 1311, Vasmer 1 , 191 f.. Frisk 594 f. 
==== head
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk. 




Akkadian 


Alan. 




Alanian (=Old Ossetic) 


Alb. 




Albanian 


Anat.
```


## [2026-09-05T20:27:00.554Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26150,26290p' POK_full.txt"
}
```


### [2026-09-05T20:27:00.704Z] TOOL RESULT

```
Burushashki 

Hunza h\k, Yas/nhek 

Etruscan 

Etruscan+ thu(n) 

Semitic 

East: Akkadian+ ishte:n, Central: Arabic wa:hid, Kashka-Darya iad, Saudi \Naah\d, 

Yemen/ v\/aah\d, Syrian ^a.hed, Lebanese ^ahad, Cypriot Texen, iraqi\Naah\d, Egyptian 

wa:hid, E Libyan '^ahad, N African (Darja) ^a.hed, Moroccan ^ahed, Sudanese \Naah\d, 

Nigerian \Na:\\\d, Zanzibari\Na:\\\, Maltese wieh=ed, Phoenecian+ '-h-d, Ugaritic+ ahd; 

Moabite+: Classical Hebrew+ 'ahat, Modern Hebrew 'axat, Classical Aramaic+ xadh, 

Modern Aramaic ahad, Classical Syriac+ hadh, Syriac kha, Vanhe; 

South: Old S. Arabian+ '-h-d, South Arabian (l-iarsusi) \:a:d, fSheriJ i'ad, So co tra i' ad; 

N Ethiopia Geez+ ?ah=adu, Tigre worot, Beni Amir orot, Tigrinya hade; 

S Ethiopia. Amharic and, Argobba hand, Harari ahad, E Gurage ad, Gafat+ ajja, Soddo att 

Goggot quna, Muher at, Masqan at, CW Gurage at, Ennemor Attic 

References: WP. I 95 ff., WH. I 368 f., 399 f., 409, 671 , 720 ff., 869, Trautmann 3, 65, 72, 
1 05, Schwyzer Gr. Gr. I 548, 588, 608, 61 3 f., 628 f., 651 . 
Page(s): 281-286 



Root / lemma: errto'"/-, empi- 
Meaning: a kind of mosquito or bee 
Note: With taboo variation b^ : pi 
Material: Gr. spnic;, -i5oq 'a mosquito '; 



Old High German //77i6'/ (oldest evidence impi pTano), Middle High German imbe {* embi- 
o) "swarm of bees, beehive', previously late-Middle High German "bee'. Modern High 
German Imme, changing through ablaut Old English imbe{*umbia) "swarm of bees'. 

References: WP. I 125, WH. I 57. 
Page(s):311 

Root / lemma: em-, em-{*huem-) 

Meaning: to take 

Grammatical information: originally athematisches present 

Material: Latin emo, -ere, e/77/"(Lithuanian emiau), emptum{= Lithuanian iifitas. Old 

Prussian /mtat. Old Bulgarian yi^/fc) "take (only in compounds), buy'. 

Maybe zero grade in alb. marr' take' < Lat emere " take'. 

Oscan pert-emesV to take away entirely, annihilate, extinguish, destroy, cut off, hinder, 

prevent ', pert-emusV taken away entirely ', per-emusf has taken wholly, seized entirely, 

taken possession of, seized, occupied ' (to Perf. *emed), pert-umum 'shaW take away 

entirely, annihilate, extinguish, destroy, cut off, hinder, prevent ' (assil. from * pertemom); 

Umbrian emantu{i) "be taken without effort, received, got, accepted ' emps^ taken out, 

taken away, removed '; 

Old Irish em- in ar-fo-em-^iake, receive ', verbal noun airitiu{: Latin emptid, Lithuanian 
is-imtis^ exception '), dT-em-^ shield ', etc.; 

Lithuanian imu, preterit emiau, /mf/"take'. East Lithuanian present ye/77Z/, Old Prussian 
//77/ds.; Labj\anJ^mu,Jemu,Jemtan6jemt, besides hemu, hemu, /fe/??/ (probably through 
contamination an equivalent originated from Gothic n/man^take', Endzelin, Latvian Gr. 
564); 

Old Church Slavic img{bmg, compare vbz-mg' take away ', etc.) yl?// "take' (perfective), 
besides imperfect: ye/77/p, /mat/ds., and as "have': stative verb imamt, imejq, imeti {*ema-, 
*eme-); 

besides Indo Germanic em- formant the rhyme rooisjem- and nem-, probably originally 
different and only secondary now and then adapted; 

Hittite u-e-mi-Ja-mi {u-emijamRl) "I catch, find', Pedersen Hittite 82'', 135. 

Note: 



The origin of labialized Old laryngeals: similar to Hittite huek-, huk- " adjure ', Tocharian A 
wak\., B M/e/r "voice'. 

References: WP. I 124 f., WH. I 400 ff., 862; Trautmann 103 f., Meillet Slave communs 80, 
203 f., EM2 300f. 
Page(s): 310-311 

Root / lemma: {endo^-f), errt^-, orrt^-, ndo^-{n§o^-?), ixb^-{* hen-nto^el-) 

Meaning: navel 

The initial laryngeal was transaformed into a vowel which was immediately nasalized. 

Note: plural with Aformant. 

Material: Old Indie [nasalized * h2anmbhya] nabhya-u. "hub", nabhi-i. "navel, hub, kinship', 

nabhTla-v\. (uncovered) " pubic region, navel dent'; Avestan naba-nazdista- " der 

verwandtschaftlich nachststehende ', besides with Aryan ph: Avestan nafo, npers. naf 

"navel'; 

gr. 6|j(paA6(; (Nom. PI. also b\x(^aKz(^) "navel, shield boss ', probably also 6|j(paK£(; " the 
unripe grapes or olives or other fruit ' (als nabelartig vorgestijlpte Knopfchen), 6|j(paKi(; " 
cup of the acorn of Valonia oak, used for tanning, and as an astringent medicine'; 

Maybe zero grade in alb. mbulonj^ coyer, shield, protect'. 

Latin umb/7/cus 'naveV, umbo, -on/s' a swelling, rounded elevation, knob, shield boss '; 

The origin of labialized Old laryngeals: 

common Armenian Celtic *bue- > gw- > g- ; Old Prussian Lithuanian Tocharian gw- > w-, 
V-, Latin gw- > u-. 

Old Irish imbliu^uayey {*embildn-). Middle Irish imlecan6s. (an attempt to the suffix 
explanation by Pedersen KG. I 495); 

Old High German naba. Old English nafu. Old Icelandic /?(?/" hub of a wheel' (also in Old 
High German naba-ger. Old English nafu-gar. Old Icelandic /7a/^/r"grober borer'). Old 
High German nabalo. Old English nafela. Old Icelandic nafl/'naveV; in addition after Liden 
KZ. 61, 17 Old High German amban, ambon, m. (ostem) "paunch'. Old Saxon ambon' 
the belly, abdomen ', Nom. Akk. PI. m. o/7-stem (Germanic * amban-, Indo Germanic 
* orrid^on-);
```


## [2026-09-05T20:27:26.324Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- WLD Bd1 p125 (leaf?)\"; grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd1_pages.txt | head -3; echo \"--- grep apis in WLD Bd1\"; grep -n \"apis\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20"
}
```


### [2026-09-05T20:27:26.394Z] TOOL RESULT

```
--- WLD Bd1 p125 (leaf?)
--- grep apis in WLD Bd1
1819:483). Der Einfall, dafi Kreuzung mit einem zu lat. apis gehorigen upilys vorliege, fit 
3127:Lat. apiscor „fasse, erreiche“, adipiscor „erlange“, coepi „habe ange- 
8151:Uber np. any „Biene“ und lat. apis „Biene“ (beide dunkel) s. noch Boi- 
8152:sacq 248, Vf. LEWb. 2 u. apis (letzteres nicht nacli Ilolthausen IF. 35, 132 
11356:35, 132) lat. apis „Biene‘‘ (sei gegentiber der Drohne, f ileus, als ,,Arbeits- 
21624:„von einem GefaB ins andere schopfen"), capistrum „Schlinge zum Fassen 
21626:aber capis, -idis „Henkelschale“, umbr. ka/iife „capide“, osk. xamdixop 
21628:(Froehde BB. 1, 185, vgl. auch KZ. 13, 452; sicher ist capisterium Lw. aus 
21722:309, Solmsen Beitr. 196, Vf. LEWb. 2 u. capis, capsa. 
21941:ziehung von np. capis „einjahriger Bock a (Uhlenbeck PBrB. 19, 330) spricht 
21944:sca/‘„Schaf“ unter idg. *sgep- : *sqcb-, z. B. Fick III 4 451 ; ob capis Beziehung 
33467:haltnis aptus : apiscor).
```


## [2026-09-05T20:27:27.362Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD nkwpyn\"; grep -n \"nkwpyn\\|nkwpn\\|ynkw\\|inku\" SOD_pages.txt | head -20; echo \"=== SOD honey\"; grep -n \"honey\" SOD_pages.txt | head -20"
}
```


### [2026-09-05T20:27:27.447Z] TOOL RESULT

```
=== SOD nkwpyn
3215:  angust      B ynkwst;    finger        Av. angusta-
6750:1041 *ngwpyn        M =¥ 'nkwpyn
6812: 1066 'nkwpyn      B, S                               ^i
8455:                                                                    1627 'spn'ynkwc'k     B                           jUo^T
10120: 2189 >ync C, B, S                                           jj     2201 >ynkw B                  (^\ ijJ^\)^\ ^^
10121:                                                                         inku ©<Skt. hingu, MP angu
10125:        STi 36.15, 83.13; Sund. AoFviii 1981 p213; C2               2202 'ynkwmync         B                                ^..^
10126:                                                                         inkumenc
12694:            Frag. Len.; MDii, cynkw, Tales. 475.15                     GMS 459; BSTi 227, 228; MDii
=== SOD honey
6817:      honey                 4                                       Go)faII
38501:health 2152,3609,3613,3614,            heretical   346, 358, 7725, 7752       honey       1066
```


## [2026-09-05T20:27:35.901Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=6700 && NR<=6830' SOD_pages.txt | grep -n \"pdf page\" ; echo \"---\"; awk 'NR<=6812' SOD_pages.txt | grep -n \"pdf page\" | tail -3; echo \"--- around 10120\"; awk 'NR<=10121' SOD_pages.txt | grep -n \"pdf page\" | tail -3"
}
```


## [2026-09-05T20:27:37.023Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8140,8160p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt; echo \"=======\"; sed -n '11340,11370p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-05T20:27:37.575Z] TOOL RESULT

```
---
--- around 10120
```


### [2026-09-05T20:27:37.634Z] TOOL RESULT

```
Liden Stud. 73 f. wegen der iiltern germ. Bed. „Schwarm von Bienen“; er 
vereinigt imbi, ymbe mit air. imbed acvmr. immet „Fulle, Menge“ unter einem 
*embh- „Fiille, Menge“ (aber lat omnis und gr. dcpevog sind keine Stiitze 
fiir eine solche Wz.); doch ware wenigstens Einmischung eines dem gr. 
ijums entsprechenden Wortes kaum abweisbar (s. Kluge s. v ) und kann 
nach Hirt IF. 32, 227 imbi, ymbe geradezu als Kollektiv *empi-o- „Bienen- 
schwarm“ aufgefaBt werden (vgl. uotq-ov : doT-yg); die Hinzufiigung von 
piano in ahd. impi piano (auch spat mndl. noch immc van byhen „examen“) 
kann nicht beweisen, daB imbi ohne Zusatz keine Beziehung gerade auf 
einen Bienenschwarm gehabt hatte. 

Uber np. any „Biene“ und lat. apis „Biene“ (beide dunkel) s. noch Boi- 
sacq 248, Vf. LEWb. 2 u. apis (letzteres nicht nacli Ilolthausen IF. 35, 132 
zu opus ; van der Yelden Uber Urspr. und Ilerkunft der idg. Sprachen 1912, 
43 erinnert an bask, abia „Stechfliege“). — Uber imbi nicht iiberzeugend 
Schroder Ablautst. 13 , IA. 28,32: als „IIohlklotz“ (worin der Bienenstock 
ist) zu dt. Nabe, opqmlog usw.. *enabh~. 

en .,in“ (:*»; slav. auch *on1 ); eni, ni os. (Ausgang wie *pi, *obhi usw. 
vielleicht mit dem Loc. auf -i verwandt, wenn nicht gar nach ihm ge- 
schaffen). Zusammenfassend Brugmann II 2 2, 827 — 837 m. Lit.; iiltere 
=======
L. Meyer BB. 7. 31 Iff., Fick aaO .j. 

Mit aisl. afl, ags. afol „ Kraft'* ware in der Bed. nachst vergleichbar gr. 
*<i7xekof) „Kraft“ in Av-ansXdaag ' dvaomoadeig lies., jon. m;."T£Aj/s „kriiftig“, 
dhytjTiekeibv „schwach“, bhy>)nf/Jv „Schwache‘ ! , jon. vtjnsXe to „bin ohnmachtig" 
i Diintzer KZ. 13. 17 f., Prellwitz BB. 24, 214 f., Y T b. 2 47, 313, Brugmann II 2 1, 
303. Bechtel Lex. 246 f.). wozu vermutlich Arte/dwv, AttoXXcov, thess. Aa/.ovv 
(Prellwitz) als „der starke Gott - ‘ und der elische MN. Tevxl-ajrXog (Prellwitz 
KZ. 45, 159). Doch ist das gr. d- gegentiber dem o- der andern Sprachen noch 
nicht befriedigend erkliirt, zumal im cs-St. ^utteXos auch ein d- als Reduktions- 
stufe keinen Platz htitte: entwedcr ist daher *dneXog nur zufalliger Anklang 
( *n-pclos M im-pulsus“??;, oder cs ist allenfalls mit ags. afol, aisl. afl (die dann 
mit ags. (efnan usw. erst durch sekundare Gruppenbildung zsgeschlossen 
waren) unter einem verschiedenen idg. *ap(f)lo- „Kraft“ zu vereinigen. 

Ivein Beleg fur Ablaut a (: o) in unserer Wz. ist (gegen Holthausen IF. 
35, 132) lat. apis „Biene‘‘ (sei gegentiber der Drohne, f ileus, als ,,Arbeits- 
biene" benannt; unannehmbar). 

2. op- „auswiihlen, den Yorzug geben, vermuten“. 

Die Wurzel steckt, wie Wackernagel IF. 3 1 , 258 ff. gezeigt hat. in gr. 

imotpopai zu em-orr- „wahlen. auslesen“: lat. *opere ist durch praed-opiont 



— obh- 


177
```


## [2026-09-05T20:27:48.083Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=7950 && NR<=8250' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | grep -n \"^[[:space:]]*[0-9]\\{2,3\\}[[:space:]]*$\\|— *[a-z]*- *$\\|^.\\{0,30\\}12[0-9] *$\" | head -20"
}
```


### [2026-09-05T20:27:49.836Z] TOOL RESULT

```
30:123 
90:124 
165:125 
225:126 
296:127
```


## [2026-09-05T20:27:58.691Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8100,8180p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-05T20:27:58.740Z] TOOL RESULT

```
Ungeklart sind die lett. Yerhiiltnisse is. J. Schmidt Krit. 157, Wiedemann 
BB. 30, 216 Anm., Endzelin Lat. predl. I 196 Anm. 4, Berneker 430 und 
briefl. Mitteilung voin 19. II. 1922,: neben nemi „nehmen“ (sichergestellt 
ffir die nordl. Dialekte Livlands, z. B. in Rujen, von Endzelin aaO.; wohl 
sicher zu *nem- „zuteilen : nehmen“) steht jetiit, jenit das nicht je- aus e- 



em- 


en 


125 


durch eine lautgesetzliche Entwicklung haben kann, s. J. Schmidt aaO., 
auch nicht mit ai. ydmati „halt“. idg. iem- zu vergleichen ist ! und nemt; 
letzteres darf nicht mit J, Schmidt auf ein idg. (Praefix ut cm-) 

projiziert werden (stiitzt also auch nicht Entstehung von germ, ncman aus 
niemo). Nach Endzelin ware nemt Verquickung von nemt mit jemt, was 
moglich ist ; jemt seinerseits ist wohl durch lit. Einfluh zu erklaren, da die 
Mehrzahl der lit. Mundarten den j-Yorschlag (jimti ) hat; oder Einwirkung 
von russ. vz-jafa, za-njatb s-njeh (danach auch nemt direkt?i? 

2. em- „leise sprechen*?? 

Eine nur nordgerm. Wz. ; altn. ymta „erwahnen, auBern“, norw T . dial. 
ymta „munkeln“, altn. ymtr „GemunkeP‘, norw.-dan. ymt ds. zu altn. nmi 
„Gerede“, ymja „einen Laut von sich geben“; alte o-Stufe in altn. emja 
(*amjon; Bed . = ymja). S. auch umla „murmeln, leise sprechen" usw. 
Dazu Falk-Torp 140S, 1580 und unten s. v. vab- „rufen“(?). 

enipi- „Stechmucke, Biene“? 

Gr. epnig „Stechmiicke i! ; ahd. imbi (al tester Beleg imp i piano) mlid. imbe 
„Bienenschwarm, Bienenstock*', erst spat-mhd. „Biene“, nhd. Imnie, ah- 
lautend ags. ymbe ( *umbia ) „Bienenschwarm“. Curtius 264. Bestritten von 
Liden Stud. 73 f. wegen der iiltern germ. Bed. „Schwarm von Bienen“; er 
vereinigt imbi, ymbe mit air. imbed acvmr. immet „Fulle, Menge“ unter einem 
*embh- „Fiille, Menge“ (aber lat omnis und gr. dcpevog sind keine Stiitze 
fiir eine solche Wz.); doch ware wenigstens Einmischung eines dem gr. 
ijums entsprechenden Wortes kaum abweisbar (s. Kluge s. v ) und kann 
nach Hirt IF. 32, 227 imbi, ymbe geradezu als Kollektiv *empi-o- „Bienen- 
schwarm“ aufgefaBt werden (vgl. uotq-ov : doT-yg); die Hinzufiigung von 
piano in ahd. impi piano (auch spat mndl. noch immc van byhen „examen“) 
kann nicht beweisen, daB imbi ohne Zusatz keine Beziehung gerade auf 
einen Bienenschwarm gehabt hatte. 

Uber np. any „Biene“ und lat. apis „Biene“ (beide dunkel) s. noch Boi- 
sacq 248, Vf. LEWb. 2 u. apis (letzteres nicht nacli Ilolthausen IF. 35, 132 
zu opus ; van der Yelden Uber Urspr. und Ilerkunft der idg. Sprachen 1912, 
43 erinnert an bask, abia „Stechfliege“). — Uber imbi nicht iiberzeugend 
Schroder Ablautst. 13 , IA. 28,32: als „IIohlklotz“ (worin der Bienenstock 
ist) zu dt. Nabe, opqmlog usw.. *enabh~. 

en .,in“ (:*»; slav. auch *on1 ); eni, ni os. (Ausgang wie *pi, *obhi usw. 
vielleicht mit dem Loc. auf -i verwandt, wenn nicht gar nach ihm ge- 
schaffen). Zusammenfassend Brugmann II 2 2, 827 — 837 m. Lit.; iiltere 
Lit. z. B. Curtius 5 309. 

Arm. i (vor Yokal y) und n- aus *m, alter *en „in“, adnominal m. Loc. 
und Acc. ; 

gr. ev und (poet.) evt, evi (so horn, stets als Postposition: att. nur mehr 
evt als Praedikat = t’leort) „in“, adnominal mit Dat. (= Loc.), Gen und in 
einem Teil des Gebietes auch noch mit Acc. („w T ohin“), in lctzterer Geltung 
anderwarts nach if zu Ivg (att. rig; danach eigen wie cfco, nicht aus *ev-Tto), 
Schulze KZ. 40, 416) erweitert (antekons. daraus eg). Tiefstufig a- z. B. in 



126 


en 


d-Asyu}, aorta^oyw (Solmsen KZ. 29, 97, Beitr. I 18f., Schulze KZ. 29, 264,
```


## [2026-09-05T20:28:11.512Z] TOOL CALL #19: Bash

```json
{
 "command": "pdftoppm -f 153 -l 153 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg153 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-05T20:28:12.801Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN apiary\"; grep -n \"apiary\" KLN_1966.txt | head; echo \"=== KLN 1971\"; grep -n \"apiary\" KLN_1971.txt | head"
}
```


### [2026-09-05T20:28:13.663Z] TOOL RESULT

```
total 14696
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:28 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  752374 Sep  5 16:12 bqt362_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  624515 Sep  5 16:12 bqt362.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 1032029 Sep  5 16:13 bqt362_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  385716 Sep  5 16:13 bqt363_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  338175 Sep  5 16:13 bqt363_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  692415 Sep  5 16:13 bqt363.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     395 Sep  5 16:10 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80793 Sep  5 16:15 pg131.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46793 Sep  5 16:20 pg133.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66991 Sep  5 16:16 pg135.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45014 Sep  5 16:12 pg137.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63658 Sep  5 16:13 pg144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60631 Sep  5 16:11 pg147.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81770 Sep  5 16:20 pg148.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


### [2026-09-05T20:28:13.729Z] TOOL RESULT

```
=== KLN apiary
3085:apiarist,  n.,  one  who  keeps  bees.  —  Formed  fr. next  word  with  suff.  -ist. apiary,  n.,  a  place  where  bees  are  kept.  —  L.  api- arium,  ‘beehouse,  beehive’,  fr.  apis.  See  Apis, a  genus  of  bees.
=== KLN 1971
17243:apiary, n., a place where bees are kept. — L. api- 
261319:of apiary fr. L. vespa , ‘wasp’, which prob. was
```


## [2026-09-05T20:28:17.429Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3080,3095p' KLN_1966.txt; echo \"=== KLN Apis genus\"; grep -n \"^Apis\\|Apis,  a  genus\\|apiology\" KLN_1966.txt | head"
}
```


### [2026-09-05T20:28:17.506Z] TOOL RESULT

```
the  sea)’  is  folk  etymology.  For  the  change  of  sh to  9,  cp.  Heb.  shiim,  Arab,  thum,  VArab. fum,  ‘garlic’,  Heb.  gadtsh,  Arab,  jddath,  VArab. jadaf,  ‘mound,  tumulus’,  and  the  Russian  PN. Feodor,  which  derives  fr.  Gk.  0s68<opo4  (see Theodore).  Cp.  Ashtoreth,  Astarte,  Ishtar.  Cp. also  April.
aphtha,  n.,  a  children’s  disease,  also  called ‘thrush’.  —  L.,  fr.  Gk.  tirplia,  ‘inflammation, eruption’,  fr.  £7txeiv,  ‘to  fasten;  to  kindle’.  See apsis.
aphthous,  adj.,  caused  by  aphthae.  —  See  prec. word  and  -ous.
aphyllous,  adj.  having  no  leaves  (bot)  —  Gk. 59UXX04,  ‘leafless’,  fr.  2-  (see  priv.  pref.  a-)  and 96XX0V,  ‘leaf’.  See  phyllo-. aphthitalite,  n.,  a  potassium  sodium  sulfate  (min¬ eral)  —  Formed  with  subst.  suff.  -ite  fr.  Gk. £9111x04,  ‘undecaying,  imperishable;  unchange¬ able’,  and  5X4,  ‘salt’ ;  so  called  because  it  is  un¬ changeable  in  air.  Gk.  £9^1x04  is  formed  fr. a-  (see  priv.  pref.  a-)  and  verbal  adj.  of  9<Mveiv, ‘to  decay’ ;  see  phthisis.  For  the  etymology  of 0X4 see  halieutic.
apiarian,  adj.,  pertaining  to  bees  or  beekeep¬ ing;  n.,  an  apiarist.  — •  Formed  with  suff.  -an fr.  L.  apiarius ,  ‘relating  to  bees’,  fr.  apis.  See Apis,  a  genus  of  bees.
apiarist,  n.,  one  who  keeps  bees.  —  Formed  fr. next  word  with  suff.  -ist. apiary,  n.,  a  place  where  bees  are  kept.  —  L.  api- arium,  ‘beehouse,  beehive’,  fr.  apis.  See  Apis, a  genus  of  bees.
apicitis,  n.,  inflammation  of  the  apex  of  an  organ (med.)  —  A  Medical  L.  hybrid  coined  fr.  L. apex,  gen.  apicis  (see  apex)  and  -itis,  a  suff.  of Greek  origin.
apiculture,  n.,  rearing  of  bees.  —  Compounded of  L.  apis,  ‘bee’,  and  cultiira,  ‘tending,  care’.  See Apis,  ‘a  genus  of  bees’,  and  culture, apiece,  adv.  —  Orig.  written  in  two  words:  a piece.
apiology,  n.,  the  scientific  study  of  bees.  —  A  hy¬ brid  coined  fr.  L.  apis,  ‘bee’,  and  Gk.  -koyia., fr.  -X6yo4,  ‘one  who  speaks  (in  a  certain  man¬ ner);  one  who  deals  (with  a  certain  topic)’.  See Apis,  a  genus  of  bees,  and  -logy.
Apios,  n.,  a  genus  of  plants  of  the  pea  family (bot)  —  ModL.,  fr.  Gk.  £juo4,  ‘pear  tree,  pear’, which  is  a  loan  word  from  an  unknown  source, whence  also  L.  pirum,  ‘pear’  (cp.  pear) ;  so  called from  the  pearlike  form  of  the  tubers.
Apis,  n.,  an  Egyptian  god  represented  as  a  man with  the  head  of  a  bull  (Egypt,  mythol.)  —  L., fr.  Gk.  'Am 4,  fr.  Egypt.  Hdpi.
Apis,  a  genus  of  bees.  —  L.,  ‘bee’,  of  unknown etymology.  Cp.  Apium,  ache,  ‘parsley’.
Apium,  n.,  a  genus  of  plants  of  the  carrot  family. —  L.,  ‘parsley’,  lit.  ‘the  plant  preferred  by  bees’, a  derivative  of  apis,  ‘bee’.  See  prec.  word, apivorous,  adj.,  bee-eater.  —  Compounded  of  L. apis,  ‘bee’,  and  -vorus,  from  the  stem  of  vordre.
apjohnite
apoplexy
90  91
=== KLN Apis genus
3084:apiarian,  adj.,  pertaining  to  bees  or  beekeep¬ ing;  n.,  an  apiarist.  — •  Formed  with  suff.  -an fr.  L.  apiarius ,  ‘relating  to  bees’,  fr.  apis.  See Apis,  a  genus  of  bees.
3088:apiology,  n.,  the  scientific  study  of  bees.  —  A  hy¬ brid  coined  fr.  L.  apis,  ‘bee’,  and  Gk.  -koyia., fr.  -X6yo4,  ‘one  who  speaks  (in  a  certain  man¬ ner);  one  who  deals  (with  a  certain  topic)’.  See Apis,  a  genus  of  bees,  and  -logy.
3090:Apis,  n.,  an  Egyptian  god  represented  as  a  man with  the  head  of  a  bull  (Egypt,  mythol.)  —  L., fr.  Gk.  'Am 4,  fr.  Egypt.  Hdpi.
3091:Apis,  a  genus  of  bees.  —  L.,  ‘bee’,  of  unknown etymology.  Cp.  Apium,  ache,  ‘parsley’.
3096:‘to  devour’.  See  Apis,  a  genus  of  bees,  and
```


## [2026-09-05T20:28:18.373Z] TOOL CALL #22: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg153.png"
}
```


### [2026-09-05T20:28:18.408Z] TOOL RESULT

```

```


## [2026-09-05T20:28:37.222Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN angubin\"; grep -n \"angubin\\|angubîn\\|angub\\|Honig\" HRN.txt | head -30"
}
```


### [2026-09-05T20:28:37.265Z] TOOL RESULT

```
=== HRN angubin
1484:124. engehtn (AM.), enguhln *Honig, vergl. terenguhin,
1489:bei. vergl. benag, n. b^nay *Honig' (36).
8408:Ar. mäSiy 'weisser Honig', moMyat 'glatter Panzer; "Wein* (dazu
8726:'Honig', ai. mädhu- süss; Honig, Meth' und aw. maSa-
8728:ksl. wedü 'Honig, Wein', nhd. Meth etc.
9821:ist, weil die Eigenschaft, Honig zu bereiten, oder
9849:sprochen, Sicilien war das Honigland, der berühmte
```


## [2026-09-05T20:28:38.816Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD angubEn\"; grep -n \"angub\\|angwb\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB\"; grep -n \"angub\\|angwb\" NYB_vol2_glossary.txt NYB.txt | head -20"
}
```


### [2026-09-05T20:28:38.876Z] TOOL RESULT

```
=== PHD angubEn
PHD.txt:212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
PHD.txt:439:~ith: femininity. *madag [mtk' | (M myg, N māya)] essence, substance. ~ig [-yÀ!] essential. ~war [-w/] essential, especial, principal. madan [mtn! | M mdn] come. madār [т comer. mādar [AMYtl < А т-у; mtl | M mdr, N ~] mother. imādayān [m!tgd?n! | М m'dy'n] book. *mādayān [m tyd?n'] essence, basis, core; essential, chief. mādayār [m tgd’l] steward; (chess) rook, castle. mādišt [m’tyst'] *matter, protoplasm. mādīyān [m’tyg?n | N ~] mare. may [my | N ~] hole, pit. magas [mks | P mgs, N ~] fly. ~ i angubén: honey-bee. magind [mkn'd | M mgyn(d)] shield, protection.
PHD.txt:961:bee magas i angubén.
PHD.txt:2303:honey angubén; ~-bee magas i angubén.
PHD.txt:5470:gabrih anguben! gowiin
PHD_mackenzie.txt:1103:anguben [DWBSYA < A dbs; )ngpyn' IN angubin] honey. lJ}~) ~""~...
PHD_mackenzie.txt:3412: ....... i anguben: honey-bee.
PHD_mackenzie.txt:6041:bee magas i anguben.                        bitterness taxlih.
PHD_mackenzie.txt:6772:helmd targ.                                    honey anguben; ,..,-bee magas
PHD_mackenzie.txt:6773:help (n.) ayarih, dastyarih, frayad,              anguben.
PHD_mackenzie.txt:10799:                                                        angubcn[
=== NYB
```


## [2026-09-05T20:28:50.358Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1478,1495p' HRN.txt; echo \"=== which leaf\"; python3 - <<'EOF'\nd=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\ntot=0\nfor i,p in enumerate(pages):\n    n=p.count('\\n')+1\n    if tot<=1484<=tot+n:\n        print('leaf index',i,'-> printed page',i-21)\n        break\n    tot+=n\nEOF"
}
```


## [2026-09-05T20:28:51.680Z] TOOL CALL #26: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(d['HRN'].get('lookup_hint'));print();print(d['BQT'].get('lookup_hint'));print();print(d['BQT'].get('page_offset'));print();print(d['IEC'].get('lookup_hint'));print();print(d['SOD'].get('page_offset'))\n\""
}
```


### [2026-09-05T20:28:52.126Z] TOOL RESULT

```
158, ist ihm darin gefolgt), dass es am Platze sein dürfte, hier kurz
auf das Wort einzugehen. Als Grundbedeutung giebt Hesych fQyartjg,
vntjQFTtjZt ax^oifooot; an; arjfjL<xCvfi Sf. xai rov: fx SiwJo^f]'^ ßaaiXixovg yQa/u-
juaTofpogov^. Suidas hat nur die letzte Bedeutung mit dem Hinzufügen
ol (Vf nvToi xai aaiaV^Ti« (lies aaydvdai); vergl. auch Herod. VIII, 98
Tovro To SQuat^jua twv InntJoy xaXh'ovai U^^nai ayyixQiliov, Dazu ayya()fvu)- 29 -
124. engehtn (AM.), enguhln *Honig, vergl. terenguhin,
sikengubi7i, sirkenguhln, gezengubln, gulengubm ; arab.
LW. anjuMn, vergl. /vskanjubm (Ibn Beitär) u. a. m.
phlv. angpen, angumen {e beweist das arm. LW.
gazpen *Tamariskenhonig).
bei. vergl. benag, n. b^nay *Honig' (36).
Das erste Glied des Compositums eng Biene' (Wörter-
bücher: änikj enik) vermag ich im Neupersischen nicht
zu belegen; es wird im Gazophylacium citirt, wohin
es aber auch nur aus persischen Originalwörterbüchern
gekommen sein wird. v. Stackeiberg, SAM^KA
H-BKOTOPWXX nEPCH4CKHX^ GIOBAX^ Kh OCETHHGKOMX
=== which leaf
leaf index 48 -> printed page 27
```


### [2026-09-05T20:28:53.927Z] TOOL RESULT

```
Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.

grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)

vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').

Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.

printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
```


## [2026-09-05T20:29:10.298Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint(len(pages))\nimport re\nfor i,p in enumerate(pages):\n    if 380<=i<=400 and ('انگبین' in p or 'انگ' in p):\n        print('leaf',i, 'approx printed', i-215)\nEOF"
}
```


## [2026-09-05T20:29:10.398Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==276' HRN.txt | head -60"
}
```


### [2026-09-05T20:29:12.123Z] TOOL RESULT

```
777
leaf 380 approx printed 165
leaf 382 approx printed 167
leaf 384 approx printed 169
leaf 386 approx printed 171
leaf 391 approx printed 176
leaf 392 approx printed 177
leaf 393 approx printed 178
leaf 394 approx printed 179
leaf 395 approx printed 180
leaf 396 approx printed 181
leaf 399 approx printed 184
leaf 400 approx printed 185
```


### [2026-09-05T20:29:13.868Z] TOOL RESULT

```
- 254 —
nähe' von duyße und furux, mu-furu/jim Verkaufe
bezw. 'ich verkaufe' von fitruyde.
122**''' enfest 'Spinnengewebe'.
ap. Via(m)haMa- (Säle mann, Shams i Fachrii
Ispahänensis lexicon persicuni, Casani 1887, S. 155 a).
Unsicher, man müsste eine Arabisirung annehmen.
Erst nacliträglich sehe ich die in dem genannten
Werke S. 184 im Index verzeichneten 9 Etymologieen
Salemanns, von denen sclion 2 oben erwähnt sind
(s. äfdum, No. 38 und gerzmän^ No. 906****). Np. häsre
V
'Beackerung (Vullers), Acker (SF) aus aw. väsfra-,
hevberüsän 'Volk, Gemeinde* (Varianten bei Vullers
s. V. berpernsän) aus phlv. varav(i)m und urmek —
russ. armydki 'Armäck, kameelhaarener , langer,
breiter Bauernrock' sind zweifelhaft, zu medhüs vergl.
oben S. 220 Anm. 1. Sutüdäu , phlv. astödän- ist
rituelles Parsenwort (Sahn. I, 267 Vers 410, III, 1399
Vers 2444 u. ö.) wie de/me.
123. Zu seiner Erklärung von ayya()n,^' schreibt mir Prof.
Jensen noch nachträglich:
j,Agru — 'Mietling kommt in der Tat in den In-
schriften vor, falls agrütu 'Miets Verhältnis* nicht von
agrn --- 'Lohn', sondern von ^agru 'Mietling* abzu-
leiten. Letzteres ist weit wahrscheinlicher. Agarütu,
für agrütu bezeugt, beweist dann die Existenz einer
Zwischenstufe ag(g)uru zwischen agru und *((ngarif.
Um Missverständnisse unmöglich zu machen, mache
ich noch besonders darauf aufmerksam, dass syr.
^. (und arab. >^') als Lehnwörter aus dem Assyr.
aufzufassen sind".
124. Als eine Vermutung möchte ich hier aussprechen,
dass np. eng 'Biene' vielleicht dasselbe Wort wie lat.
apis ist. Das letztere wird gewöhnlich mit gr. einrig
Stechfliege, Schnake' zusammengestellt, eine Identifi-
cation, die mir schon darum sehr unwahrscheinlich
ist, weil die Eigenschaft, Honig zu bereiten, oder
etwa in zweiter Linie zu summen, für die Biene so
```


## [2026-09-05T20:29:21.293Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==277' HRN.txt | head -60"
}
```


### [2026-09-05T20:29:23.114Z] TOOL RESULT

```
— 255 —
charakteristisch ist, dass ihr Stechen durchaus dahinter
zurück tritt. So Imt das Indische eine ganze Reihe
Worte für *Biene', aber keines bedeutet, so weit sich
dieselben etymologisiren lassen, 'Stecherin' — vergl.
madhukara-, madhfthff-, madhukarl- etc. ^) oder
ptts/Htfidliaya-j jmspaUh- oder sätpada- oder hhramara-
{hhpiga-) *Brunimerin\ wie wohl auch gr. ^^wraf, vergl.
dvir^pho; unklar aU-, sarägh-, sarägha-^ sardt- — ,
und auch in anderen indogermanischen Sprachen finde
ich kein Beispiel, dass ein Wort für Biene Bezeich-
nung einer Stechfliege geworden sei. Wenn sich
daher für a/ns eine bessere Anknüpfung findet, —
und eine solche glaube ich durch die an np. en(/
bieten zu können — so wird man gr. e/LintQ ohne
viel Bedauern preisgeben können. Wie so manche
anderen Wörter aus italischen Dialekten in das
Lateinische aufgenommen worden sind — z. B. bös,
sabellisch (Bersu, Die Gutturalen und ihre Ver-
bindung mit V im Lateinischen S. 139, vergl. auch
Stolz, Latein. Grammatik- S 47 Anm. 1), pahimhes,
popina, oskisch (Stolz, 55 46 Anm. 3), rüfns^ stßlus
etc. (Stolz, J5 54:^ '^5)» die mit / beginnenden Worte
lingiia, lacruma, levir etc., sabinisch (II. Seymour
Conway, Indog. Forsch. II, 157 folg.) u. a. m. ~
so ist vielleicht auch apis oskisch es Lehnwort. In
Bruttium, Lucania, Messana wurde oskiscli ge-
sprochen, Sicilien war das Honigland, der berühmte
Sitz der Bienenzucht (vergl. E. 0. von Lippmann,
Geschichte des Zuckers, S. 10, 11), die Übernahme
des oskischen Wortes in das Lateinische wäre also
durchaus nicht befremdlich. Allerdings bleibt -mp
sonst im Oskischen erhalten (vergl. R. von Planta,
Vocalismus der oskisch-umbrischen Dialekte, S. 307),
aber auch bei der Zusammenstellung mit spnl^^ ergiebt
*) Ai. admasäd' (G e 1 d n e r , Vedisohe Studien II, 1 79 folg ) passt
mehr auf die Fliege oder Wespe (wenn das ädnui- Obst ist) als auf
dip Biene.
```


## [2026-09-05T20:29:30.077Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor i,p in enumerate(pages):\n    if 'انگبین' in p:\n        print('leaf',i,'printed~',i-215, p.count('انگبین'))\nEOF"
}
```


### [2026-09-05T20:29:31.888Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:29:34.911Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==390' BQT_v1_pages.txt | head -40"
}
```


### [2026-09-05T20:29:36.842Z] TOOL RESULT

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
```


## [2026-09-05T20:29:47.574Z] TOOL CALL #32: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:174 --image 2>&1 | head -60"
}
```


### [2026-09-05T20:29:49.250Z] TOOL RESULT

```
no scan of BQT covers printed page 174 (see 'scans' in refs_online.json)
```


## [2026-09-05T20:29:54.180Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 392 394 396 398 400 402; do echo \"=== leaf $n (printed ~$((n-215)))\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' BQT_v1_pages.txt | head -8; done"
}
```


### [2026-09-05T20:29:56.339Z] TOOL RESULT

```
=== leaf 392 (printed ~177)
اگارده است که افسانه و سر گذشت باشد .
انگاده ۱ ه بروزن عموارء ."هر چیز
"که افانه وس گذشت داشد - وباد گذشتها کردن
رانیز کوبند - و ازسر گرفتن سر گذشت وافانه
را عم گفته اند بطریق کنابه چنانکه ا گر کسی
بسیارومکرراز گذشته بگوید گویشدهانگاره‌میکند»
یعنی باز از سر هیگیرد - و پس پی خزنده از
شرم و حیا را نیز کوبند - وبمعتي دفتر وحساب
=== leaf 394 (printed ~179)
انگشت ب حرف‌نهادن - کنابه
ازعیب کر فتن ودکته گیری کردن باشد .
) نگشت بر دهان گد اشتن- کنابه
از<سرت واضوی - وتعجب وتحیرباشد - واشاره
کردن بخاموشی هم هست .
بضم بای ابجد وفتح رای فرشت و سکون کاف ؛
جانورست که آنرا حوش کورمیگویند و پیوسته
درزیی زمین‌میباشد وسخ درخت ونباتات‌میخورد.
=== leaf 396 (printed ~181)
انگوز زیتونی . .
وبعربی اصابع‌المذاری گوبند .
) نگوژه؟ - با زای فارسی بر وزن
سنبوصه ؛ صمغ درخت انکدان باشد و به_بی
حلثیت و صمن‌المحروث خوانند . و تخم آنرا
بذرالانجره وقریض کویند .
که کوی کربان وتکمة کلامرا اژآن‌بگذرانند -
است .
=== leaf 398 (printed ~183)
کوبند که بدشواری از انا شود و حل
9
| ثیشه - بر‌رزن‌همینه .جاسوی‌وچاپلوی
هر چیز بسته و منجمد بأشدچه درفارسی‌سینوشن
تب ۱۵۰ ,
0 زمین ۰ ء ظرفی باشد ازسنال
مانند مو وخمچأیزگی که دوغ وا جر آ ‌کنند
او * نم اول : و سکونِ نافی » ۳
=== leaf 400 (printed ~185)
واجب و بفستا وا گیبتد و جر هی اهنت »
و آن‌قدارست ازسرانگشت ,کوچك ۷ مرانگشت
بزر که دست آدمی ۰
اوذست » بروژن بدست » بمعنی‌آودی
اس ت که وجب و بدست وشبر باشد .
و مدشه‌ایست .
ذاز شلمدار وسکون رای بی‌شطه ؛ بات بونانی ۷
آب را گویشد و مربی ماء خوائند .
=== leaf 402 (printed ~187)
آوروختن
آود و ختن ه بروزن و معنی افروخئن
است. که روشن کردن: آنشس و چراغ باشد ۷ .:
آوده » بفتح اول و ثاكك وسکون‌انی »
بمعنی ابره است که روی فبا و کلاه و امثال ان
باشد, چه درفارسی با و واو بهم نبد بل‌می با بند ‌-
اور یا ۴ ه بر وزن بوربا» نام شخصی
است که داود علیه‌السلام او را بجنك فرستاد واو
```


## [2026-09-05T20:30:02.507Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==392' BQT_v1_pages.txt | head -60"
}
```


### [2026-09-05T20:30:04.458Z] TOOL RESULT

```
رن
ار ه- باازای فارسی بر وزن غمزه ؛
مرجماث باشد و آثرا ببربی عد ی گویند .
انسته - بفتم اول و کسرثانی و سکون
سین بی‌قطه و فتح فوفالی 4 مقصورآ دته است»
وان بیخ کیاهی باشد خوشبوی که بعربی سعد
" گو بکف .
۰ ۰
انشانا - بفتم اول و سکون الی وشن
فرشت ونئای مثلته هردو مالف کشیفه » بسربالی
دوابی‌است که آنرا بغارسی مویزكك وبعربی زسبت
الجبل خوانند .
اتطلیون « با ای حطی ولام وتحتانی
بروزن عنبر گون , بلغت بونانی۱ فوی قزح را
کون دک هکمان شرطان باشد .
| نطی فیا۳ - بروزن‌افلونیا. بلفت‌ونانی
کاسنی شامی را گویند وآن سرد وتراست ودجگر
گرم را نافم باشد .9
اقاق »یک اول و سکون تانی وفای
بالف کشیده و بقاف زده ۰ روغن زءتون تازه را
گویند .
ات - بر وزن رحست  )۱(‏ همان
وخارت وزبانرا کویند که سمعنی غبن‌باشد - ودر
عربی بمعنی ننک و عار آمده است ۰
] نقست « بروزن , بدمست » پرده وتنیده
عنکبوت وا گوشد .
افقر دیا - بختح اول و فاف و سکون
ثانی و را و دال بی نقطه و تحتانی بالف کشیده »
لغتی است رومی و بعضی کوبند بونالی ۴ وممنی
آن مانند دل‌باشد وان چیزس تکهبلاد ر گوشد.
)۱( چاثه : زحمت.
۱ - بیونانی 50461105. «افتشنگای».
انگارده
بهترین وی آست که سیاه و فربه باشد و چون
بشکنند پر شیره بود . و آن گرم و خشك است
در چهارم» فوت حافظه دهد وذهن را تب زکند ,
و بعربی‌ثمرقالبلادر خوانند وبهندی بلاو مگویند.
قلیا - بکر اول و قاف و سکون‌ثانی
و لام و تحتانی بالف کدیده , بلفت احل فرب
دوایی است که آغرا بفارسی شنکار گویند وبعریی
شجرتالدم خوانند. وآن نوعی از سرخ مرداست.
بررکه آن سرخ بسياهی مابل میباشد بذ ییه بز
کوهی برخنازیی نهئد نافم بود؛ و بعضی گویند
لفت رومی است .
اون ه با قاف بروزن «یمون » بلفت
بونانی کل کنده را گویند وآن نوعی از کماةباشد
وآنرا بجهت فربهی حلوا کرده خورند. و بعربي
وردالمنتن )+( خوانند .
انگ . بغتح اول و سکون انی و کاف
فارسی . محر آب را گوبن که کوزه گران اژسفال
سازند و بجپت مرور کردن آب بهم وص لکنند.
و نام ولاتی است در هندوستان ۴ .
انگاد * - بروزن زیگار . بسنی‌صور
و پندارباشد که از پنداشتن‌است - و صور کننده
را نیز گوبند - و امر باین هعتی هم هست معنی
یشگار و انکارشی‌کن- وبمعتی انکاره نیز آمده
است که کار نانمام باشد .
نگاردن » بفتح ارل و دال ابید
وسکون نون . بمعنی‌پنداشتن وود کردنو کمان
بردن باشد .
```


## [2026-09-05T20:30:21.313Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==394' BQT_v1_pages.txt | head -70"
}
```


### [2026-09-05T20:30:23.087Z] TOOL RESULT

```
مردم فررنگ «م هست ٩‏ ۰
الث و زای قطه‌دار ساکن » سلی باشد که بآن
زمن را هموار ساز ند ۹
انگز ح بفت اول و خم نالث: و کت
تابی و زای فارسی» آهنی باشد سر کج که فیلرا
بدان بهرطرف که خواهند بي‌ند .
انگژ د ۴ ختح اول دضم ثالث‌وسکون
انی و فتح زای فارسی ودال ابجد -اکن مطلق
صعفها را گویندعموعاً و صمفی باشد بغایت‌بدبوی
و آترا پعربی حلتیت خوانندو آنرا انگژدیسب
آن گون که سمغ درحت انگدان است و ال
آن انگدان ژد باشد بفتح زای فارسی چه ژد
بلفت فرس بمعنی صمغ است و آن گرم و خشكت
است در درجه سیم .
انگز لك . بازای هوز بروزن مرجمك ,
کجك فل را گونند و آن آلی باشد سر کج از
آهن که فیلبانان فیل رابدان بپرطرف که‌خواهند
برند . و بازای فارسی هم بنظر آهده است :
اآلگژ واه بکس نات و سکون زای
فارسی و واو بالف کشپده‌بروزن »نزل‌ها. جابی‌را
کودت که شنها گوتفندان زا چر ادا تک
دارند - و کوسفندانرا نیز گفته‌اند - ویمعنی‌دانه
و ختَهةٌ میوه ها هم آهده است .
انگشت برچشم نفادن
۱ نگژه ‌ ح با زای فارسی مفتوح‌بروزن
خربزه , مخفف انگوژه است که صمغ درخت
انکدان باشد و آلرا عربان حلنیت و شیرازبان
انگثت گنده ( ۱ ) کوند. و با زای هوز نیز
ال اسگ:
ا نگسبه بفتح اول والت و سکون‌انی
و سین بی قطه و فتح بای ابجد » برزیگربرا
گویند که صاحب سامان بود وکار کنان وزراعت
کاران ببار داشته باشد .
انگشبه - با شین نقطه دار . بر وزن
و معنی انکته کت که مرن وا اسان
باشد - و سودا کر صاحب مابه را نیز گفه‌اند.
انگشت؟ - بنم اك , ممروضت که
عربك از انگشتان دست و بای باشد - و بکس
ثالت زغال را گوند که اخگر کشنه شده است.
انگشتال * ه یکی تاك , فوفانی بالف
کشبده و لام سکن , مردم‌شمیف و نحیف وعلیل
ویارنا وصاحب تقاهت راگونند .<
انگشت بد ندان گز بدن - کناه
ازنه‌جب کردن و نحیر نمودن باشد - و حسرت
و اقوی خوردن را نیز گوبند .
انگشت بر چشم نهادن د کاب
ازقبول کردن ومسلم‌داشتن باشد, وانگثث بر دیده
۳ ۳۳ رلك؛ انگود.
```


## [2026-09-05T20:30:39.299Z] TOOL CALL #36: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T20:30:39.305Z] TOOL RESULT

```


```


## [2026-09-05T20:30:44.550Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%86%DA%AF%D8%A8%DB%8C%D9%86",
 "prompt": "Give the full Persian entry: etymology of انگبین (angabin/angobin) 'honey', Middle Persian form, any reconstructed Old Iranian form, cognates, and derived terms like شکنجبین/سکنجبین, ترنجبین, گزانگبین."
}
```


## [2026-09-05T20:30:45.845Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/apis",
 "prompt": "Give the Latin entry for apis 'bee': full etymology section, including any mention of Proto-Indo-European, de Vaan, Greek ἐμπίς, Persian, unknown origin, substrate."
}
```


### [2026-09-05T20:30:52.979Z] TOOL RESULT

```
# Persian Entry: انگبین (angubīn/angabīn) - Honey

## Etymology
The word derives from **Middle Persian** (angubēn/ʾngpyn'), ultimately from **Proto-Iranian** *Hangubáynah.

## Middle Persian Form
Middle Persian: **angubēn** (DWBŠYA, ʾngpyn' /⁠angubēn⁠/)

## Cognates
Related terms appear across Iranian languages:
- Northern Kurdish: *hingiv*
- Zazaki: *engemin*
- Central Kurdish: *ھەنگِوین* (hengiwîn)
- Talysh: *انگوین* (anqevin)

The etymology notes the word is "probably not related" to انگ (ang, "yellowjacket"), but rather connected to *انگم* (angom, "resin").

## Derived Terms
- **ترانگبین** (tar-angobin) - Persian manna
- **سرکنگبین** (serkangobin) - vinegar-honey drink
- **مگس انگبین** (magas-e angobin) - honeybee
- **گزانگبین** (gaz-angobin) - tamarisk manna
- **گل‌انگبین** (gol-angobin) - conserve of rose petals and honey

*Note: The requested terms شکنجبین/سکنجبین and ترنجبین do not appear in the provided source material.*
```


### [2026-09-05T20:30:53.295Z] TOOL RESULT

```
# Latin Entry for *apis* ('bee')

## Etymology Section

The origin of Latin *apis* is uncertain. Traditionally, scholars have hypothesized a connection to Proto-Indo-European *\*e/a(m)p-i-* ("stinging insect; bee"), linking it to Ancient Greek *ἐμπίς* (empís, "stinging or biting insect"), German *Imme*, and Old English *imbe*.

However, the term exhibits characteristics of a European substrate word rather than a standard Indo-European derivation. 

According to Vennemann's Atlantic substrate theory, the ultimate source may derive from a Semitic word cognate with Egyptian *ꜥfj* ("bee"), though no attested Semitic cognates survive. De Vaan finds this hypothesis plausible.

An alternative theory suggests an Osco-Umbrian loan from *\*akuis* ("sharp, stinging"), based on phonological patterns where the Osco-Umbrian reflex of Proto-Indo-European */kʷ/ regularly becomes Latin /p/, comparable to *aqui-* ("sharp") in related words.

The entry notes that the Osco-Umbrian hypothesis requires additional sourcing.
```


## [2026-09-05T20:31:00.298Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%86%DA%AF",
 "prompt": "Give the Persian entry for انگ: all senses (including 'yellowjacket/wasp', 'mark/stamp', water-pipe) and each etymology section with Middle Persian / Proto-Iranian reconstructions."
}
```


## [2026-09-05T20:31:02.069Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%90%CE%BC%CF%80%CE%AF%CF%82",
 "prompt": "Ancient Greek ἐμπίς: meaning and full etymology (Beekes, Pokorny, relation to Latin apis, German Imme)."
}
```


### [2026-09-05T20:31:05.669Z] TOOL RESULT

```
# Persian Entry for انگ

Based on the Wiktionary content provided, the Persian entry for **انگ** (ang) includes:

## Senses

1. "A kind of commercial label used on certain goods in the past"
2. "(figuratively) slander, mud, libel"

## Etymology

The provided content does not include a full etymology section for the Persian entry with Middle Persian or Proto-Iranian reconstructions. The page only documents that Persian **انگ** exists as a noun with the two senses listed above, but lacks the historical linguistic derivation you requested.

**Note:** The Urdu and Sindhi entries do provide etymological trees tracing back through Sanskrit and Proto-Indo-European roots, but equivalent reconstructions for the Persian entry are not present in this source material. The senses related to "yellowjacket/wasp" and "water-pipe" are also not documented in this particular Wiktionary entry.
```


### [2026-09-05T20:31:08.567Z] TOOL RESULT

```
# ἐμπίς (Ancient Greek)

**Meaning:** This Ancient Greek noun refers to a mosquito or gnat, and can also denote the larva of the oestrus fly.

**Etymology:** The word has competing etymological theories:

1. **Popular derivation:** Connected to ἐμπίνω (empínō), meaning "to drink (blood)."

2. **Indo-European connection:** Pokorny links it to Proto-West Germanic *imbī ("bee") and potentially to Proto-Indo-European *h₁empí- ("gnat, biting insect"), though this remains debated among scholars. As noted, this comparison is "not universally accepted."

3. **Substrate theory:** Some scholars view it as evidence of a widespread European substrate word, particularly given parallels like Latin *apis* ("bee").

The word is a feminine third-declension noun and has descended into the Translingual genus *Empis*.
```


## [2026-09-05T20:31:17.037Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B9%E0%A4%BF%E0%A4%99%E0%A5%8D%E0%A4%97%E0%A5%81",
 "prompt": "Sanskrit हिङ्गु hiṅgu: meaning and etymology — is it Indo-European, a borrowing, of foreign/unknown origin? Any mention of Persian anguza/انغوزه, Sogdian, or asafoetida."
}
```


## [2026-09-05T20:31:18.641Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/-%D9%85#Persian",
 "prompt": "Persian suffix ‑م (-om/-um) forming ordinal numbers: etymology, Middle Persian form, Old Iranian/Avestan antecedent, and cognates (Latin -imus, Avestan -əma-)."
}
```


### [2026-09-05T20:31:20.958Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:31:25.340Z] TOOL RESULT

```
# Sanskrit हिङ्गु (hiṅgu): Etymology and Origins

## Etymology

The word is **not Indo-European**. According to the Wiktionary entry, it was "Borrowed from Proto-Iranian *Hángwr̥ ('extract, resin')," with an unexpected shift from *a to i.

## Origin Details

The term derives from Proto-Iranian roots related to asafoetida production. The source notes the derivation involves *Hanguǰatu, from which "Iranian terms for asafoetida derive."

## Meaning

हिङ्गु primarily refers to **asafoetida** (_Ferula assa-foetida_), a resinous plant product. It can also denote "a kind of liquid made from the roots of asafoetida."

## Borrowed Terms Connection

The entry documents extensive borrowing patterns across Asian languages (Chinese, Nepali, Persian, Sogdian, Tajik, Wakhi, and others), supporting its status as a recognized commodity term spread through trade and cultural contact rather than as an inherited Indo-European word.
```


## [2026-09-05T20:31:38.843Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=d.split('\\f')\n# leaf ~= p/2 + 15 -> p 257 -> leaf ~ 143\nfor i in (142,143,144):\n    print('=== leaf',i)\n    print(leaves[i][:3000])\nEOF"
}
```


### [2026-09-05T20:31:40.439Z] TOOL RESULT

```
=== leaf 142
mb. eikvas-atis (in phr. ahtis-per.. . ‘for de- parted souls'?); Li. cf. eikvoti ‘squander’ be- side eiklüs ‘nimble’. (Isophonic are Lat. 1co, ere; OLat. eic- "strike
eila, io ‘going, gait;, gang, troop; file, line’. Cf. ei-mi. Cf. WP I, 70, 104 Skt. ela “sport beside Irah, -am ‘wind’; ilā 'flow"; ir-te, mp. ‘go’ (ei-: i-); Gk. ale ile “gang, troop; W wyl “flow, gush’; OHG ia ‘haste’; Du. ijl, id.; Sw. il ‘gust’; Li. eilé line, row? be- side eilà, eilià, id. and (o-gde) ailà "row. rank’; Latv. iela ‘street beside (o-gde) aile ‘row, path, opening”. (Isophonic forms are Lat. ilia, -ium ‘waistline’; Ir. alle gs éille ‘thong’; Latv. iela (2) “peg, prop, stick’. Lit. dine" ?)
eilus, os (11-?) “mud, clay” Oss. ilà, id.; Gk. eilús, (os id.; cf. arg-ilos ‘white clay; Cz. jíl, gs -u ‘clay’; R il ‘mud’
eimi (eio) ‘go’. WP I, 102. (Plural forms: i-) Skt. émi, 1 pl. imáh; Av. aei(mi); OPer. ay-; Hitt. cf. ca-imi, cpd.; Myc. ijon, pr. pt. “going; Hom. eimi, pl. men: pr. subj. eið, íð; EMAlb. íhem (-h- due to hiatus, or fr. *-sK-); Lat. eo, īre; Pael. cf. eite! *go!; Umb. etu, 3s. jussive; W âf “shall go? beside awyf “may I go’; Br. an, 1s. pr.; inn, 1sg. fut.; EMLi. eimi; Latv. eimu, iemu, eju, id. Cf. Latv. eja ‘path’ & Li. eimé! let's go!
(eimos 'going'. Cf. oimos and see eismn- be- low) Skt. (ambig.) éman ‘path, course’; Ir. éimh ‘swift; ON ima, f. ‘strife
-einå ‘product of . . ?. Cf. -inā Lat. porc-ina ‘pork’; Cz. kon-ina, etc. (“horse- meat”, etc.); Slovene, cf. prasét-ina ‘pork’; Li. parš-iena, id.
eiså, io (ois-) ‘go, dash, impetus, outburst’. Cf. eismn-, oisá, eimi Skt. (ambig.) éSa ‘search; desire’; Lat. (ambig.) ira ‘anger’; Icel. cf. írafár *overhaste'; Li. cf. eislùs ‘going’; eisena ‘gait’
235
eisio ‘shall go’. Cf. eimi Skt. esyàmi; Gk. eið (pres. subj.); Li. eisu, ei- siu; Latv. iešu (The Li. form eisu is that of the Bible translation)
eisios (eiso-, eito-) (a cpd. pronoun) Skt. cf. esab, -a, neut. etat ‘this’; Osc. eíseís “his; etus’; eise (loc. sg. ‘in him, her, it"); Umb. erer, m., erar, f. “his, her
eisk- (eisK-) ‘request, demand, search". WP I, 12. Cf. aisK- Umb. cf. eiscurent “they shall demand": W wysg (adj. ‘proceeding’; s. ‘procedure, trend"); OSC isto, iskati & isko, ati zeck: Li. ieškau, ieškoti, id.
eismn- (eimn-) “going, movement. Cf. ei-mi and cpds., oi-m- Skt. cf. éman “path, course Ir. éimh, adj. ‘swift; ON ima ‘conflict, strife’; Li. eismas ‘going, traffic, movement; (o-gde in Hom. oima 'dash"). Variants: Li. eisena ‘gait’; W wys (‘mobility’, fr. *eist-)
eit- (theme of ei-, i- ‘go’ with extn. -t-). Cf. oit- Osc. eítuns 'soldiery'; eítuva- ( ‘money’, orig. *viaticum, ways & means"); Fal. eitam. f. acc. gallop’ ? on a pot w. horses); Li. cf. eitinis ‘rhythmic’; eitynes ‘procession’; eiti, inf. ‘go’: Latv. iet, id. Isophonic w. ON íð, pl. -ir. f. ‘deed’; Sw. cf. id “effort
eiuem ‘all right, come on! Skt. evám, id.; Gk. eien, id. (Li. isophonic eivà! is a dual form of ei-, see eimi)
eiuos, à (iuos, à) (an unidentified tree: ‘yew, gro
=== leaf 143
a; OCS acc. jọ; nom. rel.
eisio — eks, eKs- (əKs, Ks)
20
25
30
35
40
45
236
ja-Ze; Li. ji
eio, eia (ei), interj. “hey, come on’ Gk. eia; Alb. ejá; Lat. eia; Li. ei
eio, eiio (eiios) “his, her(s)' Oss. jä; Arm. iwr, Jur: Gk. heío, hop: OLat. eiius; Lat. eius; Olr. aí, á; MIr. é; Br. é; W ei; Cor. y; OCS jeje; Li. jo, jos
-ēið (extn. of “verbs of state") Hitt. parkw-iyami ‘am pure’; Lat. rub-eo; OCS rüdéjo; Li. rud-&ju; Latv. rud-&ju “am red? etc.
eiont- (iont-) “going” (act. pt.) See ei-mi, etc. Skt. yat; Gk ion, f. io(isa; Lat. iens, gs euntis; Latv. eiots, s.
eios, à “going; gait'. See ei-mi, etc. Skt. áyah, ayáb; Hom. éia, npl. “provisions for the journey’; Li. 6ja, &1jà; Latv. eja “path, way’; R cf. kol-ejà (fr. *quol-?), Cz. kolej “track?
-eios (agent-suffix) Gk. cf. khér-és, gs -80s ‘labourer’; Li. pie$-ejas “painter”, etc. Latv. mav-6js ‘diver’, etc.
e-iudh- (radical: iudh- ‘go, move? with relic of augment). See iudh- OE éode ‘went’; ME yode, yede, id.; OCz. jid, 3s. jide, id.
eke (eko, ekke, ekka, ek, ək) “behold”. Cf. eke, Ke Romani ak-, px.; Per. cf. ak-nūn ‘right now’; Kurd. ek -eke; Gk. cf. ek-ei ‘yonder’; Alb. k- in ky, kjo ('this, m. f?); Lat. ec-ce, hi-ce, etc: Osc. cf. ek-as; Umb. -ek; Ir. ac (fr. *ok or oK); Li. -k (in imperatives)
ek T. Cf. ego, eKhó Arm. es; OLI. e$ (mod. a3); Latv. es; Faliscan cf. eco, eko
(eK, ebe ‘behold’. Cf. eke, etc. and Ke) OCS jese! id.
ekno-, eKon- “eat, swallow, drink’. WP I, 112 Skt. a$nàmi, pp. asitáh eat: a$anah ‘food’; Av. as-; Per. a$; Tokh. AB yok- “drink”: yoke, yoko, yokiye ‘thirst’; yoktsi ‘drink’ Hitt. cf. ekumi “drink; give to drink’; MHG cf. nuocht, nücht, adj. ‘sober’ (vocalism obscure)
eks, eKs- (oke Ks) out: out of: (intens. & neg. px.) “very: not’. WP I. 116 Gk. ek, ex; ek-, ex-; Lat. ex; ex-; Osc. eh-; Gaul. ex-; W eh-, e-; OBr. es-, -s-; MIr. eas-, eis- (neg. px.) beside ach (except, fr. *oKs). Z-gde in Arm. c-; Alb. sh-; Go. us, ur-; Li.
237
i$. G cf. orig (‘primevaľ’, fr. *ksikós. See FK: EWDS: er-, ur-)
ekKskétros, à ‘dragon, sea-monster Tokh. A (?) arsal *poison-snake'; Lat. excetra; Ir. (?) eascar, m. ‘enemy’; OCS jasterü ‘lizard’ beside jesetrü ‘sturgeon’. (Doublets also in OCz ještěr, jeSCer & jeseter; R jàščerica & osëtr); Srb. jesetra ‘sturgeon’; Li. eškētras, erškētras, eršketas & arškētas, m. id.; OPr. esketres, id.
eKsque (eKske) ‘till; still, however’. Cf. WP I, 45 Skt. ácéha; Tokh. enske; Arm. cf. isk (fr. eKsk-?) “but, yet’; Gk. éste, éske; OCS ješte (and com. Sl.)
ekstamos ‘outermost’. WP I, 116. Cf. eKsto-, eks, ekstra Alb. i jashtëm; Lat. extimus; W eithaf, id.
eksto- (eKst-, oKst-) “out, outside; beyond, excep. WP I, 116 _ Arm. əst- (cpds. "out, beyond"); ost (prp. 'ac- cording to"); Gk. ektós; Alb. jashtë; Lat. cf. exta ‘bowels; middlings; dregs; must of wine’; Mir acht "but
eKstro, eKster- “outside; except, beyong’. WP I, 116. Cf. eKs-, etc. Lat. extra beside exterus, adj.; Osc. cf. ehtrad ‘outside’; OIr. echtar, echtair, id.; OW eithyr, W eithr ‘except, but’; Br
=== leaf 144
ani ‘horseman’; H-Hittite a$uwa-; Lyc. esve-; Thrac. cf. -espios, -aspios, adj.; Venet. ekvon (acc. sg.); Mlr. ech; Ir. each; cf. eachan ‘gale’; Gaul. epo-; Sequanian equos, pl. ‘gales’; Br. cf. é-al, éb-œl, W eb-ol ‘foal’; cf. Br. kén-ep, -eb “in foal’; OE eoh; ON jór, beside ess; Go. cf. aíhva-tundi (&horse-tooth', i.e. ‘briar; OS cf. ehu-skalk, m. ‘groom’; OLi. esva, Li. a$va ‘mare’. Extended forms; eKuolos, à in Lat. equulus, a: W ebol; Cor. ebol ‘colt, foal’; eKu-ridh- in Gaul. epo-redias, acc. pl. *horse-tamers'; OS eorid-folk, ierid-
eKskeétros, à — elg-
20
25
30
35
40
45
238
folk, coll. ‘troop of horse’; Ir. cf. eachraidh ‘cavalry’, eKuinos in Skt. a$vín, a$vinah; Lat. equinus
ekhó (theoretical form to accommodate Indic -h- with Arm. Balt. s/3) ‘T. WP I, 115. Cf. ego, eK and see J. Puhvel: Lg. 35.4.646-7. Cf. dhugotér, me$-, ĝenus for a similar problem Skt. ahám; Av. azom; OPer. adam; Oss. åz; Hitt. uk, ug-, ugg-; Arm. es; Hom. egón; Gk. egó; Alb. u, unë; Lat. ego; Faliscan eco; Osc. íív; Umb. ef; Go. ik; OHG ih, ihha; OE ic; ON ek; OCS ap jazü, ja (and com. SL); OLI. eš; Li. aš, ašen, asenai; Latv. es
el- (theme 1) ‘come, go; rise, raise’. Cf. sel- . Skt. cf. sam-aráh ‘concourse’; Arm. el, elk "eut rise, end: el! ‘go out"; elanem, aor. eli ‘go out, go up; Gk. éla! *come":; cf. perh. heílon (suppletive aor. of hairéo), and é- elthon ‘I came’; W cf. dêl ('approach', for *do-el-); (+ë in) ON áll “germ, sprout
el- (theme 2) ‘tree, forest". Cf. WP I, 152 Skt. cf. aranyam (forest; Arm. cf. eyevin, gs. -vno ‘pine’; (for an alleged Macedonian ílax, see WH and EM: ilex w. speculations. and cf. Fr houx ‘holly’ if fr. *ílicem. Alb. ilge, ilnje, f. holm-oak' are LWs fr. ilicem & lignea respectively); MIr. cf. allaid ‘wild; deer" beside elit ‘hind’; G dial. Ilme ‘elm’. (For OCS jelí “white poplar' & jela ‘fir see edhla). Br. cf. elw ‘aspen’
ela, os, is ‘awl, spindle’. WP I, 156 Skt. áraà 'awl, punch’; āņih ‘linchpin’, fr. *élnis; Arm. il, o-st. (spindle'. Dim.: ilik); OHG ala; OE æl "aw: (isophonic: Oss. ar, arä ‘shaft of car" and ON ál, pl. -ar, f. “strap, thong")
elonis (elnis, os, álonis) "deer" WP I, 154. (m. ‘stag’; f. *hind") Tokh. yàl ‘antelope or gazelle’; Arm. eyn, gs eyin ('hind'. Dim.: eynik *fawn"); Gk. cf. ellós, m.; W elain, f.; Br. élan, m.; EMG Ellend, Mod. Elen ‘elk’; OCS jelen, m. beside alünf, m. and lani, f.; R olení, m.; Li. éinis, m., eine, f.; Li. also álnis, m.; Late alnis, m.
elg- ‘miserable; misery; wretch’ (eleg-?) Arm. eyuk! “alas”; eyk “at least’; eykank ‘misery’ are ambig. as also Gk. élegos ‘mourn-
239
ing chant’; Icel. jálkur “hack, jade’; Li. cf. elgeta, m.f. *wretch'. (A parallel form *el$- for Arm. ec, Let (ruin, decay’; z-eyc, adj. “corrupt? is not ascertainable)
-elis, ios (noun and adj. extrí.) Arm. cf. eyk-eli ‘miserable’; Lat. mātru-ēlis; crud-elis; Li. broter-elis; numir-elis, etc.
(elisa, elisa. See al?sios. Laryngalism may account for fluctuation of the initial vowel: e:a. Cf. me$-, es?or, and a possible pre
```


## [2026-09-05T20:31:47.609Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^-emos\\|^emos\\|-emos (\\|-emos,\" IEC.txt | head -20; echo \"=== leaf 153/154\"; python3 - <<'EOF'\nd=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=d.split('\\f')\nfor i in (153,154):\n    print('=== leaf',i)\n    print(leaves[i][:2500])\nEOF"
}
```


### [2026-09-05T20:31:49.498Z] TOOL RESULT

```
3560:emos ‘holder’. Cf. emó & am- (2), amn-. Cf. WP I, 124 Lat. cf. auris ima ‘flap of the ear’; Cz. -jem, cpds.; OCS cf. néámü (*mute', for *ne-emo-)
=== leaf 153/154
=== leaf 153

15
20
25
30
35
40
45
254
so-, px. id.; Gaul. cf. Essui, pl. (a Celtic tribe of Brittany); OBr. eu- (in eu-les "good. voice); W hy- px; OCS omg ‘desirous’; OCz. cf. ochevny ‘wanton’
esus (esos, esi-) (2) “animal, breath, being”. Cf. es-mi, etc. Skt. ásuh (Ð “breath, life; Av. àhus (2) ‘world, place’; cf. áha ‘mind’; áhva “self, being’; Per. ahü deer": Arm. cf. ir, -i, -av, a-st. ‘thing, fact’; irav ‘rightly’; iravi, adj. ‘true’ from a type *esiiə)
esus (és-) (3) “god, demon’. Cf. esulos, etc. Skt. ásuh, id.; Av. áhus ‘lord’; Hitt. hassus ‘king’ beside eshas (‘master’. The u-st. with umlaut is functional; the a-st., IE o-st. is non- functional); Lat. erus, herus ‘master’; era, OLat. esa ‘mistress’; Gaul. Esus ‘God’; ON ass, i-st. “heathen god'
eteros basic form of a cpd. pron. w. the comparative extn. -teros. Cf. an-teros, iotero-, (ieter-), Kitero-, quetero-, etc. WP I, 99 Myc. cf. atero-weto (‘next year’. Ambig. ? *antero-); Gk. háteros, beside héteros; Alb. dial. jetër, jatér “other”; Umb. etram, f. sg. id.; OCH jeterü “a certain; some, any”
etesé (sentence particle) *so, well, but, then”, etc. Cf. iot-se, et-se
eti, eto, et “and, but, yet’. Cf. ati, atand WP I, 43. See et-se Gk. éti; cf. also ex-éti (cj. 'since"); Phryg. eti- (px); Alb. e; Lat. Umb. Pael. Fal. et; Olr. eti, eti-c; Mär eta ‘so; OW cf. etaw, eton; W eto ‘yet; Go. ib; OHG ith; ON eða, eðr; Blg.Srb. eto ‘since, as’; Li. ét, ét "but
etmn- ‘breath’. WP I, 118. See next Skt. atman, atmanah; OHG àdum (cf. atam, id.); OS athum; OFris. éthma; MHG àtem, MLG adem: Du. adem; OE &pm, id. (see FK: EWDS 17: Atem, Odem). (Consonantism obscure in Gmc.)
etór (etrom, Str) “internal organ’. WP I, 117 (Arm. irank “body, trunk’ is ambig.); Gk. étor “heart”; étron ‘belly’; OHG adara ('vein'; pl. tintestines); MHG àder (as OHG, also = ‘sinew, nerve); OE ædre ‘veim’; pl. ‘kidneys’; ON cf. æðr, as. & ds æði ‘vein’. (OCS jadro “bosom? indicates a variant consonant, cf.
255
Cz. ňadra ‘bosom’, fr. a type *en-endhro-)
et-se (et-sié-, eti-siet, e-te-siet) (particle or conj.) ‘so, be-it'. Cf. eti, siem (siet) Vedic átha; Skt. átha; Av. áo, a Arm. ete, te; Lat. etsi; cf. also Gk. éti, cj. ‘yet
eugh- (ügh-) (rage, curse, swear, vow, im- precate'. WP I, 110 Skt. cf. ühami 'expiate'; ogháh, augháh "eur. ge’; Av. uz- ('eulogize'. w. prepalatalisation); Myc. cf. euketoi ‘he praises’; Gk. eükhomai *vow, beseech, promise, exult, boast'; eükhos ‘vow, offering’; ON cf. ýgjast, refl. ‘go mad, rage’. (Arm. ogem ‘utter’ isambig. Cf
=== leaf 154
 *í, the so-called shva secundum. There are some unexplained initials in u-).
obhi, obhit-, see abhi, abhit-
oKs- ‘out’. Mir as-; W as-, id. Cf. eKs-, Ks
oIm- (olim-, lim-, lem-, Im-) ‘elm’ (of un- certain phonology. LW? or substrate?) Ir. ailm, leamh; Lat. ulmus; OHG &lm, OE elm; ON álmr; MHG (also) ilme; EGer. Ilme;
et-se (et-sié-, eti-siet, e-te-siet) — ombros, is (omber-)
20
25
30
40
45
256
eusó (us-) ‘burn’. Cf. us-
Skt. ósami, usnami; Av. u$-; Gk. heúo; Lat. üro; ON cf. usli ‘embers’; cf. (?) o-gde Av. aošō ('death'. Here: FJ: HZS)
euuis, io (euis, io) ^wear; footwear. See next.
Lat. cf. ex-uviae ‘spoils’; OCS cf. ob-uví “foot- wear'; Li. cf. áp-avas, id.; Latv. apavi, mpl. id. euuó, ið (euo, euno) ‘put on garment, shoes; wear Lat. md. ex-uo, -uére; OCS ob-ujo, -uti, freq. -uvajo ‘put on footwear’; iz-ujo etc. ‘take off (shoes); Li. cf. aunü, aŭti, pf. aviaü ‘put on shoes’; aviù, -êti “have on (shoes); Latv. aunu, aut (as Lith.)
euaio ‘exul? (based on an interj. *eua, *euuai, etc.). WP I, 110 Gk. cf. euázo, id.; Latv. ovo, -are, id.; OCz. cf. ova! ‘behold’; Slovene evo! id.
-euó, -euuó (1) frequentative verbal extn. Gk. théreuo "bunt": nuktereúo ‘spend the night; OCS lénujo, -ovati ‘lounge’; Li. Svil- pauju, -auti ‘keep on whistling’. Cf. also Cz. u-bytuji (lodge, quarter’: Gk. phüteuo *plant")
-euó, -euuo, io (2) functional verbal extn. as in Li. piemeniauju, ti, v. “be a shepherd’; tarnauju, ti ‘serve’; Gk. grammateuo, thera- peáo, etc.; OCS slugujo, -ovati ‘serve’, etc. LLat. punctuare and Lat. mütuari are merely formal equivalents to (1) and (2)
OCS ilímü & ilemü. Cf. WP I, 152
-alos, (1) noun-extn. in Gk. krótalon: Ir. crothal: Li. kràtalas ‘rattle’; (2) adj. extn. in Gk. homalós; Lat. gerulus, querulus, bibulus (full bibliography in Zucchelli: Studi sulle formazioni latine in -lo-. Parma, 1970); OE etol ‘voracious’; Cz. jedlý “eatable”, etc.
ombros, is (omber-) in Skt. àmbaram 'firma- ment’; Lat. imber beside imbrex 'roof-gutter' and ambrices ‘rafters’; Gk. ómbros (vocalism of ónoma). (A simplex may be present in Skt. ámbu *water' & Arm. amp 'cloud', but a
251
Skt. ámbhas "water" and an Arm. amb “cloud? also occur). WP I, 131
ombros, ambros ‘sour, sorrel in Skt. amblah ‘sorrel’ and OHG ampfaro ‘sour’; G Ampfer ‘sorrel’. Cf. omros (amros) below
ombhi-, etc. see ambhi-, etc.
omelom, see amelom, and add OCS imela ‘mistletoe’; OPr. emelno, n. id.; cf. LLat. imel-ita *dwarf olive”
omo- (?) in Skt. ami ‘these’ and Ober ima “this”
omos ‘raw’. See ümos
```


## [2026-09-05T20:32:01.664Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"superlative\" IEC.txt | head -20; echo \"=== mmos\"; grep -n \"\\-mmo\\|-mos (\\|^-mos\\|-emos\\b\" IEC.txt | head -20"
}
```


### [2026-09-05T20:32:01.728Z] TOOL RESULT

```
214:Sp. Spanish subj. subjunctive substr. substrate sup. supine superl. superlative Sw. Swedish Thrac. Thracian Tokh. Tokharian Ukr. Ukrainian Umb. Umbrian v. verb
3787:-amos, superlative extn. in Skt. gurut-amáh, apamah ‘heaviest; hindmost’; Av. frat-omo, up-amo ‘foremost’; ap-omo ‘last’; Hitt. sept- amas ‘seventh’; Alb. i prap-ém, i pas-ém ‘hindmost’; Lat. inf-imus, post-umus ‘lowest; latest"; Osc. ness-imas, f. pl. ‘next’; Olr. ness- am ‘next’; tress-am ‘strongest’; W nes-af, elei-af ‘next; least’; Go. aft-uma “latter, last’; OE hindema ‘hindmost; MHG  zésem ("straight line”, fr. *deKsemo-); Gk. hebd-om os; OCS sedmyi; OLi. sekmas “seventh? beside art-imas “near”; OPr. sept-mas “seventh? beside ilg-imai, adv. “at length'. Cf. also Faliscan max-omo ‘Maximus’; Per. Cahar-um “4th2; Kurd. cuvar-em, id.; Per. haft-um, Kurd. hewtem *7th., etc.
3808:onó, onói “upon; above, downward’. WP I, 58. Cf. ano (2) For *onoi, cf. OCS naj- (superlative px.). The initial occurs in Gk. anüo, áno, v. ‘do, achieve’: Li. anüoju, id. (Bois. & Hof. untenable)
6274:-istos (-isthios) (1) superlative extn.
9410:ladstos “weak, faint, immature, frail’. Cf. lados (ladsKó) Lat. cf. sub-lestus “weak, faint, slim, slender, trivial; Alb. i lashtë “immature, premature, early’; cf. the superlatives: OS lezto (letsto) ‘last’; OHG lezzist, OE latost, Du. laatst, etc.
13060:‘full, fulsome; flow, flood’. WP II, 63 Gk. pléos, pleios, adj. ‘full’; pleiðn, pléon, adj. ‘more’; pleistos, adj. “most; greatest’; Lat. cf. plerus, adj. “full, most’; plerum-que, adv. ‘mostly’; Olr. lia, adj. ‘more’; ler, m. “flood, open sea’; lir, adj. “numerous; crowded’; Ir. leor, adj. indecl. ‘plenty’ beside léar-, léir-, px. “full-, fully-; OBr. lirou, pl. “tide, open sea; OW & W Ilwyr, adj. ‘total’; adv. ‘quite’ beside W Uer, m. (2) ‘satiety’. The superlative form occurs in Av. fraesto ‘most’; Gk. pleis- tos, id.; OBr. liaus, adj. “numerous; Br. lies, adj. ‘many’; Cor. lias, m. & adj. d: W lliaws, id.; ON flestr most: fleiri, adj. ‘more’
13514:priiomos, form of superlative akin to pri-, cf. proi-, proiomos ‘foremost’ Gk. cf. (proper name) Priamos Schiet leader’; Lat. primus; MIr. riam, ríam, adv. “formerly, before’ beside riamh, adv. "ever": OW rwyf, m. ‘ruler, leader’; cf. also W rhwym, m. id. (perh. from Irish, w. preservation of -m-); OCS prémáü, adj. (straight; R prjamój, id.; Cz. přímý, id. beside OCS prémo, adv. *before- hand”; Slovene prema, prp. ‘against’; Ir. cf. also réim, pl. -eanna, f. *power, supremacy'
=== mmos
11179:-mos, de-verbal suffix in formation of nouns Skt. cf. ruk-máh ‘gold ornament’; Hitt. werite- mas ‘fear; Arm. gea-m, gs gemo, ab. s. gemov ((tissue', fr. *guiu-, q. v.); or-m, o-st. ‘wall; Gk. gá-mos (“ marriage”, fr. *$n-, q. v.); iug-mós ‘shout’; kom-mós, stolmós, pal-mós, etc.; Alb. shkel-m, m. (*kick', fr. shkel, v. id.); ngul-m, m. ((thrust, fr. ngul, v. id. See kulið); Ir. gliogr-am, m. ('rattle', fr. gliograim, v. id. See glig-, gligor-); geall-am, m. ( ‘promise’, fr. geall- aim, v. id. See gheldhó); W cf. deddf, f. law: Gk. tethmós, m. id.; Go. cf. maip-ms, m. ('treasure'. See moit- ‘turn, change); MHG cf. bar-m, sm. ‘lap, bosom’; g&l-m, sm. (noise, fr. gëllen); Cz. prám, R poróm Craft ferry” Cf. per-, por-); Li. jaüs-mas, m. (feeling, fr. jaüsti ‘to feel)
11216:motos, à, is, los, iə (2) ‘measure’. Cf. met-, metos (1), metros, metis and WP II, 237-9 Gk. cf. à-motos ('excessive, beyond measure’. Semantics of Alb. pa masë, id.); é-mos (Doric: à-), adv. “when, while’; té-mos, adv. Chen, Semantics of Li. tuo-mét ‘then’); cf. also en té-mos *thereupon'; Alb. matë, f. ‘measure’ beside masë, id. (fr. *motio); Li. mátas, m. ‘measure’; Latv. mats, mass ('corn-measure, milling-fee', fr. *motos & *motios resp.); cf. Li. (e-grade) tuo-mét “at that time’; mastas (*yard-stick', from a type *mostos, fr. *mot- tos)
```


## [2026-09-05T20:32:17.849Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\n# find leaf containing line 3787 (1-based)\nimport re\ncnt=0\nleaf=0\ntext=''\npos=0\nfor i,l in enumerate(lines,1):\n    if i==3787:\n        target=l\n        break\n# count formfeeds before\npre='\\n'.join(lines[:3786])\nprint('leaf index', pre.count('\\f'))\nleaves=d.split('\\f')\nli=pre.count('\\f')\nprint(repr(leaves[li][:200]))\nprint('...')\nprint(leaves[li][-1500:])\nEOF"
}
```


### [2026-09-05T20:32:19.583Z] TOOL RESULT

```
leaf index 154
' *í, the so-called shva secundum. There are some unexplained initials in u-).\nobhi, obhit-, see abhi, abhit-\noKs- ‘out’. Mir as-; W as-, id. Cf. eKs-, Ks\noIm- (olim-, lim-, lem-, Im-) ‘elm’ (of un- ce'
...
ud', but a
251
Skt. ámbhas "water" and an Arm. amb “cloud? also occur). WP I, 131
ombros, ambros ‘sour, sorrel in Skt. amblah ‘sorrel’ and OHG ampfaro ‘sour’; G Ampfer ‘sorrel’. Cf. omros (amros) below
ombhi-, etc. see ambhi-, etc.
omelom, see amelom, and add OCS imela ‘mistletoe’; OPr. emelno, n. id.; cf. LLat. imel-ita *dwarf olive”
omo- (?) in Skt. ami ‘these’ and Ober ima “this”
omos ‘raw’. See ümos
-amos, superlative extn. in Skt. gurut-amáh, apamah ‘heaviest; hindmost’; Av. frat-omo, up-amo ‘foremost’; ap-omo ‘last’; Hitt. sept- amas ‘seventh’; Alb. i prap-ém, i pas-ém ‘hindmost’; Lat. inf-imus, post-umus ‘lowest; latest"; Osc. ness-imas, f. pl. ‘next’; Olr. ness- am ‘next’; tress-am ‘strongest’; W nes-af, elei-af ‘next; least’; Go. aft-uma “latter, last’; OE hindema ‘hindmost; MHG  zésem ("straight line”, fr. *deKsemo-); Gk. hebd-om os; OCS sedmyi; OLi. sekmas “seventh? beside art-imas “near”; OPr. sept-mas “seventh? beside ilg-imai, adv. “at length'. Cf. also Faliscan max-omo ‘Maximus’; Per. Cahar-um “4th2; Kurd. cuvar-em, id.; Per. haft-um, Kurd. hewtem *7th., etc.
omros (omoros, ombros, mros) 'sour, bitter'. Cf. WP I, 179 & II, 235 Skt. amlah ‘sour; vinegar; wood-sorrel'; Gk. cf. am- in am-oómon (“Indian spice’, for *om- osmo- 'sharp-smelling"); Maced. (?) cf. abro- ‘astringent’; abarü ‘marjoram’; Lat. cf. amärus (-à- unexplained); Olr. amar ‘grief; W afar, id.; OHG ampfaro ‘sour; wood-sorre; OE ampre ‘sorrel’; Du. dial. amper ‘sharp, sour”; Sw. amper, id.; Li. amar
```


## [2026-09-05T20:32:30.101Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\nfor tgt in (6812,10120):\n    pre='\\n'.join(lines[:tgt-1])\n    li=pre.count('\\f')\n    print('line',tgt,'leaf',li,'printed ~',li-66)\nleaves=d.split('\\f')\nprint('=== leaf for 1066:')\nprint(leaves[6812 and 0][:0])\nEOF"
}
```


## [2026-09-05T20:32:30.990Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT anghu/ang honey\"; grep -n \"Honig\" BRT.txt | head -20"
}
```


### [2026-09-05T20:32:31.850Z] TOOL RESULT

```
line 6812 leaf 107 printed ~ 41
line 10120 leaf 152 printed ~ 86
=== leaf for 1066:
```


### [2026-09-05T20:32:31.892Z] TOOL RESULT

```
=== BRT anghu/ang honey
14791:•  j.  paenaena-  Adj.  (fem.  'nl-)  'aus  Honig bestehend,  bereitet";  *'nyä^t  (ISt)'>  zao- %raya  N.57.
14792:Ableit.  aus  *paena-  m.  'Honig'');  mp.  attgu- fin,  np.  angHÜn  'Bienenhonig'.  —  Ob  zu  lit. /Ami  'Milch'?  {s.  daiu  JSchmidt  Krit.  :<h)'). —  Pü.:  fehlt. —  ")  So  der  Ausgang  in  T.  — >)  Die  Bedeutung  'Milch'  ist  für  *ptüna-  nicht wahrscheinlich,  obwohl  sich  ja  np.  anpibln allenralls  als  'Bienen milch' fassen  Hesse;  vgl. Hb«.  PSL  19,  AGr.  /.  124.
27540:—  hamqm  . .  *xsäudrim  (sd.)  °rqm  (AS£) bamts  hamqm  ^papikwqm  N.  64;  64';  — *'paettalnya(sd.yit  °raya  (ISf.)  "auch  mit einem  Honigtrank  Opfer"  N.  57;  —  mit payB  fsufa  (sd.)  're  (LSn.)  nHi  gSu?  °re büDSmainc  paitiMirt  V.7,77;  —  vispa- nqmca  aita^qm  pasvqm  asmaniv3  (sd.) 'ra  (ISn.)  .  .'/rabaröi/ yf.i8.jo;  —  yS ape  'rqm  frabaraite  N.48;  Yt(j.3,  V.^. 14  PüZ.;  —  aiwyS  °ra  frabarHS yaoidäta dakmB.pairisih  Y.ö'j.io;  ö'Ä  14,  Vr.  rr.  3, V.I2.  a,  79. 34,  N.*65,  ^i',  ■•"T/;  — yaica ml  layäsca  hazahisla  . .  °rä  frabarät  P. 22;  —  °rä  hl  uzbaraym  YtÄsS;  — altasf  tl  ^atar»  'rä  N.  ^5 ;  —  yS  vS  äpJ . . yazäite  .  .  dahmi}.pairi.aKhar^täby5  ^rabyö Y.68.10;  10',  3,  j(?.i,  57.3,Vr.ö".  i,Yt. '■9.  J-18.  5-8,  9.  ^'-^5,  10-6,  lö,  31,  13. 94,  /7.2',  G,  J.  7,  N.  77,  Vd.5,  Any,  2^;
```


## [2026-09-05T20:32:41.413Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14780,14795p' BRT.txt; echo \"=== HUB angubin\"; grep -n \"angub\\|anguv\\|Honig\" HUB.txt | head -20"
}
```


### [2026-09-05T20:32:41.493Z] TOOL RESULT

```
Pii.i  b  c  k;  vgl.  zu  baiidräjah:
•  j.  tbista-.  'Uisla-  Adj,  PPfP.:  s. Ibai^-.
KompE.  —  li.  dvif/ä-  Adj,
•  j.  (bisyant-,  g.  daibisyant-**  Adj.  'feind- lich, fcind,  inimtcus':  rapantl  .  .  at  .  . -yanti  zastäi/täi/ (sd.) . .  Y.34. 4;  —  aei'qm *°yafitqm ''>  . .  tbaesä  \t.jo.'j6;  —  aurva- 'äianqm  'yantqnt  Y.57.  a6,  Yt  J^.  31,  *Vyt. i^";  Yt  74.34,  ^■57-''f>\  —  aurvahafiiyS pars  'yanbys  Yt.  13.  69,  Y.  68.  13;  Yt.  10. 75,75.31;  — -  vlspim  aurvd^jm  °yanttm vXspfm  ay)m  °yant>m  A.  7,  10;  —  vanä{ vupe  'yantö  Yt  75.54; — pala  nS  'yantat pairi  SrB.5.
PPA.  lum  V.lban-,  —  Pü. :  imär.  —  ')  S  i6S. 56.  —  ')  NA.  'yatqm,  s.  Var.  —  3)  In  den Hds,  TCideibt.
•  j.  (biS'vant-,  g.  daibiä'vant- '>  Adj. 'feindselig,   feind';    tbü'vatqm   tba^ä  H.g.
8;  28;  —  daibirvatö  dt'aliS  Y.2S.6. Vi..:  bSiiiär.  -  i>  S  368.  56.
*  }■  P^°>  /"%  tii'^  KompA.:  sva.  apa. In  ptarmta    und  fiäyaozä   (beide    an   wenig Vertrauens  werten  Stellen). — pa',fä.'  können sich    zu    ai.  ap&   verhalten  wie  ai. />'  zu  äpi\ vgl.  ksl.  podati  'atn-liidyai'.
ob,Google
8i7
paenaena-
•  j.  paenaena-  Adj.  (fem.  'nl-)  'aus  Honig bestehend,  bereitet";  *'nyä^t  (ISt)'>  zao- %raya  N.57.
Ableit.  aus  *paena-  m.  'Honig'');  mp.  attgu- fin,  np.  angHÜn  'Bienenhonig'.  —  Ob  zu  lit. /Ami  'Milch'?  {s.  daiu  JSchmidt  Krit.  :<h)'). —  Pü.:  fehlt. —  ")  So  der  Ausgang  in  T.  — >)  Die  Bedeutung  'Milch'  ist  für  *ptüna-  nicht wahrscheinlich,  obwohl  sich  ja  np.  anpibln allenralls  als  'Bienen milch' fassen  Hesse;  vgl. Hb«.  PSL  19,  AGr.  /.  124.
•  j.  'pacman-  n.  'Muttermilch';  yU  (nätnl. aridvt)  vupanqm  hütriünqm  däitlm  ra- %wTtn  'ma  ava.daraiti  Y.Ö^.z;  Vyt  50; —  Aä  (näml.  andvt)  .  .  yaeiäa%äiti  .  . ar^qm  xhtdrä  hä  x^a%rinqm  garm>q  hä xia%rinqm  'ma  Y,  65. 5.
KocnpE.;  Ab!eit.  —  Zum  V.  pay-,  —  S.  'pac- man- and  auch  paenaena-.  —    mp.  (Pü.)  p/m :
5.  noch  JSchmidt  Krit  104.
=== HUB angubin
562:keiten im Wege. — Afgh. gahUna *Honig' halt Geiger
3509:madu' durehweg mit 'Wein'. Die Bedeutung *Honig'
4322:Griinden, ebenso in angubw, angabin *Honig* etc.
4880:phi. tuxsdk. Vgl. auch angabin (A. M.) Honig' = angubln.
4930:und' m zn t: in *dieser = skr. ena-; angnbln *Honig*, bal.
4931:bihtag, arm. gazbSn (np. gazangubln); dgln *Sitte* = BiTvn.agen?
6239:abresum 'Seide', arm. aprisum ; angubm 'Honig , phi. angpeti^
```


## [2026-09-05T20:32:52.588Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index ang\"; grep -n -i \"angubin\\|ANGUBIN\\|angbin\" incoming/ARY/ARY_latin_index_pages.txt incoming/ARY/ARY_pages.txt | head -10; echo \"=== MON angubin\"; grep -n \"انگبین\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -10"
}
```


### [2026-09-05T20:32:52.664Z] TOOL RESULT

```
=== ARY latin index ang
=== MON angubin
incoming/MON/MON_2vol_Adena_v1_djvu.txt:25131:گزانگبین غبر از گزانگیین مستخرج ار 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:71722:منگ انگبین» تا ری( کید ) اکن | بر 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:77052:سرشکث انگبین: (کد.) ترشی که چاشنی 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:78688:سرکه و انگبین با شکر و قند سازند. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:87525:شهد: 30:۵ [ع.] (ا.) انگبین» عسل. شیرینی. 
MON_part1.txt:25131:گزانگبین غبر از گزانگیین مستخرج ار 
MON_part1.txt:71722:منگ انگبین» تا ری( کید ) اکن | بر 
MON_part1.txt:77052:سرشکث انگبین: (کد.) ترشی که چاشنی 
MON_part1.txt:78688:سرکه و انگبین با شکر و قند سازند. 
MON_part1.txt:87525:شهد: 30:۵ [ع.] (ا.) انگبین» عسل. شیرینی.
```


## [2026-09-05T20:32:53.536Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW apis\"; grep -n \"^apis\\|apis, -is\\|apis „\" LEW_1910.txt | head -10; echo \"=== LAT apis\"; grep -n \"^apis\\|apis \" LAT.txt | head -10"
}
```


### [2026-09-05T20:32:53.610Z] TOOL RESULT

```
=== LEW apis
=== LAT apis
920:abaddlr ind.: 6 paixoTuoC; "abaddir deus dicitur, quo nemine lapis uocatw
3428:apis,unguis, etc. V.aqua.
4399:apis, -is (g6n.pl. a pum ou apium, cf. Neue-Wagener, Forra? I 359 , ce
4416:apis; apiaster m. et apiastrum n.: melisse; apiastellum: renoncule,
9641:Capis a en germanique un correspondant exact: got. hafjan (pr^t.Ao/)
28624:h.: aequamentum', CGL V 309,3 h. dicitur lapis quo pondus exaequatur',
29248:ignesco,-is: s'enflanmer; igniarius ( ignarius) i. lapis "pierre a
33376:sens qui apparait a 1 'epoque imperiale: Coi. 9,13,1, apis se confestim
34281:aussi le sens de "liquefier", cf. Plin.36,63 lapis liquatur igni. De
38734:meule", lapis molaris, et simplement molaris m. "meule" et "molaire".
```


## [2026-09-05T20:32:56.361Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4399,4425p' LAT.txt"
}
```


### [2026-09-05T20:32:56.418Z] TOOL RESULT

```
apis, -is (g6n.pl. a pum ou apium, cf. Neue-Wagener, Forra? I 359 , ce
qui indique un ancien thfeme consonantique avec 6largissement partiel
en -i-, comme canis, mSnsis, etc., v. Ernout, Philologica, p.i3S et s.)
f.: abeille. - Ancien, usuel. - M.L.535.
Derives: apicula (rare mais deja dans Plaute, Cu.10). M.L.533; apia¬
rius: apiculteur, M0L.533; apiarium: rucher (cf. Geli.3,30,8), M.L.531;
apianus usite ai feminin apiana (uuaj "raisin affectionn 4 des abeilles";
apicius: meme sens. V. aussi apiun, apiastra.
Les dialectes indo-europeens qui vont du slave a 1 'indo-celtique
ont eu un nom de 1'"abeille" inconnu aux autres langues: v. sous lat.
fucus: ce nom etait de la forme *bhei~. Il n'est pas impossible que
ap~, api-, suppose par le latin, ait quelque rapport avec ce mot.
Mais on ne saurait pr6ciser.
apium, -I n.(apius a basse 6 poque) : 1“ ache des marais; 3“ persil.
Atteste depuis Virgile. Panroman sauf roumain. M.L.536; germ.: v.h.a.
f Pfi.
Derives: apiacus: d'ache; apiana: camomille (Ps.Apul.;, cf. toutefois
apis; apiaster m. et apiastrum n.: melisse; apiastellum: renoncule,
bryone ou couleuvr6e (se dit aussi apium risus); apiatus: bouilli avec
de 1'ache, tachete, mouchete (de mensis citreis, ueluti grani conge¬
rie); apiosus: se dit d'une maladie du cheval " cuius et mens hebetatur
et uisus" Veg., 1,35,3,3; cf.3,10. On 1 'explique siue quod apio cura¬
batur, siue quod ui magica apii putabatur oriri ?
Cf. aussi petrapium et apidgo ?
Apiun est sans doute " 1 'herbe aux abeilles" et correspond ainsi que
apiastrum au gr. neAicfuXXov, (ieAiooDcpuAAov„cf .Pseud. Ap., Herb.119; Varr.,
R.R.3,16,10; et id. i6id. 3,16,13, oportet doni serere quae maxime se-
```


## [2026-09-05T20:32:57.513Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4318,4326p' HUB.txt; echo ---; sed -n '4876,4884p' HUB.txt; echo ---; sed -n '6236,6242p' HUB.txt"
}
```


### [2026-09-05T20:32:57.614Z] TOOL RESULT

```
paz. phi. Maraspand^ arm. Maraspand^ zd. mqdrem spentem;
dadistdn 'Urtheil' = paz. dadastan. phi. datastan, arm. da-
tastan; abisx^ar *Tranke* (oben p. 5) u. s. w. .
In siibcin *Hirt' = zd. *fsupana- blieb u aus lautlichen
Griinden, ebenso in angubw, angabin *Honig* etc.
In der neupersisehen Poesie ist ofter da ein Vokal {e)
zii lesen, wo friiher der Compositionsvokal stand oder ge-
standen hatte (vgl. zlnehar^ yadegar Fird. I, 131, 34; name-
var 132, 55 etc.), doch geschieht dies nur metri causa, da
---
phi. apuxS(ly(i)Snlk; abr^am *Seide' = abresum, arm. apriSum;
jfavan 'Jungling' = juvdn, zd. skr. yuvan-. Fur hamana =
paz. humdna u. s. w. (oben p. 106) ist wohl humdnd zu
sprechen, wie tuxsd fiir taxsd (oben p. 47) = paz. tuxsa,
phi. tuxsdk. Vgl. auch angabin (A. M.) Honig' = angubln.
§ 24. Inl. u wird zu i in : dbistan *schwanger = phi. apus,
zd. apu&ra- =: *apw^ra-; tihf 'leer = pSz. tihf, phi. tuhik
Shk. 269; diz- *b6se* = duz, ap. dws-, zd. dus-, dui-; pisar
'Sohn* = pusar (nach Horn durch pidar beeinflusst) ^) ; misk
---
sdyisn ; bar, abar auf, iiber , ap. upariy ; bd *mit', skr. updke;
bayad *ist nothig, phi. apdyat; dbis-ian *schwanger , zd. *^/?w-
d^ra- (oben p. 5) ; dsob *Verwirrung, phi. dsop (s. oben p. 7);
abresum 'Seide', arm. aprisum ; angubm 'Honig , phi. angpeti^
arm. gaz-pen ; Dbdstan anfiillen, verschlingen', phi. opdrtan ;
bob Tater' aus *pa5 = phi. *pdp (oben § 65); -bad, -bud
'Herr (in Komp., vgl. H. 188 und 1115), zd.paiti-; biydbdn
```


## [2026-09-05T20:33:08.921Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6740,6760p' SOD_pages.txt; echo \"-----\"; sed -n '6805,6825p' SOD_pages.txt; echo \"===== 2201\"; sed -n '10115,10130p' SOD_pages.txt"
}
```


### [2026-09-05T20:33:08.998Z] TOOL RESULT

```
       GMS 659; Frag. Lcn. 49.5, 50.4, ynTywnc 81.9                                     riser'z(one
                                                                                               'wny who rises)
 1039 'nywnc'yS   B, S               <c^.Ji>(^U                                        GMS 55
      anyonciS, anyoncT/cO OnywncyS)                                              1055 'nj'wny M
      likewise
                                                                                        anzawnc, anjonc           On/Avny, >z}wny)   -^nz'wn'k,
       GMS 1109; TSP 2.927; BSTBL; MDii; Bugut. Insc.
         -w, MDii 3R 15                                                                 life giver, saviour
 1040 }nywncy5 =* 'nywnc'yS                                                            BBB; W-Li; GMS 656, 894
                                                                                  1056 'nj'wynyy M                                         ^J'xj
1041 *ngwpyn        M =¥ 'nkwpyn
                                                                                        anzawene Cnz'wyny)
1042 'nywst-        B =» 'nyw'st-
                                                                                        saviour, life giver                            J-^j '.
1043 'nywst'k       B                            cJs^    it

      anxwastc ©pp.        ^nyw'st                            ZjfpJaS i                GMS 894
      cut, broken                                                                 1057 >njmn M
                                                                                                                                              J*^         °jy
      TSP 2.118, 119 n pl70                                                             assembly
                                                                                        anjaman ©ob. -y =»Jncmn, 'ngnVn
-----
                                                                    TSP 9.133
 1065 'nkr'yp- B                      J-h~^- (oJ^lj^^y^
      angryp ? ©impf. mnk^yp                                  1075 >npst-    S                                        o^i
      Go)agitate                                                    anpast   ©pt. st. ^'np'st-, 'mpst- 'mst-, 'mpd-
      VJ 1000
                                                                    (w)fall453; Hen. Tales. 483.19; Frag. Len. 57.5
                                                                    GMS
 1066 'nkwpyn      B, S                               ^i
      angupen      Ongwpyn) ©<*angupaina-; Av.                1076 >npt-     B, S                                     o^Usi

        paena                                                       anpat ©impf. mnpt      ^}mpd-, 'np't-

      honey                 4                                       Go)faII
      TSP 19.7, 16 n p232; BSTBL, Padm. 40; KG 368                  TSP; SCE; BSTBL, Vim. 128; MSP bl5; Frag.
                                                                      2a.l7; GMS 633
 1067 'nkwst(h)     B, S                              ^i
      angusl                                                  1077 >ns»c- B => ^s'c-
        }ngwsl OnkHvst)   ©ob. -y; pi. -//   ^p>5y >nkwst,
                                                              1078 Wk     B                      ^jo^^jjL.
      finger
                                                                    ansak ©<*ham-sdka ^'ns'kCy)
===== 2201
      enakuc ? ©ena <haina ? (+kuc) =^(yyn,^wc
      slander                                                             VJ 33; TSP 6.167; Hen. Texts. 733

         STii 5.43; Gersh. Sogd. Cpds. 1945, 141                    2200 'ynd'y =» >yn5

 2189 >ync C, B, S                                           jj     2201 >ynkw B                  (^\ ijJ^\)^\ ^^
                                                                         inku ©<Skt. hingu, MP angu
      i/enc Oyns) ®<*yaunika-> Yaghn. inc, enc            ©-/z
          pi. -yst   =^yst, 'yncyst, 'ync
        woman                                                             Hen. AION 1965, 36 n 1
        STi 36.15, 83.13; Sund. AoFviii 1981 p213; C2               2202 'ynkwmync         B                                ^..^
                                                                         inkumenc
           gloss.; BSTi wydwc >ync; >yncK VJ; SCE 232,
           560; BSTBL, Padm. 67, Vim. 153; MD; Frag.                         gum
                                                                          (of) gum
           Len.; TSP n p207; -cwh.SCE 357                                 TSP 8.111 n p216; Hen. AION 1965, 36 n 1 Bcnv.
```


## [2026-09-05T20:33:27.486Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT angu-\"; grep -n \"j\\.  angu\\|angu-\\|'angu\" BRT.txt | head -10; echo \"=== BRT paena\"; grep -cn \"paena\" BRT.txt"
}
```


### [2026-09-05T20:33:27.545Z] TOOL RESULT

```
=== BRT angu-
21517:(auf  welchem,    näml.  Berg)  das  Han  -  oder der  Asphalt  -  (wächst)'.  —  VgL  «L  jälaii-  n. 'Gammi',    np.  iad  'Gummi',   angu-iad  'Harz', —  ■)  So,  ohne  Trennung,  alle  guten  Hds, j.  "yakva  Yt.  10.   2S:  s.  ya-,  Sp.   1304  O.
27940:yim  'rpm  nqma  ..yim  maiyäka  avi  duiva- ^avJtS zairimyaksm^&A.)  nqma  ao/ai/e"dcn Dasva  Z.  mit  Namen,  den  die  Übel- redenden Leute  Z,  nennen"  V.  13.  ö. Komp.;  zairimya-  +  *a/mra-  'des  Glieder  (oder Zehen)  in  einem  festen  Gehaus  stecken';  a  in der  KompFuge  statt  £  (bi.  i,  %  sgS.  ^),  %  36S. 3  b.  *aoura-  (statt  'angura-,  %  268. 47  c)  m. 'Glied'  oder  "Finget,  Zehe';  vgl.  ai.  anga- n.  'Glied',  aiigülof-  f.  'Füiger,  Zehe';  woss. ong  'Glied',  änguljä  'Finger*.  —  Vgl.  ioirim- yäia:  —  ai.  vgl.  harinu/a-  m.  'Schildkröle'.  — Pü, :  transskr.  [larimangur),  Npü. :  läi  fait.  — <)  Sa  nach  Npü.  nnd  Gü. ,  deren  Angaben von  der  Etymologie  nnterstätit  werde«.  GcR. OK.  160  denkt  vielmehr  an  den  Maulwurf. S.  noch  Sp.  Komm.  i.  297.
=== BRT paena
4
```


## [2026-09-05T20:33:28.196Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hangub%C3%A1ynah",
 "prompt": "Give the reconstruction page for Proto-Iranian *Hangubáynah: its meaning, morphological analysis (compound of what elements), and descendants."
}
```


### [2026-09-05T20:33:34.769Z] TOOL RESULT

```
# Proto-Iranian *Hangubáynah

**Meaning:** This reconstructed term denotes "honey" or "beeswax."

**Morphological Analysis:** The word is a compound formed from two elements:
- *Hángwr̥* ("extract, resin")
- *báynah* ("bee")

**Grammatical Classification:** It functions as a masculine a-stem noun in Proto-Iranian.

**Descendants:** The term evolved into numerous reflexes across Iranian language branches:

- **Northeastern:** Sogdian (angupēn), Khwarezmian (ʾnkby)
- **Southeastern:** Pashto (angabin, gabinë), Shughni (agmīn), Yazghulami (agmin), Parthian (angubēn)
- **Northwestern:** Kurdish (hengiwîn, hingivîn), Talysh (anqevin)
- **Southwestern:** Middle Persian (angubēn, angmīn), Classical and Modern Persian (angubîn/angobin)

The compound structure reflects the semantic connection between bees and honey production across ancient Iranian languages.
```


## [2026-09-05T20:33:51.988Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD maximum\"; grep -n -i \"maximum\\|minimum\" AHD_watkins1985.txt | head -12"
}
```


### [2026-09-05T20:33:52.050Z] TOOL RESULT

```
=== AHD maximum
732:form *m6-ro- in Gaelic mor, big, great: CLAYMORE. [Pok. 4, mé- 704.] mé-4, To cut down grass or grain with a sickle or scythe. Contracted from *mea-. 1. Germanic *mé- in Old English mawan, to mow: Mow?. 2. Suffixed form *mé-ti- in Germanic *médiz in Old English m#th, a mowing, a mown crop: AFTERMATH. 3. Suffixed form *mé-twd-, a mown field, in Germanic *médw6 in Old English méd (oblique case m&@dwe), meadow: MEAD?, MEADOW. [Pok. 2. mé- 703.] med-. To take appropriate measures. 1. a. Germanic *metan in Old English metan, to measure (out): METE!; b. Germanic derivative *m#t6, measure, in Old English gem&te (ge-, with; see kom), “commensurate,” fit: MEET?. 2. a. Latin medéri, to look after, heal, cure: MEDICAL, MEDICATE, (MEDICINE), (MEDICO); METHEG- LIN, REMEDY; b. Latin meditdri, to think about, con- sider, reflect: MEDITATE. 3. Suffixed form *med-es-, replaced in Latin by *modes- by influence of modus (see 4. below), in: a. Latin modestus, “keeping to the appro- priate measure,” moderate: MODEST; IMMODEST; b. Lat- in moderdre, “to keep within measure,” to moderate, control: MODERATE; IMMODERATE. 4. Suffixed o-grade form *mod-o- in Latin modus, measure, size, limit, man- ner, harmony, melody: MODAL, MODE, MODEL, MODERN, MODICUM, MODIFY, MODULATE, MODULE, MODULUS, MOLD!, (MOOD?), (MOULAGE); (ACCOMMODATE), (COM- MODE), COMMODIOUS, (COMMODITY). 5. Suffixed o-grade form *mod-yo- in Latin modius, a measure of grain: MODIOLUS, MUTCHKIN. 6. Possibly lengthened o-grade form *méd- in Germanic *mét-, ability, leisure, in: a. Old English métan, to have occasion, to be permitted or obliged: MOTE2, MUST}; b. Germanic compound é-mot-ja- (prefix *é-, meaning uncertain, from Indo- hinppoes é, 6; see Pok. é, 6 280) in Old English émetta, rest, leisure: EMPTY. [Pok. 1. med- 705.] medhu-. Honey; also mead. 1. Germanic *medu in Old English meodu, mead: MEAD!. 2. Greek methu, wine (> methuein, to be intoxicated): AMETHYST, METHYLENE. [Pok. médhu 707.] medhyo-. Middle. 1. Germanic *midja- in: a. Old English midd(e), middle: M1D!; AMID; b. West Germanic diminu- tive form *middila- in Old English middel, middle: MIDDLE; Cc. Germanic compound *midja-gardaz, “middle zone” (*gardaz, enclosure, yard; see gher-1), name of the earth conceived as an intermediate zone lying between heaven and hell, in Old Norse Midhgardhr, Midgard: MipGarD. 2. Latin medius, middle, half: MEAN, MEDIAL, MEDIAN, MEDIASTINUM, MEDIATE, MEDIUM, MITTEN, MIZZEN, MOIETY, MULLION; INTERMEDIATE, MEDIEVAL, MEDIOCRE, MEDITERRANEAN, MERIDIAN, MILIEU. 3. Greek mesos, middle: MESO-. See also me-2. [Pok. medhi- 706.] meg-. Great. 1. Germanic suffixed form *mik-ila- in: a. Old English micel, mycel, great: MUCH; b. Old Norse mikill, great: MICKLE. 2. Suffixed form *mag-no- in Latin magnus, great: MAGNATE, MAGNITUDE, MAGNUM; MAG- NANIMOUS, MAGNIFIC, (MAGNIFICENT), (MAGNIFICO), (MAGNIFY), MAGNILOQUENT. 3. Suffixed (comparative) form *mag-yos- in: a. Latin major, greater: MAJOR, MAJOR-DOMO, MAJORITY, MAJUSCULE, MAYOR; b. Latin majestds, greatness, authority: MAESTOSO, MAJESTY; c. Latin magister, master, high official (< “he who is greater”): MAESTRO, MAGISTERIAL, MAGISTRAL, MAGIS- TRATE, MASTER, (MISTER), MISTRAL, (MISTRESS). 4. Suf- fixed (superlative) form *mag-samo- in Latin maximus, greatest: MAXIM, MAXIMUM. 5. Suffixed form *mag-to-, “made great,” in Latin mactus, worshiped, blessed, sacred: MATADOR. 6. Suffixed (feminine) form *mag-ya-, “she who is great,” in Latin Maia, name of a goddess: May. 7. Suffixed form *meg-a-l- in Greek megas (stem megal-), great: MEGA-, MEGALO-; ACROMEGALY, ALMA- GEST, OMEGA. 8. Variant form *megh- in Sanskrit maha-,
734:mahat-, great: MAHARAJAH, MAHARANI, MAHARISHI, MAHATMA, MAHAYANA, MAHOUT. [Pok. meg(h)- 708.] mei-'. To change, go, move; with derivatives referring to the exchange of goods and services within a society as regulated by custom or law. 1. Latin medre, to go, pass: MEATUS; CONGE, IRREMEABLE, PERMEATE. 2. Suffixed o-grade form *moi-t- in: a. Germanic *ga-maid-az (*ga-, intensive prefix; see kom), “changed (for the worse),” abnormal, in Old English gemdd, insane: MAD; b. Latin mitdre, to change: MEW!, MOLT, MUTATE; COMMUTE, PERMUTE, REMUDA, TRANSMUTE; C. Latin miituus, “done in exchange,” borrowed, reciprocal, mutual: MUTUAL. 3. Suffixed extended zero-grade form *mit-to- in Ger- manic “missa-, “in a changed manner,” abnormally, wrongly, in: a. Old English mis-, mis-: Mis-!; b. Old Norse mis(s), mis(s)-, miss, mis-: AMISS, MISTAKE; C. Ger- manic *missjan, to go wrong, in Old English missan, to miss: MISs!, 4, Suffixed o-grade form *moi-n- in com- pound adjective *ko-moin-i-, “held in common” (*ko-, together; see kom), in: a. Germanic *gamainiz in Old English geméne, common, public, general: MEAN?; (DE- MEAN?); b. Latin commiinis, common, public, general: COMMON, COMMUNE, COMMUNICATE, (COMMUNISM). 5. Suffixed o-grade form *moi-nes- in: a. Latin minus, “service performed for the community,” duty, work, “public spectacle paid for by a magistrate,” gift: MUNICI- PAL, MUNIFICENT, REMUNERATE; b. Latin immiinis (in-, negative prefix; see ne), exempt from public service: IMMUNE. 6. Extended form *()meigv- in: a. Greek amei- bein, to change: AMOEBA; b. Latin migrdre, to change one’s place of living: MIGRATE; EMIGRATE. [Pok. 2. mei-, 3. mei- 710, meig¥- 713, 2. meit(h)- 715.] mei-2. Small. 1. Greek meidn, less, lesser: MEIOSIS; MIo- CENE. 2. Latin nimis, too much, very (< *ne-mi-s, “not little’; ne-, negative prefix; see ne). 3. Suffixed zero-grade form *mi-nu- in: a. Latin minuere, to reduce, diminish: MENU, (MINCE), MINUEND, MINUTE2; COMMI- NUTE, DIMINISH; b. Latin minor (influenced by the comparative suffix -or), less, lesser, smaller: MINOR, MINUS, MIS-!; MINUSCULE; GC. further suffixed (superla- tive) form *minu-mo- in Latin minimus, least: MINIMUM; d. Latin minister, an inferior, servant (formed after magister, master; see meg-): MINESTRONE, MINISTER, MINISTRY, MYSTERY?; @. Russian men’she, less: MENSHE- vik. [Pok. 5. mei- 711.] mei-3, To fix; to build fences or fortifications. 1. Suffixed o-grade form *moi-ro- in: a. Germanic *mair-ja- in Old English mére, boundary, border, landmark: MERE®; b. Latin miirus, wall: MURAL, MURAMIC ACID, MURE; IMMURE. 2. Suffixed o-grade form *moi-ni- in Latin miinire, to fortify, protect, strengthen: MUNITION; (AM- MUNITION), PRAEMUNIRE, PREMUNITION. 3. Possibly suffixed lengthened-grade form *méi-t- in Latin méta, boundary stone, limit: METE?. [Pok. 1. mei- 709.] mei-4, To tie. 1. Suffixed zero-grade form *mi-tro-, “con- tract, that which binds,” in: a. Greek mitra, headband, earilier a piece of armor worn around the waist: MITER; b. Old Persian Mithra-, name of a god (< “contract” < “bond”): MiTHRAS; c. Russian mir, commune, joy, peace (possibly borrowed from Iranian): mR. 2. Possibly a suffixed zero-grade form *mi-to- in Greek mitos, a warp thread: MITOSIS; DIMITY, MITOCHONDRION, SAMITE. [Pok. 4. mei- 710.] méGi-. Mild. Contracted from *meoi-. Suffixed zero-grade form *mi-ti- (< *mis-ti-) in Latin mitis, soft: MITIGATE. [Pok. 7. mei- 711.] meigh-. To urinate, 1. Germanic suffixed form *mih-stu-, urine, hence mist, fine rain, in: a. Old English mist, mist: MIST; b. Middle Dutch mieselen, to drizzle, perhaps akin to the source of Middle English misellen, to drizzle: MIZZLE; Cc. Germanic diminutive form *mihst-ila-, mistle- toe (which is propagated through the droppings of the missel thrush), in Old English mistel, mistletoe: (MISSEL THRUSH), MISTLETOE. 2. Suffixed form *migh-tu- in
1830:MAXIM meg- MAXIMUM meg-
1874:MINE? me-1 MINERVA men-! MINESTRONE mei-2 MINGLE mag- MINIKIN men-1 MINIMUM mei-2 MINISTER mei-2 MINISTRY mei-2 MINIVER wer-! MINNESINGER men-!, sengWh- MINNOW men-4 MINOR mei-2 MINT! men-1 MINUEND mei-2 MINUS mei-2 MINUSCULE mei-2 MINUTE? mei-2 MIOCENE mei-2 MIOSIS mul-
```


## [2026-09-05T20:33:54.813Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D9%86%DA%AF/",
 "prompt": "List the dictionary entries for Persian انگ (ang) from Dehkhoda, Mo'in and Amid: all distinct senses (numbered homographs انگ ۱، انگ ۲ if present), and any etymological bracket like [په.] or mention of عسل/انگبین/زنبور."
}
```


### [2026-09-05T20:34:04.244Z] TOOL RESULT

```
# Persian Dictionary Entries for انگ (ang)

## Dehkhoda Dictionary (لغت نامه دهخدا)

**Sense 1:** "ممر آب را گویند که کوزه گران از سفال سازند" – a ceramic water conduit used by potters to connect vessels.

**Sense 2:** A mark or sign placed on commercial goods for accounting purposes, noted as "ظاهراً «آنک» بالمدو کاف تازی است" (apparently from Turkish "ank").

**Sense 3:** Bee (زنبور)

**Sense 4:** Syrup/extract (شیره، عصاره), related to انگبین (honey) where the original form was "انگ گبین"

**Sense 5:** (Colloquial) Direct, accurate; used in phrases like "انگ زد" meaning a direct hit or blow

---

## Mo'in Dictionary (فرهنگ معین)

- A ceramic tube (تنبوشه)
- A mark on commercial goods
- Syrup/extract (= انج, انغ)
- Bee; honeybee (زنبور عسل)

---

## Amid Dictionary (فرهنگ عمید)

- Ceramic tube for water channels
- Bee; honeybee
- Syrup/extract
- A mark/symbol on commercial shipments
- (Metaphorically) accusation/slander
- (Adverb, colloquial) Direct, straightforward
```


## [2026-09-05T20:34:15.134Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== GPL ordinal\"; grep -n -i \"ordinal\" GPL.txt | head -12"
}
```


### [2026-09-05T20:34:15.210Z] TOOL RESULT

```
=== GPL ordinal
554:The Ordinal Numbers 48
561:§ 50. The ordinals are formed from the cardinals by the addition of the suffix ere and to the ordinals so formed (with the exception of یکم‎ " ‘first’) the suffix عین‎ in, or (its contraction) ~— 7 may be optionally superadded ; e.g.
564:the ordinal‏ «یکم ‘one hundred and first In Pipe of‏ صد و یکم
570:§ 51. The ordinal generally follows the substantive (or ز (معذود‎ as Js! پاب‎ ‘chapter first’ ; روژ دوم‎ " the second day’. But the forms ending in -% may also precede the ma‘dud ; 6۰8۰ دوهین روز‎ ‘ the second day’; که‎ (gods غستین‎ ‘the first enemy who ...’
2571:11, Zhe Ordinal Numbers
2572:§ 169, a) The ordinals from seeond to tenth are of the measure ,فاعل‎ the radical letters being the same as in the cardinals; as اول‎ ‘first’, ثانی‎ ‘second’, JU ‘third’, and so on. The feminines are formed by adding the termination i— to the masculine; as asJU ‘third’. But اول‎ ‘first’, being of the measure رافعل‎ and ‘havi the superlative signification, has for its fem. ay ala.
2573:b) The ordinals from eleventh to nineteenth are formed by adding the cardinal number عشر‎ ‘ten’ to the preceding ordinals, حادی‎ taking
```


## [2026-09-05T20:34:15.911Z] TOOL CALL #60: WebSearch

```json
{
 "query": "Wiktionary Persian ordinal suffix -م -om etymology Middle Persian -om Proto-Iranian *-ama"
}
```


### [2026-09-05T20:34:23.165Z] TOOL RESULT

```
Web search results for query: "Wiktionary Persian ordinal suffix -م -om etymology Middle Persian -om Proto-Iranian *-ama"

Links: [{"title":"ـم - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%80%D9%85"},{"title":"می - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%85%DB%8C"},{"title":"موم - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%85%D9%88%D9%85"},{"title":"Category:Middle Persian suffixes - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Middle_Persian_suffixes"},{"title":"Middle Persian literature","url":"https://en.wikipedia.org/wiki/Middle_Persian_literature"},{"title":"Category:Persian suffixes - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Persian_suffixes"},{"title":"Middle Persian","url":"https://en.wikipedia.org/wiki/Middle_Persian"},{"title":"Category:Persian terms by suffix - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Persian_terms_by_suffix"},{"title":"Dialectal Layers in West Iranian: a Hierarchical Dirichlet Process Approach to Linguistic Relationships","url":"https://arxiv.org/pdf/2001.05297"},{"title":"Iran (word)","url":"https://en.wikipedia.org/wiki/Iran_(word)"}]

Based on the search results, I found information about the Persian ordinal suffix -م (-om) on Wiktionary:

The suffix -م (-om) is inherited from Middle Persian (-om). An ordinal number formed by the suffix ـم (-om) behaves syntactically as a regular adjective, unlike the cardinals, and takes the ezâfe.

However, the search results do not contain specific information about the Proto-Iranian etymology *-ama that you mentioned in your query. The Wiktionary entry I found discusses the suffix's use in forming ordinals (like in "twentieth century" - قرن بیستم qarn-e bistom), but does not provide the Proto-Iranian reconstruction you're looking for. To find that specific etymological information, you may need to consult more specialized etymological resources or access the full Wiktionary entry directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:34:26.738Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%80%D9%85",
 "prompt": "Persian suffix ـم (-om): give the etymology section verbatim (Middle Persian form, any Old Iranian / Proto-Indo-Iranian antecedent), the sense (ordinal-forming), and examples like دوم، چهارم، پنجم."
}
```


## [2026-09-05T20:34:27.705Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/maximum",
 "prompt": "Etymology of maximum and (if shown) minimum: Latin maximus/minimus, the superlative suffix, dates of first English use."
}
```


### [2026-09-05T20:34:31.722Z] TOOL RESULT

```
# Persian Suffix ـم (-om)

**Etymology:**
Inherited from Middle Persian -om, with roots tracing back through Proto-Iranian origins.

**Sense:**
Creates ordinal numbers (first, second, third, etc.) and fractions.

**Examples:**
- دوم (dovom) — second
- چهارم (chahārom) — fourth  
- پنجم (panjom) — fifth

The suffix behaves syntactically as a regular adjective and takes the ezāfe particle. For instance, "qarn-e bistom" means "twentieth century," where the ordinal precedes the noun with the ezāfe construction.
```


### [2026-09-05T20:34:33.420Z] TOOL RESULT

```
# Etymology of Maximum

The word **maximum** entered English around 1740, derived from French and Latin sources. According to the Online Etymology Dictionary, it comes from Latin *maximus*, meaning "greatest," which itself is the superlative form of *magnus* ("great, large, big").

The Latin root traces back further to the Proto-Indo-European *mag-samo-*, a superlative construction built on the root *meg-, meaning "great."

**Key timeline:**
- **1740**: First use of *maximum* as a noun, defined as "the greatest amount, quantity, or degree"
- **1834**: Adoption as an adjective meaning "greatest, at the maximum"

Related English words developed later, including *maximize* (1802) and *maximal* (1872), both building on the core *maximum* term with standard English suffixes.
```


## [2026-09-05T20:34:41.655Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB\"; grep -n -i \"angub\\|angpen\\|ngwpyn\\|anguben\" NYB_vol2_glossary.txt NYB_vol1.txt NYB.txt 2>/dev/null | head; echo \"=== SKT apiary\"; grep -n -i \"apiary\\|^Apis\" SKT.txt | head; echo \"=== FSD apiary\"; grep -n -i \"apiary\" FSD_vol1.txt | head -3"
}
```


### [2026-09-05T20:34:41.777Z] TOOL RESULT

```
=== NYB
=== SKT apiary
802:Apiary,  a  place  for  bees.  (L.) aniim,  neut.  of  apiarius,  belor bees.  —  L.  api-,  for  apis,  a  l>ec.
=== FSD apiary
213:APIARY  TERMS.
19300:a"pl-a'rl-an,  1   G'pi-e'n-en;  2   a'pi-S'ri-an.  I.  a.  Of  or pertaining  to  bees  or  an  apiary.  II.  n.  Improperlj', an  apiarist.
19301:a'pI-3-rist,  1   G'pi-s-rist;  2>S/pi-a-rIst,  n.  A   bee-keeper a'pl-a-ry,  1   e'pi-e-n;  2   a'pi-a-ry,  n.  [-ries,  1   -nz;  2   -rig, pi.  1   4   1.  A   place  where  bees  are  kept.  2.  A   collection of  hives,  colonies  of  bees,  and  bee-culture  appliances; as,  an  apiary  of  fifty  colonies.  Some  apiaries  are  named (1)  from  their  construction;  as.  floating  apiary  (on  a   flat-- boat: used  in  ancient  Egypt),  house *a.  (a  number  o!  hives
```


## [2026-09-05T20:34:47.404Z] TOOL CALL #64: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%DA%AF%D8%A8%DB%8C%D9%86\" \\\n \"https://en.wiktionary.org/wiki/apis\" \\\n \"https://en.wiktionary.org/wiki/%E1%BC%90%CE%BC%CF%80%CE%AF%CF%82\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%B9%E0%A4%BF%E0%A4%99%E0%A5%8D%E0%A4%97%E0%A5%81\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hangub%C3%A1ynah\" \\\n \"https://abadis.ir/fatofa/%D8%A7%D9%86%DA%AF/\" \\\n \"https://en.wiktionary.org/wiki/%D9%80%D9%85\" \\\n \"https://www.etymonline.com/word/maximum\" ; do\n timeout 180 python3 tools/fetch_source.py \"$u\" --note \"pdf page 153 (book p.123): roots Embhi (angubin/apis/empis/hingu) and Emos (ordinal suffix) verification\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-05T20:34:55.115Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/966132e6ec2af018.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5f17dd6ba7a2c18b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/98ce4c400800596e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6be6daebf4bb906c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0b95c9a87f4258f3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/58458ae9369c6e3c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/96701da995e474a3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6dfc5733d72c8596.txt
```


## [2026-09-05T20:35:02.419Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW apis\"; grep -n \"apis,\" LEW_1910.txt | head -5; echo \"=== SYN bee\"; grep -n \"BEE$\\|5\\.6[0-9] BEE\\|Bienc\\|apis, prob\" SYN.txt | head -8; grep -n -i \"lat\\. apis\" SYN.txt | head -5"
}
```


## [2026-09-05T20:35:03.304Z] TOOL CALL #66: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && pdftoppm -f 153 -l 153 -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/153 && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/"
}
```


### [2026-09-05T20:35:04.224Z] TOOL RESULT

```
=== LEW apis
13388:nule I 680 nwo I 44 nuogs (dial.) IT 185 nuolikums I 797 nuoma IT 187 pabadusi II 461 pabdlstit II 625 pabalsts I 122, 559, IT 625 paduse I 3 paipala IT 249, 309 pakars I 167 paksis II 270 pakudit Il 706 palas I 59 pamisu IT 138 pampt II 244 papa, papis, papu- lis, -ula IT 250 parlags I 778 pasérs I 204 pastars IT 348 pat II 379 pats IT 350 pauna IT 248, 389 pauns II 248 paupt IT 389 péc IT 273 pedis II 273 pelawas IT 388 pelce IT 243 pelna IT 331 pelt I 59, 847 pelus II 238, 388 pempis, pempt II 244
=== SYN bee
5112:3.82 BEE Grk. pation Goths \3.-..'. Lith. bite, bitis NG pe\ooa ON byfluga Lett. bite Lat. apis Dan. ChSl.  btéela It. ape, pecchia Sw. bi SCr.  pvela Fr. abeille OE béo Boh.  véela Sp. abeja ME ibe Pol. —_pszezola Rum. albind NE bee Russ. péela Ir. bech Du. bez Skt. bhramara-, ali- Nir. beach OHG bia, bini Av. Sieiers W. gwenynen MHG bine Br. gwenanenn NHG biene
5117:3. Lat. apis, dim. apicula, etym.? Hence It. ape, OFr. ef (Fr. dial. e, etc.); fr. dim., It. pecchia, Fr. abeille, Sp. abeja. (Fr. dial. also mouche @ miel lit. ‘honey fly’). Ernout-M. 61. Walde-H. 1.57. REW 523, 525.
```


### [2026-09-05T20:35:06.779Z] TOOL RESULT

```
total 4696
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  5 16:35 .
drwxrwxr-x 10 sfmqrb sfmqrb   4096 Sep  5 16:21 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
-rw-rw-r--  1 sfmqrb sfmqrb  68501 Sep  5 13:28 108.png
-rw-rw-r--  1 sfmqrb sfmqrb  63543 Sep  5 13:35 109.png
-rw-rw-r--  1 sfmqrb sfmqrb  67502 Sep  5 13:39 110.png
-rw-rw-r--  1 sfmqrb sfmqrb  72718 Sep  5 13:38 111.png
-rw-rw-r--  1 sfmqrb sfmqrb  50381 Sep  5 13:39 112.png
-rw-rw-r--  1 sfmqrb sfmqrb  83933 Sep  5 13:54 114.png
-rw-rw-r--  1 sfmqrb sfmqrb  64811 Sep  5 14:02 117.png
-rw-rw-r--  1 sfmqrb sfmqrb  42354 Sep  5 14:08 118.png
-rw-rw-r--  1 sfmqrb sfmqrb  50224 Sep  5 14:12 120.png
-rw-rw-r--  1 sfmqrb sfmqrb  82335 Sep  5 14:19 121.png
-rw-rw-r--  1 sfmqrb sfmqrb  61026 Sep  5 14:26 123.png
-rw-rw-r--  1 sfmqrb sfmqrb  91077 Sep  5 14:38 124.png
-rw-rw-r--  1 sfmqrb sfmqrb  75202 Sep  5 14:31 125.png
-rw-rw-r--  1 sfmqrb sfmqrb  86203 Sep  4 19:03 126.png
-rw-rw-r--  1 sfmqrb sfmqrb  83553 Sep  5 16:14 128.png
-rw-rw-r--  1 sfmqrb sfmqrb  74748 Sep  5 16:15 130.png
-rw-rw-r--  1 sfmqrb sfmqrb  87739 Sep  5 16:21 134.png
-rw-rw-r--  1 sfmqrb sfmqrb  68320 Sep  5 16:17 136.png
-rw-rw-r--  1 sfmqrb sfmqrb  70436 Sep  5 16:19 140.png
-rw-rw-r--  1 sfmqrb sfmqrb  53357 Sep  5 16:18 142.png
-rw-rw-r--  1 sfmqrb sfmqrb  63658 Sep  5 16:18 144.png
-rw-rw-r--  1 sfmqrb sfmqrb  89133 Sep  5 16:21 145.png
-rw-rw-r--  1 sfmqrb sfmqrb  60631 Sep  5 16:21 147.png
-rw-rw-r--  1 sfmqrb sfmqrb  81770 Sep  5 16:21 148.png
-rw-rw-r--  1 sfmqrb sfmqrb  31185 Sep  5 16:32 150.png
-rw-rw-r--  1 sfmqrb sfmqrb  61486 Sep  5 16:35 153.png
-rw-rw-r--  1 sfmqrb sfmqrb 105296 Sep  4 19:03 311.png
-rw-rw-r--  1 sfmqrb sfmqrb  96466 Sep  4 19:03 33.png
-rw-rw-r--  1 sfmqrb sfmqrb  99093 Sep  4 19:03 39.png
-rw-rw-r--  1 sfmqrb sfmqrb  54479 Sep  4 19:03 46.png
-rw-rw-r--  1 sfmqrb sfmqrb  99295 Sep  4 19:03 54.png
-rw-rw-r--  1 sfmqrb sfmqrb  57649 Sep  5 01:38 69.png
-rw-rw-r--  1 sfmqrb sfmqrb  75801 Sep  5 01:35 71.png
-rw-rw-r--  1 sfmqrb sfmqrb  49860 Sep  5 01:47 72.png
-rw-rw-r--  1 sfmqrb sfmqrb  81180 Sep  5 01:53 73.png
-rw-rw-r--  1 sfmqrb sfmqrb  56073 Sep  5 01:50 74.png
-rw-rw-r--  1 sfmqrb sfmqrb  20612 Sep  5 02:01 75_greek_latin_arrow.png
-rw-rw-r--  1 sfmqrb sfmqrb  75134 Sep  5 02:01 75.png
-rw-rw-r--  1 sfmqrb sfmqrb  66505 Sep  5 01:56 76.png
-rw-rw-r--  1 sfmqrb sfmqrb  65211 Sep  5 02:03 77.png
-rw-rw-r--  1 sfmqrb sfmqrb  63822 Sep  5 02:07 78.png
-rw-rw-r--  1 sfmqrb sfmqrb  59439 Sep  5 02:13 79.png
-rw-rw-r--  1 sfmqrb sfmqrb  58953 Sep  5 02:13 80.png
-rw-rw-r--  1 sfmqrb sfmqrb  99904 Sep  5 02:17 81.png
-rw-rw-r--  1 sfmqrb sfmqrb  74477 Sep  5 02:22 82.png
-rw-rw-r--  1 sfmqrb sfmqrb  67094 Sep  5 02:26 83.png
-rw-rw-r--  1 sfmqrb sfmqrb  63329 Sep  5 02:31 85.png
-rw-rw-r--  1 sfmqrb sfmqrb  31530 Sep  5 02:38 86.png
-rw-rw-r--  1 sfmqrb sfmqrb  79874 Sep  5 09:55 87.png
-rw-rw-r--  1 sfmqrb sfmqrb  98452 Sep  5 09:55 88.png
-rw-rw-r--  1 sfmqrb sfmqrb  80984 Sep  5 09:56 89.png
-rw-rw-r--  1 sfmqrb sfmqrb  77182 Sep  5 09:55 90.png
-rw-rw-r--  1 sfmqrb sfmqrb  63799 Sep  5 09:56 91.png
-rw-rw-r--  1 sfmqrb sfmqrb   3476 Sep  5 10:16 92_pahlavi_box.png
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T20:35:12.015Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"HONEY\" SYN.txt | head -5"
}
```


### [2026-09-05T20:35:12.056Z] TOOL RESULT

```
9655:5.84 HONEY
```


## [2026-09-05T20:35:12.504Z] TOOL CALL #68: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-05T20:35:12.568Z] TOOL RESULT

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


## [2026-09-05T20:35:15.051Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9655,9670p' SYN.txt"
}
```


### [2026-09-05T20:35:15.097Z] TOOL RESULT

```
5.84 HONEY
HL wh HEL Goth. milip Lith. medus mel ON hunang Lett. medus miele Dan. honning ChSl. medi miel Sw. honung SCr. med mist OE hunig Boh. med pas ME huni, honi Pol. miéd 4 a honey Russ. med
wu.  _honing Skt.  madhu- ma OG hona(n)g Av. *paéna-
‘ MHG honec, honic NHG honig
Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
384 SELECTED INDO-EUROPEAN SYNONYMS
Honey was the old IE sweet, and so among the Greeks and Romans and in
2. IN *medhu- ‘honey’ and ‘mead? Walde-P. 2.261. Here as ‘honey’, Lith,
Europe generally until the introduction | Lett. medus, OPruss. meddo, Chs] | of sugar (5.85). From it was made the | medi, etc., general Slavic ; Skt. madhy,. oldest IE intoxicating drink, the ‘mead’ | Toch. mit. Elsewhere only as ‘mead! 5 ! (5.91). or for some other intoxicating drink { Most of the words for ‘honey’ belong | (5.91). : to one of two inherited groups. In Gmc. 3. ON hunang, OE hunig, ete., gen. one of these is represented in Gothic, the | eral Gmc. (except Goth.) : Skt, han- if other in words for ‘mead’, otherwise | cana- ‘golden’, kanaka- ‘gold’, Grk | ‘honey’ is expressed by a new word de- | xvnxés ‘pale yellow’ etc. Walde-p. 6 rived from its yellow color. 1.400; Falk-Torp 417. N 1. IE *melit- ‘honey’. Walde-P. 4. Av. *paéna-, implied by paénaéna- L : 2.296. Ernout-M. 602. Grk. pé\:; Lat. | ‘prepared from honey’, NPers. angubin : mel (> Romance words); Ir. mil, W., | ‘bee-honey’, prob. as (bee’s) ‘milk’ or gj Br. mel; Goth. milip (cf. OE mil-déaw | ‘juice’ : Av. payah-, paéman- ‘milk’, Skt, : ‘honey-dew, nectar’, milisc ‘honeyed’); | payas- ‘milk, juice’, Lith. pienas ‘milk’ ; Arm. meir, Alb. mjall. (5.87). Barth. 817. i B 5.85 SUGAR ; Grk. céxxapr, etc. (late) Goth. Lith.  cukrus NG = faxape ONEEE 28,2: Lett. cukurs , Lat.  saccharum (late) Dan.  sukker Cie 7 ) It. zucchero Sw. _socker SCr.  Seéer P Fr. sucre OE tet Boh. — cukr Sp. azticar ME _ sucere, sugure, etc. Pol. cukier Rum. zahdr NE sugar Russ. sachar m Ir. ay Du. —zucker Skt.  carkara- 0 NI. stilicre OHG zucura Av. et CE ie W. stwgr MHG zucker | Br. sukr NHG zucker a rk The home of sugar and its European | the article was then only an exotic ar names is India. The companions of | product used for medical purpose. The Ir : Alexander the Great told of the Indian | cultivation of the sugar cane was intro- BR : cane which produced ‘honey without | duced in Sicily and Spain by the Arabs, fl ? bees’ (wept r&v xadduor, dre mowfor wed. | and it was only after the crusades that 0 .! HedwooGy yx obcdv, Strabo 15.694). The | sugar became the common sweetening th 4 native Indian name appears in Greek | in place of the older honey. The major- 8 4 and Latin transcriptions in the first cen- ity of European forms of the name come or tury A.D. (wédAc 7d Kaddpuvoy 7d Xeyépevoyv | through Arabic via Spanish or Italian. ¥0 oakxapt, Peripl. 14; caxxyapoy eldos dy Schrader, Reallex. 2.705 ff. W Bédtros év "Ivdig xal rH ebdalporr ’ApaBig Skt. carkara- ‘gravel, grit? (AV +) W mennyoros, ebptoxouevoy éxl rOy xadduov, | later ‘sugar’ : Grk. xpdn, xpoxéd7 ‘peb- Y Diosc. 2.104; Saccharon et Arabia fert, | ble’. Walde-P. 1.463. th sed laudatius India, est autem mel in Hence, through a later Prakrit form *; harundibus collectum, Plin. 12.32), but | like Pali sakkhara-, the following: ur
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
food AN aply gaKXAPOY; odKXaPy saccharum, NG faxap,
_ sachar. kar, whence
' Pers. 84 hero, and through Fi _ guce vero, ’ ape a 1 sukere, etc. (> ME
laez
1, Grk. yada, yédaxros, Lat. lac, lactis (> Romance words, also Ir. lacht, W. llacth, Br. laez), without certain root- connection. Walde-P. 1.659. Ernout- M514, Walde-H. 1.741 f. RIEW 4817. Pedersen 1.228. 2, Ir, mlicht, blicht, W. blith; Goth. miluks, OF meolc, etc., general Gmc.; ChsI. mléko (*melko), etc., general Slav- le; Toch, A malke, B malkwer. These ate put together here despite the dispute 48 to their relationship. Certainly some and prob, all : Grk, &uéd 5 Deal - anew, Lat. mulgére, sth ne OE melcan, etc., the general Bilinreond yordl of Qs G miluh ig hen of Goth, miluks, ti the relationshi Sala Sea think ™ ue to i a the vb. is only , € assimilation of an
```


## [2026-09-05T20:36:31.306Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"apsma-\\|ap9ma\\|fratsma-\\|frat9ma\\|upsma-\\|'letzter'\\|Superl\" BRT.txt | head -20"
}
```


### [2026-09-05T20:36:31.356Z] TOOL RESULT

```
2886:Superl.  aus  'a^i'ai-JS-  (S  304  11.  5)  Adj.,  und iwar  Neubildung  lum  NS.  'i/ä  nach  Mustern
2918:^rämiifa.  Adj.,  Superl.  znm  V.  ram;—  0  Vgl GcK.  PahlV.  »7,  DsT.  ZA.  j.  33,
3117:Superl.  aus  ^afryö.maii-masla-  Adj.,  durch  Ha- plol-,  lu  S  J0<^.  —  *maiay-  m,  'Brunst',  lum V.  mad.;  vgl.  ai.  mäda-  m.;  —  "masta-  PPfP. lum  V.  mad.  (sd.).  —  Pü.:  kÜ  an  i  mast ir/ryat  masilh.  —  i)  Bei  DsT.  in  drei  Wörter zerrissen.    S.  auch  Js.  Cama  Mem.  Val.  131.
3554:an  Gerechtigkeit,  von  AHM.:  ahurvm  Durch H.pIoL  «us  -M-"«"'''"'"''-.  Superl.  aus mazdqm  ..yS  aÜahe  'mS  Y.57.4;  I.\;  — |  'apayanta- Aiy,  V¥¥.  iam\. yam-;  yant{a-  ist fravaslm  avqm  yqtn  shurahe  mazdä  ,  ,  |  Komp.-Form  zn  ü.  yämi^aväi,  IF.  /,  70. asäi°mqmca'V.26.2.  2) 'der  tüchtigste,  •  j.  apayav-  'der  es  (einem  Geräusch wirksamste"*;  'maya  fiaiti  vacastaitü  "^loxtmA  der  Stimme)  gleichtun  kann' :  _j'£si  .. der  wirksamsten  Strophe"  Y.5Ä 8;  —  °m>m\nSii..aiivi.surum>aiti  apayät{sA.)ym  apsU ra^wqm  H.'i.y, —  °mahe  rakws  Vr.i?.  j  (NS.)'*  aa/  näil  apöis(NS.)'^  iiat*maoTaya 6;  —  ihm  ..at'^rapaitim  upayali  *°m?m^^  *vala  /ramanmnö  ratufris  ", .  wenn  er  es dahmsm  N.  is,  1  gleichtun  kann  (,  ist  er  r^\    wenn  er  es
3555:Superl.  ans 'a/a™- Adj.  (eigO'CBlfemt',  Ableit    aber  nicht  gleichtun  kann,   dann  ist  er  r., ausa/a;  Ygi/a/^ma- uiidWi,.Gr.S"^jf.Ji  sofem   er   mit  mittelstarker  Stimme  auf- iBed.  'Kummus'  vgl.    ai.  para-   Adj,    —   Pu.:        _j,  „  „,r apattum.    ^i.:   pradASnatamah;    lu  N.  72  die    SagT     N.  2Ö.
4016:Superl.  aus  *a-/raiSvaiil-  Adj.  'der  kein  von der  Stelle  kennt'(?).
4362:Superl.  aas  *'zak-*'i.  —  Pü. ;    afrff.tt",  erl.: kim /r?f.ik;    Sü. :    achadmai.U.uaah.  —    M  an-
5753:Superl.  zu  asSra-.  —  Pü,;  k^  n?  {süfj  x^üs/är, Sä.  erL;  te  sarvadä  afakäiinah.
6309:/.  12. Superl.    aus   aiavani-.   —    Pü.;   aki-milum.  — I)  Als  Superl.  2a  asmiaa-  1 1.
6435:Superl.  aus  *ai-xrä3^ana!i-;  zu  'jcrairanav-  m. (d.  i.  ar.  *kräsjf°)  vgl.  xrSi-iaya-  und  zUild.  ai. vagvanüm  RV.  j.  3.  15.  —  Pü.:  vas  xrat  kar- tärtmn,  Sü.:  bahi^uddhiiartpantah.
7456:Superl.  zu  äsav-  Adj.    —    ai.  aüflia-  Adj.  —
7991:Pö.:  x^äslir  i  x^alälliim  näm  em,  erl.:  hal apSr'ik  ya-.atäa ;  s.  No.  I .  —  •>  Vgl.  hi.xia'^ra-, woia  es  den  Superlativ  vorstellen  soll.
8135:u.  ugralama-  Adj.  —   i)  Der  alte  Superl.  lu u-,ra-  ist  aajiila-,  s.  Yt.  7p.  38.
8550:Superl.  aus  ar.  *M;  s.  iis.  —  ai.  üllama-  Adj. —  Pü.:  apaliim;  s.  No.  I.  — Pü.:  a^än/ralum .  .  Hin  a/alum/7.
9786:ai,  i;Slama-  m.  EN.  —  ar,  *gaulama;  Be<3.? Anscheinend  Superl.  —  ')  Vgl,  daiu  Yt.5.  8l. Dass  es  sich  dabei  um  die  Disputation  m"' einem  BuddhiBlen  handle  (Haiig,  Dst.;  lulel: Dakab  JRAS.  iSgS.  391,  der  naidy  für  ' corroption  of  the  Vedic  name  of  the  son  r Golama,  viz.  Nodhä^  ansieht),  ht  tinerweislich ond  mir  unwahrscheinlich;  s.  noch  Jn.  Zor. 177  nnd  lu  li^ryavanl:
9838:Superl.  aus  V*"""""  Adj-,  Ableit.  aus 'fuona-; B  wie  in  iatapeJäl;  %  364  D;  vgl.  tayS.lima-.
10192:Superl.  lum  V.  ai-».  —  Pü.:  unklar  (dadan  | k  o  a  r  •  ad  k).  —  '}  Da»  »offälliee  langje  ä  ^ iai   vll.    durch    xmiäza-    »eranlasst;    ».    aber  1
10630:Superl.  lu  •jrroSToan/-  0  (aus  ar.  *kratiianl-  aus *ktatuigaiit-  ■>)  nach  Wörtern  wie  madila-, bairijla-  :  moianf-,  AaranI-  i  s.  noch  xnAuvmna: —  Pü. :  srailklum,  erl. :  dänätlum.  —  0  Vgl, asjrraiiaaiama:  Zur  arischen  Reduktion  von ^»  in  *)  {=  Aw.  %w)  s.  ZDMG.  jo.  690. Enlsprechena  auch  in  j.  aitupsAtaaißai.  Falsch BB.  //.  341.    .
10998:Superl.  zu  xsvhvijSav:
11369:(Sp.  23  u.):  *aevayaäl  aisS  bar3Smd.st)r3iti raiu/ris  "a.\u^  schon  durch  eine  einzige  .." N.  103;  P.  24';  —  *Sy?miit  .  .  vaäm  gä- %attqm  asruhm  (sd.)  N,  103.  b)  beim Kompar. :  vTante  (sd)  avat  vlsmtaeia . *matyaslit  YL7_j.73;  *Vytjo; — in  auf-: fälliger  Stellung:  masyB  i^t.)  va  aAmJt^iJ V.^50'"',  c)  beim  Superl.:  »il^ma^it .  .  stärq/ii  (sd.)  ya%a  /lar/  vayhanim  F. 4^\  —  nit>ma(sd.)^ii  *haoma.haiH^  .  . kazavrayiiyäi  asti  dalvanqm  Y.io.ö;  6';
```


## [2026-09-05T20:36:36.876Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"ema.*superlative\\|superlative.*ema\\|-ma\\b.*superl\\|fratema\\|apema\\|upema\" AVG.txt | head -15; echo \"=== AVG suffix ma\"; grep -n \"§ 3[0-9][0-9]\\..*[Ss]uperlative\" AVG.txt | head"
}
```


### [2026-09-05T20:36:37.078Z] TOOL RESULT

```
2204:Note  2.  As  seen  also  above,  comparatives  and  superlatives  may  be more  or  less  mechanically  attached  to  a  positive  of  similar  meaning  and containing  the  same  crude  stem,  see  §  365 :  e.  g.  to  taty-ma-  'strong',  the comparative  tqjyah-,  superl.  tandSta-  beside  tafymohma-,  et  al.
4732:14.  bx.-tara,  -tema  =  Skt.  -tara,  -tama  (Whitney,  §  1242). §  841.    These  suffixes  are  used  respectively  in  form- ing the  comparative   and  superlative  degree  of  adjectives, the   latter  also   in  the  ordinals  visqshma-,  satotoma;  ha-
4752:22.  Av.  -ma  =  Skt.  -ma  (Whitney,  §  1224!)). §  849.    With  -ma  as  secondary  suffix  are  made  a  few superlatives  from  prepositions,  a  few  ordinal  numerals,  a small  number  of  adjectives  from  nouns,    and   one   or  two derivative  substantives  likewise.     Examples  are:
=== AVG suffix ma
```


## [2026-09-05T20:36:39.495Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4750,4770p' AVG.txt; echo \"=== 4728-4745\"; sed -n '4728,4750p' AVG.txt"
}
```


### [2026-09-05T20:36:39.553Z] TOOL RESULT

```
Suffix  -lot,  -li,  -pa,  -Pya,  -pwa,  -pwana,  -na,  -ma,  -man,  -man.t,  -ya.      233
Noun.  Av.  ahuna-  m.  'the  Ahuna  formula'.— Adjective.  Av. fyayana-  'belonging  to  a  well'  Yt.  6.2 ;  Av.  zrayana-  'of  the  sea' ; Av.  vahmana-  'praiseworthy' ;  Av.  airyana-  'Aryan'.
22.  Av.  -ma  =  Skt.  -ma  (Whitney,  §  1224!)). §  849.    With  -ma  as  secondary  suffix  are  made  a  few superlatives  from  prepositions,  a  few  ordinal  numerals,  a small  number  of  adjectives  from  nouns,    and   one   or  two derivative  substantives  likewise.     Examples  are:
Noun.  Av.  spitama-,  spitama-  m.  'Spitama'.  —  Adjective.  Av. aptma-  'last'  =  Skt.  apamd- ;  Av.  upama-  'highest'  =  Skt.  upama-; —  Av.  fratima-  'first'  =  Skt.  pratkama-  (Whitney,  §  487  h) ;  Av. ii&uma-  'ninth'  (§§  64,  374)  =  Skt.  navamd-; — Av.  daliyuma-  'be- longing to  the  country'  (Jafyu-);  Av.  zaqtuma-  'belonging  to  the tribe'.
23.  Av.  -man  (-mana,  -mna)  =  Skt.  -man  (-mna),  Whitney,  §§  i  i68i,  12240. §  850.     A  very  few  words  show  the  suffix  -man,    or   its   variations -mana,  -mna.     The  examples  are :
Noun.  Av.  a'ryaman-  m.  'connection,  family,  Airyaman',  cf. Skt.  aryamdn-.  —  Adjective.  Av.  yatumana-  'relating  to  a  sor- cerer' ;  Av.  zaranimna-  'angered'  Yt.  10.47.
24.  Av.  -matit  =  Skt.  -mant  (Whitney,  §   1235). §  851.    The  secondary  suffix  -matit,  like  -vant  below, is  used  in  making  a  number  of  possessive  adjectives  from noun-stems.    The  noun-stems  with  which  it  is  used,  as  in Skt.,  are  chiefly  «-stems.     Examples  are:
Av.  Jiratumatit-  'having  wisdom'  =  Skt.  krdlumant- ; Av.  gaomatit-  'having  milk,  flesh'  =  Skt.  gomant-; Av.  madumatit-  'rich  in  sweets'  =  Skt.  mddhumant- ; — Av.  ar'pamatit-  'right,  true  to  fact'  (from  tf-stem) ; — Av.  afra$lmaiit-  'not  progressing'  (fr.  z'-stem).
25.  Av.  -ya  (-ay 'a)  =  Skt.  -ya  (-iya,  -iya),  Whitney,  §§  1210,
1214,   1215.
§  852.     The  suffix  -ya   corresponds   to  Skt.  -ya,  -iya (§  68,  i),  and  forms  a  large  number  of  secondary  deriva-
234  Word-Formation:  Secondary  Suffixes.
tives.  These  are  chiefly  adjectives;  less  often  they  are nouns.  The  vrddhi-strengthening  which  is  often  found  in Skt.  (Whitney,  §  1211)  is  almost  wanting  in  Avesta.  The feminine  form  is  -yd.
Before  this  suffix,  the  stems  in  -a,  -a,  drop  their  final vowel ;  the  stems  ending  in  -u  retain  the  u  unchanged,  un- less it  unites  with  a  preceding  t  into  PW,  §  94.
A  few  forms  in  -aya  occur,  either  by  retention  of stem-rt,  or  by  extension  (§  68  Note  3),  compare  Skt.  -iya, Whitney,  §  1214.  Examples  of  -ya  are:
Noun.  Av.  afyrya-  m.  'pupil' ;  Av.  n&vhaipya-  n.  nomen  propr. , cf.  Skt.  nasatya-;  Av.  v&strya-  adj.  'farming',  m.  'farmer'; — Av. avhuya-  f.  'lordship'.  —  Adjective.  From  a-stem:  Av.  aha'rya- 'lordly'  (observe  vrddhi  fr.  akura-)  Yt.  13.82,  14.39;  Av.  ajrya- 'topmost'  =  Skt.  dgrya-,  agriyd-;  Av.  haomya-  'relating  to  haoma" =^  Skt.  somyd- ;  Av.  fyaflrya-  'kingly'  =  Skt.  kfatriya- ;  Av.  yesnya- 'revered'  =  Skt.  yajfiiya-.  —  From  <f-stem :  Av.  halnya-  'belonging to  an  army'  =  Skt.  sinya- ;  Av.  galpya-  'material,  earthly'.  —  From a-stem:  Av.  rapwya-  'reasonable',  cf.  Skt.  ftviya-;  Av.  po*ruya- 'first'  =  Skt.  purvyd-;  so  Av.  gaoya-,  gSvya-  'belonging  to  the  cow* =  Skt.  gdvya-. —  From  consonant  stem:  Av.  visya-  'of  the  clan'  = Skt.  viiya-.
Note.  Observe  the  few  forms  that  show  -aya  as  remarked  upon just  above  §  852  c.  Examples  are:  Noun.  Av.  zar*daya-  n.  'heart'  =  Skt. hfdaya- ;  Av.  zar'maya-  adj.  'green',  n.  'verdure',  cf.  Skt.  harmyd-.  —  Ad- jective. Av.  aspaya-  (ace.  aspalm]  'belonging  to  a  horse'  =  Skt.  dtvya-; Av.  nSvaya-  'flowing,  navigable'  =  Skt.  n&vya.-,  cf.  §  68  Note  3.
26.  Av.  -ra  —  Skt.  -ra  (Whitney,  §§  1226,  474). §  853.     This  suffix  occurs  in  a  very  few  words ,   chiefly  pronominal derivatives.     Examples  are:
Av.  adara-  adj.  'under,  lower*  =  Skt.  ddhara-;  Av.  afara-  adj. 'later,  behind'  =  Skt.  dpara-;  Av.  upara-  adj.  'further,  above'  = Skt.  upara-.  Probably  Av.  hazavra-  adj.  and  n.  'thousand'  =  Skt. saAdsra-.  Observe  Av.  ahura-  m.  'lord,  Ahura'  =  Skt.  dsura-,
27.  Av.  -va,  (-vya)  •=.  Skt.  -va,  (-vya),  Whitney,  §   1228. §  854.     The  ending  -va  as  secondary   suffix   occurs   in   a   very   few adjectives.    These  must  be  distinguished  from  orig.  ^-adjectives  transferred to  the  a-inflection.     Examples  of  -va  as  secondary  suffix  are :
Second.  Deriv. :  —Suffix  -ra,  -va,  -vya,  -van,  -va'rf,  -vana,  -vatit.      235
=== 4728-4745
Noun.  Av.  araska-  m.  'disorder';  Av.  pasuka-  m.  'cattle,  beast'; Av.  draffaka-  m.  'banner'  (in  drafjakavatit-} ;  Av.  dahaka-  m.  nomen propr.;  Av.  majy&ka-  m.  'man'; — Av  marldika-  n.  'mercy'  (cf. Whitney,  §  Ii86c)  =  Skt.  mrdikd-;  Av.  ainika-  m.  n.  'face'  =  Skt. dnika-;  —  Av.  tiS'rikS-  f.  'woman';  Av.  pa*rik8-  f.  'fairy,  Peri'. — Adjective.  Av.  karvika-  'trifling' ;  Av.  kutaka-  'small'.  Pronominal adj.  Av.  ahmttka-  'ours'  =  Skt.  asmdka-;  Av.  fyjmaka-  'your'  =  Skt. yufmika-,  cf.  Whitney,  §  12220.
13.  Av.  -ta  =  Skt  -ta  (Whitney,  §  12450).
§  840.  This  ending  as  secondary  suffix  occurs  in  a  few  words,  ad- jectival and  substantival.  Examples  are:
Noun.  Av.  prita-  m.  'Thrita',  cf.  Skt  tritd- ;  Av.  bajyqstS-  f. 'Bushyansta'.  —  Adjective.  Av.  afavasta-  adj.  'righteous',  m.  'righ- teousness* ;  Av.  pattr'ta-  'winged'.
14.  bx.-tara,  -tema  =  Skt.  -tara,  -tama  (Whitney,  §  1242). §  841.    These  suffixes  are  used  respectively  in  form- ing the  comparative   and  superlative  degree  of  adjectives, the   latter  also   in  the  ordinals  visqshma-,  satotoma;  ha-
232  Word-Formation:  Secondary  Suffixes.
zavrotema-.    The  treatment  of  the  stem-final  before  these endings  has  already  been  given.   Examples,  see  §§  364,  374.
15.  Av.  -tat  =  Skt.  -tat  (Whitney,  §§  1238,  383k). §  842.    This  suffix  makes  feminine  abstracts.     Its  in- dependent origin  is  shown,  for  example,  in  Av.yavaeca.tdlte beside yavaetd'taeca  Ys.  62.6,  Yt.  13.50,  cf.  §  893.  Examples:
Av.  uparatSt-  f.  'supremacy'  =  Skt.  upardt&t-;  Av.  ha*rvatdt-  f. 'completeness,  Salvation'  =  Skt.  sarvdtat-.     Likewise  others.
16.  Av.  -ti  =  Skt.  -ti  (Whitney,  §  H57h).
§  843.  The  suffix  -ti  appears  as  secondary  ending  in  a  few  words; the  most  important  of  these  are  the  numerals.  Examples  are:
,  ,Av.  paitwar'ti-  f.  'bow*  (cf.  fanvar-);  Av.  $/va?ti-  'sixty'  =  Skt. fafti-;  Av.  hapta*ti-  'seventy'  =  Skt.  saptatt-;  Av.  nava'ti-  'ninety' 1=  Skt.  navati-,  see  §  366  above.
17.  Av.  -pa  (-da)  =  Skt.  -tha  (Whitney,  §   1242  d). §  844.     The  secondary  suffix  -pa   is   to   be   sought   in   one   or   two numeral  and  pronominal  words.     As  examples :    Av.  haptapa-  'seventh'  = Skt.  saptdtha-;  Kv.pufyfa-  'fifth',  cf.  Skt.  pafic-a-tha-  ; — Av.  avafia-  'thus,  so'.
1 8.  Av.  -pya  =  Skt.  -tya  (Whitney,  §   1245  b).
§  845.  This  suffix  in  Av.,  as  in  Skt.,  makes  one  or  two  derivative adjectives  from  prepositions  and  adverbs.  As  instances:  Av.  a'wi^ya- 'away,  distant' ;  Av.  pascqtyya-  'behind'.
19.  Av.  -pwa  —  Skt.  -tva  (Whitney,  §  1239).
§  846.  With  this  suffix ,  as  in  Skt.,  a  few  neuter  nouns  denoting 'condition',  'state'  are  formed  from  adjectives  and  nouns.  Examples :
Av.  avhupwa-  n.  'lordship' ;  Av.  ratufwa-  n.  'mastership' ;    Av. vavhupwa-  n.  'good  deed'  =  Skt.  vasutvd-.
20.  Av.  -Jrwatia  =  Skt.  -tvana  (Whitney,  §  1240).
§  847.  This  suffix  is  hardly  more  than  an  extension  of  the  pre- ceding, which  it  resembles  in  meaning.  A  quotable  example  is  the  abstract noun,  Av.  n&'ripwana-  n.  'marriage',  cf.  Skt.  patilvand-,  Whitney,  §  1240.
21.  Av.  -na  =  Skt.  -na  (Whitney,  §  1223  g).
§  848.  With  this  suffix  a  very  few  secondary  derivatives  are  formed. Examples  are :
Suffix  -lot,  -li,  -pa,  -Pya,  -pwa,  -pwana,  -na,  -ma,  -man,  -man.t,  -ya.      233
```


## [2026-09-05T20:36:47.597Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"postumus\\|posturaus\\|infimus\\|infumus\" LAT.txt | head -8"
}
```


### [2026-09-05T20:36:47.648Z] TOOL RESULT

```
28709:missior, infimus humillimus, quod in mundo infima humus. Souvent mis
29602:est a superus', infimus aurait ete refait ensuite, sur le modble dein-
30105:Infimus (anc. infumus), -a,-um: qui se trouve tout au bas. Forme refaite
30116:Lat. inferus, infimus repond evidemment a skr. ddharah (av. aSaro),
49378:3 ° postumus: qui v^ent le tout dernier, cf.Pl.Au.i63sq., dans la
49384:mSne que dans infimus, primus, deCumus, et 1 'adjectif a dfi d'abord
49386:Quintus, Sextus, Decumus, Decimus , et finalesent Postumus. De postumus
49411:lett .pastars "dernier". A postumus, cf. osq. pustm[as] "postresae",
```


## [2026-09-05T20:37:26.251Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '49376,49392p' LAT.txt; echo \"===\"; sed -n '30103,30120p' LAT.txt"
}
```


### [2026-09-05T20:37:26.315Z] TOOL RESULT

```
peu claire a ct 46 postremissimus, employd par C. Gracchus, dans
Aulu-Gelle 15,13,3, cf. extremissimus, etc.; M.L.6694.
3 ° postumus: qui v^ent le tout dernier, cf.Pl.Au.i63sq., dans la
1 . du droit, a dSsignd 1 'enfant apros la sort du pbre (cf. Caesellius
Vindex ap. Geli. 3, 16,5, et Varr., L.L.9, 60), celui -11 seul, d'aprbs
la loi rosaine sur la paternitS, pouvant Stre qualifid de "tout
dernier" (v. M.LeumAnn, Gnomon, 9,340); d'ou la graphie posthumus
due k un rapprocbement fait avec humus, humare. Le suffixe est 1 e
mSne que dans infimus, primus, deCumus, et 1 'adjectif a dfi d'abord
servir de prSnos, dans la sSrie des prSnoms num£ranx qu'il terminait:
Quintus, Sextus, Decumus, Decimus , et finalesent Postumus. De postumus
dd rivent Postumius-, postumo, -ds: et re posteri eur (oppos£ a anticipa),
postumatus (oppos£ a principatus), tous deux dans Tertullien.
3 ° posticus: qui se trouve en arribre (sens local); Feat.344,34
et quae ante nos sunt antica et quae post nos sunt postica dicuntur;
et dexteram anticam, sinistram posticam dicimus. Sic etiam ea caeli
pars, quae sole inlustratur ad meridiem, antica nominatur, quae ad
===
qui est plus bas; s'emploie de l'espace, et du temps (de la le sens
de "plus jeune, descendant"), du rang: Inferiores "les inf^rieurs";
Infimus (anc. infumus), -a,-um: qui se trouve tout au bas. Forme refaite
pour remplacer Imus qui avait perdu sa transparence etymologique.
Derives: infimat is (crAation de Plaute, St.493, qui 1 'oppose a sum¬
mates)', Infimitas (Amm.); Infimo (Apul.).A basse epoque, la forjne
ayant cesse d'etre comprise comme un superlatif, on rencontre le
comparatif infimior (iren.).
Inferus a un doublet infernus (cf. supernus, internus, etc.); d'ou
Inferna,-orum "les demeures des dieux Inferi "; Infernas,-atis (Vitr.).
La l.de 1 'figlise a employ 4 infernus m. dans le sens de "enfer" cf.
infernum, panroman, sauf roumain, M.L.4397, celt.: iri. iffern, britt.
uffern', germ.: ags. fern, et en a tire un adj. infernalis.
Lat. inferus, infimus repond evidemment a skr. ddharah (av. aSaro),
adhamdh "qui est au-dessous", a cote de adhdh "en bas"; le gotique
a undar "sons", et 1 'armenien dnd "sons" (entre autres sens). Mais
/ n 1 est pas conforne a la phonetique du latin de Rome; la forme du
mot est donc dialectale, ce qui s'expliquait par les emplois religieux
```


## [2026-09-05T20:37:43.626Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC empi\"; grep -n \"empi\\|embhi\" IEC.txt | head -5; echo \"=== AHD empi/bhei\"; grep -n -i \"bhei-\\|BEE \" AHD_watkins1985.txt | head -5"
}
```


### [2026-09-05T20:37:43.681Z] TOOL RESULT

```
=== IEC empi
51:My thanks are due to all previous lexicographers (“harmless drudges”) and etymologists who have unknowingly contributed to the material of this Dictionary, and who have served as a necessary corrective to a work whose only aim is to present a common denominator rather than a lost primitive speech. As an independent study, Indo-European linguistics can claim to be an exact, albeit empirical science, since it fulfils the three requisites of science, viz. collection, classification and interpretation. For such a science, absolute and final proof is probably unattainable, but if a relationship can, in terms of Euclid, be “de- monstrated" by an adequate amount of analogy, the result can be both probable and con- vincing. Historical linguistics is unique in being probably the only exact science that is linked exclusively to human behaviour. It stands or falls by the logic inherent within it, and does not depend op the dicta of any one scholar, dead or alive. In bringing this work to a close after 55 years of intense and unremitting labour, the author has tried to avoid the German fault of overloading etymologies with irrelevancies, the French fault of trim- ming the evidence to achieve a neat pattern, and the Anglo-Saxon fault of being content with approximations.
633:apotes, aptos (strong; strength’. Cf. apnu-, apolos, op-. WP I, 46 Alb. i aftë (Cable, if not a Lat. LW); Lat. aptus “tied, joined, fitted, close, proper; OE eafop 'strength' . apis (?) ‘insect’. Cf. empis Lat. cf. apis, gp. apium ‘bee’; OCz. op-oka, -uka, ap-oka ‘honeycomb’ beside Cz. jepice ‘mayfiy’.
2914:dhis- (1) ‘god, godlike’. Cf. dhiio Skt. dhisnyah ‘devout’; dhisnyam /side-altar'; dhisà 'piously'; Osc. fíísna- ‘tempie’; Umb. fiso, acc sg. fisoni (a god); fise, ds. (to a god); ON dis pl. dísir ‘goddess’; Icel. dísa, id. beside vatnadís *naiad'; OCS cf. diosovü, adj. *of a heathen god?
3562:empis, io “insect; swarm’. WP I, 125 Gk. empís; OHG imbi ‘swarm of bees; MHG imbe, OE imbe, id.; LG imm, wf. ‘bee’; Cz. cf. jepice (^mayfly', fr. *empitio); Pol. cf. jetka, id. (fr. a type *emptika); ? cf. Finn. (LW?) ampia- (^wasp- in cpds.)
3570:empis, io — en-dhe-
=== AHD empi/bhei
148:The names for a number of insects can be reconstructed in the protolanguage, includ- ing the wasP (wopsa), the hornet (*kras-ro-, a derivative of ker-', “head,” from the shape of the insect), and the fly (mu-2). The BEE (bhei-') was particularly important as the producer of honey, for which we have the common Indo-European name melit-. Honey was the only source of sugar and sweetness (swad-, “sweet,” is ancient), and notably was the base of the only certain Indo-European alcoholic beverage, MEAD, medhu-, meaning in different dialects both “mead” (“wine” in Greece) and “honey.” The Germanic lan- guages have innovated, perhaps from a taboo on speaking the name while gathering wild honey; the common Germanic English word HONEY is from an old color adjective for “yellow,” k(e)neko-.
325:English bere, bere, berlic, barley: BARLEY; BARN. 2. Latin far (stem farr-), spelt, grain: FARINA, (FARINA- CEOUS), FARRAGINOUS, FARRAGO. [Pok. bhares- 111.] bhasko-. Band, bundle. 1. Latin fascis, bundle (as of rods, twigs, or straw), also crowd of people: FASCES, FASCICLE, FASCINE, FASCISM. 2. Latin fascia, band, fillet, bandage: FASCIA, FESS. 3. Probably Latin fascinum, fascinus, an amulet in the shape of a phallus, hence a bewitching: FASCINATE. [Pok. bhasko- 111.] bhau-. To strike. 1. Germanic *bautan in: a. Old English béatan, to beat: BEAT; b. German bosseln, to do odd jobs: BUSHEL?. 2. Germanic *bautilaz, hammer, in Old English bietel, hammer, mallet: BEETLE’. 3. Germanic “bitaz in Old English diminutive buttuc, end, strip of land: BUTTOCK. 4. Germanic *butt-, name for a flatfish, in Middle Dutch butte, flatfish: HALIBUT. 5. Germanic *buttan in Old French bo(u)ter, to strike, push (> French bouton, button): BOUTON, BUTT!, BUTTON, BUTTRESS; ABUT, REBUT, SACKBUT. 6. Variant form *bhit- in: a. Latin confiitdre, to check, suppress, restrain (com-, intensive prefix; see kom): CONFUTE; b. Latin refiitdre, to drive back, rebut (re-, back; see re-): REFUTE. [Pok. 1. bhau- 112.] bhé-. To warm. Contracted from *bheo. 1. Suffixed zero-grade form *bha-to- in Germanic *batham in Old English beth, a bath, and its denominative bathian, to bathe: BATH!, BATHE. 2. Suffixed zero-grade form *bha-g- in: a. Germanic *bakan in Old English bacan, to bake: BAKE; b. Germanic *bakkan in German backen, to bake: ZWIEBACK. [Pok. bhé- 113.] bhedh-. To dig. 1. Germanic *badjam, garden plot, also sleeping place, in Old English bed(d), bed: BED. 2. O-grade form *bhodh- in: a. Latin fodere, to dig: FOSSA, (FOSSE), FOSSIL, FOSSORIAL; b. perhaps Greek bothros, pit: BOTHRIUM. [Pok. 1. bhedh- 113.] bheg-. To break. Akin to bhreg-. Possibly in various Germanic forms. 1. Germanic nasalized form *bang- in: a. Old Norse banga, a hammering, akin to the probable Scandinavian source of English BANG!; b. Swedish dia- lectal bangla, to work inefficiently, akin to the possible Scandinavian source of English BUNGLE. 2. Possibly Germanic nasalized forms *bankiz and *bank6én-, bank of earth (possibly < “feature where the contour of the ground is broken,” escarpment, riverbank, possibly also associated with “manmade earthwork’’), later also bench, table, in: a. Old English benc, bench: BENCH; b. Old Danish banke, sandbank, akin to the Scandinavian source of BANK}; c. Old High German banc, bank, bench, moneychanger’s table (> Italian banca): BANK?, BANT- LING, BUNCO; BANKRUPT; d. Old French banc, bench: BANK, BANQUET; @. Provencal banca, bench: BAN- QUETTE. [Pok. bheg- 115.] bhegr-. To run away. 1. Germanic *bakjaz, a stream, in Old Norse bekkr, a stream: BECK?. 2. Greek phebesthai, to flee in terror, forming phobos, panic, flight, fear: -PHOBE, -PHOBIA. [Pok. bhegy- 116.] bhei-'. A bee. Germanic suffixed form *bidn- in Old English 6é0, a bee: BEE}. [Pok. bhei- 116.] bhei-2. To strike. 1. Germanic suffixed form *bili- in Old English bile, bird’s beak: BILL?. 2. Germanic suffixed form *bilja- in Old English bil), sharp weapon: BILL’. [Pok. bhei(a)- 117.] bheid-. To split; with Germanic derivatives referring to biting (hence also to eating and to hunting) and wood- working. 1. Germanic *bitan in Old English *bitan, to bite: BEETLE!, BITE. 2. Zero-grade form *bhid- in: a. Ger- manic *bitiz in Old English bite, a bite, sting: B1T?; b. Germanic *bitén- in Old English bita, a piece bitten off, morsel: BIT!; c. Suffixed form *bhid-ro- in Old English bit(tjer, ‘‘biting,’’ sharp, bitter: BITTER. 3. O-grade form *bhoid- in Germanic *baitjan in: a. Old Norse beita (verb), to hunt with dogs, and beita (noun), pasture, food: BAIT!; b. Old French beter, to harass with dogs: ABET. 4. Germanic *bait-, a boat (< “dugout
1281:BEE! bhei-1
1299:BILBERRY bhel-2 BILINGUAL dnghi BILIRUBIN reudh-1 BILIVERDIN virére BILL! beu-1 BILL? bhei-2 BILLS = bhei-2 BILLET! beu-1 BILLET-DOUX = dik-u- BILLOW bhelgh- BILTONG bhel-2, dnghi BIMESTRIAL mé-2 BIN bhendh- BINAL dwo- BINARY dwo- BIND bhendh- BINNACLE ghabh- BINOMIAL nem- BIO- gW¥ei-
```


## [2026-09-05T20:37:52.130Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\nfor t in (633,3562):\n    pre='\\n'.join(lines[:t-1]); li=pre.count('\\f')\n    print('line',t,'leaf',li)\nEOF"
}
```


### [2026-09-05T20:37:53.836Z] TOOL RESULT

```
line 633 leaf 31
line 3562 leaf 145
```


## [2026-09-05T20:39:47.932Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SIN hingu\"; grep -n -i \"hingu\" SIN.txt | head -6; echo \"=== KNT fratama\"; grep -n \"fratama\\|-ama-\" KNT.txt | head -6; echo \"=== KLN maximum\"; grep -n -i \"^maximum\\|maximum, n\\|minimum, n\" KLN_1966.txt | head -4"
}
```


### [2026-09-05T20:39:48.042Z] TOOL RESULT

```
=== SIN hingu
1745:s  Hing  is  mentioned  by  Fryer  (Vol.  I,  p.  286)  as  in  use  among  the  natives  of southern  India,  "to  correct  all  distempers  of  the  brain,  as  well  as  stomach,"  "a  sort of  liquid  Assa  Fcetida,  whereby  they  smell  odiously."  This  is  the  product  of  Ferula alliacea,  collected  near  Yezd  in  Khorasan  and  in  the  province  of  Kerman,  and chiefly  used  by  the  natives  of  Bombay  (FlCckiger  and  Hanbury,  Pharmacographia, pp.  319-320;  Watt,  Commercial  Products  of  India,  p.  534).  Fryer's  distinction  be- tween hing  and  asafcetida  shows  well  that  there  were  different  kinds  and  grades  of the  article,  derived  from  different  plants.  Thus  there  is  no  reason  to  wonder  that the  Chinese  Buddhist  authors  discriminate  between  hingu  and  a-wei  (Chavannes and  Pelliot,  Traits  manicheen,  p.  234);  the  £'ou  ts'ai  ("stinking  vegetable")  is probably  also  a  variety  of  this  product.
1749:The  Chinese  understand  by  the  term  a-wei  products  of  two  different plants.  Neither  Bretschneider  nor  Stuart  has  noted  this.  Li  Si-cen1 states  that  "there  are  two  kinds  of  a-wei, —  one  an  herb,  the  other  a tree.  The  former  is  produced  in  Turkistan  (Si  yu),  and  can  be  sun- dried  or  boiled:  this  is  the  kind  discussed  by  Su  Kun.  The  latter  is produced  among  the  Southern  Barbarians  (Nan  Fan),  and  it  is  the sap  of  the  tree  which  is  taken:  this  is  the  kind  described  by  Li  Sun, Su  Sun,  and  C'en  C'en."  Su  Kun  of  the  T'ang  period  reports  that 11  a-wei  grows  among  the  Western  Barbarians  (Si  Fan)  and  in  K'un- lun.2  Sprouts,  leaves,  root,  and  stems  strongly  resemble  the  pai  li  Q I3i  (Angelica  anomala).  The  root  is  pounded,  and  the  sap  extracted from  it  is  dried  in  the  sun  and  pressed  into  cakes.  This  is  the  first quality.  Cut-up  pieces  of  the  root,  properly  dried,  take  the  second rank.  Its  prominent  characteristic  is  a  rank  odor,  but  it  can  also  stop foul  smells;  indeed,  it  is  a  strange  product.  The  Brahmans  say  that hUn-kii  (Sanskrit  hingu,  see  below)  is  the  same  as  a-wei,  and  that  the coagulated  juice  of  the  root  is  like  glue;  also  that  the  root  is  sliced, dried  in  the  sun,  and  malodorous.  In  the  western  countries  (India) its  consumption  is  forbidden.3  Habitual  enjoyment  of  it  is  said  to  do away  with  foul  breath.  The  barbarians  (3%  A)  prize  it  as  the  Chinese do  pepper."  This,  indeed,  relates  to  the  plant  or  plants  yielding  asa, and  Li  Si-cen  comments  that  its  habitat  is  in  Hwo  oou  (Qara-Khoja) and  Sa-lu-hai-ya  (Shahrokia).4  Curiously  enough,  such  a  typical  Iran- ian plant  is  passed  over  with  silence  in  the  ancient  historical  texts relative  to  Sasanian  Persia.  The  only  mention  of  it  in  the  pre-T'ang Annals  occurs  in  the  Sui  iw5  with  reference  to  the  country  Ts'ao  iff north  of  the  Ts'un-lin  (identical  with  the  Ki-pin  of  the  Han),  while the  Txai  p'in  hwan  yil  ki6  ascribes  a-wei  to  Ki-pin.
1758:"A-wei  is  produced  in  Gazna  #P  18  ffl>  (*Gia-ja-na);1  that  is,  in  north- ern India.  In  Gazna  its  name  is  hin-yii  (Sanskrit  hingu).  Its  habitat is  also  in  Persia,  where  it  is  termed  a-yii-tsie  (see  below).  The  tree grows  to  a  height  of  eight  and  nine  feet.2  The  bark  is  green  and  yellow. In  the  third  month  the  tree  forms  leaves  which  resemble  a  rodent's ear.  It  does  not  flower,  nor  does  it  produce  fruit.  The  branches,  when cut,  have  a  continuous  flow  of  sap  like  syrup,  which  consolidates,  and is  styled  a-wei.  The  monk  from  the  country  Fu-lin,  Wan  ^  by  name, and  the  monk  from  Magadha,  T'i-p'o  $i  §1  (*De-bwa,  Sanskrit  Deva), agree  in  stating  that  the  combination3  of  the  sap  with  rice  or  beans,  and powdered,  forms  what  is  called  a-wei. "4
1780:(2)  Sanskrit  HIS  hin-kil,  *hin-gu;  %  HI  hin-yit,  *hin-nu;  H  HI hiin-k'ii,  *hun-gu;  corresponding  to  Sanskrit  hingu.  In  my  opinion, the  Sanskrit  word  is  an  ancient  loan  from  Iranian.6  Garcia  gives  imgo or  imgara  as  Indian  name,  and  forms  with  initial  i  appear  in  Indian vernaculars:  cf.  Telugu  inguva;  cf.,  further,  Japanese  ingu,  Malayan angu  (according  to  J.  Bontitjs,  who  wrote  in  1658,  the  Javanese  and Malayans  have  also  the  word  hin).
5981:haridra  309,  314 harltakl  378,  58X halahala  582 hingu  358,  359,  361 *hunda  304
=== KNT fratama
1914:b. Genitive: Arta-xéaga- ‘Having a kingdom of justice’; Aršāma- (from *aría-ama-) ‘Having the might of a hero’; Haxd-manis- ‘Having the mind of a friend’; Garma-pada- ‘(Month) having the place of heat’; Asa-garta- (Тапа) having caves of stone’. :
2252:III. Secondary comparison, that is, comparison by suffixes attached to the stem of the adjective as seen in the positive degree, was made in Aryan by the use of -tara- and -tama-, cf. Gk. -répos -raros, Lt. ex-terus and ex-timus. The comparative is seen in OP fratara- and ady. apataram, the superlative in fratama-. Nt. comp. frafaram has an alternative suffix with aspirated stop, seen in the Skt. superlative prathamd-. A simpler form of the
2824:! Bv. TPS 1945.610 suggests that the engraver acci- dentally omitted martiyé before tyaišaiy, and then in- serted it after fratama when he noticed the omission. * Cf. the similar usage in Latin: Caesar, BG 1.12 quae pars civitatis Helvétiae insignem calamitatem populo Ro- mano intulerat, ea princeps poends solvit, ? The same use occurs also in Latin: Cic. ad Fam. 12.23.2 legionibus . . . {чаз sibi concilüre pecüniü cogitabat eüsque ad urbem addücere.
3751:72 15 : asabaraibis : айтуауа : Aršādā : пата : didà : Harauvatiyà : а 73 vapara : atiy&i$g pasáva : Vivàna : hada : kara : nipadiy : tyaiy :aNya © 7777 74 va : avadāšim : agarbaya : ula : martiya : tyaisaly : fratama : anuSiya :
3766:91 sdva : ntyastàyam : haw : Атха : utā : татйуй : tyatsaiy : fratama : an
3774:%-? As read and restored by KT (who followed WB's restorations), except as noted in the following. * The і before and after the first gap were visible ta Cameron, though not to KT. 9 tyatkaily : fratama :] anušiyā [: ghata : agarbaya} Wb., after the traces seen by KT; tyaiSaily now confirmed by Cameron, who found the rest illegible. 3*7! [pasdva : niyas}tdyam Wh. after traces seen by KT; payme still legible, acc. to Cameron. # asariyata КТ; àkariyatàm WB; akariya^tà Bthl., WBn.
=== KLN maximum
25441:Derivative:  nimbus-ed,  adj. nimiety,  n.,  excess,  redundancy.  —  L.  nimietds, ‘excessiveness’,  fr.  nimius,  ‘beyond  measure,  ex¬ cessive’,  fr.  nimis  ‘too  much,  beyond  measure, excessively’,  which  prob.  stands  for  nimis, contraction  of  *  ne-mi-is  and  lit.  means  not  too little’,  fr.  negative  pref.  ne-  and  I.-E.  base  *mei-, ‘to  lessen’,  whence  also  L.  minor,  minus,  smaller, less’.  For  the  first  element  see  no,  adv.,  and  cp. nay,  for  the  second  see  minimum, niminy-piminy,  adj.,  mincing;  affected;  refined.
```


## [2026-09-05T20:39:55.967Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"Maximum\" SKT.txt | head -3; echo \"=== KLN\"; grep -n \"maximum\" KLN_1966.txt | head -3"
}
```


### [2026-09-05T20:39:56.048Z] TOOL RESULT

```
10918:'      maximum,  (L)    Ncut.  of  maximtu,
23177:maxim— maximum.
=== KLN
22613:major,  adj.  —  ME.  majour,  fr.  L.  major,  ‘greater’, fr.  earlier  *majjor,  for  *mag-yds  (neut.  majus, fr.  earlier  *majjus,  for  *mag-yos),  comparative of,  and  from  the  same  base,  as,  magnus,  ‘great’, rel.  to  magis,  ‘more,  rather’.  See  magnum  and cp.  mayor  and  the  second  word  in  force  majeure. Cp.  also  maximum.
23197:maxim,  n.,  precept,  principle.  —  ME.  maxime,  fr. MF.  (=  F.)  maxime,  fr.  ML.  maxima  (short  for L.  maxima  sententia,  ‘the  greatest  sentence ), fern,  of  maximus,  ‘greatest’.  See  maximum, maximal,  adj.,  highest,  greatest.  —  Formed  with adj.  suff.  -al  fr.  L.  maximus.  See  maximum. Derivatives:  maximal-ly,  adv..  Maximalist  (q.v.) Maximalist,  n.,  formerly,  a  member  of  the  ex¬ treme  radical  group  of  the  Russian  Social  Rev¬ olutionary  party.  —  Lit.  ‘one  who  insists  on all  his  demands’,  formed  fr.  L.  maximus  (see maximum)  and  suff.  -ist.  Cp.  Minimalist. Maximilian,  masc.  PN.  —  Compounded  of  the L.  names  Maximus  and  Aemilianus.  According to  Camden,  Frederick  III  gave  this  name  coined by  him  to  his  son,  hoping  that  the  latter  ‘would imitate  the  virtues’  of  Fabius  Maximus  and Scipio  Aemilianus.
23198:maximite,  n.,  a  synonym  of  cordite.  —  Named after  Hudson  Maxim  (1853-1927),  its  inventor. For  the  ending  see  subst.  suff.  -ite. maximize,  tr.v.,  to  raise  to  the  highest  possible degree.  —  Coined  by  the  English  philosopher Jeremy  Bentham  (1748-1832)  fr.  L.  maximus, ‘greatest’  (see  maximum),  and  suff.  -ize. Derivative:  maximiz-ation,  n.
```


## [2026-09-05T20:40:00.503Z] AGENT

Now I have everything. Writing the verification file.


## [2026-09-05T20:46:22.298Z] TOOL CALL #79: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk153.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 153,\n \"book_page\": 123,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Embhi\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *embʰi-, *empi- 'a kind of gnat/mosquito, (bee)' (Pokorny 311 = Walde-Pokorny I 125 'empi- Stechmücke, Biene?'; Wiktionary *h₁empí- 'gnat, biting insect'); NO Indo-European root meaning 'honey' is reconstructible here — IE 'honey' is *melit-, 'bee' is *bʰey-\",\n   \"note\": \"The root itself is real, the language label is right, but the gloss is not. Pokorny p. 311 heads the article 'embʰi-, empi-, Meaning: a kind of mosquito or bee', with a note on taboo variation bʰ : p, and the whole material is Gk. ἐμπίς 'a mosquito', OHG imbi (impi piano) 'swarm of bees', MHG imbe, NHG Imme, OE ymbe/imbe (*umbia) 'swarm of bees'. Walde-Pokorny I 125, the second reference, is the same article ('empi- \\\"Stechmücke, Biene\\\"?') and it explicitly puts BOTH of Nourai's key words outside the root: 'Über np. ang \\\"Biene\\\" und lat. apis \\\"Biene\\\" (beide dunkel) s. noch Boisacq 248 …' — 'both obscure'. Nourai's 'honey, honey bee' is therefore his own gloss, taken over from the Iranian words in the chart. And those Iranian words belong to an entirely different family: NP انگبین / MP angubēn / Sogd. angupēn go back to Old Iranian *angu-paina- (Gharib) or Proto-Iranian *Hangubáynah = *Hángwr̥ 'extract, resin' + *báynah 'bee' (Wiktionary), with the same *hangu- 'sap, resin' that gives NP انگژد angužad, انغوزه angoze and (as a loan) Skt. hiṅgu. So the chart fuses (a) a genuine European gnat/bee word and (b) an Iranian resin word, on the strength of a conjecture Horn published in 1893 (HRN 254). Watkins/AHD has no such root at all: bee is *bhei-1 (Pok. 116), honey *melit-.\",\n   \"note_fa\": \"ریشهٔ بازسازی‌شدهٔ *embʰi-/*empi- در پوکورنی (ص ۳۱۱) و والده-پوکورنی (ج ۱ ص ۱۲۵) واقعاً وجود دارد، اما معنای آن «نوعی پشه یا زنبور» است، نه «عسل». برچسب زبانی (هندواروپایی) درست است ولی معنای «عسل، زنبور عسل» افزودهٔ نورایی است؛ در هندواروپایی «عسل» *melit- و «زنبور» *bʰey- بازسازی می‌شود. مهم‌تر آنکه همان مرجعی که نورایی می‌آورد (والده-پوکورنی ج۱ ص۱۲۵) به‌صراحت می‌گوید فارسی نو «انگ (زنبور)» و لاتینی apis «هر دو تاریک/نامعلوم‌اند» و آن‌ها را زیر این ریشه نمی‌آورد. واژه‌های ایرانی این نمودار (انگبین، انغوزه، انگژد و وام‌واژهٔ سنسکریت hiṅgu) به خانوادهٔ ایرانی *hangu- «شیره، صمغ» تعلق دارند (ایرانی آغازین *Hangubáynah = *Hángwr̥ «شیره» + *báynah «زنبور»)، نه به ریشهٔ اروپایی «پشه/زنبور». نمودار نورایی در واقع بر حدس هرن (۱۸۹۳، ص ۲۵۴) استوار است که خودش آن را «یک گمانه» (Vermutung) خوانده است.\",\n   \"sources\": [\n    W+\"apis\",\n    W+\"%E1%BC%90%CE%BC%CF%80%CE%AF%CF%82\",\n    W+\"%D8%A7%D9%86%DA%AF%D8%A8%DB%8C%D9%86\",\n    W+\"Reconstruction:Proto-Iranian/Hangub%C3%A1ynah\",\n    W+\"%E0%A4%B9%E0%A4%BF%E0%A4%99%E0%A5%8D%E0%A4%97%E0%A5%81\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:311\", \"status\": \"partial\",\n     \"note\": \"POK_full.txt: 'Root / lemma: embʰi-, empi- | Meaning: a kind of mosquito or bee | Note: With taboo variation bʰ : pi | Material: Gr. ἐμπίς, -ίδος \\\"a mosquito\\\"; Old High German imbi (oldest evidence impi piano), Middle High German imbe (*embi-o) \\\"swarm of bees, beehive\\\" … Old English imbe (*umbia) \\\"swarm of bees\\\". References: WP. I 125, WH. I 57. Page(s): 311'. The page is exactly right, but it gives no 'honey' sense and contains no Latin, Sanskrit, Iranian or Sogdian material at all.\"},\n    {\"ref\": \"WLD1:125\", \"status\": \"partial\",\n     \"note\": \"WLD Bd. I p. 125 (incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt lines 8115-8174, between the running heads 'em- / en / 125' and '126 / en'), headword 'empi- \\\"Stechmücke, Biene\\\"?': 'Gr. ἐμπίς \\\"Stechmücke\\\"; ahd. imbi (ältester Beleg impi piano) mhd. imbe \\\"Bienenschwarm, Bienenstock\\\", erst spät-mhd. \\\"Biene\\\", nhd. Imme, ablautend ags. ymbe (*umbia) \\\"Bienenschwarm\\\"'. The page carries the root but explicitly excludes Nourai's two anchors: 'Über np. ang \\\"Biene\\\" und lat. apis \\\"Biene\\\" (beide dunkel)…'.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. bhei-1 and the essay on insects\", \"stance\": \"contradicts\",\n     \"note\": \"'The BEE (bhei-1) was particularly important as the producer of honey, for which we have the common Indo-European name melit-'; 'bhei-1. A bee. Germanic suffixed form *bin- in Old English béo, a bee: BEE. [Pok. bhei- 116.]'. Watkins reconstructs no *embhi- root at all.\"},\n    {\"src\": \"IEC\", \"where\": \"s.v. empis (leaf 145, ≈ p. 240) and s.v. apis (leaf 31, ≈ p. 12)\", \"stance\": \"partial\",\n     \"note\": \"Mann: 'empis, io \\\"insect; swarm\\\". WP I, 125. Gk. empís; OHG imbi \\\"swarm of bees\\\"; MHG imbe, OE imbe, id.; LG imm, wf. \\\"bee\\\"; Cz. cf. jepice…' — no honey sense, no Iranian. He keeps Latin apis in a SEPARATE, question-marked entry: 'apis (?) \\\"insect\\\". Cf. empis. Lat. cf. apis, gp. apium \\\"bee\\\"…'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 3.82 BEE and 5.84 HONEY (pp. 183, 383-4)\", \"stance\": \"partial\",\n     \"note\": \"3.82: 'Lat. apis, dim. apicula, etym.? … Ernout-M. 61. Walde-H. 1.57.' 5.84 HONEY: 'Av. *paēna-, implied by paēnaēna- \\\"prepared from honey\\\", NPers. angubīn \\\"bee-honey\\\", prob. as (bee's) \\\"milk\\\" or \\\"juice\\\" : Av. payah-, paēman- \\\"milk\\\" … Barth. 817.' Buck thus files the Persian word under a *paēna- 'honey/milk' word, not under any bee-root.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"ang, angu; angu-paěna\", \"verdict\": \"disputed\",\n     \"derivation\": \"Neither 'ang' nor 'angu' nor 'angu-paēna' is an attested Avestan word. Bartholomae's Altiranisches Wörterbuch (col. 817) knows only the adjective paēnaēna- 'aus Honig bestehend, bereitet' (Nirangistan 57), from which he reconstructs '*paena- m. \\\"Honig\\\"' and to which he attaches 'mp. angubīn, np. angubīn \\\"Bienenhonig\\\"'; Buck 5.84 likewise lists for Avestan only '*paēna-, implied by paēnaēna-'. The compound Nourai labels Avestan is in fact Gharib's Old/Proto-Iranian reconstruction *angu-paina- (SOD no. 1066), of which only the second member is (reconstructed) Avestan. Modern Wiktionary analyses the whole family as Proto-Iranian *Hangubáynah 'honey, beeswax' < *Hángwr̥ 'extract, resin' + *báynah 'bee'. Either way the first element angu- is the Iranian 'sap, resin' word (Bartholomae himself cites 'np. žad \\\"Gummi\\\", angu-žad \\\"Harz\\\"'), and nothing in it descends from a gnat/bee root *embʰi-. So the language label is wrong (Old Iranian reconstruction, not attested Avestan) and the arrow from the root box is unsupported.\",\n     \"derivation_fa\": \"در اوستایی هیچ واژه‌ای به صورت ang یا angu یا angu-paēna گواهی نشده است. بارتولومه (ستون ۸۱۷) تنها صفت paēnaēna- «ساخته‌شده از عسل» را می‌آورد و از آن *paena- «عسل» را بازسازی می‌کند و می‌افزاید: «فارسی میانه angubīn، فارسی نو انگبین (عسلِ زنبور)». بنابراین آنچه نورایی «اوستایی» خوانده در واقع بازسازی ایرانی باستان *angu-paina- (قریب، فرهنگ سغدی، مدخل ۱۰۶۶) است که تنها جزء دوم آن اوستایی است. ریشه‌شناسی امروزی (ویکی‌واژه) کل خانواده را از ایرانی آغازین *Hangubáynah «عسل، موم» می‌داند، مرکب از *Hángwr̥ «شیره، صمغ» و *báynah «زنبور». پس جزء نخست همان angu- «شیره/صمغ» است (بارتولومه خودش «انگژد = صمغ» را یاد می‌کند) و هیچ پیوندی با ریشهٔ *embʰi- «پشه/زنبور» ندارد: ادعای نورایی در این گره پذیرفتنی نیست.\",\n     \"sources\": [W+\"Reconstruction:Proto-Iranian/Hangub%C3%A1ynah\", W+\"%D8%A7%D9%86%DA%AF%D8%A8%DB%8C%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"SOD:42\", \"status\": \"partial\",\n       \"note\": \"Gharib, Sogdian Dictionary no. 1066 (SOD_pages.txt line 6812, leaf 107 ≈ printed p. 41-42): \\\"'nkwpyn B, S | angupēn (ʾngwpyn) © <*angu-paina-; Av. paena | honey | TSP 19.7, 16 n p232; BSTBL, Padm. 40; KG 368\\\". The page therefore supports *angu-paina- and the Avestan element paena, but it gives NO Avestan 'ang/angu', no 'sweet sap' gloss and no link to an IE bee root.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"col. 817 s.v. paēnaēna-\", \"stance\": \"partial\",\n       \"note\": \"'j. paēnaēna- Adj. (fem. °nī-) \\\"aus Honig bestehend, bereitet\\\" … Ableit. aus *paena- m. \\\"Honig\\\"; mp. angubīn, np. angubīn \\\"Bienenhonig\\\". — Ob zu lit. pienas \\\"Milch\\\"? … vgl. Hbs. PSt. 19, AGr. I 124.' No Avestan ang/angu anywhere in Bartholomae; grep for 'angu-' in BRT.txt returns only 'np. angu-žad \\\"Harz\\\"' (col. ~1085).\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 5.84 HONEY, p. 384\", \"stance\": \"partial\",\n       \"note\": \"'4. Av. *paēna-, implied by paēnaēna- \\\"prepared from honey\\\", NPers. angubīn \\\"bee-honey\\\", prob. as (bee's) \\\"milk\\\" or \\\"juice\\\" : Av. payah-, paēman- \\\"milk\\\", Skt. payas- \\\"milk, juice\\\", Lith. pienas \\\"milk\\\". Barth. 817.' Only *paēna- is offered for Avestan; the honey-word is derived from 'milk/juice', not from a bee-root.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"ang, angubin\", \"verdict\": \"plausible\",\n     \"derivation\": \"Middle Persian angubēn 'honey' is solidly attested: MacKenzie, CPD p. 11 'angubēn [DWBŠYA < A dbš; ʾngpyn' | N angubin] honey' (written with the Aramaic heterogram DWBŠYA from Aram. dbš 'honey') and p. 54 'magas ī angubēn: honey-bee'; Hübschmann, Persische Studien, index of Pahlavi forms: 'angubīn \\\"Honig\\\", phl. angpēn, arm. gaz-pēn'; Bartholomae col. 817 'mp. angubīn'. The ē of angubēn is guaranteed by the Armenian loan gazpēn 'tamarisk honey' (Horn no. 124). Two reservations: (a) the form Nourai prints, 'angubin', is the New Persian shape, not the Pahlavi one (angubēn, with -bēn < *-paina-); (b) a bare Pahlavi 'ang' meaning 'honey' is in neither MacKenzie nor Nyberg — the only MP angu on record is Gharib's note at SOD no. 2201, and that is the 'resin' word (MP angu, source of Sogd. inku), not 'honey'. The node is therefore right about angubēn and wrong about ang.\",\n     \"derivation_fa\": \"«انگبین» در فارسی میانه به صورت angubēn به‌خوبی گواهی شده است: مکنزی (فرهنگ کوچک پهلوی، ص ۱۱) angubēn را با هزوارش آرامی DWBŠYA و املای ʾngpyn' می‌آورد و «مگس انگبین» را «زنبور عسل» معنی می‌کند؛ هوبشمان نیز «phl. angpēn، ارمنی gaz-pēn» را ثبت کرده و همین وام‌واژهٔ ارمنی گواه کشیدگی ē است. دو نکته: نخست آنکه صورتی که نورایی نوشته (angubin) صورت فارسی نو است نه پهلوی؛ دوم آنکه «انگ» تنها در پهلوی به معنی «عسل» در هیچ فرهنگی نیامده است — تنها angu پهلوی که قریب یاد می‌کند به معنی «صمغ/شیره» است و منشأ inku سغدی. پس بخش angubēn درست و بخش ang بی‌پشتوانه است.\",\n     \"sources\": [W+\"%D8%A7%D9%86%DA%AF%D8%A8%DB%8C%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"WLD1:125\", \"status\": \"partial\",\n       \"note\": \"WLD I 125 (the empi- article) contains no Pahlavi form whatever; its only Iranian remark is 'Über np. ang \\\"Biene\\\" und lat. apis \\\"Biene\\\" (beide dunkel)…'. It cannot support a Pahlavi 'ang, angubin : honey' node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 11 (PHD.txt line 212) and p. 54\", \"stance\": \"supports\",\n       \"note\": \"'angubēn [DWBŠYA < A dbš; ʾngpyn' | N angubin] honey'; 'magas [mks | P mgs, N ~] fly. ~ ī angubēn: honey-bee'. No bare MP 'ang' in the dictionary.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien, §24 and the Pahlavi word-list (HUB.txt lines 4322, 4880, 6239)\", \"stance\": \"supports\",\n       \"note\": \"'In sūbān \\\"Hirt\\\" = zd. *fšupāna- blieb u aus lautlichen Gründen, ebenso in angubīn, angabīn \\\"Honig\\\" etc.'; 'Vgl. auch angabīn (A. M.) \\\"Honig\\\" = angubīn'; 'abrēšum \\\"Seide\\\", arm. aprišum; angubīn \\\"Honig\\\", phl. angpēn, arm. gaz-pēn'.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\",\n       \"note\": \"grep -i 'angub|angpen|anguben' over NYB_vol1.txt / NYB_vol2_glossary.txt returns nothing; the word is not in Nyberg's glossary.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"ang «انگ ۲»\", \"verdict\": \"plausible\",\n     \"derivation\": \"Nourai's real source is Horn, Grundriss p. 254 (Nachtrag to no. 124), which is a conjecture, not a result: 'Als eine Vermutung möchte ich hier aussprechen, dass np. eng \\\"Biene\\\" vielleicht dasselbe Wort wie lat. apis ist' — and Horn goes on (p. 255) to reject the usual apis ~ Gk. ἐμπίς equation and to guess instead that Latin apis is an Oscan loan. At no. 124 (p. 29) Horn had already conceded 'Das erste Glied des Compositums eng \\\"Biene\\\" (Wörterbücher: ānik, enik) vermag ich im Neupersischen nicht zu belegen; es wird im Gazophylacium citirt, wohin es aber auch nur aus persischen Originalwörterbüchern gekommen sein wird' — i.e. NP eng 'bee' cannot be documented in real Persian texts. Borhan-e Qāṭeʿ p. 174 gives انگ only as 'مجرای آب … که کوزه‌گران از سفال سازند' (a potter's earthenware water-conduit) and as a place-name in India; Dehkhoda/Moʿin add انگ = زنبور 'bee' and انگ = شیره، عصاره 'sap, extract' (the latter explicitly linked to انگبین) — but no sense 'honey'. So the gloss is wrong: انگ is 'bee' or 'sap', and 'honey' is انگبین. The four script extras are all real words: انگبین 'honey' < MP angubēn; سکنجبین (سرکنگبین) = سرکه 'vinegar' + انگبین, borrowed into Arabic as سكنجبين (Horn no. 124: 'arab. LW anjubīn, vergl. siskanjubīn (Ibn Beiṭār)'); گزانگبین 'tamarisk manna' (whence Arm. gazpēn); انغوزه 'asafoetida', which however belongs to the *hangu- 'resin' branch (cf. انگژد angužad, انگدان angudān) — the same first element, not a bee-word.\",\n     \"derivation_fa\": \"خاستگاه واقعی این گره، حاشیهٔ هرن در «مبانی ریشه‌شناسی فارسی نو» ص ۲۵۴ است که خودِ او آن را «یک گمانه» می‌نامد: «به‌عنوان یک حدس می‌گویم که شاید فارسی نو eng «زنبور» همان واژهٔ لاتینی apis باشد». هرن پیش‌تر در مدخل ۱۲۴ (ص ۲۹) اعتراف کرده بود که «جزء نخست ترکیب، یعنی eng «زنبور»، را نمی‌توانم در فارسی نو گواه بیاورم؛ فقط در فرهنگ‌های فارسی و از آنجا در Gazophylacium آمده است». برهان قاطع (ص ۱۷۴) نیز «انگ» را تنها «مجرای آب که کوزه‌گران از سفال سازند» و نام ولایتی در هندوستان معنی کرده، و دهخدا و معین معناهای «زنبور» و «شیره، عصاره» (همان که با انگبین پیوند دارد) را افزوده‌اند؛ هیچ‌کدام «عسل» نیست. پس معنای مدخل نادرست است: «عسل» انگبین است نه انگ. چهار واژهٔ افزودهٔ نمودار همه واقعی‌اند: انگبین از angubēn پهلوی؛ سکنجبین (سرکنگبین) از سرکه + انگبین که معرّب آن «سكنجبين» است؛ گزانگبین که وام ارمنی gazpēn از آن است؛ و انغوزه که اما به شاخهٔ *hangu- «صمغ» (مانند انگژد و انگدان) تعلق دارد، نه به واژهٔ «زنبور».\",\n     \"sources\": [W+\"%D8%A7%D9%86%DA%AF%D8%A8%DB%8C%D9%86\", \"https://abadis.ir/fatofa/%D8%A7%D9%86%DA%AF/\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:174\", \"status\": \"partial\",\n       \"note\": \"Borhan-e Qāṭeʿ, BQT_v1_pages.txt leaf 391 (= printed p. 174, the leaf whose neighbours carry انگاره at leaf 392 ≈ p.175-177 and انگشت at leaf 393-394): 'انگ . بفتح اول و سکون ثانی و کاف فارسی . مجرای آب را گویند که کوزه‌گران از سفال سازند و بجهت عبور کردن آب بهم وصل کنند. و نام ولایتی است در هندوستان'. The page has the headword انگ, but not with the sense 'honey'.\"},\n      {\"ref\": \"HRN:254\", \"status\": \"partial\",\n       \"note\": \"Horn, Grundriss p. 254 (HRN.txt form-feed leaf 276): '124. Als eine Vermutung möchte ich hier aussprechen, dass np. eng \\\"Biene\\\" vielleicht dasselbe Wort wie lat. apis ist. Das letztere wird gewöhnlich mit gr. ἐμπίς \\\"Stechfliege, Schnake\\\" zusammengestellt, eine Identification, die mir schon darum sehr unwahrscheinlich ist…'. It supports the ang–apis pairing that Nourai draws, but only as an explicitly labelled conjecture, glosses the word 'Biene' (bee) not 'honey', and (p. 255) argues AGAINST connecting apis with ἐμπίς.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin s.v. انگ (via abadis.ir), with Dehkhoda and Amid on the same page\", \"stance\": \"partial\",\n       \"note\": \"Moʿin: 'تنبوشه' (earthenware pipe); 'نشان بر کالای تجارتی'; 'شیره، عصاره (= انج، انغ)'; 'زنبور؛ زنبور عسل'. Dehkhoda adds the note that the 'شیره، عصاره' sense is the one behind انگبین (original 'انگ‌گبین'). No sense 'honey'.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn no. 124, p. 29\", \"stance\": \"partial\",\n       \"note\": \"'124. engebīn (AM.), engübīn \\\"Honig\\\", vergl. terengubīn, sikengubīn, sirkengubīn, gezengubīn, gulengubīn; arab. LW. anjubīn, vergl. siskanjubīn (Ibn Beiṭār) u. a. m. phlv. angpēn, angumēn (ē beweist das arm. LW. gazpēn \\\"Tamariskenhonig\\\"). … Das erste Glied des Compositums eng \\\"Biene\\\" … vermag ich im Neupersischen nicht zu belegen.' Confirms every one of Nourai's script extras but denies that انگ itself is attestable.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Sogdian\", \"words\": \"`nkwpyn\", \"verdict\": \"disputed\",\n     \"derivation\": \"The Sogdian word itself is impeccable: Gharib no. 1066 \\\"'nkwpyn (Buddhist, Christian/Sogdian script) angupēn (ʾngwpyn) © <*angu-paina-; Av. paena — honey\\\", with the Manichaean variant no. 1041 *ngwpyn; attested TSP 19.7, 16, Padmacintāmaṇi 40. But that analysis makes it the exact Sogdian counterpart of Middle Persian angubēn (node 2) — a sister form of the same Iranian compound *angu-paina- / Proto-Iranian *Hangubáynah, whose descendants Wiktionary lists as Sogd. angupēn, Khwarezmian ʾnkby, Parthian angubēn, MP angubēn, Pashto angabin, Kurdish hingiwîn, Talysh anqevin. Drawing it straight from the root box (a PIE gnat/bee word) instead of from the Iranian compound is what modern scholarship rejects; the Sogdian form is Iranian inheritance, not a separate branch of *embʰi-.\",\n     \"derivation_fa\": \"خودِ واژهٔ سغدی بی‌عیب است: قریب (مدخل ۱۰۶۶) صورت ʾnkwpyn / angupēn را با بازسازی *angu-paina- و ارجاع به paena اوستایی ثبت کرده و شواهد آن را از متون بودایی سغدی آورده است. اما همین تحلیل نشان می‌دهد که این واژه دقیقاً همتای فارسی میانهٔ angubēn است، یعنی هم‌ریشهٔ گرهٔ شمارهٔ ۲ و بازماندهٔ همان ترکیب ایرانی *angu-paina- (ایرانی آغازین *Hangubáynah)، که بازماندگان دیگرش خوارزمی ʾnkby، پارتی angubēn، پشتو angabin، کردی hingiwîn و تالشی انگوین‌اند. بنابراین کشیدن پیکان مستقیم از ریشهٔ هندواروپایی «پشه/زنبور» به این واژه نادرست است؛ این واژه میراث ایرانی است نه شاخه‌ای جداگانه از *embʰi-.\",\n     \"sources\": [W+\"Reconstruction:Proto-Iranian/Hangub%C3%A1ynah\"],\n     \"ref_check\": [\n      {\"ref\": \"SOD:42\", \"status\": \"supports\",\n       \"note\": \"SOD_pages.txt line 6812 (leaf 107 ≈ printed p. 41-42): \\\"1066 'nkwpyn  B, S | angupēn (ʾngwpyn) ©<*angu-paina-; Av. paena | honey | TSP 19.7, 16 n p232; BSTBL, Padm. 40; KG 368\\\"; and \\\"1041 *ngwpyn M ⇒ 'nkwpyn\\\". The Sogdian word and gloss are exactly as charted; the page says nothing about an IE bee root.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"col. 817 s.v. paēnaēna-\", \"stance\": \"partial\",\n       \"note\": \"'Ableit. aus *paena- m. \\\"Honig\\\"; mp. angubīn, np. angubīn \\\"Bienenhonig\\\"' — the same compound, analysed as *angu- + *paina- 'honey', with no IE bee-root.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 5.84 HONEY, p. 384\", \"stance\": \"partial\",\n       \"note\": \"'Av. *paēna-, implied by paēnaēna- … NPers. angubīn \\\"bee-honey\\\", prob. as (bee's) \\\"milk\\\" or \\\"juice\\\" : Av. payah-, paēman- \\\"milk\\\" … Barth. 817.'\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Sanskrit\", \"words\": \"hingu\", \"verdict\": \"disputed\",\n     \"derivation\": \"Sanskrit hiṅgu- is asafoetida (Ferula assa-foetida) and its resin, a standard item of the Ayurvedic and Buddhist materia medica; the gloss 'resin' is right. Its origin, however, is not Indo-European inheritance: Laufer, Sino-Iranica p. 361, discussing Chinese hin-gu/hün-gu ← Skt. hiṅgu, states flatly 'In my opinion, the Sanskrit word is an ancient loan from Iranian', noting the Indian vernacular forms with initial i- (Telugu inguva, Malay angu). Wiktionary derives it from Proto-Iranian *Hángwr̥ 'extract, resin' (with an irregular a > i), the same element that yields NP انگژد angužad 'asafoetida resin' — a form Bartholomae himself quotes ('np. žad \\\"Gummi\\\", angu-žad \\\"Harz\\\"') — and انغوزه, انگدان. Pokorny p. 311, the page cited, contains no Sanskrit at all: its material is only Gk. ἐμπίς, OHG imbi, OE ymbe. So the arrow from *embʰi- is not supported by any source; hiṅgu is an Iranian trade-word for resin borrowed into Indic.\",\n     \"derivation_fa\": \"hiṅgu سنسکریت همان «انغوزه» (صمغ گیاه Ferula assa-foetida) است و معنای «صمغ» درست است، اما وام‌واژه است نه میراث هندواروپایی. لاوفر در «چین و ایران» (ص ۳۶۱) در بحث از صورت‌های چینی این واژه می‌نویسد: «به گمان من واژهٔ سنسکریت وام کهنی از ایرانی است»، و صورت‌های گویشی هندی با i- آغازین (تلوگو inguva) را گواه می‌آورد. ویکی‌واژه نیز آن را از ایرانی آغازین *Hángwr̥ «شیره، صمغ» می‌داند، همان جزئی که «انگژد» و «انغوزه» و «انگدان» فارسی از آن است (بارتولومه خود «انگژد = صمغ» را نقل کرده است). افزون بر این، صفحهٔ ۳۱۱ پوکورنی که نورایی به آن ارجاع داده هیچ صورت سنسکریتی ندارد. پس پیکانِ *embʰi- ← hiṅgu بی‌پشتوانه است.\",\n     \"sources\": [W+\"%E0%A4%B9%E0%A4%BF%E0%A4%99%E0%A5%8D%E0%A4%97%E0%A5%81\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:311\", \"status\": \"not_found\",\n       \"note\": \"The article on p. 311 ('embʰi-, empi-, a kind of mosquito or bee') was read in full in POK_full.txt: its entire material is 'Gr. ἐμπίς, -ίδος \\\"a mosquito\\\"; Old High German imbi …, Middle High German imbe …, Old English imbe (*umbia) \\\"swarm of bees\\\"'. There is no Sanskrit hiṅgu, and no Indo-Iranian form at all, on that page.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SIN\", \"where\": \"Laufer, Sino-Iranica pp. 358-361 (SIN.txt lines 1745-1780)\", \"stance\": \"contradicts\",\n       \"note\": \"'(2) Sanskrit hiṅ-ku, *hin-gu; hin-yü; hün-k'ü, *hun-gu; corresponding to Sanskrit hiṅgu. In my opinion, the Sanskrit word is an ancient loan from Iranian. Garcia gives imgo or imgara as Indian name, and forms with initial i appear in Indian vernaculars: cf. Telugu inguva…'\"},\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.v. (BRT.txt line 21517)\", \"stance\": \"partial\",\n       \"note\": \"'Vgl. ai. jatu- n. \\\"Gummi\\\", np. žad \\\"Gummi\\\", angu-žad \\\"Harz\\\"' — Bartholomae has the Iranian angu- 'resin' compound, i.e. the family hiṅgu really belongs to, and nowhere connects it with a bee/gnat root.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Sogdian\", \"words\": \"inku, `ynkw\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Gharib no. 2201 gives exactly this: \\\"'ynkw B | inku ©<Skt. hiṅgu, MP angu | (اَنغوزه) | Hen. AION 1965, 36 n 1\\\", followed by no. 2202 \\\"'ynkwmync | inkumenc | gum, (of) gum | TSP 8.111 n p216\\\". The circled '<' is Gharib's borrowing sign, so the dictionary itself states that Buddhist Sogdian inku is taken from Sanskrit hiṅgu (with Middle Persian angu beside it) — precisely the arrow Nourai draws — and Henning (AION 1965, p. 36 n. 1) is the authority behind it. Semantically the Sogdian word keeps the Indian trade-sense 'asafoetida resin', and the derivative inkumenc means 'gum, (of) gum'.\",\n     \"derivation_fa\": \"قریب در فرهنگ سغدی (مدخل ۲۲۰۱) دقیقاً همین را می‌آورد: «ʾynkw (سغدی بودایی) inku، وام‌گرفته از hiṅgu سنسکریت، و فارسی میانه angu»، و در مدخل ۲۲۰۱/۲۲۰۲ صورت مشتق ʾynkwmync / inkumenc «صمغی، از صمغ» را ثبت می‌کند؛ مأخذ او هنینگ (AION ۱۹۶۵، ص ۳۶، پانوشت ۱) است. پس همان پیکانی که نورایی کشیده — وام‌گیری سغدی از سنسکریت — در منبعِ خودش به‌روشنی آمده و معنای «صمغ» نیز درست است. ادعای نورایی در این گره درست است.\",\n     \"sources\": [W+\"%E0%A4%B9%E0%A4%BF%E0%A4%99%E0%A5%8D%E0%A4%97%E0%A5%81\"],\n     \"ref_check\": [\n      {\"ref\": \"SOD:87\", \"status\": \"supports\",\n       \"note\": \"SOD_pages.txt line 10120 (leaf 152 ≈ printed p. 86-87): \\\"2201 'ynkw B | inku ©<Skt. hingu, MP angu | Hen. AION 1965, 36 n 1\\\"; \\\"2202 'ynkwmync B | inkumenc | gum | (of) gum | TSP 8.111 n p216; Hen. AION 1965, 36 n 1\\\". Exactly Nourai's forms, gloss and direction of borrowing.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SIN\", \"where\": \"Laufer, Sino-Iranica pp. 358-361\", \"stance\": \"supports\",\n       \"note\": \"Laufer traces hiṅgu through Chinese hin-gu / hün-gu and Iranian, calling the Sanskrit word 'an ancient loan from Iranian' — the same Central Asian trade route along which Sogdian inku was taken over.\"},\n      {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Dictionary of Khotan Saka\", \"stance\": \"silent\",\n       \"note\": \"grep for 'hingu|inku|ynkw' in ISS_alt_DKS.txt yields no relevant Khotanese entry; the Khotanese side is silent on this word.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Latin\", \"words\": \"apis\", \"verdict\": \"disputed\",\n     \"derivation\": \"Latin apis 'bee' (gen. pl. apum/apium, dim. apicula) is old and common, but every authority on the desk says its origin is unknown, and Nourai's own reference is one of them. Walde-Pokorny I 125 — the page cited — keeps apis OUT of the empi- article and remarks 'Über np. ang \\\"Biene\\\" und lat. apis \\\"Biene\\\" (beide dunkel) s. noch Boisacq 248, Vf. LEWb.2 u. apis'. Klein: 'Apis, a genus of bees. — L., \\\"bee\\\", of unknown etymology.' Buck 3.82: 'Lat. apis, dim. apicula, etym.?' Ernout–Meillet s.v. apis: the Indo-European bee-word was *bhei- (see fucus), and 'Il n'est pas impossible que ap-, api-, supposé par le latin, ait quelque rapport avec ce mot. Mais on ne saurait préciser.' Mann keeps 'apis (?) \\\"insect\\\"' as a separate, question-marked entry from empis. Modern work (de Vaan; Wiktionary) treats apis as a European substrate word — Vennemann compares Egyptian ꜥfj 'bee' — and notes the traditional link to ἐμπίς as no more than a hypothesis; Horn (pp. 254-5), Nourai's other source, argued against it and guessed at an Oscan loan instead. Nothing supports a regular descent *embʰi- > apis (which would in any case require an unexplained loss of the nasal).\",\n     \"derivation_fa\": \"apis لاتینی «زنبور» واژه‌ای کهن و پرکاربرد است، اما همهٔ مراجع ریشهٔ آن را نامعلوم می‌دانند — از جمله همان مرجعی که نورایی آورده است. والده-پوکورنی (ج۱ ص۱۲۵) apis را بیرون از مدخل empi- نگه می‌دارد و می‌نویسد: «دربارهٔ فارسی نو ang «زنبور» و لاتینی apis «زنبور» (هر دو تاریک) …». کلاین می‌نویسد: «apis، لاتینی «زنبور»، با ریشه‌شناسی نامعلوم»؛ باک (۳٫۸۲): «lat. apis … ریشه‌شناسی؟»؛ ارنو-مه‌یه: نام هندواروپایی زنبور *bhei- بوده و «بعید نیست ap-/api- لاتینی پیوندی با آن داشته باشد، اما نمی‌توان دقیق سخن گفت». پژوهش امروزی (دو ڤان و ویکی‌واژه) apis را واژه‌ای از زیرلایهٔ اروپایی می‌شمارد و پیوند سنتی آن با ἐμπίς را تنها یک فرضیه می‌داند؛ هرن نیز (ص ۲۵۴–۲۵۵) همین پیوند را رد کرده و وام‌گیری از اُسکی را پیشنهاد داده است. پس پیکانِ *embʰi- ← apis پذیرفتنی نیست (تحول آوایی حذف خیشوم نیز توضیح‌ناپذیر می‌ماند).\",\n     \"sources\": [W+\"apis\"],\n     \"ref_check\": [\n      {\"ref\": \"WLD1:125\", \"status\": \"contradicts\",\n       \"note\": \"WLD Bd. I p. 125, last paragraph of the empi- article: 'Über np. ang \\\"Biene\\\" und lat. apis \\\"Biene\\\" (beide dunkel) s. noch Boisacq 248, Vf. LEWb.2 u. apis (letzteres nicht nach Holthausen IF. 35, 132 zu opus; van der Velden … erinnert an bask. abia \\\"Stechfliege\\\").' Walde-Pokorny mention apis only to say it is obscure and NOT part of the root.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966, s.v. 'Apis, a genus of bees' (leaf pp. 90-91)\", \"stance\": \"contradicts\",\n       \"note\": \"'Apis, a genus of bees. — L., \\\"bee\\\", of unknown etymology. Cp. Apium, ache, \\\"parsley\\\".'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 3.82 BEE, p. 183\", \"stance\": \"contradicts\",\n       \"note\": \"'3. Lat. apis, dim. apicula, etym.? Hence It. ape, OFr. ef …; fr. dim., It. pecchia, Fr. abeille, Sp. abeja. Ernout-M. 61. Walde-H. 1.57. REW 523, 525.'\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. apis (LAT.txt line 4399ff.)\", \"stance\": \"contradicts\",\n       \"note\": \"'Les dialectes indo-européens qui vont du slave à l'indo-celtique ont eu un nom de l'\\\"abeille\\\" inconnu aux autres langues: v. sous lat. fucus: ce nom était de la forme *bhei-. Il n'est pas impossible que ap-, api-, supposé par le latin, ait quelque rapport avec ce mot. Mais on ne saurait préciser.'\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. apis (leaf 31, ≈ p. 12)\", \"stance\": \"partial\",\n       \"note\": \"'apis (?) \\\"insect\\\". Cf. empis. Lat. cf. apis, gp. apium \\\"bee\\\"; OCz. op-oka, -uka, ap-oka \\\"honeycomb\\\" beside Cz. jepice \\\"mayfly\\\".' Mann sets it up as a separate, question-marked lemma cross-referring to empis, not as a descendant of it.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"English\", \"words\": \"apiary, apiology\", \"verdict\": \"confirmed\",\n     \"derivation\": \"apiary (1654) is Latin apiārium 'beehouse, beehive' (Varro, Columella), the neuter of apiārius 'relating to bees', from apis; apiology 'the scientific study of bees' is a 19th-century hybrid coined from L. apis + Gk. -λογία. Both are straightforward learned Latinisms taken directly into English, not inherited, so the arrow Latin → English is correct. (Only the ultimate root above Latin is at issue, see node 7.)\",\n     \"derivation_fa\": \"apiary (نخستین کاربرد ۱۶۵۴ م.) از apiārium لاتینی «زنبورستان، کندو» است، صورت خنثای apiārius «مربوط به زنبور» از apis؛ و apiology «زنبورشناسی» واژه‌ای دورگهٔ ساختهٔ سدهٔ نوزدهم از apis لاتینی و -λογία یونانی است. هر دو وام‌واژهٔ عالمانه‌اند و مستقیم از لاتینی به انگلیسی رفته‌اند، پس پیکان «لاتینی ← انگلیسی» درست است؛ تنها ریشهٔ بالادست (گرهٔ ۷) محل تردید است. ادعای نورایی در این گره درست است.\",\n     \"sources\": [W+\"apis\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:89\", \"status\": \"supports\",\n       \"note\": \"Klein 1966: 'apiary, n., a place where bees are kept. — L. apiarium, \\\"beehouse, beehive\\\", fr. apis. See Apis, a genus of bees.' and 'apiology, n., the scientific study of bees. — A hybrid coined fr. L. apis, \\\"bee\\\", and Gk. -λογία … See Apis, a genus of bees, and -logy.' In the two-pages-per-leaf 1966 scan these stand on the spread footed '90 91'; Nourai's page 89 is one spread earlier in the same alphabetical stretch (aphtha…Apium), so the citation is off by about one page in this printing but the entries are certainly his.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., s.v. Apiary\", \"stance\": \"supports\",\n       \"note\": \"'Apiary, a place for bees. (L.) … [apia]rium, neut. of apiarius, belonging to bees. — L. api-, for apis, a bee.'\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dict. vol. 1, s.v. apiary\", \"stance\": \"supports\",\n       \"note\": \"'a-pi-a-ry, n. 1. A place where bees are kept. 2. A collection of hives, colonies of bees, and bee-culture appliances'; with 'apiarian … Of or pertaining to bees or an apiary'.\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"Greek\", \"words\": \"ampis\", \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"There is no Greek word ampis, and no Greek word of that shape means 'honey' (Greek 'honey' is μέλι méli, PIE *melit-). What Pokorny actually prints on the cited page 311 is 'Gr. ἐμπίς, -ίδος \\\"a mosquito\\\"' — empís, a gnat or mosquito (LSJ also 'larva of the oestrus fly'); Walde-Pokorny I 125 has the same, 'Gr. ἐμπίς \\\"Stechmücke\\\"'; Mann glosses his lemma empis 'insect; swarm'. Wiktionary: ἐμπίς 'mosquito, gnat', popularly linked to ἐμπίνω 'to drink (blood)', with the Pokorny comparison to Proto-West-Germanic *imbī 'bee' and PIE *h₁empí- 'gnat, biting insect' explicitly 'not universally accepted'. So both the shape (a for e, loss of the -í-) and the gloss ('honey', imported from Nourai's root box) are wrong. I rendered pdf page 153 at 300 dpi (copy saved to data/verification/sources/refs/ocr/BOOK/153.png) and read it: the printed Greek box really does read 'ampis : honey', so the JSON is a faithful extraction and the error is the book's.\",\n     \"derivation_fa\": \"واژه‌ای به صورت ampis در یونانی وجود ندارد و هیچ واژهٔ یونانی با این ساخت به معنای «عسل» نیست («عسل» در یونانی μέλι است). آنچه پوکورنی در همان صفحهٔ ۳۱۱ چاپ کرده «ἐμπίς، -ίδος: نوعی پشه» است، و والده-پوکورنی نیز همان را «Stechmücke (پشهٔ گزنده)» آورده و مان آن را «حشره؛ انبوه/گروه» معنی کرده است. ویکی‌واژه هم ἐμπίς را «پشه، مگسک» می‌داند و مقایسهٔ پوکورنی با *imbī ژرمنی غربی را «مورد پذیرش همگانی نه» می‌شمارد. پس هم صورت (a به جای e) و هم معنی («عسل» که از جعبهٔ ریشه به اینجا سرایت کرده) نادرست است. تصویر صفحهٔ ۱۵۳ کتاب را با دقت ۳۰۰dpi گرفتم و خواندم: در خودِ کتاب هم «ampis : honey» چاپ شده است؛ بنابراین خطا از چاپ کتاب است نه از خوانش اسکن.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"ampis : honey\",\n     \"correct_form\": \"ἐμπίς (empís) 'gnat, mosquito'\",\n     \"sources\": [W+\"%E1%BC%90%CE%BC%CF%80%CE%AF%CF%82\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:311\", \"status\": \"contradicts\",\n       \"note\": \"POK_full.txt, 'Root / lemma: embʰi-, empi-, Page(s): 311': 'Material: Gr. ἐμπίς, -ίδος \\\"a mosquito\\\"'. The page gives neither the form 'ampis' nor the sense 'honey'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I p. 125\", \"stance\": \"contradicts\",\n       \"note\": \"'empi- \\\"Stechmücke, Biene\\\"? Gr. ἐμπίς \\\"Stechmücke\\\"; ahd. imbi …' — mosquito, not honey, and the form is empís.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. empis (leaf 145, ≈ p. 240)\", \"stance\": \"contradicts\",\n       \"note\": \"'empis, io \\\"insect; swarm\\\". WP I, 125. Gk. empís; OHG imbi \\\"swarm of bees\\\"; MHG imbe, OE imbe, id.; LG imm, wf. \\\"bee\\\"…' — 'insect', never 'honey'.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Ěmos\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE superlative/ordinal suffix *-m̥mo- (beside *-tm̥mo-) > Skt. -ama-, Av. -əma-, OP -ama-, Lat. -imus/-umus, Goth. -uma, Gk. -omos; Mann IEC 257 files it as '-amos, superlative extn.'\",\n   \"note\": \"Nourai's reference is exact and this is the strongest entry on the page. Mann, An Indo-European Comparative Dictionary p. 257, prints '-amos, superlative extn. in Skt. gurut-amáḥ, apamaḥ \\\"heaviest; hindmost\\\"; Av. frat-əmō, up-əmō \\\"foremost\\\"; ap-əmō \\\"last\\\"; Hitt. sept-amas \\\"seventh\\\"; … Lat. inf-imus, post-umus \\\"lowest; latest\\\"; Osc. ness-imas \\\"next\\\"; OIr. ness-am; Go. aft-uma \\\"latter, last\\\"; OE hindema; Gk. hebd-omos; OCS sedmyi; … Faliscan max-omo \\\"Maximus\\\"; Per. čahār-um \\\"4th\\\"; Kurd. čuvar-em; Per. haft-um, Kurd. hewtem \\\"7th\\\"' — i.e. every language Nourai charts, including the Persian ordinals, is on that one page. The gloss 'a suffix meaning most or last' is right (superlatives and ordinals). Only the citation form is Nourai's own: the mainstream reconstruction is the zero-grade *-m̥mo- (whence Skt. -ama-, Av. -əma-, Lat. -imus), and Mann himself writes -amos; 'Ěmos' with a full front vowel is Nourai's normalisation of the Avestan -əmō. Hence 'plausible' rather than 'confirmed'.\",\n   \"note_fa\": \"این مدخل استوارترین بخش صفحه است و ارجاع نورایی دقیق است. مان در «فرهنگ تطبیقی هندواروپایی» (ص ۲۵۷) مدخل «amos-، پسوند صفت عالی» را می‌آورد با همین گواه‌ها: سنسکریت gurut-amáḥ و apamaḥ، اوستایی frat-əmō و up-əmō «پیش‌ترین» و ap-əmō «واپسین»، لاتینی inf-imus و post-umus، گوتی aft-uma، یونانی hebd-omos، و حتی «فارسی čahār-um و haft-um؛ کردی čuvar-em و hewtem». معنای «پسوندی به معنی برترین یا واپسین» درست است. تنها نکته آنکه صورت بازسازی‌شدهٔ پذیرفتهٔ امروزی *-m̥mo- (درجهٔ صفر) است — که از آن -ama- سنسکریت، -əma- اوستایی و -imus لاتینی می‌آید — و مان خود -amos می‌نویسد؛ «Ěmos» با واکهٔ کامل، صورت هنجارشدهٔ خودِ نورایی از -əmō اوستایی است. از این رو داوری «با احتیاط پذیرفتنی».\",\n   \"sources\": [\"https://en.wiktionary.org/wiki/%D9%80%D9%85\", \"https://www.etymonline.com/word/maximum\"],\n   \"ref_check\": [\n    {\"ref\": \"IEC:257\", \"status\": \"supports\",\n     \"note\": \"IEC.txt line 3787, on the leaf whose running heads give pp. 256/257: '-amos, superlative extn. in Skt. gurut-amáḥ, apamaḥ \\\"heaviest; hindmost\\\"; Av. frat-əmō, up-əmō \\\"foremost\\\"; ap-əmō \\\"last\\\"; Hitt. sept-amas \\\"seventh\\\"; Alb. i prap-ém …; Lat. inf-imus, post-umus \\\"lowest; latest\\\"; Osc. ness-imas, f. pl. \\\"next\\\"; OIr. ness-am \\\"next\\\"; … Go. aft-uma \\\"latter, last\\\"; OE hindema \\\"hindmost\\\"; … Gk. hebd-omos; OCS sedmyi; OLi. sekmas \\\"seventh\\\" …; Faliscan max-omo \\\"Maximus\\\"; Per. čahār-um \\\"4th\\\"; Kurd. čuvar-em, id.; Per. haft-um, Kurd. hewtem \\\"7th\\\", etc.' Every element of Nourai's chart is on this page.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AVG\", \"where\": \"Jackson, Avesta Grammar §849, p. 233\", \"stance\": \"supports\",\n     \"note\": \"'22. Av. -ma = Skt. -ma (Whitney §1224i). §849. With -ma as secondary suffix are made a few superlatives from prepositions, a few ordinal numerals, a small number of adjectives from nouns … Av. apəma- \\\"last\\\" = Skt. apamá-; Av. upəma- \\\"highest\\\" = Skt. upamá-; Av. fratəma- \\\"first\\\" = Skt. prathamá-; Av. nāuma- \\\"ninth\\\" = Skt. navamá-.'\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.vv. meg- and mei-2\", \"stance\": \"partial\",\n     \"note\": \"Watkins does not lemmatise the suffix as a root, but uses it: 'Suffixed (superlative) form *mag-samo- in Latin maximus, greatest: MAXIM, MAXIMUM'; 'further suffixed (superlative) form *minu-mo- in Latin minimus, least: MINIMUM'.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. posterus 3° postumus (LAT.txt line 49378ff.)\", \"stance\": \"supports\",\n     \"note\": \"'postumus: qui vient le tout dernier … Le suffixe est le même que dans infimus, primus, decumus, et l'adjectif a dû d'abord servir de prénom, dans la série des prénoms numéraux qu'il terminait: Quintus, Sextus, Decumus, Decimus, et finalement Postumus.'\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"-emô\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Avestan -əma- is the regular secondary suffix forming superlatives from prepositions/adverbs and ordinals: Jackson, Avesta Grammar §849 (p. 233) 'Av. apəma- \\\"last\\\" = Skt. apamá-; Av. upəma- \\\"highest\\\" = Skt. upamá-; Av. fratəma- \\\"first\\\" = Skt. prathamá-; Av. nāuma- \\\"ninth\\\" = Skt. navamá-'; the parallel -təma- (= Skt. -tama-) is treated at §841. Nourai's '-emô' is the nominative singular masculine -əmō, which is how Mann cites the forms (frat-əmō, up-əmō, ap-əmō) and therefore how Nourai took them over; the gloss 'most or extreme' is exactly the function. Kent (Old Persian §) confirms the Old Iranian side: 'Secondary comparison … was made in Aryan by the use of -tara- and -tama-, cf. Gk. -τερος -τατος, Lat. ex-terus and ex-timus. The comparative is seen in OP fratara- and adv. apataram, the superlative in fratama-.'\",\n     \"derivation_fa\": \"«ـəma-» در اوستایی پسوند ثانوی و سازندهٔ صفت عالی از حروف اضافه/قیدها و نیز سازندهٔ شمار ترتیبی است. جکسون در «دستور اوستایی» (بند ۸۴۹، ص ۲۳۳) می‌نویسد: «با پسوند -ma چند صفت عالی از حروف اضافه و چند عدد ترتیبی ساخته می‌شود»، و گواه‌ها را می‌آورد: apəma- «واپسین» = سنسکریت apamá-، upəma- «بالاترین»، fratəma- «نخستین» = سنسکریت prathamá-، nāuma- «نهم». صورتی که نورایی نوشته (-emô) همان حالت فاعلی مفرد مذکر -əmō است، درست همان‌گونه که مان آن را نقل کرده (frat-əmō، up-əmō، ap-əmō). کنت نیز برای پارسی باستان همین را تأیید می‌کند: «صفت برتر در fratara- و صفت عالی در fratama- دیده می‌شود». ادعای نورایی در این گره درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D9%80%D9%85\"],\n     \"ref_check\": [\n      {\"ref\": \"IEC:257\", \"status\": \"supports\",\n       \"note\": \"IEC p. 257 s.v. -amos: 'Av. frat-əmō, up-əmō \\\"foremost\\\"; ap-əmō \\\"last\\\"' — precisely the Avestan material and the shape '-əmō' that Nourai renders '-emô'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AVG\", \"where\": \"Jackson, Avesta Grammar §849, p. 233 (and §841, p. 232)\", \"stance\": \"supports\",\n       \"note\": \"§849: 'Av. apəma- \\\"last\\\" = Skt. apamá-; Av. upəma- \\\"highest\\\" = Skt. upamá-; Av. fratəma- \\\"first\\\" = Skt. prathamá- (Whitney §487h); Av. nāuma- \\\"ninth\\\" = Skt. navamá-.' §841: '-tara, -təma = Skt. -tara, -tama … used respectively in forming the comparative and superlative degree of adjectives, the latter also in the ordinals vīsąstəma-, satōtəma-.'\"},\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Grammar §on secondary comparison (KNT.txt line 2252)\", \"stance\": \"supports\",\n       \"note\": \"'Secondary comparison … was made in Aryan by the use of -tara- and -tama-, cf. Gk. -τερος -τατος, Lt. ex-terus and ex-timus. The comparative is seen in OP fratara- and adv. apataram, the superlative in fratama-. … the Skt. superlative prathamá-.'\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"-om «-ُم»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"The New Persian ordinal suffix ‑ُم -om continues Middle Persian -om, itself from Old Iranian *-ama- (Av. -əma-, OP fratama- 'first'); the Old Iranian short a in the closed final syllable gives MP/NP -om, as in MP dudīgar/NP دوم. Mann puts the Persian forms on the very page cited: 'Per. čahār-um \\\"4th\\\"; Kurd. čuvar-em, id.; Per. haft-um, Kurd. hewtem \\\"7th\\\"'. Platts–Ranking, Grammar of the Persian Language §50: 'The ordinals are formed from the cardinals by the addition of the suffix ـم, and to the ordinals so formed (with the exception of یکم \\\"first\\\") the suffix ـین -īn … may be optionally superadded', e.g. دوهین 'the second'. Nourai's three examples are the standard formations: دوّم dovvom (دو + ـم, with the doubling/epenthetic -vv- of the diphthong-final stem), چهارم čahārom, پنجم panjom. One caveat on the drawing: Persian continues the Old Persian/Old Iranian suffix, not the Avestan one; Avestan stands here, as generally in Nourai's charts, as proxy for Old Iranian.\",\n     \"derivation_fa\": \"پسوند ترتیبی «ـُم» در فارسی نو دنبالهٔ «om-» فارسی میانه است و آن نیز از ایرانی باستان *-ama- (اوستایی -əma-، پارسی باستان در fratama- «نخستین») می‌آید؛ «a» کوتاهِ هجای پایانی بسته در فارسی میانه و نو به «o» بدل شده است. مان همین صورت‌های فارسی را در همان صفحهٔ ۲۵۷ آورده: «فارسی čahār-um «چهارم»؛ کردی čuvar-em؛ فارسی haft-um «هفتم»؛ کردی hewtem». پلاتس در «دستور زبان فارسی» (بند ۵۰) می‌نویسد: «اعداد ترتیبی با افزودن پسوند ـم به اعداد اصلی ساخته می‌شوند» و می‌افزاید که به آن‌ها (جز «یکم») می‌توان پسوند «ـین» را نیز افزود (دومین، دوهین). سه نمونهٔ نورایی — دوّم، چهارم، پنجم — همگی ساخت‌های معیارند؛ تشدیدِ «دوّم» ثانوی و از برخورد پایانهٔ «دو» با پسوند است. تنها تذکر آنکه فارسی نو این پسوند را از پارسی باستان به ارث برده، نه از اوستایی؛ در نمودارهای نورایی اوستایی معمولاً جانشین «ایرانی باستان» است. ادعای نورایی در این گره درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D9%80%D9%85\"],\n     \"ref_check\": [\n      {\"ref\": \"IEC:257\", \"status\": \"supports\",\n       \"note\": \"IEC p. 257 s.v. -amos, last lines: 'Cf. also Faliscan max-omo \\\"Maximus\\\"; Per. čahār-um \\\"4th\\\"; Kurd. čuvar-em, id.; Per. haft-um, Kurd. hewtem \\\"7th\\\", etc.' Mann himself puts the Persian ordinal suffix under this heading.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"GPL\", \"where\": \"Platts & Ranking, Grammar of the Persian Language §50 (p. 48)\", \"stance\": \"supports\",\n       \"note\": \"'§50. The ordinals are formed from the cardinals by the addition of the suffix ـم and to the ordinals so formed (with the exception of یکم \\\"first\\\") the suffix ـین -īn, or (its contraction) ـی, may be optionally superadded'; §51 gives باب اول, روز دوم, دوهین روز.\"},\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian (KNT.txt line 2252)\", \"stance\": \"supports\",\n       \"note\": \"'the superlative in fratama-' — the Old Persian ancestor of the suffix, showing that Persian -om is inherited from the Old Iranian *-ama- and need not pass through Avestan.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Latin\", \"words\": \"-imus; inf-imus; post-omus; max-imus; min-imus\", \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"Latin -imus/-umus is the regular reflex of the superlative *-m̥mo-, seen in infimus (older infumus), primus, decimus/decumus, maximus, minimus. Four of the five forms are right: infimus 'lowest' (Ernout-Meillet: 'Infimus (anc. infumus): qui se trouve tout au bas … Lat. inferus, infimus répond évidemment à skr. adhamáḥ'), maximus 'greatest' (< *mag-samo-, Watkins s.v. meg-), minimus 'least' (< *minu-mo-, Watkins s.v. mei-2). The fifth, 'post-omus', is not a Latin word: the word is postumus 'last-born, latest' (Ernout-Meillet: 'postumus: qui vient le tout dernier … Le suffixe est le même que dans infimus, primus, decumus'; the spelling posthumus is a late folk-etymological association with humus 'ground'). Mann's page 257, which Nourai is copying, prints 'Lat. inf-imus, post-umus \\\"lowest; latest\\\"' — so the -omus is Nourai's own slip (perhaps contaminated by Mann's Faliscan 'max-omo'), and the gloss 'lowest' has been carried over from infimus, whereas postumus means 'last, latest'. I read the 300-dpi rendering of pdf page 153 (saved to data/verification/sources/refs/ocr/BOOK/153.png): the printed page really shows 'post-omus : lowest', so the extraction is faithful and the error is the book's. Note also that the glosses 'maximum' and 'minimum' given for max-imus and min-imus are the English derivatives, not translations ('greatest', 'least').\",\n     \"derivation_fa\": \"پسوند لاتینی -imus/-umus بازتاب منظم *-m̥mo- (صفت عالی) است و در infimus (کهن‌تر infumus)، primus، decimus/decumus، maximus و minimus دیده می‌شود. چهار صورت از پنج صورتِ این جعبه درست است: infimus «پست‌ترین» (ارنو-مه‌یه: «infimus، کهن infumus: آنکه در پایین‌ترین جای است … برابر است با adhamáḥ سنسکریت»)، maximus «بزرگ‌ترین» و minimus «کم‌ترین». اما «post-omus» واژه‌ای لاتینی نیست؛ صورت درست postumus «واپسین، پس‌زاد» است (ارنو-مه‌یه: «postumus: آنکه در آخر همه می‌آید … پسوند همان است که در infimus، primus، decumus»؛ املای posthumus ریشه‌شناسی عامیانه و آمیختن با humus «خاک» است). مان در همان ص ۲۵۷ «Lat. inf-imus, post-umus» چاپ کرده است؛ پس «post-omus» لغزش خودِ نورایی است (شاید زیر تأثیر «max-omo» فالیسکیِ مان)، و معنی «پست‌ترین» نیز از infimus به آن سرایت کرده، حال آنکه postumus «واپسین» است. تصویر ۳۰۰dpi صفحهٔ ۱۵۳ کتاب را دیدم: در چاپ کتاب هم «post-omus : lowest» آمده است؛ بنابراین خطای چاپ کتاب است نه خطای خوانش اسکن.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"post-omus : lowest\",\n     \"correct_form\": \"post-umus (Lat. postumus) 'last, last-born, latest'\",\n     \"sources\": [\"https://www.etymonline.com/word/maximum\"],\n     \"ref_check\": [\n      {\"ref\": \"IEC:257\", \"status\": \"partial\",\n       \"note\": \"IEC p. 257 s.v. -amos prints 'Lat. inf-imus, post-umus \\\"lowest; latest\\\"' — with -umus, and with two glosses distributed over the two words. Mann's page supports the suffix and four of Nourai's forms but not the shape 'post-omus' nor the gloss 'lowest' for it. Mann's max-omo is Faliscan, not Latin.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.vv. inferus/infimus and posterus 3° postumus\", \"stance\": \"supports\",\n       \"note\": \"'Infimus (anc. infumus), -a, -um: qui se trouve tout au bas. Forme refaite pour remplacer imus … Lat. inferus, infimus répond évidemment à skr. adhamáḥ (av. aδara-)'; 'postumus: qui vient le tout dernier … d'où la graphie posthumus due à un rapprochement fait avec humus, humare. Le suffixe est le même que dans infimus, primus, decumus.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.vv. meg- and mei-2\", \"stance\": \"supports\",\n       \"note\": \"'Suffixed (superlative) form *mag-samo- in Latin maximus, greatest: MAXIM, MAXIMUM'; 'further suffixed (superlative) form *minu-mo- in Latin minimus, least: MINIMUM' — the superlative suffix in exactly Nourai's two words.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"English\", \"words\": \"maximum, minimum\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Both are Latin neuter superlatives adopted whole into English as nouns: maximum (n., 1740, via French) from Latin maximus 'greatest', superlative of magnus; minimum (n., 1660s) from Latin minimus 'least', superlative supplied to parvus/minor. Watkins/AHD, Nourai's reference here, gives both under their lexical roots with the superlative suffix spelled out: meg- '…*mag-samo- in Latin maximus, greatest: MAXIM, MAXIMUM'; mei-2 '…*minu-mo- in Latin minimus, least: MINIMUM'. So the words are genuine English Latinisms and the -imus of the parent node is indeed the element they carry; strictly, though, their lexical roots are *meg- and *mei-, and only the suffix comes from this chart's root.\",\n     \"derivation_fa\": \"هر دو واژه صفت عالی خنثای لاتینی‌اند که یکجا و بدون تغییر وارد انگلیسی شده‌اند: maximum (نخستین کاربرد ۱۷۴۰ م.، از راه فرانسه) از maximus «بزرگ‌ترین»، صفت عالی magnus؛ و minimum (حدود ۱۶۶۰ م.) از minimus «کم‌ترین»، صفت عالی که برای parvus/minor به کار می‌رود. واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage — همان مرجعی که نورایی آورده — هر دو را با ذکر صریح پسوند صفت عالی می‌آورد: زیر meg- «صورت عالی *mag-samo- در maximus لاتینی» و زیر mei-2 «صورت عالی *minu-mo- در minimus لاتینی». پس این دو واژه وام‌واژه‌های عالمانهٔ انگلیسی‌اند و پسوند -imus را با خود آورده‌اند؛ البته ریشهٔ واژگانی‌شان *meg- و *mei- است و تنها پسوندشان از ریشهٔ این نمودار می‌آید. ادعای نورایی در این گره درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/maximum\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 (AHD_watkins1985.txt): under meg- 'Great' — '4. Suffixed (superlative) form *mag-samo- in Latin maximus, greatest: MAXIM, MAXIMUM'; under mei-2 'Small' — 'c. further suffixed (superlative) form *minu-mo- in Latin minimus, least: MINIMUM'. The index confirms 'MAXIMUM meg-' and 'MINIMUM mei-2'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. maximum (SKT.txt line 10918)\", \"stance\": \"supports\",\n       \"note\": \"'maximum, (L.) Neut. of maximus' — the direct Latin borrowing, exactly as charted.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.vv. maxim, maximal, major\", \"stance\": \"supports\",\n       \"note\": \"'maxim, n. … fr. ML. maxima (short for L. maxima sententia) … fem. of maximus, \\\"greatest\\\". See maximum.'; 'maximal … Formed with adj. suff. -al fr. L. maximus. See maximum.'; s.v. major: 'fr. L. major, \\\"greater\\\" … comparative of, and from the same base as, magnus, \\\"great\\\" … Cp. also maximum.'\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-153.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk153.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-153.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 153"
}
```


### [2026-09-05T20:46:24.396Z] TOOL RESULT

```
written
JSON OK
nodes verified: 13/13
node verdicts: {'disputed': 4, 'plausible': 2, 'confirmed': 5, 'transcription_suspect': 2}
root verdicts: {'plausible': 2}
ref checks: {'partial': 5, 'supports': 6, 'not_found': 1, 'contradicts': 2}
books consulted: {'partial': 8, 'supports': 13, 'silent': 2, 'contradicts': 6} | by book: {'BRT': 3, 'SYN': 3, 'SIN': 2, 'KLN': 2, 'LAT': 2, 'IEC': 2, 'SKT': 2, 'KNT': 2, 'PHD': 1, 'HUB': 1, 'NYB': 1, 'MON': 1, 'HRN': 1, 'ISS_alt_DKS': 1, 'FSD': 1, 'WLD': 1, 'AVG': 1, 'GPL': 1, 'AHD': 1}
```


## [2026-09-05T20:46:29.985Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c -i \"hingu\\|inku\\|ynkw\" ISS_alt_DKS.txt; grep -n -i \"hingu\" ISS_alt_DKS.txt | head -3"
}
```


### [2026-09-05T20:46:30.042Z] TOOL RESULT

```
1
337:amgusda- “аза fetida’, п 89:165; Sid. rovr, BS лілри-, Sid. тау} amgüsda-, Sid. 122r3 agüsda-, from "*angu-jatu- (BSOAS 20, 1957, 50-2), Tokhara B ariwas, Uigur ub pag, Chinese a-uei < á-ngjwei; iang-kuei < iang-g'jwi (K. 1-1; 13071; and К 210°1; 4571), see BSOAS 11-786, and E. Pulleyblank, AM, n.s., 9, 1962, 99 for the final -s, West Iranian Armen. lw. angousat, angšat, angousataber ‘ bear- ing silphium’, N.Pers. angudad, апдиййп, anguyün. From *angu-Jatu- with Jatu- ' gum, resin’, Pasto Zawla, O.Ind. jatu-, jatu-vara- (JRAS 1955, 17—18), N.Pers. šad ‘gum’, IE Pok. 480 g"et-, For the variation of Iranian angu- and O.Ind. hingu-, note also the O.Ind. andola- and hindola- ‘swing’. The plant belongs to the dry Iranian region.
```


## [2026-09-05T20:46:44.585Z] TOOL CALL #81: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json\np='data/verification/page-153.json'\nd=json.load(open(p,encoding='utf-8'))\ne0=d['entries'][0]\nnodes={n['id']:n for n in e0['nodes']}\n\nbailey={\"src\":\"ISS_alt_DKS\",\"where\":\"Bailey, Dictionary of Khotan Saka, s.v. aṃgūsda- (line 337)\",\n \"stance\":\"supports\",\n \"note\":\"'aṃgūsda- \\\"asa fetida\\\" … from *angu-jatu- (BSOAS 20, 1957, 50-2) … West Iranian Armen. lw. angousat, angšat …, N.Pers. angužad, angudān, angužān. From *angu-jatu- with jatu- \\\"gum, resin\\\", Pashto žawla, O.Ind. jatu- …, N.Pers. žad \\\"gum\\\" … For the variation of Iranian angu- and O.Ind. hingu-, note also the O.Ind. andola- and hindola- \\\"swing\\\". The plant belongs to the dry Iranian region.' Bailey thus makes hiṅgu the Indic counterpart of Iranian angu- 'resin', not of any bee-word.\"}\n\n# node 5: replace/append\nnodes[5]['consulted'].append(dict(bailey))\n# node 6: replace the silent ISS entry\nnodes[6]['consulted']=[c for c in nodes[6]['consulted'] if c['src']!='ISS_alt_DKS']\nb6=dict(bailey)\nb6['note']=(\"'aṃgūsda- \\\"asa fetida\\\" … from *angu-jatu- … N.Pers. angužad, angudān, angužān … \"\n \"For the variation of Iranian angu- and O.Ind. hingu-, note also the O.Ind. andola- and hindola- \\\"swing\\\". \"\n \"The plant belongs to the dry Iranian region.' Bailey's Khotanese aṃgūsda- is the sister formation to the \"\n \"word Sogdian borrowed back from Indic as inku, and confirms that this whole family is the Iranian angu- 'resin' word.\")\nnodes[6]['consulted'].append(b6)\n\njson.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)\nprint('ok')\nPYEOF\npython3 -m json.tool data/verification/page-153.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 153"
}
```


### [2026-09-05T20:46:46.613Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 13/13
node verdicts: {'disputed': 4, 'plausible': 2, 'confirmed': 5, 'transcription_suspect': 2}
root verdicts: {'plausible': 2}
ref checks: {'partial': 5, 'supports': 6, 'not_found': 1, 'contradicts': 2}
books consulted: {'partial': 8, 'supports': 15, 'silent': 1, 'contradicts': 6} | by book: {'BRT': 3, 'SYN': 3, 'SIN': 2, 'ISS_alt_DKS': 2, 'KLN': 2, 'LAT': 2, 'IEC': 2, 'SKT': 2, 'KNT': 2, 'PHD': 1, 'HUB': 1, 'NYB': 1, 'MON': 1, 'HRN': 1, 'FSD': 1, 'WLD': 1, 'AVG': 1, 'GPL': 1, 'AHD': 1}
```


## [2026-09-05T20:47:06.041Z] AGENT

Done — `data/verification/page-153.json` written; `verify_check.py 153` reports 13/13 nodes and **0 PROBLEM lines**.

**Page 153 (book p. 123) — 2 entries, 13 nodes**
- Node verdicts: confirmed 5, plausible 2, disputed 4, transcription_suspect 2. Root verdicts: plausible 2.
- Ref checks: supports 6, partial 5, contradicts 2, not_found 1. 19 books consulted (BRT, SYN, SIN, ISS/Bailey, KLN, LAT, IEC, SKT, KNT, PHD, HUB, NYB, MON, HRN, FSD, WLD, AVG, GPL, AHD); 8 web pages archived via fetch_source.py.

**disputed**
- *Embhi* #1 Avestan "ang, angu / angu-paēna": no such Avestan words. Bartholomae col. 817 and Buck 5.84 give only Av. *paēna-; the compound is Gharib's Old Iranian *angu-paina- (PIr *Hangubáynah = *Hángwr̥ "resin" + *báynah "bee").
- #4 Sogdian ʾnkwpyn: word genuine (SOD 1066) but it is the sister of MP angubēn, i.e. Iranian inheritance, not a branch of *embʰi-.
- #5 Sanskrit hingu: Laufer (Sino-Iranica 361) "an ancient loan from Iranian"; Bailey s.v. aṃgūsda- puts it with Iranian angu- "resin"; POK 311 has no Sanskrit at all.
- #7 Latin apis: Nourai's own ref, WLD I 125, says "np. ang 'Biene' und lat. apis 'Biene' (beide dunkel)"; Klein "of unknown etymology", Buck "etym.?", Ernout–Meillet "on ne saurait préciser", de Vaan/Wiktionary substrate.

**transcription_suspect** (both `error_in: "book"` — printed page checked at 300 dpi, copy at `data/verification/sources/refs/ocr/BOOK/153.png`)
- *Embhi* #9 Greek "ampis : honey" — no such Greek word; POK 311 prints Gk. ἐμπίς "a mosquito". Both form and gloss wrong in the book.
- *Ěmos* #3 Latin "post-omus : lowest" — the word is postumus "last, latest"; Mann IEC 257, Nourai's source, prints "post-umus".

**Notable**: the whole *Embhi* tree rests on Horn, Grundriss p. 254, an explicitly labelled *Vermutung* ("np. eng 'Biene' vielleicht dasselbe Wort wie lat. apis"), where Horn also concedes he cannot attest NP *eng* at all. Entry 1 (*Ěmos*) is the strong one: IEC 257 s.v. "-amos" carries every language Nourai charts, Persian čahār-um / haft-um included.

**Extraction (owner fix, minor)**: entry 1 node #2 `script_extra` is "دوّم ، چهارم ، پنجم"; the printed page shows the damma — "دوّم ، چهارُم ، پنجُم". Everything else matches the page exactly.
