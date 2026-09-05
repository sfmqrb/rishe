# Verification process log — verify-page-169


## [2026-09-05T20:37:11.483Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 169 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-169.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-169.json. Write /home/sfmqrb/git/rishe/data/verification/page-169.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 169` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:37:13.093Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:37:13.795Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:37:13.809Z] TOOL RESULT

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


## [2026-09-05T20:37:14.168Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-169.txt"
}
```


### [2026-09-05T20:37:14.207Z] TOOL RESULT

```
1	=== PDF page 169 (book page 139) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gel, Geli, Gelu, Glue, Geleb, Gelu : to form into a ball, stick together  (refs POK:357-364, SYN:908; IEC:303)
4	#1 (parent #0) [Persian] refs=IEC:303 | gŭy «گوی» : ball, also competition in any game
5	#2 (parent #0) [Sanskrit] refs=POK:357, 361 | glâv, gula, glâu-h : parcel, ball
6	  #3 (parent #2) [Persian] refs=POK:361; MON:3382; BQT:1861 | gulleh «گولّه» : ball, bullet ; goluleh «گلوله» : bullet
7	#4 (parent #0) [Latin] refs=AHD; | globus : ball ; gluten : glue
8	  #5 (parent #4) [French] refs=None | globule
9	    #6 (parent #5) [Persian] refs=MON:3363 | golobŭl «گلبول» : globule
10	  #7 (parent #4) [English] refs=AHD | globe, globule, glue
11	#8 (parent #0) [Germanic] refs=AHD | klukjan : to clutch
12	  #9 (parent #8) [English] refs=AHD | clutch
13	    #10 (parent #9) [Persian] refs=MON:3015 | kelâč «کلاچ» : clutch
14	#11 (parent #0) [Germanic] refs=AHD | klub : a lump or group
15	  #12 (parent #11) [French] refs=None | club
16	    #13 (parent #12) [Persian] refs=MON:3039 | klub «کلوب» : a club or association
17	  #14 (parent #11) [English] refs=None | club
18	#15 (parent #0) [Germanic] refs=AHD | kling : to cling ; klimban : to hold on, climb ; klŭd : , a hill, rock, cloud ; klamp, klump, klut : a wooden shoe, clumsy person ; klaijo : sticky mud
19	  #16 (parent #15) [English] refs=None | cling, climb, cloud, clamp, clumsy, clown, clay
20	--- entry 1 ---
21	ROOT Geleb -> redirect to Gel
22	--- entry 2 ---
23	ROOT Geli -> redirect to Gel
24	--- entry 3 ---
25	ROOT Gelu -> redirect to Gel
26	--- entry 4 ---
27	ROOT Gelu -> redirect to Gel
28	--- entry 5 ---
29	ROOT Gem -> redirect to Geme
30	
```


## [2026-09-05T20:37:16.969Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-169.json | head -150",
 "description": "Read source JSON for page 169"
}
```


## [2026-09-05T20:37:17.608Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:37:20.292Z] TOOL RESULT

```
{
    "pdf_page": 169,
    "book_page": 139,
    "entries": [
        {
            "root": {
                "name": "Gel, Geli, Gelu, Glue, Geleb, Gelu",
                "lang": "Indo-European",
                "refs": "POK:357-364, SYN:908; IEC:303",
                "gloss": "to form into a ball, stick together"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Persian",
                    "refs": "IEC:303",
                    "words": [
                        {
                            "translit": "g\u016dy",
                            "gloss": "ball, also competition in any game",
                            "script": "\u06af\u0648\u06cc"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": {
                        "text": "\u062d\u0627\u0641\u0638 \u0628\u0628\u0631 \u062a\u0648 \u06af\u0648\u06cc \u0641\u0635\u0627\u062d\u062a \u06a9\u0647 \u0645\u062f\u0639\u06cc - \u0647\u06cc\u0686\u0634 \u0647\u0646\u0631 \u0646\u0628\u0648\u062f \u0648 \u062e\u0628\u0631 \u0646\u06cc\u0632 \u0647\u0645 \u0646\u062f\u0627\u0634\u062a",
                        "poet": "H\u00e2fez"
                    }
                },
                {
                    "id": 2,
                    "parent": 0,
                    "lang": "Sanskrit",
                    "refs": "POK:357, 361",
                    "words": [
                        {
                            "translit": "gl\u00e2v, gula, gl\u00e2u-h",
                            "gloss": "parcel, ball",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "Persian",
                    "refs": "POK:361; MON:3382; BQT:1861",
                    "words": [
                        {
                            "translit": "gulleh",
                            "gloss": "ball, bullet",
                            "script": "\u06af\u0648\u0644\u0651\u0647"
                        },
                        {
                            "translit": "goluleh",
                            "gloss": "bullet",
                            "script": "\u06af\u0644\u0648\u0644\u0647"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "AHD;",
                    "words": [
                        {
                            "translit": "globus",
                            "gloss": "ball",
                            "script": null
                        },
                        {
                            "translit": "gluten",
                            "gloss": "glue",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "French",
                    "refs": null,
                    "words": [
                        {
                            "translit": "globule",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 5,
                    "lang": "Persian",
                    "refs": "MON:3363",
                    "words": [
                        {
                            "translit": "golob\u016dl",
                            "gloss": "globule",
                            "script": "\u06af\u0644\u0628\u0648\u0644"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 4,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "globe, globule, glue",
                            "gloss": null,
                            "script": null
                        }
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
                        {
                            "translit": "klukjan",
                            "gloss": "to clutch",
                            "script": null
                        }
                    ],
                    "script_extra": null,
```


### [2026-09-05T20:37:20.323Z] TOOL RESULT

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


## [2026-09-05T20:37:25.105Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-169.json | sed -n '150,400p'",
 "description": "Rest of source JSON"
}
```


### [2026-09-05T20:37:26.856Z] TOOL RESULT

```
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 8,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "clutch",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 10,
                    "parent": 9,
                    "lang": "Persian",
                    "refs": "MON:3015",
                    "words": [
                        {
                            "translit": "kel\u00e2\u010d",
                            "gloss": "clutch",
                            "script": "\u06a9\u0644\u0627\u0686"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 11,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "klub",
                            "gloss": "a lump or group",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 12,
                    "parent": 11,
                    "lang": "French",
                    "refs": null,
                    "words": [
                        {
                            "translit": "club",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 13,
                    "parent": 12,
                    "lang": "Persian",
                    "refs": "MON:3039",
                    "words": [
                        {
                            "translit": "klub",
                            "gloss": "a club or association",
                            "script": "\u06a9\u0644\u0648\u0628"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 14,
                    "parent": 11,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "club",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 15,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "kling",
                            "gloss": "to cling",
                            "script": null
                        },
                        {
                            "translit": "klimban",
                            "gloss": "to hold on, climb",
                            "script": null
                        },
                        {
                            "translit": "kl\u016dd",
                            "gloss": ", a hill, rock, cloud",
                            "script": null
                        },
                        {
                            "translit": "klamp, klump, klut",
                            "gloss": "a wooden shoe, clumsy person",
                            "script": null
                        },
                        {
                            "translit": "klaijo",
                            "gloss": "sticky mud",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 16,
                    "parent": 15,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "cling, climb, cloud, clamp, clumsy, clown, clay",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Geleb",
                "redirect": "Gel"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Geli",
                "redirect": "Gel"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Gelu",
                "redirect": "Gel"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Gelu",
                "redirect": "Gel"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Gem",
                "redirect": "Geme"
            },
            "nodes": []
        }
    ]
}
```


## [2026-09-05T20:37:27.205Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','IEC','AHD','MON','BQT','KLN','SKT','LEW','LAT','WLD','ARY','WEB','FSD']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600]); print()\n\"",
 "description": "Ref metadata"
}
```


### [2026-09-05T20:37:28.951Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
```


## [2026-09-05T20:37:33.857Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 357 361 362 364; do echo \"=== POK p.$p (leaf $((p+8))) ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((p+8))\"'' POK_01.txt | head -60; done",
 "description": "Pokorny pages 357-364"
}
```


### [2026-09-05T20:37:35.736Z] TOOL RESULT

```
=== POK p.357 (leaf 365) ===
=== POK p.361 (leaf 369) ===
=== POK p.362 (leaf 370) ===
=== POK p.364 (leaf 372) ===
```


## [2026-09-05T20:37:38.535Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la POK*  && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"$f: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f) pages, $(wc -c <$f) bytes\"; done",
 "description": "Inspect POK files"
}
```


### [2026-09-05T20:37:40.238Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
POK_01.txt: 363 pages, 981836 bytes
POK_02.txt: 433 pages, 1137861 bytes
POK_03.txt: 429 pages, 1170809 bytes
POK_full.txt: 1 pages, 3971883 bytes
```


## [2026-09-05T20:37:44.668Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 357 358; do echo \"=== POK p.$p (leaf $((p-344))) ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((p-344))\"'' POK_02.txt; done",
 "description": "Pokorny p.357-358"
}
```


### [2026-09-05T20:37:46.277Z] TOOL RESULT

```
=== POK p.357 (leaf 13) ===
teinchen',  nnd.  keiserling,  keserling,  kiserling  ds.;
apr.   sixdo  f.   ,Sand',   lit.   Hezdrä   ,Kies,   Korn',   ziezdros    ,Eaes,   grober Sand',  ziegzdros  ds.,  auch  m.  Hegzdrai.
Fragwürdig   die   Zugehörigkeit  des   angeblich  phryg.  ylaaa  , Stein'  bei Steph.  Byz.  s.  v.  Movoyiaaa. WP.  I  553.
357
gel-  ,ballen,  sich  ballen;  Gerundetes,  Kugeliges'  usw.
Belege  für  die  unerweiterte  Wurzelform  sind  selten  und  z.  T.  sehr unsicher:
Ai.  gula-h,  gull  (Lex.),  gulikä  , Kugel,  Ball,  Perle',  gülma-  m.,  n.  ,Ge- schwulst,  Busch'  (zum  -ul-  vor  Kons.  s.  Wackernagel  Ai.  Gr.  I  30);  mit 7z-Suffix  ai.  gunikä  (Lex.)  »Geschwulst';
gr.  redupl.  yayyXLov  n.  , Geschwulst,  Überbein' ;
lat.  galla  f.  , Gallapfel'  als  ,kugeliger  Auswuchs'  aus  *gj,-nä  oder  "^gol-na^ daraus   entlehnt   ags.  gealla,  geallocy  nhd.  ,GallajpfeV]
alb.  gogele  , Kugel,  Ball;  Gallapfel'  (*gel-gal-na)]
älter  hoU.  kal  ,Kern  in  Äpfeln  und  Birnen';  schwed.  dial.  kalm  , Stein- haufen' ;
aksl.  hly  (zely)  , Geschwür*,  bulg.  zelka  , Drüse,  Geschwulst',  russ.  zolvb^ zolvüj,  zelvak  , Beule',  cech.  zluna,  zluva  , Geschwulst',  klr.  ^old  , Erdnuß, Erdeichel' ;  poln.  glen,  glon  , Klumpen,  Stück  Brot'.
A.  Gutturalerweiterungen:
gel-g'\
Gr.  yeXyiQ  f..  Gen.  yelyid-og  (auch  yelytog  und  -löog),  PL  yslyeig  ,Knob- lauchkern'  (wenn  nicht  wegen  Hyllg,  -id-og  ,Knoblauchkopf*  ==  ^ä-yll-S"- ,aus  TeilknöUchen,  Zehen  zusammengesetzt'  aus  redupl.  ^ysl-ylid-  dissi- miliert; doch  vgl.  auch:)  2ii.  grnja-h,  gxfijana-h  , Art  Knoblauch',  vielleicht auch  gr.  yelyrj  PL  , Trödelwaren'  (wenn  etwa  , Rundwaren,  Knöllchen', vgl.  nhd.  Kurziuaren)]
schwed.  kalk  ,Mark  im  Holz'  (,Markkügelchen'),  mengl.  kelkes  ,ova  of fishes',  colk,  colke  , Apfelkern'.
Die  folgenden  nur  germ.  (und  kelt. ?)  Wortgruppen  (idg.  gleg-,  glog-?) mit  ihren  expressiven  Verschärfungen  und  Nasalierungen  machen  keinen idg.  Eindruck,  so
glek-  in  anord.  kleggi  (*klagjan-)  , Heuhaufen',  nasaliert  nhd.  mdartl. (siebenbg.)  heu-kling,  klang  , Heuhaufen^,  klang,  klinge  , kiesige  seichte  Stelle im  Fluß;  Sandbank';  ags.  clingan  _,sich  zusammenziehen,  einschrumpfen', engl,  ding  ,sich  anklammern,  festhalten;  haften',  anord.  klengiask  ,auf jemand  eindringen^  (,*sich  anklammern'),  mhd.  klingen  , klettern'  (mit Kons.-Schärfung  nhd.  dial.  klinken  ,sich  anklammern'),  ahd.  klinga^  nhd. E2inge  ,enge  Schlucht,  Klamm',  wozu  mit  gramm.  Wechsel  (also  idg. ^^gle-n-k-)  engl,  clough  (=  ags.  *clöh  aus  *klanh-)  ,steile  Klamm',  ahd. Cläh-uelde]  ahd.  klunga  ,
=== POK p.358 (leaf 14) ===
 Knäuel',  Demin.  klungilin,  nhd.  Klüngel  ds., schwed.  klunga  ,gedräagter  Haufen,  Masse'^,  klänga  ,klettern',  anord. klungr  (*klung-ra-,  -ru-)  , Dornbusch,  Hagebutte';
mit  germ.  -k-  (z.  T.  idg.  g,  z.  T.  germ.  Kons.-Schärfung)  anord.  klaki  ,ge- frorene  Erdkruste',  klakkr  , Klumpen,  Wollklumpen,   Klecks,  Wölkchen',
358
mhd.  klah  ,Fleck,  Klecks^;   a-s.  clyccan   ,packen,  greifen'   (engl,  dutchl      1 zu  afries.  Uetsie  ,Spieß^  schwed.  hlyka  {mykja)  ,Klammer,  GabeP;
dazu  (?)  das  auf  urkelt.  hh  weisende  mir.  glacc,  nir.  glac  ,Hand', glacaim  , erfasse^;
nasaliert  norw.  dial.  klank  und  Munk  .Klumpen^  mhd.  klungeler  l Troddel^  glunkern  , baumeln',  nhd.  Klunker  ,Kotklümpchen,  Schleim, klümpchen,  Augenbutter'  (ist  aus  ähnlicher  Bed.  des  Unreinlichen  vielleicht auch  anord.  klceki  n.  ,Schmach,  Schande',  ags.  clacn  ^Beleidigung'  geflossen?);
ndd.  klinken  ,m  Falten  legen,  einschrumpfen',  klinksucht  ,Schwindsuchf,    | mhd.  klinke  ,Türklinke',  ahd.  klenken  (^klankjan)  ,schnüren,  binden',  ags.     ^ he-clencan  ,festhalten',  engl,  clench,  clinch   ,(die  Faust)  ballen;    umfassen; nieten',  mhd.  klank  ,Schlinge;  List,  Ränke'.
Auf  idg.  gleg'  weisen  jedoch  wohl  russ.  ksl.  glez-m,  -na,  -no  ,Knöchel*, poln.  glozna  ds.  und  dehnstufig  russ.  glazokz  ,Kügelchen',  glaz^  ,Auge', poln.  giaz  ,Stein,  Fels ;  Steinchen',  g^azny  ,glatt,  geschickt'  (vgl.  Berneker 301  m.  Lit.,  Persson  Beitr.  792);
Zupitza  (KZ.  36,  236)  stellt  mhd.  kluoc{-g)  ,klug,  schlau,  höflich,  zierlich' (germ.  ^^klöza-),  mnd.  klök  (germ.  *klöka-)   yklug,  listig,   gewandt'  zu  air. glicc  (nir.  glic  erweist  urkelt..  ä:ä;)  ,sapiens';   ursprüngl.   ,wie   eine  Kugel so  glatt  und  so  beweglich'?? B.  Dentalerweiterungen:
gel-t-:  zunächst  (als  , Anschwellung  —  Mutterleib  — fetus',  wie  unten bei  Kalb,  kilhurra):  2a.  jathdram  ,Bauch',  jartü-  ,Gebärmutter';  allenfalls  ai. gutikä  ,Kügelchen,  Pille,  Perle,  Trinkbecher'  (eher  dial.  aus  gudikä  ds.);
got.  kilpei  f.  ,Mutterleib',  in-kilpö  ,sch wanger',  ags.  cild  n.  ,Kind',  engl.
child
MikkolaBB.21, 225  verbindet  auch  scheinbar  schwundstuf,  schwed.  kolla^ kulla  ,Mädchen;  Weibchen  bei  einigen  Tieren'  {*kulp-)  mit  kilpei)  über aschwed.  kolder  , Kinder  aus  einer  Ehe'  s.  Liden  IF.  19,  335  und  Wz.gol;
*gle-t-  vielleicht  in  ksl.  glota  ,turba',  serb.  glota  ,Familie  (Weib  und Kinder);  arme  Leute;  Unkraut;  Unsauberkeit,  Schmutz'?
Wegen  der  Unsicherheit  des  ai.  Beispiels  sind  die  folgenden,  nur  im Germ,  sicher  belegten  Wortgruppen  (idg.  "^gel-d-,  "^gle-d-"})  nichtidg.  Herkunft verdächtig :
mit  der  Bed.  des  Tierjungen  ai.  gadi-h,  gali-h  ,junger  Stier' (V);
dazu  tiefstufig  ags.  coli  ,Junges  von  Tieren',  engl,  coli  ,Füllen
```


## [2026-09-05T20:37:53.466Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 359 360 361; do echo \"=== POK p.$p ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((p-344))\"'' POK_02.txt; done",
 "description": "Pokorny p.359-361"
}
```


### [2026-09-05T20:37:55.070Z] TOOL RESULT

```
=== POK p.359 ===
'?;
aisl.  kialta,  kilting  ,Bausch,  bauschige  Falte  des  Kleides',  norw.  dial.^ kult  , Holzstumpf,  Bergknollen,  plumpe  dicke  Figur'  (schwed.  auch  ,halb- erwachsenes  Ferkel',  vgl.  oben  ags.  colt)]
nasaliert  (*glend-)  aschwed.  Hinter  , Berggipfel,  Bergknollen',  aisl.  klettr ,Fels,  Klippe',  mnd.  nnd.  klint  ,Fels,  Klippe',  ndd.  Munt,  klunte  ,Klumpen,
359
Haufen;  dickes  Weib^  =  nhd.  dial.  klunze,  ndd.  Munter  ^Klümpchen  von ^ot  oder  Mist'  (daneben  mit  germ.  d  ndd.  klunder  ,Büschel,  Haufe', Qorw.  klundra  ,Knorren^  Knoten'  u.  dgl.);
westfäl.  klütern  (as.  ^klätirön)  ^klettern'  (eigentlich  ,kleben  oder  sich  fest anklammern'),  ndd.  kläteren,  klatteren  ds.,  nnd.  kläter  m.  , festhaftender Schmutz';  mit  ö  mndl.  hoU.  cloet,  kloet  ,Stock;  Ball,  Knauf  des  Schwertes' (spätanord.    klot    , Schwertknauf'    ist   Lw.    aus    mnd.    klöt  =  nhd.    Kloß);
mit  expressivem  -tt-:  mnd.  Matte  , Lappen' =  nhd.  dial.  Matz  , Schmutz- fleck', mndl.  Matten  ,beschmutzen',  mhd.  hekletzen  ds.,  norw.  schwed. mdartl.  klatra  , hudeln';
daneben  mit  expressivem  dd:  ndd.  kladde  , Schmutzfleck ;    Klette'  (d.i. ^die  Klebende^);    mit   Dent,  +  s :  norw.  klessa  (Mass)   ,kleben,  festhäng-en, platschen,  klatschen',  klessa  (Jdeste)  ,schmieren,  sudeln',  klussa  , beschmutzen, sudeln,  lispeln';    aisl.  Mess  , lispelnd';    vgl.  aisl.  klasi  S.  362. C.  Labialerweiterungen:
geleb(h);  gleb(h)-  {:  gl9h{h)-)  und  gleh^h)-  {:  glh{h)')  ,zusamraen- ballen'.
Lat.  (wohl  eigentlich  gall.)  galha  (*g,hhh-'^),  nach  Sueton  gall.  Bezeich- nung für  einen  ,homo  praepinguis';  ein  gall.  *galbo-  , Verdickung,  Wade, Arm'  wird  auch  wohl  vorausgesetzt  von  galheus,  -eum  ,  Armbin  de,  als Schmuck',  vielleicht  von  galbulus  , Zypressenzapfen',  deren  Vokalismus vermutlich  aus  *gjdbh-'^
anord.  kalfi  m.  ,Wade^,  kalfaböt  , Lende',  engl,  calf  ,Wade',  nhd.  mdartl. Kalb  , Muskel',  ahd.  wazzarkalb  , Wassersucht^  (,Aufschwellung  durch Wasser'),  womit  sich  (als  , Anschwellung  —  Mutterleib  —  fetus',  vgl.  engl. in  calf,  with  calf  , trächtig')  deckt  ahd.  kalb,  PL  kelbir  ,Kalb^,  ags.  cealf calfur  n.,  anord.  kalfr  ,Kalb',  got.  kalbö  f.  ,junge  Kuh,  Färse',  mit  e-Stufe ags.   cüfor-lamb ,  ahd.  küburra  f.  , weibliches  Lamm';
lat.  globus  m.  , Kugel,  Haufe,  Klumpen',  dehnstufig  lat.  gleba  f.  , Erd- scholle;  Stückchen,  Klümpchen'  (daraus  poln.  gleba  , Erdscholle'  entlehnt).
Ist  ^^e6ö  ,rusticus'  (,Schollen  aufwerfend'??)  gallisch  (dann  e)  oder  nur im  Latein  Galliens  aufgekommen?
Ahd.  kläftra  f.  ,Maß  der  ausgespannten  Arme,  Klafter''  (*glebh-) ;  ablaut. anord.  Maß  m.  ,Halsjoch,  Packsattel',  mnd.  Mave  , Halsjoch'  (*klaban- , Zusammendrückendes') ;  ags.  clyppan  , umarmen'  {^klupjan  mit  -lu-  als Tiefstufe  von  -le-),  af
=== POK p.360 ===
ries.  Meppa  ds.,  Schweiz,  chlupfel  ,Bündel',  engl. clasp  (*claps-)  ,haken,  spannen,  umfassen,  umarmen'  (wohl  auch  air.  glass , Schloß'  aus  *glabso-)]
vgl.  mit  derselben  Bed.  ,(mit  den  Armen)  zusammendrücken'  und  einem ebenfalls  am  besten  aus  einer  schweren  Wzf.  glebh- :  ghbh-  zu  erklärenden Ablaut   die   halt.  Sippe   von    lit.  gUbiu,  glebti   ,mit  den  Armen   umfassen'
360
{gUhys  .Armvoll,  UmarmungO,  gl<^^^,  9^^^^^  .umarmen,  unterstützen',  lett. gleht,   gldht    ,schützen^    lit.    glahöti    .aufbewahren,    verwahren;    erbitten',, iett.  glabdt  ,hüten,  bewahren,  warten^,  apr.  poglahü  ,herzte'  (Mühlenbach. Endzelin  I  621,  623  u.  626);
vielleicht  dazu  lit.  gelhu,  -eti  ,helfen^,  gühti  ,genesen',  apr.  galbimai 1.  PI.  Konj.  ,wir  helien' ,- pogalbton  ,geholfen' als  *gehbh.  (Trautmann  92);
slav.  *globig,  *globiti  in  serb.  z-globlm,  zglbbiti  ,zusammenlegen,  fügen«, poln.  giobic  alt  , drücken,  zusammenfügen^  (dehnstufig  sloven.  glähim^ gldbiti  ,raffen9  mit  idg.  a  oder  eher  o  (:  lat.  globus).
Ferner  mit  der  Bed.  des  , Geballten,  Runden,  Klotzigen'  germ.  *klapp, (intensive  Konsonantenschärfung)  in  anord.  klgpp  f.  ,Knüppelbrücke',  mnd. klampe  ds.,  schwed.  klapper-sten  , rundliche  Steine  zum  Pflastern',  mhd. klapf  m.  ,Fels(kopfO;
germ.  expressives  *klabb-  in  norw.  dial.  klabb  ,anhaftender  Klumpen', schwed.  klabb  (e)  ,Klotz,  Bergknollen  im  Meer,  kurzer,  dicker  Knabe' (tiefstufig  anord.  klubba  ,Keule',  woher  engl,  club)]
germ.  *klep-  (vgl.  lat.  gUba]  germ.  p  aus  express.  pp  oder  allenfalls einer  Form  mit  idg.  b)  in  anord.  kläp-eygr  ,glotzäugig',  kläpr  ein  Schelt- wort (etwa  ,Klotz')  u.  dgl. ;  über  idg.  qlep-  s.  dort;
tiefstufig  *kulb-  in  ahd.  kolbo  ,Kolben^  Keule  (als  Waffe),  Knüttel', anord.  kolfr  ,Pflanzenknollen,  Pfeil',  kylfi,  kylfa  ,Keule  u.  dgl.';  daneben mit  germ.  -p-  ndd.  kulp-öge  .Glotzauge',  mrhein.  Külp  , Schlagholz  am Dreschflegel',  schwed.  dial.  kulp  , dicker  Mensch';  mengl.  cülpey  nengl. kelp  , Salzkraut'.
Nasaliert   glembb-   (vielleicht  z.  T.  durch   Kreuzung  von    *glebh-  und *glem-) :
Mhd.  klamben  ,fest  zusammenfügen',  anord.  klembra  ,klettern',  aisl.  klgmbr , Klammer',    mhd.    klemberen    ,verklammern',    mhd.    nhd.   Klammer'^    engl." clamber  .klettern',  eigentlich   ,sich  festklammern',   wie   auch   ablaut.   ahd. klimban  ,kliramen.  klettern',  ags.  climban,  mhd.  klimben,  klimmen  , klimmen, klettern;  zwicken,  packen';  anord.  klumba  , Keule',  klumbu-fötr  .Klumpfuß';
mit  germ.  p :  aschwed.  klimper  .Klumpen,  Kloß',  aisl.  kleppr  ,Klumpeny felsige  Anhöhe',  m
=== POK p.361 ===
hd.  klimpfen  .fest  zusammendrücken';  ahd.  klampfer .Klammer',  mnd.  klampe  f.  ,Haken.  Steg',  nnd.  klamp,  klampe  ,Klumpen^ Klotz'  (nhd.  Klampe  .Klammer.  Haken,  Klotz'  ist  ndd.  Lw.,  echt  nhd. Klampfe) ;  ags.  clympe  .Klumpen',  ndd.  klumpe  , Klumpen'  (nhd.  Klumpe{n) ist  ndd.  Lw.);
poln.  glqbj  cech.  hloub  , Strunk'.
glem- :
Lat.  glomus,  -eris  n.  ,Kloß  (als  Speise);  Knäuel'  {*glemos),  glomeräre , ballen';
361
air.  glomar  ^Zaum,  Knebel'  (vgl.  S.  360  mhd.  klammer)]
ao-s.  climman  ^klettern',  mnd.  klimmer en  ds.,  mhd.  klimmen  (z.  T.  mit m'ni  aus  mh),  auch  ,beeng-en'  (nhd.  beklommen),  ags.  clam(m)  ,Band,  Griff, Fessel';  ahd.  Mamma  , Beengung,  Klemme,  Bergschlucht',  nhd.  Klamm^ l^aus.  ahd.  nhd.  klemmen,  afries.  klemma,  ags.  heclemman  , einklemmen',  mhd. ]clam  ^enge,  dicht*",  nhd.  (nd.)  klamm  ,steif  (krampfig)  vor  Kälte',  tiefstufig jjorw.  dial.  klumra  ,mit  steifen  und  erfrorenen  Händen  arbeiten';
mit  erweit.  *klam-d-:  anord.  klanda,  klandra  ,verunglimpfen,  ärgern, 2U  entwenden  suchen';
lit.  glomö-ju^  -ti  , umarmen';  mit  -g-  erweitert  lit.  glemziil,  glemzti  ,zu- sammenraffen ;  zerknittern',  lett.  glemzt  ,langsam  essen,  Unsinn  schwatzen';
ferner  glem-,  glom-  mit  alter  Bed.-Entw.  zu  ,zusammenkleben, schleimige  Masse':
gr.  yXcc(^üJv  ,triefäugig',  usw.  (lat.  glamae  Lw.) ;
alb.  nglome,  ngjome  , feucht,  frisch'  (*glemo-) ;
anord.  kläm  , Schmutzrede',  engl,  clammy  ,klebrig,  zäh',  ostpr.  klamiri ,klebrig,  feucht';
lit.  glemes,  glemes,  glemos  f.  pl.  ,zäher  Schleim',  lett.  gl^^mas,  glemi  , Schleim', gliimt  , schleimig,  glatt  werden',  glums  ,glatt'  (auch  glemzt  , gedankenlos plaudern',  glemza  , Schwätzer',  vgl.  z.  Bed.  lett.  gleists  , Schwätzer' :  glist ,schleimig  werden');  über  lit.  gleimes  s.  unten  S.  364.
D.  g(e)l-eu-,  z.  T.  mit  weiterer  konsonantischer  Ableitung:
Ai.  gläu-h  f.  ,Ballen,  Kugel,  geballte  Masse'^,  npers.  gulüle  ,Kugel';
gr.  yly-yXv-fiog  m.  ,Knochengelenk,  Türangel';
air.  glö'Sndthe,  gldo-sndthe  ,linea,  norma'  (wörtlich  ,Ballendraht');
anord.  kle  m.  (^kleio-an-)  ,Webstein',  ags.  clyne  n.  ,Metallklumpen' (*klu-n-),  schwed.  kluns  m.  , Klumpen',  isl.  klunni  ,klotzige  Person';  ahd. kliuwa,  kliwa  , Kugel,  Knäuel',  kliuwi,  kliwi  ,Knäuel'  (Demin.  mhd.  kliu- welln,  dissimiliert  nhd.  Knäuel),  ags.  cliewen  ,Garnknäuel'  (engl.  clew)\ tiefstufig  mnd.  klüwen,  holl.  kluwen  ,Knäuel';  dazu  mit  Dehnstufe  und Bed.-Entw.  ,die  packende  :  Klaue'  die  Sippe  von  germ.  *klewä :  ahd.  kläwa ,Kralle,  Klaue',  mhd.  kläioe,  mnd.  klä  , Kralle,  Klaue,  Huf,  afries.  kle? wozu  mit  Ablaut  das  Verbum  *klawjan  (geneuert  *klawan)  ,mit  den Nägeln  kratzen,  jucken',  ahd.  klauuenti  ,prurientes',  mhd.  kl'öuwen  ,kratzen', ags.  clawan  =  anord.  klä  ,reiben,  k
```


## [2026-09-05T20:38:04.742Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 362 363 364; do echo \"=== POK p.$p ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((p-344))\"'' POK_02.txt; done",
 "description": "Pokorny p.362-364"
}
```


### [2026-09-05T20:38:06.618Z] TOOL RESULT

```
=== POK p.362 ===
ratzen'  (anord.  kläeja  ,jucken'  Neubil- dung nach  der  3.  Sg.  klcär  =  *klawid),  wozu  *klawipan-  m.  in  anord.  klädi  m. ,Jucken,  Kratzen',  ags.  clceweda  ds.,  ahd.  glouuida  (lies  clouuida)  ,scabies' ; aus  dem  Verbum  stammt  die  Kürze  von  ags.  clawu  f.  ,Klaue,  Huf  (engl. claio)  und  clea  f.  (engl,  mdartl.  clea)  ds.  (letzteres  =  *klau  aus  clawu), sowie  ahd.  klöa  ,Klaue';   ahd.  cluwi  , Zange';    aisl.  klö   f.   , Klaue,   Nagel,
362
f
Haken';   aisl.    klunna    ,sich    festhängen^   vgl.    ags.    clyne,    schwed.   kl ,Klumpen',  ags.  clynian  ,ein wickeln S*
wahrscheinlich  air.  glün  ,Knie^  =  alb.  glii-ri  (geg.),  gju-ri  (tosk.)  ^KnißC (mit  idg.  *genu-  ,Kiiie'  kaum  als  Dissimilationsform  für  *gnu-n-  vereinbar weo-en  der  Gutturalverschiedenheit);
vermutlich  lit.  gliaumas  ^schleimiger  Abgang  vom  Schleifstein^^  gliaumii^ ,glatt,  schlüpfrig',  lett.  glaums,  glums  ^schleimig',  wenn  .schleimig  =  ^^^ sammenklebend,  sich  zusammenballend',  vgl.  Mühlenbach-Endzelin  I  622;i vo-1.  mit  -s-  norw.  hlyse  {*klüsion-)  .schleimiger  Klumpen',  das  von  mm klüs  .Masse',  nnd.  .Knäuel.  Wirre.  Masse',  ndd.  Muster  .Büschel.  Traube^]^ ags.  düster j  clyster  n.  ds.  nicht  zu  trennen  ist;  vgl.  von  einer  Wzf.  *^?e-t.' anord.  klasi  .Klumpen  von  Beeren  oder  Früchten.  Masse'.
Erweiterung  mit  -t-:
gr.  yXovTÖg  (zä  ykowd)  .Hinterbacke,  Gesäß',  rä  yXovria  .zwei  Erhaben- heiten des  Gehirns';  'J,
sloven.  glüta,  gluta  ,Beule.  beulenartige  Geschwulst.  Baumknorren'  (Ber-/ neker  309) ;
ablautend  ags.  clüd  m.  .a  mass  of  rock.  hill'.  engl,  cloud  .Wolke' (,Wolkenballen').  vgl.  mit  Geminata  (*kludda-)  ags.  clodd  (engl,  clod) .Erdklumpen'.  ./,'  y
Erweiterung  mit  -d-:
mnd.  klöt  m.  .Klumpen;  Hode'.  mhd.  klöz^  nhd.  Kloß,  ags.  cleot,  engl,  cleat ,Klumpen.  Keil';  ablautend  mnd.  klüt,  Hüte  .Erdklumpen',  ostfries.  klüt .Klumpen,  Bruchstück'  (in  Weiterentwicklung  letzterer  Bed.  auch:)  ags. clüt  m..  engl,  clout  .Lappen;  Metallplatte',  spätanord.  klütr  .Lappen, Klumpen';  mit  expressiver  Geminata  (*klutta-)  ags.  clott  (engl,  cht) .Klumpen'  =  mhd.  kloz,  nhd.  Klotz.
Vielleicht  hierher  lit.  glaudUü,  glausti,  lett.  glaust  .mache  etwas  eng anschmiegen',  glaudüs  .anschmiegend,  dicht  anliegend',  glüdoju  .liege  an- geschmiegt da'  (vgl.  Mühlenbach-Endzelin  I  622 f.);
russ.  gluda  .Klumpen,  Kloß'.
Erweiterung  mit  -bb-:
S
=== POK p.363 ===
ylt,  fries.  klepi  .küssen',  russ.  glyba  ,Klumpen,  Block',  g.  zemli  ,Erd- scholle'  (Berneker  310;  vgl.  zum  -h-  unten  *gle-b-),  vielleicht  lit.  glaubti ,an  die  Brust  drücken',  glaubstyti  ,liebkosen'.
E.  glei-,  z.  T.  mit  weiterer,  konsonantischer  Ableitung  (bes.  glei-t-,  -d-, glei'bb-,  glei-m-)  ,kleben,  schmieren',  aber  wohl  ursprüngl.  abgeleitet von  gel-  ,ballen';  nach  Specht  Dekl.  144  Grundbed.  ,glänzend'  (zu gel-,  gel-?)]  nominal:  gli-io-,  -no-,  -tu-;  gloi-uo-.
363
Gr.  ylla  f.  ^Leim'  (sl.  *ghjb,  s.  unten)^  yXivf]  ds.  (:  sl.  glem,  glina,  ahd. Jclenan,  air.  glenim  s.  unten);  yloiög  ^klebrige  Feuchtigkeit^,  yloiög  ^klebrig, feuchf^  (^yXocJ^ög  :\ett  glievsj  slav.  *glev^,  s.  unten),  yXLTTov  yXoiöv  Hes. (^^ylttJ^-ögilit.  glitüs  usw.),  yllxo(j.cci  ,hefte  mich  an  etwas,  verlange  heftig^, yUffXQog  ,leimig,  zäh,  schlüpfrig^  (vermutlich  mit  -qo-  von  einem  "^yVicyM aus  ^y'ki%-OY.(x))\
lat.  glüs,  -tis,  glüten,  -inis  n.  ,Leim^,  glütinö  ,leime  zusammen^  (ü  aus  oi, vgl.  das  ablautende:)  glis,  -tis  ,humus  tenax^,  glittüs  ,subactis  levibus,  te- neris^  (Grundf.  "^gleitos  mit  intensivem  tt)]
air.  glenim  (*gli-nä-mi),  cymr.  glynaf  ,adhaereö%-  dazu  ferner  air.  for- diuclainn  , verschlingt',  nach  Pedersen  KG.  II  540  aus  for-di-uks-glen-  zu *glenaid  (aus  "^gl-nä-ti)]  auch  bret.  geot  ,Gras'  aus  ^gel-tä  (Marstrander I'    Pr^s.  nas.  30f.);°
ags.  clceg  (engl,  clay),  mnd.  Jdei  ,Lehm^,  dän.  klceg  ,zäher,  fetter,  leh- ^,  miger  Schlamm^  (germ.  "^klajja-]  dazu  ndd.  kleggen  ,klettern^);  ablautend norw.  dial-  kli  ,Schlamm,  Lehm^  (die  Ableitung  mnd.  klick  ,Lehmerde' wohl  nach  slick  ,Schlick,  Lehmerde^?),  ahd,  klenan  , kleben,  schmieren^ (=  ir.  glenim,  s.  oben,  vgl.  auch  nominal  yXlvr]  usw. ;  ist  klenan  als  st.  V. I  in  die  e-Reihe  übergetreten,  daher  auch  anord.  klunna  ,festhangen^  ?) ; hochstufig  anord.  kllna  ,beschmieren^  (*klmian,  schw.  V.),  mit  oi  norw. kleina  ds.;
lit.  gliejü',  glieti  ^beschmieren',  refl.  glietis  ,kleben  bleiben';
sl.  "^ghjh  in  russ.  glej  ,Ton,  Lehm',  poln.  glej  , schlammiger  Boden'  ( :  gr. ylla',  erweitert  russ.  mdartl.  glekz  , Schleim,  Blutwasser'  aus  *gh-k^)]
gleibh'  (slav.  Entsprechungen  s.  unten) ;  an  sich  auch  aus  idg.  *glei-p- herleitbar  in
ahd.  kleben  ,kleben,  haften,  festsitzen',  as.  klibön,  ags.  clifian,  cleofian ,kleben,  anhangen',  ags.  clibbor  ,klebend',  hochstufig  ahd.  kliban  ,haften, kleben',  as.  bikllian  ds.,  ags.  cllfan  ,haften',  anord.  klifa  , klettern  (sich anheften,  anklammern)',  mndl.  cllven  ds.;  ahd.  kliba,  as.  kliva,  ags.  cllfe ,Klette';  mit  -oi-  ahd.  kleiben  , befestigen  (kleben  machen)',  nhd.  kleiben ,kleben,  kleistern';  ags.  clcefre  (*klaibriön-),  mnd.  kläver,  klever  ,Klee'; hierher  auch  anord.  kleif  f.,  klif  n.  , steile  Anhöhe',  ags.  clif  n., 
=== POK p.364 ===
 mnd.  klif , Klippe',  ahd.  klep  (-b-)  , Vorgebirge',  mndl.,  mnd.  klippe  f.  , Klippe'  (daraus nhd.  Klippe  als  , glatter  Felsen',  wie  air.  sllab  ,Berg'  zu  Wz.  *sleib-  ,gleiten'); inwieweit  in  ags.  ahd.  klimban  ,klimmen,  klettern'  neben  "^gle-m-bh  auch eine  nasalierte  Form  von  *glei-bh-  unterläuft,  ist  unklar;
aksl.  u-ghbVg  , bleibe  stecken',  Aor.  ughbq,  ,iv£Tcdyr](jav\  nglebz  (e  =  &) fivsTtceyrjv',  ablautend  (*oi)  russ.-ksl.  uglebVevati  ,infigere',  und  (*e^)  serb. gilb  ,Kot'  (Berneker  310).
364  ,
glei-d-  in  mir.  glöed  ,LeiinS  ags.  cläte  f.  .Klette^,  eilte  f.  ,HuflatticKS eng-l.  dial.  clote,  clite,  cleat  .Klette^  clite  ,Leim,  Schlamm^  ( :  lett.  gU^i^^ ,sdileimig  werdenS  vgl.  Mühlenbach-Endzelin  I  626,  627).  .g
mit  122-Formans:  ags.  cläm  ^klebriger  Stoff,  Lehm^  wozu  anord.  Kleima ,Name  einer  Riesin^  ags.  clceman  .schmieren',  ahd.   chleimen  ,leimen';
lett.  gliemezis,  gliems,  glieme  ,Schnecke,  Muschel';  lit.  gUimes  .Schleim^ glimüs  ,schleimig';  lett.  glatma  ,Scherz,  Schmeichelei^  glaimuot  ,scherzen, schmeicheln,  liebkosen'  (vgl.  norw.  dial.  kleima  ^schmieren  :  liebkosen'); Mühlenbach-Endzelin  I  621,  628 f.;  Trautmann  92;  über  lit.  gllmes  s.  oben S.  361;  %
sl.  *gUmyzdzh  in  cech.  hlemyzd'  , Schnecke'.  -^-
mit  i2-Formans  (s.  o.  yllvr]  usw.)  russ.-ksl.  gUm  , Schleim,  zähe  Feuch- tigkeit', glina  ,Ton' ;
glei't'  in  ags.  cetcllpan  , festkleben,  anhangen',  schwachstufig  cZida, clioda  m.  ,Wundpflaster',  ags.  cUde  ,Klette'  (,die  anhaftende'),  ahd.  kledda, kletta,  ndl.  klis,  klit  ,Klette',  nhd.  klettern-,  auch  wohl  mhd.  kleit,  nhd.  E2e%d, ags.  cläd  ds.;  mhd.  kllster  ,Kleister',  nisl.  kllstra  ,kleistern'  (als  ^gleit-tro- hierher  oder  mit  dem  germ,  Formans  -stra-  von  der  einf.  Wzf.  *kli-j  idg. glei-)',  norw.  kleisa  ,kleben;  (mit  der  Zunge  kleben  =)  lispelnd  oder  unrein reden',  anord.  kleiss  l  male  ,stotternd^
lit.  glitus  ,glatt,  klebrig',  glyte  ,Nasenschleim,  pl.  Fischleim',  lett.  glits ,glatt,  nett,  hübsch' ;  lett.  gllstu^  glidu,  glist  , schleimig  sein  und  werden' glldet  , schleimig  werden',  gleists  , Schwätzer';  s.  Mühlenbach-Endzelin 624,  627;  vgl.  oben  S.  363  gr.  ylitTÖv]
vielleicht  in  russ.  (usw.)  glist^,  glistd  ,Wurm,  Regenwurm,  Bandwurm' (oder  zu  nhd.  gleiten]  Berneker  304);
mit  u-Formans :  germ.  *klahca-,  ahd.  kleo-,  kle  ,Klee^  (nach  dem  kh brigen  Saft  der  Blüte?)  und  "^kllwön-,  mnd.  klie,  ahd.  klnca,  klla,  nh< Kleie  f.  (wenn  mit  idg.  I,  so  ablautgleich  mit  lett.  gllive  ,Schleim').
lit.  gleives  f.  PI.  , Schleim',  lett.  glevs  ,zäh  wie  Schleim,  schlaff  (ob  mi e  aus
```


## [2026-09-05T20:38:44.002Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -A80 '^gel-\\.* *2\\|gel-2\\|To form into a ball' AHD_watkins1985.txt | head -140",
 "description": "AHD Watkins gel-"
}
```


### [2026-09-05T20:38:44.054Z] TOOL RESULT

```
<persisted-output>
Output too large (86.9KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bt5udzv81.txt

Preview (first 2KB):
480:gel-2
481-[garwian. To make, prepare, equip. Germanic verb. 1. Old Norse gera, to make, do: GAR. 2. Form *garui-, equipment, adornment, in Italian garbo, grace, elegance of dress: GARB. 3. Form “garwa-, prepared, in Old Eng- lish gearu, gearo, ready: YARE. 4. Form *garwin- in Old Norse gervi, equipment, gear: GEAR.]
482-gau-. To rejoice; also to have religious fear or awe. Contracted from “gaou-. 1. Suffixed form *gau-d-é- in Latin gaudére, to rejoice: GAUD, (GAUDY!), GAUDY?2, JOY; ENJOY, REJOICE. 2. Form (with nasal infix) *go-n-u- in Greek ganusthai, to rejoice (> ganos, brightness, glad- ness): GANOID. [Pok. gadu- 353.]
483-[gé. Also gaia. The earth. Greek noun of unknown origin. GAEA, GEO-; APOGEE, EPIGEAL, (GEANTICLINE), GEODE, (GEORGIC), HYPOGEAL, NEOGAEA, PERIGEE.]
484-géi-'. To sprout, split open. Contracted from *geoi-. Zero-grade form *gi- (< *gis-) in: a. Germanic *ki-nan in Old English cine, cinu, cleft, ravine cut by a stream: CHINK}; b. Germanic *ki-ddn- in Frankish *kid-, sprout, young shoot, in Old French cion, shoot: scron. [Pok. géi- 355.]
485-gé@i-2. To sing. Contracted from *geai-. Zero-grade form *gi- (< *gia-) in Sanskrit gitd, song: BHAGAVAD-GITA. [Pok. géi)- 355.]
...
</persisted-output>
```


## [2026-09-05T20:38:47.104Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'Pok. gel-\\|Pok. gel- ' AHD_watkins1985.txt | head -20; echo ---; grep -n 'To form into a ball' AHD_watkins1985.txt | head",
 "description": "Find AHD gel- entry"
}
```


### [2026-09-05T20:38:47.164Z] TOOL RESULT

```
489:*klai-ni-, bright, pure, in: a. Old English cléne, pure, clean: CLEAN; b. Old English clénsian, to purify, cleanse: CLEANSE. 2. Extended and suffixed zero-grade form *glo-nd in Greek gléné, eyeball: EUGLENA. [Pok. gel- 366.] gel-3. Cold; to freeze. 1. Germanic *kaliz, coldness, in Old English c(iJele, chill: CHILL. 2. Germanic *kaldaz, cold, in Old English ceald, cold: COLD. 3. Germanic *kédl-, cool, in: a. Old English cdl, cold, cool: cooL; b. Germanic *koéljan, to cool, in Old English célan, to cool: KEEL’. 4. Suffixed form *gel-d- in Latin geldre, to freeze: GELA- TIN, GELATION, JELLY; CONGEAL. 5. Suffixed form *gel-u- in Latin gelu, frost, cold: GELID. 6. Probably suffixed zero-grade form *gl-k- in Latin glaciés, ice: GLACE, GLACIAL, GLACIATE, GLACIER, GLACIS. [Pok. 3. gel()- 365.] gembh-. Tooth, nail. I. Suffixed o-grade form *gombh-o-. 1. Germanic *kambaz, comb, in: a. Old English camb, comb: COMB, KAME; b. Old High German kamb, comb: CAM; c. Germanic denominative *kambjan, to comb, in Old English cemban, to comb: OAKUM, UNKEMPT. 2. Greek gomphos, tooth, peg, bolt: GoMPHosIS. II. Per- haps Germanic *kimb- in Old English cim-, cimb-, rim (only in compounds): CHIME?. III. Possibly suffixed form *gembh-ma in Latin gemma, bud, hence gem: GEM, GEMMA, GEMMATE, GEMMULE. [Pok. gembh- 369.] geme-. To marry. Suffixed zero-grade form “gmoa-o- in Greek gamos, marriage: GAMETE, GAMO-, -GAMOUS, -GAMY; GAMOSEPALOUS. [Pok. gem/(e)- 369.] gen-. To compress into a ball. Hypothetical Indo-Euro- pean base of a range of Germanic words referring to compact, knobby bodies and projections, sharp blows. 1. Germanic *kn-a-pp- in: a. Old English cnzpp, hilltop: KNAP?; b. Middle Dutch cnoppen, to snap, and Low German knappen, to snap, hence “to have a bite,” akin to Middle English knappen, to strike sharply, snap: KNAP!; KNAPSACK; C. Old English cnop, knob: KNop. 2. Ger- manic *kn-a-k- in Middle High German knacken, to crack; KNACKWURST. 3. Germanic *kn-a-r- in: a. Norwe- gian knart, knot in wood, akin to the source of Middle English knarre, knob: KNAR; b. Middle English knor, a swelling: KNUR. 4. Germanic *kn-u-b- in Middle Low German knobbe, knubbe, knot in wood, knob: KNOB, NuB. 5. Germanic *kn-u-k- in: a. Old English cnocian, to knock: KNOCK; b. Italian gnocco, nocchio, knot in wood: GNOCCHI; c. Middle Low German kndkel, knuckle, akin to Middle English knakel, knuckle: KNUCKLE. 6. Ger- manic *kn-u-l- in: a. Old English cnyllan, to strike: KNELL, KNOLL; b. Old English cnoll, a knoll: KNOLL!. 7. Germanic *kn-u-p- in Middle Dutch cnoppe, knob, bud: KNOBKERRIE. 8. Germanic *kn-u-t- in: a. Old Eng- lish cnytten, to tie in a knot, knit: KNIT; b. Old English cnotta, knot in cord: KNOT!; c. Old Norse kniitr, knot in cord: KNOUT. 9. Germanic *kn-u-th- in Old High German knodo, knob, knot (> French quenelle): QUENELLE 10. Germanic *kn-i-b- in Old English cnif, knife: KNIFE. 11. Germanic *kn-e-th- in Old English cnedan, to knead: KNEAD. [Pok. gen- 370.] gene-. Also gen-. To give birth, beget; with derivatives referring to aspects and results of procreation and to familial and tribal groups. 1. Suffixed zero-grade form *gn-yo- in Germanic *kunjam, family, in: a. Old English cyn(n), race, family, kin: KIN; KINDRED; b. *kuningaz, king (< “son of the royal kin”), in Old English cyning, king: KING. 2. Suffixed zero-grade form *gn-ti- in: a. Ger- manic *kundjaz, family, race, in Old English cynd, gecynd(e), origin, birth, race, family, kind: KIND!; b. Ger- manic*kundiz, natural, native, in Old English gecynde (ge-, collective prefix; see kom), natural, native, fitting: KIND?; c. Germanic variant *kinth- in Old High German kind, child: KINDERGARTEN, KRIss KRINGLE; d. Latin géns (stem gent-), race, clan (> French gens, men): GENS, GENTEEL, GENTILE, GENTLE; GENDARME. 3. Suffixed full-grade form *gen-es- in: a. Latin genus (stem gener-), race, kind: GENDER, GENERAL, GENERATE, (GENERA-
---
486:gel-'. To form into a ball; conventional base of loosely connected derivatives referring to a compact mass or coagulated lump, and to the qualities of viscosity and adhesiveness. I. Words meaning a mass or lump. 1. Ger- manic *klamp- in Middle Low German klumpe, compact group of trees: CLUMP. 2. Germanic *klub(b)- in Old Norse klubba, a lump of wood, club: cLuB!. 3. Germanic *kliw- in Old English cliewan, a ball, ball of wool: cLEW!, (CLUE). 4. Germanic *kiid- in: a. Old English clid, hill, rock: CLOUD; b. Old English clott, lump: CLOD, CLOT, (CLUTTER); ¢. Middle High German kloz, block, lump: KLUTzZ. 5. Germanic *kiit- in Old English clit, patch (< “Jump, piece of stuff, piece of cloth”): CLouT. 6. Ger- manic *klaut- in Old English *cléat, lump, wedge: CLEAT. 7. Extended form *glob- perhaps in Latin globus, ball, globe: GLOBE, (GLOBULE); CONGLOBATE. 8. Extended form *glom- in Latin glomus (stem glomer-), ball: GLOM- ERATE, GLOMERULE; AGGLOMERATE, CONGLOMERATE. 9. Extended form *gléb- in Latin gléba, lump, clod of earth, soil, land: GLEBE. 10. Extended form *gleu- in Greek gloutos, buttock: GLUTEUS. 11. Reduplicated form *gal-gl- dissimilated in Greek ganglion, cystlike tumor, hence nerve-bundle: GANGLION. II. Words meaning to stick, cling. 1. Germanic *klupjan (< *gleb-) in Old English clyppan, to embrace, fasten: cLIp2. 2. Germanic *klimban (< *gle-m-bh-), to hold fast, hold on in climb- ing, in Old English climban, to climb: CLIMB. 3. Ger- manic *klam- in: a. Old English clamm, bond, fetter: (CLAM!), CLAM2; b. Middle Low German klam, stickiness: CLAMMY. 4. Germanic *k/amp- in Middle Dutch klampe, metal clasp: CLAMP. 5. Germanic *kleb- (< *glebh-) in: a. Old English cleofian, to stick, cleave: CLEAVE?; b. Old English clife, goosegrass (a plant with hooked prickles on the stem): CLEAVERS. 6. Germanic *kling- in: a. Old English clingan, to cling: CLING; b. Old English beclenc- an, to hold fast (be-, on all sides; see ambhi): CLENCH, (CLINCH). 7. Germanic *kluk- in Old English clyccan, to clutch: cLuTCH!. 8. Germanic kléw6, remade to *klaw6, in Old English clawu, a claw: CLAW. III. Words meaning “sticky material.” 1. Extended form *glei- in: a. Ger- manic *klajj6-, clay, in Old English clég, clay: CLAY; b. probably Medieval Greek glia, gloia, glue: GLIADIN; MESOGLEA, NEUROGLIA, ZOOGLOEA; C. Russian giei, clay: GLEY. 2. Germanic *kleg- in Danish klagge, mud, akin to the Scandinavian source of English dialectal clag, to daub with mud: cuac. 3. Extended form *gleu- in Latin gliten, glue: GLUE, GLUTEN, GLUTINOUS; AGGLUTINATE, CONGLUTINATE, DEGLUTINATE. 4. Extended form *glit- possibly in Latin glittus, sticky: GLEET. [Pok. 1. gel- 357.]
```


## [2026-09-05T20:39:03.866Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC leaf 166 (p.302-303) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==167' IEC.txt | head -80",
 "description": "Mann IEC p.303"
}
```


## [2026-09-05T20:39:04.890Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN leaf 932 (p.908) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==932' SYN.txt | head -60",
 "description": "Buck SYN p.908"
}
```


### [2026-09-05T20:39:05.620Z] TOOL RESULT

```
=== IEC leaf 166 (p.302-303) ===
� ‘stick; be sticky, adhere’. WP I, 619. Sce next Olr. glenaim, Ir. gleanaim; W glynu; Cor. gleny; OHG klénan ‘smear’; beside (*-1-) ON klína, Norw. kline, id.; OCS cf. glina “clay”
glinos, à ‘viscid; viscosity, mucus, glue’.
Cf. glíno, glein-, gulen- Gk. ging ‘glue’; Olr. cf. glenaim ‘adhere’; W glyn ‘sticky; adhesion’; OHG cf. klénan ‘smear’ and (*-1-) ON klina, wd: Norw. klin ‘smear; muck’; OCS glina ‘clay’ (*-1-). WP cf. I, 619-21
glisdh- ‘cluster, clump, mass’. Cf. glisteros Gk. á-glis, gs -glithos ‘clove of garlic”, fr. - *sm-°); Hes. cf. (Maced. or Thrac.) a-glidia *earlic-cloves'; Latv. glizda ‘clay, marl’; cf. EMDou. (*-i-) klis, klisse-kruid, klitte “bur”; klissen ‘adhere’; Du. klis (also = ‘tangle, knot")
(glisgh-, cf. glisdh-, glist-, glisteros, glit-) Gk. cf. glískhros ‘clammy, sticky; G cf. Kitsch ‘sticky mess’; klitschig ‘sticky ,
glist-, glisteros ‘adhesive’. WP I, 620 Mod. Gk. glisterós 'slippery, smooth'; cf. also Gk. glískhros 'gluey; MHG klister ‘glue’; OCS glista ‘tapeworm’; Srb. glista ‘worm’. Isophonic forms are S. Alb. glisht, Alb. gisht ‘finger’ and LGer. kliste ‘thwart on raft?
glitos, à, is, us, io “sticky, adhesive; glue, slime'. WP I, 620 Hes. glítton (‘glue’, w. expressive doubling) (acc. m. or n.); Alb. cf. n-gjis, aor. n-gjita, v. ‘stick, apply’; Lat. glis, gs glitis *potter's clay’; OE cliðe ‘burdock’; clióa ‘poultice’; Li. glitis, gs -ies ‘slime’; glitas ‘glue’; glitüs ‘slimy,
279
slippery, smooth’; Latv. glita ‘slime’; glits ‘slippery, slimy, smooth’; (*-1- in Li. glyte *mucus?)
gliu- (glou-) ‘ball, clump'. Cf. glauos (2). Cf. (glou-) WP I, 617 Skt. glau “lump, goitre’; Gk. Hes. (?) glíos ‘taut; gag-glíon, n. *ganglion'; MIr. glau, glo ‘bal’; OHG kliwa, kliuwa 'clew, ball of thread'; OE cliewen; Du. kluwen; LG klugen, id. beside ON klé, pl. Kär (1oom-weight, fr. *gléu-); Srb. Slovene gliva ‘fungus’; Cz. hlíva “puffbalP'; Latv. glivene ‘pondweed’. Vocalism uncertain in Lat. gluo, ére “draw together’; (*glou-) in W glewa, 3s *glaw ‘scrape together
(glmb-, glmbh-, see glumb-, glumbh-)
globos, à “lump, mass’. WP I, 615 Arm. (?) kav, o-st. (clay'. Cf. kat “milk? for possible loss of *l); Lat. globus, um; It. ghiova ‘clod, sod; MHG klapf ‘rock’; LG klapp ‘knot at end of whip’; EME clap 'go- norrhoea'; cf. dial. to clap, v. ‘huddle together, as hares’; Du. cf. klap-bes ‘gooseberry’; Li. cf. glabuZis, m. ‘sheaf, armful'. Cf. (*-6- or *.a- in) Ir. gláib ‘mud’. Verbal derivatives in Li. glaboju ‘clutch’; Latv. glabaju ‘keep’
glogh- ‘spike, tip, crag’ Gk. glóks, gs glokhós 'awn'; glokhís ‘tip’; Pol. glaz ‘rock’; cf. (*-o- in) ON kleggi *hay- cock; horsefly'; E dial. cleg fr. ON
gloiio ‘smear, stroke, wipe’. See next. WP I, 619 LG kleien ‘stroke, paw'; EME to claw ‘to flatter’; Li. glieju, inf. glieti ‘smear
gloiios “sticky; stickiness, glue, paste, clay, loam’. WP I, 619 Oss. (?) årgå “clay, mud’; Gk. gloios, gloía ‘glue’; gloiós ‘slimy; sluggish’; MIr. glaedh, glaoidh ‘glue’; OS klei; LG, Du. klei, OFris. klai; OE clæg ‘clay, loam’; Pol. glej, id.; Li. glájus ‘cake-filling, paste’; cf. glieju, glieti, v. ‘smear’. See next
gloim- ‘daub, smear; mud, mucus, slime’. WP I, 619. Cf. gloiió, etc. OHG kleimen ‘mould from clay’; G kleimen and (fr LG) klehmen, LG kleemen “stick, lime, glue, daub’; Kiem ‘da
```


### [2026-09-05T20:39:07.340Z] TOOL RESULT

```
=== SYN leaf 932 (p.908) ===
snout, Pp ks Walde-P.
ersen 1.42.
thread’ (6.38), used also for
(semantic borrowing) Fr. fil. barvenn, fr. barv ‘barb’.
a ribl er ‘shore, bank’, but also
Lat. ripula, dim. of
Numerous other
‘edge’, like
a(c)arf, etc. (15.78).
MUHG snide, NHG schneide, fr. sniden
‘out? (9.22),
ON bord, OF bord, OHG bort, etc.,
general Gme. word, in part ‘edge, bor-
der, but esp. ‘ship’s side’, root connec-
tion dub, Walde-P, 2.163, Falk-Torp 94.
eae W. 88. NED s.v. board, sb. nee Fr. bord ‘edge, border’, etc. and,
th : — a Fr. deriv., ME bordure, NE
MLG kant, kante, D Dan,, Sy, kant, NH Be LLG >
i: : G kante), used esp. ae ae edge’ (as of a table, ata.) a fe cant (formerly ‘edge’ or §, all fr. a form of the group It. 1 @te., prob. the OF. on cn eb alk-Torp 499. NED s.v. N mee and, trond, OHG rant, or hi ‘only for the ‘boss of a eld’, but Dan., Sw., Du >)
Digitized by Arya Samaj Foundation Chennai and eGangotri
PLACE, FORM, SIZE 861 NHG rand the most comprehensive word for ‘edge’ as ‘border’, etc., prob. fr. an extension of *rem- in ON rimi ‘strip of land, ridge’, OE rima (mostly in epds.), NE rim, OHG rama ‘support, frame’ (NHG rahmen), etc. Walde-P. 2.372. Falk-Torp 876.
Goth. skaut (reg. for kpdomedov, but always ‘edge’ of a garment) : ON skaut ‘corner of cloth, skirt, bosom’, OE scéat ‘corner, region, lap, cloth’, fr. the root in OE scéotan, OHG sctozan ‘rush, throw, shoot, hit’, ete. Walde-P. 2.554. Feist 431.
OE sné@d ‘bit, slice’ and in Gospels reg. for Vulgate jimbria = xpacomedov, fr. snedan ‘cut off’.
OHG trddo (Otfr., Tat. for NT fim- bria, kpaomebov), prob. fr. the root in OE teran ‘tear’, etc. Walde-P. 1.798. Falk-
Torp 1281.
6. Lith. asmens, Lett. asmens, above, 1.
Lith. kragtas (also ‘shore, bank’, as Lett. krasts), etym.? Miuhl.-Endz. 2.260.
Lith. briauna : Ir. brit (above, 4).
Lett. mala : Lith. lyg-malas ‘full to the brim’, perh. Alb. mal ‘mountain’, etc. Miuhl.-Endz. 2.556.
7. ChSI. ostrije, etc., above, 1.
ChSl. kraji, Russ. kraj, Boh. (0)kraj (SCr., Pol. kraj mostly in other senses) : ChSI. -krojiti, etc. ‘cut’ (9.22). Berneker 605f. Here also Pol. krawedd, fr. krawaé iter. form of kroié ‘cut’. Briickner 265, 268.
ChS&l. viiskrilije (reg. for xpdomedov in Gospels), epd. of krilo ‘wing’. Berneker 615.
SCr. brid, fr. the root in SCr. brijaiz, Boh. bfiti, etc. ‘shave’ (cf. ChSl. briiva, etc. ‘razor’, 6.93).
SCr. ivica, etym.? Berneker 439.
Boh. hrana : late ChSl. grant ‘chap- ter’, Russ. gran’ ‘facet, side’, $Cr., Pol.,
CC-O. In Public Domain. Gurukul Kangri Collection, Haridwar
hi
Digitized by Arya Samaj Foundation Chennai and eGangotri
862
Russ. granica ‘boundary’, etc., these prob. : Ir. grend ‘beard’, ON gron, OE granu, OHG grana, MHG granne ‘mus- tache’ (MHG also, as NHG, ‘beard of grains’, etc.), all with common notion of something projecting. Walde-P. 1.606. Berneker 346. Briickner 155.
Pol. brzeg, also ‘shore’, like ChSl. brégit, etc. See 1.27.
SELECTED INDO-EU
```


## [2026-09-05T20:39:15.567Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"9\\.08\\|9\\. 08\" SYN.txt | head -20; echo ---; awk 'BEGIN{RS=\"\\f\"} /908/ && /BALL|ball/ {print NR\": \"substr($0,1,300)}' SYN.txt | head -10",
 "description": "Search Buck for 9.08 / ball"
}
```


### [2026-09-05T20:39:18.759Z] TOOL RESULT

```
---
980: tpa
Words for ‘g
ee Palla, also ‘ball’, fr. Langob. palla ale balla, ballo ‘ball’ (> It. balla bran Palle ‘ball, bale’, ete.), ON RE ggg" Blobe, sphere’ (below, 4).
Pr 4, * Yul Pule, Sp, bola, fr. Lat. bulla ‘bub-
IAL RELATIONS:
Digitized by Arya Samaj Foundation Chennai and eGango
```


## [2026-09-05T20:39:21.344Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=978 && NR<=981 {print \"=== leaf \"NR\" ===\"; print}' SYN.txt | head -120",
 "description": "Buck ball section"
}
```


### [2026-09-05T20:39:23.174Z] TOOL RESULT

```
=== leaf 978 ===
tula- : vrt-, Lat. vertere ‘turn’, etc. Walde-P. 1.274. Uhlen- beck 275.
Av. skarana- : Ir. cruind, ete. (above, 3). Barth. 1587.
12.82 CIRCLE
ie Goth. .. Lith.  apskritis, ratas mes ON hringr, kringla Lett. rin’k'is circulus Dan.  kreds ChSl. kragit ta, cerchio Sw. krets SCr.  krug he Ml OE trendel, hring Boh. kruh lem ME _scercle Pol. koto, krag Cilairt. of NE circle Russ. krug crc Porcul Du. cirkel, kring Skt.  mandala-, cakra- cylch, cant OHG  (A)ring, creiz Ay. oe kele'h i MHG kreiz, rinc Words aoe NHG_ kreis dots ain ‘circle’ are from various xokda, ‘wheel’: Skt. cakra- ‘wheel, Stal pone ete Of ‘turn’. But in | circle’, Av. éakra-, ON Ayol, OE hweol,
Mobably ae the most widespread and
@ a Dein farliest use was to desig- SPecially « ‘ object of circular shape, I, fel’ or ‘ring’.
Tk, KUKXos, also, esp. in neut. pl.
etc. ‘wheel’ (10.76), fr. reduplicated forms of the root *kel- in Grk. wé\opar ‘be in motion, be’, Skt. car- ‘move about’, etc. Walde-P. 1.575.
2. Lat. circulus (> It. cerchio, Fr.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
906 SELECTED INDO-EUROPEAN SYNONYMS
cercle; lit. loanwords It. circolo, Sp. cfr- culo), dim. of circus (> Rum. cerc ‘circle’, but It. cerco obs., Sp. cerco in secondary.uses), which it replaced in the sense ‘circle’, the latter coming. to be the ‘circus’ (esp. Circus Maximus, and then others) : Grk. xlpxos, xpixos ‘ring’, fr. the root *(s)ker-in Lat, curvus ‘crooked’, etc. (12.74). Walde-P. 2.569. Ernout- M. 188 ff. Walde-H. 1.220f. REW 1947, 1948.
3. Ir. ciiairt, perh. loa
=== leaf 979 ===
nword fr. Lat. cohors, -tis (> cors, -tis) ‘court, enclo- sure’. Pedersen 1.205.
Ir. cireul, NIr. ciorcal, fr. Lat. circu- lus. Vendryes, De hib. voc. 124 f.
W. cylch, Br. kelc’h, fr. Lat. circ’lus = circulus. Loth, Mots lat. 156.
W. cant, Br. kant, prob. : Gallo-Lat. cant(h)us ‘iron rim of a wheel’, etc. (see 12.353). Walde-P. 1.351 f.
4. ON hringr, OHG (h)ring, MHG rinc, OE hring (but the latter mostly ‘ring’; this meaning also in ON, OHG, and MHG, and in the modern languages the usual one) : Umbr. cringatro ‘cinc- tum, band about the shoulder as a sign of office’, ChSI. kragi ‘circle’, etc.’ (be- low, 6), fr. extensions of the root *(s)ker- as in Lat. circus, etc. (above, 2). Falk- Torp 901.
ON kringla, kringr, Du: kring, MLG krink, MHG krine, kranc (NHG kringen, kringel) : Norw. krenkja ‘wrench’, Lith. grezti ‘bore’, Lett. griezt ‘turn’, nasalized forms of the root in ON krokr ‘hook’ (12.75). Walde-P. 1.594, Falk-Torp 580f. Weigand-H. 1.1153.
Late OHG creiz, MHG kreiz (> Dan. kreds, Sw. krets), NHG kreis : MLG
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar 0
kret(e), kreit, MDu. krit id., MHG krizen ‘make a circular line’, perh. further re. lated to OHG krizzin, MHG kritzen ‘scratch, engrave’, root connection? Weigand-H. 1.1145, 1155. Palk-Torp 578.
OE trendel, cf. MLG trendel ‘round disk’, MHG irendel ‘ball, circle’, OHG trennila ‘ball, sphere’, MLG trint, trent ‘circular’ : OE trenden (rare), ME trende ‘turn round, rotate’ (NE trend), but fur: ther root connections (as with NHG trennen ‘separate’) dub. Walde-P. 1.798. Falk-Torp 1283. NED 8.y. trend.
ME cercle, NE circle, fr. Fr. cercle (above, 2). NED s.v.
5. Lith. apskritis : Lith. skriesti ‘make a circle’, skrieti ‘run or fly in a circle’, skristt ‘fly’, fr. an extension of the root in Lat. circulus (above, 2) and ON hringr, ChSl. kragii, etc. (above, 4). Walde-P. 2.571. Trautmann 267.
Lith. ratas ‘wheel’, also ‘circle’ : Lat. rota, OHG rad, ete. ‘wheel’ (10.76; cf. Lat. rotundus ‘round’, 12.81). Walde-P. 2.368.
Lett. rin’k'is, also ‘ring’, fr. MLG rink ‘ring, circle’ (above, 4). Miuihl.-Endz. 3.529,
6. ChSl. kragi, etc., general Slavic : ON hringr, etc. ‘ring, circle’ (above, 4). Berneker 626.
Pol. koto ‘wheel’ (10.76), also ‘circle’, mostly replacing the older krag in this sense.
7. Skt. mandala-, etym. dub., perh. : Ir. mell ‘globus’. Walde-P. 2.295. Uh- lenbeck 211.
Skt. cakra- : Grk. xixdos (above, 1).
gpAT.
phere’ as the generic and ore or less technical terms are such as were popularly applied to peciicules ob- jects of spherical shape, esp. ball’ (sev- eral of the words listed are also or com- nonly ball’) or ‘elod, lump’, these again based on various notions including flown up, swollen’ or ‘pressed together’. 1, Gtk. o¢atpa, etym. dub., perh. : ssupts, onvpas ‘fall of dung (from sheep, mats, ete.), pill’, Lith., Lett. spira ‘heep-dung’, NIcel. spard ‘sheep-dung’, speroill ‘goat-dung’; or: Grk. ozaipw ‘quiver’, Skt. sphur- ‘spring, quiver, trouble’, ete. Walde-P. 2.672, 668. Boisacq 926, 900. 2. Lat. globus (hence the lit. words, ae globo, ete.) : gleba ‘Tump, clod’, , uh 2 # ith: glébiz, globti ‘take in the ith * E ’ Pol. gtobié ‘press, join ee . : Beside *glem- in Lat. te’ fr G yarn)’, Lith. glomoti ‘em- fre: ,, oe *gel-in words for Waldesp a ae lump, ball’, etc. Valdez. fies : 5. Emout-M. 425. L he ee (hence the lit. words It. (above), Sphere, ete.) fr. Grk. opa
=== leaf 980 ===
tpa
Words for ‘g
ee Palla, also ‘ball’, fr. Langob. palla ale balla, ballo ‘ball’ (> It. balla bran Palle ‘ball, bale’, ete.), ON RE ggg" Blobe, sphere’ (below, 4).
Pr 4, * Yul Pule, Sp, bola, fr. Lat. bulla ‘bub-
IAL RELATIONS:
Digitized by Arya Samaj Foundation Chennai and eGangotri
PLACE, FORM, SIZE 907
12.83 SPHERE
Goth. ...- Lith. kamuolys
qpaipe ON bolir Lett. bamba
Gi apaipe aera Dan.  klode, kugle ChSl. Dee
i globus vias jera Sw. klot SCr. kugla palla, he, sphere OE  cliwen Boh. koule poule, 7 ; = fera ME bal, spere, clewe Pol. kula
* ola, 0 7 NE sphere, globe Russ. Sar
Ru glob, sfer Du. bol Skt.  guda-, gola-, bimba-
hh mell seat OHG  cliuwa, ballo Avy. flee
Nit meall, a u MHG kugel(e), kliuwe, kléz
r pane NHG  kugel
m
ble, knob’ : Lett. bulis ‘buttocks’, MLG poll ‘knob, point’, Hast Fris. pol ‘round’, ete. Walde-P. 2.111, 115. REW 1385.
3. Ir. mell (cf. Gall. Mello-dinum), Nir. meall, also ‘lump, mass, knoll’, etym. dub., perh.: Skt. mandala- ‘circle’. Walde-P. 2.295. Stokes 214 f.
NIr. cruinne (mostly ‘the globe’, also abstract ‘roundness’), W. cronnell, fr. Ir. cruinn, W. crwn ‘round’ (12.81).
Br. boull, fr. Fr. boule (above). Henry 40.
4, ON bollr (> ME bal, NE ball), OHG ballo, balla, MHG balle (but mostly ‘ball’), here also Du. bol ‘sphere’ beside OHG bolla ‘bud’, OE bolla ‘round dish, bowl’, etc. : Lat. follis ‘bellows, money- bag, ball, or cushion inflated with air’, Grk. gaddés ‘penis (as emblem)’, fr. a root *bhel- seen in Lat. flare ‘blow’ and many others based on the notion of ‘blow up’ or ‘swell’... Walde-P. 2.179. Ernout-M. 374. Walde-H. 1.524f. Franck-v. W. 79f. NED s.v. ball, sb.'.
Dan. klode, Sw. klot, fr. MLG klot = MHG kloz ‘lump, clod, ball, sphere’ : MHG kloz, NHG klotz ‘block’, OE clott ‘ump’ (NE clot), Russ. gluda ‘lump’, fr. *gleu-d-, an extension of *gel- in Lat. globus, etc. (above, 2). Walde-P. 1.618. Falk-Torp 535.
MHG kugele, NHG kugel (> Dan. kugle, older Kugel), MLG kogel (Du. kogel ‘bullet, ball, shot’) : Lith. guga
‘pommel, hill’, Russ. guglja, Pol. guga
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
908 SELECTED INDO-EUROPEAN SYNONYMS
‘bump’, etc., guttural extensions of *geu- seen also in Skt. gola- ‘ball, sphere’ (be- low), MHG kiule ‘ball or knob on the end of a stick, club with a knob on the end’ (NHG keule), etc. Walde-P. 1.558. Falk-Torp 590.
OE cliwen, ME clewe, OHG cliuwa, MHG kliuwe (all esp. ‘ball of thread or yarn’; hence with further peculiar se- mantic development NE clew, cf. NED) : Skt. glau- ‘round lump’, NPers. gulile ‘ball’, fr. *gleu- (cf. *gleu-d- in Dan. klode, et
=== leaf 981 ===
c.). Walde-P. 1.617.
ME spere, NE sphere, fr. OF r. espere, Fr. sphére (above, 2).
5. Lith. kamuolys : kamuoti ‘press to- gether, stuff’, Lett. kams, Russ. kom ‘ump’, Russ. komit’ ‘press into a ball’, MUG hemmen ‘restrain’, ete. Walde-P. 1.388. Berneker 557.
Lett. bamba, also bumba (but the lat- ter rather ‘ball, bomb’, etc.?), cf. Lith. bamba ‘navel’, bumbulis ‘bubble’, bum- buras ‘bud’, Pol. babel ‘bubble, blister’, Boh. boubel ‘bubble’, Skt. bimba- ‘sphere, orb, disc, rounded part of the body’, etc., all prob. based on a syllable imitative of the sound made with puffed- up cheeks. Walde-P. 2.107f. Miuhl.- Endz, 1.261.
6. SCr. kugla, fr. MHG kugele, NHG kugel (above, 4). Berneker 641.
Boh. koule, Pol. kula fr. MHG or
MLG kile = MHG kiule (above, 4 Berneker 641. Briickner 281.
Russ. sar, orig.?
7. Skt. guda-, perh. for *gulda-, fr the root *gel- in Lat. globus, OE cliwen, MUG kilsz, ete. (above, 2, 4). Walde-P. 1.614.
Skt. gola- : MHG kiule, NHG keule etc. (above, 4). Walde-P.1.555,
Skt. bimba- : Lett. bamba (above, 5).
).
12.84. ‘Line’ (straight or curved ‘line’). A list is omitted, since with few exceptions the Eur. words are obvious derivs. of the Latin. For a line of writ- ing or printing there are often different words (18.63).
1. Grk. ypapy7, fr. ypadw ‘write’, hence orig. a stroke or line of the writing im- plement.
2. Lat. linea, orig. ‘linen thread, line’, secondarily ‘line’ in sense here intended, sb. form of lineus ‘made of flax, linen’, fr. linum ‘flax, linen’ (6.23). Hence the usual words for ‘line’ in most of the Eur. languages (Romance, Celtic, Gmce., Balto-Slavic).
3. Boh. éara, etym.? Berneker 136.
Skt. rekna-, fr. rikh- ‘scratch’ (with development like that in Grk. ypappq) : Grk. épeixw ‘bend, bruise’, OHG riga ‘line’ (NHG reithe ‘row, order’), OF réu, raw ‘row’, etc. Walde-P. 2.344.
12.85 HOLE Grk. 6m, tpéaqua Goth. airko Lith. skylé NG Tpira ON rauf Lett. caurums Lat. foramen Dan. hul ChSl. dupina It. buco Sw. hdl SCr. rupa Fr. trou OE pyrel, hol Boh.  dira Sp. agujero, hoyo ME eihodle, thirl Pol.  dziura Rum. gauré NE hole Russ. dyra Ir. toll Du. gat Skt. _ bila-, chidra- NIr. poll OHG lok Av. been W. twll MHG loch Br, toull NHG loch
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
SP ATIAL RELATIONS:
for ‘hole’ denoted ace (NE hole in the 5, etc.) and are cog- i or ‘hollow’ or with like. Others, with f perforation or «ved from verbs for
* a or ‘split’. One of is cognate with those for ye’ for the hole in a
notion 9
is widespread.
tye! and ‘opening,
i170, Boisacq 707. Gtk. rpbrmua, fr. rpirde ‘bore’ (9.46),
hence also the back-formation Byz.,
NG zpira.
9 Lat. foramen, 9.46).
ae cavum ‘hollow, hole’, sb. fr. adj.
cous ‘hollow’ (12.72).
It. buco, prob. fr. VLat. voc(u)us =
racuus ‘empty’ (18.22). Cf. Sp. hueco
folloy
```


## [2026-09-05T20:39:35.408Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=176 && NR<=182 {print \"=== leaf \"NR\" ===\"; print substr($0,1,2500)}' IEC.txt",
 "description": "Mann IEC around p.303"
}
```


### [2026-09-05T20:39:36.935Z] TOOL RESULT

```
=== leaf 176 ===
d-) “cry, scream’. See next Lat. (ambig.) rideo (laugh', prob. < *righid-); Gallo-Lat. in It. grido, are “cry? (if not fr. Gmc.); Crim. Go. criten, MLG kriten, Du. kruten ‘cry’; Fris. krite, id.; MHG krizen, id.; Ger kreissen “be in labour”. (Variant of type *grit- in Olr. grith, W gryd, m. ‘cry’)
gridos, ios ‘cry, shout, scream’. Cf. gridó OW cf. grió-fan 'groan'; Gallo-Lat. or Gmc. LW in It. grido, grida; MHG kriz “din, shout. (O-gde in LG kreet, MHG kreiz. Variant in W gryd (fr. *grit-)
griglis, os ‘strident; cricket" W grill ‘shril’; Br. gri? (cricket, infl. by Lat. gryllus); Du. krekel, id. Radical (*grig-) in Norw. krikk-and ‘teal’. Cf. grigo
grigo, ið ‘creak, shriek OE circian; LG cf. krick-ant ‘teal’; Norw. krikk-and, id.; Li. cf. griZas ‘creaking of joints". (Isophonic are Ir. griogaim, v. 'stab, pain' and ON kriki ‘node; armpit’)
grik- ‘yelp’ (?). See next W grig *rustle?; OCS griči dog
griksKo (griks-, grisk-) ‘cry, shriek, creak.
205
Cf. grid- Alb. gérshás, aor. grisha “shout, cal; MHG krischen ‘shriek’; LG krischen ‘creak’; Li. grikšiù, éti ‘creak’
grinĝhəlos, å ‘circle, circuit’. Cf. WP I, 594 and see gren$h-, grongh- MHG kringel; ON kringla, id.; Li. grjžulas "wagon-pole; tropic; griZulé ‘knot, torque’; Latv. grizulis ‘eddy’. (Isophonic is Ir. gringal *zeal")
gringho, ið ‘turn, circle’. Cf. WP I, 594 and grengh- Du. krengen; G cf. kringeln double up": ON kringja; Li. grjZtu, inf. grižti “return”
griuos, à “neck, nape; throat, open jaws' (?). WP I, 683 Skt. grivah, grīvā ‘neck’; Av. grivo ‘nape’; OCS griva ‘mane’; Latv. griva ‘estuary’ beside (iso- phonic) grīvis ‘rank grass’. Adjectival in OCS grivínü, grivína ‘necklace’. (For R. grivna, Cz. hřivna ‘talent-weighť see guru- and cpds., esp. guriu-).
(grmbh-, see grembh-. Z-gde in OHG krum- ben *bend")
grob- (?) ‘tight, compact, firm, close’ Arm. korovi ‘robust’; Ir. cf. grobhaire ‘miser’; Du. krap ‘tight, in short supply’; f. *clasp, buckle’; G krapf, LG krapp “firm, well-baked'
(groód-, see ghrod-. Gmc. only, as in Go. ga-kroton ‘shatter’; Sw. krotas, id. and LG kraetig, kroet- “violent, foolhardy’. Latv. grods “severe” ambig.)
groos, is, us (?). (See gor$-, grag- for pos- sible isophones) Ir. groigh ‘funny’; LG krack ‘nag’; E crack, adj. ‘tiptop’; Li. graZüs ‘beautiful’; Latv. graži, mpl. ‘caprices’. 
=== leaf 177 ===
omada ‘pile’, grominica ‘shop’
grom- (2) ‘waste, rubbish, triviality, decline’ ON krọm, gs kramar ‘wasting disease’; G cf. kramen ‘potter about; Kram ‘fuss’ (vocalism uncertain); Li. gramùs ‘finicky’; Latv. cf. gramstu-, -stīt (2) ‘twaddle’; gramšķis ‘twad- der: rubbish?
grom- (3) ‘cough, cough up; sputum’ Norw. cf. kremt ‘hawking cough’; kremte ‘clear the throat’; Li. gramai ‘sputum’
grom- (4) (grombh-) ‘squeeze, grip’. Cf. grembh- Sw. kram-, cpds. “balled-, lump’; krama, v. ‘squeeze’; cf. kråm ‘stuffing’ (fr. *gromu-) and kramla, f. “wall-brace'; G kramen “be in la- bour, childbed'; OE cf. crammian ‘cram, stuff. Cf. E dial. to cram in sense of ‘press out: ON kremja, id.; Latv. cf. gramstu, -stit (1): *snatch'; (2) “feel, grope'. Variant (grombh-) in MHG kram, gs. -mmes, sm. ‘cramp’; Du. kram ‘staple, bent hook’; krammen, Fris. kramje, v. ‘staple, cramp, clamp’. Cf. grembh- and grombos (2)
grombos (1) (?). See ghromb- and next. ON krappr (2) ‘sharp, crafty’; OCS grobü ‘raw, rough, coarse? (not com. SL); Li. cf. gramblùs ‘coarse, clumsy’; Latv. grambains ‘tough’
grombos, å (2) “holder, clamp, bit, grip’. Cf. grom- (4) & WP I, 596 Br. gromm (bit-chain of horse’, fr. *-b- or *-bh-); MHG krampf ‘cramp in limbs’; Du. kramp, id.; ON krappr, adj. (1) “narrow, con-
297
stricted'; Latv. gramba ‘rut’
grombh- (1) “scrape, scratch? Hes. cf. grompheís ‘painters’; gromphás, f. “sow, pig; MHG krammen (2) ‘wound’; G krammen “scratch
grombh- (variant of grom- (4), q.v.) (2) in MHG krammen (1) ‘clutch’; Du. krammen ‘clamp, cramp, staple’; cf. G Kramme ‘staple, holder’
grómos (gråmos?) ‘home, village” Skt. gråmah “tribe, village’; OCS gramü ‘lodging’. (E-gde in MHG krām ‘tent, booth’ (Ð)
(grón-, see grån-. kreunen ‘moan’, etc.) grondos, à, is ‘edge, rim, brim’. WP 595 Lat. grunda ‘eaves, porch’; It. gronda ‘eaves’; MHG kranz ‘garland’ (LWs in Du. Dan. Sw.
krans); Li. grandis, f. “link, ring; rank, file’
grondhos, à (gronth-) ‘mass, tuft, bunch? Skt. cf. granthah, ih ‘knot’; Gk. grónthos ‘balled fist, punch’; Cor. gron ‘mass, bunch’; Br. cf. (?) grunn ‘mass, pile’; W (?) grwn, pl. grynau (fridge, baulk’, but cf. grondos, above); Latv. (ambiguous) grods ‘tightly twisted, knotted’
gronĝeið (1) (variant of grongh-, see next and cf. grengh-) MHG krenke
=== leaf 178 ===
a Celt. LW in OFr. gru ‘groats’, and Mod. gruau ‘gruel’. Eng. fr. Fr.); Pol. gruz ‘rubble; Li. grauZas, ai ‘gravel, shingle; sawdust'; grau£iü, ^ti ‘gnaw’; Latv. grauZu, grauzt ‘erode’. (Isophonic: Upper German krauch "mp"
(gróu-, see gràu-)
grubolos ‘lumpy, rough, knotty; lump, hump’. WP I, 598 and see next MLG krüpel (> HG in G krüppel 'cripple); OE crypel; OFris. kreppel; Cz. Slovak hrbol, hrbof ‘hump’; Li. grüblas, id.; gniblüs ‘rug- ged'
grubos, io “lumpy, swollen; lump’. WP I, 595-8 MHG kroph ‘goitre; crop’; OE cropp “berry, kidney, pebble, clump’; Du. krop ‘gizzard; goitre; head of cabbage’; ON kroppr, gs. kropps ‘body’ beside kryppa ‘hump’, kropna, v. ‘be crippled, hunched’; OCS grúbú ‘back’; Cz. hrb, Pol. garb ‘hump, lump’; R gorb, id.; Li. grubas ‘hump, lump, hillock’; grubùs ‘rugged’, cf. also grubtas ‘clod’. (Isophonic: Du. kroppen ‘feed birds; suffer’; OE cryppan ‘crook, bend’; ON kroppa ‘crop, pick’; OCS po-grübiti ‘to bend'; Li. grumbü, grübti, v. ‘clench; become decrepit’; Fris. kropje, v. ‘belch; last")
grud- (1) ‘murmur, resound’. WP I, 658.
" C grugió
45
ON krotr, krytr, m. id.; krytja, v. ‘murmur’; Pol. grdac, inf. ^whirr
grud- (2) ‘mess, litter; hovel’ Du. krot, n. ‘hovel; f. ‘dung’. LW in Fr. crotte’; EME cf. crotels ‘hare-droppings’; Li.
299
cf. grundü, grusti, v. ‘get messy’; Ir. gruid, f. “mash, dregs'
grud- (3) ‘quick; brittle; crumbly'. (Li. ambig.) Mlr. grod, adj. ‘short’; Ir “alert, nimble’; Li. grüdüs, ‘frail; brittle; (fig.) ‘touching’. See next.
grudh- ‘harsh, sour, pungent’. See next Arm. (ambig.) kord, i, av, adj. “rough; o-st. ‘cleared land’; ME crud ‘curd’ beside EME to crud, v. ‘to curdle’; Du. krodde “wild mustard’; ON krydd, s. ‘spice’; Sw. krydda, f. id. (Isophonic: MHG króte, Upp. G Krott *toad'. Li. grudüs is ambig., cf. grud- (3))
grüdho, io “press, crush'. See next, and cf. WP I, 650 OE crūdan, sv. 2. “press; hasten; drive; throng’; Du. kruien, v. ‘be blocked with pack-ice'; Fris. kruije, id.; Norw. kry, v. ‘swarm’; Li. grüdu & grüdziu, grüsti, v. “push; intrude; pound’; Latv. grūžu, grūst, v. “buffet. No- minal types: Ir. grúid, f. ‘terror; OE *crüd ‘pressure, drive, crowd’; Fris. krûd ‘pest’; LG cf. krüd “fruit-pulp'; Latv. grüda, f. as OE; (short grade in) MHG krot “pest, nuis- a
=== leaf 179 ===
core; stump’; kurck, pl. form ‘breast’; R gryZa ‘hernia’; Li. gružas ‘gudgeon’, cf. gružulis, m. ‘dumpling’; Cz. cf. o-hryzek ‘core; adam's apple’; hryzlice ‘grub’; Fris. krükel ‘winkle’. (Isophonic: OE crocc; Du. kruik; Sw. kruka "por!
gru£os, à (3) “dirt, grime’ Hes. grüx 'dirt in the nails; EME crock ‘soot’; Latv. gruzis, pl. gruži “dirt, smut; rub- bish?
grugos (4) “broken-down; breakdown” EME crock 'spasm, in hawks?; cf. E old crock; Du. kruk ‘bungler’; Li. gruZas ‘worn out; scrappy’
gruk- (1) ‘rumble, croak, croon, rattle’ W grwgn, adj. ‘fumbling’; grig ‘rustle, mur- mur’, fr. *grük-; OCS grükajo ‘croak, coo’; Cz. hrkat ‘rattle’. Cf. variant (*gruks-) in Li. grukšiù, éti ‘crunch’ beside (*grukt- in) W grwyth ‘murmur’
gruk- (2) ‘shrink; crease, wrinkle’ Olr. gruc, groc ‘wrinkle’; Srb. gré ‘spasm, cramp’; OCS cf. sügrüCiti sę ‘shrink’
gruloó, io ‘grunt, growl’ Gk. grullízo ‘grunt’; Du. krollen ‘howl’; Lat. cf. grulisso ‘make noise of quail’. LW?
grumb- ‘hump, hunch’. Cf. grub-, grumbh- and next. WP I, 596 Br. (ambig.) grumm “fist'; EME cf. crump- backed "bunchbacked": crump-footed “club- footeď’; LG cf. krümper, m. ‘cripple’; Li. grumbu, grubti ‘get lumpy, form a clubfoot, get humped'. (Isophonic: OE crympan ‘curl, crimp’)
grumbəlos ‘hump, grumbh- and gruməlos Alb. grúmbull ‘pile, heap’; Latv. grumbulis ‘Jump, knob, knoiP. (Isophonic: G fr. LG Krumpel, Krümpel ‘ruck, crease’: E crumple)
grumbhos, à, iə “bend, turn, twist; bent etc. Cf. WP I, 596 MHG krumbe, krümbe ‘twist, turn’; krump, -bes ‘bent’; OFris. krumb ‘bent’; OE cf. hnifol- crumb *face-downward"; ON krumma ‘paw’; Latv. grumba (‘wrinkle, fold’. But for this,
lump’. Cf. grumb-,
301
cf. grumb-, grumbolos)
grümolos, à “lump, hump, mass’. Cf. grumb-, grumbh-, etc. Cf. WP I, 591 LLat. grumulum ‘wild gourd?’ beside Lat. grümulus ‘hillock’; It. grümolo “head of cab- bage’; Du. kruimel ‘crumb’; Icel. krumla, f. ‘paw, fist; Li. grümulas ‘lump, gnurl'. Cf. grümos
grümos (1) “piece, bit. WP I, 597 Hes. cf. grüméa ‘trash’; Lat. grümus (2) ‘clot, lump’; Alb. (ambig.) grimë (‘crumb, speck’, but if < Alb. grij, v. ‘mince’, cf. guhriio); Ir. grúm “icefloe*; LG krūme ‘crumb’; Du. kruim, id.; OE cf. cruma, id. with *-ü- and MHG krume, krumme, id.; Li. cf. gru
=== leaf 180 ===
ollapse’. Lat. in-, con-
grümolos, à — güd-
10
15
20
25
30
35
40
45
302
gruo is ambig.)
(grbos (u-basis) ‘hump; humped’. Cf. grub-)
(grbh- ‘cut; cutting’. Cf. Gk. gráphos “letter”; ON kurfr ‘chip’ under grabh- and cf. garbh-)
(grdh- “noise; audible’, etc. see gurdh-; “weak, sluggish’, etc. see gurd-, gurd-)
(grg-, grgh-, see gurg-, gurgh-)
grgh- (ghrgh-?) *house, home, village Skt. grhám ‘house’; Ir. gráig, grágán “village?
(grgh- ‘squeak, shriek’, see gurgh-)
grk- ‘hoarse; hoarseness’. Cf. grquis and ghrquuó, gurks- W gryg ‘harshness, roughness; Cz. hrk (ambig.) *traucousness'
grpis, os (?) 'slough, skin, gut, pipe” Hes. grápis ‘slough of snake’; Sw. korv 'saus- age” (?).
grquis ‘raucous cry; raucous bird" (?) Hes. grápis (3) a bd Other evidence ambig. cf. gurks-, ghrquio, etc. Isophonic are Hes. grápis (2) *wrinkled' and Srb. gré ‘cramp’
grt- ‘gather, assemble’ Hes. cf. á-garris (for á-garsis ‘meeting’, fr. ageíro); Srb. græem, grtati ‘gather’; ginuti, id.; Cz. hrnout; Pol. garnać: Ukr. pri-hornuty, id. (Gk. px. fr. *sm-, q.v.) (Slav. perfectives fr. *grt-n-)
gubəlos, gubulos ‘hump, lump, boss’. Vari- ant: gubər-. See next Oss. (ambig) gubir 'hunchbacked'; MHG ko- fel “peak, summit’; Li. gübulas “lump” beside gübras ‘mound’. (Isophones: OE copel “un- steady’; LG koppel ‘paddock’; Cz. heble ‘tiny object, mite’)
gubos, à ‘pile; peak; top, head’. Cf. WP I, 562-7 MHG koph, kopf ‘poll, head, skull’; OE copp ‘summit’; EME cop ‘hillock, spindleful of yarn’; Du. kop ‘head, hilltop’; Sw. koppa (1) ‘crewcut head’ beside (*-ü- in) kūpa ‘hump’; Li. Latv. gubà, guba, f. ‘pile, stook’. (The Gmc. forms are ambig. ? *ĝub-)
gud- ‘anus, pudendum’ Skt. gudáh ‘gut, anus’; gúdā ‘bowels’; MHG kotze ‘pudenda mulieb?
güd- ‘knob, grain’, Cf. güd- (2) Arm. kut, gs. kto (1) ‘grain, kernel; Du. (*-ū-) kuit (1) ‘roe, spawn, milt’; Sw. kotte
303
‘fircone’; Li. cf. gudiniai ‘shallots’
gūd- (1) ‘grim’ Ukr. cf. hydkyj ‘ugly’; hydytysja ‘loathe’; Cz. cf. hyzdit ‘disfigure’; Li. gūdùs ‘glum, murky’
güd- (2) “lump, balP. Per güy, id. (fr. *güdio-); Arm. kujt, gs kuti, i-st. “pile, mass’; kut (2) ‘wealth’: MLG küte ‘bundle of flax’; Du. kuit ‘calf of leg’; G Kauz (2) ‘bun of hair, wisp of hair; Scots kyte ‘belly’; E dial. cf. bumble-kite ‘blackber
=== leaf 181 ===
Küchlein; Du. kuiken, id.; Li. gužas 'stork'; Alb. guzé (“coot is ambig. perh. *gugio or *gudio)
gügh- ‘huddle, hide, squat, crouch together; hiding-place, hole’. Cf. WP I, 566-7 & 638 Skt. gühami “hide”; guh, guha *hiding-place';
güd- — gulg- (gulgu-)
20
25
30
35
40
45
304
Av. a-guze (mp. *hide") beside (o-gde) gaoz- “keep, hide’; Ober gaud- *hide'; ON küga “cow, force’; Norw. kue; E to cow; MHG cf. koge ‘plague, contagion; EME to cog ‘to cheat’; Blg. gizna ‘wallow’; Li. gūžiù, gūžti ‘snuggle’; güzis, f. ‘nest of a brood’ beside gužu, ēti ‘scurry away’; G cf. sich kuscheln ‘snuggle, nestle’ (from *gughsKo. Eng. to cow & to cog appear to be dialectal variants *ü/u)
gughàa, io 'hunkers, buttocks’. Cf. gugh- and next Cz. hyže, hyZdé “ham, thigh’; Latv. guZa, id.
gughelos, à “lump, ball’. Cf. gugh-, gughaà MHG kugele ‘ball’; G Kugel ‘bullet; OE cycgel ‘cudgel’; Du. kogel ‘bullet’; Li. güZulas (bundle, sheaf ambig., cf. güigos)
guk- (?) OE cf. cohhettan *cough" (but MHG küchen ‘breathe; pant may be a hybrid, cf. G keuchen ‘pant? and hauchen breathe); R gika? ‘whoop’ Cz. hykat ‘bray’
gul- ‘throat, gullet; gorge, ditch; swallow- ing’. Cf. gulgó, gulgul- Arm. kul ‘gorge; gulp’ beside klanem *swal- low, devour’; Lat. gula; gulo ‘gullet; glutton’; Ir. goile ‘maw’; Blg. gálka ‘mastoid’. (Per. gulü ‘throat? derives from gurgət-, q.v.). Variant (*gūl-) in MHG kūle, LG kūl, OFris. kūle, Du. kuil, G Kaule & (dial.) Kuhle “hol- low, ditch’.
gül- “head, knob’. See gulos, ios Per. (ambig.) gül ‘blockhead’; güle ‘cannon- ball'; G Kaule “little ball’, cf. Keule ‘club’, Kaul-quappe ‘tadpole’; MHG küle (2) ‘ball, bowl, head’; LG kül ‘club’, kūl-pogg 'tad- pole’; ON kúla ‘knob’; kýli ‘tumour’; R (?) gili ‘redstart; Cz. hýl ‘bullfinch’ beside pa- bel ‘stump’. (For Per. gül cf. also gurd-)
gulg- (gulgu-) ‘gulp, gurgle; belch’. See gul-, gulgul- & glgos Per. (ambig.) gulū (2) ‘gurgle; Arm. cf. klklunk' (redup.), id.; Alb. gullgulloj ‘babble, purľ; Lat. cf. in-gluvies ‘craw’; Ir. glug ‘gurg- le’; MHG kolc, gs -kes ‘whirlpool’; G Kolk, id. cf. Kolk-rabe, wm. ‘caw-crow’; Du. kolk ‘whirl- pooP: OFris. kolk ‘ditch’; Du. cf. kolken, v. ‘ddy’; OE cylcan ‘belch’; Slovak (LW fr. Slovene) gl-gotat ‘gulp’; glg, m. id.; Pol.
305
(variant) gulgotać �
=== leaf 182 ===
 ‘swelling, lump; lumpy, swollen’; gumbstos ‘swollen’. WP I, 562. Cf. gumbhos, ghumb-, 2humb-, etc. (All forms but Gmc. are ambig.) Arm. (ambig.) kumb (knob, hump’, but equally fr. *kumb-, q.v, cf. Skt. kümbah, etc.); Per. cf. gumbed ‘dome; tumbler, glass’; Oss. cf. gumbul “ball of cheese; MHG kumpf ‘blunt’; G cf. kumpfig ‘potbellied’; ON kumpi ‘Jump’; OCS goba ‘sponge’; Cz. houba *fun- gus’; Li. gumbas ‘tumour’ beside gumbstu, gumbti ‘form a lump’; Latv. gumba (fr. Lith.) ‘swelling’. Cf. OCS gostü (‘dense, compact’, fr. *gumbstos) LW in Finn. kumpu ‘hill’, and in Hung. gomba ‘fungus’
gumbulos, gambəlos (gumbh-, gum-) ‘swel- ling’. WP I, 573. See gumb- and next. Oss. gumbul ‘ball of cheese’; Alb. gúmull ‘mass, pile’; OE cumbl, cumul ‘swelling’: ON
gulgul-, gulugul- — gungul-
15
20
25
30
35
40
45
306
kumbl, kuml (1) ‘cairn’; Cz. hemel ‘weft of hair, bun of hair’; Li. guñbulas, gùmulas ‘buri on tree; boil
(gumbhos, see gumb-, gumbulos and next. Gmc. forms include Icel. kubbur ‘stump’; kubba, v. ‘dock’; Sw. kubb ‘block, stump’. Other forms ambig.)
gumbhros (gumuros) *mass'. Cf. gumb-, etc. MHG kumber, kummer ‘rubbish’; G Kum- mer, id. (and ‘rubble’); Frisian: kommer ‘hare’s droppings’; Li. gumbras, gùmuras ‘Jump’
gumulos (guməlos), see gumbulos
gungəros (gungrios) “lump, knot’. See next Arm. knčiř, gs ro Cknot plait, wrinkle’, fr. *gungrio-); E conker; Li. gungaras “hunch- back?
gungos, à (1) “lump, swelling”. See next and cf. gungoros, gunos, gongos, gong-. WP I, 638. (The Alb. & Balt. evidence is ambig.) Skt. gungüh “full moon’; It. gonga ‘swelling of gland'; Alb. gungë “lump, boss, swelling"; gung, adj. “hard; impotent’: Rum. substrate cf. goangá 'dung-beetle'; Norw. kunk 'clod' beside konk (2) ‘tub’; variant in Norw. kong (*boil", fr. *geungho-); E conk “head, lump, fat nose’; cf. OE cynca (tuft, fr. *gungio(n)); Li. günga “lump, boss’; Latv. (alleged) gungis, id.
gungos (2) ‘incoherent, dumb’. Cf. gungos (1) Hind. gungà ‘dumb’; Per. gung, id.; Gk. cf. gogguzo (mutter, fr. *eunguio); Alb. cf. gung “hard to crack, impotent’; Big. cf. gágna *stam- mer; OCS cf. gognavü, -nivü ‘muttering. Hitt. kunk- is a wd. of uncertain meaning. Cf. also Skt. gufijami ‘hum, buzz (: Gk. goggüzo *tmurmur) and OCS gognajo ‘croon’. LW in Alb. gungás, id.
gungul- (1) (gunglos, io) “lump
```


## [2026-09-05T20:39:52.528Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in PHD.txt PHD_mackenzie.txt; do echo \"=== $f ===\"; grep -n -i 'gōy\\|gwd\\|goy ' $f | head -20; done; echo \"=== HRN gūi ===\"; grep -n -i 'gūi\\|güi\\|guj \\|Kugel' HRN.txt | head -30",
 "description": "Look for MP gōy in MacKenzie, Horn"
}
```


### [2026-09-05T20:39:54.435Z] TOOL RESULT

```
=== PHD.txt ===
382:*g5k4n [gwk’n'] details. Lc um ~ig [-yk'] detailed; precisely. (sassa tu) ģūmēz [gwmyc | N giméz] bull's urine (as ritual purifier). ģgūmēz- [gwmyc- | N giméz-] urinate. gön [gwa' | N gün] colour, complexion. ~ag [-k' | M geng, N güna] = gön ; sort, kind, form. gor [gwl | N ~] onager, wild ass. göspand [K YNA < А апу ? ; gwspnd | N ~] (small) cattle, sheep. ~-tihrag [-cyhlk'] holding the seed of cattle. ģūstān [gwst^n!] cattle-stall, cowshed. 1858 [gws | = M, N ~J ear. *GÓ68 [guš | N ~] cal. 14th day. tūšag [gwsk' | N ~a] corner. ģēošūsrūd [rwi^wslwt! = Av. gaošū.srūta-| acquired, learnt. 5051 [BSLYA < A bsr’; рой! | N ~] meat, flesh. ģūšwār [gwštw] | N ~] ear-ring. ģūw-, ~išn, v. ģuftan. gowag [swb k! | М gw'g, N goya] speaking, eloquent; speaker. *ģoūwizār [gwwc'[] explicit, in detail. göy [gwd | N ~] ball. göz [gwc | N ~] walnut. ~énag [gwzynk! | N gózina) a walnut sweetmeat. Gözihr [gwcyhl | Ar. jawzahr] astr. the Dragon. ~ dumb: the descending node of the moon. ~ sar: the ascending node of the moon. grab [22р | P grb] womb. grāmag [gľmk! | P gr’mg] possessions, wealth. grāmig [gľmyk! | M grmyg, N girāmī] treasured, dear. ~ih: affection, respect. 1$raw [giwb! | P grww] cane. *ģraw [glwb' | N giraw] pledge, security. ~ih, ~(a)g4n [glwk’n' | M grug*n, N giraugān] = *graw. grayidan, gray- [gl?d-yin' | P gry-, N gtráy-] lean, incline; intend, desire. ģriftan, gir- [OHDWN-tn' < A V?hd; glptn!, gyl- | M grypt, gyr-, N giriftan, ~] take, hold, restrain. «išnīģ : tangible. griftār [gipt?l | N gir~] held, taken; captive. ~Omand [-'wmnd) tangible. grih [glyh | N girth] knot. lgriw [CWLE < A swr-h; glyw'] neck, throat. ?0riw [CWLE, glyw' | M gryw] self, soul. sgriw [glyw! | P gryw, N girī(b)] a grain measure, modius, peck. griwag [glywk!' | N giriwa] hill, ridge. ģrīwbān [g/ywp?n! | N girībān] neck-guard, gorget. griyistan, griy- [BK YWN-stn'< A У bky; gld-stn! | M gryy-stn, N giristan, giry-] weep, cry.
428:kem [kym] less, fewer; v. kam. кёп [kyn' | = M, N kīn(a)] hate, malice, revenge. ~ig [-yR'] malicious, vengeful. kennār [Rl] lyre, harp. ~-sray [-sPd] harpist. kénwar [kynwl | (M kynw’r), N kinawar] vengeful, vindictive. ««īh: vindictiveness. kër [kyl | N ~] penis. kēsar [kysl] Caesar. këš [kyš | = M, N ~] dogma, faith (especially non-Mazdean). ~-dar [-d’/] sectary, non-Mazdean. keSidan, keš- [k(y)$-ytn! | (M kr$-), N kafidan] pull, draw. Kēwān [kyw’n! | Ar. kaywān] astr. Saturn. kēwūd [kypwt! | M R'ywd] box, ark. kilēl [R]yl | N ktlīd)] key. kirb [klp | M kyrb] body, form. kirbag [krpk' | M kyrbg, N Аја] virtue, good deed. ~ig [-y%!] virtuous, pious. kirbakkar [krpkkl | M kyrbkr] beneficent. ~ih: beneficence. kirih- [OBYDWNyh-, v. kardan, kiyh- | M kyryh-] be done, made. kirm [kim | M krm, N —] worm, serpent. kirrénidan, kirrén- [klyn-ytn'] rend; create (daevic). kirróg [k(y)lwk! | M grwg] artisan, craftsman; skilled. ~th: arts, crafts, craftsmanship, skill. kiš [k(y)š | M АЎ, N ~] furrow, line. kišnīz [kšnyc] = gi$niz. kištan, kar- [ZL Y TWN-tn! < А У ar; kyštn!, Pl- | M kyšt, kis- N ~] till, furrow; sow. kištār [ZLY TW NTt'l] tillage. kišw, ~4n [kysw', x! | P Аун] tillage. ~(an)zar [-c?/ | (N kištzār)] field. ki$war [Rystol | M kyswr, N ~] region, clime, continent. kišwzār, v. kišwānzār. kūb-, v. koftan. kódak [kxwtk! | M gwdk, N ~] young, small; baby. kof [kwp | = M, N koh] hill, mountain; hump. ~ag [-4! | N Абла] saddle. ~ig [-yk! | N kēkī] wild, mountain-. koftan, kūb- [kwp-tn' | N ~] beat, pound, crush. kör [kwl | M kar, N ~] blind. ~-dil [-dyl | M -dyl, N ~] blind-hearted, incorrigible. kūstan [kwstn' | = M, N ~] beat, pound. kūš-, v. kóx&-. kēšk [how fA! | N ~] pavilion, palace, kiosk.
542:~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
=== PHD_mackenzie.txt ===
2559:goy [gwd I N -] ball.
4034:pargiid [plgwt l I P prgwdg] , ,...., az: free, exempt from.
11407:ubrozisn             't"\)~~ GoY       afl'ah                        ~Q)'
=== HRN gūi ===
3804:LW. kurd. tlr, tlrek; bei. ttr, n. fir *Pfeil, Kugel'
8051:929. ffuJüle 'Kugel', (/öle.
8195:kurd. güi, güse 'Winkel*; bei. LW. gösak (127).
18196:güiifali 489.
```


## [2026-09-05T20:40:00.858Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8040,8060p' HRN.txt; echo \"=== grep gui/goi ===\"; grep -n 'gūi \\|gūi,\\|güi \\|Ball' HRN.txt | head -20",
 "description": "Horn 929 gulule"
}
```


### [2026-09-05T20:40:00.938Z] TOOL RESULT

```
AM. 168 Zeile (>), vergl. arm. Vardges, phlv. N.
pr. Vardakl (Gemme, Hörn, Mitteilungen, Heft IV,
34); gr. Qoäoy, lesb. /J^'Jor.
927»»*« gil 'Schmutz. Lehm'.
arm. kir Xehm' (Fr. Müller, WZKM. 5, 268)2).
928. guia, gelü (AM. 109 Zeile 1 v. u.) 'Kehle .
aw. garah' 'Kehle'; phlv. garük vd. 15 (11); skr.
gala-; lat. gula; arm. vergl. -kul '-verschlingend' (H.
No. 145), ker 'Nahrung, Frass' etc. (H. No. 143).
kurd. gerü 'Kehle'; af}'. yäre; oss. gm' (166; un-
sicher); sangl. yar,
929. ffuJüle 'Kugel', (/öle.
Käs. gtdi, gulla,
Vergl. ai. gldv- 'Ballen, kropfartiger Auswuchs';
ykovTog 'Ballen, Rundung (NB. so nur bei Fick, sonst
'Hinterbacke, Gesäss'); ags. cleoven, ahd. chlluwa
'KnäuV,
Am Genauesten entspricht nhd. Knaul (für Kläuel
wie ndd. Mid für klmi, vergl. engl, crewl, Fick"*, 412).
Ein Suffix 'le mit verkleinernder Bedeutung will
Darmesteter, Et. ir. I, 298, in np. merdle erkennen,
=== grep gui/goi ===
4129:449. eögän 'Schläger (im Ballspiel)'^).
4157:bei Firdüsl vom Ballspiel die Rede ist (The Game of Ball-Bai -- Chowgän-
8053:Vergl. ai. gldv- 'Ballen, kropfartiger Auswuchs';
8054:ykovTog 'Ballen, Rundung (NB. so nur bei Fick, sonst
```


## [2026-09-05T20:40:09.398Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'گلوله' MON_part1.txt MON_part2.txt | head -10; echo \"=== kalach ===\"; grep -n 'کلاچ' MON_part1.txt MON_part2.txt | head -10; echo \"=== kolob ===\"; grep -n 'کلوب' MON_part1.txt MON_part2.txt | head -10; echo \"=== golbul ===\"; grep -n 'گلبول' MON_part1.txt MON_part2.txt | head -10",
 "description": "Grep Mo'in for the four Persian words"
}
```


### [2026-09-05T20:40:09.496Z] TOOL RESULT

```
MON_part1.txt:2066:ت در کردن گلوله از تفنگ و توپ. 
MON_part1.txt:5303:است مشکل از گلوله‌ای سک وزن 
MON_part1.txt:20698:رشتن گلوله کرده باشند؛ پنبهٌ زده شده؛ غند» 
MON_part1.txt:25389:بنحک: ۱۵00 .۲ ینب گلوله کر ده نه 
MON_part1.txt:25563:حلاجی کرده و گلوله ساخته به جهت رشتن. 
MON_part1.txt:29867:گلوله‌ای از خمیر که به جهت پختن نان 
MON_part1.txt:29870:گلوله از اندازه بزرگتر باشد. آرد خشکی که 
MON_part1.txt:30829:باروت و گلوله یا نشنگ در آن نهادن. پر 
MON_part1.txt:31476:بجول» پجول. گلوله‌ای که طفلان بدان بازی 
MON_part1.txt:33560:گلوله‌ای را با راکت به سوراخی داخل کنند. 
=== kalach ===
MON_part2.txt:24509:کلاچ فر هنک فارسی معیر ۱۳۷۵ 
MON_part2.txt:24520:از حرکت باز می‌دارد. پدال کلاچ: آلتی 
MON_part2.txt:24522:دارد و راننده به وسیلهٌ آن کلاچ را بکار 
=== kolob ===
MON_part1.txt:20615:آن گرد آیند؛ کلوب. 
MON_part2.txt:25456:کلوب: «تاه۲ (ا.) باشگاه» انجمن. 
=== golbul ===
MON_part2.txt:34333:دو نوع گلبول‌های قرمز و سفید موجودند. 
MON_part2.txt:34334:گلبول‌های قرمز خصوصاً در خون جانوران 
MON_part2.txt:34342:مکعب در حدود ۵ میلیون گلبول قرمز 
MON_part2.txt:34343:وجود دارد. گلبول‌های سفید خون به منز لا 
MON_part2.txt:34346:۰ گلبول سفید موجود است‌که برخی 
MON_part2.txt:42881:مستقیماً گلبول‌های قرمز خون را مورد حمله 
MON_part2.txt:64505:که در آن گلبول‌های سفید شناورند. این 
MON_part2.txt:84316:مشخصات مهم آن این است که گلبول‌های 
MON_part2.txt:84318:حالی که ویبریون وبای معمولی گلبول‌های 
MON_part2.txt:87677:ویتامین ۸ در بدن سبب کم شدن گلبول‌های
```


## [2026-09-05T20:40:14.482Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== kalach ===\"; sed -n '24505,24525p' MON_part2.txt; echo \"=== klub ===\"; sed -n '25450,25462p' MON_part2.txt; echo \"=== golbul ===\"; sed -n '34325,34340p' MON_part2.txt",
 "description": "Mo'in entries context"
}
```


### [2026-09-05T20:40:14.561Z] TOOL RESULT

```
=== kalach ===
«السامی‌فی‌الا سامی» در معنی «دسگره) کلاته 
را آورده و در شرح سامی « کلاته» چنین 


کلاچ فر هنک فارسی معیر ۱۳۷۵ 


معنی شده: رهو نناء شبه قصرء حوله ببوت.» 
(فر.نظا.) 

کلاج: ۵ (.) (مکد.) آلتی است در 
اتومبیل که به وسیلةٌ آن راننده با اتصال وی 
به موتور نیروی دوران سوتور را به جعبة 
دنده و چرخ‌های اتومسل انتقال می‌دهد» 
همچنین با انفصال آن از موتورء» اتومییل را 
از حرکت باز می‌دارد. پدال کلاچ: آلتی 
است که زير بای چپ راننده اتومبیل قرار 
دارد و راننده به وسیلهٌ آن کلاچ را بکار 
می‌انداز د. 

کلارینت: ۰2:10 (.) (سد.) یکی از 
=== klub ===

۱۳۸۵ 


کلوا: ۲0۱۷2 [استاد رخنه گر ] (ا.) رخنه گرفتن 
و وصل کردن چیزی به چیزی دیگر. 
کلوب: «تاه۲ (ا.) باشگاه» انجمن. 
کلوینده: (0-)۱۲-02:۱012ا0! [ - کلو نده] (امر .) 
بز رگ بندگان» مهتر غلامان. 

کلو تک: (قد. -1)15 ,اداناا! (.) چوبی 
باشد که گازران و دقاقان جامه را بدان دقاقی 
کنند؛ کدنگ. 
=== golbul ===
یک از برگک‌های یکث گل؛ ۳ 
همجون برگک گل. (کن.) معشوقه‌ای که 
بدنش مانند برگک گل لطیف و نازک باشد. 
(کد.) چهره» رخساره. 
گلبن: 00و زگل سرخ | (امر) بیخ بو گل. 
بوت گل؛ ج . گلن‌هاء کلبنان. بوتهٌ کل سرخ. 
گلسول: (تد.هع)-انااهامي (یز.) (۱.) هر یک 
از سلول‌های موجود در خون جانوران که به 
دو نوع گلبول‌های قرمز و سفید موجودند. 
گلبول‌های قرمز خصوصاً در خون جانوران 


گلبام فرهنگ فارسی معین ۱۸۳ 


دارای مادة آهن موسوم به هموگلوبین
```


## [2026-09-05T20:40:35.077Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'گلوله:' MON_part1.txt MON_part2.txt | head; echo \"=== گله gulle ===\"; grep -n 'گلة\\|گلّه:\\|گله:' MON_part2.txt | head",
 "description": "Mo'in golule headword"
}
```


### [2026-09-05T20:40:35.146Z] TOOL RESULT

```
MON_part1.txt:89889:و جز آنها) سوت. صفیر گلوله: صدایی که 
=== گله gulle ===
34809:گله: «م)«(0)ا (.) رم چارپایان (گوسفند 
34832:گله: : (۵-)01۵ج (, ) (عم. .) گو شه. 
35751:گواره: (ه-)«<سي (ا) گلةً گاو و گاومیش.
```


## [2026-09-05T20:40:37.549Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '34795,34860p' MON_part2.txt",
 "description": "Mo'in around gulle/golule"
}
```


### [2026-09-05T20:40:37.593Z] TOOL RESULT

```
تفا ای تست سيسات وله 
مشسقی: (نظ.) گلوله‌ای که برای مشق و 
تمرین بکار می‌رود ولی قدرت تخریب 
ندارد. لول منور: (نظ.) گلوله‌ای است 
مخصوص خمیاره اندازها. 
گلوله باران: 2720 رامر.) (نظ.) ریزش 
کلو له‌های سیار و متوالی (توپ» تفنگ و 
غیره) بر مواضع دشمن. 
گلوند: سای | - گل ۳ + ند 
قس. گلونده| (امر.) گلوبند. هر چیز که به 
بق تحفه و هدیه به کسی فر ستنده مر سله. 
گلونند مانندی از گردو و انجیر که آن را به 
هد به فر ستند. 
گلوه: (۵-)0۱۷۸ع ( () سوراح تنور نان یزی. 
گله: «م)«(0)ا (.) رم چارپایان (گوسفند 
وی وت 
کله (۵-)«ا۵ج ( ) اظهار دلتنگی و عدم 
رضایت» شکایت» شکوه. ضعح.- در تداول 
ابر وز گله با شکایت تفاوت گونه‌ای دارد: 
کله شکایت نرم و ملایم بود از دوست نزد 
خود او یا دوستی دیگر که با هر دو طرف 
دوست است ( پس ج 
گله (ن)«اع ( .) دانه انگور که از خوشه 
جدا شده باشد. 


کله (۵-)۲۵1۸ (.) راهی که در مبان دو کوه 


واقم شده باشد 

9 (0-) ۲01-3 (قس. گللاله ] (ا. ) زلف بیجید ه 
و مجعد زنان چون موی زنگی. 

کله (ه-)2-]هي (ا.) پارچه‌ای که بر سقف 
خانه‌ها مانند سین فان نت اسان کیره 

گله: : (۵-)01۵ج (, ) (عم. .) گو شه. 

کله : (-)01۸ج (ا.) توده (هر چیز). 


1 
ُ 
1 
۱ 
۱ 
۱ 
۱ 
۱ 
1 
۱ 


گله‌بان 
گله‌بان: -(۵-)۱(2) اد (ص‌مر. امر.) 
نگهبان گله و رمه؛ شبان» چوپان. 
کله‌دار: 2۰-1 [- گل‌دارنده| (ص‌فا.) 
صاحب گله ( گوسفند و غبره)» آنکه گل را 
نگهبانی کند و پرورش دهد. 

که کردن: ۱ (0-)۱اع (مص‌ل.) 
شکایت کردن؛ شکوه کر دن. 

کله کننده" (0-)00۱2002:-.ي (ص فا.) آنکه از 
کسی يا چیزی شکایت کند؛ شاکی؛ ج.
```


## [2026-09-05T20:40:45.354Z] TOOL CALL #25: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1861 2>&1 | head -60",
 "description": "Fetch BQT page 1861"
}
```


### [2026-09-05T20:40:53.007Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 656; check the printed number and re-run with --pdf-page if off)
REF: BQT:1861  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 656  OCR-lang: fas

-۱۸۵۹- گ و کرد
گوش .* اس ت که بچِه‌گاو باشد 8 .
موشهٌ باغی گرفتن «- کنابه از گل و گار ۱ - با کان فارسی بر وزن
گوشه‌شنی وخلوت کزبدن باشد . 5 جالوری است گه نام
8 8 ی و بخرداند وغلطان غلطان بوراخ خود بردو
ود بالش * کنایه‌از کوشه و کنار عربان خنناء میگوشد .
مسند باشد . ۱ ال ۷ (۱) سرروزن کوبال» بمع
وه جام شکیته - کنابه از وال بروزن کوپال» بممتی
۹ : ۱ کوکار اس ت که سرکین
هاه لو باشد هلال گوبند . ۱ 3 گردانك باشد و عربان
گوشیار ۱ - بر وزن هوعبا .۸۸ | / )۹ خنناءکوشش (۷) ۰
حکیمی بوده ازفاری وشیخ ابوعلی‌سینا شاکردی | ۸ 1 گ و گرد* - بکس
اوکرد.۴ . 1 کاف فارسی وسکون‌را ودال
کول - بنم اول و سکون انی مجهول | ار ۴ بی‌قطه, جوهریست که‌آترا
وکاف فارسی » بمعنی تکمه گریبان باشد و آترا کبريت‌هم میگوبند و آن
کوی گریبان هم میگوبند ۴ - ودانهای سختی ک وکال چهار لوع میباشد : سفید
که در اعضا بپم میرسد و درد نمیکند و عربان |[ وزرد وسرخ وسیاء؛ وبعضی کوبندچشمه‌ایست‌روان
تولول خوانندش ۴ - و بمعنی کوماله هم آمده چون منجمد گردد کبریت شود ؛ و بسن ی کوبند

(۱) چش : گوکال . (۷) چك : میگوشد ؛ چش : - و عربان ... گوبندش .

۱ - اصح همین صورت است پمنی با کاف پارسی » از :کوش ( نام فرشته ) (۸.م.) ۳
بار ۱ پسوند میدل ای داد بمعئی داده 1 قی : بهمنیار آسپند بار ۰ هرمزدیار ( و ابوالس نکیا
کوغیارین لبان باغهری کیلانی منجم بز رکه » وی درليمهٌ دوم قرن چهارم‌هجری میزسته ومژلف
« زج جامع » و «زیج بالغ» و «مجمع‌الاسول» است . رك : کوشیارگیلانی بقلم نگارنده در نامه
فرهنگه, چاپ مشهد سال‌اول‌شمارة ۵ ۴.۲۰۸۲۰ - ظ.با «بهمتیار» که شا گرد این‌سینا
بوده (نه بعکس) خلطشد.. ولی اوآذربایجانی است . ای شکل‌قدرم +: کو, کوی (ه.م.).

ای < کوکه (و.م.) ه‌ <- کوکه («.م.) طبری عا۵ع (کوساله ( ‌ واژه نامه
۵۹4 رك :کاو کو . ‎٩‏ ** کوکال (۸.م.) . قس : اوستا ۷8۳618 801108 ,که درتضیر
دوم همرشه وبمعنی گردیدن وگرداندن‌است. لغة بمعنی‌سر کین گردان(ه.م.) ورلك : گ وگردادك.
ورك : ح۹ ۰۱۸۹۲ ۷ کوکار (هم.) . ۸ - دراوراق مانوی پپپلوی 8۷8776
«کوکرد . -ولفور» ,1 ,آ7 ,8505 , ...868188 ۸/4616 01 اقنا ۸ موصندد01)

3 . 0 ) ک و گرد (ع50۱۷۲۲ فر) جمی است بیط و جامد » برنگه زرد لیموی » ی‌مزه دی
.۰ وزن‌مخصوصآن ۱1۹۰ است ودره/۱۱۶ درجه ذوب میشود ودر 141۰ درجه بجوش‌میا ید.
کوکرد در طبیعت بوفور بورت سولفورها با سولفاتها . با بصورت اصلی خویش درحوالی کوهپای
آتشفمان یافت مشود .

۵ وشه - پم اول وکسر سوم ( در لهجهٌ مرکزی ) و بفتح آن ( در تلفظ قدیم ) ‎٩‏
‏اوستا - 38808268 ۰ کردی 02ع . 80956 . بلوچی ع 6ا8طظ8۵9 . کاشانی 8۵506
۰ آسشتق ۵ کنج » زاوبه - خلوت , خلوتگاء پکناره کناره - دستهٌآوند - دکمه, گره.
```


## [2026-09-05T20:41:05.551Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && ls -la; wc -c BQT_v3_pages.txt BQT_v4_pages.txt 2>/dev/null; grep -n 'گلوله\\|گلله\\|گوله' BQT_v3_pages.txt | head -20",
 "description": "Check BQT v3 pages text"
}
```


### [2026-09-05T20:41:05.614Z] TOOL RESULT

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
2499427 BQT_v3_pages.txt
2055176 BQT_v4_pages.txt
4554603 total
2660:‏)\( چش : شبگوله ۰
7079:. ‏شنگه‎ ay ٩٩۳ ‏شنگوله رك: لفت فری ص‎
7134:شنگوله ۸ - با وار مجهول بی وزن
7135:زنگوله ‎goer‏ شنگول است که شوخ وظریف
7500:نی بچگوله بکار پاید فرمود - و کی را نیز
13787:حر اعتا را نیز کوبند ‎OT,‏ مانند گلوله درگردن
18036:خثشرپاونهای خود را در ابجاد اینگونه باغها در فلمرو حکومت خود تشویق میکردند . اینگوله
26349:جنبانیدن مهرء و گلوله باشد در ‎Ole‏ طاس‌رامثال
34109:۳ کلاه زنگوله «+فرهنگه ‎pls‏ © :
35649:وآن ‎de‏ طفرا باشد ۴ ۰ کمان قروهه است که کمان گلوله باشد ۷ ۰
35662:که قوی قزح باشد . اندازی است که کمان گلوله باشد .
37522:و گوله وطرز وروش باشد ‏
38745:آسیب رسیده وآزار کشیده باشد - و گلولهای
46303:‏گلوله ۴ - بروزن و معنی غلوله‌است
47348:۸ - به رگوله بوی و ‎aS se‏ رنگه نکوتر بیارای آن شنکه کنگه.
48975:لیز کوشد عموماً ؟ بو گلوله‌ای که‌ازچوب‌سازند
49026:۴ -کردی 80 ‎go.‏ ) گلوله‌های بازی .کرء ) « ژابا ص ‎COW‏ -کوی در التفهیم
49087:س رکین را گلوله کند و بغلطاند و ببرد و بعریی
```


## [2026-09-05T20:41:11.125Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'NR<=46303 && /\\[pdf page/ {p=$0; n=NR} END{}' BQT_v3_pages.txt; grep -n '\\[pdf page' BQT_v3_pages.txt | awk -F: '$1<46303' | tail -3; echo \"---\"; sed -n '46280,46330p' BQT_v3_pages.txt",
 "description": "Locate golule in BQT v3"
}
```


### [2026-09-05T20:41:13.342Z] TOOL RESULT

```
46112:[pdf page 627]
46188:[pdf page 628]
46284:[pdf page 629]
---
‏اسردهان نپیش چ وکل مهره در تفك .
سوزلی سمرقندی « لباب‌الالباب‌ج+ص۱۹۵ .
۷ - رك : رشیدی

[pdf page 629]
BY ‏بنم اول و فقح‎ - ۱ om
‏و سکون ثالث ؛ ت رکیبی باشد مانند کل فند‎
‏کهگل قند را با کل و قنه‎ CT ‏لیکن ناوت‎
‏سازیت و کلنگبین را با گل و انگبین که صل‎
. ‏باشد‎
‎. ‏اول و ثانی بواو کشیده‎ ce - ۴ ‏گلق‎
‎. ‏و حلفوم باشد‎ gle ‏ممروق است که‎

گلق 4 - منم اول وفتح قرقانی وظهور
ها » کلاهی باشد گوشه‌دار پرینبه که بیشتربجهت
طفلان دوزند و کوشهای آنرا در زبرچالةً ‎lel‏
‎was‏ و وجه تسمیه‌اثر, خود ظاهر است.

‎IF‏ - بفتح اول‌بروزن تموز » ببعنی
‎Gus‏ باشد ۴ ؛ و بسی گوبند. چلغوزه(۱)است؛
و ‎cee‏ بادام کوهیرا کفته‌اند اقا علم» ومعرب‌آن
جلوز باشد +

‏گلوله ۴ - بروزن و معنی غلوله‌است
‎Sng SUS”‏ رسمان وغیره باشد .

‏لو فد * = بنتح اول پروزن فرزند »

‏(۱) خم۱: جلفوزه .

‏مرسله رااکویند عموماً بمنی هرچیز که بطریق

‎۳۲

‏تحفه و ‎Aye‏ بجابی فرستند - و چیزی باش که
‎LT‏ مانند گلوبند از جوز و انجیر سازندویجایی
فرستند خصوصاً وآ ترا کلونده لی ز گوبند - و نام
کوهی لیز هست .

‎ps BU ‏اول و سکون‎ pa = OF
. ‏الث » سوراخ تنور نان پزی را گویند‎

‏گلوی ‎Qo T‏ = مورا وسط آسیا را
‎ue‏ دانه از آن راء ریزند تا آی‌گردد .

‏گلوی ‎ers Ee‏ روده راگویند
و آن محلگذشتن آب ودانه است .

‎UF‏ = بفتح اول و ثانی مشدد وغیرمشدد
هردوآمده است » بمعنی کله ورمة گوسفند وشتر
وخر و کاو وآهو و امثال ‎ath OT‏ - وبضم اول
```


## [2026-09-05T20:41:26.678Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk '/\\[pdf page 658\\]/,/\\[pdf page 659\\]/' BQT_v3_pages.txt | head -70",
 "description": "BQT v3 pdf page 658"
}
```


### [2026-09-05T20:41:28.381Z] TOOL RESULT

```
[pdf page 658]
را

بازی کردن و خواه بز رکه باشد از برای توپ
ومنجنیق ‎٩‏ - و پمعنی خاریشت هم آمده است-
و کوزة آیخوربرا نیز گویند ۴
گق۵ - بر وزن موم ۰ ‎ALS‏ است
خوشبوی و آترا بعربی ازخ رکویند .
گومصت ؟ = بنتح اول وسکون نا
‎ce‏ اول وسکون انی
و لر میم وسکون سین بی‌نقطه و فوقالی ۰ نام
کتابی است که بر پیغمبر مجوسان که جومست

دام داشت فرود آمده ‎oy‏ .گویند ‎OT‏ کتاب را
هفتاد شتربرمیداشت مجوسان‌آن پیغمبررا کشتند

وآن کتاب را سوختند .

گومشون  ‎pa‏ اول و ‎wt Ose‏
و ‎od‏ الث و شین فطه‌دار بواو کشیده و بنون
زده + بزبان زند و پازند بمعتی آوشان و ایشان
وآنها باشد ۴ .

گو‌هن ‎٩‏ = بروزن سوزن » بلت زند
و پازند بمعنی این باشد و بعربی هذا کوبشد .

گوهه ۱ - با ‎gt‏ مجهول وقتح ثالت,
خاله‌ای را کویند که ازنی وچوب وعلف سازند.

گت « بنم اول و سکون ‎Gi‏ و لون,

Bolla stat (po) ‏کلوله‎ =

جومست
6 . قس : گومن .

Cpa) gM

‎(ps) eat‏ س غلك(هم.)
‎ee‏ هزوارش ‎avéshan‏ پپلوی (ابشان) 1۹080" است. ‎J)‏ لیب رکه ‎Noe‏
‎gdm(a)n. » ۵‏ . پهلوی 60 ( اين ) « بونکرس ‎V8‏
‏۲ - پهلوی 800 > تاوادبا ۰۱5۱ و 8002 اوستا

‏کونجی
‎caw‏ رنگ ولون باشد ۷ چ هکلگو ‎SM‏

‏راگویند - و بمعنی طرز و روش وقاعده وفالون
و صفت لیزآمده است - و بضم اول ‏ و کسر ‎tall‏
‏نام شهری است از شهر های فاری و معرب ‎OT‏
‏جون باشد ۸ .

‏گو نا * = ‎en‏ اول و نون‌بالف کشید»,
‎yom‏ گونه و رنگه ولون‌باشدچه کون گونبمعنی
‎NG,‏ است *9- و غازه‌ای که زنان بر روی
‎aL‏ ۷۱- و پمعنی طرز وروش وقاعده و قانون
و صفت هم‌آمده است ‎VF‏ و بلفت زند و پازند
بچه و بر کوسفند راگوند ‎OM‏

‏گو اب - بر وزن خوناب ؛ سرخی
وگلگوهه‌ای باشدکه زنان بجهت زببابی‌بررخسازه
‎Fadl‏

‏گو نا گون ‎oO‏ بمی‌رنگارنگگ‌است
که جنس بجنس و ‎A‏ باشد .

‏گو نجی ۰۱۷ بنم اول و کر شا
وسکون نون و شتا کید ‎HP ae!‏
وکرامی ‎ath‏ - و بمعنی شجاع ودلیر و پهلوان
‎oul‏ است
```


## [2026-09-05T20:41:44.917Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk '/\\[pdf page 629\\]/,/\\[pdf page 630\\]/' BQT_v3_pages.txt | tail -40",
 "description": "BQT p.1832 footnotes"
}
```


### [2026-09-05T20:41:49.654Z] TOOL RESULT

```
و آن محلگذشتن آب ودانه است .

‎UF‏ = بفتح اول و ثانی مشدد وغیرمشدد
هردوآمده است » بمعنی کله ورمة گوسفند وشتر
وخر و کاو وآهو و امثال ‎ath OT‏ - وبضم اول
و فتح ثالی مشدد ۰ آسمان گیری باشد و ‎OT‏
‏پارچه‌است که برسقف خالها ماشدسایبان ‎was‏
‏و موی جمم شده را ی زگوبند ‎٩‏ - و بضم اول
وفتح‌انی‌غیرمشدد. زلف معشوقرا میگوبند ۲ -
و بکس اول و فتح انی مخفف » شکوه وشکایت
‎Vast‏ - و ‎Bly‏ الگور که از خوشه جدا افنادء

‏۱ - از :کل ‎ge)‏ اول) +-انگیین (هم.)

‏۴ - دراوستا 88780 (کلو) « پهلوی 8270 ؛ سانسکریت -8818 لاتینی ‎gula‏
‏قی ارمنی لا - ( فروبرده » بلعیده ) .کردی 86۳0 ‎ghara gust.‏ و ‎gharai‏ (کردن»
‎(ay Minas‏ استی 0105 ( غیر قطمی ( ستگلیجی ‎ghar‏ «اسشق - هوبشمان ‎ATA‏ خواناری
‎geli‏ , دزفولی 8011 » سالنامةٌ گلپایگان ‎gull AS. » ty‏ ء کردی 2060۲0 , ‎gheOri‏

‎. ‏جلوز(معرب)‎ =F ale Llp 82۷1 , geryu. 88۷71 , ‏معبر تنکه)‎ , (lS)

‎gldv_ ‏غلوله . قس : هندی‌باستان‎ « ۴ . ۲۱۰ at » Corylus avellana =

‎PAYA ‏اسشق - هوبشمان‎ : Sy. ( ‏(کلوله‎ gul6k . (55) ‏لنگه) .655 ۲ثااناع‎ » Sue)

‏اضاکردی 1101 ( لوله , غلطیدن . سفوط سخت ) « ژابا ص ۰۳۸۱ ؛ ابضاً کردی 201016

‏(کلوله ) « ژابا ی ۳۹۵ ۰ .

‏۱ -کردی 801 ( زلف زنان , دستة موی ) . زازا ‎gill‏ « ژابا س ۳۷۰ افی: گلاله.

‎JC: ( girzak ‏از 6۵1۳0021 از‎ . gila ‏پازت‎ . 6 ck: ( gilak ‏پپلوی‎ - ۲

‏جنوب غربی ) ۰ از -08728-168 از ( اوستایی ) 88762 < بارتولمه ۵۱5 » < نیب رگ س۸۱*.

‎. ) ‏شکایت‎ ( gill ‏باستان - 8871 , 887108168 ( شکایت کردن . عارش شدن ) , کردی‎ was
. ۰ ٩۳۰ ‏ناله کردن ) « اسشق‎ ( 887210 , ghérzum ‏دعوی ) , استی‎ ( ۴

‏- رك : رئیدی .
[pdf page 630]
```


## [2026-09-05T20:42:05.447Z] TOOL CALL #30: Bash

```json
{
 "command": "ls site/pages/169.jpg 2>/dev/null; pdftoppm -f 169 -l 169 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg169 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 169"
}
```


### [2026-09-05T20:42:07.688Z] TOOL RESULT

```
site/pages/169.jpg
total 17232
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:42 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  752374 Sep  5 16:12 bqt362_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  624515 Sep  5 16:12 bqt362.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 1032029 Sep  5 16:13 bqt362_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  385716 Sep  5 16:13 bqt363_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  338175 Sep  5 16:13 bqt363_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  692415 Sep  5 16:13 bqt363.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62948 Sep  5 16:36 build134.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50861 Sep  5 16:34 build148b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80793 Sep  5 16:15 pg131.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46793 Sep  5 16:20 pg133.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66991 Sep  5 16:16 pg135.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45014 Sep  5 16:12 pg137.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63658 Sep  5 16:13 pg144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60631 Sep  5 16:11 pg147.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81770 Sep  5 16:20 pg148.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72186 Sep  5 16:30 pg149.png
-rw-rw-r-- 1 sfmqrb sfmqrb  131595 Sep  5 16:32 pg151_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154426 Sep  5 16:36 pg152_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62516 Sep  5 16:35 pg152.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169880 Sep  5 16:34 pg158_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168057 Sep  5 16:34 pg161_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76745 Sep  5 16:34 pg161.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61265 Sep  5 16:40 pg165.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68420 Sep  5 16:42 pg169.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T20:42:10.567Z] TOOL CALL #31: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg169.png"
}
```


### [2026-09-05T20:42:10.971Z] TOOL RESULT

```

```


## [2026-09-05T20:42:10.967Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:42:30.384Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"club, n\" \"clutch, tr\" \"globe, n\" \"glue, n\" \"globule\" \"clay, n\"; do echo \"### $w\"; grep -n -m2 -A4 \"^$w\\|[^a-z]$w\" KLN_1971.txt | head -20; done",
 "description": "Klein entries"
}
```


### [2026-09-05T20:42:32.249Z] TOOL RESULT

```
### club, n
### clutch, tr
49399:clutch, tr. and intr. v., to seize with the hands. — 
49400-ME. clucchen , clicchen, fr. OE. clyccean, ‘to 
49401-bring together, clench’, rel. to OFris. kletsie, 
49402-‘spear’, Swed. klyka, ‘crotch, fork’, and to E. 
49403-cling (q.v.) 
### globe, n
103491:globe, n. — F., fr. L. globus , ‘a round body, ball, 
103492-sphere’, in gradational relationship to L. glaeba, 
103493-gleba, ‘clod, soil, land’. See glebe and cp. words 
103494-there referred to. Cp. also globose, globule, con- 
103495-globate and the second element in hemoglobin. 
### glue, n
103770:glue, n. — ME., fr. OF. (= F.) glu, ‘birdlime’, 
103771-fr. Late L. glutem, acc. of glus, fr. L. gluten, of 
103772-s.m., which derives fr. I.-E. base *gleit-, ‘to 
103773-glue, paste’, whence also Lith. glitiis , ‘sticky, 
103774-glutinous, smooth’, glytits, ‘smooth, even’, 
--
160908:glue, n., and cp. glioma, 
160909-neurology, n., the study of the nervous system. — 
160910-Prob. coined by the English physician Thomas 
160911-Willis (1621-75) fr. neuro- and Gk. -Xoyia, fr. 
160912--X6yo?, ‘one who speaks (in a certain manner; 
### globule
103494:there referred to. Cp. also globose, globule, con- 
103495-globate and the second element in hemoglobin. 
103496-Globigerina, n., a genus of Foraminifera {zool.) 
103497-
103498-— ModL., compounded of L. globus, ‘a round 
--
103511:See globule. 
103512-
### clay, n
48428:clay, n. — ME. clei , clai, fr. OE. clxg, rel. to OS. 
48429-klei, Dan. klxg, MDu. clei, Du. klei, LG. 
48430-klei (whence G. Klei), ‘clay’, OE. c lx man, 
48431-ON. kleima, OHG. klei men, ‘to cover with clay, 
48432-besmear’, OHG. kliwa, klia, MHG. klige, kite.
```


## [2026-09-05T20:42:36.277Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -m3 -A8 '^club, n' KLN_1971.txt | head -30; echo \"=== globule ===\"; grep -n -m2 -A5 '^globule' KLN_1971.txt; echo \"=== glebe ===\"; grep -n -m2 -A10 '^glebe' KLN_1971.txt",
 "description": "Klein club, globule, glebe"
}
```


### [2026-09-05T20:42:36.375Z] TOOL RESULT

```
=== globule ===
103513:globule, n., a very small spherical body; a drop. 
103514-
103515-— F., fr. L. globulus, ‘a little ball’, dimin. of 
103516-globus. See globe and -ule. 
103517-
103518-Derivatives: globul-ar, adj., globulin (q.v.), glo- 
--
103527:globule. 
103528-
103529-globulous, adj., globular. — F. globuleux (fem. 
=== glebe ===
103275:glebe, n., soil; land; field. — L. gleba , fr. earlier 
103276-glaeba, ‘clod, soil, land’, in gradational relation- 
103277-ship to globus, ‘ball, sphere’, and cogn. with Lith. 
103278-glebys, ‘armful; clue, ball’, gldbiu , gldbti, ‘to 
103279-embrace, support*, Lett, glabt, glebt, ‘to pro- 
103280-tect’, Polish globtf, ‘to press', Czech hlobiti, ‘to 
103281-fasten with tags’, OHG. klaftra , MHG. klafter , 
103282-G. Klafter, ‘fathom’, lit. ‘the outstretched arms’, 
103283-OE. clyppan , OFris. kleppa , ‘to embrace, love’, 
103284-fr. I.-E. base *gelebh-, *glebk-, ‘to roll up into 
103285-a ball, compress’, which is an enlargement of
```


## [2026-09-05T20:42:42.243Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'club, n' KLN_1971.txt KLN_1966.txt | head; echo \"---\"; grep -n 'ON. klubba\\|klubba' KLN_1971.txt SKT.txt | head",
 "description": "Klein/Skeat club"
}
```


### [2026-09-05T20:42:42.317Z] TOOL RESULT

```
---
KLN_1971.txt:49330:dub, n. — ME. clubba, fr. ON. klubba, klumba , 
KLN_1971.txt:49356:klumba, klubba , *a thick stick, club*. See clamp
```


## [2026-09-05T20:42:45.649Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '49325,49365p' KLN_1971.txt; echo \"=== cling/climb/cloud/clump ===\"; grep -n -m1 -A6 '^cloud, n' KLN_1971.txt; grep -n -m1 -A6 '^climb, intr' KLN_1971.txt",
 "description": "Klein club/cloud/climb"
}
```


### [2026-09-05T20:42:45.747Z] TOOL RESULT

```
‘nail’, fr. L. cldvus . See clou and cp. words 
there referred to. 

Derivatives: cloy-er , n., cloy-ing, adj., cloy-ing- 
ly, adv., cloy-ing-ness, n. 
dub, n. — ME. clubba, fr. ON. klubba, klumba , 
‘a thick stick, club’. See dump and cp. words 
there referred to. 

Derivatives: club, tr. and intr. v., clubb-able, 
adj. (a hybrid), clubb-ed , adj., clubb-er, n., clubb- 
ish, clubb-y, adjs. 

duck, intr. v. — Of imitative origin. Cp. OE. 
cloccian . , Dan. klukke, Du. klokken, MHG. 
klucken , MHG., G. glucken, Gk. xXc 2 >£etv, 
xXwaoeiv, L. glocire , ‘to cluck’, which all are 
imitative. Cp. also dutch, ‘brood*. 

Derivative: cluck, n. 
due, n. — The same word as dew. 
clumber spanld, clumber, n. — Named after one 
of the estates of the ist Duke of Newcastle. 

dump, n., a heap, mass. — MLG. klurnpe, klom- 
pe, ‘clog, wooden shoe’, prop, ‘shoe formed 
from a lump of wood’, rel. to LG. klump 
(whence G. Klumpe, Klumpen), ‘clump, lump’, 
MDu. clompe , ‘Lump, mass’, Du. klomp, ‘lump; 
wooden shoe’, Dan., Swed. klump, ‘lump*, OE. 
clympre , ‘lump of metal, metal’,, and to ON. 
klumba, klubba , *a thick stick, club*. See clamp 
‘device for fastening’, and cp. club. Cp. also 
clunch. Cp. also down. 

Derivatives : clump , intr. and tr. v., clump-y , adj. 
clumsy, adj. — ME. clumsed, pp. of clumsen , ‘to 
benumb’, rel. to dial. Swed. klummsen , ‘benum- 
bed with cold’, OE. be-clemman, ‘to bind, en- 
close, fetter’, and to E. damp, ‘a device for 
fastening (q.v.). For the insertion of s before the 
=== cling/climb/cloud/clump ===
49236:cloud, n. — ME. dud, cloud, ‘rock, cloud’, fr. OE. 
49237-dud , ‘mass of rock, rock’, which meant orig. 
49238-‘mass’, and is rel. to clod (q.v.) 
49239-
49240-Derivatives: cloud, tr. and intr. v., cloud-ed, adj., 
49241-cloud-ing, n., cloud-less, adj., cloud-less-ly, adv., 
49242-cloud-less-ness, n., cloud-y, adj., cloud-i-ly, adv., 
48840:climb, intr. and tr. v. — ME. climben , fr. OE. 
48841-climban, rel. to OHG. klimban , MHG. klimben , 
48842-klimmen, G. klimmen , MLG. klimmen, klim- 
48843-meren , and in gradational relationship to ME. 
48844-clambren, clameren , ‘to climb’. The original 
48845-meaning of these words was ‘to stick on to*. 
48846-They are rel. to clam, ‘to smear’, clammy, cleave.
```


## [2026-09-05T20:42:57.878Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n 'گلوله\\|گوی ' ARY_pages.txt | head -20; echo \"=== latin index ===\"; grep -n -i 'GEL\\b\\|GLEU\\|GLEI' ARY_latin_index_pages.txt | head -20",
 "description": "Aryanpur for guy/golule"
}
```


### [2026-09-05T20:42:57.939Z] TOOL RESULT

```
176:بررسی جنبش‌های کوچگرانه‌ی دیگر در دوران‌های تاریخی الگوی کلی این کوج‌ها و پيامدهای
965:( کشاورزان و شبانان و سوداگران) وجود داشتند که نقش اجتماعی آنها با الگوی سه گانه‌ی فوق
11761:۱ بازگشت به‌زگوهگوی ی
13103:اس چم اين واژه در زبان‌های ژرمنی: گلوله اگوی نخ
=== latin index ===
271:22 GS Milne 9 goa slar gel dy Sg sad 990 OU 9 alea o Sealed J bab}
295:ayaa) ye shojly cl atiload ligt y ce Gel 5 2s!) pH! Gore ey 92 9 025)
410:poles allel yal ake cals Gel pt aS lll 9 cA ceed ole
601:NA Ibe Vee Bytee) gy dlase sl 3 al ol Scand pl j) Sb crear gleule
748:Ogee Vs ayn 4 aah; gel b Koen shad jy photiay Jhat SG pl jl gtr 3 6S
821:ga gle cg Uh) ap gor Bho SDL J CF pel Soy 6 gg) 6 FFL Gel EL;
827:Sal gy y9 Ded on, Ge pH OF AS GH OL} 5 gel ny GIL] GLA!
976:OTL AF rapes OLY abst y tr GEL] Ge ar OWIly go y alps F
1055:i P92 GEL 5S pr oy was hy te aule yo Lalb cul ere od oll
1195:say gel pile LS 30 ph Scant Gh J Es shy came 9 tals sb Oe
1262:opty Sars& leo ly Gel Gel tm Fa od Ab SOLS al 52 eS ge ealizl (g ylice
1293:2 ObML srl GEL; Opp Cond oad cd Fe slew Ls bj © Obj oS jHoSly by cul
1341:Lasgly gel UT Layla gant leas PAFEN sls yPUST (S,luls » BOUFFEE
1572:stds SUE till, 32 05s gel cm
1891:ST sly dy tle aly AS jh aan aj Stared gf Lay gal Sel gel pole IF Gotan! shy “A
2322:IGEL (GERMAN) glT IZH, AUS ARMENIAN) ga)
2689:ON, ONA (SLOVAK) S\ gel DAY, DA HAFGHANI)( 3-4) gi)
2725:Og) OW ely Seo 32 o5ly gel cabs obs jleede WY arg 4 ITs Dj Glleng, IIS
2917:“BREMENO (SLOVAK) Sigel :(OLD SCANDINAVIAN), AS Sabe!
3111:(OLD HIGH GERMAN) pS galt GEL ARMENIAN) a \
```


## [2026-09-05T20:43:03.307Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '13080,13120p' ARY_pages.txt; echo \"--- page tag ---\"; grep -n '\\[pdf page' ARY_pages.txt | awk -F: '$1<13103' | tail -2",
 "description": "Aryanpur context"
}
```


### [2026-09-05T20:43:05.115Z] TOOL RESULT

```
لول / ۴۲۱
بادداشت:
چم ان واژه در زبان فرانسه؛ پوز» فک
چم اين واژه در زبان‌های اسپانیایی و پرتغالی: یقه.
چم این واژه در زبان رومانی: دهان,
:
:
کردی (8(8.01577): هلدی (076/7): 0
ما6 ,61-18 ب#ناناه لهستانی (97ل۳0): 600۸
افغانی (پشتر) (//4۳0/۸2)+ روسی (85]4(4ا): 61۸ ْ
اشاناه ,شامه چکه (1ل250): 10۸
سانسکریت (54(/57077): 05 اسلوا کی (851.0142): 10۸
یونانی 07550): 65 ایركدی کهن (17337 صا0):
ابسلندی کهن (2 نی ۲۵م: 48۵ ماه شاه ۱
نورس کهن (۸/0785 010): 8
ساکسرنی کهن (547000 ۰:)0۵ 21۷1۸۲
فریزی کهن (۷لفا5ل7۶ 0ظ0): 8 پسگشت‌ها ارت هراد دای !
آلمانی کهن (027044(0 ۲۷/0 صاه): [ 0۹60 ۶00800
: 1۸ ای یت نا
ا آلمانی (08791۸7): 268178 3 (6-3۳) ,182 (تانااه) :
ا انگلیسی کهن (7ل50/3 ۵م): 0۲383/8۴۲ 4 (5تت ,12)) +57 َ
۱ انگلیسی (۰:)۸/0(58 ۰ 616۷۷ ,5 انا برهان قاطع : 1۳۲
ِ بادداشت, 5
اس چم اين واژه در زبان‌های ژرمنی: گلوله اگوی نخ
چم این واژه در زبان ماف یگریت و زبان‌های اسلاوی: قلنبه. :
چم این واژه در زبان یونانی؛ بند استخوان» فوزکك.
اوستایی (/4۳5374): 71 6۸32۸ ,6302۸ 6۸352
[pdf page 441]
۲ | گنبد ‏
پارسی باستان (۲8/۵14۸ 0/0): -۵82* انگلیسی (5/ا8(/0): ون 8
پهلوی (۲7مائلهه). بش61 ,شاه دانمارکی (0۸(75): 0۸
6۸8712۸ سوئدی (۱.:782/54 0۸
اوستی (015۸8201/:0558710 ,073۸2170 نروژی و۳0 268 ی
کردی (1001874): تاه هلدی (ل070): لس ی
سانسکر یت (5/5777): ایرلندی میانه (تلقلقا عتط2ص)0): کفقاه
: 71 شک تفقده ناقده َ
بونانی 0785/0): راهان پسگشت‌ها گر تین
۱ لانین (470ل): 0 ۳۳
: ابسلندی کهن (/5(42/014014 طا0): :0545
ین ۱۹۸ 5 (۳08شا7 85)
فریزی کهن (/۸ط2۶/5 ۵ا0): ۰ 1188۴ :۸12507218
--- page tag ---
13047:[pdf page 439]
13078:[pdf page 440]
```


## [2026-09-05T20:43:13.942Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '13078,13085p' ARY_pages.txt; echo \"=== search headword گلوله in index ===\"; grep -n 'گلوله' ARY_pages.txt | head; echo \"=== گوی headword ===\"; grep -n '^گوی\\|گوی /' ARY_pages.txt | head",
 "description": "Aryanpur headword"
}
```


### [2026-09-05T20:43:14.010Z] TOOL RESULT

```
[pdf page 440]
۳
لول / ۴۲۱
بادداشت:
چم ان واژه در زبان فرانسه؛ پوز» فک
چم اين واژه در زبان‌های اسپانیایی و پرتغالی: یقه.
چم این واژه در زبان رومانی: دهان,
:
=== search headword گلوله in index ===
13103:اس چم اين واژه در زبان‌های ژرمنی: گلوله اگوی نخ
=== گوی headword ===
761:گویش‌های گونا گون گردید. پس از فروپاشی امپراتوری روم و قطع تماس میان نواحی لاتین زبان طی
1447:گویک (077/0): 1360۸۷ ,ال۸ 0۸50 دانمارکی (0۸/۷18]7): 0)
1761:گویکد (/001[4): ۱۱
4155:گویکه (0077710): ,711675 8 (1۷8۳) +8727
11293:گویک (10ل007): 5۸71 10 5۰۸70۷۸7
```


## [2026-09-05T20:43:24.526Z] TOOL CALL #39: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/",
 "description": "List ARY dir"
}
```


### [2026-09-05T20:43:24.577Z] TOOL RESULT

```
total 9468
drwxrwxr-x  3 sfmqrb sfmqrb    4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb    4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb 8102112 Sep  4 14:06 ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  586473 Sep  4 14:06 ARY_latin_index_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  960497 Sep  4 14:06 ARY_pages.txt
drwxrwxr-x  2 sfmqrb sfmqrb   20480 Sep  4 13:30 ARY_pages.txt.pages
```


## [2026-09-05T20:43:29.958Z] TOOL CALL #40: Bash

```json
{
 "command": "pdftoppm -f 440 -l 440 -r 170 -png -singlefile data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf \"$SCR/ary440\" 2>/dev/null || pdftoppm -f 440 -l 440 -r 170 -png -singlefile data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/ary440; ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/ary440*",
 "description": "Render ARY page 440"
}
```


### [2026-09-05T20:43:32.014Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 68775 Sep  5 16:43 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/ary440.png
```


## [2026-09-05T20:43:34.498Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/ary440.png"
}
```


### [2026-09-05T20:43:34.517Z] TOOL RESULT

```

```


## [2026-09-05T20:43:47.620Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && awk '/\\[pdf page 44[1-9]\\]|\\[pdf page 45[0-2]\\]/{p=$0} /^گو|گوی|GUY|GŪY|GOY/{print NR\": \"p\" :: \"$0}' ARY_pages.txt | sed -n '1,40p'",
 "description": "Find ARY guy entry"
}
```


### [2026-09-05T20:43:49.414Z] TOOL RESULT

```
153:  :: زندگی می‌کردند و بهمین دلیل زبان آنها پا فاقد گویش‌ها ی گوناگون بود و یاگویش‌های آن بهم بسیار
158:  :: (8۸ظ۸ 283/7391818 ۸1۸1/1724) اگر حوزه‌ی گسترش یکه زبان زیاد شود» گویش‌های
171:  :: کش و واکنش یکی از دلایل عمده‌ی تقسیم زبان واحد هندو اروپایی ابندا به گویش‌ها و سپس به
176:  :: بررسی جنبش‌های کوچگرانه‌ی دیگر در دوران‌های تاریخی الگوی کلی این کوج‌ها و پيامدهای
186:  :: این نواحی نیز متقابلاً تحت تأثیر زبانهای محلی قرا رگرفت وکم کم به چندگویش تبدیل شد (ترکی
634:  :: نظر شمار سخنگویان (بیش از یک میلیارد نفر) بزرگترین خانواده‌ی زبان‌های هند و اروپایی
731:  :: سخنگویان به این زبان‌ها پیش از ۱۳۰ میلیون نفر است.
740:  :: یکی از گویش‌های یونانی کهن به نام «مایمینی» (۸]۷253۸۳۸۵۷) نوشته شده‌اند. این نوشته‌ها و ۱
749:  :: آثار فلسفی و تاریخ ی گوناگون. زبان یونانیکلاسیکه به ندریج تبدیل به یونانی نوین شد. سخنگویان
758:  :: است. از میان چندین گویش هند و اروپایی رایج در ایتالیای باستان» زبان لاتین (زبان شهر رم و
761:  :: گویش‌های گونا گون گردید. پس از فروپاشی امپراتوری روم و قطع تماس میان نواحی لاتین زبان طی
762:  :: قرون وسطی؛ این گویش‌ها تبدیل به زبانهای «رومانس» (10۸1۸367) یعنی فرانسه و ایتالیایی و
765:  :: مرکزی و بخشی از امریکای شمالی بردند. امروزه شمار سخنگویان این زبان‌ها به حدود ۹۰۰ میلیون
783:  :: ۰ میلیون نفر به آن سخن می‌گویند و زبان رسمی چندین کشور دیگر و زبان بین‌المللی جهان
812:  :: باستانی ترین اشاره به زبان ارمنی د رکتاب هرودوت (مورخ یونانی) آمده که می‌گوید ارتش
840:  :: صربی» کرواتی» مقدونی). جمع سخنگویان به این زبان‌ها حدود ۴۵۰ میلیون نفر است.
863:  :: شش میلیون نفر به این دو زبان سخن می‌گویند.
868:  :: مجاور آن رواج دارد و شامل است بر دوگویش»گویش شمالی يا «کگه» (۲30) وگویش جنوبی يا
871:  :: زبان سخن می‌گویند.
965:  :: ( کشاورزان و شبانان و سوداگران) وجود داشتند که نقش اجتماعی آنها با الگوی سه گانه‌ی فوق
1094:  :: می‌گوید «اگر اینجا بمانم و با مردم شهر تراوا جنگ کنم» زنده به دیار خود پرنخواهم گشت ولی
1124:  :: : هدوستان به یک زبان واحد تکلم می‌کردند ولی در اثرگذشت زمان کم کم دارای د وگویش و سپس
1130:  :: نمایان می‌سازند. ولی این نوشتارها هم از نظر شمار و گویایی به پای متون هندی باستان ,۷8016)
1150:  :: زبان پارسی کهن کمی متأخرثر از زبان اوستایی است و اصولاً از نظر گویش با اوستایی فرق
1447:  :: گویک (077/0): 1360۸۷ ,ال۸ 0۸50 دانمارکی (0۸/۷18]7): 0)
1502:  :: گونیکد (0077170): ۸۸ ولزی (517 )+ 1
1537:  :: ۱- شکل این واژه در گویش خونماری چنین است: 131.7218۸ (و شباهت آن با همریشه‌های لاتین و یونانی آن تسبتاً
1606:  :: گوتبک (شاید) (007/0): ۸61۸0۲
1627:  :: گوتیک (007[10): لاه 8 4 200
1646:  :: گونیکه (0071410): نینک
1761:  :: گویکد (/001[4): ۱۱
1914:  :: گوتیکك(شاید) (0077710): ها۸ پسگشت‌ها ادا دی دای ]
1937:  :: گونیکه (00777/0): قالش رالشاتشآ برتونی (886700): ره
2148:  :: گوتیک (ع007[71): 0 ,۶۸ سای (کلنی) خی ۸10۰
2217:  :: گوتبک (007[4[0): 5 ,6 (8ت۸0۲) :05
2234:  :: گوتبکه (007212): ۸187۸ ولزی (۴.8): ردان
2314:  :: گونبکد (00714/6): ۸۸ نروژی (/لها07077۲50: ۸
2331:  :: گوتیکد (007710): ردرارید ان 969 هن
2349:  :: 7 صفحه‌ی ‎)٩‏ می‌گوید این واژه در فارسی میائه ۸2:۸1 و در فارسی نون ۸7.0 است ولی نتوانستم این
2538:  :: گوتبک (0077/0): 18-87[1۷381 ,قلل8771 پسگشت‌ها 55 ق۲۵۲2
```


## [2026-09-05T20:43:56.216Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n 'GUY\\|GÜY\\|GOY\\|GŪY' ARY_latin_index_pages.txt | head; echo \"--- persian headword گوی in pages 44x ---\"; awk '/\\[pdf page 4[4-6][0-9]\\]/{p=$0} p!=\"\" && /گوی \\/|گوی\\/|گوی ‌\\//{print NR\": \"p\" :: \"$0}' ARY_pages.txt | head",
 "description": "Search ARY for guy"
}
```


### [2026-09-05T20:45:06.612Z] TOOL RESULT

```
859:elitr IS 3 3) oli) 9 om GUY Se Qe
6891:CRENAL . (OLD IRISH) oS 5052! KIOBE (GUY DANISH) Sails
--- persian headword گوی in pages 44x ---
```


## [2026-09-05T20:45:10.809Z] TOOL CALL #44: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-05T20:45:10.814Z] TOOL RESULT

```


```


## [2026-09-05T20:45:16.105Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%88%DB%8C",
 "prompt": "Give the full Persian etymology section(s) for گوی — especially the noun meaning \"ball, sphere, polo ball\". Quote the etymology verbatim, including Middle Persian form and any Proto-Iranian/PIE reconstruction and cited authorities (Hasandust, MacKenzie, Cheung)."
}
```


## [2026-09-05T20:45:17.302Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%84%D9%88%D9%84%D9%87",
 "prompt": "Give the Persian etymology of گلوله (golule) \"bullet, ball\" verbatim, including any PIE root, Sanskrit cognate, and cited authorities."
}
```


### [2026-09-05T20:45:22.564Z] TOOL RESULT

```
# Persian Etymology of گلوله (golule)

According to the Wiktionary entry, the word is "Inherited from Proto-Iranian, from Proto-Indo-Iranian, ultimately from Proto-Indo-European *glew-". 

The entry identifies a Sanskrit cognate: "ग्लौ (glau, 'lump')". 

The cited authorities referenced in the Further reading section are Ali-Akbar Dehkhoda's Dehkhoda Dictionary (1931–) and Sulayman Hayyim's New Persian–English Dictionary (1934).
```


### [2026-09-05T20:45:22.818Z] TOOL RESULT

```
# Persian Etymology for گوی (gōy) - "ball, sphere"

## Etymology 1 (Noun)

Based on the Wiktionary entry, here is the etymology section:

**Source Material:**
The word derives from Middle Persian (gwd /gōy/, "ball"), with documented cognates across multiple language families.

**Cognate Languages Listed:**
- Sanskrit गोल (gola)
- Persian گلوله (golule, "pellet; bullet")
- Northern Luri گولٛاْ (goła, "pellet")
- Central Kurdish گولە (gule) and گۆ (go, "ball")
- Northern Kurdish gog ("ball")
- Zazaki gudi ("ball; round")
- Classical Syriac ܓܘܝܐ (gōyāʾ) - Iranian loanword

**Authority Cited:**
MacKenzie, D. N. (1971), "gōy" in *A Concise Pahlavi Dictionary* (Oxford University Press, page 37)

**Note:** The entry indicates a "[Book Pahlavi needed]" notation for the Middle Persian form, suggesting the script representation requires verification. No Proto-Iranian reconstructions or works by Hasandust or Cheung are cited in this particular dictionary entry.
```


## [2026-09-05T20:45:41.697Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/club",
 "prompt": "Quote the full etymology of \"club\" (both the stick sense and the association sense), including the Old Norse origin and any note about French club being borrowed from English."
}
```


## [2026-09-05T20:45:42.763Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.cnrtl.fr/etymologie/club",
 "prompt": "Quote the etymology of French \"club\" verbatim: what language is it borrowed from, in what century, and what is the ultimate origin?"
}
```


### [2026-09-05T20:45:47.302Z] TOOL RESULT

```
I cannot provide the etymology of French "club" based on the content shown. The webpage excerpt provided only displays "Portail lexical" (Lexical Portal) as a header, without any etymological information about the word "club" or its origins, source language, or century of borrowing.

To answer your question accurately, I would need access to the actual etymological content from this lexical portal.
```


### [2026-09-05T20:45:48.555Z] TOOL RESULT

```
# Etymology of "Club"

**Noun (Weapon/Object):**
The word originates from Old Norse *klubba* meaning "cudgel," derived from Proto-Germanic *\*klumbon*. As documented: "c. 1200, 'thick stick wielded in the hand and used as a weapon,' from Old Norse *klubba* 'cudgel'" The gaming sense appeared later: "Specific sense of 'bat or staff used in games' is from mid-15c."

**Noun (Social Organization):**
The association meaning developed through verbal usage. The entry notes: "The sense 'company of persons organized to meet for social intercourse or to promote some common object' (1660s) apparently evolved from this word from the verbal sense 'gather in a club-like mass' (1620s), then, as a noun, 'association of people' (1640s)."

**Notable Usage:**
A 1659 observation captures the emerging social sense: "We now use the word clubbe for a sodality in a tavern."

The page does not mention French borrowing from English; rather, it notes Romance language parallels like Spanish *basto* and Italian *bastone* for the card suit.
```


## [2026-09-05T20:45:52.821Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/club",
 "prompt": "Give the French section: the etymology of French \"club\" (borrowed from which language and when). Also give the English etymology (Old Norse klubba)."
}
```


## [2026-09-05T20:45:54.110Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%84%D8%A7%DA%86",
 "prompt": "Give the Persian etymology of کلاچ (kelâč) — is it borrowed from English \"clutch\"?"
}
```


### [2026-09-05T20:45:57.983Z] TOOL RESULT

```
# Etymology Information

## English Etymology
The English word "club" comes from Middle English *clubbe*, which derives from Old Norse *klubba* or *klumba* meaning "cudgel." This traces back to Proto-Germanic *klumpô* ("clip, clasp; clump, lump; log, block").

## French Etymology
Unfortunately, the document content was truncated before reaching the French section's etymology. The page structure shows a "French" section exists with subsections for Etymology, Pronunciation, and Noun, but the actual etymological details for the French word "club" are not included in the provided text excerpt.

To obtain the French etymology, you would need to access the complete Wiktionary entry for "club."
```


### [2026-09-05T20:45:58.933Z] TOOL RESULT

```
# Persian Etymology of کلاچ (kelâč)

Yes, according to the Wiktionary entry, کلاچ is borrowed from English. The page states: "Borrowed from English _clutch_." 

The Persian word kelâč refers to a clutch—specifically, "a device to interrupt power transmission, commonly used between engine and gearbox in a car." This is a loanword adoption reflecting the automotive terminology that entered Persian from English.
```


## [2026-09-05T20:46:03.094Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://fr.wiktionary.org/wiki/club",
 "prompt": "Quote the French etymology of \"club\" verbatim (from which language, which century)."
}
```


## [2026-09-05T20:46:03.468Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%84%D9%88%D8%A8",
 "prompt": "Give the Persian etymology of کلوب — borrowed from which language?"
}
```


### [2026-09-05T20:46:06.728Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:46:07.733Z] TOOL RESULT

```
# French Etymology of "Club"

According to the Wiktionnaire article, the French word "club" comes from English and dates to 1702:

> "De l'anglais *club* (« bâton, société »), le sens étymologique de « bâton » est un emprunt de la fin du xixe siècle."

In other words, French borrowed "club" from English, where it originally meant "stick" or "society." The stick-related sense arrived as a loanword in the late 19th century.
```


## [2026-09-05T20:46:19.060Z] TOOL CALL #53: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%DB%8C\" \"https://en.wiktionary.org/wiki/%DA%AF%D9%84%D9%88%D9%84%D9%87\" \"https://www.etymonline.com/word/club\" \"https://en.wiktionary.org/wiki/club\" \"https://fr.wiktionary.org/wiki/club\" \"https://en.wiktionary.org/wiki/%DA%A9%D9%84%D8%A7%DA%86\"; do timeout 120 python3 tools/fetch_source.py \"$u\" --note 'page 169, root Gel: Persian guy/golule/kelach, English+French club' 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-05T20:46:23.652Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/58a39c03fbf55fad.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f45b0624431e7af7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a06d154c045e803c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4eeca3ea44016f59.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b90d188e24729c96.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/88549ad4cc954d77.txt
```


## [2026-09-05T20:46:28.271Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT clew/club/glue ===\"; grep -n -m1 -A4 '^CLEW\\|^Clew' SKT.txt; grep -n -m1 -A5 '^CLUB\\|^Club, a' SKT.txt; grep -n -m1 -A5 '^GLUE\\|^Glue' SKT.txt; echo \"=== LEW globus/gluten ===\"; grep -n -m2 -A6 'globus,' LEW_1910.txt | head -25; echo \"=== LAT globus ===\"; grep -n -m2 -A8 'globus' LAT.txt | head -25",
 "description": "Skeat, Walde, Ernout-Meillet"
}
```


### [2026-09-05T20:46:28.362Z] TOOL RESULT

```
=== SKT clew/club/glue ===
3560:Clew.  Clue,  a  ball  of  thread.  fE.) r/fi(V.  A.  S.  c/fTW.  short  foim  nf  r/rvvi^ a  clew.  +  Du.  kluuvn ;  whence  k/tttueni^ to  wind  on  clews  (K.  fltw  up  a  HiU( M.  H.G.  kluwtH,  Allied  to  L.gi^mm, dew.
3561-Click ;  see  Claok.
3562-Client.  (F.-L.)     F.  c/im/.  a  suJtor., L.  c/Unfer»,ucc  of  cltrtu  =  dufHS.  orig. hearer,  one  who  listens  to  advice  ;  pses  {t of  (lu^re.  to  hear.   (V  KRU.)
3563-cuff;  see  Cleave  (a).
3564-CUmatc.  (F.-Gk.)  M.E.  fUw^.^ F.  climat.  —  Ck.  «Xi^t».  stem  of  xAl'^ a  slope,  zone,  region  of  the  earth*  cfr m^ite.  -  Gk.  mkivw,  to  lean,  «loj>c: Lean.
=== LEW globus/gluten ===
=== LAT globus ===
1156:serra, globus; sur ces termes v.Kretschmer, Glotta 6,30), et par exten-
1157-sion le "combat" lui-meme. - Ancien, usuel. Les representants romans
1158-sont rares, v.M.L. 106-107 .
1159-acieris: mot de gloss., securis aerea qua in sacrificiis utebantur
1160-sacerdotes, P.F.9,7. Cf. acisculus (ou asciculus de ascia?; la forme est
1161-douteuse): instrument de lapidaire, dolabre; acisculdrius (et exacis-
1162-clo,-ds). Le rapprochement de portisculus, lui-meme obscur, n'enseigne
1163-rien.
1164-a[c]ciariun n.: ferrum durum (Gloss.), M.L.103 (et *acidle dgalement
--
11518:quus, e.g. Cic.,Rep.6,17, qui globus reliquos bmnis complectitur, sum¬
11519-mus ipse deus arcens et continens ceteros-, toutefois semble plus
11520-comprehensif, cf. Cic., Verr.5,87, erant perpauci reliqui, ceteri dimissi.
11521-- Ceteri designe un enseable par opposition k alii: Sali.Iu.74,1,
11522-ceteri formidine, pars ad Romanos, alii ad regem Bocchum profugerant ;
11523-aussi est-il souvent joint k omnes, cuncti. Le neutre 9'emploie adver-
11524-bialenent: ceterum, cetera "du reste” et depuis Salluste^ surtout
11525-dans Tite Live, ”«ais” (cf. pour le sens gr. aXXa, 'nxXXa, xa Xchtox),
11526-(de)cetero, ceteroqui(n). - Ancien, usuel et classique. Non ronan.
```


## [2026-09-05T20:46:54.780Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'globus,-i\\|globus, -i\\|^globus\\|gluten,' LAT.txt LEW_1910.txt | head -10; echo \"=== gluten LAT ===\"; grep -n -B2 -A12 'glüten\\|gluten n' LAT.txt | head -40",
 "description": "Ernout-Meillet globus/gluten"
}
```


### [2026-09-05T20:46:54.854Z] TOOL RESULT

```
LAT.txt:26373:globus (-bum Gloas.),-! a.: i° boule, balle, sphere, globe, cf.
LAT.txt:26398:globus', cf. globus Parcarum = glomus P., Bucheler CLB 493,6, et anssi
LAT.txt:26461:gluten, -inis n.: gln. Attest 4 depnis Varron et Lncrbce. Aatres
=== gluten LAT ===
```


## [2026-09-05T20:46:58.694Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26373,26400p' LAT.txt; echo \"=== gluten ===\"; sed -n '26461,26485p' LAT.txt",
 "description": "Ernout-Meillet entries"
}
```


### [2026-09-05T20:46:58.762Z] TOOL RESULT

```
globus (-bum Gloas.),-! a.: i° boule, balle, sphere, globe, cf.
Cic., N.D.3,18,47, cu* duae formae praestantes sint, ex solidis globus
(sic enim o^xxtpav interpretari placet), ex planis autem circulus aut
orbis qui xuxXoc graece dicitur', 3 0 dans la langue ailitaire: foraa-
tion dense, peloton (cf. acies, serra,1 cuneus) ; de 11: foule dense,
aasse. - Ancien, usuel et classique.
D^riv^s: globo,-as aettre en boule (usite surtout au passif); glo¬
bulus a.; globOsus = ocpatpoei. 5 r]C> globositas (Macr.); globatimi Aaa.
Marc.)j globeus (b.lat.); conglobO: r^unir en boule, aasser, pelo-
tonner, et ses derives.
Les 1 . roaanes attestent *globellus M.L.3791 (sur gubellum, lubel-
lum ... quasi globellum dans Isid.19,39,6, v. Sofer, p.136 et s.);
*globilia 3793J *globula 3793» *globuscellum 3794.
Cf . glSba et glomust Aucun rapprocheaent sur.
glocio, -Is, -Ire: glousser. Attest 4 depuis Coluaelle. M.L.3795.
Cf. glattio, glaucio, glottio, glittio, gluttio et glociddre (l. g lo¬
citare? cf. glaucito) : gallinarum proprium est cum ouis incubiturae
sunt, P.F.87,i7j gloctoro: craqueter (eri de la cigogne).
Verbe expressif k gl- initial. Cf. v.angi, c loccian.
glomus, -eris n.(et .glomus,-x a,?). Les 1 . roaanes attestent glomus
et *glemus. II y a eu contaaination de deux foraations: *glemus, -eris
(cf. glomerare, et, pour l'e, vin.gemo, it. du Nord giemo et glomus,-x,
cf., pour ce procedi, modus et pondus. L'o de glojius est bref; la
scansion gldmere dans Lucr. 1,360, n'est qu'un expedient pour eviter
le tribraque dans 1 'bexaabtre): peloton, boule. Ne diff&re guere de
globus', cf. globus Parcarum = glomus P., Bucheler CLB 493,6, et anssi
1 'abr^ge de Festus, 87,14, glomus in sacris crustulum, cymbi figura,
ex oleo coctum appellatur. Ancien. M.L.3801.
=== gluten ===
gluten, -inis n.: gln. Attest 4 depnis Varron et Lncrbce. Aatres
foraes: glutinum (Lacii.), et pias recentes: *glutis,-inis (cf. sanguen
et sanguis)', glutis,-is (Marcell. ) a. pnis f 4 a., snr leqael a 4 te
fait. an noainatif gltis (V^g., Ans., snr le type sa lus, -utis ), de»enr 4405
gnarus
dans les 1 .roaanes. M.L.3806; britt.glud.
On trouve dans 16 gloss* de Philoxbne gluS: (xiKTTTjcfXo; nais il seiblc
qu'on ait la nne reconstitntion artificielle d'un verbe d'aprbs le
glittus de Caton, lu fanssenent glutus, gluttus. 0 u bien gluo a-t-il
dtd fait sur glfis d'aprfes le nodele acus, acuo?
D^riv^s: glutino,-ds: coller, recoller (les levres d'une blessnre):
et agglUtinS, coller contre, 7ipoCTxoXXu>; conglutino, coller enseable,
souder; de-, dis-, re - glutino ; glutinSsus: collant, visqueux;
glutinator: relienr, glutinatio ; glufindnentun: reliure; glutinarius
fabricant de colle; tous temes techniques qui apparaissent seulenent
dans la latinit^ imperiale.
V. g littus.
La racine • sans donte 41 argisseaent de la forne en gl— qui se
tronye dans gleba et glonus - est attest^e par des fomes verbales
en celtique: iri. glenaid "il s'attache", etc. (v. Marstrander, 06 -
servations sur les prisents i.-e. i nasale infixde en celtique, p.10
et 31), en gemanique: v.isl.feltna "endnire", et, ave.c t, v.h.a.felenan
"endnire", etc., en baltique: lit. gleju "j'enduis, je colle", en^grec,
avec snffixe en yjs/or: yX()(opai. " j e ne colle i". Nona k suffixe -no-,
*-%&-: v.angl. clan "argile". Le slave a *glijt ( r. glej, etc.) "argile",
```


## [2026-09-05T20:47:08.015Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n 'gulûle\\|gulule\\|glāu\\|gläu\\|npers. gul' WLD_Bd1_pages.txt | head -10; echo \"=== gel- ballen ===\"; grep -n 'ballen, sich ballen\\|Gerundetes' WLD_Bd1_pages.txt | head -5",
 "description": "Walde-Pokorny Bd1 gel-"
}
```


### [2026-09-05T20:47:08.084Z] TOOL RESULT

```
=== gel- ballen ===
```


## [2026-09-05T20:47:11.241Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n 'ballen' WLD_Bd1_pages.txt | head -20; echo \"---pages---\"; grep -c '\\[pdf page' WLD_Bd1_pages.txt",
 "description": "WLD grep ballen"
}
```


### [2026-09-05T20:47:11.300Z] TOOL RESULT

```
4666:Perner acymr. aballen, ncymr. afallen, corn, auallen, bret. aualen „Apfel-
29123:n., icolcha f as. wolkan n. ,.Wolke‘ (kaum als ,.sich ballende, sich walzende
34736:ballen, hiiufen", kiicki „die Plejaden",
34808:ballen", kupenis „Schneehaufen“, kuprs „Hocker“, mit Dehnstufe qo[u]p-
36398:„Klumpen“, komitb „zusammenballen            hmikate „knittern, kniillen, ballen;                                     41
42440:„schallen, tonen   abd. scellan „scballen, tonen, klingen, liirmen 11 nhd. ver-
47036:   Anlautvariante neben lit. glebys dt. Klafter ? (s. u. gel- ,,ballen“).
50713:„ballen     *gleu- Hirt Abl. 119); aueh nicht besser zu arm. glux, gen glxoy
52357:Spielball" (oder als g e l- zu *g<i- ,ballen' Persson Beitr. 106), gr. yvhog
52402: „ballen" ist wegen Kiel-boek und alb. gal-, s. im flgdn., nicht vorzuziehen),
52436: fragliche Ankniipfung an *ycl- „ballen“              ganz fraglich auch arm. kof,
52824:zusammenballen, kauern mit dt. kauchen = kauern (und nicht annehmbar
52980:rinde' ) auch av. yiutda-, gtindct ..Teigballen"?
53013:Schlundes bei Wiederkauern auch Wiederkauballen”, mhd. lintel ,.her-                            ;
53099:.,entziindliche Geschwulst. Beule                                                                                    ciccoilu , c (iv)udu „Y iederkiiuballen ‘ (siehe
55958: ballen ’).
56118:Stud. 15; oder als *gal-nu- zu *gel- „ballen" nach Fortunatov BB.
58069:1.    gel- „ballen; gerundetes, kugeliges u. dgl.". Ygl. bes. Fick Or. und Occ.
58235:„(die Faust) ballen; umfassen; packen befestigen  mhd. Want „Schlinge;
58294:sich ballender Zucker", gudaka-h „Kugel“ (kaum mind, aus *gludos dt.                                                            :
---pages---
0
```


## [2026-09-05T20:47:15.188Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '58069,58090p' WLD_Bd1_pages.txt; echo \"=== glau/gulule ===\"; grep -n 'gulale\\|gulüle\\|gulule\\|glav-\\|glau-' WLD_Bd1_pages.txt | head -10",
 "description": "WLD gel- entry"
}
```


### [2026-09-05T20:47:15.260Z] TOOL RESULT

```
1.    gel- „ballen; gerundetes, kugeliges u. dgl.". Ygl. bes. Fick Or. und Occ.
        3, 311 f., Persson Wzerw. 54, 67, 130, 172, Johansson IF. 2, 42 f., KZ.
        36, 376 f.,  Zubaty AfslPh. 16, 423 f., Wood IF. 18, 40ff., a* 96ff.,
        Solmsen Beitr. I 222 ff., Persson Beitr. 64 ff. (mit 932 f.).
  Belege dieser einfachsten Wzf. ziemlich sparlich und z. T. recht unsicher:
  Ai. gula-h gult (Lex.), gulika „Kugel, Spielball, Perle, Pille, caput“
                          ,


(oder mit Z-Suffix zu *geu- „biegen“?);
  gr. yahvdoi und yehv&of EQefhv&oi Hes. (Solmsen; „Kiigelchen“?);
  lett. ijilas, yilens, giluotas „Geschwiilste zwischen Haut und Fleisch der

Pferde" (eher zu lit. g'de ,.Eiehel“, s. *g'iel- „Eichel“, doch ygl. u. si. zely)
      aksl. zely              (zely)       ,,   ulcus", nbulg. zelka     ;
                                                                             ,Driise,        Geschwulst", sloven, zelva
„Druse“, russ, zolvb                        ,
                                                 zolvuj ,   zelvak „Beule, Auflauf", klr. zelvak „Beule",
zolnn         „Skrofel",                  cech. zhtna,       zlma „Schlauchgeschwulst“ (Solmsen aaO.);
klr. zold „Erdnu£S, Erdeichel (Arachis hypogaea, mit unterirdischen Knollen)".
      Dagegen             aksl. zleza,              russ. zelezd ,    cech. zleza, zldza „Driise"                       und         cech.
hlaza,            poln. gloza              „Driise“ (wozu            poln. glozna            „Unterteil des Beines bei
=== glau/gulule ===
58669:   ai. glau-h „Ballen, Kugel, geballte Masse *, np. gidide „Kugel“; air. gib-,
58834:    Yielleicht hierher (Froehde BB. 10, 298) lit. glaudziii glausti lett. glau-st          ,       ,
59315:Yersuche, *glau- auch im Kelt, und Slav, zu finden, bucht Boisacq 150).
76845:dem Yorbild von so-, su-), got. taz- (in tuz-ioerjan „zweifeln u     „unglau-     =
77645:abdere „wegtun, verstecken, anoxidhai 1 , perdere „vernichten“, credere „glau-
```


## [2026-09-05T20:47:30.491Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'گوی:' MON_part2.txt | head -5; echo \"=== HUB ===\"; grep -n -i 'gui\\b\\|gūi\\|Ball\\b' HUB.txt | head -10",
 "description": "Mo'in guy, Hübschmann"
}
```


### [2026-09-05T20:47:30.549Z] TOOL RESULT

```
10551:قافیه گوی: (80.«(ع. ف. - قافیه گوینده| 
35239:گنجشک تویی‌تویی گوی: (جا د.) طوطی. 
37074:گوی: ۷ | - کو کلو له ۱ 
83826:واگوی: (0ع-۰2(- واگو - واگویه] (امس.) 
=== HUB ===
3345:936. Dazu arm. LW. gund 'Kugel', gndak *Kugel, Ball,
7241:1. t in gUi *Welt\ zd. ga^&ga- *irdisch' (siehe oben
```


## [2026-09-05T20:47:33.052Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '37070,37090p' MON_part2.txt",
 "description": "Mo'in guy entry"
}
```


### [2026-09-05T20:47:33.111Z] TOOL RESULT

```
گوهرنشان: 2.۰.17 [- گسوهر نشاننده) 
(ض‌فا.) نشاننده که‌هر) جواهرنشان. آ 
کٌّوهرنشانده] (ص‌مف.) آنجه که در آن 
گوهر نشانده باشند. هت 
گوی: ۷ | - کو کلو له ۱ 
کلو له (مطلقاً ). گوی عنر: گلوله‌ای از عنبر 
یی تا 
و به هنگام فصد بدست سمار می‌دادند تا 
سوید (لغ.) گوی معنبر: قطعه‌ای از عنبر. 
گلوله‌ای که از چوب سازند و با چوگان بازی 
کنند. گوی در میدان افکندن: گوی بازی 
کردن. مسابقه دادن مناظره کردن. گوی 


۴ ۱ ۵ ۱ 
کشا تکنه. کوعع پبراهن: کج و 
حلقه‌ای که دو بخش پیراهن را بهم متصل 
سازد. گوی آرمیده: کره ساکن (مقدمة 
2 . گوی اغبر: کرة زمین. 
کوع ستته: کر و مت 3 کر فتهی کره‌این که 
و دای تداردهسون کره ماه (مقدمه
```


## [2026-09-05T20:47:41.460Z] TOOL CALL #62: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T20:47:41.501Z] TOOL RESULT

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


## [2026-09-05T20:48:03.161Z] TOOL CALL #63: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ARY && cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ARY/441.vision.txt <<'EOF'\n[Aryanpur Kashani, Farhang-e Rishe-ha-ye Hend-o-Orupayi-ye Zaban-e Farsi, printed p. 441\n = pdf page 440 of ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf. Read from the page image\n (OCR of ARY_pages.txt lines 13078-13105 is badly damaged). Verbatim transcription of the\n table for the headword گلوله, used for verification of PDF page 169 (root \"Gel\").]\n\nسرصفحه: گلوله / ۴۴۱\n\nفارسی (PERSIAN): گلوله — GOLŪLÉ\nچم انگلیسی سرواژه‌ی فارسی: BALL, CLUE, CLEW, SKEIN\nهند و اروپایی (INDO-EUROPEAN): *GLEU-, *GLOU-, *GLU-\n\nکردی (KURDISH): GULŪR, GULŌK, GŪLŪLÉ\nافغانی (پشتو) (AFGHANI): GOLËY, GULËY\nسانسکریت (SANSKRIT): GLĀUS\nیونانی (GREEK): GIG-GLU-MOS\nایسلندی کهن (OLD SCANDINAVIAN): KLŌ\nنورس کهن (OLD NORSE): KLĒ\nساکسنی کهن (OLD SAXON): KLEUWIN\nفریزی کهن (OLD FRISIAN): KLĒ\nآلمانی کهن (OLD HIGH GERMAN): KLIUWA\nآلمانی (GERMAN): KNĀUEL\nانگلیسی کهن (OLD ENGLISH): CLIEWEN\nانگلیسی (ENGLISH): CLUE, CLEW\nهلندی (DUTCH): KLUWEN\nلهستانی (POLISH): GRUDA\nروسی (RUSSIAN): GLUDA\nچکی (CZECH): HROUDA\nاسلواکی (SLOVAK): HRUDA\nایرلندی کهن (OLD IRISH): GLŌ-, GLÁO\n\nپسگشت‌ها (REFERENCES):\n  POKORNY: 361-362\n  BARNHART: (CLUE) 182, (CLUMP) 183\n  SKEAT: (CLEW, CLUE) 114\n  برهان قاطع: ۱۸۳۲\n\nیادداشت:\n  چم این واژه در زبان‌های ژرمنی: گلوله یا گری نخ [= کلاف نخ]\n  چم این واژه در زبان‌های سانسکریت و زبان‌های اسلاوی: قلنبه.\n  چم این واژه در زبان یونانی: بند استخوان، قوزک.\n\n[بلافاصله پس از آن، سرواژه‌ی بعدی:]\nفارسی (PERSIAN): گله (به چم «شکوه و شکایت») — GELÉ ; COMPLAINT\nهند و اروپایی: *GALGH-, *G(A)LAGH- ; اوستایی (AVESTAN): GAREZ, GRƏZA, GAREZA, GƏRƏZATI\nEOF\necho saved; wc -l /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ARY/441.vision.txt",
 "description": "Save ARY vision reading"
}
```


### [2026-09-05T20:48:04.863Z] TOOL RESULT

```
saved
44 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ARY/441.vision.txt
```


## [2026-09-05T20:51:44.559Z] AGENT

Now writing the verification file.


## [2026-09-05T20:57:19.060Z] TOOL CALL #64: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build169.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_GUY = \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%DB%8C\"\nW_GOL = \"https://en.wiktionary.org/wiki/%DA%AF%D9%84%D9%88%D9%84%D9%87\"\nW_KEL = \"https://en.wiktionary.org/wiki/%DA%A9%D9%84%D8%A7%DA%86\"\nW_CLUB = \"https://en.wiktionary.org/wiki/club\"\nFR_CLUB = \"https://fr.wiktionary.org/wiki/club\"\nE_CLUB = \"https://www.etymonline.com/word/club\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"gŭy «گوی»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"NP گوی gōy/gūy 'ball' (especially the polo ball struck with the چوگان) is genuine and correctly glossed — Mo'in s.v. گوی: '[= گو، گلوله] ... گلوله‌ای که از چوب سازند و با چوگان بازی کنند' — and the Hāfez couplet quoted in the box is authentic. What is wrong is the arrow. The word goes back to Middle Persian gōy, spelt <gwd> in Book Pahlavi (MacKenzie, CPD p.37: 'gōy [gwd | N ~] ball'), and that -d- points to an older stem in *-d-. Nourai's own reference is against him: Mann, IEC p.303, lemmatises the word not under gel-/gliu- (which he treats at p.279) but under a separate entry 'gūd- (2) \\\"lump, ball\\\". Per gūy, id. (fr. *gūdio-); Arm. kujt ... \\\"pile, mass\\\"; MLG küte; Du. kuit'. Pokorny's gel- article (357-364) never cites NP gūy, although it does cite NP gulūle (p.361). Wiktionary likewise groups گوی with Skt. गोल gola- 'ball', Central Kurdish گولە gule / گۆ go, N. Kurdish gog, Zazaki gudi 'ball' — i.e. the *gaud-/*gud- 'bend, round thing' family, not *gel-.\",\n \"derivation_fa\": \"واژهٔ «گوی» به معنی گوی و توپ (به‌ویژه گویِ چوگان) از فارسی میانهٔ gōy است که در پهلوی کتابی <gwd> نوشته می‌شود (مکنزی، فرهنگ کوچک پهلوی، ص ۳۷)؛ همین املای با «د» نشان می‌دهد ستاک کهن‌تر دارای ‑d‑ بوده است. خودِ مأخذی که نورایی آورده — مان، فرهنگ تطبیقی هندواروپایی، ص ۳۰۳ — این واژه را نه ذیل gel- بلکه ذیل مدخل جداگانهٔ gūd- «توده، گوی» می‌آورد: «Per gūy, id. (fr. *gūdio-)»، همراه با ارمنی kujt و هلندی kuit. پوکورنی نیز در سراسر مقالهٔ gel- (ص ۳۵۷–۳۶۴) نامی از «گوی» فارسی نمی‌برد، هرچند gulūle را می‌آورد. ویکی‌واژه هم «گوی» را با سنسکریت gola-، کردی گولە/گۆ و زازاکی gudi هم‌ریشه می‌داند، یعنی خانوادهٔ *gaud-/*gud-. پس واژه و معنا درست‌اند ولی پژوهش امروزی پیوند آن را با ریشهٔ *gel- رد می‌کند.\",\n \"sources\": [W_GUY],\n \"ref_check\": [\n   {\"ref\": \"IEC:303\", \"status\": \"contradicts\", \"note\": \"Mann, An Indo-European Comparative Dictionary, printed p.303 (local IEC.txt, form-feed leaf 180): 'güd- (2) \\\"lump, ball\\\". Per güy, id. (fr. *gūdio-); Arm. kujt, gs kuti, i-st. \\\"pile, mass\\\" ... MLG küte \\\"bundle of flax\\\"; Du. kuit \\\"calf of leg\\\"'. The page cited does contain Persian gūy, but assigns it to *gūd-, a lemma Mann keeps entirely separate from his gel-/gliu- material (p.279 'gliu- (glou-) \\\"ball, clump\\\" ... Skt. glau \\\"lump, goitre\\\"').\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 37 s.v. gōy\", \"stance\": \"partial\", \"note\": \"'göy [gwd | N ~] ball' — confirms the Middle Persian etymon and shows the <gwd> spelling, but gives no IE root.\"},\n   {\"src\": \"MON\", \"where\": \"s.v. گوی (2-vol. Adena reprint, MON_part2 line 37074)\", \"stance\": \"partial\", \"note\": \"'گوی: [= گو، گلوله] ... گلوله‌ای که از چوب سازند و با چوگان بازی کنند' — word and sense confirmed, no etymology.\"},\n   {\"src\": \"HRN\", \"where\": \"grepped HRN.txt for gūi/güi/Ball\", \"stance\": \"silent\", \"note\": \"Horn has no article for گوی; his no. 929 covers gulūle only.\"},\n   {\"src\": \"ARY\", \"where\": \"grepped ARY_pages.txt and ARY_latin_index_pages.txt for گوی / GUY / GOY\", \"stance\": \"silent\", \"note\": \"Aryanpur has no entry for گوی (he does have گلوله at p.441).\"},\n   {\"src\": \"IEC\", \"where\": \"p. 303 s.v. gūd- (2)\", \"stance\": \"contradicts\", \"note\": \"see ref_check — separate lemma *gūd-, not gel-.\"}\n ]})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Sanskrit\", \"words\": \"glâv, gula, glâu-h\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All three shapes are real. Skt. gula-, gulī, gulikā 'Kugel, Ball, Perle, Pille' are cited by Pokorny at p.357 under the bare root gel-, i.e. under the very form Nourai heads the chart with; glāu- (nom. sg. glāuḥ) 'Ballen, Kugel, geballte Masse' — 'lump, wen, ball' — is cited at p.361 under the u-extension g(e)l-eu-. 'glâv' is simply the stem glāv- as Horn writes it (no. 929: 'Vergl. ai. glāv- \\\"Ballen, kropfartiger Auswuchs\\\"'), and Nourai's gloss 'parcel' is a loose rendering of 'compact mass'. One reservation: Walde-Pokorny (Bd. I, s.v. 1. gel-) hesitate over gula-, allowing that it may contain an l-suffix and belong to *geu- 'to bend' instead.\",\n \"derivation_fa\": \"هر سه صورت سنسکریت درست‌اند: gula-, gulī, gulikā «گوی، مهره، گلوله، حَب» را پوکورنی در ص ۳۵۷ ذیل صورت سادهٔ ریشه می‌آورد و glāu- (نهادی glāuḥ) «توده، گوی، تودهٔ فشرده» را در ص ۳۶۱ ذیل گسترش g(e)l-eu-. صورت «glâv» همان ستاک glāv- است که هرن (شمارهٔ ۹۲۹) نیز به همین شکل می‌نویسد، و «parcel» ترجمهٔ آزادِ «تودهٔ فشرده» است. تنها احتیاط این است که والده-پوکورنی دربارهٔ gula- تردید دارند و احتمال می‌دهند با پسوند ‑l‑ از *geu- «خم شدن» باشد. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:357, 361\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 13 (= printed p.357): 'gel- \\\"ballen, sich ballen; Gerundetes, Kugeliges\\\" ... Ai. gula-h, gulī (Lex.), gulikā \\\"Kugel, Ball, Perle\\\"'; leaf 17 (= p.361): 'D. g(e)l-eu- ... Ai. glāu-h f. \\\"Ballen, Kugel, geballte Masse\\\", npers. gulūle \\\"Kugel\\\"'. Both cited pages say exactly what the node claims.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I, art. '1. gel- \\\"ballen; gerundetes, kugeliges u. dgl.\\\"' (WLD_Bd1 djvu line 58069) and Bd. I 617 (line 58669)\", \"stance\": \"supports\", \"note\": \"'Ai. gula-h gulī (Lex.), gulika \\\"Kugel, Spielball, Perle, Pille\\\" (oder mit l-Suffix zu *geu- \\\"biegen\\\"?)'; and 'ai. glau-h \\\"Ballen, Kugel, geballte Masse\\\", np. gulūle \\\"Kugel\\\"'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 12.83 'Sphere', printed p.908\", \"stance\": \"supports\", \"note\": \"'OE cliwen ... : Skt. glau- \\\"round lump\\\", NPers. gulūle \\\"ball\\\", fr. *gleu- ... Walde-P. 1.617.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gel-1\", \"stance\": \"silent\", \"note\": \"Watkins's entry lists no Sanskrit under gel-1 at all (only Germanic, Latin, Greek, Slavic); it neither supports nor contradicts the Sanskrit forms.\"}\n ]})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"gulleh «گولّه»; goluleh «گلوله»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The words are right and the root is right, but the direction of the arrow is not: NP گلوله golūle 'ball, pellet, bullet' is an inherited Iranian word, not a loan from Sanskrit. Pokorny prints it side by side with the Sanskrit under the u-extension — 'Ai. glāu-ḥ ... npers. gulūle \\\"Kugel\\\"' (p.361 = WP I 617) — and Buck does the same at 12.83 (p.908): 'Skt. glau- \\\"round lump\\\", NPers. gulūle \\\"ball\\\", fr. *gleu-'. Horn no. 929 lists NP gulūle, gōle and Kāšānī gulī, gulla and says only 'Vergl. ai. glāv-'. Aryanpur (p.441) heads the entry گلوله GOLŪLÉ with 'INDO-EUROPEAN *GLEU-, *GLOU-, *GLU-' and gives Kurdish GULŪR, GULŌK, Pashto GOLËY, Skt. GLĀUS, OE CLIEWEN, E CLUE/CLEW as cognates. So the two are cognates from *gleu-, i.e. siblings, not parent and child. گولّه gulle is the same word shortened (Mo'in has گلّه gulle 'تودهٔ (هر چیز)'; Horn's Kāšān gulla; Kurdish gulle, gulōk); the 'bullet' sense is post-gunpowder, and Ottoman/Turkish gülle 'cannon-ball' is borrowed from this Persian word, not the reverse. Wiktionary: 'Inherited from Proto-Iranian ... ultimately from Proto-Indo-European *glew-', cognate Skt. ग्लौ glau 'lump'.\",\n \"derivation_fa\": \"فارسی «گلوله» واژه‌ای ایرانی و ارثی است، نه وام از سنسکریت. پوکورنی در ص ۳۶۱ آن را دوش‌به‌دوش سنسکریت می‌آورد («Ai. glāu-ḥ ... npers. gulūle 'Kugel'») و باک در بند ۱۲٫۸۳ (ص ۹۰۸) نیز هر دو را از *gleu- می‌گیرد. هرن (شمارهٔ ۹۲۹) صورت‌های gulūle، gōle و کاشانی gulī, gulla را می‌آورد و تنها می‌نویسد «قس. سنسکریت glāv-»؛ معین نیز در حاشیهٔ برهان قاطع (ص ۱۸۳۲) می‌نویسد «= غلوله. قس: هندی‌باستان glāv-»؛ آریان‌پور (ص ۴۴۱) مدخل «گلوله» را با ریشهٔ هندواروپایی *GLEU-, *GLOU-, *GLU- می‌آورد. پس این دو هم‌ریشه‌اند و پیکانِ «سنسکریت ← فارسی» رابطه را نادرست نشان می‌دهد. «گولّه/گلّه» صورت کوتاه‌شدهٔ همان واژه است (معین: گلّه «تودهٔ هر چیز»؛ کردی gulle، gulōk) و معنی «فشنگ» پس از پیدایش باروت رواج یافته است؛ ترکی gülle «گلولهٔ توپ» خود وام‌گرفته از فارسی است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W_GOL],\n \"ref_check\": [\n   {\"ref\": \"POK:361\", \"status\": \"partial\", \"note\": \"POK_02.txt leaf 17 (printed p.361): 'D. g(e)l-eu- ... Ai. glāu-h f. \\\"Ballen, Kugel, geballte Masse\\\", npers. gulūle \\\"Kugel\\\"'. The page has both words under one root, but as parallel reflexes of *g(e)l-eu-; it does not derive the Persian from the Sanskrit.\"},\n   {\"ref\": \"MON:3382\", \"status\": \"supports\", \"note\": \"Mo'in has the words (2-vol. Adena reprint: گلوله with compounds گلولهٔ مشقی/منوّر/گلوله‌باران, and گلّه 'توده (هر چیز)' at MON_part2 lines 34795-34840). Nourai's page 3382 belongs to the 6-vol. Amir Kabir printing (its ک/گ range 3015-3382 is internally consistent); our scan paginates differently.\"},\n   {\"ref\": \"BQT:1861\", \"status\": \"partial\", \"note\": \"In the Mo'in edition scanned as BQT_v3_picofile.pdf, the entry is at printed p.1832 (pdf p.629): 'گلوله - بروزن و معنی غلوله است ... گلوله ریسمان و غیره باشد', with Mo'in's own footnote '= غلوله. قس: هندی‌باستان glāv-' (and Kurdish gulōk). Printed p.1861 of that same printing (pdf p.658) carries گومست/گونه/گونا, no گلوله. Aryanpur independently cites this entry as 'برهان قاطع: ۱۸۳۲', so Nourai's 1861 looks like a slip of ~29 pages; the substance of the reference supports him.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 929, p. 208\", \"stance\": \"supports\", \"note\": \"'929. gulūle \\\"Kugel\\\", gōle. Kāš. gulī, gulla. Vergl. ai. glāv- \\\"Ballen, kropfartiger Auswuchs\\\"; γλουτός; ags. cleowen, ahd. chliuwa \\\"Knäuel\\\".' — cognate, not borrowing.\"},\n   {\"src\": \"ARY\", \"where\": \"p. 441 s.v. گلوله GOLŪLÉ (page image read; saved to sources/refs/ocr/ARY/441.vision.txt)\", \"stance\": \"supports\", \"note\": \"'هند و اروپایی (INDO-EUROPEAN): *GLEU-, *GLOU-, *GLU-'; cognates GLĀUS (Skt.), CLIEWEN (OE), CLUE/CLEW (E), Kurdish GULŪR/GULŌK; references 'POKORNY 361-362 ... برهان قاطع ۱۸۳۲'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 12.83, printed p.908\", \"stance\": \"supports\", \"note\": \"'Skt. glau- \\\"round lump\\\", NPers. gulūle \\\"ball\\\", fr. *gleu-'.\"},\n   {\"src\": \"BQT\", \"where\": \"printed p.1832 (pdf p.629 of BQT_v3_picofile.pdf), Mo'in's footnote 4\", \"stance\": \"supports\", \"note\": \"'= غلوله . قس : هندی‌باستان glāv-' — Mo'in himself makes the Sanskrit comparison Nourai draws.\"},\n   {\"src\": \"MON\", \"where\": \"s.v. گلّه (MON_part2 line 34840)\", \"stance\": \"supports\", \"note\": \"'گلّه (ا.) توده (هر چیز)' — the short form گلّه/گولّه 'lump, mass' is lexicalised in Mo'in.\"}\n ]})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Latin\", \"words\": \"globus; gluten\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"globus 'ball, sphere, dense mass (also a military formation, a crowd)' is placed by Pokorny at p.359 under the labial extension geleb(h)-/gleb(h)- 'zusammenballen', beside gleba 'clod of earth' ('lat. globus m. \\\"Kugel, Haufe, Klumpen\\\", dehnstufig lat. gleba'); Watkins: 'Extended form *glob- perhaps in Latin globus'. gluten (gen. glūtinis) 'glue' belongs to the other extension, glei- 'kleben, schmieren' (POK 363: 'lat. glūs, -tis, glūten, -inis n. \\\"Leim\\\", glūtinō'), i.e. to Nourai's 'Geli'; since his root header carries both extensions, both words are legitimately in this box. Ernout-Meillet are more reserved on globus ('Cf. glēba et glomus. Aucun rapprochement sûr') but accept the gl- root for gluten, comparing OIr. glenaid 'it sticks', OHG klenan, Lith. glieju, Gk. γλία and OE clǣg 'clay'.\",\n \"derivation_fa\": \"لاتین globus «گوی، توده، انبوه» را پوکورنی در ص ۳۵۹ ذیل گسترش لبیِ geleb(h)-/gleb(h)- «به‌هم فشردن» در کنار gleba «کلوخ» می‌آورد و واتکینز آن را «صورت گستردهٔ *glob-» می‌داند. اما gluten «سریش» به شاخهٔ دیگری تعلق دارد: glei- «چسبیدن، مالیدن» (پوکورنی ص ۳۶۳: «lat. glūs, -tis, glūten, -inis n. Leim»)، یعنی همان «Geli» سرلوحهٔ نورایی؛ چون هر دو گسترش در سرلوحه آمده‌اند، جای هر دو واژه در این جعبه درست است. ارنو–مِیه دربارهٔ globus محتاط‌ترند («هیچ مقایسهٔ مطمئنی نیست») ولی دربارهٔ gluten ریشهٔ gl- را می‌پذیرند و آن را با ایرلندی باستان glenaid و آلمانی علیای باستان klenan می‌سنجند. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985, gel-1 'To form into a ball': 'I.7 Extended form *glob- perhaps in Latin globus, ball, globe: GLOBE, (GLOBULE); CONGLOBATE' and 'III.3 Extended form *gleu- in Latin glūten, glue: GLUE, GLUTEN, GLUTINOUS'. [Pok. 1. gel- 357]\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"printed pp. 359, 363\", \"stance\": \"supports\", \"note\": \"p.359 'geleb(h); gleb(h)- ... lat. globus m. \\\"Kugel, Haufe, Klumpen\\\"'; p.363 'E. glei- ... lat. glūs, -tis, glūten, -inis n. \\\"Leim\\\"'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.vv. globus and gluten (LAT.txt lines 26373, 26461)\", \"stance\": \"partial\", \"note\": \"globus: 'Cf. glēba et glomus. Aucun rapprochement sûr' — no firm IE etymology; gluten: 'La racine, sans doute élargissement de la forme en gl- qui se trouve dans gleba et glomus, est attestée par ... irl. glenaid \\\"il s'attache\\\" ... v.h.a. klenan ... lit. glieju ... gr. γλία'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.vv. globe, glebe\", \"stance\": \"supports\", \"note\": \"'glebe ... in gradational relationship to globus, \\\"ball, sphere\\\" ... fr. I.-E. base *gelebh-, *glebh-, \\\"to roll up into a ball, compress\\\"' — Klein even writes the base in the shape Nourai heads the chart with (Geleb).\"}\n ]})\n\nnodes.append({\n \"id\": 5, \"lang\": \"French\", \"words\": \"globule\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"French globule is not a popular descendant of globus but a learned formation taken from Latin globulus, the regular diminutive of globus, into scientific French of the 16th-17th c. (Klein: 'globule, n. — F., fr. L. globulus, \\\"a little ball\\\", dimin. of globus'). Ernout-Meillet list globulus among the dérivés of globus. So the chart's Latin→French arrow is right in substance; only the intermediate globulus is left implicit.\",\n \"derivation_fa\": \"فرانسهٔ globule دنبالهٔ عامیانهٔ globus نیست، بلکه ساختی عالمانه از globulus لاتین (مصغّرِ قاعده‌مندِ globus) است که در سده‌های شانزدهم–هفدهم وارد زبان علمی فرانسه شد (کلاین: «globule, n. — F., fr. L. globulus, a little ball, dimin. of globus»). ارنو–مِیه نیز globulus را در شمار مشتقات globus می‌آورند. پس پیکانِ لاتین ← فرانسه در جوهر درست است و تنها حلقهٔ میانی globulus در نمودار نیامده است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"The node carries no reference of its own in the book (refs=None); the claim is covered by the Latin box's AHD citation.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. globule (KLN_1971 line 103513)\", \"stance\": \"supports\", \"note\": \"'globule, n., a very small spherical body; a drop. — F., fr. L. globulus, \\\"a little ball\\\", dimin. of globus.'\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. globus, list of dérivés\", \"stance\": \"supports\", \"note\": \"'Dérivés: globo,-as ... globulus m.; globōsus ... conglobō' — globulus is a Latin, not a French, coinage.\"}\n ]})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Persian\", \"words\": \"golobŭl «گلبول»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"گلبول is a modern medical loan taken straight from French globule during the French-mediated medicalisation of Persian in the late Qajar / early Pahlavi period. Mo'in prints it with its Latin-script French source and the tag (فیزیول.): 'گلبول: [globule] (ا.) هر یک از سلول‌های موجود در خون جانوران که به دو نوع گلبول‌های قرمز و سفید موجودند'. The standard compounds گلبول قرمز / گلبول سفید are calques of globule rouge / globule blanc, and the final -ul (not English -yool) shows the French, not the English, source.\",\n \"derivation_fa\": \"«گلبول» وام‌واژه‌ای پزشکی و نو است که از راه فرانسه (globule) در اواخر دورهٔ قاجار و آغاز پهلوی وارد فارسی شد؛ معین آن را با صورت لاتینی فرانسوی و نشانهٔ (فیزیول.) می‌آورد: «گلبول: هر یک از سلول‌های موجود در خون جانوران که به دو نوع گلبول‌های قرمز و سفید موجودند». ترکیب‌های «گلبول قرمز/سفید» گرته‌برداری از globule rouge/blanc فرانسوی‌اند و صورت آوایی پایانی نیز فرانسوی بودن مأخذ را نشان می‌دهد نه انگلیسی. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"MON:3363\", \"status\": \"supports\", \"note\": \"Entry found in the 2-vol. Adena reprint of Farhang-e Farsi (MON_part2 lines 34331-34346, running head page ۱۸۳۳): 'گلبول: [globule] (فیزیول.) (ا.) هر یک از سلول‌های موجود در خون جانوران که به دو نوع گلبول‌های قرمز و سفید موجودند ... در هر میلی‌متر مکعب در حدود ۵ میلیون گلبول قرمز وجود دارد.' The page number differs because our scan is a different printing from Nourai's 6-vol. Amir Kabir edition.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. گلبول\", \"stance\": \"supports\", \"note\": \"see ref_check — Mo'in gives the French Latin-script headword beside the Persian.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. globule\", \"stance\": \"supports\", \"note\": \"'globule, n. — F., fr. L. globulus' — confirms that the immediate donor of the Persian form is the French word, as the chart draws it.\"}\n ]})\n\nnodes.append({\n \"id\": 7, \"lang\": \"English\", \"words\": \"globe, globule, glue\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All three reach Latin through French rather than directly, which the chart compresses into one Latin→English arrow. globe: from French globe, from L. globus (Klein: 'globe, n. — F., fr. L. globus, \\\"a round body, ball, sphere\\\"'). globule: from French globule, from L. globulus. glue: ME glu, from Old French (= F.) glu 'birdlime', from Late Latin glūtem, accusative of glūs, beside classical L. gluten 'glue' (Klein). Watkins files GLOBE and (GLOBULE) under the extension *glob-, and GLUE, GLUTEN, GLUTINOUS under *gleu- in Latin glūten — so the origin as drawn is right; only the French stage is left out.\",\n \"derivation_fa\": \"هر سه واژهٔ انگلیسی از راه فرانسه به لاتین می‌رسند و نمودار این حلقه را حذف کرده است: globe از فرانسهٔ globe از لاتین globus؛ globule از فرانسهٔ globule از globulus؛ و glue از انگلیسی میانهٔ glu از فرانسهٔ باستان glu «چسبِ پرنده‌گیری» از لاتین متأخر glūtem (حالت رایی glūs) در کنار gluten کلاسیک (کلاین). واتکینز نیز GLOBE و GLOBULE را ذیل *glob- و GLUE و GLUTEN را ذیل *gleu- (لاتین glūten) می‌آورد. پس خاستگاه درست است و پیکانِ مستقیمِ «لاتین ← انگلیسی» تنها ساده‌سازی است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. gel-1: 'I.7 ... Latin globus, ball, globe: GLOBE, (GLOBULE); CONGLOBATE'; 'III.3 Extended form *gleu- in Latin glūten, glue: GLUE, GLUTEN, GLUTINOUS; AGGLUTINATE, CONGLUTINATE, DEGLUTINATE'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.vv. globe (line 103491), globule (103513), glue (103770)\", \"stance\": \"supports\", \"note\": \"'globe, n. — F., fr. L. globus'; 'globule, n. — F., fr. L. globulus'; 'glue, n. — ME., fr. OF. (= F.) glu, \\\"birdlime\\\", fr. Late L. glutem, acc. of glus, fr. L. gluten'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. gluten\", \"stance\": \"supports\", \"note\": \"'glutis,-is (Marcell.) m. puis f., sur lequel a été fait au nominatif glūs ... devenu [glu] dans les l. romanes. M.L.3806; britt. glud' — the Late Latin form that gave OF glu.\"}\n ]})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Germanic\", \"words\": \"klukjan\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"*klukjan is the Germanic (in fact West Germanic) reconstruction behind Old English clyccan 'to clutch, clench', with -jan the class-I weak verb suffix; this is the form printed in the 1975 AHD appendix that Nourai cites, while Watkins's 1985 revision prints the base more cautiously as 'Germanic *kluk- in Old English clyccan, to clutch' (gel-1, II.7). Pokorny reaches the same word from the guttural extension gel-g-/glek-: 'ags. clyccan \\\"packen, greifen\\\" (engl. clutch)' (p.358). The material is confined to Germanic and Pokorny warns that this whole velar-extension group 'macht keinen idg. Eindruck', but the Germanic etymon itself is standard.\",\n \"derivation_fa\": \"*klukjan صورت بازسازی‌شدهٔ ژرمنی (در واقع ژرمنی باختری) پشتِ انگلیسی باستان clyccan «چنگ زدن، مشت کردن» است و پسوند ‑jan همان نشانهٔ فعل ضعیف طبقهٔ یکم است. پیوستِ هندواروپاییِ فرهنگ American Heritage در ویراست ۱۹۷۵ — که نورایی به آن ارجاع می‌دهد — همین صورت را می‌آورد و ویرایش واتکینز (۱۹۸۵) محتاطانه‌تر *kluk- می‌نویسد. پوکورنی نیز در ص ۳۵۸ ذیل گسترش کامیِ glek- می‌آورد: «ags. clyccan 'packen, greifen' (engl. clutch)». هرچند خودِ پوکورنی هشدار می‌دهد که این دسته «نمای هندواروپایی ندارد»، ستاک ژرمنی معیار است و ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985, gel-1, II.7: 'Germanic *kluk- in Old English clyccan, to clutch: CLUTCH1.' (The 1975 New College appendix, Nourai's actual source, prints *klukjan.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"printed p. 358\", \"stance\": \"supports\", \"note\": \"'a.-s. clyccan \\\"packen, greifen\\\" (engl. clutch)' under 'A. Gutturalerweiterungen: gel-g-, glek-'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. clutch (KLN_1971 line 49399)\", \"stance\": \"partial\", \"note\": \"'clutch ... fr. OE. clyccean, \\\"to bring together, clench\\\", rel. to OFris. kletsie, \\\"spear\\\", Swed. klyka, \\\"crotch, fork\\\", and to E. cling' — Klein gives the OE etymon and the cognates but no starred Germanic form.\"}\n ]})\n\nnodes.append({\n \"id\": 9, \"lang\": \"English\", \"words\": \"clutch\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English clutch 'to seize with the hands' is ME clucchen, clicchen, from OE clyccan 'to bring together, clench' (Klein), i.e. exactly the Germanic etymon of the parent box. The mechanical noun 'coupling that engages and disengages a shaft' is a 19th-c. English engineering use of the same word ('a grasping device', 1814), transferred to the motor-car coupling from the 1890s — the sense the Persian daughter borrows. (English clutch 'brood of eggs' is an unrelated word, from cluck; Klein flags it separately.)\",\n \"derivation_fa\": \"انگلیسی clutch «چنگ زدن، محکم گرفتن» از انگلیسی میانهٔ clucchen/clicchen و آن از انگلیسی باستان clyccan «به‌هم آوردن، مشت کردن» است (کلاین)، یعنی دقیقاً همان ستاک ژرمنیِ جعبهٔ بالادست. معنای مکانیکیِ «کلاچ، کوپلینگ» کاربردی فنی از همین واژه در انگلیسیِ سدهٔ نوزدهم است (نخست «ابزار چنگ‌زننده»، ۱۸۱۴) که از دههٔ ۱۸۹۰ به کوپلینگ خودرو اطلاق شد — و همین معناست که به فارسی وام داده شده. توجه شود که clutch به معنی «کُرچهٔ تخم‌مرغ» واژهٔ دیگری است (از cluck) و به این ریشه ربطی ندارد. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985, gel-1 II.7 ends '...to clutch: CLUTCH1' — i.e. English clutch is filed under this root.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. clutch, tr. and intr. v.\", \"stance\": \"supports\", \"note\": \"'clutch, tr. and intr. v., to seize with the hands. — ME. clucchen, clicchen, fr. OE. clyccean, \\\"to bring together, clench\\\"'.\"},\n   {\"src\": \"POK\", \"where\": \"printed p. 358\", \"stance\": \"supports\", \"note\": \"'ags. clyccan \\\"packen, greifen\\\" (engl. clutch)'.\"}\n ]})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Persian\", \"words\": \"kelâč «کلاچ»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"کلاچ is a 20th-c. automotive loan taken directly from English clutch, together with the motor car itself. Persian does not tolerate an initial kl- cluster, so the English [klʌtʃ] is resolved with an epenthetic vowel as ke-lâč, the â rendering the English open vowel. Mo'in: 'کلاچ ... آلتی است در اتومبیل که به وسیلهٔ آن راننده با اتصال وی به موتور نیروی دوران موتور را به جعبهٔ دنده و چرخ‌های اتومبیل انتقال می‌دهد، همچنین با انفصال آن از موتور اتومبیل را از حرکت باز می‌دارد. پدال کلاچ ...'. Wiktionary s.v. کلاچ: 'Borrowed from English clutch.'\",\n \"derivation_fa\": \"«کلاچ» وام‌واژه‌ای است که در سدهٔ چهاردهم خورشیدی همراه با خودرو مستقیماً از انگلیسی clutch گرفته شده است. چون فارسی خوشهٔ آغازین kl- را نمی‌پذیرد، واکهٔ میانجیِ e افزوده شده و [klʌtʃ] انگلیسی به kelâč بدل شده است. معین می‌نویسد: «کلاچ … آلتی است در اتومبیل که به وسیلهٔ آن راننده با اتصال وی به موتور نیروی دوران موتور را به جعبهٔ دنده و چرخ‌های اتومبیل انتقال می‌دهد … پدال کلاچ». ویکی‌واژه نیز آن را «وام‌گرفته از انگلیسی clutch» می‌داند. ادعای نورایی درست است.\",\n \"sources\": [W_KEL],\n \"ref_check\": [\n   {\"ref\": \"MON:3015\", \"status\": \"supports\", \"note\": \"Entry found in the 2-vol. Adena reprint (MON_part2 lines 24512-24523, running head page ۱۳۷۵): 'کلاچ: (ا.) (مکد.) آلتی است در اتومبیل که به وسیلهٔ آن راننده ... نیروی دوران موتور را به جعبهٔ دنده و چرخ‌های اتومبیل انتقال می‌دهد ... پدال کلاچ'. Pagination differs from Nourai's 6-vol. Amir Kabir printing.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. کلاچ\", \"stance\": \"supports\", \"note\": \"see ref_check; Mo'in marks it a mechanical (مکد. = مکانیک) term, i.e. a technical Europeanism.\"},\n   {\"src\": \"ARY\", \"where\": \"grepped ARY_pages.txt for کلاچ\", \"stance\": \"silent\", \"note\": \"Aryanpur covers only inherited Indo-European vocabulary; modern loans such as کلاچ are not in it.\"}\n ]})\n\nnodes.append({\n \"id\": 11, \"lang\": \"Germanic\", \"words\": \"klub\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The Germanic etymon behind club is Old Norse klubba / klumba 'a thick stick, cudgel' (Klein), from Gmc *klubbōn- / *klumbōn-, the geminated and nasalised variants of the *kleub-/*klemb- material Pokorny sets under the labial extension geleb(h)-: 'tiefstufig anord. klubba \\\"Keule\\\", woher engl. club' (p.360); Watkins: 'Germanic *klub(b)- in Old Norse klubba, a lump of wood, club'. Two qualifications: the word is Scandinavian, not common Germanic, and Nourai's gloss 'a lump or group' back-projects the later English semantic development ('lump' → 'body of people') onto the Germanic etymon, which means only 'club, cudgel, block of wood'.\",\n \"derivation_fa\": \"ستاک ژرمنیِ پشتِ club انگلیسی، نورس باستان klubba/klumba «چماق، چوب کلفت» است، از ژرمنی *klubbōn-/*klumbōn-، که خود گونهٔ مشدّد و خیشومی‌شدهٔ همان مادهٔ *kleub-/*klemb- است که پوکورنی ذیل گسترش لبیِ geleb(h)- می‌آورد (ص ۳۶۰: «tiefstufig anord. klubba 'Keule', woher engl. club»)؛ واتکینز نیز *klub(b)- را ثبت کرده است. دو ملاحظه: نخست اینکه واژه اسکاندیناویایی است نه ژرمنیِ مشترک؛ دوم اینکه معنایی که نورایی داده («توده یا گروه») تحول معنایی متأخرِ انگلیسی را به صورت ژرمنی نسبت می‌دهد، حال آنکه در ژرمنی تنها «چماق، کندهٔ چوب» معنی می‌دهد. با احتیاط پذیرفتنی است.\",\n \"sources\": [E_CLUB, W_CLUB],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985, gel-1 I.2: 'Germanic *klub(b)- in Old Norse klubba, a lump of wood, club: CLUB1.' The form is supported; the gloss 'a lump or group' is not — Watkins glosses it 'a lump of wood, club'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.vv. club (KLN_1971 line 49330) and clump (line 49356)\", \"stance\": \"supports\", \"note\": \"'club, n. — ME. clubba, fr. ON. klubba, klumba, \\\"a thick stick, club\\\". See clump'; under clump: 'ON. klumba, klubba, \\\"a thick stick, club\\\"'.\"},\n   {\"src\": \"POK\", \"where\": \"printed p. 360\", \"stance\": \"supports\", \"note\": \"'germ. expressives *klabb- in norw. dial. klabb \\\"anhaftender Klumpen\\\" ... (tiefstufig anord. klubba \\\"Keule\\\", woher engl. club)' under geleb(h)-.\"}\n ]})\n\nnodes.append({\n \"id\": 12, \"lang\": \"French\", \"words\": \"club\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The ultimate origin is right but the route as drawn is not: French club is not taken from Germanic directly, it is borrowed from English. Wiktionnaire dates the 'society' sense to 1702 ('De l'anglais club (\\\"bâton, société\\\")') and treats the 'golf stick' sense as a separate late-19th-c. re-borrowing; it is one of the classic 18th-c. anglicismes of the salons, made famous by the Revolution (Club des Jacobins, 1789). So the chart should read Germanic (ON klubba) → English club → French club → Persian کلوب.\",\n \"derivation_fa\": \"خاستگاه نهایی درست است ولی مسیر نه: فرانسهٔ club مستقیماً از ژرمنی گرفته نشده، بلکه وام‌واژه‌ای از انگلیسی است. ویکی‌واژهٔ فرانسوی سال ۱۷۰۲ را برای معنای «انجمن» ثبت می‌کند («De l'anglais club») و معنای «چوگان گلف» را وام‌گیریِ دوبارهٔ اواخر سدهٔ نوزدهم می‌داند؛ این واژه از انگلیسی‌مآبی‌های مشهور سدهٔ هجدهم فرانسه است که انقلاب فرانسه آن را همه‌گیر کرد (Club des Jacobins، ۱۷۸۹). پس زنجیرهٔ درست چنین است: نورس باستان klubba ← انگلیسی club ← فرانسه club ← فارسی «کلوب». ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [FR_CLUB, E_CLUB],\n \"ref_check\": [\n   {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. club\", \"stance\": \"partial\", \"note\": \"Klein takes English club from ON klubba and says nothing of a Germanic→French route, which is what the chart draws.\"},\n   {\"src\": \"WEB\", \"where\": \"fr.wiktionary.org/wiki/club (archived via fetch_source.py)\", \"stance\": \"contradicts\", \"note\": \"'De l'anglais club (« bâton, société »)', dated 1702 — French borrowed the word from English, not from Germanic directly.\"}\n ]})\n\nnodes.append({\n \"id\": 13, \"lang\": \"Persian\", \"words\": \"klub «کلوب»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian کلوب klub 'club, association' is a French loan of the late Qajar / early Pahlavi period, like most of the European vocabulary that entered Persian through French schooling and journalism. Mo'in glosses it with its Latin-script source: 'کلوب: [Club] (ا.) باشگاه، انجمن'. Decisive for the donor language is the vowel: Persian has u, matching French club [klœb/klyb], not the English [klʌb]; and the Persian replacement word باشگاه was coined by the Farhangestān against precisely this French loan. So Nourai's French→Persian arrow is correct.\",\n \"derivation_fa\": \"«کلوب» وام‌واژه‌ای فرانسوی از اواخر دورهٔ قاجار و آغاز پهلوی است، مانند بیشتر واژگان اروپاییِ فارسی که از راه مدرسه و روزنامهٔ فرانسوی‌مآب وارد شدند؛ معین آن را با صورت لاتینیِ Club می‌آورد: «کلوب: باشگاه، انجمن». نشانهٔ قاطعِ فرانسوی بودن مأخذ، واکهٔ u است که با تلفظ فرانسوی می‌خواند نه با [klʌb] انگلیسی؛ افزون بر این واژهٔ جایگزینِ «باشگاه» را فرهنگستان دقیقاً در برابر همین وام‌واژهٔ فرانسوی ساخت. پس پیکانِ «فرانسه ← فارسی» درست است.\",\n \"sources\": [FR_CLUB],\n \"ref_check\": [\n   {\"ref\": \"MON:3039\", \"status\": \"supports\", \"note\": \"Entry found in the 2-vol. Adena reprint (MON_part2 line 25456, running head page ۱۳۸۵): 'کلوب: [Club] (ا.) باشگاه، انجمن.' Mo'in prints the European source form in Latin script, as he does for other French loans. Pagination differs from Nourai's 6-vol. printing.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. کلوب\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"WEB\", \"where\": \"fr.wiktionary.org/wiki/club (archived)\", \"stance\": \"supports\", \"note\": \"confirms that a French word club existed from 1702 and could serve as the donor of the Persian form.\"}\n ]})\n\nnodes.append({\n \"id\": 14, \"lang\": \"English\", \"words\": \"club\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English club is a Norse loan of the Danelaw period, not an inherited Old English word: 'c.1200, \\\"thick stick wielded in the hand and used as a weapon\\\", from Old Norse klubba \\\"cudgel\\\"' (Etymonline); Klein: 'club, n. — ME. clubba, fr. ON. klubba, klumba, \\\"a thick stick, club\\\"'. The 'association' sense is a native English development from the verb 'to club (together), gather in a club-like mass' (1620s), whence the noun 'association of people' (1640s) and 'company meeting in a tavern' by 1659-60 — the sense that France and then Persia borrowed.\",\n \"derivation_fa\": \"انگلیسی club واژه‌ای وام‌گرفته از نورس باستان در دورهٔ دِین‌لا است، نه واژه‌ای ارثی از انگلیسی باستان: از حدود ۱۲۰۰ م. به معنی «چوب کلفت به‌عنوان سلاح» از klubba نورسی (اتیمانلاین؛ کلاین: «ME. clubba, fr. ON. klubba, klumba»). معنی «انجمن» تحولی درون‌انگلیسی است: نخست از فعل to club «گرد هم آمدن همچون توده» (دههٔ ۱۶۲۰)، سپس اسمِ «انجمن مردمان» (دههٔ ۱۶۴۰) و «مجلسی که در میخانه گرد می‌آید» (۱۶۵۹–۱۶۶۰) — و همین معنا بود که به فرانسه و از آنجا به فارسی رفت. ادعای نورایی درست است.\",\n \"sources\": [E_CLUB, W_CLUB],\n \"ref_check\": [\n   {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None); the parent Germanic box cites AHD, which does list CLUB under gel-1.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. club, n.\", \"stance\": \"supports\", \"note\": \"'club, n. — ME. clubba, fr. ON. klubba, klumba, \\\"a thick stick, club\\\". See clump and cp. words there referred to.'\"},\n   {\"src\": \"WEB\", \"where\": \"etymonline.com/word/club (archived)\", \"stance\": \"supports\", \"note\": \"'c. 1200, \\\"thick stick ... used as a weapon\\\", from Old Norse klubba \\\"cudgel\\\" ... The sense \\\"company of persons organized to meet\\\" (1660s) apparently evolved from ... the verbal sense \\\"gather in a club-like mass\\\" (1620s).'\"},\n   {\"src\": \"POK\", \"where\": \"printed p. 360\", \"stance\": \"supports\", \"note\": \"'anord. klubba \\\"Keule\\\", woher engl. club'.\"}\n ]})\n\nnodes.append({\n \"id\": 15, \"lang\": \"Germanic\",\n \"words\": \"kling : to cling; klimban : to hold on, climb; klŭd : , a hill, rock, cloud; klamp, klump, klut : a wooden shoe, clumsy person; klaijo : sticky mud\",\n \"verdict\": \"plausible\",\n \"derivation\": \"All five are Germanic bases that Watkins does file under gel-1: *kling- (OE clingan 'to cling', II.6a); *klimban < *gle-m-bh- (OE climban, II.2); *klūd- (OE clūd 'hill, rock' > CLOUD, I.4a — Pokorny p.362: 'ags. clūd m. \\\"a mass of rock, hill\\\", engl. cloud \\\"Wolke\\\" (\\\"Wolkenballen\\\")'); *klamp- (MDu. klampe 'metal clasp' > CLAMP, II.4) together with *klump- (MLG klumpe, klompe, which Klein glosses 'clog, wooden shoe', properly 'shoe formed from a lump of wood' — the source of Nourai's otherwise puzzling gloss 'a wooden shoe') and *klūt- (OE clūt 'patch' > CLOUT, I.5); and *klajjō- (OE clǣg > CLAY, III.1a — Pokorny p.363). Two defects, both the book's own: (a) the printed page reads 'klŭd : , a hill, rock, cloud' with a stray comma before 'a hill', a misprint faithfully carried into the JSON; (b) the three forms 'klamp, klump, klut' share one gloss 'a wooden shoe, clumsy person' that fits only klump (and, at a stretch, clumsy), not klamp 'clasp' or klut 'patch'. Beyond that, Pokorny himself warns that much of this Germanic material 'macht keinen idg. Eindruck' (p.357) and may not be inherited at all — hence 'plausible' rather than 'confirmed'.\",\n \"derivation_fa\": \"هر پنج صورت، پایه‌های ژرمنی‌اند که واتکینز آن‌ها را ذیل gel- می‌آورد: *kling- (انگلیسی باستان clingan)، *klimban < *gle-m-bh- (climban)، *klūd- (clūd «تودهٔ سنگ، تپه» > cloud؛ پوکورنی ص ۳۶۲)، *klamp-/*klump- (هلندی میانه klampe «گیره»؛ آلمانی سفلای میانه klumpe/klompe که کلاین آن را «کفش چوبی، در اصل کفشی که از کندهٔ چوب تراشیده‌اند» معنی می‌کند — سرچشمهٔ همان گلاسهٔ عجیبِ «کفش چوبی» در کتاب) و *klūt- (clūt «وصله» > clout)، و *klajjō- (clǣg > clay؛ پوکورنی ص ۳۶۳). دو ایراد، هر دو از خودِ کتاب: نخست، در صفحهٔ چاپی «klŭd : , a hill, rock, cloud» با ویرگولِ زائد آمده که خطای چاپیِ کتاب است و استخراج وفادار بوده است؛ دوم، سه صورتِ klamp, klump, klut یک گلاسهٔ مشترک گرفته‌اند که تنها به klump می‌خورد نه به klamp «گیره» و klut «وصله». افزون بر این، خودِ پوکورنی (ص ۳۵۷) هشدار می‌دهد که بخش بزرگی از این مادهٔ ژرمنی «هیچ نمای هندواروپایی ندارد». پس با احتیاط پذیرفتنی است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985, gel-1: 'I.1 Germanic *klamp- in Middle Low German klumpe, compact group of trees: CLUMP'; 'I.4 Germanic *klūd- in: a. Old English clūd, hill, rock: CLOUD'; 'I.5 Germanic *klūt- in Old English clūt, patch: CLOUT'; 'II.2 Germanic *klimban (< *gle-m-bh-) ... CLIMB'; 'II.4 Germanic *klamp- in Middle Dutch klampe, metal clasp: CLAMP'; 'II.6a Germanic *kling- in Old English clingan, to cling: CLING'; 'III.1a Extended form *glei- in ... Germanic *klajjō-, clay, in Old English clǣg, clay: CLAY'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"printed pp. 357, 360, 362, 363\", \"stance\": \"partial\", \"note\": \"supports the individual forms ('ags. clingan', 'ahd. klimban, ags. climban', 'ags. clūd m. \\\"a mass of rock, hill\\\", engl. cloud', 'ags. clǣg (engl. clay)') but cautions at p.357 that the Germanic groups 'mit ihren expressiven Verschärfungen und Nasalierungen machen keinen idg. Eindruck'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.vv. clump, clumsy, cloud, climb\", \"stance\": \"supports\", \"note\": \"'clump, n., a heap, mass. — MLG. klumpe, klompe, \\\"clog, wooden shoe\\\", prop. \\\"shoe formed from a lump of wood\\\" ... and to ON. klumba, klubba, \\\"a thick stick, club\\\"' — this is where the chart's 'a wooden shoe' comes from; 'cloud ... fr. OE. clūd, \\\"mass of rock, rock\\\", which meant orig. \\\"mass\\\"'.\"}\n ]})\n\nnodes.append({\n \"id\": 16, \"lang\": \"English\", \"words\": \"cling, climb, cloud, clamp, clumsy, clown, clay\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Five of the seven are straightforward: cling < OE clingan; climb < OE climban; cloud < OE clūd 'mass of rock, hill' (the meteorological sense only from c.1300, ousting OE wolcen); clamp < MDu. klampe 'metal clasp'; clay < OE clǣg — all five are filed under gel-1 by Watkins and appear in Pokorny at pp.357-363. Two are weaker. clumsy does not continue *klump- at all: Klein derives it from ME clumsed, past participle of clumsen 'to be benumbed (with cold)', related to dial. Swed. klummsen and to OE beclemman 'to bind, fetter', i.e. to the *klam- 'press, benumb' branch — connected to the root only at one remove. clown is the weakest link: Klein and Etymonline call it of uncertain, probably Scandinavian, origin (cf. Icel. klunni, Swed. dial. kluns 'clumsy fellow' — Pokorny p.362 has 'isl. klunni \\\"klotzige Person\\\"' under g(e)l-eu-), with a Low German source also proposed; the attachment to this root is a guess, not an established derivation.\",\n \"derivation_fa\": \"پنج واژه از هفت واژه بی‌اشکال‌اند: cling از انگلیسی باستان clingan؛ climb از climban؛ cloud از clūd «تودهٔ سنگ، تپه» (معنی «ابر» تنها از حدود ۱۳۰۰ م. جای wolcen را گرفت)؛ clamp از هلندی میانه klampe؛ و clay از clǣg — هر پنج در پیوست واتکینز و در پوکورنی (ص ۳۵۷–۳۶۳) ذیل همین ریشه آمده‌اند. اما دو واژه سست‌ترند: clumsy اصلاً دنبالهٔ *klump- نیست؛ کلاین آن را از انگلیسی میانهٔ clumsed، اسم مفعولِ clumsen «کرخت شدن»، می‌گیرد که با سوئدیِ گویشی klummsen و انگلیسی باستان beclemman «بستن» پیوند دارد، یعنی از شاخهٔ *klam- «فشردن، کرخت کردن» و تنها با یک واسطه به این ریشه می‌رسد. سست‌ترین حلقه clown است که کلاین و اتیمانلاین آن را با تردید اسکاندیناویایی می‌دانند (قس. ایسلندی klunni و سوئدیِ گویشی kluns «آدم بی‌دست‌وپا»؛ پوکورنی ص ۳۶۲) و خاستگاه آلمانی سفلی نیز برای آن پیشنهاد شده است. پس برای بیشتر واژه‌ها ادعا درست است و برای clumsy و clown با احتیاط پذیرفتنی.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None); the parent Germanic box cites AHD, which lists CLING, CLIMB, CLOUD, CLAMP, CLUMP, CLOUT and CLAY under gel-1 but neither CLUMSY nor CLOWN.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"status\": None, \"where\": \"Watkins 1985 s.v. gel-1\", \"stance\": \"partial\", \"note\": \"CLING, CLIMB, CLOUD, CLAMP, CLAY (and CLUMP, CLOUT, CLOD, CLOT) are all listed; CLUMSY and CLOWN are not listed under this root anywhere in the entry.\"},\n   {\"src\": \"KLN\", \"where\": \"s.vv. clumsy (KLN_1971 line 49356ff.), cloud (49236), climb (48840), clay (48428)\", \"stance\": \"partial\", \"note\": \"'clumsy, adj. — ME. clumsed, pp. of clumsen, \\\"to benumb\\\", rel. to dial. Swed. klummsen, \\\"benumbed with cold\\\", OE. be-clemman, \\\"to bind, enclose, fetter\\\", and to E. clamp' — a different branch from klump; 'clay, n. — ME. clei, clai, fr. OE. clǣg'.\"},\n   {\"src\": \"POK\", \"where\": \"printed p. 362\", \"stance\": \"partial\", \"note\": \"'schwed. kluns m. \\\"Klumpen\\\", isl. klunni \\\"klotzige Person\\\"' under D. g(e)l-eu- — the nearest Pokorny comes to English clown, and he does not mention the English word.\"}\n ]})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Gel, Geli, Gelu, Glue, Geleb, Gelu\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *gel- 'to form into a ball; a rounded mass', with the extensions *gel-eb(h)-/*gleb(h)-, *g(e)l-eu- and *glei- (Pokorny I 357-364)\",\n \"note\": \"The root is real, the language label is right and the gloss is right — indeed the gloss is Watkins's own wording: AHD/Watkins 'gel-1. To form into a ball; conventional base of loosely connected derivatives referring to a compact mass or coagulated lump, and to the qualities of viscosity and adhesiveness. [Pok. 1. gel- 357]'; Pokorny I 357 'gel- \\\"ballen, sich ballen; Gerundetes, Kugeliges\\\" usw.'. The extra names in the header are Pokorny's own subsections: 'Geleb' = geleb(h)-/gleb(h)- 'zusammenballen' (p.359, whence globus, gleba, club), 'Gelu' = g(e)l-eu- (p.361, whence Skt. glāu-, NP gulūle, OE cliewen), 'Geli' = glei- 'kleben, schmieren' (pp.362-364, whence gluten, glue, clay). Two oddities of the header, both in the printed book and faithfully extracted: 'Gelu' is listed twice (matching the two 'Gelu -> see Gel' stubs at the foot of the page), and 'Glue' is not an IE root form at all — it is either Nourai's rendering of *gleu- or the English keyword slipped into the root list; there is no 'Glue -> see Gel' stub to go with it. The one substantive problem on the page is not in the root but in node #1 (Persian گوی), which Nourai's own reference assigns to a different root.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازینِ *gel- «گِرد کردن، به‌شکل گوی درآوردن؛ چیز گِرد و کروی» واقعی است و برچسب زبانی و معنای آن هر دو درست‌اند؛ معنایی که نورایی داده در واقع ترجمهٔ عین عبارت واتکینز است («gel-1. To form into a ball …») و پوکورنی (جلد ۱، ص ۳۵۷) می‌نویسد: «gel- ballen, sich ballen; Gerundetes, Kugeliges». نام‌های دیگرِ سرلوحه همان زیرشاخه‌های پوکورنی‌اند: Geleb = geleb(h)-/gleb(h)- «به‌هم فشردن» (ص ۳۵۹؛ خاستگاه globus و gleba و club)، Gelu = g(e)l-eu- (ص ۳۶۱؛ خاستگاه glāu- سنسکریت و «گلوله» فارسی) و Geli = glei- «چسبیدن، مالیدن» (ص ۳۶۲–۳۶۴؛ خاستگاه gluten و glue و clay). دو نکتهٔ عجیب در سرلوحه هست که هر دو در صفحهٔ چاپی نیز دیده می‌شوند و خطای خوانش اسکن نیستند: «Gelu» دو بار آمده (همسو با دو ارجاعِ «Gelu ← Gel» در پایین صفحه)، و «Glue» اصلاً صورت ریشه نیست بلکه یا نگارشِ نورایی برای *gleu- است یا واژهٔ انگلیسیِ glue که به فهرست ریشه‌ها راه یافته — و برخلاف نام‌های دیگر، ارجاعِ «Glue ← Gel» ندارد. تنها ایراد اساسیِ این صفحه در خودِ ریشه نیست، بلکه در گرهٔ شمارهٔ ۱ («گوی» فارسی) است که مأخذ خودِ نورایی آن را به ریشه‌ای دیگر می‌بندد.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:357-364\", \"status\": \"supports\", \"note\": \"POK_02.txt leaves 13-20 = printed pp. 357-364, the whole article '1. gel- \\\"ballen, sich ballen; Gerundetes, Kugeliges\\\" usw.', with sections A. Gutturalerweiterungen (gel-g-, glek-), B. Dentalerweiterungen (gel-t-), C. Labialerweiterungen (geleb(h), gleb(h)-, glem-), D. g(e)l-eu-, E. glei-. The page range Nourai gives is exactly the article.\"},\n   {\"ref\": \"SYN:908\", \"status\": \"supports\", \"note\": \"Buck 12.83 'Sphere', printed p.908: 'OE cliwen, ME clewe, OHG cliuwa, MHG kliuwe ... : Skt. glau- \\\"round lump\\\", NPers. gulūle \\\"ball\\\", fr. *gleu- (cf. *gleu-d- in Dan. klode, etc.). Walde-P. 1.617'; and p.907 'Lat. globus ... : gleba \\\"lump, clod\\\" ... beside *glem- ... : *gel- in words for \\\"press together, lump, ball\\\"'. So SYN:908 is a page number, and it does carry the material.\"},\n   {\"ref\": \"IEC:303\", \"status\": \"partial\", \"note\": \"Mann p.303 is cited for the root but is in fact the page of the separate lemma 'gūd- (2) \\\"lump, ball\\\". Per gūy'. Mann's gel-/gleu- material sits at p.279 ('gliu- (glou-) \\\"ball, clump\\\" ... Skt. glau \\\"lump, goitre\\\" ... OHG kliwa, kliuwa \\\"clew, ball of thread\\\"'). The citation is thus right for the Persian word gūy but wrong as a reference for the root gel-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, gel-1 (AHD_watkins1985.txt line 486)\", \"stance\": \"supports\", \"note\": \"'gel-1. To form into a ball; conventional base of loosely connected derivatives referring to a compact mass or coagulated lump, and to the qualities of viscosity and adhesiveness. ... [Pok. 1. gel- 357.]' — Nourai's gloss is a near-verbatim shortening of this.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I, art. '1. gel-' (WLD_Bd1 djvu line 58069)\", \"stance\": \"supports\", \"note\": \"'1. gel- \\\"ballen; gerundetes, kugeliges u. dgl.\\\" ... Belege dieser einfachsten Wzf. ziemlich spärlich und z. T. recht unsicher: Ai. gula-h gulī (Lex.), gulika \\\"Kugel, Spielball, Perle, Pille\\\"' — the predecessor of Pokorny's article, with the same headword and gloss.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann p.279 s.v. gliu- (glou-)\", \"stance\": \"partial\", \"note\": \"'gliu- (glou-) \\\"ball, clump\\\" ... Skt. glau \\\"lump, goitre\\\" ... MIr. glau, glo \\\"ball\\\"; OHG kliwa, kliuwa \\\"clew, ball of thread\\\"; OE cliewen; Du. kluwen ... WP I, 617' — Mann has the root family, but under a different page than the one cited.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. globus\", \"stance\": \"partial\", \"note\": \"'Cf. glēba et glomus. Aucun rapprochement sûr.' — the Latin etymologists are noticeably more reserved than Pokorny/Watkins about the reality of this root.\"}\n ],\n \"nodes\": nodes\n}\n\nout = {\n \"pdf_page\": 169,\n \"book_page\": 139,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [entry]\n}\n# strip accidental keys\nfor n in out[\"entries\"][0][\"nodes\"]:\n    for c in n.get(\"consulted\", []):\n        c.pop(\"status\", None)\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-169.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build169.py",
 "description": "Build page-169.json"
}
```


### [2026-09-05T20:57:21.542Z] TOOL RESULT

```
ok
```


## [2026-09-05T20:57:26.054Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-169.json > /dev/null && echo \"JSON OK\" && head -c 3 data/verification/page-169.json | xxd | head -1 && python3 tools/verify_check.py 169",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T20:57:27.868Z] TOOL RESULT

```
JSON OK
00000000: 7b0a 20                                  {. 
nodes verified: 16/16
node verdicts: {'disputed': 1, 'confirmed': 10, 'plausible': 5}
root verdicts: {'confirmed': 1}
ref checks: {'contradicts': 1, 'supports': 10, 'partial': 3, 'not_checked': 4}
books consulted: {'partial': 9, 'silent': 4, 'contradicts': 2, 'supports': 27} | by book: {'KLN': 11, 'POK': 7, 'MON': 5, 'ARY': 3, 'LAT': 3, 'WEB': 3, 'HRN': 2, 'SYN': 2, 'AHD': 2, 'PHD': 1, 'IEC': 1, 'WLD': 1, 'BQT': 1}
```


## [2026-09-05T20:57:48.413Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-169.json` written, valid JSON, `verify_check.py 169` reports **0 PROBLEM lines** (16/16 nodes).

**PDF page 169 (book p. 139) — root "Gel, Geli, Gelu, Glue, Geleb, Gelu"** (1 chart + 5 redirect stubs skipped)

- Root verdict: **confirmed** (POK I 357–364 `gel- "ballen, sich ballen"`; Nourai's gloss is verbatim Watkins's `gel-1 "To form into a ball"`).
- Node verdicts: **confirmed 10, plausible 5, disputed 1**.
- Ref checks: supports 10, partial 3, contradicts 1, not_checked 4 (nodes with `refs=None`).

Disputed / notable:
- **#1 Persian گوی gūy** — *disputed*. Nourai's own reference contradicts him: Mann IEC p.303 puts `Per gūy` under a separate lemma `gūd- (2) "lump, ball" (fr. *gūdio-)`, not under gel-; MP `<gwd>` gōy (MacKenzie CPD 37) supports a *-d- stem; Pokorny never cites gūy in the gel- article; Wiktionary groups it with Skt. gola-, Kurd. gule/gog, Zazaki gudi.
- **#3 گلوله/گولّه** — *plausible*: word and root right, arrow direction wrong. POK 361, Buck 908, Horn 929, Mo'in's BQT footnote and Aryanpur p.441 all make NP gulūle a **cognate** of Skt. glāu- under *gleu-, not a borrowing from Sanskrit.
- **#12 French club** — *plausible*: French borrowed it from **English** (1702, Wiktionnaire), not from Germanic directly; the chart skips the English stage.
- **#11 Germanic klub** — *plausible*: gloss "a lump or group" back-projects the English sense; the etymon is ON klubba "cudgel, lump of wood".
- **#15/#16 Germanic/English cluster** — *plausible*: cling/climb/cloud/clamp/clay confirmed, but **clumsy** comes from ME clumsen "be benumbed" (*klam- branch) and **clown** is only a guessed Scandinavian connection; neither is in Watkins under gel-1.

Citation problems in Nourai (not extraction errors):
- **BQT:1861** — the گلوله entry is at printed **p. 1832** in the Mo'in edition scan (Aryanpur cites the same page as برهان قاطع ۱۸۳۲); p. 1861 carries گومست/گونه. Content supports him; the page number is ~29 off.
- **IEC:303** is cited on the root box, but p.303 is the *gūd-* page; Mann's gel-/gleu- material is at p.279.
- MON page numbers (3015/3039/3363/3382) are internally consistent with his 6-vol. Amir Kabir printing; our scan is a 2-vol. reprint (entries found at 1375/1385/1833/1833 ff.).

**Extraction errors: none.** I checked the printed page image. Two oddities are the book's own, faithfully extracted: the stray comma in `klŭd : , a hill, rock, cloud`, and `Glue` in the root header, which is not an IE root form and has no matching "Glue → see Gel" stub (the stubs are Geleb, Geli, Gelu, Gelu).

New artefact saved for auditing: `data/verification/sources/refs/ocr/ARY/441.vision.txt` (Aryanpur's گلوله table, read from the page image because the OCR was unusable). Six web pages archived via `fetch_source.py`.
