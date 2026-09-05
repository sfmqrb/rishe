# Verification process log — verify-page-78


## [2026-09-05T05:58:07.690Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 78 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-78.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-78.json. Write /home/sfmqrb/git/rishe/data/verification/page-78.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 78` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T05:58:09.240Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T05:58:09.951Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T05:58:09.969Z] TOOL RESULT

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


## [2026-09-05T05:58:10.084Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-78.txt"
}
```


### [2026-09-05T05:58:10.102Z] TOOL RESULT

```
1	=== PDF page 78 (book page 48) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Beu 1, Bheu 1, Bhu : root of muffled sounds  (refs POK:97)
4	#1 (parent #0) [Avestan] refs=POK:97 | bučahin, buxti : howl, yell
5	  #2 (parent #1) [Persian] refs=IEC:116 | bŭ-tîmâr «بوتیمار» : a kind of bird of heron family
6	#3 (parent #0) [Pahlavi] refs=MON:606 | bŭm 1 : owl
7	  #4 (parent #3) [Persian] refs=POK:97 | bŭm 1 «بوم ١» : owl whose sight was believed to bring misfortune
8	#5 (parent #0) [Latin] refs=AHD; KLN:176,213 | bŭtîre : to make a "bu" sound ; butio : bittern ; bŭteô : a kind of hawk
9	  #6 (parent #5) [English] refs=None | bittern ; buzzard
10	--- entry 1 ---
11	ROOT [Indo-European] Beu 2, Bheu 2 : to swell, blow  (refs POK:98)
12	#1 (parent #0) [Latin] refs=LAT:138; AHD | bŭcina : trumpet, horn
13	  #2 (parent #1) [Aramaic] refs=None | bucina : horn
14	    #3 (parent #2) [Arabic] refs=BQT:318; AFA:284 | bŭq : horn
15	      #4 (parent #3) [Persian] refs=BQT:318 | bŭq «بوق» : horn
16	#5 (parent #0) [Germanic] refs=AHD | puk : bag, pocket
17	  #6 (parent #5) [French] refs=AHD:1011 | pocket, poche
18	    #7 (parent #6) [Persian] refs=MON:668 | pâkat «پاکت»
19	    #8 (parent #6) [English] refs=AHD | pocket, pouch
20	  #9 (parent #5) [English] refs=None | bosom, big, bud, boast, bucket, puff
21	#10 (parent #0) [Latin] refs=AHD | bulla : bubble, round object ; bulca : inflated
22	  #11 (parent #10) [English] refs=None | bullet, bowl, boil, bully, bullion, buckle
23	--- entry 2 ---
24	ROOT Bhâ -> redirect to Bhě
25	--- entry 3 ---
26	ROOT Bha -> redirect to Bhě
27	
```


## [2026-09-05T05:58:13.597Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-78.json",
 "description": "Read page 78 source JSON"
}
```


### [2026-09-05T05:58:13.648Z] TOOL RESULT

```
{
  "pdf_page": 78,
  "book_page": 48,
  "entries": [
    {
      "root": {
        "name": "Beu 1, Bheu 1, Bhu",
        "lang": "Indo-European",
        "refs": "POK:97",
        "gloss": "root of muffled sounds"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:97",
          "words": [
            {"translit": "bučahin, buxti", "gloss": "howl, yell", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "IEC:116",
          "words": [
            {"translit": "bŭ-tîmâr", "gloss": "a kind of bird of heron family", "script": "بوتیمار"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "MON:606",
          "words": [
            {"translit": "bŭm 1", "gloss": "owl", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "POK:97",
          "words": [
            {"translit": "bŭm 1", "gloss": "owl whose sight was believed to bring misfortune", "script": "بوم ١"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "بلبل به باغ و بوم به ویرانه ساخته - هر کس بقدر همت خود لانه ساخته",
            "poet": null
          }
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; KLN:176,213",
          "words": [
            {"translit": "bŭtîre", "gloss": "to make a \"bu\" sound", "script": null},
            {"translit": "butio", "gloss": "bittern", "script": null},
            {"translit": "bŭteô", "gloss": "a kind of hawk", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "bittern", "gloss": null, "script": null},
            {"translit": "buzzard", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Beu 2, Bheu 2",
        "lang": "Indo-European",
        "refs": "POK:98",
        "gloss": "to swell, blow"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Latin",
          "refs": "LAT:138; AHD",
          "words": [
            {"translit": "bŭcina", "gloss": "trumpet, horn", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Aramaic",
          "refs": null,
          "words": [
            {"translit": "bucina", "gloss": "horn", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "BQT:318; AFA:284",
          "words": [
            {"translit": "bŭq", "gloss": "horn", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:318",
          "words": [
            {"translit": "bŭq", "gloss": "horn", "script": "بوق"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "puk", "gloss": "bag, pocket", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": "AHD:1011",
          "words": [
            {"translit": "pocket, poche", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:668",
          "words": [
            {"translit": "pâkat", "gloss": null, "script": "پاکت"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "pocket, pouch", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "bosom, big, bud, boast, bucket, puff", "gloss": null, "script": null}
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
            {"translit": "bulla", "gloss": "bubble, round object", "script": null},
            {"translit": "bulca", "gloss": "inflated", "script": null}
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
            {"translit": "bullet, bowl, boil, bully, bullion, buckle", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Bhâ",
        "redirect": "Bhě"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Bha",
        "redirect": "Bhě"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T05:58:13.777Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T05:58:13.822Z] TOOL RESULT

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


## [2026-09-05T05:58:29.493Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','MON','AHD','KLN','LAT','BQT','AFA','ARY','LKT','SKT','LEW','WLD','SYN']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False)[:800]); print()\n\"",
 "description": "Inspect refs_online entries"
}
```


## [2026-09-05T05:58:29.655Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && ls tools/",
 "description": "List verification dir and tools"
}
```


### [2026-09-05T05:58:31.866Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<lea

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IE

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 74

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th for

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/82307409

AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Arabic/Aramaic in script (not OCRed) with German glosses; grep the German meaning or transliteration.", "notes": "Built from djvu.xml."}

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verificatio

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.", "notes": "", "cites": "entry numb

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.t

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Latin headword in bold at line start. For 193

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/W

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each sectio
```


### [2026-09-05T05:58:31.900Z] TOOL RESULT

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
page-74.json
process
sources
----
build_site.py
fetch_source.py
ganjoor.py
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


## [2026-09-05T05:58:35.013Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==106 || NR==107 || NR==108' POK_01.txt",
 "description": "Print Pokorny leaves 105-107"
}
```


### [2026-09-05T05:58:37.615Z] TOOL RESULT

```
edrig^,  bleibt  fern.
WP.  II  109,  WH.  I  98,  477,  851,  Kretschmer  Gl.  22,  258 f.  |
1.  bei-  ,ausschneiden,  graben,  höhlen^??  t
Vielleicht  arm.  pelem  ,höhle,  grabe^,  allenfalls  auch  mir.  belach  ,Kluft, Paß,  Weg^  und  kelt.  *bolko-,  -ä  in  cymr.  bivlch  m.  ,Spalte^,  bret.  boulc'h ds.,  mir.  bolg  f.  (das  g  nach  tolg  ds.)?  ^
WP.  II  110;  über  nichtexistierendes  ai.  bära  ,Offnung'^  s.  W^ackernagel' u.  Debrunner  KZ.  67,  171  f.
2.  bei-  ,stark^  I
Ai.  bdla-m  n.  ,Kraft,  Stärke,  Gewalt^,  bdllyän  ,stärker^,  bdlistha-h  ,der stärkste^;  gr.  ßslxlojv,  ßaXregog  ,besser'^,  ßelTLOxog,  ßelrarog  ,bester^  (das -T-  durch  Umbildung  von  *ßsXt(jjv,  *ß£XiaTog  nach  (peQTsgog  usw.);  lat. debilis  ,kraftlos,  schwach'^;  aksl.  boljhjh  ,größer'^,  bolje  Adv.  ,magis,  plus^ und  ,melius'.    Unsicher  ndl.-ndd.-fries.  pal  ,unbeweglich,  fest^
Mit  Dehnstufe  ai.  bäld-h  jung,  kindlich^,  m.  ,Knabe,  Kind^,  f.  ,Mädchen^
WP.  II  llOf.,  WH.  I  326f.
bend-,   bnd-no-   ,vorspringende    Spitze^,   vielleicht    in   folgenden    kelt.    und germ.  Wörtern:
Mir.  benn  ,Horn,  GipfeF  (*bnd-no-  oder  *bend-no-'>),  bennach  ,spitzig^; cymr.  bann   m.  ,Anhöhe,  Gipfel,  Hörn  {Hnd-no-J,  mbret.  ban  ,eminence;
97
.,..      ijauteur^;  gall.  "^ancle-hanno-  >  frz.  auvent  ^Schutzdach^  (eig.  ^großes
II       0    Jud  Rom.  49_,  389 f.;,  gall.  dial.  Zacws  Benäcus,  wenn  für  Bennäcns^
,      Gehörnte^  (Sirmione)^  aus  *benno-  (idg.  Hend-no-  oder  *5n(i-7io-);  west-
*j;-      «r»^  Spitze^;  mnd.  ^m^  ^penis^^  mhd.  (mnd.)  "pinz  ^subula'^;,  ags.  pintel
\s'   feil«"!,  pintle   auch    noch  ^Pflock^)^  uorw.  pintol  ^penis^,  wozu  wohl
\t  Ablaut  nhd.-bair.  pfotizer,  pf unzer  ^zugespitzter  KnütteF;  mit  den kolt  Formen  entsprechendem  /i-Suffix  (*penn-  aus  *bend-n-)  and.  pin Dixilhis^  nind.  piih  P"^^6  ^Pinne^  Spitze^  Nagel,  Pflock^,  mhd.  pfinne  f. Va^ol^  a^-s.  pinn  ^Pflock,  Stift^,  spätaisL  pinni  m.  ds.,  ablaut.  *pan7i- in  ostfries.  penne  =  pinne,  nd'd.  pennen  ,eme  Tür  (mit  einem  Bolzen) verrieo-eln'^;  ags.  on-pennian  ^öffnen^,  engl,  pen  ^schließen'^,  ags.  penn  m. ,Pferch^
Johansson  KZ.  36,  347  f.  (auch  gegen  Entlehnung  von  Pinne  aus  lat. pinna^  an  welcher  Kluge  ^^  festhält).
WP.  11  109  f.
2.  b(e)u',  bh{e)u-  schallnachahmend  für  dumpfe  Schalleindrücke,  z.  B. Uhuruf,  dumpfer  Schlag  u.  a.
Npers.  büm  ,Eule^;  arm.  bii^  buec  ,Eule'^  (ohne  Lautverschiebung  im Schallwort),  gr.  ßvag  m.,  ßv^a  f.  ,Uhu^,  ßvl^eiv  ,wie  ein  Uhu  schreien^, lat.  bübö  ,Uhu'^,  bulg.  buh  ,Uhu^,  russ.  bücJiath  ,dumpf  und  lang  anhaltend schreien^;  lit.  baublys  ,Rohrdommek,  baubti  , dumpf  brüllen^,  bubenü ,dröhne  dumpf^; 
 lat.  bütio  ,RohrdommeP,  büteo  ,eine  Falkenart^;  gr.  ßor; ,Ruf^,  ßodct)  ,schreie^  (daraus  lat.  boäre  ,rufen^),  ßcoargicj  ,rufe  an,  um Hilfe^  (*ßoJ^aaTQ6aj),  scheinen  von  solchem  bu-  aus  als  Reimworte  zu  70^, yodü)  (s.  Wz.  gou-)  gebildet.
Mit  auslautenden  Gutturalen:  ai.  bük-kära-h  ,Gebrüll  des  Löwen^, bukkati  ,bellt^  (av.  bucahin-  ,der  das  Geheule,  Gefauche  an  sich  hat', buxti'  ,Heulen,  Fauchen'^?),  gr.  ßvKTVjQ  ,heulend^
Vielleicht  mir.  böchna  ,Meer^  (,*tosende  Brandung^;  Gdf.  ^boukania)] lit.  bukcius  ,Stammler'^,  lett.  buksket  ,dumpf  schallen'^;  slav.  buk-  (aus hochstufigem  *bouk-)  in  russ.-ksl.  bucati  , dröhnen^,  serb.  bücem,  bukati ,brüllen^,  büclm,  bucati  ,tosen  (vom  Meere)^;  *biik-  in  russ.  usw.  byk ,Stier^;  über  angebl.  *bük-  in  aksl.  b^cela,  bbcela  ,Biene^  (vgl.  russ.  byMtb ,summen,  von  Bienen^)  s.  unten  bJiei-  und  WH.  I  555;  nasaliert  poln.  bqkac ,halblaut  reden,  murmeln^,  bqk  ,Rohrdommel',  alt  ,bübö^;  in  der  Anwen- dung auf  dumpfen  Schlag  russ.  biikatt,  büchath  {*bouk-s-)  ,stoßen,  schlagen, daß  es  schallt*,  buch  ,plumps!^,  serb.  bühnuti  ,losbrechen^,  busiti  ,schlagen, werfen,  stürzen,  mit  Gepolter  fallen^,  lit.  bukiioti,  lett.  baüks  ,Bezeichnung eines  durch  starken  Schlag  oder  Fall  hervorgebrachten  Schalles'^,  vermut-
7
98
licli  auch  huka  ^Faustschlag^  (auch  lit.  huküs  ,stumpf^  hierher  als  A^v\ Schlagen  stumpf  geworden^);  mhd.  huc  ^Schlag;,  Stoß^  (ohne  Lautvej! Schiebung  durch  stete  nebenherlaufende  Neuschöpfung),  puchen,  hitchel nhd.  pochen^  ndl.  heuken  , schlagen,  stoßen^,  schwed.  hoka,  bauka,  buk ds.  (aber  auch  , graben,  wühlen',  wie  aisl.  bauka-,  dies  ein  versch.  Wort? s.  auch  WH.  I  unter  faux),  engl,  to  poke  ,stoßen,  stechen^,  norw.  poi pauk  ,derber  Knüttel,  vielleicht  mir.  büalaim  ,schlage^  (*bougl .  .  .,  oder zu   bhäu-d-  ,schlagen').
WP.  II  112f.,  WH.  I  111,  119,  124,  470.
2.  b(e)u-,  bh{e)u-  ,aufblasen,  schwellen^,  Sprenglaut  der  aufgeblasenen Backe,  wie  auch  pu-,  phu  s.  d.;  nebenherlaufende  Urschöpfung  kreuzt die  lautgesetzliche  Entwicklung,  so  daß  z.  B.  germ.  Formen  mit  pu, aus  idg.  bu-,  aber  auch  aus  unverschobenem  idg.  oder  neuem  py, erklärbar  sind.  Aus  dem  Begriff  der  aufgeblasenen  Backe  entwickeln sich  die  Bedeutungen  ,aufschwellen,  rundlich  Aufgetriebenes  (dann auch  Eingewölbtes)  verschiedenster  Art^,  auch  ,anschwellen  machen, stopfen^  und  ,blasen,  husten  u.  dgl.^
Ursprünglich    verschieden    sind    die    Schall  wurzeln    1.    b(e)u-    für dumpfe  Schalleindrücke  und  bu-  ,Lippe,  Kuß^
Gr.  ßv  BTtl  Toü  f.isydXov  iXiyero'  y.al  2(J)(pQ(.ov  ßvßa,  dvTc  xov  aeavä  xai TtlrjQrj  xat  'fxsydXa  EM;  vermutlich  hierher  auch  ßovvög  ,Hügel'  (dialektisch),' ßovviccg  ,eine  Rübenarf^,  ßovvl^oj  ,häufe^,  ßovviov  ,eine  Doldenpf
lanze^;  re- dupl.  ßovßcüv  ,inguen,  Drüsen  neben  der  Scham,  bes.  in  krankhaft  ge- schwollenem Zustande^;  nisl.  püa  ,blasen,  atmend
Redupliziert  wie  ßvßa,  ßovßtjv  auch  lit.  bubsü,  bubseti  ,Blasen  auf- werfen' (von  Wasser  oder  gärendem  Teig),  mnd.  bubbeln  ,Blasen  auf- werfen, wallen',  schwed.  bobba  ,Schwulst,  Finne,  Insekt',  bubba  ,Laus'  und ,Trollius  europaeus'  u.  dgl.  (mit  idg.  bh  oder  mit  durch  Neuschöpfung verhinderter  Lautverschiebung  von  b),  anord.  byfa  {Hhübhiön-)  ,großer, klumpiger  Fuß',  norw.  dial.  büve,  büva  ,dicker,  klotziger  Mensch,  Butzen mann'.
Mit  sicherem  hh-i  ai.  bhü-ri-h  ,reichlich,  viel,  gewaltig',  Komp.  bhuyasi bhdvlyas-,  Superl.  bhüyistha-h,  av.  bidri-  ,reichlich,  völlig,  vollkommen^ Komp.-Adv.  baiyö  ,(mehr,  zeitlich  =)  länger,  auf  länger  als',  Superl.  &öt| stdm  ,plurimum';  arm.  bavel,  bovel  ,ba3tare';  lit.  bürys  ,Haufe  (Häuser)] Menge  (Schafe,  Vögel,  auch  Regen)',  lett.  bura  ,Haufe  (Volkes)';
ohne  r-Suf  fix:  aksl.  bujh  (j'^bhonio-)  ,wild,  grausam,  töricht^,  russ.  büjnyj ,ungestüm,  wild,  üppig  wachsend';  ob  hierher  ndd.  bö,  böje,  ndl.  bui  ,Bö, Windstoß,  Schauer'?;  gr.  q)6a-  i^ar&iiuaTa  h  t(^  awpaTLE.es.;  mit  Dehi
99
fe  *bhöu-  gr.-ion.  (pmösg,  att.  cpööeg  .Brandblasen^;  gr.  cpaioiy^,  (pav- ^^y?  ,Brandblase,  Blase^  (mit  Abi.  9u  neben  öu).
A  ch    die  Wz.  hheu-  .werden,   entstehen^  ist   wohl   aus   .schwellen^  ent-
•  i-nU  vo-1.  die  Bed.  von  ai.  prdbhiita-h  .reichlich,  zahlreich^  (:  bhdvati) jnit  der  von  bhiiri-h.
Erweiterungen  mit  1  sind  vielleicht:  ai.  buri-h,  buli-h  (unbel.)  .Hinter- backe weibliche  Scham'  =  lit.  buVts  (auch  büU,  bule)  .Hinterbacken',  gr. Lila'  ßsßvo^eva  Hes..  mnd.  poll  .Kopf.  Spitze.  Wipfel'  {Hulno-),  mnd. ^ull  voll  .(aufgetriebene)  Hülse.  Schote',  engl,  pulse  .Hülsenfrucht';  ab- lautend mnd.  puyl  .Sack',  puyla  .Geschwulst';  mit  bh-:  got.  iifbauljan, nur  im  Partiz.  ?t/6ai(Zic?ai. Aufgeblasene.  Hochmütige',  ahd.pawZa  f.  .Blatter'. a^s.  bnle  ahd.  'pülla,  mhd.  biule  .Beule',  anord.  beyla  .Höcker.  Auswuchs'. aschwed.  bolin,  bulin  .geschwollen' ;  air.  bolach  .Beule'  {*bhuläk-,  allenfalls bhol-  zu  bhel-  .schwellen');  arm.  boil,  Gen.  PI.  bulle  .Schar.  Menge.  Herde'. sorb.  bidjiti  .die  Augen  hervorstrecken,  glotzen'.
Dentalerweiterungen:  gr.  ßvtava'  xövöuXoi,  ol  ös  ßQvrava  Hes.  (a-hev ßvxlvri'  Idyvvog  ^  d(.ug.  TaQavzXvoi  Hes..  die  Quelle  der  germ.-rom.  Sippe von  nhd.  Blltte,  lat.  buttis  .Faß',  entspricht  gr.  ttütIvt]  .Korbflasche',  s.  pü- auf blasen');  hierher  wohl  poln.  buta  .Stolz',  bucic  sie  .prahlen'.
Ai.  budbuda-h  .Wasserblase.  Blase',  gr.  ßv^öv  frvKvöi',  avveröv,  yavqov dk  y.al  (J,sya  Hes.  {*budio-,  etwa  .aufgebläht'?  Doch  s.  unten  ßv^7]v  S.  101); norw.  püte  .Kissen',  püta  .dicke  Fra
```


## [2026-09-05T05:58:52.362Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC leaf 73 (p.116?) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==74' IEC.txt | head -60",
 "description": "Print Mann IEC leaf"
}
```


### [2026-09-05T05:58:54.075Z] TOOL RESULT

```
=== IEC leaf 73 (p.116?) ===
ce, adj. ‘useful; (*-u-) in broc "use, benefit’; Go. brüks *useful
bhrüg- (2) ‘tremble’ Illyr. in Lat. briza *quaking-grass'; OE broc- cian ‘tremble’; Pol. bryze *yellowrattle'
bhrugilos, see bhrigil-
bhrugh- 'swell, increase” Lat. fruor, fructus; Ir. broghaim “increase, advance, press', beside broghdha *exceeding; big, MHG brogen “raise, anger; rise; swag- ger
bhrughis, os, io (?) ‘construction’ Ir brugh ‘mansion; fort; MHG  brucke, brücke “bridge, stage’; OE brycg; Du. brug; cf. also OE brycgian, v. ‘pave paralleled in Russian most ‘bridge’; mosti? ‘to pave’; ON bryggja ‘gangway, pier; Latv. brugis ‘paved road?
bhrughno- (2) ‘shrubbery, rushes’. WP II, 208
107
Br. broenn; W brwyn; Cor. bron “rushes, reeds’; OE brogne ‘bush’
bhrug- (1), ‘fragment. Cf. bhrügo Gk. cf. phrüganon ‘chip, faggot’; OS brokko, OE broc, bryce, MHG brocke ‘fragment’ beside bruch ‘breakage’; Du. brok
bhrug- (2) “breast of animal, brisket, sweet- bread’ Arm. erbuc, gs erbco ‘breast of animal’; cf. Lat. frümen (‘glottiş’ if for *bhrugmn-); (Ir. brú, gs bronn “breast? is ambig. Cf. bhrondh-); OCz. brzicé “breast, dewlap’; Slovak brzica, id.; Cz. cf. brz-lík, m. 'sweetbread'. Cf. bhreuks-, bhreus-
bhrügo, io (?). Cf. bhru2- (1) Mir brüghaim, brüighim “bruise, crush, mash’; Li. brüzyti ‘scour’; cf. Latv. bruzaju ian (?) óbrüzos, adj. ‘refined, pure’ are un- certain as also Srb. briznem, -nuti "well up'.
bhruk- ‘hurt’ Olr. broc ((3) 'grie); Blg. brükam “prod, stir; Li. brukü, brükti “force, thrust, scutch'; Latv. brukt ‘collapse’. (Sw. bry ‘vex derives from LG brüden, id.) (EH)
bhruktos It. (Gallo-Lat?) brutto ‘ugly, fou; W brwth, m., broth, f. ‘turmoil; MHG bruht, wider- bruht ‘defiant; defiance’, cf. Ger. brohsein ‘riot, fuss’; Li. brükti ‘thrust; scutch'; Latv. brukt ‘crumble, collapse’; Cz. brkati, brknouti ‘jerk; shriek; flap; trip’. For Ir. bruth, broth, see bhrütos (2); cf. Srb. brka ‘muddie’.
bhrumbhalos, bhrumbhəros ‘buzzing insect’. See next Alb. brúmbull ‘bumble-bee’; Blg. brúmbar ‘cockchafer’ or sim.
bhrumbho, bhrumo, ið “hum, buzz, rumble’? MHG brummen; Du. brommen; Dan. brumme, and com. Gmc.; Pol. brzmieć; cf. Blg. brüméca ‘hum’
bhrumn- ‘welling-up, bhreumn-. WP IT, 208 Alb. (ambig.) brumë ‘dough, paste, plasma’; OHG. OS brunno ‘well, spring’; G cf. Brunst; Du. bronst “heat in animals? beside bron, as G Brunnen
(bhruniə 'trappings, harness, equipment.
ferment. See
bhrug- — bhrüs
10
15
20
25
30
35
40
45
108
A Celt. LW in Gmc.Sl. and Balt.) (Cf. bhrondh- for background of Ir. brü, gs bronn & bruinne; Br. brón ‘shoulder of pig beside bronn, W bron “breast?); Go. brunjo; MHG brünne; OE byrne ‘coat of maiľ; ON brynja, id.; OCS brünja *breast- plate’; OCz. brně ‘harness’; Cz. bri ‘armour, coat of mal: R bronja ‘armour’; OPrus. brunyos ‘trappings’; Latv. brunas, id.
bhrün- (bhreun-, bhrun-) ‘edge, top, crest, brow’. WP H, 196 & 207. Cf. bhrüs (1) Alb. bri, gs bm “tip, top, horn?” beside ` EMAIb. brinjë ‘rib, side, cliff, wall; Olr. cf. brú and Ir. bruinne “edge, shore, verge’; Cor. bron, pl. bronnow & bronyow *hill (all ambig. in view of homonymic brú, etc. ‘breast’, see bhrondh-); ON brún, pl. brýnn ‘cliff-edge, brow’ beside brýni ‘whetstone’; Dan.Sw. bryn ‘brim, edge, brow’, beside Sw. bryna ‘whetstone’; Li. (short vowel) bruns ‘brow’, beside brune ‘back of knife’; (*-eu- in) briaunà “edge, back of knife, keel. A possible link may exist (qua “acute, keen’) between Lat. frunitus ‘clever, in-frunitus ‘silly and ON brýnn “sharp, prompt'; brýna *sharpen, egg on'
bhruno, ið ‘roar, rush’. Cf. bhrumbh- ON bruna ‘rush’; OCz. brnéti ‘rumble’; Slo- vene brneti *whirr
bhrünos �
```


## [2026-09-05T05:58:54.134Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD beu ===\" && grep -n -i -E \"^(beu|bheu|bu|bhel|bhelgh|beu-)\" AHD_watkins1985.txt | head -40",
 "description": "Grep AHD Watkins roots"
}
```


### [2026-09-05T05:58:54.183Z] TOOL RESULT

```
=== AHD beu ===
60:But it must be stressed that linguistic heri- tage, while it may well tend to correspond with cultural continuity, does not imply ge- netic or biological descent. That is, there is no more reason to suppose that we, as speak- ers of an Indo-European language, are de- scended biologically from the speakers of Proto-Indo-European, than that the English- speaking population of Nigeria is Anglo- Saxon. The transmission of language by con- quest, assimilation, migration, or any other ethnic movement is a complex and enigmatic process which this discussion does not pro- pose to examine, beyond stating the general proposition that in the case of Indo- European no genetic conclusions can or should be drawn.
326:bhel-?
329:bhel-*
340:bheue-. Also bheu-. To be, exist, grow. I. Extended forms *bhwiy(o)-, *bhwi-. 1. Germanic *biju in Old Eng- lish béon, to be: BE. 2. Latin fieri, to become (third person singular present subjunctive fiat): FIAT. 3. Possi- bly suffixed form *bhwi-lyo- in Latin filius, son; but this is possibly from dhé(i)-. II. Lengthened o-grade form *bhéw- in Germanic *béwan in: a. Old Norse bia, to live, prepare (present participle bondi); BONDAGE, BOUND‘; HUSBAND; b. Middle Dutch bouwen, to cultivate: BOW- ERY; C. Old Danish bdth, dwelling, stall, akin to the Scandinavian source of Middle English bothe, market stall: BooTH. III. Zero-grade form *bhu-. 1. Germanic *buthia in: a. Old English bold, dwelling, house, hence byldan, to build: BUILD; b. alternate Germanic form *béthla in Middle Dutch bédel, riches, property: BOoo- DLE. 2. Greek phuein, to bring forth, make grow, phutos, a plant, and phusis, growth, nature: PHYSIC, PHYSIO-, PHYSIQUE, -PHYTE, PHYTO-, PHYTON; DIAPHYSIS, DIPHY- ODONT, EPIPHYSIS, HYPOPHYSIS, IMP, MONOPHYSITE, NEOPHYTE, PERIPHYTON, SYMPHYSIS, TRACHEOPHYTE. 3. Suffixed form *bhu-td- in Welsh bod, to be: EISTEDD- FOD. 4, Suffixed form *bhu-tu- in Latin futirus, “that is to be,” future: FUTURE. IV. Zero-grade form *bhii- (< *bhua-). 1. Germanic *biiram, dweller, especially farmer, in: a. Old English bir, “dwelling space,” bower, room: BOWER}; b. Old English gebir, dweller (ge-, collective prefix; see kom): NEIGHBOR; Cc. Middle Dutch gheboer, ghebuer, peasant: BorR, Boor. 2. Germanic *birjam, dwelling, in Old English byre, stall, hut: BYRE. 3. Suf- fixed form *bhi-lo- in Greek phulon, tribe, class, race, and phulé, tribe, clan: PHYLE, PHYLETIC, PHYLUM; PHY- LOGENY. V. Suffixal forms in Latin. 1. *du-bhw-io-, “being two,” in Latin dubius, doubtful, and dubitdre, to doubt (see dwo-). 2. *pro-bhw-o-, “growing well or straightforward” (see per'). 3. *super-bhw-o-, “being above,” in Latin superbus, superior, proud (see uper). VI. Possibly Germanic *baumaz (and *bagmaz), tree (? < “growing thing”), in: a. Old English béam, tree, beam: uel b. Middle Dutch boom, tree: BooMm?. [Pok. bheu- 146. bheug-'. To flee. 1. Zero-grade form *bhug- in Latin fugere, to flee: FUGACIOUS, FUGITIVE; CENTRIFUGAL, FEVERFEW, REFUGE, SUBTERFUGE. 2. Extended form *bhuga in: a. Latin fuga, flight (> fugdre, to drive away): -FUGE, FUGUE; FEBRIFUGE; b. Greek phugé, flight: APOPHYGE. [Pok. 1. bheug- 152.] bheug-2. To enjoy. Nasalized zero-grade form *bhu-n-g- in Latin fungi, to discharge, perform: FUNCTION, FUNGI- BLE; DEFUNCT, PERFUNCTORY. [Pok. 4. bheug- 153.] bheug-*. To bend; with derivatives referring to bent, pliable, or curved objects. 1. Germanic *baugaz in: a. Old English béag, a ring: BEE?; b. Old High German boug, a ring: BAGEL. 2. Germanic *bugon- in: a. Old English boga, a bow, arch: Bow’; b. compound *alino- bugén-, “bend of the forearm,” elbow (*alino-, forearm; see el-'), 3. Germanic biégan in Old English bigan, to bend: Bow?, BUXxOM. 4. Germanic causative form *baug- Jan in Old Norse beyla, a swelling, akin to the probable Scandinavian source of Middle English baile, baill, a handle: Barn’. 5. Germanic *buhtiz in Old English byht, a bend, angle: BIGHT. 6. Celtic *buggo-, “flexible, mallea- ble,” in Scottish and Irish Gaelic bog, soft: BoG. [Pok. 3. bheug- 152.] bhilo-. Dear, familiar. Possible source of Greek philos, dear, loving (> philein, to love): -PHILE, -PHILIA, PHILO-, -PHILOUS, PHILTER; PAM. [Pok. bhili- 153,] bhiad-. To worship. Suffixed form *bhildd-(s)men- in Latin flamen, priest (of a particular deity): FLAMEN. [In Pok. bhlag-men- 154.] bhlag-. To strike. 1. Germanic *blak-, perhaps in the probable Scandinavian source of Middle English bakke, bat: BAT?. 2. Latin flagrum, a whip (> flagellum, little whip): FLAGELLATE, FLAGELLUM, FLAIL, FLOG. 3. Latin
1326:BUSTARD awi- BUSTLE s(w)e- BUT ud- BUTCHER bhugo- BUTT! bhau- BUTTER gWou-, teue- BUTTOCK bhau- BUTTON bhau- BUTTRESS bhau- BUTYRIC g¥ou- BUXOM bheug-3 BUZZARD beu-2 BY! ambhi BYRE bheue-
```


## [2026-09-05T05:59:04.321Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 78 79 80; do echo \"=== IEC leaf $((n-1)) ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' IEC.txt | grep -n -E \"^1[0-9][0-9]$|bu-|bub|bou\" | head -20; done",
 "description": "Locate IEC page 116"
}
```


## [2026-09-05T05:59:04.803Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"beu-1\\|beu-2\\|beu-3\\|beu-\\*\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD beu roots"
}
```


### [2026-09-05T05:59:06.126Z] TOOL RESULT

```
=== IEC leaf 77 ===
15:115
=== IEC leaf 78 ===
11:116
21:117
23:bhubbh- (expressive variant of above) ‘mut- ter, burble’ OE à-byffan; Latv. bubinaju, id. See next
24:WP II, 114. See bubul- Lat. bullio (assimilated consonants); MLG bubbeln; Du. bobbelen; OCS bübljo, čti & -ati; Alb. bubullon (3sg *thunder); Cz. be- blati, Pol. bebłać ‘stammer; slobber’
26:bhubhos, à (bhubbh-) (1) ‘creature, monster’ Hitt. pupus (queried) ‘paramour, concubine’ Alb. bubë ‘grub’; LW in Srb. buba, Blg. bùba, id. and ‘bogey’; Lat. bufo 'toad' is ambig. cf. bhudh-; Ir. bob ‘trick’; MIr. boban ‘calf; Gael. ‘boy’; OFris. bobba, wm. “child”; E dial. bob *flea-beetle'; Sw. bubba ‘cockroach’; Slo- vene beba ‘dolt’; (Gmc. forms with -b-, -bb- are fr. bhubbh-); Li. bübis, io, Latv. bubis ‘spook’
27:bhubhos, à (bhubbh-) (2) “lump, swelling; crest’ Arm. cf. bbuk (dim. type, a-st. ‘crest, comb’); Rum. (substr.) bubă ‘tumour’; Ir. cf. bubán ‘coxcomb’; Du. bof (3) ‘mumps’ beside bobbekop (‘big-headďd’, fr. *bhubbh-); E bob (fr. *bhubbh-) beside dial. bub ‘breast’; Li. bubas *ball, pellet, egg, apple', etc.
28:bhubhos, ó(n) (3) ‘noise’. Cf. bub-, bubul-, etc. Arm. bbun ‘noise’; Du. bof (1) ‘thud’; cf. Li. baübti ‘bellow’ beside bübauti, id. (*-ou-/ -ü-) beside (*-u-) bubu, eti, id.
=== IEC leaf 79 ===
1:, à, is) "ball, round creature, bubble’. Cf. bubul- and bhubhos (2) Arm. bubul ənkujz ‘walnut’; Lat. bulla (dial. or expressive: “boss, knob, stud, seal, bubble’. Assim. as in barba is also possible); MHG (Alemannic type) popeln ‘bubble’; G bub- beln, id.; LG Bobbel, bobbeln, s & v id.; Fris. Du. bobbel “lump, pimple, bubble'; Sw. bubbla v. ‘bubble’; Cz. dim. bebelka ‘louse’; Li. bubulis, io “ball, pellet; Latv. bubulis "knot in yarn’
12:118
14:. side būzen ‘swell, sprout'; E bout; Fris. bût
20:bhudhmn- (bhudno-) “base, bottom, stock, stump, root, stone'. WP II, 190 Skt. budhnáh, -ám; Av. buno; Per. bun; Oss. bín, bun, beside bíndur, cpd. (bín + dür “boundary stone; farm); LW in Arm. bun (i-st. ‘trunk, root, origin); Gk. puthmén; cf. Gk. (Anatolian? Phryg.?) púndax "bottom", cf. bhrgh- for a ref. to pürgos; Alb. bun “mark, goal; spring-head, mountain hut? be- side buzém *yule-log', fr. *bhudhimn-); Lat. fundus; MIr. Ir. bun "base, root, foot? beside bond, bonn “sole of foot; Mir also bunne ‘spring, source’; Gallo-Lat. bodina *bound- ary; Br. men bonn (‘boundary stone’. LW in OFr. bonde, E bound); W bon 'stem, base, stock; OBr. cf. bon-ed ‘race, nobility: W bonedd, id.; Ligur. cf. Bodin-cus (river-name of Po, said to mean *bottomless"); variants in OHG bodam; Du. bodem as against OE botm; ON botn; Cz. cf. bedna “chest, box’;
21:119
25:bhudho(n) (2) “creature” Gk. puthón; (Rustic) Lat. bufo (*toad', assi- milated conss. as in barba, bulla) beside LLat. bufus, bufa a poisonous insect; Lat. cf. also fullo ((2) ‘earwig’, fr. *bhudlon, cf. E bottle 'fly); Ir. bod ((boor, cpds. *'bird") (the expected form *bodán does not occur); SWG Butten 'polecat; LG budde “earth- worm, louse’; OE budda ‘beetle’; EME boude *corn-worm'; ONorw. budda ‘young animal’
```


### [2026-09-05T05:59:06.166Z] TOOL RESULT

```
321:yawn, gape: BAY2, BEVEL; ABASH, ABEYANCE. 2. Possibly Vulgar Latin *abbaidre (> Old French (a)baiier), to bay: BAY‘*.] [battuere. To beat. Latin verb of unknown origin. (BATE?), BATTER!, (BATTER’), (BATTERY), BATTLE; ABATE, COMBAT, DEBATE, (RABBET), (REBATE?), (RE- BATO).] bel-. Strong. 1. Suffixed o-grade form *bol-iyo- in Russian bol’shoi, large: BOLSHEVIK. 2. Prefixed form *dé-bel-i- (dé-, privative prefix; see de-), “without strength,” in Latin débilis, weak: DEBILITATE, DEBILITY. [Pok. 2. bel- 96.] bend-. Protruding point. 1. Germanic *pannja-, “struc- ture of stakes,” in Old English penn, pen for cattle: PEN2. 2. Germanic *pund- possibly in Old English pund- (> Middle English pound), pundfald, enclosure for stray animals: POND, POUND3; IMPOUND, PINFOLD. 3. Germanic *pin- in Old English pintel, penis: PINTLE. [Pok. bend- 96.) beu-'. Also bheu-. Appears in words loosely associated with the notion “to swell.” I. Root form *beu-. 1. Ger- manic *puk- in: a. Old English pocc, pustule: POCK; b. Old French po(u)che and Old North French poke, bag: POACH!, POCKET, POKE3, POUCH, (PUCKER). 2. Old Eng- lish pyffan, to blow out: puFF. 3. Old English -piite, “fish with large head” (in aele-piite, eelpout): pouT?. II. Root form *bheu- with various Germanic derivatives. 1. Old English bdsm, bosom: Bosom. 2. Old English biic, belly, pitcher: BUCKBOARD. 3. Frankish *biak (> Old French buc), trunk of the body: TREBUCHET. 4. Old English bye), pustule: BorL?. 5. German dialectal baustern, to swell, akin to the source of Middle English bost, a bragging: BoasT!. III. Root form *beu-. 1. Latin bulla, bubble, round object, amulet (> Old French boule and Spanish bola, ball): BILL!, BILLET!, BOLA, BOULE?, BOWL’, (BULL?2), BULLA, BULLATE, BULLET, (BULLETIN); BOULE- VERSEMENT. 2. Latin bullire (> French bouiller), to bubble, boil: BOIL!, BOUILLON, BUDGE!, (BULLION), BULLY?; BOUILLABAISSE, EBULLIENCE, GARBOIL, PAR- BOIL. 3. Possibly Latin bucca (> Old French boucle, buckle, curl, and Spanish boca, mouth), (inflated) cheek: BOCACCIO, BOUCLE, BUCCAL, BUCKLE!, BUCKLE?; DE- BOUCH, DISEMBOGUE, EMBOUCHURE. 4. Greek boubén, groin, swollen gland: BUBO. [Pok. 2. beu- 98.] beu-2. Root imitative of muffled sounds. 1. Latin bitié (perhaps > Old French butor), bittern: BITTERN!. 2. Latin bited, a kind of hawk: BUZZARD. [Pok. 1. b(e)u- 97.] bha-'. To shine. Contracted from *bhas-. 1. Germanic *baukna-, beacon, signal, in: a. Old English béac(e)n, beacon: BEACON; b. Old English denominative bécnan, biecnan, to make a sign, beckon: BECKON. 2. Perhaps Germanic *bazja-, berry (< “bright-colored fruit”), in Old English berie, berige, berry: BERRY. 3. Germanic *bandwa-, “identifying sign,” banner, standard, sash, also “company united under a (particular) banner,” in: a. Spanish banda, sash: BANDOLEER; b. Late Latin ban- dum, banner, standard: BANNER, (BANNERET). 4. Suf- fixed form *bhaw-es- in Greek phds (stem phét-), light: PHOS-, PHOT, PHOTO-; PHOSPHORUS. 5. Extended and suffixed form *bhan-yo- in Greek phainein, “to bring to light,” cause to appear, show, and phainesthai (passive), “to be brought to light,” appear: FANTASY, (PANT), PHANTASM, (PHANTOM), PHASE, PHENO-, PHENOMENON; DIAPHANOUS, EMPHASIS, EPIPHANY, HIEROPHANT, PHAN- EROGAM, (PHANTASMAGORIA), PHOSPHENE, SYCOPHANT, THEOPHANY, (TIFFANY). [Pok. 1 bha@- 104.] bha-2. To speak. Contracted from *bhaa-. 1. Latin fari, to speak: FATE; AFFABLE, (FANTOCCINI), INEFFABLE, IN- FANT, (INFANTRY), PREFACE. 2. Greek phanai, to speak: -PHASIA; PROPHET. 3. Suffixed form in Germanic *ban- wan, *bannan, to speak publicly (used of particular kinds of proclamation in feudal or prefeudal custom; “to proclaim under penalty, summon to the levy, declare
1299:BILBERRY bhel-2 BILINGUAL dnghi BILIRUBIN reudh-1 BILIVERDIN virére BILL! beu-1 BILL? bhei-2 BILLS = bhei-2 BILLET! beu-1 BILLET-DOUX = dik-u- BILLOW bhelgh- BILTONG bhel-2, dnghi BIMESTRIAL mé-2 BIN bhendh- BINAL dwo- BINARY dwo- BIND bhendh- BINNACLE ghabh- BINOMIAL nem- BIO- gW¥ei-
1309:BITE bheid- BITTER bheid- BITTERN! beu-2 BITUMEN gWet-1 BIVOUAC ambhi, weg-2 BLACK bhel-1 BLACKMAIL méd- BLADDER bhié-2 BLADE bhel-3 BLAIN bhlei- BLAME bha-2 BLANCH bhel-1 BLANCMANGE bhel-1 BLAND mel-1 BLANDISH mel-1 BLANK bhel-1 BLANKET bhel-1 BLARE bhié-1 BLASPHEME bha-2 BLASPHEMOUS bha-2 BLAST bhlé-2 -BLAST melst- BLASTEMA melst- BLASTO- melst- BLASTULA melst- BLATHER bhlé-2 BLAZE! bhel-1 BLEACH bhel-1 BLEAK! bhel-1 BLEAK? bhel-1 BLEAT bhlé-1 BLEMISH bhel-1 BLENCH! bhel-1 BLEND bhel-1 BLENDE bhel-1 BLENNY mel-1 BLESBOK bhel-1, bhugo- BLIND bhel-1 BLINDFOLD bhel-1 BLINI mele- BLINTZ mele- BLISTER bhlei- BLITE mele- BLITZKRIEG bhel-1, gwere-2 BLOAT bhieu- BLOND bhel-1 BLOOM! bhel-3 BLOOM? bhel-3 BLOSSOM bhel-3 BLOW! bhié-2 BLOW3 bhel-3 BLUE bhel-1 BLUNDERBUSS (s)tene- BLUSH bhel-1 BOARD bherdh- BOAST! beu-1 BOAT bheid- BOATSWAIN bheid- BOCACCIO beu-1 BODE! bheudh- BODEGA dhé-1 BODHISATTVA bheudh-, es- BoER bheue-
1311:BOIL? beu-1
1312:BOLA beu-1
1314:BOOM? bheue- BOON! pbha-2 BOON2 deu-2 BOOR bheue- BOOT? bhad- BOOTH bheue- BORDELLO bherdh- BORDER bherdh- BORE! bher-2 BORE’ bher-1 Boreas gWero-1 BOROUGH bhergh-2 BORROW bhergh-1 BORSCHT bhar- BOSCAGE busk- BOSOM beu-1 BOTH ambh6o BOTHRIUM bhedh- BO TREE bheudh- BOTTOM bhudh- BOTTOMRY bhudh- BOTULIN gWet-3 BOTULINUM gWet-3 BOTULISM gWet-3 BOUCLE beu-1 BOUGH bhaghu- BOUILLABAISSE beu-! BOUILLON beu-1 BOULDER bhel-2 BOULE! gWele-1 BOULE? beu-! BOULEVARD bhel-2, werg-
1318:BOUTIQUE dhé-1 BOUTON bhau- BOVINE g¥ou- Bow? bheug-3 Bows bheug-3 BOWEL gW¥et-3 BOWERY bheue- BOWER! bheue- BOWL! bhel-2 BOWL? beu-1 BOWSPRIT sper-4 BOX! puxos
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1326:BUSTARD awi- BUSTLE s(w)e- BUT ud- BUTCHER bhugo- BUTT! bhau- BUTTER gWou-, teue- BUTTOCK bhau- BUTTON bhau- BUTTRESS bhau- BUTYRIC g¥ou- BUXOM bheug-3 BUZZARD beu-2 BY! ambhi BYRE bheue-
1414:DEAN dekm DEATH dheu-3 DEBACLE _bak- DEBASE bassus DEBATE battuere DEBAUCH bhelg- DEBENTURE ghabh- DEBILITATE bel- DEBILITY bel- DEBIT ghabh- DEBONAIR deu-2 DEBOUCH beu-1 DEBRIS bhréi- DEBT ghabh- DECA- dekm DECADE dekm DECAGON dekm DECALESCENCE kele-! DECALOGUE Ieg-* DECANAL dekm DECANT kanto- DECAPITATE kaput DECAY kad- DECEASE ked-
1555:GAR? garwian GARAGE wer-5 GARB garwian GARBLE kreij- GARBOIL beu-1 GARDEN gher-1 GARFISH ghaiso- GARGET gere-4 GARLIC ghalso-, leug-1 GARMENT wer-5 GARNER gre-no- GARNISH wer-5 GARRET wer-5 GARRISON wer-5 GARRULOUS | gar- GARTH gher-! Gas ghéu-
2106:POCK beu-1
2112:POINT peuk- POINT-DEVICE weidh- POINTILLISM peuk- POISE! (s)pen- POISON pO(i)- POKE’ beu-1 PoLack pele-2 POLE! kwel-1
2406:TRAPUNTO peuk- TRAUMA tera-1 TRAVAIL pag- TRAVE treb- TRAVEL pag- TRAVESTY wes-4 TRAY deru TREACLE ghwer- TREAD der-1 TREADLE der-1 TREASON d6- TREAT tragh- TREBUCHET beu-1 TRECENTO dekm, trei- TREE deru TREFOIL bhel-3 TREMATODE tere-! TREMENDOUS trem- TREMOR trem- TREMULOUS trem- TRENCH tera-2 TREPAN! tere-1 TREPHINE trei- TREPID trep-1
```


## [2026-09-05T05:59:32.586Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LAT leaf 156 ===\" && awk 'BEGIN{RS=\"\\f\"} NR==157' LAT.txt | head -40",
 "description": "Print Ernout-Meillet p.138"
}
```


## [2026-09-05T05:59:33.914Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFA leaf 314 ===\" && awk 'BEGIN{RS=\"\\f\"} NR==315' AFA.txt | head -40 && echo \"=== AFA grep bucina/buq ===\" && grep -n -i \"bucina\\|bûq\\|buq\\|Trompete\\|Horn\" AFA.txt | head -30",
 "description": "Print Fraenkel p.284 and grep"
}
```


### [2026-09-05T05:59:34.893Z] TOOL RESULT

```
=== LAT leaf 156 ===
bucerus
138
correctement par yvaOoC, genae, maxillae. a° bouch^e. - Ancien, usnel.
Panroman, M.L.1357; iri . boccoit, britt. boch, bogail.
Derives: buccula £. : 1° bouchee; joues (au pl.); 3 ° mentonnibre decasque
et tout obj et en forme de joue: bosse de bouclier, tringle de cata-
pulte: (b. lat.) sorte de vase (= bucculdre, -is ), M.L.1364; bucculentus
(Pl .), buccosus (Gloss.): joufflu; buccella (b. lat.): 1° bouchee, miette;
a° petit pain, M.L.1359,1360 (cf. 1358 buccdta); buccelldgd (plin.Val.);
buccellarius (-risj : synonyme tardif de satelles "a buocellis uel
buccellato appellatus" (Thes.). Cf. buccellatum: biscuit, pain de
munition, M.L.1361; (b)uccellatariZ,-turii, -torii , sana doute ancien
mot de la comedie, conserve par 1 es gloses qui le traduisent par
parasituli ; bucco, -onis m.(et buccus); grande bouche, bavard, sot;
de la: bucco, -as (Gloss.), bavarder, M.L.1363. - *imbuccare, M.L.
4385.
Composes: buccifer, duribuccius, debuccellatus, tous rares et tardifs.
II se peut que bucca soit d'origine celtique, et se soit substitue
dans la langue populaire & os et a gena comme etant plus expressif;
cf. beccus, celtique lui aussi. Buccus, Bucco, Buccio sont des noms
celtiques; cf. aussi Buccidcus (uicusj = Boissy, et Buccelenus dux
Francorum; Buccioualdus , eveque de Verdun, cf. Greg. Tnr.9,83: Buccioual-
dus ... ferebant enim hunc esse superbum, et ob hoc a nonnullis buccus
ualidus uocitabatur.
Mot expressif, sans correspondant hors du latin.
bucerus, bucerlus, -a, -um: aux comes de boeuf. Transcription du
gr. ( 3 ou>ceptoC^ pouxepaoC, atteste depuis Lucr.
bucetum: v. bos.
bucina, -ae f.: trompette; V6g. Mil.3,5, tuba quae directa est ap¬
pellatur, bucina quae in senet aereo circulo flectitur. - Ancien,
usuel. Les langues romanes 'attestent bucina et bucina (ce dernier,
sans doute d'aprbs les adj. en -tnus, uaccinus ), M.L.1368; britt. begin.
- bucinus m.: joueur de trompette (forme vulgaire ponr bucent). - buci¬
num: 1° son de trompette, trompette; a° coquillage, pourpre. Denominatif:
bucino, -as , M.L.1369 (et de-, di-bucino ), bucinator. Cf. aussi M.L.1365
bucellum, v. h. a. buhhi la.
Mot italique (gr. puxavri est d'origine latine). Sans doute compose
de bou- et -cana (Cuny, M 61 . F. de Saussure, p.109 et suiv.).
buda, -ae f.: ulve, herbe des marais. Cf. Claud. Don. Ae. a,135, ulu-
am... quam uulgo budam appellant. M.L.1371.
```


### [2026-09-05T05:59:37.032Z] TOOL RESULT

```
=== AFA leaf 314 ===
284
Sias TOD Telmalire Assem. Bibl. Or. II. 104 und nach dem-
selben Barh. bist. eccl. I. 361. Nöld.).
iJlls »einen Fiirsten mit Freadengeschrei empfangen**
(Belaijori 131, 3 a. f.) ist natürlich nur Ableitung yon xx^
A^^ , das auch in*s Aramäische als D vp und «£2^;^ (jr .r; ^}
••I •
übergegangen ist.
^-j ist entlehnt aus ll^^o D^3'p^3 {hiicina). Dass
Mu^irr. 30 durch aramäische Vermitteluug aus pers.
entstand, hat schon Nöldeke ZDMG. XXX. 418
bemerkt: ijo kennen schon die Araber (llu'arr. 30) als
fremd; sie suchen es allerdings aus dem Persischen zu er-
klären. ßapßuTZ'j fehlt übrigens in den aramäischen Dialec-
ten. Der Ursprung von «^^0. das man kaum von der
Wurzel ^\ »glänzen" ableiten kann, ist mir dunkel. >^I^
Mu'^arr. 94 muss allerdings mit auäälligeni Lautwandel aus
K*113^I7 entlehnt sein, oj »Pauke" ist wohl Entlehnung
aus S2in Us-^; Jli aus S^Di: (i^' Lagarde Ges. Abb.
201; ..vJs zu np.
Merkwürdigerweise haben die Araber den Räuber, da sie
doch selbst eine Nation von Räubern waren, (*^37 Gen,
XXI. 13 übers, das Targüm 0*^120^ *13/; milyorum rapa-
dum similes (Ammianus Marcell. XIV, 4, 1; Ketuböth 112^
(Rauber)) mit einem fremden Namen ^>^. ^JQi aus A^o--
rsf^ benannt. Zur Assimilation vgl. Guidi Della sede 16.
VARIA.
ÄAJ% »Himmel" ist gewiss entlehnt aus sy^PH. Bei
Oauhari wird es schon aus dem Hadit beleiht; es kommt
auch wohl nur in dieser theoloüfischeu Spraclie vor. Um
=== AFA grep bucina/buq ===
```


## [2026-09-05T05:59:50.004Z] TOOL CALL #14: Bash

```json
{
 "command": "pdftoppm -f 78 -l 78 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg78 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 78"
}
```


## [2026-09-05T05:59:51.681Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN 1966 bittern/buzzard ===\"; grep -n -i \"bittern\" KLN_1966.txt | head -10; echo \"--- 1971 ---\"; grep -n -i \"bittern\\b\" KLN_1971.txt | head -10",
 "description": "Grep Klein bittern"
}
```


### [2026-09-05T05:59:52.295Z] TOOL RESULT

```
total 7492
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 01:59 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 01:20 ..
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
-rw-rw-r-- 1 sfmqrb sfmqrb   22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb  445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58318 Sep  5 01:45 mk70.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   63822 Sep  5 01:59 pg78.png
```


### [2026-09-05T05:59:52.357Z] TOOL RESULT

```
=== KLN 1966 bittern/buzzard ===
1502:acrimony,  n.,  harsness,  bitterness;  asperity.  —  L. dcrimdnia,  ‘sharpness,  pungency’,  formed  fr.  L. acer  (fern,  acris,  neut.  acre),  ‘sharp’,  with  suff. -monia.  See  acrid  and  -mony  and  cp.  words  there referred  to.
5085:bitterling,  n.,  a  small  fish  (Rhodeus  amarus).  — Formed  from  the  adjective  bitter  with  suflf. -ling;  so  called  from  its  bitter  flavor, bittern,  n.,  a  heronlike  bird.  —  ME.  bitour,  fr. OF.  (==  F.)  butor,  fr.  VL.  *buti-taurus,  a  com¬ pound  of  L.  bated,  butio,  ‘a  kind  of  falcon  or hawk’,  and  taurus,  ‘ox’,  L.  bated  derives  fr. htttire,  ‘to  cry  like  a  bittern’,  which  is  of  imi¬ tative  origin  and  lit.  means  ‘to  utter  the  sound hiT.  Cp.  L.  hubere,  a  synonym  of  butire  and bubo,  ‘owl’,  and  see  Buteo,  Bubo.  For  the  second clement  in  VL.  *bdti-taurus  see  Taurus.  The reason  why  in  VL.  *buti-taurus  the  bittern  is compared  with  an  ox,  may  be  best  explained  by a  passage  in  Pliny  (10,42),  in  which  the  author
5087:relates  that  in  Gaul  the  bittern  was  called  taurus (i.e.  ‘ox’)  because  of  its  voice  suggestive  of  the bellowing  of  oxen.  For  the  suffixed  -n  in  bittern cp.  marten.
5088:bittern,  n.,  the  bitter  liquid  remaining  after  the crystallization  in  saltworks.  —  A  derivative  of bitter,  adj.
5958:Buteo,  n.,  a  genus  of  hawks,  the  buzzard.  —  L. bitted,  ‘a  kind  of  falcon  or  hawk’,  rel.  to  biitire , ‘to  cry  like  a  bittern’  (lit.  ‘to  utter  the  sound bu),  from  the  I.-E.  imitative  base  *bit-,  whence also  L.  bubo,  ‘owl,  horned  owl’.  Cp.  Bubo.  Cp. also  bittern,  buzzard.
5984:Derivatives:  buzz,  n.,  buzz-er,  n. buzzard,  n.  —  ME.  busard,  fr.  OF.  bus-ard, formed,  with  change  of  suff.,  fr.  OF.  buis-on, bus-on  (a  regressive  derivative  of  which  is  F. base,  ‘buzzard’),  fr.  L.  biitednem,  acc.  of  buted, ‘a  kind  of  falcon  or  hawk’.  See  Buteo  and  cp. bittern.
13925:exasperation,  n.  —  L.  exasperatio ,  gen.  -dnis,  ‘ex¬ asperation,  bitterness’,  fr.  exasperdtus,  pp.  of exasperdre.  See  prec.  word  and  -ion. excambion,  n.,  exchange  of  land  (Scot,  law)  — ML.  excambium.  See  ist  ex-  and  cambium  and cp.  exchange.
20734:kitchenette,  n.  —  A  hybrid  coined  fr.  kitchen with  -ette,  a  sulf.  of  French  origin, kitchen  midden,  refuse  marking  a  primitive  hu¬ man  settlement.  —  Dan.  kjokken  madding,  lit. ‘kitchen  midden’.  See  kitchen  and  midden, kichery,  n.  —  A  variant  of  kedgeree, kite,  n.  —  ME.  kite,  fr.  OE.  cyta,  ‘kite,  bittern’, rel.  to  ciegan  (for  orig.  *kaujan),  ‘to  call’,  MHG. ( stein-)kuze ,  G.  Kattz,  ‘screech  owl’,  MLG. kitten,  ‘to  chatter,  babble,  prate’,  LG.  kdter (whence  G.  Kdter),  ‘cur,  dog’,  fr.  I.-E,  base *gou-,  *gow-;  ‘to  shout,  cry’,  whence  also  OI. gavate,  ‘sounds,  resounds’,  Gk.  yoav,  ‘to  wail, groan,  weep’,  yooq,  ‘wailing,  groaning,  weeping’, OE.  cyme,  ‘fine,  beautiful,  splendid’,  orig.  ‘frail, delicate,  tender’.  See  comely, kith,  n.,  now  used  only  in  the  phrase  kith  and  kin. —  ME.  cuththe,  kith,  fr.  OE.  cydd(u)-,  ‘know¬ ledge,  acquaintance,  relationship;  native  coun¬ try’,  fr.  cud,  ‘known’,  pp.  of  cunnan,  ‘to  know’. See  can,  aux.  v.,  and  cp.  uncouth, kitling,  n.,  a  small  kitten.  — -  ME.,  fr.  ON.  ket- lingr,  ‘kitten;  young  of  other  animals’,  dimin. of  kdttr,  ‘cat’.  See  cat  and  dimin.  sufF.  -ling, kittel,  n.,  a  white  cotton  robe  which  pious  Jews wear  during  the  High  Holiday  services,  and  in which  they  are  buried.  —  Yiddish  kitel,  fr.  G. Kittel,  ‘frock,  coat’,  fr.  MHG.  kittel,  kitel,  ult. fr.  Arab.  qu(n,  ‘cotton’,  whence  also  G.  Kattun, ‘cotton’ ;  see  cotton.  For  the  ending  -el  in  kittel see  the  suffixes  -el  and  -le. kitten,  n.  —  ME.  kitoun,  a  blend  of  kitling  and ONF.  caton  (corresponding  to  OF.,  F.  chaton), ‘little  cat’,  dimin.  of  ONF.  cat  (corresponding to  OF.,  F.  chat),  ‘cat’.  See  cat  and  cp.  kittle,  ‘to bring  forth  kittens’,  kitty,  ‘kitten’.
38297:Taurus,  n.,  1)  a  constellation,  containing  the Pleiades  and  Hyades;  2)  one  of  the  signs  of  the zodiac  (astron.)  —  L.  taurus,  ‘bull’,  cogn.  with Gk.  Taupop,  OSlav.  turu,  ‘bull’,  Lith.  tauras, ‘aurochs’,  OPruss.  tauris,  ‘bison’;  prob.  of  Sem. origin.  Cp.  Aram,  lord,  ‘ox,  bull,  steer’,  Heb.  shdr, Akkad,  shuru,  Arab,  thor,  Ethiop.  sor,  of  s.m. Cp.  also  steer,  ‘young  ox’,  toreador,  torero,  toro and  the  second  element  in  Minotaur.  Cp.  also the  second  element  in  bittern, taut,  adj.,  drawn  tightly,  tense.  —  ME.  toght,
--- 1971 ---
30203:bittern, n., a heronlike bird. — ME. bitour , fr. 
30207:butire, ‘to cry like a bittern’, which is of imi- 
30212:reason why in VL. *buti-taurus the bittern is 
30215:relates that in Gaul the bittern was called taurus 
30217:bellowing of oxen. For the suffixed - n in bittern 
30220:bittern, n., the bitter liquid remaining after the 
35906:‘to cry like a bittern’ (lit. ‘to utter the sound 
35909:also bittern, buzzard. 
36064:bittern. 
131627:kite, n. — ME. kite, fr. OE. cyta, ‘kite, bittern’,
```


## [2026-09-05T06:00:01.828Z] TOOL CALL #16: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg78.png"
}
```


### [2026-09-05T06:00:02.154Z] TOOL RESULT

```

```


## [2026-09-05T06:00:02.151Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T06:00:13.381Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 78 -l 78 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg78_600 && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg78_600.png'); print(im.size)\n# scale factor from 1700-wide render to 600dpi\nw,h=im.size\nsx=w/1700.0\nbox=(int(350*sx),int(1210*sx),int(900*sx),int(1320*sx))\nim.crop(box).save('bulca.png')\nbox2=(int(350*sx),int(320*sx),int(900*sx),int(400*sx))\nim.crop(box2).save('avestan.png')\n\"",
 "description": "Crop bulca and Avestan boxes at 600dpi"
}
```


### [2026-09-05T06:00:17.670Z] TOOL RESULT

```
(5100, 6600)
```


## [2026-09-05T06:00:19.786Z] TOOL CALL #18: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bulca.png"
}
```


### [2026-09-05T06:00:19.801Z] TOOL RESULT

```

```


## [2026-09-05T06:00:23.440Z] TOOL CALL #19: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/avestan.png"
}
```


### [2026-09-05T06:00:23.466Z] TOOL RESULT

```

```


## [2026-09-05T06:00:30.821Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT bucahin/buxti ===\" && grep -n \"bucahin\\|buxti\\|bužahin\" BRT.txt | head -20",
 "description": "Grep Bartholomae"
}
```


### [2026-09-05T06:00:30.864Z] TOOL RESULT

```
=== BRT bucahin/buxti ===
17321:*,«K«Sfl,.    _    .)  Opt.,   oder  «ich  Kon>«  ^^;  buxtiS  njnia  ahf-i  Vtiv47.      '
25953:•  j.  saSay-  Adj.  —  ?  — :  buxtiS  nqma ahmi  'ilis  nama  ahmt  Yt  15. 47.  Geringe Stelle.
```


## [2026-09-05T06:00:31.857Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==79' IEC.txt | sed -n '1,30p'",
 "description": "Print IEC leaf 78 fully"
}
```


### [2026-09-05T06:00:33.560Z] TOOL RESULT

```
; OE byrd ‘fate’; Du. beurt ‘turn, lot; OFrankish, cf. staim-bort (a weapon: *stone-throwing catapult’)
bhrt- (2) ‘bearing, load, product. WP II, 153. Cf. bhero, bhoros
bhrsos, ios, à, is — bhübh-
15
20
25
30
35
40
45
116
Sk. bhrtíh; Av. borotis; Olr. brith; Go. ga- baürps, baürpei; MHG burt; bürde; OE byrd; ON byrð, f. beside byrór “birth; load"
bhrt- (3) “boring, bore, hole, hollow’. Cf. bhraio ON byrða “bin, trough”; Pol. barc, Cz. brt, R bort ‘hollow in tree, hive of wild bees’
bhrtós, á “borne, carried'. Cf. bherð Sk. bhrtáh; Av. boroto; Per. bilà ‘alms’; ON burór (*bearing?, etc.)
bhrug- (bhorug-, bhor-) ‘neck, windpipe’. Cf. bhrug- Oss. bárzài ‘neck’; Gk. phárux (& phárugx); ON barki
(bhru-, see bheru-. Z-gde radical in Per. balwà ‘tumult; OE brymm, m. ‘surf, sea”, prob. also in MHG brunne ‘spring’; ON brunnr, id.)
bhruos, à “arch, span, beam, bridge’. (prob. variant of bhruu- q. v.) Gaul. brivo-, brio-, briva (‘bridge’, in place- names); ON brú; Sw. bro, id.; Blg. brúvi, Srb. brv “sleeper; footbridge’; OCz. břev, pl. břvi, f. ‘beam, rafter’; cf. OCS brüvno ‘beam’; Cz. břevno, Ukr. berveno; Slovene bruno
bhū- (bhüu-) (1) theme of verb ‘to be’. Cf. bhüio & bhui-. WP II, 141 Skt. á-bhut, pf., bhütáh, pp.; Av. büta, npl.; Per. budan, inf; Gk. phüs, m. ‘son’ beside Hes. pháos ‘plant’; phué ‘growth’, éphün, aor., etc: Ir. budh (was, 3sg);; W OBr. bu, wd: Lat. Dm. id. beside OLat. fuam ‘may be’ and OBr. bi “will be’; OS bū, OE bü ‘dwelling’; Norw. bu ‘booth’; ON búi ‘dweller’; bua “dwell, be’; beside byggva ((populate', fr. *bhuu-); OHG bü, gs buwes ‘farming’; OCS byxü, etc. ‘was’; Li. būvis, 10, m. ‘creature’ beside buvau “I was’; Latv. büveju ‘I build”
bhū- (2) ‘howl, gale, blast. Cf. bhübh- Arm. bu (o-st. 'owl) beside buk, pl. form “gale, storm’; Per. cf. bü timàr ‘heron’; Phryg. or Mac. büza ‘owl’; Du. bui ‘squall’; cf. Lat. butio and MIr. bufa (‘bittern’, fr. *bhuuo-). Sw. rágn-by (LW < Du.)
bhübh- “a hooting animal’. WP II, 112 Arm. bbun (/noise', fr. *bhübhon); Lat. bübon (owl, w. assimilated consonants) beside bū- bulo, are (onomat. *büb-); MIr. cf. búbaire,
117
m. ‘bittern’; Li. bübe ‘heifer’ beside bübauti ‘bellow’
bhubbh- (expressive variant of above) ‘mut- ter, burble’ OE à-byffan; Latv. bubinaju, id. See next
WP II, 114. See bubul- Lat. bullio (assimilated consonants); MLG bubbeln; Du. bobbelen; OCS bübljo, čti & -ati; Alb. bubullon (3sg *thunder); Cz. be- blati, Pol. bebłać ‘stammer; slobber’
bhubhlos, see bhubhulos
bhubhos, à (bhubbh-) (1) ‘creature, monster’ Hitt. pupus (queried) ‘paramour, concubine’ Alb. bubë ‘grub’; LW in Srb. buba, Blg. bùba, id. and ‘bogey’; Lat. bufo 'toad' is ambig. cf. bhudh-; Ir. bob ‘trick’; MIr. boban ‘calf; Gael. ‘boy’; OFris. bobba, wm. “child”; E dial. bob *flea-beetle'; Sw. bubba ‘cockroach’; Slo- vene beba ‘dolt’; (Gmc. forms with -b-, -bb- are fr. bhubbh-); Li. bübis, io, Latv. bubis ‘spook’
bhubhos, à (bhubbh-) (2) “lump, swelling; crest’ Arm. cf. bbuk (dim. type, a-st. ‘crest, comb’); Rum. (substr.) bubă ‘tumour’; Ir. cf. bubán ‘coxcomb’; Du. bof (3) ‘mumps’ beside bobbekop (‘big-headďd’, fr. *bhubbh-); E bob (fr. *bhubbh-) beside dial. bub ‘breast’; Li. bubas *ball, pellet, egg, apple', etc.
bhubhos, ó(n) (3) ‘noise’. Cf. bub-, bubul-, etc. Arm. bbun ‘noise’; Du. bof (1) ‘thud’; cf. Li. baübti ‘bellow’ beside bübauti, id. (*-ou-/ -ü-) beside (*-u-) bubu, eti, id.
bhubhulos, à, is (bhubhlos
```


## [2026-09-05T06:00:49.717Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT Geheule/Gefauche ===\"; grep -n \"Gefauche\\|Geheule\" BRT.txt | head; echo \"=== BRT bucahin variants ===\"; grep -n -E \"buc.ahin|bucah|bušahin|buc?ahin\" BRT.txt | head; echo \"=== BRT around buxtis ===\"; sed -n '25945,25960p' BRT.txt",
 "description": "Grep Bartholomae variants"
}
```


### [2026-09-05T06:00:49.796Z] TOOL RESULT

```
=== BRT Geheule/Gefauche ===
17319:joM 'erheUt',  Miii!:*  (NS.) 'Arzt',  —  VgL*j^  •   j.  bucah'in-    Adj.   'der   das  Geheule,
=== BRT bucahin variants ===
17319:joM 'erheUt',  Miii!:*  (NS.) 'Arzt',  —  VgL*j^  •   j.  bucah'in-    Adj.   'der   das  Geheule,
=== BRT around buxtis ===
ai.  vgl.  iatoTiira'  Adj.,  Bein,  du  fiinav.  — Vgl.  'vTra-  No.  I.  —  PQ.:  lOQ  vTr.
•  j.  satö.raodana-  Adj.  'mit  hundert  Fen- stern versehen':  nmäfum  ..  °n>m  ..hata- urBjtunsm  Yt.5.  loi.
•  j.  satö-stüna-  Adj.  'auf  hundert  Säulen ruhend,   hundertsäuh'g':  nmätutn  . .  * hazaarS.frasHmban>m  V.1S.2S.
Pü.:  too  la».
•  j.  sato.straDha-  Adj.  (fem.  'ishä-)  "mit hundert   Juwelen  (?)    besetzt':    pusau. •aham  saranalfilm  Yt.  5.128.
'ilranha-  m-,  Bed.?;  ob  zu  iilsr-'i
•  j.  sala'nah-  m.  EN.  eines  Gläubigen: ultrake  'naishs  a^aotiB  "des  U.,  Sohns  des S.  .."  Yt./?.iis.
Komp.:  saia'-\.*aah-  Adj.,  zum  ai.  V.  m etwa  sva.  Ei'msraf.
•  j.  saSay-  Adj.  —  ?  — :  buxtiS  nqma ahmi  'ilis  nama  ahmt  Yt  15. 47.  Geringe Stelle.
•  j.  saSa-  f  1)  "Erscheinen,  Aufgehen' derGestime:  hakpr?l  zT irixtahe(s±)  °laya- (LS.)fa  vamaife  starasla  mäsca  kvortca V.  -2.  40.  j)  'Gutscheinen,  Gefallen, Zufriedenheit':  *'o*'>  (IS.)  F.  12.
KompA.  —  Zum  V.  ^sand-,  —  zBed.  vgl.  ai. chanda-  m.  —  PO.  (dRn.):  sahel  (3S.},  Harlan- dlh.—  I)  Hds,  vaür,  aber  unter  den  Wörtern für  J-;  -e  für  -ya,  %  26S.  32.
j.  taiSMnqm  N.  36:  lies  gai'.
'].  faiii  satre  Vyt.  79:    gemeint   ist   laÄ-zj
j.  sal-väslrahe  N.  _J/;  lies  isal.v'.
•  j.  safa-  ra.  'Huf  des  Pferdes:  aurvants..
sroawna  aisqm  'fänhüY.^j.tT.  a)  'Huf- stilck,  Stück  eines  Pferdehufs':  'fim  vä  ää- lirum  vä  zfm.var>tpm  vä  kqmBt  vä  xrüh äismanqm  "ein  Stück  Huf  oder  einen  Holz- klotz oder  einen  Erdklos  oder  sonst  ein Trumm  harter  Erde''  V.p.  11.
```


## [2026-09-05T06:00:51.963Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v1 بوق ===\"; grep -n \"بوق\" BQT_v1_pages.txt | head -20; echo \"=== BQT v1 بوتیمار ===\"; grep -n \"بوتیمار\\|بوتیمار\" BQT_v1_pages.txt | head -10; echo \"=== BQT v1 page 318 marker ===\"; grep -n \"\\[pdf page\" BQT_v1_pages.txt | head -3",
 "description": "Grep Borhan-e Qate vol1"
}
```


### [2026-09-05T06:00:52.039Z] TOOL RESULT

```
=== BQT v1 بوق ===
2963:دوش متواريك بوقت محر اندر آمد بخمه‌آن دلیر. فرخی.
9091:۵ -یسکون ها. کلمه است که‌بوقت
9814:بوقلمونت و آن نوعی از دیبای رومی. باشد که
10091:کاو؛ آهنگر بوقت کار کردن بر میان خود
13485:او میدامتته - وبوقلمون را نیز گوشه .
14587:فرش ازآن کتاب مالی نقاش باشد - و بوقلمون
15807:درمشن برهان) هم تن مرن درخت ساخته » و هرسالی بوقتی رسیدن زیتون » این‌سودالی
17686:در آن کار نکند الا روز شنبه بوقت غروب] فتاب
17864:و آ ش‌پرستان بوقت ستایشو پرستشآش پردست
18086:نهند بوقت شکافتن - و پینه را نیز گویند که‌بر
19666:و جابی‌را نیز کویند که میوه‌های‌خوشبوق‌در آنجا
20315:بوقت شکافتن چوب بررخنة آن نپند .
22097:۴ - نظر بوقوع آن درماه بهمن بکثرت . ۵ - این نامر معجم‌البلدان
23695:و بافند گان بوقت بافند کی بای 2 گذارند
29426:ماخته خشك کنند و بوقت حاجت مموشانند
=== BQT v1 بوتیمار ===
=== BQT v1 page 318 marker ===
```


## [2026-09-05T06:00:57.446Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17315,17325p' BRT.txt",
 "description": "Print Bartholomae bucahin context"
}
```


### [2026-09-05T06:00:57.489Z] TOOL RESULT

```
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


## [2026-09-05T06:00:58.132Z] TOOL CALL #25: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:318 --image 2>&1 | head -60",
 "description": "Fetch Borhan-e Qate page 318"
}
```


### [2026-09-05T06:00:59.736Z] TOOL RESULT

```
no scan of BQT covers printed page 318 (see 'scans' in refs_online.json)
```


## [2026-09-05T06:01:13.721Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -5 BQT_v1_pages.txt && echo \"...\" && grep -c \"\" BQT_v1_pages.txt && echo \"=== markers ===\" && grep -n -m5 -E \"^\\s*\\[.*\\]\" BQT_v1_pages.txt | head && echo \"=== ff count ===\" && python3 -c \"print(open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().count('\\f'))\"",
 "description": "Inspect BQT v1 pages file"
}
```


## [2026-09-05T06:01:14.535Z] TOOL CALL #27: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\"",
 "description": "Show BQT ref config"
}
```


### [2026-09-05T06:01:15.265Z] TOOL RESULT

```
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
...
32486
=== markers ===
1174:[است]» پارسی گر دان‌هر چه نیکوتر» چنانکه‌|ندر وی نقصانی نیفتد. پس گو ید
3634:[ وجه.] ماضی آن خواهد بود ؛ بمعنی میل کردن ومیل کرد » از که شنيد ؛
6503:[ ش هر ] هب - بکس رابع . کنابه از
15567:[ رك : بهلوی ] عکومت ابران مث‌روطه است که در ۱۳۲4 قمری با موافقت و صوب‌مظفرالدین
17761:[ازارباب انواع ] ناج را نگهبانی کند) و آن از عالیترین القاب بابلی است که بدو پلدشاه بز رکه
=== ff count ===
776
```


### [2026-09-05T06:01:16.998Z] TOOL RESULT

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
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209",
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


## [2026-09-05T06:01:21.958Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 536 537 538 539 540; do echo \"===== leaf $n =====\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -50; done",
 "description": "Print BQT v1 leaves around 318"
}
```


### [2026-09-05T06:01:23.686Z] TOOL RESULT

```
===== leaf 536 =====
بورش
باشد که درخانةُ ل و کنند. :
بو د بطش « با ناك بتحتانی رسیده .
وطای حطی مکسور بشین قرشت زده» بیونانی ۱
جوهربت که آنرا مرفشیشا گوبند و آن چند
قفم میباشد : بعریی حجر النور خسوانند و ور
دوا های چشم بکار بر ند گوست اک بر گردن
کودك بندند نترمد .
بور بفتح اول و سکون انی و زای
هوز, سبزبی که بسبب رطوبت برروی نان وجامه
و گلیم وپلای وامثال آن بهم میرسد - و زنبور
سیاهرا نیز گویند که برروی کلها نشبندب و تنه
درخت را نیز کفته‌اند و ضم اول وئانی مجهول.
اسب نبله که رنکش بفیدی کرابد و اسب‌جاد
وتند و تیز را هم میگویند ۴ - و مردم تیزفهم
و صاحب ادراگ را نیز بطربق اسنعاره بوز گویند
چنانکه‌مردم بی‌ادرال کند فهم‌را کودن خوانند ۴
و کودن اسب کمراء بالانی باشد .
وز بضم اول و سکون انی و زای
فارسی؛ گرافی وسنگینی نب وحرارت باشد -
ویفتح اود گرداب را گویند .
بو زار ؟ جم اول و نانی مجهول و زای
نقطه دار بالف کشده و برای می‌نقطه زده ؛ ادوبة
حاره بهء‌نی داروی کرم یکه درطعامها ریز ندهمجو
فلفل وقرنفل ودارچینی وامثال آن. 9
ود لك جتح اول بر وزن حوضك »
بمعنی بوز است ؛ و آن سبزبی باشد که بسبب
رطوت بر روی نان و گلیم و پلای وامثال آن
شدد ۰
نف
ود کف بم اول وفتح کاف وسکون
ثانی وثالث و نون و دال امد . صقه و ابوان را
کونند. وبا رای پفرشت هم‌بنظر آعده است.
بو هخا ت با میم بر وزن کوسفند ؛
کیاهی ماشد‌یغامت خرشوی» ویا رای می‌نقطه حم
بشظر آمده است
هه - ضم اول و قح ثالث »
و میم ۰ بجع بوزمند است که یاه خوشبو
باشد .
ود فه - منم اول و کسر الت و فتح
نون» ممونرا گونند» و دعر بیحمدو نه خوانده ۳
بو له » منم اول و زای فارسی و فتح
تون. غنجه و شکوفه و بهار درخت را کوش دکه "
هنوز نشکفته باشد» وآنرا بعربی کم خوالند.
بور نینه بروزن موی چینه. بوزئه را
کویندکه میمون باشده .
لو ده ه بروذن کوزه» شرابی باشد که
از آرد برنج و ارزن و جو سازند ودر ماوراءالنهر
و حندوستان ۹۹ بسیار خور ند و یه درخت را
یز کوید ٩‏
===== leaf 537 =====
- ۳۷۷ -
لو س» با ناتی مجهول » مخنف بوسه
است وبعربی قبله کویند ۱ - و بوسه کننده -
رامر بپوسیدن هم‌هست- و بائانی ممروف سخنی
- وفروننی را گویند .۶
نوستان افر وز- کلی اس 9
آنرا تاج خروس کویند بسبب شباهتی که بدان
«أرو ۳
بوستان گل نمای- کنابه‌از آسمان
هاشث .
توسحاق » با حای حطی بروزن
روستاق: عطلاخه‌ای باشنف ۴ ونام‌کانی است ۵ زحمله
کانهای فیروزة نیشابور که فیروزه آنرابوسحافی
وبواسحاقی هردو میگوبند ۴ -وبسحاق اطعمه را
بتحتانی ۳ 7 زده.نام 1 تیاو ره
- کیلکی علاط .
بوشاصب
دوازده مقام موسیقی ۵ .۳
بوسه شکستی - کناب از
وبوسه کردن پرصدا باشد .
و یه بفتح اود و کسر نانی و سکون
شین قرشت » بمعنی تفدیر باشد کد قدرت داشئن
است - و بسکون انی کر و فر و خود نمابی را
کوبند ۱ - و منم اول و کسر انی ۰ بمعنی
هستی وبودن وبعربی کون خوانند ۷ - وسکون
نانی شیافی باشد که از دربند می‌آورند و آن را
موسمدن
بوش دربندی میخوانند ۸ . گوند آن رستئیی
باشف که در مك اری ٩‏ هم هیرسد و آن را
می‌کوبند و شباف ساخنه ی آورند - سر 9
و خدك است در اول » ورمهای گرم را نافع
باشد .
بوشاد با تانی مجهول بی وزن فولاد ؛
بلفت بونانی شلغم خام را گوبند.
بو شاسب*۱ ۰ با نانی مجهود بوزن
ی
۱ - موسی خالرو را در آب می‌نشانی
۴ رك : شب ۷ وده ح 4 ورگ :
فرعون بوش جو را در غلر میکشانی .
بوش‌الدریندی ب
۶ - دراوستا 805۳۷258
فصل ٩۸‏ ید ۲٩‏ آعده :
تلبلی آورد . در بشدهش بوستی ص ٩‏ :
دیدن گرفته شده. بوشکور بلخی کوید :
شنیدم که خسرو بگوشامب دید
و زرشت بهرام کوبد :
نه در بیدار گفتم نه ببوشاسب
«بشت ۲ ص ۲۰4 ناب ۱ :
چنان کاآ تثی شد شورش بد.د.
نگوم جز بیش خی گفعلس::
===== leaf 538 =====
لهراسب ؛ بممتی خواب دیدن باشد و جربی رژبا
خوانند .
بوشیاس - بضم اول و سکون ثانی
مجهول و الث و بای فارسی بالف کشیده و بسین
بی‌نقطةٌ زده» نممئی بوشاسب است که‌خواب‌دیدن
وروّبا اشد ۱ ۴
بو شفح- - با جیم بروزن هوشنگه »
نلم قصبه ایست از خراسان» ومعرب آن فوشنج
ات ۴ ۷
لوصیر- منم اول و سکون ثانی و صاد
می‌فقطه بتحتانی رسیده و برای قرشت زژده . لغئی
بعرییآ نرا آذان‌الدب خوانند من ی کوش خرسء
بسبب شباهتی که بدان دارد - و بسضی گویند
نوعی از ماه زهره است و آن پوست درختی
باشد بغایت سیاه و آن را بعربی شیکران الحوت
کویند وبعضی دیگر گننه‌اند بافلای شامی‌است»
واه اعلي .
بو طا نيه - باطای حطی بروزن‌ساطانیه,
پوست ددختی است که آن را بمربیکرمة السودا
و بفارسی سیاه دارو خواتند ۰ و آن مانند عشفه
پردرخت پیچد .
او جصی - نم اول و سکون ثانی
و غی نقطه دار عضوم بلام زده و صاد بی نقطة
مضموم بثون زده » لفتی است بونانی ۴ » وههمی
۱ ک ۱ : پوشاست.
مس 0 اس
آن مربی ان الئور است که گلوزبان باشد ؛
وآن دوابی است ممروف» ویضی گونند این‌لت .
رومی است. ۱
بونج نم اول و سکون ثانی و فتح
غین نقطه دار و نون و چیم ساکن . شوئیز را
کوه 2 و ان تفن است ره .و سا وگ
و عربی حبة السودا خوانند - و فوشنج را نیز
کفته اند و آن ضبه ایست در خراسان تزديك
قندهار ۴ .
وه » بر وزن صوف » پرنده ایست
که بنحوست اشتهار دارد » و آنرا بوم نیز
گونده . ۳
بو فروش» بکر فا , عطار و مك
فروی را گوبند . :
وق - نم اول و سکون ثانی و قاف »
سفید مهرء باشد و آن چیزیست که در حمامها
وآسیاها و هنگامها نوازند" - و با انی مجهول
چادر بزرکی باشد که رختخواب درآن بندند .
بو قلمون -
دیبای رومی را گونند,
و آن جامه ات که
هراحظه برتگی‌تماید
و کنابه‌از کمی‌است که
هرساعت خودرا برنگی
===== leaf 539 =====
۳۵
که جانوری بگیرد خود را مشکل آن جاور
کتد و حربارا یز کفته اند , و آن نوعی از
چلیاسه بائد که حرضس برنگی نمابد - و نام
مرفی هم هست ٩‏ - و کنابه از دیا و عالم است
پسیب حوادث - و ال مفرق سنگه پشت را
بوفلمون میگویند .
و قیصا - با قلف بتحتانی رسیده و ساد
بی‌فطه بالف کشیده , بلفت بونانی درخت سفیدار
باشده وآن نومی ازیید است ۴ - و بعضی درخت
پده و پشه غال را یز گفته اند که بحربی‌شجرة
البق خوانشد .
و لگ - بن اول و سکون ثانی و کاف »
مشفف بو دکه» ودباش که» باشد. مه نمنی‌است
دبعربی عسی و لمل کویند - و بمعنی مگر حم
هست که کلمةٌ استثنا باشدب و نرجمة فرش هم
هت بفتح فا. - ونوعی ازآتش کیره هم هست
وجابی باچاهی که غله درآن پنها نکنند.
لو گان - با کاف فارسی بروزن خوبان»
بچمدان و زهدانرا گوبند» و بعربی رحم خوانند
۳ بمعتی کلزار هم بنظر آمده‌است.
بو کلاث » بفتحکاف‌ولام‌بروزن کوچکك»
میوه ایست مفزدار که آنرا ون گویند و ترکان
چتلافوچ و عربان حبالخضرا خوانند.
بوك و هگر - با میم و کاف فارسی
بروزن کوه کمر , بممتی بوكث است و مرادف
ای کف کب[ هن ی
و لعلکوبتد .
بو لححدر بالام و خای نفطه دار
و جیم و دال بی نقطه بروزن گل بر سرء ملحد
(۱) چك : حرچیزی .
۱ رك : فرحنگه روستایی ص ۰۷۲۵۸
۴ رده : بوالخدر .
هی
و بی دین و بی دبات باشد ۳ .
بو لنحك - بفتح لام و سکون نون
و جیم مفتوح بکاف زده ۰ هرچیز (۱ ) عجیب
وغرب وطرفه باشد که دیدن‌آن خنده‌آورو ۴
بو لو - منم اول و لام وسکون هر دو
واو» بلغت بوتانی 6 بمعتی بسیار باشد که عربان
کثیر گوبند .
بو لو بو دبون با اول و الث وبای
ایجد هر سه بواو رسیده وفتح دال بی‌قطه وبای
دیگر بوا و کشیده وینون زده» لغتی‌است‌بونانی ۷
و معنی‌آن بعری یکثیرالارجل باشد منی بسپاریاه
است » وآن دوابی است مشهور و بتازی‌اضرای-
الکلب خوانند ؛ و بجای بای‌آخر بای حطی هم
بو لو طر بخون - نتح طای حطی
و رای ی قطه حتالی رسیده و خای نقطه دار
بواو کشیده و بنون زده » لغتی است بونانی ۸
===== leaf 540 =====
بو عادران
باینمهنی عربی است - و زمین شیار نکرده رانیز
گفته اند - و جاو مقام و منزل و مأوا را هم
کویند ۱- و بمعنی سرشت و طبیعت نیز آمده
ات و سم او و فتح ثانی بمعني «باشم»باشد
که از بودن است
بو ماددان- نم کیامی است مابل
بکمودت و نیزی ,
و گل کبودی‌دازدوبعربی
فیصوم خوانند ۴ .
بومادان .
بعذف دال ۰ بمعنی
بومادران اسنت که نام
گیاهی باشد عابل به
کمودت و تیزی .
بو ماره بر وزن‌جوباره,نامپر نده‌است
غیر معلوم .
بوم کند باکاف بر وزن سودهند »
خانه‌ای را گوشدکه در زیر زمین کنند بجهت
کوم‌فندان ومسافران .
بومهی ۴ - بفتح ات و ها و سکون
نون, زمین لرزه‌بائد که‌بمربی زلرله خوانند؟ -
۱ - یر ایستا
۵
ورود کوسفندی را ن ز کون دکه از سکن باه
نکرده باشند ۵, ویمعنی اول بسکون نالث حم
آهله است ؛ راين اصح تم
او ههسین ع بر وزن‌خوشه چن. بمعنی
ارل بومهن است کمزازله و زمین لرزه باشد. ۷
ون « بفتح اور و سکون انی و نون.
بمعنی حصه و بپره باشد - و نم اول زهدان
و بچه دان‌که بعربی رحم کویند - وآسمان را
نیز گفته اند - و بن و نهایت و پابان و انتهای
هر چیز باشد ۷ - و رود گوسفند وگاو وامثال
آن کهآ نرا باك لکرده باشند .
بو فلس 4 - ینم اول و انی و سکون‌اك
ودال ابجد » بمعنی آهستگی باشد - و بفتح ثانی
و کسر انی بمعتی باشند - و مرد صاحب‌نخوت
و هدتی را نیز گوبند .
بو فده - بن اول وئانی وسکون‌ثالك
و فتح دال ابجد . مه‌نی هرود هته وربا لگنج
باشد - و بفتح ثانی و کسر ثانی مرد با حستی
و هیبت و ساحب نخون را کویند . ٩‏
لو ۵ » سم ٌم اول و فتح ثانی ۰ درختی‌را
گویند که هر کز بار و ثمر ناورد - و مردم
آهسته را نیز کنته‌اند ۸
۲ص ۳۱ ۰ ۱۷۱ ۰
سنابی غزنوی بدوممتی آورده :
کشوری را که عدل عام تدیف
بوم در بومش ایچ بام ندید .
```


## [2026-09-05T06:01:43.890Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL -o bqt538.jpg \"https://archive.org/download/borhan-ghate-v1/page/n538_w1200.jpg\" && file bqt538.jpg && ls -la bqt538.jpg",
 "description": "Download BQT vol1 leaf 538 image"
}
```


### [2026-09-05T06:01:46.727Z] TOOL RESULT

```
bqt538.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1240x1754, components 1
-rw-rw-r-- 1 sfmqrb sfmqrb 207980 Sep  5 02:01 bqt538.jpg
```


## [2026-09-05T06:01:48.574Z] TOOL CALL #30: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt538.jpg"
}
```


### [2026-09-05T06:01:48.600Z] TOOL RESULT

```

```


## [2026-09-05T06:02:02.183Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL -o bqt538_big.jpg \"https://archive.org/download/borhan-ghate-v1/page/n538_w2000.jpg\" && python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt538_big.jpg'); print(im.size)\nw,h=im.size\nim.crop((int(0.08*w),int(0.05*h),int(0.35*w),int(0.10*h))).resize((int(0.27*w*2),int(0.05*h*2))).save('bqt538_head.png')\nim.crop((int(0.10*w),int(0.83*h),int(0.75*w),int(0.90*h))).save('bqt538_fn6.png')\n\"",
 "description": "Crop BQT page header and footnote"
}
```


### [2026-09-05T06:02:05.810Z] TOOL RESULT

```
(2479, 3508)
```


## [2026-09-05T06:02:08.082Z] TOOL CALL #32: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt538_head.png"
}
```


### [2026-09-05T06:02:08.094Z] TOOL RESULT

```

```


## [2026-09-05T06:02:28.740Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt538_big.jpg')\nw,h=im.size\nc=im.crop((int(0.10*w),int(0.055*h),int(0.28*w),int(0.085*h)))\nc=c.resize((c.width*3,c.height*3), Image.LANCZOS)\nc.save('bqt538_head2.png'); print(c.size)\n\"",
 "description": "Higher-res header crop"
}
```


### [2026-09-05T06:02:30.416Z] TOOL RESULT

```
(1341, 318)
```


## [2026-09-05T06:02:32.789Z] TOOL CALL #34: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt538_head2.png"
}
```


### [2026-09-05T06:02:32.801Z] TOOL RESULT

```

```


## [2026-09-05T06:02:51.263Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD bum ===\"; grep -n -E \"^b[uū]m|būm|būm \" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB bum ===\"; grep -n -E \"\\bbūm\\b|\\bbum\\b\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep MacKenzie and Nyberg for bum"
}
```


### [2026-09-05T06:02:51.320Z] TOOL RESULT

```
=== PHD bum ===
PHD.txt:292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
PHD.txt:5166:awešant nirfs- nirfsišn l-2warz warz- warzāwand waržāg warzbūm warzīgar warzīdan warzišn warčašm warišn ward- wardānāg wardēn- wardénidan wardyiin F*wardagih wardag
=== NYB bum ===
533:problem of the Prs pass. suff. was conclus- ively solved by Schaeder, UJ XV, 560- 570; conjectural solution already in Ver- bum 210-212, where the MPrs examples are collected; the starting point of the explanation was furnished by the J-Prs forms dealt with by Salemann, Z. mittel- pers. Passiv, Bull. de d’Ac. Imp. des sciences de St.-Petersbourg XIII, 1900, 269-276.
1037:bim [bwm; ‘RK?’] land, landed estate _SPrs: 16; 914, 8112, — Av. OP (969) būmē-; Paz. NP bum.
2196:kandan [HPLWN-tn', kndn'] kan- 1. to dig, pl. kand engraved 113%. — 2. to destroy 4271, 7114. 9918; to tear up by the root 3316, — 3. bé ~ to throw out, to drive away 34’. — Two different vbs.: 1. Av. OP (437 sg.) 2kan-‘ to dig’, whence also gukān- (g. v.); 2. kan- ‘to throw’, whence also apakandan, frakandan, par- gandan, Morgenstierne, AO I, 249; Ver- bum 172. MPrs and NP ‘to dig’, Paz. cadan, xan- with an initial x- confirmed by the Arab. lw. randag ‘trench’ and Skr khan- (pt. khāta-). V. also kanišn.
3087:pattai [pt’y] lasting, durable, v. dagr- pattäi. — Pres. stem pt’y-: pattüy- < *pattāv- according to the SW rule, inf. ptwtn', pt?dstn': pattütan pattāyistan ‘to last’; MPrs pres. pt’y-; MPrth pt. ptwd ‘to endure, to bear’, hw-pt^w ‘possessed of good endurance’ (A-H III); side- form pattük < *pati-tuvaka-; from pati + Av. (638 sq.) ltav-. S (v. Gloss.); Ver- bum 209; Ghilain 77. Cf next w.
4137:vigräs- [wgl’s-] pres., to rouse a p. from sleep, from the dead: apäc vigräsend 10179; d(h) vigrasend 101°. — Av. (511) lgar-, v. guhräyenitan; MPrth wygr’s ‘to awake’, MPrs ‘to rouse from sleep’; Ver- bum 196; Ghilain 82, 92-93.
4269:embarrassment in dealing with these terms. The translator of Vd. 8%, who quite correctly felt that vačpyo is a pass., borrowed the Av. vb. (1322 sg.) vaēp- (otherwise not attested in Milr as far as I know) and formed from it the pass. pt. viftak, then, likewise correctly interpret- ing vaepayö (vačpayant-) as an act., form- ed from viftak the caus. vb. viftén-, but, by assimilating it formally to viftak: vifténitak, created a bizarre mixture of act. and pass. The same curious contra- diction is found in DD, purs. 719-7 which is, however, closer to the Av. original: viftak and vépénitak. Our passage 82° has chosen a mitigating vb. ‘to seduce’, *vr- dip-: MPrth pres. wdyfs- ‘to be cheated’, wdybyšn ‘error, aberration’, wdyb-gr ‘im- postor’, wdyftgyft ‘deceit’, Ghilain 81 sg.; Arm. lw. vrép < *vidép ‘oblique, pervert- ed; fault, error, depravation’; MPrs pres. wyyb- (viyéb- < "videp-), also contracted wyb-, pass. wyfs-, pt. wyft(g), abstr. wyyftgyh = viyiftageh (also wyf-), wdyb *deecit certainly borrowed from NW ; v. Verbum 173. 198; Ps. wydyptk’n "those who have gone astray’. BP wdypt >
4278:viyift or vihift, abstr. vihifiakéh ‘sodomy’ BdA p. 2078, pres. *vidēp- > viyép- > vihep- with the alternation of intervocalic -y-: -h-. This vb. has a so well defined Ablaut-series and ends so clearly in -p that it cannot be combined with Av. (670 sq.) !dab- ‘to deceive’ (against Ver- bum, l. e.). — Anklesaria's second MS has wdyptk w wyhypynytk = viyiftak u vihe- penitak = Paz. vehéfta u vehevnida, thus with two coordinated predicates (against Cod. K) as the Av. text has it, but not with the Av. vbs.
6499:bum: ~
```


## [2026-09-05T06:02:52.073Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN Eule ===\"; grep -n \"Eule\" HRN.txt HUB.txt | head -20; echo \"=== HRN bum ===\"; grep -n -E \"b[uû]m\" HRN.txt | head -20",
 "description": "Grep Horn and Hübschmann"
}
```


### [2026-09-05T06:02:52.125Z] TOOL RESULT

```
=== HRN Eule ===
HRN.txt:2437:238. {2)hum, baf'^) *Eule\ n^\
HRN.txt:2438:arm. btt, biiec 'Eule' (H. No. 59); lat. bübö; gr. ßvac^
=== HRN bum ===
834:2) 'zähle, rechne* (das Verbum ämartan ist nicht belegt) ;
934:anzunehmende Zwischenbedeutung 'bummeln' vermitteln
1303:Ein ganz anderes Verbum scheint efgenden, ewgenden
2033:gegebene Verbum baytan 'schenken', päz. baxsfdan,
2443:ap. "^bumimadana- (Spiegel, Ar. Periode 68).
2454:WZKM. 4, 131 folgg. Bei Vullcrs fehlt das Verbum.— 55 —
3866:*) Bartholomae, Altiran. Verbum 105; zur Form vergl. Studien
5408:Verbum 194, BB. 17, 111 Anm., G;oldnor, KZ. 25,520 Note 61).— 135 —
8993:Kä§. V. hat sogar als Verbum [/^kos- *sehen' noch
9118:*) Eine aw. \/^paes- kommt als Verbum nicht vor; yt. 13, 126
9297:liche Verbum ist schon im PehlevT fast verschwunden.
9541:Verbum folgend.
10470:Verbum fraraftan lesen (WZKM. 5, 350); ich habe
10800:Dialektisch hat sich das Verbum erhalten in Kas.
11147:In den erwähnten Bedeutungen wird das Verbum
```


## [2026-09-05T06:03:04.880Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2430,2450p' HRN.txt; echo \"=== HUB no 59 bu ===\"; grep -n \"bûec\\|buec\\|'Eule'\" HUB.txt | head",
 "description": "Read Horn 238 and Hübschmann"
}
```


### [2026-09-05T06:03:04.934Z] TOOL RESULT

```
Dialekte), vergl. deutsch 'Schmatz.
236. bösäs, hüsäsp (Is. 29, 7, 8) *Traum, Schlaf ^) (jüsasb
(AM.).
aw. Biisyqsta' 'Dämon des Schlafes'-); phlv. büsäsp (in
Anlehnung an Gustäsp etc.), päz. btisyCLsp.
237. {\)büfn 'Erde, Land'.
ap. btimi' *Erde'; aw. büml-j phlv. büm C^LJjMmi^
238. {2)hum, baf'^) *Eule\ n^\
arm. btt, biiec 'Eule' (H. No. 59); lat. bübö; gr. ßvac^
ßvCa,
Onomatopoetisch, sonst würden die Lautverhältnisse
nicht stimmen.
239. bTimehen 'Erdbeben {^bümmehen).
ap. "^bumimadana- (Spiegel, Ar. Periode 68).
240. böi, bö 'Geruch*, böytden^ böyämden {Je^. X'är.)^),
böstän, biistän,
aw. baoiöi- *Wohlgeruch' ; phlv. böd, böi, böylnUan;
ai. [^biidkr merken, wahrnehmen'.
') Die Aussprache mit ö ist möglioher Weise falsch. Inzwischen
ist Nöldeke, Pers Stud. II, 1 Anm. 4 hinzugekommen.
^) Nach Barth oloraae, KZ. 29, 547 Anm. 2 bedeutet Büsyqsta-
=== HUB no 59 bu ===
```


## [2026-09-05T06:03:06.539Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON part1 head ===\"; head -c 600 MON_part1.txt; echo; echo \"=== grep پاکت ===\"; grep -n \"پاکت\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -10",
 "description": "Inspect Moin files"
}
```


### [2026-09-05T06:03:06.600Z] TOOL RESULT

```
=== MON part1 head ===
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
=== grep پاکت ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:2345:آن. عنوان و نام کسی بر پشت پاکت و مانند 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:28412:پاکت: ۳2۰ (.) محفظه کاغذ که نامه و 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:62000:تحویل آن نامه‌ها امضایی از گیرندة پاکت 
MON_part1.txt:2345:آن. عنوان و نام کسی بر پشت پاکت و مانند 
MON_part1.txt:28412:پاکت: ۳2۰ (.) محفظه کاغذ که نامه و 
MON_part1.txt:62000:تحویل آن نامه‌ها امضایی از گیرندة پاکت
```


## [2026-09-05T06:03:13.703Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28405,28420p' MON_part1.txt",
 "description": "Read Moin pakat entry"
}
```


### [2026-09-05T06:03:13.746Z] TOOL RESULT

```
عاشقی که عشق او آميخته با شهوت نباشد» 
عاشق باک‌نظر. زاهد» مجرد» تارکك دنیا. 
(تص.) کسی که بدون توقع و چشمداشت به 
خدا عشق می‌ورزد. 

پاکت: ۳2۰ (.) محفظه کاغذ که نامه و 
غبره را در آن گذارند و فرستند. بسته 
جعبه؛ ج. پا کات. 

پاک‌تن: ۲۰-۸ (ص‌مر.) با کیزه تن» با ک 
بدن. بارساء با کجامه» عفیف» مق. ناپا کك تن. 
نیک اندام» نیکو اندام» نیک‌چهر. 

پا کدامن: صحمصق-۲۰ [ < با کدامان] (مص‌مر.)
```


## [2026-09-05T06:03:14.618Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"بوم\" MON_part1.txt | head -20",
 "description": "Grep Moin for بوم"
}
```


### [2026-09-05T06:03:14.671Z] TOOL RESULT

```
1000:آبادبوم: 2-07 (امر.) ناحیت آبادان؛ زمین 
3142:ه روی در و دیوار و بوم مالند. 
4075:اکو: تتطة (- ۲ گو] (ا.) (جاد.) بوم» جغد. 
4309:آلبوم: سباحالة (ا.) سجموعه‌ای که عکس 
4316:آلبومین: حتصستداة (.) (گما. جاد.) ماده‌ای 
4615:مهیا؛ مستعد. (بناء) گچی روانتر از بوم. (ور.) 
6476:کاروانی گه در زاد و بوم خویش توانگر بوده 
16243:(.) زمین» بوم. ناحیه» قسمتی از ایالت. 
22832:بروبوم. 02۲-۵-۲ (امر.) زمین» سرزمین» 
22835:بوم و بر. 
26206:زمينة کتاب» درفش» کاغذ. مرز و بوم: 
26209:بوم: سنا (ع.] (1.) (جاد.) جغدء بوف. 
26213:بومادران: 0۳-802۲ [- بوی‌مادران < 
26214:بوماران] (امر.) (گیا.) گیاهی از تیر مرکبان 
26222:بومهن: «دطه-ستا [- بومهین - بوم + مهن 
31181:گیاهان به شکل نیام است. دانه‌ها فاقد آلبومن 
32455:پلاسما: 25 (.) (بز.) مادةٌ آلبومی 
35438:مسق. بوم. قماس؛ مسصور (ط.) هیأأت؛ 
35483:(نق.) زمینه؛ مق. بوم. زمینه» اساس» شالده. 
35999:بومی گر دانند. وجه تسمیه از این جهت است
```


## [2026-09-05T06:03:31.205Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26200,26230p' MON_part1.txt",
 "description": "Read Moin bum context"
}
```


### [2026-09-05T06:03:31.252Z] TOOL RESULT

```
بوع: ((.) سرزمین» ناحبه. زمین شبار 
نکرده و نا کاشته» مق. مرز. جاه مقام منزرل» 
ماواش فت)نطتهت (سف) رنه آماده 
شده؛ اعم از پارچه و غیره که بر روی آن 
نقاشی نك ز مه بارچهة زر دوزی شده. 
زمينة کتاب» درفش» کاغذ. مرز و بوم: 
سرزمین» ناحیه. 

بوم: سنا (ع.] (1.) (جاد.) جغدء بوف. 
بوع: 00۷-۱ (فع.) اول شخص مفرد از فعل 
مضارع از «بودن»؛ باشم. 

بومادران: 0۳-802۲ [- بوی‌مادران < 
بوماران] (امر.) (گیا.) گیاهی از تیر مرکبان 
دارای ساقه‌های بلند و برگ‌هایش سیار 
بریده و گل‌هایش خوشه‌یی مرکب است. 
ارتفاعش تا ۷۰ سانتیمتر می‌رسد. رنگ 
گل‌هایش سفید با صورتی و گلبرگ‌هایش 
ریز و خوشبو است؛ زهرة القندیل» علف 
هزار برگ. 

بومهن: «دطه-ستا [- بومهین - بوم + مهن 
- مثنه. حرکت] (ا.) زمین لرزه» زلز له. 
بون: 2 [ع.] (.) دوری» جدایی. 

بود: (.) بجه‌دان» زهدان» رحم. 

بول: ۳5۰ [- بن ] (.) نهایت و پایان هر چیزء 
بویا: 7 (ص.) دارای بو. خوشو» معطر. 
بوی‌افزار: 0۵۷-۰۴2۴ [- بوافزار - بوزار]
```


## [2026-09-05T06:03:33.271Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index bu ===\"; grep -n -i -E \"^BU|BUM|BUQ|POCKET\" incoming/ARY/ARY_latin_index_pages.txt | head -20; echo \"=== ARY pages بوم ===\"; grep -n \"بوم\\b\" incoming/ARY/ARY_pages.txt | head -10",
 "description": "Grep Aryanpur"
}
```


### [2026-09-05T06:03:33.365Z] TOOL RESULT

```
=== ARY latin index bu ===
406:BUGS te pS tas crc ered acl s 2llels elite! bik WS
722:BUS HS tle Db 19 (IK phates 4) alas} yea pb GeSlyagey ygelctleel OT
800:Bu lbs y(TOCHARIAN A) A os jib ol Janta cation pgs 05g 1 SUL 5 cx!
1033:BUN y DLAI Y alae Ay STS Blaby gb Foe chlo Same abt sal y oe
1362:BUCK: (WATER) 34-35 AMNIS LATIN) 3
1371:BUCK: n AIREM ARMENIAN) gs,\
1390:BUCK: n OGNT ,
1469:BUCKL: 237-283 ALBUE DANISH) Salo
1607:BUCK: 121 ANGUST, ENGI
1624:BUCK: 523-524 OST OLD ENGLISH) oS gS)
1664:BUCK: 32 GE DANISH) Sait
1694:BUCK: 394-396 VESTA (RUMANIAN) gly
1725:BUCK: : 52 HAMMER GERMAN) ST
1756:BUCK: ns HOLD ENGLISH) pS 5nd!
1785:BUCK: (EAT) 327-328 Jist (CZECH) Sey
1827:BUCK 388 GERT {MIDDLE IRISH) «ila 543 3)
1958:BUCK: 693-696 KOMMA SWEDISH) (shy
1987:BUCK: 338 MAYSOTAN
2031:BUCK: (VOICE) 1248 OLD SCANDINAVIAN) “Sissel ‘
2130:BUCK: 3s AMBRA (GAULISH) iS
=== ARY pages بوم ===
69:بخش‌های جهان که زبان بومی یا زبان رسمی آنها یکی از زبان‌های هند و اروپایی است.
88:کوج کردهاند. طی این کوج‌های متوالی؛ آریایی‌ه با بومیان هر محل درآمیختند و در نتیجه پاک و
169:زبان خود را در نواحی تسخیر شده رواج دادند. ولی در هر ناحیه» زبان مردم بومی (و ویژگی‌های
338:اصلاً از کجا میدانیم که هند و اروپائیان بومی محل‌های فعلی خود نبودند واز.
343:اروپائیان» بسیاری از بخش‌های اروپا و آسیا دارای بومیان اولیه بوده‌اند. در آبخست‌سانه‌ی (شبه
742:می‌دهد که یونانیان بومیان اصلی آن سرزمین نبوده و به آنجا کوج کرده‌اند.
3250:واژه بر "(8۸33) که جانور درنده‌ی بومی هند است نیز به احتمال زیاد از همین ریشه است و پهلری آن 8۸71
3939:۶ /_بوفه بوم (به چم ؛جفد")
3972:بوم (به چم "سرزمین"» *زمینه") / ۱۳۷
16189:و صوروی بوممه 0 کعکمرجوم احمکقم 02 ماه 0۳۵ ۳۳۵ دهم
```


## [2026-09-05T06:03:44.731Z] TOOL CALL #43: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T06:03:44.736Z] TOOL RESULT

```


```


## [2026-09-05T06:03:45.311Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3930,3980p' incoming/ARY/ARY_pages.txt",
 "description": "Read Aryanpur index context"
}
```


### [2026-09-05T06:03:45.354Z] TOOL RESULT

```
ویر ی آلمانی ۰:68 8088806 رققتاظ 3
انگلیسی (1327راق/89): 5 دنا 111115 له
سرئدی (8820(5(7): ۳ دنا 0 (8189) ره
لهستانی (ل20//3): 8112۸ 2 (81755) دوب ای ار
لیتوانی (2/7140/424): ب811613111077 برهان قاطع + ۳۱۷
بادداشت:
چم این واژه در زبان‌های رومانی و ولزی: لب» لب و لوچه.
۳
[pdf page 135]
۶ /_بوفه بوم (به چم ؛جفد")
پهلری (۲7ماتلم۳): ۰ 8170 ,81186 ,8118 هلندی (0076/7): ی الا
سانسکربت (54۸/557077): هغانآانا اسلاوی کهن (ع7ها5 070861 صا0): ۰
ارمنی (۸701521۸): 5 لا 816۰
یونانی (0880): ۸ ,8128 لهستاتی (اقلاهه: کهکل8۸
لانین (7100مل): 8 ,81180 بلغاری (4(ملگ ۸ اتاه): 811

۱ فرانسه (4ل۳82۸0). 11801 صربی (0لف/5578): :از
اسپانیایی (7ل52۸/13): داد لیتوانی (0۸/۸2 72+ بالقبانآنآل 13
ابتالپایی (0ممله۳): رددناد 25
ایسلند یکهن (74۸۷ 5001014 00): خ۸ر63 لرنی (لتی) (/۸0 ۰:47 8178887
نورس کهن (۸07۶8 012): 16۸
ساکسرنی کهن (54340(7 2ا0): ادا پسگشت‌ها هه ری ردنا
آلمانی کهن (0فال027 04 انز صت۵): 8 ۸0000

هالاً بش1۲ 3 (0۲) ایا

۱ آلمانی (027۵/۵۷): اد 8 زان ۱ 41 (81801) مق انم 02

1 انگلیسی کهن (2۸011870 صل0): 8 6 (0۲) :۸۸25
انگلیسی (ل٩لا69/0):‏ 0 8 (0۲۲۲) :005
دانکارکی (ل18هم0): 068 0 (0) برد
سرئدی] (#لواطط#اق: 16۸ )2 :لفط ۸ ام مها
نروژ ی (0/005014: 168 برهان قاطع + ۳۱۹

۹
1 پادباشت:
۱ ریشه‌ی این واژه در هیچکدام از مراجع فارسی در دسترس من پیگیری نشده است.
برخی از واجریشه شناسان اصل اين واژه راگو: نه‌ای "نام آوا" (08031۸7070814) می‌دانند؛ یعنی این واژه
به تقلید از آوای جغد به وجرد آمده است. در هر حال» برداشت زبان‌های هند و اروپایی از این آوا ویژه‌ی آنهاست
و با واژه‌های موجرد در زبان‌های غیرهند و اروپایی فرق دارد, ْ
[pdf page 136]
0 ا گگ ی
بوم (به چم "سرزمین"» *زمینه") / ۱۳۷
اوستایی (4787۸۷): 2/11 پسگشت‌ها آشگ بر را
پارسی باستان (/( 8888 صا): ۰ 8010۳ 1
پهلوی (۸]۸۲7): 21 1 (310شآ),20 راد ها
سانسکر بت (4(۹68/7): د[لا 811 یه 8 (۲۵۳۲۲۸) ۰
8117۸0 1517 ها
ارمثی (4۵/80140): 00 ,8015 برهان قاطع - ۳۳۰
یادداشت:
معثی این واژه در سانسکریت؛ زمین» جهان,
```


## [2026-09-05T06:03:59.470Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%88%D9%82",
 "prompt": "Give the full etymology sections for the Arabic بوق and the Persian بوق (horn/trumpet): what language it is borrowed from, intermediate forms (Aramaic/Syriac, Latin bucina, Greek), and glosses."
}
```


## [2026-09-05T06:04:00.883Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%88%D9%85",
 "prompt": "Give the full Persian and Arabic entries for بوم: all etymologies (owl; land/earth), Middle Persian forms cited, and whether the 'owl' sense is said to be onomatopoeic or an Arabic loan."
}
```


### [2026-09-05T06:04:06.570Z] TOOL RESULT

```
# Persian and Arabic Entries for بوم

## Arabic

**Etymology 1 (Owl):** "Likely of native onomatopoeic origin" with Semitic parallels including Classical Syriac and Akkadian terms for birds.

**Etymology 2 (Ship):** A sailing vessel type, with the note that "ships were frequently likened to birds."

## Persian

**Etymology 1 (Land/Earth):** Derives from Middle Persian **𐭡𐭥𐭬** (būm), tracing back through Old Persian, Proto-Iranian, and Proto-Indo-Iranian to Proto-Indo-European *bʰuH- ("to be"). Meanings include land, soil, earth, field, terrain, country, realm, region, environment, and habitat.

**Etymology 2 (Owl):** "Borrowed from Arabic" **بُوم** (būm), explicitly identified as a loanword rather than onomatopoeic in Persian.

**Etymology 3:** Colloquial spoken form of **بام** (bâm, "roof").
```


### [2026-09-05T06:04:06.711Z] TOOL RESULT

```
# Etymology of بوق (Trumpet/Horn)

## Arabic بوق

**Etymology:** The Arabic term's origins are uncertain but possibly connected to Classical languages. According to Wiktionary, it may relate to "Ancient Greek _βούκινο_ (boúkino) or Latin _būcina_, and Classical Syriac _ܒܘܩܝܢܐ_ (būqīnā)." The entry also notes comparison to English "bugle" (an ox or bovine horn instrument).

**Primary meanings:** trumpet, conch, or figuratively, one who spreads falsehoods or fails to keep secrets.

## Persian بوق

**Etymology:** This term is "borrowed from Arabic _بُوق_ (būq)," representing a direct loanword rather than independent development.

**Modern meaning:** Vehicle horn or klaxon, with the archaic sense preserving the original trumpet/conch reference from Classical Arabic usage around 1060 CE in Nāṣir-i Khusraw's travel writings.

The semantic shift reflects Persian's adoption of the Arabic musical instrument term, later specialized to describe mechanical horns in contemporary Persian.
```


## [2026-09-05T06:04:21.589Z] TOOL CALL #47: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py ARY:136 --image 2>&1 | tail -30",
 "description": "Render Aryanpur page 136"
}
```


## [2026-09-05T06:04:23.380Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%AA%DB%8C%D9%85%D8%A7%D8%B1",
 "prompt": "Give the Persian entry بوتیمار: etymology, meaning, any analysis as a compound, and cited sources."
}
```


### [2026-09-05T06:04:27.929Z] TOOL RESULT

```
۱ لاتین (/7[۸ا): 58 ,8180 بلغاری (4ل71.0۸۴ا8): 815

: فرانسه (۸/۲/7ظ۳): 1180 صربی (/ل5578/۸): 1(

: اسپانیایی (7ل5۸(]9): 1110( لیتوانی (7770۸/04): نابآ11

۱ ایتالیایی ((ل): ردان 5
ایسلند یکهن (010/۸7۸۸/لشع5 طا۵): 161۸ لثرنی (لتی) (71م): 817817667
ورس کهن (۸0788 0): 16۸

۱ ساکسونی کهن (542:0(7 012): 10۴ پسگشت‌ها ای راد درا

| آلمانی کهن (42/ل057 104 صزه): 8 ۶080500

۱ هاناً بشآ1۷1 3 (]0۷) 2
آلمانی (/(058۸/۵): ند 8 ند 41 (ن111801) هام02

: انگلیسی کهن (50لا80 صا0): 11 6 (0۷1) 2 ما۸
انگلیسی (5[4لءا8(/0): 07 8 (0۴) :0/05
دانمارکی (0/[5[7م0)+ 165 0 (0۷۲) +57
سرئدی] (8(/52018): 16۸ )8 :0 ۸ 03 للملا
نروژ ی (0/07/501401: 08 برهان قاطع : ۳۱۹
۱ : ۰

. : یاداشت.
1 ریشه‌ی این واژه در هیچگدام از مراجع فارسی در دسترس من پیگیری نشده است.
۲- برخی از واجریشه شناسان اصل این واژه را گونه‌ای "نام آوا" (031031۸70701۸) می‌دانند؛ یعنی این واژه
به تقلید از آوای جغد به وجرد آمده است. در هر حال» برداشت زبان‌های هند و اروپایی از ان آوا ویژه‌ی آنهاست
و با واژه‌های موجرد در زبان‌های غیرهند و اروپایی فرق دارد. ۱
```


### [2026-09-05T06:04:34.736Z] TOOL RESULT

```
# Persian Entry: بوتیمار (butimâr)

## Etymology
The term is a compound formed from two Persian elements:
- **بو** (bu): derived from Arabic أَبُو (ʔabū), "used to form nicknames, literally 'father of'"
- **تیمار** (timâr): meaning "worry; sorrow"

## Meaning
**بوتیمار** denotes a "bittern" (a wading bird).

## Compound Analysis
This is a **Persian compound term** combining a prefix derived from Arabic with a Persian noun. The construction follows the Arabic naming convention of using "abu" (father of) to create descriptive appellations.

## Cultural Context
According to usage notes in the entry: "In medieval sources, the bittern is believed to be sick with worry that the river is going to dry up, hence the name." This etymological metaphor reflects classical Persian literary tradition, where the bird symbolizes someone "prone to unnecessary worries."

## Source
This information derives from the Wiktionary entry dated October 31, 2025, which cross-references Persian Wikipedia for additional context on the term.
```


## [2026-09-05T06:04:44.781Z] TOOL CALL #49: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ARY/ 2>/dev/null | head -20",
 "description": "Find ARY OCR cache"
}
```


### [2026-09-05T06:04:44.823Z] TOOL RESULT

```
total 1056
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 02:04 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 328629 Sep  4 13:39 0051.png
-rw-rw-r-- 1 sfmqrb sfmqrb   1571 Sep  4 13:39 0051.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1003 Sep  4 14:18 0051.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 360766 Sep  5 02:04 0136.png
-rw-rw-r-- 1 sfmqrb sfmqrb   1990 Sep  5 02:04 0136.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 355916 Sep  4 14:43 0297.png
-rw-rw-r-- 1 sfmqrb sfmqrb   1663 Sep  4 14:43 0297.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1854 Sep  4 14:52 0297.vision.txt
```


## [2026-09-05T06:04:46.194Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/pocket",
 "prompt": "Give the full etymology of \"pocket\", including Anglo-French/Old North French forms, Old French poche, and the Frankish/Germanic origin. Also any note on the root."
}
```


### [2026-09-05T06:04:52.500Z] TOOL RESULT

```
# Etymology of "Pocket"

The word "pocket" originates from mid-14c. Anglo-French *pokete*, a diminutive form derived from Old North French *poque* (also Old French *pouche*). These Romance forms trace back to a Germanic source akin to Frankish *\*pokka* "bag," which connects to Proto-Germanic *\*puk-*.

**Key linguistic progression:**
- Anglo-French *pokete* (13c.) → diminutive of *poque*
- Old North French *poque* / Old French *pouche* → from Germanic
- Frankish *\*pokka* → from Proto-Germanic *\*puk-*

**Root origin:** The Proto-Germanic *\*puk-* derives from the Proto-Indo-European root *\*beu-*, described as "an imitative root associated with words for 'to swell.'" This connection appears shared with related terms like Old English *pohha* and Old Norse *poki*, all converging on the sense of a bag or pouch-like container.

The word's semantic development expanded from a simple "small bag" (early 15c.) to specialized uses in billiards (1754), mining (1850), military contexts (1918), and figuratively to represent money or finances (1717 onward).
```


## [2026-09-05T06:04:54.636Z] TOOL CALL #51: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ARY/0136.png"
}
```


### [2026-09-05T06:04:55.111Z] TOOL RESULT

```

```


## [2026-09-05T06:04:55.109Z] INPUT

[Image: original 1500x2400, displayed at 1250x2000. Multiply coordinates by 1.20 to map to original image.]


## [2026-09-05T06:05:29.858Z] TOOL CALL #52: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ARY/0136.vision.txt <<'EOF'\n[Aryanpur, Farhang-e Rishe-ha-ye Hend-o-Orupayi-ye Zaban-e Farsi, printed p. 136 (pdf p. 135)]\nRunning head: ۱۳۶ / بوف، بوم (به چَم \"جغد\")\n\nفارسی (PERSIAN): بوف، بوم (به چَم \"جغد\")            BŪF, BŪM\nچم انگلیسی سرواژه‌ی فارسی: OWL\nهند و اروپایی (INDO-EUROPEAN): *ULŪKOS, *BH(E)U-\n\nپهلوی (PAHLAVI): BUF, BUFG, BUG\nسانسکریت (SANSKRIT): ULŪKA\nارمنی (ARMENIAN): BU, BUÉCH\nیونانی (GREEK): BUĀS, BŪZA\nلاتین (LATIN): BŪBŌ, ULUCUS\nفرانسه (FRENCH): HIBOU\nاسپانیایی (SPANISH): BŪHO\nایتالیایی (ITALIAN): GUFO\nایسلندی کهن (OLD SCANDINAVIAN): UGLA\nنورس کهن (OLD NORSE): UGLA\nساکسونی کهن (OLD SAXON): HŪC\nآلمانی کهن (OLD HIGH GERMAN): ŪWILA, ŪLA\nآلمانی (GERMAN): EULE\nانگلیسی کهن (OLD ENGLISH): ŪLE\nانگلیسی (ENGLISH): OWL\nدانمارکی (DANISH): UGLE\nسوئدی (SWEDISH): UGLA\nنروژی (NORWEGIAN): UGLE\nهلندی (DUTCH): UIL\nاسلاوی کهن (OLD CHURCH SLAVIC): BUK-\nلهستانی (POLISH): BAKAC\nبلغاری (BULGARIAN): BUH\nصربی (SERBIAN): BÚHNUTI\nلیتوانی (LITHUANIAN): HULULER, BAUBLIS\nلتونی (لتی) (LATVIAN): BŪKSHKĒT\n\nREFERENCES / پسگشت‌ها:\nPOKORNY: 97-98\nBARNHART: (OWL) 793\nDELAMARRE: (HIBOU) 141\nMACKENZIE: (OWL) 126\nONIONS: (OWL) 638\nSKEAT: (OWL) 420\nMALLORY & ADAMS: B(E)U-\nبرهان قاطع: ۳۱۹\n\nیادداشت:\n۱- ریشه‌ی این واژه در هیچکدام از مراجع فارسی در دسترس من پیگیری نشده است.\n۲- برخی از واژه‌ریشه‌شناسان اصل این واژه را گونه‌ای \"نام آوا\" (ONOMATOPOEIA) می‌دانند، یعنی این واژه\nبه تقلید از آوای جغد به وجود آمده است. در هر حال، برداشت زبان‌های هند و اروپایی از این آوا ویژه‌ی آنهاست\nو با واژه‌های موجود در زبان‌های غیرهند و اروپایی فرق دارد.\nEOF\necho saved",
 "description": "Save Aryanpur vision transcription"
}
```


### [2026-09-05T06:05:29.918Z] TOOL RESULT

```
saved
```


## [2026-09-05T06:05:31.070Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/bucina",
 "prompt": "Give the Latin entry bucina/būcina: etymology (including any derivation from bos + cano, or from an onomatopoeic root), meaning, and descendants."
}
```


### [2026-09-05T06:05:38.979Z] TOOL RESULT

```
# Latin Entry: bucina/būcina

## Etymology
The Latin term derives from _bōs, bovi-_ ("cow") combined with the root of _canō_ ("sing"). This composition literally suggests "cow-song," reflecting the instrument's origins as a shepherd's horn.

## Meaning
**Būcina** (feminine, first declension) refers to:
1. A bugle
2. A curved war trumpet
3. In Late and Medieval Latin, any trumpet generally

The Vulgate Bible usage illustrates its broader application: "the sound of the **trumpet**" in Exodus 20:18.

## Descendants
The term spawned extensive Romance and Germanic descendants:

**Romance languages:** Spanish _bocina_, Portuguese _buzina_, Galician _bucina_, Italian _buccina_, Romanian _bucium_

**Germanic languages:** German _Posaune_ (via Middle High German _busūne_), Dutch _bazuin_, Swedish _basun_, Danish _basun_

**Other routes:** French _buisine_, Catalan _botzina_, Ancient Greek _βυκάνη_ (bukánē), and English borrowings including _buccina_ and _posaune_.

This wide dispersal reflects the instrument's cultural significance across medieval European societies.
```


## [2026-09-05T06:05:48.245Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT BITTERN/BUZZARD/BULLET/POCKET/BOSOM ===\"; grep -n -E \"^(BITTERN|BUZZARD|BULLET|POCKET|POUCH|BOSOM|BOIL|BULL|BUCKLE|BUD|BIG)\" SKT.txt | head -20",
 "description": "Grep Skeat headwords"
}
```


### [2026-09-05T06:05:48.296Z] TOOL RESULT

```
=== SKT BITTERN/BUZZARD/BULLET/POCKET/BOSOM ===
```


## [2026-09-05T06:05:50.610Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW bucina ===\"; grep -n -i \"bucina\\|bücina\" LEW_1910.txt | head -10; echo \"=== LKT bucina/buq ===\"; grep -n -i \"bucina\\|būq\\|buq \" LKT.txt | head -10; echo \"=== AFM buq ===\"; grep -n \"بوق\" AFM.txt AFM_pages.txt TAD.txt TAD_pages.txt 2>/dev/null | head -10",
 "description": "Grep Walde, Lokotsch, Addi Shir, Unaysi"
}
```


### [2026-09-05T06:05:50.699Z] TOOL RESULT

```
=== LEW bucina ===
=== LKT bucina/buq ===
=== AFM buq ===
TAD_pages.txt:1449:‫سنبوق وسّنبوك ‪ -‬وفي التركية سبك وفي اليونائية ©‪6‬از‪00‬ه‪ 5‬وفي‬
TAD_pages.txt:1544:                     ‫شور ‪ -‬عبراني « شلوفار ‪ 6‬معناه جيل وهو البوق‬
TAD_pages.txt:2400:‫كرنيتة ‪7‬س ايطالى هااءد‪.‬ده معناه قرن صغير وهو بوق تحيف ينفخ فيْه‬
TAD_pages.txt:2778:                   ‫ثفير ‏ فارمي < نبور » وهو البوق والناقور ينفخ فيه‬
TAD.txt:1484:سنبوق وسّنبوك - وفي التركية سبك وفي اليونائية ©6از00ه5 وفي 
TAD.txt:1595:شور - عبراني « شلوفار 6 معناه جيل وهو البوق 
TAD.txt:2526:كرنيتة 7س ايطالى هااءد.ده معناه قرن صغير وهو بوق تحيف ينفخ فيْه 
TAD.txt:2933:ثفير ‏ فارمي < نبور » وهو البوق والناقور ينفخ فيه 
AFM.txt:3897:وقال في التاج في ترجمة السنبوق وهي لغة في السلبوك :«زورق سفر يعمل في سواحل 
AFM.txt:6249:اليد ) ¬ فيه تعريب انيور ܙ ܕܐܐ الارامي” ܫܝܦܘܪܐ ܙ البوق
```


## [2026-09-05T06:05:55.713Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT bittern ===\"; grep -n -i \"bittern\\|buzzard\" SKT.txt | head -6; echo \"=== SKT pocket ===\"; grep -n -i \"^ *POCKET\\|Pocket,\" SKT.txt | head -6; echo \"=== SKT bullet ===\"; grep -n -i \"Bullet,\" SKT.txt | head -4",
 "description": "Grep Skeat entries"
}
```


### [2026-09-05T06:05:55.791Z] TOOL RESULT

```
=== SKT bittern ===
1851:Bittern,  a  bird.   (F.-I.ow  L.)    The U   added.      M.E.   bitoure.'^F.   bttt^r,  *i bittor;'   Cot.  — Low  L.  bHtontu,  a  bit cf.  L.  butio,  a  bittern.    Origin  uni, but  prob.  from   ihe  imitative  haiC make  a  booming  noise :  whence  L. bntirx,  lo  cry  like  a  bittern,  L.  /wAp,
2075:bump  (3),  to  boom  as  a  bittern.  (C) \V.  ini'snp^  a  hollow  sound ;  hence  adetyny Imffnp,  a  bittern.
2545:Bunard.  (F.-L.)  M.  E.^«raftf.teMi an  inferior  kind  of  falcon.  — F.  bmtard. F.  bttse,  a  buzzard ;  with  suflix  -anf.— L( L.  ^«w— L.  buttfif  a  sparrow-hawk.
12121:Myrrh.  ;!• .  -  L.  -  Gk  -  Aral mirre.  ••  O.  F.    mirre    (lllh myrrhe.^t,.  wyrrAa.  — Gk. mttrr.  (i)  bitter,  (j)  myrrh. its  bitterness.  4*  Heb.  wJr,  bltt
23473:French  from  Ijnu  Latin :  »ba<«.  ballet, barbican,  bargain,  baas  ( 1 ),  bittern,  boiagc, burden  (3'),  burl,  camlet,  canton,  cape  (O, cope  (I),  cygnet,  felon?,  ferret  (i),  festival. tlat;on,  frock,  gash,  gauge  ^age),  gouge^ hntch,  oleander,  palfrey.
=== SKT pocket ===
=== SKT bullet ===
```


## [2026-09-05T06:05:57.886Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW bulla/bucca ===\"; grep -n -i \"^bulla\\|^bucca\\|bücina\\|bucina\" LEW_1910.txt | head -10; echo \"=== WLD Bd2 b(e)u ===\"; grep -n -i \"dumpfe Schalleindr\\|aufblasen, schwellen\" incoming/WLD/WLD_Bd2_pages.txt | head -6",
 "description": "Grep Walde-Hofmann and Walde-Pokorny"
}
```


### [2026-09-05T06:05:57.951Z] TOOL RESULT

```
=== LEW bulla/bucca ===
=== WLD Bd2 b(e)u ===
370:    pa^mp, bu, pu usw. „aufblasen, schwellen‘‘.
5461:scheinlicher zu apo^ pu als „Hinterer“ oder zVipQi)u- „aufblasen, schwellen“,
7024:dumpfe Schalleindriicke)    mit hh (oder ph) gr. jtiju<pi^, 7yog „Hauch, Storin,
7109:zeigten dann dieselbe Anlautschwankung wie bii-, bhu- ^aufblasen, schwellen"
7313:wie anderer Sippen fiir „aufblasen, schwellen'* ist der Sprengungslaut der
7321:bu schallnachahmend fiir dumpfe Schalleindriicke, z. B. tJhuruf, dumpfer
```


## [2026-09-05T06:06:07.526Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7313,7360p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "Print Walde-Pokorny II bu- entry"
}
```


### [2026-09-05T06:06:07.569Z] TOOL RESULT

```
wie anderer Sippen fiir „aufblasen, schwellen'* ist der Sprengungslaut der
aufgeblasenen Backe.
   Buss, biddyrh „BGule“ stammt wohl aus boldyrh, b^ldyrh\ c. boide „Beole“
u. dgl. halt Berneker fiir entlehnt (100), ebenso r. btdka „rundes Brotchen,
SemmeP. Sie wurden iibrigens, wenn urverwandt, zu got. vfbaidjan zu
stellen sein, also zur Wz.    bliu „aufblasen'\ wo ich sie auch erwahnt habe.


bu schallnachahmend fiir dumpfe Schalleindriicke, z. B. tJhuruf, dumpfer
        Schlag u. a.
    Npers.      bum „Eule“, arm. bu, buec „Eule'' rHiibschmann Arm. St. I 23,
Gr. 1 430;    ohne Lautverschiebung im Schallwort), gr. ^vaq,           „Uhu”,
^vl^etv „wie ein Uhu schreien“, lat. bubo „Uhu'\ bubilare „bu bu schreien,
vom Uhu'^, bulg. bidi „Uhu“, bilham „schreien, vom Uhu'*, russ. biichaih
„dumpf und lang anhaltend schreien"; lit. baublySj biiblys „Rohrdommel",
baiibti^ bubauti „dumpf brullen", janczm haubis „der Gott des Yiehs" fist
nach Persson Beitr. 38 f. wegen dieser auch in aschw. bbla „brullen", aisL
batda „Kuh“ und in slav. byh^^ biicati^ s. u., belegbaren Anwendung auf
das Brullen der Binder auch lat. Bfibona „Bindergottin", bubidus „zum
Bind gehorig" anzureihen, wenigstens als Kreuzungen zwischen bov- „Bind"
und solchem bu-h-^. fiir bublle ist Umgestaltung ans bovlle nach cublle und
d. abl. bfibiis ausreichend, s. Yf. LEWb.^ 98; ^ov/^aXog „Gazellenart", wor«
aus lat. bubalus ^Gazelle, Biiffel" ebenfalls Kreuzungsergebnis? Die Ein-
biirgerung der osk. Form bos statt echt lat. *vds durch ein solches Schallwort
unterstiitzt?)   lit.;bubeuit „dr6hne dumpf, buhyjit „schiage dumpf", lett.
bubinat „wiehern"; lat. bubere „pupen" = ndd. piipen „pedere"; lat. biitio
„Bohrdommel", biitire vom Naturlaut der Bohrdommel", bfdeo ..eine Falken-
art";    gr.               „Ruf“, ^odco     „schreie"    (daraus     lat.   boare   „rufen“,       s.   Yf.
LEWb.^ 94 m. Lit.; Einmischung eines echt lat. Wortes gleichen Stammes
ist trotz Persson Beitr. 898 Anm. 2 nicht wahrscheinlich), ^(doxqbco ,,rufe an, um

Hilfe" (*^ofaarpcft>, s. Bechtel KZ. 46, 162), scheinen von solchem bu aus als
Reimworte zu yorj, yodco (s Wz. you) gebildet; ir. buracli „Get6se", biirethar
,clamat" (Strachan BB. 20, 24; Gdf. eher *bri-ro-^ nicht %rtk-ro- zum flgdn.).
5


   Mit ausl, Gutturalen: ai. biik-kara-h „Gebruil des Lowen", biiMati „bellt"
(av. btdahin-  „der das Geheule, Gefauche an sich hat", buxtl- „Heulen,
Fauchen"? s. Bthl. Wb. 967 f.), gr.          „heulend" (aber ^vxdvt] „Trom-
pete" ist entlehnt aus lat. bucina „Hirtenhorn", das entweder als *bri-Jcand
„bu tutend" zu unserem Schallwort bu, oder als *bou-C(ma zu bos gehort
als „Horn, womit man die Binder zusammenblast" oder als „zum Blasen
hergerichtetes Kuhhorn"; s. zuletzt Kiedermann IF. 37, 147 m. Lit.;
                                                     bu                                                 113

    Cyror. bugad (aus hochshifigem ^boulcaiu-) „boatiis, mugitus^*, bugunad
 „mugire“, vermutlich auch ir. boclina „(Meer, *toseiide Brandling'"; Gdf.
```


## [2026-09-05T06:06:24.782Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD bulla ===\"; grep -n \"bulla\" incoming/WLD/WLD_Bd2_pages.txt | head -10; echo; echo \"=== WLD puk/Tasche ===\"; grep -n -E \"\\bpuk-|poki|pohha|Tasche\" incoming/WLD/WLD_Bd2_pages.txt | sed -n '1,15p'",
 "description": "Grep Walde-Pokorny bulla and puk"
}
```


### [2026-09-05T06:06:24.849Z] TOOL RESULT

```
=== WLD bulla ===
4525:    Abg. pecJiyrh „bulla, Blase“, pachaii „ventilare, agitare^^ mss. pachnilth
7503:     Erweiterungen mit? sind vielleicht ai. buVidi^ lit. biiTis^ lat. bulla u. dgl.
11698:*(pdXXcov von einem St. *bulla-=^ (paXXo-g stammt; lit. balms „Stier“ aus
11940:(vomWind), bellen, brfillen”, isl.-norw. bulla „babbeln, schwatzen''; aisl.
14095:,.bulla‘‘. S. Persson Wzerw. 16, 173. Beitr. 879 (auch 54ff., 931 gegen

=== WLD puk/Tasche ===
1062:peciilium „Handgeld, Taschengeld“ (Yieh als Y^ertmesser), umbr. peqiio
3771:Diite,  Tasche“ (aber pata- „Tuch, Gewand'' s. u. peU „Kleid'‘), mir. alt
5471:puk- „zusammendrangen, eng umschlieBen".
7395:ags. pocca^ pohha „r*aufgeblasener) Sack", mnl. pocke „Blatter, Pocke^%
7566:    Mit germ, h-: ahd.          mhd.        „Beutel, Tasche“, ndl. buidel, buil
7619:eiigl. poke ds., nhd. pfoch „Beuter', mnd. pftkel ,.Beiitek^ ags. pohha, pocca
7668:und unten nd. pusc ,.Beutel, cunnus*;, anord. p~i^s „Tasche, Beutel“, isl.
14689:„Beutel,  Tasche“, mdkstis „Scheide'', lit. maksznd „Futterab‘, makszt\s
27790:schwed. dan. lomme,                  fries,    lomm „Tasche" (Falk-Torp s. v,; ??
39103:                           mndl. scharpe, scherpe „Tasche, die die Pilger
39104:an einem Bande um den Hals trugen“, spatahd. scherbe „Tasche'‘, nd.
39105:schrap „Tasche“, anord. skreppa „Tasche zum Tragen an einem Bande iiber
39111:Tasche^^ Nach E. Schroder Lw. aus lat. scirpea „Binsentasche*‘.
```


## [2026-09-05T06:06:25.624Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%A7%DA%A9%D8%AA",
 "prompt": "Give the Persian entry پاکت: etymology (which European language it is borrowed from and which word), and meaning."
}
```


### [2026-09-05T06:06:29.589Z] TOOL RESULT

```
# Persian Entry: پاکت

**Etymology:** The word پاکت is "borrowed from French _paquet_." It comes from the European language French.

**Meanings:** The entry lists three definitions:
1. packet
2. parcel
3. envelope
```


## [2026-09-05T06:06:40.872Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%BE%D8%A7%DA%A9%D8%AA/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for پاکت verbatim, including any bracketed origin tag such as [فر.] or [فرانسه]. Also quote the لغت‌نامه دهخدا etymology note if present."
}
```


## [2026-09-05T06:06:42.493Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D9%88%D9%85/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entries for بوم verbatim, including bracketed origin tags such as [ع.] or [په.], for both the 'owl/جغد' sense and the 'land/سرزمین' sense."
}
```


### [2026-09-05T06:06:49.658Z] TOOL RESULT

```
# پاکت - Dictionary Entries

## Dehkhoda Dictionary Etymology
"پاکت. [ ک َ ] ( از فرانسوی ، اِ ) ( از اصل فرانسوی پاکه ، بسته ) و در فارسی محفظه ای از کاغذ نامه را گویند"

## Mo'in Dictionary Entry
"(کَ ) [ فر. ] ( اِ. ) ورقة کاغذی تا شده که نامه و غیره را در آن گذارند و در آن را می چسبانند"

The Mo'in entry indicates the word derives from French, defining it as a folded paper sheet used to enclose and send letters and similar items.
```


### [2026-09-05T06:06:51.446Z] TOOL RESULT

```
# Farhangs Mo'in Entries for بوم

Based on the dictionary content provided, here are the two main senses from Farhang-e Mo'in:

**Owl sense:**
"[ ِ . ] جغد" — Listed as a separate entry indicating the bird meaning.

**Land/region sense:**
"[ ِ . ] ۱ - سرزمین ، ناحیه . ۲ - زمین شیار نکرده . ۳ - جا، مقام . ۴ - سرشت ،طبیعت . ۵ - پارچه قاب گرفته ای که روی آن نقاشی کنند. ۶ - زمینة پارچة زردوزی شده" — Six definitions covering territory, uncultivated land, place, nature, and textile-related meanings.

Both entries carry the origin tag [ِ.] (Persian) in the Mo'in dictionary format shown in the document.
```


## [2026-09-05T06:07:02.169Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"pocket, n\" \"pouch, n\" \"bosom, n\" \"bucket, n\" \"big, adj\" \"bud, n\" \"bullet, n\" \"buckle, n\" \"bullion, n\" \"boil, v\"; do echo \"--- $w ---\"; grep -n -m1 \"$w\" KLN_1966.txt | cut -c1-700; done",
 "description": "Grep Klein for English nodes"
}
```


### [2026-09-05T06:07:03.818Z] TOOL RESULT

```
--- pocket, n ---
--- pouch, n ---
--- bosom, n ---
--- bucket, n ---
--- big, adj ---
--- bud, n ---
--- bullet, n ---
--- buckle, n ---
--- bullion, n ---
--- boil, v ---
```


## [2026-09-05T06:07:06.954Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"pocket,\" \"bosom,\" \"bullet,\" \"buckle,\" \"bucket,\" \"^big,\" ; do echo \"--- $w ---\"; grep -n -m2 -E \"$w\" KLN_1966.txt | cut -c1-900; echo; done",
 "description": "Grep Klein again"
}
```


### [2026-09-05T06:07:08.772Z] TOOL RESULT

```
--- pocket, ---
5759:which  is  prob.  cogn.  with  OI.  gavint,  ‘groin’, bubonic,  adj.,  characterized  by  swelling  in  the groin.  —  See  prec.  word  and  -ic. bucca,  n.,  cheek.  —  L.  See  next  word, buccal,  adj.,  pertaining  to  the  cheek.  —  Formed with  adj.  suff.  -al,  fr.  L.  bucca,  ’cheek’,  from  the I.-E.  imitative  base  *bu-,  ‘to  blow ;  to  swell'.  Cp. Bubo,  buckle,  bull,  ‘edict’,  debouch,  disembogue, embouchure,  pocket,  poke,  ‘a  bag’,  pox,  puck.
9465:coutel,  n.,  a  kind  of  knife  (hist.)  —  OF.  coutel (whence  F.  couteau),  fr.  L.  cultellus,  dimin.  of culler,  ‘plowshare,  knife’.  See  colter, coutil,  coutille,  n.,  a  close-woven  canvas  fabric.  — F.  coutil,  ‘drill,  twill,  ticking’,  fr.  OF.  coute (now  couette,  coite),  ‘featherbed’,  fr.  L.  culcita, ‘sack  filled  with  feathers,  cushion’,  which  is cogn.  with  Ol.  kurcah,  ‘bundle,  bunch,  tuft’. Cp.  quilt  and  words  there  referred  to. couvade,  n.,  a  practice  among  some  primitive peoples  according  to  which,  when  a  child  is born,  the  father  also  takes  to  bed  and  takes  care of  the  child.  —  F.,  ‘a  brood’,  fr.  couver,  ‘to brood’,  fr.  L.  cubdre,  ‘to  lie  down’.  See  covey and  -ade  and  cp.  concubine, cove,  n.,  a  small  bay;  a  sheltered  nook.  —  ME., fr.  OE.  

--- bosom, ---
5394:bosket,  bosquet,  n.,  a  thicket.  —  F.  bosquet, ‘grove,  thicket’,  fr.  It.  boschetto,  dimin.  of  bosco, ‘wood’,  fr.  ML.  boscus,  of  s.m.  See  bush,  ‘shrub', and  cp.  boscage,  bouquet, bosom,  n.  — •  ME.,  fr.  OE.  bosm,  rel.  to  OFris. bosm,  OS.  bosom,  MDu.  boesem,  Du.  boezem, OHG.  buosarn,  MHG.  buosem,  buosen,  G.  Bu- sen;  of  uncertain  etymology.  For  the  suff.  -om cp.  besom.  Cp.  embosom.
9528:cram,  tr.  and  intr.  v.  —  ME.  crammen ,  fr.  OE. crammian ,  "to  cram,  stuff’,  fr.  crimman, ‘to  cram, insert’,  which  is  rel.  to  ON.  kremia,  ‘to  press, squeeze’,  fr.  I.-E.  base  *grem-,‘ to  press,  squeeze’, whence  also  OI.  gramah,  ‘heap,  troop,  village’, OSlav.  gramota,  ‘a  heap \gromada,  ‘a  large  heap’, L.  gremium,  ‘bosom,  lap’.  Base  *grem-  is  an  en¬ largement  of  base  *ger-,  ‘to  gather  together’. See  gregarious  and  cp.  gremial.

--- bullet, ---
4994:an  -/-enlargement  of  the  I.-E.  imitative  base *bu-,  ‘to  blow;  to  swell’.  See  buccal  and  cp. billet,  ‘note’,  boil,  v.,  bolas,  boule,  ‘a  game’, budge,  bulb,  bull,  ‘edict’,  bullet,  bulletin. Derivative:  bill,  tr.  v.,  to  make  out  a  bill;  to announce  by  bills.
5832:Derivative:  bull,  intr.  and  tr.  v.,  bull-ish,  adj. bull,n.,  an  edict  of  the  pope.  —  ME.  bulle,  fr.  OF. bulle,  fr.  It.  bulla,  fr.  ML.  bulla,  ‘seal  affixed  to  a document,  document’,  fr.  L.  bulla,  ‘bubble,  boss, knob’,  fr.  I.-E.  *bu-l-,  whence  also  Lith.  bule, bulls,  ‘buttock’,  MDu.  puyl,  ‘bag’,  MLG.  pull, poll,  "pod,  husk’  (with  p  for  b).  I.-E.  *bu-l-  is an  -/-enlargement  of  base  *bu-,  ‘to  blow;  to swell’,  whence  L.  bucca,  “cheek".  Sec  buccal  and cp.  bill,  ‘document",  bullet,  bulletin.  Cp.  also poll,  "head".

--- buckle, ---
5423:bouche,  n.,  mouth  ( obsol .)  —  F.,  ‘mouth’,  fr.  L. bucca,  ‘cheek’.  See  buccal  and  cp.  bonne  bouche. boucle,  n.,  a  kind  of  yam  having  small  curly loops.  —  F.,  lit.  ‘buckled,  curled’,  pp.  of  bon¬ der,  ‘to  buckle,  curl’,  fr.  boucle,  ‘buckle,  curl’. See  buckle.
5759:which  is  prob.  cogn.  with  OI.  gavint,  ‘groin’, bubonic,  adj.,  characterized  by  swelling  in  the groin.  —  See  prec.  word  and  -ic. bucca,  n.,  cheek.  —  L.  See  next  word, buccal,  adj.,  pertaining  to  the  cheek.  —  Formed with  adj.  suff.  -al,  fr.  L.  bucca,  ’cheek’,  from  the I.-E.  imitative  base  *bu-,  ‘to  blow ;  to  swell'.  Cp. Bubo,  buckle,  bull,  ‘edict’,  debouch,  disembogue, embouchure,  pocket,  poke,  ‘a  bag’,  pox,  puck.

--- bucket, ---
4318:bale,  n.,  bucket,  v.,  to  dip  water.  —  See  bail, ‘bucket’.
5781:bucket,  n.  —  ME.,  fr.  AF.  buket,  dimin.  formed fr.  OE.  buc,  ‘body,  belly,  pitcher’.  See  buck, ‘body  of  a  wagon’,  and  -et.

--- ^big, ---
```


## [2026-09-05T06:07:19.226Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -m1 \"big,  adj\\|big, adj\" KLN_1966.txt | cut -c1-600; echo; grep -n -m1 \"bud,  n\\|bud, n\" KLN_1966.txt | cut -c1-600; echo; grep -n -m1 \"puff,  intr\\|puff, \" KLN_1966.txt | cut -c1-500; echo; grep -n -m1 \"boast,  n\\|boast, \" KLN_1966.txt | cut -c1-500",
 "description": "Grep Klein for big, bud, puff, boast"
}
```


### [2026-09-05T06:07:19.313Z] TOOL RESULT

```
4961:Derivatives:  bifurcat-ed,  adj.,  bifurcat-ion,  n. big,  adj.  —  ME.  bigge,  big,  of  uncertain  origin, big,  bigg,  tr.  v.,  to  build.  —  ME.  biggen,  fr.  ON. byggja,  ‘to  build;  to  dwell  in’,  which  is  rel. to  bua,  ‘to  dwell’.  See  be  and  cp.  boor,  booth. biga,n.,atwo-horsed  chariot  (Roman  antiquities). —  L.  bigae  (pi.),  contraction  of  *bi-jugae,  lit. ‘two  (horses)  yoked  together",  compounded  of bi-,  ‘twice’  and  jugum,  ‘yoke’.  See  bi-  and  yoke and  cp.  join.

5794:bud,  n.  —  ME.  budde,  rel.  to  Du.  bot,  ‘bud’,  OS. budil,  ‘bag,  purse’,  MDu.  budel,  Du.  buidel, OHG.  biitil,  MHG.  biutel,  G.  Beutel,  of  s.m., fr.  I.-E.  base  *b(h)u-,  ‘to  swell’.  See  buccal  and cp.  buddy.  Cp.  also  bolt,  ‘to  sift’.  Cp.  also boil,  ‘inflammation’.

5804:buff,  n.,  a  blow;  tr.  and  intr.  v.,  to  strike.  — ME.  buffe,  fr.  OF.  buffe,  ‘blow’,  which  is  of imitative  origin.  Cp.  buffet,  puff, buff,  n.,  skin  of  the  buffalo.  —  From  earlier  buffe, ‘buffalo,  buff’,  fr.  F.  buff le,  ‘buffalo’.  To  account for  the  loss  of  the  ending  -le,  I  would  suggest that  it  was  mistaken  for  the  diminutive  suffix and  accordingly  dropped.

5252:boast,  n.  —  ME.  boost,  best.  See  next  word, boast,  tr.  v.  —  ME.  boosten,  bosten,  fr.  boost,  bost, n.,  rel.  to  OS.  bosi,  MLG.,  MDu.  bose,  Du.  boos, ‘evil,  wicked,  angry’.  OHG.  bosi,  ‘worthless, slanderous’,  MHG.  boese,  G.  bose,  ‘evil,  bad, angry’,  Norw.  baus,  ‘proud,  bold,  daring’,  fr. Teut.  base  *baus-,  which  lit.  means  ‘to  blow  up, puff  up,  swell’.  This  base  is  an  enlarged  form of  I.-E.  *bhdu-,  *bhu-,  �
```


## [2026-09-05T06:07:31.683Z] TOOL CALL #66: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D9%88%D9%82' --note 'page 78, root Beu 2, Arabic/Persian buq <- Syriac buqina <- Latin bucina' 2>&1 | tail -2 && python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D9%88%D9%85' --note 'page 78, root Beu 1, Persian bum owl (said to be Arabic loan) vs bum land' 2>&1 | tail -2 && python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%AA%DB%8C%D9%85%D8%A7%D8%B1' --note 'page 78, root Beu 1, Persian butimar bittern = abu + timar' 2>&1 | tail -2 && python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/bucina' --note 'page 78, root Beu 2, Latin bucina < bos + cano' 2>&1 | tail -2",
 "description": "Archive Wiktionary sources"
}
```


### [2026-09-05T06:07:34.660Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2fbc9babd50fbffc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/18175ceb85ad6f57.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/511d22ca0e6ce14c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dfff9aa29c9e01d3.txt
```


## [2026-09-05T06:07:41.645Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://www.etymonline.com/word/pocket' --note 'page 78, root Beu 2, English pocket < AF pokete < ONF poque, Frankish *pokka, PGmc *puk-' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%BE%D8%A7%DA%A9%D8%AA' --note 'page 78, root Beu 2, Persian pakat < French paquet' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D9%BE%D8%A7%DA%A9%D8%AA/' --note 'page 78, MON:668 check, Moin tags pakat [fr.]' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%A8%D9%88%D9%85/' --note 'page 78, MON:606 check, Moin bum owl / bum land' 2>&1 | tail -2",
 "description": "Archive remaining web sources"
}
```


## [2026-09-05T06:07:44.073Z] TOOL CALL #68: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg78.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/78.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5",
 "description": "Copy page 78 image for audit"
}
```


### [2026-09-05T06:07:46.793Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7243cda9c113fe22.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/13170448b6bf29d8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1eb66da4fed5e0d5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4c54ec62fc3e3829.txt
```


### [2026-09-05T06:07:46.858Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  20612 Sep  5 02:01 75_greek_latin_arrow.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75134 Sep  5 02:01 75.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66505 Sep  5 01:56 76.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65211 Sep  5 02:03 77.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63822 Sep  5 02:07 78.png
```


## [2026-09-05T06:07:50.901Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-74.json'))\nprint({k:v for k,v in d.items() if k!='entries'})\ne=d['entries'][0]\nprint(json.dumps({k:(v if k!='nodes' else [v[0]]) for k,v in e.items()},ensure_ascii=False,indent=1)[:3000])\n\"",
 "description": "Inspect an existing verification file"
}
```


## [2026-09-05T06:07:51.655Z] TOOL CALL #70: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T06:07:52.413Z] TOOL RESULT

```
{'pdf_page': 74, 'book_page': 44, 'verified_by': 'claude-opus-5', 'verified_on': '2026-09-05'}
{
 "entry": 2,
 "root": "Ayer, Aier, Aien",
 "verdict": "confirmed",
 "modern_form": "PIE *h₂ey- (3) 'day, morning', heteroclitic noun *h₂óy-r̥ ~ *h₂éy-n-s 'day' (= Pokorny ā̆ier-, ā̆ien-, IEW 12; Watkins ayer-)",
 "note": "Pokorny IEW p. 12 has the entry verbatim: \"ā̆ier-, ā̆ien- n. 'Tag, Morgen'. Av. ayarə, Gen. ayąn n. 'Tag'\", and Watkins in the AHD appendix has \"ayer-. Day, morning. ... [Pok. ajer- 12.]\". Nourai's three headword variants are simply the AHD spelling (ayer-) plus Pokorny's two stem forms (aier-/aien-); the r/n heteroclisis of the Avestan paradigm (nom. ayarə : gen. ayąn) is exactly what produces the -r and -n variants. Language label 'Indo-European' and the gloss 'day, morning, early in the day' are both correct (the third part of the gloss reflects the locative *h₂éy-eri 'in the morning' behind Gk. ἦρι and Goth. air). Modern laryngealist notation is *h₂ey-/*h₂eyer-; Nourai's pre-laryngeal shape is the 1959 Pokorny shape and is not an error. The Naser-Khosrow couplet printed in the Persian box (پریر قبلهٔ احرار زابلستان بود...) uses پریر in its ordinary adverbial sense and is faithfully extracted. One substantive problem lies inside the chart, not at the root: see node #3 (پیرار).",
 "note_fa": "ریشهٔ هندواروپایی آغازینی که نورایی آن را Ayer, Aier, Aien آورده، همان ā̆ier-/ā̆ien- پوکورنی (ص ۱۲) به معنای «روز، بامداد» است؛ در ریشه‌شناسی امروزی آن را *h₂ey- و نامی دوگانه‌ستاک (heteroclitic) *h₂óy-r̥ ~ *h₂éy-n̥s بازسازی می‌کنند؛ همین گردش r/n در صرف اوستایی (فاعلی ayarə، اضافی ayąn) دو صورت Aier و Aien را توضیح می‌دهد. برچسب زبانی «هندواروپایی» و معنای جعبهٔ ریشه درست است و هر دو مأخذی که خود نورایی آورده (پوکورنی ۱۲؛ واتکینز در پیوست فرهنگ میراث آمریکایی، ص ۱۵۰۷) دقیقاً همین را می‌گویند. ادعای نورایی دربارهٔ خود ریشه درست است؛ اشکال در یکی از شاخه‌هاست (نگاه کنید به گرهٔ ۳، «پیرار»).",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ey-",
  "https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C",
  "https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C%D8%B1%D9%88%D8%B2"
 ],
 "ref_check": [
  {
   "ref": "POK:12",
   "status": "supports",
   "note": "Pokorny IEW p. 12 (POK_01.txt leaf 20, page marker '12' visible on the leaf): \"ā̆ier-, ā̆ien- n. ,Tag, Morgen'. Av. ayarə, Gen. ayąn n. ,Tag'.\" and on p. 13 \"Got. air, aisl. ár, Adv. ,frühe' ... Kompar. got. airiza ,früher' ... Superl. ags. ǣrest ... nhd. erst. WP. I 3\". Exactly the chart's root, gloss and both branches."
  },
  {
   "ref": "AHD:1507",
   "status": "supports",
   "note": "Watkins, AHD IE-roots appendix (local AHD_watkins1985.txt line 317): \"ayer-. Day, morning. 1. Germanic *airiz in: a. Old English ǣr, before: EARLY, ERE; b. Old Norse ár, before: OR2. 2. Germanic (superlative) *airistaz in Old English ǣrest, earliest: ERST. [Pok. ajer- 12.]\" — the whole Germanic/English branch of the chart, verbatim; p. 1507 is the right page of the 1975 New College appendix (a-roots, pp. 1505-1508)."
  },
  {
   "ref": "OEW:3",
   "statu
```


### [2026-09-05T06:07:52.443Z] TOOL RESULT

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


## [2026-09-05T06:09:41.582Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in (5085,5958,5781,5794,5252,4994,5759):\n    off=sum(len(l)+1 for l in lines[:target-1])\n    leaf=t[:off].count('\\f')\n    print(target,'leaf',leaf,'-> printed approx',2*(leaf-12),2*(leaf-12)+1)\n\"",
 "description": "Map Klein line numbers to printed pages"
}
```


### [2026-09-05T06:09:43.433Z] TOOL RESULT

```
5085 leaf 104 -> printed approx 184 185
5958 leaf 124 -> printed approx 224 225
5781 leaf 120 -> printed approx 216 217
5794 leaf 120 -> printed approx 216 217
5252 leaf 107 -> printed approx 190 191
4994 leaf 102 -> printed approx 180 181
5759 leaf 120 -> printed approx 216 217
```


## [2026-09-05T06:09:43.603Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON butimar ===\"; grep -n \"بوتیمار\" MON_part1.txt MON_part2.txt | head -5; echo \"=== BQT v1 timar-bird ===\"; grep -n \"تیمار\" BQT_v1_pages.txt | head -10",
 "description": "Grep Moin and Borhan for butimar"
}
```


### [2026-09-05T06:09:43.685Z] TOOL RESULT

```
=== MON butimar ===
MON_part2.txt:2727:بوتیمار. 
=== BQT v1 timar-bird ===
1002:میگریانید . یس‌از آستین طنبوری‌بر آورد وچنم‌میغواند : ابااین‌تیمار باید
21348:بو تیمار. بامیم پروزن حوسیقار . نلم
24162:بتیمار جهان دلرا چرا باید که پضانی .
32419:تیمار س بر وزن‌بیمار» خدهت وغه‌خواری
32423:کردن همآمده است - وآنرا تیماره بازباوتی‌ها
32454:من ز نیم تو بتیمار گرفتار شدم
```


## [2026-09-05T06:09:51.683Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nimport re\npages=t.split('\\f')\nfor i in (104,124):\n    p=pages[i]\n    nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$',p)\n    print('leaf',i,'page-like numbers:',nums[:8])\n    print(repr(p[:200]))\n    print('---')\n\"",
 "description": "Find Klein printed page numbers on leaves"
}
```


### [2026-09-05T06:09:53.447Z] TOOL RESULT

```
leaf 104 page-like numbers: ['176']
'is  and torque).  The  plant  was  so  called  from  its  twisted root.\nbistoury,  n.,  a  small  surgical  knife.  —  F.  bistouri. of  unknown  origin.\nbistro,  n.,  1)  a  wine  seller;  2)  a  win'
---
leaf 124 page-like numbers: ['214', '217']
' Derivatives:  bustle,  n.,  hurry,  bustl-ing,  adj., bustl-ing-ly,  adv.\nbustle,  n.,  framework  worn  by  women  to  support the  skirt.  —  Of  uncertain  origin, busy,  adj.  —  ME.  busy,  bisy'
---
```


## [2026-09-05T06:09:53.571Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:21347])\nleaf=t[:off].count('\\f')\nprint('leaf',leaf,'printed approx',leaf-220)\n\" && sed -n '21344,21360p' BQT_v1_pages.txt",
 "description": "Locate Borhan butimar entry"
}
```


### [2026-09-05T06:09:55.623Z] TOOL RESULT

```
leaf 533 printed approx 313
و نقره و امثال آن در آن بگذارند. ومعرب‌آن
بوشه , و بعربی خلاص گویند 1
بق قة خاك - کنابه از بدن و قاب
اسان باشد.
بو تیمار. بامیم پروزن حوسیقار . نلم
مرغی است که اورا عم خورك نیز گوند . و ا
پیوسته درکنار آب نشیند وازغم آنکه مباداآب
کم شود باوجود تتنگی آب نخورد واور! بمربی
یمام و یبونانی شفنین خوانند . خوردن گوشتش
بیخوایی آورد, رمقوی فوت حافظه باشد وذهن‌را
(۱) چك
۱ ر(ه: ح*۱ صفحه قبل. ۴ 9618
«اسفا ۲:۱ ص ۸۰*. ۳ رتفا دز
پهلوی بمعنی بز ( بضم اول ) است ۶ موستی .
بندهش ۱۰ . ۴ حز, 3۵۵ .
8 , پهلوی ۷2۲ , خار « بونکر
۲ ». بوچیناك (0۷1[۷12), خبار « بوستی.
```


## [2026-09-05T06:10:08.573Z] AGENT

Now I'll write the verification file.


## [2026-09-05T06:19:10.901Z] TOOL CALL #75: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk78.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 78,\n \"book_page\": 48,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Beu 1, Bheu 1, Bhu\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *b(e)u-, *bh(e)u- — an onomatopoeic (imitative) base for dull, muffled sounds (hooting, booming, thudding); Pokorny IEW 97, Walde-Pokorny II 112-113, Watkins/AHD 'beu-2'\",\n   \"note\": \"Pokorny IEW p. 97 has the entry verbatim: \\\"b(e)u-, bh(e)u- schallnachahmend fuer dumpfe Schalleindruecke, z. B. Uhuruf, dumpfer Schlag u. a.\\\", and Watkins in the AHD appendix has \\\"beu-2. Root imitative of muffled sounds. 1. Latin butio ... bittern. 2. Latin buteo, a kind of hawk: BUZZARD. [Pok. 1. b(e)u- 97.]\\\". Nourai's three headword shapes are simply Pokorny's own alternants b(e)u- / bh(e)u- plus the zero grade bhu-; the language label 'Indo-European' and the gloss 'root of muffled sounds' are both correct. Pokorny explicitly keeps this base apart from two homophonous ones: bu- 'lip, kiss' and b(e)u-/bh(e)u- 'to blow up, swell' (p. 98) — the latter is Nourai's 'Beu 2' on the same printed page, so his numbering is his own but the split is Pokorny's. Because the base is expressive, Pokorny warns that ongoing re-creation crosses the regular sound laws (Germanic p- beside b-), which is why the Latin, Iranian and Armenian members can look phonetically 'too similar'. Two of the four branches drawn from this root are sound (the Avestan words and the Latin bird names); the Pahlavi box and the Persian bird-name box are not (see nodes #2 and #3).\",\n   \"note_fa\": \"ریشه‌ای که نورایی با صورت‌های Beu 1 / Bheu 1 / Bhu آورده همان *b(e)u- / *bh(e)u- پوکورنی (فرهنگ ریشه‌شناختی هندواروپایی، ص ۹۷) است: ریشه‌ای «نام‌آوا» (onomatopoeia) برای آواهای گنگ و پژواک‌دار مانند بانگ جغد، غرّش و تُپش. واتکینز نیز در پیوست فرهنگ میراث آمریکایی همین را با نشانِ beu-2 «ریشهٔ تقلیدی آواهای خفه» آورده و به پوکورنی ۹۷ ارجاع داده است. پوکورنی این ریشه را از دو ریشهٔ هم‌آوای دیگر — bu- «لب، بوسه» و b(e)u- «باد کردن، آماسیدن» (ص ۹۸، همان که نورایی Beu 2 می‌نامد) — جدا می‌کند، پس شمارهٔ نورایی از خودِ اوست ولی این جداسازی از پوکورنی است. برچسب زبانی «هندواروپایی» و معنای جعبهٔ ریشه درست است؛ ادعای نورایی دربارهٔ خودِ ریشه پذیرفتنی است. تنها باید توجه داشت که چون ریشه نام‌آواست، پوکورنی هشدار می‌دهد که بازآفرینی پیوستهٔ آن قانون‌های آوایی را می‌شکند و ازاین‌رو شباهت صورت‌های لاتینی، ایرانی و ارمنی لزوماً نشانهٔ خویشاوندی مستقیم نیست. دو شاخه از چهار شاخهٔ این نمودار درست است (واژه‌های اوستایی و نام‌های پرندگان لاتینی) و دو شاخهٔ دیگر نه (گره‌های ۲ و ۳).\",\n   \"sources\": [W + \"%D8%A8%D9%88%D9%85\"],\n   \"ref_check\": [\n    {\"ref\": \"POK:97\", \"status\": \"supports\",\n     \"note\": \"Pokorny IEW p. 97 (POK_01.txt leaf 106, page marker '97' on the leaf): \\\"2. b(e)u-, bh(e)u- schallnachahmend fuer dumpfe Schalleindruecke, z. B. Uhuruf, dumpfer Schlag u. a. Npers. bum ,Eule'; arm. bu, buec ,Eule' ... gr. byas ... lat. bubo ,Uhu'...\\\" — exactly the root box, and it already carries the Persian and Latin members Nourai draws from it.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II pp. 112-113 (WLD_Bd2_pages.txt line 7321)\", \"stance\": \"supports\",\n     \"note\": \"\\\"bu schallnachahmend fuer dumpfe Schalleindruecke, z. B. Uhuruf, dumpfer Schlag u. a. Npers. bum ,Eule', arm. bu, buec ,Eule' (Huebschmann Arm. St. I 23 ...) ... lat. butio ,Rohrdommel', butire ,vom Naturlaut der Rohrdommel', buteo ,eine Falkenart'\\\" — Walde-Pokorny is Pokorny's own source for this entry and states it more fully.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. beu-2 (AHD_watkins1985.txt line 321)\", \"stance\": \"supports\",\n     \"note\": \"\\\"beu-2. Root imitative of muffled sounds. 1. Latin butio (perhaps > Old French butor), bittern: BITTERN1. 2. Latin buteo, a kind of hawk: BUZZARD. [Pok. 1. b(e)u- 97.]\\\"\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, p. 116 (IEC.txt leaf 78)\", \"stance\": \"partial\",\n     \"note\": \"Mann sets up the base as \\\"bhu- (2) 'howl, gale, blast. Cf. bhubh-' Arm. bu (o-st. 'owl') beside buk ... Per. cf. bu timar 'heron'; Phryg. or Mac. buza 'owl'; Du. bui 'squall'; cf. Lat. butio and MIr. bufa\\\" — same base, but Mann's membership list differs from Pokorny's (he adds the Persian bird name Nourai uses in node #2).\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"bučahin, buxti\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Both words are genuine Younger Avestan and both are attached to this root by Pokorny himself. Bartholomae, Altiranisches Woerterbuch cols. 967-968, has \\\"j. bucahin- Adj. 'der das Geheule, Gefauche an sich hat'\\\" and buxti-, the latter attested in the self-naming formula buxtiš nąma ahmi 'Buxti is my name' (Yt. 14.47, where Vərəθraγna recites his ten names). Formally bucahin- is an -in- possessive adjective built on a neuter s-stem *buč-ah- (Av. -ah-/-aŋh-) from an imitative root *buk-, with the regular Old Iranian palatalisation k > č before the front vowel of the suffix; buxti- is a ti-abstract from the same root, where k + t gives the cluster -xt- by the ordinary Iranian rule (cf. Av. vaxti- : vak-). Pokorny p. 97 places them under the guttural extension of the base, beside Skt. bukkati 'barks' and bukkāra- 'roaring of a lion', but flags the Avestan pair with a question mark because the Indo-Aryan and Iranian forms may be independent re-creations of the same noise. Nourai's single gloss 'howl, yell' is a fair rendering of Bartholomae's 'Geheule, Fauchen', though bucahin- is strictly an adjective 'having howling about it', not a noun.\",\n     \"derivation_fa\": \"هر دو واژه اوستایی نو (متأخر) و اصیل‌اند و خودِ پوکورنی آنها را زیر همین ریشه آورده است. بارتولومه در فرهنگ ایرانی باستان (ستون‌های ۹۶۷–۹۶۸) صورت j. bucahin- را صفت به معنای «دارندهٔ زوزه و فش‌فش» و buxti- را در عبارت buxtiš nąma ahmi «نام من بوخْتی است» (یشت ۱۴، بند ۴۷، در برشمردن ده نام بهرام) ثبت کرده است. از نظر ساخت، bucahin- صفتی با پسوند -in- بر پایهٔ ستاک -ah- خنثی (*buč-ah-) از ریشهٔ نام‌آوای *buk- است و دگرگونی k > č در ایرانی باستان پیش از واکهٔ پیشین قاعده‌مند است؛ buxti- نیز نامِ مصدری با پسوند -ti- از همان ریشه است که در آن k + t به خوشهٔ -xt- بدل شده (همانند vaxti- در برابر vak-). پوکورنی این جفت را در کنار سنسکریت bukkati «پارس می‌کند» و bukkāra- «غرّش شیر» می‌نشاند اما نشان پرسش می‌گذارد، چون ممکن است صورت‌های هندی و ایرانی جداگانه از همان آوا ساخته شده باشند. ادعای نورایی درست است؛ تنها معنای «زوزه، فریاد» برای هر دو واژه کمی کلی است، زیرا bucahin- صفت است نه نام.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"POK:97\", \"status\": \"supports\",\n       \"note\": \"POK_01.txt leaf 106: \\\"Mit auslautenden Gutturalen: ai. buk-kara-h ,Gebruell des Loewen', bukkati ,bellt' (av. bucahin- ,der das Geheule, Gefauche an sich hat', buxti- ,Heulen, Fauchen'?), gr. byktes ,heulend'\\\" — Nourai's box is a straight copy of this parenthesis, question mark and all.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Woerterbuch cols. 967-968 (BRT.txt line 17319)\", \"stance\": \"supports\",\n       \"note\": \"\\\"j. bucah'in- Adj. 'der das Geheule, Gefauche an sich hat' ... buxtiš nąma ahmi Yt. 14.47\\\" — both forms attested, with the exact glosses Pokorny repeats.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p. 113 (WLD_Bd2_pages.txt, 'Mit ausl. Gutturalen')\", \"stance\": \"supports\",\n       \"note\": \"\\\"(av. bucahin- ,der das Geheule, Gefauche an sich hat', buxti- ,Heulen, Fauchen'? s. Bthl. Wb. 967 f.)\\\" — Walde-Pokorny gives the Bartholomae column reference explicitly.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. beu-2\", \"stance\": \"silent\",\n       \"note\": \"Watkins lists only the two Latin bird names under beu-2; no Iranian material at all.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"bŭ-tîmâr «بوتیمار»\", \"verdict\": \"disputed\",\n     \"derivation\": \"Nourai's own reference does support him: Mann, Indo-European Comparative Dictionary p. 116, lists \\\"Per. cf. bu timar 'heron'\\\" among the members of his base bhu- (2) 'howl, gale, blast'. But that is an isolated etymology and no Iranist follows it. The standard analysis, which the Persian lexical tradition itself implies, is بوتیمار = بو (bū) + تیمار (tīmār 'care, grief, sorrow'), where the first element is the Arabic kunya-prefix أبو abū 'father of', reduced in Persian to bū- as in بوعلی Bū-ʿAlī, بوالهوس bū-l-hawas: 'father of grief', the bird of sorrows. Borhan-e Qate' (vol. 1, printed p. 313) explains the name exactly this way: the bittern is 'also called ghamḵᵛorak (little grief-eater); it sits forever at the water's edge and from grief that the water might run short it will not drink although it is thirsty'. There is besides no phonetic route from Av. bučahin-/buxti- to bū-tīmār: the second element تیمار is the well-known Middle Persian tīmār 'care, affliction' (Parthian tymʾr), and the first is a syllable that never had a -č- or -xt-. Modern scholarship therefore rejects the arrow: the word is a Persian compound with an Arabic prefix, not an inherited descendant of the Avestan noise-words.\",\n     \"derivation_fa\": \"مأخذی که خود نورایی آورده (مان، فرهنگ تطبیقی هندواروپایی، ص ۱۱۶) به‌راستی «بوتیمار» را زیر ریشهٔ bhu- «زوزه، توفان» نهاده است، اما این نظری یکّه است و هیچ ایران‌شناسی آن را نپذیرفته. تحلیل پذیرفته‌شده آن است که «بوتیمار» ترکیبی است از «بو» (کوتاه‌شدهٔ کنیهٔ عربی «ابو»، چنان‌که در بوعلی و بوالهوس) و «تیمار» به معنای «غم، اندوه، پرستاری»؛ یعنی «پدرِ اندوه». برهان قاطع (جلد ۱، ص ۳۱۳) خود همین را می‌رساند: «نام مرغی است که او را غم‌خورک نیز گویند و او پیوسته در کنار آب نشیند و از غم آنکه مبادا آب کم شود با وجود تشنگی آب نخورد». افزون بر این هیچ راه آوایی از اوستایی bučahin- / buxti- به «بوتیمار» نمی‌رسد؛ جزء دوم همان tīmār فارسی میانه (پارتی tymʾr) «تیمار، رنج» است و جزء نخست هرگز -č- یا -xt- نداشته است. پس پژوهش امروزی این پیکان را رد می‌کند: «بوتیمار» ترکیبی فارسی با پیشوند عربی است، نه بازماندهٔ واژه‌های نام‌آوای اوستایی.\",\n     \"sources\": [W + \"%D8%A8%D9%88%D8%AA%DB%8C%D9%85%D8%A7%D8%B1\"],\n     \"ref_check\": [\n      {\"ref\": \"IEC:116\", \"status\": \"supports\",\n       \"note\": \"Mann p. 116 (IEC.txt leaf 78): \\\"bhu- (2) 'howl, gale, blast. Cf. bhubh-' Arm. bu (o-st. 'owl') beside buk, pl. form 'gale, storm'; Per. cf. bu timar 'heron'; Phryg. or Mac. buza 'owl'; Du. bui 'squall'; cf. Lat. butio and MIr. bufa\\\". Nourai's citation is accurate — the reference does say what he draws, but Mann puts the word straight under the IE base, not under the Avestan node, and no other source repeats him.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"vol. 1, printed p. 313 (BQT_v1_pages.txt leaf 533)\", \"stance\": \"contradicts\",\n       \"note\": \"\\\"بوتیمار. با میم بر وزن موسیقار. نام مرغی است که او را غم‌خورک نیز گویند، و او پیوسته در کنار آب نشیند و از غم آنکه مبادا آب کم شود با وجود تشنگی آب نخورد ... و او را به عربی یمام و به یونانی شفنین خوانند\\\" — Borhan's own gloss builds the name on تیمار/غم 'grief', not on a cry.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi, s.v. بوتیمار (MON_part2.txt line 2727)\", \"stance\": \"silent\",\n       \"note\": \"Mo'in has the headword بوتیمار but the local (2-vol. abridged) text carries no origin tag for it; the 6-vol. page Nourai would need is not page-mapped in any copy on disk.\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org/wiki/بوتیمار\", \"stance\": \"contradicts\",\n       \"note\": \"\\\"From بو (bu), from Arabic أَبُو (ʔabū), used to form nicknames, literally 'father of' + تیمار (timâr, 'worry; sorrow')\\\", with the usage note \\\"In medieval sources, the bittern is believed to be sick with worry that the river is going to dry up, hence the name.\\\"\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Pahlavi\", \"words\": \"bŭm 1\", \"verdict\": \"disputed\",\n     \"derivation\": \"No Pahlavi būm 'owl' is attested. MacKenzie, A Concise Pahlavi Dictionary, has two separate entries on the same page: \\\"būf [bwp | N بوف], *būg [bwk'] owl\\\" and \\\"būm [bwm | N ~] land, earth, country\\\" — the Middle Persian owl-word is būf / *būg (written bwp, bwk'), while būm is the ordinary word for 'land' (Av./OP būmī-, PIE *bʰuH- 'to be, grow'). Nyberg's glossary agrees: \\\"būm [bwm; 'RK'] land, landed estate ... Av. OP būmī-; Paz. NP bum\\\", with no bird sense. Aryanpur's Persian IE-roots dictionary, s.v. بوف، بوم 'owl' (p. 136), likewise gives the Pahlavi line as BUF, BUFG, BUG and no BŪM. Horn, Grundriss der neupersischen Etymologie, keeps the two apart in adjacent paragraphs: §237 (1)būm 'Erde, Land' with \\\"phlv. būm\\\", §238 (2)būm, būf 'Eule' with no Pahlavi form at all. So the Pahlavi box is Nourai's own back-projection of the New Persian word: the -f/-g form is what Middle Persian actually had, and the -m of NP būm arises only later (in part by contamination with the homophonous būm 'land', in part, on the competing view, by borrowing from Arabic būm). The cited reference does not help either: Mo'in is a New Persian dictionary and, in the copy on disk, tags بوم 'owl' as Arabic, not Pahlavi.\",\n     \"derivation_fa\": \"صورت پهلوی būm به معنای «جغد» در هیچ متنی گواهی نشده است. مکنزی در فرهنگ کوچک پهلوی دو مدخل جدا دارد: būf [bwp] و *būg [bwk'] «جغد» در برابر būm [bwm] «سرزمین، زمین». نیبرگ نیز būm را تنها «زمین، ملک» می‌داند و آن را به اوستایی و پارسی باستان būmī- بازمی‌گرداند. آریان‌پور هم در مدخل «بوف، بوم (به چم جغد)» (ص ۱۳۶) ردیف پهلوی را BUF, BUFG, BUG آورده و BŪM نیاورده است. هرن در دو بند پیاپی همین جدایی را نگه می‌دارد: بند ۲۳۷ «بوم = زمین» با صورت پهلوی būm، و بند ۲۳۸ «بوم، بوف = جغد» بی هیچ صورت پهلوی. بنابراین جعبهٔ پهلویِ نورایی فرافکنی واژهٔ فارسی نو به دورهٔ میانه است؛ آنچه فارسی میانه داشته صورت -f/-g بوده و «م» پایانی فارسی نو یا از آمیختگی با «بوم» هم‌آوا (به معنی سرزمین) پدید آمده یا — بنا بر دیدگاه رقیب — از وام‌گیری عربی بوم. خطای کتاب است، نه خطای خوانش اسکن.\",\n     \"sources\": [W + \"%D8%A8%D9%88%D9%85\", \"https://abadis.ir/fatofa/%D8%A8%D9%88%D9%85/\"],\n     \"ref_check\": [\n      {\"ref\": \"MON:606\", \"status\": \"contradicts\",\n       \"note\": \"Mo'in's page 606 could not be opened directly (no page-mapped copy of the 6-vol. Farhang exists on disk or online), but the entry itself is in the 2-vol. Adena abridgement, MON_part1.txt line 26209: \\\"بوم: [ع.] (ا.) (جاد.) جغد، بوف\\\" — Mo'in gives no Pahlavi form and tags the owl-word [ع.] = Arabic, the opposite of the Pahlavi ancestry Nourai cites him for. The abadis.ir rendering of the same Mo'in entry likewise gives only 'جغد' with no Middle Persian etymon.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, s.v. būf / būm (PHD.txt line 292)\", \"stance\": \"contradicts\",\n       \"note\": \"\\\"būf [bwp | N بوف], *būg [bwk'] owl. buland ... būm [bwm | N ~] land, earth, country\\\" — the Pahlavi owl-word is būf/*būg; būm is 'land'.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. būm (NYB_vol2_glossary.txt line 1037)\", \"stance\": \"contradicts\",\n       \"note\": \"\\\"būm [bwm; 'RK'] land, landed estate ... Av. OP būmī-; Paz. NP bum\\\" — no 'owl' sense in Pahlavi.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur p. 136, s.v. بوف، بوم (به چم 'جغد')\", \"stance\": \"contradicts\",\n       \"note\": \"The Pahlavi row of the entry reads \\\"پهلوی (PAHLAVI): BUF, BUFG, BUG\\\"; references given are POKORNY 97-98, MACKENZIE (OWL) 126, برهان قاطع ۳۱۹. Read from the page image, saved to data/verification/sources/refs/ocr/ARY/0136.vision.txt.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss nos. 237-238 (HRN.txt lines 2437-2442)\", \"stance\": \"contradicts\",\n       \"note\": \"\\\"237. (1)būm 'Erde, Land'. ap. būmi- 'Erde'; aw. būmī-; phlv. būm\\\" — but \\\"238. (2)būm, būf 'Eule'. arm. bu, buec 'Eule'; lat. bubō; gr. byas, byza. Onomatopoetisch\\\" carries no Pahlavi form.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Persian\", \"words\": \"bŭm 1 «بوم ١»\", \"verdict\": \"plausible\",\n     \"derivation\": \"The New Persian word is real and its membership in this onomatopoeic family is asserted by Nourai's own reference: Pokorny p. 97 opens the entry with \\\"Npers. būm 'Eule'\\\", beside Arm. bu, buec, Gk. βύας/βύζα, Lat. būbō 'eagle-owl'. Walde-Pokorny II 112 has the same list, and Horn no. 238 gives \\\"(2)būm, būf 'Eule'\\\" with the express verdict \\\"Onomatopoetisch, sonst würden die Lautverhältnisse nicht stimmen\\\" — i.e. the sound correspondences only work because the word is a fresh imitation, not a regular inheritance. Aryanpur (p. 136) repeats this, noting that no Persian source traces the word further and that etymologists take it as a نام‌آوا. The ill-omen sense Nourai glosses is exactly Borhan-e Qate' vol. 1 p. 318: \\\"بوف ... پرنده‌ایست که به نحوست اشتهار دارد، و آن را بوم نیز گویند\\\" ('a bird famous for ill luck, also called būm'), and the couplet printed in the box (بلبل به باغ و بوم به ویرانه ساخته...) is faithfully extracted. What is only plausible, not confirmed, is the route: the parent drawn for it (a Pahlavi būm 'owl') does not exist (node #3), and Wiktionary and Mo'in both make NP بوم 'owl' a loan from Arabic بُوم — itself onomatopoeic and with Semitic parallels — which would explain the -m against Middle Persian būf/būg. Either way the word ultimately imitates the hoot; only the transmission is at issue.\",\n     \"derivation_fa\": \"واژهٔ فارسی نو «بوم» به معنی جغد اصیل است و مأخذ خود نورایی آن را زیر همین ریشه نهاده: پوکورنی در ص ۹۷ مدخل را با «Npers. būm ‹Eule›» می‌آغازد و در کنار آن ارمنی bu، buec، یونانی βύας/βύζα و لاتین būbō را می‌آورد. والده-پوکورنی (ج ۲، ص ۱۱۲) همان فهرست را دارد و هرن در بند ۲۳۸ می‌نویسد «بوم، بوف = جغد ... نام‌آواست، وگرنه تناسب‌های آوایی درست درنمی‌آید»؛ یعنی این واژه بازآفرینی تازهٔ آوای جغد است نه میراث قاعده‌مند. آریان‌پور (ص ۱۳۶) نیز همین را می‌گوید. معنایی که نورایی آورده («جغدی که دیدنش را شوم می‌دانستند») درست همان است که برهان قاطع در ص ۳۱۸ آورده: «بوف ... پرنده‌ایست که به نحوست اشتهار دارد و آن را بوم نیز گویند»؛ بیت چاپ‌شده در جعبه نیز درست استخراج شده است. آنچه با احتیاط پذیرفتنی است نه بیشتر، مسیر انتقال است: پدرِ ترسیم‌شده (بومِ پهلوی به معنی جغد) وجود ندارد، و ویکی‌واژه و معین هر دو «بوم» فارسی را وام از «بُوم» عربی می‌دانند که خود نام‌آواست؛ همین وام‌گیری «م» پایانی را در برابر būf/būg فارسی میانه توضیح می‌دهد.\",\n     \"sources\": [W + \"%D8%A8%D9%88%D9%85\", \"https://abadis.ir/fatofa/%D8%A8%D9%88%D9%85/\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:97\", \"status\": \"supports\",\n       \"note\": \"POK_01.txt leaf 106: \\\"Npers. bum ,Eule'; arm. bu, buec ,Eule' (ohne Lautverschiebung im Schallwort), gr. byas m., byza f. ,Uhu' ... lat. bubo ,Uhu'\\\" — the New Persian word stands first in Pokorny's list, exactly as the chart has it.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 238 (HRN.txt line 2437)\", \"stance\": \"supports\",\n       \"note\": \"\\\"238. (2)būm, būf 'Eule'. arm. bu, buec 'Eule' (H. No. 59); lat. bubō; gr. byas, byza. Onomatopoetisch, sonst würden die Lautverhältnisse nicht stimmen.\\\"\"},\n      {\"src\": \"BQT\", \"where\": \"vol. 1, printed p. 318 (BQT_v1_pages.txt leaf 538; page image archive.org/details/borhan-ghate-v1/page/n538)\", \"stance\": \"supports\",\n       \"note\": \"\\\"بوف - بر وزن صوف، پرنده‌ایست که بنحوست اشتهار دارد، و آنرا بوم نیز گویند\\\" — Borhan gives precisely Nourai's gloss 'owl whose sight was believed to bring misfortune'.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur p. 136, s.v. بوف، بوم (به چم 'جغد')\", \"stance\": \"supports\",\n       \"note\": \"IE line \\\"*ULŪKOS, *BH(E)U-\\\", references POKORNY 97-98; note 2: \\\"برخی از واژه‌ریشه‌شناسان اصل این واژه را گونه‌ای 'نام آوا' (ONOMATOPOEIA) می‌دانند\\\".\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. بوم (MON_part1.txt line 26209) and abadis.ir\", \"stance\": \"contradicts\",\n       \"note\": \"\\\"بوم: [ع.] (ا.) (جاد.) جغد، بوف\\\" — Mo'in marks the owl-word as an Arabic loan, as does Wiktionary (\\\"Borrowed from Arabic بُوم\\\"), against an inherited Iranian descent.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Latin\", \"words\": \"bŭtîre; butio; bŭteô\", \"verdict\": \"confirmed\",\n     \"derivation\": \"All three Latin words are real and all three are put under this root by Nourai's two references. Walde-Pokorny II 112 lists them together: \\\"lat. būtio 'Rohrdommel', būtīre 'vom Naturlaut der Rohrdommel', būteo 'eine Falkenart'\\\" (Pokorny's abridgement on p. 97 keeps būtio and būteo and drops the verb). būtīre is a first-conjugation denominative/imitative verb 'to utter the sound bū', of the same expressive type as Lat. būbō 'eagle-owl' and būbere; būtiō, -ōnis is an -iō agent/animal noun from it ('the bū-crier' = bittern), and būteō, -ōnis the same formation applied to a buzzard-like hawk. Klein s.v. bittern (p. 176) states the chain explicitly: \\\"L. būteō ... derives fr. būtīre, 'to cry like a bittern', which is of imitative origin and lit. means 'to utter the sound bū'. Cp. L. būbere, a synonym of būtīre, and būbō, 'owl'.\\\" Nourai's gloss for būtīre — 'to make a \\\"bu\\\" sound' — is Klein's wording verbatim.\",\n     \"derivation_fa\": \"هر سه واژهٔ لاتینی اصیل‌اند و هر دو مأخذی که نورایی آورده آنها را زیر همین ریشه می‌نشانند. والده-پوکورنی (ج ۲، ص ۱۱۲) هر سه را کنار هم دارد: būtio «بوتیمار/بلبل آبی»، būtīre «از آوای طبیعی بوتیمار» و būteo «گونه‌ای باز». būtīre فعلی است از صرف نخست و ساختی نام‌آوا به معنی «آوای بو برآوردن»، از همان گونه‌ای که būbō «جغد بزرگ» و būbere دارند؛ būtiō, -ōnis نامی است با پسوند -iō از همان فعل («بو-گو») و būteō, -ōnis همان ساخت برای پرنده‌ای شکاری. کلاین در ذیل bittern (ص ۱۷۶) زنجیره را روشن می‌گوید: «būteō ... از būtīre ‹مانند بوتیمار بانگ زدن› می‌آید که ساختی تقلیدی است و لفظاً یعنی ‹آوای بو برآوردن›». معنایی که نورایی برای būtīre نوشته عیناً عبارت کلاین است. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. beu-2: \\\"1. Latin butio (perhaps > Old French butor), bittern: BITTERN1. 2. Latin buteo, a kind of hawk: BUZZARD.\\\" (AHD_watkins1985.txt line 321).\"},\n      {\"ref\": \"KLN:176,213\", \"status\": \"supports\",\n       \"note\": \"Both page numbers are exact. KLN_1966.txt leaf 104 carries the printed page marker '176' and the entry \\\"bittern, n., a heronlike bird. — ME. bitour, fr. OF. (= F.) butor, fr. VL. *būti-taurus, a compound of L. būteō, būtiō, 'a kind of falcon or hawk', and taurus, 'ox'. L. būteō derives fr. būtīre, 'to cry like a bittern' ... lit. means 'to utter the sound bū'.\\\"; leaf 124 (printed 213/214) has \\\"Buteo, n., a genus of hawks, the buzzard. — L. būteō, 'a kind of falcon or hawk', rel. to būtīre ... from the I.-E. imitative base *bū-, whence also L. būbō\\\".\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. II p. 112\", \"stance\": \"supports\",\n       \"note\": \"\\\"lat. butio ,Rohrdommel', butire ,vom Naturlaut der Rohrdommel', buteo ,eine Falkenart'\\\" — the only source on disk that also has the verb būtīre, which Pokorny's condensed entry omits.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Bittern (SKT.txt line 1851)\", \"stance\": \"supports\",\n       \"note\": \"\\\"Bittern, a bird. (F.-Low L.) ... M.E. bitoure. F. butor ... Low L. būtōrius, a bittern; cf. L. butio, a bittern. Origin unc[ertain], but prob. from the imitative base BU, to make a booming noise: whence L. būtīre, to cry like a bittern, L. būbō\\\".\"},\n      {\"src\": \"LEW\", \"where\": \"Walde 1910, searched for būcina/bulla/bucca\", \"stance\": \"silent\",\n       \"note\": \"The 1910 OCR on disk yields no readable entry for these headwords (grep -n -i 'bucina|^bulla|^bucca' LEW_1910.txt returns nothing); nothing to add either way.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"bittern; buzzard\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Both English birds go back to the Latin node above, by well-documented Old French routes. Bittern: Middle English bitour (14th c.) < Old French/French butor < Vulgar Latin *būti-taurus, a compound of L. būtiō/būteō with taurus 'ox'; Klein (p. 176) explains the odd second element from Pliny, Nat. Hist. 10.42, who reports that in Gaul the bittern was called taurus because its booming call suggests the bellowing of oxen. The final -n of English bittern is a late unetymological addition on the model of marten. Buzzard: Middle English busard < Old French busard, formed with the suffix -ard from Old French buison/buson (whence modern French buse), from the Latin accusative būteōnem. Skeat gives the same two chains independently. The node has no refs of its own but is the natural continuation of node #5, and both derivations are uncontroversial.\",\n     \"derivation_fa\": \"هر دو نام پرنده در انگلیسی از همان گرهٔ لاتینی بالا و از راه فرانسهٔ کهن آمده‌اند. bittern: انگلیسی میانه bitour (سدهٔ چهاردهم) از فرانسهٔ کهن butor، از لاتین عامیانه *būti-taurus، ترکیبی از būtiō/būteō با taurus «گاو نر»؛ کلاین (ص ۱۷۶) جزء دوم را با گواهی پلینیوس (تاریخ طبیعی ۱۰٫۴۲) توضیح می‌دهد که می‌گوید در گُل این پرنده را taurus می‌خواندند زیرا بانگش به بانگ گاو می‌ماند. «ن» پایانی در bittern افزودهٔ متأخر و بی‌ریشه است، به قیاس marten. buzzard: انگلیسی میانه busard از فرانسهٔ کهن busard، ساخته با پسوند ard- از buison/buson فرانسهٔ کهن (فرانسهٔ امروز buse)، از حالت مفعولی لاتین būteōnem. اسکیت نیز همین دو زنجیره را جداگانه می‌آورد. این گره مأخذی از خود ندارد اما دنبالهٔ طبیعی گرهٔ ۵ است و هر دو ریشه‌شناسی بی‌مناقشه‌اند؛ ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n       \"note\": \"The chart gives no reference for this box; it inherits AHD and KLN:176,213 from its parent node #5, both of which name BITTERN1 and BUZZARD as the English outcomes.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"pp. 176 and 213 (KLN_1966.txt lines 5085-5087, 5958, 5984)\", \"stance\": \"supports\",\n       \"note\": \"\\\"bittern ... ME. bitour, fr. OF. (= F.) butor, fr. VL. *būti-taurus ... a passage in Pliny (10,42), in which the author relates that in Gaul the bittern was called taurus (i.e. 'ox') because of its voice suggestive of the bellowing of oxen. For the suffixed -n in bittern cp. marten.\\\"; \\\"buzzard, n. — ME. busard, fr. OF. bus-ard, formed, with change of suff., fr. OF. buis-on, bus-on ... fr. L. būteōnem, acc. of būteō\\\".\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Bittern, Buzzard (SKT.txt lines 1851, 2545)\", \"stance\": \"supports\",\n       \"note\": \"\\\"Buzzard. (F.-L.) M.E. busard ... an inferior kind of falcon. — F. busard ... F. buse, a buzzard; with suffix -ard. — Low L. *buso — L. buteo, a sparrow-hawk.\\\" and the Bittern entry quoted above.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985, index (AHD_watkins1985.txt lines 1309, 1326)\", \"stance\": \"supports\",\n       \"note\": \"The word index assigns \\\"BITTERN1 beu-2\\\" and \\\"BUZZARD beu-2\\\", i.e. exactly this root.\"}\n     ]\n    }\n   ]\n  },\n\n  {\n   \"entry\": 1,\n   \"root\": \"Beu 2, Bheu 2\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *b(e)u-, *bh(e)u- 'to blow up, swell' (the burst of an inflated cheek); Pokorny IEW 98-102, Watkins/AHD 'beu-1'\",\n   \"note\": \"Pokorny IEW p. 98: \\\"b(e)u-, bh(e)u- ,aufblasen, schwellen', Sprenglaut der aufgeblasenen Backe, wie auch pu-, phu- ... Aus dem Begriff der aufgeblasenen Backe entwickeln sich die Bedeutungen ,aufschwellen, rundlich Aufgetriebenes ... auch ,anschwellen machen, stopfen' und ,blasen, husten u. dgl.'\\\", and he adds the express warning that this root is 'ursprünglich verschieden' from the sound-imitating b(e)u- of p. 97 — i.e. Nourai's Beu 1 and Beu 2 are Pokorny's own two entries, correctly separated and correctly glossed. Watkins has the same root as beu-1: \\\"Appears in words loosely associated with the notion 'to swell'. [Pok. 2. beu- 98.]\\\", and the whole Germanic *puk-/bosom/boast branch and the Latin bulla/bullire/bucca branch of Nourai's chart are Watkins's own I, II and III. The weak points of the entry are not the root but three arrows: the Latin trumpet-word (node #1), the Persian envelope-word (node #7) and a misprinted Latin form (node #10).\",\n   \"note_fa\": \"پوکورنی در ص ۹۸ می‌نویسد: «b(e)u-, bh(e)u- ‹باد کردن، آماسیدن›، آوای ترکیدنِ گونهٔ باد‌کرده، همچون pu- و phu-؛ از مفهوم گونهٔ باد‌کرده معناهای ‹ورم کردن، چیز گِرد و برآمده› و نیز ‹دمیدن، سرفه کردن› پدید آمده است»، و به‌صراحت می‌افزاید که این ریشه «در اصل جدا» از ریشهٔ نام‌آوای ص ۹۷ است. پس Beu 1 و Beu 2 نورایی همان دو مدخل جداگانهٔ پوکورنی‌اند و برچسب و معنای هر دو درست است. واتکینز نیز همین را با نشان beu-1 آورده («در واژه‌هایی که به‌گونه‌ای آزاد با مفهوم ‹آماسیدن› پیوند دارند»؛ ارجاع به پوکورنی ۹۸) و شاخهٔ ژرمنی *puk- و شاخهٔ لاتینی bulla/bullire/bucca در نمودار نورایی درست همان بخش‌های I و II و III اوست. ضعف این مدخل در خودِ ریشه نیست، بلکه در سه پیکان است: واژهٔ لاتینیِ شیپور (گرهٔ ۱)، واژهٔ فارسی «پاکت» (گرهٔ ۷) و یک صورت لاتینی نادرست‌چاپ‌شده (گرهٔ ۱۰).\",\n   \"sources\": [W + \"bucina\"],\n   \"ref_check\": [\n    {\"ref\": \"POK:98\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt leaf 107 (page marker '98'): \\\"b(e)u-, bh(e)u- ,aufblasen, schwellen', Sprenglaut der aufgeblasenen Backe ... Ursprünglich verschieden sind die Schallwurzeln 1. b(e)u- für dumpfe Schalleindrücke und bu- ,Lippe, Kuß'.\\\" Root, language label and gloss all correct.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. beu-1 (AHD_watkins1985.txt line 321)\", \"stance\": \"supports\",\n     \"note\": \"\\\"beu-1. Also bheu-. Appears in words loosely associated with the notion 'to swell'. I. Root form *beu-. 1. Germanic *puk- ... II. Root form *bheu- ... III. Root form *beu-. 1. Latin bulla ... 2. Latin bullire ... 3. Possibly Latin bucca ... (inflated) cheek ... [Pok. 2. beu- 98.]\\\"\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II pp. 114ff. (WLD_Bd2_pages.txt lines 7395, 7503, 7619)\", \"stance\": \"supports\",\n     \"note\": \"Under the 'aufblasen, schwellen' root: \\\"ags. pocca, pohha ,(*aufgeblasener) Sack', mnl. pocke ,Blatter, Pocke' ... engl. poke ds., nhd. pfoch ,Beutel'\\\" and \\\"Erweiterungen mit l sind vielleicht ai. buliḥ, lit. bulis, lat. bulla u. dgl.\\\" — both branches Nourai draws.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. buccal (KLN_1966.txt line 5759, printed p. 216)\", \"stance\": \"supports\",\n     \"note\": \"\\\"buccal ... fr. L. bucca, 'cheek', from the I.-E. imitative base *bu-, 'to blow; to swell'. Cp. Bubo, buckle, bull, 'edict', debouch, disembogue, embouchure, pocket, poke, 'a bag', pox, puck.\\\" — Klein groups the same Latin and Germanic material.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Latin\", \"words\": \"bŭcina\", \"verdict\": \"disputed\",\n     \"derivation\": \"The word and its meaning are right — būcina is the curved horn or war-trumpet (Vegetius, Mil. 3.5: \\\"tuba quae directa est appellatur, bucina quae in semet aereo circulo flectitur\\\") — but the arrow from a root 'to swell, blow' is not what the sources say. Nourai's own reference contradicts him: Ernout-Meillet, Dictionnaire étymologique de la langue latine, p. 138, ends the article \\\"Mot italique (gr. βυκάνη est d'origine latine). Sans doute composé de bou- et -cana (Cuny, Mél. F. de Saussure, p. 109 et suiv.)\\\" — i.e. *bou-canā, literally 'cow-blowing / cow-horn', from bōs 'ox' + the root of canō 'to sound, sing', the same compound type as tībī-cen, tubi-cen. Wiktionary and the current Latin handbooks give the same analysis. Walde-Pokorny II 113 is the only source that keeps an alternative alive, and even there it offers the choice \\\"entweder als *bū-kanā ,bu tutend' zu unserem Schallwort bu, oder als *bou-canā zu bos\\\" — note that the onomatopoeic option is filed under bu- 'muffled sounds', which is Nourai's Beu 1, not Beu 2 'to swell'. Watkins's beu-1 does not list būcina at all. So the arrow is doubly misplaced: the majority view derives the word from 'ox', and even the minority view would put it under the other root on the same page.\",\n     \"derivation_fa\": \"خودِ واژه و معنایش درست است: būcina شیپور خمیدهٔ جنگی است (وگتیوس، De re militari ۳٫۵: «tuba آن است که راست باشد و bucina آن که در حلقه‌ای برنجی بر خود پیچد»). اما پیکانِ کشیده‌شده از ریشهٔ «باد کردن، دمیدن» با منابع نمی‌خواند و مأخذ خود نورایی آن را رد می‌کند: ارنو و مه‌یه در فرهنگ ریشه‌شناختی لاتین (ص ۱۳۸) مقاله را چنین می‌بندند: «واژه‌ای ایتالیک است ... بی‌گمان مرکب از bou- و cana-»؛ یعنی *bou-canā «دمیدنِ گاو، شاخ گاو» از bōs «گاو» و ریشهٔ canō «سراییدن»، از همان گونهٔ ترکیبی tībī-cen و tubi-cen. ویکی‌واژه و دستنامه‌های امروزی لاتین نیز همین را می‌گویند. تنها والده-پوکورنی (ج ۲، ص ۱۱۳) گزینهٔ دیگری را باز می‌گذارد و می‌نویسد «یا *bū-kanā ‹بو-نوازنده› از نام‌آوای bu، یا *bou-canā از bos» — و توجه کنید که همان گزینهٔ نام‌آوایی هم زیر ریشهٔ «آواهای گنگ» (یعنی Beu 1 نورایی) جای گرفته، نه زیر «آماسیدن». واتکینز نیز būcina را اصلاً زیر beu-1 نیاورده است. پس پژوهش امروزی این پیکان را رد می‌کند.\",\n     \"sources\": [W + \"bucina\"],\n     \"ref_check\": [\n      {\"ref\": \"LAT:138\", \"status\": \"contradicts\",\n       \"note\": \"Ernout-Meillet p. 138 (LAT.txt leaf 156, printed page marker '138' on the leaf, headwords bucerus ... bucina ... buda): \\\"bucina, -ae f.: trompette; Vég. Mil. 3,5 ... Mot italique (gr. βυκάνη est d'origine latine). Sans doute composé de bou- et -cana (Cuny, Mél. F. de Saussure, p. 109 et suiv.).\\\" The cited page states the opposite of the arrow.\"},\n      {\"ref\": \"AHD\", \"status\": \"not_found\",\n       \"note\": \"Watkins 1985 s.v. beu-1 lists Germanic *puk-, OE pyffan, OE -pūte, bōsm, būc, Frankish *būk, byle, baustern, Latin bulla, bullire and bucca — būcina appears nowhere in the appendix (grep of AHD_watkins1985.txt for 'bucina' is empty).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. II p. 113 (WLD_Bd2_pages.txt, under 'bu' = the muffled-sound root)\", \"stance\": \"partial\",\n       \"note\": \"\\\"aber βυκάνη ,Trompete' ist entlehnt aus lat. bucina ,Hirtenhorn', das entweder als *bū-kanā ,bu tutend' zu unserem Schallwort bu, oder als *bou-canā zu bos gehört als ,Horn, womit man die Rinder zusammenblast' ... s. zuletzt Niedermann IF. 37, 147\\\" — an open choice, and filed under Nourai's Beu 1, not Beu 2.\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org/wiki/bucina\", \"stance\": \"contradicts\",\n       \"note\": \"\\\"From bōs, bovi- ('cow') + the root of canō ('sing')\\\", with the Romance and Germanic descendants (Sp. bocina, It. buccina, OFr. buisine, MHG busūne > G. Posaune) and Ancient Greek βυκάνη as a borrowing from Latin.\"},\n      {\"src\": \"LEW\", \"where\": \"Walde 1910 (LEW_1910.txt)\", \"stance\": \"silent\",\n       \"note\": \"No readable entry for bucina survives in the OCR of the 1910 edition on disk.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Aramaic\", \"words\": \"bucina\", \"verdict\": \"confirmed\",\n     \"derivation\": \"The Latin trumpet-word was taken into Aramaic in the Roman East as Syriac ܒܘܩܝܢܐ būqīnā 'horn, trumpet' — a straight loan with the Latin -īna ending preserved and Latin c rendered by Syriac q (the Aramaic transcription of Latin/Greek k before a back vowel; the same word entered Greek as βυκάνη). It is a classic Roman military loan: the bucina was the Roman camp trumpet that marked the watches, and the word travelled with the army and later with the Peshitta's rendering of trumpet-blasts. Fraenkel, Die aramäischen Fremdwörter im Arabischen p. 284, treats the Syriac form as the immediate donor of Arabic būq, which presupposes exactly this Aramaic stage. Nourai spells the Aramaic form 'bucina', i.e. in its Latin dress; the actual Syriac shape is būqīnā, and marking the box 'Aramaic' rather than 'Syriac' is a harmless generalisation.\",\n     \"derivation_fa\": \"واژهٔ لاتینی شیپور در شرقِ رومی به آرامی راه یافت: سریانی ܒܘܩܝܢܐ (būqīnā) «شاخ، شیپور»، وامی مستقیم که پایانهٔ لاتینی -īna را نگه داشته و c لاتینی را با ق سریانی نشان داده است (شیوهٔ معمول برگردان k لاتینی/یونانی پیش از واکهٔ پسین؛ همین واژه در یونانی βυκάνη شد). این وام‌واژه‌ای نظامی است: bucina شیپور اردوگاه رومی بود که پاس‌های شب را اعلام می‌کرد و واژه همراه سپاه و سپس در ترجمهٔ پشیتّا گسترش یافت. فرانکل در «وام‌واژه‌های آرامی در عربی» (ص ۲۸۴) همین صورت سریانی را سرچشمهٔ بی‌واسطهٔ «بوق» عربی می‌داند و این خود مرحلهٔ آرامی را پیش‌فرض می‌گیرد. نورایی صورت آرامی را به جامهٔ لاتینی «bucina» نوشته، حال آنکه صورت سریانی būqīnā است؛ برچسب «آرامی» به‌جای «سریانی» هم تعمیمی بی‌زیان است. ادعای نورایی درست است.\",\n     \"sources\": [W + \"%D8%A8%D9%88%D9%82\"],\n     \"ref_check\": [\n      {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n       \"note\": \"The chart gives this box no reference of its own; it stands between LAT:138/AHD above and BQT:318/AFA:284 below, and Fraenkel p. 284 (checked at node #3) is what actually documents it.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen p. 284 (AFA.txt leaf 314, printed marker '284')\", \"stance\": \"supports\",\n       \"note\": \"\\\"[بوق] ist entlehnt aus [ܒܘܩܝܢܐ] būqīnā (bucina)\\\" — Fraenkel writes the Syriac form and glosses it with the Latin word in brackets, exactly the Latin > Aramaic > Arabic chain of the chart.\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org/wiki/بوق (Arabic section)\", \"stance\": \"supports\",\n       \"note\": \"Compares \\\"Ancient Greek βούκινο / Latin būcina, and Classical Syriac ܒܘܩܝܢܐ (būqīnā)\\\" as the sources of the Arabic word.\"},\n      {\"src\": \"TAD\", \"where\": \"al-Unaysi, Tafsir al-alfaz al-dakhila (TAD.txt)\", \"stance\": \"silent\",\n       \"note\": \"بوق occurs only as the Arabic gloss of other borrowed instrument names (شور/شلوفار, كرنيتة, نفير) and has no entry of its own; nothing on its origin.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Arabic\", \"words\": \"bŭq\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic بُوق būq 'horn, trumpet' is a loan from Aramaic/Syriac būqīnā, itself from Latin būcina. The shortening is the normal Arabic treatment of a foreign trisyllable: the final -īnā was felt as an alien ending and dropped, leaving a CūC shape (būq) that fits the native noun pattern (cf. sūq, ṭūq), after which Arabic could build a broken plural ʾabwāq and a denominative verb. Both of Nourai's references say this. Fraenkel p. 284 states the Syriac source outright; Mo'in's etymological footnote in Borhan-e Qate' at the page Nourai cites (BQT p. 318, footnote 6 to the headword بوق) reads «۶ - از عربی، از لاتینی buccina (سور، نفیر)» — 'from Arabic, from Latin buccina (horn, trumpet)'. The word is old in Arabic: the lexicographers already list it among foreign words (Fraenkel notes it in al-Jawālīqī's Muʿarrab).\",\n     \"derivation_fa\": \"«بُوق» عربی وام‌واژه‌ای است از آرامی/سریانی būqīnā که خود از لاتینی būcina آمده است. کوتاه‌شدن آن رفتار معمول عربی با واژه‌های بیگانهٔ سه‌هجایی است: پایانهٔ īnā- بیگانه احساس شد و افتاد و صورت CūC (بوق) بر جای ماند که با وزن‌های بومی مانند سوق و طوق می‌خواند؛ سپس عربی جمع مکسّر «أبواق» و فعل مشتق از آن ساخت. هر دو مأخذ نورایی همین را می‌گویند: فرانکل (ص ۲۸۴) سرچشمهٔ سریانی را صریح می‌آورد و حاشیهٔ ریشه‌شناختی معین بر برهان قاطع در همان صفحه‌ای که نورایی ارجاع داده (ص ۳۱۸، پانوشت ۶ ذیل مدخل «بوق») چنین است: «۶ - از عربی، از لاتینی buccina (سور، نفیر)». این واژه در عربی کهن است و لغویان عرب خود آن را در شمار معرّبات آورده‌اند (فرانکل به «المعرّب» جوالیقی اشاره می‌کند). ادعای نورایی درست است.\",\n     \"sources\": [W + \"%D8%A8%D9%88%D9%82\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:318\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qate' ed. Mo'in, printed p. 318 (BQT_v1_pages.txt leaf 538; page image https://archive.org/details/borhan-ghate-v1/page/n538, running head ۳۱۸). Headword: «بوق - بضم اول و سکون ثانی و قاف، سفید مهره باشد و آن چیزیست که در حمامها و آسیاها و هنگامها نوازند۶»; Mo'in's footnote 6 at the foot of the page: «۶ - از عربی، از لاتینی buccina (سور، نفیر)». Exactly Nourai's chain, minus the Aramaic link.\"},\n      {\"ref\": \"AFA:284\", \"status\": \"supports\",\n       \"note\": \"Fraenkel p. 284 (AFA.txt leaf 314): \\\"[بوق] ist entlehnt aus [ܒܘܩܝܢܐ] būqīnā (bucina)\\\" — the Aramaic link Mo'in leaves out.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein (KLN_1966.txt)\", \"stance\": \"silent\",\n       \"note\": \"Klein has no entry for Arabic būq (it produced no English word); his bucina-family entries concern only 'bugle' and 'buccinator'.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfaz al-farisiyya al-mu'arraba (AFM.txt)\", \"stance\": \"silent\",\n       \"note\": \"grep for بوق returns only unrelated words (سنبوق; نفير glossed as البوق) — Addi Shir collects Persian, not Aramaic, loans, so the absence is expected and confirms the word is not treated as Persian.\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org/wiki/بوق\", \"stance\": \"supports\",\n       \"note\": \"Arabic بوق: compared with \\\"Ancient Greek βούκινο or Latin būcina, and Classical Syriac ܒܘܩܝܢܐ (būqīnā)\\\"; senses 'trumpet, conch'.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Persian\", \"words\": \"bŭq «بوق»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian بوق būq is a borrowing of Arabic بُوق, taken over unchanged in form and meaning ('horn, trumpet') — an Arabic-mediated round trip of a Latin word, not a Persian inheritance. It is well established by the 5th/11th century: Nāṣer-e Ḵosrow uses it in the Safar-nāma (c. 1050). Borhan-e Qate' p. 318 defines it from the practical Persian usage: 'a white conch-shell; the thing that is sounded in the bath-houses, the mills and at gatherings', and Mo'in's footnote on the same page traces it 'from Arabic, from Latin buccina'. In modern Persian the sense narrowed further to the motor-horn/klaxon. Nourai's Persian script, transliteration and gloss are all correct, and BQT:318 is exactly the right page.\",\n     \"derivation_fa\": \"«بوق» فارسی وام‌گیری از «بُوق» عربی است و صورت و معنای آن («شاخ، شیپور») بی‌دگرگونی گرفته شده — یعنی بازگشتِ یک واژهٔ لاتینی به فارسی از راه عربی، نه میراث ایرانی. این واژه دست‌کم از سدهٔ پنجم هجری در فارسی جا افتاده است؛ ناصرخسرو آن را در سفرنامه (حدود ۴۴۰ ق) به کار برده است. برهان قاطع در ص ۳۱۸ آن را از کاربرد عملی فارسی تعریف می‌کند: «سفید مهره باشد و آن چیزیست که در حمامها و آسیاها و هنگامها نوازند»، و حاشیهٔ معین در همان صفحه آن را «از عربی، از لاتینی buccina» می‌داند. در فارسی امروز معنا باز هم تنگ‌تر شده و به بوقِ خودرو رسیده است. صورت فارسی، آوانگاری و معنای جعبه همه درست است و ارجاع BQT:318 دقیقاً همان صفحهٔ درست است؛ ادعای نورایی درست است.\",\n     \"sources\": [W + \"%D8%A8%D9%88%D9%82\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:318\", \"status\": \"supports\",\n       \"note\": \"Same page as node #3: the headword بوق and Mo'in's footnote «۶ - از عربی، از لاتینی buccina (سور، نفیر)» (Borhan-e Qate' ed. Mo'in p. 318; leaf image archive.org/details/borhan-ghate-v1/page/n538).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org/wiki/بوق (Persian section)\", \"stance\": \"supports\",\n       \"note\": \"\\\"Borrowed from Arabic بُوق (būq)\\\", with the earliest quotation from Nāṣer-e Ḵosrow's Safar-nāma (c. 1060) and the modern sense 'horn, klaxon'.\"},\n      {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi / abadis.ir\", \"stance\": \"supports\",\n       \"note\": \"Mo'in's dictionary entry likewise marks بوق as an Arabic loan; the fuller etymology ('from Latin buccina') is his own footnote in Borhan-e Qate' quoted above.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary\", \"stance\": \"silent\",\n       \"note\": \"No Middle Persian *būq: the word has no pre-Islamic Iranian ancestor, as expected for an Arabic loan (grep of PHD.txt for bwq/būq is empty).\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Germanic\", \"words\": \"puk\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Nourai's reference has it verbatim: Watkins's beu-1, section I.1, sets up \\\"Germanic *puk-\\\" and derives from it (a) Old English pocc 'pustule' > POCK and (b) Old French po(u)che and Old North French poke 'bag' > POACH1, POCKET, POKE3, POUCH, PUCKER. Walde-Pokorny II 114ff. lists the same Germanic group under the 'aufblasen, schwellen' root: \\\"ags. pocca, pohha '(*aufgeblasener) Sack', mnl. pocke 'Blatter, Pocke' ... engl. poke ds., nhd. pfoch 'Beutel'\\\". The semantics are the root's own: a bag is a 'swollen, inflated' thing, exactly as a pock is. On the sound side the Germanic p- corresponds to a PIE b- by Grimm's law, but Pokorny warns on p. 98 that in this expressive root continuous re-creation crosses the regular development, so that Germanic forms with pu- may go back either to IE bu- or to an unshifted or newly made pu-; the derivation is therefore accepted but is not a strict sound-law argument. The chart's shape 'puk' is a bare stem-notation of Proto-Germanic *puk-/*pukkōn-.\",\n     \"derivation_fa\": \"مأخذ نورایی عیناً همین را دارد: واتکینز در بخش I.1 ذیل beu-1 صورت ژرمنی *puk- را می‌نشاند و از آن (الف) انگلیسی کهن pocc «آبله» و (ب) فرانسهٔ کهن po(u)che و فرانسهٔ شمالی کهن poke «کیسه» را می‌گیرد که POCKET و POUCH از آنهاست. والده-پوکورنی (ج ۲، ص ۱۱۴ به بعد) همین گروه ژرمنی را زیر ریشهٔ «باد کردن، آماسیدن» می‌آورد: «انگلیسی کهن pocca، pohha ‹کیسهٔ باد‌کرده›، هلندی میانه pocke ‹آبله›... انگلیسی poke، آلمانی pfoch ‹کیسه›». تحول معنایی از خودِ ریشه برمی‌آید: کیسه چیزی «آماسیده» است، چنان‌که آبله نیز. در آواشناسی، p ژرمنی برابر b هندواروپایی است بر پایهٔ قانون گریم، اما پوکورنی در ص ۹۸ هشدار می‌دهد که در این ریشهٔ نام‌آوایی بازآفرینی پیوسته با تحول قاعده‌مند درمی‌آمیزد و صورت‌های ژرمنیِ pu- می‌توانند از bu- هندواروپایی یا از pu-ی جابه‌جانشده/نوساخته باشند؛ پس این اشتقاق پذیرفته است اما استدلال قانون آوایی محض نیست. صورت «puk» در نمودار همان ستاک ژرمنی آغازین *puk- است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/pocket\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. beu-1: \\\"I. Root form *beu-. 1. Germanic *puk- in: a. Old English pocc, pustule: POCK; b. Old French po(u)che and Old North French poke, bag: POACH1, POCKET, POKE3, POUCH, (PUCKER).\\\" (AHD_watkins1985.txt line 321).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. II (WLD_Bd2_pages.txt lines 7395, 7619)\", \"stance\": \"supports\",\n       \"note\": \"\\\"ags. pocca, pohha ,(*aufgeblasener) Sack', mnl. pocke ,Blatter, Pocke'\\\" and \\\"engl. poke ds., nhd. pfoch ,Beutel', mnd. pūkel ,Beutel', ags. pohha, pocca\\\" — under the 'swell' root.\"},\n      {\"src\": \"ETYMONLINE\", \"where\": \"etymonline.com/word/pocket\", \"stance\": \"supports\",\n       \"note\": \"\\\"Old North French poque ... from a Germanic source akin to Frankish *pokka 'bag', from Proto-Germanic *puk-\\\", itself \\\"from PIE root *beu-, an imitative root associated with words for 'to swell'\\\".\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. buccal (printed p. 216)\", \"stance\": \"partial\",\n       \"note\": \"Klein files pocket and poke 'a bag' with bucca under the imitative base *bu- 'to blow; to swell', i.e. the same root, but without setting up a Germanic *puk- stage.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"French\", \"words\": \"pocket, poche\", \"verdict\": \"plausible\",\n     \"derivation\": \"The Romance stage is real but the box mislabels it. What existed in Gallo-Romance is Old French poche / pouche 'bag, pouch' beside the Old North French (Picard-Norman) doublet poque / poke, both from Frankish *pokka (the Germanic *puk- of node #5); French poche is still the ordinary word for 'pocket'. 'Pocket' itself is not a French word: it is Anglo-French pokete (13th c.), the diminutive in -ete of Old North French poque, which is the immediate source of English pocket — so the form belongs to the Anglo-Norman variety of French written in England rather than to French proper, and it is a diminutive, not the simplex. Watkins's appendix supports the substance of the arrow ('Old French po(u)che and Old North French poke, bag' > POCKET, POUCH), so the derivation is right even though the box's headword is not a French lexeme; hence plausible rather than confirmed.\",\n     \"derivation_fa\": \"مرحلهٔ رومیایی این زنجیره واقعی است اما برچسب جعبه دقیق نیست. آنچه در گالو-رومی وجود داشت poche / pouche فرانسهٔ کهن «کیسه، جیب» است در کنار همتای شمالی (پیکاردی-نورمان) آن poque / poke، و هر دو از فرانکی *pokka (همان *puk- ژرمنی گرهٔ ۵) می‌آیند؛ poche هنوز واژهٔ معمول «جیب» در فرانسه است. اما خودِ «pocket» واژه‌ای فرانسوی نیست: صورت آنگلو-فرانسوی pokete (سدهٔ سیزدهم) است، یعنی مصغّرِ poque با پسوند ete-، که سرچشمهٔ بی‌واسطهٔ pocket انگلیسی است؛ پس این صورت به گونهٔ آنگلو-نورمانِ فرانسه در انگلستان تعلق دارد نه به فرانسهٔ اصلی، و افزون بر آن مصغّر است نه صورت ساده. چون پیوست واتکینز جانِ این پیکان را تأیید می‌کند («po(u)che فرانسهٔ کهن و poke فرانسهٔ شمالی کهن، کیسه» ← POCKET و POUCH)، ادعای نورایی با احتیاط پذیرفتنی است، نه به‌تمامی درست.\",\n     \"sources\": [\"https://www.etymonline.com/word/pocket\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:1011\", \"status\": \"not_checked\",\n       \"note\": \"Page 1011 belongs to the main body of the 1975/76 New College Edition (the entry 'pocket'), which is not on disk and is lending-only on archive.org; only the IE-roots appendix (Watkins 1985) is available locally. That appendix, s.v. beu-1, does carry the substance: \\\"Old French po(u)che and Old North French poke, bag: POACH1, POCKET, POKE3, POUCH, (PUCKER)\\\".\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"ETYMONLINE\", \"where\": \"etymonline.com/word/pocket\", \"stance\": \"partial\",\n       \"note\": \"\\\"mid-14c., from Anglo-French pokete (13c.), diminutive of Old North French poque 'bag' (Old French pouche), from a Germanic source akin to Frankish *pokka 'bag'\\\" — the French forms are poque/pouche; 'pocket' is the Anglo-French diminutive.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. buccal (printed p. 216)\", \"stance\": \"partial\",\n       \"note\": \"Cross-references \\\"pocket, poke, 'a bag'\\\" to the same base but gives no French stage in that article.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. beu-1\", \"stance\": \"supports\",\n       \"note\": \"The appendix names Old French po(u)che and Old North French poke as the Romance link between Germanic *puk- and English POCKET/POUCH.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Persian\", \"words\": \"pâkat «پاکت»\", \"verdict\": \"disputed\",\n     \"derivation\": \"Persian پاکت pākat is indeed a French loan, but of a different word. It comes from French paquet 'packet, parcel', not from poche/pocket: Wiktionary gives \\\"Borrowed from French paquet\\\", Mo'in tags the entry «(کَ) [فر.] (اِ.) ورقهٔ کاغذی تا شده که نامه و غیره را در آن گذارند و در آن را می‌چسبانند», and Dehkhoda spells the source out — «پاکت. [کَ] (از فرانسوی، اِ) (از اصل فرانسوی پاکه، بسته)». French paquet is a diminutive of Old French pacque, from Middle Dutch/Middle Low German pak 'bundle' (Germanic *pakkō-), an etymon entirely separate from *puk- 'bag': the two differ in vowel and in geminate, and paquet never meant 'pocket'. The word entered Persian late — with the European postal service in the Qajar period — and narrowed in Persian to 'envelope' (the general sense 'packet' survives in the plural پاکات). So Nourai's reference supports only the words 'from French'; the specific arrow from poche/pocket is wrong.\",\n     \"derivation_fa\": \"«پاکت» به‌راستی وام‌واژه‌ای فرانسوی است، اما از واژه‌ای دیگر: از paquet فرانسوی «بسته، مرسوله»، نه از poche/pocket. ویکی‌واژه می‌نویسد «وام‌گرفته از فرانسوی paquet»؛ معین در فرهنگ خود مدخل را «(کَ) [فر.] (اِ.) ورقهٔ کاغذی تا شده که نامه و غیره را در آن گذارند» می‌آورد و دهخدا سرچشمه را صریح می‌گوید: «پاکت. [کَ] (از فرانسوی، اِ) (از اصل فرانسوی پاکه، بسته)». paquet فرانسوی خود مصغّرِ pacque فرانسهٔ کهن است از pak هلندی میانه/آلمانی سفلای میانه «بسته، عِدل» (ژرمنی *pakkō-)، که ریشه‌ای یکسره جدا از *puk- «کیسه» است: در واکه و در همخوان مشدّد تفاوت دارند و paquet هرگز معنای «جیب» نداشته است. این واژه دیر و همراه با پست اروپایی در دورهٔ قاجار وارد فارسی شد و در فارسی معنایش به «پوشش کاغذی نامه» تنگ شد (معنای عام «بسته» در جمع «پاکات» مانده است). پس مأخذ نورایی تنها «فرانسوی بودن» را تأیید می‌کند و پیکانِ او از poche/pocket نادرست است؛ پژوهش امروزی آن را رد می‌کند.\",\n     \"sources\": [W + \"%D9%BE%D8%A7%DA%A9%D8%AA\", \"https://abadis.ir/fatofa/%D9%BE%D8%A7%DA%A9%D8%AA/\"],\n     \"ref_check\": [\n      {\"ref\": \"MON:668\", \"status\": \"partial\",\n       \"note\": \"Mo'in's own entry, quoted from abadis.ir (فرهنگ معین): \\\"(کَ ) [ فر. ] ( اِ. ) ورقة کاغذی تا شده که نامه و غیره را در آن گذارند و در آن را می چسبانند\\\" — the tag [فر.] confirms 'from French', which is all Nourai can take from the page; Mo'in names no French word, and the accompanying Dehkhoda article names paquet ('از اصل فرانسوی پاکه، بسته'), not poche. The 6-vol. page 668 itself cannot be opened (no page-mapped copy exists); the same entry is in MON_part1.txt line 28412.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org/wiki/پاکت\", \"stance\": \"contradicts\",\n       \"note\": \"\\\"Borrowed from French paquet\\\"; senses 'packet, parcel, envelope'. No connection with poche.\"},\n      {\"src\": \"MON\", \"where\": \"abadis.ir/fatofa/پاکت (فرهنگ معین + لغت‌نامهٔ دهخدا)\", \"stance\": \"partial\",\n       \"note\": \"Dehkhoda: «پاکت. [ ک َ ] ( از فرانسوی ، اِ ) ( از اصل فرانسوی پاکه ، بسته ) و در فارسی محفظه‌ای از کاغذ نامه را گویند» — French, but the word paquet 'bundle'.\"},\n      {\"src\": \"ETYMONLINE\", \"where\": \"etymonline.com/word/pocket (for the *puk- family)\", \"stance\": \"contradicts\",\n       \"note\": \"The *puk- family yields poque/pouche/poke/pocket only; 'packet' belongs to the separate Middle Dutch pak group, so the two cannot be joined at this node.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"English\", \"words\": \"pocket, pouch\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Both are the regular English outcomes of the Romance node above. Pocket: Middle English poket (mid-14th c.) < Anglo-French pokete (13th c.), the -ete diminutive of Old North French poque 'bag'; the sense 'small bag sewn into a garment' is first clear in the early 15th century, and the modern figurative senses ('pocket of resistance', 'out of pocket') are 18th-20th century developments. Pouch: Middle English pouche < Old North French pouche, the Picard-Norman form of Old French poche, same Frankish *pokka. Watkins lists both words under beu-1 at this exact point, so the box's reference is correct.\",\n     \"derivation_fa\": \"هر دو واژه بازده قاعده‌مند گرهٔ رومیایی بالایند. pocket: انگلیسی میانه poket (میانهٔ سدهٔ چهاردهم) از آنگلو-فرانسوی pokete (سدهٔ سیزدهم)، مصغّرِ poque «کیسه» در فرانسهٔ شمالی کهن؛ معنای «کیسهٔ کوچک دوخته‌شده در جامه» از آغاز سدهٔ پانزدهم روشن می‌شود و معناهای مجازی امروزی از سدهٔ هجدهم به بعد پدید آمده‌اند. pouch: انگلیسی میانه pouche از pouche فرانسهٔ شمالی کهن، صورت پیکاردی-نورمانِ poche فرانسهٔ کهن، از همان *pokka فرانکی. واتکینز هر دو واژه را دقیقاً در همین جای ذیل beu-1 آورده است، پس ارجاع جعبه درست است و ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/pocket\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. beu-1 I.1.b: \\\"Old French po(u)che and Old North French poke, bag: POACH1, POCKET, POKE3, POUCH, (PUCKER)\\\"; the word index (line 2106/2112) files POCK and POKE3 under beu-1 as well.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"ETYMONLINE\", \"where\": \"etymonline.com/word/pocket\", \"stance\": \"supports\",\n       \"note\": \"\\\"Anglo-French pokete (13c.), diminutive of Old North French poque 'bag' (Old French pouche)\\\"; senses developed 'small bag' (early 15c.) > billiards (1754), mining (1850), military (1918), 'money' (1717).\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. buccal (printed p. 216)\", \"stance\": \"supports\",\n       \"note\": \"Lists \\\"pocket, poke, 'a bag'\\\" among the words referred to the imitative base *bu- 'to blow; to swell'.\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"English\", \"words\": \"bosom, big, bud, boast, bucket, puff\", \"verdict\": \"disputed\",\n     \"derivation\": \"Four of the six are sound, one is doubtful and one is wrong. PUFF: Watkins beu-1 I.2, \\\"Old English pyffan, to blow out: PUFF\\\" — confirmed. BUD: Klein derives it from the root explicitly, \\\"bud, n. — ME. budde, rel. to Du. bot, 'bud', OS. budil, 'bag, purse', MDu. budel ... G. Beutel, of s.m., fr. I.-E. base *b(h)u-, 'to swell'. See buccal\\\" — confirmed. BOAST: Klein, \\\"rel. to OS. bōsi ... fr. Teut. base *baus-, which lit. means 'to blow up, puff up, swell'. This base is an enlarged form of I.-E. *bhāu-, *bhu-\\\", and Watkins beu-1 II.5 (German dialectal baustern 'to swell' > Middle English bost) — confirmed. BUCKET: Klein, \\\"ME., fr. AF. buket, dimin. formed fr. OE. būc, 'body, belly, pitcher'\\\", and Watkins beu-1 II.2 puts OE būc under the root — confirmed. BOSOM: Watkins beu-1 II.1 has \\\"Old English bōsm, bosom: BOSOM\\\", but Klein flatly calls it \\\"of uncertain etymology\\\" after listing the West Germanic cognates — partial. BIG: not derivable from this root at all; Klein has \\\"big, adj. — ME. bigge, big, of uncertain origin\\\", the word is absent from Watkins's beu-1 (and from his index under any root), and the usual guess is a Scandinavian source — disputed. Per the rule that a mixed box takes its worst word's verdict, the node is marked disputed for 'big' alone.\",\n     \"derivation_fa\": \"از شش واژهٔ این جعبه چهار تا درست است، یکی مشکوک و یکی نادرست. puff: واتکینز ذیل beu-1 بخش I.2 «انگلیسی کهن pyffan ‹فوت کردن›» — درست. bud: کلاین آن را صریح از همین ریشه می‌گیرد: «انگلیسی میانه budde، هم‌ریشه با bot هلندی ‹جوانه›، budil ساکسونی کهن ‹کیسه›... از ریشهٔ هندواروپایی *b(h)u- ‹آماسیدن›» — درست. boast: کلاین آن را به ستاک ژرمنی *baus- «باد کردن، پف کردن، آماسیدن» می‌رساند که گسترشی از *bhāu-/*bhu- هندواروپایی است، و واتکینز نیز (بخش II.5) همین را دارد — درست. bucket: کلاین «از آنگلو-فرانسوی buket، مصغّرِ būc انگلیسی کهن ‹تنه، شکم، کوزه›»، و واتکینز būc را زیر همین ریشه می‌نشاند — درست. bosom: واتکینز (بخش II.1) آن را زیر ریشه می‌آورد اما کلاین پس از برشمردن هم‌ریشه‌های ژرمنی غربی می‌نویسد «ریشه‌اش نامعلوم است» — نیم‌درست. big: به‌هیچ‌روی از این ریشه نمی‌آید؛ کلاین می‌نویسد «انگلیسی میانه bigge، big، خاستگاه نامعلوم» و این واژه در فهرست واتکینز زیر هیچ ریشه‌ای نیست و گمان رایج آن است که از اسکاندیناوی آمده — نادرست. بنا بر قاعدهٔ «بدترین حکم برای جعبهٔ آمیخته»، این گره به سبب همین یک واژه «رد‌شده» علامت می‌خورد.\",\n     \"sources\": [\"https://www.etymonline.com/word/pocket\"],\n     \"ref_check\": [\n      {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n       \"note\": \"The chart gives this box no reference; it inherits AHD from its parent (node #5). Checked against Watkins 1985 s.v. beu-1 and against Klein, word by word — see consulted.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. beu-1 (AHD_watkins1985.txt line 321) and word index (lines 1309-1326)\", \"stance\": \"partial\",\n       \"note\": \"Watkins has BOSOM, BOAST1, BUCKBOARD (OE būc), BOIL2 and PUFF under beu-1, but neither BIG nor BUD; the index shows \\\"BOSOM beu-1 ... BOAST! beu-1\\\" and no entry for BIG at all.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.vv. bosom (p. 190), big (p. 180), bud (p. 216), boast (p. 190), bucket (p. 216)\", \"stance\": \"partial\",\n       \"note\": \"\\\"bosom, n. — ME., fr. OE. bōsm ... of uncertain etymology\\\"; \\\"big, adj. — ME. bigge, big, of uncertain origin\\\"; \\\"bud, n. — ME. budde ... fr. I.-E. base *b(h)u-, 'to swell'. See buccal\\\"; \\\"boast ... fr. Teut. base *baus-, which lit. means 'to blow up, puff up, swell' ... an enlarged form of I.-E. *bhāu-, *bhu-\\\"; \\\"bucket, n. — ME., fr. AF. buket, dimin. formed fr. OE. būc, 'body, belly, pitcher'\\\".\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II pp. 114ff.\", \"stance\": \"partial\",\n       \"note\": \"The Germanic material collected under the 'swell' root covers the pocca/pohha/Beutel group and got. ufbauljan / ahd. pūlla / ags. bȳle 'Beule', but neither 'big' nor 'bosom' appears there.\"}\n     ]\n    },\n    {\n     \"id\": 10, \"lang\": \"Latin\", \"words\": \"bulla; bulca\", \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"BULLA is correct and well referenced: Watkins beu-1 III.1, \\\"Latin bulla, bubble, round object, amulet (> Old French boule and Spanish bola, ball): BILL1, BILLET1, BOLA, BOULE2, BOWL3, (BULL2), BULLA, BULLATE, BULLET, (BULLETIN)\\\"; Klein s.v. bull 'edict': \\\"fr. L. bulla, 'bubble, boss, knob', fr. I.-E. *bu-l-, whence also Lith. bulė, bulis, 'buttock', MDu. puyl, 'bag' ... I.-E. *bu-l- is an -l-enlargement of base *bu-, 'to blow; to swell'\\\"; Walde-Pokorny II: \\\"Erweiterungen mit l sind vielleicht ai. buliḥ, lit. bulis, lat. bulla u. dgl.\\\" BULCA, however, is not a Latin word — no such form exists in any Latin dictionary. The intended word is plainly bucca '(inflated) cheek', which is exactly what Watkins has at beu-1 III.3 (\\\"Possibly Latin bucca (> Old French boucle, buckle, curl, and Spanish boca, mouth), (inflated) cheek: ... BUCKLE1\\\") and Klein at buccal (\\\"L. bucca, 'cheek', from the I.-E. imitative base *bu-, 'to blow; to swell'\\\"), and it is the only source of 'buckle' in the child node #11. I rendered PDF page 78 at 600 dpi and read the box directly: the printed page really does show \\\"bulca : inflated\\\", so the extraction is faithful and the error is the author's own misprint (l for c). Page image kept at data/verification/sources/refs/ocr/BOOK/78.png.\",\n     \"derivation_fa\": \"«bulla» درست است و مأخذ دارد: واتکینز ذیل beu-1 بخش III.1 «لاتین bulla ‹حباب، چیز گِرد، تعویذ›» را می‌آورد و از آن BULLET و BOWL و BULLETIN را می‌گیرد؛ کلاین ذیل bull «فرمان پاپ» می‌نویسد «از لاتین bulla ‹حباب، برجستگی، دکمه›، از *bu-l- هندواروپایی ... که گسترشی با l از ریشهٔ *bu- ‹دمیدن، آماسیدن› است»؛ والده-پوکورنی نیز «گسترش‌های با l شاید ai. buliḥ و lit. bulis و lat. bulla باشند» دارد. اما «bulca» واژهٔ لاتینی نیست و چنین صورتی در هیچ فرهنگ لاتینی نیامده است. آنچه مقصود بوده آشکارا bucca «گونهٔ باد‌کرده» است؛ همان که واتکینز در بخش III.3 آورده («شاید لاتین bucca ‹گونهٔ باد‌کرده› > BUCKLE») و کلاین ذیل buccal («لاتین bucca ‹گونه›، از پایهٔ تقلیدی *bu- ‹دمیدن، آماسیدن›»)، و تنها همین واژه است که «buckle» در گرهٔ فرزند (۱۱) را توضیح می‌دهد. صفحهٔ ۷۸ نسخهٔ پی‌دی‌اف را با تفکیک ۶۰۰ نقطه بر اینچ برگرداندم و جعبه را مستقیم خواندم: در چاپ کتاب هم «bulca : inflated» آمده است. پس این خطای چاپی کتاب است نه خطای خوانش اسکن؛ داده درست استخراج شده است.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"bulca\",\n     \"correct_form\": \"bucca\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\",\n       \"note\": \"Watkins 1985 s.v. beu-1 III: \\\"1. Latin bulla, bubble, round object, amulet ... 2. Latin bullire (> French bouiller), to bubble, boil ... 3. Possibly Latin bucca (> Old French boucle, buckle, curl, and Spanish boca, mouth), (inflated) cheek: BOCACCIO, BOUCLE, BUCCAL, BUCKLE1, BUCKLE2; DEBOUCH, DISEMBOGUE, EMBOUCHURE.\\\" The reference supports bulla exactly and supports 'bucca : (inflated)' — but there is no 'bulca' in it.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.vv. bull 'edict' (p. 216) and buccal (p. 216) (KLN_1966.txt lines 5832, 5759)\", \"stance\": \"partial\",\n       \"note\": \"\\\"L. bulla, 'bubble, boss, knob', fr. I.-E. *bu-l- ... an -l-enlargement of base *bu-, 'to blow; to swell', whence L. bucca, 'cheek'\\\" — Klein has bulla and bucca side by side and no bulca.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet p. 138 (LAT.txt leaf 156)\", \"stance\": \"partial\",\n       \"note\": \"The same page Nourai cites for būcina carries the long bucca article (\\\"buccula ... bucco, -onis m. ... Mot expressif, sans correspondant hors du latin\\\") — bucca is real Latin, bulca is not.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II (WLD_Bd2_pages.txt line 7503)\", \"stance\": \"supports\",\n       \"note\": \"\\\"Erweiterungen mit l sind vielleicht ai. buliḥ, lit. bulis, lat. bulla u. dgl.\\\" — bulla under the 'swell' root, as drawn.\"}\n     ]\n    },\n    {\n     \"id\": 11, \"lang\": \"English\", \"words\": \"bullet, bowl, boil, bully, bullion, buckle\", \"verdict\": \"confirmed\",\n     \"derivation\": \"All six are assigned to this root by Nourai's parent reference, and by three different routes out of the Latin node. From bulla: BULLET (French boulette, diminutive of boule < bulla) and BOWL in its 'ball' sense (French boule; the eating-bowl BOWL1 is a different word, from Germanic *bul- under bhel-). From the derived verb bullire 'to bubble, boil': BOIL1 (Old French boillir), BULLION (Anglo-French bullion 'melting-house, mint' from the boiling of metal) and BULLY2 in the American 'first-rate, bully for you' sense that Watkins files here. From bucca '(inflated) cheek': BUCKLE1, through Old French boucle 'boss of a shield, ring' < Latin buccula, the diminutive of bucca, used of the cheek-piece of a helmet and then of the shield-boss and the ring of a strap. Watkins's beu-1 III lists exactly BILL1, BOLA, BOULE2, BOWL3, BULLA, BULLET, BULLETIN, BOIL1, BOUILLON, BULLION, BULLY2 and BUCKLE1; Klein agrees at bull 'edict' and buccal. The only nuance is that buckle comes from the mis-set 'bulca' = bucca of node #10 rather than from bulla.\",\n     \"derivation_fa\": \"هر شش واژه با پشتوانهٔ همان مأخذی که در جعبهٔ مادر آمده به این ریشه بازمی‌گردند، از سه راه جداگانه. از bulla: bullet (فرانسوی boulette، مصغّرِ boule از bulla) و bowl به معنای «گوی» (فرانسوی boule؛ bowl به معنای «کاسه» واژهٔ دیگری است از ژرمنی *bul- زیر ریشهٔ bhel-). از فعل مشتق bullire «جوشیدن»: boil (فرانسهٔ کهن boillir)، bullion (آنگلو-فرانسوی bullion «کارگاه گداختن، ضرابخانه»، از جوشاندن فلز) و bully در معنای امریکایی «عالی، آفرین» که واتکینز همین‌جا می‌نشاند. از bucca «گونهٔ باد‌کرده»: buckle از boucle فرانسهٔ کهن «برجستگی سپر، حلقه» از buccula لاتین، مصغّرِ bucca، که نخست گونه‌بندِ کلاه‌خود و سپس ناف سپر و حلقهٔ تسمه را می‌نامید. واتکینز در بخش III دقیقاً همین فهرست را دارد و کلاین نیز در دو مدخل bull و buccal همین را می‌گوید. تنها نکته آنکه buckle از همان صورت نادرست‌چاپ‌شدهٔ «bulca» (= bucca) در گرهٔ ۱۰ می‌آید نه از bulla. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n       \"note\": \"No reference on this box; it inherits AHD from node #10. Watkins 1985 s.v. beu-1 III names BULLET, BOWL3, BOIL1, BULLY2, BULLION and BUCKLE1 explicitly, so the inherited citation carries it.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. beu-1 III and word index (lines 1311-1326)\", \"stance\": \"supports\",\n       \"note\": \"\\\"1. Latin bulla ... BOWL3, (BULL2), BULLA, BULLATE, BULLET, (BULLETIN) ... 2. Latin bullire ... BOIL1, BOUILLON, BUDGE1, (BULLION), BULLY2 ... 3. Possibly Latin bucca ... BUCKLE1, BUCKLE2\\\"; the index confirms \\\"BOIL2 beu-1\\\", \\\"BOWL2 beu-1\\\", \\\"BULLET beu-1\\\", \\\"BULLION beu-1\\\", \\\"BUCKLE1 beu-1\\\".\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. bull 'edict' (p. 216) and bill 'document' (p. 180)\", \"stance\": \"supports\",\n       \"note\": \"\\\"bull, n., an edict of the pope. — ME. bulle, fr. OF. bulle, fr. It. bulla, fr. ML. bulla ... fr. L. bulla, 'bubble, boss, knob', fr. I.-E. *bu-l- ... Cp. bill, 'document', bullet, bulletin\\\", and at bill: \\\"an -l-enlargement of the I.-E. imitative base *bu-, 'to blow; to swell'. See buccal and cp. billet, 'note', boil, v., bolas, boule, 'a game', budge, bulb, bull, 'edict', bullet, bulletin.\\\"\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-78.json','w',encoding='utf-8') as f:\n    json.dump(doc,f,ensure_ascii=False,indent=1)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk78.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-78.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 78",
 "description": "Write and validate page-78 verification"
}
```


### [2026-09-05T06:19:13.967Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 17/17
node verdicts: {'confirmed': 9, 'disputed': 5, 'plausible': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 10, 'contradicts': 2, 'not_checked': 5, 'not_found': 1, 'partial': 2}
books consulted: {'supports': 23, 'silent': 8, 'contradicts': 10, 'partial': 10} | by book: {'KLN': 8, 'WLD': 6, 'WIKT': 6, 'AHD': 5, 'MON': 4, 'ETYMONLINE': 4, 'BQT': 2, 'PHD': 2, 'ARY': 2, 'HRN': 2, 'SKT': 2, 'LEW': 2, 'BRT': 1, 'NYB': 1, 'AFA': 1, 'TAD': 1, 'AFM': 1, 'LAT': 1}
```


## [2026-09-05T06:19:36.769Z] AGENT

Done. `verify_check.py 78` reports 0 PROBLEM lines, 17/17 nodes.

**Page 78 (book p. 48) — 2 entries (Beu 1, Beu 2) + 2 redirects skipped**

Verdicts: roots 2 confirmed · nodes 9 confirmed, 2 plausible, 5 disputed, 1 transcription_suspect.

Disputed / flagged:
- **Beu 1 #2 بوتیمار** — Nourai's own ref (Mann IEC:116) does list "Per. bū timār 'heron'" under IE *bhū- 'howl', but the word is بو (< Ar. أبو "father of") + تیمار "grief"; Borhan p. 313 itself glosses it as غم‌خورک, the bird that grieves the water will dry up.
- **Beu 1 #3 Pahlavi būm "owl"** — not attested. MacKenzie has būf/*būg "owl" and būm "land"; Nyberg, Aryanpur (p. 136: Pahlavi BUF, BUFG, BUG) and Horn §237/238 all agree. MON:606 gives no Pahlavi form and tags بوم "owl" as Arabic.
- **Beu 2 #1 Latin būcina** — Nourai's own ref contradicts him: Ernout-Meillet p. 138 "sans doute composé de bou- et -cana"; Wiktionary same; Walde-Pokorny leaves the onomatopoeic option open but files it under Beu **1**, and Watkins' beu-1 has no būcina.
- **Beu 2 #7 پاکت** — from French *paquet* (Wiktionary; Mo'in [فر.]; Dehkhoda "از اصل فرانسوی پاکه، بسته"), not from poche/pocket; *paquet* < MDu. *pak*, a separate etymon from *puk-.
- **Beu 2 #9 English box** — bud, boast, bucket, puff confirmed; bosom only partial (Klein: "of uncertain etymology"); **big** is "of uncertain origin" (Klein, absent from Watkins) → worst-word rule.
- **Beu 2 #10 "bulca : inflated"** (transcription_suspect) — `error_in: book`. The 600-dpi render of PDF p. 78 shows *bulca* in print, so the extraction is faithful; the intended word is Latin **bucca** "(inflated) cheek" (AHD beu-1 III.3, Klein s.v. buccal), which is what actually yields "buckle" in node #11.

Good confirmations: BQT:318 is exactly right — Mo'in's footnote 6 there reads «از عربی، از لاتینی buccina»; AFA:284 supplies the Syriac būqīnā link; KLN:176 and 213 are both exact pages (bittern / Buteo-buzzard).

**No extraction errors** — every box, script form, gloss and the بوم couplet match the printed page.

Artifacts written: `data/verification/page-78.json`; page image `sources/refs/ocr/BOOK/78.png`; Aryanpur transcription `sources/refs/ocr/ARY/0136.vision.txt`; 8 web pages archived via `fetch_source.py`.
