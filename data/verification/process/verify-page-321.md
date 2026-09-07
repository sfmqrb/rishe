# Verification process log — verify-page-321


## [2026-09-07T15:49:12.022Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 321 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-321.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-321.json. Write /home/sfmqrb/git/rishe/data/verification/page-321.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 321` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T15:49:13.951Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T15:49:14.512Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T15:49:14.529Z] TOOL RESULT

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


## [2026-09-07T15:49:15.355Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-321.txt"
}
```


### [2026-09-07T15:49:15.382Z] TOOL RESULT

```
1	=== PDF page 321 (book page 291) ===
2	--- entry 0 ---
3	ROOT [Latin] Mantellum, Mantil : cloak, towel; cloak  (refs SYN:417; KLN:932)
4	#1 (parent #0) [Arabic] refs=KLN:932 | mandîl : turban, napkin
5	  #2 (parent #1) [Persian] refs=MON:4389 | mandîl «منديل» : napkin, turban
6	  #3 (parent #1) [English] refs=KLN:932 | mandil : turban
7	#4 (parent #0) [French] refs=KLN:934 | manteau : cloak
8	  #5 (parent #4) [Persian] refs=MON:3718 | mânto «مانتو» : manteau
9	  #6 (parent #4) [English] refs=None | manteau
10	--- entry 1 ---
11	ROOT Mantil -> redirect to Mantellum
12	--- entry 2 ---
13	ROOT Manu -> redirect to Men 1
14	--- entry 3 ---
15	ROOT Manus -> redirect to Men 1
16	--- entry 4 ---
17	ROOT [Avestan] Mareğâ : grass  (refs BQT:1990)
18	#1 (parent #0) [Persian] refs=BQT:1990; MON:4019 | marğ «مَرغ ۲» : grass, a kind of fast growing weed ; marğzâr «مرغزار» : meadow ☞Kwel
19	#2 (parent #0) [Sogdian] refs=SOD:216 | mrğ : meadow
20	--- entry 5 ---
21	ROOT [Sanskrit] Mašakah : animal skin used for carrying water  (refs KLN:1018)
22	#1 (parent #0) [Pahlavi] refs=BQT:2014 | mašk : leather
23	  #2 (parent #1) [Persian] refs=MON:4147; BQT:2014 | mašk «مَشک ۳» : animal skin for carrying water ; maškŭ «مَشکو ۲» : (royal) tent | extra: مَشکو ۱ ، مَشکول ، مَشکوله
24	#3 (parent #0) [Hindustani] refs=KLN:1018 | masak : animal skin for carrying water
25	  #4 (parent #3) [English] refs=KLN:1018 | mussuck, mussuk : animal skin for carrying water
26	
```


## [2026-09-07T15:49:18.935Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-321.json",
 "description": "Read source JSON page 321"
}
```


### [2026-09-07T15:49:18.970Z] TOOL RESULT

```
{
  "pdf_page": 321,
  "book_page": 291,
  "entries": [
    {
      "root": {
        "name": "Mantellum, Mantil",
        "lang": "Latin",
        "refs": "SYN:417; KLN:932",
        "gloss": "cloak, towel; cloak"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:932",
          "words": [
            {"translit": "mandîl", "gloss": "turban, napkin", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:4389",
          "words": [
            {"translit": "mandîl", "gloss": "napkin, turban", "script": "منديل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "English",
          "refs": "KLN:932",
          "words": [
            {"translit": "mandil", "gloss": "turban", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "French",
          "refs": "KLN:934",
          "words": [
            {"translit": "manteau", "gloss": "cloak", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:3718",
          "words": [
            {"translit": "mânto", "gloss": "manteau", "script": "مانتو"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "manteau", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Mantil",
        "redirect": "Mantellum"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Manu",
        "redirect": "Men 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Manus",
        "redirect": "Men 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Mareğâ",
        "lang": "Avestan",
        "refs": "BQT:1990",
        "gloss": "grass",
        "note": "EAV:866 indicates that this word is related to the Greek word \"amorphous: shepherd\"."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:1990; MON:4019",
          "words": [
            {"translit": "marğ", "gloss": "grass, a kind of fast growing weed", "script": "مَرغ ۲"},
            {"translit": "marğzâr", "gloss": "meadow", "script": "مرغزار", "see": ["Kwel"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "بیاسود چندی زبهر شکار - همی گشت در کوه و در مرغزار", "poet": "Ferdowsî"}
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:216",
          "words": [
            {"translit": "mrğ", "gloss": "meadow", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Mašakah",
        "lang": "Sanskrit",
        "refs": "KLN:1018",
        "gloss": "animal skin used for carrying water"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BQT:2014",
          "words": [
            {"translit": "mašk", "gloss": "leather", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:4147; BQT:2014",
          "words": [
            {"translit": "mašk", "gloss": "animal skin for carrying water", "script": "مَشک ۳"},
            {"translit": "maškŭ", "gloss": "(royal) tent", "script": "مَشکو ۲"}
          ],
          "script_extra": "مَشکو ۱ ، مَشکول ، مَشکوله",
          "note": null,
          "quote": {"text": "فغستان چو آمد به مَشکوی شاه - یکی تاج بر سر زمشک سیاه", "poet": "Ferdowsî"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Hindustani",
          "refs": "KLN:1018",
          "words": [
            {"translit": "masak", "gloss": "animal skin for carrying water", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "KLN:1018",
          "words": [
            {"translit": "mussuck, mussuk", "gloss": "animal skin for carrying water", "script": null}
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


## [2026-09-07T15:49:19.654Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T15:49:19.704Z] TOOL RESULT

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


## [2026-09-07T15:49:27.285Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','SYN','MON','BQT','SOD','POK','WLD','AHD','LKT','HJB','AID','PHD','BRT','HRN','HUB','ARY','PHN','DEV','SKT','FSD','WEB','LEW','LAT','NYB','EAV','IEC','PLA','AFM','RCH','FVQ']:\n    v=d.get(k)\n    if v: print(k, json.dumps(v, ensure_ascii=False)[:600]); print()\n\""
}
```


### [2026-09-07T15:49:28.654Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4

AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lo

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar

DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

EAV {"title": "J. Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939) pp. 861-869", "edition_found": "JSTOR offprint collected in an IA item 'Studies by Jacques Duchesne-Guillemin'", "kind": "archive_djvu", "url": "https://archive.org/details/duchesne-guillemin-studies", "identifier": "duchesne-guillemin-studies", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/EAV_studies.txt", "page_offset": "The article keeps its BSOAS page numbers 861-869: leaf = printed - 702 (e.g. leaf 169 = p.871), i.e. pp. 861-869 are at leaves ~159-167. local file has \\f between leaves (0-

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.history.resource.17812; 1852 Johnson dictionarypersia00johnuoft)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 =

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
```


## [2026-09-07T15:49:33.080Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','SYN','SOD','BQT','MON']:\n    print(k, json.dumps(d[k], ensure_ascii=False, indent=1))\n    print('---')\n\""
}
```


### [2026-09-07T15:49:34.449Z] TOOL RESULT

```
KLN {
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
---
SYN {
 "title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949",
 "edition_found": "1949 (reprint scans, same pagination in all printings)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt",
 "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.",
 "notes": "Two other open copies: dictionaryofselectedsynonyms...buck_963_N, fock_a-dictionary-...; restricted: dictionaryofsele0000carl.",
 "cites": "page number of Buck, A Dictionary of Selected Synonyms (1949)"
}
---
SOD {
 "title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/SogdianDictionary",
 "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
 ],
 "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
 "covers_etymology": true,
 "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.",
 "cites": "entry number / page in Gharib's Sogdian dictionary"
}
---
BQT {
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt"
 ],
 "page_offset": "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').",
 "covers_etymology": true,
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209 | BQT_v2_pages.txt: printed page = leaf + 540 (verified by catch-lines at pp. 838-855, 869, 904); earlier estimate +543 was 3 pages off.",
 "scans": [
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
 ],
 "cites": "page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material"
}
---
MON {
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
 "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
---
```


## [2026-09-07T15:49:40.622Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"^mandil\\|mandil\\b\" KLN_1966.txt | head -30\necho \"=== mantle/mantel ===\"\ngrep -n -i \"^mantle\\|^mantel\\|^manteau\\|mantellum\\|mantelum\" KLN_1966.txt | head -30\necho \"=== mussuck ===\"\ngrep -n -i \"mussuck\\|mussuk\\|masak\" KLN_1966.txt | head -30"
}
```


### [2026-09-07T15:49:40.737Z] TOOL RESULT

```
22769:mandibulo-,  combining  form  meaning  ‘mandibu¬ lar’.  —  Fr.  L.  mandibula.  See  mandible, mandil,  n.,  a  turban.  —  Arab,  mandll,  fr.  MGk. (jkxv8y]X[.ov,  fr.  L.  mantile,  which  is  rel.  to  man- telum,  ‘towel,  (table-)napkin’.  See  mantle, n.
22770:mandilion,  n.,  a  cloak.  —  F.  mandillon ,  fr.  It. mandiglione,  ‘soldier’s  cloak’,  augment,  of OPisan  mandillo,  ‘handkerchief’,  fr.  Arab. mandil.  See  prec.  word.
=== mantle/mantel ===
22844:mantel,  n.  —  A  var.  of  mantle, mantelet,  also  mantlet,  n.,  1)  a  small  cloak;  2)  a temporary  shelter.  —  OF.,  dimin.  of  mantel. See  mantle  and  -et.
29713:mantle.
=== mussuck ===
24752:mussel,  n.,  any  of  several  bivalve  mollusks.  — ME.  muscle,  fr.  OE.  muscelle,  muscle,  fr.  VL. *muscula  [whence  also  OF.  musle  (F.  moule), OS.,  OHG.  muscula  (MHG.,  G.  muschel), ‘mussel’],  corresponding  to  L.  musculus,  ‘little mouse,  muscle;  sea  mussel’.  See  muscle. Derivatives:  mussel-ed ,  adj.,  mussel-er,  n. mussuck,  mussuk,  n.,  a  leathern  skin  for  water (India)  —  Hind,  masak,  fr.  OI.  masakah. Mussulman,  n.,  a  Moslem.  —  Turk,  musulman, fr.  Pers.  musulman,  which  is  formed  with  the adj.  suff.  -an  fr.  Arab,  muslim,  ‘Moslem’.  See Moslem.
```


## [2026-09-07T15:49:52.239Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'mandil,  n.,  a  turban' in l or 'mussuck,  mussuk' in l or re.search(r'mantle,\\s+n\\.,',l):\n        print('LEAF',i)\nEOF"
}
```


### [2026-09-07T15:49:53.665Z] TOOL RESULT

```
LEAF 500
LEAF 545
```


## [2026-09-07T15:50:00.928Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in (500,545):\n    print('==== LEAF',i)\n    print(leaves[i][:1500])\nEOF"
}
```


### [2026-09-07T15:50:02.480Z] TOOL RESULT

```
==== LEAF 500
 Yakut  mamma ,  ‘earth’  (the mammoth  was  believed  to  root  up  the  earth  like a  mole,  whence  its  name.) mammy,  n.,  1)  child’s  word  for  mother;  2)  a  Ne¬ gro  nurse.  —  See  mamma,  ‘mother’. man,  n.  —  ME.  man,  fr.  OE.  man,  ‘human  being, man’  mt  to  OS..  Swed..  Du..  OHG.,  MHG.
930
man,  G.  Mann,  ON.  madr  (for  *mannr),  Dan. mand,  Goth,  manna,  ‘man’  (cp.  Mannas,  a  tribal deity,  in  Tacitus’  Germania,  chapt.  2),  OS.  men- nisco,  OFris.  manniska,  MDu.  mensche,  Du. mens,  OHG.  mannisco,  mennisco,  MHG.  men¬ sche,  mensch,  G.  Mensch,  ‘man’  (orig.  adj. meaning  ‘human’),  and  cogn.  with  OI.  manuh, ‘man;  progenitor  of  mankind’,  Avestic  manu-, ‘man’,  OSlav.  mgSi,  ‘man’.  All  these  words  prob. meant  orig.  ‘one  who  thinks’,  fr.  I.-E.  base *men-,  ‘to  think’,  whence  also  OI.  matih,  matih, ‘thought’,  L.  mens,  gen.  mentis,  ‘mind’,  Goth. muns,  ‘thought’,  munan ,  ‘to  think',  ON.  minni, ‘mind’,  OE.  gemynd,  ‘memory’.  See  mind  and cp.  Manu,  muzhik,  and  the  second  element  in Marcomanni.  Cp.  also  minx.
Derivatives:  man,  tr.  v.,  man-ful,  adj.,  man-ful- ly,  adv.,  man-ful-ness,  n.,  man-hood ,  n.,  man-ly, adj.,  man-li-ness,  n.,  mann-ish,  adj.,  mann-ish-ly, adv.,  mann-ish-ness,  n. man,  n.,  a  unit  of  weight.  —  See  maund. manacle,  n.,  handcuff.  —  ME.  manicle,  fr.  OF. manicle,  lit.  ‘a  little  hand’,  fr.  L.  manicula,  dimin. of  manus,  ‘hand’.  
==== LEAF 545
urrain’,  which  also  derive  fr. VL.  *morire.  Cp.  murrina. murre,  n.,  1)  guillemot  of  the  genus  Uria;  2)  the razorbill  —  Related  to  dial.  E.  marrot,  morrot, ‘guillemot’;  of  uncertain  origin.  Cp.  next  word, murrelet,  n.,  any  of  various  birds  of  the  auk family.  —  Formed  fr.  murre  with  dimin.  suff. -let.
murrey,  adj.,  mulberry  red;  dark  purplish  red;  n., murrey  color.  —  ME.,  fr.  MF.  moree,  fr.  ML. moratus,  ‘mulberry  colored’,  fr.  L.  morum, ‘mulberry’.  See  mulberry, murrhine,  adj.,  made  of,  or  resembling,  murra;  n., a  murrhine  vase  ( Roman  antiq.).  —  L.  murr(h)i- nus,  ‘of,  or  made  of,  murra’,  fr.  murra,  less  cor¬ rectly  murrha,  ‘fluorspar;  agate;  a  glass  imita¬ tion’,  which  is  of  Iranian  origin.  Cp.  Pers.  mori, muri,  ‘globule  of  glass'.  Cp.  also  Gk.  pippta, fj.ouppi.va  (pi.),  which  are  of  the  same  origin  and meaning  as  L.  murra.
murrina,  n.,  a  disease  of  horses  (vet er.)  —  Sp. morriha,  ‘murrain’.  See  murrain.
Mus,  n.,  a  genus  of  rodents,  the  mouse  (zool.)  — L.  mus,  gen.  muris,  ‘mouse’.  See  mouse.
Musa,  n.,  a  genus  of  trees,  the  banana  (hot.)  — ModL.,  fr.  Arab.  mauzah,  ‘banana’,  fr.  mauz, ‘banana  tree’.
Musaph,  also  spelled  Musaf,  n.,  additional  prayer on  the  Sabbath  and  on  festivals,  immediately following  the  morning  prayer  ( =  Sltaharith).  — Mishnaic  Heb.  musaph,  ‘additional  offering,  ad¬ ditional
```


## [2026-09-07T15:50:10.882Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in (500,501,502):\n    t=leaves[i]\n    print('==== LEAF',i, 'pagenums:', re.findall(r'^\\s*(\\d{3,4})\\s*$', t, re.M))\n    for kw in ['mandil','mantile','mantle','manteau','mantel','mantilla']:\n        for m in re.finditer(kw,t):\n            s=max(0,m.start()-80); print('  ',kw,'>>',t[s:m.start()+420].replace('\\n',' '))\n            break\nEOF"
}
```


### [2026-09-07T15:50:12.418Z] TOOL RESULT

```
==== LEAF 500 pagenums: ['930', '931']
   mandil >> mbining  form  meaning  ‘mandibu¬ lar’.  —  Fr.  L.  mandibula.  See  mandible, mandil,  n.,  a  turban.  —  Arab,  mandll,  fr.  MGk. (jkxv8y]X[.ov,  fr.  L.  mantile,  which  is  rel.  to  man- telum,  ‘towel,  (table-)napkin’.  See  mantle, n. mandilion,  n.,  a  cloak.  —  F.  mandillon ,  fr.  It. mandiglione,  ‘soldier’s  cloak’,  augment,  of OPisan  mandillo,  ‘handkerchief’,  fr.  Arab. mandil.  See  prec.  word. mandola,  n.,  a  large  variety  of  mandolin.  —  It. mandola,  mandora,
   mantile >> mandil,  n.,  a  turban.  —  Arab,  mandll,  fr.  MGk. (jkxv8y]X[.ov,  fr.  L.  mantile,  which  is  rel.  to  man- telum,  ‘towel,  (table-)napkin’.  See  mantle, n. mandilion,  n.,  a  cloak.  —  F.  mandillon ,  fr.  It. mandiglione,  ‘soldier’s  cloak’,  augment,  of OPisan  mandillo,  ‘handkerchief’,  fr.  Arab. mandil.  See  prec.  word. mandola,  n.,  a  large  variety  of  mandolin.  —  It. mandola,  mandora,  ‘lute’,  fr.  Late  L.  pandur
   mantle >> L.  mantile,  which  is  rel.  to  man- telum,  ‘towel,  (table-)napkin’.  See  mantle, n. mandilion,  n.,  a  cloak.  —  F.  mandillon ,  fr.  It. mandiglione,  ‘soldier’s  cloak’,  augment,  of OPisan  mandillo,  ‘handkerchief’,  fr.  Arab. mandil.  See  prec.  word. mandola,  n.,  a  large  variety  of  mandolin.  —  It. mandola,  mandora,  ‘lute’,  fr.  Late  L.  pandur
==== LEAF 501 pagenums: ['932', '933', '934']
==== LEAF 502 pagenums: ['935', '936']
   mantle >> ate  L.  mantum,  ‘cloak’,  back  formation  fr. L.  mantelium,  ‘cloak’.  See  mantle, manteau,  n.,  cloak,  mantle.  —  F.,  fr.  OF.  mantel, fr.  L.  mantelium,  ‘cloak’.  See  mantle  and  cp. prec.  word. mantel,  n.  —  A  var.  of  mantle, mantelet,  also  mantlet,  n.,  1)  a  small  cloak;  2)  a temporary  shelter.  —  OF.,  dimin.  of  mantel. See  mantle  and  -et. mantic,  adj.,  pertaining  to  divination,  prophetic. —  Gk.  poomxo?,  ‘prophetic,  oracular’,  fr.  pav- Tt?.  See
   manteau >>  mantum,  ‘cloak’,  back  formation  fr. L.  mantelium,  ‘cloak’.  See  mantle, manteau,  n.,  cloak,  mantle.  —  F.,  fr.  OF.  mantel, fr.  L.  mantelium,  ‘cloak’.  See  mantle  and  cp. prec.  word. mantel,  n.  —  A  var.  of  mantle, mantelet,  also  mantlet,  n.,  1)  a  small  cloak;  2)  a temporary  shelter.  —  OF.,  dimin.  of  mantel. See  mantle  and  -et. mantic,  adj.,  pertaining  to  divination,  prophetic. —  Gk.  poomxo?,  ‘prophetic,  oracular’,  fr.  pav- Tt?.  See  mantis
   mantel >>   manta. 935 manumit fr.  Late  L.  mantum,  ‘cloak’,  back  formation  fr. L.  mantelium,  ‘cloak’.  See  mantle, manteau,  n.,  cloak,  mantle.  —  F.,  fr.  OF.  mantel, fr.  L.  mantelium,  ‘cloak’.  See  mantle  and  cp. prec.  word. mantel,  n.  —  A  var.  of  mantle, mantelet,  also  mantlet,  n.,  1)  a  small  cloak;  2)  a temporary  shelter.  —  OF.,  dimin.  of  mantel. See  mantle  and  -et. mantic,  adj.,  pertaining  to  divination,  prophetic. —  Gk.  poomxo?,  ‘prophetic,  orac
   mantilla >> iromantic,  oneiromantic.  —  Fr.  Gk.  pocmxo?. See  prec.  word  and  -mancy. mantilla,  n.,  a  short  mantle.  —  Sp.,  dimin.  of manta,  'cloak',  fr.  VL.  *manta.  See  manta, mantis,  n.,  any  of  various  insects  holding  up  their forelegs  as  if  in  prayer.  —  ModL.,  fr.  Gk.  pixv- vtq,  ‘seer,  prophet,  soothsayer’,  which  is  rel.  to (jLavTEia,  ‘oracle,  divination’.  See  -mancy. mantissa,  n.,  the  decimal  part  of  a  logarithm.  — L.  mantisa,  less  correctly  man
```


## [2026-09-07T15:50:22.599Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nt=leaves[500]\ni=t.find('mandil,  n.,  a  turban')\nprint('mandil idx',i)\nfor m in re.finditer(r'^\\s*(93\\d)\\s*$',t,re.M): print(m.group(1), m.start())\nprint('====')\nfor i in (502,503):\n    t=leaves[i]\n    for m in re.finditer(r'mantle,\\s+n\\.,',t):\n        print('leaf',i,'::',t[max(0,m.start()-100):m.start()+900].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T15:50:24.036Z] TOOL RESULT

```
mandil idx 10723
930 313
931 3330
====
```


## [2026-09-07T15:50:37.381Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nprint('leaf500 len',len(leaves[500]))\nprint(leaves[500][10400:11400].replace('\\n',' '))\nprint('#### leaf 502 tail search mantle')\nfor i in (502,503):\n    t=leaves[i]\n    j=t.find('mantle')\n    while j!=-1:\n        print('leaf',i,t[j:j+300].replace('\\n',' '))\n        j=t.find('mantle',j+1)\n        if j>len(t)-10: break\nEOF"
}
```


### [2026-09-07T15:50:38.732Z] TOOL RESULT

```
leaf500 len 11175
‘jaw’.  See  mandible  and  adj.  suff. -ate,  resp.  also  -ed. mandibuliform,  adj.,  having  the  form  of  a  man¬ dible.  —  Compounded  of  L.  mandibula,  ‘jaw’, and  forma,  ‘shape,  form’.  See  mandible  and form,  n. mandibulo-,  combining  form  meaning  ‘mandibu¬ lar’.  —  Fr.  L.  mandibula.  See  mandible, mandil,  n.,  a  turban.  —  Arab,  mandll,  fr.  MGk. (jkxv8y]X[.ov,  fr.  L.  mantile,  which  is  rel.  to  man- telum,  ‘towel,  (table-)napkin’.  See  mantle, n. mandilion,  n.,  a  cloak.  —  F.  mandillon ,  fr.  It. mandiglione,  ‘soldier’s  cloak’,  augment,  of OPisan  mandillo,  ‘handkerchief’,  fr.  Arab. mandil.  See  prec.  word. mandola,  n.,  a  large  variety  of  mandolin.  —  It. mandola,  mandora,  ‘lute’,  fr.  Late  L.  pandur
#### leaf 502 tail search mantle
leaf 502 mantle, manteau,  n.,  cloak,  mantle.  —  F.,  fr.  OF.  mantel, fr.  L.  mantelium,  ‘cloak’.  See  mantle  and  cp. prec.  word. mantel,  n.  —  A  var.  of  mantle, mantelet,  also  mantlet,  n.,  1)  a  small  cloak;  2)  a temporary  shelter.  —  OF.,  dimin.  of  mantel. See  mantle  and  -et
leaf 502 mantle.  —  F.,  fr.  OF.  mantel, fr.  L.  mantelium,  ‘cloak’.  See  mantle  and  cp. prec.  word. mantel,  n.  —  A  var.  of  mantle, mantelet,  also  mantlet,  n.,  1)  a  small  cloak;  2)  a temporary  shelter.  —  OF.,  dimin.  of  mantel. See  mantle  and  -et. mantic,  adj.,  pertaining  t
leaf 502 mantle  and  cp. prec.  word. mantel,  n.  —  A  var.  of  mantle, mantelet,  also  mantlet,  n.,  1)  a  small  cloak;  2)  a temporary  shelter.  —  OF.,  dimin.  of  mantel. See  mantle  and  -et. mantic,  adj.,  pertaining  to  divination,  prophetic. —  Gk.  poomxo?,  ‘prophetic,  oracular’,  f
leaf 502 mantle, mantelet,  also  mantlet,  n.,  1)  a  small  cloak;  2)  a temporary  shelter.  —  OF.,  dimin.  of  mantel. See  mantle  and  -et. mantic,  adj.,  pertaining  to  divination,  prophetic. —  Gk.  poomxo?,  ‘prophetic,  oracular’,  fr.  pav- Tt?.  See  mantis  and  adj.  suff.  -ic. -mantic,
leaf 502 mantlet,  n.,  1)  a  small  cloak;  2)  a temporary  shelter.  —  OF.,  dimin.  of  mantel. See  mantle  and  -et. mantic,  adj.,  pertaining  to  divination,  prophetic. —  Gk.  poomxo?,  ‘prophetic,  oracular’,  fr.  pav- Tt?.  See  mantis  and  adj.  suff.  -ic. -mantic,  a  combining  form  mea
leaf 502 mantle  and  -et. mantic,  adj.,  pertaining  to  divination,  prophetic. —  Gk.  poomxo?,  ‘prophetic,  oracular’,  fr.  pav- Tt?.  See  mantis  and  adj.  suff.  -ic. -mantic,  a  combining  form  meaning  ‘divining, foretelling',  used  to  form  adjectives  corre¬ sponding  to  nouns  ending  in
leaf 502 mantle.  —  Sp.,  dimin.  of manta,  'cloak',  fr.  VL.  *manta.  See  manta, mantis,  n.,  any  of  various  insects  holding  up  their forelegs  as  if  in  prayer.  —  ModL.,  fr.  Gk.  pixv- vtq,  ‘seer,  prophet,  soothsayer’,  which  is  rel.  to (jLavTEia,  ‘oracle,  divination’.  See  -manc
leaf 502 mantle,  n.  —  ME.  mantel,  fr.  OF.  mantel  (=  F. manteau),  and  ME.  mentel,  fr.  OE.  mentel.  Both OF.  mantel  and  OE.  mentel  derive  fr.  L.  man- tellum,  ‘cloak,  veil’  (whence,  with  back  forma¬ tion,  Late  L.  mantum,  ‘cloak’,  mantus,  ‘a  short cloak-),  which  is  prob.  o
leaf 502 mantle,  portmanteau. Derivative:  mantle,  tr.  and  intr.  v. mantra,  n.,  that  part  of  the  Vedas  which  contains hymns  ( Hinduism)  —  OI.  mantrah,  lit.  ‘speech, sacred  text,  counsel’,  rel.  to  Avestic  mqftra-,  of S.m.  See  mandarin. mantua,  n.,  a  mantle  formerly  worn  by  w
leaf 502 mantle,  tr.  and  intr.  v. mantra,  n.,  that  part  of  the  Vedas  which  contains hymns  ( Hinduism)  —  OI.  mantrah,  lit.  ‘speech, sacred  text,  counsel’,  rel.  to  Avestic  mqftra-,  of S.m.  See  mandarin. mantua,  n.,  a  mantle  formerly  worn  by  women. —  F.  manteau,  ‘cloak,  man
leaf 502 mantle  formerly  worn  by  women. —  F.  manteau,  ‘cloak,  mantle'  (see  mantle) ;  in¬ fluenced  in  form  by  Mantua,  town  in  Italy  (as  if the  word  meant  ‘a  mantle  manufactured  in Mantua’). Manu,  n.,  any  of  the  fourteen  mythological  pro¬ genitors  of  mankind  (Hindu  mythol.)
leaf 502 mantle'  (see  mantle) ;  in¬ fluenced  in  form  by  Mantua,  town  in  Italy  (as  if the  word  meant  ‘a  mantle  manufactured  in Mantua’). Manu,  n.,  any  of  the  fourteen  mythological  pro¬ genitors  of  mankind  (Hindu  mythol.)  — -  OI. manuh,  ‘man;  progenitor  of  mankind’,  rel.  to
leaf 502 mantle) ;  in¬ fluenced  in  form  by  Mantua,  town  in  Italy  (as  if the  word  meant  ‘a  mantle  manufactured  in Mantua’). Manu,  n.,  any  of  the  fourteen  mythological  pro¬ genitors  of  mankind  (Hindu  mythol.)  — -  OI. manuh,  ‘man;  progenitor  of  mankind’,  rel.  to Avestic  manu-
leaf 502 mantle  manufactured  in Mantua’). Manu,  n.,  any  of  the  fourteen  mythological  pro¬ genitors  of  mankind  (Hindu  mythol.)  — -  OI. manuh,  ‘man;  progenitor  of  mankind’,  rel.  to Avestic  manu-,  and  cogn.  with  OSIav.  mpzi, Goth,  manna,  OE.  mann,  ‘man’.  See  man. manual,  adj.,
```


## [2026-09-07T15:50:43.825Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nt=leaves[502]\nj=t.find('mantle,  n.  —  ME.')\nprint(t[j:j+1200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T15:50:45.266Z] TOOL RESULT

```
mantle,  n.  —  ME.  mantel,  fr.  OF.  mantel  (=  F. manteau),  and  ME.  mentel,  fr.  OE.  mentel.  Both OF.  mantel  and  OE.  mentel  derive  fr.  L.  man- tellum,  ‘cloak,  veil’  (whence,  with  back  forma¬ tion,  Late  L.  mantum,  ‘cloak’,  mantus,  ‘a  short cloak-),  which  is  prob.  of  Celtic  origin.  It.  man- tello,  OHG.  mantal,  mandal  (whence  MHG. mantel,  mandel,  G.  Mantel),  ON.  mottull,  also derive  fr.  L.  mantelium.  Cp.  manta,  manteau, mantelet,  dismantle,  portmanteau. Derivative:  mantle,  tr.  and  intr.  v. mantra,  n.,  that  part  of  the  Vedas  which  contains hymns  ( Hinduism)  —  OI.  mantrah,  lit.  ‘speech, sacred  text,  counsel’,  rel.  to  Avestic  mqftra-,  of S.m.  See  mandarin. mantua,  n.,  a  mantle  formerly  worn  by  women. —  F.  manteau,  ‘cloak,  mantle'  (see  mantle) ;  in¬ fluenced  in  form  by  Mantua,  town  in  Italy  (as  if the  word  meant  ‘a  mantle  manufactured  in Mantua’). Manu,  n.,  any  of  the  fourteen  mythological  pro¬ genitors  of  mankind  (Hindu  mythol.)  — -  OI. manuh,  ‘man;  progenitor  of  mankind’,  rel.  to Avestic  manu-,  and  cogn.  with  OSIav.  mpzi, Goth,  manna,  OE.  mann,
```


## [2026-09-07T15:50:53.044Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN mant ===\"\ngrep -n \"mantellum\\|mantēl\\|mantel\\|mantile\\|mantele\" SYN.txt | head -20\necho \"=== SYN leaf 441 (p417) ===\"\npython3 - <<'EOF'\ndata=open('SYN.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nprint(len(leaves))\nprint(leaves[441][:2500])\nEOF"
}
```


### [2026-09-07T15:50:54.458Z] TOOL RESULT

```
=== SYN mant ===
10366:6.41 CLOAK Grk.  tydrwov, xdAatva, dapos Goth. wasti, hakuls Lith. apsiaustas, ploSéius NG pavobas (lit,) ON Jeldr, skikkja, kapa, Lett.  mételis Lat. toga, pallium, paenu- mettull ChSl.  plastt, riza la, lacerna, mantel- Dan. kaabe, kappe SCr. plat, kabanica lum Sw. kappa, mantel Boh. playt’ It. mantello, cappa OE hacele, sciccels, w2- Pol. _— plaszcz Fr. manicau fels, mentel, pall Russ. plagsé Sp. manto, capa ME cloke, mantel, pall Skt.  drdpi-, pravara- Rum. mania NE cloak Ir. lenn, brat, mattal Du. mantel NIr.  claca, brat OHG = hachul, mantal W. mantell, cochl, clog MHG mantel Br. mantell NHG mantel
10392:Late Lat. mantellum, dim. of a Celto- Iberian mantum, whence Sp. manto. Hence It. mantello, OF r. mantel (> ME nantel, NE mantle), Fr. manteau (> Rum. manta); Ir. mattal, matal (fr. ON moltull), W., Br. mantell (Loth, Mots lat. 184); ON mottull, OE mentel, OHG mantal, Du.. MHG, NHG mantel (>Sw. mantel, Lith. mantelis; Lett. mételis through ORuss. mjatili; also Slavic words, most in specialized sense. Emout-M. 589. Walde-H. 2.32 f. REW 5326, 5828. Berneker 2.17. we oe capa, te late Lat. cappa Mia ists fc overing’ (Isid.), whence vith caput ied (6.55), connection kappe, Sy a dub. Hence also Dan. Another = aA poet MLG kappe). ‘dpa, Dan, kaabe ie ee ON
11254:1. NG pavrpdt, pavrihc (Byz. pavTi- Avy, -idov mostly ‘towel’) fr. Lat. mantéle, mantile ‘towel’ (6.82).
=== SYN leaf 441 (p417) ===
1545
 with @ Ir. tin pan ike adjj-00s, 0, 443, Buck, Cl.Ph. . Enya, Cret. _ pAve. coll. ‘cloth-
mre ite a, id " plsewhere mids
' Ion. «fuarvor, sg. : Sioa pl. ‘clothes’, fr. elua; oe (> It. veste, etc.), hence v
b. vestire) vestitus, vestimen- lito, Sp. vestido; Fr. véte- ment’ or coll., pl. ‘clothes’) ; ‘sarment, clothing’, pl.
formerly
placed by oF after Fr. vélement) ; Goth. wasti ‘gar-
ment’, pl. ‘clothing’; Skt. vdsas-, vasana-, Ay, vanhana- (cf. Hom. éavés ‘robe, gar- ment’, fr, *¢écavos), Skt., Av. vastra-, all sg, ‘garment’, pl. ‘clothes’; Toch. A wsdl (6886, 471).
2. Grk. &dtua ‘garment’, NG id., also sg. coll. or pl. ‘clothes’, fr. éébw ‘clothe’ (6.11).
NG pofxa ‘clothes’ (the pop. word), %. ‘garment’, fr. Slavic (below, 7). G. Meyer, Neugr. Stud. 2.55,
ne dépeua ‘garment’, esp. ‘“woman’s S, pl. ‘clothes’, late form of Grk.
ua ‘burden, what: j ’ 5: die , 1s worn’, fr. Grk.
Fr. habit ‘garment’, pl. : > fr, Lat habi :
alin ‘tat i abitus garment’, REW en 1 Condition? fr, habére ‘have’,
8p, Topa, f M8) KEW 7ogg,” OF Pah (bee
Um, 4 - seldom . cay iminte ‘clothing’ (pl.
lr. ¢mbrdca ‘clothe’ (6.11). » Pl. ‘clothing’, V, 7).
»» above, 1,
G; PERSONAL ADORNMENT AND CARE
igitized by Arya Samaj Foundation Chennai and eGangotri
395
Pedersen 1.24), W., Br. dillad, OCorn. dillat ‘clothes’, etym.? Henry 98.
Ir. étach, étiud ‘clothes’, NIr. é@adach ‘cloth, clothes’, fr. Ir. in-tuigur, étim ‘clothe’ (6.11). Pedersen 2.514, 655.
W. guwisg, Br. gwisk, gwiskamant, above, 1.
5. Goth. wasti, above, 1.
ON kledi, Dan. kleder, Sw. kldder (pl.) ‘clothes’, sg. ‘cloth’ or ‘garment’, Sw. klddning ‘garment’, coll. ‘clothes’, OE clapes, etc. (pl.) ‘clothes’, sg. ‘cloth’, MHG kleit, NHG kleid, Du. kleed ‘gar- ment, dress’, pl. ‘clothes’, MHG klez- dunge, NHG kleidung, Du. kleeding (coll.) ‘clothing’, fr. words orig. meaning ‘cloth’ (6.21).
ON buningr, binadr ‘equipment’ and esp. ‘clothing’, fr. bua ‘equip, prepare, dwell’ : Goth. bauan ‘till, dwell’, OHG, OE buan ‘dwell’, TE *bheu- ‘become, be’. Walde-P. 2.140 ff.
ON fot, pl. of fat ‘vessel’ = OF fat, OS fat, OHG faz ‘vessel’, cf. Goth. fétjan ‘adorn’, ga-féteins ‘adornment’ : Lith. puodas ‘pot’, OHG fazzdn ‘hold, contain, prepare’, also ‘dress’. Walde-P. 2.22. Falk-Torp 200.
OE gewéde, ME iwede, wede (NE widow’s weeds), OHG giwati, wat, MHG wat (coll.) ‘clothing’, orig. ‘cloth’, cf. ON vad ‘cloth’ (6.21).
OE réaf ‘spoils, booty’, but esp. ‘gar- ment’, pl. ‘clothes’ : OHG roub ‘booty’, etc. 20.48).
OE hregl ‘garment, robe, cloak’, et
```


## [2026-09-07T15:50:59.961Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndata=open('SYN.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i,l in enumerate(leaves):\n    if '6.41 CLOAK' in l or 'dim. of a Celto- Iberian mantum' in l:\n        print('LEAF',i, '=> printed approx', i-24)\n        print(l[:400])\n        print('...')\nEOF"
}
```


### [2026-09-07T15:51:01.434Z] TOOL RESULT

```
LEAF 462 => printed approx 438
r. Slavic (cf. Russ. krasit’, below, 6).
6. SCr. bojadisati, also ‘paint’, deriv. of boja ‘dye, paint’, this from Turk. boya id.
Russ. krasit’, ‘adorn’ hence ‘dye, paint’, fr. krasa ‘beauty, adornment’ : late ChSl. krasa ‘beauty’, OBoh. krasa ‘light, splendor’, etc. Berneker 607. Walde-P. 1.418 ff.
7. Skt. ra(v)jaya-, caus. of ra(i)j- ‘be bright, colored, red’ (cf. raga- ‘coloring, dyeing’, rakta-
...
LEAF 463 => printed approx 439
ke, mantel, pall Skt.  drdpi-, pravara- Rum. mania NE cloak Ir. lenn, brat, mattal Du. mantel NIr.  claca, brat OHG = hachul, mantal W. mantell, cochl, clog MHG mantel Br. mantell NHG mantel
Under ‘cloak’ are grouped the more important words for a loose outer gar- ment, without defining their more special form, even where this is known, and without attempting to include all the special varieties o
...
```


## [2026-09-07T15:51:07.534Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndata=open('SYN.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nprint(leaves[463][:3500])\nEOF"
}
```


### [2026-09-07T15:51:08.908Z] TOOL RESULT

```
ke, mantel, pall Skt.  drdpi-, pravara- Rum. mania NE cloak Ir. lenn, brat, mattal Du. mantel NIr.  claca, brat OHG = hachul, mantal W. mantell, cochl, clog MHG mantel Br. mantell NHG mantel
Under ‘cloak’ are grouped the more important words for a loose outer gar- ment, without defining their more special form, even where this is known, and without attempting to include all the special varieties of cloaks, some of which are rather ‘shawls’ or ‘capes’. For the great variety of Greek and Roman cloaks, cf. Daremberg et Saglio s.v. pallium.
1. Grk. tuarioy ‘garment’ (6.12), esp. ‘cloak’.
Grk. xAatva (> Lat. laena Tough
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
woolen cloak’, perh. through Etruscan), xAavis, orig.? Boisacg 1062. Ernout-M. 518. Walde-H. 1.749.
Grk. ¢épos ¢é&pos, : dapar’ bpalvery, mdéxeww Hesych., dopuds ‘woven basket , Lith. burva ‘a sort of garment’, buré ‘sail Walde-P. 2.164. :
Grk. yavdta (Aesch. of a Liburniad cloak), later pavdtas as Byz. and NG (lit.; but pavrta ‘military cloak or over- coat’), doubtless a loanword, but source?
2. Lat. toga : tegere ‘cover’ (12.26).
Lat. pallium (> OE pall, ME, NE
wid ee ee eee
— eee ers 06ee CSe
Se
— 7 a i a i — 2. oe eo a ene
orrm mm
a”
<n ne <a ee
=Zw
eS EM ST a i a wet a te)
opoTH 10
il, sb." 5), perh. NED s.V- ae rrowing fr. Grk.
uate pall Va a de-P. 2.58. Ernout- oves:
THs rk. gawéda (Rhin- on pac gawddns (by meta- | pap., etc.), this thesis ‘g pright-colored or shin-
: ‘light-bringing,
+ pawvones ve forth, reveal’.
115. erh. fr. lacer ‘torn, as S oe ne ‘rag’, Aaxifw ‘tear ‘ lochma ‘rag’. WaldeP. 2.419 £. Walde-H. tae: Frnout-M. 515 (“only pop. etym.”).
Late Lat. mantellum, dim. of a Celto- Iberian mantum, whence Sp. manto. Hence It. mantello, OF r. mantel (> ME nantel, NE mantle), Fr. manteau (> Rum. manta); Ir. mattal, matal (fr. ON moltull), W., Br. mantell (Loth, Mots lat. 184); ON mottull, OE mentel, OHG mantal, Du.. MHG, NHG mantel (>Sw. mantel, Lith. mantelis; Lett. mételis through ORuss. mjatili; also Slavic words, most in specialized sense. Emout-M. 589. Walde-H. 2.32 f. REW 5326, 5828. Berneker 2.17. we oe capa, te late Lat. cappa Mia ists fc overing’ (Isid.), whence vith caput ied (6.55), connection kappe, Sy a dub. Hence also Dan. Another = aA poet MLG kappe). ‘dpa, Dan, kaabe ie ee ON
’ cape, NE cope, OFr. cape). Ernout- i 1162. REW 1642. etym,? eee lenn, Gall. linna),
It, Nin bray roe, Stokes 252, Tedesen ig), Pt ‘cloth’ (6,21),
+ Coe,
Il, fr tile “ - Ir, cochul] ‘cowl’, fr. Lat. * Cwewll ‘eory], chasuble’)
igitized by Arya Samaj Foundation Chennai and eGangotri
\
NG PERSONAL ADORNMENT AND CARE 417 ING;
‘cap, hood’, orig. dub. Walde-H. 1.298 f. Pedersen 1.227.
4. Goth. wasti ‘garment’, pl. ‘clothes’ (6.12), commonest word for tyar:ov also where it means ‘cloak’ (as Mt. 5.40, Lk. 6.29).
Go
```


## [2026-09-07T15:51:17.866Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v4 pdf page 73 (printed 1990) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==73' incoming/BQT/BQT_v4_pages.txt | head -80"
}
```


### [2026-09-07T15:51:19.164Z] TOOL RESULT

```
=== BQT v4 pdf page 73 (printed 1990) ===
[pdf page 73]
مرظب -۱۹۹۰-
وآن زباده از نیم شبراز زمین بلند وبفایت سبز | اطیر خوانند ۴ - وکنابه ازآفتاب هم‌هت 8 -
و خرم و درهم روییده باشد ۱ - و لام آشهری | و پنجهٌ زنجبیل را نیز گفته اند یمنی پارچه ای
و مدینه‌ای هم هت ۲ - وعربان خلطیدن ستور | از زنجبیل که چاد شاخ داشته باشد .
راکویند در طفزار وتمامکیاء وطلف را چریدن مرغاب « بنم اول بروزن سرخاب .
وخوربن ۴ - و بفتح اول و ثانی » هم دراعرمی نام رودخانه ات که از پپلوی مروشاهجان
آب دهن راکویند ۴ - وبضم اول وسکون‌نانی» | میگذرد وآنرا مرورود هم میگوبندیمنی‌رودخانهٌ
معروف است که مطلق پرندگان باشد و عربان | مرو ‎٩‏ .8
۱ - ر4 : مرغزار » معرب مرخ « مرج » » اوستا- ۳387884 ( چمن ) » آرمنی ع
8 (چین) » سربانی ع 462۹۲27 (چین)»کردی ۰۲۵1۳۴ ۳336۲802 (چمن)
« اسشق ‎٩۷۵‏ قاط » ورك : هوبشمان ایضاً . درعربی نیز « مرخ » «منتهی‌الارب» آمده :
بله کرد ازآن سوکه بود آب و مرغ پیت از بر دامن ربگه ورغ .
و رك : مرغزار . آسدی طوسی « لغت فرس ۲۶۱ 4.
۲ - مرغاب ( بفتح اول) قربه‌ایست ازهرات وازقرای مالین - ونام نهری بمروشاهجان-
و لهری بسره «ممجم‌البلدان» رك:می‌غاب- « مغ سپید » موضمی‌است درهرات. رك : چهار مقالةٌ
عروضی‌طیم نگارنده س٩4‏ . ۴ - مرغ بالفتح » آب دهان روان»... گیاه ترچریدن, جای
کرفتن درکیاه و غلطیدن درآن « منتهی‌الارب >. ۴ - پپلوی 32۳۷ ( پرنده » مرغ ):
اوستا 339798108 ( پرنده » ماکیان ) « بارتولمه ۱۱۷۲ * « نیب رکه س ۱۵۳ ۰ نیز پپلوی
۲85 , هندی باستان -12788 ( حیوان جنکلی » مرغ ) » قس : کردی 1331۳21۷1 (اردك).
افغانی ۳2788۸ . استی 122۳80 . ( پرنده ) . بلوچی ع (9) 22078 ۰ 1331۳80 ( پرنده »
مرغ خانگی) » مازسرانی ۳38788 « اسشق ۹۷۵ > - درفارسی نیزبمعنی مرغ خانگی(ماکبان)
استممال شود .
* - نو دعی سبح را شب افروزی روز را مرخ و مرغ را روزی .
نظامی کنجوی « کنجینةٌ کنجوی ص ۱۶۲ *.
‎٩‏ - باین معنی در ممجم‌البلدان بغتح میم‌آمده‌است ولی مینورسکی ۸117813410 ضبط
کرده‌است ر4: ترجمةٌ حدودالعال. فهرست .- مرغاب جنم‌ميم مر‌کز ناحیتی‌است بنام مشهدمرغاب
در فاری۷ بفاصلةٌ 2۸ کیلومتری استخر و بکی از قرای آن مشهد مادر سلیمان است . «کیهان .
جغرافیای سیاسی ص ۳-۲۲۲ و رك : ح۲.
۶ مرغالی - بنم اول » از : مرغ ۳ آبی ( منسوب
به آب ) » زباکی 33۳882۷1 ( اردك) « کربرسن ص۸۷ > ۳۹
کیلکی 1ط3طع ۳ ( مرغایی ) » نوعی از پرندکان پرده‌دار ۹
که قم اهلی آن اردك است . و غالباً در آب زندکی میکند . ۳
منقارش پهن و درکنتاره دارای قیغه های ریزبست که آیرا ماش
الك خارج میکند و ذرات غذائی را نگاه میدارد . مرغایی
```


## [2026-09-07T15:51:40.282Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v4 pdf page 97 (printed 2014) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==97' incoming/BQT/BQT_v4_pages.txt | head -70\necho\necho \"=== faseng variant ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==97' incoming/BQT/BQT_v4_pages_faseng.txt | head -70"
}
```


### [2026-09-07T15:51:41.622Z] TOOL RESULT

```
=== BQT v4 pdf page 97 (printed 2014) ===
[pdf page 97]
مشقولیه -۹۱۸-

مشقولیه ۱ - با قاف ولام بر وزن مشاک بیف ؟ - بنم اول . بمستی بید

کردونیه , نام مادرزن وامق باشد و وامق عاشق | معك است - وبمعنی‌عود هم بنظرآمده است8 .

عضرا بود » و قصهٌ وامق و عذرا مشهور است. مشك دانه - بنم اور دانه ای باشد
مشگ » بکر اول وسکون نالی وکاف | خوشبوی که‌آنرا سوراخ کنند و برشته کشند -

فارسی ۰ ممروف لب و نام لحن بیست ودویم است ازسی‌لخن بارید۹ ؛

است . کوبند ناف ۹ وبکس اول هم‌آمده است .

آهوی خطائی است ۱ مشکدد ۷ - بفتح اول و دال اد

و عربان مك اه و که و سکون ثانی و ثالت و رای قرشت » جانورست

خوانند؟ ‏ بامین واه که معك و خيك آب را پاره و سوراخ کند.

وی اول, 11 مشگد۴ - بنم اول و فتح دال ابجد

پوست مفندی

باشد که‌درست کنده ری وسکون میم در آخر جانوری باشد سیاه رنگه

باشند خواه دباغت در غایت خوش آوازی -

8 8 3 ۸ب

شده باشد وخواء سقاه ومعك‌او همشکر ‎٩۸‏ - بفتح اول وکسرتانی, منع

شده باشد و درآن ماست وآب کنند ۴ . از شکار کردن است پعتی شکار مکن چه شکر

۱ مصحف « معشقولیه , زن پدر وامق بود . عنصری ( بلخی ) کوید :

زن بد کنش ممشقولیه نام یوش جز از بد دگر هیچ‌کام .>

« لغت فری اس ۵*۹۱ .۰

۴ - سانسکریت 71182 مسفر 77388 (موش). بونانی1330816058 ,لاتینی 10186018.
فرانسوی و انگلیی 13186 ۰ عربی مك ( بکر اول ) . غیاث کوید : اهل فاری بکر میم
واهل ماوراءاانعی پم میم خوانند . در نسخهٌ ترجمان‌البلاغه مکتوب بال ۵۰۷ قمری مشك جنم
اول ضبط شده ( رك : ترجمان البلاغه چاپ احمد آتش » بخش عکسی ص 4۷ب و۲۵۱ الف )

و با کاف تازی اسح است ؛ وآن مادهاست مأٌخوذ ا زکییه‌ای مشکین باندازة تخم مرغی » متفر
در زیر پوست شکم آهوی ختابی (غزال السك < 0106۲ 8391) نر» وفتیکه تازه باشد برنگه
شکلات ولزجچ است. اما خعك‌آن صورت گرد دارای طعم کمی تلخ وبوی تند است . آنرا بعنوان
اسای‌بسپاریازعطریات بکارمیبرند . رل : 1816۳8,10161 /370۲ ۷۷۵10916718 ور: تحقةحکیم
مژمن: مك - ۴ - در پهلوی 1322886 ۰ وآن اسلا بمعنی چرم (مخصوصاً چرمی که در
آن‌آب ریزند) وسپس‌صورت « معك اپرزین » درپهلوی ( رسالةٌ خرو کواتان بند ۱۰۳طبق چاپ
جاماسب اسالا) درآمده بمعنی خيمة سلطنتی, وهمین معنی‌است که درفارسی «مشکو» و «مشکوی»
شده (ازافادات شفاهی استاد هنینگه) در سغدی ۳98067. (مشك اپرزین881-2027288)
رد :. ۹۹۹ 11 .00 ,م2 ,0۳۵2|01 #نط۸۲ و6 . 8
6 . دبقعنفعد5 , وعندد11 ۴ رك : بید مغك. 8 -آنچه دربرهان بمعنی
عود نوشته , اصلی ندارد ( سراج اللغات بنقل فرهنگه نظام ج‌ه ص م ) - ‎٩‏ - درصورتی
که نظامی کنجوی درخرو وشیرین برای الحان باربدیآورده , لخن‌دهم است :

+ چو برگفتی نوای مشکدانه خت ن گشتی ز بوی مشك » خانه .
نظامی کنجوی * فرهنگه نظام > . ورلك : جمال‌زاده .آوازهای قدیمی ایران . مجلةٌ موسیقی ۲:
۷ سوق ۷ - از : معك( بفتح اول )در (درنده) . ۸ - هی از «شکردن»
(م.) و « شکریدن » (همم.)


=== faseng variant ===
awk: cannot open "incoming/BQT/BQT_v4_pages_faseng.txt" (No such file or directory)
```


## [2026-09-07T15:52:09.564Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD mašk ===\"\ngrep -n \"mašk\\|maSk\\|mask'\\|mškw\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== PHD marg ===\"\ngrep -n \"^marg\\|marg \" PHD.txt | head -20\necho \"=== NYB ===\"\ngrep -n \"mašk\\|marg\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T15:52:09.639Z] TOOL RESULT

```
=== PHD mašk ===
PHD.txt:164:abarmān [5/mn'] in charge. abarmānd ['pín?nd] inheritance, privilege. abarmānīģ [%n?nyk!] noble. abar-menišn Pf/myn$n'!] proud, haughty. abarón Pf*/xwn! | N wárün] contrary, wrong, sinful. ~ih: sin. abar-6z PóPeoc] stronger. ~ih: mastery. abar-tan [Pltn'] arrogant. ~th: arrogance. abarwēz Pfltvyc | (M *bruyj, N parwéz)] triumphant, victorious. ~ih: triumph, victory. abarzén, v. zmašk, abaxs [hš] repentant; regret. ~ЛЬ : repentance. abaxšāwand [5hP^wnd] regretful. abaxšāyīdan, abaxšāy- [5APd-ytn! | М ?bxPy-, N baxšūdan, baxšāy-) forgive, have mercy on. ~išn: mercy, forgiveness. ~i&nig : forgiving, merciful. labāxtar [*5?*4tl | M 7b’xtr] planet. žabāxtar [PP’htl | (N bāxtar ‘west’)] north. abaydag Pyrťk', v. paydag | M ?byd?g] invisible. ~th: invisibility. abày- : abayéd ['yt' | M Maud, N bāyad] it is necessary, fitting; must (+ infinitive). ~ist Pf?dst' | N bāyist] it was necessary. ~istan [?P?dstn!] be necessary, fitting; desire, want. ~išn: necessity. ~išnīg : necessary, fitting, seemly. abāz [L AWHL < A lI2(w)hr;?Pc | М Рс, N baz, wa] back, again, re-. ~ айдап б: attribute, ascribe to. 7 appoint t= ~ dāštan: withhold, restrain, prevent. ~ ēstādan az: abandon, desist from. — kardan: open. — kardan az: disengage from, wean. ~ mándan: remain behind. ~ pádan: remain, stay. — raftan : issue, go forth. ~ waštan O: turn into, become. ~ wirāstan: rearrange. abāzsār [LAWHLs'I] rebellious. ~ih: rebellion. āb-čihrag [$ cyhlk'] holding the seed, essence of water. abd [>24 | М "Gd J ?bd-] wonderful. ~ sahistan: seem wonderful (to) > marvel.
PHD.txt:461:īmašk [msk' | N ~] mussuck, skin bag (for liquids).
PHD.txt:462:2mašk [mšk! | N maškē] tent, pavilion. ~abarzén [-!pizyn! | M mškbrzyn] royal pavilion.
PHD.txt:463:maškīzaģ [mfkyck' | N ~a] small mussuck, skin 'table-cloth'.
PHD.txt:2874:mussuck mašk; small ~ maškīzag.
PHD.txt:3059:pavilion kēšk, mašk; royal ~ mašk- abarzēn.
PHD.txt:3685:skin Carm, dawāl, pēst; tēz; (a.) post- én; ~bag hambān, mašk; ~ 'table- cloth! maškīzag.
PHD.txt:3924:table xwān; ‘table-cloth’ maškīzag.
PHD.txt:3950:tent mašk, wiyān.
PHD.txt:4823:[140] mastog 19112256 mehtar Vess mastarg > e26 mizagūmand 2061” 406 mizagdārīh AAS 3G mizag 1.5 0G rūynī NINE maškabarzēn NS ey wi? makkizag 1923 556 1-2mašk way deh! ATES dehgiin! uses madār У. о mih мес madan, 1-3mihr мео
PHD_mackenzie.txt:5991:association hamih, nisast.               bag, skin - hamban, maSk.
=== PHD marg ===
130:delete ozarak ... padist ... add threat. pad-nigerián ... for cared for, guarded read carefully. add  parisp [plsp | M prysp] wall. ?pid ... add (M pyt). purnay [pwin'd = Av. pərənayu-] adult. add  purr-marg |-mlg| deadly, baneful. raz ... add M rz. add rebas [lyp's | N ~] rhubarb. ?ristag ... add N rasta. add гох [lhw' | N <] rook, castle (chess). sahistan ... read (M shyd, P s‘y-). add sārwār [s ]w I helmet. add  sayistan, say- [ŠKBHWN-tn < A Vškb | P sy-] lie down.
189:áhüg [TYBA < A ру; ”hwk! | MQyhwg, N āhū] gazelle. ahunawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y < А k-zy | М hy] soon(est), first. ajģahān [>20/?л! | М ieikin, N azgahan] lazy, indolent. “АҺ: laziness, indolence. ak P! | N dk] evil, harm. -ak LIN ~] diminutive suffix. a-kámagómand [k mk’ wmnd] unwilling. a-kanārag ['kr?]k! | M ?qn’rg] unlimited, boundless. ~ih: boundlessness. a-kard Pārt! | (M °gyrd)] not done, undone. Akoman ['kwmn! | М ?qwmn] Evil Thought, an arch-demon, akómand ["£wmnd] evil, harmful. alā [Py] oh! alas! Аар [STLA, STRA < A £t ;?lk! | (М rel side. alálag PPH! | N lala] anemone. ālāy-, v. ālūdan. Aleksandar Piksndl | M *Ixsyndr, N Iskandar] Alexander (of Macedon). almās(t) Pim?s(t') | (M ?rm?s), N almas] steel; diamond. аадар [?/wtk'] defiled, polluted. АҺ: defilement. ālūdan, ālāy- Photn!, *Pd- | (M ?rwd), N ~] defile, pollute. Aluh Plwh | M "If, N ~] eagle. Xum [lum] millet. N~ amā [LNE < A l-nh | М ?*°h, N má] we, us. Amadan, āy- [Y ATWN-tn! < А y twn, V*th | M?mdn,?y-, N ~] come. amahraspand [?mhrsbnd | M (?)mhr’spnd] a Holy Immortal, a-mar [ml] countless, innumerable. amar [ml | N ~] reckoning, consideration. āmār- [?m?1-] reckon, calculate. ~išn: reckoning. a-marag [mlk') countless. amaraģān [?mlk’n'] generality, commonalty. ~ig [-yk'] general. ~iha [-yh’] in general, generally. a-marg [mig] deathless, undying. ~ih: deathlessness, immortality. ámárgar [?m’lgl | N ~] reckoner. amāwand [?m'wnd] powerful, strong.
4847:mazgit mizné may magas padīr-! padīrišnī padiriftant magind makog 1-2mar marg margomand margarzān margīh
=== NYB ===
376:a-marg
386:a-marg [mlg] undying, immortal 59", 774. 1049. — V. marg.
388:a-margéh
390:a-margéh immortality 106??,
505:lapar [’pl; MDM, v. 2apar] adj. situated above, lying above: évak ~, apäk dit, v.s.v. žapāk (2); — heavenly, often in compounds: apar-apükeh etc., v. below; comp. ~-tar [’pltl] higher 5426, 581°, highest 1097; sup. ~-tom highest 415. 102°; v. also apartaréh; — adv. empha- sizing an adj.: highly, extremely: apar- aržānīk, v. aržānīk. — Av. (393) upara-, adv. upara (instr.), uparam; MPrth ’br adj. and adv. (MHC), comp. ’brdr, sup. ’brdwm; Ps. ?pldl; Paz. awartar, awardar (SGV); NP bar ‘height, top, summit’, bartar ‘higher’. ?apar [MDM, erroneous reading of OAram QDM] 1. adv. above: (3 päs) i-m guft ~ of which I spoke above 65°; či nümak" cé hac ~ nipišt" éstat the inscription that had been written here above P2:3, cf hacapar; — prev. over, on, upon, up, or simply expressing the initiation of the action, with varying vbs., cf esp. (@)ma- tan, burtan, grätan, raftan, rasitan ; follow- ed by enclitics: apar-p-im ravišn I must needs ascend 4076, v.s.v. -p(i); — refer- ring back to an encl. pron.: api-š Vidrafš . ~ mšast and V. got on it (the horse) 25W5; cē-t avdom margéh ~ raset for at the end Death will come upon thee 726-7; (martömän) tāi-šān āmēcišn ~ nē barend as long as one does not impart instruction to them 801. — 2. prep. a) local: over, on, on to, down on: Krisäsp ~ én damik raset K. is roaming all over this earth 3318; ~ giyāk on the spot 3", 102; ~ ki Zartuxst bé dahém where we shall deposit Z. 3957; ~ pad ēstāt rose to his feet 1821; asp ... — rahy vartét harness the horse! 5418-14; srišk ~ srišk drop after drop 214
1117:cê [MH; cyh 12111] 1. interrog. pron. what? 59. 726. 89? ete.; how? 1513, 51?!; with prep. 6 cé, pat cé, hac cē; cé rād? why? 351! ete.; combined with a subst.: ce zaman? 715, cē gah? 722; pat ce āivēnak? how? 76%; cé vinäs? 121, cē vat? 7322, etc. ; apar cē ātvēnak margēnītan i Zartuxst pursit how to kill Z. 4912-25-26, 4813-14 (apar governs the whole clause). — 2. rel. pron. what: či ndmakY ce ... nipištv estet, ce Šahpuhr" . . . framätY nipigstany P 2:3-4; kart" ... ce ... sahät P2:8-9; har ce 61.3218, 86%. 9618; ēt ce ... apāc āvurt 11214715; 361; pat hàn cim rād ce 121". — 3. conj. a) subordinating: because 105); ce ka id. 991. — b) coordination: for 2$. 619.22. etc., passim. — MH 305 wrong ideogr. for encl. -c(%). — < cahya, gen. sg. of Av. OP (422 sq.) ka-.
1220:dāštan [d'štn'] dār- [YHSNN-; d'1- 217. 281. 10014. 10279], imp. sg. with encl. pron. där:om [YHSNN-m] 6t; opt. 2nd p. sg. dārēš 41!?; pt. dašt = pret. pass. 3d p. sg., construed as an act. form 495-5; to keep, to hold, to sustain, to maintain, to have, 8?! and passim; — with an adj. as a complement of the obj.: Sahpuhr kanicak āžarmīk u garamik däst Š. kept the girl honoured and respected 163-4; 225 ete. passim; the complement some- times comes near to an adv., e. g. véh ~ to keep, handle a th. well 5026-27, and may be replaced by an adv.: én zan garämikihä ddr 1024; 6415; — with an obj. and pat + an adj.: to consider a p. or a th. to be ...: pat margaržān ~ to consider a p. guilty of death 1014-19; 6398-9, 8017, 839-19; pat azateh (cas. obl. sg.) där-om! consider me as a free (wom- an) — release me (from slavery)! 64, v. s. v. Gzat; — pat & ~ ku to be of the opinion that, to think, imagine that 2525, 982-3, 3227 sq. 5012-13, ef NP pindāštan < *pa(t) én daštan; pat ce dārēh how do you regard (the case mentioned in the preceding kū- clause)? 105-$; pat depahr, pat nihän
1426:3.8 [the figure l; -’y, -y, -yh] the enel. indef. art.: tigr-é [-1] 339; duxt-ē [BRTH- ^y] 14%; gad-ē [gt'-”y] one stroke with the mace 312°, 4 ēvak-ē [HD-wk!-y] one fourth 998; vāt-ē [-1] 4 hubod 73°; hec ctš-ē [-l] nö 16%; har kas-ē PYS-1] 10018; and cand yašt-ē [-1] 651°; pat har 40 sal hac zan-ē u mart-é frazand-é [al -ē's spelt -1] zāyēt every forthieth year a child is born of a woman and a man (= of one couple) 8622-23; 6 artestäreh for 6 artēštār-ē 4517. — Identical with ?e; MPrs ‘yw placed after its subst.; Paz. -é, NP -é. — The spelling [-1] is sometimes erroneously used for other suffixes -é: mēd4-1 = mode cas. obl. 72??; har marg- arzanik+-1 = -aržānīkē for the abstr. -arzanikéh 10199.
2095:*hu-vaxm [hww’hm] “of good swing", epithet of the varz ‘mace’ (v. vazr) carried by Keresāspa 100%. — Renders Av. (1832) hu-nwiata- "well swung’, epithet of the vazra- of Mithra (Yt. 65. 10132) and of the vazra- in general (Yt. 10%. 1372); < m + vaeg-, v.s. v. ?vextan. Reading hypothet- ical, no Paz. reading being known to me. I take it as *hu-vexm < "hu-vataman- from *véxtan < vaig- (q. v.), which has been largely confounded with !vextan < vaik-; *huvērm > hu-vaxm (or perhaps better *hu-vahm) cf s. v. mahmän. As to véxtan as a battle term cf 254. — As Bthl (Wb 1832) has given quite misleading information about the Phl. w. I put here the notice he quotes in its correct form. It is found in the Phl Xvaršēt ntyāyišn (= Yt 6) in Zand-i Khürtak Avistäk ed. by Dhabhar, p. 21 $ 15: ké yast Ohur- mazd % amarg api-š yast Mihr 4 fragoyot . . . (l. 14) api-§ yast vazr i *hu- vazm | pat kamär apar i dévan | i Mihr frägöyöt (e: *huvaxméh € ku bāstān eton dàret: mēnēyīhā be šavet, vināskārān pã- tifrās bē kunét, u menöyihä apäc 6 kantir äyet) ‘he who has worshipped Ohurmazd the Immortal... has (at the same time) worshipped Mihr (the god) of wide (l. 14) and he has wor- shipped: the mace of good swing on the skulls of the devs, owned by Mihr of wide pasturages (its being “‘of good swing" means that it constantly behaves in the following manner: spiritually it goes off and punishes the sinners, and spiritually it returns to the quiver [sheath?])? NP v. xub nihädah, Skr. v. su-niyukta (Dhalla, The Nyaishes, 1908, p. 50). l
2127:kart ēstēt, cigön Dahäk u Frāsyāp u Väman [thus Cod. DH; TD w’tn', Paz. vätan, perhaps for Väöarjä the father of Vaman, Tab. I, 530 init.] u apārīk hac én āivēnak marg-aržānān, pātifrās [+ Paz. vama, probably a misspelt Vaman] 10 ātvēnak-ic vitārēnd ‘those who have in- stituted their own *laws for mankind, as D. and F. and V. and other death deserving men of that kind, will undergo ten sorts of punishment’. For the whole passage cf Phl Vd ad 75? (p. 279).
2164:*kai-bāg [kdb’(g)] “having share with the kat", "sharing with the king" = co-regent 221’, v. also ném-vécak. — Coin- cides graphically with KDB’ = drag ‘lie’, which is sheer nonsense in this context. Np kiyd ‘a king, protector; a lord, a margrave’, also n. pr.
2441:marg [mlg] death 1?. 824.25, 93, 113-6, — Av. (1146) mahrka-; MPrs mrg; Paz. NP marg ; v. also margéh.
2442:marg-arZän [mlgle’n'] worthy of death 108,13.18; subst: pl. cas. obl. —-än 1219, 101’; — (pat ~ druvand evil in so far as worthy of death = through deadly sins,
2446:marg-aržānīkē [~-yk+1] deadly sin 101, — Cf the spelling mlgle’n'+1 = marg-arzané(h) in the commentary to Vd. 73? (p. 27799).
2447:margéh death 481, 5114. 64!. 726. 7721; penalty of death 45%.
2448:margénitan [~-ynytn'] to kill 4321-22, 4893.13.24.
2477:marz-pän [mlep’n'] governor of a border district, margrave 1*. 115°. 117’. — Av. (1153) maraza- ‘border district’, MPrth mrz (A-H III, BBB) + pin ‘protector’, v. pünak; borrowed in Arm: marzapan, in Aram: Syr marzbänä = Talm, and in Arab: marzubün; NP marzbün.
2492:tmašk 2126, 221: restore the reading myhk' = méxak, g. v.
2493:"maškar enemy, the probable Ir. eguiva- lent of OAram Š'NH = SANE ‘hater’ 12812; inFrP 14 ~ is the Ir. equivalent of MSN’ = MSANNE, pt. Pa‘el of the same vb. in its recent form with S instead of S. — In all probability the same as Av. (1153) maršo.kara- left without trans- lation by Bthl, but certainly ‘killer’, one of the three epithets of Verethraghna Yt.. 1428: maršo.kara- arsö.kara- frašo. kara- which correspond to the Milr. epi- thets of Zurvàn: asögar frašogar zarogar, the last meaning 'making weak, slack' and rendering marsö.kara-. Ci Nyberg, . JA 214, 1929, 240, 219, 1931, 86-91. OIr marša- must then mean 'weak' slack’ (etymology obscure; to be com- bined with Skr mrs-. v.s. v. framoš?) and maršo.kara- ‘making (the limbs) slack’ = ‘killing’, ef Hom. Xdot oi yvia ‘he
2548:mčxak [myhk'] headguarter, the king's tent when the camp of his army is pitched 2126, 221, — This is the reading of J.-A. after his MSS, and there was no reason to replace it by [mšk'] mašk, as I un- fortunately did in the text, following the example of Pagliaro and others. The emendation goes ultimately back to Geiger, the first who worked on the text
```


## [2026-09-07T15:52:24.834Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD meadow ===\"\ngrep -n -i \"meadow\" PHD.txt | head\necho \"=== PHD marw/margzar ===\"\ngrep -n \"marġ\\|marg \\[\\|marw \\[\" PHD.txt | head\necho \"=== BRT marəγa ===\"\ngrep -n \"marəγa\\|mareγa\\|marəγā\\|maregha\\|marəga\" BRT.txt | head -20\necho \"=== BRT Wiese/marg ===\"\ngrep -n \"marəy\\|marəγ\" BRT.txt | head -20"
}
```


### [2026-09-07T15:52:24.926Z] TOOL RESULT

```
=== PHD meadow ===
555:rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
2754:meadow ray; v. pasture.
=== PHD marw/margzar ===
189:áhüg [TYBA < A ру; ”hwk! | MQyhwg, N āhū] gazelle. ahunawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y < А k-zy | М hy] soon(est), first. ajģahān [>20/?л! | М ieikin, N azgahan] lazy, indolent. “АҺ: laziness, indolence. ak P! | N dk] evil, harm. -ak LIN ~] diminutive suffix. a-kámagómand [k mk’ wmnd] unwilling. a-kanārag ['kr?]k! | M ?qn’rg] unlimited, boundless. ~ih: boundlessness. a-kard Pārt! | (M °gyrd)] not done, undone. Akoman ['kwmn! | М ?qwmn] Evil Thought, an arch-demon, akómand ["£wmnd] evil, harmful. alā [Py] oh! alas! Аар [STLA, STRA < A £t ;?lk! | (М rel side. alálag PPH! | N lala] anemone. ālāy-, v. ālūdan. Aleksandar Piksndl | M *Ixsyndr, N Iskandar] Alexander (of Macedon). almās(t) Pim?s(t') | (M ?rm?s), N almas] steel; diamond. аадар [?/wtk'] defiled, polluted. АҺ: defilement. ālūdan, ālāy- Photn!, *Pd- | (M ?rwd), N ~] defile, pollute. Aluh Plwh | M "If, N ~] eagle. Xum [lum] millet. N~ amā [LNE < A l-nh | М ?*°h, N má] we, us. Amadan, āy- [Y ATWN-tn! < А y twn, V*th | M?mdn,?y-, N ~] come. amahraspand [?mhrsbnd | M (?)mhr’spnd] a Holy Immortal, a-mar [ml] countless, innumerable. amar [ml | N ~] reckoning, consideration. āmār- [?m?1-] reckon, calculate. ~išn: reckoning. a-marag [mlk') countless. amaraģān [?mlk’n'] generality, commonalty. ~ig [-yk'] general. ~iha [-yh’] in general, generally. a-marg [mig] deathless, undying. ~ih: deathlessness, immortality. ámárgar [?m’lgl | N ~] reckoner. amāwand [?m'wnd] powerful, strong.
455:mand [mnd | = M] house. miindag [m?ndk! | M m'ndg, N ~a] tired; remiss; fault, sin. “Аһ: tiredness. māndan, !màn- [K TLWN-tn! < A У ktr | M mnd, N ~] stay, remain; v. also % *mán-. mang [mng] henbane. mänig [mnyk'] household member. mānistan [{KTLWNstn'] = mandan. māništ [m?nyst!] abode, dwelling. ~ag [-k'] sedentary, settled. mānsār [mnsl = Av. ma0ra-] (holy) word, spell. -~-bar [-b/] priest. ~spand [-spnd = Av. spanta-] holy word; v. máraspand. imar [ml | M mr, N ~] number, reckoning, account; class. *mar [m/] scoundrel, felon. таг [ml | N ~] snake. mār-, —išn, v. mārdan., тагар [mik!] number. тпагар [mPk!] perceptive, sensitive. Māraspand [mrspnd | N ~] (= máns?rspand), cal. 29th day. *martabuk [mic”5wk'] brave, valiant. ~ith: bravery, valour. mard [GBRA < A gbr; mlt' | M m(y)rd, N ~) man. mārdan, màr- [ml-tn'] perceive, notice, feel. ~i$n: perception. „išnūmaud [-£rwmnd] perceptive. mardanag [mit?nk! | N ~a] manly, brave. ~ih: manliness, bravery. mardóm [ANŠWTA < A?niwt?; mltwm | M mrdwhm, N mardum] man, mankind, people. ~th: humanity, humanness. mardóm-zàádag [mltwm 2tk' | N mardum-zād] human being. ~ih: humanity. marģ [mlg | M mrg, N ~] death. ~-arzan [-lc’n'] deserving death. ~ih: = marg. --0mand [-”wmnd] mortal. mārīģ [m'Lyk! | M mryg-] word, spell. marw [mlw! | M mrw, N —, (mary)] herb. marz [mlc | M mrz, N ~] boundary, march; astr. term. marzanģēūš [mlengws | N ~] marjoram. marzidan, marz- [mlc-ytn! | М mrzyst, mrz-] copulate. išn(īh): copulation, fornication. marz(o)bàn [mlcp’n' | № ~] margrave, warden of the marches. -masāy [-ms'd] suffix, -sized. mast [mst! | = M, N ~] bemused, intoxicated.
=== BRT marəγa ===
=== BRT Wiese/marg ===
```


## [2026-09-07T15:52:37.128Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT size/Wiese ===\"\ngrep -c \"\" BRT.txt\ngrep -n \"Wiese\" BRT.txt | head -20\necho \"=== BRT mərəγa bird ===\"\ngrep -n \"mər̥γa\\|marǝγa\\|mərəγ\" BRT.txt | head\necho \"=== BRT cols 1146-1160 region: grep 'marəz' ===\"\ngrep -no \"mar[əeǝ][gγy][a-]\" BRT.txt | head -20"
}
```


### [2026-09-07T15:52:37.241Z] TOOL RESULT

```
=== BRT size/Wiese ===
30725
8471:'  'um  "ranqm  uzuxfyenlinam  srlranqm zairi^aoiianqm  vaxsA  (sd.)  apayasaite  V. /Ä63;  Yt. /Ä6;  —  at  aRyäi  (näml.  dem Rind)  mazdä.  'rä  vaxiaj  (sd.)  Y.4S.6;  — avi  racynyq/H  varauhmt  azuitlmca  'ranam Yt.  ^2.3;  —  nima  'vaire  (VS.)  varMhi masdaöäte  asaone'V.  ig.ii;  Vyt.22,  N.7/, f)7.  a)  Plut.,  im  Gegens.  zu  alxa-  Plur., 'pflanzenbewachsener Boden';  ahond  una 'rlhuca  paiti  *baooisca  vTdtnanmnS  saoa- yäti  . .  ärvatS  urva  *aexahuea  (sd.) . .  "der Seele  des  Gläubigen  ist  es  so,  als  ob  sie auf  Wiesengiund  (stehe)  und  Wohlgerüche empfinde,  .."H.  2. 7— 25.  b)  sva, 'Baum', a)  im  Gegens.  zu  var^ä-.  pairi  van>'>iJ- byasca  'räbyas^a  atsmaiibyS  (sd.)  V.  16. s.  ß)  sonst:  v3r»ynahe  . .  yS  .  .  sainif marisat  'ranqm  ". .  der ..  im  Flug  der  Bäume Wipfel  streift'"  Yt./.4.2i''.  c)  'Pflanzen- Stengel,  Reis':  yavat  akmUi  paitinqm •ranqm  aetavat . .  "so  viel  es  ihm  einzelne Reiser  gibt,  (als  ob)  er  so  viel  .  ."  V.  iV. 86,  a)  bes.    der   zum  Barisman    ge-
17418:•  j.  by-ä'rixti  Inf. 'bis  irrigare,  (das  Wasser) zweimal  hin  (zur  Wiese)  zu  lassen,  über  zu lassen':  &aj  yaval  zä  .  .  yavat  ai^a  a/s 'ü  upa.üjvariii  frabaväi  "wie  gross  (soll) das  Grundstück  (sein)?  .  .  so  dass  das Wasser  (des  Grabens)  ausreicht,  um  zwei- mal (im  Jahr)  vermittelst  Durchstechens (des  Damms)  übergelassen  zu  werden"  V. ! /4.13'^    ,  ,      I
20015:•  j.  mar»yä-f,'Wiese':^^ära  'fa  avastaya ",  .  leg  Wiesen  an"  V.  2.  a6.
20016:np.  man  "Wiese';  s.  dazu  Hbu.  ZDMG.  46. 244,  JusTi  ZDMG.  J7.  245,  NB.  14b.  —  Pü.:
23551:land, -grund,  Wiese';  yascä  °rS  vJVäpaj (sd.)  Y._J2. 10;  —  yai^a  a^a  ga%wa  mit \  ma%ime  \yä\  're  [vä\  frajasäl  ",  ,  mitten auf  einer  Weide  .  ."  V.  ;5. 4i'>;  —  yj ^wal  . .  yaeäi  afiä  . .  giuscä  "rät  aRstgnt mantüm  (sd.)  Y.jj.  4;  —  at  hvS  a^ahyä anhat  vanhiuila  'ri  mananhn  "der  wird (dereinst)  auf  der  Weide  des  A.  und  des VM.'^  sein"  Y.jj.  3;  —  yj  ahmai  gqm . .  hSiiutalal  ai  hsi  'rät  rämä.dä  ärmaiton "der,. geschaffen  hat,  aber  zu  dessen  (des Rindes)Wetde-"dievfrM.(Erde),(ihm)Frie- den  gewährend"  Y.  47-  3-  3)  'Weide- wirtschaft', Uberh.  'Landwirtschaft':  rtifij urvähs  dätsibyascä  karapanS  'rät  arSm (sd.)  Y.5/,  14;  —  nSii  htm  masn(sd.)  aSil 'r3m  frädai^he  Y.  4^.  30;  —  hScä  nä fiümS  , .  aiwyilxsayatü  hadä  asäcä  'räcä Y.  sS-  4-         [N.  Sy,  F.  5:  lies  vasf.]
23574:•  j.  viströ.dätainya-  Adj.  'wofür  die Futter-,  Wiesenmahd  bezeichnend  ist',  von MaihyBiüma  (sd.):  mat^iySiÜmtsm  'tainltn Vr.  2.  3;  —  maihysisimahe  'tainyehe  Vr. /.  3.
=== BRT mərəγa bird ===
=== BRT cols 1146-1160 region: grep 'marəz' ===
```


## [2026-09-07T15:52:46.661Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '20000,20030p' BRT.txt\necho \"=== leaf ===\"\npython3 - <<'EOF'\ndata=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n')\n# find leaf index containing line 20015\ntarget='mar»yä-f,\\'Wiese\\''\nleaves=data.split('\\f')\nacc=0\nfor i,l in enumerate(leaves):\n    n=l.count('\\n')+1\n    if acc<=20014<acc+n:\n        print('LEAF',i)\n        import re\n        print('numbers:', re.findall(r'\\b1[01]\\d\\d\\b', l)[:20])\n        break\n    acc+=n\nEOF"
}
```


### [2026-09-07T15:52:48.059Z] TOOL RESULT

```
Zum  V.  mank:  —  Pu.:  markih.  —  >)  In  der Hds.  'iaiim  gescbc.
•  j.  mahrkaO'äi  Inf."  'zu  verderben,  zu nicht  zu  machen':  y(ä3t  aiwiat  jaymat aSavatam  m'  aom  a^jymca  stfm^a  Yt. ig.  12;  —  tard^ustrim  yim  . .  na^a  vXspe ..dafva  M°   upadarinvainH (sä.)  Yl<¥.44.
Zum  V.  mar/i-,   —  Vgl.  inahrka%a..
•  j.  tnahrkäi  Inf.  'zu  töten,  zu  verderben': hr^rsi  asahe  gaikanqm  .  .  m"  asahe gaehanqm  Yt/p.  48-50;  —  yqm  fraÜ'a kprmtat  anrS  mainyul  . .  m'  afahe  gas- haaqm  Y.  p.  8;  —  naia/cit  ai^hs  yässiti syänai  .  .  fOit  m'  Y.  6$.  11.
Znm  V.  mant:  —  Vgl.  mahria-.  —  PQ. :  (Ja)
dby  Google
"47
mahrko.tvma-
•  j.  mahrkö.tama-  Adj.  'der  am  meisten Tod,  Verderben  isf;  mahrkanam  'tmm Yt^.14*.
•  j.  mahrküäa-  m.  EN.  eines  liiiAischeii ■Wesciis,DachDk.2auberers";_j'a;  °is  *ava.- miryäite  FrW,  8.  2.  [S.  noch  '^möirSs^
*)  Wenn  300  Jahre  vom  Millennium  des UxsyiUjnta  vergangen  sind,  wird  dei  Zauberer M.  durch  Schnee  und  Kälte  in  drei  J&hren  fast die  ganie  Menschheit  Temichten.  Dann  soll Yima*  Vor  (sd.)  ge&fTnet  nnd  10  die  Erde  neu bevölkert  werden:  worauf  das  Millennium  des l/xiyal.nimaA  beginnt.  Vgl.  SBE.  4^.  9,  108, rS.  1Ö9,  479,  DST.  ZA.  a.  19,  SÖDERBLOM  La vie  future  iSi  nnd  tu  ir/a-  No.  i.
Eig.   'Zerstörer,  Verderber',    lum  V.  marii-,
s.  Wh.  Gr.»  S  1197  c.
•  p.  margav-,  j.  mariav- :  mSufv-'^  m. Name  eines  Landes,  Mar^ane'^:  \'gtd namif  i/aÄyJu/Bh,^. $;  2.a; — Äauv  'gum hamih'iyam  akunaus  Bh.  4-^\  —  adam xiayaliiya^  amiy  'gauv  Bh. j,  4.t\\  — %riiTm  asatshamiiz  .  .  fi'ä^wirpssm  ,  , mifurum  sür?m  asdvammY.i.y,  —  nisäim yim  anlar?  mSurumca  iäxZTmca  V.i.'j;  — *J  iätafym  . .  mourum  här^yum  gaomüa suxo)m  ofairizimea  "hin  . .  nach  dem  zu HaraSva  gehörigen  M.  und  nach  G.  . ." YL70. 14.
AbleiL  («.  mSrg*).  —  mp.  (Pü.),  np.  marv, np.  marf-äb;  s.  daia  Hbm.  FSt.  348.  —  ■)  Aus ir,  *nargs;  S  2**  ".  375'  ^9S.  3,  #37-  — >)  M.  gilt  Id  den  pen.  Inschriften  nicht  als Hanptprovinz,  sonst  wurde  es  Bb.  /.  6,  D.  { 5.  2,  o.  3  aufgerührt  sein.  Damit  stimmt  die Angabe  Vt  10. 14,  wonach  M.  alt  zu  Harahia gehörig  bezeichnet  wird.  Anders  Justi  GIrPh. 3,  454-  Doch  vermag  ich  in  Bb,  3.  3  keine Begründnng  für  seine  Annahme  in  erkennen.
•  j.  mar»yä-f,'Wiese':^^ära  'fa  avastaya ",  .  leg  Wiesen  an"  V.  2.  a6.
np.  man  "Wiese';  s.  dazu  Hbu.  ZDMG.  46. 244,  JusTi  ZDMG.  J7.  245,  NB.  14b.  —  Pü.:
murv  ■)  (fl/e  «/öi,',  t.ri.:/vräntön  i  ip.  —  ")  Wie (Dr  mlrifO;
•  g.  maraxtar-  m.  'Zerstörer,  Verderber*: atshsus  °tars  ahyä  yaeSa  mazdä  "und  die Verderber  dieses  Lebens,  o  M"  V.  J2. 1 3 ''.
Zum  V.  marii-.  —  Pö. :  niurnjiaitär.  —  ')  Es sind  domitdie  Irrlehrer  gemeint;  vgl.  Y.45.  1, 46.  II,  JJ-  6.
•  j.  mar«x§tar-  m.  'Gestalter':  amp/anam Spftiianam  ..yöi  hinti  ankam  dämanqm ,. dataras^a  'taras/a  . .  Yt.  ig.  18.
Vgl.  gr,  li'pH  (SOLMSBN  KZ.  34-  23);  xlt nach  %SS  ^
•  j.  mar«]^-  f.  Bezeichnung  eines  Teils
'martiya-  1148
der  (tierischen)  Eingeweide:  ya^  antar» vfrüika  *as  'ja  "was  zwischen  den  Nieren sitzt,  (näml.)  M."  V.i6:joPuZ.'\
EL,  Bed.')  und  Stammantati?  —  >>  Glosse Ol  aimoHivi  (id.).  Hdt.  (nftch  Wa):  amarija.
—  »)  Falsch  DST.  ZA.  j.  51.
•  g.  manta-  m,  'Sterblicher,  Mensch': yS  .  .  sara^ustrfm  rsdat9?ts  (sd.)  °ta^U xinäus  y.  dß.  13;  —  vacS  srüidyäi  (sd.) hyat  'taälyU  vahtltfm  Y.^lj,  S;  —  yS  l däyät  (sd.)  Sfävä  •toHbyB  Y.  2p.  7.
Eig.  PFP.  rum  V.  -'mar-.  —  Vgl.  msia-.  — np.  mard,  gr.  (lo^TOC-  —  Pü.:  tnartum,  {lu  Y. ap):  eimitrlär,  eil.:  ihrfal  (auf  Grund  f^cher E^inologie).
•  j.,  g.  niar«tan-'* :  mari^n-^^  Adj.  'sterb- lich; Mensch';  Sing,  auch  kolL:  yH  banaym (sd.)  ahüm  'ntanS  (GS.;  koll.)  Y.'jo.  6;
—  ya  räahaysn  sravaf»ha . .  'rptSnS(AF.) Y. 32.13.  a)  mit  'gaya-  (sd.,  auch  fdSt) EN.  des  ersten  Menschen:  'rata;  •n'^inS, 'rdiinl};  'ry'Sinat.
=== leaf ===
LEAF 613
numbers: []
```


## [2026-09-07T15:53:01.482Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB marg ===\"\ngrep -n \"marġ\\|marg 'Wiese'\\|Wiese\" HUB.txt | head -20\necho \"=== HRN marg ===\"\ngrep -n \"Wiese\" HRN.txt | head -20"
}
```


### [2026-09-07T15:53:01.541Z] TOOL RESULT

```
=== HUB marg ===
1789:gehort daman *Wiese' nicht hierher, da rm im Neu-
3447:975 bis. jjp fifiary = 'Wiese' belegt mir R. v. Stackelberg
8826:Np. als }': mury 'Vogel' ^= zd. mereya-; mary 'Wiese'
8846:marg 'Wiese, Aue', mog *Magier , tSg 'Spitze der Lanze*,
=== HRN marg ===
4066:'Wiese' (aus "^cermen) zu [/'car- stellen, doch ist dies
8487:wo mery wächst', arab. LW. inarj *Wiese\
8488:aw. mareyOr *Wiese' (Hübschmann, ZDMG. 46, 244
8489:No. 75); arm. LW. warg 'Wiese', syr. LW. n:i*1D 'Wiese'.
```


## [2026-09-07T15:53:09.343Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '8478,8495p' HRN.txt\necho \"=== leaf/page ===\"\npython3 - <<'EOF'\ndata=open('HRN.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nacc=0\nfor i,l in enumerate(leaves):\n    n=l.count('\\n')+1\n    if acc<=8487<acc+n:\n        print('LEAF',i,'printed ~',i-21)\n        break\n    acc+=n\nEOF\necho \"=== HUB context 8820-8850 ===\"\nsed -n '8820,8850p' HUB.txt"
}
```


### [2026-09-07T15:53:10.687Z] TOOL RESULT

```
*) Merezu- im Awesta selbst gehört dagegen wohl nicht hierher.
Die sekundäre Bedeutung von gel. merz 'Damm, der durch einen Fluss
oder Sumpf oder auch durch ein Feld gezogen ist*, hat Melgunof
(vergl. ZDMG. 21, 233) zu der Zusammenstellung mit nhd. Marache^
Marschland verführt, die lautlich unmöglich ist.
') Käs. K. dagegen kargühl *Ente*.
*) Sekundäres v wie in phlv. marvärU^ np. mervärld gegen arab.
marjc^fl, gr. juaqyaqCrrji,— 219 —
975**** nie%*y zum Viehfutter dienendes Gras', meryzar *()rt,
wo mery wächst', arab. LW. inarj *Wiese\
aw. mareyOr *Wiese' (Hübschmann, ZDMG. 46, 244
No. 75); arm. LW. warg 'Wiese', syr. LW. n:i*1D 'Wiese'.
kurd. mirkj merya 'Prairie'.
V
976. meryzenf merzyen, merzyän 'Kirchhof (Beleg bei SF).
merg Tod' -r phlv. özan *Da;Kma', np. (Riväyet)
meryözen (Darm es teter. Et. ir. II, 132).
Ganz unsicher, da die PehlevTform (NB. )XTN oder
=== leaf/page ===
LEAF 233 printed ~ 212
=== HUB context 8820-8850 ===
Sessel*; ganj 'Schatz* = np. ganj\ goin 'Farbe*, ^rat; 'Pfand*
u. s. w. ; erang 'Farbe' = np. rang; zangapan *Beinschiene',
zd. zanga- 'Knochel'.
Das anlautende y von yund 'Menge, Sehaar H. 805,
oben p. 83 kann ich nicht erklaren.— 247
§ 139. Ap. g nach Vokalen und r = y bleibt im
Np. als }': mury 'Vogel' ^= zd. mereya-; mary 'Wiese'
(oben p. 98) = zd. mareya- ; may profunditas*, mayak
Grube* H. 985 ■= zd. maya- Xoch*; muy^ may *Magier
= ap. magu' (= tnayii'); mey *Wolke* = zd. maeya--^ arDy,
aroq 'Rulpsen', gr. iotvyo^iai; dyardan 'deglutire'? H. 36;
t^y 'Spitze, Schwert', zd. bitaeya- 'zweischneidig* ; juy, yOy
* Joch*, skr. yiiga- ; dtirdy 'Luge = ap. drauga- (= drauya-) ;
day 'Brandmal, Fleck, Wunde, Brenneisen, zd. daya-; doy
saure Milch*, skr. duh melken, 3 pr. dOgdhi ; royan 'Butter,
Oel' = zd. raoyna-; vazay *Frosch* = zd. vazaya^\ varg,
hary *Wasserwehr = skr. varga-: bay (in Baydod Name
der Stadt = zd. bayddata- gottgeschaffen*) = ap. baga- {baya-),
phi. inschr. bagJ {= bay); paiydm *Botschaft\ arm. patgam
= ap. ^patiyama-; BcLdyes , arm. Valgus ^ zd. vditiga^sa-,
ap. *vatiyaisa', Np. sayal =■ sagal ^) (A. M. 84, 10) 'Schakal*
ist LW. aus dem Indischen = skr. grgdla^.
Also np. deg Kochtopf aus ap. ^daika-? Siehe oben
p. 65.
Die Armenier hatten den Laut y nicht, sie setzen
daher g fiir persisch g und y:
marg 'Wiese, Aue', mog *Magier , tSg 'Spitze der Lanze*,
bag Antheil, Erbe' ^= zd. baya-, paz. bag 'Theil, Antheil'
Min. kap. 27, 70, skr. bhaga- 'Antheil, Erbtheil'; fag 'Krone',
syr. tdya, np. taj, ap. *^6lya-; patgam 'Botschaft* = np.
paiydm; VatgBs (EliSe 139) np. Badyes.
```


## [2026-09-07T15:53:18.818Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD mrg ===\"\ngrep -n \"meadow\" SOD_pages.txt | head -20\necho \"---\"\ngrep -n \"mr'\\?\\(g\\|y\\)\" SOD_pages.txt | head -20"
}
```


### [2026-09-07T15:53:18.880Z] TOOL RESULT

```
=== SOD mrg ===
19244:                                                                                     wood, meadow
19279:           wood, meadow                                                     markat ©Skt. marakata
38837:Mani's twin 10984                         meadow      5431, 5434                  Mihryazd    5659
---
6344:      bird ry   ©-\ pred. inst. ^mry1                                       amyamand ?                                        JfL
10260:                                                                             >yw mryy B                          ^io-^ < jLX ijj>
12102:2915 pwn mry        M       c>(W)^jl^ ^jLi < JU ^.jLi
12104:       Pun-mary ? (Pwn mrg)                                             garden, paradise
12107:2916 pwn mrg =» Pwn mry                                                 but (pwty)    ©nom. -())y; abl. -\ pi. -r =»bwtyst,
15857:4250 yr8mrywndy M            S             tjfjrfj                           yarmec
18642:      mar(e)-mani       (mry, m'r m'ny) =*mr m*ny               5243 m't3 B, C
19163:                                                                                 (mry)
19207:        5416 mr'ynck1 B                            ■- . J*i»                          GMS 440; MD
19213:       5417 mr'ynkh B                           *S (<jfiy)                             *mhr'>spnd ©pi. -r; ob. pi. -tyy, -tyh
19238:            death                                                               5430 mry' M                                           3J>
19239:            GMS 249, 489; BBB 520; Hen. Cosm. 307, 46;                               mary ©Parth. mrg-, OP margus
19242:              1988, 175; mrc prm, Hen, Tales. 480.9 "until                      5431 mry2 M, C, S              (£^)j/i1>*^<4^<j,>>9
19243:              death"; pnt-mrc "near death"                                           mary (mrtyh) ©Av. mar9Ya ©pi. -t(t) ^mry*
19253:                                                                             maryunde (mrywntk) ©pi -/ ^mry'wnt'k
19255:       5432 mry-' B, M, S                      «x>t ^
19256:            mry, mary ©Av. mdrdYa ©nom. ob. -y; inst.                        GMS 138, 149; Hen. Tales. 485 n 7; TSP 3.290-5,
19258:               -)()); pi. mrY^ysi ^'mry-
19262:               & etc.; BSTBL; SCE; Frag. Len.; BBB; SCE 105,           5442 mrywntk          B =* mrywndy
19263:               252, 270; BBB 511; GMS 1240, 1186; Frag. Len.           5443 mrywr C                                  (-jy^jTlT^j
```


## [2026-09-07T15:53:25.932Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndata=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nacc=0\nfor i,l in enumerate(leaves):\n    n=l.count('\\n')+1\n    if acc<=19242<acc+n:\n        print('LEAF',i,'printed ~',i-66)\n        break\n    acc+=n\nEOF"
}
```


### [2026-09-07T15:53:27.386Z] TOOL RESULT

```
LEAF 279 printed ~ 213
```


## [2026-09-07T15:53:32.073Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '19236,19300p' SOD_pages.txt"
}
```


### [2026-09-07T15:53:32.131Z] TOOL RESULT

```
            marc  <D<Av. mahrka ©ob. -yf)} ^mrch,
              mwrtk(y)                                                               STii 1.3, 67, 86, 2.19, 3.15, 56; GMS 270
            death                                                               5430 mry' M                                           3J>
            GMS 249, 489; BBB 520; Hen. Cosm. 307, 46;                               mary ©Parth. mrg-, OP margus
              BSTBL; TSP; STi 50.3, 31.13; Sund. AoFviii                             Marv
              1981 p215; STii 1.75, 2.1; BSTi 93; C2; Sund. AI                       Hen. Mittelir. p94; KG p!85, 432
              1988, 175; mrc prm, Hen, Tales. 480.9 "until                      5431 mry2 M, C, S              (£^)j/i1>*^<4^<j,>>9
              death"; pnt-mrc "near death"                                           mary (mrtyh) ©Av. mar9Ya ©pi. -t(t) ^mry*
                                                                                     wood, meadow
       5420 mrc JJnd^ M              J ' ^ o/ jU* i^\ tSj*                           GMS 485, 526, 1661; Hen. Cosm. 307, 35; MDii
            marc(e)-J3andam (mrc(y) bnd>m)
■iM                    mm*
 i
       in
                                                                                                                          mrt'ny'kh
               -v. A-5, 15; MDii pl84, 15; mrYy> Frag. Len.
               68.13; C2, 11R24
                                                                             maryunde (mrywntk) ©pi -/ ^mry'wnt'k
                                                                             lump, clod, ball
       5432 mry-' B, M, S                      «x>t ^
            mry, mary ©Av. mdrdYa ©nom. ob. -y; inst.                        GMS 138, 149; Hen. Tales. 485 n 7; TSP 3.290-5,
                                                                               2 pi. mrYwnlU TSP 3.290; YrS mrYwndyy
               -)()); pi. mrY^ysi ^'mry-
             bird                                                              "Adam's apple", Sogdica. 56, 29; Benv. Notesiv
                                                                               499
             GMS 485, 1174, 1182; TSP 2.155, 456, 3.139, 189
               & etc.; BSTBL; SCE; Frag. Len.; BBB; SCE 105,           5442 mrywntk          B =* mrywndy
               252, 270; BBB 511; GMS 1240, 1186; Frag. Len.           5443 mrywr C                                  (-jy^jTlT^j
                                                                            maryur/I
                                                                                egg
               29.4, 71.12: O3 12, 84a 10
                                                                            twisted locks, curly hair
       5433 mry-3 B                       jljipL^iJj**
            marx ©nom. -y; ace. -w =*mrx-                                   Sund. AoFviii 1981, 25R 5 p 191 n 238                     >SJ
            straight, flat            v                                5444 mryyz'tkZ-y B                            Mj^t-'r*
            GMS 491, 520, 1191; SCE 65; VJ 1497; BSTBL,                     morye-zate
              Dhy. 18; TSP 5.28, 54; adv. "equally" TSP
              2.870, 3.248 n pi 99, 7.21                                    BSTBL, Vaj. 2, Dhu. 38; Benv. Notesiv 497

      5434 mry* B                  (^)fV'j'>y^                              MRK* -»MMLK(>)
                                                                       5445 mrktth
                                                                       5446
           mary (mryh) ©ob. -yh «»mry:
           wood, meadow                                                     markat ©Skt. marakata
                                                                            emerald
            TSP 2.811, 9.85, I3ii2; -K VJ 316; -yA, SCE 241;
              pi. mrYtt, TSP 9.85                                           Hen. Sogdica. p26; TSP 8.174
                                                                       5447 mr m'ny      M                                  J^ jjv
      5435 mry'rtOi)                              xj3y>
           maryart, maryarit ©MP murwarid; Parth.                           mar-mani      -^m}r m*ny
                                                                            Mar Mani
              murgarid; Pahl. mwlwHyh Knot, mrdhe ©ob.
                                                                            Hen. Tales. 469, 35; KG
              -y(h)\ pi. mrYyrt   =>mwrPnt
                                                                       5448 mrspnt rwc        S             «U ^ 3
            pearl
            Hen. Tales. 466, 467; VJ 16\ Sogdica. 7, 7; GMS                 marspand roc        =»mnspnd rwc
              81; MSP b34, 109 el3; Sund. AoFviii 1981, 25R                 twenty-ninth day of the month
              6 pl91, 192 n239; Gersh. SI, Cahier 7, 132,                   MDiii A4R10
             *marga-ah(a)r~ita "held by the pearl-oyster"              5449 mrsysn M                            (<S^ ij^^iTJ
      5436 mryVtswrnbyy M            jUi^ Jijlj>» <^- -^Jis                 marsisin
           mar5art-sumbe                                                    Sisinius
           pearlborer                                                       Hen. JRAS 1945; Fasts. 154.4
           Hen. Tales. 466-8
                                                                       5450 mrt-       B, S                      (j^ >^      >>) j^
```


## [2026-09-07T15:53:46.632Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in (545,546):\n    print(i, re.findall(r'^\\s*(1\\d{3})\\s*$', leaves[i], re.M))\nEOF\necho \"=== HJB mussuck ===\"\ngrep -n -i \"mussuck\\|mussuk\\|MUSSUK\" HJB.txt | head\necho \"=== AID ===\"\ngrep -n -i \"mussuck\\|mussuk\\|masak\" AID.txt | head"
}
```


### [2026-09-07T15:53:48.046Z] TOOL RESULT

```
545 []
546 ['1021']
=== HJB mussuck ===
26152:Mussuck,  6036,  92a, 735a
=== AID ===
1120:Bhisti.  [Hindustani,  from  the  Persian bihisht paradise.]  A   water-carrier, one  who  carries  water  for  domestic use,  or  waters  the  roads  or  trees. Strictly  the  bhisti  uses  a   leather  bag called  a   masak,  which  he  carries  on his  back,  while  the  pakhdli  uses  a double  bag  called  a   paklidl,  which  is carried  by  a   buffalo  or  bullock.
4422:Masak.  The  Mardthi  form  of  Mashak.
4790:Mussuk.  See  Masak.
```


## [2026-09-07T15:53:53.727Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AID Mashak ===\"\ngrep -n -i \"mashak\" AID.txt | head\necho \"=== HJB mashk/mussuck body ===\"\ngrep -n -i \"mashk\\|mussack\\|MUSSUCK\\|mus-suck\" HJB.txt | head -20\ngrep -n \"masak\" HJB.txt | head -20"
}
```


### [2026-09-07T15:53:53.800Z] TOOL RESULT

```
=== AID Mashak ===
4422:Masak.  The  Mardthi  form  of  Mashak.
4427:Mashak.  [Persian  maskk.]  A   leather bag  for  carrying  water.  The  bhisti carries  it  on  his  back.  The  name distinguishes  it  from  the  double  skin used  by  the  pakhdli.
=== HJB mashk/mussuck body ===
21976:*  This  refers  to  an  Arab  legend  that  Samarkand was  founded  in  very  remote  times  by  Tobba'-al- Akbar,  Himyarite  King  of  Yenvn,  (see  t.g.  Edriti, by  Jaubcrt.  ii.  198),  and  the  following:  "The author  of  tne  Treaiite  on  the  Figure  of  the  Earth says  on  this  subject:  "This  is  what  was  told  me by  Abu-Bakr-Dimashkl— '  1  have  seen  over  the peat  gate  of  Samarkand  an  iron  tablet  bearing  an inscription,  which,  according  to  the  people  of  the place,  was  engraveid  in  Himvarite  characters,  and as  an  old  tradition  related,  had  been  the  work  of
26152:Mussuck,  6036,  92a, 735a
```


## [2026-09-07T15:54:05.004Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndata=open('AID.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nacc=0\nfor i,l in enumerate(leaves):\n    n=l.count('\\n')+1\n    if acc<=4426<acc+n:\n        print('AID LEAF',i,'printed ~',i-18)\n        break\n    acc+=n\nEOF\necho \"=== HJB search region ===\"\npython3 - <<'EOF'\nimport re\ndata=open('HJB.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nprint('leaves',len(leaves))\nfor i in range(630,660):\n    if re.search(r'[Mm]uss?u[ck]', leaves[i]):\n        print('LEAF',i)\n        j=re.search(r'[Mm]uss?u[ck]',leaves[i])\n        print(leaves[i][max(0,j.start()-300):j.start()+900].replace('\\n',' '))\n        break\nEOF"
}
```


### [2026-09-07T15:54:06.364Z] TOOL RESULT

```
AID LEAF 207 printed ~ 189
=== HJB search region ===
leaves 1062
```


## [2026-09-07T15:54:11.946Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o -i \"mus[sc][ua][ck][ck]*\" HJB.txt | head -20\necho \"---bhisti\"\ngrep -n -i \"bihishti\\|Bheesty\" HJB.txt | head -5\necho \"--- leathern water\"\ngrep -n -i \"leathern water\" HJB.txt | head -10"
}
```


### [2026-09-07T15:54:12.026Z] TOOL RESULT

```
26152:Mussuck
---bhisti
3541:BHEESTY,  s.  The  univei*sal  word in  the  Anslo-Indian  households  of N.  India  for  the  domestic  6corre- sponding  to  the  saJbkd  of  Egypt)  who supplies  the  family  with  water,  carry- ing it  in  a  mossui^  (^^')>  ^^  go^^tskin, slun^  on  his  back.  The  word  is  P. hihiMty  a  person  of  hihisht  or  paradise, though  the  application  appears  to  be peculiar  to  Hindustan.  We  have  not i)een  able  to  trace  the  history  of  this term,  which  does  not  apparently  occur in  the  Ain,  even  in  the  curious  account of  the  way  in  which  water  was  cooled and  supplied  in  the  Court  of  Akbar (Blochmann,  tr.  i.  55  9eqq.),  or  in  the old  travellers,  and  is  not  given  in Meninski's  lexicon.  Vullers  gives  it only  as  from  Shakespear's  Hindustani Diet.  [The  trade  must  be  of  ancient origin  in  India,  as  the  leather  bag is  mentioned  in  the  Veda  and  Manu (Wilson,  Rig  Veda,  ii.  28;  IrutUiUes, ii.  79.)  Hence  Col.  Temple  (Ind,  Ant., xi.  117)  suggests  that  the  word  is Indian,  and  connects  it  with  the Skt.  visk,  *to  sprinkle.*]  It  is  one of  the  fine  titles  which  Indian  servants
3549:1829.— "  Dressing  in  a  hurry,  find  the drunken  bheesty  .  .  .  has  mistaken  your boot  for  the  goglet  in  which  you  carry your  water  on  the  line  of  march." — Cafnp Miaeriei,  in  John  Shipp,  ii.  149.  N.B.— We never  knew  a  drunken  hheeity.
3550:1878.— "Here  comee  a  seal  carrying  a porpoise  on  its  back.  No !  it  is  only  our friend  the  bheesty."- /n.  vnf  Indian  Garden, 79.
10318:1829.— "  Dressing  in  a  hurry,  find  the drunken  bheesty  .  .  .  has  mistaken  your boot  for  the  goglet  in  which  you  cany  your water  on  the  line  of  march."  —  SUpp's Memoirs,  ii.  149.
15145:MXJSSUOK,^.  The  leathern  water- bag,  consisting  of  the  entire  skin  of alarge  goat,  stript  of  the  hair  and dressed,  which  is  carried  by  a  hhMhil (see  BHEESTY).  Hind.  Ttutshak^  Skt. masaJca.
--- leathern water
```


## [2026-09-07T15:54:22.967Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndata=open('HJB.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nacc=0\nfor i,l in enumerate(leaves):\n    n=l.count('\\n')+1\n    if acc<=15144<acc+n:\n        print('HJB LEAF',i)\n        import re\n        print(re.findall(r'\\b\\d{3}\\b', l)[:10])\n        break\n    acc+=n\nEOF"
}
```


### [2026-09-07T15:54:24.603Z] TOOL RESULT

```
HJB LEAF 624
['800', '809', '578', '548', '134', '394', '206', '199', '110', '280']
```


## [2026-09-07T15:54:27.900Z] TOOL CALL #33: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T15:54:27.907Z] TOOL RESULT

```


```


## [2026-09-07T15:54:32.416Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B4%DA%A9",
 "prompt": "Give the full Persian etymology sections for مشک — all senses (waterskin/leather bag; musk). Quote the etymology text verbatim, including Middle Persian forms and any cited sources (Hasandust, MacKenzie, Cheung)."
}
```


## [2026-09-07T15:54:33.787Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%BA",
 "prompt": "Give the Persian etymology sections for مرغ — both the 'bird' sense and the 'meadow/grass' sense. Quote verbatim, including Middle Persian and Avestan/Proto-Iranian forms and cited sources."
}
```


### [2026-09-07T15:54:39.841Z] TOOL RESULT

```
# Persian Etymology for مشک

## Etymology 1 (Musk)

**Middle Persian source:** From Middle Persian *mwšk'* (mušk, "musk"), from Sanskrit *मुष्क* (muṣka).

**Comparative forms:** Old Armenian *մուշկ* (mušk), Old Georgian *მუშკი* (mušḳi), and English *musk*.

**Descendants:** Arabic *مسك* (misk); Northern Kurdish *misk*; Turkish *misk*, *mis*; Urdu *مشک* (muśk).

---

## Etymology 2 (Mouse - Dialectal)

**Source note:** Compared to Northern Kurdish *mişk*. Listed as dialectal use in specific Persian regions (Khesht, Konartakhteh, Dashtestan).

---

## Etymology 3 (Waterskin/Mussuck)

**Middle Persian source:** "From Middle Persian *mšk'* (mašk, 'mussuck, skin bag'), from Old Persian *maškā-* '(inflated cow) skin', ultimately Semitic borrowing."

**Proto-Semitic connection:** Compared to Proto-Semitic *\*mašk-*.

**Cited reference:** MacKenzie, D. N. (1971), *A concise Pahlavi dictionary*, page 55.

**Descendants:** Chagatai, Uzbek *mesh*; Hindi/Urdu *मशक*/*مشک* (maśak); Punjabi variants.
```


### [2026-09-07T15:54:41.079Z] TOOL RESULT

```
# Persian Etymology for مرغ

Based on the Wiktionary article, there is **only one Persian etymology section** provided. The article does not contain a separate etymology for a "meadow/grass" sense in Persian. That meaning appears only in the Ottoman Turkish section (Etymology 2).

## The Single Persian Etymology (Bird Sense)

**Etymology section states:**

"Inherited from Middle Persian _𐭬𐭥𐭫𐭥𐭠_ (mwlw' /⁠murw⁠/) (Manichaean Middle Persian _𐫖𐫇𐫡𐫇_ (mwrw)), from Proto-Iranian _[\*mr̥gáh](/wiki/Reconstruction:Proto-Iranian/mr%CC%A5g%C3%A1h)_ ('bird')."

The article also provides comparative forms: "Compare Middle Persian _𐭬𐭥𐭫𐭥𐭠_ (mwlw' /⁠murw⁠/), Parthian _𐫖𐫇𐫡𐫃_ (mwrg /⁠murγ⁠/), Avestan _𐬨𐬆𐬭𐬆𐬖𐬀_ (mərəγa)."

The source cited is: MacKenzie, D. N. (1971), *A concise Pahlavi dictionary*.
```


## [2026-09-07T15:54:54.024Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT maška ===\"\ngrep -n \"maška\\|maska-\\|mašká\" KNT.txt | head -20\necho \"=== KNT skin ===\"\ngrep -n -i \"inflated\\|goat.skin\\|skin\" KNT.txt | head -20"
}
```


### [2026-09-07T15:54:54.093Z] TOOL RESULT

```
=== KNT maška ===
=== KNT skin ===
357:86. DIALECT MIXTURE IN THE OLD PERSIAN Inscriptions. Like most or perhaps all other series of documents, the OP inscriptions are not in pure OP dialect, free from admixture from outside.’ They contain the expected borrowings of names of persons and places, and presumably of some cultural materials. Thus Aurà ‘Assyria’, Babiruí ‘Babylon’, Mudrdya ‘Egypt’ are from Semitic; Гаа (a district in Assyria), Dubdla (a district in Babylonia), Labandna ‘Mt. Lebanon’, Haldita- (name of an Armenian) betray their non- Iranian character by the l; a few words lack a convincing IE etymology; such as si"kabrus ‘car- nelian’, багт ‘timber’, yakd (a kind of wood), skauhiS ‘weak, lowly’, or are obvious borrowings, such as maškā- ‘inflated skin’ from Aramaic. But the main outside influence is that of the Median dialect, seen in phonetic and lexical differences, perhaps also in variant grammatical forms. Aramaic also seems to have had a certain influence on the phrasing and the syntax. There is no evidence that OP itself, at the time of the inscriptions, possessed a literature of any kind apart from these inscriptions themselves.
1258:So also other instances of k and c in OP, though many of them are in words with very scanty etymological parallels, and others are obvious borrowings from other languages, such as mashd- ‘inflated skin’, Караша ‘Cappa- docia’, К@$а- ‘ethiopia’.
1373:maskā- ‘inflated skin’, from Aramaic.
1444:occurs in borrowed words, such as maškā- ‘inflated 4
1445:skin’ (from Aramaic); and in proper names, $ the origin’ of which i&-not-always clear (here $
3582:supported on (inflated) skins, others I made camel- .
5795:maskd- sb. ‘(inflated) skin’; NPers. mask, АКК. mas-ku-u ‘skin’, Aram. maškā: borrowed from Semitic ($99, $109, §117, §148.IV; see MB Gr. 5101). такаа lpf. (872) DB 1.86.
```


## [2026-09-07T15:55:05.222Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndata=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nacc=0\nfor i,l in enumerate(leaves):\n    n=l.count('\\n')+1\n    if acc<=5794<acc+n:\n        print('KNT LEAF',i)\n        import re\n        print(re.findall(r'\\b\\d{3}\\b', l)[:8])\n        print(l[:200])\n        break\n    acc+=n\nEOF"
}
```


### [2026-09-07T15:55:06.746Z] TOOL RESULT

```
KNT LEAF 215
['111', '136', '135', '767', '876', '111', '101', '103']
rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far and wide’ (GAv. düiré, LAv. duire, Skt. d'ré; $65, 6191.111) DNa 44. duraty apiy DSe 11, DZe 6, DE 18, XPa 9, XPb 18, XPe 8, XPd 13, XPf 13,
```


## [2026-09-07T15:55:14.062Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%86%D8%AF%D9%8A%D9%84",
 "prompt": "Give the Arabic etymology of منديل (mindīl/mandīl) verbatim, including the Greek and Latin forms cited, plus any Persian section."
}
```


## [2026-09-07T15:55:15.023Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/mantellum",
 "prompt": "Give the Latin etymology of mantellum verbatim, plus its descendants. Also mention mantele/mantile if referenced."
}
```


### [2026-09-07T15:55:18.939Z] TOOL RESULT

```
# Arabic Etymology of منديل

The word منديل (mandīl) was "Borrowed from Byzantine Greek _μανδίλιον_ (mandílion), _μαντίλιον_ (mantílion), or _μανδήλη_ (mandḗlē)" meaning cloth, hand towel, handkerchief, or tablecloth. These Greek terms derive from Latin _mantēlium_ or _mantēle_ with the same meanings.

A hyperclassical vocalization _مِنْدِيل_ (mindīl) exists but diverges from standard usage.

## Persian Descendant

The entry notes a Persian descendant: مندیل (mendil), which developed through the borrowing chain from Arabic into Persian, likely via Ottoman Turkish intermediation based on the documented etymological path shown in the descendants section.
```


### [2026-09-07T15:55:19.326Z] TOOL RESULT

```
Based on the Wiktionary page provided, I cannot give you the Latin etymology of mantellum because that information is not included in the content shown.

The page only states: "**mantellum** n: alternative form of _mantēle_"

The page does not provide:
- The etymological origin of mantellum
- A list of descendants
- Details about mantele or mantile beyond identifying mantellum as an alternative form

To find this etymological information, you would need to consult the full entry for mantēle on Wiktionary or other Latin etymological resources.
```


## [2026-09-07T15:55:23.251Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/mantele",
 "prompt": "Give the Latin etymology of mantēle / mantēlium / mantellum verbatim, its meanings, and the full list of descendants (including Byzantine Greek, Arabic, Old French mantel, French manteau, English mantle)."
}
```


## [2026-09-07T15:55:24.250Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mantle",
 "prompt": "Give the full Etymonline entry for mantle verbatim, including the Latin mantellum/mantelum origin discussion and any Celtic hypothesis. Also anything on manteau."
}
```


### [2026-09-07T15:55:29.289Z] TOOL RESULT

```
# Latin Etymology and Descendants of Mantēle

## Etymology

According to the Wiktionary entry, the etymology is uncertain but semantically plausible. The source states: "A decomposition into _manus_ ('hand') and _tergō_ ('to wipe, to rub') would be semant..." The document notes this morphological origin is unclear due to variant forms and scribal errors, with possible confusion involving Celtic roots.

## Meanings

The Latin word had two primary definitions:
1. A cloth for wiping hands or mouth; a towel or napkin
2. (Post-classical Latin) A tablecloth

## Descendants Listed

The Wiktionary entry provides only a partial list of descendants:
- Byzantine Greek: μανδήλη (mandḗlē)
- Galician: mantel, mantés
- Spanish: mantel
- Chavacano: mantél
- Classical Nahuatl: mantēlex

**Important note:** The page does not include Arabic, Old French mantel, French manteau, or English mantle in its descendants section. To obtain that fuller linguistic genealogy, you would need to consult additional etymological sources beyond this Wiktionary entry.
```


### [2026-09-07T15:55:31.728Z] TOOL RESULT

```
# Etymology of Mantle

## Noun Entry

The word originates from Old English *mentel*, described as "a loose, sleeveless garment worn as an outer covering, falling in straight lines from the shoulders." Its source is Latin *mantellum* ("cloak"), which spawned cognates across Romance and Germanic languages.

The etymology presents two possible origins for the Latin term:
1. **Celtic source hypothesis** - the Latin word may derive from a Celtic language
2. **Hand-towel theory** - if *mantellum* relates to *mantelum/mantelium* ("cloth, hand-towel, napkin"), it could stem from Latin *manus* ("hand")

The entry notes reinforcement occurred in the 12th century through Old French *mantel* (Modern French *manteau*). Figurative meanings emerged around 1300, referring to something that conceals or enshrouds. By 1789, the term acquired allusive use for "symbol of literary authority or artistic pre-eminence," referencing the biblical Elijah's mantle.

## Verb Entry

The verb form appears in early 13c. as *mantelen*, meaning to wrap or cover in a mantle, derived from either the noun or Old French *manteler*. Figurative senses developed by mid-15c., while intransitive uses (becoming coated or suffused with color) emerged in the 1620s-1707 period.
```


## [2026-09-07T15:55:41.775Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in مانتو مندیل منديل مشکو مرغزار; do echo \"=== $w ===\"; grep -o -m3 \".\\{0,160\\}$w.\\{0,200\\}\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5; done"
}
```


### [2026-09-07T15:55:55.348Z] TOOL RESULT

```
=== مانتو ===
=== مندیل ===
=== منديل ===
=== مشکو ===
=== مرغزار ===
```


## [2026-09-07T15:55:58.956Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nwc -c MON_part1.txt MON_part2.txt\nhead -c 400 MON_part2.txt\necho\necho \"=== try مرغ ===\"\ngrep -c \"مرغ\" MON_part2.txt MON_part1.txt"
}
```


### [2026-09-07T15:55:59.016Z] TOOL RESULT

```
4377831 MON_part1.txt
4331421 MON_part2.txt
8709252 total
معین» محمد» ۱۲۹۱ ۱۳۵۰. 


۰ 
۳ 


فرهنگ معین / محمد معین. -- تهران: آدنا: کتاب راه نو ۰۱۲۸۱ 


۲ج 
(دوره) :964-7252-51-2 :158 
(ج.۲) 964-7252-53-6 :158۷ (ج.۱) 964-7252-52-8 :5۳81] 
فهر ستنویسی بر اساس اطلاعات فیپا. 
۱. فارسی -- واژه‌نامه‌ها. الف. عنوان. 
۴۵ف ۲۹۵۴/۸
=== try مرغ ===
MON_part1.txt:198
MON_part2.txt:298
```


## [2026-09-07T15:56:05.450Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== انتو ===\"; grep -o -m5 \".\\{0,120\\}انتو.\\{0,180\\}\" MON_part2.txt | head -6\necho \"=== ندیل/نديل ===\"; grep -o -m5 \".\\{0,120\\}ندیل.\\{0,180\\}\" MON_part2.txt | head -6\necho \"=== مشک ===\"; grep -o -m8 \".\\{0,60\\}مشک.\\{0,150\\}\" MON_part2.txt | head -8\necho \"=== مرغ ===\"; grep -o -m8 \".\\{0,60\\}مرغ.\\{0,150\\}\" MON_part2.txt | head -8"
}
```


### [2026-09-07T15:56:15.331Z] TOOL RESULT

```
=== انتو ===
ugrep: error: error at position 86
-\xbf][\x80-\xbf]*){0,180}
                          \___exceeds complexity limits


=== ندیل/نديل ===
ugrep: error: error at position 86
-\xbf][\x80-\xbf]*){0,180}
                          \___exceeds complexity limits


=== مشک ===
ugrep: error: error at position 83
bf][\x80-\xbf]*){0,150}
                       \___exceeds complexity limits


=== مرغ ===
ugrep: error: error at position 83
bf][\x80-\xbf]*){0,150}
                       \___exceeds complexity limits
```


## [2026-09-07T15:56:19.901Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor f in ('MON_part1.txt','MON_part2.txt'):\n    d=open(f,encoding='utf-8',errors='replace').read()\n    for w in ('مانتو','انتو','ندیل','نديل','مشکو','مرغزار'):\n        idxs=[m.start() for m in re.finditer(w,d)][:3]\n        if idxs:\n            print('##',f,w)\n            for i in idxs:\n                print('   ', d[max(0,i-100):i+220].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T15:56:21.778Z] TOOL RESULT

```
## MON_part1.txt مانتو
    با بوی  قوی و مطبوع می‌باشد و از اسانس بودنه در  تداوی و صاون‌سازی استفاده می‌کنند  (اسانس آن دارای مانتول» استات دومانتیل»  سیمونن» دیپانتن و پولدژون می‌باشد.) برای  این کیاه اثر خلط آور بادشکن و قاعده آور و  مقوی و سهل‌کنندة هضم ذدکر کرده‌اند  پونه» پودنةٌ لب‌جوی» پودنة جویباری» نعناع  وحشی» بوده» بوناه غاغه» حبق» حی
    وزاد برخی کرم‌ها و يا جسم دیکر)  در بین بدن حیوان و پردة پوششی که بدن  حبوان را به صدف متصل می‌کند (مانتو)  قرار می‌گیرد. حیوان به منظور دفاع و طرد  این ذرةٌ خارجی شروع به ترشح مواد آهکی  جلادار موسوم به ناکر و یک مادة از ته  موسوم به کونشیولین می‌نماید که بطور  طبقات متحدالمرکز حول جسم خارجی را  فرا می‌گیرد و در حقیقت
    ) است.   م خیم‌دوزی: [-1102-.2 [ع. ف.]  (حامص.) (خیا.) دوختن لباس‌های زمستانی  و کلفت مانند بالتو و مانتو؛ کلفت‌دوزی) مق.  ناز کدوزی.   ضد: (260)9 [ع.] (ص.) مخالف؛ مغایر.  دشمن» عدو» خصم. تاساز » تاساز کار , (لعت)  دو کلمه متحد اللفظ و مختلف المعنی مانند  «فراز کردن» که به معنی بستن و باز کردن  است. (فد.) آنکه نستش با 
## MON_part1.txt انتو
    اعت؛ مق. پادنگ.  پامنبر ی 02-00001021 آف. ۰ ۰[  (حامص.) روضه‌خوانی و خوانندگی کردن  در پای منبر.   پانتوگراف: 02010-1 (امر.) (فز.) آلتین  است که با کمک آن از هر نوع نقشه و  تصوبری نسخه‌بر داری کنند.   پانتومیم: مدقم (.) (نسم.) نماش  سالاات و احساسات و اند بشه‌ها و مطالب به  کمک عمل و حرکت.   پاندو ل 01 (.) (فز.) جسم آو
    توگراف: 02010-1 (امر.) (فز.) آلتین  است که با کمک آن از هر نوع نقشه و  تصوبری نسخه‌بر داری کنند.   پانتومیم: مدقم (.) (نسم.) نماش  سالاات و احساسات و اند بشه‌ها و مطالب به  کمک عمل و حرکت.   پاندو ل 01 (.) (فز.) جسم آویخته‌ای  که حرکت نوسانی داشته باشد مانند آویز  ساعت دیواری که به چپ و راست حرکت  فندول.   پانسمان: (۰)
    ا بوی  قوی و مطبوع می‌باشد و از اسانس بودنه در  تداوی و صاون‌سازی استفاده می‌کنند  (اسانس آن دارای مانتول» استات دومانتیل»  سیمونن» دیپانتن و پولدژون می‌باشد.) برای  این کیاه اثر خلط آور بادشکن و قاعده آور و  مقوی و سهل‌کنندة هضم ذدکر کرده‌اند  پونه» پودنةٌ لب‌جوی» پودنة جویباری» نعناع  وحشی» بوده» بوناه غاغه» حبق» حیق
## MON_part1.txt ندیل
    انیدن» قضای امر.   ازار: ءقت (- ازاره] (ا.) فوطه, نگ قطیفه.  زير جامه» شلوار» سروال» تنان. دستار؛  مندیل.   ازار: عت (- ازاره - ایزاره - هزاره] (ا.)  ازاره» ایزاره» هزاره. پایاب» قعر آب.  ازاربند: ۵ (امر.) بند شلوار؛ آنجه که  شوار و تنبان بدان بندند. همیان.   از اصل: لته [ع. ف.] (ق‌مر.) اصلا    اساسا.   ارالت: اهاقت [ع
    .  ارتفاعش تا ۷۰ سانتیمتر می‌رسد. رنگ  گل‌هایش سفید با صورتی و گلبرگ‌هایش  ریز و خوشبو است؛ زهرة القندیل» علف  هزار برگ.   بومهن: «دطه-ستا [- بومهین - بوم + مهن  - مثنه. حرکت] (ا.) زمین لرزه» زلز له.  بون: 2 [ع.] (.) دوری» جدایی.   بود: (.) بجه‌دان» زهدان» رحم.   بول: ۳5۰ [- بن ] (.) نهایت و پایان هر چیزء  بویا: 7 (ص.)
     چلتوک: »5 (- شلتوک] (.) برنج    بوست نگرفته.   چلچراغ: رقتعخ اه [ - چهل‌چراغ| (امر.)  نوعی جار یا قندیل بزرگ که شمع‌ها یا  چراغ‌های بسیار در آن باشد. نوعی  اتشازی.   چلچله: (ه)داعاه* (ا.) (جاد.) پررستو جاد.)  غلیواج. (جاد.) لاک شت. سنگ پشت.  جلچلی: ]-6۵1-60 (.حسامص.) (عسم.)  بلهوسی» هوسبازی.   چلر: »ها* (ا.) ( گیا.) ر
## MON_part1.txt مشکو
    سید کننده‌ای بسیار قوی و بر عکس  بیگر مات در پزشکی و امور بهداشت خانه  مانند گندزدایی سبزی‌ها در آب مشکوک و  نیز در شتشوی زخم‌ها بصورت محلول ۴ تا  ۰ گرم در لیر بکار می‌زود. تعضی مود  آلین فاد کلیشر رنه آسانی پرمنگنات را  تسجزیه می‌کند و با اکسیژن آن ترکیب  بش شود فان لوط پر کنات کنر  گلیسرین غلیظ پس از چند انیه به خودی
    دس مخصو صا کعبه.  داخل خانه» اندرون سرای. داخل امکنة  مقدس مخصوصاً کعبه. محل اقامت اهل و  عیال مرد» مشکو(ی). اهل و عیال شخص»  پردگیان؛ برده‌نشینان» زنان عقدی و صیغه و  کنیزان مرد؛ ج. احرام.   حرمان: ۵*5۰ [ع.] (مصل.) بی‌بهره  بودن» بی‌روزی ماندن. (امص.) بی‌بهرگی»  بی نصیبی» نومیدی.   حرمت: ۱0۵۱ [ع. حرمه] (.) ایروه  عزت»
    ر را. (عر.)  اجتماع خبن و کف است در «فاعلاتن» تا  رفعلات» شود و «فعلات» چون از فاعلاتن  خیزد» آن را مشکول خوانند. (المعجم. مد.  چا. ۳۸-۳۷:۱).   شکل: 801۵ [ع.] (.) چهره» صورت؛ روی»  سیما. پیکر» کالبد. ۳ سم» طریقه. مانند» شبه»  مثل. نا ره اف ره.) 7 قد.) هیقتی اس تکه از    احاطةً یک با چند حد بوجود آید و ار    مقولاٌ کیف 
## MON_part1.txt مرغزار
    قوا لع. ف. - تفرجگّه]  (امر.) جای تفرج» گردشگاه» جایی که  شادمانی آورد» جای گشت و گذار مانند باغ  و مرغزار و جز آن.   تفر د: ۱93۳0۹ [ع.] (مص‌ل.) بکانه بودن»  تنها شدن» یکه و تنها شدن» یکه و تنها بودن.  (امص.) استقلال» خودرایی؛ ج. تفر دات.  تفرس: 923۳۳0 [ع.] (سص م.) دانستن  چیزی به علامت و نشان, به فراست دریافتن»  بو بر
     و لوازم دیگر را در آن نهند)؟  جامه‌دان» حرمدان» خرمدان.   چمن: : «مسمع (.) (گیا.) زمین سبز و خرم؛  مرغزار. گب .#گباه ی است از تب غلا ت که    دارای و نه‌های متعدد است. ب رگ‌هایش  کشده و طیل و سیر تیره و دارای  جمنده: (0-)708-« (افا. چمیدن) کسی  که به ناز راه روده خر امند ۵.   جمن‌زار: 6۰-۲ (امر .) زمینی که در آن  چمن ب
    أمور اصلاح جهان و تدبیر اسور  ناس است. ( کشاف اصطلاحات ۵۹۷ فر ع.  سج.)؛ ج. رعات (رعاة)   راغ: 3 (.) مرغزار. دامن کوه؛ دامن سبز  کوه. صحرا.   راغب: (ع.] (افا.) رغفضبت کننده؛  مایل» خواهان؛ ج. راغبین.   رافض: 2 (ع.] (افا.) ترکث کننده» رها  کننده واگذارنده.   رافضه: ()۲8۲6-2 (ع. . رافضه ] (افا.) موّنث  رافنض گروهی که پیشو
## MON_part2.txt مانتو
    ‌های ابرانی بر خاسته است.  گاباردین: 202070 (ستر. غاباردین] (.)  پارچهٌ پشمی دارای تار و پود فشرده. مانتو  غیر قابل نفوذ (امپرمابل) که از پارچة مذکور  ساز ند.   کاحمه: (م-) هدقع (۱.) قتت کاو آهن  که در برنجکاری بکار بر ند.   گادن: 88-2 کال (مص ع.) (گاد؛  کاید» خواهد گاد؛ بگای» گاینده» گاده)  جماع کردن؛ گاییدن.   گار؛ ۱
    وتم» است. ريشة علم و معرفت  اسان به خدا و خدابان را در ادیان قدیم و  جدید در مانا باید جستجو کرد.   مانتو: 0 (.) جامة کشادی که روی  لباس‌های دیگر پوشند (زن و مرد).  مانتیس: 25 [(۱.) (رض.) در لگاریتم  یر ارم وی ون  اعشاری 1" را افانتتس: کوسد: . ضصح.- با  توجه به معنی لگٌاریتم و صفر و مفسر و  مانتیس» همواره مفسر اعداد از
    است. این گیاه همه آثار نبرو دهنده و    بادشکن و خلط اور بودنه را دارا است. از  این گیاه اسانسی بنام مانتول استخراج می‌کنند  که جهت خوشبو کردن داروها و برخی  آب‌نبات‌ها و شیرینی‌ها بکار می‌رود. علاوه  بر این در معالجهٌ التهابات مخاط بینی و گلو  و دهان اسانس مزبور مورد استعمال دارد. از  انساج نعناع نوعی کافور قابل تبلور 
## MON_part2.txt انتو
    : 122۱ (.) مجرایی پهناور که دو در با  یا دو نهر را به یکدیگر متصل سازد؛ ترعه»  قنات: کانال سو ر.   کانتور: :۱20۱0 (- گنطور - گنتور] (.)  شعبهً حسابداری ننگاه با اداره‌ای.   کاند بدا 8 (.) داو طلب مقامی و  شغلی» نامزد.   کان‌شناسی: -۷20-56025 ( حامص.) علم ره    کامیاب  شناسایی معادن مختلف و آن یکی از شعب  کانفت؛: ۱ [- ک
    ه دهند اما هر یکك در داخل اتسحادبه  استقلال داخلی و خودمختاری دارند»  چنانکه کشور سویس را که از ۲۲ کانتون  تشکیل گردیده نامند. اتحاد به.   کنفر انس: 0۵6 (.) اجتماع گروهی  از متخصصان فن برای شور و بحث در  سبایل فنی. اجتماع سباستمداران؛ رسای    ۱۰۹  دول؛ وزیران به منظور حل یک مسأًله  سیاسی؛ داخلی يا بین‌المللی. خطابه ادس
    های ابرانی بر خاسته است.  گاباردین: 202070 (ستر. غاباردین] (.)  پارچهٌ پشمی دارای تار و پود فشرده. مانتو  غیر قابل نفوذ (امپرمابل) که از پارچة مذکور  ساز ند.   کاحمه: (م-) هدقع (۱.) قتت کاو آهن  که در برنجکاری بکار بر ند.   گادن: 88-2 کال (مص ع.) (گاد؛  کاید» خواهد گاد؛ بگای» گاینده» گاده)  جماع کردن؛ گاییدن.   گار؛ ۱۳
## MON_part2.txt ندیل
    م و   ندشکن: 7-10 [معر. ف.  قندشکننده] (ص‌فا. .) چکشی که ۳  کلوخه‌های قند را به اجزاء تقسیم کنند.  تندیل: [معر.] (.) چراغ. چراغدان»  شمعدن (مخصوصاً که از سقف آویزان  باشد)؛ قنادیل. قندیل ترسا: قندیلی که  پیوسته در کلیسا آویخته باشند. قندیل چرخ:  ( کد.) آفتاب و ماه. قندیل دوسر: ( کد.)  آسمان. قندیل شب: سیاهی شب. قندیل  
    زاء تقسیم کنند.  تندیل: [معر.] (.) چراغ. چراغدان»  شمعدن (مخصوصاً که از سقف آویزان  باشد)؛ قنادیل. قندیل ترسا: قندیلی که  پیوسته در کلیسا آویخته باشند. قندیل چرخ:  ( کد.) آفتاب و ماه. قندیل دوسر: ( کد.)  آسمان. قندیل شب: سیاهی شب. قندیل    فرهنک فارسی معین    قنداق  قنطار: (ند. -۰۸۱276۵[معر. یو (.) پوست  گاوی که درون آ
    ند.  تندیل: [معر.] (.) چراغ. چراغدان»  شمعدن (مخصوصاً که از سقف آویزان  باشد)؛ قنادیل. قندیل ترسا: قندیلی که  پیوسته در کلیسا آویخته باشند. قندیل چرخ:  ( کد.) آفتاب و ماه. قندیل دوسر: ( کد.)  آسمان. قندیل شب: سیاهی شب. قندیل    فرهنک فارسی معین    قنداق  قنطار: (ند. -۰۸۱276۵[معر. یو (.) پوست  گاوی که درون آن را پر زر ک
## MON_part2.txt مشکو
    ‌گشا(ی): (2005:1)۷-.۱0۱ [ع. ف. -  مشک لگشاینده] (ص‌فا.) آنکه کب را  حل کند و دشواری را اسان نماید.  مشکو: 723-1 (.مصف.) مشک کو چککت؛  مشکو: 1 [ - مشکوی مکشو به ] )1(  حرمسرای شاهان. کوشکک. بالاخانه.  مشکور: ۱20۲ [ع.] (امف.) شکر گفته»  سیاس داشته شده؛ ستوده شده.   مشحوفی: 1 (- مشکو فه ] (.) نوعی  حلوای مغز بادام و شکر. 
    مشک لگشاینده] (ص‌فا.) آنکه کب را  حل کند و دشواری را اسان نماید.  مشکو: 723-1 (.مصف.) مشک کو چککت؛  مشکو: 1 [ - مشکوی مکشو به ] )1(  حرمسرای شاهان. کوشکک. بالاخانه.  مشکور: ۱20۲ [ع.] (امف.) شکر گفته»  سیاس داشته شده؛ ستوده شده.   مشحوفی: 1 (- مشکو فه ] (.) نوعی  حلوای مغز بادام و شکر.   مشکوک: 0۱۱20 [ع.] (امف.) جیزی که
    ] (ص‌فا.) آنکه کب را  حل کند و دشواری را اسان نماید.  مشکو: 723-1 (.مصف.) مشک کو چککت؛  مشکو: 1 [ - مشکوی مکشو به ] )1(  حرمسرای شاهان. کوشکک. بالاخانه.  مشکور: ۱20۲ [ع.] (امف.) شکر گفته»  سیاس داشته شده؛ ستوده شده.   مشحوفی: 1 (- مشکو فه ] (.) نوعی  حلوای مغز بادام و شکر.   مشکوک: 0۱۱20 [ع.] (امف.) جیزی که  دربارة آن 
## MON_part2.txt مرغزار
    ) ناچیز»  نانود. فرومایه؛ بی‌اعتبار. چیز اند کك» شی  قلیل. وجه اندکك؛ ثمن بخس. به ۳  ۳7   لاش: *15 [مرغزاری] (۷.) تاراج» غارت»  یغما؛ چیاول. به # ات تن  لاش: ۱55 (.) چید   لاشبرگ: ۳۹ (کیا.) لاب تبره  رنگی که در نتیجةٌ پوسیدگی برگک‌های تازه  با خشک و ساقه‌های جوان افتاده بر روی  خاک جنگل بوجود می‌آید و در حقیقت  لاش رگ 
    ویند؛ توان. ضح.- مال و مجدور  یکی است منتهی مال را در جبر و مقاله بکار  می‌برند و مجذور را در حساب. مرغزار با  درخت. (عریی ادبه. ند. ف.) چار با مانند  اسب و استر و جز آنها. مال: ملک. متعلق  به: مال من. مربوط به. مال بی‌صاحب: مالی  که فا عب اه تسه ری که ان زر  ارزان فروشند یا در نگهداری آن اهمال  کند. مال صاحب مرده. (عم
```


## [2026-09-07T15:56:37.206Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D9%86%D8%AF%DB%8C%D9%84/",
 "prompt": "Quote the \"فرهنگ معین\" section for مندیل verbatim (including any origin tag like [ع.]), and the Dehkhoda section's definition."
}
```


## [2026-09-07T15:56:37.969Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D8%A7%D9%86%D8%AA%D9%88/",
 "prompt": "Quote the \"فرهنگ معین\" section for مانتو verbatim, including any origin tag such as [فر.] or [فر. manteau]."
}
```


### [2026-09-07T15:56:42.580Z] TOOL RESULT

```
# مندیل - Dictionary Definitions

## فرهنگ معین Section
"(مَ یا مِ ) [ ع . ] (اِ. ) دستار و عمامه . ج . منادیل ."

## Dehkhoda Dictionary Definition
The Dehkhoda section presents multiple definitions, beginning with the notion of a cloth used for wiping one's hands, sourced from *Montahat al-Arab* and *Nazem al-Atteba*. It also denotes a turban-like head garment worn around the waist, and separately describes a headcloth used for covering food. Additional meanings include various types of head wrappings and turbans, with the plural form listed as منادیل.
```


### [2026-09-07T15:56:43.174Z] TOOL RESULT

```
# فرهنگ معین Definition for مانتو

According to the Farhangi Moein section, here is the entry:

"(تُ ) \[ فر. \] (اِ. ) لباس گشادی که روی لباس های دیگر پوشیده می شود، روپوش ."

This describes مانتو as a loose garment worn over other clothing, with the French origin marker [فر.] and the etymology indicator [اِ.].
```


## [2026-09-07T15:56:55.414Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFA mandil ===\"\ngrep -n -i \"mandil\\|mandīl\\|manṭīl\" AFA.txt | head -10\necho \"=== LKT mandil ===\"\ngrep -n -i \"mandil\\|mantellum\\|manteau\" LKT.txt | head -10\necho \"=== PHN/DEV manteau ===\"\ngrep -n -i \"mandil\\|manteau\" PHN.txt DEV.txt | head -10\necho \"=== FVQ mandil ===\"\ngrep -n -i \"mandil\" FVQ.txt | head -5\necho \"=== AFM mandil ===\"\ngrep -n \"مندیل\\|منديل\" AFM.txt | head -5\necho \"=== SKT mantle ===\"\ngrep -n -i \"^Mantle\\|Mantle,\" SKT.txt | head -5"
}
```


### [2026-09-07T15:56:55.518Z] TOOL RESULT

```
=== AFA mandil ===
=== LKT mandil ===
3213:1391.  Ar.  mandil:
3214:'Tuch,  Hülle'  [aus  gr.  )aavbr|\iov,  lat. mantile  ZDMG  LI,  317;  Dozy  Vßtem 414 f.];  hieraus  sp.  pg.  kat.  mandil "Schürze'.  —  [Unmittelbar  aus  dem  lat. mantile  kommen  mantel  'Tischtuch'  und mantilla].    [DE  2^i9/3üÜ.    Eguilaz  443.
5320:mandil  1391
7306:madeixa  476 ■mahona  1449 I  manä  1398 i  mandil  1391 i  mandonguilla  355 I  maquila  1373 i  maravedi  1515 [  marcasita  1374 I  marfega(ssa)  1413
8225:mandil  1391
=== PHN/DEV manteau ===
DEV.txt:877:Caban.  Autrefois  gaban;  esj).  gaban,  portug.  gabbciOj ital.  gabbano.  Le  Dictionn.  de  M.  Littré  donne  pour  étj- mologie  l'arabe  pU^  'abâ^  drap  grossier  dont  on  fait  des capotes,  et  aussi  manteau  noir  rayé  des  derviches.  Uaba, dit  M.  Defrémery,  est  c^une  sorte  de  manteau  court,  ou- vert sur  le  devant  et  dépourvu  de  manches.  C'est  l'hahit caractéristique  des  Bédouins  à  toutes  les  époques  ^  7^  rcll y  avait  là  des  Kurdes .  .  .  dont  Yabba  est  rayé  de  bandes brunes  ou  blanches,  w  (Duhousset^.)
DEV.txt:1163:(]oRGE  ou  GojjRGE.  ^^Paquet  de  toile  de  coton  des  Indes.  55 (Littré.)  C'est  vraisemblablement  l'arabe  ^-îw  khordj,  be- sace, sac  de  voyage,  portemanteau  (qui,  avec  l'article  et le  a  d'unité,  ^j^  al-kliordja,  a  donné  l'espagnol  alforja, portug.  alforge,  besace).
PHN.txt:709:*Uft [*«Aa'] Manteau de laine grossière, rayé de blanc et de
PHN.txt:710:brun , que les Bédouins mettent par-dessus un autre manteau
PHN.txt:725:celui-ci désigne un autre genre de manteau de laine, h ca-
PHN.txt:2532:Le manteau de Mahomet portait ce nom. — Il existe chez les
PHN.txt:2534:c'est-à-dire le Manteau, et qui a été composé à la louange du
PHN.txt:2710:•Vfi [fff&i' ] Espèce de manteau court , plus juste à la taille que
PHN.txt:6084:aussi le manteau pénitentiel que tout pèlerin musulman est obligé
PHN.txt:6321:lisse ou sous le manteau appelé bénxch; dérivé de <^^i^- [^^^^]
=== FVQ mandil ===
=== AFM mandil ===
=== SKT mantle ===
4170:coftt.  CF.-G.)  M.  E.  «ft.-O.F.  eott (F.  cotle)  \  Low  L.  cola,  a  coat,  aUo  a  coL »M.  H,  G.  kottt^  kutu,  a  coane  mantle, lit  '  covering ; '  allied  to  A.  S.  «a€,  a  cot, ong.  'ooTcnog,*
11061:remnant.  (F"".  — L.>  M.I..  rcmanatint. O.  V.  rrmunmf,  a  residue.  —  I*  rrntaMftt/; stem  of  pres.  pt.  of  nema/argt  to  remain, Siantel ;  sec  below. Mantle,  a  cloak,  covering.  (F.  —  L.) M.  1l.  mantei.  •>  O.  F.  tnatttti,  later  matitrau, *  a  doke,  also  the  mantle-tree  of  a  chim- ney;' Cot.  — L.  moHUHiim,  a  napkin,  alfto a  covering ;  cf.  L.  mantiU,  a  towel.  \Vc ;iUo  find  Low  L,  mantum^  a  short  clouk, whence  Itol.  and  Span.  manlOy  Y.  mante, a  mantle.  Dor.  mantle,  vb.,  to  form  a covering  upon,  to  gather  a  scum  on  a  sur- face.
14454:demeanour.  (^K.  *  L.)  M.E 9ri,  '  the  carriflge,  or  dcmeonnr Cot.  A  »b.  due  to  the  verb carry.  —  L.  per/are.  to  carry. (^PAK.)  Der.  Afr^.  verb, anna  ; '  p«rt-<d,  P.  L,  iv.  980. r,  a  bearer  of  a  burden,  «ub- M.  E.  portour,  from  I*",  porteur. rr,  the  name  of  a  strong  malt- Balled  from  bcin)>  the  favoQiite Ion  porters.  Also  port-folia, «nough  to  carry  folio  paper pcnt'ffuiiU\,  port-mattteau,  F. t ;  Kc  Mantle,  Mantua  ;  port-
16565:Say  (2).  a  kind  ofsert^.  (F.-L.-Gk.) O.  F.  utUy  say.  (Cf.  Span,  saya^  sayo,  a tunic;  saytte,  a  thin  stufT.)  So  called because  used  for  making  a  kind  of  coat called  in  Latin  /o^,  sagum,  or  xo^^kx  ;  Low L.  sagttm,  (1)  a  mantle,  (s)  a  kind  of  cloth. *Gk.  ad7Qf.  a  soldier's  mantle;  so  called from  hanging  down.  Cf.  Skt.  jajj,safij\  to adhere,  hang  down  from.
```


## [2026-09-07T15:57:07.277Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW ===\"\ngrep -n -i \"mantellum\\|mantelum\\|mantele\\|mantile\" LEW_1910.txt | head -10\necho \"=== LAT ===\"\ngrep -n -i \"mantellum\\|mantelum\\|mantele\\|mantile\" LAT.txt | head -10"
}
```


### [2026-09-07T15:57:07.341Z] TOOL RESULT

```
=== LEW ===
=== LAT ===
36355:mantele, -ls n.; mantelium, -i (un g^n.pl. nante lorum dans Fest.
36356:118,1O n 1 est peut-etre qu'une faute de copie a moins que mantele
36357:n'ait ete confondu par Festus avec mantellum): essuie-mains; mantelium
36360:11 est probable que mantele est la forme ancienne; le mot 4 tant surtout
36362:On trouve aussi dans les gloses mantela et mantile, mantilia formes
36364:a la confusion qui s'est produite entre 5 et i. A basse epoque mantele,
36368:mantellum, - 1 : manteau, couverture; Pl.Cap.530,531. A basse epo¬
36387:mantellum, de caractere populaire. Atteste depuis Catulle. Repalidu
36400:mantus: v. mantellum.
36543:(cf. mantellum).
```


## [2026-09-07T15:57:11.306Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '36350,36405p' LAT.txt\necho \"=== leaf/page ===\"\npython3 - <<'EOF'\ndata=open('LAT.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nacc=0\nfor i,l in enumerate(leaves):\n    n=l.count('\\n')+1\n    if acc<=36354<acc+n:\n        print('LAT LEAF',i,'printed ~',i-18)\n        break\n    acc+=n\nEOF"
}
```


### [2026-09-07T15:57:12.957Z] TOOL RESULT

```
(sens ordinaire); mansuefacio, -fio, remplace k basse <?poque par man-
suStd,-Ss (Vulg.), M.L.5319; mansuetarius: dompteur (b.lat.); immansuetus
(epoq. imp£r.; d'apres avq^epoC?). Cf. aussi *ndnsuet inus, M.L.53550;
*ma(n)sus, 5334 (avec influence de maneo, mansus).
Pour la forme n an-, cf.man-tele, et v. sous manus.
mantele, -ls n.; mantelium, -i (un g^n.pl. nante lorum dans Fest.
118,1O n 1 est peut-etre qu'une faute de copie a moins que mantele
n'ait ete confondu par Festus avec mantellum): essuie-mains; mantelium
ubi manus terguntur, Varr. L.L.6,85, qui indique ainsi 1 1 ^tymologie:
*man-terg-s-li, sans doute neutre d'un adj . en -Zts; puis "nappe".
11 est probable que mantele est la forme ancienne; le mot 4 tant surtout
usite au pluriel, mantelia, on a refait sur celui-ci un sg. mantelium.
On trouve aussi dans les gloses mantela et mantile, mantilia formes
qui peuvent etre dues a 1'influences des mots en -ilis, ou plutot,
a la confusion qui s'est produite entre 5 et i. A basse epoque mantele,
specialise dans le sens de "nappe", a ete remplace dans .le sens de
"essuie-mains" par nanutergium. M.L.5335.
L'ombrien a mantrabklu (de man-tfg-t lom?). Pour man-, v. sous manus.
mantellum, - 1 : manteau, couverture; Pl.Cap.530,531. A basse epo¬
que apparait une forme mantus, ainsi definie par Isid., Or.19,34,15,
mantum Hispani uocant, quod manus tegat tantum (etym.pop.): est enim
breue amictum, qui est sans doute une derivation retrograde de man¬
tellum, comme le suppose J.B.Hofmann. Derives de mantus: mantuelis
{chlamys); mantuatus "ornamentum militare, i.e. paludatus " ( 61 .),
rares et tardifs. Panroman, sauf roumain; M.1.5336,et 533O; germ.:
v.angi, nentel , etc.; iri. matal, etc.
mantica, -ae f. : poche, sac (qu'on porte sur le dos), besace,
bissac.mantisa
G8G
Derives: nanticula', mant icul or, -ar is (arch.): mant icularum usus
pauperibus in nunnis recondendis etiam, nostro saeculo fuit/. Vnde
manticulari dicebantur, qui furandi gratia nanticulas attempt'abant.
Inde poetae pro dolose quid agendo usi sunt eo uerbo, P.F.118,3;
mant iculat i 5 , -tor, -rius .
Rapproche par les anciens de manus, comme le montre la^glose:
manticularia dicuntur ea quae frequenter in usu habentur, et quasi
manu tractantur..., P.F.ny,4. Peut-etre mot d'emprunt, cf. mantum,
mantellum, de caractere populaire. Atteste depuis Catulle. Repalidu
dans les 1 . romanes, M.L.5327 et S 327 &.
mantisa (mantissa), -ae f.: supplement. Mot etrusque d'apres P.F.
119,y, — additamentum dicitur lingua lusca, quod ponderi adicitur,
sed deterius et quod sine usu est. Lucilius (1208): "mantisa obsonia
uincit ", Sans doute mot populaire; figure seulement dans Lucilius
et Petrone. Dans Lucilius, par opposition a obsGnia, semble designer
quelque chose comme la "rijouissance" de nos bouchers, comme le suggere
M. Niedermann.
mantiscinor: hybride plaisamment tire de gr. p.avxuG, par Plaute,
Cap.8yG, sur le modele de uaticinor; cf. aussi Donat, in Ter.Eun.258
( manticinor).
manto: v. maneo.
mantus: v. mantellum.
Manturna, -ae f.: deesse d'origine etrusque, comme le dieu Mantus
(Serv. ad Aen.10,199); cf. pour le suffixe Saturnus, Iuturna. Rattache
par 1’etymologie populaire a mantum de maned, et invoquee ut maneat
noua nupta cum uiro (Varr. ap. Aug. Ciu.D. 6, y).
manubiae (noni-),-Srum f.pl.: 1° proprement "ce qu'on tient en
=== leaf/page ===
LAT LEAF 690 printed ~ 672
```


## [2026-09-07T15:57:35.044Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A4%B6%E0%A4%95",
 "prompt": "Give the Sanskrit entry for मशक (maśaka): all senses and the etymology. Does it mean 'leather bag / waterskin'? Quote verbatim. Also any Hindi section."
}
```


## [2026-09-07T15:57:36.335Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B3%D9%83",
 "prompt": "Give the Arabic entries for مسك — especially any sense 'skin, hide' (mask) and its etymology, and the 'musk' sense. Quote verbatim, and note any Proto-Semitic *mašk- reconstruction."
}
```


### [2026-09-07T15:57:42.308Z] TOOL RESULT

```
# Sanskrit Entry for मशक

**Senses:**
The Sanskrit word मशक (maśaka) is a masculine noun meaning: "gnat, mosquito, fly"

**Etymology:**
"Metathesized from Proto-Indo-Aryan *makáśas, from Proto-Indo-Iranian *makáćas"

**Does it mean 'leather bag/waterskin'?**
No. That meaning belongs to the **Hindi Etymology 1** entry only. The Sanskrit entry does not denote a leather container.

**Hindi Section (Etymology 1):**
The Hindi word has a different origin: "Borrowed from Classical Persian مشک, from Middle Persian mšk' ('mussuck, skin bag'), from Old Persian 𐎶𐏁𐎣𐎠 (m-š-k-a, '(inflated cow) skin')."

In Hindi, मशक means "a kind of leather water-holding bag" or "hydration pack" — but this sense does **not** appear in the Sanskrit section.
```


### [2026-09-07T15:57:43.428Z] TOOL RESULT

```
# Arabic Entries for مسك (mask)

## "Skin/Hide" Sense

**Etymology 2** provides: "Inherited from Proto-Semitic _[\*mašk-](/wiki/Reconstruction:Proto-Semitic/ma%C5%A1k- "Reconstruction:Proto-Semitic/mašk-")_."

The noun definition states: "recently cut hide of a new-born goat, scalp of a neonate"

## "Musk" Sense

**Etymology 3** traces the origin: "From Middle Persian [script needed] (mwšk' /⁠mušk⁠/, 'musk') (Persian مشک (mošk, 'musk')), from Sanskrit मुष्क (muṣka, 'testicle, scrotum')."

The entry defines **مِسْك** (misk) as simply: "musk"

A Quranic citation (83:25-26) illustrates usage: "its seal is of musk."

The entry also documents that this term produced descendants in Romance languages through Andalusian Arabic, including Spanish *almizcle* and Catalan *almesc*.
```


## [2026-09-07T15:57:55.509Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/webtc/getword.php?key=1%C2%A0ma%C5%9Baka",
 "prompt": "Quote the Monier-Williams entry for maśaka verbatim, listing all senses."
}
```


## [2026-09-07T15:57:56.037Z] TOOL CALL #54: WebSearch

```json
{
 "query": "Monier-Williams maśaka \"leathern bag\" Sanskrit mosquito Turner CDIAL mashak Persian mašk"
}
```


### [2026-09-07T15:57:59.783Z] TOOL RESULT

```
I cannot provide the Monier-Williams entry for maśaka because it is not contained in the web page content you shared. The page only shows a "not found" error message indicating that the term '1 maśaka' was not located in that particular resource (slp1).

To access the actual Monier-Williams dictionary entry with all senses of maśaka, you would need to consult the complete Monier-Williams Sanskrit-English Dictionary directly.
```


### [2026-09-07T15:58:03.494Z] TOOL RESULT

```
Web search results for query: "Monier-Williams maśaka "leathern bag" Sanskrit mosquito Turner CDIAL mashak Persian mašk"

Links: [{"title":"Mashaka, Masa-ka, Maśaka, Māsaka, Masaka, Māṣaka: 31 definitions","url":"https://www.wisdomlib.org/definition/mashaka"},{"title":"maśaka - Sanskrit Dictionary","url":"https://sanskritdictionary.com/?q=ma%C5%9Baka"},{"title":"Monier Williams | eBay","url":"https://www.ebay.com/shop/monier-williams?_nkw=monier+williams"},{"title":"Mashak: 2 definitions","url":"https://www.wisdomlib.org/definition/mashak"},{"title":"Monier Monier-Williams","url":"https://en.wikipedia.org/wiki/Monier_Monier-Williams"},{"title":"Sanskrit Manual, Parts 1-2...: Monier-Williams, Sir Monier: 9781277495409: Amazon.com: Books","url":"https://www.amazon.com/Sanskrit-Manual-Parts-Monier-Monier-Williams/dp/1277495408"},{"title":"Monier Monier-Williams (Author of A Sanskrit English Dictionary 2005 Deluxe Edition)","url":"https://www.goodreads.com/author/show/536678.Monier_Monier_Williams"},{"title":"Amazon.com: M Monier-Williams: Books","url":"https://www.amazon.com/Books-M-Monier-Williams/s?rh=n%3A283155%2Cp_27%3AM%2BMonier-Williams"}]

Based on the search results, I found relevant information about the Sanskrit term maśaka:

According to the Monier-Williams Sanskrit-English Dictionary, maśaka (मशक) is defined as a gnat or mosquito, an eruption on the skin, or a leather water-bag.

The search results show that this Sanskrit word has multiple meanings, with both the "mosquito" and "leather water-bag" senses documented in the Monier-Williams dictionary. However, the search results don't contain detailed information about the etymological connections to Persian mašk or references to Turner's CDIAL (Comparative Dictionary of the Indo-Aryan Languages) that you mentioned in your query. To get more complete information about those etymological relationships, you might need to consult those specific scholarly sources directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T15:58:07.732Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.wisdomlib.org/definition/mashaka",
 "prompt": "Quote the Monier-Williams (Sanskrit-English Dictionary) entry for Maśaka verbatim, listing all senses including any 'leather water-bag' sense and the texts/lexicographers cited (e.g. \"L.\" = lexicographers only)."
}
```


### [2026-09-07T15:58:13.608Z] TOOL RESULT

```
# Monier-Williams Entry for Maśaka

According to the Monier-Williams Sanskrit-English Dictionary cited in the webpage, Maśaka has these senses:

"a mosquito, gnat, any fly that bites or stings" (with textual citations from Atharva-veda and other sources)

"a particular skin disease (causing dark bean-like pustules or eruptions)" (citing Varāha-mihira's Bṛhat-saṃhitā and Suśruta)

"a leather water-bag"

The entry also notes it is "Name of a preceptor with the patronymic Gārgya (the composer of a Kalpa-sūtra)" and "Name of the district in Śāka-dvīpa inhabited by Kṣatriyas" (referencing the Mahābhārata).
```


## [2026-09-07T15:58:25.264Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== EAV leaf 164 (p866) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==165' EAV_studies.txt | head -60"
}
```


### [2026-09-07T15:58:26.654Z] TOOL RESULT

```
=== EAV leaf 164 (p866) ===
 the Bible given to all of them.? Part of the answer is that there are different God-roles even in the Bible, and it may be that the most important one — sketched in the parables of the Gospels — has never been understood as such by Christian theologians.
When Smith describes faith as “the ability to see the transcendent and to respond to it, to hear God’s voice and to act accordingly,” he is speaking of experience made possible by some of the many God-roles transmitted in the cumulative traditions.
The percept God presupposes a pattern of some kind, and I think that the leap from ‘the transcendent’ to ‘God’ as easily as Smith makes it here is neither possible nor permissible; especially not if we are to con- form to the principles for the study which he himself has promulgated in his book. Faith has too much to do with doctrine. Would Smith not agree that the next step to be taken is the study of the role-systems given in religious traditions and the experiences given by them? ®
HJALMAR SUNDEN
* Many psychological findings indicate that we must reckon with two different kinds of people, the one being able to see roles and assimilate them, the other without this disposition. The latter prefers the doctrines of religious traditions so that we can speak of the role-man (goal-oriented) versus the doctrine-man (threat- oriented). I think Smith’s protest against reifying religion to an intellectual entity and his preference for the cumulative tradition is an important reaction to the dominance of doctrine-men.
*I think we can keep the word ‘religion’ as denoting man’s relation to the Totality. It is to the All that man directs his requests for guidance through oracles and omnia. In the long run of the cumulative tradition the Totality has revealed itself not only as ‘will’ but also as ‘cosmic order’. Patterns concerned with cosmic order also deserve our attention.
IE & | THE UNIVERSITY OF CHICAGO PRESS JOURNALS
MET
On the Cityscape of the Merode Altarpiece Author(s): Jacques Duchesne-Guillemin Source: Metropolitan Museum Journal, 1976, Vol. 11 (1976), pp. 129-131
Published by: The University of Chicago Press on behalf of The Metropolitan Museum of Art
Stable URL: |https:/ / ww w.jstor.org/stable/ 1512690
JSTOR is a
```


## [2026-09-07T15:58:31.603Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"amorb\\|Etymologies avestiques\" EAV_studies.txt | head -10\necho \"=== marəγ / marey ===\"\ngrep -n \"marəy\\|marey\\|marəγ\\|mareya\" EAV_studies.txt | head -20"
}
```


### [2026-09-07T15:58:31.661Z] TOOL RESULT

```
4:"Etymologies Avestiques," from Bulletin of the School of Oriental Studies, University of London, Vol. 9, No. 4 (1939), pp. 861-869.
86:Etymologies Avestiques Author(s): J. Duchesne-Guillemin
95:Etymologies Avestiques Par J. DUCHESNE-GUILLEMIN
118:ETYMOLOGIES AVESTIQUES 863
140:ETYMOLOGIES AVESTIQUES 865
162:ETYMOLOGIES AVESTIQUES 867
175:ETYMOLOGIES AVESTIQUES 869
=== marəγ / marey ===
```


## [2026-09-07T15:58:34.262Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '140,175p' EAV_studies.txt"
}
```


### [2026-09-07T15:58:34.304Z] TOOL RESULT

```
ETYMOLOGIES AVESTIQUES 865
bazvant- postule une racine en b-, ce qui réhabilite l’étymologie par indo-eur. *bhengih- “‘ épaisseur, fermeté ”, et le d- de g. dabqz- et des autres formes qui le supposent est le méme élément adventice qui figure notamment dans av. tkaésa- “ doctrine”’ en face de kaes- *" enseigner" (cf., sur cette sorte de préfixes expressifs, A. Meillet, Ehrengabe W. Geiger, p. 234 seq.).—On observera qu'une notion comme celle d’épaisseur, de fermeté, de corpulence, prétait naturellement a modification expressive.!
La carte des formes de bqz- munies et dépourvues de l’élément d- est malaisée à dresser du fait que dans certains dialectes le traitement de *db- se confondait avec celui de *b-. Ainsi, sanglechi vozok *' fat, thick" est ambigu.—En wakhi, au contraire, oü *b- passait à v-, bāj “ thick ” se dénonce comme provenant d'un mot à *db- initial.
Mais, dans une partie au moins des autres formes où l’on a b-, à savoir dans j. bqz- “ soutenir ”, bqzah- et baënav- ‘* épaisseur ” et dans baluchi baz ‘ beaucoup ” et baz “ épais ”, il nest pas nécessaire de supposer originairement un d- dont il n'y a pas trace et de poser autre chose que la racine nue, telle qu'elle est attestée à coup sür par g. bazvant- et qu'elle reparait en dehors de l'iranien.
9. av. xaoda-
De même que le ph- de skr. phéna- “ écume ” en face de sogd. pēmak, etc., est un procédé expressif parallèle à l's- de lat. spūma, de méme, semble-t-il, la sourde aspirée à l’initiale de av. zaoöa-, v.-p. zauda- '* casque, bonnet " en face de skr. kuhara- “ caverne ”, etc. gr. kev0w *' cacher ", m. irl. codal ** peau ", joue le méme róle que l’s- de pamir. skt “ bonnet haut en peau de mouton ".
10. av. stija
Bartholomae traduit stija de Yt. 10, 71, varaOraynd .. . yd stija nijainti hamore05, par “ combat ”. Mais on attendrait alors un locatif : “ dans un combat," et c'est ainsi que traduit en effet M. Lommel. Puisque le mot est en fait à l'instrumental, il suffit d'y voir un nom d’arme, de la racine *(s)teig- qui donne gr. oriZw “ piquer ”, etc., et, sans s- initiale, notamment skr. téjate “ être pointu”, av. tiyri- ‘flèche ”, etc. L’avestique aurait ainsi conservé, en face de ces dérivés, un nom-racine à s- initiale.
€
! Le p- de lat. pinguis aprés tout d'autre origine.
* gras ", au lieu de l’ f- qu’on attend, n’a peut-être pas
866 J. DUCHESNE-GUILLEMIN-—
11. av. kuiris
Le nominatif singulier kwiris,. V. 14, 9, suppose, comme l'a vu Bartholomae, un thème en -t- ou en -d-. Le commentaire traduit par ‘armure de cou ”” et explique ‘ qui s’attache du casque à la cuirasse "*- Il s’agit en somme d’une pièce articulée, permettant la flexion du cou: Or, le sanskrit possède un terme kora- pour désigner la “ phalange "' et aussi “larticulation des doigts, des orteils, des genoux ”. La racine s'en retrouve en iranien dans av. kava- “ bosse ” (fra-kava-, apa-kava-). Nul doute que l’on doive poser un indo-ir. *kaura- à la base de kuiris. L’u de celui-ci est noté bref par tous les manuscrits sauf par Jp 1 et Mf 2 qui ont souvent la meilleure legon et que suit ici l'édition Geldner. De même que souvent ? doit être lu ax (par exemple dans vitawuhaiti- pour ,vaitahvati-, etc.), à représente ici au. Il reste à fixer le thème et à expliquer la dérivation du * kauris ainsi obtenu.
Pour commencer par l'interprétation la moins vraisemblable, on pourrait songer à un dérivé en -1d- comparable à ceux qui, en grec, se tirent de noms de parties du corps ou d’animaux (cf. Chantraine, La formation des noms en grec ancien, p. 336 seq.) : par exemple yepud- (? long en homérique, bref en prose attique, cf. Vassalini, Riv. Indo- greco-italica, ii, p. 253), *' gant". L'objection est que ce suffixe ne se retrouve ni en iranien, ni en sanskrit, bien qu'il semble antérieur au grec, au moins par sa première partie ?, ainsi qu'en témoigne hitt. kesri- “ gant "1
I] est beaucoup plus simple et plus sûr de poser un kaurit- qui dérive de *kaura- comme skr. daksinit '* avec la main droite" dérive de dáksina- '* droit". Le nom de l’armure de cou est donc, en dernière analyse, l'emploi comme substantif d'un adjectif signifiant littérale- ment ‘‘ possédant articulation " ou bien '* couvrant une articulation ”.
12. av. maraya-
?
Av. maraya-, persan müry '' prairie, páture " est le nom d'action ou d'objet correspondant aux noms d'agent gr. auopBós '' compagnon, berger ”, auophevs ‘ berger”, etc.
13. av. karana-
Le mot karana- m. *' terme, etc." de Bartholomae doit en réalité; ainsi que me le signale M. Nyberg, être posé sous la forme karan-. En
1 Sur ce mot et le nom de la main, voir mon article du BSL. de 1938, p. 211 sq.
ETYMOLOGIES AVESTIQUES 867
effet, les seules attestations qui ne soient pas ambiguës sont les nominatifs pluriels vispe karano, reconnus athématiques par Bthl. lui-même. D'autre part, le persan karän (avec métathèse : Æanar) suppose un accusatif a prédésinentielle longue, comme ravan suppose urvanam, ce qui implique un thème consonantique.—Les raisons pour lesquelles Bthl. a posé, contre ces évidences, un théme en -a- sont apparemment les suivantes. En premier lieu, l'existence des composés akarana-, düraë.karana- et éaôru.karana- ; mais ces mots contiennent l-a- de composition qui se retrouve dans *aradvd.dwhana- en face d'dmhan- etc. (cf. mes Composés, p. 3T). En second lieu, -an- forme d'habitude des neutres, à en croire le Wôrterbuch aux mots srayan- “ beauté”, masan- ‘ grandeur ”, mazan- “id.”, or karanam est masculin ; mais les trois mots cités sont ambigus et c’est arbitraire- ment que Bthl. y voit des neutres alors qu'il pose par ailleurs, sans plus de nécessité, un barozan- masculin. En réalité, karan- peut être a priori aussi bien masculin (proprement nom d’agent) que neutre (proprement nom d'instrument ou d'objet). On peut seulement s'étonner qu'en fait, bien que désignant un instrument ou objet, il soit masculin. Mais lobjection vaudrait aussi pour un théme karana-.1
Cela dit, le neutre qu'on attend se retrouve dans le gr. reXos, qui comporte le sens de *' terme, extrémité " : cette concordance irano- grecque s'ajoute à toutes celles que l'on connait. Sans doute, les suffixes différent, mais on sait qu' n et s alternent fréquemment dans la dérivation indo-européenne. D'autre part, les radicaux ne sont pas exactement superposables, mais le & conservé n'oblige pas plus à séparer karan- de réAos que le c de skr. abhicara- “ serviteur ° (en face de parikara- “‘id.’’) n’est de nature à ruiner le rapprochement avec gr. aupiroûos, lat. anculus.
14. av. duduwr
Le composé duóuw?.buzday- ne figure que dans le F., qui le donne comme un substantif — parmi les termes de droit pénal — et le traduit par ' acte d'angoisser"'. Littéralement, il sagit d’un bahuvrihi: "^ dont l'esprit est —? —"'. Le premier terme, que Bthl. suggére de rapprocher d'all. taub etc., a toute chance, avec son 7 final, de répondre à un simple en -ra-; d'autre part, la syllabe initiale du-, de redoublement, n'a pas plus d'importance que n'en a par exemple
! Pour le ** terme " congu comme animé on songera au lat. terminus.
868 J. DUCHESNE-GUILLEMIN-—
celle de skr. da-dru-ka- ** peste " en face d'av. druka- ^ id." (rapproche- ment déjà vu par Justi, 7 F., 17, p. 88, et redécouvert par M. Krogmann, KZ., 65, p. 141, et par moi-méme). On aboutit en fin de compte à un simple en -ra- et sans redoublement ; ,dubra-, qui est identique à gr. Tv$AÀós. Ce dernier a, comme on sait, le sens général de '' privé de sensibilité ", ainsi qu'en témoigne le passage maintes fois cité de l'Oedipe Roi, 371: rudAos rà T ra tóv re votv td T OppaT el. Le chátiment désigné par duóuw?.buzday- consiste donc à faire perdre connaissance, sans doute à force de coups.
On montre au paragraphe suivant que la racine de duduwi-, gr. TudAds se retrouve ailleurs en avestique.
15. g. dvafsa(h).
Sur le sens de g. dvafsa-, dvafsah-, il y a divergence entre l’avis de Geldner: ‘‘supplice, tortionnaire” et celui qu'exprimait Bartholomae dans ses Arische Forsch., 2, p.177: ‘ destruction ”’. Chacun des deux savants semblait n'avoir considéré qu’un seul des deux passages où le mot figure. De part et d'autre, il s'agit de mauvais traitements infligés aux partisans de la Dru] par Mazdäh ou par A&a; mais le contexte différe.
Au Y., 44, 14, le mot est associé à qstqséa ' traitements hostiles ", à m? morqidyaài “abattre à terre" et à sinam ‘ mise en pieces”, péripéties d'un combat dont rien n'indique qu'il se termine par une destruction, d'autant moins que la strophe suivante parle encore des mêmes partisans de la Dru], rangés en bataille contre ceux de l’Asa. Au Y., 53, 8, au contraire, les mots darozà morov0yaos ““ par le lien de la mort" ne laissent aucun doute sur l'issue du conflit, mais c'est l'idée de “‘ torture ’’ qui cette fois ne ressort pas clairement. Il semble donc que Bartholomae n'a pas vidé la question en se ralliant, dans le Wörterbuch, à la traduction par 'tourment, supplice ". Une seule notion est commune aux deux passages, celle d’un ‘acte violent, entraînant ou non la mort ”. Des parallèles fournis par les littératures avestique et pehlevie permettent de préciser ce sens.
Au Y., 9, 28, le châtiment réclamé pour des malfaiteurs n’est spécifiquement ni la mort ni la torture, c'est ' qu'on leur enlève la force de leurs pieds, qu'on leur obscurcisse l'entendement (ou: qu'on leur arrache les oreilles), qu'on détruise leur esprit’ (cf. W. Havers, IF., 25, p. 382).
ETYMOLOGIES AVESTIQUES 869
```


## [2026-09-07T15:58:53.554Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"amorbos\\|ἀμορβός\\|amorbeus\" POK_full.txt IEC.txt WLD_band3.txt 2>/dev/null | head\necho \"=== POK marəγā / npers. marġ ===\"\ngrep -n \"mar[əeǝ]y[āa]-\\|marġ\\|mary 'Wiese'\\|npers. mary\" POK_full.txt | head -20\necho \"=== POK merg- ===\"\ngrep -n \"merĝ-\\|merǝĝ-\\|Grenze, Rand\" POK_full.txt | head -10"
}
```


### [2026-09-07T15:58:53.634Z] TOOL RESULT

```
=== POK marəγā / npers. marġ ===
=== POK merg- ===
```


## [2026-09-07T15:58:57.211Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la POK* WLD* IEC* AHD* 2>/dev/null | head\necho \"=== grep Wiese in POK ===\"\ngrep -c \"Wiese\" POK_full.txt POK_01.txt POK_02.txt POK_03.txt\necho \"=== apr ===\"\ngrep -n \"Wiese\" POK_02.txt | head -20"
}
```


### [2026-09-07T15:58:57.278Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  850109 Sep  4 14:06 AHD_watkins1985.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3311889 Sep  4 14:06 IEC.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  317372 Sep  4 14:06 WLD_band3.txt
=== grep Wiese in POK ===
POK_01.txt:9
POK_02.txt:15
POK_03.txt:13
POK_full.txt:4
=== apr ===
302:gr.  yalh]  (*gjei-a,  ursprüngl.  ,die  mausartige*  ?)  , Wiesel,  Marder*,  woraus entlehnt  lat.  galea  ursprüngl.  ,*Haube  aus  Wieselfell*,  dann  , Lederhelm ; Haube  auf  dem  Kopf  afrikanischer  Hühner*  (auch  galerus  , Pelzkappe, Perücke*  ist  einem  unbelegten  gr.  *yalr]Q6g  entlehnt) ;  zu  yaXer]  auch  yali- dy'Kü)v  (yaXi-  =  ai.  giri-),  ferner  yaXrjöxjJig,  yaXeößdoXov  , Taubnessel*,  eigent- lich ,Wieselauge*,  wohl  auch  yaXiov  ds.;
2778:lat.  campus  ,Feld'  (ursprüngl.  , Biegung,  Einbuchtung,  Niederung^,  wie lit.  lankä  ,Tal,  Wiese'  zu  lefikti  , biegen') ;
3099:kek-  ,Wiesel,  Iltis*  (?).
3100:Ai.  kasa-  m.  kailkä  f.  ,Wiesel*;  aber  mit  anlaut.  Pal.  lit.  ieskas  ,Iltis*, lett.  sesks  ds.  Ist  balt.  s-  durch  progress.  Assim.  von  *ke§kas  zu  erklären, wobei  die  Nachholung  des  im  Anlaut  verdrängten  k-  im  Ausgang  der 1.  Silbe  durch  den  Anlaut  k-  der  2.  Silbe  verhindert  wurde?  Anders  über lit.  seskas  W.  Schulze  Kl.  Sehr.  630,
3588:6.  ker-  und  ker-,  Farbwurzel  für  dunkle,  schmutzige  und  graue  Farbentöne ; oft  mit  -i   und  -u   erweitert;   kor-ko-  ,Kot,   Sumpf,   ker-no-   ,Eis, Schnee',  kor-men-  , Hermelin,  Wiesel';  s.  die  Erweiterungen  kerb(h)- und  kers-. Ai.  karata-  ,dunkelrot'(?),  kuruiigd-,  kuluiigd-  m. , Antilope',  kirmira-  ,bunt', kdrisa-  n.  , Auswurf,  Dünger',  kardama-  m.  , Schlamm,  Schmutz,  Dünger'; kalka-    m.    ,Kot,    Dreck',    karka-    ,weiß'   (:  mir.    corcach)-    npers.    cardeh ,schwärzlich',  kari,  karah , Schmutz',  pehl.  karic  ,Mist';  gr.  ytögvl^a , Schnupfen, Rotz',    ytOQvvaL '   ^v^ai    Hes.,    y,aQV(j,6v '   fieXav    Hes.,    y,Qovi^(xi '  ^v^at   Hes. ; über  lat.  carbö  s.  oben  unter  3.  ker- ; mir.  corcach  f.  , Sumpf  (:  ai.  kalka-,  karka-,  s.  oben); ahd.  horo.  Gen.  horaweSj  mhd.  hör,  hurwe  ,Kot,  Schmutz'  (*k2'-U')]  ags. horh.  Gen.  horwes,  ahd.  horg  ,schmutzig'  {*kr-k-u-o) ;   aisl.  horr  ra.  ,Nasen- schleim,    Schmutz';   ags.    hrot   m.    ,Rotz',   ahd.    hroz    ds.,    asächs.    hrottag ,rotzig';  ahd.  ruoz,  rouz,  mhd.  7'uoz,  ruost,  asächs.  hrot  ,Ruß';   ags.  hrum m.  ,Ruß',  asächs.  hrum,  mhd.  PN  Rum-olt-,
3591:ven.-illyr.  PN  Carmö  (Steiermark),  rätoroman.  carmün  , Wiesel';  s.  unten kor-men- :
3595:lit.  ,sif ras  , grau,   blaugrau'  {*kf-uo-s),   sirmas  ds.   {*7cr-mo's),   lett.  sirmt ,grau'   (vgl.  ai.  syä-md-   , schwarz,    dunkel'   neben   iyä-vd-    ds.);    lit.   §irvis Jiase';  dazu  lit.  sarmä  f.  ,Reif',  lett.  sarma,  serma  ds.,  lit.  sarmuo,  Wermut , Hermelin'  (:  ahd.  harmo,   ven.-illjr.   carmö)]    h-armnonys   m.  , Wiesel',  mit' Ablaut  ostlit.  Hrmuonelis  ds.,  lett.  sermulis  m.  , Hermelin';
4123:Gr.  'AXejiag'  votsqöVj  Ttr^Xibdeg,  Vj  daav,  ^  vyqöv  Hes.; air.  cluain  , Wiese'  (klop-ni-,  auch  kleu-ni-  möglich); lit.  §lampiij  Uapti  ,naß  werden',  slapumä  ,nasse  Stelle  auf  dem  Felde^, släpias  ,naß',  lett.  slapet  ,naß  machen'; s.  noch  unten  kleu-  , spülen'. WP.  I  497,  Trautmann  306.  "
4311:kormen-  ,Wiesel*,  s.  oben  unter  6.  ker-,
5229:S.  oben  S.  309  E,  wozu  ferner  der  kelt.(?)  FIN  Licus  ,Lech^  (Bayern), die  lit.  FIN  Lieke  und  Leikä,  lit.  liekna  , sumpfige  Wiese^,  lett.  liekna  ds. ; vgl.  illyr.  Epi-licus  portus,  FIN  Pacco-licus  (Bruttium),  mod.  FIN  Lika (Kroatien).
5356:Betrug:^  ksl.  auch  ^Meerbusen,  Tal,  Wiese,  Sumpf,  abg.  sz-lgH  ,inflexus', ksl.  l^^V^  ,Binsen'  Gbiegen  — flechten'),  abg.  It^ög,  -iti  ,trenneii',  sloven. l^i^iti  ,trennen,  sondern'  und  ,biegen'  (dies  die  Grundbed.);
5554:got.  liuhap  , Licht'  (:  lat.  Lücetius,  gall.  Leucetius),  ahd.  as.  lioht  ,hell* und  n.  , Licht',  ags.  leoht  ds. ;  got.  lauhatjan  ,leuchten,  blitzen',  ahd.  lou-  • gazzen  und  schwundstufig  lohazzen  ,flammen,  feurig  sein',  ags.  llegetu  l , Blitz';  ahd.  löh  , bewachsene  Lichtung,  niedriges  Gebüsch',  mnd.  löh,  loch , Gehölz,  Busch',  Namen  wie  Water-loo,  ags.  leah  , offenes  Land,  Wiese'; aisl.  lö  fn.  ,Lichtung'  (=  ai.  lökd-  usw.);   ahd.  laue,  long,   ags.  lieg,  aisl.^
5799:Idg.  *met-  steht  neben  *me-  (oder  *ame-)  in  gr.  (J^aw  ,mähe,  schneide', ahd.  mden  ,mähen',  ags.  mäwan  ds. ;  ahd.  mato-screch  ,Wiesenhüpfer,  Heu- schrecke', nhd.  Matte  ,Wiese,  die  gemäht  wird',  ags.  mced  f.  ,Wiese, Weide'  (*möedwu)j  engl,  meadow,  aschwed.  map  ds.
6410:Arm.  mör  ^Schmutz,  Sumpf  (*mdu-ri-?),  mrur  ^Bodensatz'  {*murur)' gr.  (xiÖQCt)  (*(^vQico),  y.iQO^ai  ^fließen  lassen,  weinen',  &Xi-(xVQrjeLg  ,ins  Meer fließend';  ob  hierher  (xvQLog  ,unendlich',  jxvqlol  ,10.000'?  lat.  muria  ,Salz- lake'?  lit.  murstu,  mürti  , durchweicht  werden',  m.  PI.  mauraX  ,Entengrün', lett.  maurs  m.  ,Rasen',  lit.  mduras  , Schlamm',  ablaut.  müras  m.  ,Schmutz', lett.  murit  ,besudeln';  russ.  mur  m.  murdva  f.,  ,Wiesengras'^  dial.  ,Schimmel', müryj  , dunkelgrau',  usw.;  vgl.  S.  741  mir.  mür  ,Schlamm^
6475:Aisl.  madra  ,galium  verum',  isl.  hvU-,  kross-madra  usw.  ,Galium  boreale, glatte  Wiesenröte',  ahd.  matara  , Färberröte',  ags.  mcedere,  mceddre  f.  ds., mnd.  mede,  afries.  mide  ds. ;  slav.  *modr^  (z.  B.  cech.  modru)    blau'
```


## [2026-09-07T15:59:06.100Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt; do echo \"== $f\"; grep -n \"margo\\|merĝ\\|mer[ĝg]-\" $f | head -6; done\necho \"=== AHD merg ===\"\ngrep -n -i \"merg-\\|margin\\|march\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-07T15:59:07.703Z] TOOL RESULT

```
== POK_01.txt
== POK_02.txt
6108:Ai.  märäti,  märjati,  rnfjäti  , wischt,  reibt  ab,  reinigt',  Partiz.  Perf.  mrstd-, s-Präs.  mxksdti  , streicht,  reibt,  striegelt',  mrksdyati,  mraksdyati  , bestreicht*; av.  mardzaiti,  mdrdzaiti  , berührt  streifend',  zastä-marsta-  , durch  Hand- schlag (d.  i.  Berührung  der  Hände)  geschlossen  (Vertrag)';  d-Präsens  ai. mrddti,  mrddyati  ,ist  gnädig,  verzeiht,  verschont',  av.  mdrdzdä-  ,verzeihen' {mdrdzdika-,  marzdika-  ,sich  erbarmend',  n.  , Barmherzigkeit');  diese  ar. Worte  können  auch  *merg-  enthalten ;  nichtpalatalen  Guttural  zeigt  ai. nir-märgd-h  »Verwischung;  Abgestreiftes,  Abfall',  ni-mxgra-  , sich  anschmie- gend', vi-mjrgvari  f.  , reinlich',  apämargdh-  ,Achyranthes  aspera'  (J.  Schmidt KZ.  25,  114);
6119:WP.  II  298  f.,  WH.  I  741  f.,  II  62  f.,  121  f.,  Trautmann  178,  Specht Idg.  Dekl.  147  f.;  vgl.  auch  melk-  und  merg-.
6314:mnd.  morken  ,zerdrücken',  ags.  murc(n)ian  ,sich  grämen',  murc  , drückend, nagend  (vom  Hunger)' ;  s.  weiteres  unter  (merk-),  merg-  ,morschen,  faulen' usw.
6348:1.  znerg-  (z.  T.  auch  ostidg.  merg-)  ,abstreifen,  abwischen'.
6351:2.  merg-  s.  unter  1.  merk-.
6366:I.  merk-,  merg-,  mergk-,  merog-  ,morschen,  faulen,  einweichen',  ursprüng- lich =  (mer-)^  merk-  ,auf reiben'  (S.  737).  jedoch  schon  grundsprachlich durch   die  Beziehung  auf  die  Feuchtigkeit  verselbständigt;   mroku- , Sumpf. Lat.   marceöj    -ere  ,welk,   schlaff  sein',  marcidus  ,welk,   schlaff',   marcor ,Welkheit,  Morschheit,  Schlaffheit';  gall.  hracis  , Getreideart  zur  Malzberei- tung'; mir.  mraich,  hraichj  cymr.  corn.  brag  ,Malz',  d.  i.  ,eingeweichtes,  ge- quollenes Getreide';  gallorom.  Hracu-  (*'mraku-) , Morast'  (:  slav.  *morky  ds.), cymr.  hrag-wellt  , Sumpfgras';  gall.  mercasius  ,Sumpf',  afrz.  marchais]  gall. emhrektoii  ,eingetunkter  Bissen'  (daraus   lat.  imhractum)-  mir.  bren,  cymr. braen  (*mrakno-)  ,morsch,  faul';  mhd.  mer(e)n,  mnd.  meren  ,Brot  in  Wein oder  Wasser  eintunken'  {*merhen),  lit.  merkiüj  merkti  ,(Flachs)  einweichen',
== POK_03.txt
223:aisl.  öss  m.  »Flußmündung'  (germ.  *ösaz\  hierzu  ags.  ör  n.,  öra  m. ,Rand,  Anfang';  aus  ags.  ör  ist  mir.  or  ,ora,  margo,  linea',  acymr.  ör  ds. entlehnt.
2423:ksl.  pokromh  ,margo  panni',  russ.  kromd  ,Brotschnitte,  Kante',  ksl.  ukromt Adv.  jSingulatim'  (,*abgetrennt'),  aksl.  krome  Adv.  ,außen,  draußen';  ablaut. russ.  dial.  kremh  f.  , Abschnitt  des  Waldes' ;
=== AHD merg ===
178:The notion of government and sovereignty was well represented. The presence of the old word for tribal king, *reg- (reg-'), only in the extreme east (RAJAH) and the extreme west (Latin réx, Celtic -rix) virtually guarantees its presence in the earliest Indo-European society. (Here is an example of the phenom- enon of marginal or peripheral conservation of a form lost in the central innovating area). Roman tradition well attests the sacral char- acter of kingship among the Indo-Europeans. The functions of king and priest were differ- ent aspects of a single function of sover- eignty. It is this which is symbolized by the divine name *dyeu-poter- (deiw-), the chief of the gods.
261:ag-. To drive. 1. Latin agere, to do, act, drive, conduct, lead: ACT, AGENDUM, AGENT, AGILE, AGITATE; (ALLEGE), AMBAGE, AMBIGUOUS, (ASSAY), (CACHE), COAGULUM, COGENT, ESSAY, EXACT, (EXAMINE), (EXIGENT), FUMI- GATE, INTRANSIGENT, LEVIGATE, LITIGATE, NAVIGATE, OBJURGATE, PRODIGAL, RETROACTIVE, SQUAT, TRANS- act. 2. Greek agein, to drive, lead: -AGOGUE, AGONY; ANAGOGE, (ANTAGONIZE), CHORAGUS, DEMAGOGUE, EPACT, GLUCAGON, HYPNAGOGIC, MYSTAGOGUE, PEDA- GOGUE, PROTAGONIST, STRATAGEM, SYNAGOGUE. 3. Suf- fixed form *ag-to- in Celtic *amb(i)-ag-to-, “one sent around” (*ambi, around; see ambhi), in Latin ambactus, servant (> Medieval Latin ambactia, office): AMBASSA- DOR, EMBASSAGE, (EMBASSY). 4. Suffixed form *ag-men- in Latin agmen, a train, a moving forward, a marching column, group: AGMINATE. 5. Suffixed form *ag-ti-, “weighing” (Greek agein, “to lead,” has a sense “to weigh”), whence adjective *ag-ty-o-, “weighty,” in Greek axios, worth, worthy, of like value, weighing as much: AXIOM; AXIOLOGY, CHRONAXY. 6. Possibly suffixed form *ag-ro-, driving, pursuing, grabbing, in Greek agra, a seizing: PELLAGRA, PODAGRA. Derivative agro-. [Pok. ag- 4]
730:tive masculus, male, manly: MACHO, MALE, MASCULINE; EMASCULATE.] mat-. A kind of tool. Old English mattuc, mattock (prob- ably borrowed from Vulgar Latin *mattea): MATTOCK. [Pok. 2. mat- 700.] mater-. Mother. Based ultimately on the baby-talk form ma-2, with the kinship term suffix -fer-. 1. Germanic *méthar- in Old English mddor, mother: MOTHER}. 2. Latin mater, mother: MATER, MATERNAL, MATERNITY, (MATRICULATE), MATRIX, MATRON; MADREPORE, MATRI- MONY. 3. Greek métér, mother: METRO-; METROPOLIS. 4, Latin mdteriés, materia, tree trunk (< “matrix,” the tree’s source of growth), hence hard timber used in carpentry, hence (by a calque on Greek Aulé, wood, matter) substance, stuff, matter: MATERIAL, MATTER. 5. Greek compound Démétér, name of the goddess of produce, especially cereal crops (dé-, possibly meaning “earth”): DEMETER. [Pok. mdter- 700.] math-. Worm. With uncertain preform, but clearly re- lated, is Old English moththe, moth: motu. [Pok. 1. math- 700.] [Mawort-. Name of an Italic deity who became the god of war at Rome (and also had agricultural attributes), hence also the name of the planet Mars (doubtless from its red color, the color of blood). Latin Mars (stem Mart-), Mars: MARCH, MARS, MARTIAL, MARTIAN.] mazdo-. Pole, rod, mast. Germanic *mastaz in Old Eng- lish mest, mast: MAST}. [Pok. mazdo-s 701.] me-1. Oblique form of the personal pronoun of the first person singular. For the nominative see eg. 1. Germanic *mé- in Old English mé (dative and accusative): ME, MYSELF. 2. Possessive adjective “mei-no- in Germanic *min- in: a. Old English min, my: MINE?, My; b. Middle Dutch mijn, my: MYNHEER. [Pok. 1. me- 702.] me-2, In the middle of. 1. Suffixed form *me-dhi in Germanic *mid- in Old English mid, among, with: MID- WIFE. 2. Suffixed form *me-ta in Greek meta, between, with, beside, after: META-. See also medhyo-. [Pok. 2. me- 702.] mé-1, Expressing certain qualities of mind. Contracted from *meo-. 1. Suffixed o-grade form *mé6-to- in Ger- manic *méthaz in (i) Old English méd, mind, disposition: MooD! (ii) Old High German muot, mind, spirit, in German Gemiit, spirit, feelings, temperament: GEMUT- LICH, GEMUTLICHKEIT. 2. Perhaps Latin més (< *mé-s-), wont, humor, manner, custom: MORAL, (MORALE), MORES, MOROSE. [Pok. 5. mé- 704.] m6-2, To measure. Contracted from *meo-. I. Basic form mé-. 1. Suffixed form *mé-lo- in Germanic *mélaz in Old English m#l, “measure, mark, appointed time, time for eating, meal”: MEAL?; PIECEMEAL. 2. Suffixed form *mé-ti- in Latin métiri, to measure: MEASURE, (MEN- SURAL); (COMMENSURATE), DIMENSION, IMMENSE. 3. Possibly Greek metron, measure, rule, length, propor- tion, poetic meter (but this is referred by some to med-): METER!, METER?, (METER?), -METER, METRICAL, -METRY; DIAMETER, GEOMETRY, ISOMETRIC, METROLOGY, METRO- NOME. 4, Suffixed form *mé-trd- in Sanskrit mdtrd, a measure: MAHOUT. II. Extended and suffixed forms *mén-, *mén-en-, *mén-s-, *mén-dt-, moon, month (an ancient and universal unit of time measured by the moon). 1. Germanic *ménén- in Old English ména, moon: Moon; (Monpay). 2. Germanic *ménéth- in Old English ménath, month: MONTH. 3. Greek mén, méné, month: AMENORRHEA, CATAMENIA, DYSMENORRHEA, (MENARCHE), MENISCUS, MENOPAUSE. 4. Latin ménsis, month: MENSES, MENSTRUAL, (MENSTRUATE); BIMES- TRIAL, SEMESTER, TRIMESTER. [Pok. 3. mé- 703, ménot- 731. fen Big. Contracted from *meo-. 1. Suffixed (compara- tive) form *mé-is- in Germanic *maiz6n- in Old English mara, greater, and madre (adverb), more: MORE. 2. Suf- fixed (superlative) form *mé-isto- in Germanic *maista- in Old English m&st, most: Most. 3. Suffixed o-grade
757:merg-. Boundary, border. 1. Germanic *mark-, bound- ary, border territory; also to mark out a boundary by walking around it (ceremonially “beating the bounds”); also a landmark, boundary marker, and a mark in general (and in particular a mark on a metal currency bar, hence a unit of currency); these various meanings are widely represented in Germanic descendants and in Romance borrowings: a. Old English mearc, boundary, landmark, sign, trace: MARK}; b. Middle Dutch mark, border: MAR- GRAVE; ¢. Old French marc, marche, border country: MARCH?, (MARQUEE), MARQUIS, (MARQUISE); d. Late and Medieval Latin marca, boundary, border: MARCHIONESS; e. Old Italian marcare, to mark out: DEMARCATION; f. Old English marc and Middle High German marke, a mark of weight or money: MARK?; g. Swedish mark, a mark of money: MARKKA. 2. Germanic *markja-, mark, border, in Old Norse merki, a mark, possible source of Old French marque, a mark: MARQUETRY; REMARK. 3. Germanic denominative verb *mark6dn in Frankish *markoén, to mark out (> Old French march(iJer, to trample): MARC, MARCH!, 4, Latin margo, border, edge: MARGIN. [Pok. mereg- 738.]
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1817:MARASCA om- MARASCHINO om- MARASMUS- mer-2 MARC merg- MARCESCENT merk-1 MARCH! merg- MARCH2 merg- Marcu Mawort- MARCHIONESS merg- MARE! marko-
1818:MARE? mori- MARGARIC margarités MARGARIC ACID margarités MARGARINE margarités MARGARITE! margarités MARGARITE2 margarités MARGIN merg- MARGRAVE gravo-, merg- MARICOLOUS mori- MARICULTURE mori- MARINARA mori- MARINE mori- MARITAL mari- MARITIME mori- MARK! merg-
1819:MARK2 merg- MARKET merk-2 MARKKA merg- MARLINE mer-3 MARMALADE melit-, mélon MARQUEE merg- MARQUETRY merg- MARQUIS merg- MARQUISE merg- MARRAM_ mori- MARROW mozgo- MARRY! = mari-
2178:REIGN reg-! REIMBURSE bursa REINDEER dheu-1, ker-1 REINFORCE bhergh-2 REITERATE i- REJECT yé- REJOICE gau- REJUVENATE yeu- RELAPSE leb-! RELATE tele- RELAX slég- RELAY slég- RELEGATE leg-1 RELENT lento- RELIEVE leg¥h- RELINQUISH leikw- RELUCENT leuk- RELUCT leug-! RELY leig-1 REMAIN men-3 REMAND man-2 REMARK merg- REMEDY med- REMEMBER (s)mer-! REMEX ere-! REMINISCENT men-! REMIT (s)meit(a)- REMORA mere- REMORSE mer-2 REMOTE meue- REMOVE meue- REMUDA mei-1 REMUNERATE mei-! RENAISSANCE gene- REND rendh- RENDER do- _ RENDEZVOUS wOS RENEGADE ne RENEGE ne RENITENT kneigh- RENOUNCE neu-! RENOVATE newo- RENOWN no-men- RENT! do- REPAIR! pere-1 REPAND pete- REPARTEE pere-2 REPAST pa- REPEAT pet- REPEL pel-6 REPENT2 rép-1 REPERTORY pere-! REPINE kWei-1 REPLENISH pele-! REPLETE pele-1 REPLEVIN plegan REPLICATE plek- REPORT per-2 REPOSE! paus- REPOSIT apo- REPREHEND ghend- REPRESENT e@S- REPRESS per-5 REPRIMAND per-5 REPRISAL ghend- REPRISE ghend- REPROACH pert REPROVE per? REPTILE rép-1 REPUBLIC ré- REPUDIATE (s)peud- REPUGN peuk- REPUTE peu-
```


## [2026-09-07T15:59:24.131Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK mantellum ===\"\ngrep -n -i \"mantellum\\|mantele\\|mantile\" POK_full.txt POK_01.txt POK_02.txt POK_03.txt WLD_band3.txt AHD_watkins1985.txt IEC.txt 2>/dev/null | head -10\necho \"=== IEC mant ===\"\ngrep -n -i \"mantellum\\|mantel\" IEC.txt | head -5\necho \"=== ARY مرغ / مشک ===\"\npython3 - <<'EOF'\nimport re\nfor f in ('incoming/ARY/ARY_pages.txt','incoming/ARY/ARY_latin_index_pages.txt'):\n    d=open(f,encoding='utf-8',errors='replace').read()\n    for w in ('مرغزار','مرغ','مشک','MARGH','MASHK','MASK'):\n        idxs=[m.start() for m in re.finditer(w,d)][:2]\n        for i in idxs:\n            print('##',f,w,'::',d[max(0,i-150):i+250].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T15:59:25.775Z] TOOL RESULT

```
=== POK mantellum ===
POK_03.txt:4475:2.  terg-:  lat.  tergö,  -ere,  tergeo,  -ere  , ab  wischen,  reinigen',  mantelum, nantele  , Handtuch'  (*man-terg-sli;  zu  manus  S.  740),  ablautend  umbr.  Akk. jg.  mantrahklu,  mandraclo  ,mantele'  {^-träg-kld)\  got.  pairko  n.  ,Loch^, iefstufig  mnd.  dork  , Kielraum',  ags.  durruc  ,cumba',  ,caupolus';
=== IEC mant ===
=== ARY مرغ / مشک ===
## incoming/ARY/ARY_pages.txt مرغ ::  قاطع زا 9 : ۶۶۴ 10 84 او  یادداشت: 1  ۱- چم این واژه در برهان قاطع : چنین است: قلاب» کجکه (قلابی که با آن فبل را رانند)» پنجه و انگشتان مردم»  چنگال مرغان و جانوران دیگر (برهان قاطع :: ۹3۴)  ۲ چم این واژه در اوستی: بازو,  چم این واژه در کردی: دست.  چم این واژه در ایسلندی کهن: خانه,  چم این واژه در اکثر زبان‌های ژرمنی: قلاب, ۱  1  | جمانگلیس سرواژهی را ی ۵5 اوستایی ((4874): 37 ,۲17 نروژی (08۷۴01۵۷
## incoming/ARY/ARY_pages.txt مرغ :: 2/5 گالی (37/ال0۸): ۷۷ 0 (866) 7 برهان قاطع + ۷۱ بادداشت: ۹ ۱ چم این واژه در اوستایی و پارسی باستان و پهلری و همه‌ی زبان‌های هند و اروپایی دیگر: تخم (مرغ). ۲ واژه‌های "خاویار" و "خاک" و "خاگینه" نیز همریشه‌ی واژه‌ی "خایه" هستند. اوستایی (/472574): ۸8۰ ر-۸۷1ا وه پارسی باستان (/۸ا۸878 02): -1۸۸۷ پسگشت‌ها انخ هبات سانسکریت (84(51)/7): ۳ ۰ ,۸31۸0۸5 ,۴71۸0۸7 809 غل‌لاه ارمثی (01فا/47/52): ادن ۱۵ برهان 
## incoming/ARY/ARY_pages.txt مشک :: اژه‌ی [17۳۳۸ هل" آلمانی همریشه است. همینطور واژه‌ی فارسی «دندان» با واژه‌ی آلمانی 2۸1721 همريشه است ولی دگرگونی تلفظ آنهاء شناخت خویشی نزدیکه آنها را مشکل مي‌کند. با وجود همه‌ی این دشواری‌ها کوشیده‌ام که تا آنجا که از دستم برمی آمده همه‌ی واژه‌های [pdf page 45] ۶ | ریشه‌های هندو اروپایی زبان فارسی : همریشه‌ی هند و اروپایی را در این کتاب گرد آوری نمایم ولی لازم می‌دانم توجه خواننده را به یک نکته ج
## incoming/ARY/ARY_pages.txt مشک :: 011*) و در صفحه‌ی ۷ نیز واجربشه‌ی ۸613 را برای واژه‌های ,آل۸ و غیره می‌دهد. به پندار من این دو واجريشه یکی هستند ولی رای مزید اطمینان جلو واجریشه‌های مشکوکه نوشته‌ام(شاید). ۲ معلی این واژه در سانسکریت: آرزو؛ نبرد. معنی این واژه در یونانی؛ نیاز» مشقت. معنی این واژه در زبان‌های ژرمنی؛ ترس» درکشیدن. اوستایی (۷ل۸۲837۸): 3 آلمانی (4۸/ل05): زانایا ۱ پهلری (ماتلهه): زرا انگلیسی کهن (8#لا80 02): ۰ ۴۲-30 ک
## incoming/ARY/ARY_latin_index_pages.txt MASHK ::  sabi ou, MAMATTI, MANDATI, MATTA-  MECH RUSSIAN) gy, MARSHA HAVESTAN) (glues) MECHD :(BULGARIAN) 65 ,\sh, PAHLAVI) 65 shy MAISHAS :(LITHUANIAN) gl.) MASHK, MASHKIZAG  MAIss LATVIAN) (3) 3 MSHK SOGADIAN) «ghee MOASIS (OLD PRUSSIAN) nS ous 4 SANSKRIT) cy Sle, us  MESHAS, MASHAKA = * REFERENCES eke HOLD SCANDINAVIAN) oyS igis\ | POKORNY, Fy MEISs DELAMARRE: HOLD HIGH GERMAN) vy galt (SAC EN PEAU) 14
## incoming/ARY/ARY_latin_index_pages.txt MASHK :: u, MAMATTI, MANDATI, MATTA-  MECH RUSSIAN) gy, MARSHA HAVESTAN) (glues) MECHD :(BULGARIAN) 65 ,\sh, PAHLAVI) 65 shy MAISHAS :(LITHUANIAN) gl.) MASHK, MASHKIZAG  MAIss LATVIAN) (3) 3 MSHK SOGADIAN) «ghee MOASIS (OLD PRUSSIAN) nS ous 4 SANSKRIT) cy Sle, us  MESHAS, MASHAKA = * REFERENCES eke HOLD SCANDINAVIAN) oyS igis\ | POKORNY, Fy MEISs DELAMARRE: HOLD HIGH GERMAN) vy galt (SAC EN PEAU) 148 MEISA
## incoming/ARY/ARY_latin_index_pages.txt MASK :: N "REFERENCES eat MAIN, MANDU (KURDISH) 62, | Troromm OOS~C~SD MANTA, MANAGH (BALUCHD 23h BARNHART: (MANSION) 631 MANDA AFGHAND) (5-4) is! MACKENZIE: MASK :(TOKHARIAN A) A 655 (REMAIN) 130, (STAY) 134 MASK {(TOKHARIAN B) B 5 55 BUCK: 838 (SANSKRIT) 3 Sle ONIONS: (MANSION) 533 MAN., MAMANDBT SKEAT: (REMAIN) 509 MNAM, MUNAL — :(ARMENIAN) 4 140s seb oby ‘MENO, MENEIN GREER) lip, ‘MANEO, MANERE LATIN)
## incoming/ARY/ARY_latin_index_pages.txt MASK :: mm OOS~C~SD MANTA, MANAGH (BALUCHD 23h BARNHART: (MANSION) 631 MANDA AFGHAND) (5-4) is! MACKENZIE: MASK :(TOKHARIAN A) A 655 (REMAIN) 130, (STAY) 134 MASK {(TOKHARIAN B) B 5 55 BUCK: 838 (SANSKRIT) 3 Sle ONIONS: (MANSION) 533 MAN., MAMANDBT SKEAT: (REMAIN) 509 MNAM, MUNAL — :(ARMENIAN) 4 140s seb oby ‘MENO, MENEIN GREER) lip, ‘MANEO, MANERE LATIN) oS [pdf page 462] | FY | Cyd po 4) ole i HOLD CHU
```


## [2026-09-07T15:59:44.000Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nd=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\nfor w in ('MASHK','MASHAKA','MOASIS','MAISHAS'):\n    for m in list(re.finditer(w,d))[:3]:\n        i=m.start()\n        # find nearest [pdf page N] before\n        pg=list(re.finditer(r'\\[pdf page (\\d+)\\]', d[:i]))\n        print('##',w,'pdf page',pg[-1].group(1) if pg else '?')\n        print(d[max(0,i-1200):i+500].replace('\\n',' '))\n        print('-----')\nEOF"
}
```


### [2026-09-07T15:59:46.155Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T15:59:50.124Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nd=open('incoming/ARY/ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read()\nfor m in list(re.finditer('MASHK, MASHKIZAG',d))[:2]:\n    i=m.start()\n    pg=list(re.finditer(r'\\[pdf page (\\d+)\\]', d[:i]))\n    print('pdf page', pg[-1].group(1) if pg else '?')\n    print(d[max(0,i-2500):i+1500])\nEOF"
}
```


### [2026-09-07T15:59:52.214Z] TOOL RESULT

```
pdf page 472
 poh
MARMAROS (gly so5ly 1 A305 19 59 cu! PS oJ Stew OL a aly Say
eaileat gabe
MUZD ARURDISH) 6525 MIZHDA AAVESTAN) glo}
(SANSKRIT) ey Suile MIZD, MOZD PAHLAVI) 6 shay
MIDHA, MIDHAMA MIZD, MYZD HOSSETIC) gus s\
[pdf page 470]
”v
Fl | bye
MZDA RUSSIAN) «3 MISTHOS GREEK) gly
MZDA (CZECH) Soy MIZDO GOTHIC) S35
MZDA BOHEMIAN) gary MOLD SCANDINAVIAN) 6 ssthel
MZDA HSLOVAR) 61 gle MEDA, MIEDA
MEDA — (OLD SAXON) ofS i S-
‘REFERENCES bethy MEDE HOLD FRISIAN) oS 523
POKORNY: SSSS*S~*«SG HOLD HIGH GERMAN) of alt
BARNHART: (MEED) 648 META, MIATA
MACKENZIE: MIETE GERMAN) glT
(HIRE) 118, (PAY) 126 HOLD ENGLISH) pS gS
ONIONS: (MED) 567 MEORD, MED, MEDA
SKEAT: (MEED) 369 MEED ENGLISH) godS1
RAMAT: B (OLD CHURCH SLAVIC) 455.3%!
Tees sebGouy| - MUZDA, MIzDA
icetlook
eel a aly goat Shah Slory 5S "oop edly

MODROD (BULGARIAN) 5 ake MAZDA, MAZDAH, «(AVESTAN) gita3!

LITHUANIAN) lp MAZDRA- {OLD PERSIAN) lal, oo
MANDRAS, MUNTER MAZA, MAZDESN —:(PAHLAVI) hy

LATVIAN) (3) gi) MEDHA SANSKRIT) <4 Sui
MUODRS, MUOZHS GREEK) gli,
MYNNU AWELSH) 5) MANTHANO, MATHEIN =, “4!
MUND ALBANIAN) gigT : J@hcortue) Saf

MUNDON, MUNDERI
REFERENCES cntBny :(OLD SCANDINAVIAN) 75 g-thn!
POKORNY, = SS*S~*~«SD MUNDA
MACKENZIE: (MAZDEAN) 123 (OLD HIGH GERMAN) pf gist
| BUCK: m2 MUNTAR, MUNTER, MENDI,

ever Misha delice MENDEN
[pdf page 471]
Sy whe | FVY
lentloal
ile A isa 9 ey SG 50 o3hy yl oe 1
J yh. ee aTisln Sole
% pele pe pe Ste SSF 3 3s ol p
ea chal ys Let sda 9 AS glu 2 cal pt
23 dBA 3 Gd 205s oll ee
: Shas BLT 52 Sly ol oe
sel aag a" GIE" y "ee 3” PF eMAZDA plies! ,> -¥
MUCHUTU PAHLAVI) 6 hy
HOLD IRISH) 4S 5) p\ MICHAK, MIZH, MIZHAG
DE-MECCIM KURDISH) 2,
MYGR (WELSH) 3 MIJGAN, MIZHL, MIZHANK, MUJGAL
ABALUCHD) gx de
‘REFERENCES Wena MICAC, MISHASH, MIZHAGHAN |
POKORNY, —SSS~S~«STABTAB NIMISHA (SANSKRIT) ey Sst. |
MACKENZIE: (EYELASH) 113 MICO, MICARE X(LATIN) 3
Leeds Look eb oy (OLD BULGARIAN) 55 j\aly
~ Sent loo
: sree ahem 1oSY Ob5 29 Sly onl |
MYSLU (OLD BULGARIAN) aS 66 lil *MUSTI (OLD PERSIAN) kl poh
LITHUANIAN) gg.) MUST (PAHLAVI) 5 pgp
MAUDZHIG, MAUSTI MUTHOS GREEK) sbi
MAUDJAN AGOTHIC) 3
[pdf page 472]
Mle
MACKENZIE: (COMPLAINT) 107 ‘REFERENCES bok,
Jeetloal
Om tae gin 85 32 05a onl
MADHA., MAD-—.(AVESTAN) gleeyl

REFERENCES beth MAST HMPAHLAV) 6 hy

POKORNY, SSS ag MEST KURDISH) «53,5
AMINDAROV: (DRUNK) 215 MADYATI, (SANSKRIT) cy Sl.

Tey sabi ou, MAMATTI, MANDATI, MATTA-

MECH RUSSIAN) gy, MARSHA HAVESTAN) (glues)
MECHD :(BULGARIAN) 65 ,\sh, PAHLAVI) 65 shy
MAISHAS :(LITHUANIAN) gl.) MASHK, MASHKIZAG

MAIss LATVIAN) (3) 3 MSHK SOGADIAN) «ghee
MOASIS (OLD PRUSSIAN) nS ous 4 SANSKRIT) cy Sle, us

MESHAS, MASHAKA = *
REFERENCES eke HOLD SCANDINAVIAN) oyS igis\ |
POKORNY, Fy MEISs
DELAMARRE: HOLD HIGH GERMAN) vy galt
(SAC EN PEAU) 148 MEISA
‘MACKENZIE: (MUSSUCK) 124 MOLD CHURCH SLAVIC) oS «5 sai
ror ebb olay MECHU
MIECH POLISH) jleng)
[pdf page 473]
Kae | WE
[ee eS |
+ MUSHK (PAHLAVI) 5 shy
Le REFERENCES beh MUSKAH (SANSKRIT) Sie
POKORNY: =SO*~*~«*C~*~«S MOsKHos GREEK) ly
BARNHART: ~ (MUSK) 688 Muscus (LATIN) op3V
MACKENZIE: (MUSK) 124 MusC APRENCH) il
ONIONS: (MUSK) 598 MUSCH, MOSCHUS :(GERMAN) .glT
SKEAT: (MUSK) 392 MUSK ENGLISH) SS)
ree sbi bby MuskUS (DUTCH) sata
Jeblaol
: gb ey SL 05 22S cal oe
MAGO PORTUGUESE) i MAGU, MAGA —(AVESTAN) pls!
MAGAN, MAHTS — (GOTHIC) eS, OLD PERSIAN) jie gj)
(OLD SCANDINAVIAN) 4S eL0! MAGUSH, MAGUS, MAG
MEGA, MAGA, MUGA, MA (PAHLAVI) 65 3h,
MUGA, MEI (OLD FRISIAN) (45523 MAGU, MAGUPAT, MOGHMARD
(OLD HIGH GERMAN) 4S gilt MOKATS _:(TOKHARIAN A) A 6,00
MAGAN, MUGAN, MAG : (SANSKRIT) x Site
MAGIE (GERMAN) (glST MAGHA, MAGHAVAN-
OLD ENGLISH) 5 5831 ARMENIAN) gs)!
MAGAN, MAG MOG, MOGPET, MARTHANX
MIGHT ENGLISH) g-lSil GREEK) gy
OLD CHURCH SLAVIC) 553%! MAGIKE, MAGIKOS, MAGOS
MOG, MOSHTI MAGICE, MAGUS ALATIN) ya
MOSEU LARUSSIAN) .g9 MAGE (FRENCH) 413
(LITHUANIAN) Jl J MAGO A(SPANISH) glilyel
MAGULAS, MOKETI MAGO HUTALIAN) gal
[pdf page 474]
WO ge |
‘MACKENZIE-MOGH (MOGHMARD) 56 ‘REFERENCES eeran
ONIONS: “pox SSs—~S~SY
MOGH (MOGHM
```


## [2026-09-07T16:00:12.269Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nd=open('incoming/ARY/ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read()\nfor w in ('MARGH','MAREGHA','MARGZAR','MARG '):\n    for m in list(re.finditer(w,d))[:3]:\n        i=m.start()\n        pg=list(re.finditer(r'\\[pdf page (\\d+)\\]', d[:i]))\n        print('##',w,'pdf page', pg[-1].group(1) if pg else '?')\n        print(d[max(0,i-600):i+600])\n        print('---')\nEOF"
}
```


### [2026-09-07T16:00:14.211Z] TOOL RESULT

```
## MARG  pdf page 474
AGERMAN) glsT MAZGH —:(OLD PERSIAN) gkuel, oo)
HOLD ENGLISH) oS gulSsl MAZGA,MASG (PAHLAVI) «5 Ly,
MEARH, MEARG MAGHZ HOSSETIC) gins)
MARROW HENGLISH) galSl MEGZ, MEJU KURDISH) «53,5
MARV (DANISH) S)\ail MAZHG (BALUCHI) og sh
MERG (SWEDISH) 3 yo MAGHZA HAFGHANI) (3.4) git
MARV (NORWEGIAN) $354 MASSUNT —.(TOKHARIAN A) A 5 ni
MERG DUTCH) sacle MAJJAN (SANSKRIT) 2 Sie
OLD CHURCH SLAVIC) oS 59%o1 MICHOUG, MIDK (ARMENIAN) (go!
MozcU , MOELLE (FRENCH) 443 Tad
M6zG POLISH) lig) MOELLO «4h sPANISH) glal-l
MOzG RUSSIAN) go OLD SCANDINAVIAN) gS g.tche'
. MOZAK ASERBIAN) «ype MERGR
MOZEG BOHEMIAN) yaa y MARG — (OLD SAXON) 4S SL
MOZOG SLOVAK) Lal OLD FRISIAN) oS 623
SMAGENES —— (LITHUANIAN) gi} MERG, MERCH
MUSGENO :(OLD PRUSSIAN) oS 59 x OLD HIGH GERMAN) 4S glalT
[pdf page 475]
ok | we
‘MACKENZIE: REFERENCES beth ‘
(BRAIN) 105, (MAROW) 123 POKORNY: ~=—S*S~S*~S~«SB
Buc hy . 215 BARNHART:
tof ONIONS. (MARROW) 557 (MARROW) 635-636
“| swear: (MARROW) 363 DELAMARRE:
my _ tebb aby (MOELLE, CERVELLE) 148
BST ra |
MUCKE GERMAN) (glsT MAKHSHI HAVESTAN) glee 3|
HOLD ENGLISH) oS galS\ PAHLAVI) 5 shy,
MYGG, MYCG, MYCGE MAKHSH, MAGAS, MAKAS
MIDGE ENGLISH) gudSsi MESH, MYSH KURDISH) 53,5
MYG H(DANISH) Sail
---
## MARG  pdf page 476
) 45 (gotcha!
MUSO — {OLD PRUSSIAN) oS oo. MUGGIA (OLD SAXON) oyS 5 ,-Ste |
MOZE ALBANIAN) SUT (OLD HIGH GERMAN) yf AST i
MUCKA, MUGGA |
[pdf page 476]
i, |
i WL Cte” Coed AO 4) peel tele
BUCK: 193 ‘REFERENCES bathe
ONIONS: (MIDGE) 575. POKORNY Ss™~S~S~«m
SKEAT: (MIDGE) 374 BARNHART: (MIDGE) 659-660
nerd seb oly DELAMARRE:  (MOUSTIQUE) 143
MACKENZIE: (FLY) 114
feta
SS 3 Wags Ole Esl ast a5 SOW) 9 Hts} 2039 oll pr
AMPFER (GERMAN) gllT AMLAS SANSKRIT) Sy Sil
AMPER SWEDISH) $48. yo AMOKH ARMENIAN) «us
AMUOLS LATVIAN) (33),.g5 93 AMARUS AALATIN) 3
TAMLE, EMBLE (ALBANIAN) .g\JT AMER (FRENCH) sil
AMARG (SPANISH) glilel
‘REFERENCES. bok AMARO AUTALIAN) glx}
DELAMARRE: 163,230 AMAR (RUMANIAN) sag
BUCK 1033-1035 AMARGO = —:(PORTUGUESE) gs
THOMO STIFVE Mics dab (OLD SCANDINAVIAN) 5;scle\
YTOD (le) SVP eae Keays APR
leatlasl
i GML bald eY sh tl ably 7 lacey
serlns SEF AS) seth gts} SOAP MHS Obs 2 WS cl ew
ABA AIT Ob5 2 05s cal pe
9m Seely ge pT hg lensl s Sle odes 4 sll clad 22 ye” baal (leila
HetliF Wee ol gly!
[pdf page 477]
ae Ln
eh MAMME (GREEK) 3h y .
‘REFERENCES beth MAMMA, MAMMILLA (LATIN) 53
BUcKOSOS~S«S MAMMELLE APRENCH) 3
ONIONS: (MAMMA) 549 MAMA SPANISH) glib!
SKEAT: (MAMMALIA) 3
---
```


## [2026-09-07T16:00:21.506Z] TOOL CALL #66: Bash

```json
{
 "command": "ls site/pages/321.jpg 2>/dev/null; pdftoppm -f 321 -l 321 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg321 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T16:00:23.671Z] TOOL RESULT

```
site/pages/321.jpg
total 1244
drwx------ 2 sfmqrb sfmqrb   4096 Sep  7 12:00 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    251 Sep  7 11:49 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb  85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb 161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb  19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb  40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb  97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb 163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb     40 Sep  7 11:49 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1308 Sep  7 11:54 v2001.txt
```


## [2026-09-07T16:00:26.768Z] TOOL CALL #67: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg321.png"
}
```


### [2026-09-07T16:00:27.109Z] TOOL RESULT

```

```


## [2026-09-07T16:00:27.104Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T16:00:51.155Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt WEB_vol1.txt RCH.txt; do echo \"== $f\"; grep -n -i -o \".\\{0,90\\}mussuck.\\{0,140\\}\" $f | head -3; grep -n -i -o \".\\{0,60\\}mandil.\\{0,140\\}\" $f | head -3; done"
}
```


### [2026-09-07T16:01:15.789Z] TOOL RESULT

```
== FSD_vol1.txt
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,140}
                         \___exceeds complexity limits


ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,140}
                        \___exceeds complexity limits


== FSD_vol2.txt
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,140}
                         \___exceeds complexity limits


ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,140}
                        \___exceeds complexity limits


== FSD_vol3.txt
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,140}
                         \___exceeds complexity limits


ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,140}
                        \___exceeds complexity limits


== FSD_vol4.txt
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,140}
                         \___exceeds complexity limits


ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,140}
                        \___exceeds complexity limits


== WEB_vol1.txt
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,140}
                         \___exceeds complexity limits


ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,140}
                        \___exceeds complexity limits


== RCH.txt
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,140}
                         \___exceeds complexity limits


ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,140}
                        \___exceeds complexity limits
```


## [2026-09-07T16:01:21.792Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re,glob\nfiles=['FSD_vol3.txt','FSD_vol2.txt','WEB_vol1.txt','RCH.txt']\nfor f in files:\n    try: d=open(f,encoding='utf-8',errors='replace').read()\n    except: continue\n    for w in ('mussuck','Mussuck','mandil','Mandil','mashk'):\n        for m in list(re.finditer(w,d))[:2]:\n            i=m.start()\n            print('##',f,w,'::',d[max(0,i-120):i+300].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T16:01:24.882Z] TOOL RESULT

```
## WEB_vol1.txt mandil :: elated to or situ- ated between the hyoid bone and the man- dibula. man/dil, n. a turban. man-dil’ion (-yun), n. [OF r. mandillon.] a sol- i dier’s coat; a loose garment worn as an Over- Bi coat by men servants. ; Man-din’ga, n. and a. Mandingo. Man-din’gan, a. of the Mandingos or their language. Man-din’gin, n. Mandingo. Rens Man-din’g6, n.; pl. Man-din’gos, Man-diñ’ À g0es, [from the native name.] ` 1. one of a gro
## RCH.txt Mandil ::  of horse)  overwlielining  (people). p   mandalahy  The  wood  of  aloes.  A   magic  circle  traced on  the  ground.  Mandilahy  A   kind  of  silken  stuff. A   ^X^  mandaCt  (also  ^   al  mandalt)y  Pertaining  to  the H   •• city  of  Mandal,  especially  the  wood  of  aloes. A   ^X^  mandamy  Repentance  (especially  late). A   LeX^  mandamaty  That  which  one  repents  of. A   mundamijy  Round,  smooth.  In
## RCH.txt mashk :: lligent, p   zirakty  Ingenuity,  sagacity,  subtilty,  quickness, p   jij  zlr  gdh^  A   chair,  a   pulpit. p   zlr  mashky  Anything  placed  under  a   sheet  of  paper in  order  that  one  may  write  more  coinmodiously.  (Buriian.) p   jij  zlr^miyunahy  Middling,  ordinary,  below  par. Ztr  wd^  A   kind  of  broth,  or  spoon-meat, p   Zjij  ztrah^  Cumin-seed.  Anise,  the  wild  onion ;   also  another 
## RCH.txt mashk :: sar^mashy  A   kind  of  rough  cider-apple.  Sarmishy Dried  apricots  stuffed  with  almonds.  (Jiurhdn-i  kdit^.) sarmashky  A   copy  (for  writing). A la.^  sormo/,  Long-bodied  (camel). A   sarmaky  Orage,  an  herb.  The  herb  all-heal. V   sarmak  or  saramaky  Orage. A   4^]^  ^   Sarr  man  rdyy  Name  of  a   city  near  Baghdad. y<j^sar^mdy  A   hair’s  point;  a   mere  trifle. 9   i^^3y^^sarmutaky  Co
```


## [2026-09-07T16:01:42.192Z] TOOL CALL #70: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py"
}
```


### [2026-09-07T16:01:42.229Z] TOOL RESULT

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


## [2026-09-07T16:01:50.882Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%85%D8%B4%DA%A9' --note 'page 321, root Masakah: Persian مشک — Wiktionary derives waterskin sense from MP mask < OP maska- < Semitic, NOT Sanskrit' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A4%B6%E0%A4%95' --note 'page 321, root Masakah: Sanskrit मशक = gnat/mosquito only; Hindi मशक borrowed from Classical Persian' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%85%D8%B3%D9%83' --note 'page 321, root Masakah: Arabic مسك skin/hide < Proto-Semitic *mask-' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.wisdomlib.org/definition/mashaka' --note 'page 321, root Masakah: Monier-Williams senses of masaka incl. leather water-bag (lexicographers only)' 2>&1 | tail -3"
}
```


### [2026-09-07T16:01:54.188Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/47386dcf6068f7c8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/663b5ed50e734031.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dbe9aceb0a98fa89.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/052d189616ce306f.txt
```


## [2026-09-07T16:02:03.169Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%85%D9%86%D8%AF%D9%8A%D9%84' --note 'page 321, entry 0 node 1: Arabic مندیل < Byzantine Greek mandilion < Latin mantelium' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/mantele' --note 'page 321, entry 0 root: Latin mantele/mantellum etymology and descendants' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/mantle' --note 'page 321, entry 0: English mantle < Latin mantellum; Celtic vs manus hypotheses' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D9%85%D9%86%D8%AF%DB%8C%D9%84/' --note 'page 321 node 2: Moin مندیل [ع.] دستار و عمامه' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D9%85%D8%A7%D9%86%D8%AA%D9%88/' --note 'page 321 node 5: Moin مانتو [فر.] لباس گشاد' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%BA' --note 'page 321 entry 4: Persian مرغ bird sense; meadow sense in Ottoman Turkish section' 2>&1 | tail -2"
}
```


### [2026-09-07T16:02:08.925Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/951dda6d782d79d0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e3a2bc6dfb13f472.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b5dcd09fcc578938.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5df99a78ed4604b2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8d75b996518b1a50.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ccddebacf6481f1a.txt
```


## [2026-09-07T16:02:16.494Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%80%CE%BC%CE%BF%CF%81%CE%B2%CF%8C%CF%82",
 "prompt": "Give the Ancient Greek entry for ἀμορβός: meaning and etymology verbatim, including any statement that the etymology is unknown/uncertain and any cited authority (Beekes, Chantraine)."
}
```


## [2026-09-07T16:02:18.686Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%8E%B6%F0%8F%81%F0%8E%A3%F0%8E%A0",
 "prompt": "Give the Old Persian entry for 𐎶𐏁𐎣𐎠 (maškā): meaning, attestation, etymology (Semitic?) and descendants. Quote verbatim."
}
```


### [2026-09-07T16:02:20.295Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T16:02:23.298Z] TOOL RESULT

```
# ἀμορβός (amorbós)

## Meanings

**Etymology 1 (Noun):**
- Follower, attendant
- Shepherd

**Etymology 2 (Adjective):**
- Dark

## Etymology

**Etymology 1:** "Unknown." One theory connects it to Sanskrit *mārga* ("path").

**Etymology 2:** Derived from Proto-Indo-European *h₂mergʷ-* ("dark"), with cognates in Proto-Germanic *merkuz*, Lithuanian *márgas* ("colorful"), and Proto-Celtic *mrixtos* ("painted, speckled"). The entry includes a note requesting sources for this etymology.

**Authority cited:** Beekes, Robert S. P. (2010), *Etymological Dictionary of Greek*
```


## [2026-09-07T16:03:05.943Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E1%BC%80%CE%BC%CE%BF%CF%81%CE%B2%CF%8C%CF%82' --note 'page 321 entry 4 note: Greek amorbos \"attendant, shepherd\" — etymology Unknown (Beekes 2010); evaluates Nourai/EAV:866 claim' 2>&1 | tail -2\ncd data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nd=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\nprint('\\n'.join(lines[4468:4482]))\nleaves=d.split('\\f'); acc=0\nfor i,l in enumerate(leaves):\n    n=l.count('\\n')+1\n    if acc<=4474<acc+n:\n        print('POK_03 LEAF',i, re.findall(r'\\b10\\d\\d\\b', l)[:8]); break\n    acc+=n\nEOF"
}
```


### [2026-09-07T16:03:07.962Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d1bac0b624f20a7a.txt
^^ksl.  trovg,  truti,  ablaut.  Kausativ  traviti  ,aufzehren'  (idg.  Hreuöi^tröuew); ^,1  trava  f.  ,Garten^  (ablaut.  tr^va  aus  Hreuä),  russ.  travd  ^Gras'  (dlzu ^^  iihd.  FIN  Trave);  ablaut.  urslav.  Hrüiö  ,reibe*  in  ksl.  tryjg,  tryti  (vgl. ^.r^lJw  ,reibe  auf:  rgvci-ßiog  ,das  Leben  erschöpfend');  hierher  auch  ksl.
'rjia  , Totenfeier'  (aus  *tryzna)-
^s.  drüwigean  {''drötaöjan)  ^leiden,  dulden',  ahd.  dröa  ,onus,  passio', ^oU,  druota  ,pati';  ags.  llcdröivere  ,ein  Aussätziger^  aisl.  likprär  ,aus- iltzig';  aisl.  ^^rä  f.  {''prawö)  ,heftiges,  leidvolles  Verlangen',  prä  und  preyja ^erlangen,  sich  sehnen',  >ä  n.  ,Trotz,  pertinacia',  prär  ,pertinax',  ags.  drea, ^xou  f.  ,Leid,  Drangsal;  Drohung^,  as.  thräwerk  ,Leid^  =  ags.  dreaworc l\Qnd%  ahd.  drawa,  thraiiwa,  dröa  ,Drohung,  Drohen',  ags.  drean  .drohen, ^rängen,  plagen',  ahd.  drawen,  drewen,drauice7i,dröen,  nhd.  drohen,  dräuen-^ lit  der  Bed.-Entwicklung  ,reiben  —  quetschen,  drücken':  ags.  gedrüen ■lasammengepreßt,  verdichtet',  dryn  , drücken';
toch.  A  tsru  , wenig'  (*teruo-).
C.  Als  Erweiterung  der  i-Basis  kann  gelten:  *treid-  in  cymr.  trwyddo Jbohren'.  lit.  triedziu  .habe  starken  Durchfall';  vgl.  unten  S.  1076.
P.  Erweiterungen  von  ter-  und  treu-\ i,  terb-:  s.  S.  1071  unten.
2.  terg-:  lat.  tergö,  -ere,  tergeo,  -ere  , ab  wischen,  reinigen',  mantelum, nantele  , Handtuch'  (*man-terg-sli;  zu  manus  S.  740),  ablautend  umbr.  Akk. jg.  mantrahklu,  mandraclo  ,mantele'  {^-träg-kld)\  got.  pairko  n.  ,Loch^, iefstufig  mnd.  dork  , Kielraum',  ags.  durruc  ,cumba',  ,caupolus';
*trög-y  *trdg-  in  gr.  TQcbya)  , zernage,  knuppere,  fresse  Rohes'  (Aor.  ezga- li),  TQtoydXia  .Näschereien'.  ZQcbyXr]  .Loch,  Höhle',  tqü)^  , Kornwurm',  rgayog Bock';  arm.  t'urc,  Gen.  frcoy  .mala,  maxilla'  (Nom.  statt  *t'ruc  aus  *trög' fcrch  Entgleisung  nach  dem  Gen.  t*rcoy?)  und  aracem  ,weide'  {*tr9g')- iDch.  AB  träsk-  .kauen'.
3.  tergh-:  aksl.  träzati,  tr^zat^  , reißen',   mit  Velar   Hrgati,   trbgngti  ds. f  terp-,  trep-  (nur  bsl.):  lett.   tärps  ,Wurm'  (,der   Zerbohrende'),   lit.
^as  , Zwischenraum,  Lücke,  Kluft',  tarp,  terp  ,zwischen';  lit.  trapüs rode,  leicht  brechend',  lett.  trapj§,  trapans  .mürbe',  trapains  ,morsch. Ichig,  verwitternd',  trapet,  trepet  , verwittern,  faul,  mürbe  werden'; fcklar  aksl.  trap^  , Grube'  (*torp-),  serb.  trap  ,Rübengrube'. 5'  treugh- :  vielleicht  gr.  T^tJ^w  „r^vw",  tQv^og  n.  ,das  Abgerissene, ^Ppen'.  TQvxTjQÖg  .abgerissen,  zerlumpt';  air.  trog,  truag  , elend,  unglück- ^'.  cymr.  mbret.  tru  ,elend',  gall.  PN  Trougülus,  Tragus.
1074
i
6,  treuk-:  cymr.  trwch  ^abgeschnitten',  trychu  ,schneiden*  T* aisl.  ßrö,  PL  pr^r  f.  ,Trog',  ags.  drüh,  Gen.  dryh  t  m.  |n.  ,ds.,  Rinne.- R«^ ahd.  drüh  drück  (eigentlich  ,*Verbrecherblock')  ,Fußfessel,  TierfalU/^^* Brauche  , Falle,  Wolfs-  oder  Fuchseisen',  as.  thrüh  ,Fessel*-  mit  *  *^ Wechsel  isl.  prüga,  norw.  dial.  trüga,  tryge,  trjug  ,Art  SchneeschuV^^S^ ßrüga  , drohen'  (s.  zur  Bed.  oben  mhd.  drohen) ;  Intensiv  aschwed  BrLiS^ ags.  dryccan  ^drücken,  drängen,  einpressen',  ahd.   drucken,  nhd    d^^^
lit.  truk-stu,  -au,  -ti  ,reißen,  brechen,  platzen*,  trukis  ,Riß,  Bruch  fi    u lett.    trük-stu,   -u,   -t  , entzweigehen,    brechen;    mangeln,   fehlen'    Irfil^* >Bruch;   Mangel';   trauks  , Geschirr,   Gefäß*,  lit.    traukai  , Gefäße*  7*^ gebohrtes,  gehöhltes  Stammstück^),  lit.  trdukti  , ziehen',  apr.  p»rtr(xA% schloß'  (eig.  ,umzog'),  lett.  traukt  , schlagen';  lit.  trükti  , dauern   wikL^u trukscioti  ,zucken*.  *
POK_03 LEAF 297 ['1055']
```


## [2026-09-07T16:03:14.111Z] TOOL CALL #76: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-316.json'))\nprint(json.dumps(d['entries'][0], ensure_ascii=False, indent=1)[:3000])\n\""
}
```


### [2026-09-07T16:03:15.672Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Mâ, Mâ-ter",
 "verdict": "plausible",
 "modern_form": "PIE *méh₂tēr 'mother' (Pokorny māter- 700–701; AHD māter-), itself built on the nursery word *mā- / *méh₂- 'mother' (Pokorny mā-3, 694)",
 "note": "Both halves of the root box are real reconstructions and the language label 'Indo-European' is right, but two details of the gloss are Nourai's own. (1) Pokorny's mā-3 (p.694, the page Nourai cites) is glossed 'mother (expr. root)', not 'breast'; the 'breast' sense comes only from the reduplicated derivatives (L. mamma 'mother’s breast, nipple', mamilla), so it is a back-projection. (2) 'Mā-ter: feeder (of the family)' with the cross-reference to Ter 3 analyses -ter- as the agent suffix. Watkins and Walde–Pokorny call it the KINSHIP suffix and offer no such gloss ('Based ultimately on the baby-talk form ma-2, with the kinship term suffix -ter-'); Skeat's older view was '√MĀ to measure', i.e. 'manager of the household'; and Wiktionary reports a minority modern view of a genuine verbal root *méh₂- 'to nurse, to mother' — which is the closest anyone comes to Nourai's 'feeder', but it is not the standard account. Also note the page numbers: 694 is mā-3, while māter- is Pokorny 700–701. Nourai's closing remark about a nursery word becoming the usual term is a paraphrase of Buck 2.36 (SYN:103), which he cites correctly. Everything downstream (Avestan–Pahlavi–Persian; Germanic; Latin; Greek) is sound; the one substantive error on the page is in node #8.",
 "note_fa": "ریشهٔ هندواروپایی آغازین *méh₂tēr «مادر» (پوکورنی ۷۰۰–۷۰۱) و واژهٔ کودکانهٔ *mā- (پوکورنی ۶۹۴) هر دو واقعی اند و برچسب «هندواروپایی» درست است؛ امّا دو نکتهٔ معنایی از خود نورایی است: یکی آنکه پوکورنی در ص ۶۹۴ mā-3 را «مادر» معنی کرده و نه «پستان» — معنای پستان تنها از مشتقّات دوگان‌شده (mamma, mamilla لاتینی) برمی‌آید؛ دوم آنکه تفسیر «mā-ter = خوراک‌دهندهٔ خانواده» پسوند -ter- را پسوند فاعلی گرفته، در حالی که واتکینز و والده‌پوکورنی آن را پسوند واژگان خویشاوندی می‌دانند و چنین معنایی نمی‌دهند (ویکی‌واژه دیدگاهی اقلیتی را گزارش می‌کند که *méh₂- را ریشهٔ فعلی «شیر دادن، مادری کردن» می‌گیرد). در مجموع ریشه با احتیاط پذیرفتنی است و همهٔ شاخه‌های پایین‌دست درست اند؛ تنها خطای جدی این صفحه در گرهٔ ۸ («ممه») است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9h%E2%82%82t%C4%93r",
  "https://www.etymonline.com/word/mother"
 ],
 "ref_check": [
  {
   "ref": "POK:694",
   "status": "partial",
   "note": "Pokorny 694 is 'mā-3, Meaning: mother (expr. root), Note: redupl. māmā, māmmā ... Material: Old Indic mā ‘mother’ ... npers. mām, māmā, māmī ‘mother’ ... Latin mamma ... mamilla ‘nipple’ ... Page(s): 694' (POK_full.txt l.57758ff, grep 'lemma: mah 3'). It therefore supports the Mā- half of the root box, but glosses it ‘mother’, not ‘breast’; Pokorny's separate lemma 'mahter-, Meaning: mother, Note: based on a babble-word mah-, see there ... Page(s): 700-701' is where Mā-ter belongs, i.e. p.700-701 and
```


## [2026-09-07T16:03:22.068Z] TOOL CALL #77: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg321.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/321.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5"
}
```


### [2026-09-07T16:03:22.134Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-07T16:05:30.492Z] AGENT

Now I'll write the verification file.


## [2026-09-07T16:16:18.356Z] TOOL CALL #78: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nREFS = \"/home/sfmqrb/git/rishe/data/verification/sources/refs/\"\n\ndata = {\n \"pdf_page\": 321,\n \"book_page\": 291,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Mantellum, Mantil\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Latin mantēle / mantīle (pl. mantēlia, hence mantēlium) 'cloth for wiping the hands, towel, napkin' beside Late Latin mantellum (with back-formed mantum, mantus) 'cloak'\",\n   \"note\": \"Both Latin words are real and the language label is right, but Nourai's glosses are crossed over: mantēle/mantīle is the 'towel, napkin' word and mantellum the 'cloak' word, whereas the box reads 'Mantellum: cloak, towel' and 'Mantil: cloak' — 'Mantil: cloak' is simply wrong. Whether the two belong together is itself unsettled, and the chart quietly assumes they do. Pokorny p.1073 (root ter-, § 2 terg-) analyses 'lat. mantelum, mantele ‚Handtuch‘ (*man-terg-s-li; zu manus S.740)', with Umbrian mantrahklu, and Ernout–Meillet (s.v. mantele) quote Varro L.L. 6.85 'mantelium ubi manus terguntur' for the same manus + tergēre analysis, treating mantellum 'manteau, couverture' (Plautus, Capt. 530–531) as a separate, popular word. Klein p.935 calls mantellum 'cloak, veil' “prob. of Celtic origin”; Buck (SYN 417) makes Late Latin mantellum a diminutive of a Celto-Iberian mantum; Etymonline reports both hypotheses side by side. So the chart is right that the Arabic 'napkin/turban' word and the French 'cloak' word both come out of this Latin nest, but they may descend from two originally distinct words, and the towel/cloak labels should be swapped.\",\n   \"note_fa\": \"دو واژهٔ لاتینی در جعبهٔ ریشه واقعی اند، امّا معناها جابه‌جا شده است: mantēle / mantīle به معنای «دستمال، حوله» است و mantellum به معنای «ردا، بالاپوش»؛ پس تعریف «Mantil: cloak» نادرست است. پوکورنی (ص ۱۰۷۳) و ارنو‌مییه mantele را از *man-terg-s-li (از manus «دست» + tergēre «پاک کردن»، بر پایهٔ گواهی وارو) می‌گیرند، در حالی که کلاین (ص ۹۳۵) mantellum را احتمالاً وام‌واژه‌ای سلتی و باک (ص ۴۱۷) آن را مصغّر mantum سلتی‌ایبریایی می‌داند. پس ادعای نورایی در کلّیات با احتیاط پذیرفتنی است: هر دو شاخهٔ عربی و فرانسوی از همین خانوادهٔ لاتینی می‌آیند، امّا شاید از دو واژهٔ در اصل جداگانه.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/mantele\",\n    \"https://www.etymonline.com/word/mantle\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"SYN:417\", \"status\": \"supports\",\n     \"note\": \"Buck p.417 (§6.41 CLOAK; leaf 463 of SYN.txt, the page carrying the running head 'PERSONAL ADORNMENT AND CARE 417'): 'Late Lat. mantellum, dim. of a Celto-Iberian mantum, whence Sp. manto. Hence It. mantello, OFr. mantel (> ME mantel, NE mantle), Fr. manteau (> Rum. manta) ... ON mottull, OE mentel, OHG mantal, Du., MHG, NHG mantel'. Buck 6.82 adds 'fr. Lat. mantēle, mantile ‚towel‘'. Exactly the two senses of the root box, though Buck keeps mantellum 'cloak' and mantele 'towel' apart.\"},\n    {\"ref\": \"KLN:932\", \"status\": \"partial\",\n     \"note\": \"Klein's relevant matter is one to three pages off in the 1966 two-volume scan (KLN_1966.txt): the mandil entry sits on leaf 500 = printed pp. 930–931 ('mandil, n., a turban. — Arab. mandīl, fr. MGk. μανδήλιον, fr. L. mantile, which is rel. to mantelum, ‚towel, (table-)napkin‘. See mantle, n.'), while the mantle/manteau entries are on leaf 502 = pp. 935–936 ('mantle, n. ... Both OF. mantel and OE. mentel derive fr. L. mantellum, ‚cloak, veil‘ ... which is prob. of Celtic origin'). So the page supports the content but the citation is a page out.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"p.1073, root ter-, § 2 terg- (POK_03.txt l.4475, leaf 297)\", \"stance\": \"supports\",\n     \"note\": \"'2. terg-: lat. tergö, -ere, tergeo, -ere ‚abwischen, reinigen‘, mantelum, mantele ‚Handtuch‘ (*man-terg-s-li; zu manus S.740), ablautend umbr. Akk. sg. mantrahklu, mandraclo ‚mantele‘'. Pokorny thus has the towel word as an IE compound of manus + terg-, and no entry at all for mantellum 'cloak'.\"},\n    {\"src\": \"LAT\", \"where\": \"s.v. mantele / mantellum (leaf 690, printed p.686)\", \"stance\": \"supports\",\n     \"note\": \"'mantele, -ls n.; mantelium, -i ... essuie-mains; mantelium ubi manus terguntur, Varr. L.L.6,85, qui indique ainsi l'étymologie: *man-terg-s-li'; and separately 'mantellum, -i: manteau, couverture; Pl.Cap.530,531. A basse époque apparaît une forme mantus ... Panroman, sauf roumain'. Ernout–Meillet keep the two words in separate articles — i.e. the root box's fusion of them is the author's.\"},\n    {\"src\": \"SKT\", \"where\": \"s.v. Mantle (SKT.txt l.11061)\", \"stance\": \"supports\",\n     \"note\": \"'Mantle, a cloak, covering. (F. — L.) M.E. mantel. — O.F. mantel, later manteau ... — L. mantellum, a napkin, also a covering; cf. L. mantile, a towel. We also find Low L. mantum, a short cloak, whence Ital. and Span. manto, F. mante, a mantle.' Skeat, like Nourai, blends the two senses into one Latin word.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. merg- 'boundary, border' and the M index\", \"stance\": \"silent\",\n     \"note\": \"grep of AHD_watkins1985.txt for 'mantellum|mantele|mantile' returns nothing; MANTLE is not in Watkins' index of English reflexes, consistent with mantellum being a non-IE (or at least non-reconstructible) word.\"},\n    {\"src\": \"IEC\", \"where\": \"grep 'mantel|mantellum' in IEC.txt\", \"stance\": \"silent\",\n     \"note\": \"Mann's Indo-European Comparative Dictionary has no entry — grep returns nothing.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Arabic\",\n     \"words\": \"mandîl\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Arabic منديل mandīl 'kerchief, napkin, towel; head-cloth' is indeed the Latin word, but it did not come straight from Latin as the arrow shows: the route runs through Byzantine Greek μανδήλιον / μαντίλιον / μανδήλη, itself from Latin mantēlium / mantēle 'hand-towel'. Greek voiced the Latin -t- to -d- (a regular substitution in late/Byzantine borrowings) and its diminutive -ιον gave Arabic the -īl that lets the word sit in the fiʿlīl pattern. The word is current in the eastern Mediterranean by the early Islamic centuries; the Edessa relic known as the Mandylion carries the same Greek word. Klein (p.931/932) gives exactly this chain, and Lokotsch no. 1391 adds the westward continuation (Spanish, Portuguese, Catalan mandil 'apron'). Semantically 'hand-towel' > 'kerchief, napkin' > 'head-cloth, turban', which is why Nourai's gloss carries both 'turban' and 'napkin'. Verdict is 'plausible' only because the Byzantine Greek way-station — present in Nourai's own cited source — is missing from the chart.\",\n     \"derivation_fa\": \"«مندیل» عربی وام‌واژه‌ای لاتینی است، ولی نه مستقیم: مسیر وام‌گیری از لاتینی mantēlium «دستمال» به یونانی بیزانطینی mandēlion / mantilion و از آنجا به عربی است؛ در یونانی t لاتینی به d واک‌دار ابدال شده و پسوند کوچک‌ساز -ion مادّهٔ -īl عربی را داده است. تحول معنایی: «دستمال» ← «محرمه، دستارچه» ← «عمامه، سرپوش». کلاین و لوکوچ همین زنجیره را می‌دهند؛ تنها ایراد آن است که نمودار پلّهٔ یونانی را حذف کرده است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D9%85%D9%86%D8%AF%D9%8A%D9%84\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:932\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 500 (printed pp. 930–931), grep 'mandil,  n.,  a  turban': 'mandil, n., a turban. — Arab. mandīl, fr. MGk. μανδήλιον, fr. L. mantile, which is rel. to mantelum, ‚towel, (table-)napkin‘. See mantle, n.' — the arrow's content, plus the Greek step Nourai leaves out; the following entry 'mandilion ... fr. Arab. mandil' confirms the productivity of the loan.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"no. 1391 (LKT.txt l.3213)\", \"stance\": \"supports\",\n       \"note\": \"'1391. Ar. mandil: ‚Tuch, Hülle‘ [aus gr. μανδήλιον, lat. mantile ZDMG LI, 317; Dozy Vêtem. 414 f.]; hieraus sp. pg. kat. mandil ‚Schürze‘. — [Unmittelbar aus dem lat. mantile kommen mantel ‚Tischtuch‘ und mantilla].' Lokotsch also insists on the Greek intermediary.\"},\n      {\"src\": \"WEB\", \"where\": \"vol. 1 s.v. mandil (WEB_vol1.txt)\", \"stance\": \"supports\",\n       \"note\": \"'man/dil, n. a turban. man-dil'ion (-yun), n. [OFr. mandillon.] a soldier's coat' — the sense 'turban' for the English word, matching node #3.\"},\n      {\"src\": \"AFA\", \"where\": \"grep 'mandil|mandīl' in AFA.txt\", \"stance\": \"silent\",\n       \"note\": \"Fraenkel's Aramäische Fremdwörter im Arabischen has no entry — grep returns nothing, consistent with a Greek (not Aramaic) mediation.\"},\n      {\"src\": \"FVQ\", \"where\": \"grep 'mandil' in FVQ.txt\", \"stance\": \"silent\",\n       \"note\": \"Jeffery's Foreign Vocabulary of the Qur'an has no mandīl — the word is not Qur'anic.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"mandîl «منديل»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian مندیل mandīl is a plain Arabic loan into New Persian (the Arabic yāʾ spelling منديل that the book prints is the usual orthography for such loans), with no phonetic change beyond Persian stress; Mo'in's dictionary tags it '[ع.]' (Arabic) and glosses it دستار و عمامه، ج. منادیل — 'head-cloth and turban, pl. manādīl', with the broken plural showing that Persian took over the word as an Arabic noun. Dehkhoda's first sense, quoting Muntahā al-Arab and Nāzim al-Aṭibbā, is 'پارچه‌ای که دست بدان پاک کنند' (a cloth for wiping the hands) — i.e. both of Nourai's glosses 'napkin, turban' are attested. Since Persian has no inherited claim on the word, the Arabic→Persian arrow is the right direction; and because the Latin ancestor entered Arabic through Greek, this is not one of the Persian→Arabic→Persian round trips.\",\n     \"derivation_fa\": \"«مندیل» در فارسی نو وام‌واژه‌ای عربی است؛ معین آن را با برچسب [ع.] می‌آورد و «دستار و عمامه، ج. منادیل» معنی می‌کند — جمع مکسّر خود گواه عربی‌بودن واژه است. دهخدا نیز معنای نخست را «پارچه‌ای که دست بدان پاک کنند» می‌آورد؛ پس هر دو معنای نورایی (دستمال و عمامه) درست است. این وام‌گیری از نوع معرّب‌های بازگشته نیست، زیرا اصل واژه لاتینی است و از راه یونانی به عربی رفته است. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://abadis.ir/fatofa/%D9%85%D9%86%D8%AF%DB%8C%D9%84/\",\n      \"https://en.wiktionary.org/wiki/%D9%85%D9%86%D8%AF%D9%8A%D9%84\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"MON:4389\", \"status\": \"supports\",\n       \"note\": \"The 6-volume Amir Kabir Mo'in is not online, so the page number itself cannot be checked; the entry text can. abadis.ir/fatofa/مندیل/ , section فرهنگ معین: '(مَ یا مِ) [ع.] (اِ.) دستار و عمامه. ج. منادیل.' — Arabic origin tag and Nourai's 'turban' sense. The alphabetical position also fits: مانتو (MON:3718) precedes مندیل (MON:4389) in Persian order, as the two cited page numbers do.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"فرهنگ معین via abadis.ir s.v. مندیل\", \"stance\": \"supports\",\n       \"note\": \"'[ع.] (اِ.) دستار و عمامه. ج. منادیل.'\"},\n      {\"src\": \"MON\", \"where\": \"2-vol Adena condensation, MON_part1.txt s.v. ازار\", \"stance\": \"supports\",\n       \"note\": \"The abridgement has no مندیل headword but uses the word as a Persian gloss: 'ازار: [ع.] ... دستار؛ مندیل.' — i.e. mandīl is a live Persian word for a head-cloth.\"},\n      {\"src\": \"KLN\", \"where\": \"leaf 500 (pp. 930–931) s.v. mandil\", \"stance\": \"partial\",\n       \"note\": \"Klein gives Arab. mandīl and its Romance/English offspring but says nothing about Persian; it therefore supports the parent, not this arrow.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"English\",\n     \"words\": \"mandil\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English mandil 'a turban, an oriental head-cloth' is a book-word taken from Arabic mandīl through the travel and orientalist literature rather than by contact; Klein p.931/932: 'mandil, n., a turban. — Arab. mandīl, fr. MGk. μανδήλιον, fr. L. mantile', and Webster's New Twentieth Century (2nd ed.) vol. 1 has 'man'dil, n. a turban'. The by-form mandilion 'a loose coat, a soldier's cloak', current in 16th–17th-c. English, reached English by the Romance road instead (French mandillon < Italian mandiglione < Old Pisan mandillo < Arabic mandil), which shows the word entered Europe twice. The Arabic→English arrow is right; note that English thus has the Latin word three times over — as mandil (via Greek and Arabic), as manteau (via French) and as mantle (via Old French mantel).\",\n     \"derivation_fa\": \"واژهٔ انگلیسی mandil به معنای «عمامه» از عربی مندیل گرفته شده است و وام‌واژه‌ای کتابی است که از راه سفرنامه‌ها و متون شرق‌شناسی به انگلیسی راه یافته (کلاین ص ۹۳۱، وبستر ج۱). صورت دیگر آن، mandilion، از راه فرانسه و ایتالیایی آمده است. ادعای نورایی درست است؛ جالب آنکه همین واژهٔ لاتینی سه بار به انگلیسی وارد شده است: mandil، manteau و mantle (دوگانه‌ها).\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D9%85%D9%86%D8%AF%D9%8A%D9%84\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:932\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 500: 'mandil, n., a turban. — Arab. mandīl, fr. MGk. μανδήλιον, fr. L. mantile ...' — Klein's headword IS the English word, so the citation is squarely on target (printed pp. 930–931 in this scan).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WEB\", \"where\": \"vol. 1 (WEB_vol1.txt), s.v. mandil\", \"stance\": \"supports\",\n       \"note\": \"'man/dil, n. a turban.' followed by 'man-dil'ion (-yun), n. [OFr. mandillon.] a soldier's coat; a loose garment worn as an overcoat by men servants.'\"},\n      {\"src\": \"FSD\", \"where\": \"grep 'mandil' in FSD_vol2.txt / FSD_vol3.txt\", \"stance\": \"silent\",\n       \"note\": \"Funk & Wagnalls has no mandil entry in the volumes on disk — grep returns nothing; the word is rare enough to be omitted from general dictionaries.\"},\n      {\"src\": \"LKT\", \"where\": \"no. 1391\", \"stance\": \"partial\",\n       \"note\": \"Lokotsch traces the Arabic word into Spanish/Portuguese/Catalan mandil but not into English.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"French\",\n     \"words\": \"manteau\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"French manteau 'cloak, coat' descends from Latin mantellum through Old French mantel (11th c.): Latin -ellum > OF -el, and the OF -el then underwent the regular vocalisation of syllable-final /l/ to /u/ with monophthongisation, giving Middle French mantiau > manteau (the same change as OF chastel > château, bel > beau). Klein p.935 'manteau, n., cloak, mantle. — F., fr. OF. mantel, fr. L. mantelium'; Buck p.417 lays out the whole Romance and Germanic spread from 'Late Lat. mantellum ... Hence It. mantello, OFr. mantel (> ME mantel, NE mantle), Fr. manteau (> Rum. manta)'; Ernout–Meillet call mantellum 'Panroman, sauf roumain'. The root→French arrow is uncontroversial; the only quibble is the page: in the 1966 Klein scan manteau stands on p.935, not the cited 934.\",\n     \"derivation_fa\": \"manteau فرانسوی از لاتینی mantellum می‌آید، از راه فرانسه‌ی باستان mantel؛ در گذر از فرانسه‌ی باستان به میانه، l پایانِ هجا به u بدل شده و دوواکهٔ -eau را ساخته است (مانند chastel > château). کلاین (ص ۹۳۵) و باک (ص ۴۱۷) همین زنجیره را می‌دهند. ادعای نورایی درست است؛ تنها شمارهٔ صفحهٔ کلاین یک صفحه جابه‌جا است.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/mantle\",\n      \"https://en.wiktionary.org/wiki/mantele\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:934\", \"status\": \"partial\",\n       \"note\": \"The entry exists but one page later in the 1966 two-volume scan: KLN_1966.txt leaf 502 (printed pp. 935–936) 'manteau, n., cloak, mantle. — F., fr. OF. mantel, fr. L. mantelium. See mantle and cp. prec. word.' Content fully supports the arrow.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SYN\", \"where\": \"p.417, §6.41 CLOAK (SYN.txt leaf 463)\", \"stance\": \"supports\",\n       \"note\": \"'Late Lat. mantellum, dim. of a Celto-Iberian mantum ... Hence It. mantello, OFr. mantel (> ME mantel, NE mantle), Fr. manteau (> Rum. manta)'.\"},\n      {\"src\": \"SKT\", \"where\": \"s.v. Mantle\", \"stance\": \"supports\",\n       \"note\": \"'M.E. mantel. — O.F. mantel, later manteau ... — L. mantellum'.\"},\n      {\"src\": \"LAT\", \"where\": \"s.v. mantellum (leaf 690, printed p.686)\", \"stance\": \"supports\",\n       \"note\": \"'mantellum, -i: manteau, couverture; Pl.Cap.530,531 ... Panroman, sauf roumain; M.L.5336'.\"},\n      {\"src\": \"PHN\", \"where\": \"grep 'manteau' in PHN.txt\", \"stance\": \"silent\",\n       \"note\": \"Pihan uses 'manteau' only as a French gloss for Arabic garments ('aba, etc.); he has no entry making manteau itself an orientalism — correctly, since it is Latin.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Persian\",\n     \"words\": \"mânto «مانتو»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian مانتو mānto is a 20th-century French loan, one of the large set of European clothing words that entered Persian through Qajar and early Pahlavi contact with France; French manteau /mɑ͂to/ is rendered with مان- for the nasal vowel (Persian having no nasal vowels, the nasality is resolved into ā + n) and -تو for -teau. Mo'in tags the entry '[فر.]' (French) and glosses 'لباس گشادی که روی لباس‌های دیگر پوشیده می‌شود، روپوش'; the two-volume condensation adds '(زن و مرد)', i.e. the word was originally unisex — the modern restriction to the women's overcoat is post-1979. Nourai's gloss for the node is simply 'manteau', which is right. The French→Persian arrow is correct and the loan is recent enough that none of the 19th-century Iranian-etymology handbooks can register it.\",\n     \"derivation_fa\": \"«مانتو» وام‌واژه‌ای فرانسوی است که در سدهٔ چهاردهم قمری/بیستم میلادی از راه پوشاک فرنگی به فارسی راه یافته است؛ واکهٔ خیشومی فرانسوی در فارسی به «آ + ن» تحلیل شده و -eau به «و» بدل گشته است. معین آن را با برچسب [فر.] و معنای «لباس گشادی که روی لباس‌های دیگر پوشند (زن و مرد)» می‌آورد. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://abadis.ir/fatofa/%D9%85%D8%A7%D9%86%D8%AA%D9%88/\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"MON:3718\", \"status\": \"supports\",\n       \"note\": \"Page number not verifiable (6-vol Mo'in not online), content is: abadis.ir/fatofa/مانتو/ , فرهنگ معین '(تُ) [فر.] (اِ.) لباس گشادی که روی لباس های دیگر پوشیده می شود، روپوش.' — the [فر.] tag is exactly Nourai's French parent.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"2-vol Adena condensation, MON_part2.txt s.v. مانتو\", \"stance\": \"supports\",\n       \"note\": \"'مانتو: (ا.) جامهٔ گشادی که روی لباس‌های دیگر پوشند (زن و مرد).' (the Latin-script etymon of the print edition is lost in this OCR). The same file also has گاباردین defined as 'مانتو غیر قابل نفوذ (امپرمابل)', i.e. the word is fully naturalised.\"},\n      {\"src\": \"MON\", \"where\": \"فرهنگ معین via abadis.ir s.v. مانتو\", \"stance\": \"supports\",\n       \"note\": \"'[فر.] (اِ.) لباس گشادی ... روپوش.'\"},\n      {\"src\": \"HRN\", \"where\": \"grep 'manteau|manto' in HRN.txt\", \"stance\": \"silent\",\n       \"note\": \"Horn (1893) has no such entry — as expected, the loan is later than his Grundriss; the same holds for Hübschmann (1895) and Borhan-e Qate' (1652).\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"manteau\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English manteau, taken from French manteau in the 17th century, first as 'a cloak' and then specifically as the loose gown worn by women in the late 17th and 18th centuries. Klein p.935: 'manteau, n., cloak, mantle. — F., fr. OF. mantel, fr. L. mantelium. See mantle and cp. prec. word.' Its variant mantua 'a woman's mantle' is the same French manteau reshaped by folk etymology after Mantua in Italy, 'as if the word meant ‚a mantle manufactured in Mantua‘' (Klein, same page). manteau is thus a later doublet of mantle, which came in through Old French mantel in the 12th–13th centuries. The node carries no reference in the book, but the French→English arrow is standard and uncontested.\",\n     \"derivation_fa\": \"manteau انگلیسی در سدهٔ هفدهم میلادی از فرانسه وام گرفته شده است و دوگانهٔ (doublet) متأخرِ mantle است که پیش‌تر از فرانسه‌ی باستان mantel آمده بود. کلاین (ص ۹۳۵) می‌نویسد: 'manteau ... — F., fr. OF. mantel, fr. L. mantelium'؛ صورت mantua هم همین واژه است که بر اثر ریشه‌شناسی عامیانه به نام شهر «مانتوا» در ایتالیا بازسازی شده است. ادعای نورایی درست است، هرچند گره در کتاب بی‌ارجاع است.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/mantle\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"The node carries no reference in the book (refs=None); Klein p.935, cited for the parent node, covers this arrow too.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"leaf 502 (printed pp. 935–936) s.v. manteau, mantua\", \"stance\": \"supports\",\n       \"note\": \"'manteau, n., cloak, mantle. — F., fr. OF. mantel, fr. L. mantelium'; 'mantua, n., a mantle formerly worn by women. — F. manteau, ‚cloak, mantle‘ (see mantle); influenced in form by Mantua, town in Italy'.\"},\n      {\"src\": \"SKT\", \"where\": \"s.v. Mantle\", \"stance\": \"partial\",\n       \"note\": \"Skeat records 'O.F. mantel, later manteau' as the source of English mantle but has no separate manteau headword.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 4,\n   \"root\": \"Mareğâ\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Young Avestan marəγā- f. 'meadow' (Bartholomae, Altiranisches Wörterbuch col. 1147; Vd. 2.26), from Proto-Iranian *marga- 'meadow' — the same base as OP margav- / Av. mouru- 'Margiana, Marv'\",\n   \"note\": \"The root box is right in substance. Bartholomae col. 1147 has 'j. marəγā- f. ‚Wiese‘: ārā marəγā avastaya ‚.. leg Wiesen an‘ V. 2.26', and himself adds 'np. marγ ‚Wiese‘'; immediately above he derives OP margav-, Av. mouru- (Margiana, mod. Marv) 'Ableit. (s. marγ-)' from ir. *marγuš, so the base is well anchored in Old Iranian. Nourai's gloss 'grass' is the New Persian sense; the Avestan word means 'meadow, pasture'. The transliteration 'Mareğâ' is Nourai's usual system (ğ = γ, â = ā, e = ə) and is faithful; it must not be confused with Av. mərəγa- 'bird' (> NP murγ), a separate word that his notation would spell almost identically. The PIE background is not in Pokorny or Watkins (their merg- is 'boundary, border' > Lat. margo), so *marga- 'meadow' is at present an Indo-Iranian/Iranian item without a secure IE root. The chart's own NOTE — 'EAV:866 indicates that this word is related to the Greek word \\\"amorphous: shepherd\\\"' — is a misprint in the printed book (p.291; verified on the page image, copied to data/verification/sources/refs/ocr/BOOK/321.png): Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939), p.866 §12 writes 'Av. maraγa-, persan mūrγ ‚prairie, pâture‘ est le nom d'action ou d'objet correspondant aux noms d'agent gr. ἀμορβός ‚compagnon, berger‘, ἀμορβεύς ‚berger‘'. The Greek word is ἀμορβός amorbós, not 'amorphous', and the comparison is not accepted today: Wiktionary, following Beekes (EDG 2010), gives the etymology of ἀμορβός as 'Unknown' (with an unrelated guess linking it to Skt. mārga 'path'). So the note should be read as reporting a 1939 conjecture that modern scholarship has dropped.\",\n   \"note_fa\": \"جعبهٔ ریشه درست است: بارتولومه در ستون ۱۱۴۷ فرهنگ ایرانی باستان، اوستایی متأخر marəγā- مؤنّث را «مرغ، چمن، Wiese» معنی کرده و شاهد آن را از وندیداد ۲؛۲۶ می‌آورد و خود می‌نویسد «np. marγ ‚Wiese‘»؛ همو نام مرو (پارسی باستان margav-، اوستایی mouru-) را از همین ستاک می‌گیرد. معنای «grass» در کتاب معنای فارسی نو است، نه اوستایی («چمن، مرتع»). این واژه را نباید با mərəγa- «پرنده» (> مُرغ) اشتباه گرفت. دربارهٔ یادداشت کتاب: عبارت «amorphous: shepherd» خطای چاپی خود کتاب است (در تصویر صفحهٔ ۲۹۱ دیده می‌شود، نه خطای خوانش اسکن)؛ دوشن‌گیلمن در ص ۸۶۶ از یونانی ἀμορβός (amorbós) «همراه، شبان» سخن گفته و نه از amorphous؛ و این مقایسه امروز پذیرفته نیست (بیکس، فرهنگ ریشه‌شناسی یونانی ۲۰۱۰، ریشهٔ آن را ناشناخته می‌داند).\",\n   \"error_in\": \"book\",\n   \"book_prints\": \"EAV:866 indicates that this word is related to the Greek word \\\"amorphous: shepherd\\\".\",\n   \"correct_form\": \"ἀμορβός (amorbós) 'companion, attendant, shepherd'\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%E1%BC%80%CE%BC%CE%BF%CF%81%CE%B2%CF%8C%CF%82\",\n    \"https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%BA\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"BQT:1990\", \"status\": \"supports\",\n     \"note\": \"Borhan-e Qate' ed. Mo'in, printed p.1990 = pdf p.73 of BQT_v4_picofile.pdf (BQT_v4_pages.txt, printed = pdf+1917). The page carries the مرغ entries, and Mo'in's footnote 1 reads (OCR): '۱ - رک: مرغزار » معرب مرغ « مرج » » اوستا- [marəγā] ( چمن ) » آرمنی ... سریانی ... (چمن) » کردی ... ( چمن ) ... ورك : هوبشمان ایضاً . درعربی نیز « مرج » ...' — i.e. Mo'in gives exactly Nourai's Avestan 'meadow' word as the source of Persian marγ, with Armenian, Syriac and Kurdish parallels and the Arabic loan marj. (The Latin-script Avestan form is garbled by the Persian OCR but its position and the چمن gloss are unambiguous; Bartholomae col. 1147 supplies the reading.)\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"col. 1147 (BRT.txt l.20015–20016, leaf 613; the col. numbers '47' [=1147] and 'martiya- 1148' are on the same leaf)\", \"stance\": \"supports\",\n     \"note\": \"'• j. marəγā- f, ‚Wiese‘: ārā marəγā avastaya ‚.. leg Wiesen an‘ V. 2.26. — np. marγ ‚Wiese‘; s. dazu Hbm. ZDMG. 46.244, Justi ZDMG. 37.245, NB. 14b.' Also, just above: 'p. margav-, j. marəav-: mōuru- m. Name eines Landes, Marǵiane ... Ableit. (s. marγ-) ... Aus ir. *marγuš'.\"},\n    {\"src\": \"HRN\", \"where\": \"no. 975, printed p.219 (HRN.txt l.8487–8491, leaf 233)\", \"stance\": \"supports\",\n     \"note\": \"'975. merγ ‚zum Viehfutter dienendes Gras‘, merγzar ‚Ort, wo merγ wächst‘, arab. LW. marj ‚Wiese‘. aw. marəγā- ‚Wiese‘ (Hübschmann, ZDMG. 46, 244 No. 75); arm. LW. marg ‚Wiese‘, syr. LW. מרגא ‚Wiese‘. kurd. mirk, merγa ‚Prairie‘.'\"},\n    {\"src\": \"HUB\", \"where\": \"§139, printed p.247 (HUB.txt l.8826)\", \"stance\": \"supports\",\n     \"note\": \"'§ 139. Ap. g nach Vokalen und r = γ bleibt im Np. als γ: murγ ‚Vogel‘ = zd. mərəγa-; marγ ‚Wiese‘ (oben p. 98) = zd. marəγa-' — both the sound law and the Avestan source, and the explicit separation of the 'bird' and 'meadow' words.\"},\n    {\"src\": \"EAV\", \"where\": \"BSOAS 9.4 (1939) p.866 §12 (EAV_studies.txt l.162–175)\", \"stance\": \"partial\",\n     \"note\": \"'12. av. maraγa-. Av. maraγa-, persan mūrγ ‚prairie, pâture‘ est le nom d'action ou d'objet correspondant aux noms d'agent gr. ἀμορβός ‚compagnon, berger‘, ἀμορβεύς ‚berger‘, etc.' — confirms that Nourai's note reports Duchesne-Guillemin correctly in substance (the Greek word is amorbós, misprinted 'amorphous' in the book) but the Greek comparison itself is now abandoned. Note that EAV's own 'persan mūrγ' is a slip for marγ.\"},\n    {\"src\": \"POK\", \"where\": \"grep 'marəγ|Wiese' in POK_01/02/03.txt\", \"stance\": \"silent\",\n     \"note\": \"Pokorny has no lemma for a *marga- 'meadow'; his merg- (p.738) is 'Grenze, Rand' (Lat. margo, Goth. marka), which Watkins/AHD likewise gloss 'boundary, border' — no Iranian meadow word is attached to it.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. merg-\", \"stance\": \"silent\",\n     \"note\": \"'merg-. Boundary, border ... 4. Latin margo, border, edge: MARGIN. [Pok. mereg- 738.]' — nothing about a meadow word, so the root box's Avestan starting point is as far back as one can safely go.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Persian\",\n     \"words\": \"marğ «مَرغ ۲»; marğzâr «مرغزار»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP مرغ marγ 'a fast-growing meadow grass; grassland' continues Old Iranian *marga- (Av. marəγā- 'meadow') through an unattested Middle Persian *marγ: the Old Iranian velar stop after r became the voiced fricative γ in Middle Persian and is retained in New Persian, written غ — Hübschmann's rule (Persische Studien §139, p.247): 'Ap. g nach Vokalen und r = γ bleibt im Np. als γ: ... marγ ‚Wiese‘ = zd. marəγa-'; the Avestan feminine ending -ā was lost with all final vowels in Middle Persian. مرغزار marγzār is marγ + the productive Persian place-suffix -zār 'tract, field of' (as in گلزار، لاله‌زار، شوره‌زار), hence 'meadowland' — Horn no. 975 (p.219) gives exactly this pair, 'merγ ‚zum Viehfutter dienendes Gras‘, merγzar ‚Ort, wo merγ wächst‘', and lists the outward loans: Arabic مرج marj 'meadow', Armenian marg, Syriac margā, Kurdish mirk/merγa. Mo'in's footnote on Borhan p.1990 says the same and adds 'معرب مرغ «مرج»', i.e. Arabic marj is the arabicised form of Persian marγ, not the reverse. The chart's cross-reference '☞ Kwel' on marγzār concerns the -zār suffix, not marγ. One reservation: MacKenzie's Pahlavi dictionary has no marγ 'meadow' headword (his 'meadow, plain' is rāγ, and marw is 'herb' with an NP variant marγ), so the Middle Persian link is reconstructed rather than attested.\",\n     \"derivation_fa\": \"«مرغ» در معنای گیاه و چمن، ادامهٔ ایرانی باستان *marga- (اوستایی marəγā-) است؛ g ایرانی باستان پس از r در فارسی میانه به سایشی واک‌دار γ نرم شده و در فارسی نو به صورت «غ» مانده است (قاعدهٔ هوبشمان، مطالعات فارسی §۱۳۹، ص ۲۴۷)؛ پایانهٔ مؤنّث -ā اوستایی مانند همهٔ واکه‌های پایانی افتاده است. «مرغزار» از مرغ + پسوند مکانی پرکاربرد «-زار» است (مانند گلزار و لاله‌زار). هرن (شمارهٔ ۹۷۵، ص ۲۱۹) و معین (حاشیهٔ برهان قاطع، ص ۱۹۹۰) همین را می‌گویند و می‌افزایند که «مرج» عربی معرّبِ همین «مرغ» است (و نیز وام‌واژه‌های ارمنی marg و سریانی margā). ادعای نورایی درست است؛ تنها باید دانست که صورت فارسی میانه گواهی مستقیم ندارد و بازسازی شده است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%BA\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1990\", \"status\": \"supports\",\n       \"note\": \"BQT_v4_pages.txt pdf p.73 (= printed 1990), footnote 1 to the مرغ entry: '۱ - رک: مرغزار » معرب مرغ « مرج » » اوستا- ... ( چمن ) » آرمنی ... سریانی ... کردی ... ورك : هوبشمان ایضاً'; the body of the entry glosses مرغ (بفتح اول) as the grass 'that grows luxuriantly and green', and footnote 3 separately handles مرغ 'bird' (پهلوی murw, اوستا mərəγa-, بارتولمه ۱۱۷۲، نیبرگ ص۱۵۳) — so Nourai's page is right and the two homographs are kept apart there too.\"},\n      {\"ref\": \"MON:4019\", \"status\": \"not_checked\",\n       \"note\": \"The 6-volume Mo'in is not online and its pagination cannot be mapped; the 2-volume Adena condensation (MON_part1/2.txt) has مرغزار only as a gloss ('چمن: (ا.) زمین سبز و خرم؛ مرغزار'; 'راغ: (ا.) مرغزار. دامن کوه'), which shows the word and sense but not the cited page.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"no. 975, printed p.219\", \"stance\": \"supports\",\n       \"note\": \"'975. merγ ‚zum Viehfutter dienendes Gras‘, merγzar ‚Ort, wo merγ wächst‘, arab. LW. marj ‚Wiese‘. aw. marəγā- ‚Wiese‘ ... arm. LW. marg, syr. LW. מרגא, kurd. mirk, merγa.' Both of Nourai's words, from his Avestan parent.\"},\n      {\"src\": \"HUB\", \"where\": \"§139, p.247\", \"stance\": \"supports\",\n       \"note\": \"'marγ ‚Wiese‘ (oben p. 98) = zd. marəγa-' — the sound-law statement for the γ.\"},\n      {\"src\": \"BRT\", \"where\": \"col. 1147\", \"stance\": \"supports\",\n       \"note\": \"'np. marγ ‚Wiese‘' appended to the Avestan lemma marəγā-.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p.55 s.v. marw; p.71 s.v. rāγ (PHD.txt l.455, 555)\", \"stance\": \"partial\",\n       \"note\": \"'marw [mlw' | M mrw, N ~, (marγ)] herb' and 'rāγ [Pg | N ~] meadow, plain'; MacKenzie's English index has 'meadow rāγ; v. pasture'. So Pahlavi marγ 'meadow' is not attested in his corpus — the NP marγ he records is the variant of marw 'herb', a different word. The Old Iranian→NP line is secure, the MP stage is not attested.\"},\n      {\"src\": \"ARY\", \"where\": \"grep 'مرغزار|MARGH' in ARY_pages.txt / ARY_latin_index_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"Aryanpur has no entry for مرغ 'meadow' (his M-section entries near it are مغز/mazgā 'marrow' and مگس/maγšī 'fly'), consistent with the word having no established PIE root.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Sogdian\",\n     \"words\": \"mrğ\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Sogdian mrγ /marγ/ 'wood, meadow' is the regular Sogdian outcome of the same Old Iranian *marga-: Sogdian keeps the -rγ- cluster unchanged and, having lost final short vowels, writes the bare consonant skeleton mrγ in all three scripts. Gharib's Sogdian–Persian–English Dictionary gives it twice, entry 5431 'mrγ² M, C, S — marγ (mrγyh) ©Av. marəγa ©pl. -t(t) ... wood, meadow' and entry 5434 'mrγ⁴ B — marγ (mrγyh) ... wood, meadow', i.e. Gharib herself derives the Sogdian word from precisely the Avestan word Nourai puts in the root box. It is a sister form, not a loan from Persian, and the shift 'meadow' ~ 'wood, thicket' is the ordinary widening of an uncultivated-land term. (Do not confuse it with Gharib's 5430 mrγʾ 'Marv' and 5429 marc 'death' ©Av. mahrka.)\",\n     \"derivation_fa\": \"سغدی mrγ (خوانش marγ) «چمن، بیشه» بازماندهٔ منظم همان *marga- ایرانی باستان است؛ در سغدی خوشهٔ -rγ- دست‌نخورده مانده و واکهٔ پایانی افتاده است. قریب در فرهنگ سغدی، مدخل‌های ۵۴۳۱ و ۵۴۳۴، آن را صریحاً از اوستایی marəγa می‌گیرد؛ پس هم‌ریشهٔ «مرغ» فارسی است و وام‌واژه نیست. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"SOD:216\", \"status\": \"supports\",\n       \"note\": \"SOD_pages.txt leaf 279 (printed ≈ 213 by the +66 leaf offset, i.e. within a page or three of Nourai's 216) carries entries 5416–5449; the English gloss index of the same book lists 'meadow 5431, 5434'. Entry text: '5431 mrγ² M, C, S ... marγ (mrγyh) ©Av. marəγa ©pl. -t(t) ... wood, meadow' and '5434 mrγ⁴ B ... marγ (mrγyh) ©ob. -yh ... wood, meadow'.\"}\n      ],\n     \"consulted\": [\n      {\"src\": \"SOD\", \"where\": \"Gharib entries 5431 and 5434 (SOD_pages.txt l.19243, 19271ff)\", \"stance\": \"supports\",\n       \"note\": \"Both entries gloss 'wood, meadow' and cite '©Av. marəγa' as the source — the same Avestan word as the root box.\"},\n      {\"src\": \"BRT\", \"where\": \"col. 1147\", \"stance\": \"supports\",\n       \"note\": \"Bartholomae's Avestan marəγā- 'Wiese' is the common ancestor Gharib points to; Bartholomae lists no Sogdian, but the Avestan lemma is what the Sogdian entry rests on.\"},\n      {\"src\": \"PHD\", \"where\": \"grep 'marγ|meadow' in PHD.txt\", \"stance\": \"silent\",\n       \"note\": \"MacKenzie covers Middle Persian only; his 'meadow' is rāγ, so he neither supports nor contradicts the Sogdian form.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 5,\n   \"root\": \"Mašakah\",\n   \"verdict\": \"disputed\",\n   \"modern_form\": \"not Sanskrit: Old Persian maškā- '(inflated) skin' (Behistun DB 1.86), a loan from Semitic (Aramaic maškā, Akkadian mašku 'skin'; Proto-Semitic *mašk-, cf. Arabic مسك mask 'hide') > MP mašk > NP مشک mašk; Sanskrit maśaka- is 'gnat, mosquito' (< Proto-Indo-Aryan *makaśas)\",\n   \"note\": \"Nourai's cited source really does say what the root box says: Klein p.1018, 'mussuck, mussuk, n., a leathern skin for water (India) — Hind. masak, fr. OI. masakah', and Hobson-Jobson p.603b agrees ('Hind. mashak, Skt. maśaka'). But this is the older Indological account and modern scholarship reverses the direction. (1) The word is attested in Old Persian: maškā- '(inflated) skin', used at Behistun DB 1.86 of the skins on which Darius' troops crossed the Tigris. Kent's lexicon reads 'maškā- sb. ‚(inflated) skin‘; NPers. mašk, Akk. maš-ku-u ‚skin‘, Aram. maškā: borrowed from Semitic', and Kent's grammar lists it among the certain Semitic loanwords in OP (§86, §148.IV). (2) Sanskrit maśaka- means 'mosquito, gnat' (Atharvaveda) and, secondarily, a bean-like skin eruption; the 'leather water-bag' sense in Monier-Williams stands without a text citation, i.e. rests on the Sanskrit lexicographers alone — most probably a Sanskritisation of the vernacular Persian loan. Wiktionary derives the Sanskrit word from Proto-Indo-Aryan *makaśas (metathesis) and Hindi मशक 'waterskin' from Classical Persian مشک. (3) Whitworth's Anglo-Indian Dictionary (1885) already had 'Mashak. [Persian mashk.] A leather bag for carrying water'. So the actual chain is Semitic → Old Persian → Middle/New Persian → Indic → Anglo-Indian, and the Sanskrit root box inverts it. A minority third option exists: Aryanpur (printed p.473, pdf p.472) groups Pahlavi mašk / maškīzag and Sogdian mšk with Skt. meṣa-, Av. maēša-, Lith. maišas 'sack', OPruss. moasis 'bellows', OCS měxъ, i.e. with PIE *moiso- 'ram, sheepskin, bag' (citing Pokorny and Delamarre 'sac en peau' 148) — also not a borrowing from Sanskrit. Either way the root box's language label is wrong.\",\n   \"note_fa\": \"ریشهٔ این مدخل را پژوهش امروزی رد می‌کند. نورایی به کلاین (ص ۱۰۱۸) تکیه کرده که «Hind. masak, fr. OI. masakah» می‌نویسد و هابسن‌جابسن نیز همین را می‌گوید؛ امّا این دیدگاه قدیمی است. نخست آنکه واژه در پارسی باستان گواهی دارد: maškā- «پوست بادکرده» در سنگ‌نوشتهٔ بیستون (DB ۱؛۸۶)، و کنت آن را وام‌واژه‌ای سامی (آرامی maškā، اکدی mašku، سامی آغازین *mašk-، قس: عربی مسک) می‌داند و می‌نویسد که «مشک» فارسی نو از همان است. دوم آنکه maśaka- سنسکریت در اصل «پشه، مگس» است (از *makaśas با قلب) و معنای «مشک آب» در مونیر‌ویلیامز تنها به فرهنگ‌نویسان متأخر متکی است — بسیار محتمل سنسکریتی‌شدنِ وام‌واژهٔ فارسی. سوم آنکه ویت‌وورت (۱۸۸۵) هم نوشته «Mashak. [Persian mashk]». پس زنجیرهٔ درست چنین است: سامی ← پارسی باستان ← فارسی میانه/نو ← هندی ← انگلیسیٔ هند. (رای سومی نیز هست: آریان‌پور مشک را هم‌ریشهٔ *moiso- «پوست گوسفند، مشک» می‌داند، که آن نیز وام‌گیری از سنسکریت نیست.)\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%D9%85%D8%B4%DA%A9\",\n    \"https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A4%B6%E0%A4%95\",\n    \"https://en.wiktionary.org/wiki/%D9%85%D8%B3%D9%83\",\n    \"https://www.wisdomlib.org/definition/mashaka\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"KLN:1018\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 545 (the next leaf carries the running number 1021, so this is pp. 1018–1019 — Nourai's page): 'mussuck, mussuk, n., a leathern skin for water (India) — Hind. masak, fr. OI. masakah.' Klein does assert the Sanskrit ('Old Indian') origin, so the citation is accurate; it is Klein's claim, not Nourai's transcription, that modern work rejects.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. maškā- (KNT.txt l.5795, leaf 215) and §86 / §148.IV (l.357, 1373, 1444)\", \"stance\": \"contradicts\",\n     \"note\": \"'maškā- sb. ‚(inflated) skin‘; NPers. mašk, Akk. maš-ku-u ‚skin‘, Aram. maškā: borrowed from Semitic (§99, §109, §117, §148.IV) ... DB 1.86'; and in §86: 'are obvious borrowings, such as maškā- ‚inflated skin‘ from Aramaic'. Kent derives NP mašk straight from Old Persian and calls the word Semitic — no Sanskrit anywhere.\"},\n    {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.603b s.v. MUSSUCK (HJB.txt l.15145, leaf 624; index 'Mussuck, 603b')\", \"stance\": \"supports\",\n     \"note\": \"'MUSSUCK, s. The leathern water-bag, consisting of the entire skin of a large goat, stript of the hair and dressed, which is carried by a bhīshtī (see BHEESTY). Hind. mashak, Skt. maśaka.' Yule & Burnell take Nourai's line.\"},\n    {\"src\": \"AID\", \"where\": \"Whitworth, An Anglo-Indian Dictionary p.189 s.v. Mashak / Masak / Mussuk (AID.txt l.4422–4427, leaf 207)\", \"stance\": \"contradicts\",\n     \"note\": \"'Mashak. [Persian mashk.] A leather bag for carrying water. The bhisti carries it on his back.'; 'Masak. The Marāthī form of Mashak.'; 'Mussuk. See Masak.' Whitworth (1885) already made the Indian word a Persian loan.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, printed p.473 (pdf p.472 of ARY_latin_index_pages.txt)\", \"stance\": \"contradicts\",\n     \"note\": \"The cognate set groups '(PAHLAVI) MASHK, MASHKIZAG / MSHK (SOGDIAN) / (SANSKRIT) MESHAS, MASHAKA / MEISS (OLD SCANDINAVIAN) / MEISA (OHG) / MECHU (OCS) / MIECH (POLISH) / MECH (RUSSIAN) / MAISHAS (LITHUANIAN) / MAISS (LATVIAN) / MOASIS (OLD PRUSSIAN)' with 'REFERENCES: POKORNY ...; DELAMARRE (SAC EN PEAU) 148; MACKENZIE (MUSSUCK) 124'. Aryanpur therefore makes mašk an inherited IE word of the *moiso- 'sheepskin, bag' family, with Skt. maśaka a cognate rather than the source.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p.55 (PHD.txt l.461–463)\", \"stance\": \"partial\",\n     \"note\": \"'¹mašk [mšk' | N ~] mussuck, skin bag (for liquids)'; '²mašk [mšk' | N maškē] tent, pavilion. ~abarzēn [-'plzȳn' | M mškbrzyn] royal pavilion'; 'maškīzag [mškyck'] small mussuck, skin ‚table-cloth‘'. MacKenzie confirms the Pahlavi forms and glosses but offers no etymology, so he supports the nodes and is silent on the Sanskrit parent.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"mašk\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The Pahlavi form and gloss are impeccable — MacKenzie p.55 '¹mašk [mšk'] mussuck, skin bag (for liquids)' with the derivative maškīzag 'small mussuck', and Mo'in's footnote on Borhan p.2014 says 'در پهلوی mašk، وآن اصلاً بمعنی چرم (مخصوصاً چرمی که در آن آب ریزند)', i.e. 'in Pahlavi mašk, originally meaning leather (especially the leather into which water is poured)' — which is Nourai's gloss word for word. What is wrong is the PARENT. MP mašk continues Old Persian maškā- '(inflated) skin' (Behistun DB 1.86, of the skins used to cross the Tigris), and that Old Persian word is itself a Semitic loan — Aramaic maškā, Akkadian mašku 'skin' (Proto-Semitic *mašk-, cf. Arabic مسك mask 'freshly flayed hide') — as Kent states in so many words and Wiktionary repeats. Phonetically OP maškā- gives MP mašk by the ordinary Middle Persian loss of final vowels; a Sanskrit maśaka- would instead have had to lose its medial -a- and turn ś into š, which is not how Indic loans behave in Middle Persian, and Sanskrit maśaka- in any case means 'gnat'. So the arrow Sanskrit → Pahlavi is rejected: the direction runs Semitic → Old Persian → Pahlavi.\",\n     \"derivation_fa\": \"صورت و معنای پهلوی درست است: مکنزی (ص ۵۵) «mašk — mussuck, skin bag (for liquids)» می‌آورد و معین در حاشیهٔ برهان قاطع (ص ۲۰۱۴) «در پهلوی mašk و آن اصلاً بمعنی چرم (مخصوصاً چرمی که در آن آب ریزند)». امّا پدرِ نمودار نادرست است: mašk فارسی میانه ادامهٔ maškā- پارسی باستان (بیستون DB ۱؛۸۶) است و آن خود وام‌واژه‌ای سامی (آرامی maškā، اکدی mašku) است؛ افتادن واکهٔ پایانی در گذر از پارسی باستان به فارسی میانه قاعده‌مند است. پژوهش امروزی ادعای نورایی (سنسکریت ← پهلوی) را رد می‌کند و جهت را برعکس می‌داند.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D9%85%D8%B4%DA%A9\",\n      \"https://en.wiktionary.org/wiki/%D9%85%D8%B3%D9%83\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"BQT:2014\", \"status\": \"supports\",\n       \"note\": \"BQT_v4_pages.txt pdf p.97 (= printed 2014), the مشک/مشگ entries; footnote (OCR): 'در پهلوی [mašk] ، وآن اصلا بمعنی چرم (مخصوصا چرمی که در آن‌آب ریزند) وسپس صورت « مشک ابرزین » درپهلوی ...'. Nourai's page is right and the footnote supports his Pahlavi gloss 'leather'; it says nothing about Sanskrit.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p.55 (PHD.txt l.461–463); English index p.124 (l.2874, 3685)\", \"stance\": \"partial\",\n       \"note\": \"'¹mašk [mšk' | N ~] mussuck, skin bag (for liquids)'; 'maškīzag ... small mussuck'; index 'mussuck mašk; small ~ maškīzag' and 'skin ... ~bag hambān, mašk'. Supports the form and gloss, silent on the parent.\"},\n      {\"src\": \"KNT\", \"where\": \"Kent, Lexicon s.v. maškā- (leaf 215)\", \"stance\": \"contradicts\",\n       \"note\": \"'maškā- sb. ‚(inflated) skin‘; NPers. mašk, Akk. maš-ku-u ‚skin‘, Aram. maškā: borrowed from Semitic ... DB 1.86' — an Old Persian, Semitic-derived ancestor in place of Nourai's Sanskrit one.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, Glossary s.vv. †mašk and mēxak (NYB_vol2_glossary.txt l.2492, 2548)\", \"stance\": \"partial\",\n       \"note\": \"'†mašk 21²⁶, 22¹: restore the reading myhk' = mēxak, q.v.' and 'mēxak [myhk'] headquarter, the king's tent when the camp of his army is pitched ... there was no reason to replace it by [mšk'] mašk, as I unfortunately did in the text'. Nyberg thus withdraws one Pahlavi attestation of mašk (in the sense 'royal tent'), though he does not touch the 'skin bag' word; MacKenzie 1971 still lists ²mašk 'tent, pavilion'.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur printed p.473\", \"stance\": \"contradicts\",\n       \"note\": \"Places Pahlavi MASHK, MASHKIZAG and Sogdian MSHK in an inherited IE set with Skt. MESHAS/MASHAKA, Lith. MAISHAS, OPruss. MOASIS, OCS MECHU (Pokorny; Delamarre 'sac en peau' 148) — cognates, not a Sanskrit loan.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"mašk «مَشک ۳»; maškŭ «مَشکو ۲»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The Pahlavi→Persian arrow is solid for both words. NP مشک mašk 'water-skin' is the unchanged continuation of MP mašk (MacKenzie marks it 'N ~', i.e. identical in New Persian); the Old Persian ancestor maškā- had already lost its ending in Middle Persian, so nothing further happened. مشکو maškū is two words in one shape: (a) a real diminutive of mašk, 'small water-skin' (Mo'in: مشکو: مشک کوچک — this is the مَشکو ۱ of the chart's extra list, with مشکول and مشکوله beside it); and (b) the '(royal) tent/apartments' word, from MP ²mašk 'tent, pavilion' and the compound mašk-abarzēn 'royal pavilion' (MacKenzie p.55; Manichaean mškbrzyn). Mo'in's footnote on Borhan p.2014, on Henning's oral authority, spells out this second line: Pahlavi mašk-abarzēn in Xusrō ud Rēdag §103 (ed. Jamasp-Asana) means 'خیمهٔ سلطنتی' (royal tent), 'وهمین معنی‌است که درفارسی «مشکو» و «مشکوی» شده (ازافادات شفاهی استاد هنینگه)', with Sogdian mškw cited alongside. In classical Persian usage — including the Ferdowsī line the chart quotes, فغستان چو آمد به مشکوی شاه — maškūy is the king's private apartments, and Mo'in glosses مشکو as حرمسرای شاهان، کوشک، بالاخانه. So Nourai's '(royal) tent' is strictly the Pahlavi sense; the Persian sense had already moved from tent to palace chamber — a small gloss slip, not an etymological error.\",\n     \"derivation_fa\": \"پیوند پهلوی ← فارسی نو در هر دو واژه استوار است. «مشک» فارسی همان mašk فارسی میانه است، بی‌هیچ دگرگونی آوایی. «مشکو» دو واژهٔ هم‌نویسه است: یکی مصغّر مشک (معین: «مشک کوچک»، کنار مشکول و مشکوله)، دیگری بازماندهٔ mašk دوم پهلوی به معنای «خیمه، بارگاه» و ترکیب mašk-abarzēn «خیمهٔ سلطنتی» (مکنزی ص ۵۵). معین در حاشیهٔ برهان (ص ۲۰۱۴) به گفتهٔ شفاهی هنینگ می‌نویسد که همین ترکیب در فارسی «مشکو» و «مشکوی» شده است. در فارسی معنا از «خیمه» به «حرمسرا، کوشک، بالاخانه» تحول یافته؛ پس معنای «خیمهٔ شاهی» که نورایی داده معنای پهلوی است، نه فارسی.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D9%85%D8%B4%DA%A9\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"MON:4147\", \"status\": \"supports\",\n       \"note\": \"Page not verifiable (6-vol Mo'in not online); the entry text is in the 2-volume Adena condensation (MON_part2.txt): 'مشکو: (ا.مصف.) مشک کوچک؛ مشکو: [= مشکوی، مشکوبه] (ا.) حرمسرای شاهان. کوشک. بالاخانه.' — both of the chart's مشکو numbers, with the 'royal' sense as palace/harem rather than tent.\"},\n      {\"ref\": \"BQT:2014\", \"status\": \"supports\",\n       \"note\": \"Same page as node #1: 'وسپس صورت « مشک ابرزین » درپهلوی ( رسالةٔ خسرو کواتان بند ۱۰۳ طبق چاپ جاماسب اسانا) درآمده بمعنی خیمة سلطنتی، وهمین معنی‌است که درفارسی «مشکو» و «مشکوی» شده (ازافادات شفاهی استاد هنینگه) در سغدی mškw ...' — exactly this node's two words and their Pahlavi source.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p.55 (PHD.txt l.461–462)\", \"stance\": \"supports\",\n       \"note\": \"'¹mašk [mšk' | N ~] mussuck, skin bag (for liquids)' and '²mašk [mšk' | N maškē] tent, pavilion. ~abarzēn [-'plzȳn' | M mškbrzyn] royal pavilion' — the 'N ~' and 'N maškē' notations are MacKenzie's own statement of the Pahlavi→New Persian continuity for both senses.\"},\n      {\"src\": \"MON\", \"where\": \"2-vol Adena condensation s.v. مشکو (MON_part2.txt)\", \"stance\": \"supports\",\n       \"note\": \"'مشکو: (ا.مصف.) مشک کوچک؛ مشکو: [= مشکوی، مشکوبه] (ا.) حرمسرای شاهان. کوشک. بالاخانه.' The same volume glosses حرم with 'مشکو(ی)' — the harem sense is the standard Persian one.\"},\n      {\"src\": \"NYB\", \"where\": \"Glossary s.vv. †mašk / mēxak\", \"stance\": \"partial\",\n       \"note\": \"Nyberg reads mēxak 'the king's tent' where he had earlier printed mašk, i.e. one of the Pahlavi attestations of the 'royal tent' word is contested; this weakens the textual base of the maskhū line without touching Mo'in/Henning's Xusrō ud Rēdag evidence or MacKenzie's ²mašk.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Hindustani\",\n     \"words\": \"masak\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The word itself is real and everyday — Hindustani/Urdu मशक / مشک mašak, the whole dressed goatskin the bhīshtī carries on his back (Marathi masak) — but its parentage is the reverse of the arrow. Wiktionary derives Hindi मशक 'a kind of leather water-holding bag' from Classical Persian مشک < MP mšk' mašk < OP maškā-, and Whitworth's Anglo-Indian Dictionary (1885) already wrote 'Mashak. [Persian mashk.] A leather bag for carrying water' (with 'Masak. The Marāthī form of Mashak'). Sanskrit maśaka-, the parent Nourai draws from Klein, means 'gnat, mosquito' (Atharvaveda; from Proto-Indo-Aryan *makaśas by metathesis) and a bean-like skin eruption; Monier-Williams' further sense 'a leather water-bag' carries no text citation, i.e. it comes from the Sanskrit lexicographers, who are the usual channel by which a vernacular Persian loanword gets a Sanskrit shape. Given seven centuries of Persian as the administrative language of northern India, and given that the same object bears the same name from Old Persian onwards, the loan direction Persian → Hindustani is much the likelier. So the node's word and gloss are right, its parent is not — it should hang off the Persian node, not off a Sanskrit root.\",\n     \"derivation_fa\": \"خود واژه واقعی است: هندی/اردوی «مشک» همان مشک آب است که سقّا (بهیشتی) بر پشت می‌کشد؛ ولی پدرِ آن در نمودار برعکس است. ویکی‌واژه مشکِ هندی را وام‌واژه‌ای از فارسی کلاسیک می‌داند و ویت‌وورت (۱۸۸۵) نیز نوشته «Mashak. [Persian mashk.]». maśaka- سنسکریت در متون (از اثروودا به بعد) «پشه» است و معنای «مشک آب» در مونیر‌ویلیامز بی‌گواهِ متنی و از فرهنگ‌نویسان است. با توجه به قرن‌ها زبان دیوانی فارسی در هند، جهت فارسی ← هندی پذیرفتنی‌تر است؛ پس این گره باید زیر گرهٔ فارسی بنشیند، نه زیر ریشهٔ سنسکریت.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A4%B6%E0%A4%95\",\n      \"https://www.wisdomlib.org/definition/mashaka\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1018\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 545: 'mussuck, mussuk, n., a leathern skin for water (India) — Hind. masak, fr. OI. masakah.' Klein does make the Hindustani word a reflex of Old Indian, so Nourai reports his source faithfully; the objection is to Klein.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AID\", \"where\": \"Whitworth p.189 (AID.txt l.4422, 4427, leaf 207)\", \"stance\": \"contradicts\",\n       \"note\": \"'Mashak. [Persian mashk.] A leather bag for carrying water. The bhisti carries it on his back. The name distinguishes it from the double skin used by the pakhālī.'; 'Masak. The Marāthī form of Mashak.' Whitworth makes the Indian word Persian.\"},\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.603b s.v. MUSSUCK; p.92 s.v. BHEESTY\", \"stance\": \"supports\",\n       \"note\": \"'Hind. mashak, Skt. maśaka.' — Yule & Burnell back Klein. (Their BHEESTY article, p.92, is more cautious about Indian water-carrier vocabulary generally: 'The trade must be of ancient origin in India, as the leather bag is mentioned in the Veda and Manu ... Hence Col. Temple suggests that the word is Indian'.)\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie English index p.124 (PHD.txt l.2874)\", \"stance\": \"partial\",\n       \"note\": \"'mussuck mašk; small ~ maškīzag' — MacKenzie uses the Anglo-Indian word as his gloss for the Middle Persian one, i.e. the object and its name are continuously Iranian from the Achaemenid period on, which is what makes the Persian→Indic direction natural.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"English\",\n     \"words\": \"mussuck, mussuk\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"mussuck/mussuk is a Raj-era Anglo-Indianism taken straight from Hindustani mašak, the double spelling reflecting the unsettled 19th-century anglicisation of Hindustani final -ak (cf. dawk/dak, chowk). Hobson-Jobson p.603b: 'MUSSUCK, s. The leathern water-bag, consisting of the entire skin of a large goat, stript of the hair and dressed, which is carried by a bhīshtī (see BHEESTY). Hind. mashak, Skt. maśaka'; Klein p.1018: 'mussuck, mussuk, n., a leathern skin for water (India) — Hind. masak'; Whitworth (1885) cross-refers 'Mussuk. See Masak.' The Hindustani→English arrow is beyond doubt — it is the immediate parent all three sources agree on — and the word remains the standard English term for the object, which is why MacKenzie uses 'mussuck' to gloss Middle Persian mašk. Only the ultimate ancestor further up the chart is at issue (see the root and node #3).\",\n     \"derivation_fa\": \"«mussuck / mussuk» واژه‌ای انگلیسیِ هندی (Anglo-Indian) از دوران استعمار است که بی‌واسطه از مشکِ هندی گرفته شده؛ دوگانگی املا از بی‌قاعدگی لاتینی‌نویسیِ -ak هندی در سدهٔ نوزدهم است. هابسن‌جابسن (ص ۶۰۳)، کلاین (ص ۱۰۱۸) و ویت‌وورت (۱۸۸۵) هر سه همین پدر را می‌دهند؛ پس این پیوند قطعی است و ادعای نورایی درست. تنها سرچشمهٔ دورتر (سنسکریت) محل ایراد است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A4%B6%E0%A4%95\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1018\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 545 (pp. 1018–1019): 'mussuck, mussuk, n., a leathern skin for water (India) — Hind. masak, fr. OI. masakah.' Both spellings, the gloss and the Hindustani parent, exactly as the chart has them.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.603b (HJB.txt l.15145, leaf 624)\", \"stance\": \"supports\",\n       \"note\": \"'MUSSUCK, s. The leathern water-bag, consisting of the entire skin of a large goat, stript of the hair and dressed, which is carried by a bhīshtī (see BHEESTY). Hind. mashak, Skt. maśaka.'\"},\n      {\"src\": \"AID\", \"where\": \"Whitworth p.189 (AID.txt l.4790, 4422)\", \"stance\": \"supports\",\n       \"note\": \"'Mussuk. See Masak.' + 'Masak. The Marāthī form of Mashak. [Persian mashk.]' — supports the Hindustani→English step while contradicting the Sanskrit ancestor.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p.55 and English index p.124\", \"stance\": \"partial\",\n       \"note\": \"MacKenzie glosses Middle Persian ¹mašk as 'mussuck, skin bag (for liquids)' and indexes 'mussuck mašk' — an Iranianist's use of the English word for the Iranian object.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nout = \"/home/sfmqrb/git/rishe/data/verification/page-321.json\"\nwith io.open(out, \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\", out)\nPYEOF"
}
```


### [2026-09-07T16:16:20.168Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-321.json
```


## [2026-09-07T16:16:26.227Z] TOOL CALL #79: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-321.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 321"
}
```


### [2026-09-07T16:16:27.710Z] TOOL RESULT

```
JSON OK
nodes verified: 12/12
node verdicts: {'plausible': 1, 'confirmed': 9, 'disputed': 2}
root verdicts: {'plausible': 1, 'confirmed': 1, 'disputed': 1}
ref checks: {'supports': 11, 'partial': 1, 'not_checked': 2}
books consulted: {'supports': 21, 'silent': 7, 'partial': 9, 'contradicts': 3} | by book: {'PHD': 6, 'MON': 5, 'LKT': 2, 'WEB': 2, 'KLN': 2, 'SKT': 2, 'HRN': 2, 'BRT': 2, 'ARY': 2, 'NYB': 2, 'AID': 2, 'HJB': 2, 'AFA': 1, 'FVQ': 1, 'FSD': 1, 'SYN': 1, 'LAT': 1, 'PHN': 1, 'HUB': 1, 'SOD': 1, 'KNT': 1}
```


## [2026-09-07T16:16:46.580Z] AGENT

0 PROBLEM lines. Page 321 (book p. 291) verified.

**Counts** — 3 non-redirect entries, 12 nodes. Nodes: 9 confirmed, 1 plausible, 2 disputed. Roots: 1 confirmed, 1 plausible, 1 disputed. Ref checks: 11 supports, 1 partial, 2 not_checked. 40 `consulted` records (21 supports, 9 partial, 3 contradicts, 7 silent).

**Disputed / flagged**
- ROOT `Mašakah` (Sanskrit "animal skin for carrying water") — disputed. Klein 1018 and Hobson-Jobson 603b do say "Hind. mashak, Skt. maśaka", but Kent's OP lexicon has `maškā-` "(inflated) skin" (Behistun DB 1.86) "borrowed from Semitic" (Aram. maškā, Akk. mašku); Sanskrit maśaka- is "gnat" (< PIA *makaśas), the "leather water-bag" gloss resting only on the lexicographers. Chain is Semitic → OP → MP/NP → Indic, i.e. inverted.
- `#1 mašk` [Pahlavi] — disputed: form/gloss perfect (MacKenzie 55; Mo'in's Borhan footnote p.2014), but the parent should be OP maškā-, not Sanskrit.
- `#3 masak` [Hindustani] — disputed: Wiktionary and Whitworth's *Anglo-Indian Dictionary* (1885, p.189, "Mashak. [Persian mashk.]") make it a Persian loan, so it belongs under the Persian node.
- ROOT `Mantellum, Mantil` — plausible: the glosses are crossed (mantēle/mantīle is the *towel*, mantellum the *cloak*; "Mantil: cloak" is wrong), and the two may be etymologically distinct (Pokorny 1073 *man-terg-s-li vs. Klein's/Buck's Celtic mantum).
- `#1 mandîl` [Arabic] — plausible: right ultimate source, but the chart omits the Byzantine Greek μανδήλιον step that Nourai's own KLN:932 gives.

**Book errors (printed page, extraction faithful)** — the `Mareğâ` note prints *"related to the Greek word 'amorphous: shepherd'"*; EAV p.866 §12 actually reads ἀμορβός *amorbós* "compagnon, berger". Nourai's misprint; the comparison is also obsolete (Beekes: "unknown"). Page image saved to `data/verification/sources/refs/ocr/BOOK/321.png`.

**Extraction errors for the owner to fix: none** — the JSON matches the printed page (arrows, scripts مانتو/منديل/مَرغ ۲/مَشکو ۲, quotes, refs all check out).

**Citation drift worth noting**: KLN:932 → mandil is on pp. 930–931 of the 1966 scan; KLN:934 → manteau/mantle are on pp. 935–936; SOD:216 → the mrγ entries (5431, 5434) sit at printed ≈213. BQT:1990 and BQT:2014 are exact.
