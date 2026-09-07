# Verification process log — verify-page-346


## [2026-09-07T17:36:18.999Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 346 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-346.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-346.json. Write /home/sfmqrb/git/rishe/data/verification/page-346.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 346` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T17:36:20.703Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T17:36:21.413Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T17:36:21.431Z] TOOL RESULT

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


## [2026-09-07T17:36:21.602Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-346.txt"
}
```


### [2026-09-07T17:36:21.614Z] TOOL RESULT

```
1	=== PDF page 346 (book page 316) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Na 1, Nau, Naus : boat  (refs POK:755)
4	#1 (parent #0) [Avestan / Old Persian] refs=PRT:429; HRN:229; IRN:123 | nâu, nâviya : ship. Also any groove, line, cavity or trench used as a guide for carrying water, grain, arrow, etc. ; nâv-dân : water path, gutter ☞Dâ 2
5	  #2 (parent #1) [Persian] refs=BQT:2110; MON:4644 | nâv «ناو» : ship, water path, pipe, river ; nâv-dân «ناودان» : water way, gutter ☞Dâ 2 | extra: ناوشکن، ناودیس، ناوسار، ناخدا، ناوگان، ناوران، ناوبان، ناودار
6	#3 (parent #0) [Persian] refs=MON:4645,4650 | nâvânîdan «ناوانیدن» : to bend something (shape like a boat) ; nâvîdan «ناویدن» : to walk while moving to the sides (like a ship)
7	#4 (parent #0) [Persian] refs=MON:4649; BQT:2112; FSF:321 | nâveh «ناوه» : a guide for feeding grains to a mill, a hollow piece of wood used for carrying mud and cement, the groove on grains, the hole or guide used for shooting small arrows, the arrow shot this way. ; nâvak «ناؤک» : a small arrow (shot through a guide)
8	#5 (parent #0) [Latin] refs=AHD | navis : ship
9	  #6 (parent #5) [English] refs=None | navy ; navigate
10	#7 (parent #0) [Greek] refs=AHD | naus : ship
11	  #8 (parent #7) [English] refs=None | nautical ; nausea ; noise ; nautilus ; astronaut ; cosmonaut ; aeronaut
12	--- entry 1 ---
13	ROOT [Indo-European] Nâ 2 : to help  (refs POK:754)
14	#1 (parent #0) [Avestan / Old Persian] refs=HUB:43; HRN:72 | pa-nâtha, pati-nâtha, pa-nâh : protection help, shelter ☞Pa
15	  #2 (parent #1) [Persian] refs=HRN:72; BQT:418 | panâh «پناه» : shelter
16	
```


## [2026-09-07T17:36:24.748Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-346.json",
 "description": "Read source JSON for page 346"
}
```


### [2026-09-07T17:36:24.788Z] TOOL RESULT

```
{
  "pdf_page": 346,
  "book_page": 316,
  "entries": [
    {
      "root": {
        "name": "Na 1, Nau, Naus",
        "lang": "Indo-European",
        "refs": "POK:755",
        "gloss": "boat"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "PRT:429; HRN:229; IRN:123",
          "words": [
            {"translit": "nâu, nâviya", "gloss": "ship. Also any groove, line, cavity or trench used as a guide for carrying water, grain, arrow, etc.", "script": null},
            {"translit": "nâv-dân", "gloss": "water path, gutter", "script": null, "see": ["Dâ 2"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2110; MON:4644",
          "words": [
            {"translit": "nâv", "gloss": "ship, water path, pipe, river", "script": "ناو"},
            {"translit": "nâv-dân", "gloss": "water way, gutter", "script": "ناودان", "see": ["Dâ 2"]}
          ],
          "script_extra": "ناوشکن، ناودیس، ناوسار، ناخدا، ناوگان، ناوران، ناوبان، ناودار",
          "note": null,
          "quote": {"text": "درتحیّر طفل میزد دست و پا - آب می بردش به ناو آسیا", "poet": "Attâr"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:4645,4650",
          "words": [
            {"translit": "nâvânîdan", "gloss": "to bend something (shape like a boat)", "script": "ناوانیدن"},
            {"translit": "nâvîdan", "gloss": "to walk while moving to the sides (like a ship)", "script": "ناویدن"}
          ],
          "note": null,
          "quote": {"text": "چو مست هر طرفی می فتی و می ناوی - که شب گذشت کنون نوبت دعاست، مَخْسب", "poet": "Molavî"}
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:4649; BQT:2112; FSF:321",
          "words": [
            {"translit": "nâveh", "gloss": "a guide for feeding grains to a mill, a hollow piece of wood used for carrying mud and cement, the groove on grains, the hole or guide used for shooting small arrows, the arrow shot this way.", "script": "ناوه"},
            {"translit": "nâvak", "gloss": "a small arrow (shot through a guide)", "script": "ناؤک"}
          ],
          "note": null,
          "quote": {"text": "دلم از ناوک مژگان جفا دوخته ای - کشتن عاشق بیدل ز که آموخته ای", "poet": "Bahâr"}
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "navis", "gloss": "ship", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "navy", "gloss": null, "script": null},
            {"translit": "navigate", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "naus", "gloss": "ship", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "nautical", "gloss": null, "script": null},
            {"translit": "nausea", "gloss": null, "script": null},
            {"translit": "noise", "gloss": null, "script": null},
            {"translit": "nautilus", "gloss": null, "script": null},
            {"translit": "astronaut", "gloss": null, "script": null},
            {"translit": "cosmonaut", "gloss": null, "script": null},
            {"translit": "aeronaut", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Nâ 2",
        "lang": "Indo-European",
        "refs": "POK:754",
        "gloss": "to help"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "HUB:43; HRN:72",
          "words": [
            {"translit": "pa-nâtha, pati-nâtha, pa-nâh", "gloss": "protection help, shelter", "script": null, "see": ["Pa"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:72; BQT:418",
          "words": [
            {"translit": "panâh", "gloss": "shelter", "script": "پناه"}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-07T17:36:25.024Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T17:36:25.066Z] TOOL RESULT

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


## [2026-09-07T17:36:40.618Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','PRT','HRN','IRN','BQT','MON','AHD','HUB','FSF','FRS','ARY','PHD','BRT']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600])\n    print()\n\""
}
```


## [2026-09-07T17:36:40.749Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && head -80 data/verification/page-316.json"
}
```


### [2026-09-07T17:36:41.919Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (also originsshortetym0000unse, bwb_P8-AVM-445, 1958)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/v

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs

FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
```


### [2026-09-07T17:36:41.967Z] TOOL RESULT

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
----
{
  "pdf_page": 316,
  "book_page": 286,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-06",
  "entries": [
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
          "note": "Pokorny 694 is 'mā-3, Meaning: mother (expr. root), Note: redupl. māmā, māmmā ... Material: Old Indic mā ‘mother’ ... npers. mām, māmā, māmī ‘mother’ ... Latin mamma ... mamilla ‘nipple’ ... Page(s): 694' (POK_full.txt l.57758ff, grep 'lemma: mah 3'). It therefore supports the Mā- half of the root box, but glosses it ‘mother’, not ‘breast’; Pokorny's separate lemma 'mahter-, Meaning: mother, Note: based on a babble-word mah-, see there ... Page(s): 700-701' is where Mā-ter belongs, i.e. p.700-701 and not 694."
        },
        {
          "ref": "PRT:386,863",
          "status": "not_checked",
          "note": "Partridge, Origins (1958) — no open copy: all 8 archive.org copies are lending-only per data/verification/sources/refs_online.json (kind 'archive_restricted'), and there is no local OCR."
        },
        {
          "ref": "SYN:103",
          "status": "supports",
          "note": "Buck 2.36 on printed p.103 (SYN.txt l.2813): ‘2.36. ‘Mother’. 1. IE *māter-, prob. ... starting fr. a nursery word of the ma type. Walde-P. 2.229. Here belong the Grk., Lat., Ir., Gme. ... and Indo-Iranian forms’ and ‘2. Nursery words that have become the usual terms. Type mama (above, p. 94, Walde-P. 2.221) in It. mamma ... and W., Br. mam.’ Nourai's own remark (‘probably started as a nursery word and became a usual term’) is a paraphrase of exactly these two headings."
        }
      ],
      "consulted": [
        {
          "src": "WLD",
          "where": "Bd. II 221 (§3 mā) and Bd. II 229 (matēr-)",
          "stance": "supports",
          "note": "WLD_Bd2_pages.txt leaf 225 (printed 221): ‘3. mā Lallwort für ‚Mutter‘, redupl. mama, mammā ... Obwohl das unred. mā die Grundlage von māter- (s. d.) ist ... Ai. mā ‚Mutter‘; np. mām, māmā, māmī ‚Mutter‘’; leaf 233 (printed 229): ‘matēr- ‚Mutter‘, beruht auf dem Lallwort mā-, s. d. ... Ai. mātār-, av. mātar-, arm. mair ... gr. mētēr, dor. mātēr ... lat. mater, -tris’. Both halves of Nourai's root box are thus real and correctly linked."
        },
        {
          "src": "AHD",
          "where": "Watkins 1985 s.v. māter-",
          "stance": "partial",
          "note": "AHD_watkins1985.txt l.730: ‘māter-. Mother. Based ultimately on the baby-talk form ma-2, with the kinship term suffix -ter-. 1. Germanic *mōthar- ... 2. Latin māter ... 3. Greek mētēr ... 4. Latin māteriēs, materia, tree trunk (< “matrix,” the tree’s source of growth) ... [Pok. māter- 700.]’ Supports the structure of the whole chart but calls -ter- the KINSHIP suffix, not an agent suffix, so Nourai's gloss ‘feeder (of the family)’ is his own."
        },
        {
          "src": "IEC",
          "where": "Mann, pp. 735–736 s.v. mātēr (1) and māter- (2)",
          "stance": "partial",
          "note": "IEC.txt l.10369: ‘mātēr (māter-, mātr) (1) ‘mother’ ... WP II, 229 Skt. mātā; ... Per. mādar; Oss. mad, madä; Tokh. mācar ... Gk. métēr ... Lat. mater’, but Mann sets up a SEPARATE root ‘māter- (2) ‘wood, timber, substance’ ... Lat. materies ... materia’, i.e. he does not put Latin materia under ‘mother’ as Nourai (and Watkins) do."
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Avestan",
          "words": "mâtar",
          "verdict": "confirmed",
          "derivation": "Avestan mātar- f. ‘mother’ is the regular Iranian reflex of PIE *méh₂tēr (nom. *mātē, stem *māter-) via Proto-Iranian *máHtā: the PIE laryngeal *h₂ is lost with lengthening of the vowel, and *-ter- is retained. It is attested in the Younger Avesta (V. 12.1 yaṭ pitā vā mātā vā parəiriθyāiti ‘if father or mother dies’, Yt. 17.16, Y. 38.5 of animal mothers). Old Persian has the same stem, preserved only in the haplologised compound hamātā < *hama-mātā ‘having the same mother’ (Bisitun I 30, of Smerdis and Cambyses). Sanskrit mātár-, Greek Doric mātēr, Latin māter are the exact cognates, so the arrow root → Avestan is correct.",
          "derivation_fa": "اوستایی mātar- «مادر» بازماندهٔ قاعده‌مند هندواروپایی آغازین *méh₂tēr است که از راه ایرانی باستان *máHtā به اوستا رسیده؛ حنجرهٔ هندواروپایی افتاده و در عوض واکه کشیده شده است. این واژه در اوستای نو (وندیداد ۱۲،۱) گواهی دارد و در پارسی باستان تنها در ترکیب hamātā «همان مادری» (سنگ‌نوشتهٔ بیستون) مانده است. بارتولومه (فرهنگ ایرانی باستان، ستون ۱۱۶۷) و کنت همین را می‌گویند؛ پس این پیوند در نمودار نورایی درست است.",
          "sources": [
            "https://en.wiktionary.org/wiki/%F0%90%AC%A8%F0%90%AC%81%F0%90%AC%99%F0%90%AC%80%F0%90%AC%AD",
            "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9h%E2%82%82t%C4%93r"
          ],
          "ref_check": [
            {
              "ref": "POK:694",
              "status": "partial",
              "note": "Pokorny p.694 (mā-3) does NOT list Avestan mātar-; the Avestan form stands in the neighbouring lemma 'mahter-' … 'Old Indic matar- ‘mother’, Avestan matar-, Armenian mayr … Page(s): 700-701' (POK_full.txt l.57703ff). So the claim is right but the page number should be 700."
            },
            {
              "ref": "SKT:336",
              "status": "partial",
              "note": "Skeat's entry is real but not on p.336 of the edition on disk: 'Mother (1), a female parent. [M.E.] moder. A.S. mōdor … + Du. moeder, Icel. mōðir … L. mater, Gk. mētēr, Skt. mātā, mātṛ … formed with Aryan suffix -tar (of the agent) from √MĀ, orig. to measure … Orig. sense uncertain, perhaps ‘manager’ of the household' — SKT.txt leaf 318, i.e. printed p. ~298 of the 1911 impression (leaf = printed+20); leaf 356 = p.336 is the 'Parity–Parsee' page. Content supports Av./Skt. mātar- as source of ‘mother’, but Skeat's own etymology is √MĀ ‘to measure’, i.e. ‘manager’, not Nourai's ‘feeder’."
            }
          ],
          "consulted": [
            {
```


## [2026-09-07T17:36:53.519Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full naus ===\"; grep -n -i \"lemma: naus\" POK_full.txt | head -20\necho \"=== POK_full pages 754-755 ===\"; grep -n \"Page(s): 75[3-6]\" POK_full.txt | head -20\necho \"=== AHD nau ===\"; grep -n -i \"^nāu\\|nāu-\\|nau-1\\|nāus\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T17:36:53.595Z] TOOL RESULT

```
=== POK_full naus ===
61944:Root / lemma: naus-1 {* he-nahus-1) 
=== POK_full pages 754-755 ===
61605:Page(s): 753 
61771:Page(s): 754 
61797:Page(s): 754 
61813:Page(s): 755 
61867:Page(s): 755 
61881:Page(s): 754 
61895:Page(s): 754 
61907:Page(s): 754 
61942:Page(s): 756 
61984:Page(s): 755-756 
62495:Page(s): 756-758 
=== AHD nau ===
```


## [2026-09-07T17:36:54.467Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT nāu ===\"; grep -n \"nāu\\|nāvaya\\|nāviia\" BRT.txt | head -40\necho \"=== BRT nāθa ===\"; grep -n \"nāθa\\|pa-nāθa\\|paiti-nāθa\" BRT.txt | head -40"
}
```


### [2026-09-07T17:36:54.539Z] TOOL RESULT

```
=== BRT nāu ===
=== BRT nāθa ===
```


## [2026-09-07T17:36:57.155Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '61760,61830p' POK_full.txt\necho \"=======\"\nsed -n '61860,61990p' POK_full.txt"
}
```


### [2026-09-07T17:36:57.226Z] TOOL RESULT

```
Page(s): 731 

Root / lemma: nak- 
Meaning: fur 

Material: Gr. vcxkoc, n., voKri f. "woolen fell, fur, fleece', apvaKi(; f. (for *apvo-vaKi(;) " fleece 
', vaKu(5)piov 5£ppa Hes.; Old English naesc^saW. leather as e.g. buckskin ' {*nak-s-ko-, - 
ka\ compare the -e5-stem vqkoc;); Old Prussian nognan {irom *noknan) n. "leather' {*nak- 
no-)\ in addition after E. Lewy Old Indie naka-^ vault of the sky, firmament, heavens, skies 

References: WP. II 316. 
Page(s): 754 

Root / lemma: nana, nena etc. 

Meaning: mother, etc.. (child word) 

Material: Old Indie /7a/7a "mother, old woman ', */7a/75/7a reshaped (after svasa: svasr-) to 

nanandar^oia husband's sister', np. /75/75 "mother'; 

Alb. Geg nona, nana " mother ' 

gr. vavva, vivvr) " aunt ', vsvvoc;, vavvaq "uncle'; alb. /75/7e "mother, wet nurse '; Latin 

nonnusm., nonnaf. late " word used by young monks when addressing elders, a nun ', 

also " nurserymaid '; cymr. nain{*nanJ) "grandmother'; russ. njanja^ children keeper, 

nurse, caretaker of a baby or young children, nanny ' (dial, also "older sister '), Bulgarian 

/7e/7/" older person, elder', Serbo-Croatian nena, /7a/7a "mother', Serbian /7a/7 "father'; 

compare also Modern High German Nenne, Kinderwort for "milk'. 

References: WP. II 317, WH. II 175. 

Page(s): 754 

Root/ lemma: nant- {* he-nant-) 
Meaning: to dare, risk 



Note: only Celtic and Germanic 

Material: Old Irish ne/'tm. 'fight, struggle' {*nanth)\ Gothic ana-nanf^Jan' venture, risk', Old 
Icelandic nenna " give one's heart ', (under the influence of common Celtic -ns-, -nt- > -nn- 
), Old High German preterit ginand' have courage ', ginenden. Old Saxon nathian. Old 
English /7eA'5/7 "venture, risk'. Old Icelandic nenninn^ active, keen ', Middle High German 
genende(c)^keev\, eager'. Old High German nand {a\so in names as Ferdinand), Old 
English nodi. " courage '. 
References: WP. II 317. 
Page(s): 755 

Root / lemma: /7a5- nasalized {*neu-s) 

Meaning: nose 

Note: (/755-from the lengthened grade case this conservative stem, originally Nom. Sg.), 

originally probably " nostril ' 

Note: 

Root/ lemma: nas-: nose' derived from Root/ lemma: neu-ks-, neu-s-\ "to sniff, smell' 

which derived from zero grade of Root/ lemma: an(a)-3\ "to breathe' : Root/ lemma: 

ansu-, QSU-\ "ghost, demon': Old Indie asu-, Avestan arjhu-^ breath of life, world '. 

=======

Church Slavic /7c»z£y/7"nostrir (from -sr-), nost "nose' (russ. "foreland, promontory'). 

References: WP. II 318, WH. II 143 ff., Trautmann 193 f., Holthausen KZ. 69, 166 f., 

Specht Indo Germanic Dekl. 75. 

Page(s): 755 



Root / lemma: nag^h- {* he-nag''h-) 

Meaning: sober 

Note: Only Armenian and gr. 

Material: Armenian naut'/" sober'; gr. vncpoj, Doric vdcpw "be sober'. 

References: WP. II 317. 

Page(s): 754 

Root / lemma: na-1{*he- na-1) 

Meaning: to help, be of use 

Material: Old Indie na-tha-u. 'help', m. 'guarder', na-tha-te^ begs '; gr. 6-vi-vr|-Mi, -va-jjsv " 

use, take advantage of ', Fut. o-vn-ou), Med. 6-vi-va-|jai, Aor. u)vri|jr|v 'have benefit', 

ovsiap n., more properly 6vr|ap, -aioc, "benefit' {*o-na-uj), etc. 

References: WP. II 315. 

Page(s): 754 

Root / lemma: na-2 {* he-na-2) 

Meaning: to be afraid, ashamed 

Material: Old Irish nar^b\us\\M' {*na-sro-), na(i)re^Vc\e genitals' {*na-srlia)\ Hittite nah(h)- 

'fear, dread, be afraid', nahsania-^be afraid'. 

References: H. Pedersen Hittitisch 187. 

Page(s): 754 

Root / lemma: nau-2: nau- : nu- {*he- nau-2) 

Meaning: death; corpse 

Material: A. Gothic naus^ corpse ' {ga-namstron' bury'), Old Icelandic nar ds., Old English 

ne(o)vc\. ds.; Old Russian navb 'corpse ', acech. nav, -/m. ' hereafter, life after death, 

future life, world to come, world of the dead, hell', Latvian nawe^dea\.b\ therefrom nawet 

'slay', nawfties^ strive oneself, kill oneself; Old Prussian /70i4vs 'trunk'. 

B. Old Irish /7j/7e (older naunae) f., cymr. newynvn. ' famine' {*nauenio-), bret. naoun 
{*n9Ueno-) ds.; mcymr. /7e^eo''longing, yearning, need' {*nau-ita)\ Latvian nawWes {see 
above), Lithuanian /70i/y// "torment, smite, slay', /s-/7di/y// "destroy'; causative Old Church 
Slavic Czech ^/7ai////" exhaust', Postverbal Czech unava^ fatigue ', russ. dial, onava' 
tiredness ', zero grade Old Church Slavic unyt/"be slack, languish, tire, slacken ', Czech 
nyt/' dahinschmachten ', russ. nytb " become elegiac '. 



nau-f/-\n Gothic nau/=>st 'need, compulsion ', Old Icelandic naud, naudri. " compulsion, 
tribulation, Notwendigkeit', Old Saxon nod, Old High German not' crowdedness, 
tribulation, need'. Old English nead-, nTedt "need, obligation, tribulation'; Old Prussian 
nautin {*nauti-) (Akk.) 'need'; in Slavic forms with ^and g, /and o'(see Meillet, Slave 
commun2 61 f.): Old Church Slavic ngzda' compulsion, force, might, necessity', poln. 
ngdza'nee6', Old Bulgarian /7po'///"notigen', but also Old Church Slavic nuzda' 
compulsion, need', nud/t/ 'n6t\gen', poln. nuda' boredom, weariness '; with /poln. ngt' 
temptation ', Bulgarian nut 'compulsion ', poln. nuc/c{^6. Jhdt.) 'constrain, oblige'; the -d- 
stands as Indo Germanic extension besides -/-, das phas originated through secondary 
nasalization. 

References: WP. II 316, Trautmann 201 f.; Loth RC 45, 199 ff. 
Page(s): 756 

Root / lemma: naus-1 {* he-nahus-1) 

Meaning: boat 

Grammatical information: f. Akk. naurp 

Material: Old Indie nau-{Hor(\. nauh) 'ship, boat' {navya-^ navigable'); ap. nav/yal\ee\.' (: 

gr. vriiO(; ' belonging to the ship '); navaja-m. ' skipper, captain of a ship; sailor', Avestan 

navaza-6s (: gr. vau-r|Y6(; ds., compare also Latin navig-are, -ium); Avestan navaya-' 

navigable' (about Old Indie ati-nus. Brugrnann 111 137 Anm. 2); Armenian /7aK'ship' (from 

Pers.?); gr. hom. vr|uq, vr|6q (*vaF6q), Attic vauq, vscbc; 'ship'; Latin navisdiS. (originally 

conservative stem, compare Akk. navem= Old Indie navam, gr. vpa; Old Irish nau {Gen. 

noe, Dat. PI. noib) 'ship'; cymr. /7c»e 'flat vessel, kneading or dough trough; dough tray; 

hutch ', bret. neo6s. {*nauia)\ here gall, (vorrom.) nava' Talschlucht ', also FIN; gall. 

nausum 'sh\p'; Old Icelandic norm, 'ship', nau-st' Schiffsschuppen ', nda-tun{nda= gr. 

vnwv) ' Schiffsburg ', Old English nowend' skipper, captain of a ship; sailor', (but Middle 

High German nawe, nsewe'smaW ship'. Modern High German dial. Naueiroxw Latin); 

Norwegian no' trough from a hollow trunk ', n0la ( *ndwildn-) 'large trough, big boat' Old 

High German nuosc. Middle High German nuoschm. 'trough, gully'. Old Frisian nost 

'trough'. Middle Low German noste' Viehtrog , Wassertroq '; here the Lithuanian FIN 

Nova, polonis. Nawa. 

Maybe through metathesis alb. *naviya, a/7ya'ship' maybe Arabic origin. 

References: WP. II 315, WH. II 148 f., J. Hubschmid R. int d'Onom. 4, 3 ff. 

Page(s): 755-756 

Root/ lemma: ne2, ne{*he-ne-2) 



Meaning: Enclitic particles
```


## [2026-09-07T17:37:06.639Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD nau boat ===\"; grep -n -i \"nau\" AHD_watkins1985.txt | grep -i \"boat\\|ship\\|navis\\|naus\" | head -20\necho \"=== AHD nausea/nautical ===\"; grep -n -i \"nautical\\|nausea\\|navigate\\|nave\\b\" AHD_watkins1985.txt | head -20\necho \"=== AHD na- help ===\"; grep -n -i \"^na-\\|na-1\\|oninemi\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T17:37:06.705Z] TOOL RESULT

```
=== AHD nau boat ===
138:On the other hand, from the absence of a general word for “sea” we may deduce that the Indo-Europeans were originally an inland people. A root mori- is attested dialectally (MERE), but it may well have referred to a lake or other smaller body of water. Trans- portation by or across water was, however, known to the Indo-Europeans, since most of the languages attest an old word for boat or ship, nau-?, probably propelled by oars or a pole (ere-', “to row”).
772:nau-2, Boat. Contracted from *naau-. 1. Latin ndvis, ship: NACELLE, NAVAL, NAVICULAR, NAVIGATE, NAVY. 2. Greek naus, ship, and nautés, sailor: NAUSEA, NAUTI- CAL, NAUTILUS, (NOISE); AERONAUT, AQUANAUT, ARGO- NAUT, ASTRONAUT, COSMONAUT. [Pok. 1. ndu- 755.]
1142:HELMINTH; ANTHELMINTIC, PLATYHELMINTH. [Pok. 7. uel- 1140.] wel-‘, To tear, pull. 1. Suffixed form *wel-do- in Latin vellere, to tear, pull: AVULSE, CONVULSE, DIVULSION, EVULSION, REVULSION, SVELTE. 2. Suffixed form *wel-no- in Latin vullis, shaggy hair, wool: VELOURS, VELVET, VILLUS [Pok. 8. wel- 1144.] wele-'. Wool. Probably related to wel-‘. 1. Suffixed extended zero-grade form “*wi-nd- in: a. Germanic *wullé in Old English wul(l), wool: woot; b. Italic *wland in Latin lana (> French laine), wool, and its derivative laénig6, down: LANATE; DELAINE, LANIFER- OUS, LANOLIN, LANUGO; ¢. Celtic *wland in Welsh gwlan, wool (> Middle English flannel, woolen cloth): FLANNEL. 2. Possible suffixed o-grade form *wol(o)-no- in Greek oulos, wooly, curly: ULoTRICHOUs. [Pok. 4. uel- 1139.] wela-2. To strike, wound. 1. Suffixed o-grade form *wol()-o- in Germanic *walaz in Old Norse valr, the slain in battle in: a. Old Norse Valhdéll, Valhalla: VAL- HALLA; b. Old Norse Valkyrja, “chooser of the slain,” name of one of the twelve war goddesses (-kyrja, chooser; see geus-): VALKYRIE. 2. Suffixed basic form *welo-nes- in Latin vudnus (stem vulner-), a wound: VULNERABLE. [In Pok. 8. wel- 1144.] welg-. Wet. Germanic *welk- in: a. Old English wolc(e)n, cloud, sky: WELKIN; b. Middle English welken, to wilt: wILT!. [Pok. 2. welk-, uelg-, 1145.] welt-. Woods; wild. 1. Suffixed form *wolt-u- in Germanic *walthuz in: a. Old English weald, wald, a forest: WEALD, WOLD!; b. Old Norse vdllr, field: VOLE!. 2. Ger- manic *walthdn- in Middle English welde, a plant yield- ing a yellow dye, weld: WELD2. 3. Germanic *wilthigaz in: a. Old English wilde, wild: wip; b. Old English wildéor, wilddéor, wild beast (déor, animal; see dheu-'): WILDERNESS; C. Dutch wild, wild: WILDEBEEST. [In Pok. 4. uel- 1139.] weme-. To vomit. 1. Germanic *wam- in Old Norse vamla, qualm, and Danish vamle, to become sick, prob- ably akin to the Scandinavian source of Middle English wam(ejlen, to feel nausea, stagger: WAMBLE. 2. Latin vomere, to vomit: NUX VOMICA, VOMIT. 3. Greek emein, to vomit: EMESIS, EMETIC. [Pok. wem- 1146.] wen-', To desire, strive for. 1. Suffixed form *wen-w- in Germanic *winn(w)an, to seek to gain, in Old English winnan, to win: WIN}. 2. Suffixed zero-grade form *wn-ydé in Germanic *wunjé in Old English wynn, wen, pleasure, joy: WEN2, WINSOME. 3. Suffixed (stative) zero-grade form *wn-é-, to be contented, in Germanic *wunén in Old English wunian, to become accustomed to, dwell: won!, (wont). 4. Suffixed (causative) o-grade form *won-eyo- in Germanic *wanjan in Old English wenian, to accustom, train, wean: WEAN}. 5. Germanic *wéniz, hope, with denominative *wénjan, to hope, in Old English wénan, to expect, imagine, think: WEEN. 6. Suffixed zero-grade form *wn-sko- in Germanic *wunsk- in Old English wyscan, to desire, wish: WISH. 7. O-grade *won- perhaps in Germanic *wani- in: a. Old Norse Vanir, the Vanir: VANIR; b. Old Norse vana- in Vanadis, name of the goddess Freya: VANADIUM 8. Suf- fixed form *wen-es- in: a. Latin venus, love (> venerari, to worship): VENERATE, VENEREAL, VENERY!, VENUS; b. suffixed form *wen-es-no- in Latin venénum, love potion, poison: VENOM. 9. Suffixed form *wen-eto-, “be- loved,” possibly in Germanic *Weneda-, a Slavic people, in Old High German Winida, the Wends: WEND. 10, Suffixed form “wen-yd@ in Latin venia, favor, forgive- ness: VENIAL. 11. Lengthened-grade form *wén-d- in Latin véndri, to hunt: VENATIC, VENERY2, VENISON. 12. Suffixed basic form *wen-o- in Sanskrit vanam, forest: WANDEROO. 13. Possibly zero-grade suffixed form *wn-ig- in Sanskrit vanik, vdnijah, merchant (? < “seek- ing to gain”): BANIAN. [Pok. 1. ven- 1146.] wen-2. To beat, wound. 1. Suffixed zero-grade form
1902:NATAL gene- NATANT sna- NATATION sna- NATATORIAL sna- NATATORIUM sna- NATES not- NATHELEsS to- NATION gene- NATIVE gene- NATURE gene- NAUGHT ne, wektl- NAUGHTY ne NAUSEA nau-2 NAUTCH ner-2 NAUTICAL nau-2 NAUTILUS nau-2 NAVAL nau-2 NAVE? nobh- NAVEL nobh-, nau-2 NAVIGATE ag-, nau-2 NAVY nau-2
=== AHD nausea/nautical ===
173:It was probably not long before the disper- sal of the Proto-Indo-European community that the use of the wheel and wheeled trans- port was adopted. Despite the existence of widespread word families, most terms relat- ing to wheeled vehicles seem to be metaphors formed from already existing words; they are not primitives or primary vocables. So the word for AXLE (aks-) may mean simply “a pivotlike juncture”; the NAVE or hub of the wheel (nobh-) is the same word as NAVEL. This is clearly the case with WHEEL itself, where the widespread *k(e)-k“l-o- is an ex- pressive derivative of a verb (k"el-') meaning “to revolve or go around.” Other words for “wheel” are dialectal and again derivative, like Latin rota from a verbal root ret-, “to run.” A root wegh-, “to go, transport in a vehicle” (WAGON), is attested quite early, though not in Hittite. This evidence for the late appearance of the wheel agrees with archaeological findings that date the distri- bution of the wheel in Europe to the latter
261:ag-. To drive. 1. Latin agere, to do, act, drive, conduct, lead: ACT, AGENDUM, AGENT, AGILE, AGITATE; (ALLEGE), AMBAGE, AMBIGUOUS, (ASSAY), (CACHE), COAGULUM, COGENT, ESSAY, EXACT, (EXAMINE), (EXIGENT), FUMI- GATE, INTRANSIGENT, LEVIGATE, LITIGATE, NAVIGATE, OBJURGATE, PRODIGAL, RETROACTIVE, SQUAT, TRANS- act. 2. Greek agein, to drive, lead: -AGOGUE, AGONY; ANAGOGE, (ANTAGONIZE), CHORAGUS, DEMAGOGUE, EPACT, GLUCAGON, HYPNAGOGIC, MYSTAGOGUE, PEDA- GOGUE, PROTAGONIST, STRATAGEM, SYNAGOGUE. 3. Suf- fixed form *ag-to- in Celtic *amb(i)-ag-to-, “one sent around” (*ambi, around; see ambhi), in Latin ambactus, servant (> Medieval Latin ambactia, office): AMBASSA- DOR, EMBASSAGE, (EMBASSY). 4. Suffixed form *ag-men- in Latin agmen, a train, a moving forward, a marching column, group: AGMINATE. 5. Suffixed form *ag-ti-, “weighing” (Greek agein, “to lead,” has a sense “to weigh”), whence adjective *ag-ty-o-, “weighty,” in Greek axios, worth, worthy, of like value, weighing as much: AXIOM; AXIOLOGY, CHRONAXY. 6. Possibly suffixed form *ag-ro-, driving, pursuing, grabbing, in Greek agra, a seizing: PELLAGRA, PODAGRA. Derivative agro-. [Pok. ag- 4]
772:nau-2, Boat. Contracted from *naau-. 1. Latin ndvis, ship: NACELLE, NAVAL, NAVICULAR, NAVIGATE, NAVY. 2. Greek naus, ship, and nautés, sailor: NAUSEA, NAUTI- CAL, NAUTILUS, (NOISE); AERONAUT, AQUANAUT, ARGO- NAUT, ASTRONAUT, COSMONAUT. [Pok. 1. ndu- 755.]
787:animal: NEAT2; b. compound form *ga-nauta- (*ga-, with, together; see kom), “he with whom one shares possessions,” companion, fellow, in (i) Middle Dutch ghenét, noot, fellow: MATELOTE (ii) Old High German ginéz, companion, in German Eidgenosse, confederate: HuGuEnot. [Pok. neu-d- 768.] newn. Nine. 1. Germanic *niwun, with variant *nigun, in Old English nigon, nine: NINE, NINETEEN, NINETY, NINTH. 2. Latin novem, nine (< *noven, with m for n by analogy with the m of septem, seven, and decem, ten): NOVEMBER, NOVENA; NONAGENARIAN. 3. Ordinal form *neweno- in Latin nénus, ninth: NONA-, NONES, NOON; (NONAGON), (NONANOIC ACID). 4. Prothetic forms *enewn, *enwn in Greek ennea, nine (> *ennewa, *enwa-): ENNEAD. [Pok. e-neuen 318.] newo-. New. Related to nu-. 1. Suffixed form *new-yo- in Germanic *neuja- in: a. Old English néowe, niwe, new: NEw; b. Old Norse njyr, new: SPAN-NEW. 2. Basic form *newo- in Greek newos, neos, new: NEO-, NEON, NEOTER- IC; MISONEISM. 3. Suffixed form “new-aro- in Greek nearos, young, fresh, contracted into néros, fresh (used of fish and of water), hence néron, water: ANEROID. 4. Basic form *newo- in Latin novus, new: NOVA, NOVATION, NOVEL!, NOVEL?, (NOVELTY), NOVICE; INNOVATE, REN- OVATE. 5. Suffixed form *new-er-ko- in Latin noverca, stepmother (< “she who is new”): NOVERCAL. [Pok. neuos 709.] ni. Down. 1. Suffixed form *ni-t- in Germanic *nith- in Old English nithan, neothan, below: BENEATH, UNDER- NEATH. 2. Suffixed (comparative) form *ni-tero-, lower, in Germanic *nitheraz in Old English nither, lower: NETHER. See compound root nizdo-. [In Pok. 1. en 311.] [niké. Victory. Greek noun of unknown origin. NIKE.] nizdo-. Bird’s nest. Compound root formed from ni + *sd-, zd-, zero-grade form of sed-; literally, “place where the bird sits down.” 1. Germanic *nist- in: a. Old English nest, nest: NEST; b. Germanic ‘*nistilon in Old English nestlian, to make a nest: NESTLE. 2. Latin nidus, nest: NICHE, NIDE, NIDUS; EYAS, NIDIFY. [In Pok. sed- 887.] nobh-. Also ombh-. Navel; later also “central knob,” boss of a shield, hub of a wheel. 1. Germanic *nabo in: a. Old English nafu, nafa, hub of a wheel: NAVE?; b. compound *nabé-gaizaz, tool for piercing wheel hubs (*gaizaz, spear, piercing tool; see ghaiso-), in Old Eng- lish nafogar, auger: AUGER. 2. Variant form *ombh- in Latin umbé, boss of a shield: uMBO. 3. Suffixed form *nobh-alo- in Germanic *nabalé in Old English nafela, navel: NAVEL. 4. Suffixed variant form *ombh-alo- in: a. Latin umbilicus, navel: UMBILICUS; NOMBRIL; b. Greek omphalos, navel: OMPHALOS. [Pok. 1. (enebh-) 314.] nogh-. Also enogh-, ongh-. Nail, claw. 1. Suffixed (diminutive) form *nogh-ela- in Germanic *nagla- in Old English negl, nail: NAIL. 2. Form *onogh- in Greek onux (stem onukh-), nail: ONYX; PARONYCHIA, PERIONYCHIUM, SARDONYX. 3. Variant form *ongh- in Latin unguis, nail, claw, hoof, with diminutive ungula, hoof, claw, talon (< ongh-eld-): UNGUIS. [Pok. onogh- 780.] nogv-. Naked. 1. Suffixed forms *nog’-eto-, *nog’-oto- in Germanic *nakweda-, *nakwada- in Old English nacod, naked: NAKED. 2. Suffixed form *nog~-edo- in Latin niidus, naked: NUDE, NUDI-; DENUDE. 3. Suffixed form *nog’-mo- differentiated or developed into Greek gum- nos, naked: GYMNASIUM, GYMNAST; GYMNOSOPHIST, GYMNOSPER\M. [Pok. nog¥- 769.] no-men-. Name. Earlier form *()noo-mn, zero-grade form *(g)na-men-. 1.Germanic *nam6n- in Old English nama, name: NAME. 2. Latin némen, name, reputation: NOMINAL, NOMINATE, NOUN; AGNOMEN, COGNOMEN, DENOMINATE, IGNOMINY, MISNOMER, NOMENCLATOR, NUNCUPATIVE, PRAENOMEN, (PRONOUN), RENOWN. 3. Greek onoma, onuma, name: ONOMASTIC, -ONYM, -ONYMY; ANONYMOUS, ANTONOMASIA, EPONYM, (EPON- YMOUS), EUONYMUS, HETERONYMOUS, HOMONYMOUS,
1142:HELMINTH; ANTHELMINTIC, PLATYHELMINTH. [Pok. 7. uel- 1140.] wel-‘, To tear, pull. 1. Suffixed form *wel-do- in Latin vellere, to tear, pull: AVULSE, CONVULSE, DIVULSION, EVULSION, REVULSION, SVELTE. 2. Suffixed form *wel-no- in Latin vullis, shaggy hair, wool: VELOURS, VELVET, VILLUS [Pok. 8. wel- 1144.] wele-'. Wool. Probably related to wel-‘. 1. Suffixed extended zero-grade form “*wi-nd- in: a. Germanic *wullé in Old English wul(l), wool: woot; b. Italic *wland in Latin lana (> French laine), wool, and its derivative laénig6, down: LANATE; DELAINE, LANIFER- OUS, LANOLIN, LANUGO; ¢. Celtic *wland in Welsh gwlan, wool (> Middle English flannel, woolen cloth): FLANNEL. 2. Possible suffixed o-grade form *wol(o)-no- in Greek oulos, wooly, curly: ULoTRICHOUs. [Pok. 4. uel- 1139.] wela-2. To strike, wound. 1. Suffixed o-grade form *wol()-o- in Germanic *walaz in Old Norse valr, the slain in battle in: a. Old Norse Valhdéll, Valhalla: VAL- HALLA; b. Old Norse Valkyrja, “chooser of the slain,” name of one of the twelve war goddesses (-kyrja, chooser; see geus-): VALKYRIE. 2. Suffixed basic form *welo-nes- in Latin vudnus (stem vulner-), a wound: VULNERABLE. [In Pok. 8. wel- 1144.] welg-. Wet. Germanic *welk- in: a. Old English wolc(e)n, cloud, sky: WELKIN; b. Middle English welken, to wilt: wILT!. [Pok. 2. welk-, uelg-, 1145.] welt-. Woods; wild. 1. Suffixed form *wolt-u- in Germanic *walthuz in: a. Old English weald, wald, a forest: WEALD, WOLD!; b. Old Norse vdllr, field: VOLE!. 2. Ger- manic *walthdn- in Middle English welde, a plant yield- ing a yellow dye, weld: WELD2. 3. Germanic *wilthigaz in: a. Old English wilde, wild: wip; b. Old English wildéor, wilddéor, wild beast (déor, animal; see dheu-'): WILDERNESS; C. Dutch wild, wild: WILDEBEEST. [In Pok. 4. uel- 1139.] weme-. To vomit. 1. Germanic *wam- in Old Norse vamla, qualm, and Danish vamle, to become sick, prob- ably akin to the Scandinavian source of Middle English wam(ejlen, to feel nausea, stagger: WAMBLE. 2. Latin vomere, to vomit: NUX VOMICA, VOMIT. 3. Greek emein, to vomit: EMESIS, EMETIC. [Pok. wem- 1146.] wen-', To desire, strive for. 1. Suffixed form *wen-w- in Germanic *winn(w)an, to seek to gain, in Old English winnan, to win: WIN}. 2. Suffixed zero-grade form *wn-ydé in Germanic *wunjé in Old English wynn, wen, pleasure, joy: WEN2, WINSOME. 3. Suffixed (stative) zero-grade form *wn-é-, to be contented, in Germanic *wunén in Old English wunian, to become accustomed to, dwell: won!, (wont). 4. Suffixed (causative) o-grade form *won-eyo- in Germanic *wanjan in Old English wenian, to accustom, train, wean: WEAN}. 5. Germanic *wéniz, hope, with denominative *wénjan, to hope, in Old English wénan, to expect, imagine, think: WEEN. 6. Suffixed zero-grade form *wn-sko- in Germanic *wunsk- in Old English wyscan, to desire, wish: WISH. 7. O-grade *won- perhaps in Germanic *wani- in: a. Old Norse Vanir, the Vanir: VANIR; b. Old Norse vana- in Vanadis, name of the goddess Freya: VANADIUM 8. Suf- fixed form *wen-es- in: a. Latin venus, love (> venerari, to worship): VENERATE, VENEREAL, VENERY!, VENUS; b. suffixed form *wen-es-no- in Latin venénum, love potion, poison: VENOM. 9. Suffixed form *wen-eto-, “be- loved,” possibly in Germanic *Weneda-, a Slavic people, in Old High German Winida, the Wends: WEND. 10, Suffixed form “wen-yd@ in Latin venia, favor, forgive- ness: VENIAL. 11. Lengthened-grade form *wén-d- in Latin véndri, to hunt: VENATIC, VENERY2, VENISON. 12. Suffixed basic form *wen-o- in Sanskrit vanam, forest: WANDEROO. 13. Possibly zero-grade suffixed form *wn-ig- in Sanskrit vanik, vdnijah, merchant (? < “seek- ing to gain”): BANIAN. [Pok. 1. ven- 1146.] wen-2. To beat, wound. 1. Suffixed zero-grade form
1902:NATAL gene- NATANT sna- NATATION sna- NATATORIAL sna- NATATORIUM sna- NATES not- NATHELEsS to- NATION gene- NATIVE gene- NATURE gene- NAUGHT ne, wektl- NAUGHTY ne NAUSEA nau-2 NAUTCH ner-2 NAUTICAL nau-2 NAUTILUS nau-2 NAVAL nau-2 NAVE? nobh- NAVEL nobh-, nau-2 NAVIGATE ag-, nau-2 NAVY nau-2
=== AHD na- help ===
```


## [2026-09-07T17:37:07.669Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\necho \"=== WLD Bd2 315 area ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=316 && NR<=321' WLD_Bd2_pages.txt | grep -n \"nau\\|nā-\\|315\\|316\" | head -40"
}
```


### [2026-09-07T17:37:09.464Z] TOOL RESULT

```
=== WLD Bd2 315 area ===
4:mumble    j.niurmein, knaupeln'', engl. mtmp, norw. mumpa ds. (Ficklll^
42:hochd.) 7naticlie „Auswuchs, FuBgeschwulst der Pferde“, schweiz. 7nauch
291:(ursprgl. kons. St, vgl. acc.              navem = a\. ndvam, gr. vrja);             air.    nau (g. noe,
295:,,nauclerus'‘         (aber    mhd.    naive, ncexce       „kleines SchifP',       nhd. mdartl. Isaxie
302:   Meringers IF. 17, 149 Wzetymologie, wornach idg. nau-s vom Aushohlen,
303:Auskratzen des Einbaums benannt \uid mit got. b-nauan, aisl. b-nUa, aisl.
312:naU' nau- nu- A. „Tod, Leiche'', B.
334:            in got. natips ,,]Siot, Zwang, Gewalt’^, aisl. naud, naudr f. ,,Z\vang,
```


## [2026-09-07T17:37:16.099Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nawk 'BEGIN{RS=\"\\f\"} NR==319' WLD_Bd2_pages.txt | sed -n '270,320p'\necho \"=== search na- helfen ===\"\ngrep -n \"helfen\\|nfitzen\\|nützen\" WLD_Bd2_pages.txt | sed -n '1,5p'\ngrep -n \"na-tha\\|nathate\\|ovtvruii\\|OVIVT\" WLD_Bd2_pages.txt | head"
}
```


### [2026-09-07T17:37:17.470Z] TOOL RESULT

```
=== search na- helfen ===
14837:magh- magh- „k6nnen, vermogen, helfen“.
14853:   abg. mogq^ most! „konnen, vermogen'', pomosti, iter, pomagati „helfen“
14873:pamagoti „helfen", magoti „nutzen, taugen" (aus dem Slav.).
20799:na-     .,helfen. nutzen'\
20885:ar. nadh-, s. u. na~ „helfen“), aber auch abg. niizda „Zwang, Kot“, nuditi
```


## [2026-09-07T17:37:20.812Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nsed -n '20790,20830p' WLD_Bd2_pages.txt\necho \"=== which page ===\"\nawk 'NR<=20799 && /\\[pdf page/ {p=$0} END{}' WLD_Bd2_pages.txt\ngrep -n \"\\[pdf page\" WLD_Bd2_pages.txt | awk -F: '$1<20799' | tail -2\necho \"=== naus page ===\"\ngrep -n \"\\[pdf page\" WLD_Bd2_pages.txt | awk -F: '$1<20880' | tail -2\nsed -n '20840,20880p' WLD_Bd2_pages.txt"
}
```


### [2026-09-07T17:37:22.116Z] TOOL RESULT

```
BB. 24, llSf., hes. 121.

mlondo- „seimig, nicht wasserig“.
   Ai. mandd- m. n. {*mranda-) ,,die schmackhafte obere Schicht bei fliissigen
Speisen und Getranken, Bahm, Schleim“: lit. Uandiis „bindig, gehaltv'oll,
nicht wasserig'-. Zupitza BB. 25, 100, Prellvitz BB. 25, 283. Andere Deu-
tungen von manda- bei Uhlenbeck Ai. Wb. 211; Zugehorigkeit zu meld-
„'weich“ als Kasalinfixbildung (s. mel- „zerreiben‘-) ware fiirs ai. und lit.
Wort immerhin seitens der Bed. nicht ganz ausgeschlossen.
na-     .,helfen. nutzen'\

   Gr.                      -vdjuev „niitzen“, fut. ovi^-oco usw., oveiag, recte oyf]ag .,Yor-
teil, Nutzen“ (o-Praefix), ai. nd-tha- n.          m. „SchutzeP^     Wacker-
nagel Dehnungsgesetz 50, Solmsen KZ. 32, 288 f., Brugmann IF. 29, 411                                         ;



35, 94 f.
   Ai. natliitd- „bedrangt“, ndihate         scheinen nach Wackernagel Ai.
Gr. I 123 erst durch volksetyraol. EinfluB von ndtha- „Hilfe“ aus nadliitd-
,.bedrangt“, gleichsam „hiifsbedurftig“, nadhamana- „flehend'' (av, naidyah-
,,der Schwachere, unterliegend^^) umgestaltet zu sein;     dieses ai. nadh{iy
(das also dann nichts mit idg. net- „sich neigen, stutzen“ zu tun hat), viel-
leicht Praefix idg. no (s. an- „hinan“)     dha- „setzen'^ als          (nicht
nach Bartholomae Wb. 1061 f. zu si. nqzda „Not“, woriiber s. u. ^naii-
..Tod” ndtha- nicht zu m-td- „gefuhrt'‘ (wie qa-tha - qi-ta- ..gesungen^)      :



nach Schulze KZ. 27, 427 (zw.).

iiau-    f.    „Schiff''.

   Ai.        nail-    (nom. nduli)Boot“ (navya- „schiffbar“; ap. naviya
                                         „Schiff,
                                                   m. „Schiffer', av. navuza-
„Flotte*\ gr. vqiog ,,zuni Schiff gehorig'*' ; ncivaja-
ds.     —
        zum d s. Bartholomae Airan Wb. 1047                          —
                                                      gr. vav-fjyog ds., vgl.
                                                                         :
=== which page ===
=== naus page ===
,,nauclerus'‘         (aber    mhd.    naive, ncexce       „kleines SchifP',       nhd. mdartl. Isaxie
aus     dem Lat.; iiber dt. Nachen usw. s. u. nog'^o- „Baum“),                         in    Anwendung
auf              gehohlte Troge norw. no „Trog aus einem ausgehohlten
        scliiffsartig
Baumstamm“, nola iynoivilon-) „groBer Trog, schweres Boot“, mhd. nnoscJi
m. ..Trog, Rinne*', mnd. noste „Yiehtrog, Wassertrog“.
   Z. B. Curtius 313, Pick I^ 94, 499, II ^ 189, III^ 288 f.
   Meringers IF. 17, 149 Wzetymologie, wornach idg. nau-s vom Aushohlen,
Auskratzen des Einbaums benannt \uid mit got. b-nauan, aisl. b-nUa, aisl.
nua, ahd. nmn „zerreiben^‘ verwandt sei, erweckt bei der bisherigen Iso-
liertheit dieser germ. Sippe wenig Yertrauen; auf die lat. Glossen navia
..lignum cavatum“, navat ,,frangat', ymvo „re8cindo'‘ (F^-y KZ. 42, 86;
gegen seine Deutung auch von gr. anova^e als „caedendo                                              fecit“   s.

Kretschmer Gl. 2, 353) ist nicht zu bauen, s. C. Gl. L. YI 729 f.
   Wa d e1      ,   Etymologisches Worterbuch.   II.                                           21
naU' nau- nu- A. „Tod, Leiche'', B.
       :           :                                          „bis zur    Erschopfung abqualen;    er-
     mattet zusammensinken^'. Aus letzterer Bed. kann auch die Bed. A.
     Jebloser Korper'^ verstanden werden; Trennung beider Gruppen ist
       wegen der bait.- slay. Reihen kaum wahrscheinlich. Beide vereinigt
     bei Kretschmer   KZ. 31, 385 (wo iiber den schweren Wzvokalismus),
       Grienberger Unt. 164, Trautmann Apr. 382.
   A. got. nans „Leiche“ {gannivislron „begraben'‘), aisl. nar „Leiche“, ags.
neo- in   Zs., wie neo-fagol (wegen der folgenden bsl. AYorte nicht besser

als '^noJc-tii-5 zn'^net:- „umkommen‘') abg. navb ,,Leiche'' ac. 72dv,
                                                          ;                m.
„Grab, Jenseits, Holle“,                  lett.ndwe .,Tod'', ndtvei „toten, abtoten“, ndiviies
„sich miihen,           die letzten          Krafte anwenden (B); sich toten“; apr. noivis
„Rumpf, der tote Leib'* (Zupitza Gutt. 76, Berneker Pr. Spr. 310, Traut-
mann Apr. 386).
  B.       lett.   ndwifes     (s. o.),     lit.   ndvyti „qualen; verderben, bedriicken" (auch
„toten“,       iszndvyti              yertilgen''; altere Belege bei Trautmann
                               „vernichten,
Apr. 382); aksl. cech. naviti „ermudem’, cech. unava „Ermudung% russ.
mdartl. orzam „Mudigkeit“ schwundstufig aksl,            „schlaff sein, erschlaffen^,
cech. nyti „schmachten‘( russ. mjth „schwermutig sein, wehtun“.
            in got. natips ,,]Siot, Zwang, Gewalt’^, aisl. naud, naudr f. ,,Z\vang,
Drangsal, Sklaverei, Notwendigkeit^, as. 7i6d, ahd. not „Bedrangnis, Drang-
sal, Kot*', ags. ncad nled ,,Kotwendigkeit, Pflicht, Drangsal“; apr. nant'm
```


## [2026-09-07T17:37:33.226Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nawk 'NR<=20799 && /\\[pdf page/ {n=NR; l=$0} END{print n\": \"l}' WLD_Bd2_pages.txt\nawk 'NR<=20860 && /\\[pdf page/ {n=NR; l=$0} END{print n\": \"l}' WLD_Bd2_pages.txt\necho \"=== KNT naviya ===\"\ncd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"naviya\\|nāviya\\|nauya\" KNT.txt | head -20\necho \"=== KNT nāv ===\"\ngrep -n -i \"fleet\" KNT.txt | head -10"
}
```


### [2026-09-07T17:37:34.471Z] TOOL RESULT

```
: 
: 
=== KNT naviya ===
2718:G. Alone, to express cause: DB 1.86 2015 naviya dha ‘on account of the waters there was navig- ability’; DSe 46f didà ha[natüyà avagmat|é ‘wall fallen down from lapse of time’ (both examples doubtful, see Lex. a.vv.).
=== KNT nāv ===
```


## [2026-09-07T17:37:37.733Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"naviya\\|nāviyā\\|navigab\" KNT.txt | head -20\necho \"=== nearby lexicon ===\"\ngrep -n \"^nav\\|nav-\\| nav \" KNT.txt | head -20"
}
```


### [2026-09-07T17:37:37.789Z] TOOL RESULT

```
1794:V. Corresponding feminine forms as abstracts, which may become concretes: yauv-iyd ‘course, canal’; nàv-iyü navigability; perhaps patš-iy�� ‘writing, document’.
2718:G. Alone, to express cause: DB 1.86 2015 naviya dha ‘on account of the waters there was navig- ability’; DSe 46f didà ha[natüyà avagmat|é ‘wall fallen down from lapse of time’ (both examples doubtful, see Lex. a.vv.).
3535:84 birum : asiyavam : abiy : avam : Naditabairam : hya : Nabuk'dracara : agaubatà 85 : kara : пуа : Naditabairahya : Tigrám : adàraya : avada : aistatà : uta : i abiš : nāviyā : dha : pasiva : adam : küram : maškāuvā : avakanum : aniyam : usa : 87 bürim : akunavam : aniyahyà : asam : frinayam : Auramazdàmaiy : upastim 88 : abara : vaSnà : Auramazdaha : Tigrām : viyatarayama : avadà : avam : kàram : 80 tyam : Naditabairahyà : adam : ajanam : vasiy : ыз MR E rau
5604:naviyd- fem. adj. as sb., ‘navigability’, i.e. ‘impossibility of fording the river on foot’: Av. nàvaya- ‘navigable’, Skt. navyd-, adj. to nàv- ‘ship’ (§144.V). Hardly collective, ‘collection of ships, flotilla’, and certainly not lsf. to nav-, ‘on ship- board’; ef. König, RulD 70-1, and esp. Kent, JAOS 62.269-71 (with lit.), 63.67. ^ nàviyà nsf. DB 1.86.
=== nearby lexicon ===
578:varnavatim and other forms, = зле, Skt. 1у10-, AV. voronav-.
993:671. Tux PIE Shorr DrPHTHONGS 2$ AND au always develop like pIE ai and au, from which they can be distinguished only by etymological considerations; they originated only as zero- grades of long diphthongs. Similarly, pIE a be- came pAr. a before 7 or y of the next syllable. An almost certain example is seen in the present stem paya- (apayaiy ‘I protected’; рай-рауаша@ ‘do thou protect thyself’) as a variant of pà- (райм ‘may he protect’, etc.); since pã- seems to be the normal grade (on the testimony of Sanskrit also), then paya- must be for *po-ie-. Similarly, if the zšnau- of á-zínauliy ‘he satis- fies’ (cf. further zero-grade in zínufa 'satisfied") is an extension of root zínà- ‘learn’ (from *ĝnð-; see Lex. s.v. zénav-), 16 must stand for *gnau-.
1234:‘he satisfies’. See Lex. s.vv. zínav-, urfnav-. pIE *uek- ‘wish’ + suffix -no-, OP vašna- ‘favor’!
2534:With the vocalism of the present-tense stem: addriya, to dar-, pres. dāraya- ($215); and the uncertain [ар 0 уа] (see Lex. s.v. paté-). Formed on the present-tense stem: 3d pl. akunavaya"td, to kar-, pres. kunav-a- (§210.1); and the uncertain [айуа|вї]уа, for *atiyayastya ($215), to yam-, pres. yasa- (5212). Dubious forms on the sigmatic aorist stem, früsah[ya] to root sã- ($218.1), and on the per- fect stem, cazr|zyatd] or |clizr|iyatà], to kar-.
2544:navinaiy, 3d sg. kunavatazy. var-, pres. varnay(a)-: varnavátauy. xsnav-, pres. zinav(a)-: ü-z5navàhy. kan-, pres. kan(a)-: vi-kandhy (and -àh*-di$). jan-, pres. jan(a)-: perhaps (restored) 3d pl. vi-
2620:I. The participial suffix -lo- is accented, and the Ж verbal root is therefore regularly in the zero grade: $ thus para-ità, Skt. itd-, to ay- ‘go’; [phištā ni-pitta-, $ Skt. pistd-, to pai- ‘adorn’; sinuta- to zšnav-; a- $ тфай, Skt. kgala-, to zšan-; ava-jata, Skt. hatd-,to 4 jan-, karta-, Skt. kytd-, to kar-; u-barta- pard- 4 ратат, Skt. bhriá-, to bar-; maria-, Skt. mytd-, to Г | mar-; aría-, Skt. rtd-, to ar-; perhaps parta[m] to `
4913:(1) Prefix with verbs ay-, zšnav-, gam-, grab-, jan-, bar-, mà-, yam-; in verbal nouns dyadana-, dvahana-, and in the second parts of compounds Adiyabaukna-, Ariyáramna-, Bagabigna-, also in Akaufaciya-.
5158:^u- insep. prefix ‘good, well’ (uv- before vow- els): Av. hu-, Skt. su-, Gk. 0-уиѕ ‘having good life, healthy’, pIE *su- (§140.IV): in uxSnav-, ukàra-, ucüra-, Utüna-, ulava-, ubanwaniya-, ufrasta- ufrasta-, ubarta-, umartiya-, иғада-, uradana-, Uvaxstra-, &Uvürazmi-, warstika-, uvdsabdra-, waspa-, dinara-, uwkhamaranakara-.
5160:ucsnav- adj. ‘well satisfied’ ($142): from u- ‘good’ + zšnav- ‘satisfy’ (*wohlgeneigt", Hz. ApI 199-200; ихти ‘well-informed’, Sen 233). u[zina]us nsm. ($188.11, §190.1) DNb 27.
5332:тёпа- vb. "learn, come to know, know’: Av. xind-, Skt. jñā-, Gk. yeyrwoxw, Lt. gnóscó, NEng. know, pIE *gné- (806, $110, 8212). See also zínav-, dan-. | adünà imf. (NPers. dánàm, 568, $210) DB 1.51; DSq 3. x&ndsahy 2d sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 5110, $122) DB 1.52.
5333:azinav- vb. ‘hear, satisfy’ ($96): cf. Av. zšnav- ‘Genüge haben an’, adj. zínav- ‘Genüge leistend’, ріс. zšnůta-, sb. zínütay- ‘Zufriedenstellung’ (Bthl. AiW 557-60); apparently an extension of root zinà- ‘learn’ (cf. pIE *40- and *doy- ‘give’), with semantic development ‘learn, hear of, hear’, and ‘hear, hearken to, satisfy’ (Lg. 15.171; ef. also Bv. TPS 1945.47-50). Hz. ApI 238-40 gives an impossible equation with Skt. éru- ‘hear’ (pIE
5337:See also uzsnav-.
5338:z5nula- past pte. pass. ($71, 3242.1), cf. uzšnav-: zSnuta nsm. ‘satisfied’ DNb 26. |xsnutam) nsn. ‘heard’ DNb 53.
5339:à + zínav-: dxSnautiy (§71, $122, $208) ‘satisfy’ DNb 24. āzšnavāhy 2d sg. subj. (§227.1) ‘satisfy’ DNb 29f. äzšnudiy 2d sg. ішу. ($208, §237.1) ‘hear’ DNb 54.
5602:nàv- sb. ‘ship’: Skt. ndus, Gk. vais, Lt. nav-is, pIE *ndv- ($142). See also ndviyd-. [naval прі. (8183.1V) DZe 11 (supplied by Tm. Lex. 52).
5603:navama- adj. ‘ninth’: Ау. паота-, Skt. navamá-, pAr. navama- remade from pIE neyeno- after pAr. dasama- ‘tenth’ ($14911, $204IV), ef. Lt. nénus.  navama пзш. DB 1.10; DBa 10f.
5604:naviyd- fem. adj. as sb., ‘navigability’, i.e. ‘impossibility of fording the river on foot’: Av. nàvaya- ‘navigable’, Skt. navyd-, adj. to nàv- ‘ship’ (§144.V). Hardly collective, ‘collection of ships, flotilla’, and certainly not lsf. to nav-, ‘on ship- board’; ef. König, RulD 70-1, and esp. Kent, JAOS 62.269-71 (with lit.), 63.67. ^ nàviyà nsf. DB 1.86.
```


## [2026-09-07T17:37:39.969Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT search generic nav ===\"; grep -n \"navaya\\|navāza\\|navaza\\|nāuš\\|nau-\" BRT.txt | head -30\necho \"=== BRT nath ===\"; grep -n \"nāϑa\\|naϑa\\|panāϑa\\|paiti.nāϑa\" BRT.txt | head -20"
}
```


### [2026-09-07T17:37:40.063Z] TOOL RESULT

```
=== BRT search generic nav ===
5048:Schlacht  gehefert"  Bh.  j.3;  usw.  c)  be- gründend 'aus  den  angegebenen  Grün- den, folglich,  in  Folge  dessen'**:  paurvB yat  ditn  usca  usdvanayat  .  .  %raitaonö  .  . hS  °%a  vazata  %ri.ayar3m  ", .  der  schwebte in  Folge  dessen  .."  Ytj.öiC;  —  ai-a •  ].,  p.  ava'^a  Adv.  I)  'de,  ita';  1)  ver-  ait)m  nmä/am  baraytn  °%a  iriststn  hirt- gleichend  'so,  ebenso';  ein  Nebensatz  mit  zayin  "so  sollen  sie  die  Behausung  weg- y<^a  'wie'  geht  voraus  oder  folgt:  l_>'a;ia-  tragen  (und)  folglich  den  Toten  dalassen" sam  ..  ahaAya^  '^ä  *aiunavaya"i3  Bh.  V.  Ä  3;  a;  —  vTspe  fyrisfnti  pinnine 1. 8;  —  yd^a  .  .  hvanxhStm  .  .  fraca .  »&«  mOvayacit  .  .  tinsttUu  (sd.)  YL  14. aiti  ahvica  vazaite  ..  °^a  az»mHf  ..  a/a-.^Z.  4)  'desgleichen,  item';  pagtryäi säniYtio.iiS; — }ydh3 paruvamay  °%ä' mdarftayfn{sA)  af^nitäyukim  °>a  ätrpm Bh./,i4';  4.4,5.2;  —  \- iyam  yuviyS  {sA.)  V.J5.48;  —  mairyS  drva  bizangrB  "äa akäniy  *°^<J  *ya'iä  adam  niyastäyam  D.  ahmaoys  V. 5.35;  — JvS  nanm  ..  Jainli i-/.y,  — yimö  °'^a  kmnaot  yaia  dim  nsit  ''ha  m^nts  V.J. 37;  38;  —  ä'hrö *iiasaf  ahurö  V.  2.32;  i8.-t,t,  35,  38,  ir).  ahurake  . .  °^a  näirikayäi  V.  15.45  Gl.; 33.  a)  vorausweisend 'folgendennassen,  Vd.  2.  11) 'in  einem  solchen  Fall,  unter alio'-.lhauv  karahy3 'hä  adurußyt^  adam  solchen  Umständen':  yat  ..  spä  ahqm.- hardiyc^  amiy  Bh./.ii;  16,  2.3,  5,  ^.x'^}  baöhimtöS  vä  bavaf..°'ha  Al baeidz^m(sd.) 1.16,  2,14,^.5;  —  y-UOT  (sd.)  ..  aduru-  .'.  upi^isayffi  Y. IJ.35;  15.48.  in)'dort's'; jiya*  -hiJ  a%ah<^  adam..  amiy  Bh.  b— j';^,fs  'ha  dasiam..vlbarai  aHaisva  var>ßva 4.29;  —  '^äidiy  a>aAam  paraidiy  "so .  "wer  hat  dort  die  Rehgion  verbreitet..?" befahl  ich  ihm;  'Zieh  aus  . .'"  Bh.j.3;  V.  2.42;  39.  [Vytj^:  lies  'S«".] 9,  14,  2.6,  7,  10,  14;  —yadiy  '%a  *mam-  Ableit.  —  Eig.  'auf  jene  Weise'.  —  wo*s. yüAay  hacä  aniyanä  mä  tanam  D.5.3;Bh.  |  "^ä.  —  Pü.:  ää«,  (mV.  3.  42):  fiar^ 4-l'A — "''^  °^^  marthanS:  ..  Yt.lp.47;  — AS'':ba  vyaxmanyala:..  Yt/p.43-  a)  mit folgendem  _j'fläa  oder^ai  'insofern . .  als
10708:•  j.  xsao9ah-  n.  'Fluss,  Strömung,  Wasser- Schwall';  airy!>.layamm  .  ,  yahmya  äpu navaya  .  .  °taipha  %waxhnle  Yt  10. 14.
13151:ahmai  raes^a  x^annasca  .  .  dayata  (aP.) vatauhis  apö  tnavayala  zao%re  .  .  ahma- k?mca  mazdayamanqm  .  .  halqmcd  V.  GS, 1 1  f.  b)  II  im  Ap, :  aitJ"  adam  J'urt^-
21103:ai-^uV;;  S2J2.Ä  —  Vgl-  '>^:i'-  —  Pö.  (furj'-  a): cc  haiar»),  Npü.;  eirä  a,i;ar.  Sä,:  ya/B  yai/i. — O  Siels  mit  folgendem  n".  —  ')  So  auch  -  at statt  «m  t  -  Yt.  6. 3  lU  lesen?  —  3)  Unsicher; s.  aber  j'fl^J,  Sp.  1245  o. •  j.  ya'S'a,  j.,  g.,  p.  ya&ä  Adv.  imd  Konjn. Die  korrelativen  Demonstrativa  (Stverz.), die  im  Übergeordneten  Satz  erscheinen, ferner  °cit,  "fVj' (Stverz.  Sp.  590),  das  hinter y,  und  miinay)n  {ahe  oder  bä;  Stven. Sp.  1123  m.),  das  in  Verbindung  damit ■  id  durch  Sperrdruck  hervorge- hoben. I)  vergleichend;  I)  die  Aus- sage des  ^y'-Satzes  gilt  als  wirklich:  'wie, so  wie,  gerade  wie,  entsprechend  dem wie,  in  dem  Masse  wie;  als';  dabei  kann die  Aussage  im  y-  und  im  übergeordneten Satz  i)  verschieden,  2)  gleich  sein,  in welchem  Fall  das  Praedikat  meist  nur einmal  gesetzt  ist  a)  im  Ap.;  zu  i)  tyJ'säm adam  a'haham  ava''  *akunavayc^tä  y mäm  kSmJ'  skJ*  "was  .  .,  das  taten  sie, so  wie  es  mein  Wille  war"  D.  ff.4;  /?.  3; —  '^SsiJm  kacSm^  a'^oAyc^  ava'hä ^aiunavaya'tä  Bh.  7.  8;  —  y  mClm  kämi^ ava^a  dis  akunavam  Bh.  4. 4;  —  iyam yux'iya  (sd.)  akäniy  *ava%a  *y  adam niyastäyam  D.  //.  3;  —  adam  käram *gaiava  avastäyam  y'  paruvamciy  (nämt. ähefi)  ava%a  Bh,  i.  14;  l4^  zu  2): availäm  tiaiy  astiy  kariam  y  manä  (i^mL (tstiy  kartam)  Bh.<^.9.  b)  im  gAw.;  zu i):  kä  tsth'(sd.)  fyao'hanäi..y  *7'a  *haxmT \y :  dakyJusmaiy  duruvS  ahatty  Bh.  4-  \  (sd.)  Y. 34.  5 ;  —  a%S  nS  at?kat  y  hvö S-  a)  mit  OpL;  a)  die  Annahme  wird  wuja/  (sd.)  Y.2(j,4;  —  ydi  Jm  v!  nsit ab  künftig  möglich  hingestellt;  im  Nach-  i%3  mq'irfm  vartSintt  (sd.)  y  Tm  mSitiii^ä salz  steht  der  Opt.:  'oi  zT  ma  masyäka..  vaocacä  Y.i^5.3;  — yBt  it  a%ä  vtriwyqn yazayanta  .  .  fiä  s'usuyam  Yt  S,  1 1,  10.  y  Tl  (Sp,  367  0.)  aitl  Y.^ß.  6;  —  y  /a 55  (*'^0.  74i  —  •'^'  «f  >"S  ma^.lka  .  .  f  .  ,  mSngftScä  vaocascä  .  .  yä  vsha  ahs yazayanta  ..  api  niqm  ari.bint'ryqm  ..  tni  dadiWiahT '^.^g.^;  35.6;  —  *y  *aii aop  \t.8.2^.        b)  die  Aussage  geht  auf  I  (Sp.  9  u.)  i'kä  vansaia  yi  data  ofahsus
=== BRT nath ===
```


## [2026-09-07T17:37:50.633Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 250 (printed 229) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==251' HRN.txt | head -60"
}
```


## [2026-09-07T17:37:51.507Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 93 (printed 72) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==94' HRN.txt | head -70"
}
```


### [2026-09-07T17:37:51.886Z] TOOL RESULT

```
=== HRN leaf 250 (printed 229) ===
— 229 —
kurd. näw 'Nabel'; afy. nti^ nüm; oss. d. naffä;
bei. napag, nafag, n. nafay (259).
aw. naba[nazdista', ai. ndhhi- etc. gehen auf indog. bh
zurück, während die übrigen Formen auf ph weisen.
lOS^O'»'» nak Vermischt, nicht pur, verunreinigt*.
phlv. andk *böse', anokih^).
lC^t21. noffäh plötzlich, unerwartet*.
aw. *anäkasa' *improvisus* ; phlv. anakäslhd 'un-
vermutet', vergl. np. (igäh (No. 40).
näl 'Schilf* siehe nei (No. 1060).
1-022. näm 'Name' 2).
ap. nOtnan- 'Name* ; aw. nquian- ; phlv. mim, nCLmik
berühmt*, nämlnltan (PPGrl.); ai. wamaw- ; arm. anim
(H. No. 24).
LW. (?) kurd. näw 'Name' ; afy. nüm ; bei. nam
(181) ; oss. (echt) t. nom, d. non (198).
Rückert wollte ZDMG. 10, 219 auch neng 'Schimpf,
Schande', hierherziehen (als 'ein unregelmässig zu-
sammengezogenes Diminutiv von näm*).
1023. nän 'Brot'.
arm. nkan iyygvcplac *unter der Asche gebackenes
Brot'; vergl. chorasm. pekend (Vullers); hei. nagan,
n. nayan *Brot', nagan[pad *Bäcker* (249) ; minj. nayan;
phlv.-päz. nän (PPGl.).
Also zu l/^kan- + ^h ursprünglich '(unter die heisse
Asche) Vergrabenes* (zuerst de Lagarde)?
1024. näv Wasserkanal; Schiffchen', nävdän.
ap. näviyä' 'Flottille'; aw. navOza^ 'Schiffer* (Bar-
tholomae, ZDMG. 46, 294 Anm. 3), vergl. nävaya-
'fliessend'; phlv. nävfäk (aw. nävaya-), nävTcak (Bund.);
ai. näV' 'Schiff, Kahn, Nachen*, vergl. nävyä- *Strom*.
kurd. LW. nav; oss. LW. d. navä, t. nau- 'Schiff';
arm. nav 'Schiff*, navem 'schiffen* (H. No. 216).
naf 'Schilf*, vergl. tiäüej siehe unter nei (No. 1060).
*) Justi vergleicht ZDMG. 46, 282 arm. N. pr. Anak^ aber gegen
seine Lesung der betr. Gemme sprechen die voUständig deutlichen
Buchstaben auf dem Steine.
«j Vergl. Bartholomae, BB. XVII, 132.
```


### [2026-09-07T17:37:53.121Z] TOOL RESULT

```
=== HRN leaf 93 (printed 72) ===
72
kurd. plslk, pTsTk^ pTsT, pisile *Katze'; af/. />j^ö; bei.
[)üsi^ piinsJ, pisl (307) ; wa;^. pis, si;'n. pas.
Gewiss nicht zu ai. pncöha- ^Schwanz', wie Toma-
schek, Centralas. Stud. II, 762 will.
323. peSenjTden, pisenjidefi ^besprengt werden ^), j)^^^^j^
(Castle aus der jüd.-pers. ßibelübs.).
plilv. pas(i)nci:fan (vd. 5 (6) 61.; Bund.), vergl.
(is(i)ncitan (siehe ^Verlorenes Spraehgut', No. 33),
das im Commentar immer für aw. yhaec- (auch für
visrascayen vd. 7 (77)) steht.
Zusammenhang mit l/"Aa^c-, hincaiti, ai. l/'sec-,
sincdti ist unklar, aber doch wohl vorhanden.
324. pegäh *Frühlicht, früher Morgen .
aw. upa ~r (Jäh (s. No. 889).
325. pul^) 'Brücke.
gel. purd.
aw. peretU' 'Brücke', pesu- 'Furt' (d. i. peretü-, peäu-^
Bartholomae, Ar. Forsch. II, 35 folgg.); phlv.
puhrj puhl ^Brücke, Furt'.
kurd. per^ pir, pird, purd, pel (H.-Sch.); af/. LW.
pul.
326. peleng 'Leopard'^).
skr. p^däku' *Tiger, Panther' (ai. pfdaku-^ pfdäkü-
nur *Natter, Schlange').
kurd. LW. pilink; afy. prang,
327. penUh 'Zuflucht, Schutz', penahlden 'Schutz suchen'.
phlv. panäh,, panähih^ vergl. Mitr]panähak (AV.).
Doch wohl zu l/^pä- schützen'?
Bartholomae stützt diese Erklärung brieflich
*) Das Wort ist nicht allzu gut beglaubigt. Die anderen Wörter-
bücher belegen es gar nicht, nur der FR hat folgenden Vers Leblbl's
(Metr. Muteqärib) mit der Aussprache bis^ :
be^enjer heme tens^ enjlde end
ber an /äk^ /üues bisetijlde end
2j Nie pul gesprochen oder geschrieben (Vullers), das nur
•Geld' bedeutet.
^) Felis pardus L. (Blanford, S. 34).
```


## [2026-09-07T17:38:07.776Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB leaf 44 (printed 43) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==45' HUB.txt | head -60\necho \"=== HUB grep panah ===\"; grep -n \"panāh\\|penāh\\|panah\" HUB.txt | head -20"
}
```


### [2026-09-07T17:38:08.963Z] TOOL RESULT

```
=== HUB leaf 44 (printed 43) ===
— 34 —
Im Phi. ist apSdak oder apejak zu lesen, wenn die Schreib-
weise alt ist.
255. Np. beS *mehr als Comparativ zu has Viel' = ap. vasii/
musste auf ap. *vasyah- zuriickgehen. Dagegen spricht
np. mih gross : zd. masyah^, ^) hih klein : zd. kasyah-,
nach denen np. *bis fur ap, *vasyah- zu erwarten
ware. Jedenfalls setzt bal. gBs ein iran. *oais^ voraus,
auf das auch np. bes zuriickgehen muss.
256. Np. heSa *Wald* (= ap. *vaisa') kann ich mit zd. varesa-
{= np. *5a5 oder *bus) lautlich nicht vereinigen. Die
Entstehung von gr. ciXaog aus *fal}iaog (Bartholomae)
ist ganz unsicher.
257. Ich kann np. bel, bll *Spaten' (nach Vullers auch =
remus', nach Rosen, Np.Sprachf. p. 50 = *Schaufer),^)
belca *Hacke, Spaten nicht mit den Dialectformen bal
und berd vereinigen, mochte aber wegen der Laute auf
np. pill ^Briicke' = gel. ptird^ kurd. pird, purd^ pel
(Horn Nr. 325) verweisen. Ist berd die alteste Form,
so darf arm. bah *Hacke, Karst* (= *bhrtrom nach
Bartholomae) verglichen werden.
258. Np. him *Furcht' = skr. bhtma- 'furchtbar'.
259. Zu phi. vimdrimtan vgl. mein Zoroastrisches Lied
p. 62. Np. bt/mdr = paz. vlmdr geht nicht auf ap.
*v^mara'j das allerdings zu np. gumdr (oder btmar) ge-
worden ware, sondern auf ap. ^viinara- zuriick. Denn
m^ ist im Neup. zu 6^ (vgl. bist zwanzig' etc.)
geworden. Die Etymologic ist so wie so dunkel. Np.
tlmdr 'aegritudo, cura aegroti, custodia*, afgh. LW.
ttmOr care, attention, regimen of the sick, sickness ,
paz. tmar 'Sorge, Besorgnis' (Min. 25, 5, Shk. 269) hat
mit blmar nichts zu thun.
261. Dazu auch paz. vtni *nose, nostrils Shk. 273.
262. Lies *zehntausend' (statt 'tausend*).
*) Ap. *ma&iyah-^ vgl. siip.wa ^ts^a-.
2) Dazu afgh. LW. ra§'h^l *h61zerne Schaufel zum Worfeln' (afgh.
raSa *a heap of grain' = np. ras, raz *acervu8 frumenti excusbi*), jad.
tat. bil^ hel 'eiserne Schaufel' (Miller p. 58).
=== HUB grep panah ===
1447:327. Np. panah 'Zuflucht, Hulfe' = paz. panah Min.
1448:Gl. 154, Shk. 262, phi. panah Phi. Min. p. 15, 10,
1449:afgh. LW. panah gehort ohne Zweifel nicht zur Wrzl.
1452:panah aus *patnah {tn zu nn = w?) entstanden sein
1477:*) Vgl. auoh die Name n PanahmOy, Jazdpanah bei Hoffmann^
4307:LW. divirapati-), Mit -pet werden iibrigens (wie mit -pan^ -panah
4371:{Yazdpanah etc.) = zd. yazata-; np. yazdan 'Gott*, paz. yaz-
```


## [2026-09-07T17:38:09.415Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD nāw / panāh ===\"; grep -n -i \"nāw\\|panāh\\|nāwāz\\|nāwdān\" PHD.txt PHD_mackenzie.txt | head -30\necho \"=== NYB ===\"; grep -n -i \"panāh\\|nāw \" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T17:38:09.479Z] TOOL RESULT

```
=== PHD nāw / panāh ===
PHD.txt:540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
PHD.txt:585:šimšār Lë"! | N ~] box tree. Sir [HLBA < A hlb’; $1 | M šyyr, N ~] milk. šīrēn [5/yn! | M syryn, N ~in] sweet. ~ih: sweetness. SiSag [$y$k! | N fifa) bottle, flask. škaft [Ар] = Skeft. škāftan, škāf- [sk’p-tn' | M ‘kk’ pt, N fikáftan] split, burst. Skarag [skik! | P *škr-] (bird) of prey. škarwīdan, škarw- [fklw-ytn' | M ‘fkrw-st, N fikarfidan] stumble, stagger. škastan, Sken(n)- [TBLWN-tn' < A N tbr; škstn!, škyn- | M ‘tkn-, N stkastan, fikan-] break. ^ i$n: breaking. škēbāģ [fkyp?k! | P kyb-, N #hëba] patient. ~ih: patience. Skeft [škypt! | P “#kyft, N šigift] hard; extraordinary, astonishing; very. ~ih: hardness; hardship, distress; astonishment. šken(n)-, ~išn, v. škastan. ških- [fkyh- | N šikth-] be broken. Skóf-, у. Skuftan. Skdfag [fRwpk! | N šukēfa] flower, blossom. Skoft [škwpt'] = škeft. 1$kóh [ол | M Ай] poor. --īh: poverty. *§k6h [kwh | N sukdh] dignity, majesty; fear. škuftan, &ЕбЇ- [škwp-tn! | N fukuftan] flower, blossom. Énàs-, v. Snaxtan. šnàsag [fn'sk! | P *$n*sg] knowing, knower; sense. ~ih: knowledge. šnāxtan, $nàs- [fm htn!, fie | M хіп, Чи s-, N fin-] know, recog- nize. šnāyēnīdan, šnāyēn- [sz dyn-ytn'] please, propitiate. ~išn: happiness. šnāyīdan, šnāy- [fr'd-ytn!] praise, propitiate. --i$n : praise, gratitude. šnāz [frc | (N šinā(w))] swimming. šnāzīdan, šnāz- [fr'c-ytn! | M $2? 2-, (IN šināw-)] swim. $nóhr [snwhl | М *fnwhr] gratitude, contentment. šnūmaģ [fnwmk! | M *fnwm-] satisfaction, contentment. &nó&ag [šnwšk! | N šunoša] sneeze. $nüg [šnwk' | M *fnwg] knee. šnūman [fnwmn! = Av. xsniimaine] propitiation. 86n [swn'] kind, manner. ~ig [-yk!] customary, ordinary. šūy-, v. Sustan. Sdy [std | N ~] husband.
PHD.txt:680:žzēn [zyn! | N zin] saddle. zēn-abzār [zyn'pe!l | N zinafzár] horse-armour. zēnāwand [zy>zond] alert, vigilant. zēndān [zynd?n! | = M, N zindān] prison. «bān [-p?*x! | N -ban] jailer. ~ig [-yk! | N -i] prisoner. zënënidan, zënën- [zynyn-ytn!] look after, preserve. zēnhār [zyn)?] | N zinhàr] protection. zénig [zynyk!] armed. *zibāl [zb | N zībāl] swift (horse, etc.). zih [zyh | N zih] bow-string. zindag [zy(w)ndk! | M zyndg, N zinda] alive, living. ~th: life. zindakkar [zywndkkl | M zyndkr] vivifier, reviver. zinénidan, zinén- [zynyn-ytn'] damage, harm. zirak [zylk' | M zyr, N ~] wise, clever. zistan, v. ziwistan. zišt [zyst! | = P, N ~] hateful, ugly. ziwénidan, ziwén- [zywyn-ytn! | M zywyn-] vivify, revive. zi(wi)stan, zi(w)- [zyz-stn! | M zywystn, zyw-, N zistan] live. zi(w)išn [zywšn! | M zyysn] life; livelihood. ~ih: life, living. --6mand [-”xmnd] living, alive. ziyānaģ [zyd?nk'] young woman. zīyišn, v. zī(w)išn. zofāy [zwp'd | M zwp’y] deep; depth. *~ih: depth. ` zofr [zwpl | M zwwpr, J zwrf, (N žarf)) deep. —šy [2d] depth. ~-payag [-p'dyk'] deep. zóhr [zwhl | M zwhr] libation, offering. zor [z())wl | M zwr, N ~] power, strength. Bay ge J ~ig, ~dmand [-yk!, -wmnd | M -mnd, N —mand] powerful, strong. d z^ 201 [zwt! = Av. zaotar-] first officiating priest. ~ih: office of 201. Zraw-, v. zruftan. !zréh [zlyh | P zryh] sea, lake. *zréh [ziyh | N zirih] armour. zruftan, zraw- [zlwp-tn'] = azruftan. zūd [zwt! | M zwd, N ~] quick(ly). ^h : speed. zür [zwl | M z*wr] false, deceitful.
PHD.txt:763:alert gubrag, wigrād, zēnāwand.
PHD.txt:2926:noble abarmanig, āsnūd(ag), (āsnī- dag), āzād, āznāwar, ēr, pēšēnīg.
PHD.txt:3268:protection magind, pānāgīh, panāhīh, pasbanih, pušt, puštībānīh, sray- iin, zēnhār.
PHD.txt:4213:vigilant gubrag, zēnāwand.
PHD.txt:4718:[154] 1-2pešag 1 V. pēšpārag S eoo petyāragīh AS dax sa) petyārag ҳу 10 paydāgīh ^0 з» 10303 paydāgīh- = 95747 №0 paydagihistan 1152294 3” е 0 paydāgēn- = 527310500 paydāgēnīdan ММ 8” 5 05 paydag 15? ye» о) paygām -È ve os paygāmbar Sye Yeso petitigih A3 4) M 4290) petītīg 14) 95 1050) petit 12d уез 0› **pid we es panāh ^U? 103 panāhīh AY 10) "oul PITT puhlén- = "yes 10) puhlénidan ure rne 19у frāz erie pēhišn IMO” tay poxtan ure 125 nem! 519
PHD.txt:5104:zēnāwand ayy e$ zēnabzār ` Cer WS zēndānīg oro S zēndān wo pS zēndānbān i^o "GO u$ mër: 15 S. ` mee Ziwénidan zindagih A$ 43 HS zēnīg, zīndag yr
=== NYB ===
2277:ke [MNW] with encl. MNW-m = ké-m, MNW- = kē-š ete.; MNW-c = ké-c: A. interrog. pron. who? whom ?: én rētak kē hast? 161”; emphasized kē hàn he? who art thou, say? 561%; as cas. obl.: kē pat panāh kunom? 749; ke ax"eš hom? to whom do I belong? 624; én zanišn ké (ag.) kart? who made this deadly shot? 323; — gen. + ke: En pus + kē hast? whose son is this? 1621; or hàn 4 ke: ruvan... hàn t kē...? whose soul? 31?3; — governed by a prep.: hac ke? nazd ke? tài ke? ete. ; — indirect interrogation may be introduced by ku: gob ku to hac fradandän i ke hah 1517-18; without kū: (én-ic dine) hac pusa- ran...ı man ke zīvēt u kë mīrēt 219-19; nē (Gkah hom) i ke hàn 574. — B. rel. pron. who, which ; with pronominal antecedents : man ke, tē ke, šmāh ke, či ke, čišan ke, -$...ke, han (kas) ke, har (hàn) ke; hec (kas) ke both in a positive (6417-18) and a negative (11817-18) sense; 1. used as cas. rect. and cas. obl: (subj.) asvdr-é nest ke ... ētūn cigon to 1519-316; (dat.) (Kävul) ke Mihr u Mah pat pušt hah K. over which Sun and Moon keep guard 317%; (agens) Krisäsp ke Dahāk vanit K. by whom D. was vanquished 1064-5; — its syntactic function may be marked by an enclitic referring to the antecedent: (hu- nušk + Gana Menoi) kē-š ciš-ic pat poc nest (the progeny of the Evil Spirit) for whom there is nothing to furnish an ex- cuse 1021-?; but dastavar ké-§ guft ku there was a theologian who said 1018, also but ké-§ guft ki someone has said (taught) that 103? ; Gišān kē-šān Yam kirrenit those by whom Y. was cut to pieces 10145; — the gen. is regularly ex-
6076:pa'h: panāh
```


## [2026-09-07T17:38:19.292Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1440,1480p' HUB.txt\necho \"=== page tag: find leaf number ===\"\nawk 'NR<=1447{c+=gsub(/\\f/,\"\")} END{print \"formfeeds before:\", c}' HUB.txt"
}
```


### [2026-09-07T17:38:20.488Z] TOOL RESULT

```
324. Np. pciffdh *der fruhe Morgen, friih' (Fird. I, 456, 391
u. s. w.) kann weder =-- zd. *upakasa' noch = zd.
^paitikOsa- gesetzt werden, sondern wird am besten
mit N old eke als mp. Neubildung aus pa und gdh
*Zeit' (wie padrud^ padtd u. s. w. siehe Nr. 144) ge-
fasst, so dass es urspriinglich *bei Zeiten, zeitig
bedeutet.— 43 -
327. Np. panah 'Zuflucht, Hulfe' = paz. panah Min.
Gl. 154, Shk. 262, phi. panah Phi. Min. p. 15, 10,
afgh. LW. panah gehort ohne Zweifel nicht zur Wrzl.
pa *schiitzen'. ^) Ich mochte pa-nah teilen und nah =■
ap. *na&a' = skr. nathd- 'Zuflucht, Hiilfe' setzen. Ob
panah aus *patnah {tn zu nn = w?) entstanden sein
kann, bleibt zu untersuchen.
330. Der Bedeutung wegen nicht ganz sicher.
Hinter Nr. 333 ware nach Fr. Muller, WZKM. 6, 185 an-
zufiihren: pot a, pota scrotum' = lit. pautas^ das aber
zunachst *Ei* bedeutet (Fick, Wb.^ I, p. 84), was
von dem (unbelegten) pota nicht feststeht. Man sollte
zudem *poda erwarten. 1st das Wort iiberhaupt
persisch ?
336. 1st wegen der Bedeutung nicht sicher.
337. Np. puSa *crus sive hominis sive animalis (unbelegt)
kann, wenn aus podak entstanden, zu np. poyidan
laufen' gehoren. Vgl. nhd. Lauf , Lauft in waid-
mannischem Sinne. Zusammenhang niit pai iindet
nicht statt, vgl. Horn's Bemerkungen zu Nr. 282.
338. Zd. pqstO' in pqstdfra&ah- ist noch ganz unklar, aber
die Pehleviiibersetzung giebt es durch post wieder.
339. Der Etymologie wegen ist np. puk nicht zu verdach-
tigen. Vgl. afgh. pu, puk a puflf, a blast, the act of
blowing', pukai a puflf, inflating', pug 'the act of blowing,
a puflf*, pukql *to blow, to inflate, to breathe upon'. -
Lies (fvaaa.
340. Die beste Lesart im Armenischen ist polovat. Dies
sowie np. ptildd setzen ein phi. *pdlavat oder *pOlavat
(anstatt polofat oder polapat) voraus.
*) Vgl. auoh die Name n PanahmOy, Jazdpanah bei Hoffmann^
Ausziige p. 70 und 87. Aus dem von Fr. Muller mit Unrecht heran-
gezogenen phi. panak (= arm. -panak^ pStz. pana Shk. 262) konnte im
Neup. nur ^pana werden.— 44 —
=== page tag: find leaf number ===
formfeeds before: 53
```


## [2026-09-07T17:38:20.992Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD nāw ship ===\"; grep -o \"nāw[a-zāēīōūž-]*[^.]\\{0,80\\}\" PHD.txt | head -20\necho \"---\"; grep -n \"nāwāz\\|nāwig\\|nāw \" PHD_mackenzie.txt | head\necho \"=== NYB nāv ===\"; grep -n \"nāv\\|nāw\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-07T17:38:23.039Z] TOOL RESULT

```
=== PHD nāw ship ===
nāw-)] swim
nāwand [zy>zond] alert, vigilant
nāwand
nāwar, ēr, pēšēnīg
nāwand
nāwand ayy e$ zēnabzār ` Cer WS zēndānīg oro S zēndān wo pS zēndānbān i^o "GO u$ mër: 
---
=== NYB nāv ===
431:an-aryan [’n’ry’n] (Prth) non-Aryans HajA: 2. ŠPrth: 5.11, = Prs anörän. anäst ['n'st'] nothingness, that which is vain, worthless: dróv u ~ 83%. 8427. — Paz. anäst, Skr. v. nästikya (Mx), nästika (SGV); anahast ‘non existent’, Skr. v. asat, nāsti; anahasti ‘unreality, extinction’ (SGV, Aog.). From the neg. pref. and (v.s.v. anāvinast) + *hast; anāst < ana- hast with contraction seems to be the older form, anahast to be a recent for- mation.
4537:zēnāvandihā [zyn’wndyh?] vigilantly 6713. — From zēnāvand, Av. (1651) začnahvant- ‘vigilant’.
5469:zaēnahvant-: zēnāvan- dihā
```


## [2026-09-07T17:38:37.356Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nprint(json.dumps(d['BQT'], ensure_ascii=False, indent=1))\nprint(json.dumps(d['MON'], ensure_ascii=False, indent=1))\nprint(json.dumps(d['FSF'], ensure_ascii=False, indent=1))\n\""
}
```


### [2026-09-07T17:38:38.862Z] TOOL RESULT

```
{
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
{
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
{
 "title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/20220809_20220809_1444",
 "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"
 ],
 "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking",
 "covers_etymology": false,
 "notes": "Persian OCR fair (readable prose). Mostly glosses; some Pahlavi/Avestan notes. Edition may differ from the 1363 Donya print Nourai used."
}
```


## [2026-09-07T17:38:46.392Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\necho \"=== v4 pdf page 193 (printed 2110) ===\"; awk 'BEGIN{RS=\"\\f\"} /\\[pdf page 193\\]/' BQT_v4_pages.txt | head -60"
}
```


## [2026-09-07T17:38:47.397Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\necho \"=== v4 pdf page 195 (printed 2112) ===\"; awk 'BEGIN{RS=\"\\f\"} /\\[pdf page 195\\]/' BQT_v4_pages.txt | head -60"
}
```


### [2026-09-07T17:38:47.845Z] TOOL RESULT

```
=== v4 pdf page 193 (printed 2110) ===
[pdf page 193]
نانوخیه ۱۱
که نان‌پز باشد ۱ #۰ - وهرچیزدرازمیان خالی‌را هم کنته‌اند - وبمعنی
نانوخیه ؟ - بنتح خای نقطه دار | رخنه و سوراخ هم‌آمده است - وکشتی و جهاز
و تحتانی » بمعتی نانغواء است که زئیان باشد . | کوچك - وناودان ‎٩‏ بام خانه - و آنچه کندم
کر بر کزند کی عقرب بندند درد راساکن‌کند | بدان از دول بگلویآسیا ریزد ۷ - وچوب میان
کرم وخعك است در دویم وسیم . خالی کرده که در بعنی مواضع آب ازآن بچرخ
نان و نمکدان شکستن - کداب | آسیا خورد و بگروش آرد - و چویکی ۸ که در
از حرام خواری ‎)٩(‏ کردن باشد ۴ . مان پشت آدمی وکفل وسرین اسب فربه ودان
نانیوشان * - بکرناك با بای‌حطی م و خته خرما میباشد - و بمعنی خرام
ی با هم بنظر آمده‌است که رفتاری ازروی ناز باشدگ .

بر وزن وافروشان . بمعنی داگهان و بی خبر ی ۰ 2
و ناشنیده باشد ؛ و بفتح ثالك هم درست است. ناو! نیدن *۱-با بون بروزن‌آرامیدن,
فاق * - بروزن کاو, جوی آب راکوبند | بمعنی خمکردن و خم دادن و مانده کردانیدن

(۱) خم۱ : حرام خوری ‏

۹ ر3 : نانوا. ۴ < بانخواء (همم.) ۴ - «نان ونمکدان شکتن ۰
حرام نمکی کردن > « زشیدی > ۴ - رشیدی گوبد : « نانیوشان » ناشنیده و بی‌خبر >
عرچند لغة ترکیبی صحیح است از : نا( انفی . سلب )+ نیوشان ( صفت فاعلی از نیوشیدن ).
ولی‌شاهدی‌ندارد , ظ . مصحف «ناپیوسان» (ه.م.) * - پارسی باستان -82۷1918 (جهاز).
اوستا -88۷9228 ( کشتی ران ) , هندی باستان -82۷ ( کشتی» قایق کرجی ) » ارمنی 18۷
(کعشتی )۰ 88۷602 ( سفر دربا کردن ) « اسشق ۱*۲۶ » هوبشمان کوید : اوستا -18۷228

ارمتی ع 827 ( کنتی ران ) < -اسکریت -78۷2[4 *لانینی 82۷1818 2 ( در
‎ ) ۴‏ هویشمان ۰۱۶۲۶ استی 321 ( کشتی ) «ککه . است ۰۱۲۷ کردی 88۷
(زورق ) , 888 (قنات » ناودان ؛ راه آب ) « ژابا صس 4۱۷ ‎٩‏ - رك : ناودان .
۷ <ناوکه (هم.) :
در تحیر طفل میزد دست و پا آب می برش بناو آسیا .
عطار نیشابوری * رشیدی >.

۸ - چنین است در رشیدی بنقل ازسروری ! درفرهنگه نظام « ومثل جوبك یشت آدمی
بمنی کودیی که برقفرات پشت است, ومثل گودی میان دوکفل فربه اسب ...؟ وهمین صحیح‌است
(ر3 : مازن) ر3 : ناو4 . ‎٩‏ - رك4 : ناویدن . *- در رشیدی آمده است . از :
- تلو (هم.) ۳+ آنیدن (پسوند مصدر متمدی ) » متعدی « ناویدن » (ع.م.)

* نافوا - بسکون سوم *< نانبا « فولرس ]] ۶۱۲۸۹ » از : نان وا ( پسوند پا
قی *کردی 038 - 228 ( بان پزخانه ) « ژابا ی 2۱۹ > ؛ پزنده و فروشندة نان :

سوی نانوا شد سبك با عنان بدان شاخ زرین ازوخواست نان

بدو تانوا کفت کرا بها تدانم , نیارمش کردن رها . . .

فردوسی طوسی « شاهنامة بخ اج ٩ص‏ ۲۹۰۵ > ورك : فهرست ولف.
```


### [2026-09-07T17:38:49.116Z] TOOL RESULT

```
=== v4 pdf page 195 (printed 2112) ===
[pdf page 195]
طوه -۹۱۱۲-
وعبادت خالهٌ مجوی را کوبند ؛ ودراین زمان با | نالیدن وناله کردن هم‌هست *۱- وبمعنی‌خرامیدن
يك واو لوستد مانند طاوی وکاوی . ورفتلری بنازهم آمده است۸ - وخم شدن ومانده

ناوه ۱ - بر وزن ساره . چوب کوناه | کردیدن را نیز کفته‌اند ۸ .

میان خالی کرده راگویند که کل کاران بدا ن کل ناویژه ۱۱- بنتح زای فارسی بر وزن
کدند ۴ - وتبشی چوبینی که در آن خمید | آویزه » بممنی کلیف وداپاك وعیب دا وآمیخته
کنند ۴ - وآلتی که بدان کندم وجوازدول بسا و مففوش باشد -
ریزد ۴ - وچوب باآهن میان: خالی که تیر داوك ناه ۱۴ دزن ما اکود
را درآن نهاده اندازد ‎٩‏ - وچوبك ‎٩‏ مبان بت بروزن ماه » پوی تم را کوش
آدمی و دانکندم و خستةٌ خرما را نی زگوبی _ | یعتی بوبی که از زیر زمیتها و سردابها بر دماغ
و نام جایی ومقامی هم‌هست - وچاد رکهنه ی ۳ ناها ۴ شی گرسنه(۱)
گفته‌اند - و بدن مکتبی‌را نی ز گویند که قالب 7 **» بروزن‌باچار»یمعنی
روح باشد ۷ . باشد یمنی شغصی که از بامداد بازچیزی نخورده

ناو یدن ۸ - بروزن چاوبدن . بممنی باشد و معنی‌تر کیبی آن باآهاراست یعنی ناخوردء

پینکی باشد که مقدمةٌ خواب است ‎٩‏ - وبمعنی | چه‌آهار بمعنی خورشن باشد ۱۴.

() خم ۳:۱ ناشتا +

۱ از : ناو (ه.م.) ۰ (پسوند صفیر » نبت وغخباهت) * نا و که (ه.م.) و رك : ناو .
دراراك (سلطان] باد) 30۷810 (چوب کوناء میان خالی که کلکاران بدان کل کشند) «مکی نژاد» .
تهرانی 83۷8 ۰ بروجردی 207۷8 3 شپیدی *؛ معرب: اوق « قطرالمحیط > -

۴ در زمان ترك فلك بای نپد اند ر کل همچو هندو بکشد لاوه بر کیواش.

اين پمین فربومدی ۸« رشیدی > .
رك : سروری » رشیدی - ۴ اوه نا وکه (هم.)

* << باوکه (ه.م.) ‎٩‏ رد :جح ۸ صفحهٌ ۰۲۱۱۶

۷ - باین‌معنی ظ . برساختهٌ فرقةآذ رکیوان. ۸ از: ناو(ه.م.) + بدن ( پسوند
مصدری ) . لغة ماد ناو بچپ وراست متمایل شدن .

‎٩‏ - چومت هرطرفی‌می فتی ومی‌لاوی ‏ که شب گذشت کنون نوبت دعاست,مخسب.

‏۱ مولوی بلخی رومی « فرهنگه نظام > .
ورگ :ح ۸ + *- باین معنی شاهدی نیاورده‌اند. ۱ از : با( شفی , سب )+

‏ویژه (ه.م.) ؛ باین معنی در دساتیر استعمال شده است «* فرهنگه دساتیر ص ۲۹۹ *.

‏۴ تهرانی 84( بوی نم ). بروجردی 88 «شپیدی» ؛ درارا4 (سلطان؟ باد) 28 «مکی
نژاد» . ۴ از : دا( شی ,سب )۷ آهار (ه.م.) لفظاً بعشی بی خورش » بی آش
هرمزد نامه ی ۰۲۱۹۸

‏۴ اگر چند سیمرغ ناهار بود تن زال پیش اندرش خوار بود .

‏فردوسی طوسی * شاهنامةٌ بخ ج ٩ص‏ ۱۹۹۹ -

‏از پند حق و خوب سخن سیری وز بپر ژاژ و باطل » ناهاری.

‏« ناسر خسرو بلخی ص 4۳۸ -
اما «تاهار» ۳ تهار (در تداول ) که به غذای وسط روز اطلاق کنند. دراصل«ناهاری» (ه.م.)است .
```


## [2026-09-07T17:39:25.665Z] TOOL CALL #26: Bash

```json
{
 "command": "ls site/pages/346.jpg 2>/dev/null; pdftoppm -f 346 -l 346 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg346 && echo done && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


## [2026-09-07T17:39:26.011Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 panah ===\"; grep -n \"پناه\" BQT_v1_pages.txt | head -20"
}
```


### [2026-09-07T17:39:27.578Z] TOOL RESULT

```
site/pages/346.jpg
done
total 17800
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
-rw-rw-r-- 1 sfmqrb sfmqrb    76794 Sep  7 13:39 pg346.png
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


### [2026-09-07T17:39:27.621Z] TOOL RESULT

```
=== BQT v1 panah ===
242:که زرتشت بدربار شهریار آنجا گشتاسب پناه برد و دینش نخست در
13688:پناه ودبواری‌باشد که‌بواسطهُ کرفتن فلعموه‌حافظت
15096:در زبانهای اوستابی و پارسی باسنان بمعنی پناه و کومكك گرفته‌اند - دالا 121012 احتمال میدهد
25929:شتن مان ات که شت و پناه باشد وچوی ی که
26365:یعنی یناه ببر وپناه بخ
26390:پناهیده- بر وزن جفا پیشه ۰ بمه‌نی گرریدن هم هس .
```


## [2026-09-07T17:39:31.260Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=26365{c+=gsub(/\\f/,\"\")} END{print \"leaf(0-based)=\",c}' BQT_v1_pages.txt\nsed -n '26340,26400p' BQT_v1_pages.txt"
}
```


### [2026-09-07T17:39:32.527Z] TOOL RESULT

```
leaf(0-based)= 644
بالیدن است که بمهنی جستجو کردن و تفحص
نمودن باشدا .
پلینف‌ی ‏ بروزن فرزندی, نام نوعی از
خربزه باشد که عربان بعایخ گویند .
۳ بهلوی 1 (رله : پلکان). گیلکی
۴ رك : فیل.
٩‏ - رك : پالیدن.بیان هیجد هم (۱)
در بای فارسی با نون مشتمل بر شصت ودو لت و کنات
واعمالی که بجهت دفم چشم زخم کنند- وبمعنی
پوشیده و پنهان هم آعده است و بلغت زند
وپازند (۲) پارچه ای باشد چهار کوشه که در دو
کوشة آن دود دوژند ومتابعمان زردشت دروقت
خواندن زند و پازنه (۲) و اوستا آن را برروی
لین « بفتح اول وسکون ثانی» بمعنی اما
وبممنی لیکن باذد.
لنأث « بروزن سواد ؛ بمعنی هوا باشد
وزمن کرده است . خود ندند ۷ .
ودبیر و نوسنیه را گوبشد - وتار ابریشم را ثبز ورخت را گوشة .
گفته اند - و بضه مانندی باشد از رسمان
خش که دور دوك بچیده شود - و ماشوره را
نیز کوبند.
بنام بفتح أول بروزن کلام ۰ تعویذی
ناه ۴ - بفتح اول و الی بالف کشیده
و بهاء زده» بمعنی حمایت باشد- وسابة دیوار را
نیز پئاء گوبند - و امر بدیین ععنی هم هست
یعنی یناه ببر وپناه بخ
ناهد - باها ودالابجد بروزن‌صباحت.
0 در اوستا 8202 - ۳2101 , در هازی 0 , 024۳70201 و 27110 . در
کرد بان بشت مسمعنی جامه‌ای که درزیر زره دوشند» آمده؛ در لگ د4 وندید اد بند ٩‏
ینام جزواساحه ولوازم يك‌مرد جنگی بشمار آمده, بجزاین معانی دراوستا وپهاوی پنام عبارت‌است
از دو قطعه ارچ سفید از جنس پتبه که بروی دهان آویخته با دو نوار پیشت سر کره میززنشد .
زرنستیان ایران آن دا هروبند» لمتد. این برد؛ کوچك که بنا بتوضیحات ضیر پپلوی اوستا باید
دوبند انگشت پاین‌تر ازدهان باشد» دروقتی بکاربرده ممشودکه موبد درمقابل آتش مقدی » اوستا
سراید ومراسم دیتی بجاآورد . استعمال پنام برای آن‌است که نفی وبخار دهن‌بعتصر حقدی‌ترسد.
پنام‌از لوازم آ تربانان (موبدان) است. #يشت ۱ص ۷۹۳ و۲۹۵ ح و۳۵۵4
بتا ! نگارا ! ازچشم بدبترس همی چرا نداری پاخویشتن همی تو ینام ؛
ازین بیت پیداست که مراد همان روبند است نه‌تمویذ (مذ کور درعتن) وفرهنگه‌نویسان
مقر منة چشم بد چنن درك کرده‌اند 1 «کاتها ص۱۲ . زرانشت هرام در اردای وبراف نامه کوبد:
بشد برغخت زر اردای وبراف ۱ پنامی بررخ و کستی‌اش برناف .
۴ بهلوی 0۵0۵ [ ۳202۵10 یناهی. بناه بردن | از ۶02)8۵1 0808۵1 #از
2 * « تیب رکه ۱۱۹ بنقل‌از هوشمان» و رك: اسشق ۳۲۸-۳۲۷ .کردیدن. و ا زکسی بی‌موجب برربدن‌هم؛ 9
نبه کر دن هد کنابه از گررشتن -
و آریزایدن- وپرشان وپرا کنده ساختن‌ومتفرق
گردانیدن باشد - و کنایه از خاموش کردن -
و دقم و محو لمودن - و منکر شدن- و علجز
نعتی دنام هی آور ‌ ۱ ۰
بناهنده؟ بی وزن پرا کنده» بمعنی 1
پتاه گر نده باشد.
بناهیك » بررزن دوانید , یعنی یکی
یناه آورد +
پناهیده- بر وزن جفا پیشه ۰ بمه‌نی گرریدن هم هس .
داب زوا هکره پنبه کی - بنم کاف امر است ‏ یعنی
محو کن- ومنکرشو - و خاموش باشسوبگویز .
پنبه بز » بنتح اول و بای ابجد بروزن
کنده‌یز ۳ حلاج و تداف وشه ژترا گوینث.
پنبه در گوش کنابه ازمیدم‌غافل
وسخن لاشئو باشد .
بنبه در گوش نهادن. , پبه در
"وش افکندن ,پنبه در گوش گردت؛حر‌يك
ممتی دارد که کنابه از غفلت داشتن و سخن
ناشنوون باشد . ۱
```


## [2026-09-07T17:39:51.326Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSF ناوک ===\"; grep -n \"ناوك\\|ناوک\" FSF_pages.txt | head -20\necho \"=== FSF ناو ===\"; grep -n \"^ناو\\| ناو \" FSF_pages.txt | head -10"
}
```


### [2026-09-07T17:39:51.381Z] TOOL RESULT

```
=== FSF ناوک ===
16307:‫به‌صندوق بر ناوک انداز کرد‬
19343:                           ‫یخ‬‫ونلف‬                                 ‫بیامد یکی ناوکش برمیان‬
20003: ‫شده لعل و اهار داده به‌حون‬                      ‫دل ز ناوک چشمت گوش داشتم لیک‬
21197:‫دکرمان نهند و بیندازند و بدان‌سبب ناوک‬          ‫پدید آمد آوای دشمن ز دوست‬
21205:          ‫بکرهدار ناوک بج‬
=== FSF ناو ===
```


## [2026-09-07T17:39:52.397Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON part2 ناو ===\"; grep -n \"ناوانیدن\\|ناویدن\\|ناوه\\|ناودان\" MON_part2.txt | head -20\necho \"=== MON part1 پناه ===\"; grep -n \"پناه\" MON_part1.txt | head -10"
}
```


### [2026-09-07T17:39:52.466Z] TOOL RESULT

```
=== MON part2 ناو ===
2884:غناوه؛ (۵۱۵۷۸)۵ (.) (مس.) سازی است 
10015:مخارجه عمارت. ناودانی که بر کنارهای بام 
11521:است که با نیم‌شیار قحف طرف دیگر ناودان 
36026:کفی شتله» ( تفر ی ات درناوه مرده). 
53114:ناودانی است که آن جمع 
67846:آب. ناودان. 
70161:1( آب راهه» آب گذر. ناودان؛ ج. با فا 
73534:ناوانیدن: ۷۸ (مص م.) خم کردن» 
73548:ناودان: 2۰-۱ (امر.) جایی که در آن ناو 
73608:نسبت و شباهت - ناوه| ناوخرد. نوعی تیر 
73641:ناوه: (-)۱2۷-2 [- ناوک ] (.) ناو خرد. 
73656:ناویدن: ۱2-۲7 (مصل.) مانند ناو به 
73871:آب. قیف گونه‌ای که مانند ناودانی با جوبی 
74121:ناودان ننض و بر روی استخوان زند اعلی 
76346:انتهای مری موجود است و بنام ناودان مری 
78858:شراب نگاهدارند. ناودان. (ص.) حقیر» 
81143:نویدن: 2۷-1000 (- ناویدن] (مصل.) 
=== MON part1 پناه ===
7897:جمع کردن. در حرز کردن پناه دادن جای 
12013:بناه خواستن» پناه گرفتن» پناه بر دن. 
12056:در زدن» دست انداختن» تشبث کردن. پناه 
12490:پشت نهادن بسوی چیزی. پناه به کسی دادن. 
12491:پناه به کسی بردن. نسبت کردن بر» برداشتن 
12706:آمدن خواستن. پناه بردن به. (فق.) حالت 
16001:بردن» پناه جستن» بناهیدن. (.) بناه. 
16607:(.) زنهار)» پناه. 
17631:اند خسید ل؛ مدل[-عهلده (مسصم.) پناه 
17633:(مص‌ل.) پناه گر فتن.
```


## [2026-09-07T17:39:55.791Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '73500,73680p' MON_part2.txt"
}
```


### [2026-09-07T17:39:55.837Z] TOOL RESULT

```
نان‌ونمک: ۱۸۲۱-۰۵-۸ (امر .) نان بعلاوة 
نمکك. (مج.) طعام. (محج.) نعمت. نان و 
نمک کسی را خوردن: از سفره او خوردن. 
از نعمت او برخوردار شدن. خوردن با کسی: 
با او هم غذای شدن؛ هم نمکك شدن با 
و 

ناو: 2۷« (جهاز] (.) هر چیز دراز میان خالی. 


فر هنک فارسی معین 


۱۰۱ 
چوب کاواک که آب از آن به تنورة آسیا با 
از جابی به جایی دیگر رود. ممر آب که از 
سفال سازند و به یکدیگر وصل کنند که 
نت در آن جاری شود اودان. جوی آب؛ 
نهر. دره‌ای که رودی از میان آن بگذرد؛ 
وادی. رخنه» سوراخ. قابقی کو چکك که از 
درختی مبان کاواکك سازند. کشتی» سفینه. 
کشتی جنگی (فره.) آنچه گندم بدان از دول 
به گلوی آسیا ریزد. شیاری که در پشت 
انسان و کفل اسب است. او کفل: فاصله و 
شباری که میان دو کفل است. ناو گردن: 
فرورفتگی پشت گردن که به شکل او است. 
شیاری که در روی گندم و هسته خرما دیده 
شود. دیگ دیگ‌چه. تابه. (گیاء) نام دو 
گلب رگ تحتانی از ۵ گلب رگ جام گل گیاهان 
تبرةٌ پروانه‌واران که لبهٌ مجاور آنها سهم 
چسییده است. خرام از روی ناز. 

ناوارد: تست« آف. ع.] (ص.) غیر ماهر» 
تاش به کار ناشی. نامو جه» بیجا. 
ناوانیدن: ۷۸ (مص م.) خم کردن» 
خم دادن. مانده کر دن» خسته گردانبدن. 
ناوبان: 10-.0 (اهتبر.) کعتعی ناه ملاح. 
ستوان نیروی دریایی (فره.) 

ناوبر: ۱۲ [ - ناور نده| (ص‌فا.) کسی که 
کشتی را راه برد؛ رانندهٌ کشتی (فره.) 
ناوجه: (0-):6-.۱ (ا.مصف.) نام کوچک. 
ورن کتو هه (تظ کی کنو هن 
جنگی (فره.) (زرگری) قالبی آهنی که در 
آن شمش زر و سیم ریزند؛ مسبکه. 
ناوخدا: ۱-3 [- ناخدا| (ص‌مر. امر.) 
ملاح» کشتیبان. 

ناودان: 2۰-۱ (امر.) جایی که در آن ناو 
(ممر سفالین آب) گذارند (رشیدی). ممر 
آب (اطلاق محل به حال). ممر خروج آب 
پشت بام که از سفال یا آهن سفید سازند. 
جوی» نهر. مجرایی که گندم از دول به 


۱ 
گلوی آسیا رود. چوب دراز میان خالی که 
آب از آن به چرخ آسیا می‌ریزد و آن را به 
کُردش درمی آورد. 

ناودیس: ۱.5 (ص‌مر.) به شکل ناو 
(کشستی)؛ م‌انند نساو. (امسر.) (زم.) 
چین خوردگی بزرگک و منحنی مقعر طبقات 
0 

ناورد: 0 (- نورد - سرد نسرد»ه 
جنگ مارزه. رزمگاه؛ ممدان جنگ. 
رفتار» حرکت. قدرت» حرکت. گرد گشتن 
اسب چون دايره. جولان. 
ناوردجو(ی): ()11[-.۱ [- ناور دجو بنده ] 
(ص‌فا.) مىارزه» جنگجوی)؛ ناور دخواه. 
ناوردگاه: ۰-0 (امر.) مبدان جنگ 
رز فگاه: جولانگاه. 

ناوسار: ۰5۷-۰2 (.) دی رک آسیا که با 
چرخاب می‌گردد. مجرایی که باغستان را 
بدان آبباری کنند. ناوسان. 
ناوسارزی: 1.21 (امسر.) نوروز 
خوارزمیان. 

تا یبا لا و ۱-۲ (امر.) (نظ.) فرمانده 
ناو» فرمانده کشتی جنگی. 

ناوشکن: «مع2.: [- ناوشکننده] (ص‌فا. 
|.) (نظ.) کشتی کوچک بسیار تندرو که 
مأمور دنبال کر دن اژدرافکن‌ها است و خود 
11 نیز آبزارهایی برای افکندن اژدر دارد 
(فره.) 

ناوقه: (۵-) ۱8۷۵ (۱.) مقباس آب در قدیم؛ 
آن مقدار آب که شخصی در میان آب رود 
و به مقدار یک گز میان هر دو پای بگشاید 
و آب به زیر هر دو زانوی او برسد» آن 
مقدار آب را ناوقه گویند و گویند که ناوقه 
عبارت از آن است که مردی در میان ات 
رود و هر دو زانو بر زمین نهد و به مقدار 
یکك گز مبان آن کشاده داردو هر دو الیه 
خود از زمین بردارد و آن مقدار که از آن 


فرهنکگ فارسی معین 


ناودیس 
فرجه بیرون رود ناوقه گویند به شرط آنکه 
میان هر دو زانو بر زمین نهاده باشد نشیب نر 
و فروتر نباشد. (تاریخ قم. ۴۳. لذ.) 
ناوک: ۱2۷-2۲ [ناو + کث. بس. تصغیر و 
نسبت و شباهت - ناوه| ناوخرد. نوعی تیر 
کوچک که آن را در غلاف آهنین یا چوبین 
_ که مانند ناوی باریکک بود - گذارند و از 
کمان سر دهند تا دور تر رود. ناوی که از آن 
کندم و جو از دول به گلوی آسیا فور ریزند. 
شباری که در پشت ادمی است. شباری که 
در دانٌ گندم و هستهةٌ خرما است. هر چیز 
مبان خالی. ناوکك سحری: ( کن.) نفرینی که 
در آخرهای شب کنند. ناوک قلبی: (کن.) 
آهی که از ته دل بر آید. هجو؛ مق. مدح. 
ناوکار: ۱.۲ (ص‌شغل.) هر یک از علمة 
کشتی)؛ ملاح» ملو ان. 

ناوگان: «تی(ه-: (۱) (نظ) مجموع 
کشتی‌های جنگی یک دولت (فره.) مجموع 
کشتی‌های جنگی دولتی در ناحیه‌ای معین. 
ناوگروه: .7.۰ (امر .) (نط.) دو با سه 
دسته کسه » تیپ دربایی (فره.) 

ناوناوان: ۱2۷-03۷-0 (ق. حال) خرامان» 
گرازان. 

ناوند: 25-20 [- نان‌وند - نان‌ند] (امر.) 
بالشچه‌ای که خمیر پهن کرده بر آن نهند و 
بر دیوار تنور تافته چسانند تانان بپزد؛ 
رفنده؛ نانند. 

ناووس: 5 [- ناوس - او وس؛ معر. 
قر؛ بو.] (.) اطاق زبر زمینی که برای دفن 
میت بکار برند؛ دخمه. قبر هر فرد غیر 
مسلمان» گور کافر. گورستان زردشتیان» 
قبرستان مجوس. 

ناوه: (-)۱2۷-2 [- ناوک ] (.) ناو خرد. 
نوعی تیر. ناوی که از آن گندم و جو از دول 
به گلوی آسیا ریزند. شیاری که در پشت 
آدمی است. شباری که در دانةٌ گندم و هستة 


ناوی 
رما است: هر جز میان غالی, (رند) چوبت 
کوتاه و مجوفی که گلکاران به وسیلة آن گل 
ظرف چوبین. 

ناوی: -۰2۷(ص‌نسه.) سربازی که در 
خدمت نیروی دریابی است (فره.)» سرباز 
نیروی دریایی. 

ناویدن: ۱2-۲7 (مصل.) مانند ناو به 
چپ و راست متمایل شدن, تلوتلو خوردن. 
خرامیدن به نازء گراز بدن. خم شدن. مانده 
شدن» خسته گردیدن. میان تهی نمودن 
سنگ با قطعةً چوب. چرت زدن» پینکی 
رفتن. 

ناه [بوی نم] (.) شوانی که از زین 
نتتا کق برخیزد» وی نم. 

ناهار: 257 [د. (نه <نی) + آهار» 
بی‌خورش] (ص.) آنکه از بامداد چیزی 
رده کر یه مقضی () کرش کی رن 
نهار بودن: ناشتا بودن؛ گر سنه بودن. (ص.) 
بی‌قوت بر اثر گرسنگی. سیر ناشونده. 
سیری‌ناید یر . بی‌نصیب» محروم. تشنه. [- 
ناهاری] چیزی اندکك که بیش از طعام 
خورند» نهاری. [- اهاری] غذایی که در 
وسط روز خورده شود؛ نهار. 

ناهب: ۰560 (ع.] (افا.) غارت کنننده 
عتتما کر نله 

ناهد: 2(6۵ه [ع.] (ص.) زن بر آمده پستان. 
برخیزنده سوی دشمن» ناهض. (.) شبر»
```


## [2026-09-07T17:40:14.287Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"پناه:\" MON_part1.txt | head -5\necho \"---\"; sed -n '16590,16630p' MON_part1.txt"
}
```


### [2026-09-07T17:40:14.349Z] TOOL RESULT

```
32660:پناه: (.) حفظ حمایت» بشتی» 
32674:در پناه: در طل در کنف. 
46927:جن‌پناه: 2[ (امر.) بناه جان و 
94483:عالم‌پناه: طاقصمم-صواو [ع. ف.] (ص‌مر.) 
---

فرهنگ فارسی معیر ۱۹۱ 


یشنماز. امام جمعه: پیشنمازی که روز حمعه 
در مسحد جامع نماز خواند. مقامی روحانی 
که در اصل موظف به پیشنمازی در مسجد 
جامع و اقامة نماز جمعه بود ولی بتدریج 
مبدل به شغلی شد و هنوز نیز ايين مقام در 
عصر » ولی‌عصره امامی که در عهد خود 
دوازدهم شیعیان» مهدی(ع). آمام عصر: امام 
زمان. 

امسامت: فقس [ع. امامه] (مسصل.) 
پیشوایی کردن. (امص.) پیشوایی. پیشنمازی. 
امان؛ 0 (ع.] (سص‌ل.) بی بیم شدن. 
(امص.) بی ترسی» ایمنی. حفاظت» عنایت. 
(.) زنهار)» پناه. 

امانت: اهمقهه [ع. امانة] (مصل.) امین 
نودن. (اسص.) راستی» درستکاری؛ مس . 
خیانت. استواری. (.) مال يا چیزی که به 
زنهار» ودیمه. سته ممهور که به ستخانه 
دهند تا آن را به مقصدی برساند. (تفس.) 
تکالیفی که خدای تعالی برای خلق تعیین 
کر ده از عادات و طاعات. (تص.) جامعیت 
اسما و صفات با هستی حق. (تص.) 
استعدادی که خدای تعالی برای کسب خبر و 
علم و عشق در دل انسان به ودبعت نهاده) ج. 
امانات. 

امانی: 81« (ص‌نسه. امانت) امانتی. 
ام‌پرا ۱ نر یس : 6ا6۲مجی (.) زوجه 
امپراتور» ملکه. شهر بانو» امیراطیس. 

امپر اتور: 7 (.) عنوان سرداران 
روم قدیم. پادشاه مقتدری که بر ممالک و 
نواحی سیار سلطنت کند» شاهشاه؛ 
امپراطور؛ ایمپراطور. 

امپریال: 20065 (رص .) اسپراتوری»
```


## [2026-09-07T17:40:17.172Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '32655,32690p' MON_part1.txt"
}
```


### [2026-09-07T17:40:17.236Z] TOOL RESULT

```
آتش آن را ه روی خود بندند. تعویذی که 
به جهت دفع چشم زخم بکار آرند؛) حرز» 
وقایه. اعمالی که به جهت دفع چشم زخم 
کنند. (ص.) پوشیده» پنهان. 

پناه: (.) حفظ حمایت» بشتی» 
زشهازه استان: کننف: (من.) نگاهیان؛ 
نگاهدار حامی؛ حتافظ» حبارس. (ا.) 
پناهگاه» جای استوار» ملجا» ملاذ» مأوی. 
سای دبوار. سعادت؛ مق. نحوست. (فعل 


امر.) یناهبر» یناهنده شو. (افا.) در بعضی 


ترکیسات به معنی ریناه‌دهنده) آید: جان‌پناه. 
باه بسي خدا: به یزدان بناه» اجوذبالل» 
تن استغفرالله» عاذاً بالله. ملیدا 
عالمیان. جای بناه: پناهگاه» جای محفوظ. 
در پناه: در طل در کنف. 

پناهگاه: «جو-.ع (امر.) آنجا که برای حفظ 
13 و سلامت بناه برند؛ بناه‌جای» جای 
استوار» اند خسواره» ماٌمن. 

پناهند 7 : 2280-2002)6(8-1ج (حامص.) 
حالت و عمل بناهنده. پناهندگی سیاسی: 
مات ری کر میات خوورت 
کشور دیگری بناهنده شود. 

پناهنده: (6-)۵2021-2802 (افا.) آنکه نه 
کسی با به چیزی ناه برد: ناه آورنده» بناه 
کر نده؛ بناهیده» زنهاری» زینهاری» ملتجی؛ 
ج‌. پناهندگان. بناه‌دهنده. (مج.) باری تعالی. 
پناهیدن: 02۱2۲-7 (مص‌ل.) در حمایت 
کسی در آمدن زنهار خواستن» بناه سردن؛
```


## [2026-09-07T17:40:17.655Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/ref_page.py IRN:123 2>&1 | head -40"
}
```


### [2026-09-07T17:40:23.358Z] TOOL RESULT

```
(no exact page map; using offset 11 -> pdf page 134; check the printed number and re-run with --pdf-page if off)
REF: IRN:123  PDF: data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf page 134  OCR-lang: fas

نام‌های ایرانی در پیرامون دریای سیاه ۱۳۳
واقم شده است ومقصود از روم‌درکتاب‌های پهلوی‌هميشه آسیای صغیر و بیزانس
بوده است .

اما خشین در واژه‌های پارسی از جمله در برهان قاطع بدو صورت چنین
آمده است:

«خشین هرچیزی که به کبودی مایل و سیاه‌رنگك و تیره باشد» .

«خشی: چیزی راگوین د که سفیدی‌آن به نهایت رسیده باشدیعنی سفید سفید
وبعضی گویند بمعنی‌خشینه اس ت که سیاه تیره‌رنگك وبکبودی مایل باشد» . دراینجا
نیز چنانکه دیده می‌شوداین واژه» هم‌بمعنی درخشان آورده شد ه که همان 752622
است و هم بمعنی‌ناد رخشان‌و تیر ه که همان 2732672 کهن است . بنابرا ین ا وکسن
2 از واژة 2386 ایرانی گرفته شده و سپس نام باستانی آن ترجمه گشته و در
زبانه‌ای مختاف دریای سیاه نامیده شده است.

تعداد زیادی از نام رودهای بزرگك و کوچک اطراف دریای سیاه نیزريشه
و بن ایرانی دارند .بزرگترین این رودخانه هادانوب اس تکه‌از جنگل سیا‌سرچشمه
می‌گیرد و از آلمان و اتریش و هنگری و یوگسلاوی‌و رومانی می گذردوبدریای
سیاه فرو میریزد. این رودخانه در مسیر خود در آلمان 40220 » درچکسلوا کی
0 » در بلغارستان و یوگسلدوی 402۷ و درهنگری 102 نامیده می‌شود
و همه این نامها از ريشهٌ 430۱ اوستایی بمعنی رود و 1221۷2 فارسی باستان
بمعنی جاری شدن است .

درکتیبهُ فارسی باستان کانال سوئز که بفرمان داریوش بزرگ کنده شده
است‌واژةٌ 42800۷2 در جملةٌ زیر بکار رفته است:

ال بونه و3۵۳3 12 720۵ عصقد 2اقعام 224۵

یعنی از «پیراو» نام رودی که در مصر جاریست .

ريشه 435 در یک واژه فارسی امروزی نیز باقی است و آن واژه «ناودان»
اس ت که م رکب است از 432 +23۷ . واژهٌ ناو در فرهنگك‌های فارسی بمعنی‌چوی
```


## [2026-09-07T17:40:33.779Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/ref_page.py IRN:123 --pdf-page 124 2>&1 | head -45"
}
```


### [2026-09-07T17:40:35.079Z] TOOL RESULT

```
REF: IRN:123  PDF: data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf page 134  OCR-lang: fas

نام‌های ایرانی در پیرامون دریای سیاه ۱۳۳
واقم شده است ومقصود از روم‌درکتاب‌های پهلوی‌هميشه آسیای صغیر و بیزانس
بوده است .

اما خشین در واژه‌های پارسی از جمله در برهان قاطع بدو صورت چنین
آمده است:

«خشین هرچیزی که به کبودی مایل و سیاه‌رنگك و تیره باشد» .

«خشی: چیزی راگوین د که سفیدی‌آن به نهایت رسیده باشدیعنی سفید سفید
وبعضی گویند بمعنی‌خشینه اس ت که سیاه تیره‌رنگك وبکبودی مایل باشد» . دراینجا
نیز چنانکه دیده می‌شوداین واژه» هم‌بمعنی درخشان آورده شد ه که همان 752622
است و هم بمعنی‌ناد رخشان‌و تیر ه که همان 2732672 کهن است . بنابرا ین ا وکسن
2 از واژة 2386 ایرانی گرفته شده و سپس نام باستانی آن ترجمه گشته و در
زبانه‌ای مختاف دریای سیاه نامیده شده است.

تعداد زیادی از نام رودهای بزرگك و کوچک اطراف دریای سیاه نیزريشه
و بن ایرانی دارند .بزرگترین این رودخانه هادانوب اس تکه‌از جنگل سیا‌سرچشمه
می‌گیرد و از آلمان و اتریش و هنگری و یوگسلاوی‌و رومانی می گذردوبدریای
سیاه فرو میریزد. این رودخانه در مسیر خود در آلمان 40220 » درچکسلوا کی
0 » در بلغارستان و یوگسلدوی 402۷ و درهنگری 102 نامیده می‌شود
و همه این نامها از ريشهٌ 430۱ اوستایی بمعنی رود و 1221۷2 فارسی باستان
بمعنی جاری شدن است .

درکتیبهُ فارسی باستان کانال سوئز که بفرمان داریوش بزرگ کنده شده
است‌واژةٌ 42800۷2 در جملةٌ زیر بکار رفته است:

ال بونه و3۵۳3 12 720۵ عصقد 2اقعام 224۵

یعنی از «پیراو» نام رودی که در مصر جاریست .

ريشه 435 در یک واژه فارسی امروزی نیز باقی است و آن واژه «ناودان»
اس ت که م رکب است از 432 +23۷ . واژهٌ ناو در فرهنگك‌های فارسی بمعنی‌چوی
```


## [2026-09-07T17:40:39.187Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN\ngrep -n \"ناودان\" IRN_pages.txt | head -10\necho \"=== page tags near ===\"\ngrep -n \"\\[pdf page\" IRN_pages.txt | head -5"
}
```


### [2026-09-07T17:40:39.261Z] TOOL RESULT

```
3872:ريشه ص43 در یک واژه فارسی امروزی نیز باقی است و آن واژه «ناودان»
6772:ناودان ۱۳۳ ۰ ورئان ۱۶8
=== page tags near ===
1:[pdf page 1]
7:[pdf page 2]
17:[pdf page 3]
27:[pdf page 4]
31:[pdf page 5]
```


## [2026-09-07T17:40:43.611Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN\nsed -n '3868,3900p' IRN_pages.txt"
}
```


### [2026-09-07T17:40:43.660Z] TOOL RESULT

```
اواج نحل وند‌وق7 1 ۶2 ها۵+ حصسقد دقعام عمط

یعنی از «پیراو» نام رود ی که در مصر جاریست .

ريشه ص43 در یک واژه فارسی امروزی نیز باقی است و آن واژه «ناودان»
اس ت که م رکب است از ۹32+ 2۷. واژْهٌ ناو در فرهنگك‌های فارسی بمعنی‌چوی
[pdf page 135]
۱۳4 ایرانویج
آب یا هرچیز دراز و بیان تهمی است و «دان» بمعنای جریان آب است و بررویهم
بمعنی چیز میان‌تهی اس تکه‌آب درآن جاری باشد و دانوب بمعنی آب جاری است
و شکل بلغاری و یوگسااوی‌این واژه که 1002۷ است ترکیب آنرا بهتر نشان
می‌دهد.

«دن» 42۳ در زبان ایرانی آس ی کنونی‌نیز بمعنی رود است و تعداد زیادی
از نام‌های رودهای تفقاز شمالی بادن 40 ختم می‌شوند مانند » فیاگك دن »
گیزیل‌دن» آردن و غیره.
واژه 120 بصورت 408 در رودخانه‌های‌بزرگك دیگر نیز دیده می‌شودمانند
رود 40۳ که بدریای آزوف می‌ريزد و بصورت مرکب در نام‌رودهای دیگرآمده
بانند «0عفصل وتاوه‌نطل که بدریای سیاه می‌ریزند و 400612 که از رودهای
روسیه جنوبی است واين واژه حتی در رود 402۶ که بدریای چین می‌ریزد نیز
دیده می‌شود .
ناحیه تنگه "کرج 16700 که دریای آزوف را بدریای سیاه می‌پیوندد و
شهر ی که در کنارآن بوده است؛درروزگا ران کهن نهم1162ص2م با نم 2علناصد0
نام داشته است ونیز رودی که امروز بنام 2 يا [080م معروف است همین‌نام را
داشته است .,
نام « پنت یکاپه » نیز ایرانی است و ترکیب یافته است از واژه‌های
2+ 0220 وااصدم در زیان اوستایی‌بمعنی راه است . دراوستا درمهریشت چنین
آمده است :
1 510۴۵ 61 مد داد قلمقم خععاة ناندعدل ممقاصدم راکمه
از نج
که معنی آن چنین است: راست‌ترین راه رامی‌دهد آتش بزدا اهورا به کس ی که
دروغ نگوید. دراين جمله پنته 02012 بمعنی راه است ودر فارسی کنونی واه پند
بمعنی اندرز از همین ريشه است به معنی راه نشان دادن وفن به معنی روش و
```


## [2026-09-07T17:40:53.511Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN ship ===\"; grep -n \"10.81\\|‘Ship’\\|nāus\" SYN.txt | head -10\necho \"=== IEC nau ===\"; grep -n \"nāus\\|nāu-\\|nāu (\" IEC.txt | head -10\necho \"=== CHEUNG nath ===\"; grep -n \"nāθ\\|nath\\b\\|\\*naH\" CHEUNG.txt | head -10\necho \"=== KLN nautical/nausea/noise ===\"; grep -n \"nautical\\|nausea\\|nautilus\\|Nave (2)\\|navy\" KLN_1966.txt | head -10"
}
```


### [2026-09-07T17:40:53.609Z] TOOL RESULT

```
=== SYN ship ===
16624:M wb.) 10.54 OverTAKE oll pen Gb.) 10.55 Arrive, REACH 10.12 ae AROUND 10.56 APPRoAcH (vb.) 40.18 Wino, WRAP (vb.) 10.57 ENTER 10.14 Ron (7b.) 10.61 Carry (BEaR) 10,15 rairb.) 10.62 Brine re Russe, LIFT 10.63 SEND 10. vb.) 10.64 Leap (vb.) Ce se Tigui 10.65 D 1024 Dror (sb., of Liquid) : RIVE (vb. trans.) 1025 THROW (vb.) 10.66 Rive (vb.) 1098 SHAKE (vb. trans.) 10.67 Pusu, Sov (vb.) 1031 Bor (vb. intr.) 10.71 Roan 10.33 Smvx (vb.) 10.73 Street 10.34 Fuoat (vb.) 10.74 Brmwce 10.35 Sw (vb.) 10.75 Carrtace, Wacon, Cart 1036 Satz (vb.) 10.76 WHEEL 1037 Fuy (vb.) 10.77 AXLE 10.38 Brow (vb. intr.) 10.78 Yoxs 1041 Creer, CRAWL 10.81 Sup 1042 Ste, Sur (vb.) 10.82 Sartor 1043 Jump, Leap (vb.) 1044 Dancz (vb.) ee meee 1045 Watx (vb.) i 10.46 Run (vb.) 10.85 Oar 1047 Go 10.852 Row (vb.) 1048 Come 10.86 RuppER 1049 Go Away, Depart 10.87 Masr a Tze 10.88 Sar (sb.) 10.53 peso 10.89 AncHoR
17209:deriv. of navis ‘ship’ (10.81). Ernout- M. 624.
17227:MHG, NHG schiffen, deriv. of Schiff ‘ship’ (10.81).
17229:Lett. kug’uot, deriv. of kug'is ‘ship’ (10.81).
18361:10.81 SHIP Grk. vais, xdotoy Goth. skip Lith. laivas NG _ wAoio, xapapi ON skip (nor, fley) Lett. kug'is Lat. navis, navigium Dan. _skib ChSl.  korabljt, ladtji It. nave, vascello, bastli- Sw. skepp SCr. _brod, lada mento OE scip Boh. lod’, kordb Fr. navire, vaisseau, bali- ME  schip, vessel Pol. okrel, statek ment NE ship, vessel Russ. korabl’, sudno Sp. buque, nave, navio Du. _—_schip Skt.  ndu- Rum. corabie OHG - scif, scef Av. (navaya-, adj.) Ir. nau, long (estar) MHG  schif, schef NIr. long NHG | schiff W. llong Br. lestr
18362:‘Ship’ is understood here as a seagoing vessel of some size in contrast to the smaller ‘boat’, with disregard of the more specific technical use of NE ship and the fact that NE boat is also a popu-
18416:1. Grk. vabrns (> Lat. nauta), Ir. noaire, noere, Skt. navika-, derivs. of Grk. vats, etc. ‘ship’ (10.81).
18420:Ir. loingseach, deriv. of long ‘ship’ (10.81).
18431:‘hip! (10.81).
18480:4. Goth. skip, OHG scif ‘ship, boat? (10.81).
=== IEC nau ===
5751:8në-, alternative radical form of ĝnāu-, 2no-
5752:mi, q. V. Alb. cf. njof, njoh (“know a person’, fr. *&nesk- or *&nåsk-); OHG cf. knāu (I know’, a past- present form of type novi, -gnoviin Lat.). (Lat. i-ghOrO, are seems to represents a type *n- &naus- but wt. certain cognate forms)
11554:nāustos, à, ios, iom, io (nàut-, nauit-) “float, fleet, floating bird or object? Gk. cf. nésos, f. “island”; n&ssa, f. ‘duck’; Lat. cf. nautea 'bilge-water; Gallo-Lat. nausum (kind of boat’. Phonol. of Lat. LW nausea); OBr. (queried) -naued ‘boats’; Br. nued, nóed, pl. -u & nueZu, m. ‘roof gutter’; ON cf. naust, n. ‘boathouse’
=== CHEUNG nath ===
22860:*SANSKRIT: snath' ‘to push (down), strike (down), pierce’ (КУ) > EWAia II: 659 
51934:Sanath, 331 
51963:snath’, 349 
=== KLN nautical/nausea/noise ===
794:nautical
1817:aeronaut,  n.  —  Compounded  of  aero-  and  Gk. vx>Tr  ‘sailor  .  See  nautical.
2329:alodial,  alodium,  n.  —  See  allodial,  allodium, aloe,  n.  —  L.  aloe,  fr.  Gk.  aX6r),  ‘aloe’,  prob. borrowed  fr.  Heb.  ahaltm,  ahaldth  (pi.),  which are  perhaps  borrowed  fr.  OI.  agaruh,  aguruh, ‘aloewood’,  these  latter  being  prob.  of  Dravid- ian  origin.  Cp.  agalloch. aloetic,  adj.  containing,  or  of  the  nature  of,  aloes ; n.,  an  aloetic  medicine.  —  Formed  with  suff. -etic  fr.  Gk.  aXot],  ‘aloe’.  See  aloe, aloft,  adv.  —  ON.  a  lopt,  ‘in  the  air’,  whence  arose the  meaning  ‘on  high’.  See  a-,  ‘on’,  and  loft, aloin,  n.,  a  bitter  crystalline  substance  (chem.)  — Formed  fr.  aloe  with  chem.  suff.  -in;  so  called because  it  is  obtained  from  the  aloe, aloisiite,  n.,  a  hydrous  subsilicate  of  calcium, ferrum,  magnesium  and  sodium  (mineral.)  , Named  after  Prince  Luigi  (Latinized  into  Aloi- sius)  Amedeo  of  Savoy,  Duke  of  the  Abruzzi. For  the  ending  see  subst.  suff.  -ite. alone,  adj.  —  ME.  al  one ,  ‘all  alone  ,  fr.  al,  all , and  one,  fr.  OE.  an,  ‘one,  alone  .  Cp.  Du.  alleen, MHG.  al-ein,  al-eine,  G.  allein,  ‘alone’,  and  see all  and  one.  Cp.  also  lone, along,  adv.  and  prep.  —  ME.  anlong,  along,  fr.  OE. andlang ,  which  is  compounded  of  and-,  ‘against’, and  lang,  ‘long’.  The  first  element  is  cogn.  with Gk.  avxt,  ‘against’,  L.  ante,  ‘before’ ;  see  ante-, anti-.  For  the  second  element  see  long,  adj. aloof,  adv.  —  Originally  a  nautical  term  formed on  the  analogy  of  Du.  te  loef,  ‘to  windward  . See  loof,  luff.
2493:ammoniac,  adj.  and  n.  —  F.,  fr.  L.  ammoniacum, fr.  Gk.  afj.[i(ovtax6v,  ‘a  resinous  gum’,  prob. fr.  orig.  ’Apjxsviaxov,  ‘Armenian’,  through  the intermediate  form  apgioviaxov,  occurring  in  the works  of  ancient  authors  beside  ap.|icovtax6v; so  called  because  first  found  in  Armenia.  See Pauly-Wissova,  Real-Encyclopadie  der  klas- sischen  Altertumswissenschaft,  I,  1861. Derivative:  ammoniac-al,  adj. ammonite,  n.,  a  cephalopod  mollusk  allied  to  the nautilus  (paleontol.)  —  Formed  with  subst.  suff. -ite  fr.  L.  cornu  Ammonis,  ‘the  horn  of  (Zeus) Ammon;  so  called  from  its  shape,  which  re¬ sembles  a  ram’s  horn  (Zeus  Ammon  was  rep¬ resented  with  ram’s  horns), ammonium,  n.,  a  basic  radical,  NH4  (chem)  — ModL.,  fr.  ammonia  (q.v.) ammophilous,  adj.,  sand-loving  (zool.  and  hot.) — -  Compounded  of  ammo-  and  Gk.  iplXog, ‘loving’.  See  -philous.
3405:Argonaut,  n.  pi.,  one  of  the  heroes  led  by  Jason in  the  ship  Argo  to  fetch  the  golden  fleece  in Colchis.  —  L.  Argonauta,  fr.  Gk.  ’  Apyovau-pp, ‘sailor  of  the  Argo’,  which  is  compounded  of ’  Apyco  (see  Argo)  and  vcGrr,:,  ‘sailor,  seaman’. See  nautical.
3406:argonaut,  n.,  the  paper  nautilus  (zoo!)  —  Fr. prec.  word.
3458:armada,  n.,  a  fleet  of  warships;  specif,  the  fleet of  warships  sent  against  England  by  Philip  II of  Spain  in  1588,  called  the  Spanish  or  Invin¬ cible  Armada.  —  Sp.,  ‘fleet,  navy’,  fr.  L.  armata, fem.  pp.  of  armare,  ‘to  furnish  with  weapons’, used  as  a  noun,  fr.  arma,  ‘weapons’.  See  arm, ‘weapon’,  and  cp.  army.
3769:astronaut,  n.,  one  who  flies  through  space;  one concerned  with  space  flight.  —  Compounded of  astro-  and  Gk.  vauxrji;,  ‘sailor,  seaman’.  See nautical  and  cp.  cosmonaut, astronautics,  n.,  the  science  of  space  flight.  — Compounded  of  astro-  and  nautics.  Cp.  prec. word.  Cp.  also  cosmonautics, astronomer,  n.  —  See  astronomy  and  agential  suff. -er.
9343:Derivatives:  cosmolog-ic,  cosmolog-ic-al,  adjs., cosmolog-ic-al-ly,  adv.,  cosmolog-ist,  n. cosmonaut,  n.,  an  astronaut.  —  Compounded  of cosmo-  and  Gk.  vxorr;;,  ‘sailor,  seaman’.  See nautical  and  cp.  astronaut, cosmonautics,  n.,  astronautics.  —  Compounded of  cosmo-  and  nautics.  Cp.  prec.  word.  Cp.  also astronautics.
16373:goatee,  n.,  a  man’s  beard  resembling  a  goat’s beard.  —  Formed  from  prec.  word  with  suff.  -ee. Derivative:  goate-ed,  adj. gob,  n.,  a  mouthful  of  saliva;  a  lump  of  slimy substance.  —  OF.  gobe,  ‘a  mouthful,  a  lump’ [whence  F.  gobe,  gobbe,  ‘fattening  ball  (for poultry);  poisoned  ball  (for  a  dog)’],  of  Celtic origin;  cp.  Ir.  gob,  ‘mouth’,  Gael,  gob,  ‘beak’. Cp.  gobbet,  gobble,  ‘to  eat  greedily’,  goblet, gob,  n.,  a  sailor  in  the  navy  (slang).  —  Perh.  lit.
```


## [2026-09-07T17:40:59.095Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '794,800p' KLN_1966.txt\necho \"=== noise ===\"; grep -n \"^noise,\\|noise,  n\\.\" KLN_1966.txt | head -5\necho \"=== nausea ===\"; grep -n \"nausea,  n\\.\\|nauseous\" KLN_1966.txt | head -5\necho \"=== navy ===\"; grep -n \"navy,  n\\.\\|navigate,  intr\" KLN_1966.txt | head -5"
}
```


### [2026-09-07T17:40:59.199Z] TOOL RESULT

```
nautical
NE.
North  East
neg.
negative
Neh.
Nehemiah
=== noise ===
25532:noise,  n.,  a  loud  cry  or  shouting;  clamor;  din.  — ME.,  fr.  OF.  noise  (in  ModF.  used  only  in  the phrase  chercher  noise,  ‘to  pick  a  quarrel’),  fr.  L. nausea,  ‘seasickness’,  which  in  Vulgar  Latin prob.  had  the  meaning  of ‘unpleasant  situation, noise,  quarrel’.  For  sense  development  cp. OProven?.  nauza,  noiza,  ‘noise,  quarrel’,  which also  derive  fr.  L.  nausea.  See  Bloch-Wartburg, DELF.,  p.  412  s.v.  noise.  See  nausea.
=== nausea ===
25003:nasty,  adj.,  dirty,  foul,  filthy,  nauseous.  —  ME. nasty,  nasky,  perh.  derived  from  or  rel.  to  Du. nestig,  'foul,  dirty’,  or  of  Scand.  origin;  cp.  dial. Swed.  naskug,  nasket,  'foul,  dirty’.
25042:Naucratite,  adj.,  pertaining  to  Naucratis,  an  an¬ cient  Greek  colony,  established  by  colonists from  Miletus  in  the  Nile  Delta.  — L.  Naucratites, fr.  Gk.  NauxpaxtxvjS,  fr.  Nauxpaxt?.  For  the ending  see  subst.  suff.  -ite. naufragous,  adj.,  caused  by  shipwreck  ( archaic  or obsol.)  —  L.  naufragus,  ‘shipwrecked;  causing shipwreck’,  for  *navifragus,  which  is  compound¬ ed  of  navis,  ‘ship’,  and  the  stem  oifrangere,  'to break’.  See  naval  and  fraction.  For  E.  -ous,  as equivalent  to  L.  -us,  see  suff.  -ous. naught,  n.,  nothing.  —  ME.  naught,  nought,  etc., fr.  OE.  nawiht,  ‘nothing’,  lit.  ‘no  whit’,  fr.  nd, ‘no’,  and  wiht,  'whit’.  See  no,  adv.,  and  wight and  cp.  aught,  nought,  not,  nix,  ‘nothing’. Derivatives:  naught,  adj.,  naught-y,  adj.,  naught- i-ly,  adv.,  naught-i-ness,  n. naumachia,  naumachy,  n.,  1)  a  mock  sea  fight;  2) place  where  such  a  fight  is  presented  (Roman antiq.)  —  L.,  fr.  Gk.  vaup.a/la,  ‘naval  battle’, compounded  of  van?,  ‘ship’,  and  -uay.a,  fr. \s.y-/r„  ‘battle’.  See  nau-  and  -machy. nauplius,  n.,  a  larval  stage  in  the  development  of many  crustaceans  (zool.)  —  L.,  ‘a  kind  of  shell¬ fish  which  sails  in  its  shell  as  in  a  ship',  fr.  Gk. vau7tXtoi;,  lit.  ‘sailing  (as)  in  a  ship’,  fr.  vau<;, ‘ship’,  and  7tX£Etv,  trXetv,  ‘to  sail,  navigate, swim,  float’.  See  naval  and  flow  and  cp.  pluvial, nausea,  n.,  1)  feeling  of  sickness  at  the  stomach; 2)  disgust,  loathing.  —  L.  nausea,  nausia,  ‘sea¬ sickness’,  fr.  Gk.  vxuoia,  vauxta,  ‘seasickness’, lit.  ‘ship  sickness’,  fr.  vans,  ‘ship’.  See  naval  and cp.  nautical.  Cp.  also  noise,  which  is  a  doublet of  nausea.
25045:nauseous,  adj.,  causing  nausea,  disgusting. Formed  fr.  nausea  with  suff.  -ous.
25046:Derivatives:  nauseous-ly,  adv.,  nauseous-ness,  n. Nausicaa,  n.,  in  the  Odyssey,  daughter  of  Alci- nous,  king  of  the  Phaeacians  —  L.  Nausicaa,  fr. Gk.  Nxumxda.  The  name  prob.  means  ‘burner of  ships’,  fr.  vauc,  ‘ship’,  and  xaisiv,  ‘to  burn'. See  naval  and  caustic.
=== navy ===
25066:navigate,  intr.  v.,  to  travel  by  ship;  tr.  v.,  to  trav¬ el  through  (on  the  water  or  in  the  air) ;  to  direct (a  ship  or  an  aircraft).  —  L.  navigatus,  pp.  of navigdre,  ‘to  sail,  set  sail’,  lit.  ‘to  drive  a  ship’, fr.  *navigus,  for  *nav-agos,  ‘driving  a  ship’, which  is  compounded  of  navis,  ‘ship’,  and agere,  ‘to  set  in  motion,  drive,  lead,  conduct’. See  naval  and  agent,  adj.,  and  verbal  sufif.  -ate. For  the  change  of  d  (in  agere )  to  i  (in  *ndv-igus, nav-igare )  see  abigeat  and  cp.  words  there  re¬ ferred  to.  Cp.  also  circumnavigate, navigation,  n.,  the  act  and  art  of  navigating.  — L.  navigatio,  gen.  -onis,  fr.  navigatus,  pp.  of navigdre.  See  prec  word  and  -ion.
25067:Derivative:  navigation-ai,  adj. navigator,  n.,  1)  one  who  navigates;  2)  a  navigat¬ ing  officer;  3)  a  navvy  (British).  —  L.  navigator, ‘sailor’,  fr.  navigatus,  pp.  of  navigdre.  See  navi¬ gate  and  agential  suff.  -or  and  cp.  next  word, navvy,  n.,  an  unskilled  laborer,  esp.  one  em¬ ployed  in  making  canals,  roads,  etc.  —  Short¬ ened  fr.  navigator  (q.v.);  for  meaning  cp. navigation  in  the  dialectal  sense  ‘canal’, navy,  n.  —  ME.  navie,  fr.  OF.  navie,  ‘fleet  of ships,  ship’,  fr.  Late  L.  navia,  of  s.m.,  fr.  L. navis.  See  naval.
```


## [2026-09-07T17:41:04.937Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '25043,25044p;25060,25065p' KLN_1966.txt"
}
```


### [2026-09-07T17:41:04.988Z] TOOL RESULT

```
nauseate,  tr.  v.,  to  affect  with  nausea,  make  sick ; intr.  v.,  to  become  affected  with  nausea,  feel disgust  (rare).  —  L.  nauseat-(um),  pp.  stem  of nausedre,  ‘to  feel  seasick,  to  vomit’,  fr.  nausea. See  prec.  word  and  verbal  suff.  -ate.
Derivatives:  nauseat-ing,  adj.,  nauseat-ing-ly, adv.,  nauseat-ion,  n.
vel’.  Cp.  nave,  'hub  of  a  wheel’.  Cp.  also  om- phalo-,  omphalos,  umbilicus,  umbo,  nombril. navew,  n.,  1)  the  wild  turnip;  2)  the  rape  (rare)  — F.  naveau,  fr.  OF.  navel,  fr.  VL.  *napellus,  dim. of  napus,  ‘a  kind  of  turnip’,  fr.  Gk.  vami,  ‘mus¬ tard’,  which  is  prob.  of  Egyptian  origin.  (For the  sense  development  of  L.  napus  from  Gk. va7tu  it  should  be  borne  in  mind  that  the  mus¬ tard  plant  and  the  turnip  resemble  each  other  in form.)  Cp.  neep  and  sinapism,  the  first  element in  napiform  and  the  second  element  in  parsnip and  in  turnip.
navicert,  n.,  a  certificate  issued  to  exempt  a  ship from  search  for  contraband.  —  Short  for  navi¬ gation  certificate.
navicular,  adj.,  boat-shaped  (said  of  certain bones  in  the  fore  and  hind  feet  of  animals)  —  L. navicularius,  ‘pertaining  to  a  boat’,  fr.  navicula, ‘a  boat’,  dim.  of  navis.  See  naval  and  the  suffixes -cule  and  -ar.
Derivative:  navicular,  n.,  a  bone  resembling  a boat  ( anat .)
navigable,  adj.  —  Fr.  F.  navigable,  or  directly  fr. L.  navigabilis,  fr.  navigdre.  See  navigate  and -able.
Derivatives:  navigabil-ity,  n.,  navigable-ness,  n., navigabl-y,  adv.
```


## [2026-09-07T17:41:07.872Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"nautical,  adj\\|nautilus,  n\\|naval,  adj\" KLN_1966.txt | head"
}
```


### [2026-09-07T17:41:07.917Z] TOOL RESULT

```
25048:nautical,  adj.,  pertaining  to  ships,  seamen  or  navi¬ gation.  —  Formed  with  adj.  suff.  -al  fr.  now rare  nautic,  fr.  F.  nautique,  fr.  L.  nauticus,  ‘of, or  pertaining  to,  ships  or  sailors,  seafaring, naval,  nautical’,  fr.  Gk.  vocuxix6<;,  of  s.m.  See naval  and  cp.  words  there  referred  to.  Cp.  also
25053:nautilus,  n.,  1)  any  of  a  group  of  mollusks;  2)  the paper  nautilus  (zool.)  —  L.,  fr.  Gk.  vauxiXoi;, ‘sailor,  seaman;  the  paper  nautilus’  (so  called because  it  was  supposed  to  be  furnished  with  a membrane  which  it  used  like  a  sail),  fr.  vaiVn ‘sailor,  seaman’.  See  nautical, naval,  adj.,  pertaining  to  a  navy,  its  ships  or  men. —  Orig.  ‘pertaining  to  ships’,  fr.  L.  ndvalis,  fr. navis,  ‘ship’,  which  is  cogn.  with  OI.  nauh,  acc. ndvam,  ‘ship,  boat’,  Arm.  nav,  ‘ship’,  Gk.  vau?, ‘ship’  (whence  vaun)<;,  ‘sailor,  seaman’,  vauxi- x6?,  ‘of,  or  pertaining  to,  ships  or  sailors,  sea¬ faring,  naval,  nautical,  vocuxtXo?,  ‘sailor,  sea¬ man’),  OIr.  nau  (gen.  noe,  dat.  pi.  noib),  ‘ship’, W.  noe,  ‘a  flat  vessel;  a  kneading  trough’,  ON. nor,  ‘ship’.  Cp.  nacelle,  nau-,  nausea,  nautical, nautilus,  nave,  ‘the  central  part  of  a  church’, navicular,  navy,  navvy,  nef,  noise,  the  first  element in  naufragous,  nauplius,  navigate,  and  the  second element  in  Echeneis.
```


## [2026-09-07T17:41:11.533Z] TOOL CALL #42: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T17:41:11.540Z] TOOL RESULT

```


```


## [2026-09-07T17:41:15.034Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%88",
 "prompt": "Give the Persian (fa) section for ناو: etymology (Middle Persian, Proto-Iranian, Proto-Indo-European forms), and all senses. Also any Middle Persian / other language sections."
}
```


## [2026-09-07T17:41:16.688Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%A7%D9%87",
 "prompt": "Give the Persian section for پناه: full etymology (Middle Persian form, Proto-Iranian reconstruction, PIE root, cognates such as Sanskrit nātha), and senses. Quote the etymology text."
}
```


### [2026-09-07T17:41:22.374Z] TOOL RESULT

```
# Persian Section for ناو

## Etymology

The word derives from **Middle Persian** _nʾw_ (nāw, "ship"), which came from **Old Persian** _𐎴𐎠𐎺_ (n-a-v /nāva/). This traces back to **Proto-Iranian** _*náHuš_, and ultimately to **Proto-Indo-European** _*néh₂us_. Related cognates include Sanskrit नाव (nāva), Ancient Greek ναῦς (naûs), and Latin nāvis.

## Senses

The word has 18 documented meanings in Persian:

1. Boat or small ship (archaic usage)
2. Warship; cruiser
3. Any long, hollow object
4. Pipe
5. Gutter, drainpipe, water pipe, or downpipe
6. River, stream, channel, canal, aqueduct, or river basin
7. Cistern or tankage
8. Trough or feeder
9. Mill-dam sluice
10. Furrow or groove on human back, horse loins, wheat grain, or date-stone
11. Gluteal cleft
12. Grain-grinding passage
13. Hole
14. Crack or chink
15. Baker's rolling-pin
16. Frying pan
17. Cauldron, kettle, or pot
18. Graceful, easy gait while walking

**Note:** No separate Middle Persian section exists in the provided content.
```


### [2026-09-07T17:41:23.411Z] TOOL RESULT

```
# Persian Section for پناه

## Etymology

The page provides limited etymological information. The source states: "From [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") _[𐭯𐭭𐭠𐭧](/wiki/%F0%90%AD%AF%F0%90%AD%AD%F0%90%AD%A0%F0%90%AD%A7#Middle_Persian "𐭯𐭭𐭠𐭧")_ (panāh, "protector; refuge")."

Unfortunately, the Wiktionary entry does not include Proto-Iranian reconstructions, PIE roots, or Sanskrit cognates. The etymology section only traces the word back to Middle Persian.

## Senses

The Persian noun **پناه** (panāh / panâh) has four meanings:

1. Shelter
2. Refuge
3. Asylum
4. Protection

The entry also lists derived terms and descendants across multiple languages (Bengali, Hindustani, Kazakh, Tajik, Uyghur, and others), demonstrating the word's widespread influence in Persian-influenced linguistic regions.
```


## [2026-09-07T17:41:29.070Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%90%AD%AF%F0%90%AD%AD%F0%90%AD%A0%F0%90%AD%A7",
 "prompt": "Give the Middle Persian entry 𐭯𐭭𐭠𐭧 (panāh): full etymology, any Proto-Iranian reconstruction, cognates, and senses. Quote the etymology text verbatim."
}
```


## [2026-09-07T17:41:30.014Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/noise",
 "prompt": "Give the full etymology of \"noise\", including the debate about Latin nausea vs noxia, and dates."
}
```


### [2026-09-07T17:41:33.819Z] TOOL RESULT

```
# Middle Persian Entry: pnʾh (panāh)

## Senses
The entry provides two definitions:
1. "protector"
2. "refuge"

## Etymology
Unfortunately, the page content does not include an explicit etymology section. The entry only presents the word itself with its transliteration and meanings, without discussing Proto-Iranian reconstructions or etymological origins.

## Cognates & Descendants
The page documents extensive descendants across multiple language families descended from Persian پناه (panāh), including:

- Bengali, Chagatai, Hindustani (Hindi/Urdu), Kazakh, Turkic languages (Azerbaijani, Ottoman Turkish, Uyghur, Uzbek), Punjabi, and Turkmen

However, no Proto-Iranian reconstruction or cognate forms from related languages are provided in the visible content.
```


### [2026-09-07T17:41:37.115Z] TOOL RESULT

```
# Etymology of "Noise"

**Early History (c. 1200-1300)**
The word originated around 1200, initially meaning "sound of a musical instrument," evolving by the mid-13th century to describe "loud speech, outcry, clamor," and by 1300 encompassing "a sound of any kind from any source," particularly disagreeable sounds.

**Origin Source**
The term derives from Old French *noise*, meaning "din, disturbance, uproar, brawl" (11th century), which replaced the native English word *gedyn* (related to "din").

**The Latin Debate**
Scholars have proposed two competing Latin origins:

1. **Latin *nausea* theory**: Some scholars connect it to *nausea* ("disgust, annoyance, discomfort"), literally "seasickness." This could have developed in Vulgar Latin to mean "unpleasant situation, noise, quarrel," supported by Old Provençal *nauza* meaning "noise, quarrel."

2. **Latin *noxia* theory**: Others suggest derivation from *noxia* ("hurting, injury, damage").

The Oxford English Dictionary "considers that the sense of the word is against both suggestions," though the *nausea* connection seems more plausible given semantic shifts in Vulgar Latin.

**Related Confusion**
The word became conflated with "annoy," "noisome," and similar terms over time.

**Verb Form (late 14th century)**
As a verb, *noisen* appeared in the late 1300s, meaning "to praise" or "to spread by rumor or report."
```


## [2026-09-07T17:41:43.996Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A4%BE%E0%A4%A5",
 "prompt": "Sanskrit नाथ (nātha): give the etymology (root, PIE), senses, and any mention of Avestan/Iranian cognates. Quote the etymology."
}
```


## [2026-09-07T17:41:45.061Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%88%DA%A9",
 "prompt": "Persian ناوک: etymology (relation to ناو + diminutive suffix), senses, and descendants/borrowings into other languages (Arabic, Turkish, etc.). Quote the etymology."
}
```


### [2026-09-07T17:41:50.433Z] TOOL RESULT

```
# ناوک (nawik) - Etymology and Meaning

Based on the Wiktionary entry provided, here's what's documented:

## Etymology
The word traces back to Proto-Indo-European origins. According to the source: **"Ultimately from Proto-Indo-European *h₃nebʰ- ("navel")"** The entry also notes a comparison with Middle Persian nāfag, which similarly means "navel."

## Meaning
**ناوک** (nawik) in Central Kurdish means **navel** — the belly button or umbilicus.

## Limitation
The provided webpage content focuses exclusively on the Central Kurdish entry and does not include information about Persian etymology (such as relations to ناو or diminutive suffixes), nor does it document descendants or borrowings into Arabic, Turkish, or other languages. To find that comparative linguistic data, you would need to consult the Persian Wiktionary version or other etymological resources.
```


### [2026-09-07T17:41:50.856Z] TOOL RESULT

```
# Sanskrit नाथ (nātha): Etymology and Senses

## Etymology

**Root and PIE Origin:**
The word derives from Proto-Indo-European *h₃neh₂- ("to help, support"). As stated in the document: "From Proto-Indo-European _*h₃neh₂-_ ('to help, support')."

The Sanskrit root is नाथ्‌ (nāth, "to seek aid, ask").

**Cognates:**
The document notes a cognate in Ancient Greek: "Cognate with Ancient Greek _ὀνί̆νημῐ_ (oní̆nēmĭ, 'to help; to please')."

**Note on Iranian Cognates:**
The provided text makes no mention of Avestan or other Iranian cognates for this term.

## Primary Senses

1. **Refuge, help, resort** — the neuter noun form (citing the Atharvaveda)
2. **Protector, patron, possessor, owner, ward, guardian, lord** — the masculine noun form, frequently appearing at the end of compound names
3. **Husband** (especially in vocative form)
4. A rope passed through the nose of a draft ox

The masculine sense dominates in classical Sanskrit literature and naming conventions.
```


## [2026-09-07T17:41:58.070Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '21180,21215p' FSF_pages.txt\necho \"=== leaf ===\"; awk 'NR<=21197{c+=gsub(/\\f/,\"\")} END{print \"leaf=\",c}' FSF_pages.txt"
}
```


### [2026-09-07T17:41:59.257Z] TOOL RESULT

```
‫بدان آگهی تیز بشتافتم‬                                               ‫چگونه نباشیم امروز شاد‬
 ‫(‪)۵-۱-۱۹۳-۲۲۶۲‬‬                                    ‫که داماد باشد نبیرة قباد‬
                                    ‫ناسزاوار‬                               ‫(ویس ‪:)۲۴۱-۰۴۱‬‬
                    ‫بی‌ارج‪ .‬بی‌بها؛ ناچیز‪:‬‬                      ‫ید‬
                                                                 ‫زومی‬‫ایر‬
                                                                       ‫سو ش‬
                                                                          ‫بر چ‬
                                                                             ‫به‌مهر اند‬
 ‫سخن از چرمی دمریانست کهکاوه بر سر‬                 ‫بسازید و به یکدیگر بنازید‬
 ‫چوب کرد و به‌نام درفش کاویانی معروف‬                                            ‫(حافظ ‪:)۸۴‬‬
                                      ‫شد‪:‬‬
‫تاهار‬



‫آهنین کهمانند ناوی باریک باشد کنند و‬                        ‫بدان بی‌بها ناسزاوار پبوست‬
‫دکرمان نهند و بیندازند و بدان‌سبب ناوک‬          ‫پدید آمد آوای دشمن ز دوست‬

                         ‫خوانند» (صحاح)‪:‬‬        ‫(‪)۱-۴۶-۲۲۳۲‬‬
                                                                                       ‫ناسود‬
              ‫سپهرم به ترمذ شد و بارمان‬
                                                                          ‫نهآسواده نیاسود‪:‬‬
   ‫ازن‬
     ‫کستم ا‬
          ‫بکرهدار ناوک بج‬
‫‏)‪(£V1-F۶-F‬‬                                                ‫فریدون چو بشنید ناسود دير‬
                                       ‫ناهار‬    ‫کمندی بیاراست از چرم شیر‬
 ‫ذا[زنشانة نفی ] آ‪+‬هار [مبعهنی خورش]‬            ‫(‪)۱-۶۷-۳۳۴‬‬
                                                                             ‫والنده‬
                                                                                  ‫نالندگی ن‬
                 ‫‪-‬ناآهار‪ :‬ناخورده‪ .‬گرسنه‪:‬‬
‫کیخسرو داستان نبرد را از سران سپاه‬
                                                               ‫بیماری و بیمار (نک ناچران)‬
                                                                                      ‫نالیدن‬
                             ‫می‌پرسد‪:‬‬                                      ‫شکایت کردن‪:‬‬
=== leaf ===
leaf= 434
```


## [2026-09-07T17:42:06.668Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==435' FSF_pages.txt | grep -o \"[۰-۹]\\{2,4\\}\" | head -20\necho \"--- neighbours ---\"\nfor n in 430 435 440; do echo \"leaf $n:\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' FSF_pages.txt | tail -3; done"
}
```


### [2026-09-07T17:42:08.032Z] TOOL RESULT

```
۴۶
۲۲۳۲
۶۷
۳۳۴
۲۲۱
۶۴۳
۹۹۲۰
۱۹۳۱
۱۹۲
۲۵
۲۲۳
۸۳۴
۱۱
۱۲
۳۲۱
--- neighbours ---
leaf 430:
              ‫میوةدرحت انارمعنی می‌کند‪.‬‬                ‫کنو آشکاز‪ :‬ادال ایجد تفه ده‬
‫در شاهنامة چاپ تهران [برو خیم ] نیزکه‬

leaf 435:
                                                  ‫گیلریم‬
‫(سیاست‌نامه ‪ :)۴۵۱‬ملک انگشتری در‬                  ‫(‪۳-۶۵-۰۵۸4‬‬

leaf 440:
 ‫بنفرید بر جان ناکس گروی‬                           ‫خورش باید و نیست چیزی مرا‬
 ‫(‪)۵4-۸۵۲-۶۸۱۰۲‬‬                                     ‫(‪)۷-۵۱۳-۳۹۱‬‬
```


## [2026-09-07T17:42:11.794Z] TOOL CALL #51: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/346.jpg"
}
```


### [2026-09-07T17:42:11.813Z] TOOL RESULT

```

```


## [2026-09-07T17:42:37.171Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npdftoppm -f 346 -l 346 -r 600 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg346hi\npython3 - <<'EOF'\nfrom PIL import Image\nS=\"/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\"\nim=Image.open(S+\"/pg346hi.png\")\nprint(im.size)\nw,h=im.size\n# navak line ~ y=713/1400 of page height in the jpg preview (1400 tall?) -> use fractions\nbox=(int(0.66*w), int(0.495*h), int(0.80*w), int(0.535*h))\nim.crop(box).save(S+\"/navak.png\")\nEOF\nls -la $S/navak.png"
}
```


### [2026-09-07T17:42:40.981Z] TOOL RESULT

```
(5100, 6600)
-rw-rw-r-- 1 sfmqrb sfmqrb 3021 Sep  7 13:42 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/navak.png
```


## [2026-09-07T17:42:43.869Z] TOOL CALL #53: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/navak.png"
}
```


### [2026-09-07T17:42:43.888Z] TOOL RESULT

```

```


## [2026-09-07T17:42:51.896Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 - <<'EOF'\nfrom PIL import Image\nS=\"/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\"\nim=Image.open(S+\"/pg346hi.png\")\nw,h=im.size\nbox=(int(0.735*w), int(0.4955*h), int(0.775*w), int(0.512*h))\nc=im.crop(box)\nc=c.resize((c.width*6, c.height*6), Image.LANCZOS)\nc.save(S+\"/navak2.png\")\nprint(c.size)\nEOF\n"
}
```


### [2026-09-07T17:42:53.507Z] TOOL RESULT

```
(1224, 654)
```


## [2026-09-07T17:42:56.602Z] TOOL CALL #55: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/navak2.png"
}
```


### [2026-09-07T17:42:56.621Z] TOOL RESULT

```

```


## [2026-09-07T17:43:15.854Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY ناو ===\"; grep -n \"ناو\\b\\|^ناو\\|ناو \" incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY latin NAV ===\"; grep -n \"NAV\\|NAU\" incoming/ARY/ARY_latin_index_pages.txt | head -10\necho \"=== ARY پناه ===\"; grep -n \"پناه\" incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-07T17:43:15.931Z] TOOL RESULT

```
=== ARY ناو ===
86:نژادی بر سایرین برتری کامل داشتند. چون در آلمان و اسکاندیناوی اینگونه مردم فراوان ترند؛ آنها
95:پست‌تر از آریایی‌های ناب (یعنی آلمانی‌ها و اسکاندیناوی‌ها) بودند؛ تا چه رسد به ایرانی‌ها و
113:ارتش و فناوری وگسترش از راه کوچگری را میسر نمود. بنابراین دیدمان (17733083) مردمان این
785:اسکاندیناوی: دانمارکی» نروژی» سوئدی» و ایسلندی (با هم حدود ۲۰ میلیون نفر). کهن‌ترین متون
987:حرکت ناوگان یسونان بسوی تروا بفرستند. دو مورخ کهن» لیوی (17۷9) و پلوتارکكه
1078:کردهای پر و آسیای مرکزی وهند تا اسکاندناوی وبریتاا اسان (زیمی از آسیا وحلیا از )
1175:اوستایی و یونانی و لاتین و اسکاندیناوی» پژوهشگران را قادر کرده است که تصوی رکلی زبان هند و"
1463:معنی این واژه در زبان‌های آلمانی و اسکاندیناوی و اسلاوی: پند دادن.
9670:چم اين واژه در زبان‌های ارمنی و لاتین و گرتیکه و زبان‌های اسکاندیناوی: گونه.
10655:اسپانیایی (82۸۸18): لا یترانی (4149۷ 27 7: 81018 تناو
=== ARY latin NAV ===
1403:RADEN (DUTCH) fiche (OLD SCANDINAVIAN) :pSS-e\
1432:BARNHART: 930 4 of 7 OLD SCANDINAVIAN) (414) 4S(Setha!
1460:ILIN (BRETON) 3.5 2 HOLD SCANDINAVIAN) 45,5 42b04!
1510:REFERENCES beth OLD SCANDINAVIAN) 5.5 hes\
1527:HOLD SCANDINAVIAN) 4S.5-chs} IROE, IRON OSSETIC) ins!
1553:(OLD SCANDINAVIAN) gS guthes! AZI, AZA, AZASH, ¥(AVESTAN) (pli
1583:DELAMARRE: (NAITRE) 256 OLD SCANDINAVIAN) ¢45.s-Ley!
1603:BARNHART: (ANGST) 35, (ANGER) 34 (OLD SCANDINAVIAN) oySigh|
1656:ACKONS (OLD PRUSSIAN) oS os. 4 EGG :(OLD SCANDINAVIAN) gySisccheu!
1697:Ivr-$1d savas ubcd | ~ OLD SCANDINAVIAN) -pSLa!
=== ARY پناه ===
```


## [2026-09-07T17:43:17.509Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW navis ===\"; grep -n \"navis\" LEW_1910.txt | head -5\necho \"=== LAT navis ===\"; grep -n \"nauis\\|navis\" LAT.txt | head -8\necho \"=== SKT navy/noise ===\"; grep -n \"^Navy\\|^Noise\\|^Nautical\\|^Nausea\" SKT.txt | head -8"
}
```


### [2026-09-07T17:43:17.615Z] TOOL RESULT

```
=== LEW navis ===
=== LAT navis ===
2248:sens de actuarius dans actuaria nauis, et 1'adverbe SctUtum, q.u.), et
9852:sans doute carpasia Isid., Or.19,1,11, - nauis a Carpatho insula nomi¬
11010:celundrla, cellndrla (Gloss.): nauis, quae uelociter currit. Lire
12778:-a nauis: sorte de bateau de bois usite sur le Tibre, d'ou codicarii
16748:Cu.«44, lien dierectus est; Men.443, ducit lenbu* dierectum nauis prae¬
28811:lancer par dessus bord" iactum mercium facere leuandae nauis causa,
34602:M.1.5119. En iri. long, gall. llong, de longa ( nauis ), "vaisseau".
40514:cf.Svennung, Untersuch.z. Pallad.973, et confirmee par les 1 . romanes,nauis
=== SKT navy/noise ===
12410:Noise.  (F.-L.-Gk.  \)  M.  E.  noist.~ V.  Hoist,  O.  F.  nose,  a  debate,  quarrel, noiie  Cf.  Prov.  noisa,  nausa,  nun'ut. p.  Diez  holdn  that  it  can  only  be  derived from  L.  nausea,  &ea-sickness,  disgust,  hence annoyance,  Stc. ;  the  L.  word  being  bor- rowed from  Gkl  See  Nauaea.  >.  Some attempt  to  derive  il  from  L.  noxia,  barm, put  for  m>xa,  harm;  see  Noxioua.  (Di:«- putcd ;    bcc    Uicx,  Schelcr^  laltre.)     Der.
```


## [2026-09-07T17:43:25.043Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW ===\"; head -3 LEW_1910.txt; grep -n -i \"nāvis\\|navis,\" LEW_1910.txt | head -5\necho \"=== LAT headword ===\"; grep -n \"^nauis\\|nauis,\\|nāuis\" LAT.txt | head -5\necho \"=== SKT nausea/nautical/navy ===\"; grep -n -i \"Nausea\\.\\|Nautical\\.\\|Navy\\.\\|Nautilus\" SKT.txt | head -8"
}
```


### [2026-09-07T17:43:25.117Z] TOOL RESULT

```
=== LEW ===
eae hee ne
ee
Duquesne University:
=== LAT headword ===
2248:sens de actuarius dans actuaria nauis, et 1'adverbe SctUtum, q.u.), et
11010:celundrla, cellndrla (Gloss.): nauis, quae uelociter currit. Lire
40553:nauis, -is f. (ac.nowim et nSuem, abi. nSui et ndue; sur 1 'existence
44031:preter; arranger, ^quiper, garnir, Smare nauis, conuiuium, prouincids;
52762:nauis in asse", P.F.34i,a; ratSrius, cf. plushaut.
=== SKT nausea/nautical/navy ===
12185:Bupomatural.   (L.)    From  L.  suptr, bevond,  and  naiurai,  adj.  from  tiaturt. ivatlon,  Native,  Natiire  ;  see  HataL Naught;  »ec  ZVo  (i). Nauseous,  Nautical ;  see  Nav*  (a). Nautilus,  Naval ;  see  Nave  (a). Nave  (0,    the  liub   of  a  wbeeL   (E.) M.  E.   naue  {w^v).     A. S.  tta/u,  nafa.^ Du.  naa/t  Iccl.  nif/t  D.in.  nav,  S\red.  naf. G.  w*Stf ;  Skt.  nddki,  the  nave  of  a  wheel, navel,  centre,   boss,   from  nabh,  to  burst oat.     (VNAUH,)
12189:nautloaL  (U^Gk.i  FiomUfujuiuw, nautical. —  Gk.  vatmit6tf  pertaining  tosh ip«. —  Gk,  >«i?-f,  a  ship.
12190:nautilus,  a  sbell&sh.  (L.  -  Gk.)  L. iMw/iVitf.  — Gk.  I'avWxof.  A  seanum ;  aUo tbenautilos  ^from  its  sailing). *Gk.  rav-s, jhi|>.
```


## [2026-09-07T17:43:37.484Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '40553,40575p' LAT.txt\necho \"=== BRT navaza attempts ===\"\ngrep -n \"navaza\\|nävaza\\|nävaya\\|navaya\" BRT.txt | head -10\necho \"=== BRT col 1047 area ===\"\ngrep -n \"1047\" BRT.txt | head -5"
}
```


### [2026-09-07T17:43:37.557Z] TOOL RESULT

```
nauis, -is f. (ac.nowim et nSuem, abi. nSui et ndue; sur 1 'existence
d'une forne monosyllabique nau(i)s dans Enn. et Pl., voir Lindsay,
Early lat. Verse, p.142): navire, vaisseau. Terme gen 4 rique. _ Ancien
(Columna Rostr., Liv. Andr. ), usuel.
Deriv 4 s et composes: ndudlis'. naval; d'ou naudle,-is et nau&lia,
-ium n.: arsenal, chantier maritime (= Tot vewpia);
nduia,-ae f.: doublet populaire de nauis , i° conservi avec le sens
de "vaisseau" dans le non du jeu aut caput ( capita, caputa) aut
nauiam correspondant a notre "pile ou face"; a° panier de vendangeur
en forme de vaisseau, cf. F.168,30, et P.F.i6y,y;
nauicula (naucula), nauicella (naucella) f.: barque; naudJculor,
-aris (Mart.);
nduiculdrius (~ris): concernant le commerce maritime ou 1'armateur;nausci t
- 7 66 -
subst* n 8 u(i)cul&rius, nauclSrius m. "armateur 11 , nciuicularia f• n raetier
d f armat eur ,r • N auc l ar ius est sans doute une forme 1 at inisse de votu—
HXripoC, munie du suffixe —arius» Sans rapport avec nuuicula}
l r epenthese de 1 } u est la meme que dans Hercules 5
nduigd, -as: naviguer (cf. remigd, litigo, etc.), et ses derives navigium.,
-giolum-, nSuigator, -ti 5 , navigabilis et innavigabilis, cf .7tXeucm>c6c
et auXeucrroc; ad-, S-, in-, prae-, praeter-, re-, sub-, trans-nauigo-,
pernS.uigd.tus,
naviger, nauiuorus (po 4 t.).
=== BRT navaza attempts ===
5048:Schlacht  gehefert"  Bh.  j.3;  usw.  c)  be- gründend 'aus  den  angegebenen  Grün- den, folglich,  in  Folge  dessen'**:  paurvB yat  ditn  usca  usdvanayat  .  .  %raitaonö  .  . hS  °%a  vazata  %ri.ayar3m  ", .  der  schwebte in  Folge  dessen  .."  Ytj.öiC;  —  ai-a •  ].,  p.  ava'^a  Adv.  I)  'de,  ita';  1)  ver-  ait)m  nmä/am  baraytn  °%a  iriststn  hirt- gleichend  'so,  ebenso';  ein  Nebensatz  mit  zayin  "so  sollen  sie  die  Behausung  weg- y<^a  'wie'  geht  voraus  oder  folgt:  l_>'a;ia-  tragen  (und)  folglich  den  Toten  dalassen" sam  ..  ahaAya^  '^ä  *aiunavaya"i3  Bh.  V.  Ä  3;  a;  —  vTspe  fyrisfnti  pinnine 1. 8;  —  yd^a  .  .  hvanxhStm  .  .  fraca .  »&«  mOvayacit  .  .  tinsttUu  (sd.)  YL  14. aiti  ahvica  vazaite  ..  °^a  az»mHf  ..  a/a-.^Z.  4)  'desgleichen,  item';  pagtryäi säniYtio.iiS; — }ydh3 paruvamay  °%ä' mdarftayfn{sA)  af^nitäyukim  °>a  ätrpm Bh./,i4';  4.4,5.2;  —  \- iyam  yuviyS  {sA.)  V.J5.48;  —  mairyS  drva  bizangrB  "äa akäniy  *°^<J  *ya'iä  adam  niyastäyam  D.  ahmaoys  V. 5.35;  — JvS  nanm  ..  Jainli i-/.y,  — yimö  °'^a  kmnaot  yaia  dim  nsit  ''ha  m^nts  V.J. 37;  38;  —  ä'hrö *iiasaf  ahurö  V.  2.32;  i8.-t,t,  35,  38,  ir).  ahurake  . .  °^a  näirikayäi  V.  15.45  Gl.; 33.  a)  vorausweisend 'folgendennassen,  Vd.  2.  11) 'in  einem  solchen  Fall,  unter alio'-.lhauv  karahy3 'hä  adurußyt^  adam  solchen  Umständen':  yat  ..  spä  ahqm.- hardiyc^  amiy  Bh./.ii;  16,  2.3,  5,  ^.x'^}  baöhimtöS  vä  bavaf..°'ha  Al baeidz^m(sd.) 1.16,  2,14,^.5;  —  y-UOT  (sd.)  ..  aduru-  .'.  upi^isayffi  Y. IJ.35;  15.48.  in)'dort's'; jiya*  -hiJ  a%ah<^  adam..  amiy  Bh.  b— j';^,fs  'ha  dasiam..vlbarai  aHaisva  var>ßva 4.29;  —  '^äidiy  a>aAam  paraidiy  "so .  "wer  hat  dort  die  Rehgion  verbreitet..?" befahl  ich  ihm;  'Zieh  aus  . .'"  Bh.j.3;  V.  2.42;  39.  [Vytj^:  lies  'S«".] 9,  14,  2.6,  7,  10,  14;  —yadiy  '%a  *mam-  Ableit.  —  Eig.  'auf  jene  Weise'.  —  wo*s. yüAay  hacä  aniyanä  mä  tanam  D.5.3;Bh.  |  "^ä.  —  Pü.:  ää«,  (mV.  3.  42):  fiar^ 4-l'A — "''^  °^^  marthanS:  ..  Yt.lp.47;  — AS'':ba  vyaxmanyala:..  Yt/p.43-  a)  mit folgendem  _j'fläa  oder^ai  'insofern . .  als
7279:charakterisirenden  Adj.  (sd.,  auch  fdSt.): vispasca  äpS  yazamaide  ya  z)m3  armaesta (sd.)  *fratat.ear3tasca  (sd.)  *xqnyk  '^raots.- stälasca  par^uya  *v3iryäsca  (sd.)  "alle Wasser  auf  der  Erde  . , :  die  stehenden  und fliessenden,  die  in  Quellen  und  in  Fluss- laufen,  die  Schnee-  und  Regenwasser"  Y. 61^.6;  usw.;  —  vJspä  apd  xä  pttiti '^raotS.- stSiasca  Y.yi.g;  —  sps yal  armal^tayä.. yat  cätayä  uzuityäsca  .  .  yat  sna^ntyaica srasUntyaica  . . yat ß^tat.^antayä'W .  6.^0, 33i  36,  39;  —  äpim*  tacintqm  . .  xayanqm .  .  zrayanqm  .  .  artmaistqm  Yt.6.2;  Y.ig. 26,  Vd.4;  —  caval  nä  apa  (statt  DS.) ''frälat.cartte  .  .  paiti.iaräi  .  .  cval .  .  ape armaisfaya  (statt  DSf.)  .  .  nävayayai  tia ape  ..  ti.66(.;  —  apqm  ..  nävayaiiqm (sd.)  paiti  pintüs  Yt  //.  4 ;  usw.;  —  andvim . .  ye^he  avavat  .  .  äps  lata  (sd.)  ava.- barmle ya%ia  ..  Yt.5.15;  Ä.47; — gairil yS  uiiiä  yim  aiwiid  paoiris  äpS  hqm  gairi- ü(/('(sd.)/(WJ«/JYL/9.66; — spim  laokmta' vaitim  zaranyävaitlm  vihusavaifim  (sd.) V.^.54;  —  ap3mca  haomyqm  {sA.)  Y.  22. 2;  usw.;  — yaSsyatitim  äp^m  *pararihät Y.g.ii;F.4 f.,  V.21;  —  ?iqm.taptibyB  aiwyS caxrare(sii.)  n^r^bydY.  4.46; — apU  ai yaza- maide malkaintllcä  (sd.)  * hsbavaintlicä  . . Y.JÄ3«.  C)  GP.  apqm  mit  napat-m. (sd.,  auch  fdSt.)  Name  einer  Gottheit: apqm  napäs?  tä  apff  ..  vliax/aiti  YtS. $4; usw.  2)  von  bestimmten  Flüssen  oder Seen,  'Gewässer':  andvl  (sd.)  nqrna  äpa (NS.)"'  V.  7. 16;  —  n?mS  artduya  aps  anü- hitaya  Yt  r.  2 1 ;  Y.  6$.  i ,  Ny.  4.  o.  Vr.  1. 5 ; —  *atikäs^a  (näml.  artduyä)  mS *aaatiAä aps  apayiarsY .  65.  i;  5;  —  upa  äp.'myqm vltaaukaittm  Yt5,76;  —  njinB  ape  däit- yayä  (sd.)  Yt./.2i;  5.112,  5,29,  /7.61, V, ig.2;  —  aoi  apjm  yqm  raiakqm  (sd.) Yt.5. 63;  —  haca  apat  kqsaeyät  (sd.)  Yt ig.92,  V.ig.$;  —  a/s  ya  aw^änva  nqma Yt  ig.  62;  —  yazäi  äp^m  frazdänaom  F. 4%.  I,  2  Anhang:  apqm  (näml  ayar^y
10708:•  j.  xsao9ah-  n.  'Fluss,  Strömung,  Wasser- Schwall';  airy!>.layamm  .  ,  yahmya  äpu navaya  .  .  °taipha  %waxhnle  Yt  10. 14.
10906:•  ).,  g.  'xänav-  V.  'Genüge  haben  an  — , leisten  in  — '.  Praes.  i  xs'nu-,  5  kuxsnu-, 16  (Des.)  cixsfiusa-,  17  (Fut.)  xsnaolya-, 30  (Iter.)  xinävaya-;  J-Aor.  i  xsnaos-, 2  x/tovis:  —  PPfP.  xskuta-'^;  PFP.  xsnao- %wa';  Inf  x/nümaine,  xsnao^räi.  S. noch  ax/nus/a  und  kuxsnBsa.
12048:—  hin,  Über  —  hin,  über  —  hinweg';  a)  räum- lich: bis  Aapta  pfsavB  fraoirisysit  {sA.)  f ap3  nävaya  V.  i4'  16;  j5.  74;  —  UMayara uzXra  hvar)xlaita  .  .  t°  harqm  bimaitlfn V.  21.  $;  Yt  70.  118;  —  'ia  a/aunam urvänS   t°    harqm  .  .  *amaoiti  V.  ig.  30  j
12447:daenävazab-
13151:ahmai  raes^a  x^annasca  .  .  dayata  (aP.) vatauhis  apö  tnavayala  zao%re  .  .  ahma- k?mca  mazdayamanqm  .  .  halqmcd  V.  GS, 1 1  f.  b)  II  im  Ap, :  aitJ"  adam  J'urt^-
16161:•  j.  paranävayam-  f.  'vollkommene  Ab-  •  ]■  'paäana-  n-,  p«äaiüi-  f.  'Kampf, Wendung,  Abbitte':  -^J  (NS.)  F./o.  Schlachf:  nivanäat(sd.)  apaydH  [..]  "«a
18863:j.  näuya  Yt  l6.  3:  lies  nävaya.
18894:•  3.  nävaya-  Adj.  (fem.  °ya-)  'schiffbar',  Be- zeichnung fli essenden  Wassers  von  grösserer Breite  und  Tiefe:  airysJayatam  ..yahmya apö  'y&  p^n%wi/  XiaoiartAa  %waxi?nU Yt  10. 14;  —  . .  'hraotS.siacS  apa  taänä 'yä  Yt/J.  ro;  — pxavS /raoirisyBti  tarasca apB  'ya  (APf.)  V.  14. 16;  7<y.  74;  —  tyaäa *nä  buyat . ,  hupirihwe  a/s*'ya''>  Yt.i6.y,
=== BRT col 1047 area ===
18686:n>r)sasärahya'Y.2g.q;—y/ln)rqi{kV.) sadra  (sd.)  dngvats  Y,45.7;  zit  Vr.JiS2, G.3.6  undP.^.ü',  wo  nar/'**;  —  yönari dngvatä  urva  H.  2.  25,  a6,  33;  Nik.  3, Vd.  13,  75;  —  besonders  häufig  mit  asa- van- (Sp.  250  na.;  s.  auch  Sp.  1047  m,, 1049  o.):  yat  ba  paiti  nä  asava  nmansm uzdasia  y.3.2;  1,  Yt/0.  lao,  11.3;  — yetihe  ''nmävya  srao^S ..näca  aSava  fräyS.- kumats  Y.57. 14;  —  ydi  narS  afavanB kumataiS  mainimna  ..  Y.  70.  4;  V.ig.ig, 34,  Vd-g;  —  *^ripiäwff (sd.)  .  .  asti  atari .  .  a%a  narB  alavanS  F.sjb;  Yt/^.zs;
```


## [2026-09-07T17:43:46.608Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Schiffer\\|Schiff'\" BRT.txt | head -10\necho \"=== col numbers near 18894 ===\"\nawk 'NR>=18880 && NR<=18900' BRT.txt | grep -o \"Sp\\. [0-9]*\" | head"
}
```


### [2026-09-07T17:43:47.881Z] TOOL RESULT

```
16038:•  j.  päurva-  m,  EN,  eines  Mannes*':  tarn (näml.  artdvJm)  yazala  'vö  yd  vifr3  tiai'äzB yat  dim  usca  uzdvqnayat  .  .  %raitaoiid rrunyahe  kshrpa  ka'hrkasahe  ".  .  P.,  der kundige  Schiffer  . ."  Yt.  3. 6 1  ">.  [S.  noch *atvs.gava-  No.  4.]
18669:•  j.  naväza-  m.  'Schiffer*:  paurvS  (sd.) yS  vifrS  'a  Yt5.6i;  Az.4,  VyL2.
=== col numbers near 18894 ===
Sp. 
Sp.
```


## [2026-09-07T17:43:57.246Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9h%E2%82%82us",
 "prompt": "Reconstruction of PIE *néh₂us: meaning, declension, and the list of descendants (Indo-Iranian, Hellenic, Italic, Celtic, Germanic, Armenian). Quote the reconstruction note."
}
```


### [2026-09-07T17:44:02.860Z] TOOL RESULT

```
# Proto-Indo-European *néh₂us

## Meaning
This reconstructed term refers to a **boat**. According to the etymology section, it originated as "an agent noun originally meaning 'swimmer, that which swims'" derived from the root meaning "to swim."

## Declension
The word exhibits complex inflectional patterns. The page notes that "The inflection found in Ancient Greek and Sanskrit does not correspond to the traditional ablaut patterns of PIE and probably represents a later levelling or reinterpretation." Two alternative paradigms are proposed—an athematic hysterokinetic form and an athematic amphikinetic form—reflecting scholarly uncertainty about the original declension system.

## Descendants
The term produced reflexes across major Indo-European language families:

- **Italic**: Latin *nāvis* (ship)
- **Hellenic**: Ancient Greek *naûs* (ship)
- **Indo-Iranian**: Sanskrit derivatives
- **Celtic**: Old Irish *nau*
- **Germanic**: Old Norse *nór*
- **Armenian**: Old Armenian *naw*

These widespread descendants demonstrate the ancient pedigree and importance of this maritime vocabulary across Indo-European societies.
```


## [2026-09-07T17:44:12.438Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/ناو' --note 'page 346, root Na 1/Nau, node 2: Persian nāv etymology MP nāw < OP nāva < PIr *náHuš < PIE *néh₂us, senses ship/gutter/channel' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/پناه' --note 'page 346, root Nâ 2, node 2: Persian panāh < MP panāh' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/𐭯𐭭𐭠𐭧' --note 'page 346, root Nâ 2, node 1/2: Middle Persian pnʾh panāh protector/refuge' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/नाथ' --note 'page 346, root Nâ 2: Sanskrit nātha refuge/protector < PIE *h₃neh₂- to help, cognate Gk onínēmi' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/noise' --note 'page 346, node 8: English noise < OF noise < L nausea (vs noxia), OED doubts both' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/néh₂us' --note 'page 346, root Na 1/Nau/Naus: PIE *néh₂us boat, descendants Lat navis, Gk naus, Skt nau-, OIr nau, ON nor, OArm naw' 2>&1 | tail -3"
}
```


### [2026-09-07T17:44:16.626Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4e504ce1a50b91a2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/35536be03df12a46.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/19c6d243e8c2263c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f87ba4e6ae376a0a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/070c9e52426f7efa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cb2d58ce8427c817.txt
```


## [2026-09-07T17:44:24.022Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg346.png data/verification/sources/refs/ocr/BOOK/346.png\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/navak2.png data/verification/sources/refs/ocr/BOOK/346-navak-zoom.png\nls -la data/verification/sources/refs/ocr/BOOK/ | head"
}
```


### [2026-09-07T17:44:25.317Z] TOOL RESULT

```
total 15716
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  7 13:44 .
drwxrwxr-x 12 sfmqrb sfmqrb   4096 Sep  6 18:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-07T17:44:28.362Z] TOOL CALL #64: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-07T17:44:28.416Z] TOOL RESULT

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


## [2026-09-07T17:44:53.773Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD onin ===\"; grep -n -i \"oninemi\\|onin\\|nātha\" AHD_watkins1985.txt | head -5\necho \"=== IEC na- help ===\"; grep -n \"nāt-\\|nātho\\|nāthos\\|‘help’\" IEC.txt | head -10\necho \"=== SYN help ===\"; grep -n \"nātha\" SYN.txt | head -5"
}
```


### [2026-09-07T17:44:53.849Z] TOOL RESULT

```
=== AHD onin ===
356:dail-. To divide. Northern Indo-European root. 1. Ger- manic “dailjan in Old English d%lan, to share: DEAL. 2. Germanic *dailaz in Old English dal, portion, lot: DOLE!, 3. Germanic prefixed form *uz-dailjam, “a por- tioning out,” judgment (*uz-, out; see ud-), in Old English ordal, lot, apportionment: ORDEAL. [In Pok. da- 175.]
644:Latin cinctari, to delay: cuNCTATION. [Pok. kenk- 566, konk- 614.] konk(h)o-. Mussel, shellfish. 1. Greek konkhé, konkhos, mussel, conch: COCKLE!, CONCH, CONCHA, CONCHO-. 2. Greek kokhilos, land snail: cocHLEa. [Pok. konkho- 614.] kormo-. Pain. Germanic *harmaz in Old English hearm, harm: HARM. [Pok. ormo- 615.] koro-. War; also war-band, host, army. I. Germanic *harjaz, army. 1. Old English here, army: HERIOT. 2. Old French herban, a summoning to military service: ARRI- ERE-BAN. 3. Compound *haryja-bergaz, “army hill,” hill- fort, later shelter, lodging, army quarters (*bergaz, hill; see bhergh-?), in: a. Old English herebeorg (> Middle English herberwe), lodging: HARBOR; b. Old French herberge, lodging: HARBINGER. 4. Compound *harja- waldaz, “‘army commander” (*wald-, rule, power; see wal-), in Anglo-Norman herald, herald: HERALD. II. Ger- manic denominative *harjén in Old English hergian, to ravage, plunder, raid: HARRY. III. Germanic compound *harihring, assembly, “host-ring” (*hringaz, ring; see sker-3), in Medieval Latin harenga, harangue: HA- RANGUE. [Pok. koro-s 615.] koselo-. Hazel. Germanic *haselaz in Old English hesel, hazel: HAZEL. [Pok. kos(e)lo- 616.] kost-. Bone. Probably related to ost-. Latin costa, rib, side: COAST, COSTA, COSTARD, COSTREL, CUESTA, CUTLET; ACCOST, INTERCOSTAL, STERNOCOSTAL. [Pok. kost- 616.] krau-. Also kru-. To conceal, hide. Suffixed extended form *krup-yo- in Greek kruptein, to hide: CRYPT, CRYP- TIC, CRYPTO-, KRYPTON; APOCRYPHA. [Pok. krd(u)- 616.] kred-. Framework, timberwork. Possible root. Germanic *hr6(d)-st- in Old English hrést, roost: Roost. [Pok. kred- 617.] krei-. To sieve, discriminate, distinguish. 1. Basic form with variant instrumental suffixes in: a. suffixed form *krei-tro- in Germanic *hridra-, a sieve, in Old English hridder, hriddel, sieve: RIDDLE}; b. suffixed form *krei-dhro- in Latin cribrum, a sieve: CRIBRIFORM, GAR- BLE. 2. Suffixed form *krei-men- in (i) Latin crimen, judgment, crime: CRIME; RECRIMINATE (ii) Latin discri- men, distinction (dis-, apart): DISCRIMINATE. 3. Suffixed zero-grade form *kri-no- (participial form *kri-to-) in Latin cernere (past participle certus), to sift, separate, decide: CERTAIN; CONCERN, DECREE, DISCERN, EXCRE- MENT, INCERTITUDE, RECREMENT, SECERN, SECRET. 4. Suffixed zero-grade form *kri-n-yo- in Greek krinein, to separate, decide, judge (> krinesthai, to explain): CRISIS, CRITIC, CRITERION; APOCRINE, DIACRITICAL, EC- CRINE, ENDOCRINE, EPICRITIC, EXOCRINE, HEMATOCRIT, HyYPrROCcRISY. [Pok. 4. sker-, Section II. 945.] krek-1. To weave, beat. 1. Germanic *hreh-ulaz in Old English hréol, reel, spool for winding cord: REEL. 2. Suf- fixed o-grade form *krok-u- in Greek krokus, nap of cloth: CROCIDOLITE. [Pok. 1. krek- 618.] krek-2. Frog spawn, fish eggs. Germanic *hrog- in Middle English row, roe: ROE}. [Pok. 2. krek- 619.] krem-. Wild garlic, onion. O-grade form *krom- in Ger- manic *hram- in Old English hramsan, onion, garlic: RAMSON. [Pok. kerem- 580.] kret-'. To shake. O-grade form *krot- in Germanic *hra- thaz, swift, nimble, in Old English hreth(e), nimble, quick, prompt, ready: RATHE, (RATHER). [Pok. 1. kret- 20.
1102:ud-. Also Gd-. Up, out. 1. Germanic *it-, out, in: a. Old English at, ovuT; utmost; b. Old High German az (> German aus), out, in German garaus, “all out”: CA- ROUSE; AUSLANDER; C. Old Norse at, out: OUTLAW; d. Middle Dutch ute, uut, out: UITLANDER; e. Middle Dutch dteren, to drive away, speak out: UTTER}; f. Ger- manic suffixed (comparative) form *it-era- in Old Eng- lish dtera, outer: UTTER?; g. Germanic compound *bi-iitana (*bi-, by, at; see ambhi), “at the outside,” in Old English bitan, biite, outside (adverb): BUT; ABOUT. 2. Extended form *uds in Germanic *uz, out, and prefix *uz-, out, in: a. Old High German ir-, out, in irsezzan, to replace: ERSATZ; b. Middle Dutch oor-, out: ORT; c. Ger- manic *uz-dailjam, “a portioning out,” judgment (see dail-). 3. Suffixed (comparative) form *ud-tero- in Greek husteros, later, second, after: HYSTERESIS, HYSTERON PROTERON. 4. Greek hu- in compound hubris, violence, outrage, insolence (bri-, perhaps “heavy,” “violent”; see g”era-?): HUBRIS. [Pok. d- 1103.]
2212:SAPID sep-1 SAPIENT sep-1 SAPONACEOUS _ seib- SAPONATE seib- SAPONIFY seib- SAPONIN seib- SAPONITE seib- SAPOR sep-! SAPROBE gWei- SAPSAGO skep- SARCASM twerk- SARCO-  twerk- SARCOCARP twerk- SARCOID twerk- SARCOLEMMA lep-1 SARCOMA twerk- SARCOPHAGUS twerk- SARCOPTIC MANGE skep-, twerk- SARCOUS twerk- SARDONIC sward- SARDONYX nogh- SARMENTOSE serp-1 SARTORIUS serk- SASTRUGA ghd, ster-2 SATE! sa-
=== IEC na- help ===
3816:oregó, ið “stretch forth, extend, rule’. WP II, 362. Cf. reg-, reg- Skt. irajyāmi “lead, rule, extend’; Gk. orégó; Lat. cf. rego beside é-rigo; MIr. éirgim ‘rise’; OS cf. rekōn ‘arrange’. (Gk. arégo ‘help’ is prob. to be analysed are- ‘good’ + ágo)
6443:ieuaio ‘ease, relax, benefit, aid’ Per. cf. yavar ‘helper’; yàvari, s. ‘help’; Gk. eåð “allow, leave’; Lat. cf. juvo, are ease, benefit, help, delight
8533:Kak-, Kakt- (or Kok-, Kokt-) “arrange, com- pose, fit Skt. Saknómi “help; be fit, be able’; Saktih, f. ‘help’; Av. sač- (2) ‘befit; Ober, cf. 0akata-, pp. ‘completed’; ON hagr, hogr ‘fitting’; haga, v. “arrange”; háttr (' manner”, fr. *hahtuz); OE hagian, O.Fris. hagia, OS bi-hagon, MHG hagen (w. dat. “please, suit). Cf. also OHG
14435:régü, ið (regs-?) “see, observe". Cf. WP II, 366. (Variant rüg-) Gk. cf. a-régo, v. (^help, save’, fr. *sm-?), cf. a-rogé, f. ‘help’; o-gde: OHG ruohh, MHG ruoch, sm. & f. ‘care’; OHG ruohhen, OS rokian; OE recan, ON rækja, v. ‘care’. Cf. rüg- below. (Uncertainly Skt. laksámi “note, observe); (short vowel in) Li. reen eti, v. ‘see’; Latv. regu, redzēt, v. id. beside (long- gde) rēgs, m. “vision, ghost: (short o-gde in) R róZa, f. *grimace' (here?)
14672:Gk. arðgós, -é, mf. ‘help’; arogós, adj. “help- ful; helper’; MHG ooch, ruoche, sm. & sf. ‘care’; OHG ruoh, ruohha, id.; LG ráuk, m. ‘reason; order; care’; ráuken, v. ‘handle, manage'; cf. G ruchlos, Du. roekeloos 'reck- less’. (Not in OE thus)
16628:segh-, segh-). WP II, 481 Arm. agi, gs: agvo, s. (tail, lit. "holder", cf. also agujc, gs: aguci, s. “holder, setting, clasp, joint, staple’ beside (?) b-ognim, v. ‘be tired”; MHG sacke, sagge, wm. (“common land”, lit. ‘holding’, but see sogh-); Slovak cf. o-soh m. ‘use’; Li. saga, f. “button, clasp, buckle’; sage, f. ‘brooch’. Ambig. are Skt. sahah, adj. “mighty”; sahyam, n. ‘help’, but prob. *sogh- in view of Av. hazaoSo, adj. (agreed', fr. *sogheusio-); cf. however soghuros below. Long-gde in OCS po-sagü, m. ‘fetter; marriage’; po-sag- noti, inf. join; marry’. Ambig. also in Myc. -oko-, cpds. ‘holder’; Gk. okheüs, m. “holder, clasp, thong, bar’; okhós, adj. ‘firm, secure?
16632:sogh- (alternative form of type sogh-, sce segh- and segh-). Cf. songh- Skt. cf. sahyam, n. ‘help’; Av. cf. hazao$o, adj. ‘agreed’, Myc. oko-, m. “holder? beside Gk. ókhma, n. & okhmé, f. id.; ókhanon, okháne ‘handle’; MHG sagge, sacke, wm. (common lang’, lit. holding")
16725:panion, tracker, track, procedure”. Cf. sequ- (1), soqu- (1), etc. Skt. sakkah, sakkih, m. ‘companion’; Av. haxa, nom. sg. m., pl: haxaya, id.; Ober haxa-, cpds. id.; Gk. ópson, n. 'food eaten 'cum pane"; cf. opúō and opüio, v. “marry” beside a-Ossæð, v. ‘help’; Lat. cf. socius, m. 'com- panion, ally; OS seg, i-st., OE secg, ON seggr, pl. -ir, m. ‘man, warrior’ (fr. *soquís); OCz. cf. sok, m. ‘rival’. Here also Av. haxo, m. ‘sole of foot’; Arm. ak, Let, leg’; Phryg. (DW?) sükhos, m. “sandal; Lat. (LCW?) soccus, gs: A. m. ‘shoe, sandal’
17454:Sthá- (stho-) radical element of many of the following entries, cf. | Skt. sthah, m., sthā, f. adj. ‘standing’; sthás, mn. id.; cf. upa-sthah, -stham “vulva, anus; Av. upa-sta, f. “help; vulva’; OPer. upa-sta ‘help’; Hes. cf. opa-stó- ‘supply’; Hitt. sta-, ista-; Gk. -sthai, fut. inf. ending, beside -sta in apó-sta! 'remove?; cf. pó-sthe, f. “penis, foreskin’ beside pó-sthon, m. boy’, whence Lat. puttus via Etrusc.); Lat. sta! imperv.; stare, inf.; Ir. cf. fo-sadh, s. (crest, repose’, fr. upo-5); beside fo-tha, pl. fo-thaí *founda- tion’; W saw, m. ('stop, stoppage’, fr. *sthà-); Go. cf. usstass, f. ‘insurrection’; Li. cf. at stas, m. “distance”; Slavonic sto-, sta- passim. WP II, 606
19757:uär- (3) “strength, force, violence; strong man, champion'. Gk. forms ambig. . Gk. cf. Arés, gs: eps, m. “Mars? beside arë, f. (violence'. Ambig.); cf. also aré-go, v. ‘help’ (if fr. aré + ágo); Gk. (cpd?) Héros, Doric -à-, m. ‘hero’; W gwawr, m. id.; Illyrian (Lat.) cf. Varro, onis, m. ‘robber’; ME warr(e) ‘war’; Du. war, f. ‘confusion’; cf. G Wirr-warr, id.; (LW in Fr. guerre); R vor, m. ‘thief; Li. vara, f. “force, violence’; varu, adv. “by force’; Latv. vara, f. ‘force’; varu, ét, v. ‘be able’; varen, adv. 'mightlily very’; varonis, m. (hero'. Lat. baro, onis is said to be a variant of type varo, m. (1) ‘fool’; (2) *mercenary?)
=== SYN help ===
```


## [2026-09-07T17:44:59.209Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^nā\\|nāthos\\|nāt-\\|nātos\" IEC.txt | head -20"
}
```


### [2026-09-07T17:44:59.258Z] TOOL RESULT

```
11512:nāk- (naks-) (3) ‘come, arrive, reach, suf- fice’ Lat. cf. nanciscor, nactus, v. “find, get, reach’; OHG gi-nuogi, -nuog, adv. ‘enough’; OE nog, noh, id.; nogian, v. abound"; Big. cf. nax, prp. (towards < *nàks-); Li. nokstu, nokti, v. (‘mature’, lit. arrive); pra-noku & -nokiu, -ti ‘catch up’; Li. nāku, nākt ‘come, happen. (Un- related are Av. nãs- (2) ‘reach’ and OE nugan, 3s: neah ‘suffice’, cf. neks- ?nequ-)
11523:nām, sentence particle “but, or’. Cf. na Skt. nàma; Lat. nam; cf. quis-nam; OCS ng, cj. "but
11554:nāustos, à, ios, iom, io (nàut-, nauit-) “float, fleet, floating bird or object? Gk. cf. nésos, f. “island”; n&ssa, f. ‘duck’; Lat. cf. nautea 'bilge-water; Gallo-Lat. nausum (kind of boat’. Phonol. of Lat. LW nausea); OBr. (queried) -naued ‘boats’; Br. nued, nóed, pl. -u & nueZu, m. ‘roof gutter’; ON cf. naust, n. ‘boathouse’
16535:snātos, à (1), iə ‘twisted; twine, twist'. Cf. snaio (1). WP II, 692 Mir & Ir. snáth, m., snáithe, f. *thread'; OBr. cf. not-nid, s. ‘needle’; Br. noed, m. coll. ‘thread’; W noden, pl. -i, f. id.; Cor. nosjen, pl. -nnow, coll. næs, f. id.; OE snod, f. ‘snood’; Latv. snåte, f. ‘sheet’; R cf. also snastí, f. (rope, rigging’, but cf. snast- above). Cf. sneio, néio, etc.
```


## [2026-09-07T17:52:30.661Z] TOOL CALL #67: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-346.json",
 "content": "{\n  \"pdf_page\": 346,\n  \"book_page\": 316,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Na 1, Nau, Naus\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *néh₂us (nom. *néh₂us, acc. *néh₂um) 'boat, ship' — Pokorny 'naus-1' 755–756; Watkins/AHD nau-2 'boat'\",\n      \"note\": \"The root box is correct in every respect: the reconstruction is real (Pokorny's lemma naus-1 'boat', pp. 755–756, the page Nourai cites), the language label 'Indo-European' is right, and the gloss 'boat' is Pokorny's own word. 'Na 1 / Nau / Naus' is Nourai's own three-way spelling of one and the same stem: 'Nau' is the Indo-Iranian shape (Skt. nau-, OP nāv-), 'Naus' the Greek/Latin nominative (Gk. naûs, Lat. nāvis), 'Na 1' his index label distinguishing it from Nâ 2 'to help' below. Modern reconstruction writes it *néh₂us, an old root noun (Wiktionary, following Beekes/de Vaan, analyses it as an agent noun 'that which swims/floats'). One caveat about the branch labels rather than the root: the second half of Nourai's Iranian gloss ('any groove, line, cavity or trench used as a guide for carrying water, grain, arrow') is a New Persian semantic development, not an Old Iranian meaning, and nâv-dân is a New Persian compound — see node 1.\",\n      \"note_fa\": \"جعبهٔ ریشه درست است: *néh₂us هندواروپاییِ آغازین «کشتی، قایق» همان مدخل naus-1 پوکورنی در صفحهٔ ۷۵۵–۷۵۶ است و معنای «boat» عیناً واژهٔ خودِ پوکورنی است؛ برچسب «هندواروپایی» نیز درست است. سه صورتِ «Na 1، Nau، Naus» یک ستاک‌اند: Nau شکل هندوایرانی (سنسکریت nau-، پارسی باستان nāv-) و Naus صورت فاعلی یونانی/لاتینی (naûs، nāvis) است. ریشه‌شناسی امروزی آن را نامِ ریشه‌ای کهن *néh₂us می‌نویسد و ویکی‌واژه (به پیروی از بیکس) آن را در اصل «شناکننده، آنچه بر آب می‌رود» می‌داند. تنها نکتهٔ قابل تذکر آن است که معناهای «شیار، جوی، لولهٔ راهنما» و ترکیب «ناودان» تحول فارسی نو است، نه معنای ایرانی باستان (نگاه کنید به گرهٔ ۱).\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9h%E2%82%82us\",\n        \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%88\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:755\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt l.61944ff: 'Root / lemma: naus-1 (*he-nahus-1) | Meaning: boat | Grammatical information: f. Akk. nāum | Material: Old Indic nau- (Nom. nauḥ) \\\"ship, boat\\\" (navya- \\\"navigable\\\"); ap. nāviyā \\\"fleet\\\" (: gr. νήϊος \\\"belonging to the ship\\\"); nāvāja- m. \\\"skipper\\\", Avestan nāvāza- ds. …; Avestan nāvaya- \\\"navigable\\\" … gr. hom. νηῦς, νηός, Attic ναῦς … Latin navis ds. … References: WP. II 315 … Page(s): 755-756'. Exactly Nourai's root box, on the page he cites.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Walde–Pokorny Bd. II 315 s.v. nāu- f. 'Schiff'\",\n          \"stance\": \"supports\",\n          \"note\": \"WLD_Bd2_pages.txt (grep 'nau- f.', l.20828ff): 'nāu- f. \\\"Schiff\\\". Ai. nāu- (nom. nāuḥ) \\\"Schiff, Boot\\\" (navya- \\\"schiffbar\\\"; ap. nāviya- …, av. nāvāza- m. \\\"Schiffer\\\" …, gr. νήϊος \\\"zum Schiff gehörig\\\" … lat. navis (ursprgl. kons. St., vgl. acc. navem = ai. nāvam, gr. νῆα); air. nau (g. noe) …' — the source Pokorny himself refers to (WP. II 315), same content.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985 s.v. nau-2\",\n          \"stance\": \"supports\",\n          \"note\": \"AHD_watkins1985.txt l.772: 'nau-2. Boat. Contracted from *naau-. 1. Latin nāvis, ship: NACELLE, NAVAL, NAVICULAR, NAVIGATE, NAVY. 2. Greek naus, ship, and nautēs, sailor: NAUSEA, NAUTICAL, NAUTILUS, (NOISE); AERONAUT, AQUANAUT, ARGONAUT, ASTRONAUT, COSMONAUT. [Pok. 1. nāu- 755.]' — this single entry validates the whole right-hand side of Nourai's chart (nodes 5–8). Watkins' essay (l.138) adds: 'most of the languages attest an old word for boat or ship, nau-2, probably propelled by oars or a pole'.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck 10.81 'Ship' and 10.82 'Sailor'\",\n          \"stance\": \"supports\",\n          \"note\": \"SYN.txt l.18361: '10.81 SHIP … Lat. navis, navigium … Grk. ναῦς … Skt. nāu- … Av. (navaya-, adj.) … Ir. nau'; l.18416: '1. Grk. ναύτης (> Lat. nauta), Ir. noaire, Skt. nāvika-, derivs. of Grk. ναῦς, etc. \\\"ship\\\"'. Note Buck lists the Avestan reflex only as the ADJECTIVE navaya-, i.e. no Avestan noun 'ship' — relevant to node 1.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, p. ~1000 s.v. nāustos\",\n          \"stance\": \"partial\",\n          \"note\": \"IEC.txt l.11554: 'nāustos, ā, ios, iom, io (nāut-, nauit-) \\\"float, fleet, floating bird or object\\\" … Lat. cf. nautea \\\"bilge-water\\\"; Gallo-Lat. nausum \\\"kind of boat\\\" (Phonol. of Lat. LW nausea); … ON cf. naust, n. \\\"boathouse\\\"'. Mann has no headword *nāus 'ship' at all (grep '^nā' in IEC.txt returns nāk-, nām, nāustos only), and he treats Latin nausea as a loanword from Gallo-Latin nausum rather than from Greek — a minority view against Klein and Watkins.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"nâu, nâviya; nâv-dân\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Old Persian nāv- 'ship' is the direct reflex of PIE *néh₂us and is attested (nom.-acc. pl. nāvā) on Darius' Suez stele DZe 11; Kent, Old Persian, Lexicon s.v.: 'nāv- sb. \\\"ship\\\": Skt. nāus, Gk. naus, Lt. nav-is, pIE *nāv-'. So the 'nâu' of the node is right for Old Persian. Three details are Nourai's own, however. (a) nāviya- does not mean 'ship': Kent glosses it 'fem. adj. as sb., \\\"navigability\\\", i.e. \\\"impossibility of fording the river on foot\\\"' (DB 1.86 abiš nāviyā aha, of the Tigris before Darius' crossing) and adds 'Hardly collective, \\\"collection of ships, flotilla\\\", and certainly not lsf. to nāv- \\\"on shipboard\\\"'; Horn (p.229) still glossed ap. nāviyā 'Flottille', which is where Nourai's 'ship' comes from, but that reading is superseded (Kent, JAOS 62.269-71). (b) Avestan has no bare noun nāu-: it attests only the derivatives nāvaya- 'navigable' (Bartholomae AiW s.v. '3. nāvaya- Adj. \\\"schiffbar\\\", Bezeichnung fliessenden Wassers von grösserer Breite und Tiefe', Yt. 10.14, V. 14.16) and nāvāza- m. 'boatman' (AiW: 'navāza- m. \\\"Schiffer\\\"', of Pāurva the skilled boatman, Yt. 5.61) — and Bartholomae expressly emends the one apparent nāuya (Yt. 16.3) to nāvaya ('j. nāuya Yt 16.3: lies nāvaya'). (c) nâv-dân is a NEW Persian compound (nāv + dān), not an Old Iranian word; Farahvashi (IRN, printed p.133) presents it precisely as a modern survival: 'ریشهٔ dānu در یک واژهٔ فارسی امروزی نیز باقی است و آن واژهٔ «ناودان» است که مرکب است از nāv + dān'. The second element belongs to Av. dānu- 'river' (Nourai's cross-reference ☞Dâ 2), which is correct. Verdict therefore plausible: the arrow root→Old Iranian is sound, but the glosses and the placement of nâv-dân in this box are not.\",\n          \"derivation_fa\": \"پارسی باستان nāv- «کشتی» بازماندهٔ مستقیم *néh₂us است و در سنگ‌نوشتهٔ سوئز داریوش (DZe ۱۱) به صورت جمعِ nāvā گواهی دارد؛ کنت در واژه‌نامهٔ خود آن را «ship» می‌آورد. ولی سه نکته از خودِ نورایی است: یکم، nāviya- معنای «کشتی» ندارد بلکه کنت آن را نامِ مصدرگونهٔ «قابلِ کشتی‌رانی بودن (رود)» می‌داند (بیستون ۱٫۸۶) و معنای «ناوگان» را صریحاً رد می‌کند — این معنا از هرن (ص ۲۲۹) که «Flottille» نوشته بود به نورایی رسیده است. دوم، در اوستا اسمِ سادهٔ nāu- نیست؛ تنها nāvaya- «کشتی‌رو، قابلِ کشتی‌رانی» (مهریشت ۱۰٫۱۴) و nāvāza- «کشتی‌ران» (اردویسور یشت ۵٫۶۱) هست، و بارتولومه صورتِ ظاهریِ nāuya در یشت ۱۶٫۳ را به nāvaya تصحیح می‌کند. سوم، «ناودان» ترکیبی فارسی نو (ناو + دان) است، نه واژه‌ای ایرانی باستان؛ فره‌وشی در ایرانویج (ص ۱۳۳) آن را همچون بازماندهٔ امروزیِ dānu اوستایی «رود» معرفی می‌کند. پس این گره «با احتیاط پذیرفتنی» است: پیوندِ ریشه با ایرانی باستان درست، اما معناها و جای «ناودان» نادرست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%88\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9h%E2%82%82us\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"PRT:429\",\n              \"status\": \"not_checked\",\n              \"note\": \"Partridge, Origins (1958) — no open copy exists: refs_online.json marks PRT kind 'archive_restricted' (all archive.org copies lending-only) with local_file null, so p.429 could not be read.\"\n            },\n            {\n              \"ref\": \"HRN:229\",\n              \"status\": \"partial\",\n              \"note\": \"Horn, Grundriss no. 1024 on printed p.229 (HRN.txt leaf 250, offset leaf = printed+21): 'nāv \\\"Wasserkanal; Schiffchen\\\", nāvdān. ap. nāviyā \\\"Flottille\\\"; aw. nāvāza- \\\"Schiffer\\\" (Bartholomae, ZDMG. 46, 294 Anm. 3), vergl. nāvaya- \\\"fliessend\\\"; phlv. nāvtāk (aw. nāvaya-), nāvīcak (Bund.); ai. nāv- \\\"Schiff, Kahn, Nachen\\\", vergl. nāvyā- \\\"Strom\\\". kurd. LW. nav; oss. LW. d. navā, t. nau- \\\"Schiff\\\"; arm. nav \\\"Schiff\\\"'. The page really is Nourai's source, and even carries nāvdān — but it labels only nāvāza-/nāvaya- as Avestan and glosses ap. nāviyā 'Flottille' (fleet), not 'ship'; Kent's later 'navigability' supersedes it.\"\n            },\n            {\n              \"ref\": \"IRN:123\",\n              \"status\": \"partial\",\n              \"note\": \"Farahvashi, Iranvij: the nāv-dān passage is on printed p.133, not 123 — the book's own index (IRN_pages.txt l.6772) reads 'ناودان ۱۳۳', and the running head of that page is 'نام‌های ایرانی در پیرامون دریای سیاه ۱۳۳'. Its content supports the arrow: 'ریشهٔ dānu در یک واژهٔ فارسی امروزی نیز باقی است و آن واژهٔ «ناودان» است که مرکب است از nāv + dān … «دان» بمعنای جریان آب است و بر روی هم بمعنی چیز میان‌تهی است که آب در آن جاری باشد' (IRN_pages.txt l.3872ff, pdf pages 134–135). Either Nourai transposed the digits or he used a different printing.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian, Lexicon s.vv. nāv-, nāviyā-\",\n              \"stance\": \"partial\",\n              \"note\": \"KNT.txt l.5602: 'nāv- sb. \\\"ship\\\": Skt. nāus, Gk. naus, Lt. nav-is, pIE *nāv- (§142). See also nāviyā-. [nāvā] npl. (§183.IV) DZe 11'; l.5604: 'nāviyā- fem. adj. as sb., \\\"navigability\\\", i.e. \\\"impossibility of fording the river on foot\\\": Av. nāvaya- \\\"navigable\\\", Skt. nāvyá-, adj. to nāv- \\\"ship\\\" (§144.V). Hardly collective, \\\"collection of ships, flotilla\\\", and certainly not lsf. to nāv-, \\\"on shipboard\\\"; cf. König, RuID 70-1, and esp. Kent, JAOS 62.269-71, 63.67. nāviyā nsf. DB 1.86.' Supports OP nāv- 'ship'; contradicts the gloss 'ship' for nāviya.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, AiW s.vv. navāza-, 3. nāvaya-, and the note on nāuya\",\n              \"stance\": \"partial\",\n              \"note\": \"BRT.txt l.18669: 'j. navāza- m. \\\"Schiffer\\\": paurvō … yō vifrō °a Yt 5.61; Az.4, Vyt.2'; l.18894: '3. nāvaya- Adj. (fem. °yā-) \\\"schiffbar\\\", Bezeichnung fliessenden Wassers von grösserer Breite und Tiefe: airyō.šayanam … yahmya āpō °yā … Yt 10.14; … tarasca apō °yā V. 14.16'; l.18863: 'j. nāuya Yt 16.3: lies nāvaya.' So Avestan has the boatman and the adjective, and Bartholomae deletes the only form that looked like a bare nāu-.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"Pokorny 755–756 s.v. naus-1\",\n              \"stance\": \"partial\",\n              \"note\": \"POK_full.txt l.61944ff lists 'ap. nāviyā \\\"fleet\\\"' and 'Avestan nāvaya- \\\"navigable\\\"' and 'Avestan navāza-' — i.e. Pokorny too gives the Iranian material only in these derived shapes, with Horn's old 'fleet' gloss for nāviyā.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, Concise Pahlavi Dictionary\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'nāw' in PHD.txt returns only šnāz-/nāw- 'swim', zēnāwand, āznāwar: MacKenzie has no Middle Persian entry nāw 'ship'. Horn's phlv. nāvtāk/nāvīcak (from the Bundahišn) is thus the only Middle Iranian bridge on record, and it is a derivative, not the simple noun.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"nâv «ناو»; nâv-dân «ناودان»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian ناو nāv continues Middle Persian nāw 'ship' < Old Persian nāv- (𐎴𐎠𐎺) < Proto-Iranian *náHuš < PIE *néh₂us; the long ā and the -v are simply preserved, so the word is one of the few Persian nouns whose shape is unchanged from the Achaemenid period. Its double semantics — 'ship' and 'trough / channel / gutter' — is old and internal: a dugout boat and a hollowed log gutter are the same object (compare Welsh noe 'kneading trough', Norwegian no 'trough from a hollowed trunk', OHG nuosc 'trough, gully', all under Pokorny's naus-1), so no borrowing or contamination need be assumed. Borhan-e Qate' gives exactly Nourai's range: 'کشتی و جهاز کوچک — و ناودان بام خانه — و آنچه گندم از دول به گلوی آسیا ریزد — و چوب میان‌خالی کرده که … آب از آن به چرخ آسیا خورد' (with the Attar verse Nourai prints). ناودان nāv-dān is a New Persian compound of nāv + dān, the second element being the old Iranian *dānu- 'river, flowing water' (Av. dānu-, whence the Danube/Don names — Nourai's ☞Dâ 2), hence literally 'water-channel'; already Horn p.229 cites 'nāv \\\"Wasserkanal; Schiffchen\\\", nāvdān'. Nourai's extra list is all regular Persian word-formation on nāv: ناوشکن 'destroyer' (nāv-šekan 'ship-breaker'), ناودیس 'syncline' (nāv-dīs 'boat-shaped'), ناوسار, ناخدا (< nāv-xodā 'ship-master'), ناوگان 'fleet', ناوبان, ناودار — the military ones being 20th-century coinages of the Farhangestān, as Mo'in marks them '(فره.)'.\",\n          \"derivation_fa\": \"«ناو» فارسی نو دنبالهٔ فارسی میانهٔ nāw «کشتی» است، از پارسی باستان nāv- (𐎴𐎠𐎺)، از ایرانی آغازین *náHuš و هندواروپایی *néh₂us؛ الف کشیده و واو دست‌نخورده مانده‌اند و از این رو «ناو» از کم‌شمار نام‌های فارسی است که از دورهٔ هخامنشی تا امروز صورت خود را نگه داشته است. دو معنای «کشتی» و «جوی/تغار/ناودان» از آغاز در همین واژه بود، زیرا قایقِ یک‌پارچه و ناودانِ تراشیده از تنهٔ درخت یک چیزند (سنجیدنی با noe ولزی «تغار خمیر» و nuosc آلمانی باستان «ناودان» زیر همان ریشه در پوکورنی). برهان قاطع (ص ۲۱۱۰) همین دامنهٔ معنایی را با شاهدِ عطار می‌آورد. «ناودان» ترکیبی فارسی نو است از ناو + دان که جزء دوم آن به *dānu- ایرانی باستان «رود، آب روان» (اوستایی dānu-، ریشهٔ نام دانوب و دُن) بازمی‌گردد، پس تحت‌اللفظ «آبراهه» است؛ هرن نیز در ص ۲۲۹ «nāv, nāvdān» را کنار هم آورده است. واژه‌های افزودهٔ نورایی (ناوشکن، ناودیس، ناوسار، ناخدا، ناوگان، ناوبان، ناودار) همه ساخت‌های قاعده‌مند فارسی بر پایهٔ «ناو» اند و اصطلاحات نظامی‌شان ساختهٔ فرهنگستان است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%88\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:2110\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate', Mo'in's ed., printed p.2110 = vol 4 pdf page 193 (printed = pdf+1917; BQT_v4_pages.txt '[pdf page 193]'): headword ناو with the senses 'وکشتی و جهاز کوچك - وناودان بام خانه - و آنچه گندم بدان از دول بگلوی آسیا ریزد - وچوب میان خالی کرده که در بعضی مواضع آب ازآن بچرخ آسیا خورد و بگردش آرد', the Attar verse Nourai quotes ('در تحیر طفل میزد دست و پا / آب می بردش بناو آسیا. عطار نیشابوری'), and Mo'in's etymological footnote: 'پارسی باستان nāviya- (جهاز)، اوستا nāvāza- (کشتی ران)، هندی باستان nāv- (کشتی، قایق، کرجی)، ارمنی nav (کشتی)، navem (سفر دریا کردن) … هوبشمان … کردی nāv (زورق)، nāw (قنات، ناودان، راه آب) «ژابا»' plus 'رك: ناودان'. Nourai's node is this entry.\"\n            },\n            {\n              \"ref\": \"MON:4644\",\n              \"status\": \"supports\",\n              \"note\": \"Mo'in, Farhang-e Farsi s.v. ناو (checked in the 2-vol Adena condensation MON_part2.txt l.73510ff, the only text of Mo'in on disk): 'ناو: nāv [جهاز] (ا.) هر چیز دراز میان خالی. چوب کاواک که آب از آن به تنورهٔ آسیا یا از جایی به جایی دیگر رود. ممر آب که از سفال سازند … ناودان. جوی آب؛ نهر. دره‌ای که رودی از میان آن بگذرد؛ وادی. رخنه، سوراخ. قایقی کوچک که از درختی میان کاواک سازند. کشتی، سفینه. کشتی جنگی (فره.) …' — i.e. all four of Nourai's glosses (ship, water path, pipe, river). The neighbouring entries ناودان، ناوشکن، ناودیس، ناوسار، ناوخدا، ناوگان، ناوبان also stand there, so his 'extra' list is Mo'in's. Page number 4644 cannot be verified: the 6-volume Amir Kabir edition is not online (refs_online.json MON notes) and the condensation is unpaginated.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn no. 1024, printed p.229\",\n              \"stance\": \"supports\",\n              \"note\": \"HRN.txt leaf 250: 'nāv \\\"Wasserkanal; Schiffchen\\\", nāvdān … phlv. nāvtāk (aw. nāvaya-), nāvīcak (Bund.); ai. nāv- \\\"Schiff, Kahn, Nachen\\\" … kurd. LW. nav; oss. LW. d. navā, t. nau- \\\"Schiff\\\"'. Horn's headword already pairs nāv with nāvdān, exactly as the chart does.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Mo'in s.vv. ناودان، ناوشکن، ناودیس، ناوسار، ناوخدا، ناوگان\",\n              \"stance\": \"supports\",\n              \"note\": \"MON_part2.txt l.73548ff: 'ناودان: (امر.) جایی که در آن ناو (ممر سفالین آب) گذارند (رشیدی). ممر آب … ممر خروج آب پشت بام که از سفال یا آهن سفید سازند'; 'ناودیس: (ص‌مر.) به شکل ناو (کشتی)؛ مانند ناو. (زم.) چین‌خوردگی بزرگ و منحنی مقعر طبقات'; 'ناوخدا: [= ناخدا] ملاح، کشتیبان'; 'ناوگان: (نظ.) مجموع کشتی‌های جنگی یک دولت (فره.)'; 'ناوشکن: [= ناوشکننده] (نظ.) کشتی کوچک بسیار تندرو …(فره.)'.\"\n            },\n            {\n              \"src\": \"IRN\",\n              \"where\": \"Farahvashi, Iranvij, printed pp.133–134\",\n              \"stance\": \"supports\",\n              \"note\": \"IRN_pages.txt l.3872ff: '«ناودان» است که مرکب است از nāv + dān … و «دان» بمعنای جریان آب است و بر روی هم بمعنی چیز میان‌تهی است که آب در آن جاری باشد و دانوب بمعنی آب جاری است' — the ☞Dâ 2 cross-reference of the chart.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e Rishe-ha\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'ناو' in incoming/ARY/ARY_pages.txt returns only اسکاندیناوی / فناوری / ناوگان in running prose, and the Latin index (ARY_latin_index_pages.txt) has no NAV-/NAU- headword: Aryanpur has no entry for ناو.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"nâvânîdan «ناوانیدن»; nâvîdan «ناویدن»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both are denominal verbs built inside New Persian on the noun ناو nāv, so the arrow root → these verbs is really root → nāv → verb; the derivation is transparent and the lexicographers state it. ناویدن nāvīdan = nāv + the intransitive infinitive suffix -īdan, 'to sway from side to side like a boat/trough', hence 'to lurch, stagger; to walk with a swaying, coquettish gait (خرامیدن); to bend; to grow tired'; Borhan-e Qate' p.2112 footnote 8: 'از: ناو (ه.م.) + یدن (پسوند مصدری). لغةً ماد ناو به چپ و راست متمایل شدن', and Mo'in s.v.: 'ناویدن: nāvīdan (مص‌ل.) مانند ناو به چپ و راست متمایل شدن، تلوتلو خوردن. خرامیدن به ناز، گرازیدن. خم شدن'. ناوانیدن nāvānīdan is its causative, nāv + -ānīdan, 'to make boat-shaped, to bend'; Borhan p.2110: 'ناوانیدن … بمعنی خم کردن و خم دادن و مانده گردانیدن', with the footnote 'از: ناو + انیدن (پسوند مصدر متعدی)، متعدیِ ناویدن'. Nourai's Molavi verse (چو مست هر طرفی می‌فتی و می‌ناوی …) is the citation Borhan gives for nāvīdan under footnote 9 of p.2112, quoting Farhang-e Nezām. Both verbs are late, dictionary-attested formations rather than inherited Iranian verbs — Cheung's Etymological Dictionary of the Iranian Verb has no root *nāv-, as expected for a denominal — so the semantics ('bend like a boat', 'sway like a ship') that Nourai gives is exactly what the Persian sources give.\",\n          \"derivation_fa\": \"هر دو فعل، ساختهٔ درونِ فارسی نو بر پایهٔ نامِ «ناو» اند؛ پس پیکان در واقع «ریشه ← ناو ← فعل» است. «ناویدن» از ناو + پسوند مصدری «-یدن» است به معنای «مانند ناو به چپ و راست متمایل شدن، تلوتلو خوردن، خرامیدن، خم شدن»؛ حاشیهٔ برهان قاطع (ص ۲۱۱۲، پانویس ۸) صریح می‌گوید: «از: ناو + یدن (پسوند مصدری). لغةً ماد ناو به چپ و راست متمایل شدن»، و معین نیز همین را می‌آورد. «ناوانیدن» متعدیِ آن است، از ناو + «-انیدن»، «خم کردن، خم دادن، مانده گردانیدن» (برهان، ص ۲۱۱۰ با پانویسِ «متعدیِ ناویدن»). بیتِ مولوی که نورایی آورده، همان شاهدِ برهان برای «ناویدن» است. چون این‌ها فعل‌های اشتقاقیِ متأخرند، در فرهنگ ریشه‌شناختی فعل‌های ایرانی چونگ ریشه‌ای *nāv- نیست و انتظار هم نمی‌رود. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%88\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:4645,4650\",\n              \"status\": \"supports\",\n              \"note\": \"Mo'in (MON_part2.txt l.73534): 'ناوانیدن: nāvānīdan (مص م.) خم کردن، خم دادن. مانده کردن، خسته گردانیدن'; l.73656: 'ناویدن: nāvīdan (مص‌ل.) مانند ناو به چپ و راست متمایل شدن، تلوتلو خوردن. خرامیدن به ناز، گرازیدن. خم شدن. مانده شدن، خسته گردیدن. میان تهی نمودن سنگ با قطعهٔ چوب. چرت زدن، پینکی رفتن.' Both glosses are Nourai's, and the two page numbers he gives (4645 for the causative, 4650 for the simplex) match the alphabetical distance between them. Exact pagination unverifiable: only the unpaginated 2-vol condensation of Mo'in is available.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhan-e Qate' printed pp.2110 and 2112 (vol 4 pdf 193, 195)\",\n              \"stance\": \"supports\",\n              \"note\": \"p.2110: 'ناوانیدن - با نون بروزن آرامیدن، بمعنی خم کردن و خم دادن و مانده گردانیدن', footnote 'از: ناو (ه.م.) + انیدن (پسوند مصدر متعدی)، متعدی «ناویدن»'; p.2112: 'ناویدن - بروزن چاویدن. بمعنی پینکی … و نالیدن … و بمعنی خرامیدن و رفتاری بناز … و خم شدن و مانده گردیدن', footnote 8 'از: ناو + یدن (پسوند مصدری). لغةً ماد ناو بچپ وراست متمایل شدن', footnote 9 the Molavi verse 'چو مست هرطرفی می‌فتی و می‌ناوی / که شب گذشت کنون نوبت دعاست، مخسب. مولوی بلخی رومی «فرهنگ نظام»'.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Cheung, Etym. Dict. of the Iranian Verb\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'nāv' / '*naH' in CHEUNG.txt yields nothing relevant (only Skt. snath-): Cheung reconstructs no Iranian verbal root here, consistent with these being New Persian denominal verbs rather than inherited ones.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn no. 1024, p.229\",\n              \"stance\": \"silent\",\n              \"note\": \"Horn's nāv entry lists only the noun and nāvdān; he records no verb nāvīdan/nāvānīdan (HRN.txt leaf 250) — these are lexicographers' words, absent from his etymological corpus.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"nâveh «ناوه»; nâvak «ناؤک» (printed ناوَک)\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The etymology of the node is right and well documented: both words are diminutive/derivative formations on ناو nāv. ناوه nāveh = nāv + the suffix -a(h) (Mo'in: 'ناوه: [= ناوک] ناو خرد') and denotes exactly what Nourai lists — the hod or hollowed short log a plasterer carries mortar in, the wooden trough for kneading, the chute that lets grain run from the hopper into the mill's throat, the groove on a grain of wheat or a date-stone, and the grooved guide through which a small arrow is shot: Borhan p.2112 'ناوه … چوب کوتاه میان خالی کرده راگویند که گل‌کاران بدان گل کنند - و تشتی چوبین که در آن خمیر کنند - و آلتی که بدان گندم و جو از دول ریزد - و چوب با آهن میان‌خالی که تیر ناوک را در آن نهاده اندازد'. ناوک nāvak = nāv + the diminutive/similative suffix -ak, 'little trough' → the light arrow (or bolt) shot from such a grooved guide, whence the standard poetic 'arrow' of eyelash and glance in Nourai's Bahar verse; Mo'in s.v.: 'ناوک: nāvak [ناو + ک، پس. تصغیر و نسبت و شباهت = ناوه] ناوِ خرد. نوعی تیر کوچک که آن را در غلاف آهنین یا چوبین — که مانند ناوی باریک بود — گذارند و از کمان سر دهند تا دورتر رود'. What is wrong is the SCRIPT of the second word in the JSON: it reads «ناؤک» (wāw with hamza), which is not a possible Persian spelling. The printed page (pdf 346, rendered at 600 dpi, data/verification/sources/refs/ocr/BOOK/346.png and the 6× zoom 346-navak-zoom.png) shows «ناوَک» — a plain wāw carrying a FATHA, i.e. the vocalisation nāvak that the book uses to fix the reading; the same word appears undiacriticised as ناوک in the Bahar verse two lines below. So the extraction misread the fatha as a hamza; the book is not at fault, and the correct form is ناوک (vocalised ناوَک).\",\n          \"derivation_fa\": \"ریشه‌شناسی این گره درست است: هر دو واژه مشتقِ «ناو» اند. «ناوه» = ناو + پسوند «-ه»، و معناهایش همان است که نورایی آورده: تغار و چوبِ میان‌خالیِ گل‌کاران، تشتِ چوبینِ خمیر، ناوهٔ ریزشِ گندم از دول به گلوی آسیا، شیارِ دانهٔ گندم و هستهٔ خرما، و ناوهٔ پرتابِ تیرِ کوچک (برهان قاطع، ص ۲۱۱۲). «ناوک» = ناو + پسوند تصغیر و شباهتِ «-ک»، یعنی «ناوِ خرد» و از آنجا «تیرِ کوچکی که در غلافی ناومانند می‌گذارند و از کمان می‌رهانند» (معین، ذیل ناوک) — همان «ناوکِ مژگان» شاهدِ بهار. اما خطایی در خوانشِ اسکن هست: در JSON «ناؤک» آمده که املای ناممکنی است؛ صفحهٔ چاپی «ناوَک» است، یعنی واوِ ساده با فتحه (تصویرِ ۶۰۰ نقطه در data/verification/sources/refs/ocr/BOOK/346.png و بزرگ‌نماییِ 346-navak-zoom.png گواهِ آن است)، و در بیتِ بهار نیز همان واژه بدونِ اعراب «ناوک» نوشته شده. پس خطای خوانشِ اسکن است، نه خطای چاپی کتاب؛ صورت درست «ناوک» است.\",\n          \"error_in\": \"extraction\",\n          \"book_prints\": \"ناوَک\",\n          \"correct_form\": \"ناوک\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%88\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:4649\",\n              \"status\": \"supports\",\n              \"note\": \"Mo'in (MON_part2.txt l.73641): 'ناوه: nāve(h) [= ناوک] (ا.) ناو خرد. نوعی تیر. ناوی که از آن گندم و جو از دول به گلوی آسیا ریزند. شیاری که در پشت آدمی است. شیاری که در دانهٔ گندم و هستهٔ خرما است. هر چیز میان خالی. چوب کوتاه و مجوفی که گلکاران به وسیلهٔ آن گل [برند]. ظرف چوبین.' l.73608: 'ناوک: nāvak [ناو + ک، پس. تصغیر و نسبت و شباهت = ناوه] ناوخرد. نوعی تیر کوچک که آن را در غلاف آهنین یا چوبین — که مانند ناوی باریک بود — گذارند و از کمان سر دهند تا دورتر رود.' Both of Nourai's glosses verbatim.\"\n            },\n            {\n              \"ref\": \"BQT:2112\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' printed p.2112 = vol 4 pdf 195: 'ناوه - بر وزن ساره. چوب کوتاه میان خالی کرده راگویند که گل کاران بدان گل کنند - وتشتی چوبینی که در آن خمیر کنند - وآلتی که بدان گندم و جو از دول ریزد - وچوب با آهن میان خالی که تیر ناوک را درآن نهاده اندازد - وچوبک میان آدمی و دانهٔ گندم و هستهٔ خرما را نیز گویند', with footnote '۱ از: ناو (ه.م.) + ه (پسوند صغیر، نسبت و شباهت) = ناوک (ه.م.) و رك: ناو' and the dialect forms 'دراراک (سلطان‌آباد) nāvāk (چوب کوتاه میان خالی که گل‌کاران بدان گل کشند) «مکی‌نژاد»، تهرانی nāve, بروجردی nāve «شپیدی»'. Exactly Nourai's page and gloss.\"\n            },\n            {\n              \"ref\": \"FSF:321\",\n              \"status\": \"supports\",\n              \"note\": \"Noushin, Vazhe-namak (Farhang-e Shahnameh), printed p.321 (FSF_pages.txt leaf 435, whose page numeral reads ۳۲۱): s.v. ناوک, quoting the Sahāh — '… آهنین که مانند ناوی باریک باشد کنند و در کمان نهند و بیندازند و بدان‌سبب ناوک خوانند (صحاح)' — with the Shahnameh line 'سپهرم به ترمذ شد و بارمان / … بکرهدار ناوک …'. This is the 'arrow shot through a guide' sense of Nourai's node.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"Mo'in s.vv. ناوک، ناوه\",\n              \"stance\": \"supports\",\n              \"note\": \"quoted in ref_check above: Mo'in gives the morphological analysis 'ناو + ک، پسوند تصغیر و نسبت و شباهت' explicitly, which is precisely the derivation Nourai's arrow asserts.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhan-e Qate' p.2112, footnotes to ناوه/ناوک\",\n              \"stance\": \"supports\",\n              \"note\": \"the footnote 'از: ناو + ه (پسوند صغیر، نسبت و شباهت) = ناوک' derives both from ناو; the Arabicised form is noted as 'معرب: اوق «قطر المحیط»'.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn no. 1024, p.229\",\n              \"stance\": \"silent\",\n              \"note\": \"Horn's entry has nāv and nāvdān only; neither nāveh nor nāvak appears (HRN.txt leaf 250), so the diminutives rest on the Persian lexicographers alone.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"navis\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin nāvis, -is f. 'ship' is the regular Italic reflex of PIE *néh₂us: an originally consonant-stem root noun, as its archaic accusative nāvem (= Skt. nāvam, Gk. nêa) shows, later drawn into the i-stems (Ernout–Meillet, DELL s.v. 'nauis, -is f. (ac. nauim et nauem, abl. naui et naue …): navire, vaisseau. Terme générique. Ancien (Columna Rostrata, Liv. Andronicus), usuel'). It is attested from the earliest Latin (the Columna Rostrata inscription and Livius Andronicus, 3rd c. BCE) and produces nāvālis, nāvicula, nāvigāre, Late Latin nāvia — the whole family behind node 6. The arrow root → Latin is uncontroversial in every handbook.\",\n          \"derivation_fa\": \"لاتینی nāvis «کشتی» بازماندهٔ قاعده‌مندِ *néh₂us در شاخهٔ ایتالیک است: در اصل نامِ ریشه‌ایِ همخوان‌پایان بود — چنان‌که مفعولیِ کهنِ nāvem (برابرِ nāvam سنسکریت و nêa یونانی) نشان می‌دهد — و سپس به ستاک‌های i پیوست (ارنو–میه، ذیلِ nauis). این واژه از کهن‌ترین متون لاتین (کتیبهٔ Columna Rostrata و لیویوس آندرونیکوس، سدهٔ سومِ پیش از میلاد) گواهی دارد و nāvālis و nāvicula و nāvigāre و nāvia لاتینِ متأخر از آن برآمده‌اند که خانوادهٔ گرهٔ ۶ اند. این پیوند در همهٔ فرهنگ‌های ریشه‌شناختی پذیرفته است؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9h%E2%82%82us\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt l.772 s.v. nau-2 'Boat': '1. Latin nāvis, ship: NACELLE, NAVAL, NAVICULAR, NAVIGATE, NAVY. … [Pok. 1. nāu- 755.]' — Nourai's un-paginated 'AHD' citation is the Indo-European appendix, and it says exactly this.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout–Meillet, DELL, pp. 765–766 s.v. nauis\",\n              \"stance\": \"supports\",\n              \"note\": \"LAT.txt l.40553ff: 'nauis, -is f. … navire, vaisseau. Terme générique. Ancien (Columna Rostr., Liv. Andr.), usuel. Dérivés et composés: nāuālis: naval … nāuia, -ae f.: doublet populaire de nauis … nāuicula (naucula) … nāuigō, -ās: naviguer … nāuiger, nāuiuorus'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. naval\",\n              \"stance\": \"supports\",\n              \"note\": \"KLN_1966.txt l.25053: 'naval, adj. … fr. L. nāvālis, fr. navis, \\\"ship\\\", which is cogn. with OI. nauḥ, acc. nāvam, \\\"ship, boat\\\", Arm. nav, \\\"ship\\\", Gk. ναῦς … OIr. nau (gen. noe), \\\"ship\\\", W. noe, \\\"a flat vessel; a kneading trough\\\", ON. nór, \\\"ship\\\".'\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 10.81\",\n              \"stance\": \"supports\",\n              \"note\": \"SYN.txt l.18361: '10.81 SHIP … Lat. navis, navigium; It. nave; Fr. navire; Sp. buque, nave, navio; Rum. corabie' — the inherited Latin word and its Romance continuations.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"navy; navigate\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"navy: Middle English navie, borrowed from Old French navie 'fleet of ships, ship', which continues Late Latin nāvia 'ship' (the popular doublet of nāvis noted by Ernout–Meillet), so the modern collective sense 'fleet, naval force' is a French-period development from 'ship(ping)'. navigate: a 16th-century learned borrowing from Latin nāvigātus, past participle of nāvigāre 'to sail', itself a compound *nāv-igus < nāvis 'ship' + agere 'to drive' (whence also navigation, navigator and — clipped in 19th-century British canal-digging slang — navvy). Klein states both chains; the same words appear under Watkins' nau-2. Nourai's arrow Latin → English is therefore right, with the standard Old French / learned-Latin routes unstated but uncontroversial.\",\n          \"derivation_fa\": \"«navy» از انگلیسی میانهٔ navie است، وام‌گرفته از فرانسهٔ کهن navie «ناوگان، کشتی»، که خود دنبالهٔ nāvia لاتینِ متأخر (گونهٔ عامیانهٔ nāvis) است؛ پس معنای امروزیِ «نیروی دریایی» تحولی فرانسوی از «کشتی» است. «navigate» وام‌واژهٔ دانشورانهٔ سدهٔ شانزدهم از nāvigātus لاتین است، اسم مفعولِ nāvigāre «کشتی راندن»، که خود ترکیبِ nāvis + agere «راندن» است (و navigation و navigator و navvy از همان‌اند). کلاین هر دو زنجیره را همین‌گونه می‌آورد و واتکینز نیز این واژه‌ها را زیرِ nau-2 فهرست می‌کند. پس پیکانِ «لاتین ← انگلیسی» درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9h%E2%82%82us\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"—\",\n              \"status\": \"not_checked\",\n              \"note\": \"the node carries no refs= in the book (refs: null in the JSON), so there is nothing of Nourai's to check; the claim was verified against Klein, Skeat and Watkins instead (see consulted).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.vv. navy, navigate, navvy\",\n              \"stance\": \"supports\",\n              \"note\": \"KLN_1966.txt l.25067: 'navy, n. — ME. navie, fr. OF. navie, \\\"fleet of ships, ship\\\", fr. Late L. navia, of s.m., fr. L. navis. See naval.'; l.25066: 'navigate … L. navigatus, pp. of navigāre, \\\"to sail, set sail\\\", lit. \\\"to drive a ship\\\", fr. *navigus, for *nav-agos, \\\"driving a ship\\\", which is compounded of navis, \\\"ship\\\", and agere …'; and 'navvy … Shortened fr. navigator'.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.v. Nave (2) and cross-references\",\n              \"stance\": \"supports\",\n              \"note\": \"SKT.txt l.12185: 'Nauseous, Nautical; see Nave (2). Nautilus, Naval; see Nave (2)' — Skeat files the whole family, navy included, under the ship word, separate from Nave (1) 'hub of a wheel' (< Skt. nābhi).\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. nau-2 and the index\",\n              \"stance\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt l.772 lists NAVAL, NAVICULAR, NAVIGATE, NAVY under 'Latin nāvis'; the index (l.1902) confirms 'NAVIGATE ag-, nau-2 | NAVY nau-2', i.e. navigate is doubly rooted (nau- + ag-), matching Klein's compound analysis.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Greek\",\n          \"words\": \"naus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Ancient Greek ναῦς (Attic naûs, gen. neōs; Homeric νηῦς, νηός < *nāwos) 'ship' is the Hellenic reflex of PIE *néh₂us. The Homeric forms show the lost intervocalic *w (νηός < *nāwós), and the Doric/Aeolic ναῦς keeps the inherited long vowel where Attic-Ionic would give nē-; the accusative νῆα equals Latin nāvem and Sanskrit nāvam, which is what identifies the paradigm as an inherited root noun rather than a later formation (Pokorny 755–756). From the stem Greek built ναύτης 'sailor' — the element that gives every -naut compound in node 8 — and ναυτικός, ναυτίλος, ναυσία.\",\n          \"derivation_fa\": \"یونانی باستان ναῦς (آتیک naûs، اضافیِ neōs؛ هومری νηῦς، νηός از *nāwos) «کشتی» بازماندهٔ *néh₂us در شاخهٔ یونانی است. صورت‌های هومری نشانِ افتادنِ *w میان‌واکه‌ای اند (νηός < *nāwós) و ναῦς دوریک واکهٔ کشیدهٔ کهن را نگه داشته است؛ مفعولیِ νῆα دقیقاً برابرِ nāvem لاتین و nāvam سنسکریت است و همین است که این صرف را نامِ ریشه‌ایِ به‌ارث‌رسیده می‌شناساند (پوکورنی ۷۵۵–۷۵۶). از همین ستاک ναύτης «ملوان» ساخته شد که جزءِ دومِ همهٔ ترکیب‌های -naut در گرهٔ ۸ است، و نیز ναυτικός و ναυτίλος و ναυσία. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9h%E2%82%82us\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt l.772 s.v. nau-2: '2. Greek naus, ship, and nautēs, sailor: NAUSEA, NAUTICAL, NAUTILUS, (NOISE); AERONAUT, AQUANAUT, ARGONAUT, ASTRONAUT, COSMONAUT.' Nourai's Greek node and its English node are this paragraph.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"Pokorny 755–756 s.v. naus-1\",\n              \"stance\": \"supports\",\n              \"note\": \"POK_full.txt l.61944ff: 'gr. hom. νηῦς, νηός (*νᾱϝός), Attic ναῦς, νεώς \\\"ship\\\" … (compare Akk. navem = Old Indic navam, gr. νῆα)'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.v. naval (cognate list)\",\n              \"stance\": \"supports\",\n              \"note\": \"KLN_1966.txt l.25053: '… Gk. ναῦς, \\\"ship\\\" (whence ναύτης, \\\"sailor, seaman\\\", ναυτικός, \\\"of, or pertaining to, ships or sailors, seafaring, naval, nautical\\\", ναυτίλος, \\\"sailor, seaman\\\") …'\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 10.81, 10.82\",\n              \"stance\": \"supports\",\n              \"note\": \"SYN.txt l.18361 'Grk. ναῦς, πλοῖον' for 'ship'; l.18416 '1. Grk. ναύτης (> Lat. nauta) … derivs. of Grk. ναῦς, etc. \\\"ship\\\" (10.81)' for 'sailor'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"nautical; nausea; noise; nautilus; astronaut; cosmonaut; aeronaut\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Six of the seven are certain and all go back to Greek ναῦς through ναύτης 'sailor'. nautical < obsolete nautic < French nautique < Latin nauticus < Gk. ναυτικός. nausea < Latin nausea/nausia < Gk. ναυσία 'seasickness', literally 'ship-sickness', from ναῦς — the sense 'disgust' being a Latin-to-English extension. nautilus < Latin nautilus < Gk. ναυτίλος 'sailor', applied to the mollusc because it was thought to spread a membrane like a sail. astronaut, cosmonaut, aeronaut are modern compounds (aeronaut 1784, of balloonists; astronaut 1929; cosmonaut 1959, calquing Russian космонавт) whose second element is Gk. ναύτης. The doubtful one is noise, and Nourai gives it without a caveat. Klein does support him: 'noise … ME., fr. OF. noise …, fr. L. nausea, \\\"seasickness\\\", which in Vulgar Latin prob. had the meaning of \\\"unpleasant situation, noise, quarrel\\\" … Cp. nausea, of which noise is a doublet', citing Old Provençal nauza/noiza 'noise, quarrel' as the parallel. But Watkins prints '(NOISE)' in parentheses, i.e. flags it as uncertain; Skeat records the alternative derivation from Latin noxia 'harm' and labels the question 'Disputed'; and Etymonline reports that the OED 'considers that the sense of the word is against both suggestions'. The node is therefore 'plausible' rather than 'confirmed' — because of noise alone, the other six being confirmed.\",\n          \"derivation_fa\": \"شش واژه از هفت واژه یقینی‌اند و همه از راهِ ναῦς و ναύτης یونانی می‌آیند: nautical از nauticus لاتین و ναυτικός یونانی؛ nausea از nausea لاتین و ναυσία یونانی «دریازدگی» که تحت‌اللفظ «بیماریِ کشتی» است؛ nautilus از ναυτίλος «ملوان» که به آن نرم‌تن داده شد چون گمان می‌کردند پرده‌ای همچون بادبان می‌گستراند؛ و aeronaut (۱۷۸۴) و astronaut (۱۹۲۹) و cosmonaut (۱۹۵۹، گرته‌برداری از روسیِ космонавт) ترکیب‌های نوساخته با ναύτης اند. تنها واژهٔ مشکوک noise است که نورایی بی‌هیچ قید آورده. کلاین به سودِ او است: «noise از فرانسهٔ کهن noise، از nausea لاتین که در لاتینِ عامیانه معنای «وضع ناخوشایند، هیاهو، نزاع» داشته … دوگانهٔ nausea». اما واتکینز آن را در کمانک «(NOISE)» گذاشته یعنی نامطمئن؛ اسکیت گزینهٔ noxia «آسیب» را هم می‌آورد و مسئله را «مورد اختلاف» می‌خواند؛ و اتیمانلاین گزارش می‌کند که فرهنگِ آکسفورد معنای واژه را با هر دو فرض ناسازگار می‌بیند. پس این گره فقط به سببِ noise «با احتیاط پذیرفتنی» است و شش واژهٔ دیگر تأیید می‌شوند.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/noise\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"—\",\n              \"status\": \"not_checked\",\n              \"note\": \"the node carries no refs= in the book (refs: null in the JSON); verified against Klein, Skeat, Watkins and Etymonline instead (see consulted).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.vv. nautical, nausea, nautilus, noise, aeronaut, astronaut, cosmonaut\",\n              \"stance\": \"supports\",\n              \"note\": \"KLN_1966.txt l.25048 'nautical … fr. L. nauticus … fr. Gk. ναυτικός'; l.25042 'nausea … L. nausea, nausia, \\\"seasickness\\\", fr. Gk. ναυσία, ναυτία, \\\"seasickness\\\", lit. \\\"ship sickness\\\", fr. ναῦς … Cp. also noise, which is a doublet of nausea'; l.25053 'nautilus … Gk. ναυτίλος, \\\"sailor, seaman; the paper nautilus\\\" (so called because it was supposed to be furnished with a membrane which it used like a sail), fr. ναύτης'; l.25532 'noise, n. … ME., fr. OF. noise …, fr. L. nausea … For sense development cp. OProvenç. nauza, noiza, \\\"noise, quarrel\\\"'; l.1817 'aeronaut … Compounded of aero- and Gk. ναύτης \\\"sailor\\\"'; l.3769 'astronaut …'; l.9343 'cosmonaut …'.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.v. Noise (and Nave 2)\",\n              \"stance\": \"partial\",\n              \"note\": \"SKT.txt l.12410: 'Noise. (F.-L.-Gk.) M.E. noise … O.F. noise, a debate, quarrel … Cf. Prov. noisa, nausa … Diez holds that it can only be derived fr. L. nausea, sea-sickness, disgust, hence annoyance … Some attempt to derive it from L. noxia, harm … (Disputed; see Diez, Scheler, Littré).' Skeat thus supports the nausea route but records it as disputed — the reason this node is 'plausible'.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. nau-2 and index\",\n              \"stance\": \"partial\",\n              \"note\": \"AHD_watkins1985.txt l.772 gives 'NAUSEA, NAUTICAL, NAUTILUS, (NOISE); AERONAUT, AQUANAUT, ARGONAUT, ASTRONAUT, COSMONAUT' — six of Nourai's seven flat-out, but NOISE only in parentheses, Watkins' notation for an uncertain or indirect attachment. The index (l.1902) still lists 'NAUSEA nau-2 | NAUTICAL nau-2 | NAUTILUS nau-2'.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. nāustos\",\n              \"stance\": \"contradicts\",\n              \"note\": \"IEC.txt l.11554 derives Latin nausea not from Greek at all but from a Gallo-Latin nausum 'kind of boat' ('Gallo-Lat. nausum \\\"kind of boat\\\" (Phonol. of Lat. LW nausea)'). This is a minority position, but it would break the Greek link for nausea and noise alike.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Nâ 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *neh₂- / *h₃neh₂- 'to help, be of use' — Pokorny 'nā-1' 754; Walde–Pokorny II 315\",\n      \"note\": \"Correct: Pokorny's lemma nā-1 'to help, be of use' stands on p.754, the page Nourai cites, and 'Indo-European' is the right label for it. It is a thin root, however: Pokorny's whole material is Old Indic nā-thá- n. 'help', m. 'guarder', nāthate 'begs' plus Greek ὀνίνημι, ὄνειαρ 'benefit' — two branches only, and Watkins left it out of the AHD appendix altogether (grep of AHD_watkins1985.txt finds no such root). Modern reconstruction usually writes it with an initial laryngeal, *h₃neh₂- 'to help, support' (so Wiktionary s.v. Sanskrit नाथ, explaining the Greek o-vocalism as the laryngeal rather than as Pokorny's 'o-Präfix'). That the Iranian branch belongs here rests on Hübschmann's analysis of panāh, which is exactly what Nourai cites (HUB:43) — see node 1.\",\n      \"note_fa\": \"درست است: مدخلِ nā-1 «یاری کردن، سود رساندن» در پوکورنی همان صفحهٔ ۷۵۴ است که نورایی یاد کرده و برچسبِ «هندواروپایی» نیز بجاست. اما ریشهٔ کم‌مایه‌ای است: همهٔ گواهِ پوکورنی سنسکریتِ nā-thá- «یاری، پناه‌دهنده» و nāthate «زینهار می‌خواهد» است به‌همراهِ ὀνίνημι و ὄνειαρ یونانی — تنها دو شاخه؛ و واتکینز آن را در پیوستِ AHD نیاورده است. ریشه‌شناسی امروزی آن را معمولاً با حنجرهٔ آغازی *h₃neh₂- «یاری کردن، پشتیبانی کردن» می‌نویسد و واکهٔ o یونانی را نتیجهٔ همان حنجره می‌داند، نه «پیشوندِ o» که پوکورنی می‌گفت (ویکی‌واژه، ذیلِ نامواژهٔ سنسکریتِ ناث). تعلقِ شاخهٔ ایرانی به این ریشه بر تحلیلِ هوبشمان از «پناه» استوار است — همان مرجعی که نورایی آورده (هوبشمان، ص ۴۳).\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A4%BE%E0%A4%A5\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:754\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt (grep 'Page(s): 754', l.61881ff): 'Root / lemma: nā-1 (*he-nā-1) | Meaning: to help, be of use | Material: Old Indic nā-thá- n. \\\"help\\\", m. \\\"guarder\\\", nā-thate \\\"begs\\\"; gr. ὀ-νί-νη-μι, -νά-μεν \\\"use, take advantage of\\\", Fut. ὀνήσω, Med. ὀνίναμαι, Aor. ὠνήμην \\\"have benefit\\\", ὄνειαρ n., more properly ὄνηαρ, -ατος \\\"benefit\\\" (*ὀ-νᾱ-ω), etc. | References: WP. II 315. | Page(s): 754'. Nourai's root name, gloss and page are all exact.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Walde–Pokorny Bd. II 315 s.v. nā- 'helfen, nützen'\",\n          \"stance\": \"supports\",\n          \"note\": \"WLD_Bd2_pages.txt l.20799ff: 'nā- \\\"helfen, nützen\\\". Gr. ὀνίνημι, -νάμεν \\\"nützen\\\", fut. ὀνήσω usw., ὄνειας, recte ὄνηας \\\"Vorteil, Nutzen\\\" (ὀ-Praefix), ai. nā-tha- n. … m. \\\"Schützer\\\" … Ai. nathitá- \\\"bedrängt\\\", nāthate scheinen nach Wackernagel … erst durch volksetymol. Einfluß von nātha- \\\"Hilfe\\\" aus nadhitá- \\\"bedrängt\\\" … umgestaltet zu sein'. The doublet-warning is worth noting: Wackernagel thought the Sanskrit VERB nāthate is a folk-etymological reshaping of nadhitá-, so only the noun nātha- 'help' is a secure member of the root.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, Indo-European roots appendix\",\n          \"stance\": \"silent\",\n          \"note\": \"grep of AHD_watkins1985.txt for a root glossed 'to help' / for ὀνίνημι / nātha finds nothing: the root has no English reflex, so Watkins omits it. Its absence is not a contradiction, only silence.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, Indo-European Comparative Dictionary\",\n          \"stance\": \"silent\",\n          \"note\": \"grep '^nā' in IEC.txt yields only nāk- 'come, arrive, reach, suffice', nām (particle) and nāustos; Mann has no root nā- 'help'. (His nāk-3 'reach, suffice' is a different root and he expressly excludes Av. nās- from it.)\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"pa-nâtha, pati-nâtha, pa-nâh\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The node is Hübschmann's reconstruction, not an attested Old Iranian word, and the chart presents it as if attested — hence 'plausible'. What is real: the second element *nāθa- is the exact Iranian counterpart of Sanskrit nāthá- n. 'refuge, help', m. 'protector' (Atharvaveda onwards), from PIE *h₃neh₂- 'to help', cognate with Greek ὀνίνημι; the prefix is Old Iranian pati- 'towards, back' (OP patiy, Av. paiti-), which regularly gives Persian pa- in inherited compounds (pad-rūd > padrūd, pad-īd > padīd). Hübschmann, Persische Studien no. 327 (p.43), sets it out in so many words: he rejects Horn's derivation from √pā- 'to protect' and proposes 'pa-nāh' with nāh = OP *nāθa- = Skt. nāthá-, adding that *pati-nāh with tn > nn > n 'bleibt zu untersuchen'. Nourai's three forms are therefore Hübschmann's *pa-nāθa- and *pati-nāθa- plus the Middle Persian outcome pa-nāh, all in one box labelled 'Avestan / Old Persian'. Neither Bartholomae's Altiranisches Wörterbuch nor Kent's Old Persian lexicon has any pa-nāθa-/paiti-nāθa- or a bare Avestan nāθa-, so the Old Iranian stage is reconstructed only. Mo'in adopts it (footnote to Borhan p.418: Pahlavi pnʾh < *pati-nāθa-, 'به نقل از هوبشمان'), and it remains the standard account.\",\n          \"derivation_fa\": \"این گره بازساختِ هوبشمان است، نه واژه‌ای گواهی‌شده در ایرانی باستان، و نمودار آن را چنان می‌نماید که گویی گواهی دارد؛ از این رو «با احتیاط پذیرفتنی» است. آنچه واقعی است: جزءِ دومِ *nāθa- برابرِ دقیقِ nāthá- سنسکریت «پناه، یاری؛ پناه‌دهنده» (از اتهرواودا به این سو) است، از هندواروپاییِ *h₃neh₂- «یاری کردن» و هم‌ریشه با ὀνίνημι یونانی؛ و پیشوند، pati- ایرانی باستان «به‌سوی، باز» است (پارسی باستان patiy، اوستایی paiti-) که در ترکیب‌های موروثی به‌قاعده در فارسی به pa- بدل می‌شود (پدرود، پدید). هوبشمان در «پژوهش‌های ایرانی»، شمارهٔ ۳۲۷ (ص ۴۳) صریح می‌نویسد که ریشه‌گیری هرن از √pā- «نگاهبانی کردن» را نمی‌پذیرد و «pa-nāh» را پیشنهاد می‌کند با nāh = *nāθa- پارسی باستان = nāthá- سنسکریت، و می‌افزاید که پیدایش panāh از *patnāh (با ابدالِ tn به nn) «باید بررسی شود». در فرهنگ ایرانی باستانِ بارتولومه و واژه‌نامهٔ کنت هیچ pa-nāθa-/paiti-nāθa- و نیز nāθa- سادهٔ اوستایی نیست؛ پس مرحلهٔ ایرانی باستان تنها بازساخته است. معین همین را می‌پذیرد (حاشیهٔ برهان، ص ۴۱۸) و امروز هم دیدگاهِ پذیرفته همین است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A4%BE%E0%A4%A5\",\n            \"https://en.wiktionary.org/wiki/%F0%90%AD%AF%F0%90%AD%AD%F0%90%AD%A0%F0%90%AD%A7\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HUB:43\",\n              \"status\": \"supports\",\n              \"note\": \"Hübschmann, Persische Studien no. 327, printed p.43 (HUB.txt l.1447ff; the page number '— 43 —' is printed in the text immediately before the entry): 'Np. panāh \\\"Zuflucht, Hülfe\\\" = paz. panāh Min. Gl. 154, Shk. 262, phl. panāh Phl. Min. p.15,10, afgh. LW. panāh gehört ohne Zweifel nicht zur Wrzl. pā \\\"schützen\\\". Ich möchte pa-nāh teilen und nāh = ap. *nāθa- = skr. nāthá- \\\"Zuflucht, Hülfe\\\" setzen. Ob panāh aus *patnāh (tn zu nn = n?) entstanden sein kann, bleibt zu untersuchen.' This is verbatim Nourai's node: pa-nāθa-, pati-nāθa-, pa-nāh.\"\n            },\n            {\n              \"ref\": \"HRN:72\",\n              \"status\": \"contradicts\",\n              \"note\": \"Horn, Grundriss no. 327, printed p.72 (HRN.txt leaf 93): 'panāh \\\"Zuflucht, Schutz\\\", panāhīden \\\"Schutz suchen\\\". phlv. panāh, panāhīh, vergl. Mihr-panāhak (AV.). Doch wohl zu √pā- \\\"schützen\\\"? Bartholomae stützt diese Erklärung brieflich.' Horn (with Bartholomae's private backing) puts panāh under √pā- 'to protect' — i.e. under Nourai's OTHER root 'Pa', which is why the chart carries the cross-reference ☞Pa. Nourai cites both authorities without saying that they disagree; Hübschmann's √nā- analysis is the one modern lexicography follows.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, Altiranisches Wörterbuch\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'nāϑa', 'panāϑa', 'paiti.nāϑa' in BRT.txt returns nothing (the OCR renders Avestan θ as ϑ/9/^ inconsistently, but the neighbouring n- entries — navāza- l.18669, nāvaya- l.18894 — come out legibly, so an entry nāθa- would have surfaced): Avestan attests no *nāθa- 'help' and no pa-nāθa-. The Old Iranian forms of this node are reconstructions.\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian, Lexicon\",\n              \"stance\": \"silent\",\n              \"note\": \"no nāθa- / panāθa- in KNT.txt; Old Persian's own word in this semantic field is upastā- f. 'help' (from *upa-sthā-, cf. IEC l.17454 'Av. upa-stā, f. \\\"help\\\"; OPer. upa-stā \\\"help\\\"'), a different formation. Hübschmann's ap. *nāθa- is starred for good reason.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, Concise Pahlavi Dictionary, s.v. panāh\",\n              \"stance\": \"supports\",\n              \"note\": \"PHD.txt l.540: 'panāh [pnʾh | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~īh: protection.' Also 'pānāg [pʾn(ʾ)k | M pʾng] guard, protector; ~īh: protection' immediately before it — MacKenzie keeps panāh and pānāg (< √pā-) as two separate words, which is precisely Hübschmann's point against Horn. The Manichaean attestation ('= M') shows the word in 3rd-c. Middle Persian.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II, glossary\",\n              \"stance\": \"supports\",\n              \"note\": \"NYB_vol2_glossary.txt l.6076 indexes the Pahlavi spelling 'pnʾh: panāh', and l.2277 quotes it in a text: 'kē pat panāh kunom?' ('whom shall I take refuge with?', p.74 of the Manual's texts) — the Middle Persian form is well attested in situ.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"panâh «پناه»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian پناه panāh 'shelter, refuge, protection' is the direct continuation of Middle Persian panāh (Pahlavi pnʾh, also Manichaean and Pazand panāh, MacKenzie s.v.: 'protector; refuge'), with no phonetic change at all between the Sasanian and the New Persian form — the word is already complete in Middle Persian, and the derived panāhīdan 'to take refuge' (Horn: panāhīden 'Schutz suchen'), panāhgāh, panāhande are Persian formations on it. Behind Middle Persian panāh stands Old Iranian *pati-nāθa- (Hübschmann's *pat-nāh, with the cluster -tn- assimilated to -nn- and then simplified: *patnāh > pannāh > panāh), from *nāθa- 'help, refuge' = Skt. nāthá-, root PIE *h₃neh₂-. Mo'in states this etymology in his footnote to Borhan-e Qate' p.418 ('پهلوی pnʾh [panāhīh پناهی، پناه بردن] از *pati-nāθa- … «به نقل از هوبشمان»'), and Wiktionary gives the same Middle Persian source for the Persian word. The proper names Mihr-panāh (Ardā Wirāz Nāmag), Yazd-panāh, Panāh-mōy show the compound already productive in Middle Persian. So the arrow to Persian is confirmed; the reconstructed Old Iranian stage above it is what carries the residual uncertainty (node 1).\",\n          \"derivation_fa\": \"«پناه» فارسی نو دنبالهٔ مستقیمِ فارسی میانهٔ panāh (پهلوی pnʾh، و نیز مانوی و پازندِ panāh؛ مکنزی: «پناه‌دهنده؛ پناه») است و میان صورتِ ساسانی و فارسی نو هیچ دگرگونی آوایی رخ نداده — واژه در فارسی میانه کامل شده بود، و «پناهیدن» (هرن: «پناه جستن») و «پناهگاه» و «پناهنده» ساخت‌های فارسی بر همان اند. در پسِ panāhِ فارسی میانه صورتِ ایرانی باستانِ *pati-nāθa- می‌ایستد (بازساختِ هوبشمان: *patnāh با همگونیِ خوشهٔ -tn- به -nn- و آنگاه ساده‌شدنِ آن: *patnāh > pannāh > panāh)، از *nāθa- «یاری، پناه» برابرِ nāthá- سنسکریت و ریشهٔ هندواروپاییِ *h₃neh₂-. معین در حاشیهٔ برهان قاطع (ص ۴۱۸) همین ریشه‌شناسی را «به نقل از هوبشمان» می‌آورد و ویکی‌واژه نیز خاستگاهِ فارسی میانه را همان می‌داند. نام‌های خاصِ مهرپناه (ارداویراف‌نامه) و یزدپناه و پناه‌موی نشان می‌دهد این ترکیب در فارسی میانه زایا بوده است. پس ادعای نورایی در این گره درست است و تردید — اگر باشد — به مرحلهٔ بازساختهٔ بالای آن مربوط می‌شود.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%A7%D9%87\",\n            \"https://en.wiktionary.org/wiki/%F0%90%AD%AF%F0%90%AD%AD%F0%90%AD%A0%F0%90%AD%A7\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:72\",\n              \"status\": \"partial\",\n              \"note\": \"Horn no. 327, printed p.72 (HRN.txt leaf 93) has the word and its Middle Persian ancestor — 'panāh \\\"Zuflucht, Schutz\\\", panāhīden \\\"Schutz suchen\\\". phlv. panāh, panāhīh, vergl. Mihr-panāhak (AV.)' — so it fully supports the Persian node and the gloss 'shelter'; it differs only in the ultimate root, proposing '√pā- \\\"schützen\\\"?' instead of √nā-.\"\n            },\n            {\n              \"ref\": \"BQT:418\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate', Mo'in's ed., printed p.418 = BQT_v1_pages.txt leaf 644 (offset printed ≈ leaf − 226; l.26365): 'پناه - بفتح اول و ثانی بالف کشیده و هاء زده، بمعنی حمایت باشد - و سایهٔ دیوار را نیز پناه گویند - و امر بدین معنی هم هست یعنی پناه ببر و پناه بخواه', with Mo'in's etymological footnote 4 on the same page: 'پهلوی pnʾh [ panāhīh پناهی، پناه بردن ] از *pati-nāθa- … «۱۱۹ بنقل از هوبشمان» و رك: … ۳۲۷-۳۲۸' — i.e. Mo'in cites the very Hübschmann page (Persische Studien no. 327) that Nourai uses for node 1. Gloss and etymology both as charted.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie s.vv. panāh, pānāg\",\n              \"stance\": \"supports\",\n              \"note\": \"PHD.txt l.540: 'panāh [pnʾh | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~īh: protection.' — the Middle Persian link in the chain, kept distinct from pānāg 'guard, protector' (< √pā-).\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Mo'in, Farhang-e Farsi s.vv. پناه، پناهگاه، پناهیدن\",\n              \"stance\": \"supports\",\n              \"note\": \"MON_part1.txt l.32660ff: 'پناه: (ا.) حفظ، حمایت، پشتی، پشتوانه، استان، کنف. (ص.) نگاهبان، نگاهدار، حامی، حافظ، حارس. (ا.) پناهگاه، جای استوار، ملجأ، ملاذ، مأوی. سایهٔ دیوار …'; 'پناهیدن: panāhīdan (مص‌ل.) در حمایت کسی در آمدن، زنهار خواستن، پناه بردن'. Nourai's gloss 'shelter' is the core sense.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II\",\n              \"stance\": \"supports\",\n              \"note\": \"NYB_vol2_glossary.txt l.6076 'pnʾh: panāh' and l.2277 the textual citation 'kē pat panāh kunom?' — independent confirmation of the Middle Persian stage.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e Rishe-ha\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'پناه' in incoming/ARY/ARY_pages.txt returns no hits: Aryanpur has no entry for the word, so he neither supports nor opposes the *nā- attachment.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-07T17:52:30.702Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-346.json (file state is current in your context — no need to Read it back)
```


## [2026-09-07T17:52:34.265Z] TOOL CALL #68: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-346.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 346"
}
```


### [2026-09-07T17:52:35.683Z] TOOL RESULT

```
JSON OK
nodes verified: 10/10
node verdicts: {'plausible': 3, 'confirmed': 6, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'not_checked': 3, 'partial': 3, 'supports': 10, 'contradicts': 1}
books consulted: {'partial': 5, 'silent': 8, 'supports': 21, 'contradicts': 1} | by book: {'KLN': 4, 'PHD': 3, 'HRN': 3, 'MON': 3, 'KNT': 2, 'BRT': 2, 'POK': 2, 'ARY': 2, 'BQT': 2, 'SYN': 2, 'SKT': 2, 'AHD': 2, 'NYB': 2, 'IRN': 1, 'CHEUNG': 1, 'LAT': 1, 'IEC': 1}
```


## [2026-09-07T17:52:51.784Z] AGENT

Page 346 (book p. 316) verified. `data/verification/page-346.json` written; `verify_check.py 346` reports 10/10 nodes, 0 PROBLEM lines.

**Counts** — roots: 2 confirmed. Nodes: 6 confirmed, 3 plausible, 1 transcription_suspect. Ref checks: 10 supports, 3 partial, 1 contradicts, 3 not_checked.

**Transcription flag**
- *Na 1 / node #4, nâvak* — JSON has «ناؤک» (wāw + hamza, an impossible Persian spelling). The printed page shows «ناوَک» (wāw + **fatha**); confirmed at 600 dpi and 6× zoom. **Extraction error** — owner should fix `data/extracted/batch/page-346.json` node 4 script to `ناوک`. Audit images copied to `data/verification/sources/refs/ocr/BOOK/346.png` and `346-navak-zoom.png`.

**No disputed items.** Three `plausible` nodes, with reasons:
- #1 (Avestan/OP `nâu, nâviya`): OP nāv- 'ship' is real (DZe 11), but Kent glosses nāviyā- 'navigability' and expressly rejects 'flotilla' (Horn's old 'Flottille' is Nourai's source); Avestan has no bare nāu- (only nāvaya-, nāvāza-; Bartholomae emends nāuya Yt 16.3 → nāvaya); and nâv-dân is a New Persian compound, not Old Iranian.
- #8 (English list): six words certain, but *noise* is uncertain — Watkins prints "(NOISE)", Skeat calls it "Disputed" (nausea vs noxia), OED rejects both.
- Nâ 2 #1 (`pa-nâtha, pati-nâtha, pa-nâh`): these are Hübschmann's reconstructions (Pers. Studien 43, quoted verbatim), not attested forms — nothing in Bartholomae or Kent.

**Reference notes for the owner**
- `IRN:123` is off: the nāv-dān passage is on printed **p. 133** (the book's own index reads «ناودان ۱۳۳»); content otherwise supports the arrow.
- `HRN:72` **contradicts** Nourai: Horn (backed by Bartholomae in letters) derives panāh from √pā-, i.e. the chart's own ☞Pa root. Nourai cites both HUB:43 and HRN:72 without noting they disagree; modern lexicography follows Hübschmann.
- `PRT:429` not checked (Partridge is lending-only, no local copy). MON page numbers (4644/4645/4649/4650) unverifiable — only the unpaginated 2-vol Adena condensation is on disk; all four entries were found and support the glosses.
