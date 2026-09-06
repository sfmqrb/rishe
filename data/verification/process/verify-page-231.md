# Verification process log — verify-page-231


## [2026-09-06T15:27:58.241Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 231 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-231.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-231.json. Write /home/sfmqrb/git/rishe/data/verification/page-231.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 231` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:27:59.736Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:28:00.445Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:28:00.463Z] TOOL RESULT

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


## [2026-09-06T15:28:00.626Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-231.txt"
}
```


### [2026-09-06T15:28:00.666Z] TOOL RESULT

```
1	=== PDF page 231 (book page 201) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kâ 1, Qâ : to wish, desire  (refs POK:515)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:515 | kâ 2, kâm 2, kâma : desire
5	  #2 (parent #1) [Sogdian] refs=SOD:186 | k`m : wish, desire
6	  #3 (parent #1) [Pahlavi] refs=BQT:1578; SNS:209 | kâm : desire
7	    #4 (parent #3) [Persian] refs=BQT:1578 | kâm 1 «کام ۱» : desire | extra: کامیاب ، کامکار
8	#5 (parent #0) [Avestan / Old Persian] refs=POK:515; KNT:173 | čanah, činah, činman : desire ; aspa-canah : horse lover ☞Ekwos
9	  #6 (parent #5) [None] refs=None | 
10	#7 (parent #0) [Germanic] refs=KLN:1743 | hôraz : one who desires
11	  #8 (parent #7) [English] refs=None | whore
12	#9 (parent #0) [Latin] refs=POK:515 | carus : desire
13	  #10 (parent #9) [English] refs=None | caress, charity, cherish
14	--- entry 1 ---
15	ROOT Ka 2 -> redirect to Kwon
16	--- entry 2 ---
17	ROOT [Arabic] K.a`.b : cube  (refs FVA:353; KLN:380; PHN:131)
18	#1 (parent #0) [Persian] refs=FVA:353 | ka`b «کَعب» : ankle bone, cube root ; Ka`beh «کعبه» : Kaaba, center point ; moka`ab «مکعب» : cube, cubic
19	#2 (parent #0) [English] refs=AHD:713 | Kaaba, Caaba
20	#3 (parent #0) [Greek] refs=KLN:380; PHN:131 | kubos, kybos : cube | NOTE: POK:589 & AHD:320 derive Greek "kubos:cube" from Indo-European "Keube:hump, bent". See root "Gěu 1"
21	  #4 (parent #3) [Latin] refs=WEB:441; FSD:626 | cubus : cube
22	    #5 (parent #4) [English] refs=AHD:320 | cube
23	
```


## [2026-09-06T15:28:03.580Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-231.json",
 "description": "Read source JSON page 231"
}
```


### [2026-09-06T15:28:03.616Z] TOOL RESULT

```
{
  "pdf_page": 231,
  "book_page": 201,
  "entries": [
    {
      "root": {
        "name": "Kâ 1, Qâ",
        "lang": "Indo-European",
        "refs": "POK:515",
        "gloss": "to wish, desire"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:515",
          "words": [
            {"translit": "kâ 2, kâm 2, kâma", "gloss": "desire", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:186",
          "words": [
            {"translit": "k`m", "gloss": "wish, desire", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:1578; SNS:209",
          "words": [
            {"translit": "kâm", "gloss": "desire", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:1578",
          "words": [
            {"translit": "kâm 1", "gloss": "desire", "script": "کام ۱"}
          ],
          "script_extra": "کامیاب ، کامکار",
          "note": null,
          "quote": {"text": "به یزدان چنین دارم امّید و کام - که این ماه نو را ببینم تمام", "poet": "Asadî"}
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:515; KNT:173",
          "words": [
            {"translit": "čanah, činah, činman", "gloss": "desire", "script": null},
            {"translit": "aspa-canah", "gloss": "horse lover", "script": null, "see": ["Ekwos"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Germanic",
          "refs": "KLN:1743",
          "words": [
            {"translit": "hôraz", "gloss": "one who desires", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "whore", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:515",
          "words": [
            {"translit": "carus", "gloss": "desire", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "caress, charity, cherish", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Ka 2", "redirect": "Kwon"},
      "nodes": []
    },
    {
      "root": {
        "name": "K.a`.b",
        "lang": "Arabic",
        "refs": "FVA:353; KLN:380; PHN:131",
        "gloss": "cube"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "FVA:353",
          "words": [
            {"translit": "ka`b", "gloss": "ankle bone, cube root", "script": "کَعب"},
            {"translit": "Ka`beh", "gloss": "Kaaba, center point", "script": "کعبه"},
            {"translit": "moka`ab", "gloss": "cube, cubic", "script": "مکعب"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "به طواف کعبه رفتم به حرم رهم ندادند - که تو در برون چه کردی که درون خانه آیی", "poet": "Erâqî"}
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "English",
          "refs": "AHD:713",
          "words": [
            {"translit": "Kaaba, Caaba", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:380; PHN:131",
          "words": [
            {"translit": "kubos, kybos", "gloss": "cube", "script": null}
          ],
          "script_extra": null,
          "note": "POK:589 & AHD:320 derive Greek \"kubos:cube\" from Indo-European \"Keube:hump, bent\". See root \"Gěu 1\"",
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Latin",
          "refs": "WEB:441; FSD:626",
          "words": [
            {"translit": "cubus", "gloss": "cube", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:320",
          "words": [
            {"translit": "cube", "gloss": null, "script": null}
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


## [2026-09-06T15:28:06.061Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SOD','BQT','SNS','KNT','KLN','FVA','PHN','AHD','WEB','FSD','WLD','MON','HRN','HUB','BRT','PHD','NYB','IEC','SYN','SKT','ARY','CHEUNG']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Inspect refs_online keys"
}
```


### [2026-09-06T15:28:07.726Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 202
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verific
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG MISSING
```


## [2026-09-06T15:28:14.397Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SOD','BQT','SNS','KNT','KLN','PHN','AHD','WEB','FSD','WLD','IEC','SYN','SKT','BRT','PHD','NYB','HRN','HUB','ARY','FVA','FVQ','AFM','PLA','LKT','DEV','DOZ']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print('==',k, '| local_file:', v.get('local_file'), '| offset:', v.get('page_offset'))\n    print('   hint:', (v.get('lookup_hint') or '')[:300])\n\"; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -80"
}
```


## [2026-09-06T15:28:15.170Z] TOOL CALL #6: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md | head -120"
}
```


### [2026-09-06T15:28:16.107Z] TOOL RESULT

```
== POK | local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== SOD | local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt'] | offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
   hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (retur
== BQT | local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
   hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== SNS | local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt'] | offset: 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
   hint: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
== KNT | local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt | offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
== KLN | local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== PHN | local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt | offset: leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.
== AHD | local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
   hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== WEB | local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt | offset: not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.
== FSD | local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
== WLD | local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
   hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
== IEC | local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== SYN | local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== SKT | local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== BRT | local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== PHD | local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== NYB | local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== HRN | local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== HUB | local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== ARY | local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | offset: printed page = pdf page + 1
   hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
== FVA | local_file: None | offset: None
   hint: Searched archive.org, ketabnak, noorlib, web: no digital copy found.
== FVQ | local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] | offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves)
   hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
== AFM | local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt'] | offset: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image
   hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').
== PLA | local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] | offset: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
   hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
== LKT | local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt | offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
== DEV | local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt | offset: leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: French headword in caps at line start.
== DOZ | local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt | offset: leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Dutch headword in caps at line start.
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
```


### [2026-09-06T15:28:16.137Z] TOOL RESULT

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


## [2026-09-06T15:28:42.054Z] AGENT

Now let me check the local reference texts.


## [2026-09-06T15:28:43.429Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt; do echo \"=== $f leaves: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f)\"; done\necho \"--- POK_full lemma search\"\ngrep -n \"Page(s): 51[0-9]\" POK_full.txt | head -30"
}
```


## [2026-09-06T15:28:44.573Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full ka- lemma\"\ngrep -n \"lemma: kā-\" POK_full.txt | head\ngrep -n \"lemma: k.*begehren\" POK_full.txt | head"
}
```


### [2026-09-06T15:28:45.278Z] TOOL RESULT

```
=== POK_01.txt leaves: 363
=== POK_02.txt leaves: 433
=== POK_03.txt leaves: 429
--- POK_full lemma search
41473:Page(s): 511-512 
41826:Page(s): 510-511 
41843:Page(s): 511 
42720:Page(s): 513-514 
42750:Page(s): 514 
43136:Page(s): 517-518 
43166:Page(s): 519-520 
44458:Page(s): 515 
44480:Page(s): 515-516 
49304:Page(s): 516-517 
49474:Page(s): 517
```


### [2026-09-06T15:28:45.334Z] TOOL RESULT

```
=== POK_full ka- lemma
```


## [2026-09-06T15:28:47.327Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '44430,44500p' POK_full.txt"
}
```


### [2026-09-06T15:28:47.375Z] TOOL RESULT

```
'starve'. 

no-stem: Latin cams 'dear, worth, precious (also of price)'; Gothic hors {* hora-) ' 
adulterer, Hurer', Old Icelandic horrds., horn. ' wooing, lubricity ', Old English horn, ds.. 
Old High German huorn. ds.. Old High German huora {and huorrairom *hdridn-) ' whore ', 
Old English hore. Old Icelandic hora- {*hdrdn-) ds.; Latvian kars^ lascivious, covetous ' 
{karudt^\us\, crave, long, want'); 

reduced grade gall. Carant-us, -/7/us etc., abrit. Carant-Tnus, -orius. Old Irish caraim 
'love', ca^ae 'friend'; cymr. corn. bret. ca^'friend' {*k9-rant-s), cymr. carar\ love'; about 
(gall.?) caris(s)as. WH. I 169; Tocharian Akk. Sg. A krant, B krent'goo6' (= Celtic carant-). 

Based on Aryan kan-{0\6 Indie Perf. cakana, Aor. akanisam, Avestan cakana), can- 
(Old Indie canistam; Old Indie canas-n. ' pleasure, satisfaction', Avestan canah-, cinah- 



'desire, demand') " be given satisfaction, find pleasure ', Avestan cinman-r\. " lust, strive ' 
in a Indo Germanic -{e)nes- stem k-e-nes-1 The forms cani-, kani- can also be secondary 
as kami-syate, -tar- besides kama- (if Stokes KZ. 40, 246 has rightly compared Middle 
Irish cin. Gen. cenalove, affection ' as *kenu-, would be assessed k-en- : ka-as ks-en- : 
kes-). 

Old Indie cam- 'pleasant, welcome, mellifluous', cayamana-^ covetous ', nicayya- (is., 
cayu-^ yearning', with previously Indie replacement from /rthrough c after the concurrent 
from Aa/7-and can- {see above). 

References: WP. I 325 f., WH. I 169, 175, 885, 886, Pedersen Tocharian 109, 234. 
Page(s): 515 

Root / lemma: ka, ke, kom 

Meaning: a kind of particle (all right?) 

Material: Old Indie kam behind dative from Personen (as Dat. commodi; so also once 

Avestan k^m) and from abstract (as final dative), also in Imper., after the particles nu, su, 

hi, and in indik. main clause; 

Old Church Slavic k-b(n)^\\\\ Dat. "to'. 

Nasallos gr. kq, ke (kev could have v ecpeAkugtikov) perhaps 'probably', modal particle, 
Slavic -ka{-ko, -ku, -ki, -kiD, -ce, -ci, -cu), affixture particle esp. by Pron., through Imper. 
and through Adv., also probably ko- as preposition in Verbal- and nominal compound (e.g. 
russ. k6-voroti3 ' cervical vertebra, nape '); 

Lithuanian -A/(perhaps originally kd), -/rin Imper. (e.g. duoki, -/r" give !'). 

References: WP. I 326, Schwyzer Gr. Gr. II 568, Trautmann 111f. 
Page(s): 515-516 

Root / lemma: ked- 

Meaning: to smoke, fume 

Material: Old Indie kadru- ^bro\Nn\ perhaps also kadamba-m. " Nauelea cadamba, a tree 

with orange flowers ' and kadamba- m. ' a kind of goose with dark grey wings '; 

Old Church Slavic kadilo^ incense ', kaditT fume ', russ. dao^'haze, mist', serb. cad^ be 
dark, gloomy, misty ', caditi^ become sooty ' (etc., s. Berneker 133, 467), perhaps Old 
Prussian accodis ( *at-codis) ' Rauchloch, durch das der Rauch herauszieht '; 



These are placed as " Raucnernolzer ' (?): 

gr. K£5po(; " juniper; later: Pinus cedrus', K£5pi(; " juniper berry; fruit of cedar '; Lithuanian 
kadagys. Old Prussian kadegis^ juniper' (borrowed from Estonian kadakasl).
```


## [2026-09-06T15:28:50.199Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '44400,44432p' POK_full.txt"
}
```


### [2026-09-06T15:28:50.254Z] TOOL RESULT

```
loud call, shout, cry, name'; russ. sycb " midget owl, sparrow owl ', Czech syc'owl ' {*Ruk- 
ti-)\ doubtful Old Church Slavic 5^/r7b 'noise' {*Reu-mo-sl Brugmann l|2 1, 247). 

Maybe alb. zhurme^'r\d\se' a Slavic loanword. 

compare Suolahti Dt. bird name 185 (here about the neologism Old High German kaha 
"jackdaw' etc.; compare Lithuanian kovaseic. ds.). 

References: WP. I 331 f., WH. I 184, 190, 298, Trautmann 122. 
Page(s): 535-536 

Root / lemma: ka- 
Meaning: to like, wish 

Material: Old Indie kayamana-^ having with pleasure ' {a-kay/ya-' desirable ' with from this 
Jo-present carried-y-), Perf. cakS^ take pleasure in, love, long for ', -kaf/- (in compound) " 
demanding, requiring '; Avestan ka-'\ong, want' {kaya^. Sg., kata-, cakuse); 

-/770stem Old Indie kama-m. " lust, wish, love', Avestan Old pers. kama- m. 'desire, 
wish'; 

Note: 

-/77-stem is of Greek lllyrian origin. 

kam-\v\ Old Indie kamayati, particle Perf. Med. cakamana-, /r5/77/'a- 'charming, beautiful', 
kamana-^ eager, avid, lascivious '; Lithuanian kamaros^\us\., desire' and Latvian kamet 
'starve'. 

no-stem: Latin cams 'dear, worth, precious (also of price)'; Gothic hors {* hora-) '
```


## [2026-09-06T15:28:58.369Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_02 leaf 171 (p.515?)\"\nawk 'BEGIN{RS=\"\\f\"} NR==172' POK_02.txt | head -60"
}
```


## [2026-09-06T15:28:59.397Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins ka- / whore\"\ngrep -n -i \"whore\" AHD_watkins1985.txt | head -20\necho \"--- kā- root\"\ngrep -n \"^kā-\" AHD_watkins1985.txt | head"
}
```


### [2026-09-06T15:29:00.140Z] TOOL RESULT

```
=== POK_02 leaf 171 (p.515?)
nfluß  von  ein  ,ein^  anzunehmen.
WP.  I  208  f.,    Kluge  11  126.
iofk-  _,Tier  aus  der  Gruppe  der  Rehe^
Gr.  ^OQ^j  ^OQy.ag,  mit  volksetym.  Anschluß  an  dsQxofxai  meist  ööq^,  öogy^ög-, dogycdg  f.,  dÖQy.og  m.  ,Reh,  Gazelle^;
gallo-rom.  *iorkos  ,Reh',  cjmr.  iwrch  ,caprea  mas',  corn.  yorch,  bret. iourc'h  ,Reh'  (vermutlich  aus  dem  Keltischen  stammen  die  späteren  ver- einzelten Formen  tb^xog,  io^xsg,  Yvoxeg  bei  Opp.  und  Hes.);  gall.  FN  Jurca.
WP.  I  209;  M.-L.  9678.
iou,  iu  .schon'^,  s.  oben  S.  285.
iö[u]s-  :  iüs-,  (vermutlich  zu  2.  ieu-)  , gürten^;  iös-to-s  ,gegürtet^,  iös-men- n.  ,Gurt'.
Av.  yäti^hayeiti  (meist  mit  aiwi-)  ,gürtet^,  Partiz.  yästa-  ,gegürtet^,  yäh n.  ;Gürtelschnur^;
gr.  tibwvixi  ,gürte',Xf^(TT6g  (=  av.  yästa-,  lit.  jüostas)  , gegürtet',  CcüOtt^q ,,GürteP,  ^ü)^a  ds.  (^toja-^a  vgl.  lit.  juosmud  ,Gurt'),  ^cowj  ds.  (%a)a-vä, vgl.  russ.-ksL poj asm  ds.);  ^ovad-o)'  Liawvad-u  Hes.  etwa  thessal.  =  ^cbaS-o)?
alb.  n-gjehs  ,ich  gürte';
lit.  jüosiu,  jüosti  .gürten',  jüostas  ,gegürtet',  jüosta  , Gürtel'  neben  pa- jüseti  ,gürten'  (Ablaut  öw.ü)]
a^Lsl.  pojaiQy  -jasati  ,gürten',  'pojasT>  , Gürtel'  (usw.,  siehe  Berneker  449).
WP.  I  209,  Schwyzer  Gr.  Gr.  I  330,  Trautmann  108  f.
I.  iu-   ,ihr'  ursprüngl.  nur  Nom. ;    Kasus   obliqui  vom  St.  "es-,    u6s-   (aus *iues.  *iuos?). 1.  Ai.  yuvdm  ,ihr'  Du.,  yüydm  PL,  av.  yv^rrij  gathav.  yüs\ arm.  nachwirkend  in  den  mit  je-  anlaut.  Kasus  z.  B.  Dat.  jez  (e  nach mez  ,nobis',  liez  ,tibi');
got.  jus  ,ihr'  PL,  sonst  nach  ,wir'  (s.  ue-)  umgebildet  aisl.  er,  ags.  gEj as.  g%j  ge,  ahd.  ir]  Du.  got.  *ju-t  (:  lit.  jii-du),  sonst  nach  ,wir'  umgebildet aisl.  itj  ags.  as.  git)
33
514  ,
litjüSj  lett.  jus,  pr.  ioüs,  iaüs  ,\hr'  PL,  \\t.  ju-du  ,ihr  beide';  apr.  iouson^ lit.  jiisij(>,  lett.  jusu  ,euer^ ues-,  u^S'i    ai.  vah,  av.  vä  enkl.  für  Akk.  Gen.   Dat.  PL,   Dual   ai.  väm- vom^Akk.   *us-sme  (=  lesb.  {/^u^tfi)   aus   mit   Übernalime    des   nominativi- sehen  i-  ai.  yusmän  Akk.  (usw.),  av.  Abi.  yü§mat-
gr.  lesb.  if^u/i«  (*ms-sw-),  dor.  ifis  Akk.,  daraus  nom.  lesb.  i'^^eg,  dor. ^^<fg,  sowie  att.  i^etg  usw.;
alb.  ^'w  ,ihr'  aus  *u  ==  ai.  vah  mit  hiatustilgendem  ^■- ;
lat.  vös  (=  av.  Akk.  PL  vä?),  pälign.  vus  ,vos'  und  ,vobis^,  la
```


### [2026-09-06T15:29:00.198Z] TOOL RESULT

```
=== AHD watkins ka- / whore
560:ka-. To like, desire. Contracted from *kaa-. 1. Suffixed form *kd-ro- in: a. Germanic *héraz (feminine *hérén-), “one who desires,” adulterer, in (i) Old English hére, whore: WHORE (ii) Old Norse compound hérdémr, whore- dom (-démr, “condition”; see dhé-'): WHOREDOM; b. Latin cdrus, dear: CARESS, CHARITY, CHERISH. 2. Suf- fixed form *kd-mo- in Sanskrit kdmah, love, desire: Kama; KaMAsuTRA. [Pok. kd- 515.]
--- kā- root
```


## [2026-09-06T15:29:10.484Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_02 leaf 174\"\nawk 'BEGIN{RS=\"\\f\"} NR==174' POK_02.txt | grep -n -i -E \"kä|kama|hors|carus|canah|cinah|cinman|begehr\" | head -40\necho \"=== search POK_02 for 'kämo' / carus\"\ngrep -n \"cakuse\\|kayamäna\\|cinman\\|cinah\" POK_02.txt | head"
}
```


## [2026-09-06T15:29:11.259Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT leaf 188 (p.173)\"\nawk 'BEGIN{RS=\"\\f\"} NR==189' KNT.txt | head -60"
}
```


### [2026-09-06T15:29:12.603Z] TOOL RESULT

```
=== POK_02 leaf 174
1:mänd-]  kamra-  ^reizend,  scbön^, kamana-  ^begierig,  lüstern^;  lit.  kamaros  ,Geilheit^  und  lett.  kämet  ,hungern^
2:ro-St. :  lat.  cärus  ,lieb,  wert,  teuer  (auch  vom  Preise)^;  got.  hors  (*höra-} ,Ehebrecher,  Hurer',  aisl.  hörr  ds.,  hör  n.  ,Buhlerei,  Unzucht',  ags.  hör  n. ds.,  ahd.  huor  n.  ds.,  ahd.  huora  (und  huorra  aus  *höriön-)  ,Hure',  ags. Äöre,  aisl.  höra-  (*hörön-)  ds.;  lett.  kärs  ,lüstern,  begehrlich'  (käruot  ,be- gehren,  verlangen');
4:Beruht  ar.  kan-  (ai.  Perf.  cäkana^  Aor.  akänisam,  av.  cakana),  can-  (ai.  cani- stdm'y  ai.  cänas-  n.  ,Gefallen,  Befriedigung',  av.  canah-,  cinah-  ,y erlangen. Heischen')  ,befriedigt  sein.  Gefallen  finden',  av.  cinman-  n.  ,Begehren, Trachten'  auf  einem  idg.  -(e)wes-St.  k-e-nes-?  Die  Formen  cani-j  kani- können  ebenso  sekundär  sein  wie  kami-syate,  -tar-  neben  käma-  (wenn Stokes  KZ.  40,  246  mit  Recht  mir.  ein,  Gen.  cena  , Liebe,  Zuneigung'  als *kenu-  vergliche,  wäre  k-en-  :  kä-  wie  ks-en-  :  kes-  u.  dgl.  zu  beurteilen).
5:Ai.  cdru-  ,angenehm,  willkommen,  lieblich',  cäyamäna-  »begehrlich', nicäyya-  ds.,  cäyü-  , begehrend',  mit  erst  ind.  Ersatz  von  k  durch  c  nach dem  Nebeneinander  von  kan-  und  can-  (s.  oben).
17:Ai.  kadana-  n.  .Vernichtung',  cakäda  (unsicher,  ob  nicht  cakära?)  kada^
=== search POK_02 for 'kämo' / carus
2602:Beruht  ar.  kan-  (ai.  Perf.  cäkana^  Aor.  akänisam,  av.  cakana),  can-  (ai.  cani- stdm'y  ai.  cänas-  n.  ,Gefallen,  Befriedigung',  av.  canah-,  cinah-  ,y erlangen. Heischen')  ,befriedigt  sein.  Gefallen  finden',  av.  cinman-  n.  ,Begehren, Trachten'  auf  einem  idg.  -(e)wes-St.  k-e-nes-?  Die  Formen  cani-j  kani- können  ebenso  sekundär  sein  wie  kami-syate,  -tar-  neben  käma-  (wenn Stokes  KZ.  40,  246  mit  Recht  mir.  ein,  Gen.  cena  , Liebe,  Zuneigung'  als *kenu-  vergliche,  wäre  k-en-  :  kä-  wie  ks-en-  :  kes-  u.  dgl.  zu  beurteilen).
```


### [2026-09-06T15:29:14.879Z] TOOL RESULT

```
=== KNT leaf 188 (p.173)
’, as taken by ТИМ. Aiw 322-3; otherwise Hz. Ap! 191-2: hadtya- ‘truth’, with late loss of h-, + deriv. of d-baud- ‘be fragrant’, cf. Av. baoót- ‘fra-
OLD PERSIAN
grance’, therefore ‘having the fragrance of the truth’).  <Aé@iydbausinahya gsm. Sa 4-7.
Aéura sb. ‘Assyria (and Syria)’, a province of the Persian Empire ($6, $106.11): Elam. aš- &i-ra, АКК. áš-šur, Gk. 'Аттурв‚ but Aram. абиг. Aéuré nsf. DB 1.14f; 2.7; DPe 11; DNa 26f; DSe 26°; DSm 7°; XPh 22. Aéurayd lsf. (5186) DB 2.58f.
A@uriya- adj. ‘Assyrian’: deriv. to preceding .
($144.1), perhaps with vriddhi in first syllable (8126; Aburiya- ?). A@uriya пет. DN xvii; DSf 32; А?Р 17.
Agina- sb. ‘Acina’, ап Elamite rebel: Elam. ka-iš-ši-na, Akk. a-Si-na. Either borrowed from Elam. (Foy, KZ 37.498); or shortened from an IE name beginning with OP äç- = Av. átar- 007- ‘fire’ ($147.11, §152.1), ef. atoro-dáta- ‘Fire-given or Fire-created’ and other names (Vd. 18.52; Justi, INB 50; Bthl. AiW 324). Agina пет. DB. 1.74, 82: 4.10; DBe 1f. Acinam asm. DB 1.76.
Ld
A ciyádiya- adj. ‘Aciyadiya’, the ninth month, .
Nov.-Dec.: Elam. haššiyatiyaš, АКК. kislimu, Cpd. of átar- ‘Are’ + deriv. of yad- ‘worship’ ($126; $152.D: ‘Fire-Worship Month’. Agiyddiyahya gsm. DB 1.89; 3.18.
ada- adv. ‘then’: GAv. ald, LAv. ада, Skt. .
ба ‘therefore’ cf. Gk. трбе-бє (and -Gev) ^n front of’: pIE *e-dhe, to root in *a- ($76.11; $191.II); see also adakaty. — ada-taiy DNa 48, 45.
adakaiy adv. ‘then’: OP ada- + -kazy, Gk. aly. то ‘somewhere’, pIE *q¥ei, Isn. to int.-indef. stem ($135). DB 2.11, 24; 4.81, 82; DNb 38.
adam pron. “Р: Av. azam, Skt. adm, plE .
*eühom ($109), ef. pIE *ейб in Gk. yo, Lt. ego (8193.1). adam nsm. AmH 5,8; AsH 14; CMa 1; DB 1.1, 10, 12, 39, 52, 54 bis, 56, 59, 60, 62, 63, 64, 66, 67, 68 bis, 70, 72, 73, 75, 18, 82, 83, 86, 89, 91, 95; 23, 5, 6, 10°, 11, 15°, 19, 28, 30, 48, 50, 68, 64, 69, 72, 80, 81, 88; 3.1, 13, 25, 29, 50, 77, 80, 84; 48, 8, 11°, 14, 16, 19, 21, 24, 27, 29, 32, 40, 45, 59, 64, 71, 81, 89; 5.2, 6f, 13, 21°, 23°, 25°; DBa 1, 16; DBb 4, 6; DBe 5; DBd 3, 6; DBe 5, 8; DBf 3f; рве 5; DBh 4f, 8; ОВ: 4, 9; ОВ] 4; DPd 20; DPe 1, 7; DPh 4; DNa 8, 17, 34, 37, 531; DSa 1, 4; DSb 1; DSe; DSd 1°; DSe 7f, 16°, 34, 44°; DSf 5, 18°, 21°; D8g 1, 3°; DSi 1; DSj 1°, 2°. DSk 1, 4; DSm 1°, 6°; DSy 1; DZe 4, 7, 8, 11;
LEXICON
DE 11; DH 3f; XPa 6, 13, 14; XPb 11; XPe 6; XPd 8, 17; XP£ 8, 34f, 36, 39, 41; XPg 9; XPh 6f, 15, 29, 34, 37, 40, 421, 43, 50; ХР] bis; XSe 1°, 3°, 4°, XE 12; XV 9, 23; A!Pa 9°, 21°; D'8b 1°, 4°; A'Sa 4; A’Sb; A'8d 1, 3; A?Ha 5°; A’He 9, 16; Азра 11f; Wa 2; Wb 1; We 2; Wd 2; SDa; SDb; SXb 1; SXe 1. adam-áaty DB 2.731. айат-йт (839) DB 1.62, 83; 4.6; DNa 35. adam-sam DB 1.14; DNa 18; DSe 17 adam-[$am]; XPh 16.
mam asm. (Av. mam, Skt. mdm, рЕ *me + acc. -m; 5193.11) AsH 7, 11; DB 1.52 (métya-mam, $133), 82f, 93°; 2.18, 28, 48, 63, 67, 73, 88; 3.30; 4.35, 91; 5.13, 17, 26, 28°, 29°, 33; DPh 9; DNa 33, 31,51; ОХЬ 11, 22, 26, 46, 49; DSe 50°; DSf 9, 10, 14f, 17 bis, 57; DSi 3°; DSj 4, 6°; Рб 4°; DSs 6; DSt 7°; DZe 12; DH 71; XPa 18; XPb 27; XPe 12; XPd 17; XPf 31, 45; XPg 12; XPh 57; X8e 4°. XV 25; A!Pa 22°; A’Sa 5^; A’Sd 4; A?Ha 6; A?Hb?; A?Hc 19; A?Pa 5, 23, 24; 224, 26 ({56.У; for mand ?).
-mā asm. епс]. (Av. md, Skt. md, pIE *mé, 6193.1; cf. enel. *me in Gk. pe): nai-mā ОМ 8 (na[ima]), 10, 19; nai-pati-ma ОМ 20.
mand gsm. (Av. mana, Skt. máma, pAr. *mana, cf. Lith. mano; $193.11T) AmH 6, 10; AsH 9; DB 1.4, 9, 12, 18, 18, 19 bis, 28, 27, 60; 2.19f, 21, 25, 27, 29f, 31, 35, 40, 46, 49, 51, 55, 601, 82, 84, 87, 91f, 93; 3.0f, 10, 13, 15, 17, 20, 20f, 31, 32, 38, 45, 53, 56, 62, 67, 75f, 76, 84, 86; 4.2, 12, 35, 42, 49, 52, 531, 66, 821; 5.8, 14°, 30; Ва 5, 14£; DPd 7, 13; DPe 9; DNa 19, 21, 33; DNb 56°; DSe 18°, 20°, 38; DSf 12, 13, 58; DS} 5°; DSk 4; DSs 6°; XPa 19; XPb 23; XPe 11; XPf 16, 23, 31, 46; XPg 7; XPh 17, 19; Ха 2; XV 18; A!Pa 20°; D'Sb 4^; A’He 18.  mana-eá (8135) DPd 9f.
-maiy gsm. (gen.-dat. GAv. mót, LAv. mé, Skt. me, Gk. dat. но, pIE *mot) enclitic to айа (ns
```


## [2026-09-06T15:29:23.741Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"aspacan\\|Aspačan\\|açanā\\|horse-lover\\|delighting in horses\" KNT.txt | head -20\necho \"--- canah\"\ngrep -n \"canah\\|Canah\\|cinah\" KNT.txt | head -20"
}
```


### [2026-09-06T15:29:23.802Z] TOOL RESULT

```
385:1 Note that Ciça- in this name has the OP form and not the Median *Cióra-. * ViMüspa, Aspacand, and Vidafarnd, despite the Median phonetics, are specifi- cally Persians; but personal names often belong to other dialects or languages than that of the locality to which the owner of the name belongs. Cf. also note 1.
1192:pIE *efuo- ‘horse’, OP asa- in aec. asam and in аѕађата-; OP aspa- (with Med. sp) in waspa-, Aspacanah-, Vistaspa-; Av. aspa-, Skt. бра, Lt. equos.
1941:b. Names of other Persians: Artavardiya-, Ardumants-, Aspacanah- (M), Ulana-, Өилта-, Dàtwahya-, Dédar&i-, Bagübigna-, BagaburSa-, Marduniya-, Vaumisa- (with -s- which is not Per- sian nor Median), Vayaspara-, Vahauka-, Vahyaz- dáta-, Vidafarnah- (M), Vidarna-, Vivina-, Hazà- manis-.
5120:aspa- sb. ‘horse’, Median for ОР asa- (890), q.v.; in Aspacanah-, uvaspa-, Vistüspa-.
5121:Aspacanah- sb. ‘Aspathines’, bow-bearer of Darius: Elam. a§-ba-za-na, Akk. as-pa-[si-nal, Gk. ‘Aoraftens; aspa- ‘horse’ (59.11, §9.n2, $90) + canah- ‘desire’, Av. -Cinah-, Skt. cénas-; ‘Lover of Horses’ (§161.[a, $168.10). Азрасапа пзш. (156.11, $185.11) DNd 1.
5378:canah- sb. ‘desire’, see Aspacanah-; cf. also kam-.
--- canah
1192:pIE *efuo- ‘horse’, OP asa- in aec. asam and in аѕађата-; OP aspa- (with Med. sp) in waspa-, Aspacanah-, Vistaspa-; Av. aspa-, Skt. бра, Lt. equos.
1860:rauc-ah-, zür-ah-, har-ah- in Hara'-uvali-; can-ah- - assuming masc. forms in cpd. personal name Aspa- 4 canah-; suffixal -[аз- in rau-tah-; suffixal -nas- in d far-nah- assuming masc. forms in ер. personal 1
1913:a. Accusative: Aspa-canah- ‘Having love of horses’; Baga-yadi- ‘(Month) marked by the wor- ship of the bagas’.
1941:b. Names of other Persians: Artavardiya-, Ardumants-, Aspacanah- (M), Ulana-, Өилта-, Dàtwahya-, Dédar&i-, Bagübigna-, BagaburSa-, Marduniya-, Vaumisa- (with -s- which is not Per- sian nor Median), Vayaspara-, Vahauka-, Vahyaz- dáta-, Vidafarnah- (M), Vidarna-, Vivina-, Hazà- manis-.
5120:aspa- sb. ‘horse’, Median for ОР asa- (890), q.v.; in Aspacanah-, uvaspa-, Vistüspa-.
5121:Aspacanah- sb. ‘Aspathines’, bow-bearer of Darius: Elam. a§-ba-za-na, Akk. as-pa-[si-nal, Gk. ‘Aoraftens; aspa- ‘horse’ (59.11, §9.n2, $90) + canah- ‘desire’, Av. -Cinah-, Skt. cénas-; ‘Lover of Horses’ (§161.[a, $168.10). Азрасапа пзш. (156.11, $185.11) DNd 1.
5248:kam- vb. ‘like’, see amazamata, if for (h)- amaxmatd. See also kama-, and possibly canah-.
5378:canah- sb. ‘desire’, see Aspacanah-; cf. also kam-.
```


## [2026-09-06T15:29:25.069Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT canah / cinah / cinman\"\ngrep -n \"canah\\|cinah\\|cinman\\|činman\" BRT.txt | head -20\necho \"=== BRT kama\"\ngrep -n \"^käma-\\|^kama-\\|kāma-\" BRT.txt | head -20"
}
```


### [2026-09-06T15:29:25.127Z] TOOL RESULT

```
=== BRT canah / cinah / cinman
5840:aspacanah-
10765:•  j.  xSadrö.cinah-  m.  EM.  eines  Gläubigen: 'nat?hs  * xSviwrSspanahe  (sd.)  afaons  YL 13.  iia.
22279:•  j.  *vakqrn.sav-" ''  Adj.  —  ?  — ,  vom bilinstigenKamelhengst:  u/jya^f . .  *vaZair- yaol  'sat>/'>  aiwi.tacinahe  Yt.  14.11  ■
24407:—  ahuräi  mazdai  . .  °pa  voAa  cinahmi Y.  72, 1 ;  9, 77. 1 7,  42. 3,  77. 6,7;  —  taurva- yeinlTm    'pa  (APn.)    riuaw  Y.52.  2;  a,  Yt.
28359:•  j.  iaetö.cinah-  Adj.  'Geld  heischend"'; j/ai  'nat»hs  jasqn  kam  iha  laüim  kam.- bärayin  "wenn  sie  Geld  heischend  kommen, soll  man  Geld  (für  sie)  zusanunenbringen" V.  4.  44;  44.
=== BRT kama
```


## [2026-09-06T15:29:34.116Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('KNT.txt',encoding='utf8',errors='replace').read()\nlines=txt.split('\\n')\nfor ln in (5121,5248,5378,5120):\n    off=sum(len(l)+1 for l in lines[:ln-1])\n    leaf=txt[:off].count('\\f')\n    print(ln,'leaf(0-based)=',leaf,'-> printed p ≈',leaf-15, 'or', leaf-13)\nEOF"
}
```


### [2026-09-06T15:29:36.339Z] TOOL RESULT

```
5121 leaf(0-based)= 195 -> printed p ≈ 180 or 182
5248 leaf(0-based)= 201 -> printed p ≈ 186 or 188
5378 leaf(0-based)= 206 -> printed p ≈ 191 or 193
5120 leaf(0-based)= 195 -> printed p ≈ 180 or 182
```


## [2026-09-06T15:29:36.554Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT kama Begehren/Wunsch\"\ngrep -n \"Wunsch, Begehr\\|kama-  m\\|käma-  m\\|kāma\\|kama- \" BRT.txt | head -20\necho \"=== BRT ka- verlangen\"\ngrep -n -E \"^•?\\s*\\*?k[aä]ma-\" BRT.txt | head -20"
}
```


### [2026-09-06T15:29:36.621Z] TOOL RESULT

```
=== BRT kama Begehren/Wunsch
5453:•  j.  aratö.kar^^na-  AdJ,  'wofür  die  Er- füllung der  religiösen  Pflicht  bezeichnend ist',  von  Hamaspa^maedaya  (sd.)":  ha- maspahmaSdaim  "tum  Vr.  2.  z; —  kama- spdimaldayeAe  'nahe  Vr.  1.2;  —  *'%nö F.7'>.
9493:•  j.,  g.,  p.  käma-  m.  'Verlangen,  Wunsch': haväi  °maua  zaosai'a\t.i^.2y,  —  aeiby:! p^r^na  äpansis  (sd.)  "m^m  Y.  2(V.  10;  — arii;ä  vsizdyäi  (sd.)  °mahy3  ^.43. 13.  a)  mit  Akk.  des  Verlangten": /^..-/y- xat  (sd.)  "///?..  dBtVm  ". .  im  Verlangen !  ^'^'''5,^ nach  der  Botschaft"  V.J.M3.  b)  mit'  "?  -' Akk.  des  Verlangenden^':  II  ya>3  mäm 'ina*  ä/ta*  "wie  es  mein  Verlangen  war" D.tf.4;Bh.4  4.
=== BRT ka- verlangen
```


## [2026-09-06T15:29:43.430Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('BRT.txt',encoding='utf8',errors='replace').read()\nlines=txt.split('\\n')\nfor ln in (9493,5840,28359,10765):\n    off=sum(len(l)+1 for l in lines[:ln-1])\n    leaf=txt[:off].count('\\f')\n    blk=txt.split('\\f')[leaf]\n    nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$', blk)\n    print(ln,'leaf',leaf,'colnums-on-leaf',nums[:8])\n    print('   ',lines[ln-1][:160])\nEOF"
}
```


### [2026-09-06T15:29:45.244Z] TOOL RESULT

```
9493 leaf 280 colnums-on-leaf []
    •  j.,  g.,  p.  käma-  m.  'Verlangen,  Wunsch': haväi  °maua  zaosai'a\t.i^.2y,  —  aeiby:! p^r^na  äpansis  (sd.)  "m^m  Y.  2(V.  10;  — arii;ä  vsizdyäi  (
5840 leaf 151 colnums-on-leaf ['217']
    aspacanah-
28359 leaf 927 colnums-on-leaf []
    •  j.  iaetö.cinah-  Adj.  'Geld  heischend"'; j/ai  'nat»hs  jasqn  kam  iha  laüim  kam.- bärayin  "wenn  sie  Geld  heischend  kommen, soll  man  Geld  (für 
10765 leaf 324 colnums-on-leaf ['547']
    •  j.  xSadrö.cinah-  m.  EM.  eines  Gläubigen: 'nat?hs  * xSviwrSspanahe  (sd.)  afaons  YL 13.  iia.
```


## [2026-09-06T15:29:45.396Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD kam\"\ngrep -n \"^kām\\|^kam \\|^kāmag\\|^kāmak\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB kam\"\ngrep -n \"^kām\\|^kāmak\\|^kamak\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T15:29:45.463Z] TOOL RESULT

```
=== PHD kam
PHD.txt:5058:kām
PHD.txt:5061:kāmaghanjām
PHD.txt:5316:kāmistanī gačēn gazdum
PHD_mackenzie.txt:9517:kam                           -G~     karg                   ~~
=== NYB kam
2171:kamak 1. will, wish, desire (= kam): 6 ~ rasét (imp.) may you attain, (the ful- filment of) your Royal Pleasure! 107; brihenisn u spahr u ~ i yazdān the predestination, Heaven, and the will of the gods 69°; pat ~ as teng as ever you wish 5915; ke Būšāsp ~ nē varzét he who does not (work the will of =) addict himself to Drowsiness 841%; ~ dátan 6 to direct one's will towards
2173:kamakčh
2175:kamakéh abstr. of bahuvrihi compounds with kāmak (v. above no 3): pat ménói m in the state of being a mönöi-kämak, one whose will is determined by Heaven, 4. e., in accomplishment of the will of the heavenly beings 40??, with the gl. cigön mēnēyān apäyist, v. apāytstan; purr--~ i o ahläyeh whole-hearted devotion to Righteousness 55? (purr-kämak whose will is full, perfect); @z-~ indulging in covetousness 681 (āz-kāmak addicted to Gz); andkeh-— il will, malignity 7215 (anākēh-kāmak, v. above no. 3); varan-~ kartan to indulge in lustfulness 8411; raväk- the state, or work, of one whose
2177:kamakčh
2191:kām-kār [k?mk?l] acting according to his own will, sovereign, autocrat: pat Hran- šahr ~ 1376; comp. ~-tar Supreme So- vereign 3°, adj. 418-19, — MPrth k’mg’r ‘free, happy’ (A-H III). V. kar.
```


## [2026-09-06T15:29:52.962Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5050,5070p' PHD.txt\necho \"--- leaf\"\npython3 - <<'EOF'\ntxt=open('PHD.txt',encoding='utf8',errors='replace').read()\nlines=txt.split('\\n')\nfor ln in (5058,):\n    off=sum(len(l)+1 for l in lines[:ln-1]); print('leaf',txt[:off].count('\\f'),'-> p',txt[:off].count('\\f')-21)\nEOF\necho \"=== NYB page\"\npython3 - <<'EOF'\ntxt=open('NYB_vol2_glossary.txt',encoding='utf8',errors='replace').read()\nlines=txt.split('\\n')\nfor ln in (2171,2191):\n    off=sum(len(l)+1 for l in lines[:ln-1]); print(ln,'leaf',txt[:off].count('\\f'),'-> p',txt[:off].count('\\f')-8)\nEOF"
}
```


## [2026-09-06T15:29:54.731Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD k'm\"\ngrep -n \"k'm\\b\\|k\\`m \" SOD_pages.txt | head -20\necho \"--- gloss wish/desire in SOD\"\ngrep -n -i \"wish, desire\\|desire, wish\" SOD_pages.txt | head -20"
}
```


### [2026-09-06T15:29:54.962Z] TOOL RESULT

```
4915 | keš- AD $915 kēšdār 1$ 195 kešīdan w^ 1835513 kišwān Wis kišwānzār 14519 kišw 1.32514 kišwar = leo AA kišwzār WE ме 1 4 kištan us- kédigih vs kid ~114 nag, -ak "ua oh!
PAIILAVI KEY
kimaghanjamih "age ” 425 kāmagxwadāy ^A pr 563 kāmgār > 56 8 1-2kāmag ($e 3 kāmagwidār ` 156 3 kāmrawāg 1 ө» e 4 kāmistan uerg s kastar `, Let 4 kástan 101635 4 kāč Q» 5 kābēn wars kāpūr N vays kādag Y4ve» 5 wast 25 A wasxwüstag 1341223920 эу "kay 24 drat “ys drodádwarih! >) мео 5 у kch SIE kahist 1825-65 4
gūspand' „rs
kēwān ers
kēnīg Deres “gen 13 – ken 13
l-3kar
kār- wing! *kār-ān kārāgāh kārāgāhīh kārdāg kārīgīh kārīg kārēzār kārawānīg kārawān kārnāmag kahrubāy kalbodómand kālbod kārframān kārd
kām
kūm-
ard! kūmistan kāmzīwišn kamagómand
kāmaghanjām
[115]
180
zardčūbug zam zamīg zamān zastan zafar zadar zadan zadüg
zaxm
kāh- kāhēn- kāhēnīdan kāhīdan kāhišn kāskēnēn kāskēn
kāskēnag
hammis!, hámist!
kahwan -ganag kayk kākom
-gār
--- leaf
leaf 231 -> p 210
=== NYB page
2171 leaf 123 -> p 115
2191 leaf 124 -> p 116
```


### [2026-09-06T15:29:56.828Z] TOOL RESULT

```
=== SOD k'm
9357:     quiet, peaceful                                                  1943 Nvrnyk'm S
10759:    2422 lyw mywn          M                                                       bynt1, bntq\ Pntk'm
10832:     allotment^)               tt                                Pamkam/Panka        ©lsg. fut. =»P-, Pw-, wPyk'm
10950:       MSP b24, 87                               t^                       2497 p'tk'm
11421:2662 pntk'm
11915:2858 btmyk C                                                        pwt(y), Pwy, Pw'n, Pwt>y, PwtkWn, bwq\PwS'k'm
11974:       C2, 102V24                                           2882 pwS'k'm
16914:                                                                                                                   k'm
16983:                                           jL-6-u I           4639 q'm CB, =»M, k'm*
16986:     k'm                                                                                                                 186
16997:     4641 k'm- B, M, S       (o^ ^j~j jj)^s^tj^l>c~*j>              4658 q'rpfitt) M                           J>jj<*b<^
17010:    4643 k'm'k S                         (<*Oj'>M
17016:    4644 k'm'ntk B                   ,kc
17022:    4645 k'm'nty -* k'm'ntk                                               GMS 932f; BSTBL, Dhu. 81, Dhy. 56 etc. p96
20192:                                                                            na-kam (L'k'm)
32376:9916 wp'mk'm
32377:     uPam-kam        ©lsg. fut. =*wp-, p'mk'm                      wipaste, upaste   (wPJstk) ^wP'stgy^
33114:          34, 103                                           10175 wrnyk}m =* 'wrnyk'm
33149:10170 wrn'yk'm B                                                  wirat, wrat ©*m-rata-         =»wrm, wrcy*
33289:10216 ws*t k'm M     {^jiif)c^^€iJJ^J^iohLr,y^
--- gloss wish/desire in SOD
3877:5 »p}stk B                      (tj*<jJL><4^^                wish, desire, lust
4055:   wish, desire                                              wish
4098:   wish, desire
28540:     (/o)desire, (/cOwish                                             desire, wish
28561:     wish, desire                                                       61R25
28678:         ryt% TSP 8.107                                             wish, desire, demand
28698:8665 ryth'nkm'ny      B => ryt'ngm'ny                               wish, desire
```


## [2026-09-06T15:30:01.532Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16975,17025p' SOD_pages.txt\necho \"=== leaf\"\npython3 - <<'EOF'\ntxt=open('SOD_pages.txt',encoding='utf8',errors='replace').read()\nlines=txt.split('\\n')\noff=sum(len(l)+1 for l in lines[:16985]); leaf=txt[:off].count('\\f'); print('leaf',leaf,'-> printed p ≈',leaf-66)\nEOF"
}
```


### [2026-09-06T15:30:03.474Z] TOOL RESULT

```
4624 -k M                                                          BSTBL, Dhy. 274
                                             ,1,^-1 1              palate
       (-q) ®kn <sk(n) <(})skwn           t?>                 4637 kJkh M                               t3-<f
       durative particle                                           kak ©<*kaka <*kahaka; (*kahman) =*k>Yk(h)
       GMS 635, 641
4625 -q    C -> -k                                                 Hen. Sogdica. p5.13 n p6
                                                                   palate
4626 -q> C
                                           jL-6-u I           4639 q'm CB, =»M, k'm*
                                                              4638 k'nV          S                        jU*juJ ^
       ka (-g>) =»k>ml, k>n
     k'm                                                                                                                 186

                                                                          GMS 1125
           kam ^k*n, -q*
           future particle
           GMS 646-50; EGSii p40                                    4655 q're -» -k'r'k
                                                                    4656 -k}rk =» -k>r>k
     4640 kW B                         f^<J-"jjjT                   4657 k'rpS S                                          dj
          kam (q'm) ©<OP kama ©ace. -w
          wish                                                            karpaS ©ob. -}y
           BSTBL, Dhy. 77; rttfm, C2, 60R 21 n p63                        Sund. MHC 36.8 R9 p26
     4641 k'm- B, M, S       (o^ ^j~j jj)^s^tj^l>c~*j>              4658 q'rpfitt) M                           J>jj<*b<^
          kam (q*m-)                                                     karpaS
          0o)want, (/o)wish, (to)like                                      path
                                                                         form
          GMS 96n 1, 775; BSTBL; SCE; MDii; Frag. Len.;                   Hen. Tales. 469.24, 470 n 1; S W, C2 n p5421
             TSP; VJ; STii, S W, C2 gloss. & n pl23, 28-9;
                                                                    4659 qVp8 C                                 ^Uii.lj<.lj
             trans, pret. <?WV-, GMS 457; STi 49.11; Sund.
                                                                         karpaG ©<*kara-pa6i ©pi. -/
             AoFviii 1981 p215; STii 121; C2, Jt>/n<5V-;
             Frag. Len. 69.17                                            way, path(army road)
                                                                         BSTii 917.10, 918.6; S W, 11V 25, 11R 21, 52V
    4642 q,m-       C, M => k>m-                                           10 p54.21
    4643 k'm'k S                         (<*Oj'>M
                                               '>>\ '-J^jjjT
         kamc, kamak                                 .              4660 k'rt'k B                              jjA^tJirt*.
           wisher                                                        karte ? (k'rtk) ©<Skt. gfhastha
                                                                         householder
         MDii, Nov. 4V7 p44.7; kWkw "at will" Frye 10                     BSTBL, Dhu. 206, Dhy. 6; GMS 363
    4644 k'm'ntk B                   ,kc

         kamande (k'nVnty)                                          4661 k'rtk -> k'rt'k
         well-wisher, liking                                        4662 kVy B, M, S              (j-l-*» L •J/^w)ju>w (^>)
         TSP 5.75; Frag. Len. 71, 8                                       ©post
                                                                          suffix position with inf.
    4645 k'm'nty -* k'm'ntk                                               GMS 932f; BSTBL, Dhu. 81, Dhy. 56 etc. p96
    4646 k'mS'r- S *=» k>m-
                                                                    4663 .-k'ry -» -k'r'k
    4647 q'md'r- C ■* k>m-
=== leaf
leaf 250 -> printed p ≈ 184
```


## [2026-09-06T15:30:13.323Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN cube\"\ngrep -n \"^cube,\" KLN_1966.txt | head\ngrep -n \"^Kaaba\\|^Caaba\\|^Ka'bah\\|Ka‘bah\" KLN_1966.txt | head\necho \"=== KLN whore\"\ngrep -n \"^whore,\" KLN_1966.txt | head"
}
```


### [2026-09-06T15:30:13.399Z] TOOL RESULT

```
=== KLN cube
9841:cube,  n.  —  F.,  fr.  L.  cubus,  fr.  Gk.  xufio?,  ‘cube, cubical  die’,  prob.  of  Sem.  origin.  Cp.  Arab. ka'b,  ‘cube’,  and  see  Kaaba.  The  u  in  Gk.  xiSpo? is  equivalent  to  Sem.  ayin  (represented  by  the sign  ‘).  See  W.  Muss-Arnolt  in  Transactions  of the  American  Philological  Association,  p.  147. Gk.  in  the  sense  ‘hollow  above  the  hip’,
20519:Kaaba,  n.,  the  cube-shaped  building  in  the  Great Mosque  of  Mecca  containing  the  Black  Stone of  Mecca.  —  Arab.  ka‘bah,  ‘square  house’,  fr. ka‘b,  ‘cube’.  Cp.  cube.
=== KLN whore
```


## [2026-09-06T15:30:13.901Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS kam\"\ngrep -n \"kām\\|kam \" SNS_pages.txt | head -20"
}
```


### [2026-09-06T15:30:13.952Z] TOOL RESULT

```
=== SNS kam
2332:                                                                                                                                                (lienning BSOS.           XI, :.£) r tauJ»*-<«*U kam           * «^* ******
8631:                 r/0^ .Jl!y»f*J^w4 :kam baved:                             v**"***      **
8633:  -T/IT^ f^W* '^^-- T ^ skam abistanih:
16127:                                                              K                         kam 215/10
```


## [2026-09-06T15:30:27.857Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nfor f,ln in [('KLN_1966.txt',9841),('KLN_1966.txt',20519)]:\n    txt=open(f,encoding='utf8',errors='replace').read(); lines=txt.split('\\n')\n    off=sum(len(l)+1 for l in lines[:ln-1]); leaf=txt[:off].count('\\f')\n    print(f,ln,'leaf',leaf,'-> printed p ≈',2*(leaf-12),'or',2*(leaf-12)+1)\nEOF\necho \"=== AHD cube / keu-b\"\ngrep -n -i \"CUBE\" AHD_watkins1985.txt | head\ngrep -n \"^keu-\" AHD_watkins1985.txt | head"
}
```


### [2026-09-06T15:30:29.713Z] TOOL RESULT

```
KLN_1966.txt 9841 leaf 210 -> printed p ≈ 396 or 397
KLN_1966.txt 20519 leaf 452 -> printed p ≈ 880 or 881
=== AHD cube / keu-b
623:(SCARCE). 3. Greek karpos, fruit: -cARP, CARPEL, CARPO-, -CARPOUS. [In Pok. 4. sker- 938.] kers-'. Dark, dirty. 1. Suffixed form *ker(s)-no- in Rus- sian chérnyi (feminine chérnaya), black: CHERNOZEM. 2. Suffixed zero-grade form *krs-no- in Sanskrit krsna-), black, dark: KrisHNa. [Pok. kers- 583.] kers-2. To run. Zero-grade form *krs-. 1. Latin currere (past participle cursus), to run: CORRIDOR, (CORSAIR), COURANTE, COURIER, COURSE, CURRENT, CURSIVE, CUR- SOR, CURULE; CONCOURSE, CONCUR, DECURRENT, DIS- COURSE, EXCURSION, HUSSAR, INCUR, INTERCOURSE, OCCUR, PERCURRENT, PRECURSOR, RECOURSE, RECUR, succor. 2. Suffixed form *krs-o- in Gaulish carros, a wagon, cart, in: a. Latin carrus, a two-wheeled wagon: CAR, CAREER, CARGO, CARICATURE, CARIOLE, CAROCHE, (CARRY), CHARGE, CHARIOT; b. Latin carpentum, a two- wheeled carriage: CARPENTER. [Pok. 2. fers- 583.] kert-. To turn, entwine. I. Zero-grade form *krt-. 1. Suf- fixed form *krt-i- in Germanic *hurdiz, wickerwork frame, hurdle, in: a. Old English hyrdel, hurdle, frame: HURDLE; b. Old French hourd, fence, hurdle, scaffold: HOARDING. 2. Suffixed form “*krt-sti- in Germanic *hur- sti- in Old High German hurst, thicket: Horst. II. Per- haps suffixed variant form *krot-i- in Latin crdatis, wickerwork hurdle: CRATE, GRATE?, (GRID), GRIDDLE; (GRIDIRON). [Pok. kert- 584.] kes-'. To scratch. 1. Germanic *hezd6 in Old English heordan, coarse parts of flax: HARDS. 2. Extended form *kseu- in Greek xuein, to scrape: XYSTER. 3. Nasalized form *ks-n-eu- in: a. Germanic *snaww- in Old Norse snéggr, “close-cropped,” perhaps akin to the source of snuG!: b. Latin novdcula, razor: NOVACULITE. [Pok. kes- 585.] kes-2. To cut. Variant kas-. 1. Suffixed form *kas-tro- in: a. Latin castrare, to castrate: CASTRATE; b. Latin cas- trum, fortified place, camp (perhaps “separated place”): CASTLE. 2. Suffixed form *kas-to- in Latin castus, chaste, pure (< “cut off from, free of, faults”): CASTE, CHASTE; CASTIGATE, INCEST. 3. Suffixed (stative) form *kas-é- in Latin carére, “to be cut off from,” lack: CARET. 4. Ex- tended geminated form *kasso- in Latin cassus, empty, void: (CASHIER), QUASH. [Pok. hes- 586.] kes-°. To order. Suffixed 0-grade form *kos-mo- in Greek kosmos, order: COSMOS; MACROCOSM, MICROCOSM. keu-' Also ekeu-. To perceive, see, hear. O-grade form *akou-. 1. Extended form *kous- in: a. Germanic *haus- Jan in (i) Old English hieran, to hear: HEAR (ii) Old English he(o)rcnian, to harken: HEARKEN; b. suffixed form *9-kous-yo- in Greek akouein, to hear: ACOUSTIC. 2. Variant *skou- in: a. Germanic *skauwon in (i) Old English scéawian, to look at: SHOW (ii) Flemish scauwen, to look at: SCAVENGER; b. Germanic *skaunjaz in Mid- dle Dutch schoon, beautiful, bright (< “conspicuous, attractive”): SCONE; Cc. Germanic *skauniz in Old Eng- lish sciene, bright, sheen: SHEEN. [Pok. 1. keu- 587.] keu-?. Base of various loosely related derivatives with assumed basic meaning “to bend,” whence “a round or hollow object.” I. Extended forms *keub-, *keup-. 1. Ger- manic *haup- in: a. Old English héap, heap: HEAP; b. Dutch hoop, heap, troop: FORLORN HOPE. 2. Germanic *hupp-, to leap (by first bending the legs), in Old English hoppian, to hop: HoP!. 3. Germanic *Aupiz in Old Eng- lish hype, hip: H1P!. 4. Zero-grade form *kup-, vessel, in: a. suffixed form *kup-s- in Greek kupselé, chest, hollow vessel: CYPSELA; b. long-vowel form *kip- in (i) Ger- manic *Aifi- in Old English hyf, hive: HIVE (ii) suffixed form *kip-a in Latin cupa, tub, vat: CUPOLA, CUPULE; c. expressive form *kupp- in Late Latin cuppa, drinking vessel: cup. 5. Zero-grade form *kub- in: a. Greek kubos, cube: CUBE; b. suffixed form *kub-@- in (i) Latin cubdre, to lie down on (< “to bend down, prostrate”): COUVADE, COVEY, CUBICLE; CONCUBINE, INCUBATE, SUCCUBUS (ii) Latin cubitum, elbow: CUBIT; Cc. nasalized form *ku-m-b- in (i) Latin -cumbere, to lie down, recline: ACCUMBENT,
1402:CUBE keu-2 CUBICLE keu-2 CUBIT keu-2 CUCKING STOOL kakka- CUD gWet-1 CUDGEL ku- CUESTA kost- CUIRASS sker-1 CUISINE pekw- CUISSE koksa CULET (s)keu- CULINARY pekw- CULLET kwel-1 CULLIS kagh- CULM! kolem- CULMINATE kel-6 CULOTTES (s)keu- CULT kWel-1 CULTIVATE kwel-1 CULTRATE skel-1 CULTURE kvel-1 CULVER kel-5 cum kom CUMMERBUND bhendh-, kamer- CUMULATE keue-2 CUMULUS keue-2 CUNCTATION konk- CUNNILINGUS leigh-, (s)keu- CUNNING gné- CUNT ku-
622:keu-?
```


## [2026-09-06T15:30:29.753Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full keu-b 589\"\ngrep -n \"Page(s): 588\\|Page(s): 589\\|Page(s): 588-589\\|Page(s): 589-590\" POK_full.txt | head\necho \"--- lemma keub\"\ngrep -n \"lemma: keu-b\\|lemma: keub\\|lemma: keu-\" POK_full.txt | head"
}
```


### [2026-09-06T15:30:29.821Z] TOOL RESULT

```
=== POK_full keu-b 589
47010:Page(s): 588-592 
--- lemma keub
46660:Root / lemma: keu-1, skeu-, lengthened grade keu- 
46749:Root / lemma: keu-2, keua-
```


## [2026-09-06T15:30:48.590Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### KLN leaf 210 numerals:\"; awk 'BEGIN{RS=\"\\f\"} NR==211' KLN_1966.txt | grep -oE '(?m)\\b[0-9]{3}\\b' | head -5\nawk 'BEGIN{RS=\"\\f\"} NR==211' KLN_1966.txt | head -3\necho \"### KLN leaf 452 head:\"; awk 'BEGIN{RS=\"\\f\"} NR==453' KLN_1966.txt | head -3\necho; echo \"### PHN leaf 162 (p131)\"; awk 'BEGIN{RS=\"\\f\"} NR==163' PHN.txt | head -40"
}
```


### [2026-09-06T15:30:50.146Z] TOOL RESULT

```
### KLN leaf 210 numerals:
554
380
147
ro,  n.,  the  monetary  unit  of  Brazil.  —  Port., fr.  cruz,  ‘cross’,  fr.  L.  crucem,  acc.  of  crux, ‘cross’.  See  crucial.
cry,  intr.  and  tr.  v.  —  OF.  (=  F.)  crier,  fr.  VL. *crltare,  corruption  of  L.  quiritare,  ‘to  cry,  wail, scream’,  denominated  fr.  Quirites,  ‘Roman  ci¬ tizens’;  see  Quirites.  Accordingly  quiritare  orig. meant  ‘to  address  the  Romans’,  whence  arose the  meanings  ‘to  implore  somebody’s  help;  to raise  a  plaintive  cry;  to  cry  aloud’.  Cp.  It.  gri- dare,  OProven?.,  OSp.  cridar,  Sp.,  Port,  gritar, which  all  derive  from  L.  quiritare.  Cp.  also decry,  descry.
Derivatives:  cry,  n.,  cry-ing,  adj.,  cry-ing-ly,  adv. cry-,  form  of  cryo-  before  a  vowel, crymodynia,  n.,  pain  caused  by  cold  weather ( med .)  —  Medical  L.,  lit.  ‘pain  caused  by  frost’, fr.  xpOfioc  (for  *xpuap.6p),  ‘frost’,  and  oSu-rt], ‘pain’.  Gk.  xpupuS;  is  cogn.  with  L.  crusta, ‘crust’;  see  crust,  n.,  and  cp.  the  second  element in  isocryme.  For  the  second  element  see  -odynia. crymotherapy,  n.,  the  therapeutic  application  of cold  (med.)  —  Compounded  of  Gk.  xpOpiop, ‘frost’,  and  SEpamria,  ‘a  waiting  on,  service,  at¬ tendance’.  See  prec.  word  and  -therapy, cryo-,  before  a  vowel  cry-,  combining  form  mean¬ ing  ‘cold,  freezing’.  —  Gk.  xpuo-,  xpu-,  fr.  xpuo? (for  *xpuaoc),  ‘icy  cold,  frost’,  which  is  cogn. with  L.  crusta,  ‘crust’.  See  crust, cryogen,  n.,  a  refrigerant.  —  Compounded  of cryo-  and  -gen.
### KLN leaf 452 head:
cer  of  the kings  of  England  from  the  reign  of  William  I to  that  of  Henry  III.  —  ML.  justitiarius,  ‘officer of  justice’,  fr.  L.  justitia.  See  justice  and  subst. suff.  -ary  (representing  L.  -arius). justiciary,  adj.,  pertaining  to  justice;  n.,  an  officer of  justice.  —  ML.  justitiarius,  ‘officer  of  justice’. See  prec.  word.
justifiable,  adj.  —  F.,  fr.  justifier,  ‘to  justify’.  See justify  and  -able.
Derivatives;  justifiabil-ity,  n . ,  justifiable-ness,  n., justifiabl-y,  adv.

### PHN leaf 162 (p131)
CUB 131
c'est un nerf de bœuf taillé de la même manière. — Le mot
turc, qui est tiré du hongrois, a passé dans la langue alle-
mande, oii il s'écrit karbatsche; c'est de là que nous avons pris
cravache, petit fouet d'une seule pi^ce, et servant particulière-
ment aux personnes qui montent à cheval.
CRAVATE, s. f.(A.)
AJU; [rainât j lien passé autour du cou (d'un homme ou d'un
animal), dérivé de ^j \rahaq\ entourer d'un lien. — Il existe
en arabe un mot très-rapproché de celui-ci, et qui ne peut
manquer de confirmer le sens de cravate; c'est iUi^ [ra^aftat],
qui veut dire cou. Au moyen de la transposition des deux pre-
mières radicales (ce qui produit qarabat)^ on obtient facile-
ment le terme français cravate, sur lequel les étymologistes
ne donnent rien de satisfaisant. -^ Les Portugais écrivent
cravata et gravata, les Espagnols corbata et corbatin, les Ita-
liens cravatta, et les Anglais cravat,
CRIBLE, s. m. (a.)
JlyiP [ghirbâl] tamis, crible, instrument de forme circulaire,
et percé de trous, pour nettoyer le blé, les graines, etc.; dé-
rivé de Jo^ [gharbal] cribler, passer au crible. — Le verbe
cribler se prend quelquefois au figuré, en français, dans le
sens de choisir, trier. — Comparez avec le substantif arabe le
latin cribrum et cribellum, l'italien crivello, l'espagnol criba, et
le portugais crivo.
CUBE, s. m. (a.)
\ka^b] di à jouer, cube, solide à six faces carrées égales;
9'
```


## [2026-09-06T15:31:00.599Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==211' KLN_1966.txt | grep -nE '^[0-9]{2,4}$|^ *[0-9]{2,4} *$' \necho \"--- context around cube line\"\nsed -n '9835,9850p' KLN_1966.txt\necho \"=== leaf 453 numerals\"\nawk 'BEGIN{RS=\"\\f\"} NR==453' KLN_1966.txt | grep -nE '^ *[0-9]{2,4} *$'\nsed -n '20510,20525p' KLN_1966.txt"
}
```


## [2026-09-06T15:31:01.757Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==163' PHN.txt | sed -n '38,60p'\necho \"=== PHN KAABA/CAABA\"\ngrep -n \"^CAABA\\|^KAABA\\|Kaaba\\|kaaba\" PHN.txt | head"
}
```


### [2026-09-06T15:31:02.635Z] TOOL RESULT

```
19:380
--- context around cube line
ctenoid,  adj.,  comblike.  —  Compounded  of cten-  and  Gk.  -0Ei8ir]i;,  ‘like’,  fr.  e!8o?,  ‘form, shape’.  See  -oid.
Ctenophora,  n.  pi.,  a  phylum  of  Coelenterata (zool.)  —  ModL.,  compounded  of  cteno-  and neut.  pi.  of  Gk.  -ipopop,  ‘bearer’,  fr.  ipepeiv,  ‘to bear’.  See  -phore.
cuarenta,  n.,  a  silver  coin  of  Cuba.  —  Sp.,  ‘forty’, fr.  L.  quadraginta.  See  quadragenarian  and  cp. quarantine.
cub,  n.,  the  young  of  the  fox,  bear,  wolf,  lion, tiger  etc.  — •  Of  uncertain  origin;  perhaps  rel. to  ON.  and  Icelandic  kobbi,  Norw.  kobbe,  ‘seal’.
which  is  prob.  so  called  from  its  heavy  and clumsy  form,  to  Norw.  kubbe,  kub,  ‘stump, block’,  and  to  E.  cob,  'heap,  lump’,  and  further  to Norw.  kop,  ‘cup’,  earlier  Dan.  kop,  ‘head’,  Dan. kop,  ‘cup’,  OHG.  chuph,  kopf  ‘cup’,  MHG.  kopf, ‘drinking  vessel;  head’,  G.  Kopf,  ‘head’.  See  cup. Derivatives:  cub,  tr.  and  intr.  v.,  to  bring  forth cubs,  cubb-ing,  n.,  cubb-ish,  adj.,  cubb-ish-ly, adv.,  cubb-ish-ness,  n.,  cub-hood,  n. cub,  n.,  a  stall,  shed.  —  MDu.  cubbe  (Du.  kub, kubbe),  ‘stall,  shed’,  rel.  to  cove  (q.v.)  See  also cubby.
cubage,  n.,  cubic  content.  —  See  cube  and  -age. cubature,  n.,  cubic  content.  —  F.,  irregularly formed  fr.  L.  cubus,  ‘cube’,  on  analogy  of  qua¬ drature.  See  cube  and  -ure. cubby,  n.,  a  small  space.  —  Derived  fr.  cub, ‘stall,  shed’.
cube,  n.  —  F.,  fr.  L.  cubus,  fr.  Gk.  xufio?,  ‘cube, cubical  die’,  prob.  of  Sem.  origin.  Cp.  Arab. ka'b,  ‘cube’,  and  see  Kaaba.  The  u  in  Gk.  xiSpo? is  equivalent  to  Sem.  ayin  (represented  by  the sign  ‘).  See  W.  Muss-Arnolt  in  Transactions  of the  American  Philological  Association,  p.  147. Gk.  in  the  sense  ‘hollow  above  the  hip’,
is  not  related  to  xu(3op,  ‘cube’.
Derivatives:  cube,  tr.  v.,  cub-er,  n.,  cubic  (q.v.) cubeb,  n.,  a  small  aromatic  berry  used  in  medi¬ cine.  —  F.  cubdbe,  fr.  ML.  cubeba,  fr.  VArab. kubdba,  corresponding  to  Arab.,  kababah,  of s.m.
cubelet,  n.,  a  little  cube.  —  A  double  dimin. formed  fr.  cube  with  the  suffixes  -el  and  -et. cubic,  adj.  —  F.  cubique,  fr.  L.  cubicus,  fr.  Gk. xup  1x64,  fr.  xfi(8o?,  ‘cube’.  See  cube  and  -ic. Derivatives:  cubic,  n.,  cubic-al,  adj.,  cubic-al-ly, cubic-ly,  advs.
cubicle,  n.,  1)  a  small  sleeping  room;  2)  any  small room.  —  L.  cubiculum,  ‘an  apartment  for  re¬ clining  or  resting’,  for  cubi-clom,  lit.  ‘a  place  for reclining',  formed  from  the  stem  of  cuhdre,  ‘to lie  down,  recline’,  with  -clom,  a  suff.  denoting place.  L.  cubare  derives  fr.  I.-E.  base  *qeu-b-, ‘to  bend,  curve,  arch’,  whence  also  L.  cubitum, ‘elbow’,  Gk.  xu(Bo;,  ‘hollow  above  the  hip  of cattle’  (but  xufloc;  in  the  sense  of  ‘cube,  die’, is  a  Semitic  loan  word),  Goth,  hups,  OE.  hype, ‘hip’.  See  hip  and  cp.  accumbent,  concubine,  cou- vade,  covey,  cubit,  incubate,  incubus,  incumbent, procumbent,  recumbent,  succubus,  succumb.  Cp. also  coomb,  ‘a  deep  valley’.  Base  *qeub-  is  a -^-enlargement  of  base  *qeu-,  ‘to  bend’,  curve, arch’,  whence  —  with  reduplication  —  L.  ca- cumen  (prob.  fr.  orig.  *kakud),  ‘top,  summit’. See  high  and  cp.  cacuminal.  For  a  -p-enlargement of  this  base  see  cup  and  cp.  words  there  re¬ ferred  to.
cubiculum,  n.,  a  cubicle.  —  L.  See  cubicle, cubiform,  adj.,  having  the  form  of  a  cube.  — Compounded  of  L.  cubus,  ‘cube’,  and  forma, ‘form,  shape’.  See  cube  and  form,  n. cubism,  n.,  a  school  of  modem  art  characterized
m
by  the  use  of  cubes  and  other  geometric  solids. —  F.  cubisme,  fr.  cube,  ‘cube’;  see  cube  and -ism.  The  word  cubisme  was  coined  by  the French  art  critic  Louis  Vauxcelles  on  the  basis of  a  remark  made  by  the  French  painter  Henri Matisse  (1869-1954)  before  a  landscape  ex¬ hibited  by  Georges  Braque  (1882-1963)  in  the Autumn  Salon  of  1908.  On  that  occasion  Ma¬ tisse  spoke  of  the  ‘small  cubes’  (petits  cubes) characterizing  the  painting  of  Braque.  This  re¬ mark  induced  Vauxcelles  to  form  the  word cubisme.
cubist,  n.,  an  adherent  of  cubism.  —  F.  cubiste, fr.  cube,  ‘cube’.  See  prec.  word  and  -ist. Derivative:  cubist,  adj.
cubit,  n.  —  L.  cubitum  (also  cubitus),  ‘elbow’,  fr. I.-E.  base  *qeu-b-,  ‘to  bend,  curve’,  whence  also cubare,  ‘to  lie  down'.  See  cubicle  and  cp.  cubitus. Cp.  also  codille.
=== leaf 453 numerals
11:838
join  and  cp.  next  word.  Cp.  also  jostle,  joust, adjust.
juxtapose,  tr.  v.,  to  place  side  by  side.  —  Formed fr.  juxta-  and  pose,  ‘to  place’.  i
juxtaposition,  n.  —  F.,  formed  fr.  juxta-  and position.
juzail,  n.  —  A  var.  of  jezail.  I
jynx,  n.,  i)  the  wryneck;  2)  a  charm  (from  the  use of  this  bird  in  witchcraft).  —  ModL.  jynx  (pi.  j
jynges),  fr.  L.  iynx,  fr.  Gk.  EuyE  (gen.  Eoyyo?),
‘the  wryneck’.  Some  philologists  derive  toy!;  fr- iut^eiv,  ‘to  shout,  yell’,  so  that  Euy5  would  lit. mean  ‘the  shouting  bird’  (see  jubilate).  Accord¬ ing  to  others,  toy?  is  a  word  of  foreign  origin, but  was  assimilated  in  form  to  (u£eiv.  See Frisk,  GEW.,  I  744  s.v.  tuyi Jynx,  n.,  a  genus  of  birds,  the  wryneck  ( ornithol. )
—  ModL.,  fr.  L.  iynx,  ‘the  wryneck’.  See  prec. word.
K
Kaaba,  n.,  the  cube-shaped  building  in  the  Great Mosque  of  Mecca  containing  the  Black  Stone of  Mecca.  —  Arab.  ka‘bah,  ‘square  house’,  fr. ka‘b,  ‘cube’.  Cp.  cube.
kaama,  n.,  a  hartebeest. — S.  African  native  name. Kabyle,  n.,  1)  a  Berber  of  Algeria  or  Tunisia; 2)  the  langauge  spoken  by  the  Kabyles.  —  F., fr.  Arab,  qabd'il,  pi.  of  qabtlah,  ‘tribe’,  rel.  to qibila,  ‘was  in  front  of’.  See  cabal  and  cp. kiblah.
kaddish,  n.,  doxology  of  the  Jewish  ritual.  —  Fr. Aram,  qaddtsh,  ‘holy’,  from  the  stem  of  qedhash, ‘was  holy’,  ithqaddash,  ‘was  sanctified’,  rel.  to Heb.  qddhdsh,  ‘was  holy’,  qadhdsh,  ‘holy’;  see Kedushshah.  The  kaddish  prob.  owes  its  name to  the  second  word  of  the  text  ( yeyithqaddash , ‘and  sanctified  be’).
Kaffir,  Kafir,  n. ,  1)  a  non-Mohammedan ;  2)  a  mem¬ ber  of  the  most  intelligent  group  of  S.  African Bantu  races.  —  Fr.  Arab,  kdfir,  ‘infidel’,  prop, part,  of  kafara,  ‘he  blotted  out,  covered,  hid ;  he denied’.  See  Yom  Kippur  and  cp.  cafard. Derivative:  Kaffir,  Kafir,  adj. kaftan,  n.  —  A  var.  of  caftan, kagu,  n.,  a  crested  bird  peculiar  to  Caledonia.  — Native  name.
kaid,  n.,  the  chief  of  a  tribe  in  N.  Africa.  —  Arab. qd'id,  ‘leader’,  part,  of  qdda,  ‘he  led  (the  army)’. Cp.  alcaide, kail,  n.  —  See  kale.
kaimakam,  n.,  lieutenant  colonel  of  the  Turkish army.  —  Turk,  qdimaqam,  ‘deputy’,  contraction of  Arab,  qd’im  maqdm,  ‘substitute,  proxy’,  lit. ‘standing  in  the  place  (of  another)’,  fr.  qd'im, participle  of  qdma,  ‘he  stood’,  and  maqdm, ‘place’  (also  from  the  base  of  qdma),  rel.  to  Heb. and  Aram,  qum,  ‘to  arise,  stand  up’,  Heb. maqdm,  ‘place’,  Ethiop.  qdma,  ‘he  stood’,  Ak¬ kad.  kummu,  ‘place,  dwelling’,  kum,  kemu,  ‘in place  of’,  and  prob.  also  to  Akkad,  kaiamanu, ‘constant,  enduring;  the  planet  Saturn’  (whence Heb.  kiyyiln,  Syr.  ke'wdn,  Arab,  and  Pers. kaiwdn,  the  planet  Saturn’), kainite,  n.,  a  compound  of  sulfates  of  potassium and  magnesium  (mineral.)  —  G.  Kainit,  coined by  C.  F.  Zincken  in  1865  fr.  Gk.  xaiv6?,  ‘new’, which  is  cogn.  with  L.  re-cen-s,  gen.  recentis, ‘fresh,  new’,  and  suff.  -it,  which  goes  back  to to  Gk.  -tngs.  See  recent  and  subst.  suff.  -ite. Kainozoic,  adj.  —  See  Cenozoic. kajrine,  n.,  an  alkaloid  made  from  quinoline (mineral.)  —  Prob.  fr.  Gk.  xatp6;,  ‘the  right season,  the  right  time’.  Cp.  eucairite.  For  the ending  see  chem.  suff.  -iue. kaiser,  n.,  an  emperor;  esp.  (cap.)  a  German  em¬ peror.  —  G.  Kaiser,  fr.  MHG.  keiser,  fr.  OHG. keisar,  fr.  L.  Caesar,  whence  also  OE.  casere.
OS.  kesur,  OFris.  keiser  (Goth,  kaisar  is  bor¬ rowed  fr.  Gk.  Katoap,  which  itself  is  a  loan word  fr.  L.  Caesar).  See  Caesar  and  cp.  czar, kaka,  n.,  any  of  certain  New  Zealand  parrots.  — Maori  kaka,  ‘parrot’,  imitative  of  its  cry. kakapo,  n.,  the  owl  parrot.  —  Maori.  Cp.  prec. word.
```


### [2026-09-06T15:31:04.140Z] TOOL RESULT

```
=== PHN KAABA/CAABA
2702:Kaabat qu'est enchâssée la fameuse pierre noire, à peu près
6888:au temple de la Kaabat, et qui doit se renouveler chaque
6957:dans la Kaabat, comme on Ta tant de fois répété. Plusieurs
7364:de Perceval, tome 1", p. 236, que, par respect pour la Kaabat,
10322:Caabat ou Kaabat, n. pr. (a.) 78
```


## [2026-09-06T15:31:12.140Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==163' PHN.txt | tail -25\necho \"==== next leaf\"\nawk 'BEGIN{RS=\"\\f\"} NR==164' PHN.txt | head -15"
}
```


### [2026-09-06T15:31:14.316Z] TOOL RESULT

```
mande, oii il s'écrit karbatsche; c'est de là que nous avons pris
cravache, petit fouet d'une seule pi^ce, et servant particulière-
ment aux personnes qui montent à cheval.
CRAVATE, s. f.(A.)
AJU; [rainât j lien passé autour du cou (d'un homme ou d'un
animal), dérivé de ^j \rahaq\ entourer d'un lien. — Il existe
en arabe un mot très-rapproché de celui-ci, et qui ne peut
manquer de confirmer le sens de cravate; c'est iUi^ [ra^aftat],
qui veut dire cou. Au moyen de la transposition des deux pre-
mières radicales (ce qui produit qarabat)^ on obtient facile-
ment le terme français cravate, sur lequel les étymologistes
ne donnent rien de satisfaisant. -^ Les Portugais écrivent
cravata et gravata, les Espagnols corbata et corbatin, les Ita-
liens cravatta, et les Anglais cravat,
CRIBLE, s. m. (a.)
JlyiP [ghirbâl] tamis, crible, instrument de forme circulaire,
et percé de trous, pour nettoyer le blé, les graines, etc.; dé-
rivé de Jo^ [gharbal] cribler, passer au crible. — Le verbe
cribler se prend quelquefois au figuré, en français, dans le
sens de choisir, trier. — Comparez avec le substantif arabe le
latin cribrum et cribellum, l'italien crivello, l'espagnol criba, et
le portugais crivo.
CUBE, s. m. (a.)
\ka^b] di à jouer, cube, solide à six faces carrées égales;
9'
==== next leaf
132 GUM
hexaèdre, terme d'architecture. — Remarquez l'analogie qui
existe entre le mot arabe et le grec xûêosy le latin cubus, et
l'italien ctibo, reproduit en espagnol et en portugais. — De
[A»^ft], augmenté de la terminaison féminine » i, vient
[X:a^ftat], nom du temple de la Mekke. Voyez Gaabat.
CUBÈBE,s. f. (a.)
liii\S^ \kéhâhai\ Nom d'une plante originaire des Indes orien-
tales. Les fruits qu'elle produit sont petits, secs, sphériques,
grisâtres, ridés, à peu près, de la grosseur du poivre, et em-
ployés dans certaines préparations pharmaceutiques. — Le
même mot s'écrit cuheba en espagnol; cubebas, cobebas et cobe-
beira en portugais; cubebe en italien, et ctAeb en anglais.
CULBUTER, V. a. (a.)
^^[kabb] renverser, d'où iUS'[kabbat] culbute. Peut-être con-
```


## [2026-09-06T15:31:25.769Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WEB cube\"; grep -n \"cubus\" WEB_vol1.txt | head -5\necho \"=== FSD cube\"; grep -n \"L\\. cubus\\|cubus, <\\|cubus,\" FSD_vol1.txt | head -5"
}
```


### [2026-09-06T15:31:25.887Z] TOOL RESULT

```
=== WEB cube
10463:Court of Arches; an English ecclesiastical court of appeal, the chief and most ancient consistory court, belonging to the archbish- opric of Canterbury: so called from the church in London, known as St. Mary le Bow (de arcubus), where it was 7 held. The jurisdiction of this court extends over the province of Canterbury.
46854:cii’ba-tire, n. [from L. cubus, a cube.) the de- termination of the cubic content of a body; also, the contents so found.
46860:cube n. [Fr. cube; L. cubus; Gr. kybos, a cube,
46904:cu-bo-, [L. cubus, Gr. kybos.] a combining form “FP meaning a cube, used to signify, (a) in mathe- matics, relating toa cube, and (b) in anatomy, of or pertaining to the cuboid bone in the foot. a cū”bō-dö”deç-å-hë’'drăl, a. [cubo-, and Gr. dö- dekaedron; dédeka, twelve, and hedra, a seat, base.] presenting the two forms, a cube and a dodecahedron. z z cū’boid, a. (Gr. kyboiedés.] é 1. shaped like a cube. oe 2. designating a cubelike bone between the m and the heel bone. ; cu’/boid, n. 1. a six-sided figure each face of which is a rectangle.
96677:etc. z i r t, n. incrustation. in-crust Ai lize-ble, a. that will not crystal- sen, hat cannot be formed into crystals; un- izable. 3 nF pace, v.t.; incubated, pt., DP. incubai ing, ppr- (L. incubatus, pp. of incubare, to lie m or upon; in, in, on, and cubare, to lie.] ; 1. to sit.on and hatch (eggs). > ; 2. to keep (eggs, embryos, bacteria, etc.) in a favorable environment for hatching or de- ing. igen pate, v.i. to go through the process of i ation. te aon, n. [L. incubatio (-onis), a lying upon eggs, 2 brooding, from incubare, to lie in or upon; i, in, on, and cubare, to lie, recline.] 1, an incubating or being incubated. : 2. the phase in the development of a dis- ease between the infection and the first ap- pearance of symptoms, in-ca-ba/tion-Al, a. of incubation. in/cu-ba-tive, a. of or characterized by incu- bation, ? ee in’cū-bā-tõr, 2. [LL. incubator, one who lies in a place, from L. incubare, to lie upon or in.Ja person or thing that incubates; specifically, (a) an artificially heated container for hatch- ing eggs; (b) a similar apparatus in which premature babies are kept for a period; (c) an apparatus for developing bacterial cultures. in-cii/ba-t6-ry, a. pertaining to the process of incubation or to the means of incubating; as, _ the incubatory pouch of an ascidian. in-cibe’, v.t. to establish securely, as if set in a cube. [Obs.] in-cii/bi-tiire, 2. incubation. [Obs.] in’ci-bous, a. [L. incubare, to lie upon.] in botany, having the leaves arranged so that the upper part of each covers the base of the one above. in/ci-bus, 2.; pl. in’/cii-bus-es or in’cū-bī, [LL., nightmare, a demon supposed to be the cauge of nightmare, from L. incubare, to lie upon; 7, in, upon, and cubare, to lie.] A a spirit or demon thought in medieval emes to lie on sleeping persons, especially men, with whom it sought sexual inter- Course: see also Succubus. 2. a nightmare. : anything oppressive; a burden.
=== FSD cube
60488:country  of  tho  incubus,  and  to  recover  thoso  cautionary  towns  and  Ca"va"IIcr'2,  1   kd'va'lyS';  2   f   a   *vii 'lye',  n.  1.  Jean  (,x/n fortresses.  Motlet  John  of  Barnevcld  vol.  i,  ch.  1,  p.  18.  [h.1  1681-Vit1740).  R   French  peasant;  leader  of  the  Camlsard
83757:Brewster  Netcton.  p.  122.  [h.  1839.1 8.  Eng.  A   paving-block.  [F.t  <   I».  cubus,  <   Gr.  kybos, cube.]  —   cube'*ore",  n.  Mineral.  Same  as  rirARMAcosin- erite. —   c.  root,  the  number  which  taken  three  times  as  a factor  produces  another  number,  which  Is  called  its  cube:  as, 3   Is  the  cube  root  of  27  —   c.*spar,.«.  Mineral .   Same  as anhydrite.—  four«faced  c.,  a   tetrahexahedron. cu'beb,  1   kiu'beb;  2   cu'bSb,  n.  Med.  A   berry  of  Piper cubeba,  which  is  dried  unripe  and  used  in  medicine, especially  in  urinary  and  bronchial  diseases:  often smoked  in  the  form  of  cigarets.  [   <   LL.  cubeba,  <   Ar.  ka- bdba.]  —   African  cubebs,  the  berries  of  Piper  guineense found  in  western  Africa,  or  the  plant which  bears  them.  West-Afrlcan black  peppers*.— cu'bcb*oH",  n.
```


## [2026-09-06T15:31:34.452Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '46860,46866p' WEB_vol1.txt\necho \"=== page marker near\"\npython3 - <<'EOF'\ntxt=open('WEB_vol1.txt',encoding='utf8',errors='replace').read(); lines=txt.split('\\n')\noff=sum(len(l)+1 for l in lines[:46859]); print('leaf',txt[:off].count('\\f'))\nEOF"
}
```


## [2026-09-06T15:31:34.545Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ntimeout 600 python3 tools/ref_page.py BQT:1578 --image 2>&1 | tail -40"
}
```


### [2026-09-06T15:31:36.168Z] TOOL RESULT

```
cube n. [Fr. cube; L. cubus; Gr. kybos, a cube,
ie. 1. in geometry, a regular solid with six equal square sides. 2. in arithmetic, the third power; the product obtained by multiply- ing a given number or quantity by its square; as, 4 X 4 = 16, and CUBE 16 X 4 = 64, the cube of 4, (4 X 4 X 4). cube root; the number or quantity of which a given number or quantity is the cube: as, the cube root of 8 is 2.
cube, v.t.; cubed, $t., pp.; cubing, ppr. 1. to raise to the third power by multiplying (a number) by itself twice.
2. to form or cut into the shape of a cube or cubes; as, cube the vegetables. 3. to measure the cubic content of. opens n. (Sp. cubeba; Ar. kababa; Hind. kaba- a
1. the small, spicy berry of the Piper cubeba, from Java and other East Indian islands, used in diseases of the urinary system, and sometimes made into cigarettes, smoked for catarrh or bronchial disease.
2. such a cigarette.
cu bebiic: a. relating to or obtained from cu- ebs. cūbe ọre, a mineral, pharmacosiderite. cube spar, a mineral, anhydrite. cub/hood, x. the condition of being a cub. cubic, a. [L. cubicus; Gr. kybikos, from kybos, a cube.]
=== page marker near
leaf 472
```


### [2026-09-06T15:31:43.877Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1578.png
REF: BQT:1578  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 371  OCR-lang: fas

کالیو ۱۵۷۸
و چیزیرا که کرد وخاد برآن اشتته باشد هم کا۵ - بسکون میم » سقف دهانرگوبند
کالیده میگوبند . پمنی فك اعلی و بعربی حنك خوانند -ودهاتر1
کالیو ۱ - با اك بتحتانی کشیدمویواو | نیز کفته‌اند ۸ - وبمعلی مراد و مقصد هم آمده
زده » بممنی نادان وابله - وسرگشته وگیج(۱) | است ‎٩‏ .
حیران ۴ - و سراسیمه و پیهوش ؟ - و دیوانه کامته ۱۶ بفتح‌تای‌قرشت ءنام‌شپرست
مزاج باشد - وکر را نی زکویند یمای کس ی که از ولابت کوچ و آن مابین بنگاله و ختا واقع
کوشش نشنود و بعربی اضم خوانند ۴ . است ودرآن شهر ساحران وجادوکوان بسیارند.
کالیوس ۴ * بروزن آبنوی » بمعلی کام خاریدن «کنایه از میل کردن
کالجوش است وآن‌نان ریزه کرده باش دکه‌باکشك | واراده نمودن بچیزی باشد.
وروغن ومغز کردکان‌وادوبةٌ کوم جوشانیده‌خورندء گاهرو ۱۱ بارای بی‌نقطه بوا و کشيده,
وآفرا درخراسان اشکنهٌ قروت ی کوبند. نام شهری است مايین بنگاله و ختا ودرآن شهر
کالیوه * » بفتح واو. بسمنی کالیواست نیز مانند کامته ساحران و جادوگران ببارند
که نادان واحمق- وس رگشته ‎٩‏ ودیوانه‌مزاج ۹ وکوند رای وپادشاه | نجا نیز ساحراست .
- وکرباشد یمنی کوشش شنود ۷ . کام‌فیر ود - نم ولابتی است از
69 چش : -گیج ۰
۱ - کالیوه («.م.) ۰ از « کف گاه گاه آ مد از وقت نیز بر گذشت سراسیمه
و کالیو وخجل و بی قرار » روی بوبرانه ای نهاد .> ( عطار بیشابوری . نذ کرةالاولیاء چاپ آروپا
2 ۹ص ۷۰ ۳ کلیاوه (و.م.) 5 کالیوه («.م.) سعدی مجازاً باین هعنی آورده :
تب مکنان کفت‌کای تیزهوش! اسم به که گفتار باطل نیوش
چو کالیو دانندم اهل نت بگویند نيك وبدم هرچه‌هست.
« فرهنگه نظام > .
۳ - در رشندی و فرهنگه نظام «کالیوش» | هده وهمان اصح است.
۰ - قس : لری بیرانوندی 11۷8 ( دیوانه ) « شپیدی > ۰
‎٩‏ - نالهٌ بلبل سحرکاهان و باد مشکبوی مردم سرمت را کالیوه و شیداکند .
۰ « منوچهری دامغانی ص ۲۳ * .
۷ * کالیو («.م.) > کلیاوه (هم.). زرا رد : لغخت فرس‌صس ۰.۳4۷
‎٩‏ - اوستا و پارسی باستان - 15228 ( میل » آرزو ) « بارتولمه 4۹۳ » سانسکریت
س . 5 دیب رکه ۰۶۱۱۸ ارمنی ع 1۴- ۴8732 (آرزو » میل )ء 1823100 (خواستن,
آرز و کردن » استی 80173 (آرزو) اسشق ۸۳۸ > و رك : هوبشمان ۸۳۸ -
آنجاکه هت‌کامش, با کام اوست‌دولت و آ نج ا که هت رایش, با رای اوست گردون.
معزی نبشایوری 9۳۸ *.
۹۰ رك : کامرو ۰ ۹ - چنین نامی در معجم‌البلدان ونخبة‌الدهر و حدودالعالم‌و
غدره دیده تشدموظاهر أمسحف «کامر د» 4 _۵ عااست که موضمی‌است درحوالی بلخ«مینورسکی.
حدود ص ۲ 6۳۶ ورك : کمرد. در معجم البلدان کامة نیز ظ. مصحف همین کلمه‌است. ورله: کامته.
(برهان قاطع ۲۰۲)
```


## [2026-09-06T15:32:05.804Z] TOOL CALL #35: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1578.png"
}
```


### [2026-09-06T15:32:06.509Z] TOOL RESULT

```

```


## [2026-09-06T15:32:06.506Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-06T15:32:44.166Z] TOOL CALL #36: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT\ncat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1578.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed page ۱۵۷۸ (= BQT:1578; BQT_v3 pdf page 371) — read from the page image]\n\nRunning head: کالیو\n\nColumn entries (right→left):\n… کالیو ۱ ، کالیوس ۴ ، کالیوه ۵ …\nکام ـ بسکون میم ، سقف دهان را گویند یعنی فک اعلی و بعربی حنک خوانند ـ و دهان را\nنیز گفته‌اند ۸ ـ و بمعنی مراد و مقصد هم آمده است ۹ .\nکامته ۱۰ ـ بفتح تای قرشت ، نام شهری‌ست از ولایت کوچ و آن مابین بنگاله و ختا واقع است …\nکام خاریدن ـ کنایه از میل کردن و اراده نمودن بچیزی باشد.\nکامرو ۱۱ ـ بارای بی‌نقطه بواو کشیده ، نام شهری است مابین بنگاله و ختا …\nکام‌فیروز ـ نام ولایتی است از …\n\nMo'in's footnotes at the foot of the page:\n۸ ـ رک : لغت فرس ص ۳۴۷ .\n۹ ـ اوستا و پارسی باستان ـ kâma (میل ، آرزو) « بارتولمه ۴۶۳ » ، سانسکریت kâm ، kâmak\n« نیبرگ ۱۱۸ » ، ارمنی kam-k (آرزو ، میل) ، kamim (خواستن ، آرزو کردن) ، استی kom (آرزو)\n« استق ۸۳۸ » و رک : هوبشمان ۸۳۸ .\n   [شاهد:] آنجا که هست کامش ، با کام اوست دولت / و آنجا که هست رایش ، با رای اوست گردون.\n   « معزی نیشابوری ص ۵۳۸ » .\n۱۰ ـ رک : کامرو .\n۱۱ ـ چنین نامی در معجم‌البلدان و نخبة‌الدهر و حدودالعالم و غیره دیده نشد و ظاهراً مصحف\n«کامرد» kâ-mard است که موضعی است در حوالی بلخ «مینورسکی ، حدود ص ۳۴۶» و رک: کمرد …\n(برهان قاطع ۲۰۲)\n\n[Used for: page 231, root \"Kâ 1, Qâ\", nodes #3 (Pahlavi kâm) and #4 (Persian کام ۱).\n The footnote confirms Av./OP kâma- 'desire, wish' (Bartholomae col. 463) and the\n Pahlavi/Nyberg forms kâm, kâmak (Nyberg p.118); it does NOT mention the\n compounds کامیاب / کامکار on this page.]\nEOF\necho saved"
}
```


### [2026-09-06T15:32:44.226Z] TOOL RESULT

```
saved
```


## [2026-09-06T15:32:47.268Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN kam\"; grep -n -E \"k[aâā]m\" HRN.txt | grep -i \"wunsch\\|begier\\|verlangen\\|kām\\|kâm\" | head -10\necho \"=== HRN numbered\"; grep -n \"^ *[0-9]*\\. *kām\\|kām 'W\\|kâm\" HRN.txt | head -10\necho \"=== HUB kam\"; grep -n \"kām\\|kâm\" HUB.txt | head -15\necho \"=== CHEUNG kam\"; grep -n \"kāma\\|^\\*kam\\|kam- \" CHEUNG.txt | head -15"
}
```


### [2026-09-06T15:32:47.353Z] TOOL RESULT

```
=== HRN kam
7281:ap. aw. kama- 'Wunsch, Wille*; phlv. kamak,
7283:vielleicht arm. LW. kam-k 'Wille, Wunsch*, kamim
=== HRN numbered
=== HUB kam
=== CHEUNG kam
15377:*kamp ‘to bend’ 
15455:surround; to apply’, ? LKh. parkam- (parküfi-) ‘to sprinkle, scatter’ || (+ *ui-) OKh. 
37189:parkam- (parküü-), 230
```


## [2026-09-06T15:32:50.764Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7272,7295p' HRN.txt\npython3 - <<'EOF'\ntxt=open('HRN.txt',encoding='utf8',errors='replace').read(); lines=txt.split('\\n')\noff=sum(len(l)+1 for l in lines[:7280]); leaf=txt[:off].count('\\f'); print('leaf',leaf,'-> printed p',leaf-21)\nEOF"
}
```


### [2026-09-06T15:32:53.686Z] TOOL RESULT

```
ziehen, pflügen' zu 'säen*.
837. kaften ^spalten; graben*, kawlden^ käflden^ keffen,
keflden.
Nüldeke vergleicht gr. vA-ntzoc 'Graben*. Vergl.
unter slkäften (No. 787).
kurd. LW. vekavum 'ich wahrsage*, vek^ft (aus np.
wcl käwlden 'nachforschen') Justi No. 37; sar. käti-am
'gi'aben*.
l 838. krim 'Wunsch, Wille*, käme.
ap. aw. kama- 'Wunsch, Wille*; phlv. kamak,
kämakth , kämitan (y. 4 (12) Gl.), käm(i)stan (Men.),
vielleicht arm. LW. kam-k 'Wille, Wunsch*, kamim
'wollen, wünschen* (Hübschniann, No. 140); ai. iama-,
oss. kom 'Wille* (161).
Ob np. kam 'Gaumen* (af/. kumai) dasselbe Wort ist,
ist unsicher '). Der Vokal würde zu mhd. goume,
ags. görnUy got. ^gömö (dann nicht *gatimö) 'Gaumen*
stimmen, das zweifelnd zu gr. xuvvog 'klaffend*, /dog
(*xdfng) 'Kluft* gestellt wird; aber k und g passen
nicht zusammen. Da von einer np. Aussprache gütn
nichts bekannt ist, so durfte West, Pahl. Texts,
Part. II, 439 nicht ein phlv. gämak 'Gaumen' con-
struiren.
f 839. kän 'Mine'.
leaf 207 -> printed p 186
```


## [2026-09-06T15:33:03.641Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"838\" HUB.txt | head -20"
}
```


### [2026-09-06T15:33:03.687Z] TOOL RESULT

```
853:Nr. 838.
3052:838. Np. kdm = afgh. kumai *Gaumen' ist schwerlich
```


## [2026-09-06T15:33:07.094Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3048,3062p' HUB.txt; sed -n '848,860p' HUB.txt\npython3 - <<'EOF'\ntxt=open('HUB.txt',encoding='utf8',errors='replace').read(); lines=txt.split('\\n')\nfor ln in (3052,853):\n    off=sum(len(l)+1 for l in lines[:ln-1]); leaf=txt[:off].count('\\f'); print(ln,'leaf',leaf,'-> p',leaf-10)\nEOF"
}
```


### [2026-09-06T15:33:10.206Z] TOOL RESULT

```
spalten' ist das Causativum von kaftan 'gespalten
werden (Fird. I, 468, Z. 4), dessen Praesens nach
Vullers kafam (arisch kaph) lautet. Vgl. ia/'fissura,
ruptura'.
838. Np. kdm = afgh. kumai *Gaumen' ist schwerlich
identisch mit kam 'Wunsch, Wille'. Die germ.W5rter
fiir *Gaumen' setzen im Anlaut ein idg. gh, die irani-
schen ein idg. k voraus.
840. Dazu nach Geiger hsA, kdh 'frisches griines Gras,
das, wenn es nicht entlehnt ist, auf iran. *kah€h =
*) Besser: hari = idg. kor9 zweisilbig.— 87 —
skr. ^JfOsa^ zuriickgeht. Den Lauten nach kann das
Wort sowohl Lehnwort wie Originalwort sein.
842. Vgl. modern asp i kdtbud *Grausehimmer, Kosen,
Np. Sprachftihrer p. 38.
soli skr. vrjana- *Fangnetz, Falle, Anschlag, List, Hinter-
halt, Versteck' etc. (Pischel-Geldner, Ved. Stud. I,
143 flg.) bedeuten. Jedenfalls bleibt die Etymologic
von barzan noch vollkommen dunkel.
200. Dazu syr. LW. NDD^ID, Hoffmann, Auszuge p. 94,
Nr. 838.
201. Das in der Anmerkung vermuthete biristan *braten' ist
baristan 'zum Spinnen', wie Salemann zuerst bemerkt
hat. Die iranischen Verwandten') von biristan gehen
*) Dazu noch jud. tat. hurzire intrans., burzunde trans. (Miller
p. 59).— 27 -
auf eine iranische Wurzel brif (bal. brijfag, brSjfag
'rosten, backen', np. phi. bar^jan 'Backofen, 61. and
3052 leaf 96 -> p 86
853 leaf 36 -> p 26
```


## [2026-09-06T15:33:21.411Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS kam/kām\"; grep -n -i \"wish\\|desire\\|will,\" SNS_pages.txt | head -20\necho \"--- SNS leaves\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' SNS_pages.txt"
}
```


### [2026-09-06T15:33:23.193Z] TOOL RESULT

```
=== SNS kam/kām
--- SNS leaves
242
```


## [2026-09-06T15:33:23.412Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT ka'b\"; grep -n -i \"ka'b\\|ka‘b\\|kaaba\\|Kaʿba\\|Ka'ba\" LKT.txt | head\necho \"=== FVQ ka'b\"; grep -n -i \"ka'b\\|Ka‘ba\\|kaʿb\" FVQ_pages.txt | head\necho \"=== DEV cube\"; grep -n \"^CUBE\\|kaab\\|ka'b\" DEV.txt | head"
}
```


### [2026-09-06T15:33:23.486Z] TOOL RESULT

```
=== LKT ka'b
=== FVQ ka'b
513:of information supplied by Jewish converts such as Ka'b b. Mat!" 5
526:5 Usually called Ka'b al-Alibar. See an-XawawI, 523 ; Tbn Hajar, iii, 633-639 ;
1421:as >ve learn from al-Mas'iidi, Alvruj, iv, 46, was tho chief god of the Ka'ba.
1474:men having been employed in the rebuilding of the Ka'ba.INTRODUCTION 29
2138:quote as an example of its use Ka'b al-Ahbar, 4 the well-known convert
2150:of 0110 whoso full namo was Ka'b b. al-Ashraf Sayyid al-Afcbar.50 FOREIGN VOCABULARY OP THE QUR*AN
3985:says that when Ka'b was asked about it lie said that Ax>- in Syriac
7657:It occurs only in a Madinan Sura in a reference to the Ka'ba
=== DEV cube
```


## [2026-09-06T15:33:29.416Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS کام\"; grep -c \"کام\" SNS_pages.txt; grep -n \"کام\" SNS_pages.txt | head -10\necho; echo \"=== SNS leaf ~209\"; awk 'BEGIN{RS=\"\\f\"} NR==210' SNS_pages.txt | head -20"
}
```


### [2026-09-06T15:33:31.220Z] TOOL RESULT

```
=== SNS کام
0

=== SNS leaf ~209
                          Ujc~-li»-U *A
65

hvara- 69/7
hvarjsta-/hvarsta- 76/6
hv-apah 61/18




                                                              ob-L^-j U^U 'j'j    .**




                                          aiva- 90/12                    asa- 192/1
                                          ajanara 163/5                  ahura-mazdah
                                          ajamiya 243/3
                                          atar/aer 27/18                 1
```


## [2026-09-06T15:33:31.417Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON کام\"; grep -n \"کام ۱\\|(کام)\\|کام‌یاب\\|کامیاب\\|کامکار\\|کامگار\" MON_part1.txt MON_part2.txt | head -15\necho \"=== MON کعب\"; grep -n \"کعبه\\|مکعب\" MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-06T15:33:31.494Z] TOOL RESULT

```
=== MON کام
MON_part1.txt:22873:شاداب. کامیاب» برخوردار. صاحب نفع» 
MON_part1.txt:26460:می‌برد. بهره‌مند. شر بکث» سهیم. کامیاب. 
MON_part1.txt:34507:خرم؛ کامیاب. بهر ۵مند» متمتع. 
MON_part1.txt:34516:فیروزمند. به مراد رسیده؛ کامیاب. 
MON_part1.txt:34530:(حامص.) ظفر؛ فتح؛ غلبه. کامیابی؛ روایبی 
MON_part1.txt:53657:خوشی کامیابی؛ کامرانی. (!.) بهره؛ نصیب. 
MON_part1.txt:53670:بهر ۵» متمتع. کامیاب» خوشخت. 
MON_part1.txt:63143:(کد.) کامیاب شدن مستولی شدن. غضبنا ک 
MON_part1.txt:77006:صاحب دولت» کامکار. 
MON_part1.txt:83696:گلاب و سازگار و کامگار. ب -قافیه آوردن 
MON_part2.txt:5420:کشور اختصاص دارد و موجب کامیابی و 
MON_part2.txt:19487:کامکار: 2-۴ [- کامگار] (ص‌فا) 
MON_part2.txt:19561:کامیاب: بٍِ (ص‌مر.) کامروا؛ 
MON_part2.txt:19610:کامیاب 
MON_part2.txt:30599:انبان فرو شدن: ( کد.) کامیابی کامل بافتن او. 
=== MON کعب
MON_part1.txt:7912:را در هنگام زیارت کعبه و مراسم حیج بر 
MON_part1.txt:11249:پرده‌ها. استار کعبه: پرده‌های کعه. هتکك 
MON_part1.txt:12174:در آن روز درهای آسمان یا درهای کعبه باز 
MON_part1.txt:17937:اطراف کعبه نصب کرده بودند و در بای 
MON_part1.txt:34027:حلبی مکعب مستطیل شکل برای حفظ و 
MON_part1.txt:34447:جامةٌ انوس جلد فانوس. پیراهن کعبه: 
MON_part1.txt:34448:پارچه‌ای که بر کعبه گیرند» جامة کعبه. 
MON_part1.txt:45988:۰ ۰ سانه نتیمتر مکعب؛ هییو سولفیت دوسود 
MON_part1.txt:45990:سانتیمتر مکعب» زاج معمولی ۲ گرم. 
MON_part1.txt:52444:قصد کر دن. (شر ع.) قصد طواف کعبه کر دن
```


## [2026-09-06T15:33:39.254Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '19480,19500p' MON_part2.txt; echo ---; sed -n '19555,19570p' MON_part2.txt\necho \"=== MON کام headword\"; grep -n \"^کام\\b\\|^کام:\" MON_part2.txt | head\necho \"=== MON کعب headword\"; grep -n \"^کعب\\|کعب:\" MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-06T15:33:39.357Z] TOOL RESULT

```
معامله ده درآوردن. 

کام‌طبع: ۲ اف. ع.] (ص‌مر.) 
حریصء طماع» آزور. 

کامفر: 2 (.) کافور. ضح.- احتراز از 
استعمال این کلم بیگانه اولی است. 
کامکار: 2-۴ [- کامگار] (ص‌فا) 
کممرواء کامران. سعید؛ سععاد تمنده 
خوشبخت. موفق» عشرت‌طلب» عیاش. (.) 
جانور شکاری (سباع و طیور). (ص.) 
مطبوع ذایقه. 

کامل: 2۵ [ع.] (افا. ص.) آنچه به کمال 
رسیده» تمام) م. ناقص. بی‌عیب» بی‌نقص. 
بر » ممتل: آنکه به کمال معرفت رسد ۵ 
فاضل. دانا؛ ج. کاملین. مسن» به زاد بر آمده. 
(.) (عر.) بحری است که ارکان آن از تکرار 
«مستفاعلن» بدست 3۳ و از حور متفق 
الارکان است. جملهٌ کامل: (دس.) آن است 
که معنی آن کامل تمام باشد و به جملة دیگر 
---
شبر و ادویهٌ حاره سازند. 


فررهنک فارسی معین 


کامیاب: بٍِ (ص‌مر.) کامروا؛ 
تم و مقتضی المرام؛ مق. نا کام. 
موفقء فیروزمند. 

کامیار: :۲.2 [کام» قس. بختیار| (ص‌مر.) 
دنت کم3 موفق» فر وزمند. (اخ ( اسم 
اشخاص قرار گیرد. 

کامیون: 0 (ا.) اتومسل بر رگ برای 
حمل و نقل بار؛ اتومبیل باری. 
=== MON کام headword
545:کامل شدن. ابتداء آغاز ظهور. نتیجه, اشر. 
2077:کامل: بخشایش همه گناهان. 
4843:کامل داشته باشد؛ ملک بزرکگک» عمده 
8117:کامی موسوم است و در تشکیل سقف دهان ‏ 
8561:کاملی به گیاه تلو ل داوی هتخس ان را 
13509:کاملی است؛ ج. قطعات. ضح. قطعه که 
13967:کاملاً 0 
15528:کاملاً آبسزی است. زیرا دارای برانشی 
15532:کاملا" هوازی است و برای تنفس باید به 
16213:کامل: (منط.) آن بود که به نفس خودبین 
=== MON کعب headword
MON_part2.txt:16991:کعب. زید ین ابت. عبدالله بن سعد. معاو به. 
MON_part2.txt:23783:کعب: 9 [ع.] (.) هر بند استحوان؛ 
MON_part2.txt:23803:کعبتین: راومه ها [ع. ۰] (.) تئنبة 
MON_part2.txt:23819:کعبه: (۳۵)۵ 2 [ع. کعبة | (.) جای چهار 
MON_part2.txt:45821:مساوی یک متر باشد. متر مکعب: واحد 
MON_part2.txt:63907:مکعب: ِ ۵ [ع. ۰] (امف.) چهار کو شه 
MON_part1.txt:36865:کعبتین. ظرفی است که در آن آب و مابعات 
MON_part1.txt:83289:کعبه. شاه مشرق: (کد.) خورشید. شاه
```


## [2026-09-06T15:33:39.524Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\ngrep -n \"کام\" ARY_pages.txt | head -20\necho \"=== latin index\"; grep -n -i \"^KAM\\|KAM \" ARY_latin_index_pages.txt | head"
}
```


### [2026-09-06T15:33:39.607Z] TOOL RESULT

```
86:نژادی بر سایرین برتری کامل داشتند. چون در آلمان و اسکاندیناوی اینگونه مردم فراوان ترند؛ آنها
135:کاملاً مر دود شده است) از عهده‌ی بحث ما خارج است. بطو رکلی کوچکی نسبی آلمان وپابش‌های
517:است: از یونانی کامل‌تر و از لاتین پرواژه‌تر و از هر دو به طور چشم‌گیری پالوده‌تر
593:و زبان‌های "تخاری الف وب" (8 ب۸ ۳0671۸181۸(7) در کامل‌سازی شجره‌ی زبانهای هند و
596:هند و اروپایی راکامل‌ترکرده‌اند. هنوز کار خواندن هزاران لوح وخشت هنت به پایان نرسیده است
629:می‌شود. نوشتارهای هند و آریایی کامل‌ترین و پیشین ترین تصویر را از یک زبان کهن هند و اروپایی
744:05880 بل8510۸شا)) برمی‌خوریم. این منون تصویر کاملی از زبان و فرهنگك و ساختار
1006:پدرسالاری خانواده و قبیله‌ای هند و اروپایی از طریق چندین واژه‌ی همریشه‌ی دیگر کاملاً مشهود
1054:هسرش) پیامد دیگری نیز داشت: مقام او والاتر از مقام پدر و رئیس ابل بود ولی آنها راکاملاً
1129:!می‌دهند. نوشتارهای اوستایی بسیار متعددترند و نمای کامل‌تری از زبان ایسرانی کهن را
1139:اندازه‌ای است که برخی از واژه‌ها و جمله‌های سانسکریتکاملاً مشاب پرابرهای اوستایی ود هستند.
1198:سانسکریت هم ذکر شده است. چون در ردیابی واژه‌ها» مرحوم معین با دقت و امانت کامل مراجع
1208:خواهیم توانست تصویر کاملی از زبان فارسی و تطور آن داشته باشیم.
1218:در چند دهه‌ی اخیر رابطه‌ی زبانهای اروپایی با یکد یگر به طورکامل مورد بررسی قرارگرفته
1225:همچون بارتولومه و معین بطرر نسبتاً کامل بازتاب شده است. کوشش من در کتاب حاضر این بوده
1227:اول -بهره گیری کامل از پژوهش‌های پیشین و منعکس سازی آنها به طور کوتهوار.
1263:سئولیت صحت ردیابی‌های دسته دوم مستقیماً به عهده‌ی من است. البته هرکجا که کاملاً مطمشن 8
1266:زبان فارسی در درخت خانوادگی زبان‌های هند و اروپایی را مشخص‌تر و کامل تر نمایند. این کتاب:
1274:«مادر) یا «گاوه با «بوغ) معنی واژه‌های همریشه در زیانهای هند و اروپایی امروزی کاملدً یکی و
1345:امید من این است که پژوهشگران دیگر به تدریج کاستی‌ها را برطرف کرده و فرهنگه‌های کاملتری از
=== latin index
1711:KAMY ATHANGATNS
1712:KAMIEN POLISH) glo) ASMAN APAHLAYD) 65
1713:KAMEN (RUSSIAN) yoy E’SMAN KURDISH) 53,
1714:KAMEN (CZECH) Sx ASMAN AAFGHAND (24) glii)
1715:KAMEN (BULGARIAN) ¢5 ji, ASHMAN, (SANSKRIT) 2, Suite
1944:VENIR ° (ld) :HTALIAN)' Ul! KAM, KAM :(TOKHARIAN A) A ¢ bs
1945:VENI (44) (RUMANIANY iho, KAM, KAM :(TOKHARIAN B) B 5 )\bs
2313:DELAMARRE: (LE LONG DE) 301 SACA, SAKAM (SANSKRIT) <y Suite |
6277:KAMPAS (LITHUANIAN) gly} ETKUMPS. :(OLD PERSIAN) kl, y+
6424:KAMPT LATVIAN) (3) 99 HEFJA
```


## [2026-09-06T15:33:50.029Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '23783,23800p' MON_part2.txt; echo \"---کعبه\"; sed -n '23819,23840p' MON_part2.txt; echo \"---مکعب\"; sed -n '63907,63920p' MON_part2.txt"
}
```


### [2026-09-06T15:33:50.107Z] TOOL RESULT

```
کعب: 9 [ع.] (.) هر بند استحوان؛ 
شتالنگ. استخوان بلند پشت پای که محل 
بستن شراکك است؛ ج. کعوب. آن جانب از 
هر طرف که به روی زمین قرار گیرد در 
صورتی که هموار و برابر باشد. استخوان 
مربع که بدان نرد بازند؛ هر یک زا کعبتین» 
طاس. (رض.) عددی که دو بار در نفس خود 
شرت شتوی (خاضا رات را مکعت 
گویند.) معب بیاله: چیزی که زیر بباله و 
فنجان سازند تا به زمین تواند نشست. سعب 
غرال: [- کعب الغزل] حلوایی است به شکل 
چا شم ۱9۵۱ . نوعی فانیذ و آن چنان بود که 
قند را به قوام می آرند و باره باره می‌نمایند 
کار شانق نله کفب. کر کف" مهره‌ای است 
که آن را قاصدان و شاطران در پای خود 


بندند به تصور آنکه هر که آن را بر پای 
---کعبه
کعبه: (۳۵)۵ 2 [ع. کعبة | (.) جای چهار 
گوش؛ مکعب. قطعه‌ای استخوانی مکعب که 
بر آن شمارة اعداد از یک تا شش نوشته با 
و آن راب 
دست گیرند یا در میان طاس نهند و بر تخته 
نرد انکنند و مطابق عددی که آن نشان دهد 
بازی کنند؛ تثنية آن: کعبتین. کعبهةً جان: ( کد.) 
مقصد جان» منظور روح. کعية جهانگر د: 
کب رهرو: (کد.) آفتاب جهانتاب. کعباة 
محرم نشان: ( کد.) آفتاب جهانتاب. 
کف: ۲:۲ [قس. کفکک ] (۱.) یکی از اشکال 
انحلال هوا در مایعاتی که گرم یا تکان داده 
می‌شوند» ایجاد می‌گردد مانند کف حاصل 
از حل صابون در آب که بنام کف صابون 
خوانده می‌شود و سرجوش و کف حاصل از 
جوشاندن برخی مواد که در سطح مایم جمع 


فر هنگ فارسی معین 


۷ ۱۳ 
---مکعب
مکعب: ِ ۵ [ع. ۰] (امف.) چهار کو شه 
کت 3 9: (.) (هس.) جسمی که دارای شش 
س (حسا.) حاصل 
وب 39 ی ۵ مریم 2و 3: 

مکفر: ۵۱۵1۳:۲" [ع.] (امف.) کافر خوانده 
سل ۵. 

مکفر: 0۲ (ع.] (امف.) کفاره داده 
سل ۵. 

مکفر: 00۲( [ع.] (افتا.) سشتت: کم 
دهنده به کسی» کافر خواننده.
```


## [2026-09-06T15:33:50.914Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\ngrep -n \"KAMA\\|Kama\\|kama\" ARY_pages.txt | head -20\necho \"=== index DESIRE\"; grep -n \"DESIRE\\|WISH\" ARY_latin_index_pages.txt | head"
}
```


### [2026-09-06T15:33:50.983Z] TOOL RESULT

```
=== index DESIRE
2042:ry sguiley AWISHTEL —ARGHAND (24) gli
2818:STANDA OLD NORSE) 5 a3 ESTATAN, AWISHTADAN
4070:BESH, WISH PAHLAVI) 5 Sy VISHA, VISH- HAVESTAN) gous!
7124:AMINDAROV: (DESIRE) 311 HEDOMAI, EDOMAI (GREEK) gly
9504:OLD ENGLISH) pS g-lSsi ‘ZINDAG, ZWISHNOMAND
9673:THIVOT, ZHIVY CZECH) Sop ‘ZITISHN, ZIWISHNIH
```


## [2026-09-06T15:33:58.321Z] TOOL CALL #49: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T15:33:58.327Z] TOOL RESULT

```


```


## [2026-09-06T15:34:03.557Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%CF%8D%CE%B2%CE%BF%CF%82",
 "prompt": "Give the full etymology section for Ancient Greek κύβος (kúbos) 'cube, die'. Does it mention Semitic/Arabic ka'b origin, Pre-Greek, or PIE *keu-b-? Quote Beekes if cited. Also list attestations (Homer? Herodotus?)."
}
```


## [2026-09-06T15:34:04.195Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cube",
 "prompt": "Give the full etymology of 'cube' as printed. Does Etymonline mention an Arabic or Semitic origin for Greek kybos?"
}
```


### [2026-09-06T15:34:11.824Z] TOOL RESULT

```
# Etymology of "Cube"

Based on the Etymonline content provided:

**Full Etymology:**
The word "cube" (noun, 1550s) comes from French *cube* (13c.) and Latin *cubus*, derived from Greek *kybos* meaning "a six-sided die." The Greek term was used metaphorically for dice-like blocks, cakes, salted fish pieces, and vertebrae. The source notes that "words for dice are often loans" and references the Lydians' claimed invention of the game.

The verb form (1580s) means "to raise to the third power" mathematically, or "cut in cubes" (1947).

**Regarding Semitic/Arabic Origins:**
No, Etymonline does not mention Arabic or Semitic origins for Greek *kybos*. The entry states the origin is "of uncertain origin" and only notes that loan words for dice were common among ancient Mediterranean peoples, specifically referencing the Lydians' claimed invention.
```


### [2026-09-06T15:34:12.389Z] TOOL RESULT

```
# Etymology of Ancient Greek κύβος

## Main Etymology Section

The etymology is described as "difficult to trace." The word circulated among multiple languages, including Latin *cubus*.

**Proto-Indo-European origin:** Scholars often connect it to PIE *\*kewbh₂-* ("to lie down actively"), reconstructed from Latin *cubō* ("lie down passively") and related forms. Comparisons include Proto-Germanic *\*hupiz* ("hip") and Latin *cubitus* ("elbow").

**Alternative theory:** According to Beekes, "words for dice are often loans and the Lydians claimed to have invented the game" of κύβος, suggesting possible Lydian origin. Beekes "rejects the connections given above to the Italic and Germanic terms."

**Arabic connection denied:** The entry explicitly states the word "appears to have no relation to Arabic كَعْبَة (kaʕba)."

## No Semitic or Pre-Greek Etymology

The etymology section contains **no mention of Semitic origins, Pre-Greek substrate elements, or ka'b connection**—it explicitly denies the Arabic link.

## Notable Attestations

The page provides one quotation from **Plutarch (46–120 CE)**, *Julius Caesar* 32, featuring the famous phrase "Ἀνερρίφθω κύβος" ("Let the die be cast"). No Homer or Herodotus references appear.
```


## [2026-09-06T15:34:19.288Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/κύβος' --note 'page 231, root K.a`.b, node #3: Greek kubos etymology — Wiktionary explicitly denies any relation to Arabic ka`ba' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/cube' --note 'page 231, root K.a`.b, nodes #3-#5: cube < F cube < L cubus < Gk kybos, of uncertain origin; no Arabic' 2>&1 | tail -3"
}
```


## [2026-09-06T15:34:21.245Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/keh%E2%82%82-",
 "prompt": "Is there a PIE root *keh2- 'to desire, wish'? Give its descendants: Proto-Indo-Iranian *kaHmas, Sanskrit kāma, Avestan/Old Persian kāma, Latin cārus, Proto-Germanic *hōraz. Quote what the page says."
}
```


### [2026-09-06T15:34:22.612Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/35ad278cdf903182.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/03ef6ec76f426286.txt
```


### [2026-09-06T15:34:29.155Z] TOOL RESULT

```
# Proto-Indo-European Root *keh₂-

Yes, there is a reconstructed PIE root *keh₂- meaning "to desire."

## What the Page States

The page defines it as: **"to desire"** and notes these are reconstructed terms based on comparative evidence, not directly attested.

## Documented Descendants

The page confirms several of the descendants you mentioned:

- **Sanskrit**: "का (kā, 'to desire, like')"
- **Latin**: *kāros* is listed as a Proto-Italic form meaning "dear"
- **Proto-Germanic**: "*hōraz ('adulterer')"
- **Avestan**: Forms related to "to please" are documented

However, the page does **not** list "Proto-Indo-Iranian *kaHmas" or "Old Persian kāma" in the main descendant sections shown. It does show Proto-Indo-Iranian forms like "*kaHyati" and "*kaHtás," but the specific terms you mentioned aren't explicitly quoted in this content.
```


## [2026-09-06T15:34:33.246Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D9%85",
 "prompt": "Give the Persian entries for کام: the etymology of کام \"desire, wish\" (Middle Persian, Old Persian/Avestan forms, PIE root), and the separate کام \"palate\". Quote the etymology text and any cited sources (MacKenzie, Hasandust, Cheung)."
}
```


## [2026-09-06T15:34:34.219Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/whore",
 "prompt": "Give the full etymology of English 'whore': Old English hōre, Proto-Germanic *hōrōn / *hōraz, PIE root, and Latin cārus cognate. Quote it."
}
```


### [2026-09-06T15:34:42.171Z] TOOL RESULT

```
# Etymology of English "Whore"

Based on the Wiktionary entry, here is the complete etymological chain:

**Modern English** → **Middle English** *hore* → **Old English** *hōre* → **Proto-Germanic** *\*hōrǭ* → **Proto-Indo-European** *\*kéh₂ros* ("loved"), from *\*keh₂-* ("to wish; desire")

## Direct Quote:

"From Middle English _hore_, from Old English _hōre_, from Proto-Germanic _\*hōrǭ_, from Proto-Indo-European _\*kéh₂ros_ ("loved"), from _\*keh₂-_ ("to wish; desire")."

## Latin Cognate:

The entry notes that Latin *cārus* ("dear, expensive") is a cognate, sharing the same Proto-Indo-European root. This demonstrates how a word meaning "beloved" or "desired" in the ancestral language evolved into the English term for a prostitute—a semantic shift reflecting historical attitudes toward the profession.
```


### [2026-09-06T15:34:42.278Z] TOOL RESULT

```
# Persian Entries for کام

## Etymology 1: "Desire, Wish"

**Etymology Text:**
From Middle Persian 𐭠‎𐭬‎𐭪 (kʾm), from Old Persian 𐎣𐎠𐎶 (k-a-m), from Proto-Iranian *káHmah, from Proto-Indo-Iranian *káHmas, from Proto-Indo-European *kóh₂mos, ultimately from PIE *keh₂- ("to desire, wish").

**Cited Source:**
MacKenzie, D. N. (1971). "kām" in *A concise Pahlavi dictionary*. Oxford University Press, p. 48.

The entry documents this word's descent through historical Persian stages, tracing it back approximately 2,500 years to Indo-European roots meaning desire or longing.

## Etymology 2: "Palate"

The dictionary notes this sense with the anatomical designation but indicates the etymology is incomplete or missing, requesting contributors to add information or discuss it further.

**Note:** The entry shows this term has a separate semantic development (body part rather than emotion/intention), though no etymological source is currently provided in the Wiktionary article.
```


## [2026-09-06T15:34:50.874Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==70' PHD.txt | grep -n \"kām\\|kam\" | head -20\necho \"--- search for 'desire, wish' in PHD\"\ngrep -n \"wish, desire\\|desire, wish\\|will, desire\" PHD.txt | head -10"
}
```


### [2026-09-06T15:34:53.087Z] TOOL RESULT

```
--- search for 'desire, wish' in PHD
422:kabk [АрА! | N ~] partridge. ~-anjir [acyl | N ~] a kind of francolin. kabód [kpwt! | N ~] grey-blue; pigeon. kabótar [kpwil | M kbwtr, N ~] pigeon. kāč [с | N kāš(ki)], ~ ka: would that, if only. кадар [01А] game, joke. кадар [ktk' | M kdg, N kada] house. ~-banig [-b'mwk! | N Radbanü] mistress, lady of the house. ~ig [-yk'] domestic; servant. ~-xwaday [-hwty | P gdyxwd?y, N kadxudā] householder, master of the house. kadām [ktm | M kd?m, N кийат) which, what. c--iz-é(w) [-c-H D] whichever. kadar [kt] who, which. 7-iz-é(w) [-c-H D] whoever. kaf [kp | N —] foam, slime. kaf-, v. kaftan. kafč [kpc | N ~] ladle, skimmer. ~ag [-А! | N ~a] spoon. kafš, ~ag [kps, -k! | N Аар] shoe. ~gar [-k/ | N ~] shoemaker. kaftan, kaf- [kp-in' | P kft, kf-] fall. kah [TBNA < A tbr | N ~] chaff, straw. kān-, ~i§n, v, kāstan. _ kahas [kts | М khs] channel, sewer. kāhēnīdan, káhén- [R'hyn-ytn!] decrease, lessen (tr.). kühidan [P hytn! | N ~] = kastan. kahist [ksst'] least. kah-rubāy [Ара | N —rubá] amber. kahwan [khwbn' | M qhwn, N kukan] old. kākom [RP Rkwm | N ~] stoat. ~ i spéd: ermine. kālbod [Аро | (M k*/byd), N ~] body, shape, form. ~ӧтапа [-wmnd] corporeal. kam [km | M kmb, N ~] little, small, few; v. kem. kam [Em | = M, N ~j will, desire, purpose. kàm-, v. kāmistan. 1катаб [k?mk! | N kama] kinds of gruel, or soup. ?kümag [k?*mk! | N kama] = kam. «-hanjām [-hnc’m] gaining one’s end, successful. -~-hanjamih: success. „ūmand [-wmnd] willing(ly), desirous. ~-widar [-wt?l | N kām-gučār] successful, independent. ~-xwaday [-Awt^y] independent, absolute. kamal [kml | (M km?7)] head (daevic). ~ig [-yR!] chief (daevic).
```


## [2026-09-06T15:34:53.463Z] TOOL CALL #57: Bash

```json
{
 "command": "pdftoppm -f 231 -l 231 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg231 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T15:34:56.698Z] TOOL RESULT

```
total 4844
drwx------ 3 sfmqrb sfmqrb   4096 Sep  6 11:34 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    682 Sep  6 11:34 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb  69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb  81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4812 Sep  6 11:28 c224_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3203 Sep  6 11:28 c224_n7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12820 Sep  6 11:27 c229_bibua.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5308 Sep  6 11:27 c229_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5313 Sep  6 11:27 c229_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb   7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12347 Sep  6 11:20 c_hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12691 Sep  6 11:20 c_ieuo.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2071 Sep  6 11:26 c_ijlak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  14654 Sep  6 11:20 c_ijlak.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12239 Sep  6 11:20 c_latis.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb 111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb  11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83691 Sep  6 11:19 gen215.py
-rw-rw-r-- 1 sfmqrb sfmqrb   2303 Sep  6 11:25 j.json
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb  37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb  77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb  61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb  80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb  67513 Sep  6 11:27 mk217.py
-rw-rw-r-- 1 sfmqrb sfmqrb  74459 Sep  6 11:33 mk218b.py
-rw-rw-r-- 1 sfmqrb sfmqrb  17605 Sep  6 11:25 mk218.py
-rw-rw-r-- 1 sfmqrb sfmqrb  50138 Sep  6 11:24 mk222.py
-rw-rw-r-- 1 sfmqrb sfmqrb  78297 Sep  6 11:32 mk223.py
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  6 11:34 p216
-rw-rw-r-- 1 sfmqrb sfmqrb  17907 Sep  6 11:25 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb  54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb  53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb 141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb 194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb 117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb  76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb 147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71937 Sep  6 11:19 pg219.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb 118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb  90848 Sep  6 11:22 pg224hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55412 Sep  6 11:15 pg224.png
-rw-rw-r-- 1 sfmqrb sfmqrb  80963 Sep  6 11:32 pg225.png
-rw-rw-r-- 1 sfmqrb sfmqrb 161218 Sep  6 11:26 pg226hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74322 Sep  6 11:19 pg226.png
-rw-rw-r-- 1 sfmqrb sfmqrb  54381 Sep  6 11:31 pg227.png
-rw-rw-r-- 1 sfmqrb sfmqrb  52519 Sep  6 11:25 pg228.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78760 Sep  6 11:27 pg229hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  42112 Sep  6 11:26 pg229.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65310 Sep  6 11:32 pg230.png
-rw-rw-r-- 1 sfmqrb sfmqrb  69894 Sep  6 11:34 pg231.png
-rw-rw-r-- 1 sfmqrb sfmqrb 147680 Sep  6 11:20 sns167.jpg
```


## [2026-09-06T15:35:04.115Z] TOOL CALL #58: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg231.png"
}
```


### [2026-09-06T15:35:04.450Z] TOOL RESULT

```

```


## [2026-09-06T15:35:04.448Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:35:21.725Z] TOOL CALL #59: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py"
}
```


### [2026-09-06T15:35:21.769Z] TOOL RESULT

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


## [2026-09-06T15:35:30.496Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN whore\"; grep -n -i \"whore\" KLN_1966.txt | head -6\necho \"=== SKT charity/cherish/caress/whore\"; grep -n -i \"^CHARITY\\|^CHERISH\\|^CARESS\\|^WHORE\" SKT.txt | head\necho \"=== IEC kamo\"; grep -n \"^kāmo\\|^kamo-\\|^kāro\\|^karo-\" IEC.txt | head\necho \"=== WLD Bd1 kā\"; grep -n \"cärus\\|cārus\\|hōra-\\|kämo-\" incoming/WLD/WLD_Bd1_pages.txt | head"
}
```


### [2026-09-06T15:35:30.589Z] TOOL RESULT

```
=== KLN whore
7221:charitable,  adj .  —  OF.  (  =  F.)  See  charity  and  -able. Derivatives:  charitable-ness,  n.,  charitabl-y,  adv. charity,  n.  —  F.  charite,  fr.  L.  caritatem,  acc.  of caritas,  ‘dearness,  affection,  love’,  fr.  edrus, ‘dear,  precious,  esteemed,  loved’,  which  is  cogn. with  OTr.  carae,  ‘friend’,  caraim,  W.,  Co. car,  ‘friend’,  W.  caraf,  ‘I  love’,  Lett,  kars, ‘greedy’,  kare,  ‘desire’,  karuot,  ‘to  desire’,  ON. hora,  OE.  hore,  ‘whore’.  All  these  words  derive fr.  I.-E.  base  *qa-,  ‘to  desire',  whence  also  OI. kimah,  ‘desire’,  kdyamanah,  ‘loving’,  Toch.  B kawait,  ‘desire’,  Lith.  kamaros,  ‘lasciviousness’, Lett,  kamet,  ‘to  hunger’.  Cp.  caress,  cherish, Kama,  whore.  For  the  ending  see  suff.  -ity. charivari,  n.,  a  mock  serenade,  rough  music.  — F.,  fr.  Late  L.  caribaria,  fr.  Gk.  xap-/;  (Sapid, ‘heaviness  in  the  head,  top  heaviness’, compound¬ ed  of  xd pi,  ‘head’,  and  (hipoc,,  ‘weight’;  see cerebrum  and  baro-.  The  sense  development  of the  French  word  is  explained  easily  by  the  effect of  a  deafening  noise  (‘charivari’)  upon  the  head. Cp.  shivaree.
15210:foment,  prep.,  opposite  to  (provincial).  — Formed  fr.  fore,  adv.,  and  anent. fornicate,  intr.  v.,  to  commit  fornication.  —  ML. fornicatus,  pp.  of  fornicari,  ‘to  commit  whore¬ dom’,  fr.  fornix,  gen.  fornicis,  ‘arch,  vault; brothel’,  which  derives  fr.  fornus,  ‘oven’,  later used  in  the  general  sense  of  ‘vault,  arch’;  see furnace  and  cp.  fornix.  Brothels  were  called fomices,  i.e.  ‘arches’,  because  prostitutes  used to  gather  ‘under  the  arches’  of  certain  buildings of  ancient  Rome.
22793:mangle,  n.,  a  machine  for  smoothing  linen.  Du. mangel,  fr.  MDu.  mange,  mangonel  ,  fr.  It. mangano,  fr.  L.  manganum,  fr.  Gk.  jxayyavov, ‘any  means  for  tricking  or  bewitching,  philter, drug’  (whence  izayyavcuEiv,  ‘to  use  charms  of philters’),  fr.  I.-E.  base  *mang-,  ‘to  embellish, dress,  trim',  whence  also  OPruss.  manga, ’whore’,  Mir.  meng,  ‘craft,  deception’,  and  pos¬ sibly  also  Ol.  man  juft,  mahjulah,  ‘lovely,  charm¬ ing,  beautiful’.  Cp.  mangonel,  monger. Derivatives:  mangle,  tr.  v.,  mangl-er,  n.,  mangl¬ ing,  adj.,  mangl-ing-ly,  adv. mangle,  tr.  v.,  to  mutilate.  —  ME.  manglen,  fr. AF.  mangier,  contraction  of  mahangler,  freq.  of OF.  mahaignier,  ‘to  mutilate,  wound’.  See  maim. Derivatives;  mangl-er, n.,  mangl-ing,  adj.,  mangl- ing-ly,  adv.
=== SKT charity/cherish/caress/whore
3358:Cherish  ;  tec  Caress.
21436:Whore,  sb,  (Scand.)  The  w  is  unori- ginal.  M.  E.  ^i»r¥.  — Iccl.  Aira,  an  adul* teress,  fern,  of  A6rr,  an  adulterer;  Dan. Aort,  Swed,  Aom.  -+•  t)u,  Aoer,  G.  Aurt, O.  H.  G.  Aucra;  Goth.  Acn,  masc.  an adulterer.  Allied  to  Polish  Auram,  Church- Slavonic  kurttva,  an  aduttereaa.  Prob. also  to  L.  rarMT,  loving,  Skt.  kdmaga,  a lascivious  woman  (from  /tarn,  to  love). ^[Certainly  not  allied  to  hire  I
=== IEC kamo
=== WLD Bd1 kā
```


## [2026-09-06T15:35:40.668Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf8',errors='replace').read(); lines=txt.split('\\n')\nimport re\nfor ln in (7221,):\n    off=sum(len(l)+1 for l in lines[:ln-1]); leaf=txt[:off].count('\\f')\n    blk=txt.split('\\f')[leaf]\n    print('charity leaf',leaf,'nums',re.findall(r'(?m)^ *([0-9]{2,4}) *$',blk))\nblk=txt.split('\\f')\nfor i in (881,882,883,884,885):\n    b=blk[i]\n    print('leaf',i,'nums',re.findall(r'(?m)^ *([0-9]{2,4}) *$',b), b[:80].replace('\\n',' '))\nEOF"
}
```


## [2026-09-06T15:35:42.563Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"^Caress\" SKT.txt | head; sed -n '3350,3362p' SKT.txt\npython3 - <<'EOF'\ntxt=open('SKT.txt',encoding='utf8',errors='replace').read(); lines=txt.split('\\n')\nfor ln in (3358,21436):\n    off=sum(len(l)+1 for l in lines[:ln-1]); leaf=txt[:off].count('\\f'); print(ln,'leaf',leaf,'-> p',leaf-20)\nEOF"
}
```


### [2026-09-06T15:35:42.679Z] TOOL RESULT

```
charity leaf 152 nums ['268', '269']
leaf 881 nums [] ,  suff.  corresponding  in  meaning  to  E.  -ness. —  F.,  fr.  L.  -tiido,  g
leaf 882 nums [] (=  F.  ton¬ neau),  ‘cask,  tun’,  dimin.  of  tonne,  ‘tun’,  which derives  f
leaf 883 nums ['1666'] turriculated,  adj.,  resembling  a  small  turret  or turrets.  —  Formed  with
leaf 884 nums [] of  two',  fr.  did,  ‘two’. Derivatives:  twigg-ed,  twigg-en,  twigg-y,  adjs.
leaf 885 nums [] Truravov, ‘kettledrum’.  See  tympanum  and  subst.  suff.  -ite. tympanitic,  a
```


### [2026-09-06T15:35:44.436Z] TOOL RESULT

```
k
Pcrs.)  M.  E.  wcA^*^nf.-0.  F.  tschequitr, a  chea-board  ;  heiicc  ■.  chcckereil  cloth  on wliich  accounts  were  reckoned  by  means  of counteis.  —  O.  K.  eschet,  check;  «c  Check.
Cheek.  (E)  M.  E  ekike,  chtokt.  -  A.  S. rrc/r^,  check. + Da  i(aa^.  jaw^  dicck ;  Swed. kik,  jaw.     Allied  to  Jaw.
Cheer.  <J,  -  L.  -  Gk.)  M.  E.  chirt. orii^.  ihc  mien  ;  hence  *  to  be  of  good  (hter* —  U.  F.  chert,  the  face  —  Low.  U  €ara, face.^Gk.  «iipa,  the  head.  Der  fhttr-fult &c.
Chees*.  (L.)  M.  E.  thts*.  A.  S.  iht, (yse.  —  L.  castus^  cheese;  whence  other foMiis  are  borrowed.
Chemise.  (K.-L-C?)  ¥.  chemist, •-Laic  L.  ramiVt'a,  a^iirt,  ihin  dress.  I'rob. Celtic;  cf.  U.  Iii&h  taimma,  shiiU
Chemiat,  Chymiat ;  »hoit  for  mi- chemist  \  see  Alohemx.
Cheque,  Chequer ;  sec  Ohook.
Cherish  ;  tec  Caress.
Cherry.  (F.-L.-Gk.)  ME.  eheri.  a omlake  for  eken's^  the  final  s  being  mistaken for  the  pi.  inflcxioti.  —  O.  K.  arise.  —  1^ orranu.  a  cbcriy-trec.  —  Gk.  itlftaaoi,  a cherry-tree ;  usually  said  to  come  from Ccrwos^  in  Poaius;  a  story  which  Curtius dcMibis.
Chert,  a  kind  of  quarti.  (C?)  The Keiitiib  form  ts  chart,  rough  ^ruuniL  Pro- bably from  Irish  ceart,  a  i«:bble;  cf.  Gael. *WT,  a  shelf  of  rock,  W.  carts»  stone
Cherub.  (Heb.)  The  inie  pi.  is  iMentb- $m,  «  Hcb.  k'nlv  ^pl.  k^nivim),  a  mystic ficure.
Ch«Trtl»  a  plant,  (U-Gk.)  A.S.  r<rf- ^//.  —  L.  cartjolium  (Pliny),  — Gk.  x^f><- fw^Xo•',  chervil,  Itt.  plea&ant  leaf.-Gk. Xaf»-'«i',  to  rejoice ;  ^^vXAoa*,  leaf.
3358 leaf 99 -> p 79
21436 leaf 588 -> p 568
```


## [2026-09-06T15:35:53.700Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nblk=open('KLN_1966.txt',encoding='utf8',errors='replace').read().split('\\f')\nprint('total leaves',len(blk))\nfor i in range(915,930):\n    b=blk[i]; print(i, re.findall(r'(?m)^ *([0-9]{2,4}) *$',b), b[:70].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T15:35:55.616Z] TOOL RESULT

```
Exit code 1
total leaves 903
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
IndexError: list index out of range
```


## [2026-09-06T15:35:59.123Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nblk=open('KLN_1966.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i in range(893,903):\n    b=blk[i]; print(i, re.findall(r'(?m)^ *([0-9]{2,4}) *$',b), b[:70].replace('\\n',' '))\nEOF\necho \"=== KLN_1971 whore\"; grep -n -i \"whore,  n\\|^whore\" KLN_1971.txt | head"
}
```


### [2026-09-06T15:36:01.605Z] TOOL RESULT

```
893 [] id.  Cp.  also uvea,  uvula. uvanite,  n.,  a  hydrous  uranium  vanad
894 [] andering’,  formed with  gerundive  suff.  -bundus  fr.  vagari.  See 
895 ['1691'] ,  bodies  of  those  who were  slain  in  battle’,  wol,  ‘pestilence
896 ['1692'] ��,  nr^  (Hesychius), ‘web’,  L.  pannus,  piece  of  cloth’.  See  p
897 []   —  A  hybrid  coined  fr.  vari¬ ola  and  suff.  -ite  (representin
898 ['1694', '1695'] agential  suff.  -or. vau,  also  waw,  n.,  the  sixth  letter  of  t
899 ['1696']   F.)  veine,  fr.  L. vena,  ‘blood  vessel,  watercourse,  vein;  na
900 [] r’, vojina,  ‘war’,  Gk.  iep.ai  (for  ‘I  as¬ pire  to,  tend  to,  
901 [] , ventricle,  n.,  cavity  in  an  organ  of  the  body.  — Fr.  F.  v
902 [] ��true’,  and  Gk. ruov,  fr.  mtoraiv,  ‘to  look  at,  examine’.  Se
=== KLN_1971 whore
266963:whore, n., a prostitute. — ME. hore, fr. OE. hore, 
266976:whoredom, n. — ME. hordom, fr. ON. hordomr,
```


## [2026-09-06T15:36:09.139Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '266963,266980p' KLN_1971.txt\necho \"=== KLN_1971 caress / cherish\"\ngrep -n \"^caress, n\\|^cherish, tr\" KLN_1971.txt | head\nsed -n \"$(grep -n '^caress, n' KLN_1971.txt | head -1 | cut -d: -f1),+6p\" KLN_1971.txt\nsed -n \"$(grep -n '^cherish, tr' KLN_1971.txt | head -1 | cut -d: -f1),+6p\" KLN_1971.txt"
}
```


### [2026-09-06T15:36:10.947Z] TOOL RESULT

```
whore, n., a prostitute. — ME. hore, fr. OE. hore, 
fr. ON. hora, ‘adulteress’ (whence Dan. hore, 
Swed. hora, ‘whore’), which is rel. to ON. horr, 
‘adulterer’, and to MDu. hoere, Du. hoer, OHG. 
hoaru, MHG. huore, G. Hure, ‘whore’, Goth. 
hors , ‘adulterer’, from I.-E. base *qa-, ‘to 
desire’, whence also L. cams, ‘dear, precious’. 
See charity and cp. words there referred to. The 
w in whore is intrusive; cp. whole. 

Derivatives: whoredom (q.v.), whor-ish, adj., 
whor-ish-ly, adv., whor-ish-ness, n. 

whoredom, n. — ME. hordom, fr. ON. hordomr, 
which was formed fr. horr , ‘adulterer’, with suff. 
-domr. See prec. word and -dom. 

whorl, n., 1) a small flywheel on a spindle; 2) ar- 
=== KLN_1971 caress / cherish
39793:caress, n., an act of endearment. — F. caresse , 
44875:cherish, tr. v. — ME. cherischen , fr. OF. cheriss -, 
caress, n., an act of endearment. — F. caresse , 
back formation fr. caresser. See caress, v. 

caress, tr. v., 1) to touch endearingly; 2) to flat- 
ter, — F, caresser , fr. It. carezzare , lit. ‘to cher- 
ish’, fr. caro, ‘dear’, fr. L. carus, of s.m. See 
charity and cp. cherish. 
cherish, tr. v. — ME. cherischen , fr. OF. cheriss -, 
pres. part, stem of cherir (F. chdrir), ‘to hold 
dear, cherish’, fr. cher, ‘dear’, fr. L. cants 
(whence also It., Sp., Port, caro , OProven?., 
Catal. car). See charity and verbal suff. -ish 
and cp. caress. Derivatives: cherish-er, n., cher- 
ish-ing, adj., cherish-ing-ly, adv. , cherish-ment , n .
```


## [2026-09-06T15:36:23.035Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%83%D8%B9%D8%A8",
 "prompt": "Arabic كعب (kaʿb): give the etymology, the root ك ع ب, the meanings (ankle, heel bone, cube), and any note on Semitic cognates. Also anything on كعبة (kaʿba) and مكعب (mukaʿʿab)."
}
```


## [2026-09-06T15:36:23.800Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/whore",
 "prompt": "Give the full etymology of 'whore' as printed: Old English hore, Proto-Germanic *horaz/*horon, PIE root *ka-, Latin carus. Quote it."
}
```


### [2026-09-06T15:36:29.939Z] TOOL RESULT

```
# Etymology of "Whore"

Based on the Online Etymology Dictionary, the word traces back through these stages:

**Old English:** "hore" (prostitute, harlot)

**Proto-Germanic:** *hōran-* (feminine *hōrā-*)

**Proto-Indo-European:** *ka-* (to like, desire)

The source states: "It is considered to be, probably, etymologically, 'one who desires,' from PIE root *ka- 'to like, desire.'"

However, the document does not support the etymological chain you've requested (Old English hore → Proto-Germanic *horaz/*horon → PIE *ka-* → Latin *carus*). While the entry confirms the first three stages, it contains no mention of *carus* or any direct connection to Latin in the primary etymology section. The Latin terms discussed (*meretrix*, *putidus*, *scortum*) appear as comparative examples from other languages, not as part of "whore's" direct lineage.
```


### [2026-09-06T15:36:30.775Z] TOOL RESULT

```
# Arabic كعب (kaʿb)

## Etymology & Root
The word derives from the Semitic root **ك ع ب** (k ʕ b), which generates five related terms in Arabic.

## Primary Meanings
According to the Wiktionary entry, the noun كعب encompasses:

1. **Anatomical**: "ankle, anklebone" - the most prominent meaning, appearing in Quranic usage (5:6)
2. **Related senses**: joint, articulation, knob, node
3. **Extended uses**: heel (marked as proscribed), high heels, stub/coupon, ferrule
4. **Figurative**: fame, glory, honor, rank
5. **Geometric**: cube, die

## Verb Forms
- **Form I** (كَعَبَ): "to be full and round, to be swelling"
- **Form II** (كَعَّبَ): "to cube" or "to dice"

## Related Terms
The entry mentions **كُعْب** (kuʕb), an alternate noun meaning "breasts, bosom," sharing the same root but distinct vocalization.

The Wiktionary page does not specifically discuss كعبة (Kaaba) or مكعب (cube/cubic form) as separate entries, though the geometric sense appears in the Form II verb definition.
```


## [2026-09-06T15:36:35.016Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/keh₂-' 'https://en.wiktionary.org/wiki/کام' 'https://en.wiktionary.org/wiki/whore' 'https://www.etymonline.com/word/whore' 'https://en.wiktionary.org/wiki/كعب'; do\npython3 tools/fetch_source.py \"$u\" --note 'page 231 (roots Kâ 1 / K.a`.b) — etymology check' 2>&1 | tail -1\ndone"
}
```


### [2026-09-06T15:36:38.378Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/21a2cf1a80fa5f9b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e0e8470db344e204.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/607dbbca971ff0f3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cc8ee96647b87641.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/77fcd9b78ea346b6.txt
```


## [2026-09-06T15:36:50.470Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW carus\"; grep -n \"cārus\\|carus,\" LEW_1910.txt | head -5\necho \"=== LAT carus\"; grep -n \"^cārus\\|cārus,\" LAT.txt | head -5\necho \"=== LEW cubus\"; grep -n \"cubus\" LEW_1910.txt | head -5\necho \"=== SYN dear/desire\"; grep -n \"^4\\.\\|DEAR\\|DESIRE, WISH\\|16\\.6\" SYN.txt | head -12"
}
```


### [2026-09-06T15:36:50.567Z] TOOL RESULT

```
=== LEW carus
=== LAT carus
=== LEW cubus
=== SYN dear/desire
759:4. Goth. fairhwus (the commonest rendering of xécyos): ON fjor, OE feorh, OHG ferah ‘life’, ON firar, OF firas ‘men’ root connection? Walde-P. 2.45. Feist 139.
819:4. Ir. talam, NIr. talamh, Lat. tellus (mostly poet.) : Skt. tala- ‘surface, bot-
844:4. Boh. pida ‘bottom, ground, soil’ (Russ. pod ‘bottom of a haycock, hearth’) : Grk. wédov etc. (above, 1). Here also prob. Russ. pocva (the reg. technical term for ‘soil’), fr. *pod(d)sva beside podosva ‘sole’?
863:4. Goth. mulda = OE molde ‘loose earth, soil’, ete. (1.212).
943:4. Goth. malma = ON malmr ‘ore, metal’, OF mealm in mealmstan ‘malm- stone’, OHG melm ‘dust’, all fr. the root of Goth. malan, Lat. molere, ete. ‘grind’. Walde-P. 2.285. Feist 343.
1038:4. Goth. stabs ibns (rendering exactly the Grk. rézos zredwés ‘level place’), OE emnet (rare), OHG ebandte (Otfr., where ebent is ‘likeness’), MHG, NHG ebene, fr. adj. seen in Goth. tbns, OE efen (eben,
1080:4. Ir. glend, glenn, NIr. gleann (NE glen fr. Gael.), W. glyn : W. glan ‘brink, shore’, Br. glann ‘riverbank’ (1.27). Pedersen 1.38. Development fr. ‘steep slope’ through ‘ravine’ to ‘valley’?
1134:4. ON meginland, cpd. of megin ‘might’, in cpds. ‘main’. Similarly and perh. of Norse origin ME mayn land, NE mainland (NED s.v. main, 2).
1262:4. Ir. foirrce, fairrge ‘ocean, sea’ (rare), NIr. Jairrge (Gael. fairge ‘sea’,
1322:4. ON fjordr (whence NE firth, frith), Dan. fjord, Sw. fjdrd, used of the long, narrow arms of the sea characteristic of the Scandinavian coast : OE ford ‘ford’, Lat. portus ‘harbor’, etc. Walde-P. 2.40. Falk-Torp 226.
1352:4. Ir., Br. tonn, W. ton : early NHG ttinne ‘wave’, LG diinen ‘swell’, Lat. tumére ‘swell’, Grk. ztdos ‘swelling, Walde-P. 1.708.
1393:4. Grk. rorapss (NG POp. wordt), fr. root of rimrw ‘fall’, réropat ‘fly’, Skt. pat- ‘fly, fall’, etc. That is, Torayés was at first the ‘falling, plunging, rushing’ stream. Walde-P. 2.19. Persson, Bei- trige 654. Kretschmer, Glotta 27,248 f.
```


## [2026-09-06T15:36:57.534Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"16\\.6[0-9]\\|DESIRE\\|Desire\" SYN.txt | head -10\necho \"=== LEW car\"; grep -n -i \"\\bcarus\\b\" LEW_1910.txt | head -3; grep -n -i \"carus\" LAT.txt | head -5"
}
```


### [2026-09-06T15:36:57.601Z] TOOL RESULT

```
5093:Russ. ochotit’sja refl. (with na ‘on’ when used transitively) fr. ochata ‘de- sire, will, hunt, chase, sport’ : chotét’, ChSI. chotéi ‘wish’ (16.61). For the change ‘desire’ > ‘hunt’, cf. Skt. lubdha- ‘greedy’, as sb. ‘hunter’. Berneker 398 f.
19195:Dan. tryg, Sw. trygg: ON tryggr, Goth. triggws, OF triewe, OHG gi-triuwi, etc. ‘true, trustworthy’ (16.66). Falk- Torp 1290.
19307:In the Romance languages generally ‘to harm’ is most commonly expressed by phrases, as It. far male, Fr. faire (du) mal, Rum. face réu, all lit. ‘do ill’ (ef. ‘bad’ 16.62). Similarly, after French, Br. ober drouk, etc. and Du. kwaad doen.
19313:m ; es with ol¢ ‘pad’ (16.62). For lor-
19315:Br. ober drouk, ober gwall do ill’ (like fr. faire mal), phrases with words - ‘had’ (16.62), also ober gaow ‘do wrong (ike Fr. faire tort) with gaow ‘false, wrong, 2 lie’ (16.71).
19318:Goth. ga-sleibjan, lit. ‘endanger’ : dips ‘dangerous, bad’, sleibi ‘danger’, Ha ‘dangerous, cruel’, etc. (16.65). te eo ME harme, NE harm, : a OE hearm ‘hurt, injury, harm’ tu, face a fe one harm ; ef tts, coe se ‘ NEG harm but root connection? - Samu shame’, . a a Walde-P. 1.463, NY inj: fh a fits Dack-formation to injury Tight, law? Wrong, injustice’ : izs
21343:Words for ‘remain, stay’ (in one place as opposed to ‘move, go’) coincide in part with those for ‘remain’ = ‘be left over’ (12.17), the development being mostly from the first to the second, but sometimes the opposite. Furthermore, just as words for ‘remain’ may be used for ‘await, wait for’ (as Grk. pévw Hom. Il. 16.620, etc., Lat. manére hostem, OPers. mam amdanaya ‘awaited me’), so conversely there is a group of words which, from such notions as ‘watch, look for, hope for’, have come to mean ‘wait for’ and may then be used also intransi- tively for ‘wait’ closely approaching ‘re- main, stay’. Hence such words are added in the list, even though most of them are still distinguished in feeling and range of use from those given in the first place.
23419:ON tala, Dan. tal, anial, Sw. antal, OE getel, ME tale (OE talu only ‘ac- count, tale’), Du. getal, OHG zala, MHG zal(e), NHG zahl : ON tala ‘speak, talk’, OE italian ‘consider, reckon, account’, OHG zalén ‘count, relate, pay’, etc., (perh. Grk. 560s, Lat. dolus ‘guile, de- ceit?, but see 16.68). Walde-P. 1.808. Falk-Torp 1243. Walde-H. 1.366.
27365:influenced by the more common @ode- pos ‘muddy, turbid’, esp. of water, etc.. but also ‘dirty’ (cf. téare vite Porepav adivbov, Theocr. 16.62), deriv. of 86dos ‘mud, dirt’.
27460:16.61 Wrz, Wiss (vb.)
=== LEW car
10140:carus, -a, -»■: cher (qu'on ch6rit); et "cher, de h&ut prix; k
10154:L'adjectif carus a un correspondant dans got. hors "7K>pvo$, |ioi,)(0$",
40394:avec ane Ipithbte'qui sonligne ce caractbre: carus, dulcis. En oatre
55954:scarus, -I m. : scare (Hor., Plin.). Emprunt au gr. oxapoS, demeure
```


## [2026-09-06T15:37:01.017Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10140,10170p' LAT.txt\necho \"=== LAT cubus\"; grep -n \"^cubus\\|cubus, -i\" LAT.txt | head -3"
}
```


### [2026-09-06T15:37:01.083Z] TOOL RESULT

```
carus, -a, -»■: cher (qu'on ch6rit); et "cher, de h&ut prix; k
qui l'on attribue une grande valeur"; carum habere alqm "tenir quel-
qu'un comme 6tant de grand prix". Plaute joue sur le double sens, Ba.
309-310, ...in Ephesost Ephesiis carissimus. | - ne ille hercle mihi sit
multo tanto carior, | si me illoe auro tanto circumduxerit. Ancien,cascus
- 183 -
usuel. - M.L.1735.
Derivas: cdritBs : tendresse, affection, aaour ( amor 70 X 00 $, caritas
7100 $ dit Quint. 6,3^13) et "chert 4 ". Daas la langae de 1 'iglise a servi
a tradaire le gr. a-y<X 7 Cr|, et a 4 t <5 pris quelquefois dans 1 'acception
speciale de "charit6"; M.L.1695; iri. cartoit, gall. cardaiod. Adverbes:
care, caro. Pas de verbe. Malgr 4 la diff 4 rence de quantit 4 , les an-
ciens le rapprochent de c&reo par etyaologie popnlaire, cf.Trag.inc.
194, quam cara sint quae post carendo intellegunt.
L'adjectif carus a un correspondant dans got. hors "7K>pvo$, |ioi,)(0$",
v.h.a. huora "fille publique", et dans 1'adjectif lette fears "friand,
plein de d^sirs". Le celtique a, en regard, des d 4 riv« 5 s A vocalisme
xiro: iri. carae et gall. car "aai", iri. caraim "j'aiae".. - L' 414 aent
*-ro- aprfes o doit etre suffixal; la racine se retrouve peut-etre dans
v.nl.koxati "aiaer" avec vocaliane radical xiro coaae en celtique. - En
revanche le c- de skr. cflruj, avec son 5 reposaat sur I "aiaable, bien-
venu", eapecherait de rapprocher le groupe de skr. kdyamanah "d^sirant",
etc.
caryon, -1 n.: noix. Transcription du gr. xapuov, dont il a existi
un doublet vulgaire f£ainin carya , et peut-etre un diainutif cario la,
cf.Tbes. s.u. Le aot a de noabreux repr^sentants dans les 1 . roaanes,
N.L.1736.
caryophyllon, -In.: giroflier, girofle. Eaprunt au gr. jcoipuocpuAXov,
defora^ par l' 4 tyaologie popnlaire en pariophalum (cf.ital. garofano),
cariofolium, etc. Cf.Tbes. s.u., M.L.1737.
casa, -ae f.: huttej cabane (de pUtre); - est agreste habitaculum
=== LAT cubus
```


## [2026-09-06T15:37:56.485Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 p.325 (leaf 334)\"; awk 'BEGIN{RS=\"\\f\"} NR==334' incoming/WLD/WLD_Bd1_pages.txt | head -30"
}
```


## [2026-09-06T15:37:57.676Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC kam\"; grep -n \"^kāmos\\|^kāmo\\|^kāros\\|^karos\\|^kāro\" IEC.txt | head\necho \"=== SYN 16.61\"; sed -n '27460,27500p' SYN.txt\necho \"=== AFM كعب\"; grep -n \"كعب\" AFM_pages.txt | head -5"
}
```


### [2026-09-06T15:37:58.219Z] TOOL RESULT

```
=== WLD Bd1 p.325 (leaf 334)
                                                                     K.
qa- ,-gern haben, begehren“.
    Ai. kdyamana- ,.gern habend“ a-lcctytya „begehrenswert" mit aus diesem
                                                             (

jo-Praesens verschlepptem -y-, daher keine Stiitze fiir einen Wzansatz
*qai-, s. Persson Beitr. 574 gegen J. Schmidt Krit. 53, Wackernagel Ai.
Gr. I 15), Pf. cake „sich woran erfreuen, zu gewinnen. suchen, lieben,
begehren“, -kati- (in Zs.) „heischend, verlangend"'; av. ka- „wonach ver-
langen“ (kayo. 1 sg., kata-, cakuse Bartholomae Airan. Wb. 462); -wo-St.
                               .
                                                                 ;

ai. kama- m. „Begehren, Wunscb, Liebe“, av. ap. kama- m. „Yerlangen,

Wunsch“, woraus nacb Bartholomae Airan. Wb. 462, 463 die ai. Wz. kam-
erst sekundar entsprungen ware (Rgv. Prs. kdmayati, PPfMed. cakamand -
dann kamra- „reizend, schon“, kamana- „begierig, liistenY) doch seheint                         ;

lit. kamaros  „Geilheit“ (Nesselmann, Leskien Nom. 447) und lett. kdniet
„hungern“ (Endzelin KZ. 44, 63) die Anfange dieser Entwicklung bereits
in altere Zeit binaafzuriicken
   ro-St. lat. cams „lieb, wert, teuer (auch vom Preise)“, lett. Mrs „liistern,
               1
begehrlich (kdruot „begehren, verlangen“), got. hors „Ehebrecher, Hurer“,
                   '
```


### [2026-09-06T15:37:58.293Z] TOOL RESULT

```
=== IEC kam
6823:karos (2), see kara
=== SYN 16.61
16.61 Wrz, Wiss (vb.)
16.62 Derstre (vb.)
16.63 Hops (sb.)
16.64 THanxs
16.65 Farrarun
16.66 Tru
16.67 Li (sb.)
16.68 Dercrir
16.69 Forcive
16.71 Goop
16.72 Bap
16.73 Ruicur (adj.)
16.74 Wronc (adj.)
16.75 Sin
16.76 Fauur, Guivt
16.77 Mistaxr, Error
16.78 Bam (sb.)
16.79 Praise (sb.)
16.81 BravuriroL
16.82 Ucty
tions are so complex that no rigid classi-
fication has proved acceptable to psY-
chologists generally; and there 18 ae
tainly none which it would be profitab e
to impose upon our study, in which we
are dealing with unsophisticated 40
often overlapping notions. : While attempting to bring 1
nto con-
“Sag Seed
. TEMP
in obviously related emo- hasis on the arrange- me of the items, if would seem to have
-, « chapter on emotions _ evonvenientlY brought into "vith others of distinctly emo- aS0 especially are certain or objective notions which in-
mp tg wwe lay 20 © tions Wed. 90
situations gpire emo ger” may J ful, gncon
tonishment’ ; ely emotional ‘glory’; @ ‘shameful
act, disgrace’ to the feeling of ‘shame’ ; fegre’ aS ‘attention’ to ‘anxiety, grief, sorrow’, sometimes ‘danger’ or ‘hate’ and fondness, love’; ‘distress, trouble’ may lead to ‘anger’; objects of repulsion pro- voke ‘disgust’ and then ‘hate’ and simi- larly in other cases, while the opposite shift from subjective to objective (‘fear’ to ‘danger’, etc.) is, of course, also at- tested, Words for certain actions that are ex- pressive of emotion, whether or not they lead to actual names of emotions, are included, as ‘laugh, smile’, ‘weep’, ‘kiss’. Ina few cases the emotion is antecedent : its expression (‘love’ > ‘kiss’ in Grk. A. Osh ma Fie a rom one physical act to an- age. ‘eae both are expressive of the ‘veep"), lon (‘beat the breast’ > ee and a ‘bad’, tein? ee co ith th
esthetic notions are mvenience, as ‘good’, oe € overlapping ‘fault’ em) and ‘beautiful, ae
empessione e eed of course, that all Pree. ) emotion, 48 well as those 85s, eae and thought proc- “ titnations imately on physical actions om in the hie large measure this is inashite story of the words either pplication observable within
Digitized by Arya Samaj Foundation Chennai and eGangotri
ERAMENTAL, MORAL, AESTHETIC NOTIONS 1085
the historical period of a given language or by the cognates in other languages. But in some groups of cognates an emo- tional value is so widespread that no cer- tain trace is left of the underlying physi- cal value, so that its determination is highly speculative or hopeless.
=== AFM كعب
3808:» ( الا نوب) ما بين الكعبين م الل اي ܝ النبات ما بين عقدتنه
```


## [2026-09-06T15:38:11.989Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^kāra\\|^kara (\\|^kara-\\|^kāmos\\|^kamos\" IEC.txt | head\nsed -n \"$(grep -n '^karos (2), see kara' IEC.txt | cut -d: -f1),+2p\" IEC.txt\ngrep -n \"kāma-\\|kāmos\" IEC.txt | head -5"
}
```


### [2026-09-06T15:38:13.747Z] TOOL RESULT

```
6708:kamos, kamos, see kam- (2). Cf. WP I, 388 & 507 Gk. kémós 'bridle-bit; muzzle; wicker basket;
karos (2), see kara
karpinos “a tree, hornbeam (?) Hitt, karpinas (a tree); Lat. carpinus “horn- beam’. (Isophonic: Li. karpiniai 'lace")
karquos, à (?) joint. See kark-. (Slav. and Li. evidence ambig. Gk. also) Gk. karpós ‘wrist’; Li. kárka ‘trotter; fetlock"
```


## [2026-09-06T15:38:16.811Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^kara \" IEC.txt | head; grep -n \"'dear'\" IEC.txt | head -8\ngrep -n \"hōros\\|hōraz\\|hors 'ad\" IEC.txt | head -5"
}
```


### [2026-09-06T15:38:16.888Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:38:23.324Z] TOOL CALL #76: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg231.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/231.png && ls -l /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/231.png"
}
```


### [2026-09-06T15:38:23.387Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 69894 Sep  6 11:38 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/231.png
```


## [2026-09-06T15:38:25.067Z] AGENT

Now I'll write the verification file.


## [2026-09-06T15:45:53.829Z] TOOL CALL #77: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-231.json",
 "content": "{\n  \"pdf_page\": 231,\n  \"book_page\": 201,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Kâ 1, Qâ\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *keh₂- 'to desire, wish' (Pokorny kā-, p. 515; Walde-Pokorny qā-, WP I 325; Watkins/AHD kā-)\",\n      \"note\": \"The root is real and standard. Nourai's double heading 'Kâ 1, Qâ' simply reproduces the two competing notations of his two sources: Pokorny 1959 writes 'kā- (kǝ-), kāro-, kāmo- \\\"begehren, gern haben\\\"' (IEW 515) while Walde-Pokorny 1927 writes the same root 'qā- \\\"gern haben, begehren\\\"' (WP I 325) — q was the older way of writing plain velar *k. In laryngeal notation the root is *keh₂-, with the two derived stems *kóh₂-mo- (> Indo-Iranian kāma-) and *kéh₂-ro- (> Lat. cārus, Gmc. *hōraz). Language label ('Indo-European') and gloss ('to wish, desire') are both correct. The one soft spot in the entry is node #5 (Av. canah-/cinah-), which Pokorny himself attaches to this root only with a question mark; node #6 is a blank box printed in the book.\",\n      \"note_fa\": \"ریشهٔ هندواروپاییِ آغازین *keh₂- «خواستن، آرزو کردن» ریشه‌ای است پذیرفته‌شده؛ پوکورنی (ص ۵۱۵) آن را kā- و والده‑پوکورنی (ج ۱ ص ۳۲۵) همان را qā- می‌نویسد و همین دو نگارش است که نورایی زیر عنوان «Kâ 1, Qâ» کنار هم آورده است. دو ستاکِ مشتق از آن، یکی *kóh₂-mo- که به هندوایرانی kāma- «آرزو، کام» رسیده و دیگری *kéh₂-ro- که لاتینی cārus و ژرمنی *hōraz از آن است. برچسب زبانی و معنای ریشه در نمودار درست است؛ تنها بندِ سست، گرهٔ ۵ (اوستایی canah-/cinah-) است که خود پوکورنی آن را با علامت پرسش به این ریشه بسته است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/keh₂-\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:515\",\n          \"status\": \"supports\",\n          \"note\": \"Pokorny IEW p. 515 (POK_02.txt leaf 174; POK_full.txt line 44412 'Root / lemma: ka- / Meaning: to like, wish', 'Page(s): 515'): 'kā- ... Ai. kāyamāna- ... av. kā- \\\"verlangen\\\" (kaya 1. Sg., kāta-, cakuše); -mo-Stem ai. kāma- m. \\\"Lust, Wunsch, Liebe\\\", av. ap. kāma- m. \\\"Verlangen, Wunsch\\\"; ro-St.: lat. cārus \\\"lieb, wert, teuer\\\"; got. hors (*hōra-) \\\"Ehebrecher, Hurer\\\" ... ahd. huora \\\"Hure\\\", ags. hōre'. Exactly the root, gloss and the four branches Nourai draws.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Band I p. 325 (WLD_Bd1_pages.txt leaf 334)\",\n          \"stance\": \"supports\",\n          \"note\": \"'qā- \\\"gern haben, begehren\\\". ... av. kā- \\\"wonach verlangen\\\" (kayō 1 sg., kāta-, cakuše, Bartholomae Airan. Wb. 462); -mo-St. ai. kāma- m. \\\"Begehren, Wunsch, Liebe\\\", av. ap. kāma- m. \\\"Verlangen, Wunsch\\\" ... ro-St. lat. cārus \\\"lieb, wert, teuer\\\" ... got. hors \\\"Ehebrecher, Hurer\\\"'. This is the source of Nourai's second spelling 'Qâ'.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, s.v. kā- (AHD_watkins1985.txt line 560)\",\n          \"stance\": \"supports\",\n          \"note\": \"'kā-. To like, desire. Contracted from *kaa-. 1. Suffixed form *kā-ro- in: a. Germanic *hōraz (feminine *hōrōn-), \\\"one who desires,\\\" adulterer, in Old English hōre, whore: WHORE ... b. Latin cārus, dear: CARESS, CHARITY, CHERISH. 2. Suffixed form *kā-mo- in Sanskrit kāmaḥ, love, desire: KAMA. [Pok. kā- 515.]' — Nourai's nodes #7–#10 reproduce this entry item for item.\"\n        },\n        {\n          \"src\": \"KLN\",\n          \"where\": \"1966 ed. p. 268 s.v. charity (KLN_1966.txt leaf 152, printed numerals 268/269)\",\n          \"stance\": \"supports\",\n          \"note\": \"'All these words derive fr. I.-E. base *qā-, \\\"to desire\\\", whence also OI. kāmaḥ, \\\"desire\\\", kāyamānaḥ, \\\"loving\\\", Toch. B kawait, \\\"desire\\\", Lith. kamaros, \\\"lasciviousness\\\", Lett. kāmēt, \\\"to hunger\\\". Cp. caress, cherish, Kama, whore.'\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, searched for headwords kāmos / kāros / kara / 'dear'\",\n          \"stance\": \"silent\",\n          \"note\": \"grep -n '^kāmos\\\\|^kāros\\\\|^kara \\\\|hōraz' IEC.txt returns only unrelated lemmas (kamos 'muzzle' < WP I 388/507; karos (2) see kara). Mann has no entry for this root under the spellings tried.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"kâ 2, kâm 2, kâma\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan has both the verbal root kā- 'to long for, desire' (1 sg. pres. kaya, ppp. kāta-, perf. part. cakuše — Bartholomae AiW col. 462) and the -mo- noun kāma- m. 'Verlangen, Wunsch' (AiW col. 463), which Bartholomae marks 'j., g., p.' = attested in Younger Avestan, the Gāthās AND Old Persian. The Old Persian noun kāma- 'desire, will' is directly attested in the inscriptions (e.g. DNb, and the adverbial ablative-instrumental in the Darius texts), and its Old Persian shape is the base of the whole Iranian branch. Phonologically kāma- < PIE *kóh₂-mo-: the laryngeal *h₂ colours and lengthens the root vowel, and the o-grade suffix *-mo- makes an action/result noun 'the wanting'. Nourai's 'kâ 2' is the verbal root, 'kâm 2 / kâma' the noun stem with and without the thematic vowel; the numbers 2 are only his homograph counters.\",\n          \"derivation_fa\": \"در اوستایی هم ستاک فعلی kā- «خواستن، آرزو کردن» (kaya در اول‌شخص مفرد، صفت مفعولی kāta-، cakuše) هست و هم اسمِ kāma- «آرزو، خواست»؛ بارتولمه در ستون‌های ۴۶۲–۴۶۳ فرهنگ ایرانی باستان هر دو را آورده و kāma- را با نشانهٔ «j., g., p.» ثبت کرده است، یعنی در اوستای متأخر، گاهان و پارسی باستان هر سه گواه دارد. از دیدِ آواشناسی، kāma- بازماندهٔ *kóh₂-mo-ِ هندواروپایی است: حنجریِ *h₂ واکهٔ ریشه را کشیده کرده و پسوندِ *-mo- اسمِ حاصل ساخته است. «kâ ۲» در نمودار همان ستاک فعلی و «kâm ۲ / kâma» همان اسم است؛ شمارهٔ ۲ تنها برای جدا کردن هم‌نگاشت‌هاست. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/keh₂-\",\n            \"https://en.wiktionary.org/wiki/کام\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:515\",\n              \"status\": \"supports\",\n              \"note\": \"POK_02.txt leaf 174 / POK_full line 44415: 'av. kā- \\\"long, want\\\" (kaya 1. Sg., kāta-, cakuše)' and '-mo stem ... Avestan Old pers. kāma- m. \\\"desire, wish\\\"'. Exactly node #1.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Altiranisches Wörterbuch col. 462-463 (BRT.txt line 9493)\",\n              \"stance\": \"supports\",\n              \"note\": \"'j., g., p. kāma- m. \\\"Verlangen, Wunsch\\\": havāi °māua zaošāi Yt.13.29; ... yaθa mąm °ina āsta \\\"wie es mein Verlangen war\\\"'. Column 463 is exactly the reference Mo'in gives in his Borhān footnote («بارتولمه ۴۶۳»).\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian, Lexicon (KNT.txt line 5248, leaf 201 ≈ p. 186)\",\n              \"stance\": \"supports\",\n              \"note\": \"'kam- vb. \\\"like\\\" ... See also kāma-, and possibly canah-.' Kent lists OP kāma- as a lexicon headword and ties it to the verb kam-.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Band I p. 325\",\n              \"stance\": \"supports\",\n              \"note\": \"'av. kā- \\\"wonach verlangen\\\" (Bartholomae Airan. Wb. 462); -mo-St. ... av. ap. kāma- m. \\\"Verlangen, Wunsch\\\"' — same two forms, same two languages.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Sogdian\",\n          \"words\": \"k`m\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian k'm / q'm (Buddhist, Manichaean and Christian scripts) kām 'wish, desire', with the denominative verb k'm- 'to want, to wish' and the agent noun k'm'ntk kāmande 'well-wisher'. Gharib's Sogdian dictionary no. 4640 (p. 186) glosses it simply 'wish' and derives it '< OP kāma'. Strictly, Sogdian is an Eastern Iranian language and does not descend from Old Persian: it inherits *kāma- from Old/Proto-Iranian, so Nourai's arrow (drawn from his combined 'Avestan / Old Persian' box) is right as to the ancestor form but loose as to the branch. Note also that Sogdian kām grammaticalised into the future particle q'm/k'm (Gharib no. 4639), a Sogdian innovation of the 'want > future' type.\",\n          \"derivation_fa\": \"سغدی k'm (به خط‌های بودایی، مانوی و مسیحی) به معنی «آرزو، خواست» است، با فعلِ برساختهٔ k'm- «خواستن» و اسمِ فاعلِ k'm'ntk «نیک‌خواه». قریب در فرهنگ سغدی، مدخل ۴۶۴۰ (ص ۱۸۶)، آن را «wish» معنی کرده و ریشه‌اش را «< پارسی باستان kāma» نوشته است. دقیق‌تر آنکه سغدی از شاخهٔ ایرانیِ خاوری است و از پارسی باستان نمی‌آید، بلکه *kāma- را از ایرانی باستان به ارث برده است؛ پس پیکانِ نورایی از نظر صورتِ نیا درست ولی از نظر شاخه‌بندی مسامحه‌آمیز است. افزون بر این، همین kām در سغدی به ادات آینده‌ساز q'm/k'm بدل شده (مدخل ۴۶۳۹) که نمونهٔ آشنای تحول «خواستن ← آینده» است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"SOD:186\",\n              \"status\": \"supports\",\n              \"note\": \"Gharib, Sogdian Dictionary, printed p. 186 (SOD_pages.txt leaf 250), entry '4640 k'm B — kām (q'm) ©<OP kāma ©acc. -w — wish'; next to it '4641 k'm- B, M, S — kām (q'm-) — (to)want, (to)wish, (to)like' and '4639 q'm CB ... kam ... future particle'. Nourai's SOD:186 is a printed page number and it is exact.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SOD\",\n              \"where\": \"entries 4639-4645, printed p. 186\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check; Gharib also has '4643 k'm'k S kāmē, kāmak — wisher' and '4644 k'm'ntk B kāmande — well-wisher, liking'.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie p. 48 s.v. kām\",\n              \"stance\": \"supports\",\n              \"note\": \"'kām [km | = M, N ~] will, desire, purpose' — the bracket '= M' records that the Manichaean Middle Iranian (Parthian/Manichaean MP) spelling is identical, i.e. the same Old Iranian *kāma- underlies the Middle Iranian forms of which Sogdian kām is the Eastern member.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"kâm\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian kām (Book Pahlavi ⟨km⟩, Manichaean kʾm) 'will, desire, purpose', with the extended stem kāmag 'wish, will' and the verb kāmistan / kām- 'to want'. It continues Old Persian / Old Iranian kāma- unchanged apart from the loss of the Old Iranian thematic ending -a: OIr. *kāma- > MP kām, the final short -a being dropped in the Middle Iranian apocope. Nyberg's glossary documents the whole family in real texts (Mēnōg ī Xrad, Kārnāmag): kāmak 'will, wish, desire (= kām)', kāmakīh, and the compound kām-kār [kʾmkʾl] 'acting according to his own will, sovereign', with Manichaean Parthian kʾmgʾr. MacKenzie also gives kām-widār 'successful, independent'.\",\n          \"derivation_fa\": \"فارسی میانه (پهلوی) kām، به خط پهلویِ کتابی ⟨km⟩ و به خط مانوی kʾm، به معنی «خواست، آرزو، قصد»، همراه با ستاکِ گستردهٔ kāmag و فعلِ kāmistan / kām- «خواستن». این صورت دنبالهٔ بی‌واسطهٔ kāma-ِ ایرانی باستان است و تنها دگرگونی آوایی آن افتادنِ واکهٔ پایانی است: *kāma- ← kām، همان فرسایشِ پایانه‌ها که مشخصهٔ گذار از ایرانی باستان به میانه است. نیبرگ در واژه‌نامهٔ خود (ص ۱۱۵–۱۱۶) kāmak «خواست، آرزو (= kām)» و ترکیبِ kām-kār «به کامِ خود رفتار کننده، خودکامه/کامکار» را با گواهِ متنی آورده و پارتیِ مانوی kʾmgʾr را نیز یاد کرده است؛ مکنزی (ص ۴۸) kām و kāmag و kām-widār را ثبت کرده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/کام\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1578\",\n              \"status\": \"partial\",\n              \"note\": \"Borhān-e Qāṭeʿ ed. Moʿin, printed p. 1578 (BQT_v3 pdf p. 371; page image and transcript saved at data/verification/sources/refs/ocr/BQT/1578.png and 1578.vision.txt). The headword کام is there ('و بمعنی مراد و مقصد هم آمده است ۹') and Moʿin's footnote 9 reads 'اوستا و پارسی باستان ـ kâma (میل، آرزو) «بارتولمه ۴۶۳»، ... kâm، kâmak «نیبرگ ۱۱۸» ... و رک: هرن/هوبشمان ۸۳۸'. So the footnote does cite Nyberg for the kām/kāmak forms, but it labels the etymon 'Avestan and Old Persian', never spelling out a separate Pahlavi stage; it supports the form but not explicitly the label 'Pahlavi'.\"\n            },\n            {\n              \"ref\": \"SNS:209\",\n              \"status\": \"not_found\",\n              \"note\": \"Tavoosi's Shāyast nē Shāyast glossary: grep for 'kām', 'kam ', and Persian 'کام' in SNS_pages.txt / SNS.txt returns nothing usable — the OCR of this volume carries almost no Persian and the Latin transliterations are badly mangled (242 leaves, printed page offset undetermined). Could not confirm p. 209.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, Concise Pahlavi Dictionary p. 48 (PHD.txt leaf 69)\",\n              \"stance\": \"supports\",\n              \"note\": \"'kām [km | = M, N ~] will, desire, purpose. kām-, v. kāmistan. ²kāmag [kʾmk' | N kāma] = kām. ~-hanjām gaining one's end, successful. ~-widār [-wtʾl | N kām-gučār] successful, independent.' Note MacKenzie carefully separates 'kam [km | M kmb, N ~] little, small, few'.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II (Glossary) pp. 115-116\",\n              \"stance\": \"supports\",\n              \"note\": \"'kāmak 1. will, wish, desire (= kām): ō ~ rasēt (imp.) may you attain ... the will of the gods 69'; and 'kām-kār [kʾmkʾl] acting according to his own will, sovereign, autocrat: pat Ērānšahr ~ 1376 ... — MPrth kʾmgʾr \\\"free, happy\\\" (A-H III)'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"kâm 1 «کام ۱»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian کام kām 'desire, wish, will; success' continues Middle Persian kām without change (MP kām > NP kām; the parallel MP kāmag survives as کامه kāma). The two words printed in the box as script_extra are its classical compounds: کامیاب kām-yāb 'one who finds his desire, successful' (kām + yāb, present stem of یافتن yāftan 'to find') and کامکار kām-kār 'one who works his own will, fortunate, sovereign', the direct continuation of Pahlavi kām-kār [kʾmkʾl] with the Parthian doublet kʾmgʾr, whence also the variant کامگار kām-gār. Horn no. 838 sets out the whole line: 'kām \\\"Wunsch, Wille\\\", kāme; ap. aw. kāma- \\\"Wunsch, Wille\\\"; phlv. kāmak, kāmakīh, kāmītan, kām(i)stan (Mēn.) ... ai. kāma-, oss. kom \\\"Wille\\\"'. The homograph کام 'palate' (Nourai's numbering 'kâm 1' vs the other کام) is a different word: Hübschmann, commenting on Horn 838, states it is 'schwerlich identisch' with kām 'Wunsch, Wille', because the Germanic words for 'palate' presuppose IE *gh- and the Iranian ones *k-.\",\n          \"derivation_fa\": \"«کام» در فارسی نو به معنی «آرزو، خواست، مراد؛ کامیابی» دنبالهٔ بی‌تغییرِ kāمِ فارسی میانه است (فارسی میانه kām ← فارسی نو کام؛ صورتِ گستردهٔ kāmag نیز به «کامه» رسیده است). دو واژهٔ کنارِ مدخل در نمودار، ترکیب‌های کلاسیکِ همین واژه‌اند: «کامیاب» (کام + یاب، ستاکِ حالِ یافتن) و «کامکار» که خود دنبالهٔ مستقیمِ kām-kārِ پهلوی [kʾmkʾl] است و همتای پارتیِ مانویِ آن kʾmgʾr صورتِ «کامگار» را توضیح می‌دهد. هرن در مدخل ۸۳۸ (ص ۱۸۶) همین زنجیره را آورده است: «kām، کامه؛ پارسی باستان و اوستایی kāma-؛ پهلوی kāmak، kāmakīh، kāmistan؛ سنسکریت kāma-؛ آسی kom». نکتهٔ لازم آنکه «کام» به معنی «سقفِ دهان» واژه‌ای دیگر است؛ هوبشمان در حاشیهٔ بر شمارهٔ ۸۳۸ هرن (پرسیشه اشتودین ص ۸۶) صریحاً می‌گوید این دو «به‌دشواری یکی‌اند»، زیرا واژه‌های ژرمنی برای «کام دهان» گویای gh هندواروپایی و صورت‌های ایرانی گویای k هستند. شمارهٔ «۱» در نمودار نورایی همین جدا کردنِ دو هم‌نگاشت است و کارِ درستی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/کام\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1578\",\n              \"status\": \"supports\",\n              \"note\": \"Borhān-e Qāṭeʿ p. 1578 (image + transcript saved under refs/ocr/BQT/1578): headword 'کام ـ بسکون میم، سقف دهان را گویند ... و بمعنی مراد و مقصد هم آمده است ۹', with Moʿin's footnote 9 'اوستا و پارسی باستان ـ kâma (میل، آرزو) «بارتولمه ۴۶۳» ... و رک: هوبشمان ۸۳۸' plus the Moʿezzi verse 'آنجا که هست کامش، با کام اوست دولت'. Exactly Nourai's Persian node, including the 'desire' sense. The page does NOT contain کامیاب / کامکار (they are elsewhere in the dictionary), and the verse Nourai prints (Asadi, 'به یزدان چنین دارم امید و کام') is not the one on this page.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 838, p. 186 (HRN.txt leaf 207)\",\n              \"stance\": \"supports\",\n              \"note\": \"'838. kām \\\"Wunsch, Wille\\\", kāme. ap. aw. kāma- \\\"Wunsch, Wille\\\"; phlv. kāmak, kāmakīh, kāmītan, kām(i)stan (Mēn.), vielleicht arm. LW. kam-k \\\"Wille, Wunsch\\\", kamim \\\"wollen, wünschen\\\" (Hübschmann No. 140); ai. kāma-, oss. kom \\\"Wille\\\" (161).'\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien pp. 86-87, note on Horn 838 (HUB.txt line 3052)\",\n              \"stance\": \"partial\",\n              \"note\": \"'838. Np. kām = afgh. kumai \\\"Gaumen\\\" ist schwerlich identisch mit kām \\\"Wunsch, Wille\\\". Die germ. Wörter für \\\"Gaumen\\\" setzen im Anlaut ein idg. gh, die iranischen ein idg. k voraus.' Supports the 'desire' word by keeping it apart from the homograph 'palate' — which is why Nourai's 'kâm 1' numbering is correct.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Moʿin, Farhang-e Fārsi, s.vv. کامکار, کامیاب (MON_part2.txt lines 19487, 19561)\",\n              \"stance\": \"supports\",\n              \"note\": \"'کامکار: [= کامگار] (ص فا.) کامروا، کامران، سعید، سعادتمند، خوشبخت، موفق' and 'کامیاب: (ص مر.) کامروا، ... مق. ناکام، موفق، فیروزمند'. Both are native Persian compounds of کام, marked as such (no [ع.] Arabic tag), confirming Nourai's script_extra.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, searched ARY_pages.txt and ARY_latin_index_pages.txt for کام / KAM / DESIRE\",\n              \"stance\": \"silent\",\n              \"note\": \"No headword for کام found; the only hits for the string کام are the ordinary word کاملاً etc. in the introduction. Aryanpur does not treat this word.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"čanah, činah, činman ; aspa-canah\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The forms themselves are all real. Avestan canah- / cinah- n. 'desire, demand' is attested only in compounds (Bartholomae: θaētō.cinah- 'Geld heischend', V. 4.44; xšaθrō.cinah-, Yt. 13.111) and Avestan cinman- n. 'Begehren, Trachten'; Old Persian canah- is known from the Median-shaped personal name Aspačanā (stem Aspačanah-), Darius's bow-bearer, Elam. aš-ba-za-na, Akk. as-pa-[si-na], Greek Ἀσπαθίνης — Kent glosses it 'Lover of Horses', aspa- 'horse' + canah- 'desire', comparing Skt. cánas- 'pleasure'. What is only PLAUSIBLE is the arrow: attaching canah-/cinah- to the root *keh₂- requires an Indo-Iranian by-form kan-/can- 'to be satisfied, take pleasure' (Skt. perf. cakána, aor. ákaniṣam, Av. cakana; Skt. cánas- n.) and Pokorny himself proposes it only as a question — 'Beruht ar. kan-, can- ... auf einem idg. -(e)nes-St. k-e-nes-?' — and adds that cani-/kani- may just as well be secondary. Kent is equally guarded: 'kam- vb. \\\"like\\\" ... See also kāma-, and possibly canah-'. Modern handbooks generally keep PIIr. *kan- 'to be pleased' as an independent root, so the edge is defensible but not established. The chart's 'aspa-canah' is Nourai's normalisation; the attested Old Persian nominative is Aspačanā.\",\n          \"derivation_fa\": \"صورت‌های این گره همه واقعی‌اند: اوستایی canah-/cinah- «آرزو، طلب» تنها در ترکیب‌ها گواه دارد (بارتولمه: θaētō.cinah- «پول‌خواه» وندیداد ۴٫۴۴، و xšaθrō.cinah- یشت ۱۳٫۱۱۱) و cinman- «خواستن، در پیِ چیزی بودن»؛ پارسی باستانِ canah- نیز از نامِ خاصِ Aspačanā (ستاک Aspačanah-)، کمان‌دارِ داریوش، شناخته می‌شود که در ایلامی aš-ba-za-na و در یونانی Ἀσπαθίνης آمده است و کنت آن را «دوستدارِ اسب» معنی کرده است: aspa- «اسب» + canah- «آرزو». آنچه تنها «با احتیاط پذیرفتنی» است خودِ پیکان است: بستنِ canah-/cinah- به ریشهٔ *keh₂- نیازمندِ فرضِ گونه‌ای هندوایرانی kan-/can- «خشنود شدن» است و خودِ پوکورنی این پیوند را با علامت پرسش آورده («آیا بر ستاکِ هندواروپایی k-e-nes- استوار است؟») و افزوده که cani-/kani- می‌تواند ثانوی باشد؛ کنت نیز محتاطانه می‌نویسد «و شاید canah-». پژوهش امروزی *kan- را معمولاً ریشه‌ای مستقل می‌داند. نگارشِ «aspa-canah» هم صورتِ هنجارشدهٔ نورایی است؛ صورتِ گواه‌دارِ پارسی باستان Aspačanā است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:515\",\n              \"status\": \"partial\",\n              \"note\": \"POK_02.txt leaf 174 / POK_full line 44444: 'Beruht ar. kan- (ai. Perf. cākana, Aor. ákāniṣam, av. cakana), can- (ai. cániṣṭam; ai. cánas- n. \\\"Gefallen, Befriedigung\\\", av. canah-, cinah- \\\"Verlangen, Heischen\\\") \\\"befriedigt sein, Gefallen finden\\\", av. cinman- n. \\\"Begehren, Trachten\\\" auf einem idg. -(e)nes-St. k-e-nes-?' — the forms are all on p. 515 under kā-, but Pokorny marks the connection with a question mark, so this is support for the forms and only a hesitant support for the arrow.\"\n            },\n            {\n              \"ref\": \"KNT:173\",\n              \"status\": \"partial\",\n              \"note\": \"Kent's Lexicon entries were located at KNT.txt lines 5121 (Aspacanah-), 5248 (kam-) and 5378 (canah-), i.e. leaves 195/201/206 ≈ printed pp. 180-193, not p. 173; p. 173 in Kent's lexicon is the 'ada-/adam' stretch. Content-wise Kent says exactly what Nourai's box says: 'Aspacanah- sb. \\\"Aspathines\\\", bow-bearer of Darius: Elam. aš-ba-za-na, Akk. as-pa-[si-na], Gk. Ἀσπαθίνης; aspa- \\\"horse\\\" + canah- \\\"desire\\\", Av. -cinah-, Skt. cánas-; \\\"Lover of Horses\\\"' and 'canah- sb. \\\"desire\\\", see Aspacanah-; cf. also kam-'. Support for the content, but the page number does not match the 1950/53 edition I checked.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"AiW: θaētō.cinah- (BRT.txt line 28359), xšaθrō.cinah- col. 547 (line 10765), cinman- (line 24407)\",\n              \"stance\": \"supports\",\n              \"note\": \"'j. θaētō.cinah- Adj. \\\"Geld heischend\\\": yezi ... jasąn ... \\\"wenn sie Geld heischend kommen, soll man Geld (für sie) zusammenbringen\\\" V. 4.44' and 'j. xšaθrō.cinah- m. EN. eines Gläubigen ... Yt. 13.111'. Bartholomae has the forms but as bahuvrīhi second members only, never a free noun canah-.\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian §161, §168 and Lexicon s.v. Aspacanah-\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check; also KNT.txt line 1913 'a. Accusative: Aspa-canah- \\\"Having love of horses\\\"' and line 1860 listing 'can-ah-' among the -ah- stems.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Band I p. 325-326 (WP I 325 f., the reference Pokorny gives)\",\n              \"stance\": \"partial\",\n              \"note\": \"The qā- article runs from p. 325; the ar. kan-/can- discussion that Pokorny reprints with a question mark is Walde-Pokorny's own, i.e. the doubt is a century old and has not been resolved in Nourai's favour.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": null,\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"There is nothing to verify: on the printed page (PDF p. 231 = book p. 201, image saved at data/verification/sources/refs/ocr/BOOK/231.png) the box to the right of the 'čanah, činah, činman' box is drawn EMPTY — no language label, no reference, no word, only the rectangle and the connecting arrow. The extraction is therefore faithful (JSON: lang null, refs null, words []); the blank is an artefact of Nourai's own chart layout, presumably a derivative he intended to add (an English or Persian reflex of canah-) and never filled in. No error to report against the data.\",\n          \"derivation_fa\": \"چیزی برای راستی‌آزمایی نیست: در صفحهٔ چاپی (صفحهٔ ۲۳۱ پی‌دی‌اف = صفحهٔ ۲۰۱ کتاب) کادرِ سمتِ راستِ جعبهٔ «čanah, činah, činman» کاملاً خالی چاپ شده است — نه برچسبِ زبان دارد، نه ارجاع و نه واژه‌ای؛ تنها یک مستطیل و پیکانِ اتصال. پس خوانشِ داده‌ها درست بوده و این خلأ خطای اسکن یا استخراج نیست، بلکه خطای صفحه‌آراییِ خودِ کتاب است؛ ظاهراً نویسنده جای مشتقی را باز گذاشته و آن را پر نکرده است. تصویرِ صفحه برای بازبینی در refs/ocr/BOOK/231.png نگهداری شد.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference in the book — the box is blank on the printed page.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BOOK\",\n              \"where\": \"printed page 201 (PDF 231), image at data/verification/sources/refs/ocr/BOOK/231.png\",\n              \"stance\": \"silent\",\n              \"note\": \"Read the page render at 200 dpi: the fourth box on the right-hand column of the 'Kâ 1' chart is an empty rectangle with no text of any kind.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Germanic\",\n          \"words\": \"hôraz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *hōraz m. 'adulterer' (feminine *hōrǭ / *hōrōn- 'adulteress, prostitute') < PIE *kéh₂-ro- 'dear, beloved', the same *-ro- derivative that gives Latin cārus; the Germanic sound change is Grimm's Law, PIE *k > PGmc *h, while *eh₂ > ā > Gmc ō. The masculine is directly attested as Gothic hōrs 'μοιχός, adulterer' (Luke 18:11) and Old Norse hórr; the feminine as ON hóra, OE hōre, OHG huora, MHG huore, G. Hure. Watkins glosses *hōraz exactly as Nourai does, 'one who desires', which is a gloss of the root rather than of the attested Germanic meaning ('adulterer').\",\n          \"derivation_fa\": \"ژرمنیِ آغازین *hōraz «زناکار (مرد)» و مؤنثِ آن *hōrǭ «زنِ زناکار، روسپی»، از *kéh₂-ro-ِ هندواروپایی به معنی «عزیز، دوست‌داشتنی» — همان ساختِ پسوندیِ *-ro- که در لاتینی cārus را داده است. دگرگونی آوایی همان قانون گریم است: k هندواروپایی در ژرمنی به h بدل شده، و *eh₂ نخست به ā و سپس در ژرمنی به ō رسیده است. صورتِ مذکر در گوتیک hōrs «زناکار» (لوقا ۱۸:۱۱) و نورس باستان hórr گواه دارد، و صورتِ مؤنث در hóra نورسی، hōreٔ انگلیسی باستان، huora در آلمانی علیای باستان و Hureٔ آلمانی امروز. معنایی که نورایی داده («کسی که می‌خواهد») همان معنیِ ریشه است، نه معنیِ گواه‌دارِ ژرمنی که «زناکار» است؛ این را از واتکینز گرفته است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/whore\",\n            \"https://www.etymonline.com/word/whore\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:1743\",\n              \"status\": \"supports\",\n              \"note\": \"The 1966 two-volume scan on disk stops at about p. 1700 (last numbered leaf 899 = p. 1696), so p. 1743 itself could not be read; the same entry in Klein's 1971 one-volume edition (KLN_1971.txt line 266963) reads 'whore, n., a prostitute. — ME. hore, fr. OE. hore, fr. ON. hora, \\\"adulteress\\\" ... rel. to ON. horr, \\\"adulterer\\\", and to MDu. hoere, Du. hoer, OHG. huora, MHG. huore, G. Hure, \\\"whore\\\", Goth. hors, \\\"adulterer\\\", from I.-E. base *qā-, \\\"to desire\\\", whence also L. cārus, \\\"dear, precious\\\". See charity ... The w in whore is intrusive.' Content confirmed; the page number falls in the right stretch of vol. II (whore is near the end of the W section, pp. 1740-50).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. kā-\",\n              \"stance\": \"supports\",\n              \"note\": \"'Suffixed form *kā-ro- in: a. Germanic *hōraz (feminine *hōrōn-), \\\"one who desires,\\\" adulterer, in (i) Old English hōre, whore: WHORE' — the source of Nourai's gloss word for word.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etym. Dict., s.v. Whore, p. 568 (SKT.txt leaf 588)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Whore, sb. (Scand.) The w is unoriginal. M.E. hore. — Icel. hora, an adulteress, fem. of hórr, an adulterer; Dan. hore, Swed. hora. + Du. hoer, G. hure, O.H.G. huora; Goth. hors, masc. an adulterer. ... Prob. also to L. carus, loving, Skt. kāmagā ... (from kam, to love).'\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW p. 515\",\n              \"stance\": \"supports\",\n              \"note\": \"'got. hors (*hōra-) \\\"Ehebrecher, Hurer\\\", aisl. hōrr ds., ags. hōr n. ds., ahd. huor n. ds., ahd. huora (und huorra aus *hōriōn-) \\\"Hure\\\", ags. hōre, aisl. hōra- (*hōrōn-) ds.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"whore\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English hōre 'prostitute' (the feminine *hōrǭ, not the masculine *hōraz, is the immediate etymon), reinforced in Middle English by Old Norse hóra; ME hore > Modern English whore. The initial ⟨wh⟩ is unetymological: it appears only from the 16th century, by analogy with the many genuine wh- words and with the same hypercorrect spelling seen in whole (OE hāl) — Klein: 'The w in whore is intrusive; cp. whole'. Semantically the shift is 'the desired/beloved one' > 'adulteress' > 'prostitute', a pejoration already complete in Germanic.\",\n          \"derivation_fa\": \"انگلیسی باستان hōre «روسپی» — دقیق‌تر آنکه نیای بی‌واسطهٔ آن صورتِ مؤنثِ ژرمنی *hōrǭ است، نه مذکرِ *hōraz — که در انگلیسی میانه با hóraٔ نورس باستان تقویت شده و از hore انگلیسی میانه به whore امروزی رسیده است. ⟨wh⟩ آغازین ریشه‌شناختی نیست و تنها از سدهٔ شانزدهم پیدا می‌شود؛ نوعی تصحیحِ افراطیِ املایی به قیاسِ واژه‌های اصیلِ wh-دار، درست مانند whole که از hālِ انگلیسی باستان است (کلاین: «w در whore زائد است؛ قس whole»). از نظر معنایی زنجیرهٔ «خواستنی/محبوب ← زناکار ← روسپی» است که تحقیرِ معناییِ آن پیش از انگلیسی و در دورهٔ ژرمنی انجام گرفته بود. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/whore\",\n            \"https://www.etymonline.com/word/whore\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai gives no reference on this node; it inherits KLN:1743 from its parent, which is checked there.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"1971 ed. s.v. whore (KLN_1971.txt line 266963)\",\n              \"stance\": \"supports\",\n              \"note\": \"'whore, n., a prostitute. — ME. hore, fr. OE. hore, fr. ON. hora, \\\"adulteress\\\" ... from I.-E. base *qā-, \\\"to desire\\\", whence also L. cārus ... The w in whore is intrusive; cp. whole.'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat p. 568\",\n              \"stance\": \"supports\",\n              \"note\": \"'Whore, sb. (Scand.) The w is unoriginal. M.E. hore. — Icel. hora ... ¶ Certainly not allied to hire!'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. kā-, and Etymonline s.v. whore\",\n              \"stance\": \"supports\",\n              \"note\": \"Watkins: 'Old English hōre, whore: WHORE'. Etymonline: 'It is considered to be, probably, etymologically, \\\"one who desires\\\", from PIE root *ka- \\\"to like, desire\\\".'\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Latin\",\n          \"words\": \"carus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin cārus, -a, -um < Proto-Italic *kāros < PIE *kéh₂-ro- 'dear, beloved', the exact formal counterpart of Germanic *hōraz and of Latvian kārs 'greedy, lustful'; the same *-ro- adjective is seen in Celtic with zero grade (OIr. carae 'friend', caraim 'I love', W. caraf 'I love'). Ernout-Meillet: 'L'adjectif cārus a un correspondant dans got. hors \\\"πόρνος, μοιχός\\\", v.h.a. huora \\\"fille publique\\\", et dans l'adjectif lette kārs \\\"friand, plein de désirs\\\"'. One correction to the chart: Nourai glosses cārus 'desire', but the Latin word is an adjective meaning 'dear, beloved; costly, of high price' — 'desire' is the meaning of the root, not of the Latin word. The route and the root are right.\",\n          \"derivation_fa\": \"لاتینی cārus «عزیز، گرامی؛ گران‌بها» از ایتالیکِ آغازین *kāros و آن از *kéh₂-ro-ِ هندواروپایی «دوست‌داشتنی» است؛ همتای صوریِ دقیقِ *hōrazِ ژرمنی و kārsِ لتونیایی «آزمند، پرآرزو». همین صفتِ *-ro- در سلتی با درجهٔ صفرِ واکه دیده می‌شود: ایرلندی باستان carae «دوست»، caraim «دوست می‌دارم». ارنو و مِیه در فرهنگ ریشه‌شناختی لاتین (ص ۱۸۳) می‌نویسند: «صفتِ cārus همتایی دارد در گوتیکِ hors و در huoraٔ آلمانی علیای باستان و در صفتِ لتونیاییِ kārs». یک اصلاح بر نمودار: نورایی معنیِ cārus را «آرزو» نوشته، حال آنکه این واژه صفت است و «عزیز، گرامی» معنی می‌دهد؛ «آرزو» معنیِ ریشه است نه معنیِ واژهٔ لاتینی. مسیر و ریشه درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:515\",\n              \"status\": \"supports\",\n              \"note\": \"POK_02.txt leaf 174: 'ro-St.: lat. cārus \\\"lieb, wert, teuer (auch vom Preise)\\\"; got. hors (*hōra-) \\\"Ehebrecher, Hurer\\\" ... lett. kārs \\\"lüstern, begehrlich\\\" (kāruot \\\"begehren, verlangen\\\")'. Note that Pokorny's own gloss is 'lieb, wert, teuer', not 'desire'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout-Meillet, Dict. étym. de la langue latine p. 183 s.v. cārus (LAT.txt line 10140)\",\n              \"stance\": \"supports\",\n              \"note\": \"'cārus, -a, -um: cher (qu'on chérit); et \\\"cher, de haut prix\\\" ... L'adjectif cārus a un correspondant dans got. hors ..., v.h.a. huora \\\"fille publique\\\", et dans l'adjectif lette kārs \\\"friand, plein de désirs\\\". Le celtique a, en regard, des dérivés à vocalisme zéro: irl. carae et gall. car \\\"ami\\\", irl. caraim \\\"j'aime\\\".'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"1966 ed. p. 268 s.v. charity\",\n              \"stance\": \"supports\",\n              \"note\": \"'L. cāritātem, acc. of cāritas, \\\"dearness, affection, love\\\", fr. cārus, \\\"dear, precious, esteemed, loved\\\", which is cogn. with OIr. carae \\\"friend\\\" ... ON. hora, OE. hore, \\\"whore\\\". All these words derive fr. I.-E. base *qā-, \\\"to desire\\\".'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. kā-\",\n              \"stance\": \"supports\",\n              \"note\": \"'b. Latin cārus, dear: CARESS, CHARITY, CHERISH.' Again 'dear', not 'desire'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"caress, charity, cherish\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are Romance descendants of Latin cārus that reached English through French. (1) charity: L. cāritātem, acc. of cāritās 'dearness, affection' > Old French charité > Middle English charite; the specifically Christian sense comes from the Vulgate, where cāritās renders Greek ἀγάπη (Ernout-Meillet: 'dans la langue de l'Église a servi à traduire le gr. ἀγάπη'). (2) cherish: OF cherir, present-participle stem cheriss- (mod. F. chérir 'to hold dear'), from cher < cārus, borrowed as ME cherischen with the English -ish of the French inchoative stem. (3) caress: 17th-c. French caresse/caresser, from Italian carezza / carezzare 'to fondle', from caro < cārus — the newest of the three and the only one with an Italian relay. Watkins lists exactly these three words (CARESS, CHARITY, CHERISH) under Latin cārus.\",\n          \"derivation_fa\": \"هر سه واژه بازماندگانِ رومانسِ cārusِ لاتینی‌اند که از راهِ فرانسه به انگلیسی رسیده‌اند. یک) charity از cāritātem (حالت مفعولیِ cāritās «عزیز داشتن، مهر») به فرانسهٔ باستان charité و از آن به انگلیسی میانه charite؛ معنای ویژهٔ مسیحیِ آن از ترجمهٔ لاتینیِ کتاب مقدس (ولگاتا) می‌آید که در آن cāritās برابرِ ἀγάπηٔ یونانی نهاده شده است. دو) cherish از ستاکِ اسم‌فاعلیِ cheriss- در فعلِ chérir فرانسه («عزیز داشتن») که خود از cher < cārus است؛ انگلیسی آن را با پسوندِ -ish گرفته است. سه) caress جوان‌ترینِ این سه و تنها واژه‌ای است که واسطهٔ ایتالیایی دارد: از caresse/caresser فرانسه، از carezza/carezzare ایتالیایی «نوازش کردن»، از caro < cārus. واتکینز در فرهنگ ریشه‌های هندواروپاییِ AHD دقیقاً همین سه واژه را ذیل cārus آورده است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai gives no reference on this node; it inherits POK:515 from the Latin parent, checked there. AHD's kā- article supplies the same three English words.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"1971 ed. s.vv. caress, cherish, charity (KLN_1971.txt lines 39793, 44875; 1966 ed. p. 268 for charity)\",\n              \"stance\": \"supports\",\n              \"note\": \"'caress, tr. v. — F. caresser, fr. It. carezzare, lit. \\\"to cherish\\\", fr. caro, \\\"dear\\\", fr. L. cārus'; 'cherish, tr. v. — ME. cherischen, fr. OF. cheriss-, pres. part. stem of cherir (F. chérir), \\\"to hold dear, cherish\\\", fr. cher, \\\"dear\\\", fr. L. cārus'; 'charity, n. — F. charité, fr. L. cāritātem ... fr. cārus'.\"\n            },\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout-Meillet p. 183\",\n              \"stance\": \"supports\",\n              \"note\": \"'Dérivés: cāritās: tendresse, affection, amour ... et \\\"cherté\\\". Dans la langue de l'Église a servi à traduire le gr. ἀγάπη, et a été pris quelquefois dans l'acception spéciale de \\\"charité\\\"; M.L.1695.'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat p. 79 s.v. Cherish (SKT.txt line 3358)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Cherish; see Caress.' — Skeat likewise groups cherish with caress under the cārus family.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"K.a`.b\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Arabic root ك ع ب k-ʿ-b; kaʿb 'ankle bone, knuckle-bone, node, protuberance', hence 'die, cube'\",\n      \"note\": \"The root is genuine Arabic and Semitic: verb kaʿaba 'to be swelling, full and round', noun kaʿb 'ankle, anklebone, joint, knob, node' (the Qurʾānic sense, 5:6), from which the geometrical 'cube, die' is a secondary, mathematicians' extension, and the II-stem kaʿʿaba 'to cube'. So the root box's gloss 'cube' is the narrowest and latest of the meanings rather than the basic one. Jeffery's Foreign Vocabulary of the Qurʾān has no entry for kaʿb / kaʿba, i.e. he treats it as native Arabic — which is right and which also means it is not a Persian loan. What is NOT sound is the shape of the tree hung under the root: node #3 makes Greek kubos a descendant of this Arabic root, and that is rejected by modern scholarship (see that node). Nodes #1 (Persian) and #2 (English Kaaba) are correct.\",\n      \"note_fa\": \"ریشهٔ ك ع ب عربیِ اصیل است: فعلِ کَعَبَ «برآمده و گِرد شدن»، اسمِ کَعب «قوزکِ پا، بندِ استخوان، گره، برآمدگی» (همان معنی که در قرآن ۵:۶ آمده) و از آن، در زبانِ ریاضی‌دانان، معنیِ ثانویِ «مکعب، تاس»، و بابِ دومِ کَعَّبَ «به توان سه رساندن». پس معنایی که نورایی برای ریشه نوشته («مکعب») تنگ‌ترین و متأخرترین معنی است، نه معنیِ پایه. جفری در «واژه‌های دخیل در قرآن» مدخلی برای کعب ندارد، یعنی آن را واژه‌ای عربیِ بومی می‌شمارد؛ این نکته هم درست است و هم نشان می‌دهد که واژه وام‌واژهٔ فارسی نیست. آنچه پذیرفتنی نیست ساختِ درختِ زیرِ این ریشه است: گرهٔ ۳ یونانیِ kubos را فرزندِ این ریشهٔ عربی می‌داند و پژوهش امروزی آن را رد می‌کند. گره‌های ۱ (فارسی) و ۲ (Kaaba انگلیسی) درست‌اند.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/كعب\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"FVA:353\",\n          \"status\": \"not_checked\",\n          \"note\": \"S.M. Nahvi, Farhang-e Vāžehā-ye ʿArabi dar Fārsi — refs_online.json records that no digital copy exists (archive.org, ketabnak, noorlib and general web all searched); local_file is null. Cannot be checked.\"\n        },\n        {\n          \"ref\": \"KLN:380\",\n          \"status\": \"supports\",\n          \"note\": \"Klein 1966 p. 380 (KLN_1966.txt leaf 210, which carries the printed numeral 380), s.v. cube: 'cube, n. — F., fr. L. cubus, fr. Gk. κύβος, \\\"cube, cubical die\\\", prob. of Sem. origin. Cp. Arab. kaʿb, \\\"cube\\\", and see Kaaba. The u in Gk. κύβος is equivalent to Sem. ayin ... See W. Muss-Arnolt in Transactions of the American Philological Association, p. 147.' The page number is exact and Klein says precisely what Nourai's chart says — but Klein is reproducing Muss-Arnolt 1892, a view now abandoned.\"\n        },\n        {\n          \"ref\": \"PHN:131\",\n          \"status\": \"partial\",\n          \"note\": \"Pihan 1866 pp. 131-132 (PHN.txt leaf 163-164), s.v. CUBE: '[kaʿb] dé à jouer, cube, solide à six faces carrées égales; hexaèdre, terme d'architecture. — Remarquez l'analogie qui existe entre le mot arabe et le grec κύβος, le latin cubus, et l'italien cubo ... De [kaʿb], augmenté de la terminaison féminine ة, vient [Kaʿbat], nom du temple de la Mekke.' Pihan's book is about French words FROM Arabic, and for the Greek he claims only an 'analogie', not a derivation.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"KLN\",\n          \"where\": \"1966 ed. p. 838 s.v. Kaaba (KLN_1966.txt leaf 452, printed numeral 838)\",\n          \"stance\": \"supports\",\n          \"note\": \"'Kaaba, n., the cube-shaped building in the Great Mosque of Mecca containing the Black Stone of Mecca. — Arab. kaʿbah, \\\"square house\\\", fr. kaʿb, \\\"cube\\\". Cp. cube.'\"\n        },\n        {\n          \"src\": \"FVQ\",\n          \"where\": \"Jeffery, Foreign Vocabulary of the Qurʾān — grep for kaʿb / kaʿba in FVQ_pages.txt\",\n          \"stance\": \"silent\",\n          \"note\": \"The only hits are the personal names Kaʿb b. al-Ashraf and Kaʿb al-Aḥbār and passing mentions of 'the Kaʿba' as a building (lines 513, 1421, 7657); there is no lexical entry, i.e. Jeffery does not regard kaʿb/kaʿba as a foreign word in Arabic.\"\n        },\n        {\n          \"src\": \"AFM\",\n          \"where\": \"Addi Shir, al-Alfāẓ al-Fārisiyya al-Muʿarraba — grep 'كعب' in AFM_pages.txt\",\n          \"stance\": \"silent\",\n          \"note\": \"Single incidental hit ('ما بين الكعبين' inside another entry, line 3808); no headword كعب. Addi Shir does not list it among the Persian words arabicised, confirming it is native Arabic.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"ka`b «کَعب»; Ka`beh «کعبه»; moka`ab «مکعب»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are straightforward Arabic loans in Persian, taken over with the Arabic consonantism intact (including the ʿayn, which Persian speakers realise as a glottal stop or as compensatory length). کعب kaʿb = Ar. kaʿb 'anklebone, knuckle-bone', and in the mathematical language of the Islamic algebraists also 'cube' and hence 'cube root' (Moʿin: '(ریاضی) عددی که دو بار در نفس خود ضرب شود ... را مکعب گویند'). کعبه Kaʿbe = Ar. al-Kaʿba, the feminine kaʿba(t) 'the cubical (house)', with the Arabic tāʾ marbūṭa rendered in Persian as final -e/-a; the figurative Persian sense 'centre point, the goal one turns to' (کعبهٔ جان, کعبهٔ مقصود) is a native Persian poetic development. مکعب mokaʿʿab = Ar. mukaʿʿab, the passive participle of the II-stem kaʿʿaba 'to cube', hence 'cubed, cubic, a cube'. Moʿin marks all three [ع.], i.e. Arabic.\",\n          \"derivation_fa\": \"هر سه واژه وام‌واژه‌های عربی در فارسی‌اند که با همان ساختِ صامتیِ عربی، از جمله عینِ آغازین یا میانی، وارد شده‌اند. «کَعب» همان kaʿbِ عربی «قوزکِ پا، بندِ استخوان» است و در زبانِ ریاضیِ دانشمندانِ دورهٔ اسلامی معنیِ «مکعب» و «ریشهٔ سوم» هم یافته است؛ معین می‌نویسد: «(رض.) عددی که دو بار در نفسِ خود ضرب شود ... را مکعب گویند». «کعبه» از الکعبةِ عربی، مؤنثِ kaʿb به معنی «خانهٔ مکعب‌شکل» است و تای گِردِ عربی در فارسی به «ـه» بدل شده؛ معنیِ مجازیِ «مقصد، نقطهٔ کانونی» در ترکیب‌هایی چون «کعبهٔ جان» و «کعبهٔ مقصود» تحولِ معناییِ درون‌فارسی و شاعرانه است. «مکعب» صورتِ اسمِ مفعولِ بابِ تفعیل (کَعَّبَ «به توان سه رساندن») است. معین هر سه را با نشانِ [ع.] یعنی عربی آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/كعب\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"FVA:353\",\n              \"status\": \"not_checked\",\n              \"note\": \"No copy of Nahvi's Farhang-e Vāžehā-ye ʿArabi dar Fārsi exists online or on disk (refs_online.json: local_file null, 'Searched archive.org, ketabnak, noorlib, web: no digital copy found').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"Moʿin, Farhang-e Fārsi s.vv. کعب, کعبه, مکعب (MON_part2.txt lines 23783, 23819, 63907)\",\n              \"stance\": \"supports\",\n              \"note\": \"'کعب: [ع.] (ا.) هر بند استخوان؛ شتالنگ. استخوان بلند پشت پای که محل بستن شراک است؛ ج. کعوب ... استخوان مربع که بدان نرد بازند ... (رض.) عددی که دو بار در نفس خود ضرب شود ... را مکعب گویند'; 'کعبه: [ع. کعبة] (ا.) جای چهار گوش؛ مکعب ... کعبهٔ جان: (کن.) مقصد جان، منظور روح'; 'مکعب: [ع.] (امف.) چهار گوشه ... (هن.) جسمی که دارای شش (وجه) است'. The [ع.] tag on each is Moʿin's Arabic-loan marker.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"1966 ed. p. 838 s.v. Kaaba\",\n              \"stance\": \"supports\",\n              \"note\": \"'Arab. kaʿbah, \\\"square house\\\", fr. kaʿb, \\\"cube\\\".' Confirms the Arabic morphology behind Persian کعبه.\"\n            },\n            {\n              \"src\": \"AFM\",\n              \"where\": \"Addi Shir — searched for كعب as a headword\",\n              \"stance\": \"silent\",\n              \"note\": \"Not listed among arabicised Persian words; i.e. the direction of borrowing is Arabic → Persian, as the chart draws it, not the reverse.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"English\",\n          \"words\": \"Kaaba, Caaba\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Kaaba (older spelling Caaba, common in 18th–19th c. travel literature) is a direct transliteration of Arabic الكعبة al-Kaʿba, the cube-shaped sanctuary in the Great Mosque at Mecca, the noun being the feminine of kaʿb 'cube' — literally 'the cubical (house)'. It entered English in the 18th century through European accounts of Arabia and through French/Latin orientalist writing (whence the two vowels of ⟨aa⟩ / ⟨aa⟩ rendering the Arabic long ā, and the older ⟨C-⟩ following Latin-French spelling habits). Klein states the etymology in these terms; the word is a cultural borrowing, not a phonetic descent.\",\n          \"derivation_fa\": \"واژهٔ انگلیسیِ Kaaba (و املای کهن‌ترِ Caaba که در سفرنامه‌های سده‌های هجدهم و نوزدهم رایج بود) آوانگاریِ مستقیمِ «الکعبة» عربی است، یعنی همان بنای مکعب‌شکلِ مسجدالحرام؛ خودِ واژه مؤنثِ kaʿb «مکعب» است و تحت‌اللفظی «خانهٔ چهارگوش» معنی می‌دهد. این واژه در سدهٔ هجدهم از راهِ گزارش‌های اروپاییان از عربستان و نوشته‌های شرق‌شناسانِ فرانسوی و لاتینی‌نویس وارد انگلیسی شده است؛ املای ⟨aa⟩ نمایندهٔ الفِ کشیدهٔ عربی و ⟨C-⟩ی کهن پیروِ سنّتِ املاییِ لاتین و فرانسه است. کلاین همین را می‌گوید. این یک وام‌گیریِ فرهنگی است نه تحولِ آواییِ موروثی؛ ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD:713\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai's AHD:713 is a page of the 1975/76 American Heritage Dictionary main word list (K-section), which is not open online; the local AHD file on disk is only Watkins's 1985 Indo-European Roots appendix, which has no Kaaba entry (grep -i 'kaaba' AHD_watkins1985.txt: no hits). Content checked against Klein instead.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"1966 ed. p. 838 s.v. Kaaba (KLN_1966.txt leaf 452)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Kaaba, n., the cube-shaped building in the Great Mosque of Mecca containing the Black Stone of Mecca. — Arab. kaʿbah, \\\"square house\\\", fr. kaʿb, \\\"cube\\\". Cp. cube.'\"\n            },\n            {\n              \"src\": \"PHN\",\n              \"where\": \"Pihan p. 132 (under CUBE) and the index entry 'Caabat ou Kaabat, n. pr. (a.) 78'\",\n              \"stance\": \"supports\",\n              \"note\": \"'De [kaʿb], augmenté de la terminaison féminine ة, vient [Kaʿbat], nom du temple de la Mekke. Voyez Caabat.' Pihan's own index still spells the European form with C-, matching Nourai's second variant 'Caaba'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Greek\",\n          \"words\": \"kubos, kybos\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Ancient Greek κύβος (kúbos) 'die, cube' is real, but it cannot come from Arabic. It is attested from the earliest Greek literature — Homer already has the dice-players (Il. 23.88), and Herodotus 1.94 reports the Lydian claim to have invented dice — i.e. seven to twelve centuries before any Arabic could have reached Greek. Modern etymological dictionaries reject the Semitic derivation outright: Wiktionary's article states the word 'appears to have no relation to Arabic كَعْبَة (kaʕba)', and Beekes (EDG 2010) treats it as a loan of the substrate/Anatolian type, noting that 'words for dice are often loans and the Lydians claimed to have invented the game'. Etymonline likewise gives only 'of uncertain origin' with the Lydian remark. Nourai's own NOTE reports the competing derivation of POK:589 / AHD:320 from IE *keu-b- 'to bend' (Watkins: 'Zero-grade form *kub- in: a. Greek kubos, cube: CUBE'), which is at least chronologically possible; but Beekes rejects that too, and Klein himself, s.v. cubicle, already separated the two senses ('κύβος in the sense of \\\"cube, die\\\" is a Semitic loan word' vs κύβος 'hollow above the hip'). The one thing all modern authorities agree on is that the Arabic arrow Nourai draws is wrong: Klein's source is Muss-Arnolt's 1892 Semitic-loanword list, long superseded.\",\n          \"derivation_fa\": \"واژهٔ یونانیِ باستانِ κύβος «تاس، مکعب» واقعی است، اما نمی‌تواند از عربی آمده باشد. این واژه از کهن‌ترین ادبیاتِ یونانی گواه دارد — هومر در ایلیاد ۲۳٫۸۸ به تاس‌بازان اشاره می‌کند و هرودوت (۱٫۹۴) ادعای لودیایی‌ها را دربارهٔ اختراعِ تاس نقل می‌کند — یعنی هفت تا دوازده سده پیش از آنکه هیچ واژهٔ عربی بتواند به یونانی راه یابد. فرهنگ‌های ریشه‌شناختیِ امروزی این وام‌گیریِ سامی را یکسره رد می‌کنند: ویکی‌واژه صریحاً می‌نویسد که این واژه «ظاهراً هیچ پیوندی با «کعبة» عربی ندارد»، و بیکس در فرهنگ ریشه‌شناختی یونانی (۲۰۱۰) آن را وامی از لایهٔ زیرین یا از آناتولی می‌داند و یادآور می‌شود که «نام‌های تاس غالباً وام‌واژه‌اند و لودیایی‌ها مدعیِ اختراعِ این بازی بودند». اتیمانلاین نیز تنها «خاستگاهِ نامعلوم» می‌نویسد. خودِ نورایی در یادداشتِ نمودار آورده که پوکورنی (ص ۵۸۹) و AHD (ص ۳۲۰) این واژه را از *keu-b-ِ هندواروپایی «خم شدن» می‌گیرند — واتکینز می‌نویسد «درجهٔ صفرِ *kub-: یونانی kubos». آن راه‌حل دستِ‌کم از نظر تاریخی ممکن است، هرچند بیکس آن را هم رد می‌کند. جالب آنکه خودِ کلاین در مدخلِ cubicle این دو را از هم جدا کرده و نوشته است κύβος به معنیِ «تاس» وام‌واژه‌ای سامی است ولی κύβος به معنیِ «گودیِ بالای ران» نیست. نتیجه: پژوهش امروزی پیکانِ عربی ← یونانیِ نورایی را رد می‌کند؛ سرچشمهٔ این ادعا فهرستِ وام‌واژه‌های سامیِ موس‑آرنولت (۱۸۹۲) است که دیرزمانی است کنار گذاشته شده.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/κύβος\",\n            \"https://www.etymonline.com/word/cube\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:380\",\n              \"status\": \"supports\",\n              \"note\": \"Klein 1966 p. 380 s.v. cube (leaf 210, printed numeral 380): 'fr. Gk. κύβος, \\\"cube, cubical die\\\", prob. of Sem. origin. Cp. Arab. kaʿb, \\\"cube\\\", and see Kaaba. The u in Gk. κύβος is equivalent to Sem. ayin ... See W. Muss-Arnolt in Transactions of the American Philological Association, p. 147.' Klein does say what Nourai says — but Klein is here only a conduit for Muss-Arnolt 1892.\"\n            },\n            {\n              \"ref\": \"PHN:131\",\n              \"status\": \"partial\",\n              \"note\": \"Pihan pp. 131-132 s.v. CUBE: 'Remarquez l'analogie qui existe entre le mot arabe et le grec κύβος, le latin cubus, et l'italien cubo.' Pihan asserts only an 'analogy' between Arabic kaʿb and Greek κύβος; his book derives FRENCH cube from Arabic, and he does not claim the Greek word is borrowed from Arabic.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"1966 ed. p. 380-381 s.v. cubicle\",\n              \"stance\": \"partial\",\n              \"note\": \"'L. cubāre derives fr. I.-E. base *qeu-b-, \\\"to bend, curve, arch\\\", whence also L. cubitum, \\\"elbow\\\", Gk. κύβος \\\"hollow above the hip of cattle\\\" (but κύβος in the sense of \\\"cube, die\\\" is a Semitic loan word), Goth. hups, OE. hype, \\\"hip\\\".' Klein himself splits the Greek word in two, so even in Nourai's own source the Arabic claim covers only one of the two senses.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. keu-² (AHD_watkins1985.txt line 622), and index line 1402 'CUBE keu-2'\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'keu-². Base of various loosely related derivatives with assumed basic meaning \\\"to bend\\\" ... 5. Zero-grade form *kub- in: a. Greek kubos, cube: CUBE'. AHD derives the Greek word from Indo-European, not Arabic — this is the alternative Nourai flags in his own NOTE, and it contradicts the arrow he actually draws.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW pp. 588-592, keu-², keuǝ- (POK_full.txt block ending 'Page(s): 588-592')\",\n              \"stance\": \"contradicts\",\n              \"note\": \"Pokorny's keu-²/keub- article spans pp. 588-592, so Nourai's 'POK:589' is inside it. Pokorny too puts Greek κύβος on the IE side, not the Semitic side.\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Webster's New Twentieth Century, 2nd ed., s.v. cube (WEB_vol1.txt line 46860)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'cube n. [Fr. cube; L. cubus; Gr. kybos, a cube.]' — the chain stops at Greek; no Arabic is mentioned.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"cubus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin cubus 'cube' is a straight learned borrowing of Greek κύβος, taken over by Roman mathematical and architectural writers (Vitruvius, and the arithmetici) together with the Greek geometrical vocabulary; Greek υ is rendered by Latin u/y in the usual way and the Greek second-declension -ος becomes Latin -us. The word is technical throughout: classical Latin for the gaming die is ālea or talus, not cubus. This node is correct as drawn (Greek → Latin); the only issue is inherited from its parent, namely where the Greek word itself comes from.\",\n          \"derivation_fa\": \"لاتینیِ cubus «مکعب» وام‌گیریِ مستقیم و کتابیِ κύβοςِ یونانی است که نویسندگانِ ریاضی و معماریِ رومی (ویتروویوس و حساب‌دانان) همراه با کلِّ اصطلاح‌شناسیِ هندسهٔ یونانی به لاتین آورده‌اند؛ υی یونانی به u/y لاتین برگردانده شده و پایانهٔ صرفِ دومِ -ος به -us بدل شده است. این واژه در لاتین همیشه اصطلاحی و فنی مانده است: تاسِ بازی در لاتینِ کلاسیک ālea یا talus خوانده می‌شود نه cubus. این گره چنان‌که رسم شده درست است (یونانی ← لاتین)؛ تنها اشکال، اشکالِ به‌ارث‌رسیده از گرهٔ مادر است، یعنی خاستگاهِ خودِ واژهٔ یونانی.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/cube\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"WEB:441\",\n              \"status\": \"supports\",\n              \"note\": \"Webster's New Twentieth Century Dictionary, 2nd ed., s.v. cube (WEB_vol1.txt line 46860, leaf 472): 'cube n. [Fr. cube; L. cubus; Gr. kybos, a cube.]', and s.v. cubic '[L. cubicus; Gr. kybikos, from kybos, a cube.]'. The scan's own page numbering could not be read at this leaf, so the exact page 441 is unverified, but the entry says what is cited.\"\n            },\n            {\n              \"ref\": \"FSD:626\",\n              \"status\": \"supports\",\n              \"note\": \"Funk & Wagnalls New Standard Dictionary, s.v. cube (FSD_vol1.txt line 83757): '[F. < L. cubus, < Gr. kybos, cube.]' — exactly the Greek → Latin → French → English chain.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"1966 ed. p. 380 s.v. cube, cubic, cubiform\",\n              \"stance\": \"supports\",\n              \"note\": \"'cube, n. — F., fr. L. cubus, fr. Gk. κύβος'; 'cubic, adj. — F. cubique, fr. L. cubicus, fr. Gk. κυβικός, fr. κύβος'; 'cubiform ... Compounded of L. cubus, \\\"cube\\\", and forma'.\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"Funk & Wagnalls vol. I s.v. cube\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check; F&W add 'Eng. A paving-block' for the concrete sense, still from L. cubus.\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Webster's 2nd ed. s.v. cube / cubo-\",\n              \"stance\": \"supports\",\n              \"note\": \"'cubo-, [L. cubus, Gr. kybos.] a combining form meaning a cube'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"cube\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English cube (noun, 1550s; verb 'to raise to the third power', 1580s) comes from Middle French / French cube (13th c.), from Latin cubus, from Greek κύβος. Nourai's chart draws the arrow straight from Latin to English, omitting the French relay through which the word actually reached English — every dictionary consulted (Klein, Webster, Funk & Wagnalls, Etymonline) puts French between them: 'F., fr. L. cubus'. The semantic content did not shift: it has been the geometrical solid and, in arithmetic, the third power, from the Greek mathematicians onwards.\",\n          \"derivation_fa\": \"واژهٔ انگلیسیِ cube (اسم، حدودِ ۱۵۵۰ میلادی؛ فعل به معنی «به توان سه رساندن»، حدود ۱۵۸۰) از cubeٔ فرانسه (سدهٔ سیزدهم) گرفته شده و آن از cubusِ لاتین و آن از κύβοςِ یونانی است. نورایی پیکان را مستقیم از لاتین به انگلیسی کشیده و واسطهٔ فرانسه را انداخته است، حال آنکه همهٔ فرهنگ‌هایی که بررسی شد — کلاین، وبستر، فانک‑و‑واگنالز و اتیمانلاین — فرانسه را میانِ این دو می‌نشانند: «F., fr. L. cubus». از نظر معنایی هیچ تحولی رخ نداده است: از ریاضی‌دانانِ یونانی تا امروز همان جسمِ هندسی و همان «توانِ سوم» در حساب بوده است. ادعای نورایی جز در حذفِ حلقهٔ فرانسه درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/cube\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD:320\",\n              \"status\": \"partial\",\n              \"note\": \"Nourai's AHD:320 is the 1975/76 AHD main-dictionary page for cube (not open online). The corresponding Watkins root article is on disk: AHD_watkins1985.txt line 622, keu-² '... 5. Zero-grade form *kub- in: a. Greek kubos, cube: CUBE', and the index (line 1402) 'CUBE keu-2'. So AHD does carry English cube back to Greek kubos — but, as Nourai's own NOTE concedes, it takes the Greek word to be Indo-European, not Arabic.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"1966 ed. p. 380 s.v. cube\",\n              \"stance\": \"supports\",\n              \"note\": \"'cube, n. — F., fr. L. cubus, fr. Gk. κύβος' — the French stage that the chart omits.\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"Funk & Wagnalls vol. I s.v. cube\",\n              \"stance\": \"supports\",\n              \"note\": \"'[F. < L. cubus, < Gr. kybos, cube.]'\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Webster's 2nd ed. s.v. cube\",\n              \"stance\": \"supports\",\n              \"note\": \"'[Fr. cube; L. cubus; Gr. kybos, a cube.]'\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T15:45:53.867Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-231.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T15:45:57.997Z] TOOL CALL #78: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-231.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 231"
}
```


### [2026-09-06T15:46:01.510Z] TOOL RESULT

```
JSON OK
nodes verified: 15/15
node verdicts: {'confirmed': 12, 'plausible': 1, 'unverified': 1, 'disputed': 1}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 8, 'partial': 5, 'not_found': 1, 'not_checked': 5}
books consulted: {'supports': 33, 'partial': 3, 'silent': 3, 'contradicts': 3} | by book: {'KLN': 8, 'AHD': 4, 'SKT': 3, 'WEB': 3, 'BRT': 2, 'KNT': 2, 'WLD': 2, 'PHD': 2, 'MON': 2, 'POK': 2, 'LAT': 2, 'FSD': 2, 'SOD': 1, 'NYB': 1, 'HRN': 1, 'HUB': 1, 'ARY': 1, 'BOOK': 1, 'AFM': 1, 'PHN': 1}
```


## [2026-09-06T15:46:19.690Z] AGENT

Page 231 (book p. 201) verified: `/home/sfmqrb/git/rishe/data/verification/page-231.json` — `verify_check.py 231` reports 15/15 nodes, **0 PROBLEM lines**.

**Verdicts** — nodes: 12 confirmed, 1 plausible, 1 disputed, 1 unverified. Roots: 1 confirmed (Kâ 1, Qâ), 1 plausible (Arabic K.ʿ.b).

**Flagged items**
- **disputed** — K.ʿ.b, node #3 Greek *kubos/kybos*: cannot come from Arabic *kaʿb*. Greek κύβος is already in Homer (Il. 23.88) and Herodotus 1.94, centuries before Arabic contact. Wiktionary says it "appears to have no relation to Arabic كَعْبَة"; Beekes calls it a substrate/Lydian loan; Etymonline "of uncertain origin". Klein 1966 p.380 *does* say what Nourai says, but he is relaying Muss-Arnolt 1892. Pihan p.131 claims only an "analogie", not a derivation.
- **plausible** — Kâ 1, node #5 Av./OP *čanah, činah, činman*: forms are all real (Bartholomae; Kent s.v. Aspacanah- "Lover of Horses"), but Pokorny attaches Ind.-Ir. *kan-/can-* to *kā-* only with a question mark, and Kent writes "possibly canah-". Also, Kent's lexicon entries sit at pp. ~180–193, not the cited KNT:173.
- **plausible root** — Arabic K.ʿ.b: root is genuine, but the basic sense is 'ankle/knuckle bone, node' (Qur'an 5:6); 'cube' is a late mathematicians' extension, not the root gloss.
- **unverified** — Kâ 1, node #6: I rendered the printed page (copy at `data/verification/sources/refs/ocr/BOOK/231.png`) — the book prints a genuinely **empty box** there (no language, refs or words). The extraction is faithful; this is Nourai's own layout artefact, not a data error.

**No extraction errors found** — the JSON matches the printed page throughout.

**Minor chart inaccuracies noted in the file (not verdict-changing):** node #9 glosses Latin *cārus* "desire" (it means 'dear, beloved'); node #5's *aspa-canah* is a normalisation of attested OP *Aspačanā*; node #5's Latin→English *cube* edge omits the French relay; Sogdian is drawn from "Av./OP" though it inherits from Proto-Iranian.

**Reference availability:** FVA (Nahvi) has no digital copy anywhere — 2 refs not checked. SNS:209 not_found (that volume's OCR carries almost no usable text). AHD:713 (1976 main word list) not open online; checked against Klein p.838 instead. KLN:1743 falls past the end of the local 1966 scan (~p.1700), so I quoted the same entry from the 1971 one-volume edition. Saved a new vision transcript at `data/verification/sources/refs/ocr/BQT/1578.vision.txt` (Mo'in's footnote: Av./OP *kāma*, Bartholomae 463, Nyberg 118, Horn/Hübschmann 838).
