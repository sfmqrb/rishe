# Verification process log — verify-page-142


## [2026-09-05T20:08:18.479Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 142 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-142.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-142.json. Write /home/sfmqrb/git/rishe/data/verification/page-142.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 142` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:08:20.061Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:08:20.771Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:08:20.797Z] TOOL RESULT

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


## [2026-09-05T20:08:21.723Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-142.txt"
}
```


### [2026-09-05T20:08:21.796Z] TOOL RESULT

```
1	=== PDF page 142 (book page 112) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dumb, Dhumbhma : tail  (refs POK:227)
4	#1 (parent #0) [Avestan] refs=POK:227; HRN:128 | duma : tail
5	  #2 (parent #1) [Persian] refs=BQT:876,882 | dom, donb «دُم ، دُنب» : tail ; donbeh «دنبه» : fatty tail of a lamb | extra: دنباله
6	    #3 (parent #2) [Persian] refs=FVF:258; MON:1563 | donbal «دُنبَل» : abscess ; donbalân «دنبلان» : animal testicles
7	      #4 (parent #3) [Arabic] refs=FVF:258 | domal : abscess
8	        #5 (parent #4) [Persian] refs=MON:1561 | domal «دُمَل» : abscess | NOTE: See "Dus" for another possible root of "domal"
9	#6 (parent #0) [Persian] refs=BQT:878 | Damâvand «دماوند» : a mountain north of Tehran, originally a village at the mountain "tail" | NOTE: MON5:536 derives this word from the root "Dhem"
10	#7 (parent #0) [Persian] refs=MON:1563 | donbak, tonbak «دنبک ، تنبک» : a long tailed drum
11	#8 (parent #0) [Persian] refs=NYB:82 | každom «کژدم» : scorpion, literally "stinging tail"
12	#9 (parent #0) [Germanic] refs=POK:227 | tappa, tuppa : plug
13	  #10 (parent #9) [English] refs=AHD | tap, top, tip, tattoo, tampon
14	--- entry 1 ---
15	ROOT Dup -> redirect to Dub
16	
```


## [2026-09-05T20:08:24.878Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-142.json",
 "description": "Read source JSON page 142"
}
```


### [2026-09-05T20:08:24.932Z] TOOL RESULT

```
{
  "pdf_page": 142,
  "book_page": 112,
  "entries": [
    {
      "root": {
        "name": "Dumb, Dhumbhma",
        "lang": "Indo-European",
        "refs": "POK:227",
        "gloss": "tail"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:227; HRN:128",
          "words": [
            {"translit": "duma", "gloss": "tail", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:876,882",
          "words": [
            {"translit": "dom, donb", "gloss": "tail", "script": "دُم ، دُنب"},
            {"translit": "donbeh", "gloss": "fatty tail of a lamb", "script": "دنبه"}
          ],
          "script_extra": "دنباله",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "FVF:258; MON:1563",
          "words": [
            {"translit": "donbal", "gloss": "abscess", "script": "دُنبَل"},
            {"translit": "donbalân", "gloss": "animal testicles", "script": "دنبلان"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Arabic",
          "refs": "FVF:258",
          "words": [
            {"translit": "domal", "gloss": "abscess", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:1561",
          "words": [
            {"translit": "domal", "gloss": "abscess", "script": "دُمَل"}
          ],
          "note": "See \"Dus\" for another possible root of \"domal\"",
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:878",
          "words": [
            {"translit": "Damâvand", "gloss": "a mountain north of Tehran, originally a village at the mountain \"tail\"", "script": "دماوند"}
          ],
          "note": "MON5:536 derives this word from the root \"Dhem\"",
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:1563",
          "words": [
            {"translit": "donbak, tonbak", "gloss": "a long tailed drum", "script": "دنبک ، تنبک"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Persian",
          "refs": "NYB:82",
          "words": [
            {"translit": "každom", "gloss": "scorpion, literally \"stinging tail\"", "script": "کژدم"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Germanic",
          "refs": "POK:227",
          "words": [
            {"translit": "tappa, tuppa", "gloss": "plug", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "tap, top, tip, tattoo, tampon", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Dup",
        "redirect": "Dub"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T20:08:25.284Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:08:25.380Z] TOOL RESULT

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


## [2026-09-05T20:08:36.534Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && python3 -c \"\nimport json\nd=json.load(open('sources/refs_online.json'))\nfor k in ['POK','HRN','BQT','MON','FVQ','FVF','NYB','AHD','PHD','BRT','CHEUNG','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Check refs_online entries"
}
```


## [2026-09-05T20:08:37.438Z] TOOL CALL #6: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/ | head -50; echo ---; ls /home/sfmqrb/git/rishe/data/verification/page-127.json && head -c 3000 /home/sfmqrb/git/rishe/data/verification/page-127.json",
 "description": "List verification dir and sample file"
}
```


### [2026-09-05T20:08:38.105Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists 

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

CHEUNG null

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


### [2026-09-05T20:08:38.151Z] TOOL RESULT

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
page-43.json
page-44.json
page-45.json
page-46.json
page-47.json
page-48.json
page-49.json
page-50.json
---
/home/sfmqrb/git/rishe/data/verification/page-127.json
{
 "pdf_page": 127,
 "book_page": 97,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05",
 "entries": [
  {
   "entry": 0,
   "root": "Dhem",
   "verdict": "confirmed",
   "modern_form": "PIE *dʰemH- (LIV² *dʰmeh₁-) 'to blow, breathe; to smoke, raise dust'",
   "note": "Pokorny IEW 247-248 heads the entry 'dhem-, dhemə- \"stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)\"', so Nourai's language label (Indo-European) and his gloss 'to make vapor, raise dust' are an accurate short rendering of the German. Cheung (Etym. Dict. of the Iranian Verb, *damH³) writes the same root «PIE *dʰmeH- 'to blow' = LIV: 153 | Pok.: 247 f.»; Wiktionary reconstructs *dʰemH-. Watkins/AHD carries no dhem- root (its list goes dhembh- → dhen-¹), simply because no English word reaches it through Latin or Greek, so its silence is not a disagreement. Two weak spots in the chart: the Avestan node's gloss (node 1) and the name Damāvand (node 2), which Nourai's own source BQT:878 derives from a different root.",
   "note_fa": "ریشهٔ نمودار همان ریشهٔ هندواروپاییِ آغازینِ *dʰemH- «دمیدن، فوت کردن؛ دود و بخار برخاستن» است. پوکورنی در صفحهٔ ۲۴۷ کتاب خود آن را با معنای آلمانیِ «stieben, rauchen … wehen, blasen» آورده و برگردانِ کوتاهِ نورایی («بخار ساختن، گرد برانگیختن») با آن می‌خواند؛ چونگ نیز همین ریشه را *dʰmeH- «دمیدن» (LIV ۱۵۳) می‌نویسد. پس جعبهٔ ریشه، برچسبِ زبان و معنای آن درست است و ادعای نورایی در این حد پذیرفتنی است. تنها دو نقطهٔ سست در نمودار هست: معنایی که برای صورتِ اوستایی داده شده (گرهٔ ۱) و نامِ «دماوند» (گرهٔ ۲) که خودِ مأخذِ نورایی، یعنی حاشیهٔ معین بر برهان قاطع ص ۸۷۸، آن را از ریشهٔ دیگری می‌گیرد.",
   "sources": [
    "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86",
    "https://en.wiktionary.org/wiki/%D8%AF%D9%85"
   ],
   "ref_check": [
    {
     "ref": "POK:247",
     "status": "supports",
     "note": "POK_01.txt (grep -n 'dbem-' → line 3513), IEW p.247: 'dbem-, dhemo- ,stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben == düster, dunkel), wehen, blasen (hauchen = riechen)'; the page continues 'Ai. dhámati ,bläst', av. daδmainya- …, npers. damīdan ,blasen, wehen', dam ,Atem, Atemzug''. Exactly the root box as drawn."
    }
   ],
   "consulted": [
    {
     "src": "WLD",
     "where": "Bd. I 851 f. (WLD_Bd1 djvu line 53642)",
     "stance": "supports",
     "note": "'dhem-, dhemə- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = rieche
```


## [2026-09-05T20:08:43.420Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && python3 -c \"\nimport json\nd=json.load(open('page-127.json'))\nfor e in d['entries']:\n    for n in e['nodes']:\n        if 'am' in (n.get('words') or '') and 'vand' in (n.get('words') or ''):\n            print(json.dumps(n, ensure_ascii=False, indent=1))\n\"",
 "description": "Extract Damavand node from page 127"
}
```


### [2026-09-05T20:08:45.303Z] TOOL RESULT

```
{
 "id": 2,
 "lang": "Persian",
 "words": "dam «دَم»; damîdan «دمیدن»; damâ «دما»; Damâvand «دماوند»",
 "verdict": "disputed",
 "derivation": "Three of the four words are right, the fourth is not, so the node takes the worst verdict. (1) دم dam 'breath' < Middle Persian dam (Manichaean/Book Pahlavi dm-, /dam-/) < Proto-Iranian *damH- < PIE *dʰemH-; MacKenzie's Concise Pahlavi Dictionary has 'daftan, dam- [dptn', dm- | M dm-, N dam-idan] breathe, blow. ~išn: breath', and 'damidan [dmytn'] = daftan'. This is a different word from the homophone دم 'tail' (< dunb, Av. duma-), which Horn keeps apart as his no. 573. (2) دمیدن damīdan 'to blow, breathe' is the New Persian regularisation of MP daftan (past stem daft) on the present stem dam-: the inherited -ft- past was replaced by the productive -īd- suffix, exactly as MacKenzie's 'damidan = daftan' records; hence Horn no. 572 'dem \"Atem, Atemzug\", deme, demīden \"wehen, blasen\"'. (3) دما damā is a nominal derivative of dam with the abstract/nomen suffix -ā; Borhan-e Qāteʿ p.877 glosses it 'بمعنی دم و نفس باشد' with Moʿin's footnote '۱ رك: دم' ('see dam'), i.e. 'breath'. Nourai's gloss 'weather, heat' is the modern technical sense ('temperature', as in دماسنج 'thermometer'), which Aryanpur records explicitly; that sense is 20th-century, not classical, so the word is right but the gloss is anachronistic. (4) دماوند Damāvand does NOT belong here. In Islamic sources the name is written دنباوند dunbāvand, and Moʿin's own footnote on the page Nourai cites (BQT:878) reports Kasravi's derivation from دُما/دنب 'back, behind' + the suffix -vand (paired with نهاوند Nahāvand from نها 'front'); Wiktionary likewise gives 'from Middle Persian dmbʾwnd (dumbāwand)'. The 'mountain of vapour' reading is a folk etymology built on the homophony of dam 'breath/vapour' with dam < dunb 'tail, rear'. Nourai's own NOTE flags the conflict; modern scholarship sides with BQT:878 against the chart.",
 "derivation_fa": "از چهار واژهٔ این گره سه تا درست است و یکی نادرست، پس حکمِ گره همان بدترین حکم می‌شود. ۱) «دَم» به معنی نفس از فارسی میانهٔ dam (پهلویِ کتابی dm-)، از ایرانی باستان *damH-، از هندواروپایی آغازین *dʰemH- است؛ مکنزی در فرهنگ کوچک پهلوی می‌آورد: «daftan, dam- … breathe, blow؛ damišn نفس». این «دم» با «دمِ» هم‌آوایِ به معنی دنباله (از dunb، اوستایی duma-) یکی نیست و هرن هم آن دو را در شمارهٔ ۵۷۲ و ۵۷۳ جدا کرده است. ۲) «دمیدن» صورتِ قاعده‌مندشدهٔ فارسی نو از مصدرِ پهلویِ daftan است: ستاکِ حالِ dam- را گرفته و پسوندِ زایای -ید- را جایگزینِ گذشتهٔ -ft- کرده‌اند؛ همان که مکنزی با «damidan = daftan» ثبت کرده است. ۳) «دما» اسمی است از «دم» با پسوندِ -ا؛ برهان قاطع (ص ۸۷۷) آن را «بمعنی دم و نفس» می‌داند و معین در حاشیه می‌نویسد «رك: دم». معنایی که نورایی داده («هوا، گرما») همان کاربردِ نوِ فرهنگستانی است (چنانکه در «دماسنج») و آریان‌پور نیز آن را یاد کرده؛ پس واژه درست است ولی معنا امروزی است نه کلاسیک. ۴) «دماوند» به این ریشه ربطی ندارد: در مآخذ اسلامی «دنباوند» آمده و معین در همان صفحه‌ای که نورایی ارجاع داده (ص ۸۷۸) تحقیق کسروی را نقل می‌کند که آن را از «دُما/دنب» به معنی پشت و دنبال + پسوندِ «وند» می‌گیرد (در برابرِ «نهاوند» از «نها» به معنی پیش)؛ ویکی‌واژه نیز آن را از فارسی میانهٔ dumbāwand می‌داند. «کوهِ بخاردار» ریشه‌شناسیِ عامیانه‌ای است بر پایهٔ هم‌آواییِ «دمِ» نفس با «دمِ» دنباله. خودِ نورایی هم در یادداشت به این اختلاف اشاره کرده است؛ پژوهش امروزی جانبِ برهان قاطع را می‌گیرد و این پیوند را رد می‌کند.",
 "sources": [
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86",
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85",
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85%D8%A7%D9%88%D9%86%D8%AF"
 ],
 "ref_check": [
  {
   "ref": "POK:247",
   "status": "supports",
   "note": "IEW 247 (POK_01.txt line 3517-3518): 'npers. damīdan ,blasen, wehen', dam ,Atem, Atemzug'' — covers dam and damīdan, but says nothing of damā or Damāvand."
  },
  {
   "ref": "BQT:876,877",
   "status": "supports",
   "note": "BQT_v2_pages.txt leaf 336 = printed p.876 (offset printed = leaf+540, confirmed by the دماوند entry falling on leaf 338 = p.878, the page Nourai's own NOTE cites): headword «دم» with Moʿin's footnote 5 «هندی باستان dhamati (نفس کردن > دمیدن)؛ پهلوی dam نفس؛ اُستی dimin, dumun (دمیدن، وزیدن)؛ کردی dem؛ بلوچی dam». Leaf 337 = p.877 has «دما … بمعنی دم و نفس باشد» with footnote «۱ رك: دم». Note that footnote 7 on p.876 is the separate دم 'tail' entry (اوستا duma-, پهلوی dum, dumb …), i.e. the 'Dumb' root."
  },
  {
   "ref": "HRN:127",
   "status": "supports",
   "note": "HRN.txt leaf 149 (printed p.127, leaf = printed + 21), entry 572: 'dem \"Atem, Atemzug\", deme, demīden \"wehen, blasen\", demāγ, demār. ai. √dham-; dhámiti \"hauchen, blasen\"; phlv. dam; ksl. dŭmǫ, dǫti \"blasen\"' (continuing on p.128 with oss. dumun, dimin). Horn's very next entry, 573, is 'dum, dumb, dumbe \"Schwanz\"' — the root under which Damāvand belongs."
  }
 ],
 "consulted": [
  {
   "src": "PHD",
   "where": "MacKenzie, s.v. daftan / damidan (PHD.txt line 306; PHD_mackenzie.txt line 1864)",
   "stance": "supports",
   "note": "'daftan, dam- [dptn', dm- | M dm-, N dam-idan] breathe, blow. ~išn: breath.' and 'damidan [dmytn'] = daftan.' — gives the exact Middle Persian ancestor of both دم and دمیدن."
  },
  {
   "src": "CHEUNG",
   "where": "s.v. *damH³ (CHEUNG.txt line 4670-4712)",
   "stance": "supports",
   "note": "'*MIDDLE PERSIAN: MMP dm- …, BMP dm- /dam-/ \"to breathe\" … Inf.: BMP dptn /daftan/' and '*NWIR: NP damidan/dam- \"to blow; to breathe; to blossom; to appear (as the dawn)\"'."
  },
  {
   "src": "ARY",
   "where": "ARY_pages.txt pdf page 282 = printed p.283, s.v. دمیدن",
   "stance": "supports",
   "note": "'دمیدن (به چم «نفس کشیدن» و «فرت کردن یا ورزیدن»)' with Pahlavi damīdan/damīnīdan, Ossetic dumun/dimin, Sanskrit dhamati, Lithuanian dūmti and English DAMP, DAMPER among the descendants; footnote ۲ says «واژهٔ \"دما\" به چم \"گرما\" هم بکار می‌رود (مثلاً در \"دماسنج\")», i.e. it confirms Nourai's 'weather, heat' as a (modern) sense of دما."
  },
  {
   "src": "HUB",
   "where": "Persische Studien (grep 'dam' in HUB.txt)",
   "stance": "silent",
   "note": "Hübschmann's word list has no entry for dam/damīdan; the hits are unrelated (andām, kudām, hamdam)."
  },
  {
   "src": "BQT",
   "where": "leaf 338 = printed p.878, s.v. دماوند",
   "stance": "contradicts",
   "note": "Moʿin's footnote ۵: «دماوند که در مآخذ اسلامی \"دنباوند\" آمده، بنا به تحقیق مرحوم کسروی … مرکب است از \"دما\" (ضم دال) بمعنی پشت و دنبال، چنانکه \"نهاوند\" نیز مرکب است از \"نها\" بمعنی پیش … جزو دوم در هر دو نام \"وند\" پسوند …» — i.e. Damāvand belongs to the dumb 'tail, rear' root, not to dam 'vapour'. This is the note Nourai himself reports."
  }
 ]
}
```


## [2026-09-05T20:08:59.289Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dumb\" POK_01.txt | head -40; echo \"=== tuppa\"; grep -n \"tuppa\\|tappa\" POK_01.txt | head -20",
 "description": "Grep Pokorny for dumb"
}
```


### [2026-09-05T20:08:59.356Z] TOOL RESULT

```
2565:Ebenfalls  fernzuhalten  sind  ahd.  zahalön,  nhd.  zappeln,  sowie  ahd. zapfo,  nhd.  Zapfen,  ags.  txppa  ds.  (germ.  *tappon-)]  ebenso  nur  germ. Worte  mit  i  und  u  (vgl.  Specht  Dekl.  152 f.):  mengl.  tippen,  engl,  tip ,loise  anrühren,  leise  stoßen^,  nhd.  tippen,  mhd.  zipfen  ,(in  kurzen  Bewe- gungen) trippeln^,  anord.  tifask  ,trippeln^,  mhd.  zipf  ,Zipfel,  Spitze^, nasaliert  mnd.  timpe  f.  , Zipfel,  Ende^,  ags.  ä-timplian  ,mit  Nägeln  ver- sehen^; andrerseits  norw.  mdartl.  tuppa,  nhd.  zupfen,  anord.  toppr  ,Haar- schopf,  Gipfel'^,  ags.  topp  m.  ,Spitze,  Zipfel',  toppa  m.  ,Faden^,  ahd. zopf  ,Zopf,  Haarflechte,  Ende  eines  Dings^;  mnd.  tuhhe,  tobbe  ,Zapfen^, tobben  ,zupfen,  reißen'^,  süddt.  zöfeln  ,zögern^  (wie  zapf  ein)]  vielleicht  hierher auch  ahd.  zumpo  ,penis^,  mhd.  zumpf{e),  nhd.  Zumpt,  worüber  unter  dumb-.
3251:Av.  duma-  m.  ^Schwanz',  npers.  durrij  dumb  (*dum(}i)ma-)j  ahd.  zumpfo penis';  mhd.  zum2J>f{e),  zumpfelin  (Sütterlin  IF.  4,  93);  dazu  vielleicht  av. dumna-  n.  ;Hand  (?)'  (*dumbna-),  s.  Scheftelowitz  IF.  33,  142  mit  zahl- reichen Parallelen  für  die  Bed.-Entw.  ^Stange^  Stab  —  penis,  Schwanz' und  ,Stab  —  Arm,  Hand'.  Wohl  zu  mnd.  timpe  ;Spitze_,  Gipfel',  ags. atiinplian  ,mit  Nägeln  versehen',  nasal.  Form  von  germ.  *tippa  ,Zipfel' in  engl,  tip  _,Spitze',  mhd.  zipf[el)]  germ.  *tuppa-  ,Zopf'  in  anord.  toppr ds.,  ags.  topp  m.  ,Gipfel',  mhd.  zopf  ^Zopf,  Ende  eines  Dinges',  mit  bb: mnd.  tobbe,  tubbe  , Zapfen',  vgl.  Xqü.  duba  ,aufgestellte  Garbe';  germ. *tappan  ,Zapfen'  in  ags.  tssppa  m.  (engl,  tap)^  mnd.  tappe  m.,  ahd.  zapho, mhd.  zapfe  m.  Offenbar  ,mot  populaire'  mit  intensiver  Konsonantenschär- fung,  Nasalierung  und  Vokalwechsel  a:i:ii'^  vgl.  oben  S.  221  drop- :  drip- : drup-.    S.  auch  oben  S.  177.
3527:mit  germ.  -h-:  schwed.  dial.  dimha  st.  V.  ,dampfen,  rauchen,  stieben* dimba  ,Dampf^,  norw.  damh  n.  ,Staub^,  anord.  dumba  ,Staub,  Staubwolke' (daneben  mit  -mm-  anord.  dimmr  ,dunkeU,  afries.  ags.  dimm  ds.,  norw. mdartl.  dimma,  dumma  ,Unklarheit  in  der  Luft,  Nebeldecke^,  schwed. dimma  ,dünner  NebelQ,  ahd.  timber,  mhd.  timher,  timmer  ,dunkel,  finster, schwarz^;
3790:Nasaliert  got.  dumbs,  anord.  dumbr,  ags.  dumb  ,stumm',  ahd.  tumh ,stumm,  dumm,  unverständlich',  as.  dumb  ,ein fältig'.  Doch  scheint  ein *dhu-m-bhos  ,dunkel'  auch  durchs  Slav.  gestützt  zu  werden  (s.  unten).
3791:Vielleicht  (Berneker  215)  aksl.  dgbz  ,Eiche,  dann  Baum  überhaupt'  - als  ,Baum  mit  dunkelm  Kernholz'  wie  lat.  röbur.  Dagegen  kann  bei  lett. dumbra  zeme  ^schwarzes  Moorland'  usw.  b  Einschublaut  zwischen  m  und r  sein,  s.  oben,  ebenso  bei  lit.  duihblas  ,Schlamm'  (mhd.  tümpfel,  nhd.  Tümpel, Prellwitz  KZ.  42,  387,  vielmehr  zu  nhd.  tief,  mnd.  dumpelen  ,untertauchen', s.  Schulze  SBpr.Ak.  1910,  791  ==  Kl.  Sehr.  114).
3839:lit.  dubiis  ,tief,  hohl',  dazu  die  FIN  Dübe,  Dubingä  und  Dubysa  (== cymr.  FIN  Dyfi  aus  *Dublsä,  Pokorny  Urillyrier  46  f.),  dügnas  ,Boden' (wohl  wegen  lett.  dibens  aus  *ditbnas  =  slav.  *d^bno,  gall.  dubno-]  s.  die Lit.  bei  Berneker  245 f.);  auch  der  FIN  wruss.  Dubna  (==  lett.  Dybnoja) ,der  tiefe  Fluß'  und  die  apr.  ON  Dum{p)nisj  Dubna  zeigen  noch  bn; dumbüj  dübti  ,hohl  werden,  einsinken',  daubä,  dauburys  ,Schlucht',  düobti ,aushöhlen',   duobl  ,Höhle'   (lett.  duobs,  dtiobjS   ,tief,   hohl',  düobe   ,Grube,
=== tuppa
2564:Aus  dem  Genn.  reiht  man  noch  vieles  an,  was  eine  Bed.-Entw.  von «erteilen^  zu  ,zerreißen,  zupfen,  kurz  betasten,  kurze  täppische  Bewegun- gen machen^  u.  dgl.  voraussetzen  würde;  am  nächsten  der  Bed.  von  öa- naväv  damnum  kommt  aschw.  tappa  und  iapa  ,ein  Ende  machen,  ver- lieren^;  aisl.  tapa  ds.;  afries.  tapia  ,zupfen^,  ags.  tssppe  f.  ,Tuchstreifen^, meno-1.  tappen  (engl,  tap)  ,leicht  schlagen^,  mnd.  tappen,  täpen  (Dehnung in  offener  Silbe?)  ,zupfeu,  pflücken*^;  anord.  tcepr  ,kaum  anrührend^,  isl. i4h)ta  (*täpatjan)  ,eben  anrühren^,  norw.  mdartl.  tcepla  ,leicht  berühren, leise  treten^;  aber  norw.  mdartl.  taap{e)  m.,  dän.  taahe  ,Tor,  Tropf,  täp- pischer Mensch^,  norw.  taapen  ,schwach,  kraftlos,  untauglich^,  tcepe  n. unbedeutendes  Ding^,  anord.  föepiligr  ,knapp^,  mit  anderen  Labialstufen 8chwed.  mdartl.  tahh,  tahhe  ,Tölpel^,  tahhet  ,einfältig^,  sind  wohl  Schall- worte, ebenso  wie  ndd.  tappe,  Schweiz,  täpe,  nhd.  Tappe  ,Pfote^,  sowie iavpen,  täppisch  usw.;  s.  auch  unter  1.  dhabh-.
2565:Ebenfalls  fernzuhalten  sind  ahd.  zahalön,  nhd.  zappeln,  sowie  ahd. zapfo,  nhd.  Zapfen,  ags.  txppa  ds.  (germ.  *tappon-)]  ebenso  nur  germ. Worte  mit  i  und  u  (vgl.  Specht  Dekl.  152 f.):  mengl.  tippen,  engl,  tip ,loise  anrühren,  leise  stoßen^,  nhd.  tippen,  mhd.  zipfen  ,(in  kurzen  Bewe- gungen) trippeln^,  anord.  tifask  ,trippeln^,  mhd.  zipf  ,Zipfel,  Spitze^, nasaliert  mnd.  timpe  f.  , Zipfel,  Ende^,  ags.  ä-timplian  ,mit  Nägeln  ver- sehen^; andrerseits  norw.  mdartl.  tuppa,  nhd.  zupfen,  anord.  toppr  ,Haar- schopf,  Gipfel'^,  ags.  topp  m.  ,Spitze,  Zipfel',  toppa  m.  ,Faden^,  ahd. zopf  ,Zopf,  Haarflechte,  Ende  eines  Dings^;  mnd.  tuhhe,  tobbe  ,Zapfen^, tobben  ,zupfen,  reißen'^,  süddt.  zöfeln  ,zögern^  (wie  zapf  ein)]  vielleicht  hierher auch  ahd.  zumpo  ,penis^,  mhd.  zumpf{e),  nhd.  Zumpt,  worüber  unter  dumb-.
3251:Av.  duma-  m.  ^Schwanz',  npers.  durrij  dumb  (*dum(}i)ma-)j  ahd.  zumpfo penis';  mhd.  zum2J>f{e),  zumpfelin  (Sütterlin  IF.  4,  93);  dazu  vielleicht  av. dumna-  n.  ;Hand  (?)'  (*dumbna-),  s.  Scheftelowitz  IF.  33,  142  mit  zahl- reichen Parallelen  für  die  Bed.-Entw.  ^Stange^  Stab  —  penis,  Schwanz' und  ,Stab  —  Arm,  Hand'.  Wohl  zu  mnd.  timpe  ;Spitze_,  Gipfel',  ags. atiinplian  ,mit  Nägeln  versehen',  nasal.  Form  von  germ.  *tippa  ,Zipfel' in  engl,  tip  _,Spitze',  mhd.  zipf[el)]  germ.  *tuppa-  ,Zopf'  in  anord.  toppr ds.,  ags.  topp  m.  ,Gipfel',  mhd.  zopf  ^Zopf,  Ende  eines  Dinges',  mit  bb: mnd.  tobbe,  tubbe  , Zapfen',  vgl.  Xqü.  duba  ,aufgestellte  Garbe';  germ. *tappan  ,Zapfen'  in  ags.  tssppa  m.  (engl,  tap)^  mnd.  tappe  m.,  ahd.  zapho, mhd.  zapfe  m.  Offenbar  ,mot  populaire'  mit  intensiver  Konsonantenschär- fung,  Nasalierung  und  Vokalwechsel  a:i:ii'^  vgl.  oben  S.  221  drop- :  drip- : drup-.    S.  auch  oben  S.  177.
```


## [2026-09-05T20:09:00.798Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==235||NR==236 {print \"=== leaf \" NR \"\\n\" $0}' POK_01.txt | head -120",
 "description": "Print Pokorny leaf around p227"
}
```


### [2026-09-05T20:09:02.840Z] TOOL RESULT

```
=== leaf 235
]
o-ot.  tuggö  Ly  an.  as.  tunga^  ags.  tunge,  ahd.  zitnga^  mit  -ön-  statt  -ä; als  Ablautneubildung  vielleicht  hierher  ^nord.  tangi  ,Griffstück  der  Klinge^ rand.  tange  _,Sandrückea  zwischen  zwei  Sümpfen^;
bsl.  inzä-  m.  in  apr.  insuwis]  lit.  liezüvis  (nach  liezti  ,lecken');  aksL j§zy-ki,  skr.  jezik,  poln.  jezyk^  russ.  jazyk;  zum  Schwund  des  anlaut.  c^- s.  J.  Schmidt,  Krit.  77;
toch.  A  käntu,  Gen.  käntwis,  B  känfwo,  Obl.  käntwa  sa  {^kantwaj  um- gestellt aus  '^tankica,  idg.  *dnghua).
WP.  I  1792,  WH.  I  8U6f.,  Trautmann  104,  Specht  Dekl.  83,  Havers Sprachtabu  123  f.
cfö-  :  d9',  auch  dö-u-  :  dQU-  :  cfu-  ,geben^  (perfektiv),  Aoristwurzel  mit  sekun- därem    Präsens     di-dö-mi,     Nominaibildungen:    do-no-m,    dö-ro-tn^ dö'ti-s,    d9-ti-s    ,Gabe',    dö-ter-    ,Geber^,    Partiz.    dö-to-s,    dQ-to-s, 'd-tos,  Infinitiv  dö-men-ai,  dö-uen-ai. Ai.    dd-dä'ti  (Aor.  d-dä-m,   Opt.   deyäm,   Fut.  däsydti,   Aow  Med.  ddita ==  gr.    eöozo,   Inf.  ddmane  :  gr.  ööjxsvai,   vgl.   lat.  daminl,  falls   ursprüngh Infinitiv)  ^gibt*"  (päli  cZmna  zu  einem  Präs.  "^di-dä-ti),  av.  dadäiti  ds.,  apers. Imp.    dadätuv    ,er    soll   geben';  Wurzelnomen    ai.    dä[s]  dstu  ,dator    estu'; Infin.    dätum    (:lat.    Supin.    cZa^wm);    Partiz.    ditd-h    (unbelegt),    sekundär dattd-h,  schwundstuf,  in  ä-t-td-h,  prd-t-ta-h  ^hingegeben',  ablaut.  in  tvä-däta-h ,von  dir  gegeben',  av.  däta-j  zum  Fut.  ai.  däsyämi  (:  lit.  düosiu)  s.  Schwyzer Gr.  Gr.  I  78811;
arm.  ta-m  ,dö',  ta-m¥  ,damus'  {*dd-ie-mi)j  Aor.  etu  (==  d-dä-m,  idg. *e-c?ö-m);
224
gr.  öl'dco-^u  ,gebeS  Aor.  edcüVM,  Opt.  öoi7]v  (*donem),  Fut.  dwao),  Aor. Med.  l'JoTO;  Partiz.  doTÖg,  Infin.  hom.  öö^evai  und  hom.  tliess.  usw.  do'^jj, (su  ffixloser  Lokativ) ;
ven.  zoto  ,dedit^  =  gr.  eöoTO]  zonasto  ^döiiävit^  vielleicht  aus  *dönä-s-to von  einem  denom.  *dönäiö  (*c?ö?20-m  :  lat.  dömim)]  mess.  pi-do  (*dö-t:^[^ ■a-dät):
alb.  da-sh'd  Aor.  ^icli  g'aV  (*dd-S7n)]
lat.  döj  das,  dat,  dämus  (*dd-mös),  dätis,  dänt  (sekundär  für  *dent  aus *{di)-dn-ti),  alat.  danunt;  dedl,  dätum,  däre  ;gebe^  gewähre^,  refl.  ^begebe niich^  [das  mit  ä  nach  stä-  für  *c?ö  =  lit.  diid,  düo-h  [Specht  KZ.  55 182],  gr.  hom.  di-öio-d-i)',
vest.  di-de-t  ^dat^^,  pal.  cZi-<?a  ,det-,  mixCov.  dir sa,  der sa,  tera  ^det^  (*didät) tePtu,  dirstu,  titii  ^dato^  (*d{-de-töd),  tefte  ,datur^  {*di-da-ter)j  a-tef-a-fnst jCircumtulerit^  (^am-de-da-fos-t)-^  osk.  da\^da]d  ^dedaf^  (*däd(-di)-däd),  dadid ,dederit^  (*däd(-de)-did),  
=== leaf 236
di-de-st  ^dabit'^  dedet,  umbr.  dede  ,dedit^  (=  lat. d^-d-tt,  alt  dedet)j  umbr.  tefustj  dirsust  ^jdederit*^  (*dedust),  usw.;  isX.  porded ,porrexit^  (*por(-deyded)]
redupl.  Präsens  ital.  *di-dö(?)  in  lat.  reddö  {reddidtj  redditum,  reddere) jgebe  zurück'  aus  *re-d(iydö(?)  ist  angeblich  themat.  Umgestaltung  von *di-dö-mi',  andere  Komposita  sind  de-dö,  dl-dö,  e-dö,  prö-dö,  trä-dö  und ven-dö]
Partiz.  lat.  dätus  ^gegeben'  =  falisk.  datu  ,datum^^  vest.  data  ^data', päl.  datas  ^datas^  (- S^^-  doTÖg)j  Supin.  datum  (:ai.  Infin.  dätum)\
hierher    vielleicht   trotz    VYH.  I  193   lat.  ce-dö   .siih    her!^  PL    cette
>xs'
aus
^ce-d9te  (:gr.  Sörs);
lit.  duomi  (heute  sekundär  duodu,  lett.  duodu,  neugebildet  zum  alit. Ipv.  duodi  aus  "^dö-dhi-,  ostlit.  düomu),  2.  Sg.  düosi,  3.  Sg.  düost{i)  ,^\hi', apr.  däst  ds._,  beruhen  nach  Kofinek  Listy  filol.  65^  445  und  Szemerenyi Et.  Slav.  Roum.  1,  7  ff.  (vgl.  E.  Fraenkel  Balt.  Sprachw.  11  f.)  nicht  auf alter  Reduplikation  (angebl.  *dö-dd-mi,  bsl.  "^dödmi,  3.  Sg.  *dö-dd-ü,  bsl. *dödti  >  *dösti),  sondern  auf  unreduplizierter  athemat.  Flexion  (*dömi, PL  *ddmös);  lit.  düosti,  abg.  dast^  sind  Nachahmungen  von  lit.  hti  ,ißt' usw.,  die  neben  lit.  *e(d)mij  abg.  janib  (aus  ^ed-m-)  liegen^,  wo  das  d  der Wurzel  als  suffixal  empfunden  wurde;  zum  Fut.  lit.  duosiii  s.  oben  S.  223.
Dasselbe  würde  gelten  von  aksl.  daim  ,ich  werde  geben*,  3.  PL  dadeti (nach  jadet^  usw.);  aksl.  dazda  ,Gabe^  ist  Analogiebildung  nach  *edja ,Essen',  wo  das  d  wiederum  als  Formans  betrachtet  wurde.
Infin.  lit.  düoti,  lett.  duot,  apr.  dät  {^dö-tl-)  =  aksl.  dati^  serb.  däti, russ.  dath.  ?
Zum  Prät.  lit.  daviaü,  lett.  devu  ,gab^  s.  unten.  '
225
partiz.  *dö-na-  in  Siksl.  pre-dam,  serb.  dän,  cech.  ddn,  klr.  ddnyj  , gegeben' , *dö-tcL-  ds.  in  apr.  däts,  lit.  düotas,  lett,  cZwo^s;  einzelsprachl.  Neuerungen <;iiul  serb.  dial.  dät,  cech.  c^a^^;  dazu  lit.  duotina  ;,mannbar^^  russ.-ksl. jwdatbm,  russ.  poddtnyj  .freigebig^;  Supin.  *dötun  ,zu  geben^  in  apr.  daton (lüfin.);  lit.  c?MO%  aksl.  ohdah,  sloven.  dat,  vgl.  slav.  *datz-H  in  sloven. Jodätek,  poln.  dodatek,  russ.  doddtok  , Zugabe^;
hitt.  c?ä-  ,nehmen^^  1.  Sg.  da-ah-hi  {dahhi),  3.  Sg.  c?a-a-i  (c?äi),  wird  von Pedersen  (Mursilis  68)  und  Kretschmer  (Glotta  19^  207)  hierher  gestellt /treben^  —  :?^ür  sich  geben^  —  ^nehmen^);  dagegen  Couvreur  ^  206 ff.
Xominalbildungen:  ai.  dätar-j  dätdr-  ^Geber^^  gr.  (Jwtw^,  dojTrjo  ds., schwachstufig  (JottJo,  öÖTSiga,  lat.  cZa^o?-,  datrix.  —  Ai.  dätrd-,  av.  dä^ra- ji.  ^Geschenk^.
*dö-tel-  in  aksl.  dateljh  (*dö-tel-iu-)  ^Geber*^^  cech.  udatel  ^Angeber^,  russ. ddteh  ^Geber'.
Ai.  *däti'  ^Schenkung
```


## [2026-09-05T20:09:08.383Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=3251{n+=gsub(/\\f/,\"\")} END{print \"formfeeds before line 3251:\", n}' POK_01.txt; echo \"---context---\"; sed -n '3240,3260p' POK_01.txt",
 "description": "Locate Pokorny dumb page"
}
```


### [2026-09-05T20:09:09.990Z] TOOL RESULT

```
formfeeds before line 3251: 238
---context---
gr.  hom.  Aor.  edgaO^ov  {*e-dr-dh-om)j  jünger  edaqd-ov  ,schlief^,  sekundär ■naTadaQS-dvcü  ,schlafe  ein^;
lat.  dormiö  ,schlafe,  schlummere^  (*c?2'7m-uö)  ;
slav.  *dremiö  ,schlummere^  in  ksl.  dremlju  drimati  ,schlummern',  serb.-| drijemljem  drijemati  ,Schlaflust  haben^,  usw.
Über   die   formalen  Verhältnisse  s.  EM.  284,  zur  -em-Erweiterung  auch Pedersen  Groupement  22.
WP.  I  821,  WH.  I  372,  Trautmann  60.
dregh-   ,unwillig,  verdrossen^,  oder  vielleicht  ursprünglicher  ,schlaff,  zähe^ sein^?  -^
Got.    trigo   ,Trauer,  Widerwille^,   anord.    tregi    m.    ,Trauer,    Hindernis'/^ tregr  ,un willig,  ungeneigt^,  treginn  ,betrübt^,  ags.  trega  m.  ,Trauer,  Leiden',  _
^s^-
227
treqo  m.  ^Schmerz^,,  tregan  (nur  Inf.)  mit  Dat.  ^leid  sein^,  mndl.  tregen ficu  Hut  verlieren^  auord.  trega  =  ags.  tregian  ,betrüben^;  vgl.  mit  einer '-olil  alten  konkreten  Bed.  ^zähe,  zähe  haftend'  norw.  radartl.  treg  auch au'=;dauernd^  fest^^  trege  ,zähe  Faser^  Sehne^  harte  Haut^,  ischwed.  trägen 'unermüdlich^;  dehnstufig-  ahd.  trägi  ^träge,  langsam,  verdrossen'^  as.  trag 'schlecht'^  ags.  trüg  f.  ,Leiden^  Übel';  as.  ahd.  trägl  f.  ^Trägheit,  Verdruß'; lit.  dryz-tü,  drizau,  drizti  ^matt^  schlaff  werden'  (Büga  Kalba  ir.  s.  219)^ drizinti  ^schlaff  machen';  zum  lit.  ri  vgl.  Hirt  Idg.  Gr.  II  83. Wr.  I  ^21  f.;  Persson  Beitr.  46  f.
dumh-  (-hh?)  ^penis^  Schwanz',  vielleicht  eigentlich  ^Stab'.
Av.  duma-  m.  ^Schwanz',  npers.  durrij  dumb  (*dum(}i)ma-)j  ahd.  zumpfo penis';  mhd.  zum2J>f{e),  zumpfelin  (Sütterlin  IF.  4,  93);  dazu  vielleicht  av. dumna-  n.  ;Hand  (?)'  (*dumbna-),  s.  Scheftelowitz  IF.  33,  142  mit  zahl- reichen Parallelen  für  die  Bed.-Entw.  ^Stange^  Stab  —  penis,  Schwanz' und  ,Stab  —  Arm,  Hand'.  Wohl  zu  mnd.  timpe  ;Spitze_,  Gipfel',  ags. atiinplian  ,mit  Nägeln  versehen',  nasal.  Form  von  germ.  *tippa  ,Zipfel' in  engl,  tip  _,Spitze',  mhd.  zipf[el)]  germ.  *tuppa-  ,Zopf'  in  anord.  toppr ds.,  ags.  topp  m.  ,Gipfel',  mhd.  zopf  ^Zopf,  Ende  eines  Dinges',  mit  bb: mnd.  tobbe,  tubbe  , Zapfen',  vgl.  Xqü.  duba  ,aufgestellte  Garbe';  germ. *tappan  ,Zapfen'  in  ags.  tssppa  m.  (engl,  tap)^  mnd.  tappe  m.,  ahd.  zapho, mhd.  zapfe  m.  Offenbar  ,mot  populaire'  mit  intensiver  Konsonantenschär- fung,  Nasalierung  und  Vokalwechsel  a:i:ii'^  vgl.  oben  S.  221  drop- :  drip- : drup-.    S.  auch  oben  S.  177.
WP.  I  816,  Fick  III  155,  164,  168,  Petersson  Heterokl.  70  f.
cfus-  ,übel,  miß-'  als  1.  Kompositionsglied.
Ai.  dus-,  dur-,  av.  diLS-,  duz-  ,miß-,  übel',  arm.  t-  ,un-',  gr.  ovo-  ,miß-, übel',  lat.  in  difficilis  ,schwierig',  air.  do-j  du-  ds.  (lenierend  nach  dem Vorbild  von  so-,  su-),  got.  tuz-  (in  tuz-werjan  ,zweifeln'),  anord.  ags.  tor-j ahd.  2;wr-  ,un-',  slav.  in  abg-.  d^zdh  {^duz-djus  ^schlechter  Himmel'  ==)  ,Regen', russ.  dozdh,  poln.  deszcz^  aöech.  desc.  Gen.  dsce  und  analogisch  deH4.  Zu- sammenhang mit  deus-  ,ermangeln'  ist  sehr  wahrscheinlich.
Erst  ind.  aus  dus-  entwickelt  ist  düsyati  ,verdirbt,  wird  schlecht', dusta-  ,verdorben,  schlecht',  düsdyati  ,verdirbt,  versehrt'.
WP.  I  816,  E.  Fraenkel  M^  Pedersen  453.
duei-  ,fürchten'.
Av.  dvaed-ä  ,Bedrohung'j
arm.  erkntim  ,ich  fürchte',  erkiul  ,Furcht'  (Anlaut  wie  in  erku  ,zwei' '.*diLöu  Meillet  MSL.  8,  235);
16*
```


## [2026-09-05T20:09:18.117Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==150 {print}' HRN.txt | head -60",
 "description": "Horn p.128"
}
```


### [2026-09-05T20:09:19.851Z] TOOL RESULT

```
— 128 —
vergl. oss. d. dumun, t. dimin Vauchcn; wehen,
blasen (115)0.
Entlehnt kurd. dem, bei. dam (69).
57P». dum, dumb^), diimbe'^) 'Schwanz', dumhal).
aw. duma- 'Schwanz'; phlv. dutn^ dumb, dumhak,
arm. LW. dmak (= "^dumak).
kurd. düw, dunk; Sify. lam; oss. d. dumaij, t. diniag
(107); bei. (LW. ?) dunhag, n. di^/nJ, de^wfc (87), daneben
sicher echt d%m (briefl. Mitteilung von Dam es an
Geiger); sar. öihn, dümba, wsl/. diimbd (LW.).
Die arische Grundform muss ^dhumblmia- gelautet
haben (Bartholomae, Studien II, 101).
574. dendün 'Zahn*^), dendäne 'Mauerzinne'.
aw. vTmitö.lidanfa7i'; phlv. dandän (AV., Bund.);
ai. ddnta-,
kurd. didän *Zähne'; oss. t. dänddg 'Zahn* (104);
l)el. dantän, n. dafän^ d'anfän (70); minj. land, si/n.
dendäHj sar. dandän, wa/. dundäk.
Nach Joh. Schmidt' (zuletzt KZ. 32, 329) 'die
Esser.
V
571'"'' denuleii 'eilen, laufen, denän (Sahn. I, 121 Vers
1033, 198 Vers 1242).
ai. \/~dhan-^ dadhdnat 'laufen' (Hörn).
575. du^ do, dö^) zwei', duviim^ duyiim, duvem (AM.).
Käs. du, da.
ap. duoitlga- 'zweiter; aw. dva- 'zwei'; paz. dö,
kurd. du, du; afy. dva; oss. d. t. duvä (113); wa;^.
hüi, sar. däu, si/n. Jö, yaj'n. sangl. du, minj. do.
570. d'UVäxdeh 'zwölf, duvüzdehum.
aw. dvadasa, dvadasa-; phlv. duväcdahum^'); ai.
doädara, dvädard-.
»j Vielleicht auch zu np. dM *Rauch* (No. 579).
2) Auch dunh geschrieben.
') Geschrieben dunh".
*) Np. dend ist wohl nur eine repristinirte Form,
ö) So bei Firdüsi, z. B. Sahn. I, 127 Vers 1125, 189 Vers 1078
u. off.
^'j Wahrsolioinlioh ist wie in panedahum noch c zu lesen.
```


## [2026-09-05T20:09:20.541Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"duma-\" BRT.txt | head -20; echo \"=== dumb NYB\"; grep -n -i \"dumb\\|dum \" NYB_vol2_glossary.txt | head -20; echo \"=== PHD\"; grep -n -i \"dumb\\|^dum\\|každum\\|kazdum\" PHD.txt PHD_mackenzie.txt | head -20",
 "description": "Grep Bartholomae, Nyberg, MacKenzie"
}
```


### [2026-09-05T20:09:20.626Z] TOOL RESULT

```
4857:ungeniessbar,  bis.."  V.  6.31;  -ya  nasaum  '  h  ayaoho-duma-  Adj.  'mit  metallenem mJtgü>am  ap,m  a  vä  äir?m  a  va  "rf^a  ^^'«™«™>  Schwanz':  varJzaA,  .  .'dumaA<: (IS.) "  frabarsnte  "die  einen  . .  Leichnam  1  ' '  °'
5465:•  j.  araduma-  Adj, (?)—?— :  srinm  •m»m
9310:pairikanamca   'sihram    kkoyam    '>^«fÜ '■*«""""*'  °^''*'' ^t-*  =»■ Y.p.  i8;'Yl  jj.  135;    —    'pänS   X\..'4.i,\*  J-   kaurvö.duma-   Adj.    'mit   kahlem, FrW.  3.  3.  'Unbehaartem  Schwanz':   aspahe  kihrpa  .  .
13681:KompA.  —  VgL  dv<(nmatf'<).  —  Pü.:  mof.  — ■)  Für  falsch  halle  ich  Salemanns  Zu-^ammen- stellnng  von  dunita»-  mit  np.  damävand, GltPh.  /.  266;  vgl.  lu  duma-.
13684:•  j.  duma-  m,  'Schwanz':  dasinam  . .  hao- yqm  Ml  (näml,  !BnS)  patöyam    upa.kprm-
=== dumb NYB
272:a-dän [’d’n'] ignorant, foolish, of a man 415; dumb, brute, of an animal 122. — V. danistan.
273:| a-dinčh the guality of being dumb or ` brute, of an animal 11°.
292:a-göbak [’gwb’k] speechless, of dumb animals 122. — V. göbäk.
293:a-gobikeh speechlessness, of dumb ani- mals 119.
859:ayyāt-kār [---k'1] *remembrance-work"' = memorabilia, memoirs 184; memoran- dum 108%, 113% — Paz. ayädagär; NP yüdgàr; cf Ps. *by*tk*lyhy ‘recollection’, MPrs ’y’dg’ryh ‘mention’ (S).
1035:britan [PSKWN-tn'] brin-, to cut off, to chop off, to cut to pieces; to interrupt: 22%, 2417, 943. 10111; to break up a road (by marching on it) 2019; pt. brit- dumb whose tail has been cut off 248, ef burritak. — Av. (972) brày-, pres. brin-; Paz. bridan, brin- or buridan; NP bur(r)i- dan bur(r)-.
1042:burritak [bwlytk'] pt. cut off: ~-dumb 30? = brit-dumb (g. v.) — From burritan, burr-, secondary form of britan, — NP.
1075:xueseh api-š han and hir rād 4544-4; u... Wo... u -c: Mar u gazdum u apārīk-ic arafstr 76°; only -c with the last w.: andar hindükän hrom apdrik-ic damikihä 109 (apärik ‘etc.’ often asyndetically added); with negation: ké-§ ciš-ic pat pēc nēst man-ic [LY-c!] nest 1022; nē... u nē-c 1220.21. nE... U NĒ... u ne-c „2119-29. — 2. emphasizing particle: nün-ic K Bi: ‘etei, iu 'ahanün- -ic, hambun-ic, dit-ic,
1372:dumb [dwmb'] tail: brit. ~ 2418, v. brī- tan; burritak-—-& (-& in attributive po- sition) 302-3, v. burritak. — Av. (749) duma-; NP dumb, dunb. Cf. gaz-dum, gaz-dumb.
1373:Dumbävand [dwmb’wnd] Mount Dama- vand 115%, — KZSPrth 1. 24 dwnb'wntš, Gr. v. douu.ßaouvd, ibd. 1. 26 id., = Prs 1. 32 dunb"wney, Gr. v. (amd) TovuBaovv- tov; Hilers, AOi 22, 1954, 267—374; 24, 1956, 183-224.
1653:gaz-dum [gedwm] scorpion 76°. — Also spelt gzdwm, gzdm. ‘Whose tail is sting- ing’: v. the preceding w. and dumb. But NP kaj-dum, kaž-dum, gaž-dum ‘having a crooked tail’, cf the next w.
1654:gaž-dumb [g'edwmb'] a musical instru- ment, the horn 201%, — Mentioned to- gether with tumbak and nad as the mu- sical instrument of a marching army; ‘having a curved tail, or end’ from the natural shape of an animal’s horn: gāž = NP kaj, kaž ‘crooked, curved’; kaj, käc 'squint-eyed'.
1739:gung [gwng, gng] dumb 11°. 127. 652°. — = NP. gurbak [gwlbk'] cat 101. — NP gurbah.
1787:halak [hlk'] irresponsible, foolish, idiot: --mart a fool 707. — Paz. hala, Skr v. vikala ‘silly’ (Mx), halaa, Skr. v. grahila ‘mad’ (SGV); FrP 31 explained by apé- goban ‘dumb’. Av. (1789 sq.) harsdtš- ‘madness’ Vd. 22° is rendered in Phl by halak with the explanation kū dastavar ne däret ‘he has no rule of conduct’. Cf Bailey, BSOAS XXIV, 1961, 475.
2347:kurušk [kwlwšk'] ewe, of a big species of sheep 509-11, — Zsprm X, 20 in telling this story: meš kurušk i šīr-pistān "with milk in her udder’. Also kwryšk' = Paz. kurišk, koriák, BdA, p. 959-1? = BdJ2918— 303: meš 5 sratak: han i pat-dumb, han 4 a-dumb, u sak meš, u meš *takilé [tkly ; Paz. tagr, tgar] <u> kurišk tmeš, ke srub vazurg, asp homänäk, 3 köf [BdA corrected from tan, BdJ Paz. koh] dārēt api-š 6 bārak girénd, cigēn gobet ku Mānušcihr + amāh niyak kurišk-ē pat bārak dāšt [sak
3054:be fulfilled 65?! (cancel the rel. pron. <i> at the beginning of l. 21 and join the preceding clause bē kē karr aivāp gung ēnyā, 1. 20, to 1. 21: "With the exception of the deaf and dumb, the religious duties must be fulfilled by everyone’). — Ps. p’ths’dy; Paz. pidišah, NP pādšā(h), cf next w.; ef MPrth vb. pdyx$h- ‘to rule’; from pati + Av. (551 sqq.) zšay- = OP; v. Verbum 229 sq., BBB 95 sq.; Bailey, BSOAS XII, 1948, 328 sq.
3398:särenitan [s’lynytn'] to egg on, to incite, 6 to: 48°. 552%, 615. — Cf Paz. mardum yak awar dit särinom ‘I will stir up men against each other', SGV XIV, 27 (allus- sion to Isa. 19:2; misunderstood by de Menasce); BdA p. 59 hakar artik nē sārēnē ‘if thou dost not provoke war’. V. Verbum 205 and BSOAS XI, 1943, 61.
5141:duma-: dumb
6267:d'tbr: datavar dpyrwpt: dipivar dwnb?wnts: Dumbavand
6298:dwhšy: duxt dwnb'wncy: Dumbavand gdy: Gai
=== PHD
PHD.txt:177:a-ģūwāģ ["gwb*k!] speechless, dumb.
PHD.txt:380:gawazn [gw’sn' | N ~] deer. gawdar [0011 | N ~] calf. ģāw-dumb [g'bdwmb | N —dum] horn, trumpet. ģāw-mēš [TWR Amyš | N gā(w)mēš] buffalo. £áy-, v. ģādan. Gayómart [g”ywkmlt! = Av. gayó marata | (M gyhmwrd), N ~] the First Man. gaz [gc | N ~] tamarisk. gaz-, —išn, v. gazidan. gazag [gc’k'] biting. ģāzar [g'cl | N gázur] fuller, washerman. £azdum [gcdwm | N každum!] scorpion; astr. Scorpio. £azidag [ezytk! | N gazid] poll-tax. gazidan, gaz- [gc-, gz-ytn! | N ~] bite, sting. ~išn: biting. gëg [gdk' | M gyyg] thief. gēhān [gy)?>n! | = M, N gihān, jahān] world. ~ig [-yk'] worldly, mortal. -ģēn [-k(y)n! | M -gyn, N -gin] suffix forming adjectives of quality. gês [гуз | (M gyswg, N gēsū)] curls, locks. £étig [gytyk, gytydy | M gytyg, N géti] 1. the material world; 2. worldly. ~ig [-yk'] worldly. gil [ТУМА < A tym; gl | N ~] clay. gilag [g(y)lk! | N gila] complaint, lamentation. —-Obàr [wp] swallowing complaint, suffering in silence. ģilēn [T YN Ayn! | N gilin] (made of) clay. gilistag [g/ystk!] home, dwelling of demons. gir-, ~iSnig, v. griftan. gird [git! | M gyrd, N ~] round, circular; gathered. (9) — āmadan: gather, collect (intr.). — kardan: gather, collect (tr.). ~ih: roundness. girdag [gitk' | N ~a] disk, round. gisnag [gink' | P gyfng] short, small. ģišnīz [ginyc | N —] coriander. giyā(h) [gy^h, gy^h | (M gy'w), N ~] grass. ~izag [-yck'] a straw, blade of grass. gizistag [gcystk' | J w/Bzsth] accursed, hateful. gogird [оо | M gwgyrd, N ~] sulphur. ~ӧтапа [-’wmnd] sulphurous. gohr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage. goóhrag [gwhlk'] = göhr. ~-danag [-d^m k!] physicist. 1g6hrig [gwhlyk'] natural, essential. *ģūhrīg [gw(’)hlyk'] equivalent, substitute, indemnity,
PHD.txt:382:*g5k4n [gwk’n'] details. Lc um ~ig [-yk'] detailed; precisely. (sassa tu) ģūmēz [gwmyc | N giméz] bull's urine (as ritual purifier). ģgūmēz- [gwmyc- | N giméz-] urinate. gön [gwa' | N gün] colour, complexion. ~ag [-k' | M geng, N güna] = gön ; sort, kind, form. gor [gwl | N ~] onager, wild ass. göspand [K YNA < А апу ? ; gwspnd | N ~] (small) cattle, sheep. ~-tihrag [-cyhlk'] holding the seed of cattle. ģūstān [gwst^n!] cattle-stall, cowshed. 1858 [gws | = M, N ~J ear. *GÓ68 [guš | N ~] cal. 14th day. tūšag [gwsk' | N ~a] corner. ģēošūsrūd [rwi^wslwt! = Av. gaošū.srūta-| acquired, learnt. 5051 [BSLYA < A bsr’; рой! | N ~] meat, flesh. ģūšwār [gwštw] | N ~] ear-ring. ģūw-, ~išn, v. ģuftan. gowag [swb k! | М gw'g, N goya] speaking, eloquent; speaker. *ģoūwizār [gwwc'[] explicit, in detail. göy [gwd | N ~] ball. göz [gwc | N ~] walnut. ~énag [gwzynk! | N gózina) a walnut sweetmeat. Gözihr [gwcyhl | Ar. jawzahr] astr. the Dragon. ~ dumb: the descending node of the moon. ~ sar: the ascending node of the moon. grab [22р | P grb] womb. grāmag [gľmk! | P gr’mg] possessions, wealth. grāmig [gľmyk! | M grmyg, N girāmī] treasured, dear. ~ih: affection, respect. 1$raw [giwb! | P grww] cane. *ģraw [glwb' | N giraw] pledge, security. ~ih, ~(a)g4n [glwk’n' | M grug*n, N giraugān] = *graw. grayidan, gray- [gl?d-yin' | P gry-, N gtráy-] lean, incline; intend, desire. ģriftan, gir- [OHDWN-tn' < A V?hd; glptn!, gyl- | M grypt, gyr-, N giriftan, ~] take, hold, restrain. «išnīģ : tangible. griftār [gipt?l | N gir~] held, taken; captive. ~Omand [-'wmnd) tangible. grih [glyh | N girth] knot. lgriw [CWLE < A swr-h; glyw'] neck, throat. ?0riw [CWLE, glyw' | M gryw] self, soul. sgriw [glyw! | P gryw, N girī(b)] a grain measure, modius, peck. griwag [glywk!' | N giriwa] hill, ridge. ģrīwbān [g/ywp?n! | N girībān] neck-guard, gorget. griyistan, griy- [BK YWN-stn'< A У bky; gld-stn! | M gryy-stn, N giristan, giry-] weep, cry.
PHD.txt:384:ёгбһ [glwh | N guroh] group, crowd. gubrág [gwpl’k'] awake, alert, vigilant. ģubrās- [gwp/”s-] = wigras-, v. wigrádan. ģuftan, $0(w)- [YMRRWN-, YMLLWN-tn! < A ymlwn, V тЇ; gwptn', gwb- | M gwptn, gw-, N ~, gā(y)-] say, speak. ~išn: speech. ģuftār [gwpt?] | N ~] speaker. ~ih: (power of) speech. gugiin- [gwk’n- | M gwg^n-] destroy. gugar(i)dan, gugar- [gwk”/-(y)tn! | N guwár-idan] digest. tuģāy [gwk*dy | M gwg'y, N guwah] witness. ~ih: testimony. ģūh [gwh | N —] dung, excrement. guhrayénidan, guhrayén- [gw AP yn-ytn!] waken, arouse. gul [gwl | N ~] flower, rose. ботап [gwnmn! | = M, N ~] doubt. ~par [-A/] casting doubt. ~ig [-yk'] doubtful. ~ih, ~igih: doubt. gumardag [gwmltk'] appointee, deputy. ģumārdan, gumār- [gwm’l-tn' | М gwm'r-dn, N gumāštan, gumar-] appoint, commission, entrust. gumbad [gwmbt' | N ~] dome, fire-temple. £umég [gwmyk! | M gwmyg] mixture. guméxtan, gumēz- [gx”myhtn!, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; = gumézagih. gumëzag [gwmyck'] mixture. ~th: the Mixture, (the duration of) this material world. Jgund [gwnd | = P] army, troop; group, gathering. *gund [gwnd | N ~] testicle. gung [g(w)ng | N ~] dumb. ģurbaģ [gwibk! | N ~a] cat. Бита [gwlt! | P gwrd, N ~] hero. lih: heroism, bravery. gurdag [gwltk! | N ~a] kidney. *gurdih [ewityh] (some piece of) armour. gurdwār [gwltw’!] befitting a hero. ёпгр [gwlg | N ~] wolf. gurganig [gw/g”nyk! | N ~i] of (the province) Gurgan. gursag [ewlsk] | N gurusna !] hungry. «ЛЬ: hunger. Suën [gvfn! | N ~] male. gusnag [gwšnk! | J gušna] hungry. Gušnasp [gwšn(*)sf] the second major Fire of Sasanian Eran, that of warriors. £yà$ [gyw'k! | M gy'g, N jay] place.
PHD.txt:1706:dumb agowag, gung.
PHD.txt:2312:horn srū; (trumpet) gāwdumb.
PHD.txt:2928:node of the moon Gēzihr-dumb / -sar.
PHD.txt:4080:trumpet gawdumb.
PHD.txt:5427:jumbihistan jumbén- jumbénidan jumbidan dumb
PHD.txt:5444:gurgānīg gursagih gursag durgar jorda jorda 1-2gurdih gurd gurdwar gurdag dum, 1021 joma jomā gumānīh gumānīgīh gumānīg gumān gumāngar gumār- gumārdan gumārdag jumb- dumbēmand jumbāgīh jumbīh-
PHD.txt:5554:rasián! rasidan! gāhānbār gāhānīg gāhān -īhistan vāzdah gāwdumb gazar dahišn, dāšn Чах$арбтапа daxzag
PHD_mackenzie.txt:917:   'l" ).9~    a-gOwig [)gwb)k ] speechless, dumb.
PHD_mackenzie.txt:2490:gaw-dumb [g'fidwmb 1 N ......dum] horn, trumpet.
PHD_mackenzie.txt:2499:gazdum [gcdwm I N kazdum!] scorpion; astr. Scorpio.
PHD_mackenzie.txt:2563:  - dumb: the descending node of the moon.
PHD_mackenzie.txt:2619:gung [g(w)ng IN......,] dumb.
PHD_mackenzie.txt:6448:district awestam, kust(ag), paygos,     dumb agowag, gung.
PHD_mackenzie.txt:6782:hen kark.                                      horn sru; (trumpet) gawdumb.
PHD_mackenzie.txt:7171:node of the moon Gozihr-dumb j·sar.    on abar, pad.
PHD_mackenzie.txt:7814:totality hamagih.                        trumpet gawdumb.
```


## [2026-09-05T20:09:34.598Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==336||NR==342 {print \"\\n========= leaf \" NR \"\\n\" $0}' BQT_v2_pages.txt | head -150",
 "description": "BQT pages 876 and 882"
}
```


## [2026-09-05T20:09:36.729Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && grep -l \"MON:15\\|MON_part\" page-1*.json | head; echo ---; python3 -c \"\nimport json,glob\nfor f in ['page-127.json','page-125.json','page-124.json']:\n    d=json.load(open(f))\n    s=json.dumps(d,ensure_ascii=False)\n    import re\n    for m in re.finditer(r'MON_part\\d[^\\\"]{0,160}',s):\n        print(f, m.group(0)[:200])\n\" | head -20",
 "description": "Find how MON was located previously"
}
```


### [2026-09-05T20:09:36.823Z] TOOL RESULT

```
========= leaf 336
     ‫دله‬                                                                                     ‫یس‬


‫آب بندلدت و زوین رالیز گویند > وآن نیزه‌ای‬          ‫دل گر م کر دن ه کنابه ازعاشق‌شدن‬
‫باشد کوتاه که سنینآن دوپره نیزمیباشد ویجالب‬                                                    ‫باشد ‪.‬‬
‫خصم اندازند ‪ -‬وغلاف خوشه خرما را و آنجه‬             ‫دکلعبه کردن ‪ -‬کنابه از توجه‬
‫خوشة خرمایرآن باشف هم گفته‌انس ودست افزار‬
                                                                                ‫کردن بدل باشد ‪.‬‬
 ‫چاهکنانرا دیزگوبند و آنرا میتین خوانند ‪-‬‬           ‫بم اول و انی و سکون میم ‪:‬‬            ‫دلم‬
‫و بمعنیآونگه هم هت که آوشته و آونگان‬
     ‫آزمدہ است ‪.‬‬
               ‫باشد ؛ وباین معنی یکر اول ی‬
                                                    ‫جوششی باشد بخاارش » آونرا بعربی شری‬
                                                                                             ‫گویند ‪.‬‬
 ‫دلنگان ‪ = ۴‬بروزن زمتان » بمعنی‬                     ‫دلماك ‪ ۱‬ح بنتم اول و انی و الك‬
           ‫زآان وآویخته باشد ‪.‬‬
                             ‫آونگان اوستیکه‬         ‫وسکون‌کاف‪ ,‬دلمه راگوین دکه‌پنیر ترباشد ءوآن‬
     ‫دل نکمنواب‪۵‬ه‌ازمردمیو مهربای‬                   ‫شیریست که بعد از مایه زدن بسته شود ‪ -‬وضم‬
                                    ‫لمودن‌باشد ‪.‬‬    ‫اول و سکون انی جانورست شبیه بشکبوت ‏‬
 ‫‪,‬‬         ‫درد‬
             ‫شیغی‬
                ‫مثان‬
                   ‫اول و‬      ‫ت»ح‬
                                ‫ب‪۵‬ف*‬
                                   ‫‪4‬‬                ‫وحربی رتیل‬    ‫نےد‬
                                                                    ‫کا ک‬
                                                                       ‫گوند زهراوآدمی را حل‬
                                                                                             ‫خوانند ‪.‬‬
 ‫جالوری باشد که آنرا قاقم گوبند ‪ -‬وكربة‬
‫اند ‪ .‬وممرب آن دلق‬            ‫صحرایی رگافهمته‬       ‫دهل ‪ -‬بروزن بلیل‪ ,‬غله‌ای راگویند‬
                                                                                   ‫ل‬
                           ‫دلاله‬   ‫زن‬
                                    ‫و‬   ‫‪-‬‬   ‫است‬      ‫که هنوزخوب نرسیده باشد عموماً ‪ -‬ونخودخام‬
                           ‫ومحتاله وجامهیشمینه‬      ‫اف باشد ‪ -‬و هرغل ناری که آنرا‬      ‫کغهلدر‬
                           ‫وخرفه ومرفع‌درویشان‬                               ‫يوان کننف خضوضا ‪-‬‬
                           ‫را فيز گوند که از‬        ‫‪۵‬ه ‪ ۲‬سیختح‌اول وثانی وثالك » شهری‬
                                                                                    ‫ل‬
              ‫دله‬           ‫آن پشمپیا آوخته‬         ‫که سدازمابه زدن بسته شود وضم‌اول وسکون‬
‫باشد ‪ -‬وبا ثانی مشدد » بمعنیمکر وحیله وعلر‬          ‫ثانی‌جادوریاست زهردارشبیه بعنکبوت که جربی‬
‫وردباد رائیز گوبند‬
                 ‫وداراست ومنافق باشدا ‪ -‬گ‬                                     ‫رتلا خوانند ‪. ۴‬‬
‫‪ -‬وبکر اول بمعتی دل است کهبعربی قلب‬
                                     ‫خوانند ‪. 4۵‬‬    ‫نندی‌باشد که ازچوبوعلف‌وخا که وگل دریشس‬


                                                                       ‫(‪ )۷‬چك‪ :‬کردن ‪۰‬‬
      ‫ب)یز‬      ‫ب(اد‬
                   ‫آاك‬
                     ‫ندرار‬
                         ‫طم‪.‬ا)‪.‬‬
                              ‫سمكل( «‬
                                    ‫‪ = ۴‬دل‬                       ‫( ‪۰‬‬   ‫دلمه ( ھ‪.‬م‪.‬‬   ‫=‬   ‫‪۱‬‬

     ‫‪ - ۴‬نیز دلمه بضم اول ‪,‬طعامی است از ر گے رز وبا‬           ‫(شربته) «مکی‌نژاد» ‪.‬‬             ‫‪8‬‬
      ‫کزوشت قیمه کرده آکنده باشند ‪-‬‬
                                  ‫کلمبرگے و با بادنجان و خیار و جز آن که داخل آنها را ا‬
      ‫نیز کیسه های پولی که درجشن عروسی وباجشن نوروز بمهمانان و مدعوان دهند ‪« .‬ناظم الاطبا» ‪۰‬‬
                                                           ‫ابن رسم در گیلان حنوز معمول است ‪.‬‬
     ‫‏‪٩‬طبری فیز‬                ‫‪ - ۴‬در اراك (سلطان آباد) نیز ‪« 0280616‬مکی نژاد» ‪.‬‬
     ‫‪ - ۱‬نيز در تهران و اراك ( سلطان آباد ) « مکی‬          ‫‪) dala‬راسوس( * باص ‪‎‬یربط ‪. ۰۳۵۵‬‬
     ‫(يان آهرچیز ])‬
                  ‫‪-۲‬طری ‪ 2164‬م‬                        ‫»داژن ینعمب روخرپ و ومکش لامعتسا ‪‎‬دننک ‪.‬‬
                                                                           ‫باس ‪‎‬یربط ‪: > ۳۵۹‬‬
              ‫ملکت چو فران‪ .‬اوچومعانی قراست ‪.‬‬           ‫خرو تنهة ملك بود‪ .‬او دلهٌ ملك‬
     ‫«منوچهری دامفالی ‪٩٩‬‏ ‪.‬‬


========= leaf 342
                                                                                        ‫رو‬‫‪-‬‬

 ‫نرم وآهته رگاویند ‪ -‬ونام یکی از خو‪.‬شان‬                              ‫باشد که یمن نده ومن ‪3‬ه ‪.‬‬

 ‫افراسیاب است که در کشتن سیاوخش سعی بیار‬          ‫دمندان = بروزن قلمدان » بمعنی‬
‫کرد ‪ -‬وضم اول درعربی بی رخصت بخانة کسی‬             ‫دوزخ باشد‪ -‬وآ نش رائیز گوبند‪ -‬ونام شهرست‬
                              ‫رفتن باشد ‪. ۷‬‬       ‫از توابع کرمان ک‪.‬ویند نزديك بکانوهی است‬
 ‫ده ‪4‬‏ بنتح اول وئالی "آ نش افروزاست»‬
                                                 ‫که معدن طلا ونقره آوهن و تونیا است وغاری‬
‫ون ظفریباشد بهیأت کهآ دمی وآپ درآن کنند‬
                                      ‫آ‬
                                                ‫دارد که وسته صدای آب بگوش‌میر‪-‬دوبخاری از آن‬
 ‫ودر کنار اند کث آش لهند ‪١‬‏ از سوراخهای بیثی‬      ‫غاربرهی |بدوباطراف آن متکا تف یر ددونوشادر‬
 ‫آن بخاری برآتس وزد و آتش افروخته گردد ‪.‬‬                                            ‫می‌شود ‪. ۷‬‬
 ‫کویند از مخترعات جالبنوس است ‪ -‬وبه‌عنی دم‬       ‫دهنك ‪ - ۵‬بروزن رونده » فریاد کننده‬
 ‫آهنگران هم هست ‪ -‬و سرما وباد و برف درهم‬                                        ‫راگوند ‪.‬‬
                      ‫آءيخته رالیز گویند ‪. ۸‬‬
  ‫زت‌هز‪)۲(,‬‬
          ‫پءابلف‬
               ‫وربا‬
                  ‫د‌د‬
                    ‫نوژن‬
                       ‫دمیا ِ = بر‬                ‫‪۵‬منهه ‪ » ۴‬بنتح اول سوکون‌انی ونون‬
                                                 ‫انوار‬   ‫مفتوح (‪ ۱6۰‬نام شغالی است که دکراب‬
            ‫خون رگوایند وعربی دم خوانند ‪.‬‬
                                                 ‫سه‪.‬لی‪ ۴‬احوال اومذ کوراست‪ -‬وموراخی را نیز‬
 ‫دمیاط*‪ = ۱‬بفتح اول بروزن وطواط‪.‬‬                 ‫کویند که برای دکمشی و باد آمدن به تنور‬
           ‫لام ولایتی است ما بین مصر وعدن ‪.‬‬     ‫کرین ستوران کروابند که‬  ‫بگذارند ‪ -‬وبعرمی س‬
 ‫دمیدن « بروزن خمیدن ؛ بمعنی لاف‬                 ‫جمع کرده باشند ‪ - ۵‬و بکر اول به‌عنی رویاه‬
 ‫زدن وخودرا پربادکردن ‪ -‬و حملهآوردن باشد‬          ‫ونابه ازمردم عار‬
                                                                 ‫وشغال هردو آمده است ‪ - ۴‬ک‬
‫و برمعونیییدن و رسن لبات هم هت ‪ -‬و دم‬                                ‫ومحیل وفتان باشد ‪٩‬‏ ‪۰‬‬
‫خوردن ‪ -‬و فکسشیدن ‪ -‬وطلوع صبحرا لیز‬               ‫دمنه دالی = بدااز ابجد بر وزن‬
                                    ‫کوبند ‪.‬‬       ‫پهلوانی ‪ ۰‬لته کوهنۀ وچ ده را کوبند که در‬
‫دميلث س بکر انیو سکون تحتانی‬                         ‫موراخ تنور کنند تا بخار تذور بیرون نرود ‪.‬‬
 ‫بر وزن شريك ؛ به‌منی زمین و بوم باشد ‪٩۷-‬‏‬       ‫نیم دور ‌ بکرثانی» کنایه از‬         ‫دم‬
 ‫وبسکون‌الی وفتح تحتالی» نام قریه‌است ازقرای‬
‫غزنین ‪ .‬کوبند شهاب‌الدین غوری بزخم یکی از‬
                                                                              ‫آه درد فا باشف ‪۰‬‬


                   ‫ملاحده درا نجا شپید شد ‪.‬‬      ‫آواز‬    ‫دمو ر = بفتح اول مروزن سور‬

                                 ‫(‪ )۲‬چك‪ :‬زند ویاژند ‪.‬‬               ‫)‪ ۱‬چش ‪ :‬م‬
                                                              ‫‪-‬فتوح ‪.‬‬
 ‫‏‪ - ٩‬دمندان بفتح اول و کر دوم ‪ .‬شهری بز رکٹ و وسیم بکرمان و در آن کان‬
  ‫آهن و مس و سیم وژر ونوشادر و توتیا بیار است و معدن آن بکوهی است بنام « دنباوند *ه‬
  ‫غارست‌بز رکه‬    ‫کابونه‬
                       ‫و ارتفاع آن سه فرسنك است‌وبهفت فرمنکی شهر «چواشبر» است » و در‬
  ‫و تاربك که از درون آن آوای آب بگوش رد و بخاری دود مانند برآید و بحوالی بچید ‪.‬‬
   ‫]ارابکنند‪».‬‬
             ‫وچون متکانف گردد وزیاده شود مردم شهر وحوالی بدانجا شوند ودرهرماه با دوماه نپ‬
                      ‫‪ - ۳‬اسم فاعل از «دمیدن» ‪.‬‬           ‫« معجم البلدان پنقل از ابن الفقید» ‪.‬‬
   ‫ورتك‬
      ‫‪ - ۴‬درسان کرت ‪ 261۵82012321‬نام شفالی در پنچتنترا « وبلیاه‌ز ‪٩۹4‬‏ ‪ ۳:‬ك‬
              ‫(کلیله) نیز نام شفالی دیکر بود » واسم کلیله ودمته ازنام ابن دوشفال مأخوذ است ‪.‬‬
   ‫‪۲۸۸‬‬    ‫حه‬
           ‫صهفدر‬
               ‫بق‬
```


### [2026-09-05T20:09:38.447Z] TOOL RESULT

```
page-107.json
page-106.json
page-100.json
page-101.json
page-102.json
page-109.json
page-105.json
page-118.json
page-108.json
page-110.json
---
page-127.json MON_part1.txt line 63307: «دنیدن: [dan(īdan)] (مصدر لازم) دویدن به نشاط و خوشحالی» — Nourai's gloss verbatim.
page-127.json MON_part1.txt line 63307
page-125.json MON_part1/part2) omits all three — so the exact pages are unverified; the substance is confirmed.
page-125.json MON_part1.txt lines 59965-59975): \
page-125.json MON_part1.txt lines 58764 and 59965-59975 (Adena 2-vol. abridgement) s.v. دادا، دده
page-124.json MON_part1/2.txt) and the online copies (vajehyab, abadis) reproduce the entry text without page numbers, so p.813 cannot be located. The substance is confirmed from Dehk
```


## [2026-09-05T20:09:53.139Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"دنبه\" \"دنبل\" \"دنباله\" \"دنب\" \"دماوند\" \"دنبك\" \"تنبك\"; do echo \"=== $w\"; grep -n \"$w\" BQT_v2_pages.txt | head -6; done",
 "description": "Grep BQT v2 for donb words"
}
```


### [2026-09-05T20:09:54.925Z] TOOL RESULT

```
=== دنبه
7020:‫جنیه(‪ْ ۹ * )۱‬م اول بروزن دنبه» هر‬                     ‫و قویکدر‪-‬فتار‬      ‫وبمعتی‌حلقه همآمده‌است ‪8‬‬
20263:                 ‫این لضت دنبه بره بوده ا‬                                ‫ابجد‪ .‬بمعنی دامست که درمقابل‌سرباشد وبعربی‬
20309: ‫دنبه نهادن ‪ -‬کنابه ازفرب وبازی‬                                ‫سازند وبازیگران در زیربغل گرفته نواز ن ‪.‬د‬
38206:                                                            ‫دنبه » بمعنی‬        ‫سنب = بتم اول بورزن‬
=== دنبل
=== دنباله
19930:                              ‫ودنباله رگاونشد ‪. ۷‬‬         ‫جرمی‌شم خوانند‪ -‬وبمعنی وزن شمرباشد‪ -‬وانبانی‬
20093:                                                                   ‫هشیار" معروف است‪ - ۵‬ودنباله کش لشکررالیز‬
=== دنب
7020:‫جنیه(‪ْ ۹ * )۱‬م اول بروزن دنبه» هر‬                     ‫و قویکدر‪-‬فتار‬      ‫وبمعتی‌حلقه همآمده‌است ‪8‬‬
8434:           ‫دنبوک ے‪-‬و ‪۰‬هبانک ‪۰‬زا‬
9699:                                                     ‫=نابه ازدنباوعالم‬
9950:            ‫دنبالببرخابی » چنگال‌شیر خاری‪.‬‬                      ‫‪ - ۴‬بامن‌همی چشی‌تو وآکه ییکهخیره‬
15558:‫پنبه بافته باشند ‪ -‬و رندش زوده و شکنبه را‬                     ‫وفتح ثالث وفای بواورسده و ‪,‬جم زده ‪,‬دنبددانه‬
16478:‫داه جیدن‪ -‬بچمعینیدنبر‌دانه امت‬                       ‫دانگا ند = باکاف فارسی بروزن‌بازخانه‪.‬‬
=== دماوند
20018:    ‫® ‪ -‬دماوند که درمآخف اسلامی «دتباوند »مده بتابتحقرق مرحوم کروی ( مجلةٌابنده‬
20022:     ‫( ازمسدر وندن = نهادن ) و«افع شدن » وهاستادن» » پس دماوند بعنی شهریا آبادی با قلعة‬
20025:    ‫که ترديك بوده « نپاوند * وآن دیگررا «دماوند» نامیده‌اند‪ .‬کروی فکر کرده که شاهراهی از‬
20029:              ‫ونادلدورسراین‌شاهراهپا نهاده‌است‪ .‬کروی در یاءان نگاشته‪« :‬شایدنهاو ندودماوند ثکزونهام‬
20030:    ‫تامها راکاروایان عرب داده ‪ ۲‬قله لزدسکتر را نهاوند وآن یکی را دماوندکفته اند ‪٩‬‏ پیداست که‬
20032:        ‫وعربتان رفت وآمد میکردند بجه دلیل عربستان را ماخ گرفتند ویکی راه دماوند» ودیگریرا‬
=== دنبك
=== تنبك
```


## [2026-09-05T20:10:00.661Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport sys\ntxt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nff=0\ntargets={19930:0,20018:0,20093:0,20263:0,20309:0,20022:0,8434:0}\nfor i,l in enumerate(txt,1):\n    ff+=l.count('\\f')\n    if i in targets: targets[i]=ff\nfor k in sorted(targets): print('line',k,'-> formfeeds before:',targets[k], 'printed page approx', targets[k]+540)\n\"",
 "description": "Map BQT lines to leaves"
}
```


### [2026-09-05T20:10:02.448Z] TOOL RESULT

```
line 8434 -> formfeeds before: 145 printed page approx 685
line 19930 -> formfeeds before: 336 printed page approx 876
line 20018 -> formfeeds before: 338 printed page approx 878
line 20022 -> formfeeds before: 338 printed page approx 878
line 20093 -> formfeeds before: 339 printed page approx 879
line 20263 -> formfeeds before: 342 printed page approx 882
line 20309 -> formfeeds before: 343 printed page approx 883
```


## [2026-09-05T20:10:08.521Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19900,19960p' BQT_v2_pages.txt",
 "description": "BQT p876 dom entry"
}
```


### [2026-09-05T20:10:08.573Z] TOOL RESULT

```
     ‫«منوچهری دامفالی ‪٩٩‬‏ ‪.‬‬
   ‫پوس‬                                                                                                         ‫دلهرا‬

 ‫دليك = بفتح اول بروزن‌شريكث ‪ ,‬موه‬                        ‫دلهر | ‪ = ۱‬بکراول وهای هوز(‪)۱‬بر‬
 ‫وئمرکلی است ‪ . ۴‬وآن‌مانندتخمسه كلسەرىگڭ‬                      ‫وزن افترا‪ .‬لباامدشاهی وده آزیادشاهان‌هندوستان؛‬
‫میباشد؛ و بعضی گویند خم کل است کهبعربی‬                                       ‫وبقتح الك یزبنظرآمده امت ‪3‬‬
                                  ‫بذرالورد خواناد ‪.‬‬
                                                          ‫دلی « بکرارل وثالی بتحتان یکشید‪..‬‬
 ‫دینس = بفتح‌اول وثانیبتحتالیریده‬
                                ‫ل‬
                                                          ‫مخفف دهلی باشد وآن شهری است «شهور در‬
 ‫ولون مک‌وربین بی‌نقطهُ زده ‪ ۰‬بیونانی‪ ۴‬لوعی‬                 ‫حندوستان ‪ ۴‬؛ وبا تشدید ثانی کهفمته‌اند ‪۰‬‬
‫از صدف کوچك باشد و آنرا نا خام امت نمك‬
 ‫دلیده = بفتح'ول بروزن رسیده " خرد | سودکرده میخورند و چرن پخته شد نمیتوان‬
                                             ‫خوردن ‪.‬‬                            ‫وبلغور شدن غله راگویند ‪# .‬‬

                                                 ‫بیان هفد هم‬




‫ران بدان آ ش افروزند ‪ -‬و آه را هم‬
                                ‫کر‬‫که ز‬                    ‫» دم ولفی‬       ‫‏‪ a‬بشتح اول وسکون‌الی‬        ‫دم‬

‫وانند ‪ -‬ودهان آدمی‬
                 ‫کون ‪ -‬وافوی را لخیر‬
‫و زءان را هم گفته‌اند‪-‬‬      ‫وغیر آدمی باشد‪ -‬ووقت‬
                                                              ‫باشد © ‪ -‬وفریب وخدعه رانیز گویند ‪ -‬وبمعنی‬
           ‫‪۱‬‬     ‫‪٩‬‏‬             ‫‪۱‬‬   ‫‪۲‬‬                    ‫وبوی را یزگفته‌اند که‬           ‫‪-‬‬   ‫نخوت وتکبرهم‌هت‬
 ‫و درعربی بمه‌نی خون امت ‪٩‬‏‪ -‬وم اول دنب‬
                              ‫ودنباله رگاونشد ‪. ۷‬‬         ‫جرمی‌شم خوانند‪ -‬وبمعنی وزن شمرباشد‪ -‬وانبانی‬

                                                 ‫‪ :‬سی زده ‪.‬‬     ‫(‪ )۳‬چك‬               ‫(‪ )۱‬چك ‪ :‬وها ‪.‬‬

  ‫باستخت‌هندوتان ‪ .‬رك‪ :‬دهلی‪.‬‬              ‫‪ieD _ ۴‬‏‬             ‫رك‪ :‬بلهرا (صس‪ ۳۰۳‬ح ) )‪. (¢‬‬         ‫‏‪٩‬‬
   ‫‏‪) fruit de la rose =۴‬رف( كل ‪ ۲‬ص ‪ ۹۲.‬كلد ( رکب روا =) نرتد س‬
   ‫‪ - ۴‬بونانی ‪« 8811۱61‬ادتدکای» = ‪( 6811161‬فر) «لك‪۲‬‬                                  ‫‪ « 25‬ئاس ‪. ۲۸۱۰‬‬
  ‫‪mahd‬‏ ‪( 1010۳80 .‬نفس كردن > دعیدن)؛‬     ‫‪ - ۵‬هندی باستالی » ره‬   ‫ص‪٩۲‬‏ ‪.‬‬
  ‫ردن » وزیدن ؛ دمیان ) » کردی ع‬
                               ‫پپاوی ‪mad‬‏ ‪,‬فس ‪ :‬استی ‪nimid , 8۱۱۳‬‏ ( دکرد‬
  ‫‪۰,‬آرامی‬   ‫‪mad‬‏‬    ‫از مر ی‬       ‫(عر) ا‬      ‫‪ ۹‬ك‬                  ‫‪.‬‬   ‫“‪Yo‬‏‬    ‫سدق‬     ‫‪mad‬‏‬   ‫بلوچی‬    ‫‪۰‬‬   ‫‏‪den‬‬


  ‫‪ - ۷‬اوتا ‪( 31 -‬ذب) ‪.‬هلوی‬       ‫‪ 3‬آشوری بابلی ‪* 1721‬ولفنون ‪. ۹۸۲‬‬
  ‫‏‪dumb‬د‪.‬ی ‪ 00‬و ‪knud‬‏ افغانی ‪ 0121‬اى ‪ 83۳0‬و ‪" 830110‬باوچی‬‫‏‪ dun‬ر کر‬
  ‫‏‪ dunbag‬ر ‏‪ . dunb , dumb‬سریکلی نان ‪êmid .‬‏ ‪ .‬رخی ‪ 4090‬نا ‪ .‬مکل‬
    ‫آریابی آن ہایتی ۔ ‪ ۵ 3۲۵۳۷0‬باشد ”اق ‪ ۳۷۵‬ورك‪ :‬هوشمان ابسا؛ کیلکی ‪0‬ل‬

            ‫‪.‬‬   ‫‪.‬‬   ‫‪۶‬‬   ‫ص‬     ‫‪۳‬‬   ‫ك‬   ‫‪9‬‬   ‫‪mod‬‏‬    ‫شھمہرزادی‬    ‫و‬   ‫‪ 4‬لاسگردی‬    ‫هی‬     ‫»سر‬   ‫‪ ۰‬منگری‬       ‫‏‪dum‬‬


   ‫کالسکه برای حمل‬          ‫و انگلسی «‪ecnegilid‬‏‬         ‫او[ » از فرانوی‬        ‫© ولیجای ‪ -‬تک‬              ‫‪۱‬‬
                                                                                                ‫و يقل مافر ‪.‬‬
   ‫مشه درصفحه ‪yvA‬‏‬
  ‫دمان‬                                                                                                   ‫ت‬
                                                                                                         ‫ب‪۷‬‬

‫حیوالی که باشد و بهترین آن ازپرندکان مغز‬                   ‫دما = بفتح اول بروزن هوا » بمعثی دم‬
 ‫كربك وتیهوست وازچرند گان بره و کوساله‪,‬‬
                                      ‫س‬                    ‫ونفس باشدا ‪ -‬وبکراول بمعنی رودخانه است‬
 ‫وجمیم مفزها سرد و تر است» و مغز سرخروی‬                    ‫بلغت زند وپازند (‪ - ۱0۴‬ویمعتی مزاج وطبیعت‬
```


## [2026-09-05T20:10:09.381Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20250,20330p' BQT_v2_pages.txt",
 "description": "BQT p882-883 donbe entry"
}
```


### [2026-09-05T20:10:09.450Z] TOOL RESULT

```
                          ‫خنداخند ک‬                                     ‫وامربتشاط رفتن هم هت ‪ -‬وبعربی خم‌سر که‬
                                                      ‫دماوند ‪.‬‬                    ‫وشراب وروغن وامثال آنراگونند؟ ‪۴ .‬‬
‫از‬         ‫شبره‪١‬‏نرامست‬
                      ‫ك لیر = بروزن قن‬                                  ‫دفان ‪ » ۴‬بروزن زنان ‪ .‬بمی رفتن‬
 ‫هندوستان_ ونام گریوه‌ای هم‌هست در رکاشهمیر‬                            ‫براه‬    ‫مان‬
                                                                                 ‫او‬‫راط‬
                                                                                     ‫خبتش‬
                                                                                        ‫بنشاط و خرامان باشد» و‬
                                  ‫هیراشتهار دارد ‪.‬‬
                                                 ‫که بم‬                  ‫رونده ‪ -‬و از خشم و قر بجوش آبنده را نز‬
‫ك ذبره = براای بی‌نقطه (‪ )۲‬بر وزن‬                                                                                        ‫گویثد ‪.‬‬
‫زنکله » طنبورباشد وآن سازبت مشهور» واصل‬                                  ‫دلب * = جنم اول وسکون ثابنیاوی‬
‫اهبهت تمامی‬  ‫شچ‬‫مست‬
                 ‫این لضت دنبه بره بوده ا‬                                ‫ابجد‪ .‬بمعنی دامست که درمقابل‌سرباشد وبعربی‬
 ‫مدئبة بره داردویکثرت استممال دلمره شده است‬                                                                        ‫ذب خوانند ‪.‬‬
                           ‫است ‪. ۸‬‬          ‫نببآونره‬
                                                   ‫طمر‬
                                                     ‫وم‬                 ‫دفبال ‪ -‬بفتح اول بر وزن چنگال ‪.‬‬
                                                             ‫با را ‌‬   ‫چك‪:‬‬    ‫)‪۲‬‬           ‫‪۰‬‬       ‫)‪ (۱‬جك‪ :‬هزدهم‬

                                                                                               ‫ِ‬   ‫رك ‪:‬دیدن‬         ‫‪۱‬‬
     ‫‪۰‬‬    ‫دامقانی ‪۰٩‬‏‬     ‫«منوچهری‬
                                            ‫همه ماهه بگرد دن همی دن ‪.‬‬                  ‫همه ساله پدلبر دل همی ده‬              ‫‪۴‬‬
         ‫‪ ۰‬بردن»‬       ‫( چنانکه ‪:‬آوردن‬           ‫—‬   ‫در افعال فارسی (بهلوی ‪nat‬‏‬        ‫مصدری‬        ‫لمر ولد‬    ‫‪-‬‬    ‫‪۴‬‬

               ‫رك‪ :‬دم (ضم‌اول)‪۰ ‎‬‬       ‫‪۳‬‬    ‫‪e‬‬            ‫ی _ اسم فاعل از «دنیدن» (ه‪.‬م‪. ).‬‬                         ‫خور ‪ -‬دن ‪.‬‬


                                   ‫کنونی [‪ 0۳00060‬و ‪ « 180۳60‬واژه نامه ‪ ۰۹۳۰۰‬کیلکی اۇ‪b‬صنك‏ ‪.‬‬
                              ‫> رك ‪ :‬تنبور ‪.‬‬          ‫وجه اشتقاق عاصانه‬       ‫‪-‬‬    ‫‪۸‬‬           ‫رك‪ :‬دماو ند ‪۰‬‬        ‫‪۷‬‬

     ‫‪ #‬دلباله ‪ -‬جنم اول و کر پنجم ( لهجهٌ مرکزی ) › از ‪ :‬دتبال ‪ ( ۰ -۳‬پود نبت‬
                                                                       ‫کیلکی ‪al4bnud‬‏ ؛ عقب“ ضمیمه ‪.‬‬                    ‫وزاید (‬

                                                                                                         ‫‪۱۸۸‬‬        ‫حه‬
                                                                                                                     ‫صهفاز‬
                                                                                                                         ‫ش‬
                  ‫وتب دیگر ‪.‬‬‫راب «کلبله ودمنه» و بتقلید او در انوار‪-‬هیلی ک‬‫دت‬
                                                                          ‫‪ - ۴‬اصلا ک‬
         ‫‪(- ۷‬عر) «بی دستوری‬     ‫‪ - ٩‬بتشبیه بادمنة (کلیله ودمنه)‪. ‎‬‬     ‫ركك‪ :‬دمن ‪۰‬‬  ‫‪6‬‬
                   ‫‪۰‬‬   ‫تاگاه درآمدن ‪ :‬ولیز هلاك کردن» ‪ ۶‬متنهی الارب» «شرح قاموس»‬                          ‫درآهدن » وسدی‬

         ‫‪ - ۸‬دراراک (سلطان باد)« باد دمه» بادی که باسرما وبرفآمخته باشد‪« .‬مکی‌نژاد» ‪:‬‬


            ‫‪2‬‬           ‫‪ -‬بهلوی‬    ‫‪۹۱‬‬                    ‫‪۰‬‬   ‫معجم اللدان‬      ‫‪۱-9‬‬      ‫المالم ص‬      ‫رکه‪ :‬نود‬        ‫‪1‬‬

                                                                                                   ‫( زمین ) ‪ .‬رك ‪ :‬زمین ‪۲‬‬
                                                                                                             ‫ات‬


 ‫بنام شسخصویزن بیار بردلبةکوسفند بخلائند‬                    ‫داب غزو‪ ‌ ۱‬بنعنی دم غازه است که‬
‫و افولی خوانند و آارا درقبر کهنه بیاویز ند‬
 ‫وچراغی در زبرآن روشن کنند نا ازحرارت آن‬                                                            ‫عیب خوانند ‪.‬‬
 ‫چراغ دلبه بگدازآید و چندانکه دفبه میگدازد‬                  ‫د نباك ‪ = ۴‬م اول بر وژن اردک »‬
 ‫واغر میشود تابمیرد‪.‬‬
                   ‫آن شخص نیز میگدازد ل‬
                                                            ‫آرا ازچوب و سفال هم‬
                                                                              ‫دهلی باشد دم دراز که ن‬
 ‫دنبه نهادن ‪ -‬کنابه ازفرب وبازی‬                                ‫سازند وبازیگران در زیربغل گرفته نواز ن ‪.‬د‬
                                   ‫‪۳‬‬   ‫باشد ‪۴‬‬   ‫دادن‬
                                                            ‫د نبو‪ - 94‬بض‌اول وسکون ثالی وناك‬
 ‫‪3‬فح * ‪ -‬بانون و حایبی شقطه (‪)۱‬‬                             ‫را کویند که از‬     ‫‪ .‬موی‬    ‫و فتح واف‬         ‫بواو رسنده‬

 ‫وحر کت مجهول‪ .‬بلغت سربانی بممنی طلوصت‬                      ‫یسر آ وبخنه باشند ت وشمله وطره ودستار رالبز‬
 ‫ومراد طلوع عیسی علیه‌اللام است از نپراردن »‬                                                              ‫کفته‌اند ‪.‬٭‬
 ‫وآن رودخالنه‌است ترديك به دمشق ‪.‬گوین که‬
  ‫بی ين ز کریا عیی(ع)رادر آن رودخانه نشت‬
                                                            ‫دنه دادن ک»نابه از غافل کردن‬
 ‫ویضی گفته اند که مریم آن حضرت را در آب‬                                                   ‫وفرب دادن باشد ‪. ۴‬‬
 ‫معمودبه بشت وازآنت که صاری فرزندان‌خود‬                     ‫ده‌اد = ظرفی باشد که دنه‬
                                                                                   ‫گنب‬
                                                                                     ‫د‬
 ‫را ڪون متولد شوندبدان آب غل دهند وچون‬                      ‫ووعی از‬
                                                                  ‫گوسفند در مان آن برشت هکنند ‪ -‬ن‬
  ‫کی بدین عیی درآید وبآن آب غل دکند‬                          ‫رادرس م مترو انچتان)یدک اران‬
                                                                                   ‫وحا‪.‬‬       ‫جك‪:‬‬    ‫)‪۱‬‬



   ‫رلك‪ :‬دلبه نهادن ‪۱‬‬   ‫‪۴‬‬     ‫‪.‬‬    ‫‪kabnut‬‏‬       ‫نك‬     ‫‪= ۴‬‬         ‫غزه ‪.‬‬   ‫غازه ‪ ,‬دم‬   ‫‪ :‬دم‬   ‫رك‬      ‫‪۱‬‬
```


## [2026-09-05T20:10:47.319Z] TOOL CALL #19: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T20:10:47.327Z] TOOL RESULT

```


```


## [2026-09-05T20:10:49.715Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON donbal\"; grep -n \"دنبل\\|دنبلان\\|دمل\\|دنبك\\|دنبک\\|تنبک\\|تنبك\" MON_part1.txt MON_part2.txt | head -30",
 "description": "Grep Mo'in for donbal/domal"
}
```


### [2026-09-05T20:10:49.773Z] TOOL RESULT

```
=== MON donbal
MON_part2.txt:7299:دمل. (یز.) پوتیت () کندنل ن انساج حیوانی 
MON_part2.txt:24258:کو چک. (پز.) دمل دردنا کث زير جلدی که 
MON_part2.txt:24261:مشخصات دمل را دارد. موقعی که این دمل 
MON_part2.txt:27885:رنگ است؛ دمل کوچک. دانةٌ چرکی. 
MON_part2.txt:40026:لی؛: ۲() (یز.) دمل شکم کنل: 
MON_part2.txt:58057:دیگری فارسن است که بیشتر دمل‌های 
MON_part2.txt:61776:غده. دمل. هر چیز ممزوج) درهم آمیخته. 
MON_part2.txt:66367:مندمل: اعجوهل‌ومه [ع.] (افا.) جراحت به 
MON_part2.txt:71201:نابلد: دملدط-73 آف. ع.] (ص.) (عم.) آنکه 
MON_part1.txt:1543:بدان. دمل. 
MON_part1.txt:19175:سوزش بسیار» دمل و جوش ريزة بدن. 
MON_part1.txt:35643:خصوصاً گرهی که در میان دمل بهم رسد و 
MON_part1.txt:35644:تا آن را برنیاورند دمل نیک نشود. 
MON_part1.txt:43915:تشک: ۱0025 [- دنبک - طنبک] (ا.) 
MON_part1.txt:50177:زخم و دمل بیرون آید. مادهٌ تیره رنگ و 
MON_part1.txt:55739:روی بوست بدن پیدا گردد) دمل؛ ج 
MON_part1.txt:58460:دملی به شکل خیار که در غده‌های لنفاوی 
MON_part1.txt:62990:دمل: ام()«ه1 [ع.] (.) (پز.) زخمی که 
MON_part1.txt:63078:دنبک: ۲ ([- تشک - تمک] .) 
MON_part1.txt:63083:دنبلان: -(10۱0)۵ (امر.) (جان.) خاية 
MON_part1.txt:82415:دمل] (ا.) چ رک ریم. جراحت. 
MON_part1.txt:94209:موجب قبض و جمع دمل‌های جلدی شوند 
MON_part1.txt:97333:تولید دمل‌های دردناکك داخلی و با
```


## [2026-09-05T20:10:53.146Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '62975,63095p' MON_part1.txt",
 "description": "Mo'in donbal/domal entries"
}
```


### [2026-09-05T20:10:53.203Z] TOOL RESULT

```
آهنگران و مسگران. گلخن حمام. 

دم گرفتن: 12۲-0 (مص‌ل.) هماً واز 
شدن چند تن» شعری را دسته‌جمعی خواندن 
و تکرار کردن (در روضه‌خوانی» عزاداری يا 
مجلس صوفیان). سکوت کردن» توقف 
کردن» دست از کار کشیدن برای تازه کردن 


تفن 

دم گرگ: 1001-۰-8 (امر.) دنب گرگ 
ذنب ذثب. (کد.) صبح کاذب. (اخ.) یکی از 
منازل قمر. 

دمل: ام()«ه1 [ع.] (.) (پز.) زخمی که 
روی پوست بدن پدید شود و از آن خونابه 
و چرک آید؛ آسه. 


دم لا به: (0-)00۳0-1302 (امر.) دم جنبانیدن 
سک نزدیکك صاحب خود برای تملق. 
تملق» چاپلوسی. فروتنی. 

دمند ه: (ع-)902ه-صدل (افا.) فقوت کننده 
باد کننده. ورنده. روبنده. طلوع کننده. 
حر وشن ه. 

دمنه: (6)ممصعل [ع. دمنه ] (.) آثار خانه و 
حیات مردم در زمینی. جایی که خاکروبه 
ریزند» مزبله» خا کروه‌دان ) ج. دمن. 

دم‌و دستگا ۵ 20ع)120-0-025 (اسر.) 
شحو 6 حلال. اساب‌و آلات. 

دمور. تحددل (.) آواز نرم و آهسته. 
دمور؛ تام [ع.] (مسصل.) تساه شدن» 
هلاک گشتن. (امص.) تباهی» هلاکت. 
دمسوکرات: ۱ (ص.) ط فدار 
دموکراسی علاقمند به حکومت ملی. 
دسوکراتیک: 06001621-1 (ص‌نس..) 
طرفدار به دموکرات وابستهبه حکومت ملی. 
دموکراسی: 0۵0027 (امر .) حکومتی 
که در آن قدرت عالیه مشعث از ملت است و 
ملت اعمالش را هدایت می‌کند؛ حکومت 
مردم بر مردم. 

دمه: (۵-)120۵ (ا.) بخار. باد تند همراه برف 
و سرماء طوفان و باد. 

دمسه4: (6-)12022 01 ات دم‌یدن. دم 
آهنگری. ظرفی اسشت به هیثت کلة آدمی 
که در آن آب کنند و در کنار آتشی نهند. از 
سوراخ‌های بینی آن بخار بر آتش وزد و 
و افر وخته گردد؛ آتش‌افروز. 

دمه: (0-)2-«42 |- دم] (.) لبه چبزی مانند 
دمیدد: 0200-1127 (مصل.) (دمید» دمد» 
خواهد دمید» بدم» دمنده» دمان» دمیده؛ 
دمش). فوت کردن در چبزی» یف کردن» 
باد کردن. وزیدن (باد و مانند آن). سر از 
خاک در آوردن نبات» روییدن» رستن. سر 


۹" فرهنگک فارسی معین دمید ه 


ردن» طلوع کردن (صبح» خورشید» ماه و 
ضیره). کسی رابه سخنان چرب و نرم 
فریفتن. 

دمیده: (0-):0[-:32 (امسف.) فوت کرده؛ 
بف کر ده. وزیده. روینده. طلوع کرده. 
دن؛ 0 (.) فرباد و غوغای توام با تشاط. 
دن: «ده [ع.] (.) خم قیراندود که بزرگتر از 
سبو باشد. 

دئائت؛ 12021 [ع. دناعه | (امص.) بستی » 
پست فطر تی» نانجیبی. لثامت. خست. 
دنال" 120 (ص‌فا.) با نشاط رونده با 
شادی خرامنده. از خشم و قهر به جوش 
آینده. (حا.) درحال نشاط و هبجان. 
دنسبال: 00-51 (امر.) دم» ذنب. عقب 
چبری» پس چیزی. 

دنبالچه: (ه)م(۹0:02 (دعصف.) آخرین 
استخوان ستون مهره‌یی که در انسان از التیام 
۴ یبا ۵ مهره بوجود آمده. وجود این 
استخوان در اسان بجای دم در حیوانات 
می‌باشد. در جانوران تعداد سهره‌های 
استخوان دنبالجه متعدد است و آنها اسکلت 
دم ر تشکیل مي دهند. 

دن‌اله: (0-)000021-2 (امر.) دم. هر چیز 
مانند دم که در عقب جبزی باشد؛ دم مانند. 
پی» پس» پیر و عقب. عقبه. بقیً چیزی» پس 
مانده. ضمیمه. ضح.. به سه معنی اخیر لازم 
الاضافه است. 

دنباله‌دار: :۵-42 [- دنباله‌دارنده] (ص‌فا.) 
هر چیز که دارای دم باشد. هر چیز که دنباله 
و بقیه داشته باشد. ستارة دنباله‌دار: ستاره‌ای 
که دارای دم درازی است؛ ذوذنب. 
دنبک: ۲ ([- تشک - تمک] .) 
دهلی است دم دراز که از چوب و سفال 
سازند و بازیگران در زیر بغل گرفته و 
نت 

دنبلان: -(10۱0)۵ (امر.) (جان.) خاية 


گوسفند که آن را کباب کنند و خورند. 
بیضة گوسفند. (گیاء) نوعی قارچ که در 
امکنهٌ مررطوب روید و آن را در روغن تف 
دهند و حورند. 

دنمه: (۵-)0000-۸ (۱.) (جاد.) جزوی از بدن 
گوسفند که بجای دم در انتهای خلفی تن او 
آويخته و محتوی چربی است. پیه» چربی. 
دنبه دادن: 1.0 (مص‌م.) ( کد.) فریب 
دادن» فر بفتن.
```


## [2026-09-05T20:11:08.733Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%85%D9%84",
 "prompt": "Give the full etymology sections for Arabic دمل / دمّل (dummal) 'boil, abscess' and Persian دمل (domal). Does it say borrowed from Persian دنبل? Quote verbatim."
}
```


## [2026-09-05T20:11:10.446Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%85",
 "prompt": "Give the Persian entries for دم — especially دُم 'tail'. Quote the etymology verbatim (Middle Persian, Proto-Iranian, Avestan forms, and any related forms like دنب, دنبه)."
}
```


### [2026-09-05T20:11:15.064Z] TOOL RESULT

```
# Etymology Information for دمل

## Arabic دمل/دمّل

The etymology section states: "From the root د م ل (d m l). Compare Persian _دنبل_ (donbal, 'boil')."

The entry does **not** indicate that Arabic دمل was borrowed from Persian. Rather, it presents them as comparable words from different languages sharing a similar meaning.

## Persian دمل

The web page provided contains **only** the English Wiktionary entry for the Arabic term. There is no etymology section for a Persian entry of دمل included in this content. The page shows links to other language versions (including فارسی/Persian), but the actual Persian entry text is not displayed here.

To answer your question about Persian دمل's etymology, I would need access to the Persian Wiktionary entry itself.
```


### [2026-09-05T20:11:17.885Z] TOOL RESULT

```
# Persian دم (tail)

## Etymology 1: "Tail"

The entry states the word derives "From earlier _[دُنْب](/wiki/%D8%AF%D9%86%D8%A8#Persian "دنب")_ (dunb), see there for more."

Unfortunately, the detailed etymological chain for this sense is not fully provided in the document beyond this cross-reference.

## Etymology 2: "Breath"

This sense has a more complete etymology: "From [Middle Persian](https://en.wikipedia.org/wiki/Middle Persian "w:Middle Persian") [script needed] (dam), from [Proto-Iranian](https://en.wikipedia.org/wiki/Proto-Iranian_language "w:Proto-Iranian language") _[\*damH](/w/index.php?title=Reconstruction:Proto-Iranian/damH&action=edit&redlink=1 "Reconstruction:Proto-Iranian/damH (page does not exist)")_ ("to blow, breathe; to swell")"

The source also notes cognates including Sanskrit धमति (dhámati, "to blow"), Lithuanian, Polish, and English damp.

The document does not provide Avestan forms or additional Middle Persian details for the tail sense beyond the cross-reference to دنب (dunb).
```


## [2026-09-05T20:11:21.968Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%86%D8%A8",
 "prompt": "Quote verbatim the full Persian etymology of دنب (dunb) 'tail' — Middle Persian, Proto-Iranian, Avestan, PIE forms, cognates and derived terms."
}
```


## [2026-09-05T20:11:22.534Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%86%D8%A8%D9%84",
 "prompt": "Quote verbatim the Persian entry for دنبل (donbal) — meaning and etymology, and any link to Arabic دمل."
}
```


### [2026-09-05T20:11:26.356Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:11:28.798Z] TOOL RESULT

```
# Persian Etymology of دنب (dunb) 'tail'

**Middle Persian origin:**
"From Middle Persian dwm(b') (/⁠dum(b)⁠/)" leading to Proto-Iranian forms.

**Proto-Iranian and PIE roots:**
"From Proto-Iranian *dumáh, ultimately from Proto-Indo-European *dewmbʰ- ('penis, tail, rod')."

**Avestan cognate:**
"Cognate with Avestan duma, meaning 'penis'."

**Related language cognates include:**
Central Kurdish dû ('tail'), Northern Kurdish dûv ('tail'), Baluchi domb, Pashto lëm ('tail of sheep'), Ossetian dymæg, Sanskrit dumbaka ('the thick-tailed sheep'), and Old Armenian dmak ('fat tail of sheep').

**Related Persian terms:**
donbe, donbâl, donbâle, donbal, and donbalân all derive from this root referring to tail-related concepts.
```


## [2026-09-05T20:11:34.318Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%DA%98%D8%AF%D9%85",
 "prompt": "Quote verbatim the Persian entry for کژدم (každom) 'scorpion': etymology, Middle Persian form, components."
}
```


## [2026-09-05T20:11:35.153Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D9%86%D8%A8%DA%A9",
 "prompt": "Quote verbatim the Persian entry for تنبک (tonbak): meaning and etymology. Any mention of دنبک or onomatopoeia?"
}
```


### [2026-09-05T20:11:38.893Z] TOOL RESULT

```
# Persian Entry for کژدم (każom)

**Etymology:** "From Middle Persian [script needed] (gazdum). By surface analysis, کژ (kaž, 'bent, crooked') +‎ دم (dom, 'tail')."

**Middle Persian Form:** gazdum

**Components:** 
- کژ (kaž) meaning "bent, crooked"
- دم (dom) meaning "tail"

The entry notes this is a compound term where the semantics compare to Old Armenian kor, with related forms found in Semnani and Talysh dialects.
```


### [2026-09-05T20:11:41.827Z] TOOL RESULT

```
# Persian Entry for تنبک (tonbak)

**Meaning:** The primary definition is "tombak" (a percussion instrument), with "zarb" listed as a synonym. Etymology 2 notes it as an alternative form of تنباکو (tanbākū/tanbâku), referring to tobacco.

**Etymology:** According to the entry, it derives "From Middle Persian (twmbk' /tumbag/, 'drum'), according to Watkins, of imitative origin." It shares kinship with Old Armenian թմբուկ (tʻmbuk) and possibly Arabic دَرْبُوكَة (darbūka).

**Regarding دنبک and onomatopoeia:** Yes, both are mentioned. دنبک (dunbak/donbak) appears in the "Alternative forms" section. The entry explicitly categorizes this term under "Persian onomatopoeias," confirming its imitative etymological origin.
```


## [2026-09-05T20:11:51.603Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD watkins dumb/tap\"; grep -n -i \"dheu-b\\|dumb-\\|tappon\\|tuppa\" AHD_watkins1985.txt | head -20; echo \"=== KLN tap\"; grep -n \"^tap\\b\\|tap, n\\.\\|tappa\\|tuppa\\|toppr\" KLN_1966.txt KLN_1971.txt | head -20",
 "description": "Grep AHD and Klein for tap"
}
```


### [2026-09-05T20:11:51.679Z] TOOL RESULT

```
=== AHD watkins dumb/tap
382:blind: TYPHUS; TYPHLOSOLE. 11. Extended form *dheubh., “beclouded in the senses,” in suffixed o-grade form *dhoubh-o- in: a. Germanic *daubaz in Old English déaf, deaf: DEAF; b. nasalized form *dhu-m-bho- in Germanic *dumbaz in Old English dumb, dumb: pumps; c. Germanic *diibén- in Old English *dife, dove (< “dark-colored bird”): DOVE!. 12. Extended zero-grade form *dhwel- in: a. Germanic *dwelan, to go or lead astray, in Old English dwellan, to deceive (but influenced in sense by cognate Old Norse dvelja, to tarry): DWELL; b. Germanic *dulaz in (i) Old English dol, dull: DoL- DRUMS (ii) Middle Low German dul, dull: (DOLT), DULL. 13. Extended zero-grade form *dhwes- in Greek suffixed form *th(wjes-es-, smoke, whence Greek *th(w)es-es-yon, becoming theion, brimstone, sulfur: THIO-, THION-. 14. Perhaps Old English docce, dock (< “dark-colored plant”): Dock‘. 15. Perhaps Irish did, pipe: DUDEEN. [Pok. 4. dheu- 261.] dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English déaw, dew: DEW; b. compound *melith-dauwaz, “honeydew” (see melit-). [Pok. 1. dheu- 259.] dheu-’. To become exhausted, die. 1. Suffixed o-grade form *dhou-to- in Germanic *daudaz in Old English déad, dead: DEAD. 2. Suffixed o-grade form *dhou-tu- in Germanic *dauthuz in Old English déath, death: DEATH. 3. Suffixed o-grade form *dhow-yo- in Old Norse deyja, to die: DIE}. 4. Suffixed extended zero-grade form *dhwi-no- in Germanic *dwinan in Old English dwinan, to diminish, languish: DWINDLE. [Pok. 2. dheu- 260.] dheub-. Deep, hollow. 1. Germanic *deupaz in Old Eng- lish déop, deep: DEEP, DEPTH. 2. Germanic expressive denominative *duppjan in Old English dyppan, to im- merse, dip: pip. 3. Parallel root form *dheubh- in Ger- manic *deub-, *dub- in verb *diibjan in Old English dyfan, to dip, and difan, to sink, dive: pivE. [Pok. dheu-b- 267.] dheubh-. Wedge, peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek teukhos (< *theukhos), gear, anything produced, tool: HEPTATEUCH, HEXATEUCH, PENTA- TEUCH. [Pok. dheugh- 271.] dhghem-. Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, “earthling,” in Germanic *gumén- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth: CHTHONIC; AUTOCH- THON. 3. Zero-grade form *dhghm- in Greek khamai, on the ground: CHAMAEPHYTE, CHAMELEON, CHAMOMILE, GERMANDER. 4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth: HUMBLE, (HUMILIATE), (HUMILITY), HUMUS; EXHUME, INHUME, TRANSHUMANCE. 5. Suffixed o-grade form *(dh)ghom-on-, “earthling,” in: a. Latin homé, human being, man: HOMAGE, HOMBRE!, HOMINID, HOMO!, HOMUNCULUS, OMBRE; BONHOMIE, HOMICIDE; b. (in part) Latin himdnus, human, kind, humane: HUMAN, (HUMANE). 6. Suffixed form *(dh)ghem-ya in Russian zemlya, land, earth: SIEROZEM, ZEMSTVO. 7. Full-grade form *(dh)ghem- in Persian zamin, earth, land: ZAMINDAR. [Pok. ghdhem- 414.] dhghut-. Fish. Greek ikhthus, fish: 1cHTHYO-. [Pok. ghdha- 416,] dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic “ges-ter- in Old English geo- stran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.] dhgvhei-. To perish, die away. Zero-grade form *dhgvhi- in Greek phthinein, to die away: PHTHISIS. [Pok. gthdhei(a)- 487.)
407:[dub-. Also dup-. To drop, dip. Germanic imitative root. 1. Old English -doppa, a kind of bird (< “one that dips”): DIDAPPER. 2. Dutch doopen, to dip: DOPE. 3. Old English *dympel (diminutive with nasal infix), pool, dimple (> Middle English dimpel): DIMPLE. 4. Norwegian dumpa, to fall suddenly, akin to the Scandinavian source of Middle English dumpen, to dump: pump. [In Pok. dheu-b- 267.]]
=== KLN tap
KLN_1971.txt:55249:handle roughly, misuse’, ON. stappa (for *stam- 
KLN_1971.txt:85789:L. *stuppare, ‘to stop with flax or tow’ (whence 
KLN_1971.txt:85791:stuppa, stupa, ‘the coarse part of flax, tow’. See 
KLN_1971.txt:142904:tap, lit. ‘the great (story of the) Bharatas’. OI. 
KLN_1971.txt:157928:fr.OE. myrra, fr. L.myrrha, fr.Gk.[Jtuppa, ‘myrrh, 
KLN_1971.txt:230966:stappa (for * stampa), Dan. stampe, Swed., 
KLN_1971.txt:230967:Norw. stappa , stampa, MLG., MDu., Du. stam- 
KLN_1971.txt:232553:perh. a blend of VL. *stuppare , ‘to stop with tow’ 
KLN_1971.txt:232786:(j bot .) — ModL., fr. L. stipa, stupa, stuppa , ‘the 
KLN_1971.txt:233245:fed). These words derive fr. ML. stuppare , ‘to 
KLN_1971.txt:233248:tow’), fr. L. stuppa, stupa, ‘the coarse part of 
KLN_1971.txt:234584:The derivation of OF. estoffe, etc., fr. L. stuppa , 
KLN_1971.txt:241185:tap, n., faucet, cock. — ME. tappe , fr. OE. taeppa, 
KLN_1971.txt:241194:tap, tr. v., to supply with a tap. — ME. tappen, 
KLN_1971.txt:241199:tap, tr. and intr. v., to strike lightly. — ME. 
KLN_1971.txt:241249:tap it ion, the MGk. pronunciation of Gk. xa- 
KLN_1971.txt:241298:tap liquors’, fr. taeppa, ‘tap’. See tap, ‘pipe’, 
KLN_1971.txt:241814:tap, ‘pipe’, and to. 
KLN_1971.txt:249772:ME., fr. OE., related to ON. toppr , ‘tuft of hair’, 
KLN_1971.txt:249849:‘timbrel, tambourine’, rel. to Aram, tuppa, of
```


## [2026-09-05T20:11:52.362Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/tap",
 "prompt": "Quote verbatim the etymology of tap (n.) 'stopper/faucet' — Proto-Germanic form, and whether any PIE root is given. Also any note on tattoo/tampon relation."
}
```


### [2026-09-05T20:11:57.900Z] TOOL RESULT

```
# Etymology of Tap (n.1) - Stopper/Faucet

**Direct Quote:**
"from Old English _tæppa_, from Proto-Germanic _\*tappon_"

**Proto-Germanic Form:** *\*tappon*

**PIE Root:** The source explicitly states "Boutkan gives it no IE etymology" — meaning no Indo-European root is provided.

## Note on Tattoo/Tampon Relation

The page does not discuss any connection between tattoo and tap. However, it does mention **tampion** in the "More to explore" section, describing it as "a nasalized variant of Old French tapon" that is "related to Old High German zapfo and Old English tæppa 'stopper'" — showing tampion shares the same Germanic root as tap (n.1), both deriving from the stopper/plug concept.
```


## [2026-09-05T20:12:08.924Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '241185,241210p' KLN_1971.txt; echo \"=== tattoo\"; grep -n \"tattoo\" KLN_1971.txt | head; echo \"=== tampon\"; grep -n \"tampon\\|tampion\" KLN_1971.txt | head; echo \"=== top n\"; grep -n \"^top, n\" KLN_1971.txt | head; echo \"=== tip n\"; grep -n \"^tip, n\" KLN_1971.txt | head",
 "description": "Klein tap/tattoo/tampon/top/tip"
}
```


### [2026-09-05T20:12:09.064Z] TOOL RESULT

```
tap, n., faucet, cock. — ME. tappe , fr. OE. taeppa, 
rel. to MDu. tappe, Du. tap , OHG. zapho , 
MHG. zapfe, G. Zapfen , fr. Teut. *tappo-. Cp. 
the Teut. loan words: F. tapon and its nasalized 
var. tampon^ ‘plug, stopper’. It. zaffo, Sp. tapon , 
of s.m. (see tampon). Cp. also tapadera, tapster, 
tip, ‘end’, and the first element in tattoo, ‘drum • 
beat’. 

tap, tr. v., to supply with a tap. — ME. tappen, 
fr. OE. taeppiat t, fr. txppa, ‘tap’; rel. to MLG. 
tappen , MHG., G. zapfen, ‘to tap’. See prec. 
word. 

tap, tr. and intr. v., to strike lightly. — ME. 
tappen , fr. OF. (= F.) taper ; of imitative origin. 
Cp. tappet and tip, ‘to touch gently’. Cp. also 
dab, ‘to strike lightly’. 

Derivative: tap , n,, a light blow, tapp-er , n., 
tapp-ing, n. 

tapa, n., cloth made from the inner bark of the 
tree Papyrius papyrifera. — Of Marquesan ori- 
gin. 

=== tattoo
105481:‘he wrote’, kAhdbeth, ‘tattooing’, Arab, kataba 
130978:grave’; cp. Heb. k e thdbeth, ‘tattooing’ (Lev. 
182163:‘the painted or tattooed ones’ (fr. L. pictl, pi. of 
241191:tip, ‘end’, and the first element in tattoo, ‘drum • 
241811:tattoo, n., drum beat. — Du. taptoe , lit. ‘closing 
241816:tattoo, tr. v., to mark (the skin) with pigments ; n., 
241817:the act of tattooing. — Of Polynesian origin; 
241821:Derivatives: tattoo-age , n., tattoo-er , n., tattoo- 
241824:tattoo, n., a native-bred pony in India. — Hind. 
244094:tram, ‘vehicle’, trance, trumeau. Cp. also tattoo, 
=== tampon
133490:coffeehouses tampons, ‘let us drink’, fr. lamper , 
240859:tamper , fr. Frankish *stampon, which is rel. to 
240861:stamp, v. and cp. tampon. 
240870:tampion, n., a wooden plug or stopper put in the 
240872:var. of tampon. Cp. tompion. 
240873:tampon, n., a plug of cotton inserted into a 
240880:Derivative: tampon , tr. v. 
240881:tamponade, tamponage, tamponment, n. — Hy- 
240882:brids coined fr. tampon, with the suffixes -ade, 
241189:var. tampon^ ‘plug, stopper’. It. zaffo, Sp. tapon , 
=== top n
249771:top, n., the highest part of anything, summit. — 
249781:top, n., child’s toy. — ME. top, fr. OE. top, back 
=== tip n
248502:tip, n., end, extremity of anything. — ME. tip, 
248516:tip, n., I) gratuity; 2) a hint. — Of uncertain ori-
```


## [2026-09-05T20:12:12.222Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '249771,249790p;248502,248516p;240873,240882p;241811,241822p' KLN_1971.txt",
 "description": "Klein top/tip/tampon/tattoo entries"
}
```


### [2026-09-05T20:12:12.295Z] TOOL RESULT

```
tampon, n., a plug of cotton inserted into a 
wound, orifice, etc., to stop bleeding. — F. f 
a nasalized var. of tapon, ‘plug’, formed with 
suff. -on fr. Frankish *tappo, which is rel. to 
OHG. zapfo, OE. txppa , ‘tap’. See tap, ‘pipe; 
cock’. 

Derivative: tampon , tr. v. 
tamponade, tamponage, tamponment, n. — Hy- 
brids coined fr. tampon, with the suffixes -ade, 
tattoo, n., drum beat. — Du. taptoe , lit. ‘closing 
of the taps’, fr. tap , ‘tap’, and toe, ‘to ; shut’ (for 
sense development cp. G. zu, ‘to; closed’). See 
tap, ‘pipe’, and to. 

tattoo, tr. v., to mark (the skin) with pigments ; n., 
the act of tattooing. — Of Polynesian origin; 
cp. Tahitian tatau , tatu , ‘puncturation, mark 
made on the skin*. 

Derivatives: tattoo-age , n., tattoo-er , n., tattoo- 
ing , n. 
tip, n., end, extremity of anything. — ME. tip, 
tippe , rel. to Dan., Norw., MLG., MDu., Du. 
tip , Swed. tipp, MHG. zipf, zipfel, G, Zipfel and 
in gradational relationship to OE. txppa , ‘tap’. 
See tap, ‘pipe’, and cp. tippet. 

Derivatives : Up, tr. v., to furnish with a tip, tipp- 
er, n. 

tip, tr. v., to touch lightly, tap. — Cp. LG. tippen, 
G. tappen, ‘to touch lightly’, and E. tap, ‘to 
strike lightly’. 

Derivative: tip, n., a slight touch, 
tip, n., I) gratuity; 2) a hint. — Of uncertain ori- 
top, n., the highest part of anything, summit. — 
ME., fr. OE., related to ON. toppr , ‘tuft of hair’, 
OFris. top, ‘tuft’, ODu. topp , Du. top, ‘top’, 
OHG., MHG. zopf, ‘end, tip, tuft of hair’, G. 
Zopf, ‘tuft of hair’, Cp. tuft, toupee. Cp. also 
topple. 

Derivatives: top, adj. and tr. v., top-less , adj., 
topp-ed, adj., topp-er, n., topp-ing , adj., topp- 
ing- ly, adv., topp-ing-ness , n. 
top, n., child’s toy. — ME. top, fr. OE. top, back 
formation fr. OF. topet (cp. OF. topoie, F. 
toupie), of s.m., fr. ODu. topp, ‘head or top of 
something’, which is rel. to OE. top, ‘summit’; 
see prec. word. Cp. OHG. doph, top f, ‘top (for 
spinning)’ (whence MHG., dial. G. fop/, of 
s.m.), which is an OF. loan word, 
top-, form of topo- before a vowel, 
toparch, n., ruler of a petty state. — Late L. to - 
parcha, fr. Gk. Tonrapx^C, ‘governor of a dis-
```


## [2026-09-05T20:12:31.645Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM دمل\"; grep -n \"دمل\\|دنبل\" AFM_pages.txt | head -10; echo \"=== TAD\"; grep -n \"دمل\\|دنبل\" TAD_pages.txt | head -10; echo \"=== ARB\"; grep -n \"دمل\\|دنبل\" ARB_mo3rb.txt ARB_abdulraheem.txt | head -10; echo \"=== PLA\"; grep -n -i \"dummal\\|dunbal\\|donbal\\|Geschwür\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -10; echo \"=== FVQ\"; grep -n -i \"dummal\" FVQ_pages.txt | head",
 "description": "Grep Arabic-loan books for domal"
}
```


### [2026-09-05T20:12:31.749Z] TOOL RESULT

```
=== AFM دمل
1700:(الدمل) ܨ وهو غراى قالله يال قاريق وحمي 6 ܨ الله .
1701:قلت وهو معرب عن دمل الذي ܬܝܐܘ
=== TAD
=== ARB
ARB_mo3rb.txt:3242:من أسياجها» يقال: : أسؤة » وأسية » فُن ع قال أسمة جعلها أسما الرلة بعيئها » ودن قال أسوة دملها جمع 
ARB_mo3rb.txt:6737:والخلامق سيأ فى باب ابم ؛ وقال المؤلف هناك : « الذى يرى به الصبران ؛ وهو الطين المدور المدملق 
ARB_mo3rb.txt:8490:8 و”ابذلاهق' الذي ' بر و4 المبيان وهو الطين دور ا مدملق » وى 
ARB_mo3rb.txt:11731:الحسد كله ٠‏ وقيل : شمل سائر الأثواب أيضا» ٠‏ (م) ””دملك'“ بقعم الدال واللام و بيهما هاء 7 
ARB_mo3rb.txt:19202:وذ كنا أن مصحح ب دملها « ين باد» وتروّدنا فى صما ٠‏ ع باد» 
ARB_mo3rb.txt:23326:0 0 وإن 35 57 هذا اليناء أءواسدمله قُّ شعر أو كلا: م فالرد ول يه وم 
ARB_mo3rb.txt:24281:وتشديد الياء» وق ل أدو عبيدة معمر بن الم فى شرحه لرعلية ام دمل غناك رإخوته » 0 3 
=== PLA
9666:> - dumal: "Geschwür, Furunkel" pers. >» dumbal 1°, 
=== FVQ
```


## [2026-09-05T20:12:34.121Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB dum\"; grep -n \"dumb\\|dum '\" HUB.txt | head -10; echo \"=== ARY دم/دنب\"; grep -n \"دنبه\\|دنبال\\|کژدم\\|دنبک\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY latin\"; grep -n -i \"^DUM\\|TAIL\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Grep Hubschmann and Aryanpur"
}
```


### [2026-09-05T20:12:34.196Z] TOOL RESULT

```
=== HUB dum
5200:dmak fiir phi. *dwmai = dumbak, zd. duma 'Schwanz'; arm.
8811:stank', zd. gainti-; gandum 'Weizen, skr. godhuma-; gunda
9174:dunb-al *Schwanz', bal. LW. dunbag, nb. dumb, dunb, phi.
9175:dum, dumb, dumbak Bdh. 61. 148, 61. and Ind. 281—282,
=== ARY دم/دنب
=== ARY latin
405:b5 gal gy cael ge Obj GI HEF 5 AT tails SLL 9 yb Gene Cod pres ys
969:Snr ge ME gubitilends y pokatils 5 Sle gary 2 5p jl we dy diay lnaatail 1
8104:DUMAG, DIMAG —-«(OSSETIC) zu)
8107:MACKENZIE: (TAILD 136 DUNB, DUMB, DUNBAG
8145:DUMO, DOTI (SANSKRIT) 2 Sule
8146:DUMIU, DUMTI (LITHUANIAN) (gi -5 DHAMATI, DHAMYATE, DHMAYATE
8221:DUMAI LITHUANIAN) ol Lo HAFGHANI) (4) git
8222:DUMI LATVIAN) (3) gx TUTE :(TOKHARIAN B) B 5 j)58
8223:DUMIS (OLD PRUSSIAN) nS 3.2 (SANSKRIT) ex, Sie
8226:DUMACHA, DE THUMOS GREEK) gli
```


## [2026-09-05T20:12:43.967Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM ctx\"; sed -n '1690,1710p' AFM_pages.txt; echo; echo \"=== AFM leaf/page\"; python3 -c \"\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nff=0\nfor i,l in enumerate(t,1):\n    ff+=l.count('\\f')\n    if i==1700: print('formfeeds before 1700:',ff); break\n\"; grep -n \"\\[pdf page\" AFM_pages.txt | awk -F: '$2>1650 && $2<1760' | head",
 "description": "Addi Shir dummal context"
}
```


## [2026-09-05T20:12:45.030Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PLA ctx\"; sed -n '9650,9680p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt; echo \"=== HUB ctx\"; sed -n '9165,9185p' HUB.txt",
 "description": "Asbaghi and Hubschmann contexts"
}
```


### [2026-09-05T20:12:45.710Z] TOOL RESULT

```
=== AFM ctx
30 وقالت فيه العرب د مر ود مر الى غير ذلك
(الداموق) اللار 9 9 0 وكزر .)ܕ ومنة مأخرة
6 1 وهو كور اماد
(الدمق ) ريح وثلج تعريب دمه
(الدمقس 9 والدقّس) مسر بالابريم وقيل £ الدبياج او ¬
او ܐܐ ܨ الا مض ܡܩܡ ܢܝ د مسه:ومعتاة اطرييره الافض اوه تيون الل محلية
دمشق (021225661115 21111115م) وهو 20:07 با 0 (عاموس ”*: ¥ | ) ٠‏ واليوم
0 الدِمقس منسوب الى دمشق في كثير من اللغات وهو 0145125 3977 0
وع001735[1 بالاتكايزنة و0ع0317235 بالايطا ® وغ1001125 باكرماسة ( راجع
القاموس العبرالي تاليف جاسلئلموس )
(الدمل) ܨ وهو غراى قالله يال قاريق وحمي 6 ܨ الله .
قلت وهو معرب عن دمل الذي ܬܝܐܘ
0( 003 الأهد (005002 10 اي نفس ومن كير ܦ ماسك
( الداناج » تعريب 18 وهو العالم ٠ومن‏ الداناج مأخوذ د نج ' اي ܒܨܐ
0ل فارسي محض وهو ܣ الصيني المعروف بحب ܐܝܐ | ܨ
السلاطين
5 والدّانآق) سدس < تعريب دانك وهو بمعنى اللبّة مطاقاً ومن
ܠܨ ܪ ܓ الفاس فتعريت :23نب او 501115 اواك
ܬ0007.2 11 تعر ينب 1111111115
0 (الدانق ) 1 ܐܕ والسارق ܠ ܟ لاا دناه الأحى . “٠‏ ومنه ܐ ܐܢܐ 3
# (الدنقة » يعنى سفلة الناس ܨ 2

=== AFM leaf/page
formfeeds before 1700: 67
```


### [2026-09-05T20:12:45.755Z] TOOL RESULT

```
=== PLA ctx

9>- dalw: "Eimer" pers. mp. SePdol 8 syr. Do). 


Gw)- damsaqg: "weiße Seide" ? 2, 


> - damaq: "Wind mit Schnee" 10 aus dem pers. fg. dam v. Verbo,., damidan 


"atmen, wehen" 11, 


as-,- damaga: "Blasebalg des Schmiedes" aus dem pers.ol&, damgäh 12, 


> - dumal: "Geschwür, Furunkel" pers. >» dumbal 1°, 


1. Chista. Bd. 10 S. 1192. 

2. Dozy s. v., Muhit s. v. 

3. Mackenzie s. v. 

4. Muhit s. v. 

5. albasa s. v. 

6. Fremdwörterbuch s. v. 

=== HUB ctx
Z. 8 und 6 V. u.); gr. LW. karanh = karan = kalam —
arm. kalamb 'Kohl* (Faust us v. Byz.) = gr. xoti/upT] (vgl.
NSldeke, Pers. Stud. 2, p. 44); stmb ^^ sum^) 'Hnf, phi.
sumh Bdh. 61. 182, sunb Yatk. i. Zar. p. 67, Anm. 68,
arab. sunbok (de Lagarde, Symmicta p. 60), arm. smbak
(5. Jhd.), ap. *su(n)ba' oder *sn(n)pa-j vgl. zd. sofa- *Huf';
paskam 'domus aestiva' = arm. patskam, patskamb *6emach*
= ap. *pati'skamba' (oben p. 41).
b) ni ist urspriinglich in: dtmi = dunb^), dnnba,
dunb-al *Schwanz', bal. LW. dunbag, nb. dumb, dunb, phi.
dum, dumb, dumbak Bdh. 61. 148, 61. and Ind. 281—282,
dunb, dunbak West, PT. I, 337, arm. dmak (aus *duniak,
5. Jhd.), zd. duma- (s. oben p. 63); rtim, rilma, rum, ruma
(pi. rumgan), runb, runba *Schamhaare*, skr. roman- *Haar
(am Korper).
c) Unsicher ist, ob nb oder m urspriinglich ist in:
na7n 'feucht*, phi. nam, namb Bdh. 61. 250, bal. namb 'Thau,
Neber, afgh. nund, numd, lund 'feucht', das ich = ap.
^namna- = arisch ^^nablina- (vgl. kam *wenig = ap. kamna
Fiir
*) Bal. srunbe, suriim 'Huf gehort zu np. suru 'Horn* etc. —
```


## [2026-09-05T20:13:00.284Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=1701 && /\\[pdf page/ {last=$0; ln=NR} END{print \"AFM last pdf tag before 1701:\", ln, last}' AFM_pages.txt; grep -c \"pdf page\" AFM_pages.txt; head -3 AFM_pages.txt; echo \"=== PLA page tag\"; awk 'NR<=9666 && /\\[pdf page/ {last=$0; ln=NR} END{print \"PLA:\", ln, last}' incoming/PLA/PLA_pages.txt 2>/dev/null; awk 'NR<=9666 {n+=gsub(/\\f/,\"\")} END{print \"PLA djvu formfeeds:\",n}' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt; echo \"=== HUB leaf\"; awk 'NR<=9174 {n+=gsub(/\\f/,\"\")} END{print \"HUB formfeeds:\",n}' HUB.txt",
 "description": "Locate page numbers for AFM, PLA, HUB"
}
```


### [2026-09-05T20:13:02.303Z] TOOL RESULT

```
AFM last pdf tag before 1701:  
0
8
0
ܥܝ
=== PLA page tag
PLA:  
PLA djvu formfeeds: 0
=== HUB leaf
HUB formfeeds: 266
```


## [2026-09-05T20:13:08.905Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && python3 -c \"\nimport json\nd=json.load(open('sources/refs_online.json'))\nfor k in ['AFM','PLA','HUB','MON','NYB','ARY','FVF']:\n    e=d.get(k) or {}\n    print(k,'|offset:',e.get('page_offset'),'|hint:',(e.get('lookup_hint') or '')[:300]); print()\n\"",
 "description": "Page offsets for AFM PLA HUB MON NYB"
}
```


### [2026-09-05T20:13:11.012Z] TOOL RESULT

```
AFM |offset: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image |hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').

PLA |offset: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). |hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)

HUB |offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.

MON |offset: None |hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe

NYB |offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.

ARY |offset: printed page = pdf page + 1 |hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY

FVF |offset: None |hint: Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.
```


## [2026-09-05T20:13:23.335Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PLA page\"; grep -n \"dumal\" incoming/PLA/PLA_pages.txt | head; awk '/dumal/{print NR\": \"$0}' incoming/PLA/PLA_pages.txt | head -3; python3 -c \"\nt=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nff=0\nfor i,l in enumerate(t,1):\n    if 'dumal' in l: print('line',i,'leaf(1-based)',ff+1,'printed page',ff+1-15); break\n    ff+=l.count('\\f')\n\"\necho \"=== NYB leaf 90\"; awk 'BEGIN{RS=\"\\f\"} NR==91' NYB_vol2_glossary.txt | head -30",
 "description": "PLA page and Nyberg p82"
}
```


### [2026-09-05T20:13:25.173Z] TOOL RESULT

```
=== PLA page
7168:                                                                                                                                      dumal
7203:> - dumal:               "Geschwür,                    Furunkel"                  pers.      >» dumbal          1°,
7223:Ol.)          -    dumlän:         Pl.      V.g.       dumal.
7168:                                                                                                                                       dumal
7203: > - dumal:               "Geschwür,                    Furunkel"                  pers.      >» dumbal          1°,
7223: Ol.)          -    dumlän:         Pl.      V.g.       dumal.
line 7168 leaf(1-based) 139 printed page 124
=== NYB leaf 90
child: 1. frazand 6522-25, 661"; with the indef. art. —-e [~ + 1] 86%; ~ varzitan to produce children 67%; pl. cas. rect. ~ 963, 9726, 10514; pl. cas. obl. ~-dn 6913, ~-in [plendyn] F:5. — 2. fra- dand 16, 1013-18, 1119.11.24, 123.12.21.25. 1526 (after numeral). 1676; pl. cas. obl. —-ān 210, 37186 99, 12% 1423-5, [51% 2217, = Av. (1004 sq.) frazanti- ; MPrthPrs frzynd, MPrs also przynd; Ps. plendy; Paz. far- zand frazand; NP farzand. — fradand is the authentic SW form, preserved as an orthographical archaism, and listed in FrP ll with the gl. frazand ; the first -d- of fradand is not a dwarfed z, which only occurs in ideograms, and in the inscript- ions has a form wholly different from d.
(frazandéh abstr.) fradandéh the state of being a child: pat ~ as his own child 2?5,
Frazdän [pled?n'] the name of a river 11578, — Av. (1005) Frazdānu-.
Frazišak [Paz.] n. pr. 47*. — BdA p. 230? plzwtk; BdJ 782% Frazušag [Paz.].
fražaftan [pleptn'] to come to an end, pt. frazaft finished, in the subscriptions of books: 17, 30 etc. passim. — Av. (500) fra-gam-, pres. fra-jasaiti ‘to arrive at’; MPrs pres. frzwfs- ‘to be accomplished (A-H IT), caus. pl. prz’pt ‘to accomplish’; Verbum 190sq. Cf MPrth hnjftn, pres. hnj'm-, v.s. v. hanjām-.
frēc
fražām [ple’m] end 804. 81!; pat ~ lastly, in the end 645.721, 7212-5; ~~ pērē- zēh the final victory 77?” sq. — From the preceding vb.; Paz. farjam, faržam; NP farjam.
fražimčnitan [~-ynytn'] to complete, to carry to a conclusion 106%. 1138; v. also pat-fražāmēnītan.
tražām-kārēh [—-k'lyh] the final (escha- tological) work 7727,
frče [plyc] a surplus, or a remainder, a rest: martom (indir. obj.) — pat nēvakē- keh <i> hàn kunēnd i-šan andar gehän apäyisniktar veh dit to mankind they (the gods) will make a surplus above the felicity which in this world was seen by them as the most exquisite and the very best 10025-26 i. e., mankind will be given a felicity above the most exquisite and the very best felicity they experienced in this world. — Paz. fréz-, fréz- (v. next group) = BP /réc < *fraréc (haplology) < Olr *fra-raica- (from fra + ratk-, v. rertan), cf Skr prarecana- ‘surplus’, pra- reka- ‘abundance’, properly ‘what is pro- jecting’. To it belongs the vb. frčatan fréc- l. ‘to be over, to be left, after necessary expenses, as a gain or a rest’, 2. ‘to put aside what is surplus, to save’, or, ‘to increase by a surplus’. Cf (Paz.) ne neki frežašni . .. rà ‘not in order to add to the well-being’ SGV III, 24, Skr. v. subhasya visphitaye; har cé frēcēt hac all that is left of, or after BdA p. 1107 (plycyt' with the first y marked) = BdJ 397; PY 687; frčat ‘savings’ PVd. 379%. 1888 (comm.). Bthl., followed by others, read paréc- < *pari-raica-, identifying it with Sogd p’r’yc- ‘to leave, to abandon? (ZairWb 52; MIrM I, 14. II, 11.38 sq.) and adducing as a parallel Gr repuhehevujuevoc. However, the Paz. reading frēž is firm, unimpeachable and transparent, and as representing a living WIr tradition it 1s preferable to any reading based on Elr material (besides, Sogd p'r'yc- seems to
www.parsianjoman.org | ool wok
frée
be a secondary form of ?pr'yc-, pr'yc-, Gauthiot 126, Benveniste, GS 19). Cf also Dhabhar, PYV, Gl. p. 80. — This vb. coinc
```


## [2026-09-05T20:13:33.859Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read().split('\\n')\nff=0\nfor i,l in enumerate(t,1):\n    if i in (1372,1373,1653,1654): print('line',i,'leaf',ff,'printed',ff-8,'::',l[:90])\n    ff+=l.count('\\f')\n\"",
 "description": "Nyberg page for dumb and gazdum"
}
```


### [2026-09-05T20:13:35.763Z] TOOL RESULT

```
line 1372 leaf 79 printed 71 :: dumb [dwmb'] tail: brit. ~ 2418, v. brī- tan; burritak-—-& (-& in attributive po- sition) 
line 1373 leaf 79 printed 71 :: Dumbävand [dwmb’wnd] Mount Dama- vand 115%, — KZSPrth 1. 24 dwnb'wntš, Gr. v. douu.ßaouvd,
line 1653 leaf 94 printed 86 :: gaz-dum [gedwm] scorpion 76°. — Also spelt gzdwm, gzdm. ‘Whose tail is sting- ing’: v. the
line 1654 leaf 94 printed 86 :: gaž-dumb [g'edwmb'] a musical instru- ment, the horn 201%, — Mentioned to- gether with tum
```


## [2026-09-05T20:13:51.524Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13675,13695p' BRT.txt",
 "description": "Bartholomae duma- context"
}
```


### [2026-09-05T20:13:51.563Z] TOOL RESULT

```
•  g.  dütya-  n.  'Botschaft":  maraxtärS jigirsiai  (sd.)  kämt  %wahyä   mq>:rSne  Y.
Ableit.  au»  däla:  —  ai.  dSlyä-  n.  —  Pü.: davH^I  oitt  göiuSk  {s.  IM  düta-),  mit  der  Erl,; pesfSi;  Sil-;  puraksarafi.  —  •)  Wegen  Sü.  die wahrscheinlichere  I-esung,  sva.  "Läufer';  NpQ. allerdings  güyi.
•  j.  duSuwi.buzday-  f.  'Angstgefühl,  In- angstgeraten"':  'da  (LS.)  T.2S&.
*duimaa)r-  m.,  red.  Bild.;  Et.?')  —  'iuiday-, lum  V.  iat>d-  {%  $3  I);  ai.  buddhiy  f.;  vgl. apailLbiuH.  —  Ri.;  sahm  nimäyiSnlh  'Angsl- erregen,  Inangstversetzen',  mit  der  Erl.:  an bavel  ka  gäaiit  ka:  pa  snlh  gcdklha  icmem ;  s. dazu  No.  1  und  Reichelt  WZKM.  1$.  143. —  I)  Das  Wort  steht  unter  den  strafrecht- lichen Term.  Cecbn. ,  aber  zu  Unrecht.  Man hat  die  mit  der  Straftat  beabsichtigte  Wirkung für  die  Straftat  selbst  genommen.  Nach  V. 4. 17  könnte  an  derSlelle,  der  das  Wort  ent- DOmmen  ist,  etira  gestanden  haben :  *yö  narim duiuwi^uida  datäili  aetaS  Ai  "?-  (Name  der Straftat).  —  »  Vil.  zu  nhd.  taub  usw.
•  p.  dubäla-  ra.  Naroe  einer  Landschaft in  Babylon:  Aauv  uäapata/S  bäbiratcv  'la* nämlf  dahyäui  hacd  avadasJ^  hauv  uda- patata  Bh.j.  13.
•  j.  dunman-  n.  ''Nebel,  Nebelwolke, Wolke':  yayata  'ma  ,  .  frä.ap3m  nyäpftn upa.3p^m  (sd.)  V.21.2;  F.^g;  —  apim.. MdSrra  vat>m  'mqnia  ¥.5.15;  —  naioa 'man  utjasaiti  haratky3  paiti  banzayä "und  nicht  steigen  Nebel  empor  von . ."  Yt. 10. 50;  —  Hat  tat  'man  hqm.hishnti  . .  äat tat  '"tan  frasäupayeiti  (sd.)  magyS-kara Yt  S.  31 1
KompA.  —  VgL  dv<(nmatf'<).  —  Pü.:  mof.  — ■)  Für  falsch  halle  ich  Salemanns  Zu-^ammen- stellnng  von  dunita»-  mit  np.  damävand, GltPh.  /.  266;  vgl.  lu  duma-.
•  j,  dunmö.frut-  Adj.  'in"  den  Wolken fliegend':  vats  (NP.)  vänti  'tB  (NP.)  xä paiti  Yt/J.i4-
*/rut-  Adj.,  zum  V.  /rav:  —  ai.  'prul-  Adj.  — >)  Oder  auch  'mit'  oder  'mittelst',  wenn  die Wolken  als  Flügel  des  Windes  gedacht  wur- den.   DsT.s  *poussant  tes  nuees'  ist  unrichtig.
•  j.  duma-  m,  'Schwanz':  dasinam  . .  hao- yqm  Ml  (näml,  !BnS)  patöyam    upa.kprm-
taym ..  'nwiiHt  hl  upa.^w>rjsaym  ". .  sollen sie  ihm  auch  noch  den  Schwanz  abschnei- den" V.y.34.
zEt.  s-  S  '4>  Bthl.  Sind.  3.  101,  SDtterlin iF.  4.  93;  unriehtiE  GlrPh.  /.  a66.  —  np. dum,  dumb.  —  P[l.  1  dum.
•  j.dutnruf  n.  -?-"':  aosia{^A.)ca  paiti 'naca  %rivataca  gaisul  V.  7.  59.
Pü.:  daii  'Hand'.  —  ')  Nach  Pü.  'Hand',  was an  sich  passen  würde,  Sp.  44  m.
j.  duye:  s.  dDO:
p.  dmi' :  s.  bei  lA/*.
•  j-i  g".  P-  (dOra-)  Adj.  'fern';  nur  LS. und  Abis,  als  Adv.   i)  LS,  'fem,  fernhin':
äsnaila  zbayantsi  'ratca  Yt.  77.  * ;  ■ — ■  nara . .  ya  nasaum  avaJiUta  'ire  asahi  rasan- hqm  (sd.)  V.Ä'.g?;  YX.i4.^l\  —  Wp^r- sahyü  .  .  ari'tii  'raiy'''  paragmatä  "des Persers  Speer  ist  fernhin  gekommen"  D. ff.  4;  —  mit  Abi:  agibyS  'in  voha  as mand  (sd.)  Y.J4.  8.  a)  |  in  Verbindung mit  apiy  (sd.):  ahyäyä  bümiya  'raiapiy  D. 6.3;  X.I.3  (wo  'raiy  apty): —  mit  Aacä und  Abi.:  pSrs<^  marliytr  *'rayapiy''> hacä  pärsS^  kamaram  paliyajatä  D.  6. 4.  2)  Abis,  'von   fem;  fem;    femhin,
weit  hinweg':  yalca  asnatyagcS  'rai  i/a'itS "die  ihr  von  nah  und  die  ihr  von  fem  (kom- mend) hören  wollt"  Y.  45. 1 ;  —  asnäatca ;asmt?m  'räatca  Vyt-5p;  —  sp^^m  ..-räi ayani^m  Yt.  5.  68;  8.  z,  g.  i  (?),  10.  90, Vyt.  51,  52;  —  andvlm  sSrqm  ..  'rai frasräiqm  "..die  weitberühmte"  Y. 65. 3; Yt  8.i\  —  ySi  *iyeyqnt  'rat  asBS^ä  (sd.) "die  femhin  . ."  Y,  42.  6 ;  —  mit  haca  und AbL:  °ra£  haea  ahmat  nmSnat  ..  *yeyenli "weit  weg  von  , ."  Y.5".  14;  14^.
KompA.  (Vo- '),  •rat;  "fä/.*).  —  Zum  V.  »oto-.
— .  ai.  diitf,  dural  Adv. ;  inp.  (Pü.),  np.  dür.  —
```


## [2026-09-05T20:13:52.653Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /tmp && pdftoppm -f 142 -l 142 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/pg142 && ls -la /tmp/pg142.png",
 "description": "Render PDF page 142"
}
```


### [2026-09-05T20:13:54.636Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 53357 Sep  5 16:13 /tmp/pg142.png
```


## [2026-09-05T20:14:06.363Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/pg142.png"
}
```


### [2026-09-05T20:14:06.699Z] TOOL RESULT

```

```


## [2026-09-05T20:14:06.696Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:14:18.936Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /tmp && pdftoppm -f 142 -l 142 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/pg142hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/pg142hi.png'); print(im.size)\n# crop left region: x 550-950, y 500-2100\nim.crop((550,480,1100,2150)).save('/tmp/pg142_left.png')\n\"",
 "description": "Crop left arrow region"
}
```


### [2026-09-05T20:14:22.181Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-05T20:14:24.146Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/pg142_left.png"
}
```


### [2026-09-05T20:14:24.160Z] TOOL RESULT

```

```


## [2026-09-05T20:15:54.671Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dewmb%CA%B0-",
 "prompt": "Quote verbatim the reconstruction page for PIE *dewmbʰ- : gloss, descendants (Iranian, Germanic, Armenian, Sanskrit), and any note on Pokorny page number."
}
```


## [2026-09-05T20:15:54.885Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/tattoo",
 "prompt": "Quote verbatim both etymologies of tattoo: the military drum signal (from Dutch taptoe) and the skin-marking word (Polynesian)."
}
```


### [2026-09-05T20:15:56.537Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:16:00.826Z] TOOL RESULT

```
# Two Etymologies of "Tattoo"

**Military drum signal (1680s):**
"signal calling soldiers or sailors to quarters at night," from Dutch _taptoe_, combining _tap_ "faucet of a cask" and _toe_ "shut, to."

**Skin-marking (1769):**
"pigment design inlaid under the skin," originating from Polynesian languages including Tahitian and Samoan _tatau_ and Marquesan _tatu_, both meaning "puncture, mark made on skin."

Both meanings entered English at different times, with the military usage predating the body modification sense by nearly a century.
```


## [2026-09-05T20:16:09.915Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AF%D9%86%D8%A8%D9%84/",
 "prompt": "Quote the دنبل entry: the فرهنگ معین section (with any bracketed origin tag) and the لغت‌نامه دهخدا section. Does any give the meaning 'دمل/abscess'?"
}
```


## [2026-09-05T20:16:12.744Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC dumb\"; grep -n -i \"dumbo\\|dumb-\\|duma-\" IEC.txt | head -10; echo \"=== SYN tail\"; grep -n -i \"duma\\|dumb\" SYN.txt | head -10; echo \"=== WLD dumb\"; grep -n -i \"dumb-\\|duma- m\" WLD_band3.txt incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10",
 "description": "Grep Mann, Buck, Walde-Pokorny"
}
```


### [2026-09-05T20:16:12.829Z] TOOL RESULT

```
=== IEC dumb
2577:dumbos, à «thick, plump; mass, lump, tail. WP I, 816 Skt. cf. dumbakah, dim. 'fat-tailed sheep’; Per. dumbe ‘fat on tail of sheep’; Alb. dumé, adj. ‘plump’; OHG zumpfo; MHG zumph(e) ‘penis’; LG tümp ‘pack, crowd'; E tump “hil- lock. Cf. the variants Per. dum ‘tail’; Av.
7124:keunios (kun-) ‘corner, wedge’. Cf. WP I, 33, 398, 465. (Skt. variant: *kounios) Skt. konah, id.; Lat. (*-ü-) cuneus; G Hiene “basket-handie? (?); Srb. Slovene čunj ‘cone, skittle, sley’ beside Slovene čuneti, v. ‘cower’; Cz. cf. činky (‘dumb-bells’. LW in Slovak činy ‘sley; dymb-bells’); Blg. čunka ‘spindle-full of thread’. (A riming form occurs in Srb. tunja, f. ‘wedge’)
7602:kondulos, å ‘knob, lump, bump, gnurl, knot’. (Variants: kundəlos, kondol-, kondəl-). WP I, 390. Cf. kondos Skt. kandalah, à, am (“cheek, jowl’; m. ‘gold nugget’); kandalam (also ‘plantain flower’); Gk. kóndulos "kouckle bone, fist; kondúle “lump, bump’ beside kúndalos ‘peg’; OCS kọ- deli, f., Pol. kadziel ‘distaff; distaff-ful of flax’; R: kude? ‘hemp; distaff-ful’; Slovak kude? & kudla, f. ‘topknot, knot of tow, hair or fibre’; Cz. koudel, id. & kudla; Li. cf. kanduolas ‘kernel’; Latv. kodols, id. beside kodaļa ‘dis- taff-ful’. The background of G Hanteln (LG ?) ‘dumb-bells’ is obscure.
=== SYN tail
914:Lett. dubl’z (pl.), beside Lith. dumblas ‘slime’ in river bottom, etc., prob. (ef. Russ. grjaz’ below) : Lith. dubus ‘deep’, ‘hollow’, dubti ‘sink in’, Lett. dubra ‘swamp’, etc. Walde-P. 1.848. Muhl.- Endz. 1.509.
1975:Sw. dimma : Sw. dial. dimba ‘vapor’, Norw. dial. demba ‘mist’, dumba ‘dust’, Dan. dum ‘dim, dull’, OF dumb ‘dumb’; also ON dimmr, OE dimm ‘dim’; also, fr. a parallel form of the root, OHG-NHG dampf ‘vapor, steam’, used also for ‘mist’, as sometimes Du. damp, and for- merly NE damp (cf. NED); all fr. *dhembh-, *dhemb-, extensions of *dhem- in Skt. dham- ‘blow’, etc. Walde-P. 1.851 ff. Falk-Torp 165, 135. Hell- quist 148.
3813:Lat. britus ‘heavy, dull, irrational’ (a dialect form related to gravis ‘heavy’), in late Lat. used esp. of dumb animals. So It. bruto, NE brute in brute creation, ete. Hrnout-M. 119. Walde-H. 1.117.
5497:Skt. puccha-, lavigiila- Av. duma-
5531:Av. duma- (NPers. dum ‘tail’) : OHG zumpfo ‘penis’. Walde-P. 1.816.
8183:The common words for ‘deaf’ are not from such a logical source as ‘not hear- ing’, but rather from more general no- tions such as ‘dull’ or ‘mutilated’, as are likewise several of the words for ‘dumb’ or even ‘blind’. ‘Deaf’ and ‘dumb’ were expressed by the same word in Greek, and OHG tumb was sometimes used in both senses.
8184:1. Grk. xw¢és, in Hom. ‘dull, blunt? (xawpdv Bédos ‘blunt missile’) and ‘mute, noiseless’ (xipart xwd ‘with noiseless wave’), later both ‘dumb’ and ‘deaf’ (so still in NT), but NG xougés only ‘deaf’, prob. : xndqv ‘drone’, ChSl. chabiti ‘spoil’, pochabii ‘foolish’, Boh. ochabiti ‘make loose, weak’. Walde-P. 1.348. Boisacq 452.
8190:ON daufr, OF déaf, OHG toub, etc., general Gmc. (in most cases also in the sense of ‘dull, slow’ of mind or body; Goth. only in this sense, daubata hairto ‘dulled heart’, Mk. 8.17): ON deyfa ‘blunt, stupefy’, dofinn ‘dull, drowsy’ (Dan. doven ‘lazy’ 4.92), MHG touben ‘stupefy’, etc., Grk. ridw ‘raise a smoke, stupefy with smoke’, suddds ‘blind’ (4.97), ete., here also Goth. dumbs ‘dumb’, etc., OHG tumb ‘stupid, dumb, deaf’ (4.96), fr. *deu-bh- extension of IE *dheu- in Skt. dhia- ‘shake’, dhtima- ‘va- por, smoke’, Grk. 6iw ‘rush, rage’ and numerous other formations, with a com- mon notion of ‘whirling, rapid, dizzy motion’, applied to various physical and mental phenomena, and including some
8194:TS oF THE BUD AR suet ‘dumb’, and ‘blind’. 6. ChSl. glucht, etc., general Slavic, words £08 a: Falk-Torp 179. outside connections? Berneker 308, 309. rate? Fie kurtinas, Lett. kurls, Briickner 145 (unconvincing). 5, Lith. 1 Jriinit ‘having a mutilated urn”) (of. also Russ. kur-guzyj 7. Skt. badhira- : Ir. bodar (above, 3). eat oF n08e" Uke. kur-nosyj ‘snub- Av. karana- (so NPers. kar ‘deaf’), see tailed’, ‘deaf’ ighort- ob. also Av. karana- ‘deaf’, | above, 5 and Barth., IF 3.169. nosed’), PF tghort-eared’, all with com- Av. asrut-gao8a-, lit. ‘having unhearing Skt. kara of mutilated and presumably | ears’ (cpd. of a- privative with sru- ‘paler ‘out’. Mil. -Fndz. 2.323. | ‘hear’ and gaoga- ‘ear’). Barth. 223. fr. UE Berneker 6 4.96 DUMB ‘ Goth. dumbs, baufs Lith. nebylys, beZadis Grk. a ori ON  dumbr Lett. méms NG oie Dan. stum ChSl. némit Lat. muto, mutolo Sw. stum SCr. nijem Be et OE dumb Boh.  némy s, —imudo ME = dumb Pol. — niemy a mut NE dumb Russ. nemoj it * amlabar, balb Du. stom Skt.  miika- Nir. balbh OHG _ stum (tumb) Av. afravaota- W. mud MHG stum (tump) Br. = mud NHG  stumm
8195:Of the words for ‘dumb’, only a few are from such a logical source as ‘not speaking’. Some are from the general notion of ‘dull’, with the same word or cognates used also: for ‘deaf’ (4.95). The majority are from ‘stammer’ or the lke, most of these being of imitative origin. fn oi xagés, same as for ‘deaf’ ae CoM ‘silent’, but
=== WLD dumb
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:51453:dumb- — duei- 
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:51467:dumb- (-bhl) ,. penis, Schwanz“, vielleicht eigentlich „Stab“. 
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:51469:Av. duma- m. „Schwanz“, np. dum, dumb ( *dumb(h)ma -), ahd. sumpfo 
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:52988:Ablautentgleisung von *dumb- aus in die e-Reihe iibergetreten, sondern
```


### [2026-09-05T20:16:15.881Z] TOOL RESULT

```
# دنبل Meaning: Abscess?

Yes, the **لغت‌نامه دهخدا** section explicitly defines دنبل as an abscess:

> "دمل و برآمدگی کوچکی در جلد که رنگش سرخ و شکلش مخروطی است"

This describes a small pustule on the skin that is reddish and cone-shaped—a clear reference to an abscess.

However, the **فرهنگ معین** section does not provide this meaning. Instead, it defines دنبل as a weight-lifting dumbbell used in physical exercise, describing its types and weights.

So only the historical Dehkhoda dictionary entry includes the abscess meaning; the modern Moein dictionary entry does not.
```


## [2026-09-05T20:16:31.378Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD page\"; grep -n \"dumb- (-bhl)\\|dumb- (-bh\" incoming/WLD/WLD_Bd1_pages.txt | head; python3 -c \"\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nlast=''\nfor i,l in enumerate(t,1):\n    if '[pdf page' in l: last=l.strip()\n    if 'dumb- (-bh' in l: print(i,'| last pdf tag:',last,'|',l.strip()[:80]); break\n\"; echo \"=== ARY latin ctx\"; sed -n '8095,8115p' incoming/ARY/ARY_latin_index_pages.txt",
 "description": "WLD page number and ARY context"
}
```


### [2026-09-05T20:16:33.216Z] TOOL RESULT

```
=== WLD page
76827:dumb- (-bhl)           ,.
76827 | last pdf tag:  | dumb- (-bhl)           ,.
=== ARY latin ctx
DARE ENGLISH) gad!
[pdf page 281]
er fo {Yay
leetlasb
. wa Sed pe tgg} GIL; 22 5s cal
ben
Pra lyre |
‘ZHMPFO DUMA AVESTAN) gle gh
DUBA LATVIAN) (3) ip) DUM, DUMB (PAHLAVI) «5 3h
DUMAG, DIMAG —-«(OSSETIC) zu)
‘REFERENCES bth DUNK, DUW (KURDISH) 52,5
POKORNY ==SO*~*~C~*~<CS*é«i HBALUCHD) gx jh
MACKENZIE: (TAILD 136 DUNB, DUMB, DUNBAG
BUCK.” 209-210 LAM 4AFGHANI) (3-4) git
Ave : 1 ghii ley DHUMBHMA — (SANSKRIT) <3 Suite
(OLD HIGH GERMAN) of git
leetlaay
dtl, DHUMBHMA oly oi! ols! 2 tty LE Sal AT AVA): GbE aby Bete 32-1
1p MT te GUT 32 Sly cal pz oY
Sf) AB Abe paly aed sd Caste (3 oat FAN ph DOCK lS ]y 2,13 Jarl 1
ADOKKA 54S 5sthay! TOCKA 24S gllT YDOK iS
```


## [2026-09-05T20:16:53.607Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]',t)\nfor i in range(1,len(parts),2):\n    if parts[i]=='281':\n        print(parts[i+1][:2500])\nEOF",
 "description": "Aryanpur page 281"
}
```


### [2026-09-05T20:16:55.386Z] TOOL RESULT

```
۱/۸۲ دی دُمب
یادداشت:
چم این واژه در زبان‌های ژرمنی: جرئت کردن, ۱
1
| چواگلیس سرواژی رش بل
اوستایی (/4574): 0۸ رید انا
پهلری (#1ماللهه): 8 ,ات0 نون (لتی) (/712ها): 2۸
اوستی (0895712): 0۹6 ,0۱۸6
کردی (ل(7015): 7۷ ,01286 پسگشت‌ها رده ان اد ۲
بلرچی (الل‌تا8۸): 0 ۸00800
208۸6 ,قلاناه ,8ات0 6 (]آت71۸) انامه شا
اففانی (پشتو) (/4۳0۵/۸۸): ف1 210 علاط
سانسکریت (54(58/7): 01711181181۸ برهان قاطع : ۱ ۸۶
آلمانی کهن (0582/4(7 210 صاه):
یادداشت,
۱ در حاشیه‌ی برهان قاطع : (۸۷۹) آمده است که شاید ریشه‌ی هند و اروپایی این واژه 011118887181۸ باشد.
۲ چم این واژه در آلمانی کهن: آلت مردی.
۳ احتمال دارد که واژه‌ی انگلیسی 00276 (به چم "بخش گرشتین دُم جانور") نیز از همین واجریشه باشد (فریزی
کهن: 001 با آلمانی کهن: 10216۸ ابسلندی کهن: ه0016).
ْ
ّ
ّ
پهلوی (1ماظ۳۸): 2۸/7870 ,0۸3 آلمانی کهن (/۸/ل087 ۲/04 صا0):
اوستی (05587/6): ۰ 013410 ,0181107 ۱۱۱
کردی (008701584): 21 آلمانی ((0870/۸): رانا |
بلرچی (لل)نا/8۸): :2 انگلیسی کهن (8۷01380 صا0): 0۸26۳ ا
سانسکریت (5/977): انگلیسی (ب2ولا8(/0): ,0۸357
1 03۸6 دانمارکی (0(/13): ۳ ,0976
ایسلندی کهن (/۵ 5/0104 صاه): سرئدی (8175015): له نالا
201۸ نروژی (/0/07۷8010: نا
۳
```


## [2026-09-05T20:18:05.169Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o -n \"TAMPON\\|TATTOO\\|\\bTOP\\b\\|\\bTIP\\b\\|\\bTAP\\b\" AHD_watkins1985.txt | sort | uniq -c | head; echo \"--- roots list around dumb\"; grep -o \"dumb-\\.\" AHD_watkins1985.txt | head; echo \"--- RCH donbal\"; grep -n \"دنبل\\|dunbal\" RCH.txt | head -5; echo \"--- SKT tap\"; grep -n \"^Tap\\|Tap, a spout\\|Top, \" SKT.txt | head -5",
 "description": "AHD/Skeat/Richardson checks"
}
```


### [2026-09-05T20:18:05.263Z] TOOL RESULT

```
      1 1068:TAMPON
      2 1068:TAP
      1 1068:TATTOO
      1 1068:TIP
      1 2336:TAMPON
      1 2342:TATTOO
      1 2390:TIP
      1 2396:TOP
--- roots list around dumb
--- RCH donbal
--- SKT tap
19180:Tapestry.  (F.-L.-Gk.)  Acorrupti of  the  old  form  tapisserie.^V.  tapiijerie, tapestry.  —  F.  tapisser,  to  fumiih  with taj^cstry,  —  F.  tapis,  ta]->cilry  hangings  ; Low  L.  tapen'us.^L.  tapttt,  cloth,  hang- ings.—Gk.  TQ»7T-,  stem  of  i^Mffi,  a  carpet, woollen  rag.  Cf.  Pers.  tabastah,  a  fringed carpet
19183:Tapioca  (Brarilian.)  Brazilian  tipioka, the  poisonous  jnice  which  issues  from  the root  of  the  ca.^<>nva  when  pressed  (.Littr^) ; hence  tapioca,  which  is  also  prepared  from the  root  of  the  cassava.
19184:Tapir,  a  quadmped.  (Bratilian.)  Bra- lilian  tapyra,  a  tapir  ^Malm).
```


## [2026-09-05T20:18:08.781Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1068p' AHD_watkins1985.txt | grep -o \"TAMPON[^,;.]*\\|TAP[^,;.]*\\|TATTOO[^,;.]*\\|TIP[^,;.]*\" | head; echo \"===\"; sed -n '2336p;2342p;2390p;2396p' AHD_watkins1985.txt | cut -c1-400",
 "description": "AHD index context for tap/tattoo/tampon"
}
```


### [2026-09-05T20:18:08.844Z] TOOL RESULT

```
TAP
TATTOO!
TAMPON
TAP!
TIP!
TAPE
===
TaaL del-2 TABES ta- TACET tak-1 TACHE dek-? TACHISM deik- TACHYLYTE leu-! TACHYPNEA pneu- TACIT tak-1 Tack! dek-2 TACT tag- TACTICS tag- TACTORECEPTOR tag- TAEL tele- TAENIA ten- TAFFETA temp- TAG! dek-2 TAHSILDAR dher-2 TAIL! dek-2 TAINT teng- Tad (s)teg- TAKE tak-2 TALE del-2 TALENT tela- TALES to- TALION tele- TALISMAN kWel-1 TALK del-2 TALLOW del-4 TAME deme-2 TAMPON tap- TANDEM to- TANG! den
TASTE tag- TATTOO! tap- TAURINE! tauro- TAURINE? tauro- TAUROCHOLIC ACID tauro- Taurus _tauro- TAUTO- to-
TIP! tap-
TOOL taw- TOOTH dent- TOP! tap-
```


## [2026-09-05T20:18:13.704Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"tap-\\.\" AHD_watkins1985.txt | head; grep -o \"tap-\\. [^]]*\\]\" AHD_watkins1985.txt | head -3",
 "description": "Watkins root tap-"
}
```


### [2026-09-05T20:18:13.772Z] TOOL RESULT

```
1068:[tap-. Germanic base of various loosely related deriva- tives; “plug, wad, small compact object, projecting part; to plug, strike lightly.” Variants *tap-, *tapp-, *topp-, *tupp-. 1. Old English teppa, spigot: TAP. 2. Dutch tap, spigot: TATTOO!. 3. Old French tampon, plug: TAMPON. 4. Old French taper, to strike lightly: TAP!. 5. Old Eng- lish top, summit: ToP!. 6. Old English top, a child’s plaything, perhaps a spinning top: ToP?. 7. Old French toup, top, tuft of hair: TOUPEE. 8. Old Norse typpi (> Middle English tip), end: TIP!. 9. Old French tof(fe, tuft: TUFT. 10. Old English téppe, strip of cloth: TAPE.]
tap-. Germanic base of various loosely related deriva- tives; “plug, wad, small compact object, projecting part; to plug, strike lightly.” Variants *tap-, *tapp-, *topp-, *tupp-. 1. Old English teppa, spigot: TAP. 2. Dutch tap, spigot: TATTOO!. 3. Old French tampon, plug: TAMPON. 4. Old French taper, to strike lightly: TAP!. 5. Old Eng- lish top, summit: ToP!. 6. Old English top, a child’s plaything, perhaps a spinning top: ToP?. 7. Old French toup, top, tuft of hair: TOUPEE. 8. Old Norse typpi (> Middle English tip), end: TIP!. 9. Old French tof(fe, tuft: TUFT. 10. Old English téppe, strip of cloth: TAPE.]
```


## [2026-09-05T20:18:31.857Z] TOOL CALL #54: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D8%AF%D9%86%D8%A8\" \"https://en.wiktionary.org/wiki/%D8%AF%D9%85\" \"https://en.wiktionary.org/wiki/%D8%AF%D9%85%D9%84\" \"https://en.wiktionary.org/wiki/%DA%A9%DA%98%D8%AF%D9%85\" \"https://en.wiktionary.org/wiki/%D8%AA%D9%86%D8%A8%DA%A9\" \"https://www.etymonline.com/word/tap\" \"https://www.etymonline.com/word/tattoo\" \"https://abadis.ir/fatofa/%D8%AF%D9%86%D8%A8%D9%84/\"; do python3 tools/fetch_source.py \"$u\" --note \"pdf page 142, root Dumb/Dhumbhma: tail; verification of dom/donb, donbal, domal, kazdom, tonbak, Germanic tap\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-05T20:18:37.084Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/36a6737dc63f8966.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0877deedd98d20e4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fe6cbcfe68dab237.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d104dcb3e693d0ed.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0e7e25105a435c27.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/44cafd39344c7739.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2480969d13d31079.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8b25beb2bbb45b47.txt
```


## [2026-09-05T20:18:40.839Z] TOOL CALL #55: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/pg142.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/142.png && echo ok; sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Copy page png and inspect checker"
}
```


### [2026-09-05T20:18:42.627Z] TOOL RESULT

```
ok
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


## [2026-09-05T20:29:48.148Z] TOOL CALL #56: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build142.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_DUNB   = \"https://en.wiktionary.org/wiki/%D8%AF%D9%86%D8%A8\"\nW_DAM    = \"https://en.wiktionary.org/wiki/%D8%AF%D9%85\"\nW_DOMAL  = \"https://en.wiktionary.org/wiki/%D8%AF%D9%85%D9%84\"\nW_KAZ    = \"https://en.wiktionary.org/wiki/%DA%A9%DA%98%D8%AF%D9%85\"\nW_TONBAK = \"https://en.wiktionary.org/wiki/%D8%AA%D9%86%D8%A8%DA%A9\"\nE_TAP    = \"https://www.etymonline.com/word/tap\"\nE_TATTOO = \"https://www.etymonline.com/word/tattoo\"\nA_DONBAL = \"https://abadis.ir/fatofa/%D8%AF%D9%86%D8%A8%D9%84/\"\n\ndoc = {\n \"pdf_page\": 142,\n \"book_page\": 112,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Dumb, Dhumbhma\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Pokorny's *dumb- (-bh-?) 'penis, tail', orig. perhaps 'rod, stick'; Indo-Iranian *dʰumb(ʰ)ma- > Av. duma-, MP dum/dumb, NP dom/donb\",\n   \"note\": (\n    \"Both halves of the root name are real and both are in Nourai's own sources. Pokorny IEW 227 heads the entry \"\n    \"'dumb- (-bh?) „penis, Schwanz‘, vielleicht eigentlich „Stab‘' and gives under it 'Av. duma- m. „Schwanz‘, \"\n    \"npers. dum, dumb (*dum(b)ma-), ahd. zumpfo „penis‘' plus the Germanic *tippa/*tuppa/*tappan group — i.e. exactly \"\n    \"the shape of this chart. 'Dhumbhma' is not a second root but the Aryan (Indo-Iranian) proto-form *dʰumb(ʰ)ma- \"\n    \"reconstructed by Bartholomae (Altiran. Studien II 101), quoted by Horn no. 573 ('Die arische Grundform muss \"\n    \"*dhumbhma- gelautet haben'), by Mo'in in his footnote to Borhan-e Qate' p. 876, and used as the root headword by \"\n    \"Aryanpur. Walde-Pokorny I 816 writes it *dumb(h)ma-. Two caveats. (1) The material is confined to Iranian, \"\n    \"Germanic, Albanian and a late Sanskrit dumbaka- 'fat-tailed sheep'; Pokorny himself calls the Germanic branch \"\n    \"'offenbar mot populaire mit intensiver Konsonantenschärfung, Nasalierung und Vokalwechsel a:i:u', and Watkins/AHD \"\n    \"prints no *dumb- root at all, so 'Indo-European' is generous: the Indo-Iranian etymon is secure, the PIE status is not. \"\n    \"(2) Nourai's gloss 'tail' is the Iranian half of Pokorny's double gloss 'penis, Schwanz' and is correct for every \"\n    \"Iranian word on the page. STRUCTURAL NOTE: on the printed page (p. 112) the boxes Damâvand (#6), donbak (#7) and \"\n    \"každom (#8) branch off the vertical line that leaves the bottom of the AVESTAN duma box, not off the root line \"\n    \"(the root line runs down the far left and feeds only the Avestan box and the Germanic box). The JSON gives them \"\n    \"parent 0; they should be parent 1. This is an extraction error, not the book's.\"\n   ),\n   \"note_fa\": (\n    \"ریشهٔ نمودار درست است. پوکورنی در صفحهٔ ۲۲۷ مدخلی دارد با عنوان dumb- «نرینه، دم» که شاید در اصل \"\n    \"«چوب، عصا» بوده است، و زیر آن اوستایی duma- «دم»، فارسی نو dum/dumb و واژگان ژرمنی خانوادهٔ tap/top/tip را \"\n    \"می‌آورد؛ یعنی دقیقاً همان ساختار این نمودار. «Dhumbhma» ریشهٔ دومی نیست، بلکه صورت آریایی (هندوایرانی) \"\n    \"*dʰumb(ʰ)ma- است که بارتولومه بازسازی کرده و هرن (شمارهٔ ۵۷۳) و معین در حاشیهٔ برهان قاطع (ص ۸۷۶) و آریان‌پور هم همان را آورده‌اند. \"\n    \"دو نکتهٔ احتیاطی: یکی آنکه گواه‌های این ریشه فقط ایرانی و ژرمنی (و آلبانیایی) است و واتکینز در پیوست ریشه‌های \"\n    \"AHD اصلاً چنین ریشه‌ای ندارد؛ پس برچسب «هندواروپایی» اندکی سخاوتمندانه است، هرچند ریشهٔ هندوایرانی قطعی است. \"\n    \"دوم آنکه در صفحهٔ چاپی، خط عمودی‌ای که به جعبه‌های «دماوند»، «دنبک» و «کژدم» می‌رود از پایین جعبهٔ اوستایی duma درمی‌آید، \"\n    \"نه از خود ریشه؛ پس پدر این سه گره باید ۱ باشد نه ۰ — این خطای خوانش اسکن است، نه خطای کتاب.\"\n   ),\n   \"sources\": [W_DUNB, W_DAM],\n   \"ref_check\": [\n    {\"ref\": \"POK:227\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt line 3250-3251 (form-feed leaf 238 => IEW p. 227, the page number '227' is printed a few lines above): 'dumb- (-bh?) „penis, Schwanz‘, vielleicht eigentlich „Stab‘. / Av. duma- m. „Schwanz‘, npers. dum, dumb (*dum(b)ma-), ahd. zumpfo „penis‘ ... germ. *tuppa- „Zopf‘ in anord. toppr ds., ags. topp m. „Gipfel‘ ... germ. *tappan „Zapfen‘ in ags. tæppa m. (engl. tap), mnd. tappe m., ahd. zapho ... WP. I 816.' The page carries the root box, node 1, node 2, node 9 and node 10 all at once.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 816 (WLD_Bd1_1930 djvu lines 51467-51469; running head 'dumb- — duei-')\", \"stance\": \"supports\",\n     \"note\": \"'dumb- (-bh?) „penis, Schwanz‘, vielleicht eigentlich „Stab‘. Av. duma- m. „Schwanz‘, np. dum, dumb (*dumb(h)ma-), ahd. zumpfo' — Walde-Pokorny writes the Aryan form as *dumb(h)ma-, which is Nourai's second root name 'Dhumbhma'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. dumbos (IEC.txt line 2577)\", \"stance\": \"supports\",\n     \"note\": \"'dumbos, ā “thick, plump; mass, lump, tail”. WP I, 816. Skt. cf. dumbakah, dim. ‘fat-tailed sheep’; Per. dumbe ‘fat on tail of sheep’; Alb. dumë, adj. ‘plump’; OHG zumpfo; MHG zumph(e) ‘penis’ ... Cf. the variants Per. dum ‘tail’; Av. [duma-]' — Mann even has Nourai's donbeh.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 4.19 'tail', SYN.txt lines 5497 and 5531\", \"stance\": \"supports\",\n     \"note\": \"Buck's table of words for 'tail' gives 'Av. duma-' and comments 'Av. duma- (NPers. dum ‘tail’) : OHG zumpfo ‘penis’. Walde-P. 1.816.'\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, IE roots list (AHD_watkins1985.txt); the sequence runs dheub- / dheubh- / dheugh- with no *dumb-\", \"stance\": \"silent\",\n     \"note\": \"Watkins prints no *dumb-/*dhumbh- root; the English words of node 10 are instead gathered under a bracketed entry '[tap-. Germanic base of various loosely related derivatives; “plug, wad, small compact object, projecting part; to plug, strike lightly.” Variants *tap-, *tapp-, *topp-, *tupp-.]' — the brackets are Watkins' mark for a base he does not trace to PIE.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_pages.txt pdf page 281 = printed p. 282, s.v. دُم ، دُنب; Latin index line 8104-8107\", \"stance\": \"supports\",\n     \"note\": \"Aryanpur's entry lists Avestan DUMA, Pahlavi DUM/DUMB, Ossetic DUMAG/DIMAG, Kurdish DUNK/DUW, Baluchi DUNB/DUMB/DUNBAG, Afghan LAM, OHG ZUMPFO, and gives the root form 'DHUMBHMA'; his footnote ۱ reads «در حاشیهٔ برهان قاطع آمده است که شاید ریشهٔ هند و اروپایی این واژه DHUMBHMA باشد» — the exact provenance of Nourai's second root name.\"}\n   ],\n   \"nodes\": []\n  }\n ]\n}\n\nN = doc[\"entries\"][0][\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"duma\", \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Avestan duma- m. 'tail' is a genuine, attested word: Bartholomae, Altiranisches Wörterbuch col. 749, s.v. 'j. duma- m. \"\n  \"„Schwanz‘', citing a Vīdēvdād passage on cutting off an animal's tail ('.. sollen sie ihm auch noch den Schwanz \"\n  \"abschneiden'), and closing 'np. dum, dumb. — Ph[l]. dum'. Formally the Avestan stem continues Indo-Iranian \"\n  \"*dʰumb(ʰ)ma-, in which the cluster -mbm- was simplified to -m- in Avestan (Bartholomae, Altiran. Studien II 101; \"\n  \"Horn no. 573 'Die arische Grundform muss *dhumbhma- gelautet haben'), while the Persian branch kept the -mb-/-nb- \"\n  \"(dumb, dunb) — which is why the chart can put duma above dom/donb. Wiktionary glosses the Avestan word 'penis' rather \"\n  \"than 'tail'; that is Pokorny's double gloss, and Bartholomae's Vīdēvdād citation shows 'tail' is the sense in the text, \"\n  \"so Nourai's gloss is right. The step root → Avestan is exactly Pokorny 227.\"\n ),\n \"derivation_fa\": (\n  \"اوستایی duma- واژه‌ای واقعی و مضبوط است: بارتولومه در فرهنگ ایرانی باستان (ستون ۷۴۹) آن را «duma- مذکر، دم» \"\n  \"می‌آورد با شاهدی از وندیداد دربارهٔ بریدن دم جانور، و در پایان می‌نویسد «فارسی نو dum، dumb؛ پهلوی dum». از نظر آوایی، \"\n  \"ستاک اوستایی دنبالهٔ هندوایرانی *dʰumb(ʰ)ma- است که خوشهٔ همخوان -mbm- در اوستایی به -m- ساده شده (بارتولومه، \"\n  \"پژوهش‌های ایرانی ۲/۱۰۱؛ هرن شمارهٔ ۵۷۳)، در حالی که شاخهٔ پارسی همان -mb-/-nb- را نگاه داشته است. ویکی‌واژه معنای \"\n  \" «نرینه» را برای صورت اوستایی می‌آورد که همان معنای دوگانهٔ پوکورنی است؛ شاهد وندیداد نشان می‌دهد که معنای «دم» درست است. \"\n  \"پس ادعای نورایی درست است.\"\n ),\n \"sources\": [W_DUNB],\n \"ref_check\": [\n  {\"ref\": \"POK:227\", \"status\": \"supports\",\n   \"note\": \"POK_01.txt line 3251: 'Av. duma- m. „Schwanz‘, npers. dum, dumb (*dum(b)ma-)' — the root→Avestan→Persian chain as drawn.\"},\n  {\"ref\": \"HRN:128\", \"status\": \"supports\",\n   \"note\": \"HRN.txt form-feed leaf 149 (printed p. 128, leaf = printed + 21), entry 573: 'dum, dumb, dumbe „Schwanz‘, dumbal. aw. duma- „Schwanz‘; phlv. dum, dumb, dumbak, arm. LW. dmak (= *dumak). kurd. dūw, dunk; šgn. lam; oss. d. dumag, t. dimag; bel. dunbag, dumb, dunb ... Die arische Grundform muss *dhumbhma- gelautet haben (Bartholomae, Studien II, 101).' Horn p. 128 is precisely Nourai's citation and it carries both root names.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 749 (BRT.txt line 13684; column number confirmed by Nyberg's 'Av. (749) duma-')\", \"stance\": \"supports\",\n   \"note\": \"'j. duma- m. „Schwanz‘: ... “.. sollen sie ihm auch noch den Schwanz abschneiden” ... Et. s. § 14, Bthl. Stud. 2. 101, Sütterlin IF. 4. 93; unrichtig GIrPh. I. 266. — np. dum, dumb. — Ph. 1 dum.'\"},\n  {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (Glossary), s.v. dumb (NYB_vol2_glossary.txt line 1372, leaf 79 ≈ printed p. 71)\", \"stance\": \"supports\",\n   \"note\": \"'dumb [dwmbʾ] tail ... — Av. (749) duma-; NP dumb, dunb. Cf. gaz-dum, gaz-dumb.' Nyberg's own cross-reference chain Av. duma- > MP dumb > NP dumb/dunb is the chart's first two arrows.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, s.v. gāw-dumb / gazdum / Gōzihr-dumb (PHD.txt line 380, 2312, 2928)\", \"stance\": \"supports\",\n   \"note\": \"MacKenzie has no free-standing 'dum(b)' headword in the OCR, but the element is everywhere in compounds: 'gāw-dumb [gʾbdwmb | N —dum] horn, trumpet', 'gazdum [gcdwm | N každum] scorpion', 'Gōzihr ... ~ dumb: the descending node of the moon' — all with the Middle Persian shape dumb and the New Persian reflex dum.\"}\n ]\n})\n\nN.append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"dom, donb «دُم ، دُنب»; donbeh «دنبه» (chart also prints دنباله)\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"دُم dom / دُنب donb 'tail' < Middle Persian dumb (Book Pahlavi dwmbʾ, Nyberg p. 71) < Proto-Iranian *dumb-a- \"\n  \"(Wiktionary: 'From Middle Persian dwm(bʾ) (/dum(b)/), from Proto-Iranian *dumáh'), continuing the Indo-Iranian \"\n  \"*dʰumb(ʰ)ma- of the root box. New Persian shows the regular doublet: the cluster -mb- either assimilates to -mm- > -m \"\n  \"(dom) or is dissimilated to -nb- (donb), the same alternation Hübschmann treats in his 'nb ist ursprünglich in' list. \"\n  \"دنبه donbeh 'fat tail of a sheep' is dunb + the New Persian nominal -a(h) (MP -ag), i.e. 'the tail-thing'; Mann's \"\n  \"IE Comparative Dictionary cites it verbatim, 'Per. dumbe “fat on tail of sheep”', and Sanskrit dumbaka- 'the fat-tailed \"\n  \"sheep' shows the same formation. دنباله donbāla, printed in the chart in parentheses, is dunb + -āl + -a, the \"\n  \"abstract 'that which follows behind' (Mo'in: «دنباله: دم. هر چیز مانند دم که در عقب چیزی باشد»), and \"\n  \"Hübschmann lists 'dunb-al „Schwanz‘' in the same paragraph. All three words are correctly placed.\"\n ),\n \"derivation_fa\": (\n  \"«دُم» و «دُنب» از فارسی میانهٔ dumb (پهلوی کتابی dwmbʾ، نیبرگ ص ۷۱) و آن از ایرانی باستان *dumba- است. \"\n  \"در فارسی نو خوشهٔ -mb- دو سرنوشت یافته است: یا همگون شده و به «دم» رسیده، یا ناهمگون شده و «دنب» داده — همان دگرگونی‌ای \"\n  \"که هوبشمان در پژوهش‌های فارسی زیر عنوان «nb در اصل» آورده است. «دنبه» از dunb با پسوند اسمی ٔ-ه (پهلوی -ag) \"\n  \"ساخته شده و مان در فرهنگ تطبیقی خود عیناً «Per. dumbe “fat on tail of sheep”» را زیر همین ریشه می‌آورد؛ سنسکریت \"\n  \"dumbaka- «گوسفند دنبه‌دار» هم همین ساخت را دارد. «دنباله» که در نمودار در کمانک آمده نیز dunb + -ال + ٔ-ه است. \"\n  \"ادعای نورایی درست است.\"\n ),\n \"sources\": [W_DUNB, W_DAM],\n \"ref_check\": [\n  {\"ref\": \"BQT:876\", \"status\": \"supports\",\n   \"note\": \"BQT_v2_pages.txt, form-feed leaf 336 = printed p. 876 (offset printed = leaf + 540, fixed by the دماوند entry falling on leaf 338 = p. 878, Nourai's own next citation). Main text of the «دم» entry: «وضم اول دنب و دنباله را گویند» ('with damma on the first letter it means dunb and donbāla') — which is exactly the chart's 'dom, donb : tail (دنباله)'. Mo'in's footnote 7 to that line reads «اوستا duma- (ذنب)، پهلوی dum … کردی dun, dunb … بلوچی dunb, dumb … dunbag … آریایی آن *dhumbhma- باشد … رک: هوبشمان» (OCR noisy but the Latin forms are legible).\"},\n  {\"ref\": \"BQT:882\", \"status\": \"supports\",\n   \"note\": \"Leaf 342 = printed p. 882 has the دنب group: «دنب … بمعنی دامست که در مقابل سر باشد و بعربی ذنب خوانند», «دنبال – بفتح اول بر وزن چنگال», and the دنبه material running on to leaf 343 = p. 883 («دنبه نهادن», «دنبه دادن»). So BQT:876,882 is a correct pair of citations for dom/donb/donbeh.\"}\n ],\n \"consulted\": [\n  {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 573, p. 128\", \"stance\": \"supports\",\n   \"note\": \"'dum, dumb, dumbe „Schwanz‘ ... phlv. dum, dumb, dumbak' — Horn's headword line already contains dom, donb and donbe(h).\"},\n  {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien, form-feed leaf 266 (≈ printed p. 256, leaf = printed + 10), § 'b) nb ist ursprünglich in'\", \"stance\": \"supports\",\n   \"note\": \"'dum = dunb, dunba, dunb-al „Schwanz‘, bal. LW. dunbag, nb. dumb, dunb, phl. dum, dumb, dumbak Bdh. 61.148 ... arm. dmak (aus *dumak, 5. Jhd.), zd. duma-' — Hübschmann's dunba is donbeh and his dunb-al is donbāl.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann, s.v. dumbos (IEC.txt line 2577)\", \"stance\": \"supports\",\n   \"note\": \"'Per. dumbe ‘fat on tail of sheep’ ... Cf. the variants Per. dum ‘tail’' — both of the node's words, under the same root.\"},\n  {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Fārsi, s.vv. دنبال / دنباله / دنبه (MON_part1.txt lines 63070-63095)\", \"stance\": \"supports\",\n   \"note\": \"«دنبال: دم، ذنب. عقب چیزی»; «دنباله: دم. هر چیز مانند دم که در عقب چیزی باشد»; «دنبه: جزوی از بدن گوسفند که بجای دم در انتهای خلفی تن او آویخته و محتوی چربی است» — Mo'in defines donbeh as the tail itself, i.e. the semantic step is nil.\"}\n ]\n})\n\nN.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"donbal «دُنبَل»; donbalân «دنبلان»\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n  \"The two words do not stand equally firmly. دنبلان donbalān 'sheep's testicles (as food); also the truffle' is beyond \"\n  \"doubt a derivative of دنب dunb: it is the plural-looking -ān formation on the base that also gives donbal/donbe, and it \"\n  \"names precisely the organ of the tail-end — Mo'in: «دنبلان: خایهٔ گوسفند که آن را کباب کنند و خورند», and Asbaghi \"\n  \"records the Arabic plural dumlān borrowed with it. دنبل donbal 'boil, abscess' is a real Persian word — Dehkhodā defines \"\n  \"it «دمل و برآمدگی کوچکی در جلد که رنگش سرخ و شکلش مخروطی است» — and Wiktionary lists donbal among the derived terms \"\n  \"of دنب; but no source I could reach states the semantic step explicitly. The natural route is the concrete one that \"\n  \"donbe already shows: dunb 'tail' > 'fleshy protuberance at the rear' (donbe 'fat tail') > 'any conical protuberance on \"\n  \"the body' > 'boil', with the diminutive/adjectival -al that Hübschmann records in dunb-al. That is coherent but \"\n  \"unattested step by step, so the node is plausible rather than confirmed. Note also that Horn's 'dumbal' in entry 573 \"\n  \"is donbāl 'behind, following', not donbal 'boil'.\"\n ),\n \"derivation_fa\": (\n  \"این دو واژه یکسان استوار نیستند. «دنبلان» بی‌گمان از «دنب» است: معین آن را «خایهٔ گوسفند که آن را کباب کنند و خورند» \"\n  \"معنی کرده و همان اندام ناحیهٔ دم است؛ اسباغی نیز جمع عربی «dumlān» را از همین وام‌واژه می‌داند. «دنبل» به معنی کورک و دمل \"\n  \"واژه‌ای واقعی است (دهخدا: «دمل و برآمدگی کوچکی در جلد که رنگش سرخ و شکلش مخروطی است») و ویکی‌واژه آن را در میان \"\n  \"مشتقات «دنب» می‌آورد؛ اما هیچ مأخذی گام معنایی را صریح نگفته است. راه طبیعی همان است که در «دنبه» دیده می‌شود: \"\n  \"«دم» > «برآمدگی گوشتی پسین» > «هر برآمدگی مخروطی بر تن» > «کورک»، با پسوند -ال که هوبشمان در dunb-al ثبت کرده. \"\n  \"این زنجیره معقول است ولی گام‌به‌گام مستند نیست؛ پس ادعای نورایی با احتیاط پذیرفتنی است.\"\n ),\n \"sources\": [W_DUNB, A_DONBAL],\n \"ref_check\": [\n  {\"ref\": \"FVF:258\", \"status\": \"not_checked\",\n   \"note\": \"FVF = Emam Shushtari, Farhang-e Vāžehā-ye Fārsi dar Zabān-e ʿArabi (Tehran 1347). refs_online.json records local_file: null and no archive.org copy; only the noorlib page viewer (login/browser) has it, so p. 258 could not be opened.\"},\n  {\"ref\": \"MON:1563\", \"status\": \"partial\",\n   \"note\": \"Mo'in's lexicon (MON_part1.txt lines 63083-63090, the دنبـ stretch that on the print pagination falls at vol. 2 ≈ p. 1563) has «دنبلان (امر.) (جان.) خایهٔ گوسفند که آن را کباب کنند و خورند؛ بیضهٔ گوسفند. (گیاه) نوعی قارچ …», exactly Nourai's second gloss, but NO دنبل 'abscess' headword: the run goes دنباله‌دار → دنبک → دنبلان → دنبه. Mo'in's entry دنبل in the modern online text is 'dumbbell' (a European loan), and 'abscess' for دنبل is found only in Dehkhodā. So the reference supports donbalān and only half-supports donbal. Mo'in's own دمل entry sits about two pages earlier, matching Nourai's MON:1561 for node 5.\"}\n ],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"vajehyab/abadis دنبل page (archived)\", \"stance\": \"partial\",\n   \"note\": \"The لغت‌نامهٔ دهخدا section defines دنبل as «دمل و برآمدگی کوچکی در جلد که رنگش سرخ و شکلش مخروطی است»; the فرهنگ معین section gives only the sports 'dumbbell' sense. Confirms the word and the meaning, not the etymology.\"},\n  {\"src\": \"HUB\", \"where\": \"Persische Studien, leaf 266 (≈ p. 256)\", \"stance\": \"partial\",\n   \"note\": \"Hübschmann's list has 'dunb-al „Schwanz‘' — i.e. he knows an -al derivative of dunb, but glosses it 'tail' (= donbāl), not 'abscess'; so he documents the suffix but not the medical sense.\"},\n  {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen p. 124 (PLA_pages.txt leaf 139)\", \"stance\": \"supports\",\n   \"note\": \"'دمل - dumal: „Geschwür, Furunkel‘ pers. دنبل dumbal' and two lines later 'دملان - dumlān: Pl. v[on] dumal' — Asbaghi takes Persian donbal 'boil' as a real word and as the source of the Arabic, which is the strongest external witness for this node.\"},\n  {\"src\": \"RCH\", \"where\": \"Richardson, Persian-Arabic-English Dictionary (grep دنبل / dunbal in RCH.txt)\", \"stance\": \"silent\",\n   \"note\": \"No hit; the OCR of Richardson does not carry the headword in any spelling I tried.\"}\n ]\n})\n\nN.append({\n \"id\": 4, \"lang\": \"Arabic\", \"words\": \"domal\", \"verdict\": \"plausible\",\n \"derivation\": (\n  \"Arabic دُمَّل dummal (pl. دمامیل damāmīl) 'boil, furuncle' is a real classical word. Two accounts compete. \"\n  \"(1) The loan account, which is Nourai's: Asbaghi's Persische Lehnwörter im Arabischen p. 124 lists it flatly as \"\n  \"'دمل dumal „Geschwür, Furunkel‘ pers. دنبل dumbal', with the Arabic plural dumlān taken over as well; Addi Shir's \"\n  \"Kitab al-Alfāẓ al-Fārisiyya al-Muʿarraba likewise carries الدمل as an entry in a book that contains only arabised \"\n  \"Persian words, adding «قلت وهو معرّب عن …» ('I say: it is arabised from …'). Phonetically the loan is trivial: Persian \"\n  \"dunbal/dumbal loses the nasal-plus-stop cluster by assimilation to a geminate, dumbal > dummal, the normal Arabic \"\n  \"treatment of a foreign -mb- (cf. تنبول > تمبول). (2) The native account, which the Arabic lexicographers and Wiktionary \"\n  \"prefer: 'From the root د م ل (d m l). Compare Persian دنبل (donbal, “boil”)' — the triliteral is genuinely productive \"\n  \"in Arabic (دمَل 'to manure, to heal a wound', اندمل 'to heal over', مندمل), so dummal can be read as 'the thing that \"\n  \"closes over'. Since specialists in Persian-Arabic lexical traffic (Asbaghi, Addi Shir) back Nourai and the Arabists \"\n  \"back the native root, the arrow is plausible, not settled.\"\n ),\n \"derivation_fa\": (\n  \"عربی «دُمَّل» (جمع: دمامیل) واژه‌ای کهن است و دربارهٔ خاستگاهش دو رأی هست. یکی همان رأی نورایی: اسباغی در \"\n  \"«وام‌واژه‌های فارسی در عربی» (ص ۱۲۴) صریحاً می‌نویسد «dumal „Geschwür, Furunkel‘ از فارسی دنبل»، و ادی شیر هم «الدمل» را در \"\n  \"کتابی که سراسر ویژهٔ معرّب‌های فارسی است مدخل کرده و می‌افزاید «قلت وهو معرّب عن …». دگرگونی آوایی آسان است: \"\n  \"خوشهٔ فارسی -نب-/-مب- در عربی همگون می‌شود و مشدد می‌گردد (dumbal > dummal)، چنانکه تنبول > تمبول. رأی دوم از آنِ \"\n  \"فرهنگ‌نویسان عرب و ویکی‌واژه است: «از ریشهٔ د م ل؛ سنجیده شود با فارسی دنبل» — و این ریشه در عربی زایاست \"\n  \"(دمَل، اندمل، مندمل «به‌بودیافتن زخم»). چون متخصصان دادوستد واژگانی فارسی–عربی جانب نورایی را می‌گیرند و \"\n  \"عربی‌دانان جانب ریشهٔ بومی را، این پیوند با احتیاط پذیرفتنی است.\"\n ),\n \"sources\": [W_DOMAL],\n \"ref_check\": [\n  {\"ref\": \"FVF:258\", \"status\": \"not_checked\",\n   \"note\": \"Same as node 3: Emam Shushtari's Farhang-e Vāžehā-ye Fārsi dar Zabān-e ʿArabi is not on archive.org and has no local file (refs_online.json: local_file null), so p. 258 — which by the title of the book would indeed be a list of Persian words in Arabic — could not be read.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PLA\", \"where\": \"Asbaghi 1988, p. 124 (PLA_pages.txt leaf 139, printed = leaf − 15)\", \"stance\": \"supports\",\n   \"note\": \"'دمل - dumal: „Geschwür, Furunkel‘ pers. دنبل dumbal' (with footnote); and 'دملان - dumlān: Pl. v. dumal'. Exactly Nourai's arrow, from the standard modern monograph on Persian loans in Arabic.\"},\n  {\"src\": \"AFM\", \"where\": \"Addi Shir, Kitab al-Alfāẓ al-Fārisiyya al-Muʿarraba, s.v. (الدمل) — AFM_pages.txt line 1700, form-feed leaf 67 ≈ printed p. 59\", \"stance\": \"supports\",\n   \"note\": \"«(الدمل) وهو خراج … قلت وهو معرّب عن دمل الذي …» — the Arabic-script OCR mangles the Persian etymon (it prints دمل where the Persian دنبل is expected), but the word is entered at all in a dictionary whose entire subject is arabised Persian, and the formula معرّب عن is Addi Shir's standard 'arabised from Persian' tag.\"},\n  {\"src\": \"KLN\", \"where\": \"Klein, Comprehensive Etymological Dictionary (grep dummal / dumal)\", \"stance\": \"silent\",\n   \"note\": \"No English word derives from this Arabic term, so Klein has no entry; his Semitic notes do not touch د م ل.\"},\n  {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an (grep 'dummal' in FVQ_pages.txt)\", \"stance\": \"silent\",\n   \"note\": \"No hit — the word is not Qur'anic, so Jeffery has nothing on it.\"},\n  {\"src\": \"ARB\", \"where\": \"al-Jawālīqī, al-Muʿarrab (ARB_mo3rb.txt, grep دمل)\", \"stance\": \"silent\",\n   \"note\": \"The hits are all unrelated (دملک, مدملق, دملها in running text); al-Jawālīqī does not list دمّل among the arabised words, which is why the native-root reading remains live.\"}\n ]\n})\n\nN.append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"domal «دُمَل»\", \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"The last step — Arabic dummal back into New Persian as دُمَل domal 'boil, abscess' — is the best-attested link on the \"\n  \"branch, whatever one thinks of node 4. Mo'in's dictionary tags the headword explicitly as an Arabic loan: «دمل [ع.] \"\n  \"(ا.) (پز.) زخمی که روی پوست بدن پدید شود و از آن خونابه و چرک آید», the bracketed [ع.] being Mo'in's mark for Arabic \"\n  \"origin. Phonetically the Arabic geminate is simplified in Persian pronunciation (dummal > domal) and the word is \"\n  \"declined as a plain Persian noun (pl. دمل‌ها, and the Arabic broken plural دمامیل in learned style). If node 4 holds, \"\n  \"this is a classic round trip: Persian donbal → Arabic dummal → Persian domal, the pair donbal/domal surviving side by \"\n  \"side as a doublet, which is itself an argument for the loan account. Nourai's own NOTE ('See “Dus” for another possible \"\n  \"root of domal') points at his root Dus < PIE *dus- 'bad, ill-'; that alternative has no support in any source I \"\n  \"consulted — there is no Persian *dus-mal, and Mo'in's [ع.] tag rules it out — so the Arabic route is the right one.\"\n ),\n \"derivation_fa\": (\n  \"این حلقه استوارترین حلقهٔ این شاخه است: معین خود مدخل را با نشانهٔ [ع.] یعنی عربی می‌آورد: «دمل [ع.] (ا.) (پز.) \"\n  \"زخمی که روی پوست بدن پدید شود و از آن خونابه و چرک آید». در فارسی تشدید عربی ساده شده (dummal > domal) و واژه \"\n  \"مانند اسم فارسی صرف می‌شود. اگر گرهٔ پیشین درست باشد، این نمونهٔ خوبی از رفت‌وبرگشت وام‌واژه است: \"\n  \"فارسی «دنبل» ← عربی «دمّل» ← فارسی «دمل»، و این دو صورت امروز دوگانه (doublet) اند. یادداشت نورایی که ریشهٔ دیگری \"\n  \"(«Dus» از *dus- «بد») را محتمل دانسته، در هیچ مأخذی پشتیبانی نمی‌شود و نشانهٔ [ع.] معین آن را رد می‌کند؛ پس همین راه عربی درست است.\"\n ),\n \"sources\": [W_DOMAL, A_DONBAL],\n \"ref_check\": [\n  {\"ref\": \"MON:1561\", \"status\": \"supports\",\n   \"note\": \"MON_part1.txt line 62990 (the دمـ stretch, two Mo'in pages before the دنبـ stretch of node 3, matching the 1561/1563 pair): «دمل: [ع.] (ا.) (پز.) زخمی که روی پوست بدن پدید شود و از آن خونابه و چرک آید؛ آسه». The [ع.] tag is Mo'in's 'Arabic', i.e. the reference states precisely the arrow Arabic → Persian.\"}\n ],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"abadis دنبل page, فرهنگ معین + لغت‌نامه دهخدا sections (archived)\", \"stance\": \"supports\",\n   \"note\": \"Dehkhodā glosses دنبل by دمل itself — the two forms are treated as one word by Persian lexicography, which is what a doublet looks like.\"},\n  {\"src\": \"PLA\", \"where\": \"Asbaghi p. 124\", \"stance\": \"supports\",\n   \"note\": \"By making the Arabic a Persian loan, Asbaghi implies the modern Persian دمل is the re-imported Arabic shape; the Persian original survives as دنبل.\"},\n  {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol. 2, the دمـ pages (leaves 336-343 = pp. 876-883)\", \"stance\": \"silent\",\n   \"note\": \"Borhan lists دلم («جوششی باشد با خارش», p. 876) but has no دمل headword — unsurprising for a dictionary of Persian words, since دمل is Arabic.\"}\n ]\n})\n\nN.append({\n \"id\": 6, \"lang\": \"Persian\", \"words\": \"Damâvand «دماوند»\", \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"This is the placement modern scholarship endorses, and it is the opposite of the placement on Nourai's own page 97 \"\n  \"(root Dhem), where the same name is drawn from dam 'vapour'. The oldest attested shape of the name has the -nb-/-mb- \"\n  \"cluster: Middle Persian Dumbāwand [dwmbʾwnd] (Nyberg, Glossary p. 71), Parthian dwnbʾwnd in the Šāpur KZ inscription, \"\n  \"Greek Δουμβαουνδ in its Greek version, and دنباوند dunbāvand in the Arabic-Islamic geographers — exactly the dunb 'tail, \"\n  \"rear' of node 2, not the dam 'breath' of the other root. Mo'in's footnote on the very page Nourai cites (BQT p. 878) \"\n  \"sets out Kasravi's analysis: دما/دنب 'behind, rear' + the place-name suffix -vand (from وندن 'to place'), the pair \"\n  \"of نهاوند from نها 'front'. Bartholomae adds a negative confirmation: at Av. dunman- 'cloud, fog' he writes 'Für \"\n  \"falsch halte ich Salemanns Zusammenstellung von dunman- mit np. damāvand, GIrPh. I. 266; vgl. zu duma-' — he rejects \"\n  \"the 'mountain of cloud/vapour' etymology and points the reader to duma- 'tail'. Nourai's gloss 'originally a village \"\n  \"at the mountain tail' is a loose rendering of Kasravi (whose 'rear' is a compass/road orientation, the settlement \"\n  \"behind, not literally a mountain's tail), but the root assignment is right.\"\n ),\n \"derivation_fa\": (\n  \"این جایگاهی است که پژوهش امروزی می‌پذیرد، و درست وارونهٔ صفحهٔ ۹۷ همین کتاب است که «دماوند» را از «دم» به معنی بخار گرفته بود. \"\n  \"کهن‌ترین صورت‌های این نام خوشهٔ -نب-/-مب- دارند: فارسی میانه Dumbāwand (نیبرگ، واژه‌نامه ص ۷۱)، پارتی dwnbʾund در \"\n  \"کتیبهٔ شاپور در کعبهٔ زرتشت، یونانی Δουμβαουνδ، و در مآخذ اسلامی «دنباوند» — یعنی همان «دنب» گرهٔ ۲. معین در حاشیهٔ \"\n  \"همان صفحه‌ای که نورایی ارجاع داده (برهان قاطع ص ۸۷۸) تحقیق کسروی را می‌آورد: «دما/دنب» به معنی پشت و دنبال + پسوند \"\n  \"«وند» (از مصدر وندن = نهادن)، در برابر «نهاوند» از «نها» به معنی پیش. بارتولومه نیز ذیل dunman- «ابر، مه» می‌نویسد \"\n  \"هم‌سنجی زالمان میان این واژه و «دماوند» را نادرست می‌داند و خواننده را به duma- «دم» حواله می‌دهد. پس ادعای نورایی \"\n  \"درست است، هرچند معنایی که داده («آبادی‌ای بر دم کوه») برگردانی آزاد از سخن کسروی است.\"\n ),\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AF%D9%85%D8%A7%D9%88%D9%86%D8%AF\", W_DUNB],\n \"ref_check\": [\n  {\"ref\": \"BQT:878\", \"status\": \"supports\",\n   \"note\": \"BQT_v2_pages.txt leaf 338 = printed p. 878, Mo'in's footnote (lines 20018-20032): «دماوند که در مآخذ اسلامی «دنباوند» آمده بنا به تحقیق مرحوم کسروی … (از مصدر وندن = نهادن) … پس دماوند یعنی شهر یا آبادی با قلعهٔ … شاید نهاوند و دماوند … یکی را نهاوند و آن یکی را دماوند گفته‌اند». The cited page really does derive the name from دنب/دما 'rear', i.e. from this root.\"}\n ],\n \"consulted\": [\n  {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. Dumbāvand (NYB_vol2_glossary.txt line 1373, leaf 79 ≈ printed p. 71) — the entry immediately after 'dumb tail'\", \"stance\": \"supports\",\n   \"note\": \"'Dumbāvand [dwmbʾwnd] Mount Damavand 115. — KZŠPrth l. 24 dwnbʾwntš, Gr. v. Δουμβαουνδ, ibd. l. 26 id., = Prs l. 32 dunbʾwnd, Gr. v. (απο) Τουμβαουντου; Eilers, AOr 22, 1954, 267-374; 24, 1956, 183-224.' The 3rd-century attestations all have -mb-/-nb-, which only the 'tail/rear' word supplies.\"},\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, footnote to 'j. dunman- n. „Nebel, Nebelwolke, Wolke‘' (BRT.txt line 13681)\", \"stance\": \"supports\",\n   \"note\": \"'Für falsch halte ich Salemanns Zusammenstellung von dunman- mit np. damāvand, GIrPh. I. 266; vgl. zu duma-' — Bartholomae rejects the 'cloud/vapour' derivation and refers the name to duma- 'tail'.\"},\n  {\"src\": \"MON\", \"where\": \"Mo'in vol. 5 (Aʿlām) p. 536, the reference Nourai's own NOTE cites\", \"stance\": \"contradicts\",\n   \"note\": \"Not readable in the local copy (MON_part1/part2 are the 2-vol. lexicon abridgement without the Aʿlām volumes), but Nourai reports it as deriving the name from the root 'Dhem' (dam 'vapour'). That is the reading Bartholomae calls false and Kasravi/Mo'in-in-BQT abandon; the Middle Persian and Parthian spellings decide against it.\"}\n ]\n})\n\nN.append({\n \"id\": 7, \"lang\": \"Persian\", \"words\": \"donbak, tonbak «دنبک ، تنبک»\", \"verdict\": \"disputed\",\n \"derivation\": (\n  \"The words are real — دنبک/تنبک/تمبک is the goblet drum — but the derivation from dom 'tail' is a folk etymology \"\n  \"and modern scholarship prefers an imitative origin. Wiktionary derives تنبک 'From Middle Persian twmbkʾ /tumbag/ \"\n  \"“drum”, according to Watkins, of imitative origin', files it under 'Persian onomatopoeias', and compares Old Armenian \"\n  \"թմբուկ (tʿmbuk) and possibly Arabic دَرْبُوكَة darbūka; the sequence tom-bak imitates the two strokes of the \"\n  \"instrument (low tom on the centre, high bak on the rim), and the same syllables reappear in تمبک, دمبک, طبلک. Nyberg's \"\n  \"Pahlavi glossary independently records the Middle Persian drum name tumbak, and does so in a passage where it stands \"\n  \"beside — and therefore apart from — gaž-dumb 'horn'. Nourai's own Persian sources give him no more than a definition: \"\n  \"Borhan-e Qateʿ p. 882 and Mo'in both describe the instrument as «دهلی است دم دراز که از چوب و سفال سازند» ('a \"\n  \"long-tailed drum made of wood or clay'), which is a description of its shape, not a statement of its etymology — and \"\n  \"on the very same Borhan page Mo'in labels the parallel attempt to explain دنبوره/طنبور from دنبهٔ بره as \"\n  \"«وجه اشتقاق عامیانه», 'a folk etymology'. The chart repeats the same kind of guess.\"\n ),\n \"derivation_fa\": (\n  \"خود واژه واقعی است — «دنبک/تنبک/تمبک» همان ساز کوبه‌ای است — امّا گرفتن آن از «دم» ریشه‌شناسی عامیانه است. \"\n  \"ویکی‌واژه آن را از فارسی میانهٔ tumbag «طبل» می‌داند و به پیروی از واتکینز آن را نام‌آوا (onomatopoeia) می‌خواند و با \"\n  \"ارمنی کهن tʿmbuk می‌سنجد؛ دو هجای «tom» و «bak» همان دو ضربهٔ میانه و لبهٔ ساز است. نیبرگ نیز نام پهلوی tumbak را \"\n  \"جداگانه از gaž-dumb «شاخ، کرنای» ثبت کرده است. برهان قاطع (ص ۸۸۲) و معین تنها تعریف می‌کنند «دهلی است دم دراز» \"\n  \"که وصف شکل ساز است نه ریشه‌شناسی؛ و در همان صفحه معین کوشش مشابه برای گرفتن «دنبوره/طنبور» از «دنبهٔ بره» را \"\n  \"صریحاً «وجه اشتقاق عامیانه» می‌نامد. پژوهش امروزی ادعای نورایی را رد می‌کند.\"\n ),\n \"sources\": [W_TONBAK],\n \"ref_check\": [\n  {\"ref\": \"MON:1563\", \"status\": \"partial\",\n   \"note\": \"MON_part1.txt line 63078: «دنبک [= تنبک – تمبک] (ا.) دهلی است دم دراز که از چوب و سفال سازند و بازیگران در زیر بغل گرفته و نوازند». Mo'in gives the word, both variants (donbak = tonbak = tombak) and Nourai's gloss verbatim, but no etymology at all — he does not derive it from دم.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʿ vol. 2, leaf 342 = printed p. 882, s.vv. دنبک and دنبوره\", \"stance\": \"contradicts\",\n   \"note\": \"«دنبک – بضم اول بر وزن اردک، دهلی باشد دم دراز که آن را از چوب و سفال هم سازند» (definition only); and on the same page «دنبوره … طنبور باشد … و اصل این لغت دنبهٔ بره بوده است …» with Mo'in's footnote 8: «وجه اشتقاق عامیانه — رک: تنبور». Mo'in explicitly brands the 'from دنبه' explanation of the neighbouring instrument-name a folk etymology.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg, Glossary s.v. gaž-dumb (NYB_vol2_glossary.txt line 1654, leaf 94 ≈ printed p. 86)\", \"stance\": \"contradicts\",\n   \"note\": \"'gaž-dumb [gʿcdwmbʾ] a musical instrument, the horn 201. — Mentioned together with tumbak and nad as the musical instrument of a marching army' — Middle Persian already has tumbak as a separate drum-word alongside the genuine dumb-compound, so the drum is not a dumb- formation.\"},\n  {\"src\": \"MON\", \"where\": \"Mo'in s.v. تشک/تمبک (MON_part1.txt line 43915)\", \"stance\": \"partial\",\n   \"note\": \"«تشک: [– دنبک – طنبک] (ا.)» — the variant set تشک/دنبک/طنبک with an initial ط spelling is exactly the instability expected of an imitative word, not of an inherited compound of دم.\"}\n ]\n})\n\nN.append({\n \"id\": 8, \"lang\": \"Persian\", \"words\": \"každom «کژدم»\", \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"کژدم každom 'scorpion' is a transparent bahuvrīhi compound whose second member is exactly the dom of node 2. \"\n  \"Middle Persian gazdum [gcdwm] is in MacKenzie ('gazdum [gcdwm | N každum!] scorpion; astr. Scorpio') and in Nyberg, \"\n  \"who spells out the analysis: 'gaz-dum [gcdwm] scorpion. … “Whose tail is stinging”: v. the preceding w. and dumb. But \"\n  \"NP kaj-dum, kaž-dum, gaž-dum “having a crooked tail”'. So both of Nourai's elements are right, but his literal gloss \"\n  \"'stinging tail' renders the Middle Persian first member gaz- (the present stem of gazidan 'to bite, sting'), whereas \"\n  \"the New Persian form he prints, with کژ, has been re-analysed as kaž 'crooked, bent' — Wiktionary: 'From Middle \"\n  \"Persian gazdum. By surface analysis, کژ (kaž, “bent, crooked”) + دم (dom, “tail”)', with the semantic parallel of Old \"\n  \"Armenian kor 'crooked'. The -dum element passes from MP dumb through the same -mb > -m assimilation as dom itself; the \"\n  \"compound is old enough (attested in the Book of Dēnkard passage Nyberg cites) to have kept the shortened -dum.\"\n ),\n \"derivation_fa\": (\n  \"«کژدم» ترکیبی روشن است که جزء دومش همان «دم» گرهٔ ۲ است. صورت فارسی میانه gazdum در فرهنگ کوچک پهلوی مکنزی \"\n  \"(«gazdum … scorpion; astr. Scorpio») و در واژه‌نامهٔ نیبرگ آمده است؛ نیبرگ تحلیل را صریح می‌کند: «آن که دمش می‌گزد»، ولی \"\n  \"می‌افزاید که صورت فارسی نو «کج‌دم، کژدم، گژدم» معنای «دم‌کج» دارد. پس معنای تحت‌اللفظی‌ای که نورایی داده («دم گزنده») \"\n  \"برای جزء پهلوی gaz- (ستاک حال گزیدن) درست است، ولی در صورت فارسی نو با «کژ» به «کج، خمیده» بازتحلیل شده است \"\n  \"(ویکی‌واژه، با قیاس ارمنی کهن kor «کج»). جزء -دم همان dumb پهلوی است که در ترکیب همگون شده است. جایگاه این گره درست است.\"\n ),\n \"sources\": [W_KAZ],\n \"ref_check\": [\n  {\"ref\": \"NYB:82\", \"status\": \"supports\",\n   \"note\": \"The entry is in Nyberg's Glossary but in our scan it falls on form-feed leaf 94 ≈ printed p. 86, four pages after the p. 82 Nourai cites (p. 82 of our copy carries frazand … frēc): either the leaf/page offset of this OCR drifts or Nourai's page is slightly off. The content is exactly his claim: 'gaz-dum [gcdwm] scorpion 76. — Also spelt gzdwm, gzdm. “Whose tail is stinging”: v. the preceding w. and dumb. But NP kaj-dum, kaž-dum, gaž-dum “having a crooked tail”, cf the next w.'\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, s.v. gazdum (PHD.txt line 380 = PHD_mackenzie.txt line 2499)\", \"stance\": \"supports\",\n   \"note\": \"'gazdum [gcdwm | N každum!] scorpion; astr. Scorpio' — with the New Persian reflex každum given by MacKenzie himself, immediately after 'gazidan, gaz- [gc-, gz-ytnʾ | N ~] bite, sting'.\"},\n  {\"src\": \"NYB\", \"where\": \"same entry plus the neighbouring gaž-dumb\", \"stance\": \"supports\",\n   \"note\": \"Nyberg's next entry 'gaž-dumb … “having a curved tail, or end” from the natural shape of an animal's horn: gāž = NP kaj, kaž “crooked, curved”' shows that the -dumb element and the kaž- element are both live Middle Persian compounding material.\"},\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, s.v. duma- col. 749\", \"stance\": \"silent\",\n   \"note\": \"Bartholomae has no Avestan compound of duma- with a 'sting/crooked' first member; the compound is a Middle Persian creation, which is what MacKenzie and Nyberg say.\"}\n ]\n})\n\nN.append({\n \"id\": 9, \"lang\": \"Germanic\", \"words\": \"tappa, tuppa\", \"verdict\": \"disputed\",\n \"derivation\": (\n  \"Pokorny does draw this arrow — IEW 227 s.v. dumb- continues 'germ. *tuppa- „Zopf‘ in anord. toppr ds., ags. topp m. \"\n  \"„Gipfel‘ … germ. *tappan „Zapfen‘ in ags. tæppa m. (engl. tap), mnd. tappe m., ahd. zapho' — so Nourai's citation is \"\n  \"accurate. But Pokorny immediately hedges it: 'Offenbar mot populaire mit intensiver Konsonantenschärfung, \"\n  \"Nasalierung und Vokalwechsel a:i:u', i.e. he treats the Germanic set as an expressive formation whose vowel \"\n  \"alternation a:i:u is not an ablaut series and whose geminates are not a regular reflex of anything. Later authorities \"\n  \"decline the connection outright: Watkins/AHD gathers these words under a BRACKETED entry '[tap-. Germanic base of \"\n  \"various loosely related derivatives; “plug, wad, small compact object, projecting part; to plug, strike lightly.” \"\n  \"Variants *tap-, *tapp-, *topp-, *tupp-.]', the brackets being his mark for a base not traced to PIE; Klein stops at \"\n  \"'Teut. *tappo-'; and Etymonline reports of Old English tæppa < PGmc *tappon that 'Boutkan gives it no IE etymology'. \"\n  \"There is also a gloss problem in the box: *tappan- is indeed 'plug, bung', but *tuppa- is 'tuft, top, summit' (ON \"\n  \"toppr, OE topp), not 'plug'. Verdict: the arrow rests on Pokorny alone and modern Germanic lexicography rejects it.\"\n ),\n \"derivation_fa\": (\n  \"پوکورنی درست همین پیوند را می‌کشد: در صفحهٔ ۲۲۷ ذیل dumb- می‌نویسد «ژرمنی *tuppa- „Zopf‘ در نورسی کهن toppr، \"\n  \"انگلیسی کهن topp … ژرمنی *tappan „Zapfen‘ در انگلیسی کهن tæppa (انگلیسی tap)»؛ پس ارجاع نورایی درست است. امّا خود پوکورنی \"\n  \"بی‌درنگ احتیاط می‌کند: «آشکارا واژه‌ای عامیانه با مشددسازی و خیشومی‌شدن و تغییر واکهٔ a:i:u» — یعنی این شاخه را \"\n  \"ساخته‌ای تقلیدی/عاطفی می‌داند نه پیامد قاعده‌مند ریشه. مرجع‌های متأخرتر یکسره این پیوند را رد کرده‌اند: \"\n  \"واتکینز در پیوست AHD این واژگان را زیر مدخلی در کروشه می‌آورد — «[tap-. پایهٔ ژرمنی…]» — که نشانهٔ اوست برای پایه‌ای که به \"\n  \"هندواروپایی نمی‌رسد؛ کلاین تنها تا «Teut. *tappo-» پیش می‌رود؛ و بوتکان هیچ ریشهٔ هندواروپایی برای آن قائل نیست. \"\n  \"افزون بر این، معنای جعبه دقیق نیست: *tappan- واقعاً «درپوش، میخ‌چوب» است ولی *tuppa- «کاکل، نوک، قله» است نه «درپوش».\"\n ),\n \"sources\": [E_TAP],\n \"ref_check\": [\n  {\"ref\": \"POK:227\", \"status\": \"supports\",\n   \"note\": \"POK_01.txt line 3251, IEW p. 227: '… germ. *tuppa- „Zopf‘ in anord. toppr ds., ags. topp m. „Gipfel‘, mhd. zopf „Zopf, Ende eines Dinges‘, mit bb: mnd. tobbe, tubbe „Zapfen‘ … germ. *tappan „Zapfen‘ in ags. tæppa m. (engl. tap), mnd. tappe m., ahd. zapho, mhd. zapfe m. Offenbar ‚mot populaire‘ mit intensiver Konsonantenschärfung, Nasalierung und Vokalwechsel a:i:u.' Nourai's citation is exact; Pokorny's own reservation is what makes the node disputed.\"}\n ],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. [tap-] (AHD_watkins1985.txt line 1068)\", \"stance\": \"contradicts\",\n   \"note\": \"'[tap-. Germanic base of various loosely related derivatives; “plug, wad, small compact object, projecting part; to plug, strike lightly.” Variants *tap-, *tapp-, *topp-, *tupp-. 1. Old English tæppa, spigot: TAP. 2. Dutch tap, spigot: TATTOO¹. 3. Old French tampon, plug: TAMPON. … 5. Old English top, summit: TOP¹. … 8. Old Norse typpi (> Middle English tip), end: TIP¹ …]' — the brackets mean Watkins does not derive the base from PIE, and he prints no *dumb- root anywhere.\"},\n  {\"src\": \"KLN\", \"where\": \"Klein, s.v. tap, n., faucet, cock (KLN_1971.txt line 241185)\", \"stance\": \"partial\",\n   \"note\": \"'ME. tappe, fr. OE. tæppa, rel. to MDu. tappe, Du. tap, OHG. zapho, MHG. zapfe, G. Zapfen, fr. Teut. *tappo-.' Klein reconstructs the Germanic etymon exactly as the chart writes it, but offers no Indo-European root and no Iranian comparison.\"},\n  {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I 816, s.v. dumb-\", \"stance\": \"supports\",\n   \"note\": \"The earlier Walde-Pokorny entry, on which IEW 227 is based, already groups the Germanic material with Av. duma- — so the connection is the standard early-20th-c. view that Pokorny inherited, not Nourai's invention.\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat (grep 'Tap' in SKT.txt)\", \"stance\": \"silent\",\n   \"note\": \"The OCR of Skeat's concise dictionary yields only tapestry/tapioca/tapir in this stretch; no usable 'tap, a spout' entry, so Skeat could not be brought to bear.\"}\n ]\n})\n\nN.append({\n \"id\": 10, \"lang\": \"English\", \"words\": \"tap, top, tip, tattoo, tampon\", \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Every one of the five English words does come from the Germanic *tapp-/*topp-/*tipp- material of node 9, and the list \"\n  \"is in fact Watkins' own: AHD's bracketed entry tap- yields '1. Old English tæppa, spigot: TAP. 2. Dutch tap, spigot: \"\n  \"TATTOO¹. 3. Old French tampon, plug: TAMPON. … 5. Old English top, summit: TOP¹. … 8. Old Norse typpi (> Middle \"\n  \"English tip), end: TIP¹', i.e. exactly tap, tattoo, tampon, top, tip — so Nourai's bare 'AHD' reference is verifiable \"\n  \"and correct for this box. Routes: tap < OE tæppa 'stopper, spigot'; top < OE topp 'summit, tuft'; tip < ON typpi > ME \"\n  \"tip 'end'; tampon < French tampon, the nasalised variant of Old French tapon 'plug', itself from Frankish *tappo \"\n  \"(Klein); tattoo < Dutch taptoe, literally 'the taps shut', the 17th-c. drum signal at which innkeepers closed the \"\n  \"casks, first in English in the 1680s. One caveat the chart does not make: this is tattoo the drum-beat; the far \"\n  \"commoner English tattoo 'skin marking' (1769) is from Tahitian/Samoan tatau, Marquesan tatu, and has nothing to do \"\n  \"with this root. The node's verdict is about the English ← Germanic step, which is secure; the doubt attaches one \"\n  \"level up, at node 9.\"\n ),\n \"derivation_fa\": (\n  \"هر پنج واژهٔ انگلیسی این جعبه واقعاً از همان مادهٔ ژرمنی گرهٔ ۹ می‌آید، و فهرست دقیقاً همان فهرست واتکینز است: \"\n  \"زیر مدخل [tap-] می‌آورد TAP، TATTOO¹، TAMPON، TOP¹، TIP¹ — پس ارجاع مجمل «AHD» در این جعبه ارزیابی‌پذیر و درست است. \"\n  \"راه‌ها: tap از انگلیسی کهن tæppa «درپوش خم، شیر»؛ top از topp «قله، کاکل»؛ tip از نورسی کهن typpi «نوک»؛ tampon از \"\n  \"فرانسهٔ tampon که گونهٔ خیشومی‌شدهٔ tapon فرانسهٔ کهن و آن از فرانکی *tappo است (کلاین)؛ و tattoo از هلندی taptoe \"\n  \"که تحت‌اللفظ «خم‌ها را ببندید» است، نشانهٔ طبلی که شبانه می‌زدند (از دههٔ ۱۶۸۰ در انگلیسی). یک هشدار که نمودار \"\n  \"نمی‌دهد: این tattoo ی طبل است؛ tattoo ی خالکوبی (۱۷۶۹) از تاهیتیایی/ساموایی tatau است و ربطی به این ریشه ندارد. \"\n  \"حکم این گره دربارهٔ گام ژرمنی ← انگلیسی است که استوار است؛ تردید یک پله بالاتر، در گرهٔ ۹ است.\"\n ),\n \"sources\": [E_TAP, E_TATTOO],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 1068) s.v. [tap-] lists TAP, TATTOO¹, TAMPON, TAP¹, TOP¹, TOP², TOUPEE, TIP¹, TUFT, TAPE — Nourai's five words are the first five of that list, in AHD's own order. The index lines confirm it: 'TAMPON tap-', 'TATTOO¹ tap-', 'TIP¹ tap-', 'TOP¹ tap-'. The reference supports the English box; what it does not support is hanging it under the Persian root (see node 9).\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein, s.vv. tap / top / tip / tampon / tattoo (KLN_1971.txt lines 241185, 249771, 248502, 240873, 241811)\", \"stance\": \"supports\",\n   \"note\": \"tap: 'fr. OE. tæppa … fr. Teut. *tappo-. Cp. the Teut. loan words: F. tapon and its nasalized var. tampon “plug, stopper”, It. zaffo, Sp. tapon … Cp. also tapadera, tapster, tip “end”, and the first element in tattoo “drum-beat”.' tampon: 'F., a nasalized var. of tapon “plug” … fr. Frankish *tappo, which is rel. to OHG. zapfo, OE. tæppa.' tattoo (drum beat): 'Du. taptoe, lit. “closing of the taps”.' tattoo (skin): 'Of Polynesian origin; cp. Tahitian tatau, tatu.' top: 'ME., fr. OE., related to ON. toppr “tuft of hair” … OHG. zopf.' tip: 'ME. tip, tippe … in gradational relationship to OE. tæppa “tap”.' Klein's own cross-references assemble Nourai's five words into one family.\"},\n  {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary\", \"stance\": \"silent\",\n   \"note\": \"Not consulted usefully: the volume split of the local OCR (FSD_vol1..4) puts the T range in material whose OCR is too damaged to quote reliably; Klein and Watkins cover the same ground.\"}\n ]\n})\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-142.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write('\\n')\nprint('written', len(N), 'nodes')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build142.py",
 "description": "Build page-142.json"
}
```


### [2026-09-05T20:29:51.089Z] TOOL RESULT

```
written 10 nodes
```


## [2026-09-05T20:29:55.451Z] TOOL CALL #57: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-142.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 142",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T20:29:57.657Z] TOOL RESULT

```
JSON OK
nodes verified: 10/10
node verdicts: {'confirmed': 6, 'plausible': 2, 'disputed': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 9, 'not_checked': 2, 'partial': 2}
books consulted: {'supports': 18, 'partial': 4, 'silent': 8, 'contradicts': 4} | by book: {'MON': 5, 'NYB': 4, 'BRT': 3, 'PLA': 3, 'KLN': 3, 'PHD': 2, 'HUB': 2, 'BQT': 2, 'HRN': 1, 'IEC': 1, 'RCH': 1, 'AFM': 1, 'FVQ': 1, 'ARB': 1, 'AHD': 1, 'WLD': 1, 'SKT': 1, 'FSD': 1}
```


## [2026-09-05T20:30:18.255Z] AGENT

Done. `data/verification/page-142.json` written; `verify_check.py 142` reports 10/10 nodes, 0 PROBLEM lines.

**Page 142 (book p. 112) — root "Dumb, Dhumbhma" : tail (POK:227). Entry 1 "Dup" is a redirect, skipped.**

Verdicts: root **confirmed**; nodes **6 confirmed, 2 plausible, 2 disputed**.
Ref checks: 9 supports, 2 partial, 2 not_checked. Books consulted: 18 supports, 4 partial, 4 contradicts, 8 silent.

- Root is solid: Pokorny 227 *dumb- (-bh?) "penis, Schwanz", and "Dhumbhma" turns out to be Bartholomae's Aryan *dʰumb(ʰ)ma- (Horn 573, Walde-Pokorny I 816, Mo'in's BQT footnote, Aryanpur's headword) — not a second root. Caveat noted: Watkins/AHD prints no such PIE root.

**disputed**
- #7 دنبک/تنبک donbak, tonbak — not from دم "tail". MP *tumbag* "drum", imitative (Wiktionary/Watkins; Old Armenian tʿmbuk); Nyberg has MP tumbak separate from the dumb- compounds; BQT p.882 gives only a shape-description and on that same page Mo'in labels the parallel دنبوره < دنبهٔ بره «وجه اشتقاق عامیانه».
- #9 Germanic tappa, tuppa — Pokorny 227 does draw it but calls it a "mot populaire"; Watkins brackets `[tap-. Germanic base…]` (his mark for non-PIE), Klein stops at Teut. *tappo-, Boutkan gives *tappon no IE etymology. Also *tuppa- means "tuft/top", not "plug".

**plausible**
- #3 donbal "abscess" (donbalān is secure; the tail→boil step is unattested), #4 Arabic دمّل (Asbaghi p.124 and Addi Shir make it a Persian loan from دنبل; Wiktionary/Arabists keep the native root د-م-ل).

**Extraction error the owner must fix**: on the printed page the vertical line feeding **Damâvand (#6), donbak (#7) and každom (#8)** leaves the **bottom of the Avestan `duma` box**, not the root line (the root line runs down the far left and feeds only the Avestan box and the Germanic box). The JSON gives all three `parent: 0`; they should be `parent: 1`. Verified on a 400 dpi render; page image saved to `data/verification/sources/refs/ocr/BOOK/142.png`. Everything else (forms, scripts, glosses, refs) matches the page exactly — no transcription_suspect items.

Side note for consistency: #6 Damâvand is **confirmed** here (MP Dumbāwand, Parthian dwnbʾwnd, Greek Δουμβαουνδ; Kasravi via BQT:878; Bartholomae rejects Salemann's dunman- "cloud" derivation) — which is the mirror image of page 127, where the same name under root "Dhem" was marked disputed.
