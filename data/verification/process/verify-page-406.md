# Verification process log — verify-page-406


## [2026-09-14T00:53:09.871Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 406 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-406.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-406.json. Write /home/sfmqrb/git/rishe/data/verification/page-406.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 406` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:53:10.907Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T00:53:11.927Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:53:11.949Z] TOOL RESULT

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


## [2026-09-14T00:53:12.430Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-406.txt"
}
```


### [2026-09-14T00:53:12.448Z] TOOL RESULT

```
1	=== PDF page 406 (book page 376) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Pôu : small, young  (refs POK:842)
4	#1 (parent #0) [Avestan] refs=POK:842 | pu 1, pu-thra, puthra : son, child ; xšathra-puthra : son of king ☞Ksei ; bağa-puthra : son of God ☞Bhag ; a-puthra-tanu : having a child in body, pregnant ☞Ten 1
5	  #2 (parent #1) [Persian] refs=BQT; AEF:384 | pesar «پسر» : boy, son ; âbestan «آبستن» : "with a child in the body" | extra: پُس۲ ، پور ، پوره ، شاهپور ، فغپور
6	#3 (parent #0) [Old Persian] refs=TZF:13; MFL:102 | puča : son
7	#4 (parent #0) [Greek] refs=AHD | pais : child
8	  #5 (parent #4) [English] refs=None | pediatrics, encyclopedia
9	#6 (parent #0) [Latin] refs=AHD | parrum-affinis : with little similarity to other materials, referred to paraffin
10	  #7 (parent #6) [French] refs=None | paraffine
11	    #8 (parent #7) [Persian] refs=MON | pârâfîn «پارافین»
12	  #9 (parent #6) [English] refs=None | paraffin
13	#10 (parent #0) [Latin] refs=AHD | pau-per : with little, poor ; pu-llus : young, youngster
14	  #11 (parent #10) [English] refs=None | poor, poverty ; pony, pupil, puppet, puppy
15	#12 (parent #0) [Germanic] refs=AHD | fawaz : few, little
16	  #13 (parent #12) [English] refs=None | few
17	
```


## [2026-09-14T00:53:15.778Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-406.json",
 "description": "Show source JSON for page 406"
}
```


### [2026-09-14T00:53:15.833Z] TOOL RESULT

```
{
  "pdf_page": 406,
  "book_page": 376,
  "entries": [
    {
      "root": {
        "name": "Pôu",
        "lang": "Indo-European",
        "refs": "POK:842",
        "gloss": "small, young"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:842",
          "words": [
            {"translit": "pu 1, pu-thra, puthra", "gloss": "son, child", "script": null},
            {"translit": "xšathra-puthra", "gloss": "son of king", "script": null, "see": ["Ksei"]},
            {"translit": "bağa-puthra", "gloss": "son of God", "script": null, "see": ["Bhag"]},
            {"translit": "a-puthra-tanu", "gloss": "having a child in body, pregnant", "script": null, "see": ["Ten 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT; AEF:384",
          "words": [
            {"translit": "pesar", "gloss": "boy, son", "script": "پسر"},
            {"translit": "âbestan", "gloss": "\"with a child in the body\"", "script": "آبستن"}
          ],
          "script_extra": "پُس۲ ، پور ، پوره ، شاهپور ، فغپور",
          "note": null,
          "quote": {
            "text": "کدام شربت نوشید پورهٔ ادهم - که مست وار شد از ملک مملکت بیزار",
            "poet": "Molavî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "TZF:13; MFL:102",
          "words": [
            {"translit": "puča", "gloss": "son", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "pais", "gloss": "child", "script": null}
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
            {"translit": "pediatrics, encyclopedia", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "parrum-affinis", "gloss": "with little similarity to other materials, referred to paraffin", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "paraffine", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "pârâfîn", "gloss": null, "script": "پارافین"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "paraffin", "gloss": null, "script": null}
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
            {"translit": "pau-per", "gloss": "with little, poor", "script": null},
            {"translit": "pu-llus", "gloss": "young, youngster", "script": null}
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
            {"translit": "poor, poverty", "gloss": null, "script": null},
            {"translit": "pony, pupil, puppet, puppy", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "fawaz", "gloss": "few, little", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "few", "gloss": null, "script": null}
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


## [2026-09-14T00:53:17.850Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','BQT','AEF','TZF','MFL','MON','WLD','HRN','HUB','PHD','NYB','BRT','KNT','KLN','SKT','IEC','SYN','CHEUNG','ARY']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-14T00:53:18.937Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فار
MFL {"title": "I. M. Oranskij, Introduction to Iranian Philology (Persian translation by K. Keshavarz, Tehran 1979)", "edition_found": null, "kind": "archive_fragment", "url": "https://archive.org/details/galaxy_ub2007_yahoo_201511 (5-page image fragment of the Keshavarz translation only)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MFL/MFL_ia_ga
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
CHEUNG null
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root,
```


## [2026-09-14T00:53:55.927Z] TOOL CALL #5: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -60; echo ---; ls /home/sfmqrb/git/rishe/tools/"
}
```


### [2026-09-14T00:53:55.980Z] TOOL RESULT

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
---
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


## [2026-09-14T00:53:56.695Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T00:53:56.733Z] TOOL RESULT

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
```


## [2026-09-14T00:54:00.002Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"putlo\\|pōu-\\|pou-, p\\|pau-ro\\|pauper\\|pullus\" POK_full.txt | head -40"
}
```


### [2026-09-14T00:54:00.050Z] TOOL RESULT

```
66078:pullus 'sch\Narzgrau' (^/fromyinfolge of aniaut. p-; forms -no-); palumbes or -/5"wood-, 
66113:russ.-Church Slavic plesnt. Old Czech plesen' mildew ' and Church Slavic /0e/e5"pullus', 
66881:pauperes reshaped to proceres, -um 'die Vornehmsten; die from the wall herausragenden 
68858:t0/cr' arm' (as Latin pauper). Old High German fao, fo' little ', Dat. PI. fouuem. Old Saxon 
68862:2. With formants -Aro-/ Latin paucus' little ', pauper' arxx\' {*pauco-paros ox pau-paros?' 
68887:5. With Mormant: putra-rw., Avestan ap. pu^-ra-m. (latter from putlo-= Oscan puklo-) 
68893:pus{s)us, -a "knave, boy, girl', but pus/7/us 'very small' is Demin. from pullus {*putslo-lo-s)\
```


## [2026-09-14T00:54:00.880Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"842\" POK_full.txt | head -20; echo === ; grep -c . POK_full.txt"
}
```


### [2026-09-14T00:54:00.930Z] TOOL RESULT

```
6196:References: WP. I 47 ff., WH. I If., 842, Feist 3a, Trautmann 1 1 . 
68696:Page(s): 841-842 
68740:Page(s): 842 
68758:Page(s): 842 
68908:Page(s): 842-843 
71221:References: WP. II 322, WH. II 842, Specht KZ 66, 26 f., Indo Germanic Dekl. 239 f., 
(eval):1: == not found
```


## [2026-09-14T00:54:02.551Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '68840,68915p' POK_full.txt"
}
```


### [2026-09-14T00:54:02.615Z] TOOL RESULT

```
Balto-Slavic */Oo/oand *plid' drink ' in Old Prussian yoo/e///' trinkt', poOism. 'das Trinken', 
Old Church Slavic pi/'g, pifi' drink '; pirb m. 'Bankett', pivon. ' beverage, drink ', Czech etc. 
'beer'; Kaus. Old Church S\av'\c pq/'g, pq/it/ 'iranke'; Balto-Slavic *pdta- and *pTta- 
'getrunken' in Lithuanian puotai. 'Trinkgelage' and Old Church Slavic pitijb 'trinkbar'; 
Balto-Slavic *p^tiu\^6 *pTti\. 'das Trinken' in Old Prussian Inf. poOt{*pdti-) and slov. p?tt ' 
beverage, drink ' (Infin. *pitij\ Balto-Slavic * potu- m. 'das Trinken' in Old Prussian Inf. 
puton, poutonan6 poutwe/'dnnk', ablaut, passive russ. -Church Slavic yO/fe. 

References: WP. II 71 f., WH. I 103 f., Trautmann 228 f. 
Page(s): 839-840 

Root / lemma: pou- : pau- : pu- 

Meaning: small, little; young (of animals) 

Material: 1. With -o-suffix; Gothic fawaiP\. 'wenige'. Old Icelandic far' little, wortkarg', fa- 

t0/cr' arm' (as Latin pauper). Old High German fao, fo' little ', Dat. PI. fouuem. Old Saxon 

fa. Old English fea, PI. feawe, engl. /fen/ 'wenige'. 

2. With formants -Aro-/ Latin paucus' little ', pauper' arxx\' {*pauco-paros ox pau-paros?' 
little erwerbend, little sich constituting, originating '); Old High German fob' little '; 



Maybe alb. {*pauc-) pak' little' a Latin loanword. 

With suffix -/o-; Latin paul(l)us "small, little ' ( *pauks-lo-), pauxillus " totally little ' ( *pauk- 
s-lo-lo-). 

3. With formants -ro-zgr. iraOpot; "small, little', Latin with metathesis parvus^ smaW, 
parum ( *parvom) "to little '. 

4. " youngling, the young of an animal ': 

gr. iraOq (Attic Vasen), Gen. iraFot; (Cypriot, in addition ein new Nom. iraq), iraTt;, Gen. 
TTai56(; m. f., hom. JTd\c„ naFi5- "kid, child'; Latin puer^V\6, child, knave, boy, girl' ( *puuero- 
), puella "girl'; 

Gothic fula. Old Icelandic folixw., fylu. {*fulja-), under fyljai.. Old English fola. Old High 
German folo, fulT(n)^ plenitude, foals'; besides *pd[u]los\n Armenian i//"goat', am-ur 
infertile ' ( *n-pdlo-), yHi. "pregnanffZ-yOd/a/ya); gr. n(I)Ao(; "foals', also "young man, young 
girl', nwAiov "small foals, youngling ', alb. pele, pe/e'mare' (Fem. to *pdlos)\ perhaps med. 
Arbu-pales, if es " white foals possessing' stands for. 

5. With Mormant: putra-rw., Avestan ap. pu^-ra-m. (latter from putlo-= Oscan puklo-) 
"son, kid, child'; 

maybe alb. putra^'pa^ (of a young animal', puta^ so\e' 

gr. names as nu)-TaAo(;; Latin putus, put/7/us 'knave, boy', next to which *put-so-\n 
pus{s)us, -a "knave, boy, girl', but pus/7/us 'very small' is Demin. from pullus {*putslo-lo-s)\ 
Oscan puklo-'V\6, child' (= Old \v\6\c putra-), Paelignian puc/o/sDat PI. "pueris', mars. 
puc/es, Latin pu//us " young, the young of an animal ' ( *put-s-lo-)\ 

maybe alb. {*putillus) pu//sht' donkey's colt' 

Balto-Slavic *pufa'b\r6' in russ. -Church Slavic yOb/a "bird', yObZ/s/i. "small bird' ("bird' 
actually "young bird'), Lithuanian putyt/s'young animal, young bird' (Zartlichkeitsausdruck), 
Baltic *put-n-a-\n Latvian putns'b\r6'\ with other, demin. Formansverbindung Lithuanian 
yOaJ-/rs//s "bird'. 

maybe alb. pa/a "goose' Slavic loanword from russ. -Church Slavic yOb/a "bird' : Serbo- 
Croatian: pa'//ra"duck' [f]. 

References: WP. II 75 f., WH. II 259, 265 f., 382 f., 385 f., 394, Trautmann 233. 
Page(s): 842-843 



Root / lemma: prai- prai-, prT- (pri-) 
Meaning: to like, feel well-disposed, friendly 

Material: Old Indie pnnat/" pleases ', Med. "is cheerful about etwas', pnyateds., ' loves ',
```


## [2026-09-14T00:54:09.182Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"^pau-\\|pau-1\\|pau-2\\|putlo\\|encyclopedia\\|paraffin\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-14T00:54:09.222Z] TOOL RESULT

```
814:fana, flag, banner, weathercock: VANE; b. compound *gund-fanon-, “battle-flag” (see ghen-'). 2. Extended form *panno- in Latin pannus, piece of cloth, rag: PANE, PANEL. 3. Possibly Greek pénos, web (> Latin pdnus, a swelling): PANICLE. [Pok. pan- 788.] [pandoura. Three-stringed lute. Greek noun of obscure origin. BANDORE, MANDOLIN, PANDORE.] pant-. All. Attested only in Tocharian and Greek. Greek pas (neuter pan, stem pant-), all: PAN-, PAN; DIAPASON, PANCRATIUM, PANCREAS. [In Pok. 1. keu- 592.] pap-'. Teat (sound symbolism). Probably the same word as pap-2. 1. Middle English pap(pje, nipple: Pap}. 2. Latin diminutive papula, pimple (diminutive papilla, nipple): PAPILLA, PAPULE. 3. Variant form *pup(p)- in Latin piipus, boy, and pupa, girl: puPA, PUPIL. [In Pok. barb- 91.] pap-?. Food (baby-talk root). Reduplication of pa-. 1. Germanic nasalized form *pamp- in Flemish frequen- tative pamperen, to cram with food, akin to the source of Middle English pamperen, to pamper: PAMPER. 2. Latin pappa, food (> Middle English pap, soft food): PAP?, POPPYCOCK. [Pok. pap(p)a 789, ba*mb- 94.] papa. A child’s word for “father,” a linguistic near-uni- versal found in many languages. 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.] paso-. Kinsman by marriage. Latin parri- (for pari-) in compound parri-cida (oldest form paricidas), murderer of a near relation: PARRICIDE. [Pok. pdso-s 787.] past-. Solid, firm. 1. Germanic *fastuz, firm, fast, in: a. Old English fest, fixed, firm: FAST!; STEADFAST; b. Middle Dutch vast, firm, fast: AvAST. 2. Germanic *fastinon, to make firm or fast, in Old English festnian, to fasten, establish: FASTEN. 3. Germanic *fastén, to hold fast, observe abstinence, in: a. Old English festan, to abstain from food: rasT?; b. Old Norse fasta, to abstain from food: BREAKFAST. [Pok. pasto- 789.] pau-. Few, little. I. Adjectival form *pau-, few, little. 1. Germanic *fawaz in Old English féawe, few: FEW. 2. Suffixed form *pau-ko- in Latin paucus, little, few: PAUCITY, POCO. 3. Suffixed form *pau-ro- in metathetical form *par-wo- in Latin parvus, little, small, neuter parvum, becoming parum, little, rarely: PARAFFIN, PAR- vovirus. 4. Compound “pau-paros, producing little, poor (*par-os, producing; see pere-'), in Latin pauper, poor: PAUPER, POOR, POVERTY. II. Suffixed reduced variant form “pu-lo-, young of an animal. 1. Germanic *fulén- in Old English fola, young horse, colt: FOAL. 2. Germanic derivative *fuljé in Old Norse fylja, female colt: FILLY. 3. Latin pullus (probably with expressive gemination), young of an animal, chicken: POLTROON, PONY, POOL?, POULARD, PULLET; CATCHPOLE. III. Basic form *pau- and variant form *pi-, boy, child. 1. Suffixed form *pu-ero- in Latin puer, child: PUERILE, PUERPERAL. 2. Suffixed form “pi-sso- in Latin piisus, boy: PUSIL- LANIMOUS. 3. Suffixed form *paw-id- in Greek pais (stem paid-), child (> paideia, education): PEDO-?; ENCY- CLOPEDIA, ORTHOPEDICS. [Pok. pdu- 842.] paus-. To leave, desert, cease, stop. Greek pauein, to stop (> Latin pausa, a stopping): PAUSE, (PESADE), (POSE!); COMPOSE, DIAPAUSE, (REPOSE!). [Pok. paus- 79.] ped-'. Foot. I. Nominal root. 1. Lengthened o-grade form *pod- in Germanic *fot- in Old English fot, foot: Foor. 2. Suffixed form *ped-ero- in Germanic *feteré in Old English fetor, feter, leg iron, fetter: FETTER. 3. Suffixed form *ped-el- in Germanic *fetel- in Old High German vizzelach, fetlock, akin to the Germanic source of Middle English fitlock, fetlock, fetlock: FETLOCK. 4. Basic form *ped- in Latin pés (stem ped-), foot: PAWN2, -PED, PEDAL, PEDATE, PEDESTRIAN, PEDI-, PEDICEL, PEDUNCLE, (PEON), PES, PIONEER; MILLIPEDE, SESQUIPEDALIAN, TRIPEDAL, TRIVET, VAMP!. 5, Form *ped-yo- in: a. Latin expedire, to free from a snare (ex-, out of; see eghs): EXPEDITE; b. Latin impedire, “to put in fetters, hobble,
1456:ENAMEL mel-1 ENAMOR amma ENANTIOMER §ant- ENANTIOMORPH ant- ENARTHROSIS at- ENATE gene- ENCAUSTIC kéu- ENCEINTE? kenk-1 ENCEPHALO- ghebh-el- ENCHANT kan- ENCHASE kap- ENCHIRIDION ghesor- ENCLAVE kleu-3 ENCLITIC klei- ENCOUNTER kom ENCROACH ger-2 ENCYCLICAL kwel-1 ENCYCLOPEDIA pau- END ant- ENDEAVOR ghabh- ENDEMIC da- ENDERGONIC werg- ENDOCARDIUM kerd-1 ENDOCRINE krei- ENDOERGIC werg- ENDORSE dorsum ENDOSTEUM ost- ENDOTHECIUM dhé-1 ENDOTHELIUM dhé@(i)- ENDOW do- ENDUE deuk-, eu-1 ENDURE deru ENEMA yé-
2059:-PARA pere-1 PARABLE gWelg-1 PARABOLA gW¥ele-1 PARACHUTE pere-1 PARACLETE kele-2 PARADE pere-1 PARADIGM deik- PARADISE dheigh-, pert PARADOX dek-! PARAFFIN pau- PARAGRAPH gerbh- PARALLAX al-1 PARALLEL al-1 PARALLELEPIPED ped-! PARALOGISM leg-1 PARALYSIS leu PARAMECIUM mak- PARAMOUNT ad-, per! PARAMOUR amma, pert PARANOIA nous PARAPET peg- PARAPHERNALIA bher-1 PARAPHRASE gWhren- PARAPLEGIA plak-2 PARASOL pere-1, sawel- PARATAXIS tag- PARBOIL beu-! PARCAE pera-1 PARCEL pere-2 PARCENER pere-2 PARDON d6-
```


## [2026-09-14T00:54:09.898Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"pauper\\|pullus\\|puer\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-14T00:54:09.963Z] TOOL RESULT

```
814:fana, flag, banner, weathercock: VANE; b. compound *gund-fanon-, “battle-flag” (see ghen-'). 2. Extended form *panno- in Latin pannus, piece of cloth, rag: PANE, PANEL. 3. Possibly Greek pénos, web (> Latin pdnus, a swelling): PANICLE. [Pok. pan- 788.] [pandoura. Three-stringed lute. Greek noun of obscure origin. BANDORE, MANDOLIN, PANDORE.] pant-. All. Attested only in Tocharian and Greek. Greek pas (neuter pan, stem pant-), all: PAN-, PAN; DIAPASON, PANCRATIUM, PANCREAS. [In Pok. 1. keu- 592.] pap-'. Teat (sound symbolism). Probably the same word as pap-2. 1. Middle English pap(pje, nipple: Pap}. 2. Latin diminutive papula, pimple (diminutive papilla, nipple): PAPILLA, PAPULE. 3. Variant form *pup(p)- in Latin piipus, boy, and pupa, girl: puPA, PUPIL. [In Pok. barb- 91.] pap-?. Food (baby-talk root). Reduplication of pa-. 1. Germanic nasalized form *pamp- in Flemish frequen- tative pamperen, to cram with food, akin to the source of Middle English pamperen, to pamper: PAMPER. 2. Latin pappa, food (> Middle English pap, soft food): PAP?, POPPYCOCK. [Pok. pap(p)a 789, ba*mb- 94.] papa. A child’s word for “father,” a linguistic near-uni- versal found in many languages. 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.] paso-. Kinsman by marriage. Latin parri- (for pari-) in compound parri-cida (oldest form paricidas), murderer of a near relation: PARRICIDE. [Pok. pdso-s 787.] past-. Solid, firm. 1. Germanic *fastuz, firm, fast, in: a. Old English fest, fixed, firm: FAST!; STEADFAST; b. Middle Dutch vast, firm, fast: AvAST. 2. Germanic *fastinon, to make firm or fast, in Old English festnian, to fasten, establish: FASTEN. 3. Germanic *fastén, to hold fast, observe abstinence, in: a. Old English festan, to abstain from food: rasT?; b. Old Norse fasta, to abstain from food: BREAKFAST. [Pok. pasto- 789.] pau-. Few, little. I. Adjectival form *pau-, few, little. 1. Germanic *fawaz in Old English féawe, few: FEW. 2. Suffixed form *pau-ko- in Latin paucus, little, few: PAUCITY, POCO. 3. Suffixed form *pau-ro- in metathetical form *par-wo- in Latin parvus, little, small, neuter parvum, becoming parum, little, rarely: PARAFFIN, PAR- vovirus. 4. Compound “pau-paros, producing little, poor (*par-os, producing; see pere-'), in Latin pauper, poor: PAUPER, POOR, POVERTY. II. Suffixed reduced variant form “pu-lo-, young of an animal. 1. Germanic *fulén- in Old English fola, young horse, colt: FOAL. 2. Germanic derivative *fuljé in Old Norse fylja, female colt: FILLY. 3. Latin pullus (probably with expressive gemination), young of an animal, chicken: POLTROON, PONY, POOL?, POULARD, PULLET; CATCHPOLE. III. Basic form *pau- and variant form *pi-, boy, child. 1. Suffixed form *pu-ero- in Latin puer, child: PUERILE, PUERPERAL. 2. Suffixed form “pi-sso- in Latin piisus, boy: PUSIL- LANIMOUS. 3. Suffixed form *paw-id- in Greek pais (stem paid-), child (> paideia, education): PEDO-?; ENCY- CLOPEDIA, ORTHOPEDICS. [Pok. pdu- 842.] paus-. To leave, desert, cease, stop. Greek pauein, to stop (> Latin pausa, a stopping): PAUSE, (PESADE), (POSE!); COMPOSE, DIAPAUSE, (REPOSE!). [Pok. paus- 79.] ped-'. Foot. I. Nominal root. 1. Lengthened o-grade form *pod- in Germanic *fot- in Old English fot, foot: Foor. 2. Suffixed form *ped-ero- in Germanic *feteré in Old English fetor, feter, leg iron, fetter: FETTER. 3. Suffixed form *ped-el- in Germanic *fetel- in Old High German vizzelach, fetlock, akin to the Germanic source of Middle English fitlock, fetlock, fetlock: FETLOCK. 4. Basic form *ped- in Latin pés (stem ped-), foot: PAWN2, -PED, PEDAL, PEDATE, PEDESTRIAN, PEDI-, PEDICEL, PEDUNCLE, (PEON), PES, PIONEER; MILLIPEDE, SESQUIPEDALIAN, TRIPEDAL, TRIVET, VAMP!. 5, Form *ped-yo- in: a. Latin expedire, to free from a snare (ex-, out of; see eghs): EXPEDITE; b. Latin impedire, “to put in fetters, hobble,
995:spit!. 2. Germanic *speiw- in Old English spiwan, spio- wan, to spew: SPEW. 3. Germanic *spait- in Old English spatl, spittle: sPITTLE. 4. Germanic *spiit- in: a. Middle English spouten, to spout forth: spout; b. Dutch sputte- ren, to sputter, akin to the probable Low German source of SPUTTER. 5. Zero-grade form *spu- in Latin spuere, to spit: SPUTUM; CUSPIDOR. 6. Zero-grade form *(s)pyu- in Greek ptuein, to spit: HEMOPTYSIS, PTYALIN. [Pok. (s)p(hjieu- 999.] srebh-. To suck, absorb. Zero-grade form *srbh- in: a. Germanic *surp- in altered form in Dutch slurpen, to slurp, lap: SLURP; b. suffixed form *srbh-é- in Latin sorbére, to suck: ABSORB, ADSORB, RESORB. [Pok. srebh- 1001.] srenk-. To snore. O-grade form *sronk- in: a. Greek rhonkos, rhonkhos, a snoring: RHONCHUS; b. Greek rhunkhos, snout, bill, beak: RHYNCHOCEPHALIAN. [Pok. srenk- 1002.] sreu-. To flow. 1. Suffixed o-grade form *srou-mo- in Germanic *straumaz, stream, in: a. Old English stréam, stream: STREAM; b. Dutch stroom, stream: MAELSTROM. 2. Basic form *sreu- in: a. Greek rhein, to flow: RHEO-, -RRHEA; CATARRH, DIARRHEA, HEMORRHOID, RHYOLITE; b. suffixed form *sreu-mn in Greek rheuma, stream, humor of the body: RHEUM. 3. Suffixed zero-grade form *sru-dhmo- in Greek rhuthmos, measure, recurring mo- tion, rhythm: RHYME, RHYTHM. [Pok. sreu- 1003.]
2065:Pass pete- PASSIBLE pé@{(i)- PASSIM pete- PASSION pé@{i)- PASSIVE pé@(i)- PASTILLE pa- PASTOR pa- PASTURE pa- PATEN pete- PATENT pete- PATER peter- PATERNAL peter- PATERNOSTER nes-2 PATH pent- PATHETIC kWent(h)- PATHO- kWent(h)- PATHOGNOMIC gné- PATHOGNOMONIC kWent(h)- PATHOS kWent(h)- -PATHY kWent(h)- PATIENT pé@(i)- PATINA! pete- PATINA? pete- PATRI- peter- PATRIARCH peter- PATRICIAN peter- PATRICLINOUS _ klei- PATRIMONY peter- PATRIOT peter- PATRON peter- _ PATRONYMIC nO-men- PATULOUS  pete- PAUCITY pau- PAUPER pau- PAUSE paus- PAVE peu-
2139:PROVE per! PROVENANCE gWa- PROVENDER ghabh- PROVENIENCE gWa- PROVERB wer-& PROVIDE weid- PROVOKE wekw- PROVOST apo- PROW per! PROXIMATE per! PROXY cira PRUINOSE preus- PRUNE? ret- PRURIENT preus- PRURIGO preus- PRURITUS preus- PRY? ghend- PSALM pdl- PSALTERY pol- PSEPHOLOGY bhes-1 PSEUDEPIGRAPHA gerbh- PSEUDOMONAD _men-4 PSEUDONYM n0-men- PSILOMELANE bhes-!, mel-2 PSYCHE bhes-2 PSYCHEDELIC deiw- PSYCHIC bhes-2 PSYCHO- bhes-2 PSYLLA plou- -PTER pet- PTERIDOLOGY pet- PTEROCERCOID pet- PTERYGOID pet- PTISAN pelis-1 PTOMAINE pet- PTOSIS pet- PTYALIN spyeu- PUBERTY pubés PUBERULENT piibés PUBESCENT pubés PUBIC plibés PUBIS plbés PUBLIC populus PUCE plou- PUCKER beu-! PUDENCY (s)peud- PUDENDUM (s)peud- PUEBLO populus PUERILE pau- PUERPERAL pau- PUFF beu-!
```


## [2026-09-14T00:54:19.903Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -o \"PUPPET [a-z0-9é@!?ö-]*\\|PUPPY [a-z0-9é@!?-]*\\|PUPIL [a-z0-9é@!?-]*\\|PONY [a-z0-9é@!?-]*\\|PUPA [a-z0-9é@!?-]*\\|POOR [a-z0-9é@!?-]*\\|POVERTY [a-z0-9é@!?-]*\\|FEW [a-z0-9é@!?-]*\" AHD_watkins1985.txt | sort -u | head -20"
}
```


### [2026-09-14T00:54:19.948Z] TOOL RESULT

```
FEW bheug-!
FEW pau-
PONY pau-
POOR pau-
POOR spere-
POVERTY pau-
PUPA pap-!
```


## [2026-09-14T00:54:21.592Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"puθra\\|pu\\^ra\\|puthra\" BRT.txt | head -20; echo \"=== KNT\"; grep -n \"puça\\|pu.a-.*son\\|puqa\" KNT.txt | head -20"
}
```


### [2026-09-14T00:54:21.657Z] TOOL RESULT

```
7150:—  "^rö  ah'  m-  Y.  22.4;  —  ->rasca  ah' m'  Y.  i. 4,  Vr.  IS. 3,  S.  1.  7,  F. 39'  —  ''^räca ah'  m'  Y.  5Ä4;  —  'iar^  (Vok.)  ah'  m'  ■ Y.5Ä7;  —  'iar/  (Nom.)  mazda  'rahti Y.62.7,  9,  Yt. /0.3,  19.47-49^  V.<?,8o, Ny.5.4;  s.  noch  2.  ß)  'lan  (Vok.j ahurahe  mazda  pu^ra  Y. 65. 12;  —  düyA ms  'tars  (dXsVok.)  pü>ra  ah'  m'  Y.62.4;! 2;  ��  afrinlmi  tava  °tars  puitra  ah'  m° Y.O'-J.ii  4.23,  22.26,  Ny,  j.4;  —  xsha-\ maine  tava  '"^rö  ah'  m°  pu^ra  Y.3.Z;. /.  12,    22.3,    26,  Ny.5.4-6^   S.  i.9;  — |
11009:vas?iS  (^ur^masdähe^  mana^a  dä- fD.4.2.  B)imAwr.;  i)die Glieder  sind  nominal'';  a)  sie  folgen  sich unmittelbar:  pita  pu%rasea  .  .  iatarasüi ^■9-5i  —  pu^ra  (ND,)  ..  urvSxsayB k»r>s3spauaY.g.\a\  —  tum  akB  vahistasca ahi  YtJO.  29;  —  kanta  aiwyäxstaca Y.57.  IS  (s.  dagegen  Yt.;o.  103,  Sp.  567  u.);
14796:•  j,  'paeman-  Adj.,  nur  fem.  'mat/iT- 'säugend',  von  der  HUndio;  gatwqm  , . pu^raca  (sd)  'mainiea  V./5.  49.
15350:"..der  du  vom  vergänglichen  Leben  zum  ehedem*:  /rarasayS  .  .  yl  araca  'ra unvergänglichen  Leben  herüberkamst"  \.  /raoirisisiä  fsA.)  ya^ra  ..  VtJj.2S;  — 7.  52.  A)  Kaus.  'vorwärts  und  hinüber-   ij  nJtriJkqm  yam  apu^ram  .  .  anasaxtqm
25667:•  j.  urväxäaya-  m.  EN.  eines  Gläubigen, Sohns  des  &rita:  yai  kl  (näml.  %ritahe) pu^ra  us.taysihe  *yS  kmsäspasca  IkaiiS anyö  dätS.rätS  äai  anyS . .  ". .  zwei  Söhne . .  U.  und  K.,  ein  Richter  der  erstere, ein  Gesetzgeber,  aber.."  Y.i?.  10;  —  yat kama  nijaiäiii  az?m  {vä.(al.  hntäspB)  irä- 'hrS  "'saya'^  yai  janäni  hitäsp>m  "..dass ich  als  Rächer  meines  Binders  U.  heim- kehre, dass  ich  den  H.  töte"  Ytr5. 38; —  hubar)k?m  *vyäxan>m  bavähi  yaha "'saÄe''!  Az.  _J,
30620:Substantiv;  substantivisch:  h'  vlard  (sd.)  yi  nairya  yä- pu^rahe . .  yA  lanu.p^n'haAe ahurö  Y.  29. 4 ;  —  Syä  Hstl  (sd  )  .■  h'  *ptl  . .  *ajayaurva  *aya  ratufris  ". .  sui  ipsius  . . asakyä    mazdh    Y.4-.3;  44.2,  ^1.8;    —   uxoris  . .  filü  . ."  N.54.  U)  schwach-
=== KNT
423:xsdyabiya : dahytiném : Vistaspahyà : Dérayavahaus : z5ayattyahyà : puça : Haxámanisya : puça : Haxdémanisiya : hya : imam : lacaram : akunaus
623:b. Sometimes in other genitives standing before the nouns on which they depend: UvaxStrahyd taumayd DB 4.19, 422, eJ, g.9f (but -hyä DB 2.15f, 2.81); Nabunaitahyd puça DB 3.81, 4.14, 430, d.5f, 17 (but -hyä DB 1.79); Halditahyá puga DB 3.79; or with which they agree: Aurahyd Mazdáha ХРе 10 (cf. $44); harwahydya bumiya DSb 8f (but probably -yüyà DSf 16, 18).
779:рщй A'Hb, for puça (after парӣ, acc. to Brd. 1
922:*pullo-, OP puça, Skt. putrá-, Osc. puclo-.
1086:§78. PAR. tr, from pIE {г and й, became (ex- cept after a spirant, $79) plr. 6r, which per- sisted in Av. and in Med., but became a sibilant in OP; it is transcribed by ¢, and apparently was a sound intermediate between pure dental s and palatal $. Examples: pIE *puélo-, OP puça- ‘son’, Av. puéra-, Skt.
3048:S909. Тнк POSITION or THE GENITIVE. A geni- tive used as a genitive (not in a dative use), and depending upon a noun or adjective, precedes that noun or adjective, unless the genitive 18 attached to its noun by the article, in which instance it fol- lows: DB 1.4 mana pitä ‘my father’, but DB 2.27 kara hya тапа ‘my army’. The exception is only seeming in DB 1.9f VIII manā taumáyà tyaty paruam zšāyaðiyā аһа ‘eight (there were) of our family, who were kings before’; for amézam tau- туӣ is an appositive, equal to ‘(members) of our family’, cf. DB 1.28 Kabüjiya пата Kiraus puça amüxam taumdya ‘Cambyses by name, a son of Cyrus, (а member) of our family".
3130:cession of genitives from ‘B’ to ‘D’ would hardly be intelligible; therefore the appositive puça ‘son’ is always in the nominative, as are other embar- rassing appositives (cf. §257, §312).
3133:Агатай... Dāraywaušahyā X Shyà puça Daraya- vaušahyā Artaxsagahya XShyà puça Artaxšaçahyű XSayarcahya XShyà puça Xšayäreahyä Dāraya- vaušahyā XŠhyā puça D{éralyavausahya Vš- láspahya puça Haxamán?siya! In this the first phrase of parentage is grammatically correct; in the second, the gen. DarayavauSahyd is repeated аз a basis for clarity, and the appositive puça is in the nom. (see above), with proper depending
3137:II. The inscriptions A’Sb, A’Sd, A?Hb, AsH, А?Ра have a different scheme, in which the nomi- native of the royal name replaces the genitive. Only А?Ра is truly cogent, for the others have only these slightly varying versions of ‘son of Darius the King’: A'Sb Ddrayavaus Хбуй puça, A'Sd Darayavaus XSühyà риса, АЎНЬ Darayavaus X Š puçã; and ‘son of Ariaramnes the King’, in AsH Ariyüramna xsdyatiyahya риса. But A*Pa has a full lineage from Artaxerxes ITI back to Arsames, and uses the nominative for all royal names except for Hystaspes, also replacing the genitive of ‘king’ by nom. хёауабйуа, like X. S in АНЬ. Apparently OP had by this time become virtually а dead language employed only in writing ceremonial official records, its spoken form having suffered a wearing down of the endings (seen very clearly in Pahlavi). With the loss of the genitive ending it was natural to employ the nominative as a gen- eral case, as it had already been thus used in appositions. The gen. V*Slaspahyà probably per- sisted beeause in the earlier inscriptions available to the scribes of Artaxerxes I and later the name of Hystaspes occurred much more frequently in the genitive than in the nominative, and the scribes therefore used the familiar form in the in- seriptions whieh they composed.
3451:CMb = Cyrus, Мовонав в. 1 Kūruš : xSdyabiya : vazraka : Kabijiya 2 hyd : zšāyaðiyahyā : puça : Hazdmani siya : З айу : уада... 4... ... akutà ...
3484:28 dyabiya : араат : Kabiijiya : nima : Küraus : puça : amáxam : taumáy
3489:38 уй : XIV : тапса : Sakata : dha : yadiy : udapatatà ; hauv : kérahya : avaflü 39 : adurujiya : adam : Bardiya : amiy : һуа : Kürau$ : puça : Kabijiyahya : br
3527:72 iya : ima : tya : adam : akunavam : pasiiva : уай : xSayabiya : abavam ‚ 73 : Dürayavaus : xSdyabiya : уа : adam : Gaumatam : tyam : magum : avüjanam : ра 74 sīva : I martiya : Agina : пата : Upadarmahya : puça : hauv : udapatalá : Uujai 75 y : kàrahyà ; ava : afaha : adam : Üvjaiy : xiiiyasiya : amiy : pasdva : Uv 76 пуй: hamigiya : ауа :abiy : avam : Aginam : aSiyava : hauv : xšđyaðiya . TI :abava : Üvjaiy : uti : I martiya : Babiruviya : Naditabaira : патол : Ainatrahy
3529:78 à : puça : hauv : udapatatà : Babirauv : káram : ауада : adurujiya : adam : Nab 79 uk"dracara : amiy : hya : Nabunaitahy& : риса : pasava : kära : һуа : Babiruviya 80 : hamva : ably : avam : Naditabairam : aSiyava : Babirus : hamigiya : abava : x
3709:25 : ааһа : adam : Bardiya : amiy : hya : Kūrauš : puça : pas&va
3755:77 yasiya : yàtà : adam : Parsaiy : u(t)à : Madaiy : àham : рабу : duvitiyam : j 78 Babiruviya : hamiçiyā : abava : hacàma : I martiya : Атха : nàma : Armini 79 ya : Halditahya : puça : hauv : udapatata : Babirauv : Dubála : пата : dahy&
3758:81 racara : amiy : hya : Nabunaitahya : puça : pasàva : kara : Bübiruviya : hacáma : Һа 82 migiya : abava : abiy : avam : Arxam : aSiyava : Babirum : hauv : agarbayat
3817:1 :98tiy : Darayavaus : xsayaüiya : ima : t 2 ya:manà :kartam': Babireuv — :98ty : D З árayavaus : xSàyaftya : ima : tya : adam : akuna 4 vam : vasnà : Autamazdiha : һашаһуйуй : баг 5 da : pasáva : yada : xšāyaðiya : abavam : ХІХ : hamaran 6 Я : akunavam : vasnd : Auramazdiha : adamšim : а Т janam : uta : IX : x&ayatty& : agarbiyam : 1 Gaumata : 8 n&ma : magus : aha : hau : adurujiya : ava : абаһа : adam : 9 Bardiya : amiy : hya : Küraus : puça : hauv : Parsam : ha 3 10 migiyam : akunaus : Z Acina : пата : Uvjiya : hauv : adu 11 rujiya : ауаба : afaha : adam : xSiyaliya : amiy : Uvjaiy 12 : hauv : Üvjam : hamigiyam : akunaus : manā : I Naditabaira : n 13 dma : Babiruviya : hauv : adurujiya : avafá : aGaha : 14 adam : Nabukudracara : amiy : hya : Nabunaitahya : puga : 15 hauv : Babirum : hamigiyain : akunaus : I Martiya : na 16 ma : Pársa : hauv : adurujiya : атаба : ađaha : adam : Imani 17 š : amiy : Uvjaiy : cSayasiya : hauv : Üvjam : hamiciya 18 m : akunaus : I Fravarti$ : пата : Mada : hauv : adurujiya 19 : ауада : абаћа : adam : XSa@rita : amiy : UvaxStrahya : taumay 20 à : hauv : Madam : hamiciyam : akunaus : I Cigataxma : пата : Asa 21 gartiya : hauv : adurujiya : ava : afaha : adam : xšāyað 22 iya : amiy : Asagariaiy : UvaxStrahya : taumāyā : hauv 23 : Asagartam : hamigiyam : akunauS : І Frida : nama : 24 Margava : liauv : adurujiya : ааба : ađaha : adam :
3824:28 raus : puça : haw : Pürsam : hamiciyam : akunauS : I Ar
3826:30 ukudracara : amiy : hya : Nabunaitahya : puça : hauv : Babirum : ham 3l iciyam :akunauS : йу : Dürayavaus : xsàyatiya 2 imaiy :
```


## [2026-09-14T00:54:30.315Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KNT lexicon puça\"; grep -n \"puça-\\b\\|puça- 'son'\\|puça-, n\" KNT.txt | head; echo \"=== KNT around 4400-4600 lexicon\"; grep -n \"^.\\{0,40\\}puça\" KNT.txt | sed -n '1,40p'"
}
```


### [2026-09-14T00:54:31.475Z] TOOL RESULT

```
=== KNT lexicon puça
=== KNT around 4400-4600 lexicon
779:рщй A'Hb, for puça (after парӣ, acc. to Brd. 1
922:*pullo-, OP puça, Skt. putrá-, Osc. puclo-.
3133:Агатай... Dāraywaušahyā X Shyà puça Daraya- vaušahyā Artaxsagahya XShyà puça Artaxšaçahyű XSayarcahya XShyà puça Xšayäreahyä Dāraya- vaušahyā XŠhyā puça D{éralyavausahya Vš- láspahya puça Haxamán?siya! In this the first phrase of parentage is grammatically correct; in the second, the gen. DarayavauSahyd is repeated аз a basis for clarity, and the appositive puça is in the nom. (see above), with proper depending
3529:78 à : puça : hauv : udapatatà : Babirauv : káram : ауада : adurujiya : adam : Nab 79 uk"dracara : amiy : hya : Nabunaitahy& : риса : pasava : kära : һуа : Babiruviya 80 : hamva : ably : avam : Naditabairam : aSiyava : Babirus : hamigiya : abava : x
3758:81 racara : amiy : hya : Nabunaitahya : puça : pasàva : kara : Bübiruviya : hacáma : Һа 82 migiya : abava : abiy : avam : Arxam : aSiyava : Babirum : hauv : agarbayat
3824:28 raus : puça : haw : Pürsam : hamiciyam : akunauS : I Ar
3877:86 Ardumanis : nàma : Vahaukahyà : puça : Pársa, „ 87 iya : tuvam : kā : xSdyafiya : һуа : aparam :  Bhy^: Буйло : imaigim : martiyind : àtiy : Dürayavaus : xšāyaðiya : vaSnà : Au i(mà)m : dipim : aniyaðă : adam : akunavam : раат : ariya : aha : utd : av ast
4092:2 :dahyüvnàüm : Vistàspahy& : puça
4206:2 ahyáyà BUyà Vistaspahya : puça : Бахатал уа ba
4425:20 à : puça : Haxamanisiya TRANSLATION OF DE:
4430:2 üvnàm : Vistispahya : puça : Haxāmanišiya :
4468:20 àyaliyahyà : puça : Нах
4497:4 iyahy& : puça : Haxàmanisiya :
4566:1l ру: Dàrayavahaus : xšāyaðiyahyā : puça
4689:3 yavaudahyd : XShyà : puça : Dérayavausahya : Vi Stáspahya : puça : Haxamünesiya : imam : apadina : Dàrayavaus$ : apantyikama : ak
4777:9 aspahya : puça : Нах:
4789:9 spahy& : puça : Нах
5691:puça- sb. ‘son’: Av. puéra-, Ars. РЬ. рим, N Pers. pus, Skt. pulrá-, Ose. puclo-, рї *putlo- ($64, §75.1,§78,§148.1II). pucansm. AmH 3; AsH 4; CMb 2°; DB 1.8, 28, 39, 53, 74, 78, 79; 2.9; 3.25, 79, 81; 4.9, 14, 28, 30, 83, 84° bis, 85 bis, 86; DBa 3; DBb 6; DBd 6; DBh 7; DBi 8f; DPa 5; DPb; DPe 5; DPh 2; DNa 18, 14; DSa 2; DSb 10; DSe; DSd 2; DSe 12, 13; DSf 7; DSg 2°; DSi 2°; DS} 2°; DSk 3; DSm 2°; DSy 3; DZb 5f; DZec 6; DE 20; DH 2; XPa 10; XPb 20; XPe 9; XPd 14; XPe 4; XPf 14; XPh 11, 12; XPj; XPk; Х5е 2; XE 20; XV 15; A!Pa 15f; АЧ bis; D'Sb 2°; Аба 1, 2 bis, 3 bis; Ab; A?Sc 0° bis; А4 2; A?Ha 2°, 8, 3°, 4, 4°; А?Не 10, 11, 12, 13f, 15; A3Pa 18, 14, 15, 16, 18, 19, 20; Wa 7; Wb 8; We 9; Wd 9; Sa 8°, pucä npm. XPf 28; as nsm. А?НЬ (853; with -a after парӣ, acc. to Brd. WZKM 39.92).
```


## [2026-09-14T00:54:32.137Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD pus/puhr\"; grep -n -i \"pus\\b\\|pusar\\|puhr\\|pūhr\" PHD.txt | head -20; echo \"=== PHD abus\"; grep -n -i \"ābus\\|abus\\|apustan\\|ābistan\" PHD.txt | head"
}
```


### [2026-09-14T00:54:32.203Z] TOOL RESULT

```
=== PHD pus/puhr
213:a-pus II ārzūģ
214:a-pus [' BRE] without a son, childless. ár-, v. árdan. 5 āranj "Inc | N ~] elbow.. 9-43. "Ant *a-rāst Prst'] untruth. ārāstan, ārāy- [Pstn!,^Pd- | N ~] prepare, arrange, adorn. ~ién: arrangement, adornment. a-rawüg [”/wbk!] immobile. Ard р | M?yrd, N ~] a goddess; cal. 25th day. ard [KHM A < А gm; п | N ~] flour. агаа [py | (M rd?w)] righteous, truthful. ardan, ār- [THNN-tn' < А V thn; ?l-tn'] grind, mill. ardāyīh ['i?dyh | M?rd?yyh] righteousness, rectitude. ardig [/tyk! | M ?rdyg] battle. ardikkar рук], -kl | M?rdyqr] warlike, warrior. ~ith: doing battle. arduš [”ldwš = Av. aroduš-] a degree of sin. Ardwahišt Prtwhst' | M ?rdywhyst, (N urdībihist)] Right, the second Amahraspand, guardian of fire; cal. 2nd month; 3rd day. arešk [lysk' | M ()rysk, N rašk] envy, jealousy. ~én [-yn'] envious, jealous. ārešn Pim! | M ”7ysn-, N (a)rif] cubit. aryand [?/епа | N ~] horrible. arģawān [*/gwk'*n! | N aryawān] purple. armēšt ["/myst'] inactive, infirm. ~ih: infirmity. armēšt-ģāh [-g’s] secluded place for the infirm. агбуї&п [/wdšn'] growth. ~ig [-y&!] growing, vegetable. ars Dis | M?rs, N ~] tear (drop). artēštār УЯ? | N artēšdār!] warrior. „īh: warriorhood. arus [2/00] white. arwand [wnd] swift, valiant; river Orontes. ~ih: swiftness, valour. arwés [lwys | M ?rwys, N ~] rope. arz [KSP! < А Ар; с | N ~] worth, value. Arzah [Iz h == Av. arazahi-] the eastern continent of the earth. arzan [PE < А prg’; len! | N <) millet. arzàn Plen | M *rz'n, N ~] valuable, worthy. ~ig [-yk'] worthy. ~igih: value, worth, worthiness. arzidan, arz- [?/с-уїп! | N ~] be worth. ~išn: value, worth. arziz (сус | M ?rzyz, N ~] tin, lead. —ën [-yn'] tin, leaden. ārzōg Picwk! | M'wrzwg, N àrzó] desire, lust,
551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
617:wāspuhr [w’spwhl] principal.
618:wāspuhragān [wspwhlk’n'] 1. special, particular; 2. courtier. 7h : speciality.
1226:childless apus, starwan.
1422:courtier wāspuhragān.
3048:particular ēwāzīg, waspuhragan; in ~ pad nàméist.
3223:principal mādagwar, wāspuhr.
3730:son frazand, pus(ar).
3763:special waspuhragan.
3764:spectality wāspuhragānīh.
4704:purrmāh Ku purrsardag 15 Qa» yes dahint roe to pusyān V 10 pusar ND 10 póstén V yen 10) póst we» 105 рап}, poz So panjah ay S ya) panjag, pēzag 13619 pos- = 74010 pūšīdan Wres“O ve pēšišn VUV puštībānīh «U ye) 43 «650105 pustiban т^” оу S ANA pušt VOU 199 puštag 1100010) püdagih ^t 5120
4705:рапа, (пет!) poy- penih pus | frazand frazandih panir pondik pēyišnīg pad!, pen padgohr padnérog
4779:spāh ALY Q335 dēbahr, spihr, Nay LAKE spaxr spahbed VP OR 0335 spas ts” суз? spāsdār Nee es. spāsdārīh uA a soda) spāsešnās TO Put 0335 debàg VW ett spāsūmand ? v€ Pus” q335 spāš AV суз?
5276:nāmčišt tery Qe wāspuhr 102.294
5277:Waspuhraginih “9 ve 1 n wāspuhragān we) 103351 wāyīdan ETH wastar N 635^ | wāstaryēš ^0 ch ev wüstaryosih ^c ~ 39 \
=== PHD abus
166:~ih: wonder. àb-dàn [^5d?n!] water-holder. abdast ['5dst!] hand-guard. abdom Pfdwm | М ?bdwm] last, final(ly). ~ih: finality, end. abd-sahist [pdshst'] wonderful. abē- [5»(y)- | M ?by-, N bé] without, Jess. ~-bar [-5/] fruitless. ---bé$ [-bys] unharmed. ~-bim [-bym] fearless. ~-bimih: fearlessness. e--boy [-bwd] senseless. ---bēyih : senselessness. —-büd(ih) [-bwt', -bwtyh] deficiency. «=čim [-cym] without reason, cause. abēdān рругп!] of use, wanted. abé-|-guman [-gwmn!] without doubt, certain. —-$umiünih : certainty. ~-mizag [-m(y)ck!] tasteless. ~e must [-mwst'] uncomplaining, content. ~-niyaz [-пуа?с] free from want. ~=-68 [ws] M *by?wš, N béhóf] senseless, unconscious. -~-6Sih : senselessness, unconsciousness. abér [yl] very, much. abē-rāh Payis] e erring. abesar [fysl | M ?bysr, N afsar] crown. abesīhēnīdan, abesihén- [Ashyn-ytn', v. abesihidan] destroy. išn(īh): destruction. abesihidan, abesih- Pžs(y)%-ytn! | M? bysyh-] perish, be destroyed. —išn(ih): destruction, ruin. abespardan Pžļsp?/tn!) = abespurdan. abespurdan, abespār- [’fspwltn', ?psp'l- | M ?byspwrd, ?byspr-, N sipurdan, sipàr-] commit, entrust, consign. ubestag [5(y)s? k!] Avesta, the Mazdean scriptures, abestām [ēst m] = abestān. abestàn [°25/°п!] refuge, support, trust. ābestan Dóystn! | P ?bystn, N abtstan] = ābustan, abé-süd [yý swt'] profitless. “Аһ: profitlessness. a-bëš Буў] harmless; unharmed, invulnerable. ~ih: harmlessness; invulnerability. abē-|-wināh [-cwz?^s | M?bywr? 1] innocent. ~-wizend [-wznd] harmless, invulnerable, safe. abézag Pfyck! | M ?bycg, (N *oëza)] pure, holy. ~th: purity, holiness, abēzār Pye’, ?Буе?1 | N bézdr] free.
170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
593:tan-bahr [żn'Þ’ hl] physique. tand [tnd | = P] faint, languishing. ~ih: faintness, langour. | tan-drust [tn'drw(y)st! | N ~] healthy, whole. ~ih: health. tang [ing | = M, N ~] narrow, tight. ~ih: narrowness; distress. tanig [tn'yk! | N tani] bodily, corporal. tanigard(ig) [tnykrt(yk)! | M inygyrd] corporeal. ` tanīhā [tn'y/? | M tnyP?, N tanha] alone. tanómand [tn wmnd | N ~] corporeal. “АҺ: corporeality. tan-tdhmag [tn'twhmk'] (sap) of plants. tanuk [tnwk! | N ~] thin, shallow, tanür [tnw] | M tnwr, N ~] oven. tar [LCDr! < A l-sd; tl | M tr] over, through, across. ~ kardan, ~ menidan: abuse, despise. -tar [-z# | (M -dr), N ~] suffix forming comparative adjectives. tar [2] | M гу] darkness. tarāzēnīdan, tarāzēn- [tcyn-ytn!] weigh. tarázüg [tPcwk! | (P tPzwg), N tarazü] balance, scales; astr. Libra. targ [tlg | N ~] helmet. tarģumān [tigm?n! | M trgwmn] interpreter. tarig/k [PIyk! | M гуур, N tárik!] dark. ~th: darkness. tarist [¢/st'] = tar. tar-mānīh [t/m’nyh] perversity. tar-menišn [tImynin! | N tarmanist] perverse; contemptuous. 7h : perversity; contempt. tarr [t/, LC Dr (in error, v. tar) | N —] moist, fresh. ~ag [tik! | N ~a] vegetable. tars [2/5 | M trs, N ~] fear, respect. tarság [ts k! | M trs’g, N tarsā] Christian. tarsāģāh [15(?)/?5] respectful, reverent. ~ih: respect, reverence. tarsidan, tars- [tls-ytn' | (M tyrs??dn), N ~] fear, be afraid. tarwénidan, tarwēn- [t/zvyn-ytn! | M trw-] overcome, conquer. tas [25 | N ~] die (for gaming). tasum [tswm | = M] fourth. tāšīdan, tāš- [O i-ytn!'] cut, cleave; create. taSkanag [tšknk!] under-shirt. tašt [tšt' | N ~] bowl. tāšt [021] *certainty. ~ig [-yk'] certain. tāwān [1?(d)w’n' | N ~] compensation, obligation. taxl [t?% | (M thr), P txl, N talx] bitter.
605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
705:abuse (n.) dušnām, wad-wāzag.
706:abuse (v.) tar kardan / menidan.
1224:childbirth abusih.
3205:pregnancy ābusīh.
3206:pregnant abestan, abus(tan), zahag- отапа.
```


## [2026-09-14T00:54:46.026Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN pisar\"; grep -n -i \"pisar\\|pusar\\|pûr\\b\\|âbistan\\|abistan\\|ābistan\" HRN.txt | head -20"
}
```


### [2026-09-14T00:54:46.078Z] TOOL RESULT

```
=== HRN pisar
3044:ap. aw. pud^ra- 'Sohn ; phlv. pusar, pus, Säh]puhr;
3486:tahan, tabistan 'Sommev\ (jNnozxn, Jer. 40, 10; niwNP,
```


## [2026-09-14T00:54:47.032Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HUB\"; grep -n -i \"pisar\\|pusar\\|abistan\\|puthra\\|pu.ra-\" HUB.txt | head -20"
}
```


### [2026-09-14T00:54:47.094Z] TOOL RESULT

```
=== HUB
79:'^abustan auf zd. ^apud^ratanu- oder nur *apu&ra- *be-
83:apud^ra- schwanger steht fiir ^Opu&ra- neben richtigem
84:apu&ra- *kinderlos'.
2894:sein an pidar u, s. w. wie pusar, pisar (aus pus) etc.
4882:zd. apu&ra- =: *apw^ra-; tihf 'leer = pSz. tihf, phi. tuhik
4883:Shk. 269; diz- *b6se* = duz, ap. dws-, zd. dus-, dui-; pisar
4884:'Sohn* = pusar (nach Horn durch pidar beeinflusst) ^) ; misk
4895:'Sohn' aus *puhr neben pus (pusar) = ap. pttd'^a-; Sapur^)
6672:selbst', abistan *schwanger ) gefuhlt wurden ; kabutar 'Taube'
7251:ap. "^Old^at-, zd. drisat-] pus 'Sohn (daraus pnsar, pisar
7256:apus H. 5 = zd. "^apu&ra- (fiir apu&ra-), s. oben p. 5.
10230:abistan 5.
```


## [2026-09-14T00:54:51.124Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--- HUB 70-95\"; sed -n '68,95p' HUB.txt; echo \"--- HUB 7245-7260\"; sed -n '7245,7262p' HUB.txt; echo \"--- HUB 4880-4900\"; sed -n '4878,4900p' HUB.txt"
}
```


### [2026-09-14T00:54:51.193Z] TOOL RESULT

```
--- HUB 70-95
hat, und dass sie uberhaupt zu weit geht, wenn sie die
ganze Arbeit ftir verfehlt erklaren mSchte, weil Manches
daran zu tadeln ist.
Vgl. 8 ale m an n, Liter. Centralblatt 1893, Nr. 43, Sp. 1547/8;
Fr. Mil Her, WZKM., ,Bd. 7 -8; Maun, ZDMG. 47, 698.
Hubschmann, Persieche Studieiu 1i
■I tH9fy
5. Aus zd. *apu&ratanu- konnte np. nur bustan u. s. w.
(mit b im Anlaiit) werden, da das Gesetz besteht: die
kurzen Vocale a, i, u vor einfachen Consonanten fallen
im Neupersischen stets ab. Also ist np. dbistan aus
'^abustan auf zd. ^apud^ratanu- oder nur *apu&ra- *be-
kindet* (mit spater zugesetztem tan, vgl. x^^tan) zu-
riickzufuhren, wie auch die von Horn angefuhrten
Dialectformen ^) zeigen, die samtlich a haben. Zd.
apud^ra- schwanger steht fiir ^Opu&ra- neben richtigem
apu&ra- *kinderlos'.
6. Np.a&«5i3C^ar beiFirdusi (ed. Vullers) I, 439, v. 103.
Das Wort wird das Thema dpi- ^Wasser enthalten 2),
das doch noch nicht endgiltig durch Bartholomae
aus Bh. I, 95, 96 {apiyd, apisim) beseitigt ist. Jeden-
falls ist Bartholomae's Erklarung des np. abis-
(aus avah') unbegriindet und nicht zu begrunden, zumal
ein avah' 'Wasser durch Geldner KZ. 28, 186 fur
das Awesta nicht erwiesen ist.
7. Vgl. g. tag Teuer ZDMG. 36, 61, arm. LW. afas
*Feuer Sebeos p. 27.
8. Np. dxur 'Stair = phi. dxur oder besser ax^ar (Yatkar-i-
--- HUB 7245-7260
Zardust, arm. Zradest, Zradast, phi. Zaratust {Zara-
fuxst) => zd. ZaraO^ustra-.
3. Fur Or : fr in FrSdun, siehe p. 207.
§ 96. Ap. &^ wird im Np. zu s oder hr:
a) zu 5 in: si, [liter se *drei' (s. oben p. 78) = zd. g.
pi. x^rayqm, vgl. ap. ^Htiya- *der dritte*; si 'dreissig =
ap. "^Old^at-, zd. drisat-] pus 'Sohn (daraus pnsar, pisar
nach pidar u. s. w.) = ap. pud^a-; pas 'Wache', phi. pOs
Gl. and Ind. 91, Bdh. Gl. 96, paspamh *Schutz' Bdh. Gl. 96,
zd. padra^; das ^Sichel', phi. das Gl. and Ind. 181, skr.
datra-; obis-tan 'schwanger, phi. apustan Gl. and Ind. 16,
apus H. 5 = zd. "^apu&ra- (fiir apu&ra-), s. oben p. 5.
b) sonst zu hr, das nach urspr. langem oder zum Er-
satz^) gedehnten Vokale zu r wird: pur *Sohn = phi. puhr
V V V V
in S(a)puhr = arm. Sapuh (alter Sapurh), np. Sapur, ap.
pud^'a-; pahra^) 'Wache, arm. pah 'Nachtwache, Wache,
Gewahrsam, Gefangennahme, Belagerung' (alter parhY
--- HUB 4880-4900
paz. humdna u. s. w. (oben p. 106) ist wohl humdnd zu
sprechen, wie tuxsd fiir taxsd (oben p. 47) = paz. tuxsa,
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
```


## [2026-09-14T00:54:51.755Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--- HRN 3035-3055\"; sed -n '3035,3055p' HRN.txt"
}
```


### [2026-09-14T00:54:51.839Z] TOOL RESULT

```
--- HRN 3035-3055
LW. af/. pistän.
Vergl. Bartholomae, Indog. Forsch. I, 187 Anm. 2.
318. puser, pur 'Sohn, pus (Sahn. III, 1516 Vers 336,
1517 Vers 358 2), 1523 Vers 473).
*) So lese ich statt nvedlnltan.
*) An den beiden ersten SteUen vielleicht für puser zu emendireD,
doch kann bei puser wie bei pider die Izäfe fehlen, vergl. Landauer
zu S. 1517 Note 4.- 71 -
g. pur, Semn. i>lr; Käs. pur, pur.
ap. aw. pud^ra- 'Sohn ; phlv. pusar, pus, Säh]puhr;
ai. putrd-,
kurd. pisir, pes[mamy püer (H.-Sch.); oss. d. furf,
t. firf (294) ; bei. n. pusay (304) ; wa/. /?6Y/', ^iyn, piic^
sar. /?öc', minj. pur; arabisirt für in fayfiir, takfür ^),
i'm- (N. pr.).
319. pesend zufrieden, angenehm', pesendlden.
ap. *M/)rt -T- K^arf-; aw. [^sad- (Geldner 1 [/sad-,
KZ. 27, 242), vergl. sendah-, vahmö.sendah- (?)2) (auch
l/"sac/- 'sitzen' kommt mit inligirtem Nasal vor, vergl.
ai. ilsandt- 'Sessel*, ksl. sedq 'ich sitze', apr. sindäts),
Spiegel, Commentar II, 311 (nur fälschlich mit
```


## [2026-09-14T00:55:02.625Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"apu.ra\\|apu\\^ra\\|ápu\\|a-pu\" BRT.txt | head -20"
}
```


### [2026-09-14T00:55:02.725Z] TOOL RESULT

```
3721:aL  ÄA-i-J.  m.''Bi=ev«iB'-    -   Wegen   W-  »gl-   ,    j.    »a-puBra-    Adj.    (fem.     'rä-)    'ohne
3727:•  1,  *api-vaite''  Inf,  'zu  verstehen :  F.7.  ,,  ,  .  .^.i  .j-  _  *.  ».-.  . ■>  "^  /  KompA.  —  ai.  aputra-  Adj.;  mp.  afus,  —  l^i.: 2am  V.  val-.  —  Pü. :  andar  dänUlan.  —  ■)  Hds.        apus,  afUiar.
3744:•  j.  'a-puSra-   Adj.,    nur   fem.  °r.j-  'dieiAi  ..  baya  ahunaht    vairyehe  'oa  (IS.)''
3748:•  j.  a-puyant-  Adj.  'nicht  faulig  werdend, nicht  verwesend':  ya^  ksrmavqn  fo-as^m ahUm  azar?hnt3>n  amarpsmUm  a/riiyan- tim  -yanlpm  Yt.  ig.  11;  —  ^'ya  Vyt.  4^ '', F.jh-)').
6641:j'ff  . .  hö  ba   azh   3s  ys  .  .  V.p.51  f.;  —  yat  Ae  narS  irista  apuirai  ariAat  Vd.  2;
11225:•  j,  iaräiti- £ 'jungeFrau"^  uzw.  aÄwnscher Schöpfung:  'räiH  (NS.)  huraolaya  darr^a apuhra  aäti  V.J.  24;  —  %wqm  (näml. arpdvlm)  kainitiS  .  .  ja^iyhnte  .  .  nmänö.- faiilm  'hwam  'räitis  (NP.)  zhanäitis  Jail- yiinte  hutämJm  Ytj.S?;  —  äsca  'räitis (NS-)  ahi  yqm  il  yava  'räitinqm  k?hrpa sraistqm  dadar?sa  H.  2, 10.
12880:—  ')  S  411-  3  d. •  p.  darga-,  g.  daraga-,  j.  dar«}-a-  Adj. (fem.  °7J-)  'lang';  i)  räumlich:  Ufa  tarn car^am  yqm  'yqm  YtJp.  77;  5.50;  — mi^rtm  . .  yeAha  'yäat  bäeava  .  .  Yt.  10. 104.  z)  zeitlich:  M<?i«(sd.)  tat  äs  nsit 'y?m  Yt.5. 65;  —  "iimal  aipi  zrvätum Y.62.3,\tig.a6;  13.53;  —  °f^^  ^yo (sd.)  t^mattks  Y.31. 20;  —  'yayäsca  paiti danyjjltdis  YL  /y.  1 3  j ;  Y.68.11;  —  tsm (nämL  kämtm)  msi  data  'gahys  *yaos{^^^ vairyS  stSis  Y.  43.  13;  —  hyatcä  -gSm *Jr3gvö.d»dyS  rasö  {sd.)  Y.jo.ii; — ptn- fum/a  (sd.)  barjsma  starane  °y?mca  yasram ..yaaJnS'Vt.iO.iiSi—ya^a  Sicä  *aiivi- iayama  'ya  amiiayana  . .  hr^yrnya^^aSum (sd.)  Yt  70.  7  7 ;  —  °gäi  Tsyai  bfzvait!  hax- maim  (sd.)  Y.  40.  3;  —  'yai  hax^räi  Vt 10.  T),  17.6;  — fravaiayS . .  hulhaxmanS . .  'yaa'fyj  Aax^oralifyff  Vt  13.  30;  —  'y^m Aaxma  V.  60.  j;  —  dättm  tS tanuye  :^ar»nB ' urvnaläi  •y?m  havanfum  (sd.)  Yt77.  22; F.^b;  —  urunaica  'ye  havanhe  A.  i.ii; —  'yäi  AaosravaAAsi  .  .  -yai  AavafiAäi Vjtjs;  —  a  'yät  ^ä.bairyilt  (sd.)  Y. öo.  6;  —  'yqfi  upayanayä  (Stverz.)  Y, /.  13  usw.;  —  'ya  (APn.)  data  .  .  sara- >uäraAe  T.  ^6  {?);  —  iaia  tl  'yim  ävSya (sd.)  aakal  H.2. 34;  16.  a)  Adj.  an Stelle  unsres  Adv.'':  :^afsa  'yd  tna^äka "schlaf  lang,  o  Mensch"  V.  rÄ  16;  — earäiti  .  .  yä  'ya  apu%ra  aHti  V.  3.  34; 34.  b)  ASn.  als  Adv.:  H  utä,  'gam  jlvä
15350:"..der  du  vom  vergänglichen  Leben  zum  ehedem*:  /rarasayS  .  .  yl  araca  'ra unvergänglichen  Leben  herüberkamst"  \.  /raoirisisiä  fsA.)  ya^ra  ..  VtJj.2S;  — 7.  52.  A)  Kaus.  'vorwärts  und  hinüber-   ij  nJtriJkqm  yam  apu^ram  .  .  anasaxtqm
17836:Vgl.    ai.   soma-putväka-  m.;    mp,  frmiäk  EN.
20823:ahmäi . .  apataytn  Y.p.  15;  —  kantalit aBsqm  hufrayuxta  yBi  niyräire  saraku  . , Ytio.40;  /7.10,  Vr.J2.i;  —  nBit  hräyB nBit/räyanÄB  asahe  . .  frähnti  (sÄ)  *yBi nBit..*pmsänfe  F.44i  —  vUpanqm  narqm näirinqmca  . .  yBi  hnti  .  .  masi^aca  V. 2.  27  "J;  27  f.i "';  —  kasannm  narqm  . . yBi  hyqn  ..aeßsta  Yt&gs; —  a^aurunam .  .  ysi  *iyeyqm  düraf  Y.42.  6;  —  paragft dvaiibya  yBi  (statt  Du.)  atihn  i^aitvada- %asda  j^aOT/adai^Tsca  V.  Ä13;  —  strqm matahB  küTB yBi"'>  histsnta  ..  \t13.5j;  — /ril  hg  masdä . .  raiu%te3m  barät  gai^anqm yäi'i^  hwä  valmti  ..  ahüm  ratümcd  gal- ^anqm  Yt. /O.  92;  —  anyqm  daxstanqm yBi"i>  h»nti  atirahe  mainySus  daxsttm  V. 2.  29;  —  NSf,:  dalnqm  ..  ya  haitinqmls ..  mazistaca  . .  ya  ähtiirii  V.i2.g;  — hanyä  indat/iürya  . .  ya  vtspaJaurvairi nqma  Yty.  142;  —  %qm  p?rf%wlm  .. yqm  (s.  II)  masimca  . .  yS  barihri  paraos srJraht  ya  vJsptm  ahum  baraiti  Yt.  13.  g ; 12.  ly^,  V.  /.  9,  /l.  9;  —  arydvTm  . .  yä arSttam  xsudrä  yaoidaZaiti  Y.65.  2;  3,  lo. 15.  5^-3.  Vtj.  126,  17.2,  /p.39,  V.22. S,  Vr.7.3*,  22.1,  0,5.5;  —  caräiti  ya dariya  apu%ra  a^ti  V.J.  24;  34';  —  */ra- zainltm  .  .  ya  ml  fr^jayät  nmatamla  . . Y.6'2.5; — ND£:  haurvata  amtrytäta  yBi stB  miid»m  a^agnqm  Yt/.  35;  — ■  sanha- vaci  annavaci  yBi  Am  kihrpa  iralsla  Yt. 5.34;  —  N.-APf.  (y^.W):  fravasibyB  yä iririhusqm  .  ■  yäs/a  Jvaniqm  .  .  yasla narqm  azätanqm  Y.  2^.  5;  23.  x  {.*,  ^6.  2 ;
23434:'jagen,  jagend  verfolgen' :^ff^a8a'a»i_j'^»t apu%ram  Janaiti  vIt  vayäti  va  xraosyäti vä  patdayeiti  (sd.)  vä  V.  75. 5 ;  —  ysi  vlsps U  apayeinti  yq  *aoe  paskät  vyeinii  ". ,  denen sie  von  hinten  her  verfolgend  nachjagen" ¥.57.29;  —  y&  *ava  ^xbayats  avaähe vyqsca  vyanasca  apatse  (sd.)  zbayeitt vyqs  apagaße  vyänS  "welche  beide  um Hilfe  rufen  der  Verfolger  und  der  Ver- folgte .  ."  Vt  i^.  3S;  —  aval  vayul .  . yat  xtia  dqma  vayemi  Yt/J.  43''.  1
27040:Eig.  Bed.?  Nach  JuSTI  NB.  309  Kurzname zu  Sviraitit/Tit.  —  l'ü.:  spiiämin  (mit  dem  an der  Herkunft),  Sü.:  spüamänai,  (zu  Y.  26.  5): s^mapulrah.  —  ■)  Mit  a  im  VSm.,  DStn., und  NPm.;  »gl.  dazu  flöfc^aya- No.  i.  S.  noch No.  2.  —  >)  So  auch  YL  8.  2  zu  lesen,  wo NA.  'lainahe  bietet.
```


## [2026-09-14T00:55:04.398Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== NYB\"; grep -n -i \"pusar\\|puhr\\|ʾbwstn\\|abustan\\|ābustan\" NYB_vol2_glossary.txt | head -15; echo \"=== CHEUNG\"; grep -n -i \"pu.ra-\\|pusar\" CHEUNG.txt | head -8"
}
```


### [2026-09-14T00:55:04.468Z] TOOL RESULT

```
=== NYB
502:apäk-puhr
503:apäk-puhr [LWTH pwhl] he who has a son 22%. - Cf the NP compounds with bà: bā-āb ‘having water’ and the like.
507:(cf 41?" and 89%); ~ fravartak in the letter 1822; — combined with another prep.: ~ 6 pad estat 28%. 1189. 11917 (cf above 1871); ~ 6 ax“ i astomand 401; m andar äyiyänak 409; ~ tdi sdxdn 401; ~ pat óstak 48% (ete.). — b) temporal: ~ sal 2 mazdesn bag’ Šāhpuhr” in the year 2 of the Mazdayasnian Divine Sh. Pl:l; ~ sal "68 in the year 68 P2:1; ~ pat han jamān ka at the time when 41%, adak ~ pat jamän at that time 619; 4214; 3 sap td three nights ago 512-3, — c) figurative: on, about (esp. in headings and book titles), concerning; (reigning) over, (merciful) to, (hostile) to- wards; (means) for; ete.; — with an inf. or a v.n.: in order to 3714-15, 4515; 1185 (continued by inf. + rād, l. 6). - ~ does not govern encl. pronouns; single excep- tion apar-aš 54° (late passage). — Av. (394 sq.) upati, OP upariy; MPrthPrs br; Paz. awar; NP bar. Cf aper. — On MDM 43" v. hàreftan.
584:apé-pit [’py-’B'] fatherless 22$. ape-puhr [’pypwhl] without son 226-7.
763:ütur ['twr'; inser. ’twry] fire, referring to the old Iranian fire cult: ~ yazét god Ātur 25?; ~ farröbäg, gušnasp u burzen mihr the names of the three sacred fires connected with the three classes of the old Iranian society 118, explained 27-9; ~ farröbäg, i -bag 974. 9511; ~ gusnasp 955; ~burzén mihr 95%; ~-dn šāh the head of the sacred fires 1222-23, 131; — sal 58, āturv i Artaxšahr säl 40, āturv Šahpuhr i āturān šāh sal 24 SPrs:1-3 = sar 58, ātarē Artaxéahr sar 40, ātarē Šāhēpuhr ātarūn xšāh sār 24 SPrth:1-3: ‘... of the year 58 (viz.) the year 40 (of =) after the (enthronement) fire of Artax- Sahr, the year 24 (of =) after the (en- thronement) fire of Sahpuhr, the head of the fires’, which means the year 266 A.D., v. Christensen apud Ghirshman, Rev. des arts asiatiques X, 1936, 127—128 (the year 40 reckoned from the coronation of A. in the year 226, the year 24 reckoned from the coronation of S. in the year 242, and the year 58 reckoned from what must have been the epochal year of Sassanid time-reckoning, viz. 208 A. D.). — [~ the name of the 9th day of the month, also of the 9th month of the year; dade (q.v.) pat — the name of the 8th day of the month: FrP 28.] — Av. v.s. v. ätaxs; Prth ätarö (g. v.); MPrthPrs ’dwr; Paz. ädur; NP āčar, ādar. As to the three sacred fires v. Christensen, Sass. 164— 167; cf also de Menasee, Feux (1964); Mary Boyce, BSOAS XXXI, 1968, 52- 68, 270-289.
809:aviš [?wbš] adv. l. used instead of the prep. 6 if it refers back to an encl. pron. in the beginning of the sentence: zahr i-š ~ fréstit the poison that was sent to her 918; kū-t... ~ ne rasét lest ... shall come upon thee 688-?; api-§ ... ~ barét bring for him! 7489 = bé-§ ~ barét 76’; puhr i-Š ... ~ mat the punishment that has come upon him 741^; cigón ka-šan... ~ hilénd as if one poured ... upon them 101291, — 2. as a substitute for the prep. 6 + the encl. pron. 3d p. sg. -&: 14-16, 413.15, 727, ete. passim; taking up the rel. pron. 4226, 7213 v.s. v. ke. — Ps. ’wbsy; MPrs ’wys, from an OP adv. *abišā or *abisah derived from Av. (87 sg.) adbi, aiwi = OP abiy, as patiš (q. v.) from pati (cf also haciš : hac). I maintain my opinion expressed in HP II, 212; a
872:äzätak [’z’tk', ^otk', >-YLYDWN-tk'] true-bred, of cows 422:6; — pl. cas. obl. ~ -ün (Ce?tk?n!] used as pl. of äzät (1) 1113, ef s. v. väspuhrakän.
878:bag [bg, bk'; inser. bgy, Prs RHY”, Prth ’LH?] 1. god 381! [bk', a quotation from Y. 1019]; pl. eas. obl. —-an [bg?n!] 75! (opp. dēvān). 1131?; garān —-än kof the mountain of the mountain gods 20? (v. s. v. gar). — 2. lord: Ohurmazd ~O. the Lord, of the supreme god 211’. 2224; — of kings: Käyös ~ 458; ~ Päpak HajA:4. B:4. SPrs:8. Prth:8; ~ Artaz- šahr HajA:3. B:3. SPrs:6. Prth:6; 1091, 111%; ~ Sähpuhr HajA:1. B:1. SPrs:4. 11. Prth:4. 6. 8. P1:1. P2:9; ~ Ohurmazd P1:3; ~ Xēsrēi 10921; pitar ~ P1:10; — pl. cas. obl. —-än [SRHY?-n, bg'n'] as a pl. majestatis: öisän —-ān Šahpuhrv P 2:8, without the king's name Pl:4; šmāh ~-dn addressing the king
1117:cê [MH; cyh 12111] 1. interrog. pron. what? 59. 726. 89? ete.; how? 1513, 51?!; with prep. 6 cé, pat cé, hac cē; cé rād? why? 351! ete.; combined with a subst.: ce zaman? 715, cē gah? 722; pat ce āivēnak? how? 76%; cé vinäs? 121, cē vat? 7322, etc. ; apar cē ātvēnak margēnītan i Zartuxst pursit how to kill Z. 4912-25-26, 4813-14 (apar governs the whole clause). — 2. rel. pron. what: či ndmakY ce ... nipištv estet, ce Šahpuhr" . . . framätY nipigstany P 2:3-4; kart" ... ce ... sahät P2:8-9; har ce 61.3218, 86%. 9618; ēt ce ... apāc āvurt 11214715; 361; pat hàn cim rād ce 121". — 3. conj. a) subordinating: because 105); ce ka id. 991. — b) coordination: for 2$. 619.22. etc., passim. — MH 305 wrong ideogr. for encl. -c(%). — < cahya, gen. sg. of Av. OP (422 sq.) ka-.
1220:dāštan [d'štn'] dār- [YHSNN-; d'1- 217. 281. 10014. 10279], imp. sg. with encl. pron. där:om [YHSNN-m] 6t; opt. 2nd p. sg. dārēš 41!?; pt. dašt = pret. pass. 3d p. sg., construed as an act. form 495-5; to keep, to hold, to sustain, to maintain, to have, 8?! and passim; — with an adj. as a complement of the obj.: Sahpuhr kanicak āžarmīk u garamik däst Š. kept the girl honoured and respected 163-4; 225 ete. passim; the complement some- times comes near to an adv., e. g. véh ~ to keep, handle a th. well 5026-27, and may be replaced by an adv.: én zan garämikihä ddr 1024; 6415; — with an obj. and pat + an adj.: to consider a p. or a th. to be ...: pat margaržān ~ to consider a p. guilty of death 1014-19; 6398-9, 8017, 839-19; pat azateh (cas. obl. sg.) där-om! consider me as a free (wom- an) — release me (from slavery)! 64, v. s. v. Gzat; — pat & ~ ku to be of the opinion that, to think, imagine that 2525, 982-3, 3227 sq. 5012-13, ef NP pindāštan < *pa(t) én daštan; pat ce dārēh how do you regard (the case mentioned in the preceding kū- clause)? 105-$; pat depahr, pat nihän
1259:*Dēnē [dyny] n. pr. P1:7..— Reading not quite certain. It may be the abbre- viation of one of the numerous compound names beginning with Dén (Dén-Ohur- mazd, Den-Sähpuhr, Dēn-ayyār, Den-dät etc., v. Justi, NB).
1441:eränak [’yl’nk'], pl. cas. obl. ~-dn the Iranians 228. — Paz. érqnagq (Mx). Cf s. v. Wwäspuhrakän.
1446:VII, 1934, 265-274; Nyberg, Rel., v. Index. Eran-x"arrah-kart-Sahpuhr [-GDH- =
1754:expressed (nominal sentence as in the Semitic languages): man Sähpuhr hom 154; tē ke he? 737; to rād ke Dugdav he 4721. en rētak ke hast? who is this boy? 1617; Artaxsér ... nē pat giyāk hast 6?" sq.; kë zan-& hac õi hucihrtar nest ‘qua pulchrior non est mulier', who is the most beautiful of all women 259-19; ēzšān amüh hem ke ... we are of those who 5723-24, šmāh ke xtēn het 6111; sagr hend 86%, — 3. in the 3d p., together with a subst. virtually in dat., or with a pron. in cas. obl., it expresses ‘to possess’ xdnak i-t hast the house that belongs to thee 5325-26; fradandan i-5 hast the chil- dren he has 142; with ràd as in NP: Papak rüd pus-é hast 3?. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions, e. g. han- dešitar vicītār hom 125; frēftār hah 3419; matür hom 46’; kartar hom 101?’; brihenäk hend 7777; ke (cas. obl.) vitīrišn nest which is incorruptible 66°; tö hän-ic äkäh he this thou knowest 399; hayyär hend they help 106%; -š hayyaréh hénd they help him 1001-12; pat kamēstārēh + spihr hénd they offer resistance to the. Sphere 8721; ké (cas. obl.) Mihr u Mah pat pust hah which M. and M. protect 317-8, ete. — 5. auxiliary vb. forming compound tenses: būt hom, būt hend I was, they were, eto., v. Grammar; notice: HWH-nd, regularly hend, must stand for the subju. händ 14? (fut.). 335 (cond.). — 6. Wrong use of the ideogr. HWH-: a) HWH-wm for the encl. pron. lst p. sg., added to the pret. pass. in order to emphasize the agent-
1882:handarz-pat [hndlept'] chancellor, chief judge, head of the treasury of a province or a corporation, administrator of pro- perty: Sakistin ~ P 1:6; dar-~ 7 vàs- puhrakän the court administrator of the (royal) properties 1118-19, v. 2vdspuhrakdan and Périkhanian, REA V, 1968, 20-21 (cf s.v. väspuhr); [yztpt MLKTH-n hndrzpty KZSPrth 1. 27 = yztpt ZY b’ny(!)kn hndicpt Prs 1. 33 = Gr. v. InodtBad Bactrrcodyv avčapčaBIŠ (enumer- ated among the lower ranks of court officials). — Arm lw. handerjapet ‘the Master of the Royal household’, already in the Bible (e.g. 1 Kings 16:9 = Gr oixovéuoc), then often ‘director, manager” in different functions; when speaking of Persian officials the authors use the form anderjapet: Sakstan a. P‘aust. Buz. 4,45, mogac a. ‘the chancellor of the Magi? ibd. 4,47, or in the idiomatic Persian form Movan a. EliSe (5th c.), Hist. of the Vardans (Venedig 1838), 138. 142 (thus the MSS; the ed. han-).
=== CHEUNG
19503:*us-) LKh. uspurra- ‘full, completed’ || (+ *ham-) OKh. hambir- (etc.) ‘to be filled 
36665:uspurra-, 296
```


## [2026-09-14T00:55:15.226Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '3718,3750p' BRT.txt"
}
```


### [2026-09-14T00:55:15.277Z] TOOL RESULT

```
„^..,   .gl.  aipi.mvra;  yt  14.  31-  |0-S.  49-
■     ■    ■  «t.  »j-ii.-        L        ■   u-  j.         Ableit—  top.  (Pü.)  5fH!   1    'gravidR',  a)  *>.»•
•j.aipi-«bao)^-Adj.'hLnterhereinbiegend';  ,;„„.„_  „p.  vgl.  0*^/01.  (■tjhwanger').  - •7?  (NSm.)  nama  ahmi  Yt  /5. 45.  ■)  Vgl.  Pü.  zu  apu%rya:
aL  ÄA-i-J.  m.''Bi=ev«iB'-    -   Wegen   W-  »gl-   ,    j.    »a-puBra-    Adj.    (fem.     'rä-)    'ohne
\^°''}'-  ...    „„,,         ,  iSohn,    Kind':    camiti  .  .  yä    äariya    'ra
.  y  aipi-paramna-  Ad,.,  PPM.;  s.  l^i^.    ,  ^^^^.  „^j^^  p^^,_  ^jj^  j^g^  kinderlos  ist"
""^    ,  ^  , ,.     V.S.ai;  —  puhräne  aknm  (lüfal  fiourum
:  ^^  °?,'f 'iT^  /  t  °\  -^lü^'l"  .''  '/ramraomi)ya>,a  'nli  "einem  mit  Kindern keine  M,lch  m  der  Brust  hai^  nicht  säugf:  (^  ^^^^  ich  einen  höheren  Wert  zu)  als nätnkqm  ■  ■  ^0^^m  vlH^d.)  '/p'Bs'fmj'n  <  ^^^^  kinderlosen"  V.4-47;  -  yat  M V.i5.$;  —  hSinsinqm  ..  'pyBstnqm  Vyt  „^^^  ,„^/^  ,^^,-  ^„^^,  «„e„„  ^er  Mann 5*';         _..,,,..,,.  I  bei  seinem  Tod  kinderlos  ist"  Vd,  21;  —
...      ..  rt  T  r  .  ^  V    .    T7      ^äat  hg  'ra  atik(U  Vd.  //.
•  1,  *api-vaite''  Inf,  'zu  verstehen :  F.7.  ,,  ,  .  .^.i  .j-  _  *.  ».-.  . ■>  "^  /  KompA.  —  ai.  aputra-  Adj.;  mp.  afus,  —  l^i.: 2am  V.  val-.  —  Pü. :  andar  dänUlan.  —  ■)  Hds.        apus,  afUiar.
afivatir,  aptvaMf.  I     .   aipu^-jg^anä-  Adj.,  nur  fem.  'deren
,.  at^mi,  VI.  10.  a?^   i^yh  1  ^.^^  kinderlos  ist,  unfruchtbar':  faoiryam
•  ].  aipi-vanl^v-  m.  EN.  emes  iramschen  ^^^^^^  ^^«rf^  «/»  . .  hala  'zanyii Fürsten   der  A^rfJjJ-Dynastie,  Sohns   ^y^  jgjtikayii  \x.i-.<t.
-       -    '  1  y,';an-;  gr,  yj>^  (vgl.  Thes.  L
JCaväta'^:    kavsis  *'var»A}ui''>  asaonö  \i. ^3-^3'i  — yiml'a  karagm  'vohum  Ytig.
71- Eig.  Bed.?  Vgl.  JusTi  NB.  516.  —  >)  Bd.  jr. 35.  —  ■>  NA.  ohne  Trennung.
j.  aipt-irilS  galui    V.  5.  59:    lies    aifi.fril5.- gältä.
•  g-  *aipi.z^3'a-  '*  n.  'die  künftige  Geburt': yaoz^izA^  masyät  '%3m  vahUtH'H.4^.%; ziL  V,  j.ai,  wo  NA.  aipiji'.
Vgl.  iSt  Gdn.  KZ.  30.   531.  —  Pü.:  pas  hac
täyisH,  —  ')  NA.  getrennt;  ebenso  V./o.  18; aber  V.  5.  31   aipi.z'.
•  j.  aipi.äütay-  f  'Verschieben,  Versetzen' von  Worten  (beim  Gebet) :  kä  . .  baya ahunake  vairyehe  anaJyBxoa{sd.)°ia{LS.y> srävayamna    dasa  faiH    artye    ratavS  Y.
KompE.  >)  —  Pü. !  /a  aft  *iülakik.  —  ')  Wohl mos  dem  vorang.  ana/ü^/n  (sd.)  ausgelöst.  — »I  S.  No.  I.
•  j.  a^piäman-  Adj.  'der  nicht(s)  sieht, blind,  blöd':  i^it  ima(  vTsp?m  .  .  mürö vamaiti  *ma  (NSm.)  Yt.JO.105.
KompA.  —  •'{aitian-  n.  -Gesicht',  lum  V.  fäh- s.  Go.N,  KZ.  jo.  Säo.
•  j.  apiäma.x'ar-  Adj.  'blindlings  essend': 'rS  (NSm.",  näml.  'ist  der  Hund')  yaia  |     "'  '  '■ t3yus  V.  /J.47;  47-  I  •  j-  aipy-öxSay-  f  'Hineinsprechen,  Ein-
Pj.:  a/umän  j"!!^  (nur Transskr.)— ')  Them.  Schiebung    vott   Worten'    (beim   Gebet):
•  j.  'a-puSra-   Adj.,    nur   fem.  °r.j-  'dieiAi  ..  baya  ahunaht    vairyehe  'oa  (IS.)''
Gr.  udW.  aE.).
•  j.apu*rya-n.  "Niederkunft,  Puerperium': yal  .  .  allaoa  aisa  nsirika  tdöa  'rTin nijasst  uzustana  "wenn  .  .  dort  die  Frau dann  niederkommt  mit  einem  leblosen Kind"  V.5.4S;  Vd./.?.
Ableit.  aus  'afii'ita-.  —  Pü.:  äpusih.
•  j.  a-puyant-  Adj.  'nicht  faulig  werdend, nicht  verwesend':  ya^  ksrmavqn  fo-as^m ahUm  azar?hnt3>n  amarpsmUm  a/riiyan- tim  -yanlpm  Yt.  ig.  11;  —  ^'ya  Vyt.  4^ '', F.jh-)').
PPA.  iura  V.  J^v:  —  Pü.!  apäyiiti.  —  0  Slalt 'yqs  oder  'y5,  KZ.  2g.  562.  —  >>  Var.  a/u- yqm.
j.  hapsitt  apno  xavö  F.  2  f. :  verkehrte  Um- schrift statt  *n/ii3««(sd.)  a/naauki. j.  apniant  N.  12:  lies  apatiS-Um^m. j.  apyaeili  N.  13:  lies  afiivataili.
```


## [2026-09-14T00:55:33.744Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT xsathra-puthra\"; grep -n \"xsa\\^ra.pu\\|xsa%ra.pu\\|baga.pu\\|baγa.pu\\|baya.pu\" BRT.txt | head; echo \"=== BRT puthra headword\"; grep -n \"pu%ra-  m\\|pu\\^ra-  m\\|puSra-   m\\|'pu.ra-  m\" BRT.txt | head"
}
```


### [2026-09-14T00:55:33.821Z] TOOL RESULT

```
=== BRT xsathra-puthra
=== BRT puthra headword
```


## [2026-09-14T00:55:35.683Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC\"; grep -n -i \"putlos\\|putro-\\|pou-\\|pauros\\|paukos\" IEC.txt | head -15; echo \"=== SYN son\"; grep -n -i \"putra\\|puθra\\|puclo\" SYN.txt | head -10"
}
```


### [2026-09-14T00:55:35.776Z] TOOL RESULT

```
=== IEC
2879:dheuos, ios ‘kinsman, affinis’. Skt. dhaváh “husband, lord"; Arm. cf. ur-£u, gs or-Éui, if for type *putro-dheu- 'son-in- law’; Gk. theios ‘uncle’; theía ‘aunt
12554:paus- (phaus-) ‘puff, blow; empty, trivial’. Cf. pauros & following entries Oss. faw, pl: fäwdtä, s. abuse”; fawn, pp: fawd, v. ‘abuse’; Lat. cf. pau-per, adj. (poor, if for *pau-oper-, cf. magn-opere); OE cf. Tea gs. fea- wes, adj. ‘few’; ON fár, f: fá, cpds. fá-, id. beside fauskr, m. ‘rotten log; LG cf. fos, adj. ‘limp’; Sw. fósa, v. trout; R pux, m. (2) *rout; Cz. pouch, m. ‘hollow shel? beside pouchly ‘empty’; Ukr. cf. pux, m. ‘fluff; pux- kyj, adj. ‘soft, tender; Srb. puh, m. ‘breath, blow, bombast'; Slovene puhati, inf. ‘blow’; Srb. cf. pušiti, inf. ‘smoke — a pipe'; Ukr. puxnuty, inf. ‘swell
12556:pauslos (pausros) (ph-) ‘trivial, vain, de- spicable, worthless'. Cf. pauros & paus- above, and see next Gk. (ambig.) paüros (small, fr. *pauros or fr. *pausros); Lat. paullus, adj. ‘tiny’; Gk. (?) paüla, f. (“ pause, stoppage’. Cf. paustos below); Ir. uaill, adj. ‘vain, proud’; f. ‘a small quantity; pride; Go. cf. ga-fáurs, adj. “modest, re- strained; OCz. püchly, Cz. pouchly “empty”; Slovene puhel, adj. (empty, hollow" beside puhor, m. ‘bubble’;
13781:pūros, om, is ‘wheat, spelt’. WP II, 83 Skt. pürah, -am, -à ‘unleavened oilcake’; Hind. püri, f. ‘kind of cake’; Myc. & Gk. pürós, m. ‘wheat’; OCS pyro, n. (“bran? or “millet?); Srb. pir, m. ‘spelt’; Cz. pýr, m. “couch-grass; R pyrèj, m. id.; Li. púras, m. id. (& “wheat- grain”); purai, pl. ‘wheat’; Latv. püris, usu. pl. püri *winter-wheat. (N.B. The Finn. LW puuro ‘porridge’ derives from a type putro-, q.v.)
13817:putlos (phutlo-) “fizzy, frothy, puffy, windy, airy, vacuous’. Cf. putos, pūst- Arm. (ambig.) pul, gs: plo, o-st. (crumbling, tottering’, cf. pül- (3)); Gk. cf. phusalís, f. “bladder”; phüsalos, m. toad"; Li. putlüs, adj. ‘puffy, flabby, weak’; Latv. cf. puteklis, s. ‘dust’?
13826:putros (or putlos?) (1) ‘son, offspring’. (R. Kent: putlo-). (Skt. also f.) Skt. putráh, m. “son, child, young animal’; putrih, f. “daughter”; Av. puOro, m. ‘son’; Ober pura; id.; Per. pusar, id.; Oss. fírt, furt, id.; Osc. puklu-, id.; Lat. cf. putillus, a, mf. ‘little boy, little gir: Faliscan: putellio (queried: infant); Lat. (doubtfully) pullus, gs: -i, m. (chick, cub’, if fr. *putlo- or *puslo-, cf. pù- sos); OBrit. cf. (?) uir (grandson, descendant, if fr. *putrio-). Cf. poutos, puta
13828:putros (phutros) (3) “blow, gust, gale, fury’. Cf. puskoó, puso, putlos, etc. Oss. (ambig.) furd, ford, s. (torrent, sea'. Cf. putlo-); Icel. fuóra, v. ‘blaze’. (Isophonic: (2) Ir. othar, adj. ‘sick, ill)
=== SYN son
2425:2.25. ‘Boy. 1. Grk. rats, gen. rar- d6s (fr. *rafid-) ‘boy, girl, child’, NG matot ‘child’ (fr. dim. zaidiov), Lat. puer ‘boy’, whence puella ‘girl’ : Skt. putra-, Av. puéra- ‘son’, Osc. puklum ‘filium’, Pael. puclois ‘pueris’, Skt. pota- ‘young of an animal’, Grk. zaipos ‘little’, Lat. putus ‘boy’ (rare), pusillus ‘very small’, Goth. fawaz ‘few’, etc., all fr. the notion of ‘small’. Walde-P. 2.75 ff. Ernout-M. 782, 790.
2873:Skt.  stinu-, putra- duhitar-
2888:5. Skt. putra-, very common beside stinu-, Av. puéra-, OPers. puéra-, the
2889:reg. Iran. word : Osc. puklum ‘filium’ Pael. puclois ‘pueris’, Lat. puer ‘boy’, Grk. wats, etc. (2.25). Walde-P. 2.75 ff.
3071:irt, ‘son’s son’, son’s daughter’, and dauhitra-, ddauhitri- ‘daughter’s son, daughter’s daughter’, derivs. of putra- ‘son’, duhitar- ‘daughter’.
3187:Skt. bhrdtriya-, bhratrzya-, bhratuh putra- (a); svasriya- (b) Av. bratruya- (a)
```


## [2026-09-14T00:55:44.298Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BQT پسر\"; grep -n \"پسر\" BQT_v1_pages.txt | head -10; echo \"=== BQT آبستن\"; grep -n \"آبستن\" BQT_v1_pages.txt | head -10"
}
```


### [2026-09-14T00:55:44.362Z] TOOL RESULT

```
=== BQT پسر
187:نیای دار یوش‌است‌وارشامه پسراوست. داریوش درسنکتيشتة بفستان (بیستون)
201:یس از مر گ کمبوجیه پسر کورش که داربوش پپادشاهی رسید » سرزمینی که
913:کتیبه‌های هخامنشی بکاررفته» مطا بقاست [پارسی باستان: -012600(پسر)»
935:(شایور ع پسرشاه: بعنوان علم). نمو نةٌ هر يك |زین لپجه‌هادر کتا بهای‌زر تشتی
3008:مثال؟- «ریونیز» بروزن پیش‌خیز... نام‌پسر کیکاوس وداماد طوس
3010:بردست فرود پسر سیأوخش .>
5130:و پهلوی منسوب است به «پهلو» که پدرپاری و پسرسام بن نوح
5575:دیگر واو ساکن است که بمعنیکاف تصفیرنیز میا بدهمچو «پسروه
5589:بر ما نظری نمیکند ای پسر !دیاچ مزاف له با
5725:است همچوهپسرله » و «دخترل» *و واو سا کن‌هه‌چوه پسرو*و «دختروه!
=== BQT آبستن
6185:و یکر تاك مخفف آبستن باشد ۱ . #
7026:کویند ا کر زنی آبستن نشود فدری ازآن بضود
7027:بر‌گیرد آبستن کردد ۴ .
7862:(۱) چب ۲, چش : آبستن.
12639:باه دهد » اگر زن آبستن بخود ب رگیرد بچه
13361:آن بیاراست» بجهت دانتنآبستنی بخورد زلی
13363:البته آبستن باشد والا نباشد . ۶
15863:بر کیرد هر کز آبستن نگرده .
28315:و زنان آبستن را این‌حال بیشتر دست دهد .
```


## [2026-09-14T00:55:45.719Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== ARY index\"; grep -n -i \"PESAR\\|PUS\\|POUR\\|PUR\\b\" incoming/ARY/ARY_latin_index_pages.txt | head -15"
}
```


### [2026-09-14T00:55:45.795Z] TOOL RESULT

```
=== ARY index
690:ne CTA Sled pour Hla! plaid eS tila) OWL Doerio cal eel dln yg
961:22 Dba I SUS ey 5S Pus El; 92.2 5 LJ WME AL Gla doe S9y
1341:Lasgly gel UT Layla gant leas PAFEN sls yPUST (S,luls » BOUFFEE
1357:ABANN: HOLD IRISH) pS 5332) API, APUS (OLD PERSIAN) gal go,
3846:ONIONS: (BUSS) 130 PUSS “OS SWEDISH) 4 y+
4333:DELAMARRE: (PUR) 232 PUR, PIVON GREEK) gly
4335:BUCK: (FIRE) 71-72 PUR (ERENCH) i
4338:(PURE) 486, (FIRE) 214 PUR H(RUMANIAN) ley y
4542:GREEK) gly, PUR (KURDISH) 59,
4543:PLERES, PLETHEIN, POLUS PUR HBALUCHI) gp de
4544:PLENUS, PLERE LATIN) 3 PUR AFGHAND) (4) gl
4572:FARN .(OLD HIGH GERMAN) x5 git PUR, PURR (PAHLAVI) 53h
4573:FEARN (OLD ENGLISH) aS gS! PUR (KURDISH) 52,5
4574:SPARNAS (LITHUANIAN) gi PUR ABALUCHI) gx Sh
4575:SPARNS (LATVIAN) (33) er) PUR (AFGHANI) (3%) pat
```


## [2026-09-14T00:55:51.497Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== ARY abestan ctx\"; sed -n '1350,1365p' incoming/ARY/ARY_latin_index_pages.txt; echo \"=== ARY pages آبستن\"; grep -n \"آبستن\" incoming/ARY/ARY_pages.txt | head -5; echo \"=== ARY pages پسر\"; grep -n \"پسر\" incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-14T00:55:51.583Z] TOOL RESULT

```
=== ARY abestan ctx
hagas
[pdf page 50]
Fe . ins
ats
|
[ware tees ty ar |
APE (OLD PRUSSIAN) AS 3. ‘AP, APAM AVESTAN) gles)
ABANN: HOLD IRISH) pS 5332) API, APUS (OLD PERSIAN) gal go,
AB, AP (PAHLAVI) 6 shy,
REFERENCES eh ‘AY, DjYRAV KURDISH) 3,5
POKORNY: . 51-52 Ae, APA (SANSKRIT) 2 Sie
MACKENZIE: (WATER) 139 APIA GREEK) gli
BUCK: (WATER) 34-35 AMNIS LATIN) 3
MALLORY 129 EAV APRENCH) si
1 igbG ob, UPE A(LITHUANIAN) gigs
ro sfaseos al cai UPE ALATVIAN) (3) is)
=== ARY pages آبستن
=== ARY pages پسر
527:زبان واحد خود از عبری ناشی شده است. همچنین او نیز معتقد بود که پس از توفان نوح» سه پسر او
1030:داشت. اولی هکوبا (180178۸]) برد که برایش نوزده پسر زائید. دومی لائوتو (۸07730]) بود.
1031:که برایش دو پسر زایید.
1067:نمونه‌ی خوبی از این مخاطرات است). لذا رسم بر این بود که مردان و پسران را بکشند و زن‌ها و
1075:پسر بچه‌ها (مثلاً استیاناکس ۸7۸ ۸87۷) را از دم تیغ گذراندند.
```


## [2026-09-14T00:55:55.097Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"PUTRA\\|PUSAR\\|PUTHRA\\|PUCA\\|PAIS \\|PAIDOS\\|PAUPER\\|FAWAZ\" incoming/ARY/ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-14T00:55:55.150Z] TOOL RESULT

```
4816:PUTHRA — (OLD PERSIAN) je Jk PUTHRO A(AVESTAN) glee 3)
4819:OLD CHURCH SLAVIC) 4S 59%! PUS, PUSAR PAHLAVI) 5 ay
4824:PAOTR (4LEX(BRETON) 5 4 PUTRAS, PUSRA:(SANSKRIT) cy Suits
```


## [2026-09-14T00:55:57.054Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '4795,4840p' incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-09-14T00:55:57.097Z] TOOL RESULT

```
PRS, PRSA (CZECH) Soe PISTAN AFGHAN) (y=) gs!
PRSA * (BOHEMIAN) goa » STANAS SANSKRIT) < Ste
PRSIA SLOVAK) ,S\jhel STIN ARMENIAN) «51
SPENYS (LITHUANIAN) .\ 3 STENION (GREEK) gb.»
PUPS LATVIAN) (3) i) PECTUS (LATIN) ga
SPENIS — :(OLD PRUSSIAN) HS 3.4 POITRINE, PIS :(FRENCH) 413
SINE HOLD IRISH) 24S 543 2! PECHO (SPANISH) glilysh

PETTO s(ITALIAN) .g\dtu!
‘REFERENCES beth PIEPT ARUMANIAN) gles,
Poko =SO*=~CS~*~S~«S PEITO PORTUGUESE) i y
DELAMARRE: (OLD SCANDINAVIAN) gS hn!
(POITRINE, PIS) 108 SPENI
MACKENZIE: (BREAST) 105 :(OLD HIGH GERMAN) AS lst
BUCK: 44 SPENE, SPUNNI
AMINDAROV: (BREAST) 194 SPAN-FERKEL (GERMAN) gJT
ia) [eb ob, HOLD ENGLISH) 4S 5&1
‘SPANE, SPANU
eatlooh
gf ole 31) Obj 92 PIS rss me
hp yet Se i GUAT Obj 92 SPAN-FERKEL (5031) mt
PUTHRA — (OLD PERSIAN) je Jk PUTHRO A(AVESTAN) glee 3)
[pdf page 168]
I |
OLD CHURCH SLAVIC) 4S 59%! PUS, PUSAR PAHLAVI) 5 ay
| PUTA, PITA (OSSETIC) gos) |
PITA (RUSSIAN) «gy PUKLUM, FURT, FIRT
POTYTIS LITHUANIAN) «g\ 3) PISIR (KURDISH) 62,5
PUISIS ALATVIAN) (3) Gig) PUSAGH HBALUCHI) go yh \
PAOTR (4LEX(BRETON) 5 4 PUTRAS, PUSRA:(SANSKRIT) cy Suits
PAIS, PAUROS GREEK) Sip.
‘REFERENCES [RY a PUER, PUTUS, PAUCI :(LATIN) 539
POKORNY, ——SSsS*~S~S~S«S FAWAL GOTHIC) S35
‘BARNHART: (FEW) 379 FAR :(OLD SCANDINAVIAN) 5 (54th!
‘MACKENZIE: (SON) 133 PILTR — (4jL!}(OLD NORSE) oS e335
BUCK: 7 FA HOLD SAXON) oy gy-Sts
ONIONS: (FEW) 353 FE (OLD FRISIAN) eS 5335
SKEAT: (PEU) 756 FAO (OLD HIGH GERMAN) op gil
RAMAT: a FEA, HOLD ENGLISH) of gJ&:
Fd ight oby FEAWE
POJKE (AUEX(SWEDISH) 5a yo
, Jeeta
sa piins Se SS gy} SUUDL 12 0389 yp! ne
Sa Ss Glee M9 S33 BO yp 0sde lyay) ye Glass ate 2 edly ott ome
wf
PUSHT - (AFGHANI) (3%) iil s(AVESTAN) gles!
```


## [2026-09-14T00:56:07.112Z] TOOL CALL #30: Bash

```json
{
 "command": "sed -n '1,60p' /home/sfmqrb/git/rishe/tools/fetch_source.py"
}
```


### [2026-09-14T00:56:07.159Z] TOOL RESULT

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


## [2026-09-14T00:56:17.607Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%82w-\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%B3%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%A8%D8%B3%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%88%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%BA%D9%81%D9%88%D8%B1\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 406, root Pou, PIE *peh2w- / Persian pesar, abestan, pur, faghfur\"; done"
}
```


### [2026-09-14T00:56:21.653Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%82w-
/home/sfmqrb/git/rishe/data/verification/sources/web/6ac1f2e84b1b7a07.txt
### https://en.wiktionary.org/wiki/%D9%BE%D8%B3%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/9a936328c689df5f.txt
### https://en.wiktionary.org/wiki/%D8%A2%D8%A8%D8%B3%D8%AA%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/2805486a08944c17.txt
### https://en.wiktionary.org/wiki/%D9%BE%D9%88%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/ff652b3a9e61958b.txt
### https://en.wiktionary.org/wiki/%D9%81%D8%BA%D9%81%D9%88%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/f8695d83bae2aec5.txt
```


## [2026-09-14T00:56:23.771Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== PIE peh2w\"; head -c 3000 6ac1f2e84b1b7a07.txt; "
}
```


### [2026-09-14T00:56:23.810Z] TOOL RESULT

```
=== PIE peh2w
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%82w-
FETCHED: 2026-09-14T00:56:19Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/peh₂w- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/peh₂w- - Wiktionary, the free dictionary 

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

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Proto-Indo-European 

 Toggle Proto-Indo-European subsection 

 1.1 
 Root 

 1.1.1 
 Derived terms 

 1.2 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ peh₂w- 

 Add languages 

 Reconstruction 

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
 Get shortened URL 

 Print/export

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

 Root
 [ edit ] 

 *peh₂w- 

 few , little 

 smallness 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *peh₂w- (63 c, 0 e) 

 *peh₂u-kos [ 1 ] 
 Proto-Italic: *paukos [ 2 ] ( see there for further descendants )

 *péh₂u-ros [ 3 ] [ 4 ] [ 1 ] 
 Proto-Hellenic: *pā́uros 
 Ancient Greek: παῦρος ( paûros ) , φαῦλος ( phaûlos ) 
 Greek: φαύλος ( fávlos ) 

 Proto-Italic: *pauros , *paurelos 
 Latin: parvus ( see there for further descendants ), paullus / paulus 

 *péh₂w-ids [ 5 ] 
 Proto-Hellenic: *pā́wits ( see there for further descendants )

 *peh₂w(o)- p(o)rh₃os ( “ providing little ” ) [ 6 ] 
 Proto-Italic: *pawoparos 
 Latin: pauper ( see there for further descendants )

 *ph₂w-er-os [ 7 ] 
 Proto-Celtic: *ɸuweros 
 Proto-Brythonic: *uwer 
 Middle Welsh: wyr 
 Welsh: ŵyr ( “ grandson, grandchild ” ) 

 Proto-Italic: *puweros 
 Latin: puer ( see there for further descendants )

 *ph₂w-os 
 Proto-Germanic: *fawaz ( see there for further descendants )

 Unsorted formations 

 Albanian:
 Proto-Albanian: 
 Albanian: palo- 

 Armenian:
 Old Armenian: փոքր ( pʻokʻr ) ( probably an expressive formation ) [ 8 ] [ 9 ] [ 10 ] 
 Armenian: փոքր ( pʻokʻr ) 

 Proto-Balto-Slavic: *putas , [ 11 ] *pautas ( “ little, young of a bird ” ) 
 ⇒ Latgalian: putnys ( “ bird ” ) 

 ⇒ Latvian: putns ( “ bir
```


## [2026-09-14T00:56:28.379Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '/Unsorted formations/,/References/p' 6ac1f2e84b1b7a07.txt | head -60"
}
```


### [2026-09-14T00:56:29.592Z] TOOL RESULT

```
 Unsorted formations 

 Albanian:
 Proto-Albanian: 
 Albanian: palo- 

 Armenian:
 Old Armenian: փոքր ( pʻokʻr ) ( probably an expressive formation ) [ 8 ] [ 9 ] [ 10 ] 
 Armenian: փոքր ( pʻokʻr ) 

 Proto-Balto-Slavic: *putas , [ 11 ] *pautas ( “ little, young of a bird ” ) 
 ⇒ Latgalian: putnys ( “ bird ” ) 

 ⇒ Latvian: putns ( “ bird ” ) 

 ⇒ Lithuanian: putýtis ( “ chick ” ) 

 Sudovian: paud ( “ bird ” ) 

 Proto-Slavic: *pъtъ , *putъ 
 ⇒ Proto-Slavic: *pъtakъ ( “ bird ” ) ( see there for further descendants ), *pъtica ( “ bird ” ) ( see there for further descendants ), *pъtъka / *putъka ( “ fowl, duck ” ) 

 Proto-Indo-Iranian: *putrás ( see there for further descendants )

 Proto-Indo-Iranian: 
 Sanskrit: पोत ( pota , “ young of an animal ” ) ( see there for further descendants )

 Dacian: per ( “ son ” ) 

 References
```


## [2026-09-14T00:56:34.273Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 9a936328c689df5f 2805486a08944c17 ff652b3a9e61958b f8695d83bae2aec5; do echo \"##### $f\"; sed -n '/Etymology/,/^ *Pronunciation/p' $f | head -45; done"
}
```


### [2026-09-14T00:56:35.206Z] TOOL RESULT

```
##### 9a936328c689df5f
sed: can't read 9a936328c689df5f: No such file or directory
##### 2805486a08944c17
sed: can't read 2805486a08944c17: No such file or directory
##### ff652b3a9e61958b
sed: can't read ff652b3a9e61958b: No such file or directory
##### f8695d83bae2aec5
sed: can't read f8695d83bae2aec5: No such file or directory
```


## [2026-09-14T00:56:37.333Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 9a936328c689df5f.txt 2805486a08944c17.txt ff652b3a9e61958b.txt f8695d83bae2aec5.txt; do echo \"##### $f\"; sed -n '/Etymology/,/Pronunciation/p' \"$f\" | head -40; done"
}
```


### [2026-09-14T00:56:38.407Z] TOOL RESULT

```
##### 9a936328c689df5f.txt
 Etymology 

 1.3 
 Pronunciation 
 Etymology 

 2.2 
 Pronunciation 
 Etymology
 [ edit ] 

 Inherited from Middle Persian [Book Pahlavi needed] ( BREl ) / [Book Pahlavi needed] ( pwsl /⁠pusar⁠/ , “ son ” ) , formed from 𐭡𐭥𐭤 ( pus [BRE] , “ son ” ) on the model of kinship term pairs such as [Book Pahlavi needed] ( AH ) , [script needed] ( blʾtl' /⁠brādar⁠/ ) . The Middle Persian [Term?] is in turn inherited from Old Persian 𐎱𐎢𐏂 ( p-u-ç /⁠puça⁠/ ) . Cognate of Sanskrit पुत्र ( putra ) .

 Pronunciation
 Etymology
 [ edit ] 

 Borrowed from Classical Persian پِسَر ( pisar ) , پُسَر ( pusar ) . Cognate of Sanskrit पुत्र ( putra ) . Doublet of پُوت ( pūt ) and پُتْر ( putr ) .

 Pronunciation
##### 2805486a08944c17.txt
 Etymology 

 2.3 
 Pronunciation 
 Etymology
 [ edit ] 

 From Middle Persian [script needed] ( ʾpwstn' /⁠ābustan, ābistan⁠/ ) , from [script needed] ( ʾpws /⁠ābus⁠/ , “ pregnant ” ) , from Proto-Iranian *āpuθra- ( “ pregnant ” ) , from *puθráh ( “ son ” ) , from Proto-Indo-Iranian *putrás ( “ boy; son ” ) , from Proto-Indo-European *putlós .

 Pronunciation
##### ff652b3a9e61958b.txt
 Etymology 

 1.2 
 Adjective 

 2 
 Pashto 

 Toggle Pashto subsection 

 2.1 
 Etymology 

 2.2 
 Noun 

 3 
 Persian 

 Toggle Persian subsection 

 3.1 
 Etymology 

 3.2 
 Pronunciation 
 Etymology 

 4.2 
 Pronunciation 
 Etymology
 [ edit ] 

 Borrowed from Sanskrit पूर ( pūra ) .

 Adjective
 [ edit ] 

 پور ( por ) 

##### f8695d83bae2aec5.txt
 Etymology 

 1.3 
 Pronunciation 
 Etymology
 [ edit ] 

 Borrowed from Sogdian 𐼱𐼲𐼾𐼰𐼴𐽀 ( βɣpʾwr /⁠βaγpūr⁠/ ) ; see there for further information.

 Pronunciation
```


## [2026-09-14T00:56:46.827Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n \"Persian\" -A 40 ff652b3a9e61958b.txt | sed -n '/^[0-9]*[-:] *Persian *$/,$p' | head -60; echo \"=== raw hunt\"; grep -n \"puhr\\|Proto-Iranian\\|Middle Persian\" ff652b3a9e61958b.txt | head"
}
```


### [2026-09-14T00:56:47.920Z] TOOL RESULT

```
79: Persian 
80-
81: Toggle Persian subsection 
82-
83- 3.1 
84- Etymology 
85-
86- 3.2 
87- Pronunciation 
88-
89- 3.3 
90- Noun 
91-
92- 3.4 
93- Noun 
94-
95- 3.4.1 
96- Synonyms 
97-
98- 3.5 
99- Further reading 
100-
101- 4 
102- Urdu 
103-
104- Toggle Urdu subsection 
105-
106- 4.1 
107- Etymology 
108-
109- 4.2 
110- Pronunciation 
111-
112- 4.3 
113- Noun 
114-
115- Toggle the table of contents 
116-
117- پور 
118-
119- 11 languages 
120-
121- বাংলা 
--
217: Persian
218- [ edit ] 
219-
220- Etymology
221- [ edit ] 
222-
223- Borrowed from Bactrian πορο ( poro ) , πουρο ( pouro , “ son ” ) , from Proto-Iranian *puθráh . Compare Sogdian [script needed] ( puric , “ lady ” ) , also a Bactrian borrowing. Akin to Avestan 𐬞𐬎𐬚𐬭𐬀 ( puθra ) , Parthian 𐭁𐭓𐭉 ( BRY /⁠puhr⁠/ ) . Previously considered a Parthian borrowing.
224-
225- Pronunciation
226- [ edit ] 
227-
228: ( Classical Persian ) IPA ( key ) : /ˈpuːr/ 
229-
230- ( Dari, formal ) IPA ( key ) : [pʰuːɾ] 
231-
232- ( Dari, formal ) IPA ( key ) : [pʰuːɾ] 
=== raw hunt
223: Borrowed from Bactrian πορο ( poro ) , πουρο ( pouro , “ son ” ) , from Proto-Iranian *puθráh . Compare Sogdian [script needed] ( puric , “ lady ” ) , also a Bactrian borrowing. Akin to Avestan 𐬞𐬎𐬚𐬭𐬀 ( puθra ) , Parthian 𐭁𐭓𐭉 ( BRY /⁠puhr⁠/ ) . Previously considered a Parthian borrowing.
339: Persian terms derived from Proto-Iranian
```


## [2026-09-14T00:56:53.958Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor w in paraffin few poor poverty pony pupil puppet puppy encyclopedia pediatric; do python3 tools/fetch_source.py \"https://www.etymonline.com/word/$w\" --note \"page 406, root Pou/PIE *peh2w-: check $w\" >/dev/null; done; echo done"
}
```


### [2026-09-14T00:56:58.259Z] TOOL RESULT

```
done
```


## [2026-09-14T00:57:02.951Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 - <<'EOF'\nimport hashlib,os\nW=\"data/verification/sources/web\"\nfor w in [\"paraffin\",\"few\",\"poor\",\"poverty\",\"pony\",\"pupil\",\"puppet\",\"puppy\",\"encyclopedia\",\"pediatric\"]:\n    u=f\"https://www.etymonline.com/word/{w}\"\n    h=hashlib.sha1(u.encode()).hexdigest()[:16]\n    p=os.path.join(W,h+\".txt\")\n    t=open(p,encoding='utf-8').read()\n    i=t.find(w)\n    print(\"#####\",w,h,len(t))\n    # find the definition block\n    import re\n    m=re.search(r\"(?s)Advertisement(.{0,1800})\", t)\n    print((m.group(1) if m else t[:1500]).strip()[:1200])\n    print()\nEOF"
}
```


### [2026-09-14T00:57:04.096Z] TOOL RESULT

```
##### paraffin b09a8cde61d4a62d 7625
Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of paraffin 

 paraffin (n.) 

 colorless, tasteless fatty crystalline substance obtained from petroleum, etc., by 1832, from German Paraffin , coined c. 1830 by German chemist Karl von Reichenbach (1788-1869), who first obtained it as a waxy substance from wood tar, irregularly from Latin parum "not very, too little," which probably is related to parvus "little, small" (from PIE root *pau- (1) "few, little") + affinis "associated with" (see affinity ).

 So called "in reference to the unreactive nature of the substance" [Flood].

 In chemischer Hinsicht zeichnet sich das Paraffin durch eine merkwürdige Indifferenz aus; daher auch sein Name (von parum affinis 
 ).  [J.C. Poggendorff, 
 "Annalen der Physik und Chemie," Leipzig, 1832] 

 [ 
 From a chemical point of view, paraffin is characterized by a strange indifference; hence its name (from parum affinis 
 ). ] 

 The liquid form (originally paraffin oil ) Reichenbach called eupion , but this was the standard meaning of paraffin in English by 1860.
 also from 1838 

 Entries linking to paraffin 

 affinity

##### few d3ee5721762b67de 6565
Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of few 

 few (adj.) 

 Old English feawe (plural; contracted to fea ) "not many, a small number; seldom, even a little," from Proto-Germanic *fawaz (source also of Old Saxon fa , Old Frisian fe , Old High German fao , Old Norse far , Danish faa ), from PIE root *pau- (1) "few, little."

 Always plural in Old English, according to OED "on the analogy of the adverbial fela ," meaning "many." Phrase few and far between attested from 1660s. Unusual ironic use in quite a few "many" (1854), earlier a good few (1803).

 There is likewise another dialectical use of the word 
 few among them [i.e. "the Northern Counties"], seemingly tending to its total overthrow; for they are bold enough to say—
 "a good few," meaning 
 a good many . [Samuel Pegge, "Anecdotes of the English Language," London, 1803]

 few (n.) 

 "a small number of persons" (distinguished from the many ), c. 1300, fewe , from few (adj.).

 Never in the field of human conflict was so much owed by so many to so few. [Winston Churchill, 1940]
 also from c. 1300 

 Entries linking to few 

 fewness (n.)

##### poor 42f5218bf9842862 7764
Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of poor 

 poor (adj.) 

 c. 1200, "lacking money or resources, destitute of wealth; needy, indigent;" also "small, scanty," also voluntarily and deliberately, "devoid of possessions in conformity with Christian virtues," from Old French povre "poor, wretched, dispossessed; inadequate; weak, thin" (Modern French pauvre ), from Latin pauper "poor, not wealthy," from pre-Latin *pau-paros "producing little; getting little," a compound from the roots of paucus "little" (from PIE root *pau- (1) "few, little") and parare "to produce, bring forth" (from PIE root *pere- (1) "to produce, procure").

 It replaced Old English earm (from Proto-Germanic *arma- , which is of disputed origin). Late 13c. as "unfortunate, to be pitied or regretted." In contemptuous use, "morally inferior, miserable, wretched," by early 15c. Used figuratively ("spiritually poor") from early 14c. (to be poor in spirit is to be "spiritually humble"). Meaning "deficient in desirable or essential qualities" is from c. 1300. In reference to inhabited places from c. 1300; of soil, etc., from late 1

##### poverty aff8816c19b6beea 8863
Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of poverty 

 poverty (n.) 

 late 12c., poverte , "destitution, want, need or insufficiency of money or goods," from Old French poverte, povrete "poverty, misery, wretched condition" (Modern French pauvreté ), from Latin paupertatem (nominative paupertas ) "poverty," from pauper "poor" (see poor (adj.)).

 From early 13c. in reference to deliberate poverty as a Christian act. Figuratively from mid-14c., "dearth, scantiness;" of the spirit, "humility," from the Beatitudes.

 Seeing so much poverty everywhere makes me think that God is not rich. He gives the appearance of it, but I suspect some financial difficulties. [Victor Hugo, 
 "Les Misérables," 1862]

 Poverty line "estimated minimum income for maintaining the necessities of life" is attested from 1891; poverty trap "situation in which any gain in income is offset by a loss of state benefits" is from 1966; poverty-stricken "reduced to a state of poverty" is by 1778.

 Poverty is a strong word, stronger than 
 being poor ; 
 want is still stronger, indicating that one has not even the necessaries of lif

##### pony 27378f62bca15745 8459
Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of pony 

 pony (n.) 

 1650s, powny , "a very small horse" (less than 13 hands in height), from Scottish, apparently from obsolete French poulenet "little foal" (mid-15c.), diminutive of Old French poulain "foal," from Late Latin pullanus "young of an animal," from Latin pullus "young of a horse, fowl, etc." (from PIE root *pau- (1) "few, little") [Skeat's suggestion, still accepted]. Compare, from the same source, foal , filly , Sanskrit potah "a young animal," Greek pōlos "foal," secondarily also of other young animals; Latin pullus "young animal," Lithuanian putytis "young animal, young bird."

 A small horse, especially one of a small breed, as opposed to a colt or filly , words which indicate merely young horses. German, sensibly, indicates this animal by attaching a diminutive suffix to its word for "horse," which might yield Modern English *horslet . Modern French poney is a 19c. borrowing from English.

 The Shetland breed of ponies are stoutly built, active and hardy, with very full mane and tail, and of gentle, docile disposition. In western parts

##### pupil 1840780d5bec7665 7437
Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of pupil 

 pupil (n.1) 

 [student], late 14c., "orphan child, ward, person under the care of a guardian," from Old French pupille (14c.) and directly from Latin pupillus (fem. pupilla ) "orphan child, ward, minor," diminutive of pupus "boy" (fem. pupa "girl"), probably related to puer "child" (and thus probably from a suffixed form of PIE root *pau- (1) "few, little").

 Meaning "disciple, student youth or any person of either sex under the care of an instructor or tutor" is recorded by 1560s. Related: Pupillary; pupillarity; pupillage .
 also from late 14c. 

 pupil (n.2) 

 "center of the eye, orifice of the iris," early 15c. pupille (the word is in English in Latin form from late 14c.), from Old French pupille (14c.) and directly from Latin pupilla , originally "little girl-doll," diminutive of pupa "girl; doll" (see pupil (n.1)).

 The eye region was so called from the tiny image one sees of oneself reflected in the eye of another. Greek used a single word, korē (literally "girl;" see Kore ), to mean both "doll" and "pupil of the eye;" and compare obso

##### puppet f62e30a97393ef96 6528
Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of puppet 

 puppet (n.) 

 1530s, "doll or little figure of a person moved by strings or wires" (later applied to puppets in glove form), a later form of Middle English popet "doll" (c. 1300; compare poppet ), from Old French popette "little doll, puppet," diminutive of popee "doll, puppet" (13c., Modern French poupée ), from Vulgar Latin *puppa , from Latin pupa "girl; doll" (see pupil (n.1)).

 The metaphoric extension to "one actuated by the will of another, one whose actions are manipulated by another" is recorded from 1540s (as poppet ). Puppet show "dramatic performance with puppets" is attested from 1650s, earlier puppet-play (1550s). Puppet government , one managed by the will of another power, is attested from 1884 (in reference to Egypt). Puppet-master "manager of a puppet-show" is by 1630s.
 also from 1530s 

 Entries linking to puppet 

 poppet (n.) 

 "small human figure used in witchcraft and sorcery," c. 1300, popet , early form of puppet (n.). Meaning "small or dainty person" is recorded from late 14c.; later a term of endearment (18c.) but 

##### puppy 2f6628ada4fa1498 6503
Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of puppy 

 puppy (n.) 

 late 15c., "woman's small pet dog," a word of uncertain origin but likely to be from French poupée "doll, toy" (see puppet ). "A little dog appears to have been called puppy because petted as a doll or puppet" [Century Dictionary].

 The meaning shifted from "toy dog" to "young dog" (1590s), replacing native whelp . In early use in English the words puppet and puppy were not always distinguished. The word also was used from about that time in the contemptuous sense of "vain or silly young man."

 Puppy-dog is attested by 1590s (in Shakespeare, puppi-dogges ). Puppy love "juvenile infatuation" is from 1823. Puppy fat "excessive fat on a child or adolescent" is by 1913 (in reference to young dogs by 1894).
 also from late 15c. 

 Entries linking to puppy 

 puppet (n.) 

 1530s, "doll or little figure of a person moved by strings or wires" (later applied to puppets in glove form), a later form of Middle English popet "doll" (c. 1300; compare poppet ), from Old French popette "little doll, puppet," diminutive of popee "doll, puppet" (1

##### encyclopedia 16b7df371b53cb6f 7141
Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of encyclopedia 

 encyclopedia (n.) 

 1530s, "general course of instruction," from Modern Latin encyclopaedia (c. 1500), thought to be a false reading by Latin authors of Greek enkyklios paideia taken as "general education," but literally "training in a circle," i.e. the "circle" of arts and sciences, the essentials of a liberal education; from enkyklios "circular," also "general" (from en "in;" see in + kyklos "circle;" see cycle (n.)) + paideia "education, child-rearing," from pais (genitive paidos ) "child" (see pedo- ).

 The first encyclopedias were Latin; Cato the Censor compiled one (c. 185 B.C.E.), now lost. They were summaries of learning intended for general instruction, the "cycle of learning" proper to a free man and embodied in the seven liberal arts.

 The modern sense of "reference work arranged alphabetically" is from 1640s, often applied specifically to the French Encyclopédie ou Dictionnaire raisonné des Sciences, des Arts, et des Métiers (1751-65). Related: Encyclopedist .
 also from 1530s 

 Entries linking to encyclopedia 

 cycle (n.)

##### pediatric c0b9162b6008c3bf 5745
Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of pediatric 

 pediatric (adj.) 

 "of or pertaining to the medical care or diseases of children," 1849, from Latinized form of Greek paid- , stem of pais "child" (see pedo- ) + -iatric .
 also from 1849 

 Entries linking to pediatric 

 paediatric (adj.) 

 see pediatric ; also see pedo- , æ (1).

 pediatrician (n.) 

 "specialist or expert in pediatrics," 1884, from pediatric + -ian .

 pediatrics 
 -iatric 
 pedo- 
 See All Related Words (5) 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 fantasy 

 early 14c., "illusory appearance," from Old French fantaisie, phantasie "vision, imagination" (14c.), from Latin phantasia, from Greek phantasia "power of imagination; appearance, image, perception," from phantazesthai "picture to oneself," from phantos "visible," from phainestha

 rhinoceros 

 "ungainly quadruped having tough, thick skin and usually one or two horns on the snout," once widespread but now limited to Africa and South Asia, c. 1300, rinoceros, "a rhinoceros," als
```


## [2026-09-14T00:57:19.129Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%B1%D8%A7%D9%81%DB%8C%D9%86/\" --note \"page 406 node 8: Persian پارافین in Mo'in/Dehkhoda\" ; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/paraffin\" --note \"page 406 node 9: English paraffin from German\""
}
```


## [2026-09-14T00:57:20.531Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MFL\"; ls incoming/MFL/ 2>/dev/null; echo \"=== KLN paraffin\"; grep -n -i \"paraffin\" KLN_1966.txt | head -5; echo \"=== SKT few/pony\"; grep -n -i \"^few\\|F. Few\\|pony\" SKT.txt | head -8"
}
```


### [2026-09-14T00:57:22.349Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/64ae3504c04952b0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/257559411fe2d3fa.txt
```


### [2026-09-14T00:57:22.427Z] TOOL RESULT

```
=== MFL
MFL_ia_galaxy_ub2007.pdf
=== KLN paraffin
1856:affine,  n.,  a  relative  by  marriage  (obsoi.)  —  OF. afftn,  fr.  L.  affinis,  ‘neighboring,  related  by  mar¬ riage’,  lit.  ‘bordering  on’,  fr.  ad-  and  finis,  ‘bor¬ der,  end’.  See  fine  ‘end’,  and  cp.  the  second element  in  chromaffin,  paraffin.
7581:as  in  cacochroia.  —  Fr.  Gk.  /poi&,  ‘color’,  which is  rel.  to  /pcopia,  ‘color’.  See  chrome  and  cp.  the second  dement  in  dischroa,  Xanthochroi. -chroic,  combining  form  meaning  ‘colored’,  as  in erythrochroic.  —  Formed  with  suff.  -ic  fr.  Gk. /poia,  ‘color’.  See  -chroia. chroma,  n.,  the  quality  or  intensity  of  a  color.  — Gk.  /p£Sp.a,  ‘color’.  See  chrome, chromaffin,  adj.,  having  affinity  for  chromium salts.  —  A  hybrid  coined  fr.  Gk.  /pcopta,  ‘color’, and  L.  off  mis,  ‘related’.  See  chrome  and  affinity and  cp.  paraffin.
27272:paradoxy,  n.,  a  paradox;  paradoxical  quality.  — Gk.  TtapaSo^ta,  ‘marvelousness’,  fr.  TtapdSoi;oe. See  prec  word  and  -y  (representing  Gk.  -ia). paraffin,  n.  —  Lit.,  ‘of  small  affinity’,  coined  by the  German  chemist  Karl  von  Reichenbach (1788-1869)  in  1830  fr.  L.  par(um),  ‘little’,  and affinis,  ‘connected  with,  related  to’;  so  called by  him  because  of  its  comparative  lack  of  chem¬ ical  affinity.  L.  parum  is  cogn.  with  parvus, ‘small’, paucus,  ‘little’,  Gk.  itaupog,  ‘small’;  see paucity.  For  the  etymology  of  L.  affinis  see  affine, paraform,  n.,  a  white  powder  (chem.  ) —  Abbre¬ viation  of  paraformaldehyde.  See  para-,  ‘beside’, and  formaldehyde.
=== SKT few/pony
7356:Galloway.    •    nag,  pony.    (Scotland.)
8377:lB»ab.(E.)  M.E-Aiirm.  A.S.y(^dr*7i, itobana^loeL  harmr.  gitct.  Dan. ,  wiath.  Swcd.  hami,  anger,  giicl, 'iw,  £ricf.  KuM.  /mm/,  hlianie ;  ^kl. ,  XoC..  (rora  pnJM.  to  be  weary.  (^ if.)  Der  harm,  verb. pony,  concord.  ^F.  -  U  *  Gk.) ■f.  —  F.  Aanfi«»M.  —  L.  Aar- tk.  ifttovia,  a  joint,  proportimi, ^  Gl  ifi*^,  a  joining.  —  Gk. ftt  iVAK) BMB :  sec  Iron.
14382:Pony.  (C-)  Gad.  fmUdJk,  a  little hone,  a   pony.     Also  vulgar   Iri>h  /cw,
18160:spunk,  tii.dcr;  a  match.  &park.  spirit, mettle.  (C.-I.— Gk.)  Grig.  '  tinder. '- Gael,  and  Irisli  tpouc^  si>oiiyc,  sponyy  wood, tinder.  *•!>.  tpon^ia  (above).
```


## [2026-09-14T00:57:31.225Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== abadis parafin\"; grep -n \"پارافین\" 64ae3504c04952b0.txt | head -20; echo; echo \"=== wikt paraffin etym\"; sed -n '/Etymology/,/Noun/p' 257559411fe2d3fa.txt | head -30"
}
```


### [2026-09-14T00:57:32.330Z] TOOL RESULT

```
=== abadis parafin
4:TITLE: پارافین - معنی در دیکشنری آبادیس
6:پارافین - معنی در دیکشنری آبادیس 
10: پارافین
20: پارافین. ( فرانسوی ، اِ ) مادّه جامد و سفید که از الواح «شیست » قیری گیرند. 
25:( اسم ) جسمی است جامد و سفید که از سرد کردن ناگهانی روغنهای سنگین بدست میاید و در حدود ۴٠ درجه گداخته میشود و مخصوصا عایق خوبی برای الکتریسیته است . در شمع سازی و تهی. ورنی ها نیز استعمال میشود. پارافین مایع در پزشکی بعنوان مسهل بکار میرود .
30: [ فر. ] ( اِ. )جسمی است جامد و سفید که از سرد کردن ناگهانی روغن های سنگین به دست می آید. در شمع سازی و تهیة ورنی ها استعمال می شود. پارافین مایع در پزشکی به عنوان مسهل به کار می رود. 
38: در شیمی، پارافین ( به انگلیسی: paraffin ) نامی عمومی برای آلکان های با فرمول شیمیایی CnH۲n+2 است. واکس پارافین اشاره به پارافین جامد با n=۲۰–۴۰ دارد. پارافین ماده ای نفتی است در بازار به دو شکل مایع یا جامد یا ژله ای یافت می شود که نوع ژله و جامد آن برای تولید انواع شمع کاربرد دارد و از نوع مایع برای مصارف صنعتی استفاده می شود. مادّهٔ جامد و سفید که از الواح شیست قیری می گیرند. 
39:روغن پارافین در قرن نوزدهم میلادی به وسیله دانشمندی آلمانی بنام کارل فون ریچنباخ یافت شد. این اتفاق زمانی بود که وی در تلاش برای افزایش کارایی و تصفیه ترکیبات روغنی صنعت پتروشیمی فعالیت می کرد. به دلیل اینکه پارافین بسیار تمیز و مطمئن تر از روغن های رایج در صنعت شمع سازی می سوخت مورد استفاده قرار گرفت. کشف پارافین رونق جدیدی به تولید شمع، بسته بندی گوشت و صنایع تولید روغن در اوایل قرن بیستم میلادی داد. 
40: wiki: پارافین 
46: پارافین (paraffin)
47:نام متداول آلکان ها. اعضای مجموعۀ هیدروکربن هایی با فرمول عمومیCnH۲n+۲ اند. اعضای پایینی گروه، ازجمله متان (گاز طبیعی یا گاز مرداب)، گازی شکل اند. اعضای میانی، که عمدتاً مایع اند، پایۀ بنزین، کروزن (نفت سفید)، و روغن های روان ساز را تشکیل می دهند. حال آن که اعضای بالاتر (پارافین های جامد) جزو مواد اصلی پمادها و وسایل آرایشی اند. سوختی که با نام پرافین مصرف می شود، عموماً کروزناست. wikijoo: پارافین 
52: پارافین
56: پارافین؛ دارای بار و پاراف شده و پُر بار و بارگذاری شده 
69: کلمه ی پروفایل به لحاظ معنا و مفهوم نهفته در صندوقچه ی اسرارآمیز این کلیدواژه در قانون و قواعد ایجاد کلمات مرتبط با اصطلاح پُرُف کردن لباس و پاراف کردن و کلمه ی aprovied با ترجمه و برگردان آن به زبان فارسی به معنی تایید شدن و professional به معنی حرفه ای و همچنین کلمه ی بروفه و بَرف و بروفن و پارافین و پروفسور و پروفیل و. . . می باشد. 
79:کلمه ی دیگری که با این تعریف جور در می آید کلمه ی پارافین که در شمع سازی رایج می باشد به معنی دارای بار قابل مشاهده می باشد. 

=== wikt paraffin etym
 Etymology 

 1.3 
 Pronunciation 

 1.4 
 Noun 
 Etymology
 [ edit ] 

 From Latin paraffinum , from parum (too little) + affinis (related, affinity). Therefore low affinity or being chemically neutral .

 Pronunciation
 [ edit ] 

 ( Received Pronunciation ) IPA ( key ) : /ˈpæɹ.ə.fɪn/ 

 Audio ( Southern England ) : ( file ) 

 ( General American ) IPA ( key ) : /ˈpɛɹ.ə.fɪn/ 

 Noun
```


## [2026-09-14T00:57:41.117Z] TOOL CALL #42: Bash

```json
{
 "command": "pdftoppm -f 406 -l 406 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg406 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg406.png"
}
```


### [2026-09-14T00:57:43.147Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 63610 Sep 13 20:57 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg406.png
```


## [2026-09-14T00:57:45.104Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg406.png"
}
```


### [2026-09-14T00:57:45.760Z] TOOL RESULT

```

```


## [2026-09-14T00:57:45.757Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T00:57:59.910Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"puthra\\|pu&ra\\|pusar\\|pu%ra\\|puira\\|apus\\|abustan\\|āpuθ\" BQT_v1_pages.txt BQT_v1.txt 2>/dev/null | head -20"
}
```


### [2026-09-14T00:57:59.979Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:58:00.971Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; pdftotext -f 1 -l 5 incoming/MFL/MFL_ia_galaxy_ub2007.pdf - 2>/dev/null | head -40"
}
```


### [2026-09-14T00:58:01.949Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:58:09.265Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== فغفور\"; grep -n \"فغفور\" BQT_v2_pages.txt BQT_v1_pages.txt 2>/dev/null | head -5; echo \"=== پوره\"; grep -n \"پوره\" BQT_v1_pages.txt | head -5; echo \"=== شاهپور\"; grep -n \"شاهپور\\|شاپور\" BQT_v1_pages.txt | head -5"
}
```


### [2026-09-14T00:58:09.355Z] TOOL RESULT

```
=== فغفور
BQT_v1_pages.txt:17746:ممنی بروزن فغفور نیز درست است ٩‏ .
BQT_v2_pages.txt:1015:                                      ‫فغفور باشد ‪.‬‬              ‫جبا = بکر اول و ثالیبالفکشیده ‪,‬‬
BQT_v2_pages.txt:16991:‫اکر احیااً کاری ناصواب ازو سرزند اصلاح آن‬              ‫باسین وحا ورای بی‌نقطه بروزن فغفور ‪ -‬ویشهرا‬
BQT_v2_pages.txt:19142:    ‫ولام و سکون‌کاف » بمعتی چاليك است » و آن‬                 ‫‪ ,‬رخصت‬       ‫بروزن‌فغفوری‬    ‫ر یه ص‬   ‫دستو‬
BQT_v2_pages.txt:28274:                  ‫بدالجا رسد اکثر و افل‬             ‫زرقوری ‪ -‬با قاف بروژن فغفوری ‪۰‬‬
=== پوره
2760:لغات مشپوره آورده وازاشعار وامثال متقدمین استشهاد نموده‌است.
26731:۱- رگ:پوره
=== شاهپور
431:اردشم بایکان ( ۲۲ - ۲:۱ میلادی ) ۰ شاپور ( ۲۶۱ - ۲۷۲ ) ۰ نر سی
433:نقش رجب و نقش رستم وحاجی [باد و غار شاپور ( درفارس ) وطاق بستان
435:درمیان ایذیاسگنیشتهشاپور دز حاجی آباد و در کمبهٌ زرتشت بزر گتر و مهمتر
440:بلند در کعبه زرنشت در زیر سنگنشتة شاپور ودو سنکنبشتة بلند دیگر در نقش
14652:انگوری را نیز گفته‌اند - و نام عمة شاپور حم
```


## [2026-09-14T00:58:21.182Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%BE%D8%B3%D8%B1/\" --note \"page 406 node 2: Persian پسر in Dehkhoda/Mo'in\" >/dev/null; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%A2%D8%A8%D8%B3%D8%AA%D9%86/\" --note \"page 406 node 2: Persian آبستن in Dehkhoda/Mo'in\" >/dev/null; python3 - <<'EOF'\nimport hashlib,os,re\nW=\"data/verification/sources/web\"\nfor u in [\"https://abadis.ir/fatofa/%D9%BE%D8%B3%D8%B1/\",\"https://abadis.ir/fatofa/%D8%A2%D8%A8%D8%B3%D8%AA%D9%86/\"]:\n    h=hashlib.sha1(u.encode()).hexdigest()[:16]\n    t=open(os.path.join(W,h+\".txt\"),encoding='utf-8').read()\n    print(\"#####\",u,h)\n    for ln in t.split(\"\\n\")[:60]:\n        if len(ln.strip())>20: print(ln.strip()[:400])\n    print()\nEOF"
}
```


### [2026-09-14T00:58:27.055Z] TOOL RESULT

```
##### https://abadis.ir/fatofa/%D9%BE%D8%B3%D8%B1/ 8fdc1043b81fc3fd
URL: https://abadis.ir/fatofa/%D9%BE%D8%B3%D8%B1/
FETCHED: 2026-09-14T00:58:24Z
TITLE: پسر - معنی در دیکشنری آبادیس
پسر - معنی در دیکشنری آبادیس
مترادف پسر : ابن، پور، فرزند، صبی، طفل، غلام، نوباوه، نونهال
متضاد پسر : دختر، صبیه
معنی انگلیسی : son , boy , guy , bairn , chit , he , jack , jack- , lad , male , chap , fellow , dude , baby boy
پسر. [ پ ُ / پ َ س َ ] ( اِ ) پور. پوره. ( برهان قاطع ). پُس. فرزند نرینه. ریکا. ابن. ولد. ریمن ؟. ( برهان قاطع ). واد؟. ( برهان قاطع ). ابنم. ( منتهی الارب ) :
پسر بُد مر او را یکی خوبروی
هنرمند و همچون پدر نامجوی. فردوسی.
بخوردن نشستند با یکدگر
سیاوش پسر گشت و پیران پدر. فردوسی.
کنون کارگر شدکه بیکار گشت
پسر پیش چشم پدر خوار گشت. فردوسی.
پدر کشته گردد بدست پسر
پسر هم بدانسان بدست پدر. فردوسی.
چنین گفت مر زال را ای پسر
نگر تا نباشی جز از دادگر. فردوسی.
چو آگاه شد شاه کامد پسر
کلاه کئی برنهاده بسر. فردوسی.
خنک آن میر که در خانه آن بارخدای
پسر و دختر آن میر بود بنده و داه. فرخی.
پسر آن ملکی تو که بمردی بگشاد
ز عدن تا جروان و ز جروان تا ککری. فرخی.
سوی پسر کاکو و دیگران... نامه ها فرمودیم بقرار گرفتن این حالها بدین خوبی و نیکوئی. ( تاریخ بیهقی ). و پسر علی را و سرهنگ محسن را بمولتان فرستادند . ( تاریخ بیهقی چ ادیب ص 88 ). چون آنجا رسید یکسر تا سرای پسرم مسعود شود. ( تاریخ بیهقی ).
که پسر بود دو، مر آدم را
مِه قابیل و کهترش هابیل. ناصرخسرو.
فخر بر عالم ارواح وبر ارواح کند
آنکه در عالم اجسام چنینش پسر است. ناصرخسرو.
پسر گرچه کور است زین خانه دور
بچشم پدر شب چراغست و نور.
مذکار؛ زن که همه پسر زاید و عادتش پسر زادن باشد. ( منتهی الارب ). اذکار؛ پسر زادن. ( تاج المصادر بیهقی ) ( منتهی الارب ). مُذکِر؛ زن که همه پسر زاید. اِطابَة؛ پسران نیک سیرت زادن. دعوة؛ بپسری خواندن. اِستلاطَة؛ پسر خواندن غیری را. التیاط؛ پسر خواندن کسی را. ( منتهی الارب ). || فرزند. طفل. صَبی . جوان. غلام. خطاب است به کودکی یا جوانی خواه پسر متکلم باشد یا پسر دیگری :
جمله صید این جهانیم ای پسر
ما چو صعوه مرگ بر سان زغن. رودکی.
گفت خیز اکنون و ساز ره بسیج
رفت بایدت ای پسر ممغز تو هیچ. رودکی.
اُترور؛ پسر خرد. کودک. طِشَّة؛ پسر خردسال. ( منتهی الارب ). || یکی از سه اقنوم اهل تثلیث. عیسی. یکی از اقانیم ثلثه نزد نصاری. ابن. بیشتر بخوانید ...
پور، فرزندنرینه، مقابل دختر، پسران جمع
( اسم ) ۱- فرزند طفل جوان غلام . ۲- فرزنذ نریمه پور پس ابن ولد مقابل دختر . جمع: پسران . ۳- یکی از اقانیم سه گانه نزد عیسویان ابن . ۵-از ( پسر ) مطلق در تضاعیف جهانگشای جوینی غالبا مقصود ( شاهزاده ) است یعنی کسی که از اعقاب چنگیزخان باشد و ( پسران ) مرادف شاهزادگان است ( مقدم. جهانگشای جوینی ج ۲ ص ط. ) . یا پسر پسر . نوه سبط . یا پسر خواهر . خواهر زاده. یا پسر شوهر. ناپسری
(پِ سَ ) [ په . ] (اِ. ) ۱ - فرزند، طفل . ۲ - فرزند نرینه ، پور.

##### https://abadis.ir/fatofa/%D8%A2%D8%A8%D8%B3%D8%AA%D9%86/ 78c9aa1239315b28
URL: https://abadis.ir/fatofa/%D8%A2%D8%A8%D8%B3%D8%AA%D9%86/
FETCHED: 2026-09-14T00:58:26Z
TITLE: ابستن - معنی در دیکشنری آبادیس
ابستن - معنی در دیکشنری آبادیس
مترادف ابستن : ( آبستن ) آبسته، باردار، پابماه، حامله، دچار، دستخوش، پنهان، مخفی، نهان
متضاد ابستن : ( آبستن ) سترون، عقیم
معنی انگلیسی : expectant , gravid , pregnant , big
( آبستن ) آبستن. [ ب ِ ت َ ] ( ص ) هر مادینه از انسان و حیوان که بچه در شکم دارد. حامل. حامله. آبست. بارور. باردار. حُبْلی ̍. ( دهار ). بارگرفته. حمل برداشته :
پریچهره آبستن آمد ز مای
پسر زاد از این نامور کدخدای. فردوسی.
که ازبهر اوازدرِ بستن است
همان نیز بیمار و آبستن است. فردوسی.
گل آبستن از باد مانند مریم
هزاران پسر زاده از چارمادر. ناصرخسرو.
بلحسن آن معدن احسان کزو
دل بسخن گشته ست آبستنم. ناصرخسرو.
ای برادر گر عروس خوبت آبستن شده ست
اندر آن مدت که بودی غائب از نزد عروس
بر عروست بدگمان گشتن نباید بهر آنک
ماکیان چون نیک باشد خایه گیرد بی خروس. علی شطرنجی.
- آبستن بودن از کسی ؛ مجازاً رشوه نهانی ستده بودن از او.
- مثل آبستنان رفتن ؛ سخت بکاهلی و آهستگی راه پیمودن.
شب آبستن است ؛ وقوع حوادث تازه و غیرمنتظر ممکن است :
ترا خواسته گر ز بهر تن است
ببخش و بدان کاین شب آبستن است. فردوسی.
شب بدخواه را عقوبت زاد
شب شنودم که باشد آبستن. فرخی.
نبندد در برویم تا دهد در بزم خود جایم
نمیدانم چه زاید صبحدم آبستن است امشب. ظهیر فاریابی.
و عرب گوید: اللیل حُبْلی ̍ لست تدری ما تلد.
یک امشب را صبوری کرد باید
شب آبستن بود تا خود چه زاید. نظامی.
فریب جهان قصه روشن است
سحر تا چه زاید شب آبستن است. حافظ.
( آبستن ) ( صفت اسم ) ۱- حامله باردار ( انسان و حیوان و گیاه ) . یا مثل آبستنان رفتن . سخت بکاهلی و آهستگی راه رفتن . ۲- مخفی نهفته نهان . یا آبستن بودن . ۱ - حامله بودن باردار بودن ۲ - آبستن از کسی . رشو. نهانی از کسی گرفته بودن . یا شب آبستن است . وقوع حوادث تازه محتمل است .
حامله بارور زن یاحیوان ماده که بچه درشکم داشته باشد، باردار، آبست، آبسته، آبستان
( آبستن ) (بِ تَ ) (ص . ) = آبستان : ۱ - حامله ، باردار. ۲ - پنهان ، پوشیده . ،~شب ~ است (کن . ) وقوع حوادث تازه محتمل است .
```


## [2026-09-14T00:58:44.048Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN few\"; grep -n \"few,  adj\\|^few\\|few, adj\" KLN_1966.txt | head -3; echo \"=== KLN poor\"; grep -on \"poor,  adj\\.[^|]\\{0,320\\}\" KLN_1966.txt | head -2; echo \"=== KLN pony\"; grep -on \"pony,  n\\.[^|]\\{0,300\\}\" KLN_1966.txt | head -2; echo \"=== KLN puppet\"; grep -on \"puppet,  n\\.[^|]\\{0,300\\}\" KLN_1966.txt | head -2"
}
```


### [2026-09-14T00:58:45.221Z] TOOL RESULT

```
=== KLN few
14648:Derivatives:  fever,  tr.  and  intr.  v.,  fever-  ed,  adj., fever-ish,  adj.,  fever-ish-ly,  adv.,  fever-ish-ness, n.,  fever-ous,  adj.,  fever-ous-ly ,  adv. feverfew,  n.,  a  plant  of  the  aster  family.  OE. feferfuge,  fr.  Late  L.  febrifuga,  fr.  L.  febrifugia , lit.  ‘driving  fever  away’,  fr.  febris,  ‘fever’,  and fug-are,  ‘to  put  to  flight’,  fr.  fug-ere,  ‘to  flee’; so  called  for  its  alleged  medicinal  properties. See  prec.  word  and  fugitive  and  cp.  febrifuge, few,  adj.  —  ME.  fewe,  fr.  OE.  feawe ,  pi.  of  tea, rel.  to  OS.  fah,  ON.  far,  Dan.  faa.  Swed.  f&, ‘few’,  OFris.  fe,  OHG.  fao,  fo,  foh,  ‘little’, Goth,  fawai  (pi.),  ‘few’,  and  cogn.  with  L. paucus,  ‘few,  little'  (for  *pau-qos),  paul/us  (later spelled  paulus),  ‘little’  (for  *pauc-slo-s),  pauper, ‘poor’  (prob.  for  *pauc(o)-pars,  lit.  ‘he  who acquires  little'),  and  cogn.  with  Gk.  rraupoi;, ‘few,  little’,  no uc_,  gen.  nxiSo-,  ‘child’,  rhoXo;, ‘foal’,  L.  puber,  pubes,  ‘grown  up,  adult’,  puer, ‘child,  boy’,  puella,  ‘girl’,  putus,  ‘boy’,  pullus, ‘a  young  animal’,  Oscan  pu-klu,  ‘child’,  OI. potah,  'a  young  animal',  putrdh,  ‘son’,  Avestic pudra-,  ‘son,  child’,  OSlav.  puta,  putica,  ‘bird’, Lith.  putytis,  ‘young  animal,  young  bird’,  Lett. putus,  ‘bird’.  Alb.  pel's,  ‘mare’,  OE.  fola,  Goth. fula,  ‘foal’.  Alt  these  words  derive  fr.  I.-E.  base *pou-,  *p(u-,  *pS-,  ‘small,  little,  few,  young'. Cp.  foal.  Cp.  also  catchpole,  encyclopedia,  or¬ thopedic,  parvi-,  paucity,  Paul,  paulo-post- future,  pauper,  polecat,  poltroon,  pony,  pool  (in gambling),  poor,  poult,  poulter,  poultry,  poverty, puberty,  pubes,  pubescent,  pubis,  pucelle,  puerile, puerperal,  pullet,  Punchinello,  pupa,  pupil, ‘scholar’,  pupil  of  the  eye,  puppet,  puppy, pusillanimous,  putti  and  the  second  element  in Rajput.  Cp.  also  the  second  element  in  semper. Derivatives:  few,  n.,  few-ness,  adj. fey,  adj.,  fated;  doomed  to  die.  —  ME.  feie,  fr. OE.fiege,  rel.  to  OS .fegi,feg,  ON .  feigr,  OFris. fai,  OHG.  feigi,  ‘doomed  to  die’,  MDu.  vege, Du.  veeg,  ‘about  to  die’,  MHG.  veige,  ‘doomed to  die;  timid,  coward’,  Dan.  feig,  Swed.  feg, G.  feig,  ‘cowardly’,  and  to  OE.  fah,  ‘hostile’,
=== KLN poor
29626:poor,  adj.  and  n.  —  ME.  poure,  povre,  fr.  OF. povre,  poure  (F.  pauvre),  fr.  L.  pauper,  ’poor’, which  stands  for  *pawo-pars  and  lit.  means  ‘he who  acquires  little’,  fr.  paucus,  ‘little’,  and  the stem  of  pario,  par  ere,  ‘to  bring  forth,  produce; to  acquire,  gain’.  See  pauper  and  cp.  pove
=== KLN pony
29609:pony,  n.,  a  small  horse.  —  Scot,  powney,  fr.  obsol. F.  poulenet,  ‘little  foal’,  dimin.  of  F.  poulain, ‘foal’,  fr.  Late  L.  pull  anus,  fr.  L.  pullus,  ‘young
36733:pony,  n.,  summer  drink  made  of raisins,  lemon  juice  and  sugar.  — The  word  orig. meant  ‘beverage  of  Stepney  (an  old  district  of London)'.
=== KLN puppet
31040:puppet,  n.  —  ME.  popet,  fr.  OF.  poupette,  ‘pup¬ pet’,  dimin.  of  poupe  (whence  F.  poupee),  fr.  VL. puppa,  fr.  L.  pupa,  ‘girl;  doll,  puppet’.  See  pupa and  -et  and  cp.  puppy.
```


## [2026-09-14T00:58:52.511Z] TOOL CALL #49: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T00:58:52.564Z] TOOL RESULT

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


## [2026-09-14T00:58:54.952Z] TOOL CALL #50: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T00:58:54.995Z] TOOL RESULT

```
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


## [2026-09-14T00:59:08.807Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -c \"xsa%ra\\|xsa\\^ra\\|xsaira\" BRT.txt; echo \"---compounds\"; grep -o \"[a-zA-Z]\\{2,10\\}[.-]pu[%^i]ra\" BRT.txt | sort | uniq -c | sort -rn | head -15"
}
```


### [2026-09-14T00:59:10.250Z] TOOL RESULT

```
31
---compounds
      2 paiti.puira
```


## [2026-09-14T00:59:17.194Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"βγpʾwr\\|bgpwr\\|bagpur\\|βaγpūr\\|faghfur\\|fagfur\\|faγfūr\" SOD.txt LKT.txt HJB.txt 2>/dev/null | head -8"
}
```


### [2026-09-14T00:59:17.252Z] TOOL RESULT

```
SOD.txt:24768:China,  {country  <?/)Faghfur 
SOD.txt:89396:Faghfur  2590
```


## [2026-09-14T00:59:19.505Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '24760,24775p' SOD.txt; echo ---; grep -n \"2590\" SOD.txt | head -5"
}
```


### [2026-09-14T00:59:19.573Z] TOOL RESULT

```
pay-  purist   (Pypwryst)  ©pi.  ^Pypwr'yc 
Divine  Virgins 

BBB  579;  GMS  26,  1276-,  KG  605 

2590  pypwr  stny   B  &~*jy>&ijy&(jj^' )*>&=? 
paypur-stane 

China,  {country  <?/)Faghfur 
TSP  8;  Hen.  Texts.  763 

2591  pypwryc  =*  Pypwryc 

2592  pypwryst  =*  Pypwryst 

2593  pys-   B,  S  o^J'jj^  <j.>b  io<>~*> 
---
24765:2590  pypwr  stny   B  &~*jy>&ijy&(jj^' )*>&=? 
88189:China  2590,  3240,  3241,  3341, 
89396:Faghfur  2590 
109849:2590
```


## [2026-09-14T01:00:13.395Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/sources/refs/ocr/ 2>/dev/null | head; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg406.png data/verification/sources/refs/ocr/BOOK/406.png && echo copied"
}
```


### [2026-09-14T01:00:14.472Z] TOOL RESULT

```
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
copied
```


## [2026-09-14T01:00:14.691Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LAT parum/pauper\"; grep -on \"pauper[^|]\\{0,240\\}\" LAT.txt | head -3; echo \"=== LEW pullus\"; grep -on \"pullus[^|]\\{0,200\\}\" LEW_1910.txt | head -3"
}
```


### [2026-09-14T01:00:15.825Z] TOOL RESULT

```
=== LAT parum/pauper
15787:pauperibus
33370:paupertatem alicui; ou quelqu'un de quelque
36380:pauperibus in nunnis recondendis etiam, nostro saeculo fuit/. Vnde
=== LEW pullus
```


## [2026-09-14T01:06:22.296Z] TOOL CALL #56: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-406.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Pôu\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *peh₂w- / *pau- : *pou- : *pū- 'small, little, few; young (of an animal)'\",\n  \"note\": \"Pokorny 842-843 heads the lemma exactly as Nourai does: 'Root / lemma: pou- : pau- : pu-; Meaning: small, little; young (of animals)'. The language label (Indo-European) and the gloss 'small, young' are both right, and the whole fan-out of the chart (Av./OP puθra-, Gk. pais, Lat. pauper/pullus/parum, Gmc. *fawaz) is Pokorny's own material under that one lemma. Modern reconstruction writes the root with a laryngeal, *peh₂w- 'few, little' (Wiktionary; AHD 'pau- few, little'); Nourai's 'Pôu' is simply Pokorny's o-grade spelling. Two items on the page need qualification: the Latin box prints 'parrum-affinis', a misprint for parum affinis (and that phrase is a Neo-Latin coinage of 1830, not a Latin word), and the English box hangs pupil/puppet/puppy on Latin pullus although they come from pūpus/pūpa, which Watkins (Nourai's own AHD) files under a different root.\",\n  \"note_fa\": \"ریشهٔ هندواروپایی آغازین *peh₂w- (در پوکورنی به صورت pou- : pau- : pu- «خرد، کم؛ نوزادِ جانور»، صفحهٔ ۸۴۲–۸۴۳) درست است و برچسب زبانی و معنای آن نیز با منابع می‌خواند. همهٔ شاخه‌های این نمودار — puθra- اوستایی و پارسی باستان، pais یونانی، pauper و pullus و parum لاتینی، و *fawaz ژرمنی — در همان یک مدخلِ پوکورنی گرد آمده‌اند و واتکینز (AHD) و کلاین نیز همین خانواده را زیر همین ریشه می‌آورند. دو نکته باید اصلاح شود: صورت لاتینی چاپ‌شده «parrum-affinis» غلط چاپی کتاب به جای parum affinis است، و واژه‌های pupil/puppet/puppy در واقع از pūpa/pūpus لاتینی‌اند نه از pullus. در مجموع ادعای نورایی دربارهٔ ریشه درست است.\",\n  \"sources\": [\n    W + \"Reconstruction:Proto-Indo-European/peh%E2%82%82w-\",\n  ],\n  \"ref_check\": [\n    {\"ref\": \"POK:842\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt (lines 68850-68908), the lemma printed on pp. 842-843: 'Root / lemma: pou- : pau- : pu- | Meaning: small, little; young (of animals)'; §1 Gothic fawai, OE fea/feawe 'few'; §2 Latin paucus, pauper; §3 'gr. παῦρος … Latin with metathesis parvus, parum (*parvom) \\\"too little\\\"'; §4 'gr. παῖς, Gen. παιδός … Latin puer'; §5 'putra- m., Avestan ap. puθra- m. (latter from putlo- = Oscan puklo-) \\\"son, kid, child\\\" … Latin pullus \\\"young, the young of an animal\\\" (*put-s-lo-)'. Nourai's page number and gloss are exact.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. pau-\", \"stance\": \"supports\",\n     \"note\": \"'pau-. Few, little. I. … 1. Germanic *fawaz in Old English fēawe, few: FEW. 3. Suffixed form *pau-ro- in metathetical form *par-wo- in Latin parvus … neuter parvum, becoming parum, little, rarely: PARAFFIN. 4. Compound *pau-paros … Latin pauper: PAUPER, POOR, POVERTY. II. … Latin pullus …: PONY, PULLET. III. … 3. Suffixed form *paw-id- in Greek pais (stem paid-), child: PEDO-; ENCYCLOPEDIA, ORTHOPEDICS. [Pok. pāu- 842.]' (AHD_watkins1985.txt line 814)\"},\n    {\"src\": \"WLD\", \"where\": \"WP. II 75 f. (cited by Pokorny at the foot of the lemma)\", \"stance\": \"supports\",\n     \"note\": \"Pokorny's own 'References: WP. II 75 f., WH. II 259, 265 f., 382 f., 385 f., 394, Trautmann 233' — i.e. Walde-Pokorny II 75 ff. is the source list for this root; Buck 2.25 likewise refers the whole family to 'Walde-P. 2.75 ff.'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 2.25 'Boy'\", \"stance\": \"supports\",\n     \"note\": \"SYN.txt line 2425: 'Grk. παῖς, gen. παιδός (fr. *pafid-) \\\"boy, girl, child\\\" … Lat. puer … : Skt. putra-, Av. puθra- \\\"son\\\", Osc. puklum, … Grk. παῦρος \\\"little\\\", Lat. putus \\\"boy\\\", pusillus \\\"very small\\\", Goth. fawaz \\\"few\\\", etc., all fr. the notion of \\\"small\\\". Walde-P. 2.75 ff.'\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. few (KLN_1966.txt line 14648)\", \"stance\": \"supports\",\n     \"note\": \"Klein gathers the identical list and names the base in Nourai's own spelling: 'All these words derive fr. I.-E. base *pou-, *pu-, *pə-, \\\"small, little, few, young\\\". Cp. foal. Cp. also catchpole, encyclopedia, orthopedic, parvi-, paucity, … pauper, … pony, pool, poor, poult, poultry, poverty, puberty, … puerile, pullet, … pupa, pupil, puppet, puppy, pusillanimous'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, 'paus-/pauros' (IEC.txt line 12554) and 'putros' (line 13826)\", \"stance\": \"supports\",\n     \"note\": \"'pauros … Lat. cf. pau-per, adj. \\\"poor\\\" … OE cf. fēa gs. fēawes, adj. \\\"few\\\"'; 'putros (or putlos?) (1) \\\"son, offspring\\\" (R. Kent: putlo-) … Av. puθro, m. \\\"son\\\" … Per. pusar, id.; Osc. puklu-; Lat. (doubtfully) pullus … if fr. *putlo-'\"}\n  ],\n  \"nodes\": []\n}\n\nN = entry[\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"pu 1, pu-thra, puthra; xšathra-puthra; bağa-puthra; a-puthra-tanu\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Avestan puθra- m. 'son, child' (Bartholomae col. 907 f.; Yasna 65.12 ahurahe mazdā puθra 'son of Ahura Mazda') is the regular Iranian reflex of PIE *putlo-/*putro- under the root *peh₂w-: Pokorny p. 842 §5 'putra- m., Avestan/OP puθra- m. (the latter from putlo- = Oscan puklo-)', Proto-Indo-Iranian *putrás (= Skt. putrá-). The bare stem 'pu 1' is Nourai's own zero-grade abstraction, not an Avestan word. Of the three compounds, only a-puθra- is actually in the Avestan corpus, and it means the OPPOSITE of what the chart implies: Bartholomae lists ¹a-puθra- 'ohne Sohn, Kind' (Vd. 3.24 caraiti yā darəγa apuθra ahti 'a woman who is long without children'; MP afus, apus) alongside ²ā-puθra- (long ā-, only fem. ā-puθrā-) 'pregnant' and ā-puθrya- n. 'Niederkunft, puerperium' (Pahl. āpusīh). Nourai's 'a-puthra-tanu \\\"having a child in body, pregnant\\\"' is in fact Hübschmann's starred reconstruction *ā-puθra-tanū- (Persische Studien p. 5 n. 5), built to explain NP ābistan, not an attested text-form, and it must carry the long ā-. xšaθra-puθra 'son of a king' and baγa-puθra 'son of a god' are not in Bartholomae at all (a grep of BRT.txt for compounds in -puθra- yields only paiti.puθra-); they are Middle Iranian formations — MP šāh-puhr, Sogd. βaγ-pūr — retrojected here into Avestan. Hence plausible rather than confirmed: the root, the language and the head word are right, the three compound entries are partly reconstructed and partly Middle-Iranian.\",\n \"derivation_fa\": \"واژهٔ اوستایی puθra- «پسر، فرزند» بازماندهٔ منظمِ صورت هندوایرانی آغازین *putrás (سنسکریت putrá-) و در نهایت ریشهٔ هندواروپایی *peh₂w- است؛ پوکورنی در صفحهٔ ۸۴۲ همین را می‌آورد و بارتولومه آن را در ستون ۹۰۷ ثبت کرده است. اما از سه ترکیبِ یادشده تنها a-puθra- در متون اوستایی هست و معنایش «بی‌فرزند» است (وندیداد ۳٫۲۴؛ در فارسی میانه apus/afus)، و آنچه نورایی «باردار» خوانده در واقع ā-puθra- با الف کشیده است که بارتولومه فقط در صیغهٔ مادینه ثبت کرده؛ صورت *ā-puθra-tanū- نیز بازسازیِ ستاره‌دارِ هوبشمان (پژوهش‌های ایرانی، ص ۵، پانوشت ۵) برای توضیح «آبستن» است نه واژه‌ای متن‌بنیاد. دو ترکیب xšaθra-puθra و baγa-puθra در فرهنگ بارتولومه نیامده‌اند و در حقیقت ساخت‌های ایرانی میانه‌اند (šāhpuhr پهلوی و βaγpūr سغدی). پس ادعای نورایی دربارهٔ خودِ puθra- درست، ولی دربارهٔ ترکیب‌ها با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/peh%E2%82%82w-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:842\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt line 68887 (p. 842 §5): 'With l-formant: putra- m., Avestan ap. puθra- m. (latter from putlo- = Oscan puklo-) \\\"son, kid, child\\\"' — precisely the arrow root→Avestan puθra-. Pokorny says nothing about xšaθra-/baγa- compounds.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"s.v. ¹a-puθra-, ²ā-puθra-, ā-puθrya- (BRT.txt lines 3719-3744)\", \"stance\": \"partial\",\n    \"note\": \"'¹a-puθra- Adj. (fem. °rā-) \\\"ohne Sohn, Kind\\\": caraiti … yā darəγa °ra ahti \\\"eine Frau, die lange kinderlos ist\\\" V.3.24 … KompA. — ai. aputra- Adj.; mp. afus, apus, afusar'; separately '²ā-puθra- Adj., nur fem. °rā- [dick =] schwanger' with the note 'np. vgl. ābistan (\\\"schwanger\\\")', and 'ā-puθrya- n. \\\"Niederkunft, Puerperium\\\" … Pü.: āpusīh'. Supports puθra- and the ā-puθra- 'pregnant' link, but has no xšaθra-puθra-, no baγa-puθra- and no *ā-puθra-tanū-.\"},\n   {\"src\": \"KNT\", \"where\": \"§78 and lexicon s.v. puça- (KNT.txt lines 1086, 5691)\", \"stance\": \"supports\",\n    \"note\": \"'Examples: pIE *puḱlo-, OP puça- \\\"son\\\", Av. puθra-, Skt. putra-' (§78) and 'puça- sb. \\\"son\\\": Av. puθra-, Ars. Ph. puhr, N Pers. pus, Skt. putrá-, Osc. puclo-, pIE *putlo-'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 2.41 'Son' (SYN.txt line 2888)\", \"stance\": \"supports\",\n    \"note\": \"'Skt. putra-, very common beside sūnu-, Av. puθra-, OPers. puθra-, the reg. Iran. word : Osc. puklum \\\"filium\\\", Pael. puclois, Lat. puer, Grk. παῖς, etc. (2.25). Walde-P. 2.75 ff.'\"}\n ]\n})\n\nN.append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"pesar «پسر»; âbestan «آبستن» (+ script extra: پُس۲ ، پور ، پوره ، شاهپور ، فغپور)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"پسر pesar: Old Iranian *puθra- gives OP puça- (OP θr > ç), whence MP pus [BRE / pws] 'son' (MacKenzie p. 70); the MP by-form pusar was built on pus after the -ar of the other kinship terms pidar, brādar, mādar (Hübschmann §24: 'pisar \\\"Sohn\\\" = pusar, nach Horn durch pidar beeinflusst'), and MP u > NP i/e in that environment gives NP pesar/pisar. آبستن ābestan: MP ābus 'pregnant' (Bartholomae's Pahlavi āpus, āpusīh), extended with the suffix -tan to ābustan/ābistan, from Proto-Iranian *ā-puθra- 'having a child within' (Av. fem. ā-puθrā-), i.e. exactly Nourai's a-puθra(-tanu); Hübschmann §96a: 'ābis-tan \\\"schwanger\\\", phl. āpustan, apus = zd. *āpuθra-', and inlaut u > i by his §24. The extra script forms are all from the same etymon by different roads: پُس pos is the direct SW-Iranian reflex (MP pus); پور pur is the NW/Bactrian-shaped form, MP puhr (OP θr > hr), preserved in شاهپور Šāh-puhr 'king's son' (Hübschmann §96b: 'pur \\\"Sohn\\\" = phl. puhr in Š(a)puhr … np. Šāpūr'), Wiktionary now deriving NP pūr from Bactrian πουρο rather than directly from Parthian; پوره pura is its extended form (Rumi's پورهٔ ادهم, quoted on the page); and فغفور faγfūr 'the emperor of China' is a loan from Sogdian βaγpūr 'son of god', Gharib no. 2590 βγpwr-stny (βaγpūr-stān) 'China, (country of) Faghfur' — Horn no. 318 already lists 'arabisiert fūr in faγfūr, takfūr'. So every word in the box does come from Iranian *puθra-; only the intermediaries differ from what the single arrow suggests.\",\n \"derivation_fa\": \"«پسر» از فارسی میانهٔ pusar، و آن از pus (پارسی باستان puça-، با تبدیل θr ایرانی باستان به ç در پارسی باستان و سپس s در فارسی) که به قیاسِ pidar و brādar پسوند -ar گرفته است؛ هوبشمان (بند ۲۴) و هرن (شمارهٔ ۳۱۸) هر دو همین را می‌گویند و مکنزی نیز pus / pusar «پسر» را ثبت کرده است. «آبستن» از فارسی میانهٔ ābustan/ābistan و آن از ābus «باردار»، از ایرانی آغازین *ā-puθra- «دارندهٔ فرزند در تن»؛ ویکی‌واژه و هوبشمان (بند ۹۶الف) همین زنجیره را می‌آورند و بارتولومه هم ذیل ā-puθra- به «آبستن» فارسی اشاره کرده است؛ تبدیل u به i در هجای میانی قاعده‌ای است که هوبشمان در بند ۲۴ آورده. «پُس» بازماندهٔ مستقیم جنوب‌غربی، «پور» صورتِ شمالی‌گونه (puhr پهلوی، در شاهپور) و به گفتهٔ ویکی‌واژه وام از بلخی πουρο، «پوره» گونهٔ گسترده‌شدهٔ آن (بیت مولوی «پورهٔ ادهم» در همین صفحه)، و «فغفور» وام‌واژه‌ای از سغدی βaγpūr «پسر خدا» است (غریب، شمارهٔ ۲۵۹۰). پس ادعای نورایی درست است، تنها واسطه‌های میانی در نمودار نشان داده نشده‌اند.\",\n \"sources\": [W + \"%D9%BE%D8%B3%D8%B1\", W + \"%D8%A2%D8%A8%D8%B3%D8%AA%D9%86\", W + \"%D9%BE%D9%88%D8%B1\", W + \"%D9%81%D8%BA%D9%81%D9%88%D8%B1\", \"https://abadis.ir/fatofa/%D9%BE%D8%B3%D8%B1/\", \"https://abadis.ir/fatofa/%D8%A2%D8%A8%D8%B3%D8%AA%D9%86/\"],\n \"ref_check\": [\n   {\"ref\": \"BQT\", \"status\": \"partial\",\n    \"note\": \"Nourai cites Borhan-e Qāte' without a page. The local OCR of vols 1-2 (BQT_v1_pages.txt / BQT_v2_pages.txt) is too coarse to isolate the headwords پسر / آبستن / پوره (greps for all four returned only running text, e.g. line 6185 'و یک تاك مخفف آبستن باشد'). Indirect confirmation that Borhan carries exactly the forms Nourai puts in the box: Dehkhoda s.v. پسر quotes it three times — 'پسر. [پ ُ / پ َ س َ] (اِ) پور. پوره. (برهان قاطع). پُس. فرزند نرینه … ریمن؟ (برهان قاطع)' (abadis.ir/fatofa/پسر). So Borhan does give پور، پوره، پُس as the synonyms of پسر; it gives no etymology.\"},\n   {\"ref\": \"AEF:384\", \"status\": \"not_checked\",\n    \"note\": \"Khaleqi Motlaq's Asās-e Eshteqāq-e Fārsi is the Persian translation of Horn's Grundriss; refs_online.json has it as 'catalog' only (no copy online or on disk). Its German original at the corresponding place, Horn no. 318 (pp. 70-71), does say what the arrow says — quoted under 'consulted' below.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 318, pp. 70-71 (HRN.txt lines 3037-3047)\", \"stance\": \"supports\",\n    \"note\": \"'318. puser, pur \\\"Sohn\\\", pus (Šāhn. III …) … ap. aw. puθra- \\\"Sohn\\\"; phlv. pusar, pus, Šāh[p]uhr; ai. putrá-, kurd. pisir, … oss. d. furt, i. firt; bal. n. pusaɣ … arabisirt fūr in faɣfūr, takfūr'.\"},\n   {\"src\": \"HUB\", \"where\": \"§24 (p. 139), §96 a-b (p. 207 f.), p. 5 n. 5 (HUB.txt lines 79-84, 4882-4884, 7251-7256)\", \"stance\": \"supports\",\n    \"note\": \"'§96. Ap. θr wird im Np. zu s oder hr: a) … pus \\\"Sohn\\\" (daraus pusar, pisar nach pidar u. s. w.) = ap. puça-; … ābis-tan \\\"schwanger\\\", phl. āpustan …, apus H. 5 = zd. *āpuθra- (für apuθra-)'; 'b) … pur \\\"Sohn\\\" = phl. puhr in Š(a)puhr … np. Šāpūr, ap. puθra-'; and p. 5 n. 5: 'np. ābistan aus *ābustan auf zd. *āpuθratanu- oder nur *āpuθra- \\\"bekindet\\\" (mit später zugesetztem tan) zurückzuführen'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie pp. 70 and 5 (PHD.txt lines 551, 166-170)\", \"stance\": \"supports\",\n    \"note\": \"'pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREl, pwsl | M pwsr, N ~] son'; 'ābestan [ʾbystn' | P ʾbystn, N ābistan] = ābustan'; 'ābus, -tan [ʾpws, -tn' | M ʾbwws, v. ābestan] pregnant. ~īh: pregnancy' — the Middle Persian links pus→pusar→pesar and ābus(tan)→ābistan that the single arrow compresses.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. apāk-puhr, apē-puhr, Šāhpuhr (NYB_vol2_glossary.txt lines 502-503, 584, 878)\", \"stance\": \"supports\",\n    \"note\": \"'apāk-puhr [LWTH pwhl] he who has a son'; 'apē-puhr [ʾpypwhl] without son'; and the royal name 'bag Šāhpuhr' — the MP puhr < *puθra- that stands behind NP پور and شاهپور.\"},\n   {\"src\": \"SOD\", \"where\": \"Gharib no. 2590 (SOD.txt line 24765)\", \"stance\": \"supports\",\n    \"note\": \"'2590 βγpwr-stny / βaγpūr-stāne — China, (country of) Faghfur. TSP 8; Hen. Texts 763' — the Sogdian source of Persian فغفور.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, pdf page 168 of ARY_latin_index_pages.txt (printed p. 169)\", \"stance\": \"supports\",\n    \"note\": \"Aryanpur's entry for پسر lists exactly this family: 'PUTHRA (OLD PERSIAN) / PUTHRO (AVESTAN) / PUS, PUSAR (PAHLAVI) / PISIR (KURDISH) / PUSAGH (BALUCHI) / PUTRAS (SANSKRIT) / PAIS, PAUROS (GREEK) / PUER, PUTUS, PAUCI (LATIN) / FAWA(I) (GOTHIC) / FEAWE (OLD ENGLISH)', with references 'POKORNY; MACKENZIE (SON) 133; BUCK; SKEAT (PEU) 756'.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in and Dehkhoda s.v. پسر / آبستن via abadis.ir\", \"stance\": \"partial\",\n    \"note\": \"'پسر … (اسم) ۱- فرزند طفل … ۲- فرزند نرینه پور پس ابن ولد مقابل دختر'; 'آبستن (صفت اسم) ۱- حامله باردار' — the meanings the chart gives ('boy, son'; 'pregnant') are right; neither dictionary offers an etymology, so no confirmation of the route.\"}\n ]\n})\n\nN.append({\n \"id\": 3, \"lang\": \"Old Persian\",\n \"words\": \"puča\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old Persian puça- 'son', written p-u-ç in the cuneiform and one of the commonest words of the Achaemenid inscriptions (DB 1.28 Kabūjiya nāma Kūrauš puça 'Cambyses by name, son of Cyrus'; the royal filiation formula X-ahyā puça). It continues the same *puθra- as Avestan puθra-: Kent §78 states the sound law, 'PIE *puḱlo-, OP puça- \\\"son\\\", Av. puθra-, Skt. putra-' — Old Iranian θr became in Old Persian a sibilant transcribed ç, 'a sound intermediate between pure dental s and palatal š', which is why Persian ends with pus/pesar and not *puhr. Nourai's spelling 'puča' is a popularising transcription of that ç; the scholarly form is puça-. Drawing the node from the root rather than from the Avestan box is right: OP puça- is a sister of Av. puθra-, not a descendant of it.\",\n \"derivation_fa\": \"«puça-» پارسی باستان «پسر» است و در کتیبه‌های هخامنشی بسیار به کار رفته (بیستون ۱٫۲۸: Kabūjiya nāma Kūrauš puça «کمبوجیه نام، پسر کورش»). این واژه هم‌ریشه و هم‌سطحِ puθra- اوستایی است، نه برگرفته از آن: در پارسی باستان خوشهٔ θr ایرانی باستان به آوایی میان s و š بدل شده که آن را با ç می‌نویسند (کنت، بند ۷۸). نگارشِ «puča» در کتاب صورتِ ساده‌شدهٔ همان ç است و در متون علمی puça- نوشته می‌شود. ادعای نورایی درست است.\",\n \"sources\": [W + \"%D9%BE%D8%B3%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"TZF:13\", \"status\": \"not_checked\",\n    \"note\": \"Abolghasemi, Tārīx-e Moxtasar-e Zabān-e Fārsi — refs_online.json marks it 'website' (ketabnak.com/book/81646, login required); no copy on disk and none reachable, so p. 13 could not be read.\"},\n   {\"ref\": \"MFL:102\", \"status\": \"not_checked\",\n    \"note\": \"Oranskij, Introduction to Iranian Philology (Keshavarz's Persian translation) — the only local copy is incoming/MFL/MFL_ia_galaxy_ub2007.pdf, a five-page image fragment with no text layer (pdftotext returns nothing); p. 102 is not in it.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, lexicon s.v. puça- (KNT.txt line 5691) and §78 (line 1086)\", \"stance\": \"supports\",\n    \"note\": \"'puça- sb. \\\"son\\\": Av. puθra-, Ars. Ph. puhr, N Pers. pus, Skt. putrá-, Osc. puclo-, pIE *putlo- (§64, §75.1, §78, §148.III)', followed by the full list of attestations (DB 1.8, 28, 39 …). §78: 'PAR. θr, from pIE tl and θr … persisted in Av. and in Med., but became a sibilant in OP; it is transcribed by ç'.\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae s.v. puθra- / a-puθra- (BRT.txt line 3727)\", \"stance\": \"supports\",\n    \"note\": \"Bartholomae's Altiranisches Wörterbuch treats Avestan and Old Persian together; under a-puθra- he cites 'ai. aputra-; mp. afus, apus', and the OP form p-u-ç- is his puça- (col. 907 f.).\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. putros (IEC.txt line 13826)\", \"stance\": \"supports\",\n    \"note\": \"'putros (or putlos?) (1) \\\"son, offspring\\\". (R. Kent: putlo-) … Av. puθro, m. \\\"son\\\"; Ober pura; Per. pusar; Oss. fírt, furt; Osc. puklu-'.\"}\n ]\n})\n\nN.append({\n \"id\": 4, \"lang\": \"Greek\",\n \"words\": \"pais\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Greek παῖς, gen. παιδός 'child, boy, girl' goes back to *paw-id- (Cypriot and epic πάϝις, gen. πάϝιδος still show the digamma), a d-stem built on the zero grade of *peh₂w-; Watkins puts it under pau- as 'Suffixed form *paw-id- in Greek pais (stem paid-), child (> paideia, education)', and Buck 2.25 gives 'Grk. παῖς, gen. παιδός (fr. *pafid-)' in the same family as Skt. putra-, Av. puθra-, Goth. fawaz. Pokorny lists it in §4 of the lemma, 'youngling, the young of an animal', beside Latin puer. The chart's gloss 'child' and the arrow straight from the root are both correct; παῖς is a sister of the Iranian forms, not derived from them.\",\n \"derivation_fa\": \"واژهٔ یونانی παῖς (اضافی παιδός) «کودک» از صورت *paw-id- است؛ گونه‌های کهن قبرسی و هومری πάϝις هنوز واو (digamma) را نگه داشته‌اند و همین نشان می‌دهد که ستاک از درجهٔ صفرِ ریشهٔ *peh₂w- ساخته شده است. واتکینز (AHD) و باک (بند ۲٫۲۵) و پوکورنی (بند ۴ همان مدخل) هر سه آن را در همین خانواده و کنار puθra- اوستایی و fawaz ژرمنی می‌آورند. پس ادعای نورایی درست است و παῖς هم‌ریشهٔ صورت‌های ایرانی است نه برگرفته از آنها.\",\n \"sources\": [\"https://www.etymonline.com/word/pediatric\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. pau-, section III.3: 'Suffixed form *paw-id- in Greek pais (stem paid-), child (> paideia, education): PEDO-; ENCYCLOPEDIA, ORTHOPEDICS. [Pok. pāu- 842.]' (AHD_watkins1985.txt line 814) — exactly Nourai's Greek box and its two English children.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 842 §4 (POK_full.txt lines 68871-68873)\", \"stance\": \"supports\",\n    \"note\": \"'4. \\\"youngling, the young of an animal\\\": gr. παῦς (Attic vases), Gen. παϝος (Cypriot) … παῖς, Gen. παιδός m. f., hom. πάϝις, παϝιδ- \\\"kid, child\\\"; Latin puer \\\"child, boy, girl\\\" (*puuero-), puella \\\"girl\\\"'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 2.25 'Boy' (SYN.txt line 2425)\", \"stance\": \"supports\",\n    \"note\": \"'Grk. παῖς, gen. παιδός (fr. *pafid-) \\\"boy, girl, child\\\", NG παιδί \\\"child\\\" … : Skt. putra-, Av. puθra- \\\"son\\\" … all fr. the notion of \\\"small\\\". Walde-P. 2.75 ff.'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. few (KLN_1966.txt line 14648)\", \"stance\": \"supports\",\n    \"note\": \"Klein under the base *pou-: 'cogn. with Gk. παῦρος \\\"few, little\\\", παῖς, gen. παιδός, \\\"child\\\" … Cp. also … encyclopedia, orthopedic'.\"}\n ]\n})\n\nN.append({\n \"id\": 5, \"lang\": \"English\",\n \"words\": \"pediatrics, encyclopedia\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both are learned 16th-19th c. formations on Greek παῖς, παιδ-, not inherited words. pediatrics: 'pediatric' 1849, from Latinised Greek paid- (stem of pais) + -iatric (ἰατρικός 'of healing'), the noun pediatrics following, pediatrician 1884. encyclopedia: 1530s, from Modern Latin encyclopaedia (c. 1500), itself a false reading by Latin authors of Greek ἐγκύκλιος παιδεία 'the circle of general education' — enkyklios 'circular, general' + paideia 'child-rearing, education', a derivative of pais (gen. paidos). Because they are borrowings from Greek, the arrow Greek→English is right, but only in the sense of learned transmission (via Latin and, for 'encyclopedia', via the French Encyclopédie for the modern sense), not of inheritance.\",\n \"derivation_fa\": \"هر دو واژه ساخته‌های عالمانه‌اند نه میراث زبانی: pediatrics از صورت لاتینی‌شدهٔ ستاکِ یونانی paid- (از παῖς «کودک») به‌علاوهٔ -iatric «درمانی» در سال ۱۸۴۹ ساخته شده، و encyclopedia در دههٔ ۱۵۳۰ از لاتین نو encyclopaedia می‌آید که خود خوانشِ یکپارچهٔ عبارت یونانی ἐγκύκλιος παιδεία «آموزشِ دایره‌وارِ همگانی» است؛ paideia از همان παῖς ساخته شده است. پس پیکان «یونانی ← انگلیسی» درست است، اما راهِ آن وام‌گیری ادبی از راه لاتین است نه تحول طبیعی.\",\n \"sources\": [\"https://www.etymonline.com/word/encyclopedia\", \"https://www.etymonline.com/word/pediatric\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box; it hangs on the AHD citation of its Greek parent, which lists 'PEDO-; ENCYCLOPEDIA, ORTHOPEDICS' under pau- III.3.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. few (KLN_1966.txt line 14648)\", \"stance\": \"supports\",\n    \"note\": \"Klein's cross-reference list under the base *pou- explicitly names 'encyclopedia, orthopedic' among the English derivatives.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. pau- III.3 and index (AHD_watkins1985.txt lines 814, 1456)\", \"stance\": \"supports\",\n    \"note\": \"The index entry reads 'ENCYCLOPEDIA pau-'; the root article lists 'PEDO-; ENCYCLOPEDIA, ORTHOPEDICS'.\"},\n   {\"src\": \"ETYMONLINE\", \"where\": \"s.v. encyclopedia, pediatric\", \"stance\": \"supports\",\n    \"note\": \"'encyclopedia … from Modern Latin encyclopaedia (c. 1500), thought to be a false reading … of Greek enkyklios paideia … + paideia \\\"education, child-rearing\\\", from pais (genitive paidos) \\\"child\\\"'; 'pediatric … 1849, from Latinized form of Greek paid-, stem of pais \\\"child\\\" … + -iatric'.\"}\n ]\n})\n\nN.append({\n \"id\": 6, \"lang\": \"Latin\",\n \"words\": \"parrum-affinis\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The Latin word for 'too little' is parum (one r), the neuter of *par(v)om, by metathesis from *pau-ro-: Watkins, 'Suffixed form *pau-ro- in metathetical form *par-wo- in Latin parvus, little, small, neuter parvum, becoming parum, little, rarely: PARAFFIN'. 'parrum' with -rr- is not a Latin word; the printed page (pdf p. 406, book p. 376) really does show 'parrum-affinis', so the misprint is Nourai's own and the JSON extraction is faithful. Second, parum affinis is not a phrase of the Latin language at all but a Neo-Latin tag invented in 1830: the German chemist Karl von Reichenbach named his new wax Paraffin 'in reference to the unreactive nature of the substance' — Poggendorff's Annalen (Leipzig 1832) says 'In chemischer Hinsicht zeichnet sich das Paraffin durch eine merkwürdige Indifferenz aus; daher auch sein Name (von parum affinis)'. Klein s.v. paraffin says the same: 'Lit., \\\"of small affinity\\\", coined by the German chemist Karl von Reichenbach (1788-1869) in 1830 fr. L. par(um), \\\"little\\\", and affinis, \\\"connected with, related to\\\"'. So the root connection (parum < *pau-ro-) is sound and the gloss 'with little similarity' is a fair rendering of parum affinis; only the spelling and the implied antiquity are wrong.\",\n \"derivation_fa\": \"صورت درست لاتینی parum (با یک ر) است، حالت خنثای *par(v)om که با قلب (metathesis) از *pau-ro- پدید آمده و با parvus «خرد» هم‌ریشه است؛ آنچه کتاب چاپ کرده — «parrum-affinis» — غلط چاپی خودِ نورایی است، زیرا تصویر صفحهٔ ۴۰۶ (صفحهٔ ۳۷۶ کتاب) همین صورت را نشان می‌دهد و خطای خوانشِ اسکن در کار نیست. نکتهٔ دوم آنکه parum affinis اصلاً عبارتی از زبان لاتین کهن نیست، بلکه نام‌گذاری لاتینِ نو در سال ۱۸۳۰ به دست شیمی‌دان آلمانی کارل فون ریشنباخ است: او این مادهٔ مومی را «پارافین» نامید چون واکنش‌پذیری شیمیایی اندکی دارد (آنالن پوگندورف، لایپزیگ ۱۸۳۲). پس پیوند با ریشه درست است، ولی صورت نوشتاری غلط چاپی و قدمتِ ضمنیِ واژه نادرست است.\",\n \"error_in\": \"book\",\n \"book_prints\": \"parrum-affinis\",\n \"correct_form\": \"parum affinis\",\n \"sources\": [\"https://www.etymonline.com/word/paraffin\", W + \"paraffin\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. pau- I.3: 'Suffixed form *pau-ro- in metathetical form *par-wo- in Latin parvus, little, small, neuter parvum, becoming parum, little, rarely: PARAFFIN, PARVOVIRUS' (AHD_watkins1985.txt line 814); index 'PARAFFIN pau-' (line 2059). Watkins spells it parum — supporting the derivation but also showing the printed 'parrum' to be an error.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. paraffin (KLN_1966.txt line 27272)\", \"stance\": \"supports\",\n    \"note\": \"'paraffin, n. — Lit., \\\"of small affinity\\\", coined by the German chemist Karl von Reichenbach (1788-1869) in 1830 fr. L. par(um), \\\"little\\\", and affinis, \\\"connected with, related to\\\"; so called by him because of its comparative lack of chemical affinity. L. parum is cogn. with parvus, \\\"small\\\", paucus, \\\"little\\\", Gk. παῦρος, \\\"small\\\"'.\"},\n   {\"src\": \"POK\", \"where\": \"p. 842 §3 (POK_full.txt line 68866)\", \"stance\": \"supports\",\n    \"note\": \"'3. With formant -ro-: gr. παῦρος \\\"small, little\\\", Latin with metathesis parvus \\\"small\\\", parum (*parvom) \\\"too little\\\"'.\"},\n   {\"src\": \"ETYMONLINE\", \"where\": \"s.v. paraffin\", \"stance\": \"supports\",\n    \"note\": \"'from German Paraffin, coined c. 1830 by German chemist Karl von Reichenbach …, irregularly from Latin parum \\\"not very, too little\\\", which probably is related to parvus \\\"little, small\\\" (from PIE root *pau- (1) \\\"few, little\\\") + affinis \\\"associated with\\\"'.\"}\n ]\n})\n\nN.append({\n \"id\": 7, \"lang\": \"French\",\n \"words\": \"paraffine\",\n \"verdict\": \"plausible\",\n \"derivation\": \"French paraffine (attested from the 1830s) is the French shape of the term, with the regular French chemical suffix -ine, but it is not an independent French development out of Latin: like English paraffin it is taken over from Reichenbach's German Paraffin of c. 1830. The chart's arrow Latin→French is therefore right only in the sense that the Latin elements parum + affinis were the material of the coinage; the real chain is Neo-Latin parum affinis > German Paraffin (1830) > French paraffine > Persian پارافین. Since the node's word and its ultimate elements are correct but the immediate source language (German) is missing, plausible rather than confirmed.\",\n \"derivation_fa\": \"واژهٔ فرانسویِ paraffine از دههٔ ۱۸۳۰ به کار رفته و پسوند شیمیایی -ine فرانسوی را دارد، اما تحولی مستقل از لاتین نیست: مانند paraffin انگلیسی، وام‌گرفته از Paraffin آلمانی است که ریشنباخ در ۱۸۳۰ ساخت. بنابراین پیکان «لاتین ← فرانسوی» تنها از این نظر درست است که مصالحِ نام‌گذاری لاتینی بوده؛ زنجیرهٔ واقعی چنین است: parum affinis (لاتین نو) ← Paraffin (آلمانی، ۱۸۳۰) ← paraffine (فرانسوی) ← «پارافین» (فارسی). چون حلقهٔ آلمانی در نمودار نیامده، این گره «با احتیاط پذیرفتنی» است.\",\n \"sources\": [\"https://www.etymonline.com/word/paraffin\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for the French box; it inherits the AHD citation of its Latin parent.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. paraffin (KLN_1966.txt line 27272)\", \"stance\": \"partial\",\n    \"note\": \"Klein makes the word a German coinage of 1830 and says nothing of a French intermediary — the French and English forms are both echoes of Reichenbach's Paraffin.\"},\n   {\"src\": \"ETYMONLINE\", \"where\": \"s.v. paraffin\", \"stance\": \"partial\",\n    \"note\": \"'by 1832, from German Paraffin, coined c. 1830 by German chemist Karl von Reichenbach' — the German step that the chart omits.\"}\n ]\n})\n\nN.append({\n \"id\": 8, \"lang\": \"Persian\",\n \"words\": \"pârâfîn «پارافین»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian پارافین pārāfin is a 20th-century loan from French paraffine, as the Persian dictionaries themselves say: Dehkhoda labels it 'پارافین. (فرانسوی، اِ) مادّه جامد و سفید که از الواح شیست قیری گیرند' and Mo'in's Farhang marks it '[فر.] (اِ.) جسمی است جامد و سفید که از سرد کردن ناگهانی روغن‌های سنگین به دست می‌آید'. The tell-tale of the French route is the vocalism: French [paʁafin] with final stressed -ine is rendered pārāfin with long ā in both syllables and a final -in, not the English [ˈpærəfɪn]. So the arrow French→Persian is exactly right, and Nourai's own reference (MON = Mo'in) is the authority for it.\",\n \"derivation_fa\": \"«پارافین» وام‌واژه‌ای است از فرانسوی paraffine که در سدهٔ چهاردهم خورشیدی وارد فارسی شده است؛ دهخدا آن را «(فرانسوی، اِ)» و فرهنگ معین آن را با نشانهٔ «[فر.]» ثبت کرده‌اند. شاهد آواییِ این مسیر، کشیدگی هر دو مصوّتِ ā و پایانهٔ -in است که تلفظ فرانسوی را بازمی‌تاباند نه تلفظ انگلیسی را. پس ادعای نورایی و ارجاع او به معین درست است.\",\n \"sources\": [\"https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%B1%D8%A7%D9%81%DB%8C%D9%86/\"],\n \"ref_check\": [\n   {\"ref\": \"MON\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Fārsi s.v. پارافین, read through abadis.ir (section فرهنگ معین): '[ فر. ] (اِ.) جسمی است جامد و سفید که از سرد کردن ناگهانی روغن های سنگین به دست می آید. در شمع سازی و تهیة ورنی ها استعمال می شود. پارافین مایع در پزشکی به عنوان مسهل به کار می رود.' — '[فر.]' is Mo'in's abbreviation for فرانسوی, i.e. exactly the French source Nourai draws.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"abadis.ir/fatofa/پارافین, section فرهنگ معین\", \"stance\": \"supports\",\n    \"note\": \"See ref_check: the entry is tagged '[ فر. ]' = French.\"},\n   {\"src\": \"DKH\", \"where\": \"Dehkhoda, Loghatnāme s.v. پارافین (abadis.ir)\", \"stance\": \"supports\",\n    \"note\": \"'پارافین. ( فرانسوی ، اِ ) مادّه جامد و سفید که از الواح «شیست» قیری گیرند.' — an independent Persian dictionary giving the same French origin.\"}\n ]\n})\n\nN.append({\n \"id\": 9, \"lang\": \"English\",\n \"words\": \"paraffin\",\n \"verdict\": \"plausible\",\n \"derivation\": \"English paraffin is right as a word of this family, but not as a direct child of the Latin box: it enters English by 1832 (adjectivally 1838) from German Paraffin, Reichenbach's coinage of c. 1830, and only through it from parum affinis; Klein says 'coined by the German chemist Karl von Reichenbach … in 1830', and Etymonline 'by 1832, from German Paraffin'. The sense also shifted in English: Reichenbach's liquid fraction he called eupion, but 'paraffin (oil)' had become the standard English name for the lamp oil by 1860, whence British 'paraffin' = American 'kerosene'. Verdict plausible: correct etymon, missing German link.\",\n \"derivation_fa\": \"«paraffin» انگلیسی از نظر ریشه در همین خانواده است، اما فرزندِ مستقیمِ آن جعبهٔ لاتینی نیست: این واژه در حدود ۱۸۳۲ از آلمانی Paraffin (ساختهٔ ریشنباخ در ۱۸۳۰) به انگلیسی راه یافته است، و تنها از راه آن به parum affinis می‌رسد؛ کلاین و اتیمآنلاین هر دو همین را می‌گویند. در انگلیسی بریتانیایی معنا نیز جابه‌جا شده و «paraffin» به نفتِ چراغ (کروزن) اطلاق شده است. پس ادعای نورایی با احتیاط پذیرفتنی است: ریشه درست، ولی حلقهٔ آلمانی از قلم افتاده است.\",\n \"sources\": [\"https://www.etymonline.com/word/paraffin\", W + \"paraffin\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on the box; it inherits the AHD citation of the Latin parent, which does list 'PARAFFIN' under pau-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. paraffin (KLN_1966.txt line 27272)\", \"stance\": \"partial\",\n    \"note\": \"Klein gives the etymon Nourai gives (L. par(um) + affinis) but makes the word a German coinage of 1830, not a Latin→English descent.\"},\n   {\"src\": \"ETYMONLINE\", \"where\": \"s.v. paraffin\", \"stance\": \"partial\",\n    \"note\": \"'by 1832, from German Paraffin … The liquid form (originally paraffin oil) Reichenbach called eupion, but this was the standard meaning of paraffin in English by 1860.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins index (AHD_watkins1985.txt line 2059)\", \"stance\": \"supports\",\n    \"note\": \"'PARAFFIN pau-' — Watkins does file the English word under this root, as Nourai does.\"}\n ]\n})\n\nN.append({\n \"id\": 10, \"lang\": \"Latin\",\n \"words\": \"pau-per; pu-llus\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"pauper 'poor' is the old compound *pau-paros 'producing little', first element paucus/*pau- 'little', second the root of pariō, parere 'bring forth, produce, acquire' (PIE *perh₃-); Watkins: 'Compound *pau-paros, producing little, poor (*par-os, producing; see pere-), in Latin pauper, poor: PAUPER, POOR, POVERTY', and Klein s.v. poor 'L. pauper … stands for *pawo-pars and lit. means \\\"he who acquires little\\\"'. Nourai's segmentation 'pau-per' and gloss 'with little, poor' are right. pullus 'young of an animal, chick, foal' is the l-formation *put-s-lo- of the same root (Pokorny p. 842 §5: 'Latin pullus \\\"young, the young of an animal\\\" (*put-s-lo-)'), a sister of Oscan puklo- and of Av. puθra-; Watkins prints it as 'Suffixed reduced variant form *pu-lo-, young of an animal … Latin pullus (probably with expressive gemination)'. Both words hang correctly straight from the root, and the box's placement beside, not under, the Avestan box is right because these are Italic cognates, not borrowings.\",\n \"derivation_fa\": \"واژهٔ لاتینی pauper «تهیدست» ترکیبی کهن است از *pau- «کم» و ستاکِ فعل pariō «زاییدن، فراهم آوردن»، یعنی «آنکه اندک به دست می‌آورد»؛ واتکینز و کلاین هر دو همین را می‌گویند و بخش‌بندی «pau-per» در کتاب درست است. واژهٔ pullus «بچهٔ جانور، جوجه» نیز ساختی با پسوند -lo- از همان ریشه است (*put-s-lo-)، چنان‌که پوکورنی در صفحهٔ ۸۴۲ بند ۵ می‌آورد و آن را کنار puklo- اوسکی و puθra- اوستایی می‌نشاند. جای این جعبه در نمودار — پیوسته به خودِ ریشه و نه به شاخهٔ ایرانی — درست است، زیرا این واژه‌ها هم‌ریشه‌اند نه وام‌واژه. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/poor\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. pau-, I.4 and II.3: 'Compound *pau-paros, producing little, poor … in Latin pauper, poor: PAUPER, POOR, POVERTY'; 'Suffixed reduced variant form *pu-lo-, young of an animal … 3. Latin pullus (probably with expressive gemination), young of an animal, chicken: POLTROON, PONY, POOL, POULARD, PULLET' (AHD_watkins1985.txt line 814).\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 842 §2 and §5 (POK_full.txt lines 68862, 68893-68897)\", \"stance\": \"supports\",\n    \"note\": \"'2. With formants -ko-: Latin paucus \\\"little\\\", pauper \\\"poor\\\" (*pauco-paros or pau-paros \\\"little erwerbend\\\")'; '5. … Latin putus, putillus \\\"knave, boy\\\" … Oscan puklo- \\\"kid, child\\\" (= Old Indic putra-) … Latin pullus \\\"young, the young of an animal\\\" (*put-s-lo-)'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. poor and pony (KLN_1966.txt lines 29626, 29609)\", \"stance\": \"supports\",\n    \"note\": \"'poor … fr. L. pauper, \\\"poor\\\", which stands for *pawo-pars and lit. means \\\"he who acquires little\\\", fr. paucus, \\\"little\\\", and the stem of pario, parere'; 'pony … fr. Late L. pullanus, fr. L. pullus, \\\"young (animal)\\\"'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. paus-/pauros (IEC.txt line 12554) and putros (13826)\", \"stance\": \"supports\",\n    \"note\": \"'Lat. cf. pau-per, adj. \\\"poor\\\", if for *pau-oper-'; 'Lat. (doubtfully) pullus, gs -i, m. \\\"chick, cub\\\", if fr. *putlo- or *puslo-'.\"}\n ]\n})\n\nN.append({\n \"id\": 11, \"lang\": \"English\",\n \"words\": \"poor, poverty; pony, pupil, puppet, puppy\",\n \"verdict\": \"plausible\",\n \"derivation\": \"poor and poverty are certain: Old French povre (Mod. Fr. pauvre) < Latin pauper gives ME poure/povre 'poor' (c. 1200), and Old French poverte/povrete < Latin paupertātem gives ME poverte (late 12c.). pony is also sound on the standard account: Scots powny (1650s) < obsolete French poulenet 'little foal', diminutive of poulain < Late Latin pullānus < Latin pullus — Klein and Etymonline both give this chain (Etymonline adding '[Skeat's suggestion, still accepted]'); Skeat's own Concise Dictionary, however, prints a rival Celtic etymology, 'Pony. (C.) Gael. ponaidh, a little horse', so the pony link is well supported but not unanimous. The three remaining words are the weak point of the box: pupil, puppet and puppy do not come from pullus at all but from Latin pūpus 'boy' / pūpa 'girl, doll' — pupil < L. pupillus, diminutive of pupus; puppet < OFr. poupette, diminutive of poupée < VL *puppa < L. pupa; puppy < Fr. poupée 'doll'. Whether pūpus/pūpa belong to this root is disputed: Klein files them here ('Cp. also … pupa, pupil, puppet, puppy' under base *pou-) and Etymonline says pupus is 'probably related to puer (and thus probably from a suffixed form of PIE root *pau-)', but Watkins — the very AHD reference Nourai cites on the parent box — puts them under a different heading, 'pap-¹. Teat (sound symbolism) … Variant form *pup(p)- in Latin pūpus, boy, and pupa, girl: PUPA, PUPIL', and modern Latin etymology (de Vaan) treats pūpus/pūpa as nursery words of expressive origin. Hence plausible: four of the six words are solid, three of them are attached to the wrong Latin parent, and their ultimate root is contested by Nourai's own authority.\",\n \"derivation_fa\": \"«poor» و «poverty» بی‌گمان از این خانواده‌اند: از لاتینی pauper و paupertās از راه فرانسوی کهن povre و poverte به انگلیسی میانه رسیده‌اند. «pony» نیز بر پایهٔ تبیین رایج از فرانسوی کهنِ poulenet «کرّهٔ کوچک»، مصغّرِ poulain، از لاتینی متأخر pullānus و لاتینی pullus می‌آید (کلاین و اتیم‌آنلاین)، هرچند اسکیت در فرهنگ کوچک خود آن را از گیلیکِ ponaidh دانسته است. اما سه واژهٔ «pupil»، «puppet» و «puppy» از pullus نیامده‌اند، بلکه از pūpus/pūpa لاتینی «پسربچه/عروسک»‌اند و پیوندِ pūpa با این ریشه محل اختلاف است: کلاین و اتیم‌آنلاین آن را در همین خانواده می‌گذارند، ولی واتکینز — یعنی همان AHD که نورایی به آن ارجاع داده — این واژه‌ها را زیر ریشهٔ دیگری (pap-¹، با خاستگاه آوانمایی) آورده است. پس این گره «با احتیاط پذیرفتنی» است و جایگاه سه واژهٔ آخر در نمودار نادرست است.\",\n \"sources\": [\"https://www.etymonline.com/word/poor\", \"https://www.etymonline.com/word/poverty\", \"https://www.etymonline.com/word/pony\", \"https://www.etymonline.com/word/pupil\", \"https://www.etymonline.com/word/puppet\", \"https://www.etymonline.com/word/puppy\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"No reference on this box. Its parent cites AHD, and Watkins' index supports only part of the list: 'POOR pau-', 'POVERTY pau-', 'PONY pau-', 'FEW pau-' — but 'PUPA pap-¹' (AHD_watkins1985.txt lines 2059-2065 and 814), i.e. AHD contradicts the pupil/puppet/puppy placement.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. poor, pony, puppet, few (KLN_1966.txt lines 29626, 29609, 31040, 14648)\", \"stance\": \"supports\",\n    \"note\": \"'poor … fr. OF. povre … fr. L. pauper'; 'pony … Scot. powney, fr. obsol. F. poulenet, \\\"little foal\\\", dimin. of F. poulain, fr. Late L. pullanus, fr. L. pullus'; 'puppet … fr. OF. poupette, dimin. of poupe (whence F. poupée), fr. VL. puppa, fr. L. pupa, \\\"girl; doll\\\"'; and s.v. few Klein lists 'pony, pool, poor, poult, poultry, poverty, … pupa, pupil, puppet, puppy' all under base *pou-.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. pap-¹ and index (AHD_watkins1985.txt lines 814, 2139)\", \"stance\": \"contradicts\",\n    \"note\": \"'pap-¹. Teat (sound symbolism) … 3. Variant form *pup(p)- in Latin pūpus, boy, and pupa, girl: PUPA, PUPIL. [In Pok. bab- 91.]' — Nourai's own cited authority removes pupil (and with it puppet, puppy) from this root.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise s.v. Pony (SKT.txt line 14382)\", \"stance\": \"contradicts\",\n    \"note\": \"'Pony. (C.) Gael. ponaidh, a little horse, a pony. Also vulgar Irish …' — Skeat's Concise derives pony from Gaelic, not from Latin pullus (Etymonline nevertheless credits 'Skeat's suggestion' for the poulenet chain, so his view varied between editions).\"},\n   {\"src\": \"ETYMONLINE\", \"where\": \"s.v. pupil, puppet, puppy\", \"stance\": \"partial\",\n    \"note\": \"'pupillus … diminutive of pupus \\\"boy\\\" (fem. pupa \\\"girl\\\"), probably related to puer … and thus probably from a suffixed form of PIE root *pau- (1)'; 'puppet … from Vulgar Latin *puppa, from Latin pupa'; 'puppy … likely to be from French poupée \\\"doll, toy\\\"' — same family only 'probably', and via pupa, not pullus.\"}\n ]\n})\n\nN.append({\n \"id\": 12, \"lang\": \"Germanic\",\n \"words\": \"fawaz\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Proto-Germanic *fawaz 'few, little' is the regular Germanic outcome of the bare o-stem of this root, PIE *ph₂w-os: PIE *p gives Germanic f by Grimm's Law, and the *-w- survives as -w-. It is attested across the branch — Gothic fawai (pl.) 'few', Old Norse fár, Old Saxon fā, Old Frisian fē, Old High German fao/fō/foh 'little', Old English fēawe. Pokorny opens the lemma with precisely these forms (§1), Watkins writes 'Germanic *fawaz in Old English fēawe, few', and Wiktionary derives Proto-Germanic *fawaz from PIE *ph₂w-os under *peh₂w-. Nourai's label ('Germanic'), form and gloss 'few, little' are all correct.\",\n \"derivation_fa\": \"صورت ژرمنی آغازین *fawaz «کم، اندک» بازتاب منظمِ ستاکِ سادهٔ این ریشه است (*ph₂w-os): «پ» هندواروپایی بر پایهٔ قانون گریم در ژرمنی به «ف» بدل شده و واو نیز بر جا مانده است. گواه‌های آن در سراسر شاخهٔ ژرمنی هست: fawai گوتی، fár نورس کهن، fao/foh آلمانی علیای کهن و fēawe انگلیسی کهن. پوکورنی مدخل را با همین صورت‌ها آغاز می‌کند و واتکینز نیز «Germanic *fawaz in Old English fēawe» می‌نویسد. برچسب زبانی، صورت و معنای این گره درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/peh%E2%82%82w-\", \"https://www.etymonline.com/word/few\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. pau- I.1: 'Germanic *fawaz in Old English fēawe, few: FEW' (AHD_watkins1985.txt line 814); index 'FEW pau-' (line 1456).\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 842 §1 (POK_full.txt lines 68858-68860)\", \"stance\": \"supports\",\n    \"note\": \"'1. With -o-suffix: Gothic fawai pl. \\\"wenige\\\", Old Icelandic fár \\\"little, wortkarg\\\", fá-tœkr \\\"arm\\\" (as Latin pauper), Old High German fao, fō \\\"little\\\", Dat. Pl. fouuem, Old Saxon fā, Old English fēa, Pl. fēawe, engl. few \\\"wenige\\\".'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. few (KLN_1966.txt line 14648)\", \"stance\": \"supports\",\n    \"note\": \"'few, adj. — ME. fewe, fr. OE. fēawe, pl. of fēa, rel. to OS. fah, ON. fár, Dan. faa, Swed. få, \\\"few\\\", OFris. fē, OHG. fao, fō, foh, \\\"little\\\", Goth. fawai (pl.), \\\"few\\\", and cogn. with L. paucus'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. paus-/pauros (IEC.txt line 12554)\", \"stance\": \"supports\",\n    \"note\": \"'OE cf. fēa gs. fēawes, adj. \\\"few\\\"; ON fár, f: fá … beside fauskr, m. \\\"rotten log\\\"'.\"}\n ]\n})\n\nN.append({\n \"id\": 13, \"lang\": \"English\",\n \"words\": \"few\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old English fēawe (plural; contracted singular fēa) 'not many, a small number' < Proto-Germanic *fawaz; the OE word was always plural, and the modern singular-less 'few' continues that. Middle English fewe > Modern English few, with the regular OE ēa > ME eu/ew development (cf. dēaw > dew). Etymonline: 'Old English feawe … from Proto-Germanic *fawaz …, from PIE root *pau- (1) \\\"few, little\\\"'; Klein gives the same. The arrow Germanic→English is straightforwardly correct and this is the one node of the page that is entirely uncontroversial.\",\n \"derivation_fa\": \"واژهٔ انگلیسی few از انگلیسی کهن fēawe (جمع؛ مفردِ تقلیل‌یافته fēa) «اندک» است که خود بازماندهٔ *fawaz ژرمنی آغازین است؛ در انگلیسی کهن این واژه همواره جمع بود و همین ویژگی تا امروز مانده است. تحول آوایی ēa انگلیسی کهن به ew انگلیسی نو قاعده‌مند است (مانند dēaw ← dew). اتیم‌آنلاین و کلاین هر دو همین را می‌گویند. ادعای نورایی در این گره کاملاً درست و بی‌مناقشه است.\",\n \"sources\": [\"https://www.etymonline.com/word/few\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on the box; it inherits the AHD citation of its Germanic parent, whose index reads 'FEW pau-'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. few (KLN_1966.txt line 14648)\", \"stance\": \"supports\",\n    \"note\": \"'few, adj. — ME. fewe, fr. OE. fēawe, pl. of fēa … Goth. fawai (pl.), \\\"few\\\" … All these words derive fr. I.-E. base *pou-, *pu-, *pə-, \\\"small, little, few, young\\\".'\"},\n   {\"src\": \"ETYMONLINE\", \"where\": \"s.v. few\", \"stance\": \"supports\",\n    \"note\": \"'Old English feawe (plural; contracted to fea) \\\"not many, a small number; seldom, even a little\\\", from Proto-Germanic *fawaz …, from PIE root *pau- (1) \\\"few, little\\\". Always plural in Old English.'\"},\n   {\"src\": \"POK\", \"where\": \"p. 842 §1 (POK_full.txt line 68860)\", \"stance\": \"supports\",\n    \"note\": \"'Old English fēa, Pl. fēawe, engl. few \\\"wenige\\\"'.\"}\n ]\n})\n\ndoc = {\n  \"pdf_page\": 406,\n  \"book_page\": 376,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [entry]\n}\n\nwith io.open(\"data/verification/page-406.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\", len(N))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-406.py"
}
```


### [2026-09-14T01:06:23.609Z] TOOL RESULT

```
ok 13
```


## [2026-09-14T01:06:30.617Z] TOOL CALL #57: Bash

```json
{
 "command": "ls -la data/verification/page-406.json && python3 -m json.tool data/verification/page-406.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 406"
}
```


### [2026-09-14T01:06:31.874Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 59111 Sep 13 21:06 data/verification/page-406.json
JSON OK
nodes verified: 13/13
node verdicts: {'plausible': 4, 'confirmed': 8, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 6, 'partial': 1, 'not_checked': 8}
books consulted: {'partial': 7, 'supports': 33, 'contradicts': 2} | by book: {'KLN': 9, 'ETYMONLINE': 6, 'POK': 5, 'IEC': 3, 'AHD': 3, 'BRT': 2, 'KNT': 2, 'SYN': 2, 'MON': 2, 'HRN': 1, 'HUB': 1, 'PHD': 1, 'NYB': 1, 'SOD': 1, 'ARY': 1, 'DKH': 1, 'SKT': 1}
```


## [2026-09-14T01:06:54.414Z] AGENT

Done. Wrote `/home/sfmqrb/git/rishe/data/verification/page-406.json`; `verify_check.py 406` reports 13/13 nodes, 0 PROBLEM lines.

**Page 406 (book p. 376), single entry: ROOT "Pôu" [Indo-European] "small, young" — confirmed**
- Root verdicts: confirmed 1. Node verdicts: confirmed 8, plausible 4, transcription_suspect 1.
- Ref checks: supports 6, partial 1, not_checked 8. Books consulted: 33 supports / 7 partial / 2 contradicts (KLN, POK, AHD, IEC, SYN, BRT, KNT, HRN, HUB, PHD, NYB, SOD, ARY, SKT, MON, Dehkhoda, Etymonline).
- POK:842 checked directly: the lemma is verbatim "pou- : pau- : pu- — small, little; young (of animals)", and every branch of the chart (Av./OP puθra-, Gk. pais, Lat. pauper/pullus/parum, Gmc. *fawaz) is Pokorny's own material. Klein s.v. *few* names the base in Nourai's exact spelling.

Flagged items:
- **transcription_suspect #6 Latin "parrum-affinis"** — the printed page really shows `parrum-affinis` (image checked, copied to `data/verification/sources/refs/ocr/BOOK/406.png`), so `error_in: "book"`; correct form is `parum affinis`. Also it is not Latin at all but Reichenbach's 1830 Neo-Latin tag for German *Paraffin*.
- **plausible #1 Avestan** — puθra- confirmed, but `xšathra-puthra` and `bağa-puthra` are absent from Bartholomae (Middle Iranian šāhpuhr / Sogd. βaγpūr retrojected), and `a-puthra-tanu` is Hübschmann's starred *ā-puθra-tanū-; with short a-, Av. a-puθra- means "childless", the opposite.
- **plausible #7/#9 French paraffine / English paraffin** — correct etymon, but both are borrowings of German *Paraffin* (c. 1830); the German link is missing from the chart.
- **plausible #11 English box** — poor/poverty/pony fine; pupil, puppet, puppy come from Latin pūpus/pūpa, not pullus, and Watkins (Nourai's own AHD) files pūpa under `pap-¹` "teat (sound symbolism)", contradicting the placement. Skeat's Concise also gives pony a Gaelic etymology.
- Node #2 (pesar, âbestan) fully confirmed via Horn 318, Hübschmann §24/§96/p.5n.5, MacKenzie, Wiktionary; پور is a Bactrian/Parthian-shaped form and فغفور a Sogdian loan (Gharib no. 2590) — same etymon, different intermediaries, noted in the derivation.

No extraction errors found: the JSON matches the printed page everywhere, including `parrum-affinis`. Unreachable references: TZF:13 (login-only), MFL:102 (local copy is a 5-page image fragment), AEF:384 (catalog only — its German original, Horn 318, does support the arrow), and BQT is cited without a page and the vol.1 OCR is too coarse for the headwords (confirmed indirectly via Dehkhoda, who quotes Borhan for پور/پوره/پُس).
