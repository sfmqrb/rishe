# Verification process log — verify-page-244


## [2026-09-06T15:50:09.695Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 244 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-244.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-244.json. Write /home/sfmqrb/git/rishe/data/verification/page-244.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 244` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:50:11.289Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:50:12.000Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:50:12.017Z] TOOL RESULT

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


## [2026-09-06T15:50:12.425Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-244.txt"
}
```


### [2026-09-06T15:50:12.446Z] TOOL RESULT

```
1	=== PDF page 244 (book page 214) ===
2	--- entry 0 ---
3	ROOT [Avestan / Old Persian] Karšvar : a "circle" of land, country  (refs BRT:459; HRN:191)
4	#1 (parent #0) [Pahlavi] refs=BRT:459 | kîšvar : country
5	  #2 (parent #1) [Persian] refs=BQT:1656; BRT:459 | kešvar «کشور» : country
6	--- entry 1 ---
7	ROOT Kas 1 -> redirect to Kes 1
8	--- entry 2 ---
9	ROOT [Indo-European] Kâs 2 : to direct, command  (refs POK:533; WLD1:358)
10	#1 (parent #0) [Avestan / Old Persian] refs=POK:533; BRT:1574; SYN:1338; BQT:354 | sâs 1, sâh 1 : command ; sâsta, sâstar : ruler, oppressor ; sâxvan, sâsnâ : instructions, teachings ; paiti-sahva : return of speech, answer ☞Per 3
11	  #2 (parent #1) [Pahlavi] refs=BQT:354,1573; MON:1843 | sâstâr : ruler, oppressor ; sâstâreh : bad domination ; soxvan : instructions, speech ; passaxv, pasux : answer
12	    #3 (parent #2) [Persian] refs=BQT:354,1072,1107; HRN:160; MON:1796; FSF:99 | sâstâ «ساستا» : oppressor, demon ; soxan «سخن» : speech ; pâsox «پاسخ» : answer | extra: ساستار | NOTE: See "Kens" for another possible root of "soxan". See "Wegwh" for another possible root of "pâsox"
13	--- entry 3 ---
14	ROOT [Avestan] Kasyapa : tortoise  (refs MON:2987; SOD:204; BQT:1651)
15	#1 (parent #0) [Persian] refs=MON:2987; BQT:1651; HRN:191 | kašaf «کَشَف» : tortoise
16	#2 (parent #0) [Sogdian] refs=SOD:204 | kyšf : tortoise
17	--- entry 4 ---
18	ROOT [Sanskrit] Kâtara : shy, disoriented, wandering  (refs BQT:1555)
19	#1 (parent #0) [Persian] refs=BQT:1555 | kâtŭreh «کاتوره» : wandering, disoriented, dizziness | extra: کاتور | NOTE: Persian words may be cognates with rather than derivatives from Sanskrit
20	
```


## [2026-09-06T15:50:16.126Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-244.json",
 "description": "Read source JSON for page 244"
}
```


### [2026-09-06T15:50:16.166Z] TOOL RESULT

```
{
  "pdf_page": 244,
  "book_page": 214,
  "entries": [
    {
      "root": {
        "name": "Karšvar",
        "lang": "Avestan / Old Persian",
        "refs": "BRT:459; HRN:191",
        "gloss": "a \"circle\" of land, country"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BRT:459",
          "words": [
            {"translit": "kîšvar", "gloss": "country", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1656; BRT:459",
          "words": [
            {"translit": "kešvar", "gloss": "country", "script": "کشور"}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kas 1",
        "redirect": "Kes 1"
      },
      "nodes": []
    },
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
            {"translit": "sâs 1, sâh 1", "gloss": "command", "script": null},
            {"translit": "sâsta, sâstar", "gloss": "ruler, oppressor", "script": null},
            {"translit": "sâxvan, sâsnâ", "gloss": "instructions, teachings", "script": null},
            {"translit": "paiti-sahva", "gloss": "return of speech, answer", "script": null, "see": ["Per 3"]}
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
            {"translit": "sâstâr", "gloss": "ruler, oppressor", "script": null},
            {"translit": "sâstâreh", "gloss": "bad domination", "script": null},
            {"translit": "soxvan", "gloss": "instructions, speech", "script": null},
            {"translit": "passaxv, pasux", "gloss": "answer", "script": null}
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
            {"translit": "sâstâ", "gloss": "oppressor, demon", "script": "ساستا"},
            {"translit": "soxan", "gloss": "speech", "script": "سخن"},
            {"translit": "pâsox", "gloss": "answer", "script": "پاسخ"}
          ],
          "script_extra": "ساستار",
          "note": "See \"Kens\" for another possible root of \"soxan\". See \"Wegwh\" for another possible root of \"pâsox\"",
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kasyapa",
        "lang": "Avestan",
        "refs": "MON:2987; SOD:204; BQT:1651",
        "gloss": "tortoise",
        "note": "Cognate with Sanskrit \"kačyâpa\""
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:2987; BQT:1651; HRN:191",
          "words": [
            {"translit": "kašaf", "gloss": "tortoise", "script": "کَشَف"}
          ],
          "note": null,
          "quote": {
            "text": "چون کَشَف انبوه غوغایی بدید - بانگ وژخ مردمان، خشم آفرید",
            "poet": "Rŭdakî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:204",
          "words": [
            {"translit": "kyšf", "gloss": "tortoise", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kâtara",
        "lang": "Sanskrit",
        "refs": "BQT:1555",
        "gloss": "shy, disoriented, wandering"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:1555",
          "words": [
            {"translit": "kâtŭreh", "gloss": "wandering, disoriented, dizziness", "script": "کاتوره"}
          ],
          "script_extra": "کاتور",
          "note": "Persian words may be cognates with rather than derivatives from Sanskrit",
          "quote": {
            "text": "هیچ راحت می نبینم در سرود و رود تو - جزکه ازفریاد و زخمه ات خلق را کاتوره خاست",
            "poet": "Rŭdakî"
          }
        }
      ]
    }
  ]
}
```


## [2026-09-06T15:50:16.312Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T15:50:16.349Z] TOOL RESULT

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


## [2026-09-06T15:50:37.788Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['BRT','HRN','POK','WLD1','WLD','BQT','MON','SOD','SYN','PHD','NYB','HUB','FSF','ARY','KNT','CHEUNG','IEC','AHD','FRS','HJB','RCH']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600])\n    print()\n\""
}
```


## [2026-09-06T15:50:38.547Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && cat tools/verify_check.py | head -80"
}
```


### [2026-09-06T15:50:39.413Z] TOOL RESULT

```
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

WLD1 null

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

CHEUNG null

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4

RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.history.resource.17812; 1852 Johnson dictionarypersia00johnuoft)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 =
```


### [2026-09-06T15:50:39.470Z] TOOL RESULT

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
page-140.json
page-141.json
page-142.json
page-143.json
page-144.json
page-145.json
page-146.json
page-147.json
page-148.json
page-149.json
---
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


## [2026-09-06T15:50:47.185Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'karšvar\\|karshvar\\|karšvan\\|karsvar\\|kar\\^svar' BRT.txt | head -20; echo \"=== HRN kishvar\"; grep -n -i 'ki[sš]var\\|ke[sš]var\\|kišwar' HRN.txt | head -20"
}
```


### [2026-09-06T15:50:47.248Z] TOOL RESULT

```
4959:, .  Ailu  maza  m^rr/S  .  .  "ve  awrä  YL  z^.  *malnis  (sd.)  atiAat  pouruye  vTdv^  "vqm 41,  a)  mit  einem  ergänzenden  odsT  yä  im  af^Aaeapjma{^.)Y. 44.1g.  II)in erläuternden  Relativ:  'z'aj  karsvar}  _yff/' schwachdeiktischem  Sinn  'jener,  der'; *ar3zaAi  *savaAi  .  .  imat  iar^ar?  yat\  I)  auf  Vorhergenanntes,  Vorausgehendes :i^amra^sm  V.ip.^t);  39';  —  imS  /-irciv/ j  (Wort  oder  Satz)  zurückweisend;  i)  auf barizist^m  barszimanqm  °3raJ'>  yat  hvars  ein  Substantiv,  a)  adjektivisch,  auch  im avacT  "das  Licht  hier  (und)  jenes  Höchste !  Sinn  unsres  Artikels  (des  schwachtonigen unter  den  Hohen  dort,  was  Sonne  heisst"  'der'):  I  ka"bajiyJ' .  .  paruram  idä  xsäya- Y.  j6. 6.  2)    ohne    solchen    (ausge-  aya"  aAJ^  °vaAyü  k(fbüßyaAyS  brälä  bar-
8245:•  J->  S->  P-  UP^  1)  Praea  i)  mit  Akk.; a)  räumlich,  a)  "hin  -  zu':  mi%r)m  yO  .  . fravazaiU  Aaea  karsvar»  yat  arjsaAi  'pa karsvar»  yat  ifaniraitm  Yt  lO.  67;  — "iräyS  °pa  naz'a.paötm  (sd.)  asatUi ..bar^is V.9,11;  Vd.J2;  —  ui'trö  .  .  yS  kapm aipi.spayeiti  spaeitit^m  upa  vayoan»ni Auxmao%re  (sd.)  .  .  YL/4.13;  — para  te gaosp^nta  .  .  hao^asca  . .  *fraisyämaAi  naz- dista  upa  . .  raocä  . .  P.  34.  ß)  'bei, an':  ipanS yöi  hislmte  a:^arö  °pa  ^^anntjm V.  13.28;  —  tqm  yazata  ..  °pa  zrayi^ vouruJcaam  Ytf.iiö;  33,  38,  54,  72,  76, /2.16,  /5. 19,  27,  31';  —  *"/a  *mailUn (sd.)  barfsatiham  ^.3.20;  —  at-a  tu  anya mays  äitt  (sd.)  JasOit  .  .  paoirim  °pa mayiin  ..  tanüm  pairi.yaozdai^ita'^ .<).^\; 31',  Ö.38,  5.54;  —  minum  bara^ ..  aridvl
9395:•  ].  karsvar-,  -van-  n. 'Kreis' der  Erde,  vgl  iasuxra%',i,an:  —  V\,tkctdiakxraihimi 'Erdteü'":  />//«/  -^.^r»  j-«/  x^aniraiim\  ■  feasu.xraO-wan-  Adj.  (auch  fem.) Yt.i£.i5,^o.i5,67,i33,Y.57-3i.y./p.39,  -der  geringe  Einsicht  besitzt':  noit  ia H.  /.  I4i  -  't'^rp  yat  ar.>zahi  Yt.  i2.  9;  „^i^^a  -^wa  (NSf.)  "nicht  darum  (?)  ein ,„_,..  _  .„./   .,..„  j.^/  vouru.bar»iU:^^^^  ^„„  geringer  Einsicht"  N.40'>.
18163:•  j.  frädatx*ar«nah-  m.  EN.  eines  der sechs  Genossen  des  Sao^yant  bei  der  Auf- erstehung, Äa/azi  &esKarsvarJi'rad<^a/sa'^: 'nanks  alaofUS  Yt  y.  12S.
23821:•  j.  vouru.bar^sti-  (n.)  Name  des  im Nordwesten  gelegenen  Erdteils  {karsvar-, sd.):  tarS  'ti  vouru.jarfsti  Yt.  10.  133; 15,  V.  j().  39;   —   upa   karsvar)  yai   'ti
24032:•  j.  vidaSaßü-  (n.)  Name  des  im  Süd- westen gelegenen  Erdteils  (Karsvar-,  sd.)'': tarS  fradala/ii*  'ß'u  Yt  10.  133;  15,  V. '9-  39>  —  "P^  karSvari  yai  'flu  Yt 12.  1 2 ;  —  araeahibyS  (sd.)  .  .fraä^afsubyB 'fsubyS  Vr.  10.  i.
24037:•  j.  vi8at.x''ar»nah-  m.  EN.  eines  der sechs  Genossen  des  Saesyant  bei  der Auferstehung  und  Ratav  des  Karsvar Vidata/sa  (sd.)'':  °na>9hs  alaonS  Yt jj.  1
24858:•  j.  rao^as.caesman-  m.  EN.  eines  der sechs  Genossen  des  SaoSyant  bei  der Auferstehung,  Ralav  des  Karsvar  Art- ta/iT'^:  'mariß  a/aeirS  \'t.  1^3.  128;   iii.
27042:*)  Der  Bd.  ig.  1  als  Ratav  des  KarSvar Fradaiajsä  gilt;  s.  noch  Dk.  g.  21.  24.
=== HRN kishvar
7466:aw. karsvar- 'Weltteil'; phlv. kisvar^).
```


## [2026-09-06T15:50:48.518Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"== $f\"; grep -n 'k̑ās-\\|kās-\\|castigo\\|castigare' $f | head -8; done"
}
```


### [2026-09-06T15:50:50.966Z] TOOL RESULT

```
== POK_01.txt
== POK_02.txt
== POK_03.txt
== POK_full.txt
```


## [2026-09-06T15:50:57.307Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7455,7480p' HRN.txt; echo \"=== leaf for HRN 7466\"; python3 -c \"\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:7465])\nprint('leaf(0-based)=',t[:idx].count('\\f'))\n\""
}
```


### [2026-09-06T15:50:59.137Z] TOOL RESULT

```
n. ßusay 'todten, scli lachten (207).
856. feesß/ ^Schildkröte ; Krebs (Zodiac, Sahn. I, 77 Vers
285)', keseto (dial.).
aw. kasyapu' 'Schildkröte' oder *Krebs' (Geldner,
KZ. 25, 503, 5()6j ; skr. (Brhm.) kagydpa- 'Schildkröte .
af/. kasy 'Schildkröte'; bei. käsib (190).
857. Ä-e«efc 'Elster .
Toniaschek, Painirdialokte S. 771, veigkM'cht aw.
karsiptan-^ phlv. kars{i)ft (L)eutun*i: nicht sicher), wa/.
karjöpc, sar. karjopc, si;'n. ksebc 'ElstiM-'.
858. kiSver^ kesver 'Ph-dteil'.
aw. karsvar- 'Weltteil'; phlv. kisvar^).
859. kesläen ziehen'.
aw. [/^km's-, karsayefi^); phlv. kasttan; ai. 1. [/^kars-,
• kdrsati, karmyati 'ziehen, schleppen'.
kurd. kisän ziehen'; af>'. k/dl; bei. kasay, n. /i'asay
'ziehen, abziehen, herausziehen' (19:^); arm. LW. (?)
Karsem 'ziehen*.
») Syr. LW. J^D^'ID, J^nDD, p^DDIp; ai'ab. LW. kustij (de
Lagarde, Ges. Abb. 59, 60); bei. LW. kustl (143). — Aber nicht gehört
dazu lat. c^ista *Rippe*, das Meringer, Sitzb. WAW. CXXV, *Beitr. z.
indg. Decl.*, 42, mir nicht einleuchtend, zu ai. dbthi- 'Knochen* stellt.
') Eine Volksetymologie in 'Selections of Zätsparnm* (West
P. T. I) 7, 9.
») Aw. [/has- will Hübschmann ZDMG. 44, 558 ausser Betracht
lassen.800. kef \Schaiiin'.
=== leaf for HRN 7466
leaf(0-based)= 212
```


## [2026-09-06T15:50:59.715Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"== $f\"; grep -n -i 'k̂ās\\|kas-  \\|castīgāre\\|castigā\\|çāsti\\|çās-' $f | head -6; done; echo \"=== try schweigen/anweisen\"; grep -n 'anweisen, zurechtweisen\\|zurechtweisen' POK_full.txt | head -10"
}
```


### [2026-09-06T15:51:01.476Z] TOOL RESULT

```
== POK_01.txt
620:Ai.  ancati  (mpers.  ancUan)  und  (tiefstufig)  dcati  ^biegt,  krümmt^,  Partiz. -akna-  (mit  ä-,  ny-,  sam-),  -akta-  (mit  ud-^  ny-)  ,gebogen^;  aidkd-h  m. , Biegung,  Haken,  Biegung  zwischen  Brust  und  Hüfte*^,  ardkas-  n.  ,Biegung, Krümmung^  (=  gr.  to  liyy.og  ,Tal,  Schlucht^,  ar^kasdm  ,Seite,  Weiche'; cwku-  in  aTdküydnt-  ,Krümmungen,  Seiten Avege  suchend.*^;
== POK_02.txt
3685:Ai.  sdrdlia-  m.,  sardkas-  n.  , Herde,  Schar',  av.  sardda-,  apers.  Ö-ard- ,Art,  Gattung';
== POK_03.txt
== POK_full.txt
=== try schweigen/anweisen
```


## [2026-09-06T15:51:10.556Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 1500 POK_full.txt; echo; echo \"=== grep page marker\"; grep -n 'Seite: 533\\|533)' POK_full.txt | head -5; echo \"=== size\"; wc -l POK_full.txt POK_01.txt POK_02.txt POK_03.txt"
}
```


### [2026-09-06T15:51:10.628Z] TOOL RESULT

```
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




Anatolian 


Ang. 




Anglian 


AngN 




Anglo-Norman 


Aram.- 


■Iran 


Aramaeo-lranian 


Ash. 




Ashkun 


Ass. 




Assyrian 


Auk. 




Aukshtaitian 


Bactr. 




Bactrian 


Bel. 




Belorussian 


Br. 




British 


Bret. 




Breton 


BVan. 




Bas-Vannetais 


CCI. 




Continental Celtic 


Chak. 




Chakavian 


Chor. 




Chorasmian 


Clb. 




Celtiberian 


Class. 


Skt. 


Classical Sanskrit 


Co. 




Cornish 


Corn. 




Cornouillais 


Dae. 




Dacian 


Dan. 




Danish 


Dard. 




Dardic 


Dzuk. 




Dzukian 


EBI. 




East Baltic 


EGm. 




East Germanic 


EGmRun. 


East-Germanic Runic 


El. 




Elymian 


Elam. 




Elamite 


Elam.- 


Iran. 


Elamo-lranian 



EMoBret. 


Early Modern Breton 


EMolr. 


Early Modern Irish 


EMoW 


Early Modern Welsh 


ESI. 


East Slavic 


Faer. 


Faeroese 


FriRun. 


Frisian Runic 


Gal. 


Galindian 


Gallo-Gk. 


Gallo-Gk. (in Gk. authors) 


Gallo-Lat. 


Gallo-Latin (in Lat. authors) 


Gaul. 


Gaulish 


GaulG 


Gaulish in Greek letters 


GaulL 


Gaulish in Lat. letters 


Go. 


Gothic 


Gr. 


Greek 


Hebr. 


Hebrew 


Hell. 


Hellenistic 


Hi. 


Hindi 


HVan. 


Haut-Vannetais 


IE 


Indo-European 


Mr. 


Indo-lranian 


InsCI. 


Insular Celtic 


Iran. 


Iranian 
=== grep page marker
=== size
  93771 POK_full.txt
   5151 POK_01.txt
   6715 POK_02.txt
   5974 POK_03.txt
 111611 total
```


## [2026-09-06T15:51:15.663Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt; do echo \"== $f pages: $(python3 -c \"print(open('$f',encoding='utf-8',errors='replace').read().count(chr(12))+1)\")\"; done"
}
```


### [2026-09-06T15:51:17.438Z] TOOL RESULT

```
== POK_01.txt pages: 364
== POK_02.txt pages: 434
== POK_03.txt pages: 430
```


## [2026-09-06T15:51:22.392Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=189 && NR<=191 {print \"----- REC \" NR; print}' POK_02.txt | head -120"
}
```


### [2026-09-06T15:51:25.529Z] TOOL RESULT

```
----- REC 189
 BB.  28,  144)  , Gefäß',  kapöll  , Kniescheibe',  kapöla-  j^^ jWange'  ;
ags.  hafola  ,Kopf*.
Fraglich   ist   Zugehörigkeit   von   lat.    capillus   ,Haar,   bes.    Haupthaar* siehe  WH.  I  158.
WP.  I  346  f.,  WH.  I  158,  163  f.
kspho-  oder  köpho-  ,Huf*.
Ai.  sapkd'  m.  ,Huf,  Klaue',  av.  safa-  m.  ,Huf  des  Pferdes*; aisl.  höfr,  ags.  höf,  ahd.   huof  ,Huf'. WP.  I  346,  Specht  Idg.  Dekl.  253.
1.  kar-  , schmähen,  strafen*.
Gr.  yLccQvr]'  Lrjfiiaj  a-bxÖY.aQvoq'  avTO^i^fXiog  Hes.;
lat.  carinö,  -are  , höhnen,  spotten'  (wohl  ä) ;
air.  caire  f.  , Tadel',  acjmr.  cared  ,nequitiae*,  cymr.  caredd  , Fehler*,  com. cara  ,tadeln',  mbret.  carez  jTadel'  {^kfiä)]
ahd.    haraiven,    mhd.  Jierwen   ,verspotten',    ags.  hiertoan  ,verachten,  ver- spotten',   anord.    herfiligr    ,verächtlich,    erniedrigend',    mhd:    Aere,    herwer^ ,herb',   finn.   Lw.   Ä;arüas  ,amarus*;   tiefstufig   ags.   gehornian   , beleidigen*;
lett.  karinät  , necken,  reizen' ;  ablaut.  ostlit.  klrinti  ds. ;
aksl.  koTb,  u-kor^  ,contumelia',  u-koriti  , schmähen',  po-koriti  ,unter- werfen',  cech.  po-kora  , Demut',  po-korny  , demütig',  ablaut.  serb.-ksl.  kar<t f.  , Streit',  dech.  kdra  , Vorwurf,  Strafe*,  usw.;
vielleicht  hierher  toch.  A  kam-,  B  kam-  , quälen*.
WP.  I  353,  WH.  I  168  f. ;  Trautmann  118  stellt  die  bsl.  Wörter  zu  idg. korio-,  s.  dort.
2.  kar-,  karg-    ,laut    preisen,    rühmen',    auch    (noch)    allgemeinere    Schall-
wurzel  wie  viele  andere,   die  Verbindung  von  k  und  r  enthaltende Wurzeln;    käru-  , Sänger*. Ai.  carkarti   , erwähnt   rühmend'    (Aor.  dkarit),    carkrti-   ,Ruhm,  Preis% karkari-,   karkari  ,eine   Art   Laute',  kirti-  f.   ,Ruhm,  Kunde'   (danach  mit ^  auch  klri-,  klrin-  ,Sänger*) ;  kärü-  , Sänger,  Dichter*  (i-ä^qV^)] gr.  xaQxaiQü}  ,erdröhneS  ytrjgv^,  dor.  ytägv^  , Herold* ;
531
anord.  Tierma  (*harmjan)  , berichten,  melden',  hrödr  m.  ,Rulim,  Lob*, ^S'  hrödor  m.  ,Freude*,  hred  (*Jiröpi-)  ,Ruhm',  abd.  (h)röd-,  (Ji)ruod-  ds.  (in BN),  got-  hröpeigs  , ruhmreich',  anord.  hrösa  ,rühmen'  (*hröp-s-ön)]  ahd. (]i)ruom,  as.  hröm  ,Ruhm,  Lob,  Ehre',  dazu  ags.  hreme  , berühmt'  (*bihrömi')'^
vielleicht  als  ^-Erweiterung :  got.  hröps  , Geschrei',  ahd.  ruof  ,Ruf',  as. jio-s.  hröpan,  ahd.  (Ji)ruofan  , rufen,  schreien',  ahd.  (h)ruoft,  mhd.  gerüefte^ neruofte  n.  ,Ruf,  Schrei',  mnd.  ruchte,  rockte  n.  ,Ruf,  Schrei,  Gerücht', iihd.  (aus  dem  Ndd.)  Gerücht -^

----- REC 190
lit.   kafdas    ,Echo'.,    alit.  ap-kerdziu   ,ich  verkünde',   apr.  kirdlt   ,hören'.
WP.  I  353  f.
•2.  kar-,  redupl.  karkar-  u.  dgl.  ,hart'.
Ai.  karkara-  ,rauh,  hart*  =  gr.  naQ-^agoL'  TQa%elg  Hes.,  ai.  karkasa- ,rauh,  hart*  (auch  karaka-  m.,  ,Hage*l?)  ;vermutlich  gr.  Y.qava\/]6Q  ,hart, rauh,  felsig*.
Dazu  wohl  die  Wörter  für  ,Krebs' :  ai.  karkata-  m.  , Krebs*  {karkin- jKrebs  als  Sternbild*,  Lw.  aus  gr.  xor^xiVog),  karka-h  m.  , Krabbe* ;
gr.  y,aQ/,ivog  ds.,  lat.  cancer,  -crl  ds.  (dissim.  aus  *carcro-,  vielleicht schon  idg.,  vgl.  ai.  kajdkata-  m.  , Panzer*  aus  ^kavkj-ta-) ;
daß  aksl.  rak^  , Krebs*  aus  *krak^  dissim.  sei,  ist  möglich;  die  Ähnlich- keit mit  norw.  (usw.)  rceke  , Cancer  squilla,  Garnele'  setzt  Entlehnung des  norw.  Wortes  voraus  ;
ferner  Worte  für  harte  Schale,  Nuß :  gr,  -Adqvov  .Nuß',  Y.(xQva  f.  ,Nuß- baum' ;  lat.  carlna  f.  ,Nußschale,  Schiffskiel,  Schiff'  (vielleicht  aus  dem Gr.  nach  Keller  Volkset.  279,  in  welchem  Falle  xagvLvog  die  Quelle  ist); ,cymr.  ceri  (*carlso-)  , Obstkern*.
Mit  ^Suffixen:  got.  hardus  ,hart,  streng*,  anord.  hardr  ,hart*,  ags.  heard ,hart,  stark,  tapfer*,  as.  hard,  ahd.  hart,  herti  ,hart,  fest,  schwer*,  Adv. anord.  harda,  ags.  hearde,  ahd.  harto,  mnd.  harde  ,sehr,  besonders*  (vgl. gr.  xa^T«),  urgerm.  *hardü-  aus  idg.  *kar-tü-]  auf  Grund  einer  idg.  Er- weiterung *kre-t-,  *kj't-  äol.  (Gramm.)  ^igezog,  woneben  mit  dem  Vokalismus des  Adj.  att.  ytQccTog,  ep.  ion.  y^dgrog  , Stärke,  Kraft*,  hom.  yigarvg  ,stark' Komparat.  ion.  -ageaacjv,  att.  TtgslTTcov,  Superl.  ngdTiGTog,  ep.  -/.dgriaxog, Adv.  Y.dgTa  , stark',  y.ga%£gög,  Yxxgxsgog  , stark,  kräftig,  fest,  heftig'  (usw.); fern  bleibt  ai.  krdtu-,  av.  xratu§  ,geistige  Kraft'.
Ai.  kathind-,  kdthora-  ,hart,.  fest,  steif*  kann  auch  mit  idg.  l  zu  cymr. caled,  mir.  calad  ,hart*,  gall.  -caletos  gehören  (s.  kal-  ,hart*).
Wegen  der  Existenz  eines  weitverbreiteten  iber.-mediterr.  *carra  , Stein, Steinhaufe*  (v.  Wartburg  FEW.  s.  v.)  ist  die  Zugehörigkeit  folgender  Worte zweifelhaft,    die   teils   hierher   oder   zu   {s)ker-   , schneiden*   gehören,    teils
nichtidg.    Herkunft  sein  können:
34*
532  ,
air.  carrac  f.  (nir.  carraig)  ,Felsen,  Klippe'  und  crec  f.  ds.,  Gen.  craice^ creice,  mir.  auch  Nom.  craic  (nir.  craig)  f.  ds.,  Gen.  crexa,  stammen  alle  aus dem  Brit.,  ebenso  mir.  crach  ,rauh'  (==  schorfig) ;  zu  acymr.  carrecc,  cymr. carreg  t  , Stein,  Felsen'  (*karrika),  bret.  karreg,  corn.  carrefc  ds.,  vgl. cymr.  carro^  ,Bach'  (*karräka),  eig.  , Steinbach'  =  mir.  carrach  ,schorfig« und  gallo-rom.  *cracos  , Stein'  (v.  Wart
----- REC 191
burg  FEW.  s.  v.),  acymr.  creiÄ:, cymr.  craig  f.  (*kraki)  , Felsen',  bret.  krag  ,Sandstein',  cymr.  crach  , Schorf =  bret.  (Vannes)  kräh  ,kleiner  Hügel,  Spitze'  {*krak-,  *krakk-,  vielleicht durch  Metathese  aus  '^kar-k-)  usw.  Grundformen  sind  voridg.  *karr-  oder  idg. *(s)Är-s-  (ergäbe  kelt.  carr-),  bzw.  "^kar-k--^  ebenso  zweideutig  ital.-venezian. (ven.)  scaranto,  caranto  ,steiniger  Bergbach'  und  ven.  ON  Scarantia  > Scharnitz  (Tirol),   Carantania  , Kärnten',  usw.;
desgleichen  germ.  *har(u)gaz  , Steinhaufen,  Opferstätte'  in  anord.  hgrgr , Steinhaufen*,  ags.  hearg  m.  ,heidnischer  Tempel',  ahd.  harg  ,Hain,  Tempel' (finn.  Lw.  karko  ,Holzstoß,  Stapel',  harkko  , Klumpen,  Haufen'),  vielleicht auch  zu  air.  cymr.  bret.  carn  , Steinhügel,  Steingrab',  und  ahd.  hart  ,Berg- wald',  ags.  harad,  -ed  ds. ;  kaum  hierher  als  ,Waldbewohner'  der  altgerm. YN  Xaqovdsg,  Harudes,  ags.  Hasredas,  aisl.  Hordar]  eher  zn  air.  caur^ cur  ,Held'  (*karut-s).
WP.  I  30  f.,  345  f..  WH.  I  8,  151,  166,  168,  Loth  RC  43,  401  f.,  Thur- neysen  KZ.  48,  71;  59,  7  Anm.,  Much  Hoops  Reallex.  s.  v.  Harudes.
kär-  , Wachs'.
Gr.  ytrjQÖg  , Wachs',  yiTjglov  ,Wabe,  Wabenhonig'  kann,  obwohl  dor.  ymgög nicht  genügend  gesichert  ist,  außerhalb  des  lon.-Att.  Lehnform  aus  dieser  ^ Dialektgruppe  sein,  welchenfalls  lat.  cera  als  griech.  Lw.  gesichert  wäre;  -4,
lit.  korys  , Wabenhonig,  Honigscheibe  der  Bienen',  lett.  käres  Nom.  PL  ds.;    '
poln.  skarzyk  ,der  Vorstoß  im  Bienenstock'.  ?.
WP.  I  355,  WH.  I  202,   Specht  Idg.  Dekl.  52.  ?
karS'  ,kratzen,  striegeln,  krämpeln'.
Ai.  kasati  , reibt,  schabt,  kratzt'  (mind.  aus  *krsati),  unklar  kasäya- ,herb,  bitter,  scharf  usw.  (auch  kustha-  n.  , Aussatz',  mind.  aus  *krstha-'^)]-
lat.  carrö,  ere  ,(Wolle)  krämpeln',  Carduus  ,Distel'  (auf  Grund  voa "^carridus  ,kratzend');
lit.  karHü,  karsti  , kämmen,  striegeln,  krämpeln',  lett.  kärSu,  kärst  ,Wolle kämmen';
abg.  krasta  (*kor-stä\  russ.  korösta  f.,  skr.  krästa  ,Krätze,  Grind' ;
mnd.    harst    ,Rechen,    Harke',   wahrscheinlich   auch   mnd.   nhd.   harsch   . ,hart,  rauh',  nhd.  verharschen  , Schorf  bilden,  bei  Wunden',  mdartl.  harsch jSchneekruste',  mhd.  harsten,  verharsten  ,rauh,  hart  werden';    mit  germ.
r
533
Ablautneubildung  und  anlaut.  s-  von  der  Wurzel  sker-  hierher  auch  andd. ofskerran  starkes  Verb  , abkratzen*,  ahd.  scerran,  mhd.  scherren  starkes  Verb kratzen,  schaben*,  Intensivbildung  *skarzön  in  norw.  skarra  ,einen  schar- renden Laut  hervorbringen',  mnd.  mhd.  scharren  , kratzen,  scharren*, schwed.  skorra,  mnd.  schurren  , einen  scharrend
```


## [2026-09-06T15:51:30.176Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==192 {print}' POK_02.txt"
}
```


### [2026-09-06T15:51:31.954Z] TOOL RESULT

```
en  Laut  geben*.
Der  Wurzelvokal  ist  a ;  der  Intonationsunterschied  zw.  Lit.  und  Slav. bleibt  noch  zu  erklären.
WP.  I  355f.,  WH.  I  173f.,  Trautmann  118f.
kas-,  kas-no-  ,grau*.
Lat.  cänus  (^cas-no-s)  ,grau,  aschgrau*,  pälign.  casnar  ,senex*,  ahd.  hasan ,grau  glänzend,  poliert  fein*;  sabin.-lat.  cas-cus  ,alt*  (ursprüngl.  , altersgrau') ;
anord.  hgss  (^kas-iio-),  ags.  hasu  , graubraun*,  mhd.  heswe  ,bleich,  matt*.
Dazu  die  Benennung  des  Hasen  (vgl.  russ.  särjdk  , grauer  Hase*  :  seryj ,grau*):
ai.  sasd-  m.  (aus  *sasd-),  afghan.  soe,  Pämird.  süi]  cymr.  ceinach (-acÄ- Erweiterung  eines  *cein  =  *kasnl  , Häsin*,  Pedersen  KG.  I  86); ahd.  haso,  mit  gramm.  Wechsel  ags.  hara^  anord.  heri  (eine  Ablautsneu- bildung mit  germ.  e  scheint  norw.  schwed.  mdartl.  jase  =  anord.  *hjasi), apr.  sasins  m.  ,Hase',  sasin-tinklo  , Hasengarn*,  ON  Sassenpile  , Hasenberg'.
Eine  Erweiterung  der  Stämme  *kasen-  (:  kas-n-o-)  und  *kaseu-,  kasou- (:  kas-u-o-)  mit  Formans  -dho-  und  Schwundstufe  der  Wurzelsilbe  wird  in gr.  ^av&oq  , blond,  braun'  aus  "^ks-en-dho-  (falls  ^av-  Verquickung  von  *^ev- und  *Ja-=*?w-)?  und  ^ovd-ög  angeblich  ,goldgelb',  falls  aus  *ks-ou-dho-, angenommen,  aber  sehr  zweifelhaft.
WH.  I  156,  Hofm.  Etym.  Gr.  Wb.  221,  Trautmann  330,  Schwyzer  Gr. Gr.  I  329.
käs-,  k9S'  , zurechtweisen,  anweisen';  nur  arisch  und  armenisch.
Ai.  sästi,  1.  PI.  sismdh  , weist  zurecht,  züchtigt,  herrscht,  befiehlt,  belehrt', Partiz.  Aor.  si$dnt-  , unterweisend*,  sistd-  , zurechtgewiesen,  angewiesen, unterwiesen*  (jünger  sästa-,  wie  av.  sästa-)]  av.  sästi  ,heißt,  lehrt',  Opt. sisöit,  a-slHa-  ,verheißen* ;  ai.  sästdr-  , Bestrafer,  Gebieter*  =  av.  sästar- , Gebieter,  Fürst',  mpers.  sastär  ,Herrscher*,  ai.  iästrd-  n.  , Anweisung, Belehrung,  Lehrbuch',  av.  säx'^an-  n.  , Lehre*,  säsnä  , Lehre,  Gebot*,  ai. sisti-  f.  , Bestrafung,  Befehl*  (jünger  sasti-)^  sisya-  ,zu  unterweisen',  m. ,Schüler' ;
arm.  säst  ,Vorwurf,  Drohung,  Strenge,  Autorität',  sastem  , drohe,  schärfe ein,  gebiete',  sastik  , heftig'  (alles  iran,  Lw.  ?).
WP.  I  358,  WH.  I  179.
534  •
1.  kat-  , flechtend   zusammendrehen,   zu   Ketten,    Stricken,    Hürdengeflecht'.
Lat.  catena  , Kette'  (*cates-nä),  cassis,  -is  ,Jägergarn,  Netz'  (wegen  caUna eher  =  *kat-s-is  als  *kat-ti-s-  vielleicht  auch  casa  ,primitive  Hütte'  (xlt- ^prünglich  aus  leichtem  Geflecht;  wohl  dial.  aus  *catiä,  wie  osk
```


## [2026-09-06T15:51:43.334Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'sästar\\|sāstar\\|saxvan\\|säx\\|sāsnā\\|sasna\\|paiti\\.sax\\|paiti\\.sah\\|paitisax' BRT.txt | head -20"
}
```


### [2026-09-06T15:51:43.393Z] TOOL RESULT

```
7927:*)  Die  Worte  beziehen  sich  auf  das  Wohl- gefühl des  Gerechten  und  die  Pein  der  Gott- losen beim  Durehschreiten  des  glühenden  Metall- stromes im  letzten  Gericht,  wovon  Bd.  jo.  19 eriihlt;  s.  aj-ai-  A  und  'ä/ar-  3  b.  Pii.  erl.: /äi-  am  fa  pasäxl  i/aiiiri  tu  öaväl  "damit  mit beim  Ordal  Brand  nicht  iterde";  5.  dam  Jk. JAOS.  14-  LViii   und    lu  V.  34-  4  unter  Äärj.-
13247:—  J')  Pü. :  aidil ,  erl. :  ku  pa  frärönih  säxt ?slel;  ähnlich  Vr.  9.  1,  tl.  1.  —  J3)  Pü.; uzdäl  läk  nun  uzdahiKt  hac  nun  fräe.  — J4)  Pü.;  ayjyiin  0  a/inikiA  ua/.ll.  —  3i>  Pü.: t^  .  .  nf  bulaiid{i\  dakil.  —   3f)  Gdn.  BB,  r*.
14121:—  vUpe  *vantO  tanu.drujB  yB  ad>r)tB.tiaisB (sd.)  V. /(/.  18;  —  mairyS  'vä  bhangrB ^-  5-  3S;  Aog.  ti2i;  —  masyehe  'vats sästarsiiA.)  Y.p.  31;  Ö5.  8,  V.4.49,  2/.1, Yt.  7_J.  137;  —  masyäi  "'vaifyai  Yt.4r3;
14422:•  g,  ^'wä'vant-  Adj.  'dir  ähnlich, solchen  Eigenschaften,  wie  du  sie  hast, einer  wie  du',  immer  mit  Vok.  masdä '(wie  du)  o  J/.">:  ptrssS  aval  ya%a  hv5 yi  .  .  'vqs  masda  akiträ  yadä  hvS  at^hat yäJyao%anasea  "danach  frag  ich,  ob  der, der  . .,  einer  sein  wird  wie  du,  o  MAh., wann  der  sein  wird  und  wie  er  handeln wird"  Y.^/.  r6";  —  yS  na  mtai ..pa%S siiSii  (sd)  . .  arydrS  'vqs  hutJntuf»  sptrttö mazda  ". .  der  zuverlässig  ist,  der wissend  ist  und  heilig,  o  M."  Y.  43. 3''.  a)  im  Sinn  von 'du'  (A.\.  MasdäA)'^: masda  fryäi  'vqs  saRyäi  mavaiti  "o  M., einer  wie  du  möge  es  seinem  Freunde,  wie ich  es  bin,  mitteilen"  Y.  44.  i ;  —  ia%3  möi ..  saSyäi..  °vqs  aslstl/(sd.)  masdä  hads- mH  (sd.)  aia  vohucä  syqs  manarfhä  Y. 44-9;  —  vahiltä  sasnanqm  (sd.)  yqm Imdh  säsfl  asa  ahurS;  spmtö masda  ".  .  die  AAura  .  .  lehrt;  er  der heilige  .  .,  er  der  wie  du  ist,  o  M."  Y.
20269:Zu  sästar-,  eine  wertlose  Missbildung.
20849:—  s.  noch  Y.  47.  5  im  Anhang.  zu  3): ai  ySs  daivä  . .  yasla  va  yazaitl  "vos  et (is)  qui  vos  . .  adorat"  Y.^2. 3;  —  alm mSi  .  .  fisfB  (sd.)  yS  nS  alvS  sasna  goiata (wörtlich)  "der  ist  mir  . .  (als  der)  be- kannt,   der   allein  . .  hörte"   Y.  25. 8;  —
20855:fraHnas  drggvünlim  xiayS  "eo  (facinore) . .  quod  . .  facinus,  (üs)  quae  docuit  .  ■" Y.J2.5;  46.10;  —  vaAista  sasnanam (sd.) yqm  .  .  sästT  .  .  ahurS  "optima  doctrina- ram  (ea  est)  quam  . .  docet"  Y,  4^.  3 ; SO.  3;  —  ks  ya  (ISm.)  ma  uxsyeitl  "quis (est  is)  per  quem  .  ."  Y.  44.  3;  —  dngva- taicä  ..  *asaonl  ..  yekyäcä  hSimmyäsaitl (sd.)  ". .  fideli  . .  et  (ei)  cuius  . ."  Y.  33. I ;  —  manasia  vohü  . .  mazdqmea yalibyS  x/airjm^ä  (Sp.  571  u.)  varpdaitl ärmaiti/ ". .  et  (eos)  quibus  .  ."  Y.  2Ä3:
25270:Zum  V.  rai-.  —  au  räi^as-  n.  —  Pü.:  m, erl. :  ha!  an  pasäxt  {s.  lü  Snilay-,  Sp.  367  U.).  - ■}  Vgl.  rüayeAhi  a  und  PüErl.
26155:mit  paili  'sich  wehren  gegen  —  (Akk.), entgegentreten':  nl  als>mS  nl  dy3(a m  (Sp. 761  u.)  pai/i  r>m)m  paiti  * syOdam'^^  "der Raserei  soll  Einhalt  getan  werden!  gegen die  Grausamkeit  wehret  euch"  Y.  48. 7. Et.?    —    Pü.   (tu   Y.  31):    etSn   esän  -  akra- mv^n  —  rai   lä^i')  stüh,    Sü. :   evam  lasmai bhujtna  iatlram  vi^häli^a;  (lu  \ .  4S):  palTrai i  ariSt  fatä-ai  visiaiti),   Sü.j  praiikülam  ir/yä- iutnanufyatya    . .    firalikülain    lisyäfayämi.    — ')  So  P14  usw.;    5.  auch  KZ.  30,  526.    Vgl. Ko.  3.    Das  zweite  fiaiH  ist  nach  dem  Metram als   müssige  Wiederholung    zu   streichen.  — ')  Doch  nur  wegen  des  Anklangs  von  säxäüm an  iiu*  -  wie  man   gewiss  lux  Zeit,    als  die Pu.  gefetligl  wurde,  bereits  statt  säi"  gespro- chen hat,    5,  PJt.   —    J)   Man   las  jedenfalls syaotdam   oder  ähnlich   und  brachte  das  mit
26236:•  j.,  g.  sästar-  m.  'Gebieter,  Machthaber, Fürst':  yoAmya  °tärS  aurva  .  .  Jrä  (sd.) rSsayaOe  Yt.io.  14;  —  ahurS  *'trmqm^^ dairihupaitis  Yt  i4-  37  i  —  ''o  äaitihius AamS^sa'^rff  Yt.  13.  18,  69,  Jj.  $a;  14.  13, t6. 19.  a)  bes.  von  Feinden  des maa^schen  Glaubens'':  nSit  mä  xMaus'.. naidä  dahySus  yöi  'tärö  dngvants  ". .  noch die  ungläubigen  Machthaber  des  Landes" Y.  4(f.  I.  a)  neben  as^maoya-:  yS aiimaoyS  anasava  yH  masyS  drvä  'ta  Y. Ö5.  8;  V.  2/.  I,  Yt.  J.  7,  10;  —  mahm drvantim  't  lr»m  .  .  ahmaoy^m  V.  4-  49  i —  tna^ehe  drvatö  '/arf  (GS.)  . .  asimao-jahe ¥.9.31;  —  asimaoya/ieca  .  .  'raheca^'' pouru.mahrkahe  Y.  16. 8,  61. 4.
26238:säslär,  erl.  (zu  V.  p) :  Me  apar  andahiht  4)  dät eslel,  (zu  Y.  16) :  lik  anäkih  . . ;  Sü. :  anyäyi, Npü. :  iikananda  kär  u  jiifJ #  (s.  dazu  Bakthe- 1.EMV  Gab.  S7)-  —  ')  So  die  lect.  diff.  in Ptl;  aus  ir.  ••^■f.äm,  %  36S.  39;  zSchr.  'Ira- nifrn  m  F  1  vgl.  ätravaxi'  neben  ätriv'  (sd., No.  1).  —  ')  Es  spielt  hier  vll,  ein  andres sästar-  rail,  das  zu  läJra-  gehört.  —  3)  Them.  — 4)  S.  tu  vayöi.
29333:•)  Im  Sn.  hang  1  ä/rasiäi,  was  auf  ein  mp. andn  (d.i.  hangan\)  i  fr'  schliessen  läist.  Vgl. Aog.  6/:  eigen  fräsyäk  kacdlat  i  tamVi  ään  säxt
```


## [2026-09-06T15:51:45.346Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'kâs\\|kās-\\|kas-, kəs\\|sāstar\\|sästar\\|sāsnā' incoming/WLD/WLD_Bd1_pages.txt | head -20; echo \"=== find page 358\"; grep -n '\\[pdf page' incoming/WLD/WLD_Bd1_pages.txt | head -3"
}
```


### [2026-09-06T15:51:45.421Z] TOOL RESULT

```
=== find page 358
```


## [2026-09-06T15:51:52.209Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming/WLD/ && head -5 incoming/WLD/WLD_Bd1_pages.txt && grep -c $'\\f' incoming/WLD/WLD_Bd1_pages.txt"
}
```


## [2026-09-06T15:51:53.688Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in [26236, 9395, 20269]:\n    idx=sum(len(l)+1 for l in lines[:ln-1])\n    print(ln, 'leaf', t[:idx].count('\\f'))\nEOF"
}
```


### [2026-09-06T15:51:54.092Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
            GOVERNMENT OF INDIA
 ARCHEOLOGICAL SURVEY OF INDIA

               CENTRAL
            ARCHEOLOGICAL
887
```


### [2026-09-06T15:51:56.012Z] TOOL RESULT

```
26236 leaf 859
9395 leaf 278
20269 leaf 646
```


## [2026-09-06T15:52:04.858Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nprint('leaves', t.count('\\f')+1)\nEOF\ngrep -n 'Erdteil\\|kars-, karsayeiti' BRT.txt | head -5"
}
```


### [2026-09-06T15:52:06.819Z] TOOL RESULT

```
leaves 1041
5597:KompA-,  E.  -  Vgl  auQ-a-.  -  aL  ärv_a.,i.  gelegenem  Erdteils  {karh-ar-,  sd.):  avi  -hi Ad].,ro.:  mp.  an-aiuf.  —  ¥11.:  an/aHd,(t\iY.!r   ?.     °,  ,.  ,,.     ^  '     t,,  ,.
6573:was  auf  den  sieben  Erdteilen  ist"  Yt.  C.  3 ; —  yat  ahmi  nm3ne..  nHiriia  daxstai-atti atthat  V.5.  59;  2.  23'j  —  :^3ng.dar?sdi (sd.)  xla'irdi  Ayit  srmaitis  Y. 41^.  16;  — at  kvs  asaAyä  auAat . .  vaslri  (sd.) , . ^.JJ.  3;    —    asti^a"
17615:•  j.  fradaSaßü-  (a)  Name  des  im  Süd- osten gelegenen  Erdteils  {Karhar-,  sd.)  ■> : avi  °ßu  vTdalaßu  \X.i0.i$;  133,  \.iri- 39;   —   avi  karhian  yat  'ßu  Yt.  J2. 11;
23817:•  j.  vouru.5ar«sti-  (n.)  Name  des  im Nordosten  gelegenen  Erdteils  (karivar-, sd.);  avi  vBuru.bar3sti  'ti  YL/0. 15;  133, V,  ig,  39;  —  upa  karsvan  yai  'ti  Yl 12.  14;  —  ar>zahibyS  (sd.)  .  .  vouru.- öansliiyö  'itibyö  Vt.io.i.
23821:•  j.  vouru.bar^sti-  (n.)  Name  des  im Nordwesten  gelegenen  Erdteils  {karsvar-, sd.):  tarS  'ti  vouru.jarfsti  Yt.  10.  133; 15,  V.  j().  39;   —   upa   karsvar)  yai   'ti
```


## [2026-09-06T15:52:16.984Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '^[0-9]\\{3,4\\}$' BRT.txt | head -40; echo \"---count\"; grep -c '^[0-9]\\{3,4\\}$' BRT.txt"
}
```


### [2026-09-06T15:52:18.856Z] TOOL RESULT

```
30:1904
4136:107
4150:109
4407:113
4410:124
4533:130
4552:131
4555:132
4646:137
4649:138
4667:135
4670:136
4757:146
4782:149
4816:152
4866:157
4967:166
4976:168
5000:169
5058:173
5061:174
5131:177
5134:178
5169:179
5208:183
5351:190
5446:193
5691:207
5731:109
5789:314
5839:217
5957:224
5995:326
6010:827
6049:330
6086:335
6089:236
6218:246
6247:247
6250:248
---count
615
```


## [2026-09-06T15:52:22.185Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '^[0-9]\\{3,4\\}$' BRT.txt | awk -F: '$1>9100 && $1<9700' ; echo \"=== around 26236\"; grep -n '^[0-9]\\{3,4\\}$' BRT.txt | awk -F: '$1>25900 && $1<26600'"
}
```


### [2026-09-06T15:52:23.919Z] TOOL RESULT

```
9126:443
9146:445
9149:446
9165:447
9168:448
9187:449
9266:453
9269:454
9345:457
9463:463
9533:467
9591:471
9631:473
9634:474
=== around 26236
25991:1560
26073:1566
26105:1568
26182:1571
26277:1577
26280:1578
26306:1579
26422:1586
26567:1594
26589:1596
```


## [2026-09-06T15:52:28.282Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26180,26300p' BRT.txt"
}
```


### [2026-09-06T15:52:28.331Z] TOOL RESULT

```
SO
dby  Google
1571
IS73
>  Vt.  /p.  44:  1i«(  ftasämm.
•  j.  'säma-  Adj.  'schwarz':  aspahe  k»hrpa auruÜake  (sd.)  . .  aspahe  kikrpa  *mahe  Yt. £18   uod   31.
VgL  'lümii-.  —  S.  syämaka-,  lyäva-  und SSO-  1.
•  j.  'säma-  Adj.  Name  einer  iranischen Familie;    ^rilff  'manqm   snüts  Y.g.  10;
—  *tnaie  kinsäspahe  Yty.  61,  136. WoU  palr.  Adj.,   AbleLl.  >us  »läma-  m.   EN.
—  Vgl.  uäma-'l,  —  ')  Wertlose  Deutungen bei  Gdn.  /.  166,  MaLS  SBE.  31.  233.
•  j.  säy-  V.  'liegen'.  Praes.  i  isy-: jB^-i).  —  ppfp.  'Sita-.
Nur  Med.  i)  'hegen,  daliegen':  *saSe F.  12'^;  —  yaAmi  jä>^  (3PPM.)  . .  jata paun'a{Sf.S$$  m.)  ma/yäiiäaAl'  Vt.io.So;
—  neij  zT  m  sä  M  (sd.)  ya  darr^a  akarsta saHa  V._j.  24.  a)  mit  Abi.  im  Sinn des  vro^^:  yS  ..  aspalm  varis)/n  zimä^a sayamm  valnaiH  katärs  ayravS  {%A^  . . "der  . .  es  einem  auf  dem  Boden  liegea- den  Pfcrdshaaj  ansteht,  ob  . ."  Yt.  i4- 3ii>,  A)  bes.  um  der  Ruhe  zu  pflegen: yB  salU  Aaurvqm  tarasla  xlapansm  aya- ztmnS  . .  y.lS.S.  a)  mit  Akk,  oder  ana und  Akk.  'auf—':  yaha  ttSfryB fryäi  van- taoe  (sd.)  stanla  gätus{^.)  sayamanS .. ". .  auf  dem  gepolsterten  Lager  ruhend  . ." V.J.  35;  —  kim  kimHt  aipi  (sd.)  nmätie gätu  *saffe**  ä^aini.slarvüm  Yt.  5, 103;  — aat  aosde  haxa  Aasa  ana  bamil  saya mnanqmi''  \.  18.26.
mit  ä  'ruhen  auf—':  s.  ssits.'.
mit  paiii  -  ?  — :  il  .  .  paiti  *safre^'> *hamir3%anqm  .  .  satäis  .  .  (soll  wohl heissen)  'Sfor  dir  . .  hegen  die  Feinde  am Boden  . .  zu  hunderten  . ."  VyL  ig.
mit  päiri  'umlagern,  herumgelageit  sein um  — '  (Akk.):  haraiti  bars  hä  kama päiri- sSitefräpayä  (sd.)  datihu^  ä  upaolatthväsca Ytig.i.
■i.  i/tt,  iire;  aiäyalal);  iäyänak;  mp.  (Pü. msäyil,  räsayätt,  «isüan^\  PDn.  nasiam  'icl liege  dunieder',  gr.  aitat.  —  Pü. :  s.  eben femer  No.  6.  —  0  Zunächst  wohl  nur  dii antesonant.  Form  des  Scbwachstammes,  mi a  >U5  uridg.  i,  dann  übertragen.  —  >)  Hds. vaüe,  aber  unler  den  Wörtern  mit  !•;  oi  statt at  auch  Yt.  S-  1°^  ""'^  ■"  <^^"  besten  Hds. lu  V.  18.  S-  —  3)  DbR-  VglS.  /.  30t  erklärt den  Abi.  gewis«  fabch.  Vgl.  zSt.  Yt.  16.  10, wo  ^auäj^mtim  (i.  fäS-)  statt  sayamm  steht.
—  4)  Hds.  saite,  s.  No.  3.  Das  Snbj.  des Satzes  fehlt.  —  Sl  Ob  Gen.  pail.7  —  *)  Hds. saire  und  sal.    Pü.s  ki  haiai  afii  väml^i)-  —
7)  Usw.?,  s.  Bthl.  Stnd.  a.  91.  —  ■)  So  in leseti;  Tgl.  >u  'Jod-  No.  5,  »sar-  No.  5,  3roj~ N0.3.  Das  np.  ^oi/aff 'wegnehmen',  bei  AKQUE- TU.(s.  JusTi  Bd-iSgjberohl  auf  falscher  Punk- tiiung  des  zweiten  Zeichens,  statt  sJäan,
•  j.  '^yaxa  ajihs  ämm  säyaeti"  FrD.7.
•  j.  säy'uzdri-  m.  EN.  eines  Gföubigen: aiavazdasca  '^ritas^a  'äröi^''*  pu%ra  "A. und  e,,  die  Söhne  des  S."  Ytj.  73j  — %rilahe  •drOis^'*'^  asaonö  Yt./J.  113.
Eig.  'des  weibliehe  Zugtiere  scheckig  (s.  säC) aind';  *uiiiri-,  Fem,  in  *aidar;  lum  V.  vai- (S  S3  I).  'e'-  'O  i/ailar:  —  D  Nach  der I-DekL  —  >)  Hdi.  läildrBiS. j.  savanhay-  m.  Name  einer  Gottheit, die  die  Grossviehherden  mehrt*':  °Aalm vlslmca  alavatam  aiahe  ratüm  Y.  2.  3;  18; -  "Aä  . .  ra%we  Y.  /.  3,  33 ;  —  *'Af  (VS.)  ■' .  ra/ziS  Y.i.  20.
*)  Sie  steht  mitl^a,  aber  auch  mit  ^Öi'uniit' 1  Verbindung.  Vgl.  PüErl.:  menüi  ajiäk  hävan hamkÖT  und  SuErL;  yä  yütkäni  gaväm  prmiardha-
Vll.  Ableit.  aus  »sasiah-  n.  'Morgen';  »gL lavakh.  —  Fü.;  transskr.  —  ')  So  Ks,  Mfl; NA.  s-ru:
•  j.  sira-  m.  'Kopf,  Haupt':  avavat  .  . ya%a  *'rtma^'*  varianqm  (sd.)  daräni ". .  auf  dem  Kopf  . ."  Yt5.77;  —  'raie N.  .^2(?).  [särgm  Yt.  i^.  46:  s.  unter p;isi>jära-.]
KompA.,  E-  —  Vgl.  laraA:  —  mp.  täri/är, np.  labui-iät.  —  ')  So  F  i,  vgL  S  2/7  No.  i.
•  j.  särand'  n.  Name  einer  Krankheit, eines  Gebrechens  od.  dgl.'*:  paitistaOe yaskake  .  .  tnahrkahe  . .  'nahe . .  särastyehe V.20.3.
Fü.:  fehlt.  —  0  Wertlos  Dst.  ZA.  2.  278.
■    j.  sUray-  i.  'Bruch,  Zusammenbruch;
"Untergang"'.         [Yt.  i4~  IT-    hcs    sairi,-
baoyfm.]
KompA.  i  Ableit.  --  Zum  ai.  V.  fy^räli;  vgl m  asarXa-.  —  '>  Vgl.  zBed.  air.  ireAri  'Untcr-
gBng^
•  j.  sara-vara-  m.  'Helm':  yag/qtn  %aya- nam  ra%di!H  .  .  das^mä  'rS  V.  14.  9; *Vd.  12.
Eig.  'Kopfbedeckung' ;  *vära-  m.,  zum  V.  'vor-. —  mp.  sämär;  arm,  LW.  laiavarl,  TgL  Hbm. AGt.  I.  335.  —  Pü.:  iirvär,  erl, :  tarai,
•  }.  sirastay-  £  Name  einer  Krankheit, nach  PüErl  'kaltes  Fieber*:  aHaih'a daxmaisva  hqtn.iavainli  .  .  taßtusSa  nae- zasca  'tilca  'v.  7. 57;  —  paiästäHe  .. tafnaoSca  naitahtca  'töisca  Yt/^.  131.
Ableit.  —  Ob  sära-{ia  jarjla-)ilay-f    \gl.iFf>-
dby  Google
'573
8äh-
IS74
slay-  uod  Pü.  —  Pö.:  lart  esliitüh,  erl,:  li^ il<,ffl)  i  sarl.
•  j.  sarastya-  n,  Name  einer  Krankheit:
pailUtälSe  yaskahe  .  .   mahrkahe  .  .  °yehe
V.  20.  3. AbleiL  aus  säraslay-.  —  Pu.:  fehlt.
•  g.  sär^mna-  Adj.,  PPM.:  S.  ^sar-,
•  j.  *säiri.baoya-"  Adj.  'aus,  vor  dem Untergang  rettend':  haoimm  baire  'ffm Aaomim  vfrphrä/atum  baire  Yt/rf-SJ.
'itufja-  m.  KeltDDg',  zum  V.  batn,--;  vgl.  arm. LW.  iaii  (,  das  auf  ir.'Äi'ya-weisl).  — Npü.: iiiiak  vakial  tuHonda,  (bei  TiR  ANDÄz):  faJldl
)   NA.  t
•  j.  säiri'vant-  m.  Name  eines  Bergs oder  Gebirgs:  ahmal  haca  garayS  frao- xsyqn  .  .  'vasca  Yt  ig.  4.
Eig.  tU.  'der  mit  einem  Brach  veTschene,  d.i. geborstene,  eingestürzte  (Berg)'.
•  j.  säs^vUta-  Adj.  'der  die  gros ste  Gewalt, Stärke  besitzt,  am  meisten  vermag':  nöti 'ta  (NPm.)  mit  asfvisfä  (sd.)  Aog.  J^.
Vgl.  srviSia-;  jii*  ist  vermutlich  Mischbildung aus  misla-  und  einem  redupl.  Adj.  *säsava- (od.  ähnl.).  —  Pa. :  pa  täl  iil  x^~Ulär,  Sü.  erl.: ye  larvc/äm  upakärakaräk.
•  j.  ^sasta-  Adj.  (fem.  'ta-\  PPfP.:  S.  sah-. KompE.
•  j.  'sästa-  .\dj.  'quälend,  grausam':  imai . .  stivislim  syaohnim  masya  virizinti  'ta (NP.)  Yt.  17.  59;  —  haca  masyäi  dmaityäi 'layai''  .  .  haca  narS  'layäi''>  Yt4-3-
KompA.  —  Zum  gr.  V.  11^^  'kränite'.  —  Vgl. iäJra-.  —  ")  Unform;  soll  vll.  lu  lii/ar-  ge- hören.
•  j.,  g.  sästar-  m.  'Gebieter,  Machthaber, Fürst':  yoAmya  °tärS  aurva  .  .  Jrä  (sd.) rSsayaOe  Yt.io.  14;  —  ahurS  *'trmqm^^ dairihupaitis  Yt  i4-  37  i  —  ''o  äaitihius AamS^sa'^rff  Yt.  13.  18,  69,  Jj.  $a;  14.  13, t6. 19.  a)  bes.  von  Feinden  des maa^schen  Glaubens'':  nSit  mä  xMaus'.. naidä  dahySus  yöi  'tärö  dngvants  ". .  noch die  ungläubigen  Machthaber  des  Landes" Y.  4(f.  I.  a)  neben  as^maoya-:  yS aiimaoyS  anasava  yH  masyS  drvä  'ta  Y. Ö5.  8;  V.  2/.  I,  Yt.  J.  7,  10;  —  mahm drvantim  't  lr»m  .  .  ahmaoy^m  V.  4-  49  i —  tna^ehe  drvatö  '/arf  (GS.)  . .  asimao-jahe ¥.9.31;  —  asimaoya/ieca  .  .  'raheca^'' pouru.mahrkahe  Y.  16. 8,  61. 4.
KompE.;  Ableit.  {%.  maiyS.säslajöstS.Uma-y — Zum  V.  läh.;  s.  aber  No.  z.  —  u.  iJi/J/*  m., mp.  säslär.    —     Vgl.   sätar-;    säsla:    —    Pü.:
säslär,  erl.  (zu  V.  p) :  Me  apar  andahiht  4)  dät eslel,  (zu  Y.  16) :  lik  anäkih  . . ;  Sü. :  anyäyi, Npü. :  iikananda  kär  u  jiifJ #  (s.  dazu  Bakthe- 1.EMV  Gab.  S7)-  —  ')  So  die  lect.  diff.  in Ptl;  aus  ir.  ••^■f.äm,  %  36S.  39;  zSchr.  'Ira- nifrn  m  F  1  vgl.  ätravaxi'  neben  ätriv'  (sd., No.  1).  —  ')  Es  spielt  hier  vll,  ein  andres sästar-  rail,  das  zu  läJra-  gehört.  —  3)  Them.  — 4)  S.  tu  vayöi.
•  j,  sästö.karSta-  Adv.  'von  grausamen Menschen,  veranlasst,  bewirkt':  paitiitatje 'takt  ibatiankB  Yt.  13. 135.
•  j.,  g.  säsni-  f.  'Lehre;  Gebof:  vakilta 'nanqm  yqm  hudä  sästl  asä  akurS  ". .  ist die  beste  der  Lehren  die,  die  der  wohl- meinende Ah.  durch  Asa  lehrt"  Y.-^.a; —  tim  äzOtöi/isd.)  ahurS  mq%r3m  talal . . spunta  'naya  (IS.)  Y,  29.  7 ;  —  sraffta  'nä fiSnghyS  (sd.)  Y.  4g.  9;  —  yS  nS  alvB  'nä güsatä  zara^u^trB  spitämö  "der  einzige, der  unsre  Lehren  vernommen  hat,  ZarSp." V.2g.S;  —  mä  as  at  vS  drtgvaß  (Sp. 776  o.)  mq%rqscä  gBsta  •näscä  "keiner von  euch  höre  auf  des  ./ungläubigen Worte  und  Gebote"  Y.jj.  18";  —  gayehe man^nS  . .  yS  paoiryS  akurSi  . .  manasla *guita  'näsca  Yt.rj.87*';  —  *maihyDi.mäa- hahe  . .  yS  paoiryS  zarahustrSi  mq'hrtmca *gusla  'näsca  Yt.  JJ.  95'';  —  gusta  'na F.,?f.;  —  sat>m  'nanqm  Vyt /J.
KompA.  —  Zum  V.  läk-.  —  aL  vgL  Säsana' n.  —  Pü.:  ämöriin,  ämSxliht. —  1)  Die  lelztea Worte  der  Stelle  hat  der  Verfasser  von  Yt. '3-  87,  95  bennwt  —  ">  S.  No.  I.
•  j.  säsnö.güä-"  Adj.  'der  die  (heiligen) Lehren  hört,  vernimmt';  paoiryanqm  tkaf- lanqm  paoiryanqm  'güsqm ''  "der  ersten Verkünder  und  Hörer  der  heiligen  Lehren" Y.aö'.  4,  Yt.jj.149J'.
*gis-  Adj.,  zum  V.  gaoi-.  —  Pü. :  nigöHht  i ämöähtin,  erl. :  fratum  /lävill  i  aatalull,  — 1)  Vgl.  No.  3.  —  »)  Vgl.  Y.  19.  8,  Yt.  rj 87.  9S-  —  J'  Wo  Fl   'gülqm  bietet
•  j.,  g.  sah- V.  'hcissen'.  Praes.  1  sah-, 3  sJia-,  2z  sähT:  —  PPfP.  sJäa-'\ s:ista-.
'heissen,  lehren',  mit  dopp.  Akk.:  data xratsul . .  razSng  voAb  säAli  mananAa "(es)  lehre  (mich)  der  Schöpfer  der  Geistes- kraft durch  VM.  (seine)  Satzungen"  Y. $0. 6;  —  y^  nä  )mBs  savatshs  pdhs  slisit "der  uns  die  rechten  Wege  des  Vorteils lehren  könnte"  Y.4J.3;  —  süa  nä  aia
dby  Google
J575  üb- mit  ä  —  ssriSta-  'ST^
faiS..:^aiai^(iA.)  \.34.ii;  —  vafdäJ  \.^i.\^-,32.ft;  —  diidi  mäi . . awLmOii läsnanqm  fsd.^  jqm  . .  ilttl  aii  a^rS  hainsti  ipfniää  maiitrü  wuttdJ  briHrntj' Y.4A. 3.  yüiti  manaoAä  r-t-Aä  •mihi  "scfafnk  mir..
mit  a  Verheisseii,  in  Aassicht  stellen':  Uasterblicbkdt  und  Wohlfahrt  durch  den at  tH  atrim  . .  *ajjil)m'> ..  stzi  rapafäi  beüigsten  Gast,  o  J/i,  Kiaft  mid  Bestand ctirä-ovaahjm  (iA.)  ¥,^4.4.  durch  YM.    bei    dem    Richtereprach"    V,
mit /rJ  i/rS)  'lehren,  ofiienbaren',  mit  5J-7-  4»  'Reden,  Spreeben  lüber  Je- dopp.  Akk.:  ahyä  xraiü  JrS  mi  s3stü  mandes)':  ^J  nar^m  aSaraiam  ain^.z^ifs- vahistä  "durch  seine  Weisheit  lehre  a  mich  «Jt  .  .  kavfanhs  Isd.)  'ahäi  da-iäiti ,  V. das  Beste"  Y.  45, 6; — '/rtuasta-.       a)mit   /J- a*'-  5f    Tled^    Woti":    *ambm9wf
Akl(.  dcrPers-undlDC:  ti>m  mazdä  oAurä  •^)Bi  •r»Ä>m  T.^t;  3t,  12.  S.  noch /rff  mä  liiä  "iwahmät  vaocaAhl  *mainjr^  bei  n&ifjtjatpha-.
haca  Ja-J  i)at»hä  "du,  o  MAk^  lehre  mich      KompE.  —  Zun  V.  nk-.  —  aL  icV«-  m.  —
aas    deinem    Geist   durch    deinen    Mond      K^: -"■"'^-;*- ("L^- ■**  »6  =  ™^=™*,  ,«
1  -     j      71  >r      i>  ■-  4°-  3  """1  ■"  *■  ■  "^*";  *-  noch  No-  at
verkuDden"  H.'JS.ii.  :     _  .,  s  »■ />b«^a».*a..  —  .,  Vi.-,  ki i i li
mit  ^in  'zurechtweisen':  •Hamaästa-,    '     niiur  ämSchui,  oL:  o^  bKHät;  s.  No.  3.—
ü.  Jiu/i,  oHfoti    Htfäi.  —    ra.:  ämtilaii,    iza  .  J)  Pb.:  e  i  lä  eirma^  än.-it/nd,  eri.:  iffl«  i /ä;
Y.  ^  4):  «HJi.  —   «)  (  natt  1  3  »i#-  1)  fti'  s.  No.  z.—  1)  F6-:  lisjt  d«  Wort  «ns;  »her
idg.  ^.   —   »)  SA.  tut  'iffm;    s.  die  Vai.  —  '  die  Eri.  hat  *ii"air, ])  In  VcTwechiltme  mit  änila-;  s.  is  asular:  ,       ,  ...
^  ■  •  g-  sJoghana-  n.  sva.  sfifgAa-  i :  dus.-
•  g.  Mbl'an-  n.  'Lehre':  •:«:'AW(.\P.)  ..  jtffltf  jrm'i  mSr^rufa/ (Sp.  1150U.)  M^S mraoMl  . .  vad^mi^  (sd.)  Y.  5^.  5.  '-^Jyäauf  •näil  xratOm  .  .  Y.  J2.  9.
Zdid   V.   läk-;    wegen    ^  %,  \  Sy.    —    Pü.;|      Zum  V.  la^-. —  ai.  am^iou- n. —  Vä.:  di  lä jat^ait,  Sü. :  voianam.  |      im  i  ShiinemanJ  jcrai  ärnöxl  i  imm.
g,  ihtgh',  Veibal£:  t.  unter  i<ih-.  |*  g.   säoghav-  m.  dnw.  sSngAa-  1:  ysi
•  g.  stegha-,  aänsba-,  j.  sasha-  m.l!'«»'***^  vasimä  (Sp._i3i5  u.)  mamaata 1)  'pronantiado,  Verkündigung,  Lehre,  I '"f^'S'*' dP-)''  raixMa  aspSnäl  ssdräät Sprach':  hyai  nS  matdä  .  .  gat>äscä  tasö  ■  caxrayB  (sd.)  Y.  jj.  7.
<Ä»Äij(Sp.  665  m.)^^ . . xratäscä . . iyao>a- ,  f^"^^ \'^f/^ nI'/"'"'""' ~  ^ '  ^""^"^ »3/3    •nekascä    Y.  ?/,  11;    —  ^airft'  arA"/'       .      ,    ,         ,  *    '    '-  -  ,,
•nghäUca  yf  xl sjnghsi^-i) ..  V.51.  i
mainyB  .  .  yayä  spanyä  Siti  mravat  ySm ,  arigTTm:  nsit  nä  manä  .  .  'tighä  ,  .  xra- '  tavO  .  .  varana  (sd.)  . .  kacattifl  Y.  4S-  *  j
—  vldvä  yal'U  güerä  (sd.)    'TighanhS  Y.
FrG.
•   j.   titidah-,   g.   sSnda-   n.    i)    *dfcc- tus'.         2)  'perfectio'. KompE.  —  Zam  V.  'sand-.
S3vin-    Adj.  'nützend':    vmnjaoka
T--.  ^  ,  ki V7n>rjm.jä  ^itid  pöi  (sd.)  nama  ahmi  vtr^javä  .  .  'vi  .  ,  sürä  .  . ^ngka  'yei  fanti  Y.44.16;  —  «f  him\irMta  Ytr.  15. mfrq'z^ai  (Sp.  1083 f.)  >wahyä  mqhrais\  A^"""  ""  wo-.  -Pfl.:  «z™.»«'. •tigkakya  Y.44.14'';  —  iaS'j  ..y^j^5«i'?|»  ].,  g.  ssviSta-  Adj.  (fem.  *«-)  'der v^mdait  •f^Ääis  saosyaniqm  xrtüavö  (sd.) !  stärkste,  gewaltigste,  der  am  meisten  ver- ^.46.3.  a)  «ar'  i^.  von  der  niaHschen  j  mag';  a)  von  a)  Menschen  und  ß)  Götterrt; Lehre:    *uzinidyäi    *az3    sarjdana    (sd.)  zu  o):   "/J  bavähi  ydia  masdä  Az.2',  —
•nghahyä  Y.4J.  14.  2)  'Befehl,  Gebot' ySi  xlnüm  (sd.)  . .  halhntl  fyao^anäis  . , %wakya  mazdä  'nghohyä  Y.  4^.  la^';  — .  bavaiti  (Sp.  930  m.)    'ttftsmcit
'krits  sämanqm  '/sM.g.io;  —  moiu..AvövS fitim  baon  'ta  Yt5.98;  7J.38.  zuß): matdä  yS  °IS  v?h^rajä  fradatgaihs  Y. 55.3;  —   '^ridasd  'ta  (nämL  aü/rs)  Yt.
*anujasträi  'ahsmcit  *anu,mainyäi  Yt  j  j.  8 ;  Y.  i6^  i ;  —  jCri  nqma  ahmt /0.137.  3)'richterlicherSpruch,Richter-|(slan  NSm.)  nqma  ahmt  Yt.z.15;  — ys Spruch',  in  eschatologischemSinn:  * sSndä  .  .\°tS  ahurS  matdascü  armatlitcä  "er,  der yS  ll  'ng/iß  ajiJmpm  drüp  dtmünl  Jrtü/  gewaltigste  jV.,^.4.,  und  j^rm,  .."  Y.jij.  1 1 ; "vollstrecke  ..  den  Spruch,  der  sie  am| —  gätümcä  akuräi  *'iJi'^  straohm  (sd.) Ende  in  das  Haus  der  i3rT^f  bringen  wird"  I  ffwai/^/   V.SiS.j;    —    ahuraltl  mazdä   ..
dby  Google
1577
sötStS-
8^-  i
1578
*'taÄi^^  Y.jö'.i;  —  ahurai  masdäi ..°t3m (statt  DS.)  vfnkrayne  fi-üdat^a^äi  Vr. i7. 1 ;  —  ttm  (näml.  mihtvm)  amixüanhm yazat)m  sBrim  damshu  °t>m  YtJO.  6;  13; —  sara  mihra..'ta  Yt  70.  31;  F./2; — tiÜrlm  ..yakmäi  ..fradä^at..lffs'firalsva °täi  YtÄ45;  43,  47;  — fravaslS . . spinta ..  spifüsth  ..  sürä  ..  'tu  Yt7j.75;  147, 31,  34;  —  vartuhi  °U  (VSf.)  andvl  süre ans/Ute  Yl.  5.  18,  130,  Ny.  /.  19;  Yt g,  4.  b)  sonst:  frataan  äps  */i  Yt. 13.  78.
KompE.  —  Superl.  zu  isüra-;  vgl.  Yt  r.  15, ro.  6,  31,  13.  75,  147.  —  ai-  iävif/ha-  Adj.  - Vgl,  säsfi/üta:  -Fi.:  sät  j^astSr»),  tri  (lu Yt.  /.  8] ;  dSmSa  räi  süt  J'Shtm ;  (lU  V.  33) : sültnänä,  erL:  sät  kunänd.  —  ')  NA,  sivtit'; s.  Var.  —  3)  Diese  Übersetzung  -  Sü. :  lä- bhepsuh,  läbkUihilifan  -  lässt  erkennen,  dass ntln  in  üf  nicht  das  Superlativsuffix,  sondern ein  Nomen  sah.  Der  Anlass  daiu  wird  Y, 55.  l :  *irvisiahc  . .  yt  rtä  iil5  gewesen  sein  : süf  J^ätl  ir  .  ,  ke  amäi  j^ästär  i  neTiiaiiA.
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


## [2026-09-06T15:52:47.391Z] TOOL CALL #23: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T15:52:47.397Z] TOOL RESULT

```


```


## [2026-09-06T15:52:50.339Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'sax\\|säx' BRT.txt | grep -i 'lehre\\|paiti' | head -20; echo \"=== search pasox pahlavi PHD\"; grep -n -i 'passox\\|pass|xw\\|pʾsḥw' PHD.txt | head; grep -n -i 'sax(w)an\\|saxwan\\|saxwan\\|passox' PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-06T15:52:50.471Z] TOOL RESULT

```
3216:paiti):  pasax"  guftan,  (mit /lain):    apt  gußati,
20871:das  Relativ  ist  a)  substantivisch:  *katämS , .  pärayätf  y5  (NSm.)  asäi  b?r^jyqshmö "quis  . .?  (is)  qui  .  ."  N. /;  V.  ^.  41;  — alVS  pantä  yd  eisake  "una  est  via:  fea) quae  (est)  veritatts"  Y.  72. 1 1 ;  —  nüil  cahmi saxva  (sd.)  y5  nHit  urune  zasva  FrD._j ;  J ;  — v?hrkäi  hisvqm  datäiH  y3  azrasdäi  *mq- ^nm  (oäeti.iy;  P.  iiV  Yt.6'.4, 70.  139;  — y3  .  .  ndij  fumä  (sd.)  paiti.baraiti  läyus lumanAS  havaiti  "wer..,  (der)  . ."  V.4>  i  i *'-79.  y-  lOi  iii  *Oi  ^5-2ii  24.  'ö".  17, lü.  ro,  1 2 ,  N.  4,  7.  ^4, 15,  3i.  2^,  J/,  J3,
21224:Au.irixt^m(sd.)..trinaxtiYt.io.6B.  a)init' vorhergehendem  vTspum  S  aAm3J  'donec, bis':  näa  difyäi  aäa  ^rityäi  vJsp^m  ä ahmst  y'  hl  han/asaitt  yaia  iahrutiim *yär?  N.42;  43,  Vd..#.  3)  mit  dem Konj.  (oder  Inj.)  in  fiiCuiischem  Sinn:  yai (s.  V)  .  .frasna  (sd.)  paiti.mravSm  y  mgm ftrpsai  axtys  Yt  j.  8z;  —  y  irista  paiti us»hiltqn  ..  äa%aite  fras>m  vasna  anhui Yt  Jp.  1 1 ;  —  y  astvatjTTls  fraxHäite  .  . avaaa  drujpm  nilbarat  Yt  jg.  92  f.;  —  y yavs  dqyät  aal  daeva  :^um  (sd.)  y^  ■  ■ äayap  äaO  ..  V.,;.  32;  —  asti  zT  ana avavai  uxäata  (sd.)  ya'äsa  y  dim  vJsp5 ar»huf  äsaxiat  (sd.)  . .  pairi  irtkyqstätat (sd.)  haraite  Y.ig.  10.  /)  im  Sinn  des lat  Fut  II:  aSaha  hr  tanüm  . .  »idaihyqn vTsppm  3  ahmat  .  .  yat  (s.  c.)  frä  vayS patqn  ,  .  äat  y°  ('wenn')  ht^  frä  vayS patqn  fra  urvara  ux^qn  nysttiä  apa.- tacin  .  .  ariala  .  .  kahrptm  kvanJansJm kmnaot  V.  5.  i  a  £ ;  —  *fra  *ma  . .  *gara- yffi/ (sdj)  y  raful  fritsil  *a/asäi  N.  ip;  — y  dim  iatäj..paia  *avaMääiV.S.too(t); io3(?); — yai  nSiriAa  voAunls  atwi.vamäl y  (nachdem')  Al  'kray3  xlafiia  sacatüe V.  16. 8;  — y  ('nachdem')  kl  tanul  hilkvi Mymii  pqsnu  bavat  pascaSa  .  .  jasBtt  V. p.  31.  a)  mit  vorhei^ehendem  pasca 'postquam':  aem  ai^he  asti  utvanam  yal (s.  V)  nä  pasla  y  usthtÜäi^^  .  .  änV aÄOT  ■  upajtuyät  V.  18.  43;  s.  V.  18.  49 (unter    4).  b)    mit    vorhergehendem
24751:para.iri^yeiti  V.  /j.  50;  —  yat  ahmi  spa- 1  mit  paiti  'mittelbar,  indirekt  in  Beriih- nas^'a  narasca  para.iri>inti  V.6.i;  —  i  rung  treten  mit  -,  Einfluss  üben  auf  -'*> sBnS  vä  para.iristahe  masyehe  vä  V.  G.  \  (Akk.):  cvai  alls  spä  yö  urupis  spmtahe 10,42,  7-24;  —  vJspanqm  ahmya  nmäne\tnaiHy3ui  dämanqm  hqm.rat%wayeiti  cvat fiabänazdisianam  para.iristanqm  ,  .  fravO' \paiti.ra€%wayeiti  "auf  wie  viele  von  den sayB  V.2Ö".7;  —  pasca  /ura./rij/a/r«' Geschöpfen  ..  erstreckt  der  Hund  .  .seinen ma^yeie  pasca  /rasaxtahe{^ä.)  masyehe  V, ;  Einfluss  direkt,  auf  wie  viele  indirekt?"  V, ir).2&;  —  ä  dirn  aoxta..pourvü{%^.iTi  u.)  J.  33.  a)  insbes,  von  ansteckender,  ver-
25868:ai.  iaknili  'er  kann',  iikfoli  'er  lernt'.  —  Pü.: ämöxtan  ■lehren,  lernen';  StL:  üititum.  — '>  S.  No.  6,  7,  *iixsaya-  und  aiiiSant-.  —  ')  i (fit  fy,  S  po-  i  »■  S.  noch  No.  5-  —  ■J'  S  45- -4>  SjJ2— «  So  Pt4,  J2.  Ks.  —  6)NA. saxs' ;  s.  Var.  —  7)  Ausg.  saxi',  aber  gegen Hds. •  j.  'sak-  V.  '(zeitlich)  vorübergehen, -  sein'.    Praes.  i  ivi-»,  2  sa^a-.  —  PPfP.
26155:mit  paili  'sich  wehren  gegen  —  (Akk.), entgegentreten':  nl  als>mS  nl  dy3(a m  (Sp. 761  u.)  pai/i  r>m)m  paiti  * syOdam'^^  "der Raserei  soll  Einhalt  getan  werden!  gegen die  Grausamkeit  wehret  euch"  Y.  48. 7. Et.?    —    Pü.   (tu   Y.  31):    etSn   esän  -  akra- mv^n  —  rai   lä^i')  stüh,    Sü. :   evam  lasmai bhujtna  iatlram  vi^häli^a;  (lu  \ .  4S):  palTrai i  ariSt  fatä-ai  visiaiti),   Sü.j  praiikülam  ir/yä- iutnanufyatya    . .    firalikülain    lisyäfayämi.    — ')  So  P14  usw.;    5.  auch  KZ.  30,  526.    Vgl. Ko.  3.    Das  zweite  fiaiH  ist  nach  dem  Metram als   müssige  Wiederholung    zu   streichen.  — ')  Doch  nur  wegen  des  Anklangs  von  säxäüm an  iiu*  -  wie  man   gewiss  lux  Zeit,    als  die Pu.  gefetligl  wurde,  bereits  statt  säi"  gespro- chen hat,    5,  PJt.   —    J)   Man   las  jedenfalls syaotdam   oder  ähnlich   und  brachte  das  mit
=== search pasox pahlavi PHD
545:pas-dānišnīh [4HLd’nsnyh] anti-knowledge. pasēmāl [psym’l, v. hamemal] defendant, accused. ~ih: (legal) defence. pasen [psyn! | N pasin] final, last. pasox [p’shw' | № ~] = passox. passand [psnd | N pasand] pleasure, liking. passandidan, passand- [psnd-ytn' | M psynd-, N pasandidan] like, approve. ~išn: liking, approval. ~isnig : likeable. passáxt [ps’ht'] test. passaxtan, passàz- [ps’hin', ps’c- | M ps?xt, ps’c-] fashion, prepare; insert; test. ~išn: preparation, constitution. passazag [psck! | M pscg] suitable, fitting. ~ih: suitability. passox [pshw! | M pswx, № pāsux) answer. past [pst' | N ~] low; astr. dejection. pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance. pašm [psm | N ~] wool. ~ёп [-yn! | N ~in] woollen. pašn [psn'] bond, agreement. pāšnag [p’snk! | N ~a] heel. pāšom [p(”)$zvm) excellent. passing [pšng | N pišing] drop, exudation. paššinjag [pfnck! | N pišanja] drop. paššinjīdan, paššinj- [psnc-ytn' | N pišanjīdan) sprinkle. ~išn: sprinkling. pa&t(ag) [pšt(k)! | J pst] pact, bond, agreement. *pattān [pt’n'] noise, resonance. ~6mand [отта] resonant. pattāyistan [pi?dstn'] = pattüdan. pattüdan, pattày- [ptwtn', ptd- | P ptwdn, M pt’y-] stay, remain, last, endure. pattüg [ptwk'] enduring, patient, persevering. ^АҺһ: endurance, patience, perseverance. paxSag [phšk! | N pasa] mosquito, gnat. 1рау [pdy | N ~] foot; footstep, track. ~ 1: after. *pay [pdy | M pyy, N ~] sinew, tendon. pay [LGLE < А rglh; p'dy | M p'y, N —] foot, leg; foot (12 in.). 1,2 páy-, у, bL? pādan. payādaģ [pd’tk! | М py’dg, N piyada] on foot, foot-soldier, (chess) pawn. payag [p'd(y)k! | N paya] base, station. paydag [pyt?k! | M pyd'g, N payda] visible, obvious, revealed.
798:answer (n.) passox, (pásox).
4644:frašn frašagirdīg frašagird frašamurw fradāg fradom fradomīh pardag pambagén pambag passaxt passáxtan passox passáz- passāzišn pasen pasēmāl pasēmālīh brin-t bridan™ passazagih passazag past, pist pistag
PHD.txt:312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
PHD.txt:545:pas-dānišnīh [4HLd’nsnyh] anti-knowledge. pasēmāl [psym’l, v. hamemal] defendant, accused. ~ih: (legal) defence. pasen [psyn! | N pasin] final, last. pasox [p’shw' | № ~] = passox. passand [psnd | N pasand] pleasure, liking. passandidan, passand- [psnd-ytn' | M psynd-, N pasandidan] like, approve. ~išn: liking, approval. ~isnig : likeable. passáxt [ps’ht'] test. passaxtan, passàz- [ps’hin', ps’c- | M ps?xt, ps’c-] fashion, prepare; insert; test. ~išn: preparation, constitution. passazag [psck! | M pscg] suitable, fitting. ~ih: suitability. passox [pshw! | M pswx, № pāsux) answer. past [pst' | N ~] low; astr. dejection. pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance. pašm [psm | N ~] wool. ~ёп [-yn! | N ~in] woollen. pašn [psn'] bond, agreement. pāšnag [p’snk! | N ~a] heel. pāšom [p(”)$zvm) excellent. passing [pšng | N pišing] drop, exudation. paššinjag [pfnck! | N pišanja] drop. paššinjīdan, paššinj- [psnc-ytn' | N pišanjīdan) sprinkle. ~išn: sprinkling. pa&t(ag) [pšt(k)! | J pst] pact, bond, agreement. *pattān [pt’n'] noise, resonance. ~6mand [отта] resonant. pattāyistan [pi?dstn'] = pattüdan. pattüdan, pattày- [ptwtn', ptd- | P ptwdn, M pt’y-] stay, remain, last, endure. pattüg [ptwk'] enduring, patient, persevering. ^АҺһ: endurance, patience, perseverance. paxSag [phšk! | N pasa] mosquito, gnat. 1рау [pdy | N ~] foot; footstep, track. ~ 1: after. *pay [pdy | M pyy, N ~] sinew, tendon. pay [LGLE < А rglh; p'dy | M p'y, N —] foot, leg; foot (12 in.). 1,2 páy-, у, bL? pādan. payādaģ [pd’tk! | М py’dg, N piyada] on foot, foot-soldier, (chess) pawn. payag [p'd(y)k! | N paya] base, station. paydag [pyt?k! | M pyd'g, N payda] visible, obvious, revealed.
PHD.txt:564:sang [KYPA < A kyp’; CCA (in error); sng | (P?sng), N ~] stone, rock. -~sar [-s?1] stony place. sanj-, v. saxtan. sanwar [snwl = Av. 0anwar-] bow. sar [LOYŠE < A r'šh; sl | M sr, N ~] head; top, summit; end, begin- ning. | sarāsar [s?s] | N ~] from end to end. sard [s/t! | M srd, N ~] cold. ^Àh: coldness. sardag [sltk' = Av. sarada- | (M s’rg), J srdg] sort, kind. sardsér [s/tsyl | N ~] cold region, uplands. sārēnīdan, sárén- [s’/yn-ytn'] provoke. sargen [slgyn' | N sargin] dung, manure. sarmāģ [s/m?k! | N затта] coldness. sarw [slw(b)' | M srw, N ~] cypress. sas [ss | N ~] bug. sāstār [s”st”7 | P s?s?r] commander; tyrant. ~ih: tyranny. Sawah [sw’h = Av. sawahi-] the western continent of the earth. saxt [sQ)At! | N ~] strong, hard, severe(ly); very. “Аһ: strength, severity. saxtag [shtk! | (N saxtiyán)] morocco leather. saxtan, ѕапј- [s’htn', snc- | N ~] weigh. sāxtan, sáz- [s*htm!, ?c- | (P s?*c-), N ~] make, prepare; tolerate. sāxtārīh [Pht yh] toleration, forbearance. saxwan [МРУА < А mly’; shwn' | М sxwn, N suxan] word, speech. say-, v. südan. sayag [sg dk! | M ғур, N sáya] shade, shadow. lsaz- [sc- | M sz-, N ~] be fitting, proper, worthy. --i$n(ih): fitness, worthiness. 26а2-, —išn, v. sazistan, saz-, v, sáxtan. sazāģ [sk | N sazá] fitting, worthy. ~th: fitness, worthiness. ~ ~war [-w/ | N sazāwār] = затар. sazistan, *saz- [sc-stn'] pass. ~išn: passing, transience. ~iSnig : transient, perishable, mortal. sé [3; TLTA < А tl? | M sh, N si] three. sëb [syf | N ~] apple. sēj [sye = Av. 'Gyejah- | N ~) danger, trouble. --ómand [-”zvmnd | N —mand] dangerous. sel [si | N —] spear, javelin. sém [sym | N —] — asém. !sén(ag) [syn(k)! | N sina] breast, chest. *sén murw [synmzlw | (N simury)] a fabulous bird.
PHD.txt:798:answer (n.) passox, (pásox).
PHD.txt:1509:deceitful dēsaxwan, zūr.
PHD.txt:3766:speech dranjišn, gēwišn, guftārīh, saxwan, waz; v. good, evil.
PHD.txt:4106:two-tongued dó-saxwan. Lyrannous sézd(én), statt, tyranny sāstārīh, sēzd, tyrant sāstār,
PHD.txt:4343:word ēwāz, mārīg, saxwan, sraw, waz; holy ~ máàns?r(spand).
PHD.txt:4644:frašn frašagirdīg frašagird frašamurw fradāg fradom fradomīh pardag pambagén pambag passaxt passáxtan passox passáz- passāzišn pasen pasēmāl pasēmālīh brin-t bridan™ passazagih passazag past, pist pistag
PHD.txt:4816:saxwan sahóg
PHD.txt:4871:1 az! muhrag mang, moy saxwanī moyén tis’, cis! tis-izt moyag muhr osmar-t бёгпагї$пї O$murdan! ket murdar mog
PHD.txt:5433:gumēzagīh gumczag gumēzišn ёп! röz-šabän! dósaxwan dūsēn: stiin-t stadant dusrawih dusraw
PHD_mackenzie.txt:2014:do-saxwan [2 shwn ] two-tongued, deceitful.
PHD_mackenzie.txt:4085:pasox [p)shw I N --] = passox.
PHD_mackenzie.txt:4100:passox [pshw 1M pswx, N pasux] answer.
PHD_mackenzie.txt:4521:saxwan [MRYA < A mly'; shwn l 1M sxwn, N suxan] word, speech.
PHD_mackenzie.txt:5966:answer (n.) passox, (piisox).             arrive rasidan.
PHD_mackenzie.txt:6335: currency rawagih.                         deceitful dosaxwan, zur.
PHD_mackenzie.txt:7665:    saxwan, wiz; v. good, evil.        stem wan, (bun); v. stalk.
PHD_mackenzie.txt:7841:two-tongued do-saxwan.                   unlike ahomiinag.
```


## [2026-09-06T15:52:58.673Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%AE%D9%86",
 "prompt": "Give the full Persian etymology section for سخن (soxan): Middle Persian form, Proto-Iranian/Proto-Indo-Iranian reconstruction, PIE root, and any cited authorities (Hasandust, Cheung, MacKenzie). Also any Avestan cognate."
}
```


## [2026-09-06T15:53:00.207Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B3%D8%AE",
 "prompt": "Give the full Persian etymology of پاسخ (pāsox): Middle Persian form, prefix, root, Proto-Iranian reconstruction, PIE root and cognates."
}
```


### [2026-09-06T15:53:05.061Z] TOOL RESULT

```
# Persian Etymology for سخن (soxan)

Based on the Wiktionary content provided, here is what the article contains:

**Proto-Iranian origin:** The entry states the word comes "Ultimately from Proto-Iranian *cánhati"; see there for more."

**Cognates listed:**
- Sanskrit शंसति (śáṃsati, "to declare")
- Latin cēnseō
- Ancient Greek κῶμος (kômos)

**Important limitation:** The article explicitly notes there is a cleanup request for this Persian section, with the comment: "ultimately from X, but see there for more?" This indicates the etymology section itself is flagged as incomplete or needing improvement.

The provided content does not include:
- Middle Persian form
- Complete Proto-Indo-European reconstruction details
- Citations to Hasandust, Cheung, or MacKenzie
- Avestan cognates

The Wiktionary article directs readers to the Proto-Iranian entry for fuller etymological details, but that reconstruction page's content is not included in the material provided.
```


### [2026-09-06T15:53:05.726Z] TOOL RESULT

```
# Persian Etymology of پاسخ (pāsox)

**Middle Persian forms:** The word derives from multiple Middle Persian spellings: pshw' (/passox/), pʾshw' (/pāsox/), and 𐫛𐫘𐫇𐫟 (pswx /passox/).

**Proto-Iranian reconstruction:** From "paticahwaH," which breaks down with the root "cánhati" meaning to speak or recite.

**Proto-Indo-European root:** Ultimately traced to "ḱens-," related to perception and judgment.

**Cognates:** The term shares linguistic ancestry with Sanskrit शंसति (śaṃsati) and Latin cēnseō, all stemming from the same ancient Indo-European verbal root concerned with speaking, praising, or evaluating.
```


## [2026-09-06T15:53:19.671Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/c%C3%A1nhati",
 "prompt": "Full content: the reconstruction, meaning, PIE root, Avestan/Old Persian descendants, and the derived nouns (like *sáxwan-, *pati-sáxwah-) with their Middle Persian and New Persian outcomes."
}
```


## [2026-09-06T15:53:22.145Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'saxvan\\|sax\\^van\\|saxv' BRT.txt | head -20; echo \"=== CHEUNG sah / canh\"; grep -n 'sanh\\|canh\\|\\*sah\\|SAH\\|CANH' CHEUNG.txt | head -20"
}
```


### [2026-09-06T15:53:22.204Z] TOOL RESULT

```
20871:das  Relativ  ist  a)  substantivisch:  *katämS , .  pärayätf  y5  (NSm.)  asäi  b?r^jyqshmö "quis  . .?  (is)  qui  .  ."  N. /;  V.  ^.  41;  — alVS  pantä  yd  eisake  "una  est  via:  fea) quae  (est)  veritatts"  Y.  72. 1 1 ;  —  nüil  cahmi saxva  (sd.)  y5  nHit  urune  zasva  FrD._j ;  J ;  — v?hrkäi  hisvqm  datäiH  y3  azrasdäi  *mq- ^nm  (oäeti.iy;  P.  iiV  Yt.6'.4, 70.  139;  — y3  .  .  ndij  fumä  (sd.)  paiti.baraiti  läyus lumanAS  havaiti  "wer..,  (der)  . ."  V.4>  i  i *'-79.  y-  lOi  iii  *Oi  ^5-2ii  24.  'ö".  17, lü.  ro,  1 2 ,  N.  4,  7.  ^4, 15,  3i.  2^,  J/,  J3,
=== CHEUNG sah / canh
9158:*IE COGNATES: Hitt. /sanh-/ ‘to mean, to want, to search’, Gr. dvbo, буо, буор ‘I 
21653:interjection *Kem (related to *Kens- ?, *sanh). 
21862:scandö/scänsus ‘to climb, rise’, or rather from *Kens- (s.v. *sanh) ? 
21865:334 *sanh 
21873:*sanh ‘to declare, explain’ 
21879:songhaite (Y 32.7), YAv. sanhaite (V 18.1), 1р1. OAv. songhamahi (Y 31.1), INJ. 3sg. YAv. sanhat (V 
21880:22.8, V 22.13 f£), SUBJ. 1sg. OAv. sanghani (Y 46.17), Y Av. saghani (Vyt 13), OPT. 25р. YAv. sanhöis 
21881:(V 22.7), med. 2sg. YAv. paiti.sanhaéSa (Yt 14.35); Aor. athem.: OPT. 3sg. OAv. saxiiat (Y 44.1, Y 
21884:sasanhan (V 2.16). 0 OAv. sazdiiai may have a different etymology, viz. from *sand. 
25971:(Y 11.7), med. 2sg. YAv. upa.0Bərəsanha (У 17.4), 3sg. YAv. frä0Borosat (Yt 10.50, Yt 13.87), SUBJ. 
26174:13.88), perf. pass. uxóa- (Y 32.9, Y 33.14, Y 45.8, etc.); Inf.: aor. OAv. vaocanhé (Y 28.11); Pass.: aor. 
33716:songh-, sanh-, 334 
52179:/sanh-/, 128 
56286:*sanh 
56499:*sanh
```


### [2026-09-06T15:53:27.992Z] TOOL RESULT

```
# Proto-Iranian *cánhati

This Wiktionary entry documents a reconstructed Proto-Iranian verb meaning "to declare, explain."

## Etymology & Roots

The term derives from Proto-Indo-Iranian *ćánsati, ultimately from the Proto-Indo-European root *ḱens- ("to announce, proclaim"). It shares cognates with Sanskrit śáṃsati, Latin cēnseō, and possibly Ancient Greek kômos.

## Key Descendants

The verb produced important derived nouns that spread across Iranian languages:

- **Word/Speech noun** (*cánhuš): evolved into Old Avestan sə̄ṇγu, Middle Persian saxwan, and Classical Persian suxan
- **Answer/Response noun** (*paticahwaH): developed into Pashto poṣtena, Persian pāsux, Kurdish bersiv, and through borrowing into Armenian patasxan and Georgian ṗasuxi

## Linguistic Significance

"This Proto-Iranian entry contains reconstructed terms and roots" based on comparative evidence rather than direct attestation. The entry provides extensive inflection tables showing active and mediopassive voices across various moods and persons, demonstrating the verb's thematic present structure in Indo-European morphology.

The term's widespread descendants across Central, Northeastern, Northwestern, and Southwestern Iranian branches illustrate how ancient root vocabulary maintained continuity through millennia of language evolution.
```


## [2026-09-06T15:53:31.399Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21865,21920p' CHEUNG.txt"
}
```


### [2026-09-06T15:53:31.443Z] TOOL RESULT

```
334 *sanh 


*REFERENCES: TFL П: 539; Abrahamian 1936: 118; EVS: 61b; WIM I: 71; WIMII/1: 81; DKS: 418b f., 
224b; Werba 1997: 185; Paul 1998: 291b; Steblin-Kamenskij 1999: 320; Kümmel 2000: 181 ff.; Lecoq 
2002: 124 


*sanh ‘to declare, explain’ 

*AVESTAN: songh- (ѕарһ-) ‘to declare, explain’ || (+ *abi-) ‘to call names, curse’ || (+ 
*pati-) ‘to call up, invoke’ = Liste: 62 

Pres. them.: IND. 15р. YAv. paiti.sayhämi (V 20.7), 3sg. OAv. songhaiti (Y 43.6), med. 3sg. OAv. 
songhaite (Y 32.7), YAv. sanhaite (V 18.1), 1р1. OAv. songhamahi (Y 31.1), INJ. 3sg. YAv. sanhat (V 
22.8, V 22.13 f£), SUBJ. 1sg. OAv. sanghani (Y 46.17), Y Av. saghani (Vyt 13), OPT. 25р. YAv. sanhöis 
(V 22.7), med. 2sg. YAv. paiti.sanhaéSa (Yt 14.35); Aor. athem.: OPT. 3sg. OAv. saxiiat (Y 44.1, Y 
44.9); Partic.: perf. pass. YAv. aißi.sasta- (Yt 14.34); Inf.: aor. OAv. sasté (Y 30.8, Y 46.12), ? OAv. 
sazdiiai (Y 30.2, Y 51.16); Intens.: impf. IND. 3sg. ? YAv. asasat (V 19.15, V 19.35), SUBJ. 3р1. ? YAv. 
sasanhan (V 2.16). 0 OAv. sazdiiai may have a different etymology, viz. from *sand. 

*OLD PERSIAN: Oa" h- ‘to declare, say’. Ф According to Kuiper 1960: 159 ff., OP 0atiy 
is derived from a separate root, but see also Hoffmann (apud Goto 1987: 303, fn. 
721). = Kent: 188a 

Pres. them. {1}: impf. IND. 1sg. аба"ћат «a-0-h-m» (DB 2.30, DB 2.50, DB 2.83, etc.), «[a]-[0]-h-m» 
(DB 2.20), Zeg. a6a"ha «a-0-h» (DB 1.75, DB 2.15, DB 2.80, etc.); Pres. athem. (2): IND. 2sg. Өяһу 
«0-a-h-y» (DB 4.55, DB 4.58), 3sg. Oätiy «0-a-t-i-y» (DB 1.6, DB 1.8, DB 1.11, etc.), IMPV. 2sg. ? 
“@adiy (DB 4.54); Pass.: pres. IND. Ipl. 0ahyamahy «0-h-y-a-m-h-y» (DB 1.7), «0-[h]-y-a-m-h-y» (DBa 
10), impf. 3sg. adahya <а-0-һ-у> (DB 1.20, DNa 20), <a-0-h-y> (DB 1.23); Inf.: 0astanaiy <0-s-t-n-i-y> 
(DB 1.53) 

*MIDDLE PERSIAN: MMP sxwn, ВМР shwn (MR Y?) /saxwan/ ‘word, speech’ || (+ 
*pati-) MMP pswx, BMP pshw /passox/, p’shw /pasox/ ‘answer’? = DMMPP: 311, 
284a 

*PARTHIAN: sxwn ‘word, saying, utterance’ || (+ *pati-) pswx ‘answer’ = DMMPP: 
311, 284a 

*KHOTANESE: samja- ‘document’ 

*SOGDIAN: BSogd. sywn- ‘to utter, recite’, SSogd. sxwn, BSogd. sywnw ‘word, 
speech’ 

Inf.: BSogd. sywn’y 

*NWIR: NP suxan, saxun ‘word, speech’ || (+ *pati-) NP päsux, Bal. pas(s)aw 
‘answer’ 

*MISC: (+ *pati-) Arm. (LW) patasxani ‘answer’ (cf. Bailey 1930: 19) 

*SANSKRIT: Sams ‘to praise, recite’ (RV+) = EWAia II: 599 

«PIE *Kens- ‘to announce, proclaim’. > Perhaps, *Kens- (or *Kems-) is an old 
ingressive s-formation of *Kem- (*sam), which would be continued by Ir. only. 
c LIV: 326 | Pok.: 566
```


## [2026-09-06T15:54:11.567Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD kišwar\"; grep -n -i 'kišwar\\|kiswar\\|kišvar' PHD.txt PHD_mackenzie.txt | head -5; echo \"=== NYB\"; grep -n -i 'kiswar\\|kišwar\\|sāstār\\|sastar\\|saxwan\\|passox\\|pasox' NYB_vol2_glossary.txt | head -20; echo \"=== KNT karsvar\"; grep -n -i 'karsvar\\|karšvar' KNT.txt | head -5; echo \"=== SOD kysf\"; grep -n -i 'kyšf\\|kysf\\|kyšph\\|tortoise' SOD.txt | head -10"
}
```


### [2026-09-06T15:54:11.657Z] TOOL RESULT

```
=== PHD kišwar
PHD.txt:392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
PHD.txt:1253:clime kišwar.
PHD.txt:3360:region kišwar; v. district.
PHD.txt:4150:universe hamkišwar.
PHD.txt:5050:4915 | keš- AD $915 kēšdār 1$ 195 kešīdan w^ 1835513 kišwān Wis kišwānzār 14519 kišw 1.32514 kišwar = leo AA kišwzār WE ме 1 4 kištan us- kédigih vs kid ~114 nag, -ak "ua oh!
=== NYB
3407:sastar [s'st?]] ruler, tyrant, of infidel (non-mazdayasnian) sovereigns, pl. cas. obl. ~-dn 614. — In this sense probably borrowed from Av. (1573) sāstar-; M Prth s?st?r ‘master, lord’ (A-H III, BBB).
3408:sāstārēh bad domination, tyranny 109%.
5331:sastar-: sastar
=== KNT karsvar
=== SOD kysf
41578:tortoise 
94714:tortoise     5125
```


## [2026-09-06T15:54:19.322Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '41570,41590p' SOD.txt; echo \"=== 94700\"; sed -n '94705,94720p' SOD.txt; echo \"=== grep kysp\"; grep -n 'kyšph\\|kysph\\|kyšp\\|kysp' SOD.txt SOD_pages.txt | head -10"
}
```


### [2026-09-06T15:54:19.410Z] TOOL RESULT

```
country 

GMS  241;  >flt-kysp(>\  TSP  3.207;  -kyspyh,  GMS 
147 

5125  kysph    B  j^*c^JV 
kis(a)p  ©<Av.  kasyapa 

tortoise 

SCE  157,  353;  GMS  192 

5126  kystyc   M  c~if  tjjzif 
ko/iste/ic,  kistlc   (qystyc)  ©ob.  -y   ^kst'ych 
field,  cultivated  field 

BBB  570;  GMS  147,  1010 

5127  qystyc  =*  kystyc 

5128  kysty(y)   S,  M  jf  3c^f  t^s  <>L  <o^T 
=== 94700
tooth     3554,  3555 
top    8780 
topknot     10231 
torch     1827,  3545 
torment     387,  8101 
(fo)torment     8131 
tormented     361,  8976 
torn     11429 
torn  apart     7855 
tortoise     5125 
torture     1876,  4145,  501 1,  9634, 

9986,11175 
torture  instrument    6681,  7921, 

7945 
=== grep kysp
SOD.txt:11061:550  'ptkysp(h)   B,  M  j^f^J^ 
SOD.txt:11070:551  *ptkyspy  xwtNv   M       ^((j-^U^/ai-  fOJj^if  c*iA  »U. 
SOD.txt:13107:(s)kosp   ©Av.  kdhrp   ^kysp,  ky6rp 
SOD.txt:13114:'kysp 
SOD.txt:13131:868  >kysp   B 
SOD.txt:41567:5124  kysp  B,  M  ^ 
SOD.txt:41572:GMS  241;  >flt-kysp(>\  TSP  3.207;  -kyspyh,  GMS 
SOD.txt:41575:5125  kysph    B  j^*c^JV 
SOD_pages.txt:5318:    apd CptVh) ©<hafta                                   550 'ptkysp(h) B, M                                j^f^J^
SOD_pages.txt:5326:                                                         551 *ptkyspy xwtNv     M       ^((j-^U^/ai- fOJj^if c*iA »U.
```


## [2026-09-06T15:54:21.184Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'kar[sš]' KNT.txt | head -10; echo \"=== HRN 191 leaf check for kesef\"; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in [7456]:\n    idx=sum(len(l)+1 for l in lines[:ln-1])\n    print(ln,'leaf',t[:idx].count('\\f'))\nEOF"
}
```


### [2026-09-06T15:54:23.563Z] TOOL RESULT

```
1788:VI. The vocalism of the root varies in these for- mations, being either -a- (pIE -e- or -о- or -a-), as in baga-, bara-, daiva-; or à zero grade, as in karša-, u-zma-, darga- (see Lex. s.vv.); or a vriddhied or lengthened grade (§126), as in kdma-, asa-bāra-, Margava-.
2075:айа DB 1.28, XPh 49, 52, when used with pari-ay- ‘respect’, is probably inst. rather than abl., because of the lack of prep. Ласа; note that the text of DSe 37-9, as now restored, gives no support for the abl. in the other passages, despite my remarks JAOS 54.46, Lg. 13.308, JAOS 58.117. On inst. sg. karšā, loc. sg. karšayā, nt. асе. casam, acc. pl. ufrasta-diy, see Lex. s.vv.
2238:1! Nom. hamiciya DB 2.93 is predicate to two singular masculine nouns, but is more probably plural than dual; ef. $259. ? The form karšā does not belong here, nor probably artá-cà brazmanty (if во normalized) nor tau- mani-Saty; on these words see the Lexicon s.vv. * On these forms, cf. Kent. Lg. 19.225;
2715:D. Alone, to express specification: DNb 40f yãumainiš amiy ша daslaibuyü ша pādaibiyā ‘trained am I both as to hands and as to feet’. So also with numerals: DB 2.56 Andmakahya mahyd XV raucabi$ 6akatà aha ‘of the month Anamaka, 15 by days were past’; Wa 1 IT karšā ‘2 (units) by weight’; cf. Lg. 19.227-9.
4770:1 CXX karšayā.
4782:| Wd = Darius, Мант р. 1 LX karsayà
5284:karSa- sb. ‘weight, (unit by) weight’ (like Lt. pondo, Lg. 19.227-9), = 83.33 gr. or slightly less than 3 oz. avoirdupois (Gray, JAOS 20.55; Sehmidt, Treasury of Persepolis 62): Skt. karga- ‘pull, unit by weight’ (§29.n2, $80, $1431, VI). The OP kar$a- was one-sixth of the Babylonian mana ‘mina’ (weight; not unit of value). Elam. transcribes kur-Sa-wm, = kršam, which may mark the word as netter, since Elam. transcriptions commonly represent the nom. sg. of the foreign word; but the other evidence is rather for the masc. karšā ism. (§252D; Lg. 19.227-9; not ndm.) Wal. karíayá lsm. (§251C; Lg. 19.227-9; not npm.) We 1; Wd 1.
=== HRN 191 leaf check for kesef
7456 leaf 212
```


## [2026-09-06T15:54:34.015Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '5125 kysph' SOD_pages.txt; awk 'BEGIN{RS=\"\\f\"} /5125  kysph|5125 kysph/{print NR}' SOD_pages.txt"
}
```


## [2026-09-06T15:54:34.667Z] TOOL CALL #34: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py; ls data/verification/sources/refs/ocr/ 2>/dev/null | head"
}
```


### [2026-09-06T15:54:35.932Z] TOOL RESULT

```
18275:   5125 kysph B                                j^*c^JV        5142 kyy' M ^ ky>
270
```


### [2026-09-06T15:54:35.972Z] TOOL RESULT

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
AFM
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
```


## [2026-09-06T15:54:42.310Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls ocr/BQT | head -40; echo \"=== v3 pages head\"; grep -n '\\[pdf page' incoming/BQT/BQT_v3_pages.txt | head -3; grep -n '\\[pdf page' incoming/BQT/BQT_v4_pages.txt | head -3; echo \"=== v1\"; grep -n '\\[pdf page' BQT_v1_pages.txt | head -3"
}
```


### [2026-09-06T15:54:42.388Z] TOOL RESULT

```
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1219.png
1219.txt
1219.vision.txt
1223.png
1223.txt
1225.png
1225.txt
1225.vision.txt
1226.png
1226.txt
1275.png
1275.txt
1280.png
1280.txt
1280.vision.txt
1294.png
1294.txt
1294.vision.txt
1299.png
1299.vision.txt
1300.png
1300.txt
1300.vision.txt
1302.png
1302.txt
1302.vision.txt
1339.png
1339.txt
1357.png
1357.txt
1382.png
1382.txt
1385.png
1385.txt
1385.vision.txt
=== v3 pages head
1:[pdf page 1]
3:[pdf page 2]
24:[pdf page 3]
1:[pdf page 1]
2:[pdf page 2]
23:[pdf page 3]
=== v1
```


## [2026-09-06T15:54:43.506Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json; d=json.load(open('refs_online.json'))\nprint(json.dumps(d['BQT'].get('scans'), ensure_ascii=False, indent=1))\nprint(json.dumps(d['BQT'].get('page_offset'), ensure_ascii=False))\n\""
}
```


### [2026-09-06T15:54:45.450Z] TOOL RESULT

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
"vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...')."
```


## [2026-09-06T15:54:59.698Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== کاتوره v3\"; grep -n 'کاتوره\\|كاتوره' incoming/BQT/BQT_v3_pages.txt | head; echo \"== کشور v3\"; grep -n 'کشور\\|كشور' incoming/BQT/BQT_v3_pages.txt | head -5; echo \"== کشف v3\"; grep -n 'کشف' incoming/BQT/BQT_v3_pages.txt | head -5; echo \"== پاسخ v1\"; grep -n 'پاسخ' BQT_v1_pages.txt | head -5; echo \"== ساستا v2\"; grep -n 'ساستا' BQT_v2_pages.txt | head -5; echo \"== سخن v2\"; grep -n 'سخن' BQT_v2_pages.txt | head -5"
}
```


### [2026-09-06T15:54:59.828Z] TOOL RESULT

```
== کاتوره v3
25331:«کاتوره » سر گشته (سر کشتگی . ظ.) بود. رودکی ( سمرقندی ) گوید :
25332:هیچ ‎Col‏ می ینم در سرود ورود تو ج زکه ازفرباد وزخمه‌ات خلق را کاتوره خاست.»
== کشور v3
113:‎TMA F‏ ه محمد پادثاه متخلص به شاد. ۳ مجلد . مطیم تولکشور. لکهنو
3823:ختنی«نسونه" (روز کارنو ج) شمار۴# : کشورختن بقلم ‎hy‏ ورك: ‎beats‏ کثاب ‎les ploy pole‏
7617:‏کشور عیلام قدیم بود و بهمین مناسبت میلام را « سوزبان » با «شوشان © هم خوانده‌اند . شوش
8208:‏که در اوستا ویارسی باستان وسالسکریت بمعنی کشور وپادشاهی است (رله: شهر) وجزو دوم صفت
8210:‏مر کب یمنی کشور منتخب با پادشاهی بر گزبده . ايين کیب بار ها در اوستا بمعنی بهشت با
== کشف v3
32405:پشت وکاسه پشت و کشف باشد .
32564:کشف = ‎ce‏ اول و ثالی وسکون فا »
32587:کشفته * ‎pee‏ اول ‎JE»‏ بر وزن
32619:‎. ) ‏است . ۷ رك : کشفته . و بمعنی اخیر بفتح اول وثالی ص شکفتن ( شکافتن‎ peel
32621:‏۸ - اسم مقعول «کشفتن »:
== پاسخ v1
1116:چنین داد پاسخ که در کنج شاه یکی ساده صتدوق دیلم سباه
4855:۲- استاد مذ کور در پاسخ سو الات نگار نده‌بادداشت هالی نوشنه است که با
6794:فزونی در نامه مورخ ٩‏ خرداد ۵ در پاسخ ثکارنده نوشته‌اند : « تضیر آقای دهحذا آخر
22717:است. و پاسخ وجوابرانیز کویند*۱» وباین معنی
23329:پاسخ؟ -
== ساستا v2
31757:‫بارساء‬      ‫بروزن‬   ‫یا تای فرشت‬   ‫‪= ۴‬‬   ‫ساستا‬              ‫لسکن اکنید‌درازتر ازآن عیباشد»وا تراسالیون‬
== سخن v2
27:‫نآکو سخنیم بیاموزد مرا‬
408:                                       ‫باشذد ‪.‬‬              ‫وسخن ضیح وبلیغ را دز کونند‪# .‬‬
742:                                      ‫اکر موری سخن کوبد و کر موبی روان دارد‬
743:            ‫من‌آن‌مور سخن گویم» من‌آن موم که جان‌دارد‪.‬‬
1728:                                            ‫ات ‪2‬‬    ‫و کنایه ازسخنان خوب و لطیف هم همست ‪-‬‬
```


## [2026-09-06T15:55:08.141Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,io\ndef ctx(path, lineno, before=8, after=8):\n    lines=open(path,encoding='utf-8',errors='replace').read().split('\\n')\n    tag=None\n    for i in range(lineno-1,-1,-1):\n        m=re.match(r'\\[pdf page (\\d+)\\]', lines[i].strip())\n        if m: tag=int(m.group(1)); break\n    print(f'--- {path} line {lineno} pdfpage={tag}')\n    for l in lines[max(0,lineno-1-before):lineno-1+after]:\n        print(l)\nctx('incoming/BQT/BQT_v3_pages.txt',25331,10,8)\nprint('=====')\nctx('incoming/BQT/BQT_v3_pages.txt',32564,6,14)\nEOF"
}
```


### [2026-09-06T15:55:10.157Z] TOOL RESULT

```
--- incoming/BQT/BQT_v3_pages.txt line 25331 pdfpage=348
ومقارها جای سازند وبعبادت خدای‌تعالی کسب

‏۱ ۰ کاث . باقوت در ممجم‌البلدان کوید : « ممتی الکات باة اهل خوارزم الحائط
فی‌السحراء من فیران‌بحیطبه‌شیه. وهی‌بلدة کبيرة من نواحی‌خوارزملاانها من شرقی جیحون جمیع
‎o's‏ خوارزم ‎Lily‏ هی‌من ناحية جیحون الغريية » و بی نکاث وک رکانج ‎Aas‏ خوارزم عشرون
فرسخاً .» ۴ - ‎ul‏ معثی ‎Esl,‏ دساتیر « فاب64۷:۱ « فرهنگگ دساتیرض۷۵۹.

‏۴ - بهردومعنی عربی است . راك : منتهی‌الارب » محیطالمحیط , تاج‌العروس.

‏۴ -قی : ساننکریت ‎katara‏ ( ترسو » کمرو »گیج ؛ مضطرب)«وبلیامز ۴۱:۲۷
«کاتوره » سر گشته (سر کشتگی . ظ.) بود. رودکی ( سمرقندی ) گوید :
هیچ ‎Col‏ می ینم در سرود ورود تو ج زکه ازفرباد وزخمه‌ات خلق را کاتوره خاست.»

‏« لفت ‎“tol yg‏
درین بیت بمعنی س رگشته وواله است :
‎OT‏ بلبل کانوره برجسته زمطمورء چون دسته‌تنبور» گیرد شجراز چنگل.
« منوچپری دامغاتی ۱۷۹ > .
- این اسطلاح را از شاهنامه کرفته‌اند . فردوس ی گوید ( شاهنامةٌ بخ ج+س4؟) :
=====
--- incoming/BQT/BQT_v3_pages.txt line 32564 pdfpage=444
> خاقالی شروانی س ۲۳ > .
‎olay (‏ فاطع ۲۱۱)
[pdf page 444]
-1۱1۵۱-

وجابه ‎Lub‏ و اشارت را نیز گفته‌اندا .
کشف = ‎ce‏ اول و ثالی وسکون فا »
‎SY‏ پشت ‎ob,‏ پشت را کویند؟ - وبرج‌سرطان
را نیز ‎oT, ala”‏ برج چهارم است از ‎he‏
‎oil‏ برج فلکی؟ - و کوزة سریهن دهان ‎CD‏
‏باشد ‎lade LT,‏ هم میگوبند - و نم کوهی
‎ath‏ و بعربی کوه را جبل گویند (۱) - و بضم
اول و سکون ثالی, بمعنی سیم و نقر# سوخته
وسواد زرکری؟ ‏ - وزفت بآشد که برسر کچلها
چبانند ۴ .
شفت * - بنتح اول و انی وسکون
الث وفوقانی » بمعنی برا کنده و پربشان باشد
و ماضی ‎GET‏ هم هست یعتی پراکنده کرد
‎olen,‏ ساخت و پژمرده گردالید ؛ و بضم ‎Jal‏
‎gl,‏ هم کفته‌الد - وم اول و کسرثالی؛ عبات
```


## [2026-09-06T15:55:26.170Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=re.split(r'\\[pdf page (\\d+)\\]', t)\nd={}\nfor i in range(1,len(pages),2):\n    d[int(pages[i])]=pages[i+1]\nfor p in (444,449,450):\n    print('######## pdf',p)\n    print(d.get(p,'MISSING')[:3500])\nEOF"
}
```


### [2026-09-06T15:55:28.327Z] TOOL RESULT

```
######## pdf 444

-1۱1۵۱-

وجابه ‎Lub‏ و اشارت را نیز گفته‌اندا .
کشف = ‎ce‏ اول و ثالی وسکون فا »
‎SY‏ پشت ‎ob,‏ پشت را کویند؟ - وبرج‌سرطان
را نیز ‎oT, ala”‏ برج چهارم است از ‎he‏
‎oil‏ برج فلکی؟ - و کوزة سریهن دهان ‎CD‏
‏باشد ‎lade LT,‏ هم میگوبند - و نم کوهی
‎ath‏ و بعربی کوه را جبل گویند (۱) - و بضم
اول و سکون ثالی, بمعنی سیم و نقر# سوخته
وسواد زرکری؟ ‏ - وزفت بآشد که برسر کچلها
چبانند ۴ .
شفت * - بنتح اول و انی وسکون
الث وفوقانی » بمعنی برا کنده و پربشان باشد
و ماضی ‎GET‏ هم هست یعتی پراکنده کرد
‎olen,‏ ساخت و پژمرده گردالید ؛ و بضم ‎Jal‏
‎gl,‏ هم کفته‌الد - وم اول و کسرثالی؛ عبات
خانه و معبد بهودان را گوبند .
‎cae geht‏ اول والی بروزن‌شنفتنه

(۱) چش : - وبسبی ... گویند .

بمعنی کشردن ۱ - وشکافتن و پراکنده ویربتان
کردن ویژمرده شدن و معدوم گردبدن باشد ۷؛
و بفتح اول وثالی هم‌آمده است .

کشفته * ‎pee‏ اول ‎JE»‏ بر وزن
شنفته , بمعنی پرشان ویر کنده و پژمرده شده
وسوخته ومعدبوم گردیهه باشد ؛ ویفتح اول وثانی
هم‌آمده است .

کثف 8399 ‎b=‏ رای بی‌قطه‌بروزن
نمك‌سود » نام رودخانه‌است که ‎pple‏ لریمان در
حوالی ‎oT‏ اژدهاییرا کشت .

HSB agit ‏بنتح اول و سکون‎ - CEST
‏وبتر کی قروت‌خوانند؛‎ Vash ‏شده‎ cles ‏دوغ‎
‏ازماست‎ LST ‏ویسی کوبند نان خورشی است که‎
‏می‌پزند ؛ و بسنی گویند. طمامی باشد معرو ف که‎
‏ازآرد گندم وآرد جو و شی رگوسفنددرست‎ LST
‏ازآنرا گوشت و گندم لیزداخل‎ AG ‏میکنند و‎

میازند و مالند ‎doe‏ میخورند - و بفتح اول

۱ کش ( نم اول ) بممتی قتل و کشتار است : « سبب ترول اين ‎ay OT aT‏ که .
مصطفی ص کافرالرا شکسته بود و کشش وفارت کرده ...» ( مولوی بلخی رومی . فیه مافیسسحح
فروزانفر ص۲). .۰ ۴ - اوستا - 62838۳8 ( سنگه پشت ) با (خرچنگه ) ؛ ساسکربت
- 6861622 ( سنگگ پشت ) » بلوچی 68610 « استق ‎۸۵٩‏ ۰ , افنانی ‎kshap‏ > هوبشمان
‎CAV‏ 2

چون کثف اببوه غوغائی بدید بانگه وژخ مردمان » خشم آورید.
«درودکی سمرقندی. نفیسی. ج ۳ ص ۱۳۸۶ >
کثف دید طالم خداوند ماه .

فردوسی طوسی « رشیدی * .

‎Say ۴‏ کزف . ۵ ره ‎ges:‏ . ۱ - باین معنی باگاف فارسی

‎. ) ‏است . ۷ رك : کشفته . و بمعنی اخیر بفتح اول وثالی ص شکفتن ( شکافتن‎ peel

‏۸ - اسم مقعول «کشفتن »:
مکی )56-1 شادی کشفته یکی را باغ پیروزی شکفته.
‎pall sb‏ اسمد ک ‎GF‏ ۶ ویس ورامین س ‎۸٩‏ > .
‎٩‏ - یکی از شب هربرود که سرچشمة آن ‎Lite choy‏ اترك در کوههای ‎Mp‏
‏مسجد است و پس‌از مشروب کردن رادکان و چناران از شمال مشهد گذشته ‎Jay‏ خاتون‌بپربرود
میریزد « کیپان . جفرافیای طبیمی س ‎6۹٩‏ - ۰-کردی ‎keshk‏ ( پنیر ارم کردان .
‎kashk (0, 5‏ « ژابا ص ‎٩۳۳۹‏ , گیلکی ‎ekashk‏

‏۴ - چو کرد اختر فرخ ‎col‏ نگاه

######## pdf 449

bya

. ‏تخت کیکاوی پادشاه ابران بود»‎ Sh

کشو با - با بای ابجد بالف کشیده »
بلغت زند و پازندکمان ‎pF‏ اندازی را گویند ؛
ریجای بای ‎uml‏ نون هم پنظر آمده است٩‏ .

‎FORT‏ - با نای ‎the‏ بر وزن
خروس » تام ‎tle‏ است که تضم آن را بسربانی
‎sks‏ و بعربی پزرالکشوت خوانند .

‎OT‏ دوهی = افننتین رومیست,
‎oly‏ لوعی از بوی مادران باشد ۳ .

‏کشود ‎che‏ ال ‎Ay‏ بروزن‌سرمد.
بمعنی فجور است ‎oly‏ انتهای زور ‎‘ates‏
‎yd‏ ارتعاب در آمور فواحش است ۴ ‎pee‏
‏اول و ‎oS gana‏ است وآن رستنیی باشد
دوائی ۵

‎ist‏ ‘ = بکر اولوفتح الك‌بروزن
مهار ۰ ترجمهةٌ ‎iil‏ است که ‎th‏ حصه از هفت
‎bee‏ ربعم مسکون باشد چنانکه گوبند کشوراول
و کشور دوم یعنی اقلیم ‎Sot‏ و ‎clit‏ دوم(۱) وهر
کثوری بکو ‎oS‏ تعلق دارد : کشوراول که اقلیم

‏لا

‎-۱1۵1-

‏اول ‎Joy uth‏ و ‎OT‏ هندوستان است » دوم(۱)
بمشتری و آن چن و خطا است؛ و سیم بمریخ
و آن تر کستان ‎ath‏ چهارم ‎OTs AE‏ عراق
وخراسان است» پنجم بزهره و ‎OT‏ ماوراء التهر
است؛ ده شنم بطار دک ‎rei‏ حفتم بقم ‎OVS‏
‎las!‏ ۳ شمال است ۷
کشورخدا , کشور ‎SIAR‏ -

‏پادشاه را گوبند باعتبارمعنی تر کیبی آن,چه کشور

‎gine |‏ اقلیم و خدا ‎gine‏ صاحب وسالك بآشد.

‏ر کشود خدیی یز کرند ر ‎IGF‏
‏خف‌ایی بمعنی پادشاهی باشد.

‏کشورد بکر اول و سکون ‎gs‏
‏و فتح ‎MU‏ و رای بی‌نقطه و زای نقطه‌دار هردو
‎TL‏ بمعنی بزرک باشد 4 چه کشورزیان
~= بزرکان است

‎Sloop « ‏بکر اول وفتح انی‎ - OF
- ٩ ‏است که آنرا بیونانی اسطوخودوی کوند‎
‏وخطی را نیز گنته‌اند ۱ که بجهت علامت‌بطلان‎
‏و بسنی کوبند بععتی خط‎ NY ‏برنوشته بکشند‎

‏- هیچکدام نیت , بلکه کشونا ‎K(a)shOta‏ است بمعنی ‎OLS‏ « بونکرص۱۱۱*.
- نام عربی ‎wy‏ مشتق ازسربانی ‎kasha ( kashOtha‏ بمعنی توده کردن‌وجمم
‎Coss‏ 9 طفیلی ‎cuscute‏ با ‎épithym‏ ( فر ) ( , ‎Cuscuta Epithymum‏
) « عقار ‎۱۸٩‏ ف » ‎yy‏ شکوتا . ۴ - رگ :کشوث ‎ye‏ رك : عقار ۳
‎NAN‏ . ۴ -ظ . ‎By ds,‏ آذرکیوان . ۵ ره ‎byt:‏ , شکوتا .
۲ - اوستا - 62۲372۲ « بارتولمه £04 » , پهلوی ‎Kishvar‏ ( قطعه , ‎Cae‏
‏پازند 1690۷27 « نب رکه ۱۳۰-۱۲۸ < ‎Geel‏ دوه » < منای ۲۷۸ ۴
چون خواستی آواز؛ فتح وظفرخوش
در جود و‌خاوت بنمودی‌هنرخوش.
«معزی نیشابوری ص ۸۱۸ *.
8 - بشدید دوم . از لائینی

‏۲ - درکشور توران ‎os Ay‏ وعرأقین
هرسه بگرفتی وسیردی‌سه‌خسرو

‏۸ رگ : رشیدی . ظ. مخفف «کشاورز» ‎Cem)‏
‎oS. cassia‏ در توس به ‎Lavendula Stoechas‏ اطلاق شود « دزی ج ۲ ص 414 *.
*۶- از ‎gS:‏ (کشیدن) ‎a‏ (پوند) ‏
‎٩‏ تو یه نامگی؟ قاسمی ‎OS‏ عفو کشی حاکمی .

‏فاسم ابوار « ریدی > =

######## pdf 450

-۱4۷- کیش
ونوشته است ‎٩‏ مطلقاً خواه خط عربی‌باشدوخواه
قارسی وهندوی وغیره؛ وبعضی بمعنی‌خط ونوشته
‎ain‏ اول کفته اند و خط بطلان را بکر اول ؛
و بفتح اول و انی بمعنی خطی باشد که بکشند
خواه بر دیوار و خواه بر زمین (۱) وخواه بقلم "
وچوب و انگشت و غیره - وتنگه چاروا را نیز
کوبند و آن نواری باشد که بر زین و ‎NG‏
‏دوزند ۴ - و بععنی کدا و گدايی‌کننده ۴ -
و بمعئی آسانی در برابر دشواری نیز کفته‌اند -
و بر چار پایان هم حمل کردماند - و با تشدید
انی حیوان پالان افکنده را گوبند ۴ .

کشی * = بنتح اول و ثانی بتحنالی
کنیده . بمعنی خوشی و تندرستی باشد ؛ وباین

معنی ‎GEL‏ فارسی هم‌آمده است ۰

کشیخان ۱ ۰ بروزن پیخان ‎ian‏
‎Oy‏ و بچشم خود بن باشد ب کشیخانی
بمعنی دبوئی است ‎He‏

کشیده ۲ ۰ بر وزن رسیده | بمعنی
وزن کرده - و بلند ودراز باشد چه « کشیدمروه
مردم رو دراز و « کشیده ریش * مردم دراز رش
راگویشد - و در خراسان بمعنی نشثی باشد که
ژنان بر روی پارچه میدوزند ۸ - و مشتی
خواهتد ‎Ty‏ بزند ‎٩‏ .

کشیش ۰۱ بروزن حشیش ‎beta‏

و ‎ol,‏ نمابان و زاهدان و عالمان صاری ‎eth‏
‏وممرب ‎OT‏ قمیس است بکسر قاف .

() چش : - وخواه بر زمین .

۱ - « که , خط که اندر کشند , کثه گویند . » « لفت فری ص14۱ *.

۰ در دستوراللغه ( معنی : بطان ) و نیز مهذب‌الاسماء ‎Lat)‏ : بطان ) همین لفت
‎JK‏ رفته « فرهنگ نظام + طبری 851 ( تنگ اسب ) « واژه نامه ۵۷۹ *.

‎Gh, «- ۴‏ راکثه خوالند یعنی که مال مردم را بخودکشد . » «لفت ‎Ht‏

‏قی: ‎kesh raftan‏ ( دزدیدن » ربودن ) در تهرانی . ۴ - ‎Gat,‏ هم بمعنی «حیوان
پالان افکنده»آورده ‎Ll‏ شاهد نیاورده است . 8 از :کش ۲+-ی ( حاصل مسدر).بتشدید
شین هم‌آمده . 1 - رك : کشخان . ۲ - اسم مقعول از « کفیدن *.

‎a‏ - قسمی از فلاب دوزی که روی پارچه با ابربشم ‎OTL‏ میکردند و گلابتونآ ترا
هم کشیده میگفاند « فرهنگ نظام » - یز بمعنی زر وسیمی که از حدیده گذر دهند *
شخصم ز فرقت تو چو زر کشیده شد ‎ye‏ ز حرت تو چو سیم کشید هگیر.
‎ey les ow‏ فرهنگه نظام *.
‎٩‏ - سیلی‌را کشیده گوبند. *- قس:عربی‌قسیس» ‎+e) qeshshisha» yt‏
کاهن) «ممجمیات عربیه - سامیه ص۱۷۹ *ژابا ۰۳۳۹ , آرامی 085[115[38 (شیخ,کاهن) ‎Kp?‏
‏© کثیدن - بکر اول و فتح چهارم ( در ‎ted‏ مر کزی ) و بفتح اول ؛ از :کش +
بدن ( پسوند عصدری ) . جزو اول در اوستا - ‎Karsh‏ < بارتولمه 4۵5 » « تب رک ص ‎NTA‏
‎sae‏ باستان - ‎)karsh‏ کشیدن), پپلوی 6251020 . کردی 18180 ( کشیدن) ‎GUN.‏
‏81 . بلوچی ‎kashag‏ . ۷۵51028 ( کشیدن , برداشتن ) , ارمنی ( ‎karshem (t¢‏
( کشیدن ) « اسشق ۸۵۹ * در اوراق مانوی ( پپلوی ) 8658 ( ‎oat‏ . کوشیدن )
‎Henning , A list of Middle Persian..., BSOS,IX,1.p.84 )‏ ) امتداد دادن «
‎ata‏ کردن » دراز کردن » مثبسط کردن - بسوی خود آوردن » با خود بردن - باربردن » حمل
کردن » نزديك آوردن - تحمل کردن » صبر کردن » رنج ‎Ory‏ - جذ بکردن - رسم کردن +
قاشی کردن - سنجیدن ۰ وزن کردن +
```


## [2026-09-06T15:55:48.825Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndef leafof(path, lineno):\n    t=open(path,encoding='utf-8',errors='replace').read()\n    lines=t.split('\\n')\n    idx=sum(len(l)+1 for l in lines[:lineno-1])\n    return t[:idx].count('\\f'), lines\nfor p,ln in [('BQT_v1_pages.txt',22717),('BQT_v1_pages.txt',23329),('BQT_v2_pages.txt',31757)]:\n    lf,lines=leafof(p,ln)\n    print('###',p,'line',ln,'leaf',lf)\n    print('\\n'.join(lines[ln-12:ln+12]))\nEOF"
}
```


### [2026-09-06T15:55:50.759Z] TOOL RESULT

```
### BQT_v1_pages.txt line 22717 leaf 561
و سکون انی مجهول و وا کرمکی باشد که
امه یشمین و کاغة را بخورد و ضایع کند۸ .
پیواد - با نانی مجهولبر وزن دیوار,
عدد ده هزار را هنشت و باین حمثی. محذف الف
پیواده » با تالی مجهول بر وزن
بیجاره ؛ بیکس و غریب وتنها -- وبی‌قدروهرتبه
وبی اعتبار را گویند - و چویکه بدان كلولة
خمیر انرا تنك سازند .
یو اد با نانی مجهول بروزن شیراز »
شیره باشد که آنرا مرغ عیسی گونشد و بعر بی
خفاش خوانند - و بمعنی اجابت و فبولهم آعده
است. و پاسخ وجوابرانیز کویند*۱» وباین معنی
بجای حرف الی لون هم‌بنظرآمده است»وبمعنی
اول بجای حرف اول بای فارسی هم آعده است
پیو بادیدن » بکس ارل و اك
مجهول بر وزن فرو باریدن, ناجاویده فرو ,بردترا
کون که بمربی بلم خوانند ؛ و بفتح انی حم
آمده است که بر وزن شکم خاربدن باشد واین
اصح است . چه در اصل این لفت باوبارسن
بوده است همزه را ببایدل کرده اند بیوباربدن
؟ از:یا. ۳ بی(حاصل
۴ ۳ آسم فاعل ازددن
۷ باین معنی « بيوك » هم آمدهءو در
۸ اظ م مصحف: _ (هم).
### BQT_v1_pages.txt line 23329 leaf 576
آنم که هم یگویم‌یازند فرادست. فرخی‌سیستالی.
آدت که : «بامردم بداصل مپیوند» لبيبي .
* مزدینا ۱۸۵-۱4۲بر ون دلدگار » بیعتی سار است که فگد
باشد؟ _ ولگد کوب راه مگفتماند - و بضم ثالت
درآب و درخشکی میکنند .
پاسبان ۴ - با بای ابجدبروزنآسمان,
شب زنده دار و محافظت کنندء ۴ باشد؟ .
پاسبان طار م نهم- کابه‌از کر کب
زحل باشد .
پاسبان قلاث - بنمنی پامبان طارم
نهم ات که کوک رحل باشد .
پاسخ؟ -
دار ؛ ۳ در مقابل سوال است .9
پاسره - بنتح ثاك بر وزن تاسره »
زه‌عنی راکه ء بند که‌صاحب زراعت دروجه‌اخراجات
صرف اخراجات دبواای و غيره کنئد .
پاساث - منم ثاكت بروزن نازك. خمیازه
و دهان دره باشد . و بفتح الث یز آمده
ات ۷۸ .
: پاستگه - بر وزن آهنگه, آنچه ند
۱ - رك . یاسار.
بان ( پوند اصاف ) «اسشق ۲۷4».
زر ۱
دیگ ۷
### BQT_v2_pages.txt line 31757 leaf 534
                                                          ‫و برای یی قطةٌ زده و کر کاف و سکون شن‬
                                                           ‫و تای قرشت ‪ ۰‬بلغت سربالی تخمی است‌دوابی‬
‫خوانند ‪ ۰ ۴‬و بعضی کویند ساسان چون از بم‬                         ‫که آنرا بعربی بزرالانجره وقریض‌خوانند ‪۰‬‬
‫و خوف خواهر خود با جممی از درویشان سردر‬                   ‫ساسا لیوس ‪ -‬بکسر لاموتحتانی بواو‬
‫نام‌داشت»‬     ‫بود اوئیز ساسان‬     ‫حهان نهاد اورا ری‬
                                                           ‫رسیده وبسین بی‌نقطةٌ زده » بلغت‌سریانی‌انجدابرا‬
‫بابك والی فاری دختر خود را بوی‌داد ‪.‬بسدازآن‬                ‫کوبند ‪ ,‬وآن رستنیی بکاشهد‌صمغ! براحلتیت‬
‫فنردزان‌ساسان بن‌ساسان که نبیره های‌بايك‌بودند‬
                                                          ‫خوانند » ویس کوبند انجدان رومی‌است وآ را‬
‫ملك رافرو گرفتند وایشان راساسانبان‌خوانند؟ ‪.‬‬
                                                           ‫کاشم رومی نیز گوبند و آنهم نوعی از این است‬
‫بارساء‬      ‫بروزن‬   ‫یا تای فرشت‬   ‫‪= ۴‬‬   ‫ساستا‬              ‫لسکن اکنید‌درازتر ازآن عیباشد»وا تراسالیون‬
                     ‫نام دبوی است از تابعانآ هرمن ‪.‬‬
                                                                                    ‫وسیالیوی همگویند‪.‬‬
‫ساسر * دینتم اك‌بروزن لاغر ‪ ۰‬بمعنی‬
                                                           ‫= بروزن آسان ‪٠‬‏ صاحب ترك‬        ‫ساسان‬
‫» قلم ولی‬       ‫سارج است که سار باشف ‪ -‬رضم تال‬
                                                           ‫باشد ‪ -‬و کدا وکدابی کنندمرا‬       ‫بد‬
                                                                                              ‫فدر و‬
                                                                                                  ‫تجری‬
                                                                                                     ‫وت‬
                    ‫میان خالی که بدان چیزی نوبسند‪.‬‬          ‫یز گوبند ‪ -‬و نام پسر بهمن‌بن‌اسفندبارهم هست‬
‫تانشواه را‬      ‫‪۰‬‬    ‫قاسم‬   ‫ساسم = بر وزن‬
                                                           ‫کخهتهم خواهر وهم مادراو وحم‬    ‫که از همای د‬
```


## [2026-09-06T15:56:03.520Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndef leaves(path):\n    return open(path,encoding='utf-8',errors='replace').read().split('\\f')\nv1=leaves('BQT_v1_pages.txt')\nprint('##### v1 leaf 576 (≈p.354)')\nprint(v1[576])\nEOF"
}
```


### [2026-09-06T15:56:05.350Z] TOOL RESULT

```
##### v1 leaf 576 (≈p.354)
بر ون دلدگار » بیعتی سار است که فگد
باشد؟ _ ولگد کوب راه مگفتماند - و بضم ثالت
درآب و درخشکی میکنند .
پاسبان ۴ - با بای ابجدبروزنآسمان,
شب زنده دار و محافظت کنندء ۴ باشد؟ .
پاسبان طار م نهم- کابه‌از کر کب
زحل باشد .
پاسبان قلاث - بنمنی پامبان طارم
نهم ات که کوک رحل باشد .
پاسخ؟ -
دار ؛ ۳ در مقابل سوال است .9
پاسره - بنتح ثاك بر وزن تاسره »
زه‌عنی راکه ء بند که‌صاحب زراعت دروجه‌اخراجات
صرف اخراجات دبواای و غيره کنئد .
پاساث - منم ثاكت بروزن نازك. خمیازه
و دهان دره باشد . و بفتح الث یز آمده
ات ۷۸ .
: پاستگه - بر وزن آهنگه, آنچه ند
۱ - رك . یاسار.
بان ( پوند اصاف ) «اسشق ۲۷4».
زر ۱
دیگ ۷
پاسواد -_بممنی سوار پاست که پبادة
و چايك باشد .
پاسه - بی وزن 8 بمعشی تاسه
و تلواسه است که عیل کردن هر چیز -. و غم
واندوه ‏ و فشردن کلو باشد » دباین حعنی بجای
#9 9
پاش بر وزن ماش » بمعشی پربشان
است منی پربشان کن و از هم جدا ساز و بر
افعان .
با شات ۷" فتح الث‌بروزن ناولگ. نمعئی
خمازه باشد۷۷.
باشنا با فون بروژن آشناء یاشنة بارا
کوبند ۷۴- وخیار ثر خربزه و هندوانه و کدو
وامثال آ نرائیز کفته‌اند که‌بجهت نخم نگاهدار بر۴٩۰‏
+ کلتان ۵۱ *.
بارستگه .
ارمنی ۳80285201 < اسخق ۷۵ > جمماً
* را : باشك ۸ ی
. لت نامه». ٩‏ مرک از
نتارکان » « الفهيم بنقل لفت نامه» .
6۰ خاکرا نذمکی ده ی که باش
0 رله : باسكث . ۴ رل : باشنه.
۵ پاسدار - نگاهبان, مراقب :
بزد تیغ بر کردن پاسدار
۴ ره : پاششگه ویاشنگه.
```


## [2026-09-06T15:56:16.566Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor lf in (563,564,565):\n    s=t[lf]\n    if 'سخن' in s:\n        print('### leaf',lf,'≈p',lf+543)\n        print(s[:2600])\nEOF"
}
```


### [2026-09-06T15:56:18.249Z] TOOL RESULT

```
### leaf 563 ≈p 1106
                                                                                                      ‫=‬

‫آن قره بطالا باشد‬       ‫ون‬
                         ‫رهن‬
                           ‫یاآ‬
                             ‫یس ب‬
                                ‫آون م‬                 ‫مردم درشت وقوی هیکل و درلیارگوبند ‪- ۷‬‬
                     ‫ومعر ب آن ستوق باشد ‪.‬‬            ‫و صورتی را نیز کنته اند که از غات کراحت‬

‫ستو | * = بفتح اول سوکون‌ انی و واو‬                   ‫وراسان باشد‬
                                                                ‫و زشتی طبع از دیدش رمان ح‬
‫بالف کشیده » نباتمی است که سانزگه‌تراشیده‬             ‫‪ -‬وبمعنی کابوی نآیزمده است »وآن‌سنگینیی‬
‫اند بشکل پیرزلی درموضم بامیان قرب‌به‌خنگه‬                ‫‪-‬ص‬
                                                          ‫شندخ‬
                                                             ‫ور ک‬
                                                                ‫زی‬              ‫وراب‬
                                                                                   ‫رخاد‬               ‫دهم‬
                                                                                                        ‫رک‬‫مشد‬
                                                                                                            ‫با‬
                                                     ‫سخن اشنو وستیپنده وستیزه کنندمرالیز گویند‪.‬‬
‫بت وسرخ بت ِ سرم بروزن همدم‌می‌گویند‬
‫ستوار ‏‪ = ٩‬جم اول بر وزن کلزار ‪,‬‬                      ‫شکنج »‬       ‫سنج ه بکس اول بورزن‬
‫محف استواز استکه بمعنی مضبوط و محکم‬                  ‫چوییرا کوبند که در زیر آن غلطکها سب کنند‬
‫باشد ‪ -‬و بمعتی امین و ممتمد هم هت ‪-‬وباور‬             ‫آونرا برکردن کاوبندند و بربالای غلهایکه‬
                                                      ‫ازکاه جبدااششددبهگردانند تاغله از کام‌جدا‬
‫د جم‬     ‫یت‬        ‫مد‬           ‫کردن و صدیق‬
                     ‫اول وثالی هم آمده ات‬            ‫کردد ‪ - ۴‬وبمعنی ذخیره و پس‌انداز همآمده‬
                                                     ‫است ‪ -‬وجمم کردن مال و برهسمانیدن اسباب‬
‫ولزن بپتان»بممنی‬
               ‫ستوان ‪ - ۲‬ببصمراو‬                     ‫سوامان را بیزکفته اند؛ وبفتح اول و ثالی هم‬
‫‪ -‬ومد رامین‬        ‫ستوار است که ‪ 9‬ر‬                                                               ‫‪۳‬‬            ‫درست‬

                    ‫داشتن باشد ‪. ۵‬‬    ‫باوور‬
                                          ‫‪-‬‬
                                                      ‫شطه‬    ‫خای‬   ‫و‬   ‫پنتم اول‬      ‫=‬     ‫ستش‌شیز‬


 ‫ستودان ‏‪ = ٩‬بضم‌اول بروزن‌جپو
```


## [2026-09-06T15:56:28.370Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor lf in range(565,578):\n    s=t[lf]\n    hit = 'سخن' in s\n    print(lf, 'hasSOKHAN' if hit else '', s.replace('‌','')[:120].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-06T15:56:30.101Z] TOOL RESULT

```
565                                                                                                   ‫‪î‬‬     ‫‪۱ ۵۳‬‬ |  |  |  |  | 
566 hasSOKHAN    ‫‪۷‬‬   ‫‪4‬‬                                                                                                  ‫سنیز‬
567 hasSOKHAN   ‫سجلاط‬                                                                                       ‫==‬ |  |  ‫ونافرمالی نمودن‪
568 hasSOKHAN   ‫—‬       ‫‪۵‬‬                                                                           ‫نجن‬ |  |  | ‫سچیدن ‪ = ۲‬بروزن د
569 hasSOKHAN                                                                                                             ‫‪¬ ۱‬‬     
570 hasSOKHAN     ‫==‬                                                                            ‫وش‬ |                                
571   ‫سدوم‬                                                                                          ‫یت‬‫‪-‬‬ |  | ‫گوبند صمخ د
572    ‫تس رز —‬ |  | ‫برامن آن است کهیومرث را صد فرزدد از‬                 ‫قاضی شهر لوط است و او فتوی بلواط (‪ )۱‬داده‬ |  ‫نور ب
573                                                                                                    ‫=‬            ‫‪-‬‬ |  | 
574    ‫‪“NNN‬‬                                                                                                 ‫سراب‬ |  |  |    ‫
575                                                                                                                          
576    ‫»<<‬                                                                                            ‫سرافوج‬ |  ‫سارفكرر = 
577 hasSOKHAN
```


## [2026-09-06T15:56:34.698Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor lf in (569,570):\n    print('##### leaf',lf)\n    print(t[lf].replace('‫','').replace('‬',''))\nEOF"
}
```


### [2026-09-06T15:56:36.783Z] TOOL RESULT

```
##### leaf 569
                                                                                                            ‪¬ ۱      وه




 سج = بکر اول و فتح ثانی‌وسکون                                         ستختا له = بروزن متاه سکن مخت
جیم ‪ .علتی باشدکه آارا تنگی شضس کوبند؛ وبا                                                         و درشت رگاوند ‪.
                      جیم فارسی همآ مده است‪.                           سخت بازو ‏ با بای ابجد بالف
 سره ‪ - ۲سم اول بروزن‌مهره»بممنی                                                   کشیده و زای هوز بواو رسیده ک
                                                                       ‪۰نابه از مردم
بیگار است که کار بیمزدکردن باشد‪ -وبمعنی                                     قوی هیکل و توانا وصاحب حمایت باشد‪.
 در عربی   و    ‪۰   است    هم آمده              زیون و زیر دست
                                                                              سخت لگام ‪ -بکر لامکا
                                                                       وف‌فارسی
                     باشد‪.           هیزا
                                        تکسسضر
                                             اموعنی
                                                  بم                  بالف کشیده و بمیم زده » اسب سر کن وا کویند

 ‪ -بفتح اول بروزن رخش‪ ,کهنه                          سخحش              ‪ -وکنابه از مردم گرددکش باشد بعنی کانیکه
پرستین و کهنه جامه وکپنه کلاء و امثال ابنها                                                  سر باطاعت فرو نباورند‪3.

را کویند ؛ و باين معنی باشین نقطه دار هم                               پر کو »    ‪ - ۱ضم اول بر وزن        سختو
                               آهده است ‪.
                                                                      رود کوسفند را کویند کهآدرا با گوشت وبراج
سخالات ‪ - ۴بفتح اول و سکون آخر                                         و مصالح بر کرده بر روغن بربان کرده باشند ‪-
اسمن راکه فوفانی باشد بروزن اخلاط ‪ ۰بکل                                  کونایه ازآلت تناسل هم هت که قضب‌باشد‪.
               کوبند که باسمن سفید و کبود باشد‪.                        سخته ‪ - ۲بفتح اول بروزن اخته‪,بمعنی
 انی » ممروف         و    = بنم اول              ‪°   سین               سنجیده و بوزن درآمده و وکزرنده‌باشد؛ رصم
 اول و فتح‌ثالی            ؛
                           م وند
                               عروبی کلام کوب
                                            ابست                                                   اول کهفمته‌اند ‪۶#.
و بفتحاول و ضم ابلفیتوح اول ثوالی هم                                  سخحتی د بو ار ذهر ‪ -کنایه از
                                                     | آمفه آنت‪:.:
                                                                       آفتاب عالمتاب است کونابه ازحوادث روز کار
جور » بکر‪ .نون و فتح جیم                                سخ                                                     ‪.    هم هت



                                      ‪.        = سفدو ( ه‪ .م‪ » ) .معرب آن « سختور > « الطبیخ ‪۳۵            ‪۱

                                                                       اسم مفعول از« سختن» («‪.م‪: ).        ‪۳
        سند باد ‪.         لکت   از        »    توبی درسمر   نکته
                                                                         وره توبی در کهر ‪ ,سخته تونی درهتر
   « منوچهری دامفانی ‪٩۱٩‏ ‪.
   ‪ -. ۴از (عی) «سخر‪ . :بالْم میم وفرمان بردار » مقپور > منقاد ءوآنکه بروی ببار
                    مردم فوس کنند ‪ .وآنکه اورا هر کی مفهور وفرمان بردار سازد» «منتهی الارب» ‪.
   © = سخون («‪.م‪ » ).بهلوی ‪« 8۵۷505اویوالا                                   ‪۰   «سجللاط»(«‪.م‪).   مصحف     ‪۳




                          ‪ ۹فس ‪ 2پاسخ (بهلوی ‪ « )۷×38540ربکیه ‪ ۰۰۲ورك ‪ :اس ‪:4۲۷
  وطرح) «بارتو لمه          ) اعلان » لقشه              » عبارت) از اوسا ‪۷29 12-      ‏‪ Saxvanاکمه ۾ لفط           ‏‪ DÎو




   دکلتان ‪. ۹۱                                  عیب وهثرش نهفته باشد ‪.             تامرد سخن نگفته باشد

   ‪ ,ورن       >‪ .صنجدن         ‪۰۲۱           د بوتکر    ‪natxas‏     و سوم » پپلوی    بفتح اول    سختی ‪-   ‪#

   نه چندانکه] ترا توانند مخت ‪.                              سربر وسرا پرده و تاج وتخت            شی؛دن ‪:
                                                                                                        کدن
                                                                                                          کر
   نظامی کنجوی‪ «.کنجینه ‪4A‏ ‪.

   از ‪ :سخت ‪-۳ی ( مصدری ) ؛ صلابت » درشتی ‪ -دشواری ‪-    ‪.تح
                                                          ‪-بف
                                                            ولاتی
                                                                * سخ
  ‪« :یکی از پادشاهان پیشین دررعابت مملکت ستی کردی ولشکز    یتضد
                                                              ست »
                                                                 زحمت ‪ ۰محن
                                                                                     بختی دائتی‪ ».ک«لتان ‪. ۷۳۰

##### leaf 570
    ==                                                                            وش
                                                                                   فنردل
                                                                                       سخ
           فهمیده و سخن فهم را نیزگوبند ‪.      و سکون واو و رای قرشت » کنابه از سخن بی
سخن سنگ د بک ثالث » کنابه از                                         باشد ‪.    لطات و دل شکن

         رشان آمد ‪.
                  کگو
                    مخنی است که بر             سحن دل‌قر وش د کنابه از سخن
ح اول و خم ثالی و واو  فنت= بجوس                  وز
                                                   رخن
                                                     وسدشدل‪-ف
                                                            یح و موعظه با
                                                                        صباو
                                                                           خو
ونون هردو ساکن ؛ بمعنی سخن است که کلام         عم بنظر آمده است که بجای شین قطه‌دار زای
                                  باشد ‏‪. ١                                شطمرار باشد ‪.

سیر " ه بر وزن قفیر » دوایی است                سحن زههر بر = کنابه ازسخن بی
                                                                    وفرده باشد‪.      هزه و نك
قلخ » طبیعتش گرم و خشك است و حفوی معدم
               هم هست وسدهء جگر بگشاید‪.         سنن زن ‪ -بفتح زایقطه‌دار وسکون
ستخینوس = بنتح اول و انیبتحتالی                نکوننا»به از شاعر و قصه خوان و سخن کذار
رسیده و نون بواو کشیده و بین بی‌قطةٌ زده »     باشد ‪ -و کنایه از مردم افتراکننده و سشن فهم
 بلغت یونالی ‪ ۴کیاهی‌است که براخلال‌مامونی
 کوبند و بعربی اذخرخوانند ‪ -وبمعتی مسطکی        سهتی سنج ‪ -بمعنی سخن زن است
                        هم بنظر آمده است‪. .       مدر‪-دوم
                                                        کنهابه از شاعر و فصه خوان باش




                                                ‪ #ست] = بفتح اول و ثانی‌بالف کشیده»
                       و قدرت و توانایی حم      وثب وحمام و امثال
                                                                کوه ک        آوازیرا کونند که در
                                                              آن پیچد و معرب‌آن صداست ‪. ۴
                       بعربی فدجن ‪٩‏ بروزن      »یاهی
                                                    سداب = بس اول بروزنکلاب گ
                             الکن خوانند ‪.      باشد دوابی مانند پودنه ® ‪.خوردن‌آن دفع‌قوت
                                                زان     حمل   مردان و اسقاط       باه و مباشرت


          رطل پرکن مگوی بیش سخون ‪.                     ‪- ۱بودلی بود می بیار اکنون
  رود کی سمرقندی ‪.رود کی ‪ .اقیسیص ‪۷۶۱۱٩‏ ‪.

                 ‪ - ۴لکلرك کید ‪ :مااین ماده را نمی شناسیم ‪« .لك اص ‪۸۳۲٩‏ ‪.
 ‪-سدا باسین مپمله باين معنی در
                             ‪« ۴              ‪-نای ‪« 50810535اشترنکای» ‪.
                                                                       ‪ ۴و
    ‪۲ص
     ‪( 6۱۲فر ) د لك    =   زان
                             =     ‪۵            هیچ کتب موجوده بات ددد ‪« ».چكثسص ‪۵
   ‪ .سددسابتها‌ای ازتیر سداییان ‪8860٥4۲01۸‏ هستند و مهمترین نوع آن سداب                    ‪۹۳
   بگهای باريك وبسیار تعفن که برای کر بزاسن حشرات بکاررود‪.
                                                         کرحی ‪atuR‏ است دارای ر
                ‪« - ۱فیجن کحیدر ‪ ,کیاه سداب ‪٩‏ « منتهی‌الارب؟ ‪.          ‪.     « کل کلاب ‪4۱۲

                                                      ‪ #سد ‪ -بختح اول › رك ‪ :صد ‪.
```


## [2026-09-06T15:57:04.945Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HRN leaf 181 (=p.160)\"; awk 'BEGIN{RS=\"\\f\"} NR==182' HRN.txt | head -60"
}
```


## [2026-09-06T15:57:05.178Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN leaf 1362\"; awk 'BEGIN{RS=\"\\f\"} NR==1363' SYN.txt | head -50"
}
```


### [2026-09-06T15:57:06.821Z] TOOL RESULT

```
### HRN leaf 181 (=p.160)
- 160 —
kurd. stün, istün\ af/. stan.
Die indogermanische Grundform ist nach Hübsch-
mann, ZDMG. 39, 93, "^'sthlnä-; dagegen siehe zuletzt
J. Schmidt, KZ. 32, 385 folg.
722. fiite^ *Kampf, Krieg*, süeziden,
aw. vergl. stij- *Kampf, Streit'; phlv. stej 'Kampf*
(Bund.).
Wohl zu ai. l/^t^J-, tejate 'scharf sein, scharf werden',
vergl. Desid. titiksati *sich scharf zu machen suchen,
sich zu stählen suchen gegen Etwas, d. h. Wider-
stand entgegensetzen ; gr. ötCQm, lat. in\stigärey
germ. i^stek-^) (as. stekaUy ahd. stehhan, got. staks
'Mal, Wunde').
723. sey(t 'hart, fest; sehr, se/ß.
ai. [/^^ak-, gaknoti 'vermögen, können*, skr. qaktä-
'vermögend*; phlv. sayt^ saxtak]tum (vd. 19 (47)).
bei. sak 'hart, stark, fest' (383); yidg. sukt.
V
72 t. sw/un, SU/m (Sahn. I, 29 V. 117 neben -ww, ebendas.
V. 109) 'Wort, Rede*.
Käs. K. siixan[6ni,
aw. sax'Ore (Y. 29, 4), säx^em (y. 53, 5) ('Plan, Rat,
Rede' (Bartholomae, Ar. Forsch. III, 36, 37); phlv.
sa/wi 'Wort, Rede'.
725. sed (heute geschrieben sed; AM. sed, S. 7 Zeile 15,
aber sed, S. 8 Zeile 4) 'hundert'.
aw. safa- 'hundert*; phlv. sat; ai. gatd-,
kurd. sed; af/. sal, sil; oss. sädä (218); wa;^. sar.
LW. sad.
720. ser 'Kopf; vergl. serapa 'Ehrengewand' ^).
aw. Sarah' 'Kopf; phlv. sar^ asar 'endlos' (aw.
anayra-); ai. ciras- 'Kopf; arm. sar 'Höhe, Gipfel,
Abhang' (H. No. 247).
'J Übertritt in die e-lleihe Ca. bei Feist, No. 531).
^) oiiottnts (llesycb), de Lagarde, Ooa. Abb. 208 (?); vergl.
Miklosiob,' Dcnksobr. WAW. Band 3S, 20.
```


### [2026-09-06T15:57:08.376Z] TOOL RESULT

```
=== SYN leaf 1362
ht, strive, con- tend’, OHG sahhan ‘quarrel, contend’ : Goth. sakan ‘strive, rebuke’, etc.
ME withsaye, cpd. of with- (cf. above) and saye ‘say’ (18.22).
ME denye, NE deny, fr. OF r. deneier, Fr. dénier ‘refuse, disown’, fr. Lat. dénegare ‘reject, refuse’, cpd. of negare (above, 2). NED s.v.
5. Lith. ginéyti, iSsiginti (also uz-) : ginti (ginu, gyniau) ‘defend, protect, for-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1270
bid’, also refl. ‘deny’, and gintt (genu, giniau) ‘drive’, ChSl. Zena, ginati ‘drive’, etc. (10.65). NSBs.vv. Walde- P. 1.680 f.
Lett. liegt (also ‘forbid, refuse’), refi. liegties, etym. dub.; perh. as ‘restrain’ : Ukr. za-lyhaty ‘tie up, bind, pledge’, Lat. ligare ‘tie’, etc. (Walde-P. 2.400). Miihl.- Endz. 2.494.
6. ChSl. ottivrésti se (1sg. ottivriiga se; the usual rendering of dpyéouar in the Gospels), refl. of ottivrésti ‘throw away, reject’, cpd. of vrésti ‘throw’ (10.25).
ChSl. ottimetati se, and ottimétati se, refl. of ottimetati, ottimétati ‘throw away’ iter. to mesti ‘throw’ (10.25). Berneker 2.40, 53.
SCr. odricati, poricati, Russ. otricat’, epd. of od-, po-, ot- with sense ‘away, back’ and iter. forms to SCr. reéi,
SELECTED INDO-EUROPEAN SYNONYMS
ChSI. rest, ete. ‘say’ (18.22). of. prérékati ‘contradict? (Supr.).
Boh. popftti, Pol. zaprzeé sie, Zapieraé st¢, Russ., otperet’, epds. (in part Tefl.) of Boh. pitti ‘contest, dispute’, Pol, przeé Russ. peret’ ‘press, push, jostle’, ChSL piréti ‘beat, wash (by beating)’, A ‘contend, ‘strive’ : Skt. prt- ‘fight, quar- rel’, Arm. hari ‘strike’, ete. Walde-P. 2.42. Briickner 442,
Pol. przeczyé, fr. the ady. przeko
ChSI,
- ‘across, diagonally through’, Briickner
443.
7. Skt. ni-hnu-, apa-hnu-, epds. of ni- ‘down, back’, or apa- ‘away, back’, and hnu- ‘hide from, drive or take away’ (etym. dub., Uhlenbeck 362).
Skt. apa-lap-, epd. apa- (ef. above) and lap- ‘prate, chatter, talk’,
18.35 ASK?, REQUEST Grk. — alréw (Epwréw) Goth. bidjan Lith.  pragyti, reikalauti NG §q7G, wapaxadd ON bidja Lett. prasit Lat.  poscere, pelere, rogare Dan. _bede, forlange, fordre ChSl.  prositi, moliti It. domandare, (ri)chie- Sw. bedja, begdra, fordra SCr.  -moliti, iskati, traziti dere OE biddan, dscian, giwian Boh. _ prositt, Zddali Fr. demander ME bidde, aske, demaund Pol. prosic, zadaé Sp. pedir, rogar NE ask, request Russ. prosit’, trebovat' Rum. cere Du. verzoeken, verlangen Skt. yac-, (pra-)arthaya- Tr. condaigim, cuingim OHG _ bitten, eiscon Av., OPers. jad- Nir. tarraim MHG bitten, eischen, vor- W. gofyn Br. goulenn NHG bitten, verlangen, for-
dern
Several of the words for ‘ask, request’, briefly ‘ask’, are the same as, or related to, those for ‘ask, inquire’, briefly ‘ask’!, See 18.31. Others are cognate with words for ‘seek, desire’, ete. Besides the words listed, those for ‘wish, will’ are often used with the implication of a mild, or even firm, request.
Cf. also words for ‘pray’ (22.17), of which several are the same as those listed here, and some of the others are also used in a nonreligious sense as NE pray.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
1. IE *prek-in wo
```


## [2026-09-06T15:57:20.920Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\n# find leaf whose text contains a standalone 1338\nfor i,p in enumerate(t):\n    if re.search(r'^\\s*1338\\s*$', p, re.M):\n        print('leaf',i)\n        print(p[:2500]); break\nEOF"
}
```


## [2026-09-06T15:57:22.660Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json;d=json.load(open('../refs_online.json'))\nprint(d['MON'].get('page_offset'));print(d['MON'].get('lookup_hint'));print(d['FSF'].get('page_offset'))\n\" 2>/dev/null || python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['MON'].get('page_offset'));print(d['MON'].get('lookup_hint'));print(d['FSF'].get('page_offset'))\n\""
}
```


### [2026-09-06T15:57:22.857Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-06T15:57:24.734Z] TOOL RESULT

```
None
Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking
```


## [2026-09-06T15:57:31.690Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON کشف tortoise\"; grep -n 'کشف' MON_part2.txt MON_part1.txt | grep -i 'لاک\\|سنگ پشت\\|kasyapa' | head -5; echo \"== MON ساستار\"; grep -n 'ساستار\\|ساستا ' MON_part1.txt MON_part2.txt | head -5; echo \"== FSF\"; grep -n 'ساستار\\|ساستا' FSF_pages.txt | head -5; echo \"== FSF leaf tags\"; grep -n 'پاسخ' FSF_pages.txt | head -5"
}
```


### [2026-09-06T15:57:31.824Z] TOOL RESULT

```
== MON کشف tortoise
== MON ساستار
== FSF
3804: ‫می‌آورد «شافیدن‪ :‬سورچمک و لغزیدن‬                 ‫گزفته بساستان‬
11166:  ‫به بر گستوان بر زد و بر درید‬                                          ‫پزوهندة نامه بساستان‬
== FSF leaf tags
226:‫آفترین از سپهر‬        ‫ز من»‬   ‫درودت‬          ‫‪ ۱‬چنین داد پاسخ که«ای ماه چهر‬
394:                                                     ‫چنین داد پاسخ به افراسیاب‬
459: ‫‪۱۰۲۰۲۴۳‬‬                                                        ‫به پاسخ ندید ایج جای درنگ‬
847:                                                          ‫نين داد پاسخ که‌ای نیکخوی‬
926:   ‫از فخر گرگانی (ویس و رامین ‪:)۹۲۳-۱‬‬            ‫چوکڑ آورد رای‪ .‬پاسخ مکن‬
```


## [2026-09-06T15:57:38.931Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'ساس' FSF_pages.txt | head -20; echo \"=== leaves\"; python3 -c \"\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f'); print(len(t))\""
}
```


### [2026-09-06T15:57:40.984Z] TOOL RESULT

```
27:                                       ‫فهرستنویسی براساس اطلاعات فیپا‪.‬‬
151: ‫‪-۳‬اعراب‌گذاری واژه‌ها براساس ضرورت شعری جهت سهولت در امر خواندن و‬
1934:‫سیاه‬    ‫پارسی ابلک‪« .‬دو رنگ و بخصوص‬                    ‫[ساسیبه]‌چشم و بور ابرش وگاو دوم‬
3804: ‫می‌آورد «شافیدن‪ :‬سورچمک و لغزیدن‬                 ‫گزفته بساستان‬
5278: ‫تو از تخم ساسانی ای بندژاد‬                       ‫(‪)۲-۱۶۱-۵۲۵‬‬
5280:        ‫که ساسان شبان و شبان‌زاده بود‬                                    ‫(ناصر ‪:)۴۸۳-۸۱‬‬
5288:          ‫رم ساس‬
5294:‫نه ازتخم ساسان رسیدی به نان؟‬                                                   ‫بلنداختر‬
5326: ‫آ[بزن؛ [از بن []بانزه‪ :‬از بیخو بن هرگزء‬                           ‫‪-۴‬پی یایه‪ .‬اساس‪ .‬بنیان‪:‬‬
9881:‫به قیصر سپارد همه یک به یک‬                          ‫از پنج نسخه معتبر و قدیمی که در اساس‬
10148:                                                                 ‫[=‬‫‪+‬پساسرت‬           ‫ک‬
10880:                                                  ‫[زال] شماساس را خواست کاید برون‬
11166:  ‫به بر گستوان بر زد و بر درید‬                                          ‫پزوهندة نامه بساستان‬
11870:            ‫نگون اندر آمد شماساس گرد‬              ‫(‪)۶۸۳۲-۲۵۲‬‬
15027:                                                                 ‫به ساسانیان تاندارید اميد‬
15098:                      ‫پیات اساس» اصل‪:‬‬             ‫(‪)۶-۹۲۳-۷۳۱‬‬
15277:          ‫همه برکشیدند گردان سلیح‬                    ‫دورة ساسانیان مانده و پاره‌ای کتیبه‌ها هم در‬
15291: ‫سازند‪ .‬فخری گوید‪ :‬آنکه بهر خیر بی‌حد‬                ‫«ابران در زمان ساسانیالن» آرتورکریستنسن‬
17249:‫کهبرتخم ساسان پر آمد قفیز‬                           ‫(‪)۷-۵۴۲-۱۷۴‬‬
17311:         ‫اوستاست) از سهپیشه یبارست‬           ‫همان دست‌ورزان ابساسرکشی‪..‬‬
=== leaves
485
```


## [2026-09-06T15:57:50.292Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(100,125):\n    s=t[i]\n    m=re.findall(r'[۰-۹]{2,3}', s)\n    print(i, repr(s[:90].replace('\\n',' ')), m[:4])\nEOF"
}
```


### [2026-09-06T15:57:52.019Z] TOOL RESULT

```
100 '\u202bبرز\u202c                   \u202bی\u202c\u202bکر\u202c                   \u202bید ه\u202c                      \u202bخانهٌ خود ب' ['۲۹', '۳۳۳', '۲۰۱', '۸۳۵']
101 '                                                                                       \u202bبر' ['۶۸۱', '۵۶۷', '۸۱', '۱۷۳']
102 '\u202bبرگی\u202c                                      \u202bبرفزود\u202c   \u202bاز\u202c       \u202bصهود\u202c                  ' ['۴۶۲', '۲۸۴', '۶۵۵', '۶۸۶']
103 '                                                       \u202bمیان\u202a .\u202cتباه\u202a .\u202cخراب\u202c             ' ['۱۷', '۵۸', '۱۰۱', '۶۴۱']
104 ' \u202bبرنشست\u202c                                    \u202bاچ\u202a-\u202cیز\u202c                                    ' ['۲۰۱', '۰۴۵', '۶۳۲', '۸۹']
105 '                                                                                      \u202b\u202aRF' ['۱۰۱', '۴۷۴', '۱۰۱', '۴۷۴']
106 '           \u202bبه شمشیر جان از تنش برکنیم\u202c                                 \u202b(رودکی \u202a-\u202cنفیسی \u202a' ['۸۷۶', '۴۳۳', '۰۸', '۶۶۱']
107 '                                                                                          ' ['۸۴۲', '۹۰۱', '۷۱', '۳۷۱']
108 ' \u202bبسودی\u202c                                       \u202b\u202a۰۵\u202c\u202c   \u202bسیاوش او را به شبستان دعوت می\u200cکند' ['۰۵', '۳۶۱', '۳۱۰', '۸۰۴']
109 '                                                                                      \u202bبسی' ['۵۱۲', '۱۱۲', '۷۴', '۵۲۶']
110 '         \u202bهر آن کز میان باره انگیزند\u202c                   \u202bزیر دینار و ياقوت و مشک و عبیر\u202c  ' ['۶۵۱', '۲۰۲', '۳۲', '۵۷۱']
111 '                                           \u202b\u202a۱۰۸\u202c\u202c                                        ' ['۱۰۸', '۱۶۱', '۲۳۵', '۱۶۱']
112 '\u202bبناکام\u202c                    \u202bبگویید با ما یکایک سخن\u202c                        \u202bیدار یابی به ' ['۴۷۵', '۱۶۷', '۴۱', '۴۳']
113 '                                                 \u202b\u202a1۰\u202c\u202c   \u202bضحاک بااهریمن پیمان بسته و سوگن' ['۶۲۱', '۲۶۱', '۹۰۲', '۲۲']
114 '                           \u202b(منوچهری \u202a:)۹۲\u202c\u202c        \u202bفرس و صحاحالفرس نیامده است\u202a .\u202cدر\u202c  \u202b[' ['۹۲', '۸۳۳', '۷۴۱', '۸۵۱']
115 '                                                                                      \u202bبنی' ['۲۱۲', '۷۵۱', '۴۲۰', '۷۸۲']
116 ' \u202bبوس\u202c                                        \u202b\u202a۱۱۳\u202c\u202c               \u202bواو دم\u202c              ' ['۱۱۳', '۲۵', '۲۶', '۴۱']
117 '                                                                                      \u202bبوش' ['۴۳۱', '۵۵۸', '۲۸۳', '۵۲']
118 ' \u202bگت\u202c   \u202bرینو\u202c      \u202bبو\u202c                                        \u202bبویژه\u202c                   ' ['۳۱۲', '۶۸', '۰۲۲', '۰۷۲']
119 '                                               \u202b\u202a1۹\u202c\u202c                                     ' ['۲۱۳', '۶۶۱', '۴۲۲', '۹۱۳']
120 '        \u202bبسی باره و دژ که کردیم پست\u202c                \u202bای بسیار داشته باشد» (برهان)\u202a:\u202c\u202c     ' ['۶۵۱', '۹۹۳', '۳۱', '۱۸۳']
121 '                                                                                   \u202bبه بیج' ['۴۱۱', '۴۵۷', '۰۵۴', '۳۲']
122 '          \u202bپرستش بھی بر کنم زین جهان\u202c                            \u202bشبی چون شبه روی شسته به ' ['۷۵۱', '۴۴۳', '۶۱', '۲۵۷']
123 '                                                   \u202b\u202a۱۳۰\u202c\u202c                                ' ['۱۳۰', '۶۷', '۶۳', '۶۷۳']
124 '\u202bبیران\u202c                                           \u202b\u202a۳\u202c\u202c     \u202bدل هر دو بیداد \u202a :\u202cسلم و تور]' ['۶۰۱', '۸۵۴', '۸۹۲', '۵۷۳']
```


## [2026-09-06T15:58:08.578Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%B4%D9%88%D8%B1",
 "prompt": "Give the Persian etymology of کشور (kešvar): Middle Persian form, Avestan source karšvar, root, and meaning development. Quote the etymology section."
}
```


## [2026-09-06T15:58:09.516Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%B4%D9%81",
 "prompt": "Is there a Persian entry کشف meaning 'tortoise'? Give its etymology (Avestan kasiiapa-, Sanskrit kaśyapa-, Middle Persian). Quote it."
}
```


### [2026-09-06T15:58:16.690Z] TOOL RESULT

```
# Persian Etymology of کشور (kešvar)

The Persian term کشور derives from Middle Persian **𐭪𐭱𐭥𐭥** (kišwar), which came from Avestan **𐬐𐬀𐬭𐬀𐬱𐬀𐬎𐬎𐬀𐬭𐬀** (karšvar, meaning "realm, region; one of the seven realms").

**Root and Development:**
The Avestan source traces back to the root **𐬐𐬀𐬭𐬀𐬱𐬀** (karš-), meaning "to plough." As the etymology notes, this gives the term its literal sense: "a tract of land bordered by a ploughed line."

**Meaning Evolution:**
The word originally referred to "the seven realms of the (known) world" in ancient Iranic cultures. Following the Middle Iranian era's expanded geographical knowledge, the term broadened to encompass larger regions. After Islam's rise in Persia, it underwent "secularization of the term" and came to denote realms, countries, or territories in general usage.

Related cognates appear in Pashto (کِشْوَر), Central Kurdish (کیشوه‌ر), and other related languages, demonstrating this term's widespread adoption across Indo-Iranian language families.
```


### [2026-09-06T15:58:17.056Z] TOOL RESULT

```
# Persian Entry for کشف (Tortoise)

Yes, there is a Persian entry for کشف meaning "tortoise." It appears under **Etymology 2**.

## Etymology

The word derives from Middle Persian, with connections to earlier Indo-Iranian forms. According to the article:

> "From [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") \[Book Pahlavi needed\] (kšwk' /⁠kašawag⁠/, "tortoise"), from [Proto-Iranian](https://en.wikipedia.org/wiki/Proto-Iranian_language "w:Proto-Iranian language") _[\*kacyápah](/wiki/Reconstruction:Proto-Iranian/kacy%C3%A1pah "Reconstruction:Proto-Iranian/kacyápah")_."

The entry also notes it is "Cognate with [Sanskrit](https://en.wikipedia.org/wiki/Sanskrit "w:Sanskrit") _[कच्छप](/wiki/%E0%A4%95%E0%A4%9A%E0%A5%8D%E0%A4%9B%E0%A4%AA#Sanskrit "कच्छप")_ (kacchapa)."

The word is marked as archaic in modern Persian, with the modern term being لاک‌پشت (lāk-pušt).
```


## [2026-09-06T15:58:27.080Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/kacy%C3%A1pah",
 "prompt": "Give the full reconstruction page: meaning, PIE/PII source, and the list of descendants (Avestan, Middle Persian, Persian, Sogdian, Khotanese) with forms."
}
```


## [2026-09-06T15:58:27.625Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/k%C4%81tara",
 "prompt": "Sanskrit कातर / kātara: give the entry — meaning and etymology if present."
}
```


### [2026-09-06T15:58:30.785Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:58:33.435Z] TOOL RESULT

```
# Proto-Iranian *kacyápah

**Meaning:** "tortoise, turtle"

**Etymology:** Derived from Proto-Indo-Iranian *kaćyápas, cognate with Sanskrit kaśyápa.

**Key Descendants:**

- **Avestan:** kasiiapa (Younger Avestan)
- **Middle Persian:** kšwk (Book Pahlavi, /kašawag/), evolving to kašaf in Classical Persian
- **Sogdian:** kyšph (/kiš(a)p/)
- **Khotanese:** khuysaa
- **Ossetian:** xæfs/xæfsæ (Northeastern Iranian)

Additional reflexes appear across Northwestern Iranian languages (Kurdish dialects, Baluchi), Southeastern Iranian (Pashto: kišáb, kašáb), and Southwestern Iranian (Persian, Lurish).

The word is categorized as a masculine a-stem noun and belongs to the PIE root *kes-.
```


## [2026-09-06T15:58:42.483Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AHD watkins kes-/kas-\"; grep -n -i 'k.s-.*instruct\\|chastise\\|castigate' AHD_watkins1985.txt | head -10; echo \"== IEC / SYN sastar\"; grep -n 'sastar\\|śās\\|sasti' IEC.txt | head -5; echo \"== SYN command\"; grep -n 'COMMAND\\|Av. sāh\\|sastar' SYN.txt | head -10"
}
```


### [2026-09-06T15:58:42.572Z] TOOL RESULT

```
== AHD watkins kes-/kas-
623:(SCARCE). 3. Greek karpos, fruit: -cARP, CARPEL, CARPO-, -CARPOUS. [In Pok. 4. sker- 938.] kers-'. Dark, dirty. 1. Suffixed form *ker(s)-no- in Rus- sian chérnyi (feminine chérnaya), black: CHERNOZEM. 2. Suffixed zero-grade form *krs-no- in Sanskrit krsna-), black, dark: KrisHNa. [Pok. kers- 583.] kers-2. To run. Zero-grade form *krs-. 1. Latin currere (past participle cursus), to run: CORRIDOR, (CORSAIR), COURANTE, COURIER, COURSE, CURRENT, CURSIVE, CUR- SOR, CURULE; CONCOURSE, CONCUR, DECURRENT, DIS- COURSE, EXCURSION, HUSSAR, INCUR, INTERCOURSE, OCCUR, PERCURRENT, PRECURSOR, RECOURSE, RECUR, succor. 2. Suffixed form *krs-o- in Gaulish carros, a wagon, cart, in: a. Latin carrus, a two-wheeled wagon: CAR, CAREER, CARGO, CARICATURE, CARIOLE, CAROCHE, (CARRY), CHARGE, CHARIOT; b. Latin carpentum, a two- wheeled carriage: CARPENTER. [Pok. 2. fers- 583.] kert-. To turn, entwine. I. Zero-grade form *krt-. 1. Suf- fixed form *krt-i- in Germanic *hurdiz, wickerwork frame, hurdle, in: a. Old English hyrdel, hurdle, frame: HURDLE; b. Old French hourd, fence, hurdle, scaffold: HOARDING. 2. Suffixed form “*krt-sti- in Germanic *hur- sti- in Old High German hurst, thicket: Horst. II. Per- haps suffixed variant form *krot-i- in Latin crdatis, wickerwork hurdle: CRATE, GRATE?, (GRID), GRIDDLE; (GRIDIRON). [Pok. kert- 584.] kes-'. To scratch. 1. Germanic *hezd6 in Old English heordan, coarse parts of flax: HARDS. 2. Extended form *kseu- in Greek xuein, to scrape: XYSTER. 3. Nasalized form *ks-n-eu- in: a. Germanic *snaww- in Old Norse snéggr, “close-cropped,” perhaps akin to the source of snuG!: b. Latin novdcula, razor: NOVACULITE. [Pok. kes- 585.] kes-2. To cut. Variant kas-. 1. Suffixed form *kas-tro- in: a. Latin castrare, to castrate: CASTRATE; b. Latin cas- trum, fortified place, camp (perhaps “separated place”): CASTLE. 2. Suffixed form *kas-to- in Latin castus, chaste, pure (< “cut off from, free of, faults”): CASTE, CHASTE; CASTIGATE, INCEST. 3. Suffixed (stative) form *kas-é- in Latin carére, “to be cut off from,” lack: CARET. 4. Ex- tended geminated form *kasso- in Latin cassus, empty, void: (CASHIER), QUASH. [Pok. hes- 586.] kes-°. To order. Suffixed 0-grade form *kos-mo- in Greek kosmos, order: COSMOS; MACROCOSM, MICROCOSM. keu-' Also ekeu-. To perceive, see, hear. O-grade form *akou-. 1. Extended form *kous- in: a. Germanic *haus- Jan in (i) Old English hieran, to hear: HEAR (ii) Old English he(o)rcnian, to harken: HEARKEN; b. suffixed form *9-kous-yo- in Greek akouein, to hear: ACOUSTIC. 2. Variant *skou- in: a. Germanic *skauwon in (i) Old English scéawian, to look at: SHOW (ii) Flemish scauwen, to look at: SCAVENGER; b. Germanic *skaunjaz in Mid- dle Dutch schoon, beautiful, bright (< “conspicuous, attractive”): SCONE; Cc. Germanic *skauniz in Old Eng- lish sciene, bright, sheen: SHEEN. [Pok. 1. keu- 587.] keu-?. Base of various loosely related derivatives with assumed basic meaning “to bend,” whence “a round or hollow object.” I. Extended forms *keub-, *keup-. 1. Ger- manic *haup- in: a. Old English héap, heap: HEAP; b. Dutch hoop, heap, troop: FORLORN HOPE. 2. Germanic *hupp-, to leap (by first bending the legs), in Old English hoppian, to hop: HoP!. 3. Germanic *Aupiz in Old Eng- lish hype, hip: H1P!. 4. Zero-grade form *kup-, vessel, in: a. suffixed form *kup-s- in Greek kupselé, chest, hollow vessel: CYPSELA; b. long-vowel form *kip- in (i) Ger- manic *Aifi- in Old English hyf, hive: HIVE (ii) suffixed form *kip-a in Latin cupa, tub, vat: CUPOLA, CUPULE; c. expressive form *kupp- in Late Latin cuppa, drinking vessel: cup. 5. Zero-grade form *kub- in: a. Greek kubos, cube: CUBE; b. suffixed form *kub-@- in (i) Latin cubdre, to lie down on (< “to bend down, prostrate”): COUVADE, COVEY, CUBICLE; CONCUBINE, INCUBATE, SUCCUBUS (ii) Latin cubitum, elbow: CUBIT; Cc. nasalized form *ku-m-b- in (i) Latin -cumbere, to lie down, recline: ACCUMBENT,
1336:CASE2 kap- CASHIER kes-2 CASTE kes-? CASTIGATE kes-2 CASTLE kes-2 CASTRATE kes-2 CATA- kat-1 CATABOLISM gWele-1 CATACHRESIS gher-5 CATACLYSM kleu-2 CATALECTIC slég- CATALEPSY (s)lag¥- CATALOGUE leg-1 CATALYSIS leu-1 CATAMENIA mé-2 CATAPLEXY plak-2 CATAPULT pél- CATARRH sreu- CATASTASIS sta- CATASTROPHE streb(h)- CATCH kap- CATCHPOLE pau- CATECHIZE (s)wagh- CATEGORY ger-1 CATER-CORNERED kWetwer- CATERPILLAR pilo- CATHEDRA sed-1 CATHEPSIN kat-1 CATHETER yé- CATHODE sed-2 CATHOLIC sol- CATION ei-1 CATOPTRIC okw- CATTLE kaput CAUDILLO kaput CAUDLE kele-1 CAULESCENT kaul- CAULICLE kaul- CAULIFLOWER _bhel-3, kaul- CAULINE kaul- CAUSTIC kéu- CAUTERY kéu- CAUTION keue-1 CAVE keue-2 CAVEAT keue-1 CAVERN keue-2 CAVETTO keue-2 CAVIL  kel-8
== IEC / SYN sastar
8577:Skt. $astah, $asitah, pp. 'chastized'; sastih, Sistih, f. ‘reproof; Per. saxt “hard, strong, vio- lent’; Arm. sast, Let ‘reproof; cf. sastik, adj. ‘severe, acute’; Tokh. A (?) kast, B kest *hun- ger; Hitt. kasc & kastan, id. (here ?); Ir. cas ‘peevish, rash, violent? beside MIr. cás, ad]. “hard, cruel; W cas ‘odious’; ON bast. cpds. “harsh, violent; Icel. hastur “harsh, snappy, violent’; OE (*-à-) hæst ‘violent’ (here ?); Latv. cf. (?) sass (unripe, sour”, but this is apparent- ly isophonic with Lat. cassus ‘empty, vain, use- less. The isophone represented in Latin castus, gs -üs ‘rite, ceremony’, and in castus *devout, chaste' is of ambiguous origin, see WH and EM on these wds. though most pro- bably to type kat- “hold”, cf. cat-ena, etc.)
9025:Koktos (KoKtos) “hard, old, stiff, firm’. Cf. kokstis (with velar initial) WP I, 333 & 358 Skt. Saktáh ‘strong, able’; Av. saxto ‘firm’; Per. saxt “hard, vehement, strong? beside sift “hard, stiff; Arm. cf. sastik (w. assimilated consonants: “hard, severe"); Gaul. cotto- (in a place-name); Br. koz, Cor. coth old: Du. becht “solid, firm”
== SYN command
22305:Av. daogatara-, daogastara-, adj. (-3- fr. usastara- ‘eastern’), fr. *daogq- ‘eve. ning, west’ = Skt. dosa- ‘evening, dark- ness’ (prob. : dicis, etc., above, 1), Barth. 674. Walde-P. 1.777 f.
33534:19.45 COMMAND, ORDER (vbs.)
```


## [2026-09-06T15:58:43.406Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%95%E0%A4%BE%E0%A4%A4%E0%A4%B0",
 "prompt": "Sanskrit कातर (kātara): meanings and etymology. Quote the entry."
}
```


### [2026-09-06T15:58:49.048Z] TOOL RESULT

```
# Sanskrit कातर (kātara)

## Meanings

In Sanskrit, कातर (kātara) functions as both an adjective and noun:

**Adjective:** The term describes someone who is "cowardly, faint-hearted" or "confused."

**Noun:** As a neuter noun, it means "despair."

## Etymology

The etymology is uncertain but offers two theories. One suggests it may be a "vṛddhi derivative of कतर (katará, 'which of two?')." 

Alternatively, some evidence points to a borrowed origin, as "descendants suggest a form with unusual phonological variation and late attestation," indicating possible substrate language borrowing. The term relates to Prakrit कत्तर (kattara, meaning "rubbish").

The word traces back through Proto-Indo-European roots, connecting to the interrogative *kʷóteros ("which").
```


## [2026-09-06T15:58:57.334Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:33533])\nprint('leaf', t[:idx].count('\\f'))\nprint('\\n'.join(lines[33533:33600]))\nEOF"
}
```


### [2026-09-06T15:58:59.107Z] TOOL RESULT

```
leaf 1432
19.45 COMMAND, ORDER (vbs.)
Grk. —_xeAebw, tporracow, Goth. haitan, anabiudan Lith. liepti, isakyti etc. ON bjoda Lett. pavélé NG mpooratw, drarato Dan. _ befale, byde ChSl. (po)veléti, zapovédétz Lat. tubére, imperdre Sw. befalla, bjuda SCr.  zapovijedati, narediti It. comandare, ordinare OE hatan, (ge)béodan Boh.  nariditi, rozkdzati Fr. commander, ordonner ME coma(u)nde, bede, Pol. rozkazaé Sp. mandar, ordenar hote, charge Russ. prikazat' Rum. comanda, ordona, po- NE command, order Skt.  djna&paya-, ddic-, cas- runct (bid, charge) Av.,OPers. niSta- Ir. forcongur Du. bevelen, gebieden Nir.  orditighim OHG  gibiotan, heizan W. gorchymyn MHG heizen, gebieten Br. gourc’ hemenn NHG befehlen, gebieten,
heissen
ud-yudh- ‘boil up, go off in anger’). Walde-P. 1.204. Ernout-M. 500. Walde- H. 1.725:
Lat. imperare, cpd. of pardre ‘prepare, procure’; semantic development ‘pre- pare, arrange’, whence ‘put in order’ and thence ‘command’ (cf. Grk. rpocracow, etc., above, and It. ordinare, below). Ernout-M. 478. Walde-H. 1.683.
It. comandare, Fr. commander, Rum. comanda (neolog.), fr. MLat. comman- dare, for commendare ‘intrust, commend to, recommend’, cpd. of mandare ‘com- mit to one’s charge, enjoin, command’ (> Sp. mandar), fr. *mandha- (cf. Osc. aamanaffed ‘mandavit’), a epd. of man- = manus ‘hand’ (cf. man-ceps, etc.) and a deriv. form of IE *dhé- ‘put’. Ernout- M. 586. Walde-H. 2.24. REW 2084
It. ordinare, Fr. ordonner, Sp. ordenar (Rum. ordona, fr. Fr.; native urdina in different sense), fr. Lat. drdinare ‘set in order, arrange, appoint’, deriv. of drdé
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1338 SELECTED INDO-EUROPEAN SYNONYMS
(-inis) ‘order, rank, class’. Ernout-M. 712. REW 6090.
Rum. porunci, fr. the Slavic, cf. ChSl. porqeiti ‘trust, charge with’ (deriv. of raka ‘hand’. Miklosich 276. Cf. Lat. mandare, above). Tiktin 1218.
3. Ir. forcongur (also forcongrimm), epd. (*for-com-gair-) of gatrim ‘shout, call’ (18.18). Pedersen 2.534. f.
NI. ordiighim, deriv. of drd ‘order’, fr. Lat. drdé (above). Vendryes, De hib. voc. 162.
W. gorchymyn, Br. gourc’hemenn, epds. of Br. kemenn ‘inform, announce, command’ (W. cymyn only sb. ‘bequest, legacy’, orig. ‘command’), fr. Lat. com- mendare (above, 2). Loth, Mots lat. 156 f.
4. Goth. haitan, OE hatan, ME hote, OHG heizan, MHG heizen, NHG heis- sen = Goth. haitan ‘call’, etc. (18.41).
Goth. ana-biudan, ON bjoda, Dan. byde, Sw. bjuda, OE (ge-) béodan, ME bede (and by confusion with OE biddan ‘ask, request’, also bidde, NE bid in this sense, cf. 18.35), Du. gebieden, OHG gibiotan, MAG, NHG gebieten, in North and West Gmc. also ‘offer’ (so usually the simple verb OHG biotan, NHG bie- ten), in OE also ‘announce’ : Grk. zy- Gavouar “find out, hear’, Lith. budéti ‘wake’, ChSl. buditi ‘awaken’, Skt. budh- ‘wake, be awake, notice, be aware’, etc. Pee: 2.147, Falk-Torp 120f. Feist
ME coma(u)nde, NE command, fr. ie comander (Fr. commander, above, ME, NE charge, orig. ‘load’ (fr. OF r. charger, late Lat. carricare, deriv. of carrus ‘car’), formerly very freq. for ‘command’, esp. in our version of the Bible. NED s.y. charge, vb., 14,
NE order, fr. ME ordre ‘arrange, put in order’, deriv. of sb, ordre, fr. OFy. ordre, for earlier ordene, fr. Lat, ordo (inis). NED s.v. REW 6094. Gamill- scheg 651.
Du. bevelen, NHG befehlen, fr. MDu. bevelen (MLG also befalen > Dan. befale, Sw. befalla), MHG bevelhen ‘intrust, commend, charge with’, OHG befelahan ‘give over to, grant, commend’, also ‘hide, bury’ (cf. OF beféolan in various senses, including ‘be urgent with’; Bos- worth-Toller, Suppl. s.v.), simple verb in Goth. filhan ‘bury, hide’, etc. (4.78). Falk-Torp 57. Kluge-G. 45. Weigand- H. 1.178.
5. Lith. liepti, paliepti : OPruss. pal- laipsitwet ‘desire’, pallaips ‘command’, Grk. Nwroua: ‘be eager, long for’, Walde-P. 2.404.
Lith. {sakyti, epd. of 7- ‘to’ and sakyti ‘say’ (18.22).
Lett. pavélét, also ‘permit, grant’, epd. of vélét ‘wish’.
6. ChSl. (po)velétz : voliti ‘will, pre- fer’, Lat. velle ‘will, wish’, ete. Walde-P. 1.294.
ChSl. zapovédéti, SCr. zapovijedati, cpds. of ChSl. povédéti, SCr. povijedati ‘say, tell’ (18.22).
SCr. narediti, Boh. na¥tditi, orig. ‘put in order’: SCr. red, Boh. ¥ad, ChSIl. redt ‘order, arrangement’. Miklosich 276.
Boh. rozkdzati, Pol. rozkazaé, Russ. prikazat’, cpds. of Boh. kdzati, Pol. kazaé ‘order, preach’, Russ. kazat’ ‘show’ (cf. Russ. skazat’ ‘say’, 18.22). Berneker 497,
7. Skt. ajidpaya-, lit. ‘cause to no- tice’, caus. of a-jfd- ‘perceive, notice’, epd. of jza- ‘know’.
Skt. d-dig-, lit. ‘point out, indicate’, epd. of dig- ‘point out, show’.
Skt. ¢as-, also general ‘rule, govern, punish, correct’? = Av. sah- ‘command’ (ef. sdstar- ‘ruler’), esp. ‘teach’ : Arm. sastem ‘scold, threaten, command’. Walde-P. 1.358.
Av., OPers. ni-std-, lit. ‘establish, ar- range’, cpd. of mni- ‘down’, and sta- ‘stand, place’. Barth. 1604.
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
SOCIAL RELATIONS 1339 19.46 OBEY Grk. relBopar, axobw, Goth. ufhausjan Lith. klausyti braxobw ON higoa, hlyonask Lett. klausit NG draxobw, &xobw Dan. __lystre, lyde ChSl. poslusati Lat. oboedire, parére Sw. lyda, hérsamma SCr.  slusati It. obedire OE hyrsumian Boh.  poslouchati Fr. obéir ME _obeie, hersumie Pol. — stuchaé Sp. obedecer NE obey Russ.  sluSat’sja Rum. asculta Du. gehoorsamen Skt. anu-vrt-, anu-stha- Tr. irladigur, giallaim OHG _horen, horsamén NIr.  gallim MHG (ge)hérchen, gehorsa- Ww. ufuddhau men * Br. sentt NHG ss gehorchen
The majority of the words for ‘obey’ are the same as, or connected with, words for ‘hear’ or ‘listen’. Other se- mantic sources are ‘be persuaded’, ‘fol- low’, ‘stand by’.
1. Grk. zelGoua, also ‘believe’, lit. ‘persuade oneself, be persuaded’, mid. of zeOw ‘persuade’ : Lat. fidere ‘trust’, fidus ‘faithful’, etc. (16.65, 17.15).
Grk. dxobw ‘hear’ (15.41), but also ‘listen to, obey’, so already in Hom., and common in pop. NG; epd. braxotw ‘listen to, give ear’, class. also freq. ‘obey’ and reg. lit. NG in the latter sense.
2. Lat. oboedire (> It. obedire, Fr. obéir, Sp. obedecer), epd. of audire ‘hear’ in an earlier form (15.41), but phonology still difficult. Ernout-M. 86, 693f. Walde-H. 1.80. REW 6016.
Lat. pdrére ‘appear, be present’, whence ‘be present at one’s command, obey’, perh. : Grk. (rare) rerapeiy ‘show’. Walde-P, 2.6. Ernout-M. 733.
Rum. asculta, fr. Lat. auscultare ‘lis- ten’ (15.42),
3. Ir. irladigur (cf. no-erladaigtis, gl. parebant, Ml. 16b14, do aurlatu, gl. ad oboediendum Wh. 3b14, etc.), beside sb. trlatu ‘obedience’, adj. irlithe ‘obedient’, Toot connection? Thurneysen, Gram. 166. Walde-P. 2.393 (bottom).
MIr. giallaim, ar-giallaim, NIv. géil- lim, orig. ‘serve, be the gtall of? (Olv. giallaid ‘becomes a vassal’, Ml. 115d12,
etc.), deriv. of giall ‘hostage’. Pedersen 2.537 Anm.
W. ufuddhau, deriv. of ufudd, ufydd ‘humble, obedient’, this fr. Lat. oboediens or a blend with ufyll, fr. Lat. humilis? Cf. Ir. otbid. i. umal. Pedersen 1.195, Anm. Loth, Mots lat. 214.
Br. senti, fr. Lat. sentire ‘feel’, with semantic development through ‘hear, listen to’, ef. It. sentire (15.41). Peder- sen 1.198.
4, Goth. ufhausjan, epd. of uf ‘under’ (influence of Grk. jraxotw?) and hausjan ‘hear’, OHG horen, horran ‘hear’ and also ‘obey’ (reg. for oboedire in Tat.) = ON heyra, OE hyran, etc. ‘hear’ (15.41). Here also OE hyrsumian, ME (early) hersumie, Du. gehoorsamen, OHG (gi)- hérsamon, MHG gehorsamen, derivs. of OE (ge)hyrsum, OHG (gi)hirsam ‘obe- dient’; and MHG horchen, gehdrchen, NHG gehorchen: OHG hérechen, OF heorcian ‘listen’ (15.42).
ON hlgda, Dan. lyde, Sw. lyda, in ON mostly ‘listen’ (15.42). Here also ON, Nicel. hlyOnask (refl.).
Dan. lystre (aow more pop. than lyde, ef. Dahlerup s.v.), fr. MLG listeren ‘listen, hear’ = Du. luisteren ‘listen’, ete. (15.42).
Sw. hérsamma, fr. hérsam ‘obedient’, fr. héra ‘hear’.
ME obeie, NE obey, fr. Fr. obéir (above, 2).
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1340 SELECTED INDO-EUROPEAN SYNONYMS
5. Lith. klausyit, Lett. klauszt, lit. ‘listen’ (15.42).
6. ChSI. poslusatt (reg. for draxobw in Gospels), Boh. poslouchati, cpds. of ChSl. slugati, Boh. slouchati ‘listen’, SCr. slusati, Pol. stuchaé ‘listen, obey’ (SCr. freq. also po-slusati), Russ.
slugat’ ‘listen’, refl. slusat'sja ‘obey’, all orig. ‘listen’ (15.42).
7. Skt. anu-vrt-, lit. ‘go after, follow’, hence ‘attend, obey’, cpd. of anw- ‘after, with’, and vrt- ‘turn, move, proceed’.
Skt. anu-sthd-, lit. ‘stand by’, hence ‘perform, obey’, cpd. of anu- (cf. above) and stha- ‘stand’.
19.47 LET, PERMIT
Grk. td, edly, Erirpizw Goth. Jlétan, uslaubjan Lith. leisti, pavelyti
NG adlyw, éxirpérw ON lata, leyfa Lett. (at)l’/aut, atvélét
Lat. sinere, pati, permit- Dan.  tillade ChSl. poveléti, ostaviti tere Sw. tilldta SCr.  dozvolitz
It. lasciare, permettere OE l@tan, lifan, pafian Boh.  dovoliti, nechati
Fr. laisser, permettre ME lieve, lete Pol. pozwolié
Sp. dejar, permitir NE let, permit Russ. pozvolit', razresit'
Rum. lésa, permite Du. toelaien, veroorloven Skt. anu-jnid-
```


## [2026-09-06T15:59:10.791Z] TOOL CALL #59: Bash

```json
{
 "command": "ls site/pages/244.jpg 2>/dev/null; pdftoppm -f 244 -l 244 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg244 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T15:59:12.790Z] TOOL RESULT

```
site/pages/244.jpg
total 8512
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 11:59 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     980 Sep  6 11:59 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  180887 Sep  6 11:56 bqt1637_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50592 Sep  6 11:56 bqt1637_kaz.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   84366 Sep  6 11:54 c246_n2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51690 Sep  6 11:54 c246_n6.png
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
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:52 p233
-rw-rw-r-- 1 sfmqrb sfmqrb   33321 Sep  6 11:51 part1.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb   78380 Sep  6 11:51 pg239.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81131 Sep  6 11:51 pg240.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97613 Sep  6 11:49 pg242.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80947 Sep  6 11:59 pg244.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80632 Sep  6 11:55 pg245.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79253 Sep  6 11:54 pg246.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
```


## [2026-09-06T15:59:15.895Z] TOOL CALL #60: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg244.png"
}
```


### [2026-09-06T15:59:16.268Z] TOOL RESULT

```

```


## [2026-09-06T15:59:16.265Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:59:25.936Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=dict()\nparts=re.split(r'\\[pdf page (\\d+)\\]', t)\nfor i in range(1,len(parts),2): pages[int(parts[i])]=parts[i+1]\nfor p in (365,366,367):\n    s=pages.get(p,'')\n    print('#### pdf',p, s[:700].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-06T15:59:27.881Z] TOOL RESULT

```
#### pdf 365  | —\evy— se |  | بواو کشیده , رستنی و گیاهی است بیار ست | و نابی‌که ازآرد خشکه پشته باشند بصی خوب | ‎JL,‏ بارنکی‌هم دارد وآنرا بعربی شکاعی‌خوانند. | و عربان ‎Te‏ شخصی را ‎ation‏ که‌بیار ضیف | ولاغراست گوبند : « کاله عود شکاعی» . |  | کالگ ه بسکون ‎IT‏ بمعنی‌مرد باشد | که درمقابل زن است٩‏ - و بمعنی‌مردم که‌آدمی | باشد - و مردمك چشم هم حست و جربی اننان | ‎cell‏ خوانند ۴ - وهرچیز خشاث را کوبندعموماً | وکوشت قدید را ‎Lopes‏ - وآدمی وحیوانی که | بسیار لاغر و ضعیف شده باشد ۴ - و ان ختك |  | لپخته باشند و روغن و شیر در آن نکرده ‎wath‏ | ‏و ممرب‌آن ‎FELT‏ است وبسنی کویند کال قرض | نان‌روغنی‌است وآترا بعربی كمك خوانشد افاعلم | — وفرص ماه را نیز گوبند که ماه شب چهاردء | باشد ۵ - ونام قلمه ایست ازقلاع آذربایجان - | ویمعنیکاواك ‎ay‏ خالی‌عم 
#### pdf 366  | ۱0۷۳ | و فقلات را | تیز کویند - و (۱) ‎wate‏ عمو ‎ath‏ که ‎why‏ | ‎py‏ است . |  | , ‏بالفکنيده و بواوزده‎ » WIT | ‏وآن چنان است.که يك کس‎ ath ‏از بازی‎ ey! | » ‏دستها را برزمین گذارد و فرباد کند که « کاکاو‎ | ‏وحریفان دیگر از اطراف او درآهده او را درباد‎ | ‏آوهمان طریق دست بر زمین نپاده‎ i SOK | ‏سرپای خودرا‎ SS yes ‏از عقب حریفان دود‎ | . ‏برساند اورا بجای خودآوردا‎ |  | کا کیان - با بای بالف کشیده بروزن | باغبان ‏ گل‌کاجیره باشد که بعربی معصف رکوبند. |  | کاکره - بکسکان‌رفتح رای بی‌قطه, | داروبی است که آنرا عافرقرحا خوانند ‎ok.‏ را | زباد کند» ‎ge OT,‏ گیاهی‌باشد وبعربی‌عودالفرح | ‎ay‏ ؛ و بفتح کاف ورا عم‌آمده است. |  | کا کل ینم کاف تازی وسکون 1 |  | خانه بیر شده باشد - و ‎Bye‏ خشك |  | ye |  | و اسپ واستر وغیره باشد ۴ - ولوعی ا زکندم | حم ‎(
#### pdf 367  | IST | ‏سلمین فردون و دختر‎ le ‏بوده ازیسرزاده‎ e | ‏نیز گویند با‎ ٩ ‏زادة دختر خحاله راوراکاکوی‎ | ‏در دست سم اریمان‎ gly » ‏درآخر‎ les ‏زیادتی‎ | ‎. ‏شته شد‎ |  | OS ‏بر وزن باقوتی‎ - GIO | . ۴ ‏است که آنرا بعربی سعترخوانند‎ |  | کاکوش- بروزن آغوش » پنفشه را | ‎Pao‏ وآن کلی باشد موف ومشهور. |  | کاکول ؟ ین اف و سکون واو | ولام . ‎ISB ew‏ است که موی ‎Ole‏ سرمردان | وپسران واسب واستر باشد . |  | کا کو 4 * - ‎SE game ging‏ | است که خالو باشد وآن برادر مادر است- ‎phy‏ | ‏پهلوانی هم بود» از پسرزاده های سلم‌بن فریدون | ودخترزاده‌های ضحاك . |  | . ‏ولف‎ cue: 3). 18160 - ۱ |  | —Nevi— |  | ‎ST‏ »بر رزن خاکی ؛ نام شخصی | است که پسراورا ماکان میگفته‌اند ‎ub Se,‏ | ۹1 | کال = ‎Vo,‏ » نی خم‌وخمیده | و کج باشد ۷ - وجا ومقام وجایگاه بودچه‌متانه | کال ‎Aa Se wl.‏
```


## [2026-09-06T15:59:45.464Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HUB\"; grep -n -i 'kišvar\\|kesvar\\|kasyapa\\|suxan\\|saxvan\\|pasux\\|pâsux' HUB.txt | head -10; echo \"== ARY latin index\"; grep -n -i 'KARSHVAR\\|KESHVAR\\|SOKHAN\\|SAKHUN\\|PASOKH\\|KASHAF' incoming/ARY/ARY_latin_index_pages.txt | head -10; echo \"== ARY persian\"; grep -n 'کشور\\|سخن' incoming/ARY/ARY_pages.txt | head -8"
}
```


### [2026-09-06T15:59:45.553Z] TOOL RESULT

```
== HUB
1206:p. 103) ist nach np. und paz. pasux (Shk. 263, Min.
4398:zd. nava^); ausl. -ux aus -axv: pasux 'Antwort* = phi.
4400:= phi. fairaxv; suxtin ^= suxan *Wort', paz. saxun aus
4670:gift*, paz. pad(a)zah(a)r Shk. 261 ; np. paz. pasux *Antwort*,
6308:*Schildkr5te' neben kaSav (bei Vullers) = zd. kasyapa-y
6546:Vgl. auch kasaf 'SchildkrSte* = zd. kasyapa- (§ 71).
6767:paz. pasux 'Antwbrt' aus ^pdtsaxv (neben phi. pasaxo aus
6845:II, 297 und -pan schiitzend'; np. paz. pasux 'Antwort' aus
7466:ap. &uxra'; suxun^ suxan *Wort* aus iran. "^saxvan- = ap.
7562:•^ zd. syava- (aber kasaf 'Schildkrote' = zd. kasyapa-,
== ARY latin index
== ARY persian
106:نژاد برخی از آنها سفید و برخی دیگر هندی و بفیه افریقایی است. اکثر مردم کشور پرو از نژاد سرخ
266:در ایالت کبک در کانادا (یک زبان پیرامون) از زبان فرانسه‌ی رایج د رکشور فرانسه کمتر تغیی رکرده
386:مردم جهان به زبان عبری سخن می‌گفتند ولی از آن پس زبانهای مختلف (که در واقع نوعی تنیه ‏
634:نظر شمار سخنگویان (بیش از یک میلیارد نفر) بزرگترین خانواده‌ی زبان‌های هند و اروپایی
661:در شمال افریقاکشور ایجاد کردند. در خاور دریای خزر نیز قوم ایرانی دیگر (سغدها پا سغدیان‌ها
731:سخنگویان به این زبان‌ها پیش از ۱۳۰ میلیون نفر است.
749:آثار فلسفی و تاریخ ی گوناگون. زبان یونانیکلاسیکه به ندریج تبدیل به یونانی نوین شد. سخنگویان
765:مرکزی و بخشی از امریکای شمالی بردند. امروزه شمار سخنگویان این زبان‌ها به حدود ۹۰۰ میلیون
```


## [2026-09-06T15:59:54.431Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef leaf(ln):\n    idx=sum(len(l)+1 for l in lines[:ln-1]); return t[:idx].count('\\f')\nfor ln in (7466,6546,6308,4398,6767):\n    print('--- line',ln,'leaf',leaf(ln),'≈p',leaf(ln)-10)\n    print('\\n'.join(lines[ln-4:ln+4]))\nEOF"
}
```


### [2026-09-06T15:59:56.441Z] TOOL RESULT

```
--- line 7466 leaf 220 ≈p 210
idg. A;', k% ist im Np. nicht durch h sondern durch .s ver-
treten :
sal Mahr = zd. sareda-; surx Voth* = zd. suxra-,
ap. &uxra'; suxun^ suxan *Wort* aus iran. "^saxvan- = ap.
*&a(h)uvan' von &ah *sprechen, skr. gq^, zd. satlh; sang
*Stein, ap. a&angaina- *steinern ; sard 'kalt' = zd. sareta-;
saya *Schatten' = skr. chdya- (mit ch aus idg. k%) u. s. w.
Vgl. Horn 688 — 765. Ebenso in Zusammensetzungen :
--- line 6546 leaf 195 ≈p 185
standen sein kann ^). So bei guSof 'dissipatio* neben *gic§db,
s. p. 184, laf Trahlerei', wenn es zu laba, lava *Schmeichelei*
gehOrt etc.
Vgl. auch kasaf 'SchildkrSte* = zd. kasyapa- (§ 71).
Dunkel ist das Verhaltniss von np. farr 'Glanz, Maje-
stat* == ap. farnah' (in VindafarnO) zu dem gleichbedeuten-
den np. xurrah = zd. xwarenah- (s. oben p. 83).
§ 81. Ap. / vor t^ 5, s, r (= idg. p) ist immer =
--- line 6308 leaf 188 ≈p 178
np. sag gegen medisch spaka- {andyt-u bei Hero dot), ka§.
esbdf espd, semn. esbe, g. saba, zd. spa (nom. sg.), afgh. spai.
Fiir 6; v aus p erscheint unregelmassig / in kasaf
*Schildkr5te' neben kaSav (bei Vullers) = zd. kasyapa-y
afgh. kasap ; fdm *Schuld* = vam s. § 66 ; afranjan = avran-
jan = abratijan §72; afdum letzter (fiir afdum, oben p. 8)
= paz. awadum, phi. *ap'tum^ ap. *apatama? Vgl. auch laf
*Prahlerei' (H. 952, oben p. 96) neben lava^ laba 'Schmeichelei*
--- line 4398 leaf 136 ≈p 126
bavaiti, vgl. ap. abavam (aber np. conj. 3. p. bad aus phi.
bavdt = ap. bavatiy); nuvad^) neunzig' = zd. navaiti; nuh
*neun' aus *w^< (mit h nach dah zehn') fiir *nuv = *nav,
zd. nava^); ausl. -ux aus -axv: pasux 'Antwort* = phi.
pasaxv (oben p. 36, Pandnama Gl. p. 99) ; farrux 'gliicklich'
= phi. fairaxv; suxtin ^= suxan *Wort', paz. saxun aus
sax^'arij arm. -sohun im N. pr. Bastsohun (bei Mos. Chor.).
Wechsel von a und u: -bad == -bud *Herr (vgl. herbiid,
--- line 6767 leaf 201 ≈p 191
np. paskam *aula' = arm. patskainb = ap. ^patiskanba- (s.
oben p. 41); np. pasand 'angenehm, gefallig, paz. pasan-
dtdan *to approve* =^ ap. "^pati-sanda' (s. oben p. 41); np.
paz. pasux 'Antwbrt' aus ^pdtsaxv (neben phi. pasaxo aus
*patsaxv), vgl. arm. patasxani 'Antw^ort' (s. oben p. 36);
np. pasaxt aus *patsdxt (s. oben p. 36) neben paz. phi.
pasaxt etc. (Shk. 262 — 263) aus patsdxt, Diese Assimili-
rung war erst sassanidisch, wie das Arnienische zeigt, das
```


## [2026-09-06T16:00:40.093Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'kasyapa\\|kasiiapa' BRT.txt | head -5; echo \"== col markers near\"; grep -n 'kasyapa' BRT.txt | head -1 | cut -d: -f1"
}
```


### [2026-09-06T16:00:40.164Z] TOOL RESULT

```
9423:lat    mqm    mairyS    äkaiat    "darauf  er-  •  j.   kasyapa-    m.   'Schildkröte',    die    als
== col markers near
9423
```


## [2026-09-06T16:00:43.629Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%A9%D8%B4%D9%88%D8%B1' --note 'page 244, root Karsvar: Persian kešvar < MP kišwar < Av. karšvar' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%A9%D8%B4%D9%81' --note 'page 244, root Kasyapa: Persian kašaf tortoise etymology' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/kacy%C3%A1pah' --note 'page 244, root Kasyapa: PIr *kacyapah descendants incl. Sogdian kyšph' 2>&1 | tail -20"
}
```


### [2026-09-06T16:00:46.306Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2dd9d78a4f2397c4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/30c6853a87e94cb1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ac33ae7de882b738.txt
```


## [2026-09-06T16:00:56.286Z] TOOL CALL #66: Bash

```json
{
 "command": "for u in 'https://en.wiktionary.org/wiki/%D8%B3%D8%AE%D9%86' 'https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B3%D8%AE' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/c%C3%A1nhati' 'https://en.wiktionary.org/wiki/%E0%A4%95%E0%A4%BE%E0%A4%A4%E0%A4%B0'; do python3 tools/fetch_source.py \"$u\" --note 'page 244, roots Kas 2 / Katara: modern etymology check'; done 2>&1 | tail -10"
}
```


### [2026-09-06T16:00:59.372Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/42784e83f7dc7fbf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/010682aa738991b5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2584fc8d278b8c2e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dba81bd8aa90b077.txt
```


## [2026-09-06T16:07:53.695Z] TOOL CALL #67: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk244.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 244,\n \"book_page\": 214,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n\n # ---------------- entry 0 : Karšvar ----------------\n {\n  \"entry\": 0,\n  \"root\": \"Karšvar\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"Avestan karšvar- / karšvan- n. 'one of the seven regions (\\\"circles\\\") of the earth, continent' (Bartholomae col. 459); from the verbal root karš- 'to draw, plough (a furrow)'\",\n  \"note\": \"The Avestan word, its meaning and Nourai's gloss are exactly right: Bartholomae AiW col. 459 has 'karsvar-, -van- n. \\\"Kreis\\\" der Erde, vgl. \\\"Erdteil\\\"', i.e. literally a 'circle' of land — the seven karšvars of Zoroastrian cosmography (arəzahi, savahi, fradaδafšu, vīdaδafšu, vouru.barəšti, vouru.jarəšti, xvaniraθa). What is NOT right is the second half of the language label: 'Old Persian'. Kent's Old Persian lexicon has no karšvar-; the only OP word of this shape is karša- 'a unit of weight' (Kent p. 179), which is unrelated in meaning. The word is Avestan (and Pahlavi/Pazand) only, so the box should read 'Avestan'. Etymologically the modern consensus (Wiktionary, following the Avestan lexica) analyses karšvar- as a derivative of karš- 'to plough', the region being 'a tract bounded by a ploughed line' — a derivation Nourai does not give but which is compatible with his gloss.\",\n  \"note_fa\": \"ریشهٔ «کَرشور» در اوستا karšvar-/karšvan- به معنای «کشور، بخشی از هفت‌بخشِ زمین» است؛ بارتولمه در ستون ۴۵۹ فرهنگ ایرانی باستان آن را «دایرهٔ زمین، بخشِ زمین» معنی کرده و همین با معنایی که نورایی داده («دایره‌ای از خاک») یکی است. ساختِ واژه از ستاک karš- «شخم زدن، خط کشیدن» است، یعنی «زمینی که با شیارِ گاوآهن مرزبندی شده». تنها ایرادِ برچسبِ زبانی است: در پارسی باستان چنین واژه‌ای گواهی نشده و در واژه‌نامهٔ کِنت تنها karša- «یکای وزن» آمده که ربطی به این معنا ندارد؛ پس باید تنها «اوستایی» نوشته می‌شد. ادعای نورایی با این اصلاحِ کوچک پذیرفتنی است.\",\n  \"sources\": [W + \"%DA%A9%D8%B4%D9%88%D8%B1\"],\n  \"ref_check\": [\n    {\"ref\": \"BRT:459\", \"status\": \"supports\", \"note\": \"BRT.txt line 9395, between the OCRed column numbers 457 (line 9345) and 463 (line 9463), i.e. col. 459-461: 'j. karsvar-, -van- n. \\\\'Kreis\\\\' der Erde, vgl. \\\\'Erdteil\\\\'' with the Yašt/Yasna citations (Yt.10.15, 10.67, 10.133, Y.57.31, V.19.39). Exactly Nourai's root, gloss and page.\"},\n    {\"ref\": \"HRN:191\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 212 = printed p.191 (leaf = printed + 21), entry no. 858: 'kišver, kesver \\\\'Erdteil\\\\'. aw. karsvar- \\\\'Weltteil\\\\'; phlv. kisvar.' Horn gives precisely Nourai's three-step chain Avestan > Pahlavi > New Persian on the cited page.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"Lexicon p.179 s.v. karša-\", \"stance\": \"contradicts\", \"note\": \"grep 'kar[sš]' in KNT.txt: the only Old Persian entry is 'karša- sb. \\\\'weight, (unit by) weight\\\\' ... = 83.33 gr.'; there is no OP karšvar-, so the 'Old Persian' half of the language label has no support.\"},\n    {\"src\": \"PHD\", \"where\": \"English-Pahlavi index s.v. 'clime', 'region'; s.v. hamkišwar\", \"stance\": \"supports\", \"note\": \"MacKenzie PHD.txt line 1253 'clime kišwar', line 3360 'region kišwar; v. district', line 392 'hāmkišwar [(h)mkyšwl | M -wr] universe' — Pahlavi kišwar is well attested with exactly the meaning Nourai gives.\"},\n    {\"src\": \"BQT\", \"where\": \"vol.3 pdf p.449 = printed p.1656, footnote 6 to کشور\", \"stance\": \"supports\", \"note\": \"Mo'in's footnote: 'اوستا - karshvar «بارتولمه ۴۵۹»، پهلوی Kishvar (قطعه، قسمت)، پازند keshvar «نیبرگ ۱۲۸-۱۳۰» ... معین ۲۷۸' — Mo'in himself cites Bartholomae col. 459, i.e. the very page Nourai cites.\"},\n    {\"src\": \"BRT\", \"where\": \"cols. 459, 1874-area cross-references (vouru.barəšti-, vidaδafšu-, fradaδafšu-)\", \"stance\": \"supports\", \"note\": \"BRT.txt lines 23817, 23821, 24032: 'Name des im Nordosten/Nordwesten/Südwesten gelegenen Erdteils (karšvar-, sd.)' — confirms karšvar- as the technical term for the seven regions.\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"kîšvar\", \"verdict\": \"confirmed\",\n    \"derivation\": \"Avestan karšvar- gave Middle Persian kišwar by the regular Middle Iranian loss of the syllable-final r before the cluster (Old Iranian -ršv- > MP -šw-) and raising of the resulting short vowel: *karšvar > *kašwar > kišwar (Book Pahlavi <kyšwl>). MacKenzie's Concise Pahlavi Dictionary glosses it 'clime, region' and records the compound hāmkišwar 'the whole world, universe'; in Zoroastrian Pahlavi cosmology the haft kišwar are the seven karšvars of the Avesta, so the meaning is transmitted unchanged. Nourai's transcription 'kîšvar' with long î matches the Book Pahlavi spelling <kyšwl>; the Pazand form is kešvar (Nyberg, Manual II 128-130, as cited by Mo'in).\",\n    \"derivation_fa\": \"فارسی میانه (پهلوی) kišwar از اوستایی karšvar- به دست آمده است: خوشهٔ -ršv- ایرانی باستان در فارسی میانه ساده شده و r آن افتاده است (*karšvar > *kašwar > kišwar، به خط پهلوی <kyšwl>)، و واکهٔ کوتاه نیز به i برکشیده شده. مکنزی در فرهنگ کوچک پهلوی آن را «اقلیم، ناحیه» معنی کرده و ترکیب hāmkišwar «همهٔ جهان» را نیز آورده است؛ در جهان‌شناسی زردشتی «هفت کشور» همان هفت karšvarِ اوستا است، پس معنا دست‌نخورده مانده. صورت پازندِ keshvar را نیبرگ (۱۲۸-۱۳۰) آورده است. ادعای نورایی درست است.\",\n    \"sources\": [W + \"%DA%A9%D8%B4%D9%88%D8%B1\"],\n    \"ref_check\": [\n      {\"ref\": \"BRT:459\", \"status\": \"partial\", \"note\": \"BRT.txt line 9395 (col. 459-461) is the Avestan entry karsvar-; Bartholomae's article does not itself list the Pahlavi reflex (his Pahlavi glosses are given only where the Pahlavi version translates the passage). The page supports the Avestan starting point of the arrow, not the Pahlavi form; for that see PHD and BQT below.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"index s.vv. 'clime', 'region'; s.v. hāmkišwar (p.44)\", \"stance\": \"supports\", \"note\": \"'clime kišwar' (PHD.txt:1253), 'region kišwar' (PHD.txt:3360), 'hāmkišwar [(h)mkyšwl | M -wr] universe' (PHD.txt:392).\"},\n      {\"src\": \"HRN\", \"where\": \"p.191 no. 858\", \"stance\": \"supports\", \"note\": \"'aw. karsvar- \\\\'Weltteil\\\\'; phlv. kisvar' — Horn gives the Pahlavi form explicitly.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, pp.128-130 (as cited by Mo'in in BQT vol.3 p.1656 n.6)\", \"stance\": \"supports\", \"note\": \"Mo'in's footnote quotes 'پازند keshvar «نیبرگ ۱۲۸-۱۳۰»'; a direct grep of NYB_vol2_glossary.txt for kišwar/kiswar returned nothing (the glossary of Nyberg's Manual covers only the texts edited in Part I), so the form is confirmed via MacKenzie and Mo'in's citation of Nyberg.\"}\n    ]\n   },\n   {\n    \"id\": 2, \"lang\": \"Persian\", \"words\": \"kešvar «کشور»\", \"verdict\": \"confirmed\",\n    \"derivation\": \"New Persian کشور kešvar continues Middle Persian kišwar directly and without change of shape; the only development is the ordinary NP lowering of the Pahlavi short i to e in an open first syllable (kišwar > kešvar), the same change as in dil > del, dið > did. Semantically the word was secularised: in the Pahlavi books it is one of the seven mythical karšvars, in Ferdowsi and later New Persian it is already 'clime, region', and in the modern language 'country, state'. Borhan-e Qāṭeʿ (printed p.1656) still gives the old sense first — 'کشور: ترجمهٔ اقلیم است که هفت حصه از هفت اقلیم ربع مسکون باشد ... کشور اول ... به زحل و آن هندوستان است' — showing the astrological seven-clime scheme intact in the 17th century; the compound کشورخدای kešvar-xodāy 'king' ('lord of the realm') is listed on the same page.\",\n    \"derivation_fa\": \"«کشور» در فارسی نو دنبالهٔ مستقیم kišwarِ فارسی میانه است و تنها دگرگونی آوایی، بدل شدن iِ کوتاهِ پهلوی به eِ فارسی نو در هجای باز است (kišwar > kešvar)، همان تحولی که در dil > دل و diz > دژ دیده می‌شود. تحول معنایی از «هریک از هفت کشورِ اسطوره‌ای» به «اقلیم، ناحیه» و سپس «مملکت» رفته است؛ برهان قاطع (ص ۱۶۵۶) هنوز معنای کهن را نخست می‌آورد: «کشور: ترجمهٔ اقلیم است که هفت حصه از هفت اقلیم ربع مسکون باشد ... کشور اول ... به زحل و آن هندوستان است»، و در همان صفحه «کشورخدای» را «پادشاه» معنی کرده است. حاشیهٔ معین بر همین صفحه ریشه را اوستایی karshvar با ارجاع به بارتولمه ۴۵۹ می‌داند. ادعای نورایی درست است.\",\n    \"sources\": [W + \"%DA%A9%D8%B4%D9%88%D8%B1\"],\n    \"ref_check\": [\n      {\"ref\": \"BQT:1656\", \"status\": \"supports\", \"note\": \"Borhan-e Qāṭeʿ vol.3, pdf page 449 of BQT_v3_picofile.pdf = printed p.1656 (running head ۱۶۵۶): the headword کشور with the seven-clime explanation, followed by کشورخدا/کشورخدای; footnote 6 reads 'اوستا - karshvar «بارتولمه ۴۵۹»، پهلوی Kishvar (قطعه، قسمت)، پازند keshvar «نیبرگ ۱۲۸-۱۳۰»'. Exactly Nourai's arrow.\"},\n      {\"ref\": \"BRT:459\", \"status\": \"supports\", \"note\": \"col. 459-461 karsvar- 'Kreis der Erde, Erdteil' — the Avestan ancestor at the head of the chain, as Mo'in's own footnote on BQT 1656 also cites.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"p.191 no. 858\", \"stance\": \"supports\", \"note\": \"'858. kišver, kesver \\\\'Erdteil\\\\'. aw. karsvar- \\\\'Weltteil\\\\'; phlv. kisvar' — Horn's headword is the New Persian word itself.\"},\n      {\"src\": \"BQT\", \"where\": \"vol.3 printed p.1656 with Mo'in's footnote 6\", \"stance\": \"supports\", \"note\": \"quoted above; Mo'in adds the Pashto/Pazand comparanda and refers to his own Farhang p.278.\"},\n      {\"src\": \"PHD\", \"where\": \"s.v. kišwar\", \"stance\": \"supports\", \"note\": \"gives the Middle Persian link of the chain.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/کشور\", \"stance\": \"supports\", \"note\": \"'From Middle Persian kyšwl (kišwar), from Avestan karšvar \\\\'realm, region; one of the seven realms\\\\', from the root karš- \\\\'to plough\\\\'; literally a tract of land bordered by a ploughed line'; notes the post-Islamic secularisation to 'country'.\"}\n    ]\n   }\n  ]\n },\n\n # ---------------- entry 2 : Kâs 2 ----------------\n {\n  \"entry\": 2,\n  \"root\": \"Kâs 2\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *ḱeh₂s- (Pokorny kās-, kəs-) 'to instruct, direct, chastise'\",\n  \"note\": \"Pokorny p.533 has the root exactly as Nourai gives it: 'kās-, kəs- \\\"zurechtweisen, anweisen\\\"; nur arisch und armenisch', with Skt śāsti 'weist zurecht, züchtigt, herrscht, befiehlt, belehrt', śāstár- 'Bestrafer, Gebieter' = Av. sāstar- 'Gebieter, Fürst', MPers. sāstār 'Herrscher', Av. sāx°an- n. 'Lehre', sāsnā 'Lehre, Gebot'. Nourai's gloss 'to direct, command' and his reference WLD1:358 (= Walde-Pokorny I 358, which Pokorny cites at the foot of the article) are both correct. The one caveat, which Pokorny states himself, is that the root is attested only in Indo-Iranian and Armenian, so labelling the box 'Indo-European' is a convention rather than a comparative fact; modern reconstruction writes it *ḱeh₂s- (LIV 'kās'). The problems on this page are not with the root but with two of the Persian words hung under it — soxan and pāsox — which belong to the homophonous but distinct root *ḱens- (Pokorny 566, Nourai's own 'Kens'); see the nodes.\",\n  \"note_fa\": \"پوکورنی در صفحهٔ ۵۳۳ ریشه را دقیقاً به همان صورت آورده است: kās-, kəs- «سرزنش کردن، راهنمایی کردن؛ تنها در آریایی و ارمنی»، با سنسکریت śāsti «می‌آموزد، فرمان می‌دهد»، śāstár- «فرمانروا» برابر با اوستایی sāstar- «فرمانروا، سرور»، فارسی میانهٔ sāstār «حکمران»، اوستایی sāx°an- «آموزه» و sāsnā «آموزه، فرمان». پس ریشه، برچسب زبانی و معنای «فرمان دادن، راه نمودن» درست است و ارجاع WLD1:358 نیز همان جایی است که خودِ پوکورنی به آن ارجاع داده. تنها نکته آنکه این ریشه، به گفتهٔ خودِ پوکورنی، بیرون از هندوایرانی و ارمنی گواهی ندارد و بازسازی امروزی آن *ḱeh₂s- است. اشکال این صفحه در خودِ ریشه نیست، بلکه در دو واژهٔ «سخن» و «پاسخ» است که به ریشهٔ دیگرِ *ḱens- (پوکورنی ۵۶۶) تعلق دارند.\",\n  \"sources\": [W + \"Reconstruction:Proto-Iranian/c%C3%A1nhati\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:533\", \"status\": \"supports\", \"note\": \"POK_02.txt record 192 (the page after the running number 533 in record 191): 'käs-, k(ə)s- ,zurechtweisen, anweisen\\\\'; nur arisch und armenisch. Ai. sästi ... av. sästi ,heißt, lehrt\\\\' ... ai. sästdr- ,Bestrafer, Gebieter\\\\' = av. sästar- ,Gebieter, Fürst\\\\', mpers. sastär ,Herrscher\\\\', ... av. säx°an- n. ,Lehre\\\\', säsnä ,Lehre, Gebot\\\\' ... WP. I 358, WH. I 179.' Verbatim support for the root and its gloss.\"},\n    {\"ref\": \"WLD1:358\", \"status\": \"supports\", \"note\": \"Walde-Pokorny I 358 is the reference Pokorny himself gives at the end of the article ('WP. I 358'), and Buck (SYN p.1338) also cites 'Walde-P. 1.358' for exactly this material (Skt. śas- = Av. sāh- 'command', cf. sāstar- 'ruler'). Band I of Walde-Pokorny is not on disk as searchable page-tagged text (only WLD_band3 = the index volume), so the page was verified indirectly through the two books that cite it.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SYN\", \"where\": \"Buck §19.45 'Command, Order', p.1338\", \"stance\": \"supports\", \"note\": \"SYN.txt leaf 1432, immediately before the running head '1339': 'Skt. ças-, also general \\\\'rule, govern, punish, correct\\\\' = Av. sah- \\\\'command\\\\' (cf. sāstar- \\\\'ruler\\\\'), esp. \\\\'teach\\\\' : Arm. sastem \\\\'scold, threaten, command\\\\'. Walde-P. 1.358.'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. (kās-/kəs- material)\", \"stance\": \"partial\", \"note\": \"IEC.txt line 8577 gathers 'Skt. śastah, śasitah, pp. \\\\'chastized\\\\'; śastih, śistih f. \\\\'reproof\\\\'; Arm. sast \\\\'reproof\\\\', sastik \\\\'severe\\\\'', but Mann attaches Persian saxt 'hard' here and does not mention sāstār; he also keeps Lat. castus separate as of ambiguous origin.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, IE roots appendix\", \"stance\": \"silent\", \"note\": \"grep of AHD_watkins1985.txt finds kes-1 'to scratch', kes-2 'to cut' (castigate, chaste) and kes-3 'to order' (kosmos), but no entry for kās- 'to instruct' — expected, since Watkins lists only roots with English reflexes and this root is Indo-Iranian + Armenian only.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Etymological Dictionary of the Iranian Verb, p.334 s.v. *sanh\", \"stance\": \"partial\", \"note\": \"Cheung has no *sāh 'instruct' lemma; his neighbouring root *sanh 'to declare, explain' (< PIE *ḱens-, 'Pok.: 566') is the one that carries MP saxwan and passox, which is where Nourai's chart goes wrong further down.\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1, \"lang\": \"Avestan / Old Persian\",\n    \"words\": \"sâs 1, sâh 1; sâsta, sâstar; sâxvan, sâsnâ; paiti-sahva\",\n    \"verdict\": \"disputed\",\n    \"derivation\": \"Five of the six forms are exactly Pokorny's own material on the cited page and are confirmed. Av. sāh- (present sāsti, 3sg 'he teaches, commands'; Bartholomae AiW col. 1574-75 's.h- V. \\\"heissen\\\", Praes. 1 sāh-, mit frā \\\"lehren, offenbaren\\\"') is the Iranian continuation of PIE *ḱeh₂s-, Skt śās-; the s-present stem gives Nourai's 'sās'. The verbal adjective sāsta- 'taught, instructed' and the agent noun sāstar- m. 'Gebieter, Machthaber, Fürst' (AiW col. 1574, exactly Nourai's BRT:1574) are formed with the inherited -ta- and -tar- suffixes; sāstar- is used in the Gāthās and Yašts of hostile, non-Mazdayasnian rulers ('naidā dahyə̄uš yōi sāstārō drəgvantō \\\"nor the unbelieving rulers of the land\\\", Y.46.1'), which is why Nourai glosses it 'ruler, oppressor'. Av. sāx°an- n. 'Lehre' and sāsnā- f. 'Lehre, Gebot' (AiW cols. 1575-76, both explicitly 'zum V. sāh-') are the -van- and -nā- abstracts. The sixth item, paiti-sahva, does NOT belong here: the Avestan compound is paiti.saŋh- (YAv. paiti.saŋhāmi V.20.7, med. paiti.saŋhaēša Yt.14.35), built on the separate root sah- / Old Persian θah- 'pronuntiare, to declare' which Bartholomae puts at AiW col. 1578 and which Cheung (p.334, *sanh) and LIV derive from PIE *ḱens- (Pokorny 566) — Nourai's own alternative root 'Kens'. Nothing on Pokorny 533 licenses it. Note also that the 'Old Persian' half of the label fits only the *ḱens- word (OP θah-, θātiy 'says'), not the *ḱeh₂s- words, which are Avestan only.\",\n    \"derivation_fa\": \"پنج صورت از شش صورتِ این خانه همان چیزی است که پوکورنی در ص ۵۳۳ آورده و تأیید می‌شود: ستاک اوستایی sāh- (زمان حالِ sāsti «می‌آموزد، فرمان می‌دهد») دنبالهٔ ایرانیِ *ḱeh₂s- و هم‌ریشهٔ سنسکریت śās- است و صورتِ sās همان ستاکِ حالِ آن است؛ صفتِ مفعولیِ sāsta- «آموخته» با پسوند -ta- و نامِ فاعلِ sāstar- «فرمانروا، سرور» با پسوند -tar- ساخته شده‌اند. بارتولمه در ستون ۱۵۷۴ ـ همان صفحه‌ای که نورایی ارجاع داده ـ sāstar- را «فرمانروا، زورمند، شهریار» معنی کرده و می‌افزاید که در گاهان و یشت‌ها بیشتر دربارهٔ فرمانروایانِ بددینْ به کار می‌رود، و همین است که نورایی آن را «ستمگر» ترجمه کرده. sāx°an- «آموزه» و sāsnā- «آموزه، فرمان» نیز در ستون‌های ۱۵۷۵ـ۱۵۷۶ صریحاً «از ستاکِ sāh-» خوانده شده‌اند. اما paiti-sahva از این ریشه نیست: ترکیبِ اوستایی paiti.saŋh- است که بر ستاکِ جداگانهٔ sah- / پارسی باستانِ θah- «گفتن، اعلام کردن» ساخته شده؛ بارتولمه آن را در ستون ۱۵۷۸ جدا آورده و چونگ (ص ۳۳۴، *sanh) و LIV آن را از *ḱens- (پوکورنی ۵۶۶) می‌دانند ـ یعنی همان ریشه‌ای که خودِ نورایی زیر نام «Kens» به آن اشاره کرده است. افزون بر این، برچسبِ «پارسی باستان» تنها با همین واژهٔ *ḱens- (یعنی θah-) می‌خواند، نه با واژه‌های *ḱeh₂s- که تنها اوستایی‌اند.\",\n    \"sources\": [W + \"Reconstruction:Proto-Iranian/c%C3%A1nhati\"],\n    \"ref_check\": [\n      {\"ref\": \"POK:533\", \"status\": \"supports\", \"note\": \"quoted at the entry level: 'av. sāsti \\\\'heißt, lehrt\\\\' ... = av. sästar- \\\\'Gebieter, Fürst\\\\' ... av. säx°an- n. \\\\'Lehre\\\\', säsnä \\\\'Lehre, Gebot\\\\''. Pokorny does NOT list paiti-sah- here.\"},\n      {\"ref\": \"BRT:1574\", \"status\": \"supports\", \"note\": \"BRT.txt line 26236, between the OCRed column numbers 1571 (line 26182) and 1577 (line 26277), i.e. col. 1573-1575: 'j., g. sästar- m. \\\\'Gebieter, Machthaber, Fürst\\\\' ... a) bes. von Feinden des mazdayasnischen Glaubens ... Zum V. sāh- ... mp. sāstār'. The same opening also carries the running head 'sāh-' at col. 1574. sāsnā- ('j., g. säsnä- f. \\\\'Lehre; Gebot\\\\' ... Zum V. sāh-') and sāx°an- ('g. sāx°an- n. \\\\'Lehre\\\\' ... Zum V. sāh-') follow at cols. 1575-76.\"},\n      {\"ref\": \"SYN:1338\", \"status\": \"supports\", \"note\": \"SYN.txt leaf 1432 (§19.45, just before the running head 1339): 'Skt. ças- ... = Av. sah- \\\\'command\\\\' (cf. sāstar- \\\\'ruler\\\\'), esp. \\\\'teach\\\\' : Arm. sastem ... Walde-P. 1.358.' Buck's page number matches Nourai's SYN:1338 exactly.\"},\n      {\"ref\": \"BQT:354\", \"status\": \"partial\", \"note\": \"Borhan-e Qāṭeʿ vol.1, leaf 576 of BQT_v1_pages.txt = printed p.354 (printed ≈ leaf − 222): the page does carry the headword پاسخ ('... در مقابل سؤال است') between پاسبان and پاسره, so the citation points to the right page; but the OCR of Mo'in's footnotes on that page is too damaged to read his etymology, and in any case Borhan is a Persian dictionary and says nothing about an Avestan/Old Persian stage.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW cols. 1573-1578\", \"stance\": \"partial\", \"note\": \"supports sāstar-, sāsnā-, sāx°an- under sāh-, but keeps 'j., g. sah-, p. θah- V. \\\\'pronuntiare\\\\'' as a separate lemma at col. 1578 — the root of paiti.saŋh-, i.e. Bartholomae himself separates Nourai's last item from the rest.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p.334 s.v. *sanh 'to declare, explain'\", \"stance\": \"contradicts\", \"note\": \"'*AVESTAN: saŋh- (saŋh-) ... (+ *pati-) \\\\'to call up, invoke\\\\' ... med. 2sg. YAv. paiti.saŋhaēša (Yt 14.35) ... *OLD PERSIAN: θaⁿh- \\\\'to declare, say\\\\' ... «PIE *ḱens- \\\\'to announce, proclaim\\\\' ... Pok.: 566». The paiti- compound is assigned to *ḱens-, not to Pokorny 533.\"},\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. θah-\", \"stance\": \"partial\", \"note\": \"Old Persian has θātiy 'says', θahyāmahy, θastanaiy (Cheung: 'Kent: 188a'); there is no OP reflex of sāh- 'instruct'. So of Nourai's 'Avestan / Old Persian' label only the paiti-sahva item has an OP counterpart — and that one belongs to the other root.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck §19.45 p.1338\", \"stance\": \"supports\", \"note\": \"as quoted; Buck links Av. sāh- 'command' and sāstar- 'ruler' with Skt śās- and Arm. sastem, i.e. exactly Nourai's word-set minus paiti-sahva.\"}\n    ]\n   },\n   {\n    \"id\": 2, \"lang\": \"Pahlavi\",\n    \"words\": \"sâstâr; sâstâreh; soxvan; passaxv, pasux\",\n    \"verdict\": \"disputed\",\n    \"derivation\": \"Two of the four items are right and two are misfiled. MP sāstār 'commander, tyrant' (Book Pahlavi <s'st'r>) is the direct continuant of Av. sāstar- and is listed by both MacKenzie ('sāstār [s\\\"st\\\"l | P sāsār] commander; tyrant. ~ih: tyranny') and Nyberg, who adds the AiW column number: 'sāstar ... ruler, tyrant, of infidel (non-mazdayasnian) sovereigns ... In this sense probably borrowed from Av. (1573) sāstar-; M Prth s'st'r \\\"master, lord\\\"'. Nourai's second word sāstāreh is Nyberg's 'sāstārēh bad domination, tyranny' verbatim (= MacKenzie's sāstārīh), the abstract in -īh/-ēh; Nourai has simply copied Nyberg's Pazand-style spelling. The other two are from a different root: MP saxwan 'word, speech' (Manichaean <sxwn>, Book Pahlavi <shwn'>) and passox / pāsox 'answer' (Manichaean <pswx>, BP <pshw'>, <p'shw'>) both go back, per Cheung (p.334), Hübschmann (Persische Studien p.126, p.191, p.210) and Wiktionary, to Proto-Iranian *cánhati / *cánhuš and *pati-cahwaH, i.e. PIE *ḱens-, not to *ḱeh₂s-; the short a of saxwan and the Parthian doublets sxwn / pswx show the *sanh- stem, whereas *ḱeh₂s- would predict a long ā as in sāstār. Note also that Nourai's 'soxvan' is a hybrid spelling: the Pahlavi form is saxwan (the o first appears in New Persian).\",\n    \"derivation_fa\": \"از چهار واژهٔ این خانه دو تا درست و دو تا نابه‌جا است. sāstārِ فارسی میانه «فرمانروا، ستمگر» (به خط پهلوی <s'st'r>) دنبالهٔ مستقیم sāstar-ِ اوستایی است؛ مکنزی آن را «فرمانده؛ ستمگر» و nyberg (نیبرگ) آن را «فرمانروا، ستمگر، دربارهٔ شهریارانِ بی‌دین» معنی کرده و می‌افزاید «در این معنا احتمالاً وام‌گرفته از اوستایی (۱۵۷۳) sāstar-». واژهٔ دومِ نورایی یعنی sāstāreh نیز عیناً همان «sāstārēh: چیرگیِ بد، ستمگری» است که نیبرگ آورده (= sāstārīhِ مکنزی)، اسمِ معنا با پسوندِ -īh/-ēh. اما دو واژهٔ دیگر از ریشهٔ دیگری‌اند: saxwan «سخن، گفتار» و passox/pāsox «پاسخ» ـ بنا بر چونگ (ص ۳۳۴)، هوبشمان (پژوهش‌های ایرانی، صص ۱۲۶، ۱۹۱، ۲۱۰) و ویکی‌واژه ـ از ایرانی آغازینِ *cánhuš و *pati-cahwaH، یعنی از *ḱens- می‌آیند نه از *ḱeh₂s-. کوتاهیِ aِ saxwan و صورت‌های پارتیِ sxwn و pswx نیز همین را نشان می‌دهد، حال آنکه *ḱeh₂s- باید āِ بلند بدهد، چنان‌که در sāstār. افزون بر این، صورتِ «soxvan» که نورایی نوشته آمیخته است؛ صورتِ پهلوی saxwan است و oِ آن تازه در فارسی نو پدید می‌آید.\",\n    \"sources\": [W + \"%D8%B3%D8%AE%D9%86\", W + \"%D9%BE%D8%A7%D8%B3%D8%AE\"],\n    \"ref_check\": [\n      {\"ref\": \"BQT:354\", \"status\": \"partial\", \"note\": \"as above: printed p.354 of Borhan (BQT_v1_pages.txt leaf 576) carries the headword پاسخ, but Borhan gives Persian usage, not a Pahlavi etymology, and the footnote OCR on that leaf is unreadable.\"},\n      {\"ref\": \"BQT:1573\", \"status\": \"not_found\", \"note\": \"checked: BQT vol.3, pdf page 366 of BQT_v3_picofile.pdf carries the running head ۱۵۷۳ and contains the entries کاکاو، کاکیان، کاکره، کاکل، کاکو — nothing to do with sāstār, soxvan or pāsox. The relevant Borhan pages for this material are 1072 (ساستا) and 1107 (سخن) in vol.2; '1573' looks like a slip of the pen or a typo for 1073.\"},\n      {\"ref\": \"MON:1843\", \"status\": \"not_checked\", \"note\": \"Mo'in's 6-volume Farhang-e Farsi is on disk only as the 2-volume Adena abridgement (MON_part1/part2.txt), which has no page breaks and a different pagination; refs_online.json states outright that MON page numbers cannot be mapped. The substance of the claim (MP sāstār, saxwan, passox) is confirmed instead from MacKenzie and Nyberg.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie pp.73, 65 (s.vv. sāstār, saxwan, passox, pasox)\", \"stance\": \"partial\", \"note\": \"'sāstār [s\\\"st\\\"l | P sāsār] commander; tyrant. ~ih: tyranny' (PHD.txt:564); 'saxwan [MRYA < A mly\\\\'; shwn\\\\' | M sxwn, N suxan] word, speech' (PHD.txt:564); 'passox [pshw\\\\' | M pswx, N pāsux] answer' and 'pasox [p\\\\'shw\\\\' | N ~] = passox' (PHD.txt:545). All four Pahlavi forms exist as Nourai gives them (with saxwan, not soxvan), but MacKenzie's Manichaean equivalents sxwn / pswx already point away from a long-ā root.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.vv. sāstar, sāstārēh\", \"stance\": \"supports\", \"note\": \"NYB_vol2_glossary.txt:3407-3408: 'sāstar [s\\\\'st\\\\'l] ruler, tyrant, of infidel (non-mazdayasnian) sovereigns, pl. cas. obl. ~-ān 614. — In this sense probably borrowed from Av. (1573) sāstar-; M Prth s\\\\'st\\\\'r \\\\'master, lord\\\\' (A-H III, BBB).' / 'sāstārēh bad domination, tyranny 109.' Nourai's 'sâstâreh : bad domination' is Nyberg's gloss word for word.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p.334 s.v. *sanh, section *MIDDLE PERSIAN\", \"stance\": \"contradicts\", \"note\": \"'MMP sxwn, BMP shwn (MRY?) /saxwan/ \\\\'word, speech\\\\' || (+ *pati-) MMP pswx, BMP pshw /passox/, p\\\\'shw /pasox/ \\\\'answer\\\\'' — assigned to *sanh < PIE *ḱens-, Pokorny 566.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien pp.126 and 191\", \"stance\": \"contradicts\", \"note\": \"p.126: 'ausl. -ux aus -axv: pasux \\\\'Antwort\\\\' = phl. pasaxv ...; suxun = suxan \\\\'Wort\\\\', paz. saxun aus sax°ar-'; p.191: 'np. paz. pasux \\\\'Antwort\\\\' aus *pātsaxv (neben phl. pasaxv aus *patsaxv), vgl. arm. patasxani \\\\'Antwort\\\\' ... Diese Assimilirung war erst sassanidisch, wie das Armenische zeigt.' Hübschmann confirms the Pahlavi forms but attaches them to the 'speak' root.\"}\n    ]\n   },\n   {\n    \"id\": 3, \"lang\": \"Persian\",\n    \"words\": \"sâstâ «ساستا»; soxan «سخن»; pâsox «پاسخ» (also ساستار)\",\n    \"verdict\": \"disputed\",\n    \"derivation\": \"sāstā / sāstār «ساستا، ساستار» is correct: Borhan-e Qāṭeʿ (vol.2, printed p.1072, leaf 534 of BQT_v2_pages.txt) has 'ساستا — بر وزن پارسا: نام دیوی است از تابعان اهرمن' (\\\"the name of a demon among Ahriman's followers\\\"), the lexicographers' Persian survival of Pahlavi sāstār 'tyrant' with the final -r lost, and the doublet ساستار is Nourai's script_extra. That word does descend from Kâs 2. The other two do not. سخن soxan continues MP saxwan (loss of intervocalic w with rounding of the preceding vowel: saxwan > saxwun > soxan; Classical Persian also has suxun, and the Shahnameh rhymes both), and پاسخ pāsox continues MP passox / pāsox < *pati-saxwa-, with the Sassanian assimilation *pat-s- > pass- that Hübschmann dates by the Armenian loan patasxani. Both belong to Proto-Iranian *cánhati 'to declare' < PIE *ḱens- (Cheung p.334; Wiktionary s.vv. سخن and پاسخ; Hübschmann pp.126, 191, 210 'suxun, suxan \\\"Wort\\\" aus iran. *saxvan- = ap. *θa(h)uvan- von θah \\\"sprechen\\\", skr. śaṃs-, zd. saŋh-'). Nourai's own NOTE offers 'Kens' as an alternative root for soxan — that alternative is the one modern scholarship takes, and it applies to pāsox too; his second alternative, 'Wegwh' (PIE *wekʷ- 'to speak'), is not held by anyone for pāsox. The only living defence of Nourai's arrow is Horn, who on the page Nourai cites (HRN:160) derives suxun from Av. sax°arə / sāx°ənī 'Plan, Rat, Rede' following Bartholomae — but Bartholomae's sāx°an- (long ā) cannot give a short a in Pahlavi saxwan, which is why the modern handbooks abandoned it.\",\n    \"derivation_fa\": \"«ساستا/ساستار» درست است: برهان قاطع (ج۲، ص ۱۰۷۲) می‌نویسد «ساستا ـ بر وزن پارسا: نام دیوی است از تابعان اهرمن»، و این همان بازماندهٔ فارسیِ sāstārِ پهلوی «ستمگر» است با افتادنِ rِ پایانی؛ صورتِ «ساستار» را هم نورایی در کنارش آورده. این واژه به‌راستی از ریشهٔ Kâs 2 است. اما دو واژهٔ دیگر چنین نیستند. «سخن» دنبالهٔ saxwanِ پهلوی است (wِ میان‌واکه‌ای افتاده و واکهٔ پیشین گِرد شده: saxwan > soxan؛ در فارسی کلاسیک صورت‌های سخُن و سُخُن نیز هست) و «پاسخ» دنبالهٔ passox/pāsoxِ پهلوی از *pati-saxwa- است، با همگونیِ *pat-s- > pass- که هوبشمان آن را به دورهٔ ساسانی می‌رساند و از وام‌واژهٔ ارمنیِ patasxani تاریخ‌گذاری می‌کند. هر دو از ایرانی آغازینِ *cánhati «اعلام کردن» از *ḱens- می‌آیند (چونگ ص ۳۳۴؛ ویکی‌واژه ذیل «سخن» و «پاسخ»؛ هوبشمان صص ۱۲۶، ۱۹۱، ۲۱۰: «suxun، suxan \\\"سخن\\\" از ایرانیِ *saxvan- برابر پارسی باستانِ *θa(h)uvan- از ستاکِ θah \\\"گفتن\\\"»). خودِ نورایی در یادداشتِ نمودار «Kens» را ریشهٔ دیگرِ ممکن برای «سخن» دانسته است؛ پژوهش امروزی همان را می‌پذیرد و آن را به «پاسخ» نیز تعمیم می‌دهد. اما گزینهٔ دومِ او، «Wegwh» (یعنی *wekʷ-)، برای «پاسخ» هیچ پشتیبانی ندارد. تنها تکیه‌گاهِ نمودار، هرن است که در همان ص ۱۶۰ «سخن» را از اوستاییِ sax°arə/sāx°ənī به پیروی از بارتولمه می‌گیرد؛ ولی āِ بلندِ sāx°an- نمی‌تواند aِ کوتاهِ saxwanِ پهلوی را بدهد و به همین سبب فرهنگ‌های امروزی از آن دست کشیده‌اند.\",\n    \"sources\": [W + \"%D8%B3%D8%AE%D9%86\", W + \"%D9%BE%D8%A7%D8%B3%D8%AE\", W + \"Reconstruction:Proto-Iranian/c%C3%A1nhati\"],\n    \"ref_check\": [\n      {\"ref\": \"BQT:1072\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 534 (printed page ≈ leaf + 538, i.e. 1072; the surrounding headwords are ساسان، ساسر، ساسم, which fits the alphabetical place): 'ساستا = ۴ ... بر وزن پارسا ... نام دیوی است از تابعان اهرمن'. Exactly Nourai's gloss 'oppressor, demon'.\"},\n      {\"ref\": \"BQT:1107\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 569-570 (printed ≈ 1106-1107): the سخن article, with the footnote (partly legible in the OCR) 'سخون (م). پهلوی saxvan ... (لفظ، عبارت) از اوستا ... «بارتولمه ...»' and, next to it, 'قس: پاسخ (پهلوی pasaxv)'. Borhan/Mo'in thus give the MP > NP step Nourai draws (but derive it from Avestan sax°an-, i.e. Bartholomae's assignment, not from a chain through sāstār).\"},\n      {\"ref\": \"BQT:354\", \"status\": \"partial\", \"note\": \"printed p.354, vol.1 (leaf 576): headword پاسخ present, glossed as the counterpart of سؤال; no etymology legible in this OCR.\"},\n      {\"ref\": \"HRN:160\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 181 = printed p.160, entry no. 724: 'suxun, suxn (Sahn. I,29 V.117 neben -uwn, ebendas. V.109) \\\\'Wort, Rede\\\\'. Kās. K. suxan[ōni]. aw. sax°arə (Y.29,4), sāx°ənī (Y.53,5) \\\\'Plan, Rat, Rede\\\\' (Bartholomae, Ar. Forsch. III,36,37); phlv. saxwn \\\\'Wort, Rede\\\\'.' Horn's page supports Nourai's chain — but Horn (1893) predates the modern assignment of the word to *ḱens-.\"},\n      {\"ref\": \"MON:1796\", \"status\": \"not_checked\", \"note\": \"the 6-volume Mo'in is not available with mappable pagination (only the 2-volume Adena abridgement without page breaks); see the note on MON:1843.\"},\n      {\"ref\": \"FSF:99\", \"status\": \"not_found\", \"note\": \"Noushin's Vāzhe-namak (FSF_pages.txt, 485 leaves; printed page = leaf − 3, checked against the running numerals 108 at leaf 111, 113 at leaf 116, 130 at leaf 123): leaf 102 = printed p.99 is in the ب section (برگی، برفزود), and a grep of the whole file for ساستا/ساستار returns nothing. Either Nourai used a different printing or the number is wrong.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"HUB\", \"where\": \"Persische Studien pp.126, 191, 210\", \"stance\": \"contradicts\", \"note\": \"p.210: 'suxun, suxan \\\\'Wort\\\\' aus iran. *saxvan- = ap. *θa(h)uvan- von θah \\\\'sprechen\\\\', skr. śaṃs-, zd. saŋh-'; p.191: 'np. paz. pasux \\\\'Antwort\\\\' aus *pātsaxv ... vgl. arm. patasxani'. Hübschmann assigns both New Persian words to the 'speak' root, not to sāh- 'instruct'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p.334 s.v. *sanh, section *NWIR\", \"stance\": \"contradicts\", \"note\": \"'NP suxan, saxun \\\\'word, speech\\\\' || (+ *pati-) NP pāsux, Bal. pas(s)aw \\\\'answer\\\\'' under *sanh < PIE *ḱens-, Pok. 566.\"},\n      {\"src\": \"HRN\", \"where\": \"p.160 no. 724\", \"stance\": \"supports\", \"note\": \"Horn keeps suxan with Avestan sax°arə/sāx°ənī after Bartholomae — the minority position Nourai follows.\"},\n      {\"src\": \"BQT\", \"where\": \"vol.2 pp.1072 and 1106-1107\", \"stance\": \"partial\", \"note\": \"supports ساستا 'demon, follower of Ahriman' and the saxwan > سخن step; silent on sāstār as the source of soxan.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. saxwan, passox\", \"stance\": \"partial\", \"note\": \"gives the immediate Middle Persian ancestors of سخن and پاسخ, with Manichaean sxwn / pswx.\"}\n    ]\n   }\n  ]\n },\n\n # ---------------- entry 3 : Kasyapa ----------------\n {\n  \"entry\": 3,\n  \"root\": \"Kasyapa\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"Younger Avestan kasiiapa- m. 'tortoise' < Proto-Iranian *kacyápah < Proto-Indo-Iranian *kaćyápas (Skt kaśyápa- / kacchapa- 'tortoise')\",\n  \"note\": \"Bartholomae AiW (col. ~460, BRT.txt line 9423) has 'j. kasyapa- m. \\\\'Schildkröte\\\\'', and Mo'in's footnote 2 to کشف in Borhan-e Qāṭeʿ p.1651 gives exactly Nourai's comparison: 'اوستا - kasyapa (سنگ‌پشت) یا (خرچنگ)؛ سانسکریت - kaçyapa (سنگ‌پشت)، بلوچی kasib «استق ۱۹۰»، افغانی kshap؛ هوبشمان'. Nourai's root note 'cognate with Sanskrit kačyâpa' is Mo'in's kaçyapa = Skt kaśyápa-; modern Wiktionary reconstructs Proto-Iranian *kacyápah and prefers the by-form कच्छप kacchapa- on the Indic side, but the equation itself is uncontroversial. The gloss and the language label are both correct.\",\n  \"note_fa\": \"بارتولمه در فرهنگ ایرانی باستان (نزدیکِ ستون ۴۶۰) «kasyapa- نرینه: سنگ‌پشت» را آورده و معین در حاشیهٔ ۲ بر مدخلِ «کشف» در برهان قاطع (ص ۱۶۵۱) دقیقاً همان مقایسه‌ای را می‌کند که نورایی کرده است: «اوستا ـ kasyapa (سنگ‌پشت) یا (خرچنگ)؛ سانسکریت ـ kaçyapa (سنگ‌پشت)، بلوچی kasib، افغانی kshap؛ هوبشمان». یادداشتِ نورایی که واژه را هم‌ریشهٔ سنسکریتِ kačyâpa می‌داند همان kaçyapaِ معین است. ویکی‌واژه ایرانی آغازین را *kacyápah بازسازی می‌کند و در سوی هندی صورتِ कच्छप kacchapa- را ترجیح می‌دهد، ولی در اصلِ این هم‌ریشگی اختلافی نیست. برچسبِ زبانی و معنا هر دو درست است.\",\n  \"sources\": [W + \"%DA%A9%D8%B4%D9%81\", W + \"Reconstruction:Proto-Iranian/kacy%C3%A1pah\"],\n  \"ref_check\": [\n    {\"ref\": \"SOD:204\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary: SOD_pages.txt leaf 270 = printed p.204 (printed ≈ leaf − 66), entry no. 5125: 'kyšph B ... kis(a)p ©<Av. kasyapa ... tortoise. SCE 157, 353; GMS 192'. Gharib herself derives the Sogdian word from Avestan kasyapa, exactly Nourai's root box.\"},\n    {\"ref\": \"BQT:1651\", \"status\": \"supports\", \"note\": \"Borhan-e Qāṭeʿ vol.3, pdf p.444 = printed p.1651 (running head ۱۶۵۱ visible on the page): the headword 'کشف — بفتح اول و ثانی و سکون فا: لاک‌پشت و کاسه‌پشت را گویند' with footnote 2 'اوستا - kasyapa (سنگ‌پشت) یا (خرچنگ)؛ سانسکریت - kaçyapa (سنگ‌پشت)، بلوچی kasib «استق ۱۹۰»، افغانی kshap؛ هوبشمان'.\"},\n    {\"ref\": \"MON:2987\", \"status\": \"not_checked\", \"note\": \"Mo'in's 6-volume Farhang is available only as the 2-volume Adena abridgement without page breaks, and refs_online.json notes that MON page numbers cannot be mapped; the same author's etymological footnote in Borhan p.1651 (checked above) carries the identical claim.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AiW col. ~460 (BRT.txt line 9423)\", \"stance\": \"supports\", \"note\": \"'j. kasyapa- m. \\\\'Schildkröte\\\\', die als ...' — the Avestan word exists with exactly this meaning, on the same opening as karšvar- (cols. 457-463).\"},\n    {\"src\": \"HRN\", \"where\": \"p.191 no. 856\", \"stance\": \"supports\", \"note\": \"'856. kešef \\\\'Schildkröte; Krebs\\\\' (Zodiac, Sahn. I,77 Vers 285), keseb (dial.). aw. kasyapa- \\\\'Schildkröte\\\\' oder \\\\'Krebs\\\\' (Geldner, KZ.25,503,506); skr. (Brhm.) kaçyápa- \\\\'Schildkröte\\\\'; afgh. kasy \\\\'Schildkröte\\\\'; bel. kāsib.'\"},\n    {\"src\": \"SOD\", \"where\": \"Gharib no. 5125, p.204\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien §71 (p.178) and §80 (p.185)\", \"stance\": \"supports\", \"note\": \"p.178: 'Für b, v aus p erscheint unregelmässig f in kasaf \\\\'Schildkröte\\\\' neben kašav (bei Vullers) = zd. kasyapa-, afgh. kasap'; p.185: 'Vgl. auch kasaf \\\\'Schildkröte\\\\' = zd. kasyapa- (§71).'\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1, \"lang\": \"Persian\", \"words\": \"kašaf «کَشَف»\", \"verdict\": \"confirmed\",\n    \"derivation\": \"Avestan kasiiapa- yields New Persian کَشَف kašaf: the intervocalic -p- of Old Iranian is regularly voiced and spirantised to -b/-v- in Middle Persian (Wiktionary reconstructs the Book Pahlavi form as <kšwk'> /kašawag/ with the productive -ag suffix), and the New Persian word shows an irregular f for the expected b/v — precisely the point Hübschmann makes in Persische Studien §71: 'für b, v aus p erscheint unregelmässig f in kasaf \\\"Schildkröte\\\" neben kašav (bei Vullers) = zd. kasyapa-, afgh. kasap'. The Avestan -sii- (-sy-) becomes MP/NP -š-. The word is archaic in modern Persian (replaced by لاک‌پشت), but it is well attested in the tenth century: Nourai's citation from Rudaki, 'چون کَشَف انبوه غوغایی بدید — بانگ وژخ مردمان، خشم آورید', is the same verse Borhan-e Qāṭeʿ prints on p.1651 (Borhan has خشم آورید where Nourai prints خشم آفرید). It also survives as the river-name کَشَف‌رود north of Mashhad, which Mo'in notes in footnote 9 on the same page.\",\n    \"derivation_fa\": \"«کَشَف» فارسی نو از اوستاییِ kasiiapa- می‌آید: pِ میانِ دو واکه در ایرانی میانه به b/v نرم می‌شود (ویکی‌واژه صورتِ پهلوی را <kšwk'> یعنی kašawag با پسوندِ -ag بازسازی می‌کند) و -sii-ِ اوستایی به šِ فارسی بدل می‌شود؛ آنچه بی‌قاعده است fِ پایانی به‌جای bِ چشم‌داشتی است و هوبشمان در بند ۷۱ «پژوهش‌های ایرانی» صریحاً همین را می‌گوید: «به‌جای b و vِ برآمده از p، به‌گونهٔ بی‌قاعده f می‌آید، در kasaf \\\"سنگ‌پشت\\\" در کنار kašav (نزد ولرس) برابر اوستاییِ kasyapa-، افغانیِ kasap». این واژه امروز کهنه است و جای خود را به «لاک‌پشت» داده، ولی در سدهٔ چهارم زنده بوده؛ بیتِ رودکی که نورایی آورده («چون کَشَف انبوه غوغایی بدید ـ بانگ وژخ مردمان، خشم آورید») همان است که برهان قاطع در ص ۱۶۵۱ نقل کرده. نامِ رودِ «کَشَف‌رود» در شمالِ مشهد نیز از همین واژه است (حاشیهٔ ۹ همان صفحه). ادعای نورایی درست است.\",\n    \"sources\": [W + \"%DA%A9%D8%B4%D9%81\", W + \"Reconstruction:Proto-Iranian/kacy%C3%A1pah\"],\n    \"ref_check\": [\n      {\"ref\": \"BQT:1651\", \"status\": \"supports\", \"note\": \"printed p.1651 of Borhan (vol.3 pdf p.444): the headword کشف 'لاک‌پشت و کاسه‌پشت' with the Rudaki verse and footnote 2 deriving it from Avestan kasyapa / Sanskrit kaçyapa; footnote 9 identifies کشف‌رود, 'یکی از شعب هریرود که سرچشمهٔ آن ... در کوههای ... و پس از مشروب کردن رادکان و چناران از شمال مشهد گذشته ...'.\"},\n      {\"ref\": \"HRN:191\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 212 = printed p.191, entry no. 856: 'kešef \\\\'Schildkröte; Krebs\\\\' ... aw. kasyapa- \\\\'Schildkröte\\\\' ... skr. (Brhm.) kaçyápa-'. Horn's page is the same one that carries kišver (no. 858) — Nourai's HRN:191 does double duty for both roots on this book page.\"},\n      {\"ref\": \"MON:2987\", \"status\": \"not_checked\", \"note\": \"6-volume Mo'in not page-mappable; see the root-level note. Mo'in's own etymological footnote in Borhan p.1651 carries the identical derivation.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"HUB\", \"where\": \"Persische Studien §71 p.178, §80 p.185\", \"stance\": \"supports\", \"note\": \"quoted above — Hübschmann treats np. kasaf = zd. kasyapa- as established and only discusses the irregular f.\"},\n      {\"src\": \"HRN\", \"where\": \"p.191 no. 856\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n      {\"src\": \"BQT\", \"where\": \"vol.3 p.1651 with Mo'in's footnote 2\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/کشف (Etymology 2) and Reconstruction:Proto-Iranian/kacyápah\", \"stance\": \"supports\", \"note\": \"'From Middle Persian [Book Pahlavi needed] (kšwk\\\\' /kašawag/, \\\\'tortoise\\\\'), from Proto-Iranian *kacyápah'; the reconstruction page lists 'Avestan kasiiapa', 'Middle Persian kšwk /kašawag/, Classical Persian kašaf', 'Sogdian kyšph /kiš(a)p/', 'Khotanese khuysaa', 'Ossetian xæfs'.\"}\n    ]\n   },\n   {\n    \"id\": 2, \"lang\": \"Sogdian\", \"words\": \"kyšf\", \"verdict\": \"confirmed\",\n    \"derivation\": \"Sogdian <kyšph>, read kiš(a)p, 'tortoise' is the Sogdian cognate of Avestan kasiiapa-, not a descendant of it: Sogdian is an independent (North-)Eastern Iranian branch, so both continue Proto-Iranian *kacyápah. Gharib's Sogdian-Persian-English Dictionary no. 5125 (p.204) prints '5125 kyšph B — kis(a)p ©<Av. kasyapa — tortoise', i.e. she marks the word with the same '< Avestan' shorthand Nourai's arrow uses. The form is attested in the Buddhist Sogdian script (B), in the Sūtra of the Causes and Effects (SCE 157, 353); the digraph <ph> writes the fricative f/β, so Nourai's 'kyšf' and Gharib's 'kyšph' are the same word — the difference is one of transliteration convention, not of form. Phonologically the Sogdian shows the same *-sy- > -š- and *-p- > -f/β developments as Persian, with loss of the final syllable.\",\n    \"derivation_fa\": \"صورتِ سغدیِ <kyšph> که kiš(a)p خوانده می‌شود، هم‌ریشهٔ kasiiapa-ِ اوستایی است نه برآمده از آن؛ سغدی شاخهٔ جداگانه‌ای از ایرانیِ شرقی است و هر دو صورت از ایرانی آغازینِ *kacyápah می‌آیند. قریب در فرهنگ سغدی (شمارهٔ ۵۱۲۵، ص ۲۰۴) می‌نویسد «kyšph ب ... kis(a)p ©< اوستایی kasyapa ... سنگ‌پشت»، یعنی خودِ او همان پیکانِ نورایی را می‌کشد. واژه در متونِ سغدیِ بودایی (SCE ۱۵۷ و ۳۵۳) گواهی شده است. دو نویسهٔ <ph> در املای سغدی همان سایشیِ f/β را می‌نویسد، پس «kyšf»ِ نورایی و «kyšph»ِ قریب یک واژه‌اند و اختلاف تنها در شیوهٔ آوانویسی است. از نظر آوایی همان دگرگونی‌های *-sy- > -š- و *-p- > -f/β که در فارسی هست در سغدی نیز دیده می‌شود، با افتادنِ هجای پایانی.\",\n    \"sources\": [W + \"Reconstruction:Proto-Iranian/kacy%C3%A1pah\"],\n    \"ref_check\": [\n      {\"ref\": \"SOD:204\", \"status\": \"supports\", \"note\": \"SOD_pages.txt leaf 270 = printed p.204 (printed ≈ leaf − 66; SOD.txt lines 41575-41580): '5125 kyšph B — kis(a)p ©<Av. kasyapa — tortoise — SCE 157, 353; GMS 192'. The English index of the same dictionary lists 'tortoise 5125'. Nourai's page number is exact.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"SOD\", \"where\": \"Gharib no. 5125, p.204\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Iranian/kacyápah\", \"stance\": \"supports\", \"note\": \"lists 'Sogdian kyšph (/kiš(a)p/)' among the descendants alongside Avestan kasiiapa and Middle Persian kašawag, i.e. sister forms rather than a Sogdian borrowing from Avestan.\"},\n      {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Khotanese (via Gharib's cross-references DKS 418b, 224b)\", \"stance\": \"partial\", \"note\": \"Wiktionary's reconstruction page gives Khotanese khuysaa for the same etymon, which corroborates the Eastern Iranian side of the equation; no direct entry was located in the local ISS_alt_DKS.txt.\"}\n    ]\n   }\n  ]\n },\n\n # ---------------- entry 4 : Kâtara ----------------\n {\n  \"entry\": 4,\n  \"root\": \"Kâtara\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"Sanskrit कातर kātara- adj. 'cowardly, faint-hearted, timid; perplexed, confused'\",\n  \"note\": \"The Sanskrit word is real and Nourai's gloss is close but not exact: Monier-Williams and Wiktionary give 'cowardly, faint-hearted, timid; confused, perplexed' (and as a neuter noun 'despair'); 'wandering' is not a Sanskrit sense but the Persian one (سرگشته). Mo'in's footnote in Borhan p.1555 renders it 'ترسو، کم‌رو، گیج، مضطرب' = 'timid, shy, dizzy, agitated', which is what Nourai has translated. Wiktionary's etymology for kātara is itself uncertain — either a vṛddhi derivative of katará- 'which of two?' or a Middle-Indic/substrate word (cf. Prakrit kattara) — so the Sanskrit end of the chart is not a securely inherited Indo-Aryan form either. The chart's own NOTE ('Persian words may be cognates with rather than derivatives from Sanskrit') is the right caution and, given that the word has no Iranian cognate and Mo'in only writes قس 'compare', neither a loan nor a cognate relation can be demonstrated.\",\n  \"note_fa\": \"واژهٔ سنسکریتِ कातर kātara- واقعی است و معنای آن در مونیر ویلیامز و ویکی‌واژه «ترسو، بزدل، کم‌دل؛ سرگشته، آشفته» (و در حالتِ اسم خنثی «نومیدی») است؛ معنای «سرگردان» که نورایی افزوده معنای فارسی است نه سنسکریت. معین در حاشیهٔ ص ۱۵۵۵ برهان قاطع آن را «ترسو، کم‌رو، گیج، مضطرب» ترجمه کرده و نورایی همین را به انگلیسی برگردانده است. خودِ ریشه‌شناسیِ kātara در سنسکریت روشن نیست: یا مشتقِ وریدّهی از katará- «کدام‌یک از دو» است یا واژه‌ای از لایهٔ زیرین/میانه‌هندی (قس پراکریتِ kattara)، پس سرِ سنسکریتیِ نمودار هم استوار نیست. یادداشتِ خودِ نمودار («شاید واژه‌های فارسی هم‌ریشه باشند نه برگرفته از سنسکریت») احتیاطِ بجایی است: معین تنها «قس» (= مقایسه کنید) نوشته، نه اینکه واژه را وام‌واژه بداند، و چون این واژه در هیچ زبان ایرانیِ دیگری هم‌ریشه ندارد، نه وام‌گیری اثبات‌شدنی است و نه هم‌ریشگی.\",\n  \"sources\": [W + \"%E0%A4%95%E0%A4%BE%E0%A4%A4%E0%A4%B0\"],\n  \"ref_check\": [\n    {\"ref\": \"BQT:1555\", \"status\": \"partial\", \"note\": \"Borhan-e Qāṭeʿ vol.3, pdf page 348 of BQT_v3_picofile.pdf = printed p.1555 (offset +1207, cross-checked against pdf 444 = printed 1651 whose running head is visible): footnote 4 to the entry کاتوره reads 'قس: سانسکریت katara (ترسو، کم‌رو، گیج، مضطرب) وبلیامز ۲۴۷:۱' — i.e. Mo'in cites Monier-Williams I 247 and writes قس \\\\'compare\\\\', offering the Sanskrit word as a comparandum, not as the source. The page is exactly the one Nourai cites and it is the origin of his root box, but it does not assert derivation.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"vol.3 printed p.1555, entry کاتوره with Mo'in's footnote 4\", \"stance\": \"partial\", \"note\": \"as quoted; the entry itself reads '«کاتوره» سرگشته (سرگشتگی، ظ.) بود. رودکی (سمرقندی) گوید: هیچ راحت می نبینم در سرود و رود تو / جز که از فریاد و زخمهٔ ات خلق را کاتوره خاست' and adds a Manuchehri citation 'آن بلبل کاتوره برجسته ز مطمور'.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/कातर\", \"stance\": \"partial\", \"note\": \"'cowardly, faint-hearted; confused'; neuter 'despair'. Etymology uncertain: possibly a vṛddhi derivative of कतर (katará, \\\\'which of two?\\\\'), or a borrowing (cf. Prakrit कत्तर kattara \\\\'rubbish\\\\'), with 'unusual phonological variation and late attestation' suggesting substrate origin. No Iranian cognate is listed.\"},\n    {\"src\": \"HRN\", \"where\": \"Grundriss (grep for katur/kātūra)\", \"stance\": \"silent\", \"note\": \"Horn's Neupersische Etymologie has no entry for کاتوره; the word is a rare lexicographers' item, not part of his core vocabulary.\"},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Farsi (2-vol Adena abridgement on disk)\", \"stance\": \"silent\", \"note\": \"grep of MON_part1/part2.txt for کاتوره returns nothing; the abridgement drops rare Borhan headwords.\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1, \"lang\": \"Persian\", \"words\": \"kâtŭreh «کاتوره» (also کاتور)\", \"verdict\": \"plausible\",\n    \"derivation\": \"کاتوره kātureh is a rare Persian word of the Samanid period meaning 'bewilderment, being distraught, dizziness' (Borhan p.1555: '«کاتوره» سرگشته [سرگشتگی، ظ.] بود'), attested in the Rudaki line Nourai prints — 'هیچ راحت می نبینم در سرود و رود تو / جز که از فریاد و زخمهٔ ات خلق را کاتوره خاست' — and in Manuchehri ('آن بلبل کاتوره برجسته ز مطمور'). Formally the word looks Persian: کاتور + the ه of the abstract/adjectival formation, which is why Borhan also lists the short form کاتور (Nourai's script_extra). The link with Sanskrit kātara- 'timid, perplexed' is Mo'in's, and he states it with قس 'compare', not as a derivation; the semantic fit ('perplexed' ≈ سرگشته) is good, but the phonology is not: Sanskrit -t- would not normally surface as Persian -t- in a genuine cognate (Old Iranian would show *kātara- with the same shape only by accident), and a tenth-century direct borrowing from Sanskrit into Khorasani Persian, with no Middle Persian or Middle Indic intermediary attested, is not otherwise documented. Nourai's own note — 'Persian words may be cognates with rather than derivatives from Sanskrit' — is therefore the honest verdict; but since Sanskrit kātara- has itself no secure Indo-European etymology (Wiktionary: perhaps a vṛddhi of katará-, perhaps substrate), cognacy cannot be demonstrated either. The Persian word and its meaning are confirmed; the arrow from Sanskrit is a comparison, not an established derivation.\",\n    \"derivation_fa\": \"«کاتوره» واژه‌ای کمیاب از دورهٔ سامانی به معنای «سرگشتگی، آشفتگی، گیجی» است؛ برهان قاطع (ص ۱۵۵۵) می‌نویسد «کاتوره سرگشته (سرگشتگی، ظ.) بود» و همان بیتِ رودکی را می‌آورد که نورایی نقل کرده، و بیتی از منوچهری نیز («آن بلبل کاتوره برجسته ز مطمور»). از نظر ساخت، واژه فارسی می‌نماید: «کاتور» به‌علاوهٔ «ـه»؛ برهان صورتِ کوتاهِ «کاتور» را نیز آورده که نورایی در کنار آن نوشته است. پیوند با سنسکریتِ kātara- «ترسو، سرگشته» از معین است و او آن را با «قس» (مقایسه کنید) آورده، نه به‌عنوان ریشه. سازگاریِ معنایی خوب است، ولی از سوی آوایی دلیلی در کار نیست و وام‌گیریِ مستقیم از سنسکریت به فارسیِ خراسان در سدهٔ چهارم، بی هیچ واسطهٔ فارسی میانه یا هندیِ میانه، در جای دیگری گواهی نشده. پس یادداشتِ خودِ نورایی («شاید هم‌ریشه باشند نه برگرفته») درست‌تر است؛ اما چون خودِ kātaraِ سنسکریت هم ریشه‌شناسیِ استواری ندارد (ویکی‌واژه: شاید مشتقِ وریدّهی از katará-، شاید وام‌واژه‌ای زیرلایه‌ای)، هم‌ریشگی نیز اثبات‌شدنی نیست. واژهٔ فارسی و معنای آن تأیید می‌شود، ولی پیکانِ سنسکریت ← فارسی یک مقایسه است نه یک اشتقاقِ ثابت‌شده.\",\n    \"sources\": [W + \"%E0%A4%95%E0%A4%BE%E0%A4%A4%E0%A4%B0\"],\n    \"ref_check\": [\n      {\"ref\": \"BQT:1555\", \"status\": \"partial\", \"note\": \"printed p.1555 (BQT vol.3 pdf p.348), entry کاتوره with the Rudaki verse Nourai quotes verbatim, and footnote 4: 'قس: سانسکریت katara (ترسو، کم‌رو، گیج، مضطرب) وبلیامز ۲۴۷:۱'. The page is Nourai's source for both the root box and this node, but Mo'in writes 'compare', not 'from'.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"vol.3 p.1555\", \"stance\": \"partial\", \"note\": \"as quoted; also gives the Manuchehri citation (منوچهری دامغانی ۱۷۹) and the variant کاتور.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/कातर\", \"stance\": \"partial\", \"note\": \"confirms the Sanskrit word's meaning ('cowardly, faint-hearted; confused') but gives no Iranian descendant or cognate and calls the Sanskrit etymology itself uncertain.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie\", \"stance\": \"silent\", \"note\": \"no entry for kātureh / kātur (grep of HRN.txt).\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi (Adena 2-vol abridgement)\", \"stance\": \"silent\", \"note\": \"no کاتوره entry in MON_part1/part2.txt.\"}\n    ]\n   }\n  ]\n }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-244.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk244.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-244.json > /dev/null && echo JSON_OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 244"
}
```


### [2026-09-06T16:07:56.655Z] TOOL RESULT

```
written
JSON_OK
nodes verified: 8/8
node verdicts: {'confirmed': 4, 'disputed': 3, 'plausible': 1}
root verdicts: {'plausible': 2, 'confirmed': 2}
ref checks: {'partial': 5, 'supports': 11, 'not_found': 2, 'not_checked': 3}
books consulted: {'supports': 16, 'partial': 8, 'contradicts': 5, 'silent': 2} | by book: {'HRN': 5, 'PHD': 4, 'BQT': 4, 'Wiktionary': 4, 'CHEUNG': 3, 'HUB': 3, 'NYB': 2, 'BRT': 1, 'KNT': 1, 'SYN': 1, 'SOD': 1, 'ISS_alt_DKS': 1, 'MON': 1}
```


## [2026-09-06T16:08:17.506Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-244.json` written, `verify_check.py 244` reports 8/8 nodes, 0 PROBLEM lines.

**Page 244 (book p.214) — 4 entries (1 redirect skipped), 8 nodes**
- Node verdicts: confirmed 4, disputed 3, plausible 1. Root verdicts: confirmed 2 (Kâs 2, Kasyapa), plausible 2 (Karšvar, Kâtara).
- Ref checks: 11 supports, 5 partial, 2 not_found, 3 not_checked (MON — the 6-vol Farhang has no mappable pagination on disk).

**Disputed**
- Kâs 2 #1 (Avestan/OP `paiti-sahva`): sās/sāsta/sāstar/sāxvan/sāsnā are verbatim Pokorny 533 and confirmed, but `paiti-sahva` = Av. paiti.saŋh-, which Bartholomae puts at AiW col. 1578 and Cheung/LIV derive from PIE *ḱens- (Pok. 566).
- Kâs 2 #2 (Pahlavi `soxvan`, `passaxv/pasux`): sāstār + sāstārēh confirmed (Nyberg verbatim), but MP saxwan/passox go to Proto-Iranian *cánhati < *ḱens- (Cheung p.334, Hübschmann pp.126/191/210, MacKenzie's Manich. sxwn/pswx, Wiktionary).
- Kâs 2 #3 (Persian `soxan`, `pâsox`): same reason; ساستا is fine (BQT 1072 "نام دیوی از تابعان اهرمن"). Nourai's own NOTE offers "Kens" for soxan — that is the modern view, and it covers pâsox too; his "Wegwh" alternative for pâsox has no support. Only Horn (HRN:160, after Bartholomae) backs the chart.

**Other findings**
- Karšvar root marked plausible: Avestan karšvar- is exact (BRT col. 459 verified against OCRed column numbers), but Old Persian has no such word (Kent has only karša- 'weight').
- Kâtara marked plausible: BQT 1555 footnote 4 says "قس: سانسکریت katara" — Mo'in *compares*, does not derive; Sanskrit kātara itself has no secure etymology and no Iranian cognate. Nourai's own caveat note is the right one.
- BQT:1573 on the Pahlavi node is **not_found**: that printed page (vol. 3, running head ۱۵۷۳) holds کاکاو/کاکل etc.; likely a slip for 1073.
- FSF:99 **not_found**: p.99 of the scanned Vāzhe-namak is in the ب section and ساستا/ساستار is absent from the whole file.
- **No extraction errors** — I rendered PDF p.244 and the JSON matches the printed page exactly, including the odd "BQT:354,1573" citation and the script extras ساستار / کاتور.
