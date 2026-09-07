# Verification process log — verify-page-386


## [2026-09-07T20:42:42.652Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 386 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-386.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-386.json. Write /home/sfmqrb/git/rishe/data/verification/page-386.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 386` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:42:44.780Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T20:42:45.614Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


## [2026-09-07T20:42:45.622Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-386.txt"
}
```


### [2026-09-07T20:42:45.640Z] TOOL RESULT

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
226	Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
227	file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
228	`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.
229	
230	```json
231	{
232	  "pdf_page": 126,
233	  "book_page": 96,
234	  "verified_by": "claude-opus-5",
235	  "verified_on": "2026-09-05",
236	  "entries": [
237	    {
238	      "entry": 0,
239	      "root": "Dheigh, Dhigha",
240	      "verdict": "confirmed",
241	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
242	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
243	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
244	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
245	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
246	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
247	      "nodes": [
248	        {
249	          "id": 6,
250	          "lang": "Avestan",
251	          "words": "pairi-daeza",
252	          "verdict": "confirmed",
253	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
254	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
255	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
256	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
257	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
258	        }
259	      ]
260	    }
261	  ]
262	}
263	```
264	
265	Rules:
266	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
267	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
268	- `words` = the transliterations of the node joined by "; " (copy from the chart).
269	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
270	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
271	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
272	- If a node lists several words, cover each word; if they differ in verdict, use the worst
273	  verdict for the node and explain per word in `derivation`.
274	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
275	  scholarship takes.
276	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
277	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
278	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
279	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


### [2026-09-07T20:42:45.643Z] TOOL RESULT

```
1	=== PDF page 386 (book page 356) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Peig : to mark  (refs POK:794)
4	#1 (parent #0) [Avestan] refs=POK:794; SYN:1284; SNS:143 | paes, paeš : to decorate, mark ; paěsah, pištra : decorated, skilled
5	  #2 (parent #1) [Persian] refs=BQT:440, 443; MON:904; HRN:80 | pîseh «پیسه» : black and white markings ; pîsî «پیسی» : a disease identified with markings on skin ; pîšeh «پیشه» : skill, job skill, job
6	  #3 (parent #1) [Avestan / Old Persian] refs=POK:794; SYN:1284 | ni-pais : mark down, write ☞Nî 1
7	    #4 (parent #3) [Pahlavi] refs=BQT:2201; UNV:54 | nipištan : to write ; nibištan : to write ; nipěk, niběg : book, written material
8	      #5 (parent #4) [Persian] refs=ZFS:37; MON:4669 | neveštan «نوشتن» : to write ; nobî «نُبی» : book, the holy Koran
9	#6 (parent #0) [Old Persian] refs=SNS:164; KNT:194 | paith : to mark, decorate ; ni-paith : mark down, write ☞Nî 1
10	#7 (parent #0) [Latin] refs=AHD | pingere : paint, picture, tattoo
11	  #8 (parent #7) [English] refs=None | paint, picture, pigment
12	#9 (parent #0) [Germanic] refs=AHD | fihla : cutting tool
13	  #10 (parent #9) [English] refs=None | file : grinding tool
14	
```


## [2026-09-07T20:42:49.339Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-386.json && ls tools/",
 "description": "Read source JSON and tools"
}
```


### [2026-09-07T20:42:49.382Z] TOOL RESULT

```
{
  "pdf_page": 386,
  "book_page": 356,
  "entries": [
    {
      "root": {
        "name": "Peig",
        "lang": "Indo-European",
        "refs": "POK:794",
        "gloss": "to mark"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:794; SYN:1284; SNS:143",
          "words": [
            {"translit": "paes, paeš", "gloss": "to decorate, mark", "script": null},
            {"translit": "paěsah, pištra", "gloss": "decorated, skilled", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:440, 443; MON:904; HRN:80",
          "words": [
            {"translit": "pîseh", "gloss": "black and white markings", "script": "پیسه"},
            {"translit": "pîsî", "gloss": "a disease identified with markings on skin", "script": "پیسی"},
            {"translit": "pîšeh", "gloss": "skill, job skill, job", "script": "پیشه"}
          ],
          "note": null,
          "quote": {
            "text": "هر پیسه گمان مبر که خالی است - باشد که پلنگ خفته باشد",
            "poet": "Sa`dî"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Avestan / Old Persian",
          "refs": "POK:794; SYN:1284",
          "words": [
            {"translit": "ni-pais", "gloss": "mark down, write", "script": null, "see": ["Nî 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Pahlavi",
          "refs": "BQT:2201; UNV:54",
          "words": [
            {"translit": "nipištan", "gloss": "to write", "script": null},
            {"translit": "nibištan", "gloss": "to write", "script": null},
            {"translit": "nipěk, niběg", "gloss": "book, written material", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "ZFS:37; MON:4669",
          "words": [
            {"translit": "neveštan", "gloss": "to write", "script": "نوشتن"},
            {"translit": "nobî", "gloss": "book, the holy Koran", "script": "نُبی"}
          ],
          "note": null,
          "quote": {
            "text": "موسیچه و قمری چو مقریانند - از سروبنان هریکی نبی خوان",
            "poet": "Khosrovânî"
          }
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "SNS:164; KNT:194",
          "words": [
            {"translit": "paith", "gloss": "to mark, decorate", "script": null},
            {"translit": "ni-paith", "gloss": "mark down, write", "script": null, "see": ["Nî 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "pingere", "gloss": "paint, picture, tattoo", "script": null}
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
            {"translit": "paint, picture, pigment", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "fihla", "gloss": "cutting tool", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "file", "gloss": "grinding tool", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
build_site.py
fetch_source.py
ganjoor.py
jscheck.js
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


## [2026-09-07T20:42:50.683Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','SNS','BQT','MON','HRN','UNV','ZFS','KNT','AHD','WLD','IEC','BRT','PHD','NYB','HUB','CHEUNG','ARY','KLN','SKT']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-07T20:42:51.995Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
UNV {"title": "J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Text Der König Husrav und sein Knabe', Heidelberg diss. 1917]", "edition_found": "1917 German dissertation edition (text + glossary); 1963 Paris ed. not found", "kind": "archive_djvu", "url": "https://archive.org/details/derpahlavitextde00unva", "identifier": "derpahlavitextde00un
ZFS {"title": "Mohsen Abolghasemi, Zaban-e Farsi va Sargozasht-e An, Hirmand 1375/1996", "kind": "catalog", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy se
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG null
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
```


## [2026-09-07T20:43:15.041Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80",
 "description": "List local reference files"
}
```


### [2026-09-07T20:43:15.080Z] TOOL RESULT

```
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


## [2026-09-07T20:43:15.093Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,200p' /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T20:43:15.136Z] TOOL RESULT

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


## [2026-09-07T20:43:20.527Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','SYN','KNT','BRT','HRN','UNV','SNS','BQT','MON','PHD','NYB','HUB','IEC','WLD']:\n    v=d[k]\n    print('==',k, v.get('local_file'), '| offset:', v.get('page_offset'), '| hint:', str(v.get('lookup_hint'))[:300])\n\"",
 "description": "Show page offsets and hints"
}
```


### [2026-09-07T20:43:21.999Z] TOOL RESULT

```
== POK /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== AHD /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== SYN /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== KNT /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt | offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
== BRT /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== HRN /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== UNV /home/sfmqrb/git/rishe/data/verification/sources/refs/UNV.txt | offset: leaf = printed + 2 (e.g. leaf 9 = p.7); only 48 leaves. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Pagination of the 1963 edition differs; use the glossary (Pahlavi words in transliteration) to verify substance.
== SNS ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt'] | offset: 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image | hint: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
== BQT ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== MON ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | offset: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== PHD /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== NYB /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== HUB /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== IEC /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== WLD ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
```


## [2026-09-07T20:43:25.765Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: peig\" POK_full.txt | head; echo ---; grep -n \"peig-\" POK_full.txt | head -30",
 "description": "Grep Pokorny for peig-"
}
```


### [2026-09-07T20:43:25.823Z] TOOL RESULT

```
65001:Root / lemma: peig-1 and peik- 
---
65001:Root / lemma: peig-1 and peik- 
65699:perhaps here peig-, polg-\n Slavic *p-blzo, *pelzti, russ. -Church Slavic plezetb "crawls'
```


## [2026-09-07T20:43:26.729Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^peig\\|^peiĝ\\|peig-\\b\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins AHD for peig"
}
```


### [2026-09-07T20:43:26.780Z] TOOL RESULT

```
248:peig-2. 3. Suffixed o-grade form *poik-yos in Germanic *faigjaz in Old English fege, fated to die: FEY.
815:peig-
824:peig-'. Also peik-. To cut, mark (by incision). 1. Alter- nate form *peik- in Germanic *fihala, cutting tool, in Old English fil, file: FILE. 2. Nasalized zero-grade form *pi-n-g- in Latin pingere, to embroider, tattoo, paint, picture: PAINT, PICTOR, PICTURE, PICTURESQUE, PIG- MENT, PIMENTO, PINTO; DEPICT, PICTOGRAPH. 3. Suffixed zero-grade form *pik-ro- in Greek pikros, sharp, bitter: PICRO-. 4. O-grade form *poik- in Greek poikilos, spotted, pied, various: POIKILOTHERM. [Pok. 1. peig- 794.]
825:peig-?. Also peik-. Evil-minded, hostile. 1. Suffixed zero-grade form *pig-olo- in Germanic *fikala- in Old
828:fixed o-grade form *pozk-itd in Germanic *faihithé in Old French faida, hostility, feud: FEUD!. [Pok. 2. peig-795.] peis-'. To crush. 1. Suffixed zero-grade form *pis-to- in Latin pistillum, pestle: PESTLE, PISTIL. 2. Nasalized zero-grade form *pi-n-s- in Latin pinsdre, to pound: PISTON. 3. Possibly suffixed form *pis-lo- in Latin pilum, javelin, pestle: PILE?. 4. Perhaps Greek ptissein (pt- for p-), to crush, peel: PTISAN, (TISANE). [Pok. 1. (peis-2), pis- 796. peis-2. To blow. Germanic “fis- in Old Norse fisa, to fart, akin to the Scandinavian source of Middle English fise, fart: F1zGIG. [Pok. 2. peis- 796.] peisk-. Fish. Zero-grade form *pisk-. 1. Suffixed Ger- manic form “fisk-a- in: a. Old English fisc, fish: FISH; b. Middle Dutch vische, vis, fish: WEAKFISH. 2. Suffixed form “pisk-i- in Latin piscis, fish: PISCARY, PISCATORIAL, PISCES, PISCI-, PISCINA, PISCINE; GRAMPUS, PORPOISE. [Pok. peisk- 796.] pek-'. To make pretty. 1. Possibly Germanic “fagra- in Old English feger, beautiful: FAIR}. 2. Possibly Germanic *fagin-, *fagan-, to enjoy, in Old English fegen, joyful, glad (> fagnian, to rejoice): FAIN, FAWN}. [Pok. 1. pek- 796.] pek-?. To pluck the hair, fleece, comb. 1. Extended form *pekt- in Germanic *fehtan, to fight, in Old English feohtan, to fight: FIGHT. 2. Suffixed extended form *pekt-en- in: a. Latin pecten, a comb: PECTEN; b. zero-grade. form *pkt-en- in Greek kteis (genitive ktenos < *pktenos), a comb: CTENIDIUM; CTENOID, CTENOPHORE. [Pok. 2. pek- 797.] peku-. Wealth, movable property. 1. Germanic *fehu- in: a. Old Norse fé, property, cattle: FELLOW; b. Old French fie, fief: FEE; c. Medieval Latin feudum, feudal estate: FEUD?; INFEUDATION. 2. Suffixed form “peku-n- in Latin peciinia, property, wealth: PECUNIARY; IMPECUNIOUS. 3. Suffixed form *peku-l- in Latin peciilium, riches in cattle, private property: PECULATE, PECULIAR. [In Pok. 2. pek- 797.] pekv-. To cook, ripen. 1. Assimilated form (in Italic and Celtic) *kvekw- in Latin coquere, to cook: COOK, CUISINE, (CULINARY), KILN, KITCHEN, QUITTOR; APRICOT, BISCUIT, CONCOCT, DECOCT, PRECOCIOUS, RICOTTA. 2. Greek pe- pon, ripe: PEPO. 3. Greek peptein, to cook, ripen, digest (> peptos, cooked): PEPTIC; DRUPE, EUPEPTIC, PEPSIN, PEPTONE, PUMPKIN. 4. Greek -pepsia, digestion: DYSPEP- sia. 5. Sanskrit pakva-, ripe: PUKKA. [Pok. peky- 798.] pel-1. Dust, flour. 1. Latin pollen, fine flour, dust: PoL- LEN. 2. Latin pulvis, dust: POWDER, PULVERIZE. 3. Latin palea, chaff: PAILLASSE, PALEA. 4. Greek palunein, to sprinkle flour: PALYNOLOGY. 5. Greek poltos, porridge (made from flour), probably borrowed via Etruscan into Latin as puls, pottage: POULTICE, PULSE?. [Pok. 2 b. pel- 802.] pel-2. Pale. 1. Suffixed variant form *pal-wo- in: a. Ger- manic *falwaz in Old English fealu, fealo, reddish yellow: FALLOW DEER; b. Latin pallére, to be pale: PALE, PAL- LID, PALLOR; APPALL; C. Latin palumbés (influenced in form by Latin columbus, dove), ringdove, “gray bird”: PALOMINO. 2. Suffixed form “pel-ko- probably in Ger- manic *falkén-, falcon (< “gray bird”), in: a. Old French girfaut, gyrfalcon: GYRFALCON; b. Late Latin falcé, falcon (but Germanic *falkén- is also possibly from the Late Latin): FALCON. 3. Suffixed extended form *peli- wo- in: a. Greek pelios, dark: PELOPS; b. o-grade form *poli-wo- in Greek polios, gray: POLIOMYELITIS. 4. Per- haps Greek pelargos (< *pelawo-argos), stork (< “black- white bird”; argos, white; see arg-); PELARGONIUM. [Pok. 6. pel- 804.] pel-3. To fold. 1. Extended o-grade form *polt- in Ger- manic *falthan, *faldan in: a. Old English fealdan, faldan, to fold: FoLD!; b. Old High German faldan, to fold: FALTBOAT; Cc. Germanic compound “*faldistélaz, “folding stool” (*stdlaz, stool; see sta-), in Medieval Latin compound faldistolium, folding chair: FALDSTOOL;
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
1507:FERIA dhés- FERMATA dher-2 FERMENT bhreu-? FERN per-2 FEROCIOUS ghwer- FERRET! bher-1 FERRET? bhel-3 FERRI- ferrum FERRO- ferrum FERROUS ferrum FERRUGINOUS ferrum FERRULE wei-1 FERRY per-2 FERTILE bher-1 FERVENT bhreu-2 FERVID bhreu-2 FERVOR bhreu-2 FEss bhasko- -FEsT dhés- FESTAL dhés- FESTINATE bhers- FESTIVAL dhés- FESTIVE dhés- FESTOON dhés- FETAL dhé(i)- FETCH! ped-1 FETE dhés- FETICIDE dhé(i)- FETISH dhé-1 FETLOCK ped-! FETTER ped-1 FETTLE ped-2 FETUS dh@(i)- FEUD! peig-2 FEUD? peku- FEUILLETON bhel-3 FEVERFEW bheug-! FEW pau-
1509:FicHu dhig¥- FICKLE pelg-2 FICTILE dheigh- FicTION dheigh- -FID_ bheid- FIDELITY bheidh- FIDUCIAL  bheidh- FIDUCIARY bheidh- FIELD pele-2 FIELDFARE wer-4 FIEND pé@(i)- FIERCE ghwer- Fiesta dhés- FIFE pipp- FIFTEEN penkWe FIFTH penkwe FIGHT pek-2 FIGMENT dheigh- FIGURE dheigh- FILAMENT gWhi- FILAR gWhi- FILARIA gWhi- FILE! gWhi- FILE? peig-1 FILES pu-2 FILIAL dh@(i)- FILIATE dhé(i)- FILIBUSTER pri- FILIFORM gWhi- FILIGREE gre-no-, g¥hi- FILL pele-1 FILLET gWhi- FILLY pau-
1523:FOAL pau- FOAM (s)poi-mo- FODDER pa- FOE peig-2
2087:PHYLACTERY phulax PHYLAXIS phulax PHYLE bheue- PHYLETIC bheue- -PHYLL bhel-3 PHYLLO- bhel-3 PHYLLOCLADE kel-1 -PHYLLOUS bhel-3 PHYLLOXERA ksero- PHYLOGENY bheua- PHYLUM bheue- PHYSIC bheue- PHYSIO- bheue- PHYSIOGNOMY gn6- PHYSIQUE bheue-_ PHYSOSTIGMINE pu-1 PHYSOSTOMOUS_ pu-! -PHYTE bheue- PHYTO- bheue- PHYTON bheue- PIACULAR pius PIANO? pele-2 PIANOFORTE bhergh-2 PIAZZA plat- PIBROCH pipp- PICA2 (s)peik- PICARO (s)peik- PICE ped-1 PICEOUS_ pik- PICKET (s)peik- PICOLINE pik- PICRO- peig-1 PICTOGRAPH peig-1 PICTOR peig-! PICTURE peig-1 PICTURESQUE peig-', (s)peik- PIE? (s)peik-
2090:PIEZO- sed-1 PIGEON pipp- PIGMENT peig-1 PIKE! (s)peik- PILAR pilo-
2093:PILUS _pilo- PIMENTO peig-1 PIMPERNEL pippali PINA peio- PINCE-NEZ nas- PINE! peie-
2094:PINE? kwei-1 PINEAL peie- PINFOLD bend- PINNA pet- PINNACE peie- PINNACLE pet- PINNATE pet- PINNULE pet- PINOCYTOSIS p6(i)- PINON peio- PINTLE bend- PINTO peig-1 PIOLET skep- PIONEER ped-1 PIOUS pius
2111:POETIC kWej-2 POGROM apo-, ghrem- -POIESIS kwej-2 -POIETIC kwej-2 POIGNANT peuk- POIKILOTHERM peig-1 POILU pilo-
```


## [2026-09-07T20:43:33.272Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '65001,65090p' POK_full.txt",
 "description": "Read Pokorny peig-1 entry"
}
```


### [2026-09-07T20:43:33.322Z] TOOL RESULT

```
Root / lemma: peig-1 and peik- 

Meaning: coloured, speckled 

Material: A. Old Indie pirjkte {uube\.) " painted ', pings-, p/'/jga/a-' reddish, brown', pinjara- 

"reddish, golden '; gr. niYYCiAo(; (Hes.) 'lizard', niyYCiv ' Kucken ' Hes.; Latin pingo, -ere, 

pinxT, pictum " paint; with the needle prick ', pictor^ painter '; Old Bulgarian pegi^ 

"varicolored'; Tocharian A pik-, pek- " write, paint ' {pekant- ' painter '), B pink-, pai(y)k- " 

write '. 

Maybe alb. pike^doi, stain'. 

B. Old Indie /0//77S5//"lashes out from (esp. flesh), cuts, cuts rightly, forms, decorates ', 
pesaii-u., pesa-m. "shape, form, paint, color', pesaia-^ decorates; mellifluous; skilful' 
(compare noiKiAo(;); pisarjga-^ reddish, reddish brown ', pisa-xr\. ' Dammhirsch ' etc.; 
perhaps 5///0a- "varicolored', whether from *yC>/s/5-(Tedesco, Lang. 23, 383 ff.); 

Maybe alb. p/is "dirty, stained', i piste ^ dirty ' = Lithuanian /7/esa"smut'. 

Avestan paes-^ make colorful, adorn, decorate ', paesa-m. paesati-u. "jewellery, 
decoration ', Old pers. /7^5^B" written down ', Avestan fra-pixsta-^ decorated '; 

gr. TTOiKiAo(; "varicolored'; TTiKp6(; "sharp (of arrow), bitter, shrilly, screaming, hostilely ' 
(formal = Old Bulgarian ptstrt "varicolored'); Latin pignus, -oris^ pledge ' (if " the pinned 

'?); 

Maybe alb. peng^ pledge ' a Latin loanword. 



Gothic filu-faitis^ sehr mannigfaltig ' (compare Old \r\d'\c puru-pesa-' mannigfaltig '), Old 
High German Old Saxon /e/7 "varicolored'. Old English fail, /^^"varicolored', whereof Old 
Icelandic fa{*failidn) " paint, adorn', fa runar^ scratch Runes ' (originally "red paint '), fainn 
" brightly speckled ', Old English fagian. Old High German feiien^ adorn'; 



Lithuanian piesti^ paint, write ', paTsas, piesas " RudflecK ', piesa "smut", paTsinas, 
puisinas, pulsus^ sooty, dirty, filthy', ispaisau^ adumbro '; Old Prussian peisai^ they write 
'; Old Church Slavic pisg ptsati 'write ', ptstrb (= niKp6(;) "varicolored', ptstrgg-b " trout ' 
(also pbsi} "dog' called from the color). 

References: WP. II 9 f., WH. II 301 f., 305 f., Trautmann 210 f. 
Page(s): 794-795 

Root / lemma: pe/g-1 and peiR- 

Meaning: hostile 

Note: (Baltic peik- probably with West Indo Germanic guttural) 

Material: A. Latin piget^ it irritates me, excites, causes aversion ', piger, -gra, -grum^ 

querulous, slow, decayed '; Old Icelandic feiknu. "ruin'. Old English facen. Old Saxon 

fecanu. " betrayal, malice, deceit' (Old English fgecne^ deceitful, mad, wicked, evil'). Old 

High German feihhanu. " guilefulness, deceit'. Old English ^e/^ic "deceit', ficor cunning, 

changeable '. 

B. Old \x\6\c pfsuna-^ bosgesinm, treacherous, venaumoenscn ', p/saca- "demon'; here 
the gall. (Venetic-lllyrian) VN Pictones, Pictavi{: Lithuanian piktas) " Poitou '; 

Note: 

The name P/cfonesM\/as given to lllyrians by centum speaking tribes. 

West Germanic *fa/h/Pd\n Old High German feh/da'\r\ate, fight'. Modern High German 
Fehde, Old English fgeht^(u) f. "enmity, feud '; Old High German fehan^ zelare ' and "hate', 
Old Saxon a-fehjan^ treat hostilely ', of Adj. Old High German gifeh^ hostile ', Old English 
fah, fag^ outlawed, ostracizes ' (engl. foe^ enemy '); in addition also Old High German 
feigi^ dem Tode verfallen ', Modern High German /fe/ige "timorous' (dial, also " dem Tode 
verfallen ', "fast mature, ripe, mellow, seasoned ', or " decayed '), Old Saxon /e^/ "of death'. 
Old English faege' is worried near the death ' (engl. fe)^. Old Icelandic feigr^ dem Tode 
verfallen ' {*poikJ6s, compare Lithuanian palkas "stupid'); 

Lithuanian pa/Tras "stupid', peikiu, pe/kt/" rebuke, reproach, vilify, scold'; p/ktas^mad, 
wicked, evil, angry, irate', pykstu, pyktrxa<^e against, be mad, wicked, evil '; Latvian 
peiksts^ changeable person'; Old Prussian paikemmai \ . PI. Konj., aupaickTf c\\ea\., 
deceive', pickuls^6ey\\\ Lithuanian pikulas^6ey\\\ Latvian -pikis, p/ku/s'devW. 

References: WP. II 10 f., WH. II 300 f., Trautmann 203 f.
```


## [2026-09-07T20:43:48.399Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK Feile/fihala ===\"; grep -n \"fihala\\|Feile\\|fila \" POK_full.txt | head -10; echo \"=== POK peik- lemma list ===\"; grep -n \"lemma: peik\\|lemma: (s)peik\" POK_full.txt | head",
 "description": "Grep Pokorny for Feile"
}
```


### [2026-09-07T20:43:48.481Z] TOOL RESULT

```
=== POK Feile/fihala ===
69969:'flax break, rupture'. Middle Low Qermaurepen, repeien6s.. Old High German rifiia, riffila 
84116:sverfasiem V. "feilen', svarfu. "Abfall beim Feilen', Old English sweorfan ds., afr. swerva' 
=== POK peik- lemma list ===
```


## [2026-09-07T20:43:49.106Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT paes ===\"; grep -n \"paēs\\|paesa\\|pae s\\|schmücken\" BRT.txt | head -30",
 "description": "Grep Bartholomae for paes"
}
```


### [2026-09-07T20:43:49.157Z] TOOL RESULT

```
=== BRT paes ===
4548:•  j.  ^aQku.p3S3mna ''  Adj.  'mit  Haken, Spangen  sich  schmückend':  aSsqm  van- tinhS  .  .  -na  Yt  J7.10.
14415:mit   paiti   'ziselirend    schmücken,    aus- 1  geschaffen  war"  Y.  /O,  8, legen     mit    — '     (Instr.):     snalna     aSsqni        KompK.   —    Zum  V.  %'.far>s-;   -at!-  au;  -/-i-,
14803:'zieren,  schmücken':  s.  ^'pfsamtia-'^''  (Sp. 130  «■}.
14808:•  j.  'paesa-  m.  'Schmuck,  Zierrat':  °sa F.  10.
14810:•  j.  'paesa-  i)  Adj.  'aussätzig':  ma  mg aiiayä  zao'hrays  /ranhar?ntu  *mä  *°sa'^ yS  vUiritsJanus". .  ein  Aussätziger,  dessen Person  isolirt  ist"  Yt.5.  92.  2)  ra. 'Aus- satz': ma  ähra  .  ,  'sS  yS  vJt3r7tS.tanu! mäZa.Bm  anyqm  daxstanqm  .  ,  aarahe mainySus  "nicht  .  .  AussaU,  womit  die Isolirung  der  (betroffenen)  Person  ver- bunden ist,  . ."  V,  2.  29.
14811:Vgl.  'paesa-,  womit  das  Wort  vll.  identisch ist.  —  mp.  (Pü.),  np.  /vi').  —  >)  Hds.  map'.
14813:•  j.  paesaDhanü-  f.  EN.  eines  gläubigen Mädchens:  kanyä  °nva  (statt GS.)  asaonyä Yt.y.141.
23300:Mit  Akk.  'sich  kleiden  in  — ,  anziehen, sich  umtun;  anhaben';  Akt.  und  Med.: uai  vaslrä  vanAalu  V,_y.  19'';  ^^<Kcri7««( vastra  va»Aaia  (^S.)  andvl  YL5. 129"; —  spafta  vasträ  zanhaiti  tpaita  (sd.)  Yt 10.  126";  —  yS  vanhaiti  .  .  al^Js/a \frazus5  sanhasSa  .  .  N.92'*;p5;  —  *yffi .vanhinti  hntts^a  paiti-varahasca  ü.gi; I  —  kamn>m  (sd.)  vaste  vanhafum  V.  4. 49; *Y.8^^;  —  anyqmla  sutsm  vatfhsnahe N.52(?);  —  vanhSnS  F.S;  —  asman?m .  ,  yint  maedä  vasle  vaahansm  stfhr- paesanhim  "den  Himmel . .,  den  M.  anhat als  sein  aternengeschmiicktes  Gewand"  Yt. 13.  Z\  —  mainyul  ipjnisis  y7  xraosdtstsng asstis  vaitf  "der  heiligste  Geist,  der  die festesten  Himmel  als  Gewand  trägt"  Y. 30.  5.  Wertlos:  vanhäna  x^aita  raoci :fanvaitT^ia  vsrtsU  Yt  j.  i.
24499:•  j.  vispö.paesa-  Adj.  'mit  allem  Schmuck, allerlei  Zieraf :  vä^?Tn  .  .  's^m  zaranalmm Yt.  10.  124.  [Y.  57.  20:  lies  'paislm; s.  -pis-.]
24501:•  j.  vispö.paesah-  Adj.  (auch  fem.)  1)  'mit allem  Schmuck ,  allerlei  Zierat' :  barat kantam  . .  'satthtm  '^t  14.2'};  —  garif ttpmänäi yaj . .'sff(ASa.)  Vyt^.  3)sva, 'allseitig":  mastrm  'saithm  Y.p.  17.
24509:ai.  viivapii'  Adj.  —  VgL  ^-hpö.paesah:  —  Pfl.! harvisp  fesTt.  —  0  So  K  5,  $  26S.  9.  NA. 'faisim  mit  allzu  dürftiger  Variantenangabe.
26752:•  j.  stahr-paesah-  Adj.  'mit  Sternen  ge- schmückt': asman>m  .  .  ytt/i  mazdit  vasle (Sp.i394u.)i'aw^a«?OT  'sa»h>m''>  mainyu.- tästim  Yty.3;  Vd.2o;  —  aiwyarfkaiam 'sankim'^''  mamyuMsttm  Y.p.  26;  Vd.  t8 {'sauAs);  —  väsfm  .  .  •savÄim  mainyu.- täst»n  Yt.  10. 143;  —  nm lrum..*°sanhm'^ '> niitara.nalmlt  Y.  57.  21;  —  haomq  .  . 'sanha  (APm.)  mainyu.täsia  Yt  10.  90.
27885:•r»m  Yt./5.  S7- •  j.  zaranyö.paesa-  Adj.  (fem.  vi-)  'gold-
```


## [2026-09-07T20:43:58.265Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14780,14830p' BRT.txt",
 "description": "Read Bartholomae context around paesa"
}
```


### [2026-09-07T20:43:58.355Z] TOOL RESULT

```
Pii.i  b  c  k;  vgl.  zu  baiidräjah:
•  j.  tbista-.  'Uisla-  Adj,  PPfP.:  s. Ibai^-.
KompE.  —  li.  dvif/ä-  Adj,
•  j.  (bisyant-,  g.  daibisyant-**  Adj.  'feind- lich, fcind,  inimtcus':  rapantl  .  .  at  .  . -yanti  zastäi/täi/ (sd.) . .  Y.34. 4;  —  aei'qm *°yafitqm ''>  . .  tbaesä  \t.jo.'j6;  —  aurva- 'äianqm  'yantqnt  Y.57.  a6,  Yt  J^.  31,  *Vyt. i^";  Yt  74.34,  ^■57-''f>\  —  aurvahafiiyS pars  'yanbys  Yt.  13.  69,  Y.  68.  13;  Yt.  10. 75,75.31;  — -  vlspim  aurvd^jm  °yanttm vXspfm  ay)m  °yant>m  A.  7,  10;  —  vanä{ vupe  'yantö  Yt  75.54; — pala  nS  'yantat pairi  SrB.5.
PPA.  lum  V.lban-,  —  Pü. :  imär.  —  ')  S  i6S. 56.  —  ')  NA.  'yatqm,  s.  Var.  —  3)  In  den Hds,  TCideibt.
•  j.  (biS'vant-,  g.  daibiä'vant- '>  Adj. 'feindselig,   feind';    tbü'vatqm   tba^ä  H.g.
8;  28;  —  daibirvatö  dt'aliS  Y.2S.6. Vi..:  bSiiiär.  -  i>  S  368.  56.
*  }■  P^°>  /"%  tii'^  KompA.:  sva.  apa. In  ptarmta    und  fiäyaozä   (beide    an   wenig Vertrauens  werten  Stellen). — pa',fä.'  können sich    zu    ai.  ap&   verhalten  wie  ai. />'  zu  äpi\ vgl.  ksl.  podati  'atn-liidyai'.
ob,Google
8i7
paenaena-
•  j.  paenaena-  Adj.  (fem.  'nl-)  'aus  Honig bestehend,  bereitet";  *'nyä^t  (ISt)'>  zao- %raya  N.57.
Ableit.  aus  *paena-  m.  'Honig'');  mp.  attgu- fin,  np.  angHÜn  'Bienenhonig'.  —  Ob  zu  lit. /Ami  'Milch'?  {s.  daiu  JSchmidt  Krit.  :<h)'). —  Pü.:  fehlt. —  ")  So  der  Ausgang  in  T.  — >)  Die  Bedeutung  'Milch'  ist  für  *ptüna-  nicht wahrscheinlich,  obwohl  sich  ja  np.  anpibln allenralls  als  'Bienen milch' fassen  Hesse;  vgl. Hb«.  PSL  19,  AGr.  /.  124.
•  j.  'pacman-  n.  'Muttermilch';  yU  (nätnl. aridvt)  vupanqm  hütriünqm  däitlm  ra- %wTtn  'ma  ava.daraiti  Y.Ö^.z;  Vyt  50; —  Aä  (näml.  andvt)  .  .  yaeiäa%äiti  .  . ar^qm  xhtdrä  hä  x^a%rinqm  garm>q  hä xia%rinqm  'ma  Y,  65. 5.
KocnpE.;  Ab!eit.  —  Zum  V.  pay-,  —  S.  'pac- man- and  auch  paenaena-.  —    mp.  (Pü.)  p/m :
5.  noch  JSchmidt  Krit  104.
•  j,  'paeman-  Adj.,  nur  fem.  'mat/iT- 'säugend',  von  der  HUndio;  gatwqm  , . pu^raca  (sd)  'mainiea  V./5.  49.
Zum  V.  pay-,  —  VgL  'pacman-.  —  Pü,:  pem i  ra/l.
•  j.  "paemanyo  vs  Vyt.  13.
Vgl.  V.  31.   7,  wo  paemavaili.
•  '].  paema'vant-  Adj.,  nur  fem.  'vaili- 'die  mit  Muttermilch  versehen  ist"h  °vaHi xsviptavaiH  (VSf.)  V.  21.  7.
Pü. :  pümSvand.  —  >)  Im  Gegens.  za  sivipla-
•  j.  paes-,  p.  pais-  V.  'farbig  macheu; zieren'.  Praes.  27(Pass.)^M)w-";  j-Aor.  i pif'K  —  PPfP.  'piita-,  •pixlia-i';  Inf. 'pHianaiy.
'zieren,  schmücken':  s.  ^'pfsamtia-'^''  (Sp. 130  «■}.
mit  fm  'verzieren':  barat  kanbm  .  . frapixlt>m  vltpu.paitarghm  Yt/4.37.
'mit  aiy  'nieder-,  aufschreiben':  Jipim . .  tyäm  adam  niyapHam  "*  Bh.  4\^',  —  o»** ahyäys  dipiyä  naiy  nipistam  avakya- rädiy  naiy  nipHtam  mntyJ^  .  .  ".  .  das ist  in  dieser  Inschrift  nicht  niederge- schrieben, deshalb  ist  es  nicht  nieder- geschrieben, damit.."  BL4.8;  —  stanam .  .  yanaiy  (sd.)  dipim  naiy  nipi^täm akunaus  X.  7. 3.
t\.  fimiiti  'er  schmückt', /i'.ry<iCf, /(//a^;  mp. fäsU  'geschniickt',  np.  nuvesad  'er  schreibt', WOM.  finstun  'schreiben'  (S  62.  1  No.).  — «)  Statt  pirya-,  %  268.  9 ;  s.  No.  4.  —  ')  Kann auch  pais-  gelesen  werden.  —  ti  %  86  «E.  — 4)  '  Tor  mit  für  1  und  dies  statt  j«;;  s.  hinäan-
"pairauaräta-x^t  8  >  8
•  j.  'paesa-  m.  'Schmuck,  Zierrat':  °sa F.  10.
KompE.  —  Zum  V,  paei.,  —  ai.  'pcia-  m. ; np.  vgl.  pesa  'Scheckkuh'.  —  Vgl.  fpalsa-.  — Pu. :  fhisn.
•  j.  'paesa-  i)  Adj.  'aussätzig':  ma  mg aiiayä  zao'hrays  /ranhar?ntu  *mä  *°sa'^ yS  vUiritsJanus". .  ein  Aussätziger,  dessen Person  isolirt  ist"  Yt.5.  92.  2)  ra. 'Aus- satz': ma  ähra  .  ,  'sS  yS  vJt3r7tS.tanu! mäZa.Bm  anyqm  daxstanqm  .  ,  aarahe mainySus  "nicht  .  .  AussaU,  womit  die Isolirung  der  (betroffenen)  Person  ver- bunden ist,  . ."  V,  2.  29.
Vgl.  'paesa-,  womit  das  Wort  vll.  identisch ist.  —  mp.  (Pü.),  np.  /vi').  —  >)  Hds.  map'.
—  ')  Vgl.  die  Erklärung  von  mp.  pesU SWienAW.  67.  841. 17:  marii  T  bäsad  ti  Aamä andim  safid  bäsad.
•  j.  paesaDhanü-  f.  EN.  eines  gläubigen Mädchens:  kanyä  °nva  (statt GS.)  asaonyä Yt.y.141.
EUg.  Bed.  ?  Ob  patsah-vanü.  'schmackliebend'?
•  j.  paitah-  n.  'Schmuck,  Zierral?.
KompA.(?),  E.  —  Zum  V.  pais..  —  »X.pUas-  n.
•  j.  paeSatah-  m.  EN.  eines  Gläubigen: nanarastöis  UatikS  alaonB  Yt  y.  1 1  j ;  — sratdätsil  °tat3hö  asaortS  Yt  jj.  115;  — usmänaraheca  'tatthü  '>  Yt  y.  i  a  o ; — usmä- narahe  °lahe  (GS.)"'  asaonif  Yt.  Jj.  97.
Eig.  Bed.?  —  'Vgl.uspaeJataA-.  —  ')  In  einigen geringwertigen  Hds.  ist  pai/ijrä-aie  zugefügt.
—  I)  Nach  der  a-Dekl. p.  paisiy'i  lies  ^liy'.
j.  pa(>i%ya  N.  ig:  lies  paairya  (LSf).
•  j.  "paoS  F.  jo,  angebl.  'fauüg,  stinkend'". Pü. :  fütak.  —  ')  Der  Verfertigcr  des  F.  ist dazu  gekommen,  indem  er  das  mit  pülaktum übersetzte  pasHsla-  (sd.)  in  paas  =  pÜtai  und jÄ"  ^  tum  zerlegte!
•  j.  paoiiäta-  Adj.,  'der  fauligste,  stin- kendste': daeväis  .  .  Af!tqm  '/Jis'  Y.12.4; —  vtspanqm  *aasUm  *'hmca ''  yai  >rrfat daoiatahum  F.  40.
Supcrl.  aus  einer  Basis  ar.  *paas-,  zum  V. pav:  —  Vg\.  "paus.  —  Vä.:  pülaitum.  — ')  Hds.  paeis>sl°\
•  j.  "Atuaoiyu  (sd)  paloha"  N. /.
j,  paitiul  N.  66:  lies  pUiai. y  paUihnUm    N.  /j:    MtS  paitis' ;    s.  'a«-, Sp.  30  m.
•  j.  *'pairauarätä.x«t  ^.44- Pü.:  fehlt.
j.  pais5.tami!  N.  44:  liet  f^lSj:
dby  Google
8i9
pak'
```


## [2026-09-07T20:44:00.227Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nipista\\|ni-pis\\|nipais\\|nipaiθ\\|pixsta\\|frapixsta\" BRT.txt KNT.txt | head -20; echo \"=== KNT nipis ===\"; grep -n -i \"nipis\\|pai(n)\\|pi§\\|pis-\" KNT.txt | head -40",
 "description": "Grep for nipišta in BRT and KNT"
}
```


### [2026-09-07T20:44:00.303Z] TOOL RESULT

```
KNT.txt:1204:593. PIE $t (from Ё or ў + f) became pAr. &, and then plran. š, OP and Av. š, and Skt. st; these clusters are seen in derivatives with a t-sufhx: pIE *pik-to-, OP ni-pista- ‘engraved’; *peik-t- in
KNT.txt:2967:$290. COORDINATION AND SUBORDINATION. Not infrequently the OP texts express by coordinate clauses ideas which are logically subordinate; the result is a series of short sentences, syntactically simple, independent of each other grammatically, but logically and semantically connected. Thus, for example, DB 446-8 vafnà Auramazdaha api- mary aniyascry vasiy astiy kartam ava ahydya diptya пазу nipistam avahyarddiy naty nipistam таша ... ‘by the favor of Ahuramazda indeed, much other (work) was done by me; that (work) is not inscribed in this inscription; for the following reason it is not inscribed, lest . . .’; this could have been expressed in one complex sentence somewhat as follows: ‘much other work was done by me, which has not been inscribed in this inscription for the following reason, lest ...’. Another excellent example is found in XPf 20-25 шій Vistáspa иа Arfüma ubā ajivatam асту Auramazdim арабӣ Ката aha Dérayavaum hya manā рий avam asdyabiyam akunaus ahydyd бата 'Hystaspes and Arsames both were living, then—unto Ahu- ramazda thus was the desire—Darius who (was) my father, him he made king in this land’; in the parallel passage DSf 13-5, yadzy ‘when’ is used . instead of асїу ‘then’, and instead of Auramazdém avatà Ката aha (found also XPf 29f, DSf 15f), we find in DNa 37f (and elsewhere) yada mim ата Gha ‘as unto me was the desire’. In dating sen- tences we regularly have expressions of the type seen in DB 1.42 Garmapadahya máhyà I X rauca- bi$ fakaia aha агава zšaçam agarbdyatd ‘of the month Garmapada, 9 days had passed—then he seized the kingship’; only in DB 1.38 the date is followed by a subordinated clause, yadiy udapa- tala ‘when he rose up in rebellion’. The same phenomenon is probably present where conjunc- tions are omitted as introductory to subordinate clauses, such as the absence of tya in РМ 20 and 50 (cf. DNa 39).
KNT.txt:3841:47 m [ауа : ahy&y& : dipiyàf: палу : nipistam.: avahyarádiy : naiy : n
KNT.txt:4153:57 : avasely : didiy : yaciy : nipistam : mà :
KNT.txt:5619:nipistü npf. XPh 31. nipistam nsn. ($122) DB 441, 47f; DNb 57°; DSe 52.
BRT.txt:14805:'mit  aiy  'nieder-,  aufschreiben':  Jipim . .  tyäm  adam  niyapHam  "*  Bh.  4\^',  —  o»** ahyäys  dipiyä  naiy  nipistam  avakya- rädiy  naiy  nipHtam  mntyJ^  .  .  ".  .  das ist  in  dieser  Inschrift  nicht  niederge- schrieben, deshalb  ist  es  nicht  nieder- geschrieben, damit.."  BL4.8;  —  stanam .  .  yanaiy  (sd.)  dipim  naiy  nipi^täm akunaus  X.  7. 3.
BRT.txt:20295:•  p.  mä-tya'*  neg.  Konjn.  mit  Konjv.; 1)  hinter  einem  regierenden  Satz  mit  ava- hyarädiy  'dass  nicht,  damit  nicht':  ava- hyarädiy  naiy  nipistam  tn'  hyi^  . .  avahyH paruv  *%aday^  (sd.)  Bh,  4-8;  —  ava- hyarädty{sA.)  käram  aväjamyä''  "tya^mam xsnäsätiy  (sd.)  tyt^ . .  Bh.  i,  13,  2)  ohne regierenden  Satz,  sva,  V/Ä:  /j-a*  manä kartam  varnavatäm  ^uväm  m°  *draujT- yshy  {s^)  Bh.  ^.  6;  —  tuvam  kä  hya* aparam  itnäm  diptm  vainähy  . .  m'  vika- nähy  "du,  wer  es  auch  sei,  der  du  später diese  Inschrift  sehen  wirst  . .,  zerstöre  sie nicht"  Bh.4. 15.
BRT.txt:26702:mit  nT  'instituere,  anordnen,  befehlen', mit  Akk.  und  Inf:  D  adam  niyastayam imäm  yuviyäm  (sd.)  k^tanaiy  D.  17.  3;  3; —  ima'  stanam  (sd.)  Aauv  niyastayir  k^ta- naiyX.y.^; — pasava*  adam  niyaslJyam imäm  dipim  (sd.)  nipistanaiy  X.7.  3;!  — sä%rasal . .  yB  nistayeiti  k>r3tSe  sraosyqm (sd.)  ilart  (sd.)  ha  nÜtäta  (LS.)  iiryeiti yai  granto  nistayeiti  (Konj.)  ". ,  sofort  . . wird  sie  vollstreckt,  sobaJd  er  ergrimmt (sie  zu  vollstrecken)  befiehlt  (jusserit)"  Yt W.  109.  Undeutlich  ;*_)■«/ /iVVj  *d>nane ha%räHs  ^nis'MItanti'^''  N.  100.
=== KNT nipis ===
1609:The shortening of the sandhi combination -d c- to -c- in acty yacty ($105) is probably by way of assimilation of the weak -d (§84) to the follow- ing с-, whereupon the long consonant was short- ened; but the shortening of sandhi combinations may be merely graphic when, freeyenclitics were attached in OP, as in dpisim =-apis-Sm, tau-
2967:$290. COORDINATION AND SUBORDINATION. Not infrequently the OP texts express by coordinate clauses ideas which are logically subordinate; the result is a series of short sentences, syntactically simple, independent of each other grammatically, but logically and semantically connected. Thus, for example, DB 446-8 vafnà Auramazdaha api- mary aniyascry vasiy astiy kartam ava ahydya diptya пазу nipistam avahyarddiy naty nipistam таша ... ‘by the favor of Ahuramazda indeed, much other (work) was done by me; that (work) is not inscribed in this inscription; for the following reason it is not inscribed, lest . . .’; this could have been expressed in one complex sentence somewhat as follows: ‘much other work was done by me, which has not been inscribed in this inscription for the following reason, lest ...’. Another excellent example is found in XPf 20-25 шій Vistáspa иа Arfüma ubā ajivatam асту Auramazdim арабӣ Ката aha Dérayavaum hya manā рий avam asdyabiyam akunaus ahydyd бата 'Hystaspes and Arsames both were living, then—unto Ahu- ramazda thus was the desire—Darius who (was) my father, him he made king in this land’; in the parallel passage DSf 13-5, yadzy ‘when’ is used . instead of асїу ‘then’, and instead of Auramazdém avatà Ката aha (found also XPf 29f, DSf 15f), we find in DNa 37f (and elsewhere) yada mim ата Gha ‘as unto me was the desire’. In dating sen- tences we regularly have expressions of the type seen in DB 1.42 Garmapadahya máhyà I X rauca- bi$ fakaia aha агава zšaçam agarbdyatd ‘of the month Garmapada, 9 days had passed—then he seized the kingship’; only in DB 1.38 the date is followed by a subordinated clause, yadiy udapa- tala ‘when he rose up in rebellion’. The same phenomenon is probably present where conjunc- tions are omitted as introductory to subordinate clauses, such as the absence of tya in РМ 20 and 50 (cf. DNa 39).
3144:(c) A relative and its antecedent are both omitted in XPh 30-2 astiy айат atā dahydva уату upariy nipistà ayauda ‘there is (= ‘was’, $285) among these provinces which (are) inscribed above (one which) was in turmoil’.
3841:47 m [ауа : ahy&y& : dipiyàf: палу : nipistam.: avahyarádiy : naiy : n
4153:57 : avasely : didiy : yaciy : nipistam : mà :
4295:Sh. 35-40. The gold was brought from Sardis and from Bactria, "which here was wrought. The precious stone lapis-lazuli and carnelian which was wrought here, this was brought from Sogdiana. The precious stone turquois, this was brought from Chorasmia, which was wrought here.
4586:31 :dahyáva : tyaly : upariy : nipistà : a
4656:9 framàátàram : adam : Xšayāršā : 10 x&àyafiya : vazraka : хёдуабуа : 11 xšāyaðiyānām : xšāyaðiya : da 12 hyünàm : paruv : zanànàm : x$ 13 àya8iya : ahy&yà : bümiyà : va 14 zrakày& : düraiy : apiy : Daraya 15 vahaus : xšāyaðiyahyā : риса : Ha 16 x&manisiya :0ütiy : XSayársá 17 : xSayabiya : Dārayavauš : xSiya 18 буа : һуа : manā : pitä : hauv : va 19 502 : Auramazdaha : vasiy : tya : 20 naibam : akunauég : uta : ima : st 21 änam : hauv : niyastdya : katanaiy 22 : yaniy : dipim : naiy : nipist 23 ām : akunaus : pasáva : adam : ni 24 yastéyam : та : dipim : піра 25 iStanaiy : màm : Auramazda : pa 26 tuv : hada : бадафт : utämai 27 y : zSaqam : Ша : атану : kartam
5005:pi- sb. ‘water’: Av. áp-, NPers. db, Skt. pl. nom. dpas, acc. apás, pIE *йр-, with or without i-extension, which seems to have become 5 in OP ($422). āpišim (= apis-Sim; $41, $130) nsf. DB 1.95f. apiyálsf. DB 1.95. abis (Skt. adbhts, and dat.-abl. Skt. adbhyds, Av. aiwyó, both from *ap- bh-; §75.1V, $130, §188.V, JAOS 62.269-70; see also s.v. abi) ipf. DB 1.86.
5609:nipisti- sb. ‘impression’: deriv. of ni- + paid- ($152.11).  [niplisftiya] Isf DB. 4.90 (conj. of Kent, JAOS 62.268).
5618:mi- + pub- ‘engrave, inscribe, write’: niyapat- Sam Ist sg. aor. ($02, $102, $130, $218.T, $226.IT) DB 4.71. mipaislanaty inf. ($03, $122, $288) XV 24f. nipislam asf. past ptc. pass. (803) XV 22f.
5619:nipistü npf. XPh 31. nipistam nsn. ($122) DB 441, 47f; DNb 57°; DSe 52.
```


## [2026-09-07T20:44:11.746Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nimport re\n# find offsets of target lines\nlines=t.split('\\n')\nfor target in [5609,5618,5619,1204]:\n    pos=sum(len(l)+1 for l in lines[:target-1])\n    leaf=t.count('\\f',0,pos)\n    print(target,'leaf',leaf)\nEOF",
 "description": "Locate KNT leaves"
}
```


## [2026-09-07T20:44:13.530Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"SNS\\b\" ../refs_online.json | head -2; echo ===; grep -rn \"SNS\" /home/sfmqrb/git/rishe/data/verification/agent/ 2>/dev/null | head -5; echo \"=== abbrev list ===\"; ls /home/sfmqrb/git/rishe/data/ ; ls /home/sfmqrb/git/rishe/data/verification | head -40",
 "description": "Look for abbreviation list"
}
```


### [2026-09-07T20:44:14.277Z] TOOL RESULT

```
5609 leaf 217
5618 leaf 217
5619 leaf 217
1204 leaf 48
```


### [2026-09-07T20:44:15.485Z] TOOL RESULT

```
Exit code 1
93: "SNS": {
97:  "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.",
(eval):1: == not found
```


## [2026-09-07T20:44:22.610Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 209 217; do echo \"##### leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1{print substr($0,1,1200)}' KNT.txt; done",
 "description": "Print KNT leaves 209 and 217"
}
```


### [2026-09-07T20:44:23.828Z] TOOL RESULT

```
##### leaf 209
it (§76.V, 5148.1). Cf. Gray, AJP 58.67; Hz. Klio 8.51, AMI 2.77; Hinz, ZDMG 95.227. lacaram asm. DPa 6; АР]. dacaram ($494) рва 3.
tanii- sb. ‘body, self’ (8$153.IT) Ау. tand-, Skt. tani-; cf. Debrunner, IF 52.136. Decl., 51831. lanüs nsf. DNb 33. lanüm asf. XPf 31.
| tar- vb. ‘cross over’: Av. tar-, Skt. tdratz, caus. türáyalt, Lt. trans pte. as prep. ‘across’, cf. NEng. through. See also fara. vi- + tar- ‘go across’, caus. ‘put across’: viya- larayam Ist sg. imf. (§215) DB 5.24f. viyatarayd- mā lst pl. imf. (5230.1) DB 1.88.
fara prep. with aec. ‘through’: Av. tarō, NPers. tär, Skt. ards; formed on root tar- (q.v.) similarly to para (q.v.). іста] DZe 12.
Táravà- sb. ‘Tarava’, a town in Persia; Elam. -F-ra-ü-ma, АКК. ta-ar-ma-. Тато nsf. DB 3.22.
larsa- pres. stem. of vb. ‘fear’, with Ласа + abl.: Av. tarasaiti, NPers. térsé5, pIE "is-ske-ti (831, $97, $212), ef. pIE *tres- in Skt. trdsati, Gk. тре, also *trem- *trep- in Lt. tremit ‘trembles (with fear)’, trepidus ‘agitated (with fear). Jarsatiy ($228.1) DPd 11f. iarsa"tiy 3d pl. (§232.1) DSe 38f. alarsa imf. DB 1.50f. atarsa” 3d pl. imf. (5232.0) DB 
##### leaf 217
n üv-nara- (§142).
nàv- sb. ‘ship’: Skt. ndus, Gk. vais, Lt. nav-is, pIE *ndv- ($142). See also ndviyd-. [naval прі. (8183.1V) DZe 11 (supplied by Tm. Lex. 52).
navama- adj. ‘ninth’: Ау. паота-, Skt. navamá-, pAr. navama- remade from pIE neyeno- after pAr. dasama- ‘tenth’ ($14911, $204IV), ef. Lt. nénus.  navama пзш. DB 1.10; DBa 10f.
naviyd- fem. adj. as sb., ‘navigability’, i.e. ‘impossibility of fording the river on foot’: Av. nàvaya- ‘navigable’, Skt. navyd-, adj. to nàv- ‘ship’ (§144.V). Hardly collective, ‘collection of ships, flotilla’, and certainly not lsf. to nav-, ‘on ship- board’; ef. König, RulD 70-1, and esp. Kent, JAOS 62.269-71 (with lit.), 63.67. ^ nàviyà nsf. DB 1.86.
nàh- sb. ‘nose’: Av. nàh-, Skt. nds-, Lt. narés, NEng. nose, pIE *nds- (5110, $142).  náham asm. (81181, §185.1V) DB 2.74, 88f.
ni- prep. and verbal prefix ‘down’: Ау. ni, Skt. ni-, pIE *ni; in adv. nipadiy, and with verbs ar-, kan-, cay-, pa10-, yam-, std-, had-.
nij- verbal prefix ‘away’: sandhi form of pIE *nis- before voiced stops, generalized, cf. Av. niš-, Skt. niş- ($120); with verb ay- ‘go’.
nipadiy phrasal a
```


## [2026-09-07T20:44:40.923Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if i<170: continue\n    if i>230: break\n    # first 60 chars\n    head=p.strip()[:60].replace('\\n',' | ')\n    # look for isolated numbers\n    nums=re.findall(r'(?m)^\\s*(\\d{2,3})\\s*$',p)\n    print(i, nums[:4], head[:70])\nEOF",
 "description": "Find page numbers in KNT leaves"
}
```


### [2026-09-07T20:44:42.243Z] TOOL RESULT

```
170 [] : tya : adam : akunavam : 15 utamaiy : tya : рія : akunaus :
171 ['150'] rway has а distinct divider at the end, after Багат, db on t
172 [] th Xerxes the King: My father was Darius; Darius’s father wa
173 [] aka : xSiya | 8 biya : xSayafiyanàm :xšāyaðiya : dahy | 9 ünüm :
174 ['151', '132'] m : | 17 patiyaxsayaly : manā : bajim : abaraha : t | 18 yašām :
175 [] id, until I completed the work. | &4d. 46-56. Thou who (shalt 
176 ['153'] zSaqam : Ша : атану : kartam | Хоть то XV: The entire line 25 
177 [] this palace, by the favor of Ahuramazda, I after- wards buil
178 ['155', '156'] : hya : Dārayavauš : XS : руё : Haxdmanigiya : Mitra : mam :
179 [] 8. This is the Arab. 19. This is the Egyptian. 20. This is t
180 ['157', '158', '159'] d: LX (units) in weight. | ‚.. (= Wb ЕЎ).- | 157 | INSCRIPTIONS ON
181 ['160'] sed him, him- self becoming now king in Parsua, later called
182 ['161'] he field of historical romance. See also PW 3A.710-2, s.v. S
183 ['162'] rnment in Media and Persia, gathered an army of Medes and Pe
184 ['163'] I re- ject this interpretation of the series of sculptures, 
185 ['164'] ugh not mentioned in the Behistan inscription, must have fol
186 ['165'] � asn. DPd 20; DNa 53; XPh 43, 59; XSc 4°. ata- таш DPd 22; 
187 ['166'] t built, unrepaired’; neg. a- + pte. of kar- ‘make’. {akarta
188 [] ’, as taken by ТИМ. Aiw 322-3; otherwise Hz. Ap! 191-2: hadt
189 ['167', '168'] n., asn.); AÁuramazdü, АМ; ava (nsn.); avdkaram, avükaramca-
190 [] . Skt. apa, Gk. | and, Lt. ab, Gt. af, Gm. ab, NEng. оў, off, 
191 ['169', '170'] formed like Gk. &exero to root *segh-, ёттєтө to root *pet- 
192 [] -, GAv. angra-, LAv. apra- ‘hostile, enemy’, to рАт. root *a
193 ['171'] t’). | - | LEXICON | ч. | Атах$аса- sb. ‘Artaxerxes’ (Т, son of Xerx
194 ['172'] пат. AsH 1, 5; DB 1.4f; DBa 6; DSf 13; XPf 19, 20; A’Pa 20 (
195 ['173'] 's avabäštā adj. apm. 'thus standing". | avadà (ie. avadá) adv
196 ['174'] 3. asmanam (853) A?Pa 3. | ašnaiy adv. ‘near’, lsn. of ašna- ‘
197 ['175'] �; 4.33; DPe 7; DNa 16; DSe 15; DSm 5°; XPh 14. ima apf. DB 
198 ['176'] DB 1.34f, 41, 461; 2.74, 88f; 5.19f, 35; DNb 30, 37, 40f, 43
199 ['177'] by Hz, ApI 71-2). | ufraSa- ufrasta- adj. ‘well punished": u- 
200 ['178'] B Gr. $144, §286, $298 (Bv. takes uvd- as instr. and not vri
201 ['179'] to the wall alongside it (König, - Burgbau 32n; Hz. AMI 3.54
202 ['180'] om ã + kart- ‘cut’; but see Kent, Lg. 18.81-2). | акша aor. mi
203 [] ted by the OP writing. регу. of Iran. root *kas- (89.V, §87,
204 ['181', '182'] , 66, 70f, 78f, 80, 91, 92; 3.1, 9, 11, 20, 21, | 181 | 28, 29, 
205 [] sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 
206 ['183'] n, fall down’: [avagmat]a nsf. past pte. ($244) DSe 46f (con
207 [] 3f, 57; XPa 20; XPc 14; XPf 48, alva}m-c* ($521) DB 5.9. Ка&
208 ['185', '186'] Skt. jū- ‘press for- ward, impel quickly, excite, promote’, 
209 [] it (§76.V, 5148.1). Cf. Gray, AJP 58.67; Hz. Klio 8.51, AMI 
210 ['187'] 1) XPh 23. | tyam asi. DB 4.70f; DPd 7. tya as asf. (856.V) Am
211 ['188'] word of uncertain meaning, Sb 3. | Sanuvaniya- sb. ‘bowman’: d
212 ['189'] fnu, Lt. јеси ‘made’, NEng. do, deed, pIE *dhe-. See also wa
213 [] 5-6). | Dérayava'u- sb. ‘Darius’ (I, son of Hystaspes, king 52
214 ['191'] Hz. Ap! 136-8) nsn. as sb. ‘handiwork’, DSe 42. | Daha- adj. ‘
215 [] rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far a
216 ['193'] e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as g
217 [] n üv-nara- (§142). | nàv- sb. ‘ship’: Skt. ndus, Gk. vais, Lt.
218 [] with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing
219 [] ‘I pierce (as with a spit)’, Gt. faran ‘to travel’. рамо[т- 
220 [] tem (530, $148.I, 6154.1), ef. Av. posana- ‘battle’, Skt. pf
221 ['197', '198'] r-, Gk. rarnp, Lt. pater, Gt. fadar, pIE *poler- (863.11, 87
222 [] -. — fra&aram asn. XPf 26f, 37. | Fraéda- sb. ‘Frada’, a Margi
223 [] 1; DSe 1°; DSE 1°; D8s 1^; DSt 1; рле 1°; DE 1; XPa 1; XPb 1
224 [] 2; 4.66. abara imf. ($40, $84, 5228.) DB 1.25, 55, 88, 94; 2
225 ['201'] BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; D
226 [] 24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе
227 [] ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80
228 ['204'] so a province of the Persian Empire, ‘Egypt’; тазе. sg. as s
229 [] d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220,
230 ['206'] am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Tehera
```


## [2026-09-07T20:44:49.922Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==218{print}' KNT.txt | head -40; echo \"======= 219\"; awk 'BEGIN{RS=\"\\f\"} NR==219{print substr($0,1,1500)}' KNT.txt",
 "description": "Print KNT leaf 217-218"
}
```


### [2026-09-07T20:44:51.195Z] TOOL RESULT

```
n üv-nara- (§142).
nàv- sb. ‘ship’: Skt. ndus, Gk. vais, Lt. nav-is, pIE *ndv- ($142). See also ndviyd-. [naval прі. (8183.1V) DZe 11 (supplied by Tm. Lex. 52).
navama- adj. ‘ninth’: Ау. паота-, Skt. navamá-, pAr. navama- remade from pIE neyeno- after pAr. dasama- ‘tenth’ ($14911, $204IV), ef. Lt. nénus.  navama пзш. DB 1.10; DBa 10f.
naviyd- fem. adj. as sb., ‘navigability’, i.e. ‘impossibility of fording the river on foot’: Av. nàvaya- ‘navigable’, Skt. navyd-, adj. to nàv- ‘ship’ (§144.V). Hardly collective, ‘collection of ships, flotilla’, and certainly not lsf. to nav-, ‘on ship- board’; ef. König, RulD 70-1, and esp. Kent, JAOS 62.269-71 (with lit.), 63.67. ^ nàviyà nsf. DB 1.86.
nàh- sb. ‘nose’: Av. nàh-, Skt. nds-, Lt. narés, NEng. nose, pIE *nds- (5110, $142).  náham asm. (81181, §185.1V) DB 2.74, 88f.
ni- prep. and verbal prefix ‘down’: Ау. ni, Skt. ni-, pIE *ni; in adv. nipadiy, and with verbs ar-, kan-, cay-, pa10-, yam-, std-, had-.
nij- verbal prefix ‘away’: sandhi form of pIE *nis- before voiced stops, generalized, cf. Av. niš-, Skt. niş- ($120); with verb ay- ‘go’.
nipadiy phrasal adv. and prep., ‘on the track of, close after’: prep. ni- + loc. padiy, to pad- ‘foot’ ($76.11, $136, $140, $191.1V). тарайту adv. DB 2.73; prep. with acc. DB 3.73.
nipisti- sb. ‘impression’: deriv. of ni- + paid- ($152.11).  [niplisftiya] Isf DB. 4.90 (conj. of Kent, JAOS 62.268).
194 OLD PERSIAN
niydka- sb. ‘grandfather’: Av. nyáka- ($146.- HI); ef. apaniyüka-. {nilyaka nom. DSI 13; [n*yd|kama (522; for -Кат-тату, $41, §52.1, $130, $138.I) asm. A’Sa 4.
niyaSadayam, see had-.
Nisdya- sb. ‘Nisaya’, a district in Media: Elam. nu-is-fa-ja, Akk. ni-is-sa-a-a (5116). Per- haps from ni- ‘down’ + sdya-, to root Av. st- say- Tie’, Skt. §-, Gk. кт. ‘Ties’, pIE *kei-. Nisdya nsm. DB 1.58. |
niXadayam, see had-.
nüram adv. ‘now’: Av. nürom; from pIE *ná ‘now’ (Av. nū, Skt. пй, Lt. nu-nc, NEng. now) + final of (pAr.) *düram ‘long’ (§148.1), cf. düraty. DB 4.53.
pä- vb. ‘protect’: Av. pà-, pres. рйи, РЫ. pátan, Skt. pà-, pres. pati (ablaut, §122). See also zíacapüvan-. apayaiy lst sg. imf. mid. (Ву. BSLP 33.2.151-2; Kent, Lg. 9.42; S71, $214, $233.1II; wrongly to Skt. pt- ‘swell’, Wb. ЖА 41.820-1) XPf 39. padiy 2d sg. imv. (5208, §237.1) DPe 21f. pätwv (§208, $297.IT) AsH 12, 14; DPd 16; DPh 10; DNa 52; DSe 50; DSf 57; DS} 6°; D8n 2°; роз 7°; DSt 8°; ОН 8; XPa 18, 20; XPb 28; ХРе 12, 15; XPd 18; ХР 45, 48; XPg 13; XPh 57; Хе 5^; XV 25f; А:Ра 226; D'Sa 3; A?Hb^; A?He 19. pätw 3d pl. іту. (§237.1T) A'Sa 5°; A’Sd 4; А?На 6°; A?Pa 25. pála пзш. past ptc. pass. (§242.IT) DPe 22. pati- + pã- mid. ‘protect one’s self against’, with Ласа + abl.: райїрауаш@ (828; not wrongly written, despite MB Gr. §69) 2d sg. imv. mid. ($71, §214, 5297.11) DB 4.38.
paié- vb. ‘cut, engrave, adorn’: Av. paésa- ‘adornment’, Skt. pisdtz ‘cuts, adorns’, Gk. токіћоѕ ‘variegated’, OCS pisati ‘to write’, pIE *peik-, cf. Lt. pingit ‘embroiders, paints’ (Wb. AfOF 7.42). Cf. also nipišti-, parsiyd-, Paišiyđwwādā-, pisa-. аріа imf. DSf 54 (§211; cf. Konig, Burgbau 72). [ар #} уа] imf. pass. ($220) DB 4.91 (JAOS 62.268). [pjisia nsf. past pte. pass. ($242.1) DSf 42 (Bv. BSLP 30.1.62; Konig, Burgbau 71; not dista with Hz. Apī 121-5].
mi- + pub- ‘engrave, inscribe, write’: niyapat- Sam Ist sg. aor. ($02, $102, $130, $218.T, $226.IT) DB 4.71. mipaislanaty inf. ($03, $122, $288) XV 24f. nipislam asf. past ptc. pass. (803) XV 22f.
nipistü npf. XPh 31. nipistam nsn. ($122) DB 441, 47f; DNb 57°; DSe 52.
paišiyā- sb. ‘script, written text’: deriv. of pai- (§89, §144.V). See also Parsiyduvada-. ри nsf. DB 4.91 (conj. of Kent, JAOS 62.268).
PaiSiyd'uvdda- sb. ‘Paishtyauvada’: АКК. pi- &-"-hu-ma-du. Perhaps, 
======= 219
with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing’ + "wüdá- ‘abode’ (572, §89, §126, $127, $142, §166, 5160.1): ‘Home of the Archives and Sacred Writings’ (on Pasargadae, ef. also Kónig, RuID 66; but Hz. ApI 275-6, modifying his view ш AMI 1.86n, takes prior element to be pati-, pati- becoming pa&-, with epenthesis; Bthl. AiW 907-8 normal- izes Piši- after the Akk., but gives no etymology). Paisiydwddim asf. DB 3.42. Parsilydluvadayd absf. DB 1.36f.
pa|camàm] adj. ‘fifth’, asf.: wrong restoration of Wb. at DB 5.8 (ef. Kent, JNES 2.109).
pal- vb. ‘fly’: Av. pat-aiti, Skt. pát-ati, Gk. vérerat, Lt. рені ‘seeks’, pIE *pet-.
ud- + pat- ‘rise up, rebel’ (cf. Ву. TPS 1945.64-
66): udapalatà imf. mid. (§84, 8213, 5285.П) DB 1.36, 38, 74, 78; 2.10, 14f; 3.24, 79.
patiy adv., prep., prefix ($140.I, $1911): Av. рай, Gk. (dial.) rori, pIE *poti, cf. pIE *proti in Skt. prát, Gk. Hom. троті, classical rpés (cf. Lg. 20.9-10).
(1) Adv. ‘thereto, again’: DB 2.37, 48, 57; 3.04, 71. pati-maty ($186) DNb 32f.  nai-pati-mà ($133, 5186) DNb 20. yadi-patiy (8136) DNa 38. (ya-patiy XPa 15; XPf 40f.
(2) Prep. (8271) with ace.: DB 52 ‘during’; DNb 22 ‘against? (Hz. ApI 273 reads par[slaiy ‘in court’, sb. to root fraé-); postposed DB 2.62 ‘on’. Encl., with ace. ‘during’ DB 1.20 (8133, $136); with inst. ‘near, at’ DB 2.16°, 3.26; with loc. ‘on, upon’ DB 2.76, 91; 3.52, 92. Ву. BSLP 42.2.70 takes
```


## [2026-09-07T20:45:01.532Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ===\"; grep -n \"nibi\\|nib..tan\\|nibēg\\|nibeg\\|nipēk\\|pēsīd\\|pēsīdan\\|pēšag\\|pēs\\b\" PHD.txt | head -20; echo \"=== PHD_mackenzie ===\"; grep -n \"nib\" PHD_mackenzie.txt | head -20",
 "description": "Grep MacKenzie"
}
```


### [2026-09-07T20:45:01.610Z] TOOL RESULT

```
=== PHD ===
128:delete mezidan ... suck. for ?mēzišn ... read ! meziin ... for mistan, *mēz- read... *mēz-.. mihoxt [mytwht' = Av. midaoxta-| falsehood. *mihr .. add ~ druxtan : break faith. add mizīdan, miz- [myc-ytn' | N mazidan] suck. for *moy-mard ... read mowmard ... mēy ... add M mwy. read nüxun [n^hwn' | P nxwn, N nàxun] (finger) nail. delete nāyīzag ... (read wezag). nek, ~th ... add benefit. nibastan ... delete SKBHWN-tn' < A Vškb; nibastan ... read M nb’st, P nb’y-. nibeg ... add M nbyg. nibištan ... |YKTYBWN-tn'... (not -stn'). nidan, nay- |DB(Y)LWN-tn' < A Ydbr |... nigün, ~sar |-s 1 | (P ngws’r)| downwards. add *nihēb |nyhyp | N ~] fear, terror. for nīšān read nišān...
512:nest [LOY T! < А P?yty | M nyst, N ~] is not. ~ih : non-existence. néw [TB < A tb; nyw' | = M, N —] good, brave. ~-ardaxSir [nyw lthsyl | N nard !] backgammon. nézag [nyck! | N néza] lance. nēzūmān, —16 [nycwmn', -yk! | M nyzwm!n] dextrous, skilful. -~th: skill, artistry. nibard [nplt' | N nabard] fight, struggle, battle. ~ag [-k! | N ~a] tried, experienced. nibardīdan, nibard- [npit-ytn! | P nbrd'd] fight, do battle. nibastan, nibay- [SK BHWN-tn! < A У hb; npstn', npd- | M nbst] lie down, sleep. nibāstan, *nibày- [np'stn! | M nb’st, nb y-] lay down. nibég [npyk! | N niwé] writing, scripture, book. nibém [npdm | (P nbdm-)] lying, prostrate. nibištan, nibés- [VK TY BWN-stn! < A yktbwn, У КЬ; npstn' | M nbyšt, nbys-, N —] write. nidan, nay- [YD(B)LWN-tn! < A ydbrwn, V dbr | M nyydn, ny-] lead. nidom [nytwm] least, smallest. nifridag [nplytk' | N nifrid] accursed. nifrin [nplyn' | N <] curse. nigah [nk’s | M пол, N ~] look, attention. ~ dāštan: watch, keep. — kardan: look. ~-darih, —-dári&nih [-d?/(sn)yh | N —dārī] keeping, care. nigān [nk’n' | P ng’n] buried. nigar- [nk’l- | M ng’r-, N ~] draw, design, paint. ~ag [-h! | (M agin, N nigār)] image, picture, diagram. nigástar [nk?s I] guard; protective. nigeridan, niger- [nkyl-ytn! | N nigaridan] look, observe. --išn: observation. ~iSnig : evident, manifest. nigéxtan, nigéz- [nkyhtn!, nkyc-] expound. ~i$n: exposition. nigéz [nkyc] exposition. nigün [nkwn! | N ~] inverted, upside down. ~th: depth, downward direction. ~sar [-s?l | М ngwns’r] downwards. nihadag [nyd’tk' | M ny? dg] foundation. nihādan, nih- [TNH TWN-tn! < А hnht, ~ nht | M пуа, nyh-, N ~] put, place, establish. nihal [nbl | N ~] sapling, self-planted tree. nihān [nyh’n' | N ~] concealment, secrecy. ~ig [-yk! | N ~7] secret. nihang [nsng] small, few.
549:pazzām- [pz^m-] mature, ripen (intr.). ~išn: maturation, ripening. pazzáménidan [pz’myn-ytn'] = pazzāftan. pēčīdan, pēč- [pyc-ytn' | N ~] twist, entwine. pēm [pym] milk. péménidan, pémén- [5ymyn-ytn'] cause to well up, swell up. pen [p(y)n'] mean, miserly, niggardly. ~ih: meanness. pérámoón [pyPmwn! | M pyrmwn, N ~miin] around, péróz [pylwe | M pyrwz, N ~] victorious. ~th: victory. pérózgar [pylwekl | N ~] victorious. ~ih : victory. pés [pys | N ~] mottled, leprous; leper. pēsīdan, pēs- [pys-yin'] colour, adorn. ~iSn: adornment. pestān [pyst?n' | N ~] breast. pēš [LOYN! < A I-‘yn; руї | = M, N ~] before. IpéSag [py$k! | N péfa] trade, craft; guild, caste. *pēšaģ [pysk'] limb, member, part. pëššánig [pyš”nyk! | N pēšānī] forehead. pēšār [py | M py?r] leader, guide. ~ büdan: be guilty (of), commit. pēšārwār [руло], v. pëšyàr] urination. péSémàl [руѓут?/, v. hamēmāl] plaintiff. ~ih: prosecution, pēšēnīg [pysynyk! | (M pysyn(g), N pésina)] former; foremost, noble. pëš-gāh [pyšg”5 | N ~) audience chamber; foremost seat. pēš-kār [py$k'/ | N ~] servant. pēšēbāy [byš')wp?d | M руйору, N péfwa] leader, vanguard. ~th: leadership. pēš-pāraģ [pyšp*/k! | N —a] an appetizer. pēšyār [pyšk”/ | N ~] urine. petit [pytyt! = Av. paitita-] penance. ~ig [-yk'] penitent. ~igih: penitence. petyárag [p(y)tyd'lk! = Av. paityára- | M pty’r, N patydra] evil, mis- fortune; adversary; astr. detriment, ~th: (onslaught of) evil. рі [AB' < А "bur р(у) | M pyd] father. *pid [5(5)!! | P pyd] meat, flesh. pidar [AB Ytl, v. ipid ; ру | M pydr, N ~] father. pih [pyhw'] food, victuals. pīh [TL BA = A trb; рур | N ~] fat, tallow. pil [py] | M pyl, N ~] elephant; (chess) bishop. --bān [-p’n' | N ~] elephant-driver.
732:adorn ārāstan, azrāy-, payrāstan, pēsīdan.
1170:caste pēšag.
2177:guild pēšag.
2573:lay (down) nibastan; ~ foundations fragandan.
2602:leper, leprous pēs.
2617:lie down nibastan.
2634:limb handām, (hannām), pēšag.
2776:member handām, (hannām), pēšag.
2855:mottled pēs.
3045:pārag, pēšag,
3539:scriptures nibēg; abestāg, hādamāns'r, dad.
3694:sleep (n.) xwàb, xwamn; büšasp. sleep (v.) xuftan, nibastan, sleeping-platform bālēngāh. sleepless axwamn.
4042:trade pēšag; wāzār(a)gānīh.
4365:write nibištan.
4540:salag! škaf- škāftan nibay-! nibastant ških- šken(n)- šken(n)išn škēbāgīh škēbāg škeftīh škeft 1*$kķēh &kohih škūf- škūfag škoft škuftan hur!, šakar škarw- škarwīdan škarag škastan škaft
5080:narī nibés-t nibištant Ozan-! Ozadant
5146:nifrin wafrūnag nifrīdag Obad-/oft-1 Obastan! nibard- nibardīdan nibard nibardag nibastan wabz wafišn xwest xwestant nibistan 1-2paft waz- wizār wizür- wizarisn wizārdan wizārdwars wizīh-
=== PHD_mackenzie ===
585:       nibastan           delete SKBHWN-tn' < A Jskb;
586:       nibistan           read M nb'st, P nb'y-.
587:       nibeg ... add M nbyg.
588:       nibistan ... [YKTYBWN-tn' ... (not -stn').
1034:anibuhlag ['n)pwhlk' = Av. anapt/rt/(Ja-] inexpiable, unatonable; the
1042:inaftan, anib- ['n)pen', )n)p- I M )n)pt, Cn'm-)] avert, reject, frustrate.
2771:ham-nibardih [hmnpltyh] (single) combat.
3721:nibard [nplt l I N nabard] fight, struggle, battle.
3723:nibardidan, nibard- [nplt-ytn' I P nbrd'd] fight, do battle.
3724:nibastan, nibay- [SKBHWN-tn I < A v Ikb; npstn l , npd- I M nbst] lie
3726:nibastan, ·nibay- [np'stn' I M nb'st, nb'y-] lay down.
3727:nibeg [npyk I N niwe] writing, scripture, book.
3729:nibem [npdm I (P nbdm-)] lying, prostrate.
3730:nibi~tan, nibes- lKKTYBWN-stn < A yktbwn, v ktb; npltn l I M
6016:audience handemanih; --chamber           battle ardig, hamranih, lang, nibard,
6018:augur murw-nis.                             nibardidan; v. fight; doing
6084:book madayan, namag, nibeg.            brigandage rahdarih.
6233:combat hamnibardih, hamranih,            c01lduct (n.) warisn; v. bella'viour
6510:eternal dagrand-xwaday, hameig,                    experienced kiiragah, nibardag.
6601:fight (n.) Jang, nibard, pahikafisn;           (tazidan); cause to ..... taxtan,
```


## [2026-09-07T20:45:02.511Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB nib ===\"; grep -n \"^nib\\|nipēk\\|nibēg\\|nipištan\\|nibištan\" NYB_vol2_glossary.txt | head -20; echo \"=== UNV ===\"; grep -n -i \"nibi\\|nipi\\|nib\\|book\" UNV.txt | head -20",
 "description": "Grep Nyberg and Unvala"
}
```


### [2026-09-07T20:45:02.581Z] TOOL RESULT

```
=== NYB nib ===
2749:nipēk [npyk'] document, codex, book, pl. ~-ihā 108°. 1097. 1112-917. 1128. — < *ni-paya-ka- ‘that which is kept, or is to be kept, in safe custody’, ‘record’, originally an administrative term; MPrth Prs nbyg; Paz. nevé, nivé. From Av. (886) ni-pãy- (pres. also pay-). — Bthl’s ety- mology: nipčk < "nipčhak < *ni-paida- ka- from a SW form of nipištan (MirM IV, 30, n. 2) is untenable.
2750:nipēkēnītan [npykynytn'] to codify, to reduce to the form of an official book 111°.
3130:pēsīt [pysyt'] adorned 362. 10819, 1114. — Derived from Av. (818) paésa- ‘ornament’, from Av. (817) paés-, OP pais-, v. nipištan.
5258:ni-pais-: nipištan
6049:nbyštn, nbys-: nipištan nfryn: nifrin
7286:nuvištan (navištan, navés-): nipištan
=== UNV ===
97:Mel. As. ;  Melanges  Asiatiques,  tires  du  Bulletin  de  rAcadeiiiie  ...  de  St.  Petersltourg. ]\[x. ;  The  Book  of  the  Mainyo-i-Khard.  Tlie  Pazaiid  and  Sanskrit  d’exts  .  .  .  hy E.  W.  West.  Stuttgart  &  London  1871.
106:SBE. :  The  Sacred  Books  of  the  East  .  .  .  edited  .  .  .  hy  F.  I\Iax  ^Müller.  Oxford. SWienAW. :  Sitzungsberichte  der  kais.  Akademie  der  Wissenschaften  in  Wien.
276:räö  hastan  evenak  -  2  i  sanib  ci  p>ci  16.
698:sräy-dunibalah  u  sräy-näd  u  sräy-harhiit
1085:estäi  nipist  ängön  nipeJc  pa  us  108.
```


## [2026-09-07T20:46:28.058Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 101 (p.80) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==102{print}' HRN.txt | head -60",
 "description": "Print Horn p.80"
}
```


### [2026-09-07T20:46:29.295Z] TOOL RESULT

```
=== HRN leaf 101 (p.80) ===
— 80 -
357. 2^^'*^^ ^Handwerk, Gewerbe'.
aw. vergl. pistro- 'Gewerbe*; phlv. pesak.
358. peiyäre 'Tadel' (Sahn. III, 1763, V. 95; 1803, V. 383)^).
aw. "^paiti + 2 [/"gar' (ai. praii + gar- bedeutet auch
nur 'anrufen, begrüssen, antworten).
Spiegel, Ar. Periode, 229.
Bartholomae meint, man könne auch an Ableitung
von ai. prati + [^har- denken (vergl. pratihdrana- und
die Bedeutung von lat. ohjicere), Ai. h entspricht ja
sowohl indogermanischem gji wie g2h,
peiyäni s. peyäm (No. 348).
359. peig (peik) Tussgänger, Häscher, Bote', arab. faij,
aw. "^padika-,
de Lagarde, Ges. Abh. 74; Nöldeke, Tabari-
Übers. 448, Note 2, vergl. auch Denkschr. WAW.
Band 38, 14.
360. peikär, peigär *Kampf'.
aw. *paitikära' vergl. paiti.akerenaot (vd. 2, 6);
phlv. patkär 'Kampf (z. B. vd. 5 (33) GL), patkäritan
'Köcher, (z. B. vd. 4 (137)), patkärok (AV.).
arm. LW. payUar *Kampf' .
361. peiker *Bild'.
Sii^. patikara- 'Bild'; iphlv, patkar (Bund.), arm. LW.
pafker.
362. peikän 'Pfeilspitze, Pfeil'.
aw. paiti -\- [/kan- (?); arm. LW. paikan\daran
de Lagarde, No. 1834.
vergl. serb. LW. pHk 'Pfeilzeichen der fahrenden
Leute (Miklosich, Denkschr. WAW. Band 38, 11);
während peik 'Bote, Laufbursche' (ib. Band 35, 144
und 38, 11) zu np. peik (No. 359) gehört.
363. pei/imiden'mQ^^Gn\ zeigen', Prsies. peimäy-emj peimäny
peimäne^).
*) An der letzten Stelle wie auch sonst (z. B. IIT, 1642, Vers 2,
Calc, 1708, V. 3765) ist in der VuUers-Landauer'schen Ausgabe
h^ in p^ zu ändern.
«) Eine *Masft' (HohlmassJ, z. B. Jnnn ZKM. V, 302.
```


## [2026-09-07T20:46:41.988Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN pis ===\"; grep -n \"pīs\\|pis 'Aussatz\\|Aussatz\\|pise\\|weissfleck\" HRN.txt | head -20; echo \"=== HRN nivistan/nibistan ===\"; grep -n \"niviS\\|nivišt\\|niwištan\\|nawištan\\|nibišt\\|schreiben\" HRN.txt | head -20",
 "description": "Grep Horn for pis and nivistan"
}
```


### [2026-09-07T20:46:42.124Z] TOOL RESULT

```
=== HRN pis ===
342:man selbst an Reimen wie pisend auf hidend (79, 315) u. dgl.
3056:Praep. paiti; die Aussprache pisend findet sich nur
3070:In Indien spricht man piser ; die nämUche Aussprache soll auch
3086:323. peSenjTden, pisenjidefi ^besprengt werden ^), j)^^^^j^
3341:355. pes *Aussatz', pest leprös', pesl, pese Schecke*.
3346:(Rind)', Bund.); phlv.^eS(/Ä*Aussatz', ^;^7.<?f^ geschmückt';
3348:kurd. pis^ pisa; af}'. pes, pesai 'Aussatz.
7784:LW. kurd. gv' 'Krätze'; bei. gar ^Aussatz, Räude,
13384:pisend 319.
13387:pisenjlden 323.
=== HRN nivistan/nibistan ===
273:schreiben, wie mir die Zeichen gerade in die Feder fliessen,
613:(bezw. e) zu schreiben sein.
1781:-) Assa- hätte ich auch No. 77 schreiben müsRon (KZ. 32, 577).— 37 —
2705:schreiben), Metrum: Xeflfi
7658:kes, vergl. pö^yötkes (nur umschreibend), arm. LW. ßes.
8258:^) Die Syrer schreiben nach Mitteilung des Herrn Prof. Nöldeke
9099:schreiben, Praes. miw^s-em; nulje, nuwB^) *Wort
9102:ap. ni + [/^pais-, nipistanaiy 'schreiben* 2) — ai.
9105:kurd. LW. nivlsin schreiben; oss. d. finssun , t.
9632:schreibend), hEzam bezw. ezam (päz. hezam) ; ai. idlimd-.
9676:^) Phlv. yät ist vielleicht nur umschreibend.
10110:schreibend.
10538:schreibend, vgl. dranggav.
10831:das Pehlevl wahrscheinlich nur umschreibend.
10865:nur umschreibend.
10872:Vielleicht nur umschreibend.
10917:umschreibend (glossirt durch g(i)ris, np. c/irih).
11149:'führen, bringen {vajlnUan) nur umschreibend auf-
```


## [2026-09-07T20:46:43.721Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB ===\"; grep -n -i \"aussatz\\|pēs\\|pisa\\|nipišt\\|schreiben\" HUB.txt | head -20; echo \"=== BRT pistra ===\"; grep -n \"pistra\\|pi§tra\\|Gewerbe\" BRT.txt | head -10",
 "description": "Grep Hübschmann and Bartholomae pištra"
}
```


### [2026-09-07T20:46:43.791Z] TOOL RESULT

```
=== HUB ===
719:zu schreiben. Die echte Pehleviform war naturlich
1425:323. Np. %i(i8aifkijtdan, pisanfidan *besprengt werden =
2498:als urspriingliche Bedeutung 'Galle' zuschreiben muss,
2894:sein an pidar u, s. w. wie pusar, pisar (aus pus) etc.
4463:ataSy arm. LW. afas (Sebeos), phi. ataocs^ zd. atars; pisan-
4815:nuvistan schreiben (= nivistan) , nuvdxtun (= navOxtan)
4818:'schreiben'; praef. gu- — zd. ap. vi- in gur^xtan, guzldan
4883:Shk. 269; diz- *b6se* = duz, ap. dws-, zd. dus-, dui-; pisar
5406:Pehlevi als y zu schreiben und zu lesen ist (also z. B. ydvetan
6212:*schreiben', ap. nipistanaii/; kdbln *Mitgift* = kdvm JRAS.
6297:lektisch. Die Araber schreiben zudem sf fiir sp in pers.
6695:drjg u. s. w., BB. 4, 33) schreiben, so war der Uebergang
7251:ap. "^Old^at-, zd. drisat-] pus 'Sohn (daraus pnsar, pisar
7489:durch & umschreiben will.
7542:pes *Aussatz, aussatzig JRAS. 1894, 451 = zd. pa^sa-;
7544:ap. *nipaisamiy {niyapisam ist sigm. Aorist ^- idg. ni-e-pik^-
7766:auch hier wieder h nicht schreiben und nur uvd geben:
8439:ristan *spinnen, pr. resam, Wrzl. reik^; nivistan 'schreiben*
=== BRT pistra ===
5548:•  jj  g-  'airyaman-,  g.  airyäman-  m. 'Genosse'  uzw.  priesterlicher,  Angehöriger des  ersten  oder  Priesteratands  (s.  unter 'pistra-),  'Sodale' ;  Sing,  auch  koU.  'Soda- lität',  nur  gAw.:  iJ  yama  kp  x^allus  {%<!.) dätäis  anhat  yp  ,  .  Y.  /fg.  7 ;  —  ahyScH x'aSus  (sd.)  yjsal  ahyä  virizsntm  mat yamnn  . .  Y.J2.1;  —  yf  '^jvaj  masdn asruinm  . .  yazli  (sd.)  apa  K^'aüSuScä  tar>- maitTm  virn^nahyiilä  . .  'yamanascä  . .  Y. 33-4  i  —  y^  asäuia  vahiils  :^aSä  (sd.) vä  al  vä  v>r>iSny3  yämiiä  (IS.  als  Subj.)  '> vil .  .  Y.  JJ.  3;  —  pairl  clausus  'yama- nascä  dadaili  ndii  .  .  i-ir>z5nä  (sd.)  Y.46. I.  A)  Name  einer  Gottheit":  vairya sar)ha  para.äi'd  upa.vasanuha  avi  nmli' mm  yamaini  imat  sanhsis  'yamanäi  J' "A^,  geh  weg,  fahr  hin  ins  Haus  zu  A., das  sollst  du  dem  A.  kund  machen"  V.
16412:-        ..     ■'      ■'.  .'  --  werk,  Gewerbe'.  —   Vw.: ptiak  \\n  ^v..: -uiäya
30233:Eig.  etwa  'Betrieb'  sti.  'Gewerbe';  zdtd  V. ihav.  —  Pü.:  hittuxi  ('induitciosus'),  Sü.: frakiliiarmä  (tonst  auch  suvyODOsiyi  -  Mx.  - und  ftaij-livyai/asäyT  -  Sg.).
```


## [2026-09-07T20:46:53.150Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HRN 355\"; sed -n '3335,3360p' HRN.txt; echo \"### HRN nivistan\"; sed -n '9090,9115p' HRN.txt",
 "description": "Read Horn entries 355 and nivistan"
}
```


### [2026-09-07T20:46:53.203Z] TOOL RESULT

```
### HRN 355
2) Vergl. No. 286 Anmerkung. Als ich dort Bartholomae's
Etymologie während der Correctur einfügte, hatte ich vergessen, dass
ich selbst später die gleiche Erklärung brächte. Inzwischen ist der
vierte Bogen gedruckt worden.- 79 -
(s. Nöldeke, TabarT-Übersetzung, 117 Anm. 2; de
Lagarde, Ges. Abb. 180 irrt bezüglich des Vokals).
355. pes *Aussatz', pest leprös', pesl, pese Schecke*.
g. pTsk,
ap. madyaq = o Xengog (Ktesias bei Photius), niaadyai
corr. aus maoärai (Hesych); aw. paesa- aussätzig*
{zaranyö.pis-^ paesah- [pa^sa-) 'Schmuck', pacsa- *bunt
(Rind)', Bund.); phlv.^eS(/Ä*Aussatz', ^;^7.<?f^ geschmückt';
ai. pe^aS' 'Schmuck, Zierrat'.
kurd. pis^ pisa; af}'. pes, pesai 'Aussatz.
Vergl. de Lagarde, Ges. Abh. 75, 217, Hübsch-
mann ZDMG. 38, 426.
856. 2}es 'zuerst, zuvor, pester ^ j)Psin^ pesäm 'Stirn'.
ap. patis 'gegen'; aw. paitis^); phlv. pat(i)s-, pes,
pHäntk 'Stirn, arm. LW. patS\gam n()oardg fJfJ^^a.
wa/. pat^', pitS"^), sar. pac 'entgegen*.
LW. kurd. pU; bei. pes, n. pes^ pesa (302).
de Lagarde, Beitr. z. altb. Lex. 50; Pers. Studien,
74.
Als Praefix findet sich pes z. B. in peskär, peskes^ pes-
gäh, pes/^er (phlv. pat(i)sxur^ bezw. -/rar 'Tischtuch*,
vd. 16 (17) GL; vd. 5 (48) Gl. unklar). Vergl. auch
### HRN nivistan
1050. neverdtden (neverden) *drehen, winden, wandern',
ueoesten (AM. 2 Zeile 7), neverd.
ai. w/ f- Ki^ar^- zurückkehren, fortgehen, den
Kücken kehren etc.*.
Wenn die Etymologie richtig ist, so wäre die ur-
sprüngliche Form *mverdlden bezw. *nivesten,
nöx siehe hemz (No. 1108).
nöS, nöse 'lieblich' siehe enöse (No. 128).
1051. niwiSteu^ miwisten, nibistm, ]n2/2^ (jüd.-pers.)
schreiben, Praes. miw^s-em; nulje, nuwB^) *Wort
Gottes, Qorän*.
Käs. Z. vinemes,
ap. ni + [/^pais-, nipistanaiy 'schreiben* 2) — ai.
|X/>e^-, pincdti bedeutet nur 'schmücken'^); phlv.
n(i)p(i)stav, n(i)p(i)stak, n(i)p^k 'Schrift*; ksl. pisatL
kurd. LW. nivlsin schreiben; oss. d. finssun , t.
fissin, nifista 'Schrift' (287); bei. LW. nibTsay , pp.
nibista (261) ; wa/. si/n. sar. LW. neoisam.
Die Wörterbücher haben noch einige teils auf
falscher Punktation teils auf Analogiebildung be-
ruhende np. Formen wie nuwes (wertlos), miwesten.
Die Wurzel ist peikf, vergl. gr. tioiy.CKo^,
V) Salemaun, Noch einmal die seldsohukischen Verse, M61.
asiat. X, 217.
p{r|2?5 des Buches Ezra wird ebenfalls mit np. niivisten in Ver-
bindung gebracht.
```


## [2026-09-07T20:46:54.592Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BRT pistra ctx\"; sed -n '16400,16420p' BRT.txt; echo \"### HUB 7540\"; sed -n '7535,7550p' HUB.txt; echo \"### HUB 8435\"; sed -n '8430,8445p' HUB.txt",
 "description": "Read Bartholomae pištra and Hübschmann"
}
```


### [2026-09-07T20:46:54.689Z] TOOL RESULT

```
### BRT pistra ctx
'    .'    .    1'    I-  ir  ..  Altesroform   duu   vrieder;   t^I.    die   Vor.  in
'■/''•  ^'•^•"■'  •■  *"'•■  I     Mtj     UÄMg  CLD.  GGA.  ;js5.  3,4.
.  j.pi8-,/i3-Ot'Schmudi;Kostbukeifv.  j    ^jj^,.  „    .j,^   Stand,  Kaste'«:
an  die  Kostbarkeilen  des  leiblichen  Lebens  i
sich  klammernd  das  geistige  Leben  preis- gibt" F.  40;  40.
KompE.    —    Zum  V.  fiaes-.    —
Priester,  Krieger,  Bauer,  Handwerker" 15  17.
*)  Es  werden  deren  drei  geschiedcD,  nur  Y. rg,  17  vier.     Bauern  und    Handwerker  werden
Pü.:  ♦/«;/«  (so  jedenfaU»!),  erL :  -ifr  (PPGL  ■  (5^  gewöhnlich  zusaniinengefasst  worden  sein. 13.  4).  Dam  die  Glosse:  lai  hac  zarr  u  sTm  ,  j^,  g^«,  erscheinen  zT.  abweichende  Namen, i^ailai  iaval.  —  >)  ISach  S  a«.  1  nämlich:  a-ryamait-  oder  (vll.)  haj»aan-  Kr  den
•  p.  ",»  ä  pisä»  viyatara  »»"  Bh.5.  4.  I  P'«ster.,_:t"flS^_  nnd  nar-  fär  den  Krieger-, 0  Opfert  La  Langne  des  Mide,  wiU  \rlä  ■  =."<"■  chjai/O'-.  vastrya./iuyaH^  oder  (koll.)  i;^.- ,    ,.,„  V7    ,_    ,A  '   ima-  oder  vinzinya-  für  den  Bauernstand.   VgL
■  ■*'■  5^^*  Gdn,  VSl  ?.  18.  der  aber  nur  iT.  Richtiges  gibt
•  j.   pisinah-   m.   EN.   eines   iranischen  |     KompE.  — Zum  v./fl?j.,eig. 'Färbung,  Farbe'; Fürsten  aus  der  A'af fly-Dynastie,  Enkels      vgl.  ai-  ''«™°- m-  -  np.  __vgU  >™  'Hand-
-        ..     ■'      ■'.  .'  --  werk,  Gewerbe'.  —   Vw.: ptiak  \\n  ^v..: -uiäya
des    Kaväla:    kavBü  -natths   alaonS  Yt. '
,h).
13.  132;    —  yimca   kavam    'mm  (AS.)->   ,  ^  ^^5^^»-  m.  i)  'Quetschung.  Quetsch- Ei|!'Bed.?     Ob  A(ygl.  aipty^sinah-  (zum  V.   r"*^^'    Jü"   j^'^Pfe«'   Instrument   beige- '■'■r/B''«flj-,  S2.i)?  — »Sid'/aE.   brachte  Wunde':  _>■?  jfiwe  'nm  jatntt  ytm
-   ,   —  ar."*7-i1   ,  „.„.         .  ,j  
•  j.  pisra-  m.  Bezeichnung  einer  Vor-  ^,^.^,^  ,^^  ^^J/^^^^aiW"  (sd.)  V.  5. nchtung  zum  Schweissen  von  MetaUen:  ^  ^)  '(Ausgequetschtes  sva.)  MehT: -rai  hüca  zaranyöaa!j,ät  . .  'rat  haca  ,r>-  ^^^  ,^^  ^  ^^  ia?  darva  «ru^J  "wenn ,aii^.sa^äi  'rat  haca  «ySsji^Pät .  .  'rai^;^  ^j^j^j  ^^^  Teiganmachen)  zurecht haca  haosaJnam5.,a^ilt  V.  8.  87-90.  ,  gelegt  wird,  dann  heulen  die  D."  V.  j.32.
Et.  ?    Falsch  JK.  A  hymn  44.  -  Pu. :  p  dt  ar.    «  ^^^   ^.    ^'  ^.^_^^.     _    ^^,_  ^^    ^..^    .^^^,^
•  j.piäant- Adj. 'zerstossend,  durch Stossen  si.  piffä-  n.  'Mehl'').  —  Pü.: /«oi").—  'i  Ob zerhackend">:ww37a>i«..7'är;7«a>i^wrt/a/y;  ^''  W"-  A''^'-  '■  S  235b?-»>  S.  in  '/ilfra- {%&.)  amra.namäi  'ial5  upara.»amat  Yt.  •  S-  piSyant-  Adj.,  PPA.:  s.  pah-, J4-19-                                                         I"  j.  piixJia-  Adj.  {fem.  *3ä-)  'der  fUnfte
PPA.;    Praes.  I  oder  3.    —    Vgl.  ai.  finöüi,   „mä/iyB  (näml.  ralus)  vTsyB  zanhimB  däR-
### HUB 7540
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
Fur an- und inlaut. i' -= s ist unregelmassig s ein-
getreten in: sdx 'Ttweig =■ skr, gakha- (vgl. Bart hoi omae,
### HUB 8435
so sollte man im Np. *xis erwarten, wie umgekehrt np. xirs
eher auf iran. *fsa- (als fsa-) weist.
§ 130. Idg. st (nach i, u etc.) und kH = iran. ap. st
= np. st und s^:'
a) = s^ : mw6^^ Taust' = zd. rmdU-, arm. msrtfc 'Bundel*
= phi. "^mustik; angust 'Finger, Zehe' = zd. angusta";
ustur 'KameeV = zd. uistra--, pust 'Rucken* = zd. parsfi-,
skr. prstha-; mustan reiben, skr. mrsta-, Wrzl. m&t'g'^\
hihist 'Paradies' == zd. vahista-; xist 'ZiegeF, skr. istako-;
ristan *spinnen, pr. resam, Wrzl. reik^; nivistan 'schreiben*
= ap. nipistanaiy, pr. nuvesam, Wrzl. pdk^ ; histan 'lassen*,
skr. srsta-, Wrzl. serg^ ; hast ^) 'acht* = zd. asta, idg. okHOu ;
biristan 'braten' mit st aus skt von Wrzl. iran. brj und
bri^g = idg. bhrzg, oben p. 27.
b) = st: dost Treund' == ap. daustar-; §ast 'sechzig'
= zd. xsvasti- ; pist 'Mehl' = skr. pista- ; mahist (ZDM6.
```


## [2026-09-07T20:47:10.216Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt; do echo \"### $f\"; head -c 400 $f; echo; wc -l $f; done",
 "description": "Inspect MON files"
}
```


## [2026-09-07T20:47:11.470Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BQT v1 پیسه\"; grep -n \"پیسه\" BQT_v1_pages.txt | head -10; echo \"### BQT v1 پیشه\"; grep -n \"پیشه\" BQT_v1_pages.txt | head -10",
 "description": "Grep Borhan v1"
}
```


### [2026-09-07T20:47:22.663Z] TOOL RESULT

```
### MON_part1.txt
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


هم مشب جج جب بیج چم �
99339 MON_part1.txt
### MON_part2.txt
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
94500 MON_part2.txt
```


### [2026-09-07T20:47:22.722Z] TOOL RESULT

```
### BQT v1 پیسه
27444:پارسی پیسه شده بمعنی ابلق و دورنک : سفید وسیاه. پیسی که در نازی بر صکویند نام بیماربی
### BQT v1 پیشه
14319:اند یشه - بر وژن هم پیشه » بممنی
15335:کجا کارثان هسگنان پیشه‌بود
26390:پناهیده- بر وزن جفا پیشه ۰ بمه‌نی گرریدن هم هس .
```


## [2026-09-07T20:47:28.158Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npos=sum(len(l)+1 for l in lines[:27443])\nleaf=t.count('\\f',0,pos)\nprint('leaf',leaf)\npages=t.split('\\f')\nprint(repr(pages[leaf][:2500]))\nEOF",
 "description": "Print BQT page with pīseh"
}
```


### [2026-09-07T20:47:29.472Z] TOOL RESULT

```
leaf 666
'علت برص وجذام داشته باشده ۴.\nودنه باثانی مجهول و دال بررزن\nبی سوزن » عبل نمودن و اراده کردن بطرفی\nباشد .\nلیسه ۴ » با ثانی مجهول بروزن کیسه »\nبمعتی سیاه و سفید بهم آمشته باشد - و فیژ\nهی رنگ ی که بفید آمیخته بود» و بعربی ابلق\nکوشد ۴«\nفیش۰ بروزن ریش ۰ ممروف است که\nنقیض پی باشد ۴ - و شاخ درخت خرما\nو خرمای ابوجهل را تیز گوبند ۵ و مافل\nو خرمای ابوجهل را نیز گویند ,و آن ببانی\nکب وت ور بو که\nازمردم خسیس و رذل هم هست - وسفد را حم\nحیکوین د که یش سیاه باشد:\nی سیاز « بابای فارسی بروزن زرنگار,\nرونده و راهرو را گوشد- ویمعنی\u200cپی\u200cسیر هم\u200cآهده\nس که لکد کوب ویایمال باشد.. :\nیی سیر بابای فارسی مر وزن دردسر »\nاو 0 9\nشفه باخدت ویمعتی رونده نیز آعده است ۰\nفسست» بروزن کیست » شخصی است که\nاک تن و ع \u200f\n۴ -درپارسی باستان 085 و در اوستا ۳265 بمعنی دگاشتن و نگادیدن و شش کردن\nاست. ازهمن بنیاد است ۵۸51216 که درپهلوی بمعنی نقش ونگار بسته وزشت شده است و دد\nپارسی پیسه شده بمعنی ابلق و دورنک : سفید وسیاه. پیسی که در نازی بر صکویند نام بیماربی\nاست که تن\u200cاز نشانهای سیاه وسیید دورنگ کردد [رثد ٍ فض-]\nجاه نو سایه ایست که خورشید رابعمر امعان پسه کردن\u200cآن نیست درشماو. :\nآنوری\u200cامیوردی. «بنقل\u200cسروری».\nاین کلمه\u200cدر تر کیبات: کاو یه ( کارست بانشانهای سیاه وسیید) .کلاغ یسه (کلاغی\nاست دورنگه).کلا یه مشتف کلاغ یه (زبر وزبرشدن و ی اسراب 3\n۱-۳ «بارتولمه ۸۱۷» «نیبر کف ۱۸۱۰۱۹۰. ۴ - پارسی باستان0] 02115 ( مقابل»ضد)\nاوست۳210150), پهلوی ۳90)1(5: ۳۵68. وخی تا5ا۳2, ۳1/50. سریکلی۳26 (ضد, مقابل)\nکردی 0150 ,بلوچی ۳۵51 «اسشق ۹ ۶ تب رکه ۶ - ۸۵ ۰۹ ۵ - رگ : بیشو پیس .\n۶ پیسی - ابرص . رلك: پیش وییه .\nیه ازسفحهٌ 1۳۹\nنلاهرالبدن ویغور ومکون فی\u200cسایرالاعناء حتی ,صیرلون البدن\u200cکله\u200cایض: وبفال اهذاالنوع الننتتر.»\nوت دوجا ازین مرض بادشده: آپان بشت بند۲ » وندیداد پند۲۹. این بیماری | کرچه ساری\nنست, معپذا ملل قدم را مسیار شوم مبدانستند . از همن\u200cرو درآ بان به شت و ونددداد (ندعهای\nو۳ آمد هکه پبسی را بانداز ما کر . هردوتی همین موضوع را در کاب اول ند\n۳۸ آورده : اک کسی درمیان ابرانیان بمرض برص میتلاگردد نباید درشهر بماند ودرانجمن\nدرآید . ایرانبان کمان میکنند که مبتلابان بان مر ضگناهی دسبت بخورشید مرتکب شده\u200cاند ,\nاک بیگانه\u200cای (خارجی) دچار این ناخوشی گردد اورا از کشور ببرون میکنند. » ازروایت طبری\nو بلعمی نیز برمیآید که نزد بنی اسرائیل هم اين مرض موم بود ومبتلابان بدانرا اخراج\nمیکردند 1 رلك: قاموی ۰قدسر: فذبل: اردو ] . «مزدبسناصی ۱۱۰ - ۱۱۲ رلد: فسه .\n۵ پروزگر - مرکب از : پیروز ۳+ گر ( پسوند فاعلی ) [ رث : پیروز ] ؛\nعالب فاتح ( بر ها قاطع )٩۰\u200f'
```


## [2026-09-07T20:47:41.722Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (668,669,670):\n    print('##### leaf',i)\n    print(pages[i][:2200])\nEOF",
 "description": "Print BQT leaves 668-670"
}
```


### [2026-09-07T20:47:42.982Z] TOOL RESULT

```
##### leaf 668
پیشواز است که بعربی استفبال گوبند و نوعی
ازجامة پرشیدنی هم هست .
پیش خاه - بسنی رواق است که
بیشگاه خانه باشد - و ایوانی که در مرتبهٌ دویم
ساخته باشند ‏
پیش خورد بر وژن لیم خورد »
و پیمنی پیشکی و سلم فروخته هم هست» یعنی
فلة نارسیده و مو# نايخته وامثال آ که بیشتر
فروشند .
یشد۵اذ ۱ - با انی مجهول و دال
اسجد بروزن پیش باد ؛ بمعنی عادل اول است -
و اول کی را نیز کویند که نظلم برحاکمی
کند . وحا کمی که‌اول‌یفور مظلوم برسد- واول
پیشدادیان را هم گویند که هوشتکه باشد واو را
فارسان بشداد میگفته‌اند یعتی عادل اول و بعد
ازر طهمورث و پعد ازو جمشید و معد ازو
ضحاك و فربدون و منوچهر که شش تن باشند
. و بضی بازده تن را گفته‌اندکه ابثان دو زار
و چپار صد و ینجاه سال یادشاهی کردند : اول
هک ‏ رت حا
6۲ سه
جمشید. پنجم‌ضحاك, ششم فریدون: هفتم‌عنوچهر»
هشتم نوذر» نهم افراسیاب تركك. دهم زو پس
طهماسب‌ین منوچهر» بازدهم گرشاسب- وزری را
نیز کوین دکه مش‌از کار بمزدور و کار گر دهند
و آلرا بعربی تقدمه خوانند ۴ .
پیش‌داد بر وزن ریبش‌دار ۰ حربه‌ای
باشد بس.ار بزر که که ازآهن وفولاد سازند و بر
آن حلفهای چهار کوشه هم از فولاد تصیه کنند
وبدان خولك و کرا زکشند.
پیش‌دست < بر وزن مش صست ۰
بمعنی بعادستاست کهاجرت میشی‌دادنب ویش-
دستی کردن وسبقت نمودن- و غالب شدن باشد
و صدر مجلس را نیز کنته‌اند. ویمعنی مددکار
هم‌آمده است - و نقد راهم میگوبند که نقض
نسیه باشد.
پیش دو لشکر صحر ا- کور خر
باشد» وان جانورست شببه بخض. .
۳
یس "باشن فرشت پروریند نو 9
فرجي, و جامةٌ پیش باز راگوننددکه بیشتر زنان
پوشند .
پیشکار ه با کاف بر وژن رش دار »
خدمتکار وشا کرد و مزدور باشد - و بمعنی همد
ومماون و مددکار هم هست . #
ککه درپیش قالون وضع کرد و داد گری نمود بالضتین واضم . حمز؛ اصفهانی نیز این‌کمهرا
درست معنی کرده نود : فیشداد اول حا کم باشد چه اوشهنج اول حاکم ممالك بشمار است.
«یشتها اص ۱۷۹؛ بشتها اس 40 و۲۱۵». ۸ موف زغور اخبار ملوك الفرس دردیادشاهی حوشنگه»
کوید: ... ووضم قوانین ورسوم وبرقراری عدل بدومنسوب است وبهمین مناسبت به پیشداد ملقب
شده که بفارسی نختین واضم عبانی عدالت است.
۴۳ ح ‏ فش + راد» بعنی بیش داده :
ز بی حرص بخششی نکرده سژال بىایل دهد جود او پیش داد.
عجدی مروزی. «جپانگیری».
پشکش - بکر چهارم (در اهج؛ حر کزی) ازربشة پارسی باستان۵:5.ظ5 ۵2
(جل وکشیدن) ؛ حدیبه‌ای که بشخصی بزر کتر ندیم کنند .
##### leaf 669
۳و
فیشگاه « باکاف فارسی بروزن ثیرماه»
بیتی صدر- و صدر مجلس هردو آهده است -
وفرشی‌را نیز گوبند که‌درپیش افکنند. وفرش یکه
درپیش ابوان وصدر مجلس اندازند - و محرابب
مسجیرایز کوش ویادشاه وصاحب تخت ومسندوا
هم کنته‌انه ِ
پیشگاه نشور - کنابه از قيامت
باشد .
پیشگر - با کاف فارسی بروزن بیشتر »
خادم وخدمنکار ت ومددکار باشد 2
پیشگو- باکاف فارسی بر وزن نیکشو »
۴۹۳۳ را کونندکه در مجلس سلاطین و امرا
و اک بر صدارت شخصی کند 2 بایشان بشناسانف
و آن شخص رابعربی معرف خوانشد. و شخصي را
نیز کونند که مطاب مردم دا مرش سلاطین
میرساند» واو رادر هندوستان میرعرض ودر دکن
بخبردار گویند .
پیشگوی بروزن نیکخوی:» بمعتی
یو است که معرف باشد و شخصی که مطالب
کسی‌را بمرض سلاطین رساند .
)۱ چش : پازاح
پِشة آش
بشگه بروزت لیهژه » مضفف بیشگاه
است که هم صدر- وهم صدر مجلس- وهممحواب
مسجد باشد و فرشی‌را نیز گویند که دد پیش
آبوان وسدر مجلی اندازند-
شین خنح الث بروزن سجن , لیف
خرما را گوبند که ازآن رسن بتابند.
پیشن ه بر وزن ربونف » بمعلی پیشن
است که لیف خرما باشد واز آن رسن تابند.
پیش شیی - بکس نون پازاج (۱)را
کوبند که دابه و ماماچه باشد , و بعربی فابله
خوانند- وامر به‌پیش شستن هم هست.*
پیش | - با واو بالف کشیده » سر کرده
و پیش‌رو مردمان باشد و بعربی مقتدا گوشب -
ولوعی ازجامه هم هس ت که زنان بوشند .3
یاه بی وزن رشه » رسنی باشد که
آن را از لیف خرما تابند ‏ و با ثالی مجهول »
شفل وکار وعمل و کسب را گوند وبمربی حرفه
خوانند ۱ - و فسمی از نی ۲ باشد که شبانان
عم نوازند و آنرا توتك خوانند.
بشه آ تش کنابه از کارهای
(نی + چه) « از افادات علامه دهشدا» .
۴ - ظ . تشه
پیشنهاد خاطرم ابنکه هلا او شوم
تشنهٌ جام می روم شاید اکر سبو شوم .
باشرابط عمین ۲ گاهی میدهد. عرضه .
##### leaf 670
شطالی باشد .3
ی اد بایای حطی» بروزن وععنی
بیشکار است ت که خادم و خدستکار اک رد
ومزدور وش دست‌باشد ویمصی بیشاب و شاش
هم هست که بمربی بول گویند- و قاروره پیماررا
نیز گفته‌اند وآن شیشه‌ای باشد که بول بیمار را
درآن کنند و پیش طبیب برند » و بممنی آخر
بجای حرف آخر نون هم آمده است
پیشیاده - با ثالی مجپول بر وزن‌هیج
کاره؛ خواتجه وطبقی را گوبند که تعلات 4
در آن کنند و بمجلی آورند ٩‏ .#
بیفاد ه- باغن نقطه‌دار بروزن مخوارد:
طعنه وسرزنش وبهتان را گویند ۴ .
بغا له بر وزن بنگاله» قدح و کاسةٌ
را
هرزه هم آمده اس ۴ ۰
0 غلوش ه
کلی است‌از جنس سوسن و آنرا سوسن آسمان
کون خوانند و بر کنارهای آن خالهای سیاه
وچینهای کوچك افتاده است
دغله- ار وزن زنگله
چ‌
« بالام بروزن نیم جوش »
1 بمعنی کنج
و کوشةٌ خانه باشد - و کنج و كوشة چشم را لیز
گویند. وبمعنی براحه : دز آمده اسن که قض
راه باشد ٩‏ #
لماگنس بروزن هدن , سداب را گونند:
و آنگیاهی باشد دوابی مانند بودنه» و خوردن
11 ِِ_ قوت باه و یت ها و ی آن
۲ اول و ضم ثالث» بروزن
ومعنی پیکو باشد و آن ولامتی‌است مشهور- ونام
بیغان - بکر اول وثانی مجهول‌بروزن
ایمان» ترط و عهد وپیمان راکویند - و بممتی | هر که پادشاه آن ولابت شود ۸ - و بکر اول
ظ,. مصحف پیشپاره (معرب آن فیشفارج) . د: پیش باره .
؟ - اومتا821 1 ۵02 (حندی باستانی82 +۳261 آواز دادن» ملام دادن باسخ
دادن) . بارتي‌لمد صور کر اه این کلمهرا مشتق ازهندی باستان 12۳ +0221 ( 2۶ظ
فک رکردن) دانست. «اسشق ۳۵۸ راد: سفاره.
ی ۵ - مقلوپ : پلنوش (« .م).
٩‏ -همرثْهة بفوله . ۲ - جوالیقی کوید : «فال ابوبکر: الفیجن» السداب. لفة
شامية و لا احسبها عربية صحيحة. قال ابوبکر: و لااعلم للسداب اسماً عربباً لاهل الحجاز ۰ الا ان
اهل الیمن سمونه «الختف». «المعرب ص ٩۲4۲‏ . ۸ - عنوان جبفو باسفر ( که اغلب
بقلط بیغو وپیغونوتثه و خوانده میشود) بحکام خلخ اطلاق شده. ابن خردادبه (س ۱5) کوب د که
ملاطین ترك و تبت وخزر « حافان » خوانده میشوند « باستثنای پادشاه خرلخ که جبفوبه نامیده
میشود .» بقول کاشفری ]11 . ۲۵ یففو عنوانی بود دو درجه یابین‌تر از خاقان . عنوان ,بفو
0 ( کاغنری]]] .2]800:۳6از ۷2۳۵00) را بامد از نام قبلهباغو 72028۳00
تمیزداد. قببلهة اخبر درسمت شرقی‌ثر بن قای وتانار جا داشته‌اند (کاشفری آ .۲۸». برای اطلاعات
بیشتر" رك : : میلورسکی . حور العالم ص ۰۳۸۸
‌ پیشی - از: پیش اد ی (حصدری)؛ سبقت. . نقدم: : بیی گرفتن سیقت جستن؛ میتی
ریسی تقدم و تأخر: «پیدا کردن حال منقدمی ومتأخری که پیشی وپسی بود: پیشی ویسی ۳
بود بابطبع بود بابشرف بود...»
```


## [2026-09-07T20:47:58.185Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[669]\nprint(len(p))\nprint(p[2000:])\nEOF",
 "description": "Print rest of BQT leaf 669"
}
```


### [2026-09-07T20:47:59.632Z] TOOL RESULT

```
1528
```


## [2026-09-07T20:48:15.339Z] TOOL CALL #32: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py",
 "description": "Check fetch_source usage"
}
```


### [2026-09-07T20:48:15.374Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
"""
import sys, os, json, hashlib, re, html, time, urllib.request, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, "data", "verification", "sources", "web")
INDEX = os.path.join(WEB, "index.jsonl")
UA = "rishe-verification/1.0 (+https://github.com/sfmqrb/rishe; etymology source archiving)"


def html_to_text(s):
    s = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>|</tr>|</h[1-6]>", "\n", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n\n", s)
    return s.strip()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    note = ""
    if "--note" in sys.argv:
        note = sys.argv[sys.argv.index("--note") + 1]
        args = [a for a in args if a != note]
    if not args:
        print(__doc__); return 2
    url = args[0]
    h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]
    # IRI -> URI: percent-encode non-ASCII path/query characters so urllib accepts them
    parts = urllib.parse.urlsplit(url)
```


## [2026-09-07T20:48:21.863Z] TOOL CALL #33: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pey%E1%B8%B1-\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B4%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B3\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D9%88%D8%B4%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%A8%DB%8C%DA%AF\" \\\n \"https://www.etymonline.com/word/paint\" \\\n \"https://www.etymonline.com/word/file\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 386, root Peig, node verification\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-07T20:48:27.034Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pey%E1%B8%B1-
/home/sfmqrb/git/rishe/data/verification/sources/web/cdc1f536808ba51c.txt
### https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B4%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/b313bd5c3e906e1e.txt
### https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B3
/home/sfmqrb/git/rishe/data/verification/sources/web/1bbd135f6a0e50c7.txt
### https://en.wiktionary.org/wiki/%D9%86%D9%88%D8%B4%D8%AA%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/0ce8302405d24324.txt
### https://en.wiktionary.org/wiki/%D9%86%D8%A8%DB%8C%DA%AF
/home/sfmqrb/git/rishe/data/verification/sources/web/a45841c2094b5406.txt
### https://www.etymonline.com/word/paint
/home/sfmqrb/git/rishe/data/verification/sources/web/5d2ae2676d1f399f.txt
### https://www.etymonline.com/word/file
/home/sfmqrb/git/rishe/data/verification/sources/web/95f3ce3d9354c1b9.txt
```


## [2026-09-07T20:48:30.603Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in cdc1f536808ba51c b313bd5c3e906e1e 1bbd135f6a0e50c7; do echo \"##### $f\"; sed -n '1,400p' $f.txt | grep -n -A6 -i \"etymology\\|Descendants\\|Proto-Iranian\\|Avestan\" | head -60; done",
 "description": "Read wiktionary PIE and Persian pages"
}
```


### [2026-09-07T20:48:31.814Z] TOOL RESULT

```
##### cdc1f536808ba51c
68: Descendants 
69-
70- 1.1.3 
71: Descendants 
72-
73- 1.1.4 
74- See also 
75-
76- 1.1.5 
77- References 
--
168: Descendants
169- [ edit ] 
170-
171- Terms derived from the Proto-Indo-European root *peyḱ- (mark) (43 c, 0 e) 
172-
173- *péyḱ-t ~ *piḱ-ént ( root aorist ) [ 1 ] 
174- Proto-Indo-Iranian: 
--
180: ⇒ Proto-Germanic: *finhlōną ( see there for further descendants )
181-
182- Proto-Indo-Iranian: *pinášti 
183- Proto-Indo-Aryan: 
184- Sanskrit: पिंशति ( piṃśáti , “ to adorn; to mould, carve out, grind ” ) ( with thematicised weak stem ) 
185-
186: Proto-Iranian: *pinášti 
187- Old Persian: 𐎠𐎱𐎡𐎰 ( a-p-i-θ /⁠api⁽ⁿ⁾θaⁿ⁠/ , “ to cut, engrave, adorn ” , 3pl.impf. ) [ 6 ] 
188-
189: ⇒ Proto-Iranian: *nipinašti 
190- Old Persian: 𐎴𐎡𐎹𐎱𐎡𐎰𐎶 ( n-i-y-p-i-θ-m /⁠niyapiⁿθam⁠/ , “ to engrave, inscribe ” , 1sg.impf. ) [ 1 ] ( also interpreted as s-aorist /niyapaišam/ [ 6 ] ) 
191-
192- Proto-Italic: *pingō 
193: Latin: pingō ( “ to paint, color ” , with irregular - g - ) ( see there for further descendants )
194-
195- Proto-Tocharian: *pik- ( “ to paint, write, delineate ” ) [ 7 ] 
196- Tocharian A: pikiñc (< pik- ( “ to write ” ) )
197-
198- Tocharian B: piṅkäṃ (< pik- ( “ to write ” ) )
199-
--
202: Proto-Iranian: *páycati 
203: ⇒ Younger Avestan: 𐬀𐬧𐬐𐬎𐬞𐬀𐬉𐬯𐬆𐬨𐬥𐬀 ( aṇkupaēsəmna , “ to adorn ” , mid.ptc. ) 
204-
205- Middle Persian: 
206- Manichaean script: 𐫛𐫏𐫏𐫘𐫀𐫅 ( pyysʾd /⁠pēsād⁠/ , 3sg.subj. ) 
207-
208- *péyḱ-ye-ti ( ye-present ) [ 8 ] 
209- Proto-Balto-Slavic: *p(e)iś- ( possibly a later formation from intensive *pey-piḱ-yé-ti [ 1 ] ) 
--
214: Proto-Slavic: *pьsа̀ti ( “ to write ” ) ( see there for further descendants )
215-
216- *pe-póyḱ-e ~ *pe-piḱ-ḗr ( reduplicated stative ) 
217: ⇒ Proto-Brythonic: *gwrʉk ( see there for further descendants )
218-
219- *piḱ-ró-s [ 9 ] [ 10 ] 
220- Proto-Balto-Slavic: *piśras 
221: Proto-Slavic: *pь̀strъ ( “ variegated ” ) from an earlier **pь̀srъ ( see there for further descendants )
222-
223- Proto-Hellenic: *pikrós 
224- Ancient Greek: πῐκρός ( pĭkrós , “ sharp, pointed ” ) 
##### b313bd5c3e906e1e
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
71: Descendants 
72-
73- 1.4 
74- References 
75-
76- Toggle the table of contents 
77-
--
145: Etymology
146- [ edit ] 
147-
148: Inherited from Middle Persian pyšk' ( pēšag , “ trade, craft; guild ” ) , from Proto-Iranian *pais- ( “ to adorn, paint, write ” ) , from Proto-Indo-European *peyḱ- ( “ to mark, paint; spot, color ” ) . [ 1 ] [ 2 ] 
149-
150- Pronunciation
151- [ edit ] 
152-
153- ( Classical Persian ) IPA ( key ) : /peː.ˈʃa/ 
154-
--
197: Descendants
198- [ edit ] 
199-
200- → Azerbaijani: peşə 
201-
202- → Hindi: पेशा ( peśā ) 
203-
--
221: Persian terms derived from Proto-Iranian 
222- Persian terms derived from Proto-Indo-European 
223- Persian terms with IPA pronunciation 
224- Rhymes:Persian/a 
225- Rhymes:Persian/a/2 syllables 
226- Persian lemmas 
227- Persian nouns 
##### 1bbd135f6a0e50c7
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Adjective 
--
90: Etymology 
91-
92- 3.2 
93- Noun 
94-
95- 3.3 
96- Adjective 
--
102: Descendants 
103-
104- 3.4 
105- Further reading 
106-
107- 4 
108- Persian 
--
113: Etymology 
114-
115- 4.2 
116- Pronunciation 
117-
118- 4.3 
119- Noun 
--
128: Descendants 
129-
130- 4.7 
131- References 
132-
133- Toggle the table of contents 
134-
--
200: Etymology
201- [ edit ] 
202-
203- Compare Middle Persian [script needed] ( pys /⁠pēs⁠/ , “ mottled, leprous; leper ” ) . Ultimately from Proto-Indo-European *peyḱ- .
204-
205- Pronunciation
206- [ edit ] 
--
249: Etymology
250- [ edit ] 
251-
252- Borrowed from Persian پیس ( pis , “ leprosy ” ) , from Middle Persian [script needed] ( pys /⁠pēs⁠/ , “ mottled, leprous; leprosy ” ) .
253-
254- Noun
255- [ edit ] 
--
285: Descendants
286- [ edit ] 
287-
288- Turkish: pis
```


## [2026-09-07T20:48:43.195Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"##### noshtan\"; grep -n -B2 -A10 -i \"^ *Etymology$\" 0ce8302405d24324.txt | sed -n '1,80p'; echo \"##### nibig\"; grep -n -B2 -A12 -i \"^ *Etymology$\" a45841c2094b5406.txt | sed -n '1,60p'",
 "description": "Read wiktionary neveštan and nibīg"
}
```


### [2026-09-07T20:48:44.480Z] TOOL RESULT

```
##### noshtan
165- نبشتن ( nibištan  / nebeštan ) , نوستن ( nuwistan  / novestan ) , نویستن ( nawīstan  / navistan ) , نویشتن ( niwīštan  / nevištan ) 
166-
167: Etymology
168- [ edit ] 
169-
170- From Middle Persian npštn' ( nibištan , “ to write ” ) , from Proto-Indo-Iranian *ní ( “ downwards, into ” ) + Middle Persian *pištan- , the latter from Old Persian *pi⁽ⁿ⁾θ- , from Proto-Iranian *pais- ( “ to adorn, paint, write ” ) , from Proto-Indo-European *peyḱ- ( “ to cut out; to stitch; to paint, mark ” ) . [ 1 ] Doublet of نِبی ( nibī , “ scripture ” ) , and cognate with Russian написать ( napisatʹ , “ to write ” ) and English paint , picture . [ 2 ] 
171-
172- Pronunciation
173- [ edit ] 
174-
175- ( Classical Persian ) IPA ( key ) : /na.wiʃ.ˈtan/ , /ni.wiʃ.ˈtan/ 
176-
177- ( Dari, formal ) IPA ( key ) : [nä.wɪʃ.t̪ʰán] 
##### nibig
136- If it cannot be verified that this term meets our attestation criteria , it will be deleted. Feel free to edit this entry as normal, but do not remove {{ rfv }} until the request has been resolved.
137-
138: Etymology
139- [ edit ] 
140-
141- From Middle Persian nibeg ( “ book ” ) .
142-
143- Pronunciation
144- [ edit ] 
145-
146- ( Classical Persian ) IPA ( key ) : /ni.ˈbeːɡ/ 
147-
148- ( Dari, formal ) IPA ( key ) : [nɪ.beːɡ] 
149-
150- ( Dari, formal ) IPA ( key ) : [nɪ.beːɡ]
```


## [2026-09-07T20:48:54.097Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb && python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D9%86%D8%A8%DB%8C\" --note \"page 386, root Peig, node 5: Persian نبی 'book/Koran' from MP nibēg\" 2>&1 | tail -1",
 "description": "Archive wiktionary نبی"
}
```


## [2026-09-07T20:48:55.105Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SYN leaf for p.1284 (=leaf 1308)\"; awk 'BEGIN{RS=\"\\f\"} NR==1309{print substr($0,1,2000)}' SYN.txt",
 "description": "Print Buck p.1284"
}
```


### [2026-09-07T20:48:55.611Z] TOOL RESULT

```
python3: can't open file '/home/sfmqrb/tools/fetch_source.py': [Errno 2] No such file or directory
```


### [2026-09-07T20:48:56.822Z] TOOL RESULT

```
### SYN leaf for p.1284 (=leaf 1308)
�sound, well’ (4.83), this also esp. ‘sound in mind, sane’. Similarly poet. vé-sdnus.
Lat. dméns, déméns (less technical than insdnus), epds. of d- and dé- ‘away from’ (in cpds. often ‘without’) with méns ‘mind’.
It. pazzo, orig. a euphemistic term fr. Lat. patiéns ‘suffering’, in medicine ‘the patient’. REW 6292.
Fr. fou, see under ‘foolish’ (17.22, Lat. follis).
Sp. loco (Port. louco), orig. dub. REW 9038a.
Rum. nebun, lit. ‘not good’, neg. of bun ‘good’.
Rum. smintit, pple. of sminti ‘confuse, put in disorder, displace’, fr. Slavic, cf. ChSI. stimesti, -metq ‘confuse’. Tiktin 1446 f.
3. Ir. dasachtach (gl. amens Ml. 18213, freq. in older language; also as sb. ‘mad- man’), deriv. of ddsacht ‘madness, fury’ (16.43).
Ir. mer (cf. fear fris-a-r-heterscarad a chiall, in duine mear ‘a man from whom his sense has parted, the insane person’, Anc. Laws 5.234 bottom), NIr. mear ‘swift, sudden, lively, valiant, Joyous, giddy, raging, mad, wild’ (Dinneen), hence mire ‘madness’, and for ‘mad, in- sane’ usually NIr. ar mire lit. ‘on mad-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
a nt ew SEs
Digitized by Arya Samaj Foundation Chennai and eGangotri
1220 SELECTED INDO-EUROPEAN SYNONYMS
ness’; cf. Ir. meraige ‘idiot’, OBr. mergi- dhaam ‘je suis fou, stupide’, etym.? Loth, Voc. vieux-bret. 184f. (: Grk. poet. pdpyos ‘mad’),
NIr. (beside ar mire) also ar buile with buzle ‘frenzy, madness’ (also gen. as adj. fear buile ‘madman’, cf. Dinneen, s.v.), etym.?
W. gorffwyll, adj. and sb. ‘madness’, epd. of gor- ‘super’ and pwyll ‘wisdom, discretion, prudence, sense’ (: Ir. ciall ‘reason, sense’, 17.12).
W. gwallgof, old also sb. ‘madness’, epd. of gwall ‘defect, want’ and cof ‘memory, right mind, senses’ (17.31).
Br. foll, fr. Fr. fol. Loth, Mots lat. 169.
Br. diskiant, neg. cpd. of skiant ‘sense’ (fr. Lat. scientia ‘knowledge’).
4. Go
```


## [2026-09-07T20:49:03.610Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"18\\.5[0-9] *WRITE\\|WRITE$\\|WRITE \" SYN.txt | head -10; echo ===; grep -n \"^1284\\|1284 SELECTED\\| 1284 \" SYN.txt | head",
 "description": "Find Buck WRITE section"
}
```


### [2026-09-07T20:49:04.841Z] TOOL RESULT

```
Exit code 1
32310:18.51 WRITE
(eval):1: == not found
```


## [2026-09-07T20:49:08.575Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '32310,32330p' SYN.txt; echo \"--- surrounding page numbers ---\"; sed -n '32250,32312p' SYN.txt | grep -n \"12[0-9][0-9]\" ",
 "description": "Read Buck 18.51 WRITE"
}
```


### [2026-09-07T20:49:08.641Z] TOOL RESULT

```
18.51 WRITE
Grk. veeeu Goth. méljan Lith. radyti NG ypapw ON skrifa, rita Lett. rakstzt Lat.  scrtbere Dan. _ skrive ChSl. ptsatz It. scrivere Sw. skriva SCr. pisali Ir. écrire OE writan Boh.  psdtz Sp. escribir ME _urite Pol.  pisaé Rum. serie NE _urite Russ. pisat! Tr scribaim Du. schrijven Skt. likh- Nir.  scrtobhaim OHG - scriban, rizan OPers. ni-pis- W. ysgrifennu MHG schriben
Br. skriva NHG - schreiben
Writing as a record of speech had de- veloped in Egypt and western Asia as early as 4000 3.c., but was unknown in the place and time of IE unity. It spread from non-IE sources to the his- torical IE-speaking peoples. The ter- minology, however, is native IE, and in western Europe to a considerable extent of Latin origin.
The majority of the words for ‘write’, including Lat. scribere, which is the source of the western European words except the English, meant originally ‘scratch, cut, carve’, applicable to writ- ing on stone or wood or the later wax tablet. The Goth. méljan and the verb common to Slavic, Old Persian, and Tocharian (a notable and probably not accidental agreement) belong to groups which include verbs for ‘paint? (NHG malen and Lat. pingere), and one is tempted to assume the development ‘color, paint’ > ‘write’ as appropriate to writing on papyrus or parchment. This might apply to the Gothic and Slav- ic—and even to the Old Persian word if We assume that it was first used, not of the cuneiform (as in actual occurrence) but with reference to the contemporane- ous Aramaic script. Yet this is an un- Safe inference, since the groups in ques- tion cover other senses (as ‘mark, adorn’) from which ‘paint’ and ‘write��� may be derived independently.
1. Grk. yada, orig, ‘scratch, graze’ : OE ceorfan ‘cut, carve’, OHG kerban,
NHG kerben ‘notch, indent’, ete. Walde- P. 1.606 f.
2. Lat. scribere (> Romance words, also Ir. scrtbaim, NIr. scriobhaim, W. ysgrifennu, Br. skriva, ON skrifa, Dan. skrive, Sw. skriva, Du. schrijven, OHG scriban, MHG schriben, NHG schreiben, all ‘write’; but OE scrifan ‘decree, pass judgment, shrive’), Umbr. screhto ‘scrip- tum’, Ose. scriftas ‘scriptae’, etc. : Grk. oxapipdouat ‘scratch an outline, sketch’, ON hrifa ‘scratch’, Lett. scripat ‘notch, scratch’, fr. extensions of the root *sker- in OE, OHG sceran, Grk. xeipw, ete. ‘cut off, shear’. Walde-P. 2.586. Ernout-M. 91 f.
3. Goth. méljan (with sb. méla pl. ‘writing’) : OE mélan ‘mark, stain’, OHG malon ‘sketch, paint’ (NHG ma- len, etc.), ON mail ‘engraving (on a weap- on)’, OE mal ‘mark, sign’, OHG mal ‘sign, mark’, etc., fr. the same root as Grk. pédas ‘black’, Skt. malina- ‘dirty, black’, etc. Walde-P. 2.293. Feist 353 f.
ON rita, also ‘scratch, outline’, OE writan also ‘cut, engrave’, OHG rizan also ‘scratch, tear’ (NHG reissen), Goth. only writs, = xepata, ‘apex of a let- ter’, outside connections remote or dub., but semantic development fr. ‘scratch, cut’ clear. Walde-P. 1.287, 2.344. Falk- Torp 897. Feist 574.
4, Lith. ragyti, etym.? (Wiedemann, BB 28.59 : Lith. rézti, ChSl. rézati ‘cut’, but formal relation difficult).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
1284
Lett. raksttt, deriv. of raksts ‘writing’ (also ‘embroidery, pattern’); this prob. : Lith. rakstas ‘tomb’ (orig. ‘grave’), rakstis ‘splinter’, fr. the root of Lett. rakt ‘dig’, Lith. rakti ‘dig, rake’. Miihl.- Endz. 3.475.
5. ChSl. pisati, pisa, etc., general Slavic : OPruss. peisai ‘writes’, Lith. piesti ‘sketch, draw’, ON fa ‘color, adorn’ (fa riinar ‘write runes’), OE fag
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
‘colored, stained’, etc., Grk. srotxidos ‘gay-colored’, Skt. pig- ‘carve, prepare, adorn’, Av. pis- ‘color, adorn’, OPers. ni-pis- ‘write’, Lat. pingere (*peig- be- side *peik-) ‘embroider, paint’, Toch. ptk- ‘write, paint’ (SSS 451).
6. Skt. likh-, older rikh-, lit. ‘scratch, scrape’ : Grk. épelxw ‘rend, tear’, Lith. riekti ‘slice (bread)’. Walde-P. 2.344.
OPers. ni-pis- : ChSl. pisati (above, 5).
18.52 READ
--- surrounding page numbers ---
2:; READING AND WRITING 1281 in ChSl. préko ‘against’, prékosloviti and vit préko glagolati ‘speak against’.
28:1282 SELECTED INDO-EUROPEAN SYNONYMS
60:1283
```


## [2026-09-07T20:49:17.591Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SNS grep\"; grep -n \"pēs\\|pes\\b\\|nipēk\\|nipišt\\|nibišt\\|pišt\" SNS_pages.txt | head -20; echo \"### IEC peik\"; grep -n \"^peik\\|^peig\\|^pik-\\|^pinkt\\|peik-\" IEC.txt | head -15",
 "description": "Grep SNS and Mann"
}
```


### [2026-09-07T20:49:17.647Z] TOOL RESULT

```
### SNS grep
12122:                    tx£t4& tx&j&ij* :pes dared *»i£*nj yp                                                                     :<rdhybyd                       MiW.
15889:pes ud pas 143/2           pusih 138/19                      radSn 226/4            r€s 234/12
### IEC peik
12592:peigh- “marked, freckled; mark, birthmark, freckle'. Cf. peiK-, poiK-, poigh- Umb. peio- (queried: ‘brindled — of a pig"); MHG veige (o-gde) ‘marked for disaster, doomed’; OE (o-gde) fag *dappled'; fæge ‘fey, doomed'; Cz. piha, f. ‘freckle’; Li. cf. piegma, f. id.
12594:peik- (poik-, pik-) ‘sharp’ Alb. pikë, f. *point'; cf. pikllim, m. “bitterness, anger’; Gk. cf. pikrós ‘sharp, bitter; OHG cf. fehida, f. ‘feud, hostility ; Go. cf. bifaihón, ga-faihon, v. ‘overwhelm’; Li. peikiu, -ti, v. *upbraid'; peikiuos, -étis, v. ‘come to one's senses’; piktas, adj. “angry, malicious’
12595:peik- ‘mark, paint, draw, write’. Cf. poik-. Variant pink- OPer. -paišam, v. ‘write’; Oss. físsin, Dig. fin- sun, pp: fist, finst, id. Skt. cf. pinsámi ‘carve; decorate; write, paint’, pp: pisitah, pistáh; Tokh. A pek-, pik-, B paik-, pink- ‘write, paint’; Lat. cf. pingo, ére, id.; Mir cf. écor, adj. ‘adorning’; OCS piso, pisati, v. ‘carve, write’; R cf. pisà? kràskami ‘paint beside pisà? (and com. SI. ‘write’); Li. piešiu, -ti, v. ‘paint, draw’. Z-gde in Skt. pisáh, m. Cdeer, lit. *dappled"); Cz. pestrý, OCz. pstry ‘motley’. Cf. OE fina, wm. ‘woodpecker’?
12601:peik- (poik-, pik-) — peku
12867:pik-, pik- radical form of following entries, cf. pikolos, pikos, etc. Alb. pik, v. ‘drip; stab; embitter; pickle’; Li. pykà ‘anger’; pykstü, pýkti, v. ‘be angry; LW in Ir. pioc, pioch, m. ‘droplet; jot; pore & in Alb. pikë ‘point, dot, source of Fr. pique, fr. a Lat. type *picca. A type pīkāið arises in Alb. pikoj, v. ‘drip’; OCz. pikati, inf. ‘urinate’ and in OCS pikanina, pikotyna, f. “urine?
12886:pikið “mark, paint, adorn’. Cf. peik-, poiK-, piKtós. WP II, 9 Av. pis- ‘adorn’; Ober, ni-piš- “write down’; Per. na-vištan, inf. id.; OCS (and com. Sl.) pí39, pisati, v. ‘write, engrave’; isophonic: Li. pyštù, pišti, v. ‘get rusty’; pisüs, adj. ‘rusty
12907:(pink-, variant of type ping- (?), but cf. pik-, peik-, poik-) Tokh. B pink-, v. (write, paint'. Lat. pingo is ambig. as also Norw. Dong, adj. "elegant
13305:poikeið ‘paint, decorate’. See next and poi- Kos, and cf. peik- (pik-) OPer. cf. a-paišam 'I have written’; Tokh. B paik- ‘write’; MHG vehen, wv. tr. & intr. (1) ‘decorate, colour; become coloured"; Li. pai- šau, -yti, v. ‘draw, sketch"
13309:peik- (pik) and next Skt. pé$ah, m. 'ornament'; Av. paešō, m. id. (and ‘shape’); Ober cf. paisiya, f. ‘writing’; Oss. fes, s. (Tuck?. See note on poigh- "mark: Tokh. A cf. paik-, v. ‘write’; Gk. cf. poikilós ‘variegated’; Lat. picus, m. pica, f. (magpie; woodpecker’. Lit. ‘variegated or ‘pied’ bird"); Umb. peico, m., peica, f. as Lat., beside peica, adj. f. ‘brindled’; OS féh, MHG vech, gs: véhes, adj. ‘motley’; G cf. Feb, s. (“sable- skin’, lit. *mottled"); Go. cf. filu-fáihs, adj. *many-coloured'; Li. paiSas, paiSà, m. f. and -0s, fpl. ‘smudge, charcoal mark, blot’; cf. also piesà 'smut'; paisüs ‘smutty’. (OE fina, wm. *woodpecker' seems to represent a type *peiKno-)
```


## [2026-09-07T20:49:18.561Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KLN paint\"; grep -n \"^paint\\b\\|^picture\\|^pigment\\|^file\\b\" KLN_1966.txt | head -20",
 "description": "Grep Klein"
}
```


### [2026-09-07T20:49:18.612Z] TOOL RESULT

```
### KLN paint
14709:file,  n„  1)  a  collection  of  papers;  2)  a  line,  row.
14712:file,  n.,  a  tool  of  steel.  —  ME.  file,  fr.  OE.  feol, fit,  rel.  to  OS.,  OHG.  fila,  OSwed.  fit,  MDu., MHG.  vile,  Du.  vi/7,  G.  Feile,  and  prob.  cogn. with  OI.  pimsati,  ‘hews  out,  carves’,  L.  pingere, ‘to  paint’.  See  paint  and  cp.  words  there  re¬ ferred  to.
14714:file,  tr.  v„  to  make  foul,  to  defile  (archaic  or  dial.)
26946:paint,  tr.  and  intr.  v.  —  ME.  peynten,  painten,  fr. OF.  (=  F.)  peint,  pp.  of  peindre,  ‘to  paint’,  fr. L.  pictus,  pp.  of  pingere,  ‘to  paint,  embroider,’ fr.  I.-E.  base  *peig-,  ‘to  adorn  by  coloring  or carving’,  whence  also  OI.  piitgah,  pihgalah, ‘reddish’,  Toch.  A  pik-,  pek-,  B  pink,  paik-,  ‘to write’,  OSlav.  pigii,  ‘variegated’.  Fr.  *peik-,  a related  base,  derive  OI.  pesaldh,  ‘adorned,  dec¬ orated,  lovely’,  pesah,  ‘shape,  form’,  pimsati, ‘cuts,  carves,  adorns’,  Avestic  paes-,  ‘to  adorn’, Gk.  noiKtXo?,  ‘variegated’,  T-ixpoc,  ‘sharp, bitter’,  OHG.,  OS.  felt,  ‘variegated’,  ON.  fd, OHG.  fehjan,  ‘to  adorn’,  OE.  fah,  ‘variegated’, fagian,  ‘to  adorn’,  OSlav.  piSp,  pisati,  Lith. pieSiii,  pieSti,  ‘to  write’,  Lith.  pieSd,  ‘soot’, OSlav.  pistrii,  ‘variegated’,  pisu,  ‘dog’,  pistrogu, ‘trout’.  Cp.  depict,  picric,  pictorial,  picture,  pig¬ ment,  pint,  pinta,  pintado,  poecilo-.  Cp.  also  file, ‘fool’.
28805:pigment,  n.,  paint,  dye.  —  L.  pigmentum,  ‘col¬ oring  matter,  paint’,  from  the  stem  of  pingere,  ‘to paint’.  See  paint  and  -ment  and  cp.  pimento, pimiento  and  the  second  element  in  orpiment. Derivatives:  pigment,  tr.  and  intr.  v..  pigmentary (q.v.),  pigment-ation,  n.,  pigment-ize,  tr.  v. pigmentary,  adj.  —  L.  pigmentarius,  'pertaining to  paints’,  fr.  pigmentum.  See  prec.  word  and adj.  suff.  -ary. pigmy,  n.  —  See  pygmy.
```


## [2026-09-07T20:49:38.624Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('nleaves',len(pages))\nfor i in (283,284,285):\n    p=pages[i]\n    print('##### idx',i, p[:60].replace('\\n',' | '))\nEOF",
 "description": "Inspect BQT vol4 pages"
}
```


### [2026-09-07T20:49:39.957Z] TOOL RESULT

```
nleaves 553
##### idx 283 [pdf page 284] | ۱ بوشدارو | نوشن - بکسر اول و ثانی : معروف پیچی
##### idx 284 [pdf page 285] | بوشروان -۲۰۲-< | نوشروان - مخفت بوشیروان‌است.۱ 
##### idx 285 [pdf page 286] | ده وخ | خوردن وتیمارداشتن‌هم هست۱ - وقوی وقزح ۲
```


## [2026-09-07T20:49:46.188Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[283])\nEOF",
 "description": "Print BQT printed page 2201"
}
```


### [2026-09-07T20:49:47.478Z] TOOL RESULT

```
[pdf page 284]
۱ بوشدارو
نوشن - بکسر اول و ثانی : معروف پیچیده ودرلوردیدء باشد 8 .
است که چیزی نوشتن وکتابت کردن باشد ۱ ؛ نوش خور .> بروزن موش خور » نام
و بنم اول هم بنظرآمده است - ویفتح اودوئالی | روز پنجم است از ماههای ملکی.
بمعنی‌درلوردیدن وطی کردن وییچیدن باشد ؟ - نوشدارو - نرباق رپازمرراگوند ‎٩‏
‏و بر وزن دوختن» بمعنی نوشیدن و آخامیدن و ای تر باق وپازهررا
باشد ۴ . ۱ - و یکی‌ازنامهای شراب است ۷ ؛ وبعتی گوبند
نوشته - بکراول وتانی, بممنی کتابت ! نوغداروکنایه ازشراب است - و لام معجونی هم
کرده شده و رقم نموده ۴ - وبفتح اول » بمعنی هت ۸.
۹ نیشن * بیعتن » پپلوی 21015۳8188 (- 81885 ) ( تحریر کردن ) » پارسی
باستان -0215 ۳ 38 (نوشتن) «بارتولمه۸۱۷» «لیب رکه *۱۹*. درپارسی باستان/[83019101822,
هندی باستان-086. 0186411 فقط بمعنی‌آراستن وزبنت دادن است , اسلاوی کلیایی 81921,
استی 10890 , 51888 , 818 گنه ( نوشته » خط ) . بلوجی ع 2101928 » وخی و شغنی
و سریکلی م 86۷1912820 . رك : اسشق ۱*۵۱ ؛ کردی 8۷1918 ( تحربر ) «ژایا س 4۲۹*.
واه لپشتن با نوشتن چندین بار در سنگه‌لیشته‌های هخامنشیان بکار رفته است, مرکب است ازدو
جزه : لخت لی 8 جزئی ( پرفیکس » پیشاوند ) است بمعنی فرود و پایین که درسرلغات بهقتن
ونهادن وشتن و بمیاری ازلغات دیگر فارسمی هم دیده میشود. دوم از ربشةٌ 0218 درپارسی‌باستان
و 2269 دراوستا که بمعنی نگاشتن و نگاریدن و نفش کردن است . ازهمین بنیاد است عقاوم
که در پهلوی بممنی نش ونگار بسته وزینت شدماست؛ ودر قارسی «پیسه» شدء بمعی ابلق ودو
رنگه فاب‌اص ۰۱۱۳ ۴ بوردیدن (وم.)- نوردن (.م.)
۴ - باین هعنی « نوشیتن > ر4 : نوشیدن . ۴ - اسم مفعول از « فوشتن >
( یکر واو)-
8 - اسم مقعول از نوشتن ( بفتح واو). ‎٩‏ از : نوی ۳ دارو ؛ پهلوی<[8283
( کسیر » نوشدارو ) « منای ۲۹۹ و رك : نوش . ۷ - رك : رشیدی .
۸ - فردوسی در داستان جنکه رستم و سهراب وکشته شدن سهراب آردکه چون رستم
داست سهراب فرزند اوست که بدست وی هجروح کردیده »
بگودرز کفت آن زمان پپلوان که ای کرد با نام روشن روان
پیامی از امن سوی کاوی بر بگوش که ما را چه‌آمد بس
بدشنه چگرگاه یور دلیر دریدم که رستم مناد دی
گرت هیچ باد است کردار من یکی رنجه کن دل به نیمار من
ازآن نوشدار و که د رکنج تست کجا ختگان راکند تن‌درست
بنزديك من با یکی جام می مسزدکر فرستی هماکنون زیی-
بیامد اسپهید بکردار باد بکاروی بکسر پیامش بداد.
بدو کفت کاوس کز پیلتن کرا بیشترآب تزديك من ۲...
ولیکن اگر داروی نوش من دهم , زنده ماند پل پیلتن ۰
کند پست رستم بنیرو ترا هلاك‌آورد بی کمان مرمرا ...
فردوسی طوسی « شاهنامةٌ بخ ج اس ۹-۹۹۸
- ولف در فپرست خاهنامه » نوشدارو را به 3215278 ( بلسان ) ترجمه کرده است .
```


## [2026-09-07T20:50:06.149Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### ARY latin index peis/pais\"; grep -n -i \"PEIK\\|PEIG\\|PAIS\\|PES\\b\" incoming/ARY/ARY_latin_index_pages.txt | head -20",
 "description": "Grep Aryanpur latin index"
}
```


### [2026-09-07T20:50:06.199Z] TOOL RESULT

```
### ARY latin index peis/pais
976:OTL AF rapes OLY abst y tr GEL] Ge ar OWIly go y alps F
1237:eel PES yy jhe jie gal yo oF aa
1394:OPES VY 9 VY (2S): abi olny UGNIS -(LITHUANIAN) gly)
1626:via Lopes Kags ODDF (WELSH) 535
1818:capes wiedt Egat
2430:pleegl glaagl b 25 go wells cal.» 4eT STABULUM 2 503!) 5 "Sant pes asta
4192:HOLD CHURCH $PAVIC) 345 539-1 PES, PEDIS LATIN) 3
4825:PAIS, PAUROS GREEK) Sip.
4941:AY topes Baas HOLD ENGLISH) pS g=3Si\
5330:TEMPORA —:(PORTUGUESE) gt TAPES GREEK) gin
7235:Pes sor | OY
7379:Wer. types Bad WOS {OLD ENGLISH) oS gS:
8917:POKORNY = SSSOS*~«*CTS VOLPES MATIN) ga 4
9685:tt Lopes Kia VIVER (PORTUGUESE) Jlis
10412:YAAY y NAVA Lopes Sead SLAUNIS (OLD PRUSSIAN) 5 3. ah
10774:wer sbi oly (PAISIBLE, HEUREUX) 226
13702:Ford topes Sag OLD ENGLISH) oS podSit
```


## [2026-09-07T20:50:07.225Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### ARY pisheh\"; grep -n \"پیشه\\|پیسه\\|نوشتن\" incoming/ARY/ARY_pages.txt | head -20",
 "description": "Grep Aryanpur Persian"
}
```


### [2026-09-07T20:50:07.273Z] TOOL RESULT

```
### ARY pisheh
11786:۳ البته ان واژه در فارسی امروز به چم "عمل" و "پیشه" و "کردار" بکار می‌رود.
```


## [2026-09-07T20:50:15.115Z] TOOL CALL #46: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%D9%BE%DB%8C%D8%B3%D9%87/\" \"https://abadis.ir/fatofa/%D9%86%D8%A8%DB%8C/\" ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 386 root Peig: Mo'in (MON) entry via abadis\" 2>&1 | tail -1; done",
 "description": "Fetch Mo'in entries via abadis"
}
```


## [2026-09-07T20:50:16.370Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"نبیگ\\|نبی\\b\" MON_part2.txt | head -10; echo \"### part1\"; grep -n \"پیسه\" MON_part1.txt MON_part2.txt | head -10",
 "description": "Grep Mo'in local OCR"
}
```


### [2026-09-07T20:50:19.566Z] TOOL RESULT

```
### https://abadis.ir/fatofa/%D9%BE%DB%8C%D8%B3%D9%87/
/home/sfmqrb/git/rishe/data/verification/sources/web/7a39bb0dbd504986.txt
### https://abadis.ir/fatofa/%D9%86%D8%A8%DB%8C/
/home/sfmqrb/git/rishe/data/verification/sources/web/52c0e0779e9046e5.txt
```


### [2026-09-07T20:50:19.629Z] TOOL RESULT

```
1129:غرد: 2 [ع.] (.) خانه نبین و خانة مسقف 
1360:غرنبیدن: 0-- ۲۵۲۵۸۲۰ (مص‌ل.) (غر نسد» 
1361:غرنبد» خواهد غرنبید. بغرنب» غرنبنده» 
1362:غرنبان» غرنبیده» غرنبش» ضربنه). آواز در 
1535:بیگانه؛ اجنبی؛ مق. آشناه خودی. 
3642:() بیگانه. اجنبی+ مق. خودی. (تص 
3825:مایة رشکك. جنبیدن غیرت کسی: به غیرت 
3843:شخحص دیگی دیگری. بیگانه» اجنبی ؛ مق. 
4777:بد بر د. ۳ سالخو ردد. دار فانبی: ( کد.) جهان 
6193:شحص. نوه. نبیر ه۲ ج ج. فررزندزادگان. 
### part1
MON_part1.txt:6178:منتلا باشد» بر ص‌داره پیس» پیسه» پیس‌اندام» 
MON_part1.txt:10150:ارثم: (ع.] (ص.) مار پیسه؛ مار سیاه 
MON_part1.txt:34583:پیس: :۲ [- پیست - پیسه - پیسی] (ا.) 
MON_part1.txt:34585:(ص.) (بز.) ابررص؛ پیسه» میروص» مبتلا به 
MON_part1.txt:34634:پیسه: (6-)0152 [نگاشتن» نقش کردن» نقش 
MON_part1.txt:34641:فارسی است.) پیسه چرم: چرم دو رنگ» 
MON_part1.txt:34644:آمده. پیسه کمیت: نوعی اسب که سیاه و 
MON_part1.txt:34645:سفید باشد. رسن پیسه: ریسمان سیاه و سفید. 
MON_part1.txt:34647:است. غنح پیسه: جوال دو رنگ. مار پیسه: 
MON_part2.txt:24486:کلاییسه: (م-)2ع]15-0ه [- کلاغ‌پیسه]
```


## [2026-09-07T20:50:23.150Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '34580,34650p' MON_part1.txt; echo \"### پیشه in MON\"; grep -n \"^پیشه:\" MON_part1.txt | head",
 "description": "Read Mo'in پیس/پیسه entries"
}
```


### [2026-09-07T20:50:23.236Z] TOOL RESULT

```
۳۸۹ 


پیس: :۲ [- پیست - پیسه - پیسی] (ا.) 
(پز.) مرضی است جلدی» پیسی» برص. 
(ص.) (بز.) ابررص؛ پیسه» میروص» مبتلا به 
بررص. (.) دو رنگ. ابلق. 
پیس: ۲:6۶ (1.) (نم.) نمایشنامه. ضح.- عدم 
استعمال این کلمة بیگانه اولی استا. 
پی‌سپار: -06۲۰ ,۳21-56۳3 [< یی‌سپار نده] 
(ص‌فا.) رونده» راهرو. 
پسی سپر: 6 ,۳۵۷6۳۸۲ [- پی‌سپار ] [- 
بی سیر نده] (ص‌فا.) رونده» سالک بی سپار . 
به پای سیرنده» به زیر با گیرنده» بامال 
کننده. [- پی‌سپرده] (ص‌مف.) لگدکوب» 
بی‌سیار» بایمال» بای کوب. 
پسی سیید. -.[06 ,۳2۲-9600 [- بی‌سفید ] 
(ص‌مر.) شوم قدم؛ نامبار کث. 

پیست: ا:آ0 (- پیس] (.) شخص مبتلا به 
برصء ابر ص» پیس. 
پیست. ۱ (.) محوطه با میدان آماده 
برای ورزش مسابقه» رقص؛ تاختگاه (فره.) 
پیستودن: «ماعام (فز.) استوانه متحرکی که 
با اصطکاک در لول تلمبه پا سیلندر ماشین 
بخار حرکت کند. تکمةٌ فنری» دکمهٌ فشاری. 
کسی که از شخصی جانبداری کند؛ حامی» 
پارتی (در فرانسوی به معنی سفارش و 
توصیه است.) (مکن.) در اتومبیل لولةً فلزی 
توپری است داخل لولةٌ دیگری بنام سیلندر 
که در نتیجةٌ انفجار گاز مترا کم (مخلوط گاز 
هوا و بنزین) در ناحیة سر سیلندر (قسمت 
فوقانی پیستون) بستون در داخل سیلندرها 
شدیداً حرکت کند و این حرکت به وسیله 
آلت دیگری بنام دستة پیستون به میل‌لنگ 
نتقل شود و بالاخره رفت و آسد آن به 
حرکت دورانی میل‌لنک تبدبل گردد. دستة 
پیستون: (مکد.) در اتومبیل میلٌ آهنی است 
که به پیستون متصل است و به وسيلة آن 
حرکت رفت و آمد پیستون را به میل‌لنگک 


منتقل می‌سازد. این حرکت رفت و آمد در 
داخل لولةً سیلندر به نوبةٌ خود به حرکت 
دورانی میللنگ تبدیل می‌گردد. 

پیس سا ۷ 7 «-01 (مص‌ل.) دو رنگ 
شدن, ابلق گشتن» خلنگ گردیدن. به 
بیماری برص مبتلا شدن. 

یسی سفیك: -۳۵۷۰ ,5۵)10-(0۸ [< بسی سییك | 
(ص‌مر.) شوم قدم» نامبار کك» بی سیید. 
بدبخت» بدطا 

پیسه: (6-)0152 [نگاشتن» نقش کردن» نقش 
و نگار سته» ز ینت شده. قص. ابر ص؛ هندیا. 
آرایش و زینت] (ص.) سیاه و سپید بهم 
آمیخته, ابلق» دورنگك. ( کد.) دورو منافق. 
(بز.) مرضی است جلدی» پبسی» بر ص. 
(ص.) مبتلا به بر ص» مبر و ص» پیس. (.) زر 
نقد (بدین معنی مشترک میان هندی و 
فارسی است.) پیسه چرم: چرم دو رنگ» 
بوست الق ستور. ضح. در دیوان 
مسنئو چهر ی د. چا. ۲ ۴ ۱ «بسه چر مه») 
آمده. پیسه کمیت: نوعی اسب که سیاه و 
سفید باشد. رسن پیسه: ریسمان سیاه و سفید. 
سباه (سیه) پسه: آنکه یک رنگک او ساه 
است. غنح پیسه: جوال دو رنگ. مار پیسه: 
مار دو رنکک» ارقم. 

پیسی: آ-:آ (حامص.) (پز.) ناخوشیی 
### پیشه in MON
35292:پیشه: (0-):013 (۱.) صنعت. حر فه. ضسح.-
```


## [2026-09-07T20:50:31.260Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '35290,35300p' MON_part1.txt; echo \"### نبی MON_part2\"; grep -n \"^نبی\\|نبی:\" MON_part2.txt | head; echo \"### نوشتن\"; grep -n \"^نوشتن:\\|نوشتن:\" MON_part2.txt | head",
 "description": "Read Mo'in پیشه, نبی, نوشتن"
}
```


### [2026-09-07T20:50:31.350Z] TOOL RESULT

```
تصرفی در معنی از کت 

پیشه: (0-):013 (۱.) صنعت. حر فه. ضسح.- 
فرهنگستان این کلمه را به معنی «کسب و 
حرفه» بذیرفته. شغل» کار» عمل. عادت» 
خوی. 

تیه | (168-)2۱25-. (ص‌مر.) ( کد.) 
کار شیطان» کار شیطانی. 

پیشه گانی: ار (حامص.) بیشه‌وری. 
### نبی MON_part2
4777:بد بر د. ۳ سالخو ردد. دار فانبی: ( کد.) جهان 
47062:متنبی: ۱0۵0۸0201 [ع.] (افا.) مردی که 
74212:نبی؟ پیغچبری. حضرت نبوی: محمد (ص) 
74227:نبی: (7۵[09 [ع. نبیٌ] (ص. .) پیغامبر؛ 
74231:نبی: (قد. 6-)]۱00 ,[ع [نو شته» نامه (۲)] 
74234:نبی خوال: ۰.20 (- نبی خواننده] (ص‌فا.) 
74243:نبید: 074« |- نوید ] (ا.) میزدگانی» نوید. 
74251:نبیر ۵: (۵-)7۸01۳۸ [- نسر ] (.) فر زندراده؛ 
74261:نبیسه. (ه-)«دآناد۱ [ - نواسه ‏ نواسی - نیسه 
74263:نبیل: ار [ع.] (ص.) هو شبار» تبرخاطره 
### نوشتن
49750:رسمی؛ ج. محاضر. محضر بر آب نوشتن: 
80915:نوشتن: [- نبشتن > نوردیدن - 
80918:نوشتن: ۱۳۷۵۹ [ < بیشتن < نیشتن ] 
93139:کنند. یادگاری نوشتن: نوشتن خط و جمله یا 
93547:اثر سرما. بر یخ نوشتن: نابود انگاشتن؛ به
```


## [2026-09-07T20:50:34.643Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '74227,74245p' MON_part2.txt; echo \"###\"; sed -n '80913,80925p' MON_part2.txt",
 "description": "Read Mo'in نبی and نوشتن"
}
```


### [2026-09-07T20:50:34.733Z] TOOL RESULT

```
نبی: (7۵[09 [ع. نبیٌ] (ص. .) پیغامبر؛ 
پیغمی) رسول؟ ج. انبیاء. محمد(ص) بن 
عدالله. (اختصاصا). 

نبی: (قد. 6-)]۱00 ,[ع [نو شته» نامه (۲)] 
ا.) قرآن مجید. 

نبی خوال: ۰.20 (- نبی خواننده] (ص‌فا.) 


فر هنک فارسی معین 


۹ ۱ 
خوانندة قرآن, قاری قرآن. 

نبید: 074« |- نوید ] (ا.) میزدگانی» نوید. 
نید خوار: ]۱2۱ [- نسد (نسد) 
خوارنده| (ص‌فا.) شر اب‌خوار؛ میکسار. 
###
التحر بر . 

نوشتن: [- نبشتن > نوردیدن - 
نوردن ] (مص م.) (نوشت» نوردد» خواهد 
نوشت بنورد» نوردنده؛ نوشته) نوردیدن. 
نوشتن: ۱۳۷۵۹ [ < بیشتن < نیشتن ] 
(مصم.) (نوشت» نویسد» خواهد نوشت» 
بنویس» نویسنده؛ نویساء نوشته) اندیشه و 
مطلبی را به وسیلةٌ مداد یا قلم به روی کاغذ 
آوردن» کتابت کردن» تحر بر کر دن. 
نوشته: (0-)۱۵۷25-12 (امف.) نوردیده» طی 
سل ۵.
```


## [2026-09-07T20:50:54.878Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb && ls site/pages/386.jpg 2>/dev/null; ls data/verification/sources/refs/ocr/ 2>/dev/null | head",
 "description": "Check page image availability"
}
```


### [2026-09-07T20:50:56.114Z] TOOL RESULT

```
BOOK
```


## [2026-09-07T20:51:00.964Z] TOOL CALL #52: Bash

```json
{
 "command": "pdftoppm -f 386 -l 386 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg386 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg386.png",
 "description": "Render PDF page 386"
}
```


### [2026-09-07T20:51:02.717Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 60779 Sep  7 16:51 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg386.png
```


## [2026-09-07T20:51:07.427Z] TOOL CALL #53: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg386.png"
}
```


### [2026-09-07T20:51:07.773Z] TOOL RESULT

```

```


## [2026-09-07T20:51:07.765Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T20:51:23.337Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### WLD Bd2 p.9 (leaf 14)\"; awk 'BEGIN{RS=\"\\f\"} NR==14{print substr($0,1,2500)}' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "Print Walde-Pokorny II p.9"
}
```


## [2026-09-07T20:51:24.120Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### UNV nipek\"; grep -n \"nipek\\|nipēk\\|nipist\\|nipišt\\|Buch\" UNV.txt | head -20",
 "description": "Grep Unvala"
}
```


### [2026-09-07T20:51:24.657Z] TOOL RESULT

```
### WLD Bd2 p.9 (leaf 14)
                                              pi   — peig- und peik                                   9


urgr. "^Tiev-ia die Gdf., die dann (vgl.  Falk-Torp u. hunger mit Bed.-Par-
allelen)  an nevia ^jArmut^^, nevYjg „arm, diirftig^^ nhofxai „habe Mangel;
rniilie mich; erarbeite miihsam^^ anzuschliefien ist; s. iiber diese Gruppe

u. s})en „ziehen, spannen^^     Zu einem Wzansatz pc\iy und Verkniipfung
mit den unter pei- „schinahen“ zsgestellten Worten unter einer Urbed.
,,feindselig in Taten und Worten     liegt kein AnlaB vor.
   Verfehlt ist Perssons Beitr. 821 Deutung von lat. parvtis aus verwandtem
 pd-ru-os (s. "^pon- „klein^^).

pM-, pT j^schmahen*^.
     Ai. piyati „schniaht, hohnt^^, pnyaha-j plyd- „schniahend, hohnend'^ (? aus
p^yciti^             piyaru-       ('^pl-ani-')    j,schmahend, hohnend, ubelwollend"^,             iit-

plp-lU, -ana-h; got. fainn „tadeln“ {p^id)\ germ, "^fije-n in got. fijan, -a\da^
aisL         feon^ ahd./v^^? j,hassen“, got, fijands^ ahd.       usw. ,,Feind“.
     Schulze KZ. 27, 426, Persson Beitr. 698, Falk-Torp u. ficnde (m. weiterer
Lit.).    Gegen Yerb. mit pc- „weh tun^^ s. d,
l.   peig-    und peik „farbeln, mit schwarzer oder anderer Farbe malen,
        bunt, farbig^ (daneben Y^orte                fiir   „stechen^).
   A. Ai. pmkte (unbel.) „malt^‘, pmga-j pmgald- „r6tlich braun“, pihjdra-
„r6tlich,  rotgelb, goldfarben^; gr. myyakog (Hes.) „Eidechse^^, niyyav'
vEoaoiov. IrijuEQiag ykavxov Hes.; lat. pingo, -ere, pinxi,^ pictum „malen   mit                ;


derlfadelsticken^, /}/c^or„Maler^; (fernzuhalten mir.           nir.    „ Lacks
da nicht aus "^peigno- Stokes KZ. 41, 385), abg. peg^b „bunt"^.              Mit            —
anderer Bed. (s. u.) will Osthoff MU. IV, 326 ai. pinja ,.das Wehtun, ver-
letzen^^ anreihen(?).    IJber dt. Fink s. u. "^spingo- „Sperling, Fink“.
   B. Ai. pisdti „haut aus (bes. Fleisch), schneidet zurecht, gestaltet, bildet
(s. u.), schmuckt,    ziert^^,       n., pcradi m.     „ Gestalt, Form, Farbe
pecald- „verziert; lieblich; geschickt**^; pi^dioga- „r6tlich, rotbraun“, pi^d-h
m. ^Damhirsch^^ puplarn „h6lzernes GefaB, Napf^ (wenn „ausgeschnitztes^^?
                      ;


Petersson IF. 24, 266)
  Av. pacs- „farbig machen, schmiicken^^, pacsa- m. pacsah-                         n.   „Schmuck,
Zierat^^, ap. nipistanaiy „schreiben“.
     Gr. TtoiyJkog ,.bunt“     ;
```


### [2026-09-07T20:51:24.699Z] TOOL RESULT

```
### UNV nipek
65:16.  Für  die  Textgestaltung  verweise  ich  auf  die  mit  arabischen Ziffern  bezeichneten  Noten.  Nur  Änderungen  bezüglich  der  Izäfat  ^ und  der  Kopulativpartikel  i,  die  beide  ebenso  oft  vergessen  als  über¬ flüssig  gesetzt  sind,  habe  ich  in  den  Noten  nicht  besonders  erwäbnt; überschüssige  sind  einfach  mit  (  ),  fehlende,  und  darum  von  mir  er¬ gänzte,  mit  [  ]  eingeschlossen.  Ferner  finden  sich  in  jenen  Noten  Be¬ merkungen  zu  seltenen  Wörtern  und  zu  graphischen  Eigentümlichkeiten. Alle  mit  Buchstaben  bezeichneten  Noten  beziehen  sich  auf  die  Exegese.
1085:estäi  nipist  ängön  nipeJc  pa  us  108.
```


## [2026-09-07T20:51:34.562Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nip\\|pes\\b\\|pēs\" SNS.txt | head -30; echo \"### leaves\"; python3 -c \"\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nprint('leaves',t.count(chr(12)))\"",
 "description": "Grep SNS glossary"
}
```


### [2026-09-07T20:51:35.896Z] TOOL RESULT

```
16776:.y/\ 9 *S .±i*+, tx£t4& tx&j&ij* :pes dared : *»i£*nj yp 
31500:pes ud pas 143/2 
### leaves
leaves 242
```


## [2026-09-07T20:51:45.620Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"PAIŠ\\|\\*PAIS\\|nibēg\\|nibištan\\|nibišt\" CHEUNG.txt | head -20",
 "description": "Grep Cheung for *paiš"
}
```


### [2026-09-07T20:51:45.697Z] TOOL RESULT

```
6566:goes possibly back to the substantive YAv. fiianhu-. It could be related to *paiš 
19175:*pais 291 
19188:*pais ‘to adorn, paint; to write’ 
19237:292 *pais 
19240:(Kurm.) ävitin, etc., may have two different origins, viz. *pai$ and *pais, but not 
19265:*pais ‘to crush, grind’ 
19283:verb may have two different origins, viz. *pais and *pais, but not from *(H)uaij, 
55119:*Hraz (s.v.), *iat (s.v.), *pais, 
55617:*namH, *pais (s.v.), *skard 
55988:*baH (s.v.), *pais (s.v.), 
56039:*huar’, *kar (s.v.), *pais 
56178:*marH' , *pais, *uraiH, 
56764:*draus, *HarH, *pais 
57330:*huar’, *pais 
58420:*pais
```


## [2026-09-07T20:51:48.813Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19185,19262p' CHEUNG.txt",
 "description": "Read Cheung *pais entry"
}
```


### [2026-09-07T20:51:48.859Z] TOOL RESULT

```
*REFERENCES: Abaev, Slovar’ I: 201 


*pais ‘to adorn, paint; to write’ 

*AVESTAN: YAv. paés- ‘to adorn’ || (+ *fra-) ‘to embellish’ = Liste: 34f. 

Partic.: pres. them. YAv. anku.paésomna- (Yt 17.10), perf. pass. YAv. frapixsta- (Yt 14.27) 

*OLD PERSIAN: рї??Ө- ‘to cut, engrave, adorn’ || (+ *ni-) ‘to engrave, inscribe’ 
= Kent: 194 

Pres. them. / n-: impf. IND. 3pl. api(")0a" <a-p-i-9> (DSf 54); Aor. s- IND. lsg. niyapaisam 
«n-i-y-p-i-0-m» (DB 4.71); Partic.: perf. pass. nipista- <n-i-p-i-8-t-> (DB 4.47), <[n]-[i]-p-i-8-t-> (DSe 
52, XV 22, XPh 31); Inf: nipistanaiy <n-i-p-i-S-t-n-i-y> (XV 24); Pass.: impf. IND. 35р. "niyapiOiya 
<n-i-y-p-i-[0]-i-[y]> (РВ 4.91 |) 

*MIDDLE PERSIAN: MMP pyys-, BMP pys- /pes-/ ‘to adorn, colour’ || (+ *ni-) MMP 
nbys-, BMP nps- /nibis-/ ‘to write, copy a book = DMMPP: 291b, 239b 

Pres.: SUBJ. 3sg. MMP pyys’d; Partic.: perf. pass. BMP pysyt /pésid/ ‘(-)coloured’ || (+ *ni-) Pres.: IND. 
35р. MMP nbysyd; Partic.: pres. MMP nbys’g’n (pl.), perf. pass. BMP npstk /nibistag/; Inf.: BMP npstn 
/nibistan/; Pass.: IND. 3sg. MMP nbyst, BMP npst /nibist/, 3р1. MMP nbystynd 

*PARTHIAN: (+ *ni-) nbys- ‘to write’ = Ghilain: 61 | DMMPP: 239b 

Pres.: IND. 35р. nbysyd, SUBJ. 15р. “nbys’n, 1р1. nbys’m, IMPV. 2pl. nbysyd; Partic.: perf. pass. nbyst, 
nbystg; Inf.: nbystn 

*KHOTANESE: pisaa- ‘painter’, pisa- ‘artistic work, painting’ 

*SOGDIAN: (+ *ni-) SSogd. np(’)ys, BSogd. np ys, CSogd. npys, MSogd. npys ‘to 
write (down)’ 

Well attested: Pres.: OPT. 2sg. SSogd. “np’ysy, SSogd. npysy, SSogd. np’y’sy, IMPV. 25р. SSogd. пру”, 
SSogd. “np’ys, etc. 

*CHORESMIAN: (+ *ni-) m/nps- ‘to write” = Samadi: 131 

*BACTRIAN: (+ *ni-) vaßıo- ‘to write, describe, state (in writing)’ = S-W, Bact.: 
207a 

*NWIR: (+ *4-) Kurd. (Kurm.) 4vitin, ауёіп/ауё(2)-, (Sor.) havistin/havez-, 
havitin/hav- ‘to compose (a song); to change (colour); to cultivate (a garden)’ || 
Widely attested: (+ *ni-) NP nivistan/nivés-, Kurd. (Kurm.) nivis-/nivisin, (Sor.) 
nus-/nusin, Zaz. nustis/nusen-, Awrom. nıwistay/-nıwis-, Abz. nevesta/neves-, 
Abyan. nömüsta/nömüs- (-m- < ?) Anar. niviste/ nvis, Fariz. nevist-, Gz. 
nevis-/nevist, Gil. (Rsht.) nivistoen/nivis-, Gur. (Kand.) nüwis-, Khuns. nevis-/nevist, 
Meim. bem-neveft/a-nevi:s-, Qohr. nüsta/nüs-, Semn. -nävistä-, Siv. nivis-/nivist, 
Tr. nevesta/nves- ‘to write’. © On account of the wide-ranging meanings Kurd. 


292 *pais 


(Kurm.) ävitin, etc., may have two different origins, viz. *pai$ and *pais, but not 
from *(H)uaij, Y Av. vij- ‘to shake, swing ?' (pace Cabolov 2001, ibid.). 

*NEIR: Oss. I. fyssyn/fyst, D. finsun/finst, Orosh. pis- ‘to write’, (?) Pash. pez-/pez- 
‘to darn’ (with unexplained -z-) || (+ *ni-) Yi. nuvíš-/nuüxt, M. nuvüs-/nuvüxt-, 
nuvisk’-, Yghn. nipíš-, nëpíš-/nipíšta ‘to write’ 

*MISC: Orm. pis-/pistak ‘to write’ 

*SANSKRIT: pes ‘to adorn, hew out, carve (out), form, decorate’ (RV) = EWAia П: 
168 

«PIE *peik- ‘to paint, adorn’ => LIV: 465 f. | Pok.: 794 f. 

*IE COGNATES: Lat. pingö ‘I paint’, Toch. A pik-, B pink- ‘to write, paint’, OCS 
ppsati ‘to write’, Lith. piésti ‘to draw lines, draw, adorn’, Gr. лоікілос 


‘multicoloured, coloured, stitched with many colours’, OHG féh ‘multicoloured’ 
*REFERENCES: КРЕТ. 209b; Ivanow 1926: 421; HFL I: 405a; КРЕП: 224; Christensen, Contributions I: 
76, 174; IIFL II: 234a; Lambton 1938: 43a; Abaev, Slovar' I: 501 f.; Andreev — PeSéereva: 294a; 
MacKenzie 1966: 103; WIM I: 71; WIM II/1: 80; DKS: 241b; WIM III: 113; Cabolov 1997: 72; Werba 
1997: 357; Paul 1998: 307b; Cabolov 2001: 96 £; Lecoq 2002: 121, 123, 126 (passim); NEVP: 68.
```


## [2026-09-07T20:52:06.074Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb && python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/nib%C4%93g\" --note \"page 386 node 4: Middle Persian nibēg 'book' etymology\" 2>&1 | tail -1",
 "description": "Fetch Wiktionary MP nibēg"
}
```


### [2026-09-07T20:52:07.349Z] TOOL RESULT

```
python3: can't open file '/home/sfmqrb/tools/fetch_source.py': [Errno 2] No such file or directory
```


## [2026-09-07T20:52:10.625Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/nib%C4%93g\" --note \"page 386 node 4: Middle Persian nibeg 'book' etymology\" 2>&1 | tail -1",
 "description": "Fetch Wiktionary MP nibeg"
}
```


### [2026-09-07T20:52:48.183Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9e89ecf9cd22dc76.txt
```


## [2026-09-07T20:52:51.169Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -A8 -i \"etymology\" 9e89ecf9cd22dc76.txt | sed -n '1,40p'",
 "description": "Read Wiktionary nibeg"
}
```


### [2026-09-07T20:52:51.222Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:53:02.933Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in [2749,3130,5258]:\n    pos=sum(len(l)+1 for l in lines[:target-1])\n    leaf=t.count('\\f',0,pos)\n    print(target,'leaf',leaf,'printed~',leaf-8)\nEOF\necho \"### NYB pesak\"; grep -n \"pēšak\\|pesak\\|pēšag\" NYB_vol2_glossary.txt | head; echo \"### NYB nipistan entry\"; grep -n \"^nipištan\\|^nipist\" NYB_vol2_glossary.txt | head",
 "description": "Nyberg page numbers and pēšak"
}
```


### [2026-09-07T20:53:04.341Z] TOOL RESULT

```
2749 leaf 156 printed~ 148
3130 leaf 176 printed~ 168
5258 leaf 274 printed~ 266
### NYB pesak
3134:pēšak [pyšk'] class, profession 55°. 581%, 664. 109%, — Paz. peša; NP pēšah; from the same stem as Av. (908) pištra- in the same sense.
3135:pēšak-kār [py3k°l] craftsman, pl. cas. obl. n-ān 8117-19, — Paz. pēšagar, Skr. v. vid yavant.
6772:agar: pēšakkār pēšavāē: pēšēpāi pēšiār: pēšārvār pēšīnaga: pēšēnīk phālum: pahlom pīm: pēm pradim: fratom puh(a)l: puhl pulādīn: pēlāvatēn pur: purr pursīdan: pursītan puštaspān: puštēpān
7327:pēšah: pēšak
### NYB nipistan entry
2752:nipistan [npštn'; YKTYBWN-tn'] nipés- to write 419. 110? etc. ; nipist estet it has been written, it is written 1139; nipist ēstāt it was written 1!—?; — pres. pass. nipēsihēt [YKTYBWN-yhyt'] is being written 18%; — pat dp i zarr nipištak 1079; apar nipistak written down 108?!; nāmak ~ 6 to write a letter to 49-9. 822, an inscription P 2:3.4; apar fravartak čton nipišt estat kū it was written in the letter (then dir. speech) 1872; apar én ayyätkär nipišt estet 1135-9. — OP ni-pais- ; MPrthPrs nbyštn nbys-; Paz. nawaštan nivés-; NP nuvistan, nivištan, nivés-.
```


## [2026-09-07T20:53:20.067Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor fn,offs,targets in [('HRN.txt',21,[3341,9099]),('HUB.txt',10,[7542,8439]),('IEC.txt',None,[12886,12595]),('KLN_1966.txt',None,[26946,14712]),('SYN.txt',None,[32310])]:\n    t=open(fn,encoding='utf-8',errors='replace').read()\n    lines=t.split('\\n')\n    for tg in targets:\n        pos=sum(len(l)+1 for l in lines[:tg-1])\n        leaf=t.count('\\f',0,pos)\n        print(fn,tg,'leaf',leaf,'printed~', (leaf-offs) if offs else '?')\nEOF",
 "description": "Compute leaves for citations"
}
```


### [2026-09-07T20:53:21.433Z] TOOL RESULT

```
HRN.txt 3341 leaf 100 printed~ 79
HRN.txt 9099 leaf 256 printed~ 235
HUB.txt 7542 leaf 222 printed~ 212
HUB.txt 8439 leaf 246 printed~ 236
IEC.txt 12886 leaf 520 printed~ ?
IEC.txt 12595 leaf 507 printed~ ?
KLN_1966.txt 26946 leaf 594 printed~ ?
KLN_1966.txt 14712 leaf 320 printed~ ?
SYN.txt 32310 leaf 1376 printed~ ?
```


## [2026-09-07T20:53:51.214Z] TOOL CALL #64: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-07T20:53:51.253Z] TOOL RESULT

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


## [2026-09-07T20:53:56.921Z] TOOL CALL #65: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg386.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/386.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/386.png",
 "description": "Copy page image for audit"
}
```


### [2026-09-07T20:53:57.000Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 60779 Sep  7 16:53 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/386.png
```


## [2026-09-07T20:59:45.217Z] TOOL CALL #66: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-386.json",
 "content": "{\n  \"pdf_page\": 386,\n  \"book_page\": 356,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Peig\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *peyḱ- (older notation *peik- / *peig-) 'to mark by incision, cut, paint, make coloured'\",\n      \"note\": \"Pokorny IEW 794-795 has the lemma 'peig-1 und peik-' with the gloss 'kennzeichnen, durch Einritzen oder Färben' (the OCR of the English database dump renders it 'coloured, speckled'), and its material list is exactly the material Nourai charts: Skt. piṃśáti / péśas-, Av. paēs-, paēsa-, OP nipištanaiy, Lat. pingere, Gk. poikílos / pikrós, Goth. filu-faihs, OHG fēh, Lith. piešti 'paint, write', OCS pisati 'write'. Watkins/AHD glosses the same root 'peig-1. Also peik-. To cut, mark (by incision)' — literally Nourai's 'to mark'. The 'Indo-European' language label and the gloss are therefore right. The only thing to update is the shape of the reconstruction: because Skt. has ś and Balto-Slavic ś/s, the final consonant is a palatal, so modern handbooks (LIV 465f., Wiktionary, Cheung 2007) write *peyḱ-; the by-form with -g- that Nourai's headword 'Peig' preserves is nothing but the irregular -g- of Latin pingō (Buck: '*peig- beside *peik-'). Nourai's own reference POK:794 is the standard reference for this root. The empty box drawn to the right of the Old Persian node on the printed page carries no words and is not a node.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *peyḱ- «نشان زدن، خراشیدن، نگاشتن، رنگ کردن» (پوکورنی، ص ۷۹۴–۷۹۵، مدخل peig-1 و peik-؛ واتکینز/AHD: «بریدن، با خراش نشان گذاردن»). برچسب زبانی «هندواروپایی» و معنای «to mark» که نورایی آورده درست است. تنها نکته آن است که به گواهی ś سنسکریت (piṃśáti) و s/ś زبان‌های بالتی–اسلاوی، همخوان پایانی کامی (palatal) بوده و پژوهش امروزی آن را *peyḱ- می‌نویسد؛ صورت با g که در سرواژهٔ «Peig» بازمانده تنها بازتاب g بی‌قاعدهٔ لاتینی pingō است. ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pey%E1%B8%B1-\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:794\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt line 65001: 'Root / lemma: peig-1 and peik- … Meaning: coloured, speckled … Avestan paēs- \\\"make colorful, adorn, decorate\\\", paēsa- m. paēsah- n. \\\"jewellery, decoration\\\", Old pers. nipišta- \\\"written down\\\" … Latin pingo, -ere … Page(s): 794-795.' Nourai's page number is exact.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"AHD\",\n          \"where\": \"AHD_watkins1985.txt line 824 (Watkins 1985, s.v. peig-1)\",\n          \"stance\": \"supports\",\n          \"note\": \"'peig-1. Also peik-. To cut, mark (by incision). 1. Alternate form *peik- in Germanic *fihala, cutting tool, in Old English fīl, file: FILE. 2. Nasalized zero-grade form *pi-n-g- in Latin pingere … PAINT, PICTOR, PICTURE … PIGMENT … [Pok. 1. peig- 794.]' — the gloss 'to mark' and the two western branches Nourai charts.\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. II p. 9 (WLD_Bd2_pages.txt leaf 14)\",\n          \"stance\": \"supports\",\n          \"note\": \"'1. peig- und peik- \\\"färben, mit schwarzer oder anderer Farbe malen, bunt, farbig\\\" … Av. paēs- \\\"farbig machen, schmücken\\\", paēsa- m. paēsah- n. \\\"Schmuck, Zierat\\\", ap. nipistanaiy \\\"schreiben\\\".' Pokorny 794 cites exactly this page ('WP. II 9 f.').\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, IEC.txt line 12595 (leaf 507, ≈ col. 984) and line 12886 (leaf 520, ≈ col. 1010)\",\n          \"stance\": \"supports\",\n          \"note\": \"'peik- \\\"mark, paint, draw, write\\\". Cf. poik-. Variant pink- OPer. -paišam, v. \\\"write\\\" …' and 'pikiō \\\"mark, paint, adorn\\\" … WP II, 9 Av. piš- \\\"adorn\\\"; OPer. ni-piš- \\\"write down\\\"; Per. na-vištan, inf. id.; OCS pišǫ, pisati, v. \\\"write\\\".'\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck 18.51 WRITE, p. 1284 (SYN.txt line 32310 ff.)\",\n          \"stance\": \"supports\",\n          \"note\": \"'ChSl. pisati … Skt. piś- \\\"carve, prepare, adorn\\\", Av. piš- \\\"color, adorn\\\", OPers. ni-pis- \\\"write\\\", Lat. pingere (*peig- beside *peik-) \\\"embroider, paint\\\", Toch. pik- \\\"write, paint\\\".' Buck writes the root with -g- exactly as Nourai's headword does.\"\n        },\n        {\n          \"src\": \"CHEUNG\",\n          \"where\": \"Etymological Dictionary of the Iranian Verb, s.v. *pais, pp. 291-292 (CHEUNG.txt line 19188 ff.)\",\n          \"stance\": \"supports\",\n          \"note\": \"'*pais \\\"to adorn, paint; to write\\\" … «PIE *peik- \\\"to paint, adorn\\\" => LIV: 465 f. | Pok.: 794 f.'\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"paes, paeš; paěsah, pištra\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Bartholomae AiW col. 817-818 has the verb 'paēs-, p. paiš- V. \\\"farbig machen; zieren\\\"', i.e. Young Avestan paēs- 'to make coloured, to adorn' (participle *pišta-, *pixšta-, e.g. fra-pixšta- 'decorated', Yt 14.27), which continues PIE *peyḱ- with the regular Iranian outcome ḱ > s (Av. -aē- < PIE *-ey-). From the same verb Bartholomae lists the two nouns Nourai puts in the second line: paēsah- n. 'Schmuck, Zierrat' (AiW 818) and paēsa- m. 'Schmuck, Zierrat' (F 10), and pištra- n. 'Stand, Kaste' — the four Avestan estates, 'Priester, Krieger, Bauer, Handwerker' (Y 19.17) — formed with the *-tra- instrument suffix on the zero grade *piš- and explained by Bartholomae as literally 'Färbung, Farbe' (cf. Skt. péśas- n.), whence the sense 'the class/occupation one is marked with'. Two of Nourai's English glosses are looser than the sources: paēsah- is 'ornament, adornment' rather than the adjective 'decorated', and pištra- is 'class, caste, profession' (Horn: 'Gewerbe') rather than 'skilled' — he is glossing them ahead towards the New Persian meanings in node #2. The derivations themselves and the language label are right.\",\n          \"derivation_fa\": \"در اوستایی ستاک فعلی paēs- / paiš- «رنگین کردن، آراستن» (بارتولمه، ستون ۸۱۷) بازماندهٔ ریشهٔ هندواروپایی *peyḱ- است؛ ḱ کامی هندواروپایی در ایرانی باستان به s بدل شده و *ey به aē اوستایی. از همین ستاک است paēsah- (خنثی) و paēsa- (مذکر) «زیور، آرایه» و نیز pištra- «طبقه، پیشه» (اوستا، یسنا ۱۹/۱۷: چهار طبقهٔ موبد، ارتشتار، برزگر و پیشه‌ور) که با پسوند ابزارساز *-tra- بر پایهٔ درجهٔ صفر *piš- ساخته شده و بارتولمه معنای نخستین آن را «رنگ، نشان» می‌داند. دو معنایی که نورایی به دست داده اندکی سست است: paēsah- «زیور» است نه «آراسته»، و pištra- «طبقه/پیشه» است نه «ماهر»؛ او معنا را از پیش به سوی «پیشه»ٔ فارسی نو کشانده است. با این همه، خودِ اشتقاق درست و پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pey%E1%B8%B1-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:794\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt line 65001 ff.: 'Avestan paēs- \\\"make colorful, adorn, decorate\\\", paēsa- m. paēsati- n. \\\"jewellery, decoration\\\", Old pers. nipišta- \\\"written down\\\", Avestan fra-pixšta- \\\"decorated\\\".'\"\n            },\n            {\n              \"ref\": \"SYN:1284\",\n              \"status\": \"supports\",\n              \"note\": \"Buck 18.51 WRITE, p. 1284: 'Skt. piś- \\\"carve, prepare, adorn\\\", Av. pis- \\\"color, adorn\\\", OPers. ni-pis- \\\"write\\\" …' (SYN.txt line 32310 block).\"\n            },\n            {\n              \"ref\": \"SNS:143\",\n              \"status\": \"not_found\",\n              \"note\": \"Tavoosi's Šāyast nē Šāyast glossary is on disk only as unusable OCR (SNS.txt / SNS_pages.txt, 242 leaves, no readable printed page numbers). grep for 'pes', 'pēs', 'nip', 'pišt' returns only two hits, both the unrelated pēš 'before' ('pes dared', 'pes ud pas 143/2'). Page 143 could not be located.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae AiW col. 817-818 (BRT.txt lines 14803-14812)\",\n              \"stance\": \"supports\",\n              \"note\": \"'paēs-, p. paiš- V. \\\"farbig machen; zieren\\\" … PPfP. pišta-, pixšta- … mit fra \\\"verzieren\\\": barət kanəm frapixštəm Yt 14.27'; 'paēsa- m. \\\"Schmuck, Zierrat\\\" … Zum V. paēs-. — ai. péśa- m.; np. vgl. pēsa \\\"Scheckkuh\\\"'; 'paēsah- n. \\\"Schmuck, Zierrat?\\\" … Zum V. paēs-. — ai. péśas- n.'\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae AiW s.v. pištra- (BRT.txt line 16412)\",\n              \"stance\": \"supports\",\n              \"note\": \"'pištra- n. \\\"Stand, Kaste\\\" … Priester, Krieger, Bauer, Handwerker (Y 19.17) … Zum V. paēs-, eig. \\\"Färbung, Farbe\\\"; vgl. ai. péśas-. — np. vgl. pēša \\\"Handwerk, Gewerbe\\\". — Vw.: pēšak.' Bartholomae glosses it 'estate, caste', not 'skilled'.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"s.v. *pais, p. 291 (CHEUNG.txt line 19188 ff.)\",\n              \"stance\": \"supports\",\n              \"note\": \"'*AVESTAN: YAv. paēs- \\\"to adorn\\\" || (+ *fra-) \\\"to embellish\\\" … Partic.: pres. them. YAv. aŋku.paēsəmna- (Yt 17.10), perf. pass. YAv. frapixšta- (Yt 14.27).'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II p. 9\",\n              \"stance\": \"supports\",\n              \"note\": \"'Av. paēs- \\\"farbig machen, schmücken\\\", paēsa- m. paēsah- n. \\\"Schmuck, Zierat\\\".'\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"pîseh «پیسه»; pîsî «پیسی»; pîšeh «پیشه»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Two different Avestan formations feed this box. (a) پیسه pīse 'piebald, black-and-white' and پیسی pīsī 'vitiligo/leprosy' go back to Av. paēsa-, which Bartholomae lists twice — as 'Schmuck, Zierrat' and, probably the same word, as an adjective 'aussätzig' / noun 'Aussatz' (Yt 5.92, V 2.29) — with the explicit continuation 'mp. (Pü.), np. pīs'. The Middle Persian form is MacKenzie's pēs [pys] 'mottled, leprous; leper' beside the verb pēsīdan, pēs- 'colour, adorn'; MP ē regularly gives NP ī (pēs > pīs), and the -a/-ī suffixes give the adjective پیسه and the abstract/disease noun پیسی. (b) پیشه pīše 'craft, trade, occupation' is not from paēsa- but from Av. pištra- 'estate, occupation' through MP pēšag [pyšk'] 'trade, craft; guild, caste' — Nyberg says so in as many words, and Horn no. 357 does too; the cluster -štr- gives Middle Persian -š- with the -ag suffix, and MP -ag > NP -a/-e. Mo'in's footnote in Borhan-e Qāte' p. 440 attaches پیسه directly to OIran. paēs- 'to write, to figure, to decorate' and derives پیسی 'what the Arabs call baraṣ' from it, which is Nourai's claim verbatim. The Sa'di line quoted on the page (هر پیسه گمان مبر که خالی است / باشد که پلنگ خفته باشد) uses پیسه in the 'dappled' sense.\",\n          \"derivation_fa\": \"این خانه در حقیقت دو اشتقاق جدا را در بر دارد. نخست «پیسه» و «پیسی»: از اوستایی paēsa- که بارتولمه هم «زیور» و هم صفت «پیس، جذامی» و اسم «پیسی» (یشت ۵/۹۲، وندیداد ۲/۲۹) معنی کرده و خود می‌افزاید «مپ. (پهلوی)، فارسی نو pīs»؛ صورت فارسی میانه pēs «دورنگ، پیس» است (مکنزی) در کنار فعل pēsīdan «رنگ کردن، آراستن». ای کشیدهٔ فارسی میانه در فارسی نو به ای بدل شده (pēs > پیس) و با پسوندهای ـه و ـی «پیسه» و «پیسی» ساخته شده است. دوم «پیشه»: این یکی از paēsa- نیست، بلکه از اوستایی pištra- «طبقه، پیشه» از راه فارسی میانهٔ pēšag [pyšk'] «حرفه، صنف» می‌آید؛ نیبرگ (ص ۱۶۸) و هرن (شمارهٔ ۳۵۷، ص ۸۰) هر دو همین را می‌گویند. حاشیهٔ معین بر برهان قاطع (ص ۴۴۰) نیز «پیسه» را به paēsa- و «پیسی» را به همان بیماری برص بازمی‌گرداند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B3\",\n            \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B4%D9%87\",\n            \"https://abadis.ir/fatofa/%D9%BE%DB%8C%D8%B3%D9%87/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:440, 443\",\n              \"status\": \"supports\",\n              \"note\": \"BQT_v1_pages.txt leaf 666 = printed p. 440 (vol. 1) carries the entry پیسه and Mo'in's footnote 4: «در پارسی باستان paēs و در اوستا paēsa بمعنی نگاشتن و نگاریدن و نقش کردن است. از همین بنیاد است paēsa که در پهلوی بمعنی نقش و نگار بسته و زینت شده است و در پارسی پیسه شده بمعنی ابلق و دورنگ: سفید و سیاه. پیسی که در تازی برص گویند نام بیماری است که تن از نشان‌های سیاه و سپید دورنگ گردد» (with «بارتولمه ۸۱۷» «نیبرگ ۱۸۱، ۱۹۰»). Leaf 669 = printed p. 443 carries پیشه: «شغل و کار و عمل و کسب را گویند و بعربی حرفه خوانند»; the OCR of that page's footnote 1 is lost, so only the headword and gloss could be read there.\"\n            },\n            {\n              \"ref\": \"MON:904\",\n              \"status\": \"partial\",\n              \"note\": \"The 6-volume Amir Kabir Mo'in that Nourai paginates is not on disk; the 2-volume Adena reprint is (MON_part1.txt line 34634): «پیسه: (paēsa-) [نگاشتن، نقش کردن، نقش و نگار بسته، زینت شده. قص. ابرص؛ هندی: آرایش و زینت] (ص.) سیاه و سپید بهم آمیخته، ابلق، دورنگ … (پز.) مرضی است جلدی، پیسی، برص» and line 35292 «پیشه: (pēšag) (ا.) صنعت، حرفه». The content is exactly what Nourai cites; the page number could not be checked against the edition he used.\"\n            },\n            {\n              \"ref\": \"HRN:80\",\n              \"status\": \"supports\",\n              \"note\": \"HRN.txt leaf 102 = printed p. 80, entry '357. پیشه pīše \\\"Handwerk, Gewerbe\\\". aw. vergl. pištra- \\\"Gewerbe\\\"; phlv. pēsak.' (Horn's neighbouring entry 355, p. 79, is 'pēs \\\"Aussatz\\\", pēst \\\"leprös\\\", pēsī, pēse \\\"Schecke\\\" … aw. paēsa- \\\"aussätzig\\\" … phlv. pēs \\\"Aussatz\\\", pēsīt \\\"geschmückt\\\"; ai. péśas- \\\"Schmuck, Zierrat\\\"'.)\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD p. 68 area (PHD.txt leaf 549, s.vv. pēs, pēsīdan, pēšag)\",\n              \"stance\": \"supports\",\n              \"note\": \"'pēs [pys | N ~] mottled, leprous; leper. pēsīdan, pēs- [pys-ytn'] colour, adorn. ~išn: adornment.' and '1pēšag [pyšk' | N pēša] trade, craft; guild, caste.' MacKenzie's own New-Persian equivalents are پیس and پیشه.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II, pp. 168 (NYB_vol2_glossary.txt lines 3130, 3134)\",\n              \"stance\": \"supports\",\n              \"note\": \"'pēsīt [pysyt'] adorned … Derived from Av. (818) paēsa- \\\"ornament\\\", from Av. (817) paēs-, OP pais-, v. nipištan.' and 'pēšak [pyšk'] class, profession … Paz. pēša; NP pēšah; from the same stem as Av. (908) pištra- in the same sense.' — the second is the exact route Nourai draws for پیشه.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien §101, p. 212 (HUB.txt line 7542)\",\n              \"stance\": \"supports\",\n              \"note\": \"'pēs \\\"Aussatz, aussätzig\\\" JRAS. 1894, 451 = zd. paēsa-' — listed among the cases where Old Iranian ś appears as New Persian s.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae AiW col. 818 s.v. 2paēsa- (BRT.txt lines 14810-14811)\",\n              \"stance\": \"supports\",\n              \"note\": \"'paēsa- 1) Adj. \\\"aussätzig\\\" … 2) m. \\\"Aussatz\\\" … Vgl. 1paēsa-, womit das Wort vll. identisch ist. — mp. (Pü.), np. pīs.'\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Fārsi via abadis.ir, s.v. پیسه\",\n              \"stance\": \"supports\",\n              \"note\": \"Mo'in's entry gives the origin tag paēsa- with the bracketed sense «نگاشتن، نقش کردن، نقش و نگار بسته، زینت شده» and the meanings «سیاه و سپید بهم آمیخته، ابلق» and «(پز.) مرضی است جلدی، پیسی، برص».\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e Riše-hā-ye Hend-o-Orupāyi (incoming/ARY/ARY_pages.txt, ARY_latin_index_pages.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep for پیسه, پیشه, نوشتن in the Persian scan and for PEIK/PEIG/PAIS in the Latin index returns no headword; the OCR of this scan is too poor to use for this root.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"ni-pais\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The prefixed verb *ni-paiš- 'to write down' (literally 'to incise downwards', ni- 'down' + paiš- 'mark, incise, adorn') is Nourai's link between the ornament sense and the writing sense, and that link is standard: Buck (p. 1284) lists 'OPers. ni-pis- \\\"write\\\"' with ChSl. pisati under the same root, and Walde-Pokorny II 9 has 'ap. nipistanaiy \\\"schreiben\\\"'. The semantic step 'incise/colour' > 'write' is what Buck discusses on that very page ('the development \\\"color, paint\\\" > \\\"write\\\" as appropriate to writing on papyrus or parchment', or on the Aramaic script contemporary with the cuneiform). The reservation is the language label: the compound is attested only in Old Persian (niyapaišam DB 4.71, nipištanaiy XV 24, nipišta- DB 4.41 etc.), never in Avestan. Bartholomae prints 'mit ni \\\"nieder-, aufschreiben\\\"' inside the Avestan article paēs- but every passage he quotes there is Old Persian (Bh. 4.71, Bh. 4.8, X. 7.3), and Cheung lists the ni- compound under Old Persian only. So the box should read 'Old Persian' alone; as drawn it duplicates node #6 with a different transcription of the same verb (pais- vs. paith-).\",\n          \"derivation_fa\": \"فعل پیشوندی *ni-paiš- «فرونگاشتن، نوشتن» (پیشوند ni- «فرود» + ستاک paiš- «نشان زدن، نگاشتن») همان حلقه‌ای است که معنای «آراستن/نقش کردن» را به «نوشتن» می‌رساند و این پیوند در همهٔ منابع پذیرفته است: باک (ص ۱۲۸۴) «OPers. ni-pis- to write» و والده–پوکورنی (ج ۲ ص ۹) «ap. nipistanaiy schreiben». تحول معنایی «خراشیدن/رنگ زدن ← نوشتن» را نیز باک در همان صفحه شرح می‌دهد. تنها ایراد، برچسب زبانی است: این ترکیب فقط در پارسی باستان گواهی شده است (niyapaišam در بیستون ۴/۷۱، nipištanaiy، nipišta-) و در اوستا نیامده؛ بارتولمه هرچند آن را زیر مدخل اوستایی paēs- آورده، همهٔ شاهدهایش هخامنشی است. پس «اوستایی/پارسی باستان» باید تنها «پارسی باستان» باشد و این خانه در واقع همان خانهٔ ۶ است با آوانگاری دیگر. ادعای نورایی با این احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pey%E1%B8%B1-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:794\",\n              \"status\": \"partial\",\n              \"note\": \"POK_full.txt line 65001 block gives only the participle 'Old pers. nipišta- \\\"written down\\\"' — the root and the writing sense are there, but Pokorny lists no Avestan ni-compound.\"\n            },\n            {\n              \"ref\": \"SYN:1284\",\n              \"status\": \"supports\",\n              \"note\": \"Buck 18.51 WRITE p. 1284, paragraph 5: 'ChSl. pisati … Av. pis- \\\"color, adorn\\\", OPers. ni-pis- \\\"write\\\", Lat. pingere (*peig- beside *peik-) …' and, at the head of the table, 'OPers. ni-pis-' as the Old Persian word for 'write'. Buck labels it Old Persian, not Avestan.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae AiW col. 817 (BRT.txt line 14805)\",\n              \"stance\": \"partial\",\n              \"note\": \"'mit ni \\\"nieder-, aufschreiben\\\": dipim … tyām adam niyapišam Bh. 4.71; … naiy nipištam avahyarādiy naiy nipištam Bh. 4.8; … dipim naiy nipištām akunauš X. 7.3.' The compound is printed under the Avestan verb but all citations are Achaemenid Old Persian.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II p. 9\",\n              \"stance\": \"supports\",\n              \"note\": \"'ap. nipistanaiy \\\"schreiben\\\"' listed directly after Av. paēs-, paēsa-, paēsah-.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"s.v. *pais, p. 291\",\n              \"stance\": \"partial\",\n              \"note\": \"Cheung puts the ni- compound under '*OLD PERSIAN: pai(n)θ- \\\"to cut, engrave, adorn\\\" || (+ *ni-) \\\"to engrave, inscribe\\\" = Kent: 194'; under Avestan he records only the simplex and fra-pixšta-. No Avestan *ni-paēs-.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"nipištan; nibištan; nipěk, niběg\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The verb is beyond doubt: Book Pahlavi npštn' / nibištan, present nibēs- (MacKenzie CPD s.v.; the ideogram is KTYBWN-stn' from Aramaic ktb), Manichaean and Parthian nbyštn, nbys-, all from Old Persian ni-paiθ- with the *-ta- participle *ni-pišta- (PIE *piḱ-to- > pIran. *pišta-, Kent §93). The variation nipištan ~ nibištan is the ordinary Middle Persian lenition of intervocalic/post-nasal p to b, and both spellings are quoted by Nyberg and MacKenzie. The noun is the doubtful item. MacKenzie prints 'nibēg [npyk' | N niwē] writing, scripture, book' with no etymology, and Bartholomae (MirM IV 30 n. 2) took it as *ni-paiθa-ka- > *nipēhak > nipēk, i.e. from the same root as nibištan — which is what Nourai's arrow says. Nyberg, however, rejects that explicitly: 'nipēk … < *ni-pāya-ka- \\\"that which is kept, or is to be kept, in safe custody\\\", \\\"record\\\", originally an administrative term … From Av. ni-pāy- (pres. also pāy-). — Bthl's etymology: nipēk < *nipēhak < *ni-paiθa-ka- from a SW form of nipištan (MirM IV, 30, n. 2) is untenable.' Since the two derivations are still in competition and no later handbook settles it, the node as a whole is plausible rather than confirmed: the verbs are confirmed, the book-word is contested.\",\n          \"derivation_fa\": \"دربارهٔ فعل تردیدی نیست: پهلوی کتابی npštn' / nibištan با ستاک حال nibēs- (مکنزی؛ هزوارش KTYBWN-stn' از آرامی ktb)، پهلوی اشکانی و مانوی nbyštn، nbys-، همه از پارسی باستان ni-paiθ- با اسم مفعول *ni-pišta- (از *piḱ-to- هندواروپایی). دوگانگی nipištan/nibištan همان نرم‌شدگی پ به ب در فارسی میانه است. اما اسم nipēk/nibēg «کتاب، نوشته» محل بحث است: بارتولمه آن را *ni-paiθa-ka- > *nipēhak > nipēk، یعنی از همان ریشهٔ nibištan می‌دانست (همان که نورایی می‌گوید)، ولی نیبرگ (ج ۲ ص ۱۴۸) این را «ناپذیرفتنی» می‌خواند و nipēk را از *ni-pāya-ka- «آنچه به امانت نگاه داشته می‌شود، سند» از اوستایی ni-pāy- می‌گیرد. مکنزی هیچ ریشه‌ای نمی‌دهد. پس: فعل تأیید می‌شود و ادعای نورایی دربارهٔ nibēg با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D9%88%D8%B4%D8%AA%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D9%86%D8%A8%DB%8C%DA%AF\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:2201\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qāte' vol. 4, printed p. 2201 (incoming/BQT/BQT_v4_pages.txt, [pdf page 284]), Mo'in's footnote 9 to نوشتن: «نوشتن (بمعنی نبشتن)، پهلوی nipištan (= nibištan) (تحریر کردن)، پارسی باستان nipištanaiy (نوشتن) «بارتولمه ۸۱۷» «نیبرگ ۱۹۰» … مرکب است از دو جزء: نخست nī جزئی (پرفیکس، پیشاوند) است بمعنی فرود و پایین … دوم از ریشهٔ paiš در پارسی باستان و paēsa در اوستا که بمعنی نگاشتن و نگاریدن و نقش کردن است.» Exactly Nourai's chain.\"\n            },\n            {\n              \"ref\": \"UNV:54\",\n              \"status\": \"not_found\",\n              \"note\": \"Only the 1917 Heidelberg dissertation of Unvala's King Husrav is on disk (UNV.txt, 48 leaves), not the 1963 Paris edition Nourai paginates, so p. 54 does not exist in this copy. The word does occur in the text itself: 'ēstēd nipišt ēdōn nipēk pa us …' (UNV.txt line 1085, § 108); the glossary OCR is too broken to read the entry.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD (PHD.txt leaf 512, s.vv. nibēg, nibištan)\",\n              \"stance\": \"supports\",\n              \"note\": \"'nibēg [npyk' | N niwē] writing, scripture, book.' … 'nibištan, nibēs- [KTYBWN-stn' < A yktbwn, √ktb; npštn' | M nbyšt, nbyš-, N ~] write.' The English index (line 3539) reads 'scriptures nibēg' and (line 4365) 'write nibištan'. No etymology given for either.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II p. 148 (NYB_vol2_glossary.txt lines 2749, 2752)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"For the noun: 'nipēk [npyk'] document, codex, book … < *ni-pāya-ka- \\\"that which is kept … in safe custody\\\", \\\"record\\\", originally an administrative term; MPrth Prs nbyg; Paz. nevē, nivē. From Av. (886) ni-pāy- … Bthl's etymology: nipēk < *nipēhak < *ni-paiθa-ka- from a SW form of nipištan (MirM IV, 30, n. 2) is untenable.' For the verb, by contrast, Nyberg supports Nourai: 'nipištan [npštn'; KTYBWN-tn'] nipēs- to write … — OP ni-pais-; MPrthPrs nbyštn nbys-; Paz. nawaštan nivēs-; NP nuvištan, nivištan, nivēs-.'\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"s.v. *pais, p. 291 (Middle Persian and Parthian sections)\",\n              \"stance\": \"supports\",\n              \"note\": \"'*MIDDLE PERSIAN: MMP pyys-, BMP pys- /pēs-/ \\\"to adorn, colour\\\" || (+ *ni-) MMP nbys-, BMP nps- /nibis-/ \\\"to write, copy a book\\\" = DMMPP: 291b, 239b … Inf.: BMP npstn /nibištan/'; '*PARTHIAN: (+ *ni-) nbys- \\\"to write\\\".'\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"neveštan «نوشتن»; nobî «نُبی»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"نوشتن neveštan (also نبشتن nebeštan, نویشتن nevištan; present نویس nevīs-) is the direct continuation of MP nibištan / nibēs-: MP -b- was weakened to -w-/-v- between vowels, giving the classical doublet nibištan ~ nivištan, and the pretonic i was rounded to u/o before the following labial (nivištan > nuvištan > nevištan/neveštan) — Mo'in states the chain outright, «نوشتن [< نبشتن < نیپشتن]». Horn no. 1051 sets it out with the whole Iranian dialect family (Ossetic finssun, Balochi nibīsag, Kurdish nivīsīn) and derives it from 'ap. ni + √pais-, nipistanaiy'. نُبی nobī 'the Book, the Qur'ān' is the same word as MP nibēg 'book': MP -ēg gives NP -ī after the loss of the final -g (as in MP nāmēg > NP nāmī type, Pāzand nevē / nivē), so nibēg > nibī/nobī; it is a doublet of نوشتن in Wiktionary's words and must be kept apart from the Arabic homograph نَبیّ nabī 'prophet' (root n-b-ʾ), with which Persian poets sometimes punned. The Khosravāni line quoted on the page uses نبی in the Qur'ān sense. Mo'in has two separate entries: نبی nabī [ع.] 'پیغمبر' and نبی nibī 'قرآن مجید' with the bracketed gloss «نوشته، نامه» — i.e. exactly Nourai's 'book'.\",\n          \"derivation_fa\": \"«نوشتن» (و صورت‌های نبشتن، نویشتن؛ ستاک حال «نویس») دنبالهٔ مستقیم فارسی میانهٔ nibištan / nibēs- است: ب میان‌واکه‌ای به و نرم شده (nibištan > nivištan) و ای آغازین پیش از لب‌واج به اُ گراییده (nivištan > nuvištan > نوشتن). معین همین زنجیره را می‌آورد: «نوشتن [< نبشتن < نیپشتن]»، و هرن (شمارهٔ ۱۰۵۱، ص ۲۳۵) آن را از «ap. ni + √pais-, nipistanaiy» می‌گیرد و همتاهای ایرانی‌اش را (آسی finssun، بلوچی nibīsag، کردی nivīsīn) برمی‌شمارد. «نُبی» به معنی «کتاب، قرآن» همان nibēg پهلوی است: پسوند ـēg فارسی میانه با افتادن گ به ـی فارسی نو بدل شده (پازند nevē/nivē) و nibēg > نبی. این واژه را نباید با «نَبیّ» عربی (از ریشهٔ ن‌ب‌أ، به معنی پیامبر) یکی گرفت؛ معین نیز دو مدخل جداگانه دارد و نُبی را «قرآن مجید» با یادداشت «[نوشته، نامه]» معنی کرده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D9%88%D8%B4%D8%AA%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D9%86%D8%A8%DB%8C\",\n            \"https://abadis.ir/fatofa/%D9%86%D8%A8%DB%8C/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"ZFS:37\",\n              \"status\": \"not_checked\",\n              \"note\": \"Abolqasemi, Zabān-e Fārsi va Sargozašt-e Ān, is not digitised on any permitted platform (refs_online.json: kind 'catalog', 'Not found', re-searched 2026-09); no copy on disk.\"\n            },\n            {\n              \"ref\": \"MON:4669\",\n              \"status\": \"partial\",\n              \"note\": \"The Amir Kabir 6-volume pagination Nourai uses is not on disk, but the Adena reprint has both words: MON_part2.txt line 80918 «نوشتن: nivištan [< نپشتن < نیپشتن] (مص‌م.) … کتابت کردن، تحریر کردن» and line 74231 «نبی: (قد. nibī-) [نوشته، نامه (؟)] (ا.) قرآن مجید» — distinct from line 74227 «نبی: nabī [ع. نبیّ] (ص. ا.) پیغامبر». Content confirmed, page number unverifiable.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 1051, p. 235 (HRN.txt leaf 256)\",\n              \"stance\": \"supports\",\n              \"note\": \"'1051. niwištan, niwisten, nibistan, נביסתן (jüd.-pers.) \\\"schreiben\\\", Praes. niwēs-em; nubē, nuwē \\\"Wort Gottes, Qorān\\\". … ap. ni + √pais-, nipistanaiy \\\"schreiben\\\" — ai. √piś-, piṃśáti bedeutet nur \\\"schmücken\\\"; phlv. n(i)p(i)štan, n(i)p(i)štak, n(i)pēk \\\"Schrift\\\"; ksl. pisati. kurd. LW. nivīsīn; oss. d. finssun … Die Wurzel ist peiḱ, vergl. gr. ποικίλος.' Horn even lists 'nubē, nuwē' = نُبی 'Word of God, Qur'ān' in the same entry, exactly Nourai's second word.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien §130, p. 236 (HUB.txt line 8439)\",\n              \"stance\": \"supports\",\n              \"note\": \"'nivištan \\\"schreiben\\\" = ap. nipistanaiy, pr. nuvēsam, Wrzl. peiḱ' — listed among the Old Iranian *-št- clusters; and §101 (p. 212) 'nivēsam \\\"ich schreibe\\\" = ap. *nipaisāmiy (niyapišam ist sigm. Aorist = idg. ni-e-piḱ-so-m)'.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"s.v. *pais, p. 291 (*NWIR section)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Widely attested: (+ *ni-) NP nivištan/nivēs-, Kurd. (Kurm.) nivis-/nivisin, … Zaz. nustiš/nusen-, Awrom. niwištay/-niwis-, Gil. (Ršt.) nivistən/nivis- … \\\"to write\\\".'\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Mo'in via abadis.ir, s.v. نبی\",\n              \"stance\": \"supports\",\n              \"note\": \"Mo'in keeps the Arabic نبیّ 'prophet' and the Persian نبی 'قرآن مجید' apart, the latter with the bracketed original sense «نوشته، نامه».\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Old Persian\",\n          \"words\": \"paith; ni-paith\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Kent's Old Persian lexicon, p. 194 — the very page Nourai cites — has the entry 'paiθ- vb. \\\"cut, engrave, adorn\\\": Av. paēsa- \\\"adornment\\\", Skt. piṃśáti \\\"cuts, adorns\\\", Gk. poikílos \\\"variegated\\\", OCS pisati \\\"to write\\\", pIE *peik-, cf. Lt. pingit \\\"embroiders, paints\\\". Cf. also nipišti-, paišiyā-, Paišiyāuvādā-, pisa-. apiθa impf. DSf 54', immediately followed by 'ni- + paiθ- \\\"engrave, inscribe, write\\\": niyapaišam 1st sg. aor. DB 4.71; nipaištanaiy inf. XV 24f.; nipištam … DB 4.41, 47f; DNb 57; DSe 52; nipištā npf. XPh 31.' Kent's transliteration paiθ- (θ being the Old Persian outcome of the palatal before the front vowel in this stem, §593: 'pIE *pik-to-, OP ni-pišta- \\\"engraved\\\"') is precisely Nourai's 'paith'; some scholars read the aorist as niyapaišam with -š-, which is why Nourai's node #3 spells the same verb pais-. The verb underlies Darius' formula 'ahyāyā dipiyā naiy nipištam' ('it is not written in this inscription', DB 4.47f.) and the derived noun paišiyā- 'script, written text', whence the place-name Paišiyāuvādā-.\",\n          \"derivation_fa\": \"کنت در واژه‌نامهٔ پارسی باستان، همان صفحهٔ ۱۹۴ که نورایی به آن ارجاع می‌دهد، می‌آورد: «paiθ- فعل \\\"بریدن، کندن، آراستن\\\": اوستایی paēsa- \\\"زیور\\\"، سنسکریت piṃśáti، یونانی poikílos، اسلاوی کلیسایی pisati، هندواروپایی *peik-» و بی‌درنگ پس از آن «ni- + paiθ- \\\"کندن، نبشتن، نوشتن\\\": niyapaišam (بیستون ۴/۷۱)، nipaištanaiy (خشایارشا)، nipištam (بیستون ۴/۴۱ و ۴۷)». آوانگاری θ در برابر š به قاعدهٔ §۵۹۳ کنت برمی‌گردد (*pik-to- هندواروپایی > pišta- پارسی باستان). همین ستاک است که در فرمان داریوش «ahyāyā dipiyā naiy nipištam» («در این نبشته نوشته نشده است») و در اسم paišiyā- «نوشته، دبیره» و نام‌جای Paišiyāuvādā- دیده می‌شود. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pey%E1%B8%B1-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KNT:194\",\n              \"status\": \"supports\",\n              \"note\": \"KNT.txt leaf 218 carries the running head '194 OLD PERSIAN' and the entries 'paiθ- vb. \\\"cut, engrave, adorn\\\" … pIE *peik-', 'ni- + paiθ- \\\"engrave, inscribe, write\\\"', 'nipišti- sb. \\\"impression\\\": deriv. of ni- + paiθ-' and 'paišiyā- sb. \\\"script, written text\\\"'. Cheung 2007 independently cites the same page ('*OLD PERSIAN: pai(n)θ- … = Kent: 194').\"\n            },\n            {\n              \"ref\": \"SNS:164\",\n              \"status\": \"not_found\",\n              \"note\": \"Same problem as SNS:143 — the Šāyast nē Šāyast glossary OCR (SNS.txt, SNS_pages.txt) is unreadable and its printed page numbers were never mapped; greps for 'pes', 'nip', 'pišt' return only the unrelated pēš 'before'. Page 164 could not be located, and an Old Persian verb would in any case be odd matter for a Pahlavi text glossary.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae AiW col. 817, Old Persian material under paēs-\",\n              \"stance\": \"supports\",\n              \"note\": \"'p. pais- … mit ni \\\"nieder-, aufschreiben\\\": dipim tyām adam niyapišam Bh. 4.71 … np. nuvēsad \\\"er schreibt\\\", … np. nivištan \\\"schreiben\\\".'\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent §593 (KNT.txt line 1204) and Lexicon p. 194\",\n              \"stance\": \"supports\",\n              \"note\": \"'§593. PIE *ḱt (from ḱ or ǵ + t) became pAr. št, and then pIran. št, OP and Av. št, and Skt. ṣṭ; these clusters are seen in derivatives with a t-suffix: pIE *pik-to-, OP ni-pišta- \\\"engraved\\\"; *peik-t- in …'\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"s.v. *pais, p. 291 (*OLD PERSIAN section)\",\n              \"stance\": \"supports\",\n              \"note\": \"'pai(n)θ- \\\"to cut, engrave, adorn\\\" || (+ *ni-) \\\"to engrave, inscribe\\\" = Kent: 194. Pres. them./n-: impf. IND. 3pl. api(n)θa (DSf 54); Aor. s- IND. 1sg. niyapaišam (DB 4.71); Partic.: perf. pass. nipišta- (DB 4.47) …'\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 18.51 WRITE, p. 1284 table\",\n              \"stance\": \"supports\",\n              \"note\": \"The word for 'write' listed for Old Persian in Buck's table is 'OPers. ni-pis-'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Latin\",\n          \"words\": \"pingere\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin pingō, pingere, pīnxī, pictum 'to paint, embroider, tattoo, depict' is the nasal-infix present of this root: zero grade *piḱ- with the infix -n-, i.e. *pi-n-ǵ-/*pi-n-g-, whose perfect and participle (pīnxī, pictum) show the plain stem pic-. The -g- instead of the expected -c- is the classic irregularity of this etymon — it is why Pokorny lemmatises the root as 'peig-1 und peik-' and why Buck writes '*peig- beside *peik-'; Wiktionary flags it 'with irregular -g-', usually explained as analogical to other nasal presents (cf. fingō, tangō). Pokorny p. 794 lists 'Latin pingo, -ere, pinxī, pictum \\\"paint; with the needle prick\\\", pictor \\\"painter\\\"' in the first material paragraph, and Nourai's gloss 'paint, picture, tattoo' is Watkins' 'to embroider, tattoo, paint, picture' almost word for word (his cited reference here is AHD, and AHD is indeed the source of that wording).\",\n          \"derivation_fa\": \"لاتینی pingō, pingere «نقاشی کردن، گلدوزی کردن، خالکوبی کردن» ستاک حالِ میان‌افزودهٔ ناسال (nasal infix) این ریشه است: درجهٔ صفر *piḱ- با میان‌وند -n-، یعنی *pi-n-g-؛ ماضی و اسم مفعول (pīnxī، pictum) ستاک ساده pic- را نشان می‌دهند. حرف g به جای c مورد انتظار همان بی‌قاعدگی مشهور این ریشه است و علت آن است که پوکورنی مدخل را «peig-1 و peik-» می‌نویسد و باک «*peig- در کنار *peik-»؛ ویکی‌واژه آن را «با g بی‌قاعده» می‌خواند و معمولاً قیاس با دیگر ستاک‌های ناسال (fingō، tangō) دانسته می‌شود. پوکورنی در ص ۷۹۴ همین صورت‌ها را می‌آورد و معنایی که نورایی داده برگرفته از واتکینز/AHD است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/paint\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pey%E1%B8%B1-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt line 824, s.v. peig-1: '2. Nasalized zero-grade form *pi-n-g- in Latin pingere, to embroider, tattoo, paint, picture: PAINT, PICTOR, PICTURE, PICTURESQUE, PIGMENT, PIMENTO, PINTO; DEPICT, PICTOGRAPH.' Nourai's gloss is Watkins' wording.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW p. 794\",\n              \"stance\": \"supports\",\n              \"note\": \"'Latin pingo, -ere, pinxī, pictum \\\"paint; with the needle prick\\\", pictor \\\"painter\\\".'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, CEDEL s.v. paint (KLN_1966.txt line 26946, leaf 594)\",\n              \"stance\": \"supports\",\n              \"note\": \"'fr. L. pictus, pp. of pingere, \\\"to paint, embroider,\\\" fr. I.-E. base *peig-, \\\"to adorn by coloring or carving\\\" … Fr. *peik-, a related base, derive OI. peśaláḥ … Avestic paēs-, \\\"to adorn\\\" …'\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, IEC.txt line 12907 (~col. 1013)\",\n              \"stance\": \"supports\",\n              \"note\": \"'(pink-, variant of type ping- (?), but cf. pik-, peik-, poik-) Tokh. B pink-, v. \\\"write, paint\\\". Lat. pingo is ambig.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"paint, picture, pigment\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are Latin-via-French or direct Latin borrowings from the pingere family, and Nourai's arrow from node #7 is right for each. PAINT: Latin pictus (past participle of pingere) > Old French peint, past participle of peindre > Middle English peynten, painten (c. 1200) > paint. PICTURE: Latin pictūra 'painting', from pictus, borrowed into English in the early 15th century, first in the sense 'process of painting'. PIGMENT: Latin pigmentum 'colouring matter, paint', from the stem of pingere with the instrument suffix -mentum, in English from Old English pigment / Middle English pigment via Old French; the same word gives the doublets pimento and the second element of orpiment. None of these is a native English word, so 'English' here means 'English borrowing', as elsewhere in Nourai's Latin>English boxes.\",\n          \"derivation_fa\": \"هر سه واژه وام‌گیری‌های انگلیسی از خانوادهٔ pingere لاتینی‌اند و پیکان نورایی از خانهٔ ۷ برای هر سه درست است. paint: از pictus لاتینی (اسم مفعول pingere) > فرانسهٔ باستان peint (اسم مفعول peindre) > انگلیسی میانه peynten حدود ۱۲۰۰ م. picture: از pictūra لاتینی «نقاشی»، وام‌گرفته در آغاز سدهٔ پانزدهم. pigment: از pigmentum لاتینی «مادهٔ رنگی» با پسوند ابزارساز -mentum بر ستاک ping-، که دوگانه‌های pimento و جزء دوم orpiment نیز از آن است. هیچ‌یک واژهٔ بومی ژرمنی نیست؛ «انگلیسی» در اینجا یعنی «وام‌واژهٔ انگلیسی». ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/paint\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference of its own in the book; it inherits AHD from the Latin parent (node #7), whose peig-1 entry lists PAINT, PICTURE and PIGMENT among the English derivatives.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, CEDEL s.vv. paint, pigment (KLN_1966.txt lines 26946, 28805)\",\n              \"stance\": \"supports\",\n              \"note\": \"'paint, tr. and intr. v. — ME. peynten, painten, fr. OF. (= F.) peint, pp. of peindre, \\\"to paint\\\", fr. L. pictus, pp. of pingere …'; 'pigment, n., paint, dye. — L. pigmentum, \\\"coloring matter, paint\\\", from the stem of pingere … cp. pimento, pimiento and the second element in orpiment.'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. peig-1, and index entries (AHD_watkins1985.txt lines 824, 2087, 2090)\",\n              \"stance\": \"supports\",\n              \"note\": \"Index: 'PICTOGRAPH peig-1 … PICTOR peig-1 PICTURE peig-1 PICTURESQUE peig-1' and 'PIGMENT peig-1'.\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Etymonline, s.v. paint (archived web copy)\",\n              \"stance\": \"supports\",\n              \"note\": \"Etymonline gives the same chain: Old French peint, past participle of peindre 'to paint', from Latin pingere 'to paint, represent in a picture', from a nasalized form of PIE root *peig- 'to cut, mark by incision'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Germanic\",\n          \"words\": \"fihla\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The claim itself is standard: the Germanic word for the tool 'file' — Old English fēol/fīl, Old Saxon and Old High German fīla, Middle Dutch vile, German Feile — is normally traced to this root, the tool being named from the 'cutting/incising' sense (*peiḱ- > Gmc. *fihlō/*fīlō with Verner's-law voicing and the *-lō instrument suffix). But the form Nourai prints is wrong: his cited source, Watkins/AHD, writes 'Alternate form *peik- in Germanic *fihala, cutting tool, in Old English fīl, file: FILE', with a svarabhakti vowel — *fihala, not 'fihla'. Modern reconstructions write Proto-Germanic *finhlō (whence *fīhlō/*fīlō, from *peyḱ-lo-, with the nasal from the nasal-infix present); no handbook has a form 'fihla'. I rendered pdf page 386 at 200 dpi (copy saved as data/verification/sources/refs/ocr/BOOK/386.png) and the printed box reads 'fihla : cutting tool' — so the JSON is a faithful extraction and the dropped -a- is Nourai's own misprint of AHD's *fihala. Note also that Pokorny's peig-1 article on p. 794 does NOT list Feile at all; the Germanic 'file' words are attached to the root only by Watkins (and Klein, tentatively: 'prob. cogn. with OI. piṃśáti … L. pingere').\",\n          \"derivation_fa\": \"ادعای اصلی پذیرفتنی است: واژهٔ ژرمنی «سوهان» — انگلیسی باستان fēol/fīl، ساکسونی باستان و آلمانی علیای باستان fīla، آلمانی Feile — را معمولاً به همین ریشه بازمی‌گردانند، چون ابزار از معنای «بریدن، خراشیدن» نام گرفته است (ژرمنی آغازین *finhlō / *fīhlō با پسوند ابزارساز *-lō). اما صورتی که کتاب چاپ کرده نادرست است: مأخذ خودِ نورایی، واتکینز/AHD، «Germanic *fihala, cutting tool» می‌نویسد، با واکهٔ میانجی؛ هیچ فرهنگی صورت «fihla» ندارد. تصویر صفحهٔ ۳۸۶ کتاب را با دقت ۲۰۰ نقطه بر اینچ بازآفریدم (در data/verification/sources/refs/ocr/BOOK/386.png نگاه داشته شد) و در آن به روشنی «fihla : cutting tool» چاپ شده است؛ پس خطای خوانش اسکن نیست، خطای چاپی خودِ کتاب است. افزون بر این، پوکورنی در ص ۷۹۴ اصلاً Feile را زیر این ریشه نیاورده و تنها واتکینز (و کلاین با احتیاط) آن را به این ریشه می‌بندد.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"fihla\",\n          \"correct_form\": \"fihala (AHD/Watkins); Proto-Germanic *finhlō ~ *fīhlō\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/file\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pey%E1%B8%B1-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"partial\",\n              \"note\": \"AHD_watkins1985.txt line 824, s.v. peig-1: '1. Alternate form *peik- in Germanic *fihala, cutting tool, in Old English fīl, file: FILE.' The derivation is exactly Nourai's, but the reconstructed form is *fihala, three syllables, not the two-syllable 'fihla' the book prints.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW pp. 794-795, lemma peig-1 and peik-\",\n              \"stance\": \"silent\",\n              \"note\": \"grep for 'fihala', 'Feile', 'fila ' in POK_full.txt returns no hit inside this article; Pokorny's Germanic material here is only 'Gothic filu-faihs, Old High German / Old Saxon fēh \\\"varicolored\\\", Old English fāh, fāg', with no word for the tool.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, CEDEL s.v. file 'a tool of steel' (KLN_1966.txt line 14712, leaf 320)\",\n              \"stance\": \"supports\",\n              \"note\": \"'file, n., a tool of steel. — ME. file, fr. OE. fēol, fīl, rel. to OS., OHG. fīla, OSwed. fīl, MDu., MHG. vīle, Du. vijl, G. Feile, and prob. cogn. with OI. piṃśáti, \\\"hews out, carves\\\", L. pingere, \\\"to paint\\\". See paint and cp. words there referred to.' Klein connects it to the same root but reconstructs no Germanic *fihla.\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Etymonline, s.v. file (archived web copy)\",\n              \"stance\": \"supports\",\n              \"note\": \"Etymonline traces the tool-name to Old English fil, from Proto-Germanic *finh(a)lo (source of Old High German fila, German Feile), from PIE *peig- 'to cut, mark by incision' — again with the vowel Nourai's form lacks.\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"file\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English file 'metal tool with a roughened surface for abrading' descends from Old English fīl/fēol (West Saxon fēol, Anglian fīl), Middle English file, from the Germanic word discussed at node #9 (*finh(a)lō, cognate with Old High German fīla > German Feile, Old Saxon fīla, Middle Dutch vīle). The Old English long ī survived the Great Vowel Shift as /aɪ/, giving modern 'file'. Nourai's gloss 'grinding tool' is a reasonable rendering of Watkins' 'cutting tool'. It must be kept apart from the homonym file 'row, collection of papers', which is unrelated (Latin fīlum 'thread' > French fil, filer), and Klein indeed gives them as two separate headwords on the same page.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی file «سوهان» از انگلیسی باستان fīl/fēol و انگلیسی میانه file می‌آید، از همان صورت ژرمنی که در خانهٔ ۹ آمد (*finh(a)lō؛ هم‌ریشه با fīla آلمانی علیای باستان > Feile آلمانی امروز و vīle هلندی میانه). ای کشیدهٔ انگلیسی باستان در جابه‌جایی بزرگ واکه‌ها به /aɪ/ بدل شده است. معنایی که نورایی داده («ابزار سایش») برگردان آزاد «cutting tool» واتکینز است. این واژه را نباید با هم‌آوای آن file «ردیف، پرونده» یکی گرفت که از fīlum لاتینی «نخ» می‌آید و کلاین آن دو را دو مدخل جداگانه آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/file\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No reference is printed in this box; it inherits AHD from the Germanic parent (node #9), where Watkins ends the sub-entry with 'in Old English fīl, file: FILE'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, CEDEL (KLN_1966.txt lines 14709, 14712, leaf 320)\",\n              \"stance\": \"supports\",\n              \"note\": \"Klein has three separate headwords: 'file, n., 1) a collection of papers; 2) a line, row'; 'file, n., a tool of steel. — ME. file, fr. OE. fēol, fīl …'; and 'file, tr. v., to make foul, to defile'. Only the second is ours.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985, index (AHD_watkins1985.txt line 1509)\",\n              \"stance\": \"supports\",\n              \"note\": \"'FILE1 gʷhi- FILE2 peig-1' — the tool 'file' is assigned to peig-1, the row/thread 'file' to gʷhi- (Latin fīlum).\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etymological Dictionary, s.v. file (2)\",\n              \"stance\": \"supports\",\n              \"note\": \"Skeat likewise separates file 'a steel rasp' (A.S. fēol, O.H.G. fīhala, fīla) from file 'a line, row' (F. file, L. fīlum), confirming that Nourai's box is the tool word.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-07T20:59:45.260Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-386.json (file state is current in your context — no need to Read it back)
```


## [2026-09-07T20:59:53.055Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"file (2)\\|File, a steel\\|a steel rasp\\|fihala\\|f.hala\" SKT.txt | head -10; echo \"=== SKT file ===\"; grep -n \"^File\" SKT.txt | head -10",
 "description": "Grep Skeat for file"
}
```


### [2026-09-07T20:59:53.137Z] TOOL RESULT

```
=== SKT file ===
13986:File  (t),  a  tumour,  lit.  a  ball.  (L.)  Only in  the  pi.  pila.^'L,  pUa,  a  ball.
```


## [2026-09-07T20:59:55.270Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### paint\"; grep -n -i \"pingere\\|peig\\|peindre\" 5d2ae2676d1f399f.txt | head -8; echo \"### file\"; grep -n -i \"finh\\|peig\\|fil\\b\\|Feile\" 95f3ce3d9354c1b9.txt | head -12",
 "description": "Check archived etymonline pages"
}
```


### [2026-09-07T20:59:55.354Z] TOOL RESULT

```
### paint
25: mid-13c., peinten , "represent (someone or something) in paint;" c. 1300, "decorate (something or someone) with drawings or pictures;" early 14c., "put color or stain on the surface of; coat or cover with a color or colors;" from Old French peintier "to paint," from peint , past participle of peindre "to paint," from Latin pingere "to paint, represent in a picture, stain; embroider, tattoo," from a nasalized form of PIE root *peig- "to cut, mark by incision."
45: metal tool for abrading or smoothing, Old English feol (Mercian fil ) "file," from Proto-Germanic *fihalo "cutting tool," which is probably from PIE root *peig- "to cut, mark by incision" (source also of Old Church Slavonic pila "file, saw," Lithuanian piela "file"). Germanic cognates include Old Saxon fila , Old High German fila , Middle Dutch vile , Dutch vijl , German Feile . Century Dictionary (1906) lists and names 60 types of them for various purposes. Nail file (for the fingernails) is by 1819.
49: early 15c., "portray, paint, form a likeness of in color," from Latin depictus , past participle of depingere "to portray, paint, sketch; describe, imagine," from de "down" (see de- ) + pingere "to paint" (see paint (v.)). Extended sense of "portray in words, describe" is from mid-15c. Related: Depicted ; depicting .
66: *peig- 
75: 1640s, "of or pertaining to pictures or the making of them," with -al (1) + Latin pictorius "of a painter," from pictor "painter," from past participle stem of pingere "to make pictures" (see paint (v.)). Meaning "expressed or depicted in pictures" is from 1807; the sense of "ill
79: early 15c., pictur, pictoure, pittour, pectur, "the process or art of drawing or painting," a sense now obsolete; also "a visual or graphic representation of a person, scene, object, etc.," from Latin pictura "painting," from pictus, past participle of pingere "to make pictures, 
83: late 14c., "a red dye," from Latin pigmentum "coloring matter, pigment, paint," figuratively "ornament," from stem of pingere "to color, paint" (see paint (v.)). By 1610s in the broader sense "any substance that is or can be used by painters to impart color" (technically a dry su
95: trisulphide, yellow color," from Latin auripigmentum, from aurum "gold" (see aureate) + pigmentum "coloring matter, pigment, paint...," from stem of pingere "to color, paint," from a nasalized form of PIE root *peig- "to cut, mark by incision."...
### file
25: "place (papers) in consecutive order for future reference," mid-15c., filen , from Old French filer "string documents on a thread or wire for preservation or reference" (15c.), earlier "to spin thread," from fil "thread, string" (12c.), from Latin filum "a thread, string; thread of fate; cord, filament," which is reconstructed to be from PIE *gwhis-lom , suffixed form of root *gwhi- "thread, tendon." The notion is of documents hung up on a line in consecutive order for ease of reference.
39: metal tool for abrading or smoothing, Old English feol (Mercian fil ) "file," from Proto-Germanic *fihalo "cutting tool," which is probably from PIE root *peig- "to cut, mark by incision" (source also of Old Church Slavonic pila "file, saw," Lithuanian piela "file"). Germanic cognates include Old Saxon fila , Old High German fila , Middle Dutch vile , Dutch vijl , German Feile . Century Dictionary (1906) lists and names 60 types of them for various purposes. Nail file (for the fingernails) is by 1819.
54: 1706, a string of things in a straight line, from French enfilade , from Old French enfiler (13c.) "to thread (a needle) on a string; pierce from end to end," from en- "put on" (see en- (1)) + fil "thread" (see file (v.1)). Used of rows of apartments and lines of trees before military sense came to predominate: "a firing with a straight passage down ranks of men, channels in fortifications, etc." (1796). As a verb from 1706 in the military sense, "rake with shot through the full length." Related: Enfiladed ; enfilading . The Old French verb was borrowed in Middle English as enfile "to put (something) on a thread or string."
61: *peig- 
82: a mountain region," 1640s, especially in a military sense, "a narrow passage down which troops can march only in single file...," from French défilé, noun use of past participle of défiler "march by files" (17c.), from de- "off" (see de-) + file "row...The verb, "to march off in a line or file," is by 1705, from French défiler....
```


## [2026-09-07T21:00:01.937Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"rasp\\|A\\.S\\. feol\\|feol\\|Feile\" SKT.txt | head -15",
 "description": "Grep Skeat for feol/Feile"
}
```


### [2026-09-07T21:00:01.997Z] TOOL RESULT

```
4312:CrawL  (Scand.)  Iccl.  kra/fa,  10  paw, crawl  ;  Swed.  knxfia,  to  grope,  kraia,  to crawl ;  Dan.  kravie,  to  crawl.  Frequen* tative  from  Tent,  base  KKAP,  to  wiae, grasp,  hence,  to  grope;  sec  Cramp.
5387:Dram,  Drachm.  (F.-^.-Gk.^ drame,  drtichme^  '  a  dram,  eighth  p< an  onnc;e;'Cot.  —  L.t/rwr/ww.  — Gk.Jip a  handful,  a  drachm.i,  o-scd  both  as  V{ and  coin :  cf.  ipay^a,  as  mach  at  on grasp. —  Gk.  Upaaaofim,  I  grasp.
6403:Fathom.  (E.)  M.E,  /adrru,  A.S. fteJim  the  space  reached  by  the  extended arms,  a  ^^rasp,  embrace. +  r'"'  vadem,  Icel. fax  mr.  a  fathom,  Dan.  /avn.  Swcd.  famn^ AD  embrace,  G. /adtn.  Allied  to  FsteaL CVf'AT.)
6583:purl  (5),  to  form  an  edging  on  lace,  In- veit  stitches  in  kniLting.  (F.  —  L.)  Fre- quently misspelt  pearU  Contraction  of purfit.^Y.  pourfdcr,  to  purfle,  embroider on  an  clge  —  F.  /V«r  (L  pro\  confused  (as often)  with  Y.par  (^L.  per),  ItuQoghoQt; /!/,  a  thread. File  {3),  a  steel  rasp.  (C.)  A.S./r^/.-f Du  vij/,  iXm./;/,  Swed.//,G./«/f,  Russ. pt/ii,  a  hie,  sharp  tool.
7308:froni  the  fbriei/  end  a^inst  the  mist ;  ihe fishing  spear  is  hooked.  — O.  F.  ^^,  * gaff,  iron  hook.  Of  Celtic  origin  —Irish ^/,ga/a,  ft  hook,  W.  ta^,  a  grasp,  grapple. fork,  ^a/ht/,  a  hold-  From  Irish  gahh,  to take,  cognate  w-ith  !>.  (apere,  to  take.  And see  Gable  (^KAP.)  Der. ^ncvAvi  (obso- lete), a  spear.  W.  ga/lacA.
7435:I.  sufiix  -^r/,  iroiD  Span,  garra,  a 1.  dutch,  grasp.  —  Hret.,  W.,  sod the  ihuik  of  the  leg.
7940:Grasp.  (E.)  M.  E.  gmspen,  used  In  the sense  Mo  grope/  Put  for  grapsen  :Iike f/oj/-M.  E.  efapsm\  an  extension  (lOoi a  base^fm/-,  closely  allied  lo  Grope,  q  t
8017:Gripe  (E.)  A.  S.  grifan,  pi.  t.  grdp, pp.  gj-ipen,  to  seize.  +  Du.  grijpen.  Icel. gri  pa.  Sttxd.  gri  pa,  Dan.  gribe^  Goth. greipan.  G,  greifcn,  Ruiis.  grabite,  .Skt. grah  {yftiX\^grahh).  to  seize.  (VGARBII.) Allied  to  grab,  grasp.
11889:form ;  prob.  from  fjta/fwrfiv,  to  seize,  grasp. Der  mita'm&T/<M-csis,  a-morfh-otu.
14721:Mile,  adapled  for  piping.  (L.) rith  suffix  'iU  ^L.  -ilii)  (rom  L. /,  pp.  of  prehcndirt,  prttiden,  to jf.  •»  L.  /r(f ,  before ;  obsolete  A/m- rasp,  oogT-.atc  with  E.  0«t.  q.  v. bend.  ^L.)  L.  apprtfundere, mj  hold  of.^L.  ap-  {ad)f  to,  at; 1^  to  gi^sp  (above). "Ice.  (F.  — L.)  From  a  dia- I,  snch    as  the  Walloon  ap-
14731:imprison.  iF.-L.)  Put  lor  rm/mw. — O.  K.  €mf>risonner,  to  imprison. —Q.  F. *»i-  (•=!-.  i«),  in ;  priten^  a  prison  (below). prentice,  short  forapprentioe^abuve). prise,  priae,  a  lever.  (F.  — L.)  *  Prist, a  lever ; '  HalUwell.  Hence '  to  /riit  open a  box,'  or  corruptly,  'to  pry  opUL'— F. prise,  a  grasp,  tight  nold  (hence,  leverage). Orig.  fcm.  oi prij,  pp.  oi prcndit,  to  grasp.
14732:^^ prekendere,  to  grasp.
15601:rapaclotiB.  (L.)     Coined  60m  I.  m pad-,  crude  form  of  rapax,  grasping rapert,  to  grasp,
15629:^  wrb.  (F.  •  O.  H.G.>  M.  E. -O.  F,  rasUr  (F  «f;W-).  -OH  G. whence  G.  rojpeln,  to  rasp.  Cf. J.  hrtsfen,  to  rake  together. er,  &  light  narrow  sword.  (F.  — U-  H.  G.)  F.  rafigrt  \  it  was  con- as  Spmish.  '  kapim^  Spanische :'  1  Tl'^jrave.  No  doubt  rafiert for  '■t-'/'ift-g*,  a  name  given  in  con- nesning  *  a  rasper  '  or  poker ;  hence called  *  %.  ^roKing'Spit  of  S^xiine;' wSpan.  rasfatUra,  a  raker.  *. Span. to  n>^  scratch.  *0.  H.  G.  rasfjH ^So  Dies;  Uttre  rejects  this I,  bat  wiadvisedly.
15633:HM,  Hl  rasped,  reduced  to  powder;  pp.
```


## [2026-09-07T21:00:25.931Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 - <<'PY'\nimport json,io\np='data/verification/page-386.json'\ns=open(p,encoding='utf-8').read()\n\nold_skt='''            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etymological Dictionary, s.v. file (2)\",\n              \"stance\": \"supports\",\n              \"note\": \"Skeat likewise separates file 'a steel rasp' (A.S. fēol, O.H.G. fīhala, fīla) from file 'a line, row' (F. file, L. fīlum), confirming that Nourai's box is the tool word.\"\n            }'''\nnew_skt='''            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etymological Dictionary, s.v. File (3) (SKT.txt line 6583)\",\n              \"stance\": \"supports\",\n              \"note\": \"'File (3), a steel rasp. (E.) A.S. fēol. + Du. vijl, Dan. fil, Swed. fil, G. Feile, Russ. pila, a file, sharp tool.' Skeat keeps this apart from his File (1) 'a line, row' (F. file, L. filum), confirming that Nourai's box is the tool word; he offers no Indo-European root.\"\n            }'''\nassert old_skt in s\ns=s.replace(old_skt,new_skt)\n\ns=s.replace('''              \"src\": \"WEB\",\n              \"where\": \"Etymonline, s.v. paint (archived web copy)\",\n              \"stance\": \"supports\",\n              \"note\": \"Etymonline gives the same chain: Old French peint, past participle of peindre 'to paint', from Latin pingere 'to paint, represent in a picture', from a nasalized form of PIE root *peig- 'to cut, mark by incision'.\"''',\n'''              \"src\": \"Etymonline\",\n              \"where\": \"etymonline.com/word/paint (archived 2026-09-07 as sources/web/5d2ae2676d1f399f.txt)\",\n              \"stance\": \"supports\",\n              \"note\": \"'mid-13c., peinten ... from Old French peintier \\\\\"to paint\\\\\", from peint, past participle of peindre \\\\\"to paint\\\\\", from Latin pingere \\\\\"to paint, represent in a picture, stain; embroider, tattoo\\\\\", from a nasalized form of PIE root *peig- \\\\\"to cut, mark by incision\\\\\".' The same page derives picture (Lat. pictura) and pigment (Lat. pigmentum) from the stem of pingere.\"''')\n\ns=s.replace('''              \"src\": \"WEB\",\n              \"where\": \"Etymonline, s.v. file (archived web copy)\",\n              \"stance\": \"supports\",\n              \"note\": \"Etymonline traces the tool-name to Old English fil, from Proto-Germanic *finh(a)lo (source of Old High German fila, German Feile), from PIE *peig- 'to cut, mark by incision' — again with the vowel Nourai's form lacks.\"''',\n'''              \"src\": \"Etymonline\",\n              \"where\": \"etymonline.com/word/file (archived 2026-09-07 as sources/web/95f3ce3d9354c1b9.txt)\",\n              \"stance\": \"supports\",\n              \"note\": \"'metal tool for abrading or smoothing, Old English feol (Mercian fil) \\\\\"file\\\\\", from Proto-Germanic *fihalo \\\\\"cutting tool\\\\\", which is probably from PIE root *peig- \\\\\"to cut, mark by incision\\\\\" (source also of Old Church Slavonic pila \\\\\"file, saw\\\\\", Lithuanian piela \\\\\"file\\\\\"). Germanic cognates include Old Saxon fila, Old High German fila, Middle Dutch vile, Dutch vijl, German Feile.' Note *fihalo, with the medial vowel that the book's 'fihla' lacks.\"''')\n\ns=s.replace('''            {\n              \"src\": \"WEB\",\n              \"where\": \"Etymonline, s.v. file (archived web copy)\",''','''            {\n              \"src\": \"Etymonline\",\n              \"where\": \"etymonline\",''')\nopen(p,'w',encoding='utf-8').write(s)\njson.load(open(p,encoding='utf-8'))\nprint('ok')\nPY",
 "description": "Fix SKT and Etymonline citations"
}
```


### [2026-09-07T21:00:27.368Z] TOOL RESULT

```
ok
```


## [2026-09-07T21:00:31.444Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-386.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 386",
 "description": "Validate and run verify_check"
}
```


### [2026-09-07T21:00:32.837Z] TOOL RESULT

```
JSON OK
nodes verified: 10/10
node verdicts: {'confirmed': 7, 'plausible': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 8, 'not_found': 3, 'partial': 4, 'not_checked': 3}
books consulted: {'supports': 31, 'silent': 2, 'partial': 2, 'contradicts': 1} | by book: {'BRT': 5, 'CHEUNG': 5, 'KLN': 4, 'WLD': 2, 'PHD': 2, 'NYB': 2, 'HUB': 2, 'MON': 2, 'POK': 2, 'AHD': 2, 'Etymonline': 2, 'ARY': 1, 'HRN': 1, 'KNT': 1, 'SYN': 1, 'IEC': 1, 'SKT': 1}
```


## [2026-09-07T21:00:55.112Z] AGENT

Done. `verify_check.py 386` reports **0 PROBLEM lines** (10/10 nodes).

**Page 386 (book p. 356) — one entry, root "Peig" (PIE), 10 nodes**

Verdicts: root `confirmed`; nodes — 7 `confirmed`, 2 `plausible`, 1 `transcription_suspect`.
Ref checks: 8 supports, 4 partial, 3 not_found, 3 not_checked. 36 `consulted` entries across BRT, CHEUNG, KLN, POK, WLD, AHD, SYN, IEC, KNT, HRN, HUB, PHD, NYB, MON, SKT, ARY, Etymonline.

Flagged items:
- **#9 Germanic "fihla" — transcription_suspect (`error_in: book`).** Nourai's own source, Watkins/AHD s.v. peig-1, prints Germanic ***fihala** ("cutting tool"); Etymonline has PGmc *fihalo, modern reconstruction *finhlō. No source knows a form "fihla". I rendered pdf p. 386 at 200 dpi — the printed box reads "fihla", so the extraction is faithful and the dropped -a- is the book's misprint. Page image saved to `data/verification/sources/refs/ocr/BOOK/386.png`.
- **#3 "ni-pais" labelled [Avestan / Old Persian] — plausible.** The ni- compound is attested only in Old Persian (niyapaišam DB 4.71 etc.); Bartholomae prints it under the Avestan verb but every citation is Achaemenid, and Cheung/Buck/Kent all file it as Old Persian only. There is no Avestan *ni-paēs-; the box duplicates node #6.
- **#4 Pahlavi nipēk/nibēg — plausible.** The verb nibištan is solid, but Nyberg (Manual II p. 148) explicitly rejects deriving nibēg from this root: "nipēk < *ni-pāya-ka- … Bthl's etymology: nipēk < *nipēhak < *ni-paiθa-ka- from a SW form of nipištan … is untenable." MacKenzie gives no etymology. Nourai follows Bartholomae; the question is still open.

**No extraction errors** — the JSON matches the printed page node-for-node, including the Sa'di and Khosravāni couplets. (The empty box drawn right of the Old Persian row on the page carries no words and is correctly absent from the JSON.)

Notable positive finds: Kent's Old Persian lexicon **p. 194** — the exact page Nourai cites — has "paiθ- vb. 'cut, engrave, adorn' … pIE *peik-" plus "ni- + paiθ-"; Cheung 2007 cites the same page. Borhan-e Qāte' **p. 440** (vol. 1 leaf 666) and **p. 2201** (vol. 4, pdf p. 284) both carry Mo'in's footnote giving exactly Nourai's chain for پیسه/پیسی and نوشتن. Nyberg p. 168 confirms پیشه: "pēšak … from the same stem as Av. pištra- in the same sense."

Refs that could not be checked: **SNS:143 / SNS:164** (Tavoosi's Šāyast nē Šāyast glossary — OCR unusable, no page mapping), **UNV:54** (only the 1917 dissertation is on disk, not the 1963 Paris edition Nourai paginates), **ZFS:37** (Abolqasemi, not digitised anywhere). MON page numbers are unverifiable because only the 2-volume Adena reprint is on disk, though both entries were found and match.
