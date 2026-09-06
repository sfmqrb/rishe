# Verification process log — verify-page-207


## [2026-09-06T14:51:47.251Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 207 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-207.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-207.json. Write /home/sfmqrb/git/rishe/data/verification/page-207.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 207` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T14:51:48.874Z] AGENT

I'll start by reading the instructions file.


## [2026-09-06T14:51:49.620Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T14:51:49.636Z] TOOL RESULT

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


## [2026-09-06T14:51:49.954Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-207.txt"
}
```


### [2026-09-06T14:51:49.969Z] TOOL RESULT

```
1	=== PDF page 207 (book page 177) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gwel 2 : to pierce  (refs POK:470)
4	#1 (parent #0) [Greek] refs=POK:470; KLN:1068 | obelos, obolos : spike, nail, also nail-shaped Greek coins, money ; obelekos : a narrow pointed stone pillar
5	  #2 (parent #1) [Persian] refs=BQT:428 | pŭl «پول» : money
6	  #3 (parent #1) [Arabic] refs=ARK:232; TAD:52 | fals : money, also the scales on fish skin ; flŭs : coins ; eflâs : poverty ; mofles : poor
7	    #4 (parent #3) [Persian] refs=FVA:319; BQT:428; ARK:232 | fals «فَلس» : money, fish scales ; eflâs «افلاس» : poverty, not having money ; mofles «مُفلس» : poor, without money
8	  #5 (parent #1) [Latin] refs=KLN:1068 | obolus : spike, a narrow pointed stone pillar, also a Greek coin
9	    #6 (parent #5) [English] refs=KLN:1068; SKT:354 | Obol : an ancient Greek coin ; obelus : a line-shaped symbol (-) used in marking manuscripts. ; obelisk : a narrow pointed stone pillar
10	--- entry 1 ---
11	ROOT [Indo-European] Gwelbh : womb  (refs POK:473)
12	#1 (parent #0) [Avestan] refs=POK:473; KLN:483 | garewa : womb ; garebuš : young animal
13	  #2 (parent #1) [None] refs=None | 
14	#3 (parent #0) [Greek] refs=POK:473; KLN:483 | delphus : womb ; delphis : a marine mammal, dolphin ; adelphos : born from same womb (brothers) ; philo-adelphos : brotherly love ☞Bhili
15	  #4 (parent #3) [Arabic] refs=TAD:28 | 
16	    #5 (parent #4) [Persian] refs=MON:1552 | dolfîn «دُلفین»
17	  #6 (parent #3) [English] refs=None | dolphin, Philadelphia
18	    #7 (parent #6) [Persian] refs=None | Fîlâdelfîyâ «فیلادلفیا»
19	#8 (parent #0) [Germanic] refs=AHD | kilbur : young animal
20	  #9 (parent #8) [English] refs=None | calf
21	
```


## [2026-09-06T14:51:53.107Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-207.json",
 "description": "Read source JSON page 207"
}
```


### [2026-09-06T14:51:53.148Z] TOOL RESULT

```
{
  "pdf_page": 207,
  "book_page": 177,
  "entries": [
    {
      "root": {
        "name": "Gwel 2",
        "lang": "Indo-European",
        "refs": "POK:470",
        "gloss": "to pierce"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:470; KLN:1068",
          "words": [
            {"translit": "obelos, obolos", "gloss": "spike, nail, also nail-shaped Greek coins, money", "script": null},
            {"translit": "obelekos", "gloss": "a narrow pointed stone pillar", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:428",
          "words": [
            {"translit": "pŭl", "gloss": "money", "script": "پول"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Arabic",
          "refs": "ARK:232; TAD:52",
          "words": [
            {"translit": "fals", "gloss": "money, also the scales on fish skin", "script": null},
            {"translit": "flŭs", "gloss": "coins", "script": null},
            {"translit": "eflâs", "gloss": "poverty", "script": null},
            {"translit": "mofles", "gloss": "poor", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "FVA:319; BQT:428; ARK:232",
          "words": [
            {"translit": "fals", "gloss": "money, fish scales", "script": "فَلس"},
            {"translit": "eflâs", "gloss": "poverty, not having money", "script": "افلاس"},
            {"translit": "mofles", "gloss": "poor, without money", "script": "مُفلس"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Latin",
          "refs": "KLN:1068",
          "words": [
            {"translit": "obolus", "gloss": "spike, a narrow pointed stone pillar, also a Greek coin", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "KLN:1068; SKT:354",
          "words": [
            {"translit": "Obol", "gloss": "an ancient Greek coin", "script": null},
            {"translit": "obelus", "gloss": "a line-shaped symbol (-) used in marking manuscripts.", "script": null},
            {"translit": "obelisk", "gloss": "a narrow pointed stone pillar", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gwelbh",
        "lang": "Indo-European",
        "refs": "POK:473",
        "gloss": "womb"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:473; KLN:483",
          "words": [
            {"translit": "garewa", "gloss": "womb", "script": null},
            {"translit": "garebuš", "gloss": "young animal", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:473; KLN:483",
          "words": [
            {"translit": "delphus", "gloss": "womb", "script": null},
            {"translit": "delphis", "gloss": "a marine mammal, dolphin", "script": null},
            {"translit": "adelphos", "gloss": "born from same womb (brothers)", "script": null},
            {"translit": "philo-adelphos", "gloss": "brotherly love", "script": null, "see": ["Bhili"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Arabic",
          "refs": "TAD:28",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:1552",
          "words": [
            {"translit": "dolfîn", "gloss": null, "script": "دُلفین"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "dolphin, Philadelphia", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "Fîlâdelfîyâ", "gloss": null, "script": "فیلادلفیا"}
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
            {"translit": "kilbur", "gloss": "young animal", "script": null}
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
            {"translit": "calf", "gloss": null, "script": null}
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


## [2026-09-06T14:51:53.563Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-06T14:51:53.620Z] TOOL RESULT

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


## [2026-09-06T14:52:14.621Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','SKT','ARK','TAD','FVA','BQT','MON','AHD','BRT','PHD','HRN','HUB','AFM','PLA','FVQ','LKT','IEC','SYN','WLD','NYB','ARY']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:700] if v else 'MISSING')\n\""
}
```


## [2026-09-06T14:52:15.039Z] TOOL CALL #6: Bash

```json
{
 "command": "head -60 data/verification/page-205.json"
}
```


### [2026-09-06T14:52:16.174Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== ARK {"title": "M.H. Rokn-zadeh Adamiyyat, Arkan-e Sokhan, Sharq 1347/1968", "kind": "catalog", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pag
== FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
```


### [2026-09-06T14:52:16.204Z] TOOL RESULT

```
{
  "pdf_page": 205,
  "book_page": 175,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "entries": [
    {
      "entry": 0,
      "root": "Gwei",
      "verdict": "confirmed",
      "modern_form": "PIE *gʷeyh₃- (Pokorny 'gʷei-3, gʷeiə-, gʷii̯ē-, gʷi̯ō-, gʷī-, frequent, often with -u̯- extended') 'to live'",
      "note": "The root box is right on all three counts. Pokorny's lemma reads 'Root/lemma: gʷei-3 and gʷeiə-: gʷii̯ē-: gʷi̯ō-: gʷī-, frequent, often with -u̯- extended. Meaning: to live', with 'Page(s): 467-469', so Nourai's 'Gwei : to live' with POK:467 reproduces Pokorny's own heading and page; Watkins in the AHD appendix has 'gʷei-. Also gʷeiə-. To live ... [Pok. 3. gʷei- 467]'; Wiktionary reconstructs *gʷeyh₃- 'to live' (alternative *gʷyeh₃-); Cheung, for the Iranian verb, writes '*jaiH2 ... «PIE *gʷeiH₃-, *gʷieH₃-/*gʷih₃- \"to live\" © LIV: 215 f. | Pok.: 467 f.'. What is striking about this chart is how much of it is simply Pokorny's own article rearranged: pages 467-469 contain, in order, Avestan gaya- and gaēθā-/Old Persian gaiθā, Avestan jīti- and jīra-, Old Persian jīva-/Avestan jva-, Greek bios, zōḗ, zōion and hygiḗs, Latin vīvus/vīvō/vīta, and Old English cwicu / OHG queh — that is, every branch of the page except the modern coinages. Klein's article 'quick' (p.1288, Nourai's own citation on node 1) carries the same set in one paragraph. Three things need qualifying rather than correcting: the Avestan citation forms in node 1 ('jîta', 'merezu-jîta' for jīti-, mərəzu-jīti-/-jva-); the gloss 'to exist' given to the noun gaēθā- in node 8; and the presence of two 19th/20th-century neologisms ('mikro-bios' in the Greek box, 'vitamine' in the French box) among inherited words. Everything on the Iranian side — zīwistan/zīwandag → زیستن/زنده/ژیوه, the Arabic round trip زیبق, gayō.marətan- → کیومرث, gaēθanąm → gēhān → گیتی/کیهان/جهان, jīra- → زیرک/آژیر — checks out against Horn, Hübschmann, MacKenzie, Nyberg, Bartholomae, Asbaghi and Moʿin's footnotes on the very Borhān pages Nourai cites.",
      "note_fa": "جعبهٔ ریشه از هر سه جهت درست است: پوکورنی مادّهٔ «gʷei-3 و gʷeiə-…» را با معنای «زیستن» در صفحات ۴۶۷–۴۶۹ آورده، پس هم صورت و هم برچسبِ زبان و هم معنا و هم شمارهٔ صفحه‌ای که نورایی داده دقیق است؛ واتکینز نیز همین را می‌گوید و ویکی‌واژه آن را *gʷeyh₃- بازسازی می‌کند و چونگ در فرهنگِ فعلِ ایرانی ذیل *jaiH₂ همین ریشه را می‌آورد. نکتهٔ چشمگیر این است که بیشترِ نمودار در واقع بازچینشِ همان مقالهٔ پوکورنی است: اوستایی gaya- و gaēθā-، پارسی باستان gaiθā، jīti- و jīra-، jīva-/jva-، یونانی bios و zōḗ و hygiḗs، لاتین vīvus و vīta، و انگلیسی کهن cwicu همه در همان سه صفحه‌اند. سه نکته باید روشن شود، نه اصلاح: صورت‌های اوستاییِ گرهٔ ۱ («jîta» به‌جای jīti-)، معنای نادرستِ «to exist» برای اسمِ gaēθā- در گرهٔ ۸، و حضورِ دو نوواژهٔ سدهٔ نوزدهم و بیستم (mikro-bios و vitamine) در کنارِ واژه‌های موروثی. تمامِ بخشِ ایرانیِ نمودار — از zīwistan تا «زیستن» و «زنده» و «ژیوه»، چرخهٔ «زیبق»، gayō.marətan- تا «کیومرث»، gaēθanąm تا «گیهان/گیتی/کیهان/جهان»، و jīra- تا «زیرک/آژیر» — با هرن، هوبشمان، مکنزی، نیبرگ، بارتولمه، اصباغی و حواشیِ معین بر همان صفحاتِ برهانِ قاطع که نورایی ارجاع داده می‌خواند.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7eyh%E2%82%83-"
      ],
      "ref_check": [
        {
          "ref": "POK:467",
          "status": "supports",
          "note": "POK_full.txt lines 38677-38790: 'Root / lemma: gʷei-3 and gʷeiə-: gʷii̯ē-: gʷi̯ō-: gʷī-, frequent, often with -u̯- extended || Meaning: to live || Material: A. from *gʷei-: Old Indic jīvatu-ḥ \"life\", gaya-ḥ \"house, courtyard\" ... Avestan gaēθā, Old pers. gaiθā \"entity, house and courtyard\" ... References: WP. I 668 ff. ... Page(s): 467-469.' Exactly the root box as drawn."
        }
      ],
      "consulted": [
        {
          "src": "AHD",
          "where": "Watkins 1985, IE roots appendix s.v. gʷei- (AHD_watkins1985.txt line 540)",
          "stance": "supports",
          "note": "'gʷei-. Also gʷeiə-. To live. I. Suffixed zero-grade form *gʷi-wo-, *gʷī-wo- ... [Pok. 3. gʷei- 467.]' — the same root, gloss and Pokorny page."
        },
        {
          "src": "WLD",
          "where": "Walde-Pokorny I 668-669 (WLD_Bd1_pages.txt leaves 676-677, running head 'gʷei(ə)-')",
          "stance": "supports",
          "note": "the source article that Pokorny 467 abridges, with the Germanic and Greek material set out at length ('mhd. verquīnen ... ags. cwīnan ... got. qistjan')."
        },
        {
          "src": "KLN",
          "where": "Klein 1966 p.1288 s.v. quick",
          "stance": "supports",
          "note": "'fr. I.-E. *gwigwos, fr. base *gwei-, \"to live\", whence Goth. *qius ... OI. jivah ... Avestic jvaiti ... OPers. jiva- ... Gk. bios ... zōē ... L. vivus ... vita ... OIr. bith, W. byd, \"world\" ... Cp. also zodiac, zoetic, zoo-.'"
        },
        {
          "src": "CHEUNG",
          "where": "Etymological Dictionary of the Iranian Verb, *jaiH2, p.223",
          "stance": "supports",
          "note": "'«PIE *gʷeiH₃-, *gʷieH₃-/*gʷih₃- \"to live\" © LIV: 215 f. | Pok.: 467 f. *IE COGNATES: Lat. vivo, OCS živǫ, Lith. gyju, Latv. dzīvu \"I live\", Toch. śaw- \"to live\"'."
        },
        {
          "src": "SYN",
          "where": "Buck, Dictionary of Selected Synonyms",
          "stance": "silent",
          "note": "grep of SYN.txt for the root shapes produced no clean hit (the OCR mangles the labiovelar notation); Buck's chapter 4.74 'live' was not located in the text file."
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Avestan / Old Persian",
          "words": "jiva, jîta, jva; merezu-jîta; hu-jyâti",
```


## [2026-09-06T14:52:20.611Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 470\" POK_full.txt | head -20; echo ====; grep -n \"Page(s): 473\" POK_full.txt | head -20"
}
```


### [2026-09-06T14:52:20.677Z] TOOL RESULT

```
Exit code 1
39171:Page(s): 470-471 
(eval):1: === not found
```


## [2026-09-06T14:52:21.832Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gʷelbh\\|gʷelb\\|delphys\\|delphús\\|garəbuš\\|garəwa\" POK_full.txt | head -30"
}
```


### [2026-09-06T14:52:21.880Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T14:52:24.085Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '39120,39180p' POK_full.txt"
}
```


### [2026-09-06T14:52:24.136Z] TOOL RESULT

```
Lithuanian ^e///"prick', unpers. "ache', g/'/t/^ begin to ache ', geluo, ge/uon/s ^st\ng, 
prick', Giltine^ death goddess, death ', galas xx\. "end, death, bottom, stretch, part, slice, 
lump ' and ^e/5"pain' (= Modern High German Qual), Latvian ^a/5"cusp, peak, end, 
region', o'ze'7/" prick'; Old Prussian Akk. gallan, Vok. go/Zsm. "death', gallintwei^ s\ay\ 
ablaut, gu/senn/n Akk. "pain'; 

russ. -Church Slavic ze/ejg, ze/et/" mourn ', Old Czech ze/ef/" bemoan ', Old Church 
Slavic ze/Jaf. "affliction', ablaut. Old Church Slavic za/bi. "pain'. Old Russian za/b 6s., 
russ. za/bi. " pity', dial, "grave, graveyard ', etc.; 

the pure physical meaning " pricking, pointed ' presumably also in Armenian c/i//"twig, 
branch, finger' (from e before f), in alb. ^//s/?/ "finger' (Pedersen KZ. 39, 393, Jokl IF. 36, 
125, whereupon at first from *glen-st-\ Brugmann IF. 11, 286 Anm. had compared pATija^oo 
" touch, feel, grope '), alb. gr. glimp{gjemp, gjembl) "thorn' {*gle-mo-, Jokl aaO. 141); 

but Middle English quille, engl. quiir long feather; weaver's reel, pen made from a feather; 
hollow spine found on some animals (i.e. porcupines) ', Middle High German kil. Modern 
High German Federkiel {^Nhy n/dwindled?), westfal. kwiale^ quill ' have derived because of 
mrhein. KeiTkee\, wedge ' (Middle High German *kJl) probably an /-root, whether not folk 
etymology distortions exit through influence of Middle High German Middle Low German 
/r/7"wedge' and Middle High German /r/e/"ship'. 

2. With the meaning "pain - sorrow - death': 

Armenian keiem^ afflict ' (Meillet Msl. 8, 165); 

Old Irish at-bailF dies ' {ess-^ bain- from *^7-/7-with prefixed object pronoun "if; 
nevertheless barely after Pedersen KG. II 459 as namely "it throws life away ' to £K-paAAco, 
because of the meaning "die' returns also out of Celtic; compare also corn, bar^i deadly, 
esp. an infectious or contagious disease, a plague, pest, pestilence', cymr. aballu{*ad- 
ballu), ba//u'6\e' {*g'?-n-), ad- fe/7/o {*ate-ba/- irom *g"el-) ds.; Note: common lllyrian g"- > b- 



perhaps Latin vallessiV penenT ' (placed as Celtic verb, a present *(g"'a/-/7o ahead; 
different EM2 1129); 

Old High German Old Saxon quelan, guar endure sorrow ', Old English cwelan^AW; 
Old Norse kvelia^ afflict ', Old Saxon quellian. Old High German quellenAs., Old English 
cwellan^s\aY\ Old Norse kvgli. " torment, pain, agony'. Old English c/Va/i/ "killing, violent 
murder'; Old Saxon quala^ agony, torture ', Old High German qua/ads., "violent death'. 
Modern High German 0^5/ (lengthened grade as Lithuanian ge/a, Old Church Slavic za/b); 
Old High German, Old Saxon qua/m' death, devastation ', Old English cwea/m6s., 
Swedish kva/m' abrupt indisposition, minor illness, nausea '; Old English cuvie/c/ "death' 
{g^el-th), cwieldtTd^ eventide (*end of day'). Old High German quiltiwerk^ evening work ', 
Old Norse kveldu. {*g"'el-t6-) "evening'. 

About " aniaut variations ' (probably at best rhyme meaning) s. Siebs KZ. 37, 315, Lewy 
KZ. 40, 420. 

References: WP. I 689 f., Trautmann 83, Vendryes RC 40, 433 ff. 
Page(s): 470-471 

Root / lemma: g''el-2, g^ela- g^le- 

Meaning: to drip, flow; to throw, *boil over 

Note: though after Wackernagel KZ. 67, 159 belong a) and tS) variant verbs. 

Material: a) Old Indie galati^ trickles down, falls down, disappears ', galita-h^ vanishes,
```


## [2026-09-06T14:52:24.889Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 47[0-9]\" POK_full.txt | head; echo ---; grep -n \"Root / lemma: gʷel\" POK_full.txt | head"
}
```


### [2026-09-06T14:52:24.951Z] TOOL RESULT

```
38309:Page(s): 479 
39103:Page(s): 473 
39171:Page(s): 470-471 
39249:Page(s): 471-472 
39288:Page(s): 472-473 
39292:Page(s): 473 
39351:Page(s): 478 
39515:Page(s): 474-476 
39606:Page(s): 476-477 
39640:Page(s): 477-478 
---
```


## [2026-09-06T14:52:31.078Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=39000 && NR<=39120 && (/Root \\/ lemma/ || /Meaning:/ || /References:/ || /Page\\(s\\)/)' POK_full.txt; echo \"=== around 39060-39110\"; sed -n '39040,39110p' POK_full.txt"
}
```


## [2026-09-06T14:52:32.401Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Root / lemma\" POK_full.txt | sed -n '/38[0-9][0-9][0-9]/p' | head -5; echo ---; awk 'NR>=38900 && NR<=39400 && /Root \\/ lemma|Meaning:|Page\\(s\\)/' POK_full.txt"
}
```


### [2026-09-06T14:52:32.922Z] TOOL RESULT

```
References: WP. I 668 ff., Meillet Introduction^ 165, Specht KZ. 62, 11 1, Schwyzer Gr. Gr. 
Page(s): 467-469 
Root / lemma: g^eb^- 
Meaning: womb; young of animal 
References: WP. I 692 f., WH. I 578, Schwyzer Gr. Gr. I 295. 
Page(s): 473 
Root / lemma: g^el-l 
Meaning: to stick; pain, death 
=== around 39060-39110

vita 



Umbro-Sabino 



vita 



Wallon 



veye 



2. with ApiOTH, masc. pioTO(;; 'life, means of living, substance, the world, mankind, etc.'; 
Note: common lllyrian g"- > b-. 



with or. Lithuanian gaivus^a\er{, awal<e, smart, living '; 

verbal derivative: Old Indie y7i/a//i Avestan Jva/'t/ {\.e. jTva/t/) "lives', ap.y/Va" live!' = Latin 
v/vo, Old Church Slavic z/vg' live ' (Inf. z/t/see above), extended Lithuanian gyvenu' live 
'; Old Indie y»7i/a/A pra-jinosi^ be alive, get excited; stimulate, animate, refresh '. 

References: WP. I 668 ff., Meillet Introduction^ 165, Specht KZ. 62, 11 1, Schwyzer Gr. Gr. 
I 298, 300, 330, 5014, 6756, Trautmann 75 f. 
Page(s): 467-469 

Root / lemma: g^eb^- 

Meaning: womb; young of animal 

Material: Old Indie garbha-h, Avestan garawa- "womb, foetus', garabusu. " the young of 

an animal '; Old Indie sa-garbhya-h^ son of the same mother, brother and sister ' (= gr. 

a5£A(p£6(; ds.); 

gr. SsAcpuq, -uoc; f., Doric SsAcpua " womb, uterus' (see below); *5£A(poc; n. ds. as base 
from aSsAcpsoc; (Hom.) "couterinus, brother ' (*a-5£A(p£[a]-6^), next to which Attic a5£A(p6(; 
ds.; SsAcpa^ m. f. "piglet', 5£A(pi(;, hvo(; m. "dolphin', 5oAcp6(; n MHTpa Hes.; Specht (Indo 
Germanic Dekl. 268) reconstructs from gr. a5£Ai(p-r|p a5£A(p6q. AaKU)V£c; (Hes.) an 
originally root *g"el-\ 

the -^s-stem reappears in Old High German kilburu., chilburra\. "mother lamb'. Old 
English cilforlamb6s. (besides of es^stem Old High German kilbira6s. and - with gradation 
o after ostem as 5oA(p6(;, garbha-h- Modern High German Kalb, see above S. 359 under 
*gel-, *ge/d3^-' clench '), which point to purely velar aniaut (as gall. -Latin ga/baan6 Gothic 
A//-A'e/"womb' etc.). 

Different and mutually influencing but similar in sound families lie before: *g"'eto'^-, 
*g"'ereb'^-, and from ge/- extended b^-forms whose stem formation and specific meaning, 
however, in Germanic are presumably assumed by absorption from g"'eb^-^orms. 

References: WP. I 692 f., WH. I 578, Schwyzer Gr. Gr. I 295. 
Page(s): 473 

Root / lemma: g^el-l 

Meaning: to stick; pain, death 

Material: 1. Gr. btKKxQzo, " wasp, hornet', Hes.; [^"'-o'- 1 Nyhan Albanian].
```


### [2026-09-06T14:52:36.065Z] TOOL RESULT

```
38009:Root / lemma: ghlad- 
38031:Root / lemma: gho 
38058:Root / lemma: ghuel- 
38121:Root / lemma: ghuelg- 
38141:Root / lemma: ghuen- 
---
Page(s): 467-469 
Root / lemma: g^eb^- 
Meaning: womb; young of animal 
Page(s): 473 
Root / lemma: g^el-l 
Meaning: to stick; pain, death 
Page(s): 470-471 
Root / lemma: g''el-2, g^ela- g^le- 
Meaning: to drip, flow; to throw, *boil over 
Page(s): 471-472 
Root / lemma: g''el-3, gV- g'^la- 
Meaning: acorn; oak? 
Page(s): 472-473 
Root / lemma: g^em- 
Page(s): 473 
Root / lemma: g''er(a)-4 
Meaning: to raise the voice; praise 
Page(s): 478 
Root / lemma: g''er-1, g^era- 
Meaning: to devour; throat
```


## [2026-09-06T14:52:45.981Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '39108,39125p' POK_full.txt"
}
```


### [2026-09-06T14:52:46.029Z] TOOL RESULT

```
Material: 1. Gr. btKKxQzo, " wasp, hornet', Hes.; [^"'-o'- 1 Nyhan Albanian]. 



gr. psAovri f. "cusp, peak, needle', 6^up£An(; oimoq Horn.; but ^zKoq n. "projectile' probably 
rather to paAAu), s. about the secondary amalgamation with the latter family under 2. g'^e/- 
"trickle down, drip; throw'; opsAoc;, o^oKoq, Arcadian Doric obEkoq " spit, cusp, peak, 
pointed square pillar, obelisk, coin' s. Schwyzer Gr. Gr. I 295; 

Balto Slavic *ge//et/" it stings, hurts ' in: 

Lithuanian ^e///"prick', unpers. "ache', g/'/t/^ begin to ache ', geluo, ge/uon/s ^st\ng, 
prick', Giltine^ death goddess, death ', galas xx\. "end, death, bottom, stretch, part, slice, 
lump ' and ^e/5"pain' (= Modern High German Qual), Latvian ^a/5"cusp, peak, end, 
region', o'ze'7/" prick'; Old Prussian Akk. gallan, Vok. go/Zsm. "death', gallintwei^ s\ay\ 
ablaut, gu/senn/n Akk. "pain';
```


## [2026-09-06T14:52:46.784Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"obelos\\|obelisk\\|obolus\\|obol\\b\" KLN_1966.txt | head -30"
}
```


### [2026-09-06T14:52:46.852Z] TOOL RESULT

```
2554:amphodelite,  n.,  a  variety  of  anorthite  (mineral.) —  Compounded  of  amph-,  and  Gk.  oSeXo?,  a variant  of  6(3eX6<;,  ‘a  spit’  (see  obelus,  obelisk); so  called  in  allusion  to  the  twin  crystals  in  which it  occurs.  For  the  ending  see  subst.  suff.  -ite. amphora,  n.  —  L.,  ‘a  vessel  with  two  handles  or ears,  a  pitcher’,  fr.  Gk.  dpcpopeuc,  of  s.m.,  which is  contracted  fr.  *d[i<pi-<popEui;  (see  haplology), lit.  ‘two-handled’,  fr.  autpl  (see  amphi-)  and (pope’);,  ‘bearer,  carrier’,  fr.  <pepeiv,  ‘to  bear’. See  hear,  ‘to  carry’,  and  cp.  -phore.  Cp.  also ampulla.
4331:ballista,  n.,  an  ancient  military  engine  ( Roman antiq.)  —  L.,  fit.  ‘a  throwing  machine’,  fr.  Gk. piXXeiv,  ‘to  throw’.  See  next  word ballistic,  adj.,  pertaining  to  projectiles.  — Formed with  suff.  -istic  fr.  Gk.  fiaXXetv,  ‘to  throw’, which  stands  in  gradational  relationship  to (JoXfj,  floXoc,  ‘a  throw’,  fisXo?,  ‘bolt,  arrow, dart’,  lit.  ‘something  thrown’,  fr.  I.-E.  base *gwel-,  whence  also  OI.  apa-gurya-,  ‘swinging’, Avestic  ni-yra-'re,  ‘they  are  being  hurled  down’, Toch.  AB  kla-,  ‘to  fall’,  and  perhaps  also  OI. galati,  ‘trickles’,  OHG.  quellan,  MHG.,  G.  quel- len,  ‘to  well  up’.  Cp.  ball,  ‘party  for  dancing’, ballista,  amphibole,  amphibology,  anabolism, bdemnite,  Belostoma,  bolide,  bolometer,  boule, ‘council’,  catabolism,  devil,  diabolic,  discobolus, Eblis,  ecbolic,  Elaphebolion,  emblem,  embolism, emboly,  hyperbola,  hyperbole,  metabolism,  pa¬ rable,  parabola,  parlance,  parley,  parliament, parlor,  parol,  parole,  periblem,  problem,  scy- balum,  symbol,  Tribolium,  Tribulus. ballistics,  n.,  the  study  of  projectiles.  —  See  prec. word  and  -ics.
11626:discobolus,  n.,  a  discus  thrower.  —  L.,  fr.  Gk. Sicrxo|36Xo;,  ‘a  quoit  thrower’,  fr.  Staxo?,  ‘quoit, discus’,  and  -J36Xo?,  ‘thrower  of’,  which  stands in  gradational  relationship  to  [ixXXsw,  ‘to  throw’. See  disco-  and  ballistic.
25848:obelisk,  n.,  1)  a  rectangular  stone  column,  taper¬ ing  at  the  top  into  a  pyramid ;  2)  an  obelus.  — F.  obdisque,  fr.  L.  obeliscus,  fr.  Gk.  oBe/.in/.oq, ‘a  small  spit,  an  obelisk',  dimin.  of  6(ieX6?,  ‘a spit,  needle,  pointed  pillar,  obelisk’.  See  obelus, obelize,  tr.  v.,  to  mark  with  an  obelus.  —  Gk. opeXl^Eiv,  fr.  'i'.jO.'jc,  ‘obelus’.  See  obelus  and -ize.
25849:obelus,  n.,  a  mark  (—  or  :-)  used  in  manuscripts to  indicate  a  doubtful  passage.  —  Late  L.,  fr. Gk.  6(3eX be,,  ‘a  needle,  spit’,  which  is  of  uncer¬ tain  origin.  Cp.  obelisk,  obol,  amphodelite. Oberon,  n.,  the  king  of  the  fairies  and  husband  of Titania  (medieval  mythol.)  —  F.  Oberon,  fr.  OF. Auberon,  which  is  prob.  borrowed  from  a  Teut. source  rel.  to  E.  oaf,  elf  (qq.  v.) obese,  adj.,  very  fat,  corpulent.  —  L.  obesus,  ‘fat, stout,  plump’,  prop,  ‘that  has  eaten  himself  fat’, pp.  of  obedere,  ‘to  devour’,  fr.  ob-  and  edere,  ‘to eat’.  See  edible.
25909:oboist,  n..  one  who  plays  an  oboe.  —  A  hybrid coined  fr.  oboe  and  -ist,  a  suff.  of  Greek  origin, obol,  n.,  a  small  ancient  Greek  coin  and  weight, 1  / 6  drachma.  —  L.  obolus,  fr.  Gk.  orig.
25911:Obolaria,  n.,  a  genus  of  plants,  the  pennyworth (hot.)  —  ModL.,  fr.  Gk.  ofloXoi;,  ‘a  small  Greek coin’  (see  obol);  so  called  in  allusion  to  the thick  coin-shaped  leaves, obolus,  n.  —  See  obol.
35112:suff.  -an.  The  name  Siberia  derives  fr.  Sibir,  an ancient  Tatar  fortress  at  the  confluence  of  the rivers  Tobol  and  Irtysh.
36387:Derivative:  spore,  intr.  v. sporo-,  before  a  vowel  spor-,  combining  form meaning  ‘spore’.  —  Gk.  orcopo-,  mrrop-,  fr. arropa,  ‘a  sowing,  seed’.  See  prec.  word. Sporobolus,  n.,  a  genus  of  plants,  the  rush  grass (bot.)  —  ModL.,  compounded  of  sporo-  and the  stem  of  Gk.  fiaXXeiv,  ‘to  throw’.  See  ballistic, sporocyst,  n.,  a  cyst  which  contains  sphores.  — Compounded  of  sporo-  and  Gk.  jojotlc;,  ‘blad¬ der,  bag’.  See  cyst.
```


## [2026-09-06T14:53:02.728Z] TOOL CALL #15: Bash

```json
{
 "command": "ls site/pages/207.jpg 2>/dev/null; pdftoppm -f 207 -l 207 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg207 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-06T14:53:03.407Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"پول\" BQT_v1_pages.txt | head -20; echo \"=== v2\"; grep -n \"پول\" BQT_v2_pages.txt | head -20"
}
```


### [2026-09-06T14:53:05.782Z] TOOL RESULT

```
site/pages/207.jpg
total 232
drwx------ 2 sfmqrb sfmqrb  4096 Sep  6 10:53 .
drwx------ 4 sfmqrb sfmqrb  4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   264 Sep  6 10:53 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb 77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb 67371 Sep  6 10:53 pg207.png
```


### [2026-09-06T14:53:05.851Z] TOOL RESULT

```
961:زين ز بان از نظر اشکال کلمات بسپولت تشخیص داده میشود (جمم اسماه :
2306:۳- رهنمای سپولت .
3612:برهان قاطع : تومن با اول بثانی مجپول رسیده و میم مفتوح بنون
3617:و او را مجپول مینویسد » واوخود کجاست که مجپول صفت آن افتد » دیگر
4077:برای سپولت فهم ممانی در کتاب حاضر بدین -
4894:بمعنی خو بش بای مجپول)
7134:بحتانی مجپول و شین قسرشت » آتش پرست را
8225:) غول - نم ثالث وسکون واومجپول
9124:۲ - نهاد از کمین حر که سالار بود عمودش زپولاد آهار بود. اسدی.
9178:ز پولاد سندائی اننر شتاب
9226:آنگاه مرصورت را بوهم ازاو برآهنجد وعجپولی ثابت کندش بی آن صورت . » « زاد المسافرین
10573:بوده از نسل کشتاسب ۴ - و ناپولایتی هم‌هست
11198:ار یس با تحتانی‌مجپول بروزن ائیس:
11529:مجپول بروزن کشورسوز » خانه وسرای پادشاحان
12799:عجپول‌النسب وء‌فقودالیلد را گوند؟ ۰
13145:افوس؟ با واو مجپول بر وزن
13957:| بو سیدن - بانستانی مجپول بروزن
14647:آفو شا با ناك مجپول و شین قطمدار
14761:او به شم اول و سکرن انی مجپول
15156:ا وگ ه جنم اول و سکون ثالی مجپول
=== v2
3326:                            ‫وبا واو مجپول نو‬                     ‫باشد ‪ -‬و عذکیوت را نیز گوند ‪.‬‬
4261:  ‫ومشاور او گردید‪ .‬وی بصدرجهان پیشنهاد کرد که بجای زروسیم رایج بوضم چین‌پول کاغذی چاو را‬
4266:                              ‫صدرجهان گویخانوافتاد وصدرجهان با مشاوره با پولادچینگ س‬
4267:   ‫کردن آن بجای پول طلا ونقره تصمیم کرفت وبرلیفی بتاریخ جمادی‌الاخری سال ‪۳٩۱‬‏ از طرف‬
5031:                   ‫بروغن نرم کرد آهن ز پولا‬                                    ‫یشیرین چند چرییا فرستاد‬
7113:‫بممنی چند استکه مقدار مجپول غير معین‬                       ‫چفندر باشد کهحوبجی است معروف ‪۰‬‬
7391: ‫بر وزن‬     ‫چو لین » با انی مجپول‬
7900: ‫چیلان ‪ -‬با ثالی مجپول بکرویزلنان»‬
9903:   ‫فردوسی‌طوسی ‪۰‬‬           ‫فرو برده مسمارهای گران‪.‬‬              ‫‪ - ۴‬پولاد وخاسكآهنگران‬
11235:‫بر وزن‬     ‫خر غول" "‪ -‬باوأو مجپول‬                 ‫خرشااست که کی ادزامهای آفتاب عالم تاب‬
11635: ‫حرو چ = بائاك مجپول وجیم فارسی»‬                               ‫خلروب‬                       ‫هعروف ‪.‬‬
11671:                                                                       ‫خروسكت ‪ -‬بنالك مجپول ‪ ۰‬صفیر‬
14005:                 ‫همیدون بپول خنیور گذار ‪.‬‬
14773:‫تبالی مجپول بر وزن‬                    ‫خوشاب ‪۴‬‬
14896:‫خول = با انی مجهول بروزن طول »‬                                  ‫حشوید = با انی مجپول بر وزن‬
15111:‫بروزن‌می»عرق‌انسان وحوانات دمگر باعد(‪٩*)۷‬‏‬                               ‫مجپول گ؛یاهی‌است که‌درمیان گندم‌روبد و کندم‬
15112:‫وضم اول وئالی مجپول » خصلت وطبیعت وعادت‬                                  ‫را زبان رساند ‪ -‬وخواهر را نیز گوبند و بعریی‬
15170:‫وقلبه را نگیوزبند وآن چویی اس (‪ )۲‬که کاو‬                       ‫بیلقطة‬       ‫ودال‬   ‫ابجد مفتوح‌برا‬   ‫ودال‬   ‫تحتانیه حپول‬
19892:      ‫نیز کیسه های پولی که درجشن عروسی وباجشن نوروز بمهمانان و مدعوان دهند ‪« .‬ناظم الاطبا» ‪۰‬‬
21736:                                ‫ده ب‬             ‫و تحتانی بواو مجپول رسیده و بای فارسی‬
```


## [2026-09-06T14:53:11.520Z] TOOL CALL #17: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:428 2>&1 | head -60"
}
```


## [2026-09-06T14:53:12.976Z] TOOL CALL #18: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg207.png"
}
```


### [2026-09-06T14:53:14.348Z] TOOL RESULT

```
no scan of BQT covers printed page 428 (see 'scans' in refs_online.json)
```


### [2026-09-06T14:53:14.687Z] TOOL RESULT

```

```


## [2026-09-06T14:53:14.685Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T14:53:26.523Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"فلس\\|فَلس\\|أفلس\\|مفلس\" TAD_pages.txt | head -20; echo \"=== dolfin\"; grep -n \"دلفين\\|دلفين\\|الدلفين\" TAD_pages.txt | head -20"
}
```


### [2026-09-06T14:53:26.588Z] TOOL RESULT

```
1417:                     ‫‪ 32‬عقت باررق سه ورافلسقحدنية‬
1874: ‫ءا املناوقبة وقد بزن فلسين وني زماننا هو جزء من كيلوغرام أي من‬
2024:               ‫فلس وناني ‪ 501020‬وهو نقد بحاسيوناني كان ساوي سدس الدرمم‬
=== dolfin
1133:                                    ‫دلفين ‏ بوناني ‪ 811164‬مرادفه اللاخس‬
```


## [2026-09-06T14:53:27.817Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i,p in enumerate(pages[:3]):\n    print('---',i, p[:300])\nEOF"
}
```


### [2026-09-06T14:53:30.647Z] TOOL RESULT

```
87
--- 0                                      ‫الف‬
           ‫ياكابىاللبناك‬  ‫‪َ8‬‬
                       ‫نببى‬




       ‫لحتل‬
    ‫‪ -‬اا لدم‬  ‫‪1‬‬             ‫تت‬             ‫‪7‬‬   ‫‪:‬‬
     ‫امون‬
‫ظ‬     ‫‪1‬‬



      ‫هني بنشره وتصحيحه وتعليق <واشيه‬
                            ‫ا‬


    
--- 1                     ‫ذكرى الذ ممردص‬
 ‫الى الكير بروحه ونكرة‬        ‫الى من حك العلويغاد على الاادب‬

 ‫وقلبه ؛ الى من حب اطق وشرف الحق ولا نخاف فسيبيل المقلومةلاتم‬
                                  ‫والى الصديق الصادق فىكرم انلساانية‬


                  ‫عابلممل ي بنابت اباظ‬
                   
--- 2                                        ‫‪0‬‬

              ‫بس الآالبارىء المادل اتقامل‬
  ‫ان ميلا الى معرفة الاصل واجتهادا فياستخراج‬
                                           ‫سفى‬
                                             ‫اذىنخلق‬
                                                   ‫لها‬
```


## [2026-09-06T14:53:37.917Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2015,2035p' TAD_pages.txt; echo \"===== DOLPHIN CTX\"; sed -n '1125,1140p' TAD_pages.txt"
}
```


### [2026-09-06T14:53:37.976Z] TOOL RESULT

```
                                         ‫فعك ‪ -‬ترى « فشتك » أ حشوالبارودة‬
                          ‫‪1‬‬                                                   ‫‪1‬‬            ‫ع‬
            ‫بوناتي ثعاه‪ :‬وفى اللاثينة وءوطذم وق الايطالية دعءه؛ وهو‬                ‫ققمة و'همة‬

                                                                                     ‫غجل عزري‬
                                ‫فلانلا ‏ اتكلزي اعقطة!! وهو شعار دقيق من صوف‬

               ‫فلس وناني ‪ 501020‬وهو نقد بحاسيوناني كان ساوي سدس الدرمم‬

           ‫(‪ )1‬اهالى دمشقى اشام يمونيا فستقية لكوتما على شك الفدقة ‪ .‬وقال التباب المجازى‬


                              ‫فحق أن تدعى بفسقية‬          ‫ما‬     ‫تقم‬
                                                                   ‫عىفس‬
                                                                      ‫جس ف‬
                                                                         ‫الب‬
                                  ‫متت‬    ‫اصع‬


===== DOLPHIN CTX
‫ون«تارا »‬
        ‫أي كتبة(منسفروزيرأي كتب ) ون«مطم » أي قضاة دي‬
                        ‫«‪ 6‬از أكيتاب صغيروهو الدقتر المذكور الخ ‪...‬‬
‫اليوناني الذي معناه‬     ‫‪5‬سأمعنداء‪00‬‬
                                  ‫ات انار دذكان ‪ 4‬و‪5‬أي‬                        ‫‪5‬‬

                                               ‫كاسميناء حاوت‬      ‫اتادؤوعاء اغا ‪5‬‬
                                             ‫دلغان (© ‪ -‬عامية فصيحها غضار‬
                                    ‫دلفين ‏ بوناني ‪ 811164‬مرادفه اللاخس‬
‫دلو العفجيرانية «دلي» وهو ا_سممبمدعنلىاة مشتق من دلايداوالعربى‬
‫دمغة ‏ عامي ‪ -‬ترك ( دامغهوطمفه ومنًا» معناهالسمة والوسموالعلامة‬
                 ‫ظ‬                                       ‫والائروالطابعوالروشم ‪...‬‬
 ‫دمقس سس تعربب وماق ة قة اليونانيأي دمشقي” ويراد به نسيج حرو‬
‫أيْضيخاباكل سح ددياى دنقىوينديالبآوعنل ليلذ البزنان انا‬
‫اهودبة للنجارة ‪ 8‬وبديشيق عرش » أي على حربر الفراش الدمشقي (ّ‬
  ‫‪ 6‬وهو التراب الأتلن او تام العلين اليابس اوأنطينامنك الذيلانها لطّدرمل واحدتدمةنة‬
```


## [2026-09-06T14:53:40.035Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# find which page contains the lines\nimport itertools\ntarget1='وهو نقد'\nfor i,p in enumerate(pages):\n    if 'سدس الدرمم' in p or 'سدس الدرهم' in p:\n        print('fals page idx',i)\n    if 'دلفين' in p:\n        print('dolfin page idx',i)\nEOF\ngrep -n \"pdf page\" TAD_pages.txt | head -5"
}
```


### [2026-09-06T14:53:41.659Z] TOOL RESULT

```
dolfin page idx 31
fals page idx 55
```


## [2026-09-06T14:53:53.661Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN fals/follis\"; grep -n -i \"follis\\|fals,\\|obolos\" KLN_1966.txt | head -20; echo \"=== LKT fels/fals\"; grep -n -i \"fals\\|fels\\|follis\" LKT.txt | head -20"
}
```


### [2026-09-06T14:53:53.745Z] TOOL RESULT

```
=== KLN fals/follis
2880:harmful’,  fr.  dv-  (see  priv.  pref.  an-)  and  ocpeXoc, ‘use,  help,  advantage’,  whence  otpcXXeiv  (for ♦otpeXieiv),  ‘to  increase,  enlarge’,  oqjeXpa,  ‘ad¬ vantage’.  "OtpeXo;  prob.  meant  orig.  increase  , and  stands  for  d-tpsXo;,  fr.  pref.  0-  (see  agama) and  *<peXo!;,  which  together  with  OI.  phdlam, ‘gain,  success',  derives  fr.  I.-E.  base  *phel-,  to swell’.  This  base  is  a  collateral  form  of  base *bhel-,  ‘to  swell',  whence  L.follis,  ‘bellows’.  See follicle  and  cp.  Aphelandra,  Aphelinus. anorexia,  n.,  loss  of  appetite  (med.)  —  Medical L.,  formed  fr.  priv.  pref.  -an  and  Gk. ‘appetite’,  from  the  stem  of  opc-yew,  ‘to  stretch oneself,  reach,  reach  after,  long  for,  desire’, which  is  cogn.  with  L.  regere,  ‘to  keep  straight, guide,  lead,  rule’.  See  regent,  adj.,  and  cp. words  there  referred  to.  For  the  ending  see  suff. -ia.
5831:bull,  n.,  the  male  of  a  bovine  animal.  —  ME.  bule, bole,  fr.  OE.  bula,  ‘bull’,  rel.  to  ON.  bolt,  MDu. bul(le),  Du.  bul,  G.  Bulle,  of  s.m.,  OE.  bulluc, ‘little  bull’,  bealluc,  ‘testicle’,  ON.  bollr,  ‘ball’, fr.  I.-E.  base  *bhel-,  ‘to  swell’,  whence  also  Gk. 9«XX'j?,  ‘penis’,  cpxXXaivx,  oocXXt; ,  ‘whale’,  L. follis,  ‘a  pair  of  bellows’.  Cp.  bullock.  Cp.  also baleen,  ball,  ‘a  round  body’,  bold,  bulk,  ‘size’, follicle,  phallus.  For  derivatives  of  base  *bhelgh-, an  enlargement  of  base  *bhel-,  see  belly,  bud¬ get,  bulge.
14335:Derivatives:  fallow,  adj.  and  tr.  v. false,  adj.  —  ME.  fals,  ft.  OF.  fats,  fern,  false
14733:Derivatives :  film,  intr.  and  tr.  v.,  film-ie,  adj., film-y,  adj.,  film-i-ly,  adv.,  film-i-ness,  n. filoselle,  n.,  floss  silk.  —  F.,  fr.  dial.  It.  filosello, ‘cocoon  of  the  silkworm;  floss  silk’,  a  blend  of *folisello,  ‘a  little  bag’,  and  filo,  ‘thread’.  It. *folisello  derives  fr.  VL.  *follicellus,  fr.  L.  folli- culus,  ‘a  little  bag’,  dimin.  of  follis,  ‘a  pair  of bellows;  a  bag’;  see  follicle.  It.  filo  comes  fr. L.  filum,  ‘thread’;  see  file,  ‘a  collection  of papers’.
15106:receive  hospitably,  entertain’.  Cp.  Sp.  alfondega, which  derives  fr.  Arab,  al-,  ‘the’,  and  funduq, ‘inn’,  and  see  pandect.  Cp.  also  fonda,  fondaco. font,  n.,  receptacle  for  baptismal  water —  ME., fr.  OE.  font,  ’baptismal  font’,  fr.  L.  fans,  gen. fontis,  ‘spring,  fountain’,  in  Eccles.  Latin  ‘bap¬ tismal  font’.  See  1st  fount, font,  n.,  set  of  type  of  one  size  ( typogr .)  —  F. fonte,  ‘a  casting’,  prop,  the  fem.  pp.  of  fondre, ‘to  cast,  melt’,  used  as  a  noun.  See  found,  'to cast',  and  cp.  fount,  ‘font’, fontal,  adj.,  1)  pertaining  to  a  fountain;  2)  bap¬ tismal.  —  Late  L.  fantalis,  fr.  L.  fans,  gen.  fon¬ tis,  ‘fountain’.  See  1st  fount  and  adj.  suff.  -al. fontanel,  fontanelle,  n.,  membranous  space  be¬ tween  the  bones  of  the  skull  of  a  baby  or  a young  animal  ( anat .)  —  F.  fontanelle,  trans¬ formation  of  OF.  fontenelle,  fr.  Medical  L.  fon- tanella,  prop,  the  latinized  form  of  the  dimin. of  F.  fontaine,  ‘fountain’.  See  fountain  and dimin.  suff.  -el,  resp.  -elle. food,  n.  —  ME.  fade,  fr.  OE.  fada  (whence OE.  fador,  ‘fodder’),  rel.  to  Goth,  fadeins, ‘food’,  fadjan,  ‘to  feed’,  and  cogn.  with  Gk. TraTsTaff-ai,  ‘to  feed’,  fr,  I.-E.  *pat- ,  * P't-, -/-enlargements  of  base  *pa-,  ‘to  tend,  keep, pasture,  feed,  guard,  protect’,  whence  also  Mes- sapian  roxvo 9,  ‘bread’,  L.  pa-bulum  (for  *pd- dhlo-m),  ‘food,  fodder’,  pa-nis,  ‘bread’,  pa-scere (pp.  pd-stus),  ‘to  graze,  pasture,  feed’,  pa-stor, ‘shepherd’,  lit.  ‘feeder’,  OSlav.  pasp  (for  pa¬ sted),  pasti,  ‘to  feed,  tend  (the  flock)’,  Toch.  A pas-,  B  pdsk-,  ‘to  feed,  tend  (the  flock)’,  Hitt. pahhshi,  ‘I  keep,  tend,  protect’.  Cp.  feed,  fodder, forage,  foster,  fother,  v.  Cp.  also  appanage,  com¬ panion,  company,  impanate,  pabulum,  panda, panetela,  panification,  pannage,  pannier,  pantler, pantry,  pascual,  pastern,  pastille,  pastor,  pasture, repast.  —  Related,  and  equivalent  in  meaning, to  I.-E.  base  *pa-,  is  base  *po-,  *poi-,  *pl-, whence  Ol.  pdti,  ‘he  guards,  protects’,  go-pdh, ‘shepherd’,  payuh,  ‘guarding,  protecting’,  Gk. 7KHp.f]v,  ‘shepherd’,  tc&u,  ‘flock  of  sheep’,  ~oiua, ‘lid,  cover’,  Lith.  piemuo,  ‘shepherd’.  Cp.  the 2nd  element  in  '  ikapala  and  in  satrap.  Cp.  also ban,  ‘governor’,  and  words  there  referred  to. fool,  n.,  a  jester,  a  dupe.  —  ME.  fat,  fr.  OF.  fol (F.  fou,  fol),  ‘foot’,  fr.  L.  follis,  ‘bag,  bellows, ball  filled  with  air’,  in  VL.  ‘empty-headed  per¬ son,  fool’.  See  follicle.  Derivatives:  fool,  intr. and  tr.  v.,  fool-ery,  n ,,faol-ing,  n.,faol-ish,  adj., fool-ish-ly,  adv.,  fool-ish-ness,  n. fool,  n.,  dish  consisting  of  crushed  fruit,  milk  and cream.  —  Fr.  prec.  word  in  its  colloquial  sense ‘a  trick,  a  joke’.  For  sense  development  cp. trifle,  ‘a  thing  of  small  value;  a  sweet  dish’, foolhardy,  adj.,  foolishly  bold;  rash.  —  ME .fol- herdi,  fr.  OF.  fol  hardi.  See  fool,  ‘jester’,  and hardy.
28443:phallus,  n.,  an  image  of  the  male  organ  of  genera¬ tion.  —  L.  phallus,  fr.  Gk.  90 cXXo?,  ‘phallus',  for I.-E.  *bhj-no- ;  rel.  to  cpaXXa iva,  9aXXrj,  ‘whale', and  cogn.  with  L.  follis  (prob.  for  *bhol-nis),  ‘a pair  of  bellows'  (orig.  ‘leather  sack’),  fr.  I.-E. base  *bhel-,  'to  swell',  whence  also  ON.  boll, ‘bull’,  OE.  bulluc,  ‘little  bull’.  See  bull,  ‘male  of the  ox’  and  cp.  words  there  referred  to. Derivatives:  phallic  (q.v.),  phall-ism ,  n.,  phall- ist,  n.
=== LKT fels/fals
71:C.onstancio  Dicc  =  Francisco  Solano  Constancio,  Novo  diccionario  critico  e etymologico  da  lingua  portugueza.  3.  ed.  Paris  1845.  [Trotz  seines  Alters und  vieler  falscher  Etymologien  immer  noch  höchst  werlvoll  für  die  genaue Feststellung  der  Wortbedeutungen.]
373:a)  Vom  Vb.  amara  'befehlen',  also: 'Befehlshaber,  Fürst'.  In  der  vulg.  Form emlr  in  alle  europäischen  Sprachen  als Fremdwort  übergegangen,  bemerke  be- sonders ndl.  emier.  —  Mit  ar-rahl 'Transport',  d.  h.  die  Transportflotte,  die dem  Verkehr  u.  der  Verbindung  zwischen Andalusien  u.  Nordafrika  diente,  wurde amir  verbunden  zu  amlr  ar-rahl,  dem Titel  für  den  Befehlshaber  dieser  Flotte. Hieraus  ergeben  sich  aus  der  Verkür- zung der  Form:  pg.  amiralh,  prov. amiralhs,  atnirat,  afrz.  amiri,  nfrz. amiral  [u.  mit  falscher  etymologischer Beziehung  zu  lat.  admirari]  admiral, rum.  amiral,  it.  ammiraglio  [u.  wie  im
428:[Mit  falsrher  arabisierender  Schreibung 'araha]  'Wagen',  urahagij  'Kutscher, Fuhrmann'.  Hieraus  rum.  araha,  ha- raba  'Leiterwagen',  arabagiü,  harahagiu 'Fuhrmann';  russ.  arbn,  lilruss.  harha, hu\g.  serb.  araba  'Wagen'.  —  ,üie Arabas  werden  von  Ochsen  gezogen und  finden  sich  in  der  ganzen  Berg- landschaft des  Kaukasus  [in  weilen Teilen  Vorderasiens  und  der  Balkan- halbinsel] wieder.  Die  beiden  Räder derselben,  große  plumpe  Holzscheiben, sitzen  fest  an  der  Achse  und  drehen sich  mit  derselben  herum.  Auf  der Achse  ruht,  leicht  und  ohne  anderen Halt  als  den,  welchen  die  oben  liegende Last  des  Wagens  dem  Zapfen  gewährt, das  eigentliche  Gestell.  Mit  diesem höchst  einfachen  Fahrzcufre  wird  durch Dick  und  Dünn,  durch  Täler  und  auf Bergen,  durch  Flüsse  und  durch  Moräste gefahren,  ohne  daß  je  die  Gefahr  des Umwerfens  einträte."  Heinrich  Brugsch, Reise  der  K.  Preußischen  Gesandtschaft nach  Persien  1860  und  1861.  Leip- zig 1862.  I,  51.  [Sain  16.  Gorjajew  5. Mikl  SlEtWb  3.
844:[Sskr.  badara,  vadara].  einer  der  am weitesten  verbreiteten  Charakterbäume Indiens,  Ficus  indica  oder  bens^alensis. Im  Gebiete  von  Birma  bis  zum  Pänd- schäh  heimisch,  findet  er  sich  jetzt  von Queensland  und  China  bis  nach  Marokko und  Guinea  angepflanzt.  Angloind. burr  tree,  engl,  gewöhnlich  banian-tree [von  französischen  Reiseschriftstellern oft  falschlich  bananier  genannt]  nach der  Bezeichnung  der  indischen  Ein- geborenen als  Banianen  [aus  hind. banyä  'Kaufmann,  Händler'].  [Hobson- Johson  77.
898:'Futter  eines  Kleides  oder  eines  Stiefels' [vgl.  hier  Nr.  273  b],  in  Ägypten  mit vulgärer  Vokalisation  butäna  [A.  Nallino, L'arabo  parlato  in  Egitto,  S.  288];  hier- aus siz.  butana  'Rockfutter'.  —  Ferner mit  leichtem  Bedeutungswandel  sp.  pg.
978:[Fehlt  in  Kelekian  Kämüs,  jedoch  bei A.  Hindoglu,  Dictionnaire  Turc-Franqais. Vienne  1838.  S.  135b:  bungiik  'falsche oder  Venezianer  Glasperlen',  also  wohl allgemeiner  'Schmuck'];  hieraus  russ. bulg.  buncuk,  poln.  bunczuk  'der  Tug,  d.  h. Stange  mit  Roßschweif'  [Genaueres  hier- über s.  ZDMG  XI,  547/549],  Adj.  bun- czuczmj  'prunkhaft'.  Karlowicz  423  gibt als  Grundwort  ein  pers.  mängük  'Gold- knauf auf  der  Standarte'  [vielleicht unsere  Nr.  1396  V]  an.
1153:'Schlägel  (im  Ballspiel)'  [Horn  NpEt S.  100,  Nr.  449,  wahrscheinlich  aus präkrta  chaugäna  'vierfach',  dem  Namen für  den  Polospielplatz].  Das  Polo  ge- nannte Spiel  scheint  mediseh-persischen Ursprungs  zu  sein.  Während  es  jetzt nur  noch  in  einigen  Berglandschaften im  Norden  Indiens  erhalten  ist,  wurde es  früher  an  allen  mohammedanischen Höfen  Asiens  gespielt;  viele  Fürsten haben  es  mit  Leidenschaft  gespielt,  z.  B. Kaiser  Akbar  der  Große,  Saladin  u.  a. Vgl.  K.  Inostranzew,  Zur  Geschichte  des Polospieles.  In  Zapiski  Vostocnago  Ot- djelenija  Imp.  russk.  archeologiceskago Obsßestva.  St.  Petersburg.  Bd.  XIV, 4.  Lieferung.  Nach  Byzanz  gelangt,  hieß das  Spiel  mgr.  TluKdviov,  Vb.  tIukovi- Ceiv,  'Spielplatz  dafür'  x^uKaviaTripiov, und  in  Frankreich,  wo  es  zu  Fuß  ge- spielt wurde,  chicane.  Das  frz.  Wort bedeutete  dann,  daß  man  in  einem Kampfe  jeden  möglichen  Vorteil  wahr- nehmen durfte,  und  kam  so  zu  seiner heutigen  Bedeutung  frz.  chicane  'Kniffe, Schabernack,  Rechtsverdrehung,  Spitz- findigkeit', eigentlich  unübersetzbar,  da es  eine  wesentlich  französische  Charak- tereigenschaft bedeutet.  Dtsch.  Schikane, engl,  chicane,  chicanery.  —  Als  Name für  ein  Spiel  kommt  das  Wort  noch vor:  pg.  choca  [Constancio  Dicc  255b, freilich  mit  falscher  Etymologie]  'ein Kinderspiel  mit  Kugeln',  frz.  (Languedoc) chicane  'LochbaU',  mhd.  schaggün.  — [Ältere  Ableitungen  von  frz.  chicoter 'sich  herumzanken'  entweder  aus  lat. ciccum,  KiKKoq  'Apfelkorb,  nichtsnutziges Ding',  also  'Streit  um  eine  Nichtigkeil' oder  sp.  chico  'klein'  sind  unbegründet]. [DE  254.  Devic  DEt  93/94.  Hobson- Jobson  190/193.
1464:581.  Ar.  fals:
1978:'Schwein';  hieraus  vielleicht  siz.  canzirri, ganzirri  'ein  Werkzeug,  um  Steine  und Felsbrocken  auf  den  Rücken  der  Last- tiere zu  heben'  [vgl.  auch  den  Ortsnamen Ganzirri,  ein  See  bei  Messina,  und  das siz.  N.  pr.  Ganzaria].    [GrSVociSic  231.
2110:S74.  Ar.  hubärä: 'Trappe,  Otis',  mit  Imäla  hobera;  hier- aus wegen  der  Farbe  des  Tieres  sp. hobero,  overo  [mit  falscher  Anlehnung an  lat.  ovum  'Ei'],  pg.  fouveiro  'falb', frz.  atMre  'dass.'.  [DE  286.  Devic DEt  45.    Lammens  Rem  29.
2329:'Steuer  oder  Taxe,  die  an  den  Fiskus  zu zahlen  ist';  hieraus  mlat.  cahalla  'Steuer', prov.  sp.  gabela,  pg.  gabella,  frz.  gabelle 'Warensteuer',  it.  gabella  'dass.',  von Neapel  südwärts  und  siz.  'Miet-  und Pachtvertrag'  [z.  B.  der  Verlrag,  durch den  die  Schwefelminen  Siziliens  an  einen Unternehmer  gabelloto  verpachtet  wer- den: gewöhnlich  gegen  20''/o  vom  Werte des  gewonnenen  Schwefels,  vgl.  Globus LXVII,  154],  rum.  havalea  'Abgabe, Arbeitsdienst'  [wohl  durch  Kontamination mit  ar.  Jiawäla  'Auftrag,  Bürgschalt, Wechsel',  s.  auch  Löbel  EITAP  52] ;  russ. kabala  'Schuldbrief,  Verschrei bung,  be- sonders zur  Leibeigenschaft',  klruss.  Ä:«- bala  'Verschreibung  zum  Leibeignen', zakabalyty  'zu  seinem  Untertanen  ma- chen'. Mitar.  Art.  ergibt  sich  sp.  alcabala 'Verkaufsgebühr',  pg.alcai^ala  'Eingangs- steuer'. Aus  dem  It.  wurde  serb.  poln. gabela'ZoU,  Steuer'.  —  [Ableitung  auslat. gabulum  <^  ags.  gafol  vom  Vb.  gifan, wie  Diez  Wb  der  rom.  Spr.  150  vorschlug, ist  abzulehnen,  da  lautlich  fast  unmög- lich.] [DE  GREGORIO  in  StGUtH.  Mikl SlEtWb  107.  Bern  SlEtWb  464.  DE  74 u.  75.  Eguilaz  121.  RomForsch  IV,  589. XXII,  629.    ML  6893.
2421:'Schmaler  Riemen'  [Kelekian  Kämüs 940;  vom  Stamme  kaj  'hart,  fest;  Stein, Fels'  Vämbery  TktEtWb  S.  83,  Nr.  87; vgl.  Cag.  kajrak  'Schleifstein'] ;  hieraus bulg.  serb.  kais  'Riemen'.
2446:1027.  Tk.  kalb: 'Nachgemacht,  falsch'  [K616kian  Kämüs 968  a];  pers.  kälbzän  'Fälscher'  [von  zän, Präsensstamm  zu  zädän  'schlagen',  also 'prägen'  vgl.  hier  Nr.  489 ;  Horn  NpEt S.  1 45,  Nr.  653] ,  ebenso  tk.,  tk.  kalpazanlyk 'Fälschung';  hieraus  rum.  calp  'nichts- nutzig, falsch  [vom  Gelde  gesagt]';  cal- puzan  'Falschmünzer,  Betrüger',  calpu- panie,  calpuzanlic  'Betrügerei,  Falsch- münzerei'; bulg.  halpaw  'nachgemacht, fälsch'
2570:1085.  Pers.  käränfll: 'Gewürznelke'  [wohl  aus  dem  Sskr.], hieraus  mit  volksetymologischer  Um- bildung gr.  KapuöqpuXXov,  aber  mgr. KapoüjaqpouX,  Kapou|U(pi\;  hieraus  it. garofano,  siz.  galofaru  'Nelke',  frz. giroße  'Nelke',  giroflSe  'Levkoje',  prov. kat.  sp.  girofle,  pg.  girofre  'Nelke',  rum. garoufä,  carofil,  garofil;  aus  dem  Frz. wurde  engl,  gilliflower  [mit  Anlehnung an  flotver  'Blume',  ja  sogar  weiter  noch JuUflower  mit  Verkennung  und  ganz falscher  Deutung  des  ersten  Bestand- teiles] 'Nelke'.  Dtsch.  in  der  Aachener Mundart  Groffelsnagel  'Gewürznelke' [wie  ja  die  Nelke  wie  die  Gewürznelke ihren  Namen  'Nägel'  wegen  ihrer  Ge- stalt erhalten  haben,  z.  B.  engl,  clove, it.  chiovo  di  garofano,  frz.  clou  de  girofle, poln.  gwozdzik  von  gwozdz  'Nagel',  ndl. nagelbloem  und  kruidnagel  und  'Ge- tvilrznägelcheri'  im  Deutschen].  Bulg. kalamfir,  karamfil,  serb.  karatnfil.
2867:in  Nordafrika,  mit  dem  Grabe  eines Heiligen,  frz.  irrtümlicli  marabout,  s.  hier Nr.  141U,  genannt]';  hieraus  zum  Teil mit  ar.  Art.  sp.  alcoba,  pg.  alcova  'Schlaf- kabinett', kat.  alcova,  prov.  alcuba  'Zelt', afrz.  aucnbe  'dass.',  frz.  alcdve  'kleines Nebenzimmer',  rum.  alcove;  siz.  cnbba 'Wasserturm',  sp.  alcubilla  'dass.';  mit romanischer  Demin.-Endung  it.  ctipola, frz.  coiipole.  Dtsch.  Alkoven,  Ktqypel, mhd.  ekub  'Zelt'  [bei  WOLFRAM  VON ESCHENBACH],  ndl.  alkoof,  engl,  alcove 'Zimmervvinkei  für  Sitz  oder  Bett'  [m einem  Zimmer  oder  einer  Bibliothek].. Bulg.  kube,  serb.  kube,  kuba  'Kuppel, Gewölbe',  russ.  alkow  'Alkoven';  über vulg.  ar.  kiibbat,  kas.-tat.  kibbet,  kirgis. kibü  wurde  russ.  kibitka  'Verdeck  über einem  russ.  Wagen,  halbverdecktes  russ. Fuhrwerk'.  —  Auf  die  vulg.  Form  ar. kubbäja  'Glas  zum  Trinken'  geht  viel- leicht siz.  ciibbäita  'Art  Mandelkuchen aus  geriebenen  Apfelsinenschalen,  Honig, Karamel!'  usw.  zurück  [wegen  der  zylin- drischen Form;  vielleicht  auch  vom  ar. kubbait  'Mandelkuchen',  vgl.  Dozy  Suppl s.  V.  kubbat].  Als  Eigenname  hat  sich in  Palermo  für  ein  sarazenisches  Gebäude der  Name  La  Ctiba  erhalten  [vgl.  Schack, Poesie  und  Kunst  der  Araber  in  Spanien und  Sizilien.  ^.  II,  266/269].  —  [Mög- licherweise geht  das  ar.  Grundwort  selbst auf  pers.  gunbäd  zurück,  ZDMG  L,  646.] [Kluge  11.  DE  90/91.  95.  Eguilaz  131. Devic  DEt  14.  Lammens  Rem  8.  ML 6909.  Hobson-Jobson  11/12.  Gorjajew 4  und  139.  Bern  SlEtWb  635.  GrS VociSic  232/233.
3101:'Nachlese,  Abfälle,  Wertloses',  mit  Imäla [ä  >  e]  Itilcet ;  hieraus  sp.  luquete  'Stück Zitronen-  oder  Apfelsinenschale,  das  man in  den  Wein  tut,  um  ihm  diesen  Ge- schmack zu  geben'  [Dicc  Gast  1286  a; DE  298].
3178:'Grab,  Friedhof  [aus  ar.  kabr  'Grab' mit  Präfix  des  Ortes  ma-],  plr.  makäbir; hieraus  p^.almocävar  'Friedhof  [DE  168] sowie  sp.  macabro,  frz.  datise  macabre und  mit  falscher  Volksetymologie  miat. Chorea  Machabaeorum  'Totentanz'  [Egui- laz  441  und  Lammens  Rem  149].
3436:1491.  Ar.  luuflis: 'ßankrottierer'  [part.  praes.  act.  vom Vb.  falasa  IV  'bankrott  machen',  dies von  ar.  fals,  plr.  fulüs  'Geldstück' gr.  qpöUic  ZDMG  LI,  300]:  hieraus  rum. mofluz  'dass.',  mofluzi  'bankrott  machen', mo^M2;Zjc 'Bankrott',  vielleicht  auch  bulg. mihljuzni  'Bankrott'.
3537:'Duft,  Geruch',  hieraus  sp.  nafa,  nefa, frz.  naffe,  it.  lanfa;  mit  lat.  aqua  ver- bunden ergab  sich:  it.  acqua  nanfa,  siz. acqua  nanßa,  frz.  m«  de  naffe  'Wasser mit  Apfelsinenduft',  sp.  aguanafa  'Rosen- was.ser'.  [DE  323.  DEFREMERY  in JAs  1863,  I,  93.  Eguilaz  69/70  u.  462. ML  5808.  GrSVociSic  242.
3580:'Aptelsine'  [vielleicht  aus  •s.sVr .ndgarant^a 'Elefantenneigung',  d.  h.  Lieblingsfrucht der  Elefanten,  vgl.  Lassen,  Indische  Alter- tumskunde I,  247];  hieraus  über  das gleichlautende  ar.  Wort  sp.  naranja, pg.  laranja,  kat.  naronja,  rum.  näranfä, it.  arancia  'Apfelsine',  Adj.  rancio 'orangegelb',  [mit  Anlehnung  an  or  mit Bezug  auf  die  goldgelbe  Farbe]  frz. orange;  dtsch.  Orange,  ndl.  oranje, oranjeappel,  -boom,  engl,  orange,  poln. or«»^i;  aus  mlat.  pomarancia  <^  it.  pomo 'Apfel'  und  arancia  wurde  dtsch.  Pome- ranze. [DE  324.  Eguilaz4(;3.  ML  5822. Hobson-Jobson  642/643.  Kluge  332.  349.
```


## [2026-09-06T14:53:54.569Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN pul\"; grep -n -i \"pūl\\|pul\\b\\|pŭl\" HRN.txt | head -20; echo \"=== HUB\"; grep -n -i \"pūl\\|pul \" HUB.txt | head -20"
}
```


### [2026-09-06T14:53:54.637Z] TOOL RESULT

```
=== HRN pul
3096:325. pul^) 'Brücke.
3102:pul.
3116:2j Nie pul gesprochen oder geschrieben (Vullers), das nur
3210:340. puläd 'Stahl'.
3215:bolaf; bei. puläJ , pülat (209) ; arab. fülad, syr. "TPC.
=== HUB
2565:siipul *Milz* (Miller p. 80).
6918:sischen W5rtern nur pul *Briicke' = puhl Gazophyl. p. 296,
7378:u. s. w. ; pul = ptthl *Brucke' = ap. *pr9u' = zd. perefu-
7927:setzt werden konnte, das im Np. zu *8upul werdcn sollte. Damit vgl.
7932:gegangen. Woher aber stammt espul oder^wie^^erklftrt es sich?
```


## [2026-09-06T14:54:01.686Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1460,1480p' LKT.txt"
}
```


### [2026-09-06T14:54:01.747Z] TOOL RESULT

```
579.  Ar.  lälig:
'Lähmung  auf  einer  Seite':  hieraus  mit ar.  Art.  sp.  alferiche,  alferecia  'Epilepsie, Fallsucht  (besonders  bei  Kindern)';  die Bedeutungsänderung  erklärt  DE  115  da- mit, daß  im  Känün  von  AVICENNA  dem Kapitel  über  die  'Konvulsionen  bei  den Kindern  tasannug''  das  von  der  'ein- seitigen Lähmung  fälig''  handelnde  vor- ausgeht; möglicherweise  ist  bei  einer Übersetzung  irrtümhch  der  Titel  des folgenden  Kapitels  weggelassen  worden, so  daß  es  schien,  als  ob  die  Fallsucht im  Kapitel  al  fälig  behandelt  wäre.
580.  Ar.  falläh:
[Vom  Vb.  falaha  'spalten',  nämlich  die Erde,  d.  h.  'ackern,  pflügen';  wohl  ein uralles  Kulturwort,  s.  Möller,  Semitisch und  Indogermanisch  37  f.]  'Pflüger',  all- gemein 'Bauer'.  In  Ägypten  und  anders- wo ist  das  Wort  die  Bezeichnmig  des Landbewohners:  dtsch.  Fellach,  frz. fellah.    [Devic  DEt  117.
581.  Ar.  fals:
Plrl.  fulüs  [aus  gr.  (pöUi;  ZDMG  XXI, 672/674]  'kleine Silber-  od.  Kupfermünze' ; hieraus  sp.  foluz,  pg.  fuluz  [Constancio
Dicc  578  b]  'dass.',  siz.  u.  it.  (dial.  Li- vorno)  filussi,  it.  (dial.  Florenz)  pilosso 'Geld,  Münze'.    [DE  270.  GSAI  III,  145.
582.  Ar.  laiiak:
'Wüstentuchs,  Fenek';  hieraus  sp.  alfa- negue  'Art  Pelzwerk'.  —  Der  zur  Jagd auf  den  Fenek  benutzte  Falke  hieß  häz al-fanak  'Falke  des  F.' ;  durch  Abfall  des Grundworts  [s.  z.  B.  hier  Nr.  570]  blieb sp.  pg.  alfanegue  'Falke  mit  schwarzem Gefieder',  kat.  alfanet,  frz.  alphanette, alphanesse  'dass.'.  [Möglich  wäre  auch die  schon  von  SOUSA  gegebene  Etymo- logie: al-hanik  'der  Würger'.]  [DE  102 bis  105.  Devic  DEt  26.  Lammens  Rem  19.
583.  Ar.  fänid:
'Zuckerwerk'  [aus  pers.  pänid,  Vb.  fänl- dän' den  Zucker  rafSnieren',  s.  SCHWARZ in  ZDMG  LXXIV,  238  u.  245];  hieraus mit  ar.  Art.  und  häufigem  Wechsel  von t  und  k  sp.  alfenique,  pg.  alfenim  'Teig aus  Zucker  und  süßem  Mandelöl',  frz. alphenic  'Kandiszucker,  Teig  aus  Mandeln und  Zucker';  frz.  penid  'sucre  tors';  in der  alten  Pharmazie  saccharum  peni- dium.    [DE  112.    Devic  DEt  27.
584.  Ar.  fauika:
'Großer  Sack' ;  hieraus  sp.  fanega,  frz. fanhgue  'ein  Getreidemaß  von  55  1';  aus der  ar.  Form  fanka  wurde  pg.  fanga 'dass.,  Maß  von  20Mudd  [s.  hier  Nr.  1490]'. [DE  266.    Devic  DEt  115.
585.  Ar.  fära:
'Sprudeln'  [vgl.  fawicära  'Wassersprudel, Quelle'  Dozy  Suppl  II,  235] ;  hieraus  siz. fara  'warme,  stickige  Luft',  affarari  'an- brennen'.   [GrSVociSic  233.
586.  Ar.  faras:
'Pferd';  hieraus  frz.  haras  'Stuterei' [wohl  über  das  sp.,  wo  f  und  h  wech- seln, vgl.  lat.  facere  >  sp.  hacer];  mit ar.  Art.  sp.  pg.  alfaraz  'leichtes  Pferd der  maurischen  Reiterei';  der  Sternname Alpheraz,  Alpheraih  a  Pegasi;  afrz.  au- fage  'Pferd',  auferrant,  prov.  alferan 'grau'  [mit  lat.Suffix  ant  und  Anlehnung an  fer  'Eisen',  ferrant  'eisenfarbig,  grau] ; hieraus  wohl  afrz.  ferrant,  prov.  ferran 'Pferd  von  grauer  Farbe' ;  ganz  unkennt- lich geworden  ist  altit.  alfana  'Reittier'. [DE  108.  Eguilaz  161.  Devic  DEt  41. ML  3189.
587.  Ar.  fard:
'Einzig',  davon  ar.  fard  as-su^ä'  'der einzige  der  Hydra',  ein  Stern  2.  Größe im  Sternbilde  der  Hydra,  der  einzige heller  leuchtende  Stern  dieses  Bildes,  da die  übrigen  4.  Größe  und  darunter  sind ; hieraus  der  Sternname .4ZpÄarrfaHydrae. [Devic  DEt  26/27.    Lammens  Rem  20.
588.  Ar  fard:
'Kerbe,  Einschnitt;  Zahlung,  Löhnung;
```


## [2026-09-06T14:54:03.176Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM fals\"; grep -n \"فلس\" AFM_pages.txt | head; echo \"=== PLA\"; grep -n -i \"fals\\|Fals\\|فلس\" incoming/PLA/PLA_pages.txt | head -20; echo \"=== FVQ\"; grep -n -i \"fals\" FVQ_pages.txt | head -10"
}
```


### [2026-09-06T14:54:03.264Z] TOOL RESULT

```
=== AFM fals
1422:وهو افلس الذي يظهر نفسة ذا ئروة جزية ويطلق ايض على الذي يظهر ننسةܫ عق ܫ
1423:مفلسا ٠‏ وقالوا فيه 0
3250:» ( اللا ) الداهي المفلس 4 ܨ
=== PLA
3629:       zum       Lachen        bringt;              falscher        Safran"
=== FVQ
647:Qur'an is Arabic which they understand perfectly, so their charge is false, for how
3206:To be in vain, false.
3211:a technical religious term for the nothingness, vanity, and falseness
4322:straight, so cJui>- was supposed to be one who turned from the false
5785:Falsehood.
5800:rather to be of Iranian origin. Pers. jj j is lie, falsehood, which
5803:Phlv. both simply as JyS zur, a lie, falsehood, fiction, 2 ' and in com-
5804:pounds as ^OO^^Vr zur-yukawh = false evidence, perjury?
5810:was borrowed into Arm., where wo find qjn-p false, wow/, 7 which
7412:texts KmJTlfl means false deity, which is very close to the Qur'anic usage. Cf.
```


## [2026-09-06T14:54:15.090Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT garewa\"; grep -n \"garəwa\\|garewa\\|garəbuš\\|garebus\\|garbuš\" BRT.txt | head -20"
}
```


### [2026-09-06T14:54:15.134Z] TOOL RESULT

```
=== BRT garewa
```


## [2026-09-06T14:54:16.099Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN 483 delphys\"; grep -n -i \"delphys\\|Delta\\|adelphos\\|Philadelphia\\|dolphin\" KLN_1966.txt | head -20"
}
```


### [2026-09-06T14:54:16.157Z] TOOL RESULT

```
=== KLN 483 delphys
1610:adelpho-,  combining  form  meaning  ‘brother’.  — Gk.  dSeXtpo-,  fr.  aScktpoq,  ‘brother’,  lit.  ‘from the  same  womb’,  fr.  copul.  pref.  a-,  ‘together with’,  and  SeXcpug,  ‘womb’.  Copul.  pref.  a- stands  for  I.-E.  *sm-,  a  weak  gradational  form of  I.-E.  base  *sem-,  ’one  together’;  see  same. For  the  etymology  of  SeXqiug  see  calf  and  cp. dolphin.  Cp.  also  the  second  element  in  Dia- delphia,  Didelphia,  monadelphous,  Philadelphus. For  the  sense  development  of  Gk.  d8£X<p6g  cp. Gk.  dydoxtop,  ‘from  the  same  womb’,  fr.  copul. pref.  a-  and  yao-rf)p,  ‘belly,  womb’, adempted,  adj.,  taken  away  (law).  —  Fr.  obsol. adempt,  fr.  L.  ademptus,  pp.  of  adimere,  ‘to  take away;.  See  next  word  and  -ed. ademption,  n.,  the  act  of  taking  away.  —  L. ademptio,  gen.  -onis,  ‘a  taking  away,  seizure’,  fr. ademptus,  pp.  of  adimere.  See  adeem  and  -ion. aden-,  form  of  adeno-  before  a  vowel, adenine,  n.,  also  adenin,  a  crystalline  base  (bio- chem.)  —  Coined  by  the  German  physiological chemist  Albrecht  Kossel  (1853-1927)  fr.  Gk. dS rjv.  ‘gland’  (see  adeno-),  and  chem.  suff.  -ine, -in;  so  called  by  him  because  it  is  derived  from pancreas.
2337:alpenstock,  n.,  a  long  iron-pointed  staff  used  for climbing  mountains.  —  G.,  lit.  ‘Alp  stick’,  com¬ pounded  of  Alpen,  ‘the  Alps’,  and  Stock,  ‘stick’. See  alp,  ‘a  high  mountain’,  and  stock, alpha,  n.,  name  of  the  1st  letter  of  the  Greek  al¬ phabet.  —  L.,  fr.  Gk.  diXtpot,  fr.  Hcb.-Phoen. dleph;  see  aleph.  The  final  a  was  added  because a  Greek  word  cannot  end  with  a  9;  cp.  beta, gamma,  delta,  eta,  theta,  iota,  kappa,  lambda, sigma.  See  Theodor  Noldeke,  Die  semitischen Buchstabennamen,  in  Beitrage  zur  semitischen Sprachwissenschaft,  Strassburg,  1904,  PP-  '34 and  135,  and  Eduard  Schwyzer,  Griechische Grammatik,  Munchen,  1939,  I,  140  y. alphabet,  n.  —  L.  alphabetum,  compounded  of Gk.  &X<pa  and  (iTjxx,  names  of  the  first  two letters  of  the  Greek  alphabet.  See  alpha  and beta.
4496:Bartonia,  n.,  a  genus  of  plants  of  the  gentian family  (bot.)  —  ModL.,  named  in  honor  of Benjamin  Smith  Barton  of  Philadelphia  (died in  1815).  For  the  ending  see  suff.  -ia. baruria,  n.,  an  abnormal  condition  in  which  the urine  has  a  very  high  specific  gravity  ( med .)  — Medical  L.,  compounded  of  Gk.  (3apu<;, ‘heavy’, and  oOpov,  ‘urine’.  See  bary-,  uro-,  ‘of  urine’, and  -ia.
4732:Beltane,  n.,  an  ancient  Celtic  festival  on  May Day.  —  Gael,  bealtuinn,  a  compound  lit.  mean¬ ing  ‘blazing  fire’.  For  the  first  element  see  bale¬ fire.  The  second  element  is  rel.  to  Olr.  ten,  ‘fire’ (for  I.-E.  *tepnos),  and  cogn.  with  L.  tepere,  ‘to be  lukewarm’,  tepidus,  ‘lukewarm’.  See  tepid and  cp.  words  there  referred  to. beluga,  n.,  a  kind  of  dolphin.  —  Russ,  beluga,  fr. beliy,  ‘white’,  which  is  rel.  to  OSlav.  bilu,  ‘white’, Lith.  bciltas,  ‘white’,  Lett,  bdls,  ‘pale’,  and  cogn. with  OE.  bail,  ‘a  blazing  fire’,  ON.  bal,  ‘a  great fire’.  See  balefire  and  cp.  the  first  element  in Beltane.
6181:calf,  n.,  young  of  a  cow,  etc.  —  ME.  calf,  kalf fr.  OE.  cealf,  rel.  to  OS.,  MDu.  calf,  ON.  kalfr, Dan.  kalv,  Swed.,  Du.  kalf,  OHG.  chatp,  kalb, MHG.  kalp,  G.  Kalb,  Goth,  kalbo,  ‘calf’,  OHG. kilbur  (neut.),  kilburra  (fern.),  OE.  cilforlamb, ceolforlamb,  ‘ewe  lamb’,  fr.  I.-E.  base  *gmelbh-, *gwolhh-,  ‘womb;  young  of  an  animal’,  whence also  OI.  garbhah,  Avestic  gar(wa-,  ‘womb’,  Gk. 82X964,  80X964  (in  Hesychius),  ‘womb’,  a- 82X964,  ‘brother’  (lit.  ‘from  the  same  womb’), Avestic  gerebush,  ‘the  young  of  an  animal’.  Cp. adelpho-,  dolphin,  and  the  second  element  in dagoba.  Cp.  also  chilver.
7970:clote,  n.,  the  burdock.  —  ME.,  fr.  OE.  elate,  rel. to  OS.  cledthe,  OHG.  cletha,  cletto,  delta, MHG.,  G.  klette,  fr.  Teut.  base  *kleip-,  cor¬ responding  to  I.-E.  base  *gleit-,  -/-enlargement of  *glei-,  ‘to  cleave,  stick  to',  whence  L.  gluten, ‘glue’.  See  clay,  and  cp.  glue,  gluten, cloth,  n.  —  ME.,  fr.  OE.  c/d/ >,  ‘cloth’,  rel.  to OFris.  Math,  MDu.  fleet,  Du.  kleed,  MHG.  kleit, G.  Kleid,  ‘garment’  (ON.  klxdi  is  possibly  bor¬ rowed  fr.  OE.  chip,  a  collateral  form  of  clap). These  words  prob.  stand  in  gradational  relation¬ ship  to  OE.  clidan,  ‘to  adhere  to’,  clida,  ‘plaster’, elide,  ‘bur’.  See  glue.
10248:daleth,  n„  name  of  the  4th  letter  of  the  Hebrew alphabet.  —  Heb.  daleth,  pausal  form  of  deleth , ‘door’,  which  is  rel.  to  Ugar.  dl,  Akkad,  daltu, ‘door’;  so  called  in  allusion  to  the  ancient  He¬ brew  form  of  this  letter.  Cp.  delta.  For  the  form cp.  aleph,  lamedh,  samekh.
10385:Derivatives:  dauntless-ly,  adv.,  daunt!ess-ness,n. dauphin,  n.,  the  title  of  the  eldest  son  of  the  king of  France.  —  F.,  lit.  ‘dolphin’,  translation  of L.  Delphinus,  lit.  ‘dolphin’,  orig.  a  name  borne by  Guigo  IV,  count  of  Vienne  (died  in  1142) and  by  his  successors.  The  name  Delphinus  was chosen  in  allusion  to  the  three  dolphins  repre¬ sented  in  the  coat  of  arms  of  the  lords  above mentioned.  Hence  the  province  owned  by  them came  to  be  known  as  Delphinatus  in  Latin (whence  F.  Dauphine).  See  dolphin, dauphine,  n.,  a  dauphiness.  —  F.  dauphine,  fern, of  dauphin.  See  dauphin.
10744:Delphinidae,  n.pl.,  a  family  of  toothed  whales (zool.)  —  ModL.,  formed  with  suff.  -idae  fr.  L. delphinus,  ‘dolphin’.  See  dolphin.
10745:Delphinium,  n.,  a  genus  of  plants,  the  larkspur (bot.)  —  ModL.,  fr.  Gk.  SeXipfiaov,  ‘larkspur’, fr.  SeXtpfi;,  gen.  SsXcpivo?,  ‘dolphin’  (see  dol¬ phin);  so  called  from  the  shape  of  its  flowers, which  resemble  a  dolphin, delta,  n.,  1)  name  of  the  4th  letter  of  the  Greek alphabet ;  2)  triangular  area  formed  at  the  mouth of  some  rivers,  as  of  the  Danube.  —  Gk.  SiXza., fr.  Fleb.-Phoen.  ddleth;  see  daleth.  The  a  was added  because  a  Greek  word  cannot  end  with a  x;  cp.  alpha  and  words  there  referred  to. deltafication,  n.,  the  formation  of  a  delta.  — • Formed  fr.  delta  and  -fication. deltaic,  adj.,  forming  a  delta.  —  Formed  fr.  delta with  suff.  -ic.
10746:deltoid,  adj.,  delta-shaped,  triangular.  —  Gk. Se'AzoEiSr.c,  compounded  of  8eXxa  and  -osiStji; ‘like’,  fr.  eTSo?  ‘form,  shape’.  See  delta  and  -oid. deltoid,  n.,  the  large  muscle  covering  the  shoulder joint  (anat.)  —  From  deltoid,  adj.;  so  called from  its  triangular  shape, delubrum,  n.,  a  shrine,  a  sanctuary  ( Roman  an- dq.)  —  L.  delubrum,  ‘temple,  shrine,  sanctuary’, a  derivative  of  deluere,  ‘to  wash  off,  cleanse’, originally  meaning  ‘place  for  washing  (near  the sanctuary)’.  Delubrum  prob.  stands  for  *de- lu-dhlom  or  *de-lu-dhrom,  fr.  de,  ‘away  from’, the  stem  of  lucre,  ‘to  wash’,  and  a  suff.  denoting place  (cp.  pollubrum,  polubrum,  ‘wash  basin’, for  *po-lu-dhlom  or  *pd-lu-dhrom).  See  de-  and lave.
12026:dolphin,  n.  —  ME.  delphin,  delfyn,  fr.  OF.  daul- phin,  dalfin  (F.  dauphin),  fr.  ML.  dalfinus,  fr.  L. delphinus,  delphin,  ft.  Gk.  8eX<pt?,  gen.  SeXiptvo?, ‘dolphin’,  which  is  rel.  to  SeXipu?,  ‘womb’;  the
22325:lunkah,  n.,  a  strong  kind  of  cheroot.  —  Hind. lanka,  a  name  derived  from  the  Lankah  islands in  the  delta  of  Godavary  River,  where  tobacco is  grown.
25042:Naucratite,  adj.,  pertaining  to  Naucratis,  an  an¬ cient  Greek  colony,  established  by  colonists from  Miletus  in  the  Nile  Delta.  — L.  Naucratites, fr.  Gk.  NauxpaxtxvjS,  fr.  Nauxpaxt?.  For  the ending  see  subst.  suff.  -ite. naufragous,  adj.,  caused  by  shipwreck  ( archaic  or obsol.)  —  L.  naufragus,  ‘shipwrecked;  causing shipwreck’,  for  *navifragus,  which  is  compound¬ ed  of  navis,  ‘ship’,  and  the  stem  oifrangere,  'to break’.  See  naval  and  fraction.  For  E.  -ous,  as equivalent  to  L.  -us,  see  suff.  -ous. naught,  n.,  nothing.  —  ME.  naught,  nought,  etc., fr.  OE.  nawiht,  ‘nothing’,  lit.  ‘no  whit’,  fr.  nd, ‘no’,  and  wiht,  'whit’.  See  no,  adv.,  and  wight and  cp.  aught,  nought,  not,  nix,  ‘nothing’. Derivatives:  naught,  adj.,  naught-y,  adj.,  naught- i-ly,  adv.,  naught-i-ness,  n. naumachia,  naumachy,  n.,  1)  a  mock  sea  fight;  2) place  where  such  a  fight  is  presented  (Roman antiq.)  —  L.,  fr.  Gk.  vaup.a/la,  ‘naval  battle’, compounded  of  van?,  ‘ship’,  and  -uay.a,  fr. \s.y-/r„  ‘battle’.  See  nau-  and  -machy. nauplius,  n.,  a  larval  stage  in  the  development  of many  crustaceans  (zool.)  —  L.,  ‘a  kind  of  shell¬ fish  which  sails  in  its  shell  as  in  a  ship',  fr.  Gk. vau7tXtoi;,  lit.  ‘sailing  (as)  in  a  ship’,  fr.  vau<;, ‘ship’,  and  7tX£Etv,  trXetv,  ‘to  sail,  navigate, swim,  float’.  See  naval  and  flow  and  cp.  pluvial, nausea,  n.,  1)  feeling  of  sickness  at  the  stomach; 2)  disgust,  loathing.  —  L.  nausea,  nausia,  ‘sea¬ sickness’,  fr.  Gk.  vxuoia,  vauxta,  ‘seasickness’, lit.  ‘ship  sickness’,  fr.  vans,  ‘ship’.  See  naval  and cp.  nautical.  Cp.  also  noise,  which  is  a  doublet of  nausea.
33437:yeasts  (bot.)  —  ModL.,  lit.  ‘sugar  fungi’  (see saccharo-  and  -myces),  prop,  a  loan  translation of  G.  Zuckerpilz,  a  name  given  to  yeast  by Theodor  Schwann  (1810-82).  See  C.  C.  Mettler, History  of  Medicine,  Philadelphia  -  Toronto, 1947,  p.  261.
37301:subtonic,  n.,  in  music,  the  seventh  tone  of  the scale.  —  Coined  by  James  Rush  (see  his  Philos¬ ophy  of  the  Human  Voice,  4th  ed.,  Philadelphia, 1855,  p.  82)  fr.  sub-  and  tonic, subtract,  tr.  v.  —  L.  subtractus,  pp.  of  subtrahere, ‘to  draw  off,  withdraw’,  fr.  sub-  and  trahere,  ‘to draw’.  See  tract  and  cp.  words  there  referred  to. Derivatives:  subtract-er,  n.,  subtraction  (q.v.), subtract-ive,  adj.
40512:Turritella,  n.,  a  genus  of  gastropods  with  long turretlike  shells  ( zool .)  —  L.,  dimin.  of  turris, ‘tower’.  See  tower  and  -ella, tursio,  n.,  the  bottle-nosed  dolphin  (zool.)  — ModL.,  fr.  L.  tursio,  ‘dolphin,  porpoise',  fr.  Gk. ffupoicov,  of  s.m.,  which  is  possibly  related  to D-upaop,  ‘a  straight  shaft’.  See  thyrsus, turtle,  n.,  turtledove  (archaic).  —  ME.,  fr.  OE. turtle,  formed  fr.  L.  tur  tur  (with  dissimilation  of the  second  r  into  /),  which  is  of  imitative  origin. Cp.  Tetraonidae.
```


## [2026-09-06T14:54:29.164Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD\"; grep -n -i \"gwelbh\\|g\\\"elbh\\|kalbaz\\|chilver\" AHD_watkins1985.txt | head -10; echo \"=== AHD calf\"; grep -n \"calf\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-06T14:54:29.224Z] TOOL RESULT

```
=== AHD
1217:ADDER nétr- ADDICT deik- ADDUCE deuk- -ADELPHOUS gWelbh- ADEMPTION em- ADENO- engW- ADEPT ap-1 ADHERE ghais- ADIABATIC gWa- ADIEU delw- ADIT ei-1 ADJACENT yé- ADJECTIVE yé- ADJOIN yeug- ADJOURN deiw- ADJUDICATE yewes- ADJURE yewes- ADJUST yeug- ADJUVANT ad- ADMIRE smei- ADMIT (s)meit(9)- ADMIX meik- ADMONISH men-t ADNATE gene- ADNEXA ned- ADO ad- ADOLESCENT al-3 ADOPT op-2 ADORE Or- ADORN ar- ADRENERGIC werg- ADSCITITIOUS skei- ADSORB srebh- ADULT al-3 ADULTERATE al-1 ADULTERINE al-1 ADULTERY al-1 ADUMBRATE andho- ADUST eus- ADVANCE ant- ADVECTION wegh- ADVENT gWa- ADVENTITIOUS gWa- ADVENTURE gWa- ADVERB wer-6 ADVERSE wer-3 ADVICE weid- ADVISE weid- ADVOCATE wekw- AECIUM weik-3 AEDES swad-
1432:DOGE deuk- pocMa dek-1 pDoGMaTIC  dek-! DOIT twei- DOLABRIFORM del-3 DOLCE dik-u- DOLDRUMS_ dheu-t DOLE! dail- DOLE? del-3 DOLERITE del-2 DOLICHOCEPHALIC del-1 DOLICHOCRANIAL  del-1 DOLOR del-3 DOLPHIN gWelbh- Dott dheu-1 Dom deme-1, dhé-1 DOMAIN deme-! DOME deme-1 DOMESTIC deme-1 DOMICILE deme-! DOMINATE deme-1 DOMINICAL deme-1 DOMINIE deme-1 DOMINION deme-' DOMINO! deme-1 DOMINO2 deme-1 DONATION d6- DONATIVE d6- DONOR do- poom dhé-1 pooR dhwer- DOPE dub- DORMANT drem- DORMER drem- DORMITORY drem- DORSAL dorsum poRrsO- dorsum pory? aurum DOSE dé-
=== AHD calf
840:per-3. The young of an animal (< “a bringing forth,” “offspring”), Derivative root belonging to the group of per'. Suffixed o-grade form *por-si- in Germanic *farzi-, young cow, in Old English fearr, calf, and compound heahfore, calf (first element obscure): HEIFER. [In Pok. 2. D. per 818.]
999:nare, to make firm, establish (dé-, thoroughly; see de-): DESTINE; b. Latin obstindre, to set one’s mind on, persist (ob-, on; see epi): OBSTINATE. 8. Suffixed form *séa-tu- in Latin status, manner, position, condition, attitude: STATE, STATISTICS, STATUS. 9. Suffixed form *sto-dhlo- in Latin stabulum, standing place: STABLE. 10. Suffixed form *si-dhli- in Latin stabilis, standing firm: ESTAB- LISH, STABLE!. 11. Suffixed form *sf-td- in Greek -statés, one that causes to stand, a standing: -sTAT; ENSTATITE. III. Zero-grade form *st-, *st()- (before vowels). 1. Reduplicated form *si-sio)- in: a. Latin sis- tere, to set, place, stop, stand: ASSIST, CONSIST, DESIST, EXIST, INSIST, INTERSTICE, PERSIST, RESIST, SUBSIST; b. Greek histanai (aorist stanai), to set, place: APOSTASY, CATASTASIS, DIASTASIS, ECSTASY, EPISTASIS, EPISTEMOL- OGY, METASTASIS, PROSTATE, SYSTEM; Cc. Greek histos, web, tissue ( < “that which is set up”): HISTO-; HISTIO- cyTE. 2. Compound form *iri-st-i-, “third person stand- ing by” (see trei-). 3. Compound form *por-st-i-, “that which stands before” (*por-, before, forth; see per’), in Latin postis, post: PosT!. 4. Suffixed form *st-o- in compound *upo-st-o-, “one who stands under” (see upo). IV. Extended root *std@u- (< *staau-), becoming *stau- before consonants, *stdw- before vowels; basic meaning “stout-standing, strong.”’ 1. Suffixed extended form *staw-d in Germanic *st6w6 in Old English stéw, place: stow. 2. Probable o-grade suffixed extended form *stow-yad in Greek stoa, porch: STOA, STOIC. 3. Suffixed extended form *stau-ro- in: a. (i) Latin instaurdre, to restore, set upright again (in-, on; see en): STORE; INSTAURATION (ii) Latin restaurdre, to restore, rebuild (re-, anew, again; see re-): RESTORE; b. Greek stauros, cross, post, stake: STAUROLITE. 4. Variant *tau-ro-, bull (see tauro-). V. Zero-grade extended root stii- (< *stua-). Suffixed form “*sti-lo- in Greek stulos, pillar: STYLITE; AMPHISTYLAR, ASTYLAR, EPISTYLE, HYPOSTYLE, PERI- STYLE, PROSTYLE, STYLOBATE. VI. Secondary full-grade form *steua-. Suffixed form *steua-ro- in Sanskrit stha- vira-, thick, stout, old: THERAVADA. VII. Variant zero-grade extended root *stu-. Suffixed form *stu-t- in Old English stuthu, studu, post, prop: STUD'. VIII. Sec- ondary full-grade form *steu-. 1. Suffixed form *steu-raé in Germanic *steur6, “a steering,” in Old English stéor, a steering: STARBOARD. 2. Germanic denominative *steur- Jan in: a. Old English stieran, to steer: STEER}; b. Old Norse styra, to steer, with its derivative stjérn, a rudder, a steering, akin to the possible source of Middle English sterne, stern of a boat: STERN?. 3. Suffixed form *steu-ro-, a larger domestic animal, in Germanic *steu- raz, ox, in Old English stéor, steer: STEER?. 4. Probably Germanic diminutive *steur-ika- in Old English stirc, stierc, calf: sTIRK. See stak-. [Pok. std- 1004.]
1166:wet-2, Year. 1. Suffixed form *wet-ru- in Germanic *weth- ruz, perhaps “yearling,” in Old English wether, wether: WETHER. 2. Suffixed form *wet-es- in: a. Latin vetus, old (< “having many years”): VETERAN; INVETERATE; b. Latin veterinus, of beasts of burden, of cattle (perhaps chiefly old cattle): VETERINARY; C. Greek efos, year: ETESIAN. 3. Suffixed form *wet-olo- in Latin vitulus, calf, yearling: VEAL, VITELLUS. [Pok. wet- 1175.]
```


## [2026-09-06T14:54:30.843Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT try\"; grep -n -i \"garewa\\|garvwa\\|gar9wa\\|garabus\\|garabuS\\|garewo\" BRT.txt | head -10; echo \"=== BRT g_r_wa col 513ish\"; grep -n \"gar∂\" BRT.txt | head -10"
}
```


### [2026-09-06T14:54:30.903Z] TOOL RESULT

```
=== BRT try
11608:6o7  j^^garabuStara-
11614:•  j.  JägarabuS'tara-  Adj.  'der  besser  er- fasst,  begrifTea  hat',  mit  Akk.verb.:  hSuea ^afiayS  narä  vohu  matiB  °tarB  anhat  yS.. "und  der  von  den  beiden  Männern  hat den  guten  Sinn  besser  erfasst,  der  .." V.  4.  48.
=== BRT g_r_wa col 513ish
```


## [2026-09-06T14:54:37.307Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gWelbh-\\|gWelbh\" AHD_watkins1985.txt | head; echo \"---\"; grep -n \"^gWel\\|gWelbh-\\. \" AHD_watkins1985.txt | head"
}
```


### [2026-09-06T14:54:37.361Z] TOOL RESULT

```
1217:ADDER nétr- ADDICT deik- ADDUCE deuk- -ADELPHOUS gWelbh- ADEMPTION em- ADENO- engW- ADEPT ap-1 ADHERE ghais- ADIABATIC gWa- ADIEU delw- ADIT ei-1 ADJACENT yé- ADJECTIVE yé- ADJOIN yeug- ADJOURN deiw- ADJUDICATE yewes- ADJURE yewes- ADJUST yeug- ADJUVANT ad- ADMIRE smei- ADMIT (s)meit(9)- ADMIX meik- ADMONISH men-t ADNATE gene- ADNEXA ned- ADO ad- ADOLESCENT al-3 ADOPT op-2 ADORE Or- ADORN ar- ADRENERGIC werg- ADSCITITIOUS skei- ADSORB srebh- ADULT al-3 ADULTERATE al-1 ADULTERINE al-1 ADULTERY al-1 ADUMBRATE andho- ADUST eus- ADVANCE ant- ADVECTION wegh- ADVENT gWa- ADVENTITIOUS gWa- ADVENTURE gWa- ADVERB wer-6 ADVERSE wer-3 ADVICE weid- ADVISE weid- ADVOCATE wekw- AECIUM weik-3 AEDES swad-
1432:DOGE deuk- pocMa dek-1 pDoGMaTIC  dek-! DOIT twei- DOLABRIFORM del-3 DOLCE dik-u- DOLDRUMS_ dheu-t DOLE! dail- DOLE? del-3 DOLERITE del-2 DOLICHOCEPHALIC del-1 DOLICHOCRANIAL  del-1 DOLOR del-3 DOLPHIN gWelbh- Dott dheu-1 Dom deme-1, dhé-1 DOMAIN deme-! DOME deme-1 DOMESTIC deme-1 DOMICILE deme-! DOMINATE deme-1 DOMINICAL deme-1 DOMINIE deme-1 DOMINION deme-' DOMINO! deme-1 DOMINO2 deme-1 DONATION d6- DONATIVE d6- DONOR do- poom dhé-1 pooR dhwer- DOPE dub- DORMANT drem- DORMER drem- DORMITORY drem- DORSAL dorsum poRrsO- dorsum pory? aurum DOSE dé-
---
```


## [2026-09-06T14:54:37.512Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11595,11625p' BRT.txt"
}
```


### [2026-09-06T14:54:37.557Z] TOOL RESULT

```
•  j.  Jar«zay-  Adj.  'klagend':  yaj  ..  nars aiacnS  ..näiriiiüd  ..'zlm  baraiti  väüim  V. J.  1 1.
Znm  V.  gar>i-.  —  Pü. :  ganäiQ). y,  %.  Jat'  Vetbalf.:  s.  unter  gam-.
•  j.  Jasant-'^  Adj.  (fem.  'saitl-,  'säiti'), PPA. :  s.  gam-.
KompE.  —  ')  Dazu  jasSnt>m  F.  4g,  dessen  i (aas  ä,  %  3gS.  7)  mit  dem  von  vijmäitii  im Zusammenbang  stehen  könnte.  Ist  aber  die Form  echt?
•  j.  Jastay-  f.  'Bitte':  yal  nä  kasvtkqm- Hna  , .  "ta  (LS.)  n5il  da^äili  "wenn  er  . . bei  Bitte  (sva.  trotzdem  er  dram  gebeten wird)  . ."  V.  /<?.  34.
KompE.  —  Zum  V.  gad:  —  PS.:  ia  iädil. j.  jaiui  FrD.  g:  lies  zazus.
•  y  Jazav-  m,  (auch  mit  'spart-  m.)  Name einer  Art  des  Hundegeschlechts:  hau  °z3us (GS.)  hau  visäui  . .  hau  vTspanam  . .  spa- ct^ranam  V. /J.  16;  —  spä  *ius  V.^.^j.
Pü.:   ?ehlt  [ni  rfftnai).
j./iiAöf  Ny. /.  I:  lietßAäJ;  s.^ain-,  Sp.  4950. \.  Jaht.kaTslaht  YL  13.  141:  lies /af.i°.
•  j,  Jahi-  f.  'Weib'  uzw.  der  (Äl^iischen Schöpfung;  daher  in  verächtlichem  Sinn 'Dirne,  Mensch"':  'hi  yatumaili  -Ai  ka- x''arfhaineYt3.%  12,  16»;  V.  2/.  i7(VS.); —  °hi  . .  alimatj^B . .  masyas^a  drvi  säita V.2J. I ;  —  -ki  ..ys  (statt NSC)  xsudrä  kam,- rai^wayeiti  dahmanam  adahmanamca  . . \. 18.62;  — /aAr/äf  (NS.)'>  "/?(NS.)'> F.  2  f.;  —  jais  (AP.)  '>  F.  15.
KompA.  Qae')');  Ableit.  —  mp, /äiJ);  ai. vgl,  hasrä'  f.,  BtHL.  BB.  15.  2,  //.  339,  IF.  /. 381  No,  8.  249.  ~  Pü,  (lu  ¥.  3):  lan  ia  val, {so-nst)  )e6;  Sü.:  veiyä, /atadJtäf.  —  »)  Im Gegensati  zu  1)  Höiriiä;  vgl.  Pü.  und  V.  rS.  62 mit  N.  7/  (s.  auch  zu  Jahikä-),  z)  zu  iainyä; vgl.  M.  3.  9  mit  der  Übersetzung  der  ver- lorenen Stelle  H.  3.  27  in  Av.  //.  la,  wo ian  i  jeh  gegenüber  kamt  in  4.  iS  bezeugt ist*).  In  mp.  Schriften  gilt/?*  als  Dämonin der  Menstruation,  vgl.  Bd.  $.  7.  —  »)  Ich sehe  in  _/a^  (auch  KompA.)  und  _/a"  eine  Ver- stümmelung von  _/flA/,  *JaATlSI;  s.  ZDMG.rfj, 66S,  4S.  149.  Noch  weiter  geht  die  Verderbnis bei  Jf  statt /n*i;  s.  auch  gi.  —  J)  So,  mit  _/, nach  der  /ttirini/lesung/i*,  die  aber  vll.  durch das  Aw.  Wort  beeinllusst  ist.  —  0  An  den entsprechenden  Stellen  des  Mi,  steht  freilich beidemale  intüi,  2.  125,  167.  —  S>  An  ein ar.  Thema  '^a{).)7-  (S  /ff)  ist  doch  kaum  zu
•  j.  Jahikä-  f.  dnw.  jaAi-  '• :  yai  nä  ['ia] " .  .  frapataiti  anaiwyästa  (sd.)  vä  . .  V, /Ä'.  54;  —  narö  pairistajduorö  ..  "ka para.daxsta  (sd)  Yt/J.  54;  —  mä  ki mairys  giurvaysii  mä  °ka  Yt,Ä59;  — nSit  *mairyeke  ndif  'kayä  P.  jo ;  —  tat näiriiayäi  .  .  aJaonyai  .  .  tal  'kayäi  . . drvaityai  i^ar3%3m  H.3,iS-36;  —  'kayai
dby  Google
6o7  j^^garabuStara-
.  .  yätumaityäi  Y,  5.  33;  —  haca zanyäi  °kayai  Ytij.sj;  58;  —  as/t  ii (nämL  sanahe)  kaim  ya^a  'kaya  V.  jj. 44;  48;  —  airitö  [^A.)  pantsrum  ya^a 'ka  V.  1^.48;  48'.
AbleiL  laajakU.  —  ^.•.  )ih%  s.  im  jafä:  —
')  Im  Gegensati  tu  näiriiS-,  s.  H.  3.  18,  36.
—  ')  Ergänzende  Glosse,  s.  vafrapataili,  unier
/W-  No.  4.
•  j.  JägarabuS'tara-  Adj.  'der  besser  er- fasst,  begrifTea  hat',  mit  Akk.verb.:  hSuea ^afiayS  narä  vohu  matiB  °tarB  anhat  yS.. "und  der  von  den  beiden  Männern  hat den  guten  Sinn  besser  erfasst,  der  .." V.  4.  48.
Kompar.  ans  dem  PPfA.  des  V.  ^a*..  —  Pj.  : yäi  Ifiic  Jäl)  gfißär/ar,    ed.:  iui  fa  lan  apar
•  j.  "Jätnä-Ä  mir)t5  saoca"  Yt.4-7-
•  j.  Jätnäspa-,   g.  däjlmäspa- ''  m,  EN.
(Za/*äoTt75)  zweier  Gläubiger  r)  des  Mi- nisters Visiäspai,  Schwiegersohns  Zara- &aÄr<is">,  Bruders  FraSao^tra%  aus  der ^»j^flfamilie:  °pahe  AvSvaAe  (sd.)  Yt y- 1 03  j  — ya^rS  vS  a/sman[{sd.)  sSrtghänT ..  'pa  (VS.)  hvs^va  (sd.)  Y.  46,  17; 4g.  9 ;  —  tarn  ciitltn  'fS  hvB.gvS  tsldü :^armh  (sd.)  ala  vtnnti  Y.  5/.  18;  — yS  . .  bar?sma  */rasttrmte  ya%a  asava  °p5 */rastfrinaSa  ra/u/rif  li.Sg;  —  amava ya^a  °pü  Az.  2;  2;  Vyt_j;  —  yävaranä *frasaoslra  •/s(ND.)  ..ta  vannilcä (sd.)  . . Y./2, 7;  —  ao/i/a  tT  zarai:uslra  fralaos- tralibya  'pa^bya  Vyt.  //;  —  tarn  (näml. andvltn)  yazaia  -ps  yat  spShm  pairi.- avalnal . .  drvatqm  Yt  5.  68,  a)  °pafie aparamtahe  (sd.)  asaonS  Yt  ij.  127.
Ableit.    —    Komp.:    *Jäma-  Adj+at/tu-,  eig.
'der  -?-  Pferde  hat'.—  >)  iScbr.  s.  ?ÖJ'.  51.
Pü.  gibt  lii  allerdings  besonders,  durch  aVu/u-
luar  wieder;  s.  aber  Jil.aia.  No.  1.  —  ')  Vgl.
•  j.  Jämäspana-  patr.  Adj.  'von  Jamaspa stammend,  dessen  Nachkomme':  Aar?hau- riisJ  'nahe  asaoriS  Yt.J_y,i04;  —  varhiahe . .  'nahe  FrD.  7.
Ableit.  axa  jämlißa-.
j.  «/JF.  2f.:s.  unter  >^/-.
```


## [2026-09-06T14:54:45.196Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Junges\\|Junge eines Tieres\\|Tierjunges\\|Leibesfrucht\\|Mutterleib\" BRT.txt | head -20"
}
```


### [2026-09-06T14:54:45.248Z] TOOL RESULT

```
3592:erhalte  im  Mutterleib  die  empfangenen SShne,  so  dass  sie  nicht  sterben  . ."  Yt i_j.  r  I ;  —  frava^ayS  .  .  yä  .  .  pu^re  vT- oäraym  paiH.vtrfte  °^pniJ'^  Y.  2j.  i;  Yt. 13.28.
10253:•  j.   gaMWa-   m.    l)   'Mutterleib,   Uterus':  I         i-  Sanmü.vataahim  A.  J,  ?;  lies  a^arim-,
10257:5.  2)  'Leibesfrucht,  _/W«j'':  ma  . .  iaiiie]  gen'O.  -  IMi,:  oddamk  (Jamaspji  Gloss.547;
10372:•  j,  *gar3buS-''  n.  'Junges'  eines  Tiers:
12841:mit  ni!  'herauszenen,  reissen  aus  -' (AaA  mit  Abi.):  ^«äa  vfhrks . .  bar3%rya^ haca  ptihr^m  niidarjjiairyat  "als  ob  ein ,. Wolf  das  Kind  aus  dem  Mutterleib  heraus- risse" V.  18.  38.
16972:•  '].  baradrl-  f.  Tntgeiin,  Erhalterin; Mutter':  zqm  pgrikviXm  . . ya  '%ri  paraoi srJrahe  y3  vupsm  aAüm  .  .  baraiti  Yt y.  9;  *F,  2f.**,  *7ff'*;  —  tarn  ptn%wim  .. ■ärr«  ß  Aaoma  Y.  lo.  4;  —  '%ry3t  haca zavi/i (sd.)  V./5,6.  a)  sva. 'Mutterleib': aniaräj  nafmät  '^risva  uruhuidAva  (sd.) V.  5.  S I ;  —  yi  'hrisva  pü5>re  v^araym PaiH.v»r3te  apara.ir^PfUS  Y,  23.  i ;  Yt /_J.  11;  —  ya%a  vihrks  .  .  ''hryät  Aaca pu%nm  niidan.dairyat'V.sS.zZ.  b)sva. 'schwanger,  trächtig';  'hrayqm  *baatdri ''Sn'i?ä(näml.^uWo)/aSr3Äj(sd.)V./5.49.
19992:—  yS  mä  nä  manxiaite  (3SKj-AorM.) ««yaäaCsd.) .,  Y.57. 10;  — yai  wärdhva tmnn^aite  amakva  bUasyät  "wenn  sie (jaAi'i;  s.  %i)  nachmittags  (Üim)  Schaden zufUgt,  soll  man  (ihn)  abends  kuriren"  V. 2/- 3;  3';  —  s.  noch  m?r?n^ant-  (nur Ableit).  a)  Des.  'zu  töten  versuchen'; aSahmai  pu%rat  (statt  Akk.)  mimanx^a- nuha  aitdha  a^a  yä  kaine  attakmai /«ärJ/ (statt  Akk.)  *mimar?xl3ite  '"damit such  dein  Kind  (im  Mutterleib)  zu  töten  I' Dann  versucht  das  Mädchen  ihr  Kind damit  zu  töten"  V.  75. 14.
23709:.  PluT.  'Leibesfrucht':  hs n  ni/ainli  (sd.)  ya%a  . .
25521:•  j.  umd'wan-,  'iwar-  n.  'Eingeweide, Bauch':  'wan  F._?g;  —  yB  gSus  'wart hqmpnfraiti  (sd.)  V.  4.48;  —  auch  Plur. : astila  gaonala  ^dimohaca  *''wqmca  pah- yasca  fraväxlas^a  YL  /_J.  1 1 ;  —  yB  nars aiaonB  kaca  "wqn  bt/asyät  "der  bei  einem Gläubigen  die  Eingeweide  kurirt"  V.  7. 44(?);  —  alte  äaxma  (sd.)  upanAanzalta an/aräj  naiMät  barp%ri/va  'WBJiva  "die Leicheostätten  soll  sie  (damit)  besprengen innen  im  Mutterleib,   im  Eingeweide"  V.
```


## [2026-09-06T14:54:46.343Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"gsrsbus\\|g3r3bu\\|garabu\\|gorobu\\|grabus\\|rabuS-\" BRT.txt | head -20; echo \"--- search 'buS-'\"; grep -n \"buS-\" BRT.txt | head -20"
}
```


### [2026-09-06T14:54:46.407Z] TOOL RESULT

```
11608:6o7  j^^garabuStara-
11614:•  j.  JägarabuS'tara-  Adj.  'der  besser  er- fasst,  begrifTea  hat',  mit  Akk.verb.:  hSuea ^afiayS  narä  vohu  matiB  °tarB  anhat  yS.. "und  der  von  den  beiden  Männern  hat den  guten  Sinn  besser  erfasst,  der  .." V.  4.  48.
--- search 'buS-'
10372:•  j,  *gar3buS-''  n.  'Junges'  eines  Tiers:
```


## [2026-09-06T14:54:51.571Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10245,10275p' BRT.txt; echo \"=====\";  sed -n '10365,10385p' BRT.txt"
}
```


### [2026-09-06T14:54:51.628Z] TOOL RESULT

```
dby  Google
515  gar»d-  mit  avi  —  garäta-  516
AumataSa   hastaca  hvar^aca;    aiwi^trü-  bleiben  oder  sich  im  Hals  festsetzen"  V,
mahi  ahm  vohü  Vr.iy.i;  —  aiwi^ßnl-'  i^.^.
mahi  apqm  .  .  fräitlmca  .  .  Y,  Ö2.  n.         1     Vgl.  <'gat-  f.  —  Pü. :  galäk  (=  np.  gulü\
mit  avi  dn.:    avi  apqm^a  «m/r«- 1      ■  ^„^y.  ^  -Hitze' :  vJ  >i<y/.7  äp«ä
namca  . .  yasn,mg,f^r,n,aht  vaAm?mca  ,  .   ,,an%aüyw>m  frak»rmtatar,rSmainyus\. "7.  ■  ■  r^T         vi"-'-  V  P-      '"'''>^T»f^a  'maum  (AS.)' V.  m8.
Ut  vgl.  gradier.   —     VeL  gjnzday-.    —    Pü.!,       ,,  ,  d-  -i
•  j.   gaMWa-   m.    l)   'Mutterleib,   Uterus':  I         i-  Sanmü.vataahim  A.  J,  ?;  lies  a^arim-,
j.«   (näml.  aridvt,    mpunqm   hlmSimm' ,  ■    „„„s.starana-   m.   ein   bei    der Mää,  ••<™,.>^...v4,M,«  Y.65.=;-Arp^i„»        gebrauchtes    Gerät:    ymiäMi
(oaml,  arpdvi)  arsnqm  xsudm  m  xlaä^rt- 1  ,  ,  .       °  /  Fp  \  y  »4  7
nqm    *'wqn  ■>   (näml.  yaeidalaiÜ)    Y.  65.  |  >,i,ara„a-  n„  vll.  lü  lit.   'skilti  -Feuer  anschlü-
5.  2)  'Leibesfrucht,  _/W«j'':  ma  . .  iaiiie]  gen'O.  -  IMi,:  oddamk  (Jamaspji  Gloss.547;
mafySnam  pard  fsanmat  {sA.)  :^atU  °W3m^  ".^j/.imi;  Utensils  med  in  the/äi' »j^*-^/(highet
ra?sayät\.  15.11;    ij.   "  "r?'"l'"i    of    'he    Zoroastrian     rdigion^)
..i-^Ma-  m.  I)  -Uterus,  i) 'fetus  ;  mp-  (P";)  (^o !,/„/«/  5,™r^«rf.   -    ■)  Np.  >mr  'Kohk'
■^r.  -    .)  NA.  -,«,;    s.  aber  Var.  und  Yt.  1^,   '^Q^^  „^^^  jjpp_j_  ^g^  fernzuhalten!    i-
j.  gartiai;  lies  giribiü.
•  j.  gar«nav-  m.  'Krätze':  altaliva  dax- maeiva  Aqm.iavainti  axtii^a  'mdc'a  ..\.y.
jelil  Glrili.  /  b.  87.
•  j.,   g.   garaz-  V.   'klagen',     Praes. ,gii-}Z;  S  Jlg»r3z-  [,  25  g»r?zanä\.
57;  —päilistJUe  -näuica  (GS.)  /.rAffW-ii  1      '•''"S^"'  wehklagen,  jammern';   i)  ohne
Yt.y.i,
Obj.:  yeühe  vlxs  gpn
mp.  (Pö.)V'rr.  np.  ^^  -KritK';  so  nseh  JN. ' '■''^''«  (^d.)  a/naoiti  Yt./o.Ss;  —  «d.Vffi JAOS.  14.  cxxv.  g)r>zänä  (NPf.,  näml.  fravalay^)  /ilra-
.  j.,  g.  gamma-  (,  p,  .r«""«»-)  i)  Adj.  {""•  ■  ■  W'l-'Sr.  'S-^'S  -  f"  ffr.! 'heiss,  (Obertrieben)  warm':  aM  a/l .. ��mal  /'■«»« /nf»«i (f.) ..  »«™»'.w- (sd.) . . Yt;o.so,  V.2.S;  -  -»»».ä,  vmm  mlimla  y5»""«(3PPrA,)'>i««äimi^I  ««V,»J "2u  waimen  und  zu  kalten  Wind"  Yt.o.io:''""*'  •  '''  T*?  ■«  J™""» '»  ■?=»■ ««.«».  M  „faJ.Sal  "wenn  (ihm)  die  m  »opheten'  Y.^ja.ij  a)  mit  Dal  der heissen  Speisen  Maul  oder  Zunge  «er-  P="<"'-/"''t; '',?™''  '  .''  » '"''«»^. brennen"  V.,5.4.  2)  n.  'Hitze,  Gluf:  K^ä-)   "''":'  ^iti.Kr..  "'™,'?-"'  •?*'
mil  aot,m..,ml  •mimX.ti.t,;  —  inahyar""  l""^ ''^^^^>  «"^  '"''S"  *= •mi  «3!«  ^-J.^^yWto  ,(/«/  „j/m»;,;„-iS=e>='äes  Stiers'   Y.  25. .«;   daraus   zit-
haa  jimat  mamai!  "wenn  durch  die  !•?'"■"''!'  f'",  A  ~ /"  .'  '  ""f'^'f"'' Glut  deines  Feuers,  dss  seine  Kraft  durch  Iff""'"  ÜSP-M-)»  «■*■'«■  .■  •"'•  «'l'-i Ma  hat,  mir  die  Macht  des  guten  Sinns  I  "'■'»■  53-  ')  m.t  Inhaltsakk.: /««ir,™ zu  teil  werden  wird"  V.49.4.  ipmqm  smzatia  (sSPrM.)  a,„  'die  erste
KompA.  -  ai.  ,f*fl™«-  m.  ■Hitie',  np.  iw™  !  Klage  klagtet." Vt-/". 57 ;  58,  59.      a)  mit 'heiss'.  —  PQ.;  garvi,  gatmat.  '  Dat.  derPerson:  ta  »X'jil  *mainyJui  iiialiyil
.  p.  garma-pada-  n.,  GS.  mit  nah-  m.' '•'"'■'  «''."''''  J«'*""*'»  e"-'«  "diese Name  eines  Monats'):  -Myl  mliyHtd.)  Wo'te  meines  Geistes  klage  ich  euch, Bh  r  II    9  I    7  o  ^/.,  und  dem  /l."  Y.^2.g.
n.d.  JO„.ir  de.  e,.,..  (Mi,.  Ap,.)."-  S,  n.Ü  ,  :-;.-;,"nV"J,,rt  'IS'.';,™  "ifj*: —  0  IlTiiL.  KZ.  2JJ.  aSi.  S  ///.  I  b.  FaUch MiLr.s  G,  483,  504.  —  'i  Der  Inhalt  der  Klaye gehl  voraus.  —    J)  S  5J  I-  S-    -    '>  D«'  I""
=====
'garaJa-
gufra-
5*4
haca  "StfCa  ". ,  aus  der  Höhle  der  Dr"  \  •  g.  ganbiim  Inf.  'festzuhalten  an  — ' ^•3-T>  — yat  .  .  paiii  fra^stim  bavainli ,  {Wk.):  ahyä  vatthlus  manatihs  syaoiiann anrS.mainyavanqm  'tarn  (GP.  als  Subj.) ,  vaocat  g"  huxralus  sp?iitamcä  ärmaittm "v/o  es  am  meisten  Höhlen  .  .  gibt"  V.rfoMr/»(sd.)  "an  dieses  guten  Sinnes  Werken j,  loj  22  (als  Ob].); —  'öaF.21.  ■  hat  der  Einsichtige  festzuhalten  erklärt  und
VeI.Pü.  111  ,cJrjJj.*jr^/.i-.— ai, ^7-^(7- m. 'inneres  I  an  der  heiligen  Arm.  .  ."  Y.  j4.io'>.
■  ■  ■<■  (wozu  WklPh.  I       Zum  V.  ip-ai-.  — Vgl.  it^i^jmoj-. —  Pü.t  ^'Irfl.
-  ')  Vgl.  iSI.  KZ.  J5.  93.  JAOS.  ?/.  i22.
•  j,  *gar3buS-''  n.  'Junges'  eines  Tiers:
■  '^'^'»f'.yt--'5-_47-   \pasSus  'bus  anumayeheyi.f).%%; — pasSu^
mach,  Haus'.  -
i8g8.    1060),  erl. ;  sürSx  i  xrafsir.
►  j.    "garaäa-   Adj.   'gierig,   hastig':
'jdhra
■  Adj.    „bus  yvistahe  (sd.)  A.^.3.
Vgl.  sS.särbha-m.,  nhd.  *fl/*.  —  Pü.:  transskr.; weileres  s.  bei  DsT.  ZA.  3.  730.  —  O  So  Jp  l, •"2,  F2,  Jm4  usw.;  XA.  ^-n«*-.
garazä-  t  'Klage':  paoiryqm   'sqm gsrssacfa  (sd.)  asÜ  \t.  ij. 57;  58,  59.
Zum  V.  ganz-,  —  np.  S'la  'Klage'.
•  j.   garazäna-  Adj.  (fem.  •«:/■),  PPNL:
g.   garazday-  f  'Inbesitznehmen;  Be- kommen': yqm   ..   isyqm  dtltü   ..   ahurö
•  j.  garaSö-karata-  Adj.  'die  Galle  heraus- schneidend"':    kat    tä    tiara  yaozdayqn aiih>n  .  .  ya  rrasiuin  franuharat  sänS  i  "   ' para.iristahe  masyelu  väl  .  .  ayaozäayqn  ■ atihm  . .  lalJ'a  narS  'l^sca  (NPm.)  z^maö.- k?ntas^a  taica  tiarS  spiti.dsi'^ra  casmanal  * haca  itilbar>nti  "Sind  die  Männer  zu  pui fiziren,  die  .  .?  .  .  Sie  sind  nicht  zu  put fiziren,   und   (ebensowenig)   die  Männer, '
die  die  Galle  und  die  das  Herz  (aus  dem' Jir/cJ/Csd.)  "ä^«  Y.5/.17;  —  ai*hudäi. Hunde-  oder  Menschenleichnam)  heraus-  iVa/w  (sd.)  'dJ  (LS.)  Ryim  Y.50. 9. schneiden,  und  (ebensowenig)  die  Männer, '     Zum  v.  ,i,™vfl^-i   %  S3}-    Kig. 'Antreten'.  — (die  ihnen)  die  Augäpfel  aus  der  Augen- 1     ^"-  (''K"-)'  .?"■■".  X''fl"'- höhle  herausreissen"  V./.isf.".  E-  S"-nm-%  lies,^«*™-.
```


## [2026-09-06T14:55:03.809Z] TOOL CALL #36: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T14:55:03.815Z] TOOL RESULT

```


```


## [2026-09-06T14:55:05.711Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON dolfin\"; grep -n \"دلفین\\|دلفين\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10; echo \"=== MON pul\"; grep -c \"\" MON_part1.txt"
}
```


### [2026-09-06T14:55:05.819Z] TOOL RESULT

```
=== MON dolfin
MON_part2.txt:44118:دلفین. ماهیان (ماهی‌ها): (ج. ماهی | (جان.) 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:44118:دلفین. ماهیان (ماهی‌ها): (ج. ماهی | (جان.) 
=== MON pul
99339
```


## [2026-09-06T14:55:08.645Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '44110,44130p' MON_part2.txt"
}
```


### [2026-09-06T14:55:08.693Z] TOOL RESULT

```
سیاه رنگ این حیوان ساخته می‌شود. ضح.- 
کف درا که در نقاشی و دارو سازی و غیره 
مورد استعمال دارد عبارت از صدف انواع 
ماهی مرکب است که در زیر بوست بدن 
ان و کر تا شین آ نها فزار وارد: 
ماهی مومکث: (جاد.) یکی از گونه‌های ماهی 
ساردین است. ماهی بونس: (اخ.) ماهبی که 
طبق روایات یونس(ع) را بلعید. (جاذ.) 
دلفین. ماهیان (ماهی‌ها): (ج. ماهی | (جان.) 
رده‌ای از جانوران که آسزی هستند و 


فرهنکگ فارسی معین 


۱ ۱ 
بست‌ترین ذی‌فقاران شمار می‌آیند. وجود 
برانشی در دورة نمو جنینی بقیه حیوانات 
ذی‌فقار از جمله اسان و همجنین صفات 
دیگری که ذی‌فقاران عالی در دورهة جتنی 
نشان می‌دهند ابت می‌کند که ماهیان اجداد
```


## [2026-09-06T14:55:10.595Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%88%D9%84",
 "prompt": "Give the full Persian etymology section for پول (pul) 'money' — what origin is given (Greek obolos? Middle Persian? other), and any cited references (Hasandust, Horn, etc.)."
}
```


### [2026-09-06T14:55:17.910Z] TOOL RESULT

```
# Persian Etymology of پول (pul)

According to the Wiktionary entry, the Persian word پول (pul) meaning "money" has the following etymological origin:

**Source Language:** The term derives from Middle Persian *pōl, potentially borrowed from Ancient Greek ὀβολός (obolós).

**Cited Reference:** The entry provides one citation:
- A reference to an Iranica Online article on "Greece-xiv" at http://www.iranicaonline.org/articles/greece-xiv

The entry does not cite specific scholars like Hasandust or Horn. The etymology section is relatively brief, presenting the Greek origin as a possibility ("perhaps a borrowing") rather than a definitive conclusion, and the single reference points to a general article about Greek-Persian connections rather than a specialized etymological study.
```


## [2026-09-06T14:55:23.414Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D9%84%D8%B3",
 "prompt": "Give the Arabic etymology sections for فلس (fals) — the coin, and the fish-scale sense. What origin is given (Greek φόλλις / Latin follis? Greek obolos?) and what references are cited? Also anything on أفلس / مفلس / فلوس."
}
```


## [2026-09-06T14:55:26.143Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BD%80%CE%B2%CE%B5%CE%BB%CF%8C%CF%82",
 "prompt": "Give the Ancient Greek etymology for ὀβελός 'spit' and for ὀβολός — what origin do modern sources (Beekes) give? Is it connected to PIE *gʷelH- 'to pierce' or is it Pre-Greek? Also mention ὀβελίσκος."
}
```


### [2026-09-06T14:55:30.329Z] TOOL RESULT

```
# Etymology of فلس (fals)

## Coin Sense

The coin meaning traces back through a borrowing chain: **Aramaic פּוּלְסָא (puləsā) ← Ancient Greek φόλλις (phóllis) ← Latin follis**. The page shows this is ultimately derived from "Proto-Indo-European *bʰelǵʰ-".

## Fish-Scale Sense

The fish-scale meaning comes from "Ancient Greek φολίς (pholís)", a different Greek etymon than the coin sense.

## Related Terms

The entry documents derived words:
- **فَلَّسَ** (fallasa) — "to bankrupt"
- **أَفْلَسَ** (ʔaflasa) — "to become bankrupt"
- **إِفْلَاس** (ʔiflās) — "bankruptcy"
- **مُفَلِّس** (mufallis) — active participle
- **فُلُوس** (fulūs) — plural form, used colloquially to mean "money"

## Citations

The references section cites classical Arabic lexicographers (Lane, Freytag, Kazimirski) and modern sources (Wehr's dictionary), but does not cite sources distinguishing between the two Greek etymologies or providing additional etymology details beyond the basic chain.
```


### [2026-09-06T14:55:31.396Z] TOOL RESULT

```
# Etymology of ὀβελός and ὀβολός

According to the Wiktionary source, the origin of ὀβελός remains uncertain. The entry states that it is "Possibly an alteration of _βέλος_ (bélos, 'missile'), but the initial vocal cannot be accounted for."

Modern scholarship, particularly Beekes and Furnée, concludes that "the word is clearly Pre-Greek" rather than connected to Indo-European roots like *gʷelH-.

## Related Terms

The article notes that ὀβολός functions as an alternative form of ὀβελός. Additionally, **ὀβελίσκος** (obelískos) is listed as a derived term, representing a diminutive formation from the base word.

The Pre-Greek classification suggests this vocabulary entered Greek through substrate influence rather than through inherited Indo-European etymology, making reconstruction to PIE origins problematic.
```


## [2026-09-06T14:56:09.987Z] TOOL CALL #42: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py"
}
```


### [2026-09-06T14:56:10.039Z] TOOL RESULT

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


## [2026-09-06T14:56:11.143Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT obelisk\"; grep -n -i \"obelisk\\|obelus\\|obol\" SKT.txt | head -10; echo; echo \"=== AHD root article gwelbh\"; grep -n \"womb; young of an animal\\|young of an animal\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-06T14:56:11.214Z] TOOL RESULT

```
=== SKT obelisk
12560:Obelisk ;  see  Oboltu.
12576:ObolUB,  a  small  Uk.  coin.  (U-Gk.) L.  ff^w/.  — Gk.  60oX6t,  a  small  coin.  per> haps  orig.  in  the  shape  of  a  spike  or  nailv silted  to  Ck.  i>$oM.  a  s^
12582:obelisk.  (F.  -  L.  -  Gk.)  O.  F.  oheiisjut. ^X^ohtliicum.  ncc.  ol cifelLscHj.^QV.  iff*- kiaitM,  a  pointed  spit ;  hence  a  thin  poluted pillar;  Oiinin.  of  d^iA^s,  a  ipit
16339:Sable,  an  animal.  (F.-Slavonic.)  O.F. table.  —  Rusa.  sobole^  the  snble ;  also  a  fur- tippet.  %  \>  black  sable  was  tc^t  liked, the  word  sad/e  also  means  '  black.*

=== AHD root article gwelbh
814:fana, flag, banner, weathercock: VANE; b. compound *gund-fanon-, “battle-flag” (see ghen-'). 2. Extended form *panno- in Latin pannus, piece of cloth, rag: PANE, PANEL. 3. Possibly Greek pénos, web (> Latin pdnus, a swelling): PANICLE. [Pok. pan- 788.] [pandoura. Three-stringed lute. Greek noun of obscure origin. BANDORE, MANDOLIN, PANDORE.] pant-. All. Attested only in Tocharian and Greek. Greek pas (neuter pan, stem pant-), all: PAN-, PAN; DIAPASON, PANCRATIUM, PANCREAS. [In Pok. 1. keu- 592.] pap-'. Teat (sound symbolism). Probably the same word as pap-2. 1. Middle English pap(pje, nipple: Pap}. 2. Latin diminutive papula, pimple (diminutive papilla, nipple): PAPILLA, PAPULE. 3. Variant form *pup(p)- in Latin piipus, boy, and pupa, girl: puPA, PUPIL. [In Pok. barb- 91.] pap-?. Food (baby-talk root). Reduplication of pa-. 1. Germanic nasalized form *pamp- in Flemish frequen- tative pamperen, to cram with food, akin to the source of Middle English pamperen, to pamper: PAMPER. 2. Latin pappa, food (> Middle English pap, soft food): PAP?, POPPYCOCK. [Pok. pap(p)a 789, ba*mb- 94.] papa. A child’s word for “father,” a linguistic near-uni- versal found in many languages. 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.] paso-. Kinsman by marriage. Latin parri- (for pari-) in compound parri-cida (oldest form paricidas), murderer of a near relation: PARRICIDE. [Pok. pdso-s 787.] past-. Solid, firm. 1. Germanic *fastuz, firm, fast, in: a. Old English fest, fixed, firm: FAST!; STEADFAST; b. Middle Dutch vast, firm, fast: AvAST. 2. Germanic *fastinon, to make firm or fast, in Old English festnian, to fasten, establish: FASTEN. 3. Germanic *fastén, to hold fast, observe abstinence, in: a. Old English festan, to abstain from food: rasT?; b. Old Norse fasta, to abstain from food: BREAKFAST. [Pok. pasto- 789.] pau-. Few, little. I. Adjectival form *pau-, few, little. 1. Germanic *fawaz in Old English féawe, few: FEW. 2. Suffixed form *pau-ko- in Latin paucus, little, few: PAUCITY, POCO. 3. Suffixed form *pau-ro- in metathetical form *par-wo- in Latin parvus, little, small, neuter parvum, becoming parum, little, rarely: PARAFFIN, PAR- vovirus. 4. Compound “pau-paros, producing little, poor (*par-os, producing; see pere-'), in Latin pauper, poor: PAUPER, POOR, POVERTY. II. Suffixed reduced variant form “pu-lo-, young of an animal. 1. Germanic *fulén- in Old English fola, young horse, colt: FOAL. 2. Germanic derivative *fuljé in Old Norse fylja, female colt: FILLY. 3. Latin pullus (probably with expressive gemination), young of an animal, chicken: POLTROON, PONY, POOL?, POULARD, PULLET; CATCHPOLE. III. Basic form *pau- and variant form *pi-, boy, child. 1. Suffixed form *pu-ero- in Latin puer, child: PUERILE, PUERPERAL. 2. Suffixed form “pi-sso- in Latin piisus, boy: PUSIL- LANIMOUS. 3. Suffixed form *paw-id- in Greek pais (stem paid-), child (> paideia, education): PEDO-?; ENCY- CLOPEDIA, ORTHOPEDICS. [Pok. pdu- 842.] paus-. To leave, desert, cease, stop. Greek pauein, to stop (> Latin pausa, a stopping): PAUSE, (PESADE), (POSE!); COMPOSE, DIAPAUSE, (REPOSE!). [Pok. paus- 79.] ped-'. Foot. I. Nominal root. 1. Lengthened o-grade form *pod- in Germanic *fot- in Old English fot, foot: Foor. 2. Suffixed form *ped-ero- in Germanic *feteré in Old English fetor, feter, leg iron, fetter: FETTER. 3. Suffixed form *ped-el- in Germanic *fetel- in Old High German vizzelach, fetlock, akin to the Germanic source of Middle English fitlock, fetlock, fetlock: FETLOCK. 4. Basic form *ped- in Latin pés (stem ped-), foot: PAWN2, -PED, PEDAL, PEDATE, PEDESTRIAN, PEDI-, PEDICEL, PEDUNCLE, (PEON), PES, PIONEER; MILLIPEDE, SESQUIPEDALIAN, TRIPEDAL, TRIVET, VAMP!. 5, Form *ped-yo- in: a. Latin expedire, to free from a snare (ex-, out of; see eghs): EXPEDITE; b. Latin impedire, “to put in fetters, hobble,
840:per-3. The young of an animal (< “a bringing forth,” “offspring”), Derivative root belonging to the group of per'. Suffixed o-grade form *por-si- in Germanic *farzi-, young cow, in Old English fearr, calf, and compound heahfore, calf (first element obscure): HEIFER. [In Pok. 2. D. per 818.]
```


## [2026-09-06T14:56:18.245Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\noff=0\nfor i,p in enumerate(pages):\n    if 'ObolUB' in p or 'Obelisk ;' in p:\n        print('leaf',i,'-> printed', i-20)\nEOF\necho \"=== AHD elbh\"; grep -n \"elbh-\" AHD_watkins1985.txt | head"
}
```


## [2026-09-06T14:56:19.651Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if 'calf,  n.,  young  of  a  cow' in p:\n        print('calf leaf',i)\n    if 'obelus,  n.,  a  mark' in p:\n        print('obelus leaf',i)\nEOF"
}
```


### [2026-09-06T14:56:20.076Z] TOOL RESULT

```
leaf 336 -> printed 316
=== AHD elbh
153:Internal organs were also named in Indo- European times, including the womb (g“elbh-), gall (ghel-?), brain (mregh-mno-, confined to Low German and Greek), spleen (spelgh-), and liver (yekr). The male sexual organs, pes- and ergh-, are common patri- mony, as is ors-, “backside.”
377:dapper, heavy, strong; later quick, nimble: DAPPER. [Pok. dheb- 239.] dhegvh-. To burn, warm. Suffixed o-grade form *dhogvh- eye- in Latin fovére, to warm, cherish, foment (> fomen- tare, to foment, and fomes, tinder): FOMENT, FOMITE. [Pok. dhegth- 240.] dh@(i)-. To suck. Contracted from *dheoa(i)-. 1. Suffixed reduced form *dhé-mnd- in Latin fémina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- in Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dhyd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High German teic, dough: TEIGLACH. 4. Suffixed zero-grade form *dhigh-ird, in Latin figira, form, shape (< “result of kneading”): FIGURE; CONFIGURATION, DISFIGURE, PRE- FIGURE, TRANSFIGURE. 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: (FAINT), FEIGN, (FEINT), FICTILE, FICTION, FIGMENT; EFFIGY. 6. Nasal- ized zero-grade form *dhi-n-g(h)- in Greek thinganein, to touch: THIGMOTAXIS, THIXOTROPY. 7. Suffixed o-grade form *dhoigh-o- in Avestan daéza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English dell, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended
539:g”elbh-
540:(COVEN), (COVENANT), EVENT, INTERVENE, INVENT, MIS- ADVENTURE, PARVENU, PREVENIENT, PREVENT, PROV- ENANCE, (PROVENIENCE), REVENANT, REVENUE, SOUVENIR, SUBVENTION, SUPERVENE. 3. Suffixed zero-grade form *gvm-yo- in Greek bainein, to go, walk, step, with basis (< *gm-ti-), a stepping, tread, base, and -batés (< *gwa-to-, zero-grade of gd-, contraction of *gaa-), agential suffix, “one that goes or treads, one that is based”: BASE!, BASIS; ABASIA, ACROBAT, ADIABATIC, AMPHISBAENA, ANABAENA, DIABASE, DIABETES, STEREO- BATE, STYLOBATE. 4, Suffixed zero-grade form “g“(g)-u- in compound form “pres-gu-, “going before” (see per’). 5. Basic form *gvd- in Greek béma, step, seat, raised platform: BEMA. 6. Sanskrit jigdti, he goes: JUGGER- NAUT. [Pok. g¥d- 463.] gvadh-. To sink. Possible root. 1. Suffixed form *guadh-u- in Greek bathus, deep (> bathos, depth): BATHOS, BATHY-. 2. Greek benthos, depth, may be formed on bathus by analogy with penthos, grief, and pathos, passion, suffering (or it may be from an unrelated root *g¥(e)ndh-): BENTHOS. 3. Suffixed variant form *gudh-yo- in Greek bussos, bottom of the sea: ABYSS. [Pok. gddh- 465.] g’ébh-'. To dip, sink. Suffixed zero-grade form *gvabh-yo- in Greek baptein, to dip: (BAPTIST), BAPTIZE; ANABAPTIST. [Pok. g¥ébh- 465.] g”ébh-2. Hypothetical base of some Germanic words associated with the notion of sliminess. 1. Middle Dutch quac-, unguent, liquid, in obsolete Dutch quacksalver, quacksalver: QUACKSALVER. 2. Low German quabbeln, to shake like jelly, tremble, akin to Middle English quaven, to tremble: QUAVER. [Pok. 2. g¥ébh- 466.] grei-. Also gveia-. To live. I. Suffixed zero-grade form *gwi-wo-, *gi-wo- (< *gi9-wo-), living. 1. Germanic *kwi(k)waz in: a. Old English cwic, cwicu, living, alive: QUICK, QUICKSILVER; b. as a name for couch grass (from its rapid growth), in Old English cwice, couch grass: (COUCH GRASS), QUITCH GRASS. 2. a. Latin vivus, living, alive: VIVIFY, VIVIPAROUS; b. Latin denominative vivere, to live: VIAND, VICTUAL, VIVA, VIVACIOUS, VIVID; CON- VIVIAL, REVIVE, SURVIVE. 3. Further suffixed form *gvi- wo-td in Latin vita, life: VIABLE, VITAL; LIGNUM VITAE, VITAMIN. II. Suffixed zero-grade form *gia-o- in Greek bios, life (> bioté, way of life): BIO-, BIOTA, BIOTIC; AEROBE, AMPHIBIOUS, ANABIOSIS, CENOBITE, MICROBE, RHIZOBIUM, SAPROBE, SYMBIOSIS. III. Variant form *gwyd- (< *gvyoo-). 1. Greek z0é, life: AzO-, (DIAZO). 2. Suffixed form *gvy6-yo- in Greek zdon, zdion, living being, animal: (-Z0A), -ZOIC, ZOO-, ZOON, -ZOON. IV. Pre- fixed and suffixed form *su-g~ia-es- (*su-, well; see su-), “living in good condition,” in Greek hugiés, healthy: HYGEIA, HYGIENE. [Pok. 3. gei- 467.] g”eia-. To press down, conquer. Sanskrit jayati, he con- quers: JAIN. [Pok. gveio- 469.] gvel-'. To pierce. 1. Suffixed o-grade form “gvol-eyo- in Germanic *kwaljan in Old English cwellan, to kill, destroy: QUELL. 2. Suffixed zero-grade form *g“/-yo- in Germanic *ku/jan in Old English *cyllan, to kill, perhaps the source of Middle English killen, to kill: KILL}. 3. Full-grade form *gvel- in Greek beloné, needle: BEL- ONEPHOBIA. [Pok. 1. g¥el- 470.] gel-2. To fly; a wing. Possibly in Latin voldre, to fly: VOLANT, VOLATILE, VOLE2, VOLITANT, VOLLEY. gvel-3, To swallow. Dissimilated to *gel-. 1. Germanic *kel- in Old English ceolu, throat, dewlap, perhaps akin to Middle English cholle, throat: JowL?. 2. Germanic *keluz in Old Norse Aj6ir, keel: KEEL}. 3. Suffixed zero-grade form “gul-d in Latin gula, gullet, throat, palate: GOLIARD, GULAR, GULES, GULLET. 4, Extended (expressive) form *glutt- in: a. Latin gluttire, gliitire, to swallow: GLUT; DEGLUTITION; b. Latin glutté, a glutton: GLuTTon. [In Pok. 2. gel- 365.] gvelbh-. Womb. 1. Suffixed form *gvelbh-u- in Greek delphus, womb, whence delphis, dolphin (referring to its
542:shape): DELPHINIUM, DOLPHIN. 2. Prefixed and suffixed form *sm-gvelbh-o-, “born of one womb” (*sm-, one; see sem-'), in Greek adelphos, brother: -ADELPHOUS. [Pok. gtelbh- 473.] gvele-1. To throw, reach. Variant *g/é-, contracted from *guleg-, 1. Suffixed zero-grade form *g/-n-o- in: a. Greek ballein, to throw (with o-grade *bol- and variant *b/é-): BALLISTA; AMPHIBOLE, ASTROBLEME, CATABOLISM, DEVIL, (DIABOLIC), (EBLIS), ECBOLIC, EMBLEM, EPIBOLY, (HYPERBOLA), HYPERBOLE, METABOLISM, (PALAVER), PARABLE, (PARABOLA), (PARLEY), (PARLIAMENT), (PAR- LOR), (PAROL), (PAROLE), PROBLEM, SYMBOL; b. Greek ballizein, to dance: BALL?, (BALLAD), (BALLET), BAYA- DERE. 2. Suffixed o-grade form *gvols-d in Greek bolé, beam, ray: BOLOMETER. 3. Suffixed o-grade form *gwolo-sdé in Greek boulé, determination, will (< “throw- ing forward of the mind”), council: BOULE!; ABULIA. 4. Suffixed variant zero-grade form *gvele-mno- in Greek belemnos, dart, javelin: BELEMNITE. [Pok. 2. g¥el- 471.] gwela-2, An acorn. 1. Suffixed zero-grade form *g¥/o-nd- in Latin gldns (stem gland-), an acorn: GLAND, GLAN- DERS, (GLANDULAR), GLANS. 2. Suffixed zero-grade form *gulg-no- in Greek balanos, acorn, date: VALONIA; MYRO- BALAN. [Pok. 3. gvel- 472.] gven-. Woman. 1. Suffixed form *gven-d- in: a. Germanic *kwen6n- in Old English cwene, woman, prostitute, wife: QUEAN; b. Old Irish ben (> Irish Gaelic bean), woman: BANSHEE; C. Persian zan, woman: ZENANA. 2. Suffixed lengthened-grade form *gvén-i- in Germanic *kwéniz, woman, wife, queen, in Old English cwén, woman, wife, queen: QUEEN. 3. Suffixed zero-grade form *g“n-d- in Greek guné, woman: GYNO-, -GYNOUS, -GYNY; GYNAE- CEUM, GYNECOCRACY, (GYNECOLOGY), POLYGYNY. [Pok. gvend 473.) g”ere-'. Mountain. Possibly o-grade form *gvors- in: a. Greek boreios, “coming from the north” (? < “coming from the mountains of Thrace, north of Greece”), whence Boreas, the north wind: Boras; b. Greek Huperboreioi, Huperboreoi, name of a people living in the far north, variously explained as “they who live beyond the north wind” and “they who live beyond the mountains” (hu- per-, beyond; see uper): HYPERBOREAN. [Pok. 3. gver- 477.) gvere-2. Heavy. I. Zero-grade form *gra-. 1. Suffixed form “g“ra-u-i- in Latin gravis, heavy, weighty: GRAVE?, GRAVID, (GRIEF), GRIEVE; AGGRAVATE, AGGRIEVE. 2. Suffixed form “gro-u- in: a. Greek barus, heavy: BARITE, BARITONE, (BARIUM), BARYON, (BARYSPHERE), BARYTA; b. Sanskrit guru-, heavy, venerable: GURU. 3. Suffixed form *gro-es- in Greek baros, weight: BAR?, BARO-; CENTROBARIC, ISALLOBAR, ISOBAR. 4. Possibly *guri- in Greek bri- in compound *u(d)-bri- (see ud-). II. Suffixed extended form *g-rii-to- in Latin britus, heavy, unwieldy, dull, stupid, brutish: BRUT, BRUTE. III. Suffixed extended form *g»ri-g- in: a. Celtic *brig-o-, strength, in Italian brio, vigor: BRIO; b. Germanic *krig- in Old High German krég, chrég, stubbornness (> Ger- man Krieg, war): BLITZKRIEG, SITZKRIEG. IV. Suffixed full-grade form *gvero-nd-, millstone, in Old English cweorn, quern: QUERN. [Pok. 2. g¥er- 476.] gvere-*. To praise (aloud). 1. Suffixed zero-grade form *gvra-to- in Latin grdtus, pleasing, beloved, agreeable, favorable, thankful: GRACE, GRATEFUL, GRATIFY, GRATIS, GRATITUDE, GRATUITY; AGREE, CONGRATULATE, IN- GRATE, INGRATIATE. 2. Suffixed zero-grade form *gwro-do-, “he who praises,” in Celtic bardo-, bard, in Welsh bardd and Scottish and Irish Gaelic bard, bard: BARD}. [Pok. 4. gver(a)- 478.] gvere-4. To swallow. 1. Possibly suffixed extended form *gro-gh- in Germanic *krag-, throat, in: a. Old English *craga, throat, possible source of Middle English crawe, craw: CRAW; b. Middle Dutch craghe, throat: scrac. 2. Suffixed o-grade form *gvor-d- in Latin vordre, to swallow up: VORACIOUS, -VOROUS; DEVOUR. 3. Expres-
1217:ADDER nétr- ADDICT deik- ADDUCE deuk- -ADELPHOUS gWelbh- ADEMPTION em- ADENO- engW- ADEPT ap-1 ADHERE ghais- ADIABATIC gWa- ADIEU delw- ADIT ei-1 ADJACENT yé- ADJECTIVE yé- ADJOIN yeug- ADJOURN deiw- ADJUDICATE yewes- ADJURE yewes- ADJUST yeug- ADJUVANT ad- ADMIRE smei- ADMIT (s)meit(9)- ADMIX meik- ADMONISH men-t ADNATE gene- ADNEXA ned- ADO ad- ADOLESCENT al-3 ADOPT op-2 ADORE Or- ADORN ar- ADRENERGIC werg- ADSCITITIOUS skei- ADSORB srebh- ADULT al-3 ADULTERATE al-1 ADULTERINE al-1 ADULTERY al-1 ADUMBRATE andho- ADUST eus- ADVANCE ant- ADVECTION wegh- ADVENT gWa- ADVENTITIOUS gWa- ADVENTURE gWa- ADVERB wer-6 ADVERSE wer-3 ADVICE weid- ADVISE weid- ADVOCATE wekw- AECIUM weik-3 AEDES swad-
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1432:DOGE deuk- pocMa dek-1 pDoGMaTIC  dek-! DOIT twei- DOLABRIFORM del-3 DOLCE dik-u- DOLDRUMS_ dheu-t DOLE! dail- DOLE? del-3 DOLERITE del-2 DOLICHOCEPHALIC del-1 DOLICHOCRANIAL  del-1 DOLOR del-3 DOLPHIN gWelbh- Dott dheu-1 Dom deme-1, dhé-1 DOMAIN deme-! DOME deme-1 DOMESTIC deme-1 DOMICILE deme-! DOMINATE deme-1 DOMINICAL deme-1 DOMINIE deme-1 DOMINION deme-' DOMINO! deme-1 DOMINO2 deme-1 DONATION d6- DONATIVE d6- DONOR do- poom dhé-1 pooR dhwer- DOPE dub- DORMANT drem- DORMER drem- DORMITORY drem- DORSAL dorsum poRrsO- dorsum pory? aurum DOSE dé-
1435:DRONE! dher-3 DRooP dhreu- DROP dhreu- DROPsY wed-1 DROSHKY dhragh- DRoss_ dher-1 DROUGHT dreug- DROVE? dhrelbh- DROWN dhreg- DROWSE dhreu- DRUID deru DRUPE deru, pekw- DRY dreug- DRYAD deru DUAD dwo- DUAL dwo- DuB! dheubh- DUB? dheubh- DUBIOUS dwo- DUCAL deuk- DucaT deuk- DUCHESS deuk- DUCHY deuk- Duct deuk- DUCTILE deuk- DUDEEN dheu-1 DUE ghabh- DUEL duellum DUENNA deme-1 DUET dwo- DUKE deuk- DukHoBoR_ bher-2, dheu-! DULCET dik-u- DULCIFY dik-u- DULL dheu-! Duma dhé-1 DUMB dheu-1 DUMP dub- pDuN2 dheu-? DUNDERHEAD (s)tene- DUNE dhino- DUNGEON deme-1 DUNK teng- DUO- dwo- DUODECIMAL dekm, dwo- DUOPSONY wes-1 DUPLE dwo- DUPLEX dwo- DUPLICATE dwo- DUPLICITY dwo- DURABLE deue- DURA MATER deru DURAMEN deru DURANCE deue- DURATION deue- DURBAR dhwer- DURESS deru DURING deue- DURST dhers- DURUM deru Dusk dheu-! Dust dheu-' DutTcH teuta- DUTY ghabh- DUUMVIR wi-ro- DUVETYN dheu-! DWELL dheu-! DWINDLE dheu-3 DYAD dwo- DYNAMIC deu-2 DYNAMITE deu-2 DYNAST deu-2 DYNASTY deu-2 Dys- dus- DYSENTERY en DYSLEXIA leg-1 DYSMENORRHEA mé-2 DYSPEPSIA pekw- DYSPLASIA pele-2 DYSPNEA pneu- DYSPROSIUM ei-1
```


### [2026-09-06T14:56:21.913Z] TOOL RESULT

```
leaves 903
calf leaf 128
obelus leaf 570
```


## [2026-09-06T14:56:36.643Z] TOOL CALL #46: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(d['KLN']['page_offset']); print('---'); print(d['KLN'].get('lookup_hint'))\nprint('=== SKT'); print(d['SKT'].get('lookup_hint'))\nprint('=== TAD'); print(json.dumps(d['TAD'],ensure_ascii=False)[:900])\n\""
}
```


## [2026-09-06T14:56:36.707Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"CALF\\b\" AHD_watkins1985.txt | head -3"
}
```


### [2026-09-06T14:56:38.522Z] TOOL RESULT

```
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
---
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
=== SKT
Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
=== TAD
{"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"], "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the pa
```


### [2026-09-06T14:56:38.569Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T14:56:50.500Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (128,253,546,570):\n    p=pages[i].strip()\n    print('=== leaf',i, '| first 200:', p[:200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T14:56:52.258Z] TOOL RESULT

```
=== leaf 128 | first 200: ia and  adj.  suff.  -ate  and  cp.  discalceate. calced calccd,  adj.,  calceate.  —  Formed  with  stiff,  -ed fr.  L.  calceus ,  ‘shoe’.  See  next  word. Calceolaria,  n.,  a  genus  of  plants  
=== leaf 253 | first 200: cent  and  cp. words  there  referred  to. Derivatives:  dispers-al,  n.,  dispers-ed-ly,  adv., dispers-ible,  adj.,  dispers-ibil-ity,  n.,  dispersion (q.v.),  dispers-ive,  adj.,  dispers-ive-ly, 
=== leaf 546 | first 200: appoint,  something;  to  have  room; to  be  able;  to  be  obliged’,  d-degree  of  I.-E.  base med-,  ‘to  measure,  limit’,  whence  OE.  metan,  ‘to measure’.  See  mete,  ‘to  measure',  and  cp
=== leaf 570 | first 200: sexual  desire  in  women (med.)  —  Medical  L.,  compounded  of  nympho- and  Gk.  (tavtoe,  ‘madness,  frenzy'.  See  mania. Derivative:  nymphomani-ac,  adj.  and  n. Nyssa,  n.,  a  genus  of  pl
```


## [2026-09-06T14:57:12.836Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (127,128,129,545,546,569,570,571):\n    p=pages[i]\n    nums=re.findall(r'\\b\\d{3,4}\\b',p)\n    print(i, nums[:12])\nEOF"
}
```


### [2026-09-06T14:57:14.635Z] TOOL RESULT

```
127 ['220', '221', '139', '1961', '196', '202', '1750']
128 ['1907', '1795', '1871', '222', '1788', '1829', '223', '164', '1435', '064']
129 ['224', '225', '202']
545 ['1707']
546 ['1021']
569 ['1064']
570 ['1066']
571 ['1067', '1068', '131']
```


## [2026-09-06T14:57:25.043Z] TOOL CALL #50: Bash

```json
{
 "command": "grep -ho \"Klein 1966 p\\.[0-9]*[^\\\"]\\{0,60\\}\" data/verification/page-2*.json | head -20; echo ====; grep -ho \"\\\"ref\\\": \\\"KLN:[0-9]*\\\", \\\"status\\\": \\\"[a-z_]*\\\"\" data/verification/page-20*.json | head"
}
```


### [2026-09-06T14:57:25.626Z] TOOL RESULT

```
Exit code 1
Klein 1966 p.1288 s.v. quick
Klein 1966 p.1288 s.v. 'quick': 'fr. Teut. *qwiqwa-, \
Klein 1966 p.1288 s.v. quicksilver
Klein 1966 p.1288 s.v. quick
Klein 1966 p.1288 s.v. quick
Klein 1966 p.~960 s.v. microbe (KLN_1966.txt line 23818)
Klein 1966 p.1288 s.v. quick
Klein 1966 p.1288 s.vv. quick, quicksilver
(eval):1: === not found
```


## [2026-09-06T14:57:26.360Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (570,571,572):\n    print('=== leaf',i)\n    print(pages[i][:1500].replace('\\n',' ')[:1500])\nEOF"
}
```


### [2026-09-06T14:57:28.329Z] TOOL RESULT

```
=== leaf 570
  sexual  desire  in  women (med.)  —  Medical  L.,  compounded  of  nympho- and  Gk.  (tavtoe,  ‘madness,  frenzy'.  See  mania. Derivative:  nymphomani-ac,  adj.  and  n. Nyssa,  n.,  a  genus  of  plants,  the  tupelo  (bot.)  — ModL.,  fr.  Gk.  vuaoa,  ‘turning  post’,  which  is of  uncertain  etymology.  It  is  possibly  rel.  to vuoaetv  ‘to  touch  with  a  sharp  point,  prick, stab’.  See  nutation. nystagmus,  n.,  involuntary  oscillation  of  the  eye¬ ball  (med.)  —  Medical  L.,  fr.  Gk.  vyorayp-oc, ‘drowsiness’,  fr.  vuoxa^Etv,  ‘to  be  sleepy,  to  be drowsy,  to  doze’,  which  is  cogn.  with  Lith. snaudziu,  sndusti ,  ‘to  slumber’. Derivative:  nystagm-ic,  adj. Nyx,  n.,  the  goddess  of  night  in  Greek  mythol¬ ogy.  —  Gk.  N6£,  personification  of  the  night. See  night. % I 1 O,  interj.,  an  exclamation  expressing  admiration surprise,  fear,  etc.  —  Common  to  most  lan¬ guages;  (cp.  e.g.  Gk.  <2>,  L.  6,  oh,  OSlav.,  Lith. o,  Goth,  0,  Du.,  G.  o,  F.  o,  OI.  a,  OIr.  a,  a); of  imitative  origin.  Cp.  oh. o’,  shortened  form  of,  1)  of,  as  in  o'clock,  or  2) (dial.)  on. -o-,  connective  vowel,  orig.  used  to  join  two  ele¬ ments  of  Greek  origin  on  the  analogy  of  Greek compounds  in  which  the  o  usually  belongs  to the  stem  of  the  first  element  (cp.  e.g.  Xsux6- 9’jXXoi;,  ‘white-leafed’,  7_ELp6-uxvxtg,  ‘diviner by  palmistry’),  or  represents  another  stem  vowel or  is  an  add
=== leaf 571
o  put  before’.  It derives  fr.  L.  objectus,  pp.  of  obicere  (less  cor¬ rectly,  objicere),  ‘to  throw  or  put  before  or against’,  fr.  ob-  and  jacere  (pp.  jactus),  ‘to throw’;  see  jet,  ‘to  spirt  forth'.  For  the  change of  Latin  a  (in  jactus)  to  e  (in  ab-jeclus)  see  accent and  cp.  words  there  referred  to. Derivative:  object-or,  n. object,  n.  —  ME.,  fr.  ML.  objectum,  lit.  ‘some¬ thing  thrown  before’,  neut.  of  L.  objectus,  pp.  of obicere  (see  object,  v.) ;  prop,  a  loan  translation of  Gk.  7rpo[3X7][ix  (see  problem ). Derivatives :  object-less,  adj.,  object-less-ly,  adv., object-less-ness,  n. objectification,  n.,  the  act  of  objectifying ;  the  state of  being  objectified.  —  See  next  word  and -ation. 1067 objectify,  tr.  v.,  to  make  objective;  to  materialize. —  Compounded  of  object,  n.,  and  -fy. objection,  n.  —  ME.  objeccioun,  fr.  OF.  (=  F.) objection,  fr.  Late  L.  objectionem,  acc.  of  ob- jectio,  ‘a  throwing  or  putting  before’,  fr.  L.  ob¬ jectus,  pp.  of  obicere.  See  object,  v.,  and  -ion. Derivatives:  objection-able,  adj.,  objection-abil¬ ity,  n.,  objection-able-ness,  n.,  objection-abl-y, adv.,  objection-al,  adj. objective,  adj.  —  ML.  objectivus,  fr.  objectum, ‘object’.  See  object,  n.  and  v.  and  -ive. Derivatives:  objective-ly,  adv.,  objective-ness,  n., objectivism  (q.v,),  objectivity  (q.v.) objective,  n.,  aim,  purpose.  — 
=== leaf 572
elligible’,  orig.  ‘cover¬ ed’,  formed  fr.  ob-  and  l.-E.  base  *(s)qeu-, *(s)qewa-,  ‘to  cover’,  whence  also  L.  scutum, ‘shield’,  ON.  sky,  OE.  sceo,  OS.  skio,  ‘cloud’.  See sky  and  cp.  words  there  referred  to.  Cp.  also the  second  element  in  chiaroscuro. Derivatives:  obscure,  n.,  obscure,  v.  (q.v.),  ob- scure-ly,  adv.,  obscure-ness,  n. obscure,  tr.  v.  —  Fr.  F.  obscurer,  fr.  L.  obscurare, ‘to  make  dark,  to  darken,  obscure’,  fr.  obscurus ; partly  directly  fr.  obscure,  adj.  (q.v.) obscurity,  n.  —  OF.  obscurite  (=  F.  obscurite), fr.  L.  obscuritatem,  acc.  of  obscuritas,  ‘dark¬ ness;  indistinctness,  uncertainty’,  fr.  obscurus. See  obscure,  adj.,  and  -ity. obsecrate,  tr.  v.,  to  entreat,  implore  ( archaic )  — L.  obsecratus,  pp.  of  obsecrare,  ‘to  beseech,  en¬ treat  (on  religious  grounds)’,  fr.  ob-  and  sacrdre, ‘to  make  or  declare  sacred’,  fr.  sacer,  ‘holy, sacred’.  See  sacred  and  verbal  suff.  -ate.  For  the change  of  Latin  a  (in  sacer)  to  &  (in  ob-sicrare) see  accent  and  cp.  words  there  referred  to. obsecration,  n.,  supplication,  entreaty.  —  L.  ob- secratio,  gen.  -onis,  ‘supplication,  entreaty',  fr. obsecratus,  pp.  of  obsecrare.  See  prec.  word  and -ion. obsequies,  n.  pi.,  of  obsol.  obsequy,  funeral  rites. —  ME.  obsequie,  obseque,  fr.  OF.  obseque,  ob- sequie,  fr.  ML.  obsequiae,  which  was  influenced in  meaning  by  a
```


## [2026-09-06T14:57:49.201Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'dolphin,  n.  —  ME.' in p or 'obol,  n.,  a  small' in p or 'obelisk,  n.,' in p:\n        nums=re.findall(r'\\b\\d{3,4}\\b',p)\n        print('leaf',i,'nums',nums[:10])\nprint('--- dolphin full')\nfor i in (258,259,260):\n    print(i, re.findall(r'\\b\\d{3,4}\\b',pages[i])[:8])\nEOF"
}
```


### [2026-09-06T14:57:51.393Z] TOOL RESULT

```
leaf 259 nums ['1796', '1860', '473', '1519', '1841', '1750', '1801', '474', '475', '1086']
leaf 570 nums ['1066']
leaf 571 nums ['1067', '1068', '131']
--- dolphin full
258 ['472']
259 ['1796', '1860', '473', '1519', '1841', '1750', '1801', '474']
260 ['1849', '1803', '014', '476']
```


## [2026-09-06T14:58:04.263Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(262,270):\n    nums=[n for n in re.findall(r'\\b\\d{3}\\b',pages[i]) if 460<=int(n)<=510]\n    print(i,nums, '|', pages[i].strip()[:90].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T14:58:06.370Z] TOOL RESULT

```
262 ['478', '479'] | —  See  doom  palm. dour,  adj.,  hard,  stern  ( Scot .)  —  L.  durus,  ‘hard’. See  dur
263 ['480', '481', '483'] | oth.  ( ga)tarhjan ,  ‘to  make  distinct’, OE.  torht,  ‘bright’,  OHG.  zoraht,  ‘clear’
264 ['484', '485'] | e,  ‘dregs,  lees’,  OHG. trestir,  MHG.,  G.  trester,  ‘grapeskins,  husks’, and  cogn. 
265 ['486'] | astis  and  in  lithontriptic. drop,  tr.  and  intr.  v.  —  OE.  dropian,  fr.  dropa, ‘
266 ['487'] | the  stem  of  L.  dux,  gen.  duds, ‘leader’.  See  duke  and  adj.  suff.  -al. Derivati
267 ['488', '489', '490', '491'] | re  referred  to. Derivatives:  dull,  tr.  and  intr.  v.,  dull-ard,  n., du/l-ish,  adj
268 [] | icatid,  ‘a  doubling’,  fr.  duplicatus,  pp.  of duplicare.  See  duplicate,  v.,  and  
269 [] | for  measuring  the magnifying  power  of  telescopes.  —  Com¬ pounded  of  dyna-  and  G
```


## [2026-09-06T14:58:25.256Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (178,438,748):\n    print(i, re.findall(r'\\b\\d{3,4}\\b',pages[i])[:12], '|', pages[i].strip()[:60].replace('\\n',' '))\n# locate 'dolphin' position in leaf 259\np=pages[259]\nidx=p.find('dolphin,  n.  —  ME.')\nprint('dolphin idx',idx,'len',len(p))\nfor m in re.finditer(r'\\b(47[0-9])\\b',p):\n    print(m.group(1), m.start())\nEOF"
}
```


### [2026-09-06T14:58:26.817Z] TOOL RESULT

```
178 ['901', '253', '318', '319'] | coeno-).  Cp.  1st  con-,  contra-, count,  ‘title  of  nobi
438 ['1761', '1815', '815', '1946'] | —  ModL.,  fr.  Gk.  eEpeauovr),  ‘a wreath  of  olive  woun
748 ['1583', '1408', '1409', '1866', '1924', '1866', '1927'] | ence  also Swed.  sate,  Dan.  sxde;  rel.  to  OHG.  saze, 
dolphin idx 5159 len 11576
473 2323
474 8596
475 8600
```


## [2026-09-06T14:58:50.482Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i in (334,335,336,337):\n    print(i, re.findall(r'\\b\\d{2,4}\\b',pages[i])[:15])\n    print('   ', pages[i].strip()[:120].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T14:58:52.106Z] TOOL RESULT

```
leaves 657
334 ['1500', '10']
    ntrodactioo  of  new Mm.  (.Ck  )  Ck.  i^i>^,  new:  -Koyitx, k  Xv^ac.  discourse,  from  \iym»,  to _•«  new  ^below)
335 ['10', '1011']
    v/er-nu/turariui^ cxcvssive  in  number. Numismatic ;  see  Nomad. Nun.  (L.)  M.  E.  and  A.S.  mwne.^ Low  L.  nunna,
336 ['06']
    �■     -'i-T,   pi     AS.   rf//i, !   to  Ice).  fj/iV/,  a .'.'.V/,  a  glan'-i.  knot, taarr.  a   kernel,    ball, 
337 []
    8-sidrd  fi| (Gk.)  From  Axrd,  for  ^ctw,  eight;! a  base,  from  the  base  Af^,  to  »it ;  see octangular,  having
```


## [2026-09-06T14:59:12.715Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD pol\"; grep -n \"pōl\\|põl\\|pwl\\b\" PHD.txt PHD_mackenzie.txt | head -10; echo \"=== NYB\"; grep -n \"pōl\\|pwl\" NYB_vol2_glossary.txt | head -5; echo \"=== SYN money\"; grep -n -i \"obolos\\|obol\\b\" SYN.txt IEC.txt | head -10"
}
```


### [2026-09-06T14:59:12.813Z] TOOL RESULT

```
=== PHD pol
PHD.txt:172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
PHD.txt:551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
PHD.txt:568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
PHD_mackenzie.txt:874:   afridan, afrin- I afur- ['jjlytn l , 'plyn-, )pwl- I M )p(w)ryd, 'pwr-, P
PHD_mackenzie.txt:3196:kapur [k'pwl I Ar. hafur] camphor.
PHD_mackenzie.txt:4252:par [pwl IN.....,] francolin.
PHD_mackenzie.txt:4627:spul [spwl] spleen.
=== NYB
603:appurišn [’pwlän'] creation 10519. — MPrs . pwr ‘creation’ (A-H I), ?pwrydn ‘to create’ (S, A-H I); Paz. apurašn, Skr v.
606:appurtan [YHNSLWN-tn'] appur-, to rob, to seize and carry off 6922. 792, — FrP 21 gives as equivalents of the ideogr.: ’pwltn = appurtan, pres. ’pwlyt = ap- pure, 'pwlym = appurém, var. ’plyt, ’plym = apparét, -ém. MPrs "pwrdn, ^pwr-, Paz. apardan, apar-, aparašn evidence -pp-, v. the preceding w. Like appurišn from apa + *par-, but par- in the trans. sense of ‘to transfer’ as in the RV (cf J. Narten in Pagliaro Vol. III, 139-155; in Av. in this sense pärayeitt). Hence appar, v. above; Arm. lw. apur ‘booty’ < *apurn < *apa-purna- < *apa- prna-.
608:*ap-töm: read [hptwm] haftom. *āpurišn ['pwlin']: read appurišn.
609:a-purnài [?pwln’y], a-parnai [’pln’y] young, non-adult 16%. 2611, 536.22, — Bor- rowed from Av. (81) a-parandyu-; Paz. apurnāē, awarndé (Mx); NP barnč(h), burnā(h). Hence
610:apurnāyīk [’pwln’yk], aparnäyik [’pin’yk] a young man 44. 48°; pl. cas. rect. ~ 5235; pl. cas. obl. —-än 1019. 52%, used as cas. rect. 16%; mart ~ 4719, — Milr form; cf Av. (81 sq.) a-poronāyūka-; Paz. = the preceding w.; NP barnäk, burnäk.
=== SYN money
```


## [2026-09-06T14:59:13.425Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 gwelbh\"; grep -n -i \"delphys\\|delphus\\|garewa\\|garbha\\|kilburra\\|Kalb\" incoming/WLD/WLD_Bd1_pages.txt | head -20"
}
```


### [2026-09-06T14:59:13.489Z] TOOL RESULT

```
=== WLD Bd1 gwelbh
554:fraglich. Aber vgl. Buga, Lietuviu kalbos zodynas S. 27.
1102:Liden Stud. 71. Anders Buga, Kalba ir senove I 265.
7027:idg. sind oder niebt (s. G. Meyer).     Ygl. Buga Kalba ir sen. I 249.
9564:tier“)„mannliches Hirschkalb, junger Hirsch- oder Rehbock         vielleicht
10653:Hegel sieht;        osk. Inf. edum );  emi [aus *cdmi vgl. Buga Kalba ir sen.
11513:und Biiga Kalba ir senove I 71.
14024:teils neutr. -es-St.. was gemeingerm. Neuerung nach Kalb scheint; gegen
19636:     Man vergleiebt ai. mca ,,Kuh                                        (die       weder                  traehtig                  ist,   noch ein Kalb
23405:  Ai. rutsa-, vatsard- m. „Jahr“, vatsd- m. „Jahrling, Kalb, Kind“. rat-
23406:sakd- m. „Kalbchen“, savatardu N. du. f. „dasselbe Kalb habend" (Wacker-
23424:Jahren“, vjets f. „Kalb“ (G. Meyer Alb. Wb. 475 f.), viti „Kalb“ (ebda.; aus
23441:„*Yetusco“, Gottername; lat. vetermus „Zugvieh“; vitulus „Kalb“ = umb.
23454:Kalberreiche, Viehzuchtland"? oder alter Stammesname?) ir. feis, corn, ijuis,                                    ;
24835: Anm. 2 von der schwingenden Bewegung). und Buga Kalba ir. sen. I 297.
25343: lit. cersis „Kalb“, lett. versis ,,Ochs, Rind".
28197:die Zugstrange befestigt werden",’-        Ygl. Buga Kalba ir sen. 1175.
28359:eigene Gruppe fur sich zu stellen). Nach Buga Kalba ir sen. 1 34 f. gc-
29955:Ygl.Biiga Kalba ir s. I 301 aus *uinz-snd (Suff. wie in lit. glitosna „Weide‘‘).
30083:vgl. Buga Kalba ir sen. I 297.
34288:moclite?? / ; abg. sitju „nichtig,                          eitel".     Ygl. Buga Kalba   ir.   sen. I 291.
```


## [2026-09-06T14:59:21.810Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i in range(695,703):\n    p=pages[i]\n    print('=== leaf',i,'|', p.strip()[:400].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T14:59:23.318Z] TOOL RESULT

```
leaves 895
=== leaf 695 | g“her-                                                      C87  „Schall", apr gerdnut     .                          ,                                                              Hagen",         arm    .   larclatn „erhebe die              Stimme" (Lewv IP. 32, 161),             lett. dz'trdet                      „h6ren“, Miihlenbach-Endzelin I 552 mit Lit.      Mit in malam partem gewendeter B
=== leaf 696 | bret. gor ,/feu) ardant, furoncle"         Fick II 4 114, Loth Arch. f. celt. Lex.                                                             (s.  , 42, Osthoff IF. 4, 268f.: 27, 172); unsicher ir. gorm „blau", cymr. gwrm „dunkel", abr. TJurm-haelon MN. „aux sourcils brans" (s. Zupitza Gutt. 33, Pedersen KZ. 36, 320. KG. I 10S; ir grian            Sonne", Fick II 4 114, ver-                      
=== leaf 697 | g lJer(ejbh-, gijrebh-          — g^el-                                               689  groues              „Sonnenhitze“, cymr. gtrres „Hitze“ (zum w s. Pedersen                     (* (fibrins -)  KG-. I 108,         durch EinfluB von tes ds.) das l von air gns „Feuer",                               das     V.                                                  ;                          .    gr
=== leaf 698 | 691)                                                  guel-, guele(i)-             werfen"; fiber dfic/.og. djio/.og „Spitze, BratspieB, Obelisk", dessen 6- triiufeln; den AnscliluB erschwert, s. Boisaeq s. v. m. Lit.); lit .geliioms „Stachel", gylijs ds., ijelti ,,stecben(von Bienen): lebhaften Schmerz verursaehen", gPlia „es schmerzt" (wohl aucb gelmenis s. gel- „kalt“), geld „Schmerz" (= dt. Qi
=== leaf 699 | ,                  v   ?                ;                                                  gu e l-, guele(i)-                            691                                                                                                 :‘  bei Eryke“ (Kretschmer                 KZ. 31, 396), vgl. auch elg ala fSdlleiv „miinden (paltog ,.gefleckt“, eigentlich „gesprenkelt, besprengt“?); ahd. quell
=== leaf 700 | -     692                                                   guel       gjjelbh-    „sich legen“, guliu, gnleti , liegen“, gaolis ,, Lager von Tieren und Mcnschen'                                                                                                                1     nicht zu trennen                  ist,   s.   iiber letztere unter *gol- „liegen“.   3. gSel- „Eichel".   Lit. gile u. g
=== leaf 701 | ,                                                             l                            u                                                                                                            ,                                                                   f-'L'es-                                 693           galba und got. Jcil-pei „Hutterleib“ usw.). Nach Zupitza Gutt. 77, gall.-lat.
=== leaf 702 | ;     694                                 g«iia-, g”iids         — gusu-, g“u-       Die Zugehorigkeit von        wild bestritten wegen des Palatals von                                      ai. jasate  av. f'ra-zalnt „er verlaBt"    Schmidt IvZ. 25, 129, Pick I 4 52, 216, 407,                                      (s. J.  Hirt BB. 24, 240, Uhlenbeck Ai. Wb. s. v., Wackernagel Ai. Gr. I 160 gegen 27
```


## [2026-09-06T14:59:36.471Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[700][:2500])\nprint('~~~~~~~~~~ 701')\nprint(pages[701][:2500])\nEOF"
}
```


### [2026-09-06T14:59:38.436Z] TOOL RESULT

```
                                                             -




692                                                   guel       gjjelbh-



„sich legen“, guliu, gnleti , liegen“, gaolis ,, Lager von Tieren und Mcnschen'
                                                                                                               1




nicht zu trennen                  ist,   s.   iiber letztere unter *gol- „liegen“.


3. gSel- „Eichel".
  Lit. gile u. gyli, lett. ds/le, apr. gile „Eichel“ (als Lituanismus lett. gilas
„Geschwulste zw. Haut und Fleisch der Pferde“? s. Zubaty AfslPh. 16,
423 f. u. Miihlenbacli-Endzelin I 698, aber auch *gel- „ballen ‘); mit w-For-
mantien arm. katiii ds.               kalni „Eiche“ (Hiibschmann Zdt. m. G. 35,
655, Arm. St. I 34, Arm. Gr. I 457), gr. jidXavog „Eichel‘ (^g'ij.dno-), mit d-Er-
weiterung aksl. zelndb ds., lat. glans, -dis ds. (Curtius Gdz. 5 474; aber lett.
glluode „Scknur mit einem Qewichte an der Tiire“, Zubaty AfslPh. 16, 424, so
da£! das Gewicht ursprgl. ein eichelahnlicher Zapfen ware, ist vielmehr das
mnd. gelode „Gewicht“, Mikkola BB. 21, 224); vielleicht hierher ai. gula-h
„glans penis" (Fickl 4 405, Johansson IF. 2, 42f.; kann aber auch zur Wz.
*gcl- „ballen“ gehoren, mit welcher *g'iel- „Eichel“ trotz Johansson aaO.
nicht vermengt werden darf).
   Uber aksl. zlezu „glandula“ (Zupitza GG. 83) s. hingegen unter *gel-
„ballen“.   Fiir einen Wzansatz *g"ele- ist das bait, -e ebensowenig eine
Stiitze, wie das i von arm. Juclin; eher konnte das a der zweiten Silbe

von (idJ.avog, zelndb, glans (*g'ihndi oder     mit sog. /              —
                                                             *g“e ldndi-)            —                       als
Tiefstufe eines langcn Yokals, allenfalls e, angesprochen werden.

g“liel- „wollen‘.
    Gr. di'/co, t-lKXoj (zum Praefix s. Brugmann Album Kern29f., Grdr. II 2 2,
8 1 6 f und
      .           o-Part.) „will“, (faXiQti DtX.ei lies. (tm£d'peXog „heftig“? Prell-
                                                             •



witz 2    s.    v.   i

                         ;
                             aksl. zelvti, zelati , iter, russ.-ksl. zalati „wiinschen“, aksl. zelja
„Wunsch, Sehnsucht" (auch „trauern“ und „Trauer“ durch Anlehnung an
zah „Schmerz“ von *g'‘el- „stechen“; s. v. d. Osten-Sacken IF. 24, 241
Anm. 1). Fick BB. 16,289; 18,141; v. d. Osten-Sacken aaO. vermutet
Zugehorigkeit von lit. gilas, gills m. „Gliick, Gelingen" (schlecht bezeugt).
   Wede
~~~~~~~~~~ 701
                ,                                                             l                            u
                                                                                                           ,




                                                              f-'L'es-                                 693

         galba und got. Jcil-pei „Hutterleib“ usw.). Nach Zupitza Gutt. 77,
gall.-lat.
Osthoff Par. I 312 Anm. 1, Vf. LEWb. 2 unter galba und dem unter gel-,
gelebh- „ballen“   bemerkten liegen verschiedene, aber lautahnliche und da-
her gegenseitiger Beeinfiussung ausgesetzte Sippen vor * g'ielbh -, *gierebh-,      :



und aus gel- erweiterte fcA-Formen, die aber im Germ, vermutlich durch
Aufsaugung vou g'ielbh- Formen deren Sfcammbildung und spezifische Bed.
iibernommen haben.
   Lat. volva , vulva volba vulba ) „Gebarmutter; Eihaut der Pilze" wurde
                                 (               ,



unter Zugrundelegung der Form volba (woraus volva, vulva und das vulgare
biilba durch verschiedene Ausgleichung entstanden sein konntej hierher-
gestellt (Hervet Msl. 6, 116, Afsl. 9, 523, Brugmann I 2 593), ist aber eher
als „Hulle“ zu volvo zu stellen (wie ai. ulva-tn, -It, aucli ulba-m, -h „Eihaut,
Gebarmutter", siehe Yf. LEWb. 2 s. v. m. Lit.; Meyer-Liibke Afd. Stud. d.
neuern Spr. 122, 405f. will auf Grund der roman. Fortsetzer ein lat. volva
aus *velua und ein vulva zu ai. ulva- auseinanderhalten?).


g“es- „erloschen“.
  Ai .jdsate, jasyati                „ist erschopft", jasdyati „16scht.
                                                           erschopft" (s. u.).
  Gr. o ft iv vigil „losche“,
                            Aor. horn, ofieo-oui, da(ieoxo; „unausl6scldich“,
mit a/?£o- nach o(5og- (s. u.) fur lautges. odea-, das in £riva/u ev opevvvyev              •


Hes.; eoflgv „ich erlosch" (aus der 2. sg. c-zg’ies-s , 1. pi. e-zgics-mc, woraus
eaftgg, eofiq/uev,wonach auch lofirjv usw. wegen des Typus tfifojv und weil
auch in afievvv/.u der Wzausl. s furs Sprachgefiihl nicht melir vh. war so                             ;


Pedersen IF. 5, 47, Hirt IF. 12, 211, Abl. 142 gegen Brugmanns Doppel-
heit zgi-c- und zgi-es-, MU. I 19 ff., IF. 1, 501, Grdr. I 2 590, siehe noch
Grdr. II 2 3, 171); jon. (Herodas) y.arao [Idiom „loschen“, aus *o/ioao«( von
einem Praes. *afio[o}a'eo, woneben mit aus dem Typus ^etvajuet' ver-
schlepptem Anlaut           a[e)^eaeig, £6aoov
                                             ’
```


## [2026-09-06T14:59:53.655Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/kalb%C4%85",
 "prompt": "What is the etymology given for Proto-Germanic *kalbaz/*kalbą 'calf'? Is it from PIE *gʷelbʰ- 'womb'? Mention OHG kilburra / OE cilforlamb and any note about the velar vs labiovelar problem."
}
```


## [2026-09-06T14:59:54.363Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/obelisk",
 "prompt": "Give the etymology of obelisk, obelus and obol as given — the Greek and Latin chain and any statement about the origin of Greek obelos."
}
```


### [2026-09-06T14:59:55.504Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:00:02.352Z] TOOL RESULT

```
# Etymology of Obelisk, Obelus, and Obol

## Obelisk
The term entered English in the 1560s from French *obélisque* and Latin *obeliscus*, meaning "tapering rectangular stone column with a pyramidal apex." In printing, it refers to "a sign resembling a small dagger" used to mark obsolete words in dictionaries.

## Greek and Latin Chain
The etymological path traces: Latin *obeliscus* ← Greek *obeliskos* (diminutive of *obelos*). The Greek root *obelos* carried multiple meanings: "a spit, pointed pillar, needle, broach; obelisk; bar of metal used as a coin or weight." It also served as "a mark used in writing; horizontal line used as a diacritic."

## Origin of Greek Obelos
According to the source, the origin of Greek *obelos* is uncertain, though scholar Beekes describes it as "clearly Pre-Greek," suggesting it predates the Greek language itself.

## Obol
This ancient Greek coin and weight term (recorded from the 1660s) derives from Latin *obolus*, which came from Greek *obolos*—literally identical to *obelos*. The coin was so named "from the original shape," referencing the pointed form of a spit.
```


## [2026-09-06T15:00:07.052Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/calf",
 "prompt": "Give the full etymology of English calf (young bovine) — Proto-Germanic form, and the PIE root given (is it *gʷelbʰ- 'womb'?), plus any mention of OHG kilburra / chilver / OE cilforlamb."
}
```


## [2026-09-06T15:00:09.130Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%84%D9%81%DB%8C%D9%86",
 "prompt": "Is there a Persian entry for دلفین (dolfin) 'dolphin'? What etymology is given (Arabic دلفين, French dauphin, Greek delphis)?"
}
```


### [2026-09-06T15:00:15.363Z] TOOL RESULT

```
# Etymology of English "Calf" (Young Bovine)

Based on the Wiktionary article provided:

**Proto-Germanic Form:** The word derives from Proto-Germanic *kalbaz, with the further etymology listed as "unknown."

**Etymology Chain:**
The article states: "from [Proto-West Germanic](https://en.wikipedia.org/wiki/Proto-West_Germanic_language "w:Proto-West Germanic language") _[\*kalb](/wiki/Reconstruction:Proto-West_Germanic/kalb "Reconstruction:Proto-West_Germanic/kalb")_, from [Proto-Germanic](https://en.wikipedia.org/wiki/Proto-Germanic_language "w:Proto-Germanic language") _[\*kalbaz](/wiki/Reconstruction:Proto-Germanic/kalbaz "Reconstruction:Proto-Germanic/kalbaz")_, further etymology unknown."

**Important Limitation:**
The Wiktionary source provided contains no mention of:
- Any Indo-European root like *gʷelbʰ- ("womb")
- Old High German *kilburra*
- Old English *cilforlamb*

The article only documents the Germanic language family descent without tracing back to a proposed PIE origin or citing those specific cognates. To answer those aspects of your question would require sources not included in this material.
```


### [2026-09-06T15:00:15.461Z] TOOL RESULT

```
# Persian Entry for دلفین

Yes, there is a Persian entry for دلفین (dolfin) meaning 'dolphin'.

**Etymology Given:**

According to the Wiktionary page, the Persian term was "Borrowed from Arabic _[دُلْفِين](/wiki/%D8%AF%D9%84%D9%81%D9%8A%D9%86#Arabic "دلفين")_ (dulfīn), from Ancient Greek _[δελφίν](/wiki/%CE%B4%CE%B5%CE%BB%CF%86%CE%AF%CE%BD#Ancient_Greek "δελφín")_"

So the documented etymological path is: **Ancient Greek → Arabic → Persian**, not French. The word traces back through Arabic to the original Greek root.
```


## [2026-09-06T15:00:28.116Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%AF%D9%84%D9%81%DB%8C%D9%86",
 "prompt": "What does Mo'in's Farhang-e Farsi say s.v. دلفین? Quote the entry including any origin tag in brackets (e.g. [یو.] Greek, [ع.] Arabic, [فر.] French)."
}
```


## [2026-09-06T15:00:28.897Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D9%BE%D9%88%D9%84",
 "prompt": "What does Mo'in's Farhang-e Farsi say s.v. پول? Quote the entry including any origin tag in brackets."
}
```


### [2026-09-06T15:00:32.268Z] TOOL RESULT

```
According to Mo'in's Farhang-e Farsi, the entry for دلفین (dolphin) states:

"(دُ) [ یو. ] (اِ.) 1 - نوعی پستاندار دریایی بزرگ و بسیار باهوش . 2 - یکی از صورت های فلکی شمالی ."

The origin tag [یو.] indicates a Greek origin, and the entry provides two definitions: a large, highly intelligent marine mammal, and a northern constellation.
```


### [2026-09-06T15:00:34.938Z] TOOL RESULT

```
# Mo'in's Definition of پول (Money)

According to Mo'in's Farhang (Dictionary of Mo'in Publications), the entry for پول includes:

"آن چه که معیار ارزش مادی است و به عنوان وسیلة مبادله مورد استفاده قرار می گیرد"

This translates to: that which serves as a measure of material value and is used as a medium of exchange. The entry also notes related usages, such as پول چایی (tea money, given as a reward) and an idiomatic expression about wealth.

The origin tag appears as **[ یو . ]** at the beginning of the entry.
```


## [2026-09-06T15:00:46.758Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" BQT_v1_pages.txt | head -3; echo \"---- total pages\"; python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read();p=t.split('\\f');print(len(p));print(p[1][:200])\"\necho \"=== ARY pul\"; grep -n \"پول\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY latin\"; grep -n -i \"^PUL\\|PUL \" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-06T15:00:48.483Z] TOOL RESULT

```
---- total pages
777
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
م و اس مر هر وه او
7 رین خلت ریز یتایب بره ات
لف‌بال ۶۲ .یرک
ا اند کل داي رشب , رمع
فان تا تا
رن 9 3
کرحم تن
اد شش مرا
مو رم | مر
وک رهب اه 
=== ARY pul
2503:چم اين واژه در زبان‌های ژرمنی: پولاد.
=== ARY latin
3352:PULGO LATIN) 53 PALK (TOKHARIAN A) A $3
4902:PULCE 1(TTALIAN) gids)
4952:OLD SCANDINAVIAN) 345 eeu! PUL HAFGHAND) (4) gil
11718:| CRAMOISI ¢5cusii y CRIMSON (pul Sit glansly bas cont ate arly caer Shad HF wots
```


## [2026-09-06T15:00:58.006Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i in range(640,672,4):\n    txt=pages[i]\n    print('=== leaf',i, repr(txt.strip()[:180]))\nEOF"
}
```


### [2026-09-06T15:00:59.899Z] TOOL RESULT

```
=== leaf 640 'بیان شانزدهم\nدر بای فارسی با کاف فارسی مشتّمل برپنج لفت و کنایت\nنگ « بفتح اول و سکون ثانی . زن | بتحتانی زده بلفت زند و پازند )٩(\u200f موبد وحکیم\nنار پستان راگوش و کلوله و پندق ی که طف'
=== leaf 644 'بیان هیجد هم (۱)\nدر بای فارسی با نون مشتمل بر شصت ودو لت و کنات\nواعمالی که بجهت دفم چشم زخم کنند- وبمعنی\nپوشیده و پنهان هم آعده است و بلغت زند\nوپازند (۲) پارچه ای باشد چهار کوشه که'
=== leaf 648 'کوند وآن دا گربه نز خوانند .\nنج هر لم» کیهی باشد خوشبوی\nباندام پنج انگشت - کویند مریم مادر عیسی\nعلیه السلام در هنگام وضع حمل بر آن کیاء\nچسسلده بود*\nبنج یو ۱۵۵ - با تحنانی و واو مجه'
=== leaf 652 '. بودان تروش\nفوفانی ورای بی\u200cنقطه وسکون واو وشن\u200cنقطه دار"\nنام ساحخری بوده که درزمان خود عثل و مائند\nنداشته ۷ . ۱\nفوران دخت س من داد بی نقطه\nوسکون خای نقطه دار و تای فرشت بمعنی پسر\nا'
=== leaf 656 '4 بفتح اول وسکون ثانی » کلمه\u200cاست\nکه هنگام تصین با حیرتآمیخته برزبان رانن\nوتکرار نیز کننه؟ ۰\nیاه » بر وزن بهانه . چوبکی باشد\nکه درود گران درشکاف چوبی که باره\u200cمشکافند\nفرو برند و کفشگ'
=== leaf 660 'یاب\nوبکر او عخفف یه بات دکه درچراغ سوزند\n- وشمم تیز سلزند ۷ -\nیمیت بروزن سراب. بمعنی پاباباست\nکه ین\u200cحوض وته جربا باشد وبعربی قمع رکوبند -\nوتهات عرچیز را تز کفتهاعد - و بمعنی تاب\nلب'
=== leaf 664 'پیراهن فبا کردن\nپیراستن وزینت دادن راگویند مطلقا- و دبافت\nکردن پوست را ه مکفته\u200cاند \u200c#\nپیر آهی قبا کردن - کنابه از چا\nزدن و پاره کردن پیراهن باشد.\nپر اهی کاغدی- کنابه از داد -\nخواهی'
=== leaf 668 'پیشواز است که بعربی استفبال گوبند و نوعی\nازجامة پرشیدنی هم هست .\nپیش خاه - بسنی رواق است که\nبیشگاه خانه باشد - و ایوانی که در مرتبهٌ دویم\nساخته باشند \u200f\nپیش خورد بر وژن لیم خورد »\nو'
```


## [2026-09-06T15:01:06.580Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (651,652,653):\n    print('======= leaf',i)\n    print(pages[i][:3000])\nEOF"
}
```


### [2026-09-06T15:01:08.452Z] TOOL RESULT

```
======= leaf 651
حه ی پا حس ۱
بو پل" با بای فارسی , بروزن و معنی
ودر هندونتان با بر کک بان خور ند» ومعرب آن
فوفل است.
و وه با بای فلرسی بر وزن کوکو »
شانه سر وهدحدرا کویند که‌مرغ سلیمان‌است ِ
ک و کو خوانند .
لو له - بنم اول وفتح بای فارسی,بمعنی
لو تاه منم اول وسکون تانی وفوقاتی ؛
جگر کوسقند را کویند و لهذا غلیه‌ای که از
جگر کوسفند سازند قلبه پونی خوانند -
و بمعنی لوت هم آمده است که اقسام خوردنی‌ها
و انواع اطعمه و اثربه باشد - ونوعی از خربزه
هم هست ۰
و 4 - بانای فرشت
و مخزن را کوند . #۶
و خت" بر وزن سوخت : بمعنی پشت
باشد که از يختن است ۲
و ۵ نم اول بروزن سود » نقض ار
است وآن 7 باشد که دریهنامی جامه افته
میشود و تار بدرازی جامه ۴ - و آتشگیره را
نز کویند وآن چیزی بای دکه باچخماق آش
بروزن غوطه.خزانه
۱ -ر: پوپك:
۵ « واژه نامه۱۸۳* .
بزران
برآن زنند ۴ - وبمعت یکهنه هم آمده است که
در مقابل نو باشد ۵ .
لو ذات « با تای قرشت بروزن پوچات,
بمعنی محسوی باشد و پوداتان بمعنی مصوسات
بعنی آنچه بنطر وحس درآید۱ .
لو ده بر وزن روده » معتی جود است
که نقیش نار باشده چه آن درطول جامه و این
عم رفته را هم کفته‌اند ۷ - و رکوی سوخته -
وچوبی بوسیده کهآترا بجپت آتشگیره‌مهیا کرده
باشند ۴ ومعربی‌حراقه خوانند- وسوده وربختهرا
لیز کویند - و کندیده و ضایم شده را حم
کفته‌اند ۷
وه س بضم اول بروزن حور؛ بمعنی‌پسر
است که برادر دختر باشد ۸ و نام رای شهر
کنوج ٩‏ همست واو یکی‌از بادشاهان و رابان
حندوستان بوده. ومعرب آن فور است- وکسی‌را
یز گونند که خود را نادان و هیحمدان
وانماید ٩۴‏ - ودراجرا نز کفته‌اند و آن پرنده -
است ممروف .
پی دنه بروزن توران » نام شه رکنوج
است ومعرب آن قنوج باشد۱۱- و بمعنی خلیفه
وجانشن .- وباد گار حم‌آمده | ست- وجمع پور
حم مت که یسران باشد .
۴ طبری 6 ( بوه )۰ مازندرانی
۰۲۲۳۹ ازدسانیر «فر هگ دساتیر‎ ۳۹ ٩
-٩‏ مرب آن قنوح.
۱- رگ:پوره
کف شکردنه وراز..
======= leaf 652
. بودان تروش
فوفانی ورای بی‌نقطه وسکون واو وشن‌نقطه دار"
نام ساحخری بوده که درزمان خود عثل و مائند
نداشته ۷ . ۱
فوران دخت س من داد بی نقطه
وسکون خای نقطه دار و تای فرشت بمعنی پسر
است نه دختر » نه يك پسر بلکه چندین پسر
است ؛ چه پوران جمع سر باشد» وان نام دختی
خسرویرویز است که پیش ازآزرمیدخت پادشاهی
کرده راورا بدین نام ازجهت آن خوانده‌اند که
ازوکارهای مردانه بظهور آهده است وأورا نوران
سل ملوله تر کسنان‌وده؟
مجهول و را و دال بی نقطه و کاف فارسی بالف
کشفه و بنون زده » مناید دائست که فارسیان
خمسه مسترف4۶ه را بر پنج روزآخرآ بان ماه می-
افزایندکه مجموعه ده روژ شود وآن ده روز را
پورد گان مبگویند» ودراین روزها جشن سازند
وشادی‌تمایند و آنراجشن بورد کان‌خوانند,ومعرب
آن فوردجان است؟ .
9
پوددیان - با بای حطی » بر وزن
و ممنی پورد گان است که ایام جشن پارسیان
باشد .
و د شسب * «پورمعلوم» پفتح‌شن قمله
دار وسکون سین بي نقطه و بای ابجد » نام پدر
پو دعنقا - لفب زال پدر رستم است»
چه کویند او را سیمرغ بز رکه کرد وسیمر غ‌را
عنقا ثبز خوانند .
بور ك بر وژن خوبك , نام دخش
رای قنوج است و او در حبالةٌ بهرام گور بود .
پور کند با کاف بر وزن زورمند ,
طاق وایوان ومتزل را کوند» وباین‌معتی با زای
نقطه دار هم بنظر آمده است .
لبود هنك ه با میم بر وزن حوشمند ؛
صاحب فرزند و عبالمنه را کوند - و با ثالی
مجهول نام کیاهی است خوشیو .
و ده « بر وزن شوره ۰ بمعنی پور
باشد که بر است . و تنهٌ درخت را ای گوشدب
ویز بان هندی یمعتی تمام پاشد۷ . .
.
4۶ تور (سرح) ان (نست) بعئی
بعمنی(از نژاد)سفیداست وسرخاب وسهراب هردو بمعنیآب سرخ‌است. ازافادات امثادپور داود*.
۳ یگ سحیح و رورد کان است. بیرولی گوید 2 پرورد گان چخست 1 نج روز سن اندرآبان ماهء
وسبب نام کردن آن چنانت که کب رکان اندرین پنجروز خورشی وشراب‌نهتد روانهای «رد گان را
و همی کون دکه جان مرده بیابد وزآن غذاگیرد » و چون از بس آبانماه پنجروز افزوئی بوده
افتاد واندر کیش اذان میم ری بود. بي طردو ینجرا بکارهردند از جهت احشاطرا. وسست وششم
روز آبان‌ماه فروردکان کردند وآخرشان آخر دزدبده» وجملةٌ فرورد گان دمروز گشت. * «التفهیم
ص ۲۵۹ رله: فرورد گان . اهر تلا آن: فروردجان «النفهیم ص ۲۵۹ ح » .
۶ پپلوی 3۵۲0511250 مرکب از : پوروش بمعنی دو رنه : صیاه وسپید وییر +
اسب» دعنی دار ندهٌ اسب دورشگف بااسب شبر» درمر و حالذهب «بورشسف؟ ودر طبری پوستف ( بور-
شیف) آهده «مزدیبنا ص۷۶ وجدول برایر ص۹4۹» و ركك : پیثرسپ . ۱ - ازرشة 011۲
درسان‌کریت بمعنی پر کردن , مملو کردن و اسم مفمول آن در سانسکریت ۳00108 است یعنی
درشده» تمام, کامل. «د کتر کونهن راجا».
======= leaf 653
4 ۷۲۷-
ود یان - بکرثاك بر وزن‌حوربان»
۱ رای شهر کنوح۱ هم هست -
و زای هوز » پبرامونو کردا کرد دهان حیوانات
باشد - ومایین لب و بیتی را نیز گویندسوبم‌عنی
ساق درخت هم امده است.و نقار مرغاثرا نیز
کفته‌اند» و با زای فارسی م ۲۳
۰ ۳۹
پورش ۴ - با ابی مجهول بر وزن
سوزش » بمعتی عذر ومعذرت‌وعذرآوردن‌ومعذرت
خواستن باشد .
لودن » بر وزن سوزن » زمینی را
گویند. که بجهت زرات کردن پاك کرده
بشند .
ور ه ۳ بر وزن دوزه » بیرامون
و کردا کرد دهانرا گونند - و بمعتی ننةٌ درخت
هم‌آمده اس 8۵
ود ین ه بر وزن کوزیدن . عذر
آوردن وحعذرت خواستن باشدل" 3
وس » بر وزن طوس ۰ چرب زبانی
و قرب و فروتتی را گویند۷ .
دو یا نه بر وزن روزانه » قرب دادن
وفرونتی و بزبان خوش مردم را فربفئن .
لو ست هه ی وزن دوست » معروف
۱
است ۸ - و بمعنیغیبت هم آ مده‌استکهبد گوبی
ومذمت باشد .
پوست باد کر دن -کنابه از طبار
نه دلی نمودن وراز گفتن باشد .
پوست یرای - با بای فارسی
حطی زده » چرم کر و دیاغ را کویند .
بوست دادن » کنابه از اظهار ته
دلی نمودن ومافی‌النمیر گفتن باشد .
بوست سگ‌بر و کشدن- کناب
از بی حیامی و بی شرمی‌نمودن باشد .
بوستگال ه باکاف فارسی بالف کشیده
وبلام زده ؛ پوست بی‌مویرا گوسد که درزبردنبة
کوسفتد مي باشد وآرا باندك دلبه جدا کرده
در سبراب بر ند» و دوست در کوسفند را ف ‏
کلته‌ادد که سر ککن از حودیای آنآ و بشتهات .
۱ بوستگا له بالام بر وزن بوست پاره,
بهعنی پوستگال است که پوست زبردنبةٌ گوسفند
ودوست مقعد کوسفندباشد ۰
فوست کردن - کنابه از الیس
و محرم ساختن باشد - و غیبت نمودن و خبث
کردنرا گویند .
و ستین » لباسیاست‌مسرونه۹ .و کنابه
از غیبت ومذعت وعیب هم‌هست .
۴ کردی002, ۳6۵2, افغانی 0672 .
دروس ورامین) «اسشق ۳۳۹*.
۵ رك : بوز .
نت اسم مصدراز پوزیدن ( مسعمل
۷ - ره : پلوی .
و
```


## [2026-09-06T15:01:16.664Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (654,655):\n    print('======= leaf',i)\n    print(pages[i][:3500])\nEOF"
}
```


### [2026-09-06T15:01:18.398Z] TOOL RESULT

```
======= leaf 654
یوستین بگازر ۱
وعیب جوننده باشد ۰
(وستیی در بدن » کنابه از افثای
راز کردن باشد .
کردن. وعیب نمودن باشدا .
که بر وقت رشتن مردوك محند.
زره وجوشن را گویند - وامربردورشدن‌ویکناری
رفتن هم عست یمتی از راء دورشو - ونام کیاهی
است کهآ نرا میکویشد وشافپا میسازند واز جانب
ارمن می‌آورند و آنرا پوش دربندی میخوانند .
نقری را نافم است » و شیاف خوزی همان‌است.
و‌شا؟ - با ات بالفکشیده. پوشنده
وپوشند کی را گونند؟ .*
بو شث با ثانی‌مجهول بررزن‌حوشك»
بزبان ماوراء النه رگربه را گویند و بعربی سنود
خوانند؟ .
بو شگان - با انی مجهول ر فتح الث
وک‌اف فارسی بر وزن م وکشان. نام نوایست‌از
موسیقی - و بمعنی مغیبات‌هم‌هست بعنی‌چیهابی
که درعالم غیبت‌اند- وبسکون ثالث بروزن‌دوستان
نام جایی و مقامی است نردبك‌به نیشابورومقامی
۱ "۳ رژ۵: دوست کردن.
5 ود: بوشنج ۰ 3 له: بوشث.
۵ - کلکی 0۲ .
اسشق ۳۳۹
8۷ سم
است از مقامات سالك که آنرا بعربی غیب‌الفیب
مفدس تجلی لماید وفانی درحق ومافی در وگردد.
بو شنگ سب با ثانی مجپول بر وزن
هوشنگه , نام قربه‌ایست مابین فثدهار و مولتان
وه‌مرب‌آن فوشنج بود6 - و بسکون ثالت وفتح
نون بمعنی پوشك است که گربه باشد ٩‏ .
لو شنه» بنن اول و سکون نانی و فتح
الث و نون ۰ بمعنی سرپوش باشد - وهرچیزی
پو شه ۲ - بر وزن خوشه ؛ بمعنیمطلق
آویزند .
لكش - بنم اول وسکون ثانی و کاف 4
نز گونند که درجابی بنهان کنند وخاله بربالای
آن ریزند - و بادی که بجهت آش‌روشنکردن
از دهن بدمند - و آتشگیره را نیز گفثه‌اند
ویعربی حراقه خواندد .
بول بر وزن غول . معروف است
ویعربی فلوس کویند*۱- و بمعنی پل رودخانه‌هم
آمده است مطلقاً خواه باغعت ومشگت وخواه با
جوب «نخه ساند۱۱.
ترا
دانشگاه نهران ص ۲۳۸ .
0 تراهست محشر. رسول ححاز
دهنده پپول چشود جواز. عنضری بلخی.
بقیه درصفحهٌ 4۹٩‏
======= leaf 655
و
پولاب بر وزن دولاب » بم‌نی
حس باشد و پولاپی‌حسی, بعنی‌|نچه بحس ونظر
درآ مد ۱ ۰
که از آن‌کارد و شمشیر واعثال‌آن سازند -وتیغ
و شمشیر را نیز گویند - و نام پهلواتی است
ای ال اج و نام دو ست ماز ندرانی و اورا بولاد
غندی میگفته‌اند عم غین نقطه دار - و ب‌عنی
و3 هم هست.
ولاد خسای « کنابه ازاس‌سرزور
ماشفد .
و لادد که م کنابه‌از اسب‌پرزورباشد.
بو لادسنحان کنانه از دلاوران
وسارزان واساحه داران باشد ۰
بو لاد هندی ۰ کنابه‌ازشیترهندی
باشد 5 3 ۰
4و لافی ع با ثانی حجهول بی وژن
طولافی » نوعی از اش‌ارد باشد .
و [4 س با ثانی محپول بر وزن لوله .
خریره مضمحل شده را کویند - وهندوانه‌ومیوه
های دمگر را نز گفته‌اند که درون آنها نرم
. فوبه
و ضایع شده باشد .
زسن را گونند که تکلتو باشد .
وک - بر وزن جوی. بمعنی پوبه‌باشد
که رفتار متوط است یعنی نه نند و نه آهسته,
و بعضی رفتار تند را گوشدب واعر بدیشمه‌نی «م
ست ععنی راه رو وقدم‌بردار .
پو با ۶ بروزن کویا» رونده‌را گویشد
- و بعضی دونده را نز گفته‌اند .
بویان ۴ زان جو بارس مت موی
و د بر ورن جودال» مصی‌دوه
باشد که رونده است ه و دونده رانیز گوند ۳
وی وی ح با بای فارحی بر وزن
خوب روی . مبالفةً درا مدن و رفتن باشد بمنی
تندتند و دوان دوان - و امر باینمعنی هم هست
یعثی بدو وزود براه برو .
بو یچه- بفتح‌اول بر وزن درجه» عشقه‌را
گویند وآن گیاهی است که بردرخت یبچد .
و 4 »_ با انی مجهول بر وزن موبه .
رفتاری باشد متوسط ت + رفتار نند و دو دز |
تبز گویند .
فرهنگه دساتیر نیلمده .
«2. است ۱۱۵» کلکی ۵120) ورند: فولاد.
۴ - نمت فاعلی از پوبیدن .
بقبه ازصفحه ۲۸
۴ نعت فاعلی(صفت مشبهه) از بوسدن.
از هم باشبدن .
جامه » آنچه بدن را بپوشاند . رك : پوشا .
```


## [2026-09-06T15:01:46.453Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC gwelbh/delphus\"; grep -n -i \"gʷelbh\\|g\\*elbh\\|delphus\\|delphys\\|adelphos\\|garbha\" IEC.txt | head -10; echo \"=== IEC obelos\"; grep -n -i \"obelos\\|obolos\" IEC.txt | head -5; echo \"=== SYN brother/womb\"; grep -n -i \"adelphos\\|delphys\\|garbha\" SYN.txt | head -10"
}
```


### [2026-09-06T15:01:46.531Z] TOOL RESULT

```
=== IEC gwelbh/delphus
=== IEC obelos
=== SYN brother/womb
2912:2. Grk. a5eddés ‘brother’, adeAd7 ‘sis- ter’, dial. also ddeddeds, adeAged, fr. *4-Seddos (-cos) : Skt. sa-garbhya- ‘of the same womb’, cpd. of cop. sa- (Grk. 4-) and garbha- ‘womb’ (: Grk. deddis ‘womb’). Walde-P. 1.692. This was doubtless first used as an adj. defining oparnp, either more specifically as ‘frater uterinus’ (in contrast to brother by the same father only), or simply as ‘brother by blood’ after ¢parnp had come to be applied to the member of a phratry.
4167:4. Goth. kalbé ‘female calf’, ON kalfr, OE cealf, etc., same word as ON kalfr ‘calf of the leg’, fr. *gel-bh- an extension of *gel- in Skt. gula- ‘ball’, Lat. galla ‘gallnut’, parallel to *gel-t- in Goth. kilpet ‘womb’, OE cild ‘child’, and with a similar semantic development, in this case ‘swelling’ to ‘womb’, ‘fetus’, ‘young of an animal’, ‘calf’. But in part perh. blended with *g’elbh- in Grk. deddis, Skt. garbha- ‘womb’, etc. In any case ‘calf’ is a specialization of ‘young of an animal’. Walde-P. 1.615, 692. Feist 305 f.
4463:Grk. Séddak : deddts, Skt. garbha- ‘womb’, etc., with shift from ‘womb’ through ‘fetus’ to ‘young of an animal’, as often (cf. NE calf, etc., 3.24), then specialization to ‘pig’.
6588:(rare) : Skt, garbha-, etc.,
6593:th. wamba, gipus, kilpet Lith.  Zyvatas sarpty yaoTnPy xothla, ae kvidr Lett. mdtes miesas, mates ; etc. Dan. moderliv klepis rot dtd, BATPS Sw. moderlif oer &révo, atroba erus, i hrif, innop r.  materica \ Cries mare Ue ME wombe Boh. Zivol, matka get ma Pere NE womb Pol.  zywot, lono * — matriz, maare, Du. baarmuoder Russ. matka Rum. pintece OHG (h)ref, wamba Skt.  garbha-, yoni- brit MHG  barmuoter, muoterlip Ay. garawa-, barabri- Ir, brid (wambe) croth, bru NHG mutterleib, gebdérmut- kof ter, schoss The majority of the words for ‘womb’ 3. W. croth (formerly also ‘belly’) :
6601:7. Skt. garbha-, Av. garawa- : Grk. dekpis ‘womb’ (rare), ddeAdés ‘brother’ (2.44), with parallel forms in Goth. kalbo ‘calf’ (3.24), and with r in Grk. Bpedos ‘foetus’, etc. Walde-P. 1.692.
7260:4.73 PREGNANT Goth. inkilpo, pat es pees vos <2 ieee ON unguo, Ulett, hafan- ett. gr Grk. (yyvearpane” tb a id A di, med barni ChSl. neprazdtna NG pracgnans, GRE Dan.  frugtsommelig, svan- SCr. _trudna, breda, nose¢a lat. inciéns | iatoreg: ger; dreglig Boh. téhotna; brezt gravida, ncn a, P Sw. havande; draktig Pol. brzmienna, ciezarna te na Deine OE getacnod, bearn-éacen, Russ. beremennaja Fr encernle, 9” pee 4 med cilde Skt.  garbhini-, garbhavati-, Sp. prenada, Pets ME with childe, with barne etc. Rum. insdr Fie ut NE pregnant, with child Avy. pubra- lorrac . ; drachti Ir. ‘i hea- Du. zwanger; 9g Nir. bruinneach, tourch GHik. smaieee sach MHG _ swanger, trehtec, w. _ beichtog swere : razez, dougerez eee Breese eraeees NHG  schwanger; trdchtig
7307:7. Skt. garbhinz-, garbha- ‘womb’ (4.47).
7310:garbhavaii- fr.
```


## [2026-09-06T15:01:47.716Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD obol\"; grep -n -i \"obelus\\|obelisk\" FSD_vol3.txt FSD_vol4.txt WEB_vol1.txt 2>/dev/null | head -6; echo \"=== HUB/HRN fals\"; grep -n -i \"fals\\b\\|fulūs\\|fulus\" HRN.txt HUB.txt | head -6"
}
```


### [2026-09-06T15:01:47.823Z] TOOL RESULT

```
=== FSD obol
WEB_vol1.txt:34804:Glé-5-pa’tra’s Nee’dle, 1. an ancient Egyp- fis obelisk now in Central Park, New York
WEB_vol1.txt:34806:2. another such obelisk on the Thames Em- bankment, London.
WEB_vol1.txt:48691:2. in printing, an obelisk, a mark of refer- ence (f) in the form of a dagger. at daggers drawn; ready for attack, violence, hostility, etc. double dagger; in printing, a mark of refer- ence (f). to look daggers at; to look at with anger or hatred. dag’gér, v.t. 1. to pierce with a dagger; to stab. 2. to mark with a dagger. dag’gér, n. [prob. a corruption of diagonal.] in shipbuilding, any timber resting diagonally in the frame. daggen mọth, a moth of the genus A patela, the larvae of which infest fruit trees and their foliage: so named from a daggerlike mark on its forewing. dagger plant, a plant having leaves with sharp points, belonging to the genus Yucca. dag/gle, v.t. and v.i.; daggled, pl., pp.; daggling, ppr. (Sw. dagga, to bedew.] to trail; to make or become dirty by trailing through mud, as the lower end of a garment; to draggle. dag/gle-tail, x. a slatternly woman; a draggle tail. [Dial.] dag/gle-tdiled, a. having the lower ends of a garment dirtied with mud. [Dial.] dä-ghes: tän’ (-ges-), n. a type of heavy carpet: after Daghestan, a division of the U.S. S. R. in the Caucasus.
FSD_vol3.txt:50007:obelisk Kee illus under ouklimk
FSD_vol3.txt:84866:To mark with an obelisk (t)
FSD_vol3.txt:84884:Obelisks vary in height from 8i/t to 108 feet, and range in
=== HUB/HRN fals
```


## [2026-09-06T15:01:59.850Z] TOOL CALL #72: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/ 2>/dev/null | head; ls data/verification/sources/refs/ocr/BOOK 2>/dev/null | tail -5"
}
```


### [2026-09-06T15:01:59.893Z] TOOL RESULT

```
AFM
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
92.png
94.png
95.png
96.png
99.png
```


## [2026-09-06T15:02:02.722Z] TOOL CALL #73: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D9%BE%D9%88%D9%84' \\\n 'https://en.wiktionary.org/wiki/%D9%81%D9%84%D8%B3' \\\n 'https://en.wiktionary.org/wiki/%E1%BD%80%CE%B2%CE%B5%CE%BB%CF%8C%CF%82' \\\n 'https://www.etymonline.com/word/obelisk' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 207, roots Gwel 2 / Gwelbh: Greek obelos/obolos, Persian pul, Arabic fals, English obelisk/obol' 2>&1 | tail -2; done"
}
```


### [2026-09-06T15:02:06.010Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/bfe739d9f82003aa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6ad69afdf1c8ec70.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dd079b4bd068e5b3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/26eab585174bc7bb.txt
```


## [2026-09-06T15:02:11.792Z] TOOL CALL #74: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/calf' \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D9%84%D9%81%DB%8C%D9%86' \\\n 'https://vajehyab.com/moein/%D8%AF%D9%84%D9%81%DB%8C%D9%86' \\\n 'https://vajehyab.com/moein/%D9%BE%D9%88%D9%84' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 207, root Gwelbh/Gwel 2: calf, Persian dolfin, Moin tags for دلفین and پول' 2>&1 | tail -2; done\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg207.png data/verification/sources/refs/ocr/BOOK/207.png && echo copied"
}
```


### [2026-09-06T15:02:14.741Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6e1658b9a6a0ea46.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/873d24fea2fa5e57.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d31f2f3b698205ac.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e9b9ac869034624c.txt
copied
```


## [2026-09-06T15:02:45.472Z] TOOL CALL #75: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob\nfor f in sorted(glob.glob('data/verification/page-20*.json')):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e['nodes']:\n            if not (n.get('words') or '').strip():\n                print(f, n.get('id'), n.get('lang'), n.get('verdict'), '|', (n.get('derivation') or '')[:200])\nEOF"
}
```


### [2026-09-06T15:02:47.294Z] TOOL RESULT

```
data/verification/page-203.json 2 None unverified | Empty pass-through box. On the printed page (pdf p. 203, book p. 173; see data/verification/sources/refs/ocr/BOOK/203.png) the large rectangle to the right of the Avestan/Old Persian box is drawn but 
data/verification/page-203.json 4 French confirmed | Empty pass-through box: the printed page shows a French box with no word in it, standing between the Greek box and the Persian one. The forms it stands for are French diabète (a learned borrowing of L
data/verification/page-203.json 2 None unverified | Empty pass-through box: on the printed page (data/verification/sources/refs/ocr/BOOK/203.png) the rectangle to the right of the Avestan box in the Gwadh chart is drawn but left blank — no language, no
```


## [2026-09-06T15:02:53.531Z] AGENT

Now I'll write the verification file.


## [2026-09-06T15:11:32.639Z] TOOL CALL #76: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk207.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\ndata = {\n \"pdf_page\": 207,\n \"book_page\": 177,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Gwel 2\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *gʷel- (Pokorny 'gʷel-1') 'to stick, prick; pain, death'\",\n   \"note\": \"The root box is right on all three counts, and the page number is Pokorny's own. POK_full.txt (lines 39104-39172) has 'Root / lemma: gʷel-1 || Meaning: to stick; pain, death || ... Page(s): 470-471', and Watkins in the AHD appendix condenses it to 'gʷel-1. To pierce. ... [Pok. 1. gʷel- 470.]' — so 'Indo-European Gwel 2 : to pierce, POK:470' reproduces the standard lemma exactly (Nourai's '2' is his own serial number for the Gwel- roots, not Pokorny's). The whole chart, however, hangs on ONE debatable link: whether Greek ὀβελός / ὀβολός belongs to this root. Pokorny puts it there in so many words ('ὀβελός, ὀβολός, Arcadian Doric ὀδελός \\\"spit, cusp, peak, pointed square pillar, obelisk, coin\\\"'), but Walde-Pokorny I 690 f., the article Pokorny is abridging, already warned 'über ὀβελός, ὀβολός \\\"Spitze, Bratspieß, Obelisk\\\", dessen ὀ- den Anschluß erschwert', Klein calls ὀβελός 'of uncertain origin', Watkins drops it, and Beekes/Furnée classify it as Pre-Greek. Downstream of that, the Greek→Latin→English branch (obolus, obol, obelus, obelisk) is impeccable, the Greek→Persian branch (پول) is well supported on the Persian side (Moʿin tags پول '[یو.]' = Greek), but the Greek→Arabic branch is a different word altogether: Arabic فلس is Greek φόλλις (Latin follis), not ὀβολός. Two printing points: the Greek box prints 'obelekos', a misprint for ὀβελίσκος, and the Latin box gives obolus the meanings of obeliscus.\",\n   \"note_fa\": \"جعبهٔ ریشه درست است: پوکورنی مادّهٔ «gʷel-1» را با معنای «سوزن زدن، فرو بردن؛ درد، مرگ» در صفحات ۴۷۰–۴۷۱ آورده و واتکینز نیز آن را «to pierce» با ارجاع «Pok. 1. gʷel- 470» ثبت کرده است؛ پس صورت، برچسب زبان، معنا و شمارهٔ صفحه‌ای که نورایی داده هر چهار درست است (شمارهٔ «۲» از خودِ نورایی است، نه از پوکورنی). امّا تمامِ نمودار بر یک حلقهٔ مورد اختلاف استوار است: آیا یونانی ὀβελός/ὀβολός به این ریشه بازمی‌گردد؟ پوکورنی صریحاً چنین می‌گوید، ولی والده-پوکورنی (جلد ۱، ص ۶۹۰) همان‌جا هشدار داده که «ὀ-»ی آغازینِ آن پیوند را دشوار می‌کند، کلاین آن را «با خاستگاه نامعلوم» می‌خواند، واتکینز آن را حذف کرده و بیکس آن را پیش‌یونانی (Pre-Greek) می‌داند. شاخهٔ یونانی←لاتین←انگلیسی (obolus, obol, obelus, obelisk) بی‌عیب است؛ شاخهٔ یونانی←فارسی («پول») از سوی فارسی پشتیبانی دارد (معین آن را «[یو.]» یعنی یونانی می‌داند)؛ ولی شاخهٔ یونانی←عربی نادرست است: «فلس» عربی از φόλλις یونانی (لاتین follis) است، نه از ὀβολός. دو نکتهٔ چاپی نیز هست: صورت «obelekos» غلط چاپیِ ὀβελίσκος است، و جعبهٔ لاتین معناهای obeliscus را به obolus داده است.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%E1%BD%80%CE%B2%CE%B5%CE%BB%CF%8C%CF%82\",\n    \"https://www.etymonline.com/word/obelisk\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:470\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt lines 39104-39172: 'Root / lemma: gʷel-1 | Meaning: to stick; pain, death | Material: 1. Gr. βέλλαι \\\"wasp, hornet\\\", Hes.; gr. βελόνη f. \\\"cusp, peak, needle\\\" ... ὀβελός, ὀβολός, Arcadian Doric ὀδελός \\\"spit, cusp, peak, pointed square pillar, obelisk, coin\\\" s. Schwyzer Gr. Gr. I 295 ... References: WP. I 689 f. ... Page(s): 470-471.' Exactly the root box, and the Greek box of node 1 is lifted from this same paragraph.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, IE roots appendix s.v. gʷel-1 (AHD_watkins1985.txt line 540)\", \"stance\": \"partial\",\n     \"note\": \"'gʷel-1. To pierce. 1. Suffixed o-grade form *gʷol-eyo- in Germanic *kwaljan in Old English cwellan, to kill, destroy: QUELL. 2. ... KILL. 3. Full-grade form *gʷel- in Greek belonē, needle: BELONEPHOBIA. [Pok. 1. gʷel- 470.]' — same root, same gloss, same Pokorny page, but Watkins lists only belonē on the Greek side and deliberately omits ὀβελός/ὀβολός.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 690-691 (WLD_Bd1_pages.txt leaf 698, running head 'gʷel-, gʷele(i)-')\", \"stance\": \"partial\",\n     \"note\": \"'... über ὀβελός, ὀβολός \\\"Spitze, Bratspieß, Obelisk\\\", dessen ὀ- den Anschluß erschwert, s. Boisacq s. v. m. Lit.' — the source article Pokorny abridges says in as many words that the initial ὀ- makes the attachment of obelos/obolos to this root difficult.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. obelus (KLN_1966.txt line 25849, leaf 570 ≈ pp. 1065-1066)\", \"stance\": \"contradicts\",\n     \"note\": \"'obelus, n., a mark (— or ÷) used in manuscripts to indicate a doubtful passage. — Late L., fr. Gk. ὀβελός, \\\"a needle, spit\\\", which is of uncertain origin. Cp. obelisk, obol, amphodelite.' Klein — one of Nourai's own two references for the Greek box — refuses the IE etymology.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, Indo-European Comparative Dictionary\", \"stance\": \"silent\",\n     \"note\": \"grep of IEC.txt for 'obelos', 'obolos' and the labiovelar spellings of the root returned nothing usable (the OCR mangles Mann's *gʷ- notation).\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Greek\",\n     \"words\": \"obelos, obolos; obelekos\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"ὀβελός (Ionic-Attic; Arcadian/Doric ὀδελός) 'spit, pointed pillar', with its by-form ὀβολός used for the coin, is genuinely Greek and genuinely means what Nourai says: the obol was a spit-shaped bar of metal, six of which made a δραχμή ('a handful'), so 'nail, spit' → 'nail-shaped coin' → 'money' is the real semantic history (Etymonline s.v. obol: 'literally identical with obelos ... so called from the original shape'). What is disputed is the arrow from the root. Pokorny 470 does place ὀβελός/ὀβολός under gʷel-1 'to prick', which would require *gʷel- > βελ- with an unexplained prothetic ὀ-; Walde-Pokorny I 690 f. already noted that this ὀ- 'den Anschluß erschwert', Klein calls the word 'of uncertain origin', Watkins omits it from gʷel-1, and Beekes (followed by Wiktionary) treats the β/δ alternation ὀβελός ~ ὀδελός as the signature of a Pre-Greek substrate word. Modern scholarship therefore takes ὀβελός OUT of Indo-European altogether. Separately, the third form in the box, 'obelekos', is not a Greek word: the form is ὀβελίσκος 'little spit, obelisk', the diminutive of ὀβελός (Klein s.v. obelisk: 'Gk. ὀβελίσκος, \\\"a small spit, an obelisk\\\", dimin. of ὀβελός'). The printed page (data/verification/sources/refs/ocr/BOOK/207.png) really does read 'obelekos', so this is the author's misprint, not a scanning error.\",\n     \"derivation_fa\": \"واژهٔ یونانی ὀβελός (در آرکادی و دُری ὀδελός) به معنای «سیخ، ستون نوک‌تیز» و صورت دیگر آن ὀβολός برای سکه، هر دو یونانی‌اند و معنای‌شان همان است که نورایی آورده: «اوبول» میله‌ای سیخ‌مانند از فلز بود و شش تای آن یک دراخما می‌شد؛ پس تحوّل معنایی «سیخ/میخ ← سکهٔ میخ‌شکل ← پول» واقعی است. آنچه مورد اختلاف است پیکانِ ریشه است: پوکورنی (ص ۴۷۰) این واژه را ذیل *gʷel- «سوراخ کردن» آورده، ولی برای این کار باید «ὀ»ی آغازین را پیشوندی ناشناخته دانست؛ والده-پوکورنی خود گفته که همین «ὀ» پیوند را دشوار می‌کند، کلاین آن را «با خاستگاهِ نامعلوم» می‌داند، واتکینز آن را از این ریشه بیرون گذاشته، و بیکس دگرگونی β/δ را نشانهٔ واژه‌ای پیش‌یونانی (زیرلایه‌ای) می‌شمارد. بنابراین پژوهش امروزی این واژه را از هندواروپایی بیرون می‌برد. جدا از این، صورت سوم جعبه، «obelekos»، واژهٔ یونانی نیست؛ صورت درست ὀβελίσκος «سیخِ کوچک، اوبلیسک» است، مصغّرِ ὀβελός. تصویر صفحهٔ چاپی نشان می‌دهد که خودِ کتاب «obelekos» چاپ کرده است؛ پس خطای چاپی کتاب است، نه خطای خوانش اسکن.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"obelekos\",\n     \"correct_form\": \"obeliskos (ὀβελίσκος)\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%E1%BD%80%CE%B2%CE%B5%CE%BB%CF%8C%CF%82\",\n      \"https://www.etymonline.com/word/obelisk\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"POK:470\", \"status\": \"supports\",\n       \"note\": \"POK_full.txt line ~39112: 'ὀβελός, ὀβολός, Arcadian Doric ὀδελός \\\"spit, cusp, peak, pointed square pillar, obelisk, coin\\\" s. Schwyzer Gr. Gr. I 295' — Pokorny does list exactly these forms and these meanings under gʷel-1 on p.470, so Nourai's citation is faithful; it is Pokorny who is now outvoted.\"},\n      {\"ref\": \"KLN:1068\", \"status\": \"partial\",\n       \"note\": \"Klein's obol article (KLN_1966.txt line 25909, leaf 571, which carries the running numbers 1067/1068 — so KLN:1068 is the right page): 'obol, n., a small ancient Greek coin and weight, 1/6 drachma. — L. obolus, fr. Gk. ὀβολός'; but two entries earlier, s.v. obelus, Klein says ὀβελός 'is of uncertain origin', i.e. Klein supports the Greek→Latin route but not the Indo-European root.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 690-691 (WLD_Bd1_pages.txt leaf 698)\", \"stance\": \"contradicts\",\n       \"note\": \"'über ὀβελός, ὀβολός \\\"Spitze, Bratspieß, Obelisk\\\", dessen ὀ- den Anschluß erschwert, s. Boisacq s. v. m. Lit.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷel-1 (AHD_watkins1985.txt line 540)\", \"stance\": \"silent\",\n       \"note\": \"the Greek material under gʷel-1 is only 'Full-grade form *gʷel- in Greek belonē, needle: BELONEPHOBIA' — obelos/obolos are not listed anywhere in the appendix.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary, s.vv. Obolus / obelisk (SKT.txt leaf 336)\", \"stance\": \"partial\",\n       \"note\": \"'Obolus, a small Gk. coin. (L.—Gk.) L. obolus.—Gk. ὀβολός, a small coin, perhaps orig. in the shape of a spike or nail, allied to Gk. ὀβελός, a spit' — Skeat confirms the spit→coin semantics but goes no further back than Greek.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"pŭl «پول»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"New Persian پول pul 'money, small copper coin' is standardly derived from Greek ὀβολός, taken over in the Hellenistic/Parthian period after aphaeresis of the unstressed first syllable (*obolós > *bōl/pōl), through a Middle Persian *pōl; NP -ū- is the regular reflex of MP ō (cf. MP tōm > NP tūm). Wiktionary gives 'From Middle Persian *pōl, perhaps borrowed from Ancient Greek ὀβολός', and Moʿin's Farhang-e Fārsi tags the headword پول '[یو.]' = یونانی, Greek, which is as explicit as a Persian dictionary gets. Two cautions keep this at 'plausible' rather than 'confirmed'. First, the Middle Persian link is a reconstruction: MacKenzie's Concise Pahlavi Dictionary has no *pōl 'money' at all (its Pahlavi coin-word is pišīz 'small copper coin, farthing', PHD.txt p.68), and Horn and Hübschmann know only pul 'bridge' (< OP *pṛtu-, Av. pərətu-), a homonym that has nothing to do with money. Second, the Persian lexical tradition itself connects پول with Arabic فلوس rather than with Greek: Borhān-e Qāṭeʿ p.428, the very page Nourai cites, glosses 'پول ... معروف است و بعربی فلوس گویند'. Since Arabic fulūs is from φόλλις, that would be a different Greek word; but the phonetics of pul point to ὀβολός, and Moʿin (who edited the Borhān) tags it Greek.\",\n     \"derivation_fa\": \"«پول» در فارسی نو معمولاً وام‌واژه‌ای از یونانی ὀβολός دانسته می‌شود که در دورهٔ هلنی/اشکانی با افتادنِ هجای نخستِ بی‌تکیه (*obolós ← *pōl) وارد شده و از راه فارسی میانهٔ *pōl به فارسی نو رسیده است؛ «ō»ی فارسی میانه در فارسی نو قاعده‌مند به «ū» بدل می‌شود. ویکی‌واژه می‌نویسد «از فارسی میانهٔ *pōl، احتمالاً وام‌گرفته از یونانی باستان ὀβολός» و معین در فرهنگ فارسی مدخل «پول» را با نشانهٔ «[یو.]» یعنی یونانی آورده است. دو نکته سبب می‌شود این ادعا «با احتیاط پذیرفتنی» بماند و نه «قطعی»: نخست آنکه حلقهٔ فارسی میانه بازسازی‌شده است — مکنزی هیچ *pōl «پول» ندارد و واژهٔ سکّهٔ پهلوی نزد او pišīz است، و هرن و هوبشمان تنها pul «پُل، گذرگاه» (از ایرانی باستان *pṛtu-، اوستایی pərətu-) را می‌شناسند که هم‌آوایی بی‌ربط است. دوم آنکه سنّت فرهنگ‌نویسی فارسی «پول» را به «فلوس» عربی پیوند می‌دهد: برهان قاطع، ص ۴۲۸ — همان صفحه‌ای که نورایی ارجاع داده — می‌نویسد «پول ... معروف است و بعربی فلوس گویند». امّا چون «فلوس» عربی از φόλλις است نه از ὀβολός، و آواشناسیِ «پول» به ὀβολός راه می‌برد، مسیرِ نورایی محتمل‌تر است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D9%BE%D9%88%D9%84\",\n      \"https://vajehyab.com/moein/%D9%BE%D9%88%D9%84\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"BQT:428\", \"status\": \"partial\",\n       \"note\": \"Borhān-e Qāṭeʿ p.428 is BQT_v1_pages.txt leaf 654 (leaf 653 carries the printed numeral ۴۲۷). The entry reads 'پول بر وزن غول. معروف است و بعربی فلوس گویند ... و بمعنی پل رودخانه هم آمده است مطلقاً'. So the cited page really does carry the headword — and, note, it is also why Nourai cites BQT:428 a second time for the Arabic فلس box — but Moʿin's etymological footnote 10 there is broken off ('بقیه در صفحهٔ ۴۲۹') and is not legible in the OCR, so the page confirms the word, not the Greek origin.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Fārsi, s.v. پول (vajehyab)\", \"stance\": \"supports\",\n       \"note\": \"the headword is tagged '[ یو . ]' — یونانی, Greek — before the definition 'آن چه که معیار ارزش مادی است و به عنوان وسیلهٔ مبادله مورد استفاده قرار می‌گیرد'.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.68-69 (PHD.txt line 551)\", \"stance\": \"silent\",\n       \"note\": \"no *pōl 'money'; MacKenzie has only 'pišīz [pšyc | N ~] small copper coin, \\\"farthing\\\"' and '1puhl [pwhl | N pul] bridge'.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie no. 325 (HRN.txt line 3096)\", \"stance\": \"silent\",\n       \"note\": \"'325. pul \\\"Brücke\\\"' is Horn's only pul; he has no entry for pul 'money'.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt lines 6918, 7378)\", \"stance\": \"silent\",\n       \"note\": \"'np. pul = puhl \\\"Brücke\\\" = ap. *pṛtu- = zd. pərətu-' — again only the bridge word.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Arabic\",\n     \"words\": \"fals; flŭs; eflâs; mofles\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The Arabic words are real and the internal morphology is right: فَلْس fals 'a small copper coin' (pl. فُلُوس fulūs, whence the colloquial 'money'), form-IV أَفْلَسَ aflasa 'to go bankrupt' with verbal noun إِفْلَاس iflās 'bankruptcy' and participle مُفْلِس muflis 'bankrupt, penniless' — literally 'to be reduced to fulūs', i.e. to have nothing but coppers. What is wrong is the parent. Arabic fals is not ὀβολός but Greek φόλλις phóllis, itself Latin follis 'bellows, bag' → the late-Roman copper coin, borrowed into Arabic through Aramaic פּוּלְסָא pūlsā; Lokotsch, no. 581, states it flatly: 'Ar. fals, Plr. fulūs [aus gr. φόλλις ZDMG XXI, 672/674] \\\"kleine Silber- od. Kupfermünze\\\"', and repeats it at no. 1491 s.v. muflis. Nourai's own reference TAD:52 is the reason he drew the arrow this way — Ṭūbiyā al-ʿUnaysī's page 52 does say 'فلس – يوناني [ὀβολός] وهو نقد نحاسي يوناني كان يساوي سدس الدرهم', 'a Greek copper coin worth a sixth of a dirham', which is the definition of the obol — but that is a 1932 guess that later scholarship has replaced. The second gloss in the box, 'the scales on fish skin', is yet a third etymon: فَلْس 'fish scale' is from Greek φολίς pholís, not from either coin word.\",\n     \"derivation_fa\": \"واژه‌های عربیِ این جعبه واقعی‌اند و ساخت درونی‌شان هم درست است: «فَلْس» سکّهٔ مسینِ خرد (جمع «فُلوس»، که در گویش‌ها به معنای «پول» به کار می‌رود)، و از ریشهٔ ف‌ل‌س بابِ افعال «أفلَسَ» یعنی ورشکست شدن، مصدرش «إفلاس» و اسم فاعلش «مُفلِس» — تحت‌اللفظ «کسی که جز فلوس چیزی برایش نمانده». امّا ریشهٔ آن نادرست است: «فلس» عربی از ὀβολός نیست، بلکه از یونانیِ φόλλις (خود از لاتینِ follis «دمِ آهنگری، کیسه» و سپس نامِ سکّهٔ مسینِ روم شرقی) است که از راه آرامیِ پּוּלְסָא به عربی رسیده است؛ لوکوچ (شمارهٔ ۵۸۱) صریح می‌گوید: «Ar. fals, Plr. fulūs [از یونانی φόλλις] سکّهٔ خردِ سیمین یا مسین»، و در شمارهٔ ۱۴۹۱ ذیل «مفلس» همان را تکرار می‌کند. علّت پیکانِ نورایی مرجع خودِ اوست: طوبیا العنیسی در ص ۵۲ نوشته «فلس – يوناني، وهو نقد نحاسي يوناني كان يساوي سدس الدرهم» که همان تعریفِ «اوبول» است؛ ولی این حدسِ سال ۱۹۳۲ را پژوهش‌های بعدی کنار گذاشته‌اند. معنای دومِ جعبه، «فلسِ ماهی»، ریشهٔ سومی دارد: از یونانیِ φολίς، نه از هیچ‌یک از دو واژهٔ سکّه. پس ریشه‌شناسیِ این گره را پژوهش امروزی رد می‌کند.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D9%81%D9%84%D8%B3\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"TAD:52\", \"status\": \"supports\",\n       \"note\": \"TAD_pages.txt leaf 55 (= printed p.52; the file's 87 leaves run about 3 ahead of the printed numbers, and leaf 31 = p.28 for دلفين below) reads 'فلس – يوناني [Greek word lost in OCR] وهو نقد نحاسي يوناني كان يساوي سدس الدرهم'. Al-ʿUnaysī does derive fals from a Greek coin worth a sixth of a drachma, i.e. from ὀβολός — Nourai's citation is faithful, but the reference is wrong.\"},\n      {\"ref\": \"ARK:232\", \"status\": \"not_checked\",\n       \"note\": \"ARK = Rokn-zādeh Ādamiyyat, Arkān-e Soḵan (1347/1968); refs_online.json records 'none online ... nothing digitised on any permitted platform'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"Lokotsch, Etymologisches Wörterbuch, no. 581 (LKT.txt line 1464) and no. 1491 (line 3436)\", \"stance\": \"contradicts\",\n       \"note\": \"581: 'Ar. fals: Plr. fulūs [aus gr. φόλλις ZDMG XXI, 672/674] \\\"kleine Silber- od. Kupfermünze\\\"; hieraus sp. foluz, pg. fuluz ... it. filussi'. 1491: 'Ar. muflis: \\\"Bankrottierer\\\" [part. praes. act. vom Vb. falasa IV \\\"bankrott machen\\\", dies von ar. fals, plr. fulūs \\\"Geldstück\\\" ← gr. φόλλις ZDMG LI, 300]'.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.vv. follicle, fool, phallus (KLN_1966.txt lines 14733, 15106, 28443)\", \"stance\": \"partial\",\n       \"note\": \"Klein has no Arabic fals, but he documents the etymon Lokotsch and Wiktionary point to: 'L. follis, \\\"a pair of bellows; a bag\\\"' from I.-E. *bhel- 'to swell' — i.e. Greek φόλλις is a Latin loan, a completely different word from ὀβελός.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-Fārisiyya al-Muʿarraba (AFM_pages.txt)\", \"stance\": \"silent\",\n       \"note\": \"grep of 'فلس' returns only the incidental أفلس/مفلس of running text (lines 1422-1423, 3250); Addi Shir has no headword فلس, as expected — he lists Persian, not Greek, loans in Arabic.\"},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qurʾān (FVQ_pages.txt)\", \"stance\": \"silent\",\n       \"note\": \"no entry for فلس (the word is not Qurʾānic); grep of 'fals' returns only English 'false/falsehood' in Jeffery's prose.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Persian\",\n     \"words\": \"fals «فَلس»; eflâs «افلاس»; mofles «مُفلس»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"These are ordinary Arabic loanwords in New Persian, taken over unchanged in form and meaning from the ninth century onward with the rest of the fiscal and commercial vocabulary: فَلس fals 'a copper coin; a fish scale' (Persian keeps both Arabic senses, which are historically two different words), افلاس eflās 'bankruptcy, destitution' (the Arabic maṣdar of form IV أفلس), and مُفلس mofles 'bankrupt, penniless' (the Arabic active participle مُفلِس, with the usual Persian pronunciation mofles rather than moflis). Persian did not reshape them: no Persian suffix, no vowel change beyond the ordinary Persian reading of Arabic short vowels. The route Nourai draws (Arabic → Persian) is therefore right; what he inherits from the box above is the wrong ultimate source, since Arabic fals is from Greek φόλλις / Latin follis. Note that Persian mofles/eflās stay inside the Arabic root f-l-s and were never confused with the native پول.\",\n     \"derivation_fa\": \"این‌ها وام‌واژه‌های معمولیِ عربی در فارسی نو هستند که از سدهٔ سوم هجری به بعد همراه با دیگر واژگانِ مالی و بازرگانی، بی هیچ دگرگونی در صورت و معنا، وارد شده‌اند: «فَلس» (سکّهٔ مسین؛ و نیز فلسِ ماهی — که در عربی دو واژهٔ جداگانه‌اند)، «اِفلاس» (مصدرِ بابِ افعال از أفلَسَ) و «مُفلِس» (اسم فاعلِ همان باب، که در فارسی «مُفلِس/مُفلَس» خوانده می‌شود). فارسی هیچ پسوند یا دگرگونی آوایی بر آن‌ها نیفزوده است. پس مسیرِ «عربی ← فارسی» که نورایی کشیده درست است؛ آنچه نادرست است ریشهٔ نهایی است که از جعبهٔ بالا به ارث رسیده، زیرا «فلس» عربی از φόλλις یونانی / follis لاتین است. یادآوری: «مفلس» و «افلاس» درونِ ریشهٔ عربیِ ف‌ل‌س مانده‌اند و هرگز با «پول»ِ فارسی درنیامیخته‌اند.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D9%81%D9%84%D8%B3\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"FVA:319\", \"status\": \"not_checked\",\n       \"note\": \"FVA = Nahvi, Farhang-e Vāžehā-ye ʿArabi dar Fārsi (1368/1989); refs_online.json: 'Searched archive.org, ketabnak, noorlib, web: no digital copy found ... Catalogue record only.'\"},\n      {\"ref\": \"BQT:428\", \"status\": \"partial\",\n       \"note\": \"BQT_v1_pages.txt leaf 654 (printed p.428) has no فلس headword — it is the پ section — but it is presumably cited here for the sentence in the پول entry 'معروف است و بعربی فلوس گویند', which links the Persian and Arabic words. It does not document Persian فلس/افلاس/مفلس.\"},\n      {\"ref\": \"ARK:232\", \"status\": \"not_checked\",\n       \"note\": \"Arkān-e Soḵan is not digitised anywhere (refs_online.json).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Moʿin / Borhān-e Qāṭeʿ tradition, BQT_v1_pages.txt leaf 654 (p.428)\", \"stance\": \"supports\",\n       \"note\": \"'پول ... معروف است و بعربی فلوس گویند' — the Persian lexicographic tradition itself pairs Persian پول with Arabic فلوس, showing the Arabic word was fully naturalised.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 581 / no. 1491 (LKT.txt lines 1464, 3436)\", \"stance\": \"partial\",\n       \"note\": \"documents fals/fulūs and muflis spreading out of Arabic into Spanish, Portuguese, Sicilian and Romanian ('sp. foluz, pg. fuluz', 'rum. mofluz'); the same wave carried them east into Persian, but Lokotsch traces them to φόλλις, not ὀβολός.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen (PLA_pages.txt)\", \"stance\": \"silent\",\n       \"note\": \"no entry for فلس, as expected — Asbaghi catalogues Persian words IN Arabic, and fals is a Greek, not a Persian, loan.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Latin\",\n     \"words\": \"obolus\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Latin obolus is a straightforward learned borrowing of Greek ὀβολός, taken over with the Greek monetary system in the second century BCE (Plautus, Varro, Pliny use it for the sixth part of a drachma and for the weight of the same name); Greek -ος regularly gives Latin -us, and the word never went through a popular sound change because it stayed a technical term of coinage and pharmacy. Klein s.v. obol: 'L. obolus, fr. Gk. ὀβολός'. The arrow is therefore right, but the gloss in the box is not: Latin obolus means only the coin/weight. 'Spike, a narrow pointed stone pillar' belongs to two other Latin borrowings from the same Greek family — obelus (Late Latin, from ὀβελός, the critical sign) and obeliscus (from ὀβελίσκος, the monument) — which Nourai has collapsed into the single Latin box so that the three English words below can hang off it.\",\n     \"derivation_fa\": \"«obolus»ی لاتین وام‌واژه‌ای مستقیم و فرهیخته از یونانی ὀβολός است که در سدهٔ دوم پیش از میلاد همراه با نظام سکّهٔ یونانی وارد لاتین شد (پلاوتوس، وارّو و پلینیوس آن را برای یک‌ششمِ دراخما و نیز واحد وزن به کار برده‌اند)؛ پایانهٔ یونانیِ ‎-ος‎ قاعده‌مند به ‎-us‎ لاتین بدل می‌شود و چون واژه اصطلاحی فنّی در سکّه‌شناسی و داروسازی ماند، هیچ دگرگونی آواییِ عامیانه بر آن نگذشت. کلاین می‌نویسد: «L. obolus, fr. Gk. ὀβολός». پس پیکان درست است، امّا معنایی که در جعبه آمده نادرست است: obolus در لاتین تنها نامِ سکّه و واحد وزن است؛ معناهای «سیخ» و «ستون نوک‌تیز» به دو وام‌واژهٔ دیگر از همین خانواده تعلّق دارد — obelus (لاتین متأخّر، از ὀβελός، نشانهٔ نقدِ متن) و obeliscus (از ὀβελίσκος، بنای سنگی) — که نورایی هر سه را در یک جعبه فشرده کرده تا سه واژهٔ انگلیسیِ زیرین از آن آویخته شوند.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/obelisk\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1068\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt line 25909 (leaf 571, running numbers 1067/1068): 'obol, n., a small ancient Greek coin and weight, 1/6 drachma. — L. obolus, fr. Gk. [ὀβολός], orig. ...' and 'obolus, n. — See obol.' The Greek→Latin step is exactly Klein's.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary s.v. Obolus (SKT.txt leaf 336)\", \"stance\": \"supports\",\n       \"note\": \"'Obolus, a small Gk. coin. (L.—Gk.) L. obolus.—Gk. ὀβολός, a small coin, perhaps orig. in the shape of a spike or nail, allied to Gk. ὀβελός, a spit.'\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary (WEB_vol1.txt line 34804, 48691)\", \"stance\": \"partial\",\n       \"note\": \"Webster keeps the two senses apart — 'Cleopatra's Needle, an ancient Egyptian obelisk' for the monument, and 'in printing, an obelisk, a mark of reference (†) in the form of a dagger' for the sign — confirming that the pillar sense belongs to obeliscus/obelus, not to obolus.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"Obol; obelus; obelisk\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All three reached English through Latin, exactly as drawn, but by three separate Latin words. Obol (attested 1660s) is Latin obolus < Greek ὀβολός, the sixth of a drachma. Obelus (in English from the 15th c.) is Late Latin obelus < Greek ὀβελός, the horizontal stroke — or dagger — that Alexandrian editors, beginning with Zenodotus and Aristarchus, set in the margin of Homer to mark a line they judged spurious; hence Klein's definition 'a mark (— or ÷) used in manuscripts to indicate a doubtful passage'. Obelisk (1560s) came in through French obélisque from Latin obeliscus < Greek ὀβελίσκος 'little spit', the diminutive that the Greeks applied to the tapering Egyptian monoliths they saw at Heliopolis and Thebes. The semantic thread through all three is the spit: a spit-shaped ingot became a coin, a spit-shaped stroke became a critical sign, a spit-shaped monolith became the obelisk.\",\n     \"derivation_fa\": \"هر سه واژه دقیقاً همان‌گونه که در نمودار آمده از راه لاتین به انگلیسی رسیده‌اند، امّا از سه واژهٔ لاتینِ جداگانه. «Obol» (از دههٔ ۱۶۶۰ در انگلیسی) از obolus لاتین و آن از ὀβολός یونانی، یک‌ششمِ دراخما. «obelus» (از سدهٔ پانزدهم) از obelus لاتینِ متأخّر و آن از ὀβελός، همان خطِ افقی یا خنجرک که ویراستارانِ اسکندرانی — از زنودوتوس و آریستارخوس به بعد — در حاشیهٔ ایلیاد کنارِ بیتی می‌گذاشتند که آن را الحاقی می‌دانستند؛ از این‌رو کلاین آن را «نشانه‌ای (— یا ÷) در دست‌نویس‌ها برای نشان دادنِ عبارتِ مشکوک» تعریف می‌کند. «obelisk» (دههٔ ۱۵۶۰) از راه فرانسویِ obélisque و لاتینِ obeliscus از ὀβελίσκος «سیخِ کوچک» آمده است، مصغّری که یونانیان بر ستون‌های یکپارچهٔ مصری در هلیوپولیس و تِبس نهادند. رشتهٔ معناییِ هر سه یکی است: میلهٔ سیخ‌مانند سکّه شد، خطِ سیخ‌مانند نشانهٔ نقدِ متن، و ستونِ سیخ‌مانند اوبلیسک. ادعای نورایی در این گره درست است.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/obelisk\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1068\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt lines 25848-25849 and 25909 (leaves 570-571, pp. ~1066-1068): 'obelisk, n. ... — F. obélisque, fr. L. obeliscus, fr. Gk. ὀβελίσκος, \\\"a small spit, an obelisk\\\", dimin. of ὀβελός'; 'obelus, n., a mark (— or ÷) used in manuscripts to indicate a doubtful passage. — Late L., fr. Gk. ὀβελός'; 'obol ... — L. obolus, fr. Gk. [ὀβολός]'.\"},\n      {\"ref\": \"SKT:354\", \"status\": \"supports\",\n       \"note\": \"SKT.txt leaf 336 has both entries side by side: 'Obolus, a small Gk. coin. (L.—Gk.) L. obolus.—Gk. ὀβολός, a small coin, perhaps orig. in the shape of a spike or nail, allied to Gk. ὀβελός, a spit' and 'obelisk. (F.—L.—Gk.) O.F. obelisque, L. obeliscum, acc. of obeliscus, Gk. ὀβελίσκος, a pointed spit; hence a thin pointed pillar; dimin. of ὀβελός, a spit'. (The SKT OCR carries no usable running page numbers, so p.354 itself could not be checked against the leaf; leaf 336 of 657.)\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary s.v. obelisk (FSD_vol3.txt lines 50007, 84866, 84884)\", \"stance\": \"supports\",\n       \"note\": \"'To mark with an obelisk (†)' and 'Obelisks vary in height from 8½ ft to 108 feet' — the same two senses (critical sign, stone monument) that Nourai's English box distributes over obelus and obelisk.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary (WEB_vol1.txt lines 34804, 48691)\", \"stance\": \"supports\",\n       \"note\": \"'Cleopatra's Needle, 1. an ancient Egyptian obelisk now in Central Park, New York'; 'dagger ... 2. in printing, an obelisk, a mark of reference (†) in the form of a dagger'.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Gwelbh\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *gʷelbʰ- 'womb; young of an animal'\",\n   \"note\": \"Root, language label, gloss and page are all Pokorny's own: POK_full.txt (lines 39079-39104) reads 'Root / lemma: gʷelbʰ- || Meaning: womb; young of animal || Material: Old Indic garbha-ḥ, Avestan garəwa- \\\"womb, foetus\\\", garəbuš- \\\"the young of an animal\\\"; ... gr. δελφύς, -υος f., Doric δελφύα \\\"womb, uterus\\\"; ... ἀδελφεός (Hom.) \\\"couterinus, brother\\\" ... δελφίς, -ῖνος m. \\\"dolphin\\\" ... References: WP. I 692 f. ... Page(s): 473'. Nourai's chart is that paragraph turned into a tree, and Klein's article 'calf' carries the identical set in one sentence. Two qualifications. (1) Nourai's gloss 'womb' truncates Pokorny's 'womb; young of animal', and it is the second half that licenses the Avestan garəbuš- and the Germanic branch. (2) The Germanic branch is the weak one: Pokorny in the same article says the -s-stem OHG kilburra / OE cilforlamb and Kalb 'point to purely velar anlaut (as Gaulish-Latin galba and Gothic kilþei \\\"womb\\\")' — i.e. to *gel-, not to *gʷelbʰ-; Walde-Pokorny I 693 spells out that *gʷelbʰ-, *gʷerebʰ- and bʰ-extensions of gel- are 'verschiedene, aber lautähnliche ... Sippen' that contaminated each other; Buck 3.24 derives Goth. kalbō from *gel-bh- and allows only that it was 'in part perh. blended with *gʷelbh-'; and Wiktionary/Kroonen call PGmc *kalbaz 'further etymology unknown'. So the Avestan and Greek halves of the chart are solid and the Germanic half is a nineteenth-century guess that has since been downgraded.\",\n   \"note_fa\": \"ریشه، برچسب زبان، معنا و شمارهٔ صفحه هر چهار از خودِ پوکورنی است: در فرهنگ او آمده «Root/lemma: gʷelbʰ- | Meaning: womb; young of animal | مواد: سنسکریت garbha-، اوستایی garəwa- «زهدان، جنین»، garəbuš- «بچّهٔ جانور»؛ یونانی δελφύς «زهدان»، ἀδελφεός «برادر»، δελφίς «دلفین» ... صفحهٔ ۴۷۳». نمودار نورایی در واقع همین بند است که درخت‌وار بازچیده شده، و مقالهٔ «calf» در کلاین همهٔ این مجموعه را در یک جمله دارد. دو نکته: نخست آنکه معنایی که نورایی داده («زهدان») نیمی از معنای پوکورنی است و همان نیمهٔ دوم («بچّهٔ جانور») است که garəbuš- اوستایی و شاخهٔ ژرمنی را توجیه می‌کند. دوم آنکه شاخهٔ ژرمنی سست است: خودِ پوکورنی در همان مقاله می‌گوید صورت‌های ژرمنی (kilburra، Kalb) به آغازهٔ کامیِ ساده اشاره دارند نه به لبی‌کامیِ *gʷ-؛ والده-پوکورنی (ج ۱، ص ۶۹۳) این‌ها را «خانواده‌های جداگانه امّا هم‌آوا» می‌داند که بر یکدیگر اثر گذاشته‌اند؛ باک (بند ۳٫۲۴) kalbō گوتی را از *gel-bh- می‌گیرد و تنها می‌پذیرد که «شاید تا اندازه‌ای با *gʷelbh- درآمیخته باشد»؛ و ویکی‌واژه ریشهٔ ژرمنی آغازینِ *kalbaz را «ناشناخته» می‌خواند. پس نیمهٔ اوستایی و یونانیِ نمودار استوار است و نیمهٔ ژرمنیِ آن حدسی از سدهٔ نوزدهم است که امروز پذیرفته نیست.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/calf\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:473\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt lines 39079-39104: 'Root / lemma: gʷelbʰ- | Meaning: womb; young of animal | Material: Old Indic garbha-ḥ, Avestan garəwa- \\\"womb, foetus\\\", garəbuš- \\\"the young of an animal\\\"; Old Indic sa-garbhya-ḥ \\\"son of the same mother\\\" (= gr. ἀδελφεός); gr. δελφύς, -υος f., Doric δελφύα \\\"womb, uterus\\\" ... δελφάξ \\\"piglet\\\", δελφίς, -ῖνος m. \\\"dolphin\\\" ... the -es-stem reappears in Old High German kilburu, chilburra \\\"mother lamb\\\", Old English cilforlamb ... which point to purely velar anlaut ... References: WP. I 692 f., WH. I 578 ... Page(s): 473.'\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, IE roots appendix s.v. gʷelbh- (AHD_watkins1985.txt lines 540-542)\", \"stance\": \"partial\",\n     \"note\": \"'gʷelbh-. Womb. 1. Suffixed form *gʷelbh-u- in Greek delphus, womb, whence delphis, dolphin (referring to its shape): DELPHINIUM, DOLPHIN. 2. Prefixed and suffixed form *sm-gʷelbh-o-, \\\"born of one womb\\\" (*sm-, one; see sem-1), in Greek adelphos, brother: -ADELPHOUS. [Pok. gʷelbh- 473.]' — same root, same gloss, same page, but Watkins gives only the Greek branch and does NOT put CALF here.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 692-693 (WLD_Bd1_pages.txt leaves 700-701)\", \"stance\": \"partial\",\n     \"note\": \"'... galba und got. kilþei \\\"Mutterleib\\\" usw.). Nach Zupitza Gutt. 77, Osthoff Par. I 312 ... liegen verschiedene, aber lautähnliche und daher gegenseitiger Beeinflussung ausgesetzte Sippen vor: *gʷelbh-, *gʷerebh-, und aus gel- erweiterte bh-Formen, die aber im Germ. vermutlich durch Aufsaugung von gʷelbh-Formen deren Stammbildung und spezifische Bed. übernommen haben.'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck, Dictionary of Selected Synonyms 4.47 'womb' and 3.24 'calf' (SYN.txt lines 6601, 4167)\", \"stance\": \"supports\",\n     \"note\": \"4.47: 'Skt. garbha-, Av. garəwa- : Grk. δελφύς \\\"womb\\\" (rare), ἀδελφός \\\"brother\\\" (2.44), with parallel forms in Goth. kalbō \\\"calf\\\" (3.24) ... Walde-P. 1.692.' 3.24 adds the caveat that Goth. kalbō is 'fr. *gel-bh- ... But in part perh. blended with *gʷelbh- in Grk. δελφύς, Skt. garbha- \\\"womb\\\"'.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. calf (KLN_1966.txt line 6181; leaf 128, running numbers 222/223)\", \"stance\": \"supports\",\n     \"note\": \"'calf ... fr. I.-E. base *gwelbh-, *gwolbh-, \\\"womb; young of an animal\\\", whence also OI. garbhaḥ, Avestic garəwa-, \\\"womb\\\", Gk. δελφύς, δολφός (in Hesychius), \\\"womb\\\", ἀ-δελφός, \\\"brother\\\" (lit. \\\"from the same womb\\\"), Avestic gerebush, \\\"the young of an animal\\\". Cp. adelpho-, dolphin ... Cp. also chilver.' This single article is the source of Nourai's whole chart.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"garewa; garebuš\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Both forms are in Bartholomae, with these meanings. Younger Avestan garəwa- m. (Nourai's 'garewa') is glossed 'Mutterleib, Uterus' and, in a second sense, 'Leibesfrucht, Junges' (Altiranisches Wörterbuch col. 515, in the passage about the female principle in Yasna 65.5 and Vd. 15.11); *gərəbuš- n. 'Junges eines Tiers' (col. 523-524, pasə̄uš gərəbuš 'the young of a sheep', Yt. 8.58, A. 3.3), where Bartholomae himself adds 'Vgl. ai. gárbha- m., nhd. Kalb'. The phonology is regular: PIE *gʷelbʰ- gives Indo-Iranian *garbʰa- (labiovelar depalatalised to g before a, *l > r in Indo-Iranian), whence Sanskrit gárbha- and, with the Avestan intervocalic development of *b(h) to the spirant w, garəwa-; the u-stem *gʷelbʰ-us- appears as gərəbuš-, where -b- is preserved before the consonantal ending. Nourai's spelling 'garebuš' for gərəbuš- reflects the schwa with e, as does 'garewa' for garəwa-; these are transliteration conventions, not errors.\",\n     \"derivation_fa\": \"هر دو صورت با همین معناها در بارتولمه هست. اوستاییِ متأخّر garəwa- (نزد نورایی «garewa») در فرهنگِ ایرانیِ باستانِ او، ستون ۵۱۵، به «زهدان، رَحِم» و در معنای دوم «جنین، بچّه» معنا شده است؛ و *gərəbuš- خنثی «بچّهٔ جانور» در ستون‌های ۵۲۳–۵۲۴ (pasə̄uš gərəbuš «برّهٔ گوسفند»)، جایی که خودِ بارتولمه می‌افزاید «قس. سنسکریت gárbha- و آلمانیِ Kalb». دگرگونی‌های آوایی قاعده‌مندند: هندواروپاییِ *gʷelbʰ- در هندوایرانی *garbʰa- می‌شود (لبی‌کام پیش از a به g ساده بدل می‌شود و *l در هندوایرانی به r) و از آن سنسکریت gárbha- و در اوستایی، با نرم‌شدنِ *b(h) میان دو واکه به سایشیِ w، صورت garəwa-؛ در ستاکِ ـu یعنی gərəbuš- که ‎-b-‎ پیش از همخوان محفوظ مانده است. نگارشِ «garebuš» و «garewa» تنها شیوهٔ آوانگاری برای «ə» است، نه خطا. ادعای نورایی در این گره درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/calf\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"POK:473\", \"status\": \"supports\",\n       \"note\": \"POK_full.txt line ~39084: 'Material: Old Indic garbha-ḥ, Avestan garəwa- \\\"womb, foetus\\\", garəbuš- \\\"the young of an animal\\\"' — Pokorny p.473 gives exactly these two Avestan forms with exactly these two glosses.\"},\n      {\"ref\": \"KLN:483\", \"status\": \"supports\",\n       \"note\": \"Klein's article containing these forms is 'calf' (KLN_1966.txt line 6181): 'fr. I.-E. base *gwelbh-, *gwolbh-, \\\"womb; young of an animal\\\", whence also OI. garbhaḥ, Avestic garəwa-, \\\"womb\\\", ... Avestic gerebush, \\\"the young of an animal\\\"'. Caveat on the page number: in the 1966 two-volume printing the leaf carrying 'calf' bears the running numbers 222/223 and the 'dolphin' article falls at ~473-475, while p.483 lies in the 'dr-' range, so KLN:483 points to the dolphin/calf neighbourhood at best; the substance, however, is verbatim Klein.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch cols. 515 and 523-524 (BRT.txt lines 10253, 10372)\", \"stance\": \"supports\",\n       \"note\": \"col. 515: 'j. garəwa- m. 1) \\\"Mutterleib, Uterus\\\" ... 2) \\\"Leibesfrucht, Junges\\\"'. col. 523f.: 'j. *gərəbuš- n. \\\"Junges\\\" eines Tiers: pasə̄uš °buš anumayeheca Yt.8.58 ... Vgl. ai. gárbha- m., nhd. Kalb.'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 4.47 'womb' (SYN.txt lines 6593, 6601)\", \"stance\": \"supports\",\n       \"note\": \"the Avestan column of Buck's womb table reads 'Av. garəwa-, barəθri-', and the discussion: 'Skt. garbha-, Av. garəwa- : Grk. δελφύς \\\"womb\\\" (rare), ἀδελφός \\\"brother\\\", with parallel forms in Goth. kalbō \\\"calf\\\" ... Walde-P. 1.692.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷelbh-\", \"stance\": \"silent\",\n       \"note\": \"Watkins's article lists only the Greek reflexes; no Indo-Iranian forms are cited, so the appendix neither supports nor contradicts the Avestan box.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": null,\n     \"words\": \"\",\n     \"verdict\": \"unverified\",\n     \"derivation\": \"Empty pass-through box. On the printed page (pdf p. 207, book p. 177; see data/verification/sources/refs/ocr/BOOK/207.png) the wide rectangle to the right of the Avestan box in the Gwelbh chart is drawn but left completely blank — no language label, no reference, no word — and no arrow leaves it. The extraction is faithful to the page (lang null, refs null, words []). Judging by the layout of the other charts on this and neighbouring pages, this is the slot where a Persian reflex of Avestan garəwa- would have gone; but Persian has no inherited continuation of garəwa- (the modern word for 'womb' is the Arabic رَحِم, and زهدان is a New Persian compound of زه- 'birth' + دان), which may be exactly why the author left it empty. There is nothing here to verify.\",\n     \"derivation_fa\": \"جعبهٔ خالیِ گذری. در صفحهٔ چاپی (تصویر ۲۰۷ در پوشهٔ ocr/BOOK) مستطیل پهنِ سمت راستِ جعبهٔ اوستایی در نمودار Gwelbh کشیده شده امّا کاملاً خالی است — نه نام زبانی، نه ارجاعی، نه واژه‌ای — و هیچ پیکانی هم از آن بیرون نمی‌رود. استخراج دادهٔ JSON با صفحه می‌خواند (زبان و ارجاع تهی، فهرست واژه‌ها خالی). با توجّه به چیدمانِ نمودارهای دیگرِ همین صفحه، این جای بازماندهٔ فارسیِ garəwa- اوستایی بوده است؛ امّا فارسی هیچ بازماندهٔ موروثی از garəwa- ندارد (واژهٔ امروزی «رَحِم» عربی است و «زهدان» ترکیبی نوساخته از «زه‌» و «دان» است)، و شاید نویسنده به همین سبب آن را خالی گذاشته باشد. چیزی برای راستی‌آزمایی در این گره نیست.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BOOK\", \"where\": \"printed page, pdf p. 207 (data/verification/sources/refs/ocr/BOOK/207.png)\", \"stance\": \"supports\",\n       \"note\": \"the rectangle beside the Avestan box is empty on the page itself, so the blank node in the JSON is not an extraction failure.\"},\n      {\"src\": \"BRT\", \"where\": \"Bartholomae col. 515 s.v. garəwa-\", \"stance\": \"silent\",\n       \"note\": \"Bartholomae's Pahlavi equivalences for garəwa- are given as Pahlavi glosses only, with no New Persian continuant, consistent with the box being left blank.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Greek\",\n     \"words\": \"delphus; delphis; adelphos; philo-adelphos\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"δελφύς (gen. -ύος), Doric δελφύα, 'womb', is the regular Greek outcome of *gʷelbʰ-u-: the labiovelar *gʷ- before a front vowel becomes δ in Greek (the same change as in βοῦς/δελφ- alternations described by Schwyzer, Gr. Gr. I 295, whom Pokorny cites here), and *-lbʰ- gives -λφ-. From it come δελφίς, -ῖνος 'dolphin', named for its shape or for the belief that it bore live young like a mammal, and δελφάξ 'piglet'. ἀδελφός (Homeric ἀδελφεός) is *sm̥-gʷelbʰ-o-, 'of one womb', with copulative ἀ- < *sm̥- 'one, together' (the same prefix as in ἅπαξ, ἁπλοῦς), so literally 'co-uterine'; Buck 2.44 notes it was first an adjective qualifying φράτηρ, distinguishing the full brother from the half-brother, and only then displaced φράτηρ as the word for 'brother'. φιλάδελφος is the ordinary compound 'loving one's brother/sister'; Nourai's gloss 'brotherly love' properly renders the abstract φιλαδελφία. His cross-reference to his root 'Bhili' (PIE *bhilyo- 'dear', the source of φίλος) is right.\",\n     \"derivation_fa\": \"«δελφύς» (اضافه ‎-ύος‎) و صورت دُریِ δελφύα به معنای «زهدان»، بازتابِ قاعده‌مندِ *gʷelbʰ-u- است: لبی‌کامِ *gʷ- در یونانی پیش از واکهٔ پیشین به δ بدل می‌شود (همان دگرگونی‌ای که شوایتسر در دستور یونانیِ خود، ج ۱ ص ۲۹۵ — همان‌جا که پوکورنی به آن ارجاع می‌دهد — شرح داده) و *-lbʰ- به ‎-λφ-‎. از آن δελφίς «دلفین» ساخته شده — یا به سببِ شکلِ اندام یا به سببِ این باور که مانند پستانداران بچّهٔ زنده می‌زاید — و نیز δελφάξ «بچّه‌خوک». «ἀδελφός» (در هومر ἀδελφεός) از *sm̥-gʷelbʰ-o- است، با پیشوندِ همراهیِ ἀ- از *sm̥- «یک، با هم» (همان پیشوندِ ἅπαξ و ἁπλοῦς)، یعنی تحت‌اللفظ «هم‌زهدان»؛ باک (بند ۲٫۴۴) یادآور می‌شود که نخست صفتی برای φράτηρ بوده تا برادرِ تنی را از برادرِ ناتنی جدا کند و سپس خودْ جای φράτηρ را گرفته است. «φιλάδελφος» ترکیبِ معمولِ «برادردوست» است؛ معنایی که نورایی داده («عشق برادرانه») در واقع برابرِ اسمِ مجرّدِ φιλαδελφία است. ارجاعِ او به ریشهٔ «Bhili» (هندواروپایی *bhilyo- «عزیز»، سرچشمهٔ φίλος) درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/calf\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"POK:473\", \"status\": \"supports\",\n       \"note\": \"POK_full.txt line ~39088: 'gr. δελφύς, -υος f., Doric δελφύα \\\"womb, uterus\\\" (see below); *δελφος n. ds. as base from ἀδελφεός (Hom.) \\\"couterinus, brother\\\" (*ἁ-δελφε[ι]ός), next to which Attic ἀδελφός ds.; δελφάξ m. f. \\\"piglet\\\", δελφίς, -ῖνος m. \\\"dolphin\\\" ... Specht ... reconstructs from gr. ἀδελφήρ ... an originally root *gʷel-'.\"},\n      {\"ref\": \"KLN:483\", \"status\": \"supports\",\n       \"note\": \"Klein s.v. adelpho- (KLN_1966.txt line 1610): 'Gk. ἀδελφο-, fr. ἀδελφός, \\\"brother\\\", lit. \\\"from the same womb\\\", fr. copul. pref. ἀ-, \\\"together with\\\", and δελφύς, \\\"womb\\\". Copul. pref. ἀ- stands for I.-E. *sm̥- ... For the etymology of δελφύς see calf and cp. dolphin.' (Page caveat as at node 1: Klein's dolphin article falls near pp.473-475 of the 1966 printing, calf at 222; p.483 is in the 'dr-' range.)\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷelbh- (AHD_watkins1985.txt lines 540-542)\", \"stance\": \"supports\",\n       \"note\": \"'1. Suffixed form *gʷelbh-u- in Greek delphus, womb, whence delphis, dolphin (referring to its shape): DELPHINIUM, DOLPHIN. 2. Prefixed and suffixed form *sm-gʷelbh-o-, \\\"born of one womb\\\" ... in Greek adelphos, brother: -ADELPHOUS.'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 2.44 'brother' (SYN.txt line 2912)\", \"stance\": \"supports\",\n       \"note\": \"'Grk. ἀδελφός \\\"brother\\\" ... fr. *ἁ-δελφος : Skt. sa-garbhya- \\\"of the same womb\\\", cpd. of cop. sa- (Grk. ἁ-) and garbha- \\\"womb\\\" (: Grk. δελφύς \\\"womb\\\"). Walde-P. 1.692. This was doubtless first used as an adj. defining φράτηρ, either more specifically as \\\"frater uterinus\\\" ... or simply as \\\"brother by blood\\\".'\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 692 (WLD_Bd1_pages.txt leaves 700-701)\", \"stance\": \"supports\",\n       \"note\": \"the article gʷelbh- from which Pokorny 473 and Buck 1.692 are both drawn; Buck and Pokorny cite it as 'Walde-P. 1.692' for exactly this Greek material.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Arabic\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Language-labelled but wordless box: on the printed page the Arabic rectangle between the Greek and the Persian boxes carries only the language name and the reference TAD:28, no word. The form it stands for is دُلْفِين dulfīn, the Arabic name of the dolphin, a Hellenistic-period loan of Greek δελφίν (the accusative/late nominative by-form of δελφίς) that entered Arabic with the rest of the Greek zoological and medical vocabulary translated in ninth-century Baghdad; Greek δ- is rendered by د, the Greek -ῑν- gives the long ī of the Arabic pattern فُعْلِيل, and the word is treated as a quadriliteral noun. Nourai's own reference states this: al-ʿUnaysī, Tafsīr al-alfāẓ al-dakhīla p.28, 'دلفين — يوناني [δελφίν]، مرادفه اللاخس'. Nothing here to fault except that the box could have carried the word.\",\n     \"derivation_fa\": \"جعبهٔ نام‌دارِ بی‌واژه: در صفحهٔ چاپی مستطیلِ «عربی» میان جعبهٔ یونانی و جعبهٔ فارسی تنها نام زبان و ارجاع TAD:28 را دارد و هیچ واژه‌ای در آن نیست. واژه‌ای که جای آن خالی مانده «دُلْفین» است، نامِ عربیِ دلفین، وام‌واژه‌ای از یونانیِ δελφίν (صورتِ دیگرِ δελφίς) که در دورهٔ ترجمهٔ نهضتِ بغداد در سدهٔ سوم هجری همراه با دیگر واژگانِ جانورشناسی و پزشکیِ یونانی وارد عربی شد؛ δ یونانی با «د» نوشته می‌شود، ‎-ῑν-‎ یونانی به «ی»ی کشیده در وزنِ فُعْلیل بدل می‌گردد و واژه چهارحرفی به شمار می‌آید. خودِ مرجعِ نورایی همین را می‌گوید: طوبیا العنیسی، تفسیر الألفاظ الدخیلة، ص ۲۸: «دلفين — يوناني، مرادفه اللاخس». ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D8%AF%D9%84%D9%81%DB%8C%D9%86\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"TAD:28\", \"status\": \"supports\",\n       \"note\": \"TAD_pages.txt leaf 31 (= printed p.28; the same offset of 3 that puts فلس on leaf 55 = p.52) reads 'دلفين — يوناني [Greek form garbled in OCR] مرادفه اللاخس' in the د section, between دلغان and دلو. Al-ʿUnaysī marks the word Greek, exactly as the arrow requires.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. dolphin (KLN_1966.txt line 12026; leaf 259, running numbers 473-475)\", \"stance\": \"supports\",\n       \"note\": \"'fr. Gk. δελφίς, gen. δελφῖνος, \\\"dolphin\\\", which is rel. to δελφύς, \\\"womb\\\"' — establishes the Greek etymon that Arabic borrowed.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch, Etymologisches Wörterbuch (LKT.txt)\", \"stance\": \"silent\",\n       \"note\": \"no entry for دلفين — Lokotsch catalogues oriental words that entered European languages, and دلفين travelled the other way.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Persian\",\n     \"words\": \"dolfîn «دُلفین»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian دُلفین dolfin is the Arabic دُلْفِين dulfīn read with Persian vowels (Arabic u in a closed first syllable is regularly rendered o in Persian, and the Arabic long ī is kept), i.e. a Greek word that reached Persian through Arabic — precisely the route drawn. Wiktionary's Persian entry says so in as many words: 'Borrowed from Arabic دُلْفِين (dulfīn), from Ancient Greek δελφίν'. Moʿin's Farhang-e Fārsi, the reference Nourai cites, tags the headword '(دُ) [ یو. ] (اِ.) ۱- نوعی پستاندار دریایی بزرگ و بسیار باهوش. ۲- یکی از صورت‌های فلکی شمالی' — [یو.] = یونانی, Greek, and the second sense is the constellation Delphinus, which came into Persian with the Almagest tradition, another sign that the word arrived through the Arabic scientific literature rather than through modern French dauphin.\",\n     \"derivation_fa\": \"«دُلفین» فارسی همان «دُلْفین» عربی است که با واکه‌های فارسی خوانده می‌شود (ضمّهٔ عربی در هجای بستهٔ نخست در فارسی به «o» بدل می‌شود و «ی»ی کشیده می‌ماند)؛ یعنی واژه‌ای یونانی که از راهِ عربی به فارسی رسیده است — دقیقاً همان مسیری که در نمودار کشیده شده. ویکی‌واژه در مدخل فارسی می‌نویسد: «وام‌گرفته از عربیِ دُلْفِين، از یونانی باستان δελφίν». معین نیز — همان مرجعی که نورایی به آن ارجاع داده — مدخل را چنین آورده است: «(دُ) [ یو. ] (اِ.) ۱- نوعی پستاندار دریایی بزرگ و بسیار باهوش. ۲- یکی از صورت‌های فلکی شمالی»؛ نشانهٔ «[یو.]» یعنی یونانی، و معنای دوم صورتِ فلکیِ دلفین است که از راهِ سنّتِ مجسطی وارد فارسی شده — خود گواهی بر آنکه واژه از راهِ ادبِ علمیِ عربی آمده است نه از فرانسویِ امروزیِ dauphin. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D8%AF%D9%84%D9%81%DB%8C%D9%86\",\n      \"https://vajehyab.com/moein/%D8%AF%D9%84%D9%81%DB%8C%D9%86\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"MON:1552\", \"status\": \"supports\",\n       \"note\": \"Moʿin, Farhang-e Fārsi s.v. دلفین (read via vajehyab.com/moein/دلفین): '(دُ) [ یو. ] (اِ.) ۱- نوعی پستاندار دریایی بزرگ و بسیار باهوش. ۲- یکی از صورت های فلکی شمالی.' The origin tag [یو.] = یونانی. The page number is consistent with the د section of the continuously paginated lexicon volumes, though page numbers cannot be checked on the online text.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Fārsi s.v. دلفین (vajehyab)\", \"stance\": \"supports\",\n       \"note\": \"'[ یو. ]' — Moʿin classes the word as Greek, i.e. a Greek word naturalised in Persian, which is what the Greek→Arabic→Persian chain amounts to.\"},\n      {\"src\": \"TAD\", \"where\": \"al-ʿUnaysī p.28 (TAD_pages.txt leaf 31)\", \"stance\": \"supports\",\n       \"note\": \"'دلفين — يوناني ... مرادفه اللاخس' — the Arabic intermediary that Persian borrowed from.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ (BQT_v1/v2_pages.txt)\", \"stance\": \"silent\",\n       \"note\": \"no headword دلفین in the Borhān — a seventeenth-century Persian dictionary of 'pure Persian' words would not list a Greco-Arabic zoological term.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"dolphin, Philadelphia\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Both words are ultimately Greek, as drawn, but 'dolphin' did not come to English straight from Greek: Klein gives the full chain 'ME. delphin, delfyn, fr. OF. daulphin, dalfin (F. dauphin), fr. ML. dalfinus, fr. L. delphinus, delphin, fr. Gk. δελφίς, gen. δελφῖνος' — Greek → Latin → Medieval Latin (with the Latin -e- lowered to -a- in the Gallo-Romance forms) → Old French → Middle English, and the modern spelling with -ph- is a Renaissance re-latinisation of ME delfyn. Nourai's arrow skips Latin and French, which the Latin box he has already drawn in the Gwel 2 chart shows he was willing to draw when he wanted to. 'Philadelphia' is direct: Greek Φιλαδέλφεια, the Lydian city named after Attalus II Philadelphus, taken over unchanged by William Penn in 1682 for his Pennsylvania settlement, with the etymological sense 'brotherly love' revived deliberately for a Quaker colony. Verdict 'plausible' rather than 'confirmed' only because of the missing Latin/French links for dolphin.\",\n     \"derivation_fa\": \"هر دو واژه در نهایت یونانی‌اند، همان‌گونه که در نمودار آمده، امّا «dolphin» یکسره از یونانی به انگلیسی نرسیده است: کلاین زنجیرهٔ کامل را می‌دهد — «انگلیسیِ میانه delphin/delfyn، از فرانسویِ کهن daulphin/dalfin (فرانسویِ امروز dauphin)، از لاتینِ سده‌های میانه dalfinus، از لاتین delphinus، از یونانی δελφίς (اضافه δελφῖνος)» — یعنی یونانی ← لاتین ← لاتینِ میانه ← فرانسویِ کهن ← انگلیسیِ میانه؛ و املای امروزی با ‎-ph-‎ لاتینی‌سازیِ دوبارهٔ دورهٔ رنسانس است. پیکانِ نورایی حلقه‌های لاتین و فرانسوی را نادیده گرفته، حال آنکه در نمودارِ Gwel 2 همان صفحه جعبهٔ لاتین را کشیده است. «Philadelphia» امّا مستقیم است: یونانیِ Φιλαδέλφεια، نامِ شهری در لودیه به یادِ آتالوسِ دومِ فیلادلفوس، که ویلیام پن در ۱۶۸۲ آن را بی‌هیچ تغییر برای مستعمرهٔ کویکرِ خود در پنسیلوانیا برگزید و معنای ریشه‌ایِ «مهرِ برادرانه» را آگاهانه زنده کرد. حکمِ «با احتیاط پذیرفتنی» تنها به سببِ حذفِ حلقه‌های لاتین و فرانسوی در dolphin است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/calf\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"the English box carries no reference in the book; the claim was checked against Klein and Watkins instead.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. dolphin (KLN_1966.txt line 12026; leaf 259 ≈ pp.473-475)\", \"stance\": \"partial\",\n       \"note\": \"'dolphin, n. — ME. delphin, delfyn, fr. OF. daulphin, dalfin (F. dauphin), fr. ML. dalfinus, fr. L. delphinus, delphin, fr. Gk. δελφίς, gen. δελφῖνος, \\\"dolphin\\\", which is rel. to δελφύς, \\\"womb\\\"' — same origin, longer route than the chart draws. Klein s.v. dauphin (line 10385) adds the Delphinatus/Dauphiné story.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷelbh- and index (AHD_watkins1985.txt lines 542, 1432)\", \"stance\": \"supports\",\n       \"note\": \"the index line reads 'DOLPHIN gʷelbh-' and the article 'Greek delphus, womb, whence delphis, dolphin (referring to its shape): DELPHINIUM, DOLPHIN'.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary (WEB_vol1.txt)\", \"stance\": \"silent\",\n       \"note\": \"grep produced only 'beluga, a kind of dolphin' and similar incidental mentions; the main dolphin entry is not in the scanned volume held locally.\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"Persian\",\n     \"words\": \"Fîlâdelfîyâ «فیلادلفیا»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"فیلادلفیا is simply the Persian transcription of the place-name Philadelphia, taken over in the nineteenth and twentieth centuries with the rest of American geography through newspapers, atlases and Moʿin's aʿlām volumes. The rendering is the standard Persian treatment of a European proper name: English/Greek ph is written ف, the stressed vowels are lengthened to ا, and the final -ia is written ‎-یا‎; Persian has no independent access to the Greek Φιλαδέλφεια, so the arrow from English (rather than from Greek or French) is right for the modern city. Nothing about the form is anomalous; it is a borrowing of a name, not an etymological descent, and Nourai's chart shows it as such.\",\n     \"derivation_fa\": \"«فیلادلفیا» صرفاً آوانگاریِ فارسیِ نامِ جای Philadelphia است که در سده‌های سیزدهم و چهاردهم خورشیدی همراه با دیگر نام‌های جغرافیایِ آمریکا از راهِ روزنامه‌ها، اطلس‌ها و جلدهای اعلامِ فرهنگ معین وارد فارسی شد. شیوهٔ نگارش همان شیوهٔ همیشگیِ فارسی برای نام‌های خاصّ اروپایی است: «ph» با «ف» نوشته می‌شود، واکه‌های تکیه‌دار به «ا» کشیده می‌شوند و پایانهٔ ‎-ia‎ به ‎«یا»‎ بدل می‌گردد. فارسی هیچ راهِ مستقلی به Φιλαδέλφεια یونانی ندارد، پس پیکانی که از انگلیسی می‌آید (نه از یونانی یا فرانسوی) برای شهرِ امروزی درست است. این وام‌گیریِ یک نام است، نه تحوّلِ ریشه‌شناختی، و نمودار هم آن را همین‌گونه نشان می‌دهد. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"no reference in the book for this node; it is a transliteration of a modern place-name.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Fārsi, aʿlām volumes (vols 5-6)\", \"stance\": \"silent\",\n       \"note\": \"the local MON text files cover the lexicon volumes only; the aʿlām entry for فیلادلفیا could not be reached, and vajehyab exposes the lexicon, not the proper-name volumes.\"},\n      {\"src\": \"BOOK\", \"where\": \"printed page, pdf p. 207 (data/verification/sources/refs/ocr/BOOK/207.png)\", \"stance\": \"supports\",\n       \"note\": \"the page prints «فيلادلفيا» in the Persian box below the English one, matching the extraction; the arrow comes from the English box, not from Greek.\"}\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"Germanic\",\n     \"words\": \"kilbur\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The form is real but it is Old High German, not 'Germanic': kilburu (neut.) / chilburra (fem.) 'ewe lamb', matched by Old English cilforlamb, ceolforlamb 'ewe lamb' (whence dialectal English chilver). Nourai's gloss 'young animal' is Pokorny's gloss for the Avestan gərəbuš-, not for kilburra, which means specifically a female lamb. The attachment to *gʷelbʰ- is the old nineteenth-century view, printed by Pokorny 473 (the -es-stem 'reappears in Old High German kilburu, chilburra, Old English cilforlamb') and by Klein s.v. calf — but Pokorny in the same breath says these forms, together with Kalb, 'point to purely velar anlaut (as Gaulish-Latin galba and Gothic kilþei \\\"womb\\\")', that is, to *gel-, not to the labiovelar; Walde-Pokorny I 693 calls *gʷelbʰ-, *gʷerebʰ- and the bʰ-extensions of gel- separate but similar-sounding families that contaminated one another; and Buck 3.24 derives the Germanic group from *gel-bh- outright, conceding only that it was 'in part perh. blended with *gʷelbh-'. So the arrow is defensible but not established.\",\n     \"derivation_fa\": \"صورت واقعی است امّا آلمانیِ علیای باستان است، نه «ژرمنی»: kilburu (خنثی) / chilburra (مؤنّث) به معنای «برّهٔ ماده»، هم‌ارز با انگلیسیِ باستانِ cilforlamb «برّهٔ ماده» (که به گویشِ chilver رسیده). معنایی که نورایی داده («بچّهٔ جانور») در واقع معنای gərəbuš- اوستایی نزد پوکورنی است، نه معنای chilburra که ویژهٔ برّهٔ ماده است. پیوند دادنِ آن به *gʷelbʰ- دیدگاهِ کهنِ سدهٔ نوزدهم است که پوکورنی (ص ۴۷۳) و کلاین (ذیل calf) چاپ کرده‌اند؛ امّا پوکورنی در همان جمله می‌گوید این صورت‌ها همراه با Kalb «به آغازهٔ کامیِ ساده اشاره دارند (مانند galba در لاتینِ گُلی و kilþei گوتی به معنای زهدان)»، یعنی به *gel- نه به لبی‌کام؛ والده-پوکورنی (ج ۱ ص ۶۹۳) *gʷelbʰ- و *gʷerebʰ- و صورت‌های bʰ‌دارِ برآمده از gel- را «خانواده‌هایی جداگانه امّا هم‌آوا» می‌داند که بر هم اثر گذاشته‌اند؛ و باک (بند ۳٫۲۴) گروهِ ژرمنی را یکسره از *gel-bh- می‌گیرد و تنها می‌پذیرد که «شاید تا اندازه‌ای با *gʷelbh- درآمیخته باشد». پس این پیکان دفاع‌پذیر است ولی اثبات‌شده نیست.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/calf\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"contradicts\",\n       \"note\": \"Watkins 1985 s.v. gʷelbh- (AHD_watkins1985.txt lines 540-542) lists ONLY the Greek reflexes — delphus/delphis/adelphos, giving DELPHINIUM, DOLPHIN, -ADELPHOUS — and no Germanic material at all; the index line 'DOLPHIN gʷelbh-' has no companion 'CALF gʷelbh-'. Nourai's bare 'AHD' citation for a Germanic kilbur under this root is not borne out by the appendix.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"Pokorny 473 (POK_full.txt line ~39093)\", \"stance\": \"partial\",\n       \"note\": \"'the -es-stem reappears in Old High German kilburu, chilburra f. \\\"mother lamb\\\", Old English cilforlamb ds. ... and — with gradation o after o-stem as δολφός, garbha-h — Modern High German Kalb ... which point to purely velar anlaut (as Gaulish-Latin galba and Gothic kilþei \\\"womb\\\" etc.)' — Pokorny prints the forms here but says their anlaut points away from *gʷ-.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. calf (KLN_1966.txt line 6181)\", \"stance\": \"supports\",\n       \"note\": \"'OHG. kilbur (neut.), kilburra (fem.), OE. cilforlamb, ceolforlamb, \\\"ewe lamb\\\", fr. I.-E. base *gwelbh-, *gwolbh-, \\\"womb; young of an animal\\\" ... Cp. also chilver.'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 3.24 'calf' (SYN.txt line 4167)\", \"stance\": \"contradicts\",\n       \"note\": \"'Goth. kalbō \\\"female calf\\\", ON kalfr, OE cealf, etc. ... fr. *gel-bh- an extension of *gel- in Skt. gula- \\\"ball\\\", Lat. galla \\\"gallnut\\\", parallel to *gel-t- in Goth. kilþei \\\"womb\\\", OE cild \\\"child\\\" ... But in part perh. blended with *gʷelbh- in Grk. δελφύς, Skt. garbha- \\\"womb\\\", etc.'\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 693 (WLD_Bd1_pages.txt leaf 701)\", \"stance\": \"contradicts\",\n       \"note\": \"'liegen verschiedene, aber lautähnliche und daher gegenseitiger Beeinflussung ausgesetzte Sippen vor: *gʷelbh-, *gʷerebh-, und aus gel- erweiterte bh-Formen, die aber im Germ. vermutlich durch Aufsaugung von gʷelbh-Formen deren Stammbildung und spezifische Bed. übernommen haben.'\"}\n     ]\n    },\n    {\n     \"id\": 9,\n     \"lang\": \"English\",\n     \"words\": \"calf\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"English calf goes back to Old English cealf (Anglian celf), from Proto-Germanic *kalbaz / n-stem *kalbōn- (Gothic kalbō 'heifer', Old Norse kálfr, Old High German kalb, German Kalb), with the regular West Saxon breaking of e before l + consonant and the later loss of the -l- in the pronunciation /kɑːf/. It is therefore a sister of, not a descendant of, OHG kilburu 'ewe lamb': kilburu/cilfor- continues an -es-/-r- stem *kelb-uz-, calf an o- or n-stem *kalb-az-, and Nourai's arrow, which makes calf come out of kilbur, mis-states a relation of collateral formations as one of descent. (The direct English continuation of kilbur is dialectal chilver 'ewe lamb', which the chart does not have.) Beyond that, the whole Germanic group's link to *gʷelbʰ- is now doubted: Wiktionary, following Kroonen, gives 'from Proto-Germanic *kalbaz, further etymology unknown', and Buck derives it from *gel-bh-. So the semantics ('young of an animal') and the family are right, the intermediate step is not.\",\n     \"derivation_fa\": \"واژهٔ انگلیسیِ calf به انگلیسیِ باستانِ cealf (در گویشِ آنگلی celf) بازمی‌گردد، از ژرمنیِ آغازینِ *kalbaz / ستاکِ ‎n‎ـیِ *kalbōn- (گوتی kalbō «گوسالهٔ ماده»، نورسِ کهن kálfr، آلمانیِ علیای باستان kalb، آلمانیِ امروز Kalb)، با شکستِ قاعده‌مندِ واکه پیش از l + همخوان در وِست‌ساکسون و سپس افتادنِ l در تلفّظِ امروزی /kɑːf/. پس calf «خواهرِ» kilburu است نه «فرزندِ» آن: kilburu/cilfor- بازماندهٔ ستاکِ ‎-es-/-r-‎ یعنی *kelb-uz- است و calf بازماندهٔ ستاکِ ‎o-‎ یا ‎n-‎ یعنی *kalb-az-؛ پیکانِ نورایی که calf را از kilbur بیرون می‌آورد، رابطهٔ دو ساختِ هم‌عرض را به رابطهٔ نیا و فرزند بدل کرده است. (بازماندهٔ مستقیمِ kilbur در انگلیسی واژهٔ گویشیِ chilver «برّهٔ ماده» است که در نمودار نیامده.) افزون بر این، پیوندِ کلِّ گروهِ ژرمنی با *gʷelbʰ- امروز مورد تردید است: ویکی‌واژه به پیروی از کرونن می‌نویسد «از ژرمنیِ آغازینِ *kalbaz، ریشهٔ فراتر ناشناخته»، و باک آن را از *gel-bh- می‌گیرد. پس معنا («بچّهٔ جانور») و خانواده درست است، امّا حلقهٔ میانی نادرست.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/calf\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"the English box carries no reference in the book; checked against Klein, Buck, Pokorny and Wiktionary instead.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. calf (KLN_1966.txt line 6181; leaf 128, running numbers 222/223)\", \"stance\": \"partial\",\n       \"note\": \"'calf, n., young of a cow, etc. — ME. calf, kalf, fr. OE. cealf, rel. to OS., MDu. calf, ON. kalfr, Dan. kalv, Swed., Du. kalf, OHG. chalp, kalb, MHG. kalp, G. Kalb, Goth. kalbō, \\\"calf\\\", OHG. kilbur (neut.), kilburra (fem.), OE. cilforlamb ... fr. I.-E. base *gwelbh-' — Klein puts calf and kilbur side by side as RELATED forms of one base, not one from the other.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 3.24 'calf' (SYN.txt line 4167)\", \"stance\": \"contradicts\",\n       \"note\": \"'Goth. kalbō \\\"female calf\\\", ON kalfr, OE cealf, etc., same word as ON kalfr \\\"calf of the leg\\\", fr. *gel-bh- an extension of *gel- ... In any case \\\"calf\\\" is a specialization of \\\"young of an animal\\\".'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985, appendix index and s.v. gʷelbh-\", \"stance\": \"silent\",\n       \"note\": \"CALF is not indexed under gʷelbh- (nor is it in the article), so the AHD appendix gives the chart no support here.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-207.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk207.py && python3 -m json.tool data/verification/page-207.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 207"
}
```


### [2026-09-06T15:11:34.780Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk207.py", line 243, in <module>
    "lang": null,
            ^^^^
NameError: name 'null' is not defined
```


## [2026-09-06T15:11:40.470Z] TOOL CALL #77: Bash

```json
{
 "command": "sed -i 's/^     \"lang\": null,$/     \"lang\": None,/' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk207.py && python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk207.py && python3 -m json.tool data/verification/page-207.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 207"
}
```


### [2026-09-06T15:11:43.099Z] TOOL RESULT

```
written
JSON OK
nodes verified: 15/15
node verdicts: {'disputed': 2, 'plausible': 5, 'confirmed': 7, 'unverified': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 11, 'partial': 3, 'not_checked': 7, 'contradicts': 1}
books consulted: {'contradicts': 5, 'silent': 14, 'partial': 7, 'supports': 17} | by book: {'AHD': 5, 'KLN': 5, 'MON': 4, 'SYN': 4, 'WLD': 3, 'LKT': 3, 'WEB': 3, 'SKT': 2, 'BRT': 2, 'BOOK': 2, 'PHD': 1, 'HRN': 1, 'HUB': 1, 'AFM': 1, 'FVQ': 1, 'PLA': 1, 'FSD': 1, 'TAD': 1, 'BQT': 1, 'POK': 1}
```


## [2026-09-06T15:12:03.301Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-207.json` written, valid JSON, `verify_check.py 207` reports **0 PROBLEM lines** (15/15 nodes).

**Page 207 (book p. 177) — 2 entries, 15 nodes**
- Root verdicts: confirmed 2 (Gwel 2 = Pokorny gʷel-1 "to stick; pain, death" p.470-471; Gwelbh = Pokorny gʷelbʰ- "womb; young of animal" p.473 — both root box, gloss and page numbers check out exactly).
- Node verdicts: confirmed 7, plausible 5, disputed 2, unverified 1.

**Disputed**
- Gwel 2 #1 Greek *obelos, obolos* — Pokorny 470 does list them under the root, but Walde-Pokorny I 690 already warned "dessen ὀ- den Anschluß erschwert", Klein calls ὀβελός "of uncertain origin", Watkins drops it, Beekes/Wiktionary call it Pre-Greek. The IE attachment is now rejected.
- Gwel 2 #3 Arabic *fals, fulūs, iflās, muflis* — not from ὀβολός. Lokotsch nos. 581/1491 and Wiktionary: Arabic فلس ← Aramaic pūlsā ← Greek φόλλις ← Latin *follis*; the "fish scale" sense is a third etymon (Gk φολίς). Nourai's own ref TAD:52 does say "Greek obol", but it is a 1932 guess.

**Transcription flag (book's own misprint, extraction faithful)**
- Gwel 2 #1 prints **"obelekos"**; the correct form is ὀβελίσκος *obeliskos* (Klein s.v. obelisk). Verified against the printed page, copied to `data/verification/sources/refs/ocr/BOOK/207.png`. Recorded on the node as `error_in: "book"`.

**No extraction errors** — the JSON matches the printed page everywhere, including the two deliberately empty boxes (blank rectangle beside the Avestan box → `unverified`; Arabic TAD:28 box with a language label but no word → `confirmed`, it stands for دُلْفِين).

**Notable ref findings**
- BQT:428 located (BQT_v1_pages.txt leaf 654): "پول بر وزن غول. معروف است و بعربی فلوس گویند" — explains why Nourai cites the same page twice; Moʿin's footnote there is cut off, so it confirms the word, not the Greek origin.
- Moʿin tags both پول and دلفین "[یو.]" (Greek), supporting nodes #2 and #5; MacKenzie, Horn and Hübschmann know only *pul* "bridge", so the MP *pōl is a reconstruction (node #2 → plausible).
- Germanic branch (#8, #9) downgraded to plausible: Pokorny himself says kilburra/Kalb "point to purely velar anlaut", Buck 3.24 derives them from *gel-bh-, Watkins omits CALF from gʷelbʰ- (so Nourai's bare "AHD" citation contradicts), and calf < *kalbaz is a sister of, not a descendant of, kilbur.
- Page-number caveat worth knowing for future pages: Nourai's KLN:483 doesn't land in the 1966 two-volume pagination (calf ≈ p.222, dolphin ≈ pp.473-475, p.483 is in "dr-"); KLN:1068 and TAD:28/52 do land exactly.
