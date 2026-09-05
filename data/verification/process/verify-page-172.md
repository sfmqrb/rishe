# Verification process log — verify-page-172


## [2026-09-05T20:46:47.231Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 172 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-172.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-172.json. Write /home/sfmqrb/git/rishe/data/verification/page-172.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 172` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:46:48.770Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:46:49.479Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:46:49.495Z] TOOL RESULT

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


## [2026-09-05T20:46:49.735Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-172.txt"
}
```


### [2026-09-05T20:46:49.746Z] TOOL RESULT

```
1	=== PDF page 172 (book page 142) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Genu 1 : angle, knee  (refs POK:381)
4	#1 (parent #0) [Avestan] refs=POK:381; SOD:184 | žnu, znum : knee
5	#2 (parent #0) [Sogdian] refs=SOD:184 | jnwwq : knee
6	  #3 (parent #1) [Persian] refs=BQT:1000 | zânu «زانو» : knee
7	#4 (parent #0) [Greek] refs=POK:381 | gônia : angle, corner
8	  #5 (parent #4) [Persian] refs=MON | gŭniâ «گونیا» : set-square, right angle
9	  #6 (parent #4) [English] refs=AHD | diagonal, pentagon, polygon
10	#7 (parent #0) [Germanic] refs=AHD | kniwam : knee
11	  #8 (parent #7) [English] refs=None | knee, kneel
12	--- entry 1 ---
13	ROOT [Indo-European] Genu 2 : chin, jaw bone  (refs POK:381)
14	#1 (parent #0) [Avestan] refs=POK:381; SYN:221 | zânu, zanva : chin
15	  #2 (parent #1) [Persian] refs=SYN:221; BQT:1036; HRN:148; VIE:12 | zanax «زنخ» : chin ; câneh «چانه» : chin | extra: زنخدان
16	#3 (parent #0) [Sanskrit] refs=POK:381 | hanu : jaw, chin
17	#4 (parent #0) [Germanic] refs=AHD | kinnuz : chin
18	  #5 (parent #4) [English] refs=None | chin
19	--- entry 2 ---
20	ROOT [Indo-European] Geph, Gebh : mouth  (refs POK:382)
21	#1 (parent #0) [Avestan] refs=POK:382; KLN:833; SYN:221; DZA:58 | zaf- : mouth ; zaf-an : mouth ; zaf-ar : mouth
22	  #2 (parent #1) [Persian] refs=BQT:1024; HRN:589,663 | dahân «دهان» : mouth ; zafar «زفر» : mouth
23	#3 (parent #0) [Germanic] refs=AHD | kabal : jaw ; kaf : to chew
24	  #4 (parent #3) [English] refs=KLN:264,833 | jowl : jaw ; chafer : a beetle
25	
```


## [2026-09-05T20:46:53.707Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-172.json",
 "description": "Read source JSON for page 172"
}
```


### [2026-09-05T20:46:53.746Z] TOOL RESULT

```
{
  "pdf_page": 172,
  "book_page": 142,
  "entries": [
    {
      "root": {
        "name": "Genu 1",
        "lang": "Indo-European",
        "refs": "POK:381",
        "gloss": "angle, knee"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:381; SOD:184",
          "words": [
            {"translit": "žnu, znum", "gloss": "knee", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:184",
          "words": [
            {"translit": "jnwwq", "gloss": "knee", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1000",
          "words": [
            {"translit": "zânu", "gloss": "knee", "script": "زانو"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:381",
          "words": [
            {"translit": "gônia", "gloss": "angle, corner", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "gŭniâ", "gloss": "set-square, right angle", "script": "گونیا"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "diagonal, pentagon, polygon", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "kniwam", "gloss": "knee", "script": null}
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
            {"translit": "knee, kneel", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Genu 2",
        "lang": "Indo-European",
        "refs": "POK:381",
        "gloss": "chin, jaw bone"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:381; SYN:221",
          "words": [
            {"translit": "zânu, zanva", "gloss": "chin", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "SYN:221; BQT:1036; HRN:148; VIE:12",
          "words": [
            {"translit": "zanax", "gloss": "chin", "script": "زنخ"},
            {"translit": "câneh", "gloss": "chin", "script": "چانه"}
          ],
          "script_extra": "زنخدان",
          "note": null,
          "quote": {
            "text": "ای دل گر ازآن چاه زنخدان به درآیی - هرجا که روی زود پشیمان به در آیی",
            "poet": "Hâfez"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:381",
          "words": [
            {"translit": "hanu", "gloss": "jaw, chin", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "kinnuz", "gloss": "chin", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "chin", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Geph, Gebh",
        "lang": "Indo-European",
        "refs": "POK:382",
        "gloss": "mouth"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:382; KLN:833; SYN:221; DZA:58",
          "words": [
            {"translit": "zaf-", "gloss": "mouth", "script": null},
            {"translit": "zaf-an", "gloss": "mouth", "script": null},
            {"translit": "zaf-ar", "gloss": "mouth", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1024; HRN:589,663",
          "words": [
            {"translit": "dahân", "gloss": "mouth", "script": "دهان"},
            {"translit": "zafar", "gloss": "mouth", "script": "زفر"}
          ],
          "note": null,
          "quote": {
            "text": "زبانش بسان درختی سیاه - زفر باز کرده فگنده به راه",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "kabal", "gloss": "jaw", "script": null},
            {"translit": "kaf", "gloss": "to chew", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "KLN:264,833",
          "words": [
            {"translit": "jowl", "gloss": "jaw", "script": null},
            {"translit": "chafer", "gloss": "a beetle", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:46:55.350Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','SOD','BQT','MON','AHD','SYN','HRN','VIE','KLN','DZA','WLD','BRT','PHD','NYB','HUB','ARY','IEC','CHEUNG','SKT','FSD','WEB']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Inspect refs_online.json keys"
}
```


### [2026-09-05T20:46:57.433Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
VIE {"title": "M.A. Sajjadiyyeh, Vazheha-ye Irani dar Zaban-e Engelisi, Bonyad-e Neyshabur 1364/1985", "kind": "local_scan_ocr", "url": "https://parsianjoman.org/?p=5160 (Parsi-Anjoman hosts the 253-page scan)", "lookup_hint": "Not found.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_sajjadieh1364_parsianjoman.pdf", "/home/sfmqrb/git/rishe/data/verification/s
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
DZA {"title": "M.T. Rashed Mohassel, Daramadi bar Dastur-e Zaban-e Avestai, Khajeh 1364/1985", "kind": "purchase", "url": "taaghche.com (revised edition ebook)", "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: the 1364 Khajeh edition is not digitised; a revised edition is sold as an ebook on Taaghche."}
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
CHEUNG MISSING
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
```


## [2026-09-05T20:47:07.120Z] TOOL CALL #5: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -60; echo ---; ls /home/sfmqrb/git/rishe/data/verification/ | head -40; echo ---; sed -n 1,80p /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "List local reference files and source matrix"
}
```


### [2026-09-05T20:47:07.178Z] TOOL RESULT

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
---
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
---
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
```


## [2026-09-05T20:47:11.227Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ĝenu\\|genu-\\|ĝep\\|ĝebh\" POK_full.txt | head -40",
 "description": "Grep Pokorny for genu roots"
}
```


### [2026-09-05T20:47:11.293Z] TOOL RESULT

```
30427:(with Indo Germanic *genu-^Vx\ee' barely as dissimilation form compatible to *gnu-n- 
30771:jawbone ' are probably contaminated somehow with genu-^c\\\v! (under S. 381 f.). 
35407:Root / lemma: genu-1, gneu- {*ghenu-) 
35417:Root / lemma: genu-1, gneu- : "knee, joint' > Root / lemma: gen-1, gene-, gne-, gno- : "to 
35468:Root / lemma: genu-2\. and {genaA^--) gonady- 
35474:Root/ lemma: genu-2i. and {genad!^-:) gona6!^-\ chin' derived from Root/ lemma: genu-1, 
35499:Tocharian A sanwe-m Dual f. "mandible, lower jaw bone ' (e-extension from genu-). 
35519:derived from Root/ lemma: genu-2i. and {gensd'^-:) gonad!^-\ chin' : Root/ lemma: genu-
```


## [2026-09-05T20:47:12.642Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && python3 -c \"\nimport json\nd=json.load(open('page-124.json'))\nprint(json.dumps(d['entries'][0], ensure_ascii=False, indent=1)[:3500])\n\"",
 "description": "Look at format of an existing verification file"
}
```


### [2026-09-05T20:47:14.463Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Dhě 2",
 "verdict": "confirmed",
 "modern_form": "PIE *dʰeh₁- 'to put, place; to do' (Pokorny 235-239 dʰē-2; Watkins/AHD dhē-¹)",
 "note": "The root box is right on all three counts. Pokorny's own lemma reads 'Root / lemma: dʰe-2, Meaning: to put, place, say' with 'Page(s): 235-239', so Nourai's 'Dhě 2 : to do, set' with POK:235 reproduces Pokorny's numbering and gloss exactly; Watkins in the AHD appendix has 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235]', and Wiktionary's reconstruction page glosses *dʰeh₁- 'to do; to put, place'. The Iranian material of the chart is likewise Pokorny's own: 'with full grade Avestan Old pers. dāta-', 'Avestan ni-δaiti- „laying down, putting away, hiding“', 'Avestan gao-δi- / gao-δana- „milk container“', 'Avestan dāman-, dąman- n. „site, creature“'. Three things in Part 1 need correcting rather than the root itself. (1) The Avestan mouth-veil is paiti.dāna-, not 'paiti-dâma' (node #3) — a misprint in the printed book, and one that Mo'in's footnote on the very page Nourai cites (Borhān p.418) refutes. (2) apa-dāna- (node #6) is Old Persian, not Avestan, and means 'palace, columned hall'; 'the concealed part of a palace' is Kent's etymological comparison with Skt. apadhā-, not the word's attested sense. (3) Pahlavi dast-war (node #13) does not belong to this root at all: Horn p.127, the page Nourai cites, and Nyberg II 61 both derive it from the root daṇs-/dąh- 'to teach', and Wiktionary offers only *dasta-bara- 'hand-bearer' or *danh- 'to teach'. A fourth, smaller point: the gloss 'to settle, to give' on node #11 mixes this root with PIE *deh₃- 'to give', a distinction Nourai's own reference FFD:52 (Abolghasemi p.52) draws explicitly. Two of the four boxes on the Persian side, the Sogdian box and both of the Persian outcomes of the law-branch check out completely, and Gharib's Sogdian entry γwδʾak even carries the Avestan etymology Nourai draws.",
 "note_fa": "خودِ ریشه کاملاً درست است: پوکورنی در صفحات ۲۳۵–۲۳۹ مادهٔ dʰē-2 را با معنای «نهادن، قرار دادن» آورده و واتکینز در پیوست فرهنگ American Heritage همین را می‌گوید؛ مواد ایرانی نمودار (dāta-، ni-δaiti-، gao-δana-، dāman-) هم عیناً از همین مادهٔ پوکورنی است. سه لغزش در بخش یکم هست: ۱) صورت اوستایی «پنام» paiti.dāna- است نه paiti-dāma — خطای چاپی کتاب؛ ۲) apadāna پارسی باستان است نه اوستایی و معنایش «کاخ، تالار بار» است؛ ۳) پهلوی dastwar هیچ ربطی به این ریشه ندارد و هرن (ص ۱۲۷) و نیبرگ (ج۲ ص ۶۱) آن را از ریشهٔ daṇs-/dąh- «آموختن» می‌گیرند. نکتهٔ کوچک‌تر آنکه معنای «دادن» در خانهٔ ۱۱ متعلق به ریشهٔ دیگر *deh₃- است و ابوالقاسمی در همان FFD:52 این دو را جدا کرده است. در مجموع، ادعای نورایی دربارهٔ خودِ ریشه درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-"
 ],
 "ref_check": [
  {
   "ref": "AHD:1512",
   "status": "supports",
   "note": "Watkins's Indo-European appendix (local file AHD_watkins1985.txt line 375): 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235.]' — the same list Nourai cites by its 1975 New College page 1512 (roots are alphabetical over pp.1505-1550, so 'dhē-' falls in the right place); the copy on disk is the 1985 standalone reprint with different pagination."
  },
  {
   "ref": "POK:235",
   "status": "supports",
   "note": "POK_full.txt lines 22276-22510: 'Root / lemma: dʰe-2 / Meaning: to put, place, say' ... 'References: WP. I 826 ff ... Page(s): 235-239'."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where"
```


## [2026-09-05T20:47:18.141Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '35400,35560p' POK_full.txt",
 "description": "Print Pokorny genu-1 and genu-2 sections"
}
```


### [2026-09-05T20:47:18.222Z] TOOL RESULT

```
Common IE h- > k-. 

References: WP. I 578 ff., WH. I 613 f., II 176 ff., Trautmann 370 f.. Feist 316 f., Meillet 
Cinquantenaire 172 ff. 
Page(s): 376-378 

Root / lemma: genu-1, gneu- {*ghenu-) 

Meaning: knee, joint 

Grammatical information: n. inflection gonu, genues, gnUo^fseic; besides the /7-stem 

according to Old \v\6\c Janunf both knees ' and gr. Y6vaT0(; etc. from gonuQ- 

Comments: 

Root / lemma: genu-1, gneu- : "knee, joint' > Root / lemma: gen-1, gene-, gne-, gno- : "to 

bear', (the euphemism of lower part of te body) 

Material: Old Indie ya/7^n. "knee', Pahlavi zanuk, npers. z5/7j"knee'; Avestan Akk. Sg. 

znum, dat. abl. pi. znubyo; Old \n6\c Jnu-badh- ' the bending knees ', abhi-jnu^ up to the 

knee ', pra-jhu-h' saber-legged ', Avestan fra-snu-^ holding the knees forwards ' (:gr. 

*np6-YVu); 

Armenian cunr^kuee' (/'-extension to old ^-stem *gdnu-), PI. cunk-k'. Gen. cng-ac\N\\h 
^-extension {*gon-g-o-, compare yvu-^); 

Maybe alb. Geg {*gdnu-) gjuni, Tosc gluri^ knee'. 

gr. yovu. Gen. (Hom.) youvoc; ( *gonu6s), PI. youva, Aeolic yova "knee' (compare also 
y£uvu)v yovaTwv Hes.), besides Gen. Sg. youvaTO(; (for *yovFavo(;); lengthened grade 
ywvia "point, edge' (*yu)vFia), zero grade (compare under npoxvu) yvu-nsTsTv " drop to 
one's knees ', yvu^ " on the knees ', iyvun (besides iyvu(;, Specht KZ. 59, 220) " popliteus, 
the part behind the thigh and knee, ham ' (*£yyvua, -yvu(;); 

irpoxvu " with stretched out knee ' II. 570 stands for *np6yvu (= Old Indie pra-Jnu-h)\ 



Latin genu, -us' knee; of plants, a knot, joint ', gen/cu/um'Wnee, a little knee, a knot or 
joint on the stalk of a plant; angle '; 

Gothic kn/un., Old High German etc. kn/o, kneo {*kniwa-, Indo Germanic *gneuo) 
"knee' (Old Norse knea\so from 'knot in the straw', as Old English cneowehV knotty, from 
plants '; Latin geniculum also " a knot or joint on the stalk of a plant '; but Latin genista is 
Etruscan); an extension with Germanic /in oberschles. knutzen' squat on the knees ' and 
perhaps in Gothic knussjan " kneel ', kniwam knussjands " bending in the knees together ', 
if in a tu-siem *kn uss us irom this verb *knutjan^ based on '; 

lllyrian FIN Genusus, Low Italian PN Genusia, Messapic PN tn'-gonoxoa, Ligurian PN 
Genua, adjective derivative Genava " Geneva '; 

Tocharian A kanwem, B kenJne Dual, "the knees'; 

Hittite gi-e-nu {genu) "knee'. 

Note: 

Pronunciation of the labialized laryngeal: Hittite gi-e was gje- as in Albanian gju- 

References: WP. I 586 f., WH. I 592 f., Schwyzer Gr. Gr. I 463, 518. 
Page(s): 380-381 

Root / lemma: genu-2\. and {genaA^--) gonady- 

Meaning: chin 

Note: 

Root/ lemma: genu-2i. and {genad!^-:) gona6!^-\ chin' derived from Root/ lemma: genu-1, 

gneu-{*ghenu-) : knee, joint'. 

Material: Old Indie hanu-si. " mandible ', Avestan zanu- ds., in compounds (with 

secondary Aryan gh-, GiJntert WuS. 11, 124 f.); 

Phrygian a-^nv Akk. d-^£va "beard' (prefix a- and *gen-); (common Occidental Romance 
vowel prefix) 

gr. Y£VU(;, -uo(;f. "chin, mandible' (with secondary J-stem; compare ysvEiov "chin beard' 
from *Y£V£Fiov, Y£vr|i'(;, Attic ysvp^f. " edge of the hatchet ' from *Y£V£Fi(;); 

Latin genai. "cheek' (fur *genus aiter mala), genuTnus {dens) " grinder, molar tooth '; 



Old Irish g/{u)n'rc\ou\h\ cymr. gen'cheek, chin', PI. geneu, acorn, genau, bret. genou 
(older PI. *geneues)\ 

Gothic k/nnust "cheek' {* genus, *genues, -/7/7-fronn -nu-). Old Norse kinnt " cheek, 
mountainside ', Old English cinn. Old High German kinniu. "chin'; (under the influence of 
common Celtic -ns-, -nt- > -nn-). 

Tocharian A sanwe-m Dual f. "mandible, lower jaw bone ' (e-extension from genu-). 

gon9A'^-\v\ Lithuanian zandas^ mandible', Latvian zi/do's"chin, sharp edge'; maked. 
KQvaSoi aiaY6v£(;, yvaGoi (compare Specht KZ. 59, \W)\ 

zero grade gr. Yva9o(; f., Yva9ij6(; m. " mandible' ( *gnaA^^\ 

unclear is Armenian cnauV mandible, cheek'. 

References: WP. I 587, WH. I 589 f., Specht Dekl. 87, 253, Schwyzer Gr. Gr. 463. 
Page(s): 381-382 

Root / lemma: gep^)-, ^eb^- 

Meaning: jaw, mouth 

Note: 

Root/ lemma: gep(h)-, ^eb^-: jaw, mouth' : Root/ lemma: gerrid^-, gixt"^-: to bite; tooth' 

derived from Root/ lemma: genu-2i. and {gensd'^-:) gonad!^-\ chin' : Root/ lemma: genu- 

1, gneu-{*ghenu-) : knee, joint'. 

Material: With ptr. Avestan zafar-, za/a/7- "mouth, jaw', participle Med. vT-zafana, compare 

s-stem (besides rln-sieru) in ^rizafah- besides &rizafan-\ 

Maybe alb. Geg za" capture, bite'. 

with bh : gallorom. expressive *gobbo-. Old Irish gop, nir. gob^b\\\, beak, neb, mouth'; 

Maybe alb. ^op "vagina'. 

Germanic with ph or to partial b'^ Old Norse kjaptror kjgptr{ *kebuta- or *kefuta-) 
"muzzle, mandible, jaw ', Middle High German kivel, kiver^ jaw ' {*kefra-) Modern High 
German dial. /r/e/e"giir, ndd. keve^ jaw, gill', wherefore the verbs Norwegian kjava^ 
quarrel, argue ' (" move the jaws ') 

Maybe alb. {*zifem) zihem " quarrel' [common alb. g- > -z- ; -f- > -/?-] 



Middle Low German Low German kibbelen, kabbelen, kevelen' babble, chatter loudly ', 
Middle High German kibelen, A/fe/e/? 'quarrel, squabble', kiven, kiffen^ gnaw ', kifelen^ 
gnaw, chew '; lengthened grade Old Norse kafi. Old Saxon cafi. Old English ceafl{ev\Q\. 
jowl, jole) " jaw ' ( *kefala-). 

In addition as ' nibbler ': 

Old High German chevaro, kevar. Middle High German /rei/e/ie 'beetle, chafer' {*kebran- 
); changing through ablaut Old English ceafor {*kabra- ox *kabru-), ndd. kavel6s.; 

Lithuanian zebiu, zebtT eat slowly ', zebiu, zebetT eat, peck '; 



Old Church Slavic o-zobatT AupaiveaGai ', serb. zobatT eat, devour ', z6b\. ' oat ', 
russ. zobatb " eat, peck ', zobxx\. 'bill, beak, neb'; 

Czech zabra^QiW of the fish ', russ. zabry6s. could have covered zfrom the e-grade and 
contain a variant with g-.
```


## [2026-09-05T20:47:37.402Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '35560,35590p' POK_full.txt",
 "description": "Get page number for gep(h) lemma"
}
```


### [2026-09-05T20:47:37.453Z] TOOL RESULT

```
contain a variant with g-. 

from genib^-'b\te' as a nasalized form belongs to our root? 

References: WP. I 570 f., Trautmann 364, Benveniste Origines 10 f., Kluge''"' s. v. 'beetle, 
chafer' and ' jaw '. 
Page(s): 382 

Root / lemma: gefs- 

Meaning: to turn, bend 

Material: Armenian car'tree', PI. ' brushwood ' {*grso-)\ caray{*gr-ati-) 'servant, 

farmhand'; c^/'slant, skew, crooked' {*gorsos)\ 

gr. ysppov n. ' anything made of wicker-work; oblong shield, covered with ox-hide; 
wattled screens or booths, used in the Athen. market-place, generally, wattles; wicker 
body of a cart ' etc., also 'penis' ('*rod') (*Y£pajov); 

Maybe alb. /ra^'penis' : Gypsy AsA'penis'. 

Latin gerra^ anything made of wicker-work ', PI. gerrae^ wattled twigs; trifles, stuff, 
nonsense ' is gr. loanword; zero grade yappa pap5o(; and yapaava cppuyava. K^\\izc, 
Hes.; 

from Gr. Y£p5iO(; derives Latin gerdius^ weaver '; 



cymr. gyrrxw. " drive, impel, drift, propel, push, thrust, livestock drive ' {*gersjo-),
```


## [2026-09-05T20:47:38.661Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT zanu/znu ===\"; grep -n \"zānu\\|zanu\\|znu-\\|znūm\\|zafar\\|zafan\\|zafa\" BRT.txt | head -40",
 "description": "Grep Bartholomae for zanu, zafar"
}
```


### [2026-09-05T20:47:38.721Z] TOOL RESULT

```
=== BRT zanu/znu ===
4538:•  j.  anu.zafan-  Adj.  'längs  des  Mauls, dem  Maul  entlang  gehend';  *usrB.az(t»S hisiinte  "faiiB  takahe  "(die  Rinder)  stehen da  Tränen  vergiessend,  dem  Maul  endang gehenden  Laufs"'*  Yt. /0.38.
4814:mit  "p.parü,  y  parai''>  'weg-,  fortgehen, sich  entfernen';  a)  absol.:  natrya-san/ta . . para.ili'ii  (2SIA.)  upa.vazanuha  avi  ntnä- n>m  airyamaifii  (sii.)  V,  22.  7;  —  *para.- äip^^  upa.vazala  nairy3.sa»hs  avi  . .  V. 22. 13;  —  zaota  (sd.)  anakaxtö  par^at dqhiUäi  .  .  zao^r)m  raSxsaiti  N.  A'o;  — yezica  *alte  ratavö  *anahaxta  para.tya- yanti^^^  N,  Ai?;  —  uzayeni  psrayaii  V,  2-2. I.  a)  II  militärisch  'ausrücken,  ins  Feld ziehen':  avd^ä/aiy  a'iaAam  paraidiy (2SIA.)  avam  käram  jadty  Bh,_^.3;  2.7, 10; — ara^äsam  a>aA<im  piirait>l(iP'PTA.) avam  käram  . .  jatä  Bh._y.14_:  9,  2,6,14;
7633:•  j.  araj-ant- Adj.  (fem.  'yaiii-)  'entseulich, abscheulich';  a)  von  der  Hölle:  paosisUmäi yat  °yat  daozaahum  P.  ^o;  —  *bun9m atiksm  t)iHat?hahe  yal  'yatö  dagzanuhahe V. /^.  47;  —  °yata  haca  duzauha  Yt. /<?.44;  —  'fatal  haca  äaozavilt  Yt.  4. 7.  b)  von  Fliegen:  baivarj  maxHnqm 'yaitinam  V.14.6; — *max/i./hArpa  "faitya (ISf.)  V.7.2.
7904:)a  ahüm\aSäunS  '^.4-j.i,;  —  nynnSl  da^ayäzö vanhSuS  °oa  zafar?  *aoi^3urDayqn  °%a  rün^antS  Yt. J7.6;  —  jaginbuitarS  anhat  yS  . .  kam.- pa/miii{?.A)  ya'ha  hilu  yS  nöit  '%a  "..als der,  der  nicht  desgleichen  (tut)"  V.  4. 48.  4)    'hier*":    °Äa    ml  tarn    hqm.-
8686:•  j.  u§-  n.  'Ohr'  uzw.  «^»rischer  Wesen'': k/(NS.)  F.9(?).  A)  sonst  nur  Du.;  a)  'die Ohren':  yezi  *kva£ibya  ''-sibya''^^  aiwi.- srunvaifi  . ,  yezi  äat  nöit  /ivagibya  "Hbya aiwi.surunvait(  N.  i'ö";  Uj;  —  *'sibya F.p'>*>;  —  drimts  .  .  asi  [-//Is)  karma gava  *dvari'^ra  zafan  Yt  jr.2;  —  pairi 'si  vSrayavw»m  kam  gava  nidanzaydmoMii Yt.  j.  27;  —  g?tirvaya  h?  päoave  züvar^ pairi  iS  'si  zvrpnäioi  sk)Hd?m  si  manS kirsnüioi  Y.9.28;  —  °//  ahuralu  mazda yazamaide  darp'^räi  (sd.)  maiirahe  .  . xratüm  .  .  mar>%räi  .  .  hisvqm  . .  fra^'äküi Yt. /.  28.  a)  von  Tieren;  °H  (näml. g>us)  pairi. dar ayänli  (sd.)  daSma  .  .  Vt. 14. 56.  b)  'Gehör*,  d.  i.  Fähigkeit  richtig zu  hören  und  zu  verstehen,  sva.  'Auf- fassungs-,  Verstandeskraft':  ava  pa'oS  ava zastS  ava  °/i  däraydiiwjm  .  .  däityanqm .  . syaoiinanqm  varpzäi  Vr.  75.  1;  —  d<lya ml . .  mastim  spilnö  xsviwrjm  (sd.)  hizi'qm uruiie  -si  xratBiH  .  .  Y.62.4.
9332:•  j.    'karana-  m.    Ohr',   uzw.  rfnÄ^ischer       haben;  vgl.  Yt.  ,0.  125.-»)  Anders  freilich Wesen":    lai  drvalö   drvatyiisca    asi    usi ■     Dk.  /.  4.  44  (SBE.  47.  59). 'na{Kp.)gava*dvari>mzafar»..pairi.-\^    .     ^^^3-    V.    'ausschütten'.    Praes.    2 urvalit^m  (sd.)  Yt.//.2.  ,_(.^„^._  _  pp^p^  ^^„y^._
13989:•  j.  ^dvariSra-''  n.  'Fuss,  Bein'  uzw. daSvischex  Wesen;  tat  drvats  .  .  an  usi karftia  gava  °ra'^^^  zafar»  .  .  pairi.- unaiitim  (sd.)  Yt//.  2.
14676:•  j.  Sri-zafan-,  -zafah-  Adj.  "mit  drei Mäulero,  Rachen',  \aa  AiayDaAäia;  aiii
15621:•  j.  pairi.urvaeäta-  Adj.  'der  am  meisten, besten  zu  Grunde  richtet',  mit  Akk.:  tat drvatö  drvatySs^a  asi  [jwV]  karma  gava *ävari^ra  zafarf  .  ,  'Um  "das  ists,  was am  besten  des  Gottlosen  Augen , .  zu  Grunde richtet"  Yt  n.  2.
18789:•  j.  oasiSta-  Adj.  (fem.  'tä-)  'der  am besten  zu  Grunde  richtet';  a)  mit  Akk.: jaynista  'la  (VS.)  tayüm^a  hazanuharamca Yt. /2. 8.  b)  absol.:  artrahe  maittySui 'tqm'^  dalnqm   äalvayasnanqm   Y.  72.  11.
24563:•  j.  vi-zafana-  Adj.  'den  Rachen  auf- reissend,  mit  geöflhetem  Rachen':  gan- liarrwim  .  .yS  apata^  •nü  minxiänS  gai'iiä astvaitlS  alahe  YL/p.  41.
24826:mit  US  'aufleuchten,  aufflammen,  empor- leuchten': vlspa  anayra  raocä  (sd.)  usca us.raoi'ayäii  V.  2.  40  PüZ.;  —  zafar?  paiti uzraecaymi  Yt.  tQ.  50;  —  vTusniti  (sd.) *usi.'^raocaiti  bamya  V.  7p.  28.
27617:•  j.  za/ati-  n.  sva.  zafar-. KorapEL  —  np.  dahan.
27618:•  j.  zafar-  n,  'Mund  (,  Maul)',  uzw.  daivv scher  Wesen  ">:  tat  ärvaiS  drvalyäsca  .  . zafar»  (AS.)  .  .  pairLurvas^tjm  (sd.)  Yt. II.  z;  —  nyancö  daivayäzS  °far>  (AS.) *aoi.giurvayqn  Yt.  11.  6;  —  °/an  (AS.) paiti  uzraocaymi  Yt.  ig.  50;  —  'far^  (LS.) tafsqn  aya  masB  N.^.^t.
27619:KoinpE.  —  Vgl.  'sa/an;  'zafah-  und  iiaa- fäna-,  —  np.,  tnp.  (Pü.)  sa/iir;  vgl.  nhd.  kitfit, ai.  jimbha-  m.  'Gebiss ,  Rachen'.  —  ')  Im üegens.  zu  läh;  ilamati:  —  ')  iVersch./  -  ih »b'-  S  ^3,  femer  Hbm.  PSt  70,  Bgm.  Grdr. /'.  632 ;  falsch  Jn.  AJPh.  10.  86. j.  zaahim  N.  6^\  lies  pasväzanlum.
27890:•  j.  zaranyö.zafar-  Adj.  'mit  goldenem Maul',  sva.  Spitze,  vom  Pfeil:  isunam  . . °fram  Vtio.  i»9.
28698:•  j.  haetumata-  Adj.  'mit  dem  (Fluss)  »sihista  psiri.haizanuka  ytke  sa%aica HaHumant  zusammengehörig,  von  ihm  vaxiaica  yaotifm  dalät  ahurö  matdh  V. gebildet':  srayS  yat  kasaan  (sd.)  -Um  Yt   21.4.
```


## [2026-09-05T20:47:47.193Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== Knie ===\"; grep -n \"Knie\" BRT.txt | head -20; echo \"=== Kinn ===\"; grep -n \"Kinn\" BRT.txt | head -20",
 "description": "Grep Bartholomae for Knie and Kinn"
}
```


### [2026-09-05T20:47:47.259Z] TOOL RESULT

```
=== Knie ===
7119:nicht  am  FUlz. •  j.  ä-xsnav-'>  Adj.  'bis  zum  Knie  reichend, so  gross  dass  es  bis  zum  Knie  reicht'
7122:(sd.)  . .  'ttBs'ca  ". ,  bis  zum  Knie  reichende '  -tanm  ä);  —  haeaipr^m  anumayanatn  .  .
10919:•  j.  ^xünav-  n.  'Knie':  s.  imter  inav-. KompE.;  a.  aocb  iuxhtiu&ra-.
12298:Scheint  «US  "liMjcSnuta-  (»gL  huxfnula-)  durch  1 Antehnung  an  im'  "Knie'  =  'Ecke,  Kante' hervorgegangen  in  sein;  vgl.  Pü.  —  Pä.:  Cffl
17221:Eig.  'des  Knie«  hoch  sind,  hoehliegen'O;  vgl.
18066:•  j.  fra-änav-  Adj.  (auch  fem.)  'dieKniee(?) nach  vom  haltend',  von  der  Fliege ;  *maxH.- kihrpa  irr^aitya  'snai>s(GS(.)  apazi^ataks *akaramm.driwyä  (sd.)  V.  7,  a.
19648:•  j.  (3.)matJyöi.paitiStiina-  Adj.  'bis  zur Mitte  des  Beins  reichend,  so  gross,  dass es  bis  zur  Mitte  des  Beins  geht':  yS  paoiryS bansma  frastprmata  %tyaxitls{^^ca  .  . äxlnaiea  maihfSifaitiitänqsla  ". .  bis  zum Knie  und  bis  zur  Mitte  des  Beins  reichende (Zweige)"  Y.57.6.
28084:*:iinav-  f.  'Kinn'');  vgl.  %\.  hänav-  f.,  np. zaiiiix.  —  Pii.;  züiiak  drahnäk.  —  ')  Vor- strecken des  Kinns  bei  gleichzeitigem  Streifen des  llandiückens  vom  Ilats  her  nach  dem Kinn  tu  drückt  in  Italien  Geringschätzung aus.  —  >)  Das  ä  ist  aufrälÜg;  man  hat  das Wort  dirtim  mit  'Knie'  übersetit  —  lulelil Gdn.  SPreussAW,  ig.  414:  'Kniestoss' -  und zu  ai.  j'iinit  n.,  np.  zitiii  gestellt  Aber  Pü. spricht  nicht  dafür  j  'Knie'  wäre  zänüi.
28462:•  j,  Snav-  n.  'Knie':  s.  unter  Inav. KompE.
28566:•  j.  znav-"',  x/nav;  snav-  n.  'Knie': daSimm  (bz.  f^yum)  klstiBm  V.  Ä  61— 63', (J.  23  f.^;  —  /rasa  /raysit  .  .  3  tangaft- byasHt  äps  ä  zmtbyasHi  äpS  ä  maiiya- tias'it  apS  V.6.2T,  —  wertlos:  znaunqm Vd.  i2.  S.  noch  "snma.
28572:•  j.  *znu.barflz-'>  f.  'Kniehohe,  -tiefe"': 'barasO  n»r?b»r>zB  *gairiJnns5  mSn!>  (sd.) FrBy.
30181:•  j.  *hu-xönaoi)Ta-  n.  'gutes  Knie'": ustrahe  . .  yS  kafim  aipijpayeiü  spaHtittm upa  vaylatum  '^re  (AD.)  Aupaitisläiu'* "des  Kamel(hengst)s,  der  weisslichen Schaum  auf  seinen  Kopf  zurückwirft, auf  seine  guten  Knie  und  Beine"-  Yt 14.  iZ'^.
30182:*xsniu>%ra-  n.  'Knie'  kann  ich  nur  als  Um- bildung von  *i!nav-  n.  'Knie'  (vgl.  äsinav- und  inav-)  nach  Wörtern  wie  dvar&ra-  n, 'Bein',  ai.  cariira-  n.  'Fuss',  iharilra-  n.  'Arm' begreifen.  —  Npü.;  bisyär  xuscihr. —  i)Vgl.Bd. 34.  4,  wo  das  Kamel  hulnük  genannt  wird.  — )>  Dualrerbindung,  lu  BB.  lO,  ifiT.  —  3)  S. iSt.  Dst.  ZA.  3.  S65,  Jn.  Reader  109.
=== Kinn ===
4859:reinigung"  (sva.  "und  es  so  verunreinigen")  metallenen  (eisernen)  Kinnbacken':  vara-
7315:—  ii^ravamm  bisazy<ll{%A.')  dahmayä^ pars äfrimitN.  7. 41  ;^'?.  37,  Sl.  13. 43  Z.  a)  mit dahma-  oder  mit  d°  und  vauhai'-  Bezeich- nung des  60.  Kap.  des  Yasna:  dahma "tii  Y.60.  Überschr.;  — ■  dakmaheca  tiars alaonS  dahmqm\ca\  vaauhim  °tim  V.  6/. I.  A)  mit  dahma-  und  vavhav-  als Gottheit  ■'>;  alät  dim  aiwysiti  y,l  dahma vanhi  "tis  ultrahe  kthrpa  P.J2;  —  dah- tnqm  vanuhim  °/;i»Y.2.iS,7.a6,  P.j_j"; — dahmaya  vatahuya  °töil\.i.\<„  7.26,  8.\, 70.3.  2)  'Verwünschung*:  agvaht  .  . ana/aonS  zänu.dräjä  asti  °tii  "die  Ver- \vünschung  eines  . ,  Ungläubigen  geschieht durch  Vorstrecken  des  Kinns"  V. /<V.ii.
15110:Komp.:  faiti-\^''ar'  (S  3O4  11.  45),  elg.  'was den  Kinnladen  gegenüber  liegt'.  —  Pü. ;  pati!- 37'
28083:•  j.  zänu.dräl|ah-  Adj.  (auch  fem.)  'im Vorstrecken  des  Kinns  bestehend':  aEvahe zl  .  .  anasaonS  v'l  (NSf.)  .  .  ü/riti^  (ßAy V.  16.  II.
28084:*:iinav-  f.  'Kinn'');  vgl.  %\.  hänav-  f.,  np. zaiiiix.  —  Pii.;  züiiak  drahnäk.  —  ')  Vor- strecken des  Kinns  bei  gleichzeitigem  Streifen des  llandiückens  vom  Ilats  her  nach  dem Kinn  tu  drückt  in  Italien  Geringschätzung aus.  —  >)  Das  ä  ist  aufrälÜg;  man  hat  das Wort  dirtim  mit  'Knie'  übersetit  —  lulelil Gdn.  SPreussAW,  ig.  414:  'Kniestoss' -  und zu  ai.  j'iinit  n.,  np.  zitiii  gestellt  Aber  Pü. spricht  nicht  dafür  j  'Knie'  wäre  zänüi.
29297:Eig.  'was  die  Kinnladen  (*^ar>na-)  enthält'; S  304  IL  ao.  —  Pü.:  ervärai,  bei  Jahasfji Gtoss.  741  'bolh  the  eais;  the  left  jaw';  s. dazn  HOBH  NpEt.  375  und  SWienAW.  67. 838.  7:  arvär.güi  i  cap.  —  i>  Vgl.  rSt  Sl. ti.  4.
```


## [2026-09-05T20:48:03.289Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD grep knee ===\"; grep -n \"knee\" SOD_pages.txt | head -20; echo \"=== SOD jnww ===\"; grep -n \"jnww\\|znww\\|zʼnw\\|zanuk\" SOD_pages.txt | head -20",
 "description": "Grep Gharib Sogdian for knee"
}
```


### [2026-09-05T20:48:03.347Z] TOOL RESULT

```
=== SOD grep knee ===
7312:1223 >nyh        B, S                                   Jt,          on knees
16853:        knee
22669:     GMS 674; VJ; BSTBL; STii 7.31, 36; Frag. 2a.6;                  (fo)bow, (r<?)kneel
22696:      STii 10.42                                                  kneeling
23035:                                                                  (/o)kneel
23046:     kneeling                                                      suitable
23090:6735 pcyyrb- B                           ^iijj/J'jj                OcOkneel
23098:     OcOkneel                                                       =*-p5>k
29353:                                                                    kneeling
36097:11143 z}m B                                     ^jp-tjkijb             knee
38661: jasper 2230, 2231                      Karfish  4878                           knee    4591, 11155
38662: jasper-coloured       2229             Kashghar      4668, 4669                (ftf)kneel 6607, 6726, 6736, 6746
38663: jaundice    11584                      (/<?)keep    3414, 3583, 4577           kneeling   6622, 6727, 8886
39057:     on knees   1238                           3509,3515,3733,6199,6341,                paper    4632, 4634, 4635
=== SOD jnww ===
7311:                                                                     anzanuk ©ob. -y
16849: 4590 jnwq => jnwwq                                               zukyamenc      (jwqy'mync)
16850: 4591 jnwwq      M                                     y\j        safe, sound
29354:                                                                    spat-zanuk ©fspa-, Parth. nyspy-, nyspyd
36095:          Fll, 12, 13, 20 G6 285; TSP 19.9, 22                         zanuk    (z*nwq, z*nwk(>)) ©<*zdnuka ©ob. pi.
36104:11144 zWsp S                                         ^UU-       11157 z}nwk()) *± zWwk, jnwwq
36741:    11352 znkp8*y S                                                  zanu(k) (znw, znyq) ©<*zanuka\ Skt. hanit;
36743:          zanak-pa5e                                                   Parth. znx\ MP dnwg\ Pash. zana-y Bal. zanuk
```


## [2026-09-05T20:48:03.999Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN 221 area: chin ===\"; grep -n \"4.207\\|Chin\\b\\|CHIN\" SYN.txt | head -30",
 "description": "Grep Buck synonyms for chin"
}
```


### [2026-09-05T20:48:04.058Z] TOOL RESULT

```
=== SYN 221 area: chin ===
5194:419 Back 4.20 Hap 4.202 Sxuiu 4.203 Brain 4,204 Facr 4.205 ForEHEAD 4.206 EyEsrow 4.207 Jaw
5731:4.207 JAW 4.208 CHEEK 4.209 CHIN
5762:Av. zanu- <i Rede sh 4.207-4.209. There is considerable | the front part is the chin, the hinder part
5768:4.207. Several of the words for ‘jaw’ owe this use to some resemblance in shape, as that of a ‘sickle’ to the lower jaw in side view, of a ‘wagon, cart’ to the palate or upper jaw, of a ‘box’ to the
5812:1. Grk. -yévus ‘jaw’ and ‘cheek’, sce 4.207.
5814:Grk. ovéyév, usually ‘jaw’ (4.207), but ‘cheek’ in NT (Mt. 5.39, Lk. 6.29) and several pap. (Moulton-Milligan, s.v.).
5816:2. Lat. gena : Grk. yévus ‘jaw, cheek’, etc. See 4.207.
5824:(4.207). dim. of carro ‘cart’, and i first as slang, for Ae wsety ith reference to the lower [erent in eating. Le Riv. fil. esp. 11.316. Bee obraz ‘face’ and ‘cheek’, fr. ‘, (ChSl. obrazi ‘form, shape, plavie, ‘cheek’, etc. Tiktin image’, SCr. obraz ‘cheek , etc.
5838:OE céace (WSax.), céce (Angl.) ‘jaw’ (4.207), also ‘cheek’ (so Mt. 5.39, Lk. 6.29 in Lindisf. vs. wenge in WSax. ver- sions), and so reg. later, ME cheke, NE cheek. NED s.v. cheek.
5848:Russ. sceka, prob. orig. ‘jaw’, as Pol. szczeka, earlier szczeka (4.207).
5850:4,209. Some of the words for ‘chin’ belong to the group of cognates in which jaw’, ‘cheek’ and ‘chin’ interchange (4.207). Some reflect the ‘shape ’as ‘something projecting’ or a ‘hook’. Sev- eral belong with words for ‘beard’ (4.142), for just as ‘chin’ may give the word for ‘beard’, so conversely a word for ‘beard’ or ‘behind the beard’, ‘what has a beard on it’, may be used also for the ‘chin’, and, once so established, no incongruity is felt in applying the term equally to a woman’s chin.
5851:1. Grk. yévetoy : yévus. ‘jaw, cheek’, etc. (4.207).
5860:OE cin, OHG kinni, etc., general WGume. for ‘chin’ = Goth. kinnus, ON kinn, ete. ‘cheek’: Grk. yévus Saw, cheek’, etc. (4.207).
5862:Lett. zwods, mostly ‘chin’ but in some places ‘jaw’ : Lith. zandas, Grk. yvdbos ‘jaw’ (4.207). Miihl.-Endz. 4.759.
5931:4. Ir. gin, W. geneu (beside gen ‘chin’), Br. genou : Lat. gena, Goth. kinnus ‘cheek’, etc. (4.207).
6749:W. dylyfu gen, Br. dislevi gen, phrases with gen ‘jaw, chin’ (4.207), the verbs, used only in these phrases, being cpds. with prefix W. dy-, Br. di(s)-, but second
```


## [2026-09-05T20:48:18.298Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=16830 && NR<=16860' SOD_pages.txt; echo \"---- page tag before 16849 ----\"; awk 'NR<=16849 && /\\[pdf page/ {p=$0; n=NR} END{}' SOD_pages.txt; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<16849' | tail -3; echo \"==== 36090-36110 ====\"; awk 'NR>=36085 && NR<=36110' SOD_pages.txt; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<36095' | tail -2; echo \"==== 36735-36750 ====\"; awk 'NR>=36735 && NR<=36750' SOD_pages.txt",
 "description": "Print Sogdian dictionary context for knee entries"
}
```


### [2026-09-05T20:48:20.040Z] TOOL RESULT

```
         GMS 1245                                                     GMS 577, 907; Hen. Tales. 467, 41; AVS 98
4578 jYt>(h) M                                       <ii-U4>J
                                                                4588 jn> M                                              jj>
     zayda ©f. pp. =*jyt-                                            zna =>)zn,k(h), »zn\ pjn}(h), zn'kh
     kept                                                            knowledge
       BBB 727 a5; GMS 882, 884, 887; +wfiyy, 3sg.                   GMS 264, 1264; W-Li, ii, Gropp. p39; BBB 525;
         opt. pot. pass. Hen. Tales. 470, 58                           Tales. 473, 31
4579 jyw M                            WU^                       4589 jn'ptnym M                                    jjJuUjlj
     z(a)yu, zayu =^jwy-, 5ryw, zy-w, zy-w                           zna-patnem, zinapatnem        ^z^ptnym
            i in -: ii ■ i mium^^man^mmtmtmmmmammm
                                                                                                   mn

 jnwq

                                                                                                              184
                                                                   BBB 516; Hen. Cosm. 307.46; W-Li, Gropp. p39
        injunction
        BBB 64; Gersh. Sogd. Cpds. 138; Advice. 79ff
                                                             4601 jwky'mync      M                                   ^JU
 4590 jnwq => jnwwq                                               zukyamenc      (jwqy'mync)
 4591 jnwwq      M                                     y\j        safe, sound
                                                                   GMS    1103; BBB 516
        znuk   (z'nwk^, jnwq) ©Av. znu; Pahl. snwk
        knee
                                                             4602 jwqy'mync =* jwky'mync
        Sogdica. 49.8, 50 n p50, CMS 264, 978                4603 jwndty =* jwndyy/h
 4592 jt- M                                            O^j   4604 jwndyy/h      M                                        *xj
        zot ®<*jata ©pt. st. =»jyt-, zyt-3                        zwande
                                                                  living     (jywndyy, jwndty) ^jw'ndyCyX
        GcOstrike                                                   'zw'nt'k, zw'ntk, zwnty
        GMS 108, 577, 925; AVS 98; inf. jtyy, Hen.
---- page tag before 16849 ----
==== 36090-36110 ====
        BSTBL, Dhu. 266; SCE 14; GMS 122, 1117                  11153 zWntk B^ z>n>ntk
                                                                11154 zVnt sy- S, M, B                            o>J^y
11141 zfefin'k =» z>k6n»k                                             zanand say

11142 z}m B, S                   f>a*, ic^^r^Xj cC*J± <Sjl             (to)pzy attention
      zam ^zto
                                                                       GMS 550, 1066
        delicate, distinguished, respectable
                                                                11155 zWk        B                                       y\j
        Frag. Len. 91.3, 4, -y, 91.7; CII, 1990 Al, 10;
          Fll, 12, 13, 20 G6 285; TSP 19.9, 22                         zanuk    (z*nwq, z*nwk(>)) ©<*zdnuka ©ob. pi.

11143 z}m B                                     ^jp-tjkijb             knee
      zam ©<*6ram ^z'm, j*m                                            TSP 6.83, 2.1030, 7.21; VJ 97, 374, 1358; Frag.
      delicate                                                           4.8, S W, IIJ 1976, 46, BSTii 867.37: C2,
        TSP 3.175, 273, 287, 288, 5.24; Doc. X20; GMS;
                                                                           27V 12, 8; z}nwk sry, 56V26; Sogdica. 2
          Frag. Len. 91.3, 4, -y, 91.7
                                                                11156 z'nwq C =» zWwk
11144 zWsp S                                         ^UU-       11157 z}nwk()) *± zWwk, jnwwq
      jamasp ©pr. name
                                                                11158 zV      M, C                                     Jy>
      Jamasp
                                                                       zar ©*hazahra       =*z»r, NLPw(=lLP(w))
        Hen. JRAS 1944, 138.25, -w                                     thousand
11145 z'mn'k S                     o^l^/oy                             GMS 397, 399, 1316, 1329, 1674, 1676, 1677; C2,
==== 36735-36750 ====
                                                                11364 znw S                                              o*
           VJ pl23; TSP; BSTBL pl48; STii 9.9, 1.76; SCE
                                                                      z(i)nu ? ^zn'kh1, zyn'kh
             66, 531; Sund. AoFviii 1981, 21R8-9; Frag.
            Len. pi 13; znk*nw, Dhy. 255; "with numerals"             Hen. Tales. 483.13, 484 n 3; Gersh. Advice. p80
            "fold" GMS 1034, 1328; MSP                         11365 znwq M                            *j'jjT <*U- <j*Jj
    11352 znkp8*y S                                                  zanu(k) (znw, znyq) ©<*zanuka\ Skt. hanit;
                                               f-v>^ <oUI              =4 znw
          zanak-pa5e                                                   Parth. znx\ MP dnwg\ Pash. zana-y Bal. zanuk
          human, people
                                                                      chin, jaw
          MDii p94.5 n pi 02; Gersh. Advice. 86 f.
                                                                      GMS 375, 978; Sogdica. 49.7; STi 5.7; Sund.
            zana-pada
                                                                        AoFi 231; AoFiii 85.7
    11353 znkznk'n B                      ajUju^- <«0jf <ua
```


## [2026-09-05T20:48:42.062Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN dahan/zafar/zanax ===\"; grep -n \"dahān\\|dahan\\|zafar\\|zanax\\|zānū\\|zanu\" HRN.txt | head -40",
 "description": "Grep Horn for dahan, zafar, zanax"
}
```


### [2026-09-05T20:48:42.110Z] TOOL RESULT

```
=== HRN dahan/zafar/zanax ===
5280:aw. zafan-^ zafar- *Rachen ; phlv. dahün,
5864:aw. zafar- 'Rachen ; phlv. znfar,
5912:'Kinn' (LW.) (416); wa;<. zanax (i^W.) , si^'n. zingü,
20108:zanax 669.
```


## [2026-09-05T20:48:43.772Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== Watkins genu ===\"; grep -n -A6 \"^genu-1\\|^genu-2\\|genu-1\\.\\|genu-2\\.\\|^gep(h)\\|geph-\" AHD_watkins1985.txt | head -60",
 "description": "Grep Watkins AHD for genu roots"
}
```


### [2026-09-05T20:48:43.827Z] TOOL RESULT

```
=== Watkins genu ===
492:TION), GENERIC, GENEROUS, GENRE, GENUS; CONGENER, (CONGENIAL), DEGENERATE, (ENGENDER), MISCEGENA- TION; b. Greek genos and genea, race, family: GENEAL- OGY, GENOCIDE, GENOTYPE, HETEROGENEOUS; c. Greek suffix -genés, ‘‘-born’”: -GEN, -GENY. 4. Suffixed full-grade form *gen-yo- in: a. Latin genius, procreative divinity, inborn tutelary spirit, innate quality: GENIAL!, GENIUS; b. Latin ingenium (in-, in; see en), inborn character: ENGINE, INGENIOUS. 5. Suffixed full-grade form *gen-d- in Latin indigena (indu-, within; see en), born in (a place), indigenous: INDIGEN, (INDIGENOUS). 6. Suffixed full-grade form *gena-wo- in Latin ingenuus (in-, in; see en), born in (a place), native, natural, freeborn: INGENUOUS. 7. Suffixed full-grade form *gen- men- dissimilated in Latin germen, shoot, bud, embryo, germ: GERM, GERMAN?, (GERMANE), GERMINAL, GERMI- NATE. 8. Suffixed full-grade form *gena-ti- in Greek genesis, birth, beginning: GENESIS, -GENESIS. 9. Redupli- cated form *gi-gn- in: a. Latin gignere (past participle genitus), to beget: GENITAL, GENITIVE, GENITOR, GENT!, (GINGERLY); CONGENITAL, PRIMOGENITURE, PROGENI- TOR, (PROGENY); b. Greek gignesthai, to be born: EPI- GENE. 10. Suffixed zero-grade form *-gn-o- in Latin benignus (bene, well; see deu-?), good-natured, kindly, and malignus (male, ill; see mel-5), evil-natured, malevo- lent: BENIGN, MALIGN. 11. Zero-grade form *gna- becom- ing *gnda- in Latin praegnds (prae-, before; see per’), pregnant: PREGNANT!. 12. Suffixed zero-grade form *gna-sko- becoming *gnd-sko- in Latin gndsci, ndsci (present participle ndscéns, past participle gndtus, nd- tus), to be born: NAIVE, NASCENT, NATAL, NATION, NA- TIVE, NATURE, NEE, NOEL; (ADNATE), AGNATE, COGNATE, CONNATE, ENATE, INNATE, NEONATE, PUISNE, (PUNY), RENAISSANCE. 13. Suffixed o-grade form *gon-o- in Greek gonos (combining form -gonos), child, procre- ation, seed: GONAD, GONO-; ARCHEGONIUM, EPIGONE. 14. Zero-grade form *gn- in Sanskrit ja- in krmi-ja-, “produced by worms” (see k*rmi-). [Pok. 1. gen- 373.] genu-'. Knee; also angle. 1. Variant form *gneu- in: a. Germanic *knewam in Old English cnéo, knee: KNEE; b. Germanic *knewljan in Old English cnéowlian, to kneel: KNEEL. 2. Basic form *genu- in Latin genii, knee: GENICULATE, GENUFLECT. 3. Suffixed variant form *gon-ya- in Greek gdnia, angle, corner: -GON, GONION; AMBLYGONITE, DIAGONAL, GONIOMETER, GONIOMETRY, ORTHOGONAL. [Pok. 1. genu- 380.] genu-2. Jawbone, chin. 1. Form *genw- in Germanic *kinnuz in Old English cin(n), chin: CHIN. 2. Basic form *genu- in Greek genus, chin: GENIAL. 3. Suffixed variant form *gna-dho- in Greek gnathos, jaw: GNATHIC, -GNATHOUS; CHAETOGNATH 4, Variant form “g(h)enu- in Sanskrit hanu, jaw: HANUMAN. [Pok. 2. genu- 381.] gep(h)-. Also gebh-. Jaw, mouth. 1. Probably Germanic *kaf-, to gnaw, chew, in Old English ceaf, husks, chaff: CHAFF!, 2. Germanic *kabraz, “gnawer,” in Old English ceafor, ceafer, beetle: CHAFER; (COCKCHAFER). 3. Ger- manic *kéfalaz in Old English céafl, jaw, cheek: JOWL!. [Pok. geph-, gebh- 382.] ger-'. To gather. 1. Extended form *grem- in Germanic *kram- in Old English crammian, to stuff, cram: CRAM. 2. Reduplicated form *gre-g- in Latin grex (stem greg-), herd, flock: GREGARIOUS; AGGREGATE, CONGREGATE, EGREGIOUS, SEGREGATE. 3. Earliest forms “ager-, *ggor-d-, in Greek ageirein, to assemble, and aguris, agora, marketplace (> agoreuein, to speak): AGORA}; (AGORAPHOBIA), ALLEGORY, CATEGORY, PANEGYRIC. [Pok. 1. ger- 382.] ger-2. Curving, crooked; hypothetical Indo-European base for a variety of Germanic words with initial kr-. I. Words meaning to bend, curl; bent, crooked, hooked; something bent or hooked. 1. Germanic *krdpp6n-, a hook, especially one used in harvesting grapes, in: a. Old High German krapfo, a hook: AGRAFFE; b. Old French graper, to harvest grapes, hence (back-formation) grape,
493-gerbh-
494-vine, grape: GRAPE; c. Old French grapon, grapnel: GRAPNEL; d. Old French grape, a hook: GRAPPLE; e. Ital- ian dialectal grappa, vine stem, brandy: GRAPPA. 2. Old English crump, crumb, crooked, bent, stooping: CRUM- MIE, CRUMPET, (CRUMPLE). 3. Low German krimpen, to wrinkle: CRIMP!. 4. Middle Dutch crampe, hook, and Frankish *kramp, hook: cramMpP?. 5.Old High German krampfo, a cramp, akin to the Germanic source of Old French crampe, cramp: CRAMP!. 6. Old English crypel, a cripple: CRIPPLE. 7. Germanic *kreupan in Old English créopan, to creep: CREEP. 8. Middle Low German krink, a ring: CRINGLE. 9. Germanic *krengan in Old English cringan, to yield: CRINGE. 10. Middle Dutch crinkelen, akin to Middle English crinkelen, to make kinks in: CRINKLE. 11. Old Norse kriki, a bend, nook: CREEK. 12. Old Norse krékr, a hook: cRooOK. 13. Frankish *krok- (> Old French croc), a hook: CROCHET, (CROCKET), (CROQUET), (CROUCH); ENCROACH. 14. Old English crycc, (bent) staff, crutch: CRUTCH. 15. Old French crosse, crook: CROSIER, LACROSSE. 16. Middle Dutch crulle, curly: CRULLER, CURL. 17. Old English cranc-(stzf), a weaving implement: CRANK}. 18. Norwegian krake, a sickly beast, akin to the source of Middle English crok, an old ewe: cRocK3, 19. Old Norse karpa, to boast: CaRP!, 20. Middle Dutch kroes, curled, akin to the source of Old French grosele, gooseberry: GROSSULARITE. II. Words meaning ‘“‘a rounded mass, collection; a round object, vessel, container.” 1. Old English cruma, a frag- ment: CRUMB. 2. Frankish *kruppa, rump, akin to the Germanic source of Old French croup, rump: CROUP?, (CROUPIER), CRUPPER. 3. Old English cropp, cluster, bunch, ear of corn: crop. 4. Italian gruppo, an assem- blage: Group. 5. Old English crocc, pot: CROCK}. 6, Mid- dle Dutch cruyse, pot: CRUSE. 7. Old English cribb, manger: CRIB. 8. Old English cradel, cradle: CRADLE. 9. Frankish *kripja, cradle, akin to the Germanic source of Old French cre(s)che, crib: CRECHE. 10. Old English creet and Old Norse kartr, wagon: CART. 11. Old English croft, small enclosed field: crort. [Pok. 3. ger- 385.] gerbh-. To scratch. 1. Germanic *kerban in Old English ceorfan, to cut: CARVE. 2. Zero-grade Germanic form *kurbiz in Old English cyrf, a cutting (off): KERF. 3. Variant form *grebh- in: a. Germanic *krab(b)- in Old English crabba, a crab: CRAB}; b. Germanic *krabiz- in Old French crevise, crayfish: CRAYFISH; C. perhaps Ger- manic *krab- in Old Norse krafla, to crawl: CRAWL. 4. Zero-grade form *grbh- in Greek graphein, to scratch, draw, write, and gramma (< *grbh-mn), a picture, writ- ten letter, piece of writing, and grammé, a line: GRAF- FITO, GRAM!, -GRAM, GRAMMAR, GRAPH, -GRAPH, -GRAPHER, GRAPHIC, -GRAPHY; AGRAPHA, AGRAPHIA, DIAGRAM, EPIGRAM, (EPIGRAPH), GRAPHITE, ICONOGRA- PHY, PARAGRAPH, PROGRAM, PSEUDEPIGRAPHA, TETRA- GRAMMATON, TOPOGRAPHY. [Pok. gerebh- 392.] [gerere. To carry, carry on, act, do. Latin verb of un- known origin. Oldest form ges-, past participle gestus. GERENT, GERUND, (GEST), GESTATION, (GESTICULATE), GESTURE, JEST; ARMIGER, BELLIGERENT, (CONGERIES), CONGEST, DIGEST, EGEST, INGEST, REGISTER, SUGGEST, VELIGER.] gere-'. To grow old. 1. Suffixed lengthened-grade form *géro-s- in Greek géras, old age: AGERATUM, CALOYER, GERIATRICS. 2. Suffixed form “gera-ont- in Greek geron (stem geront-), old man: GERONTO-. [Pok. ger- 390.] gere-2. To cry hoarsely; also the name of the crane. I, Words meaning “‘to cry hoarsely”; also words denoting the crow. 1, Germanic *kré- in: a. Old English crawe, a crow: CROW}; b. Old English crdwan, to crow: CROW?; c. Old English cracian, to resound: CRACK; d. Middle Dutch krdken, to crack: CRACKNEL; @. Old Norse kraka, a crow: CRAKE. f. Middle Dutch krdnen, to groan, la- ment: CROON. 2. Possibly (but more likely imitative) Germanic *kur(r)- in Old Norse kurra, to growl, akin to Middle English curre, cur: cur. II. Words denoting a
495-20
496-ghait-
497-crane. 1. Germanic *kran-, crane, in: a. Old English cran, crane: CRANE; b. Middle Low German kran, crane: CRANBERRY. 2. Extended form *grd- in Latin griis, crane: GRUS; PEDIGREE. 3. Suffixed variant form *gra-k- in Latin grdculus, jackdaw: GRACKLE. 4. Suffixed ex- tended form *gero-no- in Greek geranos, crane: GERA- nium. [Pok. 2. ger- 383.]
498-géu-. To bend. Proposed by some as the root of Greek guros, ring (which is more likely of unknown origin): GYRE, GYRO?, GYRO-; AUTOGIRO. [Pok. géu- 393.]
```


## [2026-09-05T20:49:01.824Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== 5265-5295 ===\"; sed -n '5265,5295p' HRN.txt; echo \"=== 5850-5925 ===\"; sed -n '5850,5925p' HRN.txt",
 "description": "Print Horn context for dahan, zafar, zanax"
}
```


### [2026-09-05T20:49:01.887Z] TOOL RESULT

```
=== 5265-5295 ===
aw. dasa zehn', dasema-; phlv. dahuw; ai. r/ara,
dafamci-; arm. ^as« *zehn' (H. No. 270).
kurd. bei. LW. deh, dah; afj'. las; oss. d. t. das,
däsäm (106); wa/. das^ las, sar. dh, sij'n. J7s, te,
ya;ai. sangl. das, minj. LW. daÄ.
588. dih *Dorf*, vergl. dihgän (arab. LW. dihqän, arm.
LW. dehkan),
ap. dahyU' Xand'; aw. da/yii-; phlv. rfiA bezw. dcA,
da/yulpatj daxyu\paüh (arm. LW. dehpef), vergl. adihlk,
ttzdihtk; ai. ddsyu-,
kurd. daw; af/. LW. rfzA; bei. LW. d^A, dcÄ (58).
Die ursprüngliche np. Aussprache w^ird deh gelautet
haben.
589. dehän, dehen *Mund', dehün *Gedächtniss, Stegreif*,
dehane, dehne 'Zaum, Gebiss •^).
aw. zafan-^ zafar- *Rachen ; phlv. dahün,
kurd. LW. däw^ dan; bei. LW. dt/jp, n. daf (71).
Die kurdischen und 'bei. Formen däw bezw. dap,
daf sind augenscheinlich ziemlich alte Lehnworto.
590. dT, dtg 'gestern', :m (Is. 30, 33), dme, diröz^ dlseh.
Käs. ez6, heze; ezjind gestrig'; eze^soi^ eze]sÖ.
ai. hyds gestern; phlv. dik (PP61.) ^).
kurd. LW. 8cSve]dl gestern Abend'; oss. d. azine,
äzinä, t. znofi, zinon gestern' (11); bei. zlk^ zi (427);
wa/. yez.
Das eze etc. der Dialekte von Kasan ist sehr in-
teressant.
*) Firdüsi reimt aber das Wort auf est (Sahn. I, 205 Anm. S
Calc).
') Firdüslfliat aus metrischen Gründen bisweilen auch däh.
«) Yergl. siiukoYski s. v. dehne (S. 129).
=== 5850-5925 ===
LW. kurd. zirt, zir/ * Panzer ; af;'. zira; bei. zirili
(306); arm. zrah.
Urverwandt mit afy. zyara * Kettenpanzer', oss. zyär
Tanzer (132) ?
%l, liieryiin gelbfarbig.
aw. zairi.gaona- gelbfarbig'; phlv. vergl. zarlnqün
(vd. 2 (67)).
Vergl. np. öün aus *cigün (No. 450) und aöenjiin,
G62. »ist 'schlecht, schimpflich*, zistür.
Kää. Z. jist (auch s. v. bed).
aw. jlstayamna- (y. 8, 3) Verachtend, vorspottend'
(Geldner, 3 Yasht, 128ji); phlv. zist 'hässlich' (Men.).
af/. LW. zl/t; sar. ir^ Verdorben, schlecht, hässlich'.
663. zefer, zefr *Mund' (8ähn. I, 195, 1189).
aw. zafar- 'Rachen ; phlv. znfar,
Muss dialektisch sein, da die reguläre Form np.
dehan (No. 589) ist.
664. i^elTi, zalü 'Blutegel', zerü (AM. 180 Zeile 2 v. u.).
skr. LW. (?) Jalüka-, jaluka-, Jalikä- 'Blutegel*
(Bütticher, Arica 67).
kurd. zdü, zuliil, zalüg, zürT; af/. LW. zallü 'Blut-
egel', echt zavara\ bei. zaray (417).
Gegen Curtius' Zusammenstellung mit lat. hirüdö,
air. gil vergl. Hübsch mann, ZDMG. 38, 424.
665. zelle^ ziUe 'Grille, Heimchen'.
skr. jhillikCL', jhillU Grille, Heimchen' (Hübsch-
mann, ZDMG. 38, 424).
666. xeni 'Kälte', zemistan 'Winter.
aw. zyao- 'Winter', Gen. ziniö; phlv. zam 'Winter'
(vd. 2 (20)), zam(i)stan; ai. himä- 'Winter ; arm. vergl.
jiun 'Schnee', jmern 'Winter', jmerem 'überwintern
(H. No. 178).
oss. d. zumägy t. zimag 'Winter' (135); af/. zimai;
wa;^. zam, zamin (Adj.), sar. zainän, zamämn (Adj.),
si/n. zimjy zinj 'Schnee'.
) vt. 19, 42 ]int die neuo AuRfj^abe harözuiiem.
10*— 148 —
Daneben auch allgemein entlehnt, kurd. afy. zamistän,
bei. zamisiän, :^imisfän, zavistän (414), sar. zümistän,
yidg. zemistän.
Die Pazendlesung damistan ist belanglos und falsch
wie päz. damik statt zamtk (np. zemin).
667. ;s;emi: (Öähn. I, 134 Anm. 4, 178 Vers 877)'), zemm
*Erde.
ap. uzmaya[patiy ; aw. ^^äo 'Erde', Gen. zemö; phlv.
zamlk; ai. //wtt- auf der Erde'.
af/. zmaka 'Erde*; oss. d. zän/ä, t. zä/ (127); sar.
zems, siyn. zemc,
LW. bei. zamtk 'Felder, Saaten' (415); ausserdem
ist np. zemm^) allgemein entlehnt (vergl. bei. No. 298).
668. ^en *Weib'; zenber 'Sänfte''-).
g. Jen (Vullers sen, Asteräbäd); Käs. K. zen, Jen,
Jin, Z. mn,
aw. Jeni- (y. 53, 6), Jaini- (y. 10, 17) *Weib'; phlv.
zan; ai. Jäni-, Jäm- 'Weib, Gattin'; arm. kiu 'Frau'
(H. No. 144).
kurd. 2in 'Weib' (zaza Jev); af/. Jinat, JünaJ; bei.
Jan (174) ; si;'n. yin, sar. yJw, ;^m, niinj. zinga.
669. jSJ^^icx 'Kinn', zene/dän,
ai. Äaww- 'Kinn'; aw. zanva- (Geldnor, KZ. 30,
514); arm. cnaut Kinnbacke, Wange (H. No. 137).
af}'. LW. zana, zana/; bei. zanük, zanlk, n. zatm/
'Kinn' (LW.) (416); wa;<. zanax (i^W.) , si^'n. zingü,
sar. zangän,
670. ^eii<J gross, stark', vergl. zende plV),
aw. vergl. /ra]^«^^«-; phlv. zand[])tl (PPGL); ai.
vergl. Jantü- 'Geschöpf, Wesen, Mensch'; lat. gern, (?)
V
*3 Vergl. np. äsfl neben äsitn (Sahn. I, 177 Vers 874), ähenl (häre)
Sahn. I, 187 Vers 1054 neben ahemn (bare), Hahn. I, 39 Vers 96.
*) C'^'utjv (Glossator zu Mich. Psellus, de Lagarde Ges. Abh. 222)
ist direct das moderne np. zennn.
3) Arm. LW. zafwar (Hubs eh mann, ZDMG. 35, 134, No. 40).
*) Sputer mit Angleichiing an zhnle Mebondig* zhifle pil go-
sp rochen.149
Der Bedüutungsunterschied macht diese Zusammen-
```


## [2026-09-05T20:49:21.481Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN jowl ===\"; grep -n \"jowl\" KLN_1966.txt | head -10; echo \"=== KLN chafer ===\"; grep -n \"^chafer\\|chafer,\" KLN_1966.txt | head -10",
 "description": "Grep Klein for jowl and chafer"
}
```


### [2026-09-05T20:49:21.552Z] TOOL RESULT

```
=== KLN jowl ===
7112:chafe  with  agential  suff.  -er.  Cp.  chauffer, chafer,  n.,  a  beetle.  —  ME.,  fr.  OE.  ceafor,  rel. to  OS.  kevera,  Du.  kever,  OHG.  chevar,  MHG. kever,  G.  Kdfer,  lit.  ‘gnawer’.  Cp.  MHG.  kiven, Du.  keveren,  ‘to  gnaw’,  OE.  ceafl,  ME.  chavel, G.  Kiefer,  ‘jaw’,  and  see  jowl,  ‘jaw’, chaff,  n.,  husk  of  grain.  —  ME.  chaf  fr.  OE.  ceaf rel.  to  MDu.,  Du.  kaf  G.  Kaff,  and  prob.  also to  OHG.  cheva,  MHG.  keve,  ‘husk’. Derivatives:  chaff,  tr.  v.,  chaff-y,  adj. chaff,  tr.  v.,  to  banter.  —  Prob.  a  var.  of  chafe, chaffer,  n.,  a  bargain.  —  ME.  cheapfare,  chapfare, chaffare,  fr.  OE.  ceap,  ‘price,  bargain’  and  faru, ‘going,  journey,  proceeding’.  For  the  first  ele¬ ment  see  chapman,  cheap,  for  the  second  see fare.
20198:‘to  cram,  gorge’,  OProven?.  gava,  ‘crop,  maw’ ; prob.  influenced  in  form  by  jowl.  Cp.  jabot.
20399:jowar,  jowari,  jowarree,  n.,  millet,  durra  (India). —  Hind,  jawar,  jodr,  judr,  prob.  fr.  OI.  ydva- akara-,  ‘of  the  nature  of  barley’, jowl,  n.,  jaw.  —  ME.  chawl,  chavel,  cholle,  fr.  OE. ceaft,  ‘jaw’,  rel.  to  MHG.  kiver,  kivel,  G.  Kiefer, ON.  kjaptr,  ‘jaw’,  and  cogn.  with  OIr.  gop,  Ir. gob,  ‘beak,  mouth’,  Avestic  zafar1,  ‘mouth, gullet’.  Cp.  chafer,  ‘beetle’, joy,  n.  —  ME .joye,  fr.  OF .joie.joye  (F.joie),  fr. L.  gaudia,  pi.  of  gaudium,  ‘joy’  (but  mistaken for  a  fern,  singular  noun),  which  is  rel.  to  gau- dere,  ‘to  rejoice'.  See  gaud  and  cp.  enjoy.  Cp. also  feu  de  joie,  rejoice.
=== KLN chafer ===
7111:Derivatives:  chafe,  n.,  chafer  (q.v.) chafer,  n.,  a  vessel  for  heating.  —  Formed  fr.
7112:chafe  with  agential  suff.  -er.  Cp.  chauffer, chafer,  n.,  a  beetle.  —  ME.,  fr.  OE.  ceafor,  rel. to  OS.  kevera,  Du.  kever,  OHG.  chevar,  MHG. kever,  G.  Kdfer,  lit.  ‘gnawer’.  Cp.  MHG.  kiven, Du.  keveren,  ‘to  gnaw’,  OE.  ceafl,  ME.  chavel, G.  Kiefer,  ‘jaw’,  and  see  jowl,  ‘jaw’, chaff,  n.,  husk  of  grain.  —  ME.  chaf  fr.  OE.  ceaf rel.  to  MDu.,  Du.  kaf  G.  Kaff,  and  prob.  also to  OHG.  cheva,  MHG.  keve,  ‘husk’. Derivatives:  chaff,  tr.  v.,  chaff-y,  adj. chaff,  tr.  v.,  to  banter.  —  Prob.  a  var.  of  chafe, chaffer,  n.,  a  bargain.  —  ME.  cheapfare,  chapfare, chaffare,  fr.  OE.  ceap,  ‘price,  bargain’  and  faru, ‘going,  journey,  proceeding’.  For  the  first  ele¬ ment  see  chapman,  cheap,  for  the  second  see fare.
7279:chauffer,  n.,  a  portable  stove.  —  Prob.  a  blend of  F,  chauffoir,  ‘a  heater’  (fr.  chauffer,  ‘to  heat’), and  E.  chafer,  ‘a  vessel  for  heating’  (q.v.) chauffeur,  n.,  driver  of  a  motor  car.  —  F.,  orig. ’heater,  fire  man,  stoker’,  fr.  chauffer,  ‘to  heat’. See  chafe  and  cp.  chauffer,  rechauffe. Derivative:  chauffeur,  intr.  and  tr.  v. Chaumontel,  n.,  a  variety  of  pear.  —  Named  from Chaumontel,  a  village  in  the  Department  of Seine-et-Oise  in  France.
8074:tryse,  cocatrice,  fr.  OF.  cocatris  (F.  cocatrix), ‘a  fabulous  serpent’,  fr.  Late  L.  calcatrix, ‘treader,  tracker’,  fr.  calcare,  ‘to  tread’;  see calk,  ‘to  stop  with  oakum’.  OF.  cocatris  was influenced  in  form  by  OF.  coc,  ‘cock’.  Late  L. calcatrix  is  a  loan  translation  of  Gk.  lyvcuptov, ‘ichneumon’,  lit.  ‘tracker’,  fr.  c/vo?,  ‘track’, cockboat,  n.,  a  small  boat,  esp.  one  used  as  a tender.  —  ME.  cokbote,  fr.  cok,  ‘cockboat’,  and bote,  ‘boat’.  The  first  element  derives  fr.  OF. coque,  cogue  (F.  coche),  ‘a  kind  of  boat’,  fr.  Late L.  caudica,  ‘a  kind  of  boat',  lit.  ‘a  boat  made from  the  trunk  of  a  tree’,  fr.  L.  caudex,  gen. caudicis,  ‘trunk  of  a  tree’.  See  caudex.  OF.  coque, cogue,  were  influenced  in  form  by  MDu.  cogghe. Cp.  coxswain.  Cp.  also  cog,  ‘a  small  fishing  boat’. For  the  second  element  in  ME.  cokbote  see  boat, cockchafer,  n.  —  Compounded  of  cock,  the  bird, and  chafer;  so  called  from  its  large  size, cocker,  tr.  v.,  to  pamper.  —  Formed  with  sulf. -er  fr.  obsol.  cock,  ‘to  make  a  nestle  cock  of’. See  cock,  the  bird.  For  sense  development  cp. OF.  coqueliner,  ‘to  pamper’,  fr.  coq,  ‘cock’, cocker,  n.,  quiver  (obsol.)  —  ME.  coker,  ‘quiver, boot’,  fr.  OE.  cocur,  cocer,  rel.  to  ODu.  cocar, MDu.  coker,  Du.  koker,  OHG.  kochar,  kochdri, MHG.  kocher,  kochtere,  G.  Kocher,  “quiver’. These  Teut.  words  are  connected  with  ML.  cu- curum,  MGk.  xouxoupov,  whence  Russ,  kukor, ‘cartridge  box’.  Cp.  quiver,  ‘a  case  for  arrows’, cocker,  n.,  also  cocker  spaniel.  —  Formed  fr. cock,  the  bird;  so  called  because  originally  used for  hunting  wood  cock.
20399:jowar,  jowari,  jowarree,  n.,  millet,  durra  (India). —  Hind,  jawar,  jodr,  judr,  prob.  fr.  OI.  ydva- akara-,  ‘of  the  nature  of  barley’, jowl,  n.,  jaw.  —  ME.  chawl,  chavel,  cholle,  fr.  OE. ceaft,  ‘jaw’,  rel.  to  MHG.  kiver,  kivel,  G.  Kiefer, ON.  kjaptr,  ‘jaw’,  and  cogn.  with  OIr.  gop,  Ir. gob,  ‘beak,  mouth’,  Avestic  zafar1,  ‘mouth, gullet’.  Cp.  chafer,  ‘beetle’, joy,  n.  —  ME .joye,  fr.  OF .joie.joye  (F.joie),  fr. L.  gaudia,  pi.  of  gaudium,  ‘joy’  (but  mistaken for  a  fern,  singular  noun),  which  is  rel.  to  gau- dere,  ‘to  rejoice'.  See  gaud  and  cp.  enjoy.  Cp. also  feu  de  joie,  rejoice.
```


## [2026-09-05T20:49:23.609Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in BQT_v1_pages.txt BQT_v2_pages.txt ../refs/incoming/BQT/BQT_v3_pages.txt; do echo \"== $f\"; grep -o \"\\[pdf page [0-9]*\\]\" $f | head -2; grep -o \"\\[pdf page [0-9]*\\]\" $f | tail -2; done 2>/dev/null; echo; echo \"=== زانو in v2 ===\"; grep -n \"زانو\" BQT_v2_pages.txt | head -5",
 "description": "Check BQT page coverage"
}
```


### [2026-09-05T20:49:25.511Z] TOOL RESULT

```
== BQT_v1_pages.txt
== BQT_v2_pages.txt
== ../refs/incoming/BQT/BQT_v3_pages.txt
[pdf page 1]
[pdf page 2]
[pdf page 720]
[pdf page 721]

=== زانو in v2 ===
736:  ‫مزع < ‪ .4‬اورامان‪ »۲۲۱‬کیلکی ‪ 02‬ابن‌سینا جان‌را بمعنی‌شی بادکرده ‪ *:‬دیگر ( ازانواع‬
6225:                           ‫( بزانوشتن) ‪.‬رك ‪ :‬چوك ‪.‬‬        ‫‪ ۵‬درتر کی آذری ‪kam‬‏ ‪60 -‬‬
7526: ‫و زانوزدن‌شترراخصوصا وامربزانو زدن هم‌هست‬                                                                        ‫انداز ند ‪.‬‬
7544:  ‫تناسل‪ -‬وخم کردن زانو ‪ -‬ومز گان ‪ -‬ولوله ‪ .‬وفنات است«جفتابی ‪ ۹۹۲‬درمتنسه معنی‌اول آمده‪.‬‬
7558:‫وآن درتدهأ ست تامبارك و ددوسته در‬                    ‫کون‬           ‫بعنی‌بزانودرای ‪ .‬گوبند باین‌معنی ترکی‌است‪. ۱‬‬
```


## [2026-09-05T20:49:49.803Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in BQT_v1_pages.txt BQT_v2_pages.txt; do echo \"== $f\"; python3 -c \"\nimport sys\nt=open('$f',encoding='utf-8',errors='replace').read()\nprint('formfeeds', t.count(chr(12)))\nimport re\ntags=re.findall(r'\\[[^\\]]{0,30}page[^\\]]{0,20}\\]', t)[:5]\nprint(tags)\nprint(len(t))\n\"; done; echo; python3 /home/sfmqrb/git/rishe/tools/ref_page.py --help 2>&1 | head -30",
 "description": "Inspect BQT page files and ref_page tool"
}
```


### [2026-09-05T20:49:51.577Z] TOOL RESULT

```
== BQT_v1_pages.txt
formfeeds 776
[]
1285412
== BQT_v2_pages.txt
formfeeds 683
[]
2900526

Fetch ONE cited page of a scanned reference, on demand.

    python3 tools/ref_page.py BQT:918          # printed page 918 of Borhan-e Qate'
    python3 tools/ref_page.py IRN:119 --image  # also print the path of the page image
    python3 tools/ref_page.py BQT:918 --pdf-page 375   # override the offset mapping

Looks up the reference in data/verification/sources/refs_online.json
(`scans`: list of {file, first_printed, last_printed, pdf_offset, lang}), renders the
matching PDF page to PNG (for reading with a vision model), OCRs it with tesseract in
the reference's language(s), caches both under
data/verification/sources/refs/ocr/<ABBR>/<printed page>.{png,txt}, and prints the
OCR text. Only the cited page is ever processed — never the whole book.

`pdf_offset` means: pdf page index (1-based) = printed page + pdf_offset.

If the OCR is too poor and you transcribe the relevant passage(s) from the PNG yourself,
save that transcription as <printed page>.vision.txt next to the .txt; from then on this
tool prints the transcription instead of the OCR, so no page is ever read twice.
```


## [2026-09-05T20:49:55.744Z] TOOL CALL #21: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/ 2>/dev/null; ls data/verification/sources/refs/ocr/BQT 2>/dev/null | head -40; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nprint(json.dumps(d.get('scans'),ensure_ascii=False,indent=1))\"",
 "description": "Check BQT scan config and OCR cache"
}
```


### [2026-09-05T20:49:57.686Z] TOOL RESULT

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
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1225.png
1225.txt
1225.vision.txt
1275.png
1275.txt
1339.png
1339.txt
1357.png
1357.txt
1382.png
1382.txt
1385.png
1385.txt
1385.vision.txt
1445.png
1445.txt
1445.vision.txt
1452.png
1452.txt
1455.png
1455.txt
1462.png
1462.txt
1471.png
1471.txt
1472.png
1472.txt
1488.png
1488.txt
1492.png
1492.txt
1624.png
1624.txt
172.vision.txt
1776.png
[
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
]
```


## [2026-09-05T20:50:06.623Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['BQT_v1_pages.txt','BQT_v2_pages.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    pages=t.split('\\f')\n    print('==',f,'chunks',len(pages))\n    for w in ['زانو','دهان','زنخ','زنخدان','زفر']:\n        hits=[i+1 for i,p in enumerate(pages) if w in p]\n        print(' ',w,hits[:15], '...' if len(hits)>15 else '', 'n=',len(hits))\nEOF",
 "description": "Locate BQT headwords by chunk"
}
```


### [2026-09-05T20:50:08.318Z] TOOL RESULT

```
== BQT_v1_pages.txt chunks 777
  زانو [24, 25, 100, 255, 587, 633, 771]  n= 7
  دهان [24, 41, 55, 58, 69, 76, 79, 138, 221, 244, 250, 252, 264, 282, 292] ... n= 49
  زنخ [97, 281, 596, 700, 744]  n= 5
  زنخدان []  n= 0
  زفر [18, 24, 25, 43, 51, 56, 62, 65, 79, 97, 107, 111, 125, 138, 143] ... n= 26
== BQT_v2_pages.txt chunks 684
  زانو [17, 108, 129, 130, 184, 219, 463]  n= 7
  دهان [14, 15, 21, 72, 80, 100, 101, 115, 132, 144, 155, 166, 168, 206, 212] ... n= 47
  زنخ [21, 77, 321, 499, 559, 632, 655]  n= 7
  زنخدان [77]  n= 1
  زفر [38, 39, 62, 87, 234, 235, 294, 344, 352, 394, 432, 458, 468, 487, 490] ... n= 21
```


## [2026-09-05T20:50:16.405Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in [1,2,77,108,129]:\n    p=t[i-1]\n    print('=== chunk',i,'len',len(p))\n    print(p[:600].replace('\\n',' | '))\n    print('---tail---')\n    print(p[-300:].replace('\\n',' | '))\nEOF",
 "description": "Inspect BQT v2 chunks"
}
```


### [2026-09-05T20:50:18.171Z] TOOL RESULT

```
=== chunk 1 len 0

---tail---

=== chunk 2 len 553
                                         ‫‪7‬‬ |  |                           ‫رن‪۳‬‬ |     ‫نات‬ |       ‫ا م‬ |               ‫لض‌بال ‪ ۰ ۲۶‬رک‬ | ‫‪۱‬‬       ‫اسا تعدولیدیارتم و‬ |                                      ‫‪7‬‬ | ‫‪ ۰‬و زل رسوا »وا روون لات سا روصا مواقم‬      ‫وتان‬ |  |                       ‫‪۴2 ۱‬‬ |  |                   ‫رک یمن‬ |                   ‫م سارو کی و ررك‬ |  |  |                  ‫جلررومدا‬ |              ‫چاپ دوم فروردین ‪۳۴۳۱‬‬ |                  ‫با تجدید نظر کامل‬ |           ‫بسرمایه کتابفروشی ابن سیتناپران‬ |  |  |  |  |                    ‫چاپ افست رشدبه‬ | 
---tail---
م‬      ‫وتان‬ |  |                       ‫‪۴2 ۱‬‬ |  |                   ‫رک یمن‬ |                   ‫م سارو کی و ررك‬ |  |  |                  ‫جلررومدا‬ |              ‫چاپ دوم فروردین ‪۳۴۳۱‬‬ |                  ‫با تجدید نظر کامل‬ |           ‫بسرمایه کتابفروشی ابن سیتناپران‬ |  |  |  |  |                    ‫چاپ افست رشدبه‬ | 
=== chunk 77 len 5263
 ‫‏‪ ٩‬مس‬                                                                                                            ‫چاءآبی کنود‬ |  ‫کنابه از دنا باشد =‬                 ‫چاه دلو د‬                             ‫وجریی بشرخوانند ‪٩‬‏ ‪ -‬وکوی زنخدان خوبانرا‬ | ‫کونابه از برح دلوهم هت که یکی از دوازده‬                                                              ‫نیزجطریق استماره گفتماند ‪-‬‬ |                                        ‫‪۹‬‬   ‫فلکی است‬          ‫ردج‬ |                                                                            ‫‪ - ۴‬بااف و ون ‪.‬‬                 ‫وید‬ |                 
---tail---
ی بر روی بسته داشتیو دعوی‌خدایی کردی‪....‬‬ |                                                                                       ‫د‬ |  ‫و زاین سب اورا مقنم خواندندی و آنت که چاه ساخت بحکمت و سیماب در آن ربخت با‬ |              ‫حرهٌ ‪٩۱٩‬‏‬ |                      ‫فد‬‫صیه‬ |                          ‫بق‬ | 
=== chunk 108 len 3942
                                                                                            ‫]‪0‬‬ |  | ‫لب ازچهارجااب بجول باد که آنرا‬ |                              ‫جلابك‬ |                                  ‫او‬                     ‫زخمتيغوصدایی که‌ازچیزی برآبدهمچوشکستن‬ | ‫دزد همگوبند ‪ -‬و کردکانی که مخزآن باسالی‬                 ‫چوب ولی وخوردن چیزی برچیزی وامثال‌اینها‪-‬‬ | ‫برنباید ‪ -‬و بمعتی صف ربع هم هست که من‬                   ‫وسخن را لیزگوبند چه چکدان بمعنیمخندان‬ |                             ‫باشد یعنی هشت بك ‪.‬‬         ‫باشد ‪ -‬و بمعنی قطره ‪٩‬‏ ‪ -‬و چکیدن هم‌هست‪.‬‬ | ‫چکا چا" ‪ -‬تح ا
---tail---
 تساهک لصا‬ |    ‫باشد وارجاع بکتاب ‪ (8. 8610۳8۳1_0015,76]1121‬رکه‪ :‬ماآخذ کتاب حاض)ص*‪ ۱۵‬کردمامت‪.‬‬ |   ‫درصفحة مزبور اکزتاب اخبر جح از«چاو» چینی امت که در‪-‬ال ‪ . «۳۹۹‬بابران‌رسیده درصورتیکه‬ |                                       ‫فردوسی(هتوفی‌بین‪ )۱۱4-۹۱‬چك را استعمال کرده است‪ .‬رك‪:‬چاو ‪.‬‬ | 
=== chunk 129 len 5178
 ‫=‬                                                                                                                   ‫جور‬ |  |  |  ‫چوده ر با »رباای‌قرشت وبایابجد‬                                    ‫‪ -‬سوتیزه کردن هم‬            ‫دن‬ |                                                                                                 ‫یمنی‬ |                                                                                                    ‫شبم‬ |                                                                                                      ‫کگرو‪-‬و‬ |                                                
---tail---
اب طبری ‪6۰۳٩‬‏ درعربی «شیق ‪۰‬‬ |                                                                         ‫سر ذکر وآلت مرد است » «شرح قاموس؛ ‪.‬‬ |                                                               ‫‪.‬‬    ‫جوزه »> سحوحه‬   ‫چوزه‬   ‫رك‬   ‫‪-‬‬   ‫جوزه‬       ‫‪#‬‬ |  |   ‫(برهان قاطعم‪)۹۸‬‬ |
```


## [2026-09-05T20:50:50.875Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,label in [(463,'BQT:1000 zanu'),(487,'BQT:1024 zafar'),(499,'BQT:1036 zanax')]:\n    p=t[i-1]\n    print('='*20, label, 'chunk',i,'len',len(p))\n    for ln in p.split('\\n'):\n        s=ln.strip()\n        if any(w in s for w in ['زانو','زفر','زنخ','اوستا','پهلوی','ژ','سنسکریت','هند','فارسی باستان']):\n            print('  >',s[:300])\nEOF",
 "description": "Extract BQT pages 1000, 1024, 1036"
}
```


### [2026-09-05T20:50:52.561Z] TOOL RESULT

```
==================== BQT:1000 zanu chunk 463 len 4568
  > ‫زانو رصد اه کردن = کنابه‬                                              ‫و دامفرشتها‪.‬ست که‬      ‫وهشتم‌است ازماهپای شمسی‪-‬‬
  > ‫وزانو کرصرددن‌هم هت که بی کلمة گاهباشد‪.‬‬                               ‫حوران بپشتی لیزمامور است‪ .‬کوبند در این روز‬
  > ‫درجهانگیری نز همن معتی آ مده است ‪.‬‬‫و‬      ‫‪:‬اتز‪.‬‬‫‪۴‬الد ژ‬ ‫ر‬      ‫«ثایتی ‪. ۶۸۱‬‬
  > ‫‪ #‬زالو ‪ -‬م سوم ‪ .‬پپلوی ‪ 10۳82‬از ابرانی باستان ‪ » # 361-1۳22-‬هندی‬
  > ‫باستان ‪ . [0104 -‬در اوستا ‪ 11032 -‬برخلاف شایدبمعنی (چانه) است ‪ ۳‬رك ‪ ۱‬بارتولمه ‪۹۸-۰‬‬
  > ‫در بعض نخ خطی پهلوی ‪kW‬‏ ‪ kûnhs = hs‬آمده‪ ,‬از اوستا _ ‪unhs , ۷05‬‏ ( (‪jy‬‬
  > ‫مشت لوزدهم اوستامعمولا «زامیادیشت» خوانده ‪.‬يشود‪ .‬ایزه زامیاد (زمین) با ایزدآسمان غالبایکجا‬
==================== BQT:1024 zafar chunk 487 len 4519
  > ‫‪ - ۱‬اوستا ‪( ۲2122 -‬کلو)‪ .‬پهلوی ‪« 72122‬اسشق ‪۳٩5+.‬‏ هوبشمان‬    ‫دالته‌اند «نفی) ‪.‬‬
  > ‫«* زفر زیرین» فك اسفل است و «زفر زبرین» فك اءلی ‪ « :‬هر حیوالی بوقت خاییدن زفرزبرین‬
  > ‫جنباند و ‪,‬یکی مخالف بود چنانك تماح زفرژیرین جنباند وزبرین لجنباند> «دابشنامه ‪۳4۲۰‬‬
==================== BQT:1036 zanax chunk 499 len 4733
  > ‫حندی باستان ‪( 1102 -‬زنخ) ‏ اوستا ‪" 2۷082 -‬ارمنی ‪( 608۳6‬فك‪ ,‬کونه)‪.‬‬                               ‫‪۱‬‬
  > ‫زنخ برخون زد اراج بعداد ‪.‬‬                               ‫تراج غبغبم را کر کنی باد‬
  > ‫‪4‬دراوستا ‪( 126022‬شناساندن»‬
  > ‫‪ - ۵‬زند در پهلوی ‪( 04۳82‬شرح ‪+‬تقسیر)«اونوالا ‪./44‬‬
  > ‫معرفت) «بارتولمه ‪ .۹۹۱‬کلم اخیر از مصدر ‪ 022‬اوستابی (‪ 0121‬پارسی‌باستان) بمعنی‌داد‪-‬تن‬
  > ‫وشناختن است که یا پیشود ‪ 2‬در اوستابی صورت ‪ 11022‬در آمده د‬
  > ‫کهن تفیری برای اوستا بزبان اوستایی نوشته بودلد و ده‌ونه‌ای ازین تفیر درخوداوسنای کمولی‬
  > ‫بافیمانده و بامتن مخلوط شده است ‪ .‬بعد هسااین تفیر را از زبان اوستابی بزبان پپلوی ترجمه‬
  > ‫(اهراً بلاش‌اول اشکالی ‪). ۸۷ - ۱۵‬‬  ‫کردند ‪ .‬طبق سنت پس از تدوین اوستا در زمان ولخش ظ‬
  > ‫تفر اوستا بعنی زلد » بزبان پپلوی شروع شد و ندوین این تفیرتا اواخر عهد ساسانیمخصوصاً‬
  > ‫فصل ‪ 4‬ولدندادآمده ) ‪ .‬زلد با تفیری که امروژه در دست داریم »ت>فسیرست اآزعهد ساسایان‪.‬‬
  > ‫روبهم رفته از تفیر پهلوی اوستایمنی اززند ‪ ۰۰۰۱۶۱‬کلمه یما رسیده ‪ .‬در بار مفهوم و استعمال‬
  > ‫کلمةٌ «زند» ازقدیم تاکنون دوبسند گان‌شرق وغرب‌دچار اشتباه شدء‌اند از جمله قولمژلف برهالست‬
```


## [2026-09-05T20:51:14.159Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD ==\"; grep -n \"zānūg\\|zanug\\|zānug\\|dahān\\|dahan\\|zafar\\|zanax\" PHD.txt PHD_mackenzie.txt | head -20; echo \"== NYB ==\"; grep -n \"zānūk\\|zanuk\\|dahān\\|zafar\" NYB_vol2_glossary.txt | head -20; echo \"== HUB zafar/dahan ==\"; grep -n \"zafar\\|dahān\\|dahan\\|zanax\\|čāna\\|Kinn\" HUB.txt | head -20",
 "description": "Grep MacKenzie, Nyberg, Hübschmann"
}
```


### [2026-09-05T20:51:14.252Z] TOOL RESULT

```
== PHD ==
PHD.txt:306:īdabr [dpi] sinner, deceiver. *dabr [dpl] *dark-coloured. dad [dt' | M dd, N ~] wild animal. 1ааа [d't! | M d?d, N ~] law, justice; those scriptures dealing with legal matters. даа [d’t' | N ~] age. зааа [d>1!] tooth. tdād, v. ahlaw-dād. dādan, dah- [YH BWN-tn! < A Vyhb; d*tn!, dh- | M d'dn, (dy-), P dh- N ~, dih-] 1. give; 2. create. —išn [dh(y)sn'] giving, donation; creation. dādār [d’t?l | N ~] creator. -- ih : creatorship. dādestān [DYNA < А dyn; d'ts?n! | M d'(d)ys?n, N dá(de)stan] judgement, justice, law; case, process. dàd-gàh [2^? gs] proper place, fire temple; = daxmag. dādīg [d'tyk'] legal, concerned with the Law. dad-meh (d"tms] adult, elder. dādwar [d?twbl | (M d^ywr, P d'dbr), N da(d)war] judge. ~ih: judgement. daftan, dam- [dptn', dm- | M dm-, N dam-idan] breathe, blow. «dišn: breath. daftar [dptl | N —] register, account-book. dagr [AL YK < А ryk; dgl | M dgr > dur, N dër] long. dagrand [дата | N dërand] long. ~«xwaday [-hwt’y] eternal, of long dominion. daģr|-pattāy [dgl pt'd] long-lasting. -—-zamáàn [-2т?п!] a long time. ^-zi(w)isn [-zywsn'] long-lived. dah [ro, ASLY A < A ә | M dh, N ~] ten. dah-, —išn, v. dádan. Юаһаӣр [dř k' | (N Dahàk)] = Azdahág. dahān [РИМЕ < A p(w)m-h | M dhyn, N даһап] mouth. dahibed [dhywpt! | M dhybyd] ruler, lord of the land.
PHD.txt:317:duš-ēwāz��h 29 dwāzdahān
PHD.txt:673:zádag [2’tk' | М side, N zāda] born; child. тайап, zan- [MHYTWN-tn! < А У mh; ztn!, zn- | M zdn, zn-, N ~] hit, beat, strike, smite. ~išn: blow, smiting. zadan, zày- [YLYDWN-tn! < A Vyld; z?tn! | M zd, z'y-, N ~] bear (offspring); be born. ~išn: birth. ` ~iSnig : born, engendered, animal. zadār [2t?7] smiter; destructive. zadüg [ztwk! | (N Zad)] gum. zafar [zpl | N ~] mouth, maw (daevic). *zahā [zh?(k')] depth. zahabag [zAh'pk! | N zaháb] spring, source. 1zahag [zhk', (z^ hk!) | М zhg, N zah) child, offspring. *zAhag [2’hk'] element (water, fire, air, earth). zahagómand [zhk'wmnd] pregnant, gravid. zahār [2/7 | N ~] womb. *zahih [zhyh] = zahā, zahr [zh] | M zhr, N ~] poison, venom. zahrag [z()Alk! | N ~a] bile, gall. zalüg [zlwk' | N zali] leech. zam [zm | P zmg] winter.
PHD.txt:677:zamān [ОЮМА < А ‘dw; gwn’, zmn! | M zmn, N ~] time, hour. ~ag [zm)nk!] = zaman. *zamānīģ [zm”nyk'] prescribed. zāmēnīdan, zāmēn- [p myn-ytn' | M z?myn-] lead, send. zamestān [z7nst?n! | (М dmyst?n), N ~] winter. zamīģ [z-, zmyk! | M zmyg, N zami] earth. ~ig [-yk'] terrestrial, earthly. ---paymānīh [-pim’nyh] geometry. zāmyād [*zmd't! (misreading of z'myzdt! = zām-yazd?) | М myd, N —] cal. 28th day. zan[NYSE < A nth; zn! | = M, N ~] (ĝl. -ān, -in) woman, wife. zan- , —i$n, v. zadan. 1zand [znd | N ~] commentary, explanation, Zend. *zand [zzd | = M] district, tribe. zandag [zndk! | N zanda] rampant. zandbed [zndpt' | M zndbyd] headman of a district, tribe. zandik [zndyk' | N ~] heretic, Manichaean. rmih: heresy. zang [zng] ankle, shank. zangig [zngyk! | N zangi] negro. zanjir [zncyl | (P zyncyhr), N —] chain. zānūg [2”nwk! | P z^nwg, N zānū] knee. zard [21 | N ~] yellow. ~1һ : yellowness. zardaģ [z/tk! | N zarda] (egg) yolk. zardak [zltk! | N ~] safflower. zard|-alüg [zit?hwk! | N ~ü] apricot. ~-tdbag [-cwpk! | N —čēba] turmeric. Zardu(x)&t [zltw(h)st' | (M zrdrwšt), N Zardust] Zaraduštra, Zoroaster. zargon [zlgwn' | P zrgwng, N zaryün] golden, green, fresh. ^ jh: greenness. zarig [zlyk' | M zryg] sorrow, grief. ~6mand [-’wmnd] sad, sorrowful. zarmān [zin?n! | M zrwn-, N ~] old man; old age, decrepitude. ~ih: old age. zarr [ZH BA < А zhb’; DHBA < A dhb | M zr-, N ~] gold. ~én [ZH B Aua. zlyn! | M zryn, N —in] golden. ~(i)gar [zlykl | N ~gar] goldsmith. zarwan [2/wp?n! | P zrw’n] old age. zastan, zāy- [zstn!, z())d-] ask, demand. zaxm [ztm, z?hm | (P jxm), N ~] wound. тау [zyd$ = Av. zaya-] instrument, weapon. ZÁy-, v. zastan. zay-, -išn(-ig), v. zádan. Zāyč(aģ) [z'yc(k') | N zāyča) horoscope. zayistan [2”dstn'] = zastan.
PHD.txt:2533:knee (u)šnūg, zānūg.
PHD.txt:2751:maw zafar.
PHD.txt:2862:mouth dahān; (daevic) zafar.
PHD.txt:4380:zodiac dwazdahan; sign of the ~ axtar.
PHD.txt:5064:zardčūbug zam zamīg zamān zastan zafar zadar zadan zadüg
PHD.txt:5468:gūhragdānāg gohrag dwāzdahān dwāzdah duxt, Just 1-*dūxtun duxtar ldaw-, gūw- gūwāg 12а} dwàr- dwārīdan dwiristan dwārišn jy)
PHD_mackenzie.txt:1845:dahlin [PWME < A p(w)m-h I M dhyn, N dahan] mouth.
PHD_mackenzie.txt:5728:zafar [zpll N "'] mouth, maw (daevic).
PHD_mackenzie.txt:6927:irresponsible apursi~nig.                  knee (u)snug, zanug.
PHD_mackenzie.txt:7070:mQ'l(J zafar.                              metamorphosis wardisn; V. transfor~
PHD_mackenzie.txt:7094:  framiidiir.                                  mouth daMn; (daevic) zafar.
PHD_mackenzie.txt:7420:relationship bradarodih.                 restrain    abaz     dahan,      griftan,
PHD_mackenzie.txt:8008:year sal; -years-old -salag.            zodiac dwazdahan; sign of the .....
PHD_mackenzie.txt:9729:zafar                                   \~       zarren                       ,~
PHD_mackenzie.txt:10762:gandagih                             AU ~ ..            dwazdahan                       , t-"lK.) QY \"
== NYB ==
727:2aš [^5] the independent form of the cas. obl. 3d p. sg. = enel. -$ (g. v.); always preceding the w. to which it belongs; used 1. anaphorically in the interior of a sentence after a part of the sentence which has been placed first for emphasis: andar han Zartuxst | aš hac miyān Gp i hömikän burt || u pat uléh Zartuxšt | aš han i dašn paitištān hac Osan rote burt 5615-1? (Markwart's reading, Cat. 114 n. 1, is a failure); õi (pron.) mar | aš 6 pasčh gàv apāc rānēnīt 485; — not anaphorically: Ot (prep.) fravahr + Zartuxst | aš (viz. the snake) zafar frac zat 4012-13; purr-x"arrahéh i ax" à astómand | aš hac tan xYarrah from his (viz. Zartuxšt's) bodily splendour 377-8; — taking up an encl. -§ at the beginning of the sentence, after a part of the sen- tence which carries a lengthy attribute: api-š hamäk damik i-š apar rāh bit | aš *perävanihit kart 3316-17; — after an ad- verbial phrase beginning the sentence: adak apar pat jamän | aš hanjamanénit mūtak :61° (where aš anticipates mūtak, cf. s. v. -š). — 2. to introduce the apo- dosis (as api-$, adak-i8): after kakar 31?! ; after ka 327. 3319. 341. 565. 5717. 924. after a relative clause 3219, 9824, 100?7— 101?. — Probably identical with MPrthPrs š, written as an independent w. with two dots above (another explanation of this § v. A-H III, Gloss s. v.; ? in a fragmentary context [S] is obscure). Cf am, at, atün, asän.
1159:dahän [PWMH] mouth 1217. 509. 101". 10422, — < *dafän, the SW form of Av. (1657) zafan-, zafar-, v. zafar; MPrs dhyn; Paz. dahan; NP dahán.
1190:dänük [d’nwk'] knee 332. — SW form of zānūk, q. v.; cf Sogd 49-50.
1304:*dó-apdàn [dw'pd'n'] "he who has two water jugs — "the constellation Aguarius 510, — My guess. On the Dendera picture of the Zodiac the Aquarius carries two jugs from which water flows. The read- ing dw’cdh’n' = dvāzdahān (g. v.) adopt- ed by Antiá (following Noeldeke) does not suit the context, and the emendation *Nahdzigan ‘Capricornus’ proposed by Sanjana is of no value.
1420:dvaristan [dwb'lstn'], dvaritan [dwb'lytn'] to run, to rush, of enemies and demoniac beings 2518 ete. passim; — andar ~. to rush, to come dashing (6 into the presence of) 7526; to make an onslaught, of Ahri- man and the demons at the beginning of the world 933.13, 9519, 10318; to make an assault upon (6) 1142; — apāc ~ to run back 1024; apar ~ to coil upwards (up a tree) 4012; — bē ~ to dash off 422, 10211.14.20; — frāc ~ to rush forth 25%; to spring forth (hac from) 9674. 9819. — Av. (765) dvar- ; Paz. duärestan, dvärestan. dvarišn [dwb'lin'] the act of running; as pred.: has to run, or is running 6811-12, dvārišnēh det. v. n. = the preceding w.: višāt- ~ the act of running about with loose, open clothes 69%, v. višat. dväzdah [dw’cdh; figure] twelve; han 4 12 axtar, 12 axtarān etc., v. axtar; dväz- dahān [dw’cdh’n'] the Zodiac 57. [12-n!] Ti: i dvàzdahom [dwb’cdhwm; 12-wm] the twelfth 8216, 844, E
3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
4475:zafar [zpl] mouth, of Ahrimanic beings 40!?. 486. — Av. (1657) zafar-; cf dahän.
4521:gor zat he shot an arrow at the onager 319-20; parr 6 pist zat its wing struck (the bowl with) the meal 925-26; 57 (= 6) fravahr + Zartuxst aš zafar frac zat threw open its mouth towards Z. 4012-13; 5; (= 6) gurg zat zanak the wolf's jaw was struck 506, with the gl. kū-š dahān ēvak apäk dit frot oškan (g. v.); Vidrafš pat dil zat stabbed V. in the heart 292; 25?! (cf s. v. rad 2 b)]; 383; — ēvak 6 dit ~ to knock to- gether 12019-20; ka šamšēr frac zanēt when the sword makes a stroke forward 254 (opp. apāc vēžēt, v. *véxtan); to drive (a peg) down into the soil 202%; tanbür ~ to play on the lute 476, — Av. (490) !gan-, pres. jan-; MPrth jdn jn-; MPrs zdn zn-; Paz. NP zadan zan-. V. also janišn, zanišn, zatak, zatar; cf apa-žand, ozatan.
5471:zafan-, zafar-: dahān
5472:zafar-: zafar
== HUB zafar/dahan ==
2253:bissstiick des Ziigels ; afgh. LW. dahana fem. *the bit
3100:wie kurd. dew *Mund* zu ap. dahan, setzt also ein
6502:*Berg*, zd. kaofa- 'Hiigel, H5cker ; dahdn *Mund', paz. dahan
6515:vHbhi' (idg. vebh Veben ) ; zafar 'Rachen' (Parsenwort ? neben
6516:echt pers. dahan = zd. zafan-) = zd. zafar- von iran. zaf-
7843:6) dahan 'Mund* = zd. zafan-^ 7) d^, df^ gestern = skr.
7885:zrada-'^ zafar 'Rachen' (das aber nicht urspr. persisch ist,
7886:vgl. dahan --= zd. zafan § 80, c und 110 sowie § 163, c)
7888:zamln *Erde (g^) H. 667; zanax 'Kinn {g^h) H. 669; zud
7954:np. zafar (dialektisch),
9541:mrf *tief' = zd. jafra- (aber zafar,
9543:ist (§ 111) = zd. zafar-).
10944:np. (dahan)
```


## [2026-09-05T20:51:39.979Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN cane ==\"; grep -n \"cäne\\|čāne\\|c[aä]ne 'Kinn'\\|Kinn\" HRN.txt | head; echo \"== ARY چانه/زانو/گونیا/دهان ==\"; grep -n \"چانه\\|گونیا\\|زنخ\" incoming/ARY/ARY_pages.txt | head -20",
 "description": "Grep Horn and Aryanpur"
}
```


### [2026-09-05T20:51:40.063Z] TOOL RESULT

```
== HRN cane ==
5908:669. jSJ^^icx 'Kinn', zene/dän,
5909:ai. Äaww- 'Kinn'; aw. zanva- (Geldnor, KZ. 30,
5910:514); arm. cnaut Kinnbacke, Wange (H. No. 137).
5912:'Kinn' (LW.) (416); wa;<. zanax (i^W.) , si^'n. zingü,
10422:80. ervaraky ervär 'Kinnbacken* (für aw. hanuharena-,
10445:') Tatk. Zar. S. 54 scheint ervär allerdings nicht 'Kinnbacken'
10864:157. 2>€it(i)Hi^är 'Kinnbacken', nur AW.-Komm. Vielleicht
10866:aw. paitis/'''arena- 'Kinnbacken .
11618:eiigiiStetcäne 12ö, 176.
== ARY چانه/زانو/گونیا/دهان ==
9630:زنخ» زنخدان (به چم "چانه") | ۳۲۷
```


## [2026-09-05T20:51:41.196Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SYN 221 page area ==\"; sed -n '5850,5870p' SYN.txt; echo; echo \"== SYN Av zanu line 5762 ==\"; sed -n '5755,5775p' SYN.txt",
 "description": "Read Buck 4.209 chin section"
}
```


### [2026-09-05T20:51:41.260Z] TOOL RESULT

```
== SYN 221 page area ==
4,209. Some of the words for ‘chin’ belong to the group of cognates in which jaw’, ‘cheek’ and ‘chin’ interchange (4.207). Some reflect the ‘shape ’as ‘something projecting’ or a ‘hook’. Sev- eral belong with words for ‘beard’ (4.142), for just as ‘chin’ may give the word for ‘beard’, so conversely a word for ‘beard’ or ‘behind the beard’, ‘what has a beard on it’, may be used also for the ‘chin’, and, once so established, no incongruity is felt in applying the term equally to a woman’s chin.
1. Grk. yévetoy : yévus. ‘jaw, cheek’, etc. (4.207).
NG mvyoim, with haplology fr. ém- (rw)yevov ‘that which has a beard on it’ : r&ywv ‘beard’ (4.142). Cf. Russ. podborodok ‘chin’, lit. ‘what is under the beard’. Kretschmer, Glotta 9.231.
2, Lat. mentum (> It. mento; Fr. menton in form fr. menté, -dnis ‘person with a long chin’): W. mant jaw, mouth’ (and prob. Goth munps, etc. ‘mouth’, 4.24), fr. root *men- in Lat. é- minére, prominére ‘stand out, project’, mons, montis ‘mountain’, etc. Walde-P. 2.263. Ernout-M. 608. Walde-H. 2.72 f.
SELECTED INDO-EUROPEAN SYNONYMS
Sp. barba, also and orig, ‘beard’, and Rum. barbie deriv. (*barbilia? Tiktin 158) of barbd, Lat. barba ‘beard’ (4.142),
3. Ir. smech, NIv. smeig, smig : Lith. smakras, Lett. smakrs ‘chin’, Skt, gmacru- ‘beard’, etc. (4.142). Walde-P, 2.689. Pedersen 1.86.
W. gen : Lat. gena ‘cheek’, ete,
Br. elgez, W. elgeth (obs.), OCorn, elgeht (gl. mentum) : OBr. ail, W. ael ‘eyebrow’ (4.206). Ernault, Dict, étym. 281.
4. ON, Sw. haka, Dan. hage, orig, ‘hook’ (as still Dan. hage, Sw. hake) : OE haca, hoc, ete. (12.75). Falk-Torp 371. Hellquist 327.
OE cin, OHG kinni, etc., general WGume. for ‘chin’ = Goth. kinnus, ON kinn, ete. ‘cheek’: Grk. yévus Saw, cheek’, etc. (4.207).
5. Lith. smakras, Lett. smabkrs : Ir, smech ‘chin’, etc. (above, 3). Mihl.- Endz 3.950.
Lett. zwods, mostly ‘chin’ but in some places ‘jaw’ : Lith. zandas, Grk. yvdbos ‘jaw’ (4.207). Miihl.-Endz. 4.759.
6. SCr., Boh. brada, also and orig. ‘beard’ (4.142), and fr. same source Pol. podbrodek, Russ. podborodok, lit. ‘what is under the beard’, fr. pod ‘under’ and broda, boroda ‘beard’. Berneker 72.
7. Skt. chubuka- (RV), cubuka-, cibu- ka-, civuka- (cf. BR s.vv.), wholly ob- scure. Uhlenbeck 91. Looks like a word of imitative orig., but why ‘chin’?
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
EEE
THE BODY; BODI
i ? such notions as ‘see, look, bright, sun(?),
shining ball’. 1, IE *ok- in various formations. There are also verbal forms for ‘see’, as Skt, desid. ks-, Grk. fut. dpoua, perf. szwra, etc., but these are much less wide- spread than the nouns for ‘eye’. Walde- P. 1.169 ff. Ernout-M. 697f. Falk- Torp 1417f. Feist 64 f. Grk. doce (dual, poet.); duua mostly poet., but also sometimes in NT and pap., whence through dim. éupartov the NG part; 6¢9adpds, the usual prose form, prob. a cpd. with second part related to $aXauos ‘inner room’ and orig. used for the socket of the eye; dial. dxradnos, érritos, formation unexplained; Lat. oculus, whence the Romance words (also the Tare Ir. ugazl ‘eyes’); Goth. augo, OE éage, etc., all the Gmc. words (diph- se erolained in part by influence of tities a ; Goth. ausod, etc.? but con- Lith os this group denied by some); ti Bae Co Reng acs, ChSl. ete. oko (obs. 8.); Skt. aksi, gen. sg. aksnas; Av.
nom, dual ast (§ for xs after Usi ‘ears’),

== SYN Av zanu line 5762 ==
Lett.  Zuokls, zuods vaigs zuods, smakrs
ChSl.  Geljustt lanita eieters
SCr.  éeljust, vilica obraz brada
Boh.  éelist lice brada
Pol. —szezeka lice podbrodek
Russ. éeljust! Séeka podborodok
Skt. hanu- ganda- civuka-
Av. zanu- <i Rede sh 4.207-4.209. There is considerable | the front part is the chin, the hinder part
interchange between ‘jaw’, ‘cheek’ and
the cheek’.
There is also some inter-
‘chin’, notably in a widespread cognate group. This is not surprising, for the ‘chin’ is the prominent part of the lower jaw and the ‘cheek’ corresponds in posi- tion to the side of the jaw. Cf. Aristot. ; HA 492522 gr ctaydves db0 robrwy 7d Tpocbiov yéverov, 7d 8 dmlcQrov yevus ‘furthermore there are two Jaws; of these
change with ‘mouth’ and with ‘face’, and between ‘chin’ and ‘beard’.
4.207. Several of the words for ‘jaw’ owe this use to some resemblance in shape, as that of a ‘sickle’ to the lower jaw in side view, of a ‘wagon, cart’ to the palate or upper jaw, of a ‘box’ to the
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
mp BODY; BODILY FU
be teeth, on ‘fork’, tour OS ’ t of the Jaw in jaw Pol ‘angle�� to tha Bee ae m verbs for ‘chew’ Or wae he modern Polish) seems to have dasa slang term forthe: ‘chauter starte - Several are obscure in their d ection. i a ait words for ew, aHal ‘chin’. Orig. sense Jaw and ultimate connection with ae word for ‘knee’, 1B *genu- (neut.), Gri. yoru, Lat. geni, etc. (4.36), through some com- mon notion like ‘angle’, is probable. Walde-P. 1.587. Ernout-M. 414. -H, 1.589 f. on ‘jaw’ (so always in Hom.) and ‘cheek’, -yéverov ‘chin’ (and ‘beard’) ; Lat. gena ‘cheek’ (mostly in pl.; stem genu- in genutni dentés ‘back teeth’); W. gen ‘jaw, chin’ (Ir. gin, W. geneu, Br. genou ‘mouth’); Goth. kinnus, ON kinn, Dan., Sw. kind ‘cheek’, OE cin, OHG kinni, etc. (all WGmce. words) ‘chin’ (but in early period traces of use for ‘jaw’, as OHG chinne ‘jaws’ Notker, Ps. 31.9, OHG chinnibacho ‘jaw’, OE cinban ‘jaw- bone’); Skt. hanu- ‘jaw’ (h for 7 second- ary), Av. zanu- ‘jaw’ or ‘chin’ (in epd., Barth, 1689) , NPers. zanaz ‘chin’; Toch. Ber oa (dual, SSS, 3, ftn.). Gre ae ae extension *Gon(e)dh-, Ba ease pn ; zandas ‘jaw’, al Mihl.-Endz, 4.759) edi pail # Ok rn al yom vor) istot, =i + Boisacq 862. GROpeRT se ce nr HdBos,. vers NG Hacé\)\a, of frequency.
fr. It. mascella (below
a 2)
Pe (mostly in pl.) ae It. mascella jaw’, but
SP. mejilla « back tooth’), cheek’, Rum. mased
```


## [2026-09-05T20:51:56.539Z] TOOL CALL #28: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-05T20:51:56.650Z] TOOL RESULT

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


## [2026-09-05T20:52:04.234Z] TOOL CALL #29: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D8%A7%D9%86%D9%88\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D9%87%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D9%86%D8%AE\" \\\n \"https://en.wiktionary.org/wiki/%DA%86%D8%A7%D9%86%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%D9%86%DB%8C%D8%A7\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 172, Genu1/Genu2/Geph roots: Persian outcomes zānū, dahān, zanax, čāne, gūniyā\" ;\ndone",
 "description": "Archive Wiktionary Persian pages"
}
```


### [2026-09-05T20:52:08.283Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d1ac793429444020.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/990f5bc442991451.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b610ffaca40f3dc5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/da98bf69cb028143.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/89e934abc60579f2.txt
```


## [2026-09-05T20:52:11.852Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in d1ac793429444020 990f5bc442991451 b610ffaca40f3dc5 da98bf69cb028143 89e934abc60579f2; do echo \"##### $f\"; grep -n -i -A12 \"Etymology\" $f.txt | head -50; echo; done",
 "description": "Read etymologies from archived Wiktionary pages"
}
```


### [2026-09-05T20:52:13.857Z] TOOL RESULT

```
##### d1ac793429444020
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Derived terms 
69-
70- 1.2.2 
71- Descendants 
72-
73- 1.3 
74- Further reading 
--
85: Etymology 
86-
87- 2.3 
88- Pronunciation 
89-
90- 2.4 
91- Noun 
92-
93- 2.4.1 
94- Descendants 
95-
96- 2.5 
97- References 
--
183: Etymology
184- [ edit ] 
185-
186- Borrowed from Classical Persian زانو ( zânu , “ knee ” ) , from Proto-Iranian *jā́nu .
187-
188- Noun
189- [ edit ] 
190-
191- زانو • ( zanu ) ( definite accusative زانویی ( zanuyu ) , plural زانولر ( zanular ) ) 
192-
193- knee , the joint or the region of the joint in the middle part of the leg between the thigh and the shank 
194- Synonyms: دیز ( diz ) , ركبه ( rükbe ) 
195-
--
234: Etymology
235- [ edit ] 
236-
237: Etymology tree
238-
239- Proto-Indo-European *ǵónu 
240- Proto-Indo-Iranian *ȷ́ā́nu 
241- Proto-Iranian *jā́nu 

##### 990f5bc442991451
62: Etymology 1 
63-
64- 1.1.1 
65- Noun 
66-
67- 1.1.1.1 
68- Declension 
69-
70- 1.2 
71: Etymology 2 
72-
73- 1.2.1 
74- Noun 
75-
76- 1.2.1.1 
77- Declension 
78-
79- 2 
80- Ottoman Turkish 
81-
82- Toggle Ottoman Turkish subsection 
83-
--
88: Etymology 
89-
90- 2.3 
91- Noun 
92-
93- 2.3.1 
94- Descendants 
95-
96- 2.4 
97- Further reading 
98-
99- 3 
100- Persian 
--
108: Etymology 
109-
110- 3.3 
111- Pronunciation 
112-
113- 3.4 
114- Noun 
115-
116- 3.4.1 
117- Inflection 
118-
119- 3.4.2 
120- Descendants 

##### b610ffaca40f3dc5
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Verb 
69-
70- 1.1.2.1 
71- Conjugation 
72-
73- 1.2 
74: Etymology 2 
75-
76- 1.2.1 
77- Pronunciation 
78-
79- 1.2.2 
80- Adjective 
81-
82- 1.2.2.1 
83- Declension 
84-
85- 1.3 
86- References 
--
94: Etymology 
95-
96- 2.2 
97- Pronunciation 
98-
99- 2.3 
100- Noun 
101-
102- 2.3.1 
103- Related terms 
104-
105- 2.3.2 
106- References 
--
114: Etymology 
115-
116- 3.2 
117- Pronunciation 
118-
119- 3.3 
120- Adjective 
121-
122- Toggle the table of contents 
123-

##### da98bf69cb028143
73: Etymology 
74-
75- 2.2 
76- Pronunciation 
77-
78- 2.3 
79- Noun 
80-
81- 2.3.1 
82- Related terms 
83-
84- 2.3.2 
85- Descendants 
--
318: Etymology
319- [ edit ] 
320-
321- From Proto-Iranian *jánukah , from Proto-Indo-Iranian *ȷ́ʰánuš , from Proto-Indo-European *ǵénus ( “ chin, jaw, cheek ” ) .
322-
323- Cognates include Avestan 𐬰𐬁𐬥𐬎 ( zānu ) , Sanskrit हनु ( hánu ) , Armenian ծնոտ ( cnot ) , Latin gena , Tocharian A śanweṃ , Welsh gen , Dutch kin , English chin , German Kinn .
324-
325- Pronunciation
326- [ edit ] 
327-
328- ( Classical Persian ) IPA ( key ) : /t͡ʃaː.ˈna/ 
329-
330- ( Dari, formal ) IPA ( key ) : [t͡ʃʰɑː.nä] 

##### 89e934abc60579f2
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Inflection 
69-
70- Toggle the table of contents 
71-
72- گونیا 
73-
74- 2 languages 
--
134: Etymology
135- [ edit ] 
136-
137- From Ancient Greek γωνία ( gōnía , “ corner, angle; joiner's square; cornerstone ” ) , probably via Classical Syriac ܓܘܢܝܐ ( gōnyā ) . Doublet of زانو .
138-
139- Noun
140- [ edit ] 
141-
142- گونیا • ( guniyâ ) ( plural گونیاها ) 
143-
144- Dari
145-
146- گونیا
```


## [2026-09-05T20:52:23.411Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### zanu\"; sed -n '230,300p' d1ac793429444020.txt; echo; echo \"#### dahan\"; grep -n \"Proto-Iranian\\|Middle Persian\\|Avestan\\|Etymology\" 990f5bc442991451.txt | sed -n '1,60p'",
 "description": "Read zanu and dahan etymologies"
}
```


### [2026-09-05T20:52:23.478Z] TOOL RESULT

```
#### zanu
 [ edit ] 

 زانی ( zani ) , زونی ( zuni ) ( dialectal ) 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *ǵónu 
 Proto-Indo-Iranian *ȷ́ā́nu 
 Proto-Iranian *jā́nu 
 Persian زانو 

 From Proto-Iranian *jā́nu , from Proto-Indo-Iranian *ȷ́ā́nu , from Proto-Indo-European *ǵónu . Cognate with Mazanderani زندی ( zendi ) , [ 1 ] Ancient Greek γόνυ ( gónu ) , Latin genū , English knee . Doublet of گونیا .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /zaː.ˈnuː/ 

 ( Dari, formal ) IPA ( key ) : [zɑː.núː] 

 ( Dari, formal ) IPA ( key ) : [zɑː.núː] 
 ( Kabuli ) IPA ( key ) : [zɑː.núː] 

 ( Hazaragi ) IPA ( key ) : [zɔː.nú] 

 ( Iran, formal ) IPA ( key ) : [zɒː.núː] 

 ( Tajik, formal ) IPA ( key ) : [zɔ.nú] 

 Rhymes: -uː 

 Readings

 Classical reading ? 

 zānū

 Dari reading ? 

 zānū

 Iranian reading ? 

 zânu

 Tajik reading ? 

 zonu

 Noun
 [ edit ] 

 زانو • ( zānū / zânu ) ( plural زانوها ( zānū-hā / zânu-hâ ) , Tajik spelling зону ) 

 ( anatomy ) knee 

 Descendants
 [ edit ] 

 Judeo-Tat: zani 

 → Khalaj: zânı 

 References
 [ edit ] 

 ^ Talebi, Ali ( 2012 ), مشتی از مرواریدهای فراموش‌شده‌ی مازندران (فرهنگ واژگانی) [ A Handful of the Forgotten Pearls of Mazandaran (Dictionary) ]‎ [1] , Amol, page 39 


#### dahan
62: Etymology 1 
71: Etymology 2 
88: Etymology 
108: Etymology 
209: Etymology 1
397: Etymology 2
724: Etymology
796: Etymology
799: From Middle Persian [script needed] ( PWME /⁠dahān⁠/ , “ mouth ” ) , apparently from an earlier formation *dam-fāzek , composed of دم ( dam , “ breath ” ) + a Proto-Iranian *faź ( “ mouth, muzzle ” ) of unclear origin, perhaps sound-symbolic. [ 2 ] Another theory takes the entire formation as a derivative of a Proto-Indo-European *ǵep- ( “ mouth, to chew ” ) , whence English jowl . [ 3 ] Compare Avestan 𐬂𐬢𐬵𐬁𐬥𐬋 ( åŋhānō , “ mouth ” ) , genitive form of Avestan 𐬁𐬵 ( āh , “ mouth ” ) .
987: Persian terms inherited from Middle Persian 
988: Persian terms derived from Middle Persian 
989: Persian terms derived from Proto-Iranian 
1005: Requests for native script for Middle Persian terms
```


## [2026-09-05T20:52:32.447Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '790,880p' 990f5bc442991451.txt",
 "description": "Read dahan Persian section fully"
}
```


### [2026-09-05T20:52:32.492Z] TOOL RESULT

```
 دهن ( dahan ) ( dialectal or archaic ) [ 1 ] 

 آن ( ân ) ( colloquial ) 

 دان ( dân ) ( colloquial ) 

 Etymology
 [ edit ] 

 From Middle Persian [script needed] ( PWME /⁠dahān⁠/ , “ mouth ” ) , apparently from an earlier formation *dam-fāzek , composed of دم ( dam , “ breath ” ) + a Proto-Iranian *faź ( “ mouth, muzzle ” ) of unclear origin, perhaps sound-symbolic. [ 2 ] Another theory takes the entire formation as a derivative of a Proto-Indo-European *ǵep- ( “ mouth, to chew ” ) , whence English jowl . [ 3 ] Compare Avestan 𐬂𐬢𐬵𐬁𐬥𐬋 ( åŋhānō , “ mouth ” ) , genitive form of Avestan 𐬁𐬵 ( āh , “ mouth ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /da.ˈhaːn/ 

 ( Dari, formal ) IPA ( key ) : [d̪ä.ɦɑ́ːn] 

 ( Dari, formal ) IPA ( key ) : [d̪ä.ɦɑ́ːn] 
 ( Kabuli ) IPA ( key ) : [d̪ɑ́ːn] 

 ( Hazaragi ) IPA ( key ) : [d̪ɔ́ːn] 

 ( Iran, formal ) IPA ( key ) : [d̪æ.ɦɒ́ːn] 

 ( Tajik, formal ) IPA ( key ) : [d̪ä.ɦɔ́n] 

 Rhymes: -aːn 

 Readings

 Classical reading ? 

 dahān

 Dari reading ? 

 dahān

 Iranian reading ? 

 dahân

 Tajik reading ? 

 dahon

 Audio ( Iran ) : ( file ) 

 Noun
 [ edit ] 

 Dari

 دهان 

 Iranian Persian

 Tajik

 даҳон 

 دهان • ( dahān / dahân ) ( plural دهان‌ها ( dahān-hā / dahân-hâ ) , Tajik spelling даҳон ) 

 mouth ( cavity in the face ) 
 دهانت را باز کن. ( more literary ) ― dahân -at-râ bâz kon. ― Open your mouth . 
 دهنت و باز کن. ( more colloquial ) ― dahan -et-o bâz kon. ― Open your mouth . 
 1177 , Farīd ud-Dīn ʿAṭṭār , “ حکایت طوطی [ The Parrot's Tale ] ”, in منطق الطیر [ The Conference of the Birds ], lines 802—803 : طوطی آمد با دهان پر شکر، در لباس فستقی با طوق زر tūtī āmad bā dahān pur-šakar, dar libās-i fustuqī bā tawq-i zarr The parrot came with a mouth full of sugar, in pistachio-green robes with a golden collar 

 c. 1260s , Jalāl ad-Dīn Mohammad Rūmī , translated by Reynold A. Nicholson , مثنوی معنوی [ Masnavi-ye-Ma'navi ], volume VI, verse 4081: چون نشیند بهر خور بر روی برگ، در فتد اندر دهان مار و مرگ čūn nišīnad bahr-i xwar bar rō-yi barg, dar fatād andār dahān -i mār u marg When it [the bird] settles on the leaf for the purpose of eating, it falls into the mouth of the snake and death. 

 ( by extension ) mouth , opening 

 Inflection
 [ edit ] 

 Basic forms of دهان 

 singular

 plural

 bare

 دهان ( dahân ) 

 دهان‌ها، دهانا △ ( dahân-hấ, dahânấ △ ) 

 definitive direct object

 دهان را، دهان رو △ ( dahân râ, dahâno △ )
```


## [2026-09-05T20:52:38.347Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"Hasandust\\|حسن‌دوست\\|Cheung\\|Nyberg\\|Horn\\|Etymological Dictionary\" 990f5bc442991451.txt | head -20; echo \"---\"; sed -n '960,985p' 990f5bc442991451.txt",
 "description": "Find references on dahan page"
}
```


### [2026-09-05T20:52:38.400Z] TOOL RESULT

```
965: ^ Rastorgujeva, V. S. ; Edelʹman, D. I. ( 2007 ), “*faź-, *fāź-, *fauź-”, in Etimologičeskij slovarʹ iranskix jazykov [ Etymological Dictionary of Iranian Languages ] (in Russian), volume 3, Moscow: Vostochnaya Literatura, page 50 
967: ^ Nourai, Ali ( 2011 ), “Geph, Gebh”, in An Etymological Dictionary of Persian, English and other Indo-European Languages , page 142 
---
 References
 [ edit ] 

 ^ “ دهن ”, in Dehkhoda Dictionary ‎ [1] , 23 September 2012 (last accessed), archived from the original on 25 December 2012 

 ^ Rastorgujeva, V. S. ; Edelʹman, D. I. ( 2007 ), “*faź-, *fāź-, *fauź-”, in Etimologičeskij slovarʹ iranskix jazykov [ Etymological Dictionary of Iranian Languages ] (in Russian), volume 3, Moscow: Vostochnaya Literatura, page 50 

 ^ Nourai, Ali ( 2011 ), “Geph, Gebh”, in An Etymological Dictionary of Persian, English and other Indo-European Languages , page 142 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=دهان&oldid=92196296 "

 Categories : Arabic terms belonging to the root د ه ن 
 Arabic lemmas 
 Arabic nouns 
 Arabic masculine nouns 
 Arabic nouns with basic triptote singular 
 Arabic nouns with sound feminine plural 
 Arabic nouns with broken plural 
 Arabic nouns with triptote broken plural in -a 
 Arabic occupational nouns 
 Arabic nouns with triptote singular in -a 
 Arabic nouns with sound masculine plural 
 ar:Occupations 
 Ottoman Turkish terms derived from Classical Persian 
 Ottoman Turkish lemmas 
 Ottoman Turkish nouns
```


## [2026-09-05T20:52:50.920Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '/^ Persian/,$p' b610ffaca40f3dc5.txt | head -80",
 "description": "Read zanax Persian section"
}
```


### [2026-09-05T20:52:52.503Z] TOOL RESULT

```
 Persian 

 Toggle Persian subsection 

 2.1 
 Etymology 

 2.2 
 Pronunciation 

 2.3 
 Noun 

 2.3.1 
 Related terms 

 2.3.2 
 References 

 3 
 South Levantine Arabic 

 Toggle South Levantine Arabic subsection 

 3.1 
 Etymology 

 3.2 
 Pronunciation 

 3.3 
 Adjective 

 Toggle the table of contents 

 زنخ 

 7 languages 

 فارسی 
 Magyar 
 Kurdî 
 Malagasy 
 Русский 
 Türkçe 
 中文 

 Entry 

 Discussion 

 English 

 Read 

 Edit 

 View history 

 Tools 

 Tools

 move to sidebar 
 hide 

 Actions

 Read 

 Edit 

 View history 

 General

 What links here 
 Related changes 
 Upload file 
 Permanent link
```


## [2026-09-05T20:52:53.433Z] TOOL CALL #35: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%C3%B3nu\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%C3%A9nus\" \\\n \"https://www.etymonline.com/word/jowl\" \\\n \"https://www.etymonline.com/word/knee\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 172: PIE genu-1/genu-2/geph roots and English outcomes\" ; done",
 "description": "Archive PIE reconstruction and etymonline pages"
}
```


### [2026-09-05T20:52:56.723Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/409fd86aa10e42fc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/73e6324744212063.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f0b4f3c02c617cb0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/73b32c71deb38bc1.txt
```


## [2026-09-05T20:53:00.967Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### zanax persian etym\"; grep -n -A6 \"Proto-Iranian\\|Middle Persian\" b610ffaca40f3dc5.txt | sed -n '1,40p'; echo \"#### genu recon\"; grep -n -B2 -A25 \"Reconstruction\" 409fd86aa10e42fc.txt | sed -n '1,10p'; sed -n '/^ Etymology$/,+20p' 409fd86aa10e42fc.txt | head -40",
 "description": "Read zanax and PIE gonu pages"
}
```


### [2026-09-05T20:53:02.524Z] TOOL RESULT

```
#### zanax persian etym
#### genu recon
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%C3%B3nu
2-FETCHED: 2026-09-05T20:52:55Z
3-STATUS: 200
4:TITLE: Reconstruction:Proto-Indo-European/ǵónu - Wiktionary, the free dictionary
5-
6:Reconstruction:Proto-Indo-European/ǵónu - Wiktionary, the free dictionary 
7-
8- Jump to content 
9-
10- Main menu
```


## [2026-09-05T20:53:05.852Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== gonu ===\"; awk '/Proto-Indo-European \\[/,0' 409fd86aa10e42fc.txt | sed -n '1,70p'; echo; echo \"=== genus ===\"; awk '/Proto-Indo-European \\[/,0' 73e6324744212063.txt | sed -n '1,70p'",
 "description": "Read PIE reconstruction bodies"
}
```


### [2026-09-05T20:53:07.484Z] TOOL RESULT

```
=== gonu ===

=== genus ===
```


## [2026-09-05T20:53:10.582Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 409fd86aa10e42fc 73e6324744212063; do echo \"##### $f\"; grep -n \"Noun\\|Root\\|knee\\|jaw\\|chin\\|Descendants\\|Iranian\\|Avestan\\|Sanskrit\\|Derived\" $f.txt | sed -n '1,40p'; done",
 "description": "Locate content in PIE pages"
}
```


### [2026-09-05T20:53:12.430Z] TOOL RESULT

```
##### 409fd86aa10e42fc
62: Noun 
68: Derived terms 
71: Descendants 
139: Noun
144: knee 
231: Derived terms
253: ⇒ Proto-Germanic: *knussijaną ( “ to kneel ” ) [ 5 ] 
263: *ǵnusr-yé-ti ( “ to kneel ” , yé-denomitive ) [ 7 ] 
272: Ancient Greek: γόνατος ( gónatos , gen.sg. ) , γόνυ ( gónu , “ knee; plant node ” , nom.sg. ) 
275: Descendants
291: Proto-Indo-Iranian: *ȷ́ā́nu ( see there for further descendants )
##### 73e6324744212063
62: Noun 
74: Descendants 
140: Noun
147: jaw 
149: chin 
257: Descendants
274: Proto-Indo-Iranian: *ȷ́ʰánuš ( with unexplained aspiration of *ĵ ) ( see there for further descendants )
282: Tocharian A: śanweṃ   du ( “ jaws ” )
```


## [2026-09-05T20:53:15.782Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### gonu 130-300\"; sed -n '130,150p;225,300p' 409fd86aa10e42fc.txt; echo; echo \"### genus 135-290\"; sed -n '135,160p;255,290p' 73e6324744212063.txt",
 "description": "Print PIE reconstruction details"
}
```


### [2026-09-05T20:53:15.834Z] TOOL RESULT

```
### gonu 130-300
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Noun
 [ edit ] 

 *ǵónu   n ( oblique stem *ǵnéw- ) [ 1 ] [ 2 ] 

 knee 

 Inflection
 [ edit ] 

 Athematic, proterokinetic

 *ǵnúh₁ 

 *? 

 *ǵnúmis , *ǵnúbʰis 

 Derived terms
 [ edit ] 

 *ǵénw-eh₂ 
 Proto-Celtic: *genwā ( “ (river) bend ” ) 
 → Latin: Genava ( toponym ) 
 → English: Geneva 

 → Latin: Genua ( toponym ) ( see there for further descendants )
 → English: Genoa 

 *ǵnéw-o-m [ 1 ] 
 Proto-Germanic: *knewą [ 3 ] ( see there for further descendants )

 *ǵnu-nó-s [ 3 ] 
 Proto-Albanian: *gluna ( < earlier *gnuna ) [ 4 ] 
 Albanian: glû 
 Albanian: gju , gjû 

 *ǵnu-tó-s 
 *ǵnút-tu-s [ 5 ] 
 Proto-Germanic: *knussuz [ 5 ] 
 ⇒ Proto-Germanic: *knussijaną ( “ to kneel ” ) [ 5 ] 
 Gothic: 𐌺𐌽𐌿𐍃𐍃𐌾𐌰𐌽 ( knussjan ) 

 *ǵnut-néh₂-ti ( *néh₂-present ) [ 5 ] 
 Proto-Germanic: *knuttōną ( “ to swat ” ) [ 5 ] ( see there for further descendants )

 *ǵnuh₂-nó-s ( < plural *ǵónuh₂ ) 
 Proto-Celtic: *glūnos ( < earlier *gnūnos ) [ 6 ] ( see there for further descendants )

 *ǵnus-ró-s 
 *ǵnusr-yé-ti ( “ to kneel ” , yé-denomitive ) [ 7 ] 
 Proto-Anatolian: 
 Hittite: 𒄀𒉡𒍑𒊭𒊑𒊍𒍣 ( ge-nu-uš-ša-ri-az-zi ) 

 *ǵonw-ó-s [ 3 ] 
 Proto-Hellenic: *gonwós [ 8 ] 
 Ancient Greek: γουνός ( gounós ) 

 ⇒ Proto-Hellenic: *gónwatos [ 8 ] 
 Ancient Greek: γόνατος ( gónatos , gen.sg. ) , γόνυ ( gónu , “ knee; plant node ” , nom.sg. ) 
 Greek: γόνατο ( gónato ) 

 Descendants
 [ edit ] 

 Proto-Anatolian: 
 Hittite: 𒄀𒂊𒉡 ( ge-e-nu /⁠gēnu⁠/ , nom.-acc.sg ) , (/ganu-/ in oblique cases) [ 7 ] 

 Proto-Armenian: 
 Old Armenian: ծունր ( cunr ) 

 Proto-Balto-Slavic: 
 > ? Proto-Slavic: *zveno ( see there for further descendants )

 Proto-Hellenic: *gónu 
 Ancient Greek: γόνυ ( gónu ) 
 Greek: γόνατο ( gónato ) 

 Proto-Indo-Iranian: *ȷ́ā́nu ( see there for further descendants )

 Proto-Italic: *genū [ 9 ] ( < instrumental *ǵénuh₁ ) 
 Latin: genū ( see there for further descendants )

 Proto-Tocharian: *kenw- [ 10 ] 
 *kenwäi ( dual ) 
 Tocharian A: kanweṃ ( dual ) 

 Tocharian B: keni ( dual ) 

### genus 135-290
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Noun
 [ edit ] 

 *ǵénus   f [ 1 ] [ 2 ] 

 cheek 

 jaw 

 chin 

 Inflection
 [ edit ] 

 Athematic, amphikinetic

 singular

 nominative

 *ǵénus 
 > ? Ancient Greek: γνάθος ( gnáthos ) ( see there for further descendants )

 Descendants
 [ edit ] 

 ⇒ Proto-Armenian: 
 Old Armenian: *ծին-աւտ ( *cin-awt ) 
 Old Armenian: ծնօտ ( cnōt ) , ծնաւտ ( cnawt ) , ծնոտ ( cnot ) Armenian: ծնոտ ( cnot ) 

 ⇒ Proto-Balto-Slavic: 
 Old Prussian: żauna 

 Proto-Celtic: *genus ( see there for further descendants )

 ⇒ Proto-Germanic: *kinnuz ( with geminate *nn of uncertain origin; perhaps < *ǵenw-ú-s ? ) ( see there for further descendants )

 Proto-Hellenic: *génus 
 Ancient Greek: γένυς ( génus ) 

 Proto-Indo-Iranian: *ȷ́ʰánuš ( with unexplained aspiration of *ĵ ) ( see there for further descendants )

 ⇒ Proto-Italic: *genā   f 
 Latin: gena ( “ cheek(bone) ” ) ( see there for further descendants )

 ⇒ Phrygian: ἀζήν ( azḗn , “ beard ” ) 

 Proto-Tocharian: *ćänu 
 Tocharian A: śanweṃ   du ( “ jaws ” ) 

 References
 [ edit ] 

 ^ De Vaan, Michiel ( 2008 ), Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN 

 ^ Kroonen, Guus ( 2013 ), Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [1] , Leiden, Boston: Brill , →ISBN
```


## [2026-09-05T20:53:29.982Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### jowl\"; sed -n '1,60p' f0b4f3c02c617cb0.txt | grep -v \"^ *$\" | head -40; echo; echo \"### knee\"; grep -n -m1 -A20 \"knee (n.)\" 73b32c71deb38bc1.txt",
 "description": "Read etymonline jowl and knee"
}
```


### [2026-09-05T20:53:31.604Z] TOOL RESULT

```
### jowl
URL: https://www.etymonline.com/word/jowl
FETCHED: 2026-09-05T20:52:56Z
STATUS: 200
TITLE: Jowl - Etymology, Origin & Meaning
Jowl - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of jowl 
 jowl (n.1) 
 "jaw, jawbone," especially the underjaw, a late 16c. alteration of Middle English chawl (late 14c.), earlier chafle (c. 1200), from late Old English ceafl "jaw; cheek; jawbone; cheekbone," from Proto-Germanic *kefalaz (source of Middle High German kiver , German kiefer , Old Norse kjoptr "jaw," Danish kæft , Flemish kavel , Dutch kevel "gum"), from PIE *gep(h)- "jaw, mouth" (cognates: Old Irish gop , Irish gob "beak, mouth").
 The spelling with j- , attested from c. 1400, is perhaps from influence of the synonymous Old French joue , which also was in Middle English (see jaw (n.)). This word and jowl (n.2) have influenced one another in form and sense. Middle English also had a jolle (late 14c.) meaning "the head," especially that of a fish, which might be from either or both nouns.
 also from late 16c. 
 jowl (n.2) 
 "fold of flesh under the jaw," 1590s, alteration of Middle English cholle "fold of flesh hanging from the neck or jaw, double chin" (c. 1300), which is perhaps from or related to Old English ceole "throat" (from PIE root *gwele- (3) "to swallow;" see gullet ), but the phonetic development would be abnormal. Also see jowl (n.1).
 also from 1590s 
 Entries linking to jowl 
 gullet (n.) 
 "passage from the mouth of an animal to the stomach," c. 1300 (as a surname), from Old French golet "neck (of a bottle); gutter; bay, creek," diminutive of gole "throat, neck" (Modern French gueule ), from Latin gula "throat," also "appetite," which is related to gluttire "to gulp down, devour," glutto "a glutton." De Vaan writes, "We seem to be dealing with an onomatopoeic formation of the form *gul- / *glu- ." Compare Old English ceole "throat;" Old Church Slavonic glutu "gullet," Russian glot "draught, gulp;" Old Irish gelim "I devour."
 jaw (n.) 
 late 14c., jowe , joue , "the bones of the mouth," "A word of difficult etymology" [OED]. Probably from Old French joue "cheek," originally jode , from Gallo-Romance *gauta or directly from Gaulish *gabata , but there are phonetic problems; or perhaps a variant of Germanic words related to chew (v.); compare also the two nouns jowl . Replaced Old English ceace , ceafl . Jaws as "holding and gripping part of an appliance" is from mid-15c.; figuratively, of time, death, defeat, etc., from 1560s.
 ajar 
 chafer 
 chaff 
 cheek 
 jowly 
 See All Related Words (7) 
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 ajar 
 "slightly open, neither open nor shut," 1718, also on a jar, on the jar, perhaps from Scottish dialectal a char "turned a little way," earlier on char (mid-15c.) "on the turn (of a door or gate)," from Middle English char "a turn," from Old English cier "a turn" (see chore). For 
 cheek 

### knee
23: knee (n.) 
24-
25- "joint between the principal bones of the leg," Old English cneo , cneow "knee," from Proto-Germanic *knewa- (source also of Old Norse kne , Old Saxon kneo , Old Frisian kni , Middle Dutch cnie , Dutch knie , Old High German kniu , German Knie , Gothic kniu ), from PIE root *genu- (1) "knee; angle." For pronunciation, see kn- .
26-
27- To be across (someone's) knee in reference to spanking is from 1866. Knee-breeches is from 1827; knee-pants is from 1858. Knee-slapper "funny joke" is from 1955.
28-
29- knee (v.) 
30-
```


## [2026-09-05T20:53:45.057Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WLD Bd1 genu ==\"; grep -n \"ĝenu\\|genu-\\|ĝep\\|gep(h)\\|Knie\" incoming/WLD/WLD_Bd1_pages.txt | head -25",
 "description": "Grep Walde-Pokorny Bd1"
}
```


### [2026-09-05T20:53:45.105Z] TOOL RESULT

```
== WLD Bd1 genu ==
6336:mittelbar liber dem Knie liegende Teil des Beines“ (mind, aus *arni-
6663:einem Aste das Knieholz abgab, das man zum Pfluge brauchte. Noth
19858:mit engerer Bedeutung „Wade. Kniebeuge“ altn. vqdvi m. „Muskel, bes.
19870:„Wade u alts, aaathan „suras“, mndd. wade „Wade“, mndl. wade f. „Knie-
19874:beuge, Kniekehle“.    Vgl. Liden, KZ. 41. 396f., wo auch iiber die Bedeu-
32676:pehl. kapdrak (Scheftelowitz BB. 28, 144; „GefaB“, kapoll „Kniescheibe
34079:qeis- „Kniekehle, Schenkel u. dgl.“.
34081:limburg. hies „Kniekehle, Kniebug"; lit. kis-ka „die starke Sehne von der
34082:Wade nacb der Kniekeble bin Untersehenkel Kniekehle Leisten, eichen",
34087:im Kniegelenk".                Liden,   Le monde oriental 5 (1911) 195f.
37724:— Gegen Beziekung zu *kenk- „Kniekehle“                                              s.   d.
37764:3.   kenk- etwa „Kniekehle oder Ferse".
37765:        kenkle „Kniekehle", khika „ds., Hesse", lett. cinksla „Sehne in der
37767:Kniebeuge"; anord. ha- ( *hanha-) in ha-mot „Sprunggelenk, Fersengelenk",
37768:hd-sin „Kniesehne des Hinterbeins bei Tieren, Fersensehne beim Menschen",
37777:hpkill „Kniegelenk am HinterfuB", sowie die Sippe von lat. coxa: da
43385:Foy IF. 6, 33 Zupitza Gutt. 66, 104, 115); ahd. liahsa „Kniebug des Hinter-
43707:      Ahd. hamma „Hinterschenkel, Kniekehle", ags. hamtn „Kniekehle“, aisl.
44192:am Pfiuge, Knie am Kahn“, kumbryti „steuern“.                                              Lit. bei OsthofflF. 6, 13ff.,
44707:                                qulpb-     :   q up/b- ,,mit den Knieen einknicken,                                stolpern;
44714:„stolpern, in die Knie fallen", klupau khipoli ,,knien“, lett. kliipti Adv.
44769:wieder Petersson LUA. 1915, 20)                           s.   vielmehr quclp- „mit den Knien ein-
46079:von der Klauc bis zum Knie; Vorderbein des Schweines mit der Schulter“,
47186:abg. kotino „Knie“, klr. cilcn (ursl. *,'dm „Glied" usw. (Petersson IF. 35.
47209:  Got. hlaupan „laufen“ (Lit. u. quelp- „mit den Knien einknicken ). Gegen
```


## [2026-09-05T20:53:46.065Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC genu ==\"; grep -n \"ĝonu\\|ĝenu\\|genu- \\|gonia\\|gōnia\" IEC.txt | head -20",
 "description": "Grep Mann IEC"
}
```


### [2026-09-05T20:53:46.224Z] TOOL RESULT

```
== IEC genu ==
3526:ekhó (theoretical form to accommodate Indic -h- with Arm. Balt. s/3) ‘T. WP I, 115. Cf. ego, eK and see J. Puhvel: Lg. 35.4.646-7. Cf. dhugotér, me$-, ĝenus for a similar problem Skt. ahám; Av. azom; OPer. adam; Oss. åz; Hitt. uk, ug-, ugg-; Arm. es; Hom. egón; Gk. egó; Alb. u, unë; Lat. ego; Faliscan eco; Osc. íív; Umb. ef; Go. ik; OHG ih, ihha; OE ic; ON ek; OCS ap jazü, ja (and com. SL); OLI. eš; Li. aš, ašen, asenai; Latv. es
5652:-keneja (: Gk. -géneia, cpds.) ‘born’; Oghamic ini-gena, Olr. in-ghean, s. “daughter”; Ir. gean ‘daughter, woman’; Olr. gein, f. (child, off- spring’: Arm. cin); W cf. bach-gen, pl. bech- gyn (“boy”, cf. guaks-), beside rhi-eni, pl. “pa- rents’; Latv. cf. zēns ‘boy’ (tonal *-e-, or IE *-&-). (Semantic note. There seems to be a link between this root & type ĝenu- ‘chin’, lit. “angle of the face’, ĝonu ‘knee’, lit. ‘angle of the leg? in view of ON Dër “joint, bend? also ‘generation’: OE cnëow ‘knee; generation’: OCS kolěno ‘knee’; po-kolěnije ‘generation’; LLat. genuculum ‘knee; degree of kinship’. Cf. also genuinus ‘hereditary’)
5655:ĝenu (fón-, gon-) “bend of the leg, knee; angle’. WP I, 586. See next Skt. jànu; Av. Znu; Per. zānū; Kurd. ejno (sic); Oss. zonig, zonug, dim. type, id.; Tokh. kanw, B keni-; Arm. cunr, id. beside (dim. type) cunkn, gs cnkan and cnko; Gk. gónu; Lat. genu; Go. (metath.) kniu: OE cneow; OHG kniu, knio, gs kniwes; ON kné. Z-gde in Go. kuna-wida, f. ‘fetter; OHG chuna-withi, id. beside (0-gde) cuoni-widi, id.
5656:ĝenus (&enuo, £enoueo, geno) “jaw, jowl, angle of the face, angle, wedge’. Cf. genu, geun- Per. zanax ‘chin’; Tokh. *zanwen (written San- wen, dual no.); Arm. with relic of def. art. cnawt, i-st. ‘chin, jaw’; Gk. génus “jaw, chin, beard, axe’, cf. (0-gde in) pó-gon ('beard', from *poK-80n-, see below: poKos); cf. also siā- gon, gs -gonos ‘jawbone’; Lat. genuae, pl. ‘jaws’; cf. genuinus, adj. of the cheek or jaw’; beside gena ‘cheek, jaw’: Phryg. cf. a-zén, acc. a-zéna ‘beard’; Br. génu, genaw, m. ‘mouth’ beside gén ‘cheek’; W genau & geneu, m. be- side gen, f. id.; OCor. genau, EMCor. ganow ‘mouth’; gen (m. ‘chisel, wedge’; f. 'chin");
5678:&eunos, à ‘chap, jowl; gill of fish’. (Form of *B&enuos, see ĝenus, genua). Cf. WP I, 644 and see next Skt. cf. -jodah, cpds. ‘chin’; Li. Ziáunas, -a (jaw; pl. *gills"); Latv. Zauna ‘gill’: (OE cian ‘gill may be a misspelling for *crwan, see next); Blg. 2üna ‘lip’ is isophonic.
5705:$onu (Gun) (form of ĝenu, q.v.)
5706:Av. žnus ‘knee’; Hitt. kanu-, id.; Go. cf. kuna- wida, OHG khuna-withi (fetter', cf. E. knee & withy). (Gk. gnáthos ‘jaw’ may contain the ele- ments of ĝenu- & genus ‘angle’ combined with z-gde of Go wandjan ‘turn’ rather than w. OHG wanga ‘cheek’, qua *uanguhos, à) ĝənus “heavy” Skt. jinah ‘aged’ (?); Oss. zin, zin ‘heavy’; Arm. canr, gs canu, id. $i (?) till” Arm. zi, Z, id.; Romani £i, id.
5849:ĝounos ‘chap, jowl; gill’. Form of ĝeunos, q.v. and cf. ĝenus Du. koon (jaw, jowl’; dial. ‘gil’); Li. (e-gde in view of Latv. ž-) žiáuna ‘jawbone’; pl. ‘gills’; Latv. Zauna ‘gill’. (Du. -00- is fr. Gmc. -au-. VW:EWNT)
```


## [2026-09-05T20:53:57.935Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"cneow\\|kniu\\|znubyo\\|zafar\\|gonu\\|yovu\" incoming/WLD/WLD_Bd1_pages.txt | head -20",
 "description": "Grep WLD Bd1 for knee cognates"
}
```


### [2026-09-05T20:53:57.984Z] TOOL RESULT

```
27552:ein, aus, halte ab” (zum Spir. asper in herald, dry-, irp-tgyovu. ovv-htg-
55349:u. knort    daneben ahd. kniurig „knorrig". mhd. knurie) „Knoten, Knorren,
55760:geueu- „Ivnie" (genu-, gonu-, gonu-, gneu-, gnu-).
55767:terung zum alten M-St. gonu-, oder vielleicht gonu-, s. Brugmann Gdr. II 2
55782:fiir   *7tQoyvv,      lat.   genu', got. kniu, ahd. usw. knio, kneo „Knie" (anord. kne
55783:auch von Knoten am Strohhalm, wie ags. cneoweht „knotig, von Pflanzen",
65266:Rohrstab" (Liden IF. 19, 325; Ablaut wie genu       got. kniu  vermutlicli                                :              ;
```


## [2026-09-05T20:54:01.565Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '55755,55830p' incoming/WLD/WLD_Bd1_pages.txt; echo \"=== page tag ===\"; grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd1_pages.txt | awk -F: '$1<55760' | tail -2",
 "description": "Read Walde-Pokorny genu entry"
}
```


### [2026-09-05T20:54:03.227Z] TOOL RESULT

```
gegeniiber der von idg. *gen(tbh)- „zusammendrucken" ist berechtigt, da
„Pflock, Holzklotz" nicht einmal im Germ, iiberall ungezwungen aus „zum
Zusammendriicken, -drehen verwendeter Knebel" herzuleiten sind und die
andern Sprachen eine solche Bedeutungsfiirbung giinzlich vermissen lassen.

geueu- „Ivnie" (genu-, gonu-, gonu-, gneu-, gnu-).
   Ai. junu „Knie", pehl. zanCik, np. zanu „Knie"; av. acc. sg.
                                                                   znUm, dat.
abl. pi. znitbyo; ai. jnu-bculh- „die Knie beugend", abhi-jnu „bis ans
                                                                       Knie",
pra-jnu-h „sabelbeinig“, av. fru-snu- etwa „die Knie nach vorn haltend";
arm. cunr „Knie“ (Hiibschmann Arm. St. I 34, Arm. Gr. I 457, >-Erwei-
terung zum alten M-St. gonu-, oder vielleicht gonu-, s. Brugmann Gdr. II 2
1, 181 f.; pi. cunk-k , gen. cng-ae. mit (/-Erweiterung, *gon-g-o-, Bugge
                                                                          KZ.
32, 12,    vgl. yvv-g); gr. yovv, gen. yov(*j:)aTo? „Knie“ (pi. jon.
                                                                     yovva, iiol.
yovva,    aus *yovfa), dehnstufig (wie janu, s. o.) ycoviu „Ecke“ (*ycovf-la);
yw-7i£TEiv     die Knie sinken, ohnmachtig werden", lyv vtj
                 „in
                                                              Kmekehle"    ,;

(*ev-yvva,  Boisacq 365 m. Lit.), yvv$ „auf die Knie nieder" (mit forman-
                s.

tischem -k oder -g, s. o.).
   ngoyvv       (s.   Brugmann-Thumb GrGr. 4 127 Anm. 1)          steht 7 570 vielleicht
fiir   *7tQoyvv,      lat.   genu', got. kniu, ahd. usw. knio, kneo „Knie" (anord. kne
auch von Knoten am Strohhalm, wie ags. cneoweht „knotig, von Pflanzen",
lat. geniculum  auch Knoten an Getreidehalmen; aber lat. genista ist etrus-
kisch, s. Herbig IF. 37, 171); eine Erweiterung mit germ, t in oberschles.
knutzen „auf den Knien hocken" und vielleicht in got. kniwam knussjatuls
„in die Knie zusammenknickend", wenn auf einem z3<-St. *knussus
                                                                        von
diesem Verbum *knutjan „beruhend“ (Brugmann Grdr. II 2 1, 181 oder zu
                                                                                 ;

*gen-, *gn-eu-s- „zusammendrucken, knicken", vgl. ahd. knussen
                                                               „zerdriicken"
                                       g(h)enu-s   — gengh-                                                      5b7

und zur Bed.         dt.    knieken von    der Wzf. *gn-ei-g-t       Kogel PBrB. 7,                              177,
Streitberg IP. 23, 1 1 7 f.      — Aksl. zvcno „Glied, Radfelge“                       ist      kaum nach
Mikkola IF. 6, 351 f. aus *zenco umgestellt (einen anderen Deutungsversueh
Petersons LUA. 1916, 5 f. s. u. ghiiel- „sich krummen“), z. B. Curtius 5 179,
Pick I 4 51, 216, 431 f., Falk-Torp u. knee, kneele.
  Mhd. knoche „Knorren, Knochen" (Brugmann Grdr. II 2                      1
                                                                                   ,
                                                                                        1   S   1   )
                                                                                                        gehort zu
*gen-, *gn-eu-g- „zusammendriicken“.


gih)euu-s „Kinnbacke, Kinn“ (Anlaut europ. y,                 ai.   h,   vgl.           *yhe, gho, -tg-
     Qi)om      u. dgl.).

  Ai. lianu-h f. „Kinnbacke"; gr. yews f. „Kinn,   Kinnbacke (yevetov „Kinn-   1
                                                                                   '

                                                      11
bart“ aus *yeref-iov,    yevgtg „Schneide  des Beiles    aus *yevtdq mit  fur                               //


ei, d. i. e, vor t, Bed. wie in Barte   yvd&og) nehymv ,,Bart“ (Reichelt BB.
                                               ,


26, 225; nur sehe ich in na>- kein zu per gehoriges *po\r\~, sondern nog
mit ^-Schwund unter Ersatzdehnung vor y; ,,was am Kinn ist“); lat. dentes
genu-in’ „Baekenzahne“ (gena „Wange“ fur *genu-s nach mala, Brugmann
IF 179);
   Air. gin, giun (richtig Thurneysen Hdb. § 307 gegen Zimmer KZ. 36, 46 1 tf.)
„Mund“,   cymr. gen „Wange, Kinn‘, acymr. genou, ncymr. corn, genau
„Mund“ (aus PI. *geneu-es); got. linnus f. „\Yange, Backe“ (fiir *kinus
nach den Kasus mit nn aus nit), anord. kinn, pi. kinnr f. ds., ahd. usw.
kinni „Kinn, Kinnbacke“ (iiber anord. kanpr, kampr m. ,.Schnurrbart“, ags.
=== page tag ===
```


## [2026-09-05T20:54:15.951Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WLD geph ==\"; grep -n \"kjaptr\\|kevel\\|Kiefer\\|ceafor\" incoming/WLD/WLD_Bd1_pages.txt | head -15",
 "description": "Grep WLD for geph root"
}
```


### [2026-09-05T20:54:15.996Z] TOOL RESULT

```
== WLD geph ==
51992:   ags. geagl m. n. „Kiefer“, mnd. gdgel gcgel m. n. „Gaumen, Zahnfleisch"
52033:   *ghabh-:                pi. „Kiefern“ (in der Bed. gerichtet nach craft
52035:„Kiefer“,      s.      oder Kreuzung des letzteren mit gengl s. o.?), alter
54251:gep(h)-, gebh- „ Kiefer,                      Hund; essen, Hessen".
54285:   germ, mit ph oder teilweisem bh anord. kjaptr oder kjoptr ( *kebut oder
54286:*kefut-) „Maul, Kinnbacke, Kiefer ', mhd. kivel, kiver „Kiefer“, nhd. mdartl.
54287:kiefe „Kieme“, nd. keve Kiefer, Kieme“, wozn die Verben norw. kjava „sich
54288:zanken, streiten" („die Kiefern riihrern"), mnd. nd. kibbelen, kabbelen, kevelen
54295:                                                 .                                              ,,   Kiefer".
54768:"jbbh   ..Kiefer. Mund"?     Zupitza Gutt.                                             1   92 f., Bartholomae Airan. Wb. 1657.
55317:ferner mit den Bed. „die Kiefern zusammenklappen" und „mit den Fingern
59101:kelk „Halsgeschwulst“, anord. kjallci m. „Ivinnbacken, Kiefer (auch Hand-
60085:gheluna „Kiefer \
60091:ir. bei  s. Osthoff IF. 4, 276), aisl. giqlnar ..Kiefer'*, schw. gal ,,Kieme,
60095:Kiefer ‘, dan.   gjcelle   ds.
```


## [2026-09-05T20:54:16.984Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"زنخ\\|چانه\" incoming/ARY/ARY_pages.txt | head; echo \"== latin index ==\"; grep -n -i \"GENU\\|GONU\" incoming/ARY/ARY_latin_index_pages.txt | head",
 "description": "Grep Aryanpur"
}
```


### [2026-09-05T20:54:17.074Z] TOOL RESULT

```
9630:زنخ» زنخدان (به چم "چانه") | ۳۲۷
== latin index ==
561:“GENU: 943)!
562:“GENU :.gl)3,) ta + KNIU ig gWsT + KNEO sly JWT + KNIE rglatey
9199:GENU HITTITE) <a JANU. (SANSKRIT) 4 Sunil
9204:POKORNY: 381 GENU X(LATIN) ya
9207:MACKENZIE: (KNEE) 120 GENUNCHIO (RUMANIAN) gly)
10489:EGENU, AGNAN ASaNGA AVESTAN) gles)
```


## [2026-09-05T20:54:20.563Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '54251,54300p' incoming/WLD/WLD_Bd1_pages.txt; echo \"=== ARY 9195-9215 ===\"; sed -n '9190,9215p' incoming/ARY/ARY_latin_index_pages.txt",
 "description": "Read WLD gep(h) entry and ARY index"
}
```


### [2026-09-05T20:54:20.628Z] TOOL RESULT

```
gep(h)-, gebh- „ Kiefer,                      Hund; essen, Hessen".
    ph    :   av. zafurd , zafan- „Mund, Racben" (: ags. ceafl nach Kluge KZ. 26, 89)

p  gr. yaneXeiv
    :             djueXeTv lies., wenn „apathisch, schlafrig sein" aus einem
                           ’




Adj. *yaneXt'jz ,,gahnend“ stammt, wmzu dann auch Faiyiag, Faipcov als
„wer Maulaffen feilhalt" (Bechtel KZ. 44, 354);
    bh    :   lit.        „langsam, mit langen Zahnen essen", aksl. zobati
                     lebiu,        zcbeti
„essen‘‘           (idg. o;        kaum
                           mit zebhi und as. c«/7, s. u. auf ein neben gebh-
liegendes gebh- gobh zu beziehen), serb. zobati „Korner fressen", russ. zobn
                               :


„Pferdefutter. Hacksel mit Gerste", serb. ceeh. zob ,,Hafer“ (vgl. nach
Blankenstein und Pedersen KG. 1 161 mndl. kaf ,,Abfall von den Ahren"?);
air. gop nir. gob i/joblm-) ..Schnabel. Murid
               ,
                                              (B. bei Fick II 4 114);
                                                                         -
                                                                         '
                                                                                                      -




                                        gebfhi-      — ghed-                                              571

   germ, mit ph oder teilweisem bh anord. kjaptr oder kjoptr ( *kebut oder
*kefut-) „Maul, Kinnbacke, Kiefer ', mhd. kivel, kiver „Kiefer“, nhd. mdartl.
kiefe „Kieme“, nd. keve Kiefer, Kieme“, wozn die Verben norw. kjava „sich
zanken, streiten" („die Kiefern riihrern"), mnd. nd. kibbelen, kabbelen, kevelen
„laut schwatzen", mhd. kibelen kifelen zanken" (u. dgl., s. Falk-Torp 518
                                        ,
                                                       ,,


unter kjevle );    dehnstufig     (s. o.)   as cafl, ags. ceafl (engl. jowl, jole)
                                                 .                                              ,,   Kiefer".
  Zupitza Gutt. 192 f. m. Lit., Pick III 4 34. 1st *gembh „beiBen“ eine nas.
Form unserer Wz.?
   C'ech. zabrn „Kietnen der Fisehe", russ. zdbry (Hirt BB. 24, 258) fiigt
sich im Guttural nicht. Ob arm. cov „Meer“ als *?jobho- „(Meeres)schlund"
verwandt sei, ist hochst fraglich uber andere Deutungsversuche (worunter
=== ARY 9195-9215 ===
KNEO ZANU, SHNU AVESTAN) glingh
KNIE (GERMAN) (gilt TKNU-KA (OLD PERSIAN) gleol gos
GNEO = (OLD ENGLISH) oS gud! ZANUG, ZANUK, — (PAHLAVI) 5 sy
KNEE ENGLISH) gJS3i (U)SHNUG.
KNA DANISH) Sail ZANA (KURDISH) (52,5
KNA  yswepisH) ped TAN ABALUCHI) gr she
KNA (NORWEGIAN) 33,5 ZANGUN AFGHAND) (3-4), g3\
KNIE (DUTCH) «gata KANWEN —:(TOKHARIAN A) A 5,55
GLIN BRETON) 3.5 » KENINE, KNI-:(TOKHARIAN B) B 5 )\i
GENU HITTITE) <a JANU. (SANSKRIT) 4 Sunil

CUNR ARMENIAN) «a,j

REFERENCES" bssR] eo OREN
POKORNY: 381 GENU X(LATIN) ya
BARNHART: (KNEE) 568 GENOU (FRENCH) Wil
DELAMARRE: . (GENOU) 99 GINOCCHIO AITALIAN) gills!
MACKENZIE: (KNEE) 120 GENUNCHIO (RUMANIAN) gly)
BUCK: 243 KNIU GOTHIC) S36
ONIONS: (KNEE) 507 {OLD SCANDINAVIAN) 465-041
SKEAT: (KNEE) 324 KNE
feee igbG ob, OLD HIGH GERMAN) jf gilt

ae |
‘REFERENCES beth DYAOSH (OLD PERSIAN) yl, go 54
POKORNY: = SOSO*~*~*~*~*~S*« DyAUH SANSKRIT) oy Site
```


## [2026-09-05T20:54:29.078Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"زانو\\|دهان\\|گونیا\" incoming/ARY/ARY_pages.txt | head -20",
 "description": "Grep Aryanpur Persian pages"
}
```


### [2026-09-05T20:54:29.128Z] TOOL RESULT

```
88:کوج کردهاند. طی این کوج‌های متوالی؛ آریایی‌ه با بومیان هر محل درآمیختند و در نتیجه پاک و
576:۱-فارسی: زانو > پهلوی: - پارسی کهن:2۸17171۸ + اوستایی: 8770717 *هند و
6414:۲ این واجريشه در برخی از زبان‌های هند و اروپایی دارای چم‌های دیگری نیز بوده است: آرواره» گونه» دهان,
9672:جم این واژه در زبان ایرلندی کهن: دهان.
11851:کپ (به چم *دهان" "دهانه"» *ظرف شیشیه‌ای بزرگ"»» "قرابه») / ۳۹۹
13084:چم این واژه در زبان رومانی: دهان,
13845:واژه‌ها (و واژه‌های مشابه در دیگر زبان‌های هند و اروپایی) همه از واجریشه‌ی "مادر" (۸137870 ,۸173 آمدهاند
14725:نُس (به چم*پوزه"» *اطراف دهان) / ۴۹۷
```


## [2026-09-05T20:54:35.831Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nlines=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\ndef pg(n):\n    for i in range(n,0,-1):\n        m=re.search(r'\\[pdf page (\\d+)\\]',lines[i])\n        if m: return m.group(1)\n    return '?'\nfor n in [576,6414]:\n    print('--- line',n,'pdf page',pg(n))\n    for l in lines[n-12:n+12]:\n        if l.strip(): print('   ',l.strip()[:200])\nEOF",
 "description": "Read Aryanpur entries for zanu and zanax"
}
```


### [2026-09-05T20:54:37.444Z] TOOL RESULT

```
--- line 576 pdf page 22
    ۱
    [pdf page 22]
    ۰ ۱
    ا
    :ْ دیباچه / ۲۳
    اروپایی نشان می‌دهد که در سانسکریت 0" تبدیل به **شده است. لذا واژه‌ی پنیادین هند و اروپایی
    که همه‌ی این واژه‌ها از آن مشق شده‌اند محتمالً *4 بوده است. (امروز معتقدند که اين
    واژه‌های بنیادین *۸0۸05" بوده است). طی صد سال گذشته بازسازی واژه‌های بنیادین هند و"
    اروپایی پیشرفت بسیاری کرده است و دانشمندان ریشه مشترکك اکثر واژه‌های هند و آروپایی را (از
    ۱ طریق پیگیری پسگرایانه‌ی شکل واژه‌ها) تعبین کرده‌اند. نمونه‌ی زیر مسیر اینگونه بازسازی‌ها را در
    , مورد واژه‌ی «زائوه در زبان فارسی و زبان آلمانی نشان می‌دهد:
    ۱-فارسی: زانو > پهلوی: - پارسی کهن:2۸17171۸ + اوستایی: 8770717 *هند و
    اروپایی: 078200"
    ۲ آلمانی: 12۷1 آلمانی میانه: 1001830 + آلمانی کهن: 1221117 + هند و اروپایی: تا072(7*
    ۱ چون در دوران هند و اروپایی‌های اولیه (۳ تا ۴ هزار سال پیش از میلاد) الب وخط وجود
    نداشته تعیین دقیق آوا و معنی واژه‌های هند و اروپایی بنیادین فقط از روی پیگیری پسگرایانه و
    حدس و قیاس و مقایسه‌ی دستگاه‌های آوایی میسر است. بهمین دلیل در | کثر فهرست‌ها وکتاب‌هائی
    که با این موضوع سر و کار دارند جلو واژه‌های بازسازی شده این نشان «۵ را می‌گذارند تا فرضی
    بودن واژه‌ی بازمازی شده را نشان دهند. (درکتاب حاضر نیز از این رسم پیروی شده است). . "
    با این وجود» شماری از دانشمندان معتقدند که این واژه‌های بازسازی شده واقعاً وجود
    نداشته‌اند و چیزی جز نشانه‌های مصنوعی برای نشان دادن فرگشت زبان‌های مختلف یستند. پرخی
    دیگر از زبانشناسان معتقدند که واژه‌های بازسازی شده با پیروی از اصول اثبات شده‌ی زبانشناختی و
    پژوهش‌های مکرر شناسایی شده‌اند و آنقدر شبیه واژه‌های بنیادین هند و اروپایی هستند که یک
    زبانشناس می‌تواند (در صورت امکان بازگشت به ‎٩‏ هزار سال پیش) با هند و اروپائیان آنزمان
--- line 6414 pdf page 217
    انگلیسی کهن (بلوابا80 صا0): 2 و9 :0515
    انگلیسی (تلولا5۸/0): )2 20224 علاط
    دانمارکی (18(م0): دای 0 (01313) :0702/5
    سوئدی (31707377): 0 7 (110)) +347
    نروژی (لما0 :0/0 0 9و (ت0) ام
    ۱ هلندی (3ع07): لا برهان قاطع + ۶۶
    لیتوانی ((714ل4ل724/): 20۸5 لغت‌نامه دهغدا : ۸۳۰
    لترنی (لتی) (لا7۶م): نراد اما فرهنگ معین : ۱۳۶۹
    1 ایرلندی کهن (لافتگا ۰:0۵ 65۸ ,610
    یادداشت.
    ۱ هبچیکك از پسگشت‌های فارسی ذکری از ریشه‌ی این واژه نمی‌کنند.
    ۲ این واجريشه در برخی از زبان‌های هند و اروپایی دارای چم‌های دیگری نیز بوده است: آرواره» گونه» دهان,
    پارسی باستان (۶8۶1۸۷ 012): 2117۸185 لینوانی (01۵/4هتاب7لا). 1۸5
    کردی (0[57نام): وا
    افغانی (پشتو)(4۳0/۸01): تن پسگشت‌ها ۸87۵۵۵5
    سانسکریت (54(/588/7): مهل۲۸2۸ بطق مهد
    برنانی (072810): و۱۱ 41 (۲013 ,#5تا78ا))
    لانین (00ا7مل): 5 48 (0.3۳7) امین دا
    گونیک (ع007771): دا برهان قاطع ‏ ۶۱
    انگلیسی کهن (5ا20 صاه): ق۲] ,1307 فرهنگ معین : ۱۳۷۱
    روسی (ا55ا): 1۸ لغت‌نامه دهخدا: ۸۵
    هه
    [pdf page 218]
    چراء چریدن» چراندن / ۲۱۹
```


## [2026-09-05T20:54:51.105Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nlines=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor l in lines[6370:6416]:\n    if l.strip(): print(l.strip()[:200])\nEOF",
 "description": "Read start of Aryanpur chin entry"
}
```


### [2026-09-05T20:54:52.984Z] TOOL RESULT

```
پسگشت‌ها ادلی اد اد ان 8 (038۷) :02/10/5
0 وه موه 37
4 (008) +8۸07 9 (118۷)) 21/00
6 (۸1260783) دی ۱ ادا برهان قاطع : 1۶۳
46 (038۷) ۰ +12 ۸/۸
باه‌داشت.
چم این واژه در زبان لاتین: لثه.
چم این واژه در فریزی کهن: دندان کرسی.
اوستایی (478:87۸۷): 202 گالی (4ل8لال0۸): ید نا
پارسی باستان (۷لفاق28۴ ۰:01 1۸1۸۰ برتونی (/88570): زانیا
پهلرق (۲1مال(۸): ,کتفاققات بالقتتن
۱ ۸7 62ه 0 ,انیت پسگشت‌ها ارش مرش در
۰ کردی (80/طل): هرن ۳
۱ سانسکریت (54(/598077). :۸4۸/215
1 بمفگفقشا مهف 1 ,130 (83۸18210) ,101 (173آقغخ)
بلفاری (/(فللهماناه). آهفتن 5 (053) :۸/00
لیترانی (/0فهفنا 7 610831 1178110 برهان قاطم. ۶۸-۹ و ۶۱۱-۶۱۳
ایرلندی کهن (/1875 ا0): اراد ی
ا آوستایی (//۲897۵): ۰ 6820717 +7200 ارمنی (/(4۳۸48/۷]۵):(شاید) ار
۱ کردی (ا8اهن): 0338716 ,۲1788 برنانی 082880): ۰ 02۸11108 ,60808
۱ افغانی (پشتو) (470۸1): 72۸ لاتین (7100ما): ۸5 ب۸اه05
نخاری 4 (۸ ۰:70:۸4 8۸0۷8۸1 گوتیکه (0077716): دزانن !۱۹
سانسکریت (54۸/۶8/7): 11۸0008 ,11۸01 ایسئندی کهن (/(7070۸۸(ف3 صا0):
[pdf page 217]
۹۸ جیپ
دای گالی (8[7لدانامه): لدن
نررس کهن (۸082 ص0): دای ولزی (8ا8): ت۵۲ ,080
ساکسونی کهن (242000 ۰:00 118۸۷1 برتونی 11۳0887000 0201017
فریزی کهن (50/ل۶7 0۱): ۰ ۳۸ ,210 رن
آلمانی کهن (0574۸0 104 صا۵): پسگشت‌ها اههد
11817 81 بطق ۸0
آلمانی (0572/۸0۷): لرل۹ ۱ ۱ 66 (731)) +8۸۲7
انگلیسی کهن (بلوابا80 صا0): 2 و9 :0515
انگلیسی (تلولا5۸/0): )2 20224 علاط
دانمارکی (18(م0): دای 0 (01313) :0702/5
سوئدی (31707377): 0 7 (110)) +347
نروژی (لما0 :0/0 0 9و (ت0) ام
۱ هلندی (3ع07): لا برهان قاطع + ۶۶
لیتوانی ((714ل4ل724/): 20۸5 لغت‌نامه دهغدا : ۸۳۰
لترنی (لتی) (لا7۶م): نراد اما فرهنگ معین : ۱۳۶۹
1 ایرلندی کهن (لافتگا ۰:0۵ 65۸ ,610
یادداشت.
۱ هبچیکك از پسگشت‌های فارسی ذکری از ریشه‌ی این واژه نمی‌کنند.
۲ این واجريشه در برخی از زبان‌های هند و اروپایی دارای چم‌های دیگری نیز بوده است: آرواره» گونه» دهان,
پارسی باستان (۶8۶1۸۷ 012): 2117۸185 لینوانی (01۵/4هتاب7لا). 1۸5
کردی (0[57نام): وا
```


## [2026-09-05T20:55:01.890Z] TOOL CALL #51: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%DA%AF%D9%88%D9%86%DB%8C%D8%A7/\" \"https://en.wiktionary.org/wiki/%CE%B3%CF%89%CE%BD%CE%AF%CE%B1\"; do python3 tools/fetch_source.py \"$u\" --note \"page 172 entry 0 node 5: Persian gūniyā from Greek gōnia (Mo'in / Wiktionary)\"; done",
 "description": "Fetch Mo'in guniya and Greek gonia"
}
```


### [2026-09-05T20:55:06.274Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/35b42eb035c2e5cb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0ec33c846342072c.txt
```


## [2026-09-05T20:55:09.719Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### abadis guniya\"; grep -n \"معین\\|گونیا\\|یونان\\|فرهنگ\" 35b42eb035c2e5cb.txt | head -25; echo; echo \"### gonia\"; grep -n -A8 \"Ancient Greek\" 0ec33c846342072c.txt | head -40",
 "description": "Read Mo'in and Greek gonia entries"
}
```


### [2026-09-05T20:55:09.800Z] TOOL RESULT

```
### abadis guniya
4:TITLE: گونیا - معنی در دیکشنری آبادیس
6:گونیا - معنی در دیکشنری آبادیس 
10: گونیا
20: گونیا. ( اِ ) مثلث شکلی قائم الزوایه ، چوبین یا فلزی که معماران و نجاران بدان قائمه بودن زوایا یا آلات و چهارچوب در را معلوم کنند. و از آن برای کشیدن خطی عمود بر خط دیگر و یا خطی موازی با خط دیگر نیز استفاده نمایند. اصل کلمه از یونانی گ ، نی یا بمعنی زاویه است. آلت هندسی سه گوش. ( از برهان قاطع ) ( انجمن آرا ) ( غیاث اللغات ) : 
22:یا مسطر و گونیاش بخشم. خاقانی ( از تحفة العراقین ).
23:|| ریسمانی را گویند که استادان بنا چون خواهند عمارتی بسازند آن را بکشند و رنگ عمارت را بریزند. ( برهان قاطع ) ( انجمن آرا ). رژه. رژه بنا: شاقول ؛ سنگی که به ریسمان کرده از گونیا بیاویزند تا بدان همواری زمین معلوم کنند. ( منتهی الارب ). 
25: فرهنگ فارسی
28:( اسم ) ۱ - آلتی چوبین یا فلزی بشکل مثل قائم الزاویه دارای یک زاوی. ۹٠ درجه و دو زاوی. ۴۵ درجه ( معمولا ) در دو گوش. مجاور و آن برای ترسیم زاویه و خط عمودی بکار رود . برای ترسیم خطوط متوازی از دو گونیا استفاده میشود . بنایان و نجاران نیز از گونیا های بخصوص استفاده میکنند : کو نوح که ساز هاش بخشم یا مسطر و گونیاش بخشم . ( تحفه العراقین ) ۲ - ریسمانی که استاد بنا بوسیل. آن رنگ عمارت را میریزد . ۳ - قطع. آهن صاف بشکل یا که برای محکم کردن بند و بست چوب بکار رود . ۴ - آلتی برای اندازه گرفتن قطر اشیائ استوانه یی . ۵ - شاغول . 
30: فرهنگ معین
34: فرهنگ عمید
38: فرهنگستان زبان و ادب
44: گونیا ابزاری است به شکل مثلث از جنس فلز، پلاستیک یا چوب که از آن برای رسم زاویه قائمه و کشیدن خطی عمود بر خط دیگر یا خطی موازی با خط دیگر استفاده می کنند. گونیا از ابزار پرکاربرد در معماری و مهندسی و از ابزار کاربردی دانش آموزان در کلاس های ریاضیات و هندسه است. 
45:در برخی مواقع زبانه گونیا مدرج نمی باشد که در این صورت فقط برای صحت گونیایی بودن قطعه کار و خط کشی استفاده می شود. ولی اگر زبانه گونیا مدرج باشد علاوه بر خط کشی، برای اندازه گیری نیز می توان از آن استفاده کرد. 
46:معمولاً دو دسته گونیا ساخته می شود: یکی گونیا با گوشه های ۹۰ و ۶۰ و ۳۰ درجه و دیگری گونیا با گوشه های ۹۰ و ۴۵ و ۴۵ درجه. 
47:• گونیای معمولی ( گونیای ۹۰ درجه ) :
48:این گونیا از یک زبانه و یک بازو تشکیل شده که زبانه تحت زاویه ۹۰ درجه داخل بازو قرار گرفته است. این گونیا از نظر جنس دارای انواع مختلف چوبی، فلزی و ترکیبی از چوب و فلز و در طول های ۱۵۰، ۲۰۰، ۲۵۰، ۳۰۰ میلی متر ساخته می شود. 
49:• گونیای فارسی ثابت:
50:در بیشتر کارهای قاب سازی و غیره زاویه ۴۵ درجه مورد نیاز می باشد. به این منظور برای سهولت در کارها گونیایی ساخته شده است که زاویه ۴۵ درجه را می توان با آن رسم کرد. و از آنجایی که برش های ۴۵ درجه را در کارهای صنایع چوب، فارسی می گویند نام این وسیله گونیای فارسی ثابت نام دارد. تیغه این گونه نسبت به دسته آن تحت زاویه ۴۵ درجه قرار گرفته است، البته به وسیله این گونیا می توان دو زاویه ۴۵ و ۱۳۵ درجه را ترسیم کرد. 
51:• گونیای تاشو:
52:هرگاه بخواهیم روی قطعه کار زوایای مختلف ایجاد کنیم از گونیای تاشو استفاده می کنیم. گونیای تاشو وسیله ساده ای است و در شرایط مختلف به صورتهای گوناگون ساخته می شود. این وسیله را می توان تماماً از جنس چوب، فلز، پلاستیک یا ترکیبی از فلز وچوب ساخت. این گونیا از یک بازو و یک زبانه تشکیل شده است، زبانه آن از قسمت وسط دارای شکافی است که باعث می شود زبانه به عقب و جلو حرکت کند. نکته ایی که در مورد گونیای تاشو باید بدانیم این است که این وسیله دارای درجه بندی نیست؛ بنابراین در هنگام استفاده از گونیای تاشو لازم است که از نقاله نیز استفاده شود. بدین صورت که پس از تنظیم، با مطابقت گونیا با یک نقاله، مقدار زاویه را تنظیم می کنیم. 
53:• گونیای چرخنده
54:گونیای چرخنده شکل دیگری از گونیای تاشو است این گونیا از دو بازو تشکیل شده است که با پیچی حول یک محور می چرخد و به وسیله آن می توان زوایای خارجی و داخلی قطعه کار را امتحان کرد. گونیای چرخنده همچنین برای رسم زوایای مختلف استفاده می شود. با این گونیا می توان زوایای ۵ تا ۱۸۰ درجه را ترسیم کرد. 
55: wiki: گونیا 
57: گونیا (صورت فلکی). گونیا ( به انگلیسی: Norma ) یکی از صور فلکی جنوبی است که با صورت فلکی کژدم همسایه است که نام اولیه آن خط کش و بعد خط کش تی و بعداً به نام گونیا درآمده است کاشف این صورت فلکینیکلاس لوئیس د لاکایله ( به انگلیسی: Nicolas Louis de Lacaille ) است که ابتدا نام فرانسوی L'Équerre et La Règle را به معنی خط کش و گونیا بر آن نهاده بود. 
58:گونیا ستاره آلفا یا بتا ندارد پرنورترین ستاره آن ستاره گاما گونیا است که ستاره ای دوتایی است و همدم آن HJ 4841 نام دارد. 

### gonia
57: Ancient Greek 
58-
59: Toggle Ancient Greek subsection 
60-
61- 1.1 
62- Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
--
196: Ancient Greek
197- [ edit ] 
198-
199- Etymology
200- [ edit ] 
201-
202- Inherited from Proto-Hellenic *gonwía , from *gónu ( “ knee ” , whence γόνυ ( gónu ) ) , ultimately from Proto-Indo-European *ǵónu ( “ id ” ) . The long ω ( ō ) is from the regular Doric development of an unattested *γονϝ-ία ( *gonw-ía ) , as the paradigm of *ǵónu shows no lengthened grade (thus precluding a derivation from such an ablaut), while most mathematicians in Greek antiquity (who were most likely responsible for the word's formation) were Pythagorean (and thus wrote in Doric). [ 1 ] Despite superficial and coincidental similarities, unrelated to Sanskrit कोण ( koṇa , “ corner, angle ” ) .
203-
204- Pronunciation
--
300: This table gives Attic inflectional endings. For declension in other dialects, see Appendix:Ancient Greek dialectal declension .
301-
302- Derived terms
303- [ edit ] 
304-
305- ἄγωνος ( ágōnos ) 
306- ἀντιγώνιος ( antigṓnios ) 
307- ἀπειρόγωνος ( apeirógōnos ) 
308- γώνιος ( gṓnios ) 
--
377: Inherited from Ancient Greek γωνία ( gōnía ) .
378-
379- Noun
380- [ edit ] 
381-
382- γωνία • ( gonía )  f ( plural γωνίες ) 
383-
384- ( geometry ) angle
```


## [2026-09-05T20:55:21.162Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SYN zafar ==\"; grep -n \"zafar\\|zafan\" SYN.txt | head; echo \"== SYN 4.24 mouth ==\"; grep -n \"4.24 MOUTH\\|4.24. \" SYN.txt | head",
 "description": "Grep Buck for Avestan zafar"
}
```


### [2026-09-05T20:55:21.223Z] TOOL RESULT

```
== SYN zafar ==
5792:5. ON kjoptr (Dan. kaft, Sw. kaft now more like ‘mug’), OE ceafl, ME cha- vel, NE jowl (in part), MHG kiver, kivel, NHG kiefer, LG keve (> Dan. keve) : Av. zafar- ‘mouth’ (of evil beings). Walde-P. 1.570f. Falk-Torp 518, 521. Hellquist 544, Weigand-H. 1.103. NED s.v. jowl, sb.1.
5922:4.24 MOUTH Grk.  orépa Goth. munps Lith.  burna NG oroya ON munnr (midr) Lett. mute Lat. Gs Dan. mund ChSl. usta It. bocca Sw. mun SCr. usta Fr. bouche OE mip Boh. iista Sp. boca ME mouthe Pol. usta, geba Rum. gurd NE mouth Russ. rot Ir. gin, béoil Du. mond Skt. mukha-, Gs-, ete, NIr. _béal OHG mund Ay. Gh-, zafar- W. geneu MHG munt Br. genou NHG mund
5946:Av. zafar- ‘mouth’ (of evil beings) : OE ceafl, NHG kiefer ‘jaw’. Walde-P. 1.570f. Barth. 1657.
== SYN 4.24 mouth ==
3112:5. Lat. amita ‘father’s sister’, deriv. of pet name of the amma type (above, p. 94). Hence, with extension at the expense of matertera, OF r. ante (> ME, NE aunt), Fr. tante (> Du., NHG., Dan. tante) with t variously explained, and with dim. suffix Rum. matusd. Walde-P. 1.53. REW 4024, Wartburg 1.89.
5922:4.24 MOUTH Grk.  orépa Goth. munps Lith.  burna NG oroya ON munnr (midr) Lett. mute Lat. Gs Dan. mund ChSl. usta It. bocca Sw. mun SCr. usta Fr. bouche OE mip Boh. iista Sp. boca ME mouthe Pol. usta, geba Rum. gurd NE mouth Russ. rot Ir. gin, béoil Du. mond Skt. mukha-, Gs-, ete, NIr. _béal OHG mund Ay. Gh-, zafar- W. geneu MHG munt Br. genou NHG mund
13189:4. Skt. mila-, perh. (as the plant’s organ of drinking; cf. pdadapa- ‘tree, plant’, lit. ‘drinking with the foot’) : OHG mila ‘mouth, snout’, etc. (4.24) Wackernagel, Berl. Sitzb. 1918.410.
21970:Grk. oréua ‘mouth’ (4.24) was some- times used (through ‘front’), for the ‘point’ (Hom.) or for the ‘edge’ (Aesch.), of a weapon, e.g. oréya paxalpas ‘edge of a sword’ in LXX and NT, rendered liter- ally ds gladii in the Vulgate, this again (Lk. 21.24) by OE mip suordes in Lin- disf. vs. swurdes ecg in WSax. versions, likewise OHG mund suertes in Tat. (in Goth. the passage is lacking).
26090:Grk. yevouat, sb. yedous; Lat. (fr. pple. *gusto-) gustare (> It. gustare, Fr. gotter, Sp. gustar, Rum. gusta) sb. gustus (> It., Sp. gusto, Fr. goat, Rum. gust) and gus- tatus; Goth. kiusan ‘make trial of, prove’ (renders doxipatw), OE céosan ‘choose’, Goth. kausjan ‘taste of’ (renders yebouar, in lit. sense Lk. 14.24, elsewhere as in ‘taste of death’; sb. kustus quotable only as ‘trial, proof’), OE costian ‘try, prove, tempt’, OHG koston ‘try’, MHG, NHG kosten ‘taste of’; Skt. jus- ‘enjoy, be pleased’, Av. zaoga- ‘pleasure’.
28222:ChSl. strastt (Bacavos Mt. 4.24, raos, awa0nua, Supr.), Russ. stradanie : Chsl. stradati, Russ. stradat’ ‘suffer’, general Slavic, ChSI. strada ‘labor, toil’, perh. fr. the root of Grk. orepeds ‘firm, stiff, hard’, NHG starr, etc. ‘stiff’. Walde-P. 2.628. Miklosich 324.
```


## [2026-09-05T20:55:24.269Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\n# find page-like markers\nfor target,ln in [('jowl',20399),('chafer',7112)]:\n    print('---',target)\n    for i in range(ln-1,max(0,ln-14),-1):\n        s=lines[i-1].strip()\n        if re.fullmatch(r'\\d{2,4}', s) or re.match(r'^\\d{2,4}\\s', s):\n            print('  marker at line',i,':',s[:80]); break\n    print('  context:', lines[ln-3][:120],'||',lines[ln-2][:120])\nEOF",
 "description": "Find Klein page markers"
}
```


### [2026-09-05T20:55:27.388Z] TOOL RESULT

```
--- jowl
  context: meaning  ‘bom  under  the  planet  Jupiter;  joy¬ ful’  (this  planet  having  been  regarded  as  the source  of  joy), || Jovian,  adj.,  1)  pertaining  to,  or  resembling, Jupiter;  2)  pertaining  to  the  planet  Jupiter.  — See  Jove  a
--- chafer
  marker at line 7107 : 265
  context: chafe,  tr.  v.,  1)  to  warm  by  rubbing;  2)  to  irritate by  rubbing;  3)  to  irritate;  intr.  v.,  1)  to  rub; || Derivatives:  chafe,  n.,  chafer  (q.v.) chafer,  n.,  a  vessel  for  heating.  —  Formed  fr.
```


## [2026-09-05T20:55:39.212Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nlines=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nimport re\ndef markers(around, back=40):\n    out=[]\n    for i in range(around, max(0,around-back), -1):\n        s=lines[i-1].strip()\n        if re.fullmatch(r'\\d{2,4}', s): out.append((i,s))\n    return out\nprint('chafer', markers(7112))\nprint('jowl', markers(20399, 60))\nEOF",
 "description": "Find nearest page markers in Klein"
}
```


### [2026-09-05T20:55:41.053Z] TOOL RESULT

```
chafer [(7107, '265'), (7106, '264')]
jowl [(20382, '833'), (20363, '832')]
```


## [2026-09-05T20:56:10.086Z] TOOL CALL #56: Bash

```json
{
 "command": "ls site/pages/172.jpg 2>/dev/null; ls data/verification/sources/refs/ocr/BOOK/ 2>/dev/null | head; pdftoppm -f 172 -l 172 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg172 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg172.png",
 "description": "Render PDF page 172"
}
```


### [2026-09-05T20:56:12.721Z] TOOL RESULT

```
site/pages/172.jpg
100.png
101.png
102.png
103.png
104.png
105.png
106.png
108.png
109.png
110.png
-rw-rw-r-- 1 sfmqrb sfmqrb 73400 Sep  5 16:56 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg172.png
```


## [2026-09-05T20:56:15.352Z] TOOL CALL #57: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg172.png"
}
```


### [2026-09-05T20:56:15.740Z] TOOL RESULT

```

```


## [2026-09-05T20:56:15.713Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:58:30.693Z] TOOL CALL #58: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T20:58:30.726Z] TOOL RESULT

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


## [2026-09-05T20:58:34.881Z] TOOL CALL #59: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/ 2>/dev/null | head",
 "description": "Check VIE local files"
}
```


### [2026-09-05T20:58:34.920Z] TOOL RESULT

```
total 4696
drwxrwxr-x  3 sfmqrb sfmqrb    4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb    4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb  627891 Sep  4 14:06 VIE_pages.txt
drwxrwxr-x  2 sfmqrb sfmqrb   12288 Sep  4 13:23 VIE_pages.txt.pages
-rw-rw-r--  1 sfmqrb sfmqrb 4150115 Sep  4 14:06 VIE_sajjadieh1364_parsianjoman.pdf
```


## [2026-09-05T20:58:35.980Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^chin\\|chin, n\" KLN_1966.txt | head -3; echo \"== diagonal/polygon ==\"; grep -n \"diagonal, adj\\|polygon, n\" KLN_1966.txt | head -3",
 "description": "Grep Klein for chin and diagonal"
}
```


### [2026-09-05T20:58:36.044Z] TOOL RESULT

```
7422:chine,  n.,  backbone  of  an  animal.  —  ME.  chyne, ‘back’,  fr.  OF.  eschine  (F.  echine),  fr.  Frankish *skina.  Cp.  OHG.  scina,  ‘needle,  prickle;  shin¬ bone’,  and  see  shin.
7423:chine,  adj.,  figured  after  the  Chinese  fashion.  — F.,  pp.  of  chiner,  ‘to  color  differently,  mottle, figure’,  lit.  ‘to  color  after  the  Chinese  fashion’, fr.  Chine,  ‘China’.  See  china.
7425:chink,  n.,  split,  crack.  —  Formed  fr.  chine,  ‘fis¬ sure’,  with  dimin.  suff.  -k.
== diagonal/polygon ==
```


## [2026-09-05T20:58:42.737Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE && grep -n \"\\[pdf page 1[0-9]\\]\" VIE_pages.txt | head; python3 - <<'EOF'\nimport re\nt=open('VIE_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', t)\nd={}\nfor i in range(1,len(parts),2):\n    d[int(parts[i])]=parts[i+1]\nfor p in [12,13,14,15,16]:\n    if p in d:\n        print('=== pdf page',p,'===')\n        print(d[p][:900])\nEOF",
 "description": "Read VIE page 12"
}
```


### [2026-09-05T20:58:44.318Z] TOOL RESULT

```
182:[pdf page 10]
213:[pdf page 11]
244:[pdf page 12]
270:[pdf page 13]
310:[pdf page 14]
328:[pdf page 15]
355:[pdf page 16]
378:[pdf page 17]
406:[pdf page 18]
438:[pdf page 19]
=== pdf page 12 ===

پاورقی‌ها :

(- درپیشگفتار چاپ دوم "خودآموز سانسکریت )‌نوشته محمد علی
داعی‌الا سلام یادآوری شدم که گانی جی رهبر بزرگ هندوستان به هندیان
اندرز کرده بود گه سانسگریت و فارسی را فرا بگیرند و هندوستان گه روزی
بزرگترین جایگاه گسترش زبان فارسی بود و تا ۵۰ سال پیش نام پادشاهان
انگلستان را نیز به فارسی بر سکه‌های هندی می‌زدند .۰۰ با یورش گسترش
خواه انگلیس » هنوز یاران نزدیگ گاندی بر آن کشور فرمان می‌رانند که
انگلیسی جای فارسی را گرفته است و نخست‌وزیر (ایندیرا گاندی ]پامردمش
به انگلیسی سخن می‌راند .۰

امروزه شنیده می‌شود گه زن و شوی در خانه با خود و فرزندان » بسه
انگلیسی هندی سخن می‌گویند و اگراز آنان بپرسی که چرا چنین می‌کنند ‏
پاسخش این است که در آینده برای کاریابی و اندرشدن‌به‌دیوانهای‌کشوری
دانستن انگلیسی‌برای فرزندان بهتر است .

۲ شوروی خط گرجستان و ارمنستان را برسمیت شناخت و اجازه داد

۱ که کشورهایروپایی نیز خط لاتین خویش را نگهدارند اما دیگر کشور های
قفقاز » و تاشکند و سمرقند و بخار) و سغق
=== pdf page 13 ===

شیرین فارسی را که بگفته اینگلس تنها زبانی است که می‌تواند جهانی شود
(نگاه کنید به مجموعه آثار مارکس - اینگلس » ترجمه فارسی. جلد ۲۸ رویه
های ۲۶۰-۲۶۱ و نیز کارناهه* ابن سینا رویه ((۱] در زیر تیغ خطروسی‌و
زبان روسی » در زادگاه رودذگی از میان بردارند ! :

۳ تاریخ مهندسی در ایران - دگتر مهدی فرشاد » ازانتشارات‌بنياد
نیشابور » رویه‌های ۲۳۸-۳۳۱

۴ گارنامه این سینا » فریدون جنیدی » رویه‌های ۸۴-۸۵

۵ تاریخ مهندسی در ایران رویه‌های ۱۴۳

۶ همان دفتر رویه* ۰۹(

۷-ایرانیان این واژه‌ها را به زبان تازی چنین ترجمه گردند ؛ ظل ,
جیب » ظل تمام »جیب تمام .

۸ خوشبختانه این کار در گتایهای دی آغاز شده است »اما بسنده
نیست و می‌باید که با پژوهشی گسترده‌تر در آینده دنبال شود .

۳۹۸ ‏سهم ایران در تمدن جهان » نیز نوری رویه‎ ٩

۰ (- تاریخ یزد » جعفری رویه ۱۰۵و ۱۰۳ و نیز تاریخ مهندسی درد
ایران ۰۱۳۴

( (-نگاه کنید به فرهنگ پيشه و هنر » دکتر سیروس ابراهیم زاده ۰
بویژه پیشگفتار آن .

7 - میراث ایران نوشته سیزده‌تن خاو
=== pdf page 14 ===

: یک کاسه می‌خورند » و همراه همه آنانند که در یک راه می‌روند » همداد نیز
همه* چیزها و گسانی را گه از یک داد (قانون ) پیروی می‌کنند تأابه‌یگ‌هدف
برسند » در بر می‌گیرد !

سعید وزیری در روستای مهاباد آردستان واژه* هنداد را نیز شنیده
است .

۴ در همین دفتر به نمونه‌ای چند از این گونه واژه‌های اروپابی بر
خواهید خورد .

۵ - نگاه کنید به فرهنگ سمنانی » سرخه‌ای » [ا سگردی » سنگسری »
شهمیرزادی دکتر منوچهر ستوده » رویه‌های یازده » دوازده و سیسزده از
پیشگفتار .

۳
1
۸

=== pdf page 15 ===

و من آیاته خلق‌السموات والارض و اختسلاف
السنتکم والوانکم ان‌فی ذلک‌لایات‌للعالمین"
و در آیات او خلق آسمان و زمین و اختلاف
زبانها و رنگهای شماست بدرستی که درآن
نشانه‌هایی برای دانشمندان وجود دارد"
سوره روم -آیه ۲۲
سخن نویسنده :
زبان های فارسی وانگلیسی هردو به دسته زبان های آراگی ( وی به
اصطلاح هندوارویائی )تعلق دارند .بهمین دلیل واژهای مشابه بسیار میان
دو زبان آدیده می شود . آما علاوه بر این واژه های پایه وهمانند مثل مادر
برآدر - پدر کلمات بسیاری هم در دوره‌های بُعدی تاریخ از زبان مردم ایرآن "
وارد زبان آنگلیسی شده است بعضی از این واژه ها از زبان های آوستاعی و
پهلوی و فارسی باستان و بعضی واژه‌ها از زبانهای سومری و ایلامی و غیره
و بعضی واژه ها از زبان ها و گویش هاأی دیگر سرزمین ایران امثل آذری »
کردی » بلوچی‌به زبان آنگلیسی راه یافته اند که این کتاب نموداری از ان
واژه‌ها است . برای تکمیل مطلب سطوری هم به نفوذ ريشه های آبرآنی در
زبان های دیگر مردم انگلستان [ ولش» اسکاتلندی » ایرلندی وغیره 
=== pdf page 16 ===

بحثی پیرامون ريشه های مشترک ایرانی وانگلیسی

محققانی‌که درباره* تاریخ اقوآم‌هند وآروپائی بحث کرده‌اند ستقدند
این اقوام پس‌ازانشعاب به دسته‌های آمتعدد در سرزمین های مختلف سکنی
گزیده‌اند از جمله بخش هائی از ان اقوام در ایرآن و هندوستان وبخش-
های بزرگی درقسمت های مختلف آروبا مثل ایرلند ۰ انگلیستان » آلمان " 0
فرانسه وایتالیا متممرکز شده‌اند.اصطلاح هند و اروپایی که توسط نویسندگا ان
غربی بکار رفته احتمالا " خالی‌ازغرض نیست و شاید در آن نوعی چسبانیدن
منافع استعماری انگلیس به خطه زرخیز هندوستان مطرح بوده باشد.ازآنجا
که وآژه زبان های آریائی رساتر و اصلی‌تر ومناسب تر است وعلاوه بر هندو
اروپْا متاطق وسیعی مانند ایرآن و آسیای صغیر وافغانستان‌را در بر می‌گیرد.,
دراین کتاب غالبا از آین واژه استفاده می شود .

ناگفته نماند واژه" آریائی " قدمت چندین هزار ساله دارد و ريشه *
آنراً می تون در اوستا درزبان هندوان » در نام آیرآن ؛ ونام مردم آیرلند
یافت ۰ کاربرد این واژه به هیچ عنوان برای مقاصد غیرعلمی نژادپر
```


## [2026-09-05T20:58:52.010Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE && grep -n \"چانه\\|زنخ\\|CHIN\\|chin\\b\" VIE_pages.txt | head -20; echo \"=== pdf 26-28 ===\"; python3 - <<'EOF'\nimport re\nt=open('VIE_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', t)\nd={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}\nfor p in [25,26,27]:\n    print('=== pdf',p,'==='); print(d.get(p,'')[:700])\nEOF",
 "description": "Search VIE for chin"
}
```


### [2026-09-05T20:58:54.162Z] TOOL RESULT

```
418:صذج انگلیسی » چانه فارسی » چنه ترکی آذری وخراسانی» ۲6۵
2813:داردروقوط بد رصق چانه‌مرتورژهتورانی ( همهم انگلیسی) ‏ ذوعة
6362:ریشه‌های ایرانی در زبان انگلیسی چانه میزدند و باناباوری نشان میدادند
=== pdf 26-28 ===
=== pdf 25 ===

عمل نام سوسن ایرآنی را در خارج سوزان تلفظ می‌کنند ) ۰ :۱

۷ مروونی شکر ؛ازکلمات کمیابی است که خوداروپٌائیان تیزتصریح
به آیرانی بودن آن دارند .درانگلیسی شوگر درفتلاندی 1نزه»[501 در ترکی
شکر مرصهزم8 ودرآلمانی مرصلمن2 درفرانسه وم‌8» درعربی سکر در
روسی ساخار و درمجاری مرنءلر0 سوکور دیده می شود . بعلاوه وازه‌های
مشابه زبان های ژاپنی --ایتالیائی » اسپانیولی - پرتقالی و دیگر زبانهای ی
آروپا یافت می شود .
از این ريشه واژه‌های متعددی مثل مادم مه‌ونا 5‏ نی‌شکر 200هی.

وله قند شکن پطهودا8شکری .

درفرهنگهای آنگلیسی به چشم می‌خورد .

ها : چنانچه اسقف دانشمند آدی‌شیر درکتاب آنفیس خود واژه"
های قارسی درزبان عربی پشان داده اسث اصل این کلمه ایرانی و یمفهوم
آنگور سیاه است ( رجوع شود به برهان قاطع » ص ۱۱۸۹)از
=== pdf 26 ===

آیرآن بوده و در دوران هخامنشی یکی اززبان های رسمی ایرآن امحسوب می
شده است .

هعلة اصل این واژه انگلیسی ‏ الو فارسی است که نوعی صمغ می
باشد . ( برهان ص ۱۱۲) +ویعنی جودی که تبخبر می‌شود بکار می رود -

ومه‌رمرن این واژه بصورت صاوعه‌رصنه در رومی ( لاتین) و با
تلفظی کم و بیش مشأابه دریونانی دیده می‌شود . باعتقاد آدی‌شیر این‌واژه
دگرگون شده وگرفته شده آزفارسی سروناز اسث . شاید ريشه کلمه ورین
که نام کشور و جزیره بزرگی است و مدتها جزو مستملکات ایران هخامنشی
بشمار می‌آمد از این وأژه‌گرفته شده باشد .

60 اسفتاج این واژه ایرانی در زبان های دیگر به صورت
گوناگون یافت می‌شود از حمله درقتلاند 2321-18 پیناتیا » در انگلیسی
و فرانسه 50372010 و درزبان های دیگر آروپائی کم وبیش باتغییراتی کار
برد دارد .

اسفتاج
=== pdf 27 ===

0[ صع11۶[10چ به نی کلم است . باتوجه به شباهت این
ريشه‌هاً امکان دارد این واژه‌ها هم ريشه ایرآنی‌داشته باشد .

۱ مهطمی تیلوفر زرد ۰ مرهطاص جر ۸تبلوفر » نام گل زیبای‌تیلوفر
است که درزبان های دیگر آروپا از حمله فرانسه - یونانی - ترکی دیده می
شود ۰

م‌ومرچن نارنج وترنح درپارسی کهن به نارنج و پرتقال اطلاق می
شده‌اند » در فرانسه و‌وورومرن درزاینی 021و در زبانهای ترکی ‏ -
کردی » آسوری و بسیاری از زبان های دیگر دنیاً ريشه دوانیده است .
طوحط‌م اصل این واژه راوند و ریباس( ریواس ) است ,واژه های
مشابه در زبان‌های دیگر از جمله ایتالیاعی . فرانسه , انگلیسی ۰ ترکی دید ه
می‌شود
زنجبیل : عه‌طع‌وورزی انگلیسی » 7026۲0 ایتالبانیوططت‌و-دع
فرانسه .

نانه ونعناع ( اورقل۸, 2611۳۳۵ ) در بونانی به گونه منتا درانگلیس
```


## [2026-09-05T20:59:00.150Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE && sed -n '406,438p' VIE_pages.txt",
 "description": "Read VIE page with chin/chane"
}
```


### [2026-09-05T20:59:00.195Z] TOOL RESULT

```
[pdf page 18]
نووی روسی » بنی ترکیآذری و دیگر زبانهای ترکی (ینگه گنه ازهمین
ریشه هستند ([۲) .
م00 دور انگلیسی ین آلمانی » درفارسی ط106 روسی ( دور)
6 آنگلیسی » هورم3 فرانسه » نام فأرسی » (هر13+ فبلاندی حورج2 نام
آلمانی » ناو کردی » نامه جرج فارسی باستان ".
6 انگلیسی » هه‌او آوستاغی ؛ او فارسی » اوو0 ترکی آذری و استانبولی .
آزبکی » فنلاندی . وی پهلوی» اوه 1ج فارسی باستان » و گویش کلیمیان
کاشان ".۰
۵») انگلیسی » (ه70,۳ آلمانی ( ريشه های شبیه درسوعدی » نروزی »
دانمارکی ) گال آرمنی » گل تورانی » گام اوستاشی ( به شباهت گام و گال "
توجه فرمائید ] سگامیذان پارسی گام پهلوی ...
صذج انگلیسی » چانه فارسی » چنه ترکی آذری وخراسانی» ۲6۵
ترکی استانبولی ( ریشه‌های تورانی) .
برای توجه بیشترءتعداد دیگری ریشه‌های مشترک ایرآنی وانگلیسی را
بررسی می کنیم .

۱ مجاورت ومهاجرت به زبانهای دیگر راه یافته . درمفولی وا ستی‌و فنلاً ندی و
مجاری دیده می‌شود . در حقیقت زبان‌های یادشده محصول مهاجرت -
تورانیان و آمیزش آنان با اقوام ساگن آن سرزمین ها بوده است .دراثراین
مهاجرتها تغییراتی در ساختار زبان‌های تورانی حاصل شده و بعضی ویژگی
های دستور زبان ترکی از آن رو است (بهمین دلیل ترک یآذری‌کها زازدواج
زبان تورانی و پهلوی آذربایجان بوجود آمده از دوسو تبار آریایی‌وازدرون
محتوای فرهنگی خالص ایرانی دارد ۰.

۱ این واژه‌ها چون واژه‌های‌)ولین و ابتدایی زبان هستند نمی‌توان

متصور شد که از فارسی به انگلیسی با زبان‌های دیگر راه یافته‌اند و صحیح‌و
درست آنست که این واژه‌ها را همپایه و همريشه بدانیم . در حقیفت ایس
واژه‌ها ازروزگار یگانگی اقوام آریایی (هند واروپایی ) یاد می‌کنند . ازآنجا
که دستور گنونی زبان‌های آریایی در قرن‌های بعد نگوین‌یافته‌می توان‌تجسم
۲
[pdf page 19]
```


## [2026-09-05T20:59:12.118Z] AGENT

Now I'll write the verification file.


## [2026-09-05T21:08:16.508Z] TOOL CALL #64: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-172.json <<'JSONEOF'\n{\n  \"pdf_page\": 172,\n  \"book_page\": 142,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Genu 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ǵónu n. (oblique stem *ǵnéw-) 'knee', with 'angle, corner' in derivatives (Pokorny 'ĝenu-1, gneu-' 380-381; Watkins/AHD 'genu-1. Knee; also angle')\",\n      \"note\": \"Root, language label, gloss and reference are all right. Pokorny's lemma reads 'Root / lemma: genu-1, gneu- (*ghenu-) / Meaning: knee, joint' with 'Page(s): 380-381', so Nourai's POK:381 falls inside the lemma; Watkins's appendix has 'genu-1. Knee; also angle. ... [Pok. 1. genu- 380.]', which is where the 'angle' half of Nourai's gloss comes from — it is justified by the Greek derivative gōnía 'corner' and by Celtic *genwā '(river) bend'. Walde-Pokorny I 586 heads the same entry 'genu- \\\"Knie\\\" (genu-, gonu-, gonu-, gneu-, gnu-)', and Mann glosses it 'ĝenu (ĝón-, gon-) \\\"bend of the leg, knee; angle\\\"'. The whole Iranian side of the chart is Pokorny's own material ('Old Indic jānu, Pahlavi zanuk, npers. zānū; Avestan Akk. Sg. znum, dat. abl. pl. znubyō'). The one thing worth flagging is internal to the chart: Persian zānū (#3) continues the FULL grade *zā́nu-, whereas the Avestan box above it gives the zero grade znu-/znūm; the arrow is right in substance (Old Iranian) but not in grade.\",\n      \"note_fa\": \"خودِ ریشه بی‌عیب است: پوکورنی مادهٔ «ĝenu-1، gneu-» را با معنای «زانو، بند» در صفحات ۳۸۰–۳۸۱ آورده و ارجاع نورایی (POK:381) درست در همان ماده می‌افتد؛ واتکینز در پیوست فرهنگ American Heritage همان را «زانو؛ نیز زاویه» معنی کرده و همین است سرچشمهٔ بخش دوم معنای نمودار، که با واژهٔ یونانی gōnía «گوشه» و سلتی *genwā «خمِ رود» توجیه می‌شود. والده-پوکورنی (ج۱ ص۵۸۶) و مان نیز همین را می‌گویند. مواد ایرانی نمودار (znūm، zānūg، زانو) عیناً از خود پوکورنی است. تنها نکتهٔ درخورِ یادآوری این است که «زانو»ی فارسی از درجهٔ کاملِ *zā́nu- می‌آید نه از درجهٔ صفرِ znu- که در خانهٔ اوستایی آمده است؛ پس پیکان از نظر محتوا (ایرانی باستان) درست است ولی از نظر درجهٔ آوایی دقیق نیست.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%C3%B3nu\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:381\", \"status\": \"supports\", \"note\": \"POK_full.txt lines 35407-35450: 'Root / lemma: genu-1, gneu- {*ghenu-) / Meaning: knee, joint ... References: WP. I 586 f., WH. I 592 f. ... Page(s): 380-381' — the lemma runs across 380-381, so Nourai's page number is inside it.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"POK_full.txt l.35407-35452, pp.380-381\", \"stance\": \"supports\", \"note\": \"'Old Indic jānu n. \\\"knee\\\", Pahlavi zanuk, npers. zānū \\\"knee\\\"; Avestan Akk. Sg. znum, dat. abl. pl. znubyō ... lengthened grade γωνία \\\"point, edge\\\" (*γωνϝια) ... Gothic kniu, Old High German knio, kneo (*kniwa-, Indo Germanic *gneuo)'.\"},\n        {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt l.55760-55790, Bd. I 586-587\", \"stance\": \"supports\", \"note\": \"'genu- \\\"Knie\\\" (genu-, gonu-, gonu-, gneu-, gnu-). Ai. jānu \\\"Knie\\\", pehl. zanūk, np. zānū \\\"Knie\\\"; av. acc. sg. znūm, dat. abl. pl. znūbyō ... dehnstufig ... γωνία \\\"Ecke\\\" (*γωνϝ-ία) ... got. kniu, ahd. knio, kneo \\\"Knie\\\"'.\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.492, s.v. genu-1\", \"stance\": \"supports\", \"note\": \"'genu-1. Knee; also angle. 1. Variant form *gneu- in: a. Germanic *knewam in Old English cnéo, knee: KNEE ... 3. Suffixed variant form *gon-ya- in Greek gōnia, angle, corner: -GON, GONION; ... DIAGONAL ... [Pok. 1. genu- 380.]'\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt l.5655 and l.5705, s.v. ĝenu / ĝonu\", \"stance\": \"supports\", \"note\": \"'ĝenu (ĝón-, gon-) \\\"bend of the leg, knee; angle\\\". WP I, 586. Skt. jānu; Av. žnu; Per. zānū; ... Gk. gónu; Lat. genu; Go. (metath.) kniu; OE cneow'.\"},\n        {\"src\": \"SYN\", \"where\": \"SYN.txt l.5652 area, Buck 4.36 / 4.207 note\", \"stance\": \"supports\", \"note\": \"Buck (quoted by Mann at IEC l.5652 and in Buck 4.207 itself) treats the 'chin' group and the 'knee' word as linked 'through some common notion like \\\"angle\\\"'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"žnu, znum\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The Avestan word for 'knee' is the zero-grade stem znu-/znav-: Bartholomae AiW s.v. has 'j. znav-, xšnav-; šnav- n. \\\"Knie\\\"' (Vd. 8.61-63, 6.27), and Pokorny cites exactly the two forms Nourai prints — 'Avestan Akk. Sg. znum, dat. abl. pl. znubyō'. The initial z- is the regular Iranian reflex of the PIE palatal *ǵ (PIE *ǵ > Av. z, OP d, Skt. j; cf. Av. zasta- : OP dasta- 'hand'), and the zero grade *ǵnu- arises by loss of the root vowel in the oblique stem *ǵnéw-. Nourai's spelling 'žnu' is not a misprint: it is Mann's citation form ('Av. žnu', IEC s.v. ĝenu; 'Av. žnus', s.v. ĝonu), while Gharib and Bartholomae write znu-. Avestan also has the full grade, in the compound zānu.drājah- and in Bartholomae's zānav-, and it is that grade, not znu-, that Persian zānū continues.\",\n          \"derivation_fa\": \"واژهٔ اوستایی «زانو» ستاکِ درجهٔ صفرِ znu-/znav- است؛ بارتولمه در فرهنگ ایرانی باستان می‌آورد: «znav-، xšnav-؛ šnav- خنثی: زانو» و پوکورنی نیز دقیقاً همان دو صورتی را نقل می‌کند که نورایی آورده است: رایی مفرد znūm و برایی-ازی جمع znūbyō. آغازهٔ z بازتاب قانونمندِ کامی‌شدهٔ *ǵ هندواروپایی در ایرانی است (در اوستایی z، در پارسی باستان d، در سنسکریت j؛ سنجید‌ه شود با zasta- اوستایی در برابر dasta- پارسی باستان «دست»). صورت žnu نویسه‌گردانی مان (فرهنگ تطبیقی هندواروپایی) است، نه خطای چاپی. یادآوری: درجهٔ کاملِ اوستایی هم در ترکیب zānu.drājah- دیده می‌شود و «زانو»ی فارسی دنبالهٔ همان است نه دنبالهٔ znu-. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:381\", \"status\": \"supports\", \"note\": \"POK_full.txt l.35420: 'Old Indie yanu n. \\\"knee\\\", Pahlavi zanuk, npers. zānū \\\"knee\\\"; Avestan Akk. Sg. znum, dat. abl. pl. znubyō' — the accusative znum of the chart is Pokorny's own citation form.\"},\n            {\"ref\": \"SOD:184\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, entry 4591 printed on p.184 (SOD_pages.txt l.16849-16851, the page number '184' is printed in the same column): '4591 jnwwq M ... znuk (zʼnwkʼ, jnwq) ©Av. znu; Pahl. šnwk / knee'. Gharib herself gives the Avestan comparandum 'Av. znu' that Nourai's arrow needs.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt l.28566, AiW s.v. znav-\", \"stance\": \"supports\", \"note\": \"'j. znav-, xšnav-; šnav- n. \\\"Knie\\\": daēnəm (bz. …) V. 8.61-63 … frasa fraγžit … āpə ā znubyasčit āpə ā maiδyanas'čit āpə V.6.27'; cf. l.28572 '*znu.barəz- f. \\\"Kniehöhe, -tiefe\\\"'.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt l.5655 / l.5706\", \"stance\": \"supports\", \"note\": \"Mann prints the very form Nourai uses: 'ĝenu … Skt. jānu; Av. žnu; Per. zānū' and 'ĝonu (ĝun) … Av. žnus \\\"knee\\\"; Hitt. kanu-'.\"},\n            {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt l.55761-55762, Bd. I 586\", \"stance\": \"supports\", \"note\": \"'av. acc. sg. znūm, dat. abl. pl. znūbyō; ai. jnu-baḍh- \\\"die Knie beugend\\\", … av. fra-snu- etwa \\\"die Knie nach vorn haltend\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Sogdian\",\n          \"words\": \"jnwwq\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Manichaean Sogdian jnwwq is read znūk: in the Manichaean script <j> writes /z/, so the graphic jnwwq and the Buddhist/Christian spelling zʼnwk are the same word. Gharib's entry 4591 (p.184) reads 'jnwwq M — znuk (zʼnwkʼ, jnwq) ©Av. znu; Pahl. šnwk — knee', i.e. Sogdian znūk continues Old Iranian *znu-ka-, the zero-grade stem plus the productive -ka- suffix that also gives Pahlavi (u)šnūg and, from the full grade, zānūg. Note that Nourai hangs the Sogdian box on the root and not on the Avestan box, which is correct: Sogdian is an East Iranian sister of Avestan, not its descendant. Gharib's separate entry 11365 znwq 'zanu(k) … chin, jaw' belongs to the other root (Genu 2).\",\n          \"derivation_fa\": \"صورت سغدیِ مانوی jnwwq را znūk می‌خوانند، زیرا در خط مانوی حرف <j> آوای /z/ را می‌نگارد؛ پس این نگارش با نگارش بودایی/مسیحیِ zʼnwk یک واژه است. غریب در مدخل ۴۵۹۱ (رویهٔ ۱۸۴) می‌نویسد: «znuk (zʼnwkʼ, jnwq) © اوستایی znu؛ پهلوی šnwk — زانو». بنابراین znūk سغدی از ایرانی باستان *znu-ka- است، یعنی همان ستاکِ درجهٔ صفر با پسوند زایای -ka- که در پهلوی هم (u)šnūg و (از درجهٔ کامل) zānūg را ساخته است. نکتهٔ روش‌شناختی: نورایی این خانه را به خودِ ریشه بسته است نه به خانهٔ اوستایی، و این درست است، چون سغدی خواهرِ اوستایی است نه فرزند آن. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:184\", \"status\": \"supports\", \"note\": \"SOD_pages.txt l.16849-16851 (printed page number 184 visible in the same column): '4590 jnwq => jnwwq / 4591 jnwwq M — znuk (zʼnwkʼ, jnwq) ©Av. znu; Pahl. šnwk — knee. Sogdica 49.8, 50 n p50, GMS 264, 978'. The index (l.38661) confirms 'knee 4591, 11155'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"SOD_pages.txt l.36095-36100, entry 11155 zʼnwk\", \"stance\": \"supports\", \"note\": \"'11155 zʼnwk B — zanuk (zʼnwq, zʼnwk(ʼ)) ©<*zānuka ©ob. pl. — knee' with references TSP 6.83, VJ 97, 374; entry 11157 explicitly equates 'zʼnwk(ʼ) ≃ zʼnwk, jnwwq'.\"},\n            {\"src\": \"PHD\", \"where\": \"PHD.txt l.2533 and l.673\", \"stance\": \"supports\", \"note\": \"MacKenzie's English index 'knee (u)šnūg, zānūg' and the lemma 'zānūg [zʼnwk' | P zʼnwg, N zānū] knee' — the Pahlavi šnwk that Gharib cites for the Sogdian word.\"},\n            {\"src\": \"POK\", \"where\": \"POK_full.txt l.35420\", \"stance\": \"partial\", \"note\": \"Pokorny lists Pahlavi zanuk and npers. zānū under this root but has no Sogdian material at all — silent on jnwwq itself.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"zânu «زانو»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian زانو zānū descends from Middle Persian zānūg (written zʼnwk', Psalter zʼnwg; MacKenzie p.98), from Old Iranian *zā́nu-ka- — the FULL grade *ǵónu/*ǵēnu- plus the -ka- suffix — cognate with Sanskrit jā́nu-, Greek γόνυ, Latin genū, Gothic kniu. The Middle Persian final -g regularly drops in New Persian (zānūg > zānū), exactly as bandag > banda. Mo'in's etymological footnote on the very page Nourai cites (Borhān-e Qāṭeʿ p.1000) reads: 'زانو … پهلوی zānūg از ایرانی باستان *zānu-ka-، هندی باستان jānu-. در اوستا znav- … برخلافِ [بارتولمه] شاید بمعنی (چانه) است. رك: بارتولمه'. The one correction to the chart: the immediate ancestor is the full-grade *zānu(-ka)-, not the zero-grade Avestan znu- drawn as the parent; Middle Persian did continue the zero grade too, but as the separate word (u)šnūg (MacKenzie), and Nyberg records the Southwest doublet dānūk 'knee'. Wiktionary: 'From Proto-Iranian *jā́nu, from Proto-Indo-Iranian *ȷ́ā́nu, from Proto-Indo-European *ǵónu … Doublet of گونیا.'\",\n          \"derivation_fa\": \"«زانو»ی فارسی نو از فارسی میانهٔ zānūg (نوشتهٔ zʼnwk، در زبور zʼnwg؛ مکنزی رویهٔ ۹۸) است و آن از ایرانی باستانِ *zā́nu-ka-، یعنی درجهٔ کاملِ ریشه به‌همراه پسوند -ka-؛ هم‌ریشه با سنسکریت jā́nu-، یونانی gónu، لاتین genū و گوتیک kniu. حذف g پایانیِ فارسی میانه در فارسی نو قاعده‌مند است (zānūg > زانو، چنانکه bandag > بنده). معین در حاشیهٔ همان صفحه‌ای که نورایی ارجاع داده (برهان قاطع، ص ۱۰۰۰) می‌نویسد: «زانو … پهلوی zānūg از ایرانی باستان *zānu-ka-، هندی باستان jānu-؛ در اوستا znav-». تنها تصحیحِ لازم بر نمودار این است که نیای بی‌واسطهٔ «زانو» صورت درجهٔ کامل است نه znu- (درجهٔ صفر) که در خانهٔ بالا نشسته؛ درجهٔ صفر در فارسی میانه واژهٔ جداگانهٔ (u)šnūg را داده است و نیبرگ صورت جنوب‌غربیِ dānūk را هم ثبت کرده. در مجموع ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B2%D8%A7%D9%86%D9%88\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1000\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ, Mo'in's footnote on printed p.1000 (= BQT_v2_pages.txt form-feed chunk 463; the neighbouring headwords زفر=1024 and زنخ=1036 fix the offset at +537): '# زانو … پهلوی zānūg از ابرانی باستان *zānu-ka-، هندی باستان jānu-. در اوستا znav- … رك: بارتولمه'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD.txt l.673, s.v. zānūg\", \"stance\": \"supports\", \"note\": \"'zānūg [zʼnwk' | P zʼnwg, N zānū] knee'; the English index (l.2533) gives 'knee (u)šnūg, zānūg', i.e. Middle Persian kept both grades.\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt l.1190\", \"stance\": \"supports\", \"note\": \"'dānūk [dʼnwk'] knee 33². — SW form of zānūk, q.v.; cf Sogd 49-50.' — Nyberg's cross-reference to exactly the Sogdian pages Gharib cites for jnwwq.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt l.576, ARY pdf p.22 (dībāche p.23)\", \"stance\": \"supports\", \"note\": \"Aryanpur uses this very word as his worked example of reconstruction: '۱- فارسی: زانو > پهلوی … پارسی کهن: *ZANUKA + اوستایی: ZANU/ŠNU > هند و اروپایی: *GENU'; his زانو entry (Latin index l.9199-9207) cites 'POKORNY: 381' and lists Pahlavi 'ZANUG, ZANUK, (U)ŠNUG'.\"},\n            {\"src\": \"POK\", \"where\": \"POK_full.txt l.35420\", \"stance\": \"supports\", \"note\": \"'Pahlavi zanuk, npers. zānū \\\"knee\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"gônia\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Ancient Greek γωνία 'corner, angle; joiner's square' is the lengthened-grade derivative *gonw-íā of γόνυ 'knee' — Pokorny under this same lemma: 'lengthened grade γωνία \\\"point, edge\\\" (*γωνϝια)', and Watkins: 'Suffixed variant form *gon-ya- in Greek gōnia, angle, corner'. Wiktionary adds the historical detail: the long ω is the regular Doric outcome of unattested *γονϝ-ία, because the paradigm of *ǵónu shows no lengthened grade, and the geometers who coined the term were Pythagoreans writing Doric. The semantic step is the natural one 'bend of the leg' → 'bend, angle, corner' — the same shift that gives Proto-Celtic *genwā '(river) bend' (whence the place-names Genava/Geneva, Genua/Genoa).\",\n          \"derivation_fa\": \"واژهٔ یونانی باستان γωνία «گوشه، زاویه، گونیای نجاری» ساختهٔ درجهٔ کشیدهٔ *gonw-íā از γόνυ «زانو» است؛ پوکورنی در همین ماده می‌نویسد: «درجهٔ کشیده γωνία \\\"گوشه، لبه\\\" (*γωνϝια)» و واتکینز نیز «صورت گشتهٔ پسونددارِ *gon-ya- در یونانی gōnia \\\"زاویه، گوشه\\\"». ویکی‌واژه نکتهٔ تاریخی را می‌افزاید: ωی بلند برآیندِ قاعده‌مندِ دوری از *γονϝ-ία است، چون صرفِ *ǵónu درجهٔ کشیده ندارد و ریاضی‌دانانی که این اصطلاح را ساختند فیثاغوریان و دوری‌نویس بودند. تحول معنایی همان گذارِ طبیعیِ «خمِ پا» به «خم، زاویه، گوشه» است؛ همان گذاری که در سلتی *genwā «خمِ رود» (نام‌جای‌های ژنو و جنوا) نیز دیده می‌شود. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%B3%CF%89%CE%BD%CE%AF%CE%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:381\", \"status\": \"supports\", \"note\": \"POK_full.txt l.35432-35434: 'gr. γόνυ, Gen. (Hom.) γουνός (*gonuos) … lengthened grade γωνία \\\"point, edge\\\" (*γωνϝια), zero grade … γνυ-πετεῖν \\\"drop to one's knees\\\"'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.492, s.v. genu-1 §3\", \"stance\": \"supports\", \"note\": \"'3. Suffixed variant form *gon-ya- in Greek gōnia, angle, corner: -GON, GONION; AMBLYGONITE, DIAGONAL, GONIOMETER, GONIOMETRY, ORTHOGONAL.'\"},\n            {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt l.55772, Bd. I 586\", \"stance\": \"supports\", \"note\": \"'dehnstufig (wie jānu, s. o.) γωνία \\\"Ecke\\\" (*γωνϝ-ία)'.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt l.5655\", \"stance\": \"supports\", \"note\": \"Mann glosses the whole root 'bend of the leg, knee; angle', which is precisely the semantic bridge the Greek derivative needs.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"gŭniâ «گونیا»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian گونیا gūniyā 'set-square, try-square' is a loan of Greek γωνία, taken over with narrowing from 'angle' to 'the instrument that gives a right angle'; Wiktionary routes it through Classical Syriac ܓܘܢܝܐ gōnyā, the usual channel for Greek technical vocabulary entering Iran in late antiquity, and notes explicitly that it is a 'Doublet of زانو' — the same PIE etymon reaching Persian twice, once inherited (زانو) and once borrowed via Greek. Dehkhoda, drawing on Borhān-e Qāṭeʿ, Anjoman-ārā and Ghiyās al-Loghāt, says the same in so many words: 'اصل کلمه از یونانی گونیا بمعنی زاویه است. آلت هندسی سه گوش'. It is old in Persian: Khāqāni (12th c.) already has 'یا مسطر و گونیاش بخشم' (Tohfat al-ʿErāqeyn). The same Greek word travelled on into Ottoman/Turkish gönye. Nourai's arrow (Greek → Persian) and his gloss 'set-square, right angle' are both exact.\",\n          \"derivation_fa\": \"«گونیا» وام‌واژه‌ای است از یونانیِ γωνία با تحول معناییِ تخصیص‌یابنده: از «زاویه» به «ابزاری که زاویهٔ قائمه می‌دهد». ویکی‌واژه راه ورود آن را سریانیِ کلاسیک ܓܘܢܝܐ (gōnyā) می‌داند — همان مجرای همیشگیِ اصطلاحات فنی یونانی به ایرانِ اواخر دوران باستان — و به‌روشنی می‌افزاید که «گونیا» دوگانهٔ (doublet) «زانو» است: یک ریشهٔ هندواروپایی که دو بار به فارسی رسیده، یک‌بار میراثی و یک‌بار وام‌گرفته از یونانی. دهخدا نیز به نقل از برهان قاطع و انجمن‌آرا و غیاث‌اللغات همین را می‌گوید: «اصل کلمه از یونانی گونیا بمعنی زاویه است». واژه کهن است؛ خاقانی در تحفةالعراقین آورده: «یا مسطر و گونیاش بخشم». همین واژهٔ یونانی به ترکی هم رفته و gönye شده است. پیکان و معنای نمودار هر دو درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%D9%86%DB%8C%D8%A7\",\n            \"https://abadis.ir/fatofa/%DA%AF%D9%88%D9%86%DB%8C%D8%A7/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Nourai gives no volume/page, so only the headword could be checked. Mo'in's Farhang-e Fārsi entry (reproduced at abadis.ir/fatofa/گونیا/, section فرهنگ معین / فرهنگ فارسی) defines گونیا as '(اسم) ۱- آلتی چوبین یا فلزی بشکل مثلث قائم‌الزاویه … برای ترسیم زاویه و خط عمودی بکار رود', i.e. exactly Nourai's gloss; the Greek origin is stated in the Dehkhoda entry on the same page ('اصل کلمه از یونانی گونیا بمعنی زاویه است').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"abadis.ir s.v. گونیا (فرهنگ معین / لغت‌نامه دهخدا)\", \"stance\": \"supports\", \"note\": \"Dehkhoda, quoting برهان قاطع and انجمن‌آرا: 'گونیا. (اِ) مثلث شکلی قائم‌الزوایه، چوبین یا فلزی که معماران و نجاران بدان قائمه بودن زوایا … را معلوم کنند. اصل کلمه از یونانی گونیا بمعنی زاویه است.' with Khāqāni's verse 'یا مسطر و گونیاش بخشم'.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ s.v. گونیا, cited inside the Dehkhoda entry\", \"stance\": \"supports\", \"note\": \"Borhān is Dehkhoda's source both for the instrument sense and for the second sense 'ریسمانی را گویند که استادان بنا … بکشند'; the Greek etymology in Dehkhoda is credited to برهان قاطع / انجمن آرا / غیاث اللغات.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"diagonal, pentagon, polygon\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are learned formations on Greek γωνία as a second element -γωνος/-γώνιος 'having … angles'. Greek diagōnios 'from angle to angle' (dia- 'through, across') → Latin diagonalis → French/English diagonal (mid-16th c.); Greek pentagōnon 'five-angled figure' → Latin pentagonum → pentagon (1560s); Greek polygōnon 'many-angled figure' → polygon (1570s). They enter English in the Renaissance with the translation of Euclid, not by inheritance. Watkins lists precisely this family under the root: '-GON, GONION; AMBLYGONITE, DIAGONAL, GONIOMETER, GONIOMETRY, ORTHOGONAL', and the -gon of pentagon/polygon is his '-GON'.\",\n          \"derivation_fa\": \"هر سه واژه ساخته‌های عالمانه‌اند بر پایهٔ γωνία یونانی در جایگاه جزء دومِ ترکیب (-γωνος «دارای … زاویه»). یونانی diagōnios «از زاویه‌ای به زاویهٔ دیگر» (با پیشوند dia- «از میانِ») > لاتین diagonalis > انگلیسی diagonal (میانهٔ سدهٔ شانزدهم)؛ یونانی pentagōnon «پنج‌گوشه» > لاتین pentagonum > pentagon؛ یونانی polygōnon «چندگوشه» > polygon. این‌ها در دورهٔ رنسانس و با ترجمهٔ اقلیدس وارد انگلیسی شده‌اند، نه از راه میراث زبانی. واتکینز در پیوست فرهنگ American Heritage همین خانواده را زیر همین ریشه فهرست کرده است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.492: under 'genu-1 … 3. Suffixed variant form *gon-ya- in Greek gōnia, angle, corner: -GON, GONION; AMBLYGONITE, DIAGONAL, GONIOMETER, GONIOMETRY, ORTHOGONAL.' — DIAGONAL is named outright and pentagon/polygon fall under '-GON'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"POK_full.txt l.35433\", \"stance\": \"partial\", \"note\": \"Pokorny has the Greek base γωνία but, as a comparative dictionary of PIE, records no modern English derivatives.\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.492\", \"stance\": \"supports\", \"note\": \"See ref_check; Watkins's word list is Nourai's own cited authority here and covers the chain Greek gōnia → English -gon words.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Germanic\",\n          \"words\": \"kniwam\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *knewą (< PIE *ǵnéw-o-m, the thematised zero grade *gneu-) 'knee': Gothic kniu, Old Norse kné, Old Saxon kneo, Old High German kniu/knio, Old English cnēo(w). Pokorny writes it '*kniwa-, Indo Germanic *gneuo', which is exactly Nourai's 'kniwam' (Pokorny's stem plus the neuter nom.-acc. ending -m); Watkins prints '*knewam'. Phonetically the PIE palatal *ǵ becomes Germanic *k by Grimm's law, and the *w of the oblique stem is generalised. Wiktionary/Kroonen reconstruct *ǵnéw-o-m > Proto-Germanic *knewą.\",\n          \"derivation_fa\": \"ژرمنیِ آغازین *knewą (از *ǵnéw-o-m هندواروپایی، یعنی درجهٔ صفرِ *gneu- با مصوت درون‌مایه‌ای) «زانو»: گوتیک kniu، نورس کهن kné، ساکسون کهن kneo، آلمانی علیای کهن kniu/knio، انگلیسی کهن cnēo(w). پوکورنی آن را «*kniwa-، هندوژرمنی *gneuo» می‌نویسد که همان صورت نورایی است (ستاکِ پوکورنی به‌علاوهٔ پایانهٔ خنثای -m)، و واتکینز *knewam را به‌کار می‌برد. از نظر آوایی، *ǵ کامیِ هندواروپایی بر پایهٔ قانون گریم در ژرمنی به k بدل شده و w ستاکِ غیرفاعلی تعمیم یافته است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.492: 'genu-1 … 1. Variant form *gneu- in: a. Germanic *knewam in Old English cnéo, knee: KNEE; b. Germanic *knewljan in Old English cnéowlian, to kneel: KNEEL.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"POK_full.txt l.35441-35443, p.381\", \"stance\": \"supports\", \"note\": \"'Gothic kniu n., Old High German etc. knio, kneo (*kniwa-, Indo Germanic *gneuo) \\\"knee\\\" (Old Norse kné also from \\\"knot in the straw\\\", as Old English cneoweht \\\"knotty, from plants\\\")'.\"},\n            {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt l.55782-55783, Bd. I 586\", \"stance\": \"supports\", \"note\": \"'lat. genu; got. kniu, ahd. usw. knio, kneo \\\"Knie\\\" (anord. kné auch von Knoten am Strohhalm, wie ags. cneoweht \\\"knotig, von Pflanzen\\\")'.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"knee, kneel\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English cnēo, cnēow 'knee' → Middle English kne → knee; the denominative Old English cnēowlian 'to bend the knee' → Middle English knelen → kneel (the weak past knelt is a late analogical form, 16th c.). The initial cluster kn- was still pronounced in Middle English and lost its /k/ in the 17th century, leaving the spelling fossilised. Etymonline: 'knee (n.), Old English cnēo, cnēow \\\"knee\\\", from Proto-Germanic *knewa- (source also of Old Norse kne, … Gothic kniu), from PIE root *genu- (1) \\\"knee; angle\\\"'. Watkins names both words under the root, so the box needs no reference of its own.\",\n          \"derivation_fa\": \"انگلیسی کهن cnēo/cnēow «زانو» > انگلیسی میانه kne > knee؛ و فعلِ برساخته از آن، cnēowlian «زانو زدن» > انگلیسی میانه knelen > kneel (گذشتهٔ knelt ساختی قیاسی و متأخر است). خوشهٔ آغازینِ kn- تا انگلیسی میانه تلفظ می‌شد و در سدهٔ هفدهم /k/ آن افتاد و تنها در املا ماند. اتیمآنلاین: «knee از انگلیسی کهن cnēo، از ژرمنی آغازین *knewa-، از ریشهٔ هندواروپایی *genu- (۱) \\\"زانو؛ زاویه\\\"». این خانه در کتاب ارجاعی ندارد، ولی واتکینز هر دو واژه را زیر همین ریشه آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/knee\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none in the book)\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the printed chart; the parent Germanic box is referenced to AHD, and Watkins there names both KNEE and KNEEL.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.492\", \"stance\": \"supports\", \"note\": \"'Germanic *knewam in Old English cnéo, knee: KNEE; b. Germanic *knewljan in Old English cnéowlian, to kneel: KNEEL.'\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/knee\", \"stance\": \"supports\", \"note\": \"'knee (n.) … Old English cneo, cneow \\\"knee\\\", from Proto-Germanic *knewa- … from PIE root *genu- (1) \\\"knee; angle.\\\" For pronunciation, see kn-.'\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Genu 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ǵénus f. 'cheek, jaw, chin' (Pokorny '2. ĝenu- and (ĝenədʰ-) ĝonədʰ- : chin', pp.381-382; Watkins 'genu-2. Jawbone, chin')\",\n      \"note\": \"Root, language, gloss and page are all correct: Pokorny's lemma is 'Root / lemma: genu-2 and (ĝenədʰ-) ĝonədʰ- / Meaning: chin', 'Page(s): 381-382', so POK:381 is the first page of the lemma; Watkins has 'genu-2. Jawbone, chin … [Pok. 2. genu- 381.]', and Walde-Pokorny I 587 heads it 'g(h)enu-s \\\"Kinnbacke, Kinn\\\"'. Nourai's decision to keep Genu 1 and Genu 2 as two separate root boxes follows Pokorny's own numbering; Pokorny nevertheless adds a note deriving ĝenu-2 from ĝenu-1, Buck (p.221) calls the connection with 'knee' 'through some common notion like \\\"angle\\\" … probable', and Mann glosses the jaw root outright 'angle of the face'. Modern handbooks (de Vaan, Kroonen, as summarised on Wiktionary) list *ǵénus separately and do not commit to the link — so the two-box treatment is if anything the more cautious one. The only wrinkle in the root box: Indo-Iranian shows an unexplained aspirate (*ȷ́ʰánuš), which is why Sanskrit has h- and not j-; Pokorny calls it 'secondary Aryan gh-'.\",\n      \"note_fa\": \"ریشه، برچسب زبانی، معنا و شمارهٔ صفحه همه درست است: پوکورنی مادهٔ «ĝenu-2 و (ĝenədʰ-) ĝonədʰ-» را با معنای «چانه» در صفحات ۳۸۱–۳۸۲ آورده، پس POK:381 نخستین صفحهٔ همان ماده است؛ واتکینز نیز «genu-2. استخوان آرواره، چانه» و والده-پوکورنی (ج۱ ص۵۸۷) «g(h)enu-s \\\"آرواره، چانه\\\"». جدا نگه‌داشتن Genu 1 و Genu 2 در دو جعبه، پیروی از شماره‌گذاری خود پوکورنی است؛ هرچند پوکورنی در یادداشتی ĝenu-2 را برگرفته از ĝenu-1 می‌داند و باک (ص ۲۲۱) پیوند آن با «زانو» را «از راه مفهوم مشترکی مانند زاویه، محتمل» می‌شمارد و مان معنای ریشه را صریحاً «زاویهٔ چهره» می‌نویسد. پژوهش‌های امروزی (دِ ڤان، کرونن) *ǵénus را جداگانه فهرست می‌کنند و دربارهٔ آن پیوند حکم قطعی نمی‌دهند؛ پس تفکیک نورایی محتاطانه‌تر هم هست. تنها نکتهٔ آوایی: در هندوایرانی دمیدگیِ توضیح‌ناپذیری پدید آمده (*ȷ́ʰánuš) که چرایی h در سنسکریت hanu- را روشن می‌کند؛ پوکورنی آن را «gh ثانویِ آریایی» می‌نامد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%C3%A9nus\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:381\", \"status\": \"supports\", \"note\": \"POK_full.txt l.35468-35520: 'Root / lemma: genu-2 and (ĝenədʰ-:) ĝonədʰ- / Meaning: chin … Material: Old Indic hanu-s f. \\\"mandible\\\", Avestan zanu- ds., in compounds (with secondary Aryan gh-) … References: WP. I 587, WH. I 589 f. … Page(s): 381-382'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt l.55805 ff., Bd. I 587\", \"stance\": \"supports\", \"note\": \"'g(h)enu-s \\\"Kinnbacke, Kinn\\\" (Anlaut europ. ǵ, ai. h …). Ai. hanu-h f. \\\"Kinnbacke\\\"; gr. γένυς f. \\\"Kinn, Kinnbacke\\\" … got. kinnus f. \\\"Wange, Backe\\\" … ahd. usw. kinni \\\"Kinn, Kinnbacke\\\"'.\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.492, s.v. genu-2\", \"stance\": \"supports\", \"note\": \"'genu-2. Jawbone, chin. 1. Form *genw- in Germanic *kinnuz in Old English cin(n), chin: CHIN. 2. Basic form *genu- in Greek genus, chin: GENIAL. 3. Suffixed variant form *gna-dho- in Greek gnathos, jaw … 4. Variant form *g(h)enu- in Sanskrit hanu, jaw: HANUMAN. [Pok. 2. genu- 381.]'\"},\n        {\"src\": \"SYN\", \"where\": \"SYN.txt l.5762 ff., Buck 4.207, p.221\", \"stance\": \"supports\", \"note\": \"'Words for \\\"jaw\\\", \\\"cheek\\\", \\\"chin\\\". Orig. sense \\\"jaw\\\" and ultimate connection with the word for \\\"knee\\\", IE *genu- (neut.) … through some common notion like \\\"angle\\\", is probable. Walde-P. 1.587 … Skt. hanu- \\\"jaw\\\" (h for ǰ secondary), Av. zanu- \\\"jaw\\\" or \\\"chin\\\" (in cpd., Barth. 1689), NPers. zanax \\\"chin\\\"'.\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt l.5656, s.v. ĝenus\", \"stance\": \"supports\", \"note\": \"'ĝenus (ĝenuo, ĝenoueo, geno) \\\"jaw, jowl, angle of the face, angle, wedge\\\". Cf. genu, geun- … Per. zanax \\\"chin\\\"; Tokh. *śanwen; Arm. cnawt \\\"chin, jaw\\\"; Gk. génus …; Lat. genuae, pl. \\\"jaws\\\" … Phryg. a-zén \\\"beard\\\"'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"zânu, zanva\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both citation forms in the box are real. Bartholomae AiW has the stem 'zānav- f. \\\"Kinn\\\"; vgl. ai. hánav- f., np. zanax. — Pü.: zānak drahnāk', attested in the Videvdad compound zānu.drājah- 'consisting in thrusting out the chin' (V. 18.11), and he notes in a footnote that the long ā is unexpected and that some had wrongly translated the compound as 'knee-thrust'. Horn (no. 669) cites the oblique 'aw. zanva- (Geldner, KZ. 30, 514)' — which is precisely Nourai's second form. Pokorny gives 'Avestan zanu- ds. [= chin], in compounds (with secondary Aryan gh-)', and Buck p.221 'Av. zanu- \\\"jaw\\\" or \\\"chin\\\" (in cpd., Barth. 1689)'. Phonetically Av. z- is the regular reflex of the PIE palatal *ǵ; the Indo-Iranian branch adds an unexplained aspiration (*ȷ́ʰánuš), visible in Sanskrit h- but not in Avestan z-. The word is attested only in compounds, which is why Bartholomae's headword carries an asterisk.\",\n          \"derivation_fa\": \"هر دو صورتِ آورده‌شده در این خانه واقعی‌اند. بارتولمه در فرهنگ ایرانی باستان ستاکِ «zānav- مؤنث: چانه» را می‌آورد و آن را با hánav- سنسکریت و «زنخِ» فارسی نو می‌سنجد؛ این واژه در ترکیبِ ویدیودادیِ zānu.drājah- «پیش‌آوردنِ چانه» (وندیداد ۱۸٫۱۱) گواهی شده است، و بارتولمه در پانوشت یادآور می‌شود که ā کشیده در آن شگفت است و برخی به‌خطا آن را «زانو» ترجمه کرده‌اند. هرن (شمارهٔ ۶۶۹) صورت غیرفاعلیِ «zanva- اوستایی (به نقل از گلدنر)» را نقل می‌کند و این دقیقاً صورت دوم نمودار است. پوکورنی «zanu- اوستایی، در ترکیبات، با gh ثانویِ آریایی» و باک (ص ۲۲۱) «zanu- اوستایی \\\"آرواره\\\" یا \\\"چانه\\\" (در ترکیب، بارتولمه ۱۶۸۹)» دارند. از نظر آوایی z اوستایی بازتاب قاعده‌مندِ *ǵ کامی است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:381\", \"status\": \"supports\", \"note\": \"POK_full.txt l.35480-35482: 'Material: Old Indic hanu-s f. \\\"mandible\\\", Avestan zanu- ds., in compounds (with secondary Aryan gh-, Güntert WuS. 11, 124 f.)'.\"},\n            {\"ref\": \"SYN:221\", \"status\": \"supports\", \"note\": \"SYN.txt l.5762 ff. (Buck §4.207, printed p.221): 'Skt. hanu- \\\"jaw\\\" (h for ǰ secondary), Av. zanu- \\\"jaw\\\" or \\\"chin\\\" (in cpd., Barth. 1689), NPers. zanax \\\"chin\\\"'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt l.28083-28084, AiW s.v. zānu.drājah- / *zānav-\", \"stance\": \"supports\", \"note\": \"'j. zānu.drājah- Adj. \\\"im Vorstrecken des Kinns bestehend\\\": … V. 18.11' and '*zānav- f. \\\"Kinn\\\"; vgl. ai. hánav- f., np. zanax. — Pü.: zānak drahnāk. — Das ā ist auffällig … \\\"Knie\\\" wäre zānūi.'\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt l.5908-5910, Grundriss no. 669\", \"stance\": \"supports\", \"note\": \"'669. zenax \\\"Kinn\\\", zenexdān. — ai. hanu- \\\"Kinn\\\"; aw. zanva- (Geldner, KZ. 30, 514); arm. cnaut \\\"Kinnbacke, Wange\\\"' — the source of the chart's second Avestan form.\"},\n            {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt l.55806, Bd. I 587\", \"stance\": \"partial\", \"note\": \"Walde-Pokorny head the entry 'g(h)enu-s \\\"Kinnbacke, Kinn\\\"' and cite 'Ai. hanu-h f. \\\"Kinnbacke\\\"' but, in the lines preserved here, no Avestan form — silent on zānu- specifically.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"zanax «زنخ»; câneh «چانه» (+ زنخدان)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"زنخ zanax 'chin' continues Old Iranian *zanu-ka- (the same -ka- suffix as in *zānu-ka- > zānūg 'knee'), with the suffix consonant appearing as -x; the same formation is spread across the eastern dialects Horn lists at no. 669 — Balochi zanūk, zanīk, zanax, Wakhi zanax, Shughni zingū, Sarikoli zangān, Pashto zana/zanax. زنخدان zanaxdān, the chart's extra form, is zanax + the container suffix -dān (as in نمکدان), lexically 'the chin-socket, the dimple of the chin', and it is that word that carries the Hāfez line quoted in the box ('چاه زنخدان'). Mo'in's footnote on the very page Nourai cites (Borhān p.1036) gives 'هندی باستان hanu- (زنخ)، اوستا zānav-، ارمنی cnaut (فك، گونه)'; Horn no.669 and Buck p.221 ('NPers. zanax') agree. چانه čāne is derived by Wiktionary from Proto-Iranian *jánukah, Proto-Indo-Iranian *ȷ́ʰánuš, PIE *ǵénus, with the cognates Avestan zānu, Sanskrit hánu, Armenian cnot, Latin gena, English chin — the same etymon, so زنخ and چانه are Persian doublets. The initial č- for expected z-/j- is irregular and unexplained (a non-southwestern dialect form is the usual guess); Aryanpur's چانه entry (printed p.218) reaches the same root but opens by admitting 'هیچیک از پسگشت‌های فارسی ذکری از ریشهٔ این واژه نمی‌کنند'. Nourai's arrows are right for both words; only the č- of چانه is a loose joint.\",\n          \"derivation_fa\": \"«زنخ» دنبالهٔ ایرانی باستانِ *zanu-ka- است (همان پسوند -ka- که در *zānu-ka- > zānūg «زانو» هست) با نمود پسوند به‌صورت -x؛ همین ساخت در گویش‌های شرقی که هرن در شمارهٔ ۶۶۹ برمی‌شمارد پراکنده است: بلوچی zanūk/zanīk/zanax، وخی zanax، شغنی zingū، سریکلی zangān، پشتو zana. «زنخدان» — همان صورت افزودهٔ نمودار — از «زنخ» به‌علاوهٔ پسوند ظرف‌سازِ -دان است (مانند نمکدان) و معنای لفظی‌اش «جایگاهِ زنخ» یعنی گودیِ چانه است؛ بیتِ حافظ در همان جعبه («چاه زنخدان») به همین واژه اشاره دارد. معین در حاشیهٔ همان صفحهٔ برهان که نورایی ارجاع داده (ص ۱۰۳۶) می‌نویسد: «هندی باستان hanu- (زنخ)، اوستا zānav-، ارمنی cnaut (فك، گونه)». دربارهٔ «چانه»، ویکی‌واژه آن را از ایرانی آغازین *jánukah، از هندوایرانی *ȷ́ʰánuš، از هندواروپایی *ǵénus می‌گیرد و هم‌ریشه‌های zānu اوستایی، hánu سنسکریت، cnot ارمنی، gena لاتین و chin انگلیسی را برمی‌شمارد؛ یعنی «زنخ» و «چانه» دو صورتِ دوگانه (doublet) از یک ریشه‌اند. تنها گره، آغازهٔ چ به‌جای ز/ج است که توضیح روشنی ندارد و معمولاً آن را صورتی گویشی و ناجنوب‌غربی می‌دانند؛ آریان‌پور نیز در مدخل «چانه» (ص ۲۱۸) پیش از هر چیز اقرار می‌کند که «هیچ‌یک از پسگشت‌های فارسی ذکری از ریشهٔ این واژه نمی‌کنند». در مجموع ادعای نورایی دربارهٔ هر دو واژه پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%86%D8%A7%D9%86%D9%87\",\n            \"https://en.wiktionary.org/wiki/%D8%B2%D9%86%D8%AE\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SYN:221\", \"status\": \"supports\", \"note\": \"SYN.txt l.5762 ff., Buck §4.207 (printed p.221): '… Av. zanu- \\\"jaw\\\" or \\\"chin\\\" (in cpd., Barth. 1689), NPers. zanax \\\"chin\\\"'.\"},\n            {\"ref\": \"BQT:1036\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ p.1036 (BQT_v2_pages.txt chunk 499, offset +537 fixed by زانو=1000 and زفر=1024), Mo'in's footnote: 'هندی باستان hanu- (زنخ)، اوستا zānav-، ارمنی cnaut (فك، گونه)'.\"},\n            {\"ref\": \"HRN:148\", \"status\": \"supports\", \"note\": \"The content is Horn's no. 669: 'zenax \\\"Kinn\\\", zenexdān. — ai. hanu- \\\"Kinn\\\"; aw. zanva-; arm. cnaut' (HRN.txt l.5908-5912), together with the dialect forms bal. zanūk/zanīk/zanax, wax. zanax, šign. zingū, sar. zangān. Note that the entry sits on printed p.149 (the running head '148' falls a few lines earlier, inside nos. 666-667), so Nourai's page number is one off; Horn's own word index (HRN.txt l.20108) gives 'zanax 669.'\"},\n            {\"ref\": \"VIE:12\", \"status\": \"supports\", \"note\": \"Sajjadiyyeh, Vāzhehā-ye Irāni dar Zabān-e Engelisi (VIE_pages.txt l.418, pdf p.18 ≈ printed p.12), in his list of shared Irano-English roots: 'chin انگلیسی، چانه فارسی، چنه ترکی آذری و خراسانی، çene ترکی استانبولی'. It supports the چانه ~ chin equation Nourai draws, though Sajjadiyyeh is a popular work and wrongly files the Turkish çene as a 'Turanian' cognate (it is itself a Persian loan).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"HUB.txt l.7888, Persische Studien\", \"stance\": \"supports\", \"note\": \"Hübschmann files the word among the Persian reflexes of a palatal aspirate: 'zanax \\\"Kinn\\\" (ǵʰ) H. 669'.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt around l.6370-6414, ARY pdf p.216-217 (printed p.218), s.v. چانه\", \"stance\": \"supports\", \"note\": \"Aryanpur's چانه entry lists Avestan ZĀNU/ZANAV, Sanskrit HANU, Latin GENA/GENUS, Gothic KINNUS, Old English CIN etc. and notes '۲- این واجریشه در برخی از زبان‌های هند و اروپایی دارای چم‌های دیگری نیز بوده است: آرواره، گونه، دهان', with the caveat '۱- هیچیک از پسگشت‌های فارسی ذکری از ریشهٔ این واژه نمی‌کنند'. His index (l.9630) also carries 'زنخ، زنخدان (به چم چانه) | ۳۲۷'.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt l.5656\", \"stance\": \"supports\", \"note\": \"Mann lists 'Per. zanax \\\"chin\\\"' as the Persian member of ĝenus.\"},\n            {\"src\": \"BRT\", \"where\": \"BRT.txt l.28084\", \"stance\": \"supports\", \"note\": \"Bartholomae connects the Avestan word to the Persian one directly: '*zānav- f. \\\"Kinn\\\"; vgl. ai. hánav- f., np. zanax'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"hanu\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit hánu- f. 'jaw, jawbone' (Rigveda onwards) is the Indic member of *ǵénus. The h- where *j- is expected is the well-known Indo-Iranian aspiration of this word: Pokorny calls it 'secondary Aryan gh-' (following Güntert), Buck notes 'Skt. hanu- \\\"jaw\\\" (h for ǰ secondary)', and Wiktionary reconstructs Proto-Indo-Iranian *ȷ́ʰánuš 'with unexplained aspiration of *ĵ'. The Avestan cognate zanu-/zānav- shows the unaspirated outcome, which is why the two branches diverge in the initial. Watkins lists it as 'Variant form *g(h)enu- in Sanskrit hanu, jaw: HANUMAN' — the monkey-god's name being 'the one with (prominent) jaws'.\",\n          \"derivation_fa\": \"سنسکریت hánu- (مؤنث) «آرواره، استخوان آرواره» (از ریگ‌ودا به بعد) عضو هندیِ ریشهٔ *ǵénus است. h در جایی که *j انتظار می‌رود، همان دمیدگیِ شناخته‌شدهٔ هندوایرانی در این واژه است: پوکورنی آن را «gh ثانویِ آریایی» می‌نامد، باک می‌نویسد «hanu سنسکریت \\\"آرواره\\\" (h به‌جای ǰ، ثانوی)» و ویکی‌واژه هندوایرانیِ آغازین را *ȷ́ʰánuš «با دمیدگیِ توضیح‌ناپذیرِ *ĵ» بازسازی می‌کند. هم‌ریشهٔ اوستایی zanu-/zānav- برآیندِ نادمیده را نشان می‌دهد و از همین‌روست که آغازهٔ دو شاخه از هم جدا می‌شود. واتکینز آن را چنین می‌آورد: «صورت گشتهٔ *g(h)enu- در سنسکریت hanu \\\"آرواره\\\": HANUMAN». ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:381\", \"status\": \"supports\", \"note\": \"POK_full.txt l.35480: 'Old Indic hanu-s f. \\\"mandible\\\", Avestan zanu- ds., in compounds (with secondary Aryan gh-, Güntert WuS. 11, 124 f.)'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt l.55805-55807, Bd. I 587\", \"stance\": \"supports\", \"note\": \"'g(h)enu-s \\\"Kinnbacke, Kinn\\\" (Anlaut europ. ǵ, ai. h …). Ai. hanu-h f. \\\"Kinnbacke\\\"'.\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.492, s.v. genu-2 §4\", \"stance\": \"supports\", \"note\": \"'4. Variant form *g(h)enu- in Sanskrit hanu, jaw: HANUMAN.'\"},\n            {\"src\": \"SYN\", \"where\": \"SYN.txt l.5762, Buck 4.207 p.221\", \"stance\": \"supports\", \"note\": \"'Skt. hanu- \\\"jaw\\\" (h for ǰ secondary)'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Germanic\",\n          \"words\": \"kinnuz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *kinnuz f. 'cheek, chin' < PIE *ǵénus, with *ǵ > k by Grimm's law. Pokorny: 'Gothic kinnus f. \\\"cheek\\\" (*ĝenus, *ĝenues, -nn- from -nu-), Old Norse kinn f. \\\"cheek, mountainside\\\", Old English cinn, Old High German kinni \\\"chin\\\"'; Watkins: 'Form *genw- in Germanic *kinnuz in Old English cin(n), chin'. The geminate -nn- is the crux: Pokorny and Walde-Pokorny derive it from the oblique *-nu- (i.e. *ǵenw- with the glide assimilating), while Kroonen (via Wiktionary) leaves it 'of uncertain origin; perhaps < *ǵenw-ú-s'. The Germanic branch also shows the widespread 'jaw ~ cheek ~ chin' drift Buck describes: Gothic/Norse kinnus is 'cheek', West Germanic cinn/kinni is 'chin'.\",\n          \"derivation_fa\": \"ژرمنیِ آغازین *kinnuz (مؤنث) «گونه، چانه» از هندواروپاییِ *ǵénus است، با تبدیل *ǵ به k بر پایهٔ قانون گریم. پوکورنی: «گوتیک kinnus مؤنث \\\"گونه\\\" (*ĝenus، *ĝenues، با nn از nu)، نورس کهن kinn، انگلیسی کهن cinn، آلمانی علیای کهن kinni \\\"چانه\\\"»؛ واتکینز: «صورت *genw- در ژرمنیِ *kinnuz در انگلیسی کهن cin(n)، چانه». گرهِ کار دوگانه‌شدنِ nn است: پوکورنی و والده-پوکورنی آن را از ستاکِ غیرفاعلیِ -nu- می‌گیرند (همگونیِ w)، ولی کرونن آن را «نامعلوم، شاید از *ǵenw-ú-s» می‌داند. در همین شاخه، همان لغزشِ معناییِ «آرواره ~ گونه ~ چانه» که باک وصف می‌کند دیده می‌شود: در گوتیک و نورس «گونه» و در ژرمنی باختری «چانه». ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.492: 'genu-2. Jawbone, chin. 1. Form *genw- in Germanic *kinnuz in Old English cin(n), chin: CHIN.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"POK_full.txt l.35505-35508, p.382\", \"stance\": \"supports\", \"note\": \"'Gothic kinnus f. \\\"cheek\\\" (*ĝenus, *ĝenues, -nn- from -nu-), Old Norse kinn f. \\\"cheek, mountainside\\\", Old English cinn, Old High German kinni n. \\\"chin\\\"'.\"},\n            {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt l.55818-55820, Bd. I 587\", \"stance\": \"supports\", \"note\": \"'got. kinnus f. \\\"Wange, Backe\\\" (für *kinus nach den Kasus mit nn aus nu), anord. kinn, pl. kinnr f. ds., ahd. usw. kinni \\\"Kinn, Kinnbacke\\\"'.\"},\n            {\"src\": \"SYN\", \"where\": \"SYN.txt l.5860, Buck 4.209\", \"stance\": \"supports\", \"note\": \"'OE cin, OHG kinni, etc., general WGmc. for \\\"chin\\\" = Goth. kinnus, ON kinn, etc. \\\"cheek\\\": Grk. γένυς \\\"jaw, cheek\\\", etc. (4.207).'\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"chin\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English cinn 'chin' → Middle English chin(ne) → chin. The ch- is regular: West Germanic /k/ was palatalised to /tʃ/ before a front vowel in Old English (the same change that gives cheese, church, cheek), so the Germanic *kinnuz of the parent box surfaces with an affricate in English while German keeps Kinn. Semantically English kept the West Germanic 'chin' value rather than the Gothic/Norse 'cheek'. The box has no reference of its own, but Watkins names CHIN under genu-2, and Buck 4.209 has 'OE cin, OHG kinni, etc., general WGmc. for \\\"chin\\\"'.\",\n          \"derivation_fa\": \"انگلیسی کهن cinn «چانه» > انگلیسی میانه chin(ne) > chin. آوای ch قاعده‌مند است: در انگلیسی کهن /k/ ژرمنیِ باختری پیش از واکه‌های پیشین به /tʃ/ کامی شده است (همان دگرگونی‌ای که cheese و church و cheek را ساخته)؛ از این‌رو *kinnuz ژرمنی در انگلیسی با آوای چ ظاهر می‌شود، حال آنکه آلمانی Kinn را نگاه داشته است. از نظر معنایی انگلیسی معنای «چانه»ی ژرمنیِ باختری را نگاه داشته، نه معنای «گونه»ی گوتیک و نورس. این خانه در کتاب ارجاعی ندارد، ولی واتکینز CHIN را زیر genu-2 آورده و باک (بند ۴٫۲۰۹) می‌نویسد «cin انگلیسی کهن، kinni آلمانی علیای کهن … در سراسر ژرمنی باختری به معنای چانه». ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"(none in the book)\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the printed chart; the parent Germanic box is referenced to AHD, where CHIN is the English word listed under genu-2.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.492\", \"stance\": \"supports\", \"note\": \"'Form *genw- in Germanic *kinnuz in Old English cin(n), chin: CHIN.'\"},\n            {\"src\": \"SYN\", \"where\": \"SYN.txt l.5860, Buck 4.209 (p.222)\", \"stance\": \"supports\", \"note\": \"'OE cin, OHG kinni, etc., general WGmc. for \\\"chin\\\" = Goth. kinnus, ON kinn, etc. \\\"cheek\\\": Grk. γένυς \\\"jaw, cheek\\\"'.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Geph, Gebh\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ǵep(ʰ)-, *ǵebʰ- 'jaw, mouth' (Pokorny 'ĝep(h)-, ĝebh-', p.382; Watkins 'gep(h)-. Also gebh-. Jaw, mouth')\",\n      \"note\": \"This root box is exact on every count. Pokorny's lemma is 'Root / lemma: ĝep(h)-, ĝebh- / Meaning: jaw, mouth', 'Page(s): 382' — so the two variants Nourai prints, the gloss and the page are all Pokorny's own; Watkins repeats it verbatim, 'gep(h)-. Also gebh-. Jaw, mouth … [Pok. geph-, gebh- 382]', and Walde-Pokorny I 570 heads it 'gep(h)-, gebh- \\\"Kiefer, Mund; essen, fressen\\\"'. Pokorny's own note derives this root in turn from ĝenu-2 'chin', so the three charts on this page are, in his framework, one family. One caveat a modern reader should have: a PIE root with a plain voiced *b/*p alternating with an aspirate *bʰ is exactly the kind of reconstruction the glottalic-theory literature distrusts, and Wiktionary now writes simply *ǵep- 'mouth, to chew'; the material (Avestan zafar-/zafan-, Old Irish gop, Germanic *kefalaz/*kabraz, Baltic-Slavic zebti/zobati) is not in doubt, only the shape of the reconstructed root.\",\n      \"note_fa\": \"این جعبهٔ ریشه از هر نظر دقیق است. پوکورنی مادهٔ «ĝep(h)-، ĝebh-» را با معنای «آرواره، دهان» در صفحهٔ ۳۸۲ آورده، پس هر دو گونهٔ نوشته‌شده در نمودار و معنا و شمارهٔ صفحه از خودِ پوکورنی است؛ واتکینز عیناً همان را تکرار می‌کند و والده-پوکورنی (ج۱ ص۵۷۰) سرمدخل را «gep(h)-، gebh- \\\"آرواره، دهان؛ خوردن، جویدن\\\"» می‌نویسد. پوکورنی در یادداشتی خودِ این ریشه را برگرفته از ĝenu-2 «چانه» می‌داند؛ بدین‌سان سه نمودار این صفحه در چارچوب او یک خانواده‌اند. یک احتیاط برای خوانندهٔ امروزی: ریشه‌ای که در آن *b/*p ساده با *bʰ دمیده جانشین یکدیگر می‌شوند، همان‌گونه بازسازی‌ای است که نظریهٔ چاکنایی به آن بدگمان است، و ویکی‌واژه امروز تنها *ǵep- «دهان، جویدن» می‌نویسد؛ خودِ داده‌ها (zafar-/zafan- اوستایی، gop ایرلندی کهن، *kefalaz/*kabraz ژرمنی، zebti/zobati بالتی-اسلاوی) بی‌گمان‌اند و تنها شکلِ ریشهٔ بازسازی‌شده محل بحث است.\",\n      \"sources\": [],\n      \"ref_check\": [\n        {\"ref\": \"POK:382\", \"status\": \"supports\", \"note\": \"POK_full.txt l.35525-35566: 'Root / lemma: ĝep(h)-, ĝebh- / Meaning: jaw, mouth … Material: With ptr. Avestan zafar-, zafan- \\\"mouth, jaw\\\", participle Med. vī-zafana- … References: WP. I 570 f., Trautmann 364, Benveniste Origines 10 f., Kluge s.v. \\\"beetle, chafer\\\" and \\\"jaw\\\". Page(s): 382'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt l.54251-54295, Bd. I 570-571\", \"stance\": \"supports\", \"note\": \"'gep(h)-, gebh- \\\"Kiefer, Mund; essen, fressen\\\". ph: av. zafarə, zafan- \\\"Mund, Rachen\\\" (: ags. ceafl nach Kluge KZ. 26, 89) … bh: lit. žebiu, žebeti \\\"langsam … essen\\\", aksl. zobati \\\"essen\\\" … air. gop, nir. gob \\\"Schnabel, Mund\\\"'.\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.492, s.v. gep(h)-\", \"stance\": \"supports\", \"note\": \"'gep(h)-. Also gebh-. Jaw, mouth. 1. Probably Germanic *kaf-, to gnaw, chew, in Old English ceaf, husks, chaff: CHAFF. 2. Germanic *kabraz, \\\"gnawer\\\", in Old English ceafor, ceafer, beetle: CHAFER. 3. Germanic *kēfalaz in Old English céafl, jaw, cheek: JOWL. [Pok. geph-, gebh- 382.]'\"},\n        {\"src\": \"SYN\", \"where\": \"SYN.txt l.5792 and l.5946, Buck 4.207 (p.221) and 4.24\", \"stance\": \"supports\", \"note\": \"'ON kjǫptr …, OE ceafl, ME chavel, NE jowl (in part), MHG kiver, kivel, NHG kiefer, LG keve : Av. zafar- \\\"mouth\\\" (of evil beings). Walde-P. 1.570 f.' and, in the MOUTH section, 'Av. zafar- \\\"mouth\\\" (of evil beings) : OE ceafl, NHG kiefer \\\"jaw\\\". Walde-P. 1.570 f. Barth. 1657.'\"},\n        {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.20399, p.833 s.v. jowl\", \"stance\": \"supports\", \"note\": \"Klein makes the same Avestan-to-Germanic connection the root box asserts: 'jowl, n., jaw … fr. OE. ceafl, \\\"jaw\\\" … cogn. with OIr. gop, Ir. gob, \\\"beak, mouth\\\", Avestic zafar-, \\\"mouth, gullet\\\"'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"zaf-; zaf-an; zaf-ar\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan has a classic heteroclitic r/n-stem here: nominative-accusative zafar- beside the oblique/derivational stem zafan-, exactly the ancient type of Greek ὕδωρ / ὕδατος or Avestan asan-/ašar-. Bartholomae AiW 1657-58: 'zafar- n. \\\"Mund (, Maul)\\\", uzw. daēvischer Wesen' (Yt.11.2, Yt.11.6, Yt.19.50, N.62) with 'Vgl. zafan-; zafah- und hazafāna-. — np., mp. (Pü.) zafar; vgl. nhd. Kiefer, ai. jámbha- m. \\\"Gebiss, Rachen\\\"', and separately 'zafan- n. sva. zafar-. Kompp. — np. dahan'. The two stems show up side by side in the compounds θri-zafan-/θri-zafah- 'three-jawed' (of Aži Dahāka) and vī-zafana- 'tearing the jaws open'. Nourai's bare 'zaf-' is the shared stem abstracted from these, not an independently attested word — a normal way to write the root in a chart. Semantically the word is marked: in Avestan it is used of the mouths of daēvic beings, and Pahlavi keeps the same colouring (MacKenzie 'zafar … mouth, maw (daevic)'). Nourai's cited authorities all say this: Pokorny 'With ptr. Avestan zafar-, zafan- \\\"mouth, jaw\\\"', Klein p.833 'Avestic zafar-, \\\"mouth, gullet\\\"', Buck p.221.\",\n          \"derivation_fa\": \"در اوستایی این واژه نمونهٔ کلاسیکِ ستاکِ ناهمگونِ r/n است: صورت فاعلی-رایی zafar- در کنار ستاکِ غیرفاعلی و اشتقاقیِ zafan-، درست مانند ὕδωρ/ὕδατος یونانی. بارتولمه (فرهنگ ایرانی باستان، ستون ۱۶۵۷–۱۶۵۸) می‌نویسد: «zafar- خنثی \\\"دهان (، پوزه)\\\"، ویژهٔ موجودات دیوی» و می‌افزاید «سنجیده شود با zafan-، zafah- و hazafāna-. — فارسی نو و فارسی میانه (پهلوی) zafar؛ نیز آلمانی Kiefer، سنسکریت jámbha- \\\"دندان، حلق\\\"»؛ و در مدخل جداگانه: «zafan- خنثی، هم‌ارزِ zafar-. در ترکیبات. — فارسی نو dahan». هر دو ستاک در ترکیب‌های θri-zafan-/θri-zafah- «سه‌پوزه» (صفت اژی‌دهاک) و vī-zafana- «باز کنندهٔ پوزه» کنار هم دیده می‌شوند. صورت تنهای «zaf-» در نمودار، ستاکِ مشترکِ برگرفته از این‌هاست نه واژه‌ای گواهی‌شده، و این شیوهٔ متعارفِ نوشتن ریشه در نمودار است. از نظر معنایی واژه نشان‌دار است: در اوستا برای دهانِ موجودات دیوی به‌کار می‌رود و پهلوی هم همان رنگ را نگاه داشته (مکنزی: «zafar … دهان، پوزه (دیوی)»). ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:382\", \"status\": \"supports\", \"note\": \"POK_full.txt l.35533-35535: 'Material: With ptr. Avestan zafar-, zafan- \\\"mouth, jaw\\\", participle Med. vī-zafana-, compare s-stem (besides r/n-stem) in θrizafah- besides θrizafan-'.\"},\n            {\"ref\": \"KLN:833\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.20399, printed p.833 (page markers 832 at l.20363, 833 at l.20382): 'jowl, n., jaw. — ME. chawl, chavel, cholle, fr. OE. ceafl, \\\"jaw\\\" … and cogn. with OIr. gop, Ir. gob, \\\"beak, mouth\\\", Avestic zafar-, \\\"mouth, gullet\\\".'\"},\n            {\"ref\": \"SYN:221\", \"status\": \"supports\", \"note\": \"SYN.txt l.5792, Buck §4.207 (printed p.221): 'ON kjǫptr …, OE ceafl, ME chavel, NE jowl (in part), MHG kiver, kivel, NHG kiefer, LG keve : Av. zafar- \\\"mouth\\\" (of evil beings). Walde-P. 1.570 f. … NED s.v. jowl, sb.1.'\"},\n            {\"ref\": \"DZA:58\", \"status\": \"not_checked\", \"note\": \"Rashed-Mohassel, Darāmadi bar Dastur-e Zabān-e Avestāyi (Khājeh 1364) is not digitised — refs_online.json records 'the 1364 Khajeh edition is not digitised; a revised edition is sold as an ebook on Taaghche'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt l.27617-27619, AiW cols. 1657-1658\", \"stance\": \"supports\", \"note\": \"'j. zafan- n. sva. zafar-. Kompp. — np. dahan.' and 'j. zafar- n. \\\"Mund (, Maul)\\\", uzw. daēvischer Wesen … Vgl. zafan-; zafah- und hazafāna-. — np., mp. (Pü.) zafar; vgl. nhd. Kiefer, ai. jámbha- m. \\\"Gebiss, Rachen\\\"'; also l.14676 'θri-zafan-, -zafah- Adj. \\\"mit drei Mäulern, Rachen\\\"' and l.24563 'vī-zafana- Adj. \\\"den Rachen aufreissend\\\"'.\"},\n            {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt l.54252, Bd. I 570\", \"stance\": \"supports\", \"note\": \"'ph: av. zafarə, zafan- \\\"Mund, Rachen\\\" (: ags. ceafl nach Kluge KZ. 26, 89)'.\"},\n            {\"src\": \"PHD\", \"where\": \"PHD.txt l.673 and l.2751/2862\", \"stance\": \"supports\", \"note\": \"MacKenzie continues the Avestan word into Middle Persian unchanged: 'zafar [zpl | N ~] mouth, maw (daevic)', English index 'maw zafar', 'mouth dahān; (daevic) zafar'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"dahân «دهان»; zafar «زفر»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"زفر zafar is straightforward and confirmed: Horn no. 663 'zefer, zefr \\\"Mund\\\" (Šāhnāme I, 195, 1189). — aw. zafar- \\\"Rachen\\\"; phlv. zafar. Muss dialektisch sein, da die reguläre Form np. dehan (No. 589) ist'; Bartholomae ends his zafar- entry 'np., mp. (Pü.) zafar', MacKenzie has MP zafar 'mouth, maw (daevic)', and Mo'in's footnote on exactly the Borhān page Nourai cites (p.1024) reads 'اوستا zafar- (گلو)، پهلوی zafar … هوبشمان'. Hübschmann calls it a 'Parsenwort' — i.e. زفر is not the regular Southwest Persian development but a form carried over from the Avestan/Zoroastrian tradition, which is precisely why it keeps the daēvic colouring in the Ferdowsi line quoted in the box (a dragon's gaping maw). دهان dahān is the contested half. The classical derivation, which is Nourai's, is Bartholomae's own ('zafan- … np. dahan') and is spelled out phonetically by Nyberg, Manual II: 'dahān [PWMH] mouth … < *dafān, the SW form of Av. zafan-, zafar-, v. zafar; MPrs dhyn; Paz. dahan; NP dahān'. The mechanism is regular: PIE palatal *ǵ gives Avestan z but Old Persian / Southwest Iranian d (cf. Av. zasta- : OP dasta- 'hand'), so *ǵebʰ-en- → Av. zafan- but SW *dafan-; intervocalic -f- then weakens to -h- (as Av. kaofa- → NP kōh), giving MP dahān (written with the Aramaic ideogram PWM(E)) → NP dahān/dahan. Horn no. 589 and Hübschmann (Pers. Stud. §§80c, 110, 163c) both state it. Against this, the newest Iranian etymological dictionary, Rastorgueva–Edelman ESIJa III 50 s.v. *faź-, *fāź-, *fauź-, analyses MP dahān instead as *dam-fāzek, i.e. دم 'breath' + a Proto-Iranian *faź 'mouth, muzzle' of unclear, perhaps sound-symbolic origin; Wiktionary follows ESIJa and cites, as the competing theory, this very page of Nourai's book. So the root is not in dispute for زفر, but the descent of دهان from Av. zafan- is now only one of two accounts — hence 'plausible' for the node as a whole.\",\n          \"derivation_fa\": \"«زفر» بی‌گفت‌وگو درست است: هرن (شمارهٔ ۶۶۳) می‌نویسد «zefer، zefr \\\"دهان\\\" (شاهنامه، ج۱ ص۱۹۵ و ۱۱۸۹). — اوستایی zafar- \\\"حلق، پوزه\\\"؛ پهلوی zafar. ناگزیر گویشی است، زیرا صورت قاعده‌مندِ فارسی نو dehān است (شمارهٔ ۵۸۹)»؛ بارتولمه نیز مدخل zafar- را با «فارسی نو و پهلوی zafar» به پایان می‌برد، مکنزی zafar پهلوی «دهان، پوزهٔ دیوی» را ثبت کرده، و معین در حاشیهٔ همان صفحهٔ برهان که نورایی ارجاع داده (ص ۱۰۲۴) می‌آورد: «اوستا zafar- (گلو)، پهلوی zafar … هوبشمان». هوبشمان آن را «واژهٔ موبدی» (Parsenwort) می‌خواند، یعنی صورتی برآمده از سنت اوستایی نه تحول قاعده‌مندِ جنوب‌غربی؛ و همین توضیح می‌دهد که چرا در بیتِ فردوسیِ همان جعبه، «زفر» برای پوزهٔ اژدها به کار رفته است. اما «دهان» نیمهٔ محلِ اختلاف است. ریشه‌شناسیِ کلاسیک، که همان ریشه‌شناسیِ نورایی است، از آنِ خودِ بارتولمه است («zafan- … فارسی نو dahan») و نیبرگ آن را آوایی می‌شکافد: «dahān … از *dafān، صورت جنوب‌غربیِ zafan-/zafar- اوستایی». سازوکارش قاعده‌مند است: *ǵ کامیِ هندواروپایی در اوستایی z ولی در پارسی باستان و ایرانیِ جنوب‌غربی d می‌دهد (سنجیده شود zasta- اوستایی با dasta- پارسی باستان)، پس *dafan- جنوب‌غربی در برابر zafan- اوستایی؛ سپس f میان دو واکه به h نرم می‌شود (چنانکه kaofa- اوستایی > کوهِ فارسی) و dahān پهلوی و سپس فارسی نو پدید می‌آید. هرن (شمارهٔ ۵۸۹) و هوبشمان نیز همین را می‌گویند. در برابر، تازه‌ترین فرهنگ ریشه‌شناختیِ زبان‌های ایرانی (راستارگویوا–ادلمان، ج۳ ص۵۰، ذیل *faź-) dahān را ترکیبِ *dam-fāzek می‌داند، یعنی «دم» + *faź ایرانیِ آغازین «دهان، پوزه» با خاستگاهِ نامعلوم و شاید آواتصویری؛ ویکی‌واژه همان را می‌پذیرد و نظر رقیب را به همین صفحهٔ کتاب نورایی ارجاع می‌دهد. پس ریشه دربارهٔ «زفر» بی‌گمان است ولی دربارهٔ «دهان» تنها یکی از دو روایت است — و از این‌رو حکمِ این خانه «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AF%D9%87%D8%A7%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1024\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ p.1024 s.v. زفر (BQT_v2_pages.txt chunk 487; the offset +537 is fixed by زانو=1000 and زنخ=1036, and زفر falls alphabetically between them), Mo'in's footnote: '۱- اوستا zafar- (گلو). پهلوی zafar … هوبشمان'.\"},\n            {\"ref\": \"HRN:589\", \"status\": \"supports\", \"note\": \"HRN.txt l.5279-5282, Grundriss no. 589: 'dehān, dehen \\\"Mund\\\", dehūn \\\"Gedächtniss, Stegreif\\\", dehane, dehne \\\"Zaum, Gebiss\\\". — aw. zafan-, zafar- \\\"Rachen\\\"; phlv. dahān. — kurd. LW. dāw, dan; bel. LW. dap, n. daf'.\"},\n            {\"ref\": \"HRN:663\", \"status\": \"supports\", \"note\": \"HRN.txt l.5878-5881, Grundriss no. 663: 'zefer, zefr \\\"Mund\\\" (Šāhn. I, 195, 1189). — aw. zafar- \\\"Rachen\\\"; phlv. zafar. — Muss dialektisch sein, da die reguläre Form np. dehan (No. 589) ist.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt l.1159 and l.4475, Manual of Pahlavi II\", \"stance\": \"supports\", \"note\": \"'dahān [PWMH] mouth 12¹⁷. 50⁹. 101¹¹. 104²². — < *dafān, the SW form of Av. (1657) zafan-, zafar-, v. zafar; MPrs dhyn; Paz. dahan; NP dahān' and 'zafar [zpl] mouth, of Ahrimanic beings 40¹². 48⁶. — Av. (1657) zafar-; cf dahān'. Nyberg's index (l.5471-5472) prints 'zafan-, zafar-: dahān' and 'zafar-: zafar'.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt l.6515-6516, l.7885-7886, l.6502, Persische Studien\", \"stance\": \"supports\", \"note\": \"'zafar \\\"Rachen\\\" (Parsenwort? neben echt pers. dahan = zd. zafan-) = zd. zafar- von iran. zaf-' and 'zafar \\\"Rachen\\\" (das aber nicht urspr. persisch ist, vgl. dahan = zd. zafan § 80, c und 110 sowie § 163, c)'; the f > h step is his 'kaofa- \\\"Hügel\\\" … dahān \\\"Mund\\\", paz. dahan'.\"},\n            {\"src\": \"PHD\", \"where\": \"PHD.txt l.306 and l.673\", \"stance\": \"supports\", \"note\": \"'dahān [PWME < A p(w)m-h | M dhyn, N dahan] mouth' and 'zafar [zpl | N ~] mouth, maw (daevic)' — both Middle Persian ancestors are on the books.\"},\n            {\"src\": \"BRT\", \"where\": \"BRT.txt l.27617\", \"stance\": \"supports\", \"note\": \"Bartholomae himself makes Nourai's arrow: 'j. zafan- n. sva. zafar-. Kompp. — np. dahan.'\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/دهان, Persian section\", \"stance\": \"contradicts\", \"note\": \"'From Middle Persian (PWME /dahān/, \\\"mouth\\\"), apparently from an earlier formation *dam-fāzek, composed of دم (dam, \\\"breath\\\") + a Proto-Iranian *faź (\\\"mouth, muzzle\\\") of unclear origin, perhaps sound-symbolic. [ref: Rastorgujeva/Edelʹman, ESIJa III (2007) p.50 s.v. *faź-, *fāź-, *fauź-] Another theory takes the entire formation as a derivative of a Proto-Indo-European *ǵep- \\\"mouth, to chew\\\", whence English jowl. [ref: Nourai, An Etymological Dictionary …, page 142]' — i.e. Wiktionary's 'another theory' is this very chart.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Germanic\",\n          \"words\": \"kabal; kaf\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The second form is exactly right: Watkins reconstructs 'Probably Germanic *kaf-, to gnaw, chew, in Old English ceaf, husks, chaff: CHAFF', the verbal base behind Middle High German kiven/kiffen 'to gnaw', Dutch keveren, and behind the 'chaff' word. The first form is where the box has drifted. The Germanic 'jaw' word is Old English ceafl, Old Saxon cafl, Middle High German kivel/kiver, German Kiefer, Old Norse kjaptr, and the current reconstructions of it are *kēfalaz (Watkins 1985; etymonline *kefalaz) or, in Walde-Pokorny's terms, a lengthened-grade *kēf-al- beside *kebuta-/*kefuta- (ON kjaptr); a plain 'kabal' with short a is not what any of these print, though it is close to Pokorny's ablauting *kabra-/*kabru- for the beetle-word. So the box conflates two Germanic stems: *kēfalaz gives 'jaw' (→ jowl) and *kabraz 'gnawer' gives 'beetle' (→ chafer). The claims of the box are all recoverable from the sources; only the label 'kabal' is not a form current in the handbooks, and the chart's single 'jaw' stem is doing the work of two.\",\n          \"derivation_fa\": \"صورت دوم دقیقاً درست است: واتکینز *kaf- ژرمنی «جویدن، خاییدن» را بازسازی می‌کند که در انگلیسی کهن ceaf «پوستِ غله» و در آلمانی علیای میانه kiven/kiffen «جویدن» و در هلندی keveren دیده می‌شود. اما صورت نخست جابه‌جا شده است. واژهٔ «آرواره»ی ژرمنی همان ceafl انگلیسی کهن، cafl ساکسون کهن، kivel/kiver آلمانی علیای میانه، Kiefer آلمانی و kjaptr نورس کهن است و بازسازی امروزی‌اش *kēfalaz (واتکینز ۱۹۸۵؛ اتیمآنلاین *kefalaz) یا به بیان والده-پوکورنی درجهٔ کشیدهٔ *kēf-al- در کنار *kebuta-/*kefuta- است؛ «kabal» با a کوتاه در هیچ‌یک از این فرهنگ‌ها نیامده، هرچند به *kabra-/*kabru*ی پوکورنی برای واژهٔ «سوسک» نزدیک است. بنابراین این جعبه دو ستاکِ ژرمنی را در هم آمیخته: *kēfalaz «آرواره» را می‌دهد (> jowl) و *kabraz «جونده» «سوسک» را (> chafer). محتوای ادعا از منابع بازیافتنی است و تنها برچسبِ kabal صورتی رایج در فرهنگ‌های امروزی نیست و یک ستاک، بارِ دو ستاک را بر دوش کشیده است؛ پس این خانه «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt l.492 has Nourai's 'kaf' verbatim — 'Probably Germanic *kaf-, to gnaw, chew, in Old English ceaf, husks, chaff: CHAFF' — but the jaw-word is reconstructed there as '*kēfalaz in Old English céafl, jaw, cheek: JOWL', not 'kabal'; and the beetle-word has its own stem, '*kabraz, \\\"gnawer\\\", in Old English ceafor, ceafer, beetle: CHAFER'. Nourai's 1975 New College appendix may have printed a shorter *kab-l- shape, but the 1985 Watkins does not.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt l.54285-54295, Bd. I 571\", \"stance\": \"supports\", \"note\": \"'germ. mit ph oder teilweisem bh anord. kjaptr oder kjǫptr (*kebut- oder *kefut-) \\\"Maul, Kinnbacke, Kiefer\\\", mhd. kivel, kiver \\\"Kiefer\\\" … dehnstufig as. cafl, ags. ceafl (engl. jowl, jole) \\\"Kiefer\\\"' — the jaw-word is a lengthened-grade *kēf-, not *kab-.\"},\n            {\"src\": \"POK\", \"where\": \"POK_full.txt l.35545-35555, p.382\", \"stance\": \"supports\", \"note\": \"'Germanic … Old Norse kjaptr or kjǫptr (*kebuta- or *kefuta-) \\\"muzzle, mandible, jaw\\\" … lengthened grade Old Norse kafl, Old Saxon cafl, Old English ceafl (engl. jowl, jole) \\\"jaw\\\" (*kefala-). In addition as \\\"nibbler\\\": Old High German chevaro, kevar, Middle High German kevere \\\"beetle, chafer\\\" (*kebran-); changing through ablaut Old English ceafor (*kabra- or *kabru-)'.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.7112 (p.264/265) and l.20399 (p.833)\", \"stance\": \"supports\", \"note\": \"Klein keeps the two Germanic stems apart in the same way: 'chafer, n., a beetle. — ME., fr. OE. ceafor, rel. to OS. kevera, Du. kever, OHG. chevar … lit. \\\"gnawer\\\". Cp. MHG. kiven, Du. keveren, \\\"to gnaw\\\", OE. ceafl … and see jowl, \\\"jaw\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"jowl; chafer\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both English words are genuine members of this root, but by two different Germanic stems. jowl 'jaw': late Old English ceafl 'jaw, cheek, jawbone' → Middle English chafle (c.1200), chavel, chawl (late 14c.) → jowl, a late-16c. re-spelling with j- (attested from c.1400) under the influence of the synonymous Old French joue; Klein p.833 gives the same chain and adds the Avestan comparandum. chafer 'a beetle': Old English ceafor, ceafer → Middle English chafer, from Germanic *kabraz literally 'gnawer' — the insect named from its chewing, and preserved today mainly in cockchafer; Klein p.264/265 spells this out ('rel. to OS. kevera, Du. kever, OHG. chevar, MHG. kever, G. Käfer, lit. \\\"gnawer\\\". Cp. MHG. kiven, Du. keveren, \\\"to gnaw\\\" … and see jowl, \\\"jaw\\\"'). Etymonline confirms the jowl chain and the PIE etymon: 'from Proto-Germanic *kefalaz … from PIE *gep(h)- \\\"jaw, mouth\\\" (cognates: Old Irish gop, Irish gob \\\"beak, mouth\\\")'. Both of Nourai's page references are exact.\",\n          \"derivation_fa\": \"هر دو واژهٔ انگلیسی به‌راستی از این ریشه‌اند، ولی از راه دو ستاکِ متفاوتِ ژرمنی. «jowl» به معنای «آرواره»: انگلیسی کهنِ متأخر ceafl «آرواره، گونه، استخوان آرواره» > انگلیسی میانه chafle (حدود ۱۲۰۰)، chavel، chawl (اواخر سدهٔ چهاردهم) > jowl، با املای j از اواخر سدهٔ شانزدهم (گواهی‌شده از حدود ۱۴۰۰) به تأثیر واژهٔ هم‌معنای فرانسهٔ کهن joue. کلاین در رویهٔ ۸۳۳ همین زنجیره را می‌آورد و هم‌ریشهٔ اوستایی را نیز می‌افزاید. «chafer» به معنای «سوسک»: انگلیسی کهن ceafor/ceafer > انگلیسی میانه chafer، از ژرمنیِ *kabraz که لفظاً «جونده» است — نامِ حشره از جویدنش گرفته شده و امروز بیشتر در ترکیب cockchafer مانده است؛ کلاین در رویهٔ ۲۶۴/۲۶۵ آن را می‌شکافد. اتیمآنلاین زنجیرهٔ jowl و ریشهٔ هندواروپایی‌اش را تأیید می‌کند: «از ژرمنیِ آغازین *kefalaz … از هندواروپایی *gep(h)- \\\"آرواره، دهان\\\" (هم‌ریشه‌ها: gop ایرلندی کهن، gob ایرلندی \\\"منقار، دهان\\\")». هر دو شمارهٔ صفحه‌ای که نورایی داده دقیقاً درست است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/jowl\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:264\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.7112; the leaf carries the printed page markers 264 (l.7106) and 265 (l.7107) immediately above the entry: 'chafer, n., a beetle. — ME., fr. OE. ceafor, rel. to OS. kevera, Du. kever, OHG. chevar, MHG. kever, G. Käfer, lit. \\\"gnawer\\\". Cp. MHG. kiven, Du. keveren, \\\"to gnaw\\\", OE. ceafl, ME. chavel, G. Kiefer, \\\"jaw\\\", and see jowl, \\\"jaw\\\".'\"},\n            {\"ref\": \"KLN:833\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.20399, printed p.833: 'jowl, n., jaw. — ME. chawl, chavel, cholle, fr. OE. ceafl, \\\"jaw\\\", rel. to MHG. kiver, kivel, G. Kiefer, ON. kjaptr, \\\"jaw\\\", and cogn. with OIr. gop, Ir. gob, \\\"beak, mouth\\\", Avestic zafar-, \\\"mouth, gullet\\\". Cp. chafer, \\\"beetle\\\".'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.492, s.v. gep(h)-\", \"stance\": \"supports\", \"note\": \"'2. Germanic *kabraz, \\\"gnawer\\\", in Old English ceafor, ceafer, beetle: CHAFER; (COCKCHAFER). 3. Germanic *kēfalaz in Old English céafl, jaw, cheek: JOWL.'\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/jowl\", \"stance\": \"supports\", \"note\": \"'jowl (n.1) \\\"jaw, jawbone\\\", especially the underjaw, a late 16c. alteration of Middle English chawl (late 14c.), earlier chafle (c. 1200), from late Old English ceafl \\\"jaw; cheek; jawbone; cheekbone\\\", from Proto-Germanic *kefalaz … from PIE *gep(h)- \\\"jaw, mouth\\\" … The spelling with j-, attested from c. 1400, is perhaps from influence of the synonymous Old French joue.'\"},\n            {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt l.54295, Bd. I 571\", \"stance\": \"supports\", \"note\": \"'dehnstufig … as. cafl, ags. ceafl (engl. jowl, jole) \\\"Kiefer\\\"' — Walde-Pokorny name the English word explicitly.\"},\n            {\"src\": \"SYN\", \"where\": \"SYN.txt l.5792, Buck 4.207 p.221\", \"stance\": \"supports\", \"note\": \"'OE ceafl, ME chavel, NE jowl (in part) … : Av. zafar- \\\"mouth\\\" (of evil beings). Walde-P. 1.570 f. … NED s.v. jowl, sb.1.'\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-172.json > /dev/null && echo \"JSON OK\"",
 "description": "Write and validate page-172.json"
}
```


### [2026-09-05T21:08:30.093Z] TOOL RESULT

```
JSON OK
```


## [2026-09-05T21:08:35.293Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 tools/verify_check.py 172",
 "description": "Run verify_check for page 172"
}
```


### [2026-09-05T21:08:37.244Z] TOOL RESULT

```
nodes verified: 17/17
node verdicts: {'confirmed': 15, 'plausible': 2}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 24, 'not_checked': 3, 'partial': 1}
books consulted: {'supports': 47, 'partial': 3, 'contradicts': 1} | by book: {'WLD': 9, 'POK': 6, 'AHD': 6, 'BRT': 5, 'PHD': 4, 'SYN': 4, 'IEC': 3, 'NYB': 2, 'ARY': 2, 'Etymonline': 2, 'HUB': 2, 'SOD': 1, 'MON': 1, 'BQT': 1, 'HRN': 1, 'Wiktionary': 1, 'KLN': 1}
```


## [2026-09-05T21:08:49.923Z] TOOL CALL #66: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-172.json'\nd=json.load(open(p,encoding='utf-8'))\nn=d['entries'][1]['nodes'][1]\nn['sources']=[u for u in n['sources'] if 'D8%B2%D9%86%D8%AE' not in u]\njson.dump(d,io.open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)\nopen(p,'a',encoding='utf-8').write('\\n')\nEOF\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg172.png data/verification/sources/refs/ocr/BOOK/172.png\npython3 -m json.tool data/verification/page-172.json >/dev/null && python3 tools/verify_check.py 172",
 "description": "Clean sources, save page image, re-check"
}
```


### [2026-09-05T21:08:51.968Z] TOOL RESULT

```
nodes verified: 17/17
node verdicts: {'confirmed': 15, 'plausible': 2}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 24, 'not_checked': 3, 'partial': 1}
books consulted: {'supports': 47, 'partial': 3, 'contradicts': 1} | by book: {'WLD': 9, 'POK': 6, 'AHD': 6, 'BRT': 5, 'PHD': 4, 'SYN': 4, 'IEC': 3, 'NYB': 2, 'ARY': 2, 'Etymonline': 2, 'HUB': 2, 'SOD': 1, 'MON': 1, 'BQT': 1, 'HRN': 1, 'Wiktionary': 1, 'KLN': 1}
```


## [2026-09-05T21:09:10.149Z] AGENT

Page 172 (book p. 142) verified — `data/verification/page-172.json` written, `verify_check.py 172` shows 0 PROBLEM lines.

**Counts:** 3 roots confirmed; 17/17 nodes — 15 confirmed, 2 plausible, 0 disputed, 0 transcription_suspect. Ref checks: 24 supports, 1 partial, 3 not_checked (DZA:58 not digitised; two boxes carry no reference in the book).

**Plausible (no disputed items):**
- Geph/Gebh #2 Persian دهان/زفر — زفر is solid (Horn 663, Bartholomae, MacKenzie, Mo'in's footnote on the cited Borhān p.1024). دهان is contested: the classical route Av. *zafan-* → SW *dafan-* → MP/NP *dahān* is Bartholomae's and Nyberg's own (and Horn 589, Hübschmann), but ESIJa III 50 analyses MP *dahān* as *dam-fāzek* ("breath" + *faź*), and Wiktionary follows ESIJa while citing **this very page of Nourai** as the alternative theory.
- Geph/Gebh #3 Germanic "kabal / kaf" — *kaf-* 'to chew' is verbatim Watkins, but the jaw-word is reconstructed *kēfalaz* (Watkins 1985, etymonline) / lengthened-grade *kēf-* (WLD I 571), not "kabal"; and *chafer* actually descends from a third stem *kabraz* 'gnawer', so one box carries two stems.

**Extraction errors:** none. I rendered PDF p.172 and read it against the JSON — every box, arrow, form, gloss and reference matches (image saved to `data/verification/sources/refs/ocr/BOOK/172.png`).

**Notable findings:**
- BQT page offset for vol. 2 established as chunk + 537 (زانو 1000, زفر 1024, زنخ 1036 all land exactly), and all three Mo'in footnotes say what Nourai claims.
- SOD:184 is a *page* number, and it is right: Gharib's entry 4591 on p.184 gives "znuk … ©Av. znu; Pahl. šnwk — knee", supplying both the Avestan and the Sogdian box.
- Nourai's odd "žnu" is not a misprint — it is Mann's citation form (IEC s.v. ĝenu: "Av. žnu").
- گونیا is confirmed as a Greek loan (via Classical Syriac gōnyā) and an explicit doublet of زانو — Dehkhoda/Borhān say the same.
- HRN:148 is one page off: the zanax entry is no. 669 on printed p. 149.
- VIE:12 turned out to be checkable (VIE_pages.txt pdf p.18): Sajjadiyyeh lists "chin انگلیسی، چانه فارسی", supporting that arrow, though he wrongly files Turkish çene as a "Turanian" cognate.
