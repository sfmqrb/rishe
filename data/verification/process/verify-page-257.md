# Verification process log — verify-page-257


## [2026-09-06T16:14:31.284Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 257 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-257.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-257.json. Write /home/sfmqrb/git/rishe/data/verification/page-257.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 257` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T16:14:32.805Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T16:14:33.497Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T16:14:33.512Z] TOOL RESULT

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


## [2026-09-06T16:14:33.699Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-257.txt"
}
```


### [2026-09-06T16:14:33.739Z] TOOL RESULT

```
1	=== PDF page 257 (book page 227) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ker 3, Qer, Qor, Qr : loud noise, noisy birds  (refs POK:567)
4	#1 (parent #0) [Avestan] refs=POK:571; KLN:1305 | xraos : loud noise
5	  #2 (parent #1) [Pahlavi] refs=BQT:741 | xrusîten : yell, roar ; xros : rooster
6	    #3 (parent #2) [Persian] refs=IRT:44 | xorŭšîdan «خروشیدن» : to roar, scream ; xorŭs «خروس ( خروج )» : rooster
7	#4 (parent #0) [Avestan] refs=POK:568 | kahrkatât : some noisy birds ; kahrkâ-asa : eating bird (vulture) ☞Ed
8	  #5 (parent #4) [Persian] refs=BQT:1624,2268; MON:5001 | karkas «کرکس» : vulture ; kark, karak «کَرک ( ورتک ، وردیج )» : poultry
9	  #6 (parent #4) [Sogdian] refs=SOD:128 | crks : vulture
10	#7 (parent #0) [Persian] refs=POK:569 | sorfeh «سرفه» : cough
11	#8 (parent #0) [Sanskrit] refs=POK | krosa : a loud sound, also the distance reached by such a loud voice
12	  #9 (parent #8) [Persian] refs=BQT:1630; MON:2960 | korŭh «کروه ۱» : a unit of distance (about two miles)
13	#10 (parent #0) [Germanic] refs=AHD | hr : a ringing sound ; skrainjan, skrěki : scream ; krik : to creak
14	  #11 (parent #10) [English] refs=None | ringing, rook, raven ; scream, screech ; cricket
15	
```


## [2026-09-06T16:14:36.680Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-257.json",
 "description": "Read source JSON for page 257"
}
```


### [2026-09-06T16:14:36.713Z] TOOL RESULT

```
{
  "pdf_page": 257,
  "book_page": 227,
  "entries": [
    {
      "root": {
        "name": "Ker 3, Qer, Qor, Qr",
        "lang": "Indo-European",
        "refs": "POK:567",
        "gloss": "loud noise, noisy birds"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:571; KLN:1305",
          "words": [
            {"translit": "xraos", "gloss": "loud noise", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:741",
          "words": [
            {"translit": "xrusîten", "gloss": "yell, roar", "script": null},
            {"translit": "xros", "gloss": "rooster", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "IRT:44",
          "words": [
            {"translit": "xorŭšîdan", "gloss": "to roar, scream", "script": "خروشیدن"},
            {"translit": "xorŭs", "gloss": "rooster", "script": "خروس ( خروج )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "سگالیده در جنگ مانند قوچ - تبر برده بر سر چو تاج خروج",
            "poet": "Rŭdakî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:568",
          "words": [
            {"translit": "kahrkatât", "gloss": "some noisy birds", "script": null},
            {"translit": "kahrkâ-asa", "gloss": "eating bird (vulture)", "script": null, "see": ["Ed"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:1624,2268; MON:5001",
          "words": [
            {"translit": "karkas", "gloss": "vulture", "script": "کرکس"},
            {"translit": "kark, karak", "gloss": "poultry", "script": "کَرک ( ورتک ، وردیج )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "تانباشد همچو عنقا خاصه در عزلت غراب - تانباشد همچو شاهین خاصه درقدرت کرک",
            "poet": "Anvarî"
          }
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "Sogdian",
          "refs": "SOD:128",
          "words": [
            {"translit": "crks", "gloss": "vulture", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Persian",
          "refs": "POK:569",
          "words": [
            {"translit": "sorfeh", "gloss": "cough", "script": "سرفه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK",
          "words": [
            {"translit": "krosa", "gloss": "a loud sound, also the distance reached by such a loud voice", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "BQT:1630; MON:2960",
          "words": [
            {"translit": "korŭh", "gloss": "a unit of distance (about two miles)", "script": "کروه ۱"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "داد نقیب صبا عرض سپاه بهار - کز دو کروهی بدید یاوگیان خزان",
            "poet": "Khâqânî"
          }
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "hr", "gloss": "a ringing sound", "script": null},
            {"translit": "skrainjan, skrěki", "gloss": "scream", "script": null},
            {"translit": "krik", "gloss": "to creak", "script": null}
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
            {"translit": "ringing, rook, raven", "gloss": null, "script": null},
            {"translit": "scream, screech", "gloss": null, "script": null},
            {"translit": "cricket", "gloss": null, "script": null}
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


## [2026-09-06T16:14:37.206Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T16:14:37.242Z] TOOL RESULT

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


## [2026-09-06T16:15:04.784Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','BQT','IRT','MON','SOD','AHD','BRT','PHD','HRN','HUB','CHEUNG','NYB','ARY','IEC','SYN','WLD','SKT','HJB','AID']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\""
}
```


## [2026-09-06T16:15:05.446Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && python3 -c \"\nimport json\nd=json.load(open('data/verification/page-202.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\n\""
}
```


### [2026-09-06T16:15:06.304Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

IRT {"title": "M.A. Sajjadiyyeh, Tabar-e Moshtarek-e Iranian va Turanian, Bonyad-e Neyshabur 1368/1989", "kind": "purchase", "url": "gisoom/iketab (full title «پژوهشی در تبار مشترک ایرانیان و تورانیان», Balkh 1368)", "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only."}

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

CHEUNG null

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4

AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lo
```


### [2026-09-06T16:15:08.387Z] TOOL RESULT

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
 "entry": 0,
 "root": "Gwa, Gwâ, Gwen 2",
 "verdict": "confirmed",
 "modern_form": "PIE *gʷem- 'to go, to come' (with the collateral root *gʷeh₂- / *gʷā- 'to step, go'); Pokorny IEW 463-465",
 "note": "Pokorny's entry, which begins on p.463 exactly as Nourai cites, is headed 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“', and it is deliberately a double entry (I. gʷā-, II. gʷem-), which is why Nourai's box carries two names, 'Gwa, Gwâ'. His third name 'Gwen 2' reflects the *gʷem- > *gʷen- variant Pokorny himself notes ('Unthematisch *(e)-gʷem-t (> *e-gʷen-t)', and Latin advenam / veniō with -n- for -m-); it is not a separate root in any modern handbook, so it is Nourai's own labelling convenience rather than an error of substance. Watkins/AHD 1985 heads the same material 'gʷā-. Also gʷem-. To go, come'; Cheung splits it into *gaH¹ (PIE *gʷeh₂-, Pok. 463 f.) and *gam¹ (PIE *gʷem-, Pok. 464 f.). The gloss 'to walk, to step, to come, to go' is an accurate rendering. Two words in the chart do not belong to this root: Avestan 'gâv' in node 6 (a misprint) and 'thamân' in node 12 (an unidentifiable form), and one Persian word, nîyâm (node 3), is derived by modern scholarship from a different root (*ni-dā-, not *ni-gam-). Everything else on the page is standard, well-attested Iranian etymology.",
 "note_fa": "جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۶۳ فرهنگ خود مدخل «gʷā-, gʷem-» را با معنای «رفتن، آمدن؛ به جهان آمدن، زاده شدن» آورده و همان‌جا نام‌های gʷm̥-ti-s و gʷem-tu-s «گام، رفتار» را می‌افزاید؛ پس هر دو صورت «Gwa/Gwâ» و «Gwem» از یک مدخل‌اند و برچسب «هندواروپایی» و معنای «راه رفتن، گام برداشتن، آمدن، رفتن» درست است. نام سوم «Gwen 2» گونهٔ *gʷen- است که خود پوکورنی (در *e-gʷen-t و در veniō لاتین) یاد کرده و در کتاب‌های امروزی ریشهٔ جداگانه‌ای به شمار نمی‌رود؛ این نام‌گذاری از خود نورایی است نه خطای علمی. واتکینز (پیوست AHD) نیز همین ماده را «gʷā-, also gʷem-: رفتن، آمدن» آورده و چونگ آن را به دو ریشهٔ *gaH¹ و *gam¹ بخش کرده است. در سراسر این صفحه تنها سه لغزش هست: صورت «gâv» در گرهٔ ۶ (غلط چاپی)، صورت «thamân» در گرهٔ ۱۲ (صورتی که در هیچ فرهنگی یافت نشد) و واژهٔ «نیام» در گرهٔ ۳ که پژوهش امروزی آن را از ریشهٔ دیگری (*ni-dā-) می‌داند.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷem-"
 ],
 "ref_check": [
  {
   "ref": "POK:463",
   "status": "supports",
   "note": "POK_02.txt line 1790 (the leaf whose running numbers are 463-465): 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“, Verbaladjektiv gʷm̥-to-s. I. gʷā-: ... 2. gʷem-: ...'. The same pages carry 'av. gātu-s „Ort, Liegerstatt, Sessel, Thron“, apers. gāθu- ds.', 'av. gā-man- n. „Schritt“', 'av. jantu (*gʷem-tu-)' and 'av. jasaiti „er geht“' — i.e. Pokorny 463 alone underwrites the root box and nodes 1, 2 and 6."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I 675-677 (WLD_Bd1 djvu line 42665 ff., running head 'gʷem-, gʷā-'
```


## [2026-09-06T16:15:13.812Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kahrkāsa\\|kahrkatāt\\|kahrkatat\\|kahrkasa\" POK_full.txt POK_0*.txt | head -20"
}
```


### [2026-09-06T16:15:13.865Z] TOOL RESULT

```
POK_full.txt:46020:"rooster, cock', krkasa, krka//ka^b\rd name'; Avestan kahrkatat-t "rooster, cock', npers. 
POK_full.txt:46021:kark^ chicken ', Avestan kahrkasa-rc\. " vulture, actually Hahneesser'; Old Indie karkati
```


## [2026-09-06T16:15:14.463Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==576||NR==577' POK_01.txt | head -80"
}
```


### [2026-09-06T16:15:16.163Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:15:18.691Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '45960,46080p' POK_full.txt"
}
```


### [2026-09-06T16:15:18.735Z] TOOL RESULT

```
alb. -k > -th). 

Latin cracentes, leg. gracentes^ thin, slight, slender, slim, meagre, lean ' to gracilis^ 
skinny, slim, arid', dissim. from *cracilis. 

Old Icelandic horr{*hurha-) " thinness, leanness '; 

Lithuanian karseti, intensiv karstu, karstT become old ', iskarsqs^ frail before age ', 
karse^ senility ', Latvian nuo-karsV become old, mature, ripe, mellow, become seasoned 



kir. kors^ cleared line of land ', Serbo-Croatian krsljav' be slow in growth ', sloven, k'rs 
m. 'shrub, bush', Czech krs^ dwarf tree ', krs-ati, -nouti^ abate ', poln. dial, karslak^ low, 
crooked tree, firewood'. 

References: WP. I 420 f., WH. I 284, Berneker 670. 
Page(s): 581 

Root/ lemma: ker-1, kor-, kr- 

Meaning: a kind of sound (hoarse shrieking, etc.), *crane 

Note: 



Root / lemma: ker-1, kor-, kr-\ "a kind of sound (hoarse shrieking, etc.), *crane' derived 
from Root/ lemma: ger-2\ "to shriek (in expr. forms), *crane'. 
Note: aniaut mostly k-, rare R- also with moveable s- : (s)ker-. 
Material: I. Old Indie karata-xx\. "crow' (?), karayika^a kind of crane '. 

Gr. Kopa^, -QKoq m. "raven', KopoKiov "bill, beak, neb of raven ' {*kor-n-k-, compare Latin 
cor-n-T)^, OKOpaKi^w "dismiss contemptuously (from ic, KopaKac, paAAsiv ), Kopcbvp "crow', 
Kopacpoc; TTOioc; opvi^ Hes. {* kor-n-b^os); KopKopuyn "rumbling noise, tumult'; 

Latin ccAi/i/s "raven', cornTx, -/ic/s^crow', Umbrian curnaco' a crow ' {-/k- besides -ak-); 
Specht, Indo Germanic Dekl. 118, 161 places whereas corvus and corn/xto color root ker-; 

Alb. korb : French corbeau ; corbin : Bresciano corf : Catalan corb : Finnish korppi : 
Romanian corb : Sardinian Campidanesu crobu : Swedish korp : Valencian corp "raven' 
[common alb. -v- > -d-]. 

Czech krakoratr gaggle, cackle, chitchat, talk, snicker ' [*kor-kor-, compare 
KopKOpuyn), Serb, krakoriti^ cackle ', kir. kerekorfty^ gobble, coo '. 

see also Aar-"loud praise '. 

1. Dental extensions: 

Old Danish sAraofe "rattle, clash, groan ', Swedish Dialectal sAra/a "sound', Norwegian 
Dialectal skrata' gaggle, cackle, chitchat, talk, snicker, scold, chide, loud lachen', skratia 
"rattle, clash', Swedish sAra/Za "lachen', Danish skratte^e\v\ev\ gesprungenen Ton give'. 

2. guttural extensions: 

A. Auf -Ar- (broken reduplication): kerk-, krek-, krok-: 

Old Indie krkara-, krakara-, krkana-rr\. "a kind of partridge, game bird ', krka-vaku-m. 
"rooster, cock', krkasa, krka//ka^b\rd name'; Avestan kahrkatat-t "rooster, cock', npers. 
kark^ chicken ', Avestan kahrkasa-rc\. " vulture, actually Hahneesser'; Old Indie karkati 
(uncovered) "laehf, kraksamana-, -kraksa-, -Ara/rs//?- perhaps "knarrend'; common Old 
\v\d\c gh- > ks- 

Armenian perhaps as neologism /r5/'/r5c"Rausehen, noise', karkacem ' excess'we 
lachen, roar'; 



gr. KspKa^ ispa^ Hes., K£pKa(; Kps^ to opvsov Hes., K£pKi9aAi(; tpLob\6q Hes., KspKiq 
...£l5o(; 6pvT9o(; Hes., K£pKV0(; ispa^, n aAsKipucbv Hes., KspKOc; ... aAsKipucbv Hes., KipKoc; 
"iepa^', KopKopac; opvic;. nspYaioT Hes., Kps^ "eine Vogelart', Kipx^oq m. ' hoarseness ' (if 
from *K£pK-avog), Kspxvr), K£pxvr|i<;f. Turmfalke'; 

Latin crocid, -/?eand croco, -are^ croak, caw ' (: Irish crain, Lithuanian krokiu, Latvian 
kracu, Slavic krakati, compare with -g: gr. Kpcb^u), Old Norse hroki); 

Middle Irish crain. Gen. crana^so\N' ('grunzend'; proto Celtic *krakni-)\ cercc^hevi (but 
cymr. ysgrechf. 'scream' from Old English "sca^c 'clamor'; Middle Irish scree/? 'scream' 
from Old Norse skreeki); abret. corcid, nbret. kerc'heiz, cymr. crychydd^Reihef, Irish corr 
( *kork-so-) ' crane '; 

Old Prussian kerkot ' aquanaut (bird)', Latvian kercu, kerC gaggle, cackle, chitchat, 
talk, snicker, sough, rustle, din, fuss, noise make', Lithuanian karkiu, kafktT burr, croak, 
caw, gaggle, cackle, chitchat, talk, snicker', Lithuanian kirkiu, kFrktr screech, shriek, 
scream, squawk, cackle, croak, yell (from the Bruthenne)'; Lithuanian krekinuos, -intis 
'rutting, in heat sein (of swine)', Latvian /rece/ 'hoarse become'; Old Prussian kracto{\\es 
kracco) ' black woodpecker ', Lithuanian krake^s., Lithuanian kr(i)okiu, kr(i)6kti' groan, 
grunt' (: Latin crocid Qic), kr{i)okiys'\Natefia\\', Latvian kracu, krakt' croak, caw, 
schnarchen, groan, bawl, blaster'; Lithuanian kurkiu, /r^A/r// "quarren', Latvian kurcu, kurkt 
'quarren' (: Old Church Slavic krbkngti, changing through ablaut with Lithuanian kvafktR); 
compare MiJhlenbach-Endzelin Latvian-D. Wb II 296, 270, 322; 

Old Church Slavic krbkngti^ croak, caw ' (etc.); russ. -Church Slavic krecet-b ' cicada ', 
russ. /re/r'Aufstehnen', Arece/'Jagdfalke', serb. /r/'e/ra'clamor of the chicken or Frosche' 
(etc.), Czech s/r/e/r 'clamor'. Upper Serbian 5/r/e/r5Ka 'Eichelhaher'; russ. krochaib 
'Tauchergans', Bulgarian /r/id/ro/? 'raven', serb. krocem, krokati^ croak, caw ' (etc.); russ.- 
Church Slavic (etc.) kracu, krakati 6s.; in addition slovz. krek {*krak-b) m. 'raven'. 

Also alb. krokaV croak, caw ' a Slavic loanword. 

Nasalized: Old English firingan^ so\}v\6, clink, rattle, clash, clatter', engl. /0/7/7^'lauten, 
clink ', Old Norse iirangu. 'din, fuss, noise', iiringia ' chme' , Lithuanian krankiu, krankti^ 
croak, caw, groan ', kranksciu, kranksti6s., russ. krjakatb 'crack, creak, groan, burr, croak, 
caw '; Tocharian B kraiiko roosier, cock; Old Indie kruii, kruhca-, kraufica rw. 'Brachvogel'. 



With ani. ^-;Old Indie sari-i. "a bird', sarika^\he Indian magpie '; Armenian sareak 
"Star'; Lithuanian sarka. Old Prussian sarke^ magpie ', russ. soroka, Czech straka, serb. 
sraka^ magpie '; besides Old Church Slavic svraka, serb. svrakaAs., see below. 

With aniaut. Ru-:a\b. sorre {* kuerna) "crow' (Jokl, Mel. Pedersen 146); 

Note: 

Wrong etymology because of alb. sorre, sorrai., Bresciano cornacia, Calabrese ciavula, 
Catalan cornellai., Corsican curnachja, currachja, French corneillei., Friulian gore, 
cornile, Greek Koupouva (kourouna), Irish carog dubh, Italian cornacchia, Reggiano 
curnaccidun, Romagnolo curnacia, Romanian cioara, Romany korungxw., Sardinian
```


## [2026-09-06T16:15:22.066Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '46080,46260p' POK_full.txt"
}
```


### [2026-09-06T16:15:22.138Z] TOOL RESULT

```
curnaccidun, Romagnolo curnacia, Romanian cioara, Romany korungxw., Sardinian 
Campidanesu carroga, corroga, Sardinian carroga, corrancra, corranca, Scottish starrag, 
Spanish cornejat, Valencian cornella^crosN' from Latin comix (-icis) " crow, carrion crow '. 

Old Church Slavic soraka, serb. svraka " magpie'. 

E.f\ui-g-\ 

Old Indie kharjaf/ ^knarrt', kharga/a'e\n certain Nachtvogel (owl?)'; 

gr. Kpcb^u) 'krachze', Kpa^u), SKpayov, KSKpaya ' croak, caw (of raven), cry'; mpayuq 6 
Tpax6(; nj6(po(; olov rrpiovajv Hes.; 

Old Norse hrokr, Old English hroc, Old High German hruoh' crow'; ndd. harken, Danish 
harke^sich rauspern', Swiss harchlen' groan ', Old Norse hark, sAa^/r 'din, fuss, noise', 
herkir, skerk/rl\re' ('*knisternd'). Old Norse harka^rant, roister', ndd. harken 'scratch, 
scratch, scrape', harke' rake ', Modern High German loanword Harke; to Old Indie kharju- 
m. (uncovered) "the itchiness, scratch ', khrgala-rr\. " crutch ' (?); 

Old High German rachison' s\c\\ rauspern'. Old English hracaru., hracui. "throat'. Old 
High German rahho' jaw ', Old English hreeca rr\. "das Rauspern; saliva', hr£ecan's\cV\ 
rauspern, spucken'. Old Norse hrakam. "saliva'; Old Norse skrsekrm. "scream' {*skrek/-), 
skraekja, skrsekta'cvj', skrgkr\. PI. "lie, falsity', 5Arp/ri/5"erdichten, erlijgen'; 

Lithuanian kregzde ' swaWow' , kreget/" grur\t' , krog/u 'r6ch\e, grunt'. 

3. Labial extensions: 

A. With -p-: Old India krpate, Aor. akraplsta^ lament'; 



krcchra-^ bad '; n. "need', Middle Indie from *krpsra-\ 

npers. sarfak^ clangor', s^/f (Iran. *sarafa-) " cough '; 

Latin crepo, -55 and -is, -5/'e''knattern, rustle, crack, creak', crepundia, -d/'i7/77'Klappern 
as Kinderspielzeug, Kastagnetten' (after M. Leumann, Gnomon 9, 240, rather Etruscan); 
EM3268; 

Old Norse ^ra/^ "raven', Proto Norse HrabnaR, Old English hrsefn^ ray evi. Old High 
German hraban, hram^rayeu' (Middle High German also rappe). Old Saxon naht-ram^ a 
night-owl, an owl '; 

With 5-: Old Norse skrafa^ babble, chatter ', skraf{av\6 skrapsee below) n. "gossip'; Old 
Norse s/ra/^ "Seerabe', Old English skrgef6s.. Old High German scarba, scarvai., scarbo 
m. ds.. Modern High German Scharbe; bret. sc/'5i/"Meervoger is Germanic loanword; 

Latvian krepet, krepet^6\r{)/, filthy become', krepat^zaheu mucus auswerfen' (from 
"*rauspern'), Lithuanian skreplenti6s., Latvian krepalasP\., Lithuanian skrepliaTP\. 
"Schleimauswurf, Old Church Slavic kroplj^, kropiti^ besprinkle, sprinkle' etc., russ. 
kropotatb "drone, grumble, grumpy, surly, sullen sein, sich sorgen' etc. 

With -b-\ Old Norse skrap'das Raschein, gossip', skrapa'rusWe, babble'; Lithuanian 
skrebef/ ^rust\e', Old Church Slavic skrobofb ^ no\se' . Nasalized gr. KpsppaAa 
"Kastagnetten'. 

II. Abasis (s)(k)erei-: 

Old Irish screti., nir. scread^screarci from * skri-zd(h)a; compare Persson Beitr. I 348; 

with s-\ bret. screo {*skriua) "kreischender Meervogel'; 

Old High German Old Saxon scnan^cry\ Old High German screiu. "scream', ndd. 
schrewen, Dutch schreeuwen^cvj' {*skraiwian). West Flemish schreemen, engl. scream 
ds. {*skraimian)\ 

without s-\ Old Norse /7/'e//77/'"clamor', Old Norse hnna^cxY (of swine); compare Latvian 
kr7na'so\N' (also Irish cra/n ds. : Latin crocid) and piem. c/y/? (Ligurian?) "swine'. 

guttural extensions: 



A. With -k-\ gr. Kpks "(the yoke) knarrte, kreischte'; Lithuanian kryksciu, krykstr 
screech, shriek, scream, squawk, cackle, croak, yell ', /r/7/rse//"quaken'; 

Old Church Slavic A/7/rb "clamor', kricati^ccY; 

Old Norse hegri. Old English hragra. Old High German he/garoan6 (h)reigaro. Middle 
High German heigerav\6 reiger. Modern High German Reiher{*kroikro-, *knkro-), partly 
with diss. Schwunde of first r, 

cymr. c/y^ "hoarse', fem. creg, therefrom creg-yr^Reihef; 

eine various Lautnachahmung is Bulgarian cirkam "zwitschere, zirpe; cry, spritze' (etc. 
s. Berneker 132); 

B. With -g-\ gr. Kplyn "das Schwirren; creakiness (the Zahne)', Kpiyn n yAau^ Hes., 
Kpi^w, Kpi^ai, KSKpIya " screech, shriek, scream, squawk, cackle, croak, yell, growl ', 
Boeotian Kpi55£iJ£v (55 = y) "ysAav'; 

cymr. cre{*kriga), dychre {*dT-eks-kriga) "clamor'; derived cre-ydd, cre-yr^Reihex'; 

Old Norse hrJka^ gnash ', hrikta^ screech, shriek, scream, squawk, cackle, croak, yell '; 

with s-\ Old Norse s/r/yTt/a "Vogelschrei', as verb "chirp, twitter'. Old English scrTc 
"WiJrger', Norwegian skrTka, skreik^cvj'. Old Saxon skr/kdn6s., Old Norse skr^kr 
"scream'; 

late neologism: Modern High German Krickente, Swedish krickand, krikka6s., Dutch 
kriek, kreker cricket, Heimchen', French cr/quef6s., Dutch kricken, kreken^Z\rpen (from 
the cricket)'. Middle English creken ^ creak' , engl. creak6s., French cr/quer6s.; 

with S-: Old Church Slavic skrbgati(\.e. skrbg-) " gnash ', skrbzbt-b (i.e. skrbz-) 
"Geknirsche'. 

III. ^basis (s)k(o)reu-, (s)k(o)rau-: 

1. Latin corvus{sQQ above S. 567); Middle Irish c/y? "raven' {*krouos)\ ndd. schrauen, 
schraulen, Norwegian skryla, /y/5"cry', Norwegian dial. 5/r/y/7/5 "clatter, noise make, sharp 
clink; cough'; Old Norse skraumi^ bawler, crier, Hanswurst'; North Frisian skrummer din, 
noise, rumor'. Modern High German schrummeln^ thunder'. Old Norse s/rm/r? "gossip; 
Lithuanian kriunu, -e//"cough, groan, moan'; perhaps also Tocharian B /rem "drum'. 



2. Dental extensions: 

With -d-\ 

Old Norse hrjota'roar, bellow, schnarchen, drone, grumble'. Old English hrutan 
"schnarchen, pant, sniff, snort'. Old High German rOzan, ruzdn'ratt\e, clash, schnarchen, 
buzz'; compare Old English hrotm. " thick FliJssigkeit, mucus', etc. under S. 537; 

Middle Low German sc/?/!//©/? "schnarchen, wheeze, prusten', wfal. Sc/7/'i/te"Truthenne', 
Swedish s/r/y/5 'brag, boast', dial, 'schnarchen', Norwegian dial. sA/y/a'pant, sniff, snort, 
prusten', skrota {*skrutdn) 'brag, boast' (perhaps also Old Norse skrautu. ' splendor, 
jewellery', sArey/a 'adorn', if actually 'brag, boast', compare Norwegian 5/r/i0y/a 'adorn, 
praise, laud, brag, boast', /isy/ads.). 

With Indo Germanic-^: Old Norse hrydjai. 'Spucknapf, isl. /7/'c»d/"saliva', Norwegian 
dial, ryda, skrydai. 'mucus in neck'. 

3. guttural extensions: 

With -k-\ Lithuanian krauklys^cro\N\ kraukiu, krauktT croak, caw ', ablaut, kriuk-iu, -ti 
'grunt', Am/re'Gegrunze'; Latvian krauklisrw. 'raven', kraukis^ rook, black European bird 
of the crow family ', kraukafQ,o\^<^\\, mucus auswerfen (of cattle)'; kraukai. 
'Schleimauswurf'; 

Old Church Slavic kruk-b 'raven' (etc.); 

isl. /7/y^/a" rattle in the throat'. Middle High German ru(c)heln. Modern High German 
roche/n^ groan', Norwegian rugde^ Waldschnepfe '; in addition probably Old English hrog^ 
nasal mucus '; 

with gemination -/r/r-.- Danish skrukke^ chorWe, chuckle', skrokke ^chai, prate', next to 
which Old Danish krokke^caW, shout, cry, from chickens ', Middle Low German krochen 
'grunt; hoarse cry (of raven)'. 

With -T(-\ Old Indie krosati, Avestan xraosaiti^ shrieks, shouts, howls'. Old Indie krosa-, 
klosa- m. 'scream, earshot ', (: Old English hream^ emergency call ' from *hrauhma), 
npers. a-^/ios 'rooster, cock'; s. W. Schuize Kl. Schr.166. 

With -g-\ gr. Kpauyn "clamor', KpauY6(; 5puKoAaTTTOu €\6oc, ('kind of woodpecker ') Hes.; 
Gothic hrukkVk. ' the crows ', hrukjan^ crow '. 



References: WP. I 413ff., WH. I 275 f., 290, 291 f., 293, Trautmann 128, 139 f., Wissmann 
Nom. postverb. 130f. 
Page(s): 567-571 

Root / lemma: ker-2 
Meaning: cut' 

See also: see below (s)ker- . 
Page(s): 571 

Root / lemma: ker-4 

Meaning: cherry 

Material: Gr. Kpavo(; m. f. = Latin cornus{*krnos) ' a cornel cherry-tree ', Kpavov = Latin 

cornum^ cornel, cornelcherry ', Lithuanian *kirnasas base from Kirnis^ deus cerasorum '; 

in addition probably gr. K£paao(; " cherry tree ' (out of it Latin cerasus), perhaps thrakisch- 

Phrygian word.
```


## [2026-09-06T16:15:41.860Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD ker ===\" && grep -n \"ker-\" AHD_watkins1985.txt | grep -in \"echoic\\|hoarse\\|shriek\\|crane\\|raven\" | head -20"
}
```


### [2026-09-06T16:15:41.910Z] TOOL RESULT

```
=== AHD ker ===
11:619:ker-2, Echoic root, base of various derivatives indicating loud noises or birds. I. Zero-grade form *kr-, becoming Germanic *hr-. 1. Germanic *hring- in Old English hringan, to resound, clink: RING. 2. Germanic *hraik- in Old English hré&can, to clear the throat: RETCH. 3. Ger- manic *hrdkaz, “croaking bird,” crow, in Old English
13:621:hréc, rook: RooK!. 4. Germanic *hraban, *hrabnaz, raven, in Old English hrefn, raven: RAVEN}. 5. Extended form *krep- in Latin crepdre, to crack, burst, creak: CREPITATE, CREVICE; DECREPIT, DECREPITATE, QUEBRA- cHo. 6. Extended form *kri- in Germanic *krik- in Old French criquer, to creak, click: CRICKET!. II. Variant form *skr-. 1.Germanic *skrik- in Old English scric, thrush: SHRIKE. 2. Germanic *skrékjan- in Old Norse skrekja, to shriek: SCREAK, SCREECH. 3. Germanic *skrainjan, to shout, shriek, in Old Norse screma, to scream, perhaps akin to the possible Scandinavian source of Middle English scremen, to scream: SCREAM. III. O-grade form *kor-. 1. Latin corvus, raven: CORBEL, CORBINA, CORMORANT, CORVINE, Corvus. 2. Greek ko- rax, raven (> korakias, chough): CORACIIFORM, CORA- com. [Pok. 1. ker- 567.] ker-3. To grow. 1. Suffixed form *ker-es- in Latin Cerés, goddess of agriculture, especially the growth of grain: CEREAL, CERES. 2. Extended form *kré- (< *krea-) in: a. suffixed form *kré-yd- in Latin credre, to bring forth, create, produce (< “to cause to grow”): CREATE, CREOLE; PROCREATE; b. suffixed form *kré-sko- in Latin créscere, to grow, increase: CRESCENDO, CRESCENT, CREW!; AC- CRUE, CONCRESCENCE, CONCRETE, DECREASE, EXCRES- CENCE, INCREASE, RECRUIT. 3. Suffixed o-grade form *kor-wo-, “growing,” adolescent, in Greek kouros, koros, boy, son: DIOSCURI, HYPOCORISM. 4. Compound *sm-kéro-, “of one growth” (*sm-, same, one; see sem-'), in Latin sincérus, pure, clean: SINCERE. [Pok. 2. ker- 577.) ker-4, Heat, fire. 1. Suffixed form *ker-té in Germanic *herthé in Old English heorth, hearth: HEARTH. 2. Zero-grade form *kr- in: a. Latin carbé, charcoal, ember: CARBON, CARBUNCLE; b. extended form *krem- in Latin cremdre, to burn: CREMATE. 3. Possibly suffixed and extended form *kera-mo- in Greek keramos, potter’s clay, earthenware: CERAMIC. 4. Possibly variant ex- tended form *krds- in Russian krasa, beauty (< “bril- liance of fire”): CRASH?. [Pok. 3. ker(a)- 571.] ker-5. Also kere-. To injure. Suffixed zero-grade form *kro-yé- in Latin cariés, decay, caries: CARIES. [Pok. 4. her- 578.] ker-8. A kind of cherry. 1. Suffixed zero-grade form *kr-no- in Latin cornus, cornel tree: CORNEL. 2. Full- grade form *ker- probably in Greek kerasos, cherry: CHERRY. [Pok. 4. ker- 572.] kerd-', Heart. 1. Suffixed form *kerd-en- in Germanic *hertén- in Old English heorte, heart: HEART. 2. Zero-grade form *krd- in: a. Latin cor (stem cord-), heart: CORDATE, CORDIAL, COURAGE, QUARRY!; ACCORD, CONCORD, CORDIFORM, DISCORD, MISERICORD, RECORD; b. suffixed form *krd-yd- in Greek kardia, heart, stom- ach, orifice: CARDIA, CARDIAC, CARDIO-; DIPLOCARDIAC, ENDOCARDIUM, EPICARDIUM, MEGALOCARDIA, MYOCAR- DIUM, PERICARDIUM. 3. Possibly *kred-dha-, “‘to place trust” (an old religious term; *dho-, to do, place; see dhé-'), in Latin crédere, to believe: CREDENCE, CREDI- BLE, CREDIT, CREDO, CREDULOUS, GRANT; MISCREANT, RECREANT. [Pok. kered- 579.] kerd-2. Craft. Suffixed form *kerd-d in Old Irish cerd, art, artist: CAIRD. [Pok. 2. kerd- 579.] kerdh-. Row, herd. Suffixed form *kerdh-d@ in Germanic *herdo in Old English heord, herd: HERD. [Pok. kerdho- 579.] kere-. To mix, confuse, cook. 1. Variant form *kra- (< *kraa-) in Germanic *hrdr- in: a. possibly Old English hrér, lightly boiled, half-cooked: RARE?; b. Middle Dutch roer, motion: UPROAR. 2. Zero-grade form “krp- in: a. suffixed form *kro-ti- in Greek krasis, a mixing: IDIOSYNCRACY; b. suffixed form *kro-ter- in Greek kra- ter, mixing vessel: CRATER. [Pok. hero- 582.] kerp-. To gather, pluck, harvest. Variant karp-. 1. Ger- manic *harbistaz in Old English herfest, harvest: HAR- VEST. 2. Latin carpere, to pluck: CARPET; EXCERPT,
68:2163:RATITE era-2 RAUCOUS reu-1 RAVEN! ker-2 RAVEN? rep- RAVIN rep- RAVIOLI rap- RAVISH rep-
```


## [2026-09-06T16:15:42.709Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kahrkāsa\\|kahrkasa\\|kahrkatāt\\|xraos\\|xraosaiti\\|xrōs\" BRT.txt | head -30"
}
```


### [2026-09-06T16:15:42.756Z] TOOL RESULT

```
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
3511:Ableit.  ins  ^apajrattsa-  m.,  zum  V.  xraos-.  — ■i.  vgL   aptirBSa-  m.  'Schmätiung'.
3622:•  j.  apa.skaraka-  Adj.  'hohnsüchtig,  höh- nisch': nivßyaka  nipasnaka  °^a{NP.)  apa.- xraosaka  imä  paifi.vlsmte  Yt.  5.95.
4820:—  zu' :  xshms  asamqm  unänö  pärayeinii . .  avi  garS  nmänam  V.  75.32;  —  x3  patti apqm  paräiti  .  .  a^ra  . .  V.  jj.  51;  — xraosyS-taraca  (sd.)  .  .  hv5  urva  paräiti par3.asnäi  amihe  yaia  . .  V,  13. 8;  —  ya- tärö  paurvs  us>hiUaiti  paräiti  vahiltahe atshsus  y .  iS.^d.  2)  'aus  (dem  Haus) gehen  auf  — ,  zum  Zweck  der  Verrichtung von-'  (Akk.):  *kat!lmS  timänahe  a'iauru- fi9m{sd.)  pärayäf^''  N.  /;—  para  paoiryö äiti  (näml.  a^aururitm)  para  bityö  aiti para  "hrityS  äiti  aita  paräyaiti  ycc^a gae'^äbyS  *k)nti  "es  geht  der  erste  (auf Priesterdienst)  aus  . .  der  zweite  . .  der dritte.,;  es  gehen  die  weg,  die  (zum  Schutz) für  den  Hausstand  da'gelassen  worden) sind"  N, 2 (?)"'; — katärsm  *ä'irava  ctiauru- n>m  Vä  parayat  galiaiiqm  vä  asp^nns (sd.)  avat  N.^;  —  katärS  a'^aurun?rn ''parayat  nSirika  vä  nmätiSpaitiH  väi yezica  vä  ga^hä  vTmä  (sd.)  *katarascit ''parayat  N.  5;  *5";  —  *cvät  ''aiwtstXm parayap  'irixsapar>m  .  .  yS  haoys  (sd.)  . . paräiti  nsit  .  .  anaiwistim  (sd.)  ästryanti N.  4.  a)  mit  haca  und  Instr.:  cval  .  . äiirava  a'iaurumm  haca  ^gafi^äbis^para' yat  N,  4-  3)  'sich  an  etwas  (Akk.) machen':  yö  nar)m  ..  kasyat»he{%d.)  sanhai daoaili  vl^va  aval  hava  xraiwa  paräiti "—  wissentlich  mit  voller  Absicht  macht  er sich  daran— "V,  15- 2.  4)  'hingelangen zu  — '  sva.  'sich  verschaffen':  ffi.j(Akk.),. kaine-.tarS  äaxit^m  pärayät  tarS  ap»mca urvarqmfa  yezica  . .  tarS  (sd.)  daxst>m paräiti  . .  "nicht  soll  das  Mädchen  heim- lich sich  die  Regel  (wieder)  verschaffen, heimlich  sich  Wasser  und  Kraut  verschaf- fen .."  V.i5,9f.
10579:•  j.p  g.  xraos-  V.  'schreien'.  Praes.  2 xraosa-,  26  xraosya-.  —  PPfP.  'xrusla-.
10581:erschrecken':  yö  g^wqm  .  .  janaiti  vil vayeiti  vä  xraosyäti  vä  pazdayäti  (sd.)  vä
10583:mit  upti  "aufschreien'  vor  Angst  oder Schmerz;  zaRyUca  vispinhd  xraosmtqm upi  "und  dem  Verderben  preisgegeben sollen  sie  alle  aufschreien"  Y.  5J.  8.
10587:•  j.  xraosya-  m.  'Schreien';  a)  zum  Zweck des  Erscl^eckens,  'Anschreien'":  *'yj  F. 2jb">.  b)  aus  Angst  'Angstgeschrei': «i'iV  /li  anyä  urva  haom  urväntm  .  . bq^aiti  °yäca  (LS.)^'  voyaca  *aiihe  ". .  (bei sva.)  trotz  ihrem  (der  Seele)  Angst-  und Wehgeschrei"  V. /j.9'(?),
10589:•  j.  xraosyö.tara  Adv.  'unter  ärgerem Angstgeschrei':  'ra/a  na  ahtmlt  voyS.- laraca  kvS  urva  pariliti  par^.asnäi  atiuhe ya'^a  ..  "unter  noch  ärgerem  Angstgeschrei und  unter  grösserem  Wehklagen  geht  seine Seele  weg  zum  künftigen  Leben,  als  .  ." V.y.8.
11081:Ordnung:  manahicä  vacakicä  syaoiansi Y.30.3.  Bj  zur  Anknüpfung  eines  neuen selbständigen  Satzes  'und'  oder  imüber- setzbar;  m  folgt  dessen  erstem  Wort  b)  im Aw.:  duwar>snat>hs  da/snyä  (sd.)  hsnts xaAyJcä  .  .  xraospTitqm  (sd.)  Ufa  .  .  tratä is  dra/sS{&d.)  ..  momc3(s±)  asta  Y.5J.8; —  atySs, .  akäl  (sd)  mananh3  st3  äirym drBjtucS  pairi.matsiscä  (Sp.564  m.)  syao- tnqm  ..  Y-32-  3;  —  aj  f3  mainyB  ..vaAyi aitmcä  (sd.)  äsca  hudarthS  prj/  vTsyatä "^i-SO-y,  7  (aimaua),  32. 1  {aüyacä),  45.  7, 4-.S  i'äc'a),  49T>  1°  {''^l^^)y  49-  S  {täim, S3-3  C^*"^^);  —  a^äca  "kiwä  Smavantaslä (Sp.  567  a)  buyamä  rapsUca  tä  HS  dan- gStncS  ustäca  (ßp.  568  m.)  Y.4i-4',  —  *i)mS janhtntu  yahmat  haca  ..snatiat,.  'hriiatca (sd.)  &ia  .  .  gStd  apajasat  .  .  aß  paurva 7'aMaKyai(sd.)  ..  aidaca (sd.)  ila  ..  sadayät V.2.22— 24;  —  hö  vTsp>m  ahüm  ..va?nai .  .  darfsta  ddiat  * amir^x^äntim  vispqm ..galiqm  Yt /p.94;  —  (Vnam  ..  sqm' .  . yazamaUe  yä  ni  baraitl  yäslä  tsi  gmi  . . tä  yasamaide  Y.  38. 1 ;  —  kyatca  mSt  tnraos ..at..\. 43.12;—  prssa^a  na  ..  Y.  43- 10;  —  avavaitya  ..ya^a  im  sk  astica  im xä  avaiti..Y.i9.T,  —  *vJsqs  *tac'a'^>  i'taä Mäm^lf  . .  vJsmte  "und  diese  zwanzig Namen  .."  Yt. /.  19;  —  dasa  ..  msrfhö sayana  dva  hamina  talla  fanii  sarata  .  . V.  J.3;  2.41;' JÄ65  (/ijÄi),  YL/5.  51 ifaifa),    Y.  19.  10  f.  {fltiaica),  8.  4,    ig.  6
12027:xraosyB.taraca  (sd.)  «?  ahitiat..  hv5  urva paräiti  parll.asnäi  anuhe  ya^a  vikrkd  va- yui  (sd.)  taile  (3SPM.)  *dramna  banzilte razBire  (sd.)  V.  y.  S.
15924:1)  'aufscheuchen':  yä galwqm  yam  apu- %rqm  janaiti  va  vayHti  va  xraosyeüi  va paldayäli  va  "wer  eine  HUndin,  die  kurz zuvor  geworfen  hat,  schlägt  oder  verfolgt oder   anschreit   oder  aufscheucht"  V.  i^.
19198:•  j.  nivayaka-  Adj.  'der  einem  Schreck einflösst,  terrificus':  °ka  (NP.)  nipamaka apa.ikaraka  apaxraosaka  imä  paiti.i-Tsmte
21123:—  täsca  ti  mraemi ..jahwdtara  y  azayö  .  .y  aspahe  arsnö  psrsska  (sd.)  V,  jj.  ii; (näml.  hfnti)  ,.  y'  vä  vthrkäu/tB  V.  J<?.  65;  11;  —  cvat  .  J  y  varisnahe  kihrpake 65'i — ..xraosyjiarai^A^ca  ,.ahmäl..hvS  d!us(Sp.  674m.)  N. /off;  *^6;  —  äat  na  .. urva  paraiti .  .y  vthrkB  vayBi  (sd.)  tüite . .  xsäudrinqm  payanhqm  paiti.barai1  y"  ^rii V.  ij.  8;  P.  33;  —  ima/  vatshB  imat  srayd  c^arwia  N.  6-j ;  66^ ;  —  cvaiti  . .  *s?mana y  tarn  ..  vasanht  V.5.ar(?);  *—  /ra-' avAali  y  gäul /raraiti  H.iy;  —  ctatti vasayS  . .  ya.  masyehl!  akmät  .  .  y  ('als  l  "aäsayai  y  .  .  gämq  dvaca  *dasaca diss')  va/a/rainravaire(sd.)Yt.  13.64'^;  —  \*atüaryS^wqm  (sd)  F.  27  a.  2)  die näirivaile . .  ahntat pourum  framraomi  y  \  Aussage  des  j'°-Satzcs  ist  angenommen; inayavö{sd.)/raväx7oii'V.4.4T{i)^''.       zu  > 'wie  wenn,  als  ob';  uzw.   i)  sie   «ird  als
23300:Mit  Akk.  'sich  kleiden  in  — ,  anziehen, sich  umtun;  anhaben';  Akt.  und  Med.: uai  vaslrä  vanAalu  V,_y.  19'';  ^^<Kcri7««( vastra  va»Aaia  (^S.)  andvl  YL5. 129"; —  spafta  vasträ  zanhaiti  tpaita  (sd.)  Yt 10.  126";  —  yS  vanhaiti  .  .  al^Js/a \frazus5  sanhasSa  .  .  N.92'*;p5;  —  *yffi .vanhinti  hntts^a  paiti-varahasca  ü.gi; I  —  kamn>m  (sd.)  vaste  vanhafum  V.  4. 49; *Y.8^^;  —  anyqmla  sutsm  vatfhsnahe N.52(?);  —  vanhSnS  F.S;  —  asman?m .  ,  yint  maedä  vasle  vaahansm  stfhr- paesanhim  "den  Himmel . .,  den  M.  anhat als  sein  aternengeschmiicktes  Gewand"  Yt. 13.  Z\  —  mainyul  ipjnisis  y7  xraosdtstsng asstis  vaitf  "der  heiligste  Geist,  der  die festesten  Himmel  als  Gewand  trägt"  Y. 30.  5.  Wertlos:  vanhäna  x^aita  raoci :fanvaitT^ia  vsrtsU  Yt  j.  i.
23434:'jagen,  jagend  verfolgen' :^ff^a8a'a»i_j'^»t apu%ram  Janaiti  vIt  vayäti  va  xraosyäti vä  patdayeiti  (sd.)  vä  V.  75. 5 ;  —  ysi  vlsps U  apayeinti  yq  *aoe  paskät  vyeinii  ". ,  denen sie  von  hinten  her  verfolgend  nachjagen" ¥.57.29;  —  y&  *ava  ^xbayats  avaähe vyqsca  vyanasca  apatse  (sd.)  zbayeitt vyqs  apagaße  vyänS  "welche  beide  um Hilfe  rufen  der  Verfolger  und  der  Ver- folgte .  ."  Vt  i^.  3S;  —  aval  vayul .  . yat  xtia  dqma  vayemi  Yt/J.  43''.  1
23797:•  j.  voya-  m.  'Wchruf.Weh-,  Zetergeschrei'; i)  über  andere:  ys  F.  25b''.  2)  über sich;  xraosyai&d.jca  °yaca  (LS.)*'  *at3ke V.  jy.  9'.
23800:•  j.  voyö.tara  Adv.  'Umentantius,  unter grösserem  Wehklagen':  xraosySJara{sA.)ca nS  ahtnät  'ra^a  hvS  urva  paräiti  parS.asnSi atsuhe  ya^a  .  .  V.  /j.  8.
25632:—  %rlsat  iarS  pintümat  hi  'vätam vahiit^m  ahSm  frapärayent  (Sp.  851  m.) az»m  yO  akurS  Y.ig.6;  7/.16;  —  Al asäunqm  'vanS  (ak  AP.)  .  .  tarO  cirtvats pinlam  viiarayati  Aaas  (sd.)  .  .  yasata- nqm  V.  ig.  30;  Vd.  2;  — pairi  dim  tanava .  .  'vün-im  haca  vaAistät  ataAaot  Y,  ig.  7; 7/.  15;  —  xraosySIara{sA.)ca  .  .  hvS  'va
27163:fraca    xraosySit  fraca     syazjaysit    "ohne
28058:•  g,  zaKya-''  Adj.  'der  im  Stich  gelassen, dem  Verderben  preisgegeben  werden  wird, soll';  'XyäSs'^  (NP.)  vTspSnhS  xraospntqm upa  Y.5?.  8.
28630:Verbindung  mit  dem  Pron.  poss.  Aava^-. yS  .  .  jainti  .  .  xraosyBJara{&A.ya  .  .  kvS tirva  paräiti  parS.asnäi  arauAe  .  .  nSil  hl anyS  urva  haom  urvan>m  .  .  bqtaiti  V. /j.  8f.;  —  —  in  Korrelation  mit  eioem Relativum:  yB  .  .  ''manahtm  ahüm  *paiti.- irinaxti  nSit  hl  gäus  bvat  ^.40;  ~^  yB nars  sna'itm  usiAülaiti  a3at  Al ägtraptam V. 4. 17;  —  yB  janai  spanim  ,  .  ha  Al asti  ci^a  ^.13.4;  12,  24,  4.  11,  18,  55, 6.  10,  S.  23,  14.  1,  15.  50,  16.  14;  —  yB anyahe  nairika  .  .  *parat»hacäiti  kat  kl vä  aitm  (Sp.  338  No.2i)  ^w/^^-a/  N.6; — y5  Bsca  . .  ainartAa  asti  masyB  gMtrvaya Al  pa\awe  tavan  pairi  il  uü  vrrm&iü skandim  //'> '°'  manS  kirmüiti  Y.p.  38; V.  7.  5 1 ;  —  yS  .  ,  daAmtm  jainli  .  . i^arstn,  ^x^arB  nBti  hl  (zu  ß)"'  ar>Aat .  .  upa.bar>tayal{sA.)ca  N.  4^;  —  yaica  . . yazaite  '^rilät  tarB  ptntamHt  Al  (zu   'f)
29545:—  in  Beziehung  zu  einem  Relativ  (Sp. laoo  o.):  yS  ..jainti  ..  xraosyBJara{sA.)ca ..hvö  urva  paraiti..  Y.13.S.  b)Plur.: karapanS  kävayascä  ,  .  ying  x' f  (NSm.) urva  a:''<i/(NSf;)S>i'ä  xra^dai  (sd.)  dalnä Y.  46. 11;  —  ySi  . .  aistmpm  vandm  (sd.) .  .  x'aii  hisublS  Y.  49-  4;  —  drygvä  , , duiazöbä  hqs  x'ait  /yaoäanais  aAfmuslB (sd.)  Y.  4^-  4;  5'-  13;  —  karapata  . . "*■  jÄtrfil (sd.)  x' aii syaohanaisca  sfnghäiuä yP  1/  sfnghB  . .  Y.51. 14;  —  tq  yatäi x'nis  rUtmSnls  Y.  51.  22;  —  *asttm (sd.)  läira  fralarmta  . .  maSyaca  hvqm anu  uslTm  saoämca  V.  2. 11; — fravalipfi .  .  amalrajanB  (sd.)  ham^r^hj  havai  tä- maica  taelaica  Yt.  rj.  33;  — -  ta  (nämL frava^ays)  ya^yänti  .  .  have  asahi  üi- hrai^a  Yt  13.67;  —  /ravafayS  . .  apm alfymnä  haväi  kaHl  na/ai"^  havayäi vise  Yt  13. 66;  66'.  Undeutlich  (ver- derbt, wertlos):  *hava^'>  aUma  hava bansmarta  ti.ioS;  —  hva  hitva  V.  2. 5
```


## [2026-09-06T16:15:51.142Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kahrk\\|kalirk\\|karkasa\" BRT.txt | head -20"
}
```


### [2026-09-06T16:15:51.189Z] TOOL RESULT

```
6553:äämanqm  t»r>/sjrSrqm  k>njs  paitt  ntsrt- 1  =  -„        vt  3  q nuyai  'vayqm    kahrkäsqm  "den    allerge-     ''ko^A.  in  Abi  ei  t
9228:masys  upäps  yd  ranhaya  .  .  var?ss.stava-  ,  j.  kahrka  indekl.,  den  Ruf  des  Hahns
9233:14.  II,  34.  13;  tS-  3.  zs.  M.  4-  ,  .   kahrka'tit-  f.  (gemeiner  oder  Spott-)
9240:(fem-  Vi-).  ^  j    kahrkana-  m.  Name  einer  gläubigen
9245:/p,  19; — ya~ia  VIS.,  yahmäi  nsitcahmäi  •   j,    kahrkäsa-   m,  'Geier':    '53  zannu-
9251:srayä  voumkaiaya  Y,  65. 4;  —  ys  haaiay-j  S/-'^v^'^'jU^'ond''zD"'"w',/irLter ...va  uruassayat  '«o»  Yt,5.  131;  —  ^-i  HriÄ^-^  No^T).  -  mp,  fl'ü.  Tu  V.'s  49" rasmanS  hqm.ststse  (sd.)  ^5  ^'na  ">  J'  karkäi,  vgl.  np.  (Npa,)  kargas. iHndayänti  Yt,  jj.  39;  —  yaoz)nH  »aA'«j.*kahrkäs5.parana-"  Adj. 'mit  Federn •«ff  (NP.)'>  rasmans  Ytio.36.  2)  zeitlich  ^  des  (Vogels)  Kakrklsa  versehen':  isunqm (nur  Komp.).  ^-paranum'^  Yt/o.isg.
9548:arjnm  mainyüm  /ramiUm  aspahe  'pa (IS.)  Yt;p.29;i¥.i8,zi,r4.9;  —  ahmli . . üjasat  vaztmnö  i'sri^raynS  uftrahe  'fa ■  Yt. /4- n;  P-J-i  —  nizbayemi  iistrtni  .  . \gius  'pa  Y.if}.3T,  Yt&i6,  74.7;  —  he I  'pa  varäzaie  Yt  ;^  1 5 ;  —  maiiahe  'pa  Yt |j4.23;  —  bUzahe  'pa  Yt  74.25;  —  yat dim  us;a  usdi'qnayat  .  .  '^raltaonS  m^?- yahe  -pa  kahrkäsahe  Yt.  J.  6 1 ;  —  m»rrjahe 'pa  vär^iiahe  Yt/4. 19,  /9.35;  —  zaf- nimnpitt  .  .  :^ar^n3  m^rjyahe  'pa  fra^usap Vt/'>.34.  Undeutlich:  ratufris  *n.liri- A-ayi  'pa  näij  payauhs  nSit  sun5  'pa payai?h5  ratufris  v>hrkaya  'pa'a  paya- uha^a  N.j()*',  [V,  7.  a:  lies  maxHJ!'^
13095:j,,  g.  dahyav-''  j  dahyu-^''  f  'Landgebiet, Landschaft,  Land',  oft  zugleich  auch  von den  Bewohnern;  a)  im  Aw.:  haraiti  bars .  .  hama  psirisäite  fräpayä  (sd.)  °rihus  ä upaola>ihvasca  Yt ig-\;  —  kahrkasS  .  . yS  naotnyä{sd.)cit  haca  'hihaot  .  .  xrUm aiwi.va&iaiti  Yt.  14.  33;  — par3  *S3mS  al- tanßta  *'iih3us^  anhat  b>rptd{s^)  7-i}sir?m V.  2. 24;  —  nSii  ..  asar?hal:a  /i^fyraf/a 33
18646:~  'mähe  F.  i;  —  kahrkäsS  . .  yS  °myäUt (ISf.)^    ha'a    daiühaot    muiti.masatshim
18886:•  Yt7.3; — frsit  mg  tat  'ma  framrüm  Yt /.  S;  — yasia  me  .  .  tmi  •inlnli  (als  AP.) drfftJayS  . .  Yt/.  16;  11,  15;  —  ^vjsqs *taia  imi  'msnü  (als  NP.)  parltas^a  '.  . vismie  Yt /.  19;  —  l&sca  mg  °ma  (AP.) abaya^a  Yti5. 49,  50;  —  gSusca  'ma mazdaoätfm  Yt  Ä  2 ;  —  'mSni  amslanqtn sptnianqm  Ytrf-a;  7;  —  sPaitka  va  duyta va  'va'ni  V.  14. 15  (?) -ö.  a)  AS.  und  LS. (im  Sinn  des  IS.)^*  als  Adv.  'mit  Namen'; i)  im  jAw.  AS.  nqma,  hinter  dem  Nom. propr.ä':  iar^zahi ..yat  vaolii^A^ häkairJm °ffio  Yt/0.88;  12-7,  i^-SS';  — pairikayai .  .yS  duzyairya  yqm  mafyaka  . .  Auyäiryqm 'ma  ao/aiti!  (sd.)  YtÄ  51;  V. /j.  z,  6;  — tturf/S  .  .  yim  ma^aka  .  .  kahrkatas  'ma ac/ai/e  (sd.)  V.iS.i$;  17.31  —  vayui  bä 'ma  äkmi  Yt  75.  43 ;  43-48  (oft),  /.  7,  8, 12—15  (oft);  —  vairil yB  haosrava  'ma YtJp-sö;  59,62,  7.30,7^,129',  142,74. 59*,  V, /i".  15;  —  ar?dvi  'ma  apa  V.7.16;
27495:•  j.  srvi^täy-  Adj.  'mithömemen  Widei- haJten',  vom  Pfeil ;  ifunqm  *kahrkäss.para- nam  zaranyS.zafram  °stayam  Yt, /o,  139.
27962:•  j.  zar90U>manay-  Adj.  'mit  goldenem Halsschmuclc':  kahrkäsd  •mainii'^  yt.  14.
30344:•  j.hu-b»retö,"barfltS,''baramn'>  Absol.  •  j-  hu-fravaxS-  m.  EN.  eines  Gläubigen: 'mit  guter  Pflege',  in  Verbindung  mit  dem  '  'växs  i^^.,  statt  GS.)''  kahrkananqm  (sd.) V.  ^bar-:  nmänB.paitlm  ..yg  iiB  'tarn  barät\asaonS  Yt/J.iz?.
```


## [2026-09-06T16:15:51.377Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"xrōs\\|xrōsīdan\\|xros\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T16:15:51.438Z] TOOL RESULT

```
NYB_vol2_glossary.txt:4298:xrostan to cry, to shout: 6 didn dévan apar bē xrēst 43'-33; vàng urost 619. — MPrth xrwštn, xrws- (S, A-H III) ‘to call’, MPrs zrwstn, xrwh- (S); NP zurös ‘a loud cry’, xurošidan ‘to shout’; Ghilain 64; Verbum 185; Schaeder, IB I, 254;
PHD_mackenzie.txt:5574:xros [DYLKA < A dkr); hlws I P xrws, N Xl/Yos] cock.
PHD_mackenzie.txt:6136:call xrostan, xwandan.                  chaJJ kith.
PHD_mackenzie.txt:6215:cock xros.                               composed hambastag; be- hambiidan.
PHD_mackenzie.txt:6321:cry (v.) xrostan; (weep) griyistan.        daytime rozgar.
PHD_mackenzie.txt:11704:xuftan l               \,~,~           xrostan                \\te..1' ~
PHD_mackenzie.txt:11722:                                       xros I                   ~~
```


## [2026-09-06T16:16:05.995Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# find which page contains line numbers\nlines=t.split('\\n')\ndef findpage(sub):\n    for i,p in enumerate(pages):\n        if sub in p:\n            return i,p\n    return None,None\nfor sub in [\"kahrkäsa-   m,  'Geier'\",\"xraos-  V.  'schreien'\",\"kahrka'tit-\"]:\n    i,p=findpage(sub)\n    print(\"=== leaf(0-based)\",i,\"for\",sub[:25])\n    if p:\n        # print numbers that look like column numbers\n        print(re.findall(r'\\b\\d{3,4}\\b',p)[:30])\nEOF"
}
```


### [2026-09-06T16:16:07.628Z] TOOL RESULT

```
=== leaf(0-based) 274 for kahrkäsa-   m,  'Geier'
['131', '107', '453', '454']
=== leaf(0-based) 317 for xraos-  V.  'schreien'
['136', '535', '536']
=== leaf(0-based) 273 for kahrka'tit-
['112', '107', '299', '156', '455']
```


## [2026-09-06T16:16:12.356Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9226,9256p' BRT.txt"
}
```


### [2026-09-06T16:16:12.400Z] TOOL RESULT

```
'""  """■  ')    Nach    JtJSTI  GlrPh.  2.  455    das  Volk  der
•  j.  'kara-  n.  Name  eines  Fisches";  'r5'     Karchedonier  (KarthagerV
masys  upäps  yd  ranhaya  .  .  var?ss.stava-  ,  j.  kahrka  indekl.,  den  Ruf  des  Hahns
nhsm  äpS  urvaliim   marayeite  Yt  14.  29;  nachahmendes  Wort  'Kikeriki'.       a)  auch
V.  sg.  4a.  als  Bezeichnung  des  Hahns,
•)  Im  Mp.  iar  m<>hU,    ein  mythischer  Fisch,  KompA. ;  Abicit.  —  np.  tart  'Huhn';  ai.  vgl.
der  grösste  und  Akt  Ralav  der  Fische;  vgl.  Bd.  krka'vAkav'  m.  'Hahn',
14.  II,  34.  13;  tS-  3.  zs.  M.  4-  ,  .   kahrka'tit-  f.  (gemeiner  oder  Spott-)
.]  'kara-m.EN.emesTuramers:.^.j^e^^  ^'^^^   ^^^  ^^^^^._  \           y^  j^/,jJl
alavazdä..yatbavämaa,tut.vanyädänavs  ^^^^  ^^^^      -^  „^^^^_^^  ^...  ^„.,,„,^„^^
/ara..'r>maasa6a„>mvar,m^a..\t5.n-  uas  (NS.)  nama  aojaiU  Y.iS.iS-
'^'8'  *'''''■'                                                               '  Eig.    ■Kikerlkitum'.    —    Vgl.   ZDg.    iarktiis
•  j.,  p.  ^kara-  Adj.  (fem,  VT"-)  'machend  'Geier'O,  al.  fytaivafav-  m.  'Hahn'.  —  Pü,: (usw.)'.  *'^*-  —  '*  ZDMG.  s6.  63  i  haplol.  auä  *iar-
KompE.  —  Zum  V.   >*ar-.  —  ai.  "/■aro-  Adj.        iaiJiäi-   'Hähnerresser',  vgl.  lu  ioArhlsa-.
(fem-  Vi-).  ^  j    kahrkana-  m.  Name  einer  gläubigen
•  j.  "narate  (sd.)  karaiain"  N.p;.  Familie:      hufraväxs     'kananqm      asaonS
•  j.  'karana-  m.  'Ende';  i)  räumlich:  "des  gläubigen  H.,  (aus  der  Familie)  der 'Grenze,  Rand;  Ufer;  Flügel  (des  Heeres)';  A'."  YL/j.ia?.
dalinsm   upa   '■Tum   airihä  ziiiHi  YtiO.99;'  Ableit.  aus  Va^rin-,— ai,  vgl.  :*/-.<'ai?a-m.  (eine
12.  ao;  —  «va  -iia'>  ai^hä  2?m9  Vt.  lO.  95;  '^^  Rebhul.n.  auch  als)  EN,
/p,  19; — ya~ia  VIS.,  yahmäi  nsitcahmäi  •   j,    kahrkäsa-   m,  'Geier':    '53  zannu-
nalmanqm  "na'^  pairi.vasnöiie  ". .  bei  dem  mainil  (sd.)    YL  i4-  33;    —    msrrjahe  . ,
nicht   Anfang    noch    Ende    zu    gewahren  -sähe    Yt,  5,  61;    —    as.^ar}limaabyS  .  .
sind"  YLi^,3;  —  upa yaozsnta  -na''  zraya  dämattam*k?r>fi.:^arqttt  k:-r?ß paiti  nisri-
vouru.kaSaya  "an  den  wogenden  Ufern . ,"  ttuyjl  vayqm  'sam  V.J.  20.
Vt.5.  38;    —     yaoZiflli    vUpe    °n3    (NP,)''         KompA.'—     I^omp.;     *ta/iria-\-*.lia;     eig.
srayä  voumkaiaya  Y,  65. 4;  —  ys  haaiay-j  S/-'^v^'^'jU^'ond''zD"'"w',/irLter ...va  uruassayat  '«o»  Yt,5.  131;  —  ^-i  HriÄ^-^  No^T).  -  mp,  fl'ü.  Tu  V.'s  49" rasmanS  hqm.ststse  (sd.)  ^5  ^'na  ">  J'  karkäi,  vgl.  np.  (Npa,)  kargas. iHndayänti  Yt,  jj.  39;  —  yaoz)nH  »aA'«j.*kahrkäs5.parana-"  Adj. 'mit  Federn •«ff  (NP.)'>  rasmans  Ytio.36.  2)  zeitlich  ^  des  (Vogels)  Kakrklsa  versehen':  isunqm (nur  Komp.).  ^-paranum'^  Yt/o.isg.
KompE.  — np.^j«H,ianär4).~PÜ.;^a«fl™^,|       "»af"«J.:    %.  fiariiia..    —    D  NA.  kortii-irt    in
_,)ND.-')U<.them..vgl.flJfl««fl.No,i,-'      4,-,„J„,
3)  Hds. /M/fli-axrt.  —  41  Kaum  lu  ai.  *<j/(i- f.  .      ,     '  ,,      ,     .       -j      .     t.
(ZupiTEA  Germ,  Gmt.  107).  •    J-    •'^'■»t-    V.     schneiden'    Praes.    9
.  j.  »karana-  n.  ein  Kleidungsstück  mite- '  f '■^'''«■'  "^  ^^^^t""  =  k>nnv-'\  12b lererGrösse, 'Hose'');  v«.«.r?y^.^«..««^,,r'f''-'«-'':  9+^4  -f^^«va-,  n  k.r.>ya-i\ "eine  Hose,  die  die  beiden  Schenkel  be-'~  \^[^-°'''.^f"^'-     .  ,    .    -,      .
```


## [2026-09-06T16:16:12.956Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"xros \\[\" -A2 -B2 PHD.txt | head; echo ===; grep -n \"xrostan\" -B2 -A2 PHD.txt | head -20"
}
```


### [2026-09-06T16:16:13.010Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-06T16:16:25.547Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"xros\\|xrost\" PHD.txt | head -20"
}
```


### [2026-09-06T16:16:25.588Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:16:25.972Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5570,5580p' PHD_mackenzie.txt; echo \"----NYB----\"; sed -n '4290,4302p' NYB_vol2_glossary.txt"
}
```


### [2026-09-06T16:16:26.028Z] TOOL RESULT

```
xridan. xrin- [ZJ1NN-tn < A "II zbn I M xryd, xryn-, N xaridan,
                                  '
  (xar-)] buy.
xrohak [hlwhk' IN.......,] coral.
xros [DYLKA < A dkr); hlws I P xrws, N Xl/Yos] cock.
xri)stan [hlwstn' I M xrwst] call, cry.
xiib [hwp I M xwb, N .......,] good.
 . . . . ih: goodness.
xuftan. xufs- [HLMWN-tn l < A "II (llm; hwptn l , hwps- I M xwpt, N
  xuftan, xusp-] sleep.
xiig [HZWL Y A < A lJ,zyr); hwk l IN . . . . ] pig.
----NYB----
running round the lowest part of the lanee', also other sorts of rings, or 'coat of mail’, which is possibly a lw.; but this is à mere guess.
Xösröi [hwslwd; hwslwd' 110!5 M, but hwslwd Cod. K 43b] n. pr. A. the 3d king of the Kayanian dynasty, mostly known as Kai-Xösröi [kdhwslwd, -Iwd'] 7133. 1138-17; with the patron. Siydvaxsan 116’; eschatological hero 887°. 99—100 passim. 1065; — ~ i Kavätän, founder of five cities 114? sqq., is probably the old Kayanian king of the heroic saga. — B. the Sassanid kings from Bahram I (273— 276) onwards assumed the title ka? (g.v.) and regarded themselves as Kayanians: Kai-Kavät (488—531), his son im bag Xösröi šāhān šah i Kavätän (531-579) 10921, known as anösak-ruvän 118%; on Baxt-— v. this w. — Gr Xoopöns, NP Xusrav; Av. (1738) žhaosravah-. The spell- ings are: 1. on coins: hwslwd, hwslwdy (already Prth); hwslwy (predominant un- der Khosroes II 590-628); once hwslw? and once hwslwty (!) v. Paruck 380- 384. 386-390; Hansen, Catrang 18-19; — 2. in the inseriptions: KZSPrth hwsrw, Gr. v. Xootew, Prs hwslwb, which is also the spelling in three of the cities mention- ed 1141? sqq., certainly to be pronounced Xūsrūv = Arm Xosrov (but Syr Kösrö). In my opinion the BP form hwslwb' re- presents in reality hwslwdy, -b- being, as often at the end of the w., the cursive form of the letter d as written in the Ps.
Xösröi-mustäpät [hwsrwd mwst’p’t] the name of a town, otherwise unknown, in the W. quarter of Iran 114%, v. Cat. 58 sq.—‘Kh.’s merry settlement’: āpāt v. āpātān; must < musta-, pt. of Olr *maud-, Skr modate ‘to be delighted’, whence Av. (1109) maoóano.kara- ‘affording sensual pleasure’, (280) a-hömusta- < *ham- musta- ‘delighted’.
xrafstr [hlpstl] Ahrimanic, noxious ani- mals 76%, — Borrowed from Av. (538) arafstra-.
219
xUahišn
xrat [hlt'] reason, intellect, intelligence, wisdom, understanding, passim; mēnēyē ~, üsn xrat: v. MENİ, dsn; menöye asn ~ 7614, — Av. (535) zratu-; MPrthPrs ard; Paz. xard, x(i)rad; NP xirad.
xrós [hlws] cock 56%, — NP zurös [NW form] and xuroh (SW form); from
xrostan to cry, to shout: 6 didn dévan apar bē xrēst 43'-33; vàng urost 619. — MPrth xrwštn, xrws- (S, A-H III) ‘to call’, MPrs zrwstn, xrwh- (S); NP zurös ‘a loud cry’, xurošidan ‘to shout’; Ghilain 64; Verbum 185; Schaeder, IB I, 254;
Bailey, BSOAS XITI, 1950, 399.
*xšāh [MLK”] the Prth form of šah, to be read HajA:2-4. SPrth: 3.8.11. — The preservation of xš- in Prth is warranted by the following w. which is phonetically written.
xSahridar (Prth) [hštrdr] = Prs šahridar (g. v.), pl. eas. obl. ~-in HajA: 5,
xuftan [hwptn'; HLMWN-tn'] x"afs-, to sleep, to fall asleep 52. 6%. 32%, — Av. (1862) x"ap-, pres. xtafsa-; MPrthPrs xwftn; Paz. x"aftan, pres. avaft-, xtafs-; NP xuftan, xuspidan, pres. xuab-.
```


## [2026-09-06T16:16:45.068Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la incoming/BQT/ && wc -c BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null; echo ---; head -c 800 incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T16:16:45.132Z] TOOL RESULT

```
total 28692
drwxrwxr-x  4 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb     8390 Sep  4 14:06 BQT_v3_pagemap.json
-rw-rw-r--  1 sfmqrb sfmqrb  2499427 Sep  4 14:06 BQT_v3_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb 11053965 Sep  4 14:06 BQT_v3_picofile.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  2055176 Sep  4 14:06 BQT_v4_pages.txt
drwxrwxr-x  2 sfmqrb sfmqrb    20480 Sep  4 12:59 BQT_v4_pages.txt.pages
-rw-rw-r--  1 sfmqrb sfmqrb  8501918 Sep  4 14:06 BQT_v4_picofile.pdf
-rw-rw-r--  1 sfmqrb sfmqrb   723928 Sep  4 14:06 BQT_v5_pages.txt
drwxrwxr-x  2 sfmqrb sfmqrb    12288 Sep  4 13:14 BQT_v5_pages.txt.pages
-rw-rw-r--  1 sfmqrb sfmqrb  4472561 Sep  4 14:06 BQT_v5_picofile.pdf
4339896 BQT_v2_pages.txt
2499427 incoming/BQT/BQT_v3_pages.txt
2055176 incoming/BQT/BQT_v4_pages.txt
8894499 total
---
[pdf page 1]
[NOT OCRED - use tools/ref_page.py]
[pdf page 2]
7
Ub
sits k ge
AS ۱۰۶۲ ‏نتف‌بال‎
‏ومع‎ ‘oo ‏داي و‎ el Oe

far
en rotons ‘ ‘ ths ۰ ‏دیهان‎
‎۳ 2 7
۰ SF Ps
On Awe
۰
‏-ل‎ 9 ‘il
۱۳۴۳ ‏چاپ دوم فروردین‎
‏با تجدید نظر کامل‎
‏بسرمایه کتاپفروشی ابن سینا- تهران‎

|

چاپ افست ر شدیه
[pdf page 3]
اداره ‎“oes‏
‏ساره و6۷ ۲۰۹

pe ۰ ay sf s ‏ار بخ‎
‏سرام ودارت‌شسات‎

د انشمند محتر ,آقای‌د کترحمد معین‌استاد د انشگاه تهران
درپاسخ نامه مورخ ۲۳ اشعارمیدارد :
‎ool‏ حقوق تجد ید طبع کتاب پرهان قاطع با تس
```


## [2026-09-06T16:16:45.517Z] TOOL CALL #21: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-06T16:16:47.879Z] TOOL RESULT

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
```


## [2026-09-06T16:16:52.366Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==202' BQT_v2_pages.txt | head -60"
}
```


### [2026-09-06T16:16:53.895Z] TOOL RESULT

```
  ‫خرش‬                                                                                                 ‫سم پات‬

 ‫و بمعنی شوم ونحس و نامبارك همآمده است‬               ‫جانور کی است که‌هرچه‌برزمین افتدبخوردوبعربی‬
                ‫وابوان وصفه را گنفزتەاند ‪.‬‬          ‫وبن دکه‬
                                                          ‫‪-‬علتی را دگیز‬
                                                                      ‫اورا ارضه خوانند ‪٩‬‏ و‬
 ‫خربدار گیر ‪ -‬کنابه ازچیزی‌است‬                           ‫موی را بریزاند ‪٩‬‏ ‪ -‬و مرضی است کهوشت‬
 ‫آرا‬‫که آ رارواجی باشد وزود فروخته شود و‬              ‫اب وبینی را بتحلیل برد ‪ -‬ویضم‌اول وفتح‌ثالی‬
 ‫بنعارفبقیه‌خوانند وقیضآ اراکاسدہ کو نی ‌‪.‬‬           ‫باتشدید‪ .‬صدا وآوازی باشد که بسبب گلوفشردن‬
 ‫خریدہ ‪ - ۷‬بفتح اولبر وزن درس‬                            ‫م‬
                                                         ‫‪-‬و‬‫اوزخکولوابیدن از یی مردم برآید بض‬
              ‫معروف است که بیع شده باشد ‪-‬‬
                                                    ‫اول و انی و اظهار ها‪ .‬مضفف خروه است که‬
‫و کنیزكد به‬

                ‫لارسیده رایز گویند ‪۲‬‬     ‫ردختسر‬      ‫خروی بائد ‪ - ۴‬و جالوران وحشی را نیز‬
                                                                                   ‫گوشد ‪.‬‬
 ‫ور‌تالی‌وسکون‬
             ‫خر لش ‪ -‬بفتح اول کس‬
                                                    ‫از پنج‬          ‫بکحصه‬        ‫=‬     ‫حرة ار دشر‬
‫است ‪۰‬‬    ‫تحتالی و شن فرشت‪ .‬مخفف‌خنده رش‬

 ‫وآن کی بائد که از روی تمسخر واستهزاء پرو‬            ‫حصهٌ فاری است ‪» ۴‬ونام‌شرری نبیوزده ازبناهای‬
 ‫خنده کنند‪ - ۸‬وخنده‌ای‌رایز کوبن دکه لزروی‬           ‫اردشیر که بهمن من اسفندبار باشد ؛ وباینعنی‬
                                                                                     ‫با تشدید ثالی هم گفتماند ‪۰‬‬
 ‫تمخر وآستهزا‪ :‬وفوی نود ‪ -‬وبائاكك مجهول‬
‫بمعنی خراش باشد که اخزراشیدن است یستی‬                    ‫نی و فاتحلك‬
                                                                   ‫اول‬
                                                                     ‫وما‬
                                                                       ‫خهراث‪ -‬من‬
‫يوست از بدن برداعتن ‪٩‬‏ ‪ -‬وامر باشمعتی حم‬
                                                     ‫و سکون‌کاف » مخفف خروهك است که ممه‌نی‬
 ‫هست بعنی بخراش وپوست ازاندامش بکن ‪٩‬‏ ‪-‬‬                                     ‫مرجان باشد ‪#. ۴‬‬
 ‫وبکراول؛ کدبانو وخانون خانه رااگویشد ‪۶٩-‬‏‬           ‫خری س بکسراول والیبتحتانی کشیده‬
                ‫وضم اول بمعنی پادشاه و‬
‫ربکزه کودخدا باشد‬                                    ‫مخفف خبری است‪ .‬و آن‌کلی باشد زردرنگ‬
               ‫کودیانو را کنفزته‌اند *‪4 .۱‬‬           ‫پربر که‌میان سیاه نورآاهمیشه بهارنیز گوینده ‏‬
                            ‫‪.‬‬   ‫‪:‬آردشی‬       ‫» چش‬   ‫چك‬    ‫(‪)۲‬‬           ‫می ‪.‬‬          ‫‪+‬‬   ‫‪:‬‬   ‫چش‬    ‫(‪)۱‬‬


  ‫« این کورة اردشبر‬   ‫‪۴‬‬           ‫‪.‬‬   ‫خروی‬    ‫رکک‪:‬خروه»‬        ‫‪۴‬‬                 ‫رک‪ :‬خوره ‪.‬‬           ‫‪۱‬‬

   ‫خوره‌منسوست باردشیربن بابك ومبداً بعمارت فیروزآباکدردست‪.‬؟ «فارسنامهٌان‌البلخی‪۲۳۱‬ممد»‪.‬‬
   ‫‪ «۱ ۱‬همجتانك زنساحب‬                   ‫رك ‪ :‬خیری ‪.‬‬           ‫‪۵‬‬            ‫‪.‬‬        ‫؟خ‏رركو‪:‬حك‬
  ‫جمال دربعضی ملابی خوبتر تماید وکنیزك بیش بها در بضی معارض خربدار گیرتر آید ‪> ...‬‬
  ‫‪ ۸‬رك ‪:‬خنده رش‪-.‬‬               ‫‪ - ۲‬اسم‌مفعولاز «خریدن»‪.‬‬                        ‫« المعجم شمس قيس ص ‪.*۱۳۳‬‬
  ‫«‪۲۲‬خر‪:‬یش بعنی پوستش از اندام بناخن بازگیر‪.‎‬‬
                                            ‫‪ - ٩‬اسدی گوبد « لفت فری ‪۲۰‬‬
                                                                                                   ‫خسرو ی کف‪: ‎‬‬
  ‫جهاا بافتی کامت کنون زین بیش مخرمشم‪.* ‎‬‬                ‫جپان برشبه داود است ومن چون اورباکشتم‪.‬‬
  ‫بست دیگری که اسدی از فر دوسی‌آورده (و درآن خرهبشینه آ مده) یداست‬                        ‫و‬   ‫ازین طت‬
        ‫‪ °‬مصحف فخدیش» («‪.‬م‪۲ ).‬‬                      ‫شیدن است ‪ ,‬لفتی درخراشدن ‪.‬‬
                                                                             ‫بر‬‫که مصدر خ‬
                                                           ‫‪.‬‬       ‫‪:‬وره‬
                                                                      ‫* خرة کیالی ‪ -‬رکه خ‬
  ‫طابنعکاربا ‪» ۷۲۲‬‬        ‫د‪0‬ه«ش‪.‬‬
                               ‫ن‪72‬‬
                                 ‫ب‪011‬‬
                                    ‫* خرهدن ‪ -‬فتح اول و چپارم ‪ .‬پهلوی ‪21‬‬
  ‫دیوتکی ‪ ۸۶۱‬از ‪ :‬خری ‪٣‬‏ دن (یسوند مصدری ) ‪ .‬جزو اول درساتسکرت ‪۲K‬‏ ( خریدن )‬
```


## [2026-09-06T16:16:59.732Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'خروس' in p or 'خروه' in p:\n        print(i, 'printed', i+540, p.count('خروس'), p.count('خروه'))\nEOF"
}
```


### [2026-09-06T16:17:01.543Z] TOOL RESULT

```
53 printed 593 1 0
97 printed 637 2 0
126 printed 666 1 0
198 printed 738 3 1
199 printed 739 6 2
200 printed 740 6 7
201 printed 741 0 3
207 printed 747 1 0
243 printed 783 5 2
244 printed 784 2 6
245 printed 785 0 2
256 printed 796 1 0
374 printed 914 1 0
645 printed 1185 1 0
678 printed 1218 1 0
```


## [2026-09-06T16:17:03.634Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==201' BQT_v2_pages.txt | head -70"
}
```


### [2026-09-06T16:17:06.932Z] TOOL RESULT

```
   ‫ره‬      ‫سل‬                                                                                         ‫خروه‬

 ‫فقیرآنرا با خرما بکوبند وبخوردد ؛ بواینمعتی‬         ‫والث مجهول بر‬
                                                                 ‫‪ -‬نم اول ث‬                  ‫خروه‬
‫باتشدید(‪)۲‬ثانی همآمدمو(‪ ۳)۱‬نچه‌از کنجد باشد‬          ‫وزن گروه » بمعنی خروس است که بعربی دبك‬
                                                                 ‫خوالند ‪ -‬وتاج خروس را گیفزته‌اند ‪.‬‬
 ‫و بعربی‬    ‫وآنچه از بيد انجیر نود خرء بدانجر‬
                                                     ‫خرو هك = با ها بروزن خروسك ‪۰‬‬
 ‫کب‌الخروع گوبند ‪ -‬و بفتح اول و ضم الی‬
 ‫و اظهار ها » بمعتی نور باشد مطلفاًاعمازپرتو‬
                                                          ‫بمعنی بسداست که بعربی مرجان گویند ‪. ۴‬‬
 ‫چراغ وآش وآفتاب ؛ وعصنیی باینمعنی ْم اول‬            ‫بضم اول بر وزن گروهه ‪.‬‬               ‫خر و هه‬
 ‫داهج کي و اقا هاکر ا چنانجه گوبند‬                   ‫شپتار میان‌فرج زنان‌باشد‪ - ۴‬وجانوری را‬
                                                     ‫ادان بکرنار دام بندند تا جانوران‬                 ‫ا‬
 ‫برخاق‬     ‫خره نوراست از اند تمالی که قامز مود‬
                                                      ‫‪۸‬‬        ‫عربی‬
                                                                  ‫دیگر فرب خورده در دام افثند و‬
‫رباست بعضی بربعضی کنند‬           ‫خانل ناوریق‬
                                           ‫و بد‬                                              ‫ملواح خوانند ‪.‬‬
 ‫وبعضی بوسیله ان نورفادرشوند برصنعتها وحرفتها‬
 ‫و ازین نور آنچه خاص باند بپادشاهان بز رگ‬            ‫خر و بله‪ -‬با نحتانی مجهول بر وزن‬
‫و عادل )‪(٤‬‏ فایز گردد و آنرا کاخره گویند ‪٤‬‏‬               ‫غربیله )صدا وآواز کربةٌ سیاربلند رگاویند‬
                                                                 ‫وآواز بسیار بلند ورا را نیزگفته‌اند ‪۰‬‬
‫و باینمعنی سم اول وکر انی همبنظر آمده‬
‫؛ و باواو معدوله نیز گفته اند که خوره‬        ‫ات‬      ‫وی خوفای ها ‪.‬‬
                                                                 ‫ثلان‬
                                                                    ‫او‬                    ‫تح‬
                                                                                           ‫خبرفهه‬
‫باشد ® ‪ -‬و بمعنی حصه و بخش هم هست چه‬                 ‫پهلوی‌هم‌چیده شده گروایند ‪ -‬و هجوم وازدحام‬
    ‫مهت‬
      ‫س حص‬
         ‫قپنج‬
            ‫حکمای فرس ملك فاری را به‬                 ‫خلق را نگینزته اند که از جابی (‪ )۱‬بدشواری‬
 ‫کرده‌اند وحرحصه را نامی نهاده اند ‪ :‬اول خرۀ‬         ‫گذرند ‪ -‬ولای آب وشراب رووغن و امثال آن‬
 ‫اردشیر » دویم خر استخر » سیم خرة داراب *‬           ‫باشد ‪ -‬و کل ولای چسبنده ته حوض و جوی را‬
 ‫چپاز) خرة شاپور» پنجم خرة قباد ؛ وباین‌معنی‬        ‫کنفیتزه‌اند ‪ - ۴‬وتفل هرتخمی باشدکهروغن‬
‫هم (ه) با واومعدوله )‪(٩‬‏ آمده است ‪ - ۷‬و نام‬          ‫آا کشیده باشنداعم ازکنجد وغی رکنجدومردم‬
                                                                                           ‫ر‬

           ‫(‪ )۳‬خم‪ :۱‬چه‪.‬‬          ‫(‪ )۲‬چك‪ :‬تشدمد‪.‬‬                ‫»ش‪ :‬جای‪.‬‬
                                                                      ‫(‪ )۱‬خم ‪۱‬چ‪.‬ك چ‬
         ‫(‪ )۵‬چك ‪ ,‬چش‪ - :‬هم‬                ‫(‪ )4‬چك ‪ :‬بز رکه عادل » چس ‪ :‬عادل و مزرگ‬

                                                                             ‫)‪ ۹‬چش‪ + :‬حم ‪۰‬‬

  ‫‪٩‬راد ‪:‬خروس و خود خروه و رك‪ : ‎‬ب«عض فواید لکفتاوبی‌الجماهر یبرونی بقلم‬
                                             ‫‪:‬‬    ‫یادفامهٌالبیرولی > طبعکلکته ص ‪۲‬‬                 ‫کو‬

                ‫شود پر زاغش چو پر خروه‪.‬‬                          ‫س‬    ‫کرود‬   ‫زوز‬   ‫از حملة‬       ‫سب‬
                                                                                                  ‫ش‬


    ‫عنصری‌بلخی‪ « .‬لغت فرس ‪4۹4‬‬
   ‫‪ - ۳‬بیروای درالجماهر ص ‪ ۱-۲‬کوبد ‪ 0:‬وجنس (من‌البد) یسمی خروهك وعرب‬
   ‫از خروه (خروی) ‪+‬‬           ‫‪ ۰...‬بس خروهك هر کت‬     ‫بالغراهك‌وهوتتبیه لاسلالبسد بقلنسوة الديك‬
   ‫در اراک (سلطانب‬        ‫‪۴‬‬         ‫‪.‬‬   ‫» خروسك‬   ‫خروسه‬   ‫‪:‬‬    ‫رک‬     ‫‪۴‬‬              ‫‪.‬‬   ‫کے (یسوندشباهت)‬

                ‫آباد) ‪ 8۲781‬لجن سیاه تهحوض با آب انبار و با جری آب راگوبند ( مکی‌ژاد )‬
                                                                    ‫‪ :‬خوره (فر)‪: ‎‬‬       ‫‪ -‬رک‬     ‫‪e‬‬

                  ‫ا‬           ‫‏‪ e‬خرد‬    ‫ا‬                     ‫‪ +‬جم فزون داشت‪‎‬‬             ‫‪TT‬‬

  ‫زبرهای فاطع هه )‬                                        ‫‪2۱‬‬                       ‫مأخون‬     ‫‪-‬‬   ‫‪۹‬‬
```


## [2026-09-06T16:17:13.432Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==200' BQT_v2_pages.txt | tail -40"
}
```


### [2026-09-06T16:17:15.374Z] TOOL RESULT

```
                                                                                                          ‫‪.‬‬   ‫مردانرا نز گفته‌اند ‪۱‬‬
 ‫ین‬
  ‫شدن شیرخورند ‪ -‬وضم‌اول وفتح‌ثالكث ‪٠‬‏ کسر‬
                                                                       ‫خروس کنگرة عقل ‪ -‬کنابه از‬
                                 ‫‪.‬‬    ‫خروك تی کن گوبند‬                 ‫روح نضانی است ‪ -‬وسخن موزون و موافق را‬

                                 ‫‪0‬‬        ‫بروزن سروش‪.‬‬        ‫‪+‬‬    ‫‪:‬‬   ‫چن‬    ‫(‪ )۲‬چك‬                      ‫‪ :‬آن‪.‬‬      ‫)‪ (۱‬چش‬

                 ‫‪.‬‬   ‫خروهه‬   ‫»‬       ‫خروسك‬   ‫‪:‬‬   ‫رك‬      ‫‪۴‬‬                    ‫‪.‬‬       ‫خروهه‬   ‫‪.‬‬   ‫خروسه‬       ‫‪:‬‬   ‫رك‬   ‫‪- $‬‬

 ‫‪ - ۴‬از مصدر اوستابی ‪( 502۲8‬خروشدن ) ‪ .‬هندی باستان ‪( 2-150161-‬هلهله)‪, .‬‬
                 ‫سانسکریت ‪ « 48-15۵۲‬اسفا ‪ : ۱‬ص‪ ۷۸‬و ‪ » 44۱‬ورك ‪ :‬اسذق و هوشمان ‪. ۱۸4‬‬
                          ‫‪«- ۴‬خروش؛ بانك باشد باکرستن وبی گرستن ‪ .‬شهید (بلخی) کفت ‪:‬‬
 ‫>‪.‬‬      ‫‪۱۲۲‬‬   ‫فری‬       ‫« لفت‬        ‫>‬   ‫ندود باده بر سرودش نوش‪.‬‬                       ‫چند بردارد این هربوه خروش‬
     ‫پهلوی ‪« 50۲‬بودکر ‪۹۱۱٩‬‏ ازريشة اوستابی ‪« 50211‬اسفا ‪۲ :۱‬ص ‪۷۸۳۰‬‬                                                 ‫خروس ‏‬
     ‫=‬    ‫خروج‬       ‫=‬   ‫فارسی ‪ ۷‬خرده‬            ‫) =‬    ‫لفه بمعتی خروشنده (بمناسبت بانگوی‬                           ‫خروشدن؛‬       ‫معتی‬

                                                     ‫خواناری‌نز ‪50۲‬؛‬          ‫‪ ۲:‬ص‪۳۲۱۰‬‬             ‫خروز» بلوچی ‪sêrk‬‏ اغا‬
                                                     ‫کیلکی ‪ ۰. 5۱۲01‬فریز ندی ‪ » 50۲21‬برنی ‪ 850۲41‬؛نطنزی‬
                                                     ‫‏‪۱ . 4» XOrÛS‬ص ‪ ۷۸۲‬سمنانی ‪۲ .3 « 5۷۲0۱ « 3۵1۲۵8‬‬


                                                     ‫نام ازابران بزبانهای اسلاو رسده | »نرینهٌ ماکبان ‪ .‬رك ف‪:‬اب‪۱‬‬
                     ‫خروی‬                                                  ‫اسلام (دیك) ‪۰‬‬          ‫ففعث ‪ ۰‬دائرءاامعارف‬            ‫‪۵۳‬‬   ‫ص‬

 ‫‪۳‬‬       ‫يدن (یسوندمصدری)‬              ‫(«‪.‬م‪4 ).‬‬        ‫‪ ¥‬خر و شیدان ت صم اول وفتح ششم ‪ /‬از ‪ 2‬خروش‬

                                                                                  ‫‪۰‬‬    ‫‪a‬‏ فرباد کردن باناله وزاری‬            ‫باقڭ زدن‬




                                                                                                                    ‫بقبه ازصفحةً ‪۰۷‬‬
      ‫طبع اوخروار هت و صورتش خروار لیست‪.‬‬                                   ‫نیست مردم ناصبی‌تزديكك من » لایل خراست‬
     ‫«داصر خرو بلخی‪.*۷ ۸‬‬
                                                 ‫‪.‬‬      ‫‪:‬ب‬
                                                         ‫ئكو‬
                                                           ‫خددر» ر‬
                                                                 ‫‪ ۵4‬خروب ‪ -‬بفتح اول و دوم مش‬
```


## [2026-09-06T16:17:44.868Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i,p in enumerate(pages):\n    if 'کرکس' in p:\n        print('pdfpage~',i+1,'printed~',i+1+1205)\nEOF"
}
```


## [2026-09-06T16:17:45.868Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'کروه' in p:\n        print('pdfpage~',i+1,'printed~',i+1+1205, p.count('کروه'))\nEOF"
}
```


### [2026-09-06T16:17:46.673Z] TOOL RESULT

```
721
pdfpage~ 415 printed~ 1620
pdfpage~ 417 printed~ 1622
```


### [2026-09-06T16:17:48.506Z] TOOL RESULT

```
pdfpage~ 20 printed~ 1225 1
pdfpage~ 47 printed~ 1252 1
pdfpage~ 103 printed~ 1308 1
pdfpage~ 129 printed~ 1334 1
pdfpage~ 150 printed~ 1355 1
pdfpage~ 192 printed~ 1397 2
pdfpage~ 207 printed~ 1412 1
pdfpage~ 253 printed~ 1458 1
pdfpage~ 348 printed~ 1553 1
pdfpage~ 382 printed~ 1587 1
pdfpage~ 406 printed~ 1611 1
pdfpage~ 411 printed~ 1616 1
pdfpage~ 414 printed~ 1619 1
pdfpage~ 416 printed~ 1621 1
pdfpage~ 422 printed~ 1627 2
pdfpage~ 423 printed~ 1628 2
pdfpage~ 424 printed~ 1629 1
pdfpage~ 485 printed~ 1690 1
pdfpage~ 515 printed~ 1720 1
pdfpage~ 526 printed~ 1731 1
pdfpage~ 530 printed~ 1735 1
pdfpage~ 563 printed~ 1768 1
pdfpage~ 600 printed~ 1805 1
pdfpage~ 630 printed~ 1835 1
```


## [2026-09-06T16:17:53.991Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (414,415,416,417,418):\n    print('======== pdf page',i+1)\n    print(pages[i][:2500])\nEOF"
}
```


### [2026-09-06T16:17:55.716Z] TOOL RESULT

```
======== pdf page 415
[pdf page 415]
کرکاس

از مضافات بت‌المقدی - و ‎Ob‏ بخارا سقف
خانه زا گویند و بفتح اول وسکون ثانی» مرغ
خانگی وما کیان باشد ‏ - و کيك ‎what pal)‏
‎ol,‏ دو ‎Gp : athe ed‏ و ‎pe‏ دری ۰ در
بزرکتر وغیر دری کوچکتر- وسرطان‌وخرچنگه
را نیز گویند ۴ - و بمعنی مردم چشم هم بنظر
آمده است - و شاخ درخت را ‎a G‏ -
‎GEL,‏ فارسی درخ ک ‎USS‏ ۴ وآن
جانوری است ممروف‌درهندوستان شبیه بگاومیش
‎darn»‏ شاخی دارد . گویند اکی زهر او
را (۱) ختك ساخته بخور کنند باد بمیاری بی
اختیار از مردم رها شود - و بضم اول وفتح دویم
سربیموی را گویند که از کچلی‌شده باشدو کچل
‎eb‏ گفته‌اند - ویضم اول وسکون‌نانی‌ما کیانیرا
‎TT‏ از بیذه کردن باز آهده و هنت شده
باشد ۴ - و چشم نرمیرا گویند ۵ که ازبن‌موی
بز بروید و آنرا بثانه بر آورده برسند و شال
وامثال آن بافند و ازآن تکیه و(۲) لمد و ‎OWS‏
‏و کپنك و مانندآنهم بمالند .

کر کاس » با کاف بروزن المای ؛تخم

. ۱ -۱۷۷.-
کیاهی است که آنرا دو سر گویند و در میان
زراعت کندم (۳) و جو زوید ۱ . گرم و :خشك
است در اول و دویم و محلل ورم خنازیر باشد
وشلم همان است .
گر گام = بر وزن سرسام » بمعنی قوت
وتوانابی و مراد و مقصد باشد .
کر گدن ۲ = ‎ce‏ اول و ‎BE‏ فارسی

و دال ‎aml‏ (4) پروزن نسترن » جباتوری باشد

شبیه بگاومیش و برسربینی شاخی دارد. گویند
‎OT Se‏ در شکم مادر پنج سال می‌ماند و بعداز
یکال سربرمی‌آورد و علف میخوردوچرامیکند
و ‎me‏ طریق تا چهار سال بعد از ‎OT‏ برمیاید
و میگریزد ؛ و حکمت درین ‎OT‏ است که زبان
مادر او ‎ghar‏ درشت است و بچه درنهایت تزا کت»
‎ob‏ لیسیدن مادر ندارد و پوستش ‎ob‏ میشود ؛
وبعی ‎clea OS SaaS‏ که‌پیل ‎Las‏
‏را شکارکند ؛ و بعضی ‎Las‏ گفته‌اند که‌جانوری
است بضایت )0( بز رکه و فیل شکار و بر پشت
او خارها باشد مانشد ستونی وهرفیلی راکه شکار
کند برپشت خود اندازد ‎)٩(‏ و بجهت بچپای

(۱) چش ‎VT:‏ 0) خم ۱:- و (۳) خم ۱: -کندم .
(4) چش:- ودال ابجد . . (0) چش : بسیار. . («) چك » چش : خود دارد .

۱ - ور اوتا -۵2۳68 ( ‎]kabrkasa_ us,‏ کرکس [( درپپلوی ۷۵۲۷
( مرغ خانگی ) , ‎wae‏ بامتان -۷81] 712 ( خروی ) . کردی ‎kurk‏ ( مرغ ‎ASG‏
‏افتاني ‎cirg‏ ۰ استی ‎kark‏ ( ماکیان ) » وخی ۰6۵« اسشق ۸:۸ » ورك : هوبشمان ‎AEA‏
‏۴ - قس :کردی ‎kerkinj‏ (خرچنک ) « ژابا ۳۷۲۹ ۰ و رك : خرچنگ .

۴ ره :ک رگدن .
خروسی‌عمه‌اهل فضل‌است‌وهت
‎SS‏ فاضلان ‎USL‏ ک رکه

۴ - قس :کرج ( بضم اول ) .کپ ( بضم اول ):

‎aul ey‏ تاجدار از نژاد

‏نبارند در پیش او خابه داد .

‏سوزنی سمرقندی > فرهنگه ‎les‏ >
‎٩‏ - رك : رشیدی .

‏۵ آمروزء هم کگویند = کلك «رتیدی > .
۷ - فارسی ‎OT‏ «ک رگه » و «ک رکدن » و «کرکندن » ( لفت قرس ص 8*۱ ) » در
عربی «ک رکدن > ( با هردوکاف و بتشدید دال و تخفیف نون و نیز بتخفیف دال وتشدید ‎Cog‏
‏ا کدی ‎kurkizannu‏ , سربانی 1813080 « نسیمرن. ‎old‏ دخلةًا کدی ص۵۱». کر گدن
‎thinocéros)‏ [فر ] ( 
======== pdf page 416
[pdf page 416]
ioe bh eed

خود آورد . گویند چون فوت او نزديك شود .
فیلی بر پشت او باشد
و فراموش کند تا آن
فیل بگنده و کرم در
آن ‎sl‏ و چون فیل
تمام شود ‎OLS‏ سر ک رکدن
بجان او گذارند و او را شروع در خوردن

کنند هم ‎cole Olay‏ بمیرد ؛ و بعضی گونند
‎Ls‏ آبی است الاعلم . و معرب ‎SOT‏ کزن ۱
باشد یم ‎GE‏ اول وفتح‌کاف دویم وزای نقطه‌دار
مشدد .
ک رکر - بفتح دو کاف و سکون دوراء
یکی ازنامهای خدای‌تعالی است جل‌جلاله ۴ -
و بمعتی‌کامکار هم آمده است که پادشاه صاحب
اقبال باشد - و درخت‌کاج را نیز گویند و بعریی
صنوبر خوانند ۴ - و بکر هردوکاف نوغی از
باقلا ‎ath‏ و معرب آن جرجر(۱) است؛ و باین
‎om‏ با کاف فارسی هم هت .

کر کر افلك - بر وزن بهلوانك ؛

استخوان نرمی باشد که آنرا بمربی ‎Saree‏
‏خوانند ۴ .

(۱) چش : جیرجیر .

۵۸۳ ‏مصحف «ک رکدن» ابت . رل : چك ص‎ ٩

. ‏کرو کر‎ SS inf

. ow) kurkizannu

ک رکز
کر کر لگ - ‎shai gb Koi,‏

است دم دراز که در کنار های آب نشیند و دم

جنباند و بعربی صموه خوانند ‎٩‏ ؛ و عکه را هم
کفته‌اند؛ ویعضی ‎LS‏ را گویشد که‌سلوی‌وبلدرچین
‎Vast‏ .

کر کروهن © بفتح ‎wily ely Jol‏
بواو رسیده و های ر بنون زده » معجونی
باشد از ‎SLT‏ شکافته و فلنجه و بسباسه و صندل
مقاصری وسئبل‌الطیب و ماژو و عل . قوت دل
دهد وقبضآ ورد ۰

ک رکرهن ۷ - بنیردند رکه
وسکون نون » بلفت بربری دوائی است که‌آنرا
عاقرقرحا خوانند و آن بیخ طرخون رومی‌است.

کر کری * ه بفتح اول و الث بروزن
مرسری » استخوان نرمیرا گوبند که آنرا توان
خاییدن مانند استخوان سرشانه وغیره که سربی
‎Gy pe‏ خوانند ؛ وم اول و ثالث هم‌پنظ رآمده

ک رکز ‘ = بفتح اول و ضمثالت‌وسکون
ثانی و زای نقطه‌دار + بمعنی علامت راه و دلیل
وراهبر باشد *۱.

ح. اما چثانکه کفته شد دراکدی

۴ - (عر) بفتح دوکاف » نوعی از ‎SU SEE‏ آنرا «قمل‌فریش گونند. « دزی ‎Ye‏
‏ص ۲:4۵۸ > . بقول مایرهوف کر کر ( یکسر دوکای (عی) = ‎pin‏ « عقار ۳۱۷ ف >

۴ رك: جهانگیری » رشیدی  ‎ESS‏ رشیدی » رل : ک رکری .

© -قین : طری ۷6۲6۳8 ( سبزفبا ) > واژه‌نامه ۵44 > وركث: ک رکما:

خجته را بجز از خردما نداردکوی

. ‏رل دک رکه‎ - ٩

بنفشه را بجز از کر کر کث ندارد پای.
ناصرخسرو بلخی > رشیدی :خردما».

۲ .> عافرقرحا . هوالکر کرهان + وبقالالقرقرهان » «عقار

‎pyréthre ۰۹‏ (فی). ۱0۲۱۵۶۵۵۴ لغت سربانی است * عقار ‎Anthemis = «sya4‏

‎> ۲:4۵۸ ‏دزی ج۷ ص‎ « Pyrethrum
. ‏ک رکوز‎ « ٩

‎(pa) LS ‏سک‎ ۸

‏*- ور زحیوان به پیشت‌آید بز هست آنهم بتفرقه ک رکز . آذری‌طوسی ‎ASAP‏

======== pdf page 417
[pdf page 417]
کرکس ‎Sen OT ta‏
کر کس ت رکش - بکر رابع .

تبررهاییرا گویشد که در تر کش گذارند , چه
کر کس بمعنی تیر هم آمده است.

مردار خوار

باشدوبعربی ,
ن ‎Mb TF: my‏ - شرا ۴ را کونند

و کنابه از و ‎oT‏ ستاره‌ایمت از ثوابت .

‎ws cael‏ با فا بروزن رستخیز؛ بمعنی
که عربان کفگیر باشد وآن چمچه‌است سوراخ دار؟ .

‏سهم خوانند

‏کر کم ‎LAR‏ بر وزن مرعم ‎ves‏
‏فرحرا کوبند ۵ - و ‎gins‏ زعفران هم آمنده
است ۷ - و بعضی کویند بیخ وری است و آن
کیاهی باشد مانند کیاء کنجد .

‏کر که ۷ -بامي بروزنمرجبا.پرنده‌ای

‏امت دم دراز که بعربی صموه گویند .

‎AS ‏بنماوذبروزن‌تر‎ = MOLT ‏کر‎

‏دوائی است که آنرا حندقوقی خوانند ویفارسی
انده قوقو خوانند. برکلف مالند نافع باشد.

‏کر گمیسه - ‎te‏ اول و الت و میم

‏بتحتانی کشیده و سین ‎Mais‏ مفتوح ۰ تام ‎AS‏

‎SS‏ أ۱
کر گسار ۴ با ‎GB‏ فارسی بروژن

‎as‏ ؛ نام ولایتی است - و نام پهلوانی حم
بوده توراتی و بهمن‌ین اسفندبار او را دستگیر
کرده و او بپمن را فریب داد ازراه هفت خوان
که بی آپ وعلف بود برویینه دز برد » بیمن در
نب ‎eas‏ او را ‎dear‏ آورد.

‏کر کسان ‎ll - US‏ به دنر ‎pe‏
‎ale:‏ است که‌دوصورتند اجملة ‎Aye‏ وهشت

‏صورت فلك البروج .

‏۱ = 0 اوستا - 2۳۳858 (کرکس) . پهلوی ۷۵1۳۵5 , ‎kargas‏ .
افتانی ع 88۲885 ‎ol.‏ 62۲822 » استی 4۳885 « استق ۸4۹ ۲ ‎Ue‏ اوستایی ه رکب
از دو جزء است : ۷۵366۵ )= ‎eS‏ . مرغ )۳ 252 (خورنده) » جمعاً بمنی مرغ‌خوار
« هرمزدنامه ۱ ‎TT‏ ( لاشخور ) برنده است شکاری . بزر که وسنگین » باگردنی دراز.
خوراکث وی از اجساد جانورانست . ۴ ب صحیح ‎LSS‏ بضم اول است . رك:فهرست
ولف . ۴ - منظور ‎Bye‏ « شعری ۰ ‎Sirius‏ است » ولي ظ . مراد از «ک رکس فلك +
همان نس طاین است .

‎. ‏چشمش باشد از چتم ک رکفیز فرونتر‎ Ue ‏دارم چنانکه‎ wt - F

‏سوزنی سمرقندی «جهانگیری».

‏© _ فلك مرجامه‌ای را ماند ازرق مر اورا چون طرازی خوب ک رکم .

‏بپرامی سرخی « لفت فری ‎٩۳۵۶‏ ۰

‏۱( عر ) « ک رکم بالنم . زعفران ومصطکی * « منتهی‌الارب > . ک رکم (عر) <
۵ (فر) , ‎chélidoine‏ (فر). نام کر کم سامی‌است : آشوری 7 108۷80 » عبری
‎karkom‏ آرامی ۲0۲۷6۲۵ . اين ‎oe lea‏ زعنران ‎«e+! (crocus sativa)‏ ولی
بعدها ‎paw‏ دارویی ‎long cae‏ 6۱۲61۲02 با زعفران هندی کرفته شده . رك: عقار ۲۰۵ف.
۲ -قس ‎A ASS:‏ « حندقوقی . هوالنفل و الذرق والحابور و العرقصان » و بقال له
‎Le!‏ حباقا . وهوالکر کمان » واسمه بعجمیةالاندل‌طریله » « عقار ۱۶۷ » ورگ : ‎Gal‏ ۱2۷ ف .

======== pdf page 418
[pdf page 418]
‎Ve‏ کرمائیل

‏پرادر شلفم را گویند ۴ - و در عربی ‎we‏
‏جوانمردی وهمت باشد - و بسکون ثانی‌سبزه‌ای
راگوبند که برلبهای جوی آب رسته باشد؛ وحر
چیز را نیز کوبند از درخت و بوته و ‎Seal‏ آن

‏است خوشبوی که چند رنگه میشود و ببشتر در
کوه الوند میباشد .

‏کر کن - بفتح اول و الث بروزن‌ارزن»
دلمل ‎aS‏ پم کندم وجو ونخود ‎Wks‏
‏که نیمری شده باشد و همچنان با شاخ وب رکه
بربان کنند و خورند ؛ و بطم ‎SE‏ و کسر الث
هم گفته‌اند | و باکاف فارسی نیز آمده است .
ک رکود ۷ با کاف بروزن سردوز +

‎. ‏و دلیل وراهبر باشد‎ oly ‏علاعت‎ gine

‏کرکی ۴ - منم اول و سکون نانی
وئاك بتحتانی رسسده»
پرنده است که آنرا

‏که از کنار جوی آب روید - و درعربی درخت
انگور را خوانند - و بضم اول و سکون ‎BU‏
‏بمعنی‌غم واندوه و گرفتگی دل باشد 9 -ویمعنی
زخم وجراحت هم آمده است! 2
کرماسیس ۲ ۰ با در سین بی نقطه
بروزن مقتاطیس , بیونان ی گوشت سرخیرا گونند
که د: اندرون چشم آدمی پیدا شود .۴
کرمان شهان ۰ با شدن نقطه‌دار

‏و هه بروژن بربان پزان» نام شهری‌ومدنه‌ارست.

‏کلنك‌خوانند ۳ . اگر 5
مغز سر ‎CL‏ را در - ‎Bas‏ بروزن ‎Whe‏ ؛ تامییکی
چشم کشند شبکوریرا از آن دوپادشاه زاده باشد که مطبخی ضحال‌بودند
1 5 کی را بری مقر سراو میکشند
برد يك کس را آزاد میکردند و بجای آن‌يك کس

‏کر ‎Jie‏ هغز سر کوسفند داخل منمودند بجپت آزاری

‎ly‏ وسکون میم؛ کلم کرکی که ضحاک ‎ctl‏ و گوبند کردان از آن

‏۰ < کر کز(هم). ۳ - )4( کر کی, کثر کی [ب‌اولوتشدیدآخر ] کلنگه.
کراکی‌جمم.»منتهی‌الارب» ورك:بحرالجواهر. ‏ گرلك: کلنکه. . * ** کلم(هيم.)درین‌یت‌بابهام:
در رو زکار یچ ‎ols‏ دیدی از کرم جز در ‎Oke‏ سبزه اطراف بوستان .
اثیر اخسیکتی«فرهنگه‌نظام». ‏ ۵ -صحیح* گرم»است. رك:لفت‌فری*ع .۳‏ ۷-(عی)رك:منتهی‌الارب.

‏۷ - دزی ‎Ever) aS‏ ): چنانکه کوبند یونانی‌است. رك:فولری.6080[00601۷6,
غشاء مخاط یکه ‎Bae‏ چشم را ‎UCL‏ متصل‌سازد . ‎A‏ < کرمانتاهان, ناحیتی‌است‌درمفرب
‎ol!‏ . از شمال محدود بکوههایی که ‎ge We‏ رود دباله و گاماسب میباشد و آزمشرق‌بکوههای
کنکاور و از جنوب بکرههای کلهر و از عقرب بخا که عراق , و تفیمات حکومتی آن ساب
ازینقرار ‎LL SN: oy‏ وحومه ۲ سنقر وکیائی ۳- ‎Ole‏ دربند و بالا دربند و زیر دربند
۶- دینور و کنگاور ‎-٩‏ ماهیدشت وهارونآ باد و فیروزآ باد ۷ سحنه ۸-کرند 4- زهاب
رقصر *۱- هرسین ۶ کیپان . جفرافیای سیاسی ص ۵۷-4۵۱ » ‎Ay‏ : کرمانشاه . (س2۱۹۲۹).

‏۵ کرم - ‎JG‏ پهلوی ‎karm‏ . سانکریت ‎krimi_‏ (کرم ). کردیا ۷0لا
استی ‎kalm‏ (مار ) . ‎kaélmita‏ (کرمها ) . بلوچی ع ‎kirm‏ > اسشق - هوبشمان ۸۵۰ ۰
کیلکی 18100 ؛ کرمها جانورانی هستند غیر ذی‌فقار که عموماً بدن دراز و ترم دارند و بدون پا
هتند , و آنها راب‌دسته : کرمهای خلقوی . کرمهای پپن و کرمهای کرد تقیم میکنند .

‎o‏ کرهان - بکراول . نضت بناحیتی اطلاق میشود که از شما محدود است‌بخراسان

‏بقیه درحاية
======== pdf page 419
[pdf page 419]
TNA

-
کرم دشتی ه بفتح اول» رستنیی‌باشد
صحرائی وبفایت بلند مشود ومانند عشقه‌ولبلاب

کرم بادامه
جمای‌اند ۷ .

کرم باداهه = بکس ال و میم ۰
کرم قز را گوبند که کرم ابررشم باشد یعنی نخم
ابریشم چه بادامه ‎aby‏ را گوبند که ابریشم‌ازآن
بهم هیرسد .

گرم دا ۴ ‎Ge‏ اول . تخم‌نوعی
از مازربون است که آنرا بضارسی هفت برله
خوانند و موردانه نیز گوبند و معرب آن جرم
دانق باشد .

بردرختها می پیچد وخوشهة. ميوة ‎OT‏ زباده برده
دانه نمیشود وآنرا بعربی کرمةالیضا ۴ خوانند.

‎SG © the‏ اول وفتح ‎ME‏ بروزن
خشتك, صغیر کرم است - واشنان را نز گوشد
که بدان رخت شوبند - و لفز و چیستانرا هم
کنته‌اند ۴ - ویفتح اول‌درمژیدالفضلابمعنی‌طعامی
باشد که از باقلا پزند .

‎: ‏)آرد‎ ۳۵ wie ‏رك : ارمائیل . فردوسی طوسی ( شاهنامةٌ بخ‎ ٩

‏دو پاکیزه از کثور ‎Lot‏
‏یکی امش ارمایل پا کدین
برفتند و خوالیگریاختند
ازان‌دو(مرد)یکیرابیرداختند
برون کرد مغز سر گومیند
یکی را بجان‌داد زنهار و گفت

‏دو مرد کرانماية پارسا
دک نام کرمایل پیش بین...
خورشها باندازه پرداختند ...
جز این چاره‌ای نیز نشناختند
برآمیخت با مغز ‎OT‏ ارجمند
‎SG‏ تا ‎Ble‏ سراندرنهفت...

‏خورشگر بربشان‌بز ی چندومیش بدادی و صحرا نهادیش پیش
کنون کرد ازان‌تخمه داردنژاد کزآباد ‎wk‏ بدل برش‌باد...»

‏۴ - درین‌کلمه دولفت است : کرمدانه (عر) ۶ کردمانه ‎(Ge)‏ ۳ کردمانه ( بکسر اود )
فارسی [ که معرب آن جردمانق است ] -کرمدانه ( حب حار ) فارسی [ که معرب‌آن جرمدانق
است ] و آن بقول دزی ‎ol Fruit du garou ou Daphne‏ « دزی ج ۷ ص ‎tof‏ و
‎Gnidium‏ موی ۴ ‎couleuvrée=‏ با ‎bryone‏ ء هزار ‎ole‏ « دزی ج ۲
۴ - ظ. مسحف ‎oy?‏ = بردك » رك : کردك .

‎9

‏ص ۵۹ .

‏بقیه از ‎baie ele‏ ۱۹۲۵
و از مشرق ‎Lok,‏ سرحدی ( بلوچمتان ) و ازمغرب بیزد و فارس و از جنوب بمکران . مساحت
‎oT‏ ۲۲۰۰۰۰ کیلومترمربع است ( رلد: جفرافیای سیاسی . کیهان ص ۲46 ببس ) ۰ اکنون آنرا
استان هشتم مینامند. دوم » پایتخت این ناحیه راگویندکه بطول ‎OV‏ درجه و ‎EBVO‏ وعرض۳۰
درجه و ۲۶ ‎ids‏ و ارتفاع ۱۸۹۴ متراست » مقر است‌اندار است و دارای ۵۳۹۵۸ سکنه است
« راهنمای ابرآن .55 & متادارش ص۱۹۸ *.

‎Saker ‏کرمالشاه - بکراول ؛ ممرب آن « قرمسن *. شهرست در استان پنجم‎ oO
‏مقر استاندار » دارای‎ » ta ۱۱4۰ ‏درجه و*۱ دقبقه و عرض ۳4 درجه و*۲ دقبقه و ارتفاع‎ ۷
‏ستاد ارتش ص۲۰۰».‎ Ly. ‏هسکنه « راهنمای ابران‎ ۲

‏( برهان قاطع ‎(eA‏
```


## [2026-09-06T16:18:15.246Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (349,350,351,352):\n    print('======== pdf page',i+1,' printed~',i+1+1917)\n    print(pages[i][:1800])\nEOF"
}
```


### [2026-09-06T16:18:17.345Z] TOOL RESULT

```
======== pdf page 350  printed~ 2267
[pdf page 350]
-۹۷- وردان
ورخج! « بنتم آولونانی‌وسکون خای ورد - بکر اول و سکون ثابی و دال
نقطه‌دار وجیم . زشت وزبون وپلید وکریه‌منظ | ابجد. بمعتی شاکرد ومرید باشد - ودرعربی کاز
راکویند؟ ؛ وبا چیم فارسی‌هم آمده است .8 هرروزی ودایمی وبسویآب آبندگان وتشنگان
ورخچی؟ < بر وزن پلشتی » بمعنی | ولوبت آب دادن شترراکوبند؟ .
زشتی وزبونی وپلیدی باشد . وردان- بکر اول و با داد
* فرخچ (۸.م.) «رشیدی» « فرهنکه نظام» ** فرخج (۸.م.) ورك : فرخجی .
۴ - پیش دلشان سپهن وانجم این بوده ورخج و آن تخجم. خاقانی‌شروالی«رشیدی».
نامم همای دولت وشهبازنسرت است نی کر کس ورخج ونه زاغ تخجم است.
۰ خاقالی ۸« رشیدی >.

۴ - از : ورخچ (۸.م.) ی ( حاصل مصدر » اسم معتی ) * فرخجی (*م.)

۴ - (عر) « ورد بالفتح, گل هردرخت و غالب کل سرخ را گویند » وردة یکی - و اسب
کلگون یعنی مایین کمیت واشقر ؛ وردة موّث » ورد بالضم.و وراد ککتاب و اوراد جمع - ومرد
دلیر- وزعفران - وشیربيشه » « هنتهی‌الارب » راجع بربشةٌ *ورد» ( کل سرخ ) رك : گل. « ورد
بالکس تب » اسم است‌آنرا با نوت تب - و پاره‌ای از خواندنی از قرآن و جزآن ...- و لوبت
آب - و بهره آزآب - وکلةٌ مرغان - وبرآب آیند کان از مردم و شتر - وکروعی از لشکر. >
۰ منتهی‌الارب >.
دبالهٌ حاغبهٌ صفحهٌ قبل

0 ورجاو لد - بفتح اول وسوم وپنجم, پهلوی ۷8۲02/280 ۵ بوستی . لام نامه ص
۹ اوستایی ۷8۳90810۷881 ( نیرومند » قوی) « بارتولمه ۱۳۹۷ ؛ لغة یعنی بلند پایه
وبرازنده و ارجمند , ومجازاً بمعنی ورجمند (۸.م.) ودارای فرهة ایزدی . این صفت بارها در اوستا
برای ماه وتیشتر و کلام ایزدی وفر کیانی‌آمده است « پورداود . سوشیاس من ۳۸- ۳۹ > و رك :
پارتولمه ۰.۱۳۹۷ یکی از معتقدات مزدسنان آست که پس ازسپری شدن روزگار پادشاهی کی
کفتاسب » دیگر فر بکسی تعملق نگرفت . اما آهورمزدا آنرا تا دامنةٌ رستاخیز برای ابرایان
نگاهدارد وسوشیانت 8081081 ( موعود زرتشتی ) از فرایزدی برخوردار شود. وا زکناردرباچه
هامون برخیزد » وکیتی را از راستی وعدلآباد کند. یکی ازوقایع ظهور هوشیدر (لنشتینموعود)
بسرکارآمدن پادشاهی‌است ازنژاد کیانیان . 
======== pdf page 351  printed~ 2268
[pdf page 351]
ورد <<
اد بروزن کرمان» دانپای سخت را کوبن د که وجهاز عروس را لیز گفته اند .
ازاصنای آدمی برمیآید وبمربی‌تژلول‌میگویند۱- ورد و که - بنتح اول و کاف آخر,
و بممنی شاگردان و مربدان هم هس ت که جمم | بمهنی اول وردوك است که خانهٌ علفی باشد .
شاکرد ومربد باشد چه وردبمعنی‌شا گرد ومرید ورده۷ - ,نتم اول ونالت , مطلق‌برج
ات . را کوبند عموماً وبرج کیوتررا خصوصاً -
وردله؟ - بفتح اول بی وزن زد , وردیج۸ - باجیم ابجد بروزنسرییچ.
جهاز عروس را کوبند بعنی اسبایی که بااویخانهٌ | بممنی ورتیچ است که پرندة كوچك تن از تبهو
خوهر برلد ۰ باشد که عربان‌سلوی وترکان بلدرچین میگوبند.
ور دنه۴ - بنتح اول وثاك‌ونون,چویی ورز* - بنتح اول وسکون ثالی وزای
باشد هردوسی باريك ومیان کنده که خمین تانر! | نقطه دار . بمعتی حاصل کردن باشد - وکشت
بدان پهن سازند - وچویی‌را نیز کویندکهچرخ | و زراعت را نی زکوبند *۱- وهر صنمت وحرفت
برآن گردد وبعرپی محور خوانند . وکار باشد عموماً۱۹- و ستمت دیاغت را کوبند
وردوك - بر وزن مفلوك, خانه‌ای‌را | خصوصاً - ونام رودخانه ماوراء النهرهم خست۰0۳
کوبند که باچوب و علف پوشیده باشند ۴ - | وماوراء‌التهررا نیز کوبند۱۴- وبمعنی پیاپی‌کاری
۱ - وردان (بالکروفتح دالمپمله) رخ باشد که بهندی مه کوبند.» « رشیدی » ورك:
اجین‌آرا - ۴ <وردو3 (همم.) ۳ واردن (ه.م.) و رك : رشیدی . گلپایگالی
42 ( چوبی که باآن خمیر را صاف کنند و بشکل استوانه درآورند) « قاسمی >.
۴ ورد وکه (ء.م.) که بهندی چهپر کوبند « رشیدی >. ۵ «وردك (هم.)
-* ورد (ه.م.) ۷ - « ورده » چوب کبوتر بازان باشد که کبوتر براند
( پراشد . دحخدا ). منجيك (ترمذی) کوید :
چون مرخش از هوا بسوی ورده از معده باز تاوه شود نات . >
لغت فری ی ۸۷۶ *-
۸ ورتیج («.م.) * وردج * ورتك » هندی باستان ۷۵۲۸18 ( بلدرچین )» پپلوی
6۴ پونانی 0۳105 ۰ کردی ]۷۵۲۵ ۰ 82۷87۵6 ( بلدرچین ) . اقغانی 8۷8782 ۰
استی ع(1) ۰۷2۲063 بلوچی 8۷27028 (كبك کوهی) » وخی ۷010 « اسشق ۱۰۷۸ ور :
زاباص 4۳۰ . طبری ۷8۳48 ( مرغی است در مازندران معروف و بدیلم آرا « وشم » جم واو
وشین معجمه ومیم ؛ و
======== pdf page 352  printed~ 2269
[pdf page 352]
-۲۲۹۹- ورزش
کردن هم آمده ات » وبعربی ادمان خوانند- | وماوراءالنهر را نیز گفته‌اند که ترکستان باشد .
و مرز را نی زگفته اند ۱ و آن زمینی باش دکه ورزش ‎٩‏ - بروزن لرزش, بممنی ملکه
چهار طرف آنرا ساخته باشند
و در میان آن چیزی بکارند - و مک
وفاعل ۴ ورزیدن باشد همچو هم رن هی ی س و ی یت
آب ور ز که شناکننده است - 2 سب موه نس خی وی ی
وامرباین معنی‌هم هست۴ . َ بویت وه

زاو۴ . ۴ شاه
ورر او" - بر وزن ۰ چا ی
7ب 13 ۰ 1
برع کوب کرش که سک که
زمی‌را بدان شیا رکنند » یعنی و ربصووو با کصن ۳
کاو زراعت . وی 2 زاو
ورزرود؟* «بارای ‏ # ی
قرشت ودال بروزن ؛گرصود »
رودغانهٌ ماوراء‌النپررا گوبند - ورزاو
۱ مسحف «مرز» (م.) سراح‌اللغات بنقل فرهنك نظام ج ۵ ص‌مب .
۴ - اسم فاعل مرخم : کشاورز » آب‌ورز ,کارورز :
یکی کارورز و دکر گرزدار سزاوار هر کی پدبدست کار.
قردوسی طوسی « شاهنامة بخ‌جاص*6۹.
: ۹ زا ۳ 0 لك ۳ : 1
8 ۹ سس کی یا
۸ 7 :ِا #11 4ب ۳ :۹ ۳ ,کته ۱ ۲
| کی وید تن تن پی موی 3 س
اک ۱ : 1 ید 78 و
۸4 ۳ دای چاه" 3 وه وان
کم ۷/۱ و هام کیت
نان ی ۹ ان 1 ۲ جم آ ۳ ۳ 5
وک اب چم ی ,

9 ِ :۳ ام مه 0 که
ود لت ( نیما :. 8*۰
1۹ ۸ 0 ۱۱ 0 ۵3 0

[ وت . 1 اد ۷۷ج 7
وی ۱۵ ۷( ۹۹۰ ی
0 هکس ۱ ی
او 0 و ها که ان
ری او مه 2 ۱ ۱
خ 77 4 اي . (

ی وود بر ها : از زر ۱ ۳
و تلو ۳ 1 در چَ

ورزش باستالی
بقیه در حاشيهٌ صفحهٌ ۲۲۷۰

======== pdf page 353  printed~ 2270
[pdf page 353]
ورزکار اهفننهه
کردن و ورزبدن باشد ۱ . ورزم « بفتح اول و نانی و سکون

۰ ثالك و میم » بمعنی‌آتش باشد که پزبان

ور ز کار ؟ - باکاف بروزن شرمار , ک پا بممنیآتش باش که پزبان عربی نا
ند ۰
پر ز گر و زراعت کننده راکوبند . .۹ ی :
زاو ۲ ودره !۱ < بروزن هرزه » ,معنی‌حاسل
ورزر گاو * «کاویرا کونبند که بدان کردن - و کشت و زراعت نسودن - و صنمت
زمین زراعت را شیا رکنند. و حرفت باشد - وزراعت کننده را نی زگونند.
ورزگن ۴ « با کاف فارسی بر وزن ورزی ۷ « بر وزن درزی » هزارع
کر کدن . کوز؛ پرآب راگوبند .۰ و زراعت کننده را کوبند .۷
۱- با بلاهای عشق ورزش کن خوبشتن را بلند ارزش کن .
اوحدی ۶« فرهنکه سروری ؟.
- بمعئی شفل وکار :
شما دین مانید و خرم پوید برامش سوی ورزش خود شوید.
فردوسی طوسی « شاهنامةٌ بخج ۱ص *۹*.
- اکنون بحر کت دادن اعضای بدن برای ایجاد قدرت ونیرو , اطلاق شود . 1

۴ - از: ورز (۸.م.) ۳ کار (پوند شغل و مبالفه) ۳ کارورز ( ر4: ورز [ح۲س۰)]۲۲۹۹

۴ - از: ورز(ه م.) ۳ کاو » رك : ورزاو . ۴ - جهانگیری ازمژبدالفنلاء‌همین
لفظ و معنی را نقل کرده , موْلف فرهنگه نظام کوید : « لفظ ومعنی عجیبی است >.

- تیر پرتاب تو در دیدء بدخواه توباد تا بود راستی ثیر کج از تاب ورزم .

آسوزلی سمرقندی « رشیدی >.

+ ‏از: ورز (ه.م.) ۰-۳ (حاسل مصدر). ۷ - رك : رشیدی . از: ورز(ه.م.)‎ - ٩
.) ‏ی ( سبت دال پرفاعلیت‎

0 ورزیدن - بفتح اول و پنجم » از : ورز (ه م.) ۳ بدن ( پسوند مصدری ) ؛ پهلوی
هقال۷۵2 * برزبدن (م.) رك: اسشق ۰۱۹۷ نیب رکك ص۲۳۶ : ۷872؛ کار کردن -کوشیدن-
زحمت کنیدن :
بدیشان (کاو وخر و کوسیند) بورزید وزیشان خوربد همی باج را خویشتن پرورید ۰

فردوسی طوسی ۶۸ شاهنامةٌ بخ ج۱.ض ۰۱۹
بقیه در حاشيةٌ صقحهٌ ۲۲۷۱

بقیه از حاشیةٌ صفحهٌ ۲۲۹۹

۴ - رك : ورزیدن. ۴ سورزا (صفت فاعلی ومشبعه از ورزیدن) بمعنی‌ورزنده
کاولر که در شخم کردن زمین زراعتیکارفرمایند. پپلوی ۷۵۳28 [1 82۷ « تاوادیا ۱۹۹ کردی
8 (گاوبر ) «ژابا س ۸۳۰ » طبری ۷6۳2۵ ( کاولرکاری ) « واژه‌نامه 2۷۸۳ » کیلکی
۷ » بروجردی ۷8720 ۶ شهیدی» » در آراك ) سلطانآباد ) ۷۵۳
```


## [2026-09-06T16:18:43.753Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (422,423,424,425):\n    print('======== pdf page',i+1)\n    p=pages[i]\n    import re\n    idx=p.find('کروه')\n    print(p[max(0,idx-900):idx+1500])\nEOF"
}
```


### [2026-09-06T16:18:45.523Z] TOOL RESULT

```
======== pdf page 423
 © بضم‌اول بروژن فروت»بممنی |
فربه باشدکه دربرابر لاغراست ۷ .

کرو تنه ؟ ‎he‏ اول وثانی وفوقانی ,
وتون وسکون ثالث ؛ عنکیوت را گوبند .

کروخ ‎ae‏ اول و ‎JU‏ و سکون ۱
‎IL‏ و خای نتطه دار . نام قربه‌است از فرای
عالم ۴ .

کروخان ۴ ‎lo‏ خای نتطفداربروزن
خروسان (۱) نام برادر ‎he‏ ویسه است. ۱

‎os‏ بشم اول بروزن سرود . چاه
بیار عمیق را گویند که آب از آن بدشواری
توان کشید ؛ و بفتح اول هم کفته‌اند ۵ .

‏کر ود ه با زای نقطه‌دار بروزن‌خروس»
‎ine‏ عیش وشاط و شادی و طرب باشد ‎٩‏ -
واندوه وملالت را نیز گفته‌اند؛ و با زای فارسی
هم‌آمده است .

‏کروس» بکر اول و سکون ‎BU‏

‎PF ‏اول بر وزن‎ eae PIS
. ‏شکنبه را گونند‎

‎Shane ۲ FIST‏ کاف بر ون
کبوتر. یکی ازنامهای‌خدای‌تءالی‌است جل‌جلاله.

‎en MOIS‏ اول و فتح‌نالكوسکون
ثانی و نون » اسبیرا گوین که رنگه اومابین زرد
وبور باشد .

‏کرو نیی ۰ بفتح اول و انی ‎dy‏
‎ay‏ و نون بشحتانی کشیده و بین بی‌قطفزده,
تام جزیره ات که وامق مطلوب عذرا در ‎OV‏
‏جزیره میبود ‎AY)‏

‏کروه = نم اول و انی ‎sly‏ مجهود
رسیده و بها زده » تلث وسه يك فرسخ را گویند
وآن سه هزارکز است وبعضی گویند چهارهزار
کز*۱و زیاده ازین بیست و آنرا بعربی کراع

‏(۱) چش : خرومان . (0) خم۱: میبوده .
۲ -کرچه در تألیف این ابیات لیست بی سمین غثی وغلی ب یکووت .
انوری اییوردی « فرهنگه نظام 6
‎brace ۴‏ ۴ -کروخ بفتح اول » شهری بود که بين ‎OT‏ وهرات
ده فرسنگه مسافت ‎ay‏ و کشمش ‎OT‏ مشهور بود . رك : عمجم‌البلدان , و رك : چهار مفاله طبع
تگارنده ص2۳ ‎AR,‏ . ۴ رگ : کرو . ۵ -رك : جهانگیری . رشیدی.
۷ - چون ‎Jo‏ باده‌خوار گشت جهان با نشاط و کروز وخوش منشی .

‏خروی « لغت فری ۱۷۵ *.
۷ - محیح « کر وگر» است. ۸ = کرن ‎Cpr)‏ ورثك: کرند, کرنده؛ کرنگه.

‎: ‏عنصری (بلضی) گوید‎ oy ‏درلفت فرس * کروتیس, جزیره ای بود که وامقآنجا‎ - ٩

‏جزیره یکی بد بیونان زمن کروتیس بد نام شهری کزین ۰ ۰
‎cal?‏ فرس ۷:۳ >
‎ol‏ همان > ‎Crétes,‏ ( اقربطش ) باشد ( دهشدا ). *۶- مافت قریب دو میل که

‏۰ کر است . جهانگیری و رشیدی بممنی ثلث فرسنگه که يك میل باشد نوشته‌اند . لیکن
این لفظ درهندی دکوس» 2 درسانسکریت کروش است که بمتی دو میل انگلیسی است » و در
اقفانتان « کروه» هستعمل است « فرهنگ ‎llr‏ » در ساتمکریت ۳052 ( اصلا آواز و ‎Clans‏
‏مافت ی که آواز برسد ) «دکتر راجا > .

======== pdf page 424
 که سیب کار‎
- ‏بسته (۳) باشد‎ aig ‏سخت شده و‎ he ‏کردن‎
‏چرك هم آمده است که عربان وسخ‎ gine ‏و‎
‎۰ ٩ ‏گویند ۸ (4) - و که را نیز کنتهاند‎
‏وآن روغنی باشد که از دوغ گیرند - و بمعنی‎
‏کاروان سرا و مدرسه‎ Ste ‏حچره هم هست که‎

(۷) چش: - ‎gly‏ .. کرده است.
(4) چك » چش : میگویند :

۱ -« بدانکه لفظ کراع که در جمیم سخ موجوده برهان فاطم بهمین شکل وعنوان
واقع است » درین مقام بغابت نامناسب است ‏ زیرا که بمعنیی که مراد مسنف است دز کتب

لغت ‎oe‏ با وجود تفحص نام اصلا بنظر نرسید:

۴ - بردش دمان تا بالبر زکوه

HOON dle,

که بورش بدانجا کنام 699
فردوسی طوسی « فرهنگه نظام *.

(karve)., 5: Sie ‏درفهرست ولف این‌کلمه نامده . ۴ = (ه.م.).‎ Jy
‏سوراخ » دندان فاسد ) ( اسدی , ص۱۱۵ ) , همچنین کرو ۸۳۷ ؛ شمس فخری‌س۱۱۳برك:‎ )
‏سفدی 8006 - 627۷ ( دارای دندان مجوف با فاسد ) ؛‎ (a ۸۲4 ‏ص‎ T ‏فولری‎
‎Henning, Sogdian loan words..,BSOS ‏رخنه)‎ , Gt - ‏خالی‎ ss) krw? ‏نیز‎
‎. 2 ۰. 1 , 0 . 6۰
. ‏باز چون بر گرفت دست ز روی کروه دندان و پشت چوکانت‎
EAN ‏سمرقندی « لفت فری‎ Soy,
‏رك : رشیدی + ۵ رك : کراوبا . ۱ ۱ -ظ . برساختة فرقةً‎ ۴
‏ضبط کردهء‎ » Gurdt Zitih ‏آذرکیوان . ۷ - ولف در فهرست شاهنامه «گروی زره‎
: ‏نام قهرمانی تورالی‎
‏از کام و داد تزادست و ه رگز مباد این بزاد.‎ SGT ‏گروی زره‎
۱۹5 ‏فردوسی طوسی . شاهنامةٌ بخ ج ۶ ص‎ «
‏این هردرپاك بینم وآن هردوبا کره.‎
> ۳۸۶ ‏خسرو بلخی ص‎ ol?
. ‏تلفظ کنند‎ kere(h) ‏امروزه‎ - ٩

Joy Ole ‏نه‌ییئمت‎ Dechy ‏چون‌دست‎ - ۸

. ‏بدل‌آن : هر دو پ زگره‎ ans

======== pdf page 425
[pdf page 425]
کره آب ۱ ۱۳۲
باشد (۱) - و ‎BE‏ عکبوت را هم میگویند ۱ | احاطه کرده است .
که درآن تخم کند ویچه برآردوآ ترا مانشدکاغن ۱ ‎oS‏ - بنتح اود و ‎gt‏ بر وزن
سفید سازد - و ‎AG;‏ مانشدی را کوید که بر | غدغن » عنکبوت راگوبند.

روی نان و میوه وامثال ‎OT‏ نشبند و معرب آن- ‎BS‏ لاجودد - کنابه از آسان
‎oS‏ باشد, چه هر چیز کره کرفته را متکرج
خوانند ۴ - و نوعی از خار هم هست که ‎Bet‏
‎LT‏ یعنی فشرد؛ آنرا اقاقیا کویند - و بزبان
هندی دست برنجن باشد وآن حلقه‌ایت از ‎Wh‏

است .
‎gine gag PIES‏ کرلاجورد
است که کنابه از آسمان باشد.

‎pth = os‏ اول ‎Gilly‏ بتحتانی کشیده,
علتی است ‎Grae‏ درگوش *۱- و پردة سفیدی
را نیز کوبند که عنکبوت بجهت تخم کردن‌وبچه
برآوردن میازد ‎WY‏

‏کریاس بکر اول بر وزن ‎ll‏ «
دربار پادشاهان و امرا و ‎abel‏ را کویند - و در
عربی بالاخانه را کوند - خلوت ‎SE‏ سلاطین
وامرا راهم گفته‌اند - ومحوطةٌ درون‌سر! وطهارت
خانه ای که بربالای خانه وحجره سازند ‎ME‏

‏کریان + بطم اول وسکون ‎gl‏ وثالث
بالف کشیده و بنون‌زده » بمعنی قربانی وقداباشد
بعنی بدلی که‌خود را با ‎Mate Ast Lp Ss‏
و پکر انی هم بیمین معتی پاش - و بکس
اول در عربی خواب آلود و پینکی زننده را

‎A) ‏گویند‎

‏ونقره و ‎Sond‏ دردست کنند - و نام شبری هم
عت ۴ و بفتح ‎Jy!‏ و سکون ثانی ۰ درعربی.
بمعنی ذخشتودی و تارضایی (۲) و جبر باشد -
و م اول و ‎OS‏ ثانی؛ هم باين معنی و هم
بمعنی دشوار باشدکه درمقابل آسان است ۴ -
و بضم اول و فتح ثانی مشدد. مه اسب و ستور
و خرالاغ را کویند ‎٩‏ - و باغیر مشدد, کویبر!
"که با چوکان بازند ‎٩‏ - و ‎de‏ اسب و خر دا
نیز گفته‌اند ۷ - و هرچیز که‌آن(۳) کرد ومدوز
باشد مطلقاً ۷ - وعتاصر را 55 )4( ‎Aas Se‏
======== pdf page 426
[pdf page 426]
۱۳۳

‎OOS‏ -بنتح اولرکس‌انی‌وسکون
تحتانی وجیم ۰ بمعنی ‎BL‏ کوچك باشد مطلقاً
- و خانة کوچکی را گویند که ازنی وعلف‌سازند
‎aul‏ خانه‌ای که دهقانان در ‎LT‏ زراعت و فالیز
میسازند ۴ - و تالاربرا هم گفته‌اند که بر بالای
خرمن ‎WE‏ نا کوفته سازند تا باران ‎cole‏ نکند؛
‎ok»‏ معانی ‎pe‏ اول و با جیم فارسی‌هم آمده
است - و تولك و پرریختن جانوران پرنده را
نیز کویند ۳ خصوصاً چرغ و باز وشاهین وامثال
آنرا (۱).

‏کریچه ؟ - بطم اول بر وزن کلیجه ,
خانةٌ کوچك(۲) را کویند مطلقاً - و خانه‌ای که
دهقانان از چوب و علف در ‎UT‏ زراعت سازند ؛
و با ‎ae‏ فارسی هم درست است.

‎PS‏ - بنم اول و تانی بتحتانی کنیده
و ‎ly‏ بی‌نقطةٌ زده ۰ بمعنی پیشکار وپاکار ‎ath‏
‏- و بفتح اول درعربی ‎ATs‏ وسدا کردن کسی
‎Sash‏ سینةارگرفتهباند ۰ و سدا کی که
اورا خفه میکرده باند , وصدا وآواز خرخری
که در وقت مردن از آدمی ظاهر میشود 5 .

‏کریز ۱ - ینم اول و نانی بتحتانی

‏)0 چش: + عموماً ۰
)9( چك : چش : نیزآمده است.

‏کشیده و بزای نقطه‌دار زده » بمعنی کریج است
که ‎de SEE‏ و خانة علفی باشد - وپرریختن
پرند گانرا نیز گوبند ۷ - و بمعن ی کنج ‏ و کوش
خانه هم‌آمدء است ؛ و بفتح اول نیز گفته‌اند .

‏کرلیزه * - بنم اول » بروزن و معنی
کربجه است که خانة کوچك - و پرربشتن‌مرغان
‎ath‏ .

‏کریزی - نم اود و انی و رابع هر
دو بتحتانی کشیده , مردم پبر ومنحنی را گویند
که در قرای" او هم قصوری بهم رسیده و خرف
شده باشد - و شاهین و بازیرا نیز گویند که در
صحرا بر خود تولكك ترده باشد یعنی پر ربخته
باشد ‎٩‏ - و چیزی هم هست که بخوردپر ند گان
تکاری دهند تا زود تولك کند وپر بریزد ‎٩‏ .

‏کر یس ‎SM‏ اول وئانی‌بتحتانی
کلبده و ‎ges‏ بی ‎Ub‏ زده » بمعن
```


## [2026-09-06T16:19:01.758Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"crks\\|crkws\\|crkws\\|črkus\\|vulture\" SOD.txt | head -20; echo \"--- SOD_pages ---\"; grep -n \"crks\" SOD_pages.txt | head"
}
```


### [2026-09-06T16:19:01.816Z] TOOL RESULT

```
5911:/carkas/     c/^i-             vulture       Av.  kahrkasa- 
29018:3253  crks  B,  M,  S  ^J 
29022:vulture 
95135:vulture     3253 
--- SOD_pages ---
12990:                                                                                      3253 crks B, M, S                                  ^J
```


## [2026-09-06T16:19:03.089Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--HRN--\"; grep -n \"sarfa\\|surfa\\|kargas\\|karkas\\|ẖurōs\\|hurōs\\|xurōs\\|kark \" HRN.txt | head -20; echo \"--HUB--\"; grep -n \"sarfa\\|kargas\\|karkas\\|Kargas\\|xurōs\\|hurôs\" HUB.txt | head -20"
}
```


### [2026-09-06T16:19:03.149Z] TOOL RESULT

```
--HRN--
7403:LW. af/. gar gas; bei. kargas, w, Kargaz (127); oss.
--HUB--
5263:*thun', kark *Huhn', kargas *Geier, gard 'StauV, gardan
7541:vas = s\iv, vag Vollen'?); kargas 'Geier = zd. kahrkasa-;
8530:--^ zd. vareka- ; kargas 'Geier = zd. kahrkasa- ; pargm re-
```


## [2026-09-06T16:19:10.043Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if '3253 crks' in p:\n        print('leaf',i,'printed approx',i-66)\n        import re\n        print(re.findall(r'\\b\\d{2,4}\\b',p)[:40])\n        j=p.find('3253 crks')\n        print(repr(p[max(0,j-600):j+600]))\nEOF"
}
```


### [2026-09-06T16:19:12.013Z] TOOL RESULT

```
leaf 193 printed approx 127
['128', '3239', '879', '14', '14', '3251', '898', '13', '460', '37', '17', '3240', '3252', '507', '12', '604', '605', '3253', '3241', '222', '139', '249', '238', '1320', '3254', '3242', '940', '243', '253', '147', '13', '27', '2211', '116', '13', '3243', '3255', '33', '34', '22']
"                                                                         3252 crap'Syh  M                                    ij^\n                           candar(y) ^cyntr1                                                car9-paSe ^tfrS'p^w\n                           inland, inside(C7i/na)                                          quadruped\n                                                                                           BBB 507\n                           Anc. Lett. 6.13n 9; Hen. BSOAS 12.604, 9, 605\n                                                                                      3253 crks B, M, S                                  ^J\n             3241 entry s'r                                 j**- ^^ ij^ * < Ji-b *\n                  candare-sSr                                                               carkas ©<Av.'kahrkasa\n                  0<?}China, (toward j)China                                                vulture\n                  Anc. Lett. 222                                                           GMS 139, 249; TSP 3.238, 1320; Bailey. Asica. 8\n                                                                                      3254 crm B, S\n          "
```


## [2026-09-06T16:19:23.948Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7395,7412p' HRN.txt; echo \"=== find leaf\"; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nlines=t.split('\\n')\ntarget=lines[7402]\nfor i,p in enumerate(pages):\n    if target in p:\n        print('leaf',i,'printed',i-21)\n        break\nEOF"
}
```


### [2026-09-06T16:19:25.987Z] TOOL RESULT

```
legendes, geiles Huhn *^).
Kas. karg, kerk (s. v. mi(ry).
aw. *kahrka- in kahrkam- *Hühn«»rfresser (OtMor)';
phlv. kark; ai. kfka\mku' 'Hahn'.
kurd. kurk 'Huhn'; afy. cirg; oss. /•«;•/• 'Ih'nno,
Huhn (154); wa;^. kork,
9. kerf/es 'Geier' (Sahn. I, 120 Vers 1013).
aw. ÄraÄrArtZs^- 'Geier; \)h]\\ kahrkäs, kargua (Bund.).
LW. af/. gar gas; bei. kargas, w, Kargaz (127); oss.
cär^r//« (S. 134); syr. Dpip.
Das nur bei den Pärsen noch vorkommende np.
karkatas 'Geier scheint nach aw. kahrkatas- repristinirt
zu sein.
*) Auch nuf persischen Inschriften in Indien, vergl. Epigraphia
:ca ir, US Note 25.
*J Diese spezificirte He<ieutung der Wörtorhüclior ist vioUoicht
• küii^tUch «M'soinion.- 190 —
850. kirni *Wurm'.
=== find leaf
leaf 210 printed 189
```


## [2026-09-06T16:19:33.504Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--HRN Husten--\"; grep -n \"Husten\" HRN.txt | head -20; echo \"--HUB Husten--\"; grep -n \"Husten\" HUB.txt | head -20"
}
```


### [2026-09-06T16:19:33.565Z] TOOL RESULT

```
--HRN Husten--
6456:aufgeführt und gehört zu surfe 'Husten', surfiden.
--HUB Husten--
```


## [2026-09-06T16:19:34.859Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--CHEUNG xraud/xraus--\"; grep -n \"xrau\\|xraus\\|xrōs\\|xrus\" CHEUNG.txt | head -30"
}
```


### [2026-09-06T16:19:34.922Z] TOOL RESULT

```
--CHEUNG xraud/xraus--
10497:(contaminated with *xrau ‘to tear, break, scratch’ ?) || (+ *a-) ? Bal. (EHB) awali0/ 
28626:contamin. with *xraud) 
28851:*xrau 447 
28909:*xrau ‘to tear, break, scratch’ 
28917:448 *xraud 
28942:*xraud ‘to become/make angry ?, afraid ?, confused ?' 
28955:confuse, distract’. © Dissimilated from *pari/a-xrauda- < *раг/а-хгаиба- < 
28956:*pari/a-xrauda(ia)-. © Samadi: 158 f. 
28968:*xraus ‘to call’ 
55623:*9rah, *9ram, *xraud 
55628:*xraud, *zarH' (s.v.) 
55641:(s.v.), *xraud, *xsai (s.v.), 
55800:*scand, *xrau 
55891:*uab/f! , *xraus, *zauH 
56019:*uab/f! , *xraus, *zau H 
56588:* гай, *9ram, *xraud 
57102:*xraud 
57690:*draub, *huar”, *xrás, *xrau 
58136:*Hraup, *xrau
```


## [2026-09-06T16:19:37.566Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28960,29010p' CHEUNG.txt; echo \"=== HRN surfe ===\"; sed -n '6440,6470p' HRN.txt"
}
```


### [2026-09-06T16:19:37.629Z] TOOL RESULT

```
9 The precise meaning of this root needs to be elucidated. 

“PIE LIV: — | Pok.: 


*REFERENCES: Werba 1997: 172 


*xraus ‘to call’ 

*AVESTAN: xraos- ‘to cry’ (better: ‘to call’ ?) = Liste: 16 

Pres. {1} them.: ОРТ. 35р. YAv. fra(-ca) "xraosöit (A 3.13), IMPV. 3pl. med. OAv. xraosantam ира (Y 
53.8); Pres. {2} ja-: IND. 3sg. YAv. xraosiieiti (V 15.5) 

*MIDDLE PERSIAN: BMP hlws- /xroh-/ or /xrös-/ ‘to call, cry’, MMP xrwh ‘call’ 
(with xw’n- ‘to call’) || (+ *ni-) MMP nxrwh- ‘to reproach? = DMMPP: 364a f., 
249a f. 

Partic: perf. pass. BMP hlwst /xröst/ || (+ *ni-) Pres.: IMPV. 25р. MMP nxrwh; Partic.: perf. pass. II 
MMP nxrwhyd 

*PARTHIAN: xrws- ‘to call, evoke’, xrws ‘call’ = Ghilain: 64 | DMMPP: 364b 


*xràs 449 


Pres.: IND. 3sg. xrwsyd, 1р1. xrws’m, 3pl. xrwsynd, SUBJ. 15р. xrws’n, 1р1. xrws'm, IMPV. 2pl. xrwsyd, 
“xrwsyyd; Partic.: pres. xrwsg, perf. pass. xrwst, "xrwstg 


*KHOTANESE: grüs- ‘to call’ = SGS: 32 


*SOGDIAN: (+ *ni-) CSogd. nxrys- ‘to rebuke’ 
Impf.: IND. 3sg. CSogd. nyxrs {hapax} 


*NWIR: NP xurösidan ‘to cry, shout’, NP xurös, Anar. hiros, Jow. ru:s, Nn. huros 
‘rooster, cock’. The intervocalic -s- of NP xurösidan is the result of the following 
developments: < OP *-si- < *-0/- < Plr. *-si-. 

*SANSKRIT: kros ‘to call aloud, call to’ (RV+) > EWAia I: 416 

9 An IE provenance for this common Ш. root cannot be established. Pokorny: l.c. 
cites the isolated formation, OE hréam ‘emergency call’ (< Germ. *hrauhma ?), as a 
possible cognate. 


«PIE? > LIV: — | Pok.: 571 
=== HRN surfe ===
ndd. schuft (fichucht) 'Schulter (Bezzenberger, BB.
I, 341, vergl. Bartholomae, Studien II, 39).
si;!!. siwd, sar. sewd, sangl. siwd;.'d\hRn. sup,
740. snften 'durchbohren', Praes. sumh-eni'^), sufUem,
aw. \/saoi)' in sufrä- 'Pflug, die Geiger unter
bei. sufnbag (No. 352) noch vergleicht, niuss weg-
fallen, da miorä' zu lesen ist (vergl. Bartholomae,
der ZDMG. 46; 294 aw. suwrä- mit 'Pfeif übeisetzen
will); phlv. suftan (für aw. sifat'^); Bund.).
kurd. sonfin 'durchbohren*, Praes. bSsomim.
Vergl. np. sumb^) 'Loch* (Xo. 740), süli (No. 758).
741. sifl/iden 'pfeifen, zwitschern*.
lat. stbiläre, sißläre 'zischen, pfeifen', sibilus 'pfeifend,
zischend; Gepfeif, Gezisch'; franz. siff^er (Hörn, KZ.
32, 586 No. 19, onomatopoetische Bildungen).
np. sußJden wird dagegen nur als 'husten' bedeutend
aufgeführt und gehört zu surfe 'Husten', surfiden.
Got. sviglön 'pfeifen* (Froehde, BB. 3, 15; 14, 111)
und kelt. sige^ sidhe^ sighe 'Hauch' (Strachan, BB.
18, 147) lassen sich kaum lautlich mit den neup.-
lat. Formen vereinigen (die Araber haben safir
'pfeifend', daher np. auch mftr kerden 'pfeifen').
742. sekär, sikar^ sukar 'Kohle'.
aw. gareniö,]skarana (vd. 14, 7) 'Brennkohlen', vergl.
skairya- (vd. 8, 95) 'Kohlenmeiler (Geldner, KZ. 25,
566 Note 15); af/. skör 'Kohle'.
Hat np. nigal 'Kohle* (nur FS) etwas mit sekär zu
schaffen ?
»J Auch nicht Vd. 18, 16, vergl. Geldner, KZ. 28, 301.
') Geschrieben stmho.
^) Aw. (/ aaef' ist ihrer Bedeutung nach unsichor.
```


## [2026-09-06T16:20:11.503Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--HRN surfe entry--\"; grep -n \"surfe\\|surfiden\\|surf\" HRN.txt | head -20; echo \"--HUB kargas ctx--\"; sed -n '7535,7548p' HUB.txt"
}
```


### [2026-09-06T16:20:11.558Z] TOOL RESULT

```
--HRN surfe entry--
1285:surf, 'Kälte'.
6456:aufgeführt und gehört zu surfe 'Husten', surfiden.
22426:surf 100.
--HUB kargas ctx--
xuros und amas (A. M. 8, 8) 'Geschwulst' zu amah (Horn
p. 106 Anm. 1)? Vgl. den Wechsel von ap. rs und r^
aus rk^ (§ 103) und von ap. z, rz und d, rd (Kap. 20).
§ 101. In einigen Fallen findet sich auch zwischen
Vokalen np. s, wo, nach np. has = ap. vasiy zu urtheilen,
im Ap. s, nicht ^ stand: has viel, genug == ap. vasiy (zu
vas = s\iv, vag Vollen'?); kargas 'Geier = zd. kahrkasa-;
pes *Aussatz, aussatzig JRAS. 1894, 451 = zd. pa^sa-;
ges^ gSsU Locken* = zd. ga^sa-; nivSsam 'ich schreibe' =
ap. *nipaisamiy {niyapisam ist sigm. Aorist ^- idg. ni-e-pik^-
sO'tn); resam *ich. spinne', hah resay; xusur 'Schwiegervater
= zd. x^asura-; rasan *Strick' = skr. ragana-; cis *Muhl-
stein', vgl. zd. asan- *Stein ; btst 'zwanzig aus *visat = zd.
vlsaiti; xuros *Hahn, skr. Wrzl. krog; kus H. 852 (?)
```


## [2026-09-06T16:20:12.851Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--HJB coss--\"; grep -n -i \"^COSS\\|CoSS\\|krosa\\|krośa\\|kos, s\\.\" HJB.txt | head -20"
}
```


### [2026-09-06T16:20:12.905Z] TOOL RESULT

```
--HJB coss--
1017:Padre  Juan  Gonzales  de.  The work  was  first  published  at  Bome  in 1585 :  Historia  de  las  cossas  mas  notables, Bitos  y  Costumbres  del  Gran  Beyno  de la  China  (&c.) .  .  .  hecho  y  ordenadopor el  mvy  B.  P.  Maestro  Fr.  Joan  Gon- salea  de  Mendo^  ko.  The  cjuotations are  from  the  Hak.  Soc.'S  reprint,  2  vols. (1853),  of  B.  Parke's  E.T..  entitled  "The Historic  of  the  Greet  and  Mightie  King- dome  of  China  '*  (kc).    London,  1588.
2705:1752.— **  The  Cossembasar  merchants baring  fallen  short  in  gurrahs,  plain  taffa- ties,  ordinary  baadaimoeB,  and  chappas."— In  Long,  81.
3545:1781.— "I  have  the  happiness  to  inform you  of  the  fall  of  Bijah  Qurh  on  the  9th mst.  with  the  loss  of  only  1  sepoy,  1  beasty, and  a  cossy  (?  Cossid)  killed  .  .  ."—Letter in  India  OazetU  of  Nov.  24th.
3674:1761. — "You  will  also  receive  several private  letters  from  Hastings  and  Sykes, which  must  convince  me  as  Circumstances did  me  at  the  time,  that  the  Duteh  forces were  not  sent  with  a  View  only  of  defend- \D^  their  own  Settlements,  but  absolutely with  a  Design  of  disputing  our  Influence  and Possessions;  certain  Ruin  must  have  been the  Consequence  to  the  East  India  Company. The^  were  raising  black  Forces  at  I^tna, Cossimbazar,  Chinsura,  &c.,  and  were working  Night  and  day  to  oompleat  a  Field Artillery  ...  all  these  preparations previous  to  the  commencement  of  Hos- tilities plainly  prove  the  Dutch  meant  to act  offensively  not  defensively." — Holograph Letter  from  Glive  (unpublished)  in  the  India Office  Records.  Baled  Berkeley  Square, and  indorsed  "27th  Deer.  1761."
4603:„  "We  received  a  letter  from  .  .  . Council  at  Cossimbazar  .  .  .  advising  of their  having  sent  Ensign  McKion  with  all the  Military  that  were  able  to  travel,  150 buxenries,  4  field  pieces,  and  a  large  quan- tity of  ammunition  to  Cutway."— 7Wrf.  p.  1.
4607:„        "In  an  account  for  this  voir  we find  among  chaiges  on  behalf  of  WUliaia Wallis,  Esq.,  Chief  at  Cossimbazar : Rs. "'4Buxerie8.    .    .    20  (year)  .  240.' " MS.  Records  in  India  Office.
5438:1669.— "This  aforesaid  bird  CossebJtrea also  will  swallow  iron  and  lead,  as  we  once learned  by  experience.  For  when  our  Connes- tabel  once  had  been  casting  bulleta  on  the Admiral's  Bastion,  and  then  went  to  dinner, there  came  one  of  these  Coasebtoas  on  the bastion,  and  swallowed  60  of  the  bullets. And  .  .  .  next  day  1  found  that  the  bird after  keeping  them  a  while  in  his  maw  had regularly  cast  up  again  all  the  60."—/.  /.
7546:coss.
7564:COSSACK.
7566:COSSID,
7591:COSSIMBAZAR.
7599:CX)88IMBA2^AB,  n.p.  Properly Kdmmbdzdr,  A  town  no  longer  existing, which  closely  adjoined  the  city  of Munhidabad,  but  preceded  the  latter. It  was  the  site  of  one  of  the  most  im- portant factories  of  the  East  India Company  in  their  mercantile  days,  and was  indeed  a  chief  centre  of  all  foreign trade  in  Bengal  during  the  17  th  cen- tury. ["  In  1668  the  Company  estab- lished a  factory  at  Cossimbazaar, *  Castle  Basaar.'''— <^tn2i£woc2  Rep,  on Old  Bee,  219.)]  Fryer  (1673)  calls  it Oastle  Bazzar  (p.  is),
8148:1788.—*'  11  pandt  que  les  cateha  cosses wmt  pliis  en  usage  que  les  autres  cosses  dans le  g^uvemement  du  Decan.  "—i>Mre«  JBdiJi- antetj  zv.  190.
10523:GOW,  GAOU,  8.  Dak.  H.  gav^  An ancient  measure  of  distance  preserved in  S.  India  and  Ceylon.  In  the  latter island,  where  the  term  stiU  is  in  use,  the gavnoa  is  a  measure  of  about  4  English mile&  It  is  Pali  gdvuta,  one  quarter of  a  yojana,  and  that  again  is  the  Skt. gavyuti  with  the  same  meaning^.  There 18  in  Molesworth*s  Mahr,  victionary, and  in  Wilsotij  a  term  gaukos  (see C08S),  ^a  land  measure'  (for  which read  *  distance  measure'),  the  distance at  which  the  lowing  of  a  cow  may  be heard.  This  is  doubtless  a  form  of the  same  term  as  that  under  considera- tion, but  the  explanation  is  prolwtbly modem  and  incorrect.  The  yqjana with  which  the^fatt  is  correlated,  ap- pears etymologically  to  be  *  a  yoking,' viz.  "  the  stage,  or  aistance  to  be  ^ne in  one  harnessing  without  unyoking" (JFilUaTM);  and  the  lengths  attributed to  it  are  very  various,  oscillating  from 2^  to  9  miles,  and  even  to  8  kroSas (see  C088).  The  last  valuation  of  the yojana  would  correspond  with  that  of the  gau  at  ^.
11896:1614.— "  Per  PoOterint.  If  it  please  God this  Persian  business  fail  out  to  y'  oontentt, and  y^  you  thinke  fitt  to  adrenture  thither, I  thinke  itt  not  amisse  to  sett  you  downe  as y«  Pilotts  have  informed  mee  of  JasquM, w«^  is  a  towne  standinffe  neere  y«  edge  of a  straightte  Sea  Coast  where  a  ship  may  ride in  8  fathome  water  a  Sacar  shotte  from  y« shear  and  in  6  fathome  you  maye  bee  nearer. Jasqne  is  6  Oemet  (see  JAM,  b)  from  Ormus southwards  and  six  Oemes  is  60  cosses  makes 30  leagues.  Jasques  lieth  from  Muschet east.  From  Jasques  to  Sinda  is  200  cosses or  100  leagues.  At  Jasques  comonly  they have  northe  winde  w<^  blowethe  trade  out  of y«  Persian  Gulf  e.  Miaohet  is  on  y*  Arabian Coast,  and  is  a  little  portte  of  Portuffalls."— MS.  Letter  from  Nick.  DowtUoh,  dd.  No- vember 22,  1614,  in  India  Office ;  [Printed in  Foster,  Letters,  ii.  177,  and  compare  ii. 146].
12035:1686. — "Books  of  accounts  received  from Dacca,  with  advice  that  it  was  reported  at the  Court  there  that  the  Poll-money  or Jndgeea  lately  ordered  by  the  Mogul  would be  exacted  of  the  English  and  Dutch.  .  .  . Among  the  orders  issued  to  Pattana  Cossum- bazar,  and  Dacca,  instructions  are  eiven  to the  latter  place  not  to  pay  the  Adgeea or  Poll-tax,  if  demanded."  —  ^.  St.  Geo. Consru,  (on  Tour)  Sept.  29  and  Oct.  10; Nolea  and  Extraet*^  No.  i.  p.  49.
12643:1813.— "We  .  .  .  saw  nothing  remarkable -on  the  way  but  a  Khidmntgar  of  Chimnagie Appa,  who  was  rolling  from  Poona  to Punderpoor,  in  performance  of  a  vow  which he  made  for  a  cnild.  He  had  been  a  month at  it,  and  had  become  so  expert  that  he went  on  smoothly  and  without  pausing,  and kept  rolling  evenly  along  the  middle  of  the road,  over  stones  and  everything.  He travelled  at  the  rate  of  two  coss  a  day."— ICfphiiUtone,  in  Lifc.j  i.  257-8.
14719:1688.— "  Cossadass  ve  Chief  Secretary, Matsaddles,  and  ^e  Nabobs  Chief  Eunuch will  be  paid  all  their  money  beforehand." — Hedges,  Diary,  Jan.  6 ;  [Hak.  Soc.  i.  61].
15218:1727.— *' Mnzadabaud  is  but  12  miles from  it  (Cossimbazar),  a  Place  of  much ffreater  Antiquity,  and  the  Mogul  has  a Mint  there  ;  but  the  ancient  name  of Muxaddbaud  has  been  changed  for  Rajah- mal,'  for  above  a  Century." — A,  Hamilum, ii.  20  ;  fed.  1744].  (There  is  great  confusion in  this.)
15748:Srovisions  cross  the  Mountains.  ...*•— 'atwnier,  E.T.  ii.  183 ;  [ed.  Ball,  ii.  263], 1788.^"  Kote  Kangrah,  the  fortress  be- longing to  Uie  famous  temple  of  Nagoroote, is  given  at  49  royal  cosses,  eoual  to  99  G. miles,  from  Sirhind  (northward)." — Rennell, Memoir,  ed.  1793,  p.  107.
```


## [2026-09-06T16:20:17.806Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7540,7566p' HJB.txt"
}
```


### [2026-09-06T16:20:17.848Z] TOOL RESULT

```
1&58. — **0n  the  other  or  western  side^ over  against  the  Kingdom  of  Oriza,  the Bengalis  (ot  Btngalot)  hold  the  Kingdom  of Coepetir,  whose  plains  at  the  time  of  the risinjg^  ot  the  Ganges  are  flooded  after  the fashion  of  those  of  the  River  Nile." — Autm, Dec.  IV.  ix.  cap.  I.
This  and  the  next  passage  compared  show that  Barros  was  not  aware  that  Cospetir  and Gajpati  were  the  same.
„  **  Of  this  realm  of  Bengala^  and  of other  four  realms  its  neighbours,  the  Gen- toos  and  Moors  of  those  parts  sav  that  God has  g^ven  to  each  its  peculiar  gift :  to  Ben- gala  infantry  numberless;  to  the  Kingdom of  Orixa  elephants ;  to  that  of  Bisnaga  men most  skilful  in  the  use  of  sword  and  shield ; to  the  Kingdom  of  Dely  multitudes  of  cities and  towns ;  and  to  Cou  a  vast  number  of horses.  And  so  naming  them  in  this  order they  give  them  these  other  names,  viz. : Etpaty^  Oaspaty,  Noropaty,  Buapaty,  and Coapaty. "—^anxM,  ibid,  [These  titles  ap- pear to  be  Atvapatiy  "Lord  of  Horses  ; Qajapati  ;  Narapatiy  "  Lord  of  Men  "  ; BhUpaHy  "Lord  of  Earth";  Oopaiiy  "Lord of  Cittle."]
c.  1590.— "His  Majesty  (Akbar)  playa with  the  following  suits  of  cards.  1st.  A$k- wapaiiy  the  lord  of  horses.  The  highest  card represents  a  King  on  horseback,  resembling the  King  of  Dihli.  .  .  .  2nd.  dajpati,  the King  whose  power  lies  in  the  number  of  his elephants,  as  the  ruler  of  Orisah.  .  .  .  3rd»
C0S8.
261
coss.
Narpal^^  a  King  whose  power  lies  in  his  in- ffintry,  as  is  the  case  with  the  mlers  of Bijitprfr,"  4c.— ^U,  i.  806.
c.  1500. — "Orissa  contains  one  hundred and  twenty-nine  brick  forts,  sabject  to  the command  of  Gtljepiitty." — Ayem  (by  Glad- «rm),  ed.  1800,  ii.  11 ;  [ed.  JarrtU,  li.  126].
1753. — *'  Herodote  fait  aussi  mention d*une  ville  de  Ckupatyrtu  fo.ta.6e  vers  le haut  du  flouye  Indus,  oe  que  Mercator  a era  correspondre  k  une  denomination  qui existe  dans  la  G^cgraphie  modeme,  sans alteration  marqu^  savoir  Cospetir.  La notion  qu'on  a  de  Cospetir  se  tire  de lliistorien  Portugais  Jean  de  Barros  .  .  . la  situation  n'est  plus  celle  qui  oonvient  k Caspatynts,**—D*Anville,  4  $eq.
C08S,  8.  The  most  usual  popular measure  of  distance  in  India,  but  like the  mile  in  Europe,  and  indeed  like the  mile  within  the  British  Islands  up to  a  recent  date,  varying  much  in different  localities.
The  Skt.  word  is  JbroMi,  which  also is  a  measure  of  distance,  but  originally signified  'a  call,'  hence  the  distance  at which  a  man's  call  can  be  heard.***
In  the  Pali  vocabulary  called  Abhid- hdnappadwikdy  which  is  of  the  12th century,  tne  word  appears  in  the  form koss;  and  nearly  this,  kos^  is  the  ordi- nary Hindi.  KuroK  is  a  Persian  form of  the  word,  which  is  often  found  in Mahommedan  authors  and  in  early travellers.  These  latter  (English) often  write  course.  It  is  a  notable circumstance  that,  according  to  Wran- cell,  the  Yakuts  of  N.  Siberia  reckon oistance  by  hiataes  (a  word  which, considering  the  Russian  way  of  writ- ing Turkisn  and  Persian  words,  must be  identical  with  kos).  With  them this  measure  is  *'  indicated  by  the  time necessary  to  cook  a  piece  of  meat." Kiost  18= to  about  5  vents^  or  1|  miles, in  hilly  or  marshy  country,  out  on plain  ground  to  7  ventSj  or  2|  miles.t The  Yakuts  are  a  Turk  people,  and their  language  is  a  Turki  dialect.  The suggestion  arises  whether  the  form kos  may  not  have  come  with  the  Mon-
*  "It  Is  characteristic  of  this  region  (central fOEVSts  of  Ceylon)  that  in  traversing  the  forest they  calculate  their  inarch,  not  by  the  eye,  or  by measures  of  distance,  but  by  sounds.  Thns  a ' do^sery*  indicates  a  quarter  of  a  mile ;  a  ' oodlr't erov,'  something  more;  and  a  'Aoo'  implies  the space  over  which  a  man  can  be  heard  when  shout> ing  that  particular  monosyllable  at  the  pitch  of hfs  voice. '^—reiifisnfj  (kfUm,  iL  582.  In  a  Oanara also  to  this  day  such  expressions  as  "a  horn's Mow,"  "  a  man's  call,"  are  used  in  the  estimation 4>f  distances.    [Bee  under  GO W.  ]
t  U  NordtUla  fHbirU,  i.  81
gols  into  India,  and  modified  the previous  kraia?  But  this  is  met  by the  existence  of  the  word  koi  in  Pali, as  mentioned  above.
In  ancient  Indian  measurement,  or estimation,  4  kroias  went  to  the  yojana. Sir  H.  M.  Elliot  deduced  from  dis- tances in  the  route  of  the  Chinese pilgrim  Fa-hian  that  the  yqjana  of  his age  was  as  nearly  as  possible  7  miles. Cuimiuffham  makes  it  7^  or  8,  Fergus- son  6 ;  out  taking  Elliot's  estimate  as a  mean,  the  ancient  kos  would  be  1{ miles.
The  kos  as  laid  down  in  the  Ain  Fed. Jarretty  iii.  414]  was  of  5000  gaz  [see OUDOE].  The  official  decision  of  the British  Government  has  assigned  the length  of  Akbar's  Ildhi  ^cks  as  33  inches, and  this  would  make  Akbar's  ik(w= 2  m.  4  f .  183|  yards.  Actual  measure- ment of  road  distances  between  5  pair of  Akbar's  kM-mindrt,*  near  Delhi,  gave a  mean  of  2  m.  4  f.  158  yards.
In  the  greater  part  of  the  Bengal Presidency  the  estimated  kos  is  about 2  miles,  but  it  is  much  less  as  you approach  the  N.W.  In  the  upper  part of  the  Doab,  it  is,  with  fair  accuracy,  1 J miles.  In  Bundelkhand  again  it  is nearly  3  in.  (Cameffy\  or,  according to  Beames,  even  4  m.  [In  Madras  it is  2^  m.,  and  in  Mysore  the  StUtdnl kos  is  about  4  m.]  Reference  may  be made  on  this  subject  to  Mr.  Thomas's ed.  of  Prinsep's  Essay Sy  ii.  129  ;  and  to Mr.  Beames's  ed.  of  Elliot's  Glossary (''The  Baces  of  the  N.-JV,  PravineeSy^' ii.  194).  The  latter  editor  remarks that  in  several  parts  of  the  country there  are  two  kinds  of  kosy  a  pakkd  and a  kachchd  kos,  a  double  system  which pervades  all  the  weights  and  measures of  India  ;  and  which  has  prevailed  also in  many  other  parts  of  the  world  [see PUCKA].
c.  500.—"  A  gavySiik  (or  league— see  CK>W) is  two  kroias."— ^mamAxM^  ii.  2, 18,
C.600.— '*The  descendant  of  Kukulstha (i.e.  Rama)  having  gone  half  a  kroia^  .  .  ." — RaghuvanuAy  xiii.  79.
c.  1840.— ''Ab  for  the  mUe  it  is  called among  the  Indians  al-KorfUi."— /^  BatutOy iii.  95.
„      "  The  Sultan  gave  orders  to  assign me   a  certain  number   of   villages.    .    .    .
.  •  ".  .  .  that  Royal  Allevof  Trees  planted  by the  command  of  Jehan'Guiret  and  continued  by the  same  order  for  160  leagues,  with  little  Pyramids or  Turrets  erected  every  half  lesgue."— Mmi«r, B.T.  91 ;  [ed.  CoMtabk,  284].
COSSACK.
262
COSSID,
```


## [2026-09-06T16:20:19.372Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if \"kargas 'Geier = zd. kahrkasa-\" in p:\n        print('leaf',i,'printed',i-10)\nEOF"
}
```


### [2026-09-06T16:20:21.366Z] TOOL RESULT

```
leaf 222 printed 212
leaf 249 printed 239
```


## [2026-09-06T16:20:26.796Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l MON_part1.txt MON_part2.txt && head -c 600 MON_part1.txt"
}
```


### [2026-09-06T16:20:26.842Z] TOOL RESULT

```
  99339 MON_part1.txt
  94500 MON_part2.txt
 193839 total
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س 


همجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نامه مدش نامع 

مه مر وه ود 

3 ور 133131313 


هم مشب جج جب بیج چم مدوجو 
چم وم 
جر 


درل ولو ونر نو تلا رت 
11 


مج جرج جر یی میج 6و یوج هو هجوج وی یویر جر دم مور و 555 
و ده ها وی مزا موی
```


## [2026-09-06T16:20:32.733Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"کروه\" MON_part1.txt MON_part2.txt; grep -c \"کرکس\" MON_part1.txt MON_part2.txt; grep -c \"خروس\" MON_part1.txt MON_part2.txt"
}
```


### [2026-09-06T16:20:32.810Z] TOOL RESULT

```
MON_part1.txt:13
MON_part2.txt:38
MON_part2.txt:4
MON_part1.txt:1
MON_part2.txt:23
MON_part1.txt:25
```


## [2026-09-06T16:20:35.417Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"کرکس\" MON_part1.txt MON_part2.txt | head -10; echo \"=== kroh ===\"; grep -n \"کروه\" MON_part2.txt | head -20"
}
```


### [2026-09-06T16:20:35.476Z] TOOL RESULT

```
MON_part1.txt:89574:چنانکه دال و کرکس باز کنند؛ مق. دف. 
MON_part2.txt:22192:کرکس ترکش: تیری که در ترکش گذارند. 
MON_part2.txt:25340:کرکس. که سروی پر ندارد. 
MON_part2.txt:37955:خورد. (جاد.) کرکس. (مج.) کسی که اموال 
MON_part2.txt:53897:و کرکس و قرقی است و از دسته شکاریان 
=== kroh ===
1995:دفع امر مکروه و ناپسندی باشد؛ آن را قوة 
4468:(ابضا) ). فاعل مرکب: (فد. ) اگر ؟ کروهی از 
6593:فرموک: تاد (۱.) کروهة رسسمان 
9057:فوج: ات [ع.] (.) گکروه» دسته. 
12762:مکروهی با از تصور آن. جمع شدن پوست 
18551:کاشف مکروه (و مانند آن): بر طرف کنندة 
18552:مکروه؛ از بین برنده اندوه. کاشف به عمل 
21602:ناپسند داشتن» چیزی را مکروه داشش. 
22544:کرو (0۷-) ,6۲۵۷ ,1۵۲ [- کروه] (.) 
22597:کروه: (۷۵۳۷2۸)۵ [- کرو ] (.) دندان مبان 
22601:کروه] (.) واحد مسافت. جهانکیری و 
22607:کروه فرهنگ فارسي معیر ۱۳۳ 
22613:کروه: ۲ (.) مقام» منزل» آشانه. 
26243:کماندو: ۳(۵) 010۱ (.) گکروهی از 
27983:معادل لك فرسخ» کروه. 
29642:مسافت و آن معادل سه کروه زمین است و 
29643:چون کروه را بعضی ۳۰۰۰ گز و بعضی 
30359:بکروه 
44601:باشد؛ مق. مندوت» مکروه؛ حللال » حرام و 
45100:وود کت ت4: ناسند داشته. بکروه؛ ج.
```


## [2026-09-06T16:20:37.705Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22595,22615p' MON_part2.txt"
}
```


### [2026-09-06T16:20:37.755Z] TOOL RESULT

```
حجر دک می‌ کر دند. آثار این نژاد در 
حوزه کر ومانیون (فرانسه) بدست آمده. 
کروه: (۷۵۳۷2۸)۵ [- کرو ] (.) دندان مبان 
نهی » دندان سوراح. 

کر وه: (0۲-)۲۵۲0۰ آهند» کوس, افغانی: 
کروه] (.) واحد مسافت. جهانکیری و 
رشیدی به معنی ثلث فرسنگ (که یک میل 
باشد) نوشته و در برهان ثلث و سه یکت 
فرسخ معادل سه هزار گز و به قولی چهار گز 


کروه فرهنگ فارسي معیر ۱۳۳ 


آورده؛ در هندوستان آن را برابر دو میل 
انگلیسی می‌گیرند. 

کروه: ۲ (.) مقام» منزل» آشانه. 
کروی: 1 (ص نسه.) منسوت به کره؛ 
آنچه که به شکل گوی بود.
```


## [2026-09-06T16:20:48.176Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '53890,53905p' MON_part2.txt; echo ---; sed -n '22186,22196p' MON_part2.txt"
}
```


### [2026-09-06T16:20:48.242Z] TOOL RESULT

```
فوقانی منقار خود دارای زایده‌ای دنداسی 
شکل هستند که دن‌الة بوست روی آن را 
می بو شاند و انگشتانشان ره چنگال‌های وی 
خمیده ختم می‌شود. پرندگان شکاری به دو 
دستةٌ شکاریان روزانه و شکاریان شبانه 
تقسیم می‌شوند. مهمترین پرنده از دسته 
شکاریان روزانه عقاب و شاهین وقوش (باز) 
و کرکس و قرقی است و از دسته شکاریان 
شبانه جغد و مرغ حق است. مرغان عرشی: 
(کد.) فرشتگان» ملایکه. مرغان قاف: 
عنقاهاء سیمرغ‌ها. ترکیبات فعلی: مر غ فلانی 
دوست می‌خواند: چون کسی به مرادی رسد 
و در کمال نشاط باشد گویند یعنی دماغش 
چاق است. (قس. مرغ‌دوست). (تص.) ولی» 
مرشد. مرغ تمام: (تص.) مرد کامل» مر شد 
مرغابی: آ-29ومحج [ - مرغ آبی] (امر.) 
---

زیاد است بطوری که از فواصل دور 
ای رک ری شم نهر 
کوچکترین حرکت از نظرش مخفی 
نمی‌ماند؛ لاشخور» مردارخواره مرغ 
مر دارخوار» رخمه» نسر. (مج.) تیر» سهم. 
کرکس ترکش: تیری که در ترکش گذارند. 
کرک شدن: ۲0:00:0 (مصل.) 
بصورت کر ک. در آمدن. (عم.) ژولنده 
شدن (موی).
```


## [2026-09-06T16:20:51.043Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22160,22192p' MON_part2.txt"
}
```


### [2026-09-06T16:20:51.101Z] TOOL RESULT

```
ک رکس: :۷:۲۲ (.) (جاذ.) پرنده‌ای است 
قوی هیکل و بد ریخت و گوشتخوار از 
راستةٌ شکاریان روزانه که دارای منقار قوی 
برگشته و گردن و سر لخت و بال‌های‌وسیعو 
بسزرگمی‌باشد و در نواحی‌کوهستانی 
ول گر می‌نماید و بیشتر از لاشه تغدذ به 
کی ای و 
جنوبی و شمال آفریقا و آسیای مرکزی و 
غربی و جنوبی پراکنده است. در موقع پرواز 
گسترش بال‌های وی بالغ بر سه متر می‌شود. 
پنجه‌های کر کس بر خلاف منقار پر قدر تش 
نسبهة ضعیف است بطوری که به وسلهة 
پنجه‌هایش قادر نیست جز طعمه‌های بسیار 
کوچک را نگهداری کند و به همين جهت 
است که ببشتر از لاشه و مردار حبوانات 
دیگر تغذیه می‌نماید» پرواز وی نسبة آهسته 
ولی دارای اوج است و در مدت طولانی 
صورت می‌گیرد. قدرت دید این پرنده سیار 


1 


۱۳۴۸ فرهنگ فارسی معين کرک شدن 


زیاد است بطوری که از فواصل دور 
ای رک ری شم نهر 
کوچکترین حرکت از نظرش مخفی 
نمی‌ماند؛ لاشخور» مردارخواره مرغ 
مر دارخوار» رخمه» نسر. (مج.) تیر» سهم. 
کرکس ترکش: تیری که در ترکش گذارند.
```


## [2026-09-06T16:21:02.832Z] TOOL CALL #48: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(d['KLN']['page_offset']);print(d['KLN']['lookup_hint'])\""
}
```


### [2026-09-06T16:21:04.996Z] TOOL RESULT

```
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
```


## [2026-09-06T16:21:08.310Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nleaf=1305//2+12\nfor i in range(leaf-3,leaf+3):\n    p=pages[i]\n    print('=== leaf',i)\n    print(p[:1200])\nEOF"
}
```


### [2026-09-06T16:21:10.175Z] TOOL RESULT

```
=== leaf 661
tidhs,  per¬ taining  to  the  president’,  fr.  L.  praesidens,  gen. -entis.  See  president  and  -ial.
Derivative:  presidential-ly,  adv. presidial,  adj.,  pertaining  to,  or  having,  a  garri¬
son.  —  F.  presidial,  fr.  Late  L.  praesidialis,  ‘of  a garrison’,  L.  praesidium,  ‘a  presiding  over,  de¬ fense,  garrison’,  fr.  praesidere.  See  presidium  and adj.  suff.  -al.
presidiary,  adj.,  presidial.  —  L.  praesidiarius,  ‘per¬ taining  to  a  guard’,  fr.  praesidium.  See  prec. word.
presidio,  n.,  a  fort,  a  garrison  in  the  S.W.  of  the U.S.  and  in  Sp.  America.  —  Sp.,  ‘garrison’,  fr. L.  praesidium.  See  presidial. presidium,  n.,  a  permanent  administrative  com¬ mittee  in  the  government  of  the  U.S.S.R.  — Russ,  prezidium,  fr.  L.  praesidium,  ‘a  presiding over,  defense’,  fr.  praesidere.  See  preside, presignify,  tr.  v.,  to  signify  beforehand.  —  L.  prae- significare,  fr.  prae  (see  pre-)  and  significare,  ‘to show  by  signs,  signify’.  See  signify, press,  tr.  v.,  to  squeeze;  intr.  v.,  to  exert  pressure. —  ME.  pressen,  fr.  OF.  (=  F.)  presser,  fr.  L. pressare,  freq.  of  premere  (pp .pres
=== leaf 662
ential  suff.  -or. prevenance,  n,,  anticipation  of  the  needs  of  others. —  F.  prevenance,  fr.  prevenant,  pres.  part,  of prevenir,  ‘to  go  before,  anticipate’,  fr.  L.  prae- venire.  See  prevent  and  -ance. prevenient,  adj.,  preceding;  preventive.  — L.prae- veniens,  gen.  -ends,  pres.  part,  of  praevenire,  ‘to come  before,  anticipate’.  See  next  word  and  -ent. prevent,  tr.  v.  —  ME.  preventen,  fr.  L.  praeventus,
pp.  of  praevenire,  ‘to  come  before,  to  anticipate’, in  Late  L.  also  ‘to  prevent’,  fr.  prae  (see  pre-) and  venire,  ‘to  come’,  fr.  I.-E.  base  *gwem-,  ‘to come’,  whence  also  Goth,  qiman,  OE.  cuman, ‘to  come’.  See  come  and  cp.  venue,  ‘arrival’. Derivatives:  prevent-able,  adj.,  prevent-abil-ity, n.,  prevent-ative,  adj.  and  n.,  prevent-er,  n., prevent-ible,  adj.,  prevent-ive,  adj.  and  n., prevent-ive-ly,  adv.
prevention,  n.,  1)  the  act  of  preventing;  2)  an  ob¬ stacle.  —  Late  L.  praeventio,  gen.  -onis,  ‘the  ac¬ tion  of  anticipating’,  fr.  L.  praeventus,  pp.  of praevenire.  See  prec.  word  and  -ion.
Derivative:  prevention-al,  adj.
previous,  adj.  —  L.  praeviu
=== leaf 663
e, adj.,  and  -ive.
Derivatives:  primitive,  n.,  primitive-ly,  adv., primitive-ness,  n.,primitiv-ism,  n.,  primitiv-ist,  n., primitiv-ist-ic,  adj.
primo,  n.,  the  first  or  leading  part  ( mus .)  —  It.,  fr.
L.  primus,  ‘first’.  See  prime,  adj. primo-,  comb,  form  meaning  ‘first’.  —  L.  primo-, primo,  adv.,  ‘first’,  fr.  primus,  adj..  ‘first’.  See prime,  adj.
primogenital,  adj.,  primogenitary.  —  Eccles.  L. primogenitalis,  fr.  Late  L.  primogenitus,  ‘first¬ born’.  See  primogeniture  and  adj.  suff  -al. primogenitary,  adj.,  pertaining  to  primogeniture.
—  Formed  with  adj.  suff  -ary  fr.  Late  L.  primo- genitus,  ’firstborn’.  See  next  word.
primogenitor,  n.,  an  ancestor.  —  ML.  primogeni¬ tor,  compounded  of  primo-  and  L.  genitor,  ‘be¬ getter,  father’,  fr.  genitus,  pp.  of  gignere.  See
i
1Z4J
next  word  and  agential  suff.  -or  and  cp.  pro¬ genitor.
primogeniture,  n.,  the  state  of  being  the  first-born child  of  the  same  parents.  —  ML.  primdgeni- tura  (whence  also  F.  primogeniture),  fr.  Late  L. primogenitus,  ‘first  bom’,  which  is  compounded of  L.  primo  (adv.),  ‘first’,  and  genit
=== leaf 664
alue,  price’.  Prize  is  the  doublet  of  price  (q.v.) The  spelling  prize  is  due  to  the  influence  of prize,  ‘act  of  seizing’.  Cp.  praise, prize,  tr.  v.,  to  estimate.  —  ME.  prisen,  fr.  OF. preisier,  prisier  (F.  priser),  fr.  Late  L.  pretidre, ‘to  prize,  value’,  fr.  L.  pretium.  See  prec.  word and  cp.  misprize.
prize,  n.,  something  taken  by  force.  —  ME.  prise, fr.  OF.  (=  F.)  prise,  ‘a  taking,  seizing,  holding’, prop.  fern.  pp.  used  as  a  noun,  fr.  prendre,  'to take,  seize’,  fr.  L.  prendere,  contracted  form  of prehendere.  See  prehensile  and  cp.  prey,  prison. Cp.  also  mainprize.
Derivative:  prize,  tr.  v.,  to  force, prize,  n.,  a  lever.  —  ME.  prise,  fr.  OF.  (=.  F.) prise,  ‘a  taking,  seizing’.  See  prec.  word. Derivative:  prize,  tr.  v.,  to  press,  esp.  with  a lever,  to  pry.
pro-,  pref.  of  Latin  origin  meaning  ‘before,  for¬ ward,  forth,  for,  in  favor  of;  in  place  of,  on behalf  of;  according  to’.  —  L.  pro-,  fr.  pro, ‘before,  in  front  of,  for,  on  behalf  of,  instead  of’, rel.  to  per,  ‘through’,  prae,  ‘before’,  por-  (for *pr-),  ‘forward’  and  co
=== leaf 665
ns,  gen.  -entis,  pres.  part,  of  procidere, ‘to  fall  forward,  fall  down’,  fr.  1st  pro-  and cadere,  ‘to  fall’.  See  cadence.  For  the  change  of Latin  a  (in  cadere)  to  i  (in  prd-cidere)  see  abigeat and  cp.  words  there  referred  to. proclaim,  tr.  v.  —  ME.  proclamen,  fr.  L.  prdcld- mare,  ‘to  call  out,  cry  out’,  fr.  1st  pro-  and  cld- mare,  ‘to  call,  cry’.  See  claim,  v.
Derivative:  proclaim-er ,  n. proclamation,  n.  —  ME.  proclamacioun,  fr.  MF. (=  F.)  proclamation,  fr.  L .  proclamationem,  acc. of  proclamatio,  ‘a  calling  out,  outcry’,  fr.  pro- clamatus,  pp.  of  proclamare.  See  prec.  word  and -ation.
proclitic,  adj.  —  ModL.  procliticus,  formed  on analogy  of  encliticus  fr,  Gk.  TrpoxXIvsiv,  ‘to lean  forward’,  fr.  itpo  (see  2nd  pro-)  and  xXTveiv, ‘to  lean’.  See  enclitic.
proclivity,  n.,  tendency,  inclination.  —  F.  procli¬ vity,  fr.  L.  proclivitatem,  acc.  of  prdclivitas,  ‘des¬ cent  ;  tendency,  inclination’,  fr.  proclivis,  ‘slop¬ ing  downward;  inclined’,  fr.  1st  pro-  and  cli¬ vus,  ‘slope,  hill’.  See  clivus  and  -ity. proconsul,  n.  —  ME.,  fr.  L.  proconsul,
=== leaf 666
l,  adj.  —  Formed  with  adj.  suff.  -al  fr. Late  L.  professorius,  ‘pertaining  to  a  public teacher’,  fr.  L.  professor.  See  prec.  word. Derivatives:  professorial-ism,  n .,  professorial-ly, adv.
proffer,  tr.  v.  —  ME.  profren,  proferen,  fr.  AF. profrer,  fr.  OF.  porofrir,  profrir,  fr.  pref.  por-, ‘forward’,  and  ofrir,  ‘to  offer’.  OF,  por-  derives fr.  VL.  por,  which  corresponds  to  L.  pro, ‘before,  for’;  see  1st  pro-.  OF.  ofrir  (whence  F. offrir)  derives  fr.  VL.  *  offer  ire,  which  corre¬ sponds  to  L.  offerre,  ‘to  offer’,  for  whose  etymol¬ ogy  see  offer,  v.
proficiency,  n.  —  Formed  from  next  word  with suff.  -cy.
proficient,  adj.  —  L.  proficiens,  gen.  -ends,  pres, part,  of  proficere,  ‘to  go  forward,  advance,  effect, accomplish’,  fr.  1st  pro-  and  facer e,  ‘to  make, do’.  See  fact  and  cp.  profit.  For  the  change  of Latin  a  (in  facere)  to  l  (in  pro-ficere,  pro-ficiens) see  abigeat  and  cp.  words  there  referred  to.  For the  ending  see  suff.  -ent.
Derivatives:  proficient,  n.,  proficient-ly,  adv., proficient-ness,  n.
profile,  n.,  side  view.  —  It.  profilo,  p
```


## [2026-09-06T16:21:17.501Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(691,698):\n    print('=== leaf',i)\n    print(pages[i][:900])\nEOF"
}
```


### [2026-09-06T16:21:19.286Z] TOOL RESULT

```
=== leaf 691
’,  and  putrah,  ‘son,  boy’.  For  the  first  ele¬ ment  see  rajah.  The  second  element  is  rel.  to Avestic  and  OPers.  pudra-,  ‘son,  child’,  and cogn.  with  L.  puer,  ‘boy,  child’;  see  puerile  and cp.  words  there  referred  to. rake,  n.,  a  tool.  —  ME.  rake,  fr.  OE.  raca,  rel.  to ON.  reka,  ‘spade,  shovel’,  Swed.  raka,  ‘rake’, OHG.  rehho,  MHG.  reche,  G.  Rechen,  ‘rake’.
rake
1298
and  to  ON.  raka,  MLG.  raken,  ‘to  sweep  away’, Goth,  rikan,  ‘to  heap  up,  collect’,  and  prob. cogn.  with  Gk.  bpifeiv,  ‘to  reach,  stretch  out’, L.  regere,  ‘to  stretch,  extend,  make  straight;  to rule’,  perh.  also  with  L.  rogus,  ‘funeral  pile’.  See regent,  adj.,  andcp.  rack,  ‘instrument  of  torture’. Cp.  also  reckon.
rake,  tr.  and  intr.  v.,  to  use  a  rake,  to  scrape.  — ME.  raken,  fr.  rake,  G.,  ON.  raka,  ‘to  scrape’
=== leaf 692
anunculus  and  -arium. ranee,  n.,  a  variety  of  Belgian  marble.  —  F.,  of unknown  origin.
ranch,  n.,  a  large  farm  with  its  buildings  and  em¬ ployees.  —  Mexican  Sp.  rancho,  ‘a  small  farm’, fr.  Sp.  rancho,  ‘mess,  messroom’,  fr.  OHG. hring,  ‘circle,  ring’.  See  ring,  n.
Derivatives:  ranch,  intr.  v.,  ranch-er,  n. rancid,  adj.,  stale.  —  L.  rancidus,  ‘foul-smelling’, fr.  rancere,  ‘to  stink,  rank’,  which  is  of  uncer¬ tain  etymology.  Cp.  next  word.  For  the  ending see  adj.  suff.  -id  (representing  L.  -idus). Derivatives:  rancid-ity,  n.,  rancid-ly,  adv., rancid-ness,  n.
rancor,  rancour,  n.,  bitter  resentment,  spite.  — ME.  rancour,  fr.  OF.  rancour,  fr.  L.  rancorem, acc.  of  rancor,  ‘a  stinking  smell,  rankness,  ran¬ cidity’,  fr.  rancere.  See  prec.  word  and  -or. Derivatives:  rancor-ous,  adj.,  rancor-ou
=== leaf 693
h  is  cogn.  with  Gk.  ep^itTEoftat,  ‘to pluck  off,  feed  on’,  Alb.  rjep,  ‘I  strip,  rob’, Lith.  raples,  ‘tongs’,  ap-repiu,  ‘I  take,  seize’,  fr. I.-E.  base  *rep-,  ‘to  snatch,  seize’.  Beside  ♦rep- stands  prob.  *srep-,  *s(p-  in  Gk.  ap7rx£etv,  ‘to snatch,  seize’,  apnaS,  ‘rapacious’,  ip-avr;, ‘hook;  rake’,  apm),  ‘sickle’,  (Sprojtou,  ‘harpies’, lit.  ‘snatchers’.  Cp.  conception,  erepsin,  rap,  ‘to seize’,  obreption,  obreptitious,  rape,  ‘to  seize’, rapine,  rapt,  ratero,  raven,  ‘to  prey’,  ravin,  rav¬ ish,  subreption,  surreptitious,  usurp.  Cp.  also harpy,  sarmentose.
Derivatives:  rapid,  n.,  rapidity  (q.v.),  rapid-ly, adv.,  rapid-ness,  n.
rapidity,  n.  —  F.  rapidity,  fr.  L.  rapiditatem,  acc. of  rapiditds,  ‘swiftness,  rapidity’,  fr.  rapidus.  See prec.  word  and  -ity.
rapier,  n.,  a  light,  sharp-pointed  sword.  —
=== leaf 694
rear,  reri,  ‘to  reckon,  believe, think’ ;  see  rate,  ‘amount’.  For  the  etymology  of L.  fiat  see  fiat.
ratal,  n.,  an  amount  at  which  property  is  assessed. —  Formed  with  adj.  suff.  -al  fr.  rate,  ‘amount’, on  analogy  of  rental. ratan,  n.  —  The  same  as  rattan, ratany,  n.  —  The  same  as  rhatany. rataplan,  n.,  the  repeated  sound  of  a  drum.  —  F., of  imitative  origin.
Derivative:  rataplan,  tr.  and  intr.  v. rat-a-tat,  n.  —  See  rat-tat. ratcb,  n.,  ratchet.  —  Short  for  ratchet. Derivatives:  ratch,  tr.  v.,  to  fit  with  a  ratchet, ratch-ing,  n.
ratch,  intr.  v.,  to  reach  ( naut .)  —  A  var.  of  reach, ratchet,  n.,  a  click,  pawl.  —  F.  rochet,  ‘bobbin, spindle,  ratchet',  fr.  Frankish  *rokka,  ‘spindle’, which  is  rel.  to  OHG.  rocko,  ‘distaff’,  fr.  I.-E. base  *rug-,  ‘to  spin’.  See  rock,  ‘distaff’
=== leaf 695
.  v.,  to  devour  greedily (rare).  —  MF.  raviner ,  ‘to  ravager’,  fr.  ravine, ‘rapine’.  See  ravin.
Derivatives:  raven-ing,  adj.,  raven-ing-ly,  adv., raven-ous,  adj.,  raven-ous-ly,  adv,,  raven-ous- ness,  n.
ravigote,  n.,  shallot  sauce.  —  F.,  back  formation fr.  ravigoter,  ‘to  revive,  refresh’,  which  is  form¬ ed — with  change  of  suff. — fr.  OF.  ravigorer, of  s.m.,  fr.  pref.  ra-,  contraction  of  L.  re-  and  ad (see  re-  and  ad-)  and  vigor,  gen.  vigoris,  ‘liveli¬ ness’.  See  vigor.
ravin,  ravine,  n.,  plunder.  —  ME.  ravin,  ravine,  fr. MF.  ravine,  ‘rapine,  robbery’,  fr.  OF.,  fr.  L.  ra- pina.  See  rapine  and  cp.  raven,  ‘to  prey’.  In  ModF. ravine  means  ‘torrent,  gully’.  Cp.  next  word.
ravine,  n.,  a  deep  cleft  or  gorge.  —  F.,  ‘mountain torrent,  ravine’,  fr.  OF.  ravine,  ‘rapine,  robbery; rapidity,  im
=== leaf 696
nd  cp.  words  there  referred  to.
ream,  n.,  20  quires  of  paper.  —  ME.  reme,  fr.  OF. ray  me  (F.  rame),  fr.  Sp.  resma,  fr.  Arab.  rizmah, ‘bundle,  bundle  of  paper’.
ream,  n.,  cream;  froth.  —  ME.  rem,  fr.  OE. ream,  ‘cream’,  rel.  to  MLG.  rom,  rome,  Du. room,  MHG.  roum,  G.Rahm,  Icel.  rjomi,  ‘cream’, fr.  Teut.  base  *rauma-,  which  corresponds  peril, to  I.-E.  *raugma-,  whence  Avestic  raoyna-,  ‘but¬ ter’.  Cp.  ramekin.
Derivatives:  ream,  intr.  and  tr.  v.,  ream-y,  adj.
ream,  tr.  v.,  to  enlarge  a  hole.  —  Lit.  ‘to  make room’,  fr.  ME.  remen,  rumen,  fr.  OE.  ryman,  ‘to make  room,  widen’,  fr.  rum,  ‘spacious,  wide’. Cp.  OS.  riimian,  ON.  ryma ,  OFris.  rema,  OHG. rumen,  ‘to  make  room,  widen’.  Cp.  also  E.  dial. rime,  ‘to  enlarge  a  hole’,  and  see  room, reamer,  n.,  a  tool  for  enlarging  a  hole.
=== leaf 697
p., secondary  form  of  recabdo,  ‘caution,  care,  solic¬ itude,  attention’,  fr.  recabdar,  ‘to  gather,  keep in  custody,  assure’,  fr.  VL.  *recaptdre,  ‘to  seize’, fr.  re-  and  L.  captare,  ‘to  seek  to  catch’,  freq.  of capere  (pp.  captus ),  ‘to  catch’.  See  captive, recalcitrance,  recalcitrancy,  n.  —  Formed  from next  word  with  suff.  -ce,  resp.  -cy. recalcitrant,  adj.,  refractory.  —  F.  recalcitrant, lit.  ‘kicking  back’,  fr.  L.  recalcitrantem,  acc.  of recalcitrdns,  pres.  part,  of  recalcitrare.  See  next word  and  -ant.
Derivative:  recalcitrant,  n. recalcitrate,  intr.  v.,  to  refuse  to  obey  (rare).  — L.  recalcitrdt-(um),  pp.  stem  of  recalcitrare,  ‘to kick  back’,  fr.  re-  and  calcitrdre,  ‘to  kick’,  fr. calx,  gen.  calcis,  ‘heel’.  See  Calceolaria  and  ver¬ bal  suff.  -ate  and  cp.  inculcate.
Derivative:  recal
```


## [2026-09-06T16:21:25.375Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^raven,\\|^rook,\\|^scream,\\|^screech,\\|^cricket,\\|^ring, n\\.\" KLN_1966.txt | head -20"
}
```


### [2026-09-06T16:21:25.425Z] TOOL RESULT

```
9673:cricket,  n.,  an  insect  of  the  order  Orthoptera.  —
9676:cricket,  n.,  the  game.  —  OF.  criquet,  ‘stick,  stake used  as  goal  in  the  game  of  bowls’,  fr.  MDu. cricke,  ‘stick’,  which  stands  in  gradational relationship  to  OE.  crycc,  ‘crutch’.  See  crutch. Derivatives:  cricket-er,  n.,  cricket-ing,  n. crico-,  combining  form  meaning  ‘pertaining  to the  cricoid  cartilage’  (anal.)  —  See  next  word, cricoid  (anal.),  adj.,  pertaining  to  the  cartilage of  the  larynx;  n.,  the  cricoid  cartilage.  —  Gk. xpiKoetSf)?,  ‘ring-shaped’,  compounded  of  xpi- xos,  ‘ring’,  and  -oeiSvj^,  ‘like’,  fr.  el8o?,  ‘form, shape.  See  circus  and  -oid. cried,  past  tense  and  pp.  of  cry.  —  ME.  cride, cried,  fr.  crien,  ‘to  cry’.  See  cry  and  -ed. crier,  n.  —  ME.  criere,  fr.  OF.  criere,  nom.  of crieur,  fr.  crier,  ‘to  cry’.  See  cry  and  agential suff.  -er.
31770:raven,  n.,  a  large  bird  of  the  crow  family  (Corvus corax).  —  ME.,  fr.  OE.  hrxfn,  rel.  to  ON.  hrafn, Dan.  ravn,  MLG.  rave,  Du.  raaf,  OHG.  hraban, rabo,  MHG.  raben,  rabe,  G.  Rabe,  ‘raven’,  and cogn.  with  L.  crepare,  ‘to  creak,  clatter’,  pos¬ sibly  also  with  OI.  k(pate,  ‘laments’.  These words  are  labial  enlargements  of  I.-E.  base *qer-,  *qor-,  *qr-,  imitative  of  harsh  sounds. From  the  same  base  are  Gk.  xopa!;,  ‘crow, raven’,  xoptovij,  ‘crow’,  L.  cornix,  ‘crow’, corvus, ‘raven’,  OI.  krdsati,  Avestic  xraosaiti,  ‘cries, shouts’,  OI.  krosah,  ‘a  call,  a  shout’,  OSlav. krikii,  ‘shout’,  kridati,  ‘to  shout’,  Gk.  xpdt^eiv, xpo>£eiv,  ‘to  croak’,  xpauyiq,  ‘a  crying,  a  shout¬ ing’,  L.  crocire,  ‘to  croak’,  OSlav.  kracu,  kra- kati,  Lith.  kraukiii,  kraukti,  ‘to  croak',  OSlav. kruku,  ‘raven’,  Lith.  kraukiys,  ‘crow’,  Lett. kradklis,  ‘raven’,  Lith.  krdke,  OPruss.  krakko, ‘the  black  woodpecker’,  Mir.  corr,  ‘crane’,
31772:raven,  intr.  v.,  to  prey;  tr.  v.,  to  devour  greedily (rare).  —  MF.  raviner ,  ‘to  ravager’,  fr.  ravine, ‘rapine’.  See  ravin.
33093:rook,  n.,  a  black  bird  belonging  to  the  crow  fam¬ ily.  —  ME.  rok,  fr.  OE.  hroc,  rel.  to  ON.  hrokr, MDu.  roec,  Du.  roek,  ‘rook’,  OHG.  hruoh, ‘crow’,  of  imitative  origin.  See  raven,  n. Derivatives:  rook,  tr.  v.,  to  cheat,  rook-ery,  n., rook-ish,  adj.,  rook-ling,  n.,  rook-y,  adj. rook,  n.,  castle  (at  chess).  —  ME.  rok ,  fr.  OF.  roc. See  roc.
34222:scream,  intr.  and  tr.  v.  —  ME.  scremen,  fr.  ON. skrsema,  ‘to  terrify,  scare’,  rel.  to  Swed.  scrana, ‘to  scream’,  OS.,  OHG.  scrian,  MHG.  schrien, G.  schreien,  ‘to  cry’,  fr.  I.-E.  base  *(s)qrei-, whence  also  ON.  hreimr,  ‘scream,  cry’,  hrlna,  ‘to squeak,  squeal’,  L.  crimen,  ‘complaint,  crime’, orig.  ‘cry  of  distress’ ;  see  crime  and  cp.  screak, screech.  Base  *(s)qrei-  is  an  enlargement  of  the imitative  base  *qer-;  see  raven.
34225:screech,  intr.  and  tr.  v.  —  Fr.  earlier  scritch, which  derives  from  the  I.-E.  imitative  base *(s)qrei-.  See  scream  and  cp.  words  there  re¬ ferred  to.  Cp.  also  shriek,  which  is  a  doublet  of screech.
```


## [2026-09-06T16:21:36.630Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\ndef leafof(sub):\n    for i,p in enumerate(pages):\n        if sub in p:\n            nums=re.findall(r'\\n\\s*(1[0-9]{3}|[3-9][0-9]{2})\\s*\\n',p)\n            return i,nums\n    return None,None\nfor s in [\"raven,  n.,  a  large  bird\",\"rook,  n.,  a  black  bird\",\"scream,  intr.  and  tr.  v.\",\"cricket,  n.,  an  insect\"]:\n    print(s[:20], leafof(s))\nEOF"
}
```


### [2026-09-06T16:21:38.278Z] TOOL RESULT

```
raven,  n.,  a  larg (694, [])
rook,  n.,  a  black (721, ['1356'])
scream,  intr.  and  (745, ['1405'])
cricket,  n.,  an  i (206, ['373'])
```


## [2026-09-06T16:21:47.268Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--WLD Bd1 ker-1--\"; grep -n \"kahrkasa\\|kahrkāsa\\|kahrkatat\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt 2>/dev/null | head -10"
}
```


### [2026-09-06T16:21:47.330Z] TOOL RESULT

```
--WLD Bd1 ker-1--
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:26039:Bezeichnung des Hahnes, npers. kark ..Huhn ‘, av. kahrkasa- m. ,,Geier,
```


## [2026-09-06T16:21:48.332Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--IEC--\"; grep -n \"korax\\|kork-\\|krokos\\|krok-\\|kerk-\" IEC.txt | head -15; echo \"--SYN raven--\"; grep -n -i \"raven\\b\" SYN.txt | head -10"
}
```


### [2026-09-06T16:21:48.390Z] TOOL RESULT

```
--IEC--
7035:kerk- ‘cluck; clucking bird". Cf. kirkos and karkó. Cf. WP I, 414 Sk. cf. čarčarīh "a kind of song Hes. kerkís ʻa bird’; Ir. cearc, f. ‘hen’; Blg. cf. krékam, v. ‘croak, caw'; Latv. cf. kercu, kérkt, id.; OPr. kerko, n. (*diver-bird' or *shellduck"); Oss. cf. kark, pl. kárcítá, s. Chen. fr. *kark-); Per. cf. kürg��s (^vulture', fr. *krkot- or *karket-). (Iso- phonic: Skt. čarčāmi (abuse)
7037:(kerk-, see kirk- (krk-). E-gde forms are Slovene čresiti ‘to tan? and Li. keřšinu, -ti ‘avenge oneself)
7224:kirkos, å “a screeching bird’. Cf. WP I, 413 & II, 569 Per. cf. Giryad “cricket; Gk. kírkos (ambig: *gier-hawk'. Cf. kirK-); Hes. kirke (an un- named bird); cf. Kírke (name of a siren); Mir (ambig.) cerc, Ir. cearc, f. Chen" See kerk-); Li. kirka (gull. Ambig. cf. krk-); be- side kirkiü, -ti ‘screech’; Latv. cf. cirkstu, et, id. (*kirksK-); Slovak cf. krsiak Chawk fr. *kirksiak-
7680:kork- (?) ‘scotch, scotched', etc. (kark-?) Arm. karkem ‘baffle; silence’; MHG hargen limp, hobble’; Li. cf. karksóti, inf. “hang around, be disconsolate, mope’
7783:krak- (2) (rock, rough ground’. Cf. krok- ' (2) and krak- (1) Br. krag, pl. kragu ‘flint, pebble’; Ir. W. craig "rock beside W crag “crust, coat, shell’; long- gde in Alb. krok 'stony ground” (fr. *-à-) (LW in Eng. crag). (The hapax cracentes is prob. ‘bracing themselves")
7788:krako, ið ‘caw, croak’. Cf. krak- (5), krok-, kark-. Onomat. WP I, 414 Alb. krrok, krókem, id. (krr- an expressive variant); Lat. craco, are, id.; W crawcio, id. denom.; OCS kračọ, krakati (also com. SL), id.; Li. krokiu, -ti ‘grunt’; Latv. kràcu, krakt 'rattle, roar, snore'
7979:krok- (1) (-os, à, us) ‘stay, beam, crosspiece, strut'. (Much of the evidence is ambig.). Cf. WP I, 482-3. (Long-gde variant in Gk.(?) ON, and Srb.) Skt. cf. krakacah, -am ‘saw’; variant in Gk. króssai, króssai ‘battlements, course of stones’: (?) ON hroerar, mpl. ‘groin’: Sw. ro, pl. roer 'hipbone'; Rum. substr. cracá, f. "branch"; Ir. croch (1) *cross, gallows’; W crog, pl. au, f. ‘cross, crossbeam’; Cor. crók, pl. crogow 'gallows'; Cz. krokev, krokva, usu. pl. krokvy ‘rafter, spar’; Pol. krokiew, id.; cf. also Pol. krok (2) ‘groin, perinium, crutch’; Li. kraké (2) ‘stick’; Latv. krakis ‘stool, stand, gable’. Long-gde in Srb. krak ‘haunch’
7980:krok- (2) “loop, curl, crook, hook’ Arm. kor i-st. ‘crotchet; griffin’; Gk. krokús, f. “lock of wool’; Ir. croch (2) ‘pothook’; Br. krók, krog, pl. krogu & kreier “hook, harpoon’; krogen, pl. kregin ‘pot-handle’; Cor. rocken ‘snare’; OCS cf. krok-orjavü ‘curly’
7981:krok- (3) ‘pebble, shell Gk. krókos, krókë (2) ‘pebble’; Hes. krókkai ‘beach’; Br. cf. krogen, pl. kregin ‘shell’; Cor. crogen, pl. cregyn ‘shell, skuil; E cf. (?) rag ‘ragstone, schistic limestone’
7982:krók- variant of krok- (1) in Gk. krõssai; (?) ON hrærar; Srb. krak; Slovene krača ‘flank’; Big. krak ‘foot, leg, treadle'. Cf. WP I, 487
7983:krokəlos, krokulos ‘pebble, marble, berry’. Cf. krok- (3) Gk. krokále ‘beach’; Li. krakulai, mpl. “frog- spawn’
8102:crācens, adj. ‘lean’ (*krK-). O-gde in Li. karšē *decrepitude". Cf. kerk- and next
8427:kurguos (1) (? variant: kurquos in Gmc.) ‘filth, mucus, rheum’ Av. kuruyð "a disease’; Per. kiy "lippitude"; Arm. ambig. kork, i-st (“filth?. Cf. kork- (1)); OHG, OS horo, gs horawes ‘filth’; MHG be- horgen ‘defile’; OE horh, gs horwes ‘phlegm, filth’; horgian, v. ‘defile’; ON horr ‘snot’; Cz. krh, krhy, m. sg. & pl. “Tippitude?
8442:kurk- (4), see kurquos and cf. kurguos (1) and kork-
8450:kurquos (kurk-) “filth, mucus'. Prototype uncertain. Cf. kurguos (1) & kork- Arm. (ambig.) kork, Let ‘filth’; OE horh, gs horwes, id. (& mucus"); Latv. cf. kurkstu, kurkt (2) ‘rot, grow mouldy’
--SYN raven--
7483:Nir. cuirim, adhlacaim NE bury, inter Av. (nasu-spaya- ‘burial’) W.  claddu, daearu Du. begraven
12500:8.22 DIG oxaxTw, dplcow, Goth. graban Lith. kastt Aaxalvw ON grafa Lett. rakt oxdBuo Dan. grave ChSl. kopati, ryti fodere Sw. grdva SCr.  kopatz, ritt vangare (scavare) OE grafan, delfan Boh.  kopati, ryti ‘ied (fouir, fouil- ME grave, digge, delve Pol. —kopae, ryé sa NE dig (delve) Russ. kopat’, ryt’ oe Du. graven (delven) Skt. khan- dlaidim OHG  graban, telban Av. kan- rehercin MHG graben, telben : NHG graben cloddio, palu f Klaza, kava 1. Gtk. okdarr : a) A ChSL., SCr. (NG pop. oxéw) Grk. daxaivw (not common): Ir.
27997:Sw. skraita ‘laugh’ (Dan. skratte ‘give a cracked sound’, Norw. ‘laugh loudly’) : Sw. dial. skrata ‘resound’, older Dan. skrade ‘rattle’, Ir. scret, Nir. scread ‘ery’, fr. an extension of an imitative *(s)ker-, cf. Skt. ka@rava- ‘crow’, Grk. xopaé Lat. corvus ‘raven’, etc. Walde-P. 1.415. Falk-Torp 1025. Hellquist 946.
28443:Skt. krpa-: krp- ‘lament, implore’, Lat. crepere ‘rattle, creak’, ON hrafn, OE hrefn ‘raven’, etc. Uhlenbeck 64. Walde-P. 1.415 f. Walde-H. 1.290.
31503:Grk. xpé¢w, also and perh. orig. ‘croak’ (of frogs), ‘caw’ (of ravens), cf. xpatw ‘caw’, prob. : ON hrodkr, OE hréc, etc. ‘rook, raven’, Skt. kharj- ‘creak’, khar- gala- ‘a, certain night-bird’, all of imita- tive origin. Walde-P. 1.415. Boisacq 505.
31504:Grk. xpavyétw, with sb. xpavyn ‘cry, shout’, perh.: ON hraukr ‘cormorant’ (but cf. Falk-Torp 866), Goth. hruk ‘crowing’, hrukjan ‘crow’, fr. *krau-g-. beside *krau-k- in ChSl. krukii ‘raven’, ete., *krau-k- in Skt. kruc-, Av. xraos- ‘ery, shout’, etc. (below, 7), all from parallel extensions of the root in Kpatw
31525:OE hrgman, ME reme, deriv. of OE hrgam, ME ream ‘cry, outcry, tumult’, cf. ON hrawmi ‘noisy fellow’, perh. : Skt. kdrava-, Lat. corvus ‘raven’, from an extension of the root seen in Grk. xpatw, kpavyatw, etc. (above, 1). Walde- P. 1.417. Walde-H. 1.275.
31544:eagle (‘scream’), raven (‘croak’), and birds in general, also the horse (‘neigh’), fawn, and even sounds made by worms and fish. The verbs for ‘sing’ frequently cover the cock’s ‘crow’ and several dif- ferent bird cries.
31549:4. ‘Croak’ (a of frog, b of raven or crow, the latter NE caw). Grk. xpatw (a, b), xpwtw (b), late Lat. coaxdre (a; > Fr. coasser), crécire (b; > Fr. croas- ser b, rarely a; form influenced by coasser), NE croak (a, b), NHG quaken (a; also ‘quack’ of ducks), kréchsen (b), Russ. kvakat! (a), karkat’ (b).
```


## [2026-09-06T16:21:54.693Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26025,26055p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-06T16:21:54.743Z] TOOL RESULT

```
cech. krakorati ,.gackern'‘ ( *kor-kor -, vgl. y.ogy.oQvyy, Berneker 571), 
krakor „Gegacker“, serb. krakoriti , gracillare'*', klr. kerekority ..kollern, 
girren“, (aber russ. chorochoritbsja ,.sich wichtig macheir' bleibt fern). 

Lit., auch zu den folgenden Erweiterungen, bei Curtius 5 153, Zupitza 
Gutt. 123 f . , Trautmann Apr. 356. S. auch qar- ,,laut preisen“. 

Mit Gutturale rweiter ungen: 

Auf -q (gebrochene Reduplikation) qerq -, qrcq -, qroq-: 

Ai. krkara-, krakara -, krkana- m. ,,eine Art Rebhuhn", krka-vaku- m. 
.Hahn' 1 , krkasd, krkalikd Yogelnamen : av. kahrka indecl. ..kikeriki!”, auch 
Bezeichnung des Hahnes, npers. kark ..Huhn ‘, av. kahrkasa- m. ,,Geier, 
eigentlich Hahneesser ‘; ai. karkati (unbelegt ) ,.lacht : ‘, krdksamana-, -kraksa-, 
-kraksin- etwa „knarrend‘, krakaca- m. ,.Sage“; 

arm. vielleicht aragil ..Reiher' c ( *qraq-l s. Pedersen KZ. 39, 343) und 
— mit im Schallworte steckender Lautverschiebung odor als Neuschopfung — 
karkac ,.pigolamento, Rauschen des Wassers, Gerausch“, karkacem ..strepi- 
tare, iibermaliig lachen, brausen" (Bugge KZ. 32, 52). 

Gr. xeQy.ai;' tega£ Hes., y.egxdg ' y.Qei- to oqveov Hes., xegy.iftaMg' sgmdiog 
Hes., y.EQxig • . . . eldog doviOog Hes., xegy.rog ' icon!;, y aiexTgvtbv Hes , 
xsgxog ■ . . . aXexxgvcbv Hes., xt'gxog ,.iegag-‘ (s. Boisacq 458 Anm. 1, Fick 
KZ. 44, 347), xogxogag' ogvig. TIegyatoi Hes., xoef ,,eine Yogelart’ 1 (siehe 
Boisacq s. v.'): xeoyvog . Heiserkcit ' (wenn aus *xe gx-ovog: oder mit idg.
```


## [2026-09-06T16:22:01.613Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"qer-\\|qor-, qr-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20; echo \"=== page tag ===\"; python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'kahrkasa- m. ,,Geier' in p or 'kahrkasa-' in p:\n        print('leaf',i, p[:200].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-06T16:22:03.281Z] TOOL RESULT

```
22281:von *sqer- „schneiden“ und *qar- „schmahen“, entbehrlich). 
22298:siehe aber qer- „brennen“ und Berneker 607 f., Feist Got. Wb. 145); ahd. 
22433:-s- versch. Erw. von qer- — sqer- „schneiden‘‘ seien, was aber dem Bed.- 
22463:auf ein altes Kebeneinander yon Anit- und Set-Basis zu schlieBen ( *qer-s : 
22466:erklaren, fehlt jede Notigung (Identitat mit qer-s- „furchen“ ist unerwiesen) ; 
25778:s. u. *sqer- „verschrumpfen“), Zupitza Gutt. 185 (Lit.), Hirt PBrB. 22, 232, 
25825:rich IF. 27, 142; Sommer IF. 38, 172: zu lat. curis ..Lanze"? sqer- 
25865:qer- 
25890:1. qer- ..harren, hoffen”? 
25898:2. qer- in Worten fiir ..Kornclkirsche, Kirsche - . 
25931:qer-, qar qer-, qCr- 
25950:146 f., wonack vielleicht zu (sqer- „schneiden‘; was ist das bei Osten- 
25955:3. qer-, qar- „greifen; Griff, Handhabe"?? 
25958:Pfropfreis" usw. (doch wohl zu sqer- ..schneiden' - ), ai. karna- m. „Ohr, 
25963:4. (qer-?) qor- „hangen, hiingen". 
25969:wenn ursprgl. ,.vorgehiingter Futtersack", s. u. sqer-, sqcret- „schneiden‘‘). 
25970:Hochst fraglich ags. heurr, aisl. hjarri ,,Tiirangel ' (s. u. sqer- ..springerr). 
25987:qer-, qers- — ter-, kor-, kr- 
25993:5. qer-, qers- „Locke“? 
25997:..Strauch“ s. u. *qer- „Kornelkirsche“; lit. karciai , Mahne“, Zupitza Gutt. Ill, 
=== page tag ===
leaf 421                                                                          qer-, qers-         —       ter-, kor-,              kr-                               413 |  | 5. qer-, qers-
```


## [2026-09-06T16:22:09.510Z] TOOL CALL #57: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T16:22:09.516Z] TOOL RESULT

```


```


## [2026-09-06T16:22:12.913Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D9%81%D9%87",
 "prompt": "What does the Persian entry سرفه say — meaning, etymology, Middle Persian ancestor, PIE root? Quote the etymology section."
}
```


## [2026-09-06T16:22:14.522Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D9%88%D8%B3",
 "prompt": "Persian entry خروس: meaning and etymology — Middle Persian, Avestan, Proto-Iranian forms, and any note about Parthian vs Southwest forms. Quote it."
}
```


### [2026-09-06T16:22:16.806Z] TOOL RESULT

```
Based on the Wiktionary page provided, the Persian entry **سرفه** (sorfe) means **"cough"** as a noun.

However, the page does not contain an etymology section. There is no information provided about the etymology, any Middle Persian ancestor, or PIE root for this word. The entry only includes alternative forms, pronunciation guides for different Persian dialects, and a derived term (سرفه کردن - sorfe kardan).
```


### [2026-09-06T16:22:19.959Z] TOOL RESULT

```
# Persian Entry: خروس (xurōs)

## Meaning
The word means "rooster" or "cock."

## Etymology
According to the Wiktionary entry, the term derives from Middle Persian: "From Middle Persian \[script needed\] (hlws /⁠xrōs⁠/, 'cock', literally 'the caller'), from \[script needed\] (hlwstn' /⁠xrōstan⁠/, 'to call, to cry')."

The etymology traces the word's origin to a Middle Persian root meaning "to call or cry," reflecting the bird's characteristic vocalization.

## Note on Script Forms
The entry indicates that Middle Persian native script forms are not provided in this Wiktionary article (marked as "[script needed]"), showing gaps in the documentation of earlier Persian attestations. No specific Avestan or Proto-Iranian forms are included in the available content.
```


## [2026-09-06T16:22:31.955Z] TOOL CALL #60: WebSearch

```json
{
 "query": "سرفه ریشه‌شناسی حسن‌دوست فارسی میانه srafag Proto-Iranian cough etymology"
}
```


## [2026-09-06T16:22:32.969Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/raven",
 "prompt": "Give the etymology of raven (bird) and any PIE root cited; also note if rook, cricket, scream, screech are linked to the same imitative base."
}
```


### [2026-09-06T16:22:39.112Z] TOOL RESULT

```
# Etymology of Raven (Bird)

**Etymology Chain:**
Late Old English *ræfen* derives from Proto-Germanic *khrabanaz*, which traces to a PIE root that is "imitative of harsh sounds."

**PIE Root:** The source material notes connections to Latin *crepare* ("to creak, clatter"), *corvus* ("raven"), Greek *korax* ("raven"), and Old Church Slavonic *kruku* ("raven")—all representing onomatopoetic origins mimicking harsh vocalizations.

**Related Words:**
The document confirms that **rook** shares this etymological lineage, as Old English *hroc* ("rook") derives from the same Proto-Germanic and PIE base. However, **cricket, scream, and screech** are **not mentioned** in the provided content as linked to this imitative base, so I cannot confirm their connection based solely on this source.

The raven entry specifically emphasizes the word's imitative character: the root reflects "harsh sounds" produced by the bird itself, making the etymology fundamentally onomatopoetic in nature.
```


### [2026-09-06T16:22:40.288Z] TOOL RESULT

```
Web search results for query: "سرفه ریشه‌شناسی حسن‌دوست فارسی میانه srafag Proto-Iranian cough etymology"

Links: [{"title":"سرفه به انگلیسی - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatoen/%D8%B3%D8%B1%D9%81%D9%87/"},{"title":"فرهنگ ریشه‌شناسی فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%B3%DB%8C_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"فرهنگ ریشه‌شناختی فارسی، محمد حسن‌دوست، 1393 تهران، فرهنگستان زبان و ادب فارسی، دورۀ پنج جلدی","url":"https://lsi-linguistics.ihcs.ac.ir/article_1976.html"},{"title":"فرهنگ ریشه‌شناختی زبان فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C_%D8%B2%D8%A8%D8%A7%D9%86_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"محمد حسن‌دوست - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%85%D8%AD%D9%85%D8%AF_%D8%AD%D8%B3%D9%86%E2%80%8C%D8%AF%D9%88%D8%B3%D8%AA"},{"title":"شبکۀ ریشه‌شناسی","url":"https://t.me/s/shabakeh_risheshenasi"},{"title":"محمد حسن دوست نویسنده کتاب فرهنگ ریشه شناختی زبان فارسی(5جلدی) | ایران کتاب","url":"https://www.iranketab.ir/profile/23034-mohammad-hasandust"},{"title":"فرهنگ ریشه‌شناختی زبان فارسی | راهک","url":"https://raahak.com/?p=942"}]

I found search results related to your query. The results focus on محمد حسن‌دوست's Etymological Dictionary of Persian (Farhangi Risheshenaakhti Zabani Farsi), published in 2015 in five volumes by the Persian Language and Literature Academy.

Regarding the specific etymology of "سرفه" (cough), the search results indicate some discussion about its origin. The word سرفه derives from the Persian root سرف, though there appears to be some scholarly discussion about whether it relates to other roots.

Additionally, linguistic variants of this word that are phonetically closer to the English "cough" are found more frequently in dialects and languages of western and southwestern Iran, suggesting there may be variations across different Iranian dialects and languages.

However, the search results do not contain detailed information about the Middle Persian "srafag" or Proto-Iranian connections to cough that your query mentions. For more specific etymological details connecting these historical language stages, you may need to consult Hasandoost's full etymological dictionary directly or specialized academic sources on Proto-Iranian linguistics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T16:22:45.347Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor w in ['سرفه','خروس','کرکس','کروه']:\n    print('==',w)\n    for i,p in enumerate(pages):\n        if w in p:\n            print('  leaf',i)\nEOF"
}
```


### [2026-09-06T16:22:49.340Z] TOOL RESULT

```
== سرفه
  leaf 361
== خروس
  leaf 236
  leaf 237
== کرکس
  leaf 400
== کروه
```


## [2026-09-06T16:22:52.350Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,w in [(361,'سرفه'),(236,'خروس'),(400,'کرکس')]:\n    p=pages[i]\n    j=p.find(w)\n    print('==== leaf',i,w)\n    print(p[max(0,j-700):j+900])\nEOF"
}
```


### [2026-09-06T16:22:53.888Z] TOOL RESULT

```
==== leaf 361 سرفه
0۸71 1 571۷1838771
۱ یرنانی: (075680): 0 ‎ ..‏ لنونی (لتی) (791۵۸هل): اد ان
ا لاتین (770مل): 8 ,818110 ایرلندی کهن (نلکلقا ۵ا0م: 887 ,8۸7136
قراس (ت۳607): اد ‏ ان ولزی (۶55/0): ۲77۲۷33 07۷۷۷7138
اسپانپایی (5۳۸7/5): وا 8 ان برترنی (87610/7): ار رارا ‏ بی

گریکه. (00777/0): یراگن ین

انگلیسی کهن (نقکل8(/0 012): 51۷86107 پسگشت‌ها ارت بت دنا
اسلاوی کهن. (5۸4۲//0 6240074 طا۵): 2 ,1040-1041 ۰ :۶07070
71 5۷187۸7 7 (81571-3) 0
لهستانی (۷0/50: ۰ 8181۸6 ,5۷181 لفت‌نامه دهخدا: ۱۳۸۳
چکه (280): ان فرهنگ معین : ۹۳۴

یادداشت:

9 (صفحه‌ی ۱۰۴-۴۱) می‌گرید واژه‌ی فارسی نوین "سفلیدن" يا "سبفلیدن" (8171,18880) نیز از همین
ْ واجریشه است ولی این واژه را در هیچ کدام از فرهنگه‌ها نیافتم. شاید منظورش "سرفیدن" به چم "سرفه کردن" باشد
۱ (لغت نامه دهخدا: ۱۳۹۰۸)

و یی
ِ

ا
۱ اوستایی (/487۵2): بلوچی (2171ل8۸): 517811۸671 ,بش81
ا 800۳1 ,85۸007771 افقانی (پشتر) (//4۳0۸): بل۸ل5 م832۸
۱ پهلری (۲7مانله): 9021510 ,8027۸0 سانسکریت (5/8077):

اوستی (0858776): ,ااتاژه5 1 ات80
کردی: (۳)8015): لااران
سا را

==== leaf 236 خروس
[pdf page 237]
۸ | خروس
۲- 0311008 ریشه‌ی واژه‌های ژرمنی این فهرست را انامعلوم" می‌نامد (۸/103177(:0011075) 875)
۳ چم این واژه در همه‌ی وازه‌های اين فهرست (به جز اوستایی و پهلری): "تن "» "پدن"
اوستایی (487424)+ صربی (85781۸/۷): 7 0802
۸85 ,6۸7۸7 13تفط ,28۸05 بوهمی (8072111401): 0
پهلوی (41اتل۸ه): 205 لیتوانی (14(۷/لهلا27 7 85قاتاتاه۶ ۴
کردی (ل68/5): 005 پروسی کهن ((554ن2۸ صا0): ۰ 3360
بلرچی (الل۲لاملم8): 08 ایرلندی کهن (5/7ل# صان):
سانمکریت (5۸(/57): 6 ,0
۸ ش836۸ برترنی (/87270): 0 ,106
یونانی 0765/0): 0 ,ک۸ظ ۴
لاتین میانه (/710ما ۵/1022: ۰ ۲۵۴۸ پسگشت‌ها 5
فرانسه (ل۳88(6): 00 1 ۶0806
رومانی (۸(/1۷انا#): ناه اه 5 (۵م)) :8/37
نورس کهن (۸۷0#85 0ا0): 3 را 0 (۲00) :ما۲۸
انگلیسی کهن (5لا2۸0 ا0): +۰0 7 (۴۱۵) :2 05(/2 ۸/۸
انگلیسی (6۸707/8): ‎٩‏ دراه 16 لاه
اسلاوی کهن (2/زمل5 7ل86ابا» 0ا0): 6 (۲۱۵) 0۱0۸8۰
07 8 (۲۱) معاو
لهستانی (/۳0./8): 7 برهان قاطع : ۷۴۱
روسی (851۸(۷/#): ۸
یادداشت:
۱- 88۸7 , 0810818 معتقدند که ای
==== leaf 400 کرکس
غانی (پشت) (47017۸427)+ نا اسلوا کی (8101۸20): هه
تخاری ۸ (۸ للم ۰:70 8۸۲۵0 لیتوانی (/(۵4ا07فتا777).
سانسکریت (54/577): 0 ت30
۷6۰ کته دنله شنز لترنی (لتی) (7۲1۵/۷ا):
ارمنی (47ا۸7/87): ننشای ۱ 7 203۵۳
بونانی (072510): کید اه پروسی کهن (انفاکدت۲۸ صامم): ۸۲70
لانین (4700ه): ‏ 0۸88 ,ق0830 ایرلندی کهن (577ل8[ )+ جتفی
ایسلندی کهن (/70770(ی5 صران):

۸ ,6 ها پسگشت‌ها شک در
انگلیسی کهن (2۷60880 صا0): 17816۸01 8 وم
انگلیسی (877لا5(70): ۴ 0 (۸136) با
دانمارکی (0۸(71873): دای ۱ 9 (۸33) 2
سوئدی (8750157): 16۸ 8 (816) :00/5
نروژی (۵/08۳8007: ۸1۲618 ,81۳65 0 (16) :57
ملندی (007777)+ نداد یلا۱4 لغت‌نامه دهخدا: ۱۸۳۷۳
اسلاوی کهن (4۲76ا5 7ل#ناتن) طام): پرهان قاطع : ۱۶۳۲

زان ناد ۱
یادداشت: :
۱ واژه‌های فارسی "کرکس " و اوستایی 1۸11816۸8۸ و سانسکریت 1678۸8۸ نیز از همین واجريشه آمده‌اند.
۲- چم این واژه در زبان پهلوی: قرقاول
چم این واژه در زبان‌های غیرایرانی و غیرهندی: غرید» غدغد کردن» صدای قورباغه ایجاد کردن. :
```


## [2026-09-06T16:23:06.544Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[361][:1400])\nprint('----- leaf 400 head')\nprint(pages[400][:700])\nEOF"
}
```


### [2026-09-06T16:23:08.093Z] TOOL RESULT

```
[pdf page 362]
۹
سرت (به چم "صفیر") / ۳۶۳
یادداشت: َ

۱- برخی پسگشت‌ها واژه‌ی انگلیسی 13۸818127 و همربشه‌های ژُرمنی آنرا نیز از همین واجريشه می‌دانند.

۲ پازگشت به: آس؛ آسمان,

سانسکریت (5(/57/7): لیترانی (/(ا 77۸27 لا).
َ 71 5۷80۸71 1 571۷1838771
۱ یرنانی: (075680): 0 ‎ ..‏ لنونی (لتی) (791۵۸هل): اد ان
ا لاتین (770مل): 8 ,818110 ایرلندی کهن (نلکلقا ۵ا0م: 887 ,8۸7136
قراس (ت۳607): اد ‏ ان ولزی (۶55/0): ۲77۲۷33 07۷۷۷7138
اسپانپایی (5۳۸7/5): وا 8 ان برترنی (87610/7): ار رارا ‏ بی

گریکه. (00777/0): یراگن ین

انگلیسی کهن (نقکل8(/0 012): 51۷86107 پسگشت‌ها ارت بت دنا
اسلاوی کهن. (5۸4۲//0 6240074 طا۵): 2 ,1040-1041 ۰ :۶07070
71 5۷187۸7 7 (81571-3) 0
لهستانی (۷0/50: ۰ 8181۸6 ,5۷181 لفت‌نامه دهخدا: ۱۳۸۳
چکه (280): ان فرهنگ معین : ۹۳۴

یادداشت:

9 (صفحه‌ی ۱۰۴-۴۱) می‌گرید واژه‌ی فارسی نوین "سفلیدن" يا "سبفلیدن" (8171,18880) نیز از همین
ْ واجریشه است ولی این واژه را در هیچ کدام از فرهنگه‌ها نیافتم. شاید منظورش "سرفیدن" به چم "سرفه کردن" باشد
۱ (لغت نامه دهخدا: ۱۳۹۰۸)

و یی
ِ

ا
۱ اوستایی (/487۵2): بلوچی (2171ل8۸): 517811۸671 ,بش81
ا 800۳1 ,85۸007771 افقانی (پشتر) (//4۳0۸): بل۸ل5 م832۸
۱ پهلری (۲7مانله): 9021510 ,8027۸0 سانسکریت (5/8077):

اوستی (0858776): ,ااتاژه5 1 ات80
کردی: (۳)8015): لااران
سا را

----- leaf 400 head
[pdf page 401]
اک 66666
۲ | کرک (به چم *مرغ خانگی») ۱
اوستایی (47887/07): کرد ناه روسی ((8/5514): ۳8۵۲ ,۳3۵0175110 رین
پهلری (7شاتلمم): ۸ چک (2507)). ها ده 0:۱
اوستی (05587/6): ۸۴ بلناری (8004۵(۷7): 00
: کردی (70157): 8 نها صربی (52/810): هار
آفغانی (پشت) (47017۸427)+ نا اسلوا کی (8101۸20): هه
تخاری ۸ (۸ للم ۰:70 8۸۲۵0 لیتوانی (/(۵4ا07فتا777).
سانسکریت (54/577): 0 ت30
۷6۰ کته دنله شنز لترنی (لتی) (7۲1۵/۷ا):
ارمنی (47ا۸7/87): ننشای ۱ 7 203۵۳
بونانی (072510): کید اه پروسی کهن (انفاکدت۲۸ صامم): ۸۲70
لانین (4700ه): ‏ 0۸88 ,ق0830 ایرلندی کهن (577ل8[ )+ جتفی
ایسلندی کهن (/70770(ی5 صران):

۸ ,6 ها پسگشت‌ها شک در
انگلیسی کهن (2۷60880 صا0): 17816۸01 8 وم
انگلیسی (877لا5(70): ۴ 0 (۸136) با
دانمارکی (0
```


## [2026-09-06T16:23:24.838Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sarfa\\|surfa\\|sarafa\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-06T16:23:24.882Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:23:27.914Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"npers\\.\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | sed -n '1,200p' | grep -in \"husten\\|sarf\\|krep\" ; echo \"---krp---\"; grep -n \"krpate\\|Husten\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-06T16:23:27.982Z] TOOL RESULT

```
---krp---
26284:krahe“, kraukat ..husten, Schleim auswerfen (vom Vieh) u , krauka ..Husten, 
31902:Ai. kasatc „hustet“, kasa- m. „Husten“; lit. kosiu, -eti „husten“ = lett. kuset 
31903:ds , lit. kosul[/s „Husten“, lett. kasa, kusis, gew. kasus „Husten“ kasl'i „Stick- 
31905:russ. kasch (usw., s. Berneker 493) „Husten“; alb. (G. Meyer BB. 14, 54, 
31906:EW b. 195, kale f. ( *kosh ) „Husten“, kolem „buste“; a.gs.hwustii, ahd .hwuosto, 
31907:huosto, aisl. hdsti m. „Husteu“. Mir. casachtach „Husten“, cymr. pas (qlias-to-),
```


## [2026-09-06T16:23:31.683Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26290,26340p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-06T16:23:31.733Z] TOOL RESULT

```
mit Geminata -kk- dan. skrukke ,.glucksen“ (Holthausen aaO., Falk- 
Torp s. v.), skrokke ..plaudern - , woneben alter dan. krokke ..rufen, von 
Hiihnern“, mnd. krochcn ..grunzen; heiser schreien (vom Raben)”. 

Ai. krogati , av. xravsaiti „kreischt, schreit ‘, ai. kroca- m. Schrei, Ruf- 
weite“, npers. (Horn Np. Et. 106) x tiros „Hahn‘. 

Gr. xgavyt] „Geschrei ', xgavyog ' dgvxokdjiTov eldog Hes. (ware lautlich 
= anord. hraukr ..Seerabe, graculus cristatus", z. B. wieder Fick KZ. 43, 
144; doch wird letzteres von Falk-Torp u. raage II mit anord. hraukr 
..kegelformiger Haufen" gleichgesetzt) ; got. hruk Acc. ,,das Krahen“, hruk- 
jan „krahen‘. 

Dentalerweiterungen: 

Gr. xogvCa , Schnupfen" : anord. kridta ..knurren, schnarchen, brummen", 
ags. hrutnn ..schnarchen, schnauben“, ahd. ruffian, ruffim ..rasseln, schnar- 
chen, 8ummen“, ags. hrot m. ,.dicke Fliissigkeit, Schleim“, ahd. (h)roz, 
mhd. roz , rotz ( hrutta -), nhd. Rotz ; mnd. schriiten ..schnarchen, sclinaufen, 
prusten“, wfal. Schrute „Truthenne“ schwed. skryta .prahlen"; mdartl. 
..schnarchen", norw. mdartl. skryla ..schnauben, prusten“, dan. sAri/ifr ..prahlen, 
schreien (vom Esel)", alter dan. ..poltern, briillen, schreien, schnarchen", 
norw. mdartl. skrola ( *skrutun ) ..prahlen” (vielleicbt auch anord. skraut n. 
; ,Pracht, Schmuck", skreyta ..sclimiicken", wenn eigentlich ..Prahl vgl. 
norw. skrjyta , sclimiicken, loben, groBsprechen, prahlen”, rfiytn ds.X 

Hit idg. -t- anord. hrydja ,,Spucknapf , isl. lirodi ..Speichel", norw. 
mdartl. rydu, skiyda f. „Schleim im Halse"; fern bleiben, da mit anlaut. r-, 
ahd. rudo , ags. rop, ryppa .Riide‘‘. 



418 


ker- 


Ygl. Pick I 3 540, I 4 393, Zupifcza Gutt. 208, Hirt Abl. 114, 118, Fick 
III 4 107, 475, 573, Falk-Torp u. skryde. 

Xicht wahrscheinlicher iiber y.ogv^a, Rotz Liden Stud. 51. 

2. ker- „brennen, glfihen, heizen". 

Ai. kudayati ,.sengt" (' *kr-d -, d. i. *k e ro-d-, s. u. km- ..anzfinden 11 , nasa- 
liert kundayati „brennt -1 ); lit. kuriu , kiirti ,,heizen‘, kurenti ,.fortgesetzt 
heizen", kiirstyti .schfiren 1- , lett. kuru ( kurstu (*, hurt, frequent, kursltt, kuri- 
ndt ..heizen”, aksl. kurjq, kuriti sc „rauchen : , kurentje „Kohlenfeuer" usw. 
(J. Schmidt Yok. 332, 458, Zupitza Gutt. 114, Yf. LEWb. 2 u. carbo; Ber-
```


## [2026-09-06T16:23:39.566Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26180,26230p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-06T16:23:39.647Z] TOOL RESULT

```
liraban , hram ,,Rabe“ mhd. auch rappe ), as. naht-ram , Nachteule - (Ilolt- 
hausen KZ. 27, 623, Persson Wzerw. 50, Zupitza Gutt. 23, Fick III 4 103, 
Uhlenbeck PBrB. 26, 305, gegen Ilirts PBrB. 23, 306 Gdf. *yrdmno-). 

Isl. skrdfa „einen scharrenden Laut geben, rasseln - ', anord skrafa 
. schwatzen -- , skraf ;und skrap s. u.) n. ,,Geschwatz“ ; anord. skarfr ..See- 



416 


ker-, kor-, kr- 


rabe i£ , ags. scroef ds., ahd. scarba, scarva f., scarbo m. ds., nhd. Scharbc 
(Pick III 4 457). 

Lett, krepet , krepet „schmutzig werden“, krepat ,,zahen Schleim auswerfen" 
(aus ,.*rauspern"; vgl. gr. y.onv'Qa usw. bei der w-Basis), lit. sknplenti ds., 
lett. krepalas PI., lit. skreplial PI. „Schleimauswurf £ , aksl. kropljq , kropiti 
,.bespritzen, besprengen" usw., russ. kropoiafa .,brummen, miirrisch sein, 
sich sorgen" usw. (s. Liden Stud. 51, Berneker 622 f.). 

Mit b: lit. skrebeti „rascheln £ , aksl. skrobotz „Gerausch“, anord. skrap 
,,das Rascheln, Geschwatz", skrapa ..rascheln, schwatzen" (Lit. unter qar- 
..laut preisen", wo auch iiber got. hrops „Geschrei' £ usw.). Nasaliert gr. 

y. QepfSaka ,Ivastagnetten ££ (Boisacq s. v.). 

i-Basis ( s)q(e)rei 

Lat. vielleicht (s. Yf. LEWb. 2 s. v.) crimen , wenn ursprgl. „das Gesehrei, 
mit dem man seinen Schadiger beschuldigt" (mogliche Gdformen *hl-men, 
-k-(s)men, -g-(s)men)-, ahd. as . scrlan „schreien' £ , ahd. screi n. ..Schrei", nd. 
schrewen , ndl. sclireeuwen ,.schreien £ ( *skraiwian ), wflam. schreemcn , engl. 
scream ds. ( *skraimian ), anord. hrehnr ; ,Geschrei", anord. hrina „schreien ££ 
(vom Schweine), vgl. lett. krina „Sau ££ (ebenso ir. crain ds. : lat. crocio). 

Ygl. Muhlenbach-Endzelin Lett.-D. Wb. II 279. 

Aber lat. screClre ,.sich rauspern" (Zupitza Gutt. 158, Fick III 4 47 1 ) trotz 
norw. mdartl. skroea ds. nicht hierher, sondern zu sqer-, sker- ? ,.Ausschei- 
dung ££ , s. d. 

Gutturalerweiterungen: 

Gr. y.oixE ..(das Joch) knarrte, kreischte"; lit. kryksciit , kri/ksti „krei- 
schen", kryksztauti ,,schreien, kreischen, jauchzen ££ , krikseli ,.quaken“; aksl. 
krih, ,, Gesehrei 1 , kricati schreien '; anord. hegri, ags. hragra, ahd. heigaro 
und (Ji)reigaro, mhd. heiger und reiger, nhd. Redier ( *kroikro *krikro-,
```


## [2026-09-06T16:23:54.290Z] TOOL CALL #69: Bash

```json
{
 "command": "ls site/pages/257.jpg 2>/dev/null || pdftoppm -f 257 -l 257 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg257 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T16:23:55.965Z] TOOL RESULT

```
site/pages/257.jpg
total 11704
drwx------ 7 sfmqrb sfmqrb    4096 Sep  6 12:23 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    1276 Sep  6 12:21 agents.txt
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
-rw-rw-r-- 1 sfmqrb sfmqrb    4259 Sep  6 12:13 c250_celare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7170 Sep  6 12:13 c250_kolba.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4529 Sep  6 12:13 c250_sarez.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8664 Sep  6 12:19 c255_french2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6147 Sep  6 12:19 c255_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23626 Sep  6 12:19 c255_latin2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18287 Sep  6 12:20 c255_latin3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3398 Sep  6 12:19 c255_latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb   26231 Sep  6 12:18 c258_kars.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53453 Sep  6 12:18 c258_n2.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    2064 Sep  6 12:21 crop_cheek2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1888 Sep  6 12:21 crop_cheek.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb  111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3215 Sep  6 12:21 crop_p3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb     724 Sep  6 12:11 drive.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4491 Sep  6 12:13 fix.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   49868 Sep  6 12:23 mk251.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:52 p233
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 p245
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:21 p249
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
-rw-rw-r-- 1 sfmqrb sfmqrb  123419 Sep  6 12:13 pg250hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89076 Sep  6 12:13 pg250.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75263 Sep  6 12:04 pg251.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74772 Sep  6 12:13 pg252.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68850 Sep  6 12:14 pg253.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71025 Sep  6 12:13 pg254.png
-rw-rw-r-- 1 sfmqrb sfmqrb  148813 Sep  6 12:19 pg255hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55906 Sep  6 12:13 pg255.png
-rw-rw-r-- 1 sfmqrb sfmqrb  171848 Sep  6 12:21 pg256_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83469 Sep  6 12:20 pg256.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81240 Sep  6 12:17 pg258.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66128 Sep  6 12:23 pg259.png
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 __pycache__
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   53545 Sep  6 12:03 w241.py
```


## [2026-09-06T16:23:58.567Z] TOOL CALL #70: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/257.jpg"
}
```


### [2026-09-06T16:23:58.589Z] TOOL RESULT

```

```


## [2026-09-06T16:24:13.837Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cricket",
 "prompt": "Etymology of cricket (the insect): Old French criquer, Germanic imitative origin? Quote it."
}
```


## [2026-09-06T16:24:14.877Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%B1%DA%A9%D8%B3",
 "prompt": "Persian کرکس: etymology — Middle Persian, Avestan kahrkāsa, components? Quote the etymology."
}
```


### [2026-09-06T16:24:18.151Z] TOOL RESULT

```
# Etymology of Cricket (the Insect)

According to the Online Etymology Dictionary, the insect sense of "cricket" derives from Old French origins with imitative roots:

"from Old French _criquet_ 'a cricket' (12c.), from _criquer_ 'to creak, rattle, crackle,' of echoic origin, with a diminutive suffix"

The source notes that while the French word appears to have Germanic connections, the underlying basis is onomatopoetic—the term essentially mimics the sound the insect produces.
```


### [2026-09-06T16:24:21.106Z] TOOL RESULT

```
# Etymology of Persian کرکس (karkas)

Based on the Wiktionary entry, here's the etymology:

The word derives from **Middle Persian** (klkʾs /kargās/, "vulture"). It's cognate with **Avestan** 𐬐𐬀𐬭𐬐𐬁𐬯𐬀 (karkāsa, "vulture").

**Key quote on the literal meaning:**
> "Literally 'hen-eater', from the term underlying Persian کرک (kark, 'hen') and Proto-Indo-European *h₁ed- ('eat')."

The word also has cognates in Classical Syriac, Biblical Hebrew, and Elamite—all referring to vultures or related meanings. The Proto-Indo-European root *h₁ed- means "eat," which combines with the Persian root for "hen" to create this descriptive compound etymology.
```


## [2026-09-06T16:24:30.313Z] TOOL CALL #73: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/خروس' --note 'page 257, root Ker 3, node 3: Persian xurōs etymology (MP xrōs \"the caller\" < xrōstan)' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/سرفه' --note 'page 257, root Ker 3, node 7: Persian sorfe \"cough\" — entry has no etymology section' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/کرکس' --note 'page 257, root Ker 3, node 5: Persian karkas < MP kargās, Av. kahrkāsa \"hen-eater\"' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/raven' --note 'page 257, root Ker 3, nodes 10-11: raven/rook from PIE imitative base' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/cricket' --note 'page 257, root Ker 3, node 11: cricket < OFr criquet, criquer \"to creak\", echoic' 2>&1 | tail -3"
}
```


### [2026-09-06T16:24:34.490Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/46262a8b54bc09bf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cebb617abe547a32.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6ec7f77bdb69ced1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6a6c85e1cc61a77c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7c1b6eb6b86351b5.txt
```


## [2026-09-06T16:24:44.959Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--SKT--\"; grep -n \"^Scream\\|^Screech\\|^Rook\\|^Raven\\|^Cricket\\|^Ring, \" SKT.txt | head -20"
}
```


### [2026-09-06T16:24:45.055Z] TOOL RESULT

```
--SKT--
15673:Raven  (I),  a  bird,  (E.^  ME.  r« A.  S.  krtrfn^  Ari^w.+Do.  rttaf.  \tx\.  k^i Dan.  ravH,  G.  raSe.  Nameo  from  m  c cf.  L.  crifarr,  to  rattle.     tV  KR  A  P  j
15674:Raven  (a\  to  plunder,  devour,  Ravi Ravish ;  see  Rapid.
16174:Rook  (3),  a  distaff.  (Sand.)   ted. Swed,    rvck,  Dan.   t^    a    distaA.  4 rocken.
16203:Rook  (3),  a  castle,  at  chess.  (F.-Pcrs.) M.  E.  rook.  —  Y.  rw-.^Pen.  rekhf  a  rook. Said  to  have  meant  *  warrior.'
```


## [2026-09-06T16:24:45.663Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--ISS carkas--\"; grep -n \"carkas\\|crk\\|kahrkasa\" ISS_alt_DKS.txt | head -15"
}
```


### [2026-09-06T16:24:45.816Z] TOOL RESULT

```
--ISS carkas--
```


## [2026-09-06T16:24:54.795Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'Raven  (I),  a  bird' in p:\n        print('leaf',i,'printed',i-20)\n    if 'Scream' in p and 'Screech' in p:\n        print('scream leaf',i,'printed',i-20)\nEOF\necho \"--HENNING--\"; grep -n \"crks\\|carkas\" HENNING_selected_papers.txt | head -5"
}
```


### [2026-09-06T16:24:56.609Z] TOOL RESULT

```
leaf 417 printed 397
scream leaf 445 printed 425
--HENNING--
```


## [2026-09-06T16:24:59.060Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==446' SKT.txt | grep -i -A3 \"scream\\|screech\" | head -20"
}
```


### [2026-09-06T16:25:00.889Z] TOOL RESULT

```
Scratch.  (Scand.)  Due  to  the  con- fuiion  of  M .  E  skralten,  to  scratch,  with M.  E.  craccken,  to  scratch.  p.  M.  E. skratten  stands  for  skarten  •,  an  extended form  from  \ccXisker-a,  to  shear,  cut,  and means  'to  cut  slightly,'  to  scrape.  The word  scmpe  is  a.  similar  formation  from  the same  root  SKAR,  to  cut;  see  Shear,  y* M.  E.  cracchen  stands  for  kraisen  *.  ~  Swed. kratta,  lo  scrape,  krats,  a  scraper.- Swed. kratfa,  to  rake,  scrape ;  from  a  base  K  A  KT, on  extension  of  V^^^^*  ^^  cut.  6.  The roots  SKAR  and  KAR  are  identical;  cf. Gk.  Ktiptiv,  to  shear,  A.  S.  sceran ;  see Shear.  And  see  Qrata  (i). ScrawL  (E  1  A  contraction  of  scrabbh, to  write  carelessly,  which  see  under  Sharp. %  Confused  with  M.  E.  scrau/en,  to  crawl, a  form  of  cmwl  with  prefix  j  ( —  O.  F.  «• —  L.  ex)  used  with  an  intensive  force. Scream.  (Scand.)  M.  E  teremrm,  - \cc\.skrama,  Swed.  skrHma,  Dan.  skmmme, lo  score  ;orig.  to  cry  aloud.  Cf.Swed.j<tr<i«, a  scream.  Allied  to  Soreeoh  and  Shriek. Screech.  (Scand.)  M.  £.  teriken.^ Iccl.  sAnekj'a,  to  shriek,  Swed.  jkrika,  to shriek  ;  Dan.  skrigt.  4-  Gael,  sp^aek,  to shriek ;  \i .  ytgrecHio,  to  scream.
ahriok.  (Scand.)  Another  form  of screech  ;  from  M,  E.  scriken  (above).
shrike,  the  bntcherbird,  (Scand.)  Icel. tkrikja^  a  shrike,  lit.  'shrieker.*  —  Icel, skrikja,  to  titter,  orig.  to  shriek,  and  allied to  Iccl.  skrak/a  (above), Screeo.  (K.-Teut)  M,  E,  irmni.- OL  F.  escran,  'a  skrecn.'  Cot.  (Mod.  F. ^ran.)  Derived  by  Diex  from  G-uAragen, a  trestle,  stack  of  wood ;  cf.  also  G. uhranne,  a  railing,  schranke,  a  barrier. p.  In  the  sense  of  '  coarse  sieve/  it  is  the same  word  ;  so  called  because  it  screens  (or wards  off)  th«  coarser  particles,  and  pjre- vcats  them  from  comini;  through.
430
SCREW,
```


## [2026-09-06T16:25:09.248Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ring,  intr\\|^ring,  tr\\|hringan\" KLN_1966.txt | head -5"
}
```


### [2026-09-06T16:25:09.291Z] TOOL RESULT

```
32943:Derivatives:  ring,  tr.  and  intr.  v.,  to  encircle, ring-ed,  adj.,  ring-er,  n.,  ring-ing,  n.,  ring-less, adj.,  ring-let,  n.,  ring-Iet-ed,  ring-let-y,  adjs. ring,  intr.  v.,  to  sound;  tr.  v.,  to  cause  to  sound. —  ME.  ringen,  fr.  OE.  hringan,  rel.  to  ON. hringja,  Swed.  ringa,  MDu.,  Du.  ringen;  of imitative  origin.
39152:throng,  n.,  crowd.  —  ME.  throng,  fr.  OE.  prang, geprang,  ‘crowd,  tumult’,  rel.  to  ON.  prong,  Du. drang,  G.  Drang,  Gedrange,  ‘crowd,  throng’, OE. pringan, OS.  thringan,  ON. pryngva,  ‘to  press on,  crowd’,  Du.  dringen^to  push’,  OHG.  dringan, MHG.,  G.  dringen,  ‘to  press  on,  crowd’,  MHG. dringen,  ‘to  press  round  a  prince  at  court’,  Goth. preihan  (for  *prinhan),  ‘to  oppress’,  and  cogn. with  Avestic  draxtanam  (gen.  pi.),  ‘of  those pressed  together’,  Lith.  trenkiu,  trehkti,  ‘to  push, jolt’.
```


## [2026-09-06T16:26:53.007Z] TOOL CALL #79: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T16:26:53.049Z] TOOL RESULT

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


## [2026-09-06T16:26:58.896Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if \"gehort zu surfe\" in p or \"gehört zu surfe\" in p or \"surfe 'Husten'\" in p:\n        print('leaf',i,'printed',i-21)\nEOF"
}
```


### [2026-09-06T16:27:00.936Z] TOOL RESULT

```
leaf 184 printed 163
```


## [2026-09-06T16:33:50.108Z] TOOL CALL #81: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-257.json",
 "content": "{\n  \"pdf_page\": 257,\n  \"book_page\": 227,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ker 3, Qer, Qor, Qr\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ker-, *kor-, *kr- (Pokorny 'ker-1'; Walde-Pokorny 'qer-, qor-, qr-'; Watkins/AHD 'ker-2'), an echoic base for hoarse cries and for the birds that make them\",\n      \"note\": \"The root box is exactly right. Pokorny IEW 567-571 heads the entry 'ker-1, kor-, kr-' with the meaning 'a kind of sound (hoarse shrieking, etc.), *crane', and notes 'anlaut mostly k-, rare ḱ- also with moveable s-: (s)ker-' — which is what licenses the s- of Persian sarfa in node 7. Nourai's page reference POK:567 is the first page of that entry, and the four names in his box are not his invention: Walde-Pokorny I 413ff. print the lemma with q for k ('qer-, qor-, qr-'), and Klein (p.1305, s.v. raven) writes 'I.-E. base *qer-, *qor-, *qr-, imitative of harsh sounds'. Watkins/AHD heads the same material 'ker-2. Echoic root, base of various derivatives indicating loud noises or birds. [Pok. 1. ker- 567.]', so the gloss 'loud noise, noisy birds' is a fair rendering of both. Cross-cutting caveats for the page: (a) Cheung 2007 (*xraus, no. 449) accepts the Indo-Iranian root but says an IE provenance for it 'cannot be established', so the Avestan branch (nodes 1-3, 8-9) hangs on Pokorny's judgement rather than on universal consensus; (b) node 4's glosses are looser than the sources (kahrkatāt- is specifically 'cock', kahrkāsa- specifically 'hen-eater'); (c) the parenthesised Persian words ورتک / وردیج in node 5 are synonyms for the bird, not descendants of Av. kahrka- — Mo'in derives them from Old Indic vartikā- 'quail' (Greek ortyx); (d) node 9 (korūh) is a cultural loan from India, not a phonetic descent. No extraction errors: the JSON reproduces the printed chart faithfully (only the fatha of «کَروه ۱» in node 9 is dropped).\",\n      \"note_fa\": \"جعبهٔ ریشه درست است. پوکورنی در صفحه‌های ۵۶۷ تا ۵۷۱ فرهنگ خود مدخل «ker-1, kor-, kr-» را با معنای «آوای خشن و ناهنجار، و پرندگانی که چنین آوایی دارند» آورده است؛ پس ارجاع نورایی (POK:567) دقیقاً سرآغاز همان مدخل است و برچسب «هندواروپایی» و معنای «آوای بلند، پرندگان پرهیاهو» درست است. نام‌های چهارگانهٔ «Ker 3, Qer, Qor, Qr» نیز ساختهٔ نورایی نیست: والده-پوکورنی (جلد ۱، ص ۴۱۳ به بعد) همین ریشه را با q می‌نویسد و کلاین (ص ۱۳۰۵، ذیل raven) آن را «*qer-, *qor-, *qr-، تقلیدی از آواهای خشن» می‌آورد. واتکینز نیز در پیوست AHD همین ماده را «ker-2، ریشهٔ آوابنیاد» خوانده است. چهار نکتهٔ کلی برای این صفحه: نخست، چونگ (۲۰۰۷، ریشهٔ *xraus) ریشهٔ ایرانی را می‌پذیرد اما تصریح می‌کند که پیوند آن با هندواروپایی آغازین اثبات‌شدنی نیست؛ دوم، معنی‌هایی که نورایی برای واژه‌های اوستایی گرهٔ ۴ آورده سست است (kahrkatāt- یعنی «خروس» و kahrkāsa- یعنی «مرغ‌خوار»)؛ سوم، «ورتک» و «وردیج» در گرهٔ ۵ تنها مترادف‌های فارسی‌اند و از kahrka- نیامده‌اند، بلکه معین آن‌ها را از هندی باستان vartikā- «بلدرچین» می‌داند؛ چهارم، «کروه» در گرهٔ ۹ وام‌واژه‌ای از سانسکریت است نه بازماندهٔ آوایی ایرانی. در خواندن اسکن خطایی رخ نداده و متن استخراج‌شده با صفحهٔ چاپی می‌خواند.\",\n      \"sources\": [\n        \"https://www.etymonline.com/word/raven\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:567\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt (translated IEW dump), the entry that ends 'References: WP. I 413ff., WH. I 275 f., 290, 291 f., 293 ... Page(s): 567-571': 'Root/ lemma: ker-1, kor-, kr- | Meaning: a kind of sound (hoarse shrieking, etc.), *crane | Note: aniaut mostly k-, rare ḱ- also with moveable s- : (s)ker-'. The whole of Nourai's chart (Avestan xraos-, kahrkatāt-, kahrkāsa-, npers. kark/sarfa, Old Indic krośa-, the Germanic *hr-/*skr- forms and the English words) is drawn from these five pages.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. I 413-418 (running head 'qer-, qers- — ḱer-, ḱor-, ḱr-' on p.413)\",\n          \"stance\": \"supports\",\n          \"note\": \"Walde-Pokorny I, the source Pokorny himself cites, has the same lemma with q-notation and the same material: 'av. kahrka indecl. „kikeriki!“, auch Bezeichnung des Hahnes, npers. kark „Huhn“, av. kahrkasa- m. „Geier, eigentlich Hähneesser“' (p.414) and 'Ai. krośati, av. xraosaiti „kreischt, schreit“, ai. kroca- m. „Schrei, Rufweite“, npers. (Horn Np. Et. 106) xurōs „Hahn“' (p.417). Nourai's spellings 'Qer, Qor, Qr' come from this notation.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, s.v. ker-2 [Pok. 1. ker- 567]\",\n          \"stance\": \"supports\",\n          \"note\": \"'ker-2. Echoic root, base of various derivatives indicating loud noises or birds. I. Zero-grade form *kr-, becoming Germanic *hr-. ... III. O-grade form *kor-. 1. Latin corvus, raven ... 2. Greek korax, raven'. Same root, same gloss as the chart's box.\"\n        },\n        {\n          \"src\": \"KLN\",\n          \"where\": \"p.1305 s.v. raven, n.\",\n          \"stance\": \"supports\",\n          \"note\": \"'These words are labial enlargements of I.-E. base *qer-, *qor-, *qr-, imitative of harsh sounds. From the same base are Gk. korax, korōnē, L. cornix, corvus, OI. krośati, Avestic xraosaiti, „cries, shouts“, OI. krośah, „a call, a shout“ ...' — the very wording behind Nourai's root names.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, s.vv. kerk- and kirkos\",\n          \"stance\": \"partial\",\n          \"note\": \"Mann splits the material into several onomatopoeic lemmas rather than one: 'kerk- „cluck; clucking bird“. Cf. WP I, 414 ... Ir. cearc, f. „hen“ ... Per. cf. kürgas („vulture“, fr. *krkot- or *karket-)' and 'kirkos „a screeching bird“. Cf. WP I, 413 & II, 569'. Same etymological family, different lemma-cutting.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck 18.13 'cry, shout'\",\n          \"stance\": \"supports\",\n          \"note\": \"'*krau-k- in Skt. kruc-, Av. xraos- „cry, shout“, etc., all from parallel extensions of the root in Grk. krazō', and at 18.12 'an extension of an imitative *(s)ker-, cf. Skt. kārava- „crow“, Grk. korax, Lat. corvus „raven“. Walde-P. 1.415.'\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"xraos\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Avestan xraos- is real, but it is a VERB, 'to cry out, shout', not a noun 'loud noise': Bartholomae AiWb (cols. 535-536) has 'xraos- V. „schreien“. Praes. xraosa-, xraosya-. — PPfP. *xrusta-', with the attested forms xraosiieiti (V.15.5), fra-ca xraosōit̰ (A 3.13), xraosəntəm upa (Y.53.8); the corresponding noun is xraosya- m. 'Schreien, Angstgeschrei' (V.13.9). So Nourai's gloss is the sense of the derived noun, not of the citation form he prints. The attachment to *ker- is Pokorny's own: at IEW 571, under the -s- extension of ker-1, he writes 'Old Indic krośati, Avestan xraosaiti „shrieks, shouts, howls“ ... npers. xrōs „rooster, cock“', and Klein p.1305 lists the same pair under his base *qer-. Formally Av. xraos- = Ind.-Ir. *kraus- with the regular Iranian change of initial *k before r to x (Av. xr- : Skt. kr-). Cheung 2007 no.449 sets up Proto-Iranian *xraus 'to call' but adds 'An IE provenance for this common Indo-Iranian root cannot be established' (LIV has no entry, and Pokorny's only non-Ind.-Ir. support is the isolated OE hrēam) — hence 'plausible' rather than 'confirmed': the word and its Iranian descendants are certain, its PIE parentage is Pokorny's judgement.\",\n          \"derivation_fa\": \"صورت اوستایی xraos- درست است، اما در فرهنگ‌ها فعل است نه اسم: بارتولومه (ستون ۵۳۵-۵۳۶) آن را «xraos- فعل: فریاد کردن» می‌آورد با ستاک حال xraosa-/xraosya- و صفت مفعولی *xrusta-، و اسمِ برساخته از آن xraosya- «فریاد، بانگِ بیم» است؛ پس معنایی که نورایی داده («آوای بلند») از آنِ اسم است نه از آنِ صورتی که چاپ کرده. پیوند این ستاک با ریشهٔ هندواروپایی *ker- از خودِ پوکورنی است: او در صفحهٔ ۵۷۱ زیر گسترشِ ‑s‑ همین ریشه می‌نویسد «سنسکریت krośati، اوستایی xraosaiti «فریاد می‌کشد» ... فارسی نو xrōs «خروس»»، و کلاین (ص ۱۳۰۵) نیز همین جفت را زیر همان ریشه آورده است. از نظر آوایی xraos- بازماندهٔ هندوایرانی *kraus- است و تبدیل k آغازین به x پیش از r در ایرانی قاعده‌مند است (اوستایی xr- در برابر سنسکریت kr-). با این همه چونگ (۲۰۰۷، ریشهٔ ۴۴۹) هرچند ریشهٔ ایرانی *xraus «بانگ زدن» را می‌پذیرد، تصریح می‌کند که خاستگاه هندواروپایی آن اثبات‌شدنی نیست؛ از این‌رو ادعای نورایی «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/raven\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:571\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt, entry ker-1 (Page(s): 567-571), last section: 'With -s-: Old Indic krosati, Avestan xraosaiti „shrieks, shouts, howls“. Old Indic krosa-, klosa- m. „scream, earshot“, (: Old English hream „emergency call“ from *hrauhma), npers. xros „rooster, cock“; s. W. Schulze Kl. Schr. 166.' Exactly the arrow drawn.\"\n            },\n            {\n              \"ref\": \"KLN:1305\",\n              \"status\": \"supports\",\n              \"note\": \"Klein 1966 leaf 694 (= pp. 1304-1305), s.v. 'raven, n., a large bird of the crow family': '... labial enlargements of I.-E. base *qer-, *qor-, *qr-, imitative of harsh sounds. From the same base are ... OI. krosati, Avestic xraosaiti, „cries, shouts“, OI. krosah, „a call, a shout“ ...'. Klein's page also supplies the root box's name-forms.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"cols. 535-536 s.v. xraos-\",\n              \"stance\": \"partial\",\n              \"note\": \"'j.p g. xraos- V. „schreien“. Praes. 2 xraosa-, 26 xraosya-. — PPfP. *xrusta-'; and 'j. xraosya- m. „Schreien“; a) zum Zweck des Erschreckens „Anschreien“; b) aus Angst „Angstgeschrei“' (V.13.9). Confirms the form; contradicts the part-of-speech and gloss printed in the chart.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"no. 449, *xraus 'to call' (pp. 448-449)\",\n              \"stance\": \"partial\",\n              \"note\": \"'*xraus „to call“. AVESTAN: xraos- „to cry“ (better: „to call“?) ... MIDDLE PERSIAN: BMP hlws- /xrōh-/ or /xrōs-/ „to call, cry“ ... SANSKRIT: kroś „to call aloud“ (RV+)'; footnote: 'An IE provenance for this common Ind.-Ir. root cannot be established. Pokorny: l.c. cites the isolated formation, OE hrēam „emergency call“ ..., as a possible cognate.' — PIE? LIV: — | Pok.: 571.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I 417\",\n              \"stance\": \"supports\",\n              \"note\": \"'Ai. krośati, av. xraosaiti „kreischt, schreit“, ai. kroca- m. „Schrei, Rufweite“, npers. (Horn Np. Et. 106) xurōs „Hahn“' — under the same lemma qer-, kor-, kr-.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"xrusîten; xros\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both Middle Persian words are well attested and both descend from the Avestan-attested stem of node 1. MacKenzie, Concise Pahlavi Dictionary, prints 'xrōs [DYLKA < A dyk; hlws | P xrws, N xurōs] cock' and 'xrōstan [hlwstn' | M xrwst] call, cry'; Nyberg, Manual II p.219: 'xrōs [hlws] cock ... from xrōstan to cry, to shout ... MPrth xrwštn, xrws- „to call“, MPrs xrwstn, xrwh-; NP xurōs „a loud cry“, xurōšīdan „to shout“'. Nourai's 'xrusîten' is a variant transcription of the -īt- infinitive (xrōsītan/xrōsīdan) rather than MacKenzie's short-stem xrōstan; the present stem xrōs- is the same, so this is a citation-form difference, not an error. Historically: Ind.-Ir. *kraus- > Old Iranian *xrauš/*xraus- > MP xrōs- (au > ō regularly in Middle Persian); the noun xrōs 'cock' is a nomen agentis of the verb, literally 'the crier' — Mo'in glosses it in Borhan 'لغةً بمعنی خروشنده (بمناسبت بانگ وی)'. Cheung notes that the genuinely south-western Middle Persian shape is /xrōh-/ (Iranian *-s- > -h- in Persian proper) and that the s/š-forms are the Parthian (north-western) ones; Nyberg says the same, calling NP xurōs the NW form beside SW xurōh.\",\n          \"derivation_fa\": \"هر دو واژهٔ فارسی میانه به‌خوبی گواهی‌شده‌اند و از همان ستاکی می‌آیند که در اوستا xraos- است. مکنزی در «فرهنگ کوچک پهلوی» می‌آورد: «xrōs [hlws] خروس» و «xrōstan بانگ زدن، فریاد کردن»؛ نیبرگ (جلد دوم، ص ۲۱۹) نیز: «xrōs خروس ... از xrōstan «بانگ زدن»؛ پارتی xrwš-/xrws- «خواندن»، فارسی میانه xrwstn، xrwh-؛ فارسی نو خروش «بانگ بلند» و خروشیدن». صورت «xrusîten» نزد نورایی گونهٔ مصدرِ ‑īt‑ (xrōsītan/xrōsīdan) است در برابر مصدر کوتاهِ xrōstan نزد مکنزی؛ ستاک حال هر دو یکی است، پس این تفاوت در شیوهٔ ضبط است نه خطا. از نظر تحول آوایی: هندوایرانی *kraus- > ایرانی باستان *xraus- > فارسی میانه xrōs-، زیرا دوواکهٔ au در فارسی میانه به ō بدل می‌شود؛ و «خروس» در اصل صفت فاعلی همین فعل است، یعنی «بانگ‌زننده» — چنان‌که معین در حاشیهٔ برهان می‌نویسد «لغةً بمعنی خروشنده (بمناسبت بانگ وی)». چونگ و نیبرگ هر دو یادآور می‌شوند که صورت اصیل جنوب‌غربی xrōh- است و صورت‌های s/š از پارتی (شمال‌غربی) به فارسی رسیده‌اند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D9%88%D8%B3\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:741\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' ed. Mo'in, vol. 2: p.741 (BQT_v2_pages.txt leaf 201) carries the headwords خروه ('بمعنی خروس است که بعربی دبك خوانند') and خروهك, and the etymological footnotes Nourai is citing stand at the foot of the facing page 740 (leaf 200): 'خروس — پهلوی xrōs ... از ريشة اوستایی xraos- ... معنی خروشیدن؛ لغةً بمعنی خروشنده (بمناسبت بانگ وی) = فارسی خروه = خروج ...' and 'خروش — از مصدر اوستابی xraos- (خروشیدن). هندی باستان krośa- ... ورك: هوبشمان ۱۸۴'. The article spans 740-741; Aryanpur likewise cites 'برهان قاطع: ۷۴۱' for خروس.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, Concise Pahlavi Dictionary, s.vv. xrōs, xrōstan (p.94; English index pp. 'cock xrōs', 'cry (v.) xrōstan')\",\n              \"stance\": \"supports\",\n              \"note\": \"'xros [DYLKA < A dkr); hlws I P xrws, N Xurōs] cock.' and 'xrōstan [hlwstn' I M xrwst] call, cry.' — the ideogram DYLKA (Aramaic 'cock') and the Manichaean spelling confirm both words.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Manual of Pahlavi II (Glossary), p.219\",\n              \"stance\": \"supports\",\n              \"note\": \"'xrōs [hlws] cock 56%. — NP xurōs [NW form] and xurōh (SW form); from xrōstan to cry, to shout: ō dīdan dēvān apar bē xrēst ...; vāng xrōst. — MPrth xrwštn, xrws- „to call“, MPrs xrwstn, xrwh-; NP xurōs „a loud cry“, xurōšidan „to shout“; Ghilain 64; Verbum 185; Schaeder ...; Bailey, BSOAS XIII, 1950, 399.'\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"no. 449 *xraus, Middle Persian section\",\n              \"stance\": \"supports\",\n              \"note\": \"'MIDDLE PERSIAN: BMP hlws- /xrōh-/ or /xrōs-/ „to call, cry“, MMP xrwh „call“ ... Partic. perf. pass. BMP hlwst /xrōst/. PARTHIAN: xrws- „to call, evoke“, xrws „call“.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"xorŭšîdan «خروشیدن»; xorŭs «خروس ( خروج )»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian خروشیدن xorušīdan 'to roar, clamour' is built on the noun خروش xorūš 'clamour' + the infinitive suffix -īdan; Mo'in's own note in Borhan p.740 says so verbatim: 'خروشیدن — از: خروش + یدن (پسوند مصدری): بانگ زدن، فریاد کردن با ناله و زاری'. خروس xorūs 'cock' continues Middle Persian xrōs unchanged except for the prothetic/anaptyctic vowel of the xVr- cluster (xrōs > xurōs). The variant «خروج» printed in the parenthesis — and rhymed by Rudaki in the quoted line 'تبر برده بر سر چو تاج خروج' — is genuine and is recorded by Mo'in in the same footnote ('= فارسی خروه = خروج'), beside dialect forms Gilaki xrūs, Farizandi xorūs, Natanzi xorūs and the true south-western شکل خروه xurōh. The š of خروش/خروشیدن beside the s of خروس is the tell-tale of the Parthian stem xrōš- entering Persian alongside the inherited s-form. Hübschmann, Persische Studien §101 (p.239), lists 'xuros „Hahn“, skr. Wrzl. kroś' among the Persian words with intervocalic s, and Wiktionary derives خروس 'from Middle Persian hlws /xrōs/ „cock“, literally „the caller“, from hlwstn' /xrōstan/ „to call, to cry“'.\",\n          \"derivation_fa\": \"«خروشیدن» در فارسی نو از اسمِ «خروش» + پسوند مصدری «‑یدن» ساخته شده است؛ خودِ معین در حاشیهٔ برهان (ص ۷۴۰) همین را می‌نویسد: «خروشیدن — از: خروش ‎+‎ یدن (پسوند مصدری): بانگ زدن، فریاد کردن با ناله و زاری». «خروس» نیز دنبالهٔ بی‌واسطهٔ xrōs فارسی میانه است و تنها واکهٔ میانجی در خوشهٔ آغازین افزوده شده (xrōs > xurōs). گونهٔ «خروج» که در پرانتز آمده و رودکی آن را قافیه کرده («تبر برده بر سر چو تاج خروج») ساختگی نیست؛ معین در همان حاشیه آن را در کنار «خروه» می‌آورد، و گونه‌های گویشی گیلکی xrūs، فریزندی xorūs و نطنزی xorūs را نیز برمی‌شمارد. تفاوت «ش» در خروش/خروشیدن با «س» در خروس نشانهٔ آن است که ستاک شمال‌غربی (پارتی) xrōš- در کنار صورت جنوب‌غربی وارد فارسی شده است. هوبشمان در «پژوهش‌های فارسی» بند ۱۰۱ (ص ۲۳۹) «xuros خروس» را با ریشهٔ سنسکریت kroś می‌سنجد و ویکی‌واژه نیز آن را از فارسی میانه xrōs «بانگ‌زننده» می‌داند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D9%88%D8%B3\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"IRT:44\",\n              \"status\": \"not_checked\",\n              \"note\": \"IRT = M.A. Sajjadiyyeh, «پژوهشی در تبار مشترک ایرانیان و تورانیان», Bonyad-e Neyshabur 1368/1989. refs_online.json records it as 'purchase' only, 'Not found' online, no local file; nothing to check.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BQT\",\n              \"where\": \"vol. 2 p.740, Mo'in's footnotes on خروش / خروس / خروشیدن\",\n              \"stance\": \"supports\",\n              \"note\": \"'خروش — از مصدر اوستابی xraos- (خروشدن). هندی باستان krośa- ... ورك: اسذق و هوبشمان ۱۸۴'; 'خروس — پهلوی xrōs ... از ريشة اوستابی xraos- ... معنی خروشیدن؛ لغة بمعنی خروشنده (بمناسبت بانگ وی) = فارسی خروه = خروج ... گیلکی xrūs، فریزندی xorūs ... نطنزی xorūs'; 'خروشیدن — از: خروش + یدن (پسوند مصدری)'.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Persische Studien §101, p.239\",\n              \"stance\": \"supports\",\n              \"note\": \"'... btst „zwanzig“ aus *visat = zd. vīsaiti; xuros „Hahn“, skr. Wrzl. kroś' — Hübschmann lists xurōs among the Persian words whose intervocalic s goes back to Old Iranian s.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"no. 449, NWIr. section\",\n              \"stance\": \"supports\",\n              \"note\": \"'NWIR: NP xurōsidan „to cry, shout“, NP xurōs, Anar. hiros, Jow. ru:s, Nn. huros „rooster, cock“.'\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Grundriss, cited by Walde-Pokorny I 417 as 'Horn Np. Et. 106'\",\n              \"stance\": \"supports\",\n              \"note\": \"Horn's entry for xurōs is the standard reference behind WP I 417 'npers. (Horn Np. Et. 106) xurōs „Hahn“'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Avestan\",\n          \"words\": \"kahrkatât; kahrkâ-asa\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both Avestan forms exist and both belong to this root, but Nourai's glosses are looser than the sources. Bartholomae AiWb (cols. 453-456) has: 'kahrka indekl., den Ruf des Hahns nachahmendes Wort „Kikeriki“; auch als Bezeichnung des Hahns ... np. kark „Huhn“; ai. vgl. kṛkavāku- m. „Hahn“'; then 'kahrkatāt- f. (gemeiner oder Spott-)Name des Hahns: kahrkatās nāma aojaite V.18.15. Eig. „Kikerikitum“' — i.e. specifically 'cock' (an abstract in -tāt- built on the imitative kahrka-), not 'some noisy birds'; and 'kahrkāsa- m. „Geier“ (Yt.14.33; Yt.5.61; V.7.20) ... Komp.: *kahrka- + *āsa-; eig. „Hühnerfresser“ ... vgl. np. (Npa.) kargas'. So kahrkāsa- (Nourai's 'kahrkâ-asa', hyphenated to show the compound) is 'fowl-EATER', the second member being the agent noun of the root ad-/as- 'to eat' (PIE *h₁ed-), not 'eating bird' in general. Pokorny 568, the page cited, has both: 'Avestan kahrkatāt-t „rooster, cock“, npers. kark „chicken“, Avestan kahrkāsa- m. „vulture, actually Hahneesser“'. Verdict plausible: forms and root attachment confirmed, glosses imprecise.\",\n          \"derivation_fa\": \"هر دو صورت اوستایی واقعی‌اند و هر دو به همین ریشه می‌رسند، اما معنی‌هایی که نورایی داده دقیق نیست. بارتولومه (ستون‌های ۴۵۳-۴۵۶) می‌نویسد: «kahrka واژه‌ای صرف‌ناپذیر و تقلیدِ بانگ خروس («قوقولی‌قوقو»)، و نیز نامِ خودِ خروس ... فارسی نو کرک «مرغ خانگی»؛ قس سنسکریت kṛkavāku- «خروس»»؛ سپس «kahrkatāt- مؤنث، نامِ عامیانه یا ریشخندآمیزِ خروس (وندیداد ۱۸: ۱۵)؛ در اصل یعنی «قوقولی‌قوقوییْ بودن»» — یعنی به‌روشنی «خروس»، نه «چند پرندهٔ پرهیاهو»؛ و «kahrkāsa- مذکر «کرکس»؛ مرکب از kahrka- + āsa-؛ در اصل «مرغ‌خوار»؛ قس فارسی نو کرگس». پس جزء دوم صفت فاعلی ریشهٔ ad-/as- «خوردن» (هندواروپایی *h₁ed-) است و ترجمهٔ «پرندهٔ خورنده» نارساست. پوکورنی نیز در صفحهٔ ۵۶۸ همین دو را آورده است. حکم: صورت‌ها و پیوند ریشه‌ای درست، اما معنی‌ها سست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%A9%D8%B1%DA%A9%D8%B3\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:568\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt, ker-1, section '2. guttural extensions: A. Auf -k- (broken reduplication): kerk-, krek-, krok-': 'Old Indic krkara-, krakara-, krkana- m. „a kind of partridge“, krka-vaku- m. „rooster, cock“, krkasa, krkalika bird name; Avestan kahrkatat- „rooster, cock“, npers. kark „chicken“, Avestan kahrkasa- m. „vulture, actually Hahneesser“'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"cols. 453-456, s.vv. kahrka, kahrkatāt-, kahrkāsa-\",\n              \"stance\": \"partial\",\n              \"note\": \"'kahrka indekl., den Ruf des Hahns nachahmendes Wort „Kikeriki“, auch als Bezeichnung des Hahns'; 'kahrkatāt- f. (gemeiner oder Spott-)Name des Hahns ... kahrkatās nāma aojaite V.18.15. Eig. „Kikerikitum“'; 'kahrkāsa- m. „Geier“ ... Komp.: *kahrka- + *āsa-, eig. „Hühnerfresser“ ... vgl. np. (Npa.) kargas'. Supports the forms and the root, contradicts 'some noisy birds' and 'eating bird'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I 414\",\n              \"stance\": \"supports\",\n              \"note\": \"'av. kahrka indecl. „kikeriki!“, auch Bezeichnung des Hahnes, npers. kark „Huhn“, av. kahrkasa- m. „Geier, eigentlich Hähneesser“' — Walde-Pokorny already gives the compound analysis Nourai draws.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, s.v. kerk- 'cluck; clucking bird'\",\n              \"stance\": \"supports\",\n              \"note\": \"'kerk- „cluck; clucking bird“. Cf. WP I, 414 ... Ir. cearc, f. „hen“; ... Oss. cf. kark ...; Per. cf. kürgas („vulture“, fr. *krkot- or *karket-)' — same family, Persian kargas included.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"karkas «کرکس»; kark, karak «کَرک ( ورتک ، وردیج )»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The two headwords are right and the arrow from node 4 is standard. کرکس karkas < Middle Persian kargās/kargas (Bundahišn kahrkās) < Av. kahrkāsa- 'hen-eater'; Horn, Grundriss no. 849 (p.190): 'kerges „Geier“ (Šāhn. I,120 V.1013): aw. kahrkāsa- „Geier“; phlv. kahrkās, kargas (Bund.); LW. afγ. gargas; bal. kargas; oss. čarγas'. کرک kark 'domestic fowl' is Horn no. 848 (p.189): 'kark, kerk „Huhn“: aw. *kahrka- in kahrkāsa- „Hühnerfresser (Geier)“; phlv. kark; ai. kṛkavāku- „Hahn“; kurd. kurk, afγ. čirg, oss. kark, wax. kork'; karak is its -ak diminutive/variant. Mo'in's footnote in Borhan (vol. 3, printed ~1622-1624) states Nourai's claim word for word. BUT the parenthesised «ورتک ، وردیج» are only Persian synonyms for the game-bird, NOT descendants of kahrka-: on the very page Nourai cites for them, Borhan p.2268, Mo'in's footnote 8 on وردیج reads 'ورتیج، وردج، ورتک، هندی باستان vartikā- (بلدرچین)، ... یونانی ortyx، کردی wardā ... افغانی ..., اوستی ..., بلوچی ... (کبک کوهی)، وخی ...' — i.e. from Indo-Iranian *wartikā- 'quail' (PIE *wortu-, Greek ortyx), a completely unrelated root. Read as synonym-listing the parenthesis is harmless; read as derivation it is wrong, so the node is 'plausible' rather than 'confirmed'.\",\n          \"derivation_fa\": \"دو سرواژهٔ این گره درست است و پیکان آن از گرهٔ ۴ کاملاً استاندارد. «کرکس» از فارسی میانهٔ kargās/kargas (در بندهش kahrkās) و آن از اوستایی kahrkāsa- «مرغ‌خوار»؛ هرن در «دستور ریشه‌شناسی فارسی نو» (شمارهٔ ۸۴۹، ص ۱۹۰) می‌نویسد: «کرگس «کرکس» (شاهنامه): اوستایی kahrkāsa-؛ پهلوی kahrkās، kargas (بندهش)؛ وام در پشتو gargas، بلوچی kargas، اوستی čarγas». «کرک» نیز شمارهٔ ۸۴۸ هرن است (ص ۱۸۹): «کرک، کرک «مرغ خانگی»: اوستایی *kahrka- در kahrkāsa-؛ پهلوی kark؛ سنسکریت kṛkavāku-؛ کردی kurk، پشتو čirg، اوستی kark، وخی kork»؛ و «کرک» گونهٔ با پسوند ‑ک همان است. معین نیز در حاشیهٔ برهان (جلد سوم، صفحهٔ چاپی نزدیک ۱۶۲۲-۱۶۲۴) دقیقاً همین را می‌گوید. اما «ورتک» و «وردیج» درون پرانتز تنها مترادف‌های فارسی همان پرنده‌اند و بازماندهٔ kahrka- نیستند: در همان صفحهٔ ۲۲۶۸ برهان که نورایی به آن ارجاع داده، معین در پانوشت هشتم می‌نویسد «ورتیج، وردج، ورتک، هندی باستان vartikā- (بلدرچین)، یونانی ortyx، کردی wardā ...» — یعنی از ریشه‌ای یکسره دیگر (*wortu- هندواروپایی). اگر پرانتز را فهرست مترادف بدانیم اشکالی ندارد، اما اگر آن را زنجیرهٔ اشتقاق بخوانیم نادرست است؛ از این‌رو حکمِ گره «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%A9%D8%B1%DA%A9%D8%B3\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1624\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' ed. Mo'in, vol. 3, pdf page 417 (printed ≈1622-1624), footnote 1 to کرکس: 'قس اوستا kahrkāsa (کرکس). پهلوی kargas ... افغانی gargas ... اوستی ... اسشق ۸۴۹ ... واژهٔ اوستایی مرکب از دو جزء است: kahrka (= کرک، مرغ) + āsa (خورنده)، جمعاً بمعنی مرغ‌خوار «هرمزدنامه»'. Exactly the arrow drawn. (The neighbouring pdf page 415 has کرک 'مرغ خانگی و ماکیان'.)\"\n            },\n            {\n              \"ref\": \"BQT:2268\",\n              \"status\": \"contradicts\",\n              \"note\": \"Borhan vol. 4 pdf page 351 = printed 2268, footnote 8 s.v. وردیج: 'ورتیج، وردج، ورتک، هندی باستان vartikā- (بلدرچین)، پهلوی ..., یونانی ortyx، کردی wardā ..., افغانی ..., اوستی ..., بلوچی ... (کبک کوهی)، وخی ..., اسشق ۱۰۷۸'. The page Nourai cites derives ورتک/وردیج from *wartikā- 'quail' (Gk. ortyx), not from Av. kahrka-.\"\n            },\n            {\n              \"ref\": \"MON:5001\",\n              \"status\": \"not_checked\",\n              \"note\": \"The local Mo'in copy is the 2-volume Adena reprint of the lexicon (different pagination); p.5001 of the 6-volume Amir Kabir edition falls in the a'lam volumes (5-6, probably s.v. کوه کرکس), which are not in the local library. The lexicon entry itself was consulted separately (see 'consulted').\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HRN\",\n              \"where\": \"nos. 848-849, pp. 189-190\",\n              \"stance\": \"supports\",\n              \"note\": \"'kark, kerk „Huhn“ ... aw. *kahrka- in kahrkāsa- „Hühnerfresser (Geier)“; phlv. kark; ai. kṛkavāku- „Hahn“. kurd. kurk „Huhn“; afγ. čirg; oss. kark; wax. kork.' and '849. kerges „Geier“ (Šahn. I,120 Vers 1013): aw. kahrkāsa- „Geier“; phlv. kahrkās, kargas (Bund.). LW. afγ. gargas; bal. kargas; oss. čarγas ... Das nur bei den Pärsen noch vorkommende np. karkatas „Geier“ scheint nach aw. kahrkatās- repristinirt zu sein.'\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Persische Studien §101, p.239 (also p.212)\",\n              \"stance\": \"supports\",\n              \"note\": \"'kargas „Geier“ = zd. kahrkāsa-' (listed among the Persian words with s from Old Iranian s); p.212 repeats 'kargas „Geier“ = zd. kahrkāsa-' next to 'kark „Huhn“'.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, p.402 (pdf 401), entry «کرک (به چم «مرغ خانگی»)»\",\n              \"stance\": \"supports\",\n              \"note\": \"Lists Avestan, Pahlavi, Ossetic, Kurdish, Pashto, Tocharian A, Sanskrit, Armenian, Greek, Latin, Old Icelandic, Old English etc. under one root, with note 1: 'واژه‌های فارسی «کرکس» و اوستایی kahrkāsa و سانسکریت kṛkavāku نیز از همین واجریشه آمده‌اند.' (cites برهان قاطع p.1632).\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Farsi, s.v. کرکس (2-vol reprint OCR)\",\n              \"stance\": \"partial\",\n              \"note\": \"'کرکس: (اِ.) (جاذ.) پرنده‌ای است قوی هیکل و بد ریخت و گوشتخوار از راستهٔ شکاریان روزانه ... لاشخور، مردارخوار، رخمه، نسر' — the reprint gives the zoological description but no etymological bracket, so it corroborates the word and its sense only.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Sogdian\",\n          \"words\": \"crks\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Gharib's Sogdian dictionary, entry 3253 on p.128, is exactly Nourai's source and says exactly what the arrow says: 'crks (B, M, S) — čarkas < Av. *kahrkāsa — vulture. GMS 139, 249; TSP 3.238, 1320; Bailey, Asica 8.' The Sogdian consonant skeleton črkʾs is read /čarkas/; the initial č- against Persian k- is the well-known palatal variant of this bird-name in the north-eastern and Ossetic area (Horn no.849 lists Ossetic čarγas 'vulture' beside Persian kargas as a borrowing), and the loss of the -h- of Av. kahrkāsa- in the consonant cluster is regular in Sogdian. Semantically 'vulture' is unchanged from the Avestan.\",\n          \"derivation_fa\": \"فرهنگ سغدی بدرالزمان قریب، مدخل ۳۲۵۳ در صفحهٔ ۱۲۸، دقیقاً همان است که نورایی به آن ارجاع داده و همان را می‌گوید که پیکان نشان می‌دهد: «crks (بودایی، مانوی، مسیحی) — čarkas < اوستایی *kahrkāsa — کرکس». صورت نوشتاری črkʾs را /čarkas/ می‌خوانند؛ «چ» آغازین در برابر «ک» فارسی گونهٔ کامی‌شدهٔ شناخته‌شدهٔ این نام‌پرنده در حوزهٔ شمال‌شرقی و آسی است (هرن در شمارهٔ ۸۴۹ صورت آسی čarγas را در کنار kargas فارسی به‌عنوان وام‌واژه می‌آورد)، و افتادنِ h در خوشهٔ همخوانی kahrk- در سغدی قاعده‌مند است. معنا نیز همان «کرکس» اوستایی مانده است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"SOD:128\",\n              \"status\": \"supports\",\n              \"note\": \"SOD_pages.txt leaf 193, which carries the printed page number 128: '3253 crks B, M, S — čarkas ©<Av. *kahrkāsa — vulture — GMS 139, 249; TSP 3.238, 1320; Bailey, Asica 8'. (The SOD_alt file gives the same entry in the form '/carkas/ ... vulture Av. kahrkasa-'.) So Nourai's SOD:128 is a page number, and the page says what he claims.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SOD\",\n              \"where\": \"Gharib no. 3253, p.128\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check; Gharib explicitly writes '< Av. *kahrkāsa'.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"no. 849, p.190\",\n              \"stance\": \"partial\",\n              \"note\": \"Horn's list of the Iranian forms of the vulture-name includes 'oss. čarγas', the č-variant to which the Sogdian črkʾs belongs; Horn does not cite the Sogdian itself.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"sorfeh «سرفه»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Pokorny 569, the page cited, does contain the word: under '3. Labial extensions: A. With -p-' (Old Indic kṛpate 'lament', Latin crepō 'to crackle, creak') he writes 'npers. sarfak „clangor“, sarfa (Iran. *sarafa-) „cough“'. The s- (where the root normally shows k-) is possible only through the palatal variant Pokorny himself allows in the head-note of the lemma ('anlaut mostly k-, rare ḱ- also with moveable s-'), since Old Iranian *ḱ > s; hence his reconstruction *sarafa- 'cough' with the -p- extension voiced/spirantised to -f- between vowels. So Nourai's arrow reproduces Pokorny faithfully. It is only 'plausible', however, because no independent source corroborates it: Walde-Pokorny I 415-416, which Pokorny cites for this very extension, does not mention any Persian word (sarfa is Pokorny's 1959 addition); Wiktionary's سرفه entry has no etymology at all; Horn (no. 741, p.163) mentions 'np. sufīden ... gehört zu surfe „Husten“, surfīden' only while discussing an imitative whistling verb alongside Latin sībilāre; and Aryanpur (p.363) files سرفیدن under a different, whistle/noise root. For a transparently onomatopoeic word several imitative bases can lay claim, so the assignment to *ker- is defensible but not established.\",\n          \"derivation_fa\": \"صفحهٔ ۵۶۹ پوکورنی — همان که نورایی به آن ارجاع داده — به‌راستی این واژه را دارد: در بخش «گسترش‌های لبی، الف: با ‑p‑» (در کنار سنسکریت kṛpate «مویه کردن» و لاتین crepō «ترق‌تروق کردن») می‌نویسد: «فارسی نو sarfa «سر و صدا»، sarfa (ایرانی *sarafa-) «سرفه»». «س» آغازین (در برابر «ک» معمولِ این ریشه) تنها از راه گونهٔ کامیِ ḱ ممکن است که خود پوکورنی در سرآغاز مدخل اجازه داده است، زیرا ḱ ایرانی باستان به s بدل می‌شود؛ و p میان دو واکه به f سایشی شده است. پس نورایی امانت‌دارانه از پوکورنی نقل کرده است. با این همه حکم «با احتیاط پذیرفتنی» است، چون هیچ منبع مستقلی آن را تأیید نمی‌کند: والده-پوکورنی (جلد ۱، ص ۴۱۵-۴۱۶) که پوکورنی برای همین گسترش به آن ارجاع می‌دهد هیچ واژهٔ فارسی ندارد؛ مدخل «سرفه» در ویکی‌واژه اصلاً ریشه‌شناسی ندارد؛ هرن (شمارهٔ ۷۴۱، ص ۱۶۳) تنها گذرا می‌گوید «np. sufīden ... به surfe «سرفه» و surfīden مربوط است» آن هم در بحث از فعلی آوابنیاد به معنی «سوت زدن»؛ و آریان‌پور (ص ۳۶۳) «سرفیدن» را زیر ریشه‌ای دیگر (به چمِ «صفیر») آورده است. برای واژه‌ای آشکارا آوابنیاد چند ریشهٔ تقلیدی می‌توانند مدعی باشند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D9%81%D9%87\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:569\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt, ker-1, '3. Labial extensions: A. With -p-: Old India krpate, Aor. akraplsta „lament“; krcchra- „bad“; n. „need“ ... npers. sarfak „clangor“, s[ar]f[a] (Iran. *sarafa-) „cough“; Latin crepō, -āre „knattern, rustle, crack, creak“ ...'. Pokorny's Iranian reconstruction *sarafa- 'Husten' is exactly Nourai's claim.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I 415-416 (the *(s)krep- section)\",\n              \"stance\": \"silent\",\n              \"note\": \"Walde-Pokorny's treatment of the labial extension lists Lettish krepēt, Lithuanian skreplenti, OCS kropljǫ etc. but no Iranian word at all; grep for 'sarfa/surfa/sarafa' in WLD_Bd1 returns nothing. The Persian word is Pokorny's own 1959 addition.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"no. 741, p.163\",\n              \"stance\": \"partial\",\n              \"note\": \"'np. sufīden wird dagegen nur als „husten“ bedeutend aufgeführt und gehört zu surfe „Husten“, surfīden' — Horn attests the noun and the verb but attaches them to an onomatopoeic whistling group (Latin sībilāre, sifflare), giving no *ker- etymology.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, p.363, entry headed «سرت (به چم «صفیر»)»\",\n              \"stance\": \"partial\",\n              \"note\": \"Under a whistle/hiss root Aryanpur notes: '... می‌گوید واژه‌ی فارسی نوین «سفلیدن» یا «سیفلیدن» نیز از همین واجریشه است ولی این واژه را در هیچ کدام از فرهنگ‌ها نیافتم. شاید منظورش «سرفیدن» به چم «سرفه کردن» باشد' — i.e. a rival, non-*ker- home for the word.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Wiktionary/Mo'in: سرفه\",\n              \"stance\": \"silent\",\n              \"note\": \"The English Wiktionary entry سرفه gives only the sense 'cough' plus pronunciations and the derived سرفه کردن; there is no etymology section (archived 2026-09-06).\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"krosa\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit krośa- m. is the nominal derivative of the verb kruś-/krośati 'to cry out, call aloud' (RV onwards), formed with the same -s- extension of the root as Avestan xraosaiti. Its double meaning — 'a cry' and 'the range of a shout', hence a measure of about two miles — is exactly what Nourai prints, and is exactly Pokorny's wording on the page his bare 'POK' refers to (IEW 571): 'Old Indic krośati, Avestan xraosaiti „shrieks, shouts, howls“. Old Indic krośa-, klośa- m. „scream, earshot“'. Walde-Pokorny I 417 has the same in German: 'ai. krośa- m. „Schrei, Rufweite“'. Hobson-Jobson (p.261, s.v. COSS) spells out the semantic step: 'The Skt. word is krośa, which also is a measure of distance, but originally signified „a call“, hence the distance at which a man's call can be heard.' The transliteration 'krosa' for krośa- is Nourai's usual simplification of the palatal ś.\",\n          \"derivation_fa\": \"krośa- در سنسکریت اسمِ برساخته از فعل kruś-/krośati «بانگ زدن، فریاد کشیدن» (از ریگ‌ودا به بعد) است و با همان گسترش ‑s‑ ساخته شده که در xraosaiti اوستایی دیده می‌شود. معنای دوگانهٔ آن — «فریاد» و «بُردِ فریاد»، و از آنجا واحدی از مسافت نزدیک به دو میل — درست همان است که نورایی نوشته و درست همان است که پوکورنی در صفحهٔ ۵۷۱ (که ارجاع بی‌شمارهٔ «POK» به آن است) می‌آورد: «سنسکریت krośati، اوستایی xraosaiti «فریاد می‌کشد»؛ سنسکریت krośa-، klośa- مذکر «فریاد، بُردِ صدا»». والده-پوکورنی (جلد ۱، ص ۴۱۷) نیز همین را به آلمانی دارد: «ai. krośa- m. „Schrei, Rufweite“». هابسن-جابسن (ص ۲۶۱، ذیل COSS) گام معنایی را باز می‌کند: «واژهٔ سنسکریت krośa است که واحد مسافت هم هست، اما در اصل «بانگ» معنی می‌داده، و از آنجا مسافتی که بانگِ آدمی به آن می‌رسد». ضبط «krosa» به جای krośa- ساده‌سازی همیشگی نورایی برای «ش» کامی است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK\",\n              \"status\": \"supports\",\n              \"note\": \"Pokorny IEW 571 (the -s- extension of ker-1): 'With -s-: Old Indic krośati, Avestan xraosaiti „shrieks, shouts, howls“. Old Indic krośa-, klośa- m. „scream, earshot“ ... npers. xrōs „rooster, cock“.' Nourai's citation carries no page, but this is the page.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I 417\",\n              \"stance\": \"supports\",\n              \"note\": \"'Ai. krośati, av. xraosaiti „kreischt, schreit“, ai. kroca- [= krośa-] m. „Schrei, Rufweite“, npers. xurōs „Hahn“.'\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"no. 449 *xraus, Sanskrit section\",\n              \"stance\": \"supports\",\n              \"note\": \"'SANSKRIT: kroś „to call aloud, call to“ (RV+) > EWAia I: 416' — Mayrhofer's Etymologisches Wörterbuch des Altindoarischen is cited for the verb from which krośa- is built.\"\n            },\n            {\n              \"src\": \"HJB\",\n              \"where\": \"Hobson-Jobson p.261, s.v. COSS\",\n              \"stance\": \"supports\",\n              \"note\": \"'The Skt. word is krośa, which also is a measure of distance, but originally signified „a call,“ hence the distance at which a man's call can be heard.' Confirms both halves of Nourai's gloss.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Persian\",\n          \"words\": \"korŭh «کروه ۱»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian کروه koroh, a unit of distance, is the Indian krośa taken over into Persian — a cultural loan of the Indo-Muslim period, not an inherited Iranian word (an inherited reflex of *ḱrauśa- would not look like this, and no Middle Persian ancestor is attested). Mo'in says so in the footnote on the very page Nourai cites, Borhan vol. 3 (printed ≈1628-1630): 'مسافت قریب دو میل ... جهانگیری و رشیدی بمعنی ثلث فرسنگ که یک میل باشد نوشته‌اند، لیکن این لفظ در هندی «کوس» و در سانسکریت «کروش» است که بمعنی دو میل انگلیسی است، و در افغانستان «کروه» مستعمل است ... در سانسکریت krośa (اصلاً آواز و مسافتی که آواز برسد)'. His own Farhang-e Farsi tags the headword '[هند. کوس، افغانی: کروه]' and glosses 'واحد مسافت ... در هندوستان آن را برابر دو میل انگلیسی می‌گیرند' — Nourai's 'about two miles' verbatim. Hobson-Jobson p.261: 'In the Pali vocabulary ... the word appears in the form kosa; and nearly this, kos, is the ordinary Hindi. Kuroh is a Persian form of the word, which is often found in Mahommedan authors and in early travellers.' The Khāqāni verse quoted in the chart ('کز دو کروهی بدید یاوگیان خزان') is a genuine 12th-c. attestation. Only the direction of the arrow needs the qualification 'borrowed from', not 'descended from'.\",\n          \"derivation_fa\": \"«کروه» در فارسی واحدی از مسافت است و همان krośa هندی است که در دورهٔ اسلامی از راه هند به فارسی رسیده — وام‌واژه‌ای فرهنگی است نه بازماندهٔ ایرانیِ موروثی (نه صورت فارسی میانه‌ای از آن گواهی شده و نه تحول آوایی موروثی به چنین شکلی می‌انجامد). معین در پانوشتِ همان صفحه‌ای که نورایی به آن ارجاع داده (برهان قاطع، جلد سوم، صفحهٔ چاپی نزدیک ۱۶۲۸-۱۶۳۰) می‌نویسد: «مسافت قریب دو میل ... جهانگیری و رشیدی بمعنی ثلث فرسنگ که یک میل باشد نوشته‌اند، لیکن این لفظ در هندی «کوس» و در سانسکریت «کروش» است که بمعنی دو میل انگلیسی است، و در افغانستان «کروه» مستعمل است ... در سانسکریت krośa (اصلاً آواز و مسافتی که آواز برسد)». در «فرهنگ فارسی» خودش نیز سرواژه را با برچسب «[هند. کوس، افغانی: کروه]» آورده و «واحد مسافت ... در هندوستان آن را برابر دو میل انگلیسی می‌گیرند» — همان «حدود دو میل» نورایی. هابسن-جابسن (ص ۲۶۱) می‌افزاید: «در واژه‌نامهٔ پالی صورت kosa آمده و kos هندیِ رایج است؛ kuroh صورت فارسی این واژه است که بارها در نویسندگان مسلمان و سیاحان کهن دیده می‌شود». بیت خاقانی که در نمودار آمده گواهی سدهٔ ششم است. تنها نکته آن است که پیکان را باید «وام‌گیری» خواند نه «تحول موروثی».\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1630\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' ed. Mo'in vol. 3, pdf page 423 (printed ≈1628-1630), footnote 10 to کروه: '... این لفظ در هندی «کوس» و در سانسکریت «کروش» است که بمعنی دو میل انگلیسی است، و در افغانستان «کروه» مستعمل است ... در سانسکریت krośa (اصلاً آواز و مسافتی که آواز برسد) «دکتر راجا»'. The headword itself: 'کروه — بضم اول ... ثلث و سه یک فرسخ را گویند و آن سه هزار گز است ...'.\"\n            },\n            {\n              \"ref\": \"MON:2960\",\n              \"status\": \"supports\",\n              \"note\": \"Mo'in, Farhang-e Farsi, s.v. کروه (found in MON_part2.txt of the 2-volume Adena reprint, whose pagination differs from the 6-volume Amir Kabir edition, so the number 2960 itself could not be checked): 'کروه (koroh) [هند. کوس، افغانی: کروه] (اِ.) واحد مسافت. جهانگیری و رشیدی به معنی ثلث فرسنگ (که یک میل باشد) نوشته و در برهان ثلث و سه یک فرسخ معادل سه هزار گز ... آورده؛ در هندوستان آن را برابر دو میل انگلیسی می‌گیرند.' Content supports the node exactly.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HJB\",\n              \"where\": \"Hobson-Jobson pp. 261-262, s.v. COSS\",\n              \"stance\": \"supports\",\n              \"note\": \"'Kuroh is a Persian form of the word, which is often found in Mahommedan authors and in early travellers. These latter (English) often write course.' Also: 'In the Pali vocabulary called Abhidhānappadīpikā ... the word appears in the form kosa; and nearly this, kos, is the ordinary Hindi'; Ibn Battuta c.1340 'as for the mile it is called among the Indians al-kurūh'.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Farsi s.v. کروه\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check: Mo'in's origin bracket is '[هند. کوس، افغانی: کروه]', i.e. he too treats it as coming from India.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"vol. 3 printed ≈1628-1630\",\n              \"stance\": \"supports\",\n              \"note\": \"Headword and Mo'in's footnote, quoted in ref_check.\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Germanic\",\n          \"words\": \"hr; skrainjan, skrěki; krik\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"This box is a compressed transcript of Watkins's AHD entry, which is what Nourai's bare 'AHD' points to: 'ker-2. Echoic root ... I. Zero-grade form *kr-, becoming Germanic *hr-. 1. Germanic *hring- in Old English hringan, to resound, clink: RING. 2. Germanic *hraik- in Old English hrǣcan, to clear the throat: RETCH. 3. Germanic *hrōkaz, „croaking bird“, crow, in Old English hrōc, rook: ROOK. 4. Germanic *hraban, *hrabnaz, raven, in Old English hræfn: RAVEN. ... 6. Extended form *kri- in Germanic *krik- in Old French criquer, to creak, click: CRICKET. II. Variant form *skr-. ... 2. Germanic *skrēkjan- in Old Norse skrækja, to shriek: SCREAK, SCREECH. 3. Germanic *skrainjan, to shout, shriek, in Old Norse skrǣma, to scream ...: SCREAM. [Pok. 1. ker- 567.]' So 'hr' is Nourai's shorthand for the Germanic outcome *hr- of the zero grade *kr- (his gloss 'a ringing sound' comes from the OE hringan sub-entry); 'skrainjan, skrěki' are Watkins's *skrainjan and *skrēkjan- (Nourai's 'ě' for the ē of the second); 'krik' is Watkins's *krik-. Pokorny 567-571 has the same material independently ('Nasalized: Old English hringan „sound, clink“, engl. ring'; 'Old Norse hrókr, Old English hrōc, Old High German hruoh „crow“'; 'Old Norse hrafn, Old English hræfn „raven“, Old High German hraban'; 'Old Norse skrækr m. „scream“ (*skrēki-), skrækja'; 'Dutch kriek, kreke „cricket“ ... Middle English creken „creak“').\",\n          \"derivation_fa\": \"این جعبه رونوشتِ فشرده‌ای از مدخل واتکینز در پیوست ریشه‌های هندواروپاییِ AHD است — همان که ارجاع بی‌شمارهٔ «AHD» به آن اشاره دارد: «ker-2، ریشهٔ آوابنیاد ... ۱. صورت بی‌درجه *kr- که در ژرمنی *hr- می‌شود: (الف) ژرمنی *hring- در انگلیسی کهن hringan «طنین انداختن» ‹ RING؛ (ب) ژرمنی *hrōkaz «پرندهٔ قارقارکن» در انگلیسی کهن hrōc ‹ ROOK؛ (پ) ژرمنی *hraban، *hrabnaz در انگلیسی کهن hræfn ‹ RAVEN؛ (ت) گسترشِ *kri- در ژرمنی *krik- که از راه فرانسهٔ کهن criquer «جیرجیر کردن» به CRICKET رسیده. ۲. گونهٔ *skr-: ژرمنی *skrēkjan- در نورس کهن skrækja ‹ SCREAK/SCREECH، و ژرمنی *skrainjan در نورس کهن skrǣma ‹ SCREAM. [پوکورنی ۵۶۷]». پس «hr» کوتاه‌نوشتِ نورایی برای بازتاب ژرمنیِ *hr- است، «skrainjan, skrěki» همان *skrainjan و *skrēkjan- واتکینز، و «krik» همان *krik-. پوکورنی نیز در صفحه‌های ۵۶۷-۵۷۱ همهٔ این صورت‌ها را مستقلاً آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/raven\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt s.v. ker-2 (quoted in full in the derivation): every one of Nourai's three Germanic entries and all six English words of node 11 are in this single AHD entry, tagged '[Pok. 1. ker- 567]' — the same Pokorny page as the root box.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 567-571, ker-1\",\n              \"stance\": \"supports\",\n              \"note\": \"'Nasalized: Old English hringan „sound, clink, rattle“, engl. ring „lauten, clink“, Old Norse hringja'; 'Old Norse hrókr, Old English hrōc, Old High German hruoh „crow“'; 'Old Norse hrafn „raven“, Proto Norse HrabnaR, Old English hræfn, Old High German hraban'; 'Old Norse skrækr m. „scream“ (*skrēki-), skrækja, skrækta „cry“'; 'Dutch kriek, kreke „cricket, Heimchen“, French criquet, Middle English creken „creak“'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"s.vv. ring (to sound), rook n. (p.1356), raven n. (p.1305), scream (p.1405), screech, cricket (p.373)\",\n              \"stance\": \"supports\",\n              \"note\": \"'ring, intr. v., to sound ... fr. OE. hringan, rel. to ON. hringja ...; of imitative origin.'; 'rook, n., a black bird ... fr. OE. hrōc ... of imitative origin. See raven, n.'; 'scream ... fr. ON. skrǣma ... fr. I.-E. base *(s)qrei- ... an enlargement of the imitative base *qer-; see raven.'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I 415-416\",\n              \"stance\": \"supports\",\n              \"note\": \"'anord. hrafn, ags. hræfn, ahd. hraban, hram „Rabe“'; 'ahd., as. scrīan „schreien“, ahd. screi n. „Schrei“, nd. schrewen, ndl. schreeuwen „schreien“ (*skraiwian), wflam. schreemen, engl. scream ds. (*skraimian)'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"ringing, rook, raven; scream, screech; cricket\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All six English words are precisely the ones AHD lists under ker-2, so the box is faithful. ring (whence the gerund 'ringing') < ME ringen < OE hringan 'to resound' — Klein: 'of imitative origin'; rook < OE hrōc, Germanic *hrōkaz 'croaking bird'; raven < late OE hræfn < Proto-Germanic *hrabnaz, Etymonline 'from a PIE root imitative of harsh sounds', comparing Latin crepāre, corvus, Greek korax, OCS kruku. scream < ME scremen, from a Scandinavian source (Old Norse skrǣma, Swedish skräma), Skeat p.429 'orig. to cry aloud. Allied to Screech and Shriek'; screech is a later form of earlier scritch, Skeat p.430 '(Scand.) M.E. scriken, Icel. skrækja to shriek', Klein calls it a doublet of shriek. cricket (the insect) < ME criket < Old French criquet, from criquer 'to creak, rattle, crackle', of echoic origin with a diminutive suffix (Etymonline); Klein carefully separates this from cricket the game, which he takes from MDu. cricke 'stick' — Nourai's box means the insect, which is the AHD sense. Note that 'ringing' is a gerund rather than a lexeme in its own right, the only cosmetic looseness here.\",\n          \"derivation_fa\": \"هر شش واژهٔ انگلیسی دقیقاً همان‌هایی‌اند که واتکینز زیر ریشهٔ ker-2 برشمرده است، پس این جعبه امانت‌دارانه است. ring (و اسم‌مصدرِ ringing) از انگلیسی میانهٔ ringen و آن از انگلیسی کهن hringan «طنین انداختن»؛ کلاین آن را «آوابنیاد» می‌خواند. rook از انگلیسی کهن hrōc، ژرمنی *hrōkaz «پرندهٔ قارقارکن». raven از hræfn انگلیسی کهن و ژرمنی آغازین *hrabnaz؛ اتیمآنلاین آن را «از ریشه‌ای هندواروپایی که تقلید آواهای خشن است» می‌داند و با crepāre و corvus لاتین، korax یونانی و kruku اسلاوی کهن می‌سنجد. scream از انگلیسی میانهٔ scremen و خاستگاه اسکاندیناوی (نورس کهن skrǣma، سوئدی skräma)؛ اسکیت (ص ۴۲۹): «در اصل یعنی بانگ بلند برآوردن؛ هم‌خانوادهٔ screech و shriek». screech گونهٔ متأخر scritch است و کلاین آن را دوگانهٔ shriek می‌داند. cricket (حشره) از انگلیسی میانهٔ criket و آن از فرانسهٔ کهن criquet، از criquer «جیرجیر کردن»، با خاستگاه آوابنیاد و پسوند تصغیر؛ کلاین این را از cricket به معنی «بازی کریکت» (از هلندی میانهٔ cricke «چوب») جدا می‌کند و مقصود نمودار همان حشره است. تنها سستی خُرد این است که «ringing» اسم‌مصدر است نه واژه‌ای مستقل. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/raven\",\n            \"https://www.etymonline.com/word/cricket\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"(none)\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference of its own in the book; it inherits the parent Germanic node's 'AHD', which was checked there and supports every one of these six English words.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"s.vv. raven (p.1305), rook (p.1356), ring (to sound), scream (p.1405), screech, cricket (p.373)\",\n              \"stance\": \"supports\",\n              \"note\": \"'raven, n., a large bird of the crow family (Corvus corax). — ME., fr. OE. hræfn, rel. to ON. hrafn ... These words are labial enlargements of I.-E. base *qer-, *qor-, *qr-, imitative of harsh sounds.'; 'screech, intr. and tr. v. — Fr. earlier scritch, which derives from the I.-E. imitative base *(s)qrei-. See scream ... Cp. also shriek, which is a doublet of screech.'; 'cricket, n., an insect of the order Orthoptera' (kept distinct from 'cricket, n., the game. — OF. criquet ... fr. MDu. cricke „stick“').\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat pp. 397 (Raven) and 429-430 (Scream, Screech)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Raven (1), a bird ... A.S. hræfn ... Named from noise; cf. L. crepāre, to rattle. √KRAP'; 'Scream. (Scand.) M.E. scremen. — Icel. skræma, Swed. skräma, Dan. skræmme ... orig. to cry aloud. Cf. Swed. skran, a scream. Allied to Screech and Shriek. Screech. (Scand.) M.E. scriken. — Icel. skrækja, to shriek, Swed. skrika ...'.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. ker-2, and the reverse index 'RAVEN¹ ker-2'\",\n              \"stance\": \"supports\",\n              \"note\": \"RING, ROOK¹, RAVEN¹, SCREAK, SCREECH, SCREAM and CRICKET¹ are all listed under ker-2 — the exact set of node 11.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T16:33:50.144Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-257.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T16:33:55.391Z] TOOL CALL #82: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-257.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 257"
}
```


### [2026-09-06T16:33:58.279Z] TOOL RESULT

```
JSON OK
nodes verified: 11/11
node verdicts: {'plausible': 4, 'confirmed': 7}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 11, 'not_checked': 3, 'contradicts': 1}
books consulted: {'partial': 7, 'supports': 26, 'silent': 2} | by book: {'WLD': 5, 'CHEUNG': 4, 'HRN': 4, 'MON': 3, 'BRT': 2, 'BQT': 2, 'HUB': 2, 'ARY': 2, 'HJB': 2, 'KLN': 2, 'PHD': 1, 'NYB': 1, 'IEC': 1, 'SOD': 1, 'POK': 1, 'SKT': 1, 'AHD': 1}
```


## [2026-09-06T16:34:15.479Z] AGENT

Page 257 (book p. 227) verified — one entry, root **Ker 3, Qer, Qor, Qr** (PIE *ker- "hoarse cry / noisy birds", Pokorny IEW 567–571), 11 nodes. Written to `/home/sfmqrb/git/rishe/data/verification/page-257.json`; `verify_check.py 257` reports 11/11 nodes, 0 PROBLEM lines.

Verdicts: root **confirmed**; nodes **7 confirmed, 4 plausible**, 0 disputed, 0 transcription_suspect.
Ref checks: 11 supports, 1 contradicts, 3 not_checked (IRT:44 purchase-only; MON:5001 in the a'lam volumes, not held locally; node 11 has no refs).

Notable findings (all `plausible`, none rise to `disputed` at node level):
- **#1 Av. xraos** — real, but Bartholomae (cols. 535–536) has it as a *verb* "to shout", not a noun "loud noise"; and Cheung 2007 (no. 449 *xraus*) says the IE provenance "cannot be established", so the *ker- attachment is Pokorny's alone.
- **#4 kahrkatāt / kahrkā-asa** — forms and root fine, glosses loose: kahrkatāt- is specifically "cock" (Bartholomae: "eig. Kikerikitum"), kahrkāsa- is "hen-**eater**", not "eating bird".
- **#5 karkas, kark** — main claim confirmed by Horn 848–849, Hübschmann §101, and Mo'in's own footnote in Borhan. But the parenthesised **ورتک / وردیج** do **not** come from Av. kahrka-: on the very page Nourai cites (BQT:2268) Mo'in derives them from Old Indic *vartikā-* "quail" (Gk. ortyx). Only `contradicts` ref-check on the page.
- **#7 sorfeh** — Pokorny 569 does say "npers. sarfa (iran. *sarafa-) 'Husten'", so the citation is accurate, but nothing independent corroborates it (Walde-Pokorny silent, Wiktionary has no etymology, Horn 741 and Aryanpur p.363 file سرفیدن under a rival whistle-noise root).
- **#9 korūh** — confirmed, but it is a *loan* from Indian krośa/kos (Mo'in tags it [هند.]; Hobson-Jobson s.v. COSS), not phonetic descent; the arrow should read "borrowed from".

**Extraction errors: none.** I compared the JSON with `site/pages/257.jpg`; the only difference is a dropped fatha in node 9's script («کَروه ۱» printed, «کروه ۱» in the JSON) — cosmetic, owner's call.

Five web pages archived via `fetch_source.py` (Wiktionary خروس / سرفه / کرکس, Etymonline raven / cricket).
