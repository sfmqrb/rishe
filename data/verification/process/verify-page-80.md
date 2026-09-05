# Verification process log — verify-page-80


## [2026-09-05T06:03:31.460Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 80 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-80.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-80.json. Write /home/sfmqrb/git/rishe/data/verification/page-80.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 80` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T06:03:32.905Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T06:03:33.616Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T06:03:33.630Z] TOOL RESULT

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


## [2026-09-05T06:03:33.693Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-80.txt"
}
```


### [2026-09-05T06:03:33.712Z] TOOL RESULT

```
1	=== PDF page 80 (book page 50) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bhâ 2 : to speak, heal  (refs POK:105)
4	#1 (parent #0) [Avestan / Old Persian] refs=NYB:48; POK:105 | bišazka : healer, doctor ; baešaza : doctor, medicine
5	  #2 (parent #1) [Pahlavi] refs=AEF:237 | bešazak : doctor
6	    #3 (parent #2) [Persian] refs=BQT:399 | pezešk «پزشک» : doctor
7	  #4 (parent #1) [Sogdian] refs=SOD:117 | byc : doctor
8	#5 (parent #0) [Latin] refs=AHD | fârî : to speak
9	  #6 (parent #5) [English] refs=None | infant, fate, fame, confess, preface
10	#7 (parent #0) [Greek] refs=AHD:1304; KLN:1557 | phônĕ : voice ; sun-phônĕ : harmonious sound ☞Sem 1
11	  #8 (parent #7) [French] refs=None | telephone ; symphonie
12	    #9 (parent #8) [Persian] refs=MON:1132, 1921 | telefon «تلفن» ; gerâmâfon «گرامافون» ; samfonî «سمفونی»
13	    #10 (parent #8) [English] refs=AHD | symphony
14	  #11 (parent #7) [English] refs=None | phone, prophet
15	#12 (parent #0) [Germanic] refs=AHD | banwan : speak publicly
16	  #13 (parent #12) [English] refs=None | ban, abandon
17	--- entry 1 ---
18	ROOT [Indo-European] Bhad : good  (refs POK:106)
19	#1 (parent #0) [Avestan] refs=POK:106; KLN:167 | badra : good fortune, luck ; hu-badra : (with) good luck, lucky ☞Su 1
20	  #2 (parent #1) [None] refs=None | 
21	#3 (parent #0) [Germanic] refs=AHD | batiso : good
22	  #4 (parent #3) [English] refs=None | better, best
23	
```


## [2026-09-05T06:03:36.841Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-80.json",
 "description": "Read source JSON for page 80"
}
```


### [2026-09-05T06:03:36.870Z] TOOL RESULT

```
{
  "pdf_page": 80,
  "book_page": 50,
  "entries": [
    {
      "root": {
        "name": "Bhâ 2",
        "lang": "Indo-European",
        "refs": "POK:105",
        "gloss": "to speak, heal"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "NYB:48; POK:105",
          "words": [
            {"translit": "bišazka", "gloss": "healer, doctor", "script": null},
            {"translit": "baešaza", "gloss": "doctor, medicine", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "AEF:237",
          "words": [
            {"translit": "bešazak", "gloss": "doctor", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:399",
          "words": [
            {"translit": "pezešk", "gloss": "doctor", "script": "پزشک"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:117",
          "words": [
            {"translit": "byc", "gloss": "doctor", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "fârî", "gloss": "to speak", "script": null}
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
            {"translit": "infant, fate, fame, confess, preface", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:1304; KLN:1557",
          "words": [
            {"translit": "phônĕ", "gloss": "voice", "script": null},
            {"translit": "sun-phônĕ", "gloss": "harmonious sound", "script": null, "see": ["Sem 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "telephone", "gloss": null, "script": null},
            {"translit": "symphonie", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON:1132, 1921",
          "words": [
            {"translit": "telefon", "gloss": null, "script": "تلفن"},
            {"translit": "gerâmâfon", "gloss": null, "script": "گرامافون"},
            {"translit": "samfonî", "gloss": null, "script": "سمفونی"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "symphony", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "phone, prophet", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "banwan", "gloss": "speak publicly", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "ban, abandon", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Bhad",
        "lang": "Indo-European",
        "refs": "POK:106",
        "gloss": "good"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:106; KLN:167",
          "words": [
            {"translit": "badra", "gloss": "good fortune, luck", "script": null},
            {"translit": "hu-badra", "gloss": "(with) good luck, lucky", "script": null, "see": ["Su 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": null,
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "batiso", "gloss": "good", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "better, best", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T06:03:37.595Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T06:03:37.626Z] TOOL RESULT

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


## [2026-09-05T06:03:55.109Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','NYB','AEF','BQT','SOD','AHD','KLN','MON','BRT','PHD','HRN','HUB','WLD','IEC','SYN','SKT','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:700]); print()\n\""
}
```


## [2026-09-05T06:03:55.329Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && head -60 data/verification/page-66.json"
}
```


### [2026-09-05T06:03:56.762Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, ver

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
```


### [2026-09-05T06:03:56.808Z] TOOL RESULT

```
agent
page-101.json
page-126.json
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
page-51.json
page-52.json
page-53.json
page-54.json
page-55.json
page-56.json
page-57.json
page-58.json
page-59.json
page-60.json
page-61.json
page-62.json
page-63.json
page-64.json
page-65.json
page-66.json
page-67.json
page-68.json
page-69.json
page-70.json
page-71.json
page-72.json
page-73.json
page-74.json
page-75.json
---
{
  "pdf_page": 66,
  "book_page": 36,
  "verified_by": "claude-fable-5-1",
  "verified_on": "2026-09-04",
  "entries": [
    {
      "entry": 0,
      "root": "A`.s.r",
      "verdict": "confirmed",
      "modern_form": "Arabic root ع ص ر ʿ-ṣ-r 'to press, squeeze (the juice out)'; West Semitic *ʿṣr 'to press, restrain, retain'",
      "note": "The root box is right on all three counts: the Arabic verb عَصَرَ ʿaṣara 'he pressed, squeezed' is real, the language label is right, and the gloss 'to squeeze (the juice out)' is almost word for word the gloss of the AHD Appendix of Semitic Roots ('ʿṣr — West Semitic, to press, restrain, retain … alizarin, probably from Arabic al-ʿuṣāra, the juice, from ʿaṣara, to squeeze'). Two refinements. (a) The root is not specifically Arabic but common West Semitic: AHD labels it West Semitic and Klein, s.v. alizari, compares Hebrew ʿātzar, Aramaic-Syriac ʿătzar 'he retained' — so 'Arabic' should read 'Arabic (West Semitic)'. (b) The derived noun is vocalised ʿuṣāra عُصَارَة by AHD and by Wiktionary, ʿaṣārah by Klein; Nourai follows Klein's a-vocalism ('a`sârah'), and since both variants are attested this is not an error, only a choice of source. The European branch of the chart (Sp. → Fr. → Eng. alizarin) is Klein's and AHD's account, but AHD hedges it with 'probably', Dozy explicitly declared the origin unknown, and Wiktionary/Webster's 1913 now prefer an Ottoman-Turkish route — see node #3.",
      "note_fa": "ریشهٔ «ع ص ر» به معنای «فشردن، آب چیزی را گرفتن» ریشه‌ای اصیل و درست است و برچسب زبانی و معنای آن در نمودار نورایی با آنچه پیوست ریشه‌های سامی فرهنگ American Heritage می‌آورد یکسان است؛ تنها نکته آن است که این ریشه ویژهٔ عربی نیست و سامی غربی است (کلاین هم عبری «عَصَر» به معنای «نگاه داشتن» را هم‌ریشهٔ آن می‌داند). گونهٔ اسمی آن در فرهنگ‌های امروزی عُصارة و در کلاین عَصارة ضبط شده و نورایی ضبط کلاین را برگزیده است؛ هر دو ضبط پذیرفتنی است و خطا نیست. شاخهٔ اروپایی این نمودار (اسپانیایی ← فرانسوی ← انگلیسی alizarin) از کلاین گرفته شده، ولی همان‌گونه که در گرهٔ ۳ گفته می‌شود، این بخش قطعی نیست و ویکی‌واژه امروزه راه دیگری (از راه ترکی عثمانی) پیشنهاد می‌کند. در مجموع ادعای نورایی دربارهٔ خودِ ریشه درست است.",
      "sources": [
        "https://www.ahdictionary.com/word/semitic.html",
        "https://www.ahdictionary.com/word/search.html?q=alizarin",
        "https://en.wiktionary.org/wiki/عصارة"
      ],
      "ref_check": [
        {
          "ref": "KLN:50",
          "status": "supports",
          "note": "KLN_1966.txt, form-feed leaf 38 (two printed pages per leaf ⇒ printed pp. ~52-53, i.e. Nourai's p.50 ±2): 'alizari, n., madder root. — F., fr. Sp. alizari, fr. Arab. al-'aṣārah, \"the juice\", fr. al-, \"the\", and aṣara, \"he squeezed, pressed\", which is rel. to Heb. ʿātzar, Aram.-Syr. ʿătzār, \"he retained\".' Exactly the root, the gloss and the Romance chain Nourai draws."
        },
        {
          "ref": "FVA:273",
          "status": "not_checked",
          "note": "FVA = S.M. Nahvi, Farhang-e vāžehā-ye ʿarabi dar fārsi (1368/1989). refs_online.json records no digital copy on archive.org, ketabnak, noorlib or the open web; catalogue record only (OpenLibrary OL2012991M)."
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Arabic",
          "words": "a`sârah; al-a`sârah",
          "verdict": "confirmed",
          "derivation": "Arabic عُصَارَة ʿuṣāra (Klein: ʿaṣārah) is the regular fuʿāla/faʿāla noun of result built on the triliteral ʿ-ṣ-r 'to press': Wiktionary defines it as 'somewhat viscose liquid that one obtains by wringing, sap, juice, extract'. Nourai's two lines are one and the same word, indefinite ʿuṣāra and definite al-ʿuṣāra; he lists both because it is the article-bearing shape that travelled into Romance (Sp. alizari), the same fossilised al- seen in alcohol, alidade, alkali, almanac. The word is native Arabic — no Semitic dictionary treats it as a loan — and it is the hinge of both branches of the chart, the Persian loan عصاره and the Spanish/French dye name.",
          "derivation_fa": "واژهٔ عربی عُصارَة بر وزن فُعالَة از ریشهٔ سه‌حرفی «ع ص ر» ساخته شده و به معنای «شیره و مایعی است که از فشردن گیاه به دست می‌آید». دو صورتی که نورایی آورده (عصارة و الْعصارة) در حقیقت یک واژه‌اند، یکی نکره و دیگری معرفه؛ آوردن صورت معرفه از آن روست که همین شکلِ همراه با «الـ» بوده که به زبان‌های اروپایی راه یافته است، درست مانند alcohol و alkali و alidade. این واژه در عربی اصیل است و هیچ فرهنگ سامی آن را وام‌واژه نمی‌داند؛ ادعای نورایی در این گره درست است.",
          "sources": [
            "https://en.wiktionary.org/wiki/عصارة",
            "https://www.ahdictionary.com/word/semitic.html"
          ],
          "ref_check": [
            {
              "ref": "FVA:273",
              "status": "not_checked",
              "note": "no digital copy of Nahvi's dictionary exists (see root ref_check); the page cannot be inspected."
            }
          ],
          "consulted": [
            {
              "src": "KLN",
              "where": "KLN_1966.txt leaf 38 (≈p.52) s.v. alizari",
              "stance": "supports",
              "note": "'fr. Arab. al-'aṣārah, \"the juice\", fr. al-, \"the\", and aṣara, \"he squeezed, pressed\"' — same word, same morphology."
            },
            {
              "src": "AHD",
              "where": "online Appendix of Semitic Roots s.v. ʿṣr",
              "stance": "supports",
```


## [2026-09-05T06:04:01.365Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=113 && NR<=116' POK_01.txt | head -200"
}
```


### [2026-09-05T06:04:03.170Z] TOOL RESULT

```
A«?  , Erdscholle' 5  ai.  bdlha-ja-h  ,Eleusine  indica,  eine  Grasart', trenn  ,aus  Wurzelknollen  hervorkommend'?,  lat.  bulhus  , Zwiebel,  Bolle' ist  aus  ßolßoq  entlehnt.
Redukt.-stufig-  oder  mit  Assimil.  an  den  Vok.  der  2.  Silbe  arm.  falar Pustula,   boUa'.
WP.  11  Ulf»   ^^'^'  1   122.
brsngh-,  brongh'?  ,heiser'?
Gr.  ßqayxoq  , Heiserkeit',  ßqayxaco  ,bin  heiser',    air.  hrong{a)ide  ,heiser'; aber  g'r.  Aor.  eßqaxe  , krachte'  bleibt  wohl  fern. \VP,  I  683  f.,  II  119.
treuq-  , springen,  schnellen'.
Vielleicht  vereinigen  sich  so  gr.  ßgov-aog,  ßQevAog  (ßgavT-og),  ßgvycog  , Heu- schrecke' (ßgovxog  wohl  nach  ßqtxo)  , knirsche  mit  den  Zähnen',  und  sloven. hrknem,  brkniti,  hrkam,  bvkati,  brcati  ,mit  den  Füßen  stoßen,  ausschlagen, mit  den  Fingern  wegschnellen',  russ.  brykäth  ,mit  den  Hinterfüßen  aus- schlagen, klr.  brykdty  ^mutwillig  herumspringen,  laufen'  usw.
WP.  II  119,  Specht  Idg.  Dekl.  251  f.
bronk-  , einschließen,  einengen'.
Got.  anapraggan  , bedrängen'  zu  *pranga-  ,Beengung'  in  aschwed.  prang ,enge  Gasse',  mengl.  prange  ,Enge',  engl.  dial.  proug  , Tischgabel',  mndd. prangen  , drücken',  pranger  , Pfahl',  mhd.  pfrengen  ,einzwängen',  ahd. pfragina  , Schranke',  zu  lit.  branktas  m.  , Strangholz',  lett.  brankti  (lit.  Lw.) jfest  anliegend'.
WP.  II  119,  677  f.,  Feist  43,  Kluge  ^^  unter  Pranger.
bU'  ,Lippe,  Kuß',    als  Nachahmung  des  Kußlautes,    Sprengung   des  saugen- den Lippenverschlusses  nach   innen,    also   eigentlich  verschieden  von bu-j  bhii-  , aufblasen'  mit  normaler  Sprengung  nach  außen. Npers.  bösidan  ,küssen';  alb.  buze  ,Mund';   mir.  bus,  pus  , Lippe',  busöc, pusöc  ,Kuß'  (dazu  vermutlich  gall.  PN  Bussumäros  und  buMutton  ,Mündchen, Kuß');  nhd.  Buss  ,Kuß',  bussen  ,küssen',  Busserl  ,Kuß',  engl,  buss,  schwed. (mit  regelrechter  Lautverschiebung)  puss  ,Kuß';   lit.  bn6iüoti  , küssen',  buc den    Schall    des    Kusses    malende    Interjektion,    poln.    buzia    , Mündchen, Mäulchen;  Kuß'. WP.  I  113f.,  WH.  II  98.
Bh.
bhä-,  hhö'f  bhQ'  ,gläazen,  leuchten,  scheinen*.
Ai.  bhä  (in  Kompos.)  , Schein,  Licht,  Glanz',  hhäti  ,leuchtet,  (er-)scheint'' bhäti-hi  , Licht',  bhäna-m  n.  ,das  Leuchten,  Erscheinung'  (vgl.  air.  häii, ,vveiß',  ags.  bönian  , polieren'),  bhänü-h  , Licht,  Strahl,  Sonne'  (:  as.  banu-tj^ bhäma-h  , Licht,  Schein';  t
av.  bä-  , scheinen'  nur  mit  ä-  [aväntdm  ,den  gleichenden'),  frä  (fra- väiti  ,leuchtet  hervor')  und  vi-  (yi-bä-  , leuchten',  Benveniste  BSL.  32,  86  f.)^ vispö-bäm(ij)a-  , allglänzend',  bämya-  , licht,  glänzend',  bäirn-  m.  .Licht* Strahl';  ^
arm.  banam  (*bhä-n-)  , öffne,  enthülle'  (wenn  eigentlich  , zeige,  lasse  sicht- bar werden'),  Aor.  ba-t''si,  vgl.  gr.  cpah'ü)  und   alb.  bdj  ]
gv.  TtEcpriasTai  ,wird  erscheinen',  *-bJid-n-  im  Präse
ns  cpaivu)  (*q)avicü  statt *(pd-va)  Schwyzer  Gr.  Gr.  I  694)  , mache  sichtbar,  zeige',  (paivoixat  , er- scheine, scheine,  leuchte'  {eq)dvrjv^  Aor.  ecprjva)]  cpävsQog  , sichtbar,  offenbar, deutlich',  cpavrj  , Fackel^;  q)daig  , Aufgang  eines  Gestirns'  (s.  auch  unter  2. bhä-),  (pda(A,a,  -avog  , Erscheinung,  Gesicht,  Vorzeichen',  vgl.  7ieq)ao^evog)] dficpccSöv,  diLcpddioq  , offenbar'  (ava-cp-)]  cpdvza'  IdfxnovTa  Ples.  (zu  *(jpß^t  = ai.  bhäti)]  vgl.  aQyv-cpsog,  äoyvcpog  ,weißgiänzend' ;
alb.  gQg.  bdj,  tosk.  benj  (==  cpalvo))  , mache,  tue'  (ursprüngl.  wohl  , bringe zur  Erscheinung');
air.  bän  ,weiß',  oib  f.  (*opi-bha)  , Erscheinung,  Schönheit';
as.  banut  ,föraes' ;  ags.  bönian  , polieren'  (d.  i.  , glänzend  machen'),  ndd, (und  daraus  nhd.)  bönen  , scheuern,  höhnen',  mhd.  biienen  , höhnen'  (ob got.  bandioa,  -wo  , Zeichen',  bandwjan,  aisl.  benda  ,ein  Zeichen  geben' hierher  gehören  —  etwa  als  w-Ableitung  von  einem  Partiz.  bhä-nt-  ,schei- nend'  --,  ist  fraglich.     Lit.  bei  Feist  79  f.);
osorb.  baju,  bac  so  , unmerklich  brennen,  glimmen',  nsorb.  bajom,  bajas se  ,glimraen,  flackern';
toch.  A  pam  ,klar'  {*bhdno-),  pafii  , Schönheit',  B  penijo  ds.  (Duchesne- Guillemin  BSL.  41,  164);  A  päkär,  B  päkri,  a-päkärtse  ,offen,  deutlich'; A  pä-tsänk,  B  pa-tsähk  , Fenster'  {-tsänk  usw.  , leuchten').  Van  Windekens Lexique  78  f.;  ^  pate,  A pat  (im  Kompos.)  ,Erscheinung'  (Hhä-ti-),  Pisani Rc.  R.  Ist.  Lomb.  78,  2,  28.
f
105
. Erweiterung'  bhö-s-:  Sii.bhäs-n.  (ved.  auch  zweisilbig),  Instr.  bhäsä 1  'cht  Schein,  Herrlichkeit,  Macht',  subhäs-  , schönen  Glanz  habend',  bJiä- *   //    o-länzt^  bhüsant-  ,glänzend',   bliäsah  n.   , Licht' ;
crr  wcbayiSL'  diacpdvsi  Hes.,  öiacpcüdytcu  .beginne  zu  glänzen*  sind  vielleicht (ins  fti-(p(xv(Ty'Oj)  nach  cpojg  umgebildet,  ebenso  cpcüarrjO  , Glanz,  Leuchte'.
TJusicher  ist,  ob  mir.  basc  ,rot',  ags.  basic,  baso  ,purpurn'  (*bkds-7co-,  -uo-) iiizaschließen  sind^  zu  got.  iceina-basi  ,  Weinbeere',  ahd.  beri  , Beere',  eigent- lich ,rote  Beere'?    Dazu  der  vollstufige  MN  ahd.  Buoso,   aisl.  Bösi  usw.?
u-ErAveiterung    bhä-u-:    ai.  vl-bhäva-h,    vi-bhävan-    , strahlend,    schei- <->
nend*;
o'v.  hom.  (pde  (*(pcxfs)  , glänzte,  erschien',  cpasOwv,  -ovrog  »glänzend',  cpaeol- ußgorog,  Find.  (pav(Ji-i.tßQOTog  ,für  die  Menschen  glänzend',  cpdog  (äol. (cdvog,  pamph.  cpaßog)  att.  kontr.  (fojg^  Gen.  (pojTÖg,  q)äovg,  , Licht,  Heil', wovon  '^q)afsa-v6g  in  lesb.  (paswog,  ion.  cpasivög,  att.  cpavög  , glänzend',  hom. (pasivüj  .glänze';  Tzicpava-AO)  ,las3e  
leuchten;  zeige;  gebe  kund'.  Anders Specht  KZ.  59,  58  f.
Ist  germ.  *baukna-,  in  afries.  bähen  , Wahrzeichen,  Feuersignal',  as.  bökan , Zeichen,  Wahrzeichen',  ags.  beacen  , Zeichen,  Fahne',  ahd.  bouhhan  , Zei- chen' von  solchem  germ.  *bau-  nach  "^taikna-  , Zeichen'  gebildet?
WP.  n  122  f.,  WH.  I  454  f.,  Schwjzer  Gr.  Gr.  I  694,  709.
2.  hhä-  , sprechen'.
Ai.  wahrscheinlich  in  sabhä  .Versammlung'  (,*colloquium';  bhä-  im  Ai. allerdings  sonst  —  bis  auf  bhdnati,  s.  unten  —  nur  in  der  Bed.  , scheinen, glänzen');
arm.  bau  (^bhä-nis),  Gen.  -i  ,Wort,  Rede,  Vernunft,  Urteil,  Sache',  bay^ Gen.  bayi  ,Wort,  Ausdruck'  (*bhd-tl-s  =  gr.  q)dTig)',  bay  Partikel  ,inquit' {==z  (prjal,  auch  bam  =  (prjai^  &as  =  lesb.  cpau  aus  *bhäsi)]
gr.  (priiil^  dor.  ^ä/a  ,sage',  (prjuT],  dor.  q)df.iC(  , Kunde,  Ruf,  Offenbarung' (=  lat. /äwa;  dcprjfioreg'  äogr/coi,  ovy,  övoi,La^6{A,€voi  Hes.  und  das  erst  bei Apuleius  begegnende  affämen  , Ansprache'  braucht  keine  alte  Gleichung zu  sein);  (pdoY.ü)  ,sage,  sage  ja,  glaube'  (auch  ßdaY.avog^  lat.  fascimimj  s. unter  *baba  Schalhvort),  q)dvig  f.  , Gerücht',  cpdaig  , Sprache,  Rede,  Behaup- tung, Anzeige';  mit  Ablaut  cpwvi^  , Stimme' ;
lat. /o?';  färl  (aus  *fa-{ö(r)  =  ksl.  baju^  ags.  böian)  , sprechen',  fäcundus , redegewandt',  fätum  , Ausspruch,  Weissagung,  festgesetzte  Weltordnung, Geschick',  fäma  , Gerede,  Gerücht,  Überlieferung'  (Denom.  osk.  faamat etwa  ,ruft'),  fäbula  ,Rede,  Sage'  (*bhä-dhlä),  fäs  eigentlich  , Ausspruch, bes.  göttlicher  oder  richterlicher;  göttliches  Recht',  wohl  aus  (ne)fäs  est mit  infinitivischem  fas  (s-Stamm)  ,es  ist  (nicht)  auszusprechen  (anders EM  333);  dazu  dies  fästus  , Spruchtag  für  den  Prätor',  fästi  ,das  Verzeich-
106
nis  dieser  Tage,  Kalender';  als  Ableitung  von  einem  Partiz.  Hhd-to-s,  Uj fateovj  -erl,  fassus  , öffentlich  erklären,  zugeben'  =  osk.  fatium  ,färi',  la| Fätuus,  Beiname  des  ,Faunus  väticinäns';
aisl.  hön,  ben  , Bitte,  Gebet^  ags.  boen  , Bitte,  Fron'  (Hhä-ni-s;  oder  mi ö-Abtönung  wie  gr.  cpcxjvi^?)]  ags.  böian  ,prahlen'  (wie   lat.  jör  aus  *fäii slav.  bajg);
russ.-serb.-ksl.    baju,    bajati    , erzählen,    besprechen,    heilen',    ksl.    basi , Fabel,  Zauberspruch',  aksl.  bahji,  Gen.  -tje  ,Arzt'.
Auf  einem  Präsens  ^bh-en-  beruht  ai.  bhdnati  , spricht*;  auf  *bhdn-u^ (oder  auf  germ.  Umbildung  nach  spannan)  ahd.  bannan  redupl.  Verb] ,unter  Strafandrohung  befehlen,  verordnen,  in  Bann  tun',  ags.  bannai redupl.  Verb  ,vorladen,  befehlen',  aisl.  banna  schw.  Verb.  ,verbiete
n',  w( von  ahd.  barij  PI.  banna  , Gebot  unter  Strafandrohung*  (nhd.  Bann,  Bawdi tcald),  ags.  gebann,  aisl.  bann  n.  »Verbot,  Bann*.
Toch.  A  pä-j  pä-g-  , betteln'  (Van  Windekens   Lexique  87  f.).
Nach  Kuiper  (AO.  XII  262)  hierher  (*bhd-s-)  ai.  bhisdkti  ,heilt',  bhiSdfi jArzt',  jav.  -bis-  , heilend*;    über   av.  bisazjät   vgl.  Kuiper  Nasalpräs.  44 fj
WP.  II  123 f.,  WH.  I  437  f.,  450,  458  f.,  525 f.,  Schwjzer  Gr.  Gr.  I  674r
bhabhä  und  anklingende  Worte  für  , Bohne*,  u.  zw.  , Saubohne',  vgl.  zuml Sachlichen  Hoops  Waldb.  350,  400  f.,  464  f.,  Helm  Kltpfl.«  221,  570,1 Schrader  RL.^  159  f.  |
Lat.  faba  (fäl.  haba)  , Bohne'  (dazu  die  PN  Fabius,  Fabidius  usw.  und die  Insel  Fabäria),  russ.  usw.  bob^,  apr.  babo  ds.  Wohl  redupliziertes Lallwort  und  als  , aufgeblasene  Schote,  Schwellung'  mit  gr.  g)a-KÖg  m. , Linse' :  alb.  bathe  f.  , Saubohne*  (*bhakä)  verwandt.  Auch  aisl.  baun,  ags. bean,  ahd.  bona  , Bohne'  (Baunonia  friesische  Insel  bei  Plinius)  sind  wohl durch  Dissimil.  von  *bab7iä  zu  *baunä  entstanden. WP.  II  131,  WH.  I  436.
bhMd'  .gut*.
Ai.  bhadrd-h  , erfreulich,  glücklich,  gut',  n.  , Glück,  Heil',  sii-bhadra-h ,herrlich' =  av.  hu-badra-  »glücklich';
got.  batiza  ,besser',  batista  , bester',  aisl.  betre,  betstr,  ags.  bet{e)ra,  betst, ahd.  bezzir(o),  bezzist,  nhd.  besser,  best]  dazu  das  Adv.  des  Kompar.  aisl. betr,  ags.  bet  (*batiz),  ahd.  baz  (*bataz,  erstarrtes  Neutr.  .Nutzen');  aisl. batim.  ,Verbesserung,  Heil*,  afries.  bata  m.  , Vorteil*,  mhd.  bazze  ds.;  got. gabatnan  ,Nutzen  erlangen*,  aisl.  batna  , besser  werden*,  ags.  batian,  ahd. bazzen  ds.;  mit  Ablaut  got.  böta  f.  ,Nutzen*,  aisl.  ags.  bot  , Besserung,  Er- satz*, ahd.  buoz(a)  f.  ,Besserung,  Buße'.
WP.  II  151  f..  Feist  83,  103,  174,  J.  Weisweiler  Buße  (1930).
107
hhaZ'  zuteilen;  als  Anteil  bestimmen  oder  (ursprüngl.  medial?)  als  An- '  teil,  als  Portion  erhalten'.
Ai  bhajati  , teilt  zu'  =  av,  bag-  (bazat)  ,als  Anteil  bestimmt  sein',  ai. hhaaa-h  ,Gut,  Glück*,  av.  baga-,  baya-  n.  , Anteil,  Los,  bes.  günstiges';  ai. bhaaa-h  , Zuteiler,  Herr,  Beiname  des  Savitar  und  eine
```


## [2026-09-05T06:04:30.087Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT bisaz ===\"; grep -n -i -E 'bisaz|bišaz|baesaz|baēšaz|biSaz' BRT.txt | head -40; echo \"=== BRT badra ===\"; grep -n -i -E 'hubadra|hu-badra|hubaδra|baδra|badra-' BRT.txt | head -30"
}
```


### [2026-09-05T06:04:30.187Z] TOOL RESULT

```
=== BRT bisaz ===
4509:•  j.  anu-maya-  Adj.  'mäh  machend,  blö- kend', vom  Schaf;  mit  pasaf-:  bis  kapta pasvS  °ya  .  .  nisirinuyHt  V.  14~  16;  — pasius  *g3r>bul  'yiie  V.5. 38;  —  koU. 'pecus  ovillum':  pasiui  °yche  pawm  Y.  2. 24.  A)  als  Subst  'Schaf:  hazanram "yanqm  frSvinuyJl  vtspanqmca  aitaisqm pasvqm  ,.  V./Äyo;  —  saUm  aspanqm.. /lazaanm  gavqm  ba^oarj  "yanqm  Yt  5. 2i;  0.3,  V.i'2.4;  —  niiinmn  staor?m bisazy.lt  "malm  anj5  V.  7. 43;  43;  — 'yanqm  arsnqmV  .22.20.  a)  sva. 'Schaf- fleisch': hazat3nm  gSus  j^anüiiiqm  (sd.) baivan  'yanqm  H.;.s'*.
5398:Pü! Tarii!  i.ä:r,t.  ^  •)  Vgl.  sumü/,  Rv.  j.  32. 7 1  N-  *5;  "  -  ■  "TriAam  mazyät  gava  dmu und  Panihi  4.  1.  67.  1 "/?  V.  j.  42 ;  42  ^;  —  nmUnS^aillm  bisazyat
7315:—  ii^ravamm  bisazy<ll{%A.')  dahmayä^ pars äfrimitN.  7. 41  ;^'?.  37,  Sl.  13. 43  Z.  a)  mit dahma-  oder  mit  d°  und  vauhai'-  Bezeich- nung des  60.  Kap.  des  Yasna:  dahma "tii  Y.60.  Überschr.;  — ■  dakmaheca  tiars alaonS  dahmqm\ca\  vaauhim  °tim  V.  6/. I.  A)  mit  dahma-  und  vavhav-  als Gottheit  ■'>;  alät  dim  aiwysiti  y,l  dahma vanhi  "tis  ultrahe  kthrpa  P.J2;  —  dah- tnqm  vanuhim  °/;i»Y.2.iS,7.a6,  P.j_j"; — dahmaya  vatahuya  °töil\.i.\<„  7.26,  8.\, 70.3.  2)  'Verwünschung*:  agvaht  .  . ana/aonS  zänu.dräjä  asti  °tii  "die  Ver- \vünschung  eines  . ,  Ungläubigen  geschieht durch  Vorstrecken  des  Kinns"  V. /<V.ii.
8705:—  'saiihqm  para  frSritSii  FrW.  /0,4i ;  — ytzi  xsapsAva  mpr^ncaiie  (sd.)  'lakva bisazyat  V.  l'7.3J  —  uü'  (LS.).  A)  als weibliche  Gottheit  gedacht:  'sqm  (AS.) sriram  yazamaide  'säuAfm  . .  xsSi'inJm ravaLaspqm  .  ,  "säPikem  .  .  nvim  ranjat.- aspqm . .  avqm  'sqm . .  G.  5. 5.  a)  Name der  fünften  und  letzten  der  (priester- lichen) Tages  abteilungen*';  vupim  paiti "sauham  ä  kB  vaxsat  "immer  in  der Morgenfrühe  bis  Sonnenaufgang"  V.  /y. I.  3)  mit  süra-  Adj.  Name  des dritten  Abschnitts  der  Nacht**':  hö tiurr/ö  (j'S  parö.dars)  väHm  baraili  upa 'iaukim  yqm  särqm  V,  iS.  15;  —  'sqm särqm  V.2j\}.
9270:irisyst  (soll  heissen)  "sie  sollen  nicht  an M.  OperationeQ  austUhren,  und  nicht  soll  er durch  Operationen  Schaden  tun,  .  .  .  wenn sie  Operiren,  wenn  er  durch  Operationen Schaden  tut"  V.7,38;  —  vasö  "k^r^iitu'^ masdayama  vüsS  "ipr^tu''  bisazyät  (soll heissen)  "nach  Belieben  sollen  sie  M. opcriren,  nach  Belieben  soll  er  durch  Ope- rationen heilen"  V.  7,40.
9296:Pii, :  ke  pa  kirt  biSaziiüt.   —  ')  S  ^OJ  H-  43-
13305:•  j.  dätö.baeSaza-  Adj.  '(Arzt,)  der  mit dem  Gesetz  heilt' :  a!5.balsaz3  -zö . .  inq'irB.- balsasd  (sd.)  Yt^.  6.
16262:•  j.  pouru.baesaza-  Adj.  i)  'reich  an  HeÜ-
16500:baesaza.kai-
16508:KompA.,  E.;  Ableit.  —  lEt  s.  bisas-.  —  aL bhtfajä-  1)  Adj.,  2)  n.i  »p.  bisazali;  rp.  vgl biäli  'Aril'.  —  Pa.i  btiaziin,  bSatimih,  iiia- zinUniA.  —  0  Sicher  Yt.  T4.  34.
16509:•  j.  baeSaza.ksä'  Adj.  'Heilung  bewirkend, schaffend':  nava  bai^asä  navata  'ktsa (NPn.)  ■>  "(wieder)  frisch  (werden)  die  Ar- zeneien,  frisch  die  Heilung  schaffenden (Mittel)"  V.2J.3.
16513:•  j.  baeSazai  Inf.  'zu  heilen':  frä  äbys tanubyS     haomS     vuaite   (sd.)    b'    Y.  j
16530:•  j.  baeSazyö.tara-  Adj.  (fem.  'rä-)  'der heiltätigere':  fravasayS  .  .  yä  "ri  (NPC) ahmät..yaha  vaca  framraväire  [sd.)  Yt 13.  64.
17312:•  j.  biäaz-  den.  Praes.  32  'heilen'. 'Jemanden  (Akk.)  heilen,  kuriren,  ärzt- lich behandeln':  a^ravansm  bisazyät''^ dafimayilt  pars  il/riiöit  "einen  Priester  soll man  um  einen  feierlichen  Segensspruch kuriren"  V.7.  41;  41—44'*,  40";  —  -t»So  tl azitn  bisazätti  ku%a  ..  *apavarsne  navaca yasks  . .  "wie  soll  ich  dich  (Sp.  789  m.) heilen,  wie . .  beseitigen  die . .  Krankheiten?" V.  22. 6;    —    ohne  Obj. :   yai    anza/iva
18911:\paiti  nars  aSaorUS . .  °kala  apsnnsyäkasca varai^rm  (sd.)  pantqm  atBit  V.J.  11;  3; —  ,.  zaohrata  (sd.)  ratufris  'käscit  (GS.) apgrmäyükahecit  N.  .^0;  —  yS  anyahe'ka (IS.)  ..yS  anyehe  ^apirmSyüka  *anakaxt/T a'haurUTifm  *parar>kacaiti'ü.6i.;  6; — yHi.. 'kqm  vä  *ap}nnäyük>m  (vS)  a/t?m  dasli N.  105; —  'ka  kasujcra%wa  (sd.)  ^.40;  — ava%a  Ag  x"atg  (sd)  pu%rytn  ankat..aat yai  hvqtn  'ka^^  bavaiti(sd.)  ..yai dirftrqm \AfntiYd.2\  —  dahma  •^rf(NS.?)  ap^rma- yüke  kainike  Y.2^.3;  —  katärS  (sd.) '  a%aurumm  *parayat  'ka  va  nmänS.paiti^ va  N.5;5,  *5'>j — yai . .  nmanahe  nmOnB.- paitlm  'kam  .  .  daiöÄSui  daiiikupaitim 'kqm  bisazyätY.j.42;42',  is.$&.  a)mit asavan-  (Sp.  250  m.):  nanm  aiavanjm  . , 'kqm  a^aonlm  V.p.  33,  42,  75.12,  26,  rr.i, 2/7,  10  (statt  Ab!.),  Vr.j.4,  G.4.9;  — tat  asti  yUnO  . .  a^arihim  , .  tat  -kayai  . . ratuxsa^ray'ai  asaonyäi  H.  z.  1 8 ; — 'rikayh aiaonyä  Vd.  4-
20468:•  j.  '*'m^0'r«in.sp9iit«[n.baeSaza-*)  Adj. 'der  mit  dem  heiUgen  Wort  heilt,  kurirt': tim  ihra  AanjasätUe  yat  'tarn  "sie  sollen sich  an  den  wenden,  der  . ."  V.  7. 44.
30683:aiöis  baesaza  . .  g^mJra^avAa  (sd.)  äänu.- äräjanha  'zanka  (APn.)'>  Y.6'0.4.
=== BRT badra ===
```


## [2026-09-05T06:04:31.791Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB glossary besaz ===\"; grep -n -i -E 'be[sš]az|bi[sš]az|pizi[sš]k|be[sš]a[czk]' NYB_vol2_glossary.txt | head -40"
}
```


### [2026-09-05T06:04:31.839Z] TOOL RESULT

```
=== NYB glossary besaz ===
1006:bizišk [bešk'] a medicine-man, a physician, pl. cas. obl. ~-dn in yātūk- -ān witch- doctors 43%, — Olr. "bišaz-ka- (cf Skr bhisaj-, whence in NW (with meta- thesis) "bizaška- > bizišk (MPrth v. next w.; Arm. lw. bžišk), in SW *bisadka- > *bisa0ka- > bišihk (MPrs bšyhk). In NP the NW form bizisk, later pizisk.
7333:pizišk: bizišk
```


## [2026-09-05T06:04:47.834Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BRT 16495-16535 ==\"; sed -n '16495,16535p' BRT.txt; echo; echo \"== BRT 17300-17330 ==\"; sed -n '17305,17325p' BRT.txt"
}
```


### [2026-09-05T06:04:47.905Z] TOOL RESULT

```
== BRT 16495-16535 ==
•  j.  baeSatastura-  patr.  Adj.  'von  BaSsata- stura'-'>  abstammend,  dessen  Nachkomme': fratura  asntta  'rä  (GS.)  asaomJYt.  13.12$.
Ableit  (mit  Verschiebung  des  Wortakzents) aus  *baFiata'ilura-')  a>.  EN.  (Bed,?  *baeJoia- vU.  PFP.,  s.  bii-  und  *mtmataseura-).  —  >)  S. aber  No.  2.  —  »)  Oder  aber  aus  *iiSo/os/ura; zn  S  /00  a.  B?
•  j.  bae^aza-  1)  Adj.  (fem.  'sr-)  'heilend, heilkräftig,  heiltätig';  a)  von  Mond  imd Sternen:  mawi^m  ..  bay>m  'Km  Yt". 5;  —  vanantim  stär>m  .  .  °wm  Yt  21. 1.  b)  sonst:  als3  , ,  asti  °zanqm  bag- sai:yS.t)mö  yat  *mq%r?m.sp>nt»m.batiasyB V.7.44;  zitYtj.6;  —  mq^ranqm  'am .  .  bal^atyBJimim  Yt  J.  S;  —  vaca  ars- uxoa    van'hrayms    'zis    (APf?)   YtJÄS;
dby  Google
915
baesaza.kai-
baog-
916
8,  3)  n.,  m.'';  a)  'Heil-,  Gesundheits- mittel,  Arzenei':  avaüa  he  't?m  upsisay?n ya%a  dahmaUi^  "in  einem  solchen  Fall sollen  sie  ein  Heilmittel  für  ihn  ausfindig 2U  machen  suchen,  wie  für  einen  D."  V. y-  3S;  —  ^  '^  (näml.  haomahe)  Sa  (NP.) irlra'i arf  {sd.) ..  Y.io.  12;  —  haoma  dasdi ml  'zanqm  yäbyS  ahi  baisazma  (sd.)  V. 10.  9;  6t<.  15',  Yt  13.  13s;  —  aslm  .  . baryntlm  vupä  "sä  (AP.)  apqmca  gavamla ttrvaranamca  ". .  alle  Heilmittet  der  Wasser, Tiere  und  Pflanzen"  Y,  52.2;  —  nava  'za (NP.)  V,  2/.  3 ;  —  fravaiayö  .  .  a^is  -za (AP.)  hanmni  Y.  60.  4;  Vr.  <?.  i',  2,  F.  16,
dämqn  baisasyatica  Yt.Ä43;  —  Bat  mqm tarn  *baghsyöii'i  V.  22,  2,  9;  —  baliazySi Yt.j.63). Ableit.  aus  batsata- ').  —  Vgl.  biiat'-  —   Pü. : bisaxitiitan.  —  >)  Es  ist  nicht  unmöglich,  dus baeiaxya-    aus   ar.  'Miiasiu-   (•=  ai.  bhifejya-) unter  demEiofluss  von/df/iizii-hGrvoTgegaiigeD ist;  vgl.  tisas-  No.  i.  —  *>  So  K  1,  L4;  NA. &j".  —  3)  Vgl.  bHas-  No.  *. •  j.  'baeäazya-  Adj.  (fem.  °sya-)  Tieilend, heilkräftig,  heiltätig';  a)  von  Göttern,  Ster- nen, Wassern,  Pflanzen  udgl.:    °zya  (statt NSm.)  ftqma  ahmt  (näml.  AkM.)  . .  bae- sasyü.t>ma  Yt  j.  1 2 ;  8 ;  —  kaomS  .  .  'zyJ Y.p.i6,  57.19; —  haomahe  'zyehe  '^.10.
YtÄfio.       o)iiberhaupt'Hilfsmittel,Hitter:j  7;    —  fravalay5  'zyä  YLij.30,  3a;
(1/  (Sp.  423  u.)  aii^he  asti  'zö  "was  gibls da  für  ein  Mittel?"  Yt/4.34.  b)  'Heil- kraft': 'sa  (IS.)  ahmt  balsazySJfms  Yt.  14. 3.  c)  'Heiltum';  barat  (näml.  väts)  -am Uta  amtm^a  Yt  14. 2 ;  Fr.  g.i.  a)  insbes. in  Verbindung  mit  dasvar-  (Stverz.):  dasva- rna   'z>mca  (NS.)  V,  p.  53;  usw.  -ziii
als  Inf.  sbes.  [V.  7. 44:  lies  mäimm.- sp}nt}m  .balsaam.]
KompA.,  E.;  Ableit.  —  lEt  s.  bisas-.  —  aL bhtfajä-  1)  Adj.,  2)  n.i  »p.  bisazali;  rp.  vgl biäli  'Aril'.  —  Pa.i  btiaziin,  bSatimih,  iiia- zinUniA.  —  0  Sicher  Yt.  T4.  34.
•  j.  baeSaza.ksä'  Adj.  'Heilung  bewirkend, schaffend':  nava  bai^asä  navata  'ktsa (NPn.)  ■>  "(wieder)  frisch  (werden)  die  Ar- zeneien,  frisch  die  Heilung  schaffenden (Mittel)"  V.2J.3.
'ti's-  Adj.  ■niacbcnd',  tarn  V.  ^kar—,  ai.  *kfi- Adj.;  S  '7'-  —  Pö-:  bisasiitük  iarlärih,  erL : auisär.  —  ')  Them.
•  j.  bae§aza-3ä-  Adj.  'Heilung  schaffend': datdi  ml  bal^azanam  yäbyd  ahi  '\h  (NS.) "gib  mir  von  den  Arzeneien,  durch  die du  Heilung  schaffst"  V.  10. 9.
Pü. :  beiatimlär.
•  j.  baeSazai  Inf.  'zu  heilen':  frä  äbys tanubyS     haomS     vuaite   (sd.)    b'    Y.  j
as[m  . .  'syqm  Yt  ij.i;  —  drväspqt
°syqm  Yt  p.  2 ;    —    arfdvTin  .  .  'syqm  Y.
(5j.  I ;  —  HiirTm  .  .  'Um  Yt.  S.a;—  stärd
ySi  haptSiritiga  . .  'tya  S.  r.  13;  2,  13;  —
äpö  .  .  'zya  YtA47;  —  urvarä  'zyi  V.
10. 4.         b)  sonst:  vS^5  . .  pailiMsis{%A.)
'zya  Y. 10.18;  Ytr5.s6,  V./0.5;  —  v<^^e
\ySi  . .  'zya  as  Yt/4.40;  —  växl .  .  'zyS
FrW.5. 1;    —    %rimahe  ..   'tyehe   Yt /5.
so;  — gavafttlm^a  °>yqm  Yt  10. 15.       [V.
7.  44:  lies  mq%r3m.sp3nt3m.baiiazys\
KompE.;  Ableit.   —    Ableit.  aus  bariaia-.  —
ai.  bh4iajyä-   Adj.    —    Pü. :    beiaiiitüSr,    So. :
arogyaiarah.
•  j.  ^aeiazyäi')  Inf.  'zu  heilen,  Heilung zu  bringen':  äia  tiB  jamyät  b'  Yt/0.  5,
Zum  Praes.  31  iaelatya-.  —  <)  So  alle  guten Hds.  (Bthl.  BB.  /j.  22S)  gegen  'läS  der  NA.
•  j.  baeSazyö.tara-  Adj.  (fem.  'rä-)  'der heiltätigere':  fravasayS  .  .  yä  "ri  (NPC) ahmät..yaha  vaca  framraväire  [sd.)  Yt 13.  64.
Kompar.  aus  batsasya-.
•  j.  baeäazyö.tuma-  Adj.  'der  heilkräftigste,
heiltätigste';    a)  von  Göttern:  balsazya  . .
°ma  (statt  NS.)  nqma  ahmt  (jäsaL  AhM.)
Vt;.  12;    —    ial/aza   ahmt  (nämL  Vtr^

== BRT 17300-17330 ==
ma-  Adj.  'der  unter  den  vom  Zweifiissler abstammenden  am  meisteti  vom  Zweifiissler abstammt*:  °mp/n  janät  "mtm  tbaäayat Yt.J.  15.
•  j.  bU  Adv.  'zweimal':  b'  frasn^aym Ttiassmana  .  .  %ris  .  .  ca'hru/  .  .  xsiial V-7-75;  TV,—  y^ris  abm  upastuyät  b- Aumalanqm  "dreimal  soll  er  das  mit  A., zweimal  das  mit  H.  beginnende  Gebet aufsagen"  V.7Ä43;  ig.22(f);  —  b'  hapta^^ nmäna  "zweimal  sieben  Häuser"  V.  75.  45; Z^.  6,  i63;  —  b°  aSavat  hii^nm  yaval tacanm  "zweimal  (genommen)  ist  ein  Ä". sovieIals.."F.27a;  27a.  a)  mit  Gen.: b'  aitavaiff  "his  tanto"  V. /_j.  30.  "b" pay  b'^  N.<?(^(PJ.
KompA.;  Ableit.  —  Vgl.  -A-o-  und  *.■•;  S  88.
—  Pü.  (luV.  18):  3  bar,  (sonst):  ?.  —  ')  Vgl.
•  j.  bii-  t  'Heilmittel'.
KompE.;  Ableit.  —  Vgl.  biiis'.  bUoi',  baesas'.
—  ai.  vgl.  bhfsajä-   Adj.  'heilend',    n.  'Heil- mittel' usw.
•  j.  biäaz-  den.  Praes.  32  'heilen'. 'Jemanden  (Akk.)  heilen,  kuriren,  ärzt- lich behandeln':  a^ravansm  bisazyät''^ dafimayilt  pars  il/riiöit  "einen  Priester  soll man  um  einen  feierlichen  Segensspruch kuriren"  V.7.  41;  41—44'*,  40";  —  -t»So  tl azitn  bisazätti  ku%a  ..  *apavarsne  navaca yasks  . .  "wie  soll  ich  dich  (Sp.  789  m.) heilen,  wie . .  beseitigen  die . .  Krankheiten?" V.  22. 6;    —    ohne  Obj. :   yai    anza/iva
31*
dby  Google
967                  bi&amrüta-                       —  buna-                     968
M^fTn/aüe (sd.)  xlttf>eJtva  biianif^  V.2;.  VgL  gr.  ^^t^u  nhd. /.».■*«;  Bete  KZ.  39.
..  ,*  3&4-     Aber  die  Herkimri  des  Wortx  ist  rer-
Ableit.    ans   ai.  'hhi^a't-  m.  'Ant'j);    «i.   ^«-  ^'^''•'E-
joM 'erheUt',  Miii!:*  (NS.) 'Arzt',  —  VgL*j^  •   j.  bucah'in-    Adj.   'der   das  Geheule,
ia^a-  den.  Praes.  und  <ifl«flii.-  Inf    —    Tu.:  Gesuche  an  sich  hat":  ';aki  (NS.)  juäij
*,«K«Sfl,.    _    .)  Opt.,   oder  «ich  Kon>«  ^^;  buxtiS  njnia  ahf-i  Vtiv47.      '
SUH   to^-T^if  d«   NA.,   da.   =i.,en    sölcheD  ^^'''L''  ""     "  "*'  ""i  »^  *"  '■"''-^-
Praeseiisstanim    enreiseo   «örde,   ut   besser  •  }.   bujay- £  Name  cinei  X)a^cl•.  nasüm
baTi'  \a    lesen;    vgL   ij,^/a:j-fl.    "^1-  ^,  3.  —  janat ,  .  *ji  Janat  \\.  4.^;  —  bü'at  nonm
—  J)  D.  1-  Ableit.   ans   ai.  Hhxi-  (,Tgl.  *isi-\  ' S  V*  b.  a.  -  -     f  ).
```


## [2026-09-05T06:04:49.699Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD ==\"; grep -n -i -E 'bize[sš]k|bi[sš]e[sš]k|be[sš]az|bizi[sš]k' PHD.txt PHD_mackenzie.txt | head -20; echo \"== HRN ==\"; grep -n -i -E 'pizi[sš]k|pize[sš]k|bizi[sš]k|be[sš]az' HRN.txt | head -20; echo \"== HUB ==\"; grep -n -i -E 'pizi[sš]k|bizi[sš]k|be[sš]az|bi[sš]az' HUB.txt | head -20"
}
```


### [2026-09-05T06:04:49.796Z] TOOL RESULT

```
== PHD ==
PHD.txt:255:bayaspānīh 18 bizešk
PHD.txt:1669:doctor bizešk.
PHD.txt:3116:physician bizešk, drustabed.
PHD_mackenzie.txt:1562:besaz(en)- [by.ez(yn)-, byfC)c6'n)- I M byez-] heal, cure.
PHD_mackenzie.txt:6406:direct (a.) rast.                       doctor bizesk.
PHD_mackenzie.txt:6745:habitation mehmanih.                     heal besAz(en)-.
PHD_mackenzie.txt:7038:manna tabarzad.                            medicinal besaz, bijagan;       plant
PHD_mackenzie.txt:11203:besaz-           -~\                          pas[
PHD_mackenzie.txt:11208:besazenisnih   AU~~,                          darhandarzbcdI   \¥'eu~",*~\
PHD_mackenzie.txt:11209:besazisnih      ~~)                           darband     f
PHD_mackenzie.txt:11211:besaz-                   -vuw\                hay
PHD_mackenzie.txt:11216:besazisnih      "'Ut"'U~)                     bayaspanig        \~""'~\
PHD_mackenzie.txt:11222:besaz-                    -ou.-,              bcwar                           ~t-\
== HRN ==
11888:biziski 183.
15710:besazcfk 183.
15711:besazimtan 183.
15712:besaztnUär 183.
== HUB ==
4493:*VVelt'); bizisk Arzt' s. p. 128; bisyar Viel* ebenda.
6379:p. 26; biziSk *Arzt' H. 183; baxt ^Schicksal' H. 185; baxsi-
7999:Jbijisk^) = bizisk *Arzt': zd. baesaza- (aber skr. bhisaj-, hhi-
8212:bijisk = bizisk 'Arzt' aus "^bimk fiir *bisizk, vgl. § 112;
8229:(ba^at) zutheilen', skr. bhaj; bzisk 'Arzt' = phi. *bizisk
8591:*trocken = ap. uska--^ bizisk 'Arzt*, arm. hmk (vgl. bal.
```


## [2026-09-05T06:04:54.475Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -E '^ *183\\.|183\\. *bizi|bizi[sš]k' HRN.txt | head; echo \"---\"; grep -n 'bizi' HRN.txt | head -20"
}
```


### [2026-09-05T06:04:54.535Z] TOOL RESULT

```
11888:biziski 183.
---
2254:kurd. bizin ; af/. wuz ; bei. LW. bfiz (37) ; wa;^. buc,
6024:Dazu vielleicht auch hedi, d. i. ein aus bizi ver-
11888:biziski 183.
```


## [2026-09-05T06:04:54.971Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7990,8010p;8205,8235p' HUB.txt"
}
```


### [2026-09-05T06:04:55.017Z] TOOL RESULT

```
Dafiir sw, zn in dem LW. aus dem Avesta : arm. maz-
dezrij mazd^zn *Mazdayasnier, mazdayasnisch', phi. mazdesn
oder mazdayasn^ inschr. M-zd-y-sn, chald. phi. M-zd-y-zn
(Haug, Essay on Pahl. p. 4, 49, 50), gr. MaaSadvov {gen,{i
zd. mazdayasna- ^Mazdayasnier , mazdayasni- mazdayas-
nisch'.
Np. z aus iran. z wechselt nur selten mit i, j: nizad
'Geschlecht, Abstammung ■= zd. *nizati'\ biij neben buz
*Ziege, Bock*, zd. buza-; diz neben diz *Burg', ap. dida-;
Jbijisk^) = bizisk *Arzt': zd. baesaza- (aber skr. bhisaj-, hhi-
sakti' ?). Ueber z = z aus iran. / siehe Kap. 22.
Kapitel 21: ap. 6.
§ 113. Ap. G (= idg. F vor hellen Vokalen) ist
a) im Anlaut und nach tonlosen Konsonanten = phi. paz.
np. C] b) im Inlaut nach n = paz. np. /; c) sonst = phi.
c, paz. i, np. 0, selten z^ j,
Im Phi. steht iiberall ein Zeichen, das urspriinglich
den Lautwerth c hatte, aber in den Inschriften schon fiir z
(vgl. vcrk gross) verwandt wird und wohl auch fiir / und
z eintreten musste. Die Pehleviformen miissen daher auf
Grund des Armenisehen, und wo dieses versagt, nach Ana-
arzani 'wiirdig', 3 pr. arze Viegt auf .
c) ap. /, ^ nach Vokalen = np. j^, z, z : bajf = bal =
haz Tribut*, ap. haji-, skr. hhaj\ Uj Tfeil' (Vullers; wo
vorkommend ?) neben tez 'scharf, vgl. tiyra-^ in Komp. tizi-
*scharf, spitz', tiyri- 'Pfeil'; xujasta gesegnet' = zd. */iw-
jasta- neben paz. gazista verflucht' (§ 52, 1); bar^jan =
bar^zan 'Backofen', zu iran. brij *backen' (oben p. 27) ;
bijisk = bizisk 'Arzt' aus "^bimk fiir *bisizk, vgl. § 112;
azdaha *Drache' = zd. azis dahakd-^ farjctm *Ende' aus phi.
frajdm H. 814; bHa^ veza rein H. 253, etym. unsicher
(oben p. 33— 34); maz Treude*, skr. mah (siehe oben p. 97);
diraz 'lang = zd. drajah-; sitez *Kampf', zd. stij- *Kampf' ;
dozax *H5lle' = zd. daozanuha-; Xuzistan = ap. (H)uvja-
oder (H)uvza\ rajfa^ raza, raza oben p. 66; kUZj kuz 'ge-
kriimmt* = skr. kubja- (oben p. 89) , u. s. w. Buntes
Material bei Vullers, Gram. p. 39.
§ 122. Die armenischen Lehuworter haben nach
Vokalen stets z:
arzani Viirdig' u.s. w. § 121 b; azdahak = np. azdahd
§ 121, c ; baz *Zoll, Entgelt, Schicksal' ~ ap. baji- (oder bazi-)
§ 121, c, dazu bazapan (nur Wb.) 'doganiere' = np. bajbOft^
bazban (Fird. II, 740, 1053), bazvan ^exactor vectigalium' ; ba-
zak 'Becher', vgl. zd. bajina- 'Gefass'; bazan- 'Theil' in bazan-em
*theile' u. s. w. , bazin 'Theil, Antheil, Theilung', zd. baz
(ba^at) zutheilen', skr. bhaj; bzisk 'Arzt' = phi. *bizisk
(geschrieben bcsk Shk. 237), umgestellt aus *bisizk § 112;
bii 'Augenbutter, Triefen der Augen' = np. bij 'sordes ocu-
lorum, lippitudo'; buzem 'heile, rette, befreie', zd. buj ab-— 231 ~
legen, befreien, bal. hdjag, bozay *losen'; dazan 'bitter,
herb, scharf, np. dizan^ duzan, dizand^ da&and 'acutus
gustu, acer ; dzox-K 'Holle', up. dozaxy paz. dd£ax Min.Gl.
```


## [2026-09-05T06:05:15.450Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN besaz ==\"; grep -n -i -E 'besaz|bezes|bizis|bijisk' HRN.txt | head -20; echo \"== HRN 183 entry ==\"; grep -n -E '183\\.' HRN.txt | head -20"
}
```


### [2026-09-05T06:05:15.508Z] TOOL RESULT

```
== HRN besaz ==
1997:188. hiziSk, bijisk (*bishk) 'Arzt* (Sahn. I, 32 Vers 180,
11863:bijisk 183.
11888:biziski 183.
15710:besazcfk 183.
15711:besazimtan 183.
15712:besaztnUär 183.
== HRN 183 entry ==
11863:bijisk 183.
11887:ft/^Ä 183.
11888:biziski 183.
15020:fraspareya- 183.
15039:6o<?Sfl2frt- 183.
15710:besazcfk 183.
15711:besazimtan 183.
15712:besaztnUär 183.
15713:bB8az(0smh 183.
15718:\hja8kih 183.
17958:6Aiä^- 183.
17960:bheiajA- 183.
18646:g. pedesk 183.
22157:bzjsk 183.
22158:bzskutiuu 183.
```


## [2026-09-05T06:05:16.690Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SOD byc ==\"; grep -n -E \"byc|bys'|bysk\" SOD.txt | head -30; echo \"== SOD pages byc ==\"; grep -n -E '\\bbyc\\b' SOD_pages.txt | head -20"
}
```


### [2026-09-05T06:05:16.745Z] TOOL RESULT

```
== SOD byc ==
27555:3039  bys'  C  Jj^<£> 
== SOD pages byc ==
```


## [2026-09-05T06:05:24.362Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1990,2020p' HRN.txt"
}
```


### [2026-09-05T06:05:24.401Z] TOOL RESULT

```
r
W82. but ^Götzenbild; Liebchen.
aw. Büiti- N. pr. ; phlv. Büt, Bütjan (Gemme, Hörn,
Mitteilungen, Heft IV, S. 40, Note).
Wenn die Zusammenstellung richtig ist, so gehört
np. but in dieselbe Kategorie wie gStl^ ätes, petyäre
u. a. m.
188. hiziSk, bijisk (*bishk) 'Arzt* (Sahn. I, 32 Vers 180,
182), bmski (Sahn. I, 25 Vers 43).
aw. baesaza^ 'Arzenei, Arzt'; phlv. bBsazak (PPGl.),
*) Tiger kommen in den kaspischen Provinzen Persiens vor.
Vergl. W. T. Blanford, The Zoology and Geology, Vol. II von Easteni
Persia, An account of the journeys of the Persian boundary com-
mission 1870—1-2, London 1876, Seite 34, ein Werk, das ich für ähn-
liche Fälle öfter zu Rate gezogen habe. Leider führt es meist die
persischen Worte selbst nicht an.
') PPGl. popr^ paprä wird Justi natürlich nicht meinen; pepere
des FJ ist eine wertlose Päzendschreibung.— 4:^ --
heSaz(i)änTh, bSSuzlnUan, bSSazlnUär und auch b(i)jaskth,
vd. 7 (94) ') ; ai. bhiSdj- *Arzt', hh^aja- *Arzenei\
arrn. LW. b^sk, b£skutiun.
g. pedesk (Houtum-Schindler) kann kaum hierher-
gehören.
184. bebe, beööe *Junges (von Tier und Menschen)' 2).
g. vaöe; Käs. veöd, veöi etc.; mäz. vaöa.
phlv. vaöak (vd. 14 (53) GL), baöak (vd. 19 (99) GL;
vd. 6 (17) flf., 'Glied des Fingers)»).
kurd. vacdhä *Familie' (H.-Sch.); oss. d. mss 'Kalb'
(79); bei. gvask *Kalb' (142); wa/. vmk^ sar. visk *Kalb'.
In der Bedeutung *Knabe' entlehnt in oss. d. biÖeu,
bifbeu (Hübschmann, Seite 121), bei. baiak (17),
```


## [2026-09-05T06:05:25.384Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -E 'physician|doctor' SOD.txt | head -20; echo \"=== around 117 ===\"; grep -n -E '^ *0?117 |^117\\b' SOD.txt | head"
}
```


### [2026-09-05T06:05:25.459Z] TOOL RESULT

```
24269:physician 
27186:physician 
27200:god  of  physicians 
31489:physician 
90020:god  of  physicians    2974 
92531:physician    2518,  2972,  3616 
=== around 117 ===
6427:117.  Sec  GMS,  p.  457,  u  1. 
8343:117  »Yy8-  M  o^Jj^y^^y- 
27115:117 
43073:117 
80778:117;  BSTii:  C2  p234;  KG  477;  inf.  xwryy,
```


## [2026-09-05T06:05:37.927Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 2518 2972 3616 3039; do echo \"--- $n ---\"; grep -n -E \"^ *$n  \" SOD.txt | head -3; done; echo; sed -n '24260,24275p;27180,27210p;31480,31495p' SOD.txt"
}
```


### [2026-09-05T06:05:39.666Z] TOOL RESULT

```
--- 2518 ---
24266:2518  p>yc    B  J^^ 
--- 2972 ---
27182:2972  Pyc   B,M  v*J*<^Ji 
--- 3616 ---
31486:3616  Srwtpt   S  (j/^  xU)^Ci>7 
--- 3039 ---
27555:3039  bys'  C  Jj^<£> 


(breach 

VJ  743  n  p94;  Hen.  BSOAS  12.309,  Benv.  "to 
follow" 

2518  p>yc    B  J^^ 
Pec   =»Pyc 

physician 

TSP  6.186,  187,  JFycyw  ?  8.105  n  p216 

2519  p>ym 

Pern   ©lpl.  pres.  subj.  *=»P- 
SCE  236 

2972  Pyc   B,M  v*J*<^Ji 
Pec   ©<Av.  baesaza  ©ob.  pi.  ~ty   =*pyc>n 

ywt}w,  p>yc 
physician 

SCE  272;  GMS  384;  flycty,  BBB  517;  gen.  pi. 
fiyc%  TSP  9.78,  95;  GMS  1230 
2973pyc>n>k   B  >^>, 

Pecane   ©adj. 
medical 
TSP  9.80,  81,94 


2974  pye'n  ywt'w   B,  S  (/u^j(5Cij,)  jl£ij,^lj£- 
pecan-xutaw 

god  of  physicians 

GMS  1230;  TSP  9.78.95;  SCE  272 

2975  pycy'h   M  ^<J^Jl 
Pecya   (Pycyh)   ©f.  n. 

medicine 

GMS  1111;  Sogdica.  39.35;  TSP  8.198;  BBB  517 

3615  5rwth   S  P^u^j^j 
Srut   ®<*drwata   =»dwrt()),  s8m(=SLM) 
health,  greeting 

MDii  p200 

3616  Srwtpt   S  (j/^  xU)^Ci>7 
Srutpat   ©pr.  name 

physician 

MDii  pl85.27,  200;  MDiii  p93,  199 

3617  Srxwsk   S  >/^<j^> 
Sraxusk,  zuxsk   ©*6rigus-ka   ©nom.  -y;  pi.  -t\
```


## [2026-09-05T06:05:48.113Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '\\[pdf page' SOD_pages.txt | head -3; echo ---; grep -n -E '2972' SOD_pages.txt | head -5"
}
```


### [2026-09-05T06:05:48.174Z] TOOL RESULT

```
---
12246:2972 Pyc B,M                                                 2984 pyjypr'n =* ,pyzypr,n
39076:parents 4475, 5247                       penitent     5981                         physician      2518, 2972, 3616
```


## [2026-09-05T06:05:51.498Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n++} /2972 Pyc/{print \"form-feed page (1-based):\", n}' SOD_pages.txt; echo ---; awk 'BEGIN{RS=\"\\f\"} /2972 Pyc/{print}' SOD_pages.txt | head -30"
}
```


### [2026-09-05T06:05:52.885Z] TOOL RESULT

```
form-feed page (1-based): 183
---
                                                                                                                        byq




 117

 2964 py'r'k S                                       0l£>U    2974 pye'n ywt'w   B, S        (/u^j(5Cij,) jl£ij,^lj£-
       Pyarc (Py'ryy) ©ace. bfrw ^'py'rh                           pecan-xutaw
       evening                                                     god of physicians
                                                                   GMS 1230; TSP 9.78.95; SCE 272
       GMS 969; Hen. Tales. 467, 12.3; BBB 697; KG
         541 pl82; C2, 94R21, 22; Hen. Fasts. JRAS            2975 pycy'h M                              ^<J^Jl
         1945, 155                                                 Pecya (Pycyh) ©f. n.
                                                                   medicine
2965 py'rt- B, S                     ^l «> jjTc~o*                 GMS 1111; Sogdica. 39.35; TSP 8.198; BBB 517
     Pyart ? (byrd»r-) ©Yaghn. viyorta ©pt. St.
       -»Pyr-\ 'Py'rt-, Pyrt-                                2976 pycy'kh     B                            v^<^.>,
     (/c>)obtain                                                   pecya(k) ©f. n.
                                                                   medicine
     GMS 90, 593; BSTBL, Dhy. 391; MD; Anc. Lett.
                                                                   BSTBL, Dhy. 229
       4.5; STii 7.6
2966 py'ryy      M => Py>r>k       :                         2977 pycyh B =» Pycy>h
2967 by'tq'rc C                                              2978 by5»nh =» Py5>n
                                               fL> iv»>w
                                                             2979 pytfn B                           j\*ijLJ\<(&
       Pyatkarc
       message, embassy                                           PiSan (byS'nh) ©Av. aivi-dana-, Khot. byan
       Sund. AI 28, 1988, 1.180, 181                                 ^P6»nh
```


## [2026-09-05T06:06:01.761Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AHD bha ==\"; grep -n -E 'bh(a|ā)-|bhad-' AHD_watkins1985.txt | head -30"
}
```


### [2026-09-05T06:06:01.806Z] TOOL RESULT

```
== AHD bha ==
321:yawn, gape: BAY2, BEVEL; ABASH, ABEYANCE. 2. Possibly Vulgar Latin *abbaidre (> Old French (a)baiier), to bay: BAY‘*.] [battuere. To beat. Latin verb of unknown origin. (BATE?), BATTER!, (BATTER’), (BATTERY), BATTLE; ABATE, COMBAT, DEBATE, (RABBET), (REBATE?), (RE- BATO).] bel-. Strong. 1. Suffixed o-grade form *bol-iyo- in Russian bol’shoi, large: BOLSHEVIK. 2. Prefixed form *dé-bel-i- (dé-, privative prefix; see de-), “without strength,” in Latin débilis, weak: DEBILITATE, DEBILITY. [Pok. 2. bel- 96.] bend-. Protruding point. 1. Germanic *pannja-, “struc- ture of stakes,” in Old English penn, pen for cattle: PEN2. 2. Germanic *pund- possibly in Old English pund- (> Middle English pound), pundfald, enclosure for stray animals: POND, POUND3; IMPOUND, PINFOLD. 3. Germanic *pin- in Old English pintel, penis: PINTLE. [Pok. bend- 96.) beu-'. Also bheu-. Appears in words loosely associated with the notion “to swell.” I. Root form *beu-. 1. Ger- manic *puk- in: a. Old English pocc, pustule: POCK; b. Old French po(u)che and Old North French poke, bag: POACH!, POCKET, POKE3, POUCH, (PUCKER). 2. Old Eng- lish pyffan, to blow out: puFF. 3. Old English -piite, “fish with large head” (in aele-piite, eelpout): pouT?. II. Root form *bheu- with various Germanic derivatives. 1. Old English bdsm, bosom: Bosom. 2. Old English biic, belly, pitcher: BUCKBOARD. 3. Frankish *biak (> Old French buc), trunk of the body: TREBUCHET. 4. Old English bye), pustule: BorL?. 5. German dialectal baustern, to swell, akin to the source of Middle English bost, a bragging: BoasT!. III. Root form *beu-. 1. Latin bulla, bubble, round object, amulet (> Old French boule and Spanish bola, ball): BILL!, BILLET!, BOLA, BOULE?, BOWL’, (BULL?2), BULLA, BULLATE, BULLET, (BULLETIN); BOULE- VERSEMENT. 2. Latin bullire (> French bouiller), to bubble, boil: BOIL!, BOUILLON, BUDGE!, (BULLION), BULLY?; BOUILLABAISSE, EBULLIENCE, GARBOIL, PAR- BOIL. 3. Possibly Latin bucca (> Old French boucle, buckle, curl, and Spanish boca, mouth), (inflated) cheek: BOCACCIO, BOUCLE, BUCCAL, BUCKLE!, BUCKLE?; DE- BOUCH, DISEMBOGUE, EMBOUCHURE. 4. Greek boubén, groin, swollen gland: BUBO. [Pok. 2. beu- 98.] beu-2. Root imitative of muffled sounds. 1. Latin bitié (perhaps > Old French butor), bittern: BITTERN!. 2. Latin bited, a kind of hawk: BUZZARD. [Pok. 1. b(e)u- 97.] bha-'. To shine. Contracted from *bhas-. 1. Germanic *baukna-, beacon, signal, in: a. Old English béac(e)n, beacon: BEACON; b. Old English denominative bécnan, biecnan, to make a sign, beckon: BECKON. 2. Perhaps Germanic *bazja-, berry (< “bright-colored fruit”), in Old English berie, berige, berry: BERRY. 3. Germanic *bandwa-, “identifying sign,” banner, standard, sash, also “company united under a (particular) banner,” in: a. Spanish banda, sash: BANDOLEER; b. Late Latin ban- dum, banner, standard: BANNER, (BANNERET). 4. Suf- fixed form *bhaw-es- in Greek phds (stem phét-), light: PHOS-, PHOT, PHOTO-; PHOSPHORUS. 5. Extended and suffixed form *bhan-yo- in Greek phainein, “to bring to light,” cause to appear, show, and phainesthai (passive), “to be brought to light,” appear: FANTASY, (PANT), PHANTASM, (PHANTOM), PHASE, PHENO-, PHENOMENON; DIAPHANOUS, EMPHASIS, EPIPHANY, HIEROPHANT, PHAN- EROGAM, (PHANTASMAGORIA), PHOSPHENE, SYCOPHANT, THEOPHANY, (TIFFANY). [Pok. 1 bha@- 104.] bha-2. To speak. Contracted from *bhaa-. 1. Latin fari, to speak: FATE; AFFABLE, (FANTOCCINI), INEFFABLE, IN- FANT, (INFANTRY), PREFACE. 2. Greek phanai, to speak: -PHASIA; PROPHET. 3. Suffixed form in Germanic *ban- wan, *bannan, to speak publicly (used of particular kinds of proclamation in feudal or prefeudal custom; “to proclaim under penalty, summon to the levy, declare
323:outlaw”), in: a. Old English bannan, to summon, pro- claim, and Old Norse banna, to prohibit, curse: BAN}; b. Old French ban, feudal jurisdiction, summons to military service, proclamation, Old French bandon, power, and Old English gebann, proclamation: BANAL, BANNS; ABANDON; C. Old French banir, to banish: BAN- ISH; d. Late Latin bannus, bannum, proclamation: Ccon- TRABAND; @. Italian bandire, to muster, band together (< “to have been summoned”): BANDIT. 4. Suffixed form *bha-ni in Germanic *b6dni- in Old Norse b6n, prayer, request: BOON!. 5. Suffixed form *bhd-ma in: a. Latin fama, talk, reputation, fame: FAME, FAMOUS; DEFAME, INFAMOUS; b. Greek phémé, saying, speech: EUPHEMISM. 6. Suffixed o-grade form *bhd-nd in Greek phéné, voice, sound, and phénein, to speak: PHONE, -PHONE, PHO- NEME, PHONETIC, PHONO-, -PHONY; ANTHEM, (ANTI- PHON), APHONIA, CACOPHONOUS, EUPHONY, SYMPHONY. 7. Suffixed zero-grade form *bha-to- in Latin fatéri, to acknowledge, admit: CONFESS, PROFESS. 8. Greek blas- phémos, evil-speaking, blasphemous (first element ob- scure): (BLAME), (BLASPHEME), BLASPHEMOUS. [Pok. 2. bha- 105.] bha-bha-. Broad bean. 1. Latin faba, broad bean: FAVA BEAN. 2. Variant form *bha-un- in Germanic *bauné in Old English béan, broad bean, bean of any kind: BEAN. [Pok. bhabhé 106.] bhad-. Good. 1. Germanic (comparative) *batiz6 in Old English betera, better: BETTER. 2. Germanic (superla- tive) *batistaz in Old English bet(e)st, best: BEST. 3. Ger- manic noun *b6¢6 in Old English bét, remedy, aid: BooT?. 4. Germanic verb *batnan, to become better, in Old Norse batna, to improve: BATTEN!. [Pok. bhdd- 106.] bhag-'. To share out, apportion, also to get a share. 1. Greek phagein, to eat (< “to have a share of food”): -PHAGE, -PHAGIA, PHAGO-, -PHAGOUS. 2. Extended form *bhags- in Avestan bakhsh- in Persian bakhshidan, to give: BAKSHEESH, (BUCKSHEE). [Pok. 1. bhag- 107.] bhag-. Sharp. Suffixed form *bhag-ro- in Greek phag- ros, whetstone, also a name for the sea bream: PORGY. [Pok. 2. bhag- 107.] bhaghu-. Arm. Germanic *bdguz in Old English bdg, boh, bough: BouGu. [Pok. bhdghii-s 108.] bhago-. Beech tree. 1. Germanic *b6k6, beech, also “beech staff for carving runes on” (an early Germanic graphic device), in: a. Old English bdc, written docu- ment, composition: BOOK; b. Middle Dutch boek, beech: BUCKWHEAT. 2. Germanic *bdkjdn- in Old English béce, beech: BEECH. [Pok. bhdgo-s 107.] bhar-. Also bhor-. Projection, bristle, point. 1. Suffixed o-grade form *bhor-so- in Germanic *barsaz in Old English bzrs, perch, bass (a fish that has a spiny dorsal fin): BASs!. 2. Suffixed zero-grade form *bhAr-sti- in Germanic *bursti- in Old English byrst (> Middle Eng- lish bristel), bristle: BRISTLE. 3. Extended zero-grade form *bhrs- in: a. Germanic *bur- in Swedish borre, bur, perhaps akin to the Scandinavian source of Middle English burre, bur: BUR}; b. suffixed form *bhrs-dh- in Germanic *bruzd-, point, needle, in Old Norse broddr, spike: BRAD; C. suffixed form *bhrs-ti- in Latin fastig- ium, summit, top, extremity: FASTIGIATE, FASTIGIUM; d. possibly suffixed form *bhrs-tu- in Latin fastus, fasti- dium, disdain (from the notion of prickliness): FASTIDI- ous; e. suffixed form *bhrs-tio- in Russian borshch, cow parsley: BORSCHT. [Pok. bhar- 108.] bhardha. Beard. Possibly related to bhar-. 1. Germanic *bardaz in Old English beard, beard: BEARD. 2. Ger- manic *bard6, beard, also hatchet, broadax (the associ- ation of beard and ax is attested elsewhere in the Indo-European family; both were symbols of patriarchal authority), in Old High German barta, beard, ax: HAL- BERD. 3. Latin barba, beard: BARB!, BARBEL, BARBEL- LATE, BARBER, BARBETTE, BARBICEL, BARBULE; REBARBATIVE. [Pok. bhardhé 110.] bhares-. Also bhars-. Barley. 1. Germanic *barz- in Old
325:English bere, bere, berlic, barley: BARLEY; BARN. 2. Latin far (stem farr-), spelt, grain: FARINA, (FARINA- CEOUS), FARRAGINOUS, FARRAGO. [Pok. bhares- 111.] bhasko-. Band, bundle. 1. Latin fascis, bundle (as of rods, twigs, or straw), also crowd of people: FASCES, FASCICLE, FASCINE, FASCISM. 2. Latin fascia, band, fillet, bandage: FASCIA, FESS. 3. Probably Latin fascinum, fascinus, an amulet in the shape of a phallus, hence a bewitching: FASCINATE. [Pok. bhasko- 111.] bhau-. To strike. 1. Germanic *bautan in: a. Old English béatan, to beat: BEAT; b. German bosseln, to do odd jobs: BUSHEL?. 2. Germanic *bautilaz, hammer, in Old English bietel, hammer, mallet: BEETLE’. 3. Germanic “bitaz in Old English diminutive buttuc, end, strip of land: BUTTOCK. 4. Germanic *butt-, name for a flatfish, in Middle Dutch butte, flatfish: HALIBUT. 5. Germanic *buttan in Old French bo(u)ter, to strike, push (> French bouton, button): BOUTON, BUTT!, BUTTON, BUTTRESS; ABUT, REBUT, SACKBUT. 6. Variant form *bhit- in: a. Latin confiitdre, to check, suppress, restrain (com-, intensive prefix; see kom): CONFUTE; b. Latin refiitdre, to drive back, rebut (re-, back; see re-): REFUTE. [Pok. 1. bhau- 112.] bhé-. To warm. Contracted from *bheo. 1. Suffixed zero-grade form *bha-to- in Germanic *batham in Old English beth, a bath, and its denominative bathian, to bathe: BATH!, BATHE. 2. Suffixed zero-grade form *bha-g- in: a. Germanic *bakan in Old English bacan, to bake: BAKE; b. Germanic *bakkan in German backen, to bake: ZWIEBACK. [Pok. bhé- 113.] bhedh-. To dig. 1. Germanic *badjam, garden plot, also sleeping place, in Old English bed(d), bed: BED. 2. O-grade form *bhodh- in: a. Latin fodere, to dig: FOSSA, (FOSSE), FOSSIL, FOSSORIAL; b. perhaps Greek bothros, pit: BOTHRIUM. [Pok. 1. bhedh- 113.] bheg-. To break. Akin to bhreg-. Possibly in various Germanic forms. 1. Germanic nasalized form *bang- in: a. Old Norse banga, a hammering, akin to the probable Scandinavian source of English BANG!; b. Swedish dia- lectal bangla, to work inefficiently, akin to the possible Scandinavian source of English BUNGLE. 2. Possibly Germanic nasalized forms *bankiz and *bank6én-, bank of earth (possibly < “feature where the contour of the ground is broken,” escarpment, riverbank, possibly also associated with “manmade earthwork’’), later also bench, table, in: a. Old English benc, bench: BENCH; b. Old Danish banke, sandbank, akin to the Scandinavian source of BANK}; c. Old High German banc, bank, bench, moneychanger’s table (> Italian banca): BANK?, BANT- LING, BUNCO; BANKRUPT; d. Old French banc, bench: BANK, BANQUET; @. Provencal banca, bench: BAN- QUETTE. [Pok. bheg- 115.] bhegr-. To run away. 1. Germanic *bakjaz, a stream, in Old Norse bekkr, a stream: BECK?. 2. Greek phebesthai, to flee in terror, forming phobos, panic, flight, fear: -PHOBE, -PHOBIA. [Pok. bhegy- 116.] bhei-'. A bee. Germanic suffixed form *bidn- in Old English 6é0, a bee: BEE}. [Pok. bhei- 116.] bhei-2. To strike. 1. Germanic suffixed form *bili- in Old English bile, bird’s beak: BILL?. 2. Germanic suffixed form *bilja- in Old English bil), sharp weapon: BILL’. [Pok. bhei(a)- 117.] bheid-. To split; with Germanic derivatives referring to biting (hence also to eating and to hunting) and wood- working. 1. Germanic *bitan in Old English *bitan, to bite: BEETLE!, BITE. 2. Zero-grade form *bhid- in: a. Ger- manic *bitiz in Old English bite, a bite, sting: B1T?; b. Germanic *bitén- in Old English bita, a piece bitten off, morsel: BIT!; c. Suffixed form *bhid-ro- in Old English bit(tjer, ‘‘biting,’’ sharp, bitter: BITTER. 3. O-grade form *bhoid- in Germanic *baitjan in: a. Old Norse beita (verb), to hunt with dogs, and beita (noun), pasture, food: BAIT!; b. Old French beter, to harass with dogs: ABET. 4. Germanic *bait-, a boat (< “dugout
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1218:AEDILE aidh- AEGIS aig- AENEOUS ayes- AEOLIPILE pulé AEPYORNIS OrF- AERIAL wer-2 AERO- wer-2 AEROBE gWei- AERODYNE deu-2 AERONAUT nau-2 AESIR ansu- AESTHETIC au-5 AESTIVAL aidh- AETHER aidh- AFFABLE bha-2 AFFAIR dhé-1 AFFECT! dhé-1 AFFECT? dhé-1 AFFECTION dhé-1 AFFERENT bher-1 AFFIANCE bheidh- AFFIANT bheidh- AFFIDAVIT bheldh- AFFILIATE dhé(i)- AFFIRM dher-2 AFFIX dhigy- AFFLATUS bhié-2 AFFLICT bhiig- AFFLUENT bhleu- AFFORD pert AFFOREST dhwer- AFFRAY  pri- AFFRICATE bhréi- AFFUSION gheu- AFTER apo- AFTERMATH mé-4 AGAIN gagina AGAINST gagina AGALACTIA melg- AGAPANTHUS andh- AGE aiw- AGENDUM ag- AGENT ag- AGERATUM gere-1 AGGLOMERATE gel-1 AGGLUTINATE gel-1 AGGRAVATE gWere-2 AGGREGATE ger-? AGGRESS ghredh- AGGRIEVE gWere-2 AGHAST gheis- AGILE ag-
1247:ANTA aneta ANTAGONIZE ag- ANTE ant- ANTEBELLUM duellum ANTECEDE ked- ANTEFIX dhig¥- ANTEPENDIUM (S)pen- ANTERIOR ant- ANTHELION sawel- ANTHELMINTIC wel-3 ANTHEM bha-2 ANTHEMION andh- ANTHER andh- ANTHESIS andh- ANTHO- andh- -ANTHOUS andh- ANTHROPIC ner-2 ANTHROPO- ner-2 ANTHURIUM ors- ANTI- ant-
1248:ANTIG ant- ANTICIPATE kap- ANTIDOTE d6- ANTINOMIAN nem- ANTINOMY nem- ANTIPASTO pa- ANTIPHON bha-2 ANTIPODES ped-1 ANTIQUE ant- ANTITHESIS dhé-1
1252:AORTA wer-2 APERIENT wer-5 APERITIF wer-5 APERTURE wer-5 APEX ap-! APHELION sawel- APHONIA bha-2 APLANATIC pele-2 APLOMB plumbum APNEA pneu-
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1278:BAPTIZE gWébh-1 BAR? gWere-2 BARB! bhardha BARBARIAN baba- BARBARISM baba- BARBAROUS_ baba- BARBEL bhardha BARBELLATE bhardha BARBER bhardha BARBETTE bhardha BARBICEL bhardha BARBULE bhardha BARD! gWera-3 BARE! bhoso- BARGAIN bhergh-? BARITE gWera-2 BARITONE gWera-2 BARIUM gWera-2 BARK! bherg- BARLEY bhares- BARM_ Dbhreu-2 BARMY bhreu-2 BARN bhares- BARO- gWera-2 BAROUCHE dwo-, ret- BARROW! bher-1 BARROW? bhergh-2 BARROW’ = bher-2 BARYON gWere-2 BARYSPHERE gWere-2 BARYTA gWere-2 BASCULE (s)keu- BASE! gWa- BASE? bassus BASIS gWa- BAS-RELIEF bassus Bass! bhar- Bass? bassus BASSET! bassus BASSO bassus BAT? bhiag- BATE? battuere BATEAU bheid- BATH! bhé- BATHE bhé- BATHOS gWadh- BATHY- gWadh- BATHYSCAPH skep- BATTEN! bhad- BATTERY battuere BATTER! battuere BATTER’ battuere BATTLE battuere BAWD bhel-2 BAWL bhel-4 Bay? bat-
1280:BE- ambhi BEACON bha-1 BEAD gWhedh- BEADLE bheudh- BEAM bheue- BEAN bha-bha- BEAR! bher-1 BEAR? bher-3 BEARD bhardha BEAT bhau- BEATIFIC deu-2, dhé-1 BEATIFY deu-2 BEATITUDE deu-2 BEAU deu-2 BEAUTY deu-2 BEAVER! bher-3 BECHE-DE-MER mori- BECK? bheg¥- BECKON bha-! BECOME gWa- BED bhedh-
1294:BENIGN deu-?, gene- BENTHOS gWadh- BENUMB nem- BEQUEATH gWet-2 BEQUEST gWet-2 BEREAVE reup- BERM bhrem-2 BERRY bha-1 BERSERKER bher-3 BESPEAK spreg- BESPRENT spergh- BEsT bhad- BETOKEN deik- BETRAY d6- BETROTH deru BETTER bhad- BETWEEN dwo- BETWIXT dwo- BEVEL bat- BEVERAGE pO(i)- BEWITCH weik-2 BEZOAR gWhen-1, pa- BHAGAVAD-GITA g@i-2 BI- dwo-
1309:BITE bheid- BITTER bheid- BITTERN! beu-2 BITUMEN gWet-1 BIVOUAC ambhi, weg-2 BLACK bhel-1 BLACKMAIL méd- BLADDER bhié-2 BLADE bhel-3 BLAIN bhlei- BLAME bha-2 BLANCH bhel-1 BLANCMANGE bhel-1 BLAND mel-1 BLANDISH mel-1 BLANK bhel-1 BLANKET bhel-1 BLARE bhié-1 BLASPHEME bha-2 BLASPHEMOUS bha-2 BLAST bhlé-2 -BLAST melst- BLASTEMA melst- BLASTO- melst- BLASTULA melst- BLATHER bhlé-2 BLAZE! bhel-1 BLEACH bhel-1 BLEAK! bhel-1 BLEAK? bhel-1 BLEAT bhlé-1 BLEMISH bhel-1 BLENCH! bhel-1 BLEND bhel-1 BLENDE bhel-1 BLENNY mel-1 BLESBOK bhel-1, bhugo- BLIND bhel-1 BLINDFOLD bhel-1 BLINI mele- BLINTZ mele- BLISTER bhlei- BLITE mele- BLITZKRIEG bhel-1, gwere-2 BLOAT bhieu- BLOND bhel-1 BLOOM! bhel-3 BLOOM? bhel-3 BLOSSOM bhel-3 BLOW! bhié-2 BLOW3 bhel-3 BLUE bhel-1 BLUNDERBUSS (s)tene- BLUSH bhel-1 BOARD bherdh- BOAST! beu-1 BOAT bheid- BOATSWAIN bheid- BOCACCIO beu-1 BODE! bheudh- BODEGA dhé-1 BODHISATTVA bheudh-, es- BoER bheue-
1314:BOOM? bheue- BOON! pbha-2 BOON2 deu-2 BOOR bheue- BOOT? bhad- BOOTH bheue- BORDELLO bherdh- BORDER bherdh- BORE! bher-2 BORE’ bher-1 Boreas gWero-1 BOROUGH bhergh-2 BORROW bhergh-1 BORSCHT bhar- BOSCAGE busk- BOSOM beu-1 BOTH ambh6o BOTHRIUM bhedh- BO TREE bheudh- BOTTOM bhudh- BOTTOMRY bhudh- BOTULIN gWet-3 BOTULINUM gWet-3 BOTULISM gWet-3 BOUCLE beu-1 BOUGH bhaghu- BOUILLABAISSE beu-! BOUILLON beu-1 BOULDER bhel-2 BOULE! gWele-1 BOULE? beu-! BOULEVARD bhel-2, werg-
1328:CABARET kamer- CABEZON kaput CABLE kap- CABRILLA kapro- CABRIOLET kapro- CACHE ag- CACHEXIA segh- caco- kakka- CACODYL kakka- CACOETHES kakka-, s(w)e- CACOPHONOUS bha-2, kakka- CACOPHONY kakka- CACUMINAL keu-2 CADASTER  steigh- CADAVER kad- CADELLE kat-1 CADENCE kad- CADENT kad- CADET kaput CADRE kWetwer- CADUCEUS kar-2 CADUCICORN kad-, ker-1 CADUCOUS kad- CAECILIAN kaiko- CAECUM kaiko- CAELUM_ kae-id- CAESURA kae-id- CAGE keua-2 CAHIER kWetwer- CAINOTOPHOBIA ken-3 CAIRD kerd-2 CAISSON kap-
1390:CONFECT dhé-1 CONFEDERATE bheidh- CONFER bher-1 CONFESS bha-2 CONFETTI dhé-1 CONFIDANT bheidh- CONFIDE bheidh- CONFIDENT bheidh- CONFIGURATION dheigh- CONFIRM dher-2 CONFLAGRANT bhel-1 CONFLAGRATION bhel-1 CONFLATE bhié-2 CONFLICT bhiig- CONFLUENT bhieu- CONFORM merph-
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
1454:ELUANT leu(@)- ELUCIDATE leuk- ELUDE leid- ELUTE leu(a)- ELUVIUM leu(a)- ELYTRON wel-3 EMACIATE mak- EMANATE ma-3 EMANCIPATE man-2 EMASCULATE mas EMBASSAGE ag- EMBASSY ag- EMBELLISH deu-2 EMBER eUS- EMBER DAY ambhi, rei-3 EMBLEM gWele-1 EMBLEMENTS bhel-3 EMBOUCHURE beu-! EMBRACE mregh-u- EMBROCATE mergh- EMEND mend- EMERGE mezg-! EMERITUS (s)mer-2 EMESIS weme- EMETIC weme- EMIGRATE mei-! EMINENT men-2 EMIT (s)meit(9)- EMMET mai-1 EMOLLIENT mel-1 EMOTION meue- EMPEROR pere-! EMPHASIS bha-' EMPHYSEMA pu-! EMPIRIC per-4 EMPLOY plek- EMPORIUM per-2 EMPRISE ghend- EMPTY med- EMPYEMA pu-2 EMPYREAL pil- EMULSION melg- EMUNCTORY meug-2 EN-! en
1468:EPIBOLY gWele-1 EPIC wekw- EPICARDIUM kerd-1 EPICENE kom EPICRITIC krei- EPIDEMIC da- EPIDERMIS der-2 EPIDIDYMIS dwo- EPIDOTE do- EPIGASTRIUM gras- EPIGEAL gé EPIGENE gene- EPIGONE gene- EPIGRAM gerbh- EPIGRAPH gerbh- EPILEPSY (s)lag- EPILOGUE leg-1 EPIMYSIUM mis- EPIPHANY bha-1 EPIPHYSIS bheue- EPISCOPAL spek- EPISODE en, sed-2 EPISTASIS sta- EPISTAXIS stag- EPISTEMOLOGY sta- EPISTLE  stel- EPISTYLE sta- EPITAPH dhembh- EPITASIS ten- EPITHELIUM dhé@(i)- EPITHET dhé-1 EPITOME tem- EPOCH segh- EPODE wed-2 EPONYM nd-men- EPONYMOUS nd-men- EPOS wekw-
1477:ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
1497:Fair? dhés- FAITH bheidh- FALCON pel-2 FALDSTOOL pel-3 FALL p(h)ol- FALLOW DEER _pel-2 FALTBOAT pel-3 FAME bha-2 FAMOUS bha-2 FAN! wet-1 FANATIC dhés- FANG pag- FANTASY bha-1 FANTOCCINI bha-2 FAR pert
1503:FATE bha-2 FATHER peter- FATHOM pete- FATIDIC deik- FAUBOURG bhergh-?, dhwer- FAVA BEAN bha-bha- FAVOR ghow-é- FAVORITE ghow-é- FAWN! pek-t FAWN? dhé(i)- FAY} pag- FEALTY bheidh- FEAR per-4 FEASIBLE dhé-1 FEasT dhés- FEAT! dhé-1 FEATHER pet- FEATURE dhé-1 FEBRIFUGE bheug-! FECUND dh@(i)- FEDERAL bheidh- FEDERATE bheidh- FEE peku- FEEBLE bhlé-1 FEED pa-
1608:HIEROPHANT bha-!, eis-1 HIGH keu-2
1676:INCIDENT kad- INCINERATE keni- INCIPIENT kap- INCISE kae-id- INCITE kei-3 INCLINE klei- INCLUDE kleu-3 INCONDITE dhé-1 INCREASE ker-3 INCUBATE keu-2 INCULT kWwel-1 INCUMBENT keu-2 INCUNABULUM kei-1 INCUR kers-2 INCUS kau-2 INDEMNIFY dap- INDEMNITY dap- INDENT! dent- INDENTURE dent- INDEX deik- INDICATE deik- INDICT deik- INDIGEN gene- INDIGENOUS gene- INDIGENT eg- INDIGN dek-1 INDIGNANT dek-1 INDIGNATION dek-1 INDITE deik- INDOLENT del-3 INDOMITABLE deme-2 INDUCE deuk- INDURATE deru INDUSTRY en, ster-2 INEBRIATE 6g¥h- INEFFABLE bha-2 INELUCTABLE leug-1 INEPT ap-1
1678:INERTIA ar- INEXORABLE 6r- INFAMOUS bha-2 INFANT bha-2 INFANTRY bha-2 INFARCT bhrekw- INFECT dhé-1 INFELICITY dhé&(i)- INFER_ bher-1 INFERIOR ndher- INFERNAL ndher- INFERNO ndher- INFEST dhers- INFEUDATION peku- INFIDEL bheidh- INFIRM dher-2 INFIRMARY dher-2 INFIX dhigw- INFLAME bhel-1 INFLATE bhié-2 INFLICT  bhiig- INFLUENCE bhieu- INFLUENZA bhleu- INFRA- ndher- INFRACT bhreg- INFRANGIBLE bhreg- INFRINGE bhreg- INFUSE gheu- INGENIOUS gene- INGENUOUS gene- INGEST gerere INGRATE gWere-3 INGRATIATE gWere-3 INGRESsS ghredh- INGUINAL engW- INGURGITATE gWere-4 INHABIT ghabh- INHERE ghais- INHERIT ghé- INHIBIT ghabh- INHUME dhghem- INIMICAL amma INITIAL ej-1 INITIATE ei-1 INJECT yé- INJUNCTION yeug- INJURY yewes- INK kéu-
2051:PANT bha-1 PANTHEON dhés- PANTRY pa-
2084:-PHAGE bhag-1 -PHAGIA bhag-! PHAGO- bhag-1 -PHAGOUS  bhag-! PHALANGE bhelg- PHALANX bhelg- PHALAROPE bhel-1, ped-1 PHALLUS bhel-2 PHANEROGAM bha-! PHANTASM_ bha-! PHANTASMAGORIA bha-1 PHANTOM bha-1 PHARMACOPOEIA kWei-2 PHARYNX bher-2 PHASE bha-1 -PHASIA bha-2 PHELLEM bhel-2 PHELLODERM bhel-2 PHELLOGEN _bhel-2 PHENO- bha-1 PHENOMENON bha-1 PHEROMONE bher-1 PHILANDER ner-2 PHILANTHROPY ner-2 PHILATELY tela- -PHILE bhilo- -PHILIA bhilo- PHILLUMENIST leuk- PHILO- bhilo- PHILODENDRON deru -PHILOUS _bhilo- PHILTER bhilo- PHLEGETHON bhel-1 PHLEGM bhel-1 PHLEGMATIC bhel-1 PHLOEM bhlieu- PHLOGISTON bhel-1 PHLOGOPITE bhel-1, okw- PHLOX bhel-1 PHLYCTENA bhlieu- -PHOBE bheg¥- -PHOBIA bhegw- PHOEBE bheigw- PHOEBUS bheigw- PHONE! bha-2 -PHONE bha-2 PHONEME bha-2 PHONETIC bha-2 PHONO- bha-2 -PHONY bha-2 -PHORE bher-1 -PHORESIS bher-1 -PHOROUS bher-1 PHOS- bha-1 PHOSPHENE bha-1 PHOSPHORUS bha-1 PHOT bha-1
2085:PHOTO- bha-1 PHOTOTROPH threph- PHRASE gWhren- PHRATRY bhrater- PHREATIC bhreu-2 -PHRENIA gW¥hren- PHRENITIS gWhren- PHRENO- gWhren- PHTHIRIASIS dhgWher- PHTHISIS dhgWhei-
```


## [2026-09-05T06:06:02.104Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'پزشک' BQT_v1_pages.txt | head -20"
}
```


### [2026-09-05T06:06:02.151Z] TOOL RESULT

```
304:شناسی وپزشکی و جزاینها دز گوشه و کنار این نامةٌ را کنده و پریشان دیده
25521:کنندچنانك نن‌مردم مر پزشکی‌را وچنانك اندازه مرهندسد را...» «دانشنامه ی۵۷*.
```


## [2026-09-05T06:06:27.631Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -E 'symphony,.{0,400}' KLN_1966.txt | head -3; echo \"== batiza ==\"; grep -n -o -E 'better, adj.{0,400}' KLN_1966.txt | head -3; echo \"== best ==\"; grep -n -o -E 'best, adj.{0,350}' KLN_1966.txt | head -3"
}
```


### [2026-09-05T06:06:29.457Z] TOOL RESULT

```
8544:symphony,  harmony’,  fr.  concinere,  ‘to  sing together’,  fr.  con-  and  canere,  ‘to  sing’.  See  cant, ‘slang  of  beggars’  and  cp.  concert,  n.  For  the change  of  Latin  a  (in  canere)  to  e  (in  con-centus) see  accent  and  cp.  words  there  referred  to. concenter,  concentre,  v.,  to  concentrate.  —  F. concentrer,  fr.  con-  and  L.  centrum,  ‘center’.  See center  and  cp.  next
8554:symphony,  har¬ mony,  harmonious  music,  concert’),  fr.  con-  and cantare ,  ‘to  sing’.  See  cant,  ‘slang  of  beggars’, and  cp.  concent.  For  the  change  of  Latin  a  (in cdntdre)  to  e  (in  con-centare)  see  accent.  For  the change  of  -nt-  to  -rt-,  which  is  due  to  dissi¬ milation,  cp.  L.  carmen,  ‘song’,  dissimilated  fr. *camnen  (fr.  canere ,‘  to  sing'),  and  germen,  ‘
28576:symphony,  caco¬ phony.
== batiza ==
== best ==
```


## [2026-09-05T06:06:32.478Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -E 'symphony,  n\\..{0,500}' KLN_1966.txt KLN_1971.txt | head -4; echo \"=== phone ===\"; grep -n -o -E 'phone,  n\\..{0,400}' KLN_1966.txt | head -4"
}
```


### [2026-09-05T06:06:34.217Z] TOOL RESULT

```
KLN_1966.txt:37822:symphony,  n.  —  ME.  symphonie,  fr.  OF.  simpho- nie  (F.  symphonie),  fr.  L.  symphonia,  fr.  Gk. 0uti.9t.ma,  ‘concord  of  sound,  harmony,  agree¬ ment’,  fr.  aup9<ovoi;,  ‘agreeing  in  sound’,  fr. auv  (see  syn-)  and  9 o>vf),  ‘sound’.  See  phone, ‘speech  sound',  and  cp.  words  there  referred  to. Symphoricarpos,  n.,  a  genus  of  plants,  the  snow- berry  {bot.)  —  ModL.,  compounded  of  Gk. aup9opoc,  ‘accompanying’,  and  xap7r6s,  ‘fruit’; so  called  from  the  clustered  be
=== phone ===
2989:phone,  n.  Cp.  anthem,  which is  a  doublet  of  antiphon.
3947:phone,  n.,  an  instrument  for  helping  the  deaf to  hear.  —  A  hybrid  coined  fr.  L.  audire,  ‘to  hear’ , and  Gk.  <pcavr),  ‘sound’.  See  audible  and  phone, audit,  tr.  v.  and  n.  —  Back  formation  fr.  auditor (Qv)
10877:phone,  n.,  an  instrument  placed  against  the teeth  to  enable  the  deaf  to  hear.  —  A  hybrid coined  fr.  L.  dens,  gen.  dentis,  ‘tooth’,  and  Gk. 9 ovr),  ‘sound’.  See  denti-  and  phone.  The  correct form  would  be  odontophone,  fr.  Gk.  o8ojv,  gen. o86vto<;,  ‘tooth’,  and  cpojvr],  ‘sound’, dentist,  n.  —  F.  dentiste,  a  hybrid  coined  fr.  L. dens,  gen.  dentis,  ‘tooth’,  
11332:phone,  n.,  a  phonographic  instrument  for recording  and  reproducing.  —  A  hybrid  coined fr.  L.  dictare,  ‘to  dictate’,  and  Gk.  tpiovif),  ‘sound, voice’.  See  dictate  and  phone,  ‘speech,  sound’, dictate,  tr.  and  intr.  v.  —  L.  dictatus,  pp.  of  dic¬ tare,  ‘to  say  often,  pronounce  repeatedly,  dic¬ tate  (for  writing)’,  freq.  of  dicere  (pp.  dictus), ‘to  say’.  See  dic
```


## [2026-09-05T06:06:42.689Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=37800 && NR<=37830' KLN_1966.txt | grep -n -E '^[0-9]{3,4}' ; echo \"--- markers near ---\"; awk 'NR>=37700 && NR<=37900 && /^[0-9]{3,4}\\s*$/{print NR\": \"$0}' KLN_1966.txt | head; echo \"=== page marker search ===\"; grep -n -E '^ *1556 *$| ^*1557 *$|^ *1558 *$' KLN_1966.txt | head"
}
```


### [2026-09-05T06:06:44.381Z] TOOL RESULT

```
7:1556
--- markers near ---
=== page marker search ===
ugrep: error: error at position 17
(?m)^ *1556 *$| ^*1557 *$|^ *1558 *$
                 \___invalid syntax
```


## [2026-09-05T06:06:47.963Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -E '^ *16[5-9] *$' KLN_1966.txt | head; "
}
```


### [2026-09-05T06:06:49.518Z] TOOL RESULT

```
4754:165
4811:166
4823:167
4868:166
4869:169
```


## [2026-09-05T06:06:51.475Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4823,4870p' KLN_1966.txt"
}
```


### [2026-09-05T06:06:51.522Z] TOOL RESULT

```
167
bespangle,  tr.  v.  —  Formed  fr.  be-  and  spangle. Derivative:  bespangl-ed,  adj. bespatter,  tr.  v.  —  Formed  fr.  be-  and  spatter. Derivative :  bespatter-er,  n. bespeak,  tr.  v.  —  ME.  bespeken,  fr.  OE.  be- sp(r)ecan,  ‘to  speak  about’,  rel.  to  Du.  bespreken, G.  besprechen.  See  be-  and  speak, besprent,  adj.,  sprinkled  (archaic).  —  ME.  be- spreynt,  pp.  of  besprengen,  fr.  OE.  besprengan, ‘to  besprinkle’,  rel.  to  Du.  and  G.  besprengen, of  same  meaning.  See  be-  and  sprinkle  and  cp. next  word.
besprinkle,  tr.  v.  —  Formed  fr.  pref.  be-  and sprinkle.
Bessemer  process,  Bessemer  steel.  —  So  called after  Sir  Harry  Bessemer,  engineer  and  inventor (1813-98).
best,  adj.  —  ME.,  fr.  OE.  best,  dissimilated  fr. betst,  rel.  to  ON.  beztr,  Du.  best,  OHG.  be^isto, MHG.,  G.  best,  Goth,  batists,  ‘best’,  OE.  batian, ‘to  become  better’,  bot,  ‘remedy,  cure,  improve¬ ment,  compensation’,  and  possibly  cognate  with OI.  bhadrah,  ‘favorable,  good’,  Avestic  hubadra-, lucky’.  Cp.  better.  Cp.  also  batten,  ‘to  grow fat’,  boot,  ‘advantage’.  For  the  dissimilation  of
OE.  betst  into  best  cp.  last,  adj.
bestead,  adj.  —  ME.  bestad,  ‘placed,  situated’, formed  fr.  be-  and  stad,  ‘placed’,  fr.  ON. staddr,  ‘placed’,  pp.  of  stedja,  ‘to  place,  fix’.  See stead.
bestead,  tr.  v.,  to  help.  —  Formed  fr.  be-  and stead,  v.,  which  derives  fr.  stead,  n. bestial,  adj.  —  F.,  fr.  L.  bestialis,  Tike  a  beast’, fr.  bestia,  ‘beast’.  See  beast  and  adj.  suff.  -al. Derivatives:  bestial-ly,  adv.,  bestiary  (q.v.), bestial-ize,  tr.  v.
bestiality,  n.  —  F.  bestialite,  fr.  bestial,  fr.  L.  bes¬ tialis.  See  prec.  word  and  -ity. bestiary,  n.,  a  medieval  collection  of  fables  about beasts.  —  ML.  bestiarium,  ‘a  treatise  on  beasts’, prop.  neut.  of  the  L.  adjective  bestiarus,  ‘per¬ taining  to  beasts’,  and  as  a  noun,  fr.  bestia, ’beast’.  See  beast  and  subst.  suff.  -ary. bestir,  tr.  v.  —  ME.  bestiren,  fr.  OE.  bestyrian, ’to  heap  up’,  fr.  be-  and  styrian,  ‘to  set  in  mo¬ tion’.  See  stir.
bestow,  tr.  v.  —  ME.  bestowen,  fr.  be-  and st owen.  See  stow.
Derivatives:  bestow-al,  n.,  bestow-er,  n. bestrew,  tr.  v.  —  ME.  bestrowen,  fr.  OE.  be- streowian,  ‘to  bestrew,  cover’,  fr.  be-  and streowian,  ‘to  strew’.  See  strew, bestrewn,  pp.  of  bestrew.
bestride,  tr.  v.  —  ME.  bestriden,  fr.  OE.  bestridan, 'to  mount  a  horse’,  fr.  be-  and  stridan,  ‘to  stride’. See  stride.
bet,  n.  —  Prob.  aphetic  for  the  ME.  noun  abet,  fr.
OF.  abet,  ft.  abeter,  ‘to  incite,  bait’,  lit.  ‘to  cause to  bite’.  See  abet
Derivatives:  bet,  tr.  and  intr.  v.,  better,  n. (q.v.),  bett-ing,  n.,  bett-or,  n. beta,  n.,  name  of  the  2nd  letter  of  the  Greek  al¬
phabet.  —  Gk.  (Jvjra,  fr.  Heb.-Phoen.  beth;  see beth.  The  a  was  added  because  a  Greek  word cannot  end  with  a  t  ;  cp.  alpha  and  words  there referred  to.
Beta,  n.,  a  genus  of  plants  of  the  goosefoot family  (bot.)  —  L.,  ‘the  beet’.  See  beet, betake,  reflex,  v.  —  ME.  bitaken,  ‘to  entrust’,  fr.  bi- (see  be-)  and  taken,  ‘to  take’.  See  take, betatron,  n.,  a  device  for  accelerating  the  velo¬ cities  of  electrons  or  beta  rays.  —  Coined  fr. beta  (rays)  and  (elec)tron. betel,  n.,  the  leaf  of  the  pepper  called  Piper  betel. —  Port,  betel,  betle,  betre,  fr.  Malayal.  vettila, fr.  veru  ila,  ‘simple  leaf’, beth,  n.,  name  of  the  2nd  letter  of  the  Hebrew alphabet.  —  Heb.  beth,  lit.  ‘house’;  so  called in  allusion  to  the  ancient  Hebrew  form  of  this letter.  See  bethel  and  cp.  beta, bethel,  n.,  a  house  of  worship.  —  Heb.  beth  El, ‘the  house  of  God’.  Beth  is  the  state  construct of  bdyith,  ‘house’,  and  rel.  to  Aram,  baythd, bethd,  Ugar.  bt,  Arab,  bayt,  Akkad,  bitu, ‘house’;  cp.  beth,  beta.  Cp.  also  Basque  baita, ‘house’.  For  the  second  element  see  El.  Cp. baetulus,  baetyl.
Bethesda,  n.,  a  pool  at  Jerusalem;  a  chapel.  — Gk.  Bij&eaSd,  fr.  Aram,  beth  hesdd,  ‘house  of mercy’.  See  bethel  and  Hasidim  and  cp.  beth, beta.
bethink,  reflex,  v.  —  ME.  bethenehen,  fr.  OE. bepencan,  ‘to  consider’,  formed  fr.  be-  and  pen- can,  ‘to  think’.  See  think  and  cp.  Du.  and  G. bedenken.
betide,  intr.  and  tr.  v.  —  ME.  betiden,  formed  fr. be-  and  tiden,  ‘to  happen’,  fr.  OE.  tidan.  See
tide.
betimes,  adv.  —  Formed  fr.  be-  and  adv.  gen.  of OE.  lima,  ‘time’.  See  time  and  -s. betoken,  tr.  v.  —  ME.  betacnien,  fr.  be-  and  OE. tacnian,  ‘to  signify,  betoken’,  for  tacn,  ‘sign, token’.  See  token.
Derivative :  betoken-er,  n. bet on,  n.,  a  kind  of  concrete.  —  F.,  fr.  L.  bitumen, ‘mineral  pitch’,  later  used  in  the  sense  of  ‘mud, sand’.  See  bitumen.
Betonica,  n.,  a  genus  of  plants  of  the  mint  family (bot.)  —  L.  betonica,  ‘bettony’.  See  next  word, betony,  n.,  a  plant  of  the  genus  Betonica.  —  F. betoine,  fr.  L.  betonica,  var.  of  vettonica,  named from  thfe  VettSnes,  VectSnes  (pi.),  a  tribe  living near  the  Tagus  (now  Tajo)  in  Lusitania  (now Portugal).  VectSnes  is  prob.  a  derivative  of  ve- here,  ‘to  draw,  carry’,  and  lit.  means  ‘carriers’. See  vehicle.
betray,  tr.  v.  —  ME.  betraien,  a  hybrid  coined fr.  be-  and  OF.  trair  (F.  trahir),  ‘to  betray’, which  was  formed — with  change  of  conju¬ gation — fr.  L.  tradere.  Cp.  It.  tradire,  OProv- en?.  trair,  ‘to  betray’,  and  see  tradition.  Cp.  al¬ so  traitor,  treason.
Derivatives:  betray-al,  n.,  betray-er,  n.,  betrav- ment,  n.
betroth
oioie
betroth,  tr.  v.  —  ME.  betreuthen.  See  be-  and
troth,  truth.
Derivatives :  betrolh-al,  n.,  betroth-ed,  adj.  andn.
better,  adj.  —  ME.  bettere,  bettre  (adj.),  bet  (adv.), fr.  OE.  betera  (adj.),  bet  (adv.),  rel.  to  ON.  betri (adj.),  betr  (adv.),  Dan.  bedre,  Swed.  battre,  Du. beter  (adj.  and  adv.),  OHG.  be33iro  (adj.),  ba3 (adv.)  G.  besser  (adj.  and  adv.),  Goth,  batiza (adj.)  See  best  and  cp.  words  there  referred  to. Derivatives:  better,  v.  (q.v.),  better,  adv. andn., better-ing,  n.,  better-ment,  n.
better,  tr.  and  intr.  v.  • —  OE.  beterian,  fr.  betera, ‘better’.  See  better,  adj.
better,  n.,  one  who  bets.  —  Formed  fr.  bet  with agential  suff.  -er.
betty,  n.,  flask  of  oil;  crowbar,  etc.  —  From Betty,  pet  name  of  Elizabeth.
Betula,  n.,  the  genus  of  the  birches  (hot.)  —  L. betula,  betulla,  ‘birch  tree’,  fr.  Gaulish  betu-, ‘bitumen’  (found  in  PN.s);  cp.  Mir.  beithe, ‘box  tree’,  W.  bedwen,  ‘birch  tree’.  According to  Pliny  the  birch  tree  was  called  betu-la,  i.e. ‘bitumen  tree’,  because  the  Gauls  extracted  tar from  it;  see  bitumen.
between,  prep,  and  adv.  —  ME.  bitweonen,  bi- twenen,  bitwene.  fr.  OE.  betweonum,  fr.  be-,  ‘by’, and  tweonum,  dative  pi.  of  tweon,  ‘double, twain’,  which  is  rel.  to  Goth,  tweihnai,  ‘two each’,  fr.  twa,  ‘two’.  See  be-,  twain,  two,  and cp.  next  word.
betwixt,  prep,  and  adv.  —  ME.  betwixe,  fr.  OE. betweox,  betweohs,  betwux,  betwyx,  fr.  pref.  be-, ‘by’,  and  a  form  of  twa,  ‘two’;  cp.  OHG.  zwisk, zwiski,  MHG.  zwisc,  ‘twofold’,  OS.  twisk,  ‘be¬ tween’,  Du.  tussen,  G.  zwischen,  of  s.m.  See between.  For  the  final  -t  cp.  against,  amongst, etc.
Beulah,  fern.  PN.  —  Heb.  be'iildn,  ‘married  wom¬ an’,  fern.  pp.  of  bd‘al,  ‘he  married’,  rel.  to  bd‘al, ‘lord,  ruler,  husband’.  See  Baal.
beurre,  n.,  butter.  —  F.,  ‘butter’,  fr.  earlier  burre, fr.  L.  butyrum,  fr.  Gk.  pouxupov.  See  butter.
beurre,  n.,  any  kind  of  pear  with  soft  flesh.  —  F., pp.  of  beurrer,  ‘to  butter���,  fr.  beurre,  ‘butter’. See  prec.  word.
bevel,  n.,  inclination  of  a  surface.  —  OF.  "baivel (whence  F.  beveau,  biveau),  ‘bevel  rule’,  fr.  OF. baif,  ‘with  an  open  mouth’,  fr.  baer,  beer,  ‘to gape’.  See  bay,  ‘part  in  the  wall’,  and  cp.  words there  referred  to.
Derivatives:  bevel,  tr.  v.  bevel(l)-ed,  adj.,  be- vel(l)-er,  n.
beverage,  n.  —  OF.  bevrage,  bovrage  (F.  breu- vage),  fr.  beivre,  boivre  (F.  boire),  ‘to  drink’,  fr. L.  bibere.  See  bibulous  and  -age  and  cp.  bevy, abreuvoir.
bevue,  n.,  error,  blunder.  —  F.  bevue,  ‘blunder, mistake,  slip’,  fr.  OF.  bes-vue,  lit.  ‘an  erroneous vue’,  fr.  pejorative  pref.  bes-,  which  derives  fr. L.  bis,  ‘twice’  (see  bis-;  for  sense  development  cp. OF.  bes-torne,  ‘badly  turned’,  lit.  ‘twice  turned’), and  fr.  vue,  ‘sight’,  prop.  fern.  pp.  of  voir,  ‘to
166
169
see’,  fr.  L.  videre,  ‘to  see’.  See  vision  and  cp. words  there  referred  to.
```


## [2026-09-05T06:07:02.103Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -E 'huba[a-zA-Zδ]{0,8}ra[^ ]{0,3}.{0,220}' BRT.txt | head -10; echo \"=== search hu.ba ===\"; grep -n -o -E 'hu\\.?ba[dS8δ]ra.{0,200}' BRT.txt | head -10"
}
```


## [2026-09-05T06:07:02.219Z] TOOL CALL #29: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:399 2>&1 | head -60"
}
```


### [2026-09-05T06:07:03.953Z] TOOL RESULT

```
=== search hu.ba ===
```


### [2026-09-05T06:07:05.498Z] TOOL RESULT

```
no scan of BQT covers printed page 399 (see 'scans' in refs_online.json)
```


## [2026-09-05T06:07:10.100Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c 'pdf page' BQT_v1_pages.txt; grep -n 'pdf page' BQT_v1_pages.txt | sed -n '1,5p;395,405p'"
}
```


### [2026-09-05T06:07:10.158Z] TOOL RESULT

```
0
```


## [2026-09-05T06:07:13.592Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 600 BQT_v1_pages.txt; echo; echo \"=== ff count ===\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' BQT_v1_pages.txt; echo \"=== python refs_online BQT scans ===\"; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))['BQT']\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-09-05T06:07:15.353Z] TOOL RESULT

```
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
وک رهب اه نات مج
لش
وان روکد ور
۱ و
طراول ؛ | ع اس
چاپ دوم فروردین ۱۳۴۳
با تجدید نظر کامل
بسرمایه کنابفروشی ابن سینا - تپر اناداره کل دک زون.
شماره ۷9 9 ۳
بر
5
‌ ۰ م�
=== ff count ===
777
=== python refs_online BQT scans ===
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
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT
```


## [2026-09-05T06:07:21.791Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in 'پزشك' 'زشک' 'بزشک' 'پزش' 'پژشک'; do echo \"-- $w --\"; grep -c \"$w\" BQT_v1_pages.txt; done; echo \"=== leaf of پزش ===\"; awk 'BEGIN{RS=\"\\f\"} /پزش/{print NR}' BQT_v1_pages.txt | head"
}
```


### [2026-09-05T06:07:23.776Z] TOOL RESULT

```
-- پزشك --
3
-- زشک --
10
-- بزشک --
0
-- پزش --
6
-- پژشک --
0
=== leaf of پزش ===
15
185
216
494
559
625
```


## [2026-09-05T06:07:26.804Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==494' BQT_v1_pages.txt | grep -n 'پزش' ; echo \"=== full leaf 494 head ===\"; awk 'BEGIN{RS=\"\\f\"} NR==494' BQT_v1_pages.txt | head -40"
}
```


### [2026-09-05T06:07:28.386Z] TOOL RESULT

```
34:وم رکز او الموت بود +دائرالمعارف اسلام*. ۴ ره : پزشك. ۴ راد : پز وشم.
=== full leaf 494 head ===
آب بندند( ‏ و سکون ثابی گوی باشد که آب
درآن جمع شود - و رنگهآبرا نیز کوبند . *
بز چا لهفلاك - کنابه از برج جدی
است .
بز سم - بنتح اول و انی و سین بی
قطه و میم. و سکون الك . جل وزغ را گویند
و آن چیز سبزی باشد مانند ابریش مکه در روکه
آب بهم میرسد و وزغ در آن‌پنهان میشودوه‌عنی
ثر کیبی آن وزغ پنهان است چه سمه بمعنی
پنهان همآمده است. وآذرا بعربی طحلب کوبند
ضم طای حطی .
بز غش ۷ پم اول و الث و سکون
" الی و شین فرشت ج , ففب یکی از ازلاه اضحستر
و طایفةٌ اٍبشانرا پزغشیه خوانند .
ز گنج - بنم اول و نالثر سکون ثانی
و لون و جیم » چیزست که بدان پومت‌رادبا
و زراعت کننده را کویند ٩‏ ۱
پز رد گهاهیك - نا حکیمی است
استاد و پرورنده پرویزین انوشیروان بوده ۴ . ۷
۹ یز سك ه بضم اول و کس انی وسکون
سین بی‌نقطه, کای . دانهاست که آنرا بعربی‌عدس
خوانند .
بر شاث- بکر اول بر وزن سرشك »
حکیم و طبیب وجراح را گویند ؛ و بابای‌فارسی
هم آمده است ۴ .
بز شم ۴ - بنم اول و قح انی و سکون
الث و میم , پشم فرمی را کوند که از بن موی
بز بروید و آزرا بشاله برآرند و بتابند واز آن
ال بافبد .
لزع ح بختح ارل د ثانی و سکون غن
نقطه دار » بمعنی وزغ است که بعربی سفدع
٩‏ - از؛بزرعبی (داندایست که انداختهشود در زمین بهرروبدن «شرح قاموس؟: +- کلر,
۴ - وئیز بزر که امید (کیا) دومین‌حکمران اسمعليةٌ ابران وجااشین حسن صباح (0۳۲-۵۱۸)
وم رکز او الموت بود +دائرالمعارف اسلام*. ۴ ره : پزشك. ۴ راد : پز وشم.
۰ 2 وزغ » اوستا ۷۵2۵28 ايشت ۱ ص ۲۷۵ح». ورگ : اسفا ٩‏ : ۲ ص 4۸ .
۱ - باین‌معتی برغ (باراء مهمله ) است . ركك : برغ . ۲ - شیخ جیب‌آلدین علی بزخش
شیرازی حتوفی ۱۷۸ . « شدالازار ۷۳۷۲۳۶ ۰ < فحات‌آلاس چلپ حند ص 4۲4۱ و «از حصدی
تا جامی ترجمهٌ آفای حکمت ص ۵4۳*.
۵ ازرجمهر _ رك : بزرکمهر . ۵ برر گهار - نم اول و دوم وکسریتجيم,
پهلوی ۰۷11211787011117 ناموزیر خردمند انوشیروان در دامتالهای ابرانی. عمربآن بزرجمهر,
```


## [2026-09-05T06:07:51.630Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==494' BQT_v1_pages.txt | sed -n '40,120p'"
}
```


### [2026-09-05T06:07:53.697Z] TOOL RESULT

```
پهلوی ۰۷11211787011117 ناموزیر خردمند انوشیروان در دامتالهای ابرانی. عمربآن بزرجمهر,
مرحوم علامه قزوینی در نامه مورخ ٩‏ خرداد ۱۳۲۵ در باسخ نگارنده وشته اند : «شبهة بیست
که بونرجمهر وابوزرجمهر با هراملای دیگری برای ابتکلمه که با ذال معجمه باد» غلط فاحش :
و اشتباه عامیانه است که جزء اول این‌کلمه را بکنيةٌ ابوثر معروف از صحابةٌ مشپور حضرت‌رسول
اشتباه کرده‌اند وحتماً بزاه ممجمه درست است‌ولی «بوزرجمهر» در تاریخ بیهفی چاپ مرحوم ادیب:
کمان میکنم بکلی صحیح و حنطفی باشد چه درخط امرررزی فارسی هیج آهمیتی ندارد که ضممرا
بنحو آشباع با واو هم بنوبند با بدون اشباع بی واو مثل امید و اومید » و خرسند و خورسند
و پل و پول (بمعنی ؟۳08) وامثالها » دلی ابونرجمهر بازاه معجمه و باضاقةٌ الفی در اول» هیچ
وجهی ازسحت کمان نمیکنم داشته‌باشد. چون هیچ‌بنظر نرسیده که بز رکه را 0
«بوز رکب» بعنی بزبادتی الفی دراول‌آن. راجم بدخصیت بزر گمهر» رل بزد گمهرحکیم.تألیف
کرستنمن ترجه میکده در مج مهر سال اول شمارة ٩‏ بیمد و نیز جدااگانه منتشرشده است -
۵ 4 - بنم‌اول , م رکب از : بز + غاله (کاله) شانة صضیر«اسفا!:۲سص۹۹» ؛ بچةٌ بز .
```


## [2026-09-05T06:08:28.916Z] TOOL CALL #35: Bash

```json
{
 "command": "pdftoppm -f 80 -l 80 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg80 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-05T06:08:30.342Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KNT bisaz ==\"; grep -n -i -E 'bi[sš]az|ba[ie][sš]az' KNT.txt | head; echo \"== CHEUNG ==\"; grep -n -i -E 'bai[sš]az|bi[sš]az|be[sš]az' CHEUNG.txt | head"
}
```


### [2026-09-05T06:08:30.906Z] TOOL RESULT

```
total 8748
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 02:08 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb  502834 Sep  5 02:02 bqt538_big.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   72705 Sep  5 02:02 bqt538_fn6.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24595 Sep  5 02:02 bqt538_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22593 Sep  5 02:02 bqt538_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  207980 Sep  5 02:01 bqt538.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb  445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb   78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb   68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb  134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb  108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb  155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63822 Sep  5 01:59 pg78.png
-rw-rw-r-- 1 sfmqrb sfmqrb   58953 Sep  5 02:08 pg80.png
```


### [2026-09-05T06:08:30.961Z] TOOL RESULT

```
== KNT bisaz ==
== CHEUNG ==
2565:*bisaz (*baiSaz) ‘to heal, cure’ 
2566:*AVESTAN: YAv. bisaz- ‘to cure, heal’, also YAv. baesaza- ‘healing, curative’ 
2571:Pres. ja-: SUBJ. 1sg. YAv. bisazani (V 22.6), 3sg. YAv. bisaziiat (V 7.40 f£), OPT. 25р. YAv. bisaziiois 
2578:bys’zynyd, 3р1. BMP bys’zynynd /besazenend/, SUBJ. 3sg. MMP bys’zyn’d, 3р1. MMP bys’zyn’nd; Inf.: 
2579:caus. BMP byszynytn /besazenidan 
2592:© The denominative form bisaz derive from a noun *bis, which is continued in YAv. 
2597:variant: *baisaz. 
33314:bisaz-, 21 
56186:*bisaz 
56879:*bisaz
```


## [2026-09-05T06:08:33.606Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2560,2605p' CHEUNG.txt"
}
```


### [2026-09-05T06:08:33.665Z] TOOL RESULT

```
*IE COGNATES: OCS béda, Lith. béda ‘distress, worry’, Lith. badas (m.) ‘sorrow’ 
*REFERENCES: Werba 1997: 465 f.; ESIJa II: 158 f. 


*bisaz (*baiSaz) ‘to heal, cure’ 
*AVESTAN: YAv. bisaz- ‘to cure, heal’, also YAv. baesaza- ‘healing, curative’ 


= Liste: 38 

Pres. ja-: SUBJ. 1sg. YAv. bisazani (V 22.6), 3sg. YAv. bisaziiat (V 7.40 f£), OPT. 25р. YAv. bisaziiois 
(V 22.2, V 22.9) 

*MIDDLE PERSIAN: MMP by3’z-, ВМР by3’z-, byš(')c- /bésaz-/, ВМР bys(’)zyn- 
/besäzen-/ ‘to heal, cure’ 

Pres.: IND. 3sg. MMP byS’zynyd; Partic.: pres. MMP bys’z’g’n (pl.) ‘healing’; Caus.: IND. 3sg. MMP 
bys’zynyd, 3р1. BMP bys’zynynd /besazenend/, SUBJ. 3sg. MMP bys’zyn’d, 3р1. MMP bys’zyn’nd; Inf.: 
caus. BMP byszynytn /besazenidan 

*SOGDIAN: BSogd., MSogd. Byc ‘physician’ (GMS: §384) 

*CHORESMIAN: ? m/rBsy- ‘to heal [intr.]’ (< *fra-bad-s-ja- ?) = Samadi: 169 

*NWIR: NP pizisk (re-introduced), Kurd. (Kurm.) bizisk, (Sor.) pazisk, pizisk 
‘doctor’ 

*MISC: Arm. (LW) bzisk ‘doctor’ 

*SANSKRIT: bhisáj- (m.) ‘healer, physician’ (RV+) = EWAia II: 264 

© The denominative form bisaz derive from a noun *bis, which is continued in YAv. 
bis- (6151$ framätö ‘skilled in medicine’, F 576), Y Av. paiti.bisi- ‘medicinal, healing’ 
(Y 10.18), cf. Klingenschmitt 1968: 171 ff. This root has no IE etymology and may 
reflect an ancient cultural borrowing, on which see Lubotsky, Early Contacts: 310. 
The forms with a long vowel in the first syllable reflect an ablauting (denominative) 
variant: *baisaz. 


“PIE LIV: — | Pok.: 
*REFERENCES: Werba 1997: 432; Cabolov 2001: 196 


*braHz ‘to shine, set on fire, alight’
```


## [2026-09-05T06:08:34.794Z] TOOL CALL #38: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg80.png"
}
```


### [2026-09-05T06:08:35.136Z] TOOL RESULT

```

```


## [2026-09-05T06:08:35.131Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T06:09:02.665Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in 'تلفن' 'گرامافون' 'سمفونی' 'گرامفون'; do echo \"-- $w --\"; grep -c \"$w\" MON_part1.txt MON_part2.txt 2>/dev/null; done"
}
```


## [2026-09-05T06:09:02.986Z] TOOL CALL #40: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ 2>/dev/null | head -20; echo ---; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK 2>/dev/null | head"
}
```


### [2026-09-05T06:09:04.394Z] TOOL RESULT

```
Exit code 1
-- تلفن --
MON_part2.txt:16
MON_part1.txt:4
-- گرامافون --
MON_part2.txt:2
MON_part1.txt:2
-- سمفونی --
MON_part2.txt:0
MON_part1.txt:3
-- گرامفون --
MON_part1.txt:0
MON_part2.txt:0
```


### [2026-09-05T06:09:04.463Z] TOOL RESULT

```
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
---
101.png
126.png
311.png
33.png
39.png
46.png
54.png
69.png
71.png
72.png
```


## [2026-09-05T06:09:07.785Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -E '.{60}تلفن.{80}' MON_part1.txt | head -6; echo \"=== gram ===\"; grep -n -o -E '.{60}گرامافون.{100}' MON_part1.txt MON_part2.txt | head -6; echo \"=== samf ===\"; grep -n -o -E '.{60}سمفونی.{100}' MON_part1.txt | head -6"
}
```


### [2026-09-05T06:09:07.935Z] TOOL RESULT

```
=== gram ===
=== samf ===
```


## [2026-09-05T06:09:11.288Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'تلفن' MON_part1.txt | head -5; echo \"=== gram1 ===\"; grep -n 'گرامافون' MON_part1.txt MON_part2.txt | head -5; echo \"=== samf ===\"; grep -n 'سمفونی' MON_part1.txt | head -5"
}
```


### [2026-09-05T06:09:11.418Z] TOOL RESULT

```
1900:روزنامه» مجله» برق» تلفن و غیره. 
29376:اختصاری پست و تلگراف و تلفن. 
64234:مانند تلفن کار می‌کند. 
82483:سیم‌های برق» تلگراف يا تلفن را از جایی به 
=== gram1 ===
MON_part1.txt:65632:گرامافون. 
MON_part1.txt:89765:صفحات. صفحة گرامافون: صفحه مدوری 
MON_part2.txt:16759:گرامافون می‌سازند. در درجات حرارت‌های 
MON_part2.txt:30342:گرامافون: 0- ۳6۲۱05 (- گرامافن | .( 
=== samf ===
79622:۸۷۸ فرهنگ فارسي معین سمفونی 
79625:سسمفونی: 1 (.) (مت.) قطعة 
81424:دیگر موسیقی سمفنیکک مثل سمفونی و
```


## [2026-09-05T06:09:14.305Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '79618,79632p' MON_part1.txt; echo \"=== gram ctx ===\"; sed -n '30336,30350p' MON_part2.txt; echo \"=== telefon in part2 ===\"; grep -n 'تلفن' MON_part2.txt | head -8"
}
```


### [2026-09-05T06:09:14.415Z] TOOL RESULT

```
که کسانی که گوششان سنگین است در 
گوش گذارند تا اصوات را بهتر شنوند. 


۸۷۸ فرهنگ فارسي معین سمفونی 


سسمفونی: 1 (.) (مت.) قطعة 
تنتیکگ: هه (غ.] (.) (جان.) ماهی) ج. 
روی او است (اساطیر). 

سمن: هه [ع.] (امص.) فربهی» چاقی. 
سسمنامو لیسم: همان هه ومع .( 
حرکت و راه رفتن شخص در حالی که در 
خواب طبیعی يا مغناطیسی است. 
=== gram ctx ===

طیعی متلور ‏ ۳9 خالص است (لف.) 
گرافیک: 6 (.) نمودار جیزی به 
وسبله اشکال و خطو ط؛ نمو دار . 


گرامافون: 0- ۳6۲۱05 (- گرامافن | .( 
التن اشت که صفحه‌ای را که آوازی در 
آن ضط شده به گردش در آورد و همان 
آواز را به گوش رساند. جعبةً صوت. 
گرامی: 1-:5:»: (ص.) عزیزه محترم. 
ضح.- در نظم و نثر فصیح همه جا گرامی (- 
گرامیکث» به.) آمده و «گرام ۲ - که در 
تداول بجای گرامی پا کرام عربی (ج. کریم) 
استعمال کنند . درست نیست. 
=== telefon in part2 ===
16806:زیرزمینی یا زیردریایی که جهت برق و تلفن 
16811:دریایی برای برق و تلفن و تلگراف؛ کشیدن 
36802:آلتی که در تلفن تعبیه شده و با قرار دادن آن 
36810:را ایسجاد می‌کند. در تلفن‌های معمولی 
50407:) ج. . مسخابره. ادارةٌ مخایرات: تلفن‌خانه 
50411:وسیلهٌ تلفن و تلگراف هستند. 
50414:تلگراف و تلفن ابلاغ کردن. (امص.) ابلا 
50415:خبری به وسیلةً تلگراف و تلفن. ضح.- این
```


## [2026-09-05T06:09:28.299Z] TOOL CALL #44: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T06:09:28.307Z] TOOL RESULT

```


```


## [2026-09-05T06:09:33.202Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B2%D8%B4%DA%A9",
 "prompt": "Give the full Persian etymology section for پزشک (pezešk): Middle Persian form, Old Iranian/Avestan antecedent, any mention of metathesis, Parthian, Sogdian, and any cited sources (Hasandust, MacKenzie, Cheung)."
}
```


## [2026-09-05T06:09:35.952Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eh%E2%82%82-",
 "prompt": "What is the reconstructed meaning of PIE *bʰeh₂- (the 'speak' root)? List its descendants (Latin fārī, Greek phēmí/phōnḗ, Germanic bannan, Sanskrit bhánati) and note whether any Iranian 'heal' words (Avestan baēšaza-, Sanskrit bhiṣáj-) are listed under it."
}
```


### [2026-09-05T06:09:39.923Z] TOOL RESULT

```
# Persian Etymology of پزشک (pezešk)

Based on the Wiktionary entry, here is the etymological information provided:

**Middle Persian Origin:**
The term derives from Middle Persian (bcšk'), with the Pahlavi form 𐫁𐫉𐫏𐫢𐫐 (bzyšk /bizešk/, "doctor, physician").

**Parthian Borrowing:**
"borrowed from Parthian _𐫁𐫉𐫏𐫢𐫐_ (bzyšk /bizešk/, 'doctor, physician')"

**Proto-Iranian Root:**
The ultimate source is Proto-Iranian *bišajkah, reconstructed in this resource.

**Comparative Evidence:**
The entry notes a parallel Iranian borrowing in Old Armenian բժիշկ (bžišk), and connection to Sanskrit भिषज्यति (bhiṣajyati, "to heal") and भिषज् (bhiṣaj, "curing; medicine; doctor").

**Note:** The document does not mention Sogdian cognates, Avestan forms, metathesis, or citations to Hasandust or Cheung—only references to MacKenzie's Pahlavi dictionary and Rastorgujeva & Edelʹman's etymological dictionary of Iranian languages.
```


### [2026-09-05T06:09:41.108Z] TOOL RESULT

```
# PIE *bʰeh₂- (Speak Root)

## Reconstructed Meaning

The root has two primary meanings: **"to speak"** and **"to say"**

## Listed Descendants

The article documents these descendants:

- **Latin**: *fās* ("divine law"), *fāmā* ("fame"), *fātus* ("spoken")
- **Greek**: *phḗmē* ("report"), *phōnḗ* ("voice"), *phắskō* ("to declare")
- **Germanic**: *bannaną* (Proto-Germanic form)
- **Sanskrit**: *bhánati* (Vedic Sanskrit, "speaks")

## Iranian 'Heal' Words

**No Iranian medical terminology appears in this entry.** The article only references Proto-Indo-Iranian derivatives like *bʰáHti* and *bʰáHšaH*, which relate to the speak/say function, not healing. Words like Avestan *baēšaza-* or Sanskrit *bhiṣáj-* ("physician") are not mentioned here.
```


## [2026-09-05T06:09:50.700Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D9%84%D9%81%D9%86",
 "prompt": "What does the Persian section say about the etymology of تلفن (telefon)? Is it borrowed from French téléphone? Also state the meaning."
}
```


## [2026-09-05T06:09:51.740Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/abandon",
 "prompt": "Give the full etymology of 'abandon', including Old French a bandon, bandon, Late Latin bannum/bannus, and the Frankish/Germanic *ban- 'proclaim'."
}
```


### [2026-09-05T06:09:56.690Z] TOOL RESULT

```
# Persian Etymology of تلفن

**Etymology:** Yes, the Persian word is borrowed from French. According to the dictionary: "Borrowed from French _téléphone_."

**Meaning:** The noun تلفن (telefon) means "telephone." An example usage is provided: "What's your telephone number?" This demonstrates its straightforward reference to the communication device.
```


### [2026-09-05T06:10:00.093Z] TOOL RESULT

```
# Etymology of Abandon

The word "abandon" traces back through multiple linguistic layers:

**Old French Origins:**
The verb comes from Old French *abandonner*, formed from the adverbial phrase "à bandon" meaning "at will, at discretion." This combined à (Latin *ad*) with *bandon*, derived from Latin *bannum* — "a proclamation."

**Germanic Roots:**
The Latin *bannum* ultimately derives from "a Frankish or other Germanic word," specifically Proto-Germanic *\*bannan-* meaning "proclaim, summon, outlaw." As the etymology notes: "things all done by proclamation."

**Semantic Evolution:**
The word's meaning shifted from feudal law contexts—where "mettre sa forest à bandon" meant opening one's forest to common use—to the modern sense of relinquishing control entirely. As one historical source explains, since something "placed at the absolute command of one party must by the same act be entirely given up by the original possessor," the sense evolved from conferring temporary control to complete renunciation of authority.

The noun form entered English around 1822 from French, referring to "a letting loose, freedom from self-restraint," though this usage initially remained italicized as a foreign borrowing.
```


## [2026-09-05T06:10:01.670Z] AGENT

Now let me archive the web sources.


## [2026-09-05T06:10:06.546Z] TOOL CALL #49: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/پزشک' --note 'page 80, root Bha 2, node 3: Persian pezešk etymology (MP bizešk < Parthian bzyšk < PIr *bišajkah)' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/bʰeh₂-' --note 'page 80, root Bha 2: PIE *bʰeh₂- to speak, descendants; no Iranian heal words listed' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/تلفن' --note 'page 80, node 9: Persian telefon borrowed from French téléphone' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/abandon' --note 'page 80, node 13: abandon < OF a bandon < ML bannum < Gmc *bannan' 2>&1 | tail -3"
}
```


### [2026-09-05T06:10:09.785Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/34c32a556259e090.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8ee6532966c60366.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a7b57ad5a122cd44.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ca91075c47cd6dd2.txt
```


## [2026-09-05T06:10:16.578Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WLD Bd2 ==\"; ls incoming/WLD/ ; awk 'BEGIN{RS=\"\\f\"} /f[aā]ri/ && /bann/ {print \"leaf\",NR}' incoming/WLD/WLD_Bd2_pages.txt | head"
}
```


## [2026-09-05T06:10:18.058Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC bhad ==\"; grep -n -E 'bhad-|bhādos|batiza' IEC.txt | head -10; echo \"== IEC bha speak ==\"; grep -n -E 'bhāmi|bhānō|bhāti' IEC.txt | head -10"
}
```


### [2026-09-05T06:10:21.697Z] TOOL RESULT

```
== WLD Bd2 ==
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
leaf 129
```


### [2026-09-05T06:10:21.773Z] TOOL RESULT

```
== IEC bhad ==
1457:bhodh- (2) ‘good’ W bodd ‘goodwill, consent’; MHG bat “help, use’. (Extn. in Go. batiza beside MHG radical baz "better" implies a radical *bhod-)
== IEC bha speak ==
1112:bhāl- (3) (?) ‘speaker’. Cf. bhāið, bhāmi MHG buole, OFris. bōla ‘wooer’; OCS balij ‘incantator, doctor; cf. (*-á- in) Skt. bhale ‘expound’; Du. bellen ‘ring’
1116:bhāmā (bhāmos})} ‘sound, voice, rumour’ Skt. cf. bhamah (‘light’. For parallels see bhàió, bhāmi); Gk. phéme, Dor. -à-; Lat. fama. Cf. Myc. (in a name) A(n)ti-pamo 'Antiphamos'
1124:bhàánioó ‘declare, show’. WP II, 122. Cf. . bhāmi, bhàið, bhànos Vedic bhánàmi, Skt. bhanami “speak, declare’; Arm. banam ‘open’; Gk. phaíno; Lat. cf. af- faniae ‘gossip’; Du. boenen, LG bohnen ‘polish’; OlIr. cét-banim ‘notice’; Ir. (denom.) bánaim “lay bare? MHG (denom.) banen "open up’ beside bannen ‘declare’; OE bannan ‘sum- mon, proclaim’; OFris. bania ‘indict’ beside banna "order, proclaim’; ON banna “forbid, curse’. Uncertainly Arm. banim ‘do’; Alb. bâj, T bënj, bëj ‘do’. Gmc. LW in O & Mod. Cz. boniti (... hrózu, ... hrůzu ‘terrify’). Cf. also Gk. phanë, phanerós; W ban “promi- nent; prominence’ and Mod. Icel. banda ‘to beckon’; (a) Srb. banem; bann se “arrive unexpectedly; swagger
1126:bhānos, à, us ‘visible, plain, bright; bright- ness, sign, show’. WP II, 122. Cf. bhāið, bhāmi, bhånið Skt. bhànüh ‘brightness, sun’; Av. banus ‘ray’; Oss. bon ‘day’, cf. also bonäi “by day’; bänn ‘princess, lady’; Gk. phānós; Ir. bán ‘white, bare, baid’; OE bon *'ornament; Du. cf. boenen ‘polish, clean’; G (fr. LG) bohnen, id.; Srb. cf. banem, banuti 'arrive unexpect- edly? beside baniti se ‘swagger, show off. Uncertainly to Arm. ban, i-stem “speech, word, promise, thing”
1175:bhåu- (1) ‘shine, show; tell’. Cf. bhaio, bhāmi Arm. cf. ham-bav (o-st. ‘report, news’, fr. *som-bhau-); Gk. pháos, n. and phós (fr. *bhauos, and -es-stem) beside pháo, pháuo light, v.; cf. phanós ‘bright’ and piphaüsko ‘show’; OE bywan ‘polish, decorate’; cf. MHG bou- in bouchen ('sign', fr. *bhau- + *gn-, see ĝn-, &nósKo, w. sim. formation to MHG zei-chen, see dai- ‘divide’), OE beacen ‘beacon’; cf. Icel. bákn “monster”
1285:bhətis, os ‘speech, declaration; speaking, spoken, declared". WP II, 123. Cf. bhaio, bhāmi Arm. baj, Let ‘verb’; Gk. phásis beside á- phatos ‘ineffable’; Lat. cf. in-fit (2) (quoth'. Plautus); in-fitiae ‘denial
```


## [2026-09-05T06:10:36.337Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC bhōnā ==\"; grep -n -E \"bh[oō]n[aā]|phōnē|phone'\" IEC.txt | head -5; echo \"== SYN physician ==\"; grep -n -o -E \"Pers\\. pizi[sš]k.{0,200}|pizi[sš]k.{0,200}\" SYN.txt | head -5; echo \"== SYN good/better ==\"; grep -n -o -E \"Goth\\. batiza.{0,200}\" SYN.txt | head -3"
}
```


## [2026-09-05T06:10:37.048Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==129' incoming/WLD/WLD_Bd2_pages.txt | head -60"
}
```


### [2026-09-05T06:10:38.036Z] TOOL RESULT

```
== IEC bhōnā ==
== SYN physician ==
== SYN good/better ==
7883:Goth. batiza ‘better’, etc. Feist 103.
20593:Goth. batiza batists ‘better, best’, etc. '
29653:Goth. batiza ‘better’, ba- tists ‘best?. Walde-P. 2.151f. Falk- Torp 67.
```


### [2026-09-05T06:10:39.654Z] TOOL RESULT

```
 '                                                                                                           ;




124                                             bhai- : bbai- : bhl-


tJberlieferung'*          (Denom. osk. faamat etwa                              fahula „Rede,            Sage“,
fas eig. „Ausspriich, bes. gottlicher oder richterlicher ; gottliches Eeclit“
(wohl aus [ne]fas est mit infiaitivischem fas „e3 ist [nicht] auszasprechea^,
s.    Vf. LEWb.*          8.    V.   und    —   altes   *fas, nichl:             fordernd          — Bgm. IF
 2,149a, 179, IF. 30, 352; dazu dies fastus „Spruchtag fur den Prator'^,
fasti „da3 Verzeichnis dieser Tage, Kalender“)          als Ableitung von einem
                                                                          ;


Ptc. *bho-t6-s, lafe. fateor, -eri, fassus (in einzelnen Spuren auch fatari)
„bekenaea, zugebea“                   =
                            osk. fatiiim „fari'' (Lit. bei v. PlantaII 272; aber
 die von Zimmer KZ. 24, 209, Pick I* 489, II^ 159 weiter verglichenen air.
doadbat „demonstrat“ usvir. vielmehr zn ueld- „sehen‘‘),
    Aisl. bon, bon „Bitte, Gebet'', ags. ben „d3., Forderung'' {^bha-nl-s    oder                        ;


mlt o-Abtoming wie gr. (pcovijl); ags.             „prahleA^ (llolthausen KZ. 48,
238; wie lat. for aus *fai6r, slav. bijq; zur Abgrenzung gegeniiber dem
unthem. bha-mi             s. Bgm. 11^ 3, 100, 102, 197).

    Aus dem Balt, allenfalls (mit formantischem n, vgl. dieselbe Erw. bei
6 a- „scheinen, leuchten“) lett. 6
  2                                         „Gerucht, Nachrede“ (Bezz. BB. 27,
 178—182, Trautmann Bsl. Wb. 24; oder dehnstufig zu bheiidh-, vgl. gr.
nvaxtg „Kuade, Nachricht, Geriicbt, Ruf'^, Persson Beitr. 1 17 a 1?         Uber                     —
lit. boja,  boti „worauf achten'', Pick I^ 489, s. vielmehr v. d. Osten-Sacken
IP. 33, 206).
      Russ, - Serb. -ksl. baju,             bajati   „erzahlen, besprechen, heilea'‘ (usw., s.
Berneker           39),   ksl.       basm   „Pabel,     Ziuberspruch“, aksl. bahji, gen. -hj§
„Arzt'‘      (s.   auch Berneker 42).
      Auf einem Pras. *bh9-no (vgl. o arm, ban                    ;
                                                                       vollstufig aisl. bon, gr. ipcov^)
beruht aL bhdnati „spricht“; auf ^bhe-n-6q (: ^bha-ij- in lett. banma^.i)
oder auf germ. Umbilduug nach spannan, ahd. bannan red. Yerb. „unter
Strafandrohung befehlen, verordnen, in Bann tun“, ags. bannan red. V.
„vorladen, befehlen", aisl. banna schw. V. „verbieten", wovon ahd. ban,
pi. banna „Gebot unter Strafandrohung" (nhd. Bann,       Bannwald), ags.
gebann, aisl. bann n. „Yerbot, Bann" (diese Gruppe nicht nach Loewe
KZ. 39, 269 f. als *bandn- zu binden, "^bhendh-, was auch nicht durch die
rom. Sippe von it. bandito „Yerbannter; Yerbrecher" usw. gestiitzt wird, s.
Meyer-Liibke Rom. Wb. Ko. 930). Ir. bann, i. dligheadh Tnicht Sihev forbann
„mandatum"), ist germ, (Pick IP 159 zw.; ir. atboind „er untersagt" viel-
mehr zu *bheiidh-)»
      Ygl.   im allgem. Curtius 296, Pick I^ 88, 488, 4S9, IIP 256.

fobal-: bhai- : bhl- (hhiia-) j,sich fiirchten^.
                                               Dieser Wzansatz nach Persson
        Beitr. 234f.     (gegen Hirts Abl. 100
                               700                                    —
                                                   vgl. auch Idg. Gr. II 117,
        134        —
```


## [2026-09-05T06:10:49.103Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29645,29660p' SYN.txt; echo \"=== buck physician ===\"; grep -n -i -o -E 'physician.{0,120}' SYN.txt | sed -n '1,8p'"
}
```


### [2026-09-05T06:10:50.882Z] TOOL RESULT

```
6. Lith. geras : girti ‘praise’, Skt. gr-
‘sing, praise’, etc. (16.79), 1.686. Buga, Kalba ir Secor Meee
Lith. labas (usual only in greetings a labas rytas, laba diena ‘good Mornin 3 good day’), Lett. labs, OPruss, rae Lith. ee ‘possessions, riches’, lobtj ‘wet rich’, Skt. labh- ‘seize, grasp’
2.385. gente or
7. ChSl. dobrii, ete., genera] Slavic (Russ. dobryj now in phrases like ‘good day’, but mostly ‘kind’) : po-doba jesttt ‘it is becoming’, po-dobiti ‘make fitting’, Goth. Gutatan ‘happen’, OF ge-dafen becoming’, etc. Berneker 208-5, Walde-P. 1.824 f.
ChSl. blagt (reg. for dyaGss and xpn- orés ‘good’ in moral sense, cf. Jagié, Ent- stehungsgesch. 326), in modern Slavic mostly ‘gentle, blessed, noble’, etc., never general for ‘good’, etym. dub. Walde-P. 2.182. Berneker 69.
Russ. chorosij (has displaced dobry; as the common word for ‘good’), orig. ‘or- derly, neat’, hypocoristic formation fr. ORuss. choronent, pple. of choroniti ‘put in order’: ChSl. chraniti ‘guard, keep’. Berneker 397. Jagié, Arch. sl. Ph. 6.282 ff.
8. Skt. sddhu-, orig. ‘straight, right, ready’, fr. sadh- ‘reach one’s goal, ac- complish, guide aright, etc.’. Walde-P. 2.450.
Skt. bhadra-, also ‘blessed, auspicious, fair’, prob. : Goth. batiza ‘better’, ba- tists ‘best?. Walde-P. 2.151f. Falk- Torp 67.
Skt. vasu- (Vedic in this sense; later mostly as neut. sb. ‘goods, wealth’), AY. vanhu-, vohu- (OPers. only in prop c names, as Dadraya-vaus, Vau-misa) : Gall. -vesus (in Bello-, Sigo-vesus, ete), Gme. Wisu-rth, -mar, Wisi-Gothae, ett,
Ir. feib ‘excellence’ (dat. sg.), W- a ‘fine, splendid, gay’, etc. Wa. 1.310. site
OPers. naiba (clearly ‘g00
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
igitized by Arya Samaj Foundation Chennai and eGangotri
. TEMPERAMENTAL, MORAL, AESTHETIC NOTIONS 1177 3 and so, rather than For the numerous other Indo-Iranian 7 jnscr- 4 5) = ¢ ’ ¢ J Dsiva y, elsewhere) : Ir. noib ‘holy’, | words that may be used for ‘good’ (and ipeautifu ’- bho-) fr, the root seen in Ir. | ‘bad’), cf. Schwyzer, Die altindischen und b. ( tia ce’, Lat. nitére ‘shine, glit- | altiranischen Worter fiir gut und bése, niam Pade. 9.321. Festgabe Kaegi 12 ff. ter’: 16.72 BAD 4s (8v0-) Goth. ubils Lith. blogas, negeras, piktas Grk. og ON vandr, illr, daligr Lett. sltkts, nelabs, l’auns NG Bae i Dan. ond, slet, slem, daarlig Chsl.  zitlit Lat. a tivo, malo Sw. ond, elak, ddlig SCr.  nevaljan, zao It. Eats OE yfel (earg) Boh. &patny, zly Fr. mal(o) ME _ wvel, ill, badde Pol. aly Be wil NE bad (ill, evil) Russ. plochoj, chudoj, dur- He Pie (Grach-, do-) Du. slecht, kwaad, erg noj Nir. ole (droch-, do-) OHG ubil Skt.  pdpa-, asddhu-, abha- WV * drwg (dy-) MHG tibel, bese dra- (dus-) Br. fall, gwall, drouk NHG schlecht, schlimm Ay. aka-, aya-, avawhu- : ; (bése, tibel, arg) (dus-)
For ‘bad’ as the opposite of ‘good’ there are equally generic words in some of the IE languages, but in others a vari- ety of terms partly differentiated in feel- ing and according to the object qualified, so that it may be difficult to say which is the more nearly generic. Some are mainly ‘evil, wicked’ in the moral sense.
=== buck physician ===
7860:physician’. These then meant properly only ‘treat medical- ly’, but generally acquired the optimistic
7872:physician’ (whence also poet. md te Lat. medicare), medicina ‘medi- ee ‘remedy, medicine’, etc. hy vi-mad- ‘physician’, vi-madaya
7872:physician’, prob. an early special- ization of the root *med- in Grk. péedopar ‘be mindful of’, Lat. meditdri ‘reflect on’, Ir. m
7882:physician’ (4.87).
7887:physician’ (4.87), with form in- fluenced by lachenén, etc. (above). Weigand-H. 1.90.
7895:physician’), early Slavic borrowing from the Gme. group in Goth. lékinon, etc. (above, 4). Berneker 710. Stender- Petersen 330 f.
7897:physician’), Ay. bigaz-, etym.? Walde-P. 2.449, Barth, 966 f.
7899:PHYSICIAN
```


## [2026-09-05T06:10:58.775Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7893,7912p' SYN.txt"
}
```


### [2026-09-05T06:10:58.827Z] TOOL RESULT

```
Digitized by Arya Samaj Foundation Chennai and eGangotri
308 SELECTED INDO-EUROPEAN SYNONYMS
‘physician’), early Slavic borrowing from the Gme. group in Goth. lékinon, etc. (above, 4). Berneker 710. Stender- Petersen 330 f.
Boh. hojiti, Pol. goié = SCr. gojiti ‘care for, rear’, caus. to ChSI. 27iz, etc. ‘live’, (4.74.) Walde-P. 2.668. Berneker 319.
7. Skt. bhisaj- (only RV 8.79.1), and bhisajya- (fr. bhigaj- ‘physician’), Ay. bigaz-, etym.? Walde-P. 2.449, Barth, 966 f.
Skt. czkitsa- ‘aim at, care for, etc,’ then also ‘treat medically, cure’ (cf, also cikitsd- ‘medical practice’), desideratiye of cit- ‘perceive, intend, attend to, etc,’
4.87 PHYSICIAN
Grk. tarpés Goth. lékeis Lith. gydytojas
NG ytarpés ON leknir Lett.  drsts
Lat. medicus Dan. lage ChSl. — baltji, vratt, lékart It. medico Sw. lakare SCr. lijetnik, lijekar Fr. médecin OE lace Z Boh.  lékar
Sp. médico ME leche, fisicien Pol. lekarz
Rum. medic NE physician, doctor Russ. vraé, lekar!
Ir. liaig (midach) Du. arls Skt. bhisaj-, vaidya-, Nir. = liaigh OHG § lachi, arzat cikitsaka- W. meddyg MHG arz(e)t Av. vimad-
Br. medesin NHG arzt
The majority of the words for ‘physi- cian’ are connected with the verbs for ‘cure’, discussed in 4.86. Some are words for ‘teacher’ or ‘learned person’ used in specialized sense. Several, ac- cording to their probable etymological connections (cf. below, 3, on Ir. laig, ete., and 6 on ChSl. baltji and vract), reflect the primitive antecedent of the physician, the ‘conjurer’ or ‘medicine man’. Cf. also under ‘medicine’ (4.88), and Schrader, Reallex. 1.58 f.
1. Grk. tarpés, Hom. and dial. tarip : tdouar ‘cure’ (4.86).
2. Lat. medicus (> It. medico, OFr. mie, miege; and learned borrowings Sp. médico, Rum. medic; Fr. médecin, back formation to médecine ‘medicine’, 4.88), also poet. and late Lat. medéns pple. : medéri ‘cure’ (4.86).
3. Ir. liaig, NIr. liaigh, prob. fr. *lép-agi- ‘conjurer’ : W. llef ‘voice’, MW llefein ‘cry’, Br. lefiv ‘groan’, Skt. lap- ‘chatter, talk, whisper’, etc. Hence prob. (though also disputed) the Gmc.
group, Goth. lékezs, OE l@ce (> ODan. leke, Dan. lage), MI leche (NE leech arch.), OHG ldchi, and (re-formed after the verbs) ON leknir, Sw. ldkare; fr. Gmc. the Slavic group, late ChSl. lékari, SCr. lijekar (reformed lijeénik), Boh. léka7, Pol. lekarz, Russ. lekar’. Walde-P. 2.429. Walk-Torp 673. Feist 329. Pedersen 1.311. Stokes 251. Berneker 710. Otherwise for Gme. group (: Grk. Aeyw ‘speak’, etc.) Holthausen, If 39.71, Stender-Petersen 330.
W. meddyg, Br. mezec (obs.), also (rare) Ir. midach, fr. Lat. medicus (above, 2). Pedersen 1.239.
```


## [2026-09-05T06:11:07.222Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==454' incoming/WLD/WLD_Bd2_pages.txt | head -25"
}
```


### [2026-09-05T06:11:09.541Z] TOOL RESULT

```
                                                 sag-                                  449

* Lat. segestre „Decke aus Fell^^ hat hiermit nichts zu tun, sondern stammt
au8 gr, oreyaoTQov „Decke, bedeckter Wagen, Sanfte^ mit dissim. Schwund
des ersten t (vgl. Brugmann Grdr.      855, Stolz KG. I 97).
   Hierhergehorig ist jedoch die Gruppe lit. sagis ^Reisekleid der Litaue-
                                                        :


rinnen^,  lett. sagj'cha       Becke der Frauen^, sega „leinene Decke^,
segene „Decke, grofies Tuch, alter Mantel^, segt „decken, hiillen, bedecken“,
apr. saxtis „Rinde“ (Yf. LEWb.^ 670, Fickil^ 289; der Ansatz von urlit.
*smgtia usw. [Wiedemann BB. 29, 314] ist durch lit. sagis wideilegt). Gr.
odyog „Soldatenmantel^ stammt aus dem lat. sagum und nicht umgekehrt
(Prellwitz Et. Wb.).


S§g- „(witternd) nachspiiren'^           (:   *s9g~; oder          g^   b. u.j.

    Gr. Yiyeo/aai „gehe voran, fuhre“ (als der den Weg aufspiirende, suchende),
nachhom. „glaube, meine*^                duco; nicht besser nach Fick GGA.
1894, 237 zu dyco),        ^yejbicov,   „Anfuhrer“; abl. evayrjg „weite Urn-
                                        f]y'gT(joQ

schau gewahrend“? (Prellwitz^ 170; eher zu dyco als „gute Fiihrung bie-
```


## [2026-09-05T06:11:19.284Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==156' incoming/WLD/WLD_Bd2_pages.txt | head -30"
}
```


### [2026-09-05T06:11:21.038Z] TOOL RESULT

```
                                                                    ;                                                  ;




                                                bLongh-j bhngb            bhend-                                 151


    Granz fragwurdig eriunert Weigand-Hirt u. Bengel an                                       lit,   biize   „Keule,
Kloppel am Dreschfleger^                         (nasallos, Palatal!).


bhengh-, bhngh- (Adj. blw^ghiUs) ,,dick, dicht, feist'^
  Ai. baliiU „diclit reichlicli, vier* (Komp. Sup. bijilyas-^ bfjiistha-'^ == gr.
nayvg ) bahidci- „dick, dicht, ausgedehnt, groB, reichlich, viel“ (= gr. na-
            ;


%vXcbg Adv. bei Aristot.,                       wenn dies nicht jiingere Bildung); bqliate (unbe-
legt) ,,mehrt sich“, buhagate „befestigt, starkt'^,                                badhd-   „fest, stark‘‘;
    av.     bazali- n.            „Hohe,    Tiefe'‘,      bq^nu- m.       ds.,   bal. baz „Yiel“, haz „dicht“;
    sehr zw. arm. baztim                        „Yiel'‘   (da aus bJingh-           yielmehr      banjiun zu er-
warten ware, und darum elier                           Lw.— wenn nicht
                                                               zu lit. bed mas   iran.        —
„lMenge, Masse", lett. baft „stopfen", s. Hiibschmann Arm. Gr. I 426 m. Lit.)
    Gr. nayvg           ,,dick,     dicht, feist" fKomp.       naoocov beweist nicht fiir eine Gdf.
pnqliid         = lat. jnngtiAs^                       Bezzenberger BB. 12, 241, Pick       ST, 4S4,
Solmsen KZ.                 33, 295;       s.    vielmehr Prellwitz BB. 21, 2S6, Brugmann IF. 9,
316ff.,  Osthoff MU. YI 56 f. ), jidyog n.                              ,,Dicke"    (nach Tiayvg      fiir   "^TiEyyvg
=   av. bqzah- eingetreten), :^dyETog ds.
```


## [2026-09-05T06:11:30.396Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /batiza/{print \"leaf\",NR; print substr($0,1,120)}' incoming/WLD/WLD_Bd2_pages.txt | head -20"
}
```


### [2026-09-05T06:11:32.169Z] TOOL RESULT

```
leaf 156
                                                                    ;                                                  ;
```


## [2026-09-05T06:11:34.796Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==156' incoming/WLD/WLD_Bd2_pages.txt | grep -n -A6 -B6 'batiza'"
}
```


### [2026-09-05T06:11:36.243Z] TOOL RESULT

```
63-
64-
65- Z. B. Fick II ^ 181, Pedersen KG. I 45.
66-    Yielleicht trotz der etwas andern Bed. mit Schwundstufe hieher                                           auch ai.
67- bhadrd-h         ,,erfreulich, gliicklich, giinstig, gut", n.                „Gluck, Heil", su-bhadra-h
68- ,,herrlich"       — av. hnbadra- ..gliicklich"                 (   Bgm.I^ 411, Pedersen KZ. 36, 84 zw.,
69: Uhlenbeck Ai. Wb. 195, Feist Got. \Yb.^* ^ u. batiza).
70-   Andrerseits wird bliadrd- \z, B. von Fick I* 87, 487 f., 111*258) unter
71- einer ^Yz,            %hdd- „gut“ verglichen mit
72-
```


## [2026-09-05T06:11:45.502Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==156' incoming/WLD/WLD_Bd2_pages.txt | sed -n '40,80p'"
}
```


### [2026-09-05T06:11:46.948Z] TOOL RESULT

```
    Lit. zur
idg. Artikulationsschwankung aufzufassen sei i'Zupitza KZ. 37, 3S8) oder
daB nur pingnis, Tiayvg als 'pvgliu- mit ai. balm- (das dann idg. b- habe)
infolge eines friihidg. Wandels von b- zu p- zusammengehore (Thurneysen
lA. 22, 65), sind unstatthafte Annahmen, die eine einzelsprachliche Schwierig-
keit zu friih durch uridg. Konstruktionen zu beseitigen streben Brugmann                               :



IF. 9, 346 erwagt Kreuzung eines '^fingu-is      Ttayyg, balni- mit einem zu=
oplmiis^ Tiicov gehorigen Worte, was ich M egen der auf ein altes w-Adj.
weisen den Form seiner andern Annahme vorziehe, daB               lediglich der
Jsachkomme eines phm-g^o- (gebildet wie jv-fi-pog von ten- „schwellen")
sei; also pingiiis                = yimos JeW              -{-"^fingiiis „dick".


bhend- etwa ,,singen, schon klingen, jauchzen".
   Ai. bhandate „empfangt jauchzenden Zuruf, wird gepriesen, glanzt",
 bhdndistha-h .,am lautesten jauchzend, gellend, am besten preisend", bhan-
ddna-Ji jauchzend'", bhanddna .Justiges Tonen, Jauchzen" (die Bedeutungen
z.T. bezweifelt; schwundstufig air. mir. hind „meiodisch", abret. bann „canora".
                              ;



 Z. B. Fick II ^ 181, Pedersen KG. I 45.
    Yielleicht trotz der etwas andern Bed. mit Schwundstufe hieher                                           auch ai.
 bhadrd-h         ,,erfreulich, gliicklich, giinstig, gut", n.                „Gluck, Heil", su-bhadra-h
 ,,herrlich"       — av. hnbadra- ..gliicklich"                 (   Bgm.I^ 411, Pedersen KZ. 36, 84 zw.,
 Uhlenbeck Ai. Wb. 195, Feist Got. \Yb.^* ^ u. batiza).
   Andrerseits wird bliadrd- \z, B. von Fick I* 87, 487 f., 111*258) unter
 einer ^Yz,            %hdd- „gut“ verglichen mit
```


## [2026-09-05T06:12:41.275Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -E 'hu\\.?ba[^ ]{0,6}ra[^ ]{0,4}.{0,150}' BRT.txt | head -5; echo \"--2--\"; grep -n -o -E 'b[a@ä][δSd89]ra-.{0,120}' BRT.txt | head -5; echo \"--3--\"; grep -c 'glücklich' BRT.txt"
}
```


### [2026-09-05T06:12:43.115Z] TOOL RESULT

```
30308:hubao8i'tara-  Adj.  'der  wohlriechen- '«it  gutem  Zuerst-,  Zuvorsein',  erL:  ihrpaiih;^  dcrc':  vaiB  .  .  hubandt^  °tarö  anyaliby3 So.:  präklaimk;  s.  
--2--
17241:baSra-  m.''  (vll.)  'Krankheit':  'rs  F.  16. Zum'V.  batt:  —  Pü.:  bann,  angeblich  bahüa 'ditficult' >),  wahrscheinli
30328:ba8ra-  Ad,,  'glücklich':  ^frayair,
--3--
9
```


## [2026-09-05T06:12:45.095Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '30320,30340p' BRT.txt"
}
```


### [2026-09-05T06:12:45.140Z] TOOL RESULT

```
yza>asca  ÄSsna^ras/a  Y.3&.  3.  „  j,s,„}„  „„a    AW»  *«  ('Quitte')  »  lätrUg
PFP.  lum  V.  4/or-.  —  Pü.:  AmüaraiiA  tmii  ('Orange'?).
ataäii  dahel,  erL:  bi  nän  namCFeucbtiEkeit')  ■    ,       .              .  ,.    ,^                ,   ,            n.
anäar  Im  rawäi  i^ät;    im  GrB.  scheint    lu  '  1-  hu-baya-   Adj.  (fem.  •Ja-)    'gutes  EhC;
entsprechen:     äfi    anäar  fest  1  gSspaadän  u  glück    geniessend   Und  gewährend':     yfrUl
marluniäa;  vgL  lu  maeiani-'l.  'yä{APt)  Au/jorTs'''' ^uraolavAS  Vr,  2.  7,
.  j.  hup,r,awy.-  Adj.  (fe„.  y^-)  'eui,  tl^^T.,"!  SrC  '""*  "  '^'
bequem  zu  passiren  :    yaäa  nä  buyst  .  .  ...»         a  j-    (  1,.  1 1-  ■..    4-^-
•äw  mSf.)'>  äfl  'nävaya  Yt.76.3.  '  J"  hu-ba8ra-  Ad,,  'glücklich':  ^frayair,
Ableit.  am  •kM.p»->t,^-^-i  Adj.  -guten  Durch-,  «>?«  i^ai'afA   (Sp.gsi'-"-)   -rB^AupathsaätH
Cbergaogbietend'johneBedeutungsänderung;  aaa  apare  (sd.)   ..  Aog.jJ.
vgl.  dazu  ai.  suhöita- :  jv^di^u-.    ~~    0   Statt  ai.  tibkadra-  Adj.  'herrlich' ;  mp.  (Pü.)  iuJiLtr
•lyj,  S  2Ö1J.  32.  —   ")  Vgl.  '" hu/)rf%wim.  'glücklich';  vgl.  Hbm.  PSt.  33,
•  j.  hupö.busta-  Adj.  'wohl  durchduftet,  •  P-  ^''u-barata-  Adj.  'der  gut  lu  halten, parfdmirt':  aliqm  gäiava  hUtinU  ..  Ha  wohl  zu  pflegen  isf:  marHy^  hyif  dautiä Yt  /".  9.  *  I  ''^"^     avam  '/am    abaram    kyc^  .  ,  avam
Komp.:   hi'-Yupa^busta;  zum  V.  iaorf-;    vgl.  ""u/rasatam  aparsam    "..  den  hab  ich  gut %  36S.  1  und  2Ä4  D.  [gehalten  .  ."  Bh./.8;  4.13.
•  j.    hu-puftra-    Adj.    (fem.  -ri-)    Adj.  I     ^^^-  ""  ^-  "*"-  "  »'■  **'"-'^^-  ^'^i- 'treffliche   Söhne,    Kinder  habend':   nüi/-»  j- hu-barana-  Adj.  'gut  zu  reiten":  aipa tarn  .  .  *daste    'rm    "nicht   macht  er  sie  r"«  ■  ■  ^"^'^  hvazSna  Vyt  4S.
zur  Mutter  trefflicher  Söhne"  Y./0.15.  ''™(''  """  ^-  '*^-  *'  "^^  """^
ai.  iHpuirä-  Adj.  (fem.  'rä-).    —    Pü.:  val  rA         J-  f^^-^ämya  Yt.  7a  143'  '«»  ^i«  '*  (^d-). dahihit  hupusik  (Sü.:  jv/üfraft-o™).  «  j.  hu-bsratay-  f.  i)  'gute  Darbringung*:
•  j.  hu-ptar-  Adj.  (fem.  'fshrl-')  'der  einen  \yd^a  . .  atmia  spmta  .  .paitisqn  ^'nitlmca guten  Vater,  gute  Eltern  hat,    von  ^Xct\*uHa.b)r)itlm^a  *van/a.b>r3itlmfa  Y.60.6;
dby  Google
1829  hub«r9tö  —  hufraya§tayae/a  1830
```


## [2026-09-05T06:13:11.792Z] TOOL CALL #63: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-05T06:13:11.838Z] TOOL RESULT

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


## [2026-09-05T06:13:16.389Z] TOOL CALL #64: Bash

```json
{
 "command": "cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg80.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/80.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/80.png"
}
```


### [2026-09-05T06:13:16.453Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 58953 Sep  5 02:13 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/80.png
```


## [2026-09-05T06:21:18.331Z] TOOL CALL #65: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-80.json",
 "content": "{\n  \"pdf_page\": 80,\n  \"book_page\": 50,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Bhâ 2\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *bʰeh₂- (older notation *bhā-) 'to speak, say'\",\n      \"note\": \"The root itself is real and correctly labelled: Pokorny's second entry on p.105-106 is '2. bhā- \\\"sprechen\\\"' (Gk. φημί, Lat. for/fārī, Arm. ban, ai. bhánati, ahd. bannan), and Watkins/AHD has 'bha-2. To speak. Contracted from *bhaə-. [Pok. 2. bhā- 105]'. Nourai's page reference POK:105 is exact. The second half of his gloss, 'heal', is also Pokorny's, but it rests on two very different pillars. (a) The Slavonic branch is solid and uncontroversial: Pokorny 106 lists 'russ.-serb.-ksl. bajǫ, bajati \\\"erzählen, besprechen, heilen\\\", aksl. balьji, Gen. -ьję \\\"Arzt\\\"' — healing by spell, the same semantic bridge Buck describes at 4.87 ('reflect the primitive antecedent of the physician, the \\\"conjurer\\\" or \\\"medicine man\\\"'). (b) The Indo-Iranian branch, which is the only one Nourai actually draws (node #1), is not Pokorny's own view but a bare citation of Kuiper: 'Nach Kuiper (AO. XII 262) hierher (*bhā-s-) ai. bhiṣákti \\\"heilt\\\", bhiṣáj- \\\"Arzt\\\", jav. -biš- \\\"heilend\\\"'. Modern Iranian scholarship has abandoned that: Cheung 2007 s.v. *bisaz (*baišaz) 'to heal, cure' says flatly 'This root has no IE etymology and may reflect an ancient cultural borrowing, on which see Lubotsky, Early Contacts: 310', and his PIE/Pokorny line is left empty. Buck 4.86 already wrote 'Skt. bhiṣaj- …, Av. bišaz-, etym.?'. English Wiktionary's *bʰeh₂- page lists no Iranian or Indic word for 'heal' among the descendants. So: 'to speak' confirmed, 'heal' true only of the Slavonic sub-branch and rejected for the Iranian words that make up Nourai's whole left-hand branch.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *bʰeh₂- «سخن گفتن» ریشه‌ای اصیل و شناخته‌شده است؛ پوکورنی در صفحهٔ ۱۰۵ کتاب خود آن را زیر عنوان «۲. bhā- سخن گفتن» آورده و واتکینز در پیوست ریشه‌های هندواروپاییِ فرهنگ American Heritage نیز همین را می‌گوید، پس ارجاع نورایی به POK:105 دقیق است. اما بخش دوم معنایی که نورایی آورده، یعنی «درمان کردن»، دو پایهٔ کاملاً جدا دارد: در شاخهٔ اسلاوی این معنا استوار است (اسلاوی کهن bajati «افسون خواندن، درمان کردن» و balьji «پزشک»)، ولی در شاخهٔ ایرانی—که تنها شاخه‌ای است که نورایی رسم کرده—پوکورنی خود تنها پیشنهاد کویپر را نقل کرده است. ریشه‌شناسی امروزی این پیوند را رد می‌کند: چونگ در فرهنگ ریشه‌های فعلی ایرانی (۲۰۰۷) زیر *bisaz می‌نویسد که این ریشه «هیچ ریشه‌شناسی هندواروپایی ندارد و شاید وام‌واژه‌ای فرهنگی و بسیار کهن باشد»، و باک نیز پیش‌تر در برابر اوستایی bišaz- تنها علامت پرسش گذاشته بود. پس: «سخن گفتن» درست است، ولی «درمان کردن» برای واژه‌های ایرانی این نمودار پذیرفتنی نیست.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eh%E2%82%82-\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:105\",\n          \"status\": \"supports\",\n          \"note\": \"POK_01.txt, form-feed leaf 114 (page marker '105' immediately precedes): '2. bhā- \\\"sprechen\\\". Ai. wahrscheinlich in sabhā \\\"Versammlung\\\" … gr. φημί, dor. φᾱμί \\\"sage\\\" … lat. for; fārī (aus *fa-i̯ō(r) = ksl. bajǫ, ags. bōian) \\\"sprechen\\\" … russ.-serb.-ksl. bajǫ, bajati \\\"erzählen, besprechen, heilen\\\", ksl. basnь \\\"Fabel, Zauberspruch\\\", aksl. balьji \\\"Arzt\\\" … Nach Kuiper (AO. XII 262) hierher (*bhā-s-) ai. bhiṣákti \\\"heilt\\\", bhiṣáj- \\\"Arzt\\\", jav. -biš- \\\"heilend\\\". WP. II 123 f.' The article begins on p.105 and runs to p.106 — the page number is exact, and it is the source of both halves of Nourai's gloss.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"AHD\",\n          \"where\": \"AHD_watkins1985.txt, appendix s.v. bha-2\",\n          \"stance\": \"partial\",\n          \"note\": \"'bha-2. To speak. Contracted from *bhaə-. 1. Latin fari, to speak: FATE; AFFABLE, … INFANT, … PREFACE. 2. Greek phanai, to speak: -PHASIA; PROPHET. 3. Suffixed form in Germanic *banwan, *bannan, to speak publicly … 5. Suffixed form *bhā-mā in: a. Latin fama … b. Greek phēmē … 6. Suffixed o-grade form *bhā-nā in Greek phōnē, voice, sound … 7. Suffixed zero-grade form *bhə-to- in Latin fatēri … [Pok. 2. bha- 105.]' Every Latin, Greek, Germanic and English item of Nourai's chart is here — but Watkins glosses the root simply 'To speak' and lists no 'heal' sense and no Iranian word.\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"WLD_Bd2_pages.txt leaf 129 = Bd. II p.124 (root *bhā- 'sprechen', WP II 123 f.)\",\n          \"stance\": \"partial\",\n          \"note\": \"'Russ.-serb.-ksl. bajǫ, bajati \\\"erzählen, besprechen, heilen\\\" …, ksl. basnь \\\"Fabel, Zauberspruch\\\", aksl. balьji, gen. -ьję \\\"Arzt\\\"' and 'ahd. bannan red. Verb. \\\"unter Strafandrohung befehlen, verordnen, in Bann tun\\\", ags. bannan …, aisl. banna \\\"verbieten\\\"'. Walde-Pokorny (1927) already carries the Slavonic 'heal' sense and the Germanic ban-family, but has NO Indo-Iranian 'physician' material — Kuiper's suggestion is later (1938/39) and was added only in Pokorny 1959.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck 4.86 (cure/heal) and 4.87 (physician), SYN.txt lines 7897 and 7899 ff.\",\n          \"stance\": \"contradicts\",\n          \"note\": \"'7. Skt. bhiṣaj- (only RV 8.79.1), and bhiṣajya- (fr. bhiṣaj- \\\"physician\\\"), Av. bišaz-, etym.? Walde-P. 2.449, Barth. 966 f.' Buck refuses to give the word an etymology at all, i.e. does not accept the *bhā- connection; but at 4.87 he does confirm the semantic type ('reflect the primitive antecedent of the physician, the \\\"conjurer\\\" or \\\"medicine man\\\"', of ChSl. balьji) that justifies Pokorny's 'heal'.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, IEC.txt entries bhāl- (3), bhāmā, bhāniō, bhətis\",\n          \"stance\": \"supports\",\n          \"note\": \"'bhāl- (3) (?) \\\"speaker\\\" … OCS balij \\\"incantator, doctor\\\"'; 'bhāmā \\\"sound, voice, rumour\\\" … Gk. phēmē, Dor. -ā-; Lat. fama'; 'bhāniō \\\"declare, show\\\". WP II, 122 … OE bannan \\\"summon, proclaim\\\"; … ON banna \\\"forbid, curse\\\"'. Mann keeps the 'speaker → incantator, doctor' equation for Slavonic, i.e. the same bridge Nourai's gloss assumes.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"bišazka; baešaza\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Two words of unequal standing. (a) baēšaza- is genuine Younger Avestan, but its meaning is not 'doctor': Bartholomae col. 915-916 gives '1) Adj. (fem. -a-) \\\"heilend, heilkräftig, heiltätig\\\"' (of the moon and stars, of the mąθra) and '3) n., m. \\\"Heil-, Gesundheitsmittel, Arzenei\\\"' — 'healing / remedy, medicine'. The agent noun beside it is the denominative verb bišaz- 'to heal, treat medically' (BRT col. 966: 'aθravanəm bišazyāt … \\\"einen Priester soll man um einen feierlichen Segensspruch kurieren\\\"', V.7.41). So 'medicine' is right, 'doctor/healer' is carried by the derived -ka- noun, not by baēšaza-. (b) bišazka is NOT an attested Avestan or Old Persian word: it is a reconstruction. Nyberg's glossary p.48 writes 'Olr. *bišaz-ka-' with an asterisk, and Wiktionary reconstructs Proto-Iranian *bišajkah; Kent's Old Persian lexicon has no such entry, and the word is unattested in the Achaemenid inscriptions, so the label 'Old Persian' is unwarranted. (c) More seriously, the arrow from the root is rejected by current scholarship. Cheung 2007 sets up an Iranian root *bisaz (*baišaz) 'to heal, cure' with Avestan bišaz-/baēšaza-, MP bēsāz-, Sogdian βyc, NP pizišk, Skt. bhiṣáj-, and comments: 'The denominative form bisaz derives from a noun *biš … This root has no IE etymology and may reflect an ancient cultural borrowing, on which see Lubotsky, Early Contacts: 310'; his 'PIE LIV / Pok.' line is blank. Buck likewise: 'Av. bišaz-, etym.?'. Pokorny himself only reported Kuiper's proposal, and Walde-Pokorny (1927) did not have it at all.\",\n          \"derivation_fa\": \"دو واژه در این خانه است که ارزش یکسانی ندارند. نخست، baēšaza- اوستایی راستین است، ولی معنای آن «پزشک» نیست: بارتولومه در ستون ۹۱۵ـ۹۱۶ آن را صفت «درمان‌بخش، شفادهنده» و اسم «داروی درمان، دارو» می‌داند، و فعل نام‌بنیاد کنار آن bišaz- «درمان کردن، معالجه کردن» است (وندیداد ۷:۴۱). دوم، bišazka واژه‌ای نیست که در اوستا یا فارسی باستان به‌کار رفته باشد؛ نیبرگ آن را با ستاره می‌نویسد (*bišaz-ka- ایرانی باستان) و ویکی‌واژه صورت ایرانی آغازین *bišajkah را بازسازی می‌کند؛ کنت در واژه‌نامهٔ فارسی باستان چنین مدخلی ندارد، پس برچسب «فارسی باستان» درست نیست. مهم‌تر آنکه پیوند این خانه با ریشهٔ «سخن گفتن» را پژوهش امروزی رد می‌کند: چونگ (۲۰۰۷) ریشهٔ ایرانی *bisaz را جدا می‌آورد و می‌گوید «این ریشه هیچ ریشه‌شناسی هندواروپایی ندارد و شاید وام‌گیری فرهنگی بسیار کهنی باشد» و خانهٔ «هندواروپایی/پوکورنی» را خالی می‌گذارد. بنابراین خودِ واژه‌ها درست‌اند ولی پیوند آن‌ها با ریشهٔ *bʰeh₂- پذیرفتنی نیست.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D8%B2%D8%B4%DA%A9\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eh%E2%82%82-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"NYB:48\",\n              \"status\": \"supports\",\n              \"note\": \"NYB_vol2_glossary.txt s.v. bizišk: 'bizišk [bešk\\\\'] a medicine-man, a physician, pl. cas. obl. ~-ān in yātūk--ān witch-doctors … — OIr. *bišaz-ka- (cf Skr bhiṣaj-), whence in NW (with metathesis) *bizaška- > bizišk (MPrth v. next w.; Arm. lw. bžišk), in SW *bisadka- > *bisaθka- > bišihk (MPrs bšyhk). In NP the NW form bizisk, later pizisk.' Nyberg is exactly Nourai's source for the form 'bišazka' — but note the asterisk (Old Iranian reconstruction, not an attested Avestan/OP word).\"\n            },\n            {\n              \"ref\": \"POK:105\",\n              \"status\": \"partial\",\n              \"note\": \"POK_01.txt leaf 114-115: the Indo-Iranian healing words appear on p.106, at the very end of the article, and only as a report of somebody else's opinion — 'Nach Kuiper (AO. XII 262) hierher (*bhā-s-) ai. bhiṣákti \\\"heilt\\\", bhiṣáj- \\\"Arzt\\\", jav. -biš- \\\"heilend\\\"; über av. bišazjāt vgl. Kuiper Nasalpräs. 44 f.' Pokorny neither endorses it nor gives an Avestan form 'bišazka' or a 'doctor' gloss for baēšaza-.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, Altiranisches Wörterbuch cols. 915-916 (baēšaza-) and 966 (bišaz-), BRT.txt lines 16500-16513, 17312\",\n              \"stance\": \"partial\",\n              \"note\": \"'j. baēšaza- 1) Adj. (fem. -ā-) \\\"heilend, heilkräftig, heiltätig\\\" … 3) n., m.; a) \\\"Heil-, Gesundheitsmittel, Arzenei\\\"' and 'j. bišaz- den. Praes. 32 \\\"heilen\\\". \\\"Jemanden (Akk.) heilen, kurieren, ärztlich behandeln\\\"'. Both Avestan words exist; neither means 'doctor', and Bartholomae records no *bišazka-. His etymological line reads 'ai. bhiṣajā- … ap. bišazah?' with a question mark.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Cheung 2007, Etymological Dictionary of the Iranian Verb, s.v. *bisaz (*baišaz)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'*bisaz (*baišaz) \\\"to heal, cure\\\". AVESTAN: YAv. bišaz- \\\"to cure, heal\\\", also YAv. baēšaza- \\\"healing, curative\\\" … © The denominative form bisaz derive[s] from a noun *biš … This root has no IE etymology and may reflect an ancient cultural borrowing, on which see Lubotsky, Early Contacts: 310.' Directly denies the arrow from an Indo-European root.\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian: Grammar, Texts, Lexicon (KNT.txt) — grep 'bišaz|baešaz'\",\n              \"stance\": \"silent\",\n              \"note\": \"No hit anywhere in Kent's Old Persian lexicon: there is no Old Persian *bišazka-, so the 'Old Persian' half of the language label has no attested support.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"bešazak\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The form is real but is not the ordinary Middle Persian word for 'physician'. Horn, Grundriss no. 183, from which Nourai's reference AEF:237 (Khaleqi Motlaq's Persian translation of Horn) derives, lists exactly it: 'aw. baēšaza- \\\"Arzenei, Arzt\\\"; phlv. bēšazak (PPGl.), bēšaz(i)ānīh, bēšazīnītan, bēšazīnītār und auch b(i)žaskīh, Vd. 7 (94)'. bēšazak is thus the SW (Book-Pahlavi/Pazand-glossary) formation *baišaza-ka-, regular from Avestan baēšaza- with the productive MP suffix -ak (< OIr. *-aka-). But the living Pahlavi noun 'doctor' is bizešk: MacKenzie's Concise Pahlavi Dictionary glosses 'doctor bizešk' and keeps bēšāz(ēn)- as the verb 'heal, cure' and bēšāz 'medicinal'; Cheung likewise has BMP/MMP byš'z- /bēsāz-/ for the verb only; Nyberg derives bizišk from NW *bizaška- with s/z metathesis, noting that the SW outcome would have been *bišihk (bšyhk), a form that did not survive. So Nourai's node is a genuine Pahlavi word, but it is a derivative of the verb rather than the etymon of NP pezešk (see node #3).\",\n          \"derivation_fa\": \"«بشزک/بēšazak» صورتی راستین در فارسی میانه است، ولی واژهٔ رایج پهلوی برای «پزشک» نیست. هرن در بند ۱۸۳ «دستور ریشه‌شناسی فارسی نو» — همان بندی که ترجمهٔ فارسی‌اش (اساس اشتقاق فارسی، ص ۲۳۷) مأخذ نورایی است — می‌نویسد: «اوستایی baēšaza- «دارو، پزشک»؛ پهلوی bēšazak، bēšazīnītan، bēšazīnītār و نیز b(i)žaskīh». این صورت با پسوند نام‌ساز ‎-ak (از ایرانی باستان ‎*-aka-) از baēšaza- ساخته شده و صورت جنوب‌غربی است. اما در پهلویِ زنده، اسمِ «پزشک» bizešk است: مکنزی در فرهنگ کوچک پهلوی برای doctor همین bizešk را می‌آورد و bēšāz(ēn)- را تنها فعل «درمان کردن» می‌داند، و نیبرگ می‌گوید صورت جنوب‌غربی می‌بایست *bišihk می‌شد که از میان رفت. پس این خانه واژه‌ای درست ولی نه نیای مستقیم «پزشک» فارسی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D8%B2%D8%B4%DA%A9\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AEF:237\",\n              \"status\": \"not_checked\",\n              \"note\": \"AEF = Khaleqi Motlaq's Persian translation of Horn's Grundriss (Asās-e Ešteqāq-e Fārsi, vol. I); refs_online.json records no digital copy (searched archive.org, ketabnak, noorlib — bookshop listings only). Checked the German original instead, which is the same text: HRN.txt line 1997, entry no. 183 (printed p.44-45): 'biziŠk, bižišk (*bišk) \\\"Arzt\\\" (Šāhn. I, 32 v.180, 182), bižiškī (Šāhn. I, 25 v.43). aw. baēšaza- \\\"Arzenei, Arzt\\\"; phlv. bēšazak (PPGl.), bēšaz(i)ānīh, bēšazīnītan, bēšazīnītār und auch b(i)žaskīh, Vd. 7 (94); ai. bhiṣáj- \\\"Arzt\\\", bheṣaja- \\\"Arzenei\\\"; arm. LW. bžešk, bžeškutiun.' The Pahlavi form Nourai prints is Horn's, so the citation is almost certainly faithful.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, A Concise Pahlavi Dictionary — PHD.txt line 1669 and 3116; PHD_mackenzie.txt line 1562\",\n              \"stance\": \"partial\",\n              \"note\": \"English-Pahlavi index: 'doctor bizešk' and 'physician bizešk, drustabed'; the main list has 'bēsāz(ēn)- [byš'z(yn)-, byš(')c('n)- | M byēz-] heal, cure' and 'medicinal bēsāz, bizagān'. MacKenzie has the verb bēsāz(ēn)- and the noun bizešk, but no noun bēšazak.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 183 (HRN.txt line 1997, printed p.44-45)\",\n              \"stance\": \"supports\",\n              \"note\": \"'phlv. bēšazak (PPGl.) … und auch b(i)žaskīh' — Horn does record the Pahlavi form Nourai prints, and cites it from the Pahlavi-Pazand glossary.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. bizišk\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'in SW *bisadka- > *bisaθka- > bišihk (MPrs bšyhk). In NP the NW form bizisk, later pizisk.' Nyberg explicitly says the SW (Persid) reflex is bišihk and that New Persian took the NW (Parthian) form instead — so bēšazak cannot be the ancestor of pezešk.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"pezešk «پزشک»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Persian word and its meaning are beyond doubt — Borhān-e Qāṭeʿ has it as a headword ('pezešk, on the pattern of serešk: they call the sage, the physician and the surgeon [so]; it also occurs with Persian b-'), i.e. bezešk ~ pezešk. What Nourai's single arrow hides is the route. Both Hübschmann and Nyberg show that NP bizišk/pizišk cannot come from a SW form *bēšazak: it goes back to Old Iranian *bišaz-ka-, which in the north-west (Parthian) underwent metathesis of the two sibilants — *bišazka- > *bizaška- > MP/Parthian bizešk (written bzyšk) — whence Armenian loan bžišk and Kurdish bizišk/pizišk. Hübschmann §112/§122: 'bižisk = bizisk \\\"Arzt\\\" aus *bizizk für *bisizk' and 'bzisk \\\"Arzt\\\" = phl. *bizisk (geschrieben bcšk Shk. 237), umgestellt aus *bisizk'. Wiktionary (following MacKenzie and ESIJa) makes NP پزشک a borrowing from Parthian bzyšk 𐫁𐫉𐫏𐫢𐫐, and Cheung calls NP pizišk 're-introduced'. The final step is the regular New Persian devoicing/spelling of initial b- as p- in this word (bizišk > pizišk > modern pezešk), already noted by Nyberg ('In NP the NW form bizisk, later pizisk').\",\n          \"derivation_fa\": \"خودِ واژهٔ «پزشک» و معنای آن تردیدی ندارد؛ برهان قاطع آن را چنین آورده است: «پزشک، بکسر اول بر وزن سرشک، حکیم و طبیب و جراح را گویند؛ و با بای فارسی هم آمده است»، یعنی «بزشک/پزشک». آنچه یک پیکان نورایی پنهان می‌کند راهِ این واژه است. هوبشمان و نیبرگ نشان داده‌اند که «پزشک» نمی‌تواند از صورت جنوب‌غربی *bēšazak بیاید: نیای آن ایرانی باستان *bišaz-ka- است که در شمال‌غرب (پارتی) دچار قلب (metathesis) دو سایشیِ س و ز شده: *bišazka- > *bizaška- > پارتی/فارسی میانهٔ bizešk (نوشتهٔ bzyšk)، و از همان‌جا وام‌واژهٔ ارمنی bžišk و کردی bizišk/pizišk. هوبشمان در بند ۱۱۲ می‌نویسد «bižisk = bizisk «پزشک» از *bizizk به‌جای *bisizk». ویکی‌واژه نیز «پزشک» را وام‌گرفته از پارتی bzyšk می‌داند. مرحلهٔ پایانی، بدل شدن ب آغازین به پ در فارسی نو است (bizišk > pizišk > پزشک). پس ادعای نورایی در اصل درست است ولی راهِ آن ناقص رسم شده.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D8%B2%D8%B4%DA%A9\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:399\",\n              \"status\": \"supports\",\n              \"note\": \"BQT_v1_pages.txt, form-feed leaf 494 (= printed p.399; vol. 1 has ~95 leaves of Moʿin's introduction before p.1): «پزشک - بکسر اول بر وزن سرشک، حکیم و طبیب و جراح را گویند؛ و با بای فارسی هم آمده است» (OCR reads the headword as 'بز شاث'). Borhān confirms the word, the reading pezešk/bezešk and the gloss 'physician'; it carries no etymological footnote by Moʿin at this entry.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien §112 (HUB.txt line 7999) and §122 (line 8229)\",\n              \"stance\": \"partial\",\n              \"note\": \"'bižisk = bizisk \\\"Arzt\\\": zd. baēšaza- (aber skr. bhiṣaj-, bhiṣakti- ?)' and 'bzisk \\\"Arzt\\\" = phl. *bizisk (geschrieben bcšk Shk. 237), umgestellt aus *bisizk §112'. Hübschmann connects the word to Av. baēšaza- (as Nourai does) but insists on the metathesis and reconstructs the MP form as *bizisk, not bēšazak.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. bizišk (p.48)\",\n              \"stance\": \"partial\",\n              \"note\": \"'OIr. *bišaz-ka- …, whence in NW (with metathesis) *bizaška- > bizišk … In NP the NW form bizisk, later pizisk.' Same etymon as Nourai, different intermediate step.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Cheung 2007 s.v. *bisaz, section *NWIR\",\n              \"stance\": \"partial\",\n              \"note\": \"'*NWIR: NP pizisk (re-introduced), Kurd. (Kurm.) bizisk, (Sor.) pazisk, pizisk \\\"doctor\\\"' — the word is classed as north-west Iranian in origin, i.e. not a direct SW Persian inheritance.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sogdian\",\n          \"words\": \"byc\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Gharib's Sogdian Dictionary, printed p.117, entry 2972: 'βyc B,M — βēč — ⓔ<Av. baēšaza- — ⓞ obl. pl. ~ty ⇒ βyc'n … physician. SCE 272; GMS 384; βycty, BBB 517; gen. pl. βycẖ TSP 9.78, 95; GMS 1230'. The word is attested in both Buddhist and Manichaean Sogdian, and Gharib herself gives precisely the derivation Nourai draws (from the Avestan/Old Iranian baēšaza- family). Cheung lists the same form under his Iranian root *bisaz: 'SOGDIAN: BSogd., MSogd. βyc \\\"physician\\\" (GMS: §384)'. Phonetically βēč continues an Old Iranian *baišaz-/*bišaz- stem with the regular Sogdian development of the cluster to -č and the loss of the final syllable; the derivatives on the same page (βyc'n'k 'medical', βyc'n xwt'w 'god of physicians', βycy'h 'medicine') show it was a productive noun. Nourai's transliteration 'byc' is Gharib's own Latin transcription with β written b, and his page reference SOD:117 is exactly right.\",\n          \"derivation_fa\": \"قریب در «فرهنگ سغدی» صفحهٔ ۱۱۷، مدخل ۲۹۷۲: «βyc (βēč) — پزشک — از اوستایی baēšaza-» و در همان صفحه مشتقات آن: βyc'n'k «پزشکی، درمانی»، βyc'n xwt'w «خدای پزشکان»، βycy'h «دارو». این واژه هم در سغدی بودایی و هم در سغدی مانوی به کار رفته و چونگ نیز آن را زیر ریشهٔ ایرانی *bisaz می‌آورد. از دید آوایی βēč دنبالهٔ ستاک ایرانی باستان *bišaz-/*baišaz- است با تحول قاعده‌مند خوشهٔ پایانی به «چ» در سغدی. آوانگاشت نورایی (byc) همان آوانگاشت خودِ قریب است و ارجاع SOD:117 دقیقاً درست است؛ ادعای نورایی در این گره درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"SOD:117\",\n              \"status\": \"supports\",\n              \"note\": \"SOD_pages.txt, form-feed leaf 183, which prints the folio number '117' in the margin: '2972 βyc B,M — βēč ⓔ<Av. baēšaza- ⓞ obl. pl. ~ty ⇒ βyc'n … physician. SCE 272; GMS 384'. Page number and content both match Nourai exactly.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Cheung 2007 s.v. *bisaz, section *SOGDIAN\",\n              \"stance\": \"supports\",\n              \"note\": \"'*SOGDIAN: BSogd., MSogd. βyc \\\"physician\\\" (GMS: §384)' — same form, same meaning, same Iranian family.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae cols. 915-916 s.v. baēšaza-\",\n              \"stance\": \"supports\",\n              \"note\": \"The Avestan etymon Gharib names is Bartholomae's 'baēšaza- … \\\"Heil-, Gesundheitsmittel, Arzenei\\\"', so the Sogdian word does descend from the word in the parent box.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"fârî\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin for, fārī 'to speak' is the textbook Italic continuation of the root. Pokorny p.106 in the same article: 'lat. for; fārī (aus *fa-i̯ō(r) = ksl. bajǫ, ags. bōian) \\\"sprechen\\\", fācundus \\\"redegewandt\\\", fātum \\\"Ausspruch, Weissagung, festgesetzte Weltordnung, Geschick\\\", fāma \\\"Gerede, Gerücht, Überlieferung\\\" …, fābula \\\"Rede, Sage\\\" (*bhā-dhlā), fās …; als Ableitung von einem Partiz. *bhə-to-s, lat. fateor, -ērī, fassus \\\"öffentlich erklären, zugeben\\\" = osk. fatium \\\"fārī\\\"'. The long ā of fārī is the regular Latin reflex of PIE *eh₂ (*bʰeh₂- > fā-, with initial *bʰ- > Lat. f-), and the deponent present for/fārī reflects a *bhā-i̯e/o- present, matched by OCS bajǫ and OE bōian. Watkins/AHD sets the same equation ('1. Latin fari, to speak'), which is the AHD reference Nourai cites for this box.\",\n          \"derivation_fa\": \"فعل لاتینی for / fārī «سخن گفتن» بازماندهٔ نمونه‌وار این ریشه در شاخهٔ ایتالیک است. پوکورنی در همان مقاله (ص ۱۰۶) می‌آورد: «lat. for; fārī (از *fa-i̯ō(r) = اسلاوی کهن bajǫ، انگلیسی باستان bōian) «سخن گفتن»، fātum «گفتهٔ سرنوشت»، fāma «آوازه»، fābula «سخن، افسانه» و از صفت مفعولی *bhə-to-s صورت fateor «اقرار کردن»». آ کشیدهٔ fārī بازتاب قاعده‌مند *eh₂ هندواروپایی است و ب دمیدهٔ آغازین (*bʰ-) در لاتین به f بدل شده است. واتکینز نیز در پیوست فرهنگ American Heritage همین را می‌گوید. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eh%E2%82%82-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt s.v. bha-2: '1. Latin fari, to speak: FATE; AFFABLE, (FANTOCCINI), INEFFABLE, INFANT, (INFANTRY), PREFACE.' Nourai gives no page for this box; the appendix entry itself is the reference and it says exactly this.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"Pokorny p.106 (POK_01.txt leaf 115), article 2. bhā-\",\n              \"stance\": \"supports\",\n              \"note\": \"'lat. for; fārī (aus *fa-i̯ō(r) = ksl. bajǫ, ags. bōian) \\\"sprechen\\\", fācundus …, fātum …, fāma …, fābula \\\"Rede, Sage\\\" (*bhā-dhlā)'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny Bd. II p.123-124 (WLD_Bd2_pages.txt leaf 128-129)\",\n              \"stance\": \"supports\",\n              \"note\": \"Same Latin material, with the derivation of fateor from a participle *bhə-tó-s: 'als Ableitung von einem Ptc. *bhə-tó-s, lat. fateor, -ērī, fassus \\\"bekennen, zugeben\\\" = osk. fatiium \\\"fārī\\\"'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"infant, fate, fame, confess, preface\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All five are Latin-via-French borrowings within the fārī family, and Watkins/AHD assigns every one of them to bha-2. infant: L. īnfāns, -antis 'not speaking' (negative in- + pres. part. fāns of fārī) → OF enfant → ME infaunt, first of a child too young to speak, hence 'infant' and (through It. infante 'foot-soldier, youth') 'infantry'. fate: L. fātum, neut. pp. of fārī, 'that which has been spoken (by the gods)' → OF fat/It. fato → English 14th c. fame: L. fāma 'talk, report, reputation' (< *bhā-mā, exactly Gk. phḗmē) → OF fame → ME fame. confess: L. confitērī, pp. confessus, from fatērī 'to acknowledge' (< *bhə-to- 'spoken'), whence OF confesser. preface: L. praefātiō 'a saying beforehand', from praefārī → OF preface. Strictly only 'infant' and 'fate' are formed on fārī itself; 'fame', 'confess' and 'preface' come from fāma, fatērī and praefārī — all listed by AHD under the same root, so Nourai's grouping is the standard one.\",\n          \"derivation_fa\": \"هر پنج واژه از راه لاتین و فرانسوی به انگلیسی رسیده‌اند و واتکینز همه را زیر همین ریشه می‌آورد. infant از لاتینی īnfāns «ناسخنگو» (پیشوند منفی in- + اسم فاعل fāns از fārī) از راه فرانسوی کهن enfant؛ fate از fātum «آنچه (خدایان) گفته‌اند»، صفت مفعولی خنثای همان فعل؛ fame از fāma «آوازه» که درست هم‌ساخت یونانی phḗmē است؛ confess از confitērī (بن fatērī «اقرار کردن» از ستاک *bhə-to-)؛ و preface از praefātiō «پیش‌گفتار». به‌دقت، تنها infant و fate بی‌واسطه از fārī ساخته شده‌اند و سه واژهٔ دیگر از مشتقات آن، ولی همهٔ آن‌ها در فرهنگ‌های معتبر زیر یک ریشه می‌آیند؛ پس ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai cites no reference for this box (refs=None); the arrow is covered by the AHD citation of the parent Latin box.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"AHD_watkins1985.txt s.v. bha-2 §1, §5a, §7, and the English index\",\n              \"stance\": \"supports\",\n              \"note\": \"'1. Latin fari, to speak: FATE; AFFABLE, … INFANT, (INFANTRY), PREFACE'; '5. Suffixed form *bhā-mā in: a. Latin fama, talk, reputation, fame: FAME, FAMOUS'; '7. Suffixed zero-grade form *bhə-to- in Latin fatēri, to acknowledge, admit: CONFESS, PROFESS'. The index confirms 'INFANT bha-2', 'FATE bha-2', 'FAME bha-2', 'CONFESS bha-2'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, Comprehensive Etymological Dictionary, s.vv. infant, fate, fame, confess, preface\",\n              \"stance\": \"supports\",\n              \"note\": \"Klein routes each of them through Latin to Old French in the standard way (e.g. infant 'fr. L. īnfāns, gen. -antis, \\\"not able to speak\\\", fr. in-, \\\"not\\\", and fāns, pres. part. of fārī, \\\"to speak\\\"').\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Greek\",\n          \"words\": \"phônĕ : voice; sun-phônĕ : harmonious sound\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"φωνή 'voice, sound' is a secure derivative: Watkins reconstructs '6. Suffixed o-grade form *bhā-nā in Greek phōnē, voice, sound, and phōnein, to speak', Pokorny p.106 has 'mit Ablaut φωνή \\\"Stimme\\\"' next to φημί/φᾱμί, and the ō is the regular Greek o-grade lengthening of the *eh₂ root. The second entry, however, is a morphological analysis rather than an attested lemma: Greek has no *σύν-φωνή. What exists is the adjective σύμφωνος sýmphōnos 'agreeing in sound, concordant' and the abstract noun συμφωνία symphōnía 'concord of sound' — with the regular assimilation of ν to μ before a labial. Klein p.1556-57 s.v. symphony gives exactly this: 'fr. L. symphonia, fr. Gk. συμφωνία, \\\"concord of sound, harmony, agreement\\\", fr. σύμφωνος, \\\"agreeing in sound\\\", fr. σύν (see syn-) and φωνή, \\\"sound\\\"'. The prefix σύν does go back to PIE *sem-/*sṃ- (Nourai's ☞Sem 1 pointer), so the analysis is right; only the citation form is not a real Greek word.\",\n          \"derivation_fa\": \"یونانی φωνή «آوا، صدا» مشتق مطمئنی از این ریشه است: واتکینز آن را از صورت *bhā-nā (درجهٔ o با پسوند) می‌گیرد و پوکورنی در ص ۱۰۶ کنار φημί می‌نویسد «با تناوب واکه‌ای φωνή «آوا»». ولی صورت دوم، sun-phônĕ، واژه‌ای اصیل در یونانی نیست بلکه تجزیهٔ ساختواژی است؛ آنچه در یونانی هست صفت σύμφωνος «هم‌آوا، سازگار» و اسم συμφωνία «هم‌آوایی» است، با همگونی قاعده‌مندِ ν به μ پیش از واک لبی. کلاین (ص ۱۵۵۷) دقیقاً همین را می‌گوید. پیشوند σύν نیز به ریشهٔ هندواروپایی *sem- می‌رسد که خودِ نورایی با نشانهٔ «Sem 1» به آن ارجاع داده است. پس تحلیل درست است، تنها شکلِ مدخل ساختگی است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:1557\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt line 37822, on the leaf that carries the printed page marker 1556 (two printed pages per leaf, so 1556/1557 — Nourai's number is exact): 'symphony, n. — ME. symphonie, fr. OF. simphonie (F. symphonie), fr. L. symphonia, fr. Gk. συμφωνία, \\\"concord of sound, harmony, agreement\\\", fr. σύμφωνος, \\\"agreeing in sound\\\", fr. σύν (see syn-) and φωνή, \\\"sound\\\". See phone, \\\"speech sound\\\".' Klein prints σύμφωνος/συμφωνία, not *σύνφωνή.\"\n            },\n            {\n              \"ref\": \"AHD:1304\",\n              \"status\": \"not_checked\",\n              \"note\": \"AHD:1304 is a page of the main A-Z text of the 1975/76 New College Edition (the IE appendix is pp.1505-1550), i.e. presumably the entry 'symphony'. Only Watkins's standalone 1985 appendix and the current online appendix are available locally/online, so that page could not be inspected; the appendix itself supports the root assignment (see consulted).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"AHD_watkins1985.txt s.v. bha-2 §6\",\n              \"stance\": \"supports\",\n              \"note\": \"'6. Suffixed o-grade form *bhā-nā in Greek phōnē, voice, sound, and phōnein, to speak: PHONE, -PHONE, PHONEME, PHONETIC, PHONO-, -PHONY; ANTHEM, (ANTIPHON), APHONIA, CACOPHONOUS, EUPHONY, SYMPHONY.'\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"Pokorny p.106 (POK_01.txt leaf 115)\",\n              \"stance\": \"supports\",\n              \"note\": \"'gr. φημί, dor. φᾱμί \\\"sage\\\" … φάτις f. \\\"Gerücht\\\", φάσις \\\"Sprache, Rede, Behauptung, Anzeige\\\"; mit Ablaut φωνή \\\"Stimme\\\".'\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"French\",\n          \"words\": \"telephone; symphonie\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Two French words of very different ages, both with Greek φωνή as second element. symphonie is the inherited learned chain: Gk. συμφωνία → L. symphonia → OF simphonie (12th c., first of a musical instrument, then 'concord of sounds') → mod.F. symphonie, the sense 'orchestral work in several movements' being an 18th-century Italian-mediated specialisation. téléphone is a 19th-century neo-Greek coinage on τῆλε 'far' + -φωνον, used by Charles Bourseul and others in French from the 1850s for a sound-transmitting device and fixed on Bell's instrument after 1876; it is not an inherited word but a learned compound built from the same Greek element. Nourai gives no reference here; the box is a passing station for the Persian and English boxes that hang from it.\",\n          \"derivation_fa\": \"دو واژهٔ فرانسوی با دو سنِ کاملاً متفاوت که هر دو جزء دومشان یونانی φωνή است. symphonie زنجیرهٔ به‌ارث‌رسیدهٔ عالمانه است: یونانی συμφωνία ← لاتینی symphonia ← فرانسوی کهن simphonie (سدهٔ دوازدهم، نخست نام سازی، سپس «هم‌آوایی») ← فرانسوی امروز؛ معنای «قطعهٔ چندبخشی ارکستری» تخصیص سدهٔ هجدهم و از راه ایتالیایی است. اما téléphone واژه‌ای ساختگی و نوساخته از عناصر یونانی است (τῆλε «دور» + -φωνον) که از دههٔ ۱۸۵۰ در فرانسه به کار رفت و پس از اختراع بل (۱۸۷۶) بر همین دستگاه ثابت شد؛ یعنی وام‌واژهٔ موروثی نیست بلکه برساختهٔ عالمانه است. این خانه در نمودار تنها گذرگاهی است برای خانه‌های فارسی و انگلیسیِ پس از آن.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No reference is given for this box (refs=None); it is covered by KLN:1557 on the parent Greek box, which explicitly names 'OF. simphonie (F. symphonie)'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt line 37822 s.v. symphony; s.v. telephone\",\n              \"stance\": \"supports\",\n              \"note\": \"'ME. symphonie, fr. OF. simphonie (F. symphonie), fr. L. symphonia, fr. Gk. συμφωνία' — the French stage of Nourai's chart is Klein's. For telephone Klein describes a modern compound of Gk. τῆλε and φωνή.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"AHD_watkins1985.txt s.v. bha-2 §6 (index: SYMPHONY bha-2)\",\n              \"stance\": \"supports\",\n              \"note\": \"SYMPHONY and -PHONE are both filed under bha-2, i.e. the second element of both French words is the φωνή of the parent box.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Persian\",\n          \"words\": \"telefon «تلفن»; gerâmâfon «گرامافون»; samfonî «سمفونی»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are modern French loans in Persian, taken in the late Qajar / early Pahlavi period along with the objects they name, and all three keep the French shape rather than the English one — تلفن telefon (not *telifown) from F. téléphone, سمفونی samfonī from F. symphonie (the final -ī rendering French -ie, as in کمدی komedī, تراژدی terāžedī), گرامافون gerāmāfon from F. gramophone. Wiktionary states plainly for تلفن: 'Borrowed from French téléphone'. Moʿin's Farhang-e Fārsi has all three with a foreign-origin tag and a Latin-script etymon (گرامافون: 'gramophone … آلتی است که صفحه‌ای را که آوازی در آن ضبط شده به گردش در آورد'; سمفونی: '(مت.) قطعهٔ …', i.e. tagged as a music term). One qualification: only the second element of گرامافون belongs to this root — the first is Greek γράμμα 'letter, written character' (PIE *gerbh- 'to scratch'), the word being Emile Berliner's 1887 trade name; the same is true of the τῆλε of تلفن. Nourai's arrow is therefore right for the -fon element of each.\",\n          \"derivation_fa\": \"هر سه واژه وام‌واژه‌های نوی فرانسوی در فارسی‌اند که در اواخر قاجار و اوایل پهلوی همراه خودِ ابزارها وارد شدند و هر سه صورت فرانسوی را نگاه داشته‌اند نه انگلیسی را: «تلفن» از téléphone فرانسوی، «سمفونی» از symphonie (که «ـی» پایانی برابر ‎-ie فرانسوی است، مانند «کمدی» و «تراژدی») و «گرامافون» از gramophone. ویکی‌واژه دربارهٔ «تلفن» صریحاً می‌نویسد «وام‌گرفته از فرانسوی téléphone». معین نیز هر سه را با برچسب واژهٔ بیگانه و ریشهٔ لاتین‌نویس آورده است. تنها نکته این است که در «گرامافون» تنها جزء دوم به این ریشه بازمی‌گردد و جزء نخست یونانی γράμμα «نوشته، حرف» است (این واژه نام تجاری‌ای است که امیل برلینر در ۱۸۸۷ ساخت)؛ همین‌طور «تله‌ـ» در «تلفن» یونانی τῆλε «دور» است. پس ادعای نورایی برای جزء ‎-فون هر سه واژه درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AA%D9%84%D9%81%D9%86\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:1132, 1921\",\n              \"status\": \"partial\",\n              \"note\": \"Nourai's page numbers refer to the 6-volume Amir Kabir edition with continuous pagination, which is not the copy on disk (MON_part1/part2 are a different printing whose running heads show e.g. '۸۷۸ فرهنگ فارسي معین سمفونی'), so the exact pages could not be matched. The entries themselves were found and do support the node: MON_part1 line 79625 «سمفونی: (مت.) قطعهٔ …»; MON_part2 line 30342 «گرامافون: gramophone … آلتی است که صفحه‌ای را … به گردش در آورد … جعبهٔ صوت»; تلفن appears throughout (e.g. MON_part2 line 50407 «مخابره … تلفن‌خانه»).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"MON_part1.txt line 79625 (سمفونی), MON_part2.txt line 30342 (گرامافون)\",\n              \"stance\": \"supports\",\n              \"note\": \"Moʿin lists both as European loanwords with a Latin-script etymon and a technical gloss; گرامافون is defined «آلتی است که صفحه‌ای را که آوازی در آن ضبط شده به گردش در آورد و همان آواز را به گوش رساند. جعبهٔ صوت».\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt s.vv. gramophone, telephone, symphony\",\n              \"stance\": \"partial\",\n              \"note\": \"Klein derives gramophone from Gk. γράμμα + φωνή (a coined trade name) and telephone from τῆλε + φωνή, i.e. only the second element of each belongs to this root.\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"symphony\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English symphony is a Middle English borrowing of Old French simphonie, itself from Latin symphonia and Greek συμφωνία — precisely the chain drawn. Klein s.v.: 'symphony, n. — ME. symphonie, fr. OF. simphonie (F. symphonie), fr. L. symphonia, fr. Gk. συμφωνία, \\\"concord of sound, harmony, agreement\\\", fr. σύμφωνος, \\\"agreeing in sound\\\", fr. σύν (see syn-) and φωνή, \\\"sound\\\"'. It appears in English from the 13th century, first of a musical instrument (hurdy-gurdy, bagpipe) and of 'harmony of sound', the modern sense 'extended orchestral composition' being borrowed anew from Italian sinfonia in the 18th century. Watkins files SYMPHONY under bha-2 §6, confirming the root.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی symphony وام‌واژه‌ای از فرانسوی کهن simphonie در دورهٔ انگلیسی میانه است که خود از لاتینی symphonia و یونانی συμφωνία می‌آید — درست همان زنجیره‌ای که نورایی رسم کرده است. کلاین می‌نویسد: «symphony، از انگلیسی میانهٔ symphonie، از فرانسوی کهن simphonie، از لاتینی symphonia، از یونانی συμφωνία «هم‌آوایی، سازگاری»، از σύμφωνος، از σύν و φωνή». این واژه از سدهٔ سیزدهم در انگلیسی دیده می‌شود، نخست نام سازی و به معنی «هم‌آوایی»، و معنای امروزی «قطعهٔ بزرگ ارکستری» در سدهٔ هجدهم دوباره از ایتالیایی sinfonia گرفته شده است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt s.v. bha-2 §6 lists SYMPHONY among the English derivatives of Greek phōnē; the English index confirms 'SYMPHONY bha-2'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt line 37822 (printed p.1556/1557) s.v. symphony\",\n              \"stance\": \"supports\",\n              \"note\": \"'ME. symphonie, fr. OF. simphonie (F. symphonie), fr. L. symphonia, fr. Gk. συμφωνία' — the whole French→English step of the chart.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etymological Dictionary s.v. symphony\",\n              \"stance\": \"supports\",\n              \"note\": \"Skeat gives the same route, 'F. symphonie, L. symphonia, Gk. συμφωνία, from σύν together and φωνή a sound'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"phone, prophet\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both words belong to the root, but only one of them to the parent box. phone (in phoneme, phonetic, -phone, telephone, and as the linguistic term for a speech sound) is a direct scientific borrowing of Greek φωνή, so its parent is right. prophet, however, does not come from φωνή: it is ME prophete < OF prophete < L. prophēta < Gk. προφήτης 'one who speaks for (a god), interpreter', from πρό 'before, for' + the stem of φημί/φάναι 'to speak' — the athematic present of the same root, not its o-grade noun. AHD keeps them apart for exactly this reason: '2. Greek phanai, to speak: -PHASIA; PROPHET' versus '6. Suffixed o-grade form *bhā-nā in Greek phōnē … PHONE, -PHONE …'. So the node is right about the root and about 'phone', and one step too low for 'prophet'.\",\n          \"derivation_fa\": \"هر دو واژه به این ریشه بازمی‌گردند، ولی تنها یکی از آن‌ها به خانهٔ بالادستی. واژهٔ phone (در phoneme، phonetic، ‎-phone و تلفن، و نیز اصطلاح زبان‌شناسی «واج‌گونه/آوا») وام‌گیری مستقیم و عالمانهٔ یونانی φωνή است و جای آن درست است. اما prophet از φωνή نمی‌آید: از انگلیسی میانهٔ prophete، از فرانسوی کهن، از لاتینی prophēta، از یونانی προφήτης «آن که به‌جای خدا سخن می‌گوید، مفسّر» ساخته از πρό «پیش، به‌جای» و ستاک φημί/φάναι «گفتن» — یعنی از فعلِ همان ریشه، نه از اسمِ درجهٔ o. واتکینز نیز همین دو را جدا می‌آورد. پس ادعای نورایی دربارهٔ ریشه درست است ولی «prophet» یک پله بالاتر، زیر خودِ ریشه، جای می‌گیرد.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No reference given for this box (refs=None); checked against AHD and Klein instead.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"AHD_watkins1985.txt s.v. bha-2 §2 and §6; index entries 'PHONE! bha-2', 'PROPHET' under Greek phanai\",\n              \"stance\": \"partial\",\n              \"note\": \"'2. Greek phanai, to speak: -PHASIA; PROPHET' — PROPHET is filed under phanai, not under phōnē; '6. … Greek phōnē … PHONE, -PHONE, PHONEME, PHONETIC'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.vv. phone ('speech sound') and prophet\",\n              \"stance\": \"partial\",\n              \"note\": \"Klein derives prophet from Gk. προφήτης 'fr. πρό and the stem of φημί, \\\"I say\\\"', and phone from Gk. φωνή 'sound, voice' — two different Greek bases of the same root.\"\n            }\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Germanic\",\n          \"words\": \"banwan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Watkins reconstructs precisely this form: '3. Suffixed form in Germanic *banwan, *bannan, to speak publicly (used of particular kinds of proclamation in feudal or prefeudal custom; \\\"to proclaim under penalty, summon to the levy, declare outlaw\\\")'. The reduplicating strong verb OHG bannan, OE bannan 'to summon, proclaim' and ON banna 'to prohibit, curse' presuppose a stem *bann- < *bhə-n-w-, i.e. the same *bhā-n- present that yields Skt. bhánati 'speaks' and Arm. ban; Pokorny p.106 sets it out that way: 'auf *bhā-n-u̯- (oder auf germ. Umbildung nach spannan) ahd. bannan redupl. Verb \\\"unter Strafandrohung befehlen, verordnen, in Bann tun\\\", ags. bannan redupl. Verb \\\"vorladen, befehlen\\\", aisl. banna schw. Verb \\\"verbieten\\\", wovon ahd. ban, Pl. banna \\\"Gebot unter Strafandrohung\\\" (nhd. Bann)'. The semantic shift 'speak publicly' → 'proclaim under penalty' → 'ban, outlaw' is a Frankish legal development.\",\n          \"derivation_fa\": \"واتکینز دقیقاً همین صورت را بازسازی می‌کند: «۳. صورت پسوندی در ژرمنی *banwan، *bannan «آشکارا سخن گفتن»، در کاربردهای ویژهٔ اعلان‌های حقوقی در آیین فئودالی: اعلام کردن همراه با تهدید کیفر، فراخواندن به لشکر، بیرون راندن از پناه قانون». فعل قویِ مضاعف آلمانی باستان bannan و انگلیسی باستان bannan «فراخواندن، اعلام کردن» و نورس کهن banna «نهی کردن، نفرین کردن» همگی بر ستاک *bann- از *bhə-n-w- دلالت دارند؛ همان ستاکِ ن‌داری که سنسکریت bhánati «می‌گوید» و ارمنی ban را نیز پدید آورده است. پوکورنی در ص ۱۰۶ همین را می‌آورد. تحول معنایی «آشکارا گفتن» ← «اعلام کیفری» ← «تحریم، طرد» تحولی حقوقی در جامعهٔ فرانک‌هاست. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/abandon\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt s.v. bha-2 §3: 'Suffixed form in Germanic *banwan, *bannan, to speak publicly … a. Old English bannan, to summon, proclaim, and Old Norse banna, to prohibit, curse: BAN; b. Old French ban … and Old English gebann, proclamation: BANAL, BANNS; ABANDON; c. Old French banir, to banish: BANISH; d. Late Latin bannus, bannum, proclamation: CONTRABAND; e. Italian bandire … BANDIT.' The reconstructed form and the gloss are verbatim Nourai's.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"Pokorny p.106 (POK_01.txt leaf 115)\",\n              \"stance\": \"supports\",\n              \"note\": \"'auf *bhā-n-u̯- … ahd. bannan redupl. Verb \\\"unter Strafandrohung befehlen, verordnen, in Bann tun\\\", ags. bannan redupl. Verb \\\"vorladen, befehlen\\\", aisl. banna schw. Verb \\\"verbieten\\\"'.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, IEC.txt s.v. bhāniō 'declare, show' (WP II, 122)\",\n              \"stance\": \"supports\",\n              \"note\": \"'MHG (denom.) banen \\\"open up\\\" beside bannen \\\"declare\\\"; OE bannan \\\"summon, proclaim\\\"; OFris. bania \\\"indict\\\" beside banna \\\"order, proclaim\\\"; ON banna \\\"forbid, curse\\\".'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny Bd. II p.124 (leaf 129)\",\n              \"stance\": \"supports\",\n              \"note\": \"Same Germanic paragraph, with the explicit rejection of the rival derivation from *bhendh- 'binden': 'diese Gruppe nicht nach Loewe … als *bandn- zu binden, *bhendh-'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"English\",\n          \"words\": \"ban, abandon\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"ban continues OE bannan 'to summon, proclaim' directly (ME bannen, with the sense shifting through 'curse' — partly under Old Norse banna 'to curse' — to the modern 'prohibit'), and the noun ban 'formal prohibition' merges the native OE gebann with OF ban. abandon is the Romance side of the same Germanic word: OF abandoner, from the adverbial phrase à bandon 'at will, at (someone's) discretion', with bandon from Late/Medieval Latin bannum 'a proclamation', itself borrowed from Frankish *ban- (Proto-Germanic *bannan- 'proclaim, summon, outlaw'). Etymonline: 'mettre sa forêt à bandon' meant to throw one's forest open to common use, and since what is placed at another's absolute command is thereby given up by its owner, the sense moved from 'hand over control of' to 'forsake'. English took the verb in the 14th century.\",\n          \"derivation_fa\": \"واژهٔ ban دنبالهٔ مستقیم انگلیسی باستان bannan «فراخواندن، اعلام کردن» است که در انگلیسی میانه (bannen) و زیر تأثیر نورس کهن banna «نفرین کردن» به معنی «نفرین کردن» و سپس «منع کردن» رسیده است؛ اسم ban «منع رسمی» آمیزه‌ای از gebann انگلیسی باستان و ban فرانسوی کهن است. اما abandon شاخهٔ رومانسِ همان واژهٔ ژرمنی است: فرانسوی کهن abandoner از عبارت قیدی à bandon «به اختیار، به فرمانِ (کسی)»، و bandon از لاتینی میانهٔ bannum «اعلان» که خود وام‌واژه‌ای از فرانکی *ban- (ژرمنی آغازین *bannan- «اعلام کردن، فراخواندن، طرد کردن») است. چنان‌که Etymonline توضیح می‌دهد، «جنگل خود را à bandon نهادن» یعنی آن را برای همگان آزاد گذاشتن، و چون آنچه به فرمان دیگری سپرده شود از دست صاحبش بیرون می‌رود، معنا از «به اختیار کسی نهادن» به «رها کردن» رسیده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/abandon\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No reference given for this box (refs=None); the parent Germanic box's AHD citation covers both words ('BAN', 'ABANDON' are both listed there).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"AHD_watkins1985.txt s.v. bha-2 §3a-b and the English index ('BAN! bha-2', 'ABANDON bha-2')\",\n              \"stance\": \"supports\",\n              \"note\": \"'a. Old English bannan, to summon, proclaim, and Old Norse banna, to prohibit, curse: BAN; b. Old French ban, feudal jurisdiction, summons to military service, proclamation, Old French bandon, power … BANAL, BANNS; ABANDON.'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein s.vv. ban, abandon\",\n              \"stance\": \"supports\",\n              \"note\": \"Klein derives abandon from OF abandoner, 'fr. the phrase (mettre) a bandon, \\\"(to put) at one's disposal\\\"', bandon fr. Late L. bannum, of Teutonic origin, and ban from OE bannan.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Bhad\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *bhād- / *bhǝd- 'good' (Pokorny 106)\",\n      \"note\": \"Pokorny's article on p.106 reads 'bhād- \\\"gut\\\". Ai. bhadrá-ḥ \\\"erfreulich, glücklich, gut\\\", n. \\\"Glück, Heil\\\", su-bhadra-ḥ \\\"herrlich\\\" = av. hu-badra- \\\"glücklich\\\"; got. batiza \\\"besser\\\", batista \\\"bester\\\", aisl. betre, betstr, ags. bet(e)ra, betst, ahd. bezzir(o), bezzist, nhd. besser, best … got. gabatnan \\\"Nutzen erlangen\\\", aisl. batna \\\"besser werden\\\" … got. bōta f. \\\"Nutzen\\\", aisl./ags. bōt \\\"Besserung, Ersatz\\\", ahd. buoz(a). WP. II 151 f.' Nourai's root name, language label, gloss and page are all correct, and Watkins agrees: 'bhad-. Good. 1. Germanic (comparative) *batizō … BETTER. 2. Germanic (superlative) *batistaz … BEST … [Pok. bhǝd- 106.]' One caveat worth recording: the root is a fairly thin one. Walde-Pokorny II 151 (1927) did not yet set it up as a separate root — there bhadrá-/hubadra- is discussed under *bhend- 'etwa singen, schön klingen, jauchzen' ('Vielleicht trotz der etwas andern Bed. mit Schwundstufe hieher auch ai. bhadrá-ḥ … = av. hubadra- \\\"glücklich\\\"'), with the *bhād- 'gut' analysis attributed to Fick as the alternative; and Mann sets up 'bhodh- (2) \\\"good\\\"' instead, remarking that 'Go. batiza beside MHG radical baz \\\"better\\\" implies a radical *bhod-'. The Germanic-Indo-Iranian equation itself is standard (Klein, Buck, Feist all give it), only the exact root shape is unsettled.\",\n      \"note_fa\": \"پوکورنی در صفحهٔ ۱۰۶ می‌نویسد: «bhād- «خوب». سنسکریت bhadrá- «خوشایند، خوشبخت، خوب» و اسم خنثی «بخت، نیکی»، su-bhadra- «باشکوه» = اوستایی hu-baδra- «خوشبخت»؛ گوتی batiza «بهتر»، batista «بهترین»، انگلیسی باستان bet(e)ra، betst، آلمانی besser، best». نام ریشه، برچسب زبانی، معنا و شمارهٔ صفحه‌ای که نورایی آورده هر چهار درست است و واتکینز نیز همین را می‌گوید. تنها نکتهٔ لازم آنکه این ریشه پایه‌ای چندان استوار ندارد: والده-پوکورنی در ۱۹۲۷ هنوز آن را ریشه‌ای مستقل نمی‌دانست و bhadrá-/hubadra- را زیر ریشهٔ *bhend- «خوش‌آوا خواندن، شادی‌کنان بانگ زدن» می‌آورد و صورت *bhād- «خوب» را تنها به‌عنوان نظر فیک نقل می‌کرد، و مان نیز به‌جای آن *bhodh- (۲) «خوب» را می‌نهد. با این حال، برابری خودِ واژه‌های ژرمنی و هندوایرانی نزد کلاین و باک و فایست پذیرفته است و تنها شکل دقیق ریشه اختلافی است.\",\n      \"sources\": [],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:106\",\n          \"status\": \"supports\",\n          \"note\": \"POK_01.txt, form-feed leaf 115 (between the page markers 106 and 107): 'bhād- \\\"gut\\\". Ai. bhadrá-ḥ \\\"erfreulich, glücklich, gut\\\", n. \\\"Glück, Heil\\\", su-bhadra-ḥ \\\"herrlich\\\" = av. hu-badra- \\\"glücklich\\\"; got. batiza \\\"besser\\\", batista \\\"bester\\\" … WP. II 151 f., Feist 83, 103, 174.' Root, gloss and page are exactly Nourai's.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"AHD\",\n          \"where\": \"AHD_watkins1985.txt s.v. bhad-\",\n          \"stance\": \"supports\",\n          \"note\": \"'bhad-. Good. 1. Germanic (comparative) *batizō in Old English betera, better: BETTER. 2. Germanic (superlative) *batistaz in Old English bet(e)st, best: BEST. 3. Germanic noun *bōtō in Old English bōt, remedy, aid: BOOT. 4. Germanic verb *batnan, to become better, in Old Norse batna, to improve: BATTEN. [Pok. bhǝd- 106.]'\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Walde-Pokorny Bd. II p.151 (WLD_Bd2_pages.txt leaf 156)\",\n          \"stance\": \"partial\",\n          \"note\": \"'Vielleicht trotz der etwas andern Bed. mit Schwundstufe hieher auch ai. bhadrá-ḥ \\\"erfreulich, glücklich, günstig, gut\\\", n. \\\"Glück, Heil\\\", su-bhadra-ḥ \\\"herrlich\\\" = av. hubadra- \\\"glücklich\\\" (… Feist Got. Wb. u. batiza). Andrerseits wird bhadrá- (z.B. von Fick …) unter einer Wz. *bhād- \\\"gut\\\" verglichen mit …' — the 1927 edition places the material under *bhend- and treats *bhād- as only one of two options.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, IEC.txt s.v. bhodh- (2) 'good'\",\n          \"stance\": \"partial\",\n          \"note\": \"'bhodh- (2) \\\"good\\\" W bodd \\\"goodwill, consent\\\"; MHG bat \\\"help, use\\\". (Extn. in Go. batiza beside MHG radical baz \\\"better\\\" implies a radical *bhod-)' — same word-family, different root shape.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck 16.71 'good', SYN.txt line 29653\",\n          \"stance\": \"supports\",\n          \"note\": \"'Skt. bhadra-, also \\\"blessed, auspicious, fair\\\", prob. : Goth. batiza \\\"better\\\", batists \\\"best\\\". Walde-P. 2.151 f. Falk-Torp 67.' Buck accepts the Indo-Iranian ↔ Germanic equation on which Nourai's whole chart rests.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"badra : good fortune, luck; hu-badra : (with) good luck, lucky\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The compound is genuine, the simplex is not. hu-baδra- is attested Younger Avestan: Bartholomae col. 1829 has 'j. hu-baδra- Adj. \\\"glücklich\\\"' (Aogəmadaēčā 51), equated there with 'ai. su-bhadra- Adj. \\\"herrlich\\\"'; Pokorny p.106, Walde-Pokorny II 151 and Klein p.167 all print it as hubadra- (with plain d, the typographic convention Nourai follows), and the first element hu- 'good, well' is the Avestan reflex of PIE *h₁su- — Nourai's own ☞Su 1 pointer. But an Avestan simplex *baδra- meaning 'good fortune, luck' does not exist: Bartholomae's only baδra- entry (col. ~964) is 'baδra- m. (vll.) \\\"Krankheit\\\"' — 'perhaps \\\"illness\\\"', a hapax of the Frahang (F.16), semantically the opposite. The gloss Nourai gives, 'good fortune, luck', is that of the Sanskrit word — Pokorny: 'ai. bhadrá-ḥ \\\"erfreulich, glücklich, gut\\\", n. \\\"Glück, Heil\\\"'. So this line is a Sanskrit form and gloss under an Avestan label, presumably back-formed from the attested compound; only the compound belongs in an Avestan box.\",\n          \"derivation_fa\": \"واژهٔ مرکب اصیل است، ولی صورت ساده نه. hu-baδra- در اوستای متأخر گواهی شده است: بارتولومه در ستون ۱۸۲۹ می‌آورد «hu-baδra- صفت «خوشبخت»» و آن را برابر سنسکریت su-bhadra- «باشکوه» می‌گذارد؛ پوکورنی (ص ۱۰۶)، والده-پوکورنی (ج ۲ ص ۱۵۱) و کلاین (ص ۱۶۷) همگی آن را با «د» ساده می‌نویسند، همان شیوه‌ای که نورایی نیز به کار برده است، و جزء نخست آن hu- «خوب، نیک» بازتاب اوستایی *h₁su- هندواروپایی است (که خودِ نورایی با نشانهٔ «Su 1» به آن ارجاع داده). اما صورت سادهٔ اوستایی *baδra- به معنی «بخت و اقبال» وجود ندارد: تنها مدخل baδra- در بارتولومه «baδra- مذکر (شاید) «بیماری»» است، هاپاکسی از فرهنگ پهلوی-اوستایی «فرهنگ اویم»، یعنی درست معنای وارونه. معنایی که نورایی آورده («بخت، اقبال») از آنِ واژهٔ سنسکریت bhadrá- است. پس این سطر صورت و معنای سنسکریت را زیر برچسب «اوستایی» نشانده است؛ خطای خودِ کتاب است نه خطای خوانش اسکن، و تنها واژهٔ مرکب در این خانه جای درست دارد.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:106\",\n              \"status\": \"partial\",\n              \"note\": \"POK_01.txt leaf 115: 'ai. bhadrá-ḥ \\\"erfreulich, glücklich, gut\\\", n. \\\"Glück, Heil\\\", su-bhadra-ḥ \\\"herrlich\\\" = av. hu-badra- \\\"glücklich\\\"'. Pokorny supports hu-badra- and its gloss, but gives the simplex only for Sanskrit, never for Avestan.\"\n            },\n            {\n              \"ref\": \"KLN:167\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt leaf carrying the printed page marker 167, s.v. best: 'best, adj. — ME., fr. OE. best, dissimilated fr. betst, rel. to ON. beztr, Du. best, OHG. bezzisto, MHG., G. best, Goth. batists, \\\"best\\\", OE. batian, \\\"to become better\\\", bōt, \\\"remedy, cure, improvement, compensation\\\", and possibly cognate with OI. bhadraḥ, \\\"favorable, good\\\", Avestic hubadra-, \\\"lucky\\\".' Klein's page, form and gloss ('lucky') are exactly Nourai's — including the spelling hubadra- and the caution 'possibly cognate'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, Altiranisches Wörterbuch col. 1829 (hu-baδra-) and the baδra- entry (BRT.txt lines 30328 and 17241)\",\n              \"stance\": \"partial\",\n              \"note\": \"'j. hu-baδra- Adj. \\\"glücklich\\\" … ai. su-bhadra- Adj. \\\"herrlich\\\"' confirms the compound (and shows that the correct Avestan spelling has δ, not d); but the only simplex entry is 'baδra- m. (vll.) \\\"Krankheit\\\": F.16', i.e. no Avestan word baδra- 'good fortune' exists.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 16.71 'good' (SYN.txt line 29653)\",\n              \"stance\": \"partial\",\n              \"note\": \"'Skt. bhadra-, also \\\"blessed, auspicious, fair\\\", prob. : Goth. batiza \\\"better\\\"' — Buck cites the word as Sanskrit only, not Avestan.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny Bd. II p.151 (leaf 156)\",\n              \"stance\": \"partial\",\n              \"note\": \"'ai. bhadrá-ḥ … = av. hubadra- \\\"glücklich\\\"' — again the compound only, and hedged ('Vielleicht … mit Schwundstufe hieher').\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": null,\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"There is nothing to verify: the printed page really does show an empty box here. On the rendered page (pdftoppm -r 200 of pdf p.80, saved as data/verification/sources/refs/ocr/BOOK/80.png) the box to the right of the Avestan box in the Bhad chart is drawn with its frame and its internal divider but carries no language label, no reference and no word — the box was left blank in the book (the layout of every other chart puts a descendant language there). The extraction is therefore faithful; this is a defect of the printed page, not of the JSON, and the owner needs no data fix beyond, at most, dropping the empty node.\",\n          \"derivation_fa\": \"چیزی برای بررسی نیست: صفحهٔ چاپی در همین جا واقعاً یک کادر خالی دارد. در تصویر بازنمودهٔ صفحهٔ ۸۰ (که در data/verification/sources/refs/ocr/BOOK/80.png نگه داشته شده) کادرِ سمت راستِ کادر اوستایی در نمودار «Bhad» با چارچوب و خط جداکنندهٔ درونی رسم شده اما نه نام زبانی دارد، نه مأخذی و نه واژه‌ای؛ یعنی در خودِ کتاب خالی مانده است. پس خوانش اسکن درست و وفادار است و این نقصِ صفحهٔ چاپی است، نه خطای استخراج داده.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The box carries no reference in the book, because it carries nothing at all.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BOOK\",\n              \"where\": \"printed page 50 (pdf p.80), rendered at 200 dpi and stored as data/verification/sources/refs/ocr/BOOK/80.png\",\n              \"stance\": \"silent\",\n              \"note\": \"The box in the Bhad chart to the right of 'Avestan | POK:106; KLN:167' is empty on the printed page — frame and divider only, no text. Extraction is faithful.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Germanic\",\n          \"words\": \"batiso\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Nourai's 'batiso' is the Proto-Germanic comparative *batizô 'better' (Watkins's spelling), the -iz- being the inherited comparative suffix PIE *-yos-/-is- with Verner-voiced *s > z, added to a zero-grade *bhǝd- > Gmc. *bat-. It is directly attested in Gothic batiza 'better' (Wulfila), beside the superlative batists 'best', and continues in ON betri, OE bet(e)ra, OHG be33iro. The gloss 'good' is a shade loose — the form is a comparative, 'better' — but the family it heads (Gothic bōta 'profit', OE bōt 'remedy', ON batna 'to improve') does supply the positive sense. Pokorny p.106 and Klein p.167 both give the full paradigm.\",\n          \"derivation_fa\": \"صورتی که نورایی «batiso» نوشته، همان *batizô ژرمنی آغازین «بهتر» است (املای واتکینز): جزء ‎-iz- پسوند تفضیلیِ به‌ارث‌رسیدهٔ هندواروپایی *-yos-/-is- است که بر پایهٔ درجهٔ صفرِ *bhǝd- > ژرمنی *bat- افزوده شده، و «س» آن بر پایهٔ قانون ورنر به «ز» بدل شده است. این صورت مستقیماً در گوتی batiza «بهتر» (ترجمهٔ اولفیلا) گواهی شده است، در کنار برترین batists، و در نورس کهن betri، انگلیسی باستان bet(e)ra و آلمانی علیای باستان bezziro ادامه یافته است. تنها نکته آنکه معنای «خوب» اندکی نادقیق است، زیرا این صورت تفضیلی و به معنی «بهتر» است. پوکورنی (ص ۱۰۶) و کلاین (ص ۱۶۷) هر دو همین را می‌آورند؛ ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt s.v. bhad-: '1. Germanic (comparative) *batizō in Old English betera, better: BETTER. 2. Germanic (superlative) *batistaz in Old English bet(e)st, best: BEST.' Nourai's 'batiso' is Watkins's *batizō.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"Pokorny p.106 (POK_01.txt leaf 115)\",\n              \"stance\": \"supports\",\n              \"note\": \"'got. batiza \\\"besser\\\", batista \\\"bester\\\", aisl. betre, betstr, ags. bet(e)ra, betst, ahd. bezzir(o), bezzist, nhd. besser, best; dazu das Adv. des Kompar. aisl. betr, ags. bet (*batiz), ahd. baz (*bataz, erstarrtes Neutr. \\\"Nutzen\\\")'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt printed p.167 s.v. best, and the following column s.v. better\",\n              \"stance\": \"supports\",\n              \"note\": \"'better, adj. — ME. bettere, bettre (adj.), bet (adv.), fr. OE. betera (adj.), bet (adv.), rel. to ON. betri …, OHG. be33iro …, Goth. batiza (adj.)'.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 16.71 (SYN.txt lines 7883, 20593, 29653)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Goth. batiza batists \\\"better, best\\\", etc.' — cited as the standard Germanic comparative/superlative pair of this root.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"better, best\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The English pair is the direct native continuation of the Germanic suppletive comparative and superlative. better < ME bettere < OE betera < Gmc *batizô (the parent box); best < ME best < OE best, dissimilated from earlier betst < Gmc *batistaz, exactly as Klein describes ('best, adj. — ME., fr. OE. best, dissimilated fr. betst … For the dissimilation of OE. betst into best cp. last, adj.'). Both have been suppletive to good since Old English, good itself belonging to a wholly different root (*ghedh- 'to unite, be fitting'). Watkins files BETTER and BEST under bhad-.\",\n          \"derivation_fa\": \"این جفت انگلیسی دنبالهٔ مستقیم و بومی صورت‌های تفضیلی و عالیِ ژرمنی است: better از انگلیسی میانهٔ bettere و انگلیسی باستان betera از *batizô ژرمنی (همان خانهٔ بالادستی)، و best از انگلیسی باستان best که با ناهمگونی (dissimilation) از betst کهن‌تر پدید آمده است، درست چنان‌که کلاین توضیح می‌دهد و آن را با last می‌سنجد. هر دو از دورهٔ انگلیسی باستان صورت‌های مکمّل (suppletive) واژهٔ good شمرده می‌شوند، حال آنکه خودِ good به ریشه‌ای یکسره دیگر (*ghedh- «پیوستن، سازگار بودن») بازمی‌گردد. واتکینز نیز BETTER و BEST را زیر ریشهٔ bhad- می‌آورد؛ ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No reference given for this box (refs=None); covered by the parent box's AHD citation, whose index reads 'BETTER bhad-' and 'BEST bhad-'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt printed p.167 s.vv. best, better\",\n              \"stance\": \"supports\",\n              \"note\": \"'best, adj. — ME., fr. OE. best, dissimilated fr. betst, rel. to ON. beztr … Goth. batists, \\\"best\\\"'; 'better, adj. — … fr. OE. betera … Goth. batiza (adj.)'.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"AHD_watkins1985.txt s.v. bhad- and the English index\",\n              \"stance\": \"supports\",\n              \"note\": \"'BETTER bhad-', 'BEST bhad-'; §1 and §2 give the Old English forms betera and bet(e)st.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-05T06:21:18.366Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-80.json (file state is current in your context — no need to Read it back)
```


## [2026-09-05T06:21:21.995Z] TOOL CALL #66: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-80.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 80"
}
```


### [2026-09-05T06:21:26.541Z] TOOL RESULT

```
JSON OK
nodes verified: 17/17
node verdicts: {'disputed': 2, 'plausible': 4, 'confirmed': 10, 'unverified': 1}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'supports': 9, 'partial': 3, 'not_checked': 8}
books consulted: {'partial': 11, 'contradicts': 2, 'silent': 2, 'supports': 24} | by book: {'KLN': 8, 'AHD': 6, 'POK': 4, 'BRT': 3, 'CHEUNG': 3, 'WLD': 3, 'NYB': 2, 'SYN': 2, 'KNT': 1, 'PHD': 1, 'HRN': 1, 'HUB': 1, 'MON': 1, 'SKT': 1, 'IEC': 1, 'BOOK': 1}
```


## [2026-09-05T06:21:46.217Z] AGENT

Page 80 (book p.50) verified — `data/verification/page-80.json`, `verify_check.py 80` shows 0 PROBLEM lines.

**Counts:** 17/17 nodes — confirmed 10, plausible 4, disputed 2, unverified 1. Roots: Bhâ 2 = plausible, Bhad = confirmed. Ref checks: 9 supports, 3 partial, 8 not_checked. 16 books/sources consulted (KLN, AHD, POK, WLD, BRT, CHEUNG, NYB, PHD, HRN, HUB, SYN, IEC, SOD, KNT, MON, BQT).

**Disputed / flagged**
- **Bhâ 2, root + node #1 (Av./OP `bišazka; baešaza`)** — Nourai's "heal" branch rests on a bare citation of Kuiper inside Pokorny 105/106. Cheung 2007 s.v. `*bisaz`: "This root has no IE etymology and may reflect an ancient cultural borrowing" (Lubotsky); Buck 4.86 writes "Av. bišaz-, etym.?"; Wiktionary's `*bʰeh₂-` lists no Iranian healing word. Also `bišazka` is a reconstruction (Nyberg p.48 writes `*bišaz-ka-`), not attested Avestan and absent from Kent's Old Persian lexicon; and Bartholomae glosses `baēšaza-` "healing / remedy, medicine", not "doctor".
- **Bhad, node #1 (`badra`)** — Avestan `hu-baδra-` is genuine (BRT col. 1829; POK 106; KLN 167 s.v. *best*, which is exactly Nourai's citation), but a simplex Avestan `baδra-` "good fortune" does not exist: Bartholomae's only `baδra-` entry is "m. (vll.) 'Krankheit'". The form and gloss Nourai gives are Sanskrit `bhadrá-` under an Avestan label. Book error, not extraction error.

**Downgraded to plausible (not errors):** Pahlavi `bešazak` (real, from Horn no. 183, but MacKenzie/Nyberg/Cheung give `bizešk` as the MP noun); Persian `pezešk` (route omits the NW/Parthian metathesis `*bišazka- > bizaška- > bizešk`); Greek `sun-phônĕ` (no such lemma; Greek has `σύμφωνος`/`συμφωνία`); English `prophet` (from `phánai`, not from `phōnē`).

**Extraction errors: none.** The JSON matches the printed page throughout (page image saved to `data/verification/sources/refs/ocr/BOOK/80.png`). The empty node #2 of entry 1 is faithful — the book itself prints a blank box there; the owner may simply want to drop it from the data.

**Ref numbers checked and exact:** POK:105, POK:106, KLN:167, KLN:1557, SOD:117, BQT:399, NYB:48. Not checkable: AEF:237 (no digital copy — verified against Horn no. 183, the German original it translates), AHD:1304 (main A–Z text of the 1975 New College ed.), MON:1132/1921 (local Moʿin OCR is a different printing; the three entries themselves were found and support the node). Four web pages archived via `fetch_source.py`.
